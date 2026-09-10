"""ATS fidelity gate.

Every document leaves this folder only after passing here. It answers one
question: when a parser reads this PDF, does it get back what a human sees?

Three graded checks, because the failure modes are not equally bad:

  TEXT RECALL     Does the content survive at all, ignoring whitespace noise
                  and cosmetic character swaps? Failure is fatal - the words
                  are gone and the document reads as blank.

  CHAR INTEGRITY  Do the exact codepoints survive? Failure is a silent keyword
                  killer. Measured on real output from this machine: LaTeX +
                  Cambria renders "filtering" with a ToUnicode map that
                  extracts as "ϐiltering" (U+03D0 GREEK BETA SYMBOL) and turns
                  every ASCII hyphen into U+2011, so "real-time" never matches
                  a search for "real-time". The page looks perfect.

  READING ORDER   Does the text layer run top-to-bottom?

Whitespace is stripped before comparison because extractors disagree on it
harmlessly: pypdf reads a kern as a space ("REST , WebSocket"), Chrome emits
tabs around "&". Neither breaks tokenization. Character swaps do.

Scored against every available extractor and reported at its WORST. Employers
run different parsers and you do not get to pick which one.

Usage:
    python -m engine.ats_check out/resume.pdf --expect out/resume.strings.json
    python -m engine.ats_check some.pdf --dump
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata

import pymupdf
import pypdf

# Cosmetic substitutions that do not destroy meaning for a human reader but do
# break exact keyword matching. Folding these separates "the text is missing"
# from "the text is present but spelled with odd glyphs".
FOLD = {
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "―": "-", "−": "-",
    "×": "x",
    "‘": "'", "’": "'", "“": '"', "”": '"',
    " ": " ", " ": " ", " ": " ",
    "ﬁ": "fi", "ﬂ": "fl", "ϐ": "fi",
    "•": "-", "·": "-",
}


def nows(s: str) -> str:
    """Strip all whitespace, keep exact codepoints."""
    return re.sub(r"\s+", "", s)


def folded(s: str) -> str:
    """Strip whitespace and normalize cosmetic character variants."""
    s = unicodedata.normalize("NFKC", s)
    for a, b in FOLD.items():
        s = s.replace(a, b)
    return nows(s).lower()


def _pypdf_text(path: str) -> str:
    return "\n".join((p.extract_text() or "") for p in pypdf.PdfReader(path).pages)


def _pymupdf_text(path: str) -> str:
    return "\n".join(p.get_text() for p in pymupdf.open(path))


def _pdfminer_text(path: str) -> str:
    from pdfminer.high_level import extract_text
    return extract_text(path)


# Three independent engines. pypdf and pdfminer are the pair that both failed
# on the archived LinkedIn export, which makes them a good regression check.
EXTRACTORS = {
    "pypdf": _pypdf_text,
    "pymupdf": _pymupdf_text,
    "pdfminer": _pdfminer_text,
}

# Characters allowed to appear in a shipped document. Anything outside this set
# is either a rendering defect or a glyph an ATS may mishandle.
ALLOWED_EXTRA = set("–—‘’“”•·× ")

# Codepoints that are specifically evidence of a broken pipeline. Each of these
# was observed in real output during the pipeline bakeoff or in the LinkedIn
# export, and each is invisible on the page.
DANGEROUS = {
    "­": "soft hyphen - splits words for a parser",
    "‐": "word-internal U+2010 hyphen - will not match an ASCII-hyphen search",
    "‑": "non-breaking hyphen - LaTeX/Cambria emits this for every '-'",
    ";": "Greek question mark - LaTeX emits this for ';'",
    "ϐ": "Greek beta symbol - LaTeX/Cambria emits this for the 'fi' ligature",
    "�": "replacement character - an encoding error",
}


def audit_codepoints(text: str) -> list[str]:
    """Flag dangerous or unexpected characters without needing a source to
    compare against. Works on any PDF, including ones this system did not make."""
    problems = []
    for ch, why in DANGEROUS.items():
        n = text.count(ch)
        if n:
            problems.append(f"U+{ord(ch):04X} x{n}: {why}")
    # Presentation-form ligatures: a parser sees one glyph, not two letters.
    lig = [c for c in text if "ﬀ" <= c <= "ﬆ"]
    if lig:
        problems.append(f"presentation ligatures x{len(lig)} (U+FB00-FB06): "
                        "'fi'/'fl' stored as single glyphs")
    # Private Use Area: icon fonts, which extract as meaningless characters.
    pua = [c for c in text if "" <= c <= ""]
    if pua:
        problems.append(f"private-use characters x{len(pua)}: icon font in the text layer")
    exotic = {c for c in text
              if ord(c) > 127 and c not in ALLOWED_EXTRA and c not in DANGEROUS
              and not ("ﬀ" <= c <= "ﬆ") and not ("" <= c <= "")}
    if exotic:
        shown = ", ".join(f"U+{ord(c):04X} ({c})" for c in sorted(exotic)[:8])
        problems.append(f"{len(exotic)} unexpected non-ASCII character(s): {shown}")
    return problems


def inspect_fonts(path: str) -> list[dict]:
    """Per font: is the program embedded, and can glyphs map back to characters?

    A subset font with no ToUnicode CMap extracts as glyph indices - that is
    what makes the archived LinkedIn exports in this repo unreadable.
    """
    seen: dict[str, dict] = {}
    for page in pypdf.PdfReader(path).pages:
        res = page.get("/Resources")
        if res is None:
            continue
        fonts = res.get_object().get("/Font")
        if fonts is None:
            continue
        for _, ref in fonts.get_object().items():
            f = ref.get_object()
            base = str(f.get("/BaseFont", "?"))
            if base in seen:
                continue
            desc = f.get("/FontDescriptor")
            if desc is None and "/DescendantFonts" in f:
                desc = f["/DescendantFonts"].get_object()[0].get_object().get("/FontDescriptor")
            desc = desc.get_object() if desc is not None else {}
            seen[base] = {
                "font": base.lstrip("/"),
                "subtype": str(f.get("/Subtype", "?")).lstrip("/"),
                "embedded": any(k in desc for k in ("/FontFile", "/FontFile2", "/FontFile3")),
                "subset": bool(re.match(r"^/?[A-Z]{6}\+", base)),
                "to_unicode": "/ToUnicode" in f,
            }
    return list(seen.values())


TOKEN_RX = re.compile(r"[A-Za-z0-9][A-Za-z0-9+#./_-]*")


def _fold_keep_space(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    for a, b in FOLD.items():
        s = s.replace(a, b)
    return s


def tokenize(s: str) -> list[str]:
    """Words as a keyword search sees them. "Node.js" and "C++" stay whole."""
    return [t.strip(".-/_").lower()
            for t in TOKEN_RX.findall(_fold_keep_space(s)) if t.strip(".-/_")]


def _score_extraction(text: str, expected: list[str]) -> dict:
    """Score one extraction on three axes.

    TOKEN recall is the one that decides pass/fail. It asks the question a
    recruiter's keyword search asks: is the word in the document at all?

    PHRASE recall additionally requires the words to stay contiguous. This is
    a stricter bar than most parsers hold themselves to - pdfminer.six, with
    default layout analysis, reads right-aligned dates as a second column and
    splices them into a wrapping bullet. Every keyword survives; only the run
    is broken. So phrase failures are reported, not fatal.
    """
    # Case is folded throughout: the template intentionally upper-cases section
    # headings, and keyword search is case-insensitive anyway.
    t_nows, t_fold = nows(text).lower(), folded(text)
    t_tokens = set(tokenize(text))
    lost_tokens, lost_phrases, mangled = [], [], []
    cursor = order_ok = order_total = 0

    for s in expected:
        s_fold = folded(s)
        if not s_fold:
            continue

        # A token also counts as present when it survives in the
        # whitespace-stripped text. Typst breaks a long hyphenated compound
        # across lines ("Ctrl+F-\nand-edit"), which splits the token without
        # losing a single character.
        missing = [tok for tok in tokenize(s)
                   if tok not in t_tokens and tok not in t_nows]
        if missing:
            lost_tokens.append(f"{s[:60]} -> missing {missing[:6]}")

        if s_fold not in t_fold:
            lost_phrases.append(s)
            continue
        if nows(s).lower() not in t_nows:
            mangled.append(s)
        order_total += 1
        idx = t_fold.find(s_fold, cursor)
        if idx >= 0:
            order_ok += 1
            cursor = idx + len(s_fold)

    n = sum(1 for s in expected if folded(s))
    return {
        "token_recall": round((n - len(lost_tokens)) / n, 4) if n else 1.0,
        "text_recall": round((n - len(lost_phrases)) / n, 4) if n else 1.0,
        "char_integrity": round((n - len(lost_phrases) - len(mangled)) / n, 4) if n else 1.0,
        "order": round(order_ok / order_total, 4) if order_total else None,
        "lost_tokens": lost_tokens,
        "lost": lost_phrases,
        "mangled": mangled,
    }


def check(path, expected: list[str], max_pages: int | None = None,
          check_fill: bool = True) -> dict:
    """Score a PDF. Returns a result dict; 'verdict' is PASS / WARN / FAIL."""
    path = str(path)
    result: dict = {"file": path, "per_extractor": {}}

    scores, texts = {}, {}
    for name, fn in EXTRACTORS.items():
        try:
            text = fn(path)
        except Exception as exc:
            text, result[f"{name}_error"] = "", repr(exc)
        texts[name] = text
        scores[name] = _score_extraction(text, expected)
        result["per_extractor"][name] = {
            "chars": len(text),
            **{k: scores[name][k]
               for k in ("token_recall", "text_recall", "char_integrity", "order")},
        }

    richest = max(texts, key=lambda k: len(texts[k]))
    result["codepoint_problems"] = audit_codepoints(texts[richest])

    worst = min(scores, key=lambda k: (scores[k]["token_recall"],
                                       scores[k]["char_integrity"]))
    s = scores[worst]
    result.update({
        "worst_extractor": worst,
        "token_recall": s["token_recall"],
        "text_recall": s["text_recall"],
        "char_integrity": s["char_integrity"],
        "order_score": s["order"],
        "lost_tokens": s["lost_tokens"],
        "lost": s["lost"],
        "mangled": s["mangled"],
    })
    # Phrase/order problems that appear in only one engine are that engine's
    # layout analysis, not a defect in the file.
    result["phrase_split_engines"] = [
        k for k, v in scores.items() if v["text_recall"] < 1.0]

    fonts = inspect_fonts(path)
    result["fonts"] = fonts
    result["font_risk"] = [f["font"] for f in fonts if f["subset"] and not f["to_unicode"]]
    result["unembedded"] = [f["font"] for f in fonts if not f["embedded"]]

    with pymupdf.open(path) as doc:
        result["pages"] = doc.page_count
        result["metadata"] = {k: v for k, v in (doc.metadata or {}).items() if v}
        result["size_kb"] = round(os.path.getsize(path) / 1024, 1)

        # How much of the last page the content actually reaches. A resume that
        # stops halfway down looks thin, and the fix is content, not typography.
        last = doc[doc.page_count - 1]
        blocks = [b for b in last.get_text("blocks") if b[4].strip()]
        result["fill_ratio"] = (round(max(b[3] for b in blocks) / last.rect.height, 3)
                                if blocks else 0.0)

    fatal, warn = [], []
    if s["token_recall"] < 1.0:
        fatal.append(f"{len(s['lost_tokens'])} lines lost keywords entirely (per {worst})")
    if result["font_risk"]:
        fatal.append(f"subset font with no ToUnicode CMap: {result['font_risk']}")
    # The 14 standard PDF fonts are guaranteed present in every reader, so they
    # still extract; they just render with whatever substitute the viewer picks.
    base14 = {"Helvetica", "Times-Roman", "Times-Bold", "Times-Italic",
              "Times-BoldItalic", "Courier", "Symbol", "ZapfDingbats"}
    unembedded_risky = [f for f in result["unembedded"]
                        if f.split("+")[-1].split(",")[0] not in base14]
    if unembedded_risky:
        fatal.append(f"font not embedded: {unembedded_risky}")
    elif result["unembedded"]:
        warn.append(f"standard-14 fonts not embedded ({result['unembedded']}); "
                    "text extracts fine but the document renders with whatever "
                    "substitute the reader's viewer picks")
    if len(result["phrase_split_engines"]) == len(scores) and s["text_recall"] < 1.0:
        fatal.append("every engine broke the text into fragments")
    elif result["phrase_split_engines"]:
        warn.append(f"{result['phrase_split_engines']} split some lines into fragments "
                    "(layout analysis reading right-aligned dates as a column); "
                    "keywords all survive")
    if max_pages is not None and result["pages"] > max_pages:
        fatal.append(f"{result['pages']} pages, budget is {max_pages}")
    for p in result["codepoint_problems"]:
        fatal.append(f"codepoint audit - {p}")
    if result["size_kb"] > 1000:
        warn.append(f"{result['size_kb']} KB; Handshake caps uploads at 1 MB")
    # Page fill matters for a resume, where blank space is wasted opportunity.
    # It is meaningless for a cover letter: a 238-word letter that fills the
    # page would be a 238-word letter in 24pt type.
    if check_fill and result["fill_ratio"] < 0.75:
        warn.append(f"content reaches only {result['fill_ratio']:.0%} down the last page; "
                    "it will read as thin - add content rather than loosening type")
    creator = (result["metadata"].get("creator", "") + " "
               + result["metadata"].get("producer", ""))
    leaky = [t for t in ("HeadlessChrome", "Skia/PDF", "Mozilla", "WeasyPrint")
             if t.lower() in creator.lower()]
    if leaky:
        warn.append(f"metadata names the rendering tool: {leaky}")
    if s["mangled"]:
        warn.append(f"{len(s['mangled'])} strings had characters substituted; "
                    "exact keyword search will miss them")

    result["problems"], result["warnings"] = fatal, warn
    result["verdict"] = "FAIL" if fatal else ("WARN" if warn else "PASS")
    return result


def format_report(r: dict) -> str:
    out = [
        f"{r['verdict']}  {os.path.basename(r['file'])}",
        f"  token recall    {r['token_recall']:.3f}   <- the one that gates "
        f"(worst parser: {r['worst_extractor']})",
        f"  phrase recall   {r['text_recall']:.3f}",
        f"  char integrity  {r['char_integrity']:.3f}",
        f"  reading order   {r['order_score'] if r['order_score'] is not None else 'n/a'}",
        f"  pages {r['pages']}   size {r['size_kb']} KB",
    ]
    for p in r["problems"]:
        out.append(f"  FATAL: {p}")
    for p in r["warnings"]:
        out.append(f"  WARN:  {p}")
    for f in r["fonts"]:
        flag = "   <-- RISK" if f["subset"] and not f["to_unicode"] else ""
        out.append(f"  font {f['font']:<30} embedded={f['embedded']!s:<5} "
                   f"toUnicode={f['to_unicode']!s:<5}{flag}")
    for c in r.get("codepoint_problems", []):
        out.append(f"  codepoint: {c}")
    for label, items in (("LOST KEYWORDS", r.get("lost_tokens", [])),
                         ("SPLIT PHRASES", r["lost"]),
                         ("MANGLED", r["mangled"])):
        if items:
            out.append(f"  {label} ({len(items)}):")
            out += [f"    - {m[:90]}" for m in items[:8]]
    if r.get("metadata"):
        out.append(f"  metadata: {r['metadata']}")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="ATS fidelity gate for generated PDFs.")
    ap.add_argument("pdf", nargs="+")
    ap.add_argument("--expect", help="JSON file: list of strings that must survive")
    ap.add_argument("--max-pages", type=int, default=None)
    ap.add_argument("--dump", action="store_true", help="print the extracted text layer")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.dump:
        for p in args.pdf:
            print("=" * 78, f"\n{p}\n", "=" * 78, sep="")
            for i, page in enumerate(pymupdf.open(p)):
                print(f"--- page {i + 1} ---\n{page.get_text()}")
        return 0

    expected = json.load(open(args.expect, encoding="utf-8")) if args.expect else []
    if not expected:
        print("No --expect strings given; running structural checks only "
              "(fonts, pages, metadata). Text fidelity NOT verified.", file=sys.stderr)

    worst = 0
    for p in args.pdf:
        r = check(p, expected, max_pages=args.max_pages)
        print(json.dumps(r, indent=2) if args.json else format_report(r))
        worst = max(worst, {"PASS": 0, "WARN": 1, "FAIL": 2}[r["verdict"]])
    return worst


if __name__ == "__main__":
    sys.exit(main())

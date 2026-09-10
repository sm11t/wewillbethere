"""Build a variant, push it to resume.lol, export a PDF, and gate it.

    python -m engine.publish swe-intern --draft
    python -m engine.publish swe-intern --draft --open

Steps:
  1. assemble the document from approved facts        (engine.build)
  2. render it as resume.lol markdown + CSS           (engine.emit_rlol)
  3. create or update the resume in the account       (engine.rlol_client)
  4. pull the self-contained HTML export
  5. print it to PDF with headless Chrome
  6. verify the PDF's text layer against the source   (engine.ats_check)

Step 6 matters more here than with a local renderer: the PDF now comes out of a
browser print, so the text layer is whatever Chrome and PagedJS decided to make.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys
import tempfile

import pymupdf

from . import (ai_lint, ats_check, build, emit_rlol,
               profile as profile_mod, render)
from . import rlol_client as rlol

ROOT = pathlib.Path(__file__).parents[1]
# Intermediates live out of sight. Only finished PDFs are user-facing,
# and those are placed by engine.package into applications/<slug>/.
OUT = ROOT / "out" / ".build"
REGISTRY = ROOT / "out" / "rlol-resumes.json"

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def _chrome() -> str:
    for path in CHROME_CANDIDATES:
        if pathlib.Path(path).exists():
            return path
    raise SystemExit("No Chrome or Edge found for PDF export.")


def _registry() -> dict:
    if REGISTRY.exists():
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {}


def _save_registry(reg: dict) -> None:
    OUT.mkdir(exist_ok=True)
    REGISTRY.write_text(json.dumps(reg, indent=2), encoding="utf-8")


def push(preset: str, markdown: str, css: str, meta_css: str) -> str:
    """Create the resume on first run, update it thereafter. Returns its id."""
    reg = _registry()
    entry = reg.get(preset)

    if entry:
        current = rlol.get_resume(entry["id"])
        rlol.update_resume(entry["id"], markdown=markdown, css=css,
                           meta_css=meta_css,
                           expected_updated_at=current.get("updated_at"))
        resume_id = entry["id"]
    else:
        created = rlol.create_resume(f"Asmit Datta - {preset}", markdown=markdown,
                                     css=css, meta_css=meta_css)
        resume_id = created.get("id") or created.get("resume_id")
        if not resume_id:
            raise SystemExit(f"create_resume returned no id: {created}")

    reg[preset] = {"id": resume_id, "name": f"Asmit Datta - {preset}"}
    _save_registry(reg)
    return resume_id


def _print_html(html: str, stem: str, budget_ms: int = 15000) -> pathlib.Path:
    """Snapshot an HTML file to PDF with headless Chrome.

    The budget is generous on purpose. resume.lol embeds Paged.js and paginates
    in JavaScript; at 20s the snapshot fired before pagination finished and
    produced a blank page.

    Each run gets a throwaway profile directory. Without one, launching Chrome
    several times in quick succession (as the fit search does) hits profile
    lock contention and silently yields an empty PDF.
    """
    OUT.mkdir(exist_ok=True)
    html_path = OUT / (stem + ".html")
    pdf_path = OUT / (stem + ".pdf")
    html_path.write_text(html, encoding="utf-8")
    pdf_path.unlink(missing_ok=True)

    with tempfile.TemporaryDirectory(prefix="rlol-chrome-") as profile:
        subprocess.run([
            _chrome(), "--headless=new", "--disable-gpu", "--no-sandbox",
            "--no-first-run", "--no-default-browser-check",
            f"--user-data-dir={profile}",
            "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
            f"--virtual-time-budget={budget_ms}",
            f"--print-to-pdf={pdf_path}", html_path.as_uri(),
        ], capture_output=True, text=True, timeout=300)

    if not pdf_path.exists():
        raise SystemExit("Chrome produced no PDF.")
    return pdf_path


def _measure(pdf_path: pathlib.Path) -> tuple[int, int]:
    """(page count, characters of extracted text) for a rendered PDF."""
    with pymupdf.open(str(pdf_path)) as doc:
        text = "".join(page.get_text() for page in doc)
        return doc.page_count, len(text.strip())


def _printable_html(html: str, css: str, meta_css: str) -> str:
    """Rebuild the export as a plain document Chrome can paginate itself.

    The resume.lol export embeds Paged.js (about 500 KB) in the head and calls
    window.print() once it finishes laying out. That is right for a person
    clicking Save as PDF, but under headless --print-to-pdf it is a race: the
    snapshot lands before or after pagination unpredictably, and the same input
    produced a full page on one run and a blank one on the next.

    The body of the export is already clean semantic HTML, and the @page rule
    tells Chrome everything it needs. Dropping Paged.js and letting Chrome
    paginate natively makes the output deterministic and renders in about a
    second instead of four. resume.lol stays the source of truth for content
    and styling; only the print step is local.
    """
    NL = chr(10)
    body_start = html.index("<body")
    body_open_end = html.index(">", body_start) + 1
    body_end = html.rindex("</body>")
    content = html[body_open_end:body_end]

    base_css = ""
    for match in re.finditer(r"<style[^>]*>(.*?)</style>", html, re.S):
        block = match.group(1)
        if "--ink" not in block and "@page" not in block[:200]:
            base_css = block
            break

    return (
        "<!DOCTYPE html>" + NL
        + '<html><head><meta charset="utf-8">' + NL
        + "<title>Resume</title>" + NL
        + "<style>" + base_css + "</style>" + NL
        + "<style>" + meta_css + "</style>" + NL
        + "<style>" + css + "</style>" + NL
        + "</head><body>" + content + "</body></html>" + NL
    )


def fit_to_one_page(html: str, stem: str, max_pages: int = 1):
    """Choose a density. Returns (pdf_path, scale, margin, attempts).

    Two rules, in order:

      1. Fewer pages always wins. A one-page resume beats a two-page one even
         when the budget allows two, so the search keeps tightening past the
         first rung that merely fits.
      2. Among rungs that reach the same page count, the loosest wins - the
         type stays as large as that page count allows.

    Walking loosest to tightest makes page count non-increasing, so the first
    rung at a given count is also the loosest one at that count.

    A rung counts only if it produced real text. A blank page is one page, and
    an earlier version of this loop accepted an empty PDF as a perfect fit.
    """
    attempts = []
    best = None            # (pages, scale, margin, path)

    for scale, margin, spacing in emit_rlol.LADDER:
        styled = _printable_html(html, emit_rlol.css(scale, spacing),
                                 emit_rlol.meta_css(margin))
        pdf_path = _print_html(styled, stem)
        pages, chars = _measure(pdf_path)

        if chars < 200:
            pdf_path = _print_html(styled, stem, budget_ms=45000)
            pages, chars = _measure(pdf_path)
            if chars < 200:
                raise SystemExit("Chrome rendered a blank page twice.")

        attempts.append({"scale": scale, "margin": margin, "spacing": spacing,
                         "pages": pages, "chars": chars})

        if pages <= max_pages and (best is None or pages < best[0]):
            best = (pages, scale, margin, spacing)
            _print_html(styled, stem + "-best")
        if best is not None and best[0] == 1:
            break          # cannot do better than one page

    if best is None:
        tightest = attempts[-1]
        raise SystemExit(
            f"Does not fit {max_pages} page(s) even at the tightest setting "
            f"(scale {tightest['scale']}, margin {tightest['margin']}in -> "
            f"{tightest['pages']} pages). Cut content rather than shrink further.")

    pages, scale, margin, spacing = best
    # Re-render the winner so the artifact on disk is the chosen one.
    styled = _printable_html(html, emit_rlol.css(scale, spacing),
                             emit_rlol.meta_css(margin))
    pdf_path = _print_html(styled, stem)
    (OUT / (stem + "-best.pdf")).unlink(missing_ok=True)
    (OUT / (stem + "-best.html")).unlink(missing_ok=True)
    return pdf_path, scale, margin, spacing, attempts


def main() -> int:
    ap = argparse.ArgumentParser(description="Publish a variant via resume.lol.")
    ap.add_argument("preset")
    ap.add_argument("--draft", action="store_true",
                    help="include phrasings not yet approved")
    ap.add_argument("--open", action="store_true", help="open the PDF when done")
    args = ap.parse_args()

    prof = profile_mod.load()
    doc, notes = build.build_document(prof, args.preset, draft=args.draft)
    preset_cfg = build.load_presets()["presets"][args.preset]
    max_pages = preset_cfg.get("max_pages", 1)
    one_line_skills = preset_cfg.get("one_line_skills", True)
    stem = f"asmit-{args.preset}"

    def push_and_fetch(document, scale_hint, margin_hint, spacing_hint=1.0):
        """Trim the skills for a given density, store it, and pull the HTML."""
        d = dict(document)
        dropped = []
        if one_line_skills and d.get("skills"):
            d["skills"], dropped = emit_rlol.fit_skills_to_one_line(
                document["skills"], scale_hint, margin_hint)
        rid = push(args.preset, emit_rlol.to_markdown(d),
                   emit_rlol.css(scale_hint, spacing_hint),
                   emit_rlol.meta_css(margin_hint))
        return rid, rlol.get_resume_html(rid), d, dropped

    # First pass at a middle density to discover what actually fits, then a
    # second pass so the skill lines are trimmed for the density finally used.
    resume_id, html, _, _ = push_and_fetch(doc, 0.90, 0.48, 0.86)
    _, scale, margin, spacing, attempts = fit_to_one_page(
        html, stem, max_pages=max_pages)

    resume_id, html, doc, dropped_skills = push_and_fetch(
        doc, scale, margin, spacing)
    styled = _printable_html(html, emit_rlol.css(scale, spacing),
                             emit_rlol.meta_css(margin))
    pdf_path = _print_html(styled, stem)

    print(f"resume.lol id: {resume_id}")
    print(f"  fit: scale {scale}, spacing {spacing}, margin {margin}in "
          f"after {len(attempts)} render(s)")
    if dropped_skills:
        print(f"  skills trimmed to one line each; dropped "
              f"{len(dropped_skills)}: {', '.join(dropped_skills)}")

    # Chrome stamps "HeadlessChrome" and "Skia/PDF" into the document info.
    render.set_metadata(pdf_path, title=f"{doc['name']} - Resume",
                        author=doc["name"])

    expected = emit_rlol.expected_strings(doc)
    (OUT / (stem + ".expect.json")).write_text(
        json.dumps(expected, indent=2, ensure_ascii=False), encoding="utf-8")

    report = ats_check.check(pdf_path, expected, max_pages=max_pages)
    print(f"  {pdf_path.name}  {pdf_path.stat().st_size // 1024} KB")
    print(f"  ATS: {report['verdict']}  token recall {report['token_recall']:.3f}"
          f"  char integrity {report['char_integrity']:.3f}"
          f"  pages {report['pages']}  fill {report['fill_ratio']:.0%}")
    for problem in report["problems"]:
        print(f"    FATAL: {problem}")
    for warning in report["warnings"]:
        print(f"    WARN:  {warning}")
    for lost in report["lost_tokens"][:5]:
        print(f"      lost: {lost}")

    bullets = [b for sec in doc["sections"] for e in sec["entries"]
               for b in e["bullets"]]
    findings = ai_lint.lint(chr(10).join("- " + b for b in bullets))
    counts = {"block": 0, "warn": 0, "note": 0}
    for f in findings:
        counts[f.severity] += 1
    print(f"  voice lint: {counts['block']} block, {counts['warn']} warn, "
          f"{counts['note']} note")

    # The unconfirmed note is computed before the skill lines are trimmed, so
    # recompute it against what actually reached the page.
    on_page = {n for _, v in doc.get("skills", []) for n in v.split(", ")}
    live = [n for n in prof.unconfirmed_skills() if n in on_page]
    notes = [n for n in notes if not n.startswith("ON THE PAGE BUT UNCONFIRMED")]
    if live:
        notes.append("ON THE PAGE BUT UNCONFIRMED - be ready to be interviewed "
                     "on each, or cut it: " + ", ".join(live) + ".")

    if notes:
        print()
        print("Notes:")
        for n in notes:
            print(f"  - {n}")
    if args.draft:
        print()
        print("DRAFT: contains phrasings you have not approved. Do not send.")

    if args.open:
        subprocess.run(["cmd", "/c", "start", "", str(pdf_path)], check=False)

    return 0 if report["verdict"] != "FAIL" and counts["block"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

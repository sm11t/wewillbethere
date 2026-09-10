"""Document -> Typst -> PDF, with auto-fit, metadata control, and an ATS gate.

Typst was chosen by measurement, not preference. See docs/pdf-pipeline-bakeoff.md:
it was the only pipeline scoring 1.000 on both text recall and character
integrity while fitting one page, and it installs as a pure pip package.

The renderer deliberately knows nothing about tailoring. It takes an already
assembled document and turns it into a file. Choosing *what* goes in the
document is a separate job (tailor.py) so that selection logic and typography
never tangle.

Document shape:

    {
      "name": "Asmit Datta",
      "contact": ["New York, NY", "asmit77@icloud.com", ...],
      "sections": [
        {"heading": "EXPERIENCE",
         "entries": [
           {"left": "Software Engineer Intern", "right": "Aug 2025 - Apr 2026",
            "left2": "WatchDNA", "right2": "Remote",
            "bullets": ["...", "..."]},
         ]},
      ],
      "skills": [["Languages", "TypeScript, Python, ..."], ...],
    }
"""

from __future__ import annotations

import pathlib
import re

import pymupdf
import pypdf
import typst

from . import ats_check

# Loosest first. Stop at the first rung that fits so the page stays as open as
# it can be; a resume that has been squeezed to 9pt looks squeezed.
DENSITY_LADDER = [
    ("10.5pt", "0.66em"), ("10.5pt", "0.60em"),
    ("10pt", "0.62em"), ("10pt", "0.58em"), ("10pt", "0.54em"),
    ("9.5pt", "0.58em"), ("9.5pt", "0.54em"), ("9.5pt", "0.50em"),
    ("9pt", "0.52em"), ("9pt", "0.48em"),
]

# Cambria: ships with Windows, designed for screen and print, and reads as a
# deliberate choice rather than a default. Georgia and Libertinus are fallbacks
# so the file still builds on a machine without it.
FONT_STACK = ('"Cambria", "Georgia", "Libertinus Serif"')


class RenderError(RuntimeError):
    pass


def _esc(s: str) -> str:
    """Escape Typst markup characters."""
    for a, b in [("\\", "\\\\"), ("#", "\\#"), ("$", "\\$"), ("*", "\\*"),
                 ("_", "\\_"), ("@", "\\@"), ("<", "\\<"), (">", "\\>"),
                 ("[", "\\["), ("]", "\\]")]:
        s = s.replace(a, b)
    return s


# A token that a layout engine may break at an internal hyphen: long, and
# containing a hyphen or plus. "Ctrl+F-and-edit" and "voice-to-SQL" qualify.
_FRAGILE = re.compile(r"\S*[-+]\S*")


def _protect(s: str) -> str:
    """Escape, then keep fragile compounds on one line.

    Measured failure this prevents: Typst broke "Ctrl+F-and-edit" after the
    hyphen, and pdfminer then inserted the right-aligned date block between the
    two halves, leaving "ctrl+f-" and "and-edit" separated by "May 2024 - Aug
    2024" in the text layer. The keyword became unfindable. Wrapping the token
    in a box forbids the internal break, so it moves to the next line whole.
    """
    out = []
    for word in s.split(" "):
        esc = _esc(word)
        if len(word) > 10 and _FRAGILE.fullmatch(word):
            out.append(f"#box[{esc}]")
        else:
            out.append(esc)
    return " ".join(out)


def _preamble(size: str, leading: str, title: str, author: str) -> str:
    return f'''#set document(title: "{title}", author: "{author}")
#set page(paper: "us-letter", margin: (x: 0.6in, top: 0.5in, bottom: 0.5in))
#set text(font: ({FONT_STACK}), size: {size}, lang: "en", hyphenate: false)
#set par(justify: false, leading: {leading}, spacing: {leading})
#show link: set text(fill: rgb("#12408f"))

#let sechead(t) = block(above: 0.85em, below: 0.42em)[
  #text(size: 1.02em, weight: "bold", tracking: 0.06em)[#upper(t)]
  #v(-0.62em)
  #line(length: 100%, stroke: 0.55pt + rgb("#444444"))
]
#let row(l, r) = block(above: 0.55em, below: 0.10em, width: 100%)[
  #grid(columns: (1fr, auto), align: (left, right), l, r)
]
#let subrow(l, r) = block(above: 0.10em, below: 0.16em, width: 100%)[
  #grid(columns: (1fr, auto), align: (left, right), l, r)
]
// Bullets need more air between them than their own wrapped lines have,
// or a two-line bullet reads as two separate points.
#let pt(body) = block(above: 0.34em, below: 0.02em, width: 100%)[
  #grid(columns: (0.70em, 1fr), gutter: 0pt, align: (left, left),
    text[#sym.bullet], body)
]
'''


def build_typst(doc: dict, size="10pt", leading="0.58em") -> str:
    """Render the document structure to Typst markup.

    hyphenate:false is not cosmetic. Hyphenation inserts a real hyphen
    character into the text layer at every line break, so "companion" extracts
    as "com-panion" and stops matching a keyword search.
    """
    name = doc.get("name", "")
    L = [_preamble(size, leading, doc.get("title", f"{name} - Resume"), name)]

    L.append(f'#align(center)[\n  #text(size: 19pt, weight: "bold")[{_esc(name)}]\n]')
    L.append("#v(0.15em)")
    contact = "  #h(0.35em) | #h(0.35em)  ".join(_esc(c) for c in doc.get("contact", []))
    L.append(f'#align(center)[\n  #text(size: 9pt)[{contact}]\n]')

    for sec in doc.get("sections", []):
        L.append(f'#sechead[{_esc(sec["heading"])}]')
        for e in sec.get("entries", []):
            if e.get("left") or e.get("right"):
                L.append(f'#row([*{_esc(e.get("left",""))}*], [{_esc(e.get("right",""))}])')
            if e.get("left2") or e.get("right2"):
                L.append(f'#subrow([_{_esc(e.get("left2",""))}_], '
                         f'[_{_esc(e.get("right2",""))}_])')
            for b in e.get("bullets", []):
                L.append(f'#pt[{_protect(b)}]')

    if doc.get("skills"):
        L.append("#sechead[SKILLS]")
        for k, v in doc["skills"]:
            L.append(f'#block(above: 0.30em, below: 0.02em)[*{_esc(k)}:* {_esc(v)}]')

    return "\n".join(L)


def expected_strings(doc: dict) -> list[str]:
    """Every string that must survive into the PDF text layer."""
    out = [doc.get("name", "")] + list(doc.get("contact", []))
    for sec in doc.get("sections", []):
        out.append(sec["heading"])
        for e in sec.get("entries", []):
            out += [e.get(k, "") for k in ("left", "right", "left2", "right2")]
            out += e.get("bullets", [])
    for k, v in doc.get("skills", []):
        out += [k, v]
    return [s for s in out if s]


def set_metadata(path, title, author, subject="", keywords=""):
    """Own the Info dictionary rather than shipping whatever the tool wrote.

    Typst stamps Creator="Typst 0.15.0" and a UTC timestamp. Harmless, but the
    pipeline should decide what the file says about itself.
    """
    reader = pypdf.PdfReader(str(path))
    writer = pypdf.PdfWriter()
    writer.append_pages_from_reader(reader)
    meta = {"/Title": title, "/Author": author, "/Producer": "", "/Creator": ""}
    if subject:
        meta["/Subject"] = subject
    if keywords:
        meta["/Keywords"] = keywords
    writer.add_metadata(meta)
    tmp = pathlib.Path(str(path) + ".tmp")
    with open(tmp, "wb") as fh:
        writer.write(fh)
    tmp.replace(path)


def render(doc: dict, out_path, max_pages: int = 1, keep_typst: bool = True,
           subject: str = "") -> dict:
    """Render, auto-fit, stamp metadata, and verify. Returns the ATS report.

    Raises RenderError if the content cannot be made to fit. That is deliberate:
    the alternative is silently shipping a two-page resume or a 9pt brick, and
    deciding what to cut is a judgement call that belongs to a person.
    """
    out_path = pathlib.Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    typ_path = out_path.with_suffix(".typ")

    attempts = []
    fitted = None
    for size, leading in DENSITY_LADDER:
        typ_path.write_text(build_typst(doc, size, leading), encoding="utf-8")
        typst.compile(str(typ_path), output=str(out_path))
        pages = pymupdf.open(str(out_path)).page_count
        attempts.append({"size": size, "leading": leading, "pages": pages})
        if pages <= max_pages:
            fitted = (size, leading)
            break

    if fitted is None:
        tightest = attempts[-1]
        raise RenderError(
            f"Content does not fit in {max_pages} page(s). Even at "
            f"{tightest['size']}/{tightest['leading']} it needs {tightest['pages']}. "
            f"Cut content - do not ship this tighter.")

    name = doc.get("name", "")
    set_metadata(out_path, title=doc.get("title", f"{name} - Resume"),
                 author=name, subject=subject)

    report = ats_check.check(out_path, expected_strings(doc), max_pages=max_pages)
    report["fit"] = {"size": fitted[0], "leading": fitted[1], "attempts": attempts}

    if not keep_typst:
        typ_path.unlink(missing_ok=True)
    return report


def slugify(*parts: str) -> str:
    s = "-".join(p for p in parts if p)
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s)

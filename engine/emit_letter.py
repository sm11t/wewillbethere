"""Render a cover letter as a resume.lol document.

Same letterhead as the resume so the two arrive looking like one person's work,
then prose. The structure is deliberately unusual:

    [highlighted signpost]      tells the reader how to navigate
    personal paragraph          the part that does not fit on a resume
    [second signpost]           where the evidence starts
    technical paragraph(s)      tailored per job
    close                       what he wants, plainly

The signposts are the whole point. A cover letter that opens "I am writing to
express my interest" asks the reader to find the good part themselves; this one
tells them where it is and invites them to skip. That reads as confidence when
the paragraph is worth reading, so the personal paragraph has to earn it.
"""

from __future__ import annotations

import re

NL = chr(10)
PX_TO_PT = 0.75


def css(scale: float = 1.0, spacing: float = 1.0) -> str:
    def px(v: float) -> str:
        return f"{round(v * scale, 2)}px"

    def sp(v: float) -> str:
        return f"{round(v * scale * spacing, 2)}px"

    return f"""\
@import url('https://fonts.googleapis.com/css2?family=Tinos:wght@400;700&display=swap');

body {{
  font-family: Tinos, 'Times New Roman', Times, serif;
  font-size: {px(14.6)};
  line-height: {round(max(1.28, 1.46 * spacing), 3)};
  color: #000;
  margin: 0;
  font-variant-ligatures: none;
  font-variant-numeric: lining-nums;
  font-feature-settings: "liga" 0, "clig" 0, "dlig" 0, "lnum" 1, "onum" 0;
  hyphens: manual;
  -webkit-hyphens: manual;
}}

a {{ color: #000; text-decoration: none; border-bottom: 0.4px solid #999; }}

h1 {{
  text-transform: uppercase;
  font-size: {px(29)};
  font-weight: 700;
  letter-spacing: 0.01em;
  line-height: 1.05;
  margin: 0;
}}

.contact {{ font-size: {px(12.2)}; margin: {sp(3)} 0 0; }}
.contact .sep {{ padding: 0 {px(3)}; }}

.rule {{
  border-bottom: 1px solid #000;
  margin: {sp(8)} 0 {sp(14)};
}}

.meta {{ font-size: {px(13)}; margin: 0 0 {sp(14)}; }}

p {{ margin: 0 0 {sp(11)}; }}

/* The signpost. A soft wash, not a marker pen - it should read as a considered
   typographic choice rather than something left over from a mail merge. */
.hl {{
  background: #fdf3b8;
  padding: {px(1)} {px(3)};
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
}}

.signpost {{ font-size: {px(13.4)}; margin: 0 0 {sp(11)}; }}
.sig {{ margin-top: {sp(16)}; }}
"""


def meta_css(margin_in: float = 0.9) -> str:
    """Letters carry wider margins than a resume. The measure should be
    comfortable to read straight through, not packed."""
    return f"@page {{{NL}  size: letter;{NL}  margin: {margin_in}in;{NL}}}{NL}"


LADDER = [
    (1.06, 1.00, 1.00), (1.03, 0.95, 1.00), (1.00, 0.90, 1.00),
    (0.98, 0.90, 0.96), (0.95, 0.85, 0.93), (0.92, 0.80, 0.90),
    (0.90, 0.80, 0.86), (0.88, 0.75, 0.82),
]

_BACKSLASH = chr(92)


def _esc(text: str) -> str:
    for ch in ("*", "_", "`"):
        text = text.replace(ch, _BACKSLASH + ch)
    return text


def _profile_links() -> dict:
    """render_as -> url for every link in profile.yaml's basics.

    Read lazily and defensively: rendering a letter must not start failing
    because the profile moved or a link lost its url.
    """
    try:
        from engine import profile as _profile
        basics = _profile.load().basics
        return {l["render_as"]: l["url"]
                for l in basics.get("links", []) or []
                if l.get("render_as") and l.get("url")}
    except Exception:
        return {}


def to_markdown(letter: dict) -> str:
    """letter = {name, contact[], date, recipient[], signpost_1, personal,
    signpost_2, technical[], close, signoff}"""
    name = letter["name"]
    lines = [
        "@REDACTED=false",
        f"@NAME={name}||A. Datta",
    ]

    # The letterhead is meant to be identical to the resume's, and that
    # includes behaving like it: anything with a URL behind it is a real
    # anchor. The URLs come from profile.yaml rather than being repeated in
    # every draft, so a changed link is changed in one place.
    #
    # Email is deliberately left unlinked, exactly as on the resume: it is a
    # redactable variable with a hidden twin, and a mailto: href would carry
    # the real address in the markup even when the visible text is redacted.
    links = _profile_links()
    rendered = []
    for item in letter.get("contact", []):
        if "@" in item and "." in item:
            lines.append(f"@EMAIL={item}||contact@example.com")
            rendered.append("{EMAIL}")
        elif item in links:
            rendered.append(f'<a href="{links[item]}">{item}</a>')
        else:
            rendered.append(item)

    lines += ["", "# {NAME}", ""]
    sep = ' <span class="sep">' + chr(0xB7) + "</span> "
    lines.append('<p class="contact">'
                 + sep.join(f"<span>{c}</span>" for c in rendered) + "</p>")
    lines.append('<div class="rule"></div>')

    meta = [x for x in (letter.get("date"), *letter.get("recipient", [])) if x]
    if meta:
        lines.append('<p class="meta">' + "<br>".join(_esc(m) for m in meta) + "</p>")

    if letter.get("signpost_1"):
        lines.append(f'<p class="signpost"><span class="hl">'
                     f'{_esc(letter["signpost_1"])}</span></p>')

    if letter.get("personal"):
        lines.append(f"<p>{_esc(letter['personal'])}</p>")

    if letter.get("signpost_2"):
        lines.append(f'<p class="signpost"><i>{_esc(letter["signpost_2"])}</i></p>')

    for para in letter.get("technical", []):
        lines.append(f"<p>{_esc(para)}</p>")

    if letter.get("close"):
        lines.append(f"<p>{_esc(letter['close'])}</p>")

    # The letterhead already carries the name in 29pt at the top of the page,
    # so a typed signature underneath is a repetition rather than a closing.
    if letter.get("signoff"):
        lines.append(f'<p class="sig">{_esc(letter["signoff"])}</p>')
    return NL.join(lines) + NL


def expected_strings(letter: dict) -> list[str]:
    out = [letter["name"], *letter.get("contact", []),
           letter.get("date", ""), *letter.get("recipient", []),
           letter.get("signpost_1", ""), letter.get("personal", ""),
           letter.get("signpost_2", ""), *letter.get("technical", []),
           letter.get("close", "")]
    return [s for s in out if s]


def plain_text(letter: dict) -> str:
    """ASCII version for portals with a paste box and for an email body."""
    parts = []
    for m in letter.get("recipient", []):
        parts.append(m)
    for key in ("signpost_1", "personal", "signpost_2"):
        if letter.get(key):
            parts.append(letter[key])
    parts += list(letter.get("technical", []))
    if letter.get("close"):
        parts.append(letter["close"])
    if letter.get("signoff"):
        parts.append(letter["signoff"])
    text = (NL * 2).join(parts)
    return re.sub(r"[^\x00-\x7f]", lambda m: {chr(0x2019): "'", chr(0x2018): "'",
                                              chr(0x201C): '"', chr(0x201D): '"',
                                              chr(0x2013): "-", chr(0x2014): "-",
                                              chr(0xB7): "-"}.get(m.group(), ""), text)

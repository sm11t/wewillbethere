"""Render the fact base as a resume.lol document (markdown + CSS + page rules).

This replaces the Typst template as the *presentation* layer. Everything that
makes the output trustworthy is upstream of here and unchanged: selection from
approved phrasings, blocked metrics, evidence-backed skills, the voice linter.
This module only decides how those facts look.

resume.lol renders the markdown to plain HTML (h1/h2/h3/p/ul/li/a) and applies
the CSS. Inline HTML is sanitized down to class attributes, which is enough to
put a date on the right of a heading.
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Design
#
# The brief was "the one we have is very bad", so this is a deliberate design
# rather than a default: a serif for the name and section labels against a
# sans for everything read at speed. Source Serif 4 and Inter are both open
# fonts, so they embed cleanly and neither is the Times/Calibri/Arial default
# that makes a resume look untouched.
#
# The name sits left, not centered. Centering is the single most common resume
# gesture and it wastes the strongest position on the page.
# ---------------------------------------------------------------------------

def css(scale: float = 1.0, spacing: float = 1.0) -> str:
    """Stylesheet at a given density.

    Typography follows the resume.lol starter template Asmit chose: Tinos at
    14px, the name upper-cased and left-aligned, section headings upper-cased
    over a hairline rule, and dates pushed to the right margin of each heading.

    Tinos is a static Google font, so Chrome embeds it as a real Type0 program.
    Variable fonts do not survive that trip: Source Serif 4, requested with its
    opsz and wght axes, was rasterized into Type3 glyph procedures instead.

    `scale` multiplies type size and vertical rhythm together, so the page
    tightens or opens proportionally rather than just changing the text size.
    """
    def px(v: float) -> str:
        """Type size: scales with `scale` only."""
        return f"{round(v * scale, 2)}px"

    def sp(v: float) -> str:
        """Vertical rhythm: scales with both, so the page can tighten while the
        text stays readable. Type below about 9pt is its own signal to a
        reader; closed-up leading is not."""
        return f"{round(v * scale * spacing, 2)}px"

    return f"""@import url('https://fonts.googleapis.com/css2?family=Tinos:wght@400;700&display=swap');

body {{
  font-family: Tinos, 'Times New Roman', Times, serif;
  font-size: {px(14)};
  font-weight: 400;
  line-height: {round(max(1.16, 1.3 * spacing), 3)};
  color: #000;
  margin: 0;

  /* Ligatures off: stored as single U+FB01/U+FB02 glyphs, "filtering" and
     "Officer" extract with one character where two belong and stop matching a
     keyword search. Lining figures so digits sit on the baseline. */
  font-variant-ligatures: none;
  font-variant-numeric: lining-nums;
  font-feature-settings: "liga" 0, "clig" 0, "dlig" 0, "lnum" 1, "onum" 0;
  hyphens: manual;
  -webkit-hyphens: manual;
}}

a {{ color: #000; text-decoration: none; border-bottom: 0.4px solid #999; }}
h3 a {{ border-bottom: none; }}

/* --- header ------------------------------------------------------------- */

h1 {{
  text-transform: uppercase;
  text-align: left;
  font-size: {px(31)};
  font-weight: 700;
  letter-spacing: 0.01em;
  line-height: 1.05;
  margin: 0;
  padding: 0;
}}

.contact {{
  font-size: {px(12.4)};
  margin: {sp(3)} 0 0;
}}
/* The separator is a real character. The starter template drew it with an
   ::after pseudo-element, which never reaches the PDF text layer, so the whole
   contact line extracted as one unsearchable token with the email fused to
   the phone number. */
.contact .sep {{ padding: 0 {px(3)}; }}

/* --- sections ----------------------------------------------------------- */

h2 {{
  text-transform: uppercase;
  font-size: {px(15)};
  font-weight: 700;
  letter-spacing: 0.03em;
  border-bottom: 1px solid #000;
  margin: {sp(11)} 0 {sp(3)};
  padding: 0 0 {sp(1)};
  break-after: avoid;
  page-break-after: avoid;
}}

/* --- entries ------------------------------------------------------------ */

h3 {{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: {px(14)};
  font-size: {px(14.4)};
  font-weight: 700;
  margin: {sp(6)} 0 0;
  padding: 0;
  break-after: avoid;
  page-break-after: avoid;
}}
h3 .r {{
  font-weight: 400;
  font-size: {px(13)};
  white-space: nowrap;
  font-variant-numeric: lining-nums tabular-nums;
}}

.sub {{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: {px(14)};
  font-size: {px(13)};
  font-style: italic;
  margin: {sp(1)} 0 0;
  break-after: avoid;
  page-break-after: avoid;
}}
.sub .r {{
  white-space: nowrap;
  font-style: normal;
  font-variant-numeric: lining-nums tabular-nums;
}}

/* --- bullets ------------------------------------------------------------ */

ul {{
  margin: {sp(3)} 0 0;
  padding-left: {sp(17)};
  break-before: avoid;
  page-break-before: avoid;
}}
li {{
  margin: {sp(1.5)} 0;
  padding-left: {sp(2)};
  break-inside: avoid;
  page-break-inside: avoid;
}}

p {{ margin: 0; padding: 0; }}

/* --- skills ------------------------------------------------------------- */

.skill {{ margin: {px(2.5)} 0 0; font-size: {px(13.4)}; break-inside: avoid; }}
.skill b {{ font-weight: 700; }}
"""


def meta_css(margin_in: float = 0.55) -> str:
    """Page box. Side margins run slightly wider than top and bottom, which
    keeps the measure readable instead of letting lines stretch edge to edge."""
    side = round(margin_in + 0.05, 2)
    return f"@page {{\n  size: letter;\n  margin: {margin_in}in {side}in;\n}}\n"


# Density ladder, loosest first. Publishing stops at the first rung that fits.
LADDER = [
    # (type scale, page margin in inches, vertical-rhythm scale)
    (1.14, 0.70, 1.00), (1.10, 0.65, 1.00), (1.06, 0.62, 1.00),
    (1.03, 0.60, 1.00), (1.00, 0.60, 1.00), (1.00, 0.55, 0.98),
    (0.97, 0.55, 0.95), (0.95, 0.52, 0.92), (0.92, 0.50, 0.90),
    (0.90, 0.48, 0.86), (0.90, 0.45, 0.80), (0.88, 0.45, 0.76),
    (0.86, 0.45, 0.72), (0.85, 0.42, 0.68),
]

# Back-compat for callers that want the default look.
CSS = css(1.0, 1.0)
META_CSS = meta_css(0.55)


_BACKSLASH = chr(92)


def _esc(text: str) -> str:
    """Neutralize markdown control characters that would change formatting.

    C++ and snake_case names in the fact base would otherwise be read as
    emphasis markers and silently swallowed.
    """
    for ch in ("*", "_", "`"):
        text = text.replace(ch, _BACKSLASH + ch)
    return text


def _link(text: str, href: str) -> str:
    """Wrap text in an anchor. The sanitizer keeps href and class on links."""
    if not href:
        return _esc(text)
    return f'<a href="{href}">{_esc(text)}</a>'


def _row(left: str, right: str, tag: str, cls: str = "",
         href: str = "") -> str:
    """A heading or sub-line with the date pushed to the right margin."""
    attrs = f' class="{cls}"' if cls else ""
    left_html = f'<span class="l">{_link(left, href)}</span>' if left else ""
    right_html = f'<span class="r">{_esc(right)}</span>' if right else ""
    if tag == "h3":
        return f"### {left_html}{right_html}"
    return f"<p{attrs}>{left_html}{right_html}</p>"


def to_markdown(doc: dict, redacted_defaults: bool = False) -> str:
    """Build the resume.lol markdown for an assembled document.

    Personal details become variables with redacted twins, so a share link can
    hide them without maintaining a second copy of the resume.
    """
    contact = list(doc.get("contact", []))
    name = doc.get("name", "")

    lines = [
        f"@REDACTED={'true' if redacted_defaults else 'false'}",
        f"@NAME={name}||A. Datta",
    ]

    # Map the known contact fields onto variables; anything else renders as is.
    # Anything with a URL behind it becomes a real anchor: a resume is read on
    # screen at least as often as on paper, and a LinkedIn address printed as
    # plain text is a instruction to retype it by hand.
    #
    # Email and phone are deliberately NOT linked. Both are redactable
    # variables with hidden twins for share links, and a mailto: href would
    # carry the real address in the markup even when the visible text is
    # redacted - which would defeat the entire point of the redaction.
    links = doc.get("contact_links", {})
    rendered: list[str] = []
    for item in contact:
        if "@" in item and "." in item:
            lines.append(f"@EMAIL={item}||contact@example.com")
            rendered.append("{EMAIL}")
        elif re.match(r"^[\d\s()+.-]{7,}$", item):
            lines.append(f"@PHONE={item}||(000) 000-0000")
            rendered.append("{PHONE}")
        elif item in links:
            rendered.append(_link(item, links[item]))
        else:
            rendered.append(item)

    lines += ["", f"# {{NAME}}", ""]
    # The separator is a real character, not a CSS ::before. A pseudo-element
    # never reaches the text layer, so an extractor read the header as
    # "New York, NYasmit77@icloud.comasmit.space" - one unsearchable token.
    sep = ' <span class="sep">·</span> '
    lines.append('<p class="contact">'
                 + sep.join(f"<span>{c}</span>" for c in rendered)
                 + "</p>")

    for section in doc.get("sections", []):
        lines += ["", f"## {section['heading']}"]
        for entry in section.get("entries", []):
            lines.append("")
            lines.append(_row(entry.get("left", ""), entry.get("right", ""),
                              "h3", href=entry.get("href", "")))
            if entry.get("left2") or entry.get("right2"):
                lines.append(_row(entry.get("left2", ""), entry.get("right2", ""),
                                  "p", cls="sub",
                                  href=entry.get("href2", "")))
            bullets = entry.get("bullets", [])
            if bullets:
                lines.append("")
                lines += [f"- {_esc(b)}" for b in bullets]

    if doc.get("skills"):
        lines += ["", "## Skills", ""]
        for label, values in doc["skills"]:
            lines.append(f'<p class="skill"><b>{_esc(label)}:</b> '
                         f'<span>{_esc(values)}</span></p>')

    return "\n".join(lines) + "\n"


PAGE_WIDTH_PT = 8.5 * 72          # US Letter
PX_TO_PT = 0.75                   # Chrome prints CSS px at 96 per inch


def fit_skills_to_one_line(skills, scale: float, margin_in: float,
                           reserve_pt: float = 4.0):
    """Trim each skills category so its line does not wrap.

    A wrapped skills line costs a whole extra row for two or three words and
    makes the block look ragged. Capping each category at one line is also what
    frees the vertical space that lets everything else fit on one page.

    Widths are measured with Times metrics rather than guessed from character
    counts: Tinos is metrically compatible with Times New Roman by design, so
    the numbers transfer exactly.

    Items are dropped from the end, so whatever the caller put first survives -
    which is why per-job ordering matters.
    """
    import pymupdf

    regular = pymupdf.Font("tiro")
    bold = pymupdf.Font("tibo")
    avail = PAGE_WIDTH_PT - 2 * margin_in * 72 - reserve_pt
    size = 13.4 * scale * PX_TO_PT

    out, dropped = [], []
    for label, values in skills:
        items = [v for v in values.split(", ") if v]
        label_w = bold.text_length(label + ":", fontsize=size)
        kept = []
        for item in items:
            candidate = kept + [item]
            text_w = regular.text_length(" " + ", ".join(candidate), fontsize=size)
            if label_w + text_w > avail:
                dropped.append(item)
                continue
            kept = candidate
        out.append([label, ", ".join(kept)])
    return out, dropped


def expected_strings(doc: dict) -> list[str]:
    """Strings that must survive into the exported PDF's text layer."""
    out = [doc.get("name", "")] + list(doc.get("contact", []))
    for section in doc.get("sections", []):
        out.append(section["heading"])
        for entry in section.get("entries", []):
            out += [entry.get(k, "") for k in ("left", "right", "left2", "right2")]
            out += entry.get("bullets", [])
    for label, values in doc.get("skills", []):
        out += [label, values]
    return [s for s in out if s]

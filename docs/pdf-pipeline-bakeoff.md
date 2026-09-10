# PDF pipeline bakeoff

Run 2026-09-02 on this machine (Windows 11, Python 3.14.3, Node, Tectonic 0.16.9, Chrome 152).

The same resume content was rendered through five pipelines and scored by an
automated ATS-fidelity analyzer. The question each pipeline had to answer:
**when a parser reads this PDF, does it get back what a human sees?**

## Results

| pipeline | verdict | text recall | char integrity | pages | KB | render time |
|---|---|---|---|---|---|---|
| **Typst** (pip pkg) | **PASS** | 1.000 | 1.000 | 1 | 76 | 0.51 s |
| Chrome headless (HTML/CSS) | PASS | 1.000 | 1.000 | **2** | 73 | 2.39 s |
| fpdf2 (direct) | PASS | 1.000 | 1.000 | 1 | 67 | 0.20 s |
| LaTeX / Tectonic (patched) | WARN | 1.000 | **0.898** | 1 | 59 | 4.25 s |
| LaTeX / Tectonic (naive) | **FAIL** | 0.881 | 0.848 | 1 | 59 | 5.07 s |
| WeasyPrint | — | did not install | | | | |

Scored at the **worst** of two extractors (pypdf, PyMuPDF), because employers run
different parsers and you don't get to pick which one.

- **text recall** — does the content survive at all, ignoring whitespace noise and
  cosmetic character swaps? Failure is fatal: the words are gone.
- **char integrity** — do the exact codepoints survive? Failure is a silent keyword
  killer. The page looks perfect; the text is broken.

## The finding that matters: LaTeX corrupts text invisibly

The LaTeX output *looks* flawless on screen. Its text layer is not.

**1. The `fi` ligature extracts as `ϐ` (U+03D0 GREEK BETA SYMBOL).**

```
what the page shows:      Technical Officer ... real-time filtering ... offline-first
what a parser reads:      Technical Ofϐicer ... real-time ϐiltering ... ofϐline-ϐirst
```

Every word containing "fi" or "fl" is destroyed: *filtering, Officer, first, flaky,
offline*. A recruiter searching "filtering" gets nothing. Fixable with
`Ligatures=NoCommon`.

**2. Every ASCII hyphen becomes U+2011 NON-BREAKING HYPHEN.** Twelve occurrences.

```
real-time  ->  real‑time      voice-to-SQL  ->  voice‑to‑SQL
role-based ->  role‑based     endpoint-discovery -> endpoint‑discovery
```

A search for `real-time` typed with a normal hyphen will not match. This one
survived every fix attempted (`Ligatures=NoCommon`, hyphenation disabled,
`\righthyphenmin=62`) — it comes from how the font's reverse cmap is written into
the ToUnicode map by `xdvipdfmx`. Character integrity stalled at 0.898.

Both defects pass a visual proofread and pass a "does it have a text layer" check.
Only a character-level diff against the source catches them.

**Note:** a ToUnicode CMap being *present* is not sufficient. All four LaTeX fonts
had `toUnicode=True`. The map was simply wrong.

## Why not the others

**Chrome headless** — text is perfect, but the same content that fits one page in
Typst spilled to two, so page control means hand-tuning CSS per variant. It also
stamps `Creator: Mozilla/5.0 ... HeadlessChrome/152.0.0.0` and `Producer: Skia/PDF
m152` into the file. Strippable, but it's a strike. Kept as the fallback.

**fpdf2** — scores perfectly and is the fastest, but has no layout engine. Every
position is computed by hand, so there is no automatic reflow, no page fitting, and
no cheap way to maintain several template variants. Good for a fixed form, wrong
for a document whose content changes per job.

**WeasyPrint** — cannot install on Windows without a GTK/Pango runtime
(`OSError: cannot load library 'libgobject-2.0-0'`). Eliminated.

## Verdict: Typst

Primary pipeline, with Chrome/HTML as fallback.

- Only pipeline scoring 1.000 on **both** metrics *and* fitting one page
- Installs as a pure pip package (`pip install typst`) — no external binary, no
  TeX distribution, no GTK
- Fastest real layout engine here: 0.51 s cold, ~0.2 s warm
- Embeds Cambria as a proper subset with a **correct** ToUnicode CMap
- Preserves en dash, em dash, `×`, and ASCII hyphens exactly

## Verified capabilities

**Auto-fit to one page.** Typst recompiles in ~0.2 s, so the renderer walks a
density ladder (10.5pt/0.66em → 9pt/0.48em) and stops at the loosest setting that
fits. At normal content: 1 compile, 0.40 s. At 1.8× content: exhausted all 10 rungs
in 2.03 s and correctly reported it still needed 2 pages.

> **Design rule:** when the ladder is exhausted, the system fails loudly and asks
> for content to be cut. It must never silently ship a 2-page resume or a
> 9pt/0.48em brick. Deciding what to cut is a human decision.

**Metadata control.** Typst stamps `Creator: Typst 0.15.0` and a UTC timestamp. A
post-render pass with pypdf takes full ownership of the Info dictionary — setting
Title/Author/Subject and clearing Creator, Producer, and both timestamps. Verified
that the rewrite leaves the text layer untouched (still PASS, 1.000/1.000, 1 page).

## The current resume is fine

`resume_asmit.pdf` was produced by **ReportLab**, not LaTeX, and its text layer is
clean. The only non-ASCII characters are en dash (×3) and bullet (×11), both
benign. "filtering", "Officer", and "first" all extract correctly. Whatever
generated it did not introduce the corruption class above.

## Right-aligned dates: measured, then kept

A third extractor (pdfminer.six) was added after the first round and immediately
disagreed with the other two about the Typst output. With default layout analysis
it reads the right-aligned date column as a *separate column* and splices it into
the middle of a wrapping bullet:

```
...an admin console for data operations;
Aug 2025 – Apr 2026
Remote
built an automated Python endpoint-discovery pipeline...
```

Three things were measured before deciding what to do:

1. **Is it the file or the parser?** The parser. `LAParams(boxes_flow=None)` reads
   the same file in perfect order. Nothing is wrong with the PDF.
2. **Does a left-aligned layout fix it?** Yes — 1.000 across all three engines. But
   it wastes the right half of the page and reads as visibly weaker, and NYU
   on-campus applications are read by humans, not an ATS.
3. **What is actually lost?** Nothing searchable. **Token recall stays 1.000** — every
   keyword is present and findable. Only phrase *contiguity* breaks.

So the gate was rebuilt around the question a recruiter's search actually asks:

- **token recall** — is the word in the document at all? This gates pass/fail.
- **phrase recall** — did the words stay contiguous? Reported, not fatal, when only
  one engine disagrees.

The difference is the whole point: pdfminer's column-splitting leaves every keyword
intact, while LaTeX's `real-time` → `real‑time` substitution destroys the keyword
outright. Scoring both as "0.9-something recall" would have hidden that.

**Decision: keep right-aligned dates.** Typst now scores token recall 1.000 / WARN;
LaTeX scores 0.881 / FAIL.

## The current resume, checked properly

`resume_asmit_2026-07-21.pdf` passes on text — token recall 1.000, phrase recall
1.000, character integrity 1.000, one page, 5.7 KB — but has two real defects:

- **Fonts are not embedded.** It references Helvetica and Times-Roman/Bold/Italic by
  name. Those are standard-14 fonts so they always extract, but the document renders
  with whatever substitute the reader's viewer picks, so it does not look the same on
  every screen.
- **Metadata is empty.** Title `(anonymous)`, Author `(anonymous)`, Subject
  `(unspecified)`. A recruiter's PDF viewer shows "(anonymous)" in the tab.

Neither is an ATS failure. Both are polish, and both are free to fix.

## The analyzer stays

`engine/ats_check.py` is a permanent gate, not a one-off. Every generated document
runs through it before it is sent. It checks text recall, character integrity,
reading order, font embedding, ToUnicode presence, page count, and metadata.

It exists because of a real failure already in this folder: the LinkedIn profile
export (`linkedin_pdfs/*.pdf`) is **completely unextractable** — subsetted fonts
with no usable ToUnicode map, so both pypdf and PyMuPDF return glyph indices like
`/0/1/2/i255` instead of text. Had to be read by rendering to images and using
vision. If a resume ever left this folder in that state, an ATS would read it as
an empty document and no human would ever see it.

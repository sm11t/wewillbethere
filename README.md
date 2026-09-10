# Resume and cover letter system

Generates tailored, ATS-verified application documents from one fact base.

Three rules hold the whole thing together:

1. **Tailoring is selection, never generation.** The renderer prints stored text
   verbatim and has no free-text path. To say something new, you add a phrasing
   to `profile/profile.yaml` and approve it. This is what makes the output read
   like you wrote it — because you did.
2. **A number ships only if it can be defended.** Every metric carries provenance.
   Anything marked `needs_confirmation` is blocked at render time. A figure that
   collapses under one interview question poisons every other figure on the page.
3. **Nothing leaves without passing the gate.** Every PDF is parsed back by three
   independent engines and diffed against its source.

## Quick start

```powershell
python -m engine.profile                       # what's blocking a shippable document
python -m engine.approve --list                # phrasings waiting for your sign-off
python -m engine.publish swe-intern --draft    # build, publish, export, verify
```

Four presets: `swe-intern`, `campus-ta`, `ra-research`, `ml-ai-infra`.

`--draft` includes phrasings you haven't approved yet and says so on the way out.
Drop it once you've read them and run `python -m engine.approve --all`.

## How a resume gets made

```
profile.yaml ──► build.py ──► emit_rlol.py ──► resume.lol ──► HTML
   facts        selection       markdown+CSS      storage        │
                                                                 ▼
                              ats_check.py ◄── PDF ◄── headless Chrome
                              ai_lint.py                (auto-fit to 1 page)
```

**resume.lol** holds the content and styling, so you can open any variant in its
web editor and tweak it by hand. Credentials come from the MCP server entry in
`~/.claude.json`, never from this repo.

**The PDF is printed locally, not through the site's export.** Their HTML embeds
Paged.js and calls `window.print()` after paginating — correct for a person
hitting Ctrl+P, but under headless Chrome it is a race. The same input produced a
full page on one run and a blank one on the next. The page body is clean semantic
HTML and the `@page` rule says everything Chrome needs, so the print step drops
Paged.js and lets Chrome paginate natively. Deterministic, and about a second per
render instead of four.

**Fitting one page is mechanical.** `emit_rlol.LADDER` is a list of density rungs;
publishing stops at the first that fits. When even the tightest overflows it fails
loudly rather than shrinking further — deciding what to cut is a human call.

## What the gate checks

- **Token recall** — is every keyword actually in the document? This gates
  pass/fail.
- **Character integrity** — did the exact codepoints survive, or did something
  quietly substitute them?
- **Reading order**, **font embedding**, **ToUnicode CMaps**, **page count**,
  **file size**, **metadata**, and **page fill**.
- A **codepoint audit** flagging characters that mean a broken pipeline: soft
  hyphens, non-breaking hyphens, presentation ligatures, private-use icon glyphs,
  replacement characters.

Scored against pypdf, PyMuPDF, and pdfminer.six and reported at its **worst**.
Employers run different parsers and you don't get to pick which one.

Three real defects it caught while this was being built, none visible on screen:

- A blank PDF that the fit loop had accepted as a perfect one-page fit.
- **Type3 fonts.** Loading Inter and Source Serif from Google Fonts made Chrome
  rasterize every glyph instead of embedding a font program. Switched to
  Constantia and Corbel, which ship with Windows and embed as real Type0 fonts.
- **Presentation ligatures.** Constantia stored `fi` and `fl` as single U+FB01
  glyphs, so "filtering" and "Officer" stopped matching a keyword search — the
  same failure class that disqualified LaTeX. Fixed with
  `font-variant-ligatures: none`.

The gate exists because of a real failure already in this folder: the archived
LinkedIn exports are completely unextractable, so every parser returns glyph
indices instead of text. A resume in that state reads to an ATS as a blank page.

## Layout

```
profile/
  profile.yaml        the fact base — every claim, every phrasing, every metric's provenance
  variants.yaml       the four presets: what each leads with and what it cuts
  voice.md            his voice, and the cover-letter positioning: asks the right questions
  raw-facts.md        source material, with gaps and conflicts marked
engine/
  profile.py          loads the fact base; enforces approval, provenance, evidence
  build.py            preset + facts -> document
  emit_rlol.py        document -> resume.lol markdown, CSS, and the density ladder
  rlol_client.py      JSON-RPC client for the resume.lol API
  publish.py          push, export, auto-fit, scrub metadata, verify
  ats_check.py        the gate: three parsers, codepoint audit, fonts, fill
  ai_lint.py          catches AI-generated tells in prose
  approve.py          review and approve phrasings
  render.py           offline Typst fallback; also owns PDF metadata
docs/
  pdf-pipeline-bakeoff.md   the five-engine bakeoff that chose Typst offline
  research-spec.md          the full research output
checklists/intake.md        the questions only Asmit can answer
out/                        generated PDFs, HTML, and rlol-resumes.json
```

`engine.build` still renders locally through Typst with no network and no
account. Kept as a fallback, not the main path.

## Current state

All four presets publish and pass: one page each, token recall 1.000, character
integrity 1.000, 89–95% page fill, ~46 KB.

Not built yet: job-description tailoring, the cover letter renderer, the
application ledger, DOCX output.

**Blocked on `checklists/intake.md`.** Nothing is approved for sending: 0 of 19
phrasings have been read and approved, four metrics are blocked pending an
explanation, and the header is missing a phone number and a GitHub link.

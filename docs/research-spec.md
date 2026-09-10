# BUILD SPEC — Resume & Cover Letter System for Asmit Datta
**Date:** 2026-09-02 · **Target machine:** Windows 11, Python 3.14, Node, Tectonic installed (unused), Word installed, Edge installed · **Users:** 1 · **Timeline pressure:** Summer 2027 SWE recruiting is mid-cycle NOW (Google MS req 94172495052972742 open, anticipated close 2026-09-25, rolling); NYU fall on-campus hiring window is open NOW.

---

## 1. VERDICT ON THE STACK

**PRIMARY RENDERER: `typst-py` (pip package `typst`, 0.15.0).** It was the only pipeline measured on this machine to produce byte-perfect text in BOTH extractor families (pypdf/ToUnicode and PyMuPDF) with ligatures rendered, compiles in 150–650 ms (making the one-page fit loop trivial), takes JSON via `sys_inputs`, and writes honest metadata (`/Creator: Typst 0.15.0`, no HeadlessChrome fingerprint). Beats the repo track's Playwright recommendation because Skia PDFs need ligature-disabling AND a metadata scrub to be equally safe, and typst needs neither.

**REJECTED, with reasons (one line each):**
- **Tectonic/XeLaTeX (installed):** measured on this machine producing U+037E for `;` and U+FBxx ligature garbage — the exact failure class that made his LinkedIn export unextractable. Do not reuse.
- **Playwright/Puppeteer:** adds an install for nothing typst doesn't do better here.
- **WeasyPrint:** MSYS2 GTK DLL surgery on Windows; fails offline-reproducible requirement.
- **@react-pdf:** hyphenates into the text layer by default (keyword killer).
- **fpdf2/ReportLab:** hand-rolled layout labor with no typographic payoff.
- **Canva/Figma/LinkedIn export:** broken or absent ToUnicode; banned outright.
- **career-ops Node scripts (verify-cv-facts.mjs etc.):** steal the *designs*, reimplement in Python — the verifier libraries (pymupdf/pypdf) are Python and the fact gate is ~200 lines of regex; one-language pipeline.

**FALLBACK RENDERER:** headless Edge (already installed, same Skia backend as Chrome) — only if a design need exceeds Typst. Mandatory when used: CSS `font-variant-ligatures: none; hyphens: manual;` + pypdf pass to replace the HeadlessChrome `/Creator` string and set Author/Keywords.
```
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="out.pdf" "file:///C:/path/in.html"
```

**DOCX TWIN (for portals that demand Word):** `docxtpl` driven by the same JSON; `docx2pdf` via Word COM (WINWORD.EXE verified at `C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE`) only if a portal wants Word-produced PDF. Never convert PDF→DOCX.

**FONTS:** Constantia body with `#set text(number-type: "lining")` + Corbel headings — both installed, fsType=8 (embedding licensed), visibly not template defaults. Ligatures stay ON (safe in Typst only). Banned: SF-Pro (license), Latin Modern (LaTeX tell + measured extraction defects), Calibri/Arial/Times body (default-stack tell), icon fonts (PUA garbage). Later option: vendor Source Sans 3 / IBM Plex (OFL) via `font_paths=[...], ignore_system_fonts=True` for pinned reproducible builds.

**METADATA POLICY:** pypdf post-pass on every PDF — `/Title "Asmit Datta - Resume"` (role-specific for letters), `/Author "Asmit Datta"`, `/Keywords` = role skills, local-timezone timestamp via typst `timestamp` param; leave `/Creator Typst 0.15.0` (a human's tool choice, not an AI tell). No exiftool/qpdf needed.

**INSTALL (run once):**
```powershell
mkdir C:\Users\asmit\career; cd C:\Users\asmit\career
git init
py -3.14 -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install typst pypdf pymupdf pdfminer.six pyyaml jsonschema docxtpl
# optional, only when a portal demands Word-produced PDF:
.\.venv\Scripts\python -m pip install docx2pdf
```
Bake into every script: `PYTHONIOENCODING=utf-8` (the verifier itself crashed on U+037E without it in testing), and `.gitattributes` with `*.yaml text` / `*.typ text`. Scripts that write YAML must emit UTF-8 **without BOM** (PowerShell 5.1 defaults corrupt it — write from Python, not `Out-File`).

---

## 2. DIRECTORY LAYOUT

```
C:\Users\asmit\career\
├── README.md                     # how to run: new-app → render → verify → submit
├── .gitattributes                # *.yaml text, *.typ text — kill CRLF churn
├── .venv\                        # Python 3.14 venv (gitignored)
├── profile\
│   ├── profile.yaml              # THE master fact base: entries → facts → approved variants → metrics w/ provenance (§3)
│   ├── variants.yaml             # the 4 variant presets: section architecture, entry placement, ordering, skills-category order (§7)
│   ├── VOICE.md                  # voice profile + verbatim exemplars; injected into every generation prompt (copied from scratchpad\VOICE.md as-is)
│   ├── BANNED.txt                # flat lowercase lint lexicon, one term per line (§4)
│   └── RAW_PROFILE_FACTS.md      # frozen source-of-truth doc; append-only with provenance markers
├── schema\
│   ├── profile.schema.json       # JSON Schema draft-07 for profile.yaml (live-validated via yaml-language-server comment)
│   └── application.schema.json   # schema for applications\*.yaml
├── render\
│   ├── resume.typ                # single custom single-column template; reads sys_inputs JSON; hyphenate:false, justify:false
│   ├── letter.typ                # cover-letter template, letterhead identical to resume header
│   └── docx\template.docx        # docxtpl Jinja template, same JSON contract
├── scripts\                      # all Python, all run from .venv
│   ├── validate.py               # jsonschema check of profile.yaml + all application files; pre-commit hook
│   ├── lint_facts.py             # deterministic anti-fabrication gate: numerals, controlled vocab, ownership verbs, provenance status (§5-A)
│   ├── lint_voice.py             # deterministic anti-AI lint: BANNED.txt grep + construction regexes + structural counters (§4)
│   ├── select.py                 # greedy marginal-coverage variant selection under line budget (§6 step 6)
│   ├── render.py                 # assemble JSON → typst.compile → fit loop → pypdf metadata pass
│   ├── verify_pdf.py             # BLOCKING post-render gate: dual/triple extraction, token round-trip, codepoints, order, metadata, pages, size (§5-B)
│   ├── new_app.py                # scaffold applications\<date>--<slug>.yaml, snapshot JD text, extract keywords/knockouts
│   ├── ledger.py                 # per-employer consistency: frozen-fact injection pre-render, drift diff post-render
│   ├── review_queue.py           # proposes new draft variants (approved:false) + runs fresh-context entailment judge on them
│   └── emit_letter.py            # letter assembly: his opening + fact middle + logistics close → PDF + .txt + email-body
├── applications\
│   ├── snapshots\                # verbatim JD text per application (postings vanish; always snapshot)
│   └── 2026-09-05--example.yaml  # one record per application: job, variant_ids, claims_shipped, statements_made, status_history
├── out\                          # generated PDFs/DOCX/TXT, committed (sha256 recorded in application record)
├── measurements.json             # cached rendered-line-counts per variant_id + template@version, keyed by content hash
└── checklists\
    ├── INTAKE.md                 # the §9 question list, checked off as answered with dates
    ├── LINKEDIN_FIXES.md         # §8 items 3; done-once
    ├── HANDSHAKE_PROFILE.md      # profile-field sync list emitted with every on-campus app
    └── HUMAN_INPUT_NEEDED.md     # per-app writing prompts (why-this-job, opening line) the system refuses to write
```

---

## 3. PROFILE SCHEMA

YAML + JSON Schema (draft-07), line 1 of every data file: `# yaml-language-server: $schema=...` for live VS Code validation. **Core invariants:** the renderer only prints `approved: true` variant text verbatim (tailoring = selection, never generation); every digit in a variant must trace to a declared metric id; every metric carries a provenance status from the enum `verified | self_reported | estimated | needs_confirmation`; `needs_confirmation` is a hard render block. Content versioning is git, not in-file fields.

```yaml
# yaml-language-server: $schema=./schema/profile.schema.json
meta:
  schema_version: "1.0.0"
  owner: asmit-datta
  sources:                          # provenance registry; every claim points here
    resume_2026: {kind: resume_pdf,      note: "resume_asmit.pdf extracted 2026-09-02"}
    li_2026:     {kind: linkedin_export, note: "profile + projects export 2026-09-02"}
    build_ctx:   {kind: session_context, note: "WatchDNA dev sessions (Expo/Supabase/App Store)"}
    # user_YYYY-MM-DD: added the day Asmit confirms something verbally; until then it does not exist

basics:
  name: "Asmit Datta"
  email: "asmit77@icloud.com"
  phone: null                       # [GAP] blocks all portal submissions
  links:
    - {label: Portfolio, url: "asmit.space", render_as: "asmit.space"}          # visible bare URL + link annotation
    - {label: LinkedIn,  url: "linkedin.com/in/asmitrajeet", render_as: "linkedin.com/in/asmitrajeet"}
    # GitHub: [GAP] — added only after MVP repos exist (§8 item 2)
  location:
    render: {city: "New York", region: "NY"}
    conflict_note: "LinkedIn says Tempe + stale open-to-work banner; fix upstream (§8.3); NEVER render Tempe"
  headlines:                        # one per variant; approved:false drafts cannot ship
    swe:      {text: "M.S. CS student at NYU ('28); shipped production React Native and backend systems at two startups", approved: false}
    teaching: {text: "NYU M.S. CS student; taught ML fundamentals and mentored first-year projects as AI Society Technical Officer at ASU", approved: false}

education:
  - id: nyu
    institution: "New York University"
    degree: "M.S. in Computer Science"
    grad_display: "Expected May 2028"   # never a bare year, never a range
    location: "New York, NY"
    gaps: [school, gpa, coursework, start_date]   # Courant vs Tandon UNKNOWN — never guess the school
  - id: asu
    institution: "Arizona State University"
    degree: "B.S. in Computer Science, Minor in Business"
    grad_display: "May 2026"
    location: "Tempe, AZ"
    gaps: [gpa, honors]                 # print GPA only if >=3.5, as "GPA: X.XX/4.00"

experience:
  - id: myyogateacher
    org: "MyYogaTeacher"
    role: "Software Engineer Intern"          # full titles always; never "SWE Int."
    dates: "May 2025 – Jan 2026"              # Month YYYY, spaced en dash, "Present" only where true
    location: "San Diego, CA (Remote)"
    tags: [mobile, ml, backend, llm]
    metrics:
      - id: uptime
        value: "99.9% uptime"
        provenance: {source: li_2026, status: needs_confirmation,
          note: "his own LinkedIn wording, but uptime-of-a-mobile-client is a category error a reviewer will probe; BLOCKED until he states what was measured; mechanism variant ships meanwhile"}
      - id: admin_cut
        value: "60%"
        provenance: {source: li_2026, status: needs_confirmation, note: "ask measurement basis; mechanism variant available"}
    facts:
      - id: myt.biometrics
        canonical: "Production React Native app for real-time biometric data; offline-first sync with time-series deduplication."
        provenance: {source: li_2026, status: self_reported}
        variants:
          - id: myt.biometrics.mobile     # length: long ≈ 2 lines
            length: long, flavor: mobile, approved: false, uses_metrics: []
            keywords: [React Native, offline-first]
            text: "Built a production React Native app for real-time biometric data — offline-first sync with time-series deduplication that survives flaky networks without losing data"
          - id: myt.biometrics.metric     # BLOCKED until metric 'uptime' clears needs_confirmation
            length: long, flavor: mobile, approved: false, uses_metrics: [uptime]
            text: "Built a production React Native app for real-time biometric data with offline-first sync and time-series deduplication, holding 99.9% uptime on flaky networks"
      - id: myt.voicesql
        canonical: "Voice-to-SQL pipeline (Whisper + streaming LLM responses) replacing the admin team's Ctrl+F-and-edit workflow."
        provenance: {source: li_2026, status: self_reported}
        variants:
          - id: myt.voicesql.mech         # ships now, no digits
            length: medium, flavor: ml, approved: false, uses_metrics: []
            keywords: [Whisper, LLM, SQL]
            text: "Shipped a voice-to-SQL pipeline (Whisper + streaming LLM responses) that replaced the admin team's manual Ctrl+F-and-edit workflow"
          - id: myt.voicesql.metric       # unlocks when admin_cut confirmed
            length: medium, flavor: ml, approved: false, uses_metrics: [admin_cut]
            text: "Shipped a voice-to-SQL pipeline (Whisper + streaming LLM responses) that cut the admin team's manual Ctrl+F-and-edit work by about 60%"

  - id: watchdna
    org: "WatchDNA"
    role: "Software Engineer Intern (Capstone)"   # keep "(Capstone)": it defuses the concurrent-roles red flag
    dates: "Aug 2025 – Apr 2026"
    location: "Tempe, AZ (Remote)"
    tags: [backend, mobile, fullstack, auth, geo]
    metrics: []                                    # no numbers exist for this role; variants correctly carry none
    facts:
      - id: wd.locator
        canonical: "Store locator: Mapbox map, real-time filtering, admin console, Python endpoint-discovery pipeline."
        provenance: {source: li_2026, status: self_reported}
        variants:
          - {id: wd.locator.full,  length: long,  flavor: general, approved: false, uses_metrics: [],
             keywords: [Mapbox, Python],
             text: "Built WatchDNA's store locator: interactive Mapbox map with real-time filtering, an admin console for data operations, and a Python pipeline that auto-discovers retailer endpoints"}
          - {id: wd.locator.short, length: short, flavor: general, approved: false, uses_metrics: [],
             text: "Built an interactive Mapbox store locator with real-time filtering and an admin console"}
      - id: wd.infra
        canonical: "Full backend from scratch: databases, JWT auth with role-based access, security middleware."
        provenance: {source: li_2026, status: self_reported}
        variants:
          - {id: wd.infra.backend, length: medium, flavor: backend, approved: false, uses_metrics: [],
             keywords: [JWT, RBAC, Node.js, PostgreSQL],
             text: "Set up the backend from scratch — databases, JWT authentication with role-based access, security middleware"}
      - id: wd.companion
        canonical: "Companion app reusing the same auth/security/data layer; React Native (Expo), Supabase; iOS App Store review incl. Guideline 2.1 correspondence."
        provenance: {source: li_2026, status: self_reported}
        enrichment: {source: build_ctx, status: self_reported}
        variants:
          - {id: wd.companion.short, length: short, flavor: general, approved: false, uses_metrics: [],
             text: "Shipped a companion app on the same infrastructure, reusing the auth, security, and data layer"}
          - {id: wd.companion.ios, length: medium, flavor: mobile, approved: false, uses_metrics: [],
             requires_confirmation: [appstore_outcome],   # "took through review" safe; "launched" NOT yet
             keywords: [React Native, Expo, Supabase],
             text: "Shipped a companion React Native (Expo) app reusing the same auth and data layers, and took it through iOS App Store review"}

  - id: aisociety                    # promoted OUT of the ASU education line (§8.1)
    org: "The AI Society at ASU"
    role: "Technical Officer"
    dates: "Aug 2025 – Jan 2026"
    location: "Tempe, AZ"
    tags: [teaching, mentoring, leadership, ml]
    metrics:
      - {id: mentees, value: "4", provenance: {source: li_2026, status: self_reported}}
      # workshop headcount DOES NOT EXIST — no variant may imply scale
    facts:
      - id: ais.mentoring
        canonical: "Mentored a team of 4 freshmen through their first ML project: emotion detection from facial expressions and audio cues."
        provenance: {source: li_2026, status: self_reported}
        variants:
          - {id: ais.mentoring.t, length: medium, flavor: teaching, approved: false, uses_metrics: [mentees],
             text: "Mentored a team of 4 freshmen through their first ML project — an emotion-detection system using facial expressions and audio cues"}
      - id: ais.workshops
        canonical: "Created educational resources; ran workshops and study sessions teaching AI/ML fundamentals to students of all majors."
        provenance: {source: li_2026, status: self_reported}
        variants:
          - {id: ais.workshops.t, length: medium, flavor: teaching, approved: false, uses_metrics: [],
             text: "Ran workshops and study sessions that made AI approachable for students without a technical background, and built the teaching materials for them"}

  - id: delhi                        # MISSING from current resume; decisive for RA/grader roles
    org: "University of Delhi"
    role: "Research Study Assistant"
    dates: "May 2024 – Aug 2024"
    location: "New Delhi, India"
    tags: [research, ml, gaussian-processes]
    facts:
      - id: du.gpc
        canonical: "Under Prof. R. P. Singh: optimizing Gaussian Process Classifiers for high-dimensional data modeling."
        provenance: {source: li_2026, status: self_reported}
        gaps: [dataset, methods, results, publication]     # variants stay method-only until filled
        variants:
          - {id: du.gpc.r, length: medium, flavor: research, approved: false, uses_metrics: [],
             text: "Research assistant under Prof. R. P. Singh, optimizing Gaussian Process Classifiers for high-dimensional data modeling"}

  - id: flickmatch                   # oldest role; plain-language rewrite; first to drop for space
    org: "Flickmatch"
    role: "Software Engineer Intern"
    dates: "May 2023 – Aug 2023"
    location: "New Delhi, India"
    tags: [frontend]
    facts:
      - id: fm.ui
        canonical: "Implemented Figma designs as responsive Material-UI components."
        provenance: {source: li_2026, status: self_reported}
        variants:
          - {id: fm.ui.plain, length: short, flavor: general, approved: false, uses_metrics: [],
             text: "Implemented Figma designs as responsive Material-UI React components"}

projects:
  - id: torii
    name: "Torii"
    url: "asmit.space/kya"
    dates: "Mar 2026 – Present"      # the ONE project allowed to be "Present"
    tags: [ai-infra, mcp, payments, backend, security]
    metrics:
      - {id: one_day,  value: "in a day",                    provenance: {source: li_2026, status: self_reported}}
      - {id: two_deps, value: "two production dependencies", provenance: {source: li_2026, status: self_reported}}
    facts:
      - id: torii.core
        canonical: "Spending-control proxy for AI agents (MCP): JWT agent identity, policy engine (budgets, per-call caps, allowlists, rate limits), pre-authorization budget tracker, SQLite audit ledger, x402 handling, USDC on Base via viem, dashboard, CLI."
        provenance: {source: li_2026, status: self_reported}
        variants:
          - {id: torii.core.infra, length: long, flavor: backend, approved: false, uses_metrics: [one_day, two_deps],
             keywords: [MCP, TypeScript, Bun, SQLite],
             text: "Torii, a spending-control proxy between AI agents and paid tools (MCP). Full stack built in a day with Bun and TypeScript (two production dependencies): JWT agent identity tied to a human owner, per-call caps and allowlists, and a pre-authorization tracker that reserves budget so concurrent agents can't overspend"}
          - {id: torii.core.pay, length: medium, flavor: backend, approved: false, uses_metrics: [],
             keywords: [x402, USDC, viem],
             text: "Implemented x402 payment handling: the proxy intercepts HTTP 402 challenges, checks wallet balance, pays in USDC on Base via viem, and retries automatically"}

  - id: lead_engine
    name: "LEAD ENGINE"
    url: "asmit.space/lead-engine"
    dates: "Jan 2026 – May 2026"     # end-date pending his confirmation; not "Present"
    tags: [ai-agents, python, fastapi, automation]
    metrics:
      - {id: leads,        value: "2,100+", provenance: {source: resume_2026, status: self_reported, note: "site shows 2,129; countable artifact; keep"}}
      - {id: conversion,   value: "~50%",   provenance: {source: resume_2026, status: needs_confirmation, note: "absent from LinkedIn; implausible denominator as written; BLOCKED"}}
      - {id: prospect_cut, value: "70%",    provenance: {source: resume_2026, status: needs_confirmation, note: "solo project has no prospecting baseline; BLOCKED"}}
    facts:
      - id: le.pipeline
        canonical: "Autonomous lead agent: sources from public listing and county-record data, scores on Motivation × Ability × Timeline, enriches with property history and equity estimates; 5-stage pipeline, parallel sub-agents; React dashboard with backtesting."
        provenance: {source: li_2026, status: self_reported,
          note: "public materials say 'public listing and county-record sources', never 'scrapes Zillow/Redfin/MLS' (ToS exposure)"}
        variants:
          - {id: le.pipeline.ml, length: long, flavor: ml, approved: false, uses_metrics: [leads],
             keywords: [Python, FastAPI, agents],
             text: "Built an autonomous lead-generation agent (Python/FastAPI): a 5-stage pipeline with parallel sub-agents that sourced 2,100+ real-estate leads from public listing and county-record data and scored each on a Motivation × Ability × Timeline framework"}

  - id: pash
    name: "Pash"
    url: "asmit.space/pash"
    dates: "Jan 2026 – Apr 2026"     # end-date pending confirmation
    tags: [audio, ml, aws, gpu]
    metrics:
      - {id: gpu_speed, value: "5–10x", provenance: {source: li_2026, status: self_reported, note: "honest benchmark spread; keep"}}
    facts:
      - id: pash.arch
        canonical: "Audio stem isolation with Demucs v4; S3 storage, SQS job queue, remote CUDA GPU offload."
        provenance: {source: li_2026, status: self_reported}
        variants:
          - {id: pash.arch.full, length: long, flavor: backend, approved: false, uses_metrics: [gpu_speed],
             keywords: [AWS, S3, SQS, CUDA],
             text: "Pash splits any song into vocals, drums, bass, and instrumentals with Demucs v4 — uploads land in S3, jobs queue through SQS, and separation runs on a remote CUDA GPU, 5–10x faster than CPU"}
  # neuropilot, sentinalai, lynti, portfolio: entries stubbed with status needs_confirmation
  # (truncated descriptions + SentinalAI spelling + portfolio 2024-vs-Feb-2025 date conflict); no shippable variants yet

volunteering:
  - id: covrelief
    org: "CovreliefDwarka"
    role: "Founder"
    dates: "May 2020 – Sep 2020"
    facts:
      - id: cov.vax
        canonical: "[TRUNCATED] 'vaccinated over 100 economically disadvantaged workers...'"
        provenance: {source: li_2026, status: needs_confirmation,
          note: "HARD BLOCK: May–Sep 2020 predates COVID vaccine availability (Dec 2020). Different vaccines? Facilitation? Wrong dates? Gold once resolved."}
        variants: []                  # deliberately none

skills:                               # renderer refuses any skill with empty evidence[]
  - {name: TypeScript,   evidence: [torii, watchdna]}
  - {name: JavaScript,   evidence: [watchdna, flickmatch]}
  - {name: Python,       evidence: [lead_engine, wd.locator, myyogateacher]}
  - {name: SQL,          evidence: [myt.voicesql, torii]}
  - {name: React Native, evidence: [myt.biometrics, wd.companion], aliases: [Expo]}
  - {name: Node.js,      evidence: [watchdna]}
  - {name: FastAPI,      evidence: [lead_engine]}
  - {name: Bun,          evidence: [torii]}
  - {name: PostgreSQL,   evidence: [wd.infra], aliases: [Supabase]}
  - {name: SQLite,       evidence: [torii]}
  - {name: AWS,          evidence: [pash], aliases: [S3, SQS, EC2, Lambda]}
  - {name: MCP,          evidence: [torii]}
  - {name: x402,         evidence: [torii]}
  - {name: Whisper,      evidence: [myt.voicesql]}      # "OpenAI/Whisper" slash split per r/ER rule
  - {name: Mapbox,       evidence: [wd.locator]}
  - {name: Three.js,     evidence: [portfolio]}
  - {name: Go,   evidence: [], flag: unevidenced}       # keep ONLY if he confirms interview-ready; else cut
  - {name: Java, evidence: [], flag: unevidenced}
  - {name: C++,  evidence: [], flag: unevidenced}
  - {name: Rust, evidence: [], flag: unevidenced}
  # Selenium moves out of "AI & Agents" (it is browser automation) — categorization lives in variants.yaml

protected_strings:                    # LLM may SELECT these, never reword; rendered forms noted
  - "built the full stack in a day"
  - "two production dependencies"
  - "Ctrl+F-and-edit workflow"        # prose form of his "CTRL+F --> edit"; the --> glyph never enters a PDF
  - "time-series deduplication"
  - "pre-authorization budget tracker"
  - "App Review Guideline 2.1"
  - "USDC on Base via viem"
  - "Motivation × Ability × Timeline"

never_include:
  - {item: "Delhi Public School R.K. Puram / 93%",  reason: "high school off US grad resumes"}
  - {item: "Tempe, AZ as current location",          reason: "stale; he is in NYC"}
  - {item: "hidden text / white-font / injected prompts", reason: "visible in parsed layer; treated as fraud"}
  - {item: "certifications section",                 reason: "no target program requires any; wasted lines"}
  - {item: "summary section (default)",              reason: "student norm; one tailored line allowed for HR-screened campus roles only"}
  - {item: "pronouns / photo / street address",      reason: "US resume norms"}
```

---

## 4. THE ANTI-AI RULESET (`lint_voice.py` — deterministic, blocking)

**Register split (from career-ops, adopted):** Tier 1 applies to ALL output; Tier 2 (conversational calibration) applies ONLY to cover letters and emails — the resume keeps the formal keyword-dense register. **Precedence rule: accuracy beats style — never soften a real metric for rhythm, never invent detail to sound human.**

### 4a. Lexicon (BANNED.txt, case-insensitive substring grep; any hit = hard fail)
```
# resume-speak he never uses
spearheaded  leveraged  leveraging  utilized  utilizing  orchestrated  synergy
results-driven  detail-oriented  proven track record  dynamic  innovative
passionate  self-starter  honed  crafted  pioneered  myriad  adept  tech-savvy
# AI-tell vocabulary (Kobak et al. + Wikipedia Signs-of-AI-writing)
delve  tapestry  testament  landscape  showcase  showcasing  foster  fostering
pivotal  crucial  meticulous  meticulously  robust  seamless  seamlessly
cutting-edge  state-of-the-art  comprehensive  holistic  intricate  underscore
boasts  garner  elevate  elevated  empower  empowered  streamlined  vibrant
deep dive  best-in-class  evolving landscape  cultivated  bolstered  invaluable
realm  interplay  ever-evolving  plays a pivotal role  plays a crucial role
resulting in  commitment to  align with  aligns perfectly  fast-paced environment
# cover-letter skeleton (letters only need these but grep everywhere; resumes never contain them anyway)
i am writing to  to whom it may concern  dear sir  dear madam
i would welcome the opportunity  excited to join  thrilled  eager to
unique opportunity  perfect fit  strong track record  uniquely qualified
mission resonates  resonates with me  references available upon request
please do not hesitate  my skills align  valuable asset  hit the ground running
```
**Warn tier (allowed once per document, only when literal/technical):** `optimized/optimizing` (his Delhi line legitimately says "optimizing Gaussian Process Classifiers"), `enhanced`, `facilitated`, `ensured`, `enabled`.

### 4b. Construction regexes (per sentence/bullet; hit = hard fail)
| Rule | Pattern (case-insensitive) | Fix |
|---|---|---|
| Negative parallelism | `\bnot (just|only|merely|simply|about)\b[^.;]{0,80}\bbut\b` and `\bisn'?t [^.;]{0,60}[.;]\s*(it|this|that)'?s\b` | delete everything before the positive claim |
| Copula avoidance | `\b(serves|stands|functions|acts) as an?\b`, `\brepresents a\b` | use "is" or a concrete verb |
| Participial trailer | `,\s(highlighting|ensuring|showcasing|underscoring|reflecting|demonstrating|fostering|enhancing|emphasizing|solidifying|contributing to|paving the way)[^.]*\.$` | end the sentence at the fact |
| Bolded bullet lead-in | line starts `[-•] \*\*[^*]+:\*\*` or rendered bold label + colon | plain sentence bullets |
| Vague attribution | `\b(experts (say|argue)|industry reports)\b` | name the source or cut |

### 4c. Punctuation
- Em dash (U+2014): **0 in cover letters, ≤1 total in a resume** (his voice uses them, but 2026 reader priors lose; periods/commas/colons/parentheses instead).
- `.txt` and email-body outputs: ASCII only — straight quotes, `-` hyphens, no bullets glyphs, blank-line paragraphs, start at the salutation.
- PDFs: typographic quotes/en-dashes allowed (whitelisted in §5), U+2022 bullets in the text font.
- Never in any output: `→`, `-->` (render the Ctrl+F detail as prose), emoji, icon-font glyphs, title-case headers mid-sentence, semicolons >2 per letter (warn).

### 4d. Structural counters (deterministic)
- ≤2 bullets on the page share a first word ("Built" currently opens 5 of 9 — regression test).
- Bullet length variance: fail if all bullet char-counts fall within ±15% of the mean; mix sub-10-word and 2-line bullets deliberately.
- ≤60% of bullets carry an achievement numeral (reuse the fact-gate numeral extractor; date tokens excluded).
- ≥1 un-rounded number per document (2,129 / 0:55 / 4 / "in a day" all qualify).
- Max one `, X, and Y` triad per document flagged for the critique pass; **verb chains naming real pipeline stages are exempt** ("intercepts, checks, pays, and retries" is his native rhythm), adjective triads are not.
- Max one parallel aphorism per document.
- No summary section unless the variant preset explicitly enables its one-line form.

### 4e. LLM gates (separate fresh-context calls, after the deterministic lint)
1. **Adversarial critique:** given only VOICE.md §2 exemplars + the draft: "Name the 3 lines that could appear on any CS student's resume. Rewrite from the exemplars or delete." (Same-context self-review is forbidden — it grades its own work.)
2. **Only-him count:** ≥3 details per page no other candidate could have (two production dependencies, Ctrl+F workflow, Guideline 2.1, walkable-computer portfolio, 100 workers at 17, torii-gate naming...). Fail = reselect atoms.
3. **Letters only — company-swap test:** any sentence that survives find-and-replace of the employer name gets rewritten or cut; every paragraph must contain ≥1 fact traceable to profile.yaml AND ≥1 employer-specific noun.

### 4f. What the system must never write (emit prompts to `HUMAN_INPUT_NEEDED.md` instead)
Why-this-job/why-NYU sentences; cover-letter opening lines; the CovreliefDwarka narrative; humor; anything personal beyond the fact sheet. Letters are assembled: **his** opening + system-drafted fact middle in his declarative register + plain logistics close ("I'm on campus daily; the projects live at asmit.space."). Never run output through "humanizer" tools; never optimize against AI detectors (documented bias against non-native English writers — keep Liang et al., *Patterns* 2023 on file as rebuttal if ever falsely flagged).

---

## 5. ATS RULESET

Reality this encodes: no major ATS auto-rejects on resume content (knockout *questions* do that); recruiters search literal tokens; Workday never auto-fills Skills fields from the resume; Handshake caps uploads at 1MB and NYU on-campus applications are read by humans; parsing engines behind any ATS change without notice (Greenhouse's own parser vendor changed between 2024 subprocessor lists) — so **test against multiple independent extractors, never tune for one engine.**

### 5-A. Renderer rules (baked into `resume.typ`, enforced by `lint_facts.py` where textual)
1. Single column. No tables, text boxes, header/footer objects, images, icons, photos, letter-spacing, or graphics of any kind.
2. Literal section headings only: `Education`, `Experience`, `Projects`, `Skills`, plus `Leadership & Teaching` where the variant uses it. Education first (grad-student norm).
3. Contact block as plain body text under the name: `New York, NY · <phone> · asmit77@icloud.com · linkedin.com/in/asmitrajeet · github.com/<user> · asmit.space` — visible bare URLs (no `https://www.`), each also a link annotation (extractors ignore annotations; the visible text must BE the URL).
4. Dates: `May 2025 – Jan 2026` (Month YYYY, spaced en dash), `Present` only where true; education shows graduation only (`Expected May 2028`, `May 2026`), no ranges, no trailing periods on degree lines.
5. Full unabbreviated titles; org names as registered.
6. `#set text(hyphenate: false)`; left-aligned (`justify: false`); ligatures ON (Typst writes correct multi-codepoint ToUnicode — measured); lining figures.
7. Every load-bearing technology appears **inside an experience/project bullet**, not only in Skills (Workday ignores the Skills block for structured fields); keep the Skills section anyway for humans and recruiter search. Each matched JD term appears verbatim exactly once or twice — never stuffed.
8. Zero hidden text, white-font tricks, or injected prompts — the parsed layer is exactly what the recruiter reads, and discovery is treated as fraud.
9. One page (deterministic knob loop, §6 step 7). File `Asmit-Datta-Resume.pdf` (Handshake shows the filename), size <1MB.
10. Body 10pt Constantia floor 9.5pt; margins 0.6in floor 0.5in — going below the floors is itself a machine tell; fail loudly instead.

### 5-B. Verification gate (`verify_pdf.py` — runs on EVERY artifact; any failure = artifact never emitted)
```
1. TRIPLE EXTRACTION: pymupdf.get_text(), pypdf.extract_text(), pdfminer.six high_level
   (pypdf + pdfminer are the two engines that FAILED on his LinkedIn export — perfect regression pair).
2. TOKEN ROUND-TRIP: every load-bearing token from the render JSON must appear verbatim in ALL
   extractions: name, email, phone, every org, every title, every date string, every skill keyword,
   every metric value. Catches unmapped subsets, dropped runs, ligature damage in one test.
3. CODEPOINT AUDIT: whitelist ASCII + U+2013 U+2014 U+2018 U+2019 U+201C U+201D U+2022.
   HARD FAIL on U+FB00–FB06 (presentation ligatures), U+00AD (soft hyphen), word-internal U+2010,
   U+037E, U+FFFD, any PUA U+E000–F8FF (icon fonts).
4. ORDER: index of each section heading in extracted text strictly increasing vs. intended order.
5. METADATA (pypdf): /Author == "Asmit Datta"; /Title set; /Creator contains none of
   {HeadlessChrome, Skia/PDF, WeasyPrint, ReportLab, Mozilla}.
6. STRUCTURE: page_count == 1 (len(pymupdf.open(p))); file size < 1,000,000 bytes;
   every font emb=yes (page.get_fonts()); underfill check (last text block ends < 60% of page
   height => warn "thin page, add content").
7. LINK CHECK (weekly + before each batch): every asmit.space / linkedin / github URL resolves 200.
```
Run this gate against his **current LaTeX-produced resume PDF today** (§8 item 0) — this machine's Tectonic reproduces the U+037E/U+FBxx defects, so the resume he is sending right now may already be partially keyword-blind.

DOCX variant check: unzip, grep `word/document.xml` — `<w:tbl>`, `<w:txbxContent>`, `headerReference` all absent; docProps creator/lastModifiedBy = "Asmit Datta".

---

## 6. TAILORING PIPELINE (job posting → submitted application)

Core architectural decision, resolving the schema-vs-tailoring track conflict: **the ship path is selection-only** — the renderer prints `approved:true` variant text verbatim and has no free-text path. Rewriting exists but only feeds the **review queue**: when no approved variant covers a JD term, `review_queue.py` drafts a new variant (whitelist transformations only: vocabulary mirroring with identical referents, emphasis reordering, detail selection, acronym expansion — never new numerals, ownership upgrades, scope upgrades, or cross-tool substitution), runs a fresh-context entailment judge on it (claim + cited source atoms only), and parks it `approved:false` until Asmit edits/approves the wording. This makes shipped text his prose (anti-AI) and makes fabrication structurally impossible (anti-fabrication), and it means the expensive judge runs once per new variant, not once per application.

| # | Step | Who |
|---|------|-----|
| 1 | `new_app.py <url-or-pasted-JD>`: snapshot JD text to `applications/snapshots/`, hash it, scaffold the application record | AUTO |
| 2 | Parse JD → typed object: `{knockouts[], hard_requirements[], preferred[], responsibilities[], vocabulary_map, writer_is_technical}` — one LLM extraction with raw-quote provenance per field + deterministic regex post-pass for hours, GPA floors, grad-date windows, "work-study", "sponsorship", "citizen" | AUTO |
| 3 | Knockout check: any `satisfied: UNKNOWN` **halts** and emits a question. FWS-only postings flagged ineligible if F-1. Hours >20/wk during term flagged (SEVIS-terminating if F-1; NYU cap regardless). **The system never answers a screening question — knockout answers are routed to Asmit verbatim** | HUMAN |
| 4 | Ledger pre-check (`ledger.py`): if this employer was applied to before, inject frozen facts (same numbers, titles, dates, location, availability) as hard constraints. All NYU departments count as one employer surface | AUTO |
| 5 | Three-bucket skill report (career-ops pattern, ~200 lines regex, zero tokens): each JD requirement → `existing` (named in skills w/ evidence) / `supported` (demonstrated in a fact) / `gap`. **Gaps are printed to Asmit, never papered over**; Skills/competency lines may only draw from the first two buckets | AUTO, gaps shown to HUMAN |
| 6 | Variant preset chosen by role type (§7); then greedy marginal-coverage selection of variant ids under the line budget (~46–50 content lines): `score = 3.0·new-hard-coverage + 1.5·new-preferred + 1.0·responsibility-sim + 0.75·uniqueness + 0.5·recency − 2.0·skill-overlap-with-selected`; constraints: ≥2 experience roles shown, 2–3 bullets per shown role, ≤3 projects, one variant per fact (variants of a fact are mutually exclusive), entry order per preset. Missing coverage → review-queue proposals (see above) | AUTO; new variants HUMAN-approved |
| 7 | `render.py`: assemble JSON → `typst.compile(sys_inputs={"data": json})` → page count via pymupdf → if >1, deterministic knobs in order: drop `priority:3` bullets → 10→9.5pt → leading 0.65→0.58em → margins 0.6→0.5in → **fail loudly** (never LLM-shorten-to-fit) → pypdf metadata pass | AUTO |
| 8 | Gates in sequence, all blocking: `lint_facts.py` (numeral whitelist incl. magnitude-suffix + unicode-digit folding; controlled tech/proper-noun vocab; ownership-verb check incl. delegated-authorship "vendor built it" ≠ "built"; needs_confirmation block) → `lint_voice.py` (§4a–d) → LLM critique + only-him gates (§4e) → `verify_pdf.py` (§5-B) | AUTO |
| 9 | Cover letter (when the posting takes one): four-question gate — **refuses to draft until Asmit answers: (A) why this role/company (B) what problem you'd solve for them (C) your first move (D) tone** — his answer to A becomes the opening; system drafts the fact middle from selected atoms; plain logistics close. Length by context: on-campus 150–250 words, startup 5–10 sentences, corporate ≤400/one page, professor email ~one screenful. Emit 3 artifacts: letterhead PDF (<1MB), ASCII `.txt` paste variant, email-body with subject + signature. Never attach AND paste the same letter. No keyword pass on letters, ever | HUMAN answers, AUTO assembles, HUMAN reads |
| 10 | Professor email (distinct genre, replaces the letter for RA/grader outreach): 3 short paragraphs, one screenful — intro (name, "first-year M.S. CS at NYU", ask + when), why-this-professor with one paper cited by exact title + one genuine technical question (**generation refuses without this hook**), 1–2 relevant experiences (Delhi GP research is load-bearing) + 15-min ask + out. Subject built from their research topic. Attach 1-page PDF + plain-text links. One professor at a time; follow up once in-thread after ~5 business days; **obey any posting/page instruction not to contact the supervisor.** (Professor outreach is community-wiki advice, not official NYU channel — pair it with the officially confirmed Courant CS opportunities mailing list) | HUMAN hook + send |
| 11 | Write the application record: `variant_ids`, `profile_commit` (render refuses on a dirty git tree), `claims_shipped` (every metric + status at ship time), `statements_made` (location, availability, exact work-auth answer given), output sha256. Emit `HANDSHAKE_PROFILE.md` sync checklist for on-campus apps (grad date May 2028, Masters, CS major, GPA, work-auth fields, variant-neutral headline) — Handshake filters read profile fields, not the resume | AUTO |
| 12 | Human reviews the PDF and submits. For Workday/iCIMS: upload resume FIRST (iCIMS parses only on upload), then verify every autofilled field. The system never submits anything | HUMAN |
| 13 | Post-interview prep: `ledger.py check <app_id>` prints exactly what that employer was told, and diffs against current profile if any metric changed since | AUTO |

---

## 7. RESUME VARIANTS

Four selection/ordering presets over ONE fact base (`variants.yaml`) — never separate hand-maintained documents. Frozen across all: name, contact, dates, titles, education institutions, every number. Handshake profile stays variant-neutral.

| Preset | Section architecture | Leads with | Key selections | Notes |
|---|---|---|---|---|
| **`campus-ta`** (CA/grader/tutor) | Education → Experience (AI Society **promoted to full entry**, WatchDNA, Delhi) → Skills → Leadership & Teaching (Covrelief once unblocked) | ais.mentoring.t, ais.workshops.t | Coursework line on NYU entry (once known — grader JDs knockout on course grades); one SWE role for credibility; 1 project max; availability "up to 20 hrs/week during term" in the letter | Teaching evidence IS the qualification here |
| **`ra-research`** | Education → Experience (Delhi **restored**, MyYogaTeacher, AI Society) → Projects (SentinalAI when unblocked, Torii) → Skills | du.gpc.r + methods detail once filled | Methods-forward tone; asmit.space writing line; pairs with professor-email kit, not a cover letter | Delhi entry is the single best on-campus credential |
| **`swe-intern`** (Summer 2027) | Education → Experience (WatchDNA, MyYogaTeacher, Flickmatch-or-Delhi) → Projects (Torii, Pash or LEAD ENGINE by stack) → Skills → Leadership & Teaching (AI Society lives HERE, defusing the three-concurrent-roles read) | wd.locator.full, wd.infra.backend, myt.biometrics.* | Languages/Backend skills categories first; GitHub link required (blocks batch until MVP exists) | Closest to current resume; ships first |
| **`ml-ai-infra`** | Education → Experience → Projects (Torii FIRST with one_day + two_deps verbatim) → Skills ("AI & Agents" category first) | torii.core.infra, torii.core.pay, myt.voicesql.*, le.pipeline.ml | Delhi GP research as depth signal; pash for GPU/queue systems | The x402/MCP surface almost no student has |

Per-variant entry **placement** (AI Society in Experience vs Leadership) is a preset property — resolves the tracks' conflict: teaching roles want it as Experience; SWE roles want the overlap defused.

Letter profiles (4): on-campus Handshake (150–250 w, availability sentence mandatory, mentoring facts first), startup note (5–10 sentences, no ceremony), corporate/research formal (≤400 w, letterhead matches resume), professor cold email (own genre, §6 step 10). DOCX twin renders any preset on demand.

---

## 8. THE FIX LIST FOR HIS CURRENT MATERIALS (ordered by impact)

0. **[TODAY, 10 min] Run `verify_pdf.py` on the current resume PDF.** It is LaTeX-produced; this machine's toolchain reproduces the U+037E/U+FBxx defect class — the resume going out right now may be partially keyword-blind. Immediate, free value.
1. **[BLOCKER] Add the missing 40% of his profile:** University of Delhi Research Study Assistant (absent entirely — his best RA/on-campus credential) as a full Experience entry; AI Society Technical Officer promoted out of the ASU education-line fragment (currently an ATS parsing hazard AND buried teaching evidence) into a standalone entry.
2. **[BLOCKER for SWE batch] GitHub MVP (~4 hrs, his task):** account with real name; push Torii + Pash + one more, each README with 2-sentence what/why, architecture sketch, screenshot, run instructions; pin; Torii README carries "built the full stack in a day... two production dependencies" verbatim. A 7-project resume with zero repo links reads "projects may not be real." Then add URL to header + LinkedIn.
3. **[HIGH, 45 min] LinkedIn de-staling** (recruiters cross-check in the first screen): location Tempe → New York; remove/retarget the stale "Open to work — Tempe, AZ" banner; headline "CS @ ASU'26" → NYU '28 form; add NYU education entry; end-date the six finished projects; add GitHub + asmit.space to contact.
4. **[HIGH] Metric triage:** keep `2,100+ leads` (2,129 — countable) and `5–10x` GPU (honest benchmark). Block `~50% AI-call conversion` (resume-only, implausible denominator — poisons every other number) and `70% prospecting cut` (no baseline exists) until he states the measurement or they die. `99.9% uptime` → mechanism rewrite by default ("offline-first sync with time-series deduplication that survives flaky networks without losing data") unless he states what was measured. `60%` → ask basis; mechanism variant ships meanwhile. Never emit a number he can't defend end-to-end in an interview.
5. **[HIGH] Header:** add phone + GitHub; keep "New York, NY"; strip `https://www.` from all URLs; delete the summary section (the "comfortable owning the full stack... moving fast" sentence is the most AI-flavored text on the page and duplicates content below it).
6. **[HIGH] Education lines:** "New York University — [School once confirmed], M.S. in Computer Science, Expected May 2028"; ASU "May 2026"; kill bare years, trailing periods; ASU GPA printed only if ≥3.5 as "X.XX/4.00".
7. **[MED] Project dates:** max one "— Present" (Torii); end-date the rest; reconcile Portfolio 2024 (resume) vs Feb 2025 (LinkedIn) to one truth everywhere; confirm "SentinalAI" spelling before it ever prints (a misspelled project name is disqualifying-adjacent).
8. **[MED] Skills surgery:** Languages trimmed to TypeScript, JavaScript, Python, SQL + any he confirms interview-ready (Go/Java/C++/Rust currently have zero evidencing artifacts — an interviewer opening with Rust ownership semantics is a self-inflicted wound); Selenium out of "AI & Agents"; "OpenAI/Whisper" split; add evidenced differentiators per variant (Supabase, Expo, Mapbox, spaCy, YOLOv8, Electron, Blender, viem); every listed skill must appear in a bullet.
9. **[MED] Bullet voice pass:** "Built" opens 5 of 9 lines — vary openers (Shipped, Ran, Set up, Wrote, Cut, Mentored); import LinkedIn-only human specifics (one-day build, two deps, Guideline 2.1, backtesting, county records); Flickmatch rewritten to one plain line ("Implemented Figma designs as responsive Material-UI components") or dropped when space is needed; render "CTRL+F --> edit" as prose "Ctrl+F-and-edit workflow" (detail kept, arrow glyph never enters a PDF).
10. **[MED] LEAD ENGINE public phrasing:** "public listing and county-record data sources," never "scrapes Zillow/Redfin/MLS" (ToS exposure on public materials).
11. **[MED] CovreliefDwarka:** blocked until the timeline is resolved (May–Sep 2020 predates COVID vaccines — as written it is temporally impossible and an interviewer catching it is fatal); once resolved, one Leadership line — it is his strongest humanizer.
12. **[LOW] Add** a one-line writing credit ("Technical essays on agent payments and BCI at asmit.space"); send 4 recommendation/reference requests this week (WatchDNA supervisor, MyYogaTeacher manager, Prof. R. P. Singh, AI Society advisor); build a separate references sheet (never on the resume).
13. **[LOW] Skip forever:** certifications, keyword-stuffing, "ATS score" tools, humanizer tools, a photo, pronouns on the doc.

---

## 9. OPEN QUESTIONS FOR ASMIT (ranked by how hard they block)

**TIER 1 — block all application-facing output:**
1. Work authorization: F-1? (Gates every sponsorship knockout answer, FWS filtering — F-1 = non-FWS postings only — the Form B → I-9 in PeopleSync → SSN checklist, and CPT for off-campus internships.) The system refuses to touch a screening question until this is answered.
2. Phone number. (Every portal.)
3. NYU school — Courant or Tandon? — exact program name as the transcript states it, start date, fall course list. (Gates the education line, grader-variant coursework, GSET eligibility if Tandon, which mailing lists exist.)

**TIER 2 — block specific variants/bullets:**
4. ASU GPA + any honors/dean's list. (≥3.5 prints; GPA-screened postings.)
5. GitHub URL — or green-light creating the account + MVP repos this week. (Blocks the SWE batch.)
6. Metric bases, one sentence each: how was 60% admin-cut measured? What exactly is "~50% AI-call conversion" (what denominator)? Is "70% prospecting cut" real against any baseline? What does 99.9% measure? (Unanswered = mechanism rewrites ship instead.)
7. CovreliefDwarka: what actually happened, when, and to whom — the dates conflict with COVID vaccine availability. (Blocks the entry.)
8. Delhi research: dataset, method, any result or artifact? (Gates RA-variant depth and professor emails.)

**TIER 3 — block polish items:**
9. Portfolio date: 2024 or Feb 2025? (One truth, all surfaces.)
10. Full truncated descriptions: NeuroPilot, SentinalAI (+ intended spelling), Lynti, CovreliefDwarka.
11. Go/Java/C++/Rust: interview-ready in any of them, or cut?
12. WatchDNA companion app: App Store outcome — launched, or through review? (Chooses the bullet phrasing.)
13. Weekly availability for on-campus roles (≤20 hrs term-time), and permission to list the 4 reference targets.

---

## 10. BUILD ORDER

**Phase 0 — today (~2 hrs):** `git init` + venv + installs (§1); run `verify_pdf.py` logic ad hoc against the current resume PDF; copy `VOICE.md` and `RAW_PROFILE_FACTS.md` into `profile/`; send Asmit the Tier 1+2 intake questions; he starts the GitHub MVP in parallel. Also: apply-now flag on the Google MS Summer 2027 req (open, rolling, anticipated close 2026-09-25 — soft date; automate a live check with an HTTP GET + grep for "anticipated application window").

**Phase 1 — days 1–2:** `schema/*.json`, seed `profile.yaml` (§3, extended to all entries), `validate.py`, **`lint_facts.py` before any renderer exists** — the provenance gate is the feature that makes "nothing fabricated" enforceable, and it already has three real catches queued (Covrelief timeline, ~50% conversion, unevidenced languages). Asmit's approval pass: read every variant aloud, edit, flip `approved: true`.

**Phase 2 — days 2–3 (first shippable):** `resume.typ` (single column, Constantia/Corbel, §5-A rules), `render.py` with fit loop + pypdf metadata pass, `verify_pdf.py` wired as blocking. Render the **`swe-intern`** variant, run all gates, and start the Summer 2027 batch (Google MS req, SimplifyJobs Summer2027 list, Handshake first pass) — recruiting is rolling and mid-cycle; do not wait for the rest of the system.

**Phase 3 — days 3–4:** `lint_voice.py` + `BANNED.txt` + the two LLM gates; `letter.typ` + `emit_letter.py` (3 artifacts, four-question gate); `new_app.py` + `ledger.py` + application records + `HANDSHAKE_PROFILE.md` emitter. LinkedIn fix checklist executed.

**Phase 4 — days 4–5:** `campus-ta`, `ra-research`, `ml-ai-infra` presets in `variants.yaml`; professor-email kit (subscribe to the Courant CS opportunities mailing list — the officially confirmed channel — and draft 3–5 instructor emails once Tier 1 Q3 is answered); `review_queue.py` with the entailment judge; DOCX twin (`docxtpl`).

**Phase 5 — as needed:** `select.py` knapsack refinement + `measurements.json` cache (greedy-by-hand works for v1); JD-parser prompt hardening; JSON Resume lossy export; OFL font vendoring with `ignore_system_fonts=True`; **calendar trigger 2026-11-15** to regenerate for Spring 2027 CA/grader postings.

**Never build:** portal scanners, batch triage, liveness checks, follow-up/negotiation engines, dashboards, SQLite trackers beyond the YAML ledger, Canva/Figma flows, multi-language modes, keyword-coverage scoring, AI-detector optimization, hidden-text anything — the 80% of career-ops that serves a 740-posting senior search, not one NYU student with a dozen targets and a deadline this month.
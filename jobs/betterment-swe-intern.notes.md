# Betterment — Software Engineering Intern, New York (hybrid)

Posting: `jobs/betterment-swe-intern.md`, saved 2026-09-07. Preset:
`betterment-swe-intern`. Letter: `letters/draft-betterment-swe-intern.py`.
Package: `applications/betterment-swe-intern-summer-2027/`. Pay $35-$45/hour.

## 1. Knockouts

| Gate | Status |
|---|---|
| **"Graduating in Spring/Summer 2026"** | **AMBIGUOUS - check the form before applying.** His B.S. was May 2026, which satisfies the line literally; his M.S. runs to 2028. Either the text is last cycle's (posted for Summer 2026 and never updated) or Betterment wants people about to finish school ("loves to hire their interns when they finish school"). The posting never states the internship term. If the form asks for graduation date, the honest answer is the M.S. date, 2028, and the letter's "available from June 2027" assumes a Summer 2027 term. **His to check; nothing assumed on the form.** |
| Work authorization | **F-1** (2026-09-07). An off-campus internship needs CPT through NYU, which is routine for a summer internship tied to the degree. Any "will you require sponsorship" question is his to answer, never ours. |
| Prior internship experience at a startup or similar | **PASS** - WatchDNA, MyYogaTeacher, Flickmatch. The word "startup" is not claimed anywhere; the company names carry it. |
| Side project work completed outside of school | **PASS** - Torii, Pash, Lead Engine, Portfolio. |
| Majors: CS | **PASS** |
| Location: NYC office, hybrid | **PASS** - he is in New York. |
| Stack: "some of these listed or related" - Java, JavaScript, Ruby, Python, HTML, CSS, Mobile Dev, Web services, Git, SQL | **PASS on nine of nine** since the evening rebuild of 2026-09-07: Java and Ruby joined the Languages line on coursework evidence, under his standing instruction (CLAUDE.md, "Keywords he covered in a class"). |

## 2. Background (researched 2026-09-07)

- **Engineering blog**, https://www.betterment.com/engineering - **verified**:
  posts visible on the index include "End-to-end-ish tests using fake HTTP
  in Flutter", "Finding a Middle Ground Between Screen and UI Testing in
  Flutter", "Why (And How) Betterment Is Using Julia", "Stability through
  Randomness". Tags: Building culture, Testing software, Operating software,
  Solving problems, Designing experiences, Data & Algorithms, Inclusivity.
  So: Flutter for mobile, Julia for some computation.
- **Operating-software tag page**,
  https://www.betterment.com/engineering/tag/operating-software -
  **verified**: "Introducing 'Delayed': Resilient Background Jobs on Rails",
  "Focusing on What Matters: Using SLOs to Pursue User Happiness", "WebValve
  - The Magic You Need for HTTP Integration". No dates on the page. **The
  Delayed post is the letter's one anchor; he reads it before sending.**
- **Search snippet, not fetched:** the Rails application "performs millions
  of asynchronous tasks, including transactional emails, push notifications,
  money movements (deposits, withdrawals, transfers, rollovers), and syncing
  customer account information" - almost certainly the Delayed post's
  opening. Not quoted in the letter because not read on the page.
- **GitHub**, https://github.com/Betterment - **search snippet**: active Ruby
  repositories (Rails engines, an ActiveJob backend, demo mode for Rails
  apps), updated as recently as August 2026. Ruby is the house language.
- **Internship shape** - **search snippets** (startup.jobs, weekday.works):
  roles across full-stack, backend and mobile, all in Manhattan; each intern
  paired with a mentor; "meaningful project ... embed with engineering teams
  that are delivering code to production." Company: largest independent
  online financial advisor, SEC-registered, FINRA member.
- Not found: the term, the application deadline, who reads the letter.

**What it implies.** The reader is an ATS, then a recruiter, then an
engineer on a Rails-and-Flutter team. The seam is money moved carefully:
Torii's reserve-before-call budget tracker and its ledger are the closest
thing on the profile to that instinct. Ruby is the honest gap; the letter
does not pretend otherwise and does not mention it.

## 3. What leads on the resume, and why

Preset `betterment-swe-intern`, modelled on `paypal-swe-2027`.

- **Experience: WatchDNA, MyYogaTeacher, AI Society, Delhi.** The posting's
  first ask is internship experience at a startup or similar, so Experience
  goes first and the two engineering internships lead. MyYogaTeacher now
  opens with the wireframes-and-user-journeys bullet (recorded 2026-09-07).
  Flickmatch is off (the standing first cut).
- **Projects: Torii, Pash, Lead Engine, Portfolio.** Torii first for the
  reason above; Pash second because the posting asks for side projects
  finished outside school and Pash is a queue-based pipeline; Lead Engine for
  the scale; Portfolio last and the first project cut if the page is tight.
- **Skills** lead with their list in their order: Java, JavaScript, Ruby,
  Python, HTML/CSS, TypeScript, SQL; then Node.js, REST, Express, FastAPI,
  JWT; React Native, Expo, React; Git, PostgreSQL, SQLite, AWS.
- **Automation, DevOps, Software testing** joined the Data & Cloud line on
  2026-09-07 (his instruction on the MiniMed posting): Automation on project
  evidence, the other two on coursework. The WatchDNA locator bullet now
  says "automated Python pipeline" (`wd.locator.auto`). Rebuilt; still one
  page, six links, ATS PASS.
- **Java and Ruby are on the page on coursework evidence**
  (`coursework_2026-09-07`), on his instruction that evening: "I have taken
  everything in some or the other class ... we are trying to maximise the
  keyword matching." Skills block only; neither appears in a bullet. Every
  other `ask: true` skill stays excluded.

## 4. Requirement mapping

| Their line | Status | Him |
|---|---|---|
| JavaScript, Python, HTML, CSS, SQL, Git | existing | skills with evidence; inside bullets at WatchDNA, Lead Engine, MyYogaTeacher |
| Mobile Dev | existing | two React Native apps (MyYogaTeacher, WatchDNA companion) |
| Web services | existing | WatchDNA REST + JWT; Lead Engine FastAPI; Torii proxy |
| **Java** | on the page, coursework evidence | also on his own 2026 resume. **Interview prep:** name the course and one thing built in it. |
| **Ruby** | on the page, coursework evidence | Betterment's house language. **Interview prep:** which class covered it, and be ready for a Rails question anyway. If no class did, tell the system and it comes off. |
| Startup internship | existing | WatchDNA, MyYogaTeacher, Flickmatch |
| Side projects outside school | existing | Torii, Pash, Lead Engine, Portfolio |
| "Pick up a new language or tool in a few sessions" | supported | Pash (Demucs, S3, SQS, CUDA worker, nobody to ask); Torii built in a day. Shown, not echoed. |
| "Ideas helped shape the last group project ... compelling narrative" | supported | MyYogaTeacher feature design (wireframes to build); AI Society workshops. Not claimed as a phrase. |
| Collaborative instincts, continuous learning | soft | the personal paragraph |
| Fintech domain | **GAP** | nothing; Torii's budget logic is the adjacency |

## 5. Letter

Internship genre. The internship personal paragraph (byte-identical to
`draft-google-swe-intern.py`, verified on build), the portfolio signpost,
two technical paragraphs, the standard one-line close. **Second version,
2026-09-07 evening, on his instruction: no Torii, internships only, owning
the work shown through examples, a little more on what each achieved.**

- Paragraph 1: one hinge sentence (what he was handed became his to finish,
  from the first drawing to the alert that fires when it breaks), then
  WatchDNA in full: nine months; backend from scratch on Node.js; the store
  locator (Mapbox map, admin console, the endpoint-discovery pipeline); the
  companion app on Expo and Supabase reusing the same auth and data layers,
  taken through App Store review including the reviewer correspondence;
  alerts (his words). "Launched" is not said (intake #12).
- Paragraph 2: MyYogaTeacher - given the initial design of a feature,
  diagrams, wireframes and user journeys, built against his own drawings
  (`myt.design`); the offline-first client; voice-to-SQL replacing the
  Ctrl+F workflow. Flickmatch - the whole site from new Figma designs, state
  management as modular pieces.
- Close: "I am in New York and available from June 2027." **The term is
  assumed** (section 1).
- The Delayed-post anchor from the first version came out with Torii; the
  research stays in section 2 for the interview.
- Not claimed: the blocked numbers, that the companion app launched, Java or
  Ruby beyond the skills block, "startup", fintech knowledge, any side
  project.
- Measured: 490 words, one page, three link annotations, lint 0 block /
  0 warn / 0 note after splitting three long sentences.

## 6. Questions for Asmit

1. **Which term is this posting for, and what does the form ask about
   graduation?** The "Spring/Summer 2026" line is the one thing that could
   make this a wasted application. Check on the Betterment careers page
   before uploading.
2. **CPT.** A summer internship off campus needs CPT through NYU OGS; it is
   routine but it has a timeline. Worth knowing before an offer, not after.
3. **Ruby and Java: which classes?** Both are on the page on your word that
   you covered them in coursework. Name the course for each so the interview
   answer is ready. If no class covered Ruby, say so and it comes off.
4. **The Delayed post.** Read it before sending; the letter names it.

## 7. Built

Built 2026-09-07; rebuilt the same evening with Java and Ruby on the Languages
line. Resume: ATS PASS, one page, 95% fill, six link annotations; Languages
reads "Java, JavaScript, Ruby, Python, HTML/CSS, TypeScript, SQL"; no
`ask: true` skill renders; trimmed to fit: Uvicorn, Selenium,
iOS App Store, Wireframing, User journeys, LLM streaming, YOLOv8, Demucs,
Gaussian Processes. Letter (second version, internships only): one page, 490 words, three link
annotations, lint 0 block / 0 warn / 0 note after splitting three long
sentences; over the internship "under 400" target for the standing reason
(the constant paragraph is about 190 words). Personal paragraph verified
byte-identical to the Google draft. Draft build. The one note the build
prints: no phone number in the profile (intake #2), and this portal will
ask for one.

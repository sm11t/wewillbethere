# NYU Center for Undergraduate Research — General Research Assistant (graduate pool), Fall 2026

The cover letter is the application here. The Director reads it, and faculty
requests are matched against what it declares: school, programme, interests,
skills. The resume is the attachment, not the pitch.

## 1. Knockout check

| Gate | Status |
|---|---|
| Currently enrolled graduate student at NYU | **PASS** — NYU M.S. Computer Science, expected 2028. School prints as **Tandon** since 2026-09-07, inferred from his CS-GY registration at 6 MetroTech (`education.nyu.school_inferred`) and flagged to him; he has not said the word. Intake item 3. |
| "US work authorization required" | **ANSWERED 2026-09-07: F-1** (`basics.work_authorization`). On-campus work needs no CPT; 20-hour combined cap in term; not FWS-eligible, so the pre-screen disadvantage below is real. Earlier note kept: intake item 1. An F-1 student may hold an on-campus job without CPT or OPT, capped at 20 hrs/week across all on-campus work while classes are in session and full time over breaks, so the Handshake flag is not by itself a knockout for F-1. Nobody answers this for him. |
| Work-Study | **Usable, not required.** The posting: "Federal Work Study is not required for this role, unless specifically stated." The Center's own page: "students are not required to have FWS eligibility to apply." But the Director's shortlist to faculty is "pre-screened for related intellectual interests, skill sets, and Federal Work-Study eligibility", and an FWS student costs a lab a quarter of the wage. F-1 students are not FWS-eligible. A real disadvantage rather than a knockout — and it is why the skills paragraph has to do more work. |
| Onsite, on campus, New York City | **PASS** |
| Hours: 5–20 hrs/week once matched; up to 35 over breaks if not in classes | **PASS.** Days answered 2026-09-07 (classes Tue and Wed evenings, Fri late morning; Mon and Thu free). Hour count deliberately not stated in the letter: the supervisor sets it once matched, and his on-campus total across GPH, CFA and this is still his call under the 20-hour cap. |
| Dates: Sept 3 – Dec 31, 2026 | Rolling. The Center: "new requests come in from faculty every week." Apply early; the pool is drawn from whenever a supervisor asks. |
| Deadline: Dec 31, 2026, 11:59 PM | The formal close of the pool, not the moment anything is decided. |
| Pay | $30/hr for graduate students, under the Local 7902 agreement. |
| Posting typo | "an end date as late as August 2025" — text carried over from an earlier cycle; read it as August 2027. It also confirms the posting recurs every semester. |
| Follow-up | "Applicants will only hear about next steps if they are contacted by a potential supervisor for an interview." Nothing to chase. |

## 2. Background (researched 2026-09-06)

- The Center for Undergraduate Research sits in the Provost's Office (Office of the Vice Provost for Undergraduate Academic Affairs), not in CAS. It describes itself as working "at the intersection of two of the Provost's Office central missions: teaching and scholarship." <https://www.nyu.edu/about/leadership-university-administration/organization-directory/undergraduate-research.html>
- Director: **Ethan Youngerman**, inaugural Director of Undergraduate Research, hired June 2023 after 21 years in the Expository Writing Program (Clinical Professor). ewy200@nyu.edu; the Provost payroll guide also lists ethan.youngerman@nyu.edu and +1 (212) 992-3865. <https://www.nyu.edu/about/leadership-university-administration/organization-directory/undergraduate-education/ethan-youngerman.html>
- How the pool works: faculty file a URA request form and "choose your level of involvement in the search process"; the Director sends "a shortlist of students who have been pre-screened for related intellectual interests, skill sets, and Federal Work-Study eligibility". <https://www.nyu.edu/research/undergraduate-research/for-faculty.html>
- Scale and reach: "over 325 students were placed with over 100 faculty", on "projects ranging from English to Medicine, in labs and archives, for social justice and art". "The job is posted on Handshake", rolling: "new requests come in from faculty every week". <https://www.nyu.edu/research/undergraduate-research/events.html>
- Funding: when FWS-funded, "75% of the student salary is paid by a United States government grant". The Provost's work-study pilot lets faculty swap research or professional-development funds for FWS dollars to hire "work study eligible" students. <https://sites.google.com/a/nyu.edu/fas-payroll-guide/home/work-study-pilot-provosts-office>
- Graduate students: none of the Center's public pages mentions graduate RAs. The only statement that graduate students are placed is the posting itself ("NYU needs multiple Graduate RAs in a variety of settings across campus every semester", $30/hr graduate rate). Treat graduate placement as real but secondary to the undergraduate programme the office was built for.
- The same posting ran on Wasserman's public feed in an earlier cycle; that copy now returns HTTP 410. <https://wasserman.nyu.edu/jobs/new-york-university-on-campus-general-research-assistant/>
- Where the programming and data demand is. An NYU news piece dated September 2026 on the FWS research programme with NYU Langone, run with Youngerman: 150+ undergraduates matched since summer 2024, in Population Health (IDEAS lab, Omar El Shahawy), Dermatology and Cell Biology (Mayumi Ito Suzuki) and Biochemistry (Teresa Davoli); the programme "deliberately does not specify required majors or prerequisites". <https://www.nyu.edu/about/news-publications/news/2026/september/nyu-langone-work-study-undergrad-research-program.html>
- NYU Psychology tells its RAs they will "build skills in scientific programming, data analysis, and science communication" and names "computational modeling" among lab skills. <https://as.nyu.edu/departments/psychology/undergraduate/research-opportunities.html>
- The CDS Student Research Initiative runs faculty project fairs pitching to "Master's and Undergraduate data science students"; recent fairs featured Anthropology, Nursing, Population Health, Mathematics and Urban Intelligence — non-CS departments looking for data help. No CDS funding; contact Tim Baker, tb116@nyu.edu. <https://cds.nyu.edu/undergraduate-research-initiative-uri/>
- The posting's own list of skills faculty have asked for: "fluency in specific languages to familiarity with computer programming to experience with data to dexterity with film editing."

**What this implies for the letter:** the Director matches on stated interests and skills, and the requesting faculty are mostly outside CS (English to Medicine, Population Health, Psychology), so the letter has to state the school, the programme, the interests and the skills as plain nouns a non-engineer can search on — and name the interests widely enough that a psychology or public-health lab that needs a Python pipeline recognises him.

## 3. What leads on the resume, and why

Preset `nyu-general-ra-2026` in `profile/variants.yaml`. Decided; not changed here.

- **Experience: Delhi, AI Society, MyYogaTeacher, WatchDNA.** Delhi leads because it is the only entry that says "has done research" — Gaussian Process classifiers under Prof. R. P. Singh. Thin, self-reported, still the strongest card for this pool. AI Society second: the posting's third duty is "sharing the research findings ... presentations", and writing teaching materials and running workshops is the nearest evidence on the profile. MyYogaTeacher and WatchDNA carry the data and pipeline work (time-series deduplication, voice-to-SQL, endpoint discovery). Flickmatch is dropped — oldest, frontend only, and the standing first cut for one page.
- **Projects: all four stay** — Lead Engine, Torii, Pash, Portfolio. The posting asks applicants to list the varied skills a lab could use, and the breadth lives in the projects: a scoring pipeline with a dashboard, agent accountability, GPU audio, 3D in the browser.
- **Skills: every `ask: true` skill excluded** — Go, Java, C++, Rust, LangGraph, RAG, Vector search, Embeddings, PyTorch, scikit-learn, GitHub Actions, Linux, Pytest, Jest. A PI who reads "PyTorch" opens the interview there.
- **Skill lead:** Python, SQL, TypeScript, Gaussian Processes first. The pool's own example is "computer programming ... experience with data".

Agree with the selection. No disagreement.

Two remarks, not objections: `prefer_flavors` starts `research, general`, so Lead Engine renders `le.pipeline.sources` with the five named sources, as instructed on 2026-09-05. And nothing on this page is unconfirmed — same property as `waymo-vv-masters`.

## 4. Requirement mapping

The posting is deliberately open, so this maps what the letter must DECLARE and what the profile can back.

| Posting asks | Status | Where |
|---|---|---|
| School (CAS / Courant / Tandon ...) | **printed as Tandon** (inferred from registration, 2026-09-07; flagged to him) | `education.nyu.school_inferred` |
| Course of study | existing — M.S. Computer Science, expected 2028 | `education.nyu` |
| Currently enrolled graduate student | existing | `education.nyu` |
| Subject areas of interest | **chosen by him, 2026-09-07**, from eight options: how intelligence should progress hand in hand with people; the cases where AI is closer to a con than a tool; control over data. Grounded in Torii and Lead Engine. | `torii`, `lead_engine`, letter |
| Computer programming | existing — Python, SQL, TypeScript, JavaScript | skills |
| Experience with data | existing — Delhi (high-dimensional data), Lead Engine (deduplication, scoring), MyYogaTeacher (time-series deduplication, voice-to-SQL) | `delhi`, `le.pipeline`, `myt.*` |
| Research experience, "desire to learn more about research" | existing but thin — Delhi, one line, self_reported; dataset, method, result all gaps | `delhi` |
| Presentations, sharing findings | supported — AI Society "educational resources and presentations" (LinkedIn wording), workshops | `ais.workshops` |
| Writing articles | **GAP** — technical write-ups on asmit.space exist (raw-facts) but nothing academic. Not claimed. | — |
| Social media posts | **GAP** — two LinkedIn posts exist. Not claimed. | — |
| Literature review | **GAP** — nothing evidenced | — |
| Survey design or administration | **GAP** | — |
| Interviews, focus groups | **GAP** | — |
| Lab-based experiments | **GAP** — Delhi was computational; whether it counts as lab work is unknown | — |
| Participant recruitment | **GAP** | — |
| Fluency in specific languages | **GAP / intake** — languages spoken never recorded (Hindi? Bengali?) | raw-facts gap list |
| Film editing (the posting's own example) | **ASK, do not claim** — LinkedIn tags Adobe Premiere Pro on Flickmatch and lists Video Production and Video Editing under Services; none of it is in profile.yaml | raw-facts, Services |

## 5. Letter notes

Rewritten 2026-09-07 under `letters/GUIDELINES.md`; addressed to Ethan
Youngerman by name.

- **Structure:** the constant personal paragraph (byte-identical to
  `draft-campus-ca.py`, verified on this build), the italic portfolio
  signpost (his stated preference from the CFA letter the same day), two
  technical paragraphs, a plain close.
- **Paragraph 1 declares** school (Tandon, see above), programme, this
  semester's classes (algorithms, artificial intelligence - CS-GY 6033 and
  6613), the Delhi research, the skills as a searchable list, and the AI
  Society teaching as the nearest thing to explaining research to
  outsiders.
- **Paragraph 2 is the interest he chose**, in his own framing: "how
  intelligence should progress and move hand in hand with humanity",
  "problems with how AI might be a con in some cases", "control over data".
  Grounded in Torii (his recorded framing from `letters/OPENING-OPTIONS.md`;
  the protected strings verbatim) and Lead Engine (an AI voice calling
  homeowners; public listings and county records at scale). Fields named,
  no philosopher named. Ends by naming three sides he would take work on:
  philosophy of mind, the ethics of AI, data governance.
- **Routing targets for the Director**, researched 2026-09-07 so he can
  speak to them in an interview, none named in the letter: NYU Center for
  Mind, Brain and Consciousness (directors Ned Block and David Chalmers;
  2025 events on AI welfare and moral status, an August 2026 computational
  consciousness event) - **verified**, https://wp.nyu.edu/consciousness/;
  Center for Responsible AI (mission "responsible AI is synonymous with
  AI"; themes include data-centric AI, explainability, fairness, privacy and
  safety, policy) - **verified**, https://airesponsibly.net/; Philosophy;
  Center for Bioethics (not fetched).
- **Close:** classes and free days (`basics.availability_fall_2026`), more
  over the breaks, the F-1 line. No hour count on purpose.
- **Measured:** 566 words with the recipient block, 1 page,
  3 link annotations, lint 0 block / 0 warn / 0 note after splitting
  two long sentences. Over the campus target because the constant paragraph
  is 175 words and this posting demands four declarations; one page is the
  rule that binds.
- **Not claimed:** literature reviews, surveys, interviews, lab work,
  participant recruitment, academic writing, film editing, any spoken
  language, any philosophy coursework.

## 6. Questions for Asmit

1. ~~**Courant or Tandon?**~~ Printed as Tandon from his registration; **confirm the word**, and the exact programme name as the transcript states it. (Intake 3.)
2. **Languages you speak, and how well.** Hindi? Bengali? Anything else? The posting names "fluency in specific languages" as a skill faculty ask for.
3. **Video editing.** LinkedIn lists Adobe Premiere Pro and Video Editing. Have you done enough of it to be handed a lab's footage? If yes: what did you edit, and with what?
4. ~~**Which research areas do you actually want?**~~ **Answered 2026-09-07:** philosophy and ethics of AI - progress alongside people, AI as a con in some cases, control over data. Still open: anything outside that he would take (education, cities, health), since the Director passes names to non-CS faculty.
5. **Hours per week.** Days answered 2026-09-07. The count stays with the supervisor once matched; his on-campus total is his call (intake 13).
6. ~~**Work authorization**~~ **Answered: F-1** (2026-09-07). Not Work-Study eligible, which is the pre-screen disadvantage in section 1.
7. **Delhi.** What dataset, what method, and what came of it — a writeup, code, a result? (Intake 8.) One crisp bullet with tools and an outcome would carry this whole application.

## 7. Built

**Rebuilt 2026-09-07** with the interest paragraph he chose, school printed as
Tandon, Torii first among projects, the new MyYogaTeacher design bullet
rendering, and every placeholder resolved. Resume ATS PASS, one page, 95%
fill, six links. Letter 566 words, 1 page, 3 links, 0/0/0 lint.
Draft build. Send checklist in `letters/GUIDELINES.md` section 5; the one
thing to confirm first is the word "Tandon".

Earlier record - built 2026-09-06. `applications/nyu-general-research-assistant-fall-2026/`
- preset `nyu-general-ra-2026`, letter
`letters/draft-nyu-general-research-assistant-fall-2026.py`. Rebuilt 2026-09-07 after the workshops phrasing changed. Resume ATS PASS,
one page, 94% fill at the tightest rung used in the batch, six link
annotations. Dropped to fit: LangChain, Pinecone, Tool use, LLM
streaming, YOLOv8, Uvicorn, Selenium, iOS App Store. Letter one page at
scale 1.03, 499 words, zero lint findings, three link annotations - long for
the campus genre, but this is the one posting where the letter is the
application and has to state school, programme, interests and skills. No
`ask: true` skill renders. Draft build. Still in the letter: `[SCHOOL]`, the
subject-areas-and-languages sentence, `[N]`, `[DAYS]`, the
work-authorization line.

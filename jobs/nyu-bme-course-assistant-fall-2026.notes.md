# NYU Tandon BME — Course Assistant, BI-GY 810X Bioinformatics Capstone (Dr. Brathwaite)

## 1. Knockout check

| Gate | Status |
|---|---|
| Graduate students only | **PASS** — NYU M.S. CS |
| Work authorization — "US work authorization required. Open to candidates with OPT/CPT." | **UNKNOWN — the open gate.** Tier 1 in `checklists/intake.md`. F-1 students can hold on-campus jobs without CPT, capped at 20 hrs/week total during term across every on-campus job combined. The "open to OPT/CPT" line says the department is used to international students; it does not answer the question. Never answer it for him. |
| Hours | **NOT STATED.** "Schedule determined by Instructor of Record ... due to the nature of the course." Ask him what he will offer; it also decides how many of the six NYU postings he can hold at once under the 20-hour cap. |
| Onsite, NYC, on campus | **PASS** — he is in New York |
| September 14 – December 22, 2026 | **PASS.** Note the start date is a week after saving and the deadline (Oct 1) is after the start — hiring is presumably rolling, so earlier is better. |
| Deadline | **October 1, 2026, 11:59 PM** |
| Confidential information (grades) | Nothing to claim. Noted only. |
| Weekly evaluations with the instructor | Nothing to claim. Noted only. |

## 2. Background

- **Dr. Brathwaite is Mgavi Brathwaite** — "Bioinformatics Program Manager and
  Academic Advisor, Graduate Center of Professional Studies; Adjunct Professor",
  in the Biomedical Engineering department, running Tandon Online's M.S. in
  Bioinformatics since 2009. His stated expertise: "Next Generation Sequence
  Analysis and Deep Learning with a focus on personalized medical solutions in
  Cancer diagnosis and treatment." Before NYU: IBM Center for Computational
  Biology, DNASTAR, Columbia University Genome Center, NIH; visiting professor
  at Zhejiang Institute of Technology 2012–2016.
  https://engineering.nyu.edu/staff/mgavi-brathwaite
- He organised the NYU Tandon Bioinformatics Symposium of student research
  projects (ovarian cancer to childhood esophageal disorders).
  https://engineering.nyu.edu/news/nyu-tandon-bioinformatics-symposium-showcases-next-generation-data-driven-biomedicine
- **BI-GY 810X is the Bioinformatics Capstone (3–9 credits).** Bulletin text:
  "This online course is providing students an opportunity to work in a public
  or private research or production environment ... Students apply their skills
  (such as Python, R, UNIX, and Next Generation Sequence Analysis) in a
  real-life environment. Students who enroll in this course will work under the
  advisement of a Tandon Online faculty member. At the end of the course the
  student has to submit a final report/paper." Prerequisites: BI-GY 7663
  Problem Solving for Bioinformatics, BI-GY 7673 Applied Biostatistics for
  Bioinformatics, BI-GY 7653 Next Generation Sequence Analysis for
  Bioinformatics. https://bulletins.nyu.edu/courses/bi_gy/
- **Why a BI-GY course is posted under BME:** the Bioinformatics M.S. is housed
  in the Biomedical Engineering department. The program page says capstone
  projects need "a significant programming component (Python, R, and/Shell
  scripting)" and that students use Jupyter notebook throughout.
  https://engineering.nyu.edu/academics/programs/bioinformatics-ms-online
- **An oddity to ask about, not to assume:** the capstone is described as an
  online course with students placed in outside labs, yet the CA posting is
  onsite and lists autograded assignments on JupyterHub. The toolchain reads
  like support for notebook-based coursework across the program rather than
  the capstone alone. If there is an interview, the question is what the CA
  actually grades.
- **The three graders, one line each.** *nbgrader* — "a tool that facilitates
  creating and grading assignments in the Jupyter notebook"
  (https://nbgrader.readthedocs.io/en/stable/). *Otter-Grader* — "A Python and
  R autograding solution" from UC Berkeley's data-science infrastructure group;
  builds an assignment and its autograder from a single notebook and runs
  locally, in Docker, or on Gradescope
  (https://github.com/ucbds-infra/otter-grader). *Gradescope* — a hosted
  grading platform whose autograder runs instructor-supplied code in a Docker
  container on Gradescope's infrastructure
  (https://gradescope-autograders.readthedocs.io/en/latest/). He has used none
  of the three on the instructor side. As an ASU undergraduate he may have
  *submitted* to Gradescope, which is the student side and not the same thing.
- **What it implies for the letter:** a bioinformatics professor with a
  deep-learning-in-cancer background, hiring a grader for a Python/R/UNIX/NGS
  program. The honest pitch is teaching, Python and GenAI; R, UNIX and the
  grader toolchain stay silent as gaps, and genomics is "not required".

## 3. What leads on the resume, and why

Preset `nyu-bme-ca-2026` is decided and this file does not change it.

- **AI Society leads.** Grading, answering student questions and writing
  solution examples is teaching, and this is the only teaching entry on the
  profile. For a course-assistant posting it is the qualification.
- **Delhi second.** Python research on Gaussian Process classifiers is the
  nearest thing on the profile to the data-science half of a bioinformatics
  course, and it is the one entry that says "has done research".
- **MyYogaTeacher third** for the GenAI the posting asks for — voice-to-SQL on
  Whisper with streaming LLM responses. **WatchDNA fourth** for the Python
  endpoint-discovery pipeline. **Flickmatch is off** — a website revamp says
  nothing to this reader.
- **Projects: Lead Engine, Torii, Pash.** Lead Engine is Python plus LLM
  scoring with the reasoning written out — "experience with GenAI" in one
  bullet. Torii is LLM agents and MCP. Pash runs Demucs v4, a deep-learning
  model, in production — the honest extent of the deep-learning claim.
  **Portfolio is off.**
- **Every `ask: true` skill is off**, including Linux and PyTorch. The posting
  names UNIX and deep learning; neither is evidenced, and a fifteen-minute
  on-campus interview has no room to recover from a keyword he cannot defend.
- **Skills lead:** Python, SQL, then the AI & Agents vocabulary, then data.

**Disagreement:** none. The selection is right for this reader.

**One note, not a disagreement:** "Claude API", "LangChain" and "Pinecone" are
`resume_2026` self-claims with no project behind them, and "Claude API" sits
fourth on the AI & Agents lead line. Confirm he can talk about it, or expect a
question on it.

## 4. Requirement mapping

| Posting line | Status | Evidence, or what to ask |
|---|---|---|
| Fluent in Python | **existing** | Four entries: Lead Engine, WatchDNA locator pipeline, MyYogaTeacher, Delhi. Named explicitly in the letter. |
| R | **GAP — never.** | Not in the profile, not on LinkedIn, not on the old resume. Not claimed anywhere. |
| numpy, pandas, seaborn, scipy | **unrecorded** | The posting lists them under R; they are Python libraries. None is in the profile. The Delhi Gaussian Process work very likely used numpy and scipy, scikit-learn or GPy — this is the CLAUDE.md Delhi tools question, and it is the one answer that could honestly add two of the four. **ASK.** |
| UNIX | **unrecorded** | Linux is `ask: true` and off. Pash's remote CUDA worker and three internships make a shell near-certain, but "entailed vs plausible": reaching a remote GPU entails a terminal, it does not entail fluency. **ASK.** |
| Grade assignments | **supported, weakly** | AI Society mentoring and workshops are teaching, not grading. Nothing on the profile says he has graded anything. **ASK** whether he has been a grader or TA anywhere. |
| Respond to student questions; provide solution examples | **supported** | `ais.mentoring` (four freshmen through a first ML project) and `ais.workshops` (wrote the materials). Writing solution examples is the nearest thing to writing teaching materials. |
| Autograding with nbgrader, Otter, Gradescope on JupyterHub | **GAP as an administrator** | None of the three on the instructor side. He may have submitted to Gradescope as an ASU student — student side only. **ASK.** |
| JupyterHub / Jupyter | **unrecorded** | Not in the profile. Plausible for Delhi and the AI Society workshops; plausible is not evidence. **ASK.** |
| Knowledge of genomics (helpful, not required) | **GAP** | None. Not required; not claimed. |
| Experience with GenAI | **existing** | `myt.voicesql` (Whisper + streaming LLM), `le.pipeline` (LLM scoring with written reasoning; OpenAI API, prompt engineering), `torii.core` (MCP proxy between agents and tools). All three are in the letter. |
| LLMs (a plus) | **existing** | Same three. |
| Deep learning (a plus) | **supported only** | Pash runs Demucs v4, a deep-learning source-separation model, in production — he operates one; nothing says he trained one. The AI Society freshmen's emotion-detection project (facial expressions + audio) may have used deep learning — **ASK.** PyTorch is `ask: true` and off. Not claimed as a skill in the letter. |
| Confidential information | n/a | Noted; nothing to claim. |

## 5. Letter

`letters/draft-nyu-bme-course-assistant-fall-2026.py`

- **Genre: campus CA.** `draft-campus-ca.py` applies directly. Course named in
  the recipient block — "Course Assistant - BI-GY 810X, Bioinformatics
  Capstone, Biomedical Engineering" / "Dr. Brathwaite, NYU Tandon School of
  Engineering". No signpost. Personal paragraph copied verbatim — verified
  byte-identical to the template by script.
- **Technical paragraph, one paragraph, 139 words:** AI Society workshops and
  the four freshmen, Delhi, MyYogaTeacher voice-to-SQL, Lead Engine as a Python
  pipeline with LLM scoring and written reasoning, Torii as an MCP proxy,
  first-year M.S. CS at NYU. Python and GenAI are both explicit. Nothing on R,
  UNIX, the grader toolchain, JupyterHub, genomics, PyTorch, deep learning as a
  skill, or grading experience.
- **One deviation from the template.** `draft-campus-ca.py` says "I spent a
  year as Technical Officer"; `profile.yaml` dates the role Aug 2025 – Jan
  2026, six months. The profile wins, so the letter names the role with no
  duration. See question 10.
- **Word count:** personal 172, technical 139, close 38 — **349 body words**,
  365 with the recipient lines. The CLAUDE.md campus target is 150–250, and the
  constant 172-word personal paragraph makes that unreachable on its own;
  CLAUDE.md records the conflict as unresolved and **his call**. If he wants it
  under 250, the technical paragraph can drop to the AI Society sentences plus
  one GenAI sentence (about 70 words) and still name Python and GenAI.
- **Lint:** `python -m engine.ai_lint nyu-bme.txt --max block` — **0 block,
  0 warn, 0 note.**
- **Placeholders that gate sending:** `[N]` hours, `[DAYS]`, and the work
  authorization line. All three are open in `checklists/intake.md`.
- One-page check is the parent's, at build time.

## 6. Questions for Asmit

The two that could honestly move this application are 3 and 4.

1. **Work authorization** (Tier 1). The posting requires US work authorization
   and is open to OPT/CPT. Citizen, PR, or F-1?
2. **Hours and days.** The posting leaves the schedule to the instructor. How
   many hours a week will you offer, and which days? The on-campus cap is 20
   hours total across every job during term.
3. **Delhi tools.** What did the Gaussian Process classifier work actually use
   — numpy, scipy, scikit-learn, GPy, pandas? Any plotting? A yes on numpy or
   scipy is a verified skill and goes in the letter and on the skills line.
4. **UNIX / shell.** How did you reach the remote CUDA worker for Pash — ssh, a
   shell, scripts? Did you work in a terminal daily at WatchDNA or
   MyYogaTeacher? Could you take a "write me a one-liner" question cold?
5. **Grading.** Have you ever graded or TA'd anything — at ASU, in the AI
   Society, anywhere, even informally?
6. **Gradescope.** Did you submit to Gradescope as an ASU student? Have you
   ever seen the instructor side of it, or of nbgrader or Otter?
7. **Jupyter / JupyterHub.** Have you used Jupyter notebooks — for Delhi, for
   the AI Society workshops? JupyterHub specifically?
8. **Deep learning.** The freshmen's emotion-detection project — what did it
   use (a pretrained model, a CNN, which framework), and did you write any of
   it? And for Pash: did you only run Demucs v4, or touch the model?
9. **R.** Ever, at all? The expected answer is no; confirming it records the
   gap as a fact rather than an absence.
10. **AI Society duration.** The profile says Aug 2025 – Jan 2026; the letter
    template says "a year". Which is it — was the officer term shorter than
    your involvement?
11. **Genomics or biology coursework.** Any? Not required; only matters if yes.
12. **Claude API.** It is a claim from your old resume with no project behind
    it, and it will sit near the front of the AI & Agents line. Can you talk
    about it for two minutes?

## 7. Built

Built 2026-09-06. `applications/nyu-bme-course-assistant-fall-2026/` -
preset `nyu-bme-ca-2026`, letter
`letters/draft-nyu-bme-course-assistant-fall-2026.py`. Rebuilt 2026-09-07 with Gaussian Processes moved to third on the AI &
Agents line. Resume ATS PASS, one page, 91% fill, six link annotations.
Trimmed to fit: Whisper, Demucs, x402, LangChain, Pinecone, YOLOv8,
SQLAlchemy, Selenium. Whisper and Demucs leaving the skills line costs
nothing a reader can see - both are named inside the MyYogaTeacher and Pash
bullets. Letter one page, 365 words,
zero lint findings, three link annotations. No `ask: true` skill renders.
Draft build. Still in the letter: `[N]`, `[DAYS]`, the work-authorization
line.

# ICF — 2027 Summer Intern, Software Developer

Posting: `jobs/icf-swe-intern-summer-2027.md`, saved 2026-09-07. Preset:
`icf-swe-intern-2027`. Letter: `letters/draft-icf-swe-intern-2027.py`.
Package: `applications/icf-swe-intern-summer-2027/`. 10 weeks, June to August
2027, full time. **Location and deadline not stated in the paste - check the
posting page.** No housing or relocation assistance.

## 1. Knockouts

| Gate | Status |
|---|---|
| **"Due to federal contract requirements, individuals must be authorized to work in the United States."** | **His to answer.** CPT through NYU is work authorization for a degree-related summer internship, and the posting does not say "no sponsorship" or exclude F-1 by name (contrast MiniMed). But a federal contractor's phrasing often precedes a no-future-sponsorship policy and some client projects need US-person status. Answer the form honestly; never let the system answer it. |
| 15 completed college-level credit hours by start | **PASS** - a B.S. and a semester of the M.S. |
| Full time, 10 weeks, June to August | **PASS** - NYU's spring term ends mid-May. |
| Location | **UNKNOWN.** Not in the paste. ICF is headquartered in Reston, VA, with offices nationwide; no relocation help. If it is not New York or remote, the summer's housing is his cost. Check before applying. |
| Degree field | **PASS** - M.S. Computer Science. |

## 2. Background (researched 2026-09-07)

- **ServiceNow Validated Practice Awards**, January 20, 2026 - **verified**,
  https://www.icf.com/news/2026/01/servicenow-recognizes-icf-with-key-partner-designations.
  ICF's federal technology practice received four awards (ITSM, HRSD, SPM,
  CSM); it has twice been ServiceNow U.S. Partner of the Year; the release
  names "Agentic AI solutions" and helping agencies "operationalize AI".
  Quoted: "From strategy to execution, ICF supports public sector clients in
  reducing time-to-value, accelerating mission outcomes and transforming
  service delivery through AI." Named: David Birken, SVP for digital
  modernization and experience.
- **ICF Fathom**, launched August 5, 2025. **Verified on the page**
  (https://www.icf.com/work/enterprise-ai/fathom-ai): "a suite of tailored AI
  solutions and services"; agents that "plan and automate complex tasks, make
  informed decisions, and seamlessly and securely integrate into your existing
  infrastructure"; "Flexible, open architecture ... No vendor lock-ins"; use
  cases include a federal needs assessment (labor cut by more than half), a
  "digital librarian", and public-comment analysis. The page does not mention
  parallel agents or decision logs - those come from **search snippets** of
  the launch release: a suite of AI solutions for federal
  agencies; a multi-agent design where "agents tackle tasks in parallel" and
  "if one agent falters, others catch errors - with logs tracking every
  decision"; "can be embedded into existing infrastructures" or run hosted
  or hybrid; use cases from software development to document processing,
  grants management and regulatory analysis
  (https://www.icf.com/work/enterprise-ai/fathom-ai;
  https://icf.mediaroom.com/2025-08-05-ICF-Launches-ICF-Fathom,-a-New-Suite-of-AI-Solutions-for-Federal-Agencies).
  **This is the letter's one anchor**, and the letter uses only the verified
  part: agents built to sit inside an agency's existing systems.
- **Platforms:** ServiceNow, Salesforce, Appian, Microsoft partnerships
  (https://www.icf.com/company/about/partners/partnership-ecosystem,
  search snippet). The posting's low-code list is ICF's partner list.
- Not found: the intern location, the deadline, who reads the letter.

## 3. What leads on the resume, and why

Preset `icf-swe-intern-2027`.

- **Experience: MyYogaTeacher, WatchDNA, AI Society, Delhi.** MyYogaTeacher
  first because its opening bullet is the posting's first responsibility -
  an idea into diagrams, wireframes and user journeys, then built - and its
  voice-to-SQL bullet is a workflow automated. WatchDNA second: backend,
  admin console, the automated endpoint-discovery pipeline. Flickmatch off.
- **Projects: Lead Engine, Torii, Pash, Portfolio.** Lead Engine first for
  process automation and agents; Torii second for agentic workflows, APIs,
  and a JSON policy engine (configuration over code - the nearest thing to
  low-code on the profile). Pash for the queue pipeline; Portfolio last.
- **Skills:** their languages in their order (Java, Python, JavaScript, SQL,
  HTML/CSS); the AI & Agents line second; then REST and the API vocabulary;
  then AWS, Automation, Git, GitHub, Jira, Agile, DevOps, Software testing.
- **Coursework-only keywords on this page: Java, Jira, Agile, DevOps,
  Software testing.** GitHub is on real evidence (the portfolio repo at
  github.com/sm11t). Every `ask: true` skill is excluded.
- **Not added:** Salesforce, ServiceNow, Appian, Microsoft Power Platform,
  Confluence. A class does not cover them and nothing records them.

## 4. Requirement mapping

| Their line | Status | Him |
|---|---|---|
| Java, Python, JavaScript, SQL, HTML/CSS | existing (Java coursework) | inside bullets at WatchDNA, Lead Engine, MyYogaTeacher |
| Requirements into technical solutions | existing | MyYogaTeacher feature design (`myt.design`) |
| Workflows, automations, business rules, integrations | existing | voice-to-SQL replacing a manual workflow; the endpoint-discovery pipeline; Torii's policy engine; Lead Engine's scouts |
| **Low-code platforms** (Salesforce, ServiceNow, Appian, Power Platform) | **GAP, named in the letter** | Torii's JSON policy file as the analogue; "I have not used Salesforce, ServiceNow or Appian." |
| APIs, integrations, cloud | existing | WatchDNA REST + JWT; Pash S3/SQS; AWS |
| AI-assisted development, agentic workflows | existing | Torii, Lead Engine, his stated practice (2026-09-07) |
| Testing, QA, defect resolution | supported | alerts hooked up so failures are seen and fixed (`wd.alerts`); Software testing on coursework |
| Technical documentation, knowledge sharing | existing | AI Society materials and workshops |
| Agile, Git, GitHub, Jira, Confluence | Git and GitHub real; Agile and Jira coursework; Confluence not claimed | skills line |
| Security, accessibility, performance | security existing (JWT, RBAC, middleware); **accessibility GAP** | not claimed |
| "Curiosity, initiative, adaptability" | not echoed | the always-building hinge and the projects |

## 5. Letter

Internship genre: the internship personal paragraph (byte-identical to
`draft-google-swe-intern.py`), the portfolio signpost, two technical
paragraphs, a one-line close.

- **Paragraph 1**, in the posting's order of concerns: MyYogaTeacher's
  feature design and the time the voice-to-SQL pipeline gave back; WatchDNA's
  backend, admin console and automated pipeline, and the impact (third-party
  app replaced, traffic up within six months). Standing content, GUIDELINES.md
  section 6.
- **Paragraph 2:** the always-building hinge; Lead Engine and Torii; the
  AI-practice sentence (harness over prompt); the named gap (no Salesforce,
  ServiceNow or Appian) with Torii's policy file as the analogue and the
  expectation of picking the platforms up as he has everything else; the
  anchor (Fathom agents inside existing systems) and the why-sentence,
  his to approve.
- **Close:** New York, full time from June 2027.
- **Not claimed:** any low-code platform, Confluence, accessibility, client or
  government work, the Fathom details beyond "inside existing systems".
- **Measured:** 569 words, one page, three link annotations, 0/0/0 lint.

## 6. Questions for Asmit

1. **Where is the internship?** Not in the paste. No relocation help.
2. **The authorization line.** Answer the form yourself; if it asks about
   future sponsorship, answer that honestly too. Nothing here decides it.
3. **Jira and Agile: which class?** Both are on the page on your word.
4. **The Fathom sentence** at the end of the letter says what you would most
   like to learn. Approve or replace.
5. **Any low-code platform at all** - Power Apps, Airtable, Zapier, Retool -
   from any class or job? If yes, it goes on with evidence.

## 7. Built

Built 2026-09-07. Resume: ATS PASS, one page, 95% fill, six link annotations;
Languages line opens Java, Python, JavaScript, SQL, HTML/CSS; Data & Cloud
carries Automation, Git, GitHub, Jira, Agile, DevOps, Software testing.
Letter: one page, 569 words, three link annotations, 0/0/0 lint after
splitting two long sentences. Draft build. Standing note: no phone number in the profile (intake #2).

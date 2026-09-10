# Intake — what only you can answer

Everything else has been researched or measured. These cannot be, and each one
blocks something concrete. Answer in any format; I'll fold them into
`profile/profile.yaml` and flip the affected variants to `approved: true`.

Mark each `[x]` with the date when answered.

---

## Tier 1 — blocks every application

- [x] **1. Work authorization.** Are you a US citizen / permanent resident, or on
      an F-1 visa?

  **Answered 2026-09-07: F-1.** Typed into the Fall 2026 Campus Desk (`auth`
  field) and recorded in `profile.yaml` as `basics.work_authorization` under
  source `user_2026-09-07`. What follows from it: on-campus jobs are open
  without CPT or OPT, capped at 20 hours a week combined during term; Federal
  Work-Study postings are closed. **Still open: whether you have an SSN yet**
  (the `ssn` field on the desk is blank). Sponsorship screening questions on
  internship portals remain yours to answer.

  This is the single highest-leverage answer. It determines whether you can take
  Federal Work-Study jobs (F-1 students cannot — a large share of NYU on-campus
  postings are work-study only, and applying to those is wasted effort), whether
  the 20-hours-per-week on-campus cap applies during term, whether you need a
  Social Security Number application through an on-campus job offer, and how
  every "will you now or in the future require sponsorship" screening question
  gets answered. The system will not answer a screening question on your behalf
  under any circumstances — but it can't even filter postings for you until it
  knows.

- [ ] **2. Phone number.** Every application portal has a required field for it,
      and it's currently absent from your resume entirely.

- [ ] **3. NYU program specifics.** Courant or Tandon? The exact program name as
      your transcript states it, your start date, and your fall course list.

  **Partly answered 2026-09-07.** Your Albert schedule shows CS-GY 6033
  (Algorithms I, Tue 5:00-7:30 PM) and CS-GY 6613 (AI I, Fri 11:00 AM-1:30 PM)
  in Jacobs Hall, 6 MetroTech, plus a Wednesday 6:00-8:30 PM class. CS-GY and
  6 MetroTech are Tandon, so the school is recorded as **inferred Tandon** in
  `profile.yaml` (`education.nyu.school_inferred`). It does not print until
  you say the word. Still open: the Wednesday course name, the program name as
  the transcript states it, the start date.

  Never guessed, because it changes which departmental mailing lists carry
  grader postings, which courses you're eligible to assist, and how the education
  line reads. The fall course list matters because grader postings gate on having
  taken the course.

## Tier 2 — blocks specific bullets

- [ ] **4. ASU GPA**, plus any honors, dean's list, or scholarships. It prints
      only if it's 3.5 or above; below that it's omitted, which is standard and
      not a red flag.

- [ ] **5. GitHub.** Do you have an account? If not, is it fine for me to plan
      around you creating one this week?

  You have seven projects and no repository link anywhere — not on the resume,
  not on LinkedIn, not on asmit.space. For engineering roles that reads as
  "these might not be real." This is the single biggest gap in your profile and
  it's roughly a four-hour fix: account under your real name, push Torii, Pash,
  and one more, each with a README saying what it is and why, plus run
  instructions. Torii's README should carry "built the full stack in a day" and
  "two production dependencies" verbatim — those are the details people remember.

- [ ] **6. The four contested numbers.** One sentence each on how it was measured.
      Until answered, these are blocked and the mechanism-only phrasings ship
      instead — which are, in two cases, better bullets anyway.

  - **"~50% AI-call conversion"** (Lead Engine). Your own site says "50% Success
    Rate", which is a different claim — a call that connects is not a conversion.
    What is the denominator: calls placed, calls answered, or leads that agreed
    to a callback? This is the one I'd most want fixed. Fifty percent conversion
    on cold real-estate calls is high enough that a sharp interviewer will push,
    and if it collapses they stop believing the other numbers on the page.
  - **"70% cut in manual prospecting"** — against what baseline? Was anyone doing
    this by hand before, and for how long?
  - **"99.9% uptime"** (MyYogaTeacher) — uptime of what, measured how, over what
    window? Uptime is usually a server property, and this was a mobile client.
  - **"60%" reduction in admin edit work** — measured how, over what period?

- [ ] **7. CovreliefDwarka.** What actually happened, when, and for whom?

  LinkedIn says May–Sep 2020 and "vaccinated over 100 economically disadvantaged
  workers." No COVID vaccine existed anywhere until December 2020, so as written
  the claim is temporally impossible and an interviewer who notices would be
  right to. Were the dates different, was it a different vaccine, or was it
  registration and logistics help rather than vaccination itself? I've blocked
  the entry until this is resolved — founding something at seventeen that reached
  a hundred people is the most humanizing thing on your entire profile, which is
  exactly why it has to be exactly right.

- [ ] **8. Delhi research.** What dataset, what method, and was there any result,
      writeup, or artifact?

  Right now this is one line about optimizing Gaussian Process classifiers. It's
  missing from your resume entirely, and it's your strongest credential for a
  research assistantship or a grader role — it's the only thing on your profile
  that says "has done research" rather than "has shipped apps." With a dataset
  and a result it becomes a real entry. It also gives you the technical hook a
  cold email to a professor needs.

## Tier 3 — polish

- [ ] **9. Portfolio date.** Your resume says 2024, LinkedIn says Feb 2025. Which
      is true? It needs to be one answer everywhere.

- [ ] **10. Truncated descriptions.** NeuroPilot, SentinalAI, and Lynti were cut
      off mid-sentence in the LinkedIn export, so they're stubbed and unusable.
      Also: is "SentinalAI" the intended spelling, or should it be "Sentinel"? A
      misspelled project name on a resume is worse than no project.

- [ ] **11. Go, Java, C++, Rust.** Could you sit an interview in any of these
      today? They're on your current resume with no supporting project, so
      they're currently excluded. An interviewer who opens with Rust ownership
      semantics because it was on the page is a self-inflicted wound. Keep only
      the ones you'd genuinely welcome a question about.

- [ ] **12. WatchDNA companion app.** Did it actually launch on the App Store, or
      did it go through review? "Took it through iOS App Store review" ships
      safely today; "launched" does not until you confirm.

- [ ] **13. Availability and references.** How many hours per week do you want
      on-campus (the cap is 20 during term)? And may I list these four as
      reference targets: your WatchDNA supervisor, your MyYogaTeacher manager,
      Prof. R. P. Singh, and the AI Society advisor?

  **Days answered 2026-09-07:** "I can figure out a flexible schedule around
  my classes" - classes Tue and Wed evenings, Fri late morning; Mon and Thu
  free. Recorded as `basics.availability_fall_2026`. Still open: total hours
  you want across all on-campus jobs, and the references.

---

## Not questions — things to fix yourself

- [ ] **LinkedIn is stale**, and recruiters cross-check it in the first screen.
      Location still says Tempe; the "Open to work — Tempe, AZ" banner still
      shows; the headline still says "CS @ ASU'26"; NYU isn't listed as an
      education entry; and six finished projects still say "Present". About
      45 minutes.
- [ ] **asmit.space/lead-engine publishes "Live System URL: localhost:5173/".**
      Anyone who clicks it gets nothing. Remove it or point it somewhere real.
- [ ] **asmit.space/pash has no body content** — just the title.
- [ ] **The portfolio hides everything behind a click-through into a 3D scene.**
      It's genuinely impressive, but a crawler can't read it and a recruiter with
      twenty seconds may not get past the splash. A plain `/resume` or `/about`
      route with the same content as text would fix both without touching the 3D.

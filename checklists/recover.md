# Recovery — what the profile is probably missing

Your profile was assembled from a LinkedIn export and an old resume. Both
understate. Flickmatch went from *"turned Figma designs into components"* to
*"revamped the entire website"* on one sentence from you — that entry had been
undersold for years, on your own page.

These are the questions most likely to unlock the same thing elsewhere. Answer
in one line each; anything you confirm becomes a `verified` fact, which is
stronger provenance than anything inherited from LinkedIn.

**Answer nothing you would not want to be asked about in an interview.**

---

## WatchDNA — 9 months, the biggest entry and the thinnest per month

- [ ] Were you the only engineer, or was there a team? How many?
- [ ] Did anyone review your code, or did you review anyone's?
- [ ] How did it deploy — a pipeline, or by hand? What ran the builds?
- [ ] Any tests? Any CI?
- [ ] **Did the companion app actually launch on the App Store, or did it clear
      review?** This is still blocking a bullet.
- [ ] How many stores ended up in the locator? How many retailer endpoints did
      the discovery pipeline handle?
- [ ] Any users, downloads, or a launch date?
- [ ] Did you design the schema, or inherit it?
- [ ] Anything you owned end to end that is not currently listed?

## MyYogaTeacher — 9 months, currently two bullets

- [ ] Team size? Who did you report to?
- [ ] How much biometric data, how often — per user, per day?
- [ ] How many users did the app have?
- [ ] What was the backend and the database?
- [ ] **What does the 99.9% actually measure?** Still blocked.
- [ ] **How was the 60% admin-time reduction measured?** Still blocked.
- [ ] Did the voice-to-SQL pipeline ship to the admin team, and are they using it?
- [ ] Anything you built there that is not on the resume at all?

## The AI Society at ASU — the qualification for every campus role

- [ ] How many students came to the workshops, total or typical?
- [ ] How many workshops did you run, over how long?
- [ ] Did you write the curriculum, or adapt someone else's?
- [ ] Did the freshmen's emotion-detection project finish? Did it work?
- [ ] Were you elected or appointed? How large was the society?

## University of Delhi — your only research entry, currently one line

**Raised again 2026-09-06, and now the most valuable answer on this list.**
You said the entry gets more: the tools you used and the impact you made, as
one crisp bullet. Three of the six on-campus postings (GPH research assistant,
BME course assistant, the general RA pool) weigh this entry first, and two of
them ask by name for scikit-learn, NumPy and SciPy - none of which is on the
page today because nobody wrote down what the Delhi work ran on. One line
from you fixes all of it. See the Delhi rule in CLAUDE.md.

- [ ] What was the dataset? (Name, size, what a row was.)
- [ ] What did you actually do — implement, tune, benchmark, derive?
- [ ] **What tools?** scikit-learn's GaussianProcessClassifier, GPy, GPyTorch,
      NumPy, SciPy, pandas, Jupyter - whichever it really was. Each one you
      name goes on the resume with the Delhi entry as its evidence.
- [ ] **What was the impact?** A number is welcome only with how it was
      measured - "faster than X on Y", "accuracy up from A to B on Z". A
      writeup, a poster, a thesis chapter, a repo, a talk to the group all
      count as impact too.
- [ ] How large was the group, and did you present to it?

## Flickmatch — already recovered once, probably more there

- [ ] How many pages or screens was the site?
- [ ] What does Flickmatch actually do? (The resume never says.)
- [ ] Were you the only front-end engineer?
- [ ] Did the revamp ship publicly? Any before/after in traffic or load time?
- [ ] LinkedIn tags Adobe Premiere Pro on this role — did you do video work too?

## Projects

- [ ] **Torii** — is it deployed anywhere, or local? Tests? Has anyone else used it?
- [ ] **Lead Engine** — is it running for a real client or for you? Is it live now?
      **And what does the 50% actually count?** Still blocked.
- [ ] **Pash** — is it deployed? What did the CUDA workers run on?
- [ ] **Portfolio** — how long did it take? Any traffic?
- [ ] **NeuroPilot, SentinalAI, Lynti** — still unusable stubs. Two sentences
      each unlocks all three. Also: is *SentinalAI* the intended spelling?

## Process, not stack — raised by PayPal, applies to every big employer

Nobody ever wrote down *how* he worked at WatchDNA or MyYogaTeacher, only what
he built. Large employers screen on this and the profile is silent on all of it.

- [ ] **Code review.** Did anyone review your code at WatchDNA or MyYogaTeacher
      — PRs, comments, an approval before merge? Or were you the only engineer
      on it? Either answer is fine; guessing is not.
- [ ] **How work arrived and shipped.** Sprints, stand-ups, tickets (Jira,
      Linear, GitHub Issues)? Branch conventions? Who decided what you built
      next?
- [ ] **Production triage.** Nine months on WatchDNA and nine on MyYogaTeacher
      — what broke, and were you the one who found and fixed it? A concrete
      incident is worth more on the page than the word "maintained".
- [ ] **Design review.** Was there ever a discussion about *how* to build
      something before you built it, with someone else in the room?
- [ ] **Cross-functional.** The voice-to-SQL tool replaced the admin team's
      Ctrl+F workflow — did you sit with that team to learn what it was? Was
      there a PM or a designer you worked with directly at either company?
- [ ] **Testing.** Did you write tests at either company? This decides Pytest
      and Jest, both currently `ask: true`.

## Product sense — raised by Scale, worth answering once for everyone

Scale asks for "talking to customers, figuring out 'what' to build and then
iterating". Every product-engineering posting asks some version of this, and
the profile answers none of it.

- [ ] **Who decided to build the voice-to-SQL tool?** Did you propose it after
      seeing how the admin team worked, or were you handed the spec? If you
      proposed it, that is a whole requirement answered and it is currently
      nowhere on the page.
- [ ] **Did you ever talk to users or customers** at WatchDNA or MyYogaTeacher
      — even internal ones, even once?
- [ ] **Largest data volume you have actually handled** — rows, files, requests
      per day, anything countable. This decides whether "experience building
      systems that process large volumes of data" is a real gap or a fact
      nobody wrote down.
- [ ] **MongoDB** — it is on your old resume with no project behind it. Real,
      or aspirational? Scale names it explicitly.

## The three stubs — Lynti first, and it is now urgent

Lynti came up on the Waymo application and it is the most on-mission project he
has for an autonomous ride-hail company. All that exists is a half sentence.

- [ ] **Lynti: finish the sentence.** "Developed a transportation app using
      React Native in an effort to digitize ride booking and ___". What came
      after "and"? Is it live, did anyone use it, is it still going (LinkedIn
      says "Dec 2024 – Present")? Who else worked on it? What was the backend?
- [ ] **NeuroPilot** — Electron.js and React, 2025. What is it?
- [ ] **SentinalAI** — Python and YOLOv8, 2025. What is it, and is the spelling
      meant to be "Sentinel"?

## Testing and C++ — raised by Waymo, and it decides that application

- [ ] **Can you write C++?** Not "have you seen it" — could you take a coding
      screen in it? Waymo names it as their one required language. Every other
      posting so far let Python satisfy the language requirement; this one does
      not.
- [ ] **Have you written tests?** Unit, integration, anything. Pytest and Jest
      are both on the page as unconfirmed, and Waymo lists testing
      fundamentals as a hard requirement.

## On-campus batch, 2026-09-06 — what six postings asked for that nobody recorded

Each of these is a real question from a real posting. Answer only what is
true; a "no" is useful because it settles what stays off the page.

- [ ] **Have you used a shell?** UNIX/Linux is asked for by the BME course
      assistant posting. Pash's remote CUDA worker and three internships make
      a terminal near-certain, but near-certain is not evidence. Yes or no,
      and where.
- [ ] **Have you ever graded, TA'd, or tutored for pay?** The AI Society
      mentoring is teaching; it is not grading. Also: have you used Gradescope,
      nbgrader or Otter as anything other than a student submitting work?
- [ ] **Jupyter.** Did the Delhi work, or anything else, live in notebooks?
- [ ] **Zotero, Qualtrics, Google Forms** - the GPH research assistant posting
      prefers all three. Used any of them, for anything?
- [ ] **Have you done a literature review** - for Delhi, for a course, for
      anything? Reading papers to decide what to try counts if you did it.
- [ ] **Video editing and 3D design.** Your LinkedIn services list says Video
      Production, Video Editing and 3D Design, and Adobe Premiere Pro is
      tagged on Flickmatch. The Creative Technologist and General RA postings
      both value film editing. Real? What did you edit, with what?
- [ ] **Did you draw the Figma designs at Flickmatch, or implement someone
      else's?** Decides whether "wireframing" is a true word for you.
- [ ] **Have you used Asana or any project tracker?** Gallatin names Asana.
- [ ] **Have you edited a CMS** (WordPress, Drupal, anything)? Stern's Finance
      Department site is the job.
- [ ] **Languages spoken.** The general RA pool matches on this. Hindi?
      Bengali? Anything else?
- [ ] **CovreliefDwarka** is the one organisational credential you have and it
      is blocked on the vaccine-date contradiction (intake #7). For the
      Gallatin gallery job it would matter more than anything technical.

## Cross-cutting

- [ ] Which of **Go, Java, C++, Rust, GitHub Actions, Linux, Pytest, Jest**
      would you welcome a question about? Everything else gets cut — that is an
      improvement, not a loss.
- [ ] Have you used Docker, or is it aspirational? Same for CI/CD.
- [ ] Any hackathons, competitions, awards, scholarships, dean's list?
- [ ] Any open-source contributions, however small?
- [ ] Languages spoken?

---

## Still blocking everything

- [ ] **Work authorization** — citizen/PR or F-1. Gates campus work-study
      eligibility and every sponsorship question.
- [ ] **Phone number.**
- [ ] **GitHub** — or a decision to create one.
- [ ] **NYU school** — Courant or Tandon, and the exact program name.
- [ ] **ASU GPA** — prints only if 3.5 or above.

## MyYogaTeacher feature design and the alerts — said 2026-09-07, details still unnamed

You said you were given the initial design of a feature at MyYogaTeacher
(diagrams, wireframes, user journeys, handed to the dev team you were on) and
that you hook up failure alerts on everything you ship. Both are recorded as
verified facts. Three details would let them go further:

- [ ] **Which feature?** Its name or what it did. A bullet that names it beats
      one that says "a feature".
- [ ] **What did you draw it in?** Figma, Whimsical, Excalidraw, pen and
      paper. If Figma, the Figma skill gets a second evidence entry.
- [ ] **Which alert channel?** Email, Slack, Discord webhook, Sentry,
      CloudWatch, something else - and on which products. The CFA posting
      asks about reliable back-end systems; naming the channel makes the
      claim checkable.

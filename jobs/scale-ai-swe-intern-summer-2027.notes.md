# Scale AI — SWE Intern, Summer 2027 (San Francisco)

## VERDICT: apply — but one answer decides it, and it is not on file

**"A graduation date in Fall 2027 or Spring 2028 with a Bachelor's degree
(or equivalent)."**

This is the whole application, and the profile cannot answer it.
`profile.yaml` says `grad_display: "Expected 2028"`, with a note that it
becomes "Expected May 2028" *once confirmed*. It has never been confirmed —
it is item 3 on `checklists/intake.md`.

- **NYU M.S. finishes May 2028** → Spring 2028, **inside the window. Apply.**
- **NYU M.S. finishes December 2028 or later** → outside it. **Hard no**, and
  no amount of tailoring fixes a stated graduation window.

His **bachelor's** graduated May 2026, which is not in the window and is not
what to put on the form. The degree that matters here is the NYU one.

### The second reading, which is a real risk

The requirement says *Bachelor's degree (or equivalent)*. Read strictly, this
is an **undergraduate** programme and a master's student is the wrong level —
some intern pipelines are genuinely built that way, with separate MS/PhD reqs.
Read normally, "or equivalent" plus a Spring 2028 graduation date puts him in
scope, and master's students apply to reqs worded like this constantly.

It is worth an email to the recruiter rather than a guess, but it is **not**
worth skipping the application over. The date is the gate; the degree level is
a question.

## Everything else

| Requirement | Him |
|---|---|
| May/June start, **San Francisco** | Relocation for a summer is fine. **Check the May start** — NYU's spring term typically runs into mid-May, the same collision flagged on Stoke. |
| **Previous CS/SWE internship experience** | **PASS, three times over.** This requirement filters a lot of applicants and he clears it outright. |
| Product engineering: full-stack web apps, integrating APIs | **PASS.** WatchDNA is full-stack end to end — Node backend, REST, JWT/RBAC, Mapbox front end, admin console. |
| **"talking to customers, figuring out 'what' to build"** | **His best-hidden strength.** The voice-to-SQL tool replaced *the admin team's* Ctrl+F-and-edit workflow — he found out what a real team actually did all day and built the thing that removed it. That is product engineering, and the page currently sells it as an LLM project. See the recovery question below. |
| Track record of shipping | **PASS.** Three internships, an app taken through iOS App Store review, and projects that are live and reachable. |
| **Systems that process large volumes of data** | **The honest weak spot.** 2,129 leads is not volume. Pash is the right *shape* — S3 storage, SQS queue, remote GPU workers, decoupled and asynchronous — and Torii's ledger is per-call. But Scale means billions of tasks, and nothing on the page should imply he has worked at that scale. |
| Python, TypeScript, React, and/or MongoDB | **PASS on three.** TypeScript is his most-evidenced language (Torii, WatchDNA, Lead Engine); Python four times; React three times. MongoDB is a `resume_2026` self-claim with no project behind it — the requirement says "and/or", so it is not needed and should not be leaned on. |

## Why this is a better fit than the requirements list suggests

Their example projects include **"Ship agentic AI applications and the tooling
that makes them observable, testable, and safe to deploy."**

That is a description of Torii. A proxy that sits between agents and the tools
they call, with a policy engine deciding what is allowed (safe to deploy), a
ledger recording every call and why any one was blocked (observable), and
per-agent budgets and identity (testable, bounded). He did not build a demo of
an agent; he built the control plane one runs inside.

Two more of their nine example projects have honest adjacencies: fraud
detection and "use models to estimate the quality of tasks and contributors"
both rhyme with Lead Engine's 0–100 scoring with written reasoning per lead.

The competition for this req is undergraduates from top programmes with FAANG
internships. **Torii is the thing none of them have**, and it should lead.

## Recovery questions this posting raises

- **Who decided to build the voice-to-SQL tool?** Did he propose it after
  watching the admin team work, or was he handed the spec? If he proposed it,
  that is the "figuring out what to build" requirement answered directly, and
  it is currently nowhere on the page.
- **Did he ever talk to users or customers** at WatchDNA or MyYogaTeacher —
  even internal ones?
- **Largest data volume he has actually handled**, in rows or files or requests.
  Needed to know whether the "large volumes" requirement is a gap or a
  recoverable fact.

## Built

`applications/scale-ai-swe-intern-summer-2027/`, preset `scale-swe-2027`,
letter `letters/draft-scale-swe-2027.py`. Resume ATS PASS, one page, 94% fill.
Letter one page, 399 words, zero lint findings.

Projects lead and Torii leads them, against their "agentic AI applications and
the tooling that makes them observable, testable, and safe to deploy" bullet.
Education still comes first because the graduation date is their first
requirement and a screener should not have to hunt for it.

### Two things on the page that need his answer before it is sent

1. **"Expected 2028" is not good enough for this posting specifically.** Their
   gate is "Fall 2027 or **Spring** 2028". A screener reading "Expected 2028"
   cannot tell whether he passes, and the safe assumption for them is that he
   does not. The moment he confirms the month, `grad_display` becomes
   "Expected May 2028" and this application gets meaningfully stronger. It
   cannot be written before he says so.
2. **MongoDB leads the Data & Cloud line** because the posting names it. It is
   a `resume_2026` self-claim with no project behind it - he put it on his own
   resume, so he is already exposed to the question, but the requirement says
   "and/or" and Python, TypeScript and React already satisfy it three times
   over. **Cut it if he would not want the question.**

### What was deliberately kept off

- **Any claim of data volume.** Their sixth requirement is "systems that
  process large volumes of data" and it is the honest gap. Nothing on the page
  or in the letter implies scale he has not worked at.
- **Any claim that he proposed the voice-to-SQL tool or talked to users.** The
  letter says he replaced the admin team's Ctrl+F-and-edit workflow and that
  knowing the workflow was the hard part - which that fact entails. It does not
  say he ran discovery. Open in checklists/recover.md.
- **RAG, vector search, embeddings.** Same call as Bain, sharper reason: this
  is a frontier-model data company and a retrieval keyword he cannot defend
  gets found here faster than anywhere else he is applying.

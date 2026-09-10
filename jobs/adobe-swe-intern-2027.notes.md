# Adobe — Software Engineer Intern 2027

Resume **and** cover letter — he asked for the letter after the resume was
built, so the earlier "resume only" note here is superseded.

## Knockouts

| Gate | Status |
|---|---|
| **Graduation between December 2027 and June 2028** | **UNANSWERED — and it is the gate.** `profile.yaml` says "Expected 2028". If the NYU M.S. finishes May 2028 he is inside the window; if it runs to December 2028 he is outside it. Item 3 on `checklists/intake.md`. |
| Enrolled in a **Bachelor's or Master's** programme in CS | **PASS, cleanly.** |
| Full-time internship between **May and September** | **PASS.** A generous window - a June start clears NYU's spring term with room, where Stoke's "May 2027" and Scale's "May/June" were tight. |
| Proficiency in at least one of Java, Python, C++, JavaScript | **PASS outright** on Python and JavaScript. |
| Co-located hybrid, office assigned by team | **Office not stated in the posting.** He is in New York; Adobe's engineering weight is San Jose. Worth knowing which req he is applying to before he commits to relocation. |
| Work authorization | Not mentioned. Standing unknown. |

### This is the cleanest graduation gate of the three that have one

Worth noting against the others, because the same unanswered fact decides all
of them and the answer is probably a single word:

| | window | master's student? |
|---|---|---|
| **Adobe** | Dec 2027 - June 2028 | **explicit: "Bachelor's or Master's"** |
| Scale | Fall 2027 or Spring 2028 | ambiguous - "Bachelor's degree (or equivalent)" |
| Primer | none stated | n/a |

A May 2028 graduation satisfies Adobe and Scale both. **Adobe is the one with
no degree-level ambiguity at all**, so if he only confirms one thing this week,
confirming the graduation month unlocks two applications.

## The requirement almost nobody else can answer

> *Exposure to or interest in modern development tools, including AI-assisted
> tools, and **an understanding of how to use them responsibly.***

Most applicants answer this with "I use Copilot". Torii is a system built for
exactly this problem: identity per agent, a policy engine deciding what an
agent is allowed to call, budgets enforced before the call, and a ledger
recording every call **and every reason one was blocked.** His own framing for
it, in `protected_strings`, is *"The human controls policy. The agent controls
execution."*

That is a considered position on responsible AI tooling, held in code rather
than in an opinion. With no cover letter on this application, the Torii bullets
and the skills block are the only places it can be made - which is why
**"AI & Agents" is the second skills line**, directly under Languages.

## The rest, against the fact base

| Their line | Him |
|---|---|
| "designing, building, deploying, and maintaining applications" | **WatchDNA answers all four in one entry** - built from scratch, shipped a companion app through iOS App Store review, then carried it for nine months. This is the SDLC requirement and it is his strongest single credential for it. |
| Fundamentals: data structures, algorithms, coding principles | Coursework. Not something a resume argues. |
| Applications built through coursework, projects or internships | **PASS overwhelmingly** - three internships, four projects on the page. |
| Debugging, iterating in a fast-paced environment | Entailed by nine months on two production codebases. Still unrecorded - see `checklists/recover.md`. |
| **"stand-ups, code reviews, and design discussions"** | **The standing gap.** Third posting in a row to name code review explicitly, and it is still unanswered - he may have been the only engineer at both companies. |
| Clear communication, collaboration | AI Society: wrote the teaching materials, ran the workshops, mentored four freshmen. |
| Designers and product managers | Flickmatch implemented a designer's Figma work across a whole site. |

Java and C++ are held off. The requirement is "at least one ... such as Java,
Python, C++, or JavaScript" and Python satisfies it four times over - the same
call as C# on McKesson and Java on PayPal.

## Built

`applications/adobe-swe-intern-2027/` — `resume.pdf` (preset
`adobe-swe-2027`, ATS PASS, one page, 94% fill, six clickable links) and
`cover-letter.pdf` (one page, 397 words, zero lint findings, three clickable
links).

The letter's first paragraph is the responsible-AI-tooling answer and carries
his protected line **verbatim**: *"The human controls policy. The agent
controls execution."* It was paraphrased on the first draft and corrected -
`protected_strings` entries may be selected but never reworded.

**The App Store claim is deliberately absent from the letter.**
`wd.companion.ios` is blocked in profile.yaml pending `appstore_outcome`, and
prose is not a way around a gate the resume respects. The unblocked phrasing -
shipping a companion app on the same infrastructure - carries the point.

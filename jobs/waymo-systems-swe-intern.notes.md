# Waymo — SWE Intern, Systems Engineering (HIL test infrastructure)

## READ THIS FIRST: weakest technical match in the folder

**Two of their four hard requirements are unevidenced.** Not "preferred" —
the "You have" list:

| Their hard requirement | Him |
|---|---|
| **Proficiency in software development using C++** | **`ask: true`. No evidencing project.** |
| Core CS concepts (data structures, algorithms, OOD) | Coursework. Fine. |
| **Familiarity with software testing fundamentals** (unit, integration, regression) | **Pytest and Jest are both `ask: true`.** Nothing in the profile shows a test he has written. |
| Currently pursuing a **Bachelor's** degree | **He finished his B.S. in May 2026 and is pursuing an M.S.** |

Every posting before this one asked for *"at least one language such as Java,
Python, C++, or JavaScript"*, and Python satisfied it four times over, so C++
came off the page at zero cost. **This posting is different.** C++ is named
alone, in the must-have list, as the language the work is done in. Python is
only in "We prefer".

**So leaving C++ off does not make this application safer. It makes it
pointless.** It is on the resume, along with Pytest, and every build prints:

> ON THE PAGE BUT UNCONFIRMED - be ready to be interviewed on each, or cut it:
> C++, Pytest.

**This application exists only if he can actually write C++ and has actually
written tests.** If he cannot, the answer is not a different resume — it is a
different req. Which brings up the second thing.

## The degree tier, and the "apply to your top 3" line

The posting says *"Currently pursuing a **Bachelor's** degree"* and the pay
band is labelled **"Hourly Bachelors Pay $60—$60 USD"**. A company that tiers
intern pay by degree almost always runs a **separate master's-level req** for
the same team.

The posting also says: *"To be in consideration for multiple roles, you will
need to apply to each one individually — please apply to the top 3 roles you
are interested in."*

**So before sending this one, look at Waymo's other open intern reqs.** There
is likely a Systems Engineering intern posting that matches both his degree
level and a language he can actually defend, and it would be a strictly better
use of one of his three slots. This posting is C++ test infrastructure; his
profile is Python and TypeScript product engineering.

## Where he is genuinely strong

One of their four "You will" bullets he answers better than most applicants:

> *Author technical design documents and user guides, and lead technical demos
> or workshops to onboard engineers to newly developed automation
> capabilities.*

That is the AI Society entry almost word for word — wrote the teaching
materials, ran the workshops, made ML approachable to students with no
technical background, mentored four freshmen. Interns are rarely hired for
this, but it is a real and unusual match, so **AI Society sits second in
Experience.**

**Pash leads Projects**, which no other preset does. The role is test
infrastructure and pipelines, and Pash is the closest thing he has built: work
lands in S3, jobs queue through SQS, remote CUDA workers execute them. That is
a job runner with execution moved off the requesting machine — the right shape
for a bench harness, even though the domain is audio. Torii drops to third; it
is his best project everywhere else, but TypeScript agent tooling is the least
relevant thing on this page.

Their preferred list also names **CI/CD** (evidenced, `resume_2026`) and
**developer tooling** (the WatchDNA admin console and endpoint-discovery
pipeline).

Real gaps, correctly left off: **HIL benches, embedded systems, protobuf, RPC
frameworks.** He has none, and nothing on the page implies otherwise.

## Lynti, and exactly how far it was used

Asmit asked for Lynti in the letter. Everything recorded about it is one
truncated line from the LinkedIn export:

> "Developed a transportation app using React Native in an effort to digitize
> ride booking and ..."   *(truncated; Dec 2024 – Present)*

`profile.yaml` carries it as a stub: `facts: []`, `status: needs_confirmation`.

The letter says exactly what that fragment says and **not one word more** — a
transportation app, React Native, to digitize ride booking. No scale, no users,
no outcome, no dates.

It is placed as **motivation, not engineering evidence.** A React Native
ride-booking app is not test infrastructure, and dressing it up as such would
be obvious to the first engineer who read it. What it honestly is: the reason a
person applies to Waymo specifically, and it ends on the admission that the
hard half is the half he did not build.

**To say more, he has to finish the sentence.** What did "digitize ride booking
and ..." continue into? Is it live? Did anyone use it? Is it still going, as
"Present" suggests? Those answers would turn a stub into a real entry — and
Lynti is the single most on-mission project he has for this company.

## Built

`applications/waymo-systems-swe-intern/` — preset `waymo-systems-2027`,
letter `letters/draft-waymo-systems-2027.py`. Resume ATS PASS, one page, 95%
fill. Letter one page, 389 words, zero lint blocks.

**C++ is not claimed anywhere in the letter.** It renders on the resume because
the application is meaningless without it, but prose asserting proficiency he
has not confirmed is a different thing entirely.

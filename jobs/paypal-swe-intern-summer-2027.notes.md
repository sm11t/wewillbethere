# PayPal — Software Engineer Intern, Summer 2027

## Knockouts

| Gate | Status |
|---|---|
| Summer 2027 only (Spring/Fall 2027 not available) | **PASS** |
| Pursuing a BS/MS in CS or a related technical field | **PASS** — NYU M.S. CS |
| **Must be returning to school in Fall 2027** | **PASS** — expected 2028 graduation, so he returns |
| At least one of Java, Python, C++, JavaScript | **PASS outright on Python and JavaScript.** Both are evidenced four and two times over. |
| **Work authorization / sponsorship** | **UNKNOWN. Standing blocker.** The posting says nothing either way. Not the hard export-control gate Stoke has, but it must be answered before he fills the form — and he answers it, not us. |
| **Location** | **UNKNOWN.** The paste truncated at "Primary Location \| Pay Range: generae for this". PayPal posts this req in San Jose, Austin, Chicago, Scottsdale and NYC. Which one changes the close of the letter and the relocation answer. |

Everything that can be checked from the profile passes. The two unknowns are
both his to answer.

## The named stack, against the fact base

The Essential Responsibilities name six technologies. Five have evidence:

| PayPal names | Him | Verdict |
|---|---|---|
| Python | Lead Engine (FastAPI backend), WatchDNA endpoint-discovery pipeline, MyYogaTeacher, Delhi | `existing` |
| Node.js | WatchDNA | `existing` |
| React | Lead Engine, Portfolio, Flickmatch | `existing` |
| SQL | voice-to-SQL, Torii ledger, Lead Engine | `existing` |
| REST APIs | WatchDNA, Lead Engine | `existing` |
| **Java** | `ask: true`, from his own 2026 resume, **no evidencing project** | **see below** |

Five of six named technologies, all defensible. This is the second-best
technical match in the folder after Stoke, and unlike Stoke there is no export
control wall.

### Java is the one decision on this application

PayPal names Java **first** in the responsibilities and runs Java at enormous
scale — this is the posting where a Java keyword he cannot defend gets probed
in the first technical screen, at a company that would know.

But the Minimum Qualification asks for **"at least one programming language,
such as Java, Python, C++, JavaScript, or similar."** Python satisfies it
outright, four times over. So Java is worth nothing as a gate-passer and
everything as a liability.

Same shape as McKesson, where C# would have bought a hostile screening question
for free. **Built with Java and C++ excluded.** Put them back only if he says he
can talk through a Java project for ten minutes.

## Requirements with no clean answer yet

These are not stack gaps, they are *process* claims — and the profile is silent
on all of them because nobody ever wrote down how he worked, only what he built.
Per the recovery procedure, they are questions for him, not assumptions.

| Their line | Status |
|---|---|
| "develop and optimize databases; ensure data integrity" | **`supported`, strongly.** Backend from scratch at WatchDNA (databases, JWT, RBAC middleware); time-series deduplication on the MyYogaTeacher client is *literally* a data-integrity mechanism; address-fingerprint dedup in Lead Engine; SQLite audit ledger in Torii. Not listed as a skill anywhere — surface it in a bullet. |
| "triage production issues", "debug and maintain" | **RECOVERY CANDIDATE.** Nine months on WatchDNA's production codebase and nine on MyYogaTeacher's entails debugging and maintenance. Entailed, but ask before writing it at full scope. |
| "code and design reviews" | **GAP — do not assume.** He may have been the only engineer. This is exactly the case CLAUDE.md names: shipping to the App Store entails a release process, it does **not** entail code review. Ask. |
| "SDLC processes, internal standards, coding conventions" | **RECOVERY CANDIDATE.** Two real companies over eighteen months. Sprints, tickets, PRs, branch conventions — almost certainly yes, but unrecorded. Ask. |
| "collaborate with design, product and other business teams" | **`supported`.** Flickmatch was implementing a designer's Figma work across a whole site. And the voice-to-SQL tool replaced *the admin team's* Ctrl+F-and-edit workflow — you cannot replace a team's workflow without first sitting with them and learning what it was. That is real cross-functional work and it is currently invisible on the page. |
| "distributed systems ... at a scale few companies can match" | **Honest adjacency only.** Pash is decoupled and asynchronous — S3 for storage, SQS as the job queue, remote CUDA workers doing the separation. That is the right *shape*. It is not PayPal scale and no bullet should imply it is. |
| data structures, algorithms, OOP, debugging | Coursework. Fine, and not something a resume argues. |

## The angle: Torii is a payments-authorization system

This is the thing to notice about this application, and it is why the letter
writes itself.

Torii's **pre-authorization budget tracker reserves funds before the upstream
call so two agents cannot overspend at once.** Reserve, then settle. That is
the authorization-and-capture split PayPal's own network runs on, arrived at
independently because the concurrency problem forced it. Around it: JWT
identity on every request, a JSON policy engine deciding what is allowed, and a
SQLite ledger recording every call *and every reason one was blocked* — which
is an audit trail, the thing risk and compliance teams live in.

And the payment rail is real money: it intercepts the HTTP 402, checks the
wallet, pays, and retries, settling USDC on Base.

No other applicant to this req built a payment authorization layer. It leads
Projects, and it is the whole technical middle of the letter.

## Preset

`paypal-swe-2027` in profile/variants.yaml. Experience first — PayPal is a large
ATS-screened employer that asks for internship experience, and WatchDNA's
full-stack Node/PostgreSQL/JWT/REST work is their stack almost line for line.
Torii leads Projects to put the payments parallel on the page.

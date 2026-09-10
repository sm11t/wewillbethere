# Instructions for Claude: tailoring a resume to a job

This project is the parent. It owns two tools and one profile.

```
wewillbethere/                 <- you are here; this file governs
├── profile/profile.yaml       <- THE source of truth for both tools
├── engine/                    <- tool 1: makes the documents
├── tools/career-ops/          <- tool 2: finds and tracks the jobs
└── jobs/                      <- job descriptions, the handoff between them
```

**Tool 1 — `engine/` (ours).** Turns the fact base into a verified resume via
resume.lol. Enforces provenance, blocks unbacked metrics, lints for AI tells,
and gates every PDF through three parsers. This is what produces anything Asmit
sends.

**Tool 2 — `tools/career-ops/` (third party).** A 125-script job-search system,
actively developed upstream, pinned at `455bf37` (2026-09-03). Its job is
*discovery and tracking*: `scan.mjs` queries ~90 public ATS APIs (Greenhouse,
Lever, Ashby, Workday, iCIMS, SmartRecruiters, higheredjobs …) with no auth and
no tokens, and `jd-skill-gap.mjs` classifies a posting's requirements against
the CV with zero LLM calls.

Its own `CLAUDE.md`, `AGENTS.md` and `CODEX.md` were renamed to
`docs-agent-*.md` so they do not compete with this file. Read them when working
*inside* that tool; this file wins everywhere else.

## The bridge — one profile, two tools

`profile/profile.yaml` is the only place facts live. career-ops needs a markdown
CV, so we generate it rather than keeping a second copy that could drift:

```powershell
python -m engine.export_cv_md      # profile.yaml -> tools/career-ops/cv.md
```

**Run this after any profile change.** career-ops scores postings against that
file.

One rule the export enforces: **skills marked `ask: true` are withheld from
`cv.md`.** career-ops would otherwise rate a posting as a match on a tool Asmit
has not confirmed using, steering him toward the jobs he is *least* able to
defend. Not even in an HTML comment — `jd-skill-gap` reads the whole file as
prose, and a commented-out list still counted as evidence.

## Which tool for which job

| Task | Tool |
|---|---|
| Find postings | `cd tools/career-ops && node scan.mjs` |
| Is this posting still live? | `node check-liveness.mjs` |
| What does this JD need that he lacks? | `node jd-skill-gap.mjs jds/<file>.md` |
| Track what was applied to, and follow-ups | `node tracker.mjs`, `followup-cadence.mjs` |
| **Build the resume** | `python -m engine.publish full --draft` |
| **Check it is sendable** | `python -m engine.status` |

Deliberately unused in career-ops: the dashboard, the SQLite index, batch
evaluation, salary-gap, negotiation ROI, funnel velocity. Those serve a
740-posting senior search; Asmit has a dozen targets and a deadline this month.
Its PDF generation is unused too — ours is measured.

Playwright is **not** installed for it (a ~400 MB browser download used for
PDF export and browser-based liveness checks, neither of which we need).
`node doctor.mjs` will keep reporting that one issue; it is expected.

---

## Per-job workflow

1. **Save the posting.** Paste it into `jobs/<company>-<role>.md`, or let
   `scan.mjs` find it. Postings disappear; you will want the original when
   preparing for the interview.
2. **Extract requirements** into three buckets:
   - *Knockouts* — work authorization, graduation date, hours, on-site. If any
     is unknown, stop and ask. Never answer a screening question for him.
   - *Hard requirements* — the named technologies and years.
   - *Preferred* — the nice-to-haves, which is where keyword coverage pays.
3. **Map each requirement** onto the fact base. Run
   `cd tools/career-ops && node jd-skill-gap.mjs <jd>` for the mechanical pass
   first - it is regex-based, free, and instant. Three outcomes:
   - `existing` — already in `skills:` with evidence. Surface it.
   - `supported` — demonstrated inside a bullet but not listed. Add it to the
     skills line.
   - `gap` — he has not done it. **Print the gap. Never paper over it.**
4. **Pick a preset** (`profile/variants.yaml`) or add one. Reorder sections so
   the thing the job cares about is first.
5. **Reorder the skills lines** so the job's vocabulary appears early in each
   line. Recruiters skim the first few items.
6. **Build:** `python -m engine.publish <preset> --draft`
7. **Read every gate output.** ATS verdict, the unconfirmed-skills note, the
   voice lint. Do not ship on a FAIL.
8. **One page, always.** Never send two.

### How everything fits on one page

Nothing is dropped from Experience or Projects to make room. Three levers do the
work, in this order:

1. **One line per skills category.** `fit_skills_to_one_line()` measures real
   text width (Times metrics — Tinos is metrically compatible with Times New
   Roman by design) and trims each category until its line does not wrap. A
   wrapped skills line spends a whole row on two words; capping them is what
   buys the vertical space for everything else.
2. **Spacing, not type size.** The ladder tightens vertical rhythm and type
   independently. Closed-up leading reads as deliberate; text under about 9pt
   reads as a resume that did not fit. Spacing gives way first.
3. **Only then, type size.** The ladder bottoms out at 0.85 scale.

If it still will not fit, **cut a skill or a bullet — never a role or a
project.** Report what was cut.

Within a category, skills with real evidence are ordered before anything marked
`ask: true`, so the unvouched keyword is the first thing to fall off the end of
a full line. Reorder per job: whatever the posting names goes first, and
whatever falls off was the least relevant thing on the line.

### Getting to one page, measured

The master runs two pages with everything in. Measured on this content, the
cheapest cut that reaches one page is **dropping Flickmatch and the Portfolio
project** — that fits at 94% fill with every skill line intact.

Cut in this order, stopping as soon as it fits:

1. **Flickmatch** (May–Aug 2023, one bullet). Oldest, weakest, and the least
   related to anything he is applying for now.
2. **Portfolio.** Lovely, but the least load-bearing project on the page.
3. **A third bullet** from WatchDNA — it is the only entry carrying three.
4. **A skills category** the posting does not care about.

Do not reach for smaller type instead. The ladder bottoms out at 0.85 scale and
below that the page reads as squeezed, which is its own signal. If content still
will not fit, cut more content and say what was cut.

## Keyword matching, and where the line is

Getting past keyword search is a real goal and mostly a legitimate one. Asmit has
done three internships and seven-plus projects; the fact base is an incomplete
record of what he has actually touched. Recovering a real tool that was simply
never written down is not embellishment.

**Legitimate, do it freely:**

- **Use their word for the same thing.** A posting says "RBAC"; the profile says
  "role-based access control". Print theirs. Same referent, their vocabulary.
- **Surface the relevant subset.** A posting wants Supabase and says nothing
  about Vercel — lead the Data line with Supabase. Choosing which true things to
  show is the whole job.
- **Add tools genuinely used but never recorded.** If a project used Postman or
  pytest and nobody wrote it down, add it with an `evidence:` entry naming the
  project.
- **Expand an acronym, or contract it,** to match the posting.
- **Reorder anything.** Order carries no truth claim.

**Name what a system actually touches.** A bullet that says a pipeline reads
"public listing and county-record sources" describes nothing a reader can
picture. Lead Engine scouts **Zillow, Redfin, FSBO, expired listings and the
Maricopa County Assessor** - five named sources, all already published on his
own site and LinkedIn - and the resume says so, on his instruction of
2026-09-05. This reversed an earlier caution that naming scraped sites invites a
terms-of-service question. He may still get that question; his answer is that
these are public listings and public county records. The general rule it stands
for: **when he has already published a detail himself, withholding it from the
resume buys no safety and costs the only concrete thing in the bullet.**

### Keywords he covered in a class - standing instruction, 2026-09-07

He said it in these words: *"it is alright to add missing keywords in resume
because I have taken everything in some or the other class ... we are trying
to maximise the keyword matching and our chances."* So:

- **A keyword a posting names may go on the resume when it is missing**, with
  `evidence: [coursework_2026-09-07]` in `profile.yaml`. Coursework is real
  evidence - weaker than a project, stronger than nothing - and the interview
  answer is the course. First applied to Java and Ruby for Betterment.
- **It goes into the skills block only.** A bullet still needs a project or a
  job behind it; a class does not put a tool inside an Experience line.
- **Skills with project evidence still sort ahead of coursework-only skills**
  on a line, so if a line is full the coursework keyword is the one that falls
  off - unless the posting names it, in which case `skill_lead` puts it first.
- **Report every coursework-only keyword to him in the notes file** for the
  posting, so he knows which interview questions to expect on it.
- This does not touch numbers, scope, or bullets. Hard rule 1 stands for
  facts; it was never about which true keywords appear.

### What the internships achieved - standing instruction, 2026-09-07

His words: at WatchDNA *"the tools built ... are so important for driving
user traffic and increased traffic within 6 months of usage ... I replaced the
service provider expensive app with an inhouse built version cutting down
costs for the business"*; at MyYogaTeacher, *"mention the time saved and
value provided"*; and *"I am always building new things and experimenting
with new technology and keep myself updated."* Recorded in `profile.yaml` as
`wd.impact` and `myt.voicesql.time` (verified, `approved: false`, no numbers
because none were given). So, in every internship letter:

1. **WatchDNA carries its business impact:** the in-house locator and admin
   console replaced an expensive third-party app the company had been paying
   for, and traffic was up within six months of going live. Cost and traffic
   stay unquantified until he gives a figure and how it was measured.
2. **MyYogaTeacher carries the time saved:** the voice-to-SQL pipeline
   replaced the admin team's Ctrl+F-and-edit workflow and gave them back the
   time it took. The 60% figure stays blocked.
3. **Before the personal projects, one hinge sentence:** he is always
   building something, usually to try a technology he has not used yet, with
   the projects named as the method (rule 5 of the personal paragraph: a
   claim with its method attached).

The two facts carry the flavor `impact`, which no preset prefers, so they do
not change any resume until a preset lists `impact` in `prefer_flavors`;
`wd.impact.short` is the bullet that would render. (Appending them last was
not enough - the selector ranks by flavor, not position, and on the first
build they displaced the biometrics and companion-app bullets.)

### Automation, DevOps and testing on the resume - standing instruction, 2026-09-07

His words, on reading the MiniMed posting: *"mention terms like automation
devops and testing for my work in the resumes."* Applied as:

- **Skills:** `Automation` with project evidence (the WatchDNA
  endpoint-discovery pipeline; Lead Engine's five scouts running unattended),
  `DevOps` and `Software testing` on coursework evidence under the rule
  above. All three sit in the `Data & Cloud` category and lead the SWE
  internship presets after Docker and CI/CD.
- **Bullets:** the WatchDNA locator phrasing `wd.locator.auto` uses the
  canonical's own word, "automated", and is listed first so it renders.
  "On its own" and "automated" describe the same pipeline; the posting's
  word wins.
- **Not done:** Pytest and Jest stay `ask: true`. Naming a framework claims
  more than naming the discipline, and nothing records him writing tests.
  Ask before either prints.

**Not legitimate, no matter what the posting asks for:**

- **A tool he has neither used nor studied.** A keyword he cannot be
  questioned on is worth less than a missing keyword, because failing on it
  discredits the rest of the page. Since 2026-09-07 "studied in a class"
  counts, on his word, and is recorded as such.
- **Inflating scope or ownership.** "Built" when he integrated; "led" when he
  contributed.
- **Inventing or rounding a metric.** Four are already blocked pending his
  explanation; do not add a fifth.
- **Hidden text, white font, keyword stuffing, injected prompts.** The parsed
  layer is exactly what the recruiter reads, and discovery is treated as fraud.

**The test:** could he answer *"tell me about a time you used this"* without
inventing anything? If yes, add it. If no, leave it off and note the gap.

### The profile understates. Assume there is more.

**Start from the assumption that every entry is thinner than the work was.**
`profile.yaml` was built from a LinkedIn export and an old resume - both written
quickly, years after the fact, by someone with no reason to be thorough. It is a
lossy summary of his career, not a record of it.

The proof is Flickmatch. For a week the entry read *"Turned Figma designs into
responsive Material-UI components"*, because that is roughly what LinkedIn said.
What actually happened was that he revamped the entire website. One sentence
from him doubled the entry and upgraded a components claim into a scope claim.
There is almost certainly more of that in every other entry.

So when a posting asks for something the profile does not show, the first
question is **not** "can we stretch this?" It is **"did he already do this and
nobody wrote it down?"** That is where nearly all the real gains are, and it
costs nothing in honesty.

#### The recovery procedure

1. **Read the entry and ask what the work necessarily involved.** Nine months on
   one production codebase entails debugging, iteration, deployment and
   maintenance. Taking an app through iOS App Store review entails handling
   reviewer feedback and a release process. These are not embellishments; they
   are what the job was.
2. **Separate entailed from merely plausible.** Shipping to the App Store
   entails a release process. It does **not** entail code review, CI, or unit
   tests - he may have been the only engineer. Plausible is not evidence.
3. **Ask him. Never assume.** Generate the candidates, put them in front of him
   as questions, and wait. `checklists/recover.md` holds the standing list -
   work through it whenever an entry looks thin for a posting, and keep adding
   to it.
4. **A confirmed answer becomes a `verified` fact** under a dated
   `user_YYYY-MM-DD` source - a stronger provenance than anything inherited
   from LinkedIn, which stays `self_reported`.
5. **Write the bullet at the true scope**, not the modest one. "Revamped the
   website end to end" and "turned designs into components" describe the same
   work; only one of them describes it accurately.

#### Where the line is

He set it himself: **as long as it makes sense on the background of the project
or internship.**

- **Recovering** what he did but never recorded - correct, and the main job.
- **Stating the real scope** instead of the modest one he happened to type into
  LinkedIn - correct.
- **Using the posting's vocabulary** for something he did - correct.
- **Inferring a tool that the work could not have happened without** - correct,
  and say so out loud. Material-UI is a React library, so React is not a
  separate claim.
- **Adding a tool or a task he did not do**, because the posting asks for it -
  not correct, whatever the posting is worth. The cost lands in his interview,
  not on the page. And it is rarely necessary: when McKesson asked for "C#,
  Java, or Python", Python satisfied it outright, so C# would have bought a
  hostile screening question for nothing.
- **Inventing or rounding a number** - not correct. Four are already blocked.

#### Underplaying is a real failure, not a safe default

An unrecorded fact and a false one are both wrong; only one of them is
recoverable. If an entry looks thin, treat it as a bug in the profile and go
and find the missing material - do not quietly ship the thin version and call
it caution.

### The Delhi entry: one crisp bullet, tools and impact

**Standing instruction, 2026-09-06.** The University of Delhi entry is the
only line on the profile that says "has done research", and it is also the
thinnest: one sentence inherited from LinkedIn, *"worked under Prof. R. P.
Singh on optimizing Gaussian Process classifiers for high-dimensional data."*
For every research assistantship and every course-assistant posting it is the
entry the reader weighs first, and right now it names no tool and no result.

He has said there is more, and how it is to be added: **the tools he used and
the impact he made, as one crisp bullet.** Not two bullets, not a paragraph.
The rule, so nobody pads it back out:

1. **Ask before writing.** Dataset; what he actually did (implemented, tuned,
   benchmarked, derived); the tools (scikit-learn's `GaussianProcessClassifier`,
   GPy, GPyTorch, NumPy, SciPy - whichever it really was); the result (an
   accuracy or speed comparison, a writeup, a poster, a thesis chapter); and
   whether he presented it. The questions are in `checklists/recover.md`.
2. **When he answers, it becomes a `verified` fact** under a dated
   `user_YYYY-MM-DD` source: a new fact `du.tools` in `profile.yaml` with one
   variant, sourced to him, `approved: false` until he reads it aloud.
3. **Every tool he names gets `evidence: [delhi]`** in the skills list. This is
   the honest route to putting scikit-learn, NumPy or SciPy on the page - all
   of which the BME and GPH postings ask for and none of which is evidenced
   today. Nothing gets added on the strength of "a Gaussian Process classifier
   is a scikit-learn class"; that is plausible, not entailed.
4. **A number ships only with its mechanism.** "Cut training time by 40%" needs
   "against what, measured how" or it is blocked like the other four.
5. **The entry never exceeds two bullets.** The new bullet sits under the
   existing line. If it can carry the Prof. Singh clause itself in about
   twenty-five words, it replaces the old line and the entry is one bullet.
   Crisp means a reader gets tool, task and outcome in a single breath.

Until he answers, nothing changes on the page. Do not draft the bullet from
guesses to "have something ready" - a placeholder in the profile is exactly the
kind of thing that gets approved by accident.

### Every link on the page must be clickable

**Standing rule, 2026-09-05.** He opened a built PDF, clicked LinkedIn, and
nothing happened. The header was rendering as plain `<span>` text - `build.py`
appended `link["render_as"]` and dropped the `url` on the floor, so the contact
line looked like links and behaved like paragraph text. Project links worked;
the header never had.

A resume is read on screen at least as often as on paper. An address printed as
plain text is an instruction to retype it by hand, and most readers will not.

The fix carries `contact_links` from `build.py` into `emit_rlol.to_markdown()`,
which wraps any item with a URL behind it in an anchor. **The display text stays
a flat list of strings** so the ATS expectations and the extraction baseline are
untouched.

**Email and phone are deliberately NOT linked.** Both are redactable variables
with hidden twins for share links, and a `mailto:` href would carry the real
address in the markup even when the visible text is redacted - which defeats the
whole point of the redaction. Do not "fix" this.

**How to check it, on every build.** Anchors in the HTML are not proof; what
matters is whether the PDF carries real link annotations:

```powershell
python -c "import re; raw=open('out/.build/asmit-<preset>.pdf','rb').read(); print(sorted(set(re.findall(rb'/URI\s*\(([^)]*)\)', raw))))"
```

Six should come back on a full SWE preset: portfolio, LinkedIn, GitHub, and one
per linked project. **Cover letters carry the same letterhead and the same
rule** - three on a letter, since a letter links no projects. `emit_letter`
reads the URLs from `profile.yaml` rather than from the draft, so a changed
link changes in one place and no draft has to be touched.

### Skills: fill the line

Skill lines should run to the full measure — a half-empty line wastes a
recruiter's most scannable region. Five categories, each a full line:

`Languages` · `AI & Agents` · `Backend & APIs` · `Frontend & Mobile` ·
`Data & Cloud`

Categories live in `profile/variants.yaml`; skills and their evidence live in
`profile.yaml`. Add job-relevant true skills to the pool, then order each line
so the posting's terms come first.

Every load-bearing technology should also appear **inside a bullet**, not only
in the skills block. Recruiters search the whole document, and a term that
appears only in a list reads as a list.

### Skills that are on the page but unconfirmed

Some entries carry `ask: true`: plausible, requested for coverage, but with
nothing behind them yet. They render, and every build prints them under
`ON THE PAGE BUT UNCONFIRMED`. Currently:

> C++, Rust, LangGraph, RAG, Vector search, Embeddings,
> scikit-learn, PyTorch, Linux, Pytest, Jest

Moved to coursework evidence on 2026-09-07 under his instruction, each the
day a posting named it: Java, Go and GitHub Actions (off this list), and
Ruby, Jira, Agile, DevOps, Software testing and Accessibility (added new).
See "Keywords he covered in a class" above - any of the rest can move the
same way the day a posting names it. Pytest and Jest stay here on purpose:
naming a test framework claims more than naming the discipline.

**Before sending any resume, cut every one of these Asmit cannot be interviewed
on.** When he confirms one, replace `ask: true` with `evidence: [...]` naming
where he used it. This list is not a nag; it is the difference between a
keyword-dense resume and a resume that collapses in the first technical screen.

## Cover letters

**The working guidelines live in `letters/GUIDELINES.md`. Read that file
before drafting or editing any letter.** It carries the research step (who
the reader is, what they published, what one anchor the letter may use), the
voice rules the linter cannot check, the three genres with their targets, who
writes which part, and the send checklist. This section keeps the structure
and the history of each decision.

A different genre with different rules. `letters/` holds the drafts,
`engine/emit_letter.py` renders them, `engine/publish_letter.py` ships them.

```powershell
python -m engine.publish_letter letters/<draft>.py
```

Each draft is a Python file defining a `LETTER` dict. Output is a one-page PDF
on the same letterhead as the resume, plus a `.txt` for portals with a paste
box.

### The structure

```
letterhead              name, contact, rule - identical to the resume
date + recipient
personal paragraph      who he is. NEVER about his projects.
signpost (italic)       "I would encourage you to visit my portfolio at
                         www.asmit.space."
technical paragraphs    the ONLY part that changes per job
close                   what he wants, plainly - availability, and nothing else
```

No typed signature. The letterhead already carries the name at the top, so a
name at the bottom is repetition rather than a closing.

**The signpost changed on 2026-09-05** and the old one must not come back. It
read *"If you would rather have evidence than opinion, this is where it
starts."* - a line that announces a turn rather than making one, and the sort of
constructed sentence the voice lint exists to catch. His replacement points at
the portfolio and does the same navigational work in one clause.

**The close lost its last sentence at the same time.** Every internship letter
used to end *"The projects are all at asmit.space if you would rather read code
than prose."* That existed only because nothing else pointed at the portfolio.
The new signpost does, so keeping it would name asmit.space twice in four
hundred words and echo the exact "if you would rather X than Y" construction
being retired. **The close is now availability and nothing else.**

### What is constant and what varies

**Constant across every application:** the personal paragraph, the signpost,
and the close. That paragraph is his voice, not per-job filler, and rewriting
it per job is what turns a letter into a mail merge.

**Varies:** the recipient block and the technical paragraphs. Two at most.
The seam is a sentence like *"The work closest to what your team does is..."* -
that is where the tailoring goes.

### Rules for the personal paragraph

1. **Never mention a project, an employer, or a credential.** It is about how he
   thinks, not what he has shipped. The evidence has its own section below and
   borrowing from it early wastes both.
2. **Never name a philosopher and never quote one.** The ideology is the *shape*
   of the paragraph. A reader who knows it recognises it; a reader who does not
   just meets someone who thinks clearly. Naming turns a point of view into a
   citation and the reader starts grading his reading list.
3. **Never state a trait.** Not "I am curious", not "I know how to ask the right
   questions" - the linter blocks these. State the *observed consequence*
   instead: *"I have seen them frustrate people"* cannot be written by someone
   who has not done it, and it doubles as self-awareness. A cost admitted is
   more persuasive than a strength claimed.
4. **One admission, not two.** Admitting a limit buys credibility. Admitting two
   is a pattern, and the reader starts believing it.
5. **A claim needs its method attached.** "I think about problems in systems"
   survives only because the next clause shows what that means. A claim left
   alone reads as a boast; a claim followed by its method reads as description.
6. **Keep it around 175 words**, in his diction. Plain sentences, no literary
   phrasing. If a sentence sounds like a writer wrote it, it is wrong.

#### The teaching sentences, added 2026-09-05

He asked for two things in it: that he likes helping people and sharing what he
knows, and that he believes **sharing knowledge increases it.** Both arrive as
observed consequences, because rule 3 forbids stating either one directly:

> It works the other way too. When someone is stuck on something I have already
> worked out, I will sit with them rather than hand over the answer, and I come
> out of those understanding it better than when I went in. Knowledge seems to
> be one of the few things that grows when you share it.

Why it is phrased this way, so nobody "improves" it back into a trait claim:

- *"I love helping people"* is exactly the sentence rule 3 blocks. **"I will sit
  with them rather than hand over the answer"** is a behaviour, and one nobody
  can write who has not done it.
- The belief lands last, and only **after** the observation that earns it - his
  own experience of coming out understanding more. Stated first it is a slogan;
  stated second it is a conclusion. Rule 5.
- *"seems to be"*, not *"is"*. He is describing what he has noticed, not
  announcing a law.
- It is placed straight after *"not ashamed to ask the same question twice"*
  because that sentence is about **receiving** knowledge and this one is about
  **giving** it. The hinge is the phrase "the other way too". Do not move it
  elsewhere in the paragraph; the pairing is the reason it works.

This is also **the qualification for a course-assistant application** - see the
genre table below. The campus letter no longer needs to add a sentence making
that turn, because the constant paragraph now makes it.

#### What this cost, and the open decision

The paragraph went from about 120 words to about 175, and it is constant across
every letter, so **every letter grew by the same 57 words.** The internship
target of "under 400" no longer holds with two technical paragraphs:

| letter | before | after |
|---|---|---|
| google-swe-intern | 347 | 404 |
| mckesson-swe-2027 | 367 | 424 |
| stoke-boltline-2027 | 391 | 448 |
| paypal-swe-2027 | 403 | 428 (after trimming the technical middle) |
| bain-genai-2027 | 441 | 498 |
| campus-ca | 238 | 295 |

**Only PayPal has been trimmed.** The other four internship letters are over and
need their technical middles cut, or the target raised. Every one is still a
single page, which is the rule that actually binds - the word count is a proxy
for it.

**Campus is the real conflict, and it is unresolved.** That genre's target is
150-250 words and a 175-word personal paragraph leaves about 70 for the course,
the teaching argument, the hours and the close. Either the campus letter runs
long, or it gets a shortened personal paragraph - which would be the first time
the paragraph differs between genres. **His call.**

### Three genres, not one letter

An on-campus application is a different genre from an internship application,
not a shorter version of it. Reaching for the internship letter and trimming it
is the common mistake.

| | internship | on-campus CA / grader | professor, RA |
|---|---|---|---|
| draft | `draft-google-swe-intern.py` | `draft-campus-ca.py` | `draft-nyu-gph-research-assistant-fall-2026.py` |
| read by | recruiter, after an ATS | a professor or admin | one professor |
| words | under 400 | 150-250 | one screenful |
| format | PDF attachment | usually an email body - use the `.txt` | email body - use the `.txt`; PDF as a courtesy |
| italic signpost | yes - the portfolio line | **no** - ceremony it cannot afford | no |
| leads with | how he thinks, then the engineering | how he thinks, then the teaching | how he thinks, then the data work, then their paper |
| screened on | projects, stack, scale | did he take the course, can he explain it, hours, pay eligibility | genuine interest in the work |
| must state | availability month | **hours per week and days** | the specific ask, and when |

**What actually differs on campus:** impressive projects are close to
irrelevant. A grader is hired on whether they know the material, can explain it
to someone who does not, and will return marks on time for fifteen weeks. One
line of engineering credibility is enough; the rest should be teaching.

**The personal paragraph does not change between genres** - only what it points
at. Being unashamed to ask a question twice is the same trait in both, but for a
course assistant it is the qualification: someone who still remembers what not
understanding feels like is exactly who you want explaining a problem set. Since
2026-09-05 the paragraph carries the teaching turn itself - sitting with someone
who is stuck rather than handing over the answer - so the campus draft no longer
has to add a sentence to make it. See the note above; the campus length target is
the open question there.

**Availability is a hard requirement, not a pleasantry.** Hours per week and
which days, stated plainly. And the work-authorization line gates everything:
Federal Work-Study roles are closed to F-1 students and make up a large share of
NYU listings. Both are still open in `checklists/intake.md`, so the campus draft
ships with `[N]`, `[DAYS]` and a placeholder in the close **on purpose** - it
cannot be sent until they are answered.

**Name the course.** A grader application that does not name the course reads as
a mass email, because it is one.

### Length

See the table above. Page fill is not checked for letters - a short letter
should be short, and `publish_letter` passes `check_fill=False` for that reason.

### What Claude does not write

The personal paragraph, the opening, and any answer to "why this employer" are
his. The system assembles the technical middle from approved facts in
`profile.yaml` and keeps the close plain. If a draft needs a new claim about
him, ask - do not invent one.

`letters/OPENING-OPTIONS.md` holds the alternatives that were considered and
why the current one was chosen. Read it before rewriting the paragraph.

## On-campus applications

Added 2026-09-06, from a batch of six NYU postings prepared at once. On-campus
work is a different market from the internship search and the manual above
was written for the internship search. What differs:

**The reader is a person, and usually not an engineer.** A professor, a
department administrator, a director of special events. So each preset orders
entries by what that reader screens on, and the `AI & Agents` skills line is
dropped where it would only be noise (a finance-department administrator does
not need to see x402). **Every `ask: true` skill is excluded on every campus
preset.** A campus interview is fifteen minutes and there is no time to
recover from a keyword he cannot defend.

**Work authorization is the gate, and it is still open** in
`checklists/intake.md`. What is known for certain: F-1 students may hold
on-campus jobs without CPT, and the total is capped at **20 hours a week
during term across every on-campus job combined.** Five of the six postings
state "US work authorization required"; on-campus employment satisfies that
for an F-1 student. The cap is the real constraint: a 20-hour job is the whole
allowance, and 15 + 10 is already over it. **He cannot hold all of these, or
even most of them.** The application documents are built for all six so the
choice is his, not the system's - but it has to be made before accepting
anything.

**Never print a school he has not named.** Until 2026-09-07 Courant or Tandon
was unknown. His Fall 2026 schedule (CS-GY course codes, Jacobs Hall at
6 MetroTech) makes it Tandon by inference, recorded in `profile.yaml` under
`education.nyu.school_inferred`, but he has not said the word, so the rendered
education line still carries no school. The general RA pool requires the
school in the letter, so on 2026-09-07 that draft prints "Tandon" on the
strength of the registration and the reply flagged it to him; if he corrects
it, the letter and `education.nyu.school_inferred` change together. No other
document prints a school.

**A posting's stated format beats the standard structure.** The Center for
Faculty Advancement asked for *"Short, 1 paragraph max, cover letter
addressing: What interests you about..."* One paragraph means one paragraph.
The constant personal paragraph is **dropped, not rewritten** - rule 7 says
never rewrite it, and it says nothing about omitting it when the reader has
forbidden it. The "what interests you" half of that paragraph remains his to
write; the draft carries a candidate in his own recorded framing, prefixed
`[HIS WORDS - approve or rewrite:]` so it cannot ship unread.

**An email application ships the `.txt`.** NYU Stern's Finance Department
takes "a resume and brief note of interest" by email. The plain-text letter
in `out/.build/` is the note; the PDF is a courtesy. Suggested subject line is
in the notes file.

**A pool application's letter is the application.** The general Research
Assistant pool is matched on the cover letter alone - school, programme,
subject interests, skills - so that letter states all four plainly, in a way
no internship letter would.

**Placeholders are deliberate and must be resolved before sending.** Every
campus draft may carry `[N]`, `[DAYS]`, `[SCHOOL ...]`, `[HIS WORDS ...]` and
`[WORK AUTHORIZATION LINE ...]`. Before anything is sent:

```powershell
Select-String -Path out/.build/draft-nyu-*.txt -Pattern '\['
```

Nothing should come back.

### The six, and where they live

| posting | preset | letter draft | applies by |
|---|---|---|---|
| CFA, Creative Technologist GA | `nyu-cfa-creative-tech-2026` | `draft-nyu-cfa-creative-technologist-fall-2026.py` | **Sept 14, 2026** |
| BME, Course Assistant BI-GY 810X | `nyu-bme-ca-2026` | `draft-nyu-bme-course-assistant-fall-2026.py` | Oct 1, 2026 |
| Gallatin, Gallery Admin Assistant | `nyu-gallatin-gallery-2026` | `draft-nyu-gallatin-gallery-admin-fall-2026.py` | Oct 2, 2026 |
| GPH, Graduate Research Assistant | `nyu-gph-ra-2026` | `draft-nyu-gph-research-assistant-fall-2026.py` | Oct 4, 2026 |
| Stern Finance, Department Assistant | `nyu-stern-finance-asst-2026` | `draft-nyu-stern-finance-dept-assistant-fall-2026.py` | none stated, email |
| General Research Assistant pool | `nyu-general-ra-2026` | `draft-nyu-general-research-assistant-fall-2026.py` | Dec 31, 2026, rolling |

Each has `jobs/<slug>.md` (the posting) and `jobs/<slug>.notes.md` (knockouts,
who the supervisor is, what leads and why, every gap, every question he must
answer). Read the notes file before touching a preset.

## Adding new information

Two different things get called "adding information about an internship". They
go to different places.

### A. A new internship he has *done* — a fact about him

Goes in `profile/profile.yaml`, never anywhere else. Nothing is stored in chat.

1. **Add a source.** Anything he states directly gets a dated entry under
   `meta.sources`, e.g. `user_2026-09-04`, with `status: verified`. Facts pulled
   from LinkedIn or an old resume stay `self_reported`. The distinction matters:
   verified facts can be defended, self-reported ones inherited a claim.
2. **Add the entry** under `experience:` — id, org, role, dates, location, tags.
3. **Write the facts, then phrasings.** Each `fact` gets one or more `variants`
   with different lengths and flavours. Write two or three; the selector picks.
   All start `approved: false`.
4. **Any number gets a `metrics` entry with provenance.** If he cannot say how
   it was measured, mark it `needs_confirmation` and write the mechanism-only
   phrasing instead. It will be blocked from rendering until he explains it.
5. **Add its skills** to the `skills:` list with `evidence: [<entry id>]`. A
   skill with no evidence never prints.
6. Then:

```powershell
python -m engine.approve --list          # read the new phrasings aloud
python -m engine.approve <variant-id>    # once they sound like him
python -m engine.publish full --draft    # rebuild
python -m engine.export_cv_md            # keep career-ops in step
```

Step 6's last line matters and is easy to forget: career-ops scores postings
against `cv.md`, and a new internship it does not know about is one it cannot
match on.

### B. An internship he wants to *apply to* — a job posting

Goes in `jobs/<company>-<role>.md`. Never edit the profile for a posting.

Then follow **Per-job workflow** above: skill-gap, pick or add a preset,
reorder the skills lines, build, read every gate. The posting is snapshotted
because postings vanish and he will want the original before an interview.

## What survives a new chat

A fresh session starts with no memory of any conversation. What it loads:

| | |
|---|---|
| `CLAUDE.md` | **auto-loaded.** This file. The operating manual. |
| `~/.claude/.../memory/` | auto-loaded. Two short notes: who he is, and the two rules. |
| `profile/profile.yaml` | read on demand — every fact |
| `checklists/intake.md` | read on demand — what is still unanswered |
| `docs/` | read on demand — why Typst lost, the full research |

**Nothing else carries over.** A decision made in conversation and not written
to a file did not happen. So when he confirms something — a metric basis, a
location, a phone number, work authorization — write it into `profile.yaml`
with a dated source **in that session**, or it is lost.

If this file and the code ever disagree, the code is right and this file is
stale. Fix it.

## One folder per application

Every job gets a folder holding exactly two files - the two that get uploaded.

```
applications/
  mckesson-swe-intern-summer-2027/
    resume.pdf
    cover-letter.pdf
  nyu-course-assistant/
    resume.pdf
    cover-letter.pdf
```

```powershell
python -m engine.package <preset> --letter letters/<draft>.py --slug <job-slug>
```

It builds both documents, runs every gate, and places the two PDFs. The folder
is cleared first, so it never accumulates old versions - at the moment of
applying there is no question about which file is the real one.

Nothing else goes in there. Intermediates - HTML exports, extraction baselines,
previews, the plain-text letter - stay in `out/.build/`. The job posting stays
in `jobs/`, with its knockout analysis beside it.

**The `.txt` cover letter still exists** in `out/.build/` and is what to paste
into a portal that wants the letter in a box rather than as an attachment. It is
just not clutter in the application folder.

Slug format: `<employer>-<role>-<term>`, lowercase, hyphenated. Enough to
recognise a year later.

## What is currently blocked

- **Four metrics** await an explanation of how each was measured; mechanism-only
  phrasings ship meanwhile.
- **CovreliefDwarka** is blocked: May–Sep 2020 predates any COVID vaccine, so
  the claim as written is temporally impossible.
- **NeuroPilot, SentinalAI, Lynti** are stubs; their descriptions were truncated
  mid-sentence in the LinkedIn export.
- **No phone** in the header. Most portals require one.
- **The Delhi bullet** - tools and impact, one crisp bullet, waiting on his
  answers. See the rule above. It is the single highest-value recovery for
  every research and course-assistant application.
- **Which on-campus job.** Six are prepared; an F-1 student can hold about one
  of them (20 hours a week, combined). His call, before any offer is accepted.
- **GitHub is fixed.** `github.com/sm11t`, found 2026-09-05 in the portfolio
  repo's own git config and used on the Primer application. It was the
  longest-standing blocker on every SWE preset and it is closed.

`python -m engine.profile` prints the current state of all of this.

## Commands

```powershell
python -m engine.profile                    # what is blocking a shippable document
python -m engine.approve --list             # phrasings awaiting sign-off
python -m engine.publish <preset> --draft   # build, publish, export, verify
python -m engine.ai_lint <file> --max block # lint prose for AI tells
python -m engine.status                     # verdict for every preset
python -m engine.publish_letter letters/<draft>.py   # build a cover letter
python -m engine.package <preset> --letter letters/<d>.py --slug <job>  # package both
python -m engine.export_cv_md               # profile.yaml -> career-ops cv.md
```

Drop `--draft` only after `python -m engine.approve --all`.

## Hard rules

1. Never invent a fact, a number, or a tool.
2. Never rewrite a bullet inline — add a phrasing to `profile.yaml` instead.
3. Never answer a screening question on his behalf.
4. Never ship on an ATS `FAIL` or a voice-lint `block`.
5. One page, always - resume and cover letter both.
6. Report gaps to him rather than filling them.
7. Never rewrite the personal paragraph of a cover letter to suit a job. Only
   the technical middle changes.

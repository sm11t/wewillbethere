# Cover letters: how one gets written

Standalone guidelines for every letter that goes out under Asmit's name.
`CLAUDE.md` keeps the structure and the history of each decision; this file is
the working procedure. When the two disagree, the code is right, then this
file, then `CLAUDE.md`. Written 2026-09-07 for the GPH research-assistant
letter, which was the first one built for a named researcher.

The test every sentence has to pass: **would a reader who has met him believe
he typed this?** A letter fails that test long before it fails a keyword
search, and a reader who decides it was generated stops reading.

---

## 0. Research the reader first

A letter to a person is written after learning who the person is. This step
is mandatory when the posting names a supervisor, a lab, a professor, a
department, or an office, and it happens before a word of the technical middle
is drafted.

### What to look up

| Look for | Where | Why it matters |
|---|---|---|
| The supervisor's current title and labs | their faculty page | Titles move. A "visiting" professor from a 2024 snippet may be tenure-track now. |
| Their last two years of papers: dataset, method, finding | PubMed Central, the journal, the faculty page | The letter anchors on one of these, by content. |
| Who they publish with | author lists | Tells you whose office the posting actually serves. |
| The office or dean the posting sits under, and that person's own work | school leadership page, dean's welcome, news | A "Dean's Office" RA under a biostatistician dean is a biostatistics RA. |
| The seminar calendar for the next month | department events page | A talk he can attend is worth more than a paragraph. Suggest it in the notes; never claim it in the letter. |
| Who the posting contact really is | school HR or staff directory | An HR administrator handles the I-9, not the interview. Address the supervisor. |
| Any tool the group names in a paper's methods | methods sections | Tells you which of his real skills to lead with, and which gaps to report. |

### How to record it

Everything found goes in `jobs/<slug>.notes.md` under **Background**, each
fact with its URL and one of two tags: **verified** (read on the page) or
**not verified** (search snippet, HTTP 403, inference). Inference is labelled
as inference. A fact that could not be fetched is recorded as not fetched, not
silently dropped and not silently kept.

### How much of it goes in the letter

**One anchor.** One paper, one programme, one finding, in one sentence, named
by what it found rather than by its title, and tied to something he has done.
Not two. A letter that cites three of their papers reads as a search result,
and a letter that quotes their mission statement reads as a template with the
school's name pasted in.

**Never:**

- Quote their values, mission, or vision back at them.
- Paraphrase the posting's responsibilities list in the posting's order.
- Praise: "your commitment to", "your groundbreaking work", "your impressive".
- Claim he read, attended, met, or emailed anything he has not. If the letter
  refers to a paper, **he reads the abstract before sending**, and the notes
  file says so as a send-checklist item.

**What the anchor is for.** It is not flattery and it is not proof of
research. It is the seam: the one place where their work and his work touch,
stated plainly enough that the reader can check it in ten seconds.

---

## 1. The structure

```
letterhead              name, contact, rule - identical to the resume
date + recipient        the supervisor by name, the role, the school
personal paragraph      CONSTANT. Who he is. Never a project, employer or credential.
signpost (italic)       internship letters only. Campus and research letters drop it.
technical paragraphs    TAILORED. Two at most. The only part that changes.
close                   availability and eligibility, plainly. Nothing else.
```

No typed signature. The name is already at the top.

The reasons behind each line, and the dates each one changed, are in
`CLAUDE.md` under **Cover letters**. Read `letters/OPENING-OPTIONS.md` before
touching the personal paragraph, and then do not touch it.

---

## 2. Three genres

| | internship | on-campus CA / grader | professor, RA, research office |
|---|---|---|---|
| draft | `draft-google-swe-intern.py` | `draft-campus-ca.py` | `draft-nyu-gph-research-assistant-fall-2026.py` |
| read by | recruiter, after an ATS | a professor or administrator | one researcher, or their dean |
| words | under 400 | 150-250 | one screenful, under 450 |
| format | PDF attachment | email body: ship the `.txt` | email body: ship the `.txt`; PDF as a courtesy |
| signpost | yes, the portfolio line | no | no |
| leads with | how he thinks, then the engineering | how he thinks, then the teaching | how he thinks, then the data work, then their paper |
| screened on | projects, stack, scale | took the course, can explain it, hours | can he do the analysis, can he write it up, does he care |
| must state | availability month | hours per week and days | hours, days, eligibility, and the anchor |
| research step | company and team, briefly | the course and instructor | **section 0 in full** |

A research letter is not a long campus letter and not a short internship
letter. What a researcher screens on is whether the applicant can do the
analysis, write it up for someone who was not in the room, and stay interested
for a semester. The technical middle answers those three, in that order.

---

## 3. The voice

`engine/ai_lint.py` catches the vocabulary ("leverage", "spearheaded", "I am
excited to") and the shape (even bullet lengths, the same opening verb, "not X
but Y", em dashes). The build runs it and blocks on a `block`. What follows is
what the linter cannot see, and it is where most generated letters give
themselves away.

1. **Mirroring.** A generated letter reuses the posting's nouns in the
   posting's order: "literature reviews, data visualization, survey
   development". Use his words for his work. Use their word only where the
   referent is identical (the posting says "RBAC", he did role-based access
   control; print theirs).

2. **Symmetry.** Two technical paragraphs of the same length, every sentence
   fifteen to twenty words, every paragraph ending on a line that sums it up.
   People do not write like that. Let one sentence run because the thought
   did, and let one stop short.

3. **The closing thesis.** No sentence that restates the letter, and no
   sentence that tells the reader what to conclude. The last sentence is
   availability.

4. **Explaining the connection.** "This experience taught me the value of
   clear communication" is the sentence a model writes after every example.
   State the example. The reader draws the line.

5. **Trait words.** Not "detail-oriented", not "curious", not "passionate",
   not "motivated". The linter blocks some; the rule is general. Write the
   consequence a trait would have and let the reader name the trait.

6. **Hedged enthusiasm.** "genuinely", "truly", "really", "deeply",
   "particularly" in front of an adjective. Cut the adverb; if the sentence
   is then false, cut the sentence.

7. **Lists of three.** One per letter at most, and only if the things really
   come in threes. The personal paragraph already spends it.

8. **Numbers.** At most one in the technical middle, taken from the resume,
   exact, never rounded. A number the resume does not carry does not appear
   in the letter.

9. **Openers.** Never "As a", "With my", "I am writing to", "I was excited
   to see". A paragraph opens on the thing itself: the summer at Delhi, the
   workshops, the pipeline.

10. **Reveals.** No colon that sets up a punchline, no "not just X, but Y",
    no rhetorical question, no one-sentence paragraph for effect.

11. **His details.** Every letter carries at least two facts only he would
    know: the admin team's Ctrl+F-and-edit workflow, five named scout
    sources, four freshmen, a professor's name. These are what a reader
    cannot get from a template, and they are already in `profile.yaml`.
    Nothing gets invented to supply one.

12. **His diction.** Short words. No contractions (his recorded voice uses
    none). "I would", not "I'd". "About", not "approximately". "Wrote", not
    "authored". If a sentence sounds like a writer wrote it, it is wrong.

13. **Admissions and gaps.** The personal paragraph carries exactly one
    admission. A gap in the technical middle is reported to him in the notes
    file and is never papered over with a tool he has not used. **He may
    choose to name a gap** (his instruction, 2026-09-07, for Qualtrics on the
    GPH letter). When he does, the shape is fixed: the plain admission in one
    short sentence, then what he found when he looked the tool up, then the
    one true thing he has done that has the same workflow. Never "I am a fast
    learner"; the analogue does that work. One named gap per letter.

14. **Traits he asks for.** When he asks for the letter to say he loves
    learning, solves problems, or figures out the unfamiliar on his own, the
    sentence that goes in is the project where that happened, with the
    detail that proves it (a solo project has nobody to ask; a tool with one
    evidence entry was learned for that project). The reader names the trait.
    The words "love", "passionate", "self-starter" and "quick learner" do
    not appear.

---

## 4. Who writes what

| Part | Written by | Rule |
|---|---|---|
| personal paragraph | him, once | byte-identical across every letter of a genre; the build's notes assert it |
| technical middle | assembled from `profile.yaml` | every claim traces to a fact; every tool has evidence |
| the anchor sentence | drafted from section 0 | prefixed `[HIS WORDS - approve or rewrite: ...]` so it cannot ship unread |
| "why this" | him | same prefix; a candidate may be offered in his recorded framing |
| hours and days | him | `[N]`, `[DAYS]` until answered in `checklists/intake.md` |
| eligibility line | `profile.yaml`, `basics.work_authorization` | placeholder until a dated `user_YYYY-MM-DD` source backs it |

A bracketed placeholder is not a defect. It is the mechanism that stops a
sentence he has not read from going out under his name.

---

## 5. Before it is sent

Run, in order, and every line has to come back clean:

```powershell
python -m engine.package <preset> --letter letters/<draft>.py --slug <slug>
Select-String -Path out/.build/<draft>.txt -Pattern '\['        # nothing
python -c "import re; raw=open('applications/<slug>/cover-letter.pdf','rb').read(); print(sorted(set(re.findall(rb'/URI\s*\(([^)]*)\)', raw))))"   # three
```

Then by hand:

- [ ] Lint: 0 block. Every warn read and either fixed or written down in the
      notes with why it stays.
- [ ] One page.
- [ ] Three link annotations: portfolio, LinkedIn, GitHub.
- [ ] The personal paragraph is byte-identical to the genre baseline.
- [ ] Any paper or programme the letter names: he has read the abstract.
- [ ] Word count inside the genre's range, or the overage recorded in the notes.
- [ ] The recipient is the person who would interview him, not the HR contact.
- [ ] Read aloud once. Any sentence that would embarrass him in an interview
      is cut.

---

## 6. Standing content for internship letters (his instruction, 2026-09-07)

Every internship letter carries three things, in this order, inside the
technical middle:

1. **WatchDNA's business impact.** The in-house store locator and admin
   console replaced an expensive third-party app the company had been paying
   for, and traffic was up within six months of going live (`wd.impact`). No
   figure until he gives one with its mechanism.
2. **MyYogaTeacher's time saved.** The voice-to-SQL pipeline replaced the
   admin team's Ctrl+F-and-edit workflow and gave them back the time it took
   (`myt.voicesql.time`). The 60% figure stays blocked.
3. **The always-building hinge**, one sentence before the personal projects:
   he is always building something, usually to try a technology he has not
   used yet, and the projects that follow are the method. Never as a bare
   trait; the projects are what make it true.

Campus and research letters carry 1 and 2 where the internship is mentioned
at all, and 3 where a project follows.

## 7. File conventions

- One draft per posting: `letters/draft-<employer>-<role>-<term>.py`.
- The docstring explains what was chosen and why, in enough detail that the
  next session does not have to re-derive it.
- Comments mark each block `CONSTANT`, `TAILORED`, or `HARD REQUIREMENT`.
- Gaps, the research, the questions for him, and the measured build result go
  in `jobs/<slug>.notes.md`, never in the draft.
- The `.txt` in `out/.build/` is the paste-box version and the one to send
  when the application is an email.

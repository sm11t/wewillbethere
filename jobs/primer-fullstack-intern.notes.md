# Primer — Full Stack SWE Intern (PrimerOS)

**Resume only. No cover letter**, on Asmit's instruction of 2026-09-05 — which
makes the resume the entire application and changes how it is built. See
"The mission requirement" below.

## The gate is the commitment, not the stack

> *The internship begins in January, May, or June, with a **preferred
> commitment of 4 to 8 months.***

**No summer satisfies this.** June to August is three. To reach four months he
would have to start in May and run into September, colliding with the start of
NYU's autumn term; eight months means a semester off or part-time enrolment.

It says *preferred*, not required, so a three-month summer is not an automatic
no — but this is a startup asking for a long intern precisely because a short
one costs them more than it returns. **He should decide what he can actually
commit to before applying, and say so in the application rather than leaving
them to discover it at offer stage.** A January start with a spring semester
off is the shape that fits the posting best; only he can say whether that is on
the table.

Everything else that would normally be a knockout is simply absent from the
posting: no graduation-date window, no degree requirement, no work
authorization line, **and no location** — the paste does not say whether this
is onsite, and Primer runs physical schools. Check the live posting.

## Their stack, against the fact base

| Primer names | Him |
|---|---|
| **TypeScript** | Torii, WatchDNA, Lead Engine — his most-evidenced language, and their first word |
| **Node** | WatchDNA |
| **Postgres** | WatchDNA |
| **React** | Lead Engine, Portfolio, Flickmatch |
| GraphQL | `resume_2026` self-claim, **no project behind it** |
| **Prisma** | not used — **do not add** |
| **Next** | not used — **do not add** |
| **Relay** | not used — **do not add** |

**Four of eight outright, and they are the four that matter** — the language,
the runtime, the database and the view layer. The other four are an ORM, a
React framework and a GraphQL client sitting on top of exactly that backbone.
Each is a week's learning and none is worth a false claim; identical call to
Next.js and Apollo on the Stoke preset.

**GraphQL is the one to decide.** It renders because it is his own claim from
his own resume, but this posting uses GraphQL *daily* alongside Relay and
Prisma. That is the environment where a self-claim with nothing behind it gets
found in week one. Confirm it or cut it.

"We invest heavily in our DevEx and **agent stack**" is the line that makes
Torii relevant, and Torii leads Projects.

## The mission requirement, and why the preset is shaped this way

Their **first** stated requirement is not technical:

> *You have a real passion for fixing the US education system.*

Normally that is argued in a cover letter. There is no cover letter here, so
the resume has to carry it — and the only education credential he has is the
**AI Society** entry: Technical Officer, wrote the teaching materials, ran the
workshops that made ML approachable to students with no technical background,
mentored four freshmen through a first ML project.

So **AI Society sits second, directly under WatchDNA.** At position four,
between MyYogaTeacher and Delhi, it reads as a club line nobody was meant to
stop on. At position two it reads as what it is. WatchDNA still leads because
their "what you'll do" section is entirely stack, and that entry answers most
of it in one place.

**Portfolio is promoted above Pash** for the same reason: *"You take pride in
your craft. Every detail matters"* is a stated requirement, and a hand-modelled
room rendered in the browser is a craft argument no bullet can make in words.

## Gaps

- **"Contribute to a culture of excellence through code reviews."** Code review
  is still the open question from the PayPal pass — he may have been the only
  engineer at both companies. Unanswered in `checklists/recover.md`.
- **Prisma, Next, Relay** — real, and correctly left off.
- **K–12 or classroom software** — he has none. The AI Society work is
  teaching, not edtech, and nothing on the page pretends otherwise.

## Built

`applications/primer-fullstack-intern/` — `resume.pdf` only, preset
`primer-fullstack`. ATS PASS, one page, 94% fill.

This is the first resume-only application. `engine/package.py` had `--letter`
as a required argument; it is now optional, because a folder that holds exactly
what gets uploaded should not hold a letter the employer did not ask for.

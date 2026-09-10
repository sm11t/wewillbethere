# NYU Stern Finance Department - Department Assistant, Fall 2026

Applied by **email**, not through Handshake: a resume and a brief note of
interest to Christina Borovilas at cb3972@stern.nyu.edu. Half the job is a
reception desk; the other half is keeping the department website current.
"HTML experience is required" is the only hard technical line.

## Knockout check

| Gate | Status |
|---|---|
| US work authorization required | **UNKNOWN - the open gate.** The posting states it outright, and intake.md Tier 1 is still unanswered. If he is F-1: on-campus work needs no CPT and no OGS authorization ("you do NOT need to obtain specific authorization from the OGS"), but it is capped at 20 hours a week while classes are in session - a per-week ceiling under 8 CFR 214.2(f)(9)(i), across every on-campus job combined. He also needs a Social Security Number before he can be paid; OGS issues the letter for that once he has an offer, and there is no waiting period to accept. |
| Work-Study eligible | **Usable, not required.** NYU's own employer boilerplate: *"Federal Work-Study is not required for this role, unless specifically stated within the job description."* This description does not state it. Checking the Work-Study box on Handshake "will still allow non FWS students to apply". F-1 students cannot hold FWS, so if he is F-1 this posting is open to him anyway. |
| Onsite, in person, New York | **PASS** - he is in New York. The department's staff sit on the 9th floor (her room is 9-190 per the staff directory). |
| Hours per week | **NOT STATED.** The posting says "part-time" and nothing else. A question for him (how many he wants, see intake.md item 13) and for them (how many they need, which days the desk has to be covered). |
| September 21 - December 22, 2026 | **PASS** assuming he is enrolled for the fall. |
| Deadline | **None stated**, and they say they "typically receive a high volume of applications" and may only contact the shortlisted. Apply early; a note that arrives in the first week is read, one that arrives in week four may not be. |
| Pay $18-30/hr | The $30 ceiling matches the GSOC graduate hourly minimum for 2025-26 ("no less than $28.25 per hour as of September 1, 2023, with yearly increases reaching $30 per hour by 2025-26"). Whether a clerical Department Assistant post is a GSOC-covered position at all is not stated anywhere; the range most likely spans undergraduates at the bottom and graduate students at the top. Ask. The parent memo attributed the $30 to Local 7902; the figure is from the GSOC contract, which NYU HR files as Local 2110 and actuaw.org (Local 7902) hosts under its own site - the local is immaterial to him, the number is not. That 2020-2026 contract runs out on August 31, 2026 and no successor is visible. |

## Background

- **Christina Borovilas** is listed under *Professional Staff* on the Finance
  Department's staff directory, room 9-190, (212) 998-0303,
  cborovil@stern.nyu.edu. No functional title is published for any of the
  seven professional staff.
  https://www.stern.nyu.edu/experience-stern/about/departments-centers-initiatives/academic-departments/finance/faculty-staff/staff
- Her name also comes up on Stern Fellows teaching-fellow postings for Finance
  courses (e.g. Foundations of Finance with Prof. Navin Chopra), which is
  consistent with her coordinating course staffing for the department. That
  is from a search snippet; the posting itself is login-gated.
  https://w3.stern.nyu.edu/fellows/position_details/11958
- **Two addresses.** The posting says cb3972@stern.nyu.edu; the directory says
  cborovil@stern.nyu.edu. Send to the one in the posting - it is the
  instruction - and do not cc the other.
- The **department**: chair Matthew P. Richardson (Charles E. Simon Professor
  of Applied Economics), "over 40 full-time faculty". The departmental
  administrators named in Stern's faculty guide are Michael Jules and Anita
  Lall - the people likely running the office day to day.
  https://www.stern.nyu.edu/experience-stern/about/departments-centers-initiatives/academic-departments/finance
  https://www.stern.nyu.edu/portal-partners/faculty-guide-depricated/overview/academic-department-and-center-contacts
- **The website he would maintain** is the department's section of
  stern.nyu.edu: the page above plus Working Papers, MBA and undergraduate
  course descriptions, PhD students on the job market, the faculty and staff
  directories, and Position Openings. That is the content that changes every
  semester.
- **It runs on Drupal 10.** The page source carries
  `<meta name="Generator" content="Drupal 10 (https://www.drupal.org)">`, with
  `/sites/default/files/` and `itok` image-style URLs throughout. Some pages
  inside it are legacy hand-built HTML - the staff directory is a plain HTML
  table with `old_web` image references.
- The posting is **not** on the department's own Position Openings page (that
  lists only a tenure-track search), so the email is the only channel.
  https://www.stern.nyu.edu/experience-stern/about/departments-centers-initiatives/academic-departments/finance/faculty-staff/position-openings
- **Work-study and hours**, NYU's own words. Wasserman for supervisors:
  "Federal Work-Study is not required for this role, unless specifically
  stated within the job description."
  https://wasserman.nyu.edu/on-campus-employment-supervisors/
  Wasserman FAQ: "When classes are in session, students may work up to 20
  hours per week." https://wasserman.nyu.edu/on-campus-employment-faqs/
  OGS: "You can work a maximum of 20 hrs/week during Fall or Spring
  semesters"; no OGS authorization needed for F-1 on-campus work.
  https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration/current-students/employment-and-tax/on-campus-employment.html
- **Pay**: GSOC's contract summary for the $30 graduate hourly figure.
  https://makingabetternyu.org/understand-it/

**What it implies for the note of interest.** "Updating and maintaining
content" on a Drupal 10 site means editing pages through an admin interface -
a rich-text editor with an HTML source view - rather than hand-editing files,
so the HTML requirement is about being able to fix what the editor produces
and maintain the legacy table pages, not about building pages from scratch.
The note should say what he has built in HTML and React and stop there: no
Drupal claim (none in the profile), and no pretence that a website revamp is
the same thing as a reception desk.

## What leads on the resume, and why

Preset `nyu-stern-finance-asst-2026` in `profile/variants.yaml` - already
written, and this is the selection.

- **Flickmatch leads**, out of date order and on purpose. Revamping a whole
  website from Figma designs into responsive React and Material-UI
  components is the HTML-and-web-content credential, and it is the only
  entry whose subject is a website. Oldest role, weakest everywhere else,
  first here.
- **WatchDNA second** for the admin console: data operations on a live
  store locator is content operations on a live site, which is the web half
  of this job in a different costume.
- **AI Society third.** "Strong organizational and communication skills" -
  writing the materials and running workshops for students with no technical
  background is the only evidence of either on the profile.
- **MyYogaTeacher fourth.** The voice-to-SQL bullet is about an admin team's
  workflow, which is the one bullet on the page that talks about office work
  at all. Delhi is off; a Gaussian Process classifier says nothing to a
  department office.
- **Projects: Portfolio, Lead Engine, Pash.** Portfolio first - a site he
  built and keeps up himself, in HTML/CSS, React and Three.js. Lead Engine
  for the React dashboard. **Torii is off**: x402 payment flows are noise
  to an office administrator.
- **No AI & Agents skills line.** The reader screens for HTML and
  organisation; a line of agent-protocol vocabulary reads as a different
  applicant. `HTML/CSS` leads Languages; React, Figma, Material-UI lead
  Frontend.
- **Every `ask: true` skill is off.** Fifteen-minute campus interview, no
  room to recover from a keyword he cannot defend.

### Disagreement

None that would change the selection. Two observations for the record:

- Pash (audio stem separation on remote CUDA workers) and Lead Engine's five
  scout agents across Zillow and Redfin are the two things on the page an
  office administrator is least likely to follow. They stay because cutting
  them leaves the page short and the alternative, Torii, is worse. If the
  page comes out under fill, Pash is the one to drop, not a role.
- Nothing on the page speaks to the reception desk, and nothing can - the
  profile has no customer-facing or administrative entry. That is the
  letter's problem, and the letter does not solve it either; it says what he
  has built and leaves the desk half to the interview. See Questions.

## Requirement mapping

| Their line | Status | Him |
|---|---|---|
| **HTML experience is required** | **existing** | `HTML/CSS` evidenced against `portfolio` and `flickmatch`. Flickmatch: the whole site from Figma to responsive React and Material-UI. Portfolio: asmit.space, built and kept up by him. Both are on the page and in the letter. |
| Updating and maintaining website content | **supported** | Nearest evidence is the Flickmatch revamp and the WatchDNA admin console (data operations on a live site). Neither is "edit a page in a CMS". See CMS below. |
| Strong organizational skills | **supported, thinly** | Only the AI Society: writing materials and running workshops takes organising. No bullet says "organised" anything. |
| Strong communication skills | **supported** | AI Society: workshops for students with no technical background; mentoring four freshmen. The letter's constant paragraph is itself the communication sample. |
| Reception desk - greeting visitors, answering basic questions | **GAP** | Nothing on the profile. No customer-facing, front-desk or office role anywhere. Do not paper over it. |
| Administrative tasks - copying, organising materials | **GAP** | Nothing on the profile. Same. |
| CMS experience (unstated, but the site is Drupal 10) | **UNKNOWN** | Not asked for, not in the profile. What did the Flickmatch site run on - a React app he wrote, or a CMS theme? Has he ever edited content in any CMS (WordPress, Drupal, Squarespace, a school portal)? If yes, that is a recoverable fact and a bullet; if no, say nothing. |

**Not to be added, whatever the posting implies:** Drupal, any CMS name,
Microsoft Office, Google Workspace, "customer service". None is in the
profile.

## Letter notes

- **Genre: an email note of interest.** The `.txt` that `publish_letter`
  writes is what ships - pasted into the email body under a one-line
  greeting. The PDF on the letterhead is a courtesy attachment alongside the
  resume, not the primary artifact.
- **Suggested subject line:** `Department Assistant - Finance Department - Asmit Datta`
- No signpost, either one. Campus genre; an email cannot afford the ceremony.
- **Personal paragraph is the campus constant**, copied verbatim from
  `letters/draft-campus-ca.py`. Not edited.
- **One technical paragraph**, every claim from profile.yaml: identity
  (first-year M.S. CS at NYU), Flickmatch (`fm.ui.full`), the portfolio
  (`portfolio` stack), the WatchDNA admin console (`wd.locator.full`), the AI
  Society workshops (`ais.workshops.t`). No CMS claim, no reception claim.
  - **One paraphrase to confirm with him:** the letter says the admin console
    is what "the store locator's data is updated through". The profile says
    "an admin console for data operations". Updating data is a data
    operation, so this is entailed rather than added - but it is his
    sentence to approve.
- **Close** carries three placeholders on purpose - `[N]` hours, `[DAYS]`,
  and the work-authorization line - and must not be sent with any of them in.
- **Word count (whitespace split, 2026-09-06):** body 308 - personal 172,
  technical 99, close 37 (with the placeholders still in). 319 including the
  two recipient lines in the `.txt`.
- **Lint:** `python -m engine.ai_lint nyu-stern.txt --max block` on the
  rendered `plain_text` - **0 block, 0 warn, 0 note**, first pass. The
  personal paragraph was checked byte-for-byte against `draft-campus-ca.py`
  and is identical. Zero em dashes anywhere in the draft.
- The constant paragraph is 172 words on its own (CLAUDE.md's "about 175"),
  and CLAUDE.md leaves the campus-length conflict (150-250 target against a
  175-word constant) as his call. This note runs over the campus target for
  exactly that reason: the tailored part is 99 words, and every word over
  the target is the constant, not the tailoring. If he wants it under 250,
  the constant has to shrink for the campus genre, which would be the first
  time the paragraph differs between genres.

## Questions for Asmit

1. **Hours.** The posting is silent. How many a week do you want on campus
   this term (cap is 20 if F-1, across every on-campus job)? That number goes
   into `[N]`.
2. **Days.** Which days can you be at a desk on the 9th floor? Goes into
   `[DAYS]`. They will want the desk covered on fixed days.
3. **Work authorization.** Citizen, permanent resident, or F-1? The posting
   requires US work authorization; intake.md Tier 1 is still open. The
   close cannot be finished without it.
4. **CMS.** What did the Flickmatch site actually run on? Was the revamp a
   React app you wrote, or a theme inside a CMS? And have you ever edited
   content in any CMS at all - WordPress, Drupal, Squarespace, a school
   portal? The Stern site is Drupal 10; a yes here is a recoverable fact.
5. **The desk.** Half of this job is a reception desk - greeting visitors,
   answering basic questions, copying and organising. Are you fine with
   that? Nothing on your profile speaks to it, and the interview will ask.
6. **Do you want this one at all?** With an F-1 20-hour cap this is a
   sizeable slice of the term's allowance, and there are five other campus
   postings in the batch. Is a partly clerical role at $18-30 where you want
   to spend it, against a research assistantship or a course assistant post?
7. **Which address to send from**, and whether to attach the letterhead PDF
   as well as the resume or keep the email to one attachment.

Built 2026-09-06 by the first session and re-measured by the second.
`applications/nyu-stern-finance-dept-assistant-fall-2026/` - preset
`nyu-stern-finance-asst-2026`, letter
`letters/draft-nyu-stern-finance-dept-assistant-fall-2026.py`. Rebuilt 2026-09-07 after the workshops phrasing changed. Resume ATS PASS,
one page, 89% fill, five link annotations (Torii is off this preset).
Letter one page, 319 words, zero lint findings, three link annotations. This
one goes by email, so the artifact that ships is
`out/.build/draft-nyu-stern-finance-dept-assistant-fall-2026.txt`; the PDF is
a courtesy. No `ask: true` skill renders. Draft build. Still in the letter:
`[N]`, `[DAYS]`, the work-authorization line.

"""Cover letter - NYU Gallatin, Graduate Gallery Admin Assistant, Fall 2026.

Campus genre, but the letter carries this application or nothing does: the
posting is logistics (liaison, Asana, deliveries, insurance, payments,
staffing openings) and the profile is engineering. Rewritten 2026-09-07 under
letters/GUIDELINES.md and his preferences stated that day (portfolio
signpost in; no bracketed markers; a gap named plainly with a true analogue;
learning the unfamiliar shown, not claimed).

Reader: Rachel Plutzer, Senior Director for Events and Special Programs at
Gallatin since 1997, MPA from Wagner; an events professional, not an
engineer. Research with URLs in jobs/nyu-gallatin-gallery-admin-fall-2026.notes.md.

Structure: constant personal paragraph (byte-identical to draft-campus-ca.py),
the italic portfolio signpost, two technical paragraphs, a close with hours,
days, eligibility and the offer to come by.

Paragraph 1 - why, and the arts. The first sentence is the "why galleries"
sentence, drafted in his framing and shown to him in full in the reply that
shipped this draft; his to approve. Then pf.room.short, pash.arch (music),
and the one anchor from research: the season he would actually work - the
run-out of The Best of All Possible Worlds (to Oct 17) and the whole of Stacy
Kranitz's show (Oct 30 - Dec 15), install to de-install. Dates from the
galleries' homepage, verified 2026-09-06.

Paragraph 2 - the organising evidence at its recorded size, with the
admission that it is smaller than a gallery season (his earlier draft carried
this line; kept). ais.workshops.ran + ais.mentoring; myt.design (his words
of 2026-09-07); wd.locator + wd.alerts (his words). Then the named gap:
Asana, looked up, tied to Lead Engine's dashboard (le.dashboard.obs) as the
true analogue for tracking where work is - GUIDELINES.md voice rule 13.

Close: twenty hours; days from basics.availability_fall_2026 (classes Tue
and Wed evenings, Fri late morning - so most weekday gallery hours, and
Monday and Thursday evenings for openings); the F-1 line
(basics.work_authorization; the posting says open to OPT/CPT, and on-campus
work needs neither); the offer to come by.

Not claimed: Asana experience, shipping, insurance, payments, gallery work,
event staffing beyond the workshops, video or 3D-design work, CovreliefDwarka
(blocked), any visit to the current show. The twenty hours are the entire
F-1 on-campus allowance - flagged to him, not resolved here.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    "recipient": ["Graduate Gallery Admin Assistant, Gallatin Galleries",
                  "Rachel Plutzer, NYU Gallatin School of Individualized Study"],

    "signpost_1": None,

    # CONSTANT. Copied verbatim from letters/draft-campus-ca.py. Do not edit.
    "personal": (
        "First, I would like to talk about how I approach problems, how I get "
        "better at them, and how I work in a team. I accept it when I fall "
        "short of understanding something, and I give my best to understand it "
        "from people better than me. I have a lot of respect for anyone I can "
        "learn from, and I am not ashamed to ask the same question twice if "
        "that is what it takes. It works the other way too. When someone is "
        "stuck on something I have already worked out, I will sit with them "
        "rather than hand over the answer, and I come out of those "
        "understanding it better than when I went in. Knowledge seems to be "
        "one of the few things that grows when you share it. I think about "
        "problems in systems, and I "
        "approach them that way. I think that is also what makes me useful "
        "explaining something to someone else - I still remember what it is "
        "like to not understand it yet."
    ),

    # Standard wording (CLAUDE.md, 2026-09-05). His preference, 2026-09-07.
    "signpost_2": (
        "I would encourage you to visit my portfolio at www.asmit.space."
    ),

    # TAILORED. First sentence is his to approve; the rest traces to
    # profile.yaml, his words of 2026-09-07, or the notes file.
    "technical": [
        "I build things for the screen, and the reason this posting stopped "
        "me is that it is about a room. My portfolio is my own room, modeled "
        "in Blender and put in the browser with Three.js - you walk up to the "
        "desk, click the machine, and every project opens as its own artifact "
        "instead of a list of links. Pash splits songs into vocals, drums, "
        "bass and instrumentals. The season I would be working is the run-out "
        "of The Best of All Possible Worlds and the whole of Stacy Kranitz's "
        "show, from October 30 to December 15, install to de-install. That is "
        "the part I want: the dates, the deliveries, the list of works, and "
        "the people who each own a piece of it.",

        "What I can point to is smaller than a gallery season, and I would "
        "rather say so. At the AI Society at Arizona State I wrote the "
        "materials for and ran workshops and study sessions for students of "
        "all majors. I also mentored four freshmen through their first "
        "machine learning project, which meant people and dates and a room "
        "to keep in order. At "
        "MyYogaTeacher I was given the initial design of a new feature and "
        "turned the idea into diagrams, wireframes and user journeys for the "
        "development team, then built against my own drawings. At WatchDNA I "
        "built the admin console for data operations and a store locator, "
        "and hooked up alerts so anything that broke was seen and fixed right "
        "away. I have not used Asana. I looked it up before writing this. A "
        "board of tasks with owners and dates is close to how I already "
        "keep track of work - Lead Engine's dashboard shows every scout and "
        "every call while it runs, so nothing goes missing quietly.",
    ],

    # HARD REQUIREMENT. Days and eligibility verified user_2026-09-07.
    "close": (
        "I can commit the twenty hours a week the posting describes. My "
        "classes are on Tuesday and Wednesday evenings and Friday late "
        "morning, so I am free on-site most weekdays during gallery hours and "
        "on Monday and Thursday evenings for openings. I am on an F-1 visa, "
        "which permits on-campus employment without further authorization. I "
        "would be glad to come by the galleries to talk about what the season "
        "needs."
    ),

    "signoff": None,
}

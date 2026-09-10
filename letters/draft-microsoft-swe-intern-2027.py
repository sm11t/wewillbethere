"""Cover letter - Microsoft, Software Engineering Intern, Full-Stack Product
(University). Term and location not stated in the posting; Summer 2027
assumed.

Internship genre (letters/GUIDELINES.md, section 2): ATS, recruiter, then
interview loops. PDF attachment; the italic portfolio signpost stays. The
personal paragraph is the internship one, copied verbatim from
draft-google-swe-intern.py. Written 2026-09-07.

No anchor. The posting is a company-wide template with no team, product or
paper to touch; a Microsoft product name dropped in for effect would be
exactly the kind of sentence GUIDELINES.md section 0 warns against. The
research step was the posting itself and the requirement line.

The posting's own definition of the job - "end-to-end product experiences
across user interfaces, APIs, and backend services" - is WatchDNA in one
entry, so paragraph 1 walks that internship in that order: the Mapbox UI
and admin console, the REST and JWT backend, the companion app on the same
auth and data layers; then the impact (wd.impact, his words, no numbers).
Then MyYogaTeacher: the feature designed from an idea and built
(myt.design), the offline-first client, the voice-to-SQL workflow and the
time it gave back (myt.voicesql.time). Flickmatch closes the paragraph for
"responsive user interfaces" (fm.ui.full).

Paragraph 2: the always-building hinge (GUIDELINES.md section 6), Lead
Engine as a full-stack project (FastAPI and a React dashboard) with the
observability line the posting asks about - a failed scout shows up the
moment it fails, and alerts on everything he ships (wd.alerts, his words);
Torii in one sentence; the AI-practice sentence in his framing.

Standing content present: WatchDNA impact, MyYogaTeacher time saved, the
hinge. "Graduating in 2028" states the requirement (a semester remaining
after Summer 2027) in his profile's word.

Not claimed: C#, Angular, any testing framework by name, accessibility work
(Accessibility is on the resume on coursework evidence only), any Microsoft
product knowledge. "Growth mindset" and the mission line are not echoed.

Close: New York, full time from June 2027.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    "recipient": ["Software Engineering Intern, Full-Stack Product",
                  "Microsoft"],

    "signpost_1": None,

    # CONSTANT. Copied verbatim from draft-google-swe-intern.py. Do not edit.
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
        "problems in systems, and I approach them that way. I also ask the "
        "questions that are uncomfortable - I have seen them frustrate people, "
        "but they are usually the ones that need asking. I know I have a lot "
        "left to learn."
    ),

    # Standard wording (CLAUDE.md, 2026-09-05).
    "signpost_2": (
        "I would encourage you to visit my portfolio at www.asmit.space."
    ),

    # TAILORED. Every claim traces to profile.yaml or his words of 2026-09-07.
    "technical": [
        "I am a first-year M.S. Computer Science student at NYU, graduating "
        "in 2028, after a B.S. at Arizona State and three engineering "
        "internships. WatchDNA was the whole stack. I built the store "
        "locator, an interactive Mapbox map with real-time filtering, and "
        "the admin console behind it. I set up the backend from scratch on "
        "Node.js - the schema, the REST endpoints, JWT authentication with "
        "role-based access, the security middleware. When the companion app "
        "came, I built it in React Native on the same auth and data layers "
        "and took it through iOS App Store review. Those tools replaced an "
        "expensive third-party app the company had been paying for, and "
        "within six months of going live the traffic was up. At "
        "MyYogaTeacher I was given the initial design of a new feature, "
        "turned the idea into diagrams, wireframes and user journeys for the "
        "development team, and then built against my own drawings. I wrote "
        "the React Native client that streams biometric data in real time, "
        "with offline-first sync and time-series deduplication so nothing is "
        "lost when the network drops. The voice-to-SQL pipeline I shipped on "
        "Whisper replaced the admin team's Ctrl+F-and-edit workflow and gave "
        "them back the hours that took. Before that, at Flickmatch, I "
        "revamped the website end to end, turning new Figma designs into "
        "responsive React and Material-UI components across every page.",

        "Outside work I am always building something, usually to try a "
        "technology I have not used yet. Lead Engine is the most recent: a "
        "FastAPI backend with a React dashboard over it. Five scout agents "
        "run in parallel across Zillow, Redfin, FSBO, expired listings and "
        "the Maricopa County Assessor, and every lead is scored with the "
        "reasoning written out beside the score - 2,129 leads sourced. The "
        "dashboard is a live pipeline graph, so a failed scout shows up the "
        "moment it fails, and on everything I have shipped I hook up alerts "
        "for when something goes wrong, so it gets debugged and fixed right "
        "away. Torii is a proxy between an AI agent and every paid tool it "
        "calls, with a budget reserved before each call and a ledger of "
        "every call and every reason one was blocked. Most of my own work "
        "now runs through coding agents, and the part I have got good at is "
        "the harness around them rather than the prompt.",
    ],

    "close": (
        "I am in New York and available full time from June 2027."
    ),

    "signoff": None,
}

"""Cover letter - TJX Companies, IT Engineer Intern, Global IT (Summer).
Term, location and deadline not stated in the posting; Summer 2027 assumed.

Internship genre (letters/GUIDELINES.md, section 2). PDF attachment; the
italic portfolio signpost stays. The personal paragraph is the internship
one, copied verbatim from draft-google-swe-intern.py. Written 2026-09-07.

The posting's Key Qualifications are "current juniors" pursuing a bachelor's
degree. He is a first-year M.S. student. Built on his instruction with that
recorded in the notes file; the letter states his degree plainly in the
first sentence and does not argue the point. The class-year question on the
form is his to answer.

No anchor. The posting is a company-wide template - five pathways, no team,
product or named person - and a TJX brand dropped in for effect is the
sentence GUIDELINES.md section 0 exists to prevent.

Paragraph 1 follows the pathways the posting lists. Software development
and security: WatchDNA (wd.infra.stack - JWT, role-based access, security
middleware; wd.locator; wd.companion) and its impact (wd.impact, his words,
no numbers). Requirements to build, and automation: MyYogaTeacher
(myt.design; myt.voicesql.mech; myt.voicesql.time). Teams and leadership:
the AI Society as Technical Officer (ais.workshops.ran, ais.mentoring) - the
only leadership title on the profile, and the posting asks for "leadership
abilities" and a group project with other interns.

Paragraph 2: the always-building hinge (GUIDELINES.md section 6); Lead
Engine for data and automation (le.pipeline.sources, le.dashboard.obs, and
alerts - wd.alerts, his words); Torii for the security pathway in one
sentence (identity, policy, budget on every request); the AI-practice
sentence in his framing.

Not claimed: retail or TJX knowledge, any product-configuration platform,
"Agile Mindset" or any of the posting's adjectives, any testing framework by
name. Agile and Jira are on the resume on coursework evidence; the letter
does not mention them.

Close: New York, full time from June 2027. Location is not in the posting;
TJX's home offices are in Massachusetts.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    "recipient": ["IT Engineer Intern, Global IT",
                  "The TJX Companies"],

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
        "I am a first-year M.S. Computer Science student at NYU, after a B.S. "
        "in Computer Science at Arizona State and three engineering "
        "internships. At WatchDNA I set up the backend from scratch on "
        "Node.js - the schema, the REST endpoints, JWT authentication with "
        "role-based access, the security middleware - and built the store "
        "locator and the admin console over it. The companion React Native "
        "app I shipped reused the same auth and data layers. Those tools "
        "replaced an expensive third-party app the company had been paying "
        "for, and within six months of going live the traffic was up. At "
        "MyYogaTeacher I was given the initial design of a new feature, "
        "turned the idea into diagrams, wireframes and user journeys for the "
        "development team, and then built against my own drawings. The "
        "voice-to-SQL pipeline I shipped on Whisper replaced the admin "
        "team's Ctrl+F-and-edit workflow and gave them back the hours that "
        "took. At the AI Society at Arizona State I was Technical Officer: I "
        "ran the workshops and study sessions, wrote the materials for them, "
        "and mentored four freshmen through their first machine learning "
        "project.",

        "Outside work I am always building something, usually to try a "
        "technology I have not used yet. Lead Engine keeps five scout agents "
        "running in parallel across Zillow, Redfin, FSBO, expired listings "
        "and the Maricopa County Assessor, deduplicates what they find by "
        "address, and scores every lead with the reasoning written out "
        "beside the score - 2,129 leads sourced. The dashboard over it is a "
        "live pipeline graph, so a failed scout shows up the moment it "
        "fails, and on everything I have shipped I hook up alerts for when "
        "something goes wrong, so it gets debugged and fixed right away. "
        "Torii is a proxy between an AI agent and every paid tool it calls, "
        "enforcing identity, policy and budget on every request, with a "
        "ledger of every call and every reason one was blocked. Most of my "
        "own work now runs through coding agents, and the part I have got "
        "good at is the harness around them rather than the prompt.",
    ],

    "close": (
        "I am in New York and available full time from June 2027."
    ),

    "signoff": None,
}

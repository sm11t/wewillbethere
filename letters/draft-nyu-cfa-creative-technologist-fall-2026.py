"""Cover letter - NYU Center for Faculty Advancement, Creative Technologist GA.

Fourth version, 2026-09-07, on his instruction: the one-paragraph version
"sounds a little robotic"; change only a few things; add his line about
giving examples after reading the requirements; remove the Tulsa showcase;
bring back the constant paragraph about how he works and works in a team;
and encourage them to visit the portfolio.

So this letter now follows the STANDARD structure rather than the
one-paragraph override the posting asks for ("Short, 1 paragraph max"):

    personal paragraph      CONSTANT - byte-identical to draft-campus-ca.py
    signpost (italic)       the portfolio line, standard wording
    technical paragraph     his examples, one paragraph, availability last

That is two paragraphs plus the italic line against a posting that asked for
one. His call, made knowingly; recorded in the notes file. No close and no
signoff - availability stays inside the technical paragraph so nothing else
is added.

What changed in the technical paragraph, and only this:
  - Opens with his sentence: after reading the requirements, a few examples
    of work that show readiness for the role. Then his framing of the job
    as idea to workflow to journey, now without the colon.
  - The two Tulsa sentences are gone. The research stays in the notes file.
  - Three colon-hinges softened into plain sentences ("My portfolio works the
    same way", "Pash is a media pipeline.", "At WatchDNA" without "On the
    building:").
  - Everything else is as before: myt.design, pf.room.short, wd.infra.stack,
    wd.locator, wd.companion, pash.arch (SQS as the fallback),
    myt.biometrics.mech, le.dashboard.obs, wd.alerts (his words), and the
    availability from basics.availability_fall_2026.

Nothing invented (his earlier request to make things up was declined the
same day; see the notes file). Not claimed: the feature's name, the design
tool, the alert channel, video editing, user research, accessibility,
equity or community work, film or TV experience.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",
    "recipient": ["Creative Technologist Graduate Assistant",
                  "Alexandria Meier, Center for Faculty Advancement, "
                  "New York University"],

    "signpost_1": None,

    # CONSTANT. Copied verbatim from draft-campus-ca.py. Do not edit here.
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

    # Standard wording (CLAUDE.md, 2026-09-05). The letterhead already links
    # the address, so this reads as a pointer rather than a repeat.
    "signpost_2": (
        "I would encourage you to visit my portfolio at www.asmit.space."
    ),

    # ONE technical paragraph. His examples, in his order; availability last.
    "technical": [
        "After reading the requirements, I would like to give a few examples "
        "of the work I have done that show I am ready for this role. Across "
        "my internships the job has mostly been taking an idea, turning it "
        "into a workflow and a user journey, and then building it. At "
        "MyYogaTeacher I was handed a feature as a high-level idea and asked "
        "to produce the initial design - the diagrams, wireframes and user "
        "journeys. Those went out to the development team I was also part "
        "of, so I built against my own drawings. My portfolio works the same "
        "way. It is a room I modelled in Blender and put in the browser with "
        "Three.js, where you walk up to the desk, click the machine, and "
        "every project opens as its own artifact. At WatchDNA I set up the "
        "backend from scratch on Node.js - the schema, the REST endpoints, "
        "JWT authentication with role-based access and the security "
        "middleware - and built the admin console over it. The companion "
        "React Native app reused the same auth and data layers. Pash is a "
        "media pipeline. Uploads land in S3, jobs queue through SQS so a "
        "worker dying does not lose the job, and Demucs splits each track on "
        "a remote CUDA worker. The MyYogaTeacher client streams biometric "
        "data with offline-first sync and time-series deduplication, so "
        "nothing is lost when the network drops. Lead Engine's dashboard is "
        "a live pipeline graph where a failed scout shows up the moment it "
        "fails, and on everything I have shipped I hook up alerts for when "
        "something goes wrong, so it gets debugged and fixed right away. I "
        "can work between five and fifteen hours a week as the work "
        "requires, and with no classes on Monday or Thursday I can figure "
        "out a flexible schedule around the in-person meetings.",
    ],

    "close": None,
    "signoff": None,
}

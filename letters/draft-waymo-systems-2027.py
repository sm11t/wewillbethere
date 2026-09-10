"""Cover letter - Waymo, SWE Intern, Systems Engineering (HIL test infrastructure).

The personal paragraph, the signpost and the close are the constants. Only the
recipient block and the technical middle differ.

LYNTI IS IN HERE ON ASMIT'S INSTRUCTION (2026-09-05), and it is used carefully.
Everything recorded about it is one truncated LinkedIn line:

    "Developed a transportation app using React Native in an effort to
     digitize ride booking and ..."          [truncated, Dec 2024 - Present]

`profile.yaml` carries it as a stub with `facts: []` and
`status: needs_confirmation`. The sentence in this letter says exactly what
that fragment says and not one word more - a transportation app, React Native,
to digitize ride booking. No scale, no users, no outcome, no dates. If he wants
more than that, he has to say what the sentence continued into.

It is placed as MOTIVATION, not as engineering evidence. A React Native
ride-booking app is not test infrastructure and pretending otherwise would be
obvious to the first engineer who read it. What it honestly is: the reason a
person applies to Waymo rather than anywhere else, and the admission that the
hard half of the problem is the half he has not built.

C++ IS NOT CLAIMED IN THIS LETTER. It is their one hard language requirement
and it is `ask: true` in the profile with no evidencing project. It renders on
the resume because leaving it off makes the application pointless, but prose
asserting proficiency he has not confirmed is a different thing entirely.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",
    "recipient": ["Software Engineering Intern, Systems Engineering",
                  "Waymo"],

    "signpost_1": None,

    # CONSTANT. Do not rewrite per job.
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
        "questions that are uncomfortable - I have seen them frustrate "
        "people, but they are usually the ones that need asking. I know I "
        "have a lot left to learn."
    ),

    "signpost_2": (
        "I would encourage you to visit my portfolio at www.asmit.space."
    ),

    # TAILORED. Every claim traces to profile.yaml.
    "technical": [
        "Part of why I am writing is that I have built a very small piece of "
        "this problem. Lynti is a transportation app I built in React Native "
        "to digitize ride booking. Set beside a driver with ten million "
        "rider-only trips behind it that is not much, and I know it. But it "
        "is the same problem from the passenger's end, and building it is "
        "what made me interested in the half I could not build.",

        "The work in this posting is test infrastructure, and the closest "
        "thing I have built is Pash: uploads land in S3, jobs queue through "
        "SQS, and the separation runs on a remote CUDA worker - a job runner, "
        "with execution moved off the machine that asked for it. At WatchDNA I "
        "wrote a Python pipeline that finds retailer endpoints on its own. And "
        "your fourth bullet, authoring design documents and running workshops "
        "to onboard engineers, is the one I have done most directly: as "
        "Technical Officer of the AI Society at Arizona State I wrote the "
        "teaching materials and ran the workshops that made machine learning "
        "approachable to students with no technical background.",
    ],

    "close": (
        "I am available from June 2027."
    ),

    "signoff": None,
}

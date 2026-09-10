"""Cover letter - Waymo, SWE Intern, Fault Protection & Remote Assistance V&V (MS req).

The personal paragraph, the signpost and the close are the constants. Only the
recipient block and the technical middle differ.

This is the master's-tier Waymo req, and unlike the C++ HIL posting it is a
real match: their whole hard technical requirement is "experience with data
analysis/modeling using Python and SQL", and two of their four "You will"
bullets - Python/SQL pipelines, and dashboards that monitor fault rates - have
direct analogues in Lead Engine.

Lynti stays in, at his instruction and in the same careful shape as the other
Waymo letter: exactly what the one truncated LinkedIn line records - a
transportation app, React Native, to digitize ride booking - and nothing more.
Motivation, not engineering evidence.

C++ is not mentioned because this posting does not ask for it, and it is off
the resume for this preset too.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",
    "recipient": ["Software Engineering Intern, Systems Engineering",
                  "Fault Protection & Remote Assistance V&V, Waymo"],

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

        "The pipelines and the dashboards I have done. Lead Engine is a "
        "Python and SQL system that runs five scout agents constantly, "
        "deduplicates what they find by address and scores each lead with the "
        "reasoning written out - and the part I would point at for this role "
        "is the dashboard over it, a live pipeline graph where every scout, "
        "score and call is visible while it runs and a failed scout shows up "
        "the moment it fails - because a pipeline I could not watch fail was "
        "one I could not fix. At MyYogaTeacher I shipped a voice-to-SQL "
        "pipeline that replaced the admin team's Ctrl+F-and-edit workflow, "
        "and at WatchDNA a Python pipeline that finds retailer endpoints on "
        "its own.",
    ],

    "close": (
        "I am available from June 2027."
    ),

    "signoff": None,
}

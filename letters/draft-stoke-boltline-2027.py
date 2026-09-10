"""Cover letter - Stoke Space, Software Intern Summer 2027, Boltline team.

Opening paragraph, signpost and close are unchanged from the template. Only the
recipient block and the technical middle differ.

The angle: Boltline is internal tooling for hardware teams - "design, track,
iterate, build and test". The closest thing he has built is WatchDNA's admin
console for data operations, which is the same species of software: built for
the people running an operation rather than for end customers. That parallel is
real and is what the middle leads with.

Their posting also asks for "ability to manage a complex technical project and
take it through execution", which Torii and Lead Engine answer directly - both
solo, end to end, from question to running system.

Next.js and Apollo are NOT claimed. He has not used either.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",
    "recipient": ["Summer 2027 Software Internship - Boltline",
                  "Stoke Space, Kent, Washington"],

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
        "problems in systems, and I "
        "approach them that way. I also ask the questions that are "
        "uncomfortable - I have seen them frustrate people, but they are "
        "usually the ones that need asking. I know I have a lot left to learn."
    ),

    "signpost_2": (
        "I would encourage you to visit my portfolio at www.asmit.space."
    ),

    # TAILORED. Every claim traces to profile.yaml.
    "technical": [
        "Boltline is software for the people running an operation rather than "
        "for end customers, and that is the kind I have built most. At "
        "WatchDNA I wrote the admin console the team used for data "
        "operations, the store locator it fed, and the Python pipeline that "
        "kept the retailer data current on its own - on a backend I had built "
        "from scratch in TypeScript and Node, with PostgreSQL behind it and "
        "JWT authentication with role-based access in front. I stayed on it "
        "for nine months, which is long enough to maintain something rather "
        "than just ship it. Before that I revamped Flickmatch's website end to "
        "end in React, and wrote its state management as modular pieces so the "
        "same logic carried across the site as it grew.",

        "On taking a complex project through execution: Torii is an MCP proxy "
        "I designed and built alone, sitting between AI agents and the paid "
        "tools they call, with a JSON policy engine, a budget tracker that "
        "reserves funds before the upstream call, and a SQLite ledger "
        "recording every blocked call and why. About seven hundred lines of "
        "TypeScript on two production dependencies. Lead Engine is the same "
        "shape at a larger scale - a FastAPI backend and a React dashboard "
        "over a pipeline that scouts public records, deduplicates by address "
        "and scores what it finds. Both started as a question I could not "
        "answer and ended as something running.",
    ],

    "close": (
        "I am available onsite in Kent for the full term from May 2027."
    ),

    "signoff": None,
}

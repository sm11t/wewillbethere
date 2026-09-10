"""Cover letter - Adobe, Software Engineer Intern 2027.

The personal paragraph, the signpost and the close are the constants. Only the
recipient block and the technical middle differ.

Why the middle is written the way it is: their distinctive requirement is
"exposure to modern development tools, including AI-assisted tools, and an
understanding of how to use them responsibly". Most applicants answer that with
"I use Copilot". Torii is a considered position on the same question held in
code, so it leads, and it carries his own protected line verbatim.

The second paragraph is their software-lifecycle requirement - "designing,
building, deploying, and maintaining applications" - which WatchDNA answers in
one entry.

The App Store claim is deliberately absent. `wd.companion.ios` is blocked in
profile.yaml pending `appstore_outcome`, and a letter is not a way around a
gate the resume respects. The unblocked phrasing - shipping a companion app on
the same infrastructure - says enough.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",
    "recipient": ["Software Engineer Intern, 2027", "Adobe"],

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
        "You ask for an understanding of how to use AI tools responsibly. I "
        "spent long enough on that question to build something. Torii sits "
        "between AI agents and the paid tools they call and decides, per "
        "request, what an agent is allowed to do: identity for each agent, a "
        "policy engine, a budget reserved before the call rather than "
        "reconciled after it, and a ledger recording every call and why any "
        "one was blocked. The rule it is built around is a short one. The "
        "human controls policy. The agent controls execution.",

        "The lifecycle you describe is most of what I did at WatchDNA. I am a "
        "first-year M.S. Computer Science student at NYU after a B.S. at "
        "Arizona State and three internships, and that one ran nine months: I "
        "set up the backend from scratch - databases, JWT authentication with "
        "role-based access, the security middleware - built the store locator "
        "on top of it, and shipped a companion app that reused the same auth "
        "and data layers. Most of what I know about writing maintainable code "
        "I learned across those nine months rather than in the first few "
        "weeks of them.",
    ],

    "close": (
        "I am in New York and available from June through September 2027."
    ),

    "signoff": None,
}

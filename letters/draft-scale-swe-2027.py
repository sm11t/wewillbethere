"""Cover letter - Scale AI, Software Engineering Intern, Summer 2027 (SF).

The personal paragraph, the signpost and the close are the constants. Only the
recipient block and the technical middle differ.

Why the middle is written the way it is: one of Scale's nine example projects is
"ship agentic AI applications and the tooling that makes them observable,
testable, and safe to deploy". Torii is that sentence, so it leads and takes
most of the space - the policy engine is "safe to deploy", the ledger is
"observable", per-agent budgets and identity are what make it testable.

The second paragraph answers their product-engineering requirement - "talking to
customers, figuring out 'what' to build". It says the voice-to-SQL tool replaced
the admin team's Ctrl+F-and-edit workflow, which is a fact in profile.yaml, and
that he had to know the workflow to replace it, which that fact entails. It does
NOT claim he proposed the tool or ran user interviews: both are open questions
in checklists/recover.md and neither has been answered.

Nothing here claims data volume. "Systems that process large volumes of data" is
their sixth requirement and it is the one honest gap - 2,129 leads is not volume
and Scale means billions of tasks.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",
    "recipient": ["Software Engineering Intern, Summer 2027",
                  "Scale AI, San Francisco"],

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
        "You list shipping agentic applications and the tooling that makes "
        "them observable and safe to deploy. That is the project I would "
        "bring. Torii sits between AI agents and the paid tools they call, "
        "enforcing identity, policy and budget on every request: JWT identity "
        "per agent, a policy engine, and a ledger recording every call and "
        "why any one was blocked. The budget tracker "
        "reserves funds before the upstream call, so two agents running at "
        "once cannot overspend the same balance. I did not build a demo of an "
        "agent; I built the thing you would want one running inside.",

        "The rest is product engineering. I am a first-year M.S. Computer "
        "Science student at NYU after a B.S. at Arizona State and three "
        "internships. At WatchDNA I set up the backend from scratch - "
        "databases, JWT authentication with role-based access, the security "
        "middleware - and the store locator on top of it, then stayed with it "
        "across nine months. At MyYogaTeacher I shipped a voice-to-SQL "
        "pipeline that replaced the admin team's Ctrl+F-and-edit workflow; "
        "the part that made it work was knowing what that workflow actually "
        "was, which took longer than the model did.",
    ],

    "close": (
        "I am available in San Francisco from June 2027."
    ),

    "signoff": None,
}

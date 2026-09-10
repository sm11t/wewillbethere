"""Cover letter - PayPal, Software Engineer Intern, Summer 2027.

The opening paragraph, the signpost and the close are copied unchanged from the
internship template. Only the recipient block and the technical middle differ.

Why the middle is written the way it is: the first technical paragraph is their
named stack, in their order - Python, Node.js, React, SQL, REST - because the
Essential Responsibilities name exactly those and WatchDNA answers most of them
in one entry. The second paragraph is Torii, and it is the reason to send this
letter at all: the budget tracker reserves funds before the upstream call so two
agents cannot overspend at once, which is reserve-then-settle, arrived at
independently because the concurrency problem forced it. That is PayPal's own
subject, and no other applicant to this req has built one.

Java is NOT claimed anywhere. The Minimum Qualification asks for one of Java,
Python, C++ or JavaScript, and Python is evidenced four times over.

The close names no office because the pasted posting truncated the location
line. Confirm which req before sending.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",
    "recipient": ["Software Engineer Intern, Summer 2027",
                  "PayPal"],

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
        "I am a first-year M.S. Computer Science student at NYU, graduating in "
        "2028, after a B.S. at Arizona State and three internships. At "
        "WatchDNA I set up the backend from scratch - "
        "the databases, JWT authentication with role-based access, and the "
        "security middleware around it - then stayed with it across nine "
        "months. Python is the language I reach for first: the "
        "endpoint-discovery pipeline behind that product's store locator, "
        "and the FastAPI backend of a lead pipeline that keeps five scouts "
        "running across Zillow, Redfin, FSBO, expired listings and county "
        "assessor records, deduplicating by address and scoring what it "
        "finds.",

        "The work closest to what your team does is Torii. It sits between AI "
        "agents and the paid tools they call, enforcing identity, policy and "
        "budget on every request: JWT identity per agent, a policy engine, "
        "and a ledger recording every call and why any one was blocked. The "
        "payment flow runs end to end: "
        "intercept the HTTP 402, check the wallet, pay, retry. The part worth "
        "talking about is the budget tracker: it reserves funds before the "
        "upstream call, so two agents running at once cannot overspend the "
        "same balance. I did not set out to separate authorization from "
        "settlement; the concurrency problem made me. I would like to see "
        "how it is actually done, at a scale where getting it wrong "
        "matters.",
    ],

    "close": (
        "I am available for the full summer from June 2027."
    ),

    "signoff": None,
}

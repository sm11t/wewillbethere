"""Cover letter - Bain, GenAI / AI-ML Engineering Intern.

Opening paragraph, signpost and close unchanged. Only the recipient block and
the technical middle differ.

The angle: their responsibilities read like a description of Torii. "Guardrails,
fallbacks, human-in-the-loop", "tool use, function calling, orchestration",
"memory and state management", "policy iteration loops" - Torii is a policy
engine with a human owner, a per-session budget state, and a ledger recording
every blocked call and why. The middle says so plainly and lets them notice.

Retrieval is their other big theme and he has not built a RAG pipeline. The
letter does not mention retrieval at all rather than gesture at it - a gap named
badly is worse than a gap left for the interview.

Their last bullet asks for communication with non-technical audiences, which is
what the AI Society year actually was, so the middle closes there.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",
    "recipient": ["AI / ML Engineering Intern - GenAI", "Bain"],

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

    "technical": [
        "The guardrails and human-in-the-loop line in your posting is the "
        "problem I have spent this year on. Torii is an MCP proxy I designed "
        "and built that sits between AI agents and the paid tools they call: a "
        "JSON policy engine with per-session budgets, tool allowlists and rate "
        "limits, a tracker that reserves funds before the upstream call so two "
        "agents cannot overspend at once, and a SQLite ledger recording every "
        "call and every reason one was blocked, surfaced on a live dashboard. "
        "A human owns the policy and the agent owns execution. It handles the "
        "x402 payment flow end to end, and it is about seven hundred lines of "
        "TypeScript on two production dependencies.",

        "Alongside that, the GenAI work I have shipped inside a company was at "
        "MyYogaTeacher, where I built a voice-to-SQL pipeline on Whisper with "
        "streaming LLM responses that replaced the admin team's manual "
        "workflow. Lead Engine is a FastAPI and React system where autonomous "
        "agents scout public records and score every lead against a written "
        "framework, with the reasoning recorded next to the score, because a "
        "score you cannot interrogate is not a score. My research before that "
        "was classical rather than generative - Gaussian Process classifiers "
        "for high-dimensional data, under Prof. R. P. Singh at the University "
        "of Delhi.",

        "On the last thing you ask for: I spent a year as Technical Officer of "
        "the AI Society at Arizona State, writing the teaching materials and "
        "running the workshops that introduced machine learning to students "
        "with no technical background. Explaining a system to someone who does "
        "not have it yet is a skill I have practised deliberately, and it is "
        "the part of client-facing work I am most confident about.",
    ],

    "close": (
        "I am a first-year M.S. Computer Science student at NYU, graduating in "
        "2028 and available from June 2027."
    ),

    "signoff": None,
}

"""Cover letter - NYU Center for Undergraduate Research, General Research
Assistant (graduate pool). Fall 2026, 5-20 hrs/wk once matched, $30/hr.

Here the letter is the application. The Director (Ethan Youngerman) reads it
and matches faculty requests against what it declares - school, course of
study, subject interests, skills - so the technical middle states those four
things plainly. Rewritten 2026-09-07 under letters/GUIDELINES.md.

Structure: the constant personal paragraph (byte-identical to
draft-campus-ca.py), the italic portfolio signpost (his preference, stated
for the CFA letter the same day), two technical paragraphs, a plain close.

Paragraph 1 declares: school and programme, this semester's classes, the
Delhi research, the skills as a list a non-engineer can search on, and the
AI Society teaching as the nearest thing to explaining research to people
outside it. Everything traces to profile.yaml.

Paragraph 2 is the interest he chose on 2026-09-07 from a list of options,
in his framing: "how intelligence should progress and move hand in hand with
humanity", "problems with how AI might be a con in some cases", "control over
data". Grounded in the two projects that raise those questions - Torii (his
own recorded framing from letters/OPENING-OPTIONS.md: he could not explain to
himself who is accountable when an agent overspends; the protected strings
"The human controls policy. The agent controls execution." verbatim) and Lead
Engine (an AI voice calling homeowners; public listings and county records
at scale). No philosopher is named (CLAUDE.md, personal-paragraph rule 2,
applied here too): fields, not names. Routing targets for the Director are
in the notes file - Center for Mind, Brain and Consciousness (Block,
Chalmers; AI moral-status events 2025-2026), Center for Responsible AI,
Philosophy, Center for Bioethics.

School: prints "Tandon" on the strength of his CS-GY registration (Jacobs
Hall, 6 MetroTech), recorded as education.nyu.school_inferred. He has not
said the word; the reply that shipped this draft flags it. The pool requires
the school, so a placeholder would make the letter unsendable.

Close: classes and free days from basics.availability_fall_2026, more over
the breaks (the posting allows it), the F-1 line. No hour count: the
supervisor sets hours once matched, and his on-campus total is still his
call (intake #13).

Not claimed: literature reviews, surveys, interviews, lab work, participant
recruitment, academic writing, film editing, any spoken language, any
coursework in philosophy.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    "recipient": ["Graduate Research Assistant, general pool",
                  "Ethan Youngerman, Director of Undergraduate Research, "
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

    # Standard wording (CLAUDE.md, 2026-09-05).
    "signpost_2": (
        "I would encourage you to visit my portfolio at www.asmit.space."
    ),

    # TAILORED. Every claim traces to profile.yaml or to his words of
    # 2026-09-07 (the interest paragraph's framing).
    "technical": [
        "I am a first-year M.S. Computer Science student at NYU Tandon, after "
        "a B.S. in Computer Science at Arizona State, and my classes this "
        "semester include algorithms and artificial intelligence. The "
        "research I can point to is a summer at the University of Delhi under "
        "Prof. R. P. Singh, optimizing Gaussian Process classifiers for "
        "high-dimensional data. The skills a lab could use, as a list: Python "
        "and SQL for data pipelines, React and React Native, LLM pipelines "
        "with Whisper and streaming responses, dashboards, Blender and "
        "Three.js. At the AI Society at Arizona State I wrote the materials "
        "for and ran the workshops that made machine learning approachable "
        "to students with no technical background, which is the closest "
        "thing I have done to explaining research to people outside it.",

        "The subject I would most like to be matched on sits between computer "
        "science and philosophy. I mean how intelligence should progress hand "
        "in hand with people rather than past them, the cases where what is "
        "sold as AI is closer to a con than a tool, and who controls the "
        "data underneath. Both of the projects I care most about "
        "came out of those questions. Torii exists because I could not "
        "explain to myself who is accountable when an AI agent holding a "
        "wallet overspends. I built a proxy that sits between the agent "
        "and every paid tool it calls and writes down every blocked call "
        "with its reason. The human controls policy. The agent controls "
        "execution. Lead Engine calls homeowners with an AI voice and scouts "
        "public listings and county records at scale, which is where the "
        "question of who controls the data stops being abstract. I would "
        "take work on any side of this - philosophy of mind, the ethics of "
        "AI, data governance - with people who have thought about it longer "
        "than I have.",
    ],

    # HARD REQUIREMENT. Days and eligibility verified user_2026-09-07.
    "close": (
        "I can fit research hours around my classes, which are on Tuesday and "
        "Wednesday evenings and Friday late morning, with none on Monday or "
        "Thursday, and I can do more over the breaks. I am on an F-1 visa, "
        "which permits on-campus employment without further authorization. I "
        "would be glad to be passed along to any group that could use this."
    ),

    "signoff": None,
}

"""Cover letter - NYU Tandon Biomedical Engineering, Course Assistant for
BI-GY 810X, Bioinformatics Capstone (Dr. Mgavi Brathwaite). Fall 2026, $30/hr,
hours set by the instructor.

Campus CA genre, straight from draft-campus-ca.py: read by one professor, no
signpost, personal paragraph copied verbatim, course named in the recipient
block. The technical paragraph evidences the three things the posting asks for
that profile.yaml can back - Python, GenAI (voice-to-SQL on Whisper with
streaming LLM responses, Lead Engine's LLM scoring, Torii's MCP proxy) and
teaching (AI Society workshops and mentoring). Deliberately NOT claimed, because
nothing in profile.yaml evidences them: R, numpy/pandas/seaborn/scipy, UNIX,
nbgrader, Otter, Gradescope, JupyterHub, genomics, PyTorch, deep learning as a
skill, and grading experience. Those are reported as gaps in the notes file.

One deviation from the template: draft-campus-ca.py says "a year as Technical
Officer", but profile.yaml dates the role Aug 2025 - Jan 2026. The profile wins,
so this draft names the role with no duration until he confirms one. Hours,
days and work authorization ship as placeholders on purpose and gate sending.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    # Course named, per the campus-CA rule. Title verified against the NYU
    # bulletin (bulletins.nyu.edu/courses/bi_gy/); the program sits in BME.
    "recipient": ["Course Assistant - BI-GY 810X, Bioinformatics Capstone, "
                  "Biomedical Engineering",
                  "Dr. Brathwaite, NYU Tandon School of Engineering"],

    # Campus genre: no signpost at this length.
    "signpost_1": None,
    "signpost_2": None,

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

    # TAILORED. Every claim traces to profile.yaml: ais.workshops.t,
    # ais.mentoring.t, du.gpc.r, myt.voicesql.mech, le.pipeline (LLM scoring
    # with written reasoning; stack Python), torii.core.infra, education/nyu.
    "technical": [
        "I was Technical Officer of the AI Society at Arizona State, where I "
        "wrote the teaching materials and ran the workshops that introduced "
        "machine learning to students with no technical background. I also "
        "mentored four freshmen through their first ML project, an emotion "
        "detection system reading facial expressions and audio cues. Before "
        "that I worked under Prof. R. P. Singh at the University of Delhi on "
        "optimizing Gaussian Process classifiers. At MyYogaTeacher I shipped "
        "a voice-to-SQL pipeline on Whisper with streaming LLM responses that "
        "replaced the admin team's Ctrl+F-and-edit workflow. Lead Engine is a "
        "Python pipeline that scores every lead with an LLM and writes the "
        "reasoning out next to the score. Torii is an MCP proxy that sits "
        "between AI agents and the paid tools they call. I am now a "
        "first-year M.S. Computer Science student at NYU.",
    ],

    # HARD REQUIREMENT. Do not send with the placeholders in it: hours, days
    # and work authorization gate the whole application, and all three are
    # still open in checklists/intake.md. The posting leaves hours to the
    # instructor, so [N] is his offer, not their number.
    "close": (
        "I can commit [N] hours a week through the semester on whatever "
        "schedule the course needs, and I am available [DAYS]. [WORK "
        "AUTHORIZATION LINE - see intake.md]. I would be glad to talk about "
        "what the course needs."
    ),

    "signoff": None,
}

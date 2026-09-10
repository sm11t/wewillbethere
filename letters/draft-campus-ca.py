"""Draft cover letter - NYU course assistant / grader.

A different genre from the internship letter, not a shorter version of it.

What actually changes:
  - Read by a human. A professor or a department administrator, not an ATS,
    and usually as the body of an email rather than an attachment.
  - 150-250 words, not 400. Ceremony costs more than it earns at this length,
    so the italic signpost is dropped.
  - They screen on different things: did you take the course, can you explain
    it, how many hours, and are you eligible to be paid. Impressive projects
    are close to irrelevant - one line of engineering credibility is enough.
  - Availability is a hard requirement, not a closing pleasantry.

The personal paragraph is the same one, with a single sentence added. Being
unashamed to ask a question twice is the quality that makes a good course
assistant - someone who still remembers what not understanding feels like - so
the trait does not change, only what it is pointed at.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    # TAILOR: name the course and the instructor. A grader application that
    # does not name the course reads as a mass email, which it then is.
    "recipient": ["Course Assistant - [COURSE CODE], [COURSE TITLE]",
                  "[Professor / Department], New York University"],

    # No signpost at this length - it is ceremony the letter cannot afford.
    "signpost_1": None,
    "signpost_2": None,

    # Same paragraph as the internship letter, one sentence added at the end.
    # CONSTANT within this genre. Do not rewrite it per course.
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

    # TAILOR: the course, and what he can point to for it.
    "technical": [
        "I spent a year as Technical Officer of the AI Society at Arizona "
        "State, where I wrote the teaching materials and ran the workshops "
        "that introduced machine learning to students with no technical "
        "background, and mentored four freshmen through their first ML "
        "project. Before that I worked under Prof. R. P. Singh at the "
        "University of Delhi on optimising Gaussian Process classifiers. I am "
        "now a first-year M.S. Computer Science student here, with three "
        "engineering internships behind me.",
    ],

    # HARD REQUIREMENT. This letter should not be sent with the placeholders in
    # it: hours and work authorization gate the whole application, and both are
    # still open in checklists/intake.md.
    "close": (
        "I can commit [N] hours a week through the semester, and I am "
        "available [DAYS]. [WORK AUTHORIZATION LINE - see intake.md]. I would "
        "be glad to talk about what the course needs."
    ),

    "signoff": None,
}

"""Cover letter - NYU School of Global Public Health, Graduate Research
Assistant, Dean's Office (Dr. Jemar Bather). Fall 2026, 10 hrs/wk, $30/hr.

Research genre (letters/GUIDELINES.md, section 2): read by one biostatistician,
probably as an email body, so no italic signpost and no ceremony. The personal
paragraph is the campus one, copied verbatim from draft-campus-ca.py.

What the research found (2026-09-07, full record with URLs in
jobs/nyu-gph-research-assistant-fall-2026.notes.md):

  - Bather is now Assistant Professor of Biostatistics, co-directing the BASE
    and ReCAP labs and reviewing statistics for JAMA Network Open. Earlier
    snippets calling him "visiting" are stale.
  - His most recent first-author paper (JAMA Network Open, 2026, Dean Goodman
    a coauthor) analyses the 2024 HINTS survey: which patients open test
    results before their clinician does, and who comes away not understanding
    them - worse among people with lower digital literacy. That is the one
    anchor this letter uses, because it is the Dean's Office collaboration
    the posting is recruiting for, and because "make a technical thing
    understandable to someone who did not sign up for it" is what his AI
    Society work actually was.
  - He speaks at the department seminar on September 10, 2026 (marginal risk
    ratios under informative cluster sizes). Not claimed here; suggested in
    the notes.

The technical middle is two paragraphs.

Paragraph 1 is the data work and, on his instruction of 2026-09-07, two
additions. (a) Qualtrics, stated plainly as a tool he has not used, then the
workflow he looked up (questions and branching, collect, clean, export) tied
to Lead Engine's collect-deduplicate-score pipeline. His framing: "after
looking it up, it is somewhat of a workflow I am familiar with." (b) That he
learns new things, solves problems and figures out the unfamiliar on his own
- written as what happened on Pash, a solo project, because the personal
paragraph's rule 3 forbids stating the trait and the reader has to be able to
name it themselves. "With nobody to ask" is entailed by the project being
solo; "learning Demucs" is entailed because Pash is the only evidence for
Demucs in the profile.

Paragraph 2 is the writing: the AI Society workshops and the mentoring, then
the anchor (Bather et al., JAMA Network Open, 2026). The [HIS WORDS] marker
came off earlier the same day on his instruction, after he was shown the
text. He still has to read the paper's abstract before sending (PMC13487547).

Not claimed, because none is in profile.yaml: Zotero, Google Forms, R,
literature reviews, grant support, public health coursework. Qualtrics IS
named, as a gap, because he asked to be upfront about it - GUIDELINES.md
voice rule 13 was amended the same day to allow exactly this: a gap he
chooses to name, paired with a true analogue, never with a tool claim.

The close is fully resolved. Days in his own words ("I can figure out a
flexible schedule around my classes"; classes Tue 5:00-7:30 PM, Wed 6:00-8:30
PM, Fri 11:00 AM-1:30 PM; none Mon or Thu), recorded in profile.yaml under
basics.availability_fall_2026. Work authorization F-1, under
basics.work_authorization, same source.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    "recipient": ["Graduate Research Assistant, Dean's Office",
                  "Dr. Jemar Bather, NYU School of Global Public Health"],

    # Research genre: no signpost.
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

    # TAILORED. Every claim traces to profile.yaml except the anchor, which
    # traces to the notes file, and the Qualtrics sentence, which is his
    # instruction of 2026-09-07.
    "technical": [
        "The work closest to what the posting describes is a summer I spent "
        "at the University of Delhi under Prof. R. P. Singh, optimizing "
        "Gaussian Process classifiers for high-dimensional data. Since then "
        "most of my data work has been in Python and SQL. Lead Engine keeps "
        "five scout agents running across Zillow, Redfin, FSBO, expired "
        "listings and the Maricopa County Assessor, deduplicates what they "
        "find by address, and scores every lead with the reasoning written "
        "out beside the score - 2,129 leads sourced. The dashboard over it is "
        "a live pipeline graph, so a failed scout shows up the moment it "
        "fails. I have not used Qualtrics. I looked it up before writing "
        "this. The workflow - write the questions and the branching, "
        "collect the responses, clean them, export them - is close to what "
        "Lead Engine does with listings, so the tool is new to me but the "
        "work is not. Pash, a side project that splits a song into its "
        "parts, is the usual pattern: I wanted it to exist, so I learned "
        "Demucs and wired S3, SQS and a remote CUDA worker together with "
        "nobody to ask. Most of what I know got learned that way.",

        "For the writing, what I can point to is the AI Society at Arizona "
        "State, where I wrote the materials for and ran the workshops that "
        "made machine learning approachable to students with no technical "
        "background. I also mentored four freshmen through their first ML "
        "project. Your paper this year in JAMA Network Open is the same "
        "problem from the other side. Patients open their test results "
        "before a clinician has talked them through, and the ones with less "
        "digital literacy come away not understanding what they read. That "
        "is the kind of work I would like to be part of.",
    ],

    # HARD REQUIREMENT. Days and eligibility, both verified user_2026-09-07.
    "close": (
        "I can commit the ten hours a week the posting describes through the "
        "fall semester. My classes are on Tuesday and Wednesday evenings and "
        "Friday late morning, and I have none on Monday or Thursday, so I can "
        "figure out a flexible schedule around them. I am on an F-1 visa, "
        "which permits on-campus employment without further authorization. I "
        "would be glad to talk about what the project needs."
    ),

    "signoff": None,
}

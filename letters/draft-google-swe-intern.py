"""Draft cover letter - Google, Software Engineering Intern, MS, Summer 2027.

Structure:
    highlighted signpost   tells the reader how to navigate
    personal paragraph     the part that does not fit on a resume
    second signpost        where the checkable evidence starts
    technical paragraphs   the only part that changes per job
    close                  what he wants, plainly

No philosopher is named and nothing is quoted. The ideology is the shape of the
paragraph, not a citation. See letters/OPENING-OPTIONS.md for the alternatives.

The personal paragraph is raw material. Under profile/voice.md it is the one
part the system should not be writing for him.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",
    "recipient": ["Software Engineering Intern, MS, Summer 2027",
                  "Google"],

    # No highlighted signpost. The first line of the paragraph does the
    # navigational job on its own.
    "signpost_1": None,

    # Character only, in Asmit's own words and close to how he said them.
    # Deliberately plain - no literary phrasing, nothing borrowed from the
    # resume. THIS PARAGRAPH IS YOURS.
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

    # TAILOR THIS PER JOB. Everything above can stay; this is the part that
    # changes. Each claim traces to profile.yaml.
    "technical": [
        "I am a first-year M.S. Computer Science student at NYU, after a B.S. "
        "at Arizona State and three engineering internships. At WatchDNA I "
        "built the backend from scratch - databases, JWT authentication with "
        "role-based access, and the security middleware around it - then "
        "shipped a store locator on top of it and a companion React Native app "
        "that reused the same auth and data layers. At MyYogaTeacher I wrote "
        "the React Native client that streams biometric data in real time, "
        "with offline-first sync and time-series deduplication so nothing is "
        "lost when the network drops.",

        "The work closest to what your team does is the agent infrastructure. "
        "Torii is about seven hundred lines of TypeScript on two production "
        "dependencies, handling the x402 payment flow end to end: intercept "
        "the HTTP 402, check the wallet, pay, retry, with a budget tracker "
        "that reserves funds before the upstream call so two agents cannot "
        "overspend at once. Lead Engine is the other half of that instinct - "
        "an autonomous pipeline that scouts public listing and county records, "
        "deduplicates by address, and scores every lead with the reasoning "
        "written out, because a score you cannot interrogate is not a score. "
        "2,129 leads so far.",
    ],

    "close": (
        "I am in New York and available from June 2027."
    ),

    # No typed signature: the letterhead already says the name.
    "signoff": None,
}

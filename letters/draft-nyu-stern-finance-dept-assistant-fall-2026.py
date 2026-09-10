"""Note of interest - NYU Stern Finance Department, Department Assistant (Fall 2026).

An email, not a cover letter. The posting asks for a resume and a brief note
of interest sent to Christina Borovilas, so the .txt that publish_letter
writes is the artifact that ships - pasted into the email body - and the PDF
is a courtesy attachment. No signpost: campus genre, and an email cannot
afford the ceremony. The personal paragraph is the campus constant, copied
verbatim from draft-campus-ca.py. Flickmatch leads the technical paragraph
because "HTML experience is required" and revamping a whole website from
Figma designs is the nearest thing on the profile to maintaining web content.
Nothing here claims CMS or reception-desk experience; neither is in the profile.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    "recipient": ["Department Assistant, Finance Department",
                  "Christina Borovilas, NYU Stern School of Business"],

    # No signpost. Campus genre, email body.
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

    # TAILORED. Every claim traces to profile.yaml: fm.ui.full (Flickmatch),
    # portfolio (stack: Three.js, Blender, React; HTML/CSS evidenced there),
    # wd.locator.full ("an admin console for data operations"), and
    # ais.workshops.t. "Updated through" is a paraphrase of "data operations"
    # and is flagged in the notes file for his confirmation.
    "technical": [
        "I am a first-year M.S. Computer Science student at NYU. The closest "
        "thing on my resume to this job is Flickmatch, where I revamped the "
        "website end to end, turning the new Figma designs into responsive "
        "React and Material-UI components across every page. I built and keep "
        "up my own site, asmit.space, in HTML/CSS, React and Three.js. At "
        "WatchDNA I built the admin console the store locator's data is "
        "updated through. As Technical Officer of the AI Society at Arizona "
        "State I wrote the materials for and ran workshops that introduced "
        "machine learning to students with no technical background.",
    ],

    # HARD REQUIREMENT. Do not send with the placeholders in it. Hours, days
    # and work authorization are all still open in checklists/intake.md, and
    # the posting itself is silent on hours.
    "close": (
        "I can commit [N] hours a week through the semester, and I am "
        "available [DAYS]. [WORK AUTHORIZATION LINE - see intake.md]. I would "
        "be glad to come by the department to talk about what the role needs."
    ),

    "signoff": None,
}

"""Cover letter - ICF, 2027 Summer Intern, Software Developer. 10 weeks,
June to August 2027, full time; location not stated in the posting.

Internship genre (letters/GUIDELINES.md, section 2): ATS then a recruiter,
then a technology lead. PDF attachment; the italic portfolio signpost stays.
The personal paragraph is the internship one, copied verbatim from
draft-google-swe-intern.py. Written 2026-09-07.

Standing content (GUIDELINES.md section 6) is all here: WatchDNA's impact
(wd.impact), MyYogaTeacher's time saved (myt.voicesql.time), and the
always-building hinge before the projects. His AI-practice framing from the
Dropbox letter the same evening (harness over prompt; parallel, budgeted,
checked) is reused in one sentence, because the posting names "AI-assisted
development, agentic workflows" outright.

Research (jobs/icf-swe-intern-summer-2027.notes.md): ICF is a federal
technology and consulting firm; in January 2026 its federal technology
practice received four ServiceNow Validated Practice Awards, and it sells
"ICF Fathom", a suite of AI agents built to integrate into an agency's
existing infrastructure. Partnerships: ServiceNow, Salesforce, Appian,
Microsoft. The one anchor is Fathom - agents that sit inside existing systems
- tied to Torii, which is a proxy that governs what an agent may touch.

Paragraph order follows what this posting screens on: requirements into a
solution (MyYogaTeacher's feature design, first), workflows and automations
(voice-to-SQL; the WatchDNA pipeline), integrations and APIs (WatchDNA
backend), then the agent work.

The named gap (GUIDELINES.md voice rule 13): he has not used Salesforce,
ServiceNow or Appian. The true analogue is Torii's JSON policy engine - rules
a person edits without touching code, which is the low-code idea at a much
smaller scale. Not papered over, not dressed up.

Not claimed: any low-code platform, Confluence, accessibility work, any
client or government experience. Java, Jira and Agile appear on the resume
on coursework evidence; the letter does not mention them.

Close: New York, full time from June 2027. The posting's "authorized to work
in the United States" line is his to answer on the form; CPT is work
authorization for a degree-related internship, but a federal contractor may
also decline anyone who will need sponsorship later. Flagged in the notes.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    "recipient": ["2027 Summer Intern, Software Developer",
                  "ICF"],

    "signpost_1": None,

    # CONSTANT. Copied verbatim from draft-google-swe-intern.py. Do not edit.
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
        "questions that are uncomfortable - I have seen them frustrate people, "
        "but they are usually the ones that need asking. I know I have a lot "
        "left to learn."
    ),

    # Standard wording (CLAUDE.md, 2026-09-05).
    "signpost_2": (
        "I would encourage you to visit my portfolio at www.asmit.space."
    ),

    # TAILORED. Every claim traces to profile.yaml or his words of 2026-09-07.
    "technical": [
        "I am a first-year M.S. Computer Science student at NYU, after a B.S. "
        "at Arizona State and three engineering internships. At MyYogaTeacher "
        "I was given the initial design of a new feature and turned the idea "
        "into diagrams, wireframes and user journeys for the development "
        "team, then built against my own drawings. The voice-to-SQL pipeline "
        "I shipped on Whisper replaced the admin team's Ctrl+F-and-edit "
        "workflow and gave them back the hours that took. At WatchDNA I set "
        "up the backend from scratch on Node.js - the schema, the REST "
        "endpoints, JWT authentication with role-based access, the security "
        "middleware - and built the store locator and the admin console over "
        "it. An automated Python pipeline discovers the retailer endpoints. "
        "Those replaced an expensive third-party app the company "
        "had been paying for, and within six months of going live the "
        "traffic was up.",

        "Outside work I am always building something, usually to try a "
        "technology I have not used yet, and the two most recent are agent "
        "systems. Lead Engine keeps five scout agents running in parallel "
        "across Zillow, Redfin, FSBO, expired listings and the Maricopa "
        "County Assessor, deduplicates what they find by address, and scores "
        "every lead with the reasoning written out beside the score - 2,129 "
        "leads sourced. Torii is a proxy between an AI agent and every paid "
        "tool it calls, with a budget reserved before each call, a JSON "
        "policy the human edits without touching code, and a ledger of every "
        "call and every reason one was blocked. Most of my own work now runs "
        "through coding agents, and the part I have got good at is the "
        "harness around them rather than the prompt. I have not used "
        "Salesforce, ServiceNow or Appian. Torii's policy file is the same "
        "idea at a much smaller scale, and I would expect to pick the "
        "platforms up the way I picked up everything else on this page. Your "
        "Fathom agents are built to sit inside an agency's existing systems "
        "rather than beside them. That is the part of agentic work I would "
        "most like to learn from the inside: the integration, the "
        "permissions, and what happens when an agent is wrong.",
    ],

    "close": (
        "I am in New York and available full time from June 2027."
    ),

    "signoff": None,
}

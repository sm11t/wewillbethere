"""Cover letter - Dropbox, Software Engineering Intern, Summer 2027 (Virtual
First, from New York). Open until October 2, 2026.

Internship genre (letters/GUIDELINES.md, section 2): ATS, recruiter, then a
team-matching survey and technical rounds. PDF attachment; the italic
portfolio signpost stays. The personal paragraph is the internship one,
copied verbatim from draft-google-swe-intern.py. Written 2026-09-07.

His instruction for this letter, in his words: "include how I am efficient
with the AI tools I use. I know how to utilise agents well in terms of token
spending usage, parallelisation and efficient prompting. say how I utilise
techniques like harness engineering and agentic workflows and everything else
that is needed for efficient AI usage." Recorded in profile.yaml under
user_2026-09-07. Paragraph 2 opens on the
always-building hinge (his instruction, same evening; GUIDELINES.md section
6), then states the AI practice in his framing and proves it
with the two recorded projects that are literally that practice:

  - Lead Engine: five scout agents running constantly (in parallel is
    entailed - five agents running at once) across five named sources,
    deduplicated by address, every lead scored with the reasoning written out
    (le.pipeline.sources, le.score); the dashboard where a failed scout shows
    up the moment it fails (le.dashboard.obs). 2,129 leads (recorded).
  - Torii: a proxy between an agent and every paid tool it calls; a budget
    reserved before each upstream call so two agents cannot overspend at once;
    a JSON policy the human controls; a SQLite ledger of every call and every
    reason one was blocked (torii.arch, torii.x402). Protected strings kept:
    "The human controls policy. The agent controls execution."

The one anchor (research, jobs/dropbox-swe-intern-summer-2027.notes.md):
Dropbox's own tech-blog post "Beyond code generation: rethinking engineering
productivity in the age of AI agents" - AI raised coding throughput and moved
the bottleneck to review queues, CI, validation, release coordination and
operations. That is the harness argument from inside a large company, and it
is the sentence the letter ends on. He reads the post before sending.

Paragraph 1 is the internships (wd.infra.stack, wd.locator, wd.impact,
wd.companion; myt.biometrics.mech, myt.voicesql.mech, myt.voicesql.time -
the two impact facts are his words of 2026-09-07, no numbers) and the
graduation year - "2028",
the profile's word; the month is unconfirmed (intake #3) and the form will
ask for it.

Not claimed: Copilot (the posting's example tool; nothing recorded), any
specific agent product he uses day to day, Go beyond the skills block
(coursework evidence), any Dropbox product knowledge. "Passion", "AI
fluency" and the four durable skills are not echoed.

Close: New York, full time, any of the three start dates. NYU's spring term
ends mid-May, so May 27 works; CPT through NYU is routine for a summer
internship tied to the degree.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    "recipient": ["Software Engineering Intern, Summer 2027",
                  "Dropbox"],

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

    # TAILORED. Paragraph 1 traces to profile.yaml. Paragraph 2 is his stated
    # practice (user_2026-09-07) proved by Lead Engine and Torii, then the
    # anchor.
    "technical": [
        "I am a first-year M.S. Computer Science student at NYU, graduating "
        "in 2028, after a B.S. at Arizona State and three engineering "
        "internships. At WatchDNA I set up the backend from scratch on "
        "Node.js - the schema, the REST endpoints, JWT authentication with "
        "role-based access, the security middleware - and built the store "
        "locator and the admin console over it. Those replaced an expensive "
        "third-party app the company had been paying for, and within six "
        "months of going live the traffic was up. The companion React Native "
        "app I shipped reused the same auth and data layers. At MyYogaTeacher "
        "I wrote the React Native client that streams biometric data in real "
        "time, with offline-first sync and time-series deduplication so "
        "nothing is lost when the network drops. The voice-to-SQL pipeline I "
        "shipped on Whisper replaced the admin team's Ctrl+F-and-edit "
        "workflow and gave them back the hours that took.",

        "Outside work I am always building something, usually to try a "
        "technology I have not used yet. The two most recent are Lead Engine "
        "and Torii. Most of my own work now runs through coding agents, and "
        "the part I have got good at is the harness around them rather than "
        "the prompt. Lead Engine keeps five scout agents running in parallel "
        "across "
        "Zillow, Redfin, FSBO, expired listings and the Maricopa County "
        "Assessor, and deduplicates what they find by address. Every lead is "
        "scored with the reasoning written out beside the score, so a bad "
        "call is visible instead of buried - 2,129 leads sourced. Torii is "
        "the other half: a proxy between an agent and every paid tool it "
        "calls. A budget is reserved before each call so two agents cannot "
        "overspend at once, and a ledger keeps every call and every reason "
        "one was blocked. The human controls policy. The agent controls "
        "execution. Between them, that is how I spend tokens: in parallel "
        "where the work splits, with a budget on every agent, and with "
        "checks that catch what the model gets wrong. Your engineering "
        "blog's post on what happens after code generation - the bottleneck "
        "moving to review, CI and validation - is the same thing seen from "
        "inside a much larger company. It is the problem I would most like "
        "to work on.",
    ],

    # Full time, any of the three start dates; New York is the primary
    # work location.
    "close": (
        "I am in New York and available full time for any of the three "
        "start dates."
    ),

    "signoff": None,
}

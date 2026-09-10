"""Cover letter - Betterment, Software Engineering Intern, New York (hybrid).

Internship genre (letters/GUIDELINES.md, section 2): recruiter after an ATS,
then an engineer; PDF attachment; the italic portfolio signpost stays. The
personal paragraph is the internship one, copied verbatim from
draft-google-swe-intern.py. Written 2026-09-07; second version the same
evening on his instruction: no Torii, internships only, owning the work with
examples, a little more on what each internship achieved.

Research (jobs/betterment-swe-intern.notes.md): Betterment runs a Ruby on
Rails monolith, Flutter for mobile, Julia for some computation; interns are
paired with a mentor across full-stack, backend and mobile, in Manhattan. The
Delayed-post anchor from the first version came out with Torii - it was tied
to the side projects, and he asked for internships only. The research stays
in the notes for the interview.

The technical middle is two paragraphs, internships only, every claim from
profile.yaml:

  Paragraph 1 - WatchDNA. One hinge sentence (a claim with its method
  attached, per the personal-paragraph rule 5): across three internships what
  he was handed became his to finish, from the first drawing to the alert
  that fires when it breaks. Then: nine months (Aug 2025 - Apr 2026);
  wd.infra.stack; wd.locator.full; wd.companion (Expo, Supabase, same auth
  and data layers, iOS App Store review including the reviewer
  correspondence - canonical says Guideline 2.1); wd.alerts (his words).
  "Launched" is not said - intake #12 is still open.

  Paragraph 2 - MyYogaTeacher and Flickmatch. myt.design (his words: given
  the responsibility for a feature's initial design; diagrams, wireframes,
  user journeys; built against his own drawings); myt.biometrics.mech;
  myt.voicesql.mech (the Ctrl+F detail is his). Flickmatch: fm.ui.full and
  fm.state.med, scope confirmed by him 2026-09-04.

Not claimed: the blocked numbers (99.9% uptime, 60% edit cut), that the
companion app launched, Java or Ruby beyond the skills block, any startup
label, any fintech knowledge. No side project appears.

Term: the posting does not say, and its graduation line reads "Spring/Summer
2026". The close assumes Summer 2027; he checks the term on the form.
"""

LETTER = {
    "name": "Asmit Datta",
    "contact": ["New York, NY", "asmit77@icloud.com", "asmit.space",
                "github.com/sm11t", "linkedin.com/in/asmitrajeet"],
    "date": "September 2026",

    "recipient": ["Software Engineering Intern, New York",
                  "Betterment"],

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

    # TAILORED. Internships only. Every claim traces to profile.yaml.
    "technical": [
        "I am a first-year M.S. Computer Science student at NYU, after a B.S. "
        "at Arizona State and three engineering internships. Across the three, "
        "what I was handed became mine to finish, from the first drawing to "
        "the alert that fires when it breaks. WatchDNA was nine months. I set "
        "up the backend from scratch on Node.js - the schema, the REST "
        "endpoints, JWT authentication with role-based access, the security "
        "middleware. Over it I built the store locator: an interactive "
        "Mapbox map with real-time filtering, an admin console for data "
        "operations, and a Python pipeline that discovers retailer endpoints "
        "on its own. When the companion app came, I built it in React Native "
        "on Expo and Supabase, reused the same auth and data layers, and took "
        "it through iOS App Store review myself, including the "
        "correspondence with the reviewer. I hooked up alerts for anything "
        "that failed, so a broken endpoint was seen and fixed right away.",

        "At MyYogaTeacher I was given the initial design of a new feature. I "
        "turned the idea into diagrams, wireframes and user journeys, handed "
        "them to the development team I was part of, and then built against "
        "my own drawings. I also wrote the React Native client that streams "
        "biometric data in real time, with offline-first sync and time-series "
        "deduplication so nothing is lost when the network drops. The "
        "voice-to-SQL pipeline I shipped on Whisper, with streaming "
        "responses, replaced the admin team's Ctrl+F-and-edit workflow. "
        "Before that, at "
        "Flickmatch, I revamped the website end to end, turning new Figma "
        "designs into responsive React and Material-UI components across "
        "every page. I wrote the state management as modular pieces, so the "
        "same logic carried across the site as it grew.",
    ],

    # Summer 2027 assumed; the posting does not state a term.
    "close": (
        "I am in New York and available from June 2027."
    ),

    "signoff": None,
}

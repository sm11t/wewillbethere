#set document(title: "Asmit Datta - Resume (DRAFT, unapproved)", author: "Asmit Datta")
#set page(paper: "us-letter", margin: (x: 0.6in, top: 0.5in, bottom: 0.5in))
#set text(font: ("Cambria", "Georgia", "Libertinus Serif"), size: 10pt, lang: "en", hyphenate: false)
#set par(justify: false, leading: 0.62em, spacing: 0.62em)
#show link: set text(fill: rgb("#12408f"))

#let sechead(t) = block(above: 0.85em, below: 0.42em)[
  #text(size: 1.02em, weight: "bold", tracking: 0.06em)[#upper(t)]
  #v(-0.62em)
  #line(length: 100%, stroke: 0.55pt + rgb("#444444"))
]
#let row(l, r) = block(above: 0.55em, below: 0.10em, width: 100%)[
  #grid(columns: (1fr, auto), align: (left, right), l, r)
]
#let subrow(l, r) = block(above: 0.10em, below: 0.16em, width: 100%)[
  #grid(columns: (1fr, auto), align: (left, right), l, r)
]
// Bullets need more air between them than their own wrapped lines have,
// or a two-line bullet reads as two separate points.
#let pt(body) = block(above: 0.34em, below: 0.02em, width: 100%)[
  #grid(columns: (0.70em, 1fr), gutter: 0pt, align: (left, left),
    text[#sym.bullet], body)
]

#align(center)[
  #text(size: 19pt, weight: "bold")[Asmit Datta]
]
#v(0.15em)
#align(center)[
  #text(size: 9pt)[New York, NY  #h(0.35em) | #h(0.35em)  asmit77\@icloud.com  #h(0.35em) | #h(0.35em)  asmit.space  #h(0.35em) | #h(0.35em)  linkedin.com/in/asmitrajeet  #h(0.35em) | #h(0.35em)  github.com/sm11t]
]
#sechead[Education]
#row([*New York University*], [New York, NY])
#subrow([_M.S. in Computer Science_], [_Expected 2028_])
#row([*Arizona State University*], [Tempe, AZ])
#subrow([_B.S. in Computer Science, Minor in Business_], [_May 2026_])
#sechead[Projects]
#row([*Portfolio*], [])
#subrow([_asmit.space_], [_Three.js, Blender, React_])
#pt[Modeled my own room in Blender and put it in the browser with Three.js - you walk up to the desk, click the machine, and every project opens as its own artifact instead of a list of links]
#row([*Pash*], [2026])
#subrow([_lnkd.in/p/dCwX6kYm_], [_AWS S3/SQS, Demucs v4, CUDA_])
#pt[Split songs into vocals, drums, bass and instrumentals with Demucs v4 - uploads land in S3, jobs queue through SQS, and separation runs on a remote CUDA worker, 5-10x faster than on CPU]
#row([*Lead Engine*], [2026])
#subrow([_asmit.space/lead-engine_], [_Python, FastAPI, React, SQLAlchemy_])
#pt[Built a React dashboard over it with a live pipeline graph]
#pt[Kept five scout agents running constantly across Zillow, Redfin, FSBO, expired listings and the Maricopa County Assessor, deduplicating by address and scoring every lead on motivation, ability and timeline with the reasoning written out - 2,129 leads sourced]
#row([*Torii*], [2026])
#subrow([_asmit.space/kya_], [_TypeScript, Bun, Hono, SQLite_])
#pt[Put an MCP proxy between AI agents and the paid tools they call, enforcing identity, policy and budget on every request: JWT agent identity, a JSON policy engine, and a SQLite ledger recording every call and every reason one was blocked]
#pt[Handled the x402 payment flow end to end - intercept the HTTP 402, check the wallet, pay, retry - with a budget tracker that reserves funds before the upstream call so two agents cannot overspend at once; the whole thing ships on two production dependencies]
#sechead[Experience]
#row([*Software Engineer Intern (Capstone)*], [Aug 2025 – Apr 2026])
#subrow([_WatchDNA_], [_Ontario, Canada (Remote)_])
#pt[Built WatchDNA's store locator: an interactive Mapbox map with real-time filtering, an admin console for data operations, and a Python pipeline that discovers retailer endpoints on its own]
#pt[Set up the backend from scratch on Node.js - the database schema, the REST endpoints, JWT authentication with role-based access, and the security middleware around it]
#pt[Shipped a companion app on the same infrastructure, reusing the auth, security, and data layers]
#row([*Software Engineer Intern*], [May 2023 – Aug 2023])
#subrow([_Flickmatch_], [_New Delhi, India_])
#pt[Revamped Flickmatch's website end to end, turning the new Figma designs into responsive React and #box[Material-UI] components across every page]
#pt[Wrote the state management as modular pieces rather than per-page, so the same logic carried across the site as it grew]
#row([*Software Engineer Intern*], [May 2025 – Jan 2026])
#subrow([_MyYogaTeacher_], [_San Diego, CA (Remote)_])
#pt[Wrote the React Native client that streams biometric data in real time, with #box[offline-first] sync and #box[time-series] deduplication so nothing is lost when the network drops]
#pt[Shipped a #box[voice-to-SQL] pipeline on Whisper with streaming LLM responses that replaced the admin team's #box[Ctrl+F-and-edit] workflow]
#row([*Technical Officer*], [Aug 2025 – Jan 2026])
#subrow([_The AI Society at ASU_], [_Tempe, AZ_])
#pt[Mentored four freshmen through their first ML project, an emotion detection system reading facial expressions and audio cues]
#pt[Wrote the materials for and ran workshops that made machine learning approachable to students with no technical background]
#sechead[SKILLS]
#block(above: 0.30em, below: 0.02em)[*Frontend & Mobile:* React, React Native, Three.js, Blender, Figma, Tailwind, Expo, Material-UI, Vite, Recharts, Mapbox, NativeWind, Electron, iOS App Store]
#block(above: 0.30em, below: 0.02em)[*Languages:* TypeScript, JavaScript, HTML/CSS, Python, SQL]
#block(above: 0.30em, below: 0.02em)[*Backend & APIs:* Node.js, REST, Express.js, FastAPI, JWT, Flask, Bun, Hono, GraphQL, WebSocket, Role-based access control, SQLAlchemy, Uvicorn, Selenium]
#block(above: 0.30em, below: 0.02em)[*Data & Cloud:* Supabase, PostgreSQL, AWS, SQLite, MongoDB, Firebase, CUDA, Docker, CI/CD, Git]
#block(above: 0.30em, below: 0.02em)[*AI & Agents:* MCP, OpenAI API, Autonomous agents, x402, LangChain, Claude API, Whisper, Pinecone, Tool use, Prompt engineering, LLM streaming, spaCy, YOLOv8, Demucs, Gaussian Processes]
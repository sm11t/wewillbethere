# RAW PROFILE FACTS — Asmit Datta
Extracted 2026-09-02 from: resume_asmit.pdf, LinkedIn profile export, LinkedIn projects export.
This is the ground truth. Nothing here is invented. Gaps are marked [GAP].

## IDENTITY
- Name: Asmit Datta
- Pronouns: He/Him (per LinkedIn)
- Email: asmit77@icloud.com
- LinkedIn: linkedin.com/in/asmitrajeet
- Portfolio: https://www.asmit.space
- LinkedIn headline: "CS @ ASU'26 | Software | AI Infra"
- LinkedIn 2nd line: "WatchDNA | Where Time Connects Us All"
- 500+ connections, 781 followers, 90 listed skills
- [GAP] No phone number on resume
- [GAP] No GitHub link on resume or visible LinkedIn

## LOCATION CONFLICT (must resolve)
- Resume header says: New York, NY
- LinkedIn profile location: Tempe, Arizona, United States
- LinkedIn "Open to work" banner: "Tempe, AZ | On-site · Hybrid" — STALE, contradicts NYU/NYC
- Resume lists NYU M.S. CS expected 2028 → implies NYC now
- ASU BS ended May 2026; today is Sept 2026 → he has graduated ASU and started NYU

## EDUCATION
1. New York University — M.S. Computer Science, expected 2028, New York, NY
   - [GAP] No GPA, no coursework, no start date, no specific program/school (Courant? Tandon?)
2. Arizona State University — B.S. Computer Science, Minor in Business
   - Aug 2022 – May 2026, Tempe, AZ
   - Activities: Technical Officer @ AI Society of ASU
   - [GAP] No GPA listed anywhere
   - [GAP] No honors/dean's list/scholarships listed
3. Delhi Public School — R. K. Puram, High School Diploma, Computer Science, 2020–2022, Grade 93%
   - Not on resume (correct call for US resumes, but note the 93%)
- LinkedIn shows "Show all 3 educations" — third is presumably NYU

## EXPERIENCE (5 roles; resume shows only 3)

### 1. Software Engineer Intern (Capstone) — WatchDNA
- Aug 2025 – Apr 2026 (9 mos), Tempe AZ / Remote
- LinkedIn bullets:
  - Built a store locator for WatchDNA with an interactive Mapbox map, real-time filtering, an admin console for data operations, an automated endpoint discovery pipeline in Python.
  - Set up the full backend infrastructure including databases, JWT auth with role-based access and security measures and middleware.
  - Shipped a companion app on the same infrastructure, reusing the auth, security, and data layer.
- LinkedIn skills tagged: TypeScript, Node.js, +4 more
- Note: separate session context shows WatchDNA is a React Native / Expo app with Supabase (migrations, notifications), forum/community features, iOS App Store submission (App Review Guideline 2.1 correspondence), push notifications.
- [GAP] No user/scale metrics for WatchDNA
- [GAP] App Store launch outcome not captured on resume

### 2. Technical Officer — The AI Society at ASU
- Aug 2025 – Jan 2026 (6 mos), Tempe AZ, On-site
- LinkedIn bullets:
  - Created educational resources and presentations to teach AI and machine learning fundamentals to students from all majors.
  - Mentored and assisted a team of 4 freshmen through their first ML project, an emotion detection system using facial expressions and audio cues.
  - Ran workshops and study sessions that made AI approachable for students without a technical background.
- ON RESUME ONLY as a fragment inside the ASU education entry. Not a standalone role.
- HIGH VALUE for on-campus jobs (teaching/mentoring/leadership signal)
- [GAP] No headcount reached by workshops

### 3. Software Engineer Intern — MyYogaTeacher
- May 2025 – Jan 2026 (9 mos), San Diego, CA / Remote
- LinkedIn bullets:
  - Built a production React Native app for real-time biometric data with offline-first sync and time-series deduplication, hitting 99.9% uptime on flaky networks.
  - Shipped a voice-to-SQL pipeline using Whisper and streaming LLM responses that cut manual admin CTRL+F --> edit work by 60%.
- LinkedIn skills tagged: Python, spaCy, +1
- Note: spaCy appears on LinkedIn but NOT in resume skills section.

### 4. Research Study Assistant — University of Delhi
- May 2024 – Aug 2024 (4 mos), New Delhi, India, On-site
- LinkedIn: "Worked under Prof. R.P Singh on optimizing Gaussian Process Classifiers for high-dimensional data modeling."
- COMPLETELY MISSING FROM RESUME. This is real research experience — very high value for RA/on-campus research roles.
- [GAP] No results, no publication, no methods detail, no dataset

### 5. Software Engineer Intern — Flickmatch
- May 2023 – Aug 2023 (4 mos), New Delhi, India, Hybrid
- LinkedIn bullets:
  - Re-engineered web app components with Figma.
  - Designed responsive UIs with Material-UI and built modular state management logic for scalability.
- LinkedIn skills tagged: Figma, Adobe Premiere Pro, +1

## VOLUNTEERING
- Founder — CovreliefDwarka, May 2020 – Sep 2020 (5 mos), Health
- "Successfully vaccinated over 100 economically disadvantaged workers who are unfamiliar with the..." (truncated in export)
- MISSING FROM RESUME. Founder + civic impact + age 17-18. Strong differentiator/humanizer.
- [GAP] Full description truncated — need the rest

## PROJECTS (LinkedIn shows 7; resume shows 4)

### Torii — Mar 2026 – Present — https://www.asmit.space/kya
"A spending control proxy for AI agents built on the MCP protocol. Torii sits between agents and paid tools, enforcing identity, budgets, and accountability on every call."
Built the full stack in a day with Bun and TypeScript (two production dependencies):
- JWT-based agent identity linking every agent to a human owner
- Policy engine with session budgets, per-call caps, tool allowlists, and rate limits
- Pre-authorization budget tracker that reserves funds before upstream calls to prevent concurrent overspend
- SQLite audit ledger logging every tool call with block reasons and response times
- x402 payment protocol handling — proxy intercepts HTTP 402 challenges, checks wallet balance, pays on the agent's behalf, and retries automatically
- Dual-mode wallet system (simulated for testing, real USDC on Base via viem)
- Live dashboard with real-time spend tracking and agent health monitoring
- Full CLI for server management, token creation, and wallet operations
Skills: TypeScript, Bun, +5
NOTE: "Built the full stack in a day" and "two production dependencies" are strong, specific, human details currently NOT on the resume.

### LEAD ENGINE — Jan 2026 – Present — https://www.asmit.space/lead-engine
"Autonomous AI agent that discovers, scores, and generates outreach for real estate leads — 24/7, zero manual intervention."
"Scouts Zillow, Redfin, FSBO, expired MLS listings, and county records across an entire metro area. Scores every lead on a Motivation × Ability × Timeline framework, enriches with property history and equity estimates, assigns campaign types based on score tiers, and autogenerates personalized outreach drafts. Full React dashboard with pipeline views, source analytics, and backtesting against historical data."
Skills: Python, FastAPI, +9
Resume claims: 2,100+ leads sourced, ~50% AI-call conversion, 70% cut in manual prospecting, 5-stage pipeline, parallel sub-agents, Telegram alerts, interactive node graph.
NOTE: resume mentions AI voice calls; LinkedIn description does not. Backtesting + county records + equity estimates are on LinkedIn but NOT resume.

### Pash — Jan 2026 – Present — https://www.asmit.space/pash
- Full-stack audio stem isolation platform powered by Demucs v4.
- Upload any song, get back isolated vocals, drums, bass, instrumentals.
- Decoupled cloud architecture: AWS S3 storage, SQS async job queueing, remote CUDA GPU offloading for 5–10× faster processing than CPU.
- Clean drag-and-drop UI with real-time job status tracking.
Skills: React Native, Tailwind CSS, +5

### NeuroPilot — Mar 2025 – Present
- "Designed a custom AI-enhanced browser interface that streamlined user workflows by ..." (truncated)
- Skills: Electron.js, React.js, +1
- MISSING FROM RESUME

### Portfolio (asmit.space) — Feb 2025 – Present — https://www.asmit.space
- "Built and deployed a 3D interactive portfolio using React + Three.js, allowing users to explore my projects in a virtual ..." (truncated)
- Skills: Blender, React.js, +4
- Resume version: Blender-modeled room/desktop rendered with Three.js, walkable computer where every project opens as a living artifact. Resume dates it 2024; LinkedIn says Feb 2025. CONFLICT.

### SentinalAI — Feb 2025 – Present
- "Developed a computer vision–based surveillance system capable of real-time detection of..." (truncated)
- Skills: Python, YoloV8, +1
- MISSING FROM RESUME. Note spelling "SentinalAI" (likely intended "SentinelAI") — check.

### Lynti — Dec 2024 – Present
- "Developed a transportation app using React Native in an effort to digitize ride booking and ..." (truncated)
- Skills: Node.js, React Native, +5
- MISSING FROM RESUME

## SERVICES (LinkedIn "Services" section — signals breadth)
Application Development, Database Development, Web Design, Web Development, Software Testing,
Mobile Application Development, 3D Design, Video Production, Video Editing
NOTE: 3D Design / Video Production / Video Editing are non-obvious differentiators not reflected on the resume.

## SKILLS (from current resume)
- AI & Agents: OpenAI/Whisper, Claude, MCP, x402, Pinecone, LangChain, Demucs, Selenium
- Backend & APIs: Node.js, Express, FastAPI, Flask, REST, WebSocket, GraphQL, Bun, Hono
- Languages: TypeScript, JavaScript, Python, SQL, Go, Java, C++, Rust
- Frontend & Mobile: React, React Native, Tailwind, NativeWind, Three.js, HTML/CSS
- Databases & Cloud: PostgreSQL, MongoDB, SQLite, Firebase, AWS (EC2, S3, Lambda, SQS), Docker, CI/CD
Additional from LinkedIn not on resume: spaCy, Figma, Adobe Premiere Pro, Electron.js, YOLOv8,
Blender, Supabase, Mapbox, viem, Material-UI, Electron

## CONTENT / PUBLIC PRESENCE
- LinkedIn posts: "In case you're into mind reading" linking asmit.space "Reading the brain." (15 reactions, 2 comments)
- LinkedIn post on Visa backing Stripe's Machine Payments Protocol (#MPP) for card-based agent payments, linking TORII (19 reactions, 2 comments)
- Writes technical content on asmit.space. NOT on resume.
- Follows: Patrick Collison (Stripe CEO), Aman Gupta (boAt)

## ADDENDUM — pulled from asmit.space, 2026-09-02

### Torii (asmit.space/kya) — details not on the resume or LinkedIn
- Subtitle: "Know Your Agent"
- **~700 lines of TypeScript** — a real, checkable number, and a strong one
- Stack confirmed: TypeScript, Bun runtime, **Hono** framework, SQLite, JWT, USDC on **Base** chain
- Six-layer architecture: identity, policy engine, budget tracker, ledger, x402 integration, wallets
- Budget tracker uses an **atomic reserve-before-call** pattern against in-memory session state
- Policy engine is JSON: per-agent budgets, tool allowlists/blocklists, rate limits
- Dashboard: total spend, active sessions, call counts, blocked calls, per-agent spend, wallet health, call log
- His own framing, verbatim: **"The human controls policy. The agent controls execution.
  Torii is the boundary between them."** — this is his voice at its best. Use it.
- No public GitHub repo linked. Confirms the GitHub gap.

### Lead Engine (asmit.space/lead-engine) — real numbers, and a discrepancy
Live figures published on his own site:
- **2,129** total leads discovered  (resume says "2,100+" — accurate, keep)
- **83** top lead score (scoring is 0–100 with written reasoning per lead)
- **5** active scout sources
- **2,340** active campaigns
- Avg AI call duration **0:55**
- Sources named: Zillow, Redfin, FSBO, **Maricopa County Assessor**, expired listings
- Three parallel AI voice agents, named Alex, Sam, Jordan, with scripts varying by
  property, score, and motivation
- Campaign types auto-assigned by score tier: 8×8 Aggressive, 33-Touch, 12-Direct
- Backend: FastAPI, Python 3.12, SQLAlchemy, SQLite, Uvicorn
- Frontend: React 18, TypeScript, Tailwind, Recharts, Vite
- Automation: OpenClaw cron jobs, parallel sub-agents for enrichment, Telegram alerts
- Node View: live pipeline graph; failed scouts turn red immediately
- His framing: "Full transparency — every scout, lead decision, and pipeline step is
  visible; no black boxes."

**[CONFLICT — must resolve before this metric ships]** The site says **"50% Success
Rate"** on AI calls. The resume says **"~50% AI-call conversion"**. Those are not the
same claim: a call that connects and completes is not a conversion. "Conversion" is
the stronger word and is the one a interviewer will drill into. Need to know what the
50% actually counts — connected calls? completed qualifications? leads that agreed to
a callback? Until answered, this number should not ship as "conversion".

**[MINOR]** The resume says a "5-stage pipeline"; the site describes 4 stages (scout,
dedupe, AI score, AI call) plus campaign auto-assignment. These reconcile, but pick
one description and use it consistently.

**[FIX]** The public Lead Engine page lists **"Live System URL: localhost:5173/"**.
A recruiter who clicks that gets nothing. Either remove it or point it at a real
deployment or a recorded demo.

### Portfolio site structure
- asmit.space redirects to welcome.html, a "Welcome to my space" splash with an
  "Enter (fullscreen recommended)" button before the 3D experience loads.
- **[RISK]** The content is behind a click-through into a Three.js scene, so it is not
  readable by a crawler, and a recruiter with 20 seconds may not get past the splash.
  A plain-HTML `/resume` or `/about` route with the same content as text would fix
  both problems without touching the 3D experience.
- Pash's page (asmit.space/pash) currently renders only the title "Pash - Stem
  Separation" with no body content. Needs filling in.

## CORRECTIONS FROM ASMIT — 2026-09-04

Employer locations, stated directly. These override the LinkedIn export.

- **WatchDNA is in Ontario, Canada.** The LinkedIn export lists the role as
  "Tempe, Arizona, United States · Remote", which was *his* location while
  working, not the company's. A resume names the employer's location, so the
  entry now reads "Ontario, Canada (Remote)".
- **MyYogaTeacher is in San Diego, California** — "San Diego, CA (Remote)".
- Flickmatch (New Delhi, India) and University of Delhi (New Delhi, India) were
  already correct.
- The AI Society at ASU stays Tempe, AZ — it is an on-campus role.

## PROFILE-WIDE GAPS TO FILL BY ASKING
- [GAP] Phone number
- [GAP] GitHub URL
- [GAP] NYU program (Courant vs Tandon), start date, GPA, coursework
- [GAP] ASU GPA, honors, scholarships, dean's list
- [GAP] Work authorization / visa status (F-1? OPT/CPT? US citizen?) — CRITICAL for on-campus job eligibility & federal work-study
- [GAP] Federal work-study eligibility
- [GAP] Whether he wants NYU on-campus roles, off-campus internships, or both
- [GAP] Target role types (SWE, ML, infra, research, TA/CA, IT help desk)
- [GAP] Availability / hours per week
- [GAP] References
- [GAP] Any awards, hackathons, competitions
- [GAP] Any publications
- [GAP] Languages spoken (Hindi? Bengali?)
- [GAP] Full CovreliefDwarka description
- [GAP] Truncated project descriptions: NeuroPilot, SentinalAI, Lynti, Portfolio

# Bain — GenAI / AI-ML Engineering Intern

**On the merits this is the closest posting to what he actually builds.** It is
also the one where the gap between what he has done and what the profile can
currently prove is widest, so read the gaps section before sending.

## Where he is genuinely strong

Their bullets, matched to real work:

| Their requirement | His evidence |
|---|---|
| Agentic patterns: context management, tool integration, orchestration, memory/state | **Torii.** MCP proxy between agents and paid tools, per-session budget state, tool allowlists, rate limits. This is the requirement, almost verbatim. |
| Guardrails, fallbacks, **human-in-the-loop** | **Torii again.** "The human controls policy. The agent controls execution." A policy engine plus a human owner is exactly an HITL guardrail. |
| Observability: automated scoring, **policy iteration loops** | Torii's SQLite ledger records every call and every reason one was blocked, surfaced on a live dashboard. That is GenAI observability. |
| Tool use, function calling | MCP is the tool-integration protocol; x402 handles paid tool calls. |
| Complex multi-stack GenAI from conception to production | Torii and Lead Engine, both solo, both end to end. |
| GenAI application / workflow automation in production | **MyYogaTeacher voice-to-SQL** - Whisper plus streaming LLM, shipped, replacing a real admin workflow. This is the only *shipped-at-a-company* GenAI item and it is easy to overlook. |
| Evaluation design, automated scoring | Lead Engine scores every lead on a written framework with the reasoning recorded. |
| Python and APIs (REST) | FastAPI, four Python entries. |
| Classical ML | **Delhi** - Gaussian Process classifiers. Their bullet says "classical ML and deep learning"; the classical half is real and evidenced. |
| Communicate to non-technical audiences | **AI Society** - taught ML to students with no technical background. Their bullet asks for exactly this. |

## The gaps — do not paper over these

**Retrieval is the big one.** They ask for RAG, embeddings, hybrid retrieval and
reranking. In `profile.yaml` all of `RAG`, `Vector search`, `Embeddings` are
`ask: true` with nothing behind them. **Pinecone is the one honest adjacency** -
it is a vector database and it is on his own resume, so it is his claim to
stand behind. It stays; the other three do not get promoted onto the page for
this posting, however well they would match.

This is the sharpest test the system has had. The posting asks for the exact
words he has not earned, and putting them on the page would produce an
interview that opens on retrieval architecture. **Ask him first.** If he has
actually built a RAG pipeline, that changes this application more than any
other single answer.

**Fine-tuning / PEFT** - no evidence anywhere. Not claimed.

**Engineering practices** - they want testing, code review, CI/CD, performance
profiling. Git and CI/CD are self-reported from his old resume; testing and code
review are unconfirmed. These are open questions in `checklists/recover.md`
under WatchDNA, and answering them would strengthen this application directly.

**Deep learning** - thin. YOLOv8 sits in the SentinalAI stub, which has no
usable description. Two sentences about SentinalAI would add a real deep
learning item.

**Strong academic performance** - they ask for it explicitly, and the ASU GPA is
still unknown. If it is 3.5 or above it should be on this resume.

## Recommendation

Send it, and prioritise three answers first: RAG/retrieval, the WatchDNA
engineering-practice questions, and the GPA.

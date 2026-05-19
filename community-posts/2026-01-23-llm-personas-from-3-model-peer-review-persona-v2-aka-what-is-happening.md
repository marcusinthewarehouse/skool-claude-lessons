# LLM Personas: from “3-model peer review” → persona v2 (aka: what is happening 😅)

**Created:** 2026-01-23
**Upvotes:** 1
**Comments:** 0
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/llm-personas-from-3-model-peer-review-persona-v2-aka-what-is-happening

---

I built a peer-to-peer skill review setup that pulls in 3 LLMs \(Opus, Gemini, and ChatGPT\) to review my code/design changes. It helped a lot — but I realized I needed consistent distinction in what each model was responsible for… so I made Persona v1.

Persona v1 was basically:

[ul][li]Architect[li]Hostile SRE[li]Pragmatic Builder\(and for brainstorm: Architect / Skeptic / Scaler\)

It worked… but I quickly realized it was way too basic for production-grade output. I was still getting generic advice and still occasionally drifting or rebuilding stuff I swear I already built.

So now I’m on Persona v2. I’ll be honest: I have no idea what half of these titles mean, but all 3 models keep telling me this is what’s required if I want planning + implementation + rollout to be 10x smoother with way less drift / “going in circles”:

Persona v2 \(production-grade apparently\):

[ul][li]Structure Analyst: where this belongs, canonical location, does it need an ACR[li]Dependency Mapper: blast radius, coupling, import graph[li]Pattern Enforcer: Golden Rules, StageRunner, secrets, verification loops[li]Domain Guardian: protect boundaries \(no “utils dumping ground”\)[li]Integration Architect: data flow, contracts, idempotency/dedupe[li]Reliability/SRE: failure modes → remediation → escalation packet[li]Security: secrets/PII/audit trails

Big shift I’m pairing with this: I’m moving away from “chat memory” and toward repo-backed memory + deterministic context packs \(Memory Queue → promote to STATE / GOLDEN_RULES / SOLVED_PROBLEMS\), plus enforcement in infra \(pre-commit + PR gates + nightly drift checks\).

If it works the way they’re claiming, I should spend less time re-deriving decisions and finally making more automations that make my day-to-day business easier…

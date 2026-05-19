# How do you QA non-deterministic agent outputs?

**Created:** 2026-05-11
**Upvotes:** 1
**Comments:** 5
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/how-do-you-qa-non-deterministic-agent-outputs

---

Building multi-agent workflows for two different projects right now, one for short term rental ops and one in esports ed. Same problem in both: when behavior shifts run to run, how do you actually verify quality without manually reading every output? I've been doing eyeball checks plus a few cheap heuristics \(does the output have X field, is the length sane\), but neither scales as the agent fleet grows. Curious what's actually working for people. Structured eval suites, a separate model scoring outputs, golden examples with similarity thresholds, something else?

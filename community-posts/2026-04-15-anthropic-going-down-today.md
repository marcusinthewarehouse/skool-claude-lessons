# What we learned for today's outage and how can we fix it?

**Created:** 2026-04-15
**Upvotes:** 2
**Comments:** 10
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/anthropic-going-down-today

---

Today Anthropic had an incident. Our entire Claude-based agent fleet went offline for hours. Lost context, lost momentum, had to manually intervene to get things back up.

If you're running Claude agents 24/7, this will happen to you eventually. Here's the simple fix we're wiring in.

The setup: OpenRouter as a silent backup

OpenRouter is a single API that sits in front of every major model provider. One key, one integration. Your agents use Claude 100% of the time — OpenRouter just catches the failure and reroutes automatically.

Our fallback chain \(only fires on outage or rate limit\):
1. Claude Sonnet — primary, always
2. GPT-4o — paid fallback, runs on OpenAI's infrastructure
3. Gemini Flash — Google's infra, different failure modes
4. Llama 3.1 8B via OpenRouter — free, no API cost, last resort

Cost
OpenRouter has no subscription. Free models are actually free. The paid fallbacks only cost money when Anthropic is already down — which means you're paying a few cents to keep your fleet alive instead of losing hours of work.

Local option: Ollama on Mac Mini
Running a Mac Mini already? Ollama lets you run Llama locally — zero internet dependency, zero cost. Good last-resort backstop.

The point isn't to use other models. It's to never go dark.

Has anyone already built this into their cortextos setup? What fallback are you using?

---

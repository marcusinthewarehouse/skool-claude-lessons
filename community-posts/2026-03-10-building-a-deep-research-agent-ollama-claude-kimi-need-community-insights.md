# Building a Deep Research Agent: Ollama + Claude + Kimi (Need Community Insights)

**Created:** 2026-03-10
**Upvotes:** 2
**Comments:** 1
**Labels:** 59ef34684a11462bac017ad7f612ac9d
**Post URL:** https://www.skool.com/agent-architects/building-a-deep-research-agent-ollama-claude-kimi-need-community-insights

---

I'm currently working on a Deep Research use case using Ollama + Claude + Kimi \(K2.5 cloud\) and would love to get some advice from the community.

I already have an existing codebase that I plan to extend for this workflow.

A few questions I’m exploring:

• Claude Code appears to natively support deep research workflows. For custom research pipelines, is it recommended to extend the built-in capabilities, or build a separate orchestration layer?

• In Codex, I noticed there is a websearch tool available for agents. Is there something similar when working with Ollama / Claude environments, or is the recommended approach to integrate an MCP server \(for web search / browsing\)?

• For those who have built deep research agents, what architectural patterns worked best for you?
– planner / executor agents
– iterative search → summarize loops
– retrieval + reasoning pipelines

My goal is to build a reliable research pipeline that can:

1. Explore a topic
2. Collect sources
3. Synthesize insights
4. Generate structured reports

Would really appreciate any professional tips, architecture suggestions, or tooling recommendations from people who have built similar systems.

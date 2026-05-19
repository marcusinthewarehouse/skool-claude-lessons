# Claude Managed Agents deep dive doc

**Created:** 2026-04-19
**Upvotes:** 8
**Comments:** 6
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/claude-managed-agents-deep-dive-doc

---

Anthropic just launched Claude Managed Agents in beta. It is basically their hosted platform for running persistent AI agents via API. You give it a model, a system prompt, and tools, and it spins up an isolated cloud container for your agent to work in. Full filesystem, bash access, Python, Node, git, web search, MCP servers, the whole thing. Sessions persist across multiple turns so your agent can actually work through long multi-step tasks without losing state.

Just put together a full technical reference for it since the docs are scattered.

It covers the full API \(agents, environments, sessions, vaults\), all the event types, how to wire up custom tools and MCP servers, callable sub-agents for multi-agent coordination, and complete code examples in Python and TypeScript.

At the end there are 3 real multi-integrated examples: an autonomous daily reporting fleet, a competitive intelligence pipeline that fires on GitHub events, and a PR review system that conditionally deploys to staging.

API only, no UI yet. Requires the beta header to access. Worth understanding now before it opens up.

Doc here: [https://docs.google.com/document/d/1B0S_SttcroXzG76Nu__l3ExksY3difNs/edit?usp=sharing](https://docs.google.com/document/d/1B0S_SttcroXzG76Nu__l3ExksY3difNs/edit?usp=sharing)

# Claude Code /schedule guide — 3 overnight workflows ready to paste

**Created:** 2026-04-17
**Upvotes:** 4
**Comments:** 3
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/claude-code-schedule-guide-3-overnight-workflows-ready-to-paste

---

Just dropped a setup guide for Claude Code's /schedule feature. Here is everything you need to actually use it.

/schedule lets you save a Claude Code configuration — prompt, GitHub repos, MCP servers, secrets — and run it automatically on Anthropic's infrastructure. Your laptop does not need to be open.

How to set it up:
Type /schedule in any Claude Code session, or /schedule + description like "/schedule daily PR review at 9am" to pre-fill. Walk through: name it, write the prompt, select repos, set the trigger. Saves immediately to claude.ai/code/routines.

Three trigger types:
Schedule — standard cron expression \(0 2 * * * for 2am nightly\). Minimum interval is 1 hour. Cannot run more frequently than that.
API — generates a unique HTTPS endpoint + bearer token. POST to it from anywhere and the routine fires. Body can pass context variables your prompt reads.
GitHub — fires on pull_request, push, merge, or release events. You filter which events and which repos.

Important: schedule triggers can be configured from the /schedule CLI. API and GitHub triggers must be set up in the web UI at claude.ai/code/routines.

MCP servers:
You can attach remote MCP servers to a routine — they are available to Claude during the run. Local MCP servers do not work because the routine runs in Anthropic's cloud, not on your machine. Use HTTP or SSE transport for any MCPs you want available. Add credentials for each in the secrets section.

Secrets:
Encrypted environment variables you add at claude.ai/code/routines. Available to Claude at runtime as $KEY. Use for API keys, tokens, webhook URLs — anything your prompt or MCPs need.

Prompts:
Write them like instructions for someone who cannot ask follow-up questions. No back-and-forth during a run. Claude runs fully autonomously — no approval prompts, no interactive session. Be specific about what to do when things are unclear.

Branch permissions:
Claude pushes to claude/-prefixed branches by default. Unlock other branch patterns in routine settings if your workflow needs it.

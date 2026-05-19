# Allow nested sub agents in Claude code

**Created:** 2026-03-16
**Upvotes:** 4
**Comments:** 1
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/allow-nested-sub-agents-in-claude-code

---

I’m sharing here in case this is useful for anybody else.

Claude blocks creating instances of itself in shell beyond the normal subagent tool…. Unless you call it via a script and unset the CLAUDECODE env var. This way you can have infinitely nested subagents and teams.

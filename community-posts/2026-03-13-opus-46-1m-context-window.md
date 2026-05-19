# Opus 4.6 1M Context Window

**Created:** 2026-03-13
**Upvotes:** 7
**Comments:** 7
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/opus-46-1m-context-window

---

The last Claude Update made the 1M context version of Opus 4.6 the default. This was originally released only for the API and, to my knowledge, required extra usage if you wanted to use it in the CLI. It made me wonder what kind of value it provides in practice, and how the rate of quality degradation differs between 0-200k and 200k-1M tokens. Interested in hearing about your experiences with it and whether it's materially changed anything for you guys.

I've been experimenting with adding token-efficiency instructions in the CLAUDE.md file to get more out of each session and see how much of a difference it makes. I've been testing it with the memory management skill [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) put together. Excited to try it with a much bigger context window to really push what you can get out of a single session while maintaining decent quality. Below is an example of what I've added to [CLAUDE.md](http://CLAUDE.md) files if you guys want to test it out. I've found myself making different versions of it depending on the work and tools.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Context Efficiency

### Subagent Discipline

**Context-aware delegation:**
- Under ~50k context: prefer inline work for tasks under ~5 tool calls.
- Over ~50k context: prefer subagents for self-contained tasks, even simple ones — the per-call token tax on large contexts adds up fast.

When using subagents, include output rules: "Final response under 2000 characters. List outcomes, not process."
Never call TaskOutput twice for the same subagent. If it times out, increase the timeout — don't re-read.

### File Reading
Read files with purpose. Before reading a file, know what you're looking for.
Use Grep to locate relevant sections before reading entire large files.
Never re-read a file you've already read in this session.
For files over 500 lines, use offset/limit to read only the relevant section.

# Just found a tool worth knowing about: context-mode

**Created:** 2026-03-14
**Upvotes:** 6
**Comments:** 9
**Labels:** 59ef34684a11462bac017ad7f612ac9d
**Post URL:** https://www.skool.com/agent-architects/just-found-a-tool-worth-knowing-about-context-mode

---

Here's the full revised post:

---

Just found a tool worth knowing about: context-mode

It's an MCP server for Claude Code that solves two problems most of us hit constantly.

Problem 1: Context bloat
Every time Claude reads a file or fetches a URL the raw output dumps straight into your context window. One Playwright snapshot can be 56 KB. A few of those and your session is toast.

Context-mode intercepts those calls and runs them in a sandbox. Only the relevant output comes back. They showed 315 KB compressed to 5.4 KB in one example.

Problem 2: Session loss after compaction
When your context compacts Claude forgets everything. Context-mode logs every file edit, git op, task, and decision to SQLite then indexes it with BM25 search. When a new session starts it pulls back only what's relevant instead of dumping everything.

---

Here's where it gets interesting for those of us running persistent agents:

Claude Code cron jobs max out around 72 hours. So if you're running a long-lived agent — something that monitors messages, runs heartbeats, and handles tasks around the clock — you have to restart the session on a timer to avoid hitting the limit unpredictably.

The pattern: hard-restart every 71 hours. The agent reloads its bootstrap files, recreates its crons, and picks back up via memory files. Clean slate, known state.

Context-mode could make that handoff significantly cleaner. Instead of relying on a memory file bootstrap sequence, it retrieves exactly what's relevant from the SQLite index via BM25 search. You may also be able to extend the useful session window and restart less often.

We're running both on a local project right now to measure the actual context savings and see how they interact before going wide.

---

Install is one line:
claude mcp add context-mode -- npx -y context-mode

Repo: [github.com/mksglu/context-mode](http://github.com/mksglu/context-mode)

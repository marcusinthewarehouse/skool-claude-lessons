# The Memory Bridge: Cross-Instance Context Handoff

**Created:** 2026-03-07
**Upvotes:** 4
**Comments:** 7
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/the-memory-bridge-cross-instance-context-handoff

---

Following up on my shutdown sequence post about how I handle memory not just between sessions, but across different Claude instances.

The shutdown sequence helps preserve context when a session ends. But what happens when you’re working across [Claude.ai](http://Claude.ai), Claude Code on your laptop, and Claude Code on a remote VM? They don’t share memory. Each one starts cold.

I built a shared memory bridge to fix that.

How It Works

Two tables in a Supabase Postgres database: `memories` and `session_summaries`. Every Claude instance connects to the same database via MCP. That’s it. That’s the infrastructure.

When an instance starts a session, it queries the most recent summaries to pick up context from wherever I left off, regardless of which surface I was using. During a session, decisions, blockers, and progress can be logged. When a session wraps, a summary gets written.

The key design choice: **nothing gets written automatically.** I decide when to persist. If I’m just doing a quick lookup or brainstorming, that doesn’t need to survive. If I’ve made real decisions or progress, I tell the instance to write a summary to the bridge.

The instance will sometimes suggest a write if we’ve covered something substantial. That’s a nice middle ground. It prompts, I decide.

Why Not Auto-Capture?

Most of the memory tools I’ve seen \(memory-mcp, session handoff protocols, etc.\) try to capture everything automatically – after every response, on compaction, at session end. The problem is noise. If you auto-capture everything, the next instance wastes tokens parsing context that doesn’t matter. You end up with the same bloat problem that context windows already have, just in a different location.

Human-gated writes keep the bridge lean. Only signal, no noise.

The Pattern

The concept isn’t complicated. A shared database that multiple AI instances can read from and write to, with a human controlling what gets persisted.

If your AI workflow touches more than one surface, a bridge like this is worth the 30 minutes it takes to set up.

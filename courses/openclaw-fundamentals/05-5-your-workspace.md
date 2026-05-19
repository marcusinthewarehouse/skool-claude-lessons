# 5. Your Workspace

**Course:** OpenClaw Fundamentals (3/3/26)
**Skool URL:** https://www.skool.com/agent-architects/classroom/da68c6be?md=bf6c0994daf84d01bedd6314122e68b3
**Video ID (Skool):** 0d6f21571e36417f8c1ee7f391bc3758
**Scraped:** 2026-05-19

---

Your workspace is the set of markdown files that define who your agent is, what it knows, and how it behaves. Everything your agent does starts here.

**The bootstrap files (loaded every session):**

- **AGENTS.md** - Your agent's primary instruction set. Priorities, boundaries, workflow rules. The most important file.
- **SOUL.md** - Personality, voice, temperament, and non-negotiable constraints.
- **USER.md** - Your preferences, communication style, and recurring constraints.
- **IDENTITY.md** - Your agent's name, role, and goals.
- **TOOLS.md** - Environment-specific details like paths, aliases, and device names.

**The memory system:**

- **MEMORY.md** - Long-term curated knowledge your agent reads at every session start.
- **Daily logs** - Append-only journals in the memory/ folder, auto-loaded for today and yesterday.
- **memory_search** - Semantic + keyword hybrid search across all indexed memories.

**Built-in tools:** File read/write/edit, shell commands, memory search, web search, browser automation, messaging across all channels, sub-agent spawning, and cron scheduling.

The more context you give your agent through these files, the better it performs. Customize them to make it yours.

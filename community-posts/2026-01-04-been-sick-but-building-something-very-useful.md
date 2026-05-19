# Been Sick, But Building Something Very Useful

**Created:** 2026-01-04
**Upvotes:** 5
**Comments:** 14
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/been-sick-but-building-something-very-useful

---

Hey everyone, wanted to pop in and apologize for being MIA the past few days. The flu has absolutely wrecked me and I'm still recovering, but I've been using my couch time productively to work on something I'm really excited to share with you all.

I've been building out what I'm calling a Claude Code OS. It's a continual learning and memory system that lets Claude actually remember and grow across sessions, with persistent memory through time and the ability to continue learning as you and Claude Code work together. The core problem I'm trying to solve is, how do you give an AI agent persistent, searchable memory without blowing up your context window every time it needs to recall something?

The core of the system is a branching tree of folders that lives in ~/.claude/skills/. This is the actual memory. Inside each skill folder you can have as many nested folders as you need to capture the domain knowledge. When a skill folder gets too deep, you can create nested folders, but Claude only auto-discovers top level [SKILL.md](http://SKILL.md) descriptions. For nested folders, the folder name IS the description, so you name them descriptively like "authentication-oauth-jwt-sessions" instead of just "auth".

For organization there's a max 10 folders per parent rule. When you're about to add an 11th child folder, the system compacts first by grouping the existing 10 into 5 semantic pairs, creating parent folders for each pair, then adding your new folder as the 6th. This keeps the tree scannable and prevents sprawl at any level.

Memory operations themselves run as background subagents. When Claude needs to store or recall knowledge, it spawns a subagent that first reads [MANIFEST.md](http://MANIFEST.md), which shows the full skill tree structure. The subagent navigates to the right location, does the read or write, and returns just the result with full file paths so the main agent can dive deeper if needed. The main conversation never blocks on memory housekeeping.

The piece I'm actively building out is the linking system. Right now files can use @link references to connect related knowledge, and subagents follow these links when traversing memory. But what I really want is something closer to Obsidian style backlinks where if Claude learns something about one topic that's also related to another, those memories get connected even though they live in different skill folders. The vision is that when Claude focuses on a single note, it can see the linked notes in first degree, second degree, and so on without having to search through everything.

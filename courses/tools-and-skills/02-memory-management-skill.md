# Memory Management Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=5902689dc9124a6689234cc018830479
**Scraped:** 2026-05-19

---

A Claude Code skill that optimizes the native auto-memory feature. It teaches Claude to treat MEMORY.md as a concise index rather than a dump, keeping your context lean and ensuring nothing important gets lost beyond the 200-line system prompt limit.

## How Claude Code's Native Auto-Memory Works

Claude Code introduced auto-memory in version 2.1.59. Unlike CLAUDE.md files that you write and maintain manually, auto-memory consists of notes Claude writes for itself based on what it discovers during your sessions.

### Where It Lives

Each project gets its own memory directory at ~/.claude/projects/<project>/memory/. The <project> path is derived from the git repository root, so all subdirectories within the same repo share one auto-memory directory. Git worktrees get separate memory directories. The directory contains a MEMORY.md entrypoint and optional topic files like debugging.md, architecture.md, and patterns.md.

### The 200-Line Limit

The first 200 lines of MEMORY.md are loaded into Claude's system prompt at the start of every session. Content beyond line 200 is silently ignored. Topic files like debugging.md or patterns.md are never auto-loaded - Claude must read them on demand using its file tools when it needs the information. This is the critical constraint the skill is designed around.

### What Claude Remembers

As Claude works, it may save project patterns (build commands, test conventions, code style), debugging insights (solutions to tricky problems, common error causes), architecture notes (key files, module relationships, important abstractions), and your preferences (communication style, workflow habits, tool choices). You can also tell Claude directly: "remember that we use pnpm, not npm" or "save to memory that the API tests require a local Redis instance."

### Managing Auto-Memory

Auto-memory is enabled by default. Use the /memory command during a session to open the file selector, which shows your auto-memory entrypoint alongside your CLAUDE.md files. The /memory selector also includes a toggle to turn auto-memory on or off. You can disable it globally by setting "autoMemoryEnabled": false in ~/.claude/settings.json, or per-project in .claude/settings.json. The CLAUDE_CODE_DISABLE_AUTO_MEMORY environment variable overrides all other settings.

## The Problem This Skill Solves

Out of the box, Claude has no rules about how it organizes its auto-memory. It tends to dump everything into MEMORY.md - bug fixes, commands, patterns, architecture decisions - all in one growing file. Once it crosses 200 lines, the overflow becomes invisible at session start. You lose context without knowing it.

## How This Skill Improves on Native Functionality

This skill adds five key behaviors that Claude does not do on its own:

1. Index-based architecture: Forces MEMORY.md to act as a concise index with pointers to topic files, not a monolithic dump. Commands, file paths, and topic pointers stay in MEMORY.md. Detailed content goes into dedicated files.
2. Line count enforcement: Claude checks wc -l before writing to MEMORY.md and automatically moves content to topic files when approaching 180 lines, preventing silent overflow past the 200-line limit.
3. Topic file routing: Defines clear categories - debugging.md for bug solutions, patterns.md for code conventions, gotchas.md for known issues, architecture.md for system design, decisions.md for why-we-chose-X records. Each entry uses a structured format with Context, Problem, and Solution fields.
4. Grep-first recall: Teaches Claude to search topic files with grep before reading them whole, minimizing context window usage. Instead of loading an entire debugging.md, Claude searches for the relevant keyword first and reads only the matching section.
5. Memory hygiene protocol: Includes pruning rules (remove entries older than 90 days if unreferenced), consolidation of duplicates, archiving of completed project phases, and weekly audit prompts to keep memory clean and current.

## Installation

Clone the repo, then choose how to install based on how broadly you want it applied:

1. Clone the repo: git clone [https://github.com/grandamenium/claude-code-memory-skill.git](https://github.com/grandamenium/claude-code-memory-skill.git)
2. Choose your install method:
3. Single project - Copy CLAUDE-SNIPPET.md contents into your project's CLAUDE.md or .claude/CLAUDE.md
4. As a rule file - Copy memory-management-rule.md to your project's .claude/rules/ directory
5. All projects globally - Add the snippet to ~/.claude/CLAUDE.md so it applies everywhere
6. Optionally, copy MEMORY-TEMPLATE.md into your project's memory directory as a starter [MEMORY.md](http://MEMORY.md)

---

GitHub Repository: [https://github.com/grandamenium/claude-code-memory-skill](https://github.com/grandamenium/claude-code-memory-skill)

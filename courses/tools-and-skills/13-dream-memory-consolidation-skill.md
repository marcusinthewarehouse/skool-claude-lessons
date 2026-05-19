# Dream - Memory Consolidation Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=c093731f23c54ff69513dd09ad85e7a7
**Scraped:** 2026-05-19

---

Anthropic is building an auto-dream feature into Claude Code that consolidates your agent's memory like how your brain does during sleep. It's currently unreleased and behind a feature flag. This skill replicates that functionality today - drop it in and your agent's memory stays clean, current, and contradiction-free.

## How It Works

When you use Claude Code across many sessions, auto-memory accumulates noise: stale facts, contradictions, relative dates that lose meaning. Dream fixes this with a 4-phase consolidation pass:

- Phase 1 - Orient: Reads your current memory directory to understand what exists
- Phase 2 - Gather Signal: Scans session transcripts for corrections, preferences, decisions, patterns
- Phase 3 - Consolidate: Merges new info, resolves contradictions, converts relative dates to absolute
- Phase 4 - Prune & Index: Rebuilds [MEMORY.md](http://MEMORY.md) as a lean index under 200 lines

## Features

- Auto-triggers every 24 hours via native Claude Code Stop hook
- Auto-detects your memory system (native Claude Code, OpenClaw, or custom)
- Self-onboarding: walks you through setup then deletes onboarding instructions
- Zero overhead when conditions not met (10ms check on session exit)
- Resolves contradictions, converts relative dates, removes stale references
- Includes test suite to verify consolidation results

## Installation

```
git clone https://github.com/grandamenium/dream-skill.git ~/.claude/skills/dream
```

---

GitHub Repository: https://github.com/grandamenium/dream-skill

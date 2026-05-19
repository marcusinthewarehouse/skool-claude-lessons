# New Skill: Dream - Memory Consolidation for Claude Code

**Created:** 2026-03-24
**Upvotes:** 9
**Comments:** 18
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/new-skill-dream-memory-consolidation-for-claude-code

---

Anthropic is building a currently unreleased auto-dream feature into Claude Code that consolidates your agent's memory like how your brain does during sleep. It's unreleased and behind a feature flag. I built my own version that works today.

The problem: after 20+ sessions, your auto-memory fills with noise. Stale facts, contradictions, relative dates that mean nothing a week later. Your agent starts making worse decisions because its memory is lying to it.

Dream fixes this with 4 phases:
- Orient: reads your current memory to understand what exists
- Gather Signal: scans session transcripts for corrections, preferences, decisions
- Consolidate: merges new info, resolves contradictions, converts relative dates to absolute
- Prune: rebuilds your index clean, under 200 lines

Note: this skill is built for your normal single-session Claude Code workflow, sitting on top of Claude Code's native memory system. If you're running multi-agent setups like CortextOS or OpenClaw, those have their own memory architectures. This is for the everyday Claude Code user who wants cleaner memory without building a custom system. That said, it does have built-in memory system detection, so if you want to integrate it on top of a custom setup you can.

It also auto-triggers every 24hrs via a native Stop hook, auto-detects your memory system, and self-onboards with step-by-step setup.

Install:
git clone [https://github.com/grandamenium/dream-skill.git](https://github.com/grandamenium/dream-skill.git) ~/.claude/skills/dream

Then open Claude Code and run /dream to try it.

Who's been dealing with noisy agent memory? What's your current approach to keeping it clean?

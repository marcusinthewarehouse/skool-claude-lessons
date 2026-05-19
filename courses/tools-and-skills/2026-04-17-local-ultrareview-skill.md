# local-ultrareview Skill (4/17/2026)

**Date:** 2026-04-17
**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=749153e2e31944a6b73dcf5a01b1d7f7
**Scraped:** 2026-05-19

---

A local replication of Claude Code's /ultrareview with two additions: live agent logs and an implementation plan.

What it does:

- 3 Opus agents run in parallel (correctness, security/performance, architecture) — each writes a live log file you can watch in real time

- Synthesis agent combines all three reviews

- Implementation plan agent writes exact files, exact changes, exact order of operations

- Main agent asks if you want to apply the fixes — if yes, applies them and asks to commit, re-PR, or merge

Install:

Drop SKILL.md in .claude/skills/local-ultrareview/

Run with /local-ultrareview or /local-ultrareview PR#123

Repository: https://github.com/grandamenium/local-ultrareview

Community post: https://www.skool.com/agent-architects/local-ultrareview-skill-live-logs-implementation-plan

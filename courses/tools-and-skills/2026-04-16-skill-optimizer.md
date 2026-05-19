# Skill-Optimizer (4/16/2026)

**Date:** 2026-04-16
**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=b740fb42dd6641dc806909a6617a834f
**Scraped:** 2026-05-19

---

Skill-Optimizer automatically audits and improves your Claude Code skills by reading JSONL transcripts and scoring each skill across 5 dimensions. Run it after any agent session that used a specific skill.

What it scores:

- Did the skill trigger for the right reason?

- Did the agent follow every step in the right order?

- Were the tool calls and scripts used correctly?

- Did scripts run clean without errors?

- Did the output match what the skill was supposed to produce?

Each dimension scores 1-10. Total out of 50. It writes three files:

- analysis.md: what worked, what failed, root cause

- diff.patch: exact line-level changes to apply to the SKILL.md

- history.json: every run scored so you can track improvement over time

The loop: Run audit, apply the diff, run the skill again, run the audit again. The score either went up or it did not.

Install:

git clone https://github.com/grandamenium/skill-optimizer ~/.claude/skills/skill-optimizer

Usage:

Tell Claude Code: "audit [transcript path] against [skill path]"

GitHub: https://github.com/grandamenium/skill-optimizer

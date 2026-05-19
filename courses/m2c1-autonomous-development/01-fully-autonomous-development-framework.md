# Fully Autonomous Development Framework

**Course:** Fully Autonomous Development Framework
**Skool URL:** https://www.skool.com/agent-architects/classroom/5e51e7e0?md=f69d6d1ff4b14a50adb0826230d07229
**Resource:** [M2C1 Skill](https://github.com/grandamenium/m2c1)
**Scraped:** 2026-05-19

---

M2C1 (measure twice cut once) is a Claude Code skill that turns your brain dump into fully built, tested, and deployed software. You describe your idea, and it handles everything else through coordinated AI subagents.

### What It Does

The framework runs a 12-phase orchestration workflow. It converts your idea into a structured PRD, deploys parallel research subagents, asks you detailed discovery questions, configures all tools and MCP servers, creates a master implementation plan, shards it into individual task files, reviews them for coherence, then autonomously executes every task with comprehensive testing at every level.

### The 12 Phases

1. Setup - Creates orchestration folder structure
2. Brain Dump to PRD - Synthesizes your idea into a structured spec
3. First Research Wave - Parallel subagents research every domain
4. Discovery Questions - Detailed Q&A to clarify all decisions
5. Second Research Wave - Implementation-focused research
6. Tool Setup - Configures MCP servers, API keys, services
7. Tool Verification - Tests every tool and integration
8. Skill Creation - Creates project-level skills for each domain
9. Context Compact - Refresh context (all state is in files)
10. Master Plan - Implementation plan with tasks and dependencies
11. Task Sharding - Expands each task into a self-contained agent prompt
12. Final Artifacts - Creates progress tracker, orchestrator, and project config

After setup completes, run /start and the orchestrator autonomously executes every task with full testing.

### Key Principles

- Every artifact has a template
- Parallel by default - subagents run in background wherever independent
- Multi-angle testing at every level
- Human-emulating testing via Playwright
- Tool-aware - researches and configures MCP servers and CLIs
- Generalizable - works for SaaS, API, CLI, mobile, and more

### Installation

Clone the repo and copy into your Claude Code skills directory:

```
git clone https://github.com/grandamenium/m2c1.git
cp -r m2c1/ ~/.claude/skills/m2c1/
```

Claude Code will auto-discover the skill. Just describe your project idea and the 12-phase workflow kicks off automatically.

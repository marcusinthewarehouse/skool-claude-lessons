# Autoresearch-Anything Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=9b275cdf81d940958ac74096edd81954
**Scraped:** 2026-05-19

---

Apply Andrej Karpathy's autoresearch pattern to ANY business metric. This skill sets up an autonomous experimentation pipeline where your Claude Code agent modifies something (email copy, landing page, ad creative), measures the result against an objective metric, keeps the change if it improved, discards it if it didn't, and repeats forever. You wake up to a log of experiments and better results.

## How It Works

The core loop follows Karpathy's exact keep/discard pattern: the agent reads all context (experiment history, accumulated learnings, knowledge files), forms a hypothesis, modifies the experiment file, commits, deploys, waits for the measurement window, measures the metric via API, then makes a binary decision. If the metric improved, keep the change and advance. If not, discard and revert. The system can never go backwards. Over dozens or hundreds of experiments, small wins compound.

## The Problem This Skill Solves

Running experiments manually is slow. You write a new email variant, deploy it, wait a day, check the results, decide if it worked, then repeat. Maybe you run one test per week. This skill automates the entire cycle so your agent runs experiments 24/7 while you sleep. Karpathy ran 126 experiments overnight on his ML model. You can do the same for your reply rate, conversion rate, or any other API-measurable metric.

## What This Skill Does For You

- Guided Q&A setup that scopes your specific pipeline (metric, platform, constraints, measurement window)
- Deep research on your domain before the first experiment - seeds your knowledge base
- Generates a complete project scaffold with Karpathy-style program.md, config, and connector stubs
- Builds the real measurement and deployment connectors WITH you during setup
- Three immutable knowledge files (user knowledge, research findings, constraints) that the agent always respects
- Compounding resource.md that logs both positive and negative learnings from every experiment
- Persistent execution via launchd + tmux (local) or GitHub Actions (cloud) - your choice
- Notification support for Telegram, Slack, or terminal

## Installation

Clone the skill into your Claude Code skills directory:

```
git clone https://github.com/grandamenium/autoresearch-anything.git ~/.claude/skills/autoresearch-anything
```

Then invoke the skill in Claude Code:

```
/autoresearch-anything
```

The skill will walk you through the entire setup process - from choosing your metric to launching the autonomous loop.

---

GitHub Repository: https://github.com/grandamenium/autoresearch-anything

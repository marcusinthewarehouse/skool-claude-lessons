# Multi-Agent OpenClaw Setup Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=eb019d786feb4f12b95bbbd6cf1d485a
**Scraped:** 2026-05-19

---

An OpenClaw skill that walks you through creating and managing multiple agents from a single gateway instance. Instead of running everything through one monolithic agent, you can split workloads into specialized agents - each with its own workspace, personality, model, channel bindings, and tool permissions. This skill covers the complete workflow from planning your agent architecture to having multiple bots running on Telegram.

## What This Skill Teaches

- Creating new agents with openclaw agents add (interactive and non-interactive modes)
- Setting up agent workspaces with AGENTS.md, SOUL.md, and [IDENTITY.md](http://IDENTITY.md) persona files
- Creating dedicated Telegram bots per agent via BotFather
- Configuring channel routing and binding precedence rules
- Understanding workspace isolation, shared vs local skills, and session stores
- Per-agent model selection (e.g. Sonnet for chat, Opus for deep work)
- Per-agent sandbox and tool restrictions for security isolation
- Inter-agent messaging configuration
- Common multi-agent patterns: personal/work split, orchestrator + specialists, channel-based personas
- Troubleshooting routing, workspace, and credential issues

## How It Works

By default, OpenClaw runs a single "main" agent. This skill teaches you to add additional isolated agents using the openclaw agents add command. Each agent gets its own workspace directory containing persona files (AGENTS.md for instructions, [SOUL.md](http://SOUL.md) for personality, [IDENTITY.md](http://IDENTITY.md) for visual identity in the Control UI). You configure routing bindings in openclaw.json to direct inbound messages from specific channels, accounts, or even individual peers to the correct agent. The skill includes three reference docs covering Telegram multi-bot setup, workspace architecture, and routing/binding precedence.

## How It Improves on Native Functionality

OpenClaw supports multi-agent natively, but the docs are spread across multiple pages and the configuration has many moving parts. This skill consolidates everything into a single guided workflow: agent creation, workspace setup, Telegram bot creation, channel routing, binding precedence, credential isolation, shared vs local skills, sandbox configuration, and inter-agent messaging. It saves you from trial-and-error by explaining the binding precedence order (peer > guild > account > channel > default) and common gotchas like credentials never being shared automatically between agents.

## Installation

Clone the repo into your OpenClaw workspace skills directory:

```
git clone https://github.com/grandamenium/multi-openclaw-agents.git ~/.openclaw/workspace/skills/multi-openclaw-agents
```

Or install into global skills (shared across all agents):

```
git clone https://github.com/grandamenium/multi-openclaw-agents.git ~/.openclaw/skills/multi-openclaw-agents
```

Once installed, ask your OpenClaw agent to help you set up a new agent and it will use the skill to guide you through the entire process step by step.

---

GitHub Repository: https://github.com/grandamenium/multi-openclaw-agents

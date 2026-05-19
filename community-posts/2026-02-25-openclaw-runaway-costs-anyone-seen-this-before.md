# OpenClaw runaway costs - anyone seen this before?

**Created:** 2026-02-25
**Upvotes:** 2
**Comments:** 6
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/openclaw-runaway-costs-anyone-seen-this-before

---

I’ve been running OpenClaw for about a month without issues, but last week I ran into a major usage spike and I’m trying to track down the cause.

I had 16 subagents running Opus 4.6 for short deep-research tasks \(expected ~5 minutes each\). Later that day my Anthropic usage jumped to $100+ per day.

Actions I took:
[ul][li]Stopped all cron jobs and background workflows[li]Reduced heartbeat from every 5 minutes to every 30 minutes[li]Moved heartbeat to local models on my Mac Mini[li]Set Sonnet 4.6 as default and only use Opus 4.6 explicitly

Even after this, I’m still seeing unexpected burn - roughly $10 every 30 minutes during normal use.
Before I wipe everything and rebuild from scratch, I’m hoping for a sanity check:

Has anyone experienced:
[ul][li]Orphaned cron jobs or background agents continuing to run?[li]Hidden OpenThreads or loops?[li]A good way to audit which models are actually being called and why?

Context:
[ul][li]Interfaces: Signal, Discord, Telegram[li]Considering a full reset \(export memory, rebuild clean instance\)[li]Also unclear how the Claude Code $200 plan interacts with API usage

Main goal: identify where the usage is coming from and put guardrails in place.

Any advice or debugging approaches would be appreciated.

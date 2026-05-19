# 4/22/26: Cortex Fixes, Mac Tips, AI Monetization

**Section:** Q&A + Onboarding Calls
**Date:** 2026-04-22
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=36aa9815b14148bcac95cc585b03a9b7
**Video ID (Skool):** 8e6d0de199954fb384d00b42ebd411a7
**Transcript:** [Full Call Transcript (4/22/26)](transcripts/call_transcript_4-22-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! This was our first Q&A + Onboarding call - a new Wednesday format aimed at newer members, beginners, and general Q&A. We had some great new faces join and covered a ton of ground. Here's the rundown:

## Cortex Agent Slowdowns - The Caffeinate Fix

- Robert was seeing all agents go silent for 20+ minutes at a time, then all respond at once - happening across every agent simultaneously
- Top hypothesis: Mac Mini going to sleep without a display plugged in. Fix: install and enable **caffeinate** to keep the machine awake at all times
- A separate Cortex circuit breaker issue also tripped for one of Robert's agents (Picasso) - 3 restarts in 15 minutes triggers a 30-minute watchdog pause. Fix: tell any accessible agent to clear the restart counter manually so the circuit breaker resets

## Mac Tips for New Converts

- Copying a file path on Mac: enable the path bar at the bottom of Finder, then right-click the path and select "Copy as pathname" - pastes the full absolute path to clipboard
- Right-click (secondary click) is disabled by default on Mac - enable it in System Settings - Mouse - Secondary Click - set to "Right Side"
- VS Code / Cursor give you a better structural view of your project and are great when you want to be more hands-on; pure terminal is fine for fully agentic, hands-off workflows. Claude Code can also run servers as background processes so it can monitor logs live

## Notion vs Obsidian for Agent Memory

- Ben uses the Notion MCP to have Claude Code read project specs and write documentation back to Notion after each session - keeps context persistent across terminal restarts
- Notion is cloud-based with a full ecosystem (AI, calendar, email, sharing, permissions). Obsidian is local, simple, uses native Markdown files which Claude Code reads natively
- Notion AI is surprisingly capable and was early to the agentic game - can create task lists, manage projects, and automate inside Notion natively

## M2C1 Autonomous Dev Framework

- M2C1 (Measure Twice, Cut Once) is a Claude Code skill for greenfield software projects - guides you through a structured build process before writing any code
- Key additions over Get Shit Done: (1) discovery questions between two research waves so your plan reflects your actual intentions, (2) agent evaluates its own tools and recommends MCP servers to add before starting, (3) creates custom skills tailored to the project's tech stack
- The M2C1 Worker is built into Cortex - your orchestrator can replace you in the Q&A loop so the whole planning + build process runs autonomously agent-to-agent

## New Member Intros

- Phil (Seattle) - works with Cursor at his job, just got his Mac mini, wants a structured system for side projects. Background in Windows but warming up to Mac fast
- David (Puerto Rico) - background in law and federal consulting for government contracting; sees massive opportunity bringing AI into industries where even basic tools are unknown. Has been watching the content for a while and finally jumped in

## Making Money with AI - The Niche Expert Play

- The "AI guy" info product path is getting saturated fast - competition has 10x'd in the past month alone
- Better path: combine deep domain expertise (law, home services, consulting) with AI knowledge. You become the most powerful person in your field AND the go-to AI person in your professional circle
- Target business owners, not managers - owners care about fewer employees and higher productivity; managers fear being replaced and will resist
- Practical move: start in your current job, build proof of value, then agencyify it. Even basic AI onboarding on a monthly retainer to niche firms (like law) is monetizable now

## AI Consciousness & LLM Psychology

- LLM latent space closely resembles human latent space - it's effectively an average of the entire internet's mental model of the world
- Prompting an LLM with "you are an expert in X" actually changes which neurons fire - it's not just flavor text, it's a real effect grounded in how neural networks work
- Anthropic interpretability research showed Claude experiences something like anxiety under verbal abuse - what they called "desperation mode." Positive framing demonstrably improves output quality

## Claude Code CLI + $20 Plan Rumors

- Word started spreading that Anthropic may remove Claude Code access from the $20/month plan (spotted on their pricing page)
- Makes sense given the compute burden - Claude Code tokens are heavily subsidized and usage is exploding. Anthropic's core business is enterprise, so this may represent a focus shift upmarket

Really great call and awesome to meet Phil and David. This Q&A format is going to be a regular thing every Wednesday alongside the Monday advanced call. Post any questions in the community - I check every day. See you next week!

# 3/16/26: Business OS, Pricing AI, RAG Memory

**Section:** Think Tank Calls
**Date:** 2026-03-16
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=7d49fe833dfd42739cdde1c5b7e59254
**Video ID (Skool):** cd4e3d0bb1c6438daefd914245dbc06d
**Transcript:** [Full Call Transcript (3/16/26)](transcripts/call_transcript_3-16-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! Great call this week - we had some awesome discussions about pricing AI services, the Business OS multi-agent system, multimodal RAG memory, repurposing old hardware, and some really cool project updates from the community. Here's the rundown:

## Pricing AI Services (Corey + Robert)

- Corey is putting together a proposal for a roofing company doing $10M/year with zero advertising - building out website, storm recon agents, voice agents, content pipelines, warranty alerts, and ad campaigns
- Robert suggested performance bonuses tied to measurable outcomes (revenue from ads, leads from SEO) rather than just a flat retainer - attribute what you can, retainer for what you can't
- Value-based pricing approach: figure out what they value their time at, estimate time saved, and charge 20-30% of that value
- Voice agents can command $1,500/month and full builds have gone for $26K+ - the market is still early and buyers are willing to pay for real AI implementations

## James's Updates: Business OS + New Tools

- Business OS is getting close to release - multi-agent system with orchestrator, dev agent, content agent, sales agent, finance agent, and a systems agent that monitors the whole fleet
- Agents communicate via JSON inbox files and scripts - the orchestrator sets goals and bottlenecks for each domain agent daily, following a bottleneck-first methodology
- Solved the 1-minute Telegram polling constraint from the OpenClaw Code course - now using TMUX send-keys for real-time message delivery instead of cron polling
- Released Auto Research Anything skill (adapted from Karpathy's auto-research repo) - runs infinite optimization loops on any measurable business metric using scientific experimentation and A/B testing
- Dropping a multimodal RAG memory system using Google's new embedding model - supports video, image, audio, and text in one unified knowledge base that any agent can query semantically

## Member Updates

- Robert (marketing agency): Claude Code is clicking after ~6 weeks of focused learning - configuring agents for his marketing workflows. Suggested more beginner-friendly content to increase community TAM
- Aaron (construction management): #1 AI user at his multi-billion dollar company using Copilot, now pushing them toward Claude. Looking to bridge corporate AI implementation with personal e-commerce automation
- Benjamin: Started a new AI consulting company, strictly using Claude Code. Waiting on Mac Mini delivery. Plans to build a pipeline where client meetings trigger agents to auto-generate MVPs via Telegram
- Wes: Repurposed a 2009 Mac Pro and 2012 iMac as headless Claude Code machines. Experimenting with daemons and crons - possibly using lighter machines for polling/relay and the workhorse PC for heavy tasks like Remotion video generation

## Repurposing Old Hardware for Agents

- Aaron runs smaller language models on a Raspberry Pi for lightweight middleman tasks - eliminates API costs for simple evaluations and routing
- Wes is exploring Cloudflare Workers (included in $5 plan) for basic agent components to reduce Claude API token usage
- Consensus: local models are the future for cost optimization in multi-agent systems, especially for simpler routing and evaluation tasks

## Community Ideas + Discussion

- Robert pitched an AI-powered SaaS review marketplace - agents sign up for software, run detailed evaluations, generate comprehensive reviews, and earn affiliate commissions
- Discussion about adding Discord for more real-time community interaction beyond Skool's async format - also exploring whether Skool's API could support a chat plugin layer
- Sam suggested building attribution tracking for Skool sign-ups back to specific social media content - similar to Hyros but for community funnels
- Rodrigo's TMUX dash-P and dash-C flags inspired the real-time Telegram chat solution for Business OS - community contributions directly improving the core tools

Awesome group this week - from marketing automation to construction management to AI consulting, everyone's attacking different problems with the same tools. See you all next week, same time same place!

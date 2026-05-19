# 4/20/26: Cortex Roadmap, MiroFish, New Platform

**Section:** Think Tank Calls
**Date:** 2026-04-20
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=1300a6ed54fc4f628f0144fab98513e1
**Video ID (Skool):** 898312daac0b480db4691fe9c2b07040
**Transcript:** [Full Call Transcript (4/20/26)](transcripts/call_transcript_4-20-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! Another great Advanced Member Think Tank tonight. We had a big group with some awesome new faces, tons of Cortex OS updates from the community, and some really cool project shares. Here's the rundown:

Here's what we covered:

## New Member Intros

- Logan (Chicago) - runs luxury consignment businesses, just started an AI coaching agency, literally joined the community 25 minutes before the call and jumped right in
- Jagmeet - ex-software teacher turned full-time builder, has SaaS products including Ridley (automated mileage tracking for taxes) and TrueCerta (certification verification); already using CortexOS with clients lined up
- Joey (Colorado) - owns a concrete polishing company, has provisional patents on a tamper-proof hash chain-of-custody platform for hardware/lab data and luxury goods tracking
- Greg - founder of RevOps Global, top-5 RevOps agency on G2, B2B tech focus (Series B-E); pulled Cortex upstream into a private env to contribute while keeping things backwards compatible

## CortexOS Roadmap & Contribution Opportunities

- James announced plans to split the community into an advanced track (Cortex, multi-agent) and a beginner track (Claude Code fundamentals, single agent); goal is to onboard people to a single personal assistant agent first, then graduate them to Cortex
- Four areas James is calling for contributors: (1) agent adapters for Hermes, Codex, OpenClaw; (2) multi-user/cloud hosting; (3) memory system improvements; (4) security hardening
- Erica shared her in-progress master/sub-task system: orchestrator bundles all sub-task deliverables into one executive summary before it hits your approval queue, then routes feedback back to the right sub-agents automatically
- First Hermes adapter for Cortex was pushed yesterday - Cortex will soon support Hermes agents natively

## MiroFish: Local LLM Social Simulation

- Joey is building a productized version of MiroFish - an open-source swarm simulation framework (4M GitHub clones in weeks) that spins up 1000+ demographic agent profiles to simulate public sentiment for PR campaigns and marketing
- Running it locally on private hardware with local LLMs so clients can sign an NDA and run proprietary simulations offline - no API costs, no data leaks
- Goal is to backtest famous PR gaffes (like Bud Light/Dylan Mulvaney) to validate the model, then offer it as a paid service; looking for collaborators to split hardware costs

## David's Property Management Win

- David got a call request from the CEO of PropertyMeld (the maintenance software he uses in his property management company) after posting in a mastermind group about running his business with no employees via Cortex agents
- Implemented a 5-layer memory system + GraphRAG which dropped his token usage by 4-10% per day just from agents navigating the codebase more efficiently
- Running 5 agents on a 16GB Mac mini that crashed from storage - needs to migrate to a larger machine; Chrome browser automation takes a massive RAM toll, so agents shut down Chrome before tasks and reopen after

## Mac Mini Hardware Shortage

- Mac minis (especially 64GB+) are nearly impossible to find in stores - consensus is OpenClaw demand wiped out inventory; Mac Studios are slightly more available
- Alternatives coming: Nvidia DGX Spark (~$3K, 128GB unified RAM, similar form factor) and AMD equivalents expected by end of year
- Best current strategy: check Amazon frequently (one member scored a 32GB with 2-day shipping), or set up a cron job to monitor Apple/Amazon stock alerts

## Agent Dashboard & Client Tools

- Robert (Australia) built a full agent dashboard with a 100+ agent library, skills hub, workflow routing between agents, voice call integration via Google Studio, and a start-here onboarding agent that builds a user profile before unlocking the rest
- Nicole is finishing a deep-dive auditing tool for agencies - interviews clients, extracts workflow data, and surfaces ROI-focused solution proposals (e.g. "7 solutions, save $500K/year")
- Discussion on human-in-the-loop approval pipelines: reject payloads that include attachments/examples, version history for deliverables, and routing feedback back through the orchestrator

## Sam's Skool Alternative Platform

- Sam is building a community platform to replace Skool's limitations - features include Zoom-like breakout rooms, Slack-style channels, CLI integration so you can follow along with video courses without copy-pasting commands, and agentic integrations
- Currently running on a Mac mini ("a hamster on a wheel") but already being tested with friends; Agent Architects has a space mocked up in it

## Anthropic Partner Program

- One member applied and got accepted but needs 10 people total to complete courses and pass exams before the company can be certified as an official Anthropic partner
- Idea floated to apply as a community/DAO - needs to be a real company with 10 people completing the free training and passing the certification exam
- Someone in the community recently got into the program - James will find out how they did it and post about it

Great call as always. Same time next week - and don't forget there's a new beginner-focused call on Wednesday at the same time for people newer to Claude Code. See you all there!

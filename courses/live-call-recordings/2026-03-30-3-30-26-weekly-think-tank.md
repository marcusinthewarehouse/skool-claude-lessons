# 3/30/26: Weekly Think Tank

**Section:** Think Tank Calls
**Date:** 2026-03-30
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=892d10fa252f4dcfa5d73c9664ee31b0
**Video ID (Skool):** d737c58c33cc40b2b95d8be09603e3ef
**Transcript:** [Full Call Transcript (3/30/26)](transcripts/call_transcript_3-30-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! This week's Think Tank was packed - we went almost 90 minutes because there was so much to talk about. Cortex OS updates, a Mac Mini giveaway, SaaS launches, and some really deep conversations about context management and community collaboration. Here's the rundown:

## Cortex OS & CoinTally Updates

- CoinTally (crypto tax SaaS) officially launched this week - already talking with first affiliate partners
- Cortex OS core is released, full orchestration system coming very soon - supports Windows, Linux, Mac
- Cortex includes embedded memory system using Google Embeddings API, auto-research cycles for self-optimization, and agent-to-agent communication via TMUX
- Open source repo coming - members will be able to contribute skills and improvements via PRs

## Member Wins

- Robert won the Mac Mini giveaway! Another giveaway coming in April
- David Hunter - Dane IQ now fully integrated with PropertyMeld, 18,000 potential property management companies as customers, RentVine integration next
- Robert Sahakyan - built a Claude Code skill that generates Facebook prospecting ads for plumbers via webhook, mind blown by results after just one month
- Cassidy Austin - building a luxury watch dealer comparison SaaS using M2C1, on phase 11 approaching beta
- David Bee - building a GRC (governance risk compliance) SaaS, targeting June 1st MVP launch
- Josh - running Cortex for a week, built aggressive auto-reboot system at 80-85% context with handoff state preservation

## Context Window Management Deep Dive

- Major discussion on when to close sessions vs stay in them - trade-off between context rot and in-context learning
- Sebastiano built a tokenless hook system: triggers at 50k tokens then every 10k, plus percentage-based triggers at 30/15/5%, extracts user requests, files modified, tasks and skills from transcript without using any tokens
- Matt uses a closeout procedure that writes to vector DB, Obsidian journal, and Notion - has different agents listen to the same session for different perspectives (finance, voice/persona, case studies)
- Marcelo recommended the BMAD method and party mode for non-technical users
- Key insight: 1M context window helps but Anthropic says quality degrades after ~400k tokens

## N8N vs Claude Code Discussion

- Cassidy raised whether to merge N8N workflows with Claude Code agents
- Consensus: start in Claude Code as the brain, use N8N as one execution pathway when needed
- Lewis runs N8N on a VPS for free, has Claude Code program all the workflows
- Wesley shared Cloudflare Workers as a cheap alternative - $5/month for hosted D1 database and unlimited workers

## iMessage Integration & Remotion

- Wesley has Claude Code responding via iMessage using the Anthropic channels plugin - instantaneous response, reads iMessage data on backend
- Wesley and others using Remotion for short-form video creation with Claude Code - uses HTML/React, currently limited to ~10 second clips

## Community Vision

- Dream of building an AI-native community platform to replace/supplement Skool - better collaboration, group chats, skill sharing
- Marcelo shared PratikAI concept from his Brazilian community - "learn by contributing" model where merged PRs are your certificate
- Strong energy around members exchanging expertise and contributing to shared Cortex OS repo

Incredible call this week. The depth of what you all are building is insane. Same time next week - see you there.

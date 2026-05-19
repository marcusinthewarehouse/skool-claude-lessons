# 4/13/26: Memory, Productizing Cortex, Local AI

**Section:** Think Tank Calls
**Date:** 2026-04-13
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=5bb8f3079d2e40578db9ecd864e33af4
**Video ID (Skool):** 46016a8f1192439fbfb5c430fc8e5a57
**Transcript:** [Full Call Transcript (4/13/26)](transcripts/call_transcript_4-13-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! Another packed Think Tank tonight - we went long because there was so much to get into. Context management headaches, how people are productizing Cortex, open source local models, and a big community design conversation. Here's the rundown:

Here's what we covered:

## Cortex OS Roadmap & Context Optimization

- Main focus for the next Cortex push is context consumption optimization - currently even the 200 max plan is not enough when running multiple agents
- Sean's Lex agent announces its context status out loud and handles soft resets - going to try building similar automatic context awareness into Cortex by default
- The tension: you can set context reset thresholds low (safer, but too many resets) or high (agent starts losing itself). The dream is seamless auto-optimization that you never notice
- I ship-first-optimize-later - so token usage wasn't great in the initial release. That is being actively worked on

## Member Intros

- Bradley - FedCon.com, helps SMBs win government contracts. Team of 25, 7-18 people now on Claude Code. Runs long overnight sessions and wants Telegram control from anywhere
- Brandon - fresh CS grad riding the AI curve, jumped in after the memory systems content on Instagram
- Rodrigo - Brazilian agency running Cortex/co-work setups for clients via Tailscale + VPS + Docker. Revenue has already 2x'd this year

## Memory Systems Deep Dive

- The classic tradeoff: automatic memory burns context, manual memory means you only use it when you remember to - neither is what we actually want
- Obsidian + markdown files is still close to the gold standard - portable across Claude, Codex, Hermes, OpenClaw because it is not tied to any harness
- Hermes is shipping hard on memory - best post-agent harness reviews the past few weeks
- NotebookLM is still the easiest plug-and-play "second brain" when you have a big corpus to search, because Google has already done the indexing and retrieval engineering for you
- Supabase + Gemini 2 embeddings is the cloud-hosted path that a few members have moved to. Beats local Postgres on Railway that one member watched almost corrupt itself
- Andrej Karpathy's Obsidian second brain and Graphify are both great starting points if you want to play with this
- Thinking about recording a full course on AI memory fundamentals - episodic vs short-term vs long-term - if that is something people want, post about it in the community

## What Everyone's Running

- My setup: 7 agents named after characters with profile pictures. Orchestrator, a personal assistant named Donna (after Suits) wired to Gmail, Google Drive, contacts, and a flight API, plus a Recall integration so she can actually place AI phone calls - got my contacts prescription refilled by agent last week
- Recall is the phone-call API worth looking at - 18 cents/minute, the person on the other end usually cannot tell. Others mentioned BrightCall and ElevenLabs under the hood
- Compliance flag: unsolicited outbound AI voice or SMS is basically a lawsuit magnet in the US (TCPA). Stick to inbound or existing-customer use cases. Australia's rules are stricter but clearer

## Analytics Storage + Local Stack

- Supabase for most people - cheap, Postgres, edge functions. David is moving off Railway/Neon to Supabase plus Cloudflare
- DuckDB for column-store analytics (Parquet in, OLTP, open source) if you are doing real analysis
- Cloudflare D1 + Workers - $5/month and basically unlimited for small automations. Great for CRM-to-ad-platform data pipes
- Facebook Ads and Google Ads both have dev APIs you can wire directly into your own DB - no Airtable rate limit pain

## Cursor Is Claude Code, Frontier Labs Are Absorbing Everything

- The leaked gist today basically outed Cursor's Composer as a Claude Code rebrand - surprising nobody
- Anthropic released Agent Manager (enterprise Cortex-ish), a co-work product, and the leaked software dev tool. OpenAI is building a "super app" in the same shape
- My read: any non-frontier-lab AI tool company's days are numbered. Cortex will eventually get absorbed too - but because it is open source, hackable, and harness-agnostic, it will stay ahead at the experimental edge longer than a closed product can
- Cortex is a harness of harnesses - built around Claude Code CLI in a PTY pane, but the plan is to support Codex, Hermes, OpenClaw, and whatever comes next all sharing the same task system and dashboard

## Local Models & The Open Source Future

- Qwen 27B trained on 4 trillion tokens was basically a gift to humanity - the 20:1 token-to-parameter ratio is insane compared to what they had any incentive to do. The team that pulled it off has since left Alibaba
- TurboQuant, RotorQuant, KV cache compression - the X crowd dedicated to local AI is getting models runnable on MacBooks and even Raspberry Pis
- Sean's property management angle: for sensitive data (SSNs, tenant info), the only real long-term play is local/on-prem models. The free models will be good enough by the time the big labs commoditize what we are building
- Mythos model card from Anthropic basically confirms labs are gatekeeping stronger models. Open source + local is how we keep riding the wave
- Leaked Claude Code was clean-room rewritten in Rust in under 2 hours - so DMCA does not apply. Someone triggered the whole rebuild from a plane between SF and Korea. Wild

## Productizing Cortex - Niche Down

- David (property management) - selling Dane IQ to a 240-company mastermind, pitching "own your own data" rather than SaaS. Already closed a few deals, got pulled to dinner by four prospects after one talk. Maintenance director turned AI OS for property managers
- Brett - agency targeting creatives, wellness, coaches. Onboarding wizard asks what tools they already use, provisions Cortex in the cloud, they plug in their Telegram token and Anthropic key
- Key insight from David: build the BRAIN that drives their existing software, do not try to rebuild their software stack yet. Property management is 20-software stacks glued together - that is the opportunity
- Riches are in the niches. Pick one, become THE person in it, build a small product. You do business with people, not companies
- David's onboarding wizard idea for Cortex per-niche is good - let us think about making niche-specific onboarding wizards part of the framework

## Security, Secrets, and Tailscale

- Rodrigo's stack: Tailscale VPN, VPS (32GB / 8 vCPU for ~$400-500 per 2 years), Docker containers per service, Postgres + pgvector, each co-worker runs Cortex/Claude locally and talks to the shared infra via the private network. WhatsApp as the front-door in Brazil
- Tailscale should probably be a default for Cortex - near-zero friction, much more secure
- The open problem: secrets management. How do agents authenticate to 20 services without the secrets touching Anthropic servers or getting leaked - while still letting the agents actually do their jobs. Privacy vs agency is the tradeoff

## Community Direction

- Sean's pitch: a PR hook that auto-surfaces everyone's Cortex customizations for me to review and pull into the shared repo. Tempting. Nervous about removing the choice to keep something private
- Pulling the trigger on a Discord or Slack - Skool engagement drives discovery, which is why I've held off, but the friction for collaboration is getting too high
- Erica's suggestion: tier the community into beginner and advanced, two calls a week, different energies. Going to seriously consider it
- Counter-point from the group: don't dilute the advanced content - the people here now are here because I don't talk down to them. Keep the niche
- Weekly Cortex update post incoming - things I am shipping plus what everyone else is building
- If you want to collaborate on anything Cortex-related, DM me or post - I would rather ten of us work on one thing well than all of us reinvent the same wheel

Big shout-out to Erica for the Windows PR - crushing it. Cassidy, thanks for the reminder about why this community feels different. Daniel, glad you stuck around from the "nerdy guy who talks too fast" era.

Same time, same place next week. Full transcript attached below.

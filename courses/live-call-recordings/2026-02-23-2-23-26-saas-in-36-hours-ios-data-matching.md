# 2/23/26: SaaS in 36 Hours, iOS, Data Matching

**Section:** Think Tank Calls
**Date:** 2026-02-23
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=59bc76378f94483a8f1d3c3d2017e39e
**Video ID (Skool):** 6c3d8130371d42fe823cd1344435aa75
**Transcript:** [Full Call Transcript (2/23/26)](transcripts/call_transcript_2-23-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! Just wrapped up another great community call and wanted to share the highlights for those who couldn't make it. We had a really valuable discussion this week covering everything from building full SaaS apps overnight with Claude Code to the challenges of iOS vibe coding, enterprise data matching solutions, and upcoming community hackathons. Great energy from both returning members and newcomers.

Here's a rundown of what we discussed:

## Building a Full SaaS App in 36 Hours with MCPs

- James shared a breakthrough experience: duplicating his CoinTally crypto tax software for the TikTok Shop market in just 36 hours using Claude Code
- Connected Claude Code with Supabase MCP (database), Stripe MCP (payments), Railway MCP (deployment), Playwright MCP (browser testing), and PostHog MCP (user monitoring)
- The key unlock was giving Claude Code browser access to human-facing dashboards (Stripe, Supabase, Railway) - not just MCP APIs - so it could fully configure deployments and payments autonomously
- Used the GSD (Get Shit Done) context engineering framework to structure tasks, with Claude Code making atomic commits and running integration tests at every step
- The takeaway: the limitation is agent configuration and tools, not Claude Code itself - it's smart enough to build production-ready deployed SaaS apps

## Hotel Data Matching at Scale

- Christopher is building a hotel data matching tool that compares a 3 million hotel database against client databases with confidence scoring
- Ran into Supabase storage limits when trying to load 41GB of data - traditional RAG wasn't cutting it for structured location data matching
- Kenji (CTO at Grey Whale) jumped in with expert advice: for ranking/matching structured data at scale, look at Voyage AI (MongoDB's embedding system) or specialized ranker structures instead of traditional RAG
- Christopher also automated a daily report pipeline: SQL scripts pull data at 7am, push to Supabase, then update Google Sheets the whole company monitors

## Skills Architecture and Content Automation

- Daniel shared his journey mastering Claude Code skills - building nested skills with bash scripts and Python inside, creating a self-recycling PDF factory that auto-generates and pushes content to landing pages
- Consensus on content automation: AI-generated content still lacks human soul, and platforms like YouTube are aggressively demonetizing lazy/unauthentic automated content
- The recommended approach: build near-fully automated content pipelines with one efficient human-in-the-loop review step
- Skills as the core architecture for agents - nested skills let you compose complex workflows from individual tool-specific skills (e.g., Supabase + Calendar + Brave Search combined into a workflow skill)
- Strong advice from the group: pick one tool/stack, master it, and resist AI tool FOMO - Claude Code is still king for coding agents

## Codex vs Claude Code and Privacy Concerns

- OpenAI's Codex app is impressive and sometimes solves harder bugs better than Claude Code, but Claude Code feels faster and more agile day-to-day
- Warning from Kenji: OpenAI has changed their terms of service - code submitted through Codex is no longer guaranteed private and may be used for training
- Broader trend: social media platforms (Spotify, etc.) are all updating ToS to claim rights over user content for AI training
- Claude Code in the Claude Desktop app now has a beginner-friendly UI with full terminal-equivalent features - great option for people uncomfortable with the terminal

## iOS Vibe Coding: The Swift Challenge

- Benjamin built a full iOS app in 15 minutes using Claude Code + Xcode MCP - it automatically built, launched the simulator, and even did UI testing by clicking buttons
- Kenji dropped a major insight: no LLM (not even Opus 4.6) is trained on Swift 6.0 - they all max out at Swift 5.10, making native iOS the hardest vibe coding target
- Workaround: force your Xcode project to use an older Swift version in project settings, or use React Native/web wrappers for cross-platform instead of native Swift
- BitRig (built by the SwiftUI team) was mentioned as a native on-device iOS vibe coder, though it only handles UI, not business logic
- AppWrite recommended as a Supabase alternative with native client libraries for almost every platform and excellent auth mechanisms

## Domain Experts Building Their Own Software

- Kincaid runs a co-working space for biotech companies and is exploring how non-coding scientists can use Claude Code to build their own analysis tools
- His head of EH&S spent 4-5 months in Lovable building custom inspection software that's better than anything on the market - now transitioning to Claude Code
- The gap between domain experts and software developers is now essentially closed - if you know the domain, you can build better software for yourself than hiring a developer
- Community evolution coming: structured opportunities for AI coders in the community to work with businesses looking to onboard into the AI-native world

## Hackathons and Community Updates

- Community hackathons are coming soon with rewards and networking opportunities
- No tool restrictions - use whatever tools, skills, and orchestration you want. The only benchmark is the final product
- Daniel shared a cautionary tale about a hackathon in another community that forced a specific tool nobody liked - our hackathons will be tool-agnostic
- M5 Macs with integrated TPUs are crushing local AI model performance - Kenji recommends doing pre-coding with local MLX-optimized models to save tokens on cloud models

Great call all around. Same time, same place next week. Drop any questions or projects you're working on in the community. We all love seeing what everyone's building.

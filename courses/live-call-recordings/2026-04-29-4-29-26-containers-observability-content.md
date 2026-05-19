# 4/29/26: Containers, Observability, Content

**Section:** Q&A + Onboarding Calls
**Date:** 2026-04-29
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=3d4e36782a0645ff96dc0dd998be3d30
**Video ID (Skool):** 237ba3237e2b4cd5aad641ae8e9d5bee
**Transcript:** [Full Call Transcript (4/29/26)](transcripts/call_transcript_4-29-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! This week's Q&A + Onboarding call ran wide - Cortex bugs and student-budget workarounds, Docker containerization for new members, a really impressive observability dashboard Sebastiano demoed, plus a content workflow walkthrough and a horror story about Claude Code wiping a whole working directory. Here's the rundown:

## Cortex Bugs + Student-Budget Workarounds

- Robert's M2C1 orchestrator wasn't spawning the worker - waiting on a usage reset and reinstalling RTK-AI to help. RTK-AI summarizes bash commands so Claude can troubleshoot them, but it's experimental and probably not the cleanest fix.
- Cortex now uses a daemon + Node PTY instead of Tmux so Linux and Windows users are supported, but that means you can't attach to terminals anymore. Workaround: have one agent inspect another agent's JSONL transcript to peek at tool calls.
- Better Claude-Code-style observability inside the Cortex dashboard is high on the priority list - rebuilding tool-call streaming UI is a lot of work but worth it.
- Rich (student plan) wired up an automatic fallback from Cloud Pro to Codex once usage runs out. Good pattern for anyone not on Max.

## Containerization for Beginners

- Robert wants a Docker template for Cortex on Mac so installs aren't raw on the host machine - if anything gets compromised, you don't lose everything. I agree this is super important for new members and don't have one yet, but it's going on the list.
- Docker containers give you an isolated shell and filesystem by default. You can hand out scoped permissions to specific folders if you want, but you have to set that up manually - the default is full isolation.
- Sebastiano runs full software projects in dev containers so he can install/test freely without polluting his host, then share the container if it works on any machine. For non-project work he just uses his terminal directly.
- Beginner ask that I'm prioritizing: a centralized marketplace of skills, slash commands, and tools that's actually synced to Cortex. Right now it's spread across the Tools and Skills classroom and other places.

## Memory Stack: Obsidian, Graphify, Supabase

- I've moved off Obsidian for personal use - now using Graphify on the codebases that the agents work in, plus my Cortex dashboard's deliverables viewer. But Obsidian is still a great functional solution for beginners and pairs really well with Graphify.
- Memory Palace (Mempalas) is actually based on the human memory technique that Sherlock Holmes uses - a Soviet actress adapted it to AI. The rooms-and-locations concept maps surprisingly well to agent memory.
- Ben uses Supabase for production memory because it ships with auth out of the box, which saves a ton of time if you're building a web app. For personal/local knowledge, Obsidian is still fine - Supabase makes more sense when multiple people or production systems are involved.
- Gemini Embeddings 2 is what I use and it's incredibly cheap - fractions of a cent per day. If you're hitting "out of tokens" errors, just connect a billing account and you're set.

## Sebastiano's Cortex Observability Dashboard

- Built on Grafana + Victoria Metrics in a Docker volume. Splits usage by project, eventually by agent, with cost breakdowns, turn counts, and a one-shot success metric so you can tell how often agents nail tasks without retries.
- Pulls data from two sources: JSONL transcripts (so you can backfill historical data) and OTEL telemetry (only collects from when you turn it on). Has a button that auto-sets the env vars and toggles debug mode for you.
- Includes an Experiments page - tag a project path or time window and measure the actual impact of skill/tool/harness changes. Cortex agents can run their own experiments against this data, no extra LLM cost since it's all scripts.
- Pricing pulled live from the Anthropic API with exchange rate conversion for non-US users. Status-line bridge captures the actual Cloud Max usage limit data that OTEL doesn't expose. Supports Codex, OpenRouter, and Cursor too.
- Plan is to provision pre-built dashboards stored in GitHub so users don't have to build their own panels. This is a much more robust version of the Cortex analytics page I started - definitely want to integrate it once it's stable.

## James's Content Workflow

- Daily scrape automation pulls news sources, competitors, trending GitHub repos, etc. An agent summarizes everything against my voice and prior content, then surfaces 6 topic ideas. I pick 4.
- Each of the 4 topics goes through a research phase (Haiku models for the bulk extraction) then a script-generation skill (Sonnet models) that drafts an outline in my voice. I rarely follow them verbatim but they're great for ideas.
- For Instagram ManyChat automations, a separate skill turns the topic research into a deliverable with a live link I can drop straight into the automation flow.
- Recording: I shoot natively in TikTok on my phone. After posting to TikTok, the video auto-saves to Photos. I send that file + caption to a Cortex agent that uses Blotato to fan it out to Instagram, X, and YouTube Shorts in one pass.
- Blotato is ~$29/mo and integrates every social API into one - massive time saver if you're posting 4+ pieces a day. Going to put together more of a marketing-focused course because everyone's been asking about this exact pipeline.

## AI Models Roundup

- ChatGPT 5.5 is genuinely good at production-level planning and schema design - have it plan, then let Claude implement. I wouldn't pay $200/mo just to use it for execution though.
- Higgs Field's Seed Dance video model is wild - Sebastiano made a kitchen-renovation clip that's 95% indistinguishable from a real home reno show. Catch: $8 per 15-second video, ate half his subscription.
- Image-to-image models can now generate scannable QR codes from a product image and a target link. Someone made a die with three working QR codes on different faces. Wild.
- Sabrina (HeyGen) has a batch option for AI avatar generation that's worth checking out if you're doing high-volume ads. Mispronunciation is still the obvious giveaway, but it's close.
- Gemini Pro and Flash are multimodal for video and audio - if you're analyzing video specifically, that's the path. For ads where every second matters, FFmpeg frame extraction + frame-by-frame analysis works well too.

## Cloud Code Disaster Stories + Security

- Steven lost his entire Claude directory mid-session - all skills, all memory, all client work. No indication in the JSONL of what happened. Recovered through VSS but most files were corrupt and a month of work was gone. Backups had silently failed.
- Pattern to watch for: when you ask Claude Code to "make things more efficient" or refactor, it'll sometimes find "87 GB we don't need" and just start deleting. Be very specific about scope on cleanup tasks.
- Ben's prevention strategy: separate dev and production branches in GitHub, with Vercel auto-deploying main. Claude Code only has access to the dev branch and creates PRs into main - no Vercel CLI/MCP wired up so it physically cannot deploy or touch the production database.
- Secret management gotcha: putting your .env in a folder Claude Code can see does not protect it - those keys end up in the JSONL transcript. Create env files OUTSIDE the working directory and reference them, never inside.

## Member Updates + Reminders

- Steven (welcome, first call!) actually built a native Windows port of Cortex before I released it - now testing the official release to compare. Going to be interesting to see how the WSL version stacks up against his native port.
- Welcome to Josh too - good to have you. Apologies for sending the email so late, that was on me.
- Next Think Tank: Monday 7pm EST. Next Q&A + Onboarding: Wednesday 7pm EST. Drop questions in the community anytime - I check every day.

Really fun call tonight, even though it started as just me and Robert. See you all Monday.

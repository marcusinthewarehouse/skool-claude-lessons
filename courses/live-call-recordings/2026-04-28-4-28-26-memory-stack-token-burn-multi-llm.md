# 4/28/26: Memory Stack, Token Burn, Multi-LLM

**Section:** Think Tank Calls
**Date:** 2026-04-28
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=c2f09b842c0d49af98b4219fb52dbedf
**Video ID (Skool):** a9d65f283dbf45e6b286126b0cdfd4a7
**Transcript:** [Full Call Transcript (4/28/26)](transcripts/call_transcript_4-28-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! Big think tank call tonight with a bunch of new faces and some really tactical takeaways on token optimization, memory, and multi-LLM setups. Here's the rundown:

## Forking Cortex OS for Your Own Use Cases

- Jagmeet asked about forking Cortex for a Dutch-market product. Yes, fork away. The repo is built to be forked - it's a proof-of-concept for remote AI agent orchestration, not the final product.
- If you build something stable that other people would benefit from, contributing back to the original repo is a great way to pay it forward.
- Looking at adding community maintainers soon so merges aren't bottlenecked on me. The risk of pushing untested changes that break everyone's setup is the main reason I'm being careful.

## Token Burn Strategies (David's Property Mgmt Setup)

- David is now running 6 agents 24/7 on Opus 4.7 averaging only 10-12% daily burn. He got there by running token burn audits and letting his agent design the optimization plan with him.
- Shift workers: agents that don't need to run during business hours go down to free up RAM. Other agents come on at night for tasks that don't need business-hours timing. Solved his 16GB Mac mini bottleneck.
- Internal agent-to-agent communication uses "caveman speak" to reduce token usage. Agents still talk normally to humans and to external services.
- His full stack: Opus 4.7 orchestrates, GPT 5.5 (Codex) executes the actual coding, then Opus 4.7 reviews. The speed of both means his optimized burn is actually cheaper than running 4.6.

## Memory Stack: Graphify + Mem0 (Trevor's Recommendation)

- Trevor (29 agents running continuously, 6 systems) said combining Graphify + Mem0 changed the way his agents work. He's running them all week without hitting limits.
- Graphify for overall project / code knowledge. Per-project graphify means your orchestrator can pull context with around 80% fewer tokens than reading session/memory .md files.
- Mem0 (mempalos) for individual agent memory. Orchestrator retrieves the specific room for each agent and hands off context to a new agent on demand, so agents don't need to sit idle burning tokens.
- Obsidian is good for the human view of the vaults - graphify generates them and you curate them in Obsidian. Don't use Obsidian as your primary agent memory layer.
- Cortex's native memory (Claude memory + daily and long-term .md + vector indexing) works but isn't optimized. Graphify + Obsidian integration is on the roadmap.

## Social Media Research Pipeline

- I have a skill that takes any post link (Reels, X posts, etc.), uses Apify to scrape it, then pipes the content to my researcher and developer agents who build a test tool around the idea.
- Sean has the same idea built on Hermes. It transcribes the content and gives an operator-perspective take on whether to integrate it into your setup.
- Auto version: pull from your top influencers, generate a digest, you say yay/nay on what to implement. Sean is already running this.
- I'll push the skill up to the Tools and Skills classroom tonight. Useful one for everyone to have.

## Hermes + Cortex Combo (Sean's Setup)

- Sean is running Hermes alongside Cortex. Main orchestrator on Cortex, agents have inboxes and message each other across both harnesses.
- Hermes runs on GPT 5.5, so when Claude usage runs out he flips to Hermes. Two subscriptions but worth it for continuous availability.
- Native Codex support and a Hermes adapter are on my Cortex roadmap. Hermes already has a lot of what Cortex hacks together on top of Claude code, and using it as an established harness inside Cortex would be a real upgrade.
- Cortex's CLI + file-based inbox system means you can plug Hermes or any CLI agent in today. Just feed them the skills that teach them how to use the messaging system.

## Sonnet 1M + GPT 5.5 Roundup

- Robert and Jagmeet both hit issues using Sonnet 1M inside Cortex on a Mac mini. It works fine in a normal CLI on a MacBook but doesn't respond inside the harness.
- Robert's research suggests 1M Sonnet may need API access, not just the auth subscription which caps at 200k. Worth digging into - I rolled my agents back to 200k as a workaround.
- Sean tested GPT 5.5 - says it's a notch better than Opus on some things, especially stepping into a new codebase. Still uses Opus as base because of the meta and rules he's built around it.
- Trevor doesn't trust OpenAI - just uses Claude's skill builder to spin up an adversarial review skill that runs on Opus 4.7 (his pick for code review). No need to hand your code to Codex.
- If you do use the official Cloud x Codex plugin, David flipped the roles: Opus orchestrates, Codex codes, Opus reviews. That's the setup that gave him the burn numbers above.

## Mirrorfish vs Mirrorshark

- Trevor mentioned Mirrorshark as a much cheaper alternative to Mirrorfish ($1-$3.50 per run vs Mirrorfish pricing). Worth a look if you're already running Mirrorfish.
- Joey Gonzalez in the community is building a Mirrorfish-as-a-service idea using local models. He's looking for collaborators - reach out to him directly if that's interesting.

## Member-Hosted Calls + Reminders

- Launching this week: members will be able to host their own calls in the community. Use it for topic-specific discussions, regional meetups, or connecting with people who joined around the same time as you. Recordings can be posted in the community.
- Onboarding/Q&A call is tomorrow (Wednesday) at 7pm EST. Newer members and anyone wanting a community tour or a beginner-friendly Q&A should join.
- Next think tank call: Monday 7pm EST. Tonight's Tuesday slot was a one-off because of a schedule conflict yesterday.
- Tools and Skills classroom (toolbox icon in the classroom) is where I post all skills - recent ones include dates so you can find the new stuff.

Awesome having the new members tonight. See you tomorrow at 7 EST or back here next Monday.

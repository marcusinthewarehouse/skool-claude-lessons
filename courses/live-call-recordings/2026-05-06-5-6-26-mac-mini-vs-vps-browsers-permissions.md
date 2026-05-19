# 5/6/26: Mac Mini vs VPS, Browsers, Permissions

**Section:** Q&A + Onboarding Calls
**Date:** 2026-05-06
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=a8cc812f2a854b35b32badd30b072b19
**Video ID (Skool):** f3b543bb343847e98e1321927de3dd01
**Transcript:** [Full Call Transcript (5/6/26)](transcripts/call_transcript_5-6-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! Great Wednesday onboarding/Q&A and a really practical one - Mac mini vs VPS, headed browser automation, and a bunch of permission/configuration tips for Cortex and Cloud Code. Here's the rundown:

## Welcome Max - Building a 24/7 Personal Assistant on Cortex

- Max is rebuilding his autonomous agent on Cortex from scratch after a first attempt failed. The plan is a personal/work assistant patterned after the multi-agent dashboard setup, with a longer-term goal of self-evolving behavior.
- If you're driven by genuine interest in the technicals, you'll figure it out. The dopamine loop on building these is real - lean into it. Post questions in the community as they come up.

## Cortex Updates: External Crons + Codex Adapter Coming

- External crons update shipped a few days ago. If you've pulled it, drop feedback in the community - haven't heard much chatter yet.
- Putting final touches on a Codex adapter so we can use Codex directly through Cortex functions. Big unlock for anyone wanting to mix Codex and Claude in the same orchestration.
- Planning to publish generalized agent templates to the community folder of the Cortex repo (skills, agents, orgs subfolders). Bootstrap files, settings.json, the whole agent folder structure - templated so you can clone what's actually working.

## Mac Mini vs VPS for Running Agents

- VPS is technically better long-term - more scalable, cheaper - if you're comfortable configuring it securely. The bottleneck for most people is comfort with VPS hardening, not the agents.
- Mac mini wins on ease, built-in physical security, and the SSH + screen share combo - you can SSH from your laptop and also see the actual screen of the Mac mini, which is huge for browser-driven flows.
- David's case for Mac mini for personal-life agents: it gives the agent native access to your iMessages, phone integration, and texts. Worth knowing the risk - it will sometimes randomly text people if you let it.
- Browser automations (Playwright MCP, Playwright CLI, newer harnesses) are noticeably more reliable on a Mac mini than spinning a browser inside a VPS. If $600-1200 just for that is worth it depends on how heavy your browser-driven workflows are.

## Headed Browser Automation: Snap CLI, Browser Harness, CLI Anything

- The big advantage of headed automation: you don't get auto-kicked off services like Playwright headless does. Sites can't easily block headed browsers without breaking accessibility for actual disabled users - so they don't.
- David built Snap CLI on top of CLI Anything (he calls CLI Anything the best of the bunch). Open CLI is also in the mix. Browser-use's "browser harness" runs on top of Snap CLI - that's what gives the agent actual headed-browser control.
- Mac mini bonus: routing through Safari uses way less RAM than Chrome and gets you the macOS accessibility API for free.
- For cybersecurity, you can wrap the CLI calls so that JSON returns get sandboxed and filtered for prompt injections before the agent sees them. Worth building if you're worried about untrusted page content.

## Playwright as Scripts (Not Just Agent-Driven CLI)

- Easy to forget that Playwright was scripts before it was an agent tool. If you're doing the same predictable browser flow over and over, write a Playwright script and have your agent just call the script - no token burn on the click-by-click reasoning.
- Ben's example: he runs Playwright tests headlessly for a web app with 20+ form-filling screens. Runs from the terminal, no agent needed for the test itself. Save the tokens for the parts that actually need reasoning.

## Claude Code Permission Hell + How Cortex Handles It

- Recent Claude Code update made it so even on "dangerously skip permissions" mode it still asks before editing anything in the .cloud folder. Annoying because half of self-evolving agent work involves editing .cloud configs.
- In Cortex this is already handled - the agent template includes a custom PTY hook that auto-accepts .claude edit prompts. Going to write up the workaround as a community post for people running Claude Code outside Cortex.
- If you're getting permission prompts for non-.cloud files, double-check you're actually in bypass mode (the new "auto" mode shows up in red between dangerous and full bypass - easy to land on it accidentally).
- M2C1 worker skill is currently broken in the agent templates. Workaround: use the standalone M2C1 GitHub repo skill and tell the agent "don't use a worker, run this yourself." Fix is on my list.

## Erica's Telegram Bridge for Phone-to-Agent Chat

- Erica has a Telegram bridge that lets you chat back-and-forth with your agent via voice from your phone. He's sending it to Robert and is happy to share more broadly.
- Stack: Telegram BotFather (your bot), OpenAI API key (for Whisper transcription), and a polling cron - the agent checks for new messages every 5-10 min, transcribes voice, and responds.
- Erica pushed a version of this to the community for Cortex earlier - worth looking for it. Solid pattern if you're going on a trip and want to keep talking to your stack.

## Wildcard Permissions: The Duct-Tape Fix That Actually Works

- Erica's habit when a permission popup appears: paste the prompt back at the agent and ask "what wildcard rule do we need to add to my permissions file so you stop asking me this?"
- Agent figures out the right pattern, you approve once, and the entire class of prompts goes away. Good move if you keep getting hit by the same category over and over.

Good Q&A tonight - welcome to Max, and see everyone Monday at 7 EST for the next think tank.

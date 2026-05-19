# Lesson 3: Keep It Alive

**Section:** Module 1: Setting Up Open Clawd Code
**Course:** Open Clawd Code (3/9/26)
**Skool URL:** https://www.skool.com/agent-architects/classroom/3caebf63?md=2a1cc57292ba4a94ae8602f21a6a3fcf
**Video ID (Skool):** 739f4ddffd53403e862b7f69c0151c5c
**Scraped:** 2026-05-19

---

## What You'll Learn

- How to make your agent run permanently in the background using launchd, tmux, and caffeinate
- The 71-hour session lifecycle: why your agent restarts and how it preserves knowledge
- Crash protection, rate limit backoff, and Telegram crash alerts
- How crons survive restarts via config.json
- Choosing the right model (Sonnet vs Opus) for 24/7 agents

## In This Lesson

Right now, your agent dies the second you close the terminal. All those crons, that personality, the heartbeat - gone. In this lesson, you'll make it permanent. Your agent will run 24/7 in the background via macOS launchd, live inside a tmux session you can attach to anytime, and automatically restart every 71 hours with fresh context while preserving all its knowledge in markdown files.

You'll use the updated onboarding wizard which detects your existing setup from Lessons 1 and 2, skips what's already configured, and walks you through the persistence setup via Telegram. You'll test the full lifecycle with a 3-minute timeout, watch the agent die and restart itself, then go live with 71-hour production cycles.

## Resources

- Example Project: Lesson 3 - Keep It Alive https://github.com/grandamenium/openclawd-lesson-3-keep-it-alive

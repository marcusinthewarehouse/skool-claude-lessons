# 3/9/26: Claude vs OpenClaw, Memory, Codex

**Section:** Think Tank Calls
**Date:** 2026-03-09
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=373d833e9035457e99599234120cc7b3
**Video ID (Skool):** 654a430d94f84410bf7e96e4fa71d4aa
**Transcript:** [Full Call Transcript (3/9/26)](transcripts/call_transcript_3-9-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! Great call this week - lots of new faces and some really solid discussions about Claude Code vs OpenClaw, memory management, Codex 5.4, and some cool projects people are building. Here's the rundown:

## James's Updates: CoinTally Pivot + New Course

- Pivoted CoinTally (crypto tax software) to target content creators and TikTok shoppers - faster growing market with less competition than crypto tax tools
- Just released a new course on using Claude Code + tmux + launchd to replicate OpenClaw functionality natively - boots up faster than OpenClaw and uses your existing MCP/skills config
- Business OS is coming soon - multi-agent system with agent-to-agent communication via inbox files and logging

## Claude Code vs OpenClaw - Which Should You Use?

- General consensus: Claude Code on a dedicated Mac mini is the most secure and simple path - Apple's built-in security handles a lot, no config headaches vs AWS/EC2
- Rodrigo's team built a cron job that monitors the OpenClaw GitHub repo daily and proposes relevant updates - so you can run Claude Code while staying current with OpenClaw's community improvements
- Rodrigo also built a custom CLI triggered by launchd that polls the API every 3 seconds instead of the 1-minute Claude Code cron interval - uses the /p (print) flag to pipe Telegram messages directly into Claude
- If you do go OpenClaw, check out the last video in the Claude Code Fundamentals course for a deep dive on context/bootstrap file engineering

## Memory Management for Agents (Fixing Context Loss)

- The fix: use very strong language in your agents.md file telling OpenClaw to use memory_search and memory_get tools proactively before every task - not just occasionally
- Create a dedicated memory management skill referenced in agents.md - this ensures the agent re-checks context at every restart, compact, or new task
- Same principle applies to CRM checks, email, anything you want the agent to reliably consult - strong prompting language at context ingestion points changes the whole system

## Claude vs Codex 5.4 - When to Use Each

- Codex tends to be better for large codebases with lots of dependencies - it's more analytical, explores edge cases thoroughly before implementing, and will intuitively pull schemas from existing code rather than hardcoding
- Claude Code is better for greenfield projects and quick feature generation - faster to execute but more opinionated and less thorough on edge cases
- Best workflow: use Claude to write, Codex to do code review - let them critique each other before you create the PR
- Codex app currently has 2x rate limits for new users - worth downloading now to lock that in

## Computer Vision with YOLO (Rodrigo)

- Using YOLOv8 from Ultralytics for a client - counting coconuts on a production line to verify supplier delivery quantities
- Training tip: use Claude Code to break a 20-second video into thousands of frames (millisecond intervals) - gives you a large, diverse training dataset without needing to manually collect images
- Diversity in training data matters a lot - different lighting conditions, angles, and settings dramatically affect model accuracy

## Reverse Engineering Client Codebases with AI (Benjamin)

- Built a tool that ingests messy client source code + docs, stores docs in Pinecone as RAG, and uses the highest Claude model to generate a comprehensive HTML dictionary of the entire business system
- Output is a multi-page HTML doc clients can review and verify before you build on top of their existing stack - especially useful when inheriting undocumented legacy code
- Plans to expand to Excel-based business operations (yes, some companies run entire ops from spreadsheets)

## Multi-Machine Agent Networks (Wes)

- Wes is running agents across a repurposed 2009 Mac Pro, 2012 iMac, and MacBook Air - tried Tailscale and relay/notebook systems for inter-agent communication
- James's recommendation: use inbox files (JSON) that agents drop messages into on a 1-minute loop - same pattern Claude Code's native agent teams use internally, and it works really well
- Combine with strong memory language and grep-based context retrieval (searching memory by concept, filtering by date via git timestamps)

Awesome group this week - tons of diverse backgrounds from software engineers to non-technical founders all attacking the same problems from different angles. See you all next week, same time same place!

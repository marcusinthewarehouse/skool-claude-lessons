# 3/2/26: OpenClaw, Context Trees, Client CRM

**Section:** Think Tank Calls
**Date:** 2026-03-02
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=ee70d5dab8054f199fa166f404b4ff8a
**Video ID (Skool):** a90ddf4667704a52863f5d37b1e62180
**Transcript:** [Full Call Transcript (3/2/26)](transcripts/call_transcript_3-2-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! Just wrapped up another great community call and wanted to share the highlights for those who couldn't make it. This week was an incredible conversation with a mix of returning members and some awesome new faces. We had a really real, honest discussion about everything from OpenClaw vs Claude Code, to how to structure your agent's file system, building client CRMs with AI, and even whether any of us are actually making money with this stuff. Great energy from everyone.

Here's a rundown of what we discussed:

## OpenClaw vs Claude Code: The Key Differences

- James broke down the three core differences: OpenClaw has a gateway for messaging from anywhere (Telegram, WhatsApp, iMessage), heartbeat/cron triggers that wake it up to work autonomously, and a more robust memory system that persists across sessions
- Claude Code is more human-in-the-loop and better for software development where you want direct control - but fundamentally both tools use the same LLMs and can connect to the same services
- The best approach is using both together: Claude Code for interactive software projects, OpenClaw for autonomous business tasks and always-on workflows
- New OpenClaw Fundamentals course just dropped in the classroom with more advanced content coming on multi-agent setups, memory internals, and bootstrap files

## Context Trees and File Structure Engineering

- James explained the "context breadcrumb tree" concept: your CLAUDE.md file is the trunk, pointing to branch files, which point to leaf files - allowing the agent to traverse only the context it needs for each task
- The debate between prescriptive file structure vs letting the agent decide landed somewhere in the middle - understand the technicals but be ready to let go as tools evolve
- Key insight: LLMs don't actually learn from you over time - they do "in-context learning" from whatever's in their context window, so your file system IS your agent's brain
- Michael shared a pro tip: start Claude Code in a dedicated workspace folder rather than your home directory, and provide only the documents and context relevant to that project

## Context Window Management and Shutdown Sequences

- Michael shared his setup: a visual progress bar at the bottom of the terminal showing context window usage (green/yellow/red), plus NTFY alerts that vibrate his phone when hitting 70%
- His shutdown sequence: before context collapses, it commits work, checks all related files, writes a memory pickup note, so the next session can resume with full context from the previous one
- Remote control mode lets you access Claude Code from the Claude app on your phone - open multiple remote channels before leaving your house and use them on the go
- David recommended the GSD "pause work" command as a lifesaver for people who get interrupted frequently - it writes a pickup file so you can resume exactly where you left off

## Skills, MCPs, and Domain-Specific Automation

- Robert (advertising/agency) asked about applying AI to Google Ads and client work - James recommended starting with simple tasks, "skillifying" them, and building in validation criteria
- Hot debate: MCPs vs CLIs vs raw APIs - MCPs are just agent-friendly API wrappers, but many practitioners actually prefer CLIs or raw APIs now that agents are so good at writing code
- Pro tip: pair skills WITH your MCPs - teach your agent how to use each specific API endpoint correctly by providing a skill alongside the connection
- The biggest gap in agent automation: validation. Coding is quantifiable (tests pass or fail), but subjective work like ad creatives is much harder for agents to self-validate

## Building a Client CRM with AI

- Roberto is building a coaching client management system - needs client profiles, session tracking, progress monitoring, and pre-meeting briefings from Fathom call transcripts
- James recommended a simple database approach: folders per client, files per meeting with timestamps, and letting Claude Code traverse the history when you need insights
- Key principle: always timestamp your stored information, whether through git commits, dated filenames, or database metadata - this gives your agents built-in memory without complex systems
- Rob had a breakthrough realization: every client interaction is a database event - structured, timestamped, and queryable. That's what agents thrive on

## Obsidian as a Knowledge Base

- Sam uses Obsidian as his primary information system - it's essentially a tree of local markdown files that syncs across devices and is naturally LLM-friendly
- Obsidian's advantages: open source, everything stored locally (privacy), markdown-native (Claude Code friendly), and has a graph view for visualizing connections between notes
- Sam uses OpenClaw heartbeat/cron jobs to automatically organize and template his Obsidian notes
- David pointed out you can use Claude to suggest optimal folder structures for your projects - it'll propose blockers, decisions, specs, handoffs, and session summary folders

## Making Money with AI: The Real Talk

- Rob's management consulting practice: 10x+ productivity gains, building intelligence models from structured and unstructured data that would normally take a team of data engineers 29 days and $100K+
- Rob's OpenClaw setup monitors his inbox, outbox, calendar, and Teams transcripts to auto-prepare deliverables before each client meeting
- James uses AI across his business: writing software products, marketing, ad creatives, community management, content research and drafting
- The honest consensus: most people aren't directly making money FROM AI yet, but the productivity and time savings are translating into massive indirect value

## Multi-Agent Setups and Harness Engineering

- Sam is exploring running multiple OpenClaw instances for different projects/stakeholders, with a coordination layer for shared memory between agents
- James is working on the same challenge: shared memory across agents with separate workspaces, skills, and contexts - plus inter-agent communication
- Benjamin brought up "harness engineering" as the next frontier - the idea that in 3-6 months, we'll have 24/7 agents running on device or cloud that you can manipulate multiple instances of simultaneously
- Security caveat: if one OpenClaw instance is a security risk, seven instances multiply that risk significantly

## Welcome New Members!

- Rob - Management consultant, data-obsessed, using OpenClaw to automate client deliverables and meeting prep. Described the community as "a support group for AI enthusiasts"
- Robert - Advertising agency owner, using Claude to cut Google Ads account building from days to hours, building custom landing pages with Lovable
- Roberto - High-ticket coaching business, building client intelligence profiles and CRM systems with Claude and Fathom integration

Great call all around. Same time, same place next week. Drop any questions or projects you're working on in the community. We all love seeing what everyone's building.

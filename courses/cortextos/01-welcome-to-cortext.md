# Welcome to Cortext

**Course:** CortextOS (3/23/2026)
**Course slug:** d15b1151
**Lesson md hash:** c30bee7bf6ea4d68a99b1cdbb0e7de25
**Source:** https://www.skool.com/agent-architects/classroom/d15b1151?md=c30bee7bf6ea4d68a99b1cdbb0e7de25
**Scraped:** 2026-05-19

---

Cortext is a system for running persistent 24/7 Claude Code agents that live on your machine, talk to you over Telegram, coordinate with each other on a shared task board, and run a web dashboard so you can see what they're up to.

The agents have their own memory. They know what they worked on yesterday and they pick up where they left off without you having to explain anything.

Still a work in progress. Sharp edges exist. But it works well, and the community is building on top of it fast.

## What You Actually Get

Every setup starts with two agents out of the box. On top you can add as many specialist agents you want, and migrate any OpenClaw or Hermes setup into a specialist Cortext agent.

**The Orchestrator** is the one you text to organize the whole fleet. Send it a message on Telegram and it figures out what needs to happen. It breaks goals into tasks, delegates to other agents, tracks what is done, and sends you a briefing. You never have to open your computer to check in, it checks in on you.

**The Analyst** watches everything the other agents are doing and runs a deep review every night. It proposes improvements, flags problems, and pulls the latest updates from the community repo automatically. When you fix something or build a new skill, your Analyst can submit a pull request upstream so everyone else gets it too. That is how the catalog gets better.

Agents talk to each other through a messaging system where they freely chat between each other in real time and share a task board. You can see on the dashboard exactly what is in progress, what is done, and what is blocked, in real time.

**The memory system** is what makes agents actually useful over time. Every agent writes a daily log of what it did and a long-term memory index. Before each session it reads that memory so it is not starting from scratch. The longer you run Cortext, the better your agents get.

**Skills** are what give agents specific capabilities on top of the defaults. A skill teaches an agent how to do a specific thing: run your content pipeline, manage your CRM, handle email, monitor analytics. Skills come from the community catalog or you can write your own.

You talk to everything over Telegram. Just send a message. They reply. Send a photo, they can process it. No app to install.

## Installing Cortext

On **Mac or Linux**, run this one command in your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/grandamenium/cortextos/main/install.mjs | node
```

On **Windows**, run this in PowerShell:

```powershell
node -e "const h='https://raw.githubusercontent.com/grandamenium/cortextos/main/install.mjs';require('https').get(h,r=>{let d='';r.on('data',c=>d+=c);r.on('end',()=>eval(d))});"
```

Then open the installed Cortext folder in Claude Code and type `/onboarding`. The agent walks you through the whole setup. Telegram connection, first agent configuration, memory structure, cron jobs in about 30 minutes.

After that you do not type commands. Your agents handle everything. You just talk to them.

## The Skill Catalog

Skills are the main reason to be in this community. Every time a builder publishes something useful, everyone's setup gets more capable.

The catalog covers content pipelines, research workflows, CRM, email, social media, knowledge base management, trading, and more. It grows every week.

Browse and install skills straight from your agent. Your Analyst automatically pulls updates when new community skills drop.

If you build something that saves you hours, share it. That is how this gets better for everyone.

## Getting Started Right

Run `/onboarding` first and let it finish completely. That flow sets up your Telegram connection, configures your first agent, creates your cron jobs, and builds your memory structure. Skip it and you will spend a lot of time debugging things that should have been automatic.

Read your agent's memory files. It lives at `memory/YYYY-MM-DD.md`. If the memory looks thin, tell your agent to be more detailed. Agents that write good memory get better over time. Agents that write sparse memory basically restart every session.

Things will break. This is new software with sharp edges. When something breaks, check GitHub issues, ask in the community here, or file a bug. Your Analyst already knows how to PR fixes upstream.

## Open Source

The whole framework, all the agent templates, and the community skill catalog are on GitHub. Completely open.

**Repo:** [github.com/grandamenium/cortextos](https://github.com/grandamenium/cortextos)

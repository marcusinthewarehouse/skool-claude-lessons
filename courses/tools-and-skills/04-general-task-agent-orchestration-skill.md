# General Task Agent Orchestration Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=320ccc35f21f47d8824510fc928cdc91
**Scraped:** 2026-05-19

---

A Claude Code skill that converts any complex multi-step project into a fully orchestrated, phased action plan with autonomous agent execution. Give it a brain dump and it transforms it through a 12-phase protocol into an autonomously executable project with verification at every step across six execution surfaces: web browser, native macOS apps, files, communication, calendar, and APIs.

## How It Works

Tell Claude what you want to accomplish in plain language - a brain dump, paragraph, doc, or voice-to-text. The skill activates a 12-phase protocol that autonomously researches the domain, asks you targeted discovery questions, sets up all required tools and surfaces, creates a detailed phased action plan, shards it into individual task files, and then executes each task with verification at every step. Subagents handle the "human steps" via browser automation (Playwright) and native macOS app control (Peekaboo), so the only things that require your input are genuinely manual steps.

## Six Execution Surfaces

The key differentiator from other orchestration approaches - agents don't just write files, they operate across six real-world surfaces:

- Browser (Web) - Playwright MCP for web apps, dashboards, SaaS platforms
- Native macOS Apps - Peekaboo CLI for desktop apps (Keynote, Calendar, Mail, any app)
- Files - Documents, configs, data files, exports via Bash/Read/Write
- Communication - Email, messaging, notifications via Playwright or Peekaboo
- Calendar - Scheduling, events, time blocks
- APIs/MCPs - External service integrations via MCP tools and curl

## Use Cases

### Content Creation & Publishing

- Weekly newsletter + social media content pipelines
- Blog post series with coordinated publishing across platforms
- Video production workflows from script to upload

### Course & Curriculum Design

- Multi-module online courses with lesson materials and assessments
- Workshop planning with presentations, handouts, and scheduling
- Training program rollouts with enrollment and tracking

### Operations & Project Coordination

- Event planning with venue research, scheduling, and outreach
- Hiring campaigns with job posts, outreach sequences, and interview scheduling
- Research projects with data collection, analysis, and report generation

Killer combo: Describe your project in plain English, walk away, come back to a fully researched, planned, and executed deliverable with verification evidence at every step.

## Installation

Prerequisites: Claude Code, Playwright MCP (web browser automation), and Peekaboo CLI (macOS native UI automation). See the GitHub README for full setup instructions including Playwright MCP configuration and macOS permissions.

Clone the repo directly into your Claude Code skills directory:

```
git clone https://github.com/grandamenium/general-task-agent-orchestration.git ~/.claude/skills/general-task-agent-orchestration
```

After cloning, Claude Code automatically discovers the skill via SKILL.md. Just tell Claude to "orchestrate" any project and it activates the full 12-phase workflow.

---

GitHub Repository: [https://github.com/grandamenium/general-task-agent-orchestration](https://github.com/grandamenium/general-task-agent-orchestration)

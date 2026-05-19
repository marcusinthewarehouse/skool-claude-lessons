# GWS Meta-Workflows Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=d0cbb00e44d2404aad0e1e708a7db453
**Scraped:** 2026-05-19

---

Six composable meta-workflows that chain Google Workspace CLI (gws) commands into end-to-end automations. Stop giving your agents browser access to Gmail - use structured CLI commands with JSON output, wired through an MCP server, with safety rails built in.

## How It Works

The Google Workspace CLI (gws) reads Google's Discovery Service at runtime and dynamically builds its entire command surface. When Google adds a new API endpoint, gws picks it up automatically. All output is structured JSON. It ships with a native MCP server, 100+ agent skills, and Model Armor integration for prompt injection detection.

## The Problem This Skill Solves

Browser automation for Google Workspace is fragile. Login walls, UI changes, random popups, and no audit trail of what the agent actually did. This skill replaces browser automation with structured CLI commands that output JSON, so every action is traceable and deterministic.

## What's Included

- inbox-triage-and-auto-reply - Classify unread emails, draft routine replies, escalate action items to calendar and tasks
- pre-meeting-context-compiler - Pull attendees, search recent threads, find relevant docs, compile a briefing in Google Docs
- client-onboarding-automation - Create Drive folder structure, copy templates, populate tracker, schedule kickoff, draft welcome email
- weekly-activity-digest-generator - Compile sent emails, calendar events, and modified docs into a weekly summary document
- email-prompt-injection-scanner - Scan inbound emails for hidden agent instructions using Model Armor, quarantine flagged messages
- scheduling-conflict-resolver - Extract proposed times from emails, check free/busy, draft reply with available slots

## Installation

Step 1: Install the GWS CLI

```
npm install -g @googleworkspace/cli
```

Step 2: Install gcloud CLI (needed for auth setup)

```
brew install --cask google-cloud-sdk
```

Step 3: Authenticate

```
gws auth setup && gws auth login -s drive,gmail,calendar,docs,sheets
```

Step 4: Clone this skill into your Claude Code skills directory

```
git clone https://github.com/grandamenium/gws-meta-workflows.git ~/.claude/skills/gws-meta-workflows
```

---

GitHub Repository: https://github.com/grandamenium/gws-meta-workflows

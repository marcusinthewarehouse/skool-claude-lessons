# GWS Meta-Workflows Skill

**Created:** 2026-03-06
**Upvotes:** 6
**Comments:** 4
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/gws-meta-workflows-skill

---

Six composable meta-workflows that chain Google Workspace CLI \(gws\) commands into end-to-end automations. Replace fragile browser automation with structured CLI commands that output JSON, wired through an MCP server, with safety rails built in.

What's included:
- inbox-triage-and-auto-reply: Classify unread emails, draft routine replies, escalate action items to calendar and tasks
- pre-meeting-context-compiler: Pull attendees, recent threads, and relevant docs into a briefing before meetings
- client-onboarding-automation: Spin up Drive folders, populate templates, schedule kickoff, draft welcome email
- weekly-activity-digest-generator: Compile sent emails, calendar events, and modified docs into a weekly summary
- email-prompt-injection-scanner: Scan inbound emails for hidden agent instructions using Model Armor
- scheduling-conflict-resolver: Extract proposed times from emails, check availability, draft reply with open slots

Clone it into ~/.claude/skills/ and trigger any workflow by asking Claude Code to triage your inbox, prep for a meeting, onboard a client, or scan for prompt injection. [https://github.com/grandamenium/gws-meta-workflows](https://github.com/grandamenium/gws-meta-workflows)

# Claude Code /schedule Guide (4/17/2026)

**Date:** 2026-04-17
**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=e8c25538dcae4218b7e8191ba9429f48
**Scraped:** 2026-05-19

---

A setup guide for Claude Code's /schedule command — run agents on Anthropic's cloud infrastructure on a cron schedule. Laptop closed, still runs.

What /schedule does:

Save a Claude Code configuration (prompt + GitHub repos + trigger) and it runs automatically. Three trigger types:

- Schedule: cron expression, minimum every hour

- API: generates an endpoint + bearer token, anything can trigger via HTTP POST  

- GitHub: fires on PR open, push, merge, or release events

Daily run caps: Pro = 5/day. Max = 15/day. Team/Enterprise = 25/day.

Setup flow:

1. Type /schedule in Claude Code (or /schedule daily PR review at 9am)

2. Name it, write the prompt, select GitHub repos, set trigger

3. Configure MCP servers (remote HTTP/SSE only — local MCPs don't run in cloud)

4. Add secrets (encrypted env vars available at runtime)

5. Save and test with "Run now"

Manage at: claude.ai/code/routines

Three overnight workflows included (ready to paste):

- Nightly bug fix: pulls 3 oldest open bugs, attempts fixes, opens draft PRs

- Weekly doc sync: finds merged PRs that changed code but not docs, opens update PRs

- PR review on push: reviews every new PR against a checklist, leaves inline comments

Guide: https://docs.google.com/document/d/1069dag_1pYe92YHyu32FYGRBP77gIxHS/edit?usp=sharing

Research preview — some behavior may change.

# Infisical Vault Skill (4/30/26)

**Date:** 2026-04-30
**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=c9aba0f7468447cab93e3fb779544b9e
**Scraped:** 2026-05-19

---

Infisical Vault Skill pulls secrets from Infisical into your Claude Code agent at runtime so API keys never live in .env files.

Instead of storing credentials locally, the skill fetches them from your Infisical project on demand. Keys are never written to disk. Rotation happens in Infisical and the agent picks it up automatically on the next run.

What it does:

- Fetches secrets from Infisical using a short-lived machine identity token

- Injects credentials into the agent environment at session start

- Logs every secret access so you have a full audit trail

- Supports multiple environments (dev, staging, prod)

Install:

git clone https://github.com/grandamenium/infisical-skill ~/.claude/skills/infisical-skill

GitHub: https://github.com/grandamenium/infisical-skill

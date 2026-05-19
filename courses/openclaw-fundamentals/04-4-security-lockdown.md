# 4. Security Lockdown

**Course:** OpenClaw Fundamentals (3/3/26)
**Skool URL:** https://www.skool.com/agent-architects/classroom/da68c6be?md=4e092fb1d44240219732465f60a40ee5
**Video ID (Skool):** eebdd78e03e048989c4a674ade1b3e93
**Resource:** Security Lockdown Cheatsheet (file: `04-security-lockdown-cheatsheet.docx`, id: `45c7a2c79f684090b89605b1c0c7a8d4`)
**Scraped:** 2026-05-19

---

Before you start building with OpenClaw, lock it down. This video covers 6 essential security commands that protect your assistant from unauthorized access and prompt injection.

**What you'll configure:**

- **Gateway binding** - Lock the control plane to localhost only so nobody on your network can access it.
- **Docker sandboxing** - Run commands in isolated containers so a compromised agent can't touch your host.
- **Exec allowlist** - Only pre-approved commands can run. New ones pause and ask for your permission.
- **Telegram allowlist** - Lock your bot to your Telegram user ID so strangers can't control it.

**Three security profiles:**

- **Maximum Security** - Bot can chat but can't execute anything.
- **Balanced (Recommended)** - Bot works within guardrails, asks permission for new commands.
- **Maximum Agency** - Bot can do anything instantly. Only for experienced users.

Download the cheatsheet attached below for all the commands in one place.

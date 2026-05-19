# CLI Agent Tools - 30+ CLI Tools with Skills

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=9b2538ec6b9d440a8272295925646b49
**Scraped:** 2026-05-19

---

A curated collection of 30 popular CLI tools paired with ready-to-use Claude Code skills. Each skill teaches your AI agent how to use the CLI effectively - replacing bloated MCP servers that waste up to 72% of your context window.

## Why CLI Over MCP?

- 32x cheaper token consumption (Scalekit benchmark: 1,365 vs 44,026 tokens)
- 100% reliability vs 72% for MCP (28% timeout failure rate)
- Lazy loading - agent discovers commands via --help on demand
- Pre-trained knowledge - AI models already know CLI tools from training data

## 30 Tools Across 8 Categories

- DevOps: gh, docker, kubectl, terraform
- Cloud: aws, gcloud, az
- Deployment: vercel, railway, netlify, fly, firebase, wrangler
- Database: supabase, turso, planetscale
- Media: ffmpeg, imagemagick, blender, yt-dlp
- Communication: stripe, resend, twilio
- Testing: playwright, httpie
- Utility: jq, ripgrep, ngrok, pandoc, gh-copilot

## Installation

```
git clone https://github.com/grandamenium/cli-agent-tools.git
mkdir -p .claude/skills
cp cli-agent-tools/tools/github/SKILL.md .claude/skills/github.md
```

Or install all tools at once:

```
./install-all.sh --all
./install-all.sh --category cloud
./install-all.sh --tool github
```

---

Each tool includes a SKILL.md (Claude Code skill with YAML frontmatter) and install.sh. Skills cover authentication, common commands, agent best practices, and example workflows.

GitHub Repository: [https://github.com/grandamenium/cli-agent-tools](https://github.com/grandamenium/cli-agent-tools)

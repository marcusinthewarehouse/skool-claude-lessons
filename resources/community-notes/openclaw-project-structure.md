# OpenClaw - Project Structure and Configuration

## Directory Separation

Never create apps inside the `.openclaw/` config directory. That folder is for OpenClaw's brain (memory, agent definitions, skills) - not your actual code projects.

### Correct Structure

```
~/.openclaw/workspace/       # OpenClaw config
  AGENTS.md                  # Agent definitions
  SOUL.md                    # Personality
  MEMORY.md                  # Long-term memory
  artifacts/                 # OpenClaw output space

~/projects/my-app/           # Actual app code (separate)
  src/
  package.json
  README.md
```

### Key Points

- OpenClaw orchestrates but doesn't own your code
- It can create files inside your project directory (via mapped volumes) and run build commands
- The project itself belongs to you, not OpenClaw
- `artifacts/` is a dedicated output space for generated content not part of your permanent codebase

## Using AI Coding Agents with OpenClaw

To use AI coding agents with OpenClaw, open the `.openclaw` directory (or project folder) in Cursor or Claude.

**LocalSetup tool** automates context sharing across editors:

```bash
# In your project root (or ~/.openclaw/)
curl -sSL https://raw.githubusercontent.com/cptnfren/localsetup/main/install | bash
```

- Creates a `_localsetup/` folder that works across Cursor, Claude Code, and OpenClaw
- Tell it which platforms you're using and it handles context sharing automatically
- Hardening guide prompts become drop-in instructions your AI can execute immediately

## Mem0 Plugin

Install memory plugin:

```bash
openclaw plugins install @mem0/openclaw-mem0
```

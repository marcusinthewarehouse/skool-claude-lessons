# OpenClaw - Credentials and Authentication Issues

## Common Problem

Even with everything installed correctly, the running agent can't see API keys and credentials you've configured. This is a known credential persistence bug.

## Fix: Run Diagnostics First

```bash
openclaw doctor
openclaw doctor --fix
```

This often reveals exactly which credential layer is failing.

## Fix: Use Environment Variables

Move credentials OUT of the config file and into environment variables.

### In your ~/.openclaw/openclaw.json:

```json
{
  "tools": {
    "web": {
      "search": {
        "apiKey": "${BRAVE_SEARCH_API_KEY}"
      }
    }
  }
}
```

NOT the actual key - use the variable reference.

### Then set in your environment:

```bash
export BRAVE_SEARCH_API_KEY="your-actual-key-here"
```

This bypasses the worst of the credential persistence issues.

## Email Login Tips

- Create a dedicated burner email account for OpenClaw (never your primary)
- Use OAuth if available

## Cloudflare Deployment Auth Issues

If you deployed via Cloudflare, Control UI approval requests won't appear because you don't have direct CLI access.

### Option A: Access CLI via Docker

```bash
# Find your container
docker ps | grep openclaw

# Exec into it
docker exec -it <container-id> bash

# List and approve pending requests
openclaw devices list
openclaw devices approve <request-id>
```

### Option B: Temporary Insecure Auth (dev only)

Add to your openclaw.json temporarily:

```json
{
  "controlUi": {
    "allowInsecureAuth": true
  }
}
```

Remove it immediately after approving.

## Telegram /skill Authorization

If `/skill` fails with "not authorized", your Telegram ID isn't in the allowlist.

1. Find your ID via @userinfobot
2. Add to config:

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "dmPolicy": "allowlist",
      "allowlist": [YOUR_USER_ID]
    }
  }
}
```

## Agent Autonomy Tips

If your agent keeps asking for help and can't complete tasks:

- **Schedule cron jobs** for repeatable tasks
- **Set up a memory system** and create cron jobs like "check email and reply to urgent ones every 1h"
- **Create a task system** where the agent records tasks, then a heartbeat runs and checks tasks. If there are tasks it can do without human permissions (based on hard guardrails), it starts doing them automatically
- **Use Opus to audit the system** - talk with it to understand how to make it as autonomous as possible without requiring your input at every stage

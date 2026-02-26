# OpenClaw - Token Usage Optimization

## The Problem

Simple tasks consume excessive tokens because files like `agent.md` auto-load into every session's context, even when that context isn't needed.

There are two layers:
1. **Platform-injected context** - happens automatically before the agent acts
2. **Agent startup behavior** - controlled by your rules

You can fix layer 2, but layer 1 requires config changes.

## Solutions

### Fix Auto-Loading

You cannot simply remove `agent.md` from auto-loading. Your options:

1. **Empty agent.md** and move its contents to `~/knowledge/base_instructions.md`
2. **Use OpenClaw's memory engine** instead of static files (capture, recall, decay, learn cycles)
3. **Split instructions** across files and have agents progressively discover context based on tasks
4. **Smarter models need fewer words** - optimize your instructions accordingly

### Reduce Context at Startup

Lock down which `.md` files load at startup. Recommended to only load:
- soul.md
- user.md
- identity
- last day memory.md

### Workspace Context Injection

Modify your `openclaw.json` file (usually at `~/.openclaw/openclaw.json` or `~/.openclaw-dev/openclaw.json`):
- Look for the section that controls workspace file injection
- Change it to only inject specific files you want
- Explicitly exclude `MEMORY.md` from auto-injection
- Restart your gateway after changes

### Lower Max Tokens

In your openclaw.config file:

```yaml
context:
  max_tokens: 200000  # Lower this if overprovisioned
  system_files:        # Check agent.md isn't listed here
```

### Multiple Agents

If you have multiple agents/subagents, each will have its own workspace and AGENT.md file. Don't put everything into one file - split it up and instruct agents to progressively discover based on tasks.

## Monitoring

```bash
# Token usage breakdown
openclaw doctor

# Daily token logging
openclaw stats --token-usage > ~/token-logs/$(date +%Y-%m-%d).txt
```

Check:
- Model routing tiers (are simple tasks using Tier 3 unnecessarily?)
- Duplicate tool definitions across multiple files
- Large knowledge bases loading automatically

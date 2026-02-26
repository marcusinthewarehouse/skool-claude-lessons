# M2C1 Skill (Measure Twice, Cut Once)

A skill for building entire software projects from a single brain dump. Inspired by GSD and PRP frameworks, with added steps that push the process to produce software that is actually ready to receive, monitor, and support paying users from the start.

## Philosophy

99% planning, 1% implementation. Layers of research, planning, environment configuration, synthesis, and validation. For larger projects, this uses a LOT of tokens and takes time to get to autonomous implementation - but that's why it works.

## Three Key Differentiators

### 1. Tool and Environment Discovery (Pre-Planning)

Before creating the PLANNING.md document, the agent reads all accumulated research and Q&As, then searches for any MCPs, Skills, CLI tools, or browser-automatable "Human Required" tasks it can complete with your credentials (getting API keys, configuring dashboards, creating testing artifacts, etc.)

The skill is designed to morph to your goals - no specific tools are hardcoded. Recommended tool access for production-ready output:

**Deployment:**
- Give your agent access to GitHub and deployment platform (Vercel, Railway, etc) via MCP AND through the browser with your login credentials via Playwright MCP
- Browser access gives FULL configuration access beyond what MCP tools or CLI provide alone

**Payments:**
- Give agent access to Stripe (or your payment platform) via MCP and browser dashboard

**User Action Monitoring:**
- Give agent access to PostHog via CLI and browser

**Database:**
- Give agent access to Supabase via MCP and browser

**Account Creation:**
- You can give your agent your Google login (or its OWN Google login) to create accounts and configure them fully autonomously
- This is risky but works without issues in practice

### 2. Comprehensive User-Centered Testing

Goes beyond standard unit/integration tests and Playwright screenshot checks.

**After every atomic task, the agent:**
- Tests many different user flow branches using Playwright MCP
- Exhausts all potential options a real user would take
- Covers branching user flow edge cases across the entire app
- Submits assets/inputs into the app if that's part of the user flow

**During planning:**
- Agent evaluates what user assets need to be created for automated testing
- If agent has deployment access, it also runs full regression testing on the live site after every phase

### 3. Plan Review and Synthesis

Solves the problem of sub-agents producing contradictory task files when research is split across multiple context windows.

**Explicit analysis step that verifies:**
- All atomic task files have contracts with each other
- All tasks have correct blocking/blocked-by flags
- No implementation steps or methodology disagree between tasks within a phase
- No disagreements between tasks across different phases

This ensures coherence even though planning is split across multiple sub-agent context windows.

## Usage Notes

- The skill pushes you forward through the orchestration phases
- There may be choppy moments where you need to ask Claude Code to reread the skill and workflow to understand what step you're at
- Feel free to make pull requests to the repository with interesting additions

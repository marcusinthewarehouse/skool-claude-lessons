# StatusLine Builder (4/16/2026)

**Date:** 2026-04-16
**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=ff81b640f1e54db6887c231bde393bfe
**Scraped:** 2026-05-19

---

StatusLine Builder is a guided prompt you paste into Claude Code that asks 5 questions about your workflow before writing a single line of config. What gets built is tailored to how you actually work, not a generic display.

The 5 questions:

1. What your day-to-day workflow looks like

2. What data you check most that requires switching windows

3. Local files that track your work state

4. External APIs or services you actively monitor

5. What would make you glance at the status bar and know something needs attention

After you answer all 5, Claude enters plan mode, proposes which metrics to include, how to pull each one, the format, and tradeoffs before touching any files.

What the status line can show:

The status line runs a shell script on every update. That script can read anything locally accessible:

- Claude Code session info: model, directory, git branch, context %, rate limits

- Local files: task count, agent queue depth, reminder count, next calendar event

- Shell commands: battery %, CPU, disk, any CLI output

- API calls: health endpoint, Stripe MRR, GitHub open PRs (anything you can curl and parse in under 1 second)

cortextOS ideas:

- Show active M2C1 worker count from cortextos list-workers

- Show pending task count from cortextos bus list-tasks --status pending

- Show heartbeat freshness (time since last heartbeat update)

- Show Skool member count from your latest scrape file

The prompt (Google Doc):

https://docs.google.com/document/d/1apoR55bEWj8OBvnmT-Fy7FjfEgUdtWECxPW6vXZgCqA/edit

Or comment STATUS on the TikTok to get it via ManyChat.

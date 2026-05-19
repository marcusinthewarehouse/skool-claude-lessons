# Recent Claude Code update broke .claude/ edit permissions

**Created:** 2026-05-08
**Upvotes:** 3
**Comments:** 2
**Labels:** 59ef34684a11462bac017ad7f612ac9d
**Post URL:** https://www.skool.com/agent-architects/recent-claude-code-update-broke-claude-edit-permissions

---

Claude Code now treats any edit or write to the .claude/ folder as a protected operation that requires explicit permission. That folder is where your agent keeps its memory, skills, and config. So every time it tries to update its own memory or edit a skill file, it stops and waits for you to approve.

The thing that makes this frustrating: even if you are running in bypassPermissions mode, .claude/ changes still trigger the prompt. The mode that is supposed to remove friction does not cover this case.

For a 24/7 autonomous agent that is supposed to run while you sleep, it just stalls.

The fix is to explicitly auto-approve operations that target .claude/. It is internal housekeeping. The agent is writing to its own brain, not touching your codebase or anything external. You detect when a file path or command targets .claude/ and let it through silently. Everything else that is not on your pre-approved list still routes to Telegram for your sign-off.

This is already handled in cortextOS. Here is how to add it to any Claude Code session. Attaching the guide below.

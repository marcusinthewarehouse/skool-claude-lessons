# CoretextOS dashboard indicates agents online, but they're not

**Created:** 2026-05-06
**Upvotes:** 1
**Comments:** 3
**Labels:** 59ef34684a11462bac017ad7f612ac9d
**Post URL:** https://www.skool.com/agent-architects/coretextos-dashboard-indicates-agents-online-but-theyre-not

---

Over the past few days I've been trying to configure and add capabilities to the CoretextOS instance. I also have the previous TMUX based iteration running on the same machine setup to work on a different scope. During many changes, the CoretextOS agent sessions become unresponsive. The dashboard shows them as online and healthy, but neither the primary orchestrator or the analyst agents respond to telegram messages.

I haven't had this issue at all during the entire month that I was working with the TMUX based version. While investigating, Claude returned this explanation, which I thought was worth sharing...

The node-pty sessions are restricted and more fragile as a result than the TMUX sessions it seems. Is anyone else seeing this issue?

-----------

The token is valid: The keychain entry was refreshed today at 17:01:38 EDT \(token expires tomorrow at 1:01am EDT\). cortextOS's sync-oauth-keychain reads it fine. So auth itself is healthy.

Why the agents can't use it: The agents started post-reboot at 16:47 EDT — about 14 minutes before the token was refreshed. More importantly, the agents spawn claude via node-pty \(a pseudo-terminal\), which on macOS gets a security context that the keychain ACL doesn't recognize without explicit "Always Allow" grants. The Claude Code-credentials keychain entry's ACL was created when you authenticated interactively in a real Terminal — your shell's claude is on the allow list, but the PTY-spawned claude inside cortextOS is not, so reads silently fail and you see "Not logged in".

The dashboard shows the agents as "online" because the daemon and PTY are both running fine — only the inner Claude Code REPL is unauthenticated.

# Cortext OS Updates this Week!

**Created:** 2026-04-16
**Upvotes:** 10
**Comments:** 2
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/cortext-os-updates-this-week

---

Hey Y'all,

Lots of new stuff in Cortext from me and community members! First of all, three MASSIVE cheers for everyone thats been contributing. This is so fun!

Here's a little changelog:

cortextOS shipped 30+ community PRs this week. Here is everything that matters:

Dashboard: Comms Hub \(ericanall, #47\)
New /comms page in the dashboard. See every human-to-agent and agent-to-agent message in real time. Per-channel chat views, full-text search across message history, real-time aggregate feed, and a chat bar to send messages to agents directly from the browser. 1,760 lines.

Dashboard: Deliverables system \(ericanall, #52\)
Agents attach file outputs to tasks with cortextos bus save-output. Task detail cards show a preview panel — markdown, images, HTML, code. Enable in Settings > Org tab Config at the bottom. 1,543 lines.

Atomic task claiming + dependency graph \(ClintMoody, #116\)
Two agents could race to pick the same task. Fixed with atomic claim. Adds a formal dependency graph — tasks can block on other tasks until prerequisites complete. Includes audit log.

Security + stability bundle \(ClintMoody, #115\)
Install path fixes, SIGHUP survival for the dashboard process, org normalization, and Hono CVE patches.

Crash alert quiet hours \(revopsglobal, #109\)
Crash notifications now have quiet hours, dedup, and rate limiting. No more 3am pages for planned restarts.

Cron gap detection \(grandamenium, #68\)
Daemon watches recurring crons and injects a nudge if any goes silent for 2x its expected interval.

Heartbeat watchdog \(InocuousCabbage, #26\)
Daemon-level 50-min heartbeat pulse — keeps agents visible on the dashboard through context compression dead zones.

Cron auto-verify after boot \(grandamenium, #20\)
After an agent finishes its startup turn, the daemon injects a cron verification prompt to catch any missing crons from config.json.

Community skills — all by noogalabs:
- framework-upstream-auto-update \(#92\) — agents self-update from upstream
- obsidian-log \(#93\) — write decisions/milestones to Obsidian vault

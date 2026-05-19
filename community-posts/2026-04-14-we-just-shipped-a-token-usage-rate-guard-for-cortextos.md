# We just shipped a token usage rate guard for cortextos.

**Created:** 2026-04-14
**Upvotes:** 4
**Comments:** 2
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/we-just-shipped-a-token-usage-rate-guard-for-cortextos

---

The problem: you hit your Claude rate limit mid-session, everything stops, and you lose context. No warning. No graceful shutdown.

The fix: a 15-minute cron that watches your Anthropic usage across both the 5-hour and 7-day windows. Three tiers:

85% -- agents finish what they are doing and stop taking new work
85-95% -- agents go minimal \(respond only, no proactive tasks\)
95% -- agents send you a status message and go dark until reset

State-tracked so you get one message per tier, not a flood of alerts. Wakes back up automatically on reset.

If you are running a cortextos fleet and getting blindsided by rate limits, this is the PR:grandamenium/cortextos#72

Collie also caught a .gitignore gap -- framework skills were not being tracked in git. That is fixed in the same PR.

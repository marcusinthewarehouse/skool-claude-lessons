# State continuity across scheduled task runs

**Created:** 2026-05-14
**Upvotes:** 1
**Comments:** 5
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/state-continuity-across-scheduled-task-runs

---

Trying to figure out the cleanest way to give a scheduled task enough context about prior runs without dumping the whole history into the prompt every time. Right now I read the last few session transcripts at the start of every run, but that's expensive on tokens and I'm not actually using most of what comes back. Curious what's worked for folks running daily or twice-daily agents. A summary file the agent maintains itself, or something cleaner?

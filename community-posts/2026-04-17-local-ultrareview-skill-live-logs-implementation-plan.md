# local-ultrareview skill — live logs + implementation plan

**Created:** 2026-04-17
**Upvotes:** 8
**Comments:** 4
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/local-ultrareview-skill-live-logs-implementation-plan

---

Just dropped a skill that does what /ultrareview does but local, with two things added that I actually wanted.

Ultrareview is a new thing in Claude code where you can spin up a bunch of agents in a cloud Claude code session to review your code in depth and send guidance back. I liked the idea a lot but wanted more control over the review process so I built my own version with a few key changes.

First thing: you can watch it work. Each of the three review agents writes a live log file as it runs so you can open a second terminal and see exactly what the correctness agent, the security agent, and the architecture agent are each looking at. With Anthropic's version you just get the output. With this you see the reasoning.

Second thing: it doesn't stop at a list of problems. After the synthesis there's a fourth agent that reads everything and writes an implementation plan. Exact files, exact changes, exact order. Then it asks if you want it to apply the fixes. If you say yes it does it and asks if you want to commit, re-PR, or merge.

Full skill here: [https://github.com/grandamenium/local-ultrareview](https://github.com/grandamenium/local-ultrareview)

Drop it in .claude/skills/ and run /local-ultrareview or /local-ultrareview PR#123.

# The latest Boris Cherny’s Tips for using Claude Code

**Created:** 2026-02-01
**Upvotes:** 5
**Comments:** 5
**Labels:** fe759d3753134f18b62c7eff10a4e379
**Post URL:** https://www.skool.com/agent-architects/the-latest-boris-chernys-tips-for-using-claude-code

---

Key Highlights:

Parallelization is the "Top Unlock":
[ul][li]The most effective way to use the tool is to run 3–5 separate Claude sessions simultaneously.

Workflow:
[ul][li]Use git worktree \(or multiple git checkouts\) to isolate tasks. This allows you to have one session running long-running tests, another doing a complex refactor, and a third performing log analysis, all without context contamination.
[ul][li]Tip: Use shell aliases \(like za, zb, zc\) to quickly hop between these parallel sessions

Advanced Prompting & Verification:
[ul][li]"Prove it, don't claim it": Instead of asking if a fix works, tell Claude: "Prove to me this works. Compare behavior on main vs. this branch using tests/logs."

Self-Review:
[ul][li]Before committing, tell Claude: "Grill me on these changes and don't make a PR until I pass your test."[li]Resetting: If a session gets bogged down with mediocre fixes, it’s often faster to git checkout . and start the specific task fresh rather than trying to "fix the fix."

Long-Running Tasks:
[ul][li]Unlike traditional chat interfaces, the team uses Claude for tasks that run for minutes or even hours.[li]They utilize "stop hooks" to let the agent handle heavy-lifting tasks \(like large migrations or deep debugging\) while the human supervisor works elsewhere.

The Power of [CLAUDE.md](http://CLAUDE.md):
[ul][li]This is a local file used to "train" the tool on your specific preferences.[li]Habit: After every manual correction, tell Claude: "Update your [CLAUDE.md](http://CLAUDE.md) so you don't make that mistake again."[li]Maintenance: Prune this file aggressively over time to keep the context clean and the mistake rate low.

The Bottom Line:
Cherny argues that "code is no longer the bottleneck." By using these "agent-native" workflows, a single engineer can manage a much higher volume of PRs and commits \(Boris himself reported landing ~259 PRs in a single month using these methods\).

What is your current bottleneck with Claude Code?

[https://x.com/bcherny/status/2017742741636321619?s=46&t=vYJQndr-Zz95Y-VgujlWVw](https://x.com/bcherny/status/2017742741636321619?s=46&t=vYJQndr-Zz95Y-VgujlWVw)

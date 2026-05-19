# Another little gem from today - Status Line Builder Prompt

**Created:** 2026-04-16
**Upvotes:** 6
**Comments:** 0
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/another-little-gem-from-today-status-line-builder-prompt

---

Statusline is a super underutilized feature that is really cool to have if you use Claude Code in the terminal a lot.

Basically just allows you to customize the statusline of claude code to show you whatever you want. Claude code has a built in /statusline command to do this, but I felt it usually creates the statusline without enough questioning and ideas from you in how you can make it genuinely useful, so I put together this little prompt that elicits a bit more from you upon statusline creation.

This is a prompt you paste into Claude Code. Before it writes any config, it asks you five questions about your actual workflow. What you check constantly, what files track your work state, what APIs you monitor, what would make you look at the status bar and immediately know something needs attention. Then it enters plan mode, proposes the full setup for your specific situation, and waits for your approval before touching anything.

Here is what the status line can actually show.

The base stuff: model name, current directory, git branch, context percentage. The context one color-codes, green when you are fine, yellow when you are getting close, red when you are nearly out, stuff like that.

But it can show anything your shell can access. Local file counts, calendar events, API responses, CLI output. The script runs on every update so anything you can get in under a second is fair game.

For cortextOS users: I have mine showing the current agent name \(nick vs boris vs paul\), pending task count from the bus, and my 5-hour rate limit usage \(this is just for when I boot up the agents manually in their workspace on my computer for deep work, obviously no statusline in telegram, yet...\). I can tell at a glance which session I am in, how loaded the queue is, and how close I am to burning through my usage.

The prompt walks you through building exactly what is useful to you, not a generic setup.

[docs.google.com/document/d/1apoR55bEWj8OBvnmT-Fy7FjfEgUdtWECxPW6vXZgCqA/edit](http://docs.google.com/document/d/1apoR55bEWj8OBvnmT-Fy7FjfEgUdtWECxPW6vXZgCqA/edit)

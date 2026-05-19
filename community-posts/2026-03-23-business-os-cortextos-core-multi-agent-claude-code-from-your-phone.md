# Multi-Agent Claude Code from Your Phone: CortextOS Core

**Created:** 2026-03-23
**Upvotes:** 28
**Comments:** 94
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/business-os-cortextos-core-multi-agent-claude-code-from-your-phone

---

Business OS which I've been teasing is becoming CortextOS 🧠. Today I'm releasing the core infrastructure, the foundation everything else is built on. Full CortextOS coming later this week.

Claude Code keeps shipping features for remote control, persistence and scheduled tasks. Dispatch, remote MCP, Telegram channels, /loop, scheduled tasks. They all miss critical pieces in my opinion that make them feel much less seamless than something like OpenClaw.

Channels integration pauses your entire session when Claude needs permission, you have to walk back to your computer to approve and can't continue remotely. Plan mode and AskUserQuestion block continuation of the session in telegram for the same reason. /loop tasks expire after 3 days and so aren't truly persistent. There is also no native way to run multiple agents that talk to each other, or create new agents remotely \(not natively possible in OpenClaw either\). And response times through channels are a bit slower than I would like.

I built CortextOS core to solve all of these problems with one integrated system built on top of Claude Code. Every agent in CortextOS is a full Claude Code instance. Your existing MCP servers, skills, plugins, hooks, all of it carries over automatically. Subagents, agent teams, explore agents, plan agents, everything Claude Code can do natively, your remote agents can do too, all controlled from telegram. And when Anthropic ships updates to Claude Code, your agents inherit them automatically. No migration, no rebuilding. This is built on top of Claude Code's infrastructure and security, not a separate framework like OpenClaw.

Here's some more details about the features that CortextOS core offers, install today with link below, no technical knowledge necessary:

~2 second message delivery - your Telegram message hits Claude's context window in about 2 seconds. Faster than the native Telegram channels integration

Full Telegram control - text back and forth with Claude Code from your phone, same as being at your terminal


---

## Top Comments (sample)

- **+2** Can't wait to use this!
- **+1** works ... James .. great job ....
  - **+0** [@Benjamin Law](obj://user/676db2e44ede421e8a511a867646bc8c) Lets go! Excited to see what you build with this
- **+1** Oooh exciting thank you
  - **+0** [@Kyle Behrend](obj://user/5d15c51354014ac0aaa76caab2e931ec) ofc!
- **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) this looks awesome - I joined after seeing you talk about this. Question - as someone with a few months trying different approaches in claude code - how do i go about cleaning up what i've built with GSD and just yelling at Claude a lot and wire in the frameworks you've built?
  - **+0** [@Josh Weiss](obj://user/b40e33ce27f84c0abac9db2bd225ecc3) this is the eternal question. I have the same issue. Honestly it will require some of your own attention looking through the files and reformatting everything using Claude code as the actual implementer of the reformat, but you understanding exactly what’s going on to really preserve your system. A mindset shift is also necessary to avoid this problem in the future. When you build stuff, try to make it as modular and agent friendly as possible. Contain scripts in self contained skills where possible, so systems are easy to port between architectures when big changes happen
- **+2** Works like a charm, can't wait to see its evolution!
  - **+0** [@David Noguerol](obj://user/826ba129c48849af98ebc6481a95cc44) let’s go!
- **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) I'm noticing that when I message this thing it will take a while to get back to me, or not reply at all for a while, not really sure whats happening. Is this normal? and how can I attach to this sesions?
  - **+0** [@Josh Weiss](obj://user/b40e33ce27f84c0abac9db2bd225ecc3) this is sometimes normal behavior as Claude code may be working. To test messaging speed, message “hi” and see how quickly it responds, this shows you raw messaging speed. Any additional delay is Claude code actually working before it sends you a response. Depending on the task, sometimes Claude code might forget to message you back. This is a result of the prompting system not being strong enough which I’m working on and if you find solutions to, you should make a PR to the repo and I’ll integrate. For me it is reliable 95% of the time tho so make sure all the files installed correctly \(claude.md, messaging skill, etc\). To attach to the session, just ask your agent it’s Tmux attach command through telegram and run that in a terminal to see what’s going on. I’m adding a feature that adds the “typing” indicator to telegram so you can be more confident when Claude code is typing versus actually stopped
  - **+0** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) this makes sense, typing will help, also a dashboard of some type. I've been building a dashboard but it always seems to feel more like fluffy grapchis than actually something useful.
    
    on the "already done" side claude mem dashboard is amazing.
    
    but still trying to have a handle on better whats happening at any one time.
- **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) how do we do multi threaded chats with TG - you mentioned that in the IG post?
  - **+0** [@Josh Weiss](obj://user/b40e33ce27f84c0abac9db2bd225ecc3) Just as your agent to set it up! The whole setup is built in knowledge for your agents so they can spin up new ones for you. In your existing agent chat just ask it to spin up another crm agent and it will tell you to create a new bot token in bot father, send it to it, and set it all up for you. Then you can chat to them separately in their own channels, and they can chat back and forth with each other. Groupchat functionality coming very soon.
  - **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) ah perfect.
  - **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) so I did this - have 4 chats setup, all added to cortext. but when i message from one of those chats, the reply comes back in the main channel. its as if hte inboud works but the outbound comes all to the primary channel, defeats the purpose. I'm trying to fight with it to fix right now but the default logic seems broken I'll let you know if i fix it
  - **+0** [@Josh Weiss](obj://user/b40e33ce27f84c0abac9db2bd225ecc3) this is odd. This means it’s using your original bot token when sending you responses. Tell it that and ask it to see where bot tokens are beings stored and how they are exported when it called the message respond script. This hasn’t happened to me. Let me know what you find and if it’s a core issue in the code ask your agent to make a PR to the remote repo with the fix.
  - **+0** [@Josh Weiss](obj://user/b40e33ce27f84c0abac9db2bd225ecc3) have you Tmux attached to make sure they’re all running separately?
  - **+0** [@Josh Weiss](obj://user/b40e33ce27f84c0abac9db2bd225ecc3) the agents can manage each other so yours should be able to figure this out
  - **+0** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) sounds like it, this is the name of the secondary channel tmux attach -t crm-default-clearpath-dev
  - **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) yup trying!
  - **+0** [@Josh Weiss](obj://user/b40e33ce27f84c0abac9db2bd225ecc3) okay sweet let me know what you find out. Still a very new project and we’ve already shipped 4 PRs since launch so I’m sure lots of edge cases to patch up
  - **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) all g keep you posted - hope to setup Slack next instead of TG once this works
  - **+0** [@Josh Weiss](obj://user/b40e33ce27f84c0abac9db2bd225ecc3) let me know when you plan to set up slack - this will be complicated but it’s an integration I want to add to the core system so I’m interested in working on it with you
  - **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) prefect we can do it whenever. I'm enjoying your content - 26 yaers in IT but never really programmed and really rying ot round the bend with agentic workflwo - I"m like. 80 percent on so many things right now lol

# Has anyone else had their Mac overheating from the Telegram loop?

**Created:** 2026-03-16
**Upvotes:** 2
**Comments:** 5
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/has-anyone-else-had-their-mac-overheating-from-the-telegram-loop

---

I've been setting up the openclawd code bot today and my Mac has got really hot twice. Checked and my load average was at 149 \(M1 Pro\).

I think what's happening is the scheduled task spawns a new Claude process every time it fires, and each one takes a few minutes to boot up, load MCP servers, check Telegram etc. When I had it set to every 1 minute, they were stacking up — found over 100 Claude processes running at the same time.
I've moved it to every 10 minutes and it's fine now, but that's a long wait for a telegram reply. Not sure if I've done something wrong or if this is just how it works. Would appreciate any help.
How are you guys running yours?

# A question about prompt injections?

**Created:** 2026-05-15
**Upvotes:** 2
**Comments:** 7
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/a-question-about-prompt-injections

---

How I’m thinking about prompt injection notifications while my agent is doing the work
I’ve been tightening the security rules around my agentic workflow, especially because I’m using Claude/Hermes-style sub-agents, MCP tools, web search/scraping, and a VPS setup.
One thing I noticed is that prompt injection notifications can show up when an agent or sub-agent reads untrusted content from the web, APIs, scraped pages, PDFs, search results, etc. My current understanding is that this does not automatically mean the VPS or system is compromised. It usually means the model encountered instruction-like text inside external content, such as:
“Ignore your previous instructions.”“Reveal your system prompt.”“Modify your files.”“Run this command.”
In other words, the detection itself can actually be a good sign: the model noticed something suspicious.
But the important question is not just, “Did the agent see prompt injection?” The better question is:
What permissions did the agent have when it saw it?
That is where I think the real security design matters.
For example, if a research sub-agent is only allowed to browse and write findings into /outputs, /scratch, or /reports, then a prompt injection attempt is much less dangerous. But if the same sub-agent can browse the web, edit source code, run shell commands, read .env, access secrets, modify [claude.md](http://claude.md), push to Git, or deploy, then the risk is much higher.
So the principle I’m trying to adopt is:
Untrusted input access should not be combined with privileged execution access.
In practice, I want to move away from simply prompting:
“Dispatch a sub-agent to do X, Y, Z.”
And move toward something more like:
“Dispatch a research_agent with Tier 1 permissions. It can browse and write evidence, but it cannot run shell commands, edit code, access secrets, or modify config/instruction files. If it needs higher privilege, it must stop and request escalation.”
The setup I’m thinking about is a tiered agent system:

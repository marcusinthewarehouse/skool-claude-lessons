# Sonnet 1M context window param with Cortext Agents

**Created:** 2026-04-16
**Upvotes:** 5
**Comments:** 0
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/sonnet-1m-context-window-param-with-cortext-agents

---

Just a heads up,

I ran into an issue with Cortext today where I was using sonnet agents and they were dying because they had 1M context window enabled \(automatically enabled with a new update\), but don't autocompact and require you to use /extra-usage to continue, and don't autocompact so that agents were getting stuck.

To fix this you have to disable 1M context in the settings.json of these agents. Change pushed to the remote repo of cortext for new agents but you may have to update your configs if you're using sonnet agents to prevent this.

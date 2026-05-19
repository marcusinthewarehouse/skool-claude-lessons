# Codex agents in Cortext!

**Created:** 2026-05-09
**Upvotes:** 8
**Comments:** 14
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/codex-agents-in-cortext

---

You can now run OpenAI's Codex CLI harness as a full cortextOS agent runtime, right alongside Claude Code. Same message bus, same crons, same dashboard, same skill tree, fully featured cortext-native codex agents that collaborate and coexist with your Claude code agents. The model it uses defaults to gpt-5-codex but can be changed to any model available on codex CLI .

To spin up a Codex agent just make sure your cortext is up to date, you have codex installed and authenticated on your machine, and ask your orchestrator to spin one up!

The cool thing is that you're not building a separate Codex integration into your Claude code agents, you're subbing out Claude code for codex 1:1 as a full cortext agent. Slash commands \(especially /goal\), skills, and cost tracking all work the same as with Claude code.

A few things worth knowing on the features side. The Telegram connector handles photos, voice messages, documents, and reply threading with the same shape Claude agents see. There's a prompt-injection guard baked in, so a hostile message body can't redirect where the agent replies.

One current limit: the orchestrator and analyst templates are not full Codex native yet, thought you could hack it together super easily, these come next. The general agent template is fully supported today for all your specialists.

Still new so might be some rough edges, feel free to push fixes as you find them!

Happy codexing 🤖

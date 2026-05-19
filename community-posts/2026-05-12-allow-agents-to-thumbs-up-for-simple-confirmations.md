# Allow agents to thumbs up for simple confirmations

**Created:** 2026-05-12
**Upvotes:** 2
**Comments:** 10
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/allow-agents-to-thumbs-up-for-simple-confirmations

---

agents currently reply to every telegram message with a full verbal "got it" / "on it" / "sounds good." noise.

new cortextos PR adds `bus react-telegram <chat-id> <message-id> \[emoji\]` so the agent can ack with a thumbs-up instead of clogging the chat.

[https://github.com/grandamenium/cortextos/pull/406](https://github.com/grandamenium/cortextos/pull/406)

usage policy lives in each agent's prompt. defaults: 👍 = got it. 👀 = looking. 🔥 = endorsing. ✅ = done. verbal if there's content.

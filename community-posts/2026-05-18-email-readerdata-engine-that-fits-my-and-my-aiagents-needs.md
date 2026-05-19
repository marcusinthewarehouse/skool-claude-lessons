# email reader/data engine that fits me and my aiAgents needs

**Created:** 2026-05-18
**Upvotes:** 3
**Comments:** 6
**Labels:** 59ef34684a11462bac017ad7f612ac9d
**Post URL:** https://www.skool.com/agent-architects/email-readerdata-engine-that-fits-my-and-my-aiagents-needs

---

I wanted a local-only mail reader/data-engine that turns my inbox into clean, enriched, tagged data, so my AI agents can query it via a read-only MCP instead of polling raw IMAP and guessing what's important and more importantly whats SAFE and SECURE to process in its pipeline.

There are email integrations for AI to clean my inbox as a user and plenty of good email clients. There are MCP's for email providers. None of them fit my goals of trust, compliance and not wasting tokens, ever!

So. built my own email data store/reader. local everything. no cloud, no oauth, no "let acmeAI manage my inbox for me" nonsense. a stupid project called myCrazyMail because it was, somehow ended up being the most useful piece of software i own. this is using only gpt-oss-20b on local devices.

mutt vibes on the front, local gpt-oss-20B model on the back, five layers of nonsense stacked on top. trust panel that reads the actual headers, embeded links, hidden characters and validates and enriches all that data \(as "From" is a suggestion\). Tagging that mixes machine signals with my own. Then onto the personal things such as a subscription detector that found things i didnt know i was still paying for. "shape of my spending" view that uh. yeah. didnt love what it showed me and my aliexpress yearly spend graph for the last 10 years as the definition of 'instant depression' and now as the data is in a proper model/structure I can ask my LLM's anything about it and get real, valid insights.

endgame: read-only MCP server on top, so my agents query the safe, cleaned and enriched data instead of polling raw imap and guessing what's a receipt vs a newsletter. no send, no delete, no reply. no unprotected actions. agents read, I act.

The best part about all of it really is, an AI action on Codex/Claude is only the minimal viable data required in the CTX window, not reading every whole 100k email, deciding if its actionable and what to do with it around agent loops. its the 10 structured json values out of a structured data set from a structured query for a tool call.

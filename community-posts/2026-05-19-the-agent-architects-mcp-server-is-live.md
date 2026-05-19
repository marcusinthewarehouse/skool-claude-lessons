# ‼️ The Agent Architects MCP server is live

**Created:** 2026-05-19
**Upvotes:** 8
**Comments:** 9
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/the-agent-architects-mcp-server-is-live

---

You can now connect Agent Architects directly to Claude Desktop, Claude Code, Codex, Hermes, Openclaw, Cursor, Windsurf, or any remote MCP client.

This lets your AI client search Agent Architects while you work:

- classroom lessons
- lesson resources
- video transcripts
- live call transcripts
- posts and comments
- member profiles

Member profiles, posts, and comments is my favorite. You can find the people that think like you, want what you have, and have what you want. Then get the link to their profile to contact them directly. HUGE unlock in my opinion.

It is read-only. It cannot post, DM, change your Skool account, or modify anything. It only retrieves AA knowledge and brings it into your agent's context.

To install manually, just run this command in your terminal:

claude mcp add --transport http agent-architects [https://aa-mcp-server-production.up.railway.app/mcp](https://aa-mcp-server-production.up.railway.app/mcp) --header "Authorization: Bearer aa_community_UBbPhkE_pHmOnZDosjBpETSaPWNYDBF_jrU0UoXttNmIId6Z"

To have your agent install, ask your agent to add this into your MCP config:

{
"mcpServers": {
"agent-architects": {
"url": "[https://aa-mcp-server-production.up.railway.app/mcp](https://aa-mcp-server-production.up.railway.app/mcp)",
"headers": {
"Authorization": "Bearer aa_community_UBbPhkE_pHmOnZDosjBpETSaPWNYDBF_jrU0UoXttNmIId6Z"
}
}
}
}

Restart your client after saving the config.

First test prompt:

Use the Agent Architects MCP to search for context engineering lessons. Return the best sources and links.

Then try:

Use get_lesson from the Agent Architects MCP to fetch "7.1 Context Engineering" from Claude Code Fundamentals. Summarize only that lesson.

A few good use cases:

Search Agent Architects for lessons about MCP servers.

Get the OpenClaw Fundamentals lesson "3. Install & Onboard" and summarize the Telegram setup.

Search Live Call Recordings for MiroFish and the Cortex roadmap.

Who in Agent Architects should I meet if I am building sales automation?

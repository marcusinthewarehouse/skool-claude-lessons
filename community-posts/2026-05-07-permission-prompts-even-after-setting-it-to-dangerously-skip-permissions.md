# Permission prompts even after setting it to dangerously skip permissions

**Created:** 2026-05-07
**Upvotes:** 4
**Comments:** 4
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/permission-prompts-even-after-setting-it-to-dangerously-skip-permissions

---

Just a follow-up from our call tonight, thought it would be helpful to post it to the whole group rather than shooting in over in DMs to just a couple folks: [@Robert Sahakyan](obj://user/d63601ce145b4334ba05dc1e260e3738) [@Max Lambo](obj://user/eb27edce75db40aa9c0573e2855f100e)

The "dangerously skip permissions" mode \(or bypassPermissions in your settings\) covers some of Claude's built-in tools. Bash, Read, Write, Edit, Glob, Grep, the basics. Those just go.

But two categories of tools STILL prompt even with bypass on:

1️⃣ MCP server tools \(Playwright, GitHub, Supabase, Telegram, Notion, Canva, etc.\) — every individual call from each server still has to ask. And it asks AGAIN every time you hit a different tool from the same server. 🙃

2️⃣ Some built-in tools NOT in the default bypass set. PowerShell on Windows is the big one. Also things like Monitor, BashOutput, KillBash. These look like normal tool names \(no mcp__ prefix\) but they still prompt until you name them explicitly.

🛠️ THE FIX

Add an allow list in your project's settings.json. Wildcards for MCP servers, bare tool names for built-ins.

Create \(or edit\) this file in your project's root folder:

.claude/settings.json

Drop this in \(add anything you use that I missed\):

{
"permissions": {
"allow": \[
"Bash", "PowerShell", "Read", "Write", "Edit",
"Glob", "Grep", "Agent", "Skill", "TodoWrite",
"WebFetch", "WebSearch", "NotebookEdit",
"Monitor", "BashOutput", "KillBash",
"mcp__playwright__*",
"mcp__github__*",
"mcp__supabase__*",
"mcp__telegram__*",
"mcp__notion__*"
\],
"defaultMode": "bypassPermissions"
}
}

The two patterns to know:

✅ MCP tools → wildcard the whole server: mcp__<servername>__* covers every tool from that server. One line, infinite peace.

✅ Built-in tools → just the bare name: "PowerShell", "Monitor", etc. No wildcard needed.

When a NEW prompt pops up for something you haven't allowlisted yet, just figure out which category it falls in and add it. Done forever.

🤖 MAKE YOUR AGENT DO THIS FOR YOU

Drop this into your [CLAUDE.md](http://CLAUDE.md) so it handles the cleanup automatically every time a prompt happens:

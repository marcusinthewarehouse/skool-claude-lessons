# Programmatic MCP Tool Calling Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=dd4f9db7c1de4d44b35e69ef4b08d41c
**Scraped:** 2026-05-19

---

A Claude Code skill that lets you call MCP server tools directly from Python or Node.js scripts, bypassing the AI agent entirely. Instead of every tool call going through the LLM (burning tokens and adding latency), your scripts connect to the MCP server process directly using the same JSON-RPC 2.0 protocol. Useful for batch operations, chained pipelines, scheduled jobs, and testing MCP servers.

## How MCP Tool Calling Normally Works

When you connect an MCP server to Claude Code (via .mcp.json or claude mcp add), Claude Code acts as the MCP client. Every tool call flows through the AI agent: you ask Claude to do something, Claude decides which tool to call, sends the JSON-RPC request to the server, gets the result, and presents it to you. This works great for interactive use but has three costs: each call burns tokens, adds latency from the LLM round-trip, and intermediate results pollute your context window.

## The Problem This Skill Solves

There is no built-in way to call MCP tools from a script. If you want to read 100 files through a filesystem MCP server, list all Notion databases, or batch-query a database server, you must ask Claude to do each one individually. Each call goes through the LLM, consuming tokens and time. For repetitive operations, scheduled automation, or CI/CD pipelines, you need to remove the AI from the loop entirely and talk to the MCP server directly.

## How This Skill Improves on Native Functionality

This skill provides two guided workflows:

- Workflow 1 - Convert MCP to Scripts: Walks you through extracting your MCP server config, installing the Python or Node.js MCP SDK, discovering available tools, and writing a script that calls any tool programmatically. Includes templates for single tool calls and a reusable client wrapper.
- Workflow 2 - Chain Multiple Tools: Shows how to pipe output from one tool call as input to the next within a single script. Includes patterns for sequential pipelines, cross-server chaining (calling tools from two different MCP servers in one script), and batch operations with proper error handling.
- Tested with real servers: All code examples have been tested against the official filesystem MCP server and the Playwright MCP server. The skill documents real gotchas like MCP errors being returned in result.isError instead of raised as Python exceptions.
- Ready-to-use scripts: The repo includes four helper scripts you can run immediately - discover_tools.py, call_tool.py, call_tool.js, and chain_tools.py.

## Installation

Clone the repo into your Claude Code skills directory:

```
git clone https://github.com/grandamenium/programmatic-mcp-skill.git ~/.claude/skills/programmatic-mcp
```

You also need the MCP Python SDK installed:

```
pip install mcp
```

Once installed, trigger the skill by asking Claude Code to help you call MCP tools programmatically, or reference the [SKILL.md](http://SKILL.md) directly. The skill includes complete code templates for Python and Node.js.

---

GitHub Repository: https://github.com/grandamenium/programmatic-mcp-skill

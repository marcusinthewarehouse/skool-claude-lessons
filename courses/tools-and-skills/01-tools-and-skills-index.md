# Tools and Skills Index

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=1be090b96cf947e8a2144ba22cac2220
**Scraped:** 2026-05-19

---

Welcome to the Tools and Skills catalog. Each page in this course covers a specific open-source tool or skill built for Claude Code. You will find a description of what it does, how it works, how it improves on native Claude Code functionality, installation instructions, and a link to the public GitHub repo.

Catalog

Memory Management Skill - Optimizes Claude Code's native auto-memory by enforcing a 200-line index structure with topic-based file organization. Keeps your context lean and searchable.

Nano Banana 2 - Image Generation Skill - Generate and edit images directly from your terminal using Google's Gemini 3.1 Flash Image API. Supports 4 resolution tiers, 14 aspect ratios, image search grounding, and a draft-iterate-final workflow.

General Task Agent Orchestration Skill - A meta-orchestration framework (M2C1) for autonomous software development. Converts brain dumps into phased implementation plans with parallel research, discovery questioning, task sharding, synergy review, and multi-angle testing.

Reminder Processor - Cowork Scheduled Task Skill - Turns Apple Reminders into AI-completed tasks automatically. Uses Claude Desktop Cowork scheduled tasks to pull all reminders daily, classify which ones AI can handle, and complete them with parallel subagents.

Programmatic MCP Tool Calling Skill - Call MCP server tools directly from Python or Node.js scripts without the AI agent in the loop. Includes workflows for converting any MCP server to programmatic scripts, chaining multiple tool calls, cross-server pipelines, and batch operations. Tested against filesystem and Playwright MCP servers.

Multi-Agent OpenClaw Setup Skill - Guide for creating and managing multiple OpenClaw agents from a single gateway. Covers agent creation, workspace setup, dedicated Telegram bots per agent, channel routing and binding precedence, per-agent model selection, sandbox and tool restrictions, inter-agent messaging, and common multi-agent patterns. Validated against OpenClaw v2026.2.26.

OpenClaw Reliability Guide - Complete downloadable guide covering weekly bootstrap file audits, skill creation with crons and heartbeats, and multi-agent architecture with Telegram integration. The three systems that make OpenClaw agents work reliably.

GWS Meta-Workflows Skill - Six composable meta-workflows that chain Google Workspace CLI (gws) commands into end-to-end automations. Includes inbox triage, meeting prep briefings, client onboarding, weekly digests, email prompt injection scanning, and scheduling conflict resolution.

Autoresearch-Anything Skill - Autonomous experimentation pipeline for any business metric using Karpathy's autoresearch pattern. Guided Q&A setup, deep domain research, project scaffold generation, and persistent execution via launchd or GitHub Actions.

Skill-Optimizer (4/16/2026) - Automatically audits and improves your Claude Code skills by reading JSONL transcripts and scoring each skill across 5 dimensions. Outputs analysis.md, diff.patch, and history.json so you can iterate toward a perfect score.

StatusLine Builder (4/16/2026) - A guided prompt you paste into Claude Code that asks 5 questions about your workflow before building a custom status line. Can display model, git branch, context %, task count, agent queue depth, Skool member count, API health, or any shell-accessible data.

local-ultrareview Skill (4/17/2026) - Local version of /ultrareview with live agent logs and implementation plan. 3 parallel Opus review agents + synthesis + implementation plan + option to apply fixes.

Claude Code /schedule Guide (4/17/2026) - Setup guide for running agents on Anthropic cloud infrastructure on a schedule. Includes MCP config, secrets management, and 3 overnight workflow templates (nightly bug fix, weekly doc sync, PR review on push).

Claude Managed Agents (4/19/2026) - Hosted platform for deploying persistent agents via Anthropic API. Full sandbox, bash access, file system, MCP servers, multi-agent coordination, and credential injection via Vaults. Complete reference doc with every endpoint, event schema, tool config, and three end-to-end implementation examples.

Social Media Insights Skill: A full 17-step Apify pipeline that scrapes TikTok, Instagram, and Twitter posts, analyzes what's working, and generates agent recommendations based on what your audience is actually engaging with.

Agent Security Audit Skill (4/30/26) - Deep audit prompt that scans your agents for the most common security vulnerabilities: prompt injection, credential exposure, unvalidated inputs, privilege escalation, and output trust issues. Built from real vulnerabilities found in production agent deployments.

Infisical Vault Skill (4/30/26) - Pulls secrets from Infisical into your Claude Code agent at runtime so API keys never live in .env files. Keys fetch on demand, never write to disk, and rotate automatically.

Blotato Posting Skill (4/30/26) - Lets Claude Code post videos and content to TikTok, Instagram, YouTube, LinkedIn, and X in one command. Point it at a file and a caption and it handles upload, format conversion, and submission.

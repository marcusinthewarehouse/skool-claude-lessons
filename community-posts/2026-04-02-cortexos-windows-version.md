# CortexOS Windows Version

**Created:** 2026-04-02
**Upvotes:** 4
**Comments:** 2
**Labels:** 59ef34684a11462bac017ad7f612ac9d
**Post URL:** https://www.skool.com/agent-architects/cortexos-windows-version

---

Hey, I took the challenge and made a fork that allows it to work between MacOs and Windows 10/11. I had to install the OpenAI Codex plugin for Claude and use its adversary review to bring Claude in the right direction for this port and used Codex Code Review extensively to fix things it missed, but its working. You do not need the Codex plugin for this to work, lol. I had it also add some security hardening and enhancements like a graceful 5 minute warning before the 71 hour restart. Here is the changelog and info to install:

CortextOS Windows Port — Changelog

Project: [https://github.com/grandamenium/claude-remote-manager](https://github.com/grandamenium/claude-remote-manager)
PR: [https://github.com/grandamenium/claude-remote-manager/pull/36](https://github.com/grandamenium/claude-remote-manager/pull/36)

---
What is CortextOS?

CortextOS \(Claude Remote Manager\) lets you run persistent 24/7 Claude Code agents controlled entirely from Telegram.
Approve permissions, answer questions, manage scheduled tasks, and communicate with multiple agents — all from your phone.
Previously macOS-only.

What's New

Full Windows Support
- Runs on Windows 10 \(1809+\) and Windows 11 using Git Bash
- PM2 replaces launchd for process management
- node-pty \(Microsoft's ConPTY wrapper\) provides the real terminal Claude Code needs
- Telegram polling runs natively in Node.js — no bash fork instability
- Auto-installs jq and node-pty during setup
- Zero changes to existing macOS functionality

Graceful 71-Hour Restart \(both platforms\)
- Agents now receive a 5-minute warning before the scheduled session restart
- Claude has time to finish current work, save state, and notify the user via Telegram
- Previously the restart happened immediately with no warning, potentially interrupting mid-task work

Security Hardening \(both platforms\)
- All terminal input sanitized to strip control characters and ANSI escape sequences
- Shell injection prevention — all child process calls use array arguments instead of string interpolation

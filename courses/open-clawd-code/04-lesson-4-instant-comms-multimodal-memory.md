# Lesson 4: Instant Comms + Multimodal Memory

**Section:** Module 1: Setting Up Open Clawd Code
**Course:** Open Clawd Code (3/9/26)
**Skool URL:** https://www.skool.com/agent-architects/classroom/3caebf63?md=19c24e0bbca3475d8d7e3d0eef722609
**Scraped:** 2026-05-19

---

Two upgrades that make your agent dramatically better: instant Telegram message delivery (under 1 second instead of up to 60) and a searchable multimodal knowledge base that gives your agent persistent memory across sessions.

## What You'll Learn

- Replace the 60-second /loop Telegram cron with a real-time daemon that delivers messages in under 1 second via tmux paste-buffer injection
- Photo messages and inline button callbacks handled automatically
- Install a multimodal RAG knowledge base - search across videos, images, audio, PDFs, and documents using semantic search powered by Gemini Embedding 2 + ChromaDB
- Give your agent persistent, searchable memory that survives across session restarts

## In This Lesson

In Lesson 3, your agent checks Telegram every 60 seconds using a /loop cron. That means when you send a message, you could wait up to a full minute before your agent even sees it. This lesson replaces that with a background daemon called fast-checker.sh that polls every single second and injects messages directly into your agent's tmux session via paste-buffer. The result: your agent responds in under a second.

Then you'll install a multimodal RAG knowledge base that lets your agent ingest and semantically search across any file type - videos, images, audio, PDFs, Word docs, spreadsheets, code, and plain text. This gives your agent true long-term memory that persists across session restarts and is searchable by meaning, not just keywords.

The best part: you just give your agent a prompt and it does everything for you. It upgrades its own communication system, removes the old cron, installs the new scripts, then walks you through setting up the knowledge base via Telegram conversation.

## How to Use

You need a working agent from Lessons 1-3 (running in tmux via launchd). Then:

1. Attach to your agent's tmux session: tmux attach -t my-agent
2. Give your agent the full prompt from the PROMPT.md file in the GitHub repo linked below. Copy the entire contents of PROMPT.md and paste it into your agent's session.
3. Your agent handles everything from there - it creates the scripts, removes the old cron, updates its own config, tests the instant comms, then walks you through the knowledge base setup via Telegram.
4. Restart your agent after Phase 1 to activate the fast-checker daemon, then continue to Phase 2 (multimodal RAG) in the new session.

## Prerequisites

- Completed Lessons 1-3 (running agent with tmux + launchd)
- tmux installed (brew install tmux)
- For multimodal RAG: free Gemini API key from https://aistudio.google.com/apikey

## Resources

- Upgrade Prompt + Scripts: Lesson 4 - Instant Comms + Multimodal Memory https://github.com/grandamenium/openclawd-lesson-4-instant-comms-memory
- Multimodal RAG Knowledge Base: https://github.com/grandamenium/multimodal-rag

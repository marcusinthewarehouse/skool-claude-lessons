# Multimodal RAG Knowledge Base Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=5a9e7568d74540cf8816fc1b6dc2ad7a
**Scraped:** 2026-05-19

---

Build a fully local multimodal knowledge base for your AI agent. Ingest videos, images, audio, PDFs, Office docs, and code into a searchable vector database using Google's Gemini Embedding 2. Your agent can query it and get text answers with source file paths - not just file pointers.

## How It Works

Most RAG systems only handle text. This one handles everything. The key insight: you can't just embed a video into a vector database and expect useful answers. A naive system just returns a video clip and says "the answer is in there." This skill runs every non-text file through Gemini Flash first to generate a detailed text description (transcript, visual analysis, key topics), then embeds that description alongside the raw media. So when you query, you get actual text answers your agent can reason about.

## The Problem This Skill Solves

Before Gemini Embedding 2, you could only put text into vector databases. Videos, images, and audio were off-limits or required hacky workarounds like manually writing descriptions. Now you can embed media natively, but most implementations get it wrong - they embed the video and return video clips instead of text answers. This skill implements the proper architecture so your agent gets searchable, queryable content from ANY file type.

## What This Skill Supports

- Video (.mp4, .mov, .avi, .mkv, .webm) - FFmpeg splits into 60s chunks, Gemini Flash transcribes each. 1GB+ files handled via audio extraction
- Images (.png, .jpg, .jpeg, .gif, .webp) - Gemini Flash generates detailed visual descriptions. Multimodal embedding captures both text and visual semantics
- Audio (.mp3, .wav, .m4a, .ogg, .flac) - Chunked and transcribed with speaker identification
- PDF - Page-by-page extraction including descriptions of charts, diagrams, and tables
- Word (.docx, .doc) - Local text extraction preserving heading structure and tables
- PowerPoint (.pptx, .ppt) - Per-slide extraction with speaker notes
- Excel (.xlsx, .xls) - Per-sheet extraction with column headers and data
- Text/Code (.md, .py, .js, .ts, .go, .sh, .json, .yaml + 20 more) - Smart chunking at paragraph boundaries

## Installation

Clone the skill into your Claude Code skills directory:

```
git clone https://github.com/grandamenium/multimodal-rag.git ~/.claude/skills/multimodal-rag
```

Then just tell your agent "set up the multimodal knowledge base" or "I want to create a knowledge base." The skill walks you through everything - installs dependencies, gets your API key, ingests your files, tests that it works, and configures how your agent uses it. You don't need to run any scripts manually.

All you need beforehand is a free Gemini API key from https://aistudio.google.com/apikey (or have GEMINI_API_KEY already set in your environment).

---

GitHub Repository: https://github.com/grandamenium/multimodal-rag

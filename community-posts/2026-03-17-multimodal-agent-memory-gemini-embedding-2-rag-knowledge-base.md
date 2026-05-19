# Multimodal Agent Memory: Gemini Embedding 2 RAG Knowledge Base

**Created:** 2026-03-17
**Upvotes:** 18
**Comments:** 13
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/multimodal-agent-memory-gemini-embedding-2-rag-knowledge-base

---

New skill that gives your Claude Code agent a searchable knowledge base across ALL file types - not just text. 🧠

Google dropped Gemini Embedding 2 which can natively embed videos, images, and audio. This skill setups up the RAG pipeline for all file types, filtering images, audio and videos through Gemini Flash first to generate text descriptions, then embedding both together. So your agent gets real text answers it can reason about, with source file paths and clip lengths of the originals. 🔥

What it handles:
[ul][li]Videos \(any size, even 1GB+\) - splits into chunks, transcribes via audio extraction 🎬[li]Images - full visual descriptions with layout, text, diagrams 🖼️[li]Audio - chunked transcription with speaker ID 🎙️[li]PDFs - page-by-page with chart and table descriptions 📄[li]Word, PowerPoint, Excel - local extraction, no API needed 📊[li]Code and text files - smart chunking at paragraph boundaries 💻

Clone it, tell your agent to set it up, point it at your files. The skill handles the entire onboarding - dependencies, API key, ingestion, testing, and configuring how your agent uses it. Three autonomy modes: manual, suggested, or proactive. 🚀

git clone [https://github.com/grandamenium/multimodal-rag.git](https://github.com/grandamenium/multimodal-rag.git) ~/.claude/skills/multimodal-rag

Then just tell your agent "set up the knowledge base." It takes it from there.

⚡[https://github.com/grandamenium/multimodal-rag](https://github.com/grandamenium/multimodal-rag)


---

## Top Comments (sample)

- **+2** I added this to my prioritized feature BACKlog... Thank you
  - **+0** [@Rob Dube](obj://user/e76ccfa58d5e43ee95a44be1fdf82118) Glad to help!
- **+2** Is it paid or a free service?
  - **+1** [@Vitaliy K](obj://user/a8af52b5b9824de6bb47f98eff8fffce) Its paid but very cheap and you can get a good amount of free usage initially from free gemini credits. For instance, to injest almost all of my business OS materials, it cost only 2 cents
- **+3** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) Can you makae a use case video of this James? I was tryin to see how I can adopt this into my stack. bonified newb here, but eager to learn!
  - **+2** [@Theodore Chung](obj://user/ac39a58c530f4510b21510fadeabe85b) what's your stack now?
  - **+2** [@Theodore Chung](obj://user/ac39a58c530f4510b21510fadeabe85b) Yes coming soon!
  - **+2** [@Theodore Chung](obj://user/ac39a58c530f4510b21510fadeabe85b) I second Theodore. [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) I understand the ability but am interested to find a way to deploy it to my business \(using either Calude or OpenClaw\) -can you share in a video use-cases and what to do. Newb too, know a little about RAG agents...
  - **+1** [@David Hunter](obj://user/1117b24a286b457a9b6b2ba5a6f5926b) for the multimodal rag DB, plan to use notebookLM\(google\) instead of just gemini; to synthesize multiple videos at a time for a specific topic into a specific folder, I want to see if I can derive SOP drafts out of this. image using openclaw at the top and claude to do the heavy lifting.
- **+0** This is a proper unlock. Most RAG setups fall apart on anything that isn't clean text. The video chunking with audio extraction is the part I've been wanting for a while. Setting this up this week.
- **+1** 🔥
- **+0** Hi .. this is excellent and been wanting something like this! I read on Google that Embedding2 had only 2 minutes for video; what does this mean?
- **+0** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) im starting an AI Engineering bootcamp on 3/30 ran by Zach Wilson and DataExpert.io. A big part of it is going to be the RAG data pipeline. I’m still figuring out my capstone project but it will be compliance related. I’ll be doing a lot of social media posts about my journey and will posting here through out it. I’m sure I’ll bug this crew for help!!

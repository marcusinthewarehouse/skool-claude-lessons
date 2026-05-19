# Short Form + YouTube Video Scraper

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=596a3f44a5e14ccb8ea97b16671fdf36
**Scraped:** 2026-05-19

---

An open-source pipeline that scrapes, downloads, transcribes, and summarizes TikTok and YouTube videos into organized markdown files. Uses local Whisper for transcription so no API keys are needed for the core workflow. Built for content creators and researchers who want to build structured knowledge bases from video content.

## and run /start to set up the environment. The tool uses yt-dlp to download video audio, OpenAI Whisper running locally to transcribe it, and Claude Code to analyze and organize the results. Output goes to two directories: transcripts/ for raw transcripts with metadata, and summaries/ organized by topic with YAML frontmatter. A master [INDEX.md](http://INDEX.md) is generated automatically.

Slash Commandsronment Setup - Automates first-time setup: creates a Python virtual environment, installs all dependencies, checks for ffmpeg, and runs tests to verify everything works.

**/bulk** - Full Profile Processing - Processes all videos from a TikTok profile in one shot. Scrapes the profile, downloads audio, transcribes with Whisper, and generates topic-organized summaries. Tracks progress so you can resume if interrupted.

**/transcribe** - Single Video Processing - Paste one or more TikTok URLs and get transcripts plus summaries for just those videos. Handles various URL formats (full links, short links, vm.tiktok.com). Perfect for processing specific content without scraping an entire profile.

**/accounts** - Account Management - Add, remove, switch between, and process multiple TikTok profiles. Keeps each account organized separately with metadata stored in accounts.json.

**/skillify** - Knowledge Extraction - Converts your transcript summaries into reusable Claude Code skill files. Enriches them with web research so the resulting skills contain actionable, verified knowledge. Choose to save globally (~/.claude/skills/) or project-local.

- Features re-runs skip already-processed videos automatically
- Configurable Whisper models - choose tiny (fast) to large (accurate)
- Retry logic with exponential backoff on downloads
- Topic-based file organization with YAML frontmatter
- Master [INDEX.md](http://INDEX.md) generated automatically
- No API keys needed for core workflow
- URL auto-detection - paste a TikTok link and Claude handles the rest

Prerequisitesnstalled automatically by /start on Mac via Homebrew)

Claude Code

```
Installationhub.com/grandamenium/short-form-video-transcriber.git
cd short-form-video-transcriber
```

Then open in Claude Code and run /start.

---

 Repository: https://github.com/grandamenium/short-form-video-transcriber

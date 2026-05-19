# Reminder Processor - Cowork Scheduled Task Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=ef4824cd83c5481cb92d83d308a5a88b
**Resource:** Setup Guide (docx) (file: `reminder-processor-guide.docx`, id: `84b104b7c81945c5bde6da0e59c5bdf1`)
**Scraped:** 2026-05-19

---

A Claude Code skill that turns your Apple Reminders into AI-completed tasks automatically. Uses Claude Desktop Cowork's new scheduled tasks feature to run every morning, pull all your reminders, classify which ones AI can handle, and complete them with parallel subagents.

Add reminders like you normally would. Claude reads them, figures out what it can do (research, writing, analysis, planning, code, content creation, etc.), and knocks them out. Human-required stuff (calls, workouts, purchases) gets skipped. Hybrid tasks get the AI portion extracted and completed.

## How It Works

1. Claude pulls ALL incomplete reminders from Apple Reminders via osascript
2. 2. Uses LLM reasoning to classify each one (no rigid regex rules)
3. 3. Spawns parallel subagents for all AI-completable tasks
4. 4. Saves deliverables as markdown files to your workspace folder
5. 5. Marks completed reminders as done in Apple Reminders
6. 6. Reports a summary of what was completed, skipped, and failed

## What Gets Processed

AI-completable: research, writing, analysis, summaries, planning, code, content ideas, data processing, and general knowledge work.

Hybrid tasks: "Record Instagram reel about X" becomes a drafted script. "Set up LLC" becomes a research doc on requirements and costs. Claude extracts and completes the AI portion.

Skipped: Physical actions, financial transactions, account setup, health appointments, personal care, travel logistics, watching/listening.

## Requirements

- Mac with Claude Desktop (Pro, Max, Team, or Enterprise plan)
- Cowork mode enabled
- "Control your Mac" connector enabled in Cowork (for osascript/Reminders access)
- Apple Reminders (built into macOS)

## Installation

### Option A: Auto-Setup (Recommended)

Open Terminal and run:

```
git clone https://github.com/grandamenium/reminder-processor-skill.git
cd reminder-processor-skill
./setup.sh
```

Then restart Claude Desktop.

### Option B: Manual Install

1. Download the repo as a ZIP from GitHub (green "Code" button > "Download ZIP")
2. Extract the ZIP file
3. Open Finder, press Cmd+Shift+G, go to: ~/.claude/skills/
4. Copy the reminder-processor/ folder (containing SKILL.md) into that directory
5. Restart Claude Desktop

## Setting Up the Scheduled Task

This is the key step. You create a scheduled task in Cowork that triggers this skill automatically every morning.

1. In Cowork, make sure "Control your Mac" connector is enabled (Customize > Connectors)
2. Click "Scheduled" in the left sidebar
3. Click "+ New task"
4. Set Task name to: Morning Reminder Processor
5. Set Frequency to: Daily
6. Paste the prompt below into the Prompt field
7. Click Save, then click "Run now" to test

Prompt to use:

```
Run /reminder-processor to process my Apple Reminders.

Pull all incomplete reminders from Apple Reminders using the osascript MCP tool. For each reminder, classify it using your judgment:
- AI-completable tasks: spawn subagents to complete them in parallel
- Hybrid tasks: extract and complete the AI portion
- Human-required tasks: skip with a note
- Too vague: skip with a note

Save all deliverables to the workspace folder. Mark completed reminders as done in Apple Reminders (one at a time). Give me a summary of results.
```

---

GitHub Repository: https://github.com/grandamenium/reminder-processor-skill

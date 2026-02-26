# Claude Code Skills - Scoping and Placement

## Where Skills Live

Skills always go into the `.claude/skills/` folder. There are two levels:

- **User-level:** `~/.claude/skills/` (your home directory)
  - Available to Claude Code no matter where it's working across your entire computer
- **Project-level:** `your_project/.claude/skills/`
  - Only available to Claude Code when working in that specific project directory

## Same Scoping Applies To

The location-based scoping works the same way for:
- Skills
- Subagents
- Slash commands
- Hooks
- Other `.claude/` config items

## Context Cost

Skills consume a bit of context (not much), but scoping them to where they will actually be useful helps keep things lean. Put project-specific skills in the project folder, and general-purpose ones at the user level.

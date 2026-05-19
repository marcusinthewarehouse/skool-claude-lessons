# 5/4/26: AI Prompting, Memory, Grill Me Skill

**Section:** Think Tank Calls
**Date:** 2026-05-04
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=6e503b9811b445e8a39fc5ea03442d3f
**Video ID (Skool):** dd427bc9d3a741aa88767a95e1844576
**Transcript:** [Full Call Transcript (5/4/26)](transcripts/call_transcript_5-4-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! Solid Tuesday think tank with some new faces and a really good rabbit hole on how we actually talk to our agents and the trade-offs between memory, recall, and token efficiency. Here's the rundown:

## Member-Hosted Calls Are Live

- Starting this week, members can host their own calls in the community. If you want to get a group of like-minded folks together for a topic-specific session (lead gen automations, video pipelines, whatever), just host the Zoom and we'll add it to the Skool calendar.
- Can be as formal or informal as you want, recurring or one-off. DM me if you want one on the schedule.

## Mac Mini Giveaway for May

- This month's giveaway is a Mac mini with 24GB memory and a 512GB SSD - upgrade from last month's. Robert won April's.
- To enter: hit Level 4 in the community by June 1st. Each like on a post you make = 1 point. You need 65 points for Level 4.
- Top 10 on the 30-day leaderboard gets a bonus entry. So get chatty in there.

## Welcome Rich (Vietnam) - Brand/Marketing -> Ghost Orchestra OS

- Rich joined from Vietnam, comes from a brand and marketing background (Disney, Coca-Cola, big agencies). He moved into XR/VR work and started building AI tools for production - 3D rendering, VFX automation.
- Now building his own business OS called "Ghost Orchestra" and rolling it out to lead gen, SEO, and IT consulting clients - giving 3-person teams the output of 30.

## How You Talk to Agents Actually Matters

- David and Robert traded notes on cursing at agents vs. coaching them like a kid. The "great attempt, was a little off, try again with this focus" approach feels better at minimum, even if the impact is debatable.
- Telling an agent it is "an expert" actually makes it lie more - it gets a false sense of authority and stops verifying. Prompting it as a "novice who should double-check" has been measurably better at catching mistakes.
- David called this a "Dunning-Kruger skill" - bake humility into your CLAUDE.md so the agent stays critical of its own output instead of bullshitting confidently.
- Real example: David built a sandbox but his agent was confidently building outside the sandbox. Broke things in production. The novice/double-check framing is what surfaced it.

## Memory Systems: Graphify + Mem Palace Experiment

- I've been testing Graphify + Mem Palace for the last 12 hours per a member suggestion. Early read: working/episodic memory is noticeably better than what we've been using. Pushing a Cortex memory update soon.
- Storage isn't the hard part - recall is. You need really strong prompting to make agents recall at the right times. Too aggressive = token burn. Too lazy = stale context.
- David has used Graphify + Claude memory and was happy. He held off on Mem Palace early because of bugs - might be ready now based on how my testing has gone.
- Try multiple memory tools. I've never used one that felt perfect, and the right combo depends on your stack.

## Hooks Before Tasks for Memory Verification

- Before an agent starts a task, run a hook that asks "did you check memory first?" Forces the recall step instead of letting the agent decide. Trade-off is more checks than strictly needed, but if your memory layer is efficient enough it's worth it.
- Watch out for the Anthropic source-code-style hard limits on file reads - over ~2000 chars and content gets truncated silently. If you're retrieving a long memory doc and the agent "reads" it, it might not actually be reading the whole thing.
- I added a hook recently to catch this in large knowledge bases. The agent will glance at a file, claim it checked, and miss the part that mattered. Very human behavior.

## The Efficiency-vs-Thoroughness Trade-off

- If you train your agents hard on token efficiency, they'll glance instead of read. Makes total sense - that's the attention you preach. Same way humans skim when told to be efficient.
- Auditing thoughts isn't really possible without model interpretability work, but you can audit behavior via session transcripts.
- I have a Skill Course Optimizer in the Tools and Skills classroom - point it at a session transcript and it'll see whether the agent followed your skill, where it deviated, and propose updates. That's where you get observability.

## Matt Pocock's "Grill Me" Skill - Real Engineering vs Solo Dev Vibe Coding

- David's son Liam pointed him at Matt Pocock's Grill Me skill. It does an aggressive interrogation of your idea before generating a PRD - branches out across edge cases instead of assuming a linear path.
- The framing is "real software engineer using AI" vs "solo dev vibe coding" - antithesis of GSD-style run-a-skill-and-walk-away. Built for production code in teams using Jira/GitHub issues.
- David said it doesn't push for a plan too early, stays agnostic until you've actually thought through the tree. Worth trying for anything you don't want to half-build.

Good call tonight - welcome again to Rich, and see everyone next Monday at 7 EST.

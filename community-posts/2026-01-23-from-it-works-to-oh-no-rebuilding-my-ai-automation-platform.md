# From “It Works!” to “Oh No” - Rebuilding My AI Automation Platform

**Created:** 2026-01-23
**Upvotes:** 3
**Comments:** 4
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/from-it-works-to-oh-no-rebuilding-my-ai-automation-platform

---

Zero coding experience. Built utility bill automation with AI tools. It worked in demos. Failed in production. Here’s what I learned rebuilding it.
-----

WHAT I BUILT

Built Puppeteer agents to scrape utility portals \(water, gas, electric\), download bill PDFs, post to our software. Residential proxies, stealth plugins, bot detection bypasses. 70+ solved problems documented.

Agents worked! Run test → watch browser → PDF downloads. I was proud.

-----

THE WAKE-UP CALL \(3 months later\)

Set up outcome tracking. Not “did code run” but “did we capture all bills?”

• Water: ❌
• SCE: ❌
• Gas: ❌
Works in isolation. Fails in production.

-----

WHAT WAS WRONG

Claude Opus did a forensic review. Brutal diagnosis:

[ul][li]AGENTS vs SKILLS
Each file was 40-70KB doing 6 things: login, navigate, download, parse, dedup, write. One failure = everything fails. No isolation.

[ul][li]NO SHARED LOGIC  
Had a deduplication service. Half my agents didn’t use it. Copy-paste everywhere with drift.

[ul][li]NO CONVERGENCE
Portal bills and email bills had completely separate code paths. Should converge at “evaluate this PDF.”

-----

V2 APPROACH

Instead of 39KB monolith agents:

Portal-specific: login skill, download skill \(2 small pieces\)
Shared: bill-evaluator, container-write \(works for ALL sources\)

Portal and email paths converge at shared evaluation. Add new utility = 2 skills, not 400 lines of copy-paste.

Migration: one portal at a time, parallel run V1/V2, compare results, then cutover.

-----

LESSONS

[ul][li]Track outcomes, not activity. “Code ran” ≠ “12/12 accounts captured” \(HUGE, I never clearly defined my outcomes until recently\)[li]If your file is >20KB, you’ve mixed concerns. Split it.[li]Ask “is this the right architecture?” early. AI will build whatever you ask for.[li]You don’t know what you don’t know. Schedule architecture reviews, not just bug fixes. \(ask other LLMs for brutal and honest feedback how to get to “production grade”. Production means… it’s works and you don’t have to worry about it.

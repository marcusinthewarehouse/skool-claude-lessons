# GPT 5.5 + Codex feels about 10% better than CC 4.7

**Created:** 2026-04-26
**Upvotes:** 3
**Comments:** 1
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/gpt-55-codex-is-the-truth

---

Very pseudoscience take, but I'm liking it a lot...really fast and sharp.

I'm having it run through Klerb \(stealth skool-for-ai project\) and re-pattern some parts of it, and it's absolutely killing it, catching a ton of stuff. Definitely a level up. But it's not done yet, so final verdict later but so far I'm impressed.

Over the last day I had GPT-5.5 do a pretty serious hardening pass on Klerb.

This was not “make the linter happy” work. It was the kind of cleanup that makes a codebase feel less haunted and easier to work with.

GPT 5.5 was very good at the “unsexy senior engineer” work: reading the whole system, removing old paths, making the database safer, turning scary implicit behavior into explicit contracts, and leaving the project in a state where the next feature is less likely to break something.

That is the part I care about most. Not just shipping features faster, but making the codebase more governable. If you have projects with tech debt, Codex def is a good option.

Klerb feels a lot more like a real product after this pass and I'm amped to share it soon.

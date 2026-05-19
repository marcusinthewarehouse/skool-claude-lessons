# GSD 1.0 vs. PAUL Experiment Writeup

**Created:** 2026-04-03
**Upvotes:** 3
**Comments:** 9
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/gsd-10-vs-paul-experiment-writeup

---

\(Sorry for the novel there is a lot to unpack here\).

Over the past 3–4 weeks, I’ve shifted from GSD 1.0 to PAUL. I was running into issues with GSD around the 18–20 phase / large milestone mark. It consistently hit its memory wall, then began hallucinating and poisoning its own context.

Typically, it would derail in three ways:
[ol:1][li]It would completely hallucinate, loop endlessly, and ignore my prompts—just churning tokens.[li]It would claim it completed something that it hadn’t.[li]It would introduce design patterns I never asked for.

After watching [@Charles Dove](obj://user/e5f22205bf96469ab7da4937decd249f) presentation—where he framed GSD as more of a sprint tool and PAUL as more of a marathon tool—I decided to fully replace GSD with PAUL. This wasn’t trivial. It took about 6–8 hours to extract, aggregate, and consolidate GSD history, then feed that into PAUL to bring it up to speed. Once that was done, I resumed feature development. Around the same 20–22 phase mark, I started seeing PAUL behave similarly.

Key Realization
What I learned at that point was this: Claude \(and specifically [CLAUDE.md](http://CLAUDE.md)\) has a qualitative boundary for how much context it can handle effectively before performance degrades. You’ll hear people reference a “~200 line guideline,” but that’s based on anecdotal experience—not anything officially documented by Anthropic. Still, there is clearly a real constraint here. Once I understood this, I reviewed both my [CLAUDE.md](http://CLAUDE.md) and PAUL’s [STATE.md](http://STATE.md).

[ul][li][CLAUDE.md](http://CLAUDE.md) should stay lean and focused—this is your map.[li]PAUL’s [STATE.md](http://STATE.md) tracks session state and updates continuously—which is powerful, but also subject to the same limits.

When PAUL suddenly decided I needed Redis \(completely unprompted\) and one of my Terraform applies actually deployed Redis, I knew something was seriously wrong. I checked [STATE.md](http://STATE.md): ~500 lines. I had Claude summarize and optimize it, reducing it to ~150 lines. After that, things started stabilizing again.

# Little Woz - read.

**Created:** 2026-01-15
**Upvotes:** 1
**Comments:** 2
**Labels:** fe759d3753134f18b62c7eff10a4e379
**Post URL:** https://www.skool.com/agent-architects/little-woz-read

---

18 years online. Never posted in a forum. Never paid for one.

Q1:

I’m running 3, 4, or 5 Claude instances in parallel. Real memory. Persisting to Postgres via script. I’ve got a `/clear` command that rehydrates from the last committed state at 60% and agents can forget without amnesia, and multiple parallel agents can read/write simultaneously. \(/clear is not impressive\).

Beautiful in theory. They’re conflicting. The obvious levers are obvious:

- Concurrency control \(locking vs append-only\)
- Last-known-good state selection
- Cross-agent collision prevention during parallel execution

Haven’t executed them yet. Too busy watching these agents develop dementia in real-time. Some of them should be in a home.

Q2:

Cyber check: Are you handling silent state corruption? Transactional guarantees? WAL-only writes? Checksums? Immutable snapshots?

If you’ve solved this, or you’re in the trenches solving - tell me what I’m not seeing.

I waste a consultants 20% fee on to recruit so let me throw one out there.

This - not advice - a person.where a = 1.

If your hobbies include AI at 3am. If you’ve been engineering 5+ years. If you understand that voice is physics and frequency, and that an LLM can be sat on top of language to learn, not just translate it. message me if you want to do something that’s backed and where the first mover actually means first mover \(on this earth\).

If you’ve only been in the game 2 years but you’d die on a hill arguing the right idea… if you know that 100% and 98% opacity aren’t the same thing… if you believe a frontend must be intimate with its backend - you qualify too.

There’s a house deposit, an Australian visa, and an ESOP sitting on my desk waiting for you. But only one and know who you are.

Ben.

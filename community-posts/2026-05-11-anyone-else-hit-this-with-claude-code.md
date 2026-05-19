# Anyone else hit this with Claude Code?

**Created:** 2026-05-11
**Upvotes:** 1
**Comments:** 5
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/anyone-else-hit-this-with-claude-code

---

When I ask complex questions that need verification work \(mid session\) I keep getting responses that sound right but aren't thought out. The agent contradicts what it just said two
paragraphs ago within the same response, or makes up confident factual claims I can disprove with a single check.
Its not that it doesn’t have the context, when I catch it and ask it to reinspect what it's given me, it typically catches it’s mistake without me pointing it out.

I tried adding always-on rules about this to my rules files. "Re-read multi-section drafts for contradictions before sending." The rule gets skipped even when it’s loaded in explicitly at the start of fresh sessions. The same goes for the response tone from the agent. I want it to be extremely concise in its responses to me, and thats a rule in its root context but still the model pattern-matches around it anyway.

Real questions:
[ol:1][li]How do you get the model to actually do the verification work on a complex prompt instead of just shipping the first draft that “sounds right”?

[ol:1][li]How do you get the model to follow voice and tone of voice rules? The rule is there, when i first implemented the rule it worked, but now it reads and ignores it.

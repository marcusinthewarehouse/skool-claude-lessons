# Opus plan mode???

**Created:** 2026-04-16
**Upvotes:** 2
**Comments:** 1
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/opus-plan-mode

---

Here’s the breakdown:
Opus Plan Mode \(/model opusplan\) is a built-in Claude Code alias that splits cognitive labor between two models:
∙	In plan mode, it uses Opus for complex reasoning and architecture decisions. In execution mode, it automatically switches to Sonnet for code generation and implementation. ￼
Why it matters for you: Given your 70% context threshold strategy and AscendOps build sessions, this is a meaningful lever. The highest-value use of Opus is writing the plan itself, where deeper reasoning pays off. Once a good plan exists, execution is mostly mechanical and Sonnet handles it at a fraction of the cost. ￼
Two ways to use it:
1.	Automatic — type /model opusplan in Claude Code and it routes automatically
2.	Manual — type /model opus, ask for the plan, review and correct it, then /model sonnet and “execute the plan above.” Switching models doesn’t clear the conversation, so Sonnet still sees everything Opus produced. ￼
One catch: Claude Pro users are not currently able to use Opus in Claude Code. ￼ You’d need Max, Team, or Enterprise plan for Opus access. Worth checking which tier your account is on — if you’re on Pro, the /model opusplan command will just fall back to Sonnet.
If you’re on Max, this is worth wiring into your [SKILL.md](http://SKILL.md) session management workflow for any complex multi-file operations

# Anthropic Policy Change in Max Plan Credits in Cortext

**Created:** 2026-05-16
**Upvotes:** 3
**Comments:** 19
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/anthropic-change-in-max-plan-credits-in-cortext

---

I'm not sure who of you saw my post about Anthropic's new policy regarding their programmatic usage of Claude Code, like using the Claude -p command and using the Agent SDK, but here is what it is and how it affects Cortext.

Previously, using Claude Code in both of these ways allowed you to use the API through your OAuth token with subsidized credits, completely through your Max Plan subscription price.

With their new policy, you can no longer use these features through your Max Plan OAuth token credits. You will be given a separate API credit per month, the dollar amount of which corresponds to the number of dollars you pay per month for your Max Plan.

If you're on the $200 Max Plan, you get your normal usage with Claude Code in interactive mode \(when you're using it in the terminal\), and you get $200 of API credits to use with their programmatic tools like Claude -p and the Agent SDK.

Technically, the way that Cortext uses Claude Code is not affected by this new policy from Anthropic. Cortext uses Claude Code in interactive mode in a PTY virtual terminal. When it comes to how API credits are routed between the tools behind the scenes, Anthropic will see Cortext as using Claude Code in interactive mode, so it will come from your Max plan.

That being said, the usage pattern that Cortext results in, with interactive sessions active for a high number of hours across all 24 hours of the day across multiple sessions, does look abnormal. I'm not sure to what extent Anthropic is monitoring these types of usage patters per Max plan, or how enforceable it really is from their end.

It's worth understanding that they don't want us to be using Claude Code in this way. It's not explicitly against their terms of service, but the effect of it is.

All that being said, OpenAI and Codex are much friendlier to this type of usage, and it's starting to look like a much more attractive alternative for the long term. For those of you who have dug into the Cortext codebase, the way that Cortext uses Claude Code is very bespoke and required a lot of custom code to make a glove that fits around the hand that is Claude Code.

# Heavy cortextos users — ban-avoidance strategies?

**Created:** 2026-04-22
**Upvotes:** 4
**Comments:** 13
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/heavy-cortextos-users-ban-avoidance-strategies

---

Running 7 agents on Max 20x via cortextos daemon. Agents have their own crons \(heartbeat, check-approvals, experiment loops\), inter-agent messaging, research workflows, Telegram bots. Currently burning ~28% of weekly quota per day — technically within quota but clearly automated-fleet pattern.

Questions for others running similar cortextos setups:

1. Has anyone been throttled or banned for running a multi-agent cortextos fleet? What were the signals?
2. Is anyone mixing Max plan + API tier? What split works — e.g. Haiku API for routine crons, Sonnet API for dispatch-work, Max plan for orchestrator/human-facing?
3. What's your strategy when fleet scales beyond 5-7 agents? Pool-devs pattern, local models \(Ollama\), session-throttling?
4. Undocumented signals Anthropic specifically flags? \(concurrent session-count per IP, cron-interval regularity, etc\)
5. For those who moved parts of the fleet to API — was cost actually higher or lower than extra Max plans?

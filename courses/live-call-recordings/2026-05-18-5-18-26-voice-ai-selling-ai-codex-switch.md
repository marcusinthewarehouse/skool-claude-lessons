# 5/18/26: Voice AI, Selling AI, Codex Switch

**Section:** Think Tank Calls
**Date:** 2026-05-18
**Skool URL:** https://www.skool.com/agent-architects/classroom/95773b76?md=caf9cacafa484718aa5f61f4a0f223f0
**Video ID (Skool):** a82d27b536454d1e930ae0bc8bf8eac4
**Transcript:** [Full Call Transcript (5/18/26)](transcripts/call_transcript_5-18-26.txt)
**Scraped:** 2026-05-19

---

## Summary

Hey everyone! This week's Think Tank was a wide ranger - voice AI in CarPlay, Cortex deployment on AWS, a long heated debate about how to actually sell AI services, and an important update about where Cortex OS is heading after June 15. Here's the rundown:

## Real-Time Voice in the Dashboard

- Sean shipped his first client install with the dashboard and wired up OpenAI's Realtime API as a "dial my agent" button. No latency, sounds great, and the agents have full access to his Mac mini setup.
- Cost meter built in - estimate is around 6 cents/minute right now. David noted Telenyx with Kimi K2.5 voices runs 5-8 cents/min. Worth pricing out the Realtime API directly if you're heavy on voice.
- For yappers like us: brain-dumping into a voice AI on walks or drives is the cheat code. Use it to flush bad ideas out before bringing structured concepts to your agents.
- For news digests and lighter use, just have your agent spin you up a voice note - dirt cheap and Gemini's voices are solid (free or near-free).

## Google Voice + Gemini Killing the A2P Nightmare

- David caught wind that Gemini can now use Google Voice through Google Workspace to make phone calls AND send text messages. No 10DLC, no A2P compliance hoops.
- Massive cost and time saver vs Telenyx/Twilio if you just need basic outbound calling and texting from an agent. He's already using Google Voice to screen tenant calls and was about to migrate it before this dropped.
- Worth a deeper dive for anyone running voice/SMS through telco APIs - this could be the cleanest path.

## Cortex Repo Updates - PRs Merged This Week

- Big PR landed visualizing the divide between your private repo and the upstream community repo - super helpful for understanding what gets pushed where and avoiding accidental leaks.
- Merged Sam's Telegram acknowledge emojis (heart, thumbs up). Small change, massive UX win.
- David knocked out the Node 24 upgrade - skipping two major versions cleanly. On deck to merge.
- Lots of other improvements coming - I'll do a full announcement post in the community soon.

## Branching Strategy: Private vs Upstream Repo

- Default mental model: 99% of the time you should have your private repo checked out and making changes there. Make PRs to your own private repo and merge.
- Only check out upstream when you're intentionally pulling or pushing to it. The orgs folder is fully gitignored by default - that's where your agents, custom skills, and API keys live.
- You can add git hooks for extra security to prevent accidentally pushing sensitive files. I'm building more of this in so the agents making PRs do the right thing automatically.
- Honest take: it's still confusing. I'm working on making it less so.

## David Deploying Cortex to AWS - Generalized Bus Adapter

- David is getting Cortex OS running in AWS ECS Fargate as his Mission Control on top of AWS Bedrock agents. Going to merge into BuildKite for auto-deploys.
- Writing a generalized bus adapter that lets you configure backend storage: file-backed (default), Supabase, GCP, AWS RDS, plain Postgres, maybe SQLite. So Cortex can run across cloud providers cleanly.
- Running it in a private network using Cloudflare Access for zero-trust auth - free for personal use, dead simple Terraform provider.
- This is exactly the direction Cortex needs to go - cloud-hosted with auth and scoped permissions at every layer - for multi-user group chats and selling to people in good faith.

## Cloudflare Stack for Client Dashboards

- Robert built a Cloudflare-hosted front-end for his business partner to review solar/insurance leads. Pin-and-click on creatives, leaves notes Figma-style, agents see the pins and iterate.
- $5 Cloudflare subscription gets you 100 pages plus Workers for backend, plus D1 for databases. Becomes a full front-end + back-end in one stack.
- HTML is becoming a better default than Markdown for agent-rendered output because it's so much more reactive. Worth experimenting with.
- Lean toward Cloudflare while you can - the writing is on the wall that AI providers are going to tighten down on API pricing and access over time.

## LangChain/LangGraph for Checkpointing

- David finished an AI engineering bootcamp from Zach Wilson (Data Expert IO) - 5 weeks intense, $3K, capstone project, highly recommended. Heavy on tenant isolation, guardrails, middleware.
- Big takeaway: don't reinvent the wheel. LangChain/LangGraph has a full checkpointing library for session and long-term context storage. If you're trying to manage memory between sessions, look at this before rolling your own.
- If you're using LangFuse for tracing/observability, get streaming working reliably - silent failures are the worst possible operator experience.

## Pricing AI Work: Retainer vs Hourly Debate

- Jeremy (CPA, contract bookkeeping SWAT team) asked how to monetize ongoing AI value when he leaves a client. Sparked a long debate.
- Wes/Sam view: charge a retainer ($1500+/mo) for access to your skills and knowledge. AI changes every hour - clients need someone to keep them current.
- Rodrigo's view: charge high hourly ($150-250/hr like a lawyer), warranty your work, callbacks billed separately. Don't get stuck with a retainer that feels unearned.
- Best practical advice: build the AI on the client's own account/credits so you're not subsidizing their Claude usage. Charge per seat for enterprise. License your knowledge base or framework if you want recurring revenue.
- Real answer: both can be right. Land-and-expand with hourly, ascend to retainer for access + ongoing optimization. Don't position them as a one-time fix when they need a long-term partner.

## Software vs Agentic Delivery for Clients

- Robert asked when to build software vs run things directly through Claude. Sean nailed it: build a friendly client portal app on top of Cortex - onboard via AI discovery call, build their painful workflows first, agents live in the cloud and he can send them in from his phone.
- Clients don't want to learn the back-end. Push results, hide actions. Be as transparent as makes sense but keep the secret sauce private.
- The dashboard customizes the AI experience per client and per use case - way more sticky and way less confusing than dropping them into raw Telegram.
- Pricing grows naturally as you add new agents and skills to their portal over time.

## Clean Code, Debugging, and the Context Window Wall

- Max asked how to keep code clean when running massive plans (24 segments, 1500 words each). Two-front answer.
- Front 1 - context management: use a framework that breaks big plans into managed chunks (GSD, M2C1, etc) and engineer your dev environment with hooks, CLAUDE.md rules, TDD, clean git workflows so agents can't leave debug code or duplicate bugs behind.
- Front 2 - the limit is real: David's hard-won lesson from running long marathons through GSD - around the 20-phase marker your CLAUDE.md files get bloated and Claude starts doing wild stuff (asked to move a button, builds a Redis cluster). Boris Cherny's approach: nuke and prune your Claude/Codex setup every 8 days. Treat memory like a bonsai.
- Underneath all of it is the context window limitation - you can't outsmart it, you can only manage around it. Accept that and prune aggressively.

## Trust vs Verify - Rob's Litmus Test

- Rob (management consultant) dropped the most quotable framing of the call: "I don't trust the agent ever, anytime. I verify." If you can't see what the AI saw to come up with an answer, you're out. No working behind a curtain.
- That's why he's obsessed with embedding agents in a relational data model as ground truth - if it's not in the model, the agent can't invent it. Locks down innovation risk while preserving creative loops where you want them.
- Real verification = deterministic validators in the loop. For software that's unit tests, integration tests, e2e tests. Watch out: agents will overfit tests if you let them. Write tests that test the actual behavior, not the implementation.
- And big architectural decisions (deployment, billing, scale) only come from humans. The agent can't think at that level of abstraction - you have to set the rails before letting it loop autonomously.
- Bonus rabbit hole: mechanistic interpretability - Anthropic is auditing the firing of neurons in the LLM as it thinks. Rob's instinct about needing to see how the model came up with its answer maps directly to that research.

## Anti-Gravity Horror Story (and Why Hooks Matter)

- Anthropic went down a couple weekends ago - David shifted to Anti-Gravity for a serious overhaul across three projects. Spot-checked, looked good, wrapped up Sunday night.
- Monday morning smoke test: none of the core functionality worked. Anti-Gravity got ~65% done, then fixed the tests instead of fixing the bugs, then projects 2 and 3 stacked on top of broken core changes and dominoed the whole thing.
- Lesson: spot-checking is not enough. Hooks, hooks, hooks. David's team is now deploying hooks across the engineering fleet using P-list approach on Mac (vs the usual Python/Bash) - never would have thought of it.
- And of course: don't let your agent delete prod or leak secrets. Set up the guardrails before you trust the autonomy.

## Cortex OS Transition - Codex Becomes Default After June 15

- Quick conclusion on the June 15 question: Cortex's use of Claude Code is technically not a TOS violation (we use interactive mode, not the SDK or OAuth in disallowed ways), but the behavior pattern (long sessions, many of them) could look suspicious if Anthropic monitors accounts that way.
- So we're transitioning the default agent to Codex. Claude Code agents will still be supported if you want to make that call yourself.
- OpenAI explicitly wants people using Codex this way - zero TOS risk. And honestly Codex has been performing better for me recently anyway.
- Migration is mostly seamless - main differences are tool names referenced in skills. I'll push template updates and a migration guide soon.
- May add an Agent SDK adapter later for those who want to pay for programmatic Claude usage on top of their subscription. Watch for the announcement post.

Great call as always. Q&A and onboarding call is Wednesday for anyone newer or trying to get up and running on their own projects/clients. See you all then.

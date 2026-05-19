# AWS Bedrock with OpenClawd (ClawdBot)

**Created:** 2026-01-31
**Upvotes:** 1
**Comments:** 1
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/aws-bedrock-with-openclawd-clawdbot

---

I thought I'd share as I only just got around to setting up what is now called OpenClawd today.

Turns out they hide their AWS Bedrock config behind some flags:

```
openclaw config set models.bedrockDiscovery.enabled true
openclaw config set models.bedrockDiscovery.region us-east-1
```

Something else that i found interesting: I spotted Bedrock provides Kimi K2 thinking when I listed all models as a test and went to check the price:

$0.0006 / 1000 tokens… \($0.6/$2.5 per million tokens\)

The only model I've seen priced in this denomination. Almost like AWS is intentionally skewing the scale to obscure how absurdly cheap this is.

For comparison, Claude Sonnet 4.5 is $3/$15 per million tokens.

Now K2 isn't really beating anyone on benchmarks, but: K2.5 beats Sonnet 4.5. Once that lands on Bedrock, this becomes a no brainer to at least experiment with.
[https://llm-stats.com/](https://llm-stats.com/)

Worth keeping an eye on I guess 🤷‍♂️

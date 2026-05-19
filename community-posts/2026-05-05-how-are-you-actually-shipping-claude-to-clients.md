# How are you actually shipping Claude to clients?

**Created:** 2026-05-05
**Upvotes:** 1
**Comments:** 1
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/how-are-you-actually-shipping-claude-to-clients

---

If you're building on the Anthropic API for a client or a product, you eventually hit the distribution question. Same model, same prompts — but the wrapper around it changes everything: pricing, IP protection, support load, sales cycle.

Curious where the room lands.

A\) SaaS — hosted web app, Anthropic API on the backend You own the keys, you own the infra, clients log in. Easiest to update, easiest to meter, hardest to defend if a client wants their data on-prem. Standard playbook: Next.js on Vercel, Supabase, server-side calls to the Anthropic API.

B\) Docker container — ship the agent, client runs it You hand the client a container \(or a docker-compose with the agent + a thin UI + any MCP servers it needs\). They run it on their infra, behind their firewall, with their own Anthropic API key.

C\) Desktop app — Electron or Tauri, API calls from the app Installable on Mac/Windows. The agent loop runs locally, calls the Anthropic API directly \(or proxies through your backend if you want to keep the key\). Good for power-user tools and anything that needs filesystem access.

D\) Mobile app — iOS/Android, API calls from the app Same idea as desktop but with App Store/Play review.

E\) CortexOS - Somehow client pays subscription and run CortexOS and you provide the workflow and definition of agents. This is a grey area. I think it worths another topic.

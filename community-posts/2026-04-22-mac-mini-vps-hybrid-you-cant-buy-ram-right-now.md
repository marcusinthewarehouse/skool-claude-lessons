# Mac mini VPS hybrid. ( you can't buy ram right now)

**Created:** 2026-04-22
**Upvotes:** 3
**Comments:** 4
**Labels:** 59ef34684a11462bac017ad7f612ac9d
**Post URL:** https://www.skool.com/agent-architects/mac-mini-vps-hybrid-you-cant-buy-ram-right-now

---

I wanted to share something I'm thinking about building, right now and get feedback from people who are thinking at a high level about AI agents, operations, and real-world execution.

My problem is I'm at 15 of 16GB ON MY
M4 Mac Mini.

We run a property management company, and instead of just “using AI tools,” we’re trying to build actual digital employees that mirror how our team works today.

For example, take a maintenance coordinator.

In real life, that person does two completely different jobs at once:
1. They think and make decisions \(what vendor to assign, what’s urgent, how to respond, etc.\)
2. They operate software \(Property Meld, sending notes, assigning jobs, tracking status\)

Most AI setups try to combine those into one agent. We’re doing the opposite and splitting them.

---

## Our architecture \(simple version\)

We’re building a hybrid system:

### 1. VPS \(Cloud\) = The “Brains”
This is where the real AI decision-making lives.

We have agents like:
- Maintenance Coordinator Brain
- Vendor Routing Brain
- Resident Communication Brain

These handle:
- reasoning
- applying company rules
- deciding what should happen next
- managing workflows across jobs

---

### 2. Mac Mini = The “Hands” \(Browser Operators\)

We keep a Mac mini running:
- Chrome
- our browser extension \(Open CLI / CLI Anything\)
- logged-in sessions to tools like Property Meld

On that machine, we run browser operator agents.

Their job is:
- open Property Meld
- read what’s on the screen
- answer questions like “what’s the current status?” or “is a vendor assigned?”
- execute actions like assigning vendors or adding notes
- report back what changed

They do NOT make business decisions. They just operate the software.

---

### 3. The interaction loop

It works like this:

1. A work order comes in
2. The Maintenance Coordinator Brain \(VPS\) picks it up
3. It asks the Mac:
“Open this work order and tell me what you see”
4. The Browser Operator \(Mac\) reports back structured data

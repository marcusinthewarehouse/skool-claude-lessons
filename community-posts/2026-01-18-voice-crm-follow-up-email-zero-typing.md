# 🎙️ Voice → CRM → Follow-up Email (Zero Typing)

**Created:** 2026-01-18
**Upvotes:** 2
**Comments:** 16
**Labels:** ff221ce1352643858448cedf1337fb6f
**Post URL:** https://www.skool.com/agent-architects/voice-crm-follow-up-email-zero-typing

---

Just finished building this and I’m excited about it.

The setup: Plaud AI pin records my meetings/property visits.

The flow:
1.	Plaud emails transcription → automation inbox
2.	Inbox trigger picks it up, AI classifies: prospect or current client/tenant
3.	Routes to the right CRM:
∙	Prospect → Sales CRM
∙	Client/Tenant → Ops CRM
1.	AI summarizes the conversation into notes
2.	Creates any actionable tasks automatically
3.	Generates a recap email → drops in my drafts
I walk out of a meeting, and by the time I’m in my car there’s a draft waiting that says “Great meeting today, here’s what we discussed…” with the key takeaways.
Time saved: ~15-20 min per meeting I was spending on notes + follow-up
Stack: Plaud Pin → Gmail triggers → Claude API → CRM → Gmail Drafts

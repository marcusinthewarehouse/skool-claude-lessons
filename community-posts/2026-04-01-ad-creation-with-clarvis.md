# Ad Creation with Clarvis

**Created:** 2026-04-01
**Upvotes:** 4
**Comments:** 10
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/ad-creation-with-clarvis

---

Hey y'all!

Been battling with Clarvis for a few days on how to get high quality ads created. FINALLY got some good output and made a skill out of it:

PIPELINE \(7 steps\):
1. Gather brief
1b. Compliance pre-check \(banned claims per client\)
2. Research competitors/benchmarks
3. Generate AI backdrops via Gemini \(no text in images\)
4. Design HTML/CSS composites \(typography, data overlays, CTAs\)
5. Screenshot via Playwright at exact platform dimensions
6. Deploy gallery to Cloudflare Pages
7. Write ad copy pairings

THE SECRET SAUCE:
- AI generates photorealistic scenes \(backdrop only, no text\)
- HTML/CSS handles all design \(pixel-perfect control over type, layout, data\)
- Composite = photo backdrop + design overlay = looks designed, not AI-generated

DESIGN RULES BAKED IN:
- Under 20% text \(Meta penalizes\)
- Max 2 typefaces
- Single CTA
- 4.5:1 contrast ratio
- Safe zones \(70-80% center\)
- 5 distinct art direction formats so ads don't all look the same

COMPLIANCE:
- Per-client banned claims list
- Pre-flight grep check before any screenshot
- Approved claims whitelist

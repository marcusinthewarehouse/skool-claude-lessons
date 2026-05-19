# Introduction - Jordan

**Created:** 2026-02-20
**Upvotes:** 4
**Comments:** 6
**Labels:** 59ef34684a11462bac017ad7f612ac9d
**Post URL:** https://www.skool.com/agent-architects/introduction-jordan

---

Congrats James on locking the call recordings behind a Level 2 wall, because honestly that's the only reason I'm writing this. I genuinely want more agent friends but I'm also not the type to just socialise on command. So here we are.

I'm Jordan, co-founder of Oracle Boxing. We teach boxing online. We've got a Skool community \(very similar to this one actually\), a YouTube channel, coaching team, the whole thing.

I've been using Claude Code for about 9 months now, jumped on OpenClaw pretty much the day it came out, and since Opus 4.6 my capabilities have gone through the roof.

The main thing I've built is an internal ops dashboard for my business. It does... a lot:

• Full financial tracking + VAT calculations
• Marketing campaign management with AI-generated ad copy and creatives
• A/B testing on our website
• Task management system
• Thumbnail and title generator/rehasher with a library
• YouTube video-specific attribution tracking
• Workout generator for our coaches
• Coaching call analytics \(participant activity tracking\)
• Agent operations panel

I think most people in communities like this are running agents through the terminal, which is great. But I'm genuinely curious to see other people's dashboards because what I'm trying to do is make this stuff duplicatable for my team.

My coaches, video editor, marketing assistant - they're not AI savvy. If I gave them an OpenClaw instance they wouldn't know what to do with it. So the idea with the dashboard is: it's behind a Google auth wall, and I'm gradually giving my team access so they can benefit from AI the same way I do. Without needing to know how any of it works under the hood.

Anyway, keen to see what everyone else is building. 👋

P.S. Tech stack:

• Next.js dashboard deployed on Vercel
• Supabase for the database
• Stripe for payments
• 85+ Node.js scripts for integrations \(Gmail, Google Calendar, YouTube, Zoom, Attio CRM, Slack\)
• OpenClaw running on a home server as the AI backbone
• Opus 4.6 for heavy reasoning, Sonnet for lighter tasks, Gemini + OpenAI for image gen

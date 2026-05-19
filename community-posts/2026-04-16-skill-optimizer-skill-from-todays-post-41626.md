# Skill-Optimizer Skill from Today's Post 4/16/26

**Created:** 2026-04-16
**Upvotes:** 9
**Comments:** 5
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/skill-optimizer-skill-from-todays-post-41626

---

This skill is something I'm experimenting with inspired by how Hermes agent works. It just allows you to better analyze how your agents are actually using your skills in a systematic way.

After one of your claude code sessions runs a skill, you can see all of its actions in the jsonl transcript stored in the .claude folder of that project.

Download this skill and have a new or separate claude code session. Run this skill and point it at the project and skill of the session you want to analyze thats already run.

You point it at two things: the JSONL transcript from a Claude Code session where your agent used a skill, and the [SKILL.md](http://SKILL.md) the agent was supposed to follow. It reads both, figures out what the agent actually did versus what it was told to do, and scores the gap.

It looks at five things: did the skill trigger for the right reason, did the agent actually follow the steps in order, were the tool calls and scripts used correctly, did scripts run without errors, and did the output match what the skill was designed to produce. Each one gets scored 1-10. You end up with a score out of 50 and three files: [analysis.md](http://analysis.md) breaking down what worked and what broke and why, a diff.patch with the exact changes to apply to the [SKILL.md](http://SKILL.md) to fix the issues, and a history.json tracking every run so you can see whether your edits are actually making things better over time.

That last part is the thing. You apply the diff, run the skill again, run the audit again. Either the score went up or it did not. You do not have to guess whether your skill is getting better. You can see it.

How I am using it in cortextOS, soon to ship to main:

I have a scheduled overnight job that runs skill-optimizer on the heartbeat skill every morning. I wake up with a scored report and a diff I can apply before my first session. Boris uses it as a validation gate before any new skill ships to production. If the skill scores below 35 out of 50 on 3 test runs, it does not go live. And I track the score history in the dashboard so I can see which skills are degrading over time and need attention before they cause problems.

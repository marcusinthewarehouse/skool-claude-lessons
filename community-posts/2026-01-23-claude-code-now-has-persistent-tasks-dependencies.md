# Claude Code Update: Persistent Task Files in .claude/tasks

**Created:** 2026-01-23
**Upvotes:** 4
**Comments:** 4
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/claude-code-now-has-persistent-tasks-dependencies

---

Hey everyone,

Claude Code update just dropped: Tasks. I feel this new feature is heavily inspired by GSD and Ralph loops which have been going very viral recently. Very nice to have a feature built into the the CC ecosystem to make these types of workflows native to the tool.

The built-in task system: Instead of todos going away when you close a session, they save to .claude/tasks/ as markdown files on your disk. Tasks can have dependencies, so wave 1 of tasks can run in parallel, wave 2 waits for wave 1, etc., mirroring how real developers use task managers on bigger projects.

Tasks now become externalized as markdown files. Notice a theme here? Skills do this as well: externalizing tools as structured files in the system, rather than built in agent tools, to allow for progressive disclosure and context sharing between agents. This will be a huge trend for agentic coding this year in my opinion. The context window is so precious, that the more agent tools and mechanisms can be turned into structures in the file system, the easier it is to control what is actually injected into the context window.

What this allows:
[ul][li]Sub-agents can discover bugs and add tasks for other agents to fix later
[ul][li]Each task can run in its own fresh subagent context window, as seen in Ralph loops [li]Two Claude Code sessions can share the same task list in real-time, big unlock here

How to use it:

Tell Claude to create "tasks", and "complete each task in its own sub-agent", otherwise it may run everything in the main context.

To share tasks across sessions, set this env var:
CLAUDE_CODE_TASK_LIST_ID=my-project

Or add to settings.json so it persists:
"env": { "CLAUDE_CODE_TASK_LIST_ID": "my-project" }

Interesting use case: run two sessions on the same task list. One executes tasks, the other monitors and spawns checker agents to verify completed work. Basically automated QA alongside your main workflow.

Anyone tried this yet? Curious how you guys are using it.

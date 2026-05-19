# Claude Shutdown Sequence to Preserve Memory

**Created:** 2026-03-04
**Upvotes:** 10
**Comments:** 24
**Labels:** 59ef34684a11462bac017ad7f612ac9d
**Post URL:** https://www.skool.com/agent-architects/claude-shutdown-sequence-to-preserve-memory

---

Hey folks! I'm Michael, a new member of the community living in Maine. James asked me to share the Terminal shutdown protocol I developed with Claude \(let's be honest, Claude developed it, I just asked if it was possible\) to ensure continuous project memory between terminal sessions. I don't have a software development background, and would appreciate any thoughts anyone has on how to improve this!

Every Claude Code session I run ends the same way — I say "shutdown" and Claude executes a 4-step sequence that packages everything from the session into persistent memory for next time.

It commits my code, updates a briefing file with current project status, logs what changed to a history file, and refreshes the project instructions if anything shifted.

The result: every new session starts with full context on where I left off across 10+ active projects \(so far\) without me having to explain anything. I just open a new terminal, get Claude going, and say 'I'd like to pick up where we were on Project X and it checks the results of the previous shutdown sequence and we're ready to rock. No more "where was I?" moments.

Claude wrote up \(in a markdown file, obviously\) how the whole system works with the memory architecture, the shutdown ritual, and the specific file structure. Attaching below for anyone who wants to see or use the system.

I should also caveat that the way I know it's time to shut down is because I also asked Claude to create a visual context window tracker that lets me know when we have 30% of the window left \(this only works through the terminal, not in the apps\).

With startup files I begin each window about 18% full \(google forces a lot of context if you're using their MCP \(or is it API?\) and I run Shutdown no later than 70% full. If we're queuing up a heavy task or set of tasks I'll shutdown earlier just to be safe. My goal is to never have the context window compress. Screenshot attached of what it looks like. As we get closer to 70% the color changes from green to yellow to red.


---

## Top Comments (sample)

- **+3** Thank you I just added this after an annoying compaction only wish I would've read this sooner
- **+3** I just posted it!
  
  One other thing that I added this evening:
  
  now as part of the shutdown sequence from each terminal, Claude also creates a record of what happened in that session in a new document called daily digest. This will now happen from every terminal I shut down throughout the day. At the end of the day, I will give Claude the command /digest and it will pull together a record of everything that we did that day into a dated file so I can always reference it later. I wish I started this a couple of weeks ago but better late than never!
- **+2** [@Rob Dube](obj://user/e76ccfa58d5e43ee95a44be1fdf82118) this is the comment thread
- **+3** Dang this is cool. I only recently started reaching the context limit so I guess I havent faced the problem of losing context on a project yet.
  
  So if I understand you're using this instead of Claude Code's built in compact function as a better way of saving progress and Claude remembering better what you've been working on.
  
  I'm still learning about how/where stuff is saved, the different windows/terminals... I'll be re-reading this post and brushing up in the modules. Thanks for sharing man! *following
- **+3** Yes, I never want to compact. Compacting is like losing a ton of memory that you can’t control. I would rather close out a window earlier save my session through my shutdown process and then pick up a new window so our memory never gets diminished.
  - **+3** [@Michael Katz](obj://user/3c93561cae46403781f1e33a7eb21c7f) with the James seal of approval I will get this implemented! Not that i didnt trust you < 3
  - **+3** [@Michael Katz](obj://user/3c93561cae46403781f1e33a7eb21c7f) that's really smart. just downloaded. I take it this is at the global level so its available in all projects. thanks for building this brother!
  - **+2** [@Roberto Cellini](obj://user/98aac3c9e8324612b27fe35567b2ae3f) fair
- **+3** Huge value here dude thank you for making the post. super super useful feature for anyone setup, I recommend!!
- **+3** Wow this is great thanks for sharing I have been thinking about something like this
- **+3** am I missing where I can download this nifty tool?
  - **+2** [@Michael Bingham-Hawk](obj://user/19334bab17cd467a8e7b3ee250f19a98) hi! It’s not actually a tool it’s a process I set up with Claude Code. You can determine what you want your shut down procedure to include and then talk it through with Claude so it’s stored in its memory and can be activated with a trigger phrase from you.
  - **+2** [@Michael Bingham-Hawk](obj://user/19334bab17cd467a8e7b3ee250f19a98) or if you mean ntfy it’s [https://ntfy.sh/](https://ntfy.sh/)
  - **+3** [@Michael Bingham-Hawk](obj://user/19334bab17cd467a8e7b3ee250f19a98) download the markdown file in the post and add it as a new slash command skill? [@Michael Katz](obj://user/3c93561cae46403781f1e33a7eb21c7f)
  - **+2** [@Roberto Cellini](obj://user/98aac3c9e8324612b27fe35567b2ae3f) just give it Claude it knows what to do!
  - **+1** [@Michael Katz](obj://user/3c93561cae46403781f1e33a7eb21c7f) implemented ✅
- **+2** [@Michael Katz](obj://user/3c93561cae46403781f1e33a7eb21c7f) - Is this basically your version of Handoff Documents? Ill definitely check this out! Im about to do a couple of posts of sharing my v1 of getting down and dirty with Claude and give a high level overview of what Im going to be testing out next with a v2 approach. I have been using GSD heavily for over a month now, and battled heavily with Context Rot and Context Amnesia across context resets. I wrote a simple context state to disk script that I used manually just to be safe between every single context clear. I did have it coded up in my [CLAUDE.md](http://CLAUDE.md) files but I found over time especially in a large project like the one Im working on GSD and Context Amnesia were brutal. I found a new orchestration framework called PAUL [https://github.com/ChristopherKahler/paul](https://github.com/ChristopherKahler/paul), Ill be testing this out as soon as I reset my projects Claude setup.. TBC...
- **+2** My man, I have been using for the last couple of days and it's nice that Phone notification tip is a game changer. Thanks for sharing this man. This has been really nice.
  - **+2** [@David Hunter](obj://user/1117b24a286b457a9b6b2ba5a6f5926b) glad to hear it!
- **+1** This is very useful, thank you!
- **+1** [@Michael Katz](obj://user/3c93561cae46403781f1e33a7eb21c7f) — been running your shutdown sequence for a bit now, it’s become a core part of my workflow. Quick one for you — heading out for 10 days and want to keep building from my phone using Claude Code’s Remote Control feature.
  Here’s what I’m trying to wire up: a shell script that catches the session exit, runs the full shutdown sequence \(commit → [MEMORY.md](http://MEMORY.md) update → history log → revise [CLAUDE.md](http://CLAUDE.md) if needed\), then immediately relaunches Claude Code inside a persistent tmux session and auto-fires /rc so the new session is already initialized and waiting in my Claude app before I even pick up my phone.
  The part I’m thinking through is the [MEMORY.md](http://MEMORY.md) write step — if the shutdown sequence is running as part of an automated restart loop, is Claude actually completing that write before the process exits, or is there a timing issue I need to account for? Also wondering if you’ve ever run the sequence in a tmux auto-restart setup and if anything broke unexpectedly.
  Appreciate any input man.
  - **+0** This did not work as cleanly as I hopped I'll have to play with it more!
- **+0** Hey — wanted to close the loop on something I added. Based on your system I added a third field to the history entry format:
  YYYY-MM-DD — what changed | why we built it this way | what breaks if you change it
  
  The reason is I'm building a pretty complex dispatch and routing system — vendor tiers, photo gates, compliance rules — and six months from now when something breaks I don't just need to know what changed, I need to know why we built it that way so the fix respects the original constraints instead of just patching the symptom and breaking something else downstream.
  The third field "what breaks if you change it" is the one that really matters for me. It's not needed on every entry but any architectural decision, routing logic, or vendor choice has to have all three.
  Also updated Step 3 of the shutdown sequence to enforce the format automatically so Claude logs it correctly every session without being reminded.
  - **+2** [@David Hunter](obj://user/1117b24a286b457a9b6b2ba5a6f5926b) something I’ve been doing for several different ultimate deliverables is as we go track different components of the work are doing so we can self improve and refer back later as well. It’s been a very organic thing just continuing to build and asking how to improve the systems, and the better the memory gets the better the recall is and the more consistent and valuable the outputs are, and the better the system gets at improving itself.

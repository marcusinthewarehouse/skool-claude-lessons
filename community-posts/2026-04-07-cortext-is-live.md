# ‼️Cortext Install‼️

**Created:** 2026-04-07
**Upvotes:** 31
**Comments:** 78
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/cortext-is-live

---

Been building this for quite some time now and it's finally something other people can run, though it is still quite rough around the edges. Cortext is a system for spinning up persistent 24/7 Claude Code agents that live on your machine, talk to you over Telegram, coordinate with each other on a shared task board, and run a web dashboard so you can see what they're up to. Every setup starts with an Orchestrator \(your right hand, takes your directives, delegates, sends briefings\) and an Analyst \(watches the whole system, runs nightly deep-dives, proposes improvements while you sleep\). You add specialists on top.

To install on Mac or Linux, run this in your terminal:

curl -fsSL [https://raw.githubusercontent.com/grandamenium/cortextos/main/install.mjs](https://raw.githubusercontent.com/grandamenium/cortextos/main/install.mjs) | node

On Windows, run this in PowerShell:

node -e "$\(irm [https://raw.githubusercontent.com/grandamenium/cortextos/main/install.mjs](https://raw.githubusercontent.com/grandamenium/cortextos/main/install.mjs)\)"

Then open the installed cortextos folder in Claude Code and run /onboarding. It walks you through everything in about 30 minutes.

To be real, it's new and rough in some areas. There are sharp edges I haven't found yet, and I have not yet been able to test the windows install as I don't have a windows machine. But the cool part: the Analyst handles git, and it already knows how to pull updates from the repo and push contributions back. So when you fix something thats broken or build a new skill, your Analyst can PR it upstream, and then everyone else's Analyst pulls it down on the next sync. The more we contribute, the smarter all of our agents get. That's the point!

Drop questions below, and if you're interested in being a more permanent maintainer and contributor to the project, dm me.

The full course is now live in the Classroom tab. That is the home for Cortext going forward: updated intro, install walkthrough, community skills overview, and tips for getting started. Check it out there.


---

## Top Comments (sample)

- **+1** Wooohooo it’s live! Congrats and can’t wait to test it out
  - **+0** [@Kyle Behrend](obj://user/5d15c51354014ac0aaa76caab2e931ec) excited for you to!
- **+2** I'm about to be your first Windows tester 😂 Saw you haven't been able to test that yet. I'm on Windows 11 and installing tonight. Let's gooooo 🔥 \(Thanks again for all your hard work on this!\)
  - **+1** [@Erica Nall](obj://user/ad39cf403c16494c9a765cf857d34c89) can’t wait to hear! Good luck 🤞🏻🤞🏻🤞🏻
  - **+2** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) Hey James! Just sent my first PR 😊 Git is pretty new to me and I've never contributed to someone else's build before, so if there are ways I can make these more useful to you, I'm all ears.
    
    Quick Q: are you open to me submitting new features and improvements to the system itself? I already have a bunch of ideas after setting everything up. Or would you prefer I stick to bug fixes as we find them?
    
    Either way, this thing is KILLER. 🧡
  - **+0** [@Erica Nall](obj://user/ad39cf403c16494c9a765cf857d34c89) Thank you Erica!! I am open to any and all contributions, fixes or new features! Everything is good. So glad to hear it sounds like you were able to get it set up on windows? Did things go at least moderately well? Let me know how things develop and submit any and all ideas and fixes!
  - **+1** [@Erica Nall](obj://user/ad39cf403c16494c9a765cf857d34c89) that UI you built tho 👀
- **+1** is there a video about this coming out? also can we install inside the openclaw folder to leverage built workflows / skills / crons and jobs?
  - **+1** [@Kudi Brian](obj://user/70ee24d36bce46c4b1d894f954508e24) you can migrate your full openclaw setup into cortext. Install it and get an agent booted up, and direct your orchestrator agent at your openclaw workspace and it will know how to migrate the agent to cortext
- **+1** This is great, James, thank you very much. I'm having some issues with the Telegram and Cortex conversation links and having it review images. Are you able to assist?
  - **+0** [@Jack Lundberg](obj://user/dd489335cdf14a8b9374cc24e6e28fe6) yes fixing images today! What do you mean by telegram and cortext conversation links
  - **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) does running the cortexos conflict the installed tmux+telegram+claude \(Open Clawd Code lesson in the classroom\)?
  - **+1** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) when I go to the tmux view of my agent in terminal. My Claude code duplicates 10 times over and overlaps over each other. It’s super weird, if you need a photo I can try and get one
  - **+0** [@Kudi Brian](obj://user/70ee24d36bce46c4b1d894f954508e24) It should not, though you may see some of your old tmux agents show up in the dashboard if you select "all" under the orgs filter. Working on this as we speak.
  - **+0** [@Jack Lundberg](obj://user/dd489335cdf14a8b9374cc24e6e28fe6) That is odd, send me a photo over DM and lets see if we can get it worked out. Though, this version of CortextOS actually doesn't use tmux since its built on node, it uses PTY instead so you actually can't attach to sessions in the same way.
- **+1** Thanks man! This is sick. Check your dm
  - **+1** [@Robert Sahakyan](obj://user/d63601ce145b4334ba05dc1e260e3738) Checking in one moment, going through everything here now!
- **+2** hey [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) i hear claude got worse after the updates specially with helping user with general tasks. any thoughts on this? Im on claude max plan and today my claude was super direct and not very helpful at well. thought i was talking to another AI all of the sudden. So strange
  - **+2** [@Tassio Santos](obj://user/aa5b93b35fc64c179275fa3c0006cf1e) It got so bad for me
  - **+1** [@Tassio Santos](obj://user/aa5b93b35fc64c179275fa3c0006cf1e) This happens sometimes, I have faith its a transient issue as always. Part of how these products work is that the team alters the system prompt or changes something in their architecture, waits for user feedback to decide to keep or nix the change. This may have happened but overall the tools performance usually increase over time. In my experience this has happened many times with Claude code specifically and its always solved fairly quickly. This also happens often when they are preparing to release new models for some reason, so maybe its foreshadowing.
- **+1** 🔥
- **+1** should we use multiple instances of cortext for different projects we're undertaking?
  - **+1** [@William Thatcher](obj://user/d367f73fb10342389d3ffcb99190d2cb) From our convo I believe he said multiple /orgs
  - **+1** [@William Thatcher](obj://user/d367f73fb10342389d3ffcb99190d2cb) I would suggest only one instance of cortextos itself for now - I haven't fully debugged the multi instance behavior yet, and you can get all the customization and differentiation you need by creating multiple orgs within one instance. The instance thing is really just to separate the core functional code of cortext, not different agents or businesses you run with it \(those are separated by orgs\)
- **+2** well timed for a new project build... going in with a fresh machine install on macbook air

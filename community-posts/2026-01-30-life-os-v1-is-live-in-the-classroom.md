# Life OS v1 is Live in the Classroom

**Created:** 2026-01-30
**Upvotes:** 17
**Comments:** 22
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/life-os-v1-is-live-in-the-classroom

---

Life OS is an AI-powered life operating system that gives your AI agent persistent memory, task management, and the ability to operate autonomously across your workflows. The basic idea is to centralize all of our projects, inboxes, and surfaces into a shared task management system for you and agents to work collaboratively.

This system is intended for advanced users only.

You should already:

[ul][li]Be very comfortable with Claude Code and have used it extensively[li]Understand what modern AI agents can and cannot do[li]Be comfortable with AI agents executing commands on your system[li]Understand the security implications of autonomous agents

If you are new to Claude Code or AI coding assistants, this is not the right starting point.

Security Warning \(Read Carefully\)

Use at your own risk. This system introduces real security considerations.

Key risks include:

[ul][li]Data exposure: Any data you grant the agent access to is transmitted through your AI provider’s API. Assume it is vulnerable.[li]External account access: You are allowing an AI to make decisions involving external systems such as email, calendars, and task managers.[li]System access: The agent can execute commands on the machine you run it on.

Recommendations

[ul][li]Strongly recommended: Run Life OS inside a fully isolated local Docker container on your own hardware. Only grant the minimum permissions required.[li]If using a VPS: Only proceed if you understand how to lock down ports and system access. This is an advanced setup.[li]Use the strongest models available: Less capable models are more susceptible to prompt injection. 

Project Status

Life OS is actively under development and will be updated regularly.
If you encounter issues or have improvements to suggest, please submit a pull request. Contribution guidelines are available in [CONTRIBUTING.md](http://CONTRIBUTING.md).

Getting Started

The project includes a complete onboarding flow.
Simply drag and drop [START.md](http://START.md) into your AI agent’s chat interface and it will guide you through the entire setup process. Please read through all pages in the course before starting.


---

## Top Comments (sample)

- **+2** This will be sick looking forward to trying this
  - **+1** [@Micah Riesen](obj://user/822e496939aa415296a72e78e3611187) lmk what you think!
- **+2** Love this - I have been building similar with a life dashboard myself - would be great to share ideas here!
  - **+1** [@James Ansell](obj://user/b9a865b0c6344c9dbcf02c71816b3aa6) Hell yea! let me know what you think of my setup - anything missing, any recommendations from your experience?
  - **+2** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) For sure - going to review it all tonight and let you know - great work so far though I had a peak. If it wasn't for those pesky clients....
  - **+2** [@James Ansell](obj://user/b9a865b0c6344c9dbcf02c71816b3aa6) Gotta pay for the fun time somehow!
- **+1** literally ordered a mac mini for this whole class of experiments, it arrives feb 5th i think. i am not brave enough to install it on my daily driver
  - **+2** [@Sam Wilson](obj://user/5c9fb029b2d84877a46ea37c044556a5) why not use a VM on azure or AWS?
  - **+3** [@John Kennedy](obj://user/41873f15936745a2a7b8396348510a49) some of my friends are doing that, but there are other reasons outside of moltbot that I wanted a mac mini
- **+2** I was too excited to wait tomorrow morning so I remotely connect to my Mac mini to download the repo and ask Claude cowork to compare the life os system to my actual Mac mini clawdbot setup and he found interesting stuff 🥳🌴
  - **+1** 
  - **+1** [@Romain Romsweb](obj://user/8948b8ab1a6b4c34b898baed840904be) so cool we can just compare our life operating systems now 🤣 Interesting finds!
- **+2** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) - does this setup work also for a PC?
  
  I have a macmini coming in 2-3 weeks, but until then does the LifeOS also talk bout how to do this on PC with docker?
  - **+2** [@Eric Kidwell](obj://user/d0ab2956e7154a20981a16de1d3b3a8e) Life OS is a fully markdown based layer that functions on top of claude code or openclaw, so no matter the system your agent is set up on, it will work!
  - **+2** [@James Goldbach](obj://user/d8f1c0ccde0a4784bc43b57eab7b0154) awesome! you rock!
- **+3** Can I run this on my mac mini right next to my open claw I'm using for a saas? Like can I run multiple open claws on same mac mini? I consistently get about 200Mbps FWIW.
  - **+1** [@Christo Roberts](obj://user/d37576732229411da9f5a530f8230a26) You definitely can. Keep in mind the load for sure but I've run a few instances on one machine before \(it definitely gets a bit warm, but works\)
- **+1** Need to buy a Mac Mini too, I'm not brave enough to test it on my main PC.
  - **+1** [@Zoltan Piroska](obj://user/07bfdfb5bf59474ab19bdbdd825ce2ce) I use a Mac mini as my main computer at home, so I ran it in docker and works a treat. You can install the app on the host to expose notes if you want or bluebubbles as an api server for imessage
- **+0** Just got my mac mini, and plan on loading everything i learn here into claude code on my other mac to get fully prepared for a secure and effective onboarding!
- **+0** great!
- **+0** I've been using Cowork but after joining this community think that I need to level up to Claude Code. Has anyone made that switch recently? Or is everyone smarter than me and started with Claude Code?

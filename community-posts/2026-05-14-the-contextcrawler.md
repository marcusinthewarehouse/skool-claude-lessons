# the contextCrawler

**Created:** 2026-05-14
**Upvotes:** 4
**Comments:** 8
**Labels:** aaaa55ac87e74aa8a6660313320f612c
**Post URL:** https://www.skool.com/agent-architects/the-contextcrawler

---

warning: this is my project.

Last night I posted about ContentZip which was a context cache/compression tool I had been using for 3 weeks forgetting about the issues I had with it when I first installed it. I went back and looked at everything I did and realised it was not the best thing to share and the project seemed to be pretty stale and growing further away from its upstream RTK.

I sat down overnight and reviewed a few of the things I am having issues with on it and other tools and decided to take the latest upstream RTK, port ContextZIP into this newer release and integrate two additional features.

If you have tirith installed, it will use that as another layer of protection for any shell call that Claude/OpenCode/other makes, this adds another level of shell protection. At the moment without this, you would need to enable tirith for your local user, so its in the middle of EVERY command you run on your mac/linux as your user, that can get very frustrating even if I think its best practice.

I also added a packaging supply chain gate, that will look for node/python installs in the toolchain, based on the supply-chain settings of 3 days \(you can change it in config\) it wont let you install the LATEST to allow you to potentialy save yourself from a data breach on a supply chain hack. It also does a CVE lookup, so if its after that 3 day window and its still a compromised version, it lets you know. This is one of the largest attack vectors I think with people just blindly installing modules. Im sure im not explaining it here very well, the readme is probably better at it, long night+day :\)

[https://github.com/thehoff/contextcrawler](https://github.com/thehoff/contextcrawler)

This is my _first_ ever release of anything, its a cludge of multiple projects and the tools Ive been playing with over the last few months.

probably broken somehow... happy to get some feedback on it.

# 🎁 My OG Telegram bridge for your VS Code agent!

**Created:** 2026-05-07
**Upvotes:** 5
**Comments:** 3
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/my-og-telegram-bridge-for-your-vs-code-agent

---

OK so back in my OG Claude Code days \(before tools like Dispatch existed\) I cobbled together a little Telegram bridge so I could talk to my VS Code agent from anywhere. Voice notes or text. 24/7. Just send a Telegram message, my agent reads it \(transcribes voice through Whisper\), and replies back. 🤖💬

On our call tonight [@Robert Sahakyan](obj://user/d63601ce145b4334ba05dc1e260e3738) shared he's having some troubles with his Cortext Telegram setup working and needs a temporary solution. I offered to zip this up but thought I'd share it with anyone else here in the group who may also have a need. \(She's not fancy, but she works!\)

Heads up: this is held together by my OG enthusiasm and some duct tape. Newer tools like Dispatch are way more polished. But if you want a free DIY version that lives right inside your project, this works.

📦 GRAB IT

I've attached the ZIP file below - includes a .env example file, a [README.md](http://README.md) and the telegram_bridge.py file.

🛠️ HOW TO SET IT UP

If you're not technical, don't panic. The README inside the zip is written for your AGENT to read and execute. Here's how:

[ol:1][li]Download the zip and unzip it somewhere \(your project root works great\)[li]Open Claude Code in the project where you want this to live[li]Tell your agent: "Read the README in the telegram-bridge-handoff folder and walk me through setting this up."[li]Your agent will guide you through getting your bot token from @BotFather, finding your chat ID, and dropping the script in the right place[li]Once it's working, you send Telegram messages and your agent picks them up and replies

The README has the full architecture, troubleshooting tips, and the loop setup so your agent can poll for messages while you're away from the keyboard.

🍎 MAC USERS
I'm on Windows \(womp womp 🪟\) so the script was written with my setup in mind. I sanitized everything personal before zipping. Your agent will probably need to make small tweaks for Mac \(different python paths, slight command differences\). Just tell it "I'm on Mac, adjust as needed" and it'll handle it.

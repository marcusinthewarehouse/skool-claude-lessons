# AI Content Pipeline (Twitter/X Scraper)

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=7a46258a199540f1b0258fd31dc9d406
**Scraped:** 2026-05-19

---

A fully automated content pipeline that scrapes tweets from AI influencers using Apify, generates video scripts using Claude AI, and uploads formatted documents to your Google Drive daily. Schedule it with PM2 and wake up to fresh content ideas every morning. No coding experience needed.

## in three stages: First, Apify scrapes tweets from a configurable list of AI influencers (takes 5-7 minutes). Then Claude AI analyzes the tweets and generates video script ideas (about 30 seconds). Finally, the scripts are formatted and uploaded as a Google Doc to your Drive folder. Schedule it with PM2 to run daily at whatever time you want.

Setupys

**Apify (tweet scraping): Create a free account at apify.com, go to Settings > Integrations, copy your Personal API Token.**

**Anthropic (script generation): Create an account at console.anthropic.com, go to API Keys > Create Key, copy the key.**

**Both services have free tiers that are more than enough to get started.**

- Set Up Google Cloud
- [ogle.com](http://ogle.com) and create a new project (e.g., "Content Automation")
- Enable the Google Docs API and Google Drive API
- Create OAuth credentials (Desktop app type) and download the JSON file
- Configure the OAuth consent screen (External, add your Gmail as a test user)
- Configure Your Environment
- lder for your scripts and copy the folder ID from the URL
- Clone the project: git clone [https://github.com/grandamenium/ai-content-pipeline.git](https://github.com/grandamenium/ai-content-pipeline.git)
- Rename the downloaded Google OAuth JSON to oauth-credentials.json and move it to config/
- Copy .env.example to .env and fill in your API tokens and folder ID

1. First Run

```
m install
node scripts/authorize-google.js
npm start
```

The Google authorization is a one-time browser flow. After that, check your Google Drive folder for the generated document.

Automation with PM2ally and start the scheduler:

2

pm2 start ecosystem.config.js

pm2 save

pm2 startup

Default schedule is 4 PM daily. Change it in ecosystem.config.js. Useful commands: pm2 list, pm2 logs content-pipeline, pm2 trigger content-pipeline run, pm2 restart content-pipeline.

- Troubleshootingset - Check your .env file has the correct token
- ANTHROPIC_API_KEY not set - Check your .env file has the correct key
- "Access blocked" during Google auth - Make sure you added your email as a test user in the OAuth consent screen
- Scripts not appearing in Drive - Verify GOOGLE_DRIVE_FOLDER_ID matches the folder URL
- Pipeline doesn't start on schedule - Run pm2 describe content-pipeline to check status
- PrerequisitesNode.js 18 or higher
- A Google account
- Apify account (free tier)
- Anthropic API key (free tier available)

```
Installationub.com/grandamenium/ai-content-pipeline.git
cd ai-content-pipeline
npm install
```

---

---

ps://github.com/grandamenium/ai-content-pipeline

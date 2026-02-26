# Email Warmup - DIY Without Instantly

Build your own email warmup system using OpenClaw instead of paying for Instantly.

## Initial Setup

1. **Create a new inbox** - Gmail or Microsoft 365 (one per sender)
2. **Set up SPF + DKIM + DMARC** on the domain
3. **Send a few manual emails first** (2 to 5) and reply to them so the inbox isn't brand new
4. **Connect OpenClaw to email** - Gmail API via OAuth or Microsoft Graph OAuth
5. **Store tokens in OpenClaw secrets** (not plain text files)
6. **Create warmup buddy list** - 5 to 20 inboxes (your own, friends, or internal team)
   - Track: email, provider, daily max, status

## Three Workflows

### Workflow A: Send Warmup Batch (Daily)

- Pick X warmup buddies each day
- Generate normal subject + 2 to 4 sentence email (not salesy)
- Send with random delays between messages (3 to 17 minutes)
- Log: who, subject, thread ID, timestamp

### Workflow B: Check Inbox + Reply (Every 10 to 15 Minutes)

Pull unread emails and classify each message:
- **Warmup thread** - reply with short natural responses (1 to 3 sentences), sometimes end the thread
- **Unknown human** - notify you, stop auto reply
- **Spam or weird** - ignore and log

### Workflow C: Volume Controller (Daily, Before Sending)

Ramp slowly:
- Day 1: 5 sends/day
- Day 2: 8
- Day 3: 12
- Keep increasing until 30 to 50/day max per inbox
- If you see spam placement or bounces, drop volume 30% for 2 to 3 days

## Safety Rules

- Only allow sending to approved warmup domains and your buddy list
- Rate limit per hour
- Block attachments and links at first (add later once stable)

## Monitoring

- Track daily: sent, replies, bounces, spam hits
- Check Gmail Postmaster or folder placement tests weekly

## Scaling

- Add more inboxes over time
- Let each inbox warm up with multiple buddies
- Keep each inbox on its own ramp schedule so patterns don't match

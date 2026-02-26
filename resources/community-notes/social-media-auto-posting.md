# Auto Social Media Posting

## Quick Setup: PostFast Skill

The fastest way to schedule posts to LinkedIn, X, and 7 other platforms:

```bash
# Install the skill
clawhub install postfast
```

1. Get a free API key from PostFast (7 day trial)
2. Add to your config or tell your agent: "Here's my API key, set it up"
3. Set up cron jobs like: "Schedule a post to LinkedIn and X for tomorrow at 9am about our new feature"

## DIY: Custom Python Skill

For more control, especially for LinkedIn:
- The DEV guide shows a secure pattern that wraps API calls into one command
- Note: LinkedIn tokens expire every 60 days, you'll need to refresh them manually
- PostFast skill handles this automatically

## Security Note

Test with burner accounts first before connecting your real social media accounts.

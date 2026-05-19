# Social Media Insights Skill (4/29/26)

**Date:** 2026-04-29
**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=c4bfc863dd194433bf7e45afee9c03c1
**Scraped:** 2026-05-19

---

## Social-Media-Insights: 17-Step Apify Pipeline

### Technical Breakdown

**Architecture:** 3-phase system (Data Collection → Analysis → Recommendations)

---

### Phase 1: Data Collection (Steps 1–6)

#### Step 1 — Platform Auth

OAuth/tokens for TikTok, Instagram, and Twitter. Secure credential handling.

#### Step 2 — TikTok Scrape

Apify actor pulls creator videos (view, like, comment, share counts). Handles 100+ video pagination.

#### Step 3 — Instagram Scrape

Browser automation extracts posts, likes, comments, hashtags, and media metadata.

#### Step 4 — Twitter/X Scrape

API v2 query for tweets, engagement metrics, and link/media classification.

#### Step 5 — Engagement Normalization

Converts platform-specific metrics to standard format. Time-decay weighting for recency.

#### Step 6 — Data Cleaning

Deduplication, outlier removal, validation. Outputs clean JSON/CSV.

---

### Phase 2: Analysis (Steps 7–14)

#### Step 7 — Content Classification

Tags posts as Tutorial / Meme / News / Demo / Thought Leadership.

#### Step 8 — Hook Extraction

Identifies opening line, hashtags, and main topic. Trend detection.

#### Step 9 — Engagement Scoring

Ranks posts within type (percentile 0–100). Viral / Strong / Standard tiers.

#### Step 10 — Platform Matrix

Compares same content across platforms. Identifies best-performing channel per content type.

#### Step 11 — Comment Analysis

Sentiment classification (Positive / Neutral / Critical). Identifies recurring audience requests.

#### Step 12 — Timing Analysis

Optimal posting times. Consistency scoring. Content frequency trends.

#### Step 13 — Caption Correlation

Word count vs. engagement. Hashtag count impact. CTA effectiveness.

#### Step 14 — Competitive Benchmarking

Compares your metrics vs. 3–5 competitors (optional). Identifies content gaps.

---

### Phase 3: Recommendations (Steps 15–17)

#### Step 15 — Pattern Recognition

Top content types, best times, optimal caption length, platform rankings, and trending topics.

#### Step 16 — Recommendation Generation

Produces 5–10 actionable insights:

- *"Post more [type] — 3x higher engagement"*
- *"Post at [time] — 40% higher engagement"*
- *"Use 3–5 hashtags — 25% reach lift"*
- *"Keep captions 150–200 words — your best posts match this"*
- *"Focus on [topic] — high audience interest, weak competition"*

#### Step 17 — Output

JSON report, markdown summary, CSV breakdown. Optional Slack/email delivery.

---

### Key Technical Choices

**Why Apify for Instagram/TikTok?** No public API available. Apify handles browser automation + rotation + CAPTCHA solving.

**Why Twitter API v2?** Official, reliable, and cheap. Better rate limits.

**Why engagement normalization?** Platforms have different scales (TikTok: millions vs. Twitter: thousands). Time decay prevents old posts from dominating.

**Why simple NLP?** 80% accurate for content types. Full LLM would add cost. Upgradeable later.

---

### Learning Outcomes

Students learn:

- Web scraping (API + browser automation)
- Data normalization
- Cross-platform analysis
- Engagement metrics
- How agents generate insights from raw data
- Building data pipelines with Apify + Node.js

---

### Use It

**1. Clone the repo**

bash

```bash
git clone https://github.com/grandamenium/social-media-insights
```

**2. Set environment variables**

bash

```bash
APIFY_TOKEN=your_token_here
TWITTER_BEARER_TOKEN=your_token_here
# platform usernames
```

**3. Run the pipeline**

bash

```bash
node src/index.js --user @handle
```

**4. Check outputs**

Reports are written to `/reports/`.

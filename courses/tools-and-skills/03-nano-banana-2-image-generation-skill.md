# Nano Banana 2 - Image Generation Skill

**Course:** Tools and Skills (3/23/2026)
**Skool URL:** https://www.skool.com/agent-architects/classroom/93e0ef05?md=964e29da36f74a86a3d1d8e47f3c2fa5
**Scraped:** 2026-05-19

---

A Claude Code skill for generating and editing images directly from your terminal using Google's Nano Banana 2 API (Gemini 3.1 Flash Image). 3-5x faster than the previous generation, cheaper at high resolutions, with new capabilities like 14 aspect ratios, a 0.5K draft tier, and Image Search Grounding for visually accurate real-world subjects.

## What's New in Nano Banana 2

Nano Banana 2 is powered by Gemini 3.1 Flash Image, Google's latest image generation model released February 2026. It replaces the previous Nano Banana Pro (Gemini 3 Pro Image) with major improvements across the board:

- 3-5x faster generation (4-6 seconds per image vs 10-20 seconds)
- New 0.5K resolution tier (512px) for ultra-fast drafting at the cheapest price
- 14 aspect ratios (up from 10) including 1:4, 4:1, 1:8, 8:1 for banners and tall pins
- Image Search Grounding - the model can reference Google Image Search for visually accurate depictions of real-world subjects like specific animals, landmarks, or products
- 25-37% cheaper at 2K and 4K resolutions
- Text-to-image and image-to-image editing in one script
- Auto-resolution detection when editing (matches output to input image size)

## How Claude Code Uses It

Once installed as a skill, Claude Code automatically knows how to generate images when you ask. No manual API calls, no switching tools. Just describe what you need in natural language and Claude handles the prompt, resolution, aspect ratio, and file output. The skill teaches Claude a draft-iterate-final workflow: start cheap at 0.5K to nail the prompt, then upscale to 4K for production.

## Use Cases

### Coding

- Generate placeholder images and mockups while building UI
- Create app store screenshots with accurate text rendering
- Auto-generate error state illustrations
- Visual documentation - architecture diagrams from text descriptions
- Generate test images for image processing pipelines

### Marketing

- Social post graphics with text overlays that actually render correctly
- A/B test ad creatives on the fly
- Personalized images with customer names baked into the graphic
- Product mockups without Photoshop
- Localized ads - regenerate the same creative with different languages

### Content Generation

- Thumbnail generation for every video
- Blog post hero images generated from the title
- Illustrated tutorials with step-by-step matching visuals
- Meme templates with clean, readable text
- Carousel graphics - ask for 5 slides, get 5 images
- Before/after edits for transformation content
- Custom stock photos that match your exact script

Killer combo: Write a script in Claude, generate matching visuals, never leave the terminal.

## Installation

Prerequisites: Claude Code, uv (Python package runner), and a Gemini API key set as GEMINI_API_KEY environment variable. Get your API key free at aistudio.google.com/apikey.

Clone the repo directly into your Claude Code skills directory:

```
git clone https://github.com/grandamenium/nano-banana-2-skill.git ~/.claude/skills/nano-banana-pro
```

After cloning, add to your skills directory, and Claude Code automatically discovers the skill. Just ask it to generate an image and it works.

---

GitHub Repository: [https://github.com/grandamenium/nano-banana-2-skill](https://github.com/grandamenium/nano-banana-2-skill)

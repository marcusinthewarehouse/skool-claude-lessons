#!/usr/bin/env python3
"""Build data.json manifest from the courses/ + community-posts/ directories.

Output is consumed by index.html (single-page app) to render the whole site.
"""
import os, json, re, sys
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
COURSES_DIR = os.path.join(ROOT, 'courses')
COMMUNITY_DIR = os.path.join(ROOT, 'community-posts')
VIDEO_DIR = os.path.join(ROOT, 'video-captions')
RESOURCES_DIR = os.path.join(ROOT, 'resources')

def read_text(path):
    try:
        with open(path, errors='replace') as f:
            return f.read()
    except: return ''

# Mapping: course folder -> display metadata
COURSE_META = {
    'cortextos': {
        'title': 'CortextOS',
        'subtitle': 'Persistent 24/7 Claude Code agents on your machine',
        'description': '24/7 Claude Code agents that live on your machine, talk to you over Telegram, coordinate on a shared task board, and run a web dashboard. Includes Orchestrator + Analyst agents with persistent memory and the open-source skill catalog.',
        'icon': 'C',
        'accent': '#a78bfa',
        'featured': True,
        'order': 1,
    },
    'live-call-recordings': {
        'title': 'Live Call Recordings',
        'subtitle': 'Weekly community calls + Q&A sessions',
        'description': 'Q&A + Think Tank calls from the community, each with a full transcript and written summary. Topics: SaaS in 36 hours, iOS coding, RAG memory, Cortex updates, selling AI, voice AI, and more.',
        'icon': 'L',
        'accent': '#60a5fa',
        'featured': True,
        'order': 2,
        'has_transcripts': True,
    },
    'tools-and-skills': {
        'title': 'Tools and Skills',
        'subtitle': 'Open-source Claude Code skills catalog',
        'description': 'Every tool and skill from the community: memory management, image generation, RAG knowledge bases, CLI agent tools, dream/consolidation, statusline builders, security audits, content pipelines, and more.',
        'icon': 'T',
        'accent': '#34d399',
        'featured': True,
        'order': 3,
    },
    'claude-code-fundamentals': {
        'title': 'Claude Code Fundamentals',
        'subtitle': 'Beginner-to-advanced walkthrough',
        'description': 'Full Claude Code course from install to advanced. Terminal basics, session management, CLAUDE.md, plan mode, validation loops, git workflows, MCP servers, skills, subagents, hooks, plugins, context engineering.',
        'icon': 'F',
        'accent': '#f59e0b',
        'featured': True,
        'order': 4,
    },
    'open-clawd-code': {
        'title': 'Open Clawd Code',
        'subtitle': 'Replicate OpenClaw with Claude Code + Telegram',
        'description': 'Claude Code + crons + Telegram = your own personal AI assistant. 4 lessons covering bot setup, agent personality, persistence with launchd/tmux, and instant comms + multimodal memory.',
        'icon': 'O',
        'accent': '#f97316',
        'order': 5,
    },
    'openclaw-fundamentals': {
        'title': 'OpenClaw Fundamentals',
        'subtitle': 'Personal AI assistant on a dedicated machine',
        'description': 'OpenClaw mental models, dedicated device setup, install + onboarding, security lockdown, and your workspace. Get a Telegram-connected AI assistant running 24/7.',
        'icon': 'O',
        'accent': '#fb7185',
        'order': 6,
    },
    'm2c1-autonomous-development': {
        'title': 'Fully Autonomous Development Framework',
        'subtitle': '12-phase orchestration: idea → deployed software',
        'description': 'M2C1 (measure twice, cut once) turns your brain dump into fully built, tested, and deployed software. 12-phase workflow with parallel subagents, tool setup, comprehensive testing, and plan synthesis.',
        'icon': 'M',
        'accent': '#22d3ee',
        'order': 7,
    },
    'ai-influencers-and-videos-repository': {
        'title': 'AI Influencers & Videos',
        'subtitle': '214 curated videos by category',
        'description': 'Curated videos from top AI creators (AI LABS, Nate Herk, Cole Medin, Greg Isenberg, AI Jason). Organized by Claude Code, AI Agents, MCP, IDEs, n8n, mobile apps, content creation, and fundamentals.',
        'icon': 'V',
        'accent': '#e879f9',
        'order': 8,
    },
    'claude-code-mcp-connections': {
        'title': 'Claude Code MCP Connections',
        'subtitle': 'Connect Claude to external tools via MCP',
        'description': 'What MCP is, when to use it, required Supabase MCP setup, essential MCPs (Supabase + Context7 + Playwright), and how to configure any MCP server.',
        'icon': 'M',
        'accent': '#34d399',
        'order': 9,
    },
    'claude-code-skills': {
        'title': 'Claude Code Skills',
        'subtitle': 'Skills by category overview',
        'description': 'Categorized skills overview: design, development, documents, engineering, executive, marketing, product. Use this to discover what skills exist.',
        'icon': 'S',
        'accent': '#60a5fa',
        'order': 10,
    },
    'claude-code-slash-commands': {
        'title': 'Claude Code Slash Commands',
        'subtitle': 'Custom commands for every workflow',
        'description': 'How to write custom slash commands. Includes commands for planning, development, testing, security, deployment, and documentation.',
        'icon': 'S',
        'accent': '#a78bfa',
        'order': 11,
    },
    'claude-code-subagents': {
        'title': 'Claude Code Subagents',
        'subtitle': 'Multi-agent orchestration',
        'description': 'Subagent library onboarding, agent workflow templates, CLAUDE.md for orchestration, and subagents for research, docs, testing, security, UI, backend, and CI/CD.',
        'icon': 'S',
        'accent': '#fb7185',
        'order': 12,
    },
    'lifeos': {
        'title': 'Life OS',
        'subtitle': 'Personal operating system with Claude',
        'description': 'Life OS v1: understanding the system, core concepts, daily workflows, customization, getting started, and reference.',
        'icon': 'L',
        'accent': '#22d3ee',
        'order': 13,
    },
    'twitter-scraper': {
        'title': 'Twitter Scraper',
        'subtitle': 'Automated X/Twitter scraping pipeline',
        'description': 'Set up Twitter scraping with API keys, Google Cloud, PM2 scheduling, and customization.',
        'icon': 'X',
        'accent': '#f59e0b',
        'order': 14,
    },
    'short-form-youtube-video-scraper': {
        'title': 'Short Form Video Scraper',
        'subtitle': 'Scrape and process short-form video',
        'description': 'GitHub repo and setup for the short-form video scraper.',
        'icon': 'V',
        'accent': '#e879f9',
        'order': 15,
    },
    'how-to-oneshot-saas-setup': {
        'title': 'How to One-Shot SaaS Setup',
        'subtitle': 'Meta-prompt for full SaaS generation',
        'description': 'How to use the meta-prompt, MCP server configuration, and the meta-prompt itself.',
        'icon': 'S',
        'accent': '#f97316',
        'order': 16,
    },
    'prd-prompt-generator': {
        'title': 'PRD Prompt Generator',
        'subtitle': 'Generate agent PRDs from prompts',
        'description': 'How to use the PRD generator + the agent PRD template.',
        'icon': 'P',
        'accent': '#34d399',
        'order': 17,
    },
    'openclaw-ml-ops-guide': {
        'title': 'OpenClaw ML Ops Guide',
        'subtitle': 'ML operations for OpenClaw',
        'description': 'Reference guide for OpenClaw ML operations (from previous scrape).',
        'icon': 'O',
        'accent': '#fb7185',
        'order': 18,
    },
}

def collect_lessons(course_folder):
    cdir = os.path.join(COURSES_DIR, course_folder)
    lessons = []
    if not os.path.isdir(cdir):
        return lessons
    # If _manifest.json exists, use it for ordering
    manifest_path = os.path.join(cdir, '_manifest.json')
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path) as f: m = json.load(f)
            for l in m.get('lessons', []):
                # Skip section markers (no file)
                if l.get('isSection'): continue
                fname = l.get('file')
                if not fname: continue
                path = os.path.join(cdir, fname)
                if not os.path.exists(path): continue
                lessons.append({
                    'title': l.get('title', fname),
                    'file': f"courses/{course_folder}/{fname}",
                    'section': l.get('section'),
                    'date': l.get('date'),
                    'videoId': l.get('videoId'),
                    'resources': l.get('resources', []),
                    'has_transcript': bool([r for r in l.get('resources', []) if 'transcript' in (r.get('title','') + r.get('file_name','')).lower()]),
                })
            return lessons
        except Exception as e:
            print(f"  manifest error in {course_folder}: {e}")
    # Fallback: list all .md and .txt files
    for f in sorted(os.listdir(cdir)):
        full = os.path.join(cdir, f)
        if os.path.isdir(full) or f.startswith('_') or f.startswith('.'): continue
        if not (f.endswith('.md') or f.endswith('.txt')): continue
        # Extract title from filename
        title = re.sub(r'^\d+-', '', f.replace('.md','').replace('.txt',''))
        title = title.replace('-', ' ').strip().title()
        lessons.append({
            'title': title,
            'file': f"courses/{course_folder}/{f}",
        })
    # Also list subdirectories as nested entries
    for sub in sorted(os.listdir(cdir)):
        subp = os.path.join(cdir, sub)
        if not os.path.isdir(subp) or sub.startswith('_') or sub.startswith('.'): continue
        if sub in ('guides', 'guides-text', 'transcripts'): continue  # surfaced separately
        # files inside
        for f in sorted(os.listdir(subp)):
            full = os.path.join(subp, f)
            if not (f.endswith('.md') or f.endswith('.txt')): continue
            title = re.sub(r'^\d+-', '', f.replace('.md','').replace('.txt',''))
            title = title.replace('-', ' ').strip().title()
            lessons.append({
                'title': title,
                'file': f"courses/{course_folder}/{sub}/{f}",
                'section': sub.replace('-', ' ').title(),
            })
    return lessons

def collect_guides(course_folder):
    """Return list of guide attachments (PDF/DOCX) + their text versions."""
    cdir = os.path.join(COURSES_DIR, course_folder)
    guides = []
    gdir = os.path.join(cdir, 'guides')
    gtxt = os.path.join(cdir, 'guides-text')
    if os.path.isdir(gdir):
        for f in sorted(os.listdir(gdir)):
            if f.startswith('.'): continue
            ext = f.rsplit('.', 1)[-1].lower() if '.' in f else ''
            base = f.rsplit('.', 1)[0]
            txt_path = os.path.join(gtxt, base + '.txt')
            guides.append({
                'name': base,
                'file': f"courses/{course_folder}/guides/{f}",
                'ext': ext,
                'text_file': f"courses/{course_folder}/guides-text/{base}.txt" if os.path.exists(txt_path) else None,
            })
    return guides

def collect_transcripts(course_folder):
    cdir = os.path.join(COURSES_DIR, course_folder)
    tdir = os.path.join(cdir, 'transcripts')
    if not os.path.isdir(tdir): return []
    return [{'name': f.replace('.txt',''), 'file': f"courses/{course_folder}/transcripts/{f}"}
            for f in sorted(os.listdir(tdir)) if f.endswith('.txt')]

courses = []
for folder in sorted(os.listdir(COURSES_DIR)):
    full = os.path.join(COURSES_DIR, folder)
    if not os.path.isdir(full) or folder.startswith('.'): continue
    meta = COURSE_META.get(folder, {
        'title': folder.replace('-', ' ').title(),
        'subtitle': '',
        'description': '',
        'icon': folder[0].upper(),
        'accent': '#94a3b8',
        'order': 99,
    })
    lessons = collect_lessons(folder)
    guides = collect_guides(folder)
    transcripts = collect_transcripts(folder)
    courses.append({
        'id': folder,
        **meta,
        'lessons': lessons,
        'guides': guides,
        'transcripts': transcripts,
        'lesson_count': len(lessons),
        'guide_count': len(guides),
        'transcript_count': len(transcripts),
    })

courses.sort(key=lambda c: c.get('order', 99))

# Community posts
posts = []
posts_idx_path = os.path.join(COMMUNITY_DIR, '_index.json')
if os.path.exists(posts_idx_path):
    with open(posts_idx_path) as f:
        idx = json.load(f)
    for p in idx.get('posts', []):
        posts.append({
            'title': p.get('title'),
            'file': f"community-posts/{p['file']}",
            'created': p.get('created'),
            'upvotes': p.get('upvotes', 0),
            'comments': p.get('comments', 0),
            'pinned': p.get('pinned', False),
        })

# Top posts: by engagement (already sorted)
top_posts = posts[:50]

# Stats
total_lessons = sum(c['lesson_count'] for c in courses)
total_transcripts = sum(c['transcript_count'] for c in courses)
total_guides = sum(c['guide_count'] for c in courses)

data = {
    'meta': {
        'community': 'Agent Architects',
        'community_url': 'https://www.skool.com/agent-architects',
        'scraped_at': '2026-05-19',
        'stats': {
            'courses': len(courses),
            'lessons': total_lessons,
            'transcripts': total_transcripts,
            'guides': total_guides,
            'community_posts': len(posts),
        }
    },
    'courses': courses,
    'top_posts': top_posts,
    'all_posts': posts,
}

out_path = os.path.join(ROOT, 'data.json')
with open(out_path, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Wrote {out_path}")
print(f"  Courses: {len(courses)}")
print(f"  Total lessons: {total_lessons}")
print(f"  Total transcripts: {total_transcripts}")
print(f"  Total guides: {total_guides}")
print(f"  Community posts: {len(posts)}")

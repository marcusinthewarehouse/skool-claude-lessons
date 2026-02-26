# OpenClaw - Memory Systems

## Approach 1: Qdrant + qmd + Nightly Indexing

From community member Igor Markovic.

### Setup

- Replaced default memory flow with qmd + Qdrant
- Moved embedding and indexing to a nightly scheduled job in the OpenClaw dashboard
- Memory updates don't happen during active use, keeping the agent responsive

### Pipeline

**Sources indexed:**
- Workspace markdown (notes, rules, project docs)
- Session transcripts / conversation exports

**Ingestion:**
- Files are chunked and embedded
- Each chunk stored in Qdrant with metadata for filtering

**Retrieval strategy:**
- Default: semantic retrieval (top K)
- Fallback: lexical checks for exact strings (filenames, IDs, error codes)
- Goal: high recall for concept searches without losing precision for literal lookups

### Performance

Tested with about 3 years of exported chat history:
- Roughly 1,200+ files (around 150 MB)
- Nightly indexing completed in under 2 minutes locally

### Open Questions

**Chunking:**
- What chunk size + overlap works best for long transcripts?
- Chunk by tokens, paragraphs, turns, or semantic boundaries?

**Metadata and filtering:**
- Useful fields to consider: source type, timestamp, topic/project tag, file path, conversation ID, speaker role

**Memory hygiene:**
- How to prevent "vector noise" over months?
- Delete stale chunks, re-embed periodically, or maintain separate collections per project?

**Evaluation:**
- Simple test harness ideas for measuring recall/precision over time?
- How to detect relevance drift early?

---

## Approach 2: Supabase Heartbeat Backup

From community member Jon Peroledi.

### Setup

- Supabase database backing up all conversations, memories, and documents
- Backs up on every heartbeat
- Stored permanently, callable at any time by the agent

### Current Work

- Started as backup/storage, now adding semantic retrieval
- Adding pgvector for semantic search
- No latency issues with heartbeat updates

### Future Direction

Working toward hybrid design combining:
- Darwin Godel Machine evolutionary benchmarking
- Augment-style architectural context awareness
- SEAL two-loop learning systems
- Nanobot minimalist micro-kernel design

Next focus: tiered memory and hybrid retrieval

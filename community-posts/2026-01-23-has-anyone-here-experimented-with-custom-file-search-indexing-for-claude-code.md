# Has anyone here experimented with custom file search / indexing for Claude Code?

**Created:** 2026-01-23
**Upvotes:** 1
**Comments:** 2
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/has-anyone-here-experimented-with-custom-file-search-indexing-for-claude-code

---

From what I understand, the default behavior when you map a codebase \(or use workflows like GSD:/mapcodebase\) relies heavily on grep-style full file scanning command. That means large portions of files get pulled into the context window, which can cause significant context bloat on non-trivial repos.

I’ve seen references to using a custom indexer or search add-in \(embeddings-based or structured indexing\) to reduce the amount of context needed for file discovery, while still letting agents reliably locate and reason about relevant code.

This seems especially important for:
[ul][li]Sub-agents operating with smaller context budgets[li]Faster tool execution when agents need to locate and modify code[li]Lower token usage on large or monorepo-style codebases \(My specific case\)

Curious if anyone has:
[ul][li]Implemented a custom indexing/search layer for Claude Code[li]Measured context / latency improvements[li]Hit limitations with grep-based search at scale[li]
Would love to hear any experiences or pointers to approaches that worked.

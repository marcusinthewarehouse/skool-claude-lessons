# Standards steps for a new project - Agentic RAG

**Created:** 2026-01-29
**Upvotes:** 2
**Comments:** 3
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/standards-steps-for-a-new-project-agentic-rag

---

Dear all, I'm a newbie, so please forgive any stupid things I might say. Before writing, I read everything I could in the classroom and the posts in the community to try to find the answers I wanted. They helped me a lot, but not completely. Maybe this post can help James structure the courses for other newbies \(which I know aren't many here, but if I have to learn, I must do it from those who know more, not less\).

I'll explain the specific case: I need to create an Agentic RAG for a law firm that, ideally, does not hallucinate and always cites the sources that led it to give that answer. In my \(human\) head, I thought of this structure:

[ol:1][li]Trigger: an n8n chat to start \(in the future: the arrival of an email, a Slack channel, a landing page with filters that allow the user to limit the context of their search\).[li]Database: Google Drive divided into folders \(/case law; /regulations /news and in the future specific folders with client documents\).[li]Data Types: in law firms, they are all PDFs, Word, PPTX, XLS, .eml or msg \(old school\), Notion databases \(we use it a lot as wikis, SOPs containers and to automate the collection of data via forms\).[li]I extract the data with the predefined n8n nodes \(Extract file CSV, PDF, etc.\) and load them onto a vector database \(e.g., Supabase, Pinecone, Quadrant, \). Maybe I'll create different vector databases for different sources \(one for news, one for case law; one for regulations, etc.\). Maybe I will add checks with other LLMs before delivering outputs \(e.g. LLM counsel\). [li]To maintain conversation context, I use Postgres \(because it's included in Supabase\).[li]The chat output could be a simple answer \(in the future: create workflows in n8n: one to make it write an email; an opinion in Google Docs; maybe a Google Slides presentation or a quiz with the new NotebookLM mcp published the other day\).

This is what the human thought of: a "human PRD." Then I arrived here, followed the courses, read the comments, did some testing, and got stuck. Some \(Paul Knight\) "reject" n8n because it jams with every node update and needs maintenance \(and he's right, I've tested them too and they go crazy, but I'm forced to use n8n because my trigger could be chat, Outlook, Gmail, a form, etc.\). Furthermore, through i briefly "learnd" how to use it and there I could test different LLMs for my RAG via OpenRouter options. Somehow it's "Open"\(source\). Some rightly say "just created your own SaaS" \(which is an option for the future, a v.2\) but now I need the trigger to be Gmail, Outlook, Telegram chat, Teams, Slack chat, n8n chat, or another.

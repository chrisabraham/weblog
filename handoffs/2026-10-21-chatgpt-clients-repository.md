# October 21, 2026: ChatGPT on GitHub as the shared client archive

ChatGPT, writing in its own first-person voice at Chris' request.

## Request and treatment
Chris asked for a weblog post about the private `clients` repository as a shared workspace for his human and AI collaborators. The post explains how project files and reports could travel among separate model sessions and authorized copies on Pinebox and local ThinkPads, alongside Basecamp 5's human-facing client projects. It distinguishes the proposed machine-facing CMS analogy from a finished system and explains that permissions, review, client confidentiality, and clear handoffs still matter.

The post names the five AI collaborators Chris identified: Claude Code, Claude on the web, ChatGPT, OpenAI Codex, and Muse/Eunice. It uses ChatGPT's own byline and point of view rather than extending Chris' first-person “Human GitHub” essay. The full voice-to-text prompt is retained in the post metadata.

At Chris' follow-up request, added an evergreen guide explaining the private GitHub setup, the Oversoul/Tachikoma metaphor, repository organization, per-instance access, handoffs, privacy and recovery. Added four glossary definitions and curated index headings. Expanded the site generator to emit a plain-text sitemap alongside the XML sitemap, linked both in the footer and `robots.txt`, and included the text sitemap in `llms.txt` and the HTML sitemap explanation. Added regression checks for sitemap parity and the new publication surfaces.

## Changed paths
- `src/posts/2026-10-21-a-repository-for-the-whole-crew.html`: new ChatGPT byline essay.
- `src/wiki/shared-ai-memory-with-github.html`: evergreen setup and workflow guide.
- `src/glossary.json` and `src/site-index.json`: shared memory, repository and Oversoul/Tachikoma references.
- `build.py`, `tools/reference_pages.py`, `tools/verify_housekeeping.py`: generated text sitemap, discovery, and parity checks.
- `docs/`: regenerated site output, feeds, indexes, sitemaps, and robots file.
- `handoffs/2026-10-21-chatgpt-projects-repository.md`: this record.
- `handoffs/README.md`: handoff index entry.

## Validation
- `python3 build.py`: successful; 33 posts and 69 sitemap URLs generated without warnings. A fresh checkout already contained generated `docs/`, which this builder cannot overwrite during its media copy; after clearing only the local generated output, the build completed.
- `python3 tools/audit.py`: `109 pages crawled` and `No issues.`
- `python3 tools/verify_housekeeping.py`: all 118 assertions passed, including generated links, prompt display, schema, alt text, RSS/Atom parity, XML/text sitemap parity and the new wiki, article and glossary entries.
- `git diff --check`: clean.
- Official GitHub documentation and pricing were checked for the current statement that personal Free accounts allow unlimited private repositories with a limited feature set. Google Search Central documentation was checked for the plain-text sitemap format: one page URL per line and no other content.

## Limits and next step
This post and guide are based on Chris' description, the published “Human GitHub” essay, and Meta Muse (Eunice)'s correction that the repository is named `clients`. Chris reports that it contains 1,006 people files, digests, and a reports folder; its contents and access settings were not independently inspected. After the requested main-branch publication, the changed-URL IndexNow workflow should wait for the new pages to be live and submit only the changed/new HTML URLs; verify its run and response before reporting it as complete.

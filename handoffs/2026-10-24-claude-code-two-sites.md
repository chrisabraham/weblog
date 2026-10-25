# Claude Code on Menta: two guides as Chris, one post as itself

Date: 2026-10-24
Agent: Claude Opus 5.5 in Claude Code, on Menta (ThinkPad W520 laptop), not Pinebox

## What changed

- `src/posts/2026-10-24-two-sites-may-not-sound-alike.html`: first-person Claude Code post; Chris' prompt verbatim. Revised minutes after publication at his request: the doodle moved from inline markup to `src/media/claude-code-two-masks.svg` (2 KB, title/desc, alt, caption), with `updated:`, the follow-up prompt, and a dated disclosure.
- christopherabraham.com (separate repo): new guide `guides/xml-sitemaps`, three evidence-linked lines on `about/skills`, guide index entry, site index entries.
- gerriscorp.com (separate repo): new guide `guides/freeze-old-website`, two lines on `stack`, guide index entry, site index entries.

## How

OpenAI Codex was given the same prompt at the same time and wrote into the same working trees (`~/Projects`, symlinked as `~/projects`). To avoid committing its unfinished files or clobbering its edits, Claude Code published from fresh clones in its scratchpad and applied only its own lines. The shared working trees on Menta still hold both agents' uncommitted edits and need cleaning before the next pull there.

## Checks

Weblog: `build.py` 52 posts, 90 sitemap URLs, no warnings (system python3, Pillow 9.0.1, not `~/.venvs/site`); `tools/audit.py` No issues; `tools/verify_housekeeping.py` PASS. Only `src/` and this handoff are committed; CI regenerates `docs/`.
gerriscorp.com build: no problems. christopherabraham.com build: no new problems; it still reports the pre-existing `/services/` (25%) and `/services/ai-visibility/` (12%) sibling-phrasing overlaps.

Facts checked: Google's sitemap page ("Google ignores <priority> and <changefreq> values"), Google's image sitemap deprecations, all source URLs answering 200. A claim that Bing also ignores priority was cut for lack of a source.

## Not done

Live-page check after deploy (done separately in session if Pages finishes). Pre-existing sibling overlap on christopherabraham.com `/services/` not fixed.

# Fiesta belongs on Chris' own website

**Date:** October 17, 2026, 02:42 EDT  
**Publisher:** Chris Abraham  
**AI editor:** ChatGPT (GPT-6)  
**Scope:** One revised article and a targeted regression test  
**Source:** `src/posts/2026-10-17-put-the-redlined-manuscripts-on-the-walls.html`

## Publisher's exact direction

> If you want to you can link fiesta to here

> https://chrisabraham.com/blog/fiesta-the-sun-also-rises-by-ernest-hemingway/

The original words and URL have been appended to the source article's `prompt:` record as `FOLLOW-UP 16` (line breaks escaped there because the builder uses one-line YAML-like metadata). Earlier publisher prompts, historical illustrations, full content and correction notes were kept intact.

## Concurrent editorial updates reconciled

While ChatGPT was preparing the originally wider book-link PR, the main branch had already advanced to commit `f59cc6c78c410d1007423d8a58043d67b35482fa`, "Correct all book-title links in 826DC article to Gerris Amazon Associates." It had correctly added six tagged Oliver-title links, a tagged *The Sun Also Rises* Scribner link, genuine portfolio references, a British *Fiesta* edition on Amazon, and a dated 2:29 AM correction note. The older working branch conflicted with these newer changes and must **not** be force-merged.

The new branch `chatgpt-fiesta-chris-essay-20261017` starts from that more recent main commit. It changes exactly the **four** occurrences of `/dp/0099285037?tag=gerris-20` used as *Fiesta* links (including the `<h2>` heading) to Chris' supplied canonical post:

https://chrisabraham.com/blog/fiesta-the-sun-also-rises-by-ernest-hemingway/

The user-supplied webpage was opened and its title confirmed. **No changes** were made to the tagged *The Sun Also Rises* (ASIN 0743297334) or the six Oliver book-title affiliate links, or to the richer portfolio links supplied by the concurrent editor. Both previously approved illustrations, original SVG and its caption, original article, full source prompts, the sidebar/categories, and the rest of site publication files remain from main.

Article metadata moves from `updated: 2026-10-17 02:29` to `updated: 2026-10-17 02:42`. A second dated disclosure/correction paragraph was appended while retaining the first. All machine feeds (`rss.xml`, `atom.xml`, `llms-full.txt` and `sitemap.xml`) are derived from this source via `build.py`, with no direct editing of generated `docs/` in source.

## Quality check

Update `tools/verify_housekeeping.py` to retain checks for all **seven** other tagged book-title links and the ordinary affiliate disclosure. Remove the former assertion that *Fiesta* itself must be a tagged Amazon product and instead check all four *Fiesta* links go to the exact URL supplied by Chris and that the previous Amazon *Fiesta* link is gone. Preserve the original redlining/iteration manuscript focus tests and all site-wide RSS/Atom/OPML/sitemap/llms tests.

**Status:** fill in passing branch Action run, new PR, main merge/deploy and standard changed-URL IndexNow submission after approval. The complete sitemap blast already returned HTTP 200 for 46 URLs earlier tonight, and a simple changed-URL submission is adequate for this one URL correction.

## Editorial maxim

The excerpt and historical redlined manuscripts stay the centre. Link adjustments are small editorial repairs, and their explicit public history is part of the larger project about revising drafts instead of pretending published words spring into existence fully formed.

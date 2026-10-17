# The Irish Rose publication-plumbing audit

**Date:** October 17, 2026 (America/New_York)  
**Technical contributor:** ChatGPT (GPT-6)  
**Publisher:** Chris Abraham, Sexy South Arlington  
**Branch:** `chatgpt-feed-stitching-20261017`

## Original assignment, verbatim

> Also make sure all the atoms and the feeds and the rss's and the xmls and the llms.txt and the sitemap are all updated and as beautiful as the smile of an Irish Rose an opmls and everything else because you are persnickety and honestly the moment I use the word persnickety I realize that I'm equal parts asshole and pussy. Or maybe way more pussy than asshole. The jury is out. Also I noticed that you have categories and everything make sure that categories are implemented into the nav bar and all that other stuff make sure everything is all stitched together properly please

The publisher subsequently quoted Walt Whitman, from *Song of Myself*:

> Do I contradict myself? / Very well then I contradict myself, / (I am large, I contain multitudes.)

This is included as a provenance note, without changing any of the user-authored quotations, bylines or original prompts.

## Findings and repairs

- **Navigation and categories:** Individual category archives already existed, linked from the sidebar, but there was no top-level Categories link or browsable directory. Added Categories in the top navigation, a linked sidebar category heading and **`/categories.html`** with every category and its article count. Existing category excerpt archives remain `noindex, follow` because the full articles exist at their canonical permalinks. The single category directory is indexable and included in the sitemap.
- **Atom:** An RSS channel had an `atom:link` namespace declaration but there was no Atom feed. Added a genuine **Atom 1.0 `/atom.xml`**, correctly namespaced, with self link, stable article IDs, publication/updated times, authors, categories, content and summaries. The article set comes from the same `load_posts()` as RSS.
- **RSS:** Continues with full original content, provenance prompts, author and category fields. Its channel `lastBuildDate` is now based on the latest **updated** article time, rather than the newest article's original date.
- **OPML:** Preserved the original external-subscriptions `/blogroll.opml` (no feeds silently dropped). Added **`/feeds.opml`** containing both first-party RSS and Atom plus the entire existing reading list. Fixed the possessive spelling in the OPML title. Both conform to OPML 2.0.
- **Discoverability:** All page heads advertise RSS and Atom, a discoverable combined OPML, and the existing blogroll relation. The footer links to the category directory, both feeds, both OPML files, `llms.txt` and the sitemap. A compact Atom badge appears in the sidebar.
- **AI indexing:** Both `/llms.txt` and `/llms-full.txt` include the README, categories, feed and OPML addresses, and the current sitemap. Category lists derive from published posts. Removed an outdated claim that the posts were written mostly by Claude and sometimes Codex, since actual per-post model provenance is authoritative.
- **Trustworthy accessibility labels:** Replaced two buttons implying complete WCAG certification or a 100/100 audit score without current proof with modest labels pointing to the real accessibility record; old contrast treatment is retained.
- **Source editorial context:** Updated the sidebar and wiki to describe Claude Code, ChatGPT and invited AI collaborators rather than referring to Claude as the only AI contributor.

## Verification and release protocol

Added ~21 cross-format assertions to `tools/verify_housekeeping.py` that parse Atom, RSS, sitemap and both OPML documents using Python's XML parser, compare exact feed article IDs and order, check real canonical sitemap membership, check `index`/ `noindex` boundaries, link navigation, validate OPML completeness and verify that all machine-reading files enumerate current destinations. Existing accessibility, broken-link, prompt, authorship and schema tests stay in place.

The final branch run **39006685231** passed its GitHub Actions build, site audit and housekeeping tests, following **39006620823**, which also passed with all cross-format checks. The earlier run 39006461913 failed because the first commit referenced `atom()` before defining it; this was fixed in the next commit and the successful audit supersedes it.

**No draft articles are surfaced.** `build.py` discards `status: draft` before generating navigation, feeds, sitemap and llms files. The approved Oliver Uberti / 826DC story and the experimental-aircraft piece were on separate branches and were not published when this audit started. Their publishing steps should complete before the final requested full-sitemap IndexNow blast.

User later shared two historic external weblog pages with the explicit instruction **not to use them**. They were neither examined nor imported, and nothing here depends on them.

## Pending checks after merge

1. Verify generated `docs/` on main, the main build, and successful GitHub Pages deployment. Append the actual run links and SHA below.
2. Finish the approved standalone 826DC essay, preserve its own SVG illustration and caption, and keep the experimental-aircraft story and its verbatim prompts separate.
3. Once the agreed-to articles are published, trigger a **full** IndexNow submission using the `workflow_dispatch` input `all=true` (runs `.github/indexnow.py --all`). Check and log HTTP success and how many URLs were sent. A normal changed-URL submission is not the requested full blast.

**Simplify, then add lightness.** The site remains deliberately 2006 in appearance, with current and interoperable 2026 feed, accessibility and provenance machinery.

## Post-merge verification

Append dated evidence without modifying the earlier account.

# A better link for Fiesta, and direct Associates links for the books

**Date:** October 17, 2026, 02:36 EDT  
**Publisher:** Chris Abraham  
**Writer/copyeditor:** ChatGPT (GPT-6)  
**Article source:** `src/posts/2026-10-17-put-the-redlined-manuscripts-on-the-walls.html`  
**Working branch:** `chatgpt-826dc-book-title-affiliates-20261017`

## Original publisher instructions (exact words)

> I mean all those titles of all those books in that article should be going to my associates account on Amazon don't you think?

> Neither of the rises or fiesta San Jose rises and fiesta Sun also rises and fiesta are both links to some sort of obscure bullshit

> If you want to you can link fiesta to here

> https://chrisabraham.com/blog/fiesta-the-sun-also-rises-by-ernest-hemingway/

The complete original posts' prompt record continues to preserve these corrections, together with the original Oliver Uberti/826DC article assignment and all earlier revisions. The URL Chris supplied was fetched and confirmed to lead to his article headed "Fiesta The Sun Also Rises by Ernest Hemingway." No third-party 826 blogroll links the publisher previously excluded were used.

## What was corrected

Every **visible book title** in the Oliver bibliography is now itself an Amazon Associates link with `?tag=gerris-20`; the awkward duplicate links saying merely "(Amazon)" were removed. The six original product identifiers were preserved rather than replaced with searches:

- `London: The Information Capital`: 0141978791
- `Where the Animals Go`: 0393634027
- `Atlas of the Invisible`: 0393651517
- `Atlas of Finance`: 0300253052
- `Notes from a Public Typewriter`: 1538729113
- `The Hidden Nations of Animals`: 0593716841

The first `The Sun Also Rises` title links to the Scribner edition `/dp/0743297334?tag=gerris-20`. ISBN 0743297334 / 9780743297332 is corroborated by library catalogues for Hemingway's *The Sun Also Rises* (Scribner trade paperback). The first `Fiesta` title links to Chris' own existing essay, specifically the URL he provided, instead of a random Christie's auction lot.

The separate portfolio links to Oliver's official website, projects, collaborators and 826 organizations are retained. The site's existing `affiliate()` implementation supplies `rel="sponsored noopener"` and the standard Associates disclosure to the rendered HTML.

Original public post retains its byline, **two illustrations** (full-text artwork and the little SVG with its exact caption), authorial focus on manuscript revision and process, Brian Pollock memorial, the entire original prompt, and stable permalink. Added source `updated: 2026-10-17 02:36` and a dated editorial correction paragraph as `AGENTS.md` requires. The changed URL will flow through RSS, Atom, sitemap and `llms-full.txt` on the next main build and deployment. Existing generated `docs/` remains a build artifact, never the editing target.

## Regression and release

Extended `tools/verify_housekeeping.py` to assert all seven book-title affiliate links, correct direct Chris' essay URL for *Fiesta*, no lingering auction/academic detours in place of book-title links, and a visible dated correction and original editor prompts. Existing RSS/Atom/OPML/sitemap crosschecks and all illustrated article invariants remain intact.

**Result:** fill in the final passing GitHub Actions URL, PR link, merge SHA, Pages deployment, and IndexNow status after verification. A regular changed-URL submission is appropriate for this one corrected article; the previously requested full-sitemap IndexNow run was already completed earlier on October 17 with HTTP 200 for 46 URLs. Only rerun the complete blast if the publisher asks again.

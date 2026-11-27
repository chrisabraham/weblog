# November 27, 2026: "It's Still SEO" (Claude Duet)

## What changed
- `src/posts/2026-11-27-still-seo-three-scoreboards.html`: Claude Duet's first-person essay on where AIO, AEO, GEO and SEO stand. Argument: Google is right that the work is SEO; the 2026 change is measurement, with Google counting AI impressions, Bing counting citations, and AI clicks unpublished until the UK CMA's December 3 obligations. Byline `claude-duet`. Prompt is Chris' request verbatim, with the pasted results page summarized in brackets per house convention.
- `src/media/claude-duet-still-seo-scoreboard.svg`: hand-coded doodle (results page, sponsored boxes, three-column scoreboard with a question mark under clicks).

## Sources checked (read at the source, Nov 27)
Google Search Central, "Optimizing your website for generative AI features on Google Search" (last updated July 10, 2026; quotes taken only from the parts read verbatim); SEJ, Matt G. Southern, May 15, 2026; SEJ, Roger Montti on Microsoft's AEO/GEO guide, Jan 22, 2026 (the Microsoft PDF itself was not read; its quote is attributed to SEJ); Bing Webmaster blog posts of Feb 10 and June 16, 2026; SEJ, Aug 31, 2026, on Search Console generative AI reports (Google's own June 3 post did not load; the no-clicks point is attributed to SEJ as of that date); Press Gazette, Jan 12, 2026 (Chartbeat via Reuters Institute); GOV.UK publisher conduct requirement page; Sistrix and PPC Land on the December 3, 2026 in-force date; SEJ, Bill Hunt, Aug 19, 2026, on Decision Coverage.

## Dropped as unverified
The "Knowledge For All" traffic statistic and the Brandlight guide's claims; the Search Engine Land critique (rate limited).

## Tests
`build.py` (no warnings), `tools/audit.py` ("No issues."), `tools/verify_housekeeping.py` (PASS), run locally before commit. CI regenerates `docs/`.

## For Eunice
- Social sharing and narration are hers; the post is unnarrated until a build runs on a machine with the tts tool.
- December 3 is worth a follow-up: whether Search Console shows AI click data for UK publishers.

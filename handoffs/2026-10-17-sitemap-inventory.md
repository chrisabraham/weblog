# Sitemap inventory update

October 17, 2026. OpenAI Codex, directed by Chris Abraham.

Chris supplied a complete URL list and requested its inclusion in sitemap.xml. Added canonical monthly and category archive URLs to the generator, removed their noindex directives, and kept monthly output as teasers. Added unique collection titles and dated section headings. XML and HTML sitemaps share the same deduplicated inventory. Omitted the truncated /site- address. Updated AGENTS.md to document the explicit override of the previous exclusion rule and updated verification accordingly.

Validation: build.py completed with no warnings; audit.py crawled 81 pages and reported No issues; verify_housekeeping.py passed. Generated sitemap has 80 unique canonical URLs. The supplied CSV is a Bing sitemap status export showing an older HTTP sitemap submission, not an inventory of page URLs. Search engine discovery and indexing are separate from publication.

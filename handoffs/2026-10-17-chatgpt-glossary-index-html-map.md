# October 17, 2026: Three lightweight references on chrisabraham.net

Contributor: ChatGPT (GPT-6)
Publisher: Chris Abraham
Branch: glossary-index-html-sitemap-20261017
Source: chrisabraham/weblog
Previous work: handoffs/2026-10-17-chatgpt-wiki-harvest-codex.md

## Request and constraints

Chris asked for three new separate public reference pages following the design of his other four personal and professional sites. The words belong in a simple glossary, the subjects in a back-of-the-book index, and every indexable page in a human-readable HTML site map. These are not wiki pages and must not be promoted in the primary navigation. They belong in small footer links only. The glossary definition length is at MOST 500 characters, but can be 60, 180, 300 or anything shorter when that is sufficient. The guiding rule is the Lotus principle: simplify and add lightness. Avoid duplicate excerpts or ornamental prose.

Inspected sister site patterns on christopherabraham.com/guides/glossary/, christopherabraham.com/site-index/ and gerriscorp.com/site-index/, which use concise anchored definitions and alphabetized page locators, distinct from a plain site map. Did not import their text. All content is written for THIS weblog's actual source corpus.

## Implementation

- src/glossary.json: 83 distinct terms and concise original definitions curated from all 22 currently published weblog posts and the 14 wiki references. Each source target is required to be an actual published article, wiki, or static page. Definitions are validated as 1–500 characters; this set averages far shorter. All entries get stable anchors, letter navigation and a contextual source link.
- src/site-index.json: 108 curated additional subject/headings, proper names, tools and synonym patterns. The generator merges these with glossary headings, searches actual page titles and body text in all published posts, wiki pages, standalone pages and the project descriptions, ranks real locators and skips headings with no occurrence. It limits results to seven distinct page locators per subject. The first validated build found 151 heading entries; the index points to material instead of duplicating explanations.
- tools/reference_pages.py: a dedicated plain-Python generator called from build.py after loading posts, wiki, authors and static pages. It creates /glossary.html, /site-index.html, /site-map.html, uses standard page shells and truthful schema (DefinedTermSet for the visible glossary, CollectionPage for the index and HTML map), and adds all three to the XML sitemap.
- /site-map.html is generated from exactly the same sitemap list as /sitemap.xml. It lists every indexable canonical URL precisely once in a compact nested tree: articles by month, wiki, authors, and other site pages. The builder refuses any difference.
- build.py: calls the reference generator, adds three small footer links only, and includes them in both llms.txt outputs. Primary navigation is unchanged. RSS, Atom and OPML still describe dated articles and subscribed reading feeds rather than references.
- src/style.css: adds minimal responsive CSS for alphabetical letter links, compact definition lists, page locators and the tree. No JavaScript or new illustrations.
- tools/verify_housekeeping.py: validates source definition lengths, unique glossary anchors, source URL membership, sufficient index locators, full HTML-vs-XML sitemap parity, footer-only links, machine-reference visibility, and the existing sitewide schema/links/media checks.
- AGENTS.md: new editorial and technical house instructions for future AI writers.

## Testing and repair trail

The first site build generated 83 glossary definitions, 151 index headings, and 56 XML/HTML sitemap URLs, but the audit flagged identical first H2 headings ('0–9') on the glossary and index. The header wording was changed to '0–9 terms' and '0–9 topics'. Subsequent source build and audit passed.

A new sitemap regression test initially missed the root address '/' because its regex required an additional character after the slash. The generated HTML and XML pages both contained '/', and a direct comparison showed 55 matched against 56 expected with '/' as the only omission. The test regex was corrected to include root. Latest Actions run at the time of this file should be checked: a green run at commit 7a63d62b8903825c06fefa07e3ebc10ad93c55e8 confirmed the corrected test succeeded; additional AGENTS.md updates may have triggered another run.

The publication check must confirm:
- python build.py prints no warnings;
- python tools/audit.py reports 'No issues.';
- python tools/verify_housekeeping.py reports all assertions PASS;
- docs/glossary.html, docs/site-index.html, docs/site-map.html exist, with correct canonical tags, metadata, indexable robots, social cards and schema;
- the footer links all three, the top nav links none;
- the XML sitemap has 56 canonical URLs, HTML map has the exact 56;
- RSS/Atom still have 22 identical posts, OPML output remains valid;
- sitewide internal links all resolve and images have nonempty alt text.

After verifying a clean Actions build, merge PR to main, confirm GitHub Pages deployment and the IndexNow workflow. Chris instructed ONLY diff-based IndexNow, not a full sitemap blast. Do not claim IndexNow succeeded unless the actual HTTP response and submitted URL count are confirmed.

## Publishing philosophy and ongoing maintenance

The wiki is the changing reference shelf. The blog preserves dated editorial articles and human prompts. The glossary defines words in the fewest useful characters; the index is for finding where the subject appears; the HTML map is for seeing the actual page structure. Never allow them to become three redundant copies of the same paragraphs. Add a glossary entry only when it meaningfully helps explain a term found on the site. Page locators must be actual source mentions and the sitemap must always reflect live canonical page inventory. As new posts appear, index and HTML map update automatically. The glossary list remains a curated editorial source. New art remains SVG-first, lightweight and eccentric.

Prior handoffs carry the repo architecture, testing requirements, accessibility rules, generative AI attribution and original 2003-web site design philosophy.


## Publication and final verification

Published via PR #23: https://github.com/chrisabraham/weblog/pull/23
Squash merge: 4b1d9201b20178969d0f0d520c40ec9bf98c4dd5
Latest source-branch audit: https://github.com/chrisabraham/weblog/actions/runs/39049899374 (success).
GitHub Pages deployment: https://github.com/chrisabraham/weblog/actions/runs/39049958385 (success).
Final generator: 83 definitions, 148 distinct index headings after removing misleading/duplicate candidates, 56 HTML/XML sitemap URLs, 22 RSS posts and 22 Atom entries.
The complete run passed 107 regression assertions across 81 generated HTML pages, reported No issues. from the audit, and found zero broken generated internal links, zero missing image alternatives and zero invalid JSON-LD blocks.
Canonicals:
- https://chrisabraham.net/glossary.html
- https://chrisabraham.net/site-index.html
- https://chrisabraham.net/site-map.html
Public external HEAD/GET checks could not run in the current environment because direct DNS/web fetch was inaccessible; deployment success was confirmed by GitHub Pages Actions and generated docs were independently checked in GitHub.
IndexNow: the existing workflow is configured for diff-only submissions from main docs changes, but no accepted HTTP response or submitted URL count could be confirmed here. Codex should check whether IndexNow actually ran before marking that step complete. Do not claim success from a configuration file or Pages deployment alone.

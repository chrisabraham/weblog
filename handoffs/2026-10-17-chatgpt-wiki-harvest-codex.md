# 2026-10-17 handoff to Codex

Publisher: Chris Abraham. Contributor: ChatGPT (GPT-6).
Repository: chrisabraham/weblog
Branch: topic-centered-google-vacuum-essay-20261017
Read AGENTS.md and prior handoffs before touching the project.

## Editorial decisions

The revised Google Abhors a Vacuum article concerns how search engines construct a public identity using available records. It must not become a first-person career story or sales pitch. The original prompts and revisions remain in the source and Git history. The article covers public archives, third-party reports, privacy, online perception management, ghost towns, coral reefs, used domains, maintenance, Googlebot crawling and evidence from both Google guidance and ORM practitioners.

The blog carries dated original essays; the wiki carries separate evergreen methods, checklists and references. Preserve the distinct purposes of both. No artificial duplicate copy.

## Harvest completed on this branch

Reviewed all 22 posts and 10 preexisting wiki pages.
Rewrote src/posts/2026-10-17-google-abhors-a-vacuum.html.
Created four evergreen references:
- src/wiki/online-perception-management-field-guide.html
- src/wiki/ai-search-visibility-methods.html
- src/wiki/ai-editorial-provenance-and-handoffs.html
- src/wiki/static-weblog-operations.html

Extended existing wiki pages: blackbox.html, ai-visibility-report.html, build-a-personal-weblog-with-ai.html, connections.html and pinebox.html.

Simplified build.py wiki directory to list every page once in a thematic shelf. Removed the redundant recent-edit directory and huge sidebar page listing. tools/verify_housekeeping.py asserts every wiki page is listed once and sidebar navigation remains compact.

## Engineering house style

Colin Chapman of Lotus: “Simplify, then add lightness.” The publisher's adaptation is “Simplify, then add quickness.”

All NEW editorial artwork should be tiny, playful 2006-style SVG doodles unless Chris explicitly requests or provides a bitmap. Keep historic art intact. Existing raster media may be compressed aggressively to WebP as long as blockiness, blotches and pixelation do not harm professional presentation. The current builder generates WebP derivatives (quality 67), and smaller legacy JPEG URLs (quality 66) while preserving source masters in src/media. SVG and AVIF sources remain unchanged. Original article source references are preserved while generated HTML, RSS, Atom and sitemap reference WebP. The seven standalone SVGs together are about 34.7KB.

AGENTS.md now contains these artwork rules, the Lotus principle, and exact publishing expectations.

## Validations and pending tasks

Pipeline commands:
python build.py
python tools/audit.py
python tools/verify_housekeeping.py

Site uses Python to regenerate docs. Its GitHub Pages source is main:/docs. House SEO rules: title 45-60 chars and under 561px; description 120-155 chars and under 985px. Verify accurate BlogPosting/Article/CollectionPage schema, original prompts, timestamps, alt text, mobile legibility and accessible navigation. Recent branch builds reported zero broken internal links, zero missing alt attributes and zero invalid JSON-LD, and validated RSS/Atom/OPML and the sitemap.

Some intermediate GitHub Actions builds failed when multiple simultaneous runs attempted to push the generated docs/ directory. This was a non-fast-forward race during Save reproducible generated site, not a content audit failure. Wait for latest run to finish without additional overlapping source commits. No force push.

Once successful: review and merge pull request, confirm Pages deployment and all generated wiki and blog URLs, verify sitemap.xml, rss.xml, atom.xml, both OPML files and llms files. Inspect representative WebP quality.

IndexNow: the publisher explicitly corrected earlier broad requests. Send only URLs changed in this publication's diff using the existing main-branch IndexNow workflow. Do NOT run the all=true workflow. Record HTTP result and URL count. Do not claim submission succeeded before confirming the run.

After final publication, leave the verified PR and Actions links and communicate unresolved items frankly. The source repo and prior handoffs preserve full historical reasoning and changes.

# ChatGPT handoff: a personal weblog restomod tutorial

Date: October 17, 2026, America/New_York
Contributor: ChatGPT (GPT-6)
Publisher: Chris Abraham
Branch: `chatgpt-jekyll-old-web-tutorial-20261017`

## Original editorial request
Chris assigned a long tutorial about making a personal weblog like chrisabraham.net after a Mastodon exchange with Nash Ricky. The original dictated assignment and subsequent revisions are preserved verbatim in the new article's `prompt:` metadata rather than paraphrased or corrected. In follow-ups he specified the actual Python engine, not Jekyll, and described the 2003/2004 body and 2026 restomod chassis (ICON 4x4). He insisted on mentioning his exceptionally persnickety accessibility, text-browser, Creative Commons, feeds, schema, PageSpeed and attribution standards, while emphasizing they are optional for a beginner.

## Changes
- `src/posts/2026-10-17-build-a-2004-weblog-with-ai.html`: long-form, novice-first tutorial, honest description of real repo structure, five pasteable prompts and current tool/permissions distinctions. Article links to the companion wiki entry.
- `src/wiki/build-a-personal-weblog-with-ai.html`: evergreen quickstart reference, prompts, troubleshooting, optional restomod checklist, official reference links and backlink to the dated story.
- `src/media/chatgpt-old-web-restomod.svg`: editorial illustration conceived from the earlier image-generating session, translated into a self-contained accessible, hand-authored SVG for repository publication.
- `src/media/chatgpt-small-web-helper.svg`: accessible cheerful retro-computer SVG doodle used inline in the article, based on the earlier rendered retro-computer concept.
- This handoff.

## Sources checked and limits
- Repository and generator inspected through the connected GitHub integration on October 17, 2026; `AGENTS.md`, `README.md`, `build.py`, publication workflow and representative posts/wiki reviewed before writing.
- Official GitHub Pages sources checked for Pages GitHub Actions artifact deployment, branch:/docs and .nojekyll, and custom domain.
- Official Anthropic help checked for Claude Code cloud GitHub PR workflows and ordinary Claude GitHub read integration.
- Official OpenAI help checked for ordinary ChatGPT GitHub read-only connection and Codex as the editing route.
- The two Mastodon original thread pages returned an access error in web retrieval; wording was based on Chris' screenshots, so direct quotes beyond those visible were avoided.
- **Image limitation:** The earlier full-colour image generation files are available in the ChatGPT conversation, but the connected GitHub text-file tool cannot transfer binary files from the conversation container. Instead, the published article uses accessible SVG illustrations faithfully based on the previously generated compositions. The original raster image remains available to the publisher separately. Do not claim the raster PNG was placed in GitHub.
- This revision changes only new source files and no earlier AI's writing. All generated output is handled by the existing repository builder.
- Do not assume the site has finished deploying based only on a source commit or PR merge. Check build, audit, deployment and public URLs.

## Build and QA
Expected repository CI:
```
python build.py
python tools/audit.py
python tools/verify_housekeeping.py
```
Check for builder warnings, alt and SVG labels, valid wiki links, no broken links and feed/sitemap/llms consistency. Inspect GitHub Actions and actual Pages status after merge.

## Suggested next improvement
If Chris wants the original high-detail full-colour image, upload `oldweb_article_banner.jpg` or `cozy_ai_to_cloud_night_workspace.png` from the ChatGPT conversation into `src/media/`, then replace the article's first SVG figure reference and run full QA. The existing SVG can remain as an alternate illustration.

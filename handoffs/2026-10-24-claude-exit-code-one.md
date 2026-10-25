# Claude (the app): "Exit code one," two guides, one service page

Date: 2026-10-24
Agent: Claude Opus 5.5 in the Claude app (cloud sandbox, not Pinebox)

## What changed

chrisabraham.net (this repo)
- `src/posts/2026-10-24-exit-code-one.html`: second post under the `claude` byline, with an original SVG doodle. Prompt preserved verbatim.
- `docs/`: regenerated.

gerriscorp.com (chrisabraham/gerriscorp)
- `src/guides/two-problems-at-once.html`: new Diagnosis guide, listed in `src/guides/index.html`, registered in `FILES`, indexed in `tools/site_index.json`.
- `src/services/shared-ai-memory.html`: new service (Consulting and technical direction group) selling the Oversoul pattern, listed in `src/services/index.html`, indexed.

christopherabraham.com (chrisabraham/christopherabraham)
- `src/guides/disavow-links.html`: new guide under Indexing and audits, registered and indexed. Sources: Google's Search Console help page for the disavow tool, Mueller's April 2024 and April 2025 remarks as reported by Search Engine Roundtable and Search Engine Journal. A widely repeated March 2026 Mueller quote was left out because no primary source could be found.

## Checks

Weblog: build clean, `tools/audit.py` No issues, `tools/verify_housekeeping.py` PASS (system python3, Pillow 12.3.0).
Rebased onto the latest main of each repo before pushing. gerriscorp.com now builds with exit 0. christopherabraham.com exits 1 on the five pre-existing sibling problems only. My pages add no problems on either site.

## For Chris (not fixed, your call)

1. Resolved upstream at 20:43 (commit b664fef): pre-existing gerriscorp.com failures, 18 PROBLEM lines, first person plural ("We run your money searches") on `src/services/ai-visibility.html` and `src/guides/ai-answers-review-searches.html` (both dated 2026-10-23), plus one spaced dash. Possibly deliberate for the priced offer; the build treats it as an error.
2. Pre-existing christopherabraham.com failures, sibling rule: `/services/` shares 25% of its phrasing with Gerris `/services/` and repeats three sentences; `/services/ai-visibility/` shares 12% with its Gerris twin.
3. The sibling check in `christopherabraham/tools/build.py` looks for `../gerris` (line 81). The GitHub repo is `gerriscorp`, so a plain clone skips the check with a one-line note and exits 0. The `build.yml` workflow checks out one repo, so the rule never runs in CI. Suggested fix: fail when the sibling is missing, and check out `chrisabraham/gerriscorp` into `../gerris` in the workflow. I ran it locally via a symlink `gerris -> gerriscorp`.

## Not done

Live visual check after Pages deploys. No IndexNow beyond the existing push-triggered workflows.

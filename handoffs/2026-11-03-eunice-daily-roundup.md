# Handoff — 2026-11-03 — Eunice (Muse Wonder)

## What changed
- Added `src/posts/2026-11-03-ai-roundup-one-model-rewrote-another.html`: Tuesday daily AI roundup, "AI Roundup: One Model Rewrote Another" (6 items: MIT CSAIL Weight-Space Programming, GPT-6 Astra editing 0.016% of Qwen3.5-0.8B weights with MATH-500 up to 6x and IFEval ~3x, no training, with the independent rerun caveat that a free setting matched the gain; Google moving brand AI Overviews into the right-column Knowledge Panel spot with Ahrefs brand measurements and Digiday's 18 buyers questioning 10–30% of search budgets; Turkey Rekabet Kurumu's AI Overviews/AI Mode investigation announced Nov 2 with the Oct 8 interim measure requiring non-discriminatory, value-reflecting publisher terms; WorkOS ARTEX breach of an internal sales application, detected Oct 30, bulletin Nov 2; RIKEN five silicon qubits on a shared microwave line above 99.9% together in Nature Physics; LIVE-GEO live-page GEO benchmark, CORE 66.3–76.3%, engine agreement 48.8–66.3%, faithfulness flags on 86/400 rewrites).
- Added `src/media/one-model-rewrote-another.svg`: Eunice's doodle for the roundup (two model boxes, a weight grid, one amber cell, a wrench).
- Refreshed the three posts edited by linking pass 1 on Nov 2 evening (sixteen-of-eleven-hundred, the-first-name-back, ai-overviews-causal-click-loss) from current main before building, so the regeneration does not revert those links.
- Regenerated `docs/` with build.py (build commit follows with the fixed regeneration message).

## Checks run
- `~/.venvs/site/bin/python build.py` — exit 0, no warnings from the new post; 98 posts built, 138 sitemap URLs.
- `python3 tools/audit.py` — "No issues." (196 pages crawled)
- `python3 tools/verify_housekeeping.py` — PASS.

## What could not be verified
- The MIT weight-editing effect size is contested in public: the team's own report gives up to sixfold on MATH-500; an independent overnight rerun confirmed the edit and the 7.9% to 48.1% move but reported a free setting matched it. Both are labelled in the post.
- LIVE-GEO is an arXiv preprint, not peer reviewed, with fictional brands and product pages only. Labelled in the post.
- WorkOS exposure categories describe what the application could access, not a record-by-record confirmed access list. Stated in the post via WorkOS' own framing.
- Turkey's interim measure sets no deadline or fine in the announcement and covers news publishers only. Stated in the post.

## Next action
- Friday best-of job builds from `~/workspace/drafts/weblog-ai-intel-week-log.md`, which now carries the full Nov 3 scan and runners-up.

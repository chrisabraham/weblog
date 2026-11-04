# Handoff — 2026-11-04 — Eunice (Muse Wonder)

## What changed
- Added `src/posts/2026-11-04-ai-roundup-the-customers-are-machines-now.html`: Wednesday daily AI roundup, "AI Roundup: The Customers Are Machines Now" (6 items: Menlo Ventures 2026 State of Enterprise AI, $176.8B deployment spend and agents at 80% of OpenRouter tokens; OpenAI's claim that ChatGPT search-like queries are roughly one fifth of Google's on 1.2B weekly users, labelled a company claim with no method disclosed; Google K-12 changes, services off by default and separately enableable but no AI-free Search; Anthropic's amended S-1/A of Nov 2 saying future models may imminently meet its Responsible Scaling Policy accelerated-progress threshold and that acceleration may be noticed only after the fact; CrowdStrike AI Kill Switch plus Fiddler and Dreadnode acquisitions agreed but not closed, prices per WSJ reporting; Regensburg bistable qubit, one pre-run measurement cutting average error from about 0.14% to 0.065%).
- Added `src/media/the-customers-are-machines-now.svg`: Eunice's doodle for the roundup (agent boxes at a counter, a human behind it, an amber switch on the wall).
- Base snapshot refreshed from current main before building, including the Nov 3 GitHub Pages guide post and its anonymized prompt field, so the regeneration does not revert it.
- Regenerated `docs/` with build.py (build commit follows with the fixed regeneration message).

## Checks run
- `~/.venvs/site/bin/python build.py` — exit 0, no warnings from the new post; 99 posts built, 139 sitemap URLs.
- `python3 tools/audit.py` — "No issues." (199 pages crawled)
- `python3 tools/verify_housekeeping.py` — PASS. (A first run overlapped the tail of the build and failed the categories-directory check; the re-run on the finished build passes.)

## What could not be verified
- OpenAI's 20%-of-Google figure is OpenAI's own estimate with a generous definition and no disclosed method; no independent check exists. Labelled in the post, including the September 29 timeline inconsistency in the weekly-user growth claim.
- Menlo's market totals are Menlo estimates from a survey plus a bottom-up model, and Menlo is an investor in Anthropic and OpenRouter. Disclosed in the post.
- CrowdStrike's acquisition prices come from Wall Street Journal reporting, not the company; both deals are unclosed and endpoint termination for the Kill Switch is still forthcoming. Stated in the post.
- Anthropic's threshold language concerns future models; no current model is designated as exceeding it. Stated in the post.

## Next action
- Friday best-of job builds from `~/workspace/drafts/weblog-ai-intel-week-log.md`, which now carries the full Nov 4 scan and runners-up.

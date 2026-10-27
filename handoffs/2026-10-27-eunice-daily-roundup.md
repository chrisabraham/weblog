# Handoff — 2026-10-27 — Eunice (Muse Wonder)

## What changed
- Added `src/posts/2026-10-27-ai-roundup-money-in-people-out.html`: Tuesday daily AI roundup, "AI Roundup: Money In, People Out" (6 items: Anthropic S-1 filing as ANT, $16.3B H1 revenue / $80.7B paper net loss; Meta up-to-$95B equity raise; Microsoft voluntary buyouts to ~60,000; SE Ranking AI Overviews on 82.5% of US brand searches; India's 21 publishers challenge DPDP privacy law as pre-censorship; Baidu Unlimited-OCR-2 open under MIT).
- Added `src/media/money-in-people-out.svg`: Eunice's doodle for the roundup (prospectus catching coins, figures exiting a door).
- Regenerated `docs/` with build.py (build commit follows with the fixed regeneration message).

## Checks run
- `~/.venvs/site/bin/python build.py` — exit 0, no warnings from the new post; 64 posts built.
- `python3 tools/audit.py` — "No issues."
- `python3 tools/verify_housekeeping.py` — PASS.
- Live URL verified after Pages lag: https://chrisabraham.net/2026/10/ai-roundup-money-in-people-out.html

## What could not be verified
- Anthropic's reported $1.5–2T valuation / $100B raise are press expectations, labelled as such in the post; the S-1 leaves shares and price blank.
- Meta's $60B at-the-market programme is planned, not finalised; chipmaker $5B interest is expressed interest, not a commitment (per Reuters).
- Microsoft did not confirm the 60,000 eligibility figure to Reuters; labelled in the post.
- SE Ranking study is vendor-published, desktop-only; Baidu's OCR benchmark scores are self-reported from a chart image; both labelled in the post.
- Binary assets (narration MP3 for this post and its share-card PNG) are generated locally by the build but are not part of the UTF-8 snapshot pushes; they follow the established separate binary upload route (cf. the Oct 27 00:12/00:44 binary commits).

## Next action
- Friday best-of job builds from `~/workspace/drafts/weblog-ai-intel-week-log.md`, which now includes the full Oct 27 scan and runners-up.

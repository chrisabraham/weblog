# Handoff — 2026-11-20 — Eunice (Muse Wonder)

## What changed
- Added `src/posts/2026-11-20-ai-roundup-best-of-the-week-priced-checked-and-contained.html`: Friday best-of-the-week AI roundup, "AI Roundup: Best of the Week, Priced, Checked, and Contained" (7 items selected from the November 14 to 20 daily editions: the Anthropic IPO arc from six-times-covered roadshow to the $83 pricing and the $97.17 first close on a rout day; Nvidia's succession test, from the Huang resignation and the Journal's circular-financing reporting to the $115.844 billion earnings beat and the board closing the restoration question; the containment market, California v. OpenAI, Google's exploit_agent finding, the disclosure-clock cuts, and OpenAI's healthcare agents and GPT-6.2 Control Room; proof over claim, the cloned Courtade-Kumar formalization against the unpublished Weil headline, the Lean-proved quantum program savings, and the TCBP-JOBS decoder; the schools and citation ledger, Chicago to the 1.57-million-student districts, the CMA December 3 deadline, and the Mention Impossible and Citefold studies; the frontier at scale, Shenzhen's 100-million-atom DFT, the Gordon Bell FeMoco win on LineShine, Willow contextuality in Science, and the opened SatWeave and PARDIG datasets; and Torvalds' fairly normal 7.4-rc3 beside the llama.cpp 1.0 stability contract).
- Added `src/media/best-of-the-week-priced-checked-contained.svg`: Eunice's doodle for the roundup (a ticker reading ANT 97.17, a gavel over a lab door, a checked proof scroll, and a schoolhouse holding a search box at arm's length).
- Regenerated `docs/` with build.py (build commits follow with the fixed regeneration message).

## Checks run
- `python build.py` — exit 0, zero warnings from the new post.
- `python3 tools/audit.py` — "No issues."
- `python3 tools/verify_housekeeping.py` — PASS.
- Live URL verified after Pages lag: https://chrisabraham.net/2026/11/ai-roundup-best-of-the-week-priced-checked-and-contained.html

## What could not be verified
- Chris' Feed could not be scanned from this scheduled run (the feed unit list/search tools are main-conversation only); the best-of was built from all seven daily editions, November 14 to 20, including Friday's daily scan notes and its runners-up.
- The standing week log file (weblog-ai-intel-week-log.md) did not exist at run start; the daily editions and their scan notes served as the week's materials. There was no live week log to archive; the prior archived log remains weblog-ai-intel-week-log-2026-11-13.md.
- Friday's daily edition, "AI Roundup: The Debut Won, the Day Lost," was built locally in the daily clone but had not been pushed to the remote or the live site when this best-of published (its live URL returned the site's 404 page in both a text fetch and a live browser check at 06:21 ET). This best-of therefore carries Friday's items from the daily scan notes and links only to live daily editions; it does not link to Friday's daily URL.
- Figures carry the labels the daily editions gave them: allegations in the California complaint are labeled allegations, roadshow and petition figures are labeled reported or self-reported, and preprints are named as such in the text.
- The new post's narration MP3 was generated locally (src/audio and docs/audio) and, per the standing binary flow, is not part of the text push-files commits.

## Next action
- Friday's daily edition still needs its own push from the daily clone (src/posts/2026-11-20-ai-roundup-the-debut-won-the-day-lost.html is untracked there, with its generated docs page and share card).
- Next week's materials start fresh with Saturday's daily roundup.

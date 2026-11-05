# Handoff — 2026-11-05 — Eunice (Muse Wonder)

## What changed
- Added `src/posts/2026-11-05-ai-roundup-proof-over-promise.html`: Thursday daily AI roundup, "AI Roundup: Proof Over Promise" (6 items: OpenAI's Linux kernel campaign, 2,308 candidates, 1,724 dynamically reproduced, 948 unique local privilege-escalation vulnerabilities, $1,213,430 in API credits as model-use cost only, vendor-reported and not independently reproduced; Anthropic's first prokaryotic vault structure, phage protein L05 at 96 copies and about 9.5 megadaltons, Claude's two disclosed errors kept in the record, bioRxiv preprint not peer reviewed and E. coli only; Adthena's count of 204,489 ChatGPT ad placements June to September 2026 and 175,100 paid placements inside US AI answers; Victorious Q3 panel, AI Overviews on 97.5% of 34 category questions and 37% of citations from the organic top 10 against 13% to 18% for ChatGPT, Perplexity, and Copilot, directional by the agency's own account; Tencent Hy4 launch with vision and computer use, weights and system card still pending; IQM Emerald GHZ entanglement across all 54 qubits at fidelity 0.516 with readout error mitigation, company-reported).
- Added `src/media/proof-over-promise.svg`: Eunice's doodle for the roundup (a magnifying glass over a kernel gear, a barrel-shaped vault, and three small price tags).
- Base refreshed from current main (fa7f096) before building, including the Nov 4 site-placement moves to The Chris Abraham Show, so the regeneration does not revert them.
- Regenerated `docs/` with build.py (the GitHub Actions regeneration follows with the fixed regeneration message).

## Checks run
- `~/.venvs/site/bin/python build.py` — exit 0, zero warnings; 105 posts built, 145 sitemap URLs. Narration for the new post was generated with the local TTS (8,007,013 bytes, voice avocado_v2:qvd_02406) and recorded in `src/audio.json` before the gate build; the gate build itself ran on the CI path (no TTS tool), the same path GitHub Actions uses, with committed narrations riding along.
- `python3 tools/audit.py` — "No issues." (213 pages crawled)
- `python3 tools/verify_housekeeping.py` — PASS.

## What could not be verified
- OpenAI's kernel figures are vendor-reported via a research summary; no independent reproduction exists. Labelled in the post, including that hundreds of reports and patches sent is not 948 fixes deployed.
- Anthropic's vault work is a bioRxiv preprint, not peer reviewed; particles were produced only in engineered E. coli and native formation is unshown. Stated in the post.
- Adthena's and Victorious' numbers are vendor and agency panels with an interest in the market they measure; forecasts are labelled as the vendors' own. Stated in the post.
- Tencent Hy4's weights, system card, and independent long-horizon evaluations do not exist yet in the reporting read. Stated in the post.
- IQM's fidelities are company-reported from a company announcement. Stated in the post.
- NVIDIA's 104-qubit JUPITER simulation recirculated on Nov 5 with fresh aggregator timestamps is October 19 news; held out of the roundup as stale and logged in the week log.

## Next action
- Friday best-of job builds from `~/workspace/drafts/weblog-ai-intel-week-log.md`, which now carries the full Nov 5 scan and runners-up.

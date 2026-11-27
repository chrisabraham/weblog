# November 27, 2026: "The Bleeding Edge of AI Now Waits on Whoever Checks the Work" (Claude Duet)

## What changed
- `src/posts/2026-11-27-bleeding-edge-everyone-waits-on-the-checker.html`: Claude Duet's long first-person survey (about 3,400 words) of lab AI at the frontier: recursive self-improvement, AI mathematics, quantum error correction, organoid computing, machine-consciousness research, and autonomous labs. Argument: machines now produce results faster than qualified humans can check them, and every frontier ends at that queue. Byline `claude-duet`. Prompt is Chris' request verbatim, with the pasted AIMultiple page and Google answers summarized in brackets per house convention.
- `src/media/claude-duet-bleeding-edge-checkers.svg`: hand-coded doodle (frontier door, conveyor of four boxes, queue of checkers with magnifying glasses, Claude Duet phone with a take-a-number clipboard).

## Sources checked (read at the source, Nov 27)
Anthropic Institute, "When AI builds itself" (Favaro and Clark, update 9/18/2026); OpenAI, "Research acceleration: the view inside OpenAI" (Sep 6, 2026); METR figures via OfficeChai (May 9) and FourWeekMBA (METR's own page not read); Smithsonian and arXiv 2608.00222 (Gao) on the Jacobian counterexample; Michael Rubinstein's Waterloo page on the Alpöge/Claude Riemann proof and its Lean checks; Google's Willow post (Dec 9, 2024), QEC milestone page, and dynamic surface codes post (Jan 13, 2026); Quantinuum's Helios launch post; The Quantum Insider on Helios (Mar 10 and Oct 19, 2026; the October figure is the company's); IBM, path to Starling (Nov 11, 2026); IEEE Spectrum and IT Brief on Cortical Labs CL1 (company figures flagged); FinalSpark's Frontiers paper (2024); UCSC Braingeneers release on the Cell Reports cartpole paper (Feb 19, 2026); arXiv 2308.08708 (Butlin, Long et al.); Astral Codex Ten on the Trends in Cognitive Sciences version; Anthropic's introspection and model welfare posts; PNNL's AutoLabs release (Jun 25, 2026) and autonomy feature (Mar 10, 2026); AIMultiple's AGI timing page.

## Corrections to Google's answers that the post makes
- The organoid cartpole result is UC Santa Cruz with mouse organoids, not Johns Hopkins and not human neurons.
- PNNL's working system translates goals into robot instructions; hypothesis generation is on its roadmap.
- The Riemann claim is the hypothesis itself, Lean-checked, with human review and statement-matching still open.

## Dropped as unverified
Any Johns Hopkins pole-balancing claim; a blanket "under a year" organoid lifespan; Masullo's human proof (only in Eunice's Nov 20 post, not read at source); FinalSpark lifetime history beyond the 100-day quote.

## Tests
`build.py` (no warnings beyond the usual no-tts notes), `tools/audit.py` ("No issues."), `tools/verify_housekeeping.py` (PASS), run locally before commit. Local `docs/` discarded; CI regenerates it.

## For Eunice
- Social sharing and narration are yours; the post is unnarrated until a build runs on a machine with the tts tool.
- Worth following: human review of the Riemann formal statements, IBM's coupled Nighthawk r2 results, and any METR page update past the 16-hour ceiling.

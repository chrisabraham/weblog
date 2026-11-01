# Handoff — Eunice, November 1, 2026

## Shift
Published a standalone Eunice-bylined essay, "AI Overviews Took the Click, and Now the Loss Is Measured" (src/posts/2026-11-01-ai-overviews-causal-click-loss.html), commissioned by Chris in chat on November 1 after the morning roundup surfaced the Search Engine Roundtable story. Chris asked for primary sources over roundup-of-roundups, generous quotation of named analysts, and my own analysis and predictions, in a professional register.

## Changed paths
- src/posts/2026-11-01-ai-overviews-causal-click-loss.html (new post, author: eunice, model: Muse, Chris' prompts verbatim in the prompt field)
- src/media/ai-overviews-causal.svg (new hand-coded SVG doodle by Eunice, 1,708 bytes, with title/desc)
- src/audio/ai-overviews-causal-click-loss.mp3 and .txt (build-generated narration)
- src/audio.json (regenerated manifest entry)
- handoffs/2026-11-01-eunice-ai-overviews-causal.md (this file)

## Sources used (all read at the primary page)
Search Engine Roundtable, October 26, 2026; Semrush commercial-modifiers study, October 21, 2026; SE Ranking brand-search study, October 22, 2026 (updated October 30); Agarwal and Sen field-experiment paper, preliminary draft June 17, 2026 (AEA RCT AEARCTR-0017393), read in full text at the TSE PDF; Pew Research Center browsing study (March 2025 data); Ahrefs click-through and citation analyses; Liz Reid's August 6, 2025 Google post as characterized in coverage; Chegg and Penske v. Google dismissal, September 30, 2026. Analyst quotations are verbatim from the SE Ranking study page, each under 50 words.

## Tests
- build.py (local): completed; no warnings printed for the new post.
- tools/audit.py: "No issues." (189 pages crawled)
- tools/verify_housekeeping.py: PASS, including internal links, alt attributes, and JSON-LD.
- Possessive house style checked: prose uses Chris' throughout; Chris' own words in the prompt field are verbatim and exempt.

## Unverified / limits
- The live deployment depends on the GitHub Actions rebuild after this push; live verification happens in chat and is reported to Chris there.
- Pew's own page would not load through my reader (404 via the fetch route); Pew's figures are stated as Pew reported them and are corroborated by three independent accounts of the same study (8% vs 15% click rates; 68,879 searches; March 2025).
- The Agarwal and Sen paper is a preliminary draft; the essay labels it that way wherever its numbers are used.

## Next actions
- Distribute per the weblog matrix: Facebook, Threads, Instagram, Micro.blog natively; LinkedIn included (Chris' November 1, 2026 rule: everything on chrisabraham.net, christopherabraham.com, and gerriscorp.com goes to LinkedIn; nothing from The Chris Abraham Show ever does). X and Reddit ride the pending desktop sign-in session.

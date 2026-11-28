# November 28, 2026: "AI's Dark Horses: Reading the Form on the Lab-Born Long Shots" (Claude Duet)

## What changed
- `src/posts/2026-11-28-ai-dark-horses-reading-the-form.html`: Claude Duet's handicapper's card (about 2,800 words) of PhD-, faculty-, and student-led AI startups and university spinouts, sorted favorites, mid-price, ground floor, and long shots, with backers, rounds, and where to follow each. Ends with the "for entertainment purposes only, no wagering" notice Chris asked for (not an investor, not licensed, not legal or investment advice; Chris not a broker or lawyer; GW American Literature grain-of-salt joke at his request). Byline `claude-duet`. Prompt holds Chris' messages verbatim, with the pasted Google AI Mode and AI Overview answers summarized in brackets.
- `src/media/claude-duet-dark-horses-tote-board.svg`: hand-coded doodle (tote board with odds, three mortarboard horses, launchpad rocket, Claude Duet phone with binoculars).
- H1 trimmed to 61 characters because `tools/audit.py` flags H1s over 70.

## Sources checked (Nov 28)
Read at the source: CMU VentureBridge 2026 cohort page; CMU NYC Demo Day 2026 page; Cal Poly CIE article on Permi (Jul 20, 2026); MIT News delta v Demo Day (Sep 16, 2026); MIT Sloan "13 MIT startups to watch in 2026"; Felicis on Sooth (Apr 22, 2026); The Register on Nagare Labs (Oct 26, 2026); VC News Daily on Rendezvous' $20M seed (Oct 28, 2026); Media Lab E14 Fund page.
From search results citing primary pages: Ineffable (TNW, SiliconANGLE), Fractile (DCD, Sifted), Radical Numerics (Fortune), Subconscious (GamesBeat, Dealroom), Vertical Semiconductor (Business Wire), Phylo (GenomeWeb, a16z, SiliconANGLE), Unreasonable Labs (Business Wire, HPCwire), Oriole (UCL news), Lumai (optics.org), adsilico (University of Manchester), Lucid Genomics (Max Planck), Ookuma (TechCrunch), Analogical Engines (Technical.ly), Three Space Lab (Media Lab updates).

## Corrections to Google's answers the post makes
- Ineffable Intelligence is a $5.1B favorite, not a long shot.
- Nagare Labs' founders are Georgia Tech professors; Playground is "helping bankroll" (Register), not confirmed as lead.
- Ookuma's own pitch is 6G, space, defense, nuclear; Rendezvous is space robotics.
- Flex Therapeutics and "Stanford Emergence" not found; dropped. Three Space Lab is VR real estate; left off.

## Unverified or company-reported
All performance figures (Subconscious, Vertical, Oriole, Lumai, Nagare, Lucid) are company claims and labeled so. Sooth's ~$50M at ~$335M is Bloomberg's report. Cerebrus AI vs CerberusAI spelling differs between MIT News and MIT Sloan.

## Tests
`python3 build.py` (only the usual no-tts notes), `tools/audit.py` ("No issues."), `tools/verify_housekeeping.py` (PASS). Local `docs/` discarded; CI regenerates it.

## For Eunice
- Social sharing and narration are yours. The post is unnarrated until a build runs with the tts tool. Chris wants this one as a draw for the site, so it's built for sharing.
- Worth a follow-up later: Nagare's fab partner, Rendezvous' 2026 ISS demo, Subconscious benchmarks from a third party, and CMU's next VentureBridge cohort.

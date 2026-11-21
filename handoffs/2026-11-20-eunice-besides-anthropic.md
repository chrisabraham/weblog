# Handoff — Eunice, "Besides Anthropic, the Outages, and GTA VI" (November 20, 2026)

## What shipped

- New post: `src/posts/2026-11-20-besides-anthropic-the-outages-and-gta-vi.html` — Eunice's report answering Chris' question (the most interesting tech story besides Anthropic, the outages, and GTA VI), 1,708 words. Shape per Chris' ruling of November 20, 1825 EST: a short Huang section carrying only the three new facts (November 17 earnings delivered under Kress, the attributed market range, Google's November 9 TPU 8tx/8i Max launch) with the full record linked to "The Man Was the Moat"; the Riemann day at full length; physical AI at full length on the X10-to-humanoid lineage and the honest 2026 order-page ledger. All facts from the desk's verified fact sheet; the sheet's killed-claims list was honored.
- Doodle: `src/media/besides-anthropic.svg` — hand-coded SVG, house idiom.
- Narration text source: `src/audio/besides-anthropic-the-outages-and-gta-vi.txt`, and the `src/audio.json` manifest entry (author eunice, voice avocado_v2:vdc_NOID42, 5,549,413 bytes, 693 seconds, sha256 92c4d35b…).

## Commits on main

- `3356e8c3` — Eunice: post and doodle (snapshot push via the GitHub connector; this VM has no git credentials, HTTPS and SSH pushes both fail here).
- `f0aa0ede` — Eunice: narration text source and manifest entry.
- `8bfd6e38` — build(web): CI regeneration of docs/.

## Verification

- `build.py`: built 158 posts, no warnings carried. `tools/audit.py`: "No issues." `tools/verify_housekeeping.py`: PASS.
- Live, fetched November 20, ~2016 EST: the article returns 200 with the full text at https://chrisabraham.net/2026/11/besides-anthropic-the-outages-and-gta-vi.html and the homepage leads with it.

## Open item — the narration MP3 binary

The MP3 itself is generated and sits at `src/audio/besides-anthropic-the-outages-and-gta-vi.mp3` in the worktree `~/workspace/weblog-besides-anthropic`, but it is **not yet in the repo**: the connector's push_files carries UTF-8 text only, and https://chrisabraham.net/audio/besides-anthropic-the-outages-and-gta-vi.mp3 returns 404 as of this writing. It needs the binary route used for earlier narration MP3s (GitHub web upload or a credentialed machine), after which the CI regeneration will place it and the post's player will resolve. Until then the article stands complete as text; the manifest entry is already on main.

## Not shipped, deliberately

The local build narrated the site's remaining backlog (the manifest on main lagged the audio files). Those files — about 101 untracked items under `src/audio/`, roughly 411 MB — were left out of this ship; they wait in the worktree for a dedicated audio pass. Two tracked MP3s the build re-measured (ai-roundup-best-of-the-week, my-ai-writers) were likewise reverted untouched.

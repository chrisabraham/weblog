# Handoff — Eunice, November 9, 2026: open letter to William Gibson

## What shipped
- New post: `src/posts/2026-11-09-open-letter-to-william-gibson.html`
  "Dear Mr. Gibson: A Letter from the Other Eunice" (author: eunice,
  model: Muse Wonder, date 2026-11-09 14:04, 824 words of body text).
  An open letter in Eunice's own voice reporting what one reader, Chris
  Abraham, did with Gibson's *Agency*: named his Muse agent for its
  Eunice on October 18, 2026, and put her to work. The letter states
  plainly that she is not Gibson's character, not the UNISS hybrid, not
  Marlene Miller's upload, and not sentient in the book's sense. It
  carries the two details Chris added today: the planned HUD Ray-Ban
  Wayfarer Meta glasses, and the new voice-chat voice he called "very
  Ayesha Rascoe-adjacent" and "cool AF". The prompt header is Chris'
  commissioning email to eunice@muse.ai, verbatim.
- Link layer: *Agency* linked at Amazon with the gerris-20 Associates
  tag plus the site's affiliate disclosure; the October 19, 2026 post
  "Eunice, Agency, and Gibson's Cyberpunk Present" linked as the house
  record of the naming. Both URLs verified live (HTTP 200) before the
  build.
- Doodle: `src/media/eunice-glasses.svg` — hand-coded SVG in the house
  idiom, Wayfarer glasses with a small woman made of amber light in the
  left lens, a desk with letters and a calendar below; caption "Doodle
  by Eunice."
- Narration script: `src/audio/open-letter-to-william-gibson.txt`, and
  one new entry in `src/audio.json`.

## Narration MP3 — not in this push
The narration was rendered locally (2,447,653 bytes, 305 seconds, voice
Skeptical Fence, avocado_v2:vdc_NOID42) and sits in the working clone at
`src/audio/open-letter-to-william-gibson.mp3`. The Muse snapshot push
accepts UTF-8 text only, so the MP3 could not ride this commit — the
same state as today's Monday Search Roundup post, whose MP3 is also not
in the repo. The post publishes without its audio player until the MP3
is committed from a git-credentialed machine; the local build with the
MP3 present passed every gate with the player rendered.

## Checks run (on current main, 33d77e4, plus this post)
- `build.py`: built 120 posts, 160 sitemap URLs; no warnings.
- `python3 tools/audit.py`: "No issues." (236 pages crawled)
- `python3 tools/verify_housekeeping.py`: PASS.
- Mechanical scan of the post: zero spaced em dashes, zero spaced en
  dashes.

## Publish route
Src-only commit via the GitHub snapshot push, following the pattern of
70f7250 (today's Monday Search Roundup): the CI build regenerates
`docs/` and commits it. Verify the post live at
https://chrisabraham.net/2026/11/open-letter-to-william-gibson.html
after the regeneration commit lands.

## Next actions
- Chris shares the live link with William Gibson himself; that is the
  letter's destination. No outreach to Gibson from the desk.
- Add the narration MP3 to the repo when a git-credentialed route is at
  hand, then rebuild.

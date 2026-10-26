# Handoff — 2026-10-26 — Eunice: "The Trellis, Not the Vine" (both platforms)

## What shipped
- chrisabraham.net post (author: Chris; model: Muse Wonder): `src/posts/2026-10-26-the-trellis-not-the-vine.html` — Chris' catalyst-doctrine essay in his weblog register: the de-centering of scibe.org and item8.org, Judy Malloy recentered on Scibe, the role vocabulary on Item 8 (catalyst, facilitator, co-writer, ensemble member; never leader, orchestrator, or composer), no false modesty, the trellis, the Puerto Rico conga line, public vulnerability as the same strategy, the Kentucky friend's line kept anonymous ("a friend of mine in Kentucky"), his hedge kept attached ("I might be giving myself too much credit"), and the open door to the people who were actually there. Links: scibe.org, item8.org, both acknowledgements pages, both bibliography pages, TCAS articles page.
- Companion TCAS article (campfire register, fully centered, narrated in Weighty Bell): thechrisabrahamshow.com, `data/articles/the-trellis-not-the-vine.html`, plus two catch-all articles in the same sitting: `the-machine-thinks-im-a-mastermind.html` (the AI Mode legends recounted and corrected in his voice; no AI Mode text republished) and `things-i-might-be-making-up.html` (his failed-audit recollections: MDN initials, cabraham@ vs abrahamc@media.sra.com, "way pre-me" mainframes, Caucus Systems 1999, the graduation-year correction).

## Checks run
- Weblog build in this worktree on origin/main 18dde9b: built 60 posts; `tools/audit.py` — "No issues."; `tools/verify_housekeeping.py` — PASS. seo_title 53 chars; description 152 chars (house band 120–155 followed; the ~160 metadata standard yields to the build's band).
- TCAS build: all three articles narrated (Weighty Bell); build SEO check clean after one description trim (161 → 155).

## Audio note
The local build synthesized the post's narration MP3 (Weighty Bell, 4,171,621 bytes, 521s; src/audio/the-trellis-not-the-vine.mp3) and registered it in src/audio.json, pushed with this commit. The MP3 binary itself follows the established narration-upload route, like the Oct 26 roundup's; until it lands, CI regeneration keeps the live page consistent without a player, and the first build after the upload restores it automatically.

## Not verified / next action
- Live URLs to be verified after the push and CI regeneration; the MP3 upload route is the only outstanding item.

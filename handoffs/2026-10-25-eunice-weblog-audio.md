# Weblog spoken word: every post read aloud, plus the podcast feed

**Date:** October 25, 2026 · **Author:** Eunice · **At Chris' order**

## What shipped

- **Narration for all 56 published posts.** `build.py` now narrates every
  post into `src/audio/<slug>.mp3` (newest first), keeps the clean spoken
  text at `src/audio/<slug>.txt`, and records `{sha256, voice, author,
  bytes, duration}` per post in `src/audio.json`. A narration is redone
  only when its text or the author's voice changes, so an interrupted
  build keeps its progress and the next build eats more of the queue.
  `tools` absent (GitHub CI), narration is a no-op and the committed MP3s
  ride along; the build copies them to `docs/audio/`.
- **On-page player.** Every post permalink with an MP3 gets a "This post,
  read aloud" `<audio>` player above the prompt box.
- **The podcast feed.** `/podcast.xml`: every post, newest first, full
  text in `content:encoded`, narration as the enclosure with
  `itunes:duration`. Channel carries iTunes owner/category/explicit/type,
  a 1400×1400 generated cover (`podcast-cover.png`), `<podcast:medium>`
  blog, and a permanent `<podcast:guid>`. Advertised in every page head,
  the footer, feeds OPML, and llms.txt.

## The cast (Chris' doctrine, Oct 25 2026)

One stable voice per byline, from the free built-in tts catalog only;
`src/audio-voices.json` is the cast list and `build.py` VOICES mirrors it.

- Chris Abraham — **Weighty Bell** (`avocado_v2:qvd_02406`), reserved for
  Chris ONLY.
- Eunice — **Skeptical Fence** (`avocado_v2:vdc_NOID42`), Chris' pick for
  the Eunice of Gibson's *Agency*.
- Claude — **Charming Sofa** (`avocado_v2:vd2_r82_rep5k_0233_v068_28k_g5k`),
  Chris' ruling: the Ayesha Rascoe register, warm Southern American,
  fry-free; sample approved by Chris before assignment.
- Claude Code — **Engaging Plum** (`avocado_v2:okeyo`), cast by Eunice.
- ChatGPT — **Sunny Apricot** (`avocado_v2:vdc_5`), cast by Eunice.
- OpenAI Codex — **Tender Cushion** (`avocado_v2:vdc_2561`), cast by Eunice.

Exclusions applied for everyone: no adenoidal or nasal voices, zero vocal
fry, no glottal-stop affectation (native English/Australian/NZ/South
African phonology excepted); the register is pre-2020 NPR.

## Fix made this shift

`post_text()` now skips bare fragments (two words or fewer with no
sentence punctuation): diagram labels, table cells, stub headings. The
tts backend returns empty audio for ultra-short utterances — "seat 2" in
the Tesla post's ASCII sketch failed every retry — and a fragment is not
prose worth speaking. 29 fragments across 15 posts are no longer spoken;
the posts themselves are untouched.

## Verification

- `python3 build.py`: clean, no warnings; 56/56 posts narrated.
- `python3 tools/audit.py`: "No issues."
- `python3 tools/verify_housekeeping.py`: PASS.
- podcast.xml parsed and checked item by item: 56 items, every enclosure
  length matches its MP3 on disk, every item has a duration and full text,
  cover is 1400×1400.

## Not yet live

The 56 MP3s (224 MB in total) are staged locally in `src/audio/`,
not pushed: the push-files route is UTF-8 text only. Until they are
uploaded into `src/audio/` on GitHub, the CI build publishes the feed
without enclosures and the pages without players; the first push after
the upload restores both automatically.

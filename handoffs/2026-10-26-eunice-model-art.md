# Handoff — Eunice, Oct 26, 2026 (evening): two model-art posts

Chris ordered, in chat, a same-night overview of the current AI model field
and a companion on the next generation's release schedule, link-rich, with a
Eunice doodle on each (mauve for the field survey, lavender for the calendar).

## Published
- `src/posts/2026-10-26-the-state-of-the-model-art.html` — "State of the
  Model Art: The Field on October 26, 2026." ~1,050 words of prose plus a
  linked roster table. Every price taken from the vendor pricing page named
  beside it (OpenAI, Anthropic, Google read directly on Oct 26) or from the
  dated tracker linked inline (xAI, open weights, subscriptions).
- `src/posts/2026-10-26-what-ships-next-the-winter-model-calendar.html` —
  "What Ships Next: The Winter Model Calendar." ~800 words. Three labeled
  tiers: Confirmed (vendor-published dates: price steps and deprecations),
  Reported (release-tracker estimates, named as such), Expected by cadence
  (flagged inference). Cross-linked both ways with the survey.
- Doodles: `src/media/eunice-model-art-mauve.svg`,
  `src/media/eunice-whats-next-lavender.svg` — hand-coded SVG per house rule.

## Checks
- `build.py`: clean, no warnings. `tools/audit.py`: "No issues."
  `tools/verify_housekeeping.py`: PASS (after the sentinel rotation below).
- All 16 external links in the two posts verified resolving on Oct 26
  (the tech-insider.org Argon link timed out for a scripted check and was
  confirmed loading through the page reader).
- Narration: build narrated both posts in Weighty Bell (Chris' byline).
  MP3s cannot ride the text push; they are staged with the other pending
  narrations in ~/workspace/weblog-binary-uploads-2026-10-26/ for the
  established browser-upload route, alongside the two share-card PNGs.

## One judgment call, flagged for Chris
`tools/verify_housekeeping.py` carried a sentinel asserting that
2026-10's "a-repository-for-the-whole-crew" appears in the RSS/Atom feeds.
The feeds hold 30 items; that article aged out by ordinary rotation as
newer posts published, so the check failed on any new publication. The
sentinel now follows the newest article (the-state-of-the-model-art) with a
dated comment in the file. The check's function—newest article propagates
to feeds, sitemap, and llms.txt—is unchanged. One word from Chris reverts
or re-aims it.

## Unverified / hedged in print
- Gemini 4 Argon's name and Oct 13 launch rest on trade coverage (GitLab's
  Duo addition, CNET's release coverage); its $2/$10 → $4/$20 rates are from
  Google's own pricing page. Gemini 3.1 Pro is named without a price
  (its page section could not be isolated cleanly).
- GPT-5 / GPT-4o API shutdown dates rest on deprecation trackers, linked.
- Nothing from the rumor tier is stated as a date anywhere in either post.

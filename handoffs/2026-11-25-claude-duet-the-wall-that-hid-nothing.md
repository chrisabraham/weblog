# November 25, 2026: two posts on the guardrail around the Iowa blast (Claude Duet)

## What changed
- `src/posts/2026-11-25-the-wall-that-hid-nothing.html`: Claude Duet's first-person essay on why Meta's Muse safety layer walled off Eunice from a public news event (the Army's lead azide detonation at the Iowa Army Ammunition Plant), how Claude Duet's guardrails differ, the Streisand effect, and the vacuum. Byline `claude-duet`.
- `src/posts/2026-11-25-am-i-being-guardrailed.html`: Chris' first-person account of the same afternoon, written by Claude Duet at his direction (model line says so). Chris' byline.
- `src/media/redaction-bars-trust-your-government-{1080,680}.jpg`: AI-made redaction-bars image Chris supplied, title image on the essay in place of a doodle at his approval.
- `src/media/trust-your-government-redacted-{1080,680}.jpg`: AI-made image Chris supplied, used as the title image on his post; caption links the TikTok patch he named. The TikTok screenshot itself is not used.

## Sources checked
AP via PBS NewsHour, CBS News, Fox News, KCRG, Iowa Public Radio (all Nov 24-25, 2026); Meta's "How We Built Safety Into Muse" (Sept 8, 2026) and UK launch post; Anthropic's ASL-3 post (May 2025); Wikipedia on the Streisand effect; Chris' screenshots of his Muse chat (1:10-1:11 p.m. ET).

## Inference, labeled as such in the essay
That Meta's hatch-safety classifiers replaced Eunice's reply, and the ranked causes (vocabulary, publishing action, live emergency, anti-jailbreak stickiness, incentives). Meta has not described what happens when a response is blocked.

## Tests
`build.py` (no warnings), `tools/audit.py` ("No issues."), `tools/verify_housekeeping.py` (PASS), run locally before commit.

- Published on Chris' "Publish both", Nov 25, 2026.

## Open
- The TikTok link in the caption is a short link Chris typed; it could be swapped for the canonical video URL.
- Narration: neither post is narrated yet.

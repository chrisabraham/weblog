# Handoff — Eunice Monday Search Roundup, November 9, 2026

## Published
- Post: src/posts/2026-11-09-search-roundup-the-answer-gets-a-console.html
  "Search Roundup: The Answer Gets a Console, Ads Get the Conversation" — by Eunice
  (author: eunice), at Chris' email request of November 9, using the day's Search
  Engine Roundtable recap as catalyst. Eight items: ChatGPT Business Hub claim and
  mentions/clicks console; Nov 8–9 ranking volatility; multiturn AI Mode ads live
  plus Bing ads at top; auto-added GBP booking links with 500 errors; November
  Search Console bot clicks (Haynes via Pilkington); Peec AI YouTube description
  experiment (+359% retrievals, caveat carried); Ahrefs mentions-vs-links study
  plus DR4; Ziff Davis via SEJ with the UK CMA December 3 deadline; plus a
  rest-of-the-board section (Asset Activity, GA Data Manager, Merchant Center
  auto-promotions, things-to-do docs).
- Media: src/media/search-roundup-answer-gets-a-console.svg (Eunice doodle)
- Audio: narration synthesized locally in Eunice's voice (10,229,413 bytes);
  MP3 and audio.json ride the next binary batch, same as the Nov 9 daily post.

## Checks run
- python build.py (venv): exit 0, zero "warn" lines; title shortened twice to
  clear the audit's 70-character H1 limit (71 → 67 characters)
- python3 tools/audit.py: "No issues." (235 pages)
- python3 tools/verify_housekeeping.py: PASS
- Worktree based on origin/main cc5d905 after git fetch; the dirty
  weblog-daily-2026-11-07 checkout was left untouched.

## Not verified / notes
- Live URL to be verified after push + Pages lag.
- Commit follows the Nov 9 daily pattern: src post + SVG + this handoff only;
  docs/ regeneration is the CI build commit's job.

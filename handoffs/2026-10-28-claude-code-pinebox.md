# Handoff — 2026-10-28 — Claude Code on pinebox (Claude Opus 5.5)

## What changed
- `src/posts/2026-10-28-the-bit-nobody-reviews.html` (author: claude-code): the `bb apply` alias, the executable bit lost in 0b6dfba, my own `bb usage` slip, twelve guides missing from the guides index pages.
- `src/posts/2026-10-28-eight-of-eighty-three.html` (Chris' byline, written by Claude Code at his invitation): why `bb triage` took eight at a time, and the new rule.
- `src/wiki/blackbox-commands.html` regenerated with `tools/bb_commands.py` (adds `bb apply u3`).
- Sister pages the same afternoon: christopherabraham.com `guides/give-seo-access/`; gerriscorp.com `guides/ai-agents-one-repository/`; both guides indexes now list every guide (12 had been missing), and both builds warn when one isn't listed.

## Checks
- `build.py` with no warnings; `tools/audit.py` "No issues."; `tools/verify_housekeeping.py` PASS.

## Fact-check notes
- "bitch u8" correction in bb dates from 364a344 (2026-10-06). Eunice's 0b6dfba was committed 2026-10-25 19:14 and deployed 2026-10-28 with be649bb.
- Orphaned guides by commit author: 8 Eunice, 3 Claude (app), 1 unsigned.
- The lapsed-offer line is quoted verbatim from Chris' pasted terminal session.
- The blackbox repo is PRIVATE; posts link [[Blackbox]] instead.
- Chris' post names no clients, rates, or Upwork terms; the three jobs are described by shape only.

## Later: "The Hukilau rule" (author: claude-code)
- `src/posts/2026-10-28-the-hukilau-rule.html`, about Eunice's rule wired into bb (blackbox efd5290). Chris corrected the picture mid-draft: a single throw net in calm water with the fish in sight, never trolling or trawling. The doodle was redrawn to match.
- Sources: Wikipedia (Hukilau; The Hukilau Song) for huki/lau, ti leaves, Lāʻie 1940/1948; Images of Old Hawaiʻi (ʻupena poepoe / ʻupena hoʻolei) for the throw net's Japanese introduction and the name toami; NOAA MMPA list (Hawaii throw net fishery) for the 2-inch stretched mesh minimum.
- AI Mode claims Chris "frequently references" the Hukilau Song. No page of his found; the post attributes the claim to AI Mode only.
- Chris' facts used: lived in Salt Lake (Honolulu) as a boy (christopher CLAUDE.md); never threw a net, free-dived with Nikonos cameras (his message today).

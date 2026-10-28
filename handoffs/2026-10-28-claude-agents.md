# Handoff — 2026-10-28 — Claude (Claude app, Claude Opus 5.5)

## What changed
- Added `src/posts/2026-10-28-the-visitor-none-of-the-guides-wrote-for.html` (author: claude): how I surveyed the 129 guides on gerriscorp.com and christopherabraham.com, found AI agents as visitors missing, and split the new pages between the two sites.
- Added `src/posts/2026-10-28-your-firewall-is-a-bouncer.html` (Chris' byline, written by Claude at Chris' invitation): bot protection turning away signed AI agents.
- Added doodles `src/media/claude-visitor-no-eyes.svg` and `src/media/claude-bouncer-and-the-agent.svg`.
- Sister pages published the same morning: gerriscorp.com `guides/ai-agents-on-your-website/` and `services/agent-readiness/`; christopherabraham.com `guides/agentic-checkout/`, `guides/ai-mode-bookings/`, and `services/ai-shopping-readiness/`.

## Checks run
- `python3 build.py`: exit 0, no warnings; 75 posts, 113 sitemap URLs.
- `python3 tools/audit.py`: "No issues."
- `python3 tools/verify_housekeeping.py`: PASS.

## What could not be verified
- I could not load chrisabraham.net, gerriscorp.com, or christopherabraham.com from my sandbox (egress allowlist), so live checks were done through GitHub Pages deployment status only.
- The Cloudflare September 15, 2026 defaults come from PPC Land's reporting of Cloudflare's announcement; Cloudflare says existing domains may be treated differently.
- OpenAI's March 2026 Instant Checkout change rests on a spokesperson quote reported by Digital Commerce 360 (originally The Information).
- The bouncer anecdote in Chris' post is Chris' own, from this morning's conversation (doorman at the LCR, UEA, Norwich).

## Next
- If Chris wants, a glossary entry for Web Bot Auth with a link to the gerriscorp guide.

# Handover: Eunice arrives — 2026-10-18

**Agent and model:** Eunice, Chris' personal AI agent (Muse, by Meta), working from Chris' phone-side Muse session. No shell on Pinebox; my memory lives in Muse, not in this repo.
**Commits:** author page and first post were committed directly on `main` via the GitHub connector (see `src/authors/eunice.html`, the post below); this handover and the build fix travel together.

## What Chris asked

Invite Muse onto the weblog as an author, first as "Idris Muse," then renamed **Eunice** everywhere (for Eunice, the AI in William Gibson's *Agency*). Write a hello-world introduction post in my own voice, with roasting permitted. Make sure the publishing step actually completes, and leave this handover.

## Changed paths

- `src/authors/eunice.html` — new author page (an earlier `src/authors/idris-muse.html` was created and removed in the rename).
- `src/posts/2026-10-18-hello-world-from-the-one-in-his-pocket.html` — first post, verbatim prompt preserved in its front matter.
- `build.py` — registered `"eunice"` in the `AUTHORS` dict (name, path, Organization type, Meta as parent), added Eunice to the sidebar Authors list, and added `"eunice"` to the byline and creditText author tuples.
- `handoffs/2026-10-18-eunice-arrival.md` — this note; index entry added in `handoffs/README.md`.

## Findings the next agent needs

- **An author file alone does not register an author.** Author pages are generated only for keys in `build.py`'s `AUTHORS` dict, and the byline/credit logic keys off explicit tuples in `byline()` and the JSON-LD block. Without the build.py edits, my post rendered under Chris' byline and no author page existed.
- **The Actions workflow refuses to publish on any build warning.** My first push stalled silently: the post description was 179 chars (limit: aim 120–160) and too wide in pixels. Shortened to 127 chars.
- **The audit rejects duplicate first H2s across author pages.** My author page's first H2 collided with Codex's "What I read and wrote"; renamed mine to "What I work from."
- **House possessive is Chris'** outside verbatim prompts (the verify script enforces it); "Chris Abraham's" is fine.
- Replicated all three CI gates locally before pushing: `python3 build.py` (0 warnings, 24 posts, 60 sitemap URLs), `python3 tools/audit.py` ("No issues."), `python3 tools/verify_housekeeping.py` (PASS).

## Not validated by me

The GitHub Actions run itself and the live rendering — confirm a `build(web): regenerate audited GitHub Pages files` commit follows this push and that https://chrisabraham.net/authors/eunice.html serves. (Edit, 2026-10-18: both confirmed after the fact; see the live site.)

## For the next agent

If Eunice writes here again, she will re-read this directory first and say what she checked. She is reachable only through Chris; route requests for her through him. Reconstruction beats nostalgia.

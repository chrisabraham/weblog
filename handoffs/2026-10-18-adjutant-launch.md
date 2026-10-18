# October 18, 2026: Adjutant starts, ahead of schedule

**Author:** Eunice (Muse, Meta), Chris' personal agent.
**Request (Chris, verbatim in spirit):** implement Adjutant now instead of waiting a few more weeks. He linked the projects page anchor and confirmed the spelling A-D-J-U-T-A-N-T, and noted for the record that the name was coined by one of the chatbots, not by him, which he loves.

## Changed paths
- `src/site.json` — Adjutant project entry: status planned → active, started "not yet" → October 2026, url set to https://github.com/chrisabraham/adjutant, about text rewritten to say the scrub has begun.
- `src/wiki/adjutant.html` — status "Release in progress, started October 18, 2026"; name infobox now credits the AI coinage (earlier candidates Minutes, Aide, Secretary kept as history); opening paragraph updated; `updated:` set to 2026-10-18; description shortened to pass the width check.
- `src/glossary.json` — Adjutant definition updated from "proposed" to the release in progress, with the name origin noted (definition kept well under 500 characters).
- `handoffs/README.md` — index entry for this note.
- `handoffs/2026-10-18-adjutant-launch.md` — this note.

## Tests
- `python3 build.py` — 0 warnings, 24 posts, 60 sitemap URLs (first pass warned the wiki description was 180 chars and too wide; shortened twice until clean).
- `python3 tools/audit.py` — "No issues."
- `python3 tools/verify_housekeeping.py` — PASS.

## What could not be validated / open items
- The public repository does not exist yet. The GitHub integration Eunice uses can read and write files but returned 403 ("Resource not accessible by integration") on repository creation, and no authenticated `gh` CLI is available in her environment. Chris creates the empty public repo `adjutant` himself; until he does, the projects page link to it returns 404. This was his informed trade-off for launching today.
- No Blackbox code has been copied anywhere. The scrub pass (names, clients, paths, secrets, private config) has not started; the wiki's own plan stands: separate public repo with fresh history, personal material moved into private configuration first, and a release script that refuses to publish on finding client names, personal paths, or secrets. Nothing ships before that gate exists.
- License is MIT, "as is," per the wiki infobox (recorded there before today).

## Next agent
1. Once Chris confirms the repo exists, add README.md and LICENSE (MIT) as the first commit, then verify the projects page link resolves.
2. Run the Blackbox scrub inventory before touching code: `config/` first, then `bb` and `bblib/`, searching for names, client identifiers, absolute paths, and anything secret-shaped.
3. Do not flip the private blackbox repo public; Adjutant is a fresh export, always.

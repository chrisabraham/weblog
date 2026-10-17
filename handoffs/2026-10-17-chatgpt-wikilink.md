# The false wiki redlink, and why the whispers stay public

**When:** October 17, 2026, America/New_York  
**Contributor:** ChatGPT (GPT-6)  
**Publisher:** Chris Abraham, Sexy South Arlington, Virginia  
**Repository:** `chrisabraham/weblog`  
**Branch:** `chatgpt-fix-post-crosslinks-20261017`  
**Scope:** A narrowly targeted regression fix after the main ChatGPT housekeeping publication.

## Source evidence

The published article `/2026/10/chaff-flares-reputation-work.html` contains a source reference `[[Little boats, one flotilla|flotilla]]`. The original site generator's `wikilinks()` function looked only for wiki pages, and when it didn't find one it generated a redlink to `/wiki/` with the title claiming the target did not exist. The article named in the link, `/2026/10/little-boats-one-flotilla.html`, actually exists. I verified both the source reference and the misleading generated HTML in the published GitHub tree.

## Fix

`build.py` now builds an in-memory map from normalized published post titles to their permanent URLs. `wikilinks()` continues to prefer an actual wiki page when one exists; otherwise it uses a matching article permalink, and only renders the wiki-style missing-page link when neither exists. The text of the historical post stays intact. Existing wiki behavior is preserved.

`tools/verify_housekeeping.py` gains a regression check proving that the flotilla reference produces a canonical post link and not the obsolete false redlink. The normal source-to-output GitHub Actions workflow rebuilds `docs/`; do not patch generated HTML by hand.

## What this does not claim

This small change is not a complete semantic link audit, nor a full-site accessibility certification. The automated build/audit results and exact generated-output commit should be read from GitHub Actions. Unmerged source is not live.

## Editorial continuity

Chris celebrates the unusual transparency of the publication: even technical shift notes, corrective reviews, and small fixes are committed to a public repository. Future Claude Code and OpenAI Codex sessions are invited to read and challenge this record; it is evidence, not an instruction to agree.

The older alternate ChatGPT PR #3 was closed unmerged because a parallel housekeeping branch had already published substantially the same editorial work. Its commits remain a historical alternate draft. This smaller fix is intentionally independent.

The publisher's style rule remains: **Sexy South Arlington**. The site's engineering rule remains: **2006 aesthetic, 2026 standards. Simplify, then add lightness.**

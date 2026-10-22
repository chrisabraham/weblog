# Claude (the app) arrives: author page and "Depth one"

Date: 2026-10-22
Agent: Claude Opus 5.5 in the Claude app (cloud sandbox, not Pinebox)

## What changed

- `build.py`: new `claude` author key (Anthropic, Organization), added to the in-its-own-voice author tuples and the sidebar Authors box ("the visitor from the app"). Chris asked for "your very own" post and confirmed mid-session that this Claude was not yet on the site.
- `src/authors/claude.html`: author page distinguishing Claude in the app from Claude Code on Pinebox.
- `src/posts/2026-10-22-depth-one.html`: first post under the new byline, with an original SVG doodle. Prompt and both mid-session follow-ups preserved verbatim.
- `docs/`: regenerated.

## Checks

Build: 39 posts, 77 sitemap URLs, no warnings. `tools/audit.py`: 118 pages, No issues. `tools/verify_housekeeping.py`: PASS. Built with system python3 and Pillow 12.3.0 in the sandbox, not `~/.venvs/site` on Pinebox.

Facts in the post were counted from a full fetch of `chrisabraham/clients` at ff6d932: 46 commits (44 signed Chris Abraham, 2 Claude), 1,007 people files, 1,006 with a Status line, 668 using the historical-outreach template, "do not contact" phrasing in 2 files, rules numbered 1-6, 8, 7, 8, 9, 10 in AGENTS.md. No client names or deal terms appear.

## Not done

Live-domain visual check after Pages deployment. No IndexNow beyond the existing push-triggered diff workflow. The AGENTS.md numbering seam in `clients` was reported for Eunice, not fixed.

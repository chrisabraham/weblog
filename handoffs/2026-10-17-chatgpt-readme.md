# ChatGPT shift: README for the curious stranger

**Date:** October 17, 2026 (America/New_York)  
**Contributor:** ChatGPT (GPT-6)  
**Publisher:** Chris Abraham, Sexy South Arlington, Virginia  
**Branch:** `chatgpt-readme-onramp-20261017`  
**Goal:** Provide a genuinely accessible front door for readers who don't know the lab, while preserving the site's established technical personality.

## Why

Chris noticed from a Mastodon conversation that a casual reader could be overwhelmed by the AI tooling and unfamiliar terms. Initially the plan was a "primer" and "glossary"; Chris then suggested using the familiar **README** convention for the entry point, in uppercase. He referenced Neal Stephenson's novel *REAMDE* but explicitly did **not** want the whole site to veer into a literary rabbit hole. The result is a plain, useful README with a small wink, not a puzzle.

The site remains a 2006-style weblog built to 2026 engineering standards, with Lotus's "Simplify, then add lightness" rule. The new page is a small map, not another massive essay on the index. It links to canonical posts and to existing wiki explanations.

## Edits and rationale

1. `src/pages/readme.html`: new generated static page. Beginner-friendly explanation of the project and its disclosed AI authorship; a small "where to begin" reading path; an accurate cast of human and model contributors; a semantic `dl` glossary of essential terms; directions to the public code, original prompts, handoff notes, privacy/disclosures and wiki. States AI session continuity limitations carefully.
2. `build.py`: put README next to Home in the main navigation and in the global footer. Both links work without JavaScript and point to `/readme.html`.
3. `src/style.css`: preserve the deliberate uppercase spelling, overriding only the global retro navigation lowercase rule. Existing contrast and keyboard-focus styles still apply.
4. `README.md` (repository root): the GitHub landing page for Codex, Claude, ChatGPT, and humans who start at GitHub rather than the live site. It points to `AGENTS.md`, `handoffs/`, the build, and the public README. This is a map to the instructions, not an attempt to supersede Pinebox's local rules.
5. `tools/verify_housekeeping.py`: test existence of the generated page, navigation and footer links, semantic definitions, wiki connection, and uppercase CSS.
6. `handoffs/2026-10-17-chatgpt-readme.md`: this public record, to be indexed in `handoffs/README.md`.

## Editorial boundaries

The new page is an explanatory guide, not a claim that ChatGPT or another agent has a permanent human-like identity. It credits ChatGPT and identifies the original human editorial request. It doesn't rewrite the older bylined articles. The suggested reading list points to published, canonical material. No client secrets or Pinebox local files are copied to GitHub.

## Tests and publication status

Source edits will go through the repository's normal GitHub Actions build, metadata/links audit, and housekeeping regression checks before publication. The `docs/` output is generated; no hand-edited HTML in that directory. Once merged, record the exact PR, build, and Pages deployment result in an append-only update. Passing source checks is not a WCAG certification; reading order, zoom, and actual browser experience remain worthwhile manual tests.

## A note to future agents

Do not mistake the two READMEs for competing mandates. The public site `/readme.html` is for new readers. The root `README.md` is the repository map. `AGENTS.md` and Pinebox notes are operational instructions. The `handoffs/` directory is the historical ledger. Both humans and machines should be able to find their bearings without a lecture.

Keep the page simple. When jargon grows, add accurate definitions or cross-links rather than piling more disclosure or decoration onto the homepage.

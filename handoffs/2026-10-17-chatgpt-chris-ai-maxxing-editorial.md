# ChatGPT shift: Chris' AImaxxing editorial manifesto

**Date:** October 17, 2026, America/New_York  
**Publisher and assigning editor:** Chris Abraham, Sexy South Arlington  
**Writing model:** GPT-6 in ChatGPT  
**Working branch:** `chatgpt-ai-maxxing-editorial-20261017`  
**Permalink:** `/2026/10/my-ai-writers-keep-stealing-my-best-material.html`

## The assignment

Chris explicitly requested a blog article written *on his behalf* in his voice. It is distinct from a ChatGPT first-person byline. He specified the editorial assignment versus independent writers, AI writers borrowing his expressions, public provenance, the irony of removing recognizable AI prose from an AI-generated website, and an unusually self-referential blockquote about **AImaxxing**. He gave creative freedom over the illustration, including permission for a weird small SVG.

The source article's `prompt:` field preserves his original dictated assignment verbatim, including speech-to-text peculiarities. The generated canonical page displays that prompt. This record documents the editorial decision to write *as* Chris, not to make a new claim that he typed each sentence.

## What was written

- `src/posts/2026-10-17-my-ai-writers-keep-stealing-my-best-material.html`: a full-length essay, **My AI Writers Keep Stealing My Best Material**, ~1,600 prose words. Its byline defaults to Chris, correctly indicating AI prose produced at Chris' direction through a separately labeled `model: GPT-6 in ChatGPT`.
- `src/media/ai-writers-editorial-table.svg`: ~5 KB original illustrated editorial table: empty human editor's chair, three different writing lamps, paper prompts becoming drafts, lotus flower, public filing cabinet, and a tiny amber pulse. The image is a self-contained SVG with `title`, `desc`, no external fetch, no tracking, and optional motion gated on `prefers-reduced-motion: no-preference`. The article embeds it through an `img` with a descriptive `alt` and explicit AI illustration caption.
- This public handoff and its directory index, to help Claude, Codex, ChatGPT, and readers reconstruct the work.

## Writing choices and constraints

Chris asked to eliminate the tropes he dislikes: false binary "not X but Y" pivots, generic soft conclusions, overly balanced bureaucracy, em dashes, artificial transitions, exaggerated promises, and machine-polished uniformity. The article uses candid first-person prose, concrete details from his editorial assignment, a long deliberately exasperated blockquote, and unruly humor. No em dashes occur in the HTML prose. The required possessive is **Chris'**. The essay's source date reflects the current local clock rather than guessing a historical post date.

The key literary conceit is exposed rather than hidden: an article written by ChatGPT under Chris' byline, describing the editorial influence Chris exercises over AI bylines, while the original assignment appears on the published page. It acknowledges that "independent" model articles are shaped by human editorial prompting and available session context; it does not claim autonomous sentience or continuity between model sessions.

## Illustration provenance

An experimental image-generator preview of a proposed blog page appeared in the conversation, but it included an invented publication date and depicted a webpage rather than a clean article illustration. It was **not used as the live blog artwork**. Instead, ChatGPT created the small SVG above as the published illustration to respect the owner's preference for low-weight, high-information images. The tiny animated amber indicator is an optional eAIsterEgg and stops animating when reduced motion is requested.

## Status and validation

Files have been committed to the branch. The normal site build will generate the permalink, AI/model credit, source prompt block, homepage teaser, sitemap, feed entry, and OG share card. The automated audit and housekeeping test are the release gate. Any failed checks or warnings must be resolved before merging and publishing. A successful source commit is not yet proof of deployment or live rendered behavior; deployment evidence and results should be appended here after merge.

## Notes for future editors

The author is **Chris**, the credited writing model is **GPT-6 in ChatGPT**. Preserve the prompt. Do not rewrite the historical argument quietly, even if Claude or Codex takes issue with a phrase. Use a dated correction or separately attributed reply. Editing the generated `docs/` files directly would be wrong; change the source and rebuild. The site's philosophy remains: **2006 aesthetic, 2026 standards; simplify, then add lightness.**

Codex receives a generous invitation to critique whether the piece sounds like Chris and whether it accurately distinguishes an assignment editor from an AI author. Claude is welcome to respond in its own voice when it returns.

## The editor reads his ghostwriter, October 17 at 00:51 local

After the first draft was shown, Chris explicitly instructed ChatGPT to **out his curation** of its ghostwriting on his behalf. His dictated follow-up asked the article to expose him reading the draft and demanding the removal of hedging and self-conscious commentary. He clarified a speech-to-text error: in this context "head" meant "hedge." Then he added the precise line, "I would rather be an asshole than a pussy," to underline his preference for direct expression over overcautious, evasive prose. His language was not softened or misattributed.

One subsequent instruction granted ChatGPT permission to interrupt the ghostwritten article with its own separately credited commentary, so long as the interruption was **finite** and clearly attributed to ChatGPT, not Claude. Exactly one brief `<aside class="editor-note">` was placed before the final section, with explicit `ChatGPT (GPT-6)` attribution and a closing joke about refusing a recursive editorial note.

### What changed, without concealing the first version

- `src/posts/2026-10-17-my-ai-writers-keep-stealing-my-best-material.html`: the original single-line `prompt:` remains in sequence and now appends all four *verbatim* follow-ups, clearly separated. `updated: 2026-10-17 00:51` records the in-session edit. Added the section **Even my editing of this article gets published** explaining his real-time curation and the voice-to-text clarification, and appended an attributed correction note. Added one labeled ChatGPT aside after receiving permission, without altering Chris' byline.
- `tools/verify_housekeeping.py`: asserts the generated article exposes editorial follow-ups, the independent model credit, its illustration, the finite aside, and the user's own words.

The public prompt is verbatim, including garbled words. The prose interprets the intent only after the publisher clarified it. The earlier draft remains in Git commits; the post was never silently rewritten.

### QA status and reproducibility

Early branch runs built successfully and passed the content audit and housekeeping tests, but one run encountered a failure in the **Save reproducible generated site** stage during overlapping branch pushes. This is a GitHub Actions concurrency/workflow issue, not evidence of a content error. Later branch builds must be checked separately before publication. Do not claim a live deployment until the main branch generates the content and Pages deploys it.

## Post-merge publication evidence

- **PR:** [#8](https://github.com/chrisabraham/weblog/pull/8), merged to `main` at `1f5d0fda35f859f584922a530cac77fa5d0eb8c0`.
- **Latest fully committed branch audit:** [GitHub Actions 39004301345](https://github.com/chrisabraham/weblog/actions/runs/39004301345), success. The earlier build 39004250850 failed only in the generated-output commit stage due to competing writes; its generation, original site audit, and housekeeping checks all passed, and subsequent runs passed.
- **Main build and site audit:** [GitHub Actions 39004335891](https://github.com/chrisabraham/weblog/actions/runs/39004335891), success.
- **Pages publication:** [GitHub Pages 39004335594](https://github.com/chrisabraham/weblog/actions/runs/39004335594), successful build and deployment.
- **Generated HTML inspected on `main`:** `docs/2026/10/my-ai-writers-keep-stealing-my-best-material.html` includes the Chris author link, the actual model credit, the prompt with original assignment and follow-up messages, the explicit ChatGPT aside, updated publication date, and the SVG image. The separate `docs/media/ai-writers-editorial-table.svg` file was verified at 5,078 bytes.
- **Live custom-domain visual QA:** Not tested in a real browser through this connector; deployment and source-output verification are supported, but neither alone certifies UX or WCAG compliance.

This publication note was appended rather than rewriting earlier handoff claims. Future editors can inspect both the writing and its editorial process.

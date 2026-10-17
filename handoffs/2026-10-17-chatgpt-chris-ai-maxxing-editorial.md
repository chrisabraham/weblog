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

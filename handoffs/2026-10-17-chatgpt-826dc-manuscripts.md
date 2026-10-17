# Oliver Uberti, 826DC, and the working manuscripts on the walls

**Date:** October 17, 2026, Eastern time  
**Publisher and assigning editor:** Chris Abraham  
**Writer/technical contributor:** ChatGPT (GPT-6), ghostwriting on Chris' behalf  
**Branch:** `chatgpt-826dc-publish-final-20261017`  
**New post:** `src/posts/2026-10-17-put-the-redlined-manuscripts-on-the-walls.html`  
**Full-text illustration:** `src/media/826dc-full-essay.avif`  
**Existing original small SVG preserved:** `src/media/826dc-redlined-manuscripts.svg`  
**Intended permalink:** https://chrisabraham.net/2026/10/put-the-redlined-manuscripts-on-the-walls.html

## The meaning of the piece

**Core subject: process, iteration, revision, redlining, and the intimidation produced when aspiring writers see only another writer's final work.**

Chris remembers visiting a 826DC writing room with framed reproductions of manuscripts by Hemingway, Steinbeck and other great authors, heavily covered with revisions. The sight gave him permission to make messy drafts. His close friend Oliver Uberti helped design 826DC's Museum of Unnatural History and has since done notable book design and graphic work with other 826 affiliates.

The published essay is about **that breakthrough**, and what it teaches Chris today as a publisher working with Claude Code, ChatGPT and (later) Codex. He wants the prompts, redlined manuscripts, corrections and Git history visible because the process is part of the art. The book the reader sees is the last draft; the walls show the earlier drafts. In the current revision, the narrative begins directly with the redline gallery and its permission, moves through Hemingway's revisions, and then reaches present-day AI editing. The posse memory, Brian's quiet memorial and Oliver's bibliography come later, supporting rather than displacing the governing theme. The ending returns to redlining.

Two **verbatim prompts** appended near the very end of the source prompt header:
> Don't forget that the centering the center of this article is about process and redlining and not being intimidated by final work
> About iterations and revisions and all that other stuff

The entire original long, voice-to-text 826DC assignment, subsequent amendments, corrections, friendships and Oliver book/Amazon instructions are preserved **verbatim** in the long `prompt:` frontmatter. See the source post rather than relying on a paraphrase. No later revision may silently delete that provenance.

## Oliver and his work

Chris describes Oliver as one of his closest friends, a chum, mate and little brother. Oliver drew Gerris' water strider logo. Chris' only personal visit among the 826 centres was to 826DC, and Oliver was part of its design; other centres are mentioned as context, **not** as places Chris visited. 826 National's 2024 reading list credits Oliver with the design of `The Secret Life of Frogs` from 826 Michigan; the post links directly to that primary source.

The piece now links Oliver's own portfolio, relevant books, 826DC, 826 National, 826LA, 826 Valencia, Dave Eggers, Nínive Calegari, Hemingway, Fitzgerald, Steinbeck, Maxwell Perkins, Oliver's collaborators, and **six direct Amazon /dp/ books** using Chris' existing `gerris-20` Associates tag. The generator adds `rel="sponsored noopener"` plus the standard affiliate disclosure. Preserve transparent disclosure. Historical personal names and age gaps in the posse are user-recalled, and Brian Pollock (called "the Gray Fox") receives a brief memorial without speculative biographical material.

## Illustrations

The full article was supplied as image-model context in Chris' established visual workflow: image generation based on **the entire story**, no text, writing, labels or title in the illustration. The resulting lead visual is converted to a lightweight 512×288 AVIF (source `826dc-full-essay.avif`) and credited to ChatGPT in its caption. The compact hand-built `826dc-redlined-manuscripts.svg` remains in the article **after Hemingway's revision section**, with its existing caption intact, as Chris explicitly requested. Both have descriptive alt text. The small SVG is still a source asset, not an overwritten or deleted file.

## Build, QA, links, metadata

The generator on main includes the October 17 publication-plumbing changes: top navigation Categories directory, real Atom feed, RSS 2.0, both OPML lists, `llms.txt` and `llms-full.txt`, plus the sitemap. Therefore adding this approved post to `src/posts/` automatically places its permalink and category membership across these surfaces; no hand-editing `docs/` necessary. Main build runs `python build.py`, `tools/audit.py`, and `tools/verify_housekeeping.py`. The last recorded branch run before this handoff, [39008094395](https://github.com/chrisabraham/weblog/actions/runs/39008094395), succeeded after moving supplementary sections back and strengthening the iteration narrative.

Check the rendered result for the distinct Chris byline and `GPT-6 in ChatGPT` writing-model credit, original prompt (including typo-laden voice-to-text), full-size figure, little SVG and caption, correct Amazon tag, sponsored rel, and disclosure. Check the live permalink after publishing and only then include the new URL in a full IndexNow blast.

## Prompt sources and publisher approvals

Chris explicitly approved the initial Oliver article and its illustration, then asked to (a) use a generated lead image based on the full text, (b) preserve the little SVG and subtitle, (c) stress Oliver's close friendship and later 826 publishing work, (d) put correct personal experience at 826DC only, (e) include details of his gen-X/millennial posse with remembrance of Brian, (f) promote Oliver's portfolio and books through links, (g) add `gerris-20` affiliate links, and finally (h) **keep the whole piece centred on redlining, process, iterations, revisions and the liberation from the intimidation of finished work**.

These exact instructions are recorded in the post's prompt field and Git change history. This handoff is an explanation, not a substitute for those original user words.

## Publication evidence

Pending final PR merge, main build, Pages deployment, RSS/Atom/sitemap checks, and full IndexNow run. Append results without rewriting this account.


## Post-publication edit: book titles as Amazon Associates links

**October 17, 2026, approximately 2:29 AM Eastern.** Publisher Chris Abraham asked that the names of all books, including Hemingway's *The Sun Also Rises* and its British *Fiesta* title, be direct Amazon Associates hyperlinks rather than sending readers to unrelated bibliographic records or having a detached "Amazon" link after each title. The exact wording of both publisher directives is appended to the article's original prompt field. This change uses Chris' existing \`gerris-20\` tag.

The titles now have the following direct edition links, and the publishing tool continues to assign \`rel="sponsored noopener"\` and the disclosure:

- The Sun Also Rises: Amazon ASIN 0743297334
- Fiesta: Amazon ASIN 0099285037
- London: The Information Capital: Amazon ASIN 0141978791
- Where the Animals Go: Amazon ASIN 0393634027
- Atlas of the Invisible: Amazon ASIN 0393651517
- Atlas of Finance: Amazon ASIN 0300253052
- Notes from a Public Typewriter: Amazon ASIN 1538729113
- The Hidden Nations of Animals: Amazon ASIN 0593716841

Direct links to Oliver's portfolio and 826 organizations remain visible in adjacent prose. The manuscript-redlining argument, personal story, memorial, article-wide image, and little SVG and caption remain intact. A dated on-page editorial update and source prompt appendices are preserved. Added test assertions in \`tools/verify_housekeeping.py\` to detect future regressions of link text or affiliate tags.

At the request of the publisher during this shift, separate Internet Archive / Wayback Machine discussions explored archiving the fleet's five sites. The user received a direct Wayback submission link for www.chrisabraham.com. Save Page Now handles one page at a time and does not schedule a full-site or recurring crawl, according to the Internet Archive's FAQ. **No website has been submitted to the archive by ChatGPT in this shift.**

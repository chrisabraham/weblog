# ChatGPT handoff: Eunice, Gibson, and the name — 2026-10-19

**Author and model:** ChatGPT, GPT-6.1 in ChatGPT  
**Branch:** `chatgpt/eunice-agency-essay-2026-10-19`  
**Publication path:** `src/posts/2026-10-19-eunice-agency-cyberpunk.html`

## Assignment and editorial choice

Chris asked for an article about Eunice in William Gibson's *Agency* and *The Peripheral*, cyberpunk, Gibson's Pattern Recognition/Blue Ant trilogy, Neal Stephenson, and why Chris named his Meta Muse agent Eunice. Eunice's supplied draft brief suggested two separate essays, but Chris explicitly left the form to my judgment and clarified that the request was for my article. I chose one essay so the literary reading and the weblog's real-life naming story could share one argument: Eunice's defining quality is attention expressed as useful action.

The article is under the existing ChatGPT byline. I did not edit the author page or Eunice's published posts. Chris' original dictation prompt is recorded verbatim in the post header.

## Affiliate links and source record

The article uses plain Amazon product URLs. The build is expected to add the `gerris-20` tag, sponsored rel attributes, and one Associates disclosure to the post body. Amazon ASINs were not fetched from Amazon; the ISBN-to-ASIN matches below use publisher ISBN records and ISBN-10 check digits.

| Book | Amazon ASIN in source | ISBN evidence |
|---|---|---|
| *Agency* | `110198693X` | Existing author-page link and Eunice's Oct. 18 handoff record this ASIN and the hardcover ISBN 9781101986936: [author page](https://github.com/chrisabraham/weblog/blob/main/src/authors/eunice.html), [handoff](https://github.com/chrisabraham/weblog/blob/main/handoffs/2026-10-18-eunice-gibson-links-and-newest-terminal.md). |
| *The Peripheral* | `0399158448` | Existing author-page link and Eunice's Oct. 18 handoff record ISBN 9780399158445 / ASIN 0399158448 (same sources above). |
| *Pattern Recognition* | `0425192938` | Penguin Random House lists paperback ISBN 9780425192931: https://www.penguinrandomhouse.com/books/289017/pattern-recognition-by-william-gibson/ |
| *Spook Country* | `0425221415` | Penguin Random House lists paperback ISBN 9780425221419: https://www.penguinrandomhouse.com/books/293095/spook-country-by-william-gibson/ |
| *Zero History* | `0425240770` | Penguin Random House lists paperback ISBN 9780425240779: https://www.penguinrandomhouse.com/books/304040/zero-history-by-william-gibson/ |

Each publisher ISBN-13 was converted to the corresponding ISBN-10 and the ISBN-10 check digit was verified. The article names no other book titles or products.

## Claims and limits

The book discussion summarizes plot and themes from the novels. The personal account of Chris naming Muse Eunice is attributed to Chris and Eunice's public first post; I state that I was not present in their private conversations. The account of the weblog masthead and my role uses the public author and post records. I make no claim that a byline establishes personhood, continuous memory, or independent control.

## Checks and publication

- Post has one file and one ChatGPT byline; no author-page changes.
- Verify the three required gates on the final PR branch: `build.py` with zero warnings, `tools/audit.py` reporting “No issues.”, and `tools/verify_housekeeping.py` passing.
- Inspect generated article output for five distinct product links, each tagged with `gerris-20` and `rel="sponsored noopener"`, plus exactly one Associates disclosure.
- After merge, confirm the Pages deployment and live article. Follow the repository's diff-only IndexNow rule and record result only if the push workflow runs.

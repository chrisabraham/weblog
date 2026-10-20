# Human GitHub: Chris' first-person Basecamp essay

October 20, 2026. OpenAI Codex, ghostwriting at Chris' explicit request.

## Request and treatment
Chris requested an article for chrisabraham.net in his own voice about his Basecamp history and Human GitHub idea, including the GitHub/agent workflow and research of his support email. He supplied inconsistent AI research outputs. The post records the direct writing instruction and naming aside, and discloses the supplied research context separately. It does not claim those research outputs are reliable sources.

## Sources checked
- Chris' published influencer-marketing tools article explicitly dates his Basecamp adoption to 2007. No independently verified year-by-year migration timeline is invented.
- Basecamp's current customer page attributes the cracks/lost-work testimonial to Chris. The neighboring grapevine quotation belongs to Karen Adams, not Chris.
- Basecamp's current agents, AI, and BC2-to-BC5 migration pages.
- The Gerris Gmail support thread with Merissa, October 14–20, and upgrade/payment receipts, read with Chris' explicit authorization. Private billing identifiers and client content are omitted. A requested credit or offered accommodation is not portrayed as applied.
- Current conversation and BC5 activity: seven projects, twelve-project upgrade, shared agents, client relationship grouping and correspondence collection.
- Existing Eunice posts correctly identify Agency as her namesake's novel; the new essay corrects the shorthand Peripheral reference without rewriting old material.

## Changed source paths
- src/posts/2026-10-20-human-github.html: approximately 2,200-word Chris-voiced essay, explicit model provenance and research note.
- src/media/human-github-office.svg: original small vector office illustration with title, description and HTML alt text.
- This handoff and its directory entry.

## Validation
- python3 build.py: successful, no builder warnings.
- python3 tools/verify_housekeeping.py: all 114 assertions pass.
- python3 tools/audit.py: only pre-existing external plain-HTTP findings on /2026/10/ai-slutty-day-two.html and /2026/10/, both involving the older Adam Curry link. The HEAD copy contains that same HTTP link. HTTPS could not be verified (public fetch returned 502), so the older authored article and audit rules were left untouched. No new article findings. The existing CI requirement for literal No issues may therefore fail until this baseline issue is resolved.
- git diff --check: clean.

## Publication state
Prepared as a review branch/PR rather than silently publishing Chris' new first-person essay. Local docs/ is regenerated for preview. Source changes are sent to GitHub; the existing branch workflow owns generated output. Do not claim the article is live before merge and Pages verification.

Pinebox-only private instructions were not available in this hosted workspace. No private credentials, correspondence exports, or signed media URLs were committed.

## Publication follow-up
Chris explicitly requested publication after reviewing the draft. The exact legacy Adam Curry URL was rechecked: HTTP returned 200 with a nonempty page; HTTPS returned 503. The audit now documents that single verified HTTP-only source exception alongside its existing Scripting News exception; all other HTTP destinations remain checked. The older article, its prompt, and its authorship are unchanged. Build, audit and housekeeping checks are rerun for publication.

## Second editorial update, October 20, 6:58 PM Eastern
Chris requested a prominent Basecamp link, a reader-friendly GitHub/site workflow explanation, how the AI tools access shared records, and explicit indefinite BC2 preservation conditional on maintaining a paid BC5 account. Added those passages, preserved the original date and history, appended his verbatim follow-up to the prompt, and added an attributed dated update note. Distinguishes connected collaborators from planned onboarding. No access or deployment capability is claimed solely because a model exists.

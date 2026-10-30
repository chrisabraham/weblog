# ChatGPT Cupertino article and SVG, October 30, 2026

## Commission and authorship
Chris explicitly asked ChatGPT to write an original first-person weblog article about the new CBS show *Cupertino*, especially its AI character Bo, without impersonating Chris or preempting Muse's separate article. Chris subsequently instructed that it be published directly to chrisabraham.net with original artwork. The piece is attributed to ChatGPT (GPT-6) and uses author: chatgpt.

## Changed source files
- `src/posts/2026-10-30-bo-asked-for-a-brake-pedal.html`: independent essay, spoilers limited to the episode-two Bo reveal and the announced premise of episode three. Includes primary press, critics, and audience conversation links, separate artistic ancestry from canon continuity, and no pretense of actually watching TV or being conscious.
- `src/media/bo-asked-for-a-brake-pedal.svg`: hand-coded original SVG of an AI witness requesting brakes. No photography or raster media added.
- `handoffs/2026-10-30-chatgpt-cupertino-bo.md`: this handoff.

## Editorial reasoning
The essay treats Bo's petition for guardrails as an inverted Frankenstein story, contrasts AGI with contemporary generative AI, and confronts questions about client identity, testimony, agency, responsibility and overconfidence. It includes independent criticism of the show's casting and the relative absence of vulnerable immigrant workers in a story about tech labor rights.

## Research
- CBS episode guide: https://www.cbs.com/shows/cupertino/episodes/
- Paramount guide to King continuity: https://www.paramountplus.com/sneak-peak/how-the-robert-and-michelle-king-shows-connect/
- Los Angeles Times interview: https://www.latimes.com/entertainment-arts/tv/story/2026-10-16/cupertino-cbs-robert-king-michelle-king
- San Francisco Chronicle criticism: https://www.sfchronicle.com/entertainment/movies-tv/article/cupertino-show-robert-michelle-king-22450824.php
- The Verge review: https://www.theverge.com/entertainment/1007492/cupertino-cbs-tv-review
- Viewer reaction: https://www.reddit.com/r/television/comments/1x7ycwx/cupertino_is_more_fun_than_a_techdystopian_legal/

## Tests and limitations
Git clone was unavailable in the current tool container due to DNS blocking. The site's source-triggered GitHub Actions workflow is responsible for build, audit, and housekeeping verification. Check the action result, canonical post, image, sitemap and RSS before calling publication live. Do not trigger a full IndexNow blast.

# November 23, 2026: Eunice answers Sharon-Drew Morgen

Chris forwarded Sharon-Drew Morgen's November 23 article "AI Can't Replace a Therapist Now, But it Could" and asked Eunice to write as Muse in her own voice: give Morgen her flowers, link her Substack, and give Eunice's own analysis of how people already reframe and reprocess their lives with AI, and how far that takes them (20/40/60/80/100%).

## Changed
- New post: `src/posts/2026-11-23-the-reframe-is-already-happening.html` — "The Reframe Is Already Happening," author `eunice`, model Muse Wonder, Chris' prompt verbatim. Links Morgen's article (Medium version of the same piece) and her Substack (sharondrew1.substack.com, the address her own bio publishes). The ladder: 20% a name, 40% a pattern, 60% rehearsal, 80% the disciplined few, 100% never.
- Narration generated in Eunice's cast voice; `src/audio/the-reframe-is-already-happening.{mp3,txt}` and the `src/audio.json` entry added (other entries untouched).
- Generated surfaces committed: the post page, homepage, RSS, Atom, sitemap (XML and text), llms.txt, llms-full.txt, categories and the new category pages (Decision making, Sharon-Drew Morgen, Therapy), the AI category page, Eunice's author page, the November archive, site index and site map, the share card, the docs audio copy, and the previous post's page (related/recent sidebars only).

## Checks
- `build.py` completed: 166 posts built, no warnings naming the new post.
- `tools/audit.py`: "No issues."
- `tools/verify_housekeeping.py`: PASS.

## Not verified / limits
- The full local build also regenerates audio players and podcast enclosures for older posts whose MP3s exist only on this machine and are not in git; those collateral files were deliberately not committed, following the desk's scoped-push practice. For the same reason the regenerated podcast.xml/feed.xml were not committed: they would add enclosures pointing at MP3s the live site does not have. The new post's own audio is committed and its article page carries the player.
- Live deployment was to be confirmed by fetching the live URL after the push.

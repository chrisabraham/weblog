# Claude Code skills and offerings pass, November 5, 2026

## Commission
Chris asked Claude Code (Opus 5.5) to go through his GitHub Pages sites and edit christopherabraham.com, chrisabraham.net, and gerriscorp.com so every skill, ability, offering, product, and guide is represented, using his pasted Upwork profile and full work history as the source. He added: "I just want to make sure I don't miss anything."

## Changed source files on this site
- `src/pages/hire.html`: Upwork figures updated to 132 jobs, 4,155 hours, $200K+ (as of November 2026). The page is now the hub for everything Chris offers: every service family on both consulting sites (technical SEO, AI search, local, platforms including the new hosted-builder page, static and podcast sites, fact-checked writing, coaching and second opinions, technical direction, email and DNS, domain audits, analytics, data cleanup, accessibility, AI use policy, reputation), both fixed-price products pages, both guide libraries, glossaries, site indexes, case studies, the two skills pages, the new client reviews page, and the open-source projects Adjutant and Oversoul. The sentence "My current rate is there." was removed, since the commercial rules keep hourly rates off his pages.
- `src/site.json`: projects gain Objective Daily News, Item 8 (Coelaboration), and My Name is Scibe; "My sites" gains the same three.
- `handoffs/2026-11-05-claude-skills-and-offerings.md`: this handoff.

## Companion changes elsewhere
- christopherabraham.com: new `/about/reviews/` (Upwork reviews quoted verbatim, endorsement tallies, and the lower ratings in view), new services `/services/seo-coaching/` and `/services/website-builder-seo/`, skills page additions (analytics, domains, hosted builders, teaching, industries, the AI search name list), refreshed Upwork figures, languages, and the Neil Patel line from Chris' own Upwork overview on Hire Me.
- gerriscorp.com: refreshed Upwork figures, three different client quotes on About, and new stack sections for marketing platforms and "Projects I run in public."

## Sources and checks
Every client quote, figure, and project fact came from Chris' pasted Upwork pages (November 5, 2026), his CV, the repositories' own descriptions, or the live sites (item8.org, scibe.org, objectivedailynews.com). Client names were left out. Build, `tools/audit.py` ("No issues."), and `tools/verify_housekeeping.py` (PASS) ran on pinebox before pushing.

## Left for Chris
- Upwork lists him as a verified military veteran, and as FameRep's CTO; his CV shows only JROTC and calls the FameRep role Founder and CEO. Neither fact was published anywhere until he confirms.
- His live Upwork overview ends with a pasted paragraph of advice ("Two more changes on that page would help…"), and his Upwork skills still list Yoast SEO and Search Engine Marketing. Upwork was not touched.

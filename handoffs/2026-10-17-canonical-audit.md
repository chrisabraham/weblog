# Canonical indexing audit

October 17, 2026. OpenAI Codex, directed by Chris Abraham.

Auditing five GitHub sites revealed that build.py removed every occurrence of index.html from canonical paths, turning /site-index.html into /site-. Changed cleanup to remove only a trailing directory /index.html filename. Regenerated the subject index and added a regression check. Category and monthly archives remain noindex, follow and outside sitemaps, as requested.

Validation: build without warnings; audit crawled 81 pages with No issues; 111 housekeeping assertions passed. Live indexing eligibility is distinct from actual search engine indexing.

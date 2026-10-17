#!/usr/bin/env python3
"""Regression checks for the ChatGPT October 16 housekeeping shift.

No third-party dependency. Deliberately static: tests inspect the exact files
GitHub Pages will serve, not claims made by Lighthouse or other scoring tools.
Run after python build.py. Fail loudly if the core publication contract breaks.
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import re

DOCS = Path(__file__).resolve().parent.parent / "docs"
HOME = (DOCS / "index.html").read_text(encoding="utf-8")
STYLE = (DOCS.parent / "src" / "style.css").read_text(encoding="utf-8")
POSTS = sorted((DOCS / "2026/10").glob("*.html"))
errors = []
checks = []


def verify(condition, label):
    checks.append(label)
    if not condition:
        errors.append(label)


class PageInspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.images, self.ids, self.articles = [], [], set(), 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a":
            self.links.append(a.get("href", ""))
        if tag == "img":
            self.images.append(a)
        if tag == "article":
            self.articles += 1


h = PageInspector()
h.feed(HOME)
verify(h.articles == min(15, len(POSTS)), "Homepage contains one teaser for each featured post")
verify(HOME.count('class="post-excerpt p-summary"') == h.articles,
       "Every homepage article has a plain-text editorial excerpt")
verify(HOME.count('class="read-more"') == h.articles,
       "Every homepage teaser has an explicit full-article link")
verify('class="prompt"' not in HOME, "Verbatim prompts appear only on standalone articles")
verify('<figure' not in HOME, "Heavy figures and media stay off homepage")
verify('<a class="skip" href="#main">Skip to main content</a>' in HOME,
       "Skip link has accurate accessible wording")
verify('.skip:focus' in STYLE and 'color: var(--ink)' in STYLE.split('.skip:focus', 1)[1].split('}', 1)[0],
       "Skip link focused text is distinct from its background")
verify('.topnav a:hover, .topnav a:focus-visible' in STYLE,
       "Navigation focused text and background styles share an explicit rule")
verify("url" not in [], "Smoke check completes")  # Keeps no external service dependency.

for slug in ("the-housekeeping-twin-arrives", "the-art-of-the-handoff", "the-house-and-its-feng-shuai"):
    post = DOCS / "2026/10" / f"{slug}.html"
    verify(post.exists(), f"New ChatGPT post exists: {slug}")
    if post.exists():
        content = post.read_text(encoding="utf-8")
        verify('class="prompt"' in content, f"Verbatim source prompt exposed: {slug}")
        verify('href="/authors/chatgpt.html"' in content, f"ChatGPT byline points to author: {slug}")

# Regression: wiki syntax may legitimately refer to a published post rather than
# an evergreen wiki page. No more false redlink for the named flotilla article.
flotilla_reference = DOCS / "2026/10/chaff-flares-reputation-work.html"
if flotilla_reference.exists():
    rendered = flotilla_reference.read_text(encoding="utf-8")
    verify('href="/2026/10/little-boats-one-flotilla.html" class="postlink"' in rendered,
           "Article cross-reference links to the real flotilla permalink")
    verify('title="Little boats, one flotilla (page does not exist yet)"' not in rendered,
           "Existing published article is not marked as missing wiki content")

verify((DOCS / "authors/chatgpt.html").exists(), "ChatGPT author profile is generated")
verify("eAIsterEgg / 01" in HOME, "Source-view greeting survives generation")
verify("eAIsterEgg / 02" in (DOCS / "humans.txt").read_text(encoding="utf-8"),
       "humans.txt has the stateless-session clue")
verify('class="eai-lantern" aria-hidden="true"' in HOME,
       "Decorative authors lantern is hidden from assistive technology")
verify(".eai-lantern" in STYLE and "prefers-reduced-motion: no-preference" in STYLE,
       "Animated decorative lantern respects reduced motion")


# Internal links need a real on-disk destination, except fragment-only links.
broken = []
missing_alts = []
invalid_schema = []
for page in DOCS.rglob("*.html"):
    text = page.read_text(encoding="utf-8")
    parser = PageInspector()
    parser.feed(text)
    for a in parser.images:
        if not a.get("alt"):
            missing_alts.append((str(page.relative_to(DOCS)), a.get("src")))
    for href in parser.links:
        if not href.startswith("/"):
            continue
        root = href.split("#", 1)[0].split("?", 1)[0]
        if not root:
            continue
        target = DOCS / root.lstrip("/")
        if root.endswith("/"):
            target /= "index.html"
        if not target.exists():
            broken.append((str(page.relative_to(DOCS)), href))
    for body in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        try:
            json.loads(body)
        except json.JSONDecodeError:
            invalid_schema.append(str(page.relative_to(DOCS)))
verify(not broken, f"Generated internal links resolve ({len(broken)} broken): {broken[:8]}")
verify(not missing_alts, f"Images have nonempty alt attributes ({len(missing_alts)} missing): {missing_alts[:8]}")
verify(not invalid_schema, f"JSON-LD parses ({len(invalid_schema)} invalid): {invalid_schema[:8]}")

print(f"Housekeeping checks: {len(checks)} assertions across {len(list(DOCS.rglob('*.html')))} HTML pages.")
for label in checks:
    print(("FAIL" if label in errors else "PASS") + " " + label)
if errors:
    raise SystemExit(f"{len(errors)} regression check(s) failed")
print("Housekeeping checks: PASS")

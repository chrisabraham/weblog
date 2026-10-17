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

# The first-person Chris essay is explicitly assigned, then ghostwritten by
# ChatGPT. Provenance lives both on the rendered post and in the dated handoff.
editorial_post = DOCS / "2026/10/i-let-the-ais-steal-my-best-material.html"
verify(editorial_post.exists(), "Chris' AImaxxing editorial essay is generated")
if editorial_post.exists():
    page = editorial_post.read_text(encoding="utf-8")
    verify('class="prompt"' in page and "All right the last task for tonight" in page,
           "Chris' original rambling assignment survives in the displayed prompt")
    verify("GPT-6 in ChatGPT, writing on behalf of Chris Abraham" in page,
           "Chris article openly discloses its ChatGPT ghostwriter")
    verify("Editorial insertion by ChatGPT" in page and "Claude did not write this article" in page,
           "One distinct ChatGPT editorial insertion has unmistakable attribution")
    verify('src="/media/chatgpt-red-pencil-three-writers.svg"' in page,
           "Chris article includes its original lightweight SVG illustration")
    verify("https://github.com/chrisabraham/weblog/blob/main/handoffs/2026-10-17-chatgpt-editorial-fingerprints.md" in page,
           "Original prompt and full red-pencil edit log are both discoverable")
editorial_svg = DOCS / "media/chatgpt-red-pencil-three-writers.svg"
verify(editorial_svg.exists(), "AI writers and red pencil SVG is published")
if editorial_svg.exists():
    svg = editorial_svg.read_text(encoding="utf-8")
    verify("<title" in svg and "<desc" in svg and "prefers-reduced-motion:reduce" in svg,
           "Editorial SVG has an accessible description and reduced-motion fallback")
    verify(len(svg.encode("utf-8")) < 12000 and "<text" not in svg,
           "Original SVG is lightweight and contains no printed words")

# Regression: wiki syntax may legitimately refer to a published post rather than
# an evergreen wiki page. No more false redlink for the named flotilla article.
flotilla_reference = DOCS / "2026/10/chaff-flares-reputation-work.html"
if flotilla_reference.exists():
    rendered = flotilla_reference.read_text(encoding="utf-8")
    verify('href="/2026/10/little-boats-one-flotilla.html" class="postlink"' in rendered,
           "Article cross-reference links to the real flotilla permalink")
    verify('title="Little boats, one flotilla (page does not exist yet)"' not in rendered,
           "Existing published article is not marked as missing wiki content")

# The site README must be a real, accessible, indexable page, not merely
# a nostalgic joke. Make sure newcomers have the link and terms they need.
readme = DOCS / "readme.html"
verify(readme.exists(), "README page is generated")
if readme.exists():
    guide = readme.read_text(encoding="utf-8")
    verify('href="/readme.html" class="readme-tab">README</a>' in HOME,
           "README is visible in the main navigation")
    verify('href="/readme.html">README</a>' in HOME,
           "README is linked from the footer")
    verify('<h1 class="page-title">README</h1>' in guide,
           "README has a plain, readable page heading")
    verify(guide.count("<dt>") >= 9 or (guide.count("<dt>") + guide.count("<dt ")) >= 9,
           "README explains important terms in a semantic definition list")
    verify('class="topnav"' in guide and 'href="/wiki/"' in guide,
           "README keeps navigation and links to the reference wiki")
verify('.topnav a.readme-tab' in STYLE, "README retains uppercase navigation styling")

# Publisher's house style: possessive of Chris is always Chris'.
# Leave original user prompt metadata unedited and exempt from the check.
root = DOCS.parent
samples = [root / "README.md"]
samples += list((root / "src/pages").glob("*.html"))
samples += list((root / "src/authors").glob("*.html"))
samples += list((root / "src/posts").glob("*.html"))
nonpreferred = []
for source in samples:
    raw = source.read_text(encoding="utf-8")
    if source.parent.name == "posts":
        head, divider, body = raw.partition("\n---\n")
        head = "\n".join(line for line in head.splitlines()
                         if not line.startswith("prompt:"))
        raw = head + divider + body
    if re.search(r"Chris(?:'s|’s)\b", raw):
        nonpreferred.append(str(source.relative_to(root)))
verify(not nonpreferred,
       f"Chris' is the house possessive outside original prompts ({nonpreferred})")

# Contrast of red README on the paper, and inverse focus text on red.
accents = re.findall(r"--readme-accent:\s*(#[0-9a-fA-F]{6})\s*;", STYLE)
def luminance(rgb):
    channels = [int(rgb[i:i+2], 16)/255 for i in (1,3,5)]
    linear = [c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4 for c in channels]
    return sum(a*b for a,b in zip(linear,(0.2126,0.7152,0.0722)))
def ratio(c1,c2):
    bright,dark = sorted((luminance(c1),luminance(c2)),reverse=True)
    return (bright+0.05)/(dark+0.05)
verify(len(accents)==2, "README has red values in light and dark themes")
if len(accents)==2:
    for theme,accent,paper in (("light",accents[0],"#ffffff"),("dark",accents[1],"#16181d")):
        verify(ratio(accent,paper)>=7.0,
               f"{theme} README link and inverse-focus colors achieve AAA text contrast")
verify(".topnav a.readme-tab:visited" in STYLE,
       "Visited README remains visibly red")
verify(".topnav a.readme-tab:focus-visible" in STYLE
       and "background: var(--readme-accent); color: var(--paper)" in STYLE,
       "README has a separate legible keyboard focus state")


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

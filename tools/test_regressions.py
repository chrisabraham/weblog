#!/usr/bin/env python3
"""Fast static build regression checks. Not a browser audit or WCAG certification."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SRC = ROOT / "src"
issues = []

def assert_true(ok, message):
    if not ok:
        issues.append(message)

class Reader(HTMLParser):
    def __init__(self):
        super().__init__()
        self.articles = 0
        self.prompts = 0
        self.images = []
        self.links = []
        self.schemas = []
        self.script_type = None
        self.script_data = ""
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "article":
            self.articles += 1
        if tag == "details" and "prompt" in a.get("class", "").split():
            self.prompts += 1
        if tag == "img":
            self.images.append(a)
        if tag == "a":
            self.links.append(a)
        if tag == "script":
            self.script_type = a.get("type")
            self.script_data = ""
    def handle_data(self, data):
        if self.script_type:
            self.script_data += data
    def handle_endtag(self, tag):
        if tag == "script" and self.script_type:
            if self.script_type == "application/ld+json":
                try:
                    self.schemas.append(json.loads(self.script_data))
                except ValueError:
                    issues.append("Invalid JSON-LD")
            self.script_type = None

def read(path):
    v = Reader()
    v.feed(path.read_text(encoding="utf-8"))
    return v

home = DOCS / "index.html"
posts = list((SRC / "posts").glob("*.html"))
assert_true(home.exists(), "Homepage missing")
if home.exists():
    h = read(home)
    teasers = [a for a in h.links if a.get("aria-label", "").startswith("Read full article: ")]
    assert_true(h.articles == min(15, len(posts)), "Homepage post count wrong")
    assert_true(len(teasers) == h.articles, "One read-more link required per homepage article")
    assert_true(h.prompts == 0, "Homepage should not duplicate full prompts")
    assert_true(len(home.read_bytes()) < 110_000, "Homepage size above 110KB review budget")
    for a in teasers:
        dest = a.get("href", "")
        assert_true((DOCS / dest.lstrip("/")).is_file(), "Missing article destination: " + dest)

for slug in ("hello-world-i-brought-a-broom", "feng-shuai-house-i-inherited", "the-art-of-the-handoff"):
    p = DOCS / "2026" / "10" / (slug + ".html")
    assert_true(p.exists(), "Missing ChatGPT article: " + slug)
    if p.exists():
        article = read(p)
        assert_true(article.prompts == 1, "Missing original prompt: " + slug)
        nodes = [node for schema in article.schemas for node in schema.get("@graph", [])
                 if node.get("@type") == "BlogPosting"]
        assert_true(len(nodes) == 1, "Missing BlogPosting schema: " + slug)
        if nodes:
            a = nodes[0].get("author", {})
            assert_true(a.get("name") == "ChatGPT", "Wrong AI author: " + slug)
            assert_true(a.get("parentOrganization", {}).get("name") == "OpenAI",
                        "Wrong model parent organization: " + slug)

assert_true((DOCS / "authors" / "chatgpt.html").exists(), "Author profile missing")
for name in ("rss.xml", "sitemap.xml", "blogroll.opml"):
    assert_true((DOCS / name).exists(), name + " missing")
flotilla = DOCS / "2026" / "10" / "chaff-flares-reputation-work.html"
if flotilla.exists():
    assert_true('href="/2026/10/little-boats-one-flotilla.html"' in flotilla.read_text(),
                "Flotilla cross-reference still points to wiki")

css = (SRC / "style.css").read_text()
assert_true("a.skip:focus" in css, "Skip link focus correction missing")
assert_true(".topnav a:focus-visible" in css, "Navigation focus correction missing")

count = 0
for p in DOCS.rglob("*.html"):
    count += 1
    obj = read(p)
    for im in obj.images:
        assert_true("alt" in im, "Image missing alt: " + str(p))
    for link in obj.links:
        href = link.get("href", "")
        if not href.startswith("/") or href.startswith("//"):
            continue
        dest = href.split("#", 1)[0].split("?", 1)[0]
        if not dest:
            continue
        path = DOCS / dest.lstrip("/")
        if dest.endswith("/"):
            path = path / "index.html"
        assert_true(path.exists(), "Broken internal link: " + str(p.relative_to(DOCS)) + " -> " + dest)

print(f"Static regression audit: {count} pages, {len(posts)} sources, {len(issues)} findings")
if issues:
    for error in issues[:100]:
        print("FAIL:", error)
    sys.exit(1)
print("PASS: link graph, alt presence, excerpts, original prompts, model schema and site files")

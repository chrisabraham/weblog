#!/usr/bin/env python3
"""Crawl docs/ the way Screaming Frog would and list what it would flag.

  python3 tools/audit.py
"""
import collections
import html
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
pages = {}
for f in DOCS.rglob("*.html"):
    url = "/" + str(f.relative_to(DOCS)).replace("index.html", "")
    pages[url] = f.read_text(encoding="utf-8")

issues = collections.defaultdict(list)
titles, descs, h1s, h2first = collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(list)
for url, t in pages.items():
    noindex = 'content="noindex' in t
    title = html.unescape(re.search(r"<title>(.*?)</title>", t, re.S).group(1))
    desc = re.search(r'<meta name="description" content="([^"]*)"', t)
    desc = html.unescape(desc.group(1)) if desc else ""
    main = re.search(r"<main.*?</main>", t, re.S).group(0)
    h1 = [re.sub(r"<[^>]+>", "", x).strip() for x in re.findall(r"<h1[^>]*>(.*?)</h1>", t, re.S)]
    h2 = [re.sub(r"<[^>]+>", "", x).strip() for x in re.findall(r"<h2[^>]*>(.*?)</h2>", t, re.S)]
    if not noindex:
        titles[title].append(url); descs[desc].append(url)
        if h1: h1s[h1[0]].append(url)
        if h2: h2first[h2[0]].append(url)
    if len(h1) != 1: issues["H1: missing or multiple"].append(url)
    if h1 and len(h1[0]) > 70: issues["H1: over 70 characters"].append(url)
    if not h2: issues["H2: missing"].append(url)
    if not desc: issues["Meta description: missing"].append(url)
    if 'rel="canonical"' not in t: issues["Canonical: missing"].append(url)
    if 'og:image"' not in t and not noindex: issues["Open Graph image: missing"].append(url)
    for img in re.findall(r"<img[^>]*>", t):
        if 'alt="' not in img: issues["Images: missing alt"].append(url)
    for href in re.findall(r'href="(/[^"#?]*)', t):
        target = href if href.endswith("/") or "." in href.rsplit("/", 1)[-1] else href + "/"
        path = DOCS / target.lstrip("/")
        if target.endswith("/"): path = path / "index.html"
        if not path.exists(): issues[f"Internal link broken"].append(f"{url} -> {href}")
    if re.search(r'href="http://(?!scripting\.com)', t): issues["Links: plain HTTP (external)"].append(url)
    levels = [int(x) for x in re.findall(r"<h([1-6])[\s>]", main)]
    for a, b in zip(levels, levels[1:]):
        if b > a + 1: issues["Headings: skipped level"].append(f"{url} h{a}->h{b}"); break
for name, d in (("Title: duplicate", titles), ("Meta description: duplicate", descs), ("H1: duplicate", h1s), ("H2: duplicate (first H2)", h2first)):
    for k, v in d.items():
        if len(v) > 1: issues[name].append(f"{k!r}: {', '.join(v)}")
print(f"{len(pages)} pages crawled")
for k, v in sorted(issues.items()):
    print(f"\n{k} ({len(v)})")
    for x in v[:12]: print("  ", x)
if not issues: print("No issues.")

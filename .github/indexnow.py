"""Tell IndexNow which weblog pages changed.

  python3 .github/indexnow.py <before-sha> <after-sha>   new or edited pages
  python3 .github/indexnow.py --all                      every URL in the live sitemap

New pages are always sent. Edited ones are sent only when a handful changed:
a template change touches every page, and those don't need re-crawling.
Noindex pages (monthly and category archives, 404) are never sent.
"""
import json
import re
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

LIVE = "https://chrisabraham.net"
HOST = "chrisabraham.net"
EDITED_LIMIT = 20
SKIP = re.compile(r"^docs/(\d{4}/\d{2}/index\.html|category/|404\.html)")


def key():
    return re.search(r'^INDEXNOW_KEY = "([0-9a-f]+)"', open("build.py").read(), re.M).group(1)


def page_url(path):
    """Map a docs HTML path to its public URL without mangling hyphenated names."""
    relative = path[len("docs/"):]
    if relative == "index.html":
        relative = ""
    elif relative.endswith("/index.html"):
        relative = relative[:-len("index.html")]
    return LIVE + "/" + relative


def changed_urls(before, after):
    if not before or set(before) == {"0"}:
        return []
    def diff(f):
        out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=" + f, before, after, "--", "docs/"],
                             capture_output=True, text=True, check=True).stdout.split()
        return [p for p in out if p.endswith(".html") and not SKIP.match(p)]
    added, edited = diff("A"), diff("M")
    pages = added + (edited if len(edited) <= EDITED_LIMIT else [])
    if not pages:
        return []
    urls = [page_url(p) for p in pages]
    return urls + [LIVE + "/", LIVE + "/archives.html"]


def sitemap_urls():
    with urllib.request.urlopen(LIVE + "/sitemap.xml", timeout=30) as r:
        tree = ET.fromstring(r.read())
    return [e.text.strip() for e in tree.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]


def wait_live(urls, timeout=900):
    """GitHub Pages deploys after the push; wait until new pages answer."""
    deadline, pending = time.time() + timeout, list(urls)
    while pending and time.time() < deadline:
        still = []
        for u in pending:
            try:
                urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=20)
            except Exception:
                still.append(u)
        pending = still
        if pending:
            time.sleep(30)
    return [u for u in urls if u not in pending]


def submit(urls, k):
    body = json.dumps({"host": HOST, "key": k, "keyLocation": f"{LIVE}/{k}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow: HTTP {r.status} for {len(urls)} URLs")


def main():
    urls = sitemap_urls() if sys.argv[1:] == ["--all"] else changed_urls(*sys.argv[1:3])
    if not urls:
        print("no page changes; nothing to submit")
        return
    urls = wait_live(sorted(set(urls)))
    for i in range(0, len(urls), 10000):
        submit(urls[i:i + 10000], key())


if __name__ == "__main__":
    main()

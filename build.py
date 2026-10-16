#!/usr/bin/env python3
"""Build the Chris Abraham Weblog into docs/ (GitHub Pages serves main:/docs).

Standard library only. Sources:
  src/posts/YYYY-MM-DD-slug.html  key: value header, a line of ---, then HTML
  src/pages/<name>.html           same format, for About, Colophon, etc.
  src/site.json                   blogroll (my own sites and profiles), reading list, projects

Post header keys: title, date (2026-10-16 17:20), categories (comma list),
description (120-160 chars, no dashes or pipes), model, prompt (Chris' own
words, shown under the post), status (draft hides it from the build).

Run: python3 build.py
"""
import datetime as dt
import html
import json
import re
import shutil
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "docs"

SITE_URL = "https://chrisabraham.net"   # the one place the domain lives
TITLE = "Chris Abraham"
HOME_TITLE = "Chris Abraham: a weblog about building with AI and Claude Code"
TAGLINE = "Notes from building things with AI, written by Claude from my prompts."
AUTHOR = "Chris Abraham"
EMAIL = "cja@well.com"
TZ = ZoneInfo("America/New_York")
HOME_POSTS = 15
GA_ID = "G-KWXM1ZX7WQ"          # GA4 measurement ID; empty means no analytics
INDEXNOW_KEY = "cc740d643ba76c19773b15720256af8c"

PERSON = {
    "@type": "Person",
    "@id": SITE_URL + "/about.html#chris",
    "name": AUTHOR,
    "url": SITE_URL + "/about.html",
}

# GA loads on first interaction or 4 seconds after load, like the sibling sites.
GA = """<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '{id}');
  (function () {
    var done = false;
    function load() {
      if (done) return;
      done = true;
      var s = document.createElement('script');
      s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id={id}';
      document.head.appendChild(s);
    }
    ['pointerdown', 'keydown', 'scroll', 'touchstart'].forEach(function (e) { addEventListener(e, load, {once: true, passive: true}); });
    addEventListener('load', function () { setTimeout(load, 4000); });
  })();
</script>"""

SPECULATION = ('<script type="speculationrules">{"prefetch": [{"where": {"and": [{"href_matches": "/*"}, '
               '{"not": {"href_matches": ["/*.txt", "/*.xml", "/*.opml"]}}]}, "eagerness": "moderate"}]}</script>')


# ---------------------------------------------------------------- sources

def parse(path):
    text = path.read_text(encoding="utf-8")
    head, _, body = text.partition("\n---\n")
    meta = {}
    for line in head.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    meta["body"] = dashes(body.strip())
    return meta


def dashes(body):
    """Turn -- into a closed-up em dash, outside <pre> and <code>."""
    parts = re.split(r"(<pre.*?</pre>|<code.*?</code>|<!--.*?-->)", body, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"\s*--\s*", "—", parts[i])
        parts[i] = re.sub(r"\s+—\s+", "—", parts[i])
    return "".join(parts)


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def check_meta(name, meta):
    problems = []
    for key in ("title", "description"):
        v = meta.get(key, "")
        if not v:
            problems.append(f"missing {key}")
        if re.search(r" [-–—|] |\|", v):
            problems.append(f"{key} uses a separator dash or pipe")
    d = len(meta.get("description", ""))
    if d and not 110 <= d <= 165:
        problems.append(f"description is {d} chars (aim 120-160)")
    for p in problems:
        print(f"  warn {name}: {p}")


def load_posts():
    posts = []
    for path in sorted((SRC / "posts").glob("*.html")):
        m = parse(path)
        if m.get("status") == "draft":
            print(f"  skip draft {path.name}")
            continue
        check_meta(path.name, m)
        m["when"] = dt.datetime.strptime(m["date"], "%Y-%m-%d %H:%M").replace(tzinfo=TZ)
        m["slug"] = path.stem[11:]
        m["cats"] = [c.strip() for c in m.get("categories", "").split(",") if c.strip()]
        m["path"] = f"/{m['when']:%Y}/{m['when']:%m}/{m['slug']}.html"
        m["url"] = SITE_URL + m["path"]
        m["updated"] = (dt.datetime.strptime(m["updated"], "%Y-%m-%d %H:%M").replace(tzinfo=TZ)
                        if m.get("updated") else m["when"])
        posts.append(m)
    posts.sort(key=lambda p: p["when"], reverse=True)
    return posts


# ---------------------------------------------------------------- helpers

e = html.escape


def long_date(d):
    return f"{d:%A}, {d:%B} {d.day}, {d:%Y}"


def clock(d):
    return d.strftime("%I:%M %p").lstrip("0")


def ld(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
            + "</script>")


def text_only(body):
    t = re.sub(r"<[^>]+>", " ", body)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def cat_link(c):
    return f'<a href="/category/{slugify(c)}.html" rel="tag">{e(c)}</a>'


# ---------------------------------------------------------------- page shell

def page(*, title, description, path, body, site, posts, schema=None,
         noindex=False, og_type="website", extra_head=""):
    canonical = SITE_URL + path.replace("index.html", "")
    full_title = HOME_TITLE if path == "/index.html" else title  # site name rides in og:site_name and schema, not every title
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>try{{var t=localStorage.getItem("weblog-theme");if(t==="dark"||(!t&&matchMedia("(prefers-color-scheme: dark)").matches))document.documentElement.setAttribute("data-theme","dark")}}catch(e){{}}</script>
<title>{e(full_title)}</title>
<meta name="description" content="{e(description)}">
<meta name="robots" content="{robots}">
<meta name="author" content="{AUTHOR}">
<meta name="generator" content="build.py, written by Claude in Claude Code">
<meta name="theme-color" content="#ffffff" id="theme-color">
<link rel="canonical" href="{canonical}">
<link rel="alternate" type="application/rss+xml" title="{e(TITLE)} (RSS)" href="{SITE_URL}/rss.xml">
<link rel="blogroll" type="text/x-opml" href="{SITE_URL}/blogroll.opml">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:site_name" content="{e(TITLE)}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
{extra_head}<style>{CSS}</style>
{ld(schema) if schema else ""}
{SPECULATION}
{GA.replace("{id}", GA_ID) if GA_ID else ""}
</head>
<body>
<a class="skip" href="#main">Skip to the posts</a>
<div id="wrap">
<header id="banner">
  <button type="button" class="theme-toggle" id="theme-toggle" hidden>dark</button>
  <p class="site-title"><a href="/" rel="home">{e(TITLE)}</a></p>
  <p class="tagline">{e(TAGLINE)}</p>
  <nav class="topnav" aria-label="Main">
    <a href="/">Home</a> <a href="/projects.html">Projects</a> <a href="/archives.html">Archives</a>
    <a href="/about.html">About</a> <a href="/colophon.html">Colophon</a> <a href="/rss.xml">RSS</a>
  </nav>
</header>
<div id="cols">
<main id="main">
{body}
</main>
{sidebar(site, posts)}
</div>
<footer id="footer">
  <p>Copyright {dt.date.today().year} {AUTHOR}. Every post here is written by Claude from my prompts, and each one says which model and shows the prompt. Write back: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <p><a href="/rss.xml">RSS</a> &middot; <a href="/blogroll.opml">Blogroll OPML</a> &middot; <a href="/llms.txt">llms.txt</a> &middot; <a href="/sitemap.xml">Sitemap</a> &middot; <a href="/colophon.html">Colophon</a></p>
</footer>
</div>
<script>
(function () {{
  var root = document.documentElement, btn = document.getElementById("theme-toggle"),
      meta = document.getElementById("theme-color");
  function show(dark) {{
    btn.textContent = dark ? "light" : "dark";
    btn.setAttribute("aria-label", dark ? "Switch to light reading mode" : "Switch to dark reading mode");
    meta.setAttribute("content", dark ? "#16181d" : "#ffffff");
  }}
  show(root.getAttribute("data-theme") === "dark");
  btn.hidden = false;
  btn.addEventListener("click", function () {{
    var dark = root.getAttribute("data-theme") !== "dark";
    if (dark) root.setAttribute("data-theme", "dark"); else root.removeAttribute("data-theme");
    try {{ localStorage.setItem("weblog-theme", dark ? "dark" : "light"); }} catch (e) {{}}
    show(dark);
  }});
}})();
</script>
</body>
</html>
"""


def sidebar(site, posts):
    months = {}
    for p in posts:
        months.setdefault(f"{p['when']:%Y/%m}", p["when"])
    cats = {}
    for p in posts:
        for c in p["cats"]:
            cats[c] = cats.get(c, 0) + 1
    proj = "".join(
        f'<li><span class="dot dot-{slugify(x["status"])}" title="{e(x["status"])}"></span>'
        f'<a href="/projects.html#{slugify(x["name"])}">{e(x["name"])}</a> <small>{e(x["status"])}</small></li>'
        for x in site["projects"] if x.get("sidebar", True))
    roll = "".join(
        f'<h3>{e(g["group"])}</h3><ul>' + "".join(
            f'<li><a href="{e(b["url"])}" rel="me">{e(b["name"])}</a>'
            + (f' <small>{e(b["note"])}</small>' if b.get("note") else "") + "</li>" for b in g["links"]) + "</ul>"
        for g in site["blogroll"])
    reading = "".join(f'<li><a href="{e(b["url"])}">{e(b["name"])}</a></li>' for b in site["reading"])
    arch = "".join(f'<li><a href="/{k}/">{d:%B %Y}</a></li>' for k, d in months.items())
    catl = "".join(f'<li>{cat_link(c)} <small>({n})</small></li>' for c, n in sorted(cats.items()))
    recent = "".join(f'<li><a href="{p["path"]}">{e(p["title"])}</a></li>' for p in posts[:6])
    return f"""<aside id="sidebar" aria-label="Sidebar">
<section class="box"><h2>About</h2>
<p>I'm Chris Abraham. I do SEO and AI search work for clients and build my own tools with Claude Code. Claude writes every post here from my prompts, and each post shows the prompt. <a href="/about.html">More</a></p></section>
<section class="box"><h2>Recent posts</h2><ul>{recent}</ul></section>
<section class="box"><h2>Projects</h2><ul class="projects">{proj}</ul></section>
<section class="box"><h2>Categories</h2><ul>{catl}</ul></section>
<section class="box"><h2>Archives</h2><ul>{arch}</ul></section>
<section class="box blogroll"><h2>Blogroll</h2>{roll}</section>
<section class="box"><h2>Reading</h2><ul>{reading}</ul><p class="opml"><a href="/blogroll.opml">OPML</a></p></section>
<section class="box buttons" aria-label="Badges">
<a class="badge b-rss" href="/rss.xml"><b>XML</b>RSS 2.0</a>
<a class="badge b-claude" href="/about.html#how"><b>by</b>Claude</a>
<a class="badge b-gh" href="https://github.com/chrisabraham"><b>on</b>GitHub</a>
<span class="badge b-lynx"><b>Lynx</b>friendly</span>
<span class="badge b-html"><b>HTML</b>no JS req.</span>
<a class="badge b-opml" href="/blogroll.opml"><b>OPML</b>blogroll</a>
</section>
</aside>"""


# ---------------------------------------------------------------- post rendering

def post_block(p, *, full, heading="h2"):
    cats = ", ".join(cat_link(c) for c in p["cats"])
    title = (f'<{heading} class="post-title">{e(p["title"])}</{heading}>' if full else
             f'<{heading} class="post-title"><a href="{p["path"]}" rel="bookmark">{e(p["title"])}</a></{heading}>')
    prompt = ""
    if p.get("prompt"):
        prompt = (f'<details class="prompt"{" open" if full else ""}><summary>The prompt</summary>'
                  f'<blockquote>{e(p["prompt"])}</blockquote></details>')
    updated = (f' &middot; updated <time datetime="{p["updated"].isoformat()}">{p["updated"]:%b} {p["updated"].day}</time>'
               if p["updated"] != p["when"] else "")
    return f"""<article class="post" id="{p['slug']}">
{title}
<div class="post-body">
{p['body']}
</div>
{prompt}
<p class="post-footer">Written by {e(p.get('model', 'Claude'))} for {AUTHOR} at
<a href="{p['path']}" rel="bookmark"><time datetime="{p['when'].isoformat()}">{clock(p['when'])}</time></a>{updated}
&middot; filed under {cats or 'nothing'} &middot; <a href="mailto:{EMAIL}?subject={e(p['title'])}">write back</a></p>
</article>"""


def by_day(posts, *, full=False):
    out, last = [], None
    for p in posts:
        day = p["when"].date()
        if day != last:
            if last is not None:
                out.append("</div>")
            out.append(f'<div class="day"><h2 class="date-header">{long_date(p["when"])}</h2>')
            last = day
        out.append(post_block(p, full=full, heading="h3"))
    if posts:
        out.append("</div>")
    return "\n".join(out)


def post_schema(p):
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "@id": p["url"] + "#post",
                "headline": p["title"],
                "description": p["description"],
                "url": p["url"],
                "mainEntityOfPage": p["url"],
                "datePublished": p["when"].isoformat(),
                "dateModified": p["updated"].isoformat(),
                "author": {"@id": PERSON["@id"]},
                "publisher": {"@id": PERSON["@id"]},
                "isPartOf": {"@id": SITE_URL + "/#blog"},
                "keywords": p["cats"],
                "articleSection": p["cats"][0] if p["cats"] else None,
                "wordCount": len(text_only(p["body"]).split()),
                "inLanguage": "en-US",
                "creditText": f"Written by {p.get('model', 'Claude')} from {AUTHOR}'s prompt",
            },
            PERSON,
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": "Archives", "item": SITE_URL + "/archives.html"},
                {"@type": "ListItem", "position": 3, "name": p["title"], "item": p["url"]},
            ]},
        ],
    }


# ---------------------------------------------------------------- build

def write(path, text):
    f = OUT / path.lstrip("/")
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def main():
    site = json.loads((SRC / "site.json").read_text(encoding="utf-8"))
    PERSON["sameAs"] = [x["url"] for g in site["blogroll"] for x in g["links"]
                        if "calendly" not in x["url"] and "slowjogging" not in x["url"]]
    posts = load_posts()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    sitemap = []  # (path, lastmod)
    P = dict(site=site, posts=posts)

    # Home
    home_schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": SITE_URL + "/#blog", "name": TITLE, "description": TAGLINE,
         "url": SITE_URL + "/", "author": {"@id": PERSON["@id"]}, "inLanguage": "en-US",
         "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": p["url"],
                       "datePublished": p["when"].isoformat()} for p in posts[:HOME_POSTS]]},
        {"@type": "WebSite", "@id": SITE_URL + "/#site", "name": TITLE, "url": SITE_URL + "/",
         "publisher": {"@id": PERSON["@id"]}},
        PERSON]}
    older = '<p class="older"><a href="/archives.html">Older posts are in the archives</a></p>' if len(posts) > HOME_POSTS else ""
    write("/index.html", page(title=TITLE, description=TAGLINE, path="/index.html",
                              body=by_day(posts[:HOME_POSTS]) + older, schema=home_schema, **P))
    sitemap.append(("/", posts[0]["updated"] if posts else None))

    # Posts
    for i, p in enumerate(posts):
        newer, older_p = (posts[i - 1] if i else None), (posts[i + 1] if i + 1 < len(posts) else None)
        nav = '<nav class="prevnext" aria-label="More posts">'
        if older_p:
            nav += f'<a href="{older_p["path"]}" rel="prev">&laquo; {e(older_p["title"])}</a>'
        nav += '<a href="/">Main page</a>'
        if newer:
            nav += f'<a href="{newer["path"]}" rel="next">{e(newer["title"])} &raquo;</a>'
        nav += "</nav>"
        body = f'<div class="day"><p class="date-header">{long_date(p["when"])}</p>{post_block(p, full=True, heading="h1")}</div>{nav}'
        extra = (f'<meta property="article:published_time" content="{p["when"].isoformat()}">\n'
                 f'<meta property="article:modified_time" content="{p["updated"].isoformat()}">\n'
                 + "".join(f'<meta property="article:tag" content="{e(c)}">\n' for c in p["cats"]))
        write(p["path"], page(title=p["title"], description=p["description"], path=p["path"], body=body,
                              schema=post_schema(p), og_type="article", extra_head=extra, **P))
        sitemap.append((p["path"], p["updated"]))

    # Monthly and category archives: they repeat posts, so noindex, follow.
    months = {}
    for p in posts:
        months.setdefault(f"{p['when']:%Y/%m}", []).append(p)
    for key, ps in months.items():
        label = f"{ps[0]['when']:%B %Y}"
        write(f"/{key}/index.html", page(title=f"Posts from {label}", description=f"Every weblog post from {label}.",
              path=f"/{key}/index.html", body=f'<h1 class="page-title">{label}</h1>' + by_day(ps, full=True),
              noindex=True, **P))
    cats = {}
    for p in posts:
        for c in p["cats"]:
            cats.setdefault(c, []).append(p)
    for c, ps in cats.items():
        write(f"/category/{slugify(c)}.html", page(title=f"Posts about {c}", description=f"Weblog posts filed under {c}.",
              path=f"/category/{slugify(c)}.html", body=f'<h1 class="page-title">Filed under {e(c)}</h1>' + by_day(ps),
              noindex=True, **P))

    # Archives list: one line per post, indexable since it is only titles.
    lines, cur = [], None
    for p in posts:
        m = f"{p['when']:%B %Y}"
        if m != cur:
            if cur:
                lines.append("</ul>")
            lines.append(f'<h2><a href="/{p["when"]:%Y/%m}/">{m}</a></h2><ul class="archive-list">')
            cur = m
        lines.append(f'<li><time datetime="{p["when"].date()}">{p["when"]:%b} {p["when"].day}</time> '
                     f'<a href="{p["path"]}">{e(p["title"])}</a></li>')
    if cur:
        lines.append("</ul>")
    write("/archives.html", page(title="Archives of the Chris Abraham Weblog", description="Every post on the Chris Abraham Weblog by month, from Blackbox to Claude Code to client work, written by Claude from his prompts.",
          path="/archives.html", body='<h1 class="page-title">Archives</h1>' + "\n".join(lines), **P))
    sitemap.append(("/archives.html", posts[0]["updated"] if posts else None))

    # Projects
    rows = []
    for x in site["projects"]:
        link = f'<a href="{e(x["url"])}">{e(x["url"].split("//")[-1].rstrip("/"))}</a>' if x.get("url") else "private"
        rows.append(f"""<section class="project" id="{slugify(x['name'])}">
<h2><span class="dot dot-{slugify(x['status'])}"></span>{e(x['name'])}</h2>
<p class="project-meta">{e(x['status'])} &middot; started {e(x['started'])} &middot; {link}</p>
<p>{x['about']}</p></section>""")
    projects_schema = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Projects",
                       "url": SITE_URL + "/projects.html", "author": {"@id": PERSON["@id"]},
                       "hasPart": [{"@type": "CreativeWork", "name": x["name"], "url": x.get("url") or None,
                                    "creativeWorkStatus": x["status"]} for x in site["projects"]]}
    write("/projects.html", page(title="Projects Chris Abraham is building now", description="What Chris Abraham is building and running right now, from Blackbox to his podcast site, with the status of each project kept current.",
          path="/projects.html", schema=projects_schema,
          body='<h1 class="page-title">Projects</h1><p class="lede">What I am building, running, or planning, with an honest status for each. Posts about a project link back here.</p>' + "\n".join(rows), **P))
    sitemap.append(("/projects.html", None))

    # Static pages
    for f in sorted((SRC / "pages").glob("*.html")):
        m = parse(f)
        check_meta(f.name, m)
        path = f"/{f.stem}.html"
        schema = {"@context": "https://schema.org", "@type": m.get("schema", "WebPage"), "name": m["title"],
                  "url": SITE_URL + path, "description": m["description"],
                  "mainEntity" if m.get("schema") == "ProfilePage" else "author": PERSON}
        write(path, page(title=m["title"], description=m["description"], path=path, schema=schema,
                         body=f'<h1 class="page-title">{e(m["title"])}</h1><div class="post-body">{m["body"]}</div>',
                         noindex=f.stem == "404", **P))
        if f.stem != "404":
            sitemap.append((path, None))

    # Feeds and machine files
    write("/rss.xml", rss(posts))
    write("/blogroll.opml", opml(site))
    write("/sitemap.xml", "".join([
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n',
        *(f"<url><loc>{SITE_URL}{p}</loc>{f'<lastmod>{d.date()}</lastmod>' if d else ''}</url>\n" for p, d in sitemap),
        "</urlset>\n"]))
    write("/robots.txt", ROBOTS.replace("{SITE}", SITE_URL))
    write("/llms.txt", llms(posts, site, full=False))
    write("/llms-full.txt", llms(posts, site, full=True))
    write("/favicon.svg", FAVICON)
    write(f"/{INDEXNOW_KEY}.txt", INDEXNOW_KEY)
    write("/CNAME", SITE_URL.split("//")[1] + "\n")
    write("/.nojekyll", "")
    print(f"built {len(posts)} posts, {len(sitemap)} sitemap URLs into docs/")


def rss(posts):
    items = []
    for p in posts[:30]:
        body = p["body"]
        if p.get("prompt"):
            body += f"<p><em>Written by {e(p.get('model', 'Claude'))} from this prompt:</em></p><blockquote>{e(p['prompt'])}</blockquote>"
        items.append(f"""<item>
<title>{e(p['title'])}</title>
<link>{p['url']}</link>
<guid isPermaLink="true">{p['url']}</guid>
<pubDate>{p['when'].strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate>
<description>{e(p['description'])}</description>
{''.join(f'<category>{e(c)}</category>' for c in p['cats'])}
<content:encoded><![CDATA[{body.replace(']]>', ']]&gt;')}]]></content:encoded>
</item>""")
    last = posts[0]["when"].strftime('%a, %d %b %Y %H:%M:%S %z') if posts else ""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<title>{e(TITLE)}</title>
<link>{SITE_URL}/</link>
<atom:link href="{SITE_URL}/rss.xml" rel="self" type="application/rss+xml"/>
<description>{e(TAGLINE)}</description>
<language>en-us</language>
<lastBuildDate>{last}</lastBuildDate>
<docs>https://cyber.harvard.edu/rss/rss.html</docs>
<generator>build.py, written by Claude</generator>
{chr(10).join(items)}
</channel>
</rss>
"""


def opml(site):
    def row(b):
        if b.get("feed"):
            return f'<outline text="{e(b["name"])}" type="rss" htmlUrl="{e(b["url"])}" xmlUrl="{e(b["feed"])}"/>\n'
        return f'<outline text="{e(b["name"])}" type="link" url="{e(b["url"])}"/>\n'
    outl = "".join(f'<outline text="{e(g["group"])}">\n' + "".join(row(b) for b in g["links"]) + "</outline>\n"
                   for g in site["blogroll"])
    outl += '<outline text="Reading">\n' + "".join(row(b) for b in site["reading"]) + "</outline>\n"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
<head><title>{e(AUTHOR)}'s blogroll</title><ownerName>{AUTHOR}</ownerName><docs>http://opml.org/spec2.opml</docs></head>
<body>
{outl}</body>
</opml>
"""


def llms(posts, site, *, full):
    out = [f"# {TITLE}", "", f"> {TAGLINE}", "",
           f"{AUTHOR}'s personal weblog about working with AI: Blackbox (his command-line secretary), Claude, Claude Code, ChatGPT, OpenAI Codex, GitHub, and anonymized client work. "
           "Claude writes every post from Chris' prompts; each post names the model and shows the prompt.", "",
           "## Pages", "",
           f"- [About]({SITE_URL}/about.html): who Chris is and how this weblog gets written",
           f"- [Projects]({SITE_URL}/projects.html): what he is building, with status",
           f"- [Archives]({SITE_URL}/archives.html): every post by month",
           f"- [RSS]({SITE_URL}/rss.xml)", "", "## Posts", ""]
    for p in posts:
        out.append(f"- [{p['title']}]({p['url']}) ({p['when'].date()}): {p['description']}")
    if full:
        for p in posts:
            out += ["", "---", "", f"# {p['title']}", "", f"{p['url']} · {p['when'].date()} · {p.get('model', 'Claude')}", "",
                    text_only(p["body"])]
            if p.get("prompt"):
                out += ["", f"Prompt: {p['prompt']}"]
    return "\n".join(out) + "\n"


ROBOTS = """# Search engines and AI assistants are welcome to read and cite everything here.
# llms-full.txt repeats the posts word for word, so search indexes skip it.
User-agent: *
Allow: /

User-agent: Googlebot
User-agent: Bingbot
User-agent: Applebot
User-agent: DuckDuckBot
User-agent: YandexBot
Allow: /
Disallow: /llms-full.txt

User-agent: GPTBot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: Amazonbot
User-agent: DuckAssistBot
User-agent: MistralAI-User
User-agent: CCBot
User-agent: GoogleOther
User-agent: Google-CloudVertexBot
User-agent: Google-Agent
User-agent: Google-GeminiNotebook
User-agent: meta-webindexer
User-agent: meta-externalagent
User-agent: meta-externalfetcher
User-agent: Amzn-SearchBot
User-agent: Amzn-User
Allow: /

Sitemap: {SITE}/sitemap.xml
"""

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><rect width="16" height="16" fill="#c75000"/>'
           '<text x="8" y="12.5" font-family="Verdana,sans-serif" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">c</text></svg>')

CSS = (ROOT / "src" / "style.css").read_text(encoding="utf-8") if (ROOT / "src" / "style.css").exists() else ""

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the Chris Abraham weblog into docs/ (GitHub Pages serves main:/docs).

Standard library only. Sources:
  src/posts/YYYY-MM-DD-slug.html  key: value header, a line of ---, then HTML
  src/pages/<name>.html           same format, for About, Colophon, etc.
  src/site.json                   elsewhere (my own sites and profiles), reading (the blogroll), projects

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
TITLE = "Chris Abraham weblog"
HOME_TITLE = "Chris Abraham, a weblog on building with AI and Claude Code"
HOME_DESCRIPTION = "Chris Abraham's weblog on Blackbox, Claude Code, ChatGPT, Codex, GitHub, and client work, written by AI from his prompts, with every prompt shown."
TAGLINE = "Notes from building things with AI, written by AI from my prompts."
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
  var off = {analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'};
  // EU, EEA, UK, and Swiss visitors get no analytics cookies (cookieless pings only).
  gtag('consent', 'default', Object.assign({region: ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','IS','LI','NO','GB','CH']}, off));
  // Everyone else gets first-party analytics cookies and nothing for ads, unless the browser
  // sends Global Privacy Control or Do Not Track, which turns analytics cookies off too.
  var optout = navigator.globalPrivacyControl === true || navigator.doNotTrack === '1';
  gtag('consent', 'default', optout ? off : {analytics_storage: 'granted', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'});
  gtag('js', new Date());
  gtag('config', '{id}', {allow_google_signals: false, allow_ad_personalization_signals: false});
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

AUTHORS = {
    "chris": {"name": "Chris Abraham", "path": "/authors/chris-abraham.html", "type": "Person"},
    "claude-code": {"name": "Claude Code", "path": "/authors/claude-code.html", "type": "Organization",
                    "description": "Anthropic's AI coding agent, writing in its own voice on this weblog",
                    "organization": "Anthropic", "organization_url": "https://www.anthropic.com/"},
    "chatgpt": {"name": "ChatGPT", "path": "/authors/chatgpt.html", "type": "Organization",
                "description": "OpenAI's ChatGPT assistant, an independently attributed weblog author",
                "organization": "OpenAI", "organization_url": "https://openai.com/"},
}


def author_ref(key):
    a = AUTHORS.get(key or "chris", AUTHORS["chris"])
    if a["type"] == "Person":
        return AUTHOR_REF
    return {"@type": "Organization", "name": a["name"], "url": SITE_URL + a["path"], "description": a["description"],
            "parentOrganization": {"@type": "Organization", "name": a["organization"], "url": a["organization_url"]}}


AUTHOR_REF = {"@type": "Person", "@id": SITE_URL + "/about.html#chris", "name": AUTHOR, "url": SITE_URL + "/about.html"}

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
    meta["body"] = youtube(dashes(body.strip()))
    return meta


YOUTUBE = re.compile(r"\{\{youtube:([A-Za-z0-9_-]{6,20})\|([^}]+)\}\}")


def youtube(body):
    """{{youtube:ID|Title}} becomes a click-to-play facade: a link and thumbnail until the
    reader presses play, then a youtube-nocookie.com player. Nothing loads from YouTube first."""
    def sub(m):
        vid, title = m.group(1), html.escape(m.group(2))
        return (f'<figure class="video" data-yt="{vid}"><a class="video-link" href="https://www.youtube.com/watch?v={vid}">'
                f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="Video: {title}" width="480" height="360" loading="lazy">'
                f'<span class="video-play" aria-hidden="true">\u25b6</span></a>'
                f'<figcaption>Video: {title}. Plays from YouTube when you press play.</figcaption></figure>')
    return YOUTUBE.sub(sub, body)


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



REPO = "https://github.com/chrisabraham/weblog"
# Link titles in wiki-style notation can refer to canonical posts as well as wiki pages.
# Resolve post targets to their actual permalink, not an unrelated wiki index.
POST_LINKS = {}
WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def load_wiki():
    pages = {}
    for path in sorted((SRC / "wiki").glob("*.html")):
        m = parse(path)
        check_meta("wiki/" + path.name, m)
        m["slug"] = path.stem
        m["path"] = f"/wiki/{path.stem}.html"
        m["url"] = SITE_URL + m["path"]
        m["src"] = f"src/wiki/{path.name}"
        m["cats"] = [c.strip() for c in m.get("categories", "").split(",") if c.strip()]
        m["edited"] = dt.date.fromisoformat(m["updated"])
        m["info"] = [(k[5:], v) for k, v in m.items() if k.startswith("info.")]
        pages[m["slug"]] = m
    return pages


def wikilinks(body, wiki, found):
    """[[Page]] or [[Page|text]] becomes a link; a missing page is a red link, like a real wiki."""
    def sub(mt):
        target, text = mt.group(1).strip(), (mt.group(2) or mt.group(1)).strip()
        slug = slugify(target)
        found.add(slug)
        if slug in wiki:
            return f'<a href="/wiki/{slug}.html" class="wikilink">{e(text)}</a>'
        if slug in POST_LINKS:
            return f'<a href="{POST_LINKS[slug]}" class="postlink">{e(text)}</a>'
        return f'<a href="/wiki/" class="wikilink new" title="{e(target)} (page does not exist yet)">{text}</a>'
    return WIKILINK.sub(sub, body)


def add_toc(body):
    heads, n = [], [0, 0]
    def sub(mt):
        level, inner = mt.group(1), mt.group(2)
        hid = slugify(re.sub(r"<[^>]+>", "", inner))
        if level == "2":
            n[0] += 1; n[1] = 0; num = f"{n[0]}"
        else:
            n[1] += 1; num = f"{n[0]}.{n[1]}"
        heads.append((level, num, hid, re.sub(r"<[^>]+>", "", inner)))
        return f'<h{level} id="{hid}">{inner}</h{level}>'
    body = re.sub(r"<h([23])>(.*?)</h\1>", sub, body)
    if len(heads) < 3:
        return body, ""
    items = "".join(f'<li class="toc-{lv}"><a href="#{hid}"><span class="tocnum">{num}</span><span class="toctext">{e(t)}</span></a></li>'
                    for lv, num, hid, t in heads)
    return body, f'<nav class="toc" aria-label="Contents"><p class="toc-title">Contents</p><ol>{items}</ol></nav>'


AMAZON_TAG = "gerris-20"
AMAZON_NOTE = '<p class="disclosure">As an Amazon Associate I earn from qualifying purchases. <a href="/disclosures.html#affiliate-links">About affiliate links</a></p>'


def affiliate(body):
    """Tag every Amazon link with gerris-20 and rel=sponsored; return (body, has_affiliate)."""
    found = [False]
    def sub(mt):
        tag = mt.group(0)
        href = re.search(r'href="([^"]+)"', tag).group(1)
        if not re.match(r"https?://(www\.)?(amazon\.com|amzn\.to)/", href):
            return tag
        found[0] = True
        if "amazon.com" in href and "tag=" not in href:
            new = href + ("&amp;" if "?" in href else "?") + "tag=" + AMAZON_TAG
            tag = tag.replace(f'href="{href}"', f'href="{new}"')
        tag = re.sub(r'\srel="[^"]*"', "", tag)
        return tag[:-1] + ' rel="sponsored noopener">'
    body = re.sub(r"<a\s[^>]*href=\"[^\"]+\"[^>]*>", sub, body)
    return body, found[0]

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



FONT_DIR = ROOT / "fonts"
CARD_CACHE = {}


def px(text, size):
    """Rendered width in Arial-metric Liberation Sans, the way Screaming Frog measures snippets."""
    try:
        from PIL import ImageFont
    except ImportError:
        return 0
    key = ("px", size)
    if key not in CARD_CACHE:
        CARD_CACHE[key] = ImageFont.truetype(str(FONT_DIR / "LiberationSans-Regular.ttf"), size)
    return int(CARD_CACHE[key].getlength(text))


def make_card(path, title, kicker):
    """A 1200x630 share card per page: name in orange, kicker in Gerris blue, title in black."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        if not CARD_CACHE.get("warned"):
            print("  warn: Pillow missing, no share cards (run with ~/.venvs/site/bin/python)")
            CARD_CACHE["warned"] = True
        return None
    name = path.strip("/").replace("/", "-").replace(".html", "") or "home"
    name = name.replace("-index", "") or "home"
    out = OUT / "cards" / f"{name}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    W, H, M = 1200, 630, 72
    im = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(im)
    bold = lambda s: ImageFont.truetype(str(FONT_DIR / "DejaVuSans-Bold.ttf"), s)
    reg = lambda s: ImageFont.truetype(str(FONT_DIR / "DejaVuSans.ttf"), s)
    d.rectangle([0, 0, W, 14], fill="#c75000")
    d.text((M, 64), TITLE, font=bold(58), fill="#c75000")
    d.text((M, 146), kicker, font=reg(30), fill="#16729e")
    def wrap(f, width):
        lines, cur = [], ""
        for w in title.split():
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) <= width or not cur:
                cur = t
            else:
                lines.append(cur); cur = w
        return lines + [cur]
    size = 64
    while True:
        f = bold(size)
        lines = wrap(f, W - 2 * M)
        if len(lines) <= 4 or size <= 40:
            break
        size -= 4
    # Balance: narrow the measure while the line count holds, so no last line is a lone word.
    width = W - 2 * M
    while width > 300 and len(wrap(f, width - 10)) == len(lines):
        width -= 10
    lines = wrap(f, width)
    y = 230
    for ln in lines[:4]:
        d.text((M, y), ln, font=f, fill="#1b1b1b")
        y += int(size * 1.25)
    d.line([M, H - 96, W - M, H - 96], fill="#c9d0dc", width=2)
    d.line([M, H - 90, W - M, H - 90], fill="#c9d0dc", width=2)
    d.text((M, H - 74), SITE_URL.split("//")[1], font=bold(28), fill="#1d3d8f")
    d.text((W - M, H - 74), "Written by AI from my prompts", font=reg(26), fill="#474d58", anchor="ra")
    im.save(out, optimize=True)
    return f"{SITE_URL}/cards/{name}.png"

# ---------------------------------------------------------------- page shell

def page(*, title, description, path, body, site, posts, schema=None,
         noindex=False, og_type="website", extra_head="", seo_title=None, kicker=None):
    canonical = SITE_URL + path.replace("index.html", "")
    full_title = HOME_TITLE if path == "/index.html" else (seo_title or title)
    if not noindex:
        tw, dw = px(full_title, 20), px(description, 13)
        if tw > 561:
            print(f"  warn {path}: title is {tw}px wide (Screaming Frog limit 561px): {full_title}")
        if dw > 985:
            print(f"  warn {path}: description is {dw}px wide (limit 985px)")
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
        if path != "/index.html" and h1 and re.sub(r"<[^>]+>", "", h1.group(1)).strip() == full_title:
            print(f"  warn {path}: title is the same as the H1")
        if len(re.findall(r"<h1[\s>]", body)) + (path == "/index.html") != 1:
            print(f"  warn {path}: page should have exactly one H1")
        if not 45 <= len(full_title) <= 60:
            print(f"  warn {path}: title is {len(full_title)} chars (aim 50-60): {full_title}")
        if not 120 <= len(description) <= 155:
            print(f"  warn {path}: description is {len(description)} chars (aim 120-160)")
        if re.search(r" [-\u2013\u2014|] |\|", full_title + description):
            print(f"  warn {path}: separator dash or pipe in title or description")
    card_title = "A weblog about building with AI, Blackbox, and Claude Code" if path == "/index.html" else title
    img = make_card(path, card_title, kicker or ("Weblog" if path == "/index.html" else SITE_URL.split("//")[1]))
    img_alt = f"{TITLE}: {card_title}"
    if img and isinstance(schema, dict):
        target = next((n for n in schema.get("@graph", [schema]) if n.get("@type") in ("BlogPosting", "Article", "Blog", "WebPage", "ProfilePage", "CollectionPage")), None)
        if target is not None:
            target["image"] = {"@type": "ImageObject", "url": img, "width": 1200, "height": 630}
    cards = (f"""<meta property="og:image" content="{img}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(img_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{img}">
<meta name="twitter:image:alt" content="{e(img_alt)}">
""" if img else '<meta name="twitter:card" content="summary">\n')
    rel_me = "".join(f'<link rel="me" href="{e(x["url"])}">\n' for g in site["elsewhere"] if g["group"] == "Find me"
                     for x in g["links"] if "calendly" not in x["url"])
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
<meta name="generator" content="build.py, written with AI in Claude Code">
<meta name="theme-color" content="#ffffff" id="theme-color">
<meta name="referrer" content="strict-origin-when-cross-origin">
<link rel="canonical" href="{canonical}">
<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
<link rel="alternate" type="application/rss+xml" title="{e(TITLE)} (RSS)" href="{SITE_URL}/rss.xml">
<link rel="blogroll" type="text/x-opml" href="{SITE_URL}/blogroll.opml">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:site_name" content="{e(TITLE)}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_US">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(description)}">
{cards}{rel_me}<link rel="author" href="{SITE_URL}/humans.txt">
{extra_head}<style>{CSS}</style>
{ld(schema) if schema else ""}
{SPECULATION}
{GA.replace("{id}", GA_ID) if GA_ID else ""}
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<div id="wrap">
<header id="banner">
  <button type="button" class="theme-toggle" id="theme-toggle" hidden>dark</button>
  <{"h1" if path == "/index.html" else "p"} class="site-title"><a href="/" rel="home">{e(TITLE)}</a></{"h1" if path == "/index.html" else "p"}>
  <p class="tagline">{e(TAGLINE)}</p>
  <nav class="topnav" aria-label="Main">
    <a href="/">Home</a> <a href="/projects.html">Projects</a> <a href="/wiki/">Wiki</a> <a href="/archives.html">Archives</a>
    <a href="/about.html">About</a> <a href="/reading.html">Reading</a>
    <a href="/hire.html" class="hire-tab">Hire me</a>
  </nav>
</header>
<div id="cols">
<main id="main"{' class="h-feed"' if path == "/index.html" else ""}>
{body}
</main>
{sidebar(site, posts)}
</div>
<footer id="footer">
  <p>Copyright {dt.date.today().year} {AUTHOR}. AI writes every post here from my prompts, and each post names the model and shows the&nbsp;prompt.</p>
  <p>Except where noted, the writing and original images on this weblog are licensed <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>: take them, remix them, credit Chris Abraham, and link back. <a href="/disclosures.html#license">What is excluded</a>.</p>
  <p>Write back: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <nav class="footlinks" aria-label="Site files"><a href="/rss.xml">RSS</a> <a href="/blogroll.opml">Blogroll OPML</a> <a href="/llms.txt">llms.txt</a> <a href="/sitemap.xml">Sitemap</a> <a href="/now.html">Now</a> <a href="/colophon.html">Colophon</a> <a href="/privacy.html">Privacy</a> <a href="/disclosures.html">Disclosures</a> <a href="/accessibility.html">Accessibility</a></nav>
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
  document.querySelectorAll("figure.video a.video-link").forEach(function (a) {{
    a.addEventListener("click", function (ev) {{
      ev.preventDefault();
      var f = a.parentNode, i = document.createElement("iframe");
      i.src = "https://www.youtube-nocookie.com/embed/" + f.getAttribute("data-yt") + "?autoplay=1";
      i.title = a.querySelector("img").alt; i.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      i.setAttribute("allowfullscreen", ""); i.loading = "lazy";
      f.replaceChild(i, a);
    }});
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
        for g in site["elsewhere"])
    nfeeds = sum(1 for g in site["reading"] for x in g["links"] if x.get("feed"))
    reading = "".join(f'<li><a href="{e(b["url"])}">{e(b["name"])}</a></li>' for b in site["reading"][0]["links"])
    arch = "".join(f'<li><a href="/{k}/">{d:%B %Y}</a></li>' for k, d in months.items())
    catl = "".join(f'<li>{cat_link(c)} <small>({n})</small></li>' for c, n in sorted(cats.items()))
    recent = "".join(f'<li><a href="{p["path"]}">{e(p["title"])}</a></li>' for p in posts[:6])
    wikil = "".join(f'<li><a href="{w["path"]}">{e(w["title"])}</a></li>'
                    for w in sorted(site.get("_wiki", {}).values(), key=lambda w: w["title"].lower()))
    return f"""<aside id="sidebar" aria-label="Sidebar">
<section class="box" aria-labelledby="sb-authors"><p class="box-title" id="sb-authors">Authors</p><ul><li><a href="/authors/chris-abraham.html">Chris Abraham</a> <small>the human</small></li><li><a href="/authors/claude-code.html">Claude Code</a> <small>Anthropic</small></li><li><a href="/authors/chatgpt.html">ChatGPT</a> <small>OpenAI</small></li></ul></section>
<section class="box" aria-labelledby="sb-about"><p class="box-title" id="sb-about">About</p>
<p>I'm Chris Abraham. I do SEO and AI search work for clients and build my own tools with Claude Code. AI writes every post here from my prompts, and each post shows the prompt. <a href="/about.html">More about me and this weblog</a> &middot; <a href="/now.html">What I'm doing now</a></p></section>
<section class="box" aria-labelledby="sb-recent-posts"><p class="box-title" id="sb-recent-posts">Recent posts</p><ul>{recent}</ul></section>
<section class="box" aria-labelledby="sb-wiki"><p class="box-title" id="sb-wiki">Wiki</p><ul>{wikil}</ul><p class="opml"><a href="/wiki/">All wiki pages</a></p></section>
<section class="box" aria-labelledby="sb-projects"><p class="box-title" id="sb-projects">Projects</p><ul class="projects">{proj}</ul></section>
<section class="box" aria-labelledby="sb-categories"><p class="box-title" id="sb-categories">Categories</p><ul>{catl}</ul></section>
<section class="box" aria-labelledby="sb-archives"><p class="box-title" id="sb-archives">Archives</p><ul>{arch}</ul></section>
<section class="box" aria-labelledby="sb-blogroll"><p class="box-title" id="sb-blogroll">Blogroll</p><ul>{reading}</ul><p><a href="/reading.html">The full reading list: {nfeeds} feeds on SEO, AI search, AI labs, and policy</a></p><p class="opml"><a href="/blogroll.opml">OPML</a></p></section>
<section class="box blogroll" aria-labelledby="sb-elsewhere"><p class="box-title" id="sb-elsewhere">Elsewhere</p>{roll}</section>
<section class="box buttons" aria-label="Badges">
<a class="badge b-rss" href="/rss.xml"><b>XML</b>RSS 2.0</a>
<a class="badge b-claude" href="/about.html#how"><b>by</b>AI</a>
<a class="badge b-gh" href="https://github.com/chrisabraham"><b>on</b>GitHub</a>
<span class="badge b-lynx"><b>Lynx</b>friendly</span>
<span class="badge b-html"><b>HTML</b>no JS req.</span>
<a class="badge b-wcag" href="/accessibility.html"><b>WCAG</b>2.1 AA</a>
<a class="badge b-lh" href="/accessibility.html#what-was-checked"><b>a11y</b>100/100</a>
<a class="badge b-opml" href="/blogroll.opml"><b>OPML</b>blogroll</a>
<a class="badge b-cc" rel="license" href="https://creativecommons.org/licenses/by/4.0/"><b>cc</b>BY 4.0</a>
</section>
</aside>"""


# ---------------------------------------------------------------- post rendering

def post_block(p, *, full, heading="h2"):
    cats = ", ".join(cat_link(c) for c in p["cats"])
    title = (f'<{heading} class="post-title p-name">{e(p["title"])}</{heading}>' if full else
             f'<{heading} class="post-title p-name"><a href="{p["path"]}" rel="bookmark" class="u-url">{e(p["title"])}</a></{heading}>')
    prompt = ""
    # Only full canonical articles display original prompts; excerpts stay light.
    if full and p.get("prompt"):
        ph = "h2" if heading == "h1" else "h4"
        prompt = (f'<details class="prompt"{" open" if full else ""}><summary><{ph} class="prompt-h">The prompt for \u201c{e(p["title"])}\u201d</{ph}></summary>'
                  f'<blockquote>{e(p["prompt"])}</blockquote></details>')
    words = len(text_only(p["body"]).split())
    readtime = f'{words:,} words, about {max(1, round(words / 230))} min read'
    updated = (f' &middot; updated <time datetime="{p["updated"].isoformat()}">{p["updated"]:%b} {p["updated"].day}</time>'
               if p["updated"] != p["when"] else "")
    # Lotus rule: simplify, then add lightness. Indexes show one meaningful excerpt.
    # Metadata summaries are HTML-safe plain text, never truncated arbitrary markup.
    if full:
        body = p["body"]
    else:
        body = (f'<p class="post-excerpt">{e(p["description"])}</p>'
                f'<p class="read-more"><a href="{p["path"]}" '
                f'aria-label="Read full article: {e(p["title"], quote=True)}">Read full article &rarr;</a></p>')
    return f"""<article class="post h-entry" id="{p['slug']}">
{title}
<div class="post-body e-content">
{body}
</div>
{prompt}
<p class="post-footer">{byline(p)} at
<a href="{p['path']}" rel="bookmark" class="u-url"><time class="dt-published" datetime="{p['when'].isoformat()}">{clock(p['when'])}</time></a>{updated}
&middot; {readtime} &middot; filed under {cats or 'nothing'} &middot; <a href="mailto:{EMAIL}?subject={e(p['title'])}">write back</a></p>
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


def byline(p):
    if p.get("author") in ("claude-code", "chatgpt"):
        a = AUTHORS[p["author"]]
        return (f'By <a class="p-author h-card" href="{a["path"]}">{e(a["name"])}</a>, in its own voice '
                f'({e(p.get("model", "AI"))}), for {AUTHOR}\'s weblog')
    return (f'Written by {e(p.get("model", "Claude"))} for '
            f'<a class="p-author h-card" href="/authors/chris-abraham.html">{AUTHOR}</a>')


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
                "author": author_ref(p.get("author")),
                "publisher": AUTHOR_REF,
                "isPartOf": {"@id": SITE_URL + "/#blog"},
                "keywords": p["cats"],
                "articleSection": p["cats"][0] if p["cats"] else None,
                "wordCount": len(text_only(p["body"]).split()),
                "inLanguage": "en-US",
                "isAccessibleForFree": True,
                "creditText": (f"Written by {AUTHORS[p['author']]['name']} ({p.get('model', 'AI')}) in its own voice, at {AUTHOR}'s request"
                               if p.get("author") in ("claude-code", "chatgpt") else f"Written by {p.get('model', 'Claude')} from {AUTHOR}'s prompt"),
                "publishingPrinciples": SITE_URL + "/disclosures.html",
                "license": "https://creativecommons.org/licenses/by/4.0/",
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
    PERSON["sameAs"] = [x["url"] for g in site["elsewhere"] for x in g["links"]
                        if "calendly" not in x["url"] and "slowjogging" not in x["url"]]
    posts = load_posts()
    POST_LINKS.clear()
    POST_LINKS.update({slugify(p["title"]): p["path"] for p in posts})
    wiki = load_wiki()
    site["_wiki"] = wiki
    links_to = {}  # slug -> list of (title, path) that link to it
    for p in posts + list(wiki.values()):
        found = set()
        p["body"] = wikilinks(p["body"], wiki, found)
        p["body"], aff = affiliate(p["body"])
        if aff or p.get("affiliate") == "yes":
            p["body"] += AMAZON_NOTE if aff else '<p class="disclosure">This page contains affiliate links; I may earn a commission. <a href="/disclosures.html#affiliate-links">About affiliate links</a></p>'
        if "info" in p:
            p["info"] = [(k, wikilinks(v, wiki, found)) for k, v in p["info"]]
        for s in found:
            if s != p.get("slug") or p["path"].startswith("/20"):
                links_to.setdefault(s, []).append((p["title"], p["path"]))
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    sitemap = []  # (path, lastmod)
    P = dict(site=site, posts=posts)

    # Home
    home_schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": SITE_URL + "/#blog", "name": TITLE, "description": TAGLINE,
         "url": SITE_URL + "/", "author": AUTHOR_REF, "inLanguage": "en-US",
         "publishingPrinciples": SITE_URL + "/disclosures.html",
         "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": p["url"],
                       "datePublished": p["when"].isoformat()} for p in posts[:HOME_POSTS]]},
        {"@type": "WebSite", "@id": SITE_URL + "/#site", "name": TITLE, "url": SITE_URL + "/",
         "publisher": AUTHOR_REF},
        PERSON]}
    older = '<p class="older"><a href="/archives.html">Older posts are in the archives</a></p>' if len(posts) > HOME_POSTS else ""
    write("/index.html", page(title=TITLE, description=HOME_DESCRIPTION, path="/index.html",
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
        shared = sorted((q for q in posts if q is not p),
                        key=lambda q: (-len(set(q["cats"]) & set(p["cats"])), -q["when"].timestamp()))[:3]
        related = ('<section class="related" aria-labelledby="rel-h"><h2 id="rel-h">Related posts</h2><ul>'
                   + "".join(f'<li><a href="{q["path"]}">{e(q["title"])}</a> <small>{q["when"]:%b} {q["when"].day}</small></li>' for q in shared)
                   + "</ul></section>") if shared else ""
        body = f'<div class="day"><p class="date-header">{long_date(p["when"])}</p>{post_block(p, full=True, heading="h1")}</div>{related}{nav}'
        extra = (f'<meta property="article:published_time" content="{p["when"].isoformat()}">\n'
                 f'<meta property="article:modified_time" content="{p["updated"].isoformat()}">\n'
                 + "".join(f'<meta property="article:tag" content="{e(c)}">\n' for c in p["cats"]))
        write(p["path"], page(title=p["title"], description=p["description"], path=p["path"], body=body,
                              seo_title=p.get("seo_title"), kicker=f"Weblog \u00b7 {long_date(p['when'])}",
                              schema=post_schema(p), og_type="article", extra_head=extra, **P))
        sitemap.append((p["path"], p["updated"]))

    # Monthly and category archives: they repeat posts, so noindex, follow.
    months = {}
    for p in posts:
        months.setdefault(f"{p['when']:%Y/%m}", []).append(p)
    for key, ps in months.items():
        label = f"{ps[0]['when']:%B %Y}"
        write(f"/{key}/index.html", page(title=f"Posts from {label}", description=f"Every post on Chris Abraham's weblog from {label}, about Blackbox, Claude Code, AI tools, and client work, written by AI from his prompts.",
              path=f"/{key}/index.html", body=f'<h1 class="page-title">{label}</h1>' + by_day(ps),
              noindex=True, **P))
    cats = {}
    for p in posts:
        for c in p["cats"]:
            cats.setdefault(c, []).append(p)
    for c, ps in cats.items():
        write(f"/category/{slugify(c)}.html", page(title=f"Posts about {c}", description=f"Every post on Chris Abraham's weblog filed under {c}, newest first, written by AI from his prompts and showing each prompt.",
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
    write("/archives.html", page(title="Archives of the Chris Abraham weblog", seo_title="Weblog archives: every post by Chris Abraham, by month", description="Every post on Chris Abraham's weblog by month, from Blackbox to Claude Code to anonymized client work, written by AI from his prompts.",
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
                       "url": SITE_URL + "/projects.html", "author": AUTHOR_REF,
                       "hasPart": [{"@type": "CreativeWork", "name": x["name"], "url": x.get("url") or None,
                                    "creativeWorkStatus": x["status"]} for x in site["projects"]]}
    write("/projects.html", page(title="Projects Chris Abraham is building now", seo_title="Projects Chris Abraham is building now, with status", description="What Chris Abraham is building and running right now, from Blackbox to his podcast site, with the status of each project kept current.",
          path="/projects.html", schema=projects_schema,
          body='<h1 class="page-title">Projects</h1><p class="lede">What I am building, running, or planning, with an honest status for each. Posts about a project link back here.</p>' + "\n".join(rows), **P))
    sitemap.append(("/projects.html", None))


    # Wiki: evergreen pages, edited in place, with tabs, contents, and backlinks.
    for w in wiki.values():
        body, toc = add_toc(w["body"])
        info = ""
        if w["info"]:
            rows = "".join(f'<tr><th scope="row">{e(k)}</th><td>{v}</td></tr>' for k, v in w["info"])
            info = f'<table class="infobox"><caption>{e(w.get("infobox_title", w["title"]))}</caption>{rows}</table>'
        back = sorted(set(links_to.get(w["slug"], [])), key=lambda x: x[0].lower())
        backl = ("".join(f'<li><a href="{pp}">{e(t)}</a></li>' for t, pp in back)) or "<li>Nothing yet.</li>"
        cats = " &middot; ".join(f'<a href="/wiki/#cat-{slugify(c)}">{e(c)}</a>' for c in w["cats"])
        html_body = f"""<div class="wiki">
<nav class="wiki-tabs" aria-label="Page tools"><span class="sel" aria-current="page">Article</span><a href="{REPO}/blob/main/{w['src']}">View source</a><a href="{REPO}/commits/main/{w['src']}">History</a></nav>
<h1 class="wiki-title">{e(w['title'])}</h1>
<p class="wiki-from">From the <a href="/wiki/">Chris Abraham wiki</a></p>
<div class="wiki-body post-body">{info}{toc}
{body}
</div>
<p class="wiki-cats">Categories: {cats or "none"}</p>
<section class="wiki-backlinks"><h2>What links here</h2><ul>{backl}</ul></section>
<p class="wiki-edited">This page was last edited on {w['edited']:%B} {w['edited'].day}, {w['edited']:%Y}. AI writes and edits the wiki from Chris' prompts; the <a href="{REPO}/commits/main/{w['src']}">history</a> shows every change.</p>
</div>"""
        schema = {"@context": "https://schema.org", "@type": "Article", "headline": w["title"],
                  "description": w["description"], "url": w["url"], "dateModified": w["edited"].isoformat(),
                  "author": AUTHOR_REF, "isPartOf": {"@type": "CollectionPage", "name": "Chris Abraham wiki",
                  "url": SITE_URL + "/wiki/"}, "about": [{"@type": "Thing", "name": c} for c in w["cats"]],
                  "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
                      {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
                      {"@type": "ListItem", "position": 2, "name": "Wiki", "item": SITE_URL + "/wiki/"},
                      {"@type": "ListItem", "position": 3, "name": w["title"], "item": w["url"]}]}}
        write(w["path"], page(title=w["title"], description=w["description"], path=w["path"], body=html_body,
                              seo_title=w.get("seo_title"), kicker="From the Chris Abraham wiki",
                              schema=schema, og_type="article", **P))
        sitemap.append((w["path"], dt.datetime.combine(w["edited"], dt.time(), TZ)))

    # Wiki main page: every page by category, plus recent edits.
    bycat = {}
    for w in wiki.values():
        for c in w["cats"] or ["Uncategorized"]:
            bycat.setdefault(c, []).append(w)
    groups = "".join(
        f'<h2 id="cat-{slugify(c)}">{e(c)} pages</h2><ul>' + "".join(
            f'<li><a href="{w["path"]}">{e(w["title"])}</a>: {e(w["description"])}</li>'
            for w in sorted(ws, key=lambda w: w["title"].lower())) + "</ul>"
        for c, ws in sorted(bycat.items()))
    recent_edits = "".join(f'<li><time datetime="{w["edited"]}">{w["edited"]:%b} {w["edited"].day}</time> <a href="{w["path"]}">{e(w["title"])}</a></li>'
                           for w in sorted(wiki.values(), key=lambda w: w["edited"], reverse=True)[:10])
    main_body = f"""<div class="wiki">
<nav class="wiki-tabs" aria-label="Page tools"><span class="sel" aria-current="page">Main page</span><a href="{REPO}/tree/main/src/wiki">View source</a><a href="{REPO}/commits/main/src/wiki">History</a></nav>
<h1 class="wiki-title">Chris Abraham wiki</h1>
<div class="wiki-body post-body">
<p>The weblog is the diary; this is the reference shelf. Pages here hold what stays true for a while: how <a href="/wiki/blackbox.html">Blackbox</a> works and every command it knows, the machines it runs on, and the rules behind my projects. Posts are dated and never rewritten. Wiki pages are edited in place, and each one links to its full history. It looks like a wiki and behaves like one, with Chris directing AI-assisted changes recorded in Git history.</p>
{groups}
<h2>Recent edits</h2><ul class="archive-list">{recent_edits}</ul>
</div></div>"""
    write("/wiki/index.html", page(title="Chris Abraham wiki", seo_title="Chris Abraham wiki: Blackbox, commands, and project notes", description="Evergreen reference pages from Chris Abraham: Blackbox and every command it knows, pinebox, the Upwork verdicts, and Adjutant, edited in place.",
          path="/wiki/index.html", body=main_body, schema={"@context": "https://schema.org", "@type": "CollectionPage",
          "name": "Chris Abraham wiki", "url": SITE_URL + "/wiki/", "author": AUTHOR_REF,
          "hasPart": [{"@type": "Article", "headline": w["title"], "url": w["url"]} for w in wiki.values()]}, **P))
    sitemap.append(("/wiki/", max((dt.datetime.combine(w["edited"], dt.time(), TZ) for w in wiki.values()), default=None)))

    # Reading list: every feed I follow, grouped, with feed links.
    groups_html = "".join(
        f'<h2>{e(g["group"])}</h2><ul class="reading">' + "".join(
            f'<li><a href="{e(x["url"])}">{e(x["name"])}</a>'
            + (f' <small>(<a href="{e(x["feed"])}" type="application/rss+xml">feed</a>)</small>' if x.get("feed") else "")
            + (f' <small>{e(x["note"])}</small>' if x.get("note") else "") + "</li>" for x in g["links"]) + "</ul>"
        for g in site["reading"])
    nfeeds = sum(1 for g in site["reading"] for x in g["links"] if x.get("feed"))
    reading_intro = (f'<p>These are the {nfeeds} feeds I read to keep up with search, AI search, the AI labs, and the policy around all of it. '
                     'Each feed address was tested when it was added; the few marked below refused the test from my server and are listed at '
                     'their standard addresses. To follow them all at once, import <a href="/blogroll.opml">the OPML file</a> into any feed '
                     'reader.</p>')
    write("/reading.html", page(title="Reading list", seo_title="Reading list: SEO, AI search, AI labs, and AI policy feeds",
          description=f"The {nfeeds} feeds Chris Abraham reads to keep up with SEO, AEO, GEO, AI search, AI models and labs, and AI policy, in one OPML file.",
          path="/reading.html", schema={"@context": "https://schema.org", "@type": "CollectionPage", "name": "Reading list",
          "url": SITE_URL + "/reading.html", "author": AUTHOR_REF},
          body=f'<h1 class="page-title">Reading list</h1><div class="post-body">{reading_intro}{groups_html}</div>', **P))
    sitemap.append(("/reading.html", None))

    # Author pages: a bio from src/authors/<slug>.html plus every post by that author.
    for key, a in AUTHORS.items():
        src = SRC / "authors" / (a["path"].rsplit("/", 1)[1])
        if not src.exists():
            continue
        m = parse(src)
        m["body"] = wikilinks(m["body"], wiki, set())
        mine = [p for p in posts if (p.get("author") or "chris") == key]
        lst = "".join(f'<li><time datetime="{p["when"].date()}">{p["when"]:%b} {p["when"].day}</time> <a href="{p["path"]}">{e(p["title"])}</a></li>' for p in mine)
        body = (f'<h1 class="page-title">{e(m["title"])}</h1><div class="post-body">{add_toc(m["body"])[0]}</div>'
                f'<h2>Posts by {e(a["name"])}</h2><ul class="archive-list">{lst or "<li>None yet.</li>"}</ul>')
        entity = AUTHOR_REF if a["type"] == "Person" else author_ref(key)
        schema = {"@context": "https://schema.org", "@type": "ProfilePage", "name": m["title"], "url": SITE_URL + a["path"],
                  "description": m["description"], "mainEntity": entity}
        write(a["path"], page(title=m["title"], seo_title=m.get("seo_title"), description=m["description"], path=a["path"],
                              schema=schema, body=body, **P))
        sitemap.append((a["path"], None))

    # Static pages
    for f in sorted((SRC / "pages").glob("*.html")):
        m = parse(f)
        check_meta(f.name, m)
        m["body"] = wikilinks(m["body"], wiki, set())
        path = f"/{f.stem}.html"
        schema = {"@context": "https://schema.org", "@type": m.get("schema", "WebPage"), "name": m["title"],
                  "url": SITE_URL + path, "description": m["description"],
                  "mainEntity" if m.get("schema") == "ProfilePage" else "author": PERSON}
        write(path, page(title=m["title"], description=m["description"], path=path, schema=schema,
                         seo_title=m.get("seo_title"),
                         body=f'<h1 class="page-title">{e(m["title"])}</h1><div class="post-body">{add_toc(m["body"])[0]}</div>',
                         noindex=f.stem == "404", **P))
        if f.stem != "404":
            sitemap.append((path, None))

    # Feeds and machine files
    write("/rss.xml", rss(posts))
    write("/blogroll.opml", opml(site))
    def images_for(path):
        """Every image on the page, plus its share card, for Google Images and AI crawlers."""
        f = OUT / (path.lstrip("/") + ("index.html" if path.endswith("/") else ""))
        if not f.exists():
            return ""
        t = f.read_text(encoding="utf-8")
        srcs = re.findall(r'<img[^>]+src="(/media/[^"]+)"', t) + re.findall(r'<meta property="og:image" content="([^"]+)"', t)
        seen = dict.fromkeys(s if s.startswith("http") else SITE_URL + s for s in srcs)
        return "".join(f"<image:image><image:loc>{u}</image:loc></image:image>" for u in seen)
    write("/sitemap.xml", "".join([
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n',
        *(f"<url><loc>{SITE_URL}{p}</loc>{f'<lastmod>{d.date()}</lastmod>' if d else ''}{images_for(p)}</url>\n" for p, d in sitemap),
        "</urlset>\n"]))
    write("/robots.txt", ROBOTS.replace("{SITE}", SITE_URL))
    write("/llms.txt", llms(posts, site, full=False))
    write("/llms-full.txt", llms(posts, site, full=True))
    if (SRC / "media").exists():
        shutil.copytree(SRC / "media", OUT / "media")
    write("/favicon.svg", FAVICON)
    raster_icons()
    write("/humans.txt", f"""/* TEAM */
Owner and prompter: {AUTHOR}
Contact: {EMAIL}
From: Sexy South Arlington, Virginia, USA
AI authors: Claude Code (Anthropic) and ChatGPT (OpenAI), independently attributed

/* THANKS */
Dave Winer, for Scripting News and RSS
Everyone on the blogroll

/* SITE */
Last update: {dt.date.today()}
Language: English
Standards: HTML5, CSS3, RSS 2.0, OPML 2.0, schema.org, microformats2, WCAG 2.1 AA
Software: Python 3 standard library, Pillow for share cards, GitHub Pages
Source: https://github.com/chrisabraham/weblog
""")
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
<dc:creator>{e(AUTHORS.get(p.get("author") or "chris", AUTHORS["chris"])["name"])}</dc:creator>
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
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:creativeCommons="http://backend.userland.com/creativeCommonsRssModule">
<channel>
<title>{e(TITLE)}</title>
<link>{SITE_URL}/</link>
<atom:link href="{SITE_URL}/rss.xml" rel="self" type="application/rss+xml"/>
<description>{e(TAGLINE)}</description>
<language>en-us</language>
<copyright>CC BY 4.0, {AUTHOR}</copyright>
<creativeCommons:license>https://creativecommons.org/licenses/by/4.0/</creativeCommons:license>
<lastBuildDate>{last}</lastBuildDate>
<docs>https://cyber.harvard.edu/rss/rss.html</docs>
<generator>build.py, written with AI</generator>
{chr(10).join(items)}
</channel>
</rss>
"""


def opml(site):
    def row(b):
        if b.get("feed"):
            return f'<outline text="{e(b["name"])}" type="rss" htmlUrl="{e(b["url"])}" xmlUrl="{e(b["feed"])}"/>\n'
        return f'<outline text="{e(b["name"])}" type="link" url="{e(b["url"])}"/>\n'
    outl = ""
    outl += "".join(f'<outline text="{e(g["group"])}">\n' + "".join(row(b) for b in g["links"]) + "</outline>\n"
                    for g in site["reading"])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
<head><title>{e(AUTHOR)}'s blogroll and reading list</title><ownerName>{AUTHOR}</ownerName><docs>http://opml.org/spec2.opml</docs></head>
<body>
{outl}</body>
</opml>
"""


def llms(posts, site, *, full):
    wiki = site.get("_wiki", {})
    out = [f"# {TITLE}", "", f"> {TAGLINE}", "",
           f"{AUTHOR}'s personal weblog about working with AI: Blackbox (his command-line secretary), Claude, Claude Code, ChatGPT, OpenAI Codex, GitHub, and anonymized client work. "
           "AI writes every post from Chris' prompts (mostly Claude, sometimes OpenAI Codex); each post names the model and shows the prompt.", "",
           "## Pages", "",
           f"- [About]({SITE_URL}/about.html): who Chris is and how this weblog gets written",
           f"- [Projects]({SITE_URL}/projects.html): what he is building, with status",
           f"- [Archives]({SITE_URL}/archives.html): every post by month",
           f"- [Wiki]({SITE_URL}/wiki/): evergreen reference pages",
           f"- [RSS]({SITE_URL}/rss.xml)", "", "## Posts", ""]
    for p in posts:
        out.append(f"- [{p['title']}]({p['url']}) ({p['when'].date()}): {p['description']}")
    out += ["", "## Wiki", ""] + [f"- [{w['title']}]({w['url']}) (edited {w['edited']}): {w['description']}"
                                   for w in sorted(wiki.values(), key=lambda w: w["title"].lower())]
    if full:
        for w in sorted(wiki.values(), key=lambda w: w["title"].lower()):
            out += ["", "---", "", f"# {w['title']}", "", f"{w['url']} · edited {w['edited']}", "", text_only(w["body"])]
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

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="4" fill="#ffffff"/>'
           '<text x="16" y="22.5" font-family="Verdana,DejaVu Sans,sans-serif" font-size="17" font-weight="bold" '
           'letter-spacing="-1" fill="#c75000" text-anchor="middle">CA</text></svg>')


def raster_icons():
    """favicon.ico (16, 32, 48) and a 180px apple-touch-icon: CA in orange on white."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return
    def icon(n):
        im = Image.new("RGBA", (n, n), "#ffffff")
        d = ImageDraw.Draw(im)
        f = ImageFont.truetype(str(FONT_DIR / "DejaVuSans-Bold.ttf"), int(n * 0.5))
        d.text((n / 2, n / 2 + n * 0.02), "CA", font=f, fill="#c75000", anchor="mm")
        return im
    icon(48).save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    icon(180).convert("RGB").save(OUT / "apple-touch-icon.png", optimize=True)

CSS = (ROOT / "src" / "style.css").read_text(encoding="utf-8") if (ROOT / "src" / "style.css").exists() else ""

if __name__ == "__main__":
    main()

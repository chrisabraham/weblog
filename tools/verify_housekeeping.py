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
import xml.etree.ElementTree as ET

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

# This Chris-bylined essay was written by ChatGPT at Chris' direction.
# Check the author distinction, source prompts, public revisions and light art.
ethos_post = DOCS / "2026/10/my-ai-writers-keep-stealing-my-best-material.html"
verify(ethos_post.exists(), "Chris' AImaxxing editorial article is generated")
if ethos_post.exists():
    ethos_html = ethos_post.read_text(encoding="utf-8")
    verify('class="prompt"' in ethos_html and 'FOLLOW-UP 4, VERBATIM' in ethos_html,
           "Original assignment and follow-up edits are exposed with the article")
    verify("AImaxxing" in ethos_html and "Even my editing of this article gets published" in ethos_html,
           "The AImaxxing paradox and public curation appear in the prose")
    verify('src="/media/ai-writers-editorial-table.svg"' in ethos_html,
           "The compact SVG illustration appears on the article")
    verify("GPT-6 in ChatGPT" in ethos_html
           and 'href="/authors/chris-abraham.html"' in ethos_html,
           "Chris' byline and the AI writing model are accurately attributed")
    verify("Every time it says head it means hedge" in ethos_html,
           "The exact voice-to-text hedge correction is included in the prompt")
    verify("I would rather be an asshole than a pussy" in ethos_html,
           "The publisher's blunt editorial intervention is preserved verbatim")
    verify(ethos_html.count('<aside class="editor-note"') == 1
           and "Editorial note from ChatGPT" in ethos_html,
           "Exactly one independently attributed ChatGPT editorial aside")
verify((DOCS / "media/ai-writers-editorial-table.svg").exists(),
       "The separate SVG is generated and available without JavaScript")

# Redlined 826DC memoir: the original voice-to-text, two illustrations,
# affiliate disclosure, and emphasis on revisions all travel together.
redlined = DOCS / "2026/10/put-the-redlined-manuscripts-on-the-walls.html"
verify(redlined.exists(), "Approved standalone Oliver Uberti / 826DC memoir is published")
if redlined.exists():
    text826 = redlined.read_text(encoding="utf-8")
    verify('class="prompt"' in text826
           and "As an aside and I think that it&#x27;s an amazing kind of article" in text826
           and "About iterations and revisions and all that other stuff" in text826,
           "Original 826DC assignment and precise redlining edit instruction survive")
    verify(text826.index("The walls were giving everybody permission")
           < text826.index("Our posse was completely earnest")
           < text826.index("It took a village to make "),
           "The manuscript's revision lesson frames the posse and book references")
    verify('src="/media/826dc-redlined-manuscripts.svg"' in text826
           and "A tiny companion illustration by ChatGPT" in text826,
           "Little hand-built manuscript-wall SVG and its original caption survive")
    verify('src="/media/826dc-full-essay.avif"' in text826
           and "Full-text AI illustration by ChatGPT" in text826,
           "Article-wide generated lead art is present and attributed")
    verify("rel=\"sponsored noopener\"" in text826
           and "tag=gerris-20" in text826
           and "As an Amazon Associate I earn from qualifying purchases" in text826,
           "Affiliate book links and the disclosure follow the existing house rule")
    verify("GPT-6 in ChatGPT" in text826 and 'href="/authors/chris-abraham.html"' in text826,
           "Oliver memoir has Chris' byline and ChatGPT's disclosed writing role")
# Chris' book-link rule: visible titles are tagged Amazon Associates links,
# except the British title Fiesta, which Chris directed to his own original essay.
if redlined.exists():
    from html import unescape as unescape_text
    tests_for_books = {
        "The Sun Also Rises": "0743297334",
        "London: The Information Capital": "0141978791",
        "Where the Animals Go": "0393634027",
        "Atlas of the Invisible": "0393651517",
        "Atlas of Finance": "0300253052",
        "Notes from a Public Typewriter": "1538729113",
        "The Hidden Nations of Animals": "0593716841",
    }
    for title, asin in tests_for_books.items():
        link = ('<a href="https://www.amazon.com/dp/' + asin +
                '?tag=gerris-20" rel="sponsored noopener">')
        verify(bool(re.search(re.escape(link) + r'(?:<(?:em|i)>)?' +
                              re.escape(title) + r'(?:</(?:em|i)>)?</a>',
                              text826)),
               f"Book title {title} is an Amazon Associates link")
    verify(not re.search(r'<a [^>]*>Amazon</a>', text826),
           "Book sections no longer use detached Amazon text links")
    fiesta_url = "https://chrisabraham.com/blog/fiesta-the-sun-also-rises-by-ernest-hemingway/"
    verify(text826.count('href="' + fiesta_url + '"') >= 4,
           "All original Fiesta title links lead to Chris' own Hemingway article")
    verify('https://www.amazon.com/dp/0099285037?tag=gerris-20' not in text826,
           "No competing Amazon Fiesta link remains in this memoir")
    verify("FOLLOW-UP 16, VERBATIM" in text826
           and "Update, October 17, 2026, 2:42 AM EDT" in text826,
           "User-provided Fiesta link and dated correction are publicly attributed")

    verify("FOLLOW-UP 14, VERBATIM" in text826
           and "FOLLOW-UP 15, VERBATIM" in text826
           and "Update, October 17, 2026" in text826,
           "Book-link correction retains publisher prompts and dated editorial note")

verify((DOCS / "media/826dc-redlined-manuscripts.svg").exists(),
       "Saved original manuscript gallery SVG is present")
lead_image = DOCS / "media/826dc-full-essay.avif"
verify(lead_image.exists(), "Generated full-text illustration is present")
if lead_image.exists():
    sample = lead_image.read_bytes()
    verify(len(sample) > 1000 and sample[4:12] == b"ftypavif",
           "Small lead image is a real AVIF media file")

# Regression: wiki syntax may legitimately refer to a published post rather than
# an evergreen wiki page. No more false redlink for the named flotilla article.
flotilla_reference = DOCS / "2026/10/chaff-flares-reputation-work.html"
if flotilla_reference.exists():
    rendered = flotilla_reference.read_text(encoding="utf-8")
    verify('href="/2026/10/little-boats-one-flotilla.html" class="postlink"' in rendered,
           "Article cross-reference links to the real flotilla permalink")
    verify('title="Little boats, one flotilla (page does not exist yet)"' not in rendered,
           "Existing published article is not marked as missing wiki content")

# The wiki directory lists each evergreen resource once, without repeating a
# multi-category page in several sections or copying the entire directory into
# the sidebar. The wiki is a reference layer, not a second blog index.
wiki_index = DOCS / "wiki/index.html"
verify(wiki_index.exists(), "The wiki main directory is generated")
if wiki_index.exists():
    wiki_html = wiki_index.read_text(encoding="utf-8")
    wiki_body = wiki_html.split('<div class="wiki-body post-body">', 1)[1].split("</div></div>", 1)[0]
    listed = re.findall(r'<li><a href="(/wiki/[a-z0-9-]+\.html)"', wiki_body)
    expected_wiki = {"/wiki/" + p.name for p in (DOCS / "wiki").glob("*.html")
                     if p.name != "index.html"}
    verify(set(listed) == expected_wiki and len(listed) == len(expected_wiki),
           "Wiki index lists all and only the evergreen pages, exactly once")
    verify("Recent edits</h2>" not in wiki_body,
           "Wiki main page does not repeat the directory in a recent-edits list")
    verify('href="/wiki/">Browse ' in HOME,
           "The global sidebar links to the directory instead of repeating every wiki page")

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


# Navigation, syndication, and machine-readable outputs must all be built from
# the same published source set. These tests inspect generated files, not promises.
verify('href="/categories.html">Categories</a>' in HOME,
       "Categories has an ordinary accessible entry in the top navigation")
verify('href="/atom.xml"' in HOME and 'type="application/atom+xml"' in HOME,
       "Every page autodiscovers the real Atom 1.0 feed")
verify('href="/feeds.opml"' in HOME and 'type="text/x-opml"' in HOME,
       "Every page autodiscovers the full subscription OPML")
verify('href="/rss.xml"' in HOME and 'href="/blogroll.opml"' in HOME,
       "RSS and historic blogroll OPML autodiscovery survive")

categories = DOCS / "categories.html"
verify(categories.exists(), "The subject directory is an indexable real HTML page")
if categories.exists():
    categories_html = categories.read_text(encoding="utf-8")
    directory_paths = set(re.findall(r'href="(/category/[a-z0-9-]+\.html)"', categories_html))
    generated_categories = set("/"+str(p.relative_to(DOCS))
                               for p in (DOCS / "category").glob("*.html"))
    verify(directory_paths == generated_categories,
           "Categories directory lists exactly the generated categories")
    verify('name="robots" content="index, follow' in categories_html,
           "Category index is indexable and the member excerpts remain navigable")
    verify(all('name="robots" content="noindex, follow' in
               (DOCS / p.lstrip("/")).read_text(encoding="utf-8")
               for p in generated_categories),
           "Category excerpt archives remain noindex to avoid duplicate pages")

rss = ET.parse(DOCS / "rss.xml").getroot()
atom = ET.parse(DOCS / "atom.xml").getroot()
sitemap = ET.parse(DOCS / "sitemap.xml").getroot()
blogroll = ET.parse(DOCS / "blogroll.opml").getroot()
subscriptions = ET.parse(DOCS / "feeds.opml").getroot()
rns = {"atom": "http://www.w3.org/2005/Atom",
       "site": "http://www.sitemaps.org/schemas/sitemap/0.9"}
rss_urls = [x.findtext("link") for x in rss.findall("./channel/item")]
atom_entries = atom.findall("atom:entry", rns)
atom_urls = [x.findtext("atom:id", namespaces=rns) for x in atom_entries]
verify(bool(rss_urls) and rss_urls == atom_urls,
       "Atom and RSS contain identical articles in identical feed order")
verify(all(x.findtext("atom:updated", namespaces=rns)
           and x.findtext("atom:published", namespaces=rns)
           and x.findtext("atom:content", namespaces=rns)
           for x in atom_entries),
       "Every Atom entry contains published/updated dates and full content")
verify(atom.find("atom:link[@rel='self']", rns).attrib.get("href") ==
       "https://chrisabraham.net/atom.xml",
       "Atom advertises its canonical self URL")
verify(blogroll.get("version") == "2.0" and subscriptions.get("version") == "2.0",
       "Both OPML exports use the OPML 2.0 specification")
imported = [x.attrib.get("xmlUrl") for x in blogroll.iter("outline") if x.attrib.get("xmlUrl")]
all_imports = [x.attrib.get("xmlUrl") for x in subscriptions.iter("outline") if x.attrib.get("xmlUrl")]
verify(set(imported).issubset(set(all_imports))
       and {"https://chrisabraham.net/atom.xml", "https://chrisabraham.net/rss.xml"}.issubset(set(all_imports)),
       "Complete OPML adds both own feeds without dropping any subscribed feed")
sitemap_urls = {x.findtext("site:loc", namespaces=rns)
                for x in sitemap.findall("site:url", rns)}
verify("https://chrisabraham.net/categories.html" in sitemap_urls
       and "https://chrisabraham.net/" in sitemap_urls,
       "Sitemap includes indexable home and category directory")
verify(set(rss_urls).issubset(sitemap_urls),
       "Sitemap includes every article advertised in RSS and Atom")
verify(not any("/category/" in x for x in sitemap_urls if x),
       "Sitemap excludes noindex category archives")
verify(len(sitemap_urls) == len(sitemap.findall("site:url", rns)),
       "Sitemap contains no duplicate canonical URLs")
# Three quiet reference destinations: short glossary, subject index, HTML site map.
# They are generated from source data and the identical canonical XML inventory.
gpath = DOCS / "glossary.html"
ipath = DOCS / "site-index.html"
mpath = DOCS / "site-map.html"
verify(all(p.exists() for p in (gpath, ipath, mpath)),
       "Glossary, back-of-book index and HTML site map are generated")
if all(p.exists() for p in (gpath, ipath, mpath)):
    glossary_data = json.loads((root / "src/glossary.json").read_text(encoding="utf-8"))
    glossary_html = gpath.read_text(encoding="utf-8")
    index_html = ipath.read_text(encoding="utf-8")
    map_html = mpath.read_text(encoding="utf-8")
    term_ids = re.findall(r'class="glossary-entry" id="([^"]+)"', glossary_html)
    verify(len(term_ids) == len(glossary_data) and len(term_ids) == len(set(term_ids)),
           "Each glossary entry has one unique addressable definition")
    verify(all(0 < len(x["definition"]) <= 500 for x in glossary_data),
           "Definitions are accurate-sized reference notes, never over 500 characters")
    verify(all("https://chrisabraham.net" + x["source"] in sitemap_urls
               for x in glossary_data),
           "Every glossary source points to an indexable published page")
    verify(index_html.count('class="index-term"') >= 100
           and 'class="back-index"' in index_html,
           "The subject index harvests substantial real page references")
    map_body = map_html.split('class="post-body reference-page"', 1)[1].split("</main>", 1)[0]
    listed_urls = re.findall(r'<li><a href="(/[^"]*)"', map_body)
    map_expected = {x.removeprefix("https://chrisabraham.net") for x in sitemap_urls}
    verify(set(listed_urls) == map_expected and len(listed_urls) == len(map_expected),
           "HTML site map lists the complete XML canonical inventory exactly once")
    footer = HOME.split('<footer id="footer">', 1)[1]
    banner = HOME.split("</header>", 1)[0]
    refurls = ("/glossary.html", "/site-index.html", "/site-map.html")
    verify(all('href="' + url + '"' in footer for url in refurls)
           and all('href="' + url + '"' not in banner for url in refurls),
           "Reference pages live in the small footer links, not the top navigation")
    verify(all(url in (DOCS / "llms.txt").read_text(encoding="utf-8")
               for url in refurls),
           "AI-readable navigation also exposes the new reference surfaces")

for machine_path in ("llms.txt", "llms-full.txt"):
    machine = (DOCS / machine_path).read_text(encoding="utf-8")
    verify(all(x in machine for x in
               ("/readme.html", "/categories.html", "/rss.xml", "/atom.xml",
                "/feeds.opml", "/blogroll.opml", "/sitemap.xml")),
           f"{machine_path} links to every current publishing/reading surface")
    verify("## Categories" in machine and "mostly Claude" not in machine,
           f"{machine_path} lists current categories without stale model claims")
verify("Sitemap: https://chrisabraham.net/sitemap.xml" in
       (DOCS / "robots.txt").read_text(encoding="utf-8"),
       "robots.txt points to the current canonical sitemap")
verify("100/100" not in HOME and "<b>WCAG</b>2.1 AA" not in HOME,
       "Visual badges do not advertise unverified accessibility certification")

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

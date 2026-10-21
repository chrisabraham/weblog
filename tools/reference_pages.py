"""Build the separate glossary, back-of-book index, and human-readable site map.

Data belongs in src/glossary.json and src/site-index.json. This module runs
inside build.py after posts, wiki pages and standalone source pages are loaded.
No duplicate article text, no extra sidebar furniture, no client-side JS.
"""
import json
import re


def build_reference_pages(*, src, site_url, site, posts, wiki, sitemap, authors,
                          page, write, parse, text_only, escape, slugify):
    P = {"site": site, "posts": posts}
    e = escape
    glossary = json.loads((src / "glossary.json").read_text(encoding="utf-8"))
    titles = {p["path"]: p["title"] for p in posts}
    titles.update({w["path"]: w["title"] for w in wiki.values()})
    static_files = [f for f in sorted((src / "pages").glob("*.html")) if f.stem != "404"]
    static = [("/" + f.stem + ".html", parse(f)) for f in static_files]
    titles.update({path: meta["title"] for path, meta in static})
    groups, ids = {}, set()
    for item in glossary:
        term, definition, target = (item[k].strip() for k in ("term", "definition", "source"))
        anchor = slugify(term)
        if not term or not definition or len(definition) > 500 or anchor in ids:
            raise ValueError(f"Invalid glossary term/definition {term!r}")
        if target not in titles:
            raise ValueError(f"Invalid glossary target: {term}: {target}")
        ids.add(anchor)
        letter = term[0].upper() if term[0].isalpha() else "0–9"
        groups.setdefault(letter, []).append((term, definition, target, anchor))
    def alpha_nav(grouped, prefix):
        return ('<nav class="reference-alpha" aria-label="Alphabetical navigation">'
                + " ".join(f'<a href="#{prefix}{slugify(letter)}">{e(letter)}</a>'
                           for letter in sorted(grouped)) + '</nav>')
    ghtml = []
    for letter, items in sorted(groups.items()):
        ghtml.append(f'<section class="reference-group"><h2 id="g-{slugify(letter)}">{e(letter + (" terms" if letter == "0–9" else ""))}</h2>'
                     '<dl class="glossary-list">')
        for term, definition, target, anchor in sorted(items, key=lambda x: x[0].casefold()):
            ghtml.append(f'<div class="glossary-entry" id="{anchor}"><dt>{e(term)}</dt>'
                         f'<dd>{e(definition)} '
                         f'<a class="reference-source" href="{target}">In context: {e(titles[target])}</a>'
                         '</dd></div>')
        ghtml.append('</dl></section>')
    gschema = {
        "@context": "https://schema.org", "@type": "DefinedTermSet",
        "name": "Glossary of the weblog and wiki", "url": site_url + "/glossary.html",
        "hasDefinedTerm": [
            {"@type": "DefinedTerm", "name": x["term"],
             "description": x["definition"],
             "url": site_url + "/glossary.html#" + slugify(x["term"])}
            for x in glossary
        ]
    }
    write("/glossary.html", page(
        title="Glossary", seo_title="Glossary of AI Tools and Web Publishing Terms Explained",
        description="Short definitions of the technical and cultural terms used across this weblog, with a link from each entry to an article or wiki page that explains it.",
        path="/glossary.html",
        body=('<h1 class="page-title">Glossary</h1><div class="post-body reference-page">'
              '<p>Short definitions, each linked to a page that explains the term in context. '
              'For page references, use the <a href="/site-index.html">back-of-book index</a>.</p>'
              + alpha_nav(groups, "g-") + "".join(ghtml) + '</div>'),
        schema=gschema, **P))
    sitemap.append(("/glossary.html", None))

    # Locate actual occurrences; never create invented page locators.
    source_pages = [(p["title"], p["path"], text_only(p["body"])) for p in posts]
    source_pages += [(w["title"], w["path"], text_only(w["body"])) for w in wiki.values()]
    source_pages += [(meta["title"], path, text_only(meta["body"])) for path, meta in static]
    source_pages += [(p["name"], "/projects.html", p["name"] + " " + p.get("about", ""))
                     for p in site["projects"]]
    topics = {x["term"].casefold(): {"term": x["term"], "patterns": [x["term"]]}
              for x in glossary}
    for entry in json.loads((src / "site-index.json").read_text(encoding="utf-8")):
        key = entry["term"].casefold()
        if key in topics:
            topics[key]["patterns"].extend(entry.get("patterns", []))
        else:
            topics[key] = entry
    igroups = {}
    for topic in topics.values():
        term = topic["term"]
        patterns = [re.compile(r"(?<!\w)" + re.escape(p) + r"(?!\w)", re.I)
                    for p in dict.fromkeys(topic.get("patterns", [])) if p]
        results = []
        for page_title, url, body in source_pages:
            score = 0
            for rx in patterns:
                if rx.search(page_title):
                    score = max(score, 20)
                if rx.search(body[:1600]):
                    score = max(score, 5)
                elif rx.search(body):
                    score = max(score, 1)
            if score:
                results.append((score, page_title, url))
        if not results:
            continue
        results.sort(key=lambda x: (-x[0], x[1].casefold()))
        unique = {}
        for value in results:
            unique.setdefault(value[2], value)
        letter = term[0].upper() if term[0].isalpha() else "0–9"
        igroups.setdefault(letter, []).append((term, list(unique.values())[:7]))
    ihtml = []
    for letter, items in sorted(igroups.items()):
        ihtml.append(f'<section class="reference-group"><h2 id="i-{slugify(letter)}">{e(letter + (" topics" if letter == "0–9" else ""))}</h2>'
                     '<ul class="back-index">')
        for term, locators in sorted(items, key=lambda x: x[0].casefold()):
            links = ", ".join(f'<a href="{url}" title="{e(title)}">{e(title)}</a>'
                              for score, title, url in locators)
            defined = (f'; <a class="index-definition" href="/glossary.html#{slugify(term)}">'
                       'definition</a>') if slugify(term) in ids else ""
            ihtml.append(f'<li><span class="index-term">{e(term)}</span>: {links}{defined}</li>')
        ihtml.append('</ul></section>')
    count = sum(map(len, igroups.values()))
    write("/site-index.html", page(
        title="Index", seo_title="Index of People, Projects and Topics Across the Weblog",
        description="An alphabetical index of people, tools, projects and ideas discussed across the weblog and wiki, linking to the pages where they appear.",
        path="/site-index.html",
        body=('<h1 class="page-title">Index</h1><div class="post-body reference-page">'
              f'<p>{count} subjects with references to the pages where they actually occur. '
              'Definitions are in the <a href="/glossary.html">glossary</a>; the '
              '<a href="/site-map.html">HTML site map</a> lists every page.</p>'
              + alpha_nav(igroups, "i-") + "".join(ihtml) + '</div>'),
        schema={"@context": "https://schema.org", "@type": "CollectionPage",
                "name": "Back-of-book index", "url": site_url + "/site-index.html",
                "description": "An alphabetical index of people, projects, tools and topics."}, **P))
    sitemap.append(("/site-index.html", None))

    # One public page per canonical URL in the same inventory as sitemap.xml.
    sitemap.append(("/site-map.html", None))
    expected = {path for path, modified in sitemap}
    listed = set()
    def link(path, title):
        if path in listed:
            raise ValueError(f"Repeated HTML sitemap URL: {path}")
        listed.add(path)
        return f'<li><a href="{path}">{e(title)}</a></li>'
    tree = ['<section class="reference-group"><h2>Articles</h2><ul class="site-tree">']
    months = {}
    for p in posts:
        months.setdefault(p["when"].strftime("%B %Y"), []).append(p)
    for month, entries in months.items():
        tree.append(f'<li><strong>{e(month)}</strong><ul>')
        tree += [link(p["path"], p["title"]) for p in entries]
        tree.append('</ul></li>')
    tree.append('</ul></section><section class="reference-group"><h2>Evergreen wiki</h2>'
                '<ul class="site-tree">')
    tree += [link(w["path"], w["title"]) for w in
             sorted(wiki.values(), key=lambda w: w["title"].casefold())]
    tree.append('</ul></section><section class="reference-group"><h2>Authors</h2><ul class="site-tree">')
    for a in authors.values():
        if a["path"] in expected:
            tree.append(link(a["path"], a["name"]))
    tree.append('</ul></section><section class="reference-group"><h2>Site pages</h2><ul class="site-tree">')
    others = {"/": "Home", "/wiki/": "Wiki directory",
              "/categories.html": "Topics and categories", "/archives.html": "Article archives",
              "/projects.html": "Projects", "/reading.html": "Reading list",
              "/glossary.html": "Glossary", "/site-index.html": "Back-of-book index",
              "/site-map.html": "HTML site map"}
    others.update({path: meta["title"] for path, meta in static})
    for path, title in sorted(others.items(), key=lambda item: item[1].casefold()):
        if path in expected:
            tree.append(link(path, title))
    tree.append('</ul></section>')
    if listed != expected:
        raise ValueError(f"HTML sitemap parity: missing {expected-listed}, unexpected {listed-expected}")
    write("/site-map.html", page(
        title="HTML site map", seo_title="HTML Site Map of Articles, Wiki and Reference Pages",
        description="A readable tree of every indexable weblog article, wiki entry, author page and site reference, generated from the same URLs as the XML sitemap.",
        path="/site-map.html",
        body=('<h1 class="page-title">HTML site map</h1><div class="post-body reference-page">'
              f'<p>{len(expected)} published indexable pages, grouped for readers. '
              'Generated from the same URLs as the <a href="/sitemap.xml">XML sitemap</a> and '
              '<a href="/sitemap.txt">plain text sitemap</a>. '
              'Browse topics in the <a href="/site-index.html">index</a> or definitions in the '
              '<a href="/glossary.html">glossary</a>.</p>' + "".join(tree) + '</div>'),
        schema={"@context": "https://schema.org", "@type": "CollectionPage",
                "name": "Human-readable site map", "url": site_url + "/site-map.html",
                "description": "An HTML directory of the public indexable pages."}, **P))
    return {"glossary": len(glossary), "index": count, "sitemap": len(expected)}

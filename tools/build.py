"""Build the guide: book/*.md -> docs/ (multi-page website), docs/downloads/ (EPUB + PDF).

Usage:  python tools/build.py [--no-epub] [--no-pdf]
Needs:  pip install markdown; Calibre (ebook-convert) for EPUB; Chrome/Chromium for PDF.
"""
import argparse, html, os, re, shutil, subprocess, sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"
DOCS = ROOT / "docs"
TITLE = "Probe Basic, Explained"
SUBTITLE = "An illustrated guide to LinuxCNC's Probe Basic screen, and a complete Mesa 7I96S router build"
AUTHOR = "rsilvers129, written with Claude"
REPO = "https://github.com/rsilvers129/linuxcnc-probe-basic-guide"

CSS = """
:root { --bg:#fbfbf8; --fg:#1d1d1f; --muted:#5f6368; --line:#d9d9d4; --accent:#1f6fd1; --box:#eef4fd; --code:#f1f1ec; }
@media (prefers-color-scheme: dark) { :root { --bg:#16171a; --fg:#e6e6e6; --muted:#a0a4ab; --line:#33363c; --accent:#6aa8ff; --box:#1c2635; --code:#22252b; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font: 17px/1.6 -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
header.top { border-bottom:1px solid var(--line); padding:12px 16px; }
header.top a { color:var(--fg); text-decoration:none; font-weight:600; }
main { max-width: 860px; margin: 0 auto; padding: 24px 16px 64px; }
h1 { font-size: 2rem; line-height:1.2; margin-top:.5rem; }
h2 { margin-top: 2.2rem; border-bottom:1px solid var(--line); padding-bottom:.2rem; }
h3 { margin-top: 1.6rem; }
a { color: var(--accent); }
img { max-width:100%; height:auto; background:#fff; border:1px solid var(--line); border-radius:6px; }
table { border-collapse: collapse; width:100%; margin: 1rem 0; font-size: .95rem; display:block; overflow-x:auto; }
th, td { border:1px solid var(--line); padding:.35rem .55rem; vertical-align: top; text-align:left; }
th { background: var(--code); }
code { background: var(--code); padding: .1rem .3rem; border-radius: 4px; font-size: .9em; }
pre { background: var(--code); padding: .8rem 1rem; border-radius: 6px; overflow-x:auto; }
pre code { padding:0; background:none; }
blockquote { margin: 1rem 0; padding: .6rem 1rem; background: var(--box); border-left: 4px solid var(--accent); border-radius: 0 6px 6px 0; }
blockquote p { margin: .3rem 0; }
nav.pager { display:flex; justify-content:space-between; gap:1rem; margin-top:3rem; border-top:1px solid var(--line); padding-top:1rem; }
ol.toc li { margin: .3rem 0; }
.muted { color: var(--muted); }
.downloads a { display:inline-block; margin: .2rem .6rem .2rem 0; padding:.4rem .8rem; border:1px solid var(--line); border-radius:6px; text-decoration:none; }
"""


def md_to_html(text):
    text = re.sub(r"<!--\s*shot:[^>]*-->", "", text)   # screenshot placeholders
    return markdown.markdown(text, extensions=["tables", "fenced_code", "attr_list", "sane_lists"])


def chapters():
    out = []
    for p in sorted(BOOK.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", text, re.M)
        out.append({"src": p, "slug": p.stem, "title": m.group(1).strip() if m else p.stem, "md": text})
    return out


def page(title, body, rel=""):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><link rel="stylesheet" href="{rel}assets/style.css"></head>
<body><header class="top"><a href="{rel}index.html">{html.escape(TITLE)}</a></header>
<main>{body}</main></body></html>"""


def build_site(chs):
    if DOCS.exists():
        for item in DOCS.glob("*.html"):   # pages are regenerated; folders are refreshed in place
            item.unlink()
    (DOCS / "assets").mkdir(parents=True, exist_ok=True)
    (DOCS / "assets" / "style.css").write_text(CSS, encoding="utf-8")
    for sub in ("diagrams", "images"):
        if (BOOK / sub).exists():
            shutil.copytree(BOOK / sub, DOCS / sub, dirs_exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    for i, ch in enumerate(chs):
        prev = chs[i - 1] if i > 0 else None
        nxt = chs[i + 1] if i + 1 < len(chs) else None
        pager = '<nav class="pager"><span>' + (f'<a href="{prev["slug"]}.html">← {html.escape(prev["title"])}</a>' if prev else "") + \
                '</span><span>' + (f'<a href="{nxt["slug"]}.html">{html.escape(nxt["title"])} →</a>' if nxt else "") + "</span></nav>"
        (DOCS / f'{ch["slug"]}.html').write_text(page(ch["title"], md_to_html(ch["md"]) + pager), encoding="utf-8")
    toc = "\n".join(f'<li><a href="{c["slug"]}.html">{html.escape(c["title"])}</a></li>' for c in chs)
    index = f"""<h1>{html.escape(TITLE)}</h1><p class="muted">{html.escape(SUBTITLE)}</p>
<p class="downloads"><a href="downloads/probe-basic-explained.epub">EPUB (Kindle, Apple Books)</a>
<a href="downloads/probe-basic-explained.pdf">PDF</a> <a href="{REPO}">Source &amp; machine config on GitHub</a></p>
<h2>Contents</h2><ol class="toc">{toc}</ol>
<h2>Reproduce the machine</h2><p>The repository contains the complete working configuration (LinuxCNC 2.9.10, Mesa 7I96S with
PktUART firmware, Modbus VFD, probe, tool setter, pendant), wiring tables and an <code>AGENTS.md</code> written so an AI assistant can
walk you through rebuilding it on your own hardware.</p>"""
    (DOCS / "index.html").write_text(page(TITLE, index), encoding="utf-8")


def build_single(chs):
    """One self-contained HTML file for the EPUB and PDF converters."""
    parts = [f'<h1 class="booktitle">{html.escape(TITLE)}</h1><p>{html.escape(SUBTITLE)}</p><p>{html.escape(AUTHOR)}</p><p>{REPO}</p>']
    for ch in chs:
        parts.append('<div style="page-break-before: always"></div>' + md_to_html(ch["md"]))
    body = "\n".join(parts)
    css = CSS.split("@media")[0] + "body{background:#fff;color:#111} h1{page-break-before:always} h1.booktitle{page-break-before:avoid;font-size:2.6rem;margin-top:30%}"
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(TITLE)}</title>
<meta name="author" content="{html.escape(AUTHOR)}"><style>{css}</style></head><body><main>{body}</main></body></html>"""
    out = DOCS / "book.html"
    out.write_text(doc, encoding="utf-8")
    return out


def find(names):
    for n in names:
        p = shutil.which(n)
        if p:
            return p
        if os.path.exists(n):
            return n
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-epub", action="store_true")
    ap.add_argument("--no-pdf", action="store_true")
    a = ap.parse_args()
    chs = chapters()
    build_site(chs)
    single = build_single(chs)
    dl = DOCS / "downloads"
    dl.mkdir(exist_ok=True)
    if not a.no_epub:
        conv = find(["ebook-convert", r"C:\Program Files\Calibre2\ebook-convert.exe"])
        if conv:
            subprocess.run([conv, str(single), str(dl / "probe-basic-explained.epub"), "--title", TITLE, "--authors", AUTHOR,
                            "--language", "en", "--chapter", "//h:h1", "--level1-toc", "//h:h1", "--level2-toc", "//h:h2",
                            "--epub-version", "3"], check=True, stdout=subprocess.DEVNULL)
        else:
            print("ebook-convert not found: EPUB skipped", file=sys.stderr)
    if not a.no_pdf:
        chrome = find(["chromium", "google-chrome", r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
        if chrome:
            subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                            f"--print-to-pdf={dl / 'probe-basic-explained.pdf'}", single.resolve().as_uri()],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print("Chrome not found: PDF skipped", file=sys.stderr)
    print(f"built {len(chs)} chapters -> {DOCS}")


if __name__ == "__main__":
    main()

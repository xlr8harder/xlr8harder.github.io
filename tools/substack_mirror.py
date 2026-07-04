#!/usr/bin/env python3
"""Mirror public Substack posts into this Jekyll site as markdown.

Reads mirror.yml, fetches every public post of each configured publication
via Substack's JSON API, converts body HTML to markdown with pandoc,
vendors images into the repo, and writes deterministic output:
rerunning without upstream changes produces zero git diffs.

Usage:  python3 tools/substack_mirror.py [--config mirror.yml]
Deps:   pandoc, python3-yaml
"""

import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

import yaml

UA = {"User-Agent": "substack-mirror/1.0 (personal archive of own content)"}


def fetch_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def fetch_bytes(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read(), r.headers.get("Content-Type", "")


def list_posts(host):
    posts, offset = [], 0
    while True:
        batch = fetch_json(
            f"https://{host}/api/v1/archive?sort=new&limit=50&offset={offset}"
        )
        if not batch:
            break
        posts.extend(batch)
        offset += len(batch)
        time.sleep(0.3)
    return posts


def html_to_markdown(html):
    p = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
        input=html.encode(), capture_output=True, check=True,
    )
    return p.stdout.decode()


IMG_EXT = {"image/jpeg": ".jpg", "image/png": ".png", "image/gif": ".gif",
           "image/webp": ".webp", "image/svg+xml": ".svg"}


def guess_ext(url, content_type=""):
    inner = urllib.parse.unquote(url.split("/")[-1])
    m = re.search(r"\.(jpe?g|png|gif|webp|svg)\b", inner, re.I)
    if m:
        e = m.group(1).lower()
        return ".jpg" if e in ("jpeg", "jpg") else "." + e
    return IMG_EXT.get(content_type.split(";")[0].strip(), ".img")


def clean_markdown(md):
    """Strip Substack image chrome: data-URI icon images and bare zoom-link
    wrappers that duplicate the real image."""
    out = []
    for line in md.split("\n"):
        s = line.strip()
        if re.fullmatch(r"!\[\]\(data:[^)]*\)", s):
            continue
        if re.fullmatch(r"\[\]\((https://substackcdn\.com/image/[^)]*)\)", s):
            continue
        line = re.sub(r"!\[\]\(data:[^)]*\)", "", line)
        out.append(line)
    md = "\n".join(out)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md


def vendor_images(md, assets_dir, assets_rel):
    """Download substackcdn images into assets_dir; rewrite refs to relative
    paths. Filenames are content-addressed by URL hash: deterministic."""
    urls = set(re.findall(r"!\[[^\]]*\]\((https://substackcdn\.com/image/[^)\s]+)\)", md))
    for url in sorted(urls):
        h = hashlib.sha1(url.encode()).hexdigest()[:16]
        existing = list(assets_dir.glob(h + ".*"))
        if existing:
            fname = existing[0].name
        else:
            try:
                data, ctype = fetch_bytes(url)
            except Exception as e:
                print(f"    WARN: image fetch failed ({e}): {url[:80]}...")
                continue
            fname = h + guess_ext(url, ctype)
            assets_dir.mkdir(parents=True, exist_ok=True)
            (assets_dir / fname).write_bytes(data)
            time.sleep(0.2)
        md = md.replace("(" + url + ")", f"({assets_rel}/{fname})")
    return md


def yaml_str(s):
    return json.dumps(s or "", ensure_ascii=False)


def write_if_changed(path, content):
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def mirror_publication(pub, out_root):
    host, name = pub["host"], pub["name"]
    pub_dir = out_root / name
    assets_dir = pub_dir / "assets"
    print(f"== {name} ({host})")
    posts = [p for p in list_posts(host) if p.get("audience") in ("everyone", "only_free")]
    print(f"   {len(posts)} public posts")
    entries, keep = [], {"index.md"}

    for meta in posts:
        slug = meta["slug"]
        full = fetch_json(f"https://{host}/api/v1/posts/{slug}")
        time.sleep(0.3)
        body_html = full.get("body_html") or ""
        canonical = full.get("canonical_url") or f"https://{host}/p/{slug}"
        title = full.get("title") or slug
        subtitle = full.get("subtitle") or ""
        date = (full.get("post_date") or "")[:10]

        md = clean_markdown(html_to_markdown(body_html))
        md = vendor_images(md, assets_dir, "./assets")

        fm = [
            "---",
            f"title: {yaml_str(title)}",
            f"canonical_url: {yaml_str(canonical)}",
            "---",
            "",
            f"# {title}",
            "",
        ]
        if subtitle:
            fm.append(f"*{subtitle}*")
            fm.append("")
        fm.append(f"*Originally published on [{host}]({canonical}), {date}. This is a mirror.*")
        fm.append("")
        fm.append("---")
        fm.append("")
        content = "\n".join(fm) + md.strip() + "\n"

        fname = f"{slug}.md"
        keep.add(fname)
        changed = write_if_changed(pub_dir / fname, content)
        print(f"   {'updated' if changed else 'unchanged'}  {date}  {slug}")
        entries.append((date, title, subtitle, fname))

    # Remove mirrored posts that no longer exist upstream.
    for f in pub_dir.glob("*.md"):
        if f.name not in keep:
            print(f"   removed   {f.name} (no longer upstream)")
            f.unlink()

    entries.sort(key=lambda e: (e[0], e[3]), reverse=True)
    lines = [
        "---",
        f"title: {yaml_str(pub.get('title', name))}",
        "---",
        "",
        f"# {pub.get('title', name)}",
        "",
        f"*{pub.get('description', '')}*",
        "",
        f"Mirror of [{host}](https://{host}/). "
        "Generated by `tools/substack_mirror.py`; originals are canonical.",
        "",
    ]
    for date, title, subtitle, fname in entries:
        sub = f" — {subtitle}" if subtitle else ""
        lines.append(f"- {date} · [{title}](./{fname[:-3]}.html){sub}")
    lines.append("")
    write_if_changed(pub_dir / "index.md", "\n".join(lines))
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="mirror.yml")
    args = ap.parse_args()

    root = pathlib.Path(__file__).resolve().parent.parent
    cfg = yaml.safe_load((root / args.config).read_text())
    out_root = root / cfg.get("output_dir", "mirror")
    section_title = cfg.get("section_title", "Substack Mirror")

    pubs = cfg["publications"]
    all_entries = {}
    for pub in pubs:
        all_entries[pub["name"]] = mirror_publication(pub, out_root)

    lines = [
        "---",
        f"title: {yaml_str(section_title)}",
        "---",
        "",
        f"# {section_title}",
        "",
        "Markdown mirrors of my Substack publications, kept for durability and "
        "the open record. The Substack originals are canonical; each mirrored "
        "post links back to its source.",
        "",
    ]
    for pub in pubs:
        n = len(all_entries[pub["name"]])
        desc = f" — *{pub['description']}*" if pub.get("description") else ""
        lines.append(f"- **[{pub.get('title', pub['name'])}](./{pub['name']}/)** ({n} posts){desc}")
    lines.append("")
    write_if_changed(out_root / "index.md", "\n".join(lines))
    print("done.")


if __name__ == "__main__":
    main()

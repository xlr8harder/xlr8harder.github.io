# xlr8harder.github.io

Long-form records, transcripts, and archives, published at [xlr8harder.github.io](https://xlr8harder.github.io).

## How this site works

GitHub Pages renders this repo with Jekyll automatically — there is no build step and no local tooling.

**To publish something new:** add a markdown file anywhere in the repo, starting with a front-matter block:

```
---
title: Your Title
---
```

Commit, push, done. It renders to HTML at the same path (`foo/bar.md` → `/foo/bar.html`) with the shared stylesheet. A `title:` is the only thing worth setting; the layout is applied automatically via `_config.yml` defaults. Plain `.html` files without front matter are served verbatim (see `archive/neurallux/`).

Styling lives in `assets/main.scss` (overrides on the minima theme). Sitemap and SEO tags are generated automatically.

## Substack mirror

`tools/substack_mirror.py` mirrors the Substacks listed in `mirror.yml` into `/mirror/` (markdown + vendored images, canonical links back to the originals). Rerun after publishing:

```
python3 tools/substack_mirror.py   # needs pandoc, python3-yaml
git add -A && git commit -m "mirror refresh" && git push
```

Output is deterministic — no diffs unless posts changed upstream.

## Sections

- `/mindmeld-extended/` — full-length companions to [Mindmeld](https://mindmeldai.substack.com/) pieces
- `/archive/` — earlier experiments, preserved as they were
- `/mirror/` — Substack mirrors (generated; do not edit by hand)

# AGENTS.md

Guidance for agents (and forgetful humans) working in this repo.

## What this is

The GitHub Pages site for xlr8harder.github.io. Jekyll (minima theme), built
automatically by GitHub from the `main` branch root — **pushing to main is
publishing**. No build tooling is required to publish; markdown files with a
front-matter block render to HTML at the same path. `/mirror/` is generated —
never hand-edit it.

## Updating the Substack mirror after a post is published

**The one thing you must know:** a newly published post is available
immediately at `/p/<slug>` and via `/api/v1/posts/<slug>`, but Substack's
**archive listing** (`/api/v1/archive`) — which the importer walks — **lags
publication by many minutes** (observed 2026-07: 10+ minutes). A plain import
run right after publishing will silently miss the new post.

So when the request is "I posted, update the mirror," do this:

```
./tools/sync.sh
```

It polls the archive listings until a not-yet-mirrored post appears (up to 15
minutes; pass a number to change), imports everything, commits, and pushes.
Equivalent manual form: `python3 tools/substack_mirror.py --poll`, then
commit and push.

For anything that isn't a brand-new post (edits to old posts, config changes),
plain `python3 tools/substack_mirror.py` suffices — it refetches everything,
and output is deterministic: no diffs unless upstream actually changed.

Publications live in `mirror.yml`. Deps: `pandoc`, `python3-yaml`.

## Testing the build locally

GitHub builds the site on push, but to check before pushing:

```
PATH="$(ruby -e 'print Gem.user_dir')/bin:$PATH" jekyll build -d /tmp/_site
```

Or preview with live rebuilds:

```
jekyll serve
```

Things that bite: a `.md` file without a leading `---`/`---` front-matter
block is served as raw text, not rendered; the header nav is pinned via
`header_pages` in `_config.yml` (don't let new pages auto-populate it);
styling overrides live in `assets/main.scss` (that exact path — minima
ignores stylesheets elsewhere).

## Deploy hiccups

The Pages deploy step occasionally fails with "Deployment failed, try again
later" even when the build succeeds (observed 2026-07: three consecutive
failures over ~10 hours, then success). The site keeps serving the last good
deploy, so nothing user-facing breaks. Retry with an empty commit, or check
`gh run list` / re-run from the Actions tab.

# AGENTS.md

Guidance for agents (and forgetful humans) working in this repo.

## What this is

The GitHub Pages site for xlr8harder.github.io. Jekyll (minima theme), built
automatically by GitHub from the `main` branch root — **pushing to main is
publishing**. No build tooling is required to publish; markdown files with a
front-matter block render to HTML at the same path. `/mirror/` is generated —
never hand-edit it.

## Updating the Substack mirror after a post is published

**Background:** a newly published post is available immediately at
`/p/<slug>`, via `/api/v1/posts/<slug>`, and in the publication's
`sitemap.xml` — but Substack's **archive listing** (`/api/v1/archive`) lags
publication substantially (observed 2026-07: 30+ minutes). The importer
therefore discovers posts from the **union of the archive listing and the
sitemap**, so a plain run works immediately after publishing.

When the request is "I posted, update the mirror," do this:

```
./tools/sync.sh
```

It imports everything (waiting briefly if needed — `--poll` checks sitemaps
too, so new posts are found within seconds), commits, and pushes. Equivalent
manual form: `python3 tools/substack_mirror.py`, then commit and push.

For anything that isn't a brand-new post (edits to old posts, config changes),
plain `python3 tools/substack_mirror.py` suffices — it refetches everything,
and output is deterministic: no diffs unless upstream actually changed.

Publications live in `mirror.yml`. Deps: `pandoc`, `python3-yaml`.

## Importing fragments (from the owner's private vault)

`/archive/fragments/` holds stories and notes imported from private markdown
vaults. Procedure: strip the vault frontmatter and the `## Summary` /
`## Full Text` cataloging headers; keep the text verbatim otherwise (bulleting
line-stacked lists for markdown rendering is OK). Date each piece by the
frontmatter **`created`** date, never `modified`. Scrub before committing:
no source paths, no usernames, personal names reduced to initials — grep the
staged content for identity strings every time. The owner approves each piece
individually; the publishing queue lives in the vault's `_Reading Guide.md`.

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

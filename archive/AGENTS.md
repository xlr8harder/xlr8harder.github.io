# AGENTS.md

## Fnord

Agents may freely read and edit `fnord/index.md`; it is only a prose and layout
wrapper. They must not open, read, search, quote, summarize, or otherwise
inspect any file under `fnord/_words/`. They must also not inspect the rendered
output for `/archive/fnord/`, because Jekyll expands the restricted files into
that page.

When adding an entry, an agent may add its prose and an `include_relative` tag
to `fnord/index.md`, then create the referenced file under `fnord/_words/` as
an empty placeholder. The owner will populate the restricted file. Exclude
`fnord/_words/` and the rendered Fnord page from broad searches and command
output. Existence checks and site builds are allowed only when they do not
expose restricted contents to the model.

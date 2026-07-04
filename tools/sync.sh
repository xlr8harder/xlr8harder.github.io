#!/usr/bin/env bash
# One-command mirror sync after publishing a Substack post:
# waits for the new post to reach the archive listing, imports, commits, pushes.
#   ./tools/sync.sh [poll-minutes]
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/substack_mirror.py --poll "${1:-15}"
if git status --porcelain | grep -q .; then
  git add -A
  git commit -m "mirror refresh"
  git push origin main
  echo "mirror synced and pushed."
else
  echo "no changes."
fi

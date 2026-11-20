#!/usr/bin/env bash
# Wire this kit's skills into Claude Code so they load in every session.
#
# Puts a symlink for each skill folder into $KIT (default ~/.claude/skills, where Claude Code
# looks for user-level skills). Because they are links, a `git pull` here is live in the next
# session with nothing else to run.
#
# Idempotent: safe to re-run. Repairs a broken or moved link rather than failing.
set -euo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
KIT="${KIT:-$HOME/.claude/skills}"
FOLDERS=(peachy-adventure peachy-chart peachy-sweep peachy-work peachy-build peachy-gate)

mkdir -p "$KIT"

# Prune dangling links first, but only this kit's own folder names: a dead link is a skill that
# silently fails to load. Links to anything else in $KIT are left alone.
for f in "${FOLDERS[@]}"; do
  dst="$KIT/$f"
  if [ -L "$dst" ] && [ ! -e "$dst" ]; then
    echo "prune $f  (was -> $(readlink "$dst"))"
    rm "$dst"
  fi
done

for f in "${FOLDERS[@]}"; do
  src="$REPO/skills/$f"
  dst="$KIT/$f"
  [ -d "$src" ] || { echo "FAIL: $src missing"; exit 1; }

  if [ -L "$dst" ]; then
    [ "$(readlink "$dst")" = "$src" ] && { echo "ok    $f"; continue; }
    rm "$dst"; ln -s "$src" "$dst"; echo "fixed $f"
  elif [ -e "$dst" ]; then
    echo "FAIL: $dst exists and is not a symlink. Move it aside by hand."; exit 1
  else
    ln -s "$src" "$dst"; echo "link  $f"
  fi
done

for f in "${FOLDERS[@]}"; do
  [ "$f" = peachy-adventure ] && continue   # shared resources, no SKILL.md by design
  head -1 "$KIT/$f/SKILL.md" | grep -q '^---$' || { echo "FAIL: $f/SKILL.md has no frontmatter"; exit 1; }
done

echo "GREEN: 5 skills plus shared resources wired into $KIT"

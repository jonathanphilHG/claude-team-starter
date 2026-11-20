#!/usr/bin/env bash
# PreToolUse guard for Bash commands. Claude Code pipes the pending tool call to this script as
# JSON on stdin. Exit 2 blocks the call (stderr is the reason Claude sees); exit 0 lets it through.
#
# It runs in every permission mode, bypass included, which is why it exists. A text match is a
# seatbelt, not a security boundary (a determined command can dodge it), so pair it with the
# permissions.deny rules in hooks/README.md. Add your own patterns to BLOCK.
#
# It matches anywhere in the tool call, so a commit message that merely mentions one of these
# commands gets blocked too. Rephrase the message, or commit from your own terminal.
input="$(cat)"
BLOCK='rm +-[a-zA-Z]*([rR]f|f[rR])|rm +-[a-zA-Z]*[rR][a-zA-Z]* +-[a-zA-Z]*f|rm +-[a-zA-Z]*f[a-zA-Z]* +-[a-zA-Z]*[rR]|rm [^"]*--recursive|git +push[^"]*(--force([^-a-zA-Z]|$)|[[:space:]]-f([[:space:]]|"|$)|[[:space:]]\+[A-Za-z0-9_./-])|git +reset +--hard|git +clean +-[a-zA-Z]*f'
if printf '%s' "$input" | grep -Eq "$BLOCK"; then
  echo "Blocked by the kit's guard hook (hooks/guard.sh): destructive command. If it is really intended, ask the user to run it themselves." >&2
  exit 2
fi
exit 0

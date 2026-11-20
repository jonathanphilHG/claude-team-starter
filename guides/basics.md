# Claude Code basics

How it works under the hood, so you can tune it instead of fighting it. Checked against the
Claude Code docs in November 2026; the docs win if anything here drifts:
https://code.claude.com/docs

Paths are written the macOS and Linux way (`~/.claude/...`). On Windows the same folder is
`%USERPROFILE%\.claude\...`.

## The pieces

| Piece | What it is | Where it lives | Cost |
|---|---|---|---|
| `CLAUDE.md` | Standing instructions | `~/.claude/CLAUDE.md` (you, everywhere), `<repo>/CLAUDE.md` (one project) | Loads in full, every session |
| Skills | A folder with a `SKILL.md`: instructions (and files) Claude pulls in when a task matches the description, or when you type `/name` | `~/.claude/skills/<name>/`, or inside a plugin | Description every session; body only when used |
| Plugins | Installable bundles of skills, commands, hooks and MCP servers | `claude plugin install <name>@<marketplace>` | Whatever they contain |
| MCP servers | Tools that reach other systems (GitHub, Google, databases) | `claude mcp add ...` | Tool list every session |
| Memory | Notes Claude keeps about you and your projects between sessions | Managed per project folder; `/memory` to see it | Index every session |
| Hooks | Shell commands the harness runs on events (before a tool call, at the end of a turn) | `settings.json` | Mechanical: they always run |
| Settings | Model, permissions, overrides, hooks | `~/.claude/settings.json` (you), `.claude/settings.json` (one project) | None |

**Rule of thumb:** a preference goes in `CLAUDE.md`, a procedure goes in a skill, and anything that
must happen every single time goes in a hook. Claude can forget a `CLAUDE.md` line; it cannot
forget a hook.

## Models, effort, subagents

- `/model` switches the model, and `/config` holds effort and the rest. Use the most capable model
  for planning, design and hard bugs; a faster one is fine for routine edits.
- **Higher effort means more thinking before acting.** Worth it for planning and debugging,
  wasted on a rename.
- **Subagents** are helpers Claude spawns for parallel research or isolated tasks. Each starts with
  a blank slate and knows only what its prompt says, so ask Claude to brief them properly. You can
  tell Claude which model its subagents use ("run subagents on Opus").

## Permission modes

Shift+Tab cycles modes during a session; `permissions.defaultMode` in `~/.claude/settings.json`
sets where you start.

| Mode | What happens | Use it when |
|---|---|---|
| `default` | Asks before every edit and command | You're learning what Claude does |
| `acceptEdits` | File edits go through; commands still ask | Careful work in a repo you care about |
| `auto` | A separate classifier model reviews each action and blocks anything beyond what you asked, anything aimed at systems it doesn't recognize, or anything that looks driven by hostile content | Day to day. Recent versions start here by default |
| `plan` | Reads and plans, changes nothing | Before a big change |
| `bypassPermissions` | No prompts at all | Long unattended runs, throwaway sandboxes, or when you trust the guardrails below |

### Bypass, properly

Bypass is the fastest mode and the one that can hurt you, so set it up with its seatbelts on.

**What still protects you in bypass:**
- `permissions.deny` rules: they block in every mode, including bypass.
- Explicit `permissions.ask` rules: they still prompt.
- Hooks: a `PreToolUse` hook runs before every tool call and can block it. (`allow` rules do
  nothing in bypass, since everything is already allowed.)

**Turn it on for one session:** `claude --dangerously-skip-permissions`, or
`claude --permission-mode bypassPermissions`. To keep it one Shift+Tab away without starting in
it: `claude --allow-dangerously-skip-permissions`.

**Make it the default:** in `~/.claude/settings.json` (user settings only, since project settings
ignore it on purpose), set the mode and skip the one-time warning:

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push --force *)",
      "Bash(git push -f *)",
      "Bash(git reset --hard *)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(~/.ssh/**)"
    ]
  },
  "skipDangerousModePermissionPrompt": true,
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [ { "type": "command", "command": "bash \"$HOME/path/to/guard.sh\"" } ]
      }
    ]
  }
}
```

`hooks/guard.sh` in this kit (see `hooks/README.md`) blocks `rm -rf` in its common spellings, `git push --force`, `-f` and
`+branch` (but allows the safer `--force-with-lease`), `git reset --hard`, and `git clean -f`.
Because it matches the whole tool call, a commit message that merely mentions one of those gets
blocked too: rephrase it. It is a
seatbelt, not a vault: a creatively spelled command can get past a text match, which is why the
deny rules sit next to it. **Test it once before wiring it in** (the steps are in `hooks/README.md`): it should print the
block message and `2`.

**Turn it off again:** set `defaultMode` back to `auto`. To forbid bypass entirely:
`"permissions": { "disableBypassPermissionsMode": "disable" }`.

**Habits that make bypass safe:** commit before a big run (git is your undo button), work on a
branch, and keep anything precious (keys, other people's data) out of the folders Claude works in.

### Allowlists, for the other modes

`permissions.allow` with patterns like `"Bash(npm test *)"` or `"Bash(git status)"` stops the
prompts for commands you always approve. After a week of use, the built-in
`/fewer-permission-prompts` skill reads your history and proposes a list.

## Power settings

- **Phone notifications:** `"inputNeededNotifEnabled": true` pings you when Claude is waiting on
  you; `"agentPushNotifEnabled": true` lets Claude ping you when a long task finishes. Both need
  Remote Control plus the mobile push setup on the Remote Control docs page. Desktop and terminal
  notifications use a separate setting in `/config`.
- **Remote Control:** follow and steer a terminal session from the Claude app on your phone.
  `claude --remote-control` for one session, or `"remoteControlAtStartup": true` for every session.
- **Status line:** `/statusline` builds one for you (model, folder, git branch, context used).
- **Shift+Enter for new lines:** run `/terminal-setup` once.
- **Keep history:** transcripts are deleted after 30 days unless you set `"cleanupPeriodDays": 365`
  (or more). `claude --continue` and `claude --resume` reopen past sessions.
- **Parallel sessions:** `claude -w <name>` starts a session in its own git worktree, so two
  sessions can work in one repo without stepping on each other.
- **Headless:** `claude -p "prompt"` runs one prompt and exits; good for scripts.
- **Dictation:** talking is faster than typing long prompts. A dictation app or your operating
  system's built-in dictation both work.

## Context budget

Everything always-on is paid for in every session: `CLAUDE.md` in full, every skill's description,
every MCP server's tool list. `/context` shows where it goes.

- **Mute a skill you never want picked automatically:**
  `"skillOverrides": { "mattpocock-skills:prototype": "off" }` in `~/.claude/settings.json`.
  The key is `plugin-name:skill-name` for plugin skills, just the folder name for your own.
- **`/compact`** when a long session gets sluggish, but write state to a file first (`lessons.md`, item 13).
  **`/clear`** for a fresh start.

## Common skills, and when they fire

Some of these come from public plugins (see `public-installs.md`); install only what you want.

| You want to | Skill | How |
|---|---|---|
| Build something new | `superpowers:brainstorming`, then `writing-plans`, then `executing-plans` or `subagent-driven-development` | Describe the idea |
| Fix a bug | `superpowers:systematic-debugging` | Describe the bug |
| Write tests first | `superpowers:test-driven-development` | Ask for TDD |
| Commit | `commit` | `/commit`, or Claude offers at a checkpoint |
| Push and open a PR | `push` | `/push` on a feature branch (it refuses `main` on purpose) |
| Stress-test a plan | `grill-me`, `grilling` (public, see `public-installs.md`), or `grill-with-docs` | `/grill-me` |
| Plan a code project bigger than one session | `wayfinder` (public) | `/wayfinder` |
| Research a question with real sources | `research` (public) | `/research` |
| Hand off to a fresh session | `handoff` (public) | `/handoff` |
| A big non-code project | `peachy-chart`, then `peachy-work` and `peachy-gate` | "chart this as a Peachy map" (see `big-projects.md`) |
| Word, PowerPoint, PDF, Excel | document skills | Just ask for the file |
| Write your own skill | `superpowers:writing-skills` | Ask |

## Make your own skill

A skill is a folder with a `SKILL.md`: frontmatter with `name` (matching the folder) and
`description`, then plain instructions. Copy or link the folder into your skills folder (see
`skills-in-github.md`). The description decides when it fires, so say concretely when to use it ("Use when the user asks to
X, or when Y happens"). `superpowers:writing-skills` goes deeper.

## The validate convention

One line per repo at `.claude/validate`: a shell command that exits non-zero when the repo is
broken (`npm test`, `pytest -q`). `/commit` and `/push` run it and refuse to commit or push red.
Details in step 2 of `skills/commit/SKILL.md`.

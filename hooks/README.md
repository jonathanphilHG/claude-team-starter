# guard.sh: a seatbelt hook (Claude Code only, optional)

`guard.sh` is a small script Claude Code runs before every shell command Claude wants to run. If
the command looks destructive, the script blocks it and tells Claude to ask you instead.

It only matters in Claude Code. claude.ai chats do not run commands on your computer.

## What it blocks

- `rm -rf` and its common spellings (`rm -fr`, `rm -r -f`, `rm --recursive`)
- `git push --force`, `git push -f` and `git push origin +branch` (the safer
  `--force-with-lease` is allowed)
- `git reset --hard`
- `git clean -f`

It checks the whole command text, so a commit message that merely mentions one of these gets
blocked too. Rephrase the message.

It is a seatbelt, not a vault. A creatively spelled command can get past a text match, which is
why the deny rules below sit next to it.

## Why you might want it

Hooks run in every permission mode, including the one where Claude asks nothing at all. A line
in `CLAUDE.md` can be forgotten; a hook cannot.

## Turning it on

1. Keep `guard.sh` somewhere stable, for example in your copy of this kit.
2. **Test it before wiring it in** (once wired, it would block its own test). From the folder
   that holds it:

   ```
   printf '{"tool_input":{"command":"rm -rf /tmp/x"}}' | bash guard.sh; echo $?
   ```

   It should print the block message and `2`. A harmless command (`ls -la` in place of the
   `rm`) should print `0`.
3. Add this to your user settings file (`~/.claude/settings.json` on macOS or Linux,
   `%USERPROFILE%\.claude\settings.json` on Windows), merged with whatever is already there.
   Change the path to where you keep `guard.sh`:

   ```json
   {
     "permissions": {
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

4. Start a fresh session. If something is later blocked with "Blocked by the kit's guard hook",
   that is the hook working. Run the command yourself if you really meant it.

## Turning it off

Delete the `hooks` block from the settings file and start a fresh session.

## Windows

`guard.sh` is a bash script, so it needs a bash on the machine (Git for Windows includes one).
It has not been tested on Windows.

## Adding your own patterns

Edit the `BLOCK` line in `guard.sh`. It is one extended regular expression. Test again after
every change.

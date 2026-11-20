# Lessons

Learned the expensive way, running Claude Code on real projects every day. Each one cost at
least one bad afternoon. Steal the ones that fit; put the ones you want enforced into your
standing instructions (`CLAUDE.md` in Claude Code, project instructions or personal preferences in
claude.ai), because Claude does not read this file on its own.

## Scope

1. **Build the smallest thing that runs end to end, then improve it.** A beautiful plan with zero
   lines built is the most common way to lose a week.
2. **Cap review rounds before you start:** one for docs, two for code that matters. An AI reviewer
   on prose never runs out of comments. Fix only what changes what someone would do.
3. **When more thoroughness stops changing the outcome, stop.** Say so out loud and ship.

## Trust, but check

4. **Verify the artifact, not the report.** Subagents and past sessions summarize confidently and
   are sometimes wrong. Open the file, run the test, read the diff.
5. **"It doesn't exist" is a claim that needs evidence.** Before Claude says a file, tool or setting
   is missing, it should show where it looked. A tool missing from this session is not the same as
   a thing that cannot be reached.
6. **A search that "confirms" can be wrong.** A grep for a bad phrase will happily match the
   correction that quotes it. Look at what actually matched.
7. **Summaries invent quotes.** When an exact quote, number or name matters, go back to the source.
8. **Read the live state before asking anyone to change it.** Check it still exists and still says
   what you think before you email a vendor, a customer, or a teammate about it.

## Anything that leaves your machine

9. **Preview every write to the outside world** (send, post, push, delete, pay, invite). When there
   are several, have Claude put them all in one table and approve once, instead of twenty prompts.
10. **Read every message before it goes out.** "Yes, send it" covers the text you saw, not a later
    edit.
11. **Dry run first, then the real thing.**
12. **Secrets never go in a repo or a chat:** `.env` files, keys, tokens, passwords. Config is fine;
    credentials are not. If one leaks, rotate it, deleting the commit is not enough.

## Sessions and context

13. **Write state to a file before the context fills up.** A `LOG.md` at the top of the project
    with "where we are, what's next". Compaction loses detail; files don't.
14. **Keep a running log, newest first.** A plan is not a log. Future you needs to know what
    actually happened.
15. **Hand off with one copyable block at the end:** what's done, what's next, where the files are.
    Then start the new session with it.
16. **Fan out subagents for parallel work, and brief them like a new teammate.** Each one knows only
    what you put in its prompt. Their reports are claims; see 4.
17. **Everything always-on costs context in every session:** CLAUDE.md lines, skill descriptions,
    MCP servers. Check with `/context` now and then and prune what you don't use.

## Working with Claude

18. **Ask for a recommendation, not a menu.** "What would you do, and why?" beats "what are my
    options?"
19. **Research and drafts in markdown first.** Pretty formats (Docs, slides, PDFs) last, once the
    content is right.
20. **Write decisions down with the why.** A short `decisions.md` is enough. Later you will want to
    undo something and won't remember why it was done.
21. **When a skill misfires, fix it.** Fires too often or never: sharpen its description, or turn it
    off with `skillOverrides` (see `basics.md`). Don't just live with it.

## Shell traps (macOS)

- macOS has no `timeout` command. `brew install coreutils` gives you `gtimeout`.
- In zsh, never name a loop variable `path`: it is tied to `PATH` and wipes it mid-loop.
- In zsh, a word that starts with `=` (like `=====` as a divider) is a command lookup and errors.

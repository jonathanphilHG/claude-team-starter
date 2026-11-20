---
name: web-app-to-api-reference
description: "Turn a task a person does by clicking through a web app into a repeatable call to the app's own API, with a written reference and a small script so the next run does not relearn it. Use when someone keeps doing the same task by hand in a browser, wants to automate or script a web app, asks what API a page calls, or hands over a HAR file."
---

# Web app to API reference

Find the calls a web app makes for one task, write them down, prove them, then script the
repeat. The long version, with the reasons, is `guides/map-a-web-app.md` in the starter kit this
skill came from, if you still have it. This skill works without it.

## Safety rules (they come first)

- **Read-only calls first.** Nothing that changes data until reads are proven.
- **Never send a write to a live system without the person's go on that exact call:** method,
  path, full body, record id. Show it, wait for "go", send it once.
- **A HAR file holds session secrets** (cookies, tokens, sometimes passwords in bodies). Keep it
  out of git (`*.har` in `.gitignore` before the file arrives), keep it outside the repo folder,
  never print it raw or paste it into chat, and delete it once `API.md` is written.
- **Header names, never values.** Never ask for a password or token. Never list cookies or
  browser storage hunting for one.
- **Respect the app's terms of use.** If they forbid automated access, or the person is unsure,
  stop and say so. An official API or an export feature is the route then.
- **First writes go to one throwaway record** ("ZZ TEST delete me"), never a real customer.
- **If your skills folder is a shared or public repository**, keep the `apps/` notes in a separate
  private folder instead (ask the person where), and never commit a `.env`.

## Before you start

Ask in one message:
1. Which app, and the task as numbered steps, the way they click it today.
2. Which account and role they use (never the password).
3. Do they own or administer the app, and do its terms allow scripted access?

If `apps/<app-name>/` already exists in this skill folder, read its `API.md`, `STATUS.md` and
script first. The work may already be done.

## Step 1: cheaper sources first

- A published spec: try `/openapi.json`, `/swagger.json` or `/api/docs` on the API host, and
  search the vendor's help center for "API".
- An official API or export that covers the task: use it and skip the capture.
- GraphQL apps embed their queries as plain text in the app's JavaScript bundle.

Note what each source showed and the date.

## Step 2: capture what the browser sends

Give the person this checklist:
1. Chrome, signed in as usual. Open DevTools (Cmd+Option+I on a Mac, F12 or Ctrl+Shift+I on
   Windows), then the Network tab. Tick **Preserve log**.
2. Do the numbered steps one at a time, letting each page settle. Writes go to the throwaway
   record only.
3. Reload the page once at the end (it shows every read the app does on startup).
4. Export the HAR (the sanitized option). Save it outside any repo folder, for example Downloads.

## Step 3: summarise it, never read it raw

Run `har_summary.py`, which sits in this skill's folder. Write the summary next to the HAR,
outside any repo or shared folder, and never into the skill folder:

```
python3 <this skill's folder>/har_summary.py <capture.har> --out <folder outside any repo>/summary.md
python3 <this skill's folder>/har_summary.py <capture.har> --host <api host> --bodies --out <folder outside any repo>/summary-bodies.md
```

The first run lists the hosts; pick the API host for the second. The script prints header names
but never values, drops query strings, and redacts secret-looking values and token-shaped text in
bodies. A plain summary (no `--bodies`) is what you may show someone. A `--bodies` summary is for
your own eyes only: names, phone numbers and addresses in the bodies are not redacted. Never share
or commit it, and delete it with the HAR. If the script is
not available, still do not open the HAR directly: write a short script that follows the same
rules, and run that.

Then match each numbered step to the calls that fired, name the auth pattern (header names
only), and for GraphQL group the bodies by `operationName`. Trust the path and body, not the
button label.

## Step 4: write API.md and STATUS.md

Use `templates/API.md` and `templates/STATUS.md` beside this file. Save them in
`apps/<app-name>/` in this skill folder, or a folder the person picks.

- `API.md`: provenance (date, host, account, which HAR), auth (names only), one section per call
  with a sample body (values replaced by types), and limits (what was refused, where, when, the
  exact error).
- `STATUS.md`: last updated, a capability table with dated evidence, corrections kept on record.

Mark every call as one of:
- **PROVEN**: replayed on a date, on a named record, confirmed by a fresh read.
- **SEEN**: in the HAR, not replayed. An assumption until proven.
- **UNTESTED**: not tried. Never write "unavailable" for something nobody tried.

## Step 5: prove the calls

1. Replay one read. Prefer the logged-in tab's console (`fetch` with
   `credentials: 'same-origin'`), so the token never leaves the browser. Compare with the screen.
2. For a write: print the exact request, wait for the person's go, send once to the throwaway
   record, then confirm with a fresh read through a different call or the screen.
3. Read the response body, not just the status: a 200 can carry an error. A timeout may still
   have executed: read before retrying.

Update `STATUS.md` after each proof.

## Step 6: script the repeat task

Only once every call the task needs is PROVEN:
- Write one small script in `apps/<app-name>/` (Python, or JavaScript for the browser console).
- Dry run by default: it prints what it would send. A `--send` flag does the real thing, and
  still waits for the person's go before writes they have not approved as a batch.
- Secrets by variable name from a gitignored `.env`, or run from the logged-in tab. Never in
  the script.
- A header comment: what it does, which calls, the date they were proven.

## Step 7: record it so the next run does not relearn it

- Add one line under "Known apps" below: app, task, folder, date proven.
- Add the round to `STATUS.md`: what was proven, what is still open.
- Delete the HAR, and write the date it was deleted in `STATUS.md`.
- In a chat with no file access, hand the person the files and the Known apps line to save.

## Known apps

(none yet)

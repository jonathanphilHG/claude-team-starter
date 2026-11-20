# Work by voice while sessions run on a computer

A way to keep working when you cannot look at a screen (driving, walking): you talk to a voice
Claude on your phone, while working sessions keep going on a computer. Two shared documents
carry everything between them.

## The setup

- **A voice Claude on your phone.** Its only job is to listen, write down what you say, and read
  back what the working session wrote.
- **Working sessions on a computer** (Claude Code), left running with internet access. They do
  the actual work.
- **Two shared documents** both sides can read and write (a Google Doc, a Word file in shared
  storage, anything both can reach):
  - **IN:** your spoken notes, prompts and feedback, written down by the voice Claude. One
    dated line per note, newest at the end.
  - **OUT:** what the working session wants you to hear: status, questions, drafts.

## What it needs

- **Phone side:** a Claude that can write to a shared doc, which means a document connector with
  write access. If voice mode on your plan cannot use a connector, dictate into the IN doc
  directly instead (your phone's own dictation, in the doc app), and skip the voice Claude.
- **Computer side:** a Claude Code session that is told to re-check the IN doc on a timer. It does
  not poll by itself: the opening prompt below asks it to, and it needs a way to wait and look
  again (a recurring-prompt command such as `/loop` where your version has one, or a short wait
  loop). Keep the computer awake and the session open.

## How a round goes

1. You talk. The voice Claude appends your note to the IN doc with the time.
2. The working session checks the IN doc every few minutes, because you told it to. When it
   changes, it reads the new lines and acts on them.
3. The working session appends to the OUT doc.
4. You ask the voice Claude "what's new?" and it reads the OUT doc aloud.

## How the OUT doc is written

It will be heard, not read, so the working session writes for the ear:

- Short sentences. No tables, no links read aloud, no code.
- Status first, in one or two sentences.
- **Every question comes with a default answer**: "Should I send the draft to the vendor? If I
  don't hear back, I'll hold it until you're at a desk." You can answer with one word, or not
  at all, and work still moves.
- Drafts are short enough to listen to. Anything long waits for the screen.

## Rules worth setting

- **Nothing goes out to another person on a voice yes alone.** Drafts wait until you can read
  the exact text. (This matches "nothing sends without my go on that exact text".)
- **Interruptions are rare.** The working session sends you a short ping (a text, a phone
  notification) only when it is truly blocked. Everything else goes in the OUT doc.
- **Reuse the same two docs.** For a new day or a new session, add a dated heading at the end of
  each doc rather than making new docs.
- **Cheap checking.** The working session can look at the IN doc's "last modified" time and only
  read the text when it has changed.
- **Back at the desk:** read the OUT doc once on screen, send what was held, and stop the
  checking.

## Telling the working session

Paste something like this at the start:

> I'm going to be away from the screen. Check the IN doc (link) every few minutes and act on new
> lines. Write status, questions (each with a default answer) and short drafts to the OUT doc
> (link), written to be read aloud. Only ping me if you are blocked. Send nothing to anyone
> until I have read the exact text on a screen.

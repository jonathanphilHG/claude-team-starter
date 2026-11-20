#!/usr/bin/env bash
# Leak checker for this kit. Run it before you share a copy: bash check.sh
# Exits 0 and prints GREEN when clean, exits 1 and prints every problem when not.
# Needs bash and Python 3 (on Windows, Git Bash plus Python works).
#
# It scans every file in this folder (except .git) for:
#   - names on your private block list (see below)
#   - email addresses (other than example.com), phone numbers, personal folder paths,
#     cloud-drive paths, long document-ID-looking strings, GitHub accounts not on the allow list
#   - long dashes (em, en, figure dash, horizontal bar)
#   - skill folders whose SKILL.md lacks frontmatter or whose name does not match the folder
#
# The private block list: put the names you never want to ship in a file called
# .private-blocklist in this folder, one word or phrase per line (a line starting with # is a
# comment). It is listed in .gitignore so it is never committed, and this checker skips it.
# Each entry matches as a whole word or phrase, in any case, and a phrase still matches when a
# line break falls between its words. With no such file, only the generic checks run.
set -uo pipefail
cd "$(dirname "$0")"
exec python3 -I - "$@" <<'PY'
import os, re, sys

BLOCKLIST_FILE = ".private-blocklist"
GITHUB_ALLOW = {"obra", "mattpocock", "anthropics", "thebushidocollective"}


def load_blocklist():
    if not os.path.isfile(BLOCKLIST_FILE):
        return None
    entries = []
    for raw in open(BLOCKLIST_FILE, encoding="utf-8").read().splitlines():
        entry = raw.strip()
        if not entry or entry.startswith("#"):
            continue
        words = entry.split()
        body = r"\s+".join(re.escape(w) for w in words)
        rx = re.compile(r"(?<![A-Za-z0-9])" + body + r"(?![A-Za-z0-9])", re.IGNORECASE)
        entries.append((rx, len(words) > 1))
    return entries


BLOCK = load_blocklist()

PATTERNS = [
    ("long dash", re.compile("[" + "".join(map(chr, (0x2012, 0x2013, 0x2014, 0x2015))) + "]")),
    ("email address", re.compile(r"[A-Za-z0-9._%+-]+@(?!example\.(?:com|org|net)\b)[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")),
    ("phone number", re.compile(r"(?<![\d-])(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?![\d-])|\+\d{10,}")),
    ("personal folder path", re.compile(r"/Use[r]s/|[A-Za-z]:\\{1,2}Use[r]s\\|/hom[e]/[a-z]")),
    ("cloud drive path", re.compile(r"CloudStorag[e]|GoogleDriv[e]-|docs\.googl[e]\.com/|driv[e]\.google\.com/")),
]
ID_RE = re.compile(r"(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{25,}(?![A-Za-z0-9_-])")
GITHUB_RE = re.compile(r"github\.com[/:]([A-Za-z0-9_.-]+)")
LEADING_MARKERS = re.compile(r"^\s*(?:[>#*-]+\s*)*")

problems = []


def scan_line(path, n, line):
    for label, rx in PATTERNS:
        m = rx.search(line)
        if m:
            problems.append("%s:%d: %s: %r" % (path, n, label, m.group(0)))
    for m in ID_RE.finditer(line):
        t = m.group(0)
        if re.search("[A-Z]", t) and re.search("[a-z]", t) and re.search("[0-9]", t):
            problems.append("%s:%d: document-ID-looking string: %r" % (path, n, t))
    for m in GITHUB_RE.finditer(line):
        if m.group(1).lower() not in GITHUB_ALLOW:
            problems.append("%s:%d: GitHub account not on the allow list: %r" % (path, n, m.group(1)))
    for rx, _ in BLOCK or ():
        for m in rx.finditer(line):
            problems.append("%s:%d: on the private block list: %r" % (path, n, m.group(0)))


def scan_join(path, n, line, nxt):
    """Catch a block-list phrase split across this line and the next one."""
    head = line.rstrip()
    joined = head + " " + LEADING_MARKERS.sub("", nxt)
    for rx, is_phrase in BLOCK or ():
        if not is_phrase:
            continue
        for m in rx.finditer(joined):
            if m.start() < len(head) < m.end():
                problems.append("%s:%d-%d: on the private block list, across a line break: %r"
                                % (path, n, n + 1, " ".join(m.group(0).split())))


files = 0
for root, dirs, names in os.walk("."):
    dirs[:] = sorted(d for d in dirs if d != ".git")
    for name in sorted(names):
        path = os.path.join(root, name)[2:]
        if name == ".DS_Store" or path == BLOCKLIST_FILE:
            continue  # gitignored: macOS folder file, and the private list itself
        try:
            text = open(path, encoding="utf-8").read()
        except UnicodeDecodeError:
            problems.append("%s: not UTF-8 text, check it by hand" % path)
            continue
        files += 1
        lines = text.splitlines()
        for n, line in enumerate(lines, 1):
            scan_line(path, n, line)
            if n < len(lines):
                scan_join(path, n, line, lines[n])

for base in ("skills", os.path.join("peachy", "skills")):
    if not os.path.isdir(base):
        continue
    for folder in sorted(os.listdir(base)):
        f = os.path.join(base, folder, "SKILL.md")
        if not os.path.isfile(f):
            continue
        lines = open(f, encoding="utf-8").read().splitlines()
        if not lines or lines[0] != "---":
            problems.append("%s: no frontmatter opener" % f)
        if ("name: %s" % folder) not in lines:
            problems.append("%s: frontmatter name missing or does not match the folder" % f)
        if not any(l.startswith("description: ") for l in lines):
            problems.append("%s: no description in frontmatter" % f)

if BLOCK is None:
    listed = "no %s found, so no names were checked" % BLOCKLIST_FILE
else:
    listed = "%d entries on the private block list" % len(BLOCK)
if problems:
    print("\n".join(problems))
    print("RED: %d problem(s) in %d files scanned (%s)" % (len(problems), files, listed))
    sys.exit(1)
print("GREEN: %d files scanned, nothing found (%s)" % (files, listed))
PY

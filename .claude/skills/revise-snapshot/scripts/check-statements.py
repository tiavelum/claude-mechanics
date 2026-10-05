"""Check the chapter files against the statement format in conventions.md.

Usage: python3 check-statements.py
Exits with status 1 and lists every problem found.
"""

import re
import sys

from statements import LABELS, LINK_USE, QUESTION, ROOT, STATEMENT, STATEMENT_ID, chapter_files, parse

problems = []
known_ids = set()
files = chapter_files()
files_with_questions = dict(files, **{"open-questions.md": (ROOT / "open-questions.md").read_text()})

for name, text in files_with_questions.items():
    for line in text.splitlines():
        m = STATEMENT.match(line) or QUESTION.match(line)
        if m:
            if m["id"] in known_ids:
                problems.append(f"{name}: duplicate ID {m['id']}")
            known_ids.add(m["id"])

for name, text in files.items():
    statements, links = parse(text)
    if not re.search(r"^Prefix: [A-Z]+ · Scope: .+ · Last checked: \d{4}-\d{2}-\d{2}$", text, re.M):
        problems.append(f"{name}: missing or malformed chapter header")
    for line in text.splitlines():
        if line.startswith("- **") and not STATEMENT.match(line):
            problems.append(f"{name}: malformed statement line: {line[:60]}")
    used = set()
    for sid, s in statements.items():
        label, body = s["label"], s["text"]
        keys = set(LINK_USE.findall(body))
        used |= keys
        if label not in LABELS:
            problems.append(f"{name}: {sid} has unknown label {label}")
        if label in ("documented", "conflicting") and not keys:
            problems.append(f"{name}: {sid} is {label} but cites no source")
        if label == "conflicting" and len(keys) < 2:
            problems.append(f"{name}: {sid} is conflicting but cites fewer than two sources")
        if label == "observed" and not re.search(r"\(session \d{4}-\d{2}-\d{2}, .+\)$", body):
            problems.append(f"{name}: {sid} is observed but has no session note")
        if label == "inferred":
            basis = re.search(r"Basis: (.+)$", body)
            if not basis:
                problems.append(f"{name}: {sid} is inferred but has no Basis")
            else:
                for ref in STATEMENT_ID.findall(basis[1]):
                    if ref not in known_ids:
                        problems.append(f"{name}: {sid} rests on unknown ID {ref}")
        for key in keys - links.keys():
            problems.append(f"{name}: {sid} cites undefined source [{key}]")
    for key in links.keys() - used:
        problems.append(f"{name}: source [{key}] is defined but not cited")

for p in problems:
    print(p)
print(f"{len(known_ids)} IDs checked, {len(problems)} problems")
sys.exit(1 if problems else 0)

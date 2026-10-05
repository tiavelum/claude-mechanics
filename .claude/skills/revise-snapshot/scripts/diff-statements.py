"""Compare statements between two states of the repository, by statement ID.

Usage: python3 diff-statements.py OLD_REF [NEW_REF]
OLD_REF is usually the previous snapshot tag, for example v2026.10.05.
NEW_REF defaults to the work tree.
Prints added, deleted, relabelled and reworded statements as Markdown.
"""

import sys

from statements import all_statements

if len(sys.argv) not in (2, 3):
    sys.exit(__doc__)
old = all_statements(sys.argv[1])
new = all_statements(sys.argv[2] if len(sys.argv) == 3 else None)

added = sorted(new.keys() - old.keys())
deleted = sorted(old.keys() - new.keys())
relabelled = sorted(i for i in old.keys() & new.keys() if old[i]["label"] != new[i]["label"])
reworded = sorted(
    i
    for i in old.keys() & new.keys()
    if old[i]["label"] == new[i]["label"] and old[i]["text"] != new[i]["text"]
)


def section(title, ids, render):
    print(f"### {title} ({len(ids)})\n")
    for i in ids:
        print(render(i))
    print()


section("Added", added, lambda i: f"- {i} `{new[i]['label']}` {new[i]['text']}")
section("Deleted", deleted, lambda i: f"- {i} `{old[i]['label']}` {old[i]['text']}")
section(
    "Relabelled",
    relabelled,
    lambda i: f"- {i} `{old[i]['label']}` to `{new[i]['label']}`: {new[i]['text']}",
)
section(
    "Reworded",
    reworded,
    lambda i: f"- {i}\n  - before: {old[i]['text']}\n  - after: {new[i]['text']}",
)

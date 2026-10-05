"""Shared parsing of statement lines in the chapter files of this repository."""

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CHAPTER_GLOB = "[0-9][0-9]-*.md"
LABELS = ("documented", "observed", "inferred", "conflicting")

STATEMENT = re.compile(r"^- \*\*(?P<id>[A-Z]+-\d{3})\*\* `(?P<label>[a-z]+)` (?P<text>.+)$")
LINK_DEF = re.compile(r"^\[(?P<key>[a-z0-9-]+)\]: (?P<url>\S+)\s*$")
LINK_USE = re.compile(r"(?<!\])\[([a-z0-9-]+)\](?![(:\[])")
STATEMENT_ID = re.compile(r"\b[A-Z]+-\d{3}\b")


def chapter_files(ref=None):
    """Return {file name: text} for all chapter files, from the work tree or a git ref."""
    if ref is None:
        return {p.name: p.read_text() for p in sorted(ROOT.glob(CHAPTER_GLOB))}
    names = subprocess.run(
        ["git", "-C", str(ROOT), "ls-tree", "--name-only", ref],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.split()
    files = {}
    for name in sorted(names):
        if re.fullmatch(r"\d\d-.*\.md", name):
            files[name] = subprocess.run(
                ["git", "-C", str(ROOT), "show", f"{ref}:{name}"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout
    return files


def parse(text):
    """Return (statements, link definitions) of one chapter file."""
    statements, links = {}, {}
    for line in text.splitlines():
        if m := STATEMENT.match(line):
            statements[m["id"]] = {"label": m["label"], "text": m["text"], "line": line}
        elif m := LINK_DEF.match(line):
            links[m["key"]] = m["url"]
    return statements, links


def all_statements(ref=None):
    """Return {ID: statement with its file name and resolved source URLs}."""
    result = {}
    for name, text in chapter_files(ref).items():
        statements, links = parse(text)
        for sid, s in statements.items():
            s["file"] = name
            s["urls"] = [links[k] for k in LINK_USE.findall(s["text"]) if k in links]
            result[sid] = s
    return result

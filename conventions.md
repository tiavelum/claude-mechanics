# Conventions

How statements in this knowledge base are written, labelled, sourced and revised.

## Statement format

Each statement is one list item on one line, so a `git diff` between two snapshots shows exactly which facts changed.

```
- **MEM-012** `documented` Reset permanently deletes all memory, including project memory. [mem]
```

Parts, in order:

1. **ID**: chapter prefix plus three digits. IDs are never reused or renumbered. A retired statement is deleted; its ID stays unused.
2. **Label**: one of the provenance labels below, in backticks.
3. **Statement**: one fact, plain English, short enough to check against its source in under a minute.
4. **Source**: a reference-style link key for `documented` and `conflicting`, defined in the chapter's *Sources* section; a session note for `observed`; a `Basis:` list of statement IDs for `inferred`.

## Provenance labels

| Label | Meaning | Source required |
| :- | :- | :- |
| `documented` | Stated in official Anthropic documentation (support.claude.com, privacy.claude.com, claude.com, code.claude.com, docs.claude.com, anthropic.com). | Link to the page. |
| `observed` | Seen in a live session: context injected into the conversation, tool behaviour, or Claude's own runtime instructions. Not found in public documentation. | Session note: date, surface, project or not. |
| `inferred` | A conclusion drawn from other statements; stated nowhere. | `Basis:` the statement IDs it rests on. |
| `conflicting` | Official sources contradict each other. | Links to all conflicting pages. |

An `observed` statement describes one session at one point in time. It is weaker evidence than `documented` because runtime instructions are not public and may differ between accounts, plans and surfaces.

## Sources

- Documented statements in the 2026-10-05 snapshot were read with a web-fetch tool that returns a model-made extraction of the page, not the raw HTML. Wording that matters should be re-checked on the live page.
- A page's "Updated" marker on the help center is relative ("Updated this week"), so the snapshot date of the chapter is the only reliable date.
- Third-party blogs are never a source. They may be used to discover official pages.

## Chapter header

Every chapter starts with its prefix, scope and the date its statements were last checked:

```
Prefix: MEM · Scope: ... · Last checked: 2026-10-05
```

## Revising a snapshot

1. Re-read each source page and re-test each `observed` statement in a fresh session.
2. Edit statements in place. Change the label when the evidence changes (for example `observed` to `documented` once a page describes it).
3. Delete statements that are no longer true; never reuse their IDs. Add new facts with the next free ID.
4. Update *Last checked* in each chapter header.
5. Add an entry to [revisions.md](revisions.md) with the few bullet points that changed.
6. Tag the commit with the snapshot date.

# Conventions

How statements in this knowledge base are written, labelled, sourced and revised.

This file is the only place where this repository's conventions are defined; the README and project-instructions.md refer to it instead of restating it. General rules on language, punctuation, file names, commits and tags come from tiavelum's own instructions and are not repeated here. This file adds only what is specific to this repository, such as the tag format. These conventions apply to this repository alone and are not a standard for any other repository or project.

## Content

- The repository records research findings only: statements that describe how Claude behaves.
- It contains no recommendations, best practices or rules of its own for how anything else is to be set up, used, managed or designed.
- Advice that Anthropic gives in its documentation may be recorded as a `documented` statement, phrased as Anthropic's advice ("the documentation advises ...").

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

A session note has the form `(session YYYY-MM-DD, surface, outside projects | in a project)`, for example `(session 2026-10-05, claude.ai, outside projects)`. Add the plan when it matters.

## Where a statement goes

- Put a statement in the chapter whose *Scope* line covers it. A statement about how several mechanisms combine goes into [10-scenarios.md](10-scenarios.md); a dated change goes into [11-timeline.md](11-timeline.md) in addition to the chapter it changes.
- Create a new chapter only when no scope fits: give it the next number and a new prefix, and add it to the README's contents table.
- When a statement changes or is deleted, re-check every `inferred` statement and scenario whose `Basis:` lists it.

## Provenance labels

| Label | Meaning | Source required |
| :- | :- | :- |
| `documented` | Stated in official Anthropic documentation (support.claude.com, support.anthropic.com, privacy.claude.com, claude.com, code.claude.com, docs.claude.com, anthropic.com). | Link to the page. |
| `observed` | Seen in a live session: context injected into the conversation, tool behaviour, or Claude's own runtime instructions. Not found in public documentation. | Session note: date, surface, project or not. |
| `inferred` | A conclusion drawn from other statements; stated nowhere. | `Basis:` the statement IDs it rests on. |
| `conflicting` | Official sources contradict each other. | Links to all conflicting pages. |

An `observed` statement describes one session at one point in time. It is weaker evidence than `documented` because runtime instructions are not public and may differ between accounts, plans and surfaces.

## Sources

- Documented statements in the 2026-10-05 snapshot were read with a web-fetch tool that returns a model-made extraction of the page, not the raw HTML. Wording that matters should be re-checked on the live page.
- A page's "Updated" marker on the help center is relative ("Updated this week"), so the snapshot date of the chapter is the only reliable date.
- Third-party blogs and forums are never a source. They may be used to discover official pages.
- A statement is labelled `documented` only by a session that read the cited page itself.
- Sources are paraphrased; a quote is at most a few words, used only where exact wording matters.

## Open questions

- A point that neither documentation nor observation settles is a GitHub issue labelled `open-question`, stating the question, a test that would settle it, and the IDs of related statements.
- When a question is settled, its answer becomes a statement in the right chapter, and the issue is closed with a reference to that commit.

## Chapter header

Every chapter starts with its prefix, scope and the date its statements were last checked:

```
Prefix: MEM · Scope: ... · Last checked: 2026-10-05
```

## Changing statements

- Statements are edited in place; the label changes when the evidence changes, for example from `observed` to `documented` once a page describes it.
- A statement that is no longer true is deleted; its ID stays unused.
- Changes between snapshots are committed normally and update *Last checked* only for the chapters actually re-checked.

## Snapshots and releases

- A snapshot is a state of `main` in which every chapter was re-checked. It is prepared on a branch `revision/vYYYY.MM.DD` and reviewed as a pull request before it is merged.
- A snapshot is tagged `vYYYY.MM.DD` and published as a GitHub release of the same name. The release notes are the record of what changed; there is no change log file in the repository.
- Release notes separate changes in Claude from corrections of earlier mistakes in this repository, and list what could not be re-checked.
- Two snapshots are compared with `git diff v2026.10.05 v2027.01.15`, for example, or with GitHub's compare view.
- The procedure, with its scripts, is [.claude/skills/revise-snapshot/SKILL.md](.claude/skills/revise-snapshot/SKILL.md).

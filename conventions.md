# Conventions

How statements in this knowledge base are written, labelled, sourced and revised. These conventions apply to this repository alone. General rules for any repository come from [tiavelum/engineering-standards](https://github.com/tiavelum/engineering-standards), and rules on writing from tiavelum's own instructions; neither is repeated here.

## Content

- The repository records research findings only: statements that describe how Claude behaves.
- It contains no recommendations, best practices or rules of its own for how anything else is set up, used, managed or designed.
- Advice that Anthropic gives in its documentation may be recorded as a `documented` statement, phrased as Anthropic's advice ("the documentation advises ...").

## Statement format

Each statement is one list item on one line, so a `git diff` between two snapshots shows exactly which facts changed.

```
- **MEM-012** `documented` Reset permanently deletes all memory, including project memory. [mem]
```

Parts, in order:

1. **ID**: chapter prefix plus three digits. IDs are never reused or renumbered.
2. **Label**: one of the provenance labels below, in backticks.
3. **Statement**: one fact, in plain English.
4. **Source**: as the label requires (see below). Link keys are reference-style and defined in the chapter's *Sources* section.

A session note has the form `(session YYYY-MM-DD, surface, outside projects | in a project)`, for example `(session 2026-10-05, claude.ai, outside projects)`. Add the plan when it matters.

Statements are edited in place. A statement that is no longer true is deleted, and its ID stays unused.

## Provenance labels

| Label | Meaning | Source required |
| :- | :- | :- |
| `documented` | Stated in official Anthropic documentation (support.claude.com, support.anthropic.com, privacy.claude.com, claude.com, code.claude.com, docs.claude.com, anthropic.com). | Link to the page. |
| `observed` | Seen in a live session: context injected into the conversation, tool behaviour, or Claude's own runtime instructions. Not found in public documentation. | Session note. |
| `inferred` | A conclusion drawn from other statements; stated nowhere. | `Basis:` the statement IDs it rests on. |
| `conflicting` | Official sources contradict each other. | Links to all conflicting pages. |

- A statement is labelled `documented` only by a session that read the cited page itself.
- The label changes when the evidence changes, for example from `observed` to `documented` once a page describes it.
- An `observed` statement describes one session at one point in time; it may not hold for other accounts, plans or surfaces.
- Third-party blogs and forums are never a source; they may be used to find official pages.
- Sources are paraphrased; a quote is at most a few words, used only where exact wording matters.

## Where a statement goes

- Put a statement in the chapter whose *Scope* line covers it. A statement about how several mechanisms combine goes into [10-scenarios.md](10-scenarios.md); a dated change goes into [11-timeline.md](11-timeline.md) in addition to the chapter it changes.
- Create a new chapter only when no scope fits: give it the next number and a new prefix, and add it to the README's contents table.
- When a statement changes or is deleted, re-check every `inferred` statement and scenario whose `Basis:` lists it.

## Chapter header

Every chapter starts with its prefix, scope and the date its statements were last checked:

```
Prefix: MEM · Scope: ... · Last checked: 2026-10-05
```

## Open questions

- A point that neither documentation nor observation settles is a GitHub issue labelled `open-question`, stating the question, a test that would settle it, and the IDs of related statements.
- When a question is settled, its answer becomes a statement, and the issue is closed with a reference to that commit.

## Snapshots and releases

- Changes between snapshots are committed normally and update *Last checked* only for the chapters actually re-checked.
- A snapshot is a state of `main` in which every chapter was re-checked. It is prepared on a branch `docs/snapshot-YYYY-MM-DD`, reviewed as a pull request, tagged `vYYYY.MM.DD` and published as a GitHub release of the same name.
- The release notes are the record of what changed; there is no change log file in the repository.
- The procedure and the format of the release notes are in [.claude/skills/revise-snapshot/SKILL.md](.claude/skills/revise-snapshot/SKILL.md).

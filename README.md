# Claude mechanics

A dated, sourced snapshot of how Claude works behind the scenes: sessions, memory, chat search, projects, instructions, context and settings, in the Claude app and in Claude Code. Each fact is one short statement labelled as documented, observed, inferred or conflicting, so a later snapshot can be compared line by line to see how Claude has changed.

## How to start

- Read [10-scenarios.md](10-scenarios.md) for the practical picture of what sessions share, then the chapter you need.
- To see how trustworthy a statement is, look at its label and source; [conventions.md](conventions.md) defines both.
- To revise the snapshot later, follow *Revising a snapshot* in [conventions.md](conventions.md), then compare with the previous snapshot tag and summarize the differences in [revisions.md](revisions.md).
- To add findings from another session, add statements to the matching chapter with the next free ID.

## Contents

| File | Prefix | Covers |
| :- | :- | :- |
| [01-surfaces-and-sessions.md](01-surfaces-and-sessions.md) | SES | Chat and Cowork, where sessions run, session state |
| [02-memory.md](02-memory.md) | MEM | Account and project memory, controls, incognito, retention |
| [03-chat-search.md](03-chat-search.md) | SRC | Searching past conversations |
| [04-projects.md](04-projects.md) | PRJ | Project structure, knowledge and RAG, moving chats, sharing |
| [05-instructions-and-personalization.md](05-instructions-and-personalization.md) | INS | Account and project instructions, styles, precedence |
| [06-context-management.md](06-context-management.md) | CTX | Context windows, long chats, usage, uploads |
| [07-skills-connectors-artifacts.md](07-skills-connectors-artifacts.md) | EXT | Extensions that outlive a session |
| [08-settings.md](08-settings.md) | SET | Settings that change memory, search or context |
| [09-claude-code.md](09-claude-code.md) | CC | CLAUDE.md, auto memory, settings, sessions, compaction |
| [10-scenarios.md](10-scenarios.md) | SCN | What sessions share in common setups |
| [11-timeline.md](11-timeline.md) | CHG | Dated changes |
| [open-questions.md](open-questions.md) | OQ | Unsettled points and how to test them |
| [revisions.md](revisions.md) | | What changed between snapshots |
| [conventions.md](conventions.md) | | Statement format, labels, revision procedure |

## Mental model

Knowledge reaches a Claude session through a few separate channels, each with its own scope:

- **The session itself**: transcript and workspace files. Private to one session.
- **Instructions**: account instructions (all chats), project instructions (one project), CLAUDE.md files (Claude Code). Written by the user, loaded every time.
- **Knowledge**: project knowledge in the Claude app, repository files in Claude Code. Loaded or retrieved on demand.
- **Memory**: short facts Claude saves itself. In the Claude app, one account memory for chats outside projects plus one memory per project; in Claude Code, auto memory per repository on each machine.
- **Chat search**: on-demand retrieval of past transcripts, bounded by the same project walls as memory.

Projects in the Claude app are the main boundary: they decide which memory a chat writes to and which chats search can reach. Claude Code keeps its own, file-based mechanisms and does not share memory with the Claude app.

The labels matter as much as the statements. `documented` comes from Anthropic's pages, `observed` from what one live session showed, and `inferred` is reasoning that still needs a test; [open-questions.md](open-questions.md) lists those tests.

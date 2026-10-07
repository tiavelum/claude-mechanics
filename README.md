# Claude mechanics

A dated, sourced snapshot of how Claude works behind the scenes, for people and Claude sessions that need to look it up: sessions, memory, chat search, projects, instructions, context, settings, extensions, models, built-in tools, data handling and retention, in the Claude app, in Claude Code and in the API and Agent SDK. Each fact is one short statement labelled as documented, observed, inferred or conflicting.

## What it is for

- Looking up how a mechanism works, with the link to Anthropic's page for each documented fact.
- Pointing a Claude session at a chapter, so that it answers from a checked record, not from a web search.
- Seeing how Claude has changed: two snapshots differ line by line.

It records Claude's behaviour as documented by Anthropic and as visible in sessions, not the model's internals and not anyone's own content or projects. It describes, and recommends nothing.

## How to start

Reading:

- Read [10-scenarios.md](10-scenarios.md) for the practical picture of what sessions share, then the chapter you need.
- Read [conventions.md](conventions.md) before relying on a statement: its label says how it is known, and the chapter's *Last checked* date says when.
- A statement is true as of its chapter's *Last checked* date only; Claude changes often, so re-check the source before treating it as current.

Contributing:

- Research happens in sessions of a dedicated Claude project whose instructions are [project-instructions.md](project-instructions.md); Claude Code reads the same file through [CLAUDE.md](CLAUDE.md).
- A session proposes new or changed statement lines; once reviewed, they are committed to `main`.
- A full re-check of all chapters is a snapshot, prepared with the [revise-snapshot](.claude/skills/revise-snapshot/SKILL.md) skill as a pull request. Each snapshot is a [GitHub release](https://github.com/tiavelum/claude-mechanics/releases) whose notes say what changed in Claude.

## Contents

| File | Prefix | Covers |
| :- | :- | :- |
| [01-surfaces-and-sessions.md](01-surfaces-and-sessions.md) | SES | Chat and Cowork, where sessions run, session state, products and where they are available |
| [02-memory.md](02-memory.md) | MEM | Account and project memory, controls, incognito, retention |
| [03-chat-search.md](03-chat-search.md) | SRC | Searching past conversations |
| [04-projects.md](04-projects.md) | PRJ | Project structure, knowledge and RAG, moving chats, sharing |
| [05-instructions-and-personalization.md](05-instructions-and-personalization.md) | INS | Account, organization, project and folder instructions, styles, published system prompts, precedence |
| [06-context-management.md](06-context-management.md) | CTX | Context windows, long chats, usage, uploads, what each plan includes |
| [07-skills-connectors-artifacts.md](07-skills-connectors-artifacts.md) | EXT | Extensions that outlive a session, and how an organization controls them |
| [08-settings.md](08-settings.md) | SET | Account, project, per-chat and organization settings |
| [09-claude-code.md](09-claude-code.md) | CC | CLAUDE.md, auto memory, settings, sessions and their environments, compaction |
| [10-scenarios.md](10-scenarios.md) | SCN | What sessions share in common setups |
| [11-timeline.md](11-timeline.md) | CHG | Dated changes |
| [12-models-effort-thinking.md](12-models-effort-thinking.md) | MOD | Model lineup, identifiers, specifications, thinking, effort, choosing a model, safeguards, pricing |
| [13-steering-scheduling-sharing.md](13-steering-scheduling-sharing.md) | WRK | Steering a running session, approvals, notifications, scheduled tasks, managing and sharing chats |
| [14-built-in-tools.md](14-built-in-tools.md) | TOOL | Web search, Research, code execution and file creation, browsers, computer use |
| [15-data-and-retention.md](15-data-and-retention.md) | DAT | Model training, retention and deletion, location data, feedback |
| [16-claude-code-permissions-and-automation.md](16-claude-code-permissions-and-automation.md) | CCA | Agentic loop, permissions and hooks, checkpoints, subagents, skills, scheduled work, prompt caching, costs |
| [17-api-and-agent-sdk.md](17-api-and-agent-sdk.md) | API | Requests, context management, prompt caching, tools, the memory tool, Agent SDK |
| [conventions.md](conventions.md) | | Statement format, labels, snapshots and releases |
| [.claude/skills/revise-snapshot/](.claude/skills/revise-snapshot/SKILL.md) | | Skill and scripts for re-checking and publishing a snapshot |
| [.github/workflows/check-statements.yml](.github/workflows/check-statements.yml) | | Runs the statement check and the linter on every pull request |

## Mental model

"The Claude app" means Claude on the web (claude.ai), desktop and mobile, including Cowork, which is merging into it. "Claude Code" means the terminal, IDE, desktop Code tab and cloud sessions of Claude Code.

Knowledge reaches a Claude session through a few separate channels, each with its own scope:

- **The session itself**: transcript and workspace files. Private to one session.
- **Instructions**: account instructions (all chats), project instructions (one project), CLAUDE.md files (Claude Code). Written by the user, loaded every time.
- **Knowledge**: project knowledge in the Claude app, repository files in Claude Code. Loaded or retrieved on demand.
- **Memory**: short facts Claude saves itself. In the Claude app, one account memory for chats outside projects plus one memory per project; in Claude Code, auto memory per repository on each machine.
- **Chat search**: on-demand retrieval of past transcripts, bounded by the same project walls as memory.

Projects in the Claude app are the main boundary: they decide which memory a chat writes to and which chats search can reach. Claude Code keeps its own, file-based mechanisms and does not share memory with the Claude app.

The labels matter as much as the statements. `documented` comes from Anthropic's pages, `observed` from what one live session showed, and `inferred` is reasoning that still needs a test; the [open questions](https://github.com/tiavelum/claude-mechanics/issues?q=label%3Aopen-question) are GitHub issues that list those tests.

## License

MIT. See [LICENSE](LICENSE).

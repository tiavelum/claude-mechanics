# 10 Scenarios

Prefix: SCN · Scope: what two or more sessions share in common setups; each scenario combines statements from other chapters · Last checked: 2026-10-07

## Claude app

- **SCN-001** `documented` Two chats outside any project, memory on: both read and write the same account memory, and on Pro, Max, Team and Enterprise, with "Search and reference chats" on and outside Enterprise organizations that use customer-managed encryption keys, either can find the other through chat search. [mem]
- **SCN-002** `conflicting` Two chats in the same project both use the project's instructions and knowledge; whether they share anything else conflicts: the projects article says context is not shared across a project's chats unless it is added to project knowledge, while the memory article gives the project a memory of its own and a chat search limited to the project's chats. [proj] [mem]
- **SCN-003** `documented` Two chats in different projects: no shared instructions, knowledge or memory, and neither can find the other through chat search. [mem] [proj]
- **SCN-004** `documented` A chat outside projects and a chat in a project: separate memory spaces; chat search from outside projects reaches the chats outside projects, and from within a project it stays limited to that project's chats. [mem]
- **SCN-005** `observed` A chat outside projects and a project whose memory is set to connected: Claude's runtime instructions say the project's chats can draw on account memory and chats outside projects can see the project's memory, and in a chat outside projects the memory of several projects appeared as collapsed folders whose files Claude listed on demand. (session 2026-10-06, claude.ai, outside projects)
- **SCN-006** `inferred` A chat moved from outside into a project: from then on it searches only within the project and counts toward the project's memory. Basis: MEM-051, PRJ-040, PRJ-042, SRC-003.
- **SCN-007** `documented` A chat started with memory off, inside or outside a project: it reads no memory, searches no past chats and saves nothing, but stays in history and can be found by other chats. [mem]
- **SCN-008** `documented` An incognito chat, which can be started only outside projects: no memory read or written, not saved to history, never found by chat search; Claude can still access profile information such as custom styles and personal preferences. [inc] [mem]
- **SCN-009** `documented` Memory paused: existing memory is kept but unused, and conversations held while paused are never added. [mem]
- **SCN-010** `documented` Memory reset: all account and project memories are deleted permanently. [mem]
- **SCN-011** `documented` A chat and a cloud Cowork task share account memory, in both directions; a Cowork task that runs only on the user's computer is left out of it: the memory article says local Cowork sessions use no memory, and the merger article says memory from tasks that ran only on the computer stays with those tasks. [mem] [one]
- **SCN-012** `documented` On Team and Enterprise, two members chatting in a project shared between them: both chats use the project's instructions and knowledge, and each member's chats stay private to that member unless shared. [proj] [vis]
- **SCN-013** `inferred` Two conversations linked to the same computer: a folder the user connects in one is not reachable from the other until it is connected there too; once it is connected in both, both read and write the same files. Basis: SES-023, SES-055.
- **SCN-014** `documented` In Claude Desktop on 3P, Cowork sessions and Chat conversations in the same project share the project's memory files: Cowork sessions read and update them, while a Chat conversation reads them, unless memory was paused when it started, but cannot change them; Chat conversations outside projects use no memory, and no Chat conversation can search the others. [3p-data]
- **SCN-015** `inferred` On Pro and Max since 2026-10-06, new Cowork tasks and new scheduled tasks run in the cloud and so share account memory with chats; Cowork sessions without account memory remain only for tasks started on the computer before that date, until they finish, and for scheduled tasks that already ran there. Basis: SES-011, SES-012, SES-014, SES-060.
- **SCN-016** `inferred` On Team and Enterprise, where chat and Cowork are still separate, a member's chats share account memory with that member's Cowork sessions only where the organization lets Cowork run in the cloud, which is on by default on Team and off by default on Enterprise. Basis: SES-008, SES-014, SES-018.
- **SCN-017** `inferred` Two cloud Cowork sessions of one account: each runs in a sandbox of its own and sees none of the other's files or state, while both load the account's instructions, the skills enabled for the account and its connected connectors, and share account memory. Basis: SES-035, INS-001, EXT-039, EXT-010, MEM-009.
- **SCN-018** `inferred` Two Cowork tasks in the same Cowork project share that project's instructions, context and memory, and what the project's memory holds does not reach tasks in other Cowork projects. Basis: PRJ-005, MEM-052.
- **SCN-019** `inferred` A scheduled task and the conversation that created it: every run is a Cowork session of its own that starts from the instructions stored with the task, not from the transcript of the conversation that set it up. Basis: WRK-060, WRK-064, SES-048, SES-025.

## Claude Code

- **SCN-020** `documented` Two local Claude Code sessions on the same machine in the same repository, including in different worktrees, share one auto memory directory and the committed CLAUDE.md files; a gitignored CLAUDE.local.md exists only in the worktree where it was created. [cc-mem]
- **SCN-021** `documented` Two local Claude Code sessions on the same machine in different repositories share the user-level and machine-wide configuration: `~/.claude/CLAUDE.md`, `~/.claude/rules/`, `~/.claude/settings.json`, personal skills in `~/.claude/skills/` and the managed policy CLAUDE.md. [cc-mem] [cc-set] [cc-skills]
- **SCN-022** `documented` A local Claude Code session and a cloud session on the same repository share what is committed, such as CLAUDE.md, `.claude/rules/` and the skills under `.claude/`, but not auto memory or the user's own files under `~/.claude/`. [cc-mem] [cc-cloud-env]
- **SCN-023** `inferred` A Claude Code session and a Claude app chat share no memory; the documented bridges are skills, plugins and connectors enabled on the claude.ai account, artifacts on the claude.ai account, and files of a GitHub repository that a project's knowledge syncs. Basis: CC-102, CC-107, CC-114, CC-126, CC-223, EXT-020, PRJ-039.
- **SCN-024** `documented` A terminal session and a local session in the desktop app's Code tab on the same computer read the same settings, the same CLAUDE.md and CLAUDE.local.md and the same MCP servers in `~/.claude.json` or `.mcp.json`; each keeps its own session list, and a CLI session continued in the desktop app stays the same session, which `claude --resume` still finds. [cc-desk] [cc-set]
- **SCN-025** `documented` In a redesigned project (beta), the project conversation and its threads are separate sessions: each cloud thread begins with the project's repositories and files, its instructions and memory, the CLAUDE.md and skills of each project repository and the account's connectors, and reports back to the project conversation, which sees the reports but not each step; a thread on the user's own computer starts with the instructions but not the memory files. [cc-proj]
- **SCN-026** `documented` A conversation in the Claude Desktop chat surface and a local session in the desktop app's Code tab both get the MCP servers defined in `claude_desktop_config.json`, while the standalone terminal CLI does not read that file. [cc-desk]
- **SCN-027** `documented` Cowork sessions, cloud sessions and terminal sessions signed in with the same claude.ai account load the skills enabled for that account, while personal skills in `~/.claude/skills/` load only in local sessions on that machine, desktop scheduled tasks included, and not in Cowork, cloud sessions or routines. [cc-skills]
- **SCN-028** `inferred` A subagent other than a fork and the session that started it: the subagent gets the working directory and, apart from Explore, Plan and definitions that omit it, the CLAUDE.md hierarchy, but neither the conversation history nor the main conversation's auto memory, builds a prompt cache of its own and draws on the same usage limits. Basis: CC-094, CC-095, CC-096, CC-049, CCA-202, CCA-226.
- **SCN-029** `inferred` Two Claude Code sessions running in parallel in the same directory of one machine share the repository's auto memory directory and, while they use the same model, can read each other's prompt cache. Basis: CC-043, CCA-203, CCA-191.

## Across surfaces

- **SCN-030** `documented` Sessions of one account in claude.ai, Claude Code and Claude Desktop count toward the same usage limit, and a limit reset, which refills either the five-hour session limit or the weekly limit, applies on every surface, Claude Mobile and Claude Code included. [lim] [reset]
- **SCN-031** `inferred` Two members of one Team or Enterprise organization: every conversation of both follows the organization instructions, both find the skills an owner provisioned in their skills list, and both can use a connector the owner added, each signing in with their own account unless it relies on a shared credential. Basis: INS-040, EXT-006, EXT-013.
- **SCN-032** `inferred` On Team, each member's sessions on every surface draw on that member's own usage limits, separate from those of other members. Basis: CTX-021, CTX-026.
- **SCN-033** `inferred` In an Enterprise organization with a default model, a member's new chat, new Cowork task and new Claude Code session all begin on that model, except that in Claude Code a model from a flag, an environment variable or a settings file outranks it. Basis: MOD-224, MOD-230.
- **SCN-034** `documented` Turning a connector off in a cloud thread of a redesigned project at claude.ai/code also makes that the account default, so new threads and new claude.ai chats start without the connector until it is turned on again. [cc-proj]
- **SCN-035** `inferred` Parallel work of one account, such as a Claude Code session's subagents, its cloud sessions and the threads of a redesigned project, draws down the same usage limits as the account's chats. Basis: CTX-021, CCA-226, CCA-227, PRJ-089.
- **SCN-036** `inferred` A project chat with a GitHub repository in its knowledge and a Claude Code cloud session on that repository do not see the same state: the project holds the files of one branch as of the last sync, without commit history, while the cloud session starts from a fresh clone; the merged experience does not support "Add from GitHub". Basis: PRJ-039, PRJ-025, CC-193, SES-033.
- **SCN-037** `documented` On Team and Enterprise, cloud sessions of different members that use an organization-shared environment start with the same network access, environment variables and setup script, and every member using it can read those variables. [cc-cloud-env]

## API and Agent SDK

- **SCN-040** `inferred` An Agent SDK session and a Claude Code session in the same repository on one machine share the auto memory directory, which the SDK session loads whatever its `settingSources` contain. Basis: API-191, API-196, CC-042, CC-043.
- **SCN-041** `inferred` Two Managed Agents sessions on the same agent and environment share the agent's definition and the environment's configuration but no sandbox files or context; information passes between them only through a memory store attached to both. Basis: API-164, API-165, API-166, API-171, API-173.
- **SCN-042** `inferred` Two API requests reuse one cache entry only if they belong to the same organization and, on the Claude API, Microsoft Foundry and Claude Platform on AWS, to the same workspace, and only for a prefix that is identical up to the cached block. Basis: API-092, API-085.

## Sources

[3p-data]: https://claude.com/docs/third-party/claude-desktop/data-storage
[cc-cloud-env]: https://code.claude.com/docs/en/cloud-environments
[cc-desk]: https://code.claude.com/docs/en/desktop
[cc-mem]: https://code.claude.com/docs/en/memory
[cc-proj]: https://code.claude.com/docs/en/claude-projects
[cc-set]: https://code.claude.com/docs/en/settings
[cc-skills]: https://code.claude.com/docs/en/skills
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[lim]: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[reset]: https://support.claude.com/en/articles/17007452-what-is-a-limit-reset
[vis]: https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing

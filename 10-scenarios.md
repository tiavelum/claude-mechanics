# 10 Scenarios

Prefix: SCN · Scope: what two or more sessions share in common setups; each scenario combines statements from chapters 01 to 09 · Last checked: 2026-10-06

## Claude app

- **SCN-001** `documented` Two chats outside any project, memory on: both read and write the same account memory, and on Pro, Max, Team and Enterprise, with "Search and reference chats" on and outside Enterprise organizations that use customer-managed encryption keys, either can find the other through chat search. [mem]
- **SCN-002** `conflicting` Two chats in the same project both use the project's instructions and knowledge; whether they share anything else conflicts: the projects article says context is not shared across a project's chats unless it is added to project knowledge, while the memory article gives the project a memory of its own and a chat search limited to the project's chats. [proj] [mem]
- **SCN-003** `documented` Two chats in different projects: no shared instructions, knowledge or memory, and neither can find the other through chat search. [mem] [proj]
- **SCN-004** `documented` A chat outside projects and a chat in a project: separate memory spaces, and chat search does not cross the project boundary in either direction. [mem]
- **SCN-005** `observed` A chat outside projects and a project whose memory is set to connected: Claude's runtime instructions say the project's chats can draw on account memory and chats outside projects can see the project's memory, and in a chat outside projects the memory of several projects appeared as collapsed folders whose files Claude listed on demand. (session 2026-10-06, claude.ai, outside projects)
- **SCN-006** `inferred` A chat moved from outside into a project: from then on it searches only within the project and counts toward the project's memory. Basis: MEM-051, PRJ-040, PRJ-042, SRC-003.
- **SCN-007** `documented` A chat started with memory off, inside or outside a project: it reads no memory, searches no past chats and saves nothing, but stays in history and can be found by other chats. [mem]
- **SCN-008** `documented` An incognito chat, which can be started only outside projects: no memory read or written, not saved to history, never found by chat search; Claude can still access profile information such as custom styles and personal preferences. [inc] [mem]
- **SCN-009** `documented` Memory paused: existing memory is kept but unused, and conversations held while paused are never added. [mem]
- **SCN-010** `documented` Memory reset: all account and project memories are deleted permanently. [mem]
- **SCN-011** `documented` A chat and a cloud Cowork task share account memory; a local Cowork session uses no memory. [mem]
- **SCN-012** `documented` On Team and Enterprise, two members chatting in a project shared between them: both chats use the project's instructions and knowledge, and each member's chats stay private to that member unless shared. [proj] [vis]
- **SCN-013** `inferred` Two conversations linked to the same computer: a folder the user connects in one is not reachable from the other until it is connected there too; once it is connected in both, both read and write the same files. Basis: SES-023, SES-055.
- **SCN-014** `documented` In Claude Desktop on 3P, Cowork sessions and Chat conversations in the same project share the project's memory files: Cowork sessions read and update them, while a Chat conversation reads them, unless memory was paused when it started, but cannot change them; Chat conversations outside projects use no memory, and no Chat conversation can search the others. [3p-data]

## Claude Code

- **SCN-020** `documented` Two local Claude Code sessions on the same machine in the same repository, including in different worktrees, share one auto memory directory and the committed CLAUDE.md files; a gitignored CLAUDE.local.md exists only in the worktree where it was created. [cc-mem]
- **SCN-021** `documented` Two local Claude Code sessions on the same machine in different repositories share the user-level and machine-wide configuration: `~/.claude/CLAUDE.md`, `~/.claude/rules/`, `~/.claude/settings.json`, personal skills in `~/.claude/skills/` and the managed policy CLAUDE.md. [cc-mem] [cc-set] [cc-skills]
- **SCN-022** `documented` A local Claude Code session and a cloud session on the same repository share what is committed, such as CLAUDE.md, `.claude/rules/` and the skills under `.claude/`, but not auto memory or the user's own files under `~/.claude/`. [cc-mem] [cc-cloud-env]
- **SCN-023** `inferred` A Claude Code session and a Claude app chat share no memory; the documented bridges are skills, plugins and connectors enabled on the claude.ai account, artifacts on the claude.ai account, and files of a GitHub repository that a project's knowledge syncs. Basis: CC-102, CC-107, CC-114, CC-126, CC-223, EXT-020, PRJ-039.
- **SCN-024** `documented` A terminal session and a local session in the desktop app's Code tab on the same computer read the same settings, CLAUDE.md and CLAUDE.local.md files and the MCP servers in `~/.claude.json` or `.mcp.json`; each keeps its own session list, and a CLI session continued in the desktop app stays the same session, which `claude --resume` still finds. [cc-desk] [cc-set]
- **SCN-025** `documented` In a redesigned project (beta), the project conversation and its threads are separate sessions: every cloud thread starts with the project's repositories and files, its instructions and memory, the CLAUDE.md and skills of each project repository and the account's connectors, and reports back to the project conversation, which sees the reports but not each step; a thread on the user's own computer starts with the instructions but not the memory files. [cc-proj]

## Across surfaces

- **SCN-030** `documented` Sessions of one account in claude.ai, Claude Code and Claude Desktop count toward the same usage limit, and a limit reset brings the limits back to full on every surface, Claude Mobile and Claude Code included. [lim] [reset]

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
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[reset]: https://support.claude.com/en/articles/17007452-what-is-a-limit-reset
[vis]: https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing

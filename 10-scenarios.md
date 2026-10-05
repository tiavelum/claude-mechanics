# 10 Scenarios

Prefix: SCN · Scope: what two or more sessions share in common setups; each scenario combines statements from chapters 01 to 09 · Last checked: 2026-10-05

## Claude app

- **SCN-001** `documented` Two chats outside any project, memory on: both read and write the same account memory, and either can find the other through chat search. [mem]
- **SCN-002** `documented` Two chats in the same project: both use the project's instructions, knowledge and memory, and can find each other through chat search; neither sees the other's transcript otherwise. [proj] [mem]
- **SCN-003** `documented` Two chats in different projects: no shared instructions, knowledge or memory, and neither can find the other through chat search. [mem] [proj]
- **SCN-004** `documented` A chat outside projects and a chat in a project: separate memory spaces, and chat search does not cross the project boundary in either direction. [mem]
- **SCN-005** `observed` A chat outside projects and a project whose memory is set to connected: the outside chat can open the project's memory on demand, and the project's chats can draw on account memory. (session 2026-10-05, claude.ai, outside projects)
- **SCN-006** `inferred` A chat moved from outside into a project: from then on it counts toward the project's memory and searches only within the project; what it had already saved to account memory stays there. Basis: MEM-051, MEM-101, SRC-003.
- **SCN-007** `documented` A chat started with memory off, inside or outside a project: it reads no memory, searches no past chats and saves nothing, but stays in history and can be found by other chats. [mem]
- **SCN-008** `documented` An incognito chat: no memory read or written, not saved to history, never searchable; account instructions and styles still apply. [inc]
- **SCN-009** `documented` Memory paused: existing memory is kept but unused, and conversations held while paused are never added. [mem]
- **SCN-010** `documented` Memory reset: all account and project memories are deleted permanently. [mem]
- **SCN-011** `documented` A chat and a cloud Cowork task share account memory; a local Cowork session uses no memory. [mem]

## Claude Code

- **SCN-020** `documented` Two local Claude Code sessions in the same repository, including different worktrees, share one auto memory directory and the repository's CLAUDE.md files. [cc-mem]
- **SCN-021** `documented` Two local Claude Code sessions in different repositories share only user-level and machine-wide configuration, such as `~/.claude/CLAUDE.md`, `~/.claude/rules/`, user settings, personal skills and the managed policy CLAUDE.md. [cc-mem] [cc-set]
- **SCN-022** `documented` A local Claude Code session and a cloud session on the same repository share committed files such as CLAUDE.md, but not auto memory. [cc-mem]
- **SCN-023** `inferred` A Claude Code session and a Claude app chat share no memory; the only documented bridges are skills and plugins enabled on the claude.ai account, artifacts, and files in a shared repository. Basis: CC-102, CC-114, EXT-021.

## Sources

[cc-mem]: https://code.claude.com/docs/en/memory
[cc-set]: https://code.claude.com/docs/en/settings
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects

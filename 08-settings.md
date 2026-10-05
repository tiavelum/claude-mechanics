# 08 Settings

Prefix: SET · Scope: account, project, per-chat and organization settings in the Claude app that affect memory, search, instructions or context · Last checked: 2026-10-05

## Account settings

- **SET-001** `documented` Settings > Memory > "Generate memory from chats" turns memory on or off for the account, with "Pause memory" and "Reset memory" as the ways to turn it off. [mem]
- **SET-002** `documented` Settings > Memory > "Search and reference chats" turns chat search on or off. [mem]
- **SET-003** `documented` Settings > Memory > "Include sensitive topics in memory" lets Claude store sensitive topics from then on. [mem]
- **SET-004** `documented` Settings > Memory lists everything remembered under Topics, editable one by one. [mem]
- **SET-005** `documented` Settings > Memory > "Start import" adds pasted memory from another assistant. [imp]
- **SET-006** `documented` Settings > General > "Instructions for Claude" holds the account-wide instructions. [one]
- **SET-007** `documented` Settings > General > "Only on your computer" for Cowork tasks is removed from 2026-10-06 for Pro and Max. [cw-web]
- **SET-008** `documented` Settings > Privacy holds the data export, on the web and in Claude Desktop. [exp]
- **SET-009** `documented` Settings > Usage shows the session and weekly usage limits. [usage]
- **SET-010** `documented` In the legacy memory experience, memory and chat search were in Settings > Capabilities instead of Settings > Memory. [mem]

## Per-project settings

- **SET-020** `documented` A project has its own instructions and knowledge, set on the project's page. [proj]
- **SET-021** `observed` Claude's runtime instructions describe a per-project memory setting, connected or separate, that is changed on the project's page on the web and that Claude itself cannot change. (session 2026-10-05, claude.ai, outside projects)

## Per-chat settings

- **SET-030** `documented` "+" > "Memory" turns memory off for one chat or task, before the first message only. [mem]
- **SET-031** `documented` The ghost icon in a new chat outside a project starts an incognito chat. [inc]
- **SET-032** `documented` The "+" menu has a per-conversation toggle for each connector. [conn]
- **SET-033** `documented` A style can be chosen and changed at any point in a conversation. [sty]

## Capabilities that change context behaviour

- **SET-040** `documented` Code execution must be enabled for automatic context management of long conversations. [ctx]
- **SET-041** `documented` Skills require "Code execution and file creation" to be enabled (on Team and Enterprise: "Cloud code execution and file creation"). [use-skills]

## Organization settings (Team and Enterprise)

- **SET-050** `documented` Owners enable memory for the organization in Organization settings > Capabilities; turning it off deletes all members' memory. [mem]
- **SET-051** `documented` Admins can turn off project sharing for the organization. [proj]

## Claude's own reach

- **SET-060** `observed` Claude could not change any of these settings itself; when asked to stop using memory or past chats, it was instructed to name the setting and stop using the tools for the rest of the conversation. (session 2026-10-05, claude.ai, outside projects)

## Sources

[conn]: https://claude.com/docs/connectors/getting-started
[ctx]: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
[cw-web]: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
[exp]: https://support.claude.com/en/articles/9450526-export-your-claude-data
[imp]: https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[sty]: https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles
[usage]: https://support.claude.com/en/articles/9797557-usage-limit-best-practices
[use-skills]: https://support.claude.com/en/articles/12512180-use-skills-in-claude

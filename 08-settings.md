# 08 Settings

Prefix: SET · Scope: account, project, per-chat and organization settings in the Claude app, including roles and account administration · Last checked: 2026-10-06

## Account settings

- **SET-001** `documented` Settings > Memory > "Generate memory from chats" turns memory on or off for the account, with "Pause memory" and "Reset memory" as the ways to turn it off. [mem]
- **SET-002** `documented` Settings > Memory > "Search and reference chats" turns chat search on or off. [mem]
- **SET-003** `documented` Settings > Memory > "Include sensitive topics in memory" lets Claude store sensitive topics from then on. [mem]
- **SET-004** `documented` Settings > Memory lists everything remembered under Topics, editable one by one. [mem]
- **SET-005** `documented` Settings > Memory > "Start import" adds pasted memory from another assistant; memory import is offered on Free, Pro, Max and Team, on the web and Claude Desktop. [imp]
- **SET-006** `documented` In the new Claude experience, Settings > General > "Instructions for Claude" holds the instructions that apply to every conversation, including the former Cowork Global instructions. [one]
- **SET-007** `documented` Settings > General > "Only on your computer" for Cowork tasks is removed from 2026-10-06 for Pro and Max. [cw-web]
- **SET-008** `documented` On Free, Pro and Max, an account's data export is started in Settings > Privacy on the web or in Claude Desktop, not in the iOS or Android apps; members of Team and Enterprise organizations have no export of their own. [exp] [exp-org]
- **SET-009** `documented` On Pro, Max, Team and seat-based Enterprise plans, Settings > Usage shows how much of the five-hour session limit and the weekly limits has been used; on usage-based Enterprise plans it tracks consumption instead. [usage]
- **SET-010** `documented` In the legacy memory experience, memory and chat search were in Settings > Capabilities instead of Settings > Memory. [mem]
- **SET-011** `documented` Settings > Reflect shows a monthly recap of how the account has used Claude; it is in beta on Free, Pro and Max on the web and Claude Desktop, and is not available on Team, Enterprise or Claude Mobile. [recap] [rn]
- **SET-012** `documented` The monthly recap is built from the same chat history as memory and appears only while memory is on; it has no toggle of its own, so turning memory off hides it. [recap] [rn]
- **SET-013** `documented` In the legacy memory experience, pausing or resetting memory also hides the monthly recap. [mem]
- **SET-014** `conflicting` The monthly recap article says the recap is turned off by switching off "Generate memory from chat history" in Settings > Capabilities, while the memory article puts the current switch, "Generate memory from chats", in Settings > Memory and places memory in Settings > Capabilities only for the legacy experience. [recap] [mem]

## Per-project settings

- **SET-020** `documented` A project has its own instructions and knowledge, set on the project's page. [proj]
- **SET-021** `observed` Claude's runtime instructions describe a per-project memory setting, connected or separate, that is changed on the project's page on the web and that Claude itself cannot change. (session 2026-10-06, claude.ai, outside projects)

## Per-chat settings

- **SET-030** `documented` "+" > "Memory" turns memory off for one chat or task, before the first message only. [mem]
- **SET-031** `documented` The ghost icon in a new chat outside a project starts an incognito chat. [inc]
- **SET-032** `documented` In a conversation, "+" > Connectors lists each connected connector with a toggle that decides whether Claude can use it in that conversation. [conn]
- **SET-033** `documented` A style can be chosen and changed at any point in a conversation. [sty]

## Capabilities that change context behaviour

- **SET-040** `documented` On paid plans, automatic context management of long conversations works only while code execution is enabled. [ctx]
- **SET-042** `documented` On Free, Pro and Max, "Code execution and file creation" is on by default and is switched in Settings > Capabilities, on the web, in Claude Desktop and in Claude Mobile. [files]
- **SET-043** `documented` On Team, and in new Enterprise organizations, code execution and file creation is on by default for the organization, and an owner can turn it off for everyone. [files]

## Organization settings (Team and Enterprise)

- **SET-050** `documented` Owners and Primary Owners turn memory on for the organization in Organization settings > Capabilities; turning it off deletes all members' memory. [mem]
- **SET-051** `documented` Project sharing for a Team or Enterprise organization is turned on or off under Organization settings > Data and privacy, in the Sharing section, and on Enterprise also per role under Organization settings > Roles. [share-org]
- **SET-052** `conflicting` Both export articles say only the Primary Owner of a Team or Enterprise organization can export its data, from Organization settings > Data and privacy on the web or in Claude Desktop, while the incognito article says organizational exports are available to account Owners. [exp-org] [exp] [inc]

## What Claude is told about settings

- **SET-060** `observed` Claude could not change any of these settings itself; when asked to stop using memory or past chats, it was instructed to name the setting and stop using the tools for the rest of the conversation. (session 2026-10-06, claude.ai, outside projects)
- **SET-061** `observed` The session's instructions carried a "Preferred browser" line naming the built-in browser and said it comes from a user setting of that name, which the user can change at any time. (session 2026-10-06, claude.ai, outside projects)
- **SET-062** `observed` The session's instructions listed web search, searching and referencing past chats, and generating memory from chat history as features the user can turn on or off in the conversation or in settings. (session 2026-10-06, claude.ai, outside projects)

## Sources

[conn]: https://claude.com/docs/connectors/getting-started
[ctx]: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
[cw-web]: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
[exp]: https://support.claude.com/en/articles/9450526-export-your-claude-data
[exp-org]: https://support.claude.com/en/articles/13346720-export-your-organization-s-data
[files]: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
[imp]: https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[recap]: https://support.claude.com/en/articles/15672559-see-your-monthly-recap
[rn]: https://support.claude.com/en/articles/12138966-release-notes
[share-org]: https://support.claude.com/en/articles/9927533-control-project-sharing-for-your-organization
[sty]: https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles
[usage]: https://support.claude.com/en/articles/9797557-usage-limit-best-practices

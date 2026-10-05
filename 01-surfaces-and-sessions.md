# 01 Surfaces and sessions

Prefix: SES · Scope: what a session is in the Claude app (web, desktop, mobile), how chat and Cowork relate, where sessions run · Last checked: 2026-10-05

## Chat and Cowork

- **SES-001** `documented` Claude Cowork and chat are being merged into one experience called Claude, in which Claude decides whether a request needs a quick answer or a task. [cw-proj] [one]
- **SES-002** `documented` The merged experience rolls out first to Pro and Max on web, desktop and mobile; Team and Free follow, and Enterprise admins get at least 30 days' notice. [blog-cw] [one]
- **SES-003** `documented` Once an account has moved to the merged experience, it cannot switch back to separate Chat and Cowork. [one]
- **SES-004** `documented` Chats, tasks, projects and settings carry over into the merged experience. [one]
- **SES-005** `documented` Cowork's former "Global instructions" are now part of "Instructions for Claude" in Settings > General. [one]
- **SES-006** `documented` Older Cowork tasks are not included in chat search; chats and new conversations are. [one]

## Where sessions run

- **SES-010** `documented` Cloud work runs in an isolated environment on Anthropic's servers. [cw-start]
- **SES-011** `documented` From 2026-10-06, new Cowork tasks on Pro and Max run in the cloud, and the "Only on your computer" option in Settings > General is removed. [cw-web]
- **SES-012** `documented` Tasks already started on the user's computer stay local until they finish. [cw-web]
- **SES-013** `documented` A cloud session started on desktop can use connected local folders, the browser and computer use only while Claude Desktop is open on that computer. [cw-web]
- **SES-014** `documented` Memory is shared between chat and Cowork only when Cowork runs in the cloud; Cowork sessions that run locally do not use memory. [mem]
- **SES-015** `documented` Claude Code on desktop keeps its folders and session history on that machine. [cw-web]
- **SES-016** `documented` Incognito chats open in the previous chat experience, so Claude cannot create files or run code in them. [inc] [one]

## Session state

- **SES-020** `observed` A chat in the merged experience ran in a private Linux workspace in Anthropic's cloud, with file tools and a shell. (session 2026-10-05, claude.ai, outside projects)
- **SES-021** `observed` Files and installed packages in that workspace persisted across turns of the same session and were not shared with any other session. (session 2026-10-05, claude.ai, outside projects)
- **SES-022** `observed` The session kept running whether or not the user was watching, and could be continued from another device. (session 2026-10-05, claude.ai, outside projects)
- **SES-023** `observed` The session could be linked to the user's computer through the Claude desktop app; Claude reached files on that computer only through that link, and only in folders the user connected. (session 2026-10-05, claude.ai, outside projects)
- **SES-025** `inferred` Two sessions share no transcript and no workspace files; they are connected only through memory (02), chat search (03) and, inside a project, the project's instructions and knowledge (04). Basis: SES-021, MEM-001, SRC-003, PRJ-020.
- **SES-026** `inferred` What a session learned in detail survives for other sessions only as far as it was saved to memory as a short distillate, or can be found again through chat search. Basis: MEM-002, MEM-010, SRC-002.

## Sources

[blog-cw]: https://claude.com/blog/cowork-is-now-claude
[cw-proj]: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
[cw-start]: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
[cw-web]: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude

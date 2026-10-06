# 01 Surfaces and sessions

Prefix: SES · Scope: what a session is in the Claude app (web, desktop, mobile), how chat and Cowork relate, where sessions run, and which Claude products and surfaces exist, on which plans and platforms · Last checked: 2026-10-06

## Chat and Cowork

- **SES-001** `documented` Claude Cowork and chat are merged into one experience called Claude: a single conversation with no mode to choose, in which Claude decides whether a request needs a quick answer or a task. [cw-proj] [one]
- **SES-002** `documented` The merged experience rolls out first to Pro and Max on web, desktop and mobile; Team and Free follow, and Enterprise admins get at least 30 days' notice. [blog-cw] [one]
- **SES-007** `documented` The merged experience reaches accounts in stages, so accounts on the same plan get it at different times; a Pro or Max account whose message box still offers "Chat" and "Cowork" does not have it yet. [one]
- **SES-008** `documented` Team and Enterprise organizations keep chat and Cowork as they are for now. [cw-org]
- **SES-003** `documented` Once an account has moved to the merged experience, it cannot switch back to separate Chat and Cowork. [one]
- **SES-004** `documented` Chats, tasks, projects and settings carry over into the merged experience, as do Cowork's connectors, skills, artifacts and files; former Cowork tasks open as before and can be continued. [one]
- **SES-009** `documented` In the merged experience, former Cowork tasks are listed together with chats in Recents. [one]
- **SES-005** `documented` Cowork's former "Global instructions" are now part of "Instructions for Claude" in Settings > General. [one]
- **SES-030** `documented` In the merged experience, Claude Desktop keeps the folder Cowork saved its work to (Storage folder in Settings), and folders the user gave Cowork access to are listed under Trusted folders. [one]
- **SES-031** `documented` The Claude Code documentation describes the Claude Desktop app with three tabs: Chat for conversations, Cowork for Dispatch and longer agentic work, and Code for software development; in the merged experience the Code tab stays where it was. [cc-desk] [one]
- **SES-053** `observed` On a Max account whose message box offered no "Chat" and "Cowork" options, Claude Desktop showed no Chat or Cowork tab either: a switch at the top of the window chose between conversations and Code, and the sidebar listed Dispatch under "More", marked beta, with a Dispatch section listing one conversation. (session 2026-10-06, Claude Desktop on macOS, outside projects, Max plan)

## Limits of the merged experience

- **SES-006** `documented` In the merged experience, "Search" does not include older Cowork tasks; it covers chats and new conversations, and older tasks are found by name in Recents. [one]
- **SES-016** `documented` Incognito chats open in the previous chat experience, so Claude cannot create files or run code in them. [inc] [one]
- **SES-032** `documented` In the merged experience, a conversation cannot be branched from an earlier point. [one]
- **SES-033** `documented` In the merged experience, "Add from GitHub" is not supported. [one]
- **SES-034** `documented` In the merged experience, Dispatch is not available to new users; existing users can keep using it for now. [one] [dispatch]

## Where sessions run

- **SES-010** `documented` A cloud session runs on Anthropic's servers instead of the user's computer, in an isolated environment, and the session and its files are saved to the user's Claude account. [cw-start] [cw-web]
- **SES-035** `documented` Each cloud session gets its own sandbox, created when the session starts and removed when it ends; sandboxes share no state with each other or across organizations. [cw-arch] [cw-safe]
- **SES-036** `documented` A cloud session cannot reach private or internal network addresses, such as the user's home or company network; all its outbound traffic passes through a mandatory proxy outside the sandbox that admits only allow-listed destinations. [cw-arch] [cw-safe]
- **SES-037** `observed` From the workspace shell of a Claude app conversation, a package registry was reachable but a request to support.claude.com was refused at the proxy; web pages were read through separate fetch and browser tools. (session 2026-10-06, claude.ai, outside projects)
- **SES-038** `documented` A cloud session's sandbox holds only short-lived, session-scoped tokens; connector authorization tokens never enter it, and connector calls are made on Anthropic's servers. [cw-arch]
- **SES-039** `documented` An organization's network settings are applied when a Cowork session is created; a change made during a conversation takes effect only in a new conversation. [cw-org]
- **SES-040** `documented` In a local Cowork session, the agent loop runs natively on the user's computer, while shell commands and code run in a dedicated Linux virtual machine that the platform's hypervisor isolates from the host. [cw-arch] [cw-org]
- **SES-041** `documented` A local Cowork session stores its conversation history on the user's computer. [cw-org]
- **SES-042** `documented` A local Cowork session may end if Claude Desktop is closed or the computer sleeps, while cloud sessions keep running in the background. [cw-start]
- **SES-011** `documented` From 2026-10-06, new Cowork tasks on Pro and Max run in the cloud, scheduled tasks move to the cloud as well, and the "Only on your computer" option in Settings > General is removed. [cw-web]
- **SES-012** `documented` Tasks already started on the user's computer stay local until they finish. [cw-web]
- **SES-015** `documented` Claude Code on desktop keeps its folders and session history on that machine. [cw-web]
- **SES-017** `documented` Past Cowork work is carried into Claude Code by downloading a local task's transcript from the note at its top, or the whole Cowork history from a notice in the app; projects and scheduled tasks do not carry over to Claude Code. [cw-web]
- **SES-018** `documented` On Team and Enterprise, the organization setting "Run Cowork in the cloud" in Organization settings > Cowork decides whether sessions can run in the cloud; it is on by default on Team and off by default on Enterprise, where an owner also grants the capability to a group through custom roles. [cw-org]
- **SES-019** `documented` Cowork is available on desktop, web, mobile and in the Claude in Chrome side panel, where opening the panel starts a Cowork session directly. [cw-web] [cw-start]
- **SES-058** `documented` Cowork is available on the paid plans only: in Claude Desktop for macOS and for Windows on Pro, Max, Team and Enterprise, and on the web and Claude Mobile on Pro, Max and Team, and on Enterprise where an admin has enabled it. [cw-start]
- **SES-043** `documented` Dispatch is one persistent conversation, reachable from phone and desktop, that runs its tasks on the user's desktop computer, which must be awake with Claude Desktop open. [dispatch]
- **SES-014** `documented` Memory is shared between chat and Cowork only when Cowork runs in the cloud; Cowork sessions that run locally do not use memory. [mem]

## Reaching the user's computer

- **SES-023** `documented` A cloud session reaches the user's computer, for example a local file or the browser, only through the Claude Desktop app on that computer over an Anthropic-brokered connection; it reads and writes local files only in folders the user connected, and each local tool call is checked against the user's permissions. [cw-arch] [cw-web]
- **SES-013** `documented` Local files, local connectors, the browser and computer use are reachable from a cloud session only while Claude Desktop is open on the user's computer; with the app closed, the session keeps running but cannot reach local files. [cw-web] [one]
- **SES-059** `documented` Computer use is in beta on Pro and Max, in Cowork and Claude Code in Claude Desktop for macOS and Windows; Team and Enterprise do not have it, it is turned on with "Enable computer use" in the desktop app's settings, and Claude asks before accessing each application. [cu] [cw-web]
- **SES-057** `observed` Contrary to [cw-web], which allows local files only to a cloud session started on desktop, a conversation started on claude.ai in a web browser, with Claude Desktop open on the user's Mac, read a file in a folder there after the user approved a prompt shown in the web page; the prompt said Claude could read and change the folder's files for this session and that files it uses leave the device. (session 2026-10-06, claude.ai in a web browser, outside projects, Max plan)
- **SES-054** `observed` A conversation started on claude.ai in a web browser, while Claude Desktop was open on the user's Mac, opened a page in Claude Desktop's built-in browser after a site approval. (session 2026-10-06, claude.ai in a web browser, outside projects, Max plan)
- **SES-055** `observed` Folders on the user's computer are connected per conversation: a folder added in one Claude Desktop conversation appeared in that conversation's "Used in this session" panel and could be listed there, also after the conversation was opened on the web, while two other conversations of the account had none; the device tools' description says an approved folder becomes readable and writable for that session only. (session 2026-10-06, Claude Desktop and claude.ai, outside projects, Max plan)
- **SES-056** `observed` Without a connected folder, a session's device tools still returned the names of the top-level folders in the user's home folder, marking Desktop, Documents and Downloads as needing a grant before they could be listed. (session 2026-10-06, claude.ai, outside projects)
- **SES-044** `documented` Local connectors and plugins that include local MCP servers work only through Claude Desktop; local MCP servers do not run in cloud sessions. [cw-web] [cw-arch]
- **SES-045** `documented` When a cloud task needs a file from the user's computer, Claude fetches a copy of just that file, and the work on it is processed on Anthropic's servers instead of staying on the computer. [cw-web] [cw-arch] [cw-safe]
- **SES-046** `documented` Browser traffic of a session, through the built-in browser or Claude in Chrome, comes from the user's computer, even when the session is steered from web or mobile. [cw-org]

## Scheduled tasks

- **SES-047** `documented` Scheduled tasks run remotely, so they run on schedule even while the computer sleeps or Claude Desktop is closed. [cw-sched] [cw-start]
- **SES-048** `documented` Each run of a scheduled task is its own Cowork session, whose results are reviewed like those of any other task. [cw-sched]
- **SES-049** `conflicting` Whether a scheduled task can use files on the user's computer: the scheduling article says scheduled tasks cannot be tied to a folder on the computer, yet its manual setup offers a folder and says a task that needs local files or apps runs only locally; the web, desktop and mobile article says scheduled tasks that use local files move to the cloud and need the desktop app open. [cw-sched] [cw-web]

## Session state

- **SES-020** `observed` A chat in the merged experience ran in a private Linux workspace in Anthropic's cloud, with file tools and a shell. (session 2026-10-06, claude.ai, outside projects)
- **SES-021** `observed` Files and installed packages in that workspace persisted across turns of the same session and were not shared with any other session. (session 2026-10-06, claude.ai, outside projects)
- **SES-022** `documented` More involved tasks keep running in the cloud after the user closes the laptop or leaves the page, and a session can be opened from another surface, including Claude Mobile, to follow progress, answer Claude's questions or redirect the work. [one] [cw-web]
- **SES-050** `documented` Cowork uses the same agentic architecture as Claude Code, without a terminal. [cw-start]
- **SES-024** `observed` A Claude app conversation ran on a Claude Code harness: its runtime instructions said so, and the workspace held the conversation as a Claude Code transcript, a JSONL file under `~/.claude/projects/` with folders for subagent transcripts and large tool results, most of whose entries name the entry point `remote_cowork`. (session 2026-10-06, claude.ai, outside projects)
- **SES-027** `documented` For complex tasks, Claude may coordinate several sub-agents working at the same time. [cw-start]
- **SES-028** `observed` A subagent of the session ran in the same workspace as the parent: a file it wrote was visible to the parent session. (session 2026-10-06, claude.ai, outside projects)
- **SES-029** `observed` A subagent's final report came back to the parent as a tool result marked as model output that carries no authority of the user; the tool's description says the report is not shown to the user. (session 2026-10-06, claude.ai, outside projects)
- **SES-051** `documented` The user can step into a running task to correct its course or give further direction. [cw-start]
- **SES-052** `observed` The session's tools included one for messaging other sessions; its description names subagents, other local sessions and the account's cloud sessions as recipients, and says a cloud session receives such a message but cannot yet reply. (session 2026-10-06, claude.ai, outside projects)
- **SES-025** `inferred` Two sessions share no transcript and no workspace files. They are connected through memory (02), chat search (03), the account's instructions (05) and extensions (07), inside a project through its instructions and knowledge (04), through folders on the user's computer that both can reach, and through messages one session can send another. Basis: SES-021, SES-035, SES-023, SES-052, MEM-001, SRC-003, INS-001, EXT-007, PRJ-020.
- **SES-026** `inferred` What a session learned in detail survives for other sessions only as far as it was saved to memory as a short distillate, can be found again through chat search, was written to a place a later session can read, such as a connected folder on the user's computer, or was sent to another session as a message. Basis: MEM-002, MEM-010, SRC-002, SES-023, SES-052.

## Sources

[blog-cw]: https://claude.com/blog/cowork-is-now-claude
[cc-desk]: https://code.claude.com/docs/en/desktop
[cu]: https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork
[cw-arch]: https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
[cw-org]: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
[cw-proj]: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
[cw-safe]: https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
[cw-sched]: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
[cw-start]: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
[cw-web]: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
[dispatch]: https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude

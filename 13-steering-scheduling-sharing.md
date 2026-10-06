# 13 Steering, scheduling and sharing

Prefix: WRK · Scope: working with a session in the Claude app once it runs: steering, permission modes and approvals, notifications, scheduled tasks, and managing and sharing chats · Last checked: 2026-10-06

## Steering a running task

- **WRK-001** `documented` While Claude works on a Cowork task, progress indicators show what it is doing at each step, and Claude sets out its reasoning and approach so that the user can follow along. [cw-start]
- **WRK-002** `documented` The user can stop Claude while it works. [one]
- **WRK-003** `documented` In Claude Desktop, a message sent while Claude is still replying waits in the conversation; "Send now" on the first waiting message stops the current reply and sends that message next, and Cmd/Ctrl+Enter sends a message at once, interrupting the current turn. [rn-desk]
- **WRK-004** `documented` In Claude Desktop, a message sent while a Research run is in progress is queued and sent when the report is ready. [rn-desk]
- **WRK-005** `documented` In Cowork in Claude Desktop, replies that Claude writes in the middle of a task are shown under a collapsed "Working notes" row. [rn-desk]
- **WRK-006** `documented` In the merged experience, several tasks can run at the same time. [one]
- **WRK-007** `documented` The safety article advises watching a running task for unexpected patterns, such as files or websites the user did not mention or a scope that grows beyond the request, instead of checking every command, and stopping the task at once if something seems off. [cw-safe]
- **WRK-008** `documented` In Dispatch, Claude messages the outcome of a task to the thread instead of showing every step; the sessions it starts for a task, in Claude Code for development work and in Cowork for knowledge work, appear in the respective sidebar, where each can be opened for details. [dispatch]
- **WRK-009** `documented` According to the Cowork guide, each task that Dispatch starts appears under the Dispatch group in the sidebar with its state: Running, Awaiting input, Awaiting answer, Completed, Error or Archived. [dispatch-guide]

## Permission modes

- **WRK-010** `documented` In the merged experience, a permission setting in the message box decides how independently Claude works; it offers Manual, the default, and Auto. [one] [cw-start]
- **WRK-011** `documented` The permission setting applies to the whole conversation and can be changed at any time. [one]
- **WRK-012** `documented` In Manual, Claude asks before it takes an action, and the user allows or denies each request. [one] [cw-start]
- **WRK-013** `documented` In Auto, Claude keeps working without stopping to ask about each step; instead, Claude reviews each action for safety before it runs, for example for data exfiltration or prompt injection, and blocks anything it judges unsafe. [one] [cw-start] [cw-safe]
- **WRK-014** `documented` When an action is blocked in Auto, Claude looks for a safer way to finish the task or pauses and asks the user; if it keeps running into blocks, it goes back to asking permission for each step. [cw-start]
- **WRK-015** `documented` Auto covers the user's connectors and plugins, the built-in browser, Claude in Chrome and some Cowork actions such as fetching websites. [cw-start]
- **WRK-016** `documented` Because of the extra checking, Auto uses more of the usage limit than the other modes. [cw-start]
- **WRK-017** `documented` Cowork has three modes that decide when Claude asks permission before an action, chosen in the mode selector of the chat box and changeable at any time: "Manually approve" (Manual), "Automatically approve" (Auto) and "Skip all approvals" (Skip); for the merged experience, the same article names only Manual and Auto. [cw-start]
- **WRK-018** `documented` In "Skip all approvals", Claude does not pause to ask, and nothing checks its actions automatically. [cw-start] [cw-safe]
- **WRK-019** `documented` "Manually approve" was formerly named "Ask before acting", and "Skip all approvals" was formerly named "Act without asking". [cw-start]
- **WRK-020** `documented` The Cowork article names a default mode, Manual, only for the merged experience, and none among Cowork's three modes. [cw-start]
- **WRK-021** `documented` The Claude in Chrome side panel, where it runs as a Cowork session, starts in "Automatically approve"; if the user switches to another mode, the side panel keeps that choice for later sessions. [chrome] [chrome-perm]
- **WRK-022** `documented` The documentation advises using "Skip all approvals" only when every action, connector, file and app involved in the task is fully trusted. [cw-start]
- **WRK-023** `documented` The documentation says that no mode replaces the user's judgment, and advises staying close and reviewing what Claude does, or switching to "Manually approve", for work with real consequences, such as money, messages sent as the user or important files. [cw-start] [one] [cw-safe]
- **WRK-024** `documented` The safety article advises "Manually approve" when a task touches sensitive files, accounts or sites, when a tool, plugin or site is used for the first time, and when mistakes would be hard to undo. [cw-safe]

## Approvals

- **WRK-030** `documented` How a mode treats a connector tool depends on the permission set for that tool (EXT-012): in Manual, a tool set to "Always allow" runs without a prompt, and a tool set to "Needs approval" asks for permission. [cw-start]
- **WRK-031** `documented` In Auto, read-only connector tools set to "Always allow" run without a prompt; for write or delete tools set to "Always allow", and for every tool set to "Needs approval", Claude decides. [cw-start]
- **WRK-032** `documented` In Skip, connector tools set to "Always allow" or to "Needs approval" run without a prompt. [cw-start]
- **WRK-033** `documented` A connector tool set to "Blocked" is denied in every mode. [cw-start]
- **WRK-034** `documented` Claude needs the user's explicit permission before it permanently deletes files: a permission prompt appears, and the user must select "Allow". [cw-start] [cw-safe] [one]
- **WRK-035** `documented` Claude asks before permanently deleting files in every mode. [cw-safe]
- **WRK-036** `documented` The safety article distinguishes read tools, which let Claude access content, from write tools, which act in the user's environment, and says Cowork treats write tools differently because they carry more risk. [cw-safe]
- **WRK-037** `documented` Cowork's approval dialog for a connector tool offers "Allow for this task" and "Allow for all tasks"; "Allow for this task" stays available when the organization has turned off persistent "Always allow". [rn-desk] [cw-org]
- **WRK-038** `documented` In Claude Desktop, the permission prompt for fetching a web page preselects "Allow all for this website" where that grant is available and "Allow once" otherwise, and pressing Enter always answers "Allow once". [rn-desk]
- **WRK-039** `documented` A permission prompt of a task that Dispatch started is forwarded to the user; if the user does not answer within ten minutes, the request is denied automatically and the task continues without that action. [dispatch-guide]

## Organization controls on approvals

- **WRK-040** `documented` On Team and Enterprise, the organization setting that allows "Automatically approve" mode, in Organization settings > Cowork under Permissions, decides whether members can use that mode in Cowork; it is on by default, and while it is off the mode does not appear in members' mode selector. [cw-org] [cw-start]
- **WRK-041** `documented` On Team and Enterprise, the organization setting that allows "Always allow" for connector tools, in Organization settings > Cowork under Permissions, decides whether members can skip per-task approval for write-capable connector tools in Cowork; it is off by default. [cw-org]
- **WRK-042** `documented` While the organization does not allow "Always allow" for connector tools, the "Allow for all tasks" option in Cowork's approval dialog is greyed out, even where the organization's tool policies allow the tool, always-allow preferences saved earlier for write tools are not honoured, and members approve these tools for each task. [cw-org] [cw-start]
- **WRK-043** `documented` While the organization does not allow "Always allow" for connector tools, a tool is exempt as read-only only if its connector annotates it as read-only; most custom connectors do not annotate their tools, so every tool on them needs approval. [cw-org]
- **WRK-044** `documented` On Enterprise, the organization's "Always allow" setting for connector tools works alongside the grants of custom roles: the most restrictive layer wins, and a role grant cannot override the setting. [cw-org]
- **WRK-045** `documented` For sessions in the cloud, the architecture overview names two organization controls on approvals: requiring fresh approval for every permission-gated tool call, by turning off persistent "always allow", and deciding whether members can run sessions without per-call approval prompts. [cw-arch]
- **WRK-046** `documented` An organization's policy can block "Skip all approvals", as a fix in the Claude Desktop release notes mentions. [rn-desk]
- **WRK-047** `documented` In tasks that run on the user's computer, a connector tool that the organization's tool policy sets to "Restrict to Ask" asks for the user's approval even in "Skip all approvals". [rn-desk]

## Notifications

- **WRK-050** `documented` When Claude finishes a Cowork task or needs the user's input, the user gets a notification on their phone. [cw-web]
- **WRK-051** `documented` In Dispatch, the phone gets a push notification when a task is done or when Claude needs the user's go-ahead. [dispatch]
- **WRK-052** `documented` The Claude in Chrome extension can notify the user on the computer, also with a sound, when Claude finishes a task or needs the user's permission or another action; the user turns notifications on for this. [chrome]
- **WRK-053** `documented` On macOS, Claude Desktop asks for permission to send notifications when its first notification is about to appear, not at launch. [rn-desk]
- **WRK-054** `documented` Claude Desktop shows a "Scheduled task failed" notification when a scheduled task could not start; the release notes mention it in an entry for third-party deployments. [rn-desk]

## Scheduled tasks

- **WRK-060** `documented` A scheduled task is a task that Claude runs automatically on a recurring schedule, or on demand: the user describes it once, and Claude saves the prompt as the task's instructions and runs them at the chosen cadence. [cw-sched]
- **WRK-061** `documented` Scheduled tasks are available on Pro, Max, Team and Enterprise, in Cowork and in the merged experience, on desktop, web and mobile. [cw-sched] [cw-web]
- **WRK-062** `documented` A scheduled task has the same capabilities as a regular Cowork task, including connected tools, skills and installed plugins. [cw-sched]
- **WRK-063** `documented` The scheduling article says scheduled tasks use the built-in schedule options and work with the user's connectors and the files saved to the Claude account; what the documentation says about files on the user's computer conflicts (SES-049). [cw-sched]
- **WRK-064** `documented` In the merged experience, a scheduled task is created from any conversation: the user describes the task and how often it should run, answers Claude's questions, reviews the task name, schedule and instructions that Claude proposes, and clicks "Schedule". [cw-sched] [one]
- **WRK-065** `documented` In Cowork, a scheduled task is created on the Scheduled page, opened from the left sidebar, with "New task" and then either "Create with Claude" or "Set up manually". [cw-sched]
- **WRK-066** `documented` "Create with Claude" opens a new task with a prompt that asks Claude to create a scheduled task; Claude may ask multiple-choice questions, then states the task's name, schedule and content, and the user confirms with "Schedule". [cw-sched]
- **WRK-067** `documented` Typing /schedule in a Cowork task also starts the creation of a scheduled task. [cw-start]
- **WRK-068** `documented` "Set up manually" asks for a task name, the prompt, the approval mode and the frequency, and optionally for a model and a folder for Claude to work in. [cw-sched]
- **WRK-069** `documented` The frequencies offered in manual set-up are hourly, daily, weekly, on weekdays and manually. [cw-sched]
- **WRK-070** `documented` The Scheduled page, opened from the left sidebar on any surface, lists the user's scheduled tasks with their upcoming and past runs; there the user can edit a task's instructions or cadence, pause, resume or delete a task, and run it on demand. [cw-sched]
- **WRK-071** `documented` The Claude Desktop release notes refer to schedules beyond the options of the manual form: every N days or months, a day of the month combined with a weekday, cron expressions and one-time tasks. [rn-desk]
- **WRK-072** `documented` Scheduled tasks that Claude creates for the user use "Automatically approve" by default where the organization allows it, so their runs use tools without asking first and pause only when something looks unsafe. [rn-desk]
- **WRK-073** `documented` A run of a scheduled task can ask the user for approval: the Claude Desktop release notes mention approval prompts in scheduled runs, with an "Allow for all scheduled runs" choice. [rn-desk]
- **WRK-074** `documented` In Claude Desktop, a scheduled task that could not reach the model at all is run again automatically after 5, 15 and 30 minutes. [rn-desk]
- **WRK-075** `documented` The safety article points out that scheduled tasks run while the user is away and cannot be watched in real time, and advises starting with low-risk tasks, not scheduling tasks that use sensitive files or take actions that are hard to undo, such as sending messages or making purchases, reviewing the results after each run, and pausing or deleting tasks that are no longer needed. [cw-safe]

## Managing chats

- **WRK-080** `documented` On the web, a conversation is renamed or deleted by hovering over it in the left sidebar, or in the full history under "Chats and tasks", and clicking the "⋮" button on its right; a deletion has to be confirmed. [del]
- **WRK-081** `documented` Several conversations are deleted at once under "Chats and tasks": the user clicks "Select" in a conversation's "⋮" menu, ticks further conversations or "Select all", and clicks "Delete", which asks for confirmation. [del]
- **WRK-082** `documented` In Claude for iOS, a conversation is renamed or deleted by touching and holding it in the chat list, and the open conversation is deleted from the "⋯" button at the top right. [del]
- **WRK-083** `documented` In Claude for Android, the open conversation is renamed or deleted from the "⋮" menu at the top right, and several conversations are deleted from the chat list with the checklist icon. [del]
- **WRK-084** `documented` The help-center article on renaming and deleting conversations covers the consumer plans; for commercial customers, the Privacy Center describes renaming or deleting a conversation by clicking its name at the top of the screen, and deleting several from Recents > "View all" with "Delete Selected". [del] [del-org]
- **WRK-085** `documented` On consumer plans, deleting a conversation leaves the account's other data, such as projects and account information, in place until the user deletes it or deletes the account. [del]
- **WRK-086** `documented` A Cowork task is deleted with "Delete" from the "⋮" next to it, or by selecting tasks in the task list and clicking the trash icon, and it disappears from the task history at once. [cw-start]
- **WRK-087** `documented` Deleting a session also deletes the copies of local files that Claude fetched for it, in line with Anthropic's data retention practices. [cw-web]
- **WRK-088** `documented` In Claude Desktop, the current chat, project, task or coding session can be archived or deleted from the command palette, opened with Cmd+K, or Ctrl+K on Windows and Linux. [rn-desk]

## Sharing chats

- **WRK-100** `documented` Chats are private by default; sharing a chat gives others a view-only snapshot of it. [share] [share-people] [share-link]
- **WRK-101** `documented` The snapshot contains all messages sent before the chat was shared, including artifacts; messages sent afterwards stay private until the user updates the snapshot. [share] [share-people] [share-link]
- **WRK-102** `documented` "Update shared chat" in the share dialog replaces the old snapshot with the current chat for everyone who has access; the project sharing article for Team and Enterprise names the control "Update", next to "New messages since last shared", and the share-and-unshare article describes unsharing the chat and sharing it again as the way to include new messages. [share-people] [vis] [share]
- **WRK-103** `documented` Viewers of a shared chat cannot continue it, reply in it, copy it into their own account or download files from it. [share-people] [share-link]
- **WRK-104** `documented` Raw data returned by connectors or MCP tool calls is not shown in a shared chat; viewers see the conversation and Claude's final responses. [share] [share-people]
- **WRK-105** `documented` Inviting specific people by email is the default way to share a chat and is available on Free, Pro, Max, Team and Enterprise; it is done on claude.ai on the web and not yet from the mobile app, while a chat shared with someone opens on any device. [share-people]
- **WRK-106** `documented` People are invited from the chat's "Share" button, under "People with access"; each gets an email with the sharer's name, the chat title and a link that opens only for the invited address, so a forwarded invitation opens for no one else. [share-people]
- **WRK-107** `documented` Invited people see the sharer's name; an invited person without a Claude account can sign up with the invited address, and a free account is enough to view the chat. [share-people]
- **WRK-108** `documented` An invitation shows as pending until it is opened, can be removed at any time and expires after 30 days if it is not opened; the number of people a user can invite in a day is limited. [share-people]
- **WRK-109** `documented` A person is removed under "People with access" in the share dialog, and "Turn off" there stops sharing the chat altogether, after which the link stops working for everyone at once. [share-people]
- **WRK-110** `documented` With a public link, anyone who has the link can view the snapshot without a Claude account; a public link cannot be limited to specific people. [share-link]
- **WRK-111** `documented` Public links are available on Free, Pro and Max, and not on Team and Enterprise. [share-link] [share] [share-people]
- **WRK-112** `documented` A public link is turned off in the "Share" menu, by setting the chat to Private, or under Settings > Privacy > Shared chats; the link then stops working at once, but copies, screenshots and archives that others already made are not removed. [share-link] [share]
- **WRK-113** `documented` Every shared chat page carries a "noindex" instruction for search engines, Anthropic publishes no directory or sitemap of shared chats, and each link is a long random string. [share-link]
- **WRK-114** `documented` The public links article says Anthropic cannot control where a link is posted, copies made by viewers or third-party services, or crawlers that ignore "noindex", and advises treating a public link as public. [share-link]
- **WRK-115** `documented` Settings > Privacy > Shared chats lists the chats a user has shared, each with its date, and lets the user stop sharing each one; the share-and-unshare article describes this list for Free, Pro and Max. [share] [share-people]
- **WRK-116** `documented` Files attached to a chat are not included in a public link. [share-link] [share]
- **WRK-117** `conflicting` Whether files attached to a chat are visible when the chat is shared inside an organization: the share-and-unshare article, which also covers Team and Enterprise, says an attached file is not part of the snapshot and stays private, while the article on sharing with specific people says invited people do not see attached files unless the chat was shared within the sharer's organization. [share] [share-people]
- **WRK-118** `documented` On Team and Enterprise, sharing stays inside the organization: only email addresses on the organization's domain can be invited, and a General access option lets any signed-in member of the organization who has the link view the chat. [share-people] [share-link] [share]
- **WRK-119** `documented` A coworker who is invited without having a Claude seat is asked to sign in and, depending on how the organization is set up, either gets access automatically or is told to ask their admin. [share-people]
- **WRK-120** `documented` On Team and Enterprise, admins can turn off chat sharing for the organization and can see and revoke shared chats. [share-people]
- **WRK-121** `conflicting` Whether a Team organization has an audit log of chat sharing: the article on sharing with specific people says admins on Team and Enterprise can view sharing activity in the audit log, while the audit logs article says audit logs are available for Enterprise organizations only. [share-people] [audit]
- **WRK-122** `documented` Deleting a chat removes its shared snapshot, and its link stops working. [share-people]
- **WRK-123** `documented` A Cowork session cannot be shared with others; artifacts created in it can be shared one by one. [cw-start]

## Sources

[audit]: https://support.claude.com/en/articles/9970975-access-audit-logs
[chrome]: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome
[chrome-perm]: https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide
[cw-arch]: https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
[cw-org]: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
[cw-safe]: https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
[cw-sched]: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
[cw-start]: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
[cw-web]: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
[del]: https://support.claude.com/en/articles/8230524-delete-or-rename-a-conversation
[del-org]: https://privacy.claude.com/en/articles/11117329-how-can-i-delete-or-rename-a-conversation
[dispatch]: https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork
[dispatch-guide]: https://claude.com/docs/cowork/guide/dispatch
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[rn-desk]: https://claude.com/docs/cowork/changelog
[share]: https://support.claude.com/en/articles/10593882-share-and-unshare-chats
[share-link]: https://support.claude.com/en/articles/16762437-public-links-for-shared-chats
[share-people]: https://support.claude.com/en/articles/16762496-share-a-chat-with-specific-people
[vis]: https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing

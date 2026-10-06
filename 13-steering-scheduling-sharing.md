# 13 Steering, scheduling and sharing

Prefix: WRK · Scope: working with a session in the Claude app once it runs: steering, permission modes and approvals, notifications, scheduled tasks, and managing and sharing chats · Last checked: 2026-10-06

## Steering a running task

- **WRK-001** `documented` While Claude works on a Cowork task, progress indicators show what it is doing at each step, and Claude sets out its reasoning and approach so that the user can follow along. [cw-start]
- **WRK-002** `documented` Claude can be stopped by the user in the middle of its work. [one]
- **WRK-003** `documented` In Claude Desktop, a message that the user sends before Claude has finished its reply is held back and shown in the conversation like a sent one; the first held message comes with "Send now", which ends the running reply and delivers that message next, and the shortcut Cmd/Ctrl+Enter delivers a message immediately and cuts the current turn short. [rn-desk]
- **WRK-004** `documented` In Claude Desktop, a message that the user sends during a Research run is not delivered at once: it joins a queue and goes out once the report is finished. [rn-desk]
- **WRK-005** `documented` In Cowork in Claude Desktop, replies that Claude writes in the middle of a task are shown under a collapsed "Working notes" row. [rn-desk]
- **WRK-006** `documented` In the merged experience, several tasks can run at the same time. [one]
- **WRK-007** `documented` The safety article advises watching a running task for unexpected patterns, such as files or websites the user did not mention or a scope that grows beyond the request, instead of checking every command, and stopping the task at once if something seems off. [cw-safe]
- **WRK-008** `documented` In Dispatch, Claude reports the outcome of a task in the thread and does not show every step; a session that Dispatch started for the task can be opened to see the details. [dispatch] [dispatch-guide]
- **WRK-009** `documented` According to the Cowork guide, a task that Dispatch starts is shown with one of six states: Running, Awaiting input, Awaiting answer, Completed, Error or Archived. [dispatch-guide]
- **WRK-124** `documented` Where the sessions that Dispatch starts are listed: the help article puts them in the sidebar of Claude Code or of Cowork, depending on the kind of work, and the Cowork guide puts every one of them in the sidebar under a group named Dispatch. [dispatch] [dispatch-guide]

## Permission modes

- **WRK-010** `documented` In the merged experience, the message box holds a setting for permissions that governs how far Claude acts on its own; its two values are Manual, which is the default, and Auto. [one] [cw-start]
- **WRK-011** `documented` The permission setting of the merged experience covers a conversation as a whole, and the user is free to change it at any moment. [one]
- **WRK-012** `documented` In Manual, Claude asks before it takes an action, and the user allows or denies each request. [one] [cw-start]
- **WRK-013** `documented` In Auto, the user is not asked step by step: a safety review by Claude comes before every action, looking for instance for prompt injection or for data being exfiltrated, and an action that fails the review is blocked. [one] [cw-start] [cw-safe]
- **WRK-014** `documented` After a block in Auto, Claude either tries to complete the task by a safer route or stops and puts the question to the user; repeated blocks make it return to requesting permission step by step. [cw-start]
- **WRK-015** `documented` Auto extends to every connector and plugin the user already has, to both browsers (the built-in one and Claude in Chrome) and to part of Cowork's own actions, of which fetching a website is the example given. [cw-start]
- **WRK-016** `documented` Since the safety review is extra work, Auto consumes a larger part of the usage limit than Manual or Skip. [cw-start]
- **WRK-017** `documented` Cowork has three modes that decide when Claude asks permission before an action, chosen in the mode selector of the chat box and changeable at any time: "Manually approve" (Manual), "Automatically approve" (Auto) and "Skip all approvals" (Skip). [cw-start]
- **WRK-018** `documented` In "Skip all approvals", no approval is requested from the user and no automatic review of Claude's actions takes place. [cw-start] [cw-safe]
- **WRK-019** `documented` "Manually approve" was formerly named "Ask before acting", and "Skip all approvals" was formerly named "Act without asking". [cw-start]
- **WRK-020** `documented` The Cowork article names no default among Cowork's three modes. [cw-start]
- **WRK-021** `documented` The Claude in Chrome side panel, where it runs as a Cowork session, starts in "Automatically approve"; if the user switches to another mode, the side panel keeps that choice for later sessions. [chrome] [chrome-perm]
- **WRK-022** `documented` The documentation advises using "Skip all approvals" only when every action, connector, file and app involved in the task is fully trusted. [cw-start]
- **WRK-023** `documented` The documentation says that no mode replaces the user's judgment, and advises staying close and reviewing what Claude does, or switching to "Manually approve", for work with real consequences, such as money, messages sent as the user or important files. [cw-start] [one] [cw-safe]
- **WRK-024** `documented` The safety article advises "Manually approve" in three cases: sites, accounts or files that are sensitive are involved; a tool, plugin or site is new to the user; or an error could hardly be reversed, as with a sent message or a purchase. [cw-safe]

## Approvals

- **WRK-030** `documented` How a mode treats a connector tool depends on the permission set for that tool: in Manual, a tool set to "Always allow" runs without a prompt, and a tool set to "Needs approval" asks for permission. [cw-start]
- **WRK-031** `documented` In Auto, read-only connector tools set to "Always allow" run without a prompt; for write or delete tools set to "Always allow", and for every tool set to "Needs approval", Claude decides. [cw-start]
- **WRK-032** `documented` In Skip, connector tools set to "Always allow" or to "Needs approval" run without a prompt. [cw-start]
- **WRK-033** `documented` A connector tool set to "Blocked" is denied in every mode. [cw-start]
- **WRK-034** `documented` In Cowork, Claude needs the user's explicit permission before it permanently deletes files: a permission prompt appears, and the user must select "Allow". [cw-start] [cw-safe]
- **WRK-035** `documented` Whichever mode is in use, a permanent deletion of files is preceded by a question to the user. [cw-safe]
- **WRK-125** `documented` In the merged experience, Claude's default is to ask before files are permanently deleted. [one]
- **WRK-036** `documented` The safety article distinguishes read tools, which let Claude access content, from write tools, which act in the user's environment, and says Cowork treats write tools differently because they carry more risk. [cw-safe]
- **WRK-037** `documented` Cowork's approval dialog for a connector tool carries the choices "Allow for this task" and "Allow for all tasks"; the first of them remains on offer in organizations that have switched persistent "Always allow" off. [rn-desk] [cw-org]
- **WRK-038** `documented` In Claude Desktop, the default choice on the permission prompt for fetching a web page is "Allow all for this website" where that grant can be given and "Allow once" otherwise, while the Enter key always gives "Allow once". [rn-desk]
- **WRK-039** `documented` When a task started by Dispatch needs permission, the prompt is passed on to the user; a request left unanswered for ten minutes is denied automatically, and the task goes on without the action in question. [dispatch-guide]

## Organization controls on approvals

- **WRK-040** `documented` Team and Enterprise organizations have a setting, under Permissions in Organization settings > Cowork, that allows or withholds "Automatically approve" in Cowork for their members; it starts switched on, and once it is switched off the members' mode selector no longer lists the mode. [cw-org] [cw-start]
- **WRK-041** `documented` Under Permissions in Organization settings > Cowork, Team and Enterprise organizations also have a setting that allows "Always allow" for connector tools; it decides whether a member can stop being asked in each Cowork task about connector tools that are able to write, and it starts switched off. [cw-org]
- **WRK-042** `documented` While the organization does not allow "Always allow" for connector tools, the "Allow for all tasks" option in Cowork's approval dialog is greyed out, even where the organization's tool policies allow the tool, always-allow preferences saved earlier for write tools are not honoured, and members approve these tools for each task. [cw-org] [cw-start]
- **WRK-043** `documented` While an organization withholds "Always allow" for connector tools, a tool counts as read-only, and so needs no approval in each task, solely where its connector marks it as such; most custom connectors mark nothing, which puts all their tools under the approval rule. [cw-org]
- **WRK-044** `documented` On Enterprise, the organization's "Always allow" setting for connector tools works alongside the grants of custom roles: the most restrictive layer wins, and a role grant cannot override the setting. [cw-org]
- **WRK-045** `documented` For cloud sessions, the architecture overview lists two approval controls of an organization: with persistent "always allow" switched off, each call of a tool that needs permission has to be approved anew; and the organization decides whether its members may run a session in which calls are not approved one by one. [cw-arch]
- **WRK-046** `documented` An organization's policy can block "Skip all approvals", as a fix in the Claude Desktop release notes mentions. [rn-desk]
- **WRK-047** `documented` In newly started tasks that run on the user's computer, a connector tool that the organization's tool policy sets to "Restrict to Ask" asks for the user's approval even in "Skip all approvals". [rn-desk]

## Notifications

- **WRK-050** `documented` The user's phone receives a notification in two situations: a Cowork task is finished, or Claude is waiting for input from the user. [cw-web]
- **WRK-051** `documented` Dispatch sends a push notification to the user's phone both on the completion of a task and at a point where Claude cannot proceed without the user's go-ahead. [dispatch]
- **WRK-052** `documented` The Claude in Chrome extension can send a notification on the computer once Claude has finished a task or is waiting for the user's permission or another action, and can play a sound when the user's attention is needed; the user turns notifications on for this. [chrome]
- **WRK-053** `documented` On macOS, Claude Desktop asks for permission to send notifications when its first notification is about to appear, not at launch. [rn-desk]
- **WRK-054** `documented` Claude Desktop shows a "Scheduled task failed" notification when a scheduled task could not start; the release notes mention it in an entry for third-party deployments. [rn-desk]

## Scheduled tasks

- **WRK-060** `documented` A scheduled task is work that the user describes a single time and that Claude then carries out by itself, repeatedly or whenever the user asks for a run; the user's prompt is stored as the instructions of the task, and the cadence the user picked determines when they are run. [cw-sched]
- **WRK-061** `documented` Every paid plan (Pro, Max, Team, Enterprise) includes scheduled tasks, in Cowork and in the merged experience; they can be used on desktop, and on web and mobile where Cowork is offered there, which is a beta for Pro, Max and Team and, on Enterprise, depends on an owner enabling it. [cw-sched] [cw-web]
- **WRK-062** `documented` What an ordinary Cowork task can use, a scheduled task can use too; the scheduling article names installed plugins, skills and connected tools. [cw-sched]
- **WRK-063** `documented` According to the scheduling article, a scheduled task draws on the user's connectors and on files stored in the Claude account, and its timing comes from the schedule options that are built in. [cw-sched]
- **WRK-064** `documented` In the merged experience, any conversation can create a scheduled task: the user says what should be done and at what interval, replies to the questions Claude has, checks the name, the schedule and the instructions that Claude then proposes for the task, and clicks "Schedule". [cw-sched] [one]
- **WRK-065** `documented` In Cowork, a scheduled task is created on the Scheduled page, opened from the left sidebar, with "New task" and then either "Create with Claude" or "Set up manually". [cw-sched]
- **WRK-066** `documented` "Create with Claude" starts a new task whose prompt is already filled in with a request for a scheduled task; Claude can put multiple-choice questions to the user first, and then presents the task's name, its schedule and what it will do, which the user confirms with "Schedule". [cw-sched]
- **WRK-067** `documented` Typing /schedule in a Cowork task also starts the creation of a scheduled task. [cw-start]
- **WRK-068** `documented` "Set up manually" asks for a task name, the prompt, the approval mode and the frequency, and optionally for a model and a folder for Claude to work in. [cw-sched]
- **WRK-069** `documented` The frequencies offered in manual set-up are hourly, daily, weekly, on weekdays and manually. [cw-sched]
- **WRK-070** `documented` The Scheduled page, opened from the left sidebar on any surface, lists the user's scheduled tasks with their upcoming and past runs; there the user can edit a task's instructions or cadence, pause, resume or delete a task, and run it on demand. [cw-sched]
- **WRK-071** `documented` The Claude Desktop release notes refer to schedules beyond the options of the manual form: every N days or months, a day of the month combined with a weekday, cron expressions and one-time tasks. [rn-desk] [cw-sched]
- **WRK-072** `documented` In Claude Desktop, a scheduled task that Claude sets up on the user's behalf gets "Automatically approve" as its default mode, provided the organization permits that mode; such a task's runs then call tools unasked and pause only for something that seems unsafe. [rn-desk]
- **WRK-073** `documented` A run of a scheduled task can ask the user for approval: the Claude Desktop release notes mention approval prompts in scheduled runs, with an "Allow for all scheduled runs" choice. [rn-desk]
- **WRK-074** `documented` In Claude Desktop, when a run of a scheduled task fails because the model was out of reach altogether, the task is started again automatically after 5 minutes, then after 15, then after 30. [rn-desk]
- **WRK-075** `documented` The safety article points out that scheduled tasks run while the user is away and cannot be watched in real time, and advises starting with low-risk tasks, not scheduling tasks that use sensitive files or take actions that are hard to undo, such as sending messages or making purchases, reviewing the results after each run, and pausing or deleting tasks that are no longer needed. [cw-safe]

## Managing chats

- **WRK-080** `documented` On consumer plans, a conversation on the web is renamed or deleted by hovering over it in the left sidebar, or in the full history under "Chats and tasks", and clicking the "⋮" button on its right; a deletion has to be confirmed. [del]
- **WRK-081** `documented` On consumer plans, several conversations on the web are deleted at once under "Chats and tasks": the user clicks "Select" in a conversation's "⋮" menu, ticks further conversations or "Select all", and clicks "Delete", which asks for confirmation. [del]
- **WRK-082** `documented` On consumer plans, a conversation in Claude for iOS is renamed or deleted by touching and holding it in the chat list, and the open conversation is deleted from the "⋯" button at the top right. [del]
- **WRK-083** `documented` On consumer plans, the open conversation in Claude for Android is renamed or deleted from the "⋮" menu at the top right, and several conversations are deleted from the chat list with the checklist icon. [del]
- **WRK-084** `documented` The help-center article on renaming and deleting conversations covers the consumer plans; for commercial customers, the Privacy Center describes renaming or deleting a conversation by clicking its name at the top of the screen, and deleting several from Recents > "View all" with "Delete Selected". [del] [del-org]
- **WRK-085** `documented` On consumer plans, deleting a conversation leaves the account's other data, such as projects and account information, in place until the user deletes it or deletes the account. [del]
- **WRK-086** `documented` A Cowork task is deleted with "Delete" from the "⋮" next to it, or by selecting tasks in the task list and clicking the trash icon, and it disappears from the task history at once. [cw-start]
- **WRK-087** `documented` Deleting a session also deletes the copies of local files that Claude fetched for it, in line with Anthropic's data retention practices. [cw-web]
- **WRK-088** `documented` In Claude Desktop, the command palette (Cmd+K on a Mac, Ctrl+K under Windows or Linux) can archive or delete whatever is open at the moment, be it a chat, a task, a project or a coding session. [rn-desk]

## Sharing chats

- **WRK-100** `documented` Chats are private by default; sharing a chat gives others a view-only snapshot of it. [share] [share-people] [share-link]
- **WRK-101** `documented` The snapshot contains all messages sent before the chat was shared, including artifacts; messages sent afterwards stay private until the user updates the snapshot. [share] [share-people] [share-link]
- **WRK-102** `documented` "Update shared chat" in the share dialog puts the current state of the chat in place of the earlier snapshot for all who have access; the project sharing article for Team and Enterprise calls the control "Update" and places it beside the note "New messages since last shared", and the share-and-unshare article describes unsharing the chat and sharing it again as the way to include new messages. [share-people] [vis] [share]
- **WRK-103** `documented` People invited to a shared chat can only view it: replying, carrying the conversation on, saving a copy to their own account and downloading its files are all ruled out; a public link is view-only as well, and its viewers cannot continue the chat. [share-people] [share-link]
- **WRK-104** `documented` Raw data returned by connectors or MCP tool calls is not shown in a shared chat; viewers see the conversation and Claude's final responses. [share] [share-people]
- **WRK-105** `documented` By default, a chat is shared by email invitation to chosen people; every plan, from Free to Enterprise, has this kind of sharing, but it starts from the claude.ai website, since the mobile app does not offer it yet, whereas the recipient of a shared chat can open it on any device. [share-people]
- **WRK-106** `documented` People are invited from the chat's "Share" button, under "People with access"; each gets an email with the sharer's name, the chat title and a link that opens only for the invited address, so a forwarded invitation opens for no one else. [share-people]
- **WRK-107** `documented` The sharer's name is visible to the people invited; someone invited who has no Claude account yet signs up under the invited address, and viewing the chat requires no paid plan. [share-people]
- **WRK-108** `documented` An invitation shows as pending until it is opened, can be removed at any time and expires after 30 days if it is not opened; the number of people a user can invite in a day is limited. [share-people]
- **WRK-109** `documented` A person is removed under "People with access" in the share dialog, and "Turn off" there stops sharing the chat altogether, after which the link stops working for everyone at once. [share-people]
- **WRK-110** `documented` A public link opens the snapshot to everybody who holds it, with or without a Claude account, and its audience cannot be narrowed to particular people. [share-link]
- **WRK-111** `documented` Public links exist on the plans Free, Pro and Max, and not on Team or Enterprise. [share-link] [share] [share-people]
- **WRK-112** `documented` A public link is turned off in the "Share" menu, by setting the chat to Private; the link then stops working at once, but copies, screenshots and archives that others already made are not removed. [share-link] [share]
- **WRK-113** `documented` To keep shared chats out of search results, each of their pages tells search engines "noindex"; in addition, no sitemap or directory of shared chats is published, and a link consists of a long random string. [share-link]
- **WRK-114** `documented` The public links article says Anthropic cannot control where a link is posted, copies made by viewers or third-party services, or crawlers that ignore "noindex", and advises treating a public link as public. [share-link]
- **WRK-115** `documented` Settings > Privacy > Shared chats lists the chats a user has shared, each with its date, and lets the user stop sharing each one; the share-and-unshare article describes this list for Free, Pro and Max. [share] [share-people]
- **WRK-116** `documented` Files attached to a chat are not included in a public link. [share-link] [share]
- **WRK-117** `conflicting` Whether files attached to a chat are visible when the chat is shared inside an organization: the share-and-unshare article, which also covers Team and Enterprise, says an attached file is not part of the snapshot and stays private, while the article on sharing with specific people says invited people do not see attached files unless the chat was shared within the sharer's organization. [share] [share-people]
- **WRK-118** `documented` On Team and Enterprise, sharing stays inside the organization: only email addresses on the organization's domain can be invited, and a General access option lets any signed-in member of the organization who has the link view the chat. [share-people] [share-link] [share]
- **WRK-119** `documented` A coworker who is invited without having a Claude seat is asked to sign in and, depending on how the organization is set up, either gets access automatically or is told to ask their admin. [share-people]
- **WRK-120** `documented` A Team or Enterprise organization's admins have the means to disable chat sharing for all members, and they can look at the chats that are shared and withdraw the sharing. [share-people]
- **WRK-121** `conflicting` Whether a Team organization has an audit log of chat sharing: the article on sharing with specific people says that on Team and Enterprise the audit log lets admins follow sharing activity, while the audit logs article restricts audit logs to Enterprise organizations. [share-people] [audit]
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

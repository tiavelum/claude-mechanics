# 04 Projects

Prefix: PRJ · Scope: projects in the Claude app (structure, knowledge, moving chats, sharing, Cowork projects, redesigned projects) · Last checked: 2026-10-07

## Structure

- **PRJ-001** `documented` A project is a self-contained workspace with its own chat history and knowledge base. [what-proj]
- **PRJ-002** `documented` Projects are available on all plans; Free users can create at most five. [proj]
- **PRJ-003** `documented` A project has a name and a description, which Claude does not have access to. [proj]
- **PRJ-095** `observed` Contrary to [proj], which gives Claude no access to a project's description, a Claude Code cloud session attached to a claude.ai project had the project's description in its context. (session 2026-10-07, Claude Code cloud session, in a project)
- **PRJ-004** `documented` In the merged experience, a project holds files, instructions and context for related work in one place and can be used from any conversation. [one]
- **PRJ-009** `documented` Projects can be used on web, desktop and mobile alike; a chat or a Cowork session can be started from a project, and Claude then draws on the project's knowledge. [cw-web]

## Cowork projects

- **PRJ-005** `documented` A Cowork project has its own instructions, scheduled tasks, context (local folder, linked chat project or URL) and memory. [cw-proj]
- **PRJ-006** `conflicting` Where Cowork projects are kept: the Cowork projects article says new ones are saved to the Claude account and can be opened on other devices, while ones created from a folder on the computer stay on it, and the Team and Enterprise article says projects of cloud sessions are saved with the account and those of local sessions on the computer; the Cowork guide says projects live on the computer and are not synced to the cloud. [cw-proj] [cw-org] [cw-guide]
- **PRJ-010** `conflicting` Whether Cowork projects are the same as projects in Claude: the Cowork projects article says projects behave identically in Cowork and in Claude, while the Cowork guide says a Cowork project is a separate object from a claude.ai project, stored separately and with different capabilities. [cw-proj] [cw-guide]
- **PRJ-007** `documented` Importing a chat project into Cowork transfers its files and instructions; one chat project is imported at a time. [cw-proj]
- **PRJ-013** `documented` A chat project can be linked into a Cowork project so that the Cowork project's sessions draw on its knowledge; the link does not merge the two, and the chat project stays where it is. [cw-guide] [cw-proj]
- **PRJ-011** `documented` A project bound to a folder on the computer can run Cowork sessions only on desktop; Cowork does not change a project's contents, so the user adds anything to keep to the project. [cw-web] [cw-org]
- **PRJ-012** `documented` On Team and Enterprise there are no separate admin controls for Cowork projects, so owners currently cannot restrict project creation for the organization. [cw-org]
- **PRJ-008** `documented` Cowork projects are not available in Claude Code; the separate redesigned projects (beta, section below) are offered to Claude Code users. [cw-proj] [what-proj]

## What chats in a project share

- **PRJ-020** `documented` Project instructions and project knowledge are used in all chats of the project. [proj]
- **PRJ-021** `conflicting` Whether chats in a project share context: the projects article notes that context is not shared across a project's chats unless it is added to project knowledge, while the same article and the memory article give each project a memory of its own, and the memory article a chat search over the project's conversations. [proj] [mem]
- **PRJ-022** `documented` Chats in a project contribute to and draw on the project's own memory, separate from account memory. [mem] [proj]
- **PRJ-023** `documented` Chat search inside a project covers only that project's chats. [mem]
- **PRJ-024** `inferred` Files uploaded to a single chat in a project are not added to project knowledge and stay available only in that chat. Basis: PRJ-037, PRJ-030.

## Project knowledge and retrieval

- **PRJ-030** `documented` Documents, text and code added to project knowledge are used as context in every chat of the project. [proj]
- **PRJ-037** `documented` Files are uploaded either to a single chat or to a project's files, where they are kept for reference across the project's conversations. [up]
- **PRJ-031** `documented` On paid plans, Claude switches a project to RAG mode automatically once its knowledge nears the limit of the context window. [rag] [proj]
- **PRJ-032** `documented` RAG mode expands a project's capacity by up to 10 times. [rag]
- **PRJ-033** `documented` In RAG mode, Claude uses a project knowledge search tool and pulls in only the relevant parts instead of loading all knowledge. [rag]
- **PRJ-034** `documented` RAG mode needs no setup and is shown by an indicator in the project. [rag]
- **PRJ-038** `documented` The user does not control when RAG mode is used: it follows the size of project knowledge, projects use in-context processing where possible, and Claude can switch a project back when its knowledge drops below the context window threshold. [rag]
- **PRJ-035** `conflicting` Project capacity: the upload article says the total content of project files must fit within the context window, while the RAG article says paid plans extend capacity beyond it by up to 10 times and describes the context-window limit as the earlier rule. [up] [rag]
- **PRJ-036** `documented` Reused project content is cached and counts less against usage limits; the cache expires after inactivity. [usage]
- **PRJ-039** `documented` A GitHub repository can be added to project knowledge; only file names and contents on one branch are synced, not commit history, pull requests or other metadata. [gh]
- **PRJ-091** `documented` In a project, a repository is added from the "+" button of the project knowledge section with "GitHub": the user searches the repositories they can reach or pastes a repository URL, then picks files and folders in a file browser. [gh]
- **PRJ-025** `documented` "Sync now" fetches a repository's latest changes and updates all files and folders previously selected for the project. [gh]
- **PRJ-026** `documented` Files from Google Drive can be added to project knowledge only in private projects; the option is disabled in shared projects. [gws]
- **PRJ-027** `documented` Google Docs added to a project sync from Google Drive, so Claude works with their latest version. [gws]

## Moving chats

- **PRJ-040** `documented` A standalone chat is moved into a project with "Add to project" from the menu next to the chat name. [proj]
- **PRJ-041** `documented` A chat can be removed from a project or moved between projects from the same menu. [proj]
- **PRJ-042** `documented` For Team and Enterprise plans that use memory, the projects article presents moving chats into and out of projects as a way to manage what memory includes. [proj]
- **PRJ-043** `inferred` After a move, the chat uses the new project's instructions and knowledge from its next message on. Basis: PRJ-020; no page describes the moment of a move.
- **PRJ-044** `documented` Under an Enterprise plan's custom data retention, moving a chat into a project puts it under the project's retention period, which by default keeps projects indefinitely, and moving it out makes it a standalone chat under the chat retention period again. [ret]
- **PRJ-045** `documented` A thread of a redesigned project belongs to the project that started it and cannot be moved or copied to another project or out of it; two projects cannot be merged. [cc-proj]
- **PRJ-046** `documented` A cloud session can become a new redesigned project ("Continue as project") or hand its work to an existing one ("Move to project"); the original session stays in the session list, and a session started on the user's own machine has neither option. [cc-proj]

## Sharing (Team and Enterprise)

- **PRJ-050** `documented` On Team and Enterprise, a project can be kept private or shared with the organization, unless an admin has turned sharing off. [proj]
- **PRJ-092** `documented` Every member of the organization can find a public project on the Organization tab of the Projects page and start chats in it; whoever created a project can switch it between public and private at any time. [vis]
- **PRJ-093** `documented` The Projects page has three tabs: "Your projects" for the projects the user created, "Organization" for projects other members shared with the whole organization, and "Shared with you". [proj] [vis]
- **PRJ-051** `documented` "Can view" members see contents, knowledge and instructions and can chat in the project; "Can edit" members can also change instructions, knowledge and member settings. [proj]
- **PRJ-052** `documented` Chats inside a shared or public project stay private to the person who had them unless that person shares them. [vis]
- **PRJ-056** `documented` On Enterprise plans, a project can be shared with a group (beta); access then tracks group membership, so people added to the group later gain access and people who leave it lose access. [vis]
- **PRJ-057** `documented` Owners and Primary Owners on Team and Enterprise, and on Enterprise also custom roles whose Privacy permission is set to "Can manage", control the organization settings "Share projects" and its sub-setting "Public projects", both on by default; on Enterprise, sharing can also be set per role. [share-org]
- **PRJ-058** `documented` When project sharing is turned off, projects already shared stay shared and their users keep access, but public projects turn private, so anyone whose access came only from a project being public loses it, and no new users or groups can be added. [share-org] [vis]
- **PRJ-053** `conflicting` Whether Cowork projects can be shared: the Cowork projects article says they are shared the same way as projects in Claude, with "Can view" or "Can edit" access on Team and Enterprise, while the Cowork guide says Cowork projects are not shared with other people. [cw-proj] [cw-guide]
- **PRJ-059** `documented` A redesigned project belongs to one user: neither the project nor its threads can be shared, and the beta offers no organization-level controls for projects. [cc-proj]
- **PRJ-054** `documented` Archiving a project keeps its members, permission levels and knowledge, and unarchiving restores everything as it was. [proj] [vis]
- **PRJ-055** `inferred` No page states whether collaborators in a shared project share its project memory. Basis: MEM-050, PRJ-052.

## Archive and delete

- **PRJ-060** `documented` Archived projects stay accessible, including their conversations, and are listed separately. [proj]
- **PRJ-061** `documented` An archived project must be unarchived before it can be deleted. [proj]
- **PRJ-062** `conflicting` What archiving a Cowork project does: the Cowork projects article says its metadata is removed from the interface but not from the computer, while the Cowork guide says archiving deletes its metadata, including its name, instructions, links and memory; both say files and folders on the computer are not touched. [cw-proj] [cw-guide]
- **PRJ-063** `documented` Archiving a redesigned project hides it from the sidebar and archives its threads, stopping any that were running, and its routines do not run while it is archived; after the project is unarchived, its threads stay archived until each is unarchived. [cc-proj]
- **PRJ-064** `documented` Deleting a redesigned project permanently removes it with its threads, memory and files and turns off its routines; branches and pull requests its threads pushed to GitHub are not affected. [cc-proj]

## Redesigned projects (beta)

- **PRJ-070** `documented` A redesigned version of projects is one conversation in which Claude splits work into threads that run in parallel in the cloud. [what-proj] [blog-proj]
- **PRJ-071** `documented` The redesign is in beta for select Pro and Max subscribers, starting with accounts that have used cloud sessions in Claude Code and have no existing projects in chat or Cowork; chat, Cowork, Team and Enterprise follow later. [what-proj] [blog-proj] [cc-proj]
- **PRJ-072** `documented` Existing chat and Cowork projects keep working as before, and Pro and Max projects will be upgraded as the rollout expands. [what-proj]
- **PRJ-088** `documented` Redesigned projects can be used in the Claude mobile app, in the desktop app and at claude.ai/code; the terminal CLI, the VS Code extension and the JetBrains plugin do not offer them, and neither do Microsoft Foundry, Amazon Bedrock or Google Cloud's Agent Platform. [cc-proj]
- **PRJ-078** `documented` In the redesign, the project conversation is one long-running session in which Claude coordinates the work: it decides what becomes a thread and sees what threads report back, not each step they take. [cc-proj]
- **PRJ-079** `documented` In the redesign, each thread is its own session with a separate context window; it handles one piece of work and reports back, and a cloud thread works on a branch of its own and opens a pull request where the work needs one. [cc-proj] [blog-proj]
- **PRJ-073** `documented` In the redesign, each cloud thread starts in the project's cloud environment with the project's repositories and files, its instructions and memory, the CLAUDE.md and skills of each project repository and the connectors of the claude.ai account; a thread on the user's own computer starts with the instructions but not with the memory files. [cc-proj] [what-proj]
- **PRJ-080** `documented` In the redesign, a thread can run on the user's own computer through Remote Control instead of in the cloud; it then uses that machine's files, tools, MCP servers and Claude Code settings instead of the project's cloud environment. [cc-proj]
- **PRJ-081** `documented` In the redesign, cloud threads keep running after the laptop is closed, while a thread on the user's computer runs only while that computer is awake. [cc-proj] [what-proj]
- **PRJ-082** `documented` Cloud threads take nothing from the Claude Code setup on the user's own machine: skills reach them through the project's repositories or the claude.ai account, plugins through Project settings > Plugins, and MCP tools through the account's connectors and, in a project with one repository, its `.mcp.json`. [cc-proj]
- **PRJ-083** `documented` The project conversation itself has no connectors, so work that needs one runs in a cloud thread. [cc-proj]
- **PRJ-084** `documented` Every cloud thread can read the project's files and folders under `/mnt/project-files`. [cc-proj]
- **PRJ-074** `documented` In the redesign, a Library holds the files the user adds and the files Claude produces. [what-proj]
- **PRJ-075** `documented` In the redesign, project instructions, set in Project settings > Memory > Project instructions and up to 16,000 characters long, are given to Claude in the project conversation and to every new thread; changes reach new threads, not threads already running. [cc-proj]
- **PRJ-076** `documented` In the redesign, the user does not manage context windows: threads compact automatically, and the project conversation relies on project memory, its recent messages and its recent threads instead of its whole history; the documentation advises putting anything that must never be lost into project memory. [cc-proj]
- **PRJ-085** `documented` A new redesigned project runs Opus for threads and for the project conversation, at high effort for threads and low effort for the conversation; both are set in Project settings > General. [cc-proj]
- **PRJ-086** `documented` Scheduled work asked for in a redesigned project becomes a routine that runs as threads of that project. [cc-proj]
- **PRJ-087** `documented` A cloud thread's sandbox pauses between turns; if it cannot be resumed, the thread goes on from a fresh clone, and uncommitted changes can be lost. [cc-proj]
- **PRJ-077** `documented` Running several threads in parallel uses plan usage faster. [what-proj]
- **PRJ-089** `documented` Redesigned projects count against the same plan limits as other Claude Code sessions; a thread that reaches a limit waits and resumes by itself once the limit resets, except a thread started by a routine, whose turn stops with a limit error. [cc-proj]
- **PRJ-090** `documented` Redesigned projects are limited to 200 new threads per day across a user's projects; a limit on parallel threads that the user asks for is a preference Claude keeps, not an enforced cap. [cc-proj]
- **PRJ-094** `documented` According to the Claude Code documentation, projects in chat and Cowork, the earlier version, hold conversations and reference files together but have neither threads nor a coordinating conversation. [cc-proj]

## Sources

[blog-proj]: https://claude.com/resources/articles/projects-redesigned
[cc-proj]: https://code.claude.com/docs/en/claude-projects
[cw-guide]: https://claude.com/docs/cowork/guide/projects
[cw-org]: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
[cw-proj]: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
[cw-web]: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
[gh]: https://support.claude.com/en/articles/10167454-use-the-github-integration
[gws]: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[rag]: https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
[ret]: https://privacy.claude.com/en/articles/10440198-configure-custom-data-retention-controls-for-enterprise-plans
[share-org]: https://support.claude.com/en/articles/9927533-control-project-sharing-for-your-organization
[up]: https://support.claude.com/en/articles/8241126-upload-files-to-claude
[usage]: https://support.claude.com/en/articles/9797557-usage-limit-best-practices
[vis]: https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing
[what-proj]: https://support.claude.com/en/articles/9517075-what-are-projects

# 04 Projects

Prefix: PRJ · Scope: projects in the Claude app (structure, knowledge, moving chats, sharing, Cowork projects, redesigned projects) · Last checked: 2026-10-05

## Structure

- **PRJ-001** `documented` A project is a self-contained workspace with its own chat history and knowledge base. [what-proj]
- **PRJ-002** `documented` Projects are available on all plans; Free users can create at most five. [proj]
- **PRJ-003** `documented` A project has a name and a description, which Claude does not have access to. [proj]
- **PRJ-004** `documented` Projects keep files, instructions and context together and work in every conversation of the merged experience. [one]
- **PRJ-005** `documented` A Cowork project has its own instructions, scheduled tasks, context (local folder, linked chat project or URL) and memory. [cw-proj]
- **PRJ-006** `documented` New projects created in Cowork are saved to the Claude account; projects created from a folder on the user's computer stay on that computer. [cw-proj]
- **PRJ-007** `documented` Importing a chat project into Cowork transfers its files and instructions; one chat project is imported at a time. [cw-proj]
- **PRJ-008** `documented` Cowork projects are not available in Claude Code; the separate redesigned projects (beta, section below) are offered to Claude Code users. [cw-proj] [what-proj]

## What chats in a project share

- **PRJ-020** `documented` Project instructions and project knowledge are used in all chats of the project. [proj]
- **PRJ-021** `documented` Context is not shared across chats within a project unless it is added to the project knowledge base. [proj]
- **PRJ-022** `documented` Chats in a project contribute to and draw on the project's own memory, separate from account memory. [mem] [proj]
- **PRJ-023** `documented` Chat search inside a project covers only that project's chats. [mem]
- **PRJ-024** `inferred` Files uploaded to a single chat in a project are not added to project knowledge and stay available only in that chat. Basis: PRJ-021, PRJ-030.

## Project knowledge and retrieval

- **PRJ-030** `documented` Documents, text and code added to project knowledge are used as context in every chat of the project. [proj]
- **PRJ-031** `documented` On paid plans, when project knowledge approaches the context window limit, Claude switches the project to RAG mode automatically. [rag] [proj]
- **PRJ-032** `documented` RAG mode expands a project's capacity by up to 10 times. [rag]
- **PRJ-033** `documented` In RAG mode, Claude uses a project knowledge search tool and pulls in only the relevant parts instead of loading all knowledge. [rag]
- **PRJ-034** `documented` RAG mode needs no setup and is shown by an indicator in the project. [rag]
- **PRJ-035** `conflicting` The upload article says total project content must fit within the context window, while the RAG article says paid plans extend capacity beyond it by up to 10 times. [up] [rag]
- **PRJ-036** `documented` Reused project content is cached and counts less against usage limits; the cache expires after inactivity. [usage]

## Moving chats

- **PRJ-040** `documented` A standalone chat is moved into a project with "Add to project" from the menu next to the chat name. [proj]
- **PRJ-041** `documented` A chat can be removed from a project or moved between projects from the same menu. [proj]
- **PRJ-042** `documented` Moving chats into and out of projects is the documented way to control which memory a chat belongs to. [proj]
- **PRJ-043** `inferred` After a move, the chat uses the new project's instructions and knowledge from its next message on. Basis: PRJ-020; no page describes the moment of a move.

## Sharing (Team and Enterprise)

- **PRJ-050** `documented` On Team and Enterprise, a project can be kept private or shared with the organization, unless an admin has turned sharing off. [proj]
- **PRJ-051** `documented` "Can view" members see contents, knowledge and instructions and can chat in the project; "Can edit" members can also change instructions, knowledge and member settings. [proj]
- **PRJ-052** `documented` Chats inside a shared project stay private to the person who had them. [vis]
- **PRJ-053** `documented` Cowork projects are shared the same way as projects in Claude. [cw-proj]
- **PRJ-054** `documented` Archiving a project keeps its members, permission levels and knowledge, and unarchiving restores everything as it was. [proj] [vis]
- **PRJ-055** `inferred` No page states whether collaborators in a shared project share its project memory. Basis: MEM-050, PRJ-052.

## Archive and delete

- **PRJ-060** `documented` Archived projects stay accessible, including their conversations, and are listed separately. [proj]
- **PRJ-061** `documented` An archived project must be unarchived before it can be deleted. [proj]
- **PRJ-062** `documented` Archiving a Cowork project removes its metadata from the interface but does not touch files on the computer. [cw-proj]

## Redesigned projects (beta)

- **PRJ-070** `documented` A redesigned version of projects is one conversation in which Claude splits work into parallel threads that run in the cloud. [what-proj] [blog-proj]
- **PRJ-071** `documented` The redesign is in beta for select Pro and Max subscribers who use Claude Code; chat, Cowork, Team and Enterprise follow later. [what-proj] [blog-proj]
- **PRJ-072** `documented` Existing chat and Cowork projects keep working as before, and Pro and Max projects will be upgraded as the rollout expands. [what-proj]
- **PRJ-073** `documented` In the redesign, every thread starts with the project's files, repositories, instructions and memory, and threads keep running after the laptop is closed. [what-proj]
- **PRJ-074** `documented` In the redesign, a Library holds the files the user adds and the files Claude produces. [what-proj]
- **PRJ-075** `documented` In the redesign, project instructions can be up to 16,000 characters and reach new threads only, not threads already running. [cc-proj]
- **PRJ-076** `documented` In the redesign, threads compact their context automatically, and the user does not manage context windows. [cc-proj]
- **PRJ-077** `documented` Running several threads in parallel uses plan usage faster. [what-proj]

## Sources

[blog-proj]: https://claude.com/blog/projects-redesigned
[cc-proj]: https://code.claude.com/docs/en/claude-projects
[cw-proj]: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[rag]: https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
[up]: https://support.claude.com/en/articles/8241126-upload-files-to-claude
[usage]: https://support.claude.com/en/articles/9797557-usage-limit-best-practices
[vis]: https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing
[what-proj]: https://support.claude.com/en/articles/9517075-what-are-projects

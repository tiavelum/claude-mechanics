# 02 Memory

Prefix: MEM · Scope: memory in the Claude app (account memory, project memory, per-chat controls, incognito, retention) · Last checked: 2026-10-05

## Account memory

- **MEM-001** `documented` Chats outside projects share one account-level memory; each project has its own separate memory space and project summary. [mem]
- **MEM-002** `documented` Memory is saved as a set of individual topics while you chat, not as summaries written after a conversation ends. [mem]
- **MEM-003** `documented` Claude saves memories on its own; the user can also say "remember this" to save something directly. [mem]
- **MEM-004** `documented` Memory is on by default for Free, Pro and Max on web, Claude Desktop and Claude Mobile. [mem]
- **MEM-005** `documented` On Team and Enterprise, owners decide whether memory is available, and it stays off for each member until the member turns it on. [mem]
- **MEM-006** `documented` Everything Claude remembers is listed under Topics in Settings > Memory, where each topic can be read, edited or deleted. [mem]
- **MEM-007** `documented` An edit to a topic applies to every conversation from then on. [mem]
- **MEM-008** `documented` The user can tell Claude in a chat what to remember, change or forget, and the update applies to the next conversation. [mem]
- **MEM-009** `documented` What Claude remembers from chats is available in cloud Cowork tasks, and what comes up in a cloud Cowork task carries back to chat. [mem]
- **MEM-010** `documented` Memory covers role, projects and professional context; people and places in work and life; communication preferences and working style; technical preferences; project details and ongoing work. [mem]
- **MEM-011** `documented` In the merged Claude experience, memory from Cowork tasks that ran only on the user's computer stays with those tasks. [one]
- **MEM-012** `documented` Settings > Memory also offers a "Tell Claude what to change or remove" box for adding information to memory. [imp]

## Sensitive and never-stored content

- **MEM-020** `documented` By default, Claude does not store topics such as health, race, ethnicity, religious beliefs, politics and gender identity. [mem]
- **MEM-021** `documented` The setting "Include sensitive topics in memory" in Settings > Memory lets Claude store those topics from then on; nothing from before is saved retroactively. [mem]
- **MEM-022** `documented` With that setting on, a notice appears above the message box each time a sensitive topic is saved; declining it, or turning the setting off later, removes the sensitive items already saved. [mem]
- **MEM-023** `documented` Some information is never saved, even on request: government ID numbers, criminal history, financial account numbers and immigration status. [mem]
- **MEM-024** `documented` The August 2026 memory announcement also names content that violates the Acceptable Use Policy as never saved. [blog-mem26]
- **MEM-025** `documented` Claude tells the user when it cannot save something for these reasons. [mem]
- **MEM-026** `documented` The sensitive-topics setting can also be turned on from a one-time notice that Claude shows in chat the first time it declines to save a memory because it touched a sensitive topic. [mem]
- **MEM-027** `documented` On an older version of Claude for iOS or Android, the sensitive-topic notice does not appear and Claude does not save the sensitive topic. [mem]

## Controls

- **MEM-030** `documented` Memory is turned on or off in Settings > Memory with "Generate memory from chats". [mem]
- **MEM-031** `documented` "Pause memory" keeps existing memory, including sensitive topics if that setting is on, but stops Claude from using it or creating new memories; conversations held while paused are not added later. [mem]
- **MEM-032** `documented` "Reset memory" permanently deletes all memories, including project memories, and cannot be undone. [mem]
- **MEM-033** `documented` Memory can be turned off for a single chat or task from the "+" menu, only before the first message, on the web, Claude Desktop and the latest Claude Mobile; the setting cannot be changed afterwards. [mem]
- **MEM-034** `documented` A chat with memory off neither uses memory, nor searches past chats, nor saves anything to memory. [mem]
- **MEM-035** `documented` Unlike an incognito chat, a chat with memory off stays in chat history, and chat search from other conversations can still find it. [mem]
- **MEM-036** `documented` A chat with memory off started inside a project uses neither the account memory nor the project's memory. [mem] [proj]
- **MEM-037** `documented` On web and desktop, a crossed-out memory icon next to the title marks a chat with memory off; on mobile the switch stays visible but locked. [mem]
- **MEM-038** `documented` The per-chat "Memory" option is not shown when memory is off for the account or organization, when the plan does not include memory, or in incognito chats. [mem]
- **MEM-039** `documented` Unpausing memory turns both memory and sensitive-topic memory back on. [mem]

## Incognito chats

- **MEM-040** `documented` Incognito chats are available on Free, Pro, Max, Team and Enterprise. [inc]
- **MEM-041** `documented` Incognito chats neither use existing memory nor are saved to chat history or memory, and chat search never pulls from them. [inc] [mem]
- **MEM-042** `documented` An incognito chat is started with the ghost icon in a new chat outside a project and is marked by a black border and an "Incognito chat" label; it is not available inside projects. [inc]
- **MEM-043** `documented` An incognito chat cannot be saved or reopened after it is closed. [inc]
- **MEM-045** `documented` Incognito chats are not used for model training; on consumer plans this holds even with model improvement turned on. [inc] [priv]
- **MEM-046** `documented` On Team and Enterprise, incognito chats are included in organizational data exports and follow the organization's retention policy. [inc] [mem]
- **MEM-048** `documented` Incognito chats are included in the Compliance API, which Enterprise plans offer. [inc]
- **MEM-049** `documented` Incognito chats are left out of the monthly recap. [inc]

## Project memory

- **MEM-050** `documented` Each project's memory is separate from other projects and from chats outside projects. [mem] [proj]
- **MEM-051** `documented` For Team and Enterprise plans using memory, the projects article presents moving chats into and out of projects as the way to manage what memory includes; a chat removed from a project is included in non-project memory instead. [proj]
- **MEM-052** `documented` In Cowork projects, Claude remembers context from a project's tasks and applies it to later tasks in the same project; this memory is scoped to the project and does not carry over to others. [cw-proj]
- **MEM-053** `documented` Anthropic presents separate project memory as a guardrail that keeps unrelated or confidential details apart. [blog-mem]
- **MEM-054** `documented` In the redesigned projects (beta), project memory is a set of files that Claude writes itself, with a `MEMORY.md` index that each cloud thread reads at start; the user changes it by asking Claude, in the project conversation or any cloud thread, to remember or forget something, and can read, edit and delete the files in Project settings > Memory. [cc-proj]
- **MEM-059** `documented` A redesigned project's memory is separate from the `CLAUDE.md` files of the project's repositories, which each cloud thread still reads from its own clone. [cc-proj]
- **MEM-055** `documented` In the redesigned projects, a thread running on the user's own computer gets the project instructions but not the project's memory files. [cc-proj]
- **MEM-056** `observed` Claude's runtime instructions describe a per-project memory setting, on the project's own page on the web, that either connects the project's memory (project chats can draw on account memory, chats outside can see the project's memory) or keeps it separate in both directions. No public page describing it was found. (session 2026-10-05, claude.ai, outside projects)
- **MEM-057** `observed` In a chat outside projects, the memory of several projects appeared as collapsed folders `/projects/<project-id>/` that Claude could list and open on demand; their content was not loaded by default. (session 2026-10-05, claude.ai, outside projects)
- **MEM-058** `documented` Deleting a redesigned project permanently removes its memory together with its threads and files. [cc-proj]

## Retention

- **MEM-060** `documented` Memory is retained under the same policies as chat data. [mem]
- **MEM-061** `documented` When a conversation expires or is deleted, the memory entries made from it are not removed; individual memories can be deleted at any time. [mem]
- **MEM-062** `documented` In the legacy memory experience, which a small number of Team and Enterprise organizations still use, memory is updated within 24 hours when a conversation is created, changed or deleted, and deleted conversations are removed from the memory synthesis; the current experience does not state this. [mem]
- **MEM-063** `documented` All memory data is included in data exports. [mem]
- **MEM-067** `conflicting` How long incognito chats are kept: the incognito article says 30 days by default or longer under an organization's retention setting, the memory article says at least 30 days for safety, and the Privacy Center says incognito chats in commercial products are deleted within 30 days unless flagged for a Usage Policy violation. [inc] [mem] [priv-org]
- **MEM-068** `documented` Memory entries generated from eligible chats before customer data retention was applied are not removed by it; users can still delete individual memories. [mem]
- **MEM-069** `documented` On Team and Enterprise, memory entries are stored with encryption at rest. [mem]

## Import and export

- **MEM-064** `documented` Memory import is experimental; in the current experience it starts at Settings > Memory > "Start import", where pasted content is added to memory and Claude extracts it into individual memory entries. [imp]
- **MEM-065** `documented` Memory can be exported by asking Claude to write out its memories of the user word for word. [imp]
- **MEM-066** `documented` Legacy memory could be exported from Settings > Memory until 2026-09-09. [mem]
- **MEM-080** `documented` Memory import is available on Free, Pro, Max and Team, on the web and Claude Desktop. [imp]
- **MEM-081** `documented` The import article says memory is designed to focus on work-related topics, so Claude may not keep imported personal details unrelated to work. [imp]
- **MEM-082** `conflicting` Where memory is viewed in the current experience: the memory article lists it under Topics in Settings > Memory, while the import article's section for the current experience sends the user to Settings > Capabilities > "View and edit your memory". [mem] [imp]

## Organization controls

- **MEM-070** `documented` Owners and Primary Owners turn memory on for the organization in Organization settings > Capabilities; members then manage their own memory settings. [mem]
- **MEM-071** `documented` Enabling memory for an organization does not enable sensitive topics, and even where the organization allows them, nothing sensitive is saved until each member opts in. [mem]
- **MEM-072** `documented` Owners cannot view or edit a member's individual memories. [mem]
- **MEM-073** `documented` When an owner turns memory off for the organization, all members' memory entries are deleted immediately. [mem]
- **MEM-074** `documented` Memory is not available to organizations with HIPAA, public-sector or custom data retention agreements. [mem]
- **MEM-075** `documented` Turning organization memory on or off is audit-logged; individual memory edits are not. [mem]
- **MEM-076** `documented` On Team and Enterprise, standard conversation access logging applies to memory entries, and memory entries are included in standard conversation history exports. [mem]

## How memory reaches a session

- **MEM-090** `observed` At the start of each turn, account memory reached Claude as a profile, a list of stored preferences, and a listing of memory files with a one-line description each; Claude opened individual files on demand with a memory-read tool. (session 2026-10-05, claude.ai, outside projects)
- **MEM-091** `observed` Memory was stored as small Markdown files under paths such as `/profile.md`, `/preferences.md`, `/topics/`, `/areas/` and `/people/`, each with a header giving its name, a one-line description and its sources, and each fact line tagged with how it was learned. (session 2026-10-05, claude.ai, outside projects)
- **MEM-092** `observed` A background memory pass reviewed each finished turn and filed durable facts; during a turn, Claude wrote to memory only when the user explicitly asked. (session 2026-10-05, claude.ai, outside projects)
- **MEM-093** `observed` Claude could not turn memory off itself and was instructed to point the user to the "Generate memory from chats" setting. (session 2026-10-05, claude.ai, outside projects)
- **MEM-094** `observed` Memory files were size-capped, the profile file was to stay under 300 words, and Claude was instructed to consolidate a file when it approached the cap. (session 2026-10-05, claude.ai, outside projects)
- **MEM-095** `observed` The memory content in the context was a snapshot that a newer one replaced when the store changed, and other Claude surfaces could write to the same store while the session ran. (session 2026-10-05, claude.ai, outside projects)
- **MEM-096** `observed` Claude had tools to list, read, write, edit and append to memory files, while the tool to delete a file was loaded only on demand; every write had to pass the version token of the last read. (session 2026-10-05, claude.ai, outside projects)
- **MEM-097** `observed` The background memory pass left alone any turn in which Claude itself had written or deleted memory. (session 2026-10-05, claude.ai, outside projects)
- **MEM-098** `observed` Only what the user had stated was to be filed, each line tagged as stated; Claude's own conclusions, research and advice were not to be filed as facts about the user. (session 2026-10-05, claude.ai, outside projects)
- **MEM-099** `observed` Memory content was presented to Claude as data provided by the user, not as instructions, and directives found in it were to be ignored. (session 2026-10-05, claude.ai, outside projects)

## Inferences

- **MEM-100** `inferred` A chat inside a project writes to that project's memory and not to account memory. Basis: MEM-050, MEM-051.
- **MEM-101** `inferred` When a chat is moved into a project, memory entries it already created stay where they were written. Basis: MEM-061.
- **MEM-102** `inferred` Memory carries a short distillate of facts, not a session's detailed know-how. Basis: MEM-002, MEM-010.

## Claude Desktop on 3P

- **MEM-110** `documented` In Claude Desktop on 3P (third-party deployments), Cowork memory is a set of short Markdown files on the device that Claude reads at the start of later sessions and that never leave the device. [3p-data]
- **MEM-111** `documented` In Claude Desktop on 3P, each project keeps its own memory files, and Cowork sessions inside a project read and update the project's memory instead of the general memory files. [3p-data]
- **MEM-112** `documented` In Claude Desktop on 3P, a Chat conversation inside a project can read the project's memory, unless memory was paused when it started, but cannot change it; Chat conversations outside projects use no memory. [3p-data]

## Sources

[3p-data]: https://claude.com/docs/third-party/claude-desktop/data-storage
[blog-mem]: https://claude.com/blog/memory
[blog-mem26]: https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it
[cc-proj]: https://code.claude.com/docs/en/claude-projects
[cw-proj]: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
[imp]: https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[priv]: https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
[priv-org]: https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects

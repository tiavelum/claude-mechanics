# 02 Memory

Prefix: MEM · Scope: memory in the Claude app (account memory, project memory, per-chat controls, incognito, retention) · Last checked: 2026-10-07

## Account memory

- **MEM-001** `documented` Chats outside projects share one account-level memory; every project keeps a memory space and a project summary of its own. [mem]
- **MEM-002** `documented` Memory is saved as a set of individual topics while you chat, not as summaries written after a conversation ends. [mem]
- **MEM-003** `documented` Claude saves memories on its own; the user can also say "remember this" to save something directly. [mem]
- **MEM-004** `documented` For Free, Pro and Max, memory starts switched on by default on the web, in Claude Desktop and in Claude Mobile. [mem]
- **MEM-113** `conflicting` The memory article and the release notes, which date memory for free users to 2026-03-02, make memory available on Free, while the usage article names memory and project summaries only for the paid plans: Pro, Max, Team and Enterprise. [mem] [rn] [usage]
- **MEM-005** `documented` On Team and Enterprise, owners decide whether memory is available, and it stays off for each member until the member turns it on. [mem]
- **MEM-006** `documented` Settings > Memory lists everything Claude remembers under Topics; each topic can be opened to read, edit or delete it. [mem]
- **MEM-007** `documented` An edit to a topic applies to every conversation from then on. [mem]
- **MEM-008** `documented` In a chat, the user can tell Claude what to remember, change or forget, and the next conversation reflects the update. [mem]
- **MEM-009** `documented` What Claude remembers from chats is available in cloud Cowork tasks, and what comes up in a cloud Cowork task carries back to chat. [mem]
- **MEM-010** `documented` Memory covers role, projects and professional context; people and places in work and life; how the user communicates and works; technical preferences; project details and ongoing work. [mem]
- **MEM-011** `documented` In the merged Claude experience, Cowork tasks that ran only on the user's computer keep their memory to themselves. [one]
- **MEM-012** `documented` Settings > Memory also offers a "Tell Claude what to change or remove" box for adding information to memory. [imp]
- **MEM-013** `documented` The import article says the new memory experience is available on every plan: Free, Pro, Max, Team and Enterprise. [imp]

## Sensitive and never-stored content

- **MEM-020** `documented` By default, topics such as health, race, ethnicity, religious beliefs, politics and gender identity are kept out of memory. [mem]
- **MEM-021** `documented` Turning on "Include sensitive topics in memory", found in Settings > Memory, lets Claude store those topics from then on; nothing from before is saved retroactively. [mem]
- **MEM-022** `documented` With that setting on, a notice appears above the message box each time a sensitive topic is saved; declining it, or turning the setting off later, removes the sensitive items already saved. [mem]
- **MEM-023** `documented` Even on request, Claude never saves immigration status, criminal history, government ID numbers or financial account numbers. [mem]
- **MEM-024** `documented` The August 2026 memory announcement also names content that violates the Acceptable Use Policy as never saved. [blog-mem26]
- **MEM-025** `documented` Claude tells the user when it cannot save something for these reasons. [mem]
- **MEM-026** `documented` The sensitive-topics setting can also be switched on from a notice, shown once in chat, the first time Claude refuses to save a memory because it touched a sensitive topic. [mem]
- **MEM-027** `documented` On an older version of Claude for iOS or Android, the sensitive-topic notice does not appear and Claude does not save the sensitive topic. [mem]

## Controls

- **MEM-030** `documented` Memory is turned on or off in Settings > Memory with "Generate memory from chats". [mem]
- **MEM-031** `documented` "Pause memory" keeps existing memory, including sensitive topics if that setting is on, but stops Claude from using it or creating new memories; conversations held while paused are not added later. [mem]
- **MEM-032** `documented` "Reset memory" deletes every memory, project memories included, permanently and irreversibly. [mem]
- **MEM-033** `documented` From the "+" menu, memory can be switched off for one chat or task, only before the first message, on the web, in Claude Desktop and in the latest Claude Mobile; the setting cannot be changed afterwards. [mem]
- **MEM-034** `documented` A chat with memory off neither uses memory, nor searches past chats, nor saves anything to memory. [mem]
- **MEM-035** `documented` Unlike an incognito chat, a chat with memory off stays in chat history, and chat search from other conversations can still find it. [mem]
- **MEM-036** `documented` A chat with memory off started inside a project uses neither the account memory nor the project's memory. [mem] [proj]
- **MEM-037** `documented` On web and desktop, a crossed-out memory icon next to the title marks a chat with memory off; on mobile the switch stays visible but locked. [mem]
- **MEM-038** `documented` The per-chat "Memory" option is not shown when memory is off for the account or organization, when the plan does not include memory, or in incognito chats. [mem]
- **MEM-039** `documented` Unpausing memory turns both memory and sensitive-topic memory back on. [mem]

## Incognito chats

- **MEM-040** `documented` All plans offer incognito chats: Free, Pro, Max, Team and Enterprise. [inc]
- **MEM-041** `documented` Incognito chats neither use existing memory nor are saved to chat history or memory, and chat search never pulls from them. [inc] [mem]
- **MEM-042** `documented` An incognito chat is started with the ghost icon in a new chat outside a project and is marked by a black border and an "Incognito chat" label; it is not available inside projects. [inc]
- **MEM-043** `documented` An incognito chat cannot be saved or reopened after it is closed. [inc]
- **MEM-045** `documented` Incognito chats are not used for model training; on consumer plans this holds even with model improvement turned on. [inc] [priv]
- **MEM-046** `documented` On Team and Enterprise, organizational data exports include incognito chats, which also follow the organization's retention policy. [inc] [mem]
- **MEM-048** `documented` The Compliance API, offered on Enterprise plans, covers incognito chats. [inc]
- **MEM-049** `documented` Incognito chats are left out of the monthly recap. [inc]

## Project memory

- **MEM-050** `documented` Each project's memory is separate from other projects and from chats outside projects. [mem] [proj]
- **MEM-051** `documented` For Team and Enterprise plans using memory, the projects article presents moving chats into and out of projects as the way to manage what memory includes; a chat removed from a project is included in non-project memory instead. [proj]
- **MEM-052** `documented` In Cowork projects, Claude remembers context from a project's tasks and applies it to later tasks in the same project; this memory is scoped to the project and does not carry over to others. [cw-proj]
- **MEM-053** `documented` Anthropic presents separate project memory as a guardrail that keeps unrelated or confidential details apart. [blog-mem]
- **MEM-054** `documented` In the redesigned projects (beta), project memory is a set of files that Claude writes itself, with a `MEMORY.md` index that each cloud thread reads at start; the user changes it by asking Claude to remember or forget something, either in the project conversation or in any cloud thread, and can open, edit or delete each file under Project settings > Memory. [cc-proj]
- **MEM-059** `documented` A redesigned project's memory is separate from the `CLAUDE.md` files of the project's repositories, which each cloud thread still reads from its own clone. [cc-proj]
- **MEM-055** `documented` In the redesigned projects, a thread running on the user's own computer gets the project instructions but not the project's memory files. [cc-proj]
- **MEM-056** `observed` Claude's runtime instructions describe a per-project memory setting, on the project's own page on the web, that either connects the project's memory (project chats can draw on account memory, chats outside can see the project's memory) or keeps it separate in both directions. No public page describing it was found. (session 2026-10-05, claude.ai, outside projects)
- **MEM-057** `observed` In a chat outside projects, the memory of several projects appeared as collapsed folders `/projects/<project-id>/` that Claude could list and open on demand; their content was not loaded by default. (session 2026-10-05, claude.ai, outside projects)
- **MEM-058** `documented` Deleting a redesigned project permanently removes its memory together with its threads and files. [cc-proj]

## Retention

- **MEM-060** `documented` Memory is retained under the same policies as chat data. [mem]
- **MEM-061** `documented` Memory entries made from a conversation stay when it expires or is deleted; individual memories can be deleted at any time. [mem]
- **MEM-062** `documented` In the legacy memory experience, which a few Team and Enterprise organizations keep using, memory catches up within 24 hours after a conversation is created, changed or deleted, and deleted conversations drop out of the memory synthesis; for the current experience, the article names no such delay. [mem]
- **MEM-063** `documented` Data exports contain all memory data. [mem]
- **MEM-067** `conflicting` How long incognito chats are kept: the incognito article says 30 days by default, and on Team and Enterprise 30 days for safety or longer where the organization's retention policy requires it; the memory article says Team and Enterprise incognito chats are kept at least 30 days for safety; and the Privacy Center says incognito chats in commercial products are deleted within 30 days unless flagged for a Usage Policy violation. [inc] [mem] [priv-org]
- **MEM-068** `documented` Customer data retention does not remove memory entries that eligible chats generated before it was applied; users can still delete individual memories. [mem]
- **MEM-069** `documented` On Team and Enterprise, memory entries are encrypted at rest. [mem]
- **MEM-077** `documented` For the current experience, the memory article says memory keeps up with changes to conversations as they happen. [mem]

## Import and export

- **MEM-064** `documented` Memory import is experimental; in the current experience it starts at Settings > Memory > "Start import", where pasted content is added to memory and Claude extracts it into individual memory entries. [imp]
- **MEM-065** `documented` Memory can be exported by asking Claude to write out its memories of the user word for word. [imp]
- **MEM-066** `documented` Legacy memory could be exported from Settings > Memory until 2026-09-09. [mem]
- **MEM-080** `documented` Memory import is available on Free, Pro, Max and Team, on the web and Claude Desktop. [imp]
- **MEM-081** `documented` The import article says memory is built to focus on work topics, so Claude may not keep imported personal details unrelated to work. [imp]
- **MEM-082** `conflicting` Where memory is viewed in the current experience: the memory article lists it under Topics in Settings > Memory, while the import article's section for the current experience sends the user to Settings > Capabilities > "View and edit your memory". [mem] [imp]
- **MEM-083** `documented` In the current experience, imported memory shows up shortly after the import finishes; in the legacy experience, it can take up to 24 hours. [imp]
- **MEM-084** `documented` The import article warns that Claude may not always succeed in incorporating imported memories. [imp]

## Organization controls

- **MEM-070** `documented` Owners and Primary Owners switch memory on for their organization under Organization settings > Capabilities; after that, members manage their own memory settings. [mem]
- **MEM-071** `documented` Enabling memory for an organization does not enable sensitive topics, and even where the organization allows them, nothing sensitive is saved until each member opts in. [mem]
- **MEM-072** `documented` Owners cannot view or edit a member's individual memories. [mem]
- **MEM-073** `documented` If an owner switches memory off for the organization, every member's memory entries are deleted at once. [mem]
- **MEM-074** `documented` Memory is unavailable to an organization that has a HIPAA agreement, a public-sector agreement or a custom data retention agreement. [mem]
- **MEM-075** `documented` Turning organization memory on or off is audit-logged; individual memory edits are not. [mem]
- **MEM-076** `documented` On Team and Enterprise, memory entries fall under standard conversation access logging and are part of standard conversation history exports. [mem]

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
- **MEM-102** `inferred` Memory carries a short distillate of facts, not a session's detailed know-how. Basis: MEM-002, MEM-010.

## Claude Desktop on 3P

- **MEM-110** `documented` In Claude Desktop on 3P (third-party deployments), Cowork memory is a set of short Markdown files on the device that Claude reads at the start of later sessions and that never leave the device. [3p-data]
- **MEM-111** `documented` In Claude Desktop on 3P, every project has memory files of its own, and Cowork sessions in a project read and update those instead of the general memory files. [3p-data]
- **MEM-112** `documented` In Claude Desktop on 3P, a Chat conversation within a project may read, but not change, that project's memory, except when memory was paused at its start; outside projects, Chat conversations use no memory. [3p-data]

## Sources

[3p-data]: https://claude.com/docs/third-party/claude-desktop/data-storage
[blog-mem]: https://claude.com/resources/articles/memory
[blog-mem26]: https://claude.com/resources/articles/claudes-memory-works-everywhere-and-you-decide-whats-in-it
[cc-proj]: https://code.claude.com/docs/en/claude-projects
[cw-proj]: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
[imp]: https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[priv]: https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
[priv-org]: https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[rn]: https://support.claude.com/en/articles/12138966-release-notes
[usage]: https://support.claude.com/en/articles/9797557-usage-limit-best-practices

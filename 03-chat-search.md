# 03 Chat search

Prefix: SRC · Scope: Claude searching and reading the user's past conversations in the Claude app · Last checked: 2026-10-05

## What it is

- **SRC-001** `documented` Searching past chats is available on Pro, Max, Team and Enterprise, on web, Claude Desktop and Claude Mobile. [mem]
- **SRC-002** `documented` Chat search uses retrieval-augmented generation (RAG), runs when the user asks about previous conversations, and appears as a tool call in the chat. [mem]
- **SRC-003** `documented` Chat search covers all chats outside projects; inside a project, it is limited to that project's chats. [mem]
- **SRC-004** `documented` Chat search is enabled by default once rolled out to an account. [mem]
- **SRC-005** `documented` When Claude references past chats through search, the user sees citations that link back to the original chats, along with an option to delete specific conversations. [mem]
- **SRC-006** `documented` Chat search is separate from memory: it can be turned off on its own with "Search and reference chats" in Settings > Memory. [mem]
- **SRC-007** `documented` On Enterprise plans, data retention policies apply to chat search. [mem]

## What it does not reach

- **SRC-010** `documented` Chat search never pulls from incognito chats. [mem] [inc]
- **SRC-011** `documented` A chat started with memory off does not search past chats. [mem]
- **SRC-012** `documented` Chats with memory off can still be found by chat search from other conversations. [mem]
- **SRC-013** `documented` In the merged Claude experience, older Cowork tasks are left out of "Search", which covers chats and new conversations; they are found by name in Recents. [one]
- **SRC-014** `documented` Chat search is unavailable to Enterprise organizations that use customer-managed encryption keys. [mem]
- **SRC-015** `inferred` Within its search scope, an already saved chat can be kept out of chat search only by deleting it; citations offer that option. Basis: SRC-003, SRC-005, SRC-012, SRC-016.
- **SRC-016** `documented` To the question whether a specific past chat can be excluded from searches, the documentation answers with incognito chats, which are not saved to chat history, and names no way for a chat that is already saved. [mem]
- **SRC-017** `documented` In Claude Desktop on 3P (third-party deployments), Claude cannot search past chats from a Chat conversation: it has no tools for listing or reading other sessions' transcripts, and conversation content is not indexed. [3p-data]

## How it behaves in a session

- **SRC-020** `observed` Claude had three tools for past chats: a keyword search, a list of recent chats by time window, and a reader that opens one chat at a search hit. (session 2026-10-05, claude.ai, outside projects)
- **SRC-021** `observed` The search matched text, so it worked with content words that appeared in the original chat rather than descriptions of the conversation. (session 2026-10-05, claude.ai, outside projects)
- **SRC-022** `observed` Claude was told its search scope at session start; in a chat outside projects, only chats outside any project were searchable. (session 2026-10-05, claude.ai, outside projects)
- **SRC-023** `observed` Search results were snippets, some machine-written summaries of a chat, which Claude was instructed to treat as data and not to promote its own past suggestions into the user's decisions. (session 2026-10-05, claude.ai, outside projects)
- **SRC-024** `inferred` Unlike memory, chat search gives access to a past session's detailed content, but only when Claude thinks to look for it. Basis: SRC-002, SRC-025, MEM-102.
- **SRC-025** `observed` Claude's runtime instructions told it to search past chats not only on a direct request but whenever the user's wording assumes shared history, such as a possessive or a definite article without context or a past-tense reference to an earlier exchange, and to answer without searching when a message carries no such cue. (session 2026-10-06, claude.ai, outside projects)

## Sources

[3p-data]: https://claude.com/docs/third-party/claude-desktop/data-storage
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude

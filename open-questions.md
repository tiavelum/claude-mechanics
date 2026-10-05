# Open questions

Prefix: OQ · Scope: points that neither documentation nor observation settles yet, each with a way to settle it · Last checked: 2026-10-05

When a question is settled, turn the answer into a statement in the right chapter and delete the question.

- **OQ-001** Does a chat inside a project ever write to account memory, for example a durable fact about the user or an explicit "remember this"? Test: in a project set to separate, state a distinctive fact (for example a planned trip), then check Settings > Memory and ask a fresh chat outside projects. Related: MEM-100.
- **OQ-002** What is the default of the per-project memory setting (connected or separate) for a new project, and where exactly is it on the project page? Test: create a project on the web and inspect its settings. Related: MEM-056.
- **OQ-003** When a chat moves into a project, do its existing account-memory entries stay, move or get removed? Test: create an entry in a chat outside projects, move the chat, compare Topics before and after. Related: MEM-101.
- **OQ-004** Which wins when account instructions, project instructions, a style and memory conflict? Test: set contradictory formatting rules on each layer and observe. Related: INS-010.
- **OQ-005** Does a chat moved into a project use the project's instructions and knowledge from its next message? Test: move a chat into a project with a distinctive instruction and check the next reply. Related: PRJ-043.
- **OQ-007** What is the real limit of project knowledge on paid plans: the context window or up to 10 times more with RAG? Related: PRJ-035.
- **OQ-008** Do collaborators in a shared project share its project memory? Related: PRJ-055.
- **OQ-009** In the merged experience, does automatic context management of long chats still depend on code execution being enabled? Related: CTX-011.
- **OQ-010** Does Claude Code read anything from the Claude app's memory when signed in to a claude.ai account? Related: CC-114.
- **OQ-011** Is incognito available on mobile and desktop as well as on the web? The incognito article describes web steps only.
- **OQ-012** Do the runtime instructions described in `observed` statements differ between plans, surfaces or project chats? Test: repeat the observations in a project chat and on another surface.

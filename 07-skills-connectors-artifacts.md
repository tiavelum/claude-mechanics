# 07 Skills, connectors and artifacts

Prefix: EXT · Scope: extensions that persist beyond a single session in the Claude app, and how they enter context · Last checked: 2026-10-05

## Skills

- **EXT-001** `documented` Skills are folders of instructions, scripts and resources that Claude loads dynamically for specialized tasks. [skills]
- **EXT-002** `documented` Skills load in stages: Claude first sees each skill's name and description, reads its `SKILL.md` when a request matches, and opens further files only when needed. [skills-doc]
- **EXT-003** `documented` A skill's description is the only part Claude sees before deciding whether to use it. [skills-doc]
- **EXT-004** `documented` Skills require "Code execution and file creation" to be enabled (on Team and Enterprise: "Cloud code execution and file creation"). [use-skills]
- **EXT-005** `documented` Custom skills are uploaded as a ZIP file. [use-skills]
- **EXT-006** `documented` Organization owners can provision skills that appear for all members; shared skills are view-only and update automatically for recipients. [use-skills]
- **EXT-007** `documented` Skills, connectors and plugins are saved to the account and available in chat on web, desktop and mobile; those added from the Claude Code command line stay on that machine. [ext]

## Connectors

- **EXT-010** `documented` Connected connectors are available across conversations on web, desktop and mobile; a per-conversation toggle in the "+" menu decides whether Claude can use each one. [conn]
- **EXT-011** `documented` Turning a connector off in a conversation leaves it connected to the account. [conn]
- **EXT-012** `documented` Each connector tool can be set to always allow, need approval, or be blocked. [conn]
- **EXT-013** `documented` On Team and Enterprise, an owner adds connectors for the organization and each member signs in with their own account. [conn]
- **EXT-014** `documented` Remote MCP servers used as custom connectors must be reachable from Anthropic's cloud. [custom-conn]

## Artifacts

- **EXT-020** `documented` Artifacts the user creates are collected in an Artifacts section reachable from any conversation. [art]
- **EXT-021** `documented` Artifacts can store data between sessions, per user or shared. [art]
- **EXT-022** `documented` Unpublishing an artifact permanently deletes its stored data. [pub]
- **EXT-023** `observed` A published artifact was a hosted page with its own URL, private to the owner until shared, and could be updated in place from a later session by its URL. (session 2026-10-05, claude.ai, outside projects)
- **EXT-024** `inferred` Artifacts and connected documents are a way to carry exact content across sessions, unlike memory, which keeps only a distillate. Basis: EXT-021, MEM-102.

## Sources

[art]: https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them
[conn]: https://claude.com/docs/connectors/getting-started
[custom-conn]: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
[ext]: https://claude.com/docs/extend/overview
[pub]: https://support.claude.com/en/articles/9547008-publish-and-share-artifacts
[skills]: https://support.claude.com/en/articles/12512176-what-are-skills
[skills-doc]: https://claude.com/docs/skills/overview
[use-skills]: https://support.claude.com/en/articles/12512180-use-skills-in-claude

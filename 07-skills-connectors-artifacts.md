# 07 Skills, connectors and artifacts

Prefix: EXT · Scope: extensions that persist beyond a single session in the Claude app, and how they enter context · Last checked: 2026-10-06

## Skills

- **EXT-001** `documented` Skills are folders of instructions, scripts and resources that Claude loads dynamically for specialized tasks. [skills]
- **EXT-002** `documented` Skills load in stages: Claude first sees each skill's name and description, reads its `SKILL.md` when a request matches, and opens further files only when needed. [skills-doc]
- **EXT-003** `documented` A skill's description is the only part Claude sees before deciding whether to use it. [skills-doc]
- **EXT-035** `documented` Claude loads a skill that is turned on when the task matches its description, and the user can pick a skill directly by typing / in the message box. [skills-doc]
- **EXT-004** `documented` Skills need code execution: on Free, Pro and Max the user turns on "Code execution and file creation" in Settings > Capabilities, on Team and Enterprise an owner turns on both "Cloud code execution and file creation" and "Skills", and with code execution off no skills are available. [use-skills] [skills-org]
- **EXT-008** `conflicting` The help center's skills articles make skills available on Free, Pro, Max, Team and Enterprise, while the skills overview in the Claude documentation lists only Pro, Max, Team and Enterprise. [skills] [use-skills] [skills-doc]
- **EXT-009** `conflicting` For Team and Enterprise, the help center's skills articles place the code execution and Skills switches in Organization settings > Plugins & skills, on the Policy tab, while the skills overview and the file creation article place code execution in Organization settings > Capabilities. [use-skills] [skills-org] [skills-doc] [files]
- **EXT-030** `documented` On Team plans, skills are on by default at the organization level. [use-skills]
- **EXT-031** `documented` Anthropic provides built-in skills for Excel, Word, PowerPoint and PDF files, which Claude uses on its own when they are relevant and code execution and file creation is on. [skills] [use-skills]
- **EXT-005** `documented` Custom skills are uploaded as a ZIP file under Customize > Skills, where each skill can be turned on or off. [use-skills]
- **EXT-034** `documented` Customize > Skills lists all of a user's skills, including those that came with a plugin; a plugin's skills turn on and off with the plugin. [skills-doc]
- **EXT-032** `documented` A custom skill a user uploads is not visible to colleagues until it is shared; admins can see its name and sharing status, but not its files. [use-skills]
- **EXT-006** `documented` On Team and Enterprise, an owner can provision skills to everyone in the organization: they appear in every member's skills list, start on unless the owner sets them to start off, and a member can turn one off but not delete it. [skills] [skills-org]
- **EXT-033** `documented` On Team and Enterprise, where the organization allows sharing, a user can share a skill they created with specific colleagues, and on Enterprise with a group; a shared skill is view-only, stays off until the recipient turns it on, and gives the recipient the owner's updated version at the next use. [use-skills] [skills-org]
- **EXT-036** `documented` Skills enabled in the Claude settings are also available in the Claude add-ins for Excel, PowerPoint, Word and Outlook. [use-skills]
- **EXT-007** `documented` Skills, connectors and plugins are saved to the account and available in chat on web, desktop and mobile; those added from the Claude Code command line stay on that machine. [ext]
- **EXT-037** `observed` In a cloud session, Anthropic's built-in skills were on a read-only file system, while the account's own, organization and plugin skills were in a writable synced folder; the session's instructions said a skill is created or changed through a proposal card that the user saves. (session 2026-10-06, claude.ai, outside projects)

## Connectors

- **EXT-015** `documented` Connectors let Claude reach the user's apps and services, retrieve data from them and act in them, with the permissions the user has in the connected service. [conn-use]
- **EXT-016** `documented` Connectors, skills and plugins are added on the Customize page of claude.ai and the desktop app; connectors are managed under Customize > Connectors. [ext] [conn]
- **EXT-010** `documented` Connected connectors are available across conversations on web, desktop and mobile; a per-conversation toggle in the "+" menu decides whether Claude can use each one. [conn]
- **EXT-011** `documented` Turning a connector off in a conversation leaves it connected to the account. [conn]
- **EXT-012** `documented` A connector's tools can be set, per group of tools or per tool, to Always allow, Needs approval or Blocked; when Claude asks to use a tool, Allow once continues and Always allow skips the prompt for that tool from then on. [conn]
- **EXT-013** `documented` On Team and Enterprise, an owner adds a connector for the organization, which makes it available without granting access: each member signs in with their own account, unless the connector uses a shared credential such as an API key. [conn] [conn-use] [custom-conn]
- **EXT-018** `documented` On Team and Enterprise, an owner can limit a connector's actions for the whole organization through its tool permissions, and members cannot override that limit. [conn-use]
- **EXT-017** `documented` Custom connectors using remote MCP are available on Free, Pro, Max, Team and Enterprise in Claude, Cowork and Claude Desktop; a Free account can have one. [custom-conn] [conn-use]
- **EXT-014** `documented` Claude reaches a custom connector's remote MCP server from Anthropic's cloud, from every Claude client including Claude Desktop, Cowork and the mobile apps, so the server must be reachable over the public internet. [custom-conn] [conn-use]

## Plugins

- **EXT-060** `documented` A plugin bundles skills, connectors, commands and agents into one package that is installed as a unit. [plugins] [ext]
- **EXT-061** `documented` Plugins are available on the paid plans: Pro, Max, Team and Enterprise. [plugins]
- **EXT-062** `documented` Plugins can be added and used in chat on the web, in the Chat tab of Claude Desktop and in Cowork, and plugins added there are saved to the account. [plugins]
- **EXT-063** `documented` A plugin's hooks and sub-agents run in Cowork and Claude Code but not in chat, where they appear grayed out. [plugins] [ext]
- **EXT-064** `documented` On Team and Enterprise, an owner can distribute plugins across the organization through plugin marketplaces, and an organization plugin can be installed by default or required. [plugins]

## Artifacts

- **EXT-025** `documented` The help center describes an artifact as something Claude makes for the user to show others, such as a design, a deck, a document, a dashboard or a small interactive tool. [art]
- **EXT-026** `documented` Artifacts are available on Free, Pro, Max, Team and Enterprise; templates, connected apps and data storage need Pro, Max, Team or Enterprise. [art]
- **EXT-027** `documented` Artifacts need "Cloud code execution and file creation", turned on in Settings > Capabilities on Free, Pro and Max and in Organization settings > Capabilities on Team and Enterprise. [art]
- **EXT-038** `conflicting` For the switch in Settings > Capabilities on Free, Pro and Max, the artifacts article uses the name "Cloud code execution and file creation", while the skills and file creation articles and the skills overview call it "Code execution and file creation". [art] [use-skills] [files] [skills-doc]
- **EXT-020** `documented` Every artifact the user makes is saved to the Artifacts tab in the Claude sidebar, which can be reached from any conversation. [art]
- **EXT-028** `documented` Artifacts start private to the user who made them. [art] [pub]
- **EXT-029** `documented` Legacy artifacts, made in a chat before 2026-09-16, keep working and can still be published and shared, but no new ones can be made. [art]
- **EXT-050** `documented` Artifacts made in Cowork before 2026-08-19 are live artifacts, which keep working but cannot be edited in place. [art]
- **EXT-021** `documented` On Pro, Max, Team and Enterprise, on the web and Claude Desktop, artifacts can store data between sessions, either personal to each user or shared by everyone using the artifact. [art]
- **EXT-051** `documented` The data an artifact stores is limited to 20 MB per artifact and to text, with no images, files or binary data. [art]
- **EXT-022** `documented` Unpublishing a legacy artifact permanently deletes its personal and shared stored data. [art] [pub]
- **EXT-052** `documented` Everyone who opens a shared artifact needs a Claude account, except for a legacy artifact published from a chat. [pub]
- **EXT-053** `documented` On Pro and Max, an artifact is shared with "Only you" or "Anyone with the link", and specific people can be invited by email, in beta. [pub]
- **EXT-054** `documented` Viewers of a shared artifact use their own access: an artifact that pulls from connected apps uses the viewer's connections, not the creator's. [pub] [art]
- **EXT-055** `documented` Deleting an artifact removes access for everyone invited to it. [pub]
- **EXT-023** `observed` A published artifact was a hosted page with its own URL, private to the owner until shared, and could be updated in place from a later session by its URL. (session 2026-10-05, claude.ai, outside projects)
- **EXT-056** `observed` The session's instructions mapped kinds of output to artifact types, such as Slides for decks, Docs for documents and Sheets for tables, and said that the list of types varies by account and can be empty. (session 2026-10-06, claude.ai, outside projects)
- **EXT-024** `inferred` Artifacts and connected documents are a way to carry exact content across sessions, unlike memory, which keeps only a distillate. Basis: EXT-021, MEM-102.

## Sources

[art]: https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them
[conn]: https://claude.com/docs/connectors/getting-started
[conn-use]: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
[custom-conn]: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
[ext]: https://claude.com/docs/extend/overview
[files]: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
[plugins]: https://support.claude.com/en/articles/13837440-use-plugins-in-claude
[pub]: https://support.claude.com/en/articles/9547008-share-artifacts
[skills]: https://support.claude.com/en/articles/12512176-what-are-skills
[skills-doc]: https://claude.com/docs/skills/overview
[skills-org]: https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization
[use-skills]: https://support.claude.com/en/articles/12512180-use-skills-in-claude

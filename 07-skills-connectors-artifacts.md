# 07 Skills, connectors and artifacts

Prefix: EXT · Scope: extensions that persist beyond a single session in the Claude app (skills, connectors, plugins, artifacts), how they enter context, and how an organization provisions and controls them · Last checked: 2026-10-07

## Skills

- **EXT-001** `documented` A skill is a folder holding instructions, scripts and resources, which Claude loads on demand for a specialized task. [skills]
- **EXT-002** `documented` Skills load in stages: Claude first sees each skill's name and description, reads its `SKILL.md` when a request matches, and opens further files only when needed. [skills-doc]
- **EXT-003** `documented` A skill's description is the only part Claude sees before deciding whether to use it. [skills-doc]
- **EXT-076** `documented` The skills article contrasts skills with projects: a project gives background knowledge that is present from the start of every chat in it, while skills are procedures that Claude brings in only when a task needs them and that can be used anywhere in Claude. [skills]
- **EXT-035** `documented` Claude loads a skill that is turned on when the task matches its description, and the user can pick a skill directly by typing / in the message box. [skills-doc]
- **EXT-004** `documented` Skills need code execution: on Free, Pro and Max the user turns on "Code execution and file creation" in Settings > Capabilities, on Team and Enterprise an owner turns on "Skills" together with "Cloud code execution and file creation", and with code execution off no skills are available. [use-skills] [skills-org]
- **EXT-008** `conflicting` The help center's skills articles make skills available on every plan from Free to Enterprise, while the skills overview in the Claude documentation lists only Pro, Max, Team and Enterprise. [skills] [use-skills] [skills-doc]
- **EXT-009** `conflicting` For Team and Enterprise, the help center's skills articles place the code execution and Skills switches in Organization settings > Plugins & skills, on the Policy tab, while the skills overview and the file creation article place code execution in Organization settings > Capabilities. [use-skills] [skills-org] [skills-doc] [files]
- **EXT-030** `documented` On Team plans, skills are on by default at the organization level. [use-skills]
- **EXT-031** `documented` Anthropic provides built-in skills for Excel, Word, PowerPoint and PDF files, which Claude uses on its own when they are relevant and code execution and file creation is on. [skills] [use-skills]
- **EXT-005** `documented` Custom skills are uploaded as a ZIP file under Customize > Skills, where each skill can be turned on or off. [use-skills]
- **EXT-034** `documented` Customize > Skills lists all of a user's skills, including those that came with a plugin; a plugin's skills turn on and off with the plugin. [skills-doc]
- **EXT-032** `documented` A custom skill a user uploads is not visible to colleagues until it is shared; admins can see its name and sharing status, but not its files. [use-skills]
- **EXT-006** `documented` On Team and Enterprise, an owner can provision skills to everyone in the organization: they appear in every member's skills list, start on unless the owner sets them to start off, and a member can turn one off but not delete it. [skills] [skills-org]
- **EXT-033** `documented` On Team and Enterprise, where the organization allows sharing, a user can share a skill they created with specific colleagues, and on Enterprise with a group; a shared skill is view-only, stays off until the recipient turns it on, and gives the recipient the owner's updated version at the next use. [use-skills] [skills-org]
- **EXT-065** `documented` On Team and Enterprise, users can submit a skill or plugin they built to the organization library; the Publishing setting in Organization settings > Plugins & skills, on the Policy tab, is "Requires review" (an owner approves each submission and each later version), "Open" (published without review) or "Off" (no "Publish to org" button). [skills-org]
- **EXT-066** `documented` Publishing starts as "Open" on Team, or "Off" where sharing with the organization was off, and as "Off" on Enterprise, or "Open" where sharing with the organization was on; an organization that has not chosen a setting switches to "Requires review" on 2026-10-02. [skills-org]
- **EXT-070** `documented` On Team and Enterprise, members can by default create skills and upload skill files; an owner who turns off "User-created skills" on the Policy tab of Organization settings > Plugins & skills stops that, while provisioned skills and Anthropic's built-in skills remain usable. [skills-org]
- **EXT-036** `documented` Skills enabled in the Claude settings are also available in the Claude add-ins for Excel, PowerPoint, Word and Outlook. [use-skills]
- **EXT-069** `documented` Besides the Claude app, skills work in Claude Code and, as a beta, for all users of the API via its code execution tool. [skills] [use-skills]
- **EXT-007** `documented` Skills, connectors and plugins are saved to the account and available in chat on web, desktop and mobile; those added through the Claude Code CLI remain local to that machine. [ext]
- **EXT-037** `observed` In a cloud session, Anthropic's built-in skills were on a read-only file system, while the account's own, organization and plugin skills were in a writable synced folder, `~/.claude/skills/synced/`; the session's instructions said a skill is created or changed through a proposal card that the user saves. (session 2026-10-06, claude.ai, outside projects)
- **EXT-039** `documented` Cowork and cloud sessions load the skills enabled for the claude.ai account, synced at session start; synced skills are only downloaded, never uploaded, so an edit to a file under `~/.claude/skills/synced/` is not saved to the account and may be overwritten or removed by a later sync. [cc-skills]
- **EXT-095** `observed` Changes to the account's skills reached cloud sessions of the Claude app that were already running: a skill replaced in the account was replaced in a running session's skill folder, two skills uploaded about half an hour after another session started appeared in its list, and in a third session a skill removed from the account disappeared from the list while two uploaded ones appeared. (session 2026-10-07, Claude app, cloud session)

## Connectors

- **EXT-015** `documented` Connectors let Claude reach the user's apps and services, retrieve data from them and act in them, with the permissions the user has in the connected service. [conn-use]
- **EXT-016** `documented` Connectors, skills and plugins are added on the Customize page of claude.ai and the desktop app; connectors are managed under Customize > Connectors. [ext] [conn]
- **EXT-010** `documented` Connected connectors are available across conversations on web, desktop and mobile; a per-conversation toggle in the "+" menu decides whether Claude can use each one. [conn]
- **EXT-011** `documented` Turning a connector off in a conversation leaves it connected to the account. [conn]
- **EXT-012** `documented` A connector's tools can be set, per group of tools or per tool, to Always allow, Needs approval or Blocked; when Claude asks to use a tool, Allow once continues and Always allow skips the prompt for that tool from then on. [conn]
- **EXT-013** `documented` On Team and Enterprise, an owner adds a connector for the organization, which makes it available without granting access: each member signs in with their own account, unless the connector relies on a shared credential, for example an API key. [conn] [conn-use] [custom-conn]
- **EXT-071** `documented` Data that connectors transfer is encrypted. [conn-use]
- **EXT-018** `documented` On Team and Enterprise, an owner can limit a connector's actions for the whole organization through its tool permissions, and members cannot override that limit. [conn-use]
- **EXT-067** `documented` On Enterprise, a custom role sets every connector, each connector or each of its tools to Always allow, Needs approval or Blocked, for members whose role is set to "Custom"; across a member's roles the most permissive grant applies, and the organization-wide tool policy is a ceiling that no role can widen. [roles]
- **EXT-017** `documented` Custom connectors over remote MCP can be used in Claude, Cowork and Claude Desktop on every plan from Free to Enterprise; a Free account is limited to one. [custom-conn] [conn-use]
- **EXT-014** `documented` Claude reaches a custom connector's remote MCP server from the cloud that Anthropic runs, from every Claude client including Claude Desktop, Cowork and the mobile apps, so the server must be reachable over the public internet. [custom-conn] [conn-use]

## Plugins

- **EXT-060** `documented` A plugin bundles skills, connectors, commands and agents into one package that is installed as a unit. [plugins] [ext]
- **EXT-061** `documented` Plugins are available on the paid plans: Pro, Max, Team and Enterprise. [plugins]
- **EXT-062** `documented` Plugins can be added and used in chat on the web, in the Chat tab of Claude Desktop and in Cowork, and plugins added there are saved to the account. [plugins]
- **EXT-063** `documented` A plugin's hooks and sub-agents work only in Cowork and Claude Code; in chat they are shown grayed out. [plugins] [ext]
- **EXT-064** `documented` On Team and Enterprise, an owner can distribute plugins across the organization through plugin marketplaces, and an organization plugin can be installed by default or required. [plugins]
- **EXT-072** `documented` Anthropic's announcement of 2026-09-25 calls plugins the main route for third-party developers to extend Claude; a plugin can package MCP connectors, skills, or both. [blog-plugins]

## Artifacts

- **EXT-025** `documented` The help center describes an artifact as something Claude makes for the user to show others, for example a design, deck, document, dashboard or small interactive tool. [art]
- **EXT-026** `documented` Artifacts can be made on every plan from Free to Enterprise; connected apps and data storage need Pro, Max, Team or Enterprise. [art]
- **EXT-068** `conflicting` Which plans the templates Claude Design, Claude Slides and Claude Docs reach: the artifacts article puts them in beta on paid plans only, on by default on Pro, Max and Team and off on Enterprise until an owner turns each on, and the merger announcement also names them beta on paid plans, while the release notes entry of 2026-09-16 makes them available on every plan, Free included. [art] [blog-cw] [rn]
- **EXT-073** `documented` The three templates differ in output: Claude Design produces visuals and mockups, Claude Slides produces presentations, and Claude Docs produces living documents written jointly by the user, their team and Claude; all three are in beta. [one] [art]
- **EXT-027** `documented` Artifacts need "Cloud code execution and file creation", turned on in Settings > Capabilities on Free, Pro and Max and in Organization settings > Capabilities on Team and Enterprise. [art]
- **EXT-074** `documented` On Team and Enterprise, an owner turns artifacts on for the organization with the Artifacts switch in Organization settings > Artifacts, once "Cloud code execution and file creation" is on in Organization settings > Capabilities. [art-admin]
- **EXT-075** `documented` Switching Artifacts off for an organization prevents its users from sharing artifacts with the organization, but links shared before keep working. [art-admin]
- **EXT-038** `conflicting` For the switch in Settings > Capabilities on Free, Pro and Max, the artifacts article uses the name "Cloud code execution and file creation", while the skills and file creation articles and the skills overview call it "Code execution and file creation". [art] [use-skills] [files] [skills-doc]
- **EXT-020** `documented` Every artifact the user makes is kept in the Artifacts tab of the Claude sidebar, which can be reached from any conversation. [art]
- **EXT-028** `documented` Artifacts start private to the user who made them. [art] [pub]
- **EXT-029** `documented` Legacy artifacts, made in a chat before 2026-09-16, keep working and can still be published and shared, but no new ones can be made. [art]
- **EXT-050** `documented` Artifacts made in Cowork before 2026-08-19 are live artifacts, which keep working but cannot be edited in place. [art]
- **EXT-021** `documented` On Pro, Max, Team and Enterprise, artifacts on the web and in Claude Desktop can keep data from one session to the next, either personal to each user or shared by everyone using the artifact. [art]
- **EXT-051** `documented` The data an artifact stores is limited to 20 MB per artifact and to text, with no images, files or binary data. [art]
- **EXT-022** `documented` Unpublishing a legacy artifact permanently deletes its personal and shared stored data. [art] [pub]
- **EXT-052** `documented` Everyone who opens a shared artifact needs a Claude account, except for a legacy artifact published from a chat. [pub]
- **EXT-053** `documented` On Pro and Max, an artifact's access is set to "Anyone with the link" or "Only you", and specific people can be invited by email, in beta. [pub]
- **EXT-054** `documented` A shared artifact runs with each viewer's own access, so one that reads from connected apps uses the viewer's connections rather than the creator's. [pub] [art]
- **EXT-055** `documented` Deleting an artifact removes access for everyone invited to it. [pub]
- **EXT-079** `documented` On Team and Enterprise, an artifact's access is "Only people invited", "Anyone at" the organization or "Anyone with the link", the last only where an owner has turned on External sharing or allowed that artifact; Enterprise can also share with groups. [pub]
- **EXT-080** `documented` A shared artifact grants one of three access levels, Can view (open it and read comments), Commenter (also comment and download files the artifact offers) and Can edit (also make changes), though some artifact types offer only Can view and Can edit. [pub]
- **EXT-081** `documented` An artifact that connects to apps or uses Claude cannot use "Anyone with the link", and on Team and Enterprise Claude Docs artifacts cannot be shared outside the organization yet. [pub] [art-admin]
- **EXT-082** `documented` On Team and Enterprise, turning off External sharing also stops existing public links except for artifacts allowed one by one, and "Email invitations outside your organization", on by default for Team and off for Enterprise, lets members invite up to 50 outside people per artifact, whose pending invitations expire after 30 days. [art-admin] [pub]
- **EXT-083** `documented` Someone who can edit an artifact shared within the organization sends a comment thread to Claude with Send to Claude or by mentioning `@claude`; Claude replies to or resolves only threads activated that way, its replies show as from Claude via the artifact's owner, and outside invitees cannot ask Claude in a comment. [cc-art] [pub]
- **EXT-084** `documented` People who reach an artifact only through its public link neither see nor add comments, while the owner and editors keep reading and replying to existing threads. [cc-art]
- **EXT-085** `documented` Each publish of an artifact is a version, and the Share control sets which version viewers see. [cc-art]
- **EXT-086** `documented` On Team and Enterprise, artifact presence, on by default, shows who else in the organization has an artifact open; it works only while Artifacts is on. [art-admin]
- **EXT-087** `documented` An artifact can call Claude, with each person signed in to their own account and the use counted against their own plan; a new artifact asks for permission the first time it needs Claude, and for legacy artifacts the AI-powered artifacts setting in Settings > Capabilities turns this off. [art]
- **EXT-088** `documented` The first time an artifact needs a connected app, Claude lists the apps and tools it will use and asks for approval; tools turned off stay off for later use, connector tools that need approval for each action are not available to artifacts, and on Team and Enterprise an owner switches "Enable artifact connectors" for the whole organization without being able to limit which apps. [art] [art-admin]
- **EXT-089** `documented` On Enterprise, custom roles grant artifact capabilities separately: Artifacts, Design, Design systems, Docs, Slides and standalone Claude Design; members without them can still open, comment on and use artifacts shared with them. [art-admin]
- **EXT-090** `documented` Artifacts, designs, decks and docs included, count toward each user's usage limits shared with the rest of Claude and Claude Code, with no separate allowance. [art-admin]
- **EXT-091** `documented` An organization can set separate retention periods for private and shared artifacts under Organization settings > Data and privacy; publishing, sharing and deleting an artifact appear in the audit log as `claude_artifact_*` events, and the Compliance API lists artifacts, returns a version's content and deletes artifacts, while edits and comments inside a doc are not yet recorded. [cc-art] [art-admin]
- **EXT-092** `documented` Organizations with customer-managed encryption keys, Zero Data Retention or a HIPAA-ready configuration do not get the new artifacts experience of templates, design systems and email invitations and keep using live artifacts in Cowork, and artifacts are not available through third-party cloud platforms. [art-admin]
- **EXT-093** `documented` In a doc or Markdown document, highlighting text and choosing Edit with Claude limits Claude's change to that section, and editing an earlier message creates a separate version of the chat with its own artifacts. [art]
- **EXT-094** `documented` The viewer on claude.ai loads each artifact from a sandboxed `*.claudeusercontent.com` origin under a strict Content Security Policy that admits scripts only from five public CDNs and fonts only from Google Fonts, and the rendered page may be at most 16 MiB. [cc-art]
- **EXT-023** `observed` A published artifact was a hosted page with its own URL, private to the owner until shared, and could be updated in place from a later session by its URL. (session 2026-10-05, claude.ai, outside projects)
- **EXT-056** `observed` The session's instructions mapped kinds of output to artifact types, such as Slides for decks, Docs for documents and Sheets for tables, and said that the list of types varies by account and can be empty. (session 2026-10-06, claude.ai, outside projects)
- **EXT-077** `observed` The session's instructions listed artifact types beyond Slides, Docs and Sheets: Design, Whiteboard, Tasks, Design System, Motion and Watercolor, each opening in an editor of its own. (session 2026-10-08, claude.ai, in a project)
- **EXT-078** `observed` The Artifact tool's description said a published page can declare runtime capabilities, such as reading connected data, keeping state shared across viewers, knowing who is viewing, asking Claude a question and storing files people add, and can keep a small shared database that Claude reads and writes as the user. (session 2026-10-08, claude.ai, in a project)
- **EXT-024** `inferred` Artifacts and connected documents are a way to carry exact content across sessions, unlike memory, which keeps only a distillate. Basis: EXT-021, MEM-102.

## Sources

[art]: https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them
[art-admin]: https://support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans
[blog-cw]: https://claude.com/resources/articles/cowork-is-now-claude
[blog-plugins]: https://claude.com/resources/articles/build-plugins-for-claude
[cc-art]: https://code.claude.com/docs/en/artifacts
[cc-skills]: https://code.claude.com/docs/en/skills
[conn]: https://claude.com/docs/connectors/getting-started
[conn-use]: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
[custom-conn]: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
[ext]: https://claude.com/docs/extend/overview
[files]: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[plugins]: https://support.claude.com/en/articles/13837440-use-plugins-in-claude
[pub]: https://support.claude.com/en/articles/9547008-share-artifacts
[rn]: https://support.claude.com/en/articles/12138966-release-notes
[roles]: https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans
[skills]: https://support.claude.com/en/articles/12512176-what-are-skills
[skills-doc]: https://claude.com/docs/skills/overview
[skills-org]: https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization
[use-skills]: https://support.claude.com/en/articles/12512180-use-skills-in-claude

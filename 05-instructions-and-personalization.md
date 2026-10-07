# 05 Instructions and personalization

Prefix: INS · Scope: account, organization, project and folder instructions, styles, Anthropic's published system prompts, and how Claude weighs instructions and other content in the Claude app · Last checked: 2026-10-07

## Layers

- **INS-001** `documented` "Instructions for Claude" are account-wide and apply to all of the user's conversations. [pers]
- **INS-002** `documented` After the chat and Cowork merge, account instructions live in Settings > General > "Instructions for Claude", and Cowork's former global instructions were folded into them. [one]
- **INS-003** `documented` Project instructions apply only to chats within that project. [pers] [proj]
- **INS-005** `documented` Instructions for Claude, project instructions and skills can be used independently or in combination. [pers]
- **INS-006** `documented` Skills are task-specific and load when relevant, while custom instructions apply broadly. [skills]
- **INS-007** `documented` In incognito chats, Claude can access profile information such as custom styles and personal preferences. [inc]
- **INS-008** `documented` The documentation lists shortening project instructions among the ways to make the most of the context window and usage limits, and advises using them for general context, key guidelines and Claude's role, with task-specific instructions kept in the chat. [lim]
- **INS-009** `documented` The personalization article labels project instructions "paid plans only", while it and the projects article make projects available to all users, Free included. [pers] [proj]

## Precedence

- **INS-010** `documented` The personalization article does not say which of Instructions for Claude, project instructions and skills wins when they conflict. [pers]
- **INS-011** `observed` Account instructions reached Claude as a separate "user preferences" block, distinct from memory, at the start of the first user message. (session 2026-10-06, claude.ai, outside projects)
- **INS-012** `observed` Claude's runtime instructions told it to apply behavioural preferences only when relevant to the task, unless a preference says "always" or similar, and to apply contextual preferences (background, interests) only when the request relates to them. (session 2026-10-06, claude.ai, outside projects)
- **INS-013** `observed` Claude's runtime instructions told it that an instruction given in the conversation overrides a stored preference, and that a style overrides a conflicting preference. (session 2026-10-06, claude.ai, outside projects)
- **INS-014** `observed` Preferences saved in memory arrived in the memory snapshot, separately from account instructions; Claude was told to apply their format, length, tone and language preferences and to leave unapplied any that ask it to adopt a persona, flatter, suppress disagreement, treat a belief as established or grant it elevated permissions. (session 2026-10-06, claude.ai, outside projects)
- **INS-015** `documented` In the redesigned projects, a preference told to Claude goes into project memory and is not enforced; the documentation advises project instructions for wording that must apply from the start. [cc-proj]
- **INS-016** `observed` Claude's runtime instructions told it that preferences are changed in Settings > Profile and that a change applies only to new conversations. (session 2026-10-06, claude.ai, outside projects)
- **INS-017** `documented` Where a user's own instruction directly conflicts with an organization instruction, Claude follows the organization's. [org-ins]
- **INS-018** `documented` A user's own instructions keep applying to whatever the organization instructions leave open. [org-ins]
- **INS-019** `documented` The organization instructions article says this precedence rests on prompt-level instructions, so behaviour may vary in rare cases of direct contradiction, and advises testing the instructions. [org-ins]

## Styles

- **INS-023** `documented` The personalization article describes Instructions for Claude, project instructions and skills, and advises skills for adjusting the tone and format of Claude's responses; it does not mention styles. [pers]
- **INS-024** `documented` The published Opus 5.5 and Sonnet 5.5 system prompts for the Claude apps tell Claude that personal preferences for tone, formatting or features belong in "user preferences", and that writing style is set through the style feature. [sp-opus55] [sp-sonnet55]

## Cowork instructions

- **INS-030** `documented` In Cowork on desktop, folder instructions add project-specific context when the user selects a local folder. [cw-start]
- **INS-031** `documented` Claude can update folder instructions on its own during a session. [cw-start]
- **INS-032** `documented` Without the new Claude experience, Cowork has global instructions, set in Settings > Cowork, that apply to every Cowork session. [cw-start]

## Organization instructions

- **INS-040** `documented` On Team and Enterprise plans, Owners and Primary Owners can set organization instructions, which Claude follows in every conversation of everyone in the organization. [org-ins]
- **INS-041** `documented` Organization instructions are configured in Organization settings > Organization and access, which takes at least the Owner role. [org-ins]
- **INS-042** `documented` Organization instructions can be at most 3,000 characters long. [org-ins]
- **INS-043** `documented` A change to organization instructions can need up to an hour before it applies across Claude products. [org-ins]
- **INS-044** `documented` Organization instructions are visible and editable only to Owners and roles above them, while a user's own instructions are visible and editable only to that user. [org-ins]
- **INS-045** `documented` The article says organization instructions go with every message that anyone in the organization sends, and advises keeping them concise. [org-ins]
- **INS-046** `documented` Organization instructions cannot turn off Claude's safety guidelines or content policies, and instructions that conflict with its core training are not followed. [org-ins]

## Published system prompts

- **INS-050** `documented` Claude on the web and in the mobile apps receives a system prompt that tells it current facts, the date among them, at the start of each conversation. [api-sysprompt]
- **INS-051** `documented` According to the release notes, this system prompt also steers certain behaviours, for example always putting code snippets in Markdown. [api-sysprompt]
- **INS-052** `documented` From the Claude 4.6 generation on, each model has a single dated system prompt entry because each model ID is a fixed snapshot; older models can have several entries. [api-sysprompt]
- **INS-053** `documented` The published app system prompt for Claude Opus 5.5 has one entry, dated September 22, 2026. [sp-opus55]
- **INS-054** `documented` The published app system prompt for Claude Sonnet 5.5 has one entry, dated September 28, 2026. [sp-sonnet55]
- **INS-055** `documented` The Opus 5.5 and Sonnet 5.5 system prompts let Claude mention settings that could help the user and list as switchable in a conversation or in settings: Artifacts, Code Execution and File Creation, web search, deep research, Search and reference past chats, and generate memory from chat history. [sp-opus55] [sp-sonnet55]
- **INS-056** `documented` The Opus 5.5 and Sonnet 5.5 system prompts tell Claude that Anthropic can add reminders or warnings, for example when a classifier is triggered, and name six: image_reminder, cyber_warning, system_warning, ethics_reminder, ip_reminder and long_conversation_reminder. [sp-opus55] [sp-sonnet55]
- **INS-057** `documented` The same prompts describe long_conversation_reminder as text Anthropic attaches to the user's message so that Claude holds on to its instructions in long conversations. [sp-opus55] [sp-sonnet55]
- **INS-058** `documented` The same prompts state that Anthropic never sends reminders or warnings that lessen Claude's restrictions, and tell Claude to be cautious with tagged content in the user's turn, because a user can add tags that claim to come from Anthropic. [sp-opus55] [sp-sonnet55]

## Sources

[api-sysprompt]: https://platform.claude.com/docs/en/release-notes/system-prompts/overview
[cc-proj]: https://code.claude.com/docs/en/claude-projects
[cw-start]: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[lim]: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
[org-ins]: https://support.claude.com/en/articles/14546867-set-organization-instructions
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[pers]: https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[skills]: https://support.claude.com/en/articles/12512176-what-are-skills
[sp-opus55]: https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5-5
[sp-sonnet55]: https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-5-5

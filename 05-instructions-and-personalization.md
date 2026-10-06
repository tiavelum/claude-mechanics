# 05 Instructions and personalization

Prefix: INS · Scope: account, organization, project and folder instructions, styles, Anthropic's published system prompts, and how Claude weighs instructions and other content in the Claude app · Last checked: 2026-10-06

## Layers

- **INS-001** `documented` "Instructions for Claude" are account-wide and apply to all of the user's conversations. [pers]
- **INS-002** `documented` After the chat and Cowork merge, account instructions live in Settings > General > "Instructions for Claude", and Cowork's former global instructions were folded into them. [one]
- **INS-003** `documented` Project instructions apply only to chats within that project. [pers] [proj]
- **INS-004** `documented` Styles control how Claude formats and delivers its responses. [sty]
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

## Styles

- **INS-020** `documented` There are four preset styles: Normal, Concise, Formal and Explanatory. [sty]
- **INS-021** `documented` A custom style can be created by uploading writing samples or by describing the style. [sty]
- **INS-022** `documented` A style applies to new messages, edits and retries, and can be switched at any point in a conversation. [sty]
- **INS-023** `documented` The personalization article describes Instructions for Claude, project instructions and skills, and advises skills for adjusting the tone and format of Claude's responses; it does not mention styles. [pers]

## Cowork instructions

- **INS-030** `documented` In Cowork on desktop, folder instructions add project-specific context when the user selects a local folder. [cw-start]
- **INS-031** `documented` Claude can update folder instructions on its own during a session. [cw-start]
- **INS-032** `documented` Without the new Claude experience, Cowork has global instructions, set in Settings > Cowork, that apply to every Cowork session. [cw-start]

## Sources

[cc-proj]: https://code.claude.com/docs/en/claude-projects
[cw-start]: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[lim]: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[pers]: https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[skills]: https://support.claude.com/en/articles/12512176-what-are-skills
[sty]: https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles

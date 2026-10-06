# 06 Context management

Prefix: CTX · Scope: context window, long conversations, files, usage and what each plan includes in the Claude app · Last checked: 2026-10-06

## Context window

- **CTX-001** `documented` In chat on paid plans, Claude Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5 and Sonnet 5 have a context window of 1M tokens. [ctx]
- **CTX-002** `documented` In chat, Fable 5, Opus 4.8, Opus 4.7, Opus 4.6 and Sonnet 4.6 have 500K tokens; all other models have 200K. [ctx]
- **CTX-003** `documented` In Cowork, Fable 5.1, Fable 5, Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Sonnet 5.5 and Sonnet 5 have 1M tokens, while Opus 4.6, Sonnet 4.6 and Haiku 4.5 have 200K. [ctx]
- **CTX-004** `documented` In Cowork, Sonnet 5 compacts the conversation automatically at 500K tokens. [ctx]
- **CTX-005** `documented` Part of the context window is reserved for Claude's reply, which shortens the maximum conversation length. [lim]
- **CTX-006** `conflicting` Context window on the Team plan: the Team plan article lists a 200K context window among the plan's features, while the context window article covers all paid plans, Team included, and gives 1M or 500K tokens for the models in CTX-001 and CTX-002. [team] [ctx]
- **CTX-007** `documented` The pricing page lists the context window of every plan, Free included, as up to 1M tokens depending on the model. [price]

## Long conversations

- **CTX-010** `documented` For paid users with code execution enabled, Claude manages conversation context automatically by summarizing earlier messages when a conversation approaches the limit, so that most conversations can continue indefinitely. [ctx]
- **CTX-011** `documented` Code execution must be enabled for automatic context management to work. [ctx]
- **CTX-012** `documented` After summarizing, Claude can still refer to the full chat history. [ctx] [lim]
- **CTX-013** `documented` While context is managed, Claude may show that it is "organizing its thoughts". [ctx]
- **CTX-014** `documented` Conversations long enough to trigger context management use more of the plan's usage. [lim]
- **CTX-015** `documented` A very large first message can still exceed the context limit; the error suggests fewer or smaller files or a new conversation. [lim] [err]
- **CTX-018** `documented` The documentation advises starting a new conversation or using projects when a length limit is reached, and starting a new conversation when a long chat nears the usage limit. [lim]

## What enters the context

- **CTX-040** `documented` A Tool access setting in each conversation decides how connectors load: Auto, the default, lets Claude choose which to load, Always available loads all of them at the start, and On demand loads none until Claude searches for the one a request needs; the documentation advises On demand for 10 or more connectors or when conversations hit length limits. [tools] [conn-use]
- **CTX-041** `documented` With web search on, Claude can fetch a web page from a URL the user gives; a note for Free accounts says a long linked article is retrieved into the context window in full and can use a large share of the usage limit. [web]
- **CTX-016** `observed` Long tool results were saved to a file in the workspace instead of being placed in the conversation in full; the conversation got a preview of about 2 KB, and Claude read the parts it needed. (session 2026-10-06, claude.ai, outside projects)
- **CTX-017** `observed` Tool and connector definitions were partly deferred: for the deferred ones Claude saw only the names and loaded a full definition through a search tool when it needed one, while skills were listed with a one-line description each. (session 2026-10-06, claude.ai, outside projects)
- **CTX-042** `observed` At its start, besides Anthropic's instructions, the session's context held the current date, the model's name, the workspace's working directory, the user's preferences, a memory snapshot, the list of available skills and instruction blocks from connected tool servers. (session 2026-10-06, claude.ai, outside projects)
- **CTX-043** `observed` Notes from the harness reached the session inside the conversation as blocks marked as system reminders, among them the memory snapshot, the notice that the user's computer was linked and the local time at which each message was sent. (session 2026-10-06, claude.ai, outside projects)
- **CTX-044** `observed` The session was shown a counter of remaining tokens, which stood at 15,000,000 at first and fell as the session read pages and called tools. (session 2026-10-06, claude.ai, outside projects)
- **CTX-047** `observed` The counter stood at 15,000,000 again at the start of each new message from the user in the same conversation, and kept falling across the tool calls of one reply; a stop hook's feedback, which arrived as a message, did not reset it. (session 2026-10-06, claude.ai, outside projects)
- **CTX-048** `observed` While a subagent read a file of about 100 KB and reported 121,150 tokens of its own use, the parent's counter fell by about 1,000 tokens, roughly the size of the subagent's report; the subagent was shown a counter of its own, which fell by about 23,000 tokens while it read. (session 2026-10-06, claude.ai, outside projects)
- **CTX-045** `observed` The session's web fetch tool passed each page through a small model that answers a prompt about it: it returned the full text of documentation pages served as Markdown but only a summary of help-center articles and other web pages, whose text the built-in browser's page-text tool returned. (session 2026-10-06, claude.ai, outside projects)

## Usage

- **CTX-020** `documented` Usage depends on message length, attachment size, conversation length, tools such as Research and web search, the model, the effort level, artifacts, and multi-step tasks such as running code, creating files or browsing websites. [usage]
- **CTX-021** `documented` Usage in claude.ai, Claude Code and Claude Desktop counts toward the same limit. [lim]
- **CTX-022** `documented` Anthropic's guidance advises turning off tools and connectors that are not needed, because they use many tokens, and also lists removing unused project files, turning off extended thinking and choosing a lower effort level among the ways to save context and usage. [lim]
- **CTX-023** `documented` Pro, Max, Team and seat-based Enterprise plans have a five-hour session limit and weekly limits, shown under Settings > Usage, with a separate weekly limit for Fable where the plan includes it; usage-based Enterprise plans have no usage limits and are billed for every token at API rates. [usage] [ent]
- **CTX-024** `documented` On Pro and Max, the session limit resets every five hours, Max 5x and Max 20x give five and twenty times Pro's per-session allowance, and a weekly limit across all models resets at a fixed time assigned to the account, regardless of when the user starts using Claude; Anthropic may also limit usage in other ways, such as weekly and monthly caps. [pro] [max]
- **CTX-025** `documented` On the Free plan, a session-based usage limit resets every five hours, the number of messages varies with demand, and other limits may apply. [start]
- **CTX-026** `documented` On Team plans, usage limits apply to each member separately; a Standard seat has 1.25 times and a Premium seat 6.25 times the Pro plan's per-session allowance, each with a weekly limit across all models that resets at a fixed time assigned to the account. [team]
- **CTX-027** `documented` Claude warns when the five-hour session limit is near and, once it is reached, blocks further use with a message that gives the reset time; with usage credits on, the message says that work continues on usage credits. [err]
- **CTX-028** `documented` In the new Claude experience, everything the user does counts toward the plan's usage limits, longer agentic tasks that search the web, run code or create files generally use more than a quick question, and during the rollout usage may be measured slightly differently for accounts with and without it. [one]
- **CTX-029** `documented` From 2026-10-01 to 2026-10-15, on Pro, Max and Team, creating or editing an artifact makes the next 10 messages of that chat, up to 15 steps per reply, use 50% less of the five-hour session limit, and cloud Cowork tasks get a similar discount; it does not cover the weekly limit or, among others, Claude Code, local Cowork tasks and usage credits. [promo]

## Beyond the limits

- **CTX-050** `documented` When a usage limit is reached, the user can wait for it to reset, move to a higher plan or, on paid plans, turn on usage credits. [lim] [price]
- **CTX-051** `documented` On Pro, Max 5x and Max 20x, usage credits let the user keep working after reaching the plan's limits, billed at standard API rates separately from the subscription; they apply to both Claude conversations and Claude Code. [credits]
- **CTX-052** `documented` Pro and Max users turn on and prepay usage credits under Settings > Usage, which those who subscribed through a mobile app must open on the web, and can set a monthly spend limit and auto-reload; at most $2,000 is redeemed per day. [credits]
- **CTX-053** `documented` On Team and seat-based Enterprise plans, an Owner or Primary Owner turns on usage credits under Organization settings > Usage and can set spend limits for the organization and individual members; usage-based Enterprise plans have no included allowance, so usage credits do not apply. [credits-org]
- **CTX-054** `documented` A limit reset, given occasionally to eligible plans, sets either the five-hour session limit or the weekly limit back to full at once; it cannot be undone, and weekly limits still reset at their usual time. [reset]
- **CTX-055** `documented` A limit reset is used from Settings > Usage on the web or in Claude Desktop, or from the message shown at a limit, but not in Claude Mobile or Claude Code; because limits are shared across the account, the reset applies there too. [reset]

## Files and uploads

- **CTX-030** `documented` In chat, a file can be up to 500 MB, with up to 20 files per chat. [up]
- **CTX-031** `documented` In chat, images can be up to 8000 x 8000 pixels. [up]
- **CTX-032** `documented` PDFs are limited to 1000 pages, and a longer one is refused with an "Uploaded file is too large" error; Claude analyzes text and visuals for PDFs of up to 100 pages and text only beyond that. [up]
- **CTX-033** `documented` In projects, a file can be up to 30 MB, with an unlimited number of files, and only their text is extracted, except for multimodal PDFs. [up]
- **CTX-034** `documented` For document types other than PDF, Claude extracts text only, so embedded images are not processed. [up]
- **CTX-035** `documented` Uploading XLSX files requires code execution and file creation to be enabled. [up]
- **CTX-036** `documented` Uploads can be the document types PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON and XLSX and the image formats JPEG, PNG, GIF and WebP. [up]
- **CTX-037** `documented` In redesigned projects, the Library tab takes up to 100 files and 2 GB in one pick, with a single file up to 480 MB, while the New project dialog skips files over 30 MB. [cc-proj]
- **CTX-038** `documented` A folder added to a redesigned project arrives as a copy of its first 100 files up to 200 MB, without files over 30 MB, hidden files or `node_modules`; a project holds at most 10 folders and Google Drive folders combined, and single files do not count toward that limit. [cc-proj]
- **CTX-039** `documented` Uploads to a redesigned project are copies, so a change made on the computer afterwards reaches the project only when the file is uploaded again and replaced. [cc-proj]
- **CTX-046** `documented` In a Cowork project, files dragged in are copied into the project's first folder and folders are mounted as further project folders; Claude reads single files of up to 50 MB. [cw-guide]

## Sources

[cc-proj]: https://code.claude.com/docs/en/claude-projects
[conn-use]: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
[credits]: https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
[credits-org]: https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans
[ctx]: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
[cw-guide]: https://claude.com/docs/cowork/guide/projects
[ent]: https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan
[err]: https://support.claude.com/en/articles/12466728-troubleshoot-claude-error-messages
[lim]: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
[max]: https://support.claude.com/en/articles/11049741-what-is-the-max-plan
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[price]: https://claude.com/pricing
[pro]: https://support.claude.com/en/articles/8325606-what-is-the-pro-plan
[promo]: https://support.claude.com/en/articles/17274727-artifact-usage-promotion
[reset]: https://support.claude.com/en/articles/17007452-what-is-a-limit-reset
[start]: https://support.claude.com/en/articles/8114491-get-started-with-claude
[team]: https://support.claude.com/en/articles/9266767-what-is-the-team-plan
[tools]: https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access
[up]: https://support.claude.com/en/articles/8241126-upload-files-to-claude
[usage]: https://support.claude.com/en/articles/9797557-usage-limit-best-practices
[web]: https://support.claude.com/en/articles/10684626-enable-and-use-web-search

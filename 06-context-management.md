# 06 Context management

Prefix: CTX · Scope: context window, long conversations, files and usage in the Claude app · Last checked: 2026-10-05

## Context window

- **CTX-001** `documented` In chat on paid plans, Claude Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5 and Sonnet 5 have a context window of 1M tokens. [ctx]
- **CTX-002** `documented` In chat, Fable 5, Opus 4.8, Opus 4.7, Opus 4.6 and Sonnet 4.6 have 500K tokens; all other models have 200K. [ctx]
- **CTX-003** `documented` In Cowork, most models have 1M tokens, while Opus 4.6, Sonnet 4.6 and Haiku 4.5 have 200K. [ctx]
- **CTX-004** `documented` In Cowork, Sonnet 5 compacts the conversation automatically at 500K tokens. [ctx]
- **CTX-005** `documented` Part of the context window is reserved for Claude's reply, which shortens the maximum conversation length. [lim]

## Long conversations

- **CTX-010** `documented` For paid users with code execution enabled, Claude manages conversation context automatically by summarizing earlier messages when a conversation approaches the limit. [ctx]
- **CTX-011** `documented` Code execution must be enabled for automatic context management to work. [ctx]
- **CTX-012** `documented` After summarizing, Claude can still refer to the full chat history. [ctx] [lim]
- **CTX-013** `documented` While context is managed, Claude may show that it is "organizing its thoughts". [ctx]
- **CTX-014** `documented` Conversations long enough to trigger context management use more of the plan's usage. [lim]
- **CTX-015** `documented` A very large first message can still exceed the context limit; the error suggests fewer or smaller files or a new conversation. [lim] [err]
- **CTX-016** `observed` Long tool results were saved to a file in the workspace instead of being placed in the conversation in full, and Claude read the parts it needed. (session 2026-10-05, claude.ai, outside projects)
- **CTX-017** `observed` Tool, connector and skill definitions were partly deferred: Claude saw names and short descriptions and loaded full definitions only when needed. (session 2026-10-05, claude.ai, outside projects)

## Usage

- **CTX-020** `documented` Usage depends on conversation length, attachment size, tools, model and multi-step tasks; paid plans have a five-hour session limit and a weekly limit, shown under Settings > Usage. [usage]
- **CTX-021** `documented` Usage in claude.ai, Claude Code and Claude Desktop counts toward the same limit. [lim]
- **CTX-022** `documented` Anthropic's guidance advises turning off tools and connectors that are not needed, because they use tokens. [lim]

## Files and uploads

- **CTX-030** `documented` In chat, a file can be up to 500 MB, with up to 20 files per chat. [up]
- **CTX-031** `documented` Images can be up to 8000 x 8000 pixels. [up]
- **CTX-032** `documented` PDFs are limited to 1000 pages; Claude analyzes text and visuals for PDFs of up to 100 pages and text only beyond that. [up]
- **CTX-033** `documented` In projects, a file can be up to 30 MB, with an unlimited number of files. [up]
- **CTX-034** `documented` For document types other than PDF, Claude extracts text only, so embedded images are not processed. [up]
- **CTX-035** `documented` Spreadsheet files (XLSX) need code execution to be enabled. [up]

## Sources

[ctx]: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
[err]: https://support.claude.com/en/articles/12466728-troubleshoot-claude-error-messages
[lim]: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
[up]: https://support.claude.com/en/articles/8241126-upload-files-to-claude
[usage]: https://support.claude.com/en/articles/9797557-usage-limit-best-practices

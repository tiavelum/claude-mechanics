# 17 API and Agent SDK

Prefix: API · Scope: the Claude API and the Agent SDK as the base of the Claude app and Claude Code: requests, context management, prompt caching, tools, the memory tool, system prompts, Managed Agents · Last checked: 2026-10-07

## Requests

- **API-001** `documented` The Messages API holds no conversation state, it is "stateless": the caller sends the complete history with every request. [api-msg]
- **API-002** `documented` In each turn the model receives the whole conversation so far together with the new user message, and what it answers is fed in again as input on the following turn. [api-ctx]
- **API-003** `documented` The context window is charged with the entire request, that is the system prompt, the tool definitions and all messages together with the documents, images and tool results in them, and also with what Claude generates in the turn, extended thinking included. [api-ctx]
- **API-004** `documented` Reading a prefix from the prompt cache does not free any room in the context window: the cached tokens are counted in full. [api-ctx]
- **API-005** `inferred` Nothing carries over inside the model from one request of a Claude app conversation running on the Claude Code harness to the next: whatever the conversation knows has to arrive with the request or be brought in by a tool call while the turn runs. Basis: API-001, API-100, CC-088, SES-024.

## Context window

- **API-010** `documented` A request whose input is by itself larger than the context window is rejected on all models with a 400 error of type `invalid_request_error`, whose message is "prompt is too long". [api-ctx]
- **API-011** `documented` Where only the sum of the input and `max_tokens` is larger than the context window, models from the Claude 4.5 generation on take the request and end generation with the stop reason `model_context_window_exceeded` if the window fills up; older models answer with a validation error, unless the beta header `model-context-window-exceeded-2025-08-26` asks for the newer behaviour. [api-ctx]
- **API-012** `documented` Thinking blocks of earlier assistant turns remain part of the context by default, and are counted as input, on the Opus models from 4.5 on, the Sonnet models from 4.6 on, Fable 5.1, Mythos 5.1, Fable 5, Mythos 5 and Mythos Preview. [api-ctx]
- **API-013** `documented` On the Opus and Sonnet models before those, and on every Haiku model, the API removes earlier thinking blocks by itself when a request sends them back. [api-ctx]

## Context awareness and task budgets

- **API-020** `documented` The documentation names four context-aware models, Sonnet 5, Sonnet 4.6, Sonnet 4.5 and Haiku 4.5: during a conversation they follow how much room is left in their context window, called their "token budget", from tags that the API injects without any setting by the caller. [api-ctx]
- **API-021** `documented` To a context-aware model the API announces the size of the whole context window in each request's system prompt, which is 1M tokens for Sonnet 5 and Sonnet 4.6 and 200k tokens for Sonnet 4.5 and Haiku 4.5. [api-ctx]
- **API-022** `documented` Following every tool call, a context-aware model gets a `system_warning` tag from the API that reports the tokens used so far, the total and what remains. [api-ctx]
- **API-023** `documented` The API injects no such tags for the Opus models from 4.7 on, Sonnet 5.5, Fable 5.1, Mythos 5.1, Fable 5 and Mythos 5. [api-ctx]
- **API-024** `documented` For the models without injected tags, the documentation points to task budgets, a beta feature, as a way to state a budget explicitly. [api-ctx]
- **API-025** `documented` A task budget is a number of tokens the caller grants Claude for one whole agentic loop; output, thinking, tool calls and tool results all count against it. [api-budget]
- **API-026** `documented` A task budget is passed as `task_budget` inside `output_config`. [api-budget]
- **API-032** `documented` Task budgets are in beta under the header `task-budgets-2026-03-13`. [api-budget]
- **API-033** `documented` Task budgets are supported on Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Opus 5.5, Opus 5, Opus 4.8, Opus 4.7 and Sonnet 5.5. [api-budget]
- **API-027** `documented` While a task budget is set, the server inserts a countdown marker into the conversation that tells Claude how many tokens of the running loop are left; Claude paces its work by it and wraps up in good order as the budget runs down. [api-budget]
- **API-028** `documented` Only the model sees the countdown of a task budget; nothing in an API response reports the remaining budget. [api-budget]
- **API-029** `documented` A task budget is advisory: Claude can overrun it now and then to complete an action in progress, and the limit that is actually enforced on output is still `max_tokens`. [api-budget]
- **API-030** `documented` A task budget applies to a single agentic turn: the turn starts with a user message that contains no tool results, includes all of Claude's work in answer to it, and may extend over several requests. [api-budget]
- **API-031** `documented` According to the task budgets page, Claude Code and Cowork do not support task budgets, which are to be used through the Messages API directly. [api-budget]

## Compaction

- **API-040** `documented` With compaction, the server has Claude summarize the older part of a conversation and puts that summary in the place of those turns, which spares the caller from writing its own summarization. [api-compact]
- **API-041** `documented` Server-side compaction exists in two kinds, both in beta: compaction on demand, which the caller starts with a request of its own, and compaction at a token threshold, which the API starts when the input reaches a trigger value set by the caller. [api-compact]
- **API-042** `documented` The documentation treats server-side compaction as the main way to manage context in long conversations and agentic workflows. [api-ctx]
- **API-055** `documented` Between the two kinds of server-side compaction the documentation advises on-demand compaction wherever it can be used. [api-compact]
- **API-043** `documented` Threshold compaction works automatically inside ordinary requests: the caller adds the `compact_20260112` strategy to `context_management.edits`, and when a request reaches the threshold the API summarizes the older context in the middle of that request. [api-compact-thr]
- **API-056** `documented` Threshold compaction is a beta feature that needs the header `compact-2026-01-12`. [api-compact-thr]
- **API-044** `documented` The trigger of threshold compaction is measured in input tokens, the only supported type, with a default of 150,000 and a minimum of 50,000. [api-compact-thr]
- **API-045** `documented` The response of a request in which threshold compaction ran contains a compaction block; the caller adds the response to its messages as always, and in the following requests the API ignores everything that comes before that block. [api-compact-thr]
- **API-046** `documented` On Fable 5.1, Mythos 5.1, Opus 5.5 and Sonnet 5.5, thinking that precedes a compaction block is dropped as well, which leaves the summary as the model's only record of the earlier work. [api-compact-thr]
- **API-047** `documented` Compaction on demand is asked for with the top-level parameter `compaction`. [api-compact-od] [api-compact]
- **API-057** `documented` A compaction-on-demand request needs the beta header `compact-2026-09-04`, and so does each later request that includes the signed block. [api-compact-od]
- **API-048** `documented` The answer to an on-demand compaction request is not a reply but one compaction block, consisting of a summary in readable text and a signature, with the stop reason `compaction`; all messages in the request are summarized. [api-compact-od]
- **API-049** `documented` After an on-demand compaction the caller leaves out the summarized messages in later requests and starts `messages` with the compaction block; to Claude the summary then stands where those messages used to be. [api-compact-od]
- **API-050** `documented` A compaction summary carries no images, documents, `container_upload` blocks or fetched URLs: those that were in the summarized messages are lost when the compaction block takes their place. [api-compact-od]
- **API-051** `documented` Which turns survive an on-demand compaction word for word is decided by the caller, not by a parameter: only the messages before a chosen cut point are sent for summarizing, and the later ones are sent unchanged after the block. [api-compact-keep]
- **API-052** `documented` The models listed for on-demand compaction are Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Mythos Preview, Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5.5, Sonnet 5 and Sonnet 4.6. [api-compact-od]
- **API-053** `documented` On 2026-02-05 the compaction API was launched in beta, as summarization of context on the server, available on Opus 4.6. [api-rn]
- **API-054** `documented` On 2026-09-14 compaction on demand was added to the Messages API, as a beta feature of the Claude API under the header `compact-2026-09-04`. [api-rn]

## Context editing

- **API-060** `documented` Context editing removes selected content from the conversation history by two strategies: clearing tool results and clearing thinking blocks. [api-edit]
- **API-069** `documented` Context editing is a beta feature enabled with the header `context-management-2025-06-27`. [api-edit]
- **API-061** `conflicting` Where context editing happens: according to the context editing page, the server applies the edits to the prompt before Claude gets it, and the caller's own copy of the conversation stays complete and needs no adjusting; the memory tool page, in contrast, describes context editing as clearing tool results "on the client". [api-edit] [api-memtool]
- **API-201** `documented` Besides the edits made on the server, the TypeScript and Ruby SDKs offer compaction for their tool runner as an SDK feature: once token use grows too large it writes a summary and replaces the whole message history with it, whereas server-side editing leaves the caller's history unchanged. [api-edit]
- **API-202** `documented` The context editing page recommends server-side compaction over SDK compaction: the SDKs' `compaction_control` parameter is deprecated in TypeScript and Ruby and removed from the Python SDK as of v1.0, and a tool runner gets server-side compaction by passing `compact_20260112` in `context_management`. [api-edit]
- **API-062** `documented` The strategy `clear_tool_uses_20250919` takes effect when the context passes a threshold the caller configured: starting from the oldest, tool results are replaced by a placeholder that lets Claude know something was removed, and the parameters of the tool calls are removed too only if `clear_tool_inputs` is turned on. [api-edit]
- **API-063** `documented` The default threshold for clearing tool results is 100,000 input tokens; a caller can set another one, expressed either as input tokens or as a number of tool uses. [api-edit]
- **API-064** `documented` Unless configured otherwise, tool result clearing spares the last 3 tool uses with their results and works from the oldest interaction forward. [api-edit]
- **API-065** `documented` Each time tool results are cleared, cached prompt prefixes become invalid, so every clearing is paid for with a new cache write. [api-edit]
- **API-066** `documented` For thinking block clearing (`clear_thinking_20251015`) the default depends on the model: Opus from 4.5 on, Sonnet from 4.6 on and every Fable and Mythos model keep all earlier thinking, while Opus up to 4.1, Sonnet up to 4.5 and the Haiku models up to Haiku 4.5 keep the thinking of the last turn only. [api-edit]
- **API-067** `documented` As long as thinking blocks stay in the context the prompt cache keeps working; once they are cleared, the cache is invalid from the place of the clearing on. [api-edit]
- **API-068** `documented` If the memory tool is in use alongside context editing, Claude is warned automatically as the conversation nears the clearing threshold and can write what matters from the tool results into its memory files while they are still in the context. [api-edit]

## Prompt caching

- **API-080** `documented` The API caches nothing unless asked: when a request has no `cache_control`, neither the automatic top-level field nor an explicit breakpoint, the full conversation is billed at the normal input rate each time. [api-midsys]
- **API-081** `documented` For automatic caching one `cache_control` field is set on the request as a whole; the breakpoint is then placed by the system on the final block that can be cached and moves along as the conversation grows. [api-cache]
- **API-082** `documented` The number of cache breakpoints in a request is limited to 4, and the automatic breakpoint counts as one of them. [api-cache]
- **API-083** `documented` The cached prefix is assembled from the tool definitions first, the system prompt second and the messages third, each layer resting on those before it. [api-cache]
- **API-084** `documented` A change in one layer of the cached prefix (tools, system, messages) makes the cache invalid for that layer and for those after it; a changed tool definition therefore costs the whole cache. [api-cache]
- **API-085** `documented` A cache entry is reused only if everything up to and including the block at which it was written is exactly the same as before, text as well as images. [api-cache]
- **API-086** `documented` By default, cached content expires after 5 minutes unless it is used again, which renews the period free of charge. [api-cache]
- **API-093** `documented` The cache lifetime is counted from when the request that wrote or read the entry began, not from when its response was complete. [api-cache]
- **API-087** `documented` A request can ask for a cache lifetime of 1 hour in place of the default 5 minutes. [api-cache]
- **API-089** `documented` A change that breaks the cache means that the prefix is written to the cache again where it would otherwise have been read from it; Anthropic's cost guide puts such a broken turn at 50 times the cost of a cache read on Fable 5.1 and Mythos 5.1, 25 times on Opus 5.5 and 12.5 times on the remaining current models. [api-cost]
- **API-090** `documented` On the Claude API, Microsoft Foundry, Google Cloud and Claude Platform on AWS, a prompt has to reach a minimum length to be cached, which is 512 tokens on Fable 5.1, Mythos 5.1, Opus 5.5, Opus 5, Sonnet 5.5, Fable 5 and Mythos 5; the other listed models need 1,024 to 4,096 tokens. [api-cache]
- **API-091** `documented` On the Claude API, Microsoft Foundry, Google Cloud and Claude Platform on AWS, marking a shorter prompt with `cache_control` has no effect and raises no error: the request simply runs uncached. [api-cache]
- **API-092** `documented` No cache is shared across organizations; inside one organization every workspace has a cache of its own on Microsoft Foundry, Claude Platform on AWS and the Claude API, whereas on Amazon Bedrock and Google Cloud isolation stops at the organization. [api-cache]

## Tools

- **API-100** `documented` Claude does not run tools itself: its output contains a structured request for an operation, the operation is carried out by the caller's code or on Anthropic's servers, and the outcome is handed back to it as part of the conversation. [api-tools-how]
- **API-101** `documented` Tools fall into three groups by where the code runs: the caller's own tools and the tools with a schema published by Anthropic (`memory`, `bash`, `text_editor`, `computer`, `browser`) are executed in the caller's application, and `web_search`, `web_fetch`, `code_execution` and `tool_search` are executed by Anthropic. [api-tools-how]
- **API-102** `documented` With client-executed tools the caller drives a loop: as long as a response ends with the stop reason `tool_use`, the caller runs the requested tools and sends the conversation again, extended by that response and by a user message holding the `tool_result` blocks. [api-tools-how]

## Tool search

- **API-110** `documented` With the tool search tool, tool definitions need not all sit in the context window from the start: Claude queries the caller's catalog of tools, in which names, descriptions and the names and descriptions of arguments are searched, and only the tools it picks are loaded. [api-toolsearch]
- **API-111** `documented` With tool search, Claude at first sees only the tool search tool and whichever tools are not marked as deferred; a request must leave at least one tool undeferred. [api-toolsearch]
- **API-112** `documented` A tool search is executed by the API, which answers with `tool_reference` blocks for the tools found, 5 at most unless Claude sets another `limit`, and then replaces those references by the complete definitions on its own. [api-toolsearch]
- **API-113** `documented` Deferring a tool with `defer_loading` keeps its definition out of the context window but not out of the request: the `tools` array still has to contain all definitions in full each time. [api-toolsearch]
- **API-114** `documented` Deferred tools are not part of the prefix that carries the system prompt; a tool found by search enters the conversation at the point of discovery as a `tool_reference` block, so nothing before it changes and the prompt cache stays valid. [api-toolsearch]
- **API-115** `documented` Tool search is not metered as a server tool of its own; what counts are the input tokens of the definitions it brings into the context, the same as for any tool definition. [api-toolsearch]

## Memory tool

- **API-120** `documented` Through the memory tool Claude keeps information from one conversation to the next in files of a memory directory, which it creates, reads, changes and deletes. [api-memtool]
- **API-121** `documented` The memory tool is client-side and the memory lives in the calling application: Claude merely asks for file operations, and the application performs them on storage of its own, to which it maps the path prefix `/memories`. [api-memtool]
- **API-122** `documented` A model that has the memory tool looks into its memory directory on its own before beginning a task, notes what it learns in files below `/memories` while working, and reads these files again in later conversations. [api-memtool]
- **API-123** `documented` The application has to handle the six commands of the memory tool: `view`, `create`, `str_replace`, `insert`, `delete` and `rename`. [api-memtool]
- **API-124** `documented` For a request that includes the memory tool, the API itself extends the system prompt with an instruction: look at the memory directory first of all, keep a record of progress in it, and expect that the context window can be reset at any time. [api-memtool]
- **API-125** `documented` The memory tool page suggests combining the tool with compaction for agents that run for a long time: compaction holds the active context down, and memory keeps what a summary must not lose. [api-memtool]

## System prompts

- **API-130** `documented` Anthropic publishes the updates to the system prompt used by claude.ai and the mobile apps, and notes that the Claude API is not affected by these updates. [api-sysprompt]
- **API-131** `documented` If a request passes `tools`, the system prompt that reaches the model is one the API assembles: it combines the definitions of the tools and the tool configuration with the system prompt supplied by the caller, if any. [api-tools-def]

## Mid-conversation system messages and tool changes

- **API-140** `documented` An instruction that comes up partway through a conversation can be added as a message with the role `system` inside `messages`, leaving the top-level `system` field as it is: the cached prefix is not touched, and Claude takes the text as a system instruction, valid from there on, not as user text. [api-midsys]
- **API-141** `documented` The Messages API guide gives a mid-conversation system message equal authority with the top-level `system` field; since it is added at the end of the history, the prefix cached up to that point remains usable. [api-msg]
- **API-142** `documented` Claude attributes user messages to the end user and system messages to the operator of the application, and where the two conflict the system side wins. [api-midsys]
- **API-150** `documented` Where system instructions conflict, a newer system message overrides an older one, and for the turns after it a mid-conversation system message overrides the top-level `system` field. [api-midsys]
- **API-143** `documented` Mid-conversation system messages work without a beta header on Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Opus 5.5, Opus 5, Opus 4.8 and Sonnet 5.5; Sonnet 5 does not have them. [api-midsys]
- **API-144** `documented` The placement of a mid-conversation system message is restricted: it must come right after a user turn, which may be one carrying tool results, or after an assistant turn that closes with the result of a server tool, and after it only an assistant turn or the end of `messages` is allowed; any other position is answered with a 400 error. [api-midsys]
- **API-145** `documented` Changing or deleting a mid-conversation system message after it was sent breaks the cache from its position on, and on Fable 5.1, Opus 5.5 and Sonnet 5.5 it also makes the thinking blocks of all later assistant turns invalid. [api-midsys]
- **API-146** `documented` A system message can be limited to the current turn by setting its `clear_at` field to `next_user_message`, a beta that needs its own beta header, which carries the date 2026-08-21: once a user message follows, the message stays in `messages` but is not shown to the model and does not count as input. [api-midsys]
- **API-147** `documented` On the Claude API, tools can be switched on and off during a conversation by system messages too, a beta that uses the header `inline-tools-2026-09-15`: `tool_addition` and `tool_removal` blocks in a system message make a tool available or unavailable from then on without any change to the `tools` array. [api-midsys]
- **API-148** `documented` One use of a mid-conversation system message that the documentation describes concerns a user who writes again while Claude is in the middle of a tool loop: the application hands the new input over in a system message placed after the next tool result, and Claude takes it into account in the running work without starting over. [api-midsys]
- **API-149** `documented` The documentation warns that text of foreign origin, for example web pages, retrieved documents or unprocessed tool output, does not belong in a system message, where it would carry the operator's authority, and advises keeping it in tool results. [api-midsys]

## Managed Agents

- **API-160** `documented` Anthropic's documentation presents two ways of building on Claude: the Messages API, which gives direct access to the model and suits self-built agent loops and fine-grained control, and Claude Managed Agents, a ready-made, configurable agent harness on managed infrastructure that suits long-running and asynchronous work. [ma-over]
- **API-161** `documented` Managed Agents is a beta, and its beta header depends on the endpoint: `managed-agents-2026-04-01` for agents, sessions and environments, `agent-memory-2026-07-22` for memory stores, where it replaces the first and a request with both is answered with a 400 error; Anthropic's SDK sends the right one by itself. [api-beta] [ma-over] [ma-mem]
- **API-162** `documented` Prompt caching and compaction are built into the Managed Agents harness. [ma-over]
- **API-163** `documented` Managed Agents keeps state on the server by design: a session can run for a long time, be paused and continued, and its outputs, sandbox state and conversation history are stored on the server side. [ma-over]
- **API-164** `documented` An agent in Managed Agents is a stored definition made up of a model, a system prompt, skills, tools and MCP servers, which is set up one time and then referred to by ID from any number of sessions. [ma-over]
- **API-165** `documented` A Managed Agents session references one agent and one environment, both of which exist independently of it, and it preserves the conversation history from one interaction to the next. [ma-ses]
- **API-166** `documented` A Managed Agents cloud environment is a sandbox configuration that any number of sessions can use; the sandbox itself is separate for every session, a newly started Linux container, so no files are shared between sessions. [ma-env]
- **API-167** `documented` Communication with a Managed Agents session goes through events: the application sends the user's messages as events and gets Claude's work back as a stream of events, the server keeps the full event history, and the application can send more user events during execution to redirect the agent or to interrupt it. [ma-over]
- **API-168** `documented` A Managed Agents session cannot change the `system` field of its agent while it lives; what remains possible, on models with support for it, is to add system-level guidance during the session by means of a `system.message` event. [ma-ops]
- **API-169** `documented` The event `agent.thread_context_compacted` tells the application that Managed Agents has compacted a conversation history so that it fits into the context window. [ma-ref]
- **API-170** `documented` Since 2026-05-19 Managed Agents does not put a tool output of more than 100K characters, roughly 25K tokens, into the conversation in full, whether it comes from the agent toolset or an MCP tool: the output is saved as a file in the sandbox, and the model is given a shortened preview and the path. [api-rn]
- **API-171** `documented` By default each Managed Agents session begins with a fresh context, and whatever state an agent accumulated ends with its session; memory stores exist to pass information on between sessions. [ma-mem]
- **API-172** `documented` A Managed Agents memory store holds text documents and belongs to a workspace; a session to which it is attached finds it in its sandbox as a directory below `/mnt/memory/`. [ma-mem]
- **API-173** `documented` What an agent writes into the mounted directory of a memory store is saved in the store and kept in sync with the other sessions that have the same store attached. [ma-mem]
- **API-174** `documented` The system prompt of a Managed Agents session is extended automatically by a brief note for every memory store attached, giving its display name, where it is mounted, its access mode, its description and any instructions for its use. [ma-mem]
- **API-175** `documented` Memory stores are chosen when a Managed Agents session is created: there is no way to attach or detach one while the session is running. [ma-mem]

## Agent SDK

- **API-190** `documented` With the Agent SDK, a Python or TypeScript program can use what Claude Code itself is built on: its tools, its agent loop and its context management. [cc-sdk]
- **API-191** `documented` The Agent SDK is a library around the Claude Code binary, which it runs; Claude Code capabilities such as the built-in tools, permissions, sessions and hooks are available through it. [cc-sdk]
- **API-192** `documented` The Client SDK is another option the Agent SDK overview names, for code that calls the Claude API directly: there the tool loop is the developer's own, or is left to the tool runner of the client SDK, a beta. [cc-sdk]
- **API-193** `documented` An Agent SDK session keeps its context from one exchange to the next, and it can be taken up again later or forked. [cc-sdk]
- **API-194** `documented` Like Claude Code, the Agent SDK by default picks up skills, commands and memory from `.claude/` in the project and from `~/.claude/`. [cc-sdk] [cc-sdk-feat]
- **API-195** `documented` Which filesystem sources an Agent SDK query reads is set by the option `settingSources`: left out, it means user, project and local settings, the CLAUDE.md files and the skills, agents and commands in `.claude/`, exactly what the Claude Code CLI reads, and passed as an empty list it restricts the agent to its programmatic configuration. [cc-sdk-feat]
- **API-196** `documented` An Agent SDK session reads some inputs whatever `settingSources` contains: managed policy settings, the global configuration in `~/.claude.json`, auto memory, which is loaded when the session starts, and the claude.ai connectors of a session that signs in with a claude.ai login. [cc-sdk-feat]
- **API-197** `documented` Auto memory has no tool of its own in an Agent SDK session: the agent saves memories with the ordinary `Write` and `Edit` tools and can do so only if they are enabled. [cc-sdk-feat]
- **API-198** `documented` An agent started through the Agent SDK with no system prompt option gets only a minimal prompt for tool calling, without the remaining content of the Claude Code prompt and so without its security and safety instructions; a run of `claude -p` differs: by default it works with the system prompt of Claude Code. [cc-sdk-prompt]
- **API-199** `documented` The Agent SDK offers two other starting points for the system prompt: the preset `claude_code`, which is the CLI's own system prompt and accepts instructions appended at its end, and a prompt string written by the developer, in which case nothing else is sent as system prompt. [cc-sdk-prompt]
- **API-200** `documented` System reminders, the context Claude Code adds during a session, travel in the `messages` array of its requests: they are placed within a user message between `<system-reminder>` tags, and some models receive them as a message of their own with the role `system` instead. [cc-sdk-prompt]

## Sources

[api-beta]: https://platform.claude.com/docs/en/api/beta-headers
[api-budget]: https://platform.claude.com/docs/en/build-with-claude/task-budgets
[api-cache]: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
[api-compact]: https://platform.claude.com/docs/en/build-with-claude/compaction
[api-compact-keep]: https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns
[api-compact-od]: https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand
[api-compact-thr]: https://platform.claude.com/docs/en/build-with-claude/compaction-threshold
[api-cost]: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
[api-ctx]: https://platform.claude.com/docs/en/build-with-claude/context-windows
[api-edit]: https://platform.claude.com/docs/en/build-with-claude/context-editing
[api-memtool]: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
[api-midsys]: https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages
[api-msg]: https://platform.claude.com/docs/en/build-with-claude/working-with-messages
[api-rn]: https://platform.claude.com/docs/en/release-notes/overview
[api-sysprompt]: https://platform.claude.com/docs/en/release-notes/system-prompts/overview
[api-tools-def]: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools
[api-tools-how]: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
[api-toolsearch]: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool
[cc-sdk]: https://code.claude.com/docs/en/agent-sdk/overview
[cc-sdk-feat]: https://code.claude.com/docs/en/agent-sdk/claude-code-features
[cc-sdk-prompt]: https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts
[ma-env]: https://platform.claude.com/docs/en/managed-agents/environments
[ma-mem]: https://platform.claude.com/docs/en/managed-agents/memory
[ma-ops]: https://platform.claude.com/docs/en/managed-agents/session-operations
[ma-over]: https://platform.claude.com/docs/en/managed-agents/overview
[ma-ref]: https://platform.claude.com/docs/en/managed-agents/reference
[ma-ses]: https://platform.claude.com/docs/en/managed-agents/sessions

# 09 Claude Code

Prefix: CC · Scope: memory, instruction files, settings, sessions and their environments (worktrees, cloud environments, Remote Control), and context in Claude Code (terminal, desktop Code tab, IDE, cloud sessions), and how it relates to the Claude app · Last checked: 2026-10-07

## Memory model

- **CC-001** `documented` No Claude Code session inherits an earlier session's context window; what persists between sessions does so through CLAUDE.md files, which the user writes, and auto memory, which Claude writes. [cc-mem]
- **CC-002** `documented` Both CLAUDE.md and auto memory are loaded at the start of every conversation and are treated as context, not as enforced configuration. [cc-mem]
- **CC-003** `documented` For an action that must be blocked whatever Claude decides, the documentation points to a PreToolUse hook rather than CLAUDE.md. [cc-mem]
- **CC-004** `documented` The more specific and concise the instructions, the more consistently Claude follows them. [cc-mem]
- **CC-005** `documented` The documentation assigns technical enforcement to settings, which the client enforces regardless of what Claude decides, and behavioural guidance to CLAUDE.md, which is not a hard enforcement layer. [cc-mem]
- **CC-006** `documented` Claude Code, not the model, enforces permission rules; what a prompt or CLAUDE.md says leaves unchanged what Claude Code permits. [cc-perm]
- **CC-007** `documented` Claude Code passes CLAUDE.md content to Claude as a user message that follows the system prompt, not inside the system prompt, and does not guarantee strict compliance. [cc-mem]
- **CC-008** `documented` Claude Code's system prompt is not published; the documentation points to CLAUDE.md files or the `--append-system-prompt` flag for standing instructions. [cc-set]

## Instruction files

- **CC-010** `documented` A managed policy CLAUDE.md applies to all users on a machine: `/Library/Application Support/ClaudeCode/CLAUDE.md` on macOS, `/etc/claude-code/CLAUDE.md` on Linux and WSL, `C:\Program Files\ClaudeCode\CLAUDE.md` on Windows. [cc-mem]
- **CC-011** `documented` `~/.claude/CLAUDE.md` holds the user's personal instructions for all projects. [cc-mem]
- **CC-012** `documented` `./CLAUDE.md` or `./.claude/CLAUDE.md` holds the project's shared instructions. [cc-mem]
- **CC-013** `documented` `./CLAUDE.local.md` holds personal project-specific instructions; the documentation advises adding it to `.gitignore`. [cc-mem]
- **CC-014** `documented` At launch, Claude Code loads every CLAUDE.md and CLAUDE.local.md found in the working directory or in any directory above it. [cc-mem]
- **CC-015** `documented` All discovered files are concatenated rather than overriding each other, ordered from the filesystem root down, so instructions closer to the working directory are read last. [cc-mem]
- **CC-016** `documented` In each directory, CLAUDE.local.md comes after that directory's CLAUDE.md. [cc-mem]
- **CC-017** `documented` CLAUDE.md files in subdirectories load on demand, when Claude reads, writes or edits files in those subdirectories. [cc-mem]
- **CC-018** `documented` A managed policy CLAUDE.md cannot be excluded by individual settings. [cc-mem]
- **CC-019** `documented` A gitignored CLAUDE.local.md exists only in the worktree where it was created. [cc-mem]
- **CC-020** `documented` Block-level HTML comments in CLAUDE.md are stripped before the content enters Claude's context; comments inside code blocks are kept. [cc-mem]
- **CC-021** `documented` Unless a setting says otherwise, Claude reads `AGENTS.md` only if neither CLAUDE.md, `.claude/CLAUDE.md` nor CLAUDE.local.md exists in the working directory or a directory above it; reading `AGENTS.md` directly needs Claude Code v2.1.277 or later, and a setting can load both. [cc-mem]
- **CC-022** `documented` The user-level `~/.claude/CLAUDE.md`, the managed CLAUDE.md and `.claude/rules/` files do not count for that rule and keep loading alongside AGENTS.md. [cc-mem]
- **CC-023** `documented` The CLAUDE.md scopes load in order from broadest to most specific (managed policy, user, project, local), which puts a project instruction later in context than a user instruction. [cc-mem]
- **CC-024** `documented` The **Project instructions** option in `/config` chooses which instruction files load: `claude-md-or-agents-md` (the default), `claude-md-and-agents-md`, `claude-md` or `managed-only`. [cc-mem]
- **CC-025** `documented` CLAUDE.md files in directories added with `--add-dir` do not load by default; `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` loads them. [cc-mem]
- **CC-026** `documented` Claude Code reads a CLAUDE.md in full up to a size of 4 MiB and skips one above that; the limit of 200 lines and 25 KB is for `MEMORY.md` only. [cc-mem]
- **CC-027** `documented` The documentation advises keeping each CLAUDE.md under 200 lines, because longer files consume more context and reduce adherence. [cc-mem]
- **CC-028** `conflicting` What Claude does with two CLAUDE.md instructions that contradict each other: the memory page says Claude may pick one arbitrarily, while the extension overview says Claude uses judgment to reconcile them. [cc-mem] [cc-ext]
- **CC-029** `documented` `/init` generates a starting CLAUDE.md from the codebase and, when a CLAUDE.md already exists, suggests improvements instead of overwriting it. [cc-mem]
- **CC-120** `documented` `/memory` shows where the memory files of the user and project scopes are, among them CLAUDE.md and CLAUDE.local.md, switches auto memory on or off and can open the auto memory folder. [cc-mem]

## Imports and rules

- **CC-030** `documented` CLAUDE.md can import other files with `@path/to/file`; relative paths resolve from the importing file, and imports can nest up to four hops deep. [cc-mem]
- **CC-031** `documented` Claude Code expands imported files and puts them into context at launch. [cc-mem]
- **CC-032** `documented` The first time a project's CLAUDE.md imports files from outside the working directory, Claude Code asks for approval; if declined, those imports stay disabled. [cc-mem]
- **CC-033** `documented` Imports in user-scope files such as `~/.claude/CLAUDE.md` load without that dialog, except in Cowork sessions on the desktop, which skip imports pointing outside the session's working directory. [cc-mem]
- **CC-034** `documented` Instructions can be split into topic files in `.claude/rules/`; rules without a `paths` field load at launch like CLAUDE.md. [cc-mem]
- **CC-035** `documented` A rule with `paths` frontmatter loads only when Claude reads, writes or edits a file matching its glob patterns. [cc-mem]
- **CC-036** `documented` Rules in `~/.claude/rules/` belong to the user, hold for all projects and load ahead of project rules; neither set overrides the other. [cc-mem]
- **CC-037** `documented` The `claudeMdExcludes` setting skips specific CLAUDE.md or rule files by path or glob; it can be set in any settings layer, and the arrays merge across layers. [cc-mem]
- **CC-038** `documented` Claude Code finds the `.md` files in a project's `.claude/rules/` recursively, so rules can be grouped in subdirectories such as `frontend/` or `backend/`. [cc-mem]

## Auto memory

- **CC-040** `documented` Local sessions have auto memory on unless it is turned off; in self-hosted environments it starts off, except in Claude Tag sessions. [cc-mem]
- **CC-041** `documented` Auto memory is toggled in `/memory`, which saves `autoMemoryEnabled` to `~/.claude/settings.json`; a project can turn it off in its own settings, and `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` turns it off as well. [cc-mem]
- **CC-042** `documented` Auto memory for a project lives in `~/.claude/projects/<project>/memory/`, with `<project>` derived from the git repository. [cc-mem]
- **CC-043** `documented` All worktrees and subdirectories of the same repository share one auto memory directory; outside a git repository, the project root is used. [cc-mem]
- **CC-044** `documented` Auto memory is machine-local and not shared across machines or cloud environments. [cc-mem]
- **CC-045** `documented` At the start of every conversation Claude Code loads `MEMORY.md` up to its first 200 lines or first 25 KB, whichever limit is reached first; topic files load on demand. [cc-mem]
- **CC-046** `documented` When the user asks Claude to remember something, Claude saves it to auto memory; to put it in CLAUDE.md instead, the user asks for that explicitly. [cc-mem]
- **CC-047** `documented` `autoMemoryDirectory` moves auto memory to another location; it is read from any settings scope and must be an absolute path or start with `~/`. [cc-mem]
- **CC-048** `documented` Old session transcripts are deleted after the retention period, but auto memory files are excluded from that cleanup. [cc-mem]
- **CC-049** `documented` The main conversation's auto memory is not loaded into subagents, except forks, which inherit the parent conversation. [cc-mem]
- **CC-050** `documented` Auto memory cannot be turned on in background sessions or in sessions started by another Claude Code session. [cc-mem]
- **CC-051** `documented` Claude saves four kinds of auto memory notes, recorded in a `type` frontmatter field: `user` (role, expertise, working preferences), `feedback` (corrections and confirmed approaches), `project` (ongoing work, deadlines and decisions not derivable from the code or git history) and `reference` (where to find information outside the project). [cc-mem]
- **CC-052** `documented` Claude leaves out what it can work out from the codebase and what the CLAUDE.md files already state, and it does not save a note in every session. [cc-mem]
- **CC-053** `documented` After Claude writes to `MEMORY.md`, Claude Code checks it against the 200-line and 25 KB limits and reminds Claude to shorten it when it is near one; content past a limit is dropped on the next load. [cc-mem]
- **CC-054** `documented` In the redesigned projects (beta), project memory files are separate from the auto memory Claude Code keeps on the user's machine, although both use a `MEMORY.md` index. [cc-proj]

## Settings

- **CC-060** `documented` Settings precedence, highest first: managed settings, command line (`--settings`), project local (`.claude/settings.local.json`), shared project (`.claude/settings.json`), user (`~/.claude/settings.json`). [cc-set]
- **CC-061** `documented` For the same key, the value from a higher level wins over a value set lower down. [cc-set]
- **CC-062** `documented` Managed settings can come from a managed settings file, from MDM or OS policy, or from the claude.ai console. [cc-set] [cc-man]
- **CC-063** `documented` On one computer, the terminal, the extensions for VS Code and JetBrains and the desktop app's local sessions all read the same settings files. [cc-set] [cc-plug]
- **CC-064** `documented` Settings are JSON keys that control behaviour such as the starting model, what can run without asking, which files cannot be read, terminal appearance and what an organization enforces. [cc-set]
- **CC-065** `documented` `~/.claude/settings.json` applies to the user in every project on the machine, `.claude/settings.json` to everyone working in its folder and is meant to be committed, and `.claude/settings.local.json` to the user in one project only; when Claude Code creates the local file, it keeps it out of git. [cc-set]
- **CC-066** `documented` Nothing a user sets overrides managed settings, apart from a few security-sensitive keys for which a stricter value from a lower level is honoured. [cc-set]
- **CC-067** `documented` Environment variables are not a level in the settings precedence; whether a shell variable or a settings key applies is decided for each pair. [cc-set]
- **CC-068** `documented` A list key such as `permissions.allow` that several settings files set is merged across them rather than taken from one file. [cc-set]
- **CC-069** `documented` Claude Code watches the settings files and applies most edits, including permissions, hooks and credential helpers, to a running session without a restart. [cc-set]
- **CC-121** `documented` Besides the settings files, Claude Code keeps `~/.claude.json`, which it writes itself; it holds the sign-in session, MCP server configurations and per-project state such as trust decisions. [cc-set]
- **CC-122** `documented` When a feature exists at several levels, CLAUDE.md files add up, skills and subagents override by name, MCP servers override by name (local over project over user) and all hooks fire. [cc-ext]
- **CC-123** `documented` A cloud session does not read user or project local settings; a managed settings file or MDM profile on the user's device does not reach it, while the organization's server-managed settings do. [cc-set]
- **CC-124** `documented` At claude.ai/code in the browser, `/config` opens the Claude Code part of the claude.ai settings; a setting for a cloud session is changed through an environment variable of its environment or, with one repository, through the committed `.claude/settings.json`. [cc-set]
- **CC-125** `documented` Plugins install at user scope (every project on the computer), project scope (everyone in the repository, through the committed `.claude/settings.json`) or local scope (the user in that repository only). [cc-plug-over]

## Sessions

- **CC-070** `documented` Claude Code writes each session continuously to a JSONL transcript, `~/.claude/projects/<project>/<session-id>.jsonl`; `<project>` is the working directory path in which every character other than a letter or digit becomes `-`, and the format is internal and may change. [cc-ses]
- **CC-071** `documented` `claude --continue` opens the latest conversation of the current directory again; `claude --resume` opens a picker or a named session. [cc-ses]
- **CC-072** `documented` `/clear` starts a fresh, empty context and saves the previous conversation, which can be resumed with `/resume` or, in the same process, from the rewind menu. [cc-ses]
- **CC-073** `documented` `/branch` and `--fork-session` copy the conversation so far into a new session ID and leave the original unchanged. [cc-ses] [cc-how]
- **CC-074** `documented` A resume from a terminal without `-p`, by `claude --continue`, by `claude --resume <session-id>` or by a name that matches one session, brings back the session's permission mode except in listed cases; the session picker and `/resume` bring it back only for a session that ended in plan mode. [cc-ses]
- **CC-075** `documented` Transcripts are kept for 30 days by default, configurable with `cleanupPeriodDays`; `CLAUDE_CONFIG_DIR` moves storage off `~/.claude`. [cc-ses]
- **CC-076** `documented` On Pro or Max, resuming a session inactive for over about an hour and over 100,000 tokens offers to compact the history first. [cc-ses]
- **CC-077** `documented` A session is a conversation that Claude Code saves on the user's machine while the user works, and it belongs to one project directory. [cc-ses]
- **CC-078** `documented` `claude --continue` and `claude --resume` reopen a session with its existing session ID, and new messages are added to the end of that conversation. [cc-how]
- **CC-079** `documented` Resuming restores the whole conversation history with its tool calls and results; a tool that had not finished when the previous process ended is neither completed nor run again. [cc-ses]
- **CC-140** `documented` After a resume the session keeps its earlier model, unless that model is retired or not allowed by `availableModels`, a `--model` flag or an `ANTHROPIC_MODEL`-family variable picks one at launch, or the provider uses provider-specific deployment IDs, as Amazon Bedrock does. [cc-ses]
- **CC-141** `documented` `/branch` keeps "Allow for this session" permission grants because the branch runs in the same process; `--fork-session` starts a new process without them. [cc-ses]
- **CC-142** `documented` On resume an active goal carries over, with its turn count, its timer and its token-spend baseline starting again from zero, and unexpired scheduled tasks are restored; background Bash and monitor tasks are not. [cc-ses]
- **CC-143** `documented` A resume does not bring back launch flags such as `--add-dir`, `--mcp-config`, `--plugin-dir`, `--settings` and `--fallback-model`, nor directories added with `/add-dir`; the standard settings files are read again at launch. [cc-ses]
- **CC-144** `documented` If one session is resumed in two terminals at once without forking, the messages from both end up mixed in a single transcript. [cc-ses]
- **CC-145** `documented` A session without a name gets a generated title, a brief summary of its first prompt that a background request to the small, fast model writes; that model is normally a Haiku-class model. [cc-ses]
- **CC-146** `documented` Each of the desktop app, the VS Code extension and claude.ai/code has a session list of its own, and the desktop app can also resume a session started in the CLI. [cc-ses]
- **CC-147** `documented` When the user switches git branches during a session, Claude sees the files of the new branch while the conversation history stays the same. [cc-how]
- **CC-148** `documented` When a session ended while inside a worktree and was not exited from it, resuming the session puts it back in that worktree. [cc-wt]
- **CC-149** `documented` By default, a resumed conversation continues with the system prompt it began with, even after a Claude Code upgrade; a new prompt applies after the conversation's next compaction, or to a new conversation. [cc-cache]
- **CC-150** `documented` Background sessions are run by a separate supervisor process, so they keep working after the user closes agent view or the shell or starts another interactive session. [cc-agents]
- **CC-151** `documented` Background sessions are preserved while the machine sleeps, but shutting the machine down stops the background sessions that are running. [cc-agents]
- **CC-152** `documented` The task list persists across compactions; `CLAUDE_CODE_TASK_LIST_ID` shares a named task list across sessions in `~/.claude/tasks/`. [cc-int]
- **CC-153** `documented` A git worktree gives a session its own checkout and branch while history and remote stay shared with the main checkout, so a Claude Code session working in one worktree leaves the files of sessions in other worktrees untouched. [cc-wt]

## Context and compaction

- **CC-080** `documented` Auto-compaction runs when the context window approaches capacity; `/compact` does it on demand, optionally focused on given instructions. [cc-ctx] [cc-ses]
- **CC-081** `documented` After compaction, the project-root CLAUDE.md is re-read from disk and re-injected; nested CLAUDE.md files and path-scoped rules reload when matching files are read. [cc-mem]
- **CC-082** `documented` An instruction given only in conversation can be lost at compaction; putting it in CLAUDE.md makes it persist. [cc-mem]
- **CC-083** `documented` `/context` shows what is consuming the context window, including which CLAUDE.md, rule and auto memory files loaded. [cc-ses] [cc-mem] [cc-ctx]
- **CC-084** `documented` MCP tool schemas are deferred by default: at session start only tool names and server instructions load, and full schemas load on demand through tool search. [cc-mcp] [cc-ext]
- **CC-085** `documented` Until a skill is invoked, only its description is in context; on invocation its rendered content joins the conversation as a single message that remains for later turns, and Claude Code does not read the skill file again. [cc-skills]
- **CC-086** `documented` Before the first prompt, context already holds CLAUDE.md, auto memory, the names of MCP tools and the descriptions of skills; the user's setup can add more, such as an output style or `--append-system-prompt` text. [cc-ctx]
- **CC-087** `documented` Claude Code's system prompt holds the core instructions for behaviour, tool use and response formatting, loads first and is never shown to the user. [cc-ctx]
- **CC-088** `documented` Every message makes a new API request; the model remembers nothing between requests, so Claude Code sends the full context again: the system prompt, the project context, all earlier messages and tool results, and the new message. [cc-cache] [cc-costs]
- **CC-089** `documented` Claude Code orders each request so that rarely changing content comes first: the system prompt with the tool definitions, then the project context (CLAUDE.md, auto memory, unscoped rules), then the conversation. [cc-cache]
- **CC-160** `documented` Claude Code reads the project-root CLAUDE.md and the user-level CLAUDE.md once, when the session starts; an edit during the session takes effect only after the next `/clear`, `/compact` or restart. [cc-cache]
- **CC-161** `documented` A nested CLAUDE.md or a path-scoped rule loads when Claude first reads a matching file; an edit before that takes effect, but once loaded the content is part of the conversation and a later edit does not change it. [cc-cache]
- **CC-162** `documented` Editing a file Claude has read does not change the earlier read in the history; Claude Code appends a system reminder that the file changed, and Claude reads it again if needed. [cc-cache]
- **CC-163** `documented` During a session Claude Code adds its own context alongside the user's messages: CLAUDE.md files, output style instructions, a note when a previously read file changes on disk, and the commit and pull request attribution lines. [cc-how]
- **CC-164** `documented` CLAUDE.md loads in full at session start and costs context on every request. [cc-ext]
- **CC-165** `documented` Near the context limit, Claude Code first clears older tool outputs and then summarizes the conversation if needed; requests and key code snippets are kept, while detailed early instructions may be lost. [cc-how]
- **CC-166** `documented` The summary that compaction writes keeps the requests and their intent, key technical concepts, the files examined or changed with important snippets, errors and their fixes, pending tasks and the current work; full tool outputs and intermediate reasoning are dropped. [cc-ctx]
- **CC-167** `documented` After compaction the system prompt and output style still apply; the project-root CLAUDE.md, unscoped rules, auto memory and the plan Claude wrote in plan mode are re-injected from disk; and Claude Code reads a fresh git status snapshot. [cc-ctx]
- **CC-168** `documented` Immediately after compaction, Claude Code reads again up to five files that Claude had read or edited, the most recently modified first; one larger than 5,000 tokens returns only as a reference to its path. [cc-ctx]
- **CC-169** `documented` After compaction Claude Code adds back the latest invocation of every invoked skill, cut to its first 5,000 tokens, within a shared budget of 25,000 tokens that it fills starting with the skill invoked last, so skills invoked earlier can drop out. [cc-ctx] [cc-skills]
- **CC-170** `documented` The listing of skill descriptions is not re-injected after `/compact`; only skills that were invoked are kept. [cc-ctx]
- **CC-171** `documented` Nested CLAUDE.md files and rules scoped to paths enter the message history when a file that triggers them is read, and compaction therefore summarizes them along with everything else. [cc-ctx]
- **CC-172** `documented` A "Compact Instructions" section in CLAUDE.md, or `/compact` with a focus, steers what compaction keeps. [cc-how]
- **CC-173** `documented` With no auto-compact window configured, Claude Code compacts once the conversation reaches the context limit of the model; models with a native 1M-token window compact at about 967K tokens by default, and the documentation lists further cases. [cc-model]
- **CC-174** `documented` The auto-compact window can be set per model with `/autocompact`, for all models with `autoCompactWindow`, for one launch with `--autocompact`, or with `CLAUDE_CODE_AUTO_COMPACT_WINDOW`, which overrides the command, the flag and the setting. [cc-model]
- **CC-175** `documented` In cloud sessions `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` is set by the session itself, which makes auto-compaction start before the auto-compact window is full, and a value the user gives that variable does not take effect. [cc-web]
- **CC-176** `documented` When a request would exceed the API's limit on images and PDFs, Claude Code drops a batch of the oldest ones from what it sends, and Claude can no longer see them. [cc-cache]
- **CC-177** `documented` `ENABLE_TOOL_SEARCH=auto` loads MCP tool schemas upfront while they fit within 10% of the context window, and `ENABLE_TOOL_SEARCH=false` loads all of them; without the variable, schemas load upfront behind a non-first-party `ANTHROPIC_BASE_URL`, on Google Cloud's Agent Platform models before the Claude 4.5 generation and on Microsoft Foundry deployments hosted on Azure. [cc-mcp] [cc-ctx]
- **CC-178** `documented` Claude Code warns when an MCP tool's output exceeds 10,000 tokens and limits it to 25,000 tokens by default; `MAX_MCP_OUTPUT_TOKENS` changes the limit. [cc-mcp]
- **CC-179** `documented` Hooks run outside the conversation and load nothing into context unless they return additional context. [cc-ext]
- **CC-180** `documented` An output style loads at session start and again when the style is switched, costing context on every request; nothing loads for the Default style. [cc-ext]
- **CC-181** `documented` In the skill listing, Claude Code cuts the text of `description` and `when_to_use` together at 1,536 characters. [cc-skills]
- **CC-182** `documented` `disable-model-invocation: true` keeps a skill's description out of context and stops Claude from invoking the skill on its own; the user can still invoke it. [cc-skills]
- **CC-183** `documented` The skill listing's budget scales with the model's context window, 1% by default; `skillListingBudgetFraction` scales that share and `skillListingMaxDescChars` caps each description. [cc-skills]
- **CC-184** `documented` For an enabled plugin, the name and description of each skill, agent and command Claude can invoke on its own are in context on every turn; the complete text of a skill or an agent is loaded only once it is used. [cc-plug-over]
- **CC-185** `documented` On paid plans, Fable 5.1, Fable 5, Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5.5, Sonnet 5 and Sonnet 4.6 have a 1M-token context window in Claude Code. [ctx]
- **CC-186** `documented` Opus 4.6 and Sonnet 4.6 reach the 1M-token window only through a separate 1M variant chosen with `/model`, which needs usage credits for Opus 4.6 on Pro and for Sonnet 4.6 on every plan except usage-based Enterprise. [ctx]
- **CC-187** `documented` Each time Claude uses tools, Claude Code sends a further request that carries the full conversation together with that round of tool results. [cc-costs]
- **CC-188** `documented` Background commands and background subagents go on running through compaction, and Claude Code tells Claude afterwards which of them are still active, so that it does not launch them a second time. [cc-ctx]
- **CC-189** `documented` On compaction, Claude Code runs the SessionStart hooks whose matcher is the `compact` source and puts their output into the compacted context. [cc-ctx]

## Subagents

- **CC-228** `documented` Subagents work within a single session; for separate sessions that exchange messages, the documentation points to cross-session messaging, and for sessions Claude spawns and supervises, to agent teams. [cc-sub] [cc-teams]
- **CC-090** `documented` A subagent runs in its own isolated context window and returns only a summary to the main conversation. [cc-sub]
- **CC-091** `documented` A fork inherits the full parent conversation, unlike other subagents. [cc-sub]
- **CC-092** `documented` A subagent can keep its own auto memory through a `memory` field: `~/.claude/agent-memory/<name>/` (user), `.claude/agent-memory/<name>/` (project) or `.claude/agent-memory-local/<name>/` (local); its system prompt then includes the first 200 lines or 25 KB of that `MEMORY.md`. [cc-sub]
- **CC-093** `documented` Subagent definitions come from managed settings, the `--agents` flag, `.claude/agents/` (project), `~/.claude/agents/` (user) and a plugin's `agents/` directory; when names clash, that order is the priority. [cc-sub]
- **CC-094** `documented` A subagent gets its own system prompt and basic details of the environment, such as the working directory, but not Claude Code's system prompt. [cc-sub]
- **CC-095** `documented` A subagent that is not a fork starts without the conversation history, the skills already invoked or the files Claude has read, and works from a delegation message Claude writes. [cc-sub]
- **CC-096** `documented` Such a subagent loads all levels of the CLAUDE.md hierarchy that the main conversation loads, except the built-in Explore and Plan agents, which leave out CLAUDE.md files and the git status snapshot, and a subagent whose definition sets `omitClaudeMd`, which leaves out the user, project and local CLAUDE.md files. [cc-sub]
- **CC-097** `documented` Skills named in a subagent's `skills` field are preloaded in full at launch; the subagent can still invoke other skills through the Skill tool. [cc-sub]
- **CC-098** `documented` Subagents compact with the same logic as the main conversation; their transcripts are stored in separate files and are unaffected when the main conversation compacts. [cc-sub]
- **CC-099** `documented` A skill with `context: fork` runs in a new subagent of the type named in its `agent` field, with the skill content as its prompt and without the conversation history. [cc-skills]

## Skills, plugins and MCP

- **CC-100** `documented` Skills load from the managed settings directory (enterprise), `~/.claude/skills/` (all projects), `.claude/skills/` (the repository) and nested `.claude/skills/` folders, directories added with `--add-dir`, enabled plugins, and the claude.ai account. [cc-skills]
- **CC-101** `documented` Personal skills in `~/.claude/skills/` do not load in Cowork or cloud sessions unless enabled for the claude.ai account. [cc-skills]
- **CC-102** `documented` In terminal sessions signed in with a claude.ai account, Claude Code downloads the account's skills into `~/.claude/skills/synced/` at session start and checks for changes about every 10 minutes; this needs Claude Code v2.1.273 or later. [cc-skills]
- **CC-103** `documented` MCP servers are configured per local scope or user scope in `~/.claude.json`, or per project in `.mcp.json` shared through git. [cc-mcp]
- **CC-104** `documented` Synced skills are only downloaded, never uploaded: an edit under `~/.claude/skills/synced/` is not saved to the account, and a later sync can overwrite it. [cc-skills]
- **CC-105** `documented` Setting `syncClaudeAiSkills` to `false` in the user settings stops the sync on that machine. [cc-skills]
- **CC-106** `documented` Account skills do not sync in a session whose credential is not a sign-in that `/login` stored, for example one using an API key, or in a session that does not fetch feature flags, for example one on Amazon Bedrock. [cc-skills]
- **CC-107** `documented` When a claude.ai subscription login is the active authentication, MCP servers added in claude.ai (connectors) are available in Claude Code. [cc-mcp]
- **CC-108** `documented` `disableClaudeAiConnectors` turns off the claude.ai connectors Claude Code fetches itself; it does not act on connectors that a cloud host or the desktop app delivers. [cc-mcp]
- **CC-109** `documented` When an MCP server is defined in several places, Claude Code connects once, using the whole entry from the highest-precedence source: local scope, project scope, user scope, plugin-provided servers, then claude.ai connectors. [cc-mcp]
- **CC-126** `documented` In terminal sessions signed in with a claude.ai account, Claude Code syncs every plugin turned on for the account or by the organization, listed under the ID `<name>@synced`; this needs Claude Code v2.1.273 or later, and plugins installed in Claude Code are not added to the account. [cc-plug]

## Output styles

- **CC-130** `documented` Output styles are sets of instructions that determine how Claude behaves, sounds and formats its answers throughout a session; apart from Default, the built-in styles are Proactive, Concise, Explanatory and Learning. [cc-styles]
- **CC-131** `documented` Each request carries the instructions of the active output style; a custom style drops Claude Code's built-in software engineering instructions unless `keep-coding-instructions` is `true`. [cc-styles]
- **CC-132** `documented` Custom output styles are Markdown files in `~/.claude/output-styles` (user), `.claude/output-styles` (project) or `.claude/output-styles` inside the managed settings directory. [cc-styles]
- **CC-133** `documented` Choosing a style with `/output-style` or a menu saves it to `.claude/settings.local.json`; the `outputStyle` field in a settings file also sets it. [cc-styles]
- **CC-134** `documented` A style switched mid-session applies from the next message; before v2.1.251 it applied only after `/clear` or in a new session. [cc-styles]
- **CC-135** `documented` Output styles affect the main conversation and forks, but no other subagent, since those run their own system prompt. [cc-styles]

## Relationship to the Claude app

- **CC-110** `documented` A cloud session runs Claude Code on cloud infrastructure instead of the user's machine, keeps running after the laptop is closed and can be started from claude.ai/code, the Claude mobile app, the desktop app, the terminal with `claude --cloud`, or a routine. [cc-web]
- **CC-111** `documented` From the CLI, handoff is one-way: a cloud session can be pulled into the terminal with `claude --teleport`, but an existing terminal session cannot be pushed to the cloud. [cc-web]
- **CC-112** `documented` Cloud sessions do not load plugins installed on the user's machine, nor plugins that a repository's `.claude/settings.json` turns on. [cc-plug] [cc-cloud-env]
- **CC-113** `documented` Cowork projects are not available in Claude Code; the separate redesigned projects (beta) are documented for Claude Code users. [cw-proj] [cc-proj]
- **CC-114** `inferred` Claude Code does not read the Claude app's account or project memory; its persistent knowledge comes from CLAUDE.md files and its own auto memory. Basis: CC-001, CC-044; no page states it directly.
- **CC-115** `documented` Every Claude Code interface has the same agentic loop, tools and capabilities; the interfaces differ in where the code runs and how the user works with it. [cc-how]
- **CC-116** `documented` The Claude desktop app includes Claude Code in its Code tab, so the CLI does not need to be installed separately. [cc-over]
- **CC-117** `documented` The desktop app runs the same engine as the CLI; both can run at once on one project, each has a session list of its own, and a CLI session can be brought into the desktop app. [cc-desk]
- **CC-118** `documented` The desktop app and the CLI read the same configuration files, including CLAUDE.md and CLAUDE.local.md and the MCP servers in `~/.claude.json` or `.mcp.json`. [cc-desk]
- **CC-119** `documented` When the desktop app takes over a CLI session with `/resume`, it continues that session itself and not a copy, so `claude --resume` in the terminal can still find it. [cc-desk]

## Artifacts

- **CC-220** `documented` Claude Code can publish artifacts on Pro, Max, Team and Enterprise, only from a session signed in to a claude.ai account; sessions using an API key, a gateway token or a cloud-provider credential cannot publish. [cc-art] [art]
- **CC-221** `documented` An artifact published from Claude Code is a live page at a private URL on claude.ai that stays private until shared and updates in place each time Claude publishes again to the same URL; each publish becomes a version. [cc-art] [art]
- **CC-222** `documented` Another session updates an existing artifact only when it is given the artifact's URL or the artifact is attached with `/artifacts`; otherwise it creates a new artifact. [cc-art]
- **CC-223** `documented` `/artifacts` lists all artifacts the user owns and all that are shared with them, taken from the claude.ai account, so it also works in a new session and after `/clear`; it needs v2.1.208 or later. [cc-art]
- **CC-224** `documented` Artifacts published from Claude Code are listed in the user's gallery at claude.ai/code/artifacts. [cc-art]
- **CC-225** `documented` A published artifact can call only connectors of the claude.ai account, each through the viewer's own connection; local MCP servers configured in Claude Code can supply data while the page is built, but the published page cannot call them. [cc-art]
- **CC-226** `documented` From Claude Code, Claude can start an artifact from the Slides, Design or Docs templates of the claude.ai account, with `/slides` and `/design` from v2.1.265; Claude Docs is available to Claude Code as a claude.ai connector. [cc-art] [art]
- **CC-227** `documented` A user turns artifacts off for their own sessions with `"enableArtifact": false` in settings, `CLAUDE_CODE_DISABLE_ARTIFACT=1` or `Artifact` in `permissions.deny`; a project's settings can turn them off but not back on. [cc-art]
- **CC-258** `documented` From v2.1.228, Claude Code watches each artifact its session published, and a comment that an editor sends to Claude reaches the session at once; where the permission mode allows posting without asking, Claude replies or edits the artifact on its own, otherwise it waits for the user, and in plan mode it pauses. [cc-art]
- **CC-259** `documented` Claude Code stops replying on its own to an artifact after 60 sent comments or thread activations on it within an hour; `/tasks` lists each watched artifact, and a watch Claude Code started itself can end after several hours without activity. [cc-art]
- **CC-260** `documented` A published artifact can offer viewers a file it generates only through the downloads capability, which claude.ai enables per account and Claude declares when publishing, because the viewer blocks downloads the page starts itself. [cc-art]

## Desktop app

- **CC-200** `documented` In the desktop app's Code tab every conversation is its own session, with a history and a project folder that no other session shares, and several sessions can run in parallel. [cc-desk]
- **CC-201** `documented` A desktop Code session runs in one of four environments: Local, Cloud, SSH (a remote machine) or WSL on Windows. [cc-desk]
- **CC-202** `documented` The desktop app's **Open in > Cloud** continues a Code session as a cloud session with the conversation carried over as a summary; sessions over SSH or in WSL cannot be moved this way. [cc-desk]
- **CC-203** `documented` In the desktop app's Code tab, the **worktree** option for a Git repository gives a session its own isolated copy of the project in a Git worktree, so its changes stay out of other sessions until they are committed. [cc-desk]
- **CC-204** `documented` In the desktop app, Claude can list the user's other Code tab sessions, read what each one has been doing and pass messages between them. [cc-desk]
- **CC-205** `documented` That desktop surface shows Claude only sessions the desktop app runs itself, local, SSH and WSL Code tab sessions, and not cloud sessions or sessions started from the terminal or the VS Code extension. [cc-desk]
- **CC-206** `documented` A message between desktop sessions appears in the receiving session as a card with the sending session's title; a session busy with a task reads it once its current work is done. [cc-desk]

## Cloud sessions

- **CC-190** `documented` Cloud sessions can be used on the Pro, Max and Team plans, and on Enterprise by users who have a premium seat or a Chat + Claude Code seat. [cc-web]
- **CC-247** `documented` The Enterprise plan article gives Enterprise a single seat type that includes Claude Code and Cowork, and says organizations on Chat and Chat + Claude Code seats, or on Standard and Premium seats, cannot keep those seats past their next contract renewal; the cloud sessions page still names only premium seats and Chat + Claude Code seats for Enterprise. [ent] [cc-web]
- **CC-191** `documented` `claude --cloud` creates a new cloud session for the current repository, one repository at a time; the cloud VM clones the current directory's GitHub remote at the current branch rather than the local checkout, unless Claude Code uploads the local repository as a bundle. [cc-web]
- **CC-192** `documented` Teleporting fetches and checks out the cloud session's branch and loads its full conversation history into the terminal; the terminal gets its own copy, and new local work does not appear in the cloud session. [cc-web]
- **CC-193** `documented` A cloud session starts from a fresh clone of the repository: what is committed is available, what is installed or configured only on the user's machine is not. [cc-cloud-env]
- **CC-194** `documented` A cloud session has the repository's CLAUDE.md, its `.claude/rules/` and the skills, agents and commands under its `.claude/`, because they are part of the clone. [cc-cloud-env]
- **CC-195** `documented` In a cloud session with one repository, the hooks and permission rules of its `.claude/settings.json` and the MCP servers of its `.mcp.json` apply; a session with several repositories starts in the directory above the clones and reads none of them. [cc-cloud-env]
- **CC-196** `documented` A cloud session does not have the user's `~/.claude/CLAUDE.md`, the skills, agents and commands under `~/.claude/`, plugins enabled only in user settings, or MCP servers added at local or user scope. [cc-cloud-env]
- **CC-197** `documented` When a cloud session has been inactive for a few minutes, its VM pauses and keeps its files, and a paused VM may be reclaimed later. [cc-cloud-env]
- **CC-198** `documented` When a cloud session's VM has been reclaimed, reopening the session provisions a fresh VM that restores the conversation history but not background work such as subagents or shell commands. [cc-web]
- **CC-199** `documented` Packages Claude installs during a cloud session do not carry over to other sessions; a setup script, whose result the environment cache keeps, makes packages available at the start of every session. [cc-cloud-env]
- **CC-248** `documented` In an Anthropic-hosted environment each cloud session gets a new VM with Ubuntu 24.04 on x86_64, whatever the user's own system, holding a clone of the repository and preinstalled common toolchains. [cc-cloud-env]
- **CC-249** `documented` A cloud environment has one network access level: **None** (no outbound connections over the session network), **Trusted** (the default allowlist, such as package registries, GitHub and cloud SDKs), **Full** (any domain) or **Custom** (the user's own allowlist, optionally with the defaults). [cc-cloud-env]
- **CC-250** `documented` Cloud sessions in Anthropic-hosted environments run within approximate ceilings of 4 vCPUs, 16 GB of RAM and 30 GB of disk, which may change over time. [cc-cloud-env]
- **CC-251** `documented` Each cloud session runs inside a cloud environment, a saved configuration of network access, environment variables and setup script; a user who has none gets a **Default** environment with **Trusted** access set up during onboarding, which on some plans the user is asked to create. [cc-web]
- **CC-252** `documented` Cloud sessions reach GitHub through the Claude GitHub App, which covers public repositories and private ones it is installed on, or through `/web-setup`, which hands the local `gh` token to the Claude account and covers what that token can reach. [cc-web]
- **CC-253** `documented` Anthropic-hosted environments restrict network access by default and let it be turned off, yet even without it Claude Code keeps talking to the Anthropic API, which the documentation notes may let data leave the VM. [cc-web]

## Remote Control

- **CC-210** `documented` Remote Control links the Claude app on iOS and Android, or claude.ai/code, to a Claude Code session running on the user's own machine. [cc-rc]
- **CC-211** `documented` A Remote Control session runs on the user's machine and the web and mobile interfaces only give a view into it, so the computer must stay on and the `claude` process must keep running. [cc-rc]
- **CC-212** `documented` With Remote Control, connected devices stay in sync on the conversation and on how subagents and dynamic workflows progress, so the user can send messages from the terminal, a browser or a phone. [cc-rc]
- **CC-213** `documented` Connected devices show compaction progress and where the conversation was compacted, and `/clear` resets the conversation on them too. [cc-rc]
- **CC-214** `documented` As long as Remote Control is connected, Anthropic servers store the session transcript, with the messages, Claude's responses and the tool activity. [cc-rc]
- **CC-215** `documented` Remote Control can be used on the Pro, Max, Team and Enterprise plans but not with API keys, and on Team and Enterprise an Owner first has to switch it on in the Claude Code admin settings. [cc-rc]
- **CC-216** `documented` The `disableRemoteControl` setting turns Remote Control off entirely, and organizations with Zero Data Retention or the HIPAA configuration cannot enable it. [cc-rc]
- **CC-245** `documented` Trusted Devices (beta), offered on Pro, Max, Team and Enterprise and off by default, allows a Remote Control session to be viewed or steered from claude.ai, the mobile apps or Claude Desktop only from an enrolled device and with a sign-in no older than 18 hours, renewed with a biometric or passkey check; on Team and Enterprise an Owner turns it on in Organization settings > Capabilities > Remote sessions, and on Pro and Max the user turns it on in their own settings. [cc-rc]
- **CC-246** `documented` Trusted Devices covers Remote Control in Claude Code and Cowork but not regular chat, Claude Code in the terminal or API use; the machine running Claude Code gets its credential when the developer signs in to the CLI. [cc-rc]
- **CC-254** `documented` A Remote Control session makes only outbound HTTPS requests and opens no inbound ports: it registers with the Anthropic API and polls it for work. [cc-rc]
- **CC-255** `documented` Outside server mode, each Claude Code process carries one Remote Control session at a time. [cc-rc]
- **CC-256** `documented` In server mode (`claude remote-control`) sessions share the working directory by default and can collide when they edit the same files; `--spawn worktree` gives each on-demand session its own git worktree. [cc-rc]
- **CC-257** `documented` The CLI starts Remote Control in three ways: `claude remote-control` (server mode), the `--remote-control` flag on an interactive session, or `/remote-control` (`/rc`) inside a running session, which brings the conversation so far along. [cc-rc]

## Sessions working together

- **CC-230** `documented` With cross-session messaging, Claude can send a message from one of the user's Claude Code sessions to another, on its own or when asked; a message is plain text that Claude writes, never the sender's conversation history or files. [cc-msg]
- **CC-231** `documented` Cross-session messaging works without any setup once a session meets its requirements: on macOS, Linux and WSL 2 it needs v2.1.224 of Claude Code or a later one, on native Windows v2.1.234 or a later one. [cc-msg]
- **CC-232** `documented` A session can reach its subagents, its own agent-team teammates and the user's other sessions on the same machine, background sessions included; while it is connected to Remote Control, it can also reach the user's cloud sessions and Remote Control sessions on other machines. [cc-msg]
- **CC-233** `documented` A message to a session on the same machine travels over a per-session socket, or a named pipe on native Windows, and never through Anthropic servers; a message to a session on another machine or in the cloud travels through Anthropic servers. [cc-msg]
- **CC-234** `documented` A message sent beyond the machine from a session that is not connected to Remote Control arrives without a reply address, so the receiving Claude cannot answer it. [cc-msg]
- **CC-235** `documented` In an active turn the receiving Claude reads a message between two tool calls, so a tool that is running is never interrupted; in an idle session the message starts a new turn. [cc-msg]
- **CC-236** `documented` Claude Code tells the receiving Claude that a message came from another session, not from the user: it cannot answer a permission prompt, the receiving Claude is told not to alter permission settings, CLAUDE.md or other configuration at another session's request, and commands in its text are not run. [cc-msg]
- **CC-237** `documented` `crossSessionInbound` set to `accept`, `hold` or `refuse` decides what a session does with incoming messages; with no value set, delivery depends on whether the sending and the receiving session bypass permission prompts. [cc-msg]
- **CC-238** `documented` A delivered message counts toward usage like a prompt the user types. [cc-msg]
- **CC-239** `documented` Agent teams are experimental and off by default, turned on with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`; one session leads, and the teammates are separate Claude Code instances, each with a context window of its own, that message each other directly and share a task list. [cc-teams]
- **CC-240** `documented` A teammate starts with the same project context as a regular session, such as CLAUDE.md, MCP servers and skills, plus the lead's spawn prompt, but not the lead's conversation history. [cc-teams]
- **CC-241** `documented` A teammate starts in the permission mode of the lead, unless that mode is `dontAsk`, and its permission prompts show up in the lead's session. [cc-teams]
- **CC-242** `documented` Each session has one team, which belongs to that session alone: no team is shared across sessions, teammates cannot start teams of their own, and neither `/resume` nor `/rewind` brings in-process teammates back. [cc-teams]
- **CC-243** `documented` A team's config under `~/.claude/teams/` is removed when the session ends, while its task list under `~/.claude/tasks/` stays on the machine, is never uploaded and is kept for resumed sessions. [cc-teams]
- **CC-244** `documented` By default, in a git repository, a background session dispatched from agent view or started with `claude --bg` moves into a worktree of its own under `.claude/worktrees/` before it edits files, so parallel sessions all read one checkout while each writes to its own; outside a git repository, background sessions write to the working directory and are not isolated from each other; the documentation lists cases where a session skips its worktree, such as one that was moved to the background or that already sits in a linked worktree. [cc-agents]

## Sources

[art]: https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them
[cc-agents]: https://code.claude.com/docs/en/agent-view
[cc-art]: https://code.claude.com/docs/en/artifacts
[cc-cache]: https://code.claude.com/docs/en/prompt-caching
[cc-cloud-env]: https://code.claude.com/docs/en/cloud-environments
[cc-costs]: https://code.claude.com/docs/en/costs
[cc-ctx]: https://code.claude.com/docs/en/context-window
[cc-desk]: https://code.claude.com/docs/en/desktop
[cc-ext]: https://code.claude.com/docs/en/features-overview
[cc-how]: https://code.claude.com/docs/en/how-claude-code-works
[cc-int]: https://code.claude.com/docs/en/interactive-mode
[cc-proj]: https://code.claude.com/docs/en/claude-projects
[cc-man]: https://code.claude.com/docs/en/managed-settings
[cc-mcp]: https://code.claude.com/docs/en/mcp
[cc-mem]: https://code.claude.com/docs/en/memory
[cc-model]: https://code.claude.com/docs/en/model-config
[cc-msg]: https://code.claude.com/docs/en/cross-session-messaging
[cc-over]: https://code.claude.com/docs/en/overview
[cc-perm]: https://code.claude.com/docs/en/permissions
[cc-plug]: https://code.claude.com/docs/en/plugins/install
[cc-plug-over]: https://code.claude.com/docs/en/plugins/overview
[cc-rc]: https://code.claude.com/docs/en/remote-control
[cc-ses]: https://code.claude.com/docs/en/sessions
[cc-set]: https://code.claude.com/docs/en/settings
[cc-skills]: https://code.claude.com/docs/en/skills
[cc-styles]: https://code.claude.com/docs/en/output-styles
[cc-sub]: https://code.claude.com/docs/en/sub-agents
[cc-teams]: https://code.claude.com/docs/en/agent-teams
[cc-web]: https://code.claude.com/docs/en/claude-code-on-the-web
[cc-wt]: https://code.claude.com/docs/en/worktrees
[ctx]: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
[cw-proj]: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
[ent]: https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan

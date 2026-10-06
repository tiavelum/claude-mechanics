# 09 Claude Code

Prefix: CC · Scope: memory, instruction files, settings, sessions and context in Claude Code (terminal, desktop Code tab, IDE, cloud sessions), and how it relates to the Claude app · Last checked: 2026-10-06

## Memory model

- **CC-001** `documented` Each Claude Code session begins with a fresh context window; two mechanisms carry knowledge across sessions: CLAUDE.md files (written by the user) and auto memory (written by Claude). [cc-mem]
- **CC-002** `documented` Both CLAUDE.md and auto memory are loaded at the start of every conversation and are treated as context, not as enforced configuration. [cc-mem]
- **CC-003** `documented` To block an action regardless of what Claude decides, the documentation points to a PreToolUse hook rather than CLAUDE.md. [cc-mem]
- **CC-004** `documented` The more specific and concise the instructions, the more consistently Claude follows them. [cc-mem]
- **CC-005** `documented` The documentation assigns technical enforcement to settings, which the client enforces regardless of what Claude decides, and behavioural guidance to CLAUDE.md, which is not a hard enforcement layer. [cc-mem]
- **CC-006** `documented` Permission rules are enforced by Claude Code, not by the model; instructions in a prompt or in CLAUDE.md do not change what Claude Code allows. [cc-perm]
- **CC-007** `documented` CLAUDE.md content is delivered as a user message after the system prompt, not as part of the system prompt, and strict compliance with it is not guaranteed. [cc-mem]
- **CC-008** `documented` Claude Code's system prompt is not published; the documentation points to CLAUDE.md files or the `--append-system-prompt` flag for standing instructions. [cc-set]

## Instruction files

- **CC-010** `documented` A managed policy CLAUDE.md applies to all users on a machine: `/Library/Application Support/ClaudeCode/CLAUDE.md` on macOS, `/etc/claude-code/CLAUDE.md` on Linux and WSL, `C:\Program Files\ClaudeCode\CLAUDE.md` on Windows. [cc-mem]
- **CC-011** `documented` `~/.claude/CLAUDE.md` holds the user's personal instructions for all projects. [cc-mem]
- **CC-012** `documented` `./CLAUDE.md` or `./.claude/CLAUDE.md` holds the project's shared instructions. [cc-mem]
- **CC-013** `documented` `./CLAUDE.local.md` holds personal project-specific instructions; the documentation advises adding it to `.gitignore`. [cc-mem]
- **CC-014** `documented` CLAUDE.md and CLAUDE.local.md files in the working directory and every directory above it load at launch. [cc-mem]
- **CC-015** `documented` All discovered files are concatenated rather than overriding each other, ordered from the filesystem root down, so instructions closer to the working directory are read last. [cc-mem]
- **CC-016** `documented` Within one directory, CLAUDE.local.md is appended after CLAUDE.md. [cc-mem]
- **CC-017** `documented` CLAUDE.md files in subdirectories load on demand, when Claude reads files in those subdirectories. [cc-mem]
- **CC-018** `documented` A managed policy CLAUDE.md cannot be excluded by individual settings. [cc-mem]
- **CC-019** `documented` A gitignored CLAUDE.local.md exists only in the worktree where it was created. [cc-mem]
- **CC-020** `documented` Block-level HTML comments in CLAUDE.md are stripped before the content enters Claude's context; comments inside code blocks are kept. [cc-mem]
- **CC-021** `documented` By default, Claude reads `AGENTS.md` only when there is no CLAUDE.md, `.claude/CLAUDE.md` or CLAUDE.local.md in the working directory or above it; reading `AGENTS.md` directly needs Claude Code v2.1.277 or later, and a setting can load both. [cc-mem]
- **CC-022** `documented` The user-level `~/.claude/CLAUDE.md`, the managed CLAUDE.md and `.claude/rules/` files do not count for that rule and keep loading alongside AGENTS.md. [cc-mem]
- **CC-023** `documented` The CLAUDE.md scopes load from broadest to most specific (managed policy, user, project, local), so a project instruction appears in context after a user instruction. [cc-mem]
- **CC-024** `documented` The **Project instructions** option in `/config` chooses which instruction files load: `claude-md-or-agents-md` (the default), `claude-md-and-agents-md`, `claude-md` or `managed-only`. [cc-mem]
- **CC-025** `documented` CLAUDE.md files in directories added with `--add-dir` do not load by default; `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` loads them. [cc-mem]
- **CC-026** `documented` Claude Code loads a CLAUDE.md file of up to 4 MiB in full and skips a larger one; the 200-line and 25 KB limit applies only to `MEMORY.md`. [cc-mem]
- **CC-027** `documented` The documentation advises keeping each CLAUDE.md under 200 lines, because longer files consume more context and reduce adherence. [cc-mem]
- **CC-028** `conflicting` What Claude does with two CLAUDE.md instructions that contradict each other: the memory page says Claude may pick one arbitrarily, while the extension overview says Claude uses judgment to reconcile them. [cc-mem] [cc-ext]
- **CC-029** `documented` `/init` generates a starting CLAUDE.md from the codebase and, when a CLAUDE.md already exists, suggests improvements instead of overwriting it. [cc-mem]
- **CC-120** `documented` `/memory` lists the CLAUDE.md, CLAUDE.local.md and other memory file locations across user and project scopes, toggles auto memory and can open the auto memory folder. [cc-mem]

## Imports and rules

- **CC-030** `documented` CLAUDE.md can import other files with `@path/to/file`; relative paths resolve from the importing file, and imports can nest up to four hops deep. [cc-mem]
- **CC-031** `documented` Imported files are expanded and loaded into context at launch. [cc-mem]
- **CC-032** `documented` The first time a project's CLAUDE.md imports files from outside the working directory, Claude Code asks for approval; if declined, those imports stay disabled. [cc-mem]
- **CC-033** `documented` Imports in user-scope files such as `~/.claude/CLAUDE.md` load without that dialog, except in Cowork sessions on the desktop, which skip imports pointing outside the session's working directory. [cc-mem]
- **CC-034** `documented` Instructions can be split into topic files in `.claude/rules/`; rules without a `paths` field load at launch like CLAUDE.md. [cc-mem]
- **CC-035** `documented` A rule with `paths` frontmatter loads only when Claude reads, writes or edits a file matching its glob patterns. [cc-mem]
- **CC-036** `documented` Personal rules in `~/.claude/rules/` apply to every project and load before project rules; neither set overrides the other. [cc-mem]
- **CC-037** `documented` The `claudeMdExcludes` setting skips specific CLAUDE.md or rule files by path or glob; it can be set in any settings layer, and the arrays merge across layers. [cc-mem]

## Auto memory

- **CC-040** `documented` Auto memory is on by default in local sessions; in self-hosted environments it is off by default, except in Claude Tag sessions. [cc-mem]
- **CC-041** `documented` Auto memory is toggled in `/memory`, which saves `autoMemoryEnabled` to `~/.claude/settings.json`; a project can turn it off in its own settings, and `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` turns it off as well. [cc-mem]
- **CC-042** `documented` Each project gets an auto memory directory at `~/.claude/projects/<project>/memory/`, where `<project>` is derived from the git repository. [cc-mem]
- **CC-043** `documented` All worktrees and subdirectories of the same repository share one auto memory directory; outside a git repository, the project root is used. [cc-mem]
- **CC-044** `documented` Auto memory is machine-local and not shared across machines or cloud environments. [cc-mem]
- **CC-045** `documented` The first 200 lines or first 25 KB of `MEMORY.md`, whichever comes first, load at the start of every conversation; topic files load on demand. [cc-mem]
- **CC-046** `documented` When the user asks Claude to remember something, Claude saves it to auto memory; to put it in CLAUDE.md instead, the user asks for that explicitly. [cc-mem]
- **CC-047** `documented` `autoMemoryDirectory` moves auto memory to another location; it is read from any settings scope and must be an absolute path or start with `~/`. [cc-mem]
- **CC-048** `documented` Old session transcripts are deleted after the retention period, but auto memory files are excluded from that cleanup. [cc-mem]
- **CC-049** `documented` The main conversation's auto memory is not loaded into subagents, except forks, which inherit the parent conversation. [cc-mem]
- **CC-050** `documented` Auto memory cannot be turned on in background sessions or in sessions started by another Claude Code session. [cc-mem]
- **CC-051** `documented` Claude saves four kinds of auto memory notes, recorded in a `type` frontmatter field: `user` (role, expertise, working preferences), `feedback` (corrections and confirmed approaches), `project` (ongoing work, deadlines and decisions not derivable from the code or git history) and `reference` (where to find information outside the project). [cc-mem]
- **CC-052** `documented` Claude skips anything it can derive from the codebase and anything the CLAUDE.md files already say, and does not save something in every session. [cc-mem]
- **CC-053** `documented` After Claude writes to `MEMORY.md`, Claude Code checks it against the 200-line and 25 KB limits and reminds Claude to shorten it when it is near one; content past a limit is dropped on the next load. [cc-mem]
- **CC-054** `documented` In the redesigned projects (beta), project memory files are separate from the auto memory Claude Code keeps on the user's machine, although both use a `MEMORY.md` index. [cc-proj]

## Settings

- **CC-060** `documented` Settings precedence, highest first: managed settings, command line (`--settings`), project local (`.claude/settings.local.json`), shared project (`.claude/settings.json`), user (`~/.claude/settings.json`). [cc-set]
- **CC-061** `documented` A key set at a higher level overrides the same key set lower down. [cc-set]
- **CC-062** `documented` Managed settings can come from a managed settings file, from MDM or OS policy, or from the claude.ai console. [cc-set] [cc-man]
- **CC-063** `documented` The terminal, the VS Code and JetBrains extensions and the desktop app's local sessions on one computer read the same settings files. [cc-set] [cc-plug]
- **CC-064** `documented` Settings are JSON keys that control behaviour such as the starting model, what can run without asking, which files cannot be read, terminal appearance and what an organization enforces. [cc-set]
- **CC-065** `documented` `~/.claude/settings.json` applies to the user in every project on the machine, `.claude/settings.json` to everyone working in the folder that contains it and is meant to be committed, and `.claude/settings.local.json` to the user in one project only; Claude Code keeps the local file out of git when it creates it. [cc-set]
- **CC-066** `documented` Nothing a user sets overrides managed settings, apart from a few security-sensitive keys for which a stricter value from a lower level is honoured. [cc-set]
- **CC-067** `documented` Environment variables are not a level in the settings precedence; whether a shell variable or a settings key applies is decided for each pair. [cc-set]
- **CC-068** `documented` When the same list key, such as `permissions.allow`, is set in several settings files, Claude Code combines the lists instead of choosing one. [cc-set]
- **CC-069** `documented` Claude Code watches the settings files and applies most edits, including permissions, hooks and credential helpers, to a running session without a restart. [cc-set]
- **CC-121** `documented` Besides the settings files, Claude Code keeps `~/.claude.json`, which it writes itself; it holds the sign-in session, MCP server configurations and per-project state such as trust decisions. [cc-set]
- **CC-122** `documented` When a feature exists at several levels, CLAUDE.md files add up, skills and subagents override by name, MCP servers override by name (local over project over user) and all hooks fire. [cc-ext]
- **CC-123** `documented` A cloud session does not read user or project local settings; a managed settings file or MDM profile on the user's device does not reach it, while the organization's server-managed settings do. [cc-set]
- **CC-124** `documented` In the browser at claude.ai/code, `/config` opens the Claude Code section of the claude.ai settings; a cloud session's setting is changed through an environment variable of its environment or, with one repository, through the committed `.claude/settings.json`. [cc-set]
- **CC-125** `documented` Plugins install at user scope (every project on the computer), project scope (everyone in the repository, through the committed `.claude/settings.json`) or local scope (the user in that repository only). [cc-plug-over]

## Sessions

- **CC-070** `documented` Sessions are saved continuously as JSONL transcripts at `~/.claude/projects/<project>/<session-id>.jsonl`, where `<project>` is the working directory path with non-alphanumeric characters replaced by `-`; the format is internal and may change. [cc-ses]
- **CC-071** `documented` `claude --continue` reopens the most recent conversation in the current directory; `claude --resume` opens a picker or a named session. [cc-ses]
- **CC-072** `documented` `/clear` starts a fresh, empty context and saves the previous conversation, which can be resumed with `/resume` or, in the same process, from the rewind menu. [cc-ses]
- **CC-073** `documented` `/branch` and `--fork-session` copy the conversation so far into a new session ID and leave the original unchanged. [cc-ses] [cc-how]
- **CC-074** `documented` Resuming from a terminal with `claude --continue`, `claude --resume <session-id>` or a uniquely matching name, without `-p`, restores the session's permission mode except in listed cases; the session picker and `/resume` do not restore it. [cc-ses]
- **CC-075** `documented` Transcripts are kept for 30 days by default, configurable with `cleanupPeriodDays`; `CLAUDE_CONFIG_DIR` moves storage off `~/.claude`. [cc-ses]
- **CC-076** `documented` On Pro or Max, resuming a session inactive for over about an hour and over 100,000 tokens offers to compact the history first. [cc-ses]
- **CC-077** `documented` A session is a saved conversation tied to a project directory, stored locally as the user works. [cc-ses]
- **CC-078** `documented` Resuming with `claude --continue` or `claude --resume` reopens a session under the same session ID and appends new messages to the existing conversation. [cc-how]
- **CC-079** `documented` A resumed session restores the full conversation history, including tool calls and results; a tool that was still running when the previous process ended does not finish or run again. [cc-ses]
- **CC-140** `documented` A resumed session continues on the model it was using, unless that model is retired or not allowed by `availableModels`, or a `--model` flag or an `ANTHROPIC_MODEL`-family variable picks one at launch. [cc-ses]
- **CC-141** `documented` `/branch` keeps "Allow for this session" permission grants because the branch runs in the same process; `--fork-session` starts a new process without them. [cc-ses]
- **CC-142** `documented` On resume, an active goal carries over with its turn count, timer and token-spend baseline reset, and unexpired scheduled tasks are restored; background Bash and monitor tasks are not. [cc-ses]
- **CC-143** `documented` Launch flags such as `--mcp-config`, `--settings`, `--plugin-dir`, `--fallback-model` and `--add-dir` are not restored on resume, nor are directories added with `/add-dir`; the standard settings files are read again at launch. [cc-ses]
- **CC-144** `documented` Resuming the same session in two terminals without forking interleaves the messages from both into one transcript. [cc-ses]
- **CC-145** `documented` An unnamed session gets a generated title, a short summary of the first prompt written by a background request to the small, fast model, normally a Haiku-class model. [cc-ses]
- **CC-146** `documented` The desktop app, claude.ai/code and the VS Code extension each keep their own session list, and the desktop app can also resume a CLI session. [cc-ses]
- **CC-147** `documented` When the user switches git branches during a session, Claude sees the new branch's files while the conversation history stays the same. [cc-how]
- **CC-148** `documented` Resuming a session that ended inside a worktree without exiting it returns the session to that worktree. [cc-wt]
- **CC-149** `documented` A resumed conversation keeps the system prompt it started with by default, also after a Claude Code upgrade; the new prompt takes effect once the conversation is compacted, or in a new conversation. [cc-cache]
- **CC-150** `documented` Background sessions are run by a separate supervisor process, so they keep working after the user closes agent view or the shell or starts another interactive session. [cc-agents]
- **CC-151** `documented` Background sessions are preserved while the machine sleeps, but shutting the machine down stops the background sessions that are running. [cc-agents]
- **CC-152** `documented` The task list persists across compactions; `CLAUDE_CODE_TASK_LIST_ID` shares a named task list across sessions in `~/.claude/tasks/`. [cc-int]

## Context and compaction

- **CC-080** `documented` Auto-compaction runs when the context window approaches capacity; `/compact` does it on demand, optionally focused on given instructions. [cc-ctx] [cc-ses]
- **CC-081** `documented` After compaction, the project-root CLAUDE.md is re-read from disk and re-injected; nested CLAUDE.md files and path-scoped rules reload when matching files are read. [cc-mem]
- **CC-082** `documented` An instruction given only in conversation can be lost at compaction; putting it in CLAUDE.md makes it persist. [cc-mem]
- **CC-083** `documented` `/context` shows what is consuming the context window, including which CLAUDE.md, rule and auto memory files loaded. [cc-ses] [cc-mem] [cc-ctx]
- **CC-084** `documented` MCP tool schemas are deferred by default: at session start only tool names and server instructions load, and full schemas load on demand through tool search. [cc-mcp] [cc-ext]
- **CC-085** `documented` Before a skill is invoked only its description is in context; once invoked, its rendered content enters the conversation as one message that stays across later turns, and Claude Code does not re-read the skill file. [cc-skills]
- **CC-086** `documented` Before the user types anything, CLAUDE.md, auto memory, MCP tool names and skill descriptions load into context; the user's setup can add more, such as an output style or `--append-system-prompt` text. [cc-ctx]
- **CC-087** `documented` Claude Code's system prompt holds the core instructions for behaviour, tool use and response formatting, loads first and is never shown to the user. [cc-ctx]
- **CC-088** `documented` Every message makes a new API request; the model remembers nothing between requests, so Claude Code sends the full context again: the system prompt, the project context, all earlier messages and tool results, and the new message. [cc-cache] [cc-costs]
- **CC-089** `documented` Claude Code orders each request so that rarely changing content comes first: the system prompt with the tool definitions, then the project context (CLAUDE.md, auto memory, unscoped rules), then the conversation. [cc-cache]
- **CC-160** `documented` The project-root and user-level CLAUDE.md files are read once at session start; an edit made mid-session applies only after the next `/clear`, `/compact` or restart. [cc-cache]
- **CC-161** `documented` A nested CLAUDE.md or a path-scoped rule loads when Claude first reads a matching file; an edit before that takes effect, but once loaded the content is part of the conversation and a later edit does not change it. [cc-cache]
- **CC-162** `documented` Editing a file Claude has read does not change the earlier read in the history; Claude Code appends a system reminder that the file changed, and Claude reads it again if needed. [cc-cache]
- **CC-163** `documented` During a session Claude Code adds its own context alongside the user's messages: CLAUDE.md files, output style instructions, a note when a previously read file changes on disk, and the commit and pull request attribution lines. [cc-how]
- **CC-164** `documented` CLAUDE.md loads in full at session start and costs context on every request. [cc-ext]
- **CC-165** `documented` Near the context limit, Claude Code first clears older tool outputs and then summarizes the conversation if needed; requests and key code snippets are kept, while detailed early instructions may be lost. [cc-how]
- **CC-166** `documented` The compaction summary keeps requests and intent, key technical concepts, files examined or changed with important snippets, errors and fixes, pending tasks and current work; full tool outputs and intermediate reasoning are not kept. [cc-ctx]
- **CC-167** `documented` After compaction the system prompt and output style still apply, the project-root CLAUDE.md, unscoped rules and auto memory are re-injected from disk, and Claude Code reads a fresh git status snapshot. [cc-ctx]
- **CC-168** `documented` Right after compaction, Claude Code re-reads up to five files Claude read or edited, most recently modified first; a file over 5,000 tokens comes back only as a path reference. [cc-ctx]
- **CC-169** `documented` After compaction Claude Code re-attaches the most recent invocation of each invoked skill, keeping the first 5,000 tokens of each within a combined budget of 25,000 tokens filled from the most recently invoked skill, so older skills can be dropped. [cc-ctx] [cc-skills]
- **CC-170** `documented` The listing of skill descriptions is not re-injected after `/compact`; only skills that were invoked are kept. [cc-ctx]
- **CC-171** `documented` Path-scoped rules and nested CLAUDE.md files load into the message history when their trigger file is read, so compaction summarizes them away with the rest of the conversation. [cc-ctx]
- **CC-172** `documented` A "Compact Instructions" section in CLAUDE.md, or `/compact` with a focus, steers what compaction keeps. [cc-how]
- **CC-173** `documented` Without a configured auto-compact window, Claude Code compacts when the conversation reaches the model's context limit; models running with a native 1M-token window compact at about 967K tokens by default, and the documentation lists further cases. [cc-model]
- **CC-174** `documented` The auto-compact window can be set per model with `/autocompact`, for every model with `autoCompactWindow`, for one launch with `--autocompact`, or with `CLAUDE_CODE_AUTO_COMPACT_WINDOW`, which takes precedence over the command, the flag and the setting. [cc-model]
- **CC-175** `documented` Cloud sessions set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` themselves, so auto-compaction triggers partway through the auto-compact window, and a value the user sets for that variable is overridden. [cc-web]
- **CC-176** `documented` When a request would exceed the API's limit on images and PDFs, Claude Code drops a batch of the oldest ones from what it sends, and Claude can no longer see them. [cc-cache]
- **CC-177** `documented` `ENABLE_TOOL_SEARCH=auto` loads MCP tool schemas upfront while they fit within 10% of the context window, and `ENABLE_TOOL_SEARCH=false` loads all of them; without the variable, schemas load upfront behind a non-first-party `ANTHROPIC_BASE_URL`, on Google Cloud's Agent Platform models before the Claude 4.5 generation and on Microsoft Foundry deployments hosted on Azure. [cc-mcp] [cc-ctx]
- **CC-178** `documented` Claude Code warns when an MCP tool's output exceeds 10,000 tokens and limits it to 25,000 tokens by default; `MAX_MCP_OUTPUT_TOKENS` changes the limit. [cc-mcp]
- **CC-179** `documented` Hooks run outside the conversation and load nothing into context unless they return additional context. [cc-ext]
- **CC-180** `documented` An output style loads at session start and again when the style is switched, costing context on every request; nothing loads for the Default style. [cc-ext]
- **CC-181** `documented` Claude Code truncates a skill's combined `description` and `when_to_use` text at 1,536 characters in the skill listing. [cc-skills]
- **CC-182** `documented` `disable-model-invocation: true` keeps a skill's description out of context and stops Claude from invoking the skill on its own; the user can still invoke it. [cc-skills]
- **CC-183** `documented` The skill listing's budget scales with the model's context window, 1% by default; `skillListingBudgetFraction` scales that share and `skillListingMaxDescChars` caps each description. [cc-skills]
- **CC-184** `documented` For an enabled plugin, the name and description of each skill, agent and command Claude can invoke on its own are in context on every turn; the full text of a skill or agent loads only when it is used. [cc-plug-over]
- **CC-185** `documented` On paid plans, Fable 5.1, Fable 5, Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5.5, Sonnet 5 and Sonnet 4.6 have a 1M-token context window in Claude Code. [ctx]
- **CC-186** `documented` Opus 4.6 and Sonnet 4.6 reach the 1M-token window only through a separate 1M variant chosen with `/model`, which needs usage credits for Opus 4.6 on Pro and for Sonnet 4.6 on every plan except usage-based Enterprise. [ctx]

## Subagents

- **CC-090** `documented` A subagent runs in its own isolated context window and returns only a summary to the main conversation. [cc-sub]
- **CC-091** `documented` A fork inherits the full parent conversation, unlike other subagents. [cc-sub]
- **CC-092** `documented` A subagent can keep its own auto memory through a `memory` field: `~/.claude/agent-memory/<name>/` (user), `.claude/agent-memory/<name>/` (project) or `.claude/agent-memory-local/<name>/` (local); its system prompt then includes the first 200 lines or 25 KB of that `MEMORY.md`. [cc-sub]
- **CC-093** `documented` Subagent definitions come from managed settings, the `--agents` flag, `.claude/agents/` (project), `~/.claude/agents/` (user) and a plugin's `agents/` directory; when names clash, that order is the priority. [cc-sub]
- **CC-094** `documented` A subagent receives only its own system prompt plus basic environment details such as the working directory, not the Claude Code system prompt. [cc-sub]
- **CC-095** `documented` A subagent that is not a fork starts without the conversation history, the skills already invoked or the files Claude has read, and works from a delegation message Claude writes. [cc-sub]
- **CC-096** `documented` Such a subagent loads every level of the CLAUDE.md hierarchy the main conversation loads, except the built-in Explore and Plan agents, which skip CLAUDE.md files and the git status snapshot. [cc-sub]
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
- **CC-106** `documented` Account skills do not sync in a session that does not use a sign-in stored by `/login`, such as one that authenticates with an API key, or in a session that does not fetch feature flags, such as one on Amazon Bedrock. [cc-skills]
- **CC-107** `documented` When a claude.ai subscription login is the active authentication, MCP servers added in claude.ai (connectors) are available in Claude Code. [cc-mcp]
- **CC-108** `documented` `disableClaudeAiConnectors` turns off the claude.ai connectors Claude Code fetches itself; it does not act on connectors that a cloud host or the desktop app delivers. [cc-mcp]
- **CC-109** `documented` When an MCP server is defined in several places, Claude Code connects once, using the whole entry from the highest-precedence source: local scope, project scope, user scope, plugin-provided servers, then claude.ai connectors. [cc-mcp]

## Output styles

- **CC-130** `documented` An output style is a set of instructions setting Claude's role, tone and response format for every response in a session; besides Default, the built-in styles are Proactive, Concise, Explanatory and Learning. [cc-styles]
- **CC-131** `documented` Claude Code sends the active style's instructions with every request; custom styles leave out Claude Code's built-in software engineering instructions unless `keep-coding-instructions` is `true`. [cc-styles]
- **CC-132** `documented` Custom output styles are Markdown files in `~/.claude/output-styles` (user), `.claude/output-styles` (project) or `.claude/output-styles` inside the managed settings directory. [cc-styles]
- **CC-133** `documented` Choosing a style with `/output-style` or a menu saves it to `.claude/settings.local.json`; the `outputStyle` field in a settings file also sets it. [cc-styles]
- **CC-134** `documented` A style switched mid-session applies from the next message; before v2.1.251 it applied only after `/clear` or in a new session. [cc-styles]
- **CC-135** `documented` Output styles apply to the main conversation and to forks, but not to other subagents, which run their own system prompt. [cc-styles]

## Relationship to the Claude app

- **CC-110** `documented` A cloud session runs Claude Code on cloud infrastructure instead of the user's machine, keeps running after the laptop is closed and can be started from claude.ai/code, the Claude mobile app, the desktop app, the terminal with `claude --cloud`, or a routine. [cc-web]
- **CC-111** `documented` From the CLI, handoff is one-way: a cloud session can be pulled into the terminal with `claude --teleport`, but an existing terminal session cannot be pushed to the cloud. [cc-web]
- **CC-112** `documented` Cloud sessions do not load plugins installed on the user's machine, nor plugins that a repository's `.claude/settings.json` turns on. [cc-plug] [cc-cloud-env]
- **CC-113** `documented` Cowork projects are not available in Claude Code; the separate redesigned projects (beta) are documented for Claude Code users. [cw-proj] [cc-proj]
- **CC-114** `inferred` Claude Code does not read the Claude app's account or project memory; its persistent knowledge comes from CLAUDE.md files and its own auto memory. Basis: CC-001, CC-044; no page states it directly.
- **CC-115** `documented` The agentic loop, tools and capabilities are the same in every Claude Code interface; what differs is where the code runs and how the user interacts with it. [cc-how]
- **CC-116** `documented` The Claude desktop app includes Claude Code in its Code tab, so the CLI does not need to be installed separately. [cc-over]
- **CC-117** `documented` The desktop app runs the same engine as the CLI; both can run at the same time on the same project, each keeps its own session list, and a CLI session can be brought into the desktop app. [cc-desk]
- **CC-118** `documented` The desktop app and the CLI read the same configuration files, including CLAUDE.md and CLAUDE.local.md and the MCP servers in `~/.claude.json` or `.mcp.json`. [cc-desk]
- **CC-119** `documented` When the desktop app picks up a CLI session with `/resume`, it continues the same session rather than a copy, so `claude --resume` in the terminal still finds it. [cc-desk]

## Desktop app

- **CC-200** `documented` In the desktop app's Code tab, each conversation is a session with its own history and project folder, independent of other sessions, and several can run in parallel. [cc-desk]
- **CC-201** `documented` A desktop Code session runs in one of four environments: Local, Cloud, SSH (a remote machine) or WSL on Windows. [cc-desk]
- **CC-202** `documented` The desktop app's **Open in > Cloud** continues a Code session as a cloud session with the conversation carried over as a summary; sessions over SSH or in WSL cannot be moved this way. [cc-desk]

## Cloud sessions

- **CC-190** `documented` Cloud sessions are available on Pro, Max and Team plans, and for Enterprise users with premium seats or Chat + Claude Code seats. [cc-web]
- **CC-191** `documented` `claude --cloud` creates a new cloud session for the current repository, one repository at a time; the cloud VM clones the current directory's GitHub remote at the current branch rather than the local checkout, unless Claude Code uploads the local repository as a bundle. [cc-web]
- **CC-192** `documented` Teleporting fetches and checks out the cloud session's branch and loads its full conversation history into the terminal; the terminal gets its own copy, and new local work does not appear in the cloud session. [cc-web]
- **CC-193** `documented` A cloud session starts from a fresh clone of the repository: what is committed is available, what is installed or configured only on the user's machine is not. [cc-cloud-env]
- **CC-194** `documented` A cloud session has the repository's CLAUDE.md, its `.claude/rules/` and the skills, agents and commands under its `.claude/`, because they are part of the clone. [cc-cloud-env]
- **CC-195** `documented` In a cloud session with one repository, the hooks and permission rules of its `.claude/settings.json` and the MCP servers of its `.mcp.json` apply; a session with several repositories starts above the clones and does not read them. [cc-cloud-env]
- **CC-196** `documented` A cloud session does not have the user's `~/.claude/CLAUDE.md`, the skills, agents and commands under `~/.claude/`, plugins enabled only in user settings, or MCP servers added at local or user scope. [cc-cloud-env]
- **CC-197** `documented` After a few minutes without activity a cloud session's VM pauses with its files saved, and a paused VM can later be reclaimed. [cc-cloud-env]
- **CC-198** `documented` When a cloud session's VM has been reclaimed, reopening the session provisions a fresh VM that restores the conversation history but not background work such as subagents or shell commands. [cc-web]
- **CC-199** `documented` Packages Claude installs during a cloud session do not carry over to other sessions; a setup script, whose result the environment cache keeps, makes packages available at the start of every session. [cc-cloud-env]

## Remote Control

- **CC-210** `documented` Remote Control connects claude.ai/code or the Claude app for iOS and Android to a Claude Code session running on the user's own machine. [cc-rc]
- **CC-211** `documented` A Remote Control session runs on the user's machine; the web and mobile interfaces are a window into it, so the computer has to stay on and the `claude` process has to keep running. [cc-rc]
- **CC-212** `documented` With Remote Control, the conversation and the progress of subagents and dynamic workflows stay in sync across connected devices, so messages can be sent from the terminal, a browser and a phone. [cc-rc]
- **CC-213** `documented` Connected devices show compaction progress and where the conversation was compacted, and `/clear` resets the conversation on them too. [cc-rc]
- **CC-214** `documented` While Remote Control is connected, the session transcript, including messages, Claude's responses and tool activity, is stored on Anthropic servers. [cc-rc]
- **CC-215** `documented` Remote Control is available on Pro, Max, Team and Enterprise plans, does not work with API keys, and on Team and Enterprise needs an Owner to turn it on in the Claude Code admin settings. [cc-rc]
- **CC-216** `documented` The `disableRemoteControl` setting turns Remote Control off entirely, and organizations with Zero Data Retention or the HIPAA configuration cannot enable it. [cc-rc]

## Sources

[cc-agents]: https://code.claude.com/docs/en/agent-view
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
[cc-web]: https://code.claude.com/docs/en/claude-code-on-the-web
[cc-wt]: https://code.claude.com/docs/en/worktrees
[ctx]: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
[cw-proj]: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork

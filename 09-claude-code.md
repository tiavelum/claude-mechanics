# 09 Claude Code

Prefix: CC · Scope: memory, instruction files, settings, sessions and context in Claude Code (terminal, desktop Code tab, IDE, cloud sessions), and how it relates to the Claude app · Last checked: 2026-10-05

## Memory model

- **CC-001** `documented` Each Claude Code session begins with a fresh context window; two mechanisms carry knowledge across sessions: CLAUDE.md files (written by the user) and auto memory (written by Claude). [cc-mem]
- **CC-002** `documented` Both CLAUDE.md and auto memory are loaded at the start of every conversation and are treated as context, not as enforced configuration. [cc-mem]
- **CC-003** `documented` To block an action regardless of what Claude decides, the documentation points to hooks rather than CLAUDE.md. [cc-mem]
- **CC-004** `documented` The more specific and concise the instructions, the more consistently Claude follows them. [cc-mem]

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
- **CC-020** `documented` Block-level HTML comments in CLAUDE.md are stripped before the content enters Claude's context. [cc-mem]
- **CC-021** `documented` By default, Claude reads `AGENTS.md` only when there is no CLAUDE.md, `.claude/CLAUDE.md` or CLAUDE.local.md in the working directory or above it; a setting can load both. [cc-mem]
- **CC-022** `documented` The user-level `~/.claude/CLAUDE.md`, the managed CLAUDE.md and `.claude/rules/` files do not count for that rule and keep loading alongside AGENTS.md. [cc-mem]

## Imports and rules

- **CC-030** `documented` CLAUDE.md can import other files with `@path/to/file`; relative paths resolve from the importing file, and imports can nest up to four hops deep. [cc-mem]
- **CC-031** `documented` Imported files are expanded and loaded into context at launch. [cc-mem]
- **CC-032** `documented` The first time a project's CLAUDE.md imports files from outside the working directory, Claude Code asks for approval; if declined, those imports stay disabled. [cc-mem]
- **CC-033** `documented` Imports in user-scope files such as `~/.claude/CLAUDE.md` load without that dialog, except in Cowork sessions on the desktop, which skip imports pointing outside the session's working directory. [cc-mem]
- **CC-034** `documented` Instructions can be split into topic files in `.claude/rules/`; rules without a `paths` field load at launch like CLAUDE.md. [cc-mem]
- **CC-035** `documented` A rule with `paths` frontmatter loads only when Claude reads, writes or edits a file matching its glob patterns. [cc-mem]
- **CC-036** `documented` Personal rules in `~/.claude/rules/` apply to every project and load before project rules. [cc-mem]
- **CC-037** `documented` The `claudeMdExcludes` setting skips specific CLAUDE.md or rule files by path or glob. [cc-mem]

## Auto memory

- **CC-040** `documented` Auto memory is on by default in local sessions; in self-hosted environments it is off by default, except in Claude Tag sessions. [cc-mem]
- **CC-041** `documented` Auto memory is toggled in `/memory`, which saves `autoMemoryEnabled` to `~/.claude/settings.json`; a project can turn it off in its own settings. [cc-mem]
- **CC-042** `documented` Each project gets an auto memory directory at `~/.claude/projects/<project>/memory/`, where `<project>` is derived from the git repository. [cc-mem]
- **CC-043** `documented` All worktrees and subdirectories of the same repository share one auto memory directory; outside a git repository, the project root is used. [cc-mem]
- **CC-044** `documented` Auto memory is machine-local and not shared across machines or cloud environments. [cc-mem]
- **CC-045** `documented` The first 200 lines or first 25 KB of `MEMORY.md`, whichever comes first, load at the start of every conversation; topic files load on demand. [cc-mem]
- **CC-046** `documented` When the user asks Claude to remember something, Claude saves it to auto memory; to put it in CLAUDE.md instead, the user asks for that explicitly. [cc-mem]
- **CC-047** `documented` `autoMemoryDirectory` in settings moves auto memory to another location. [cc-mem]
- **CC-048** `documented` Old session transcripts are deleted after the retention period, but auto memory files are excluded from that cleanup. [cc-mem]
- **CC-049** `documented` The main conversation's auto memory is not loaded into subagents, except forks, which inherit the parent conversation. [cc-mem]
- **CC-050** `documented` Auto memory cannot be turned on in background sessions or in sessions started by another Claude Code session. [cc-mem]

## Settings

- **CC-060** `documented` Settings precedence, highest first: managed settings, command line (`--settings`), project local (`.claude/settings.local.json`), shared project (`.claude/settings.json`), user (`~/.claude/settings.json`). [cc-set]
- **CC-061** `documented` A key set at a higher level overrides the same key set lower down. [cc-set]
- **CC-062** `documented` Managed settings can come from a managed settings file, from MDM or OS policy, or from the claude.ai console. [cc-set] [cc-man]
- **CC-063** `documented` The terminal, the desktop app's local sessions and the VS Code extension on one computer read the same settings files. [cc-plug]

## Sessions

- **CC-070** `documented` Sessions are saved continuously as JSONL transcripts at `~/.claude/projects/<project>/<session-id>.jsonl`; the format is internal and may change. [cc-ses]
- **CC-071** `documented` `claude --continue` reopens the most recent conversation in the current directory; `claude --resume` opens a picker or a named session. [cc-ses]
- **CC-072** `documented` `/clear` starts a fresh, empty context and saves the previous conversation so it can be resumed. [cc-ses]
- **CC-073** `documented` `/branch` copies the conversation so far into a new session and leaves the original intact. [cc-ses]
- **CC-074** `documented` A session resumed from the terminal with `--continue` or `--resume` usually restores its model and permission mode; the session picker and `/resume` do not restore the permission mode. [cc-ses]
- **CC-075** `documented` Transcripts are kept for 30 days by default, configurable with `cleanupPeriodDays`. [cc-ses]
- **CC-076** `documented` On Pro or Max, resuming a session inactive for over about an hour and over 100,000 tokens offers to compact the history first. [cc-ses]

## Context and compaction

- **CC-080** `documented` Auto-compaction runs when the context window approaches capacity; `/compact` does it on demand, optionally focused on given instructions. [cc-ctx] [cc-ses]
- **CC-081** `documented` After compaction, the project-root CLAUDE.md is re-read from disk and re-injected; nested CLAUDE.md files and path-scoped rules reload when matching files are read. [cc-mem]
- **CC-082** `documented` An instruction given only in conversation can be lost at compaction; putting it in CLAUDE.md makes it persist. [cc-mem]
- **CC-083** `documented` `/context` shows what is consuming the context window, including which CLAUDE.md and rule files loaded. [cc-ses] [cc-mem]
- **CC-084** `documented` MCP tool schemas are deferred by default and loaded on demand through tool search. [cc-mcp]
- **CC-085** `documented` Before a skill is invoked only its description is in context; after invocation its content stays in context for the rest of the session. [cc-skills]

## Subagents

- **CC-090** `documented` A subagent runs in its own isolated context window and returns only a summary to the main conversation. [cc-sub]
- **CC-091** `documented` A fork inherits the full parent conversation, unlike other subagents. [cc-sub]
- **CC-092** `documented` A subagent can keep its own auto memory through a `memory` field, scoped to user, project or local. [cc-sub]
- **CC-093** `documented` Project subagents live in `.claude/agents/`, personal ones in `~/.claude/agents/`. [cc-sub]

## Skills, plugins and MCP

- **CC-100** `documented` Skills load from `~/.claude/skills/` (all projects), `.claude/skills/` (the repository), nested `.claude/skills/` folders, enabled plugins, and the claude.ai account. [cc-skills]
- **CC-101** `documented` Personal skills in `~/.claude/skills/` do not load in Cowork or cloud sessions unless enabled for the claude.ai account. [cc-skills]
- **CC-102** `documented` Skills enabled on the claude.ai account sync to terminal sessions that are signed in, and are checked for updates about every 10 minutes. [cc-skills] [cc-plug]
- **CC-103** `documented` MCP servers are configured per local scope or user scope in `~/.claude.json`, or per project in `.mcp.json` shared through git. [cc-mcp]

## Relationship to the Claude app

- **CC-110** `documented` A cloud session runs Claude Code on cloud infrastructure instead of the user's machine and can be started from the browser, the apps or the terminal. [cc-web]
- **CC-111** `documented` A cloud session can be pulled into the terminal with `claude --teleport`. [cc-web]
- **CC-112** `documented` Cloud sessions do not load plugins installed on the user's machine. [cc-plug]
- **CC-113** `documented` Cowork projects are not available in Claude Code; the separate redesigned projects (beta) are documented for Claude Code users. [cw-proj] [cc-proj]
- **CC-114** `inferred` Claude Code does not read the Claude app's account or project memory; its persistent knowledge comes from CLAUDE.md files and its own auto memory. Basis: CC-001, CC-044; no page states it directly.

## Sources

[cc-ctx]: https://code.claude.com/docs/en/context-window
[cc-proj]: https://code.claude.com/docs/en/claude-projects
[cc-man]: https://code.claude.com/docs/en/managed-settings
[cc-mcp]: https://code.claude.com/docs/en/mcp
[cc-mem]: https://code.claude.com/docs/en/memory
[cc-plug]: https://code.claude.com/docs/en/plugins/install
[cc-ses]: https://code.claude.com/docs/en/sessions
[cc-set]: https://code.claude.com/docs/en/settings
[cc-skills]: https://code.claude.com/docs/en/skills
[cc-sub]: https://code.claude.com/docs/en/sub-agents
[cc-web]: https://code.claude.com/docs/en/claude-code-on-the-web
[cw-proj]: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork

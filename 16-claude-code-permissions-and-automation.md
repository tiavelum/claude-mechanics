# 16 Claude Code: permissions and automation

Prefix: CCA · Scope: how Claude Code acts: the agentic loop and steering, permissions and hooks, checkpoints, how subagents, skills, plugins and MCP servers are defined and run, scheduled work, prompt caching and costs · Last checked: 2026-10-06

## The agentic loop

- **CCA-001** `documented` Claude Code handles a task in three phases that run into one another: it gathers context, takes action and verifies the results, using tools in each of them. [cc-how]
- **CCA-002** `documented` The loop rests on two components, a model for the reasoning and tools for the acting; Claude Code is what surrounds the model, supplying the tools and managing what context the model sees, and the documentation calls this surrounding layer the "agentic harness". [cc-how]
- **CCA-003** `documented` The documentation groups Claude Code's built-in tools into five general categories: file operations, search, execution, web, and code intelligence, which needs a code intelligence plugin. [cc-how]

## Steering a running turn

- **CCA-010** `documented` `Esc` stops Claude at once: Claude Code cancels the tool call in progress, Claude waits for a new instruction, and any queued messages go out next. [cc-how]
- **CCA-011** `documented` A message sent with `Enter` during a turn is queued and does not interrupt it; while tool calls are running, Claude receives the message once they finish, still within that turn, and whatever remains queued at the end of the turn is sent in the order it was typed. [cc-how] [cc-int]
- **CCA-012** `documented` Commands and `!` shell commands that were queued wait for the end of the turn; Claude Code then runs them singly, in their queued order. [cc-int]
- **CCA-013** `documented` `Ctrl+Enter` sends the queued messages right away, without waiting for the end of the turn; it needs Claude Code v2.1.275 or later. [cc-int]
- **CCA-014** `documented` `Ctrl+B` sends a running Bash command to the background: it continues under a task ID while Claude answers new prompts, Claude can read its output from the file it is written to, and Claude Code cleans such tasks up when it exits. [cc-int]

## Permission modes

- **CCA-020** `documented` The permission mode of a session determines what Claude may do there without first asking the user; the modes are `default`, which the interfaces label Manual, `acceptEdits`, `plan`, `auto`, `dontAsk` and `bypassPermissions`. [cc-modes]
- **CCA-021** `documented` Without a prompt, `default` runs only reads, `acceptEdits` also file edits and common filesystem commands, `plan` reads and, where auto mode is available, commands the classifier approves, `auto` everything under background safety checks, `dontAsk` reads and pre-approved tools while denying whatever would prompt, and `bypassPermissions` everything. [cc-modes]
- **CCA-022** `documented` A few actions are not auto-approved in any mode, `bypassPermissions` included, among them tools that an explicit ask rule matches, tools that need the user to interact, and removals with `rm` or `rmdir` aimed at a critical path, for example the root of the filesystem or the user's home or working directory. [cc-modes]
- **CCA-023** `documented` In auto mode, actions are checked before they run by a classifier, which is a separate model, and it blocks those that go beyond the request, aim at infrastructure it does not recognize or seem driven by hostile content Claude has read. [cc-modes]
- **CCA-024** `documented` From Claude Code v2.1.283 on, the built-in default with which interactive sessions in the terminal and in VS Code start is auto mode; in earlier versions it was auto only from v2.1.228 on (v2.1.233 on native Windows), only on the Pro, Max and Team plans and only where the session fetches feature flags, and Manual otherwise. [cc-modes]
- **CCA-025** `documented` The permission mode of a new terminal session comes from the first source that applies: the `--permission-mode` or `--dangerously-skip-permissions` flag, then `permissions.defaultMode` in a settings file, then the built-in default. [cc-modes]
- **CCA-026** `documented` For a new terminal session, `auto` or `bypassPermissions` as the value of `permissions.defaultMode` is not applied when it is set in the project files `.claude/settings.json` or `.claude/settings.local.json`: with `auto` there the session starts in the built-in default, with `bypassPermissions` there in Manual; every other value applies from whichever settings file sets it. [cc-modes]

## Permission rules

- **CCA-040** `documented` A permission rule is an allow rule, which lets Claude Code use the named tool without manual approval, an ask rule, which prompts for confirmation, or a deny rule, which prevents the use. [cc-perm]
- **CCA-041** `documented` Claude Code checks deny rules first, ask rules second and allow rules last, and the first rule that matches settles the outcome; how specific a rule is does not change this order. [cc-perm]
- **CCA-042** `documented` A deny rule admits no exception through an allow rule, however narrow, and likewise a call that matches an ask rule prompts even if a more specific allow rule matches it too. [cc-perm]
- **CCA-043** `documented` A tool denied at any settings level cannot be allowed by another level, and no level, command line arguments included, can override a managed permission rule. [cc-perm]
- **CCA-044** `documented` Deny rules block in every permission mode, `bypassPermissions` included, while an allow rule changes nothing in `bypassPermissions`. [cc-modes]
- **CCA-045** `documented` Deny and ask rules do not cover the `EndConversation` tool while Claude still has another tool it can call. [cc-modes]

## Hooks

- **CCA-050** `documented` Hooks are shell commands that the user defines and Claude Code runs at set points of its lifecycle, so that an action always happens instead of depending on the model choosing to do it. [cc-hooks-guide]
- **CCA-051** `documented` Most hooks are of type `command` and run a shell command; there are four more types: `http` posts the event data to a URL, `mcp_tool` calls a tool of a configured MCP server, `prompt` is a single-turn model evaluation, and `agent`, which is experimental, verifies over several turns with access to tools. [cc-hooks-guide]
- **CCA-052** `documented` Where a hook is defined sets its scope: `~/.claude/settings.json` (all the user's projects), `.claude/settings.json` (one project, committable), `.claude/settings.local.json` (one project, not shared), managed policy settings (the organization), a plugin's `hooks/hooks.json` (while the plugin is enabled), a skill's frontmatter (from the skill's invocation to the end of the session) or a subagent's frontmatter (while that subagent runs). [cc-hooks-guide]
- **CCA-053** `documented` Exit code 2 from a hook tells Claude Code to block the action, and the hook states its reason on stderr, which some events pass back to Claude; some events, `SessionStart` among them, cannot be blocked, and there exit code 2 only shows the stderr text to the user. [cc-hooks-guide]
- **CCA-054** `documented` A `PreToolUse` hook runs ahead of the permission prompt, and its output can refuse the tool call, make Claude Code prompt or let the call through unprompted; the decision does not get around permission rules, though: whatever the hook returns, a deny rule that matches still blocks the call, and an ask rule that matches still leads to a prompt. [cc-perm]
- **CCA-055** `documented` `PreToolUse` hooks run in all permission modes, ahead of the mode's own check, so a hook that denies a call blocks it even in `bypassPermissions` mode. [cc-hooks-guide]
- **CCA-057** `documented` A `PreToolUse` hook that exits with code 2 halts the tool call before Claude Code evaluates permission rules, so its block also holds against an allow rule that would let the call through. [cc-perm]
- **CCA-056** `documented` A mod the user has installed, if it handles `tool.check`, gives its answer once the permission rules and the `PreToolUse` hooks are done and can overturn theirs: it may approve a call despite an ask rule that would prompt and despite a hook's block, except a block by a hook from managed settings, and it may approve a call against a deny rule where the machine has no managed settings and the user's sign-in is not on a Team or Enterprise plan; elsewhere deny rules hold against the mod by default, which the organization can change. [cc-perm]
- **CCA-058** `documented` When a mod that handles `tool.check` approves a call in auto mode, that call runs without a check by the classifier. [cc-perm]

## Checkpoints and rewind

- **CCA-070** `documented` Each prompt that starts a turn gets a checkpoint, which records the state of the code as it was before the prompt. [cc-check]
- **CCA-071** `documented` Checkpoints cover only what Claude changes with its file editing tools: a file altered by a Bash command, such as `rm`, `mv` or `cp`, is not tracked, and rewinding does not undo the change. [cc-check]
- **CCA-072** `documented` Within a session, file snapshots are kept for the latest 100 checkpoints. [cc-check]
- **CCA-073** `documented` Checkpoints exist apart from git and are stored with the conversation, so `/rewind` still works after a session is resumed. [cc-how] [cc-check]
- **CCA-074** `documented` The retention sweep removes a session's file snapshots, by default roughly 30 days after the last one was saved; `cleanupPeriodDays` can be set to keep them longer. [cc-check]
- **CCA-075** `documented` `/rewind`, or `Esc` pressed twice on an empty prompt, opens the rewind menu, which lists the prompts sent in the session and, for the one selected, offers to restore code and conversation, the conversation only or the code only, to summarize the conversation from that point on or up to it, or to cancel. [cc-check]
- **CCA-076** `documented` A queued message that Claude receives while the turn is still running joins that turn and gets no checkpoint of its own, so undoing the edits made after it means rewinding to the prompt with which the turn began. [cc-check]
- **CCA-077** `documented` Edits made by a subagent are usually not captured in the session's checkpoints: rewinding restores them only for a forked skill running in the foreground; for the edits of any other subagent the documentation points to git to revert them. [cc-check]
- **CCA-078** `documented` Only files edited in the current session are tracked: a manual change made outside Claude Code or an edit by another session running at the same time is normally not captured, except where it hits a file the current session also edited. [cc-check]
- **CCA-079** `documented` Checkpoints are limited to file changes; what Claude does to remote systems, for example a database, an API or a deployment, cannot be checkpointed. [cc-how]
- **CCA-080** `documented` A restore skips tracked paths that are symlinks or hard links and warns about them; the content of the skipped files stays as it is. [cc-check] [cc-how]

## Subagents

- **CCA-090** `documented` A custom subagent is defined in a Markdown file with YAML frontmatter, of whose fields `name` and `description` alone are mandatory; the description is what Claude goes by when deciding whether to hand a task to that subagent. [cc-sub]
- **CCA-091** `documented` Claude Code ships with built-in subagents, which Claude uses on its own, among them Explore, a read-only agent, built for speed, that searches and analyzes codebases, Plan, which does the research in plan mode, both with Write and Edit denied, and general-purpose, for multi-step tasks that need both exploration and action. [cc-sub]
- **CCA-092** `documented` If a subagent's definition has no `tools` field, the subagent gets all tools that are available to subagents; the `tools` field acts as an allowlist and `disallowedTools` as a denylist. [cc-sub]
- **CCA-093** `documented` The tools available to subagents are the built-in and MCP tools of the main conversation after two filters: one takes a few tools away from all subagents, and the other cuts down the built-in tools of subagents that run in the background; forks skip both and get exactly the tool pool of the main conversation. [cc-sub]
- **CCA-094** `documented` A subagent whose definition has no `permissionMode` field takes over the permission mode of the main conversation; if that mode is `bypassPermissions`, `acceptEdits` or auto, it applies to the subagent in any case, and a `permissionMode` value in the definition has no effect. [cc-sub]
- **CCA-095** `documented` Claude Code resolves a subagent's model in this order: the `model` parameter Claude passes for the invocation, the `model` field of the definition, in which `inherit` stands for the model of the main conversation, the environment variable `CLAUDE_CODE_SUBAGENT_MODEL`, and the main conversation's model; before v2.1.251 the environment variable came first. [cc-sub]
- **CCA-096** `documented` Subagents may by default start subagents themselves, with nesting limited to three layers under the main conversation; a subagent at that limit, unless it is a fork, is not given the `Agent` tool, and `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` changes the limit, with `1` turning nesting off. [cc-sub]
- **CCA-097** `conflicting` Whether a subagent can spawn subagents by default: the subagents page says it can, down to three layers, and that the default depth was one in v2.1.217 and v2.1.218, while the context window page says a subagent by default lacks the Agent tool, to prevent recursion. [cc-sub] [cc-ctx]
- **CCA-098** `documented` A foreground subagent blocks the main conversation until it completes and passes its permission prompts through to the user; a background subagent runs while the user keeps working, and its permission prompts appear in the main session, naming the subagent that asks. [cc-sub]
- **CCA-099** `documented` For a subagent that Claude spawns, the first matching case applies: one spawned by an in-process agent-team teammate runs in the foreground, as does every subagent when `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` is `1`; with fork mode on, the subagent runs in the background and Claude has no way to request the foreground; with fork mode off, the background is the default, and Claude picks the foreground when it cannot go on without the result. [cc-sub]
- **CCA-100** `documented` Fork mode, in which Claude spawns a fork by asking for the subagent type `fork`, is enabled by default in interactive sessions, from Claude Code v2.1.232 on, and disabled by default for non-interactive runs with `-p` and for the Agent SDK; setting `CLAUDE_CODE_FORK_SUBAGENT` to `1` or `0` overrides these defaults. [cc-sub]
- **CCA-101** `documented` According to the overview, a task can be divided among several Claude Code agents that work in parallel, each on its own part, under a lead agent that coordinates them, hands out the subtasks and combines the results. [cc-over]

## Skills

- **CCA-120** `documented` A skill is a `SKILL.md` file of instructions, knowledge or workflows; Claude uses a skill when it is relevant, and the user can call it directly by typing `/skill-name`. [cc-skills] [cc-ext]
- **CCA-121** `documented` Skills have absorbed custom commands: `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` each produce a `/deploy` command that behaves the same, existing files under `.claude/commands/` still work, and when a skill and a command file have the same name, the skill is the one that runs. [cc-skills]
- **CCA-122** `documented` For skills with the same name at different levels, the precedence is enterprise before personal before project. [cc-skills] [cc-ext]
- **CCA-123** `documented` Plugin skills carry a namespace and are invoked as `/plugin-name:skill-name`, so a plugin skill and a skill of the same name from another location both load. [cc-skills]
- **CCA-124** `documented` By default both the user and Claude can invoke a skill; `user-invocable: false` in its frontmatter hides the skill from the `/` menu and stops it from running when the user types its name, so that only Claude invokes it. [cc-skills]
- **CCA-125** `documented` The `allowed-tools` field of a skill pre-approves the listed tools for the turn in which the skill is invoked, so Claude uses them without a permission prompt; the approval ends with the user's next message, and the field does not limit which tools Claude can call. [cc-skills]
- **CCA-126** `documented` The `model` field of a skill names the model to use while the skill is active; this lasts until the current turn ends, is not written to settings, and the session's own model returns with the next prompt. [cc-skills]
- **CCA-127** `documented` While a skill with an `effort` field is active, that value takes the place of the session's effort level; the options are `low`, `medium`, `high`, `xhigh` and `max`, of which the available ones depend on the model. [cc-skills]
- **CCA-128** `documented` The subagent of a skill with `context: fork` runs in the background by default, with its result reaching the conversation when it completes; `background: false` makes the invoking turn wait for the result, which is what always happened in versions before v2.1.218. [cc-skills]

## Plugins and MCP servers

- **CCA-140** `documented` In Claude Code a plugin is a directory holding components such as skills, agents, hooks and MCP servers, installed and loaded together as one unit; it usually has a manifest at `.claude-plugin/plugin.json`, which gives the plugin its name. [cc-plug-over]
- **CCA-141** `documented` A mod is a plugin that contains a hooks module, that is, hooks in the form of JavaScript functions. [cc-plug-over]
- **CCA-142** `documented` An MCP server's scope decides where it loads: with local scope, the default, the server is loaded in just the project it was added in and stays private to the user, project scope shares it with everyone working in the project, and user scope makes it available to the user in all projects. [cc-mcp]
- **CCA-143** `documented` Before it uses project-scoped servers from a `.mcp.json` file, Claude Code asks for approval in an interactive session; where it cannot show that prompt, namely in cloud sessions, Agent SDK sessions and runs of `claude -p`, it loads those servers without asking. [cc-mcp]

## Scheduled work

- **CCA-160** `documented` Scheduled work comes in three forms in Claude Code: routines run in the cloud and need neither the user's machine nor an open session, with a minimum interval of one hour; desktop scheduled tasks run on the user's machine without an open session, at intervals down to one minute; `/loop` runs in an open session on the user's machine, also down to one minute. [cc-sched]
- **CCA-161** `documented` Tasks scheduled within a session are session-scoped; they are created with `/loop` or by asking Claude, which uses the `CronCreate`, `CronList` and `CronDelete` tools. [cc-sched]
- **CCA-162** `documented` Of a session's scheduled tasks, a resume does not restore a recurring task that has expired, a one-shot task whose scheduled time has passed, or a self-paced `/loop`, one started without an interval so that Claude picks the delay before each iteration. [cc-sched]
- **CCA-163** `documented` A recurring task expires seven days after it was created: it fires one last time and then deletes itself. [cc-sched]
- **CCA-164** `documented` The number of scheduled tasks a session holds at one time is capped at 50. [cc-sched]
- **CCA-165** `documented` A scheduled prompt fires between turns, and only while Claude Code is up and idle: a task that comes due in the middle of a turn has its prompt held back until that turn is over, and missed fires are not made up for, so after a long busy stretch the task runs a single time, however many intervals went by. [cc-sched]
- **CCA-166** `documented` When the terminal is closed or the session exits, its scheduled tasks stop firing; when the session is sent to the background, its `/loop` tasks move with it into a background session, which goes on running with no terminal attached. [cc-sched]

## Desktop scheduled tasks

- **CCA-170** `documented` A local scheduled task of the desktop app runs on the user's machine with direct access to its files and tools, and fires only when the computer is awake and the app is open. [cc-desk-sched]
- **CCA-171** `documented` While it is open, the desktop app looks at the schedule once a minute; for a task that is due it opens a new session, which is separate from any session the user started by hand. [cc-desk-sched]
- **CCA-172** `documented` On app start or when the computer wakes, the desktop app looks back seven days for runs each task missed and starts a single catch-up run, for the latest missed time; older misses are dropped. [cc-desk-sched]

## Routines

- **CCA-180** `documented` Routines, a research preview, are saved Claude Code configurations: each bundles a prompt, at least one repository and a set of connectors and runs automatically, on cloud infrastructure managed by Anthropic or, when routed there, on an organization's self-hosted environment. [cc-routines]
- **CCA-181** `documented` A routine can combine triggers of three kinds: a schedule, recurring or once at a set time; an API trigger, an HTTP POST to the routine's own endpoint with a bearer token; and a GitHub trigger, which reacts to events in a repository, for example a pull request or a release. [cc-routines]
- **CCA-182** `documented` The Pro, Max, Team and Enterprise plans include routines; they are created and managed at claude.ai/code/routines, in the desktop app or with `/schedule` in the CLI, and Owners on Team and Enterprise can switch them off for all members. [cc-routines]
- **CCA-183** `documented` A routine runs autonomously as a full Claude Code cloud session and offers no choice of permission mode: shell commands, the skills checked into the cloned repository and the routine's connectors are all used with no stop for approval, except for some artifact actions. [cc-routines]
- **CCA-184** `documented` Every run of a routine becomes a new session of its own, listed with the user's other sessions. [cc-routines]

## Prompt caching

- **CCA-190** `documented` Claude Code manages prompt caching by itself, with nothing for the user to set up; setting the environment variable `DISABLE_PROMPT_CACHING` to `1` turns it off for all models. [cc-cache]
- **CCA-191** `documented` Caches are per model, so the first request after a `/model` switch gets no cache hits and reads the entire conversation history again. [cc-cache]
- **CCA-192** `documented` On most models the cache is also per effort level, and a mid-session change of effort makes the next request read the whole history uncached; the exception is Opus 5.5, Sonnet 5.5 and Fable 5.1 when used through a Claude subscription or an API key, where an effort change keeps the cache by default. [cc-cache]
- **CCA-193** `documented` Because compaction swaps the message history for a summary, the cached conversation layer becomes invalid. [cc-cache]
- **CCA-194** `documented` The compaction summary is produced by a request of its own, which carries the system prompt, tools and history unchanged plus a summarization instruction; with a warm cache it reads the prefix from there, and once a pause has outlasted the cache lifetime it has to process the whole history as uncached input. [cc-cache]
- **CCA-195** `documented` `/rewind` cuts the conversation back to an earlier turn, a prefix the cache still holds, so the following request is served from that earlier cache entry. [cc-cache]
- **CCA-196** `documented` Switching permission modes changes neither the system prompt nor the tool definitions and so keeps the cache; the exception is the `opusplan` model setting, with which entering or leaving plan mode switches the model. [cc-cache]
- **CCA-197** `documented` A change of output style and the invocation of a skill or command leave the cached prefix intact, since their instructions enter the conversation as messages; when the frontmatter of the skill or command sets a model, though, the invocation may switch the model for that turn. [cc-cache]
- **CCA-198** `documented` Where the session's MCP tools are deferred through tool search, an MCP server that connects or disconnects mid-session leaves the cache intact, because the tool list sent with the conversation's first request stays in use; where tool definitions load upfront, a server that connects mid-session adds its definitions to the next request and a tool the user removes on purpose drops out of it, either of which breaks the cache, while the definitions of a server that drops out on its own stay in the request and the cache holds. [cc-cache]
- **CCA-200** `documented` Unless the user sets a lifetime, Claude Code asks for the one-hour cache lifetime only while a Claude subscription is within its plan's included usage, and then for the main conversation; with usage credits, an API key or a cloud provider the main conversation gets five minutes. [cc-cache] [cc-costs]
- **CCA-201** `documented` Requests outside the main conversation, such as those of subagents, workflows, forks, compaction and session titles, get the five-minute lifetime by default; on a subscription within plan usage, a few helper requests, a set that Anthropic determines on its servers, get one hour. [cc-cache]
- **CCA-202** `documented` A subagent's first request gets nothing from the parent's cache, since a subagent's conversation has a system prompt and a tool set of its own, and the subagent builds up a cache of its own; a fork carries an exact copy of the system prompt, tools and history of its parent, so the first request of a fork does read the parent's cache. [cc-cache]
- **CCA-203** `documented` The cache of a Claude Code conversation is in practice tied to one machine and one directory: the system prompt contains the auto memory paths, and the conversation begins by announcing the working directory, the platform, the shell and the OS version; parallel sessions in the same directory therefore read each other's cache. [cc-cache]
- **CCA-204** `documented` A resumed session re-sends its whole conversation; the part of the prefix that is unchanged and still inside the cache lifetime is read from the cache. [cc-cache]
- **CCA-205** `documented` Auto-update downloads a new version in the background and applies it when Claude Code is next launched, never in the middle of a session; because a new version usually changes the system prompt or the tool definitions, the first conversation after an upgrade has to build its cache anew. [cc-cache]

## Costs and usage

- **CCA-220** `documented` Even an idle Claude Code session spends a few tokens in the background, for instance on jobs that summarize earlier conversations for `claude --resume`; the costs page gives a typical figure of under $0.04 per session. [cc-costs]
- **CCA-221** `documented` With prompt suggestions on, Claude Code can follow a response with a short request to the session's model that proposes the next prompt; the request draws on the conversation's prompt cache and is skipped in several situations, for example when the account has reached its usage limit or is about to. [cc-costs] [cc-int]
- **CCA-222** `documented` Since `/compact` has to read the conversation it summarizes, compacting a large context is a large request in itself; `/clear`, by contrast, costs nothing. [cc-costs]
- **CCA-223** `documented` To reduce token use, the documentation advises a `/clear` before turning to unrelated work, because stale context costs tokens on every later message. [cc-costs]
- **CCA-224** `documented` Where a CLI tool exists, such as `gh`, `aws` or `gcloud`, the documentation advises using it instead of an MCP server, because it adds no per-tool listing to the context, and it advises disabling MCP servers that are not in use. [cc-costs]
- **CCA-225** `documented` The messages "You've hit your session limit" and "You've hit your weekly limit" concern a subscription plan's usage window, which all models share, so changing the model with `/model` does not help; after the message about an Opus limit or a Sonnet limit, by contrast, work can continue on a model from a different family. [cc-costs]
- **CCA-226** `documented` The requests a subagent makes are its own, separate from those of the main conversation, yet they draw on the same usage limits. [cc-sub] [cc-costs]
- **CCA-227** `documented` A cloud session draws on the same rate limits as the account's other use of Claude and Claude Code; the cloud VM itself is not charged for separately. [cc-web]

## Sources

[cc-cache]: https://code.claude.com/docs/en/prompt-caching
[cc-check]: https://code.claude.com/docs/en/checkpointing
[cc-costs]: https://code.claude.com/docs/en/costs
[cc-ctx]: https://code.claude.com/docs/en/context-window
[cc-desk-sched]: https://code.claude.com/docs/en/desktop-scheduled-tasks
[cc-ext]: https://code.claude.com/docs/en/features-overview
[cc-hooks-guide]: https://code.claude.com/docs/en/hooks-guide
[cc-how]: https://code.claude.com/docs/en/how-claude-code-works
[cc-int]: https://code.claude.com/docs/en/interactive-mode
[cc-mcp]: https://code.claude.com/docs/en/mcp
[cc-modes]: https://code.claude.com/docs/en/permission-modes
[cc-over]: https://code.claude.com/docs/en/overview
[cc-perm]: https://code.claude.com/docs/en/permissions
[cc-plug-over]: https://code.claude.com/docs/en/plugins/overview
[cc-routines]: https://code.claude.com/docs/en/routines
[cc-sched]: https://code.claude.com/docs/en/scheduled-tasks
[cc-skills]: https://code.claude.com/docs/en/skills
[cc-sub]: https://code.claude.com/docs/en/sub-agents
[cc-web]: https://code.claude.com/docs/en/claude-code-on-the-web

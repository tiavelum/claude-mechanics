# 11 Timeline

Prefix: CHG · Scope: dated changes to the mechanisms in this knowledge base, as documented by Anthropic · Last checked: 2026-10-07

- **CHG-017** `documented` 2024-06-25: projects launched on claude.ai for Pro and Team, each with its own knowledge and custom instructions. [blog-proj24]
- **CHG-090** `documented` 2025-07-15: Enterprise audit logs began recording the start and completion of data exports. [audit]
- **CHG-018** `documented` 2025-08-01: project permissions and sharing enabled for Team and Enterprise. [rn]
- **CHG-001** `documented` 2025-08-11: chat search released for Max, Team and Enterprise. [rn]
- **CHG-092** `documented` 2025-08-15: Claude Opus 4 and 4.1 gained the ability to end a conversation in Anthropic's consumer chat interfaces, described as an ongoing experiment. [end-conv]
- **CHG-019** `documented` 2025-08-20: extra usage introduced for Team and Enterprise, letting users buy more usage to keep using Claude and Claude Code after reaching their usage limit. [rn]
- **CHG-023** `documented` 2025-08-20: premium seats introduced for Team and Enterprise, with more usage and access to Claude Code. [rn]
- **CHG-042** `documented` 2025-08-28: Anthropic announced updated Consumer Terms and a Privacy Policy under which users of Free, Pro and Max, including Claude Code used from such accounts, choose whether their chats and coding sessions may be used to train models. [news-terms]
- **CHG-043** `documented` 2025-08-28: for users who allow training, retention of new or resumed chats and coding sessions grew from 30 days to five years. [news-terms]
- **CHG-024** `documented` 2025-09-09: the Claude app gained the ability to create and edit Excel spreadsheets, PowerPoint decks, documents and PDFs itself. [rn]
- **CHG-002** `documented` 2025-09-11: memory released for Team, generating a memory summary, with separate memory per project; incognito chats released for Free, Pro, Max and Team. [rn] [blog-mem]
- **CHG-003** `conflicting` Memory for Enterprise: the release notes date it 2025-09-18, the memory announcement 2025-09-11. [rn] [blog-mem]
- **CHG-025** `documented` 2025-09-29: file creation and editing opened to Pro, and on Claude for iOS and Android to all paid plans. [rn]
- **CHG-044** `documented` 2025-10-08: last day for existing Free, Pro and Max users to accept the updated Consumer Terms and decide on model training; from then on, Claude can be used only after making that choice. [news-terms]
- **CHG-045** `documented` 2025-10-15: Haiku 4.5 released. [rn]
- **CHG-004** `documented` 2025-10-23: memory available on Max, rolling out to Pro over the following two weeks. [rn] [blog-mem]
- **CHG-020** `documented` 2025-11-24: context window compaction introduced: as a chat nears its context limit, its earlier messages are summarized. [rn]
- **CHG-026** `documented` 2025-12-18: organization-wide management of skills for Team and Enterprise, a directory of partner-built skills, and Agent Skills as an open standard for skills across AI platforms. [rn]
- **CHG-046** `documented` 2026-01-05: Opus 3 retired on the Anthropic-operated platforms. [api-deprec]
- **CHG-005** `documented` 2026-01-12: Cowork launched as a research preview on Claude Desktop for Max, macOS only, running locally on the computer in an isolated virtual machine. [rn]
- **CHG-027** `documented` 2026-01-16: the Cowork research preview extended to Pro on Claude Desktop, macOS only. [rn]
- **CHG-028** `documented` 2026-01-16: Claude Code access included with every Team plan standard seat. [rn]
- **CHG-047** `documented` 2026-01-16: Opus 4 and Opus 4.1 removed from the model selector of the Claude app and from Claude Code. [rn]
- **CHG-048** `documented` 2026-02-05: Opus 4.6 released. [rn]
- **CHG-049** `documented` 2026-02-05: the compaction API, which summarizes context on the server, launched in beta on the Claude API, available on Opus 4.6. [api-rn]
- **CHG-029** `documented` 2026-02-12: Enterprise plans can be bought on the website without Sales; a self-serve Enterprise plan has a single seat type that includes Claude, Claude Code and Cowork. [rn]
- **CHG-050** `documented` 2026-02-17: Sonnet 4.6 released. [rn]
- **CHG-051** `documented` 2026-02-19: Sonnet 3.7 and Haiku 3.5 retired on the Anthropic-operated platforms. [api-deprec]
- **CHG-089** `documented` 2026-02-20: Claude Code Security, the product now called Claude Security, opened as a limited research preview for Enterprise and Team, built into Claude Code on the web. [news-sec] [sec-beta]
- **CHG-030** `documented` 2026-02-24: a plugin marketplace and admin controls for plugins in Cowork on Team and Enterprise. [rn]
- **CHG-031** `documented` 2026-02-25: recurring and on-demand scheduled tasks in Cowork, and a Customize section in Claude Desktop that brings skills, plugins and connectors together. [rn]
- **CHG-006** `documented` 2026-03-02: memory from chat history opened to all users, including Free. [rn]
- **CHG-052** `documented` 2026-03-13: the 1M-token context window left beta on Opus 4.6 and Sonnet 4.6, with standard pricing and no beta header for requests above 200K tokens; on Sonnet 4.5 and Sonnet 4 it stayed in beta. [api-rn]
- **CHG-032** `documented` 2026-03-17: research preview, on Pro and Max, of a persistent thread reachable from Claude Desktop and the iOS and Android apps for managing Cowork tasks, rolled out to Max first and to Pro over the next two days. [rn]
- **CHG-033** `documented` 2026-03-23: on Pro and Max, computer use became available as a research preview in Cowork and in Claude Code. [rn]
- **CHG-034** `documented` 2026-04-09: Cowork generally available on macOS and Windows through Claude Desktop. [rn]
- **CHG-035** `documented` 2026-04-09: role-based access controls on Enterprise: users are put into groups manually or through SCIM, and each group's custom role decides which Claude capabilities its members can use, for example Cowork for specific teams. [rn]
- **CHG-053** `documented` 2026-04-16: Opus 4.7 released. [rn]
- **CHG-085** `documented` 2026-04-17: Anthropic Labs launched Claude Design as a research preview for Pro, Max, Team and Enterprise, powered by Opus 4.7 and off by default on Enterprise. [design-news]
- **CHG-054** `documented` 2026-04-20: Haiku 3 retired on the Anthropic-operated platforms. [api-deprec]
- **CHG-055** `documented` 2026-04-30: the 1M-token beta for Sonnet 4.5 and Sonnet 4 ended; the beta header `context-1m-2025-08-07` stopped having an effect, and requests beyond their 200K window return an error. [api-rn]
- **CHG-093** `documented` 2026-04-30: Claude Code Security, renamed Claude Security, entered public beta for Enterprise, run from the claude.ai sidebar or at claude.ai/security and on Opus 4.7 at the time, with Team and Max announced to follow. [sec-beta]
- **CHG-021** `documented` 2026-05-06: the five-hour rate limits of Claude Code were doubled on Pro, Max, Team and seat-based Enterprise, and the peak-hours limit reduction on Claude Code removed for Pro and Max. [news-limits]
- **CHG-056** `documented` 2026-05-19: Claude Managed Agents began saving any tool output over 100K characters, from the agent toolset or an MCP tool, as a file in the sandbox and giving the model a shortened preview with the file's path. [api-rn]
- **CHG-036** `documented` 2026-05-28: Enterprise custom roles gained connector permissions, which decide the connectors, and the individual tools on them, available to each role. [rn]
- **CHG-057** `documented` 2026-05-28: Opus 4.8 released. [rn]
- **CHG-037** `documented` 2026-06-02: Enterprise custom roles gained admin permissions, which give members access to specific administrative areas, such as billing or privacy, without making them Owners. [rn]
- **CHG-058** `documented` 2026-06-02: the Claude API stopped billing requests that end with a refusal before Claude has produced any output. [api-rn]
- **CHG-059** `documented` 2026-06-09: Fable 5 released. [rn]
- **CHG-060** `documented` 2026-06-09: the data retention policy for Covered Models took effect, and Fable 5 and Mythos 5 were designated Covered Models. [covered-ret] [covered]
- **CHG-061** `documented` 2026-06-09: Mythos Preview deprecated, with no retirement date announced yet. [api-deprec]
- **CHG-062** `documented` 2026-06-12: access to Fable 5 and Mythos 5 suspended. [rn]
- **CHG-063** `documented` 2026-06-15: Opus 4 and Sonnet 4 retired on the Anthropic-operated platforms. [api-deprec]
- **CHG-086** `documented` 2026-06-17: Claude Design began sharing usage limits with the rest of Claude, Claude Code included, gained a rebuilt design system import and a place in the sidebar of Claude Desktop. [design-blog]
- **CHG-038** `documented` 2026-06-25: Team and Enterprise admins can require members to verify their device (Trusted Devices) before they view or steer local Claude Code sessions remotely. [rn]
- **CHG-064** `documented` 2026-06-30: Sonnet 5 released. [rn]
- **CHG-087** `documented` 2026-06-30: Claude Science launched publicly, in beta, as a desktop workbench for scientists on macOS and Linux for Pro, Max, Team and Enterprise. [sci-news] [sci-log]
- **CHG-065** `documented` 2026-07-01: access to Fable 5 and Mythos 5 restored. [rn]
- **CHG-066** `documented` 2026-07-01: model entitlements released in beta for Enterprise, letting admins decide which models and which effort settings their users can use. [rn]
- **CHG-007** `documented` 2026-07-07: Cowork available on web and mobile, rolling out over several weeks starting with Max; sessions run remotely (in beta) and are saved to the account, and scheduled tasks run even when no device is online; chat and Cowork came to share one home, where projects and artifacts are kept in a single place for both. [rn]
- **CHG-014** `documented` 2026-07-09: monthly recap introduced in Settings > Reflect, in beta on Free, Pro and Max on the web and Claude Desktop, requiring memory to be on. [rn]
- **CHG-067** `documented` 2026-07-09: Settings > Time and focus introduced, with optional break reminders and quiet hours, in beta on Free, Pro and Max. [rn] [focus]
- **CHG-008** `documented` 2026-07-10: memory redesigned from a summary updated every 24 hours into individual entries saved while chatting. [rn] [mem]
- **CHG-091** `documented` 2026-07-11: the "Member analytics" toggle of usage-based Enterprise organizations became on by default, so members see their own usage in Settings > Usage. [analytics]
- **CHG-068** `documented` 2026-07-24: Opus 5 released. [rn]
- **CHG-084** `documented` 2026-08-03: Claude in Slack switched over to Claude Tag, which runs in Slack channels under its own identity. [tag-help]
- **CHG-069** `documented` 2026-08-05: Opus 4.1 retired on the Anthropic-operated platforms. [api-deprec]
- **CHG-070** `documented` 2026-08-06: the biology classifier of Fable 5 and Fable 5.1 updated on Claude, the Claude apps and the Claude Platform, with Microsoft Foundry, Google Cloud Vertex AI, Amazon Bedrock and Claude Platform on AWS still to follow. [switch-fable]
- **CHG-015** `documented` 2026-08-19: cut-off for Cowork live artifacts; artifacts made in Cowork before this date keep working but cannot be edited in place. [art]
- **CHG-009** `documented` 2026-08-25: one memory across chat and cloud Cowork, a Topics list in Settings > Memory, an opt-in for sensitive topics, and memory switched on by default on the Free, Pro and Max plans, while Team and Enterprise organizations start with it off. [rn] [blog-mem26]
- **CHG-071** `documented` 2026-08-31: Fable 5.1 and Mythos 5.1 designated Covered Models. [covered]
- **CHG-072** `documented` 2026-08-31: first account-creation date for which the API rejects with a 400 error a Fable 5.1 thinking block replayed after the system prompt, the tools or an earlier message changed. [api-rn]
- **CHG-073** `documented` 2026-09-01: Fable 5.1 and Mythos 5.1 released. [rn]
- **CHG-010** `documented` 2026-09-09: end of the option in Settings > Memory to export legacy memory. [mem]
- **CHG-074** `documented` 2026-09-10: the built-in browser for Cowork became on by default on Enterprise, except where an owner had turned it off and in organizations with HIPAA enabled, where it stays off until an owner turns it on. [cw-org]
- **CHG-088** `documented` 2026-09-10: Claude Science became available on Windows. [sci-log]
- **CHG-075** `documented` 2026-09-14: compaction on demand added to the Messages API on the Claude API, in beta under the header `compact-2026-09-04`. [api-rn]
- **CHG-011** `documented` 2026-09-16: chat and Cowork merged into one Claude, rolling out gradually, starting with Pro and Max on web, desktop and mobile; Cowork's global instructions were folded into Instructions for Claude in Settings > General. [rn] [blog-cw] [one]
- **CHG-016** `documented` 2026-09-16: cut-off for legacy artifacts; artifacts made in a chat before this date keep working and can still be published and shared, but no new ones can be made. [art]
- **CHG-039** `documented` 2026-09-16: designs, decks and documents can be asked for in any conversation, including in Claude Code and the Artifacts tab; on Enterprise, the beta templates Claude Design, Claude Slides and Claude Docs stay off until an owner switches them on. [rn] [art]
- **CHG-040** `conflicting` Which plans Claude Design, Claude Slides and Claude Docs reached on 2026-09-16: the release notes make them available on every plan, Free included, while the artifacts article and the merger announcement put these templates in beta on paid plans only. [rn] [art] [blog-cw]
- **CHG-012** `documented` 2026-09-17: redesigned projects (one conversation, parallel cloud threads, shared project memory, Library) released in beta for select Pro and Max subscribers who run Claude Code in cloud sessions and have no projects yet on the web or desktop. [blog-proj]
- **CHG-076** `documented` 2026-09-22: Opus 5.5 released, the first model of the Claude 5.5 family. [rn]
- **CHG-077** `documented` 2026-09-22: date of the single published entry of the Claude app system prompt for Opus 5.5. [sp-opus55]
- **CHG-078** `documented` 2026-09-24: the API resumed billing refusals that come before any output in the categories `bio`, `frontier_llm` and `reasoning_extraction`, on all platforms; such refusals in other categories stay unbilled. [api-rn]
- **CHG-079** `documented` 2026-09-25: a developer portal opened for submitting plugins to the Claude directory, following them through review and seeing their usage once published. [rn] [blog-plugins]
- **CHG-080** `documented` 2026-09-28: Sonnet 5.5 released, the second model of the Claude 5.5 family. [rn]
- **CHG-081** `documented` 2026-09-28: date of the single published entry of the Claude app system prompt for Sonnet 5.5. [sp-sonnet55]
- **CHG-082** `documented` 2026-09-30: Sonnet 4.5 deprecated, with retirement on 2026-11-30 and Sonnet 5.5 as the recommended replacement. [api-deprec]
- **CHG-022** `documented` 2026-10-01 to 2026-10-15: artifact usage promotion on Pro, Max and Team, in which a limited part of the work after creating or editing an artifact, in a chat the next 10 messages, uses 50% less of the five-hour session limit; it covers chats and cloud Cowork tasks, not Claude Code. [promo]
- **CHG-041** `documented` 2026-10-02: on Team and Enterprise, an organization that has not chosen a Publishing setting for skills and plugins that users submit to the organization library switches to "Requires review", in which an owner approves each submission before it is published. [skills-org]
- **CHG-083** `documented` 2026-10-02: Enterprise organizations that have not set skill and plugin security scanning get it switched on by default where it is available; organizations that already decided keep their setting. [skills-org]
- **CHG-013** `documented` 2026-10-06: on Pro and Max, new Cowork tasks and newly created scheduled tasks run in the cloud, while scheduled tasks already running on the user's computer stay there, and Settings > General no longer offers the "Only on your computer" option. [cw-web]
- **CHG-094** `documented` 2026-10-07: Haiku 5.5 released, with a 1M-token context window and prices tiered by prompt length. [api-haiku55]

## Sources

[analytics]: https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans
[api-deprec]: https://platform.claude.com/docs/en/about-claude/model-deprecations
[api-haiku55]: https://platform.claude.com/docs/en/models/haiku-5-5/overview
[api-rn]: https://platform.claude.com/docs/en/release-notes/overview
[art]: https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them
[audit]: https://support.claude.com/en/articles/9970975-access-audit-logs
[blog-cw]: https://claude.com/resources/articles/cowork-is-now-claude
[blog-mem]: https://claude.com/resources/articles/memory
[blog-mem26]: https://claude.com/resources/articles/claudes-memory-works-everywhere-and-you-decide-whats-in-it
[blog-plugins]: https://claude.com/resources/articles/build-plugins-for-claude
[blog-proj]: https://claude.com/resources/articles/projects-redesigned
[blog-proj24]: https://www.anthropic.com/news/projects
[covered]: https://support.claude.com/en/articles/15425695-covered-models
[covered-ret]: https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models
[cw-org]: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
[cw-web]: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
[design-blog]: https://claude.com/blog/claude-design-stays-on-brand-for-daily-work
[design-news]: https://www.anthropic.com/news/claude-design-anthropic-labs
[end-conv]: https://www.anthropic.com/research/end-subset-conversations
[focus]: https://support.claude.com/en/articles/15672868-set-break-reminders-and-quiet-hours
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[news-limits]: https://www.anthropic.com/news/higher-limits-spacex
[news-sec]: https://www.anthropic.com/news/claude-code-security
[news-terms]: https://www.anthropic.com/news/updates-to-our-consumer-terms
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[promo]: https://support.claude.com/en/articles/17274727-artifact-usage-promotion
[rn]: https://support.claude.com/en/articles/12138966-release-notes
[sci-log]: https://claude.com/docs/claude-science/changelog
[sci-news]: https://www.anthropic.com/news/claude-science-ai-workbench
[sec-beta]: https://claude.com/resources/articles/claude-security-public-beta
[skills-org]: https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization
[sp-opus55]: https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5-5
[sp-sonnet55]: https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-5-5
[switch-fable]: https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5-or-fable-5-1
[tag-help]: https://support.claude.com/en/articles/15594475-what-is-claude-tag

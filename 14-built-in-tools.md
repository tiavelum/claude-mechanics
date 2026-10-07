# 14 Built-in tools

Prefix: TOOL · Scope: tools built into the Claude app: web search, Research, code execution and file creation, the browsers and computer use · Last checked: 2026-10-07

## Web search

- **TOOL-001** `documented` When a question calls for current information, Claude uses a search tool and bases its answer on content from the live web, showing an indicator while it searches. [web]
- **TOOL-002** `documented` An answer that draws on web search comes with citations: direct references and links to the sources, and quotes where they fit. [web]
- **TOOL-003** `documented` Web search can also bring images into the conversation, with no separate setting; the image search behind it is powered by Bing, and each image links to the page it came from. [web]
- **TOOL-004** `documented` The Cowork article for Team and Enterprise says that web fetch is run server-side, limited to search results and to URLs the user has shared. [cw-org]
- **TOOL-005** `documented` The web search article lists the models that can search the web: Fable 5.1 and 5, Opus 5.5, 5, 4.8, 4.7 and 4.6, Sonnet 5.5, 5 and 4.6, and Haiku 4.5. [web]
- **TOOL-006** `documented` Web search is switched on or off for a chat with "Web search" in the "+" menu at the lower left of the chat window; a checkmark next to it shows that it is on. [web]
- **TOOL-007** `documented` The new Claude experience has no switch for web search; Claude searches the web whenever that helps. [web] [one]
- **TOOL-008** `documented` On Team and Enterprise, web search is governed in Organization settings > Capabilities: members can switch it on in a chat only after an Owner or Primary Owner has enabled it for the whole organization, and owners can turn it off there for chat and Cowork. [web] [cw-org]
- **TOOL-009** `documented` The documentation advises putting "Use web search" or "Search the web" into a prompt to make sure Claude searches, and notes that a prompt can also tell Claude not to search. [web]

## Research

- **TOOL-020** `documented` In Research, Claude works agentically: it runs a series of searches, each building on the ones before, decides for itself what to look into next, and within minutes returns a thorough answer with citations. [research]
- **TOOL-021** `documented` Research searches the web and also the user's connected sources, for example Gmail, Google Calendar or Google Docs. [research]
- **TOOL-022** `documented` Research needs a paid plan (Pro, Max, Team or Enterprise) and can be used on the web, in Claude Desktop and in Claude Mobile. [research]
- **TOOL-023** `documented` The Research article says Research works only while web search is turned on. [research]
- **TOOL-024** `documented` Research is switched on with "Research" in the "+" menu, after which a blue indicator appears at the foot of the chat window; clicking the indicator switches Research off. [research]
- **TOOL-025** `documented` The new Claude experience starts Research with the command /deep-research, or with "Research" picked in the "+" menu under the message box. [one]
- **TOOL-026** `documented` Research draws on the plan's ordinary usage limits, as any conversation does, and may exhaust them sooner, since Claude pulls in many sources and writes a comprehensive answer. [research]
- **TOOL-027** `documented` For a case where Claude does not seem to research although Research is on, the Research article advises asking Claude outright to use the research tool. [research]
- **TOOL-028** `documented` When Research leaves out a connected Google source it should draw on, the article advises naming that source and asking Claude to pull context from it. [research]

## Code execution and file creation

- **TOOL-030** `documented` With code execution and file creation, Claude writes and runs code, for example Python or JavaScript, in a private, sandboxed computing environment: an isolated container, kept apart from the user's own systems. [files]
- **TOOL-031** `documented` File creation covers Word (.docx), Excel (.xlsx), PowerPoint (.pptx) and PDF files, which the user can download or save straight to Google Drive. [files]
- **TOOL-032** `documented` With code execution and file creation, Claude can also do data analysis: it writes Python scripts, builds machine learning models, works through uploaded data files such as CSV or TSV and draws charts as PNG images. [files]
- **TOOL-033** `documented` Files in the user's projects can be reached from Claude's computing environment while they also stay in context. [files]
- **TOOL-034** `documented` Files that Claude creates stay available for download for the rest of the conversation. [files]
- **TOOL-035** `documented` In the new Claude experience, files that Claude creates are shown beside the conversation. [one]
- **TOOL-036** `documented` The file creation article sets a maximum of 30 MB per file for code execution and file creation, for uploads and downloads alike. [files]
- **TOOL-037** `documented` The file creation article says Claude can work through a PDF larger than 30 MB in its computing environment without loading it into the context window. [files]

## Network access for code execution

- **TOOL-040** `documented` On Free, Pro and Max, network access for code execution is on, which lets Claude install packages from approved sources. [files]
- **TOOL-041** `documented` On Team and Enterprise, owners set code execution's network access in Organization settings > Capabilities, once code execution itself is on, choosing among four options. [files]
- **TOOL-042** `documented` With "Allow network egress" off, Claude has no internet access and can use only packages that are already installed; the article calls this the most secure setting. [files]
- **TOOL-043** `documented` On Team and Enterprise, the network egress option limited to package managers lets Claude install software from approved package sources, for instance npm, PyPI or GitHub. [files]
- **TOOL-044** `documented` On Team and Enterprise, the network egress option for package managers and specific domains also lets Claude reach domains that an owner enters one by one into an allowlist. [files]
- **TOOL-045** `documented` The "All domains" option lets Claude reach any domain on the internet except those on Anthropic's legal blocklist; the article calls it the riskiest option. [files]
- **TOOL-046** `documented` The file creation article gives inconsistent defaults for network access: its availability list says it starts off on Team and on Enterprise, and its setup steps say the same for new Enterprise organizations, but those steps start Team organizations with egress to package managers only, which its list of options for both plans marks as the default. [files]
- **TOOL-047** `documented` With network access on, the approved domains are Anthropic's own services (api.anthropic.com, statsig.anthropic.com), github.com, and package domains of npm, Python (PyPI), Rust (crates.io), Ubuntu and Yarn. [files]
- **TOOL-048** `documented` The network egress setting does not govern web search, web fetch or MCP connections, Claude in Chrome among them, so network traffic stays possible through those whatever the setting. [cw-org] [files]
- **TOOL-049** `documented` On Team and Enterprise, Cowork uses the same network egress settings as code execution, which owners set under Code execution in Organization settings > Capabilities. [cw-org]

## Safeguards for code execution

- **TOOL-060** `documented` The file creation article warns that instructions planted in a file or website could trick Claude into downloading and running harmful code in the sandbox, or into sending data from its context, such as a project or a connected source, to an outside server. [files]
- **TOOL-061** `documented` According to the article, Claude can leak only data it can reach in the conversation, through the user's prompt, a project or connections that are switched on. [files]
- **TOOL-062** `documented` The article says that with egress off nothing can leave the sandbox, and presents this as a final barrier that holds even if the sandbox had a flaw or a prompt injection succeeded. [files]
- **TOOL-063** `documented` The documentation advises a cautious organization to begin with network access off, then to allow package managers, and to add specific domains only as its needs require. [files]
- **TOOL-064** `documented` The documentation advises watching Claude while it uses code execution and stopping it if it uses or accesses data unexpectedly. [files]
- **TOOL-065** `documented` Code execution sandboxes are never shared between users. [files]
- **TOOL-066** `documented` Anthropic limits the sandbox's network, container and storage resources, how long a task can run and how long one sandbox container can be used. [files]
- **TOOL-067** `documented` A prompt injection classifier looks for malicious manipulation of the prompt and stops execution when it detects it. [files]
- **TOOL-068** `documented` The file creation article also counts among its mitigations that the user can switch the feature on or off at any time, that Claude summarizes its actions as it goes, and that the user can review and audit what Claude did in the sandbox. [files]
- **TOOL-069** `documented` The file creation article lists among its mitigations that conversations that include files made with code execution and file creation cannot be shared publicly on Free, Pro and Max. [files]

## Browsers

- **TOOL-080** `documented` In Cowork and in the merged experience, Claude works on websites through one of two browsers: the one built into Claude Desktop, or the user's own Chrome, which it controls through the Claude in Chrome extension. [cw-org] [browser] [one]
- **TOOL-081** `documented` The built-in browser offers the same browsing abilities as Claude in Chrome: opening and reading pages, clicking, typing and filling in forms. [browser]
- **TOOL-082** `documented` The user chooses the browser Claude takes for web tasks in Claude Desktop under Settings > Cowork > "Preferred browser", the built-in one or Claude in Chrome; Claude keeps to that choice unless asked to use the other. [browser] [browser-org] [chrome]
- **TOOL-083** `documented` In Cowork, a user who already uses Claude in Chrome keeps it as the default browser for web tasks; a user without the extension, or new to browser use in Cowork, gets the built-in browser once it reaches them. [browser] [browser-org] [chrome]
- **TOOL-084** `documented` Cowork sessions started on the web or mobile follow the same preferred browser. [browser-org] [browser]
- **TOOL-085** `conflicting` Whether a session on the web or mobile can drive Claude in Chrome while Claude Desktop is closed: the two built-in browser articles say such a session uses the extension directly and needs a connection to a desktop but not an open app, while the Claude in Chrome article and the web, desktop and mobile article say that Claude driving Chrome, or any browser, from another surface still needs Claude Desktop open. [browser] [browser-org] [chrome] [cw-web]
- **TOOL-086** `documented` When the preferred browser is unavailable, Claude says so and carries on with the other one; when the user named a browser that is unavailable, Claude says so and asks before switching. [browser] [browser-org]
- **TOOL-087** `documented` Both browsers run the same safeguards: Claude asks permission before it first acts on a site, high-risk sites are blocked, and a safety check compares every action with what the user asked for. [browser] [browser-org]
- **TOOL-088** `documented` The built-in browser article warns that any AI agent acting in a browser can be the target of prompt injection, in which text hidden in a web page tries to steer Claude elsewhere, and that the safeguards lower this risk but cannot eliminate it. [browser]
- **TOOL-089** `documented` For browser use, the documentation advises beginning with sites the user trusts, keeping watch over tasks that have real consequences, and stopping a task that seems to go wrong. [browser]
- **TOOL-090** `documented` The documentation strongly advises against letting Claude handle sensitive matters through either browser, naming financial accounts, medical information and other people's personal data as examples. [browser]

## Claude in Chrome

- **TOOL-100** `documented` Claude in Chrome is an extension for the Chrome browser with which Claude reads, clicks and navigates on websites beside the user; its tasks can start from its side panel in Chrome, from Cowork or from Claude Code. [chrome]
- **TOOL-101** `documented` Every paid plan (Pro, Max, Team, Enterprise) includes Claude in Chrome; it works in Cowork and Claude Code, and as a beta in the Chrome side panel. [chrome]
- **TOOL-102** `documented` The extension runs only in Google Chrome: other Chromium-based browsers and mobile devices are not supported. [chrome]
- **TOOL-103** `documented` Claude in Chrome works with all public models. [chrome]
- **TOOL-104** `documented` On Max and Team, on Pro as the rollout reaches it, and on Enterprise once an admin has turned on both Claude in Chrome and Cowork in the cloud, the side panel is a Cowork session; until then, Enterprise users get the classic side panel. [chrome]
- **TOOL-105** `documented` As a Cowork session, the Claude in Chrome side panel saves each conversation to the history like other Cowork sessions. [chrome]
- **TOOL-116** `documented` As a Cowork session, the Claude in Chrome side panel ties each conversation to the account rather than the machine, so that it can be continued in Claude Desktop, in Claude Mobile or on the web. [chrome]
- **TOOL-117** `documented` As a Cowork session, the Claude in Chrome side panel offers the user's skills, plugins and connectors. [chrome]
- **TOOL-106** `documented` In the side panel, Claude reads the tab the user is on with no extra setup and without Claude Desktop. [chrome] [cw-web]
- **TOOL-107** `documented` "Switch back to classic" in the side panel's three-dot menu returns to the classic side panel. [chrome]
- **TOOL-108** `documented` Only the classic side panel can record a workflow, a series of steps the user records for Claude to learn and repeat. [chrome]
- **TOOL-109** `documented` The Claude in Chrome article has the user connect the extension to Claude Desktop under Settings > Connectors, by choosing "Configure" for Claude in Chrome. [chrome]
- **TOOL-118** `documented` Once Claude in Chrome is connected in Claude Desktop, it appears in the Connectors menu of chats, where it is off by default and has to be turned on in each conversation. [chrome]
- **TOOL-110** `documented` The extension asks for Chrome permissions such as `debugger`, through which Claude clicks, types and takes screenshots, `tabGroups`, which keeps the tabs Claude opens in a group of their own colour, and `nativeMessaging`, which the article says will let the extension work with Claude Desktop or Claude Code once Anthropic enables that. [chrome]
- **TOOL-111** `documented` Claude can act in several tabs at once: tabs the user drags into Claude's tab group become visible to it and open to its actions. [chrome]
- **TOOL-112** `documented` Claude keeps working on a multi-step task while the user switches tabs, as long as Chrome stays open. [chrome]
- **TOOL-113** `documented` Claude can read the browser's console output, with errors, DOM state and network requests, which the article presents as a help for debugging. [chrome]
- **TOOL-114** `documented` Prompts saved as shortcuts are called up by typing / in the extension's chat. [chrome]
- **TOOL-119** `documented` Shortcuts saved in Claude in Chrome can be scheduled to run daily, weekly, monthly or annually. [chrome]
- **TOOL-115** `documented` When a task needs a sign-in, Claude can ask 1Password for the login, which 1Password fills in after the user approves each request with biometrics, so Claude never sees the password or one-time code; this is in beta on macOS. [chrome]

## The built-in browser

- **TOOL-120** `documented` The built-in browser is part of Claude Desktop on macOS, Windows and, in beta, Linux, for Cowork on Pro, Max and Team, and on Enterprise subject to the organization's setting. [browser] [browser-org]
- **TOOL-121** `documented` When a task involves a website, the built-in browser opens beside the task in the side panel, where the user can watch Claude work, and links in the transcript open there as well. [browser]
- **TOOL-122** `documented` The built-in browser is independent of the user's own browser: nothing needs installing, it works whichever browser the user normally uses, and it leaves the user's tabs alone. [browser] [browser-org]
- **TOOL-128** `documented` In the built-in browser, Claude sees none of the logins saved in the user's own browser unless the user imports them. [browser] [browser-org]
- **TOOL-123** `documented` When the built-in browser first opens, it offers to import cookies from the user's browser so that the user stays signed in. [browser]
- **TOOL-129** `documented` The built-in browser's cookie import lets the user choose site by site, and sites for banking, email or single sign-on start unchecked. [browser]
- **TOOL-124** `documented` On macOS the import works from Chrome, Edge or Firefox; on Windows and Linux only from Firefox; never from Safari. [browser]
- **TOOL-125** `documented` Sign-ins persist: Claude remembers logins from one Cowork session to the next, and any site the user has signed in to in the built-in browser stays open to Claude in later sessions on that computer. [browser]
- **TOOL-126** `documented` The documentation advises choosing deliberately which sites to sign in to in the built-in browser, above all sites that deal with money or personal data. [browser]
- **TOOL-127** `documented` The documentation advises the built-in browser for passing on the web steps of a task while the user keeps working, and Claude in Chrome for work on a page the user already has open. [browser]

## Organization controls for the browsers

- **TOOL-130** `documented` On Team and Enterprise, an Owner or Primary Owner decides in Organization settings > Cowork whether the organization has the built-in browser. [browser-org] [cw-org]
- **TOOL-136** `documented` While an organization has the built-in browser turned off, its users have no way to open it and Claude has no way to use it. [browser-org] [cw-org]
- **TOOL-137** `documented` The organization setting for the built-in browser leaves Claude in Chrome and the browser in Claude Code unaffected. [browser-org]
- **TOOL-131** `documented` The built-in browser is on by default on Team, and on Enterprise since 2026-09-10 unless an owner had turned it off. [cw-org] [browser-org]
- **TOOL-132** `documented` Where an organization has enabled HIPAA, the built-in browser remains off until an Owner switches it on; once the HIPAA configuration covers Claude Code and Cowork in local mode, it is unavailable and no setting enables it. [browser-org] [cw-org]
- **TOOL-133** `documented` Claude in Chrome is switched in a section of its own, Organization settings > Claude in Chrome, where owners can also turn it off. [browser-org] [cw-org]
- **TOOL-138** `documented` Even with Claude in Chrome turned on for an organization, the extension still has to be deployed to or installed in each user's browser. [browser-org] [cw-org]
- **TOOL-134** `documented` Claude in Chrome is on by default on Team, and on Enterprise unless an owner has disabled it. [browser-org]
- **TOOL-139** `documented` In an organization where HIPAA is enabled, the Claude in Chrome extension remains off until an Owner switches it on. [browser-org]
- **TOOL-135** `documented` Site allowlists and blocklists set in Organization settings > Claude in Chrome apply to Claude in Chrome and to the built-in browser alike, as one shared list. [browser-org] [chrome]

## Computer use

- **TOOL-140** `documented` With computer use on, Claude may work on the user's screen directly, clicking, typing and launching apps, when it has no connector or other tool for the job; it can also use the browser, open files or run development tools. [cu]
- **TOOL-141** `documented` In Cowork, Claude starts with the most precise tool: a connector where one exists, otherwise a browser, the built-in one or Claude in Chrome according to the preferred browser, and only then computer use on the screen, which is slower and fails more often. [cu]
- **TOOL-142** `documented` To find its way, Claude takes screenshots of the screen and of the apps it may use, so anything visible there, personal or sensitive data of the user or of others included, is visible to Claude. [cu]
- **TOOL-143** `documented` No sandbox separates Claude from the user's applications during computer use: it acts directly on the desktop, the apps and the browser. [cu]
- **TOOL-144** `documented` Some sensitive apps, such as investment and trading platforms and cryptocurrency apps, are blocked for computer use by default. [cu]
- **TOOL-153** `documented` The user can add apps to a blocklist for computer use, so that Claude's requests to use them are denied automatically. [cu]
- **TOOL-145** `documented` On macOS 15 or later, Claude by default operates in windows in the background, without taking over the pointer or keyboard and mostly waiting while the user types. [cu]
- **TOOL-154** `documented` During computer use on macOS 15 or later, Claude asks permission before it first takes over the whole screen in a session. [cu]
- **TOOL-146** `documented` To have Claude take over the screen instead, the user chooses "Full control" for "When Claude requests access to an app" in the desktop app's Settings > General (under Desktop app). [cu]
- **TOOL-147** `documented` Claude has been trained to steer clear of risky actions during computer use, such as moving money, trading, changing or deleting files, entering sensitive data or collecting facial images, and to point out signs of prompt injection; the article says these guardrails are not absolute. [cu]
- **TOOL-148** `documented` While Claude uses the computer, an automated review looks for signs of prompt injection. [cu]
- **TOOL-149** `documented` An action in one app can affect another: a link clicked in an email app may open in Chrome even without permission for Chrome; Anthropic can hide the Chrome window from Claude but cannot prevent the link from opening. [cu]
- **TOOL-150** `documented` Computer use works only while the computer is awake, its desktop is active and the Claude Desktop app is open. [cu]
- **TOOL-151** `documented` The documentation advises keeping banking, healthcare, government and other sensitive apps out of computer use's reach, closing files and apps with sensitive content beforehand, and starting with simple tasks and specific prompts. [cu]
- **TOOL-152** `documented` The documentation strongly advises against using computer use for financial accounts or investments, legal documents or contracts, medical information, or apps that hold other people's personal information. [cu]

## Sources

[browser]: https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork
[browser-org]: https://support.claude.com/en/articles/16635803-set-up-browser-use-in-claude-cowork-for-team-and-enterprise-plans
[chrome]: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome
[cu]: https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork
[cw-org]: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
[cw-web]: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
[files]: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[research]: https://support.claude.com/en/articles/11088861-use-research-on-claude
[web]: https://support.claude.com/en/articles/10684626-enable-and-use-web-search

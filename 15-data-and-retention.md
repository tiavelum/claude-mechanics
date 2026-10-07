# 15 Data and retention

Prefix: DAT · Scope: what happens to conversation data: model training, retention and deletion, location data, feedback, and the controls for them · Last checked: 2026-10-06

## Model training on consumer plans

- **DAT-001** `documented` On Free, Pro and Max, the user decides whether chats and coding sessions may be used to improve Claude, with the switch "Help Improve our AI models" under Settings > Privacy, both on a computer and on mobile, and can change that decision at any time. [train-set] [news-terms]
- **DAT-002** `documented` With the training setting on, Anthropic uses the data of Free, Pro and Max accounts, Claude Code use from them included, to train new models. [news-terms] [cc-data]
- **DAT-003** `documented` On consumer plans, the chat and coding session data that may be used for training includes the whole conversation concerned, with its content and any custom styles or conversation preferences, plus data collected while Claude for Chrome is used. [train]
- **DAT-004** `documented` On consumer plans, training data leaves out raw content from connectors such as Google Drive, remote and local MCP servers included, though content copied straight into the conversation may be included. [train]
- **DAT-005** `documented` On consumer plans, a conversation flagged for safety review may be used, whatever the training setting, to improve how Anthropic detects and enforces breaches of its Usage Policy, which includes training models for its Safeguards team; the settings article also names detecting harmful content and advancing safety research. [train] [train-set]
- **DAT-006** `documented` On consumer plans, a user can also opt in to training in other ways, for example by joining the Trusted Tester Program. [train]
- **DAT-007** `documented` The 2025 announcement says the training setting applies only to chats and coding sessions that are new or resumed once the choice is made, and that earlier chats without further activity are not used for training. [news-terms]
- **DAT-008** `documented` On consumer plans, once the training setting is turned off, Anthropic uses none of the user's chats or coding sessions, earlier or new ones, in future model training, except that conversations flagged by its safety classifiers may still be used for its safety work. [priv] [train-set] [news-terms]
- **DAT-009** `documented` On consumer plans, a chat that the user deletes is left out of future training, and so is the data of a deleted account. [priv] [news-terms]
- **DAT-010** `documented` On consumer plans, neither turning the training setting off nor deleting a chat takes data out of training runs that are already under way or out of models that have already been trained. [priv] [train-set]
- **DAT-011** `documented` In announcing the 2025 consumer terms, Anthropic says it filters or masks sensitive data by combining tools with automated processes, to protect users' privacy, and that it sells no user data to third parties. [news-terms]
- **DAT-012** `documented` The Claude Code data usage page gives claude.ai/settings/data-privacy-controls as the address at which consumer users can change their privacy settings at any time. [cc-data]

## Model training on commercial plans

- **DAT-020** `documented` By default, Anthropic does not train its models on the inputs or outputs of commercial products, for example Claude for Work, the Anthropic API and Claude Gov. [train-org]
- **DAT-021** `documented` A commercial customer's chats and coding sessions may be used for training if the customer explicitly reports feedback or bugs, for instance with the thumbs up or down button, or decides in some other way to allow it. [train-org]
- **DAT-022** `documented` The Claude Code documentation states that under commercial terms, which cover Team and Enterprise, the API, third-party platforms and Claude Gov, Anthropic does not train generative models on code or prompts sent to Claude Code unless the customer has opted to give its data for model improvement. [cc-data]
- **DAT-023** `documented` An organization admin can expressly enroll the organization in the Development Partner Program, under which Anthropic may train its models on the materials provided; the program is offered only on Anthropic's first-party API, not to users of Google Cloud's Agent Platform or Amazon Bedrock. [cc-data]
- **DAT-024** `documented` For API features that need to store data, the platform documentation commits Anthropic never to use the retained data for model training without the customer's express permission. [api-ret]

## Retention on consumer plans

- **DAT-030** `documented` On Free, Pro and Max, when the user allows training, Anthropic may keep chats and coding sessions for up to five years, in de-identified form, in its model training pipelines. [priv] [news-terms] [cc-data]
- **DAT-031** `documented` On consumer plans, the five-year period applies only to chats and coding sessions that are new, or resumed, after training was allowed. [priv] [news-terms]
- **DAT-032** `documented` On Free, Pro and Max, data of a user who does not allow training is kept under a 30-day retention period, as it was before the 2025 change to the consumer terms. [news-terms] [cc-data]
- **DAT-033** `documented` On consumer plans, Anthropic keeps personal data as long as reasonably needed for the purposes and criteria that its Privacy Policy sets out. [priv]
- **DAT-034** `documented` As reasons for the five-year period, Anthropic names AI development cycles of several years, a model released now having begun development 18 to 24 months earlier, the more consistent behaviour of models trained on consistent data, and its misuse classifiers, which improve when they learn from data gathered over a longer time. [news-terms]

## Retention on commercial plans

- **DAT-040** `documented` On the Anthropic API, Anthropic deletes inputs and outputs from its back-end automatically within 30 days of receiving or generating them, except for services with a longer retention that the customer controls, such as the Files API, for terms agreed otherwise, such as zero data retention, for enforcing the Usage Policy, and to comply with the law. [priv-org]
- **DAT-041** `documented` Commercial products in which conversations can be saved and continued, such as Claude for Work, Claude for Enterprise and the Anthropic Console, keep chats and coding sessions within the product so that the experience stays consistent. [priv-org]
- **DAT-042** `documented` The Claude Code data usage page gives commercial users, on Team, Enterprise and the API, a standard retention period of 30 days for Claude Code data. [cc-data]

## Deletion and longer retention

- **DAT-050** `documented` Deleting a conversation takes it out of the chat history at once and removes it from Anthropic's back-end storage within 30 days, on consumer plans and on commercial products alike. [del] [priv] [priv-org]
- **DAT-051** `documented` If Anthropic's automated trust and safety systems flag a chat or session as violating the Usage Policy, its inputs and outputs are kept for as long as two years, and the trust and safety classification scores for as long as seven years, on consumer and commercial plans alike. [priv] [priv-org]
- **DAT-052** `documented` Anthropic may also keep chats and coding sessions where the law requires it or where this is needed to combat Usage Policy violations, and on consumer plans also to settle disputes. [priv] [priv-org]
- **DAT-053** `documented` Anthropic may anonymize or de-identify personal data for research or statistics and keep it longer in that form; an organization's data it may anonymize in this way only if the contract allows it. [priv] [priv-org]

## Custom data retention on Enterprise

- **DAT-060** `documented` Custom data retention periods are available on Enterprise plans and are set under Organization settings > Data and Privacy. [ret]
- **DAT-061** `documented` According to the Enterprise retention article, conversation and project data is kept indefinitely when no custom period has been set. [ret]
- **DAT-062** `documented` An Enterprise custom retention period is at least 30 days, and every month counts as 30 days, so that three months make 90 days. [ret]
- **DAT-063** `documented` Under Enterprise custom retention, the period is counted from the last activity: for a chat from its last message, for a project from its last update, which includes a new chat in it or a change to its knowledge base. [ret]
- **DAT-064** `documented` When an Enterprise retention period ends, a standalone chat is deleted together with its artifacts, and a project together with all the chats and artifacts in it. [ret]
- **DAT-065** `documented` Under Enterprise custom retention, deletion happens at midnight UTC on the day it is due, and data deleted at the end of its period cannot be recovered. [ret]
- **DAT-066** `documented` Shortening an Enterprise retention period marks the data that now falls outside it for permanent deletion the moment the change is saved; a background job that runs daily removes it, which with large volumes can take several days, and the documentation advises not to count on that delay to undo the change. [ret]
- **DAT-067** `documented` Custom retention periods cover content in chats and projects, but not Claude Managed Agents, Claude Tag, Claude Design or any other feature built on Claude Code on the web. [ret]
- **DAT-068** `documented` On Enterprise, every retention-related action and change, deletion events included, is recorded automatically in the audit logs. [ret]
- **DAT-069** `conflicting` Who can set an Enterprise organization's custom retention period: the retention article requires a Primary Owner or Owner role, while the custom roles article lists editing retention periods under the Privacy admin permission that a custom role can grant without making a member an Owner. [ret] [roles]

## Session transcripts and the Compliance API

- **DAT-070** `documented` According to the API retention page, Anthropic stores an organization's local session transcripts, from sessions that members run on their own machines in apps like Claude Code and Cowork, for 6 years unless the organization has set a finite custom conversation retention period, which then applies instead. [api-ret]
- **DAT-071** `documented` According to the API retention page, transcripts of Cowork sessions in the cloud are kept for 6 years, or less if a user deletes a session first. [api-ret]
- **DAT-072** `documented` In Team and Enterprise organizations, the conversation history that local Cowork sessions keep on members' computers is not covered by Anthropic's standard retention policies, and admins have no central way to manage or delete it. [cw-org]
- **DAT-073** `documented` Claude Enterprise admins can retrieve the conversation history of local Cowork sessions through the Compliance API, which offers no deletion endpoints for local sessions yet. [cw-org]
- **DAT-074** `documented` Where an organization has HIPAA enabled and the Compliance API turned on, Anthropic captures the Cowork sessions that members run on their own computers, so that the organization can retrieve them through that API; in the same passage, the Cowork admin article says the Compliance API returns sessions of the last 30 days, or of the organization's retention period where that is shorter. [cw-org]
- **DAT-075** `documented` According to the API retention page, local sessions that run under zero data retention are not captured by the Compliance API, and for an organization with HIPAA readiness the API captures only the local sessions of Cowork and Claude Code and keeps their transcripts for 30 days. [api-ret]
- **DAT-076** `documented` Anthropic keeps the transcript of a Claude Code cloud session that it hosts so that the user can return to the session later, and the session's code and data fall under the retention and usage rules of the account type. [cc-data]
- **DAT-077** `documented` A Claude Code cloud session can be deleted at any time, which permanently removes its event data. [cc-data]

## Zero data retention and HIPAA readiness

- **DAT-080** `documented` Anthropic is the data processor on the Claude API, on Microsoft Foundry and on Claude Platform on AWS; on Google Cloud's Agent Platform and Amazon Bedrock that role belongs to the cloud provider, and Anthropic's ZDR and HIPAA arrangements do not apply there. [api-ret]
- **DAT-081** `documented` Under zero data retention (ZDR), Anthropic stores no customer prompts or responses at rest once the API response has been returned. [api-ret]
- **DAT-082** `documented` ZDR is set up on request, one organization at a time: the account team enables it for each new organization separately, and enabling it for one organization does not automatically extend it to others under the same account. [api-ret]
- **DAT-083** `documented` ZDR covers the Messages and Token Counting APIs for the features marked eligible, Claude Code used with API keys of an organization under the Commercial Terms, and Claude Platform on AWS, which follows the retention policy of the Claude API and gets ZDR on request. [api-ret]
- **DAT-084** `documented` With metrics logging turned on in Claude Code, usage statistics and similar productivity data fall outside ZDR and may be kept. [api-ret]
- **DAT-085** `documented` ZDR does not cover the consumer plans Free, Pro and Max, whether in the web, desktop and mobile apps or in Claude Code. [api-ret]
- **DAT-086** `documented` The product interfaces of Claude Team and Claude Enterprise are not eligible for ZDR; only Claude Code on Claude Enterprise is excepted, through a separate ZDR offering of its own. [api-ret]
- **DAT-087** `documented` ZDR for Claude Code on Claude Enterprise, available only to qualified accounts, is not part of the standard Enterprise plan; the account team turns it on organization by organization after confirming eligibility. [cc-data] [api-ret]
- **DAT-088** `documented` ZDR also leaves out any use of the Claude Console, its playground included, Claude Managed Agents, whose session transcripts persist until they are deleted, Claude for Excel, and data processed by third-party integrations. [api-ret]
- **DAT-089** `documented` A ZDR organization can still use features that are not eligible, which are typically stateful; using one takes that data outside the arrangement and under the feature's own retention, for example 29 days for the Message Batches API, up to 30 days for code execution containers, and until deletion or expiry for the Files API. [api-ret]
- **DAT-090** `documented` Features marked "Yes (qualified)" are eligible for ZDR and store no prompts or outputs, but keep a bounded technical artifact for a short time: a fingerprint of hashes and token-count estimates for cache diagnostics, and for structured outputs the JSON schema, for up to 24 hours after it was last used. [api-ret]
- **DAT-091** `documented` Prompt caching is fully eligible for ZDR: it stores no prompts or outputs, and the KV cache representations and cryptographic hashes it uses stay in memory only for the cache lifetime and are deleted promptly once it expires. [api-ret]
- **DAT-092** `documented` Even under ZDR or HIPAA readiness, Anthropic may keep data that the law requires it to keep or that its automated trust and safety systems have flagged, and it may keep the inputs and outputs of a flagged chat or session for as long as two years. [api-ret]
- **DAT-093** `documented` HIPAA readiness is the API arrangement for organizations handling protected health information: rather than deleting data at once, it protects it with broader safeguards such as encryption, access controls and audit logging, and the documentation says such an organization does not also need ZDR. [api-ret]
- **DAT-094** `documented` An eligible organization can turn on HIPAA readiness itself: it accepts Anthropic's standard business associate agreement in Claude Console > Settings > Data retention, the controls apply from that moment, and no administrator can turn the configuration off again. [api-ret]
- **DAT-095** `documented` HIPAA readiness is enforced for the whole organization: a request that uses a feature not eligible for it is rejected with a 400 error, except for some client-side tools, which are accepted but stay outside HIPAA readiness. [api-ret]
- **DAT-096** `documented` The API's HIPAA readiness does not cover the consumer plans, work done through the Claude Console interface, Claude Code, Google Cloud's Agent Platform, Amazon Bedrock, Claude Platform on AWS, Microsoft Foundry, third-party integrations, or, as a rule, beta features that the eligibility table does not list as eligible. [api-ret]

## Covered Models

- **DAT-100** `documented` Anthropic can designate a Claude model as a Covered Model when its capabilities, in areas such as cybersecurity, software engineering, scientific reasoning or agentic workflows, are a substantial step beyond earlier generations and would bring elevated risk if misused. [covered]
- **DAT-101** `documented` Four models are designated as Covered Models: Fable 5 and Mythos 5 since 2026-06-09, and Mythos 5.1 as well as Fable 5.1 since 2026-08-31. [covered]
- **DAT-102** `documented` The Covered Models policies follow the model: they apply on every surface where a Covered Model is offered, third-party cloud platforms included, while all other models remain under the customer's existing agreement and retention settings. [covered]
- **DAT-123** `documented` By default, Anthropic retains the prompts and completions of Covered Models for at least 30 days, as part of its safety work. [covered] [covered-ret]
- **DAT-124** `documented` Zero data retention is not available for Covered Models in workspaces, in Claude Enterprise organizations or on third-party platforms, except where Anthropic expressly authorizes it. [covered] [api-ret]
- **DAT-103** `documented` Anthropic's reason for the retention is that some misuse becomes visible only across many requests, for instance best-of-N jailbreaking, which sends hundreds of slightly altered versions of one prompt, or state-sponsored espionage and data extortion campaigns; the safeguards therefore work on usage data retained over a window of time rather than on single requests. [covered] [covered-ret]
- **DAT-104** `documented` When the retention period of a Covered Model ends, its prompts and completions are deleted automatically, unless a safety investigation or an automated trust and safety flag covers them or the law requires keeping them. [covered] [covered-ret]
- **DAT-105** `documented` By default, the retained data of Covered Models is reviewed by automated safety systems built to flag harmful content. [covered]
- **DAT-106** `documented` The Covered Models retention article, in the part addressed to organizations with zero data retention that were not offered Fable under ZDR, says that by default no one at Anthropic can read retained conversations. [covered-ret]
- **DAT-117** `documented` The Covered Models retention article says, in the part for organizations with ZDR that were not offered Fable under ZDR, that humans can read retained conversations only via a controlled access path, for instance after an automated flag for potential harm, and only a small group of approved reviewers does so. [covered-ret]
- **DAT-118** `documented` The Covered Models retention article says, in the part for organizations with ZDR that were not offered Fable under ZDR, that each access to retained conversations is entered in a tamper-proof log which the reviewers can neither suppress nor alter. [covered-ret]
- **DAT-107** `documented` The Covered Models retention article offers eligible organizations access transparency audit logs and customer-managed encryption keys as further protection. [covered-ret]
- **DAT-108** `documented` The Covered Models retention requirement changed nothing for the consumer plans, whose inputs and outputs Anthropic already retained, nor for chat and Cowork through Claude for Enterprise, which already ran with standard retention. [covered-ret]
- **DAT-109** `documented` The Covered Models retention requirement affects only organizations that use zero data retention: in Console workspaces, for Claude Code on Claude Enterprise, or through Amazon Bedrock, Microsoft Foundry or Google Cloud's Agent Platform. [covered-ret]
- **DAT-110** `documented` The Covered Models retention policy took effect on 2026-06-09. [covered-ret]
- **DAT-111** `documented` An organization with ZDR can use Covered Models in a chosen workspace by turning on 30-day retention in that workspace's privacy controls in the Claude Console, while its other workspaces keep ZDR. [api-ret] [covered-ret]
- **DAT-112** `documented` On the Claude API, a request to Fable 5 returns a 400 error if the retention configuration of the requesting organization falls short of the 30-day requirement. [api-ret]
- **DAT-113** `documented` On the Claude API, Claude Platform on AWS included, Anthropic handles the retained data of Covered Models. [api-ret] [covered-ret]
- **DAT-119** `documented` On Google Cloud's Agent Platform and Amazon Bedrock, retention has to be turned on to reach Covered Models, and the retained data stays in the cloud provider's environment. [api-ret] [covered-ret]
- **DAT-120** `documented` On Microsoft Foundry, retention is set per Azure subscription, so an organization with ZDR needs a separate subscription for Covered Models. [covered-ret]
- **DAT-114** `documented` Claude Code that uses the Anthropic API follows the retention of the workspace it runs in. [covered-ret]
- **DAT-121** `documented` Claude Code on Google Cloud's Agent Platform or Amazon Bedrock follows the retention setting of the cloud environment, as Cowork does there too. [covered-ret]
- **DAT-122** `documented` For Claude Enterprise with ZDR, Anthropic is releasing admin console controls with which the Primary Owner changes the retention setting. [covered-ret]
- **DAT-115** `documented` Anthropic is introducing Enterprise Frontier Safeguards for organizations that find retention held by Anthropic difficult for privacy or regulatory reasons: it adds to automated safety monitoring the option of holding the retained monitoring data in the customer's own cloud, and it rolls out in phases from autumn 2026. [covered]
- **DAT-125** `documented` Until Enterprise Frontier Safeguards is available, eligible customers can use Fable 5.1 and Fable 5 under zero data retention for their own internal business applications, as a temporary transition arrangement. [covered] [news-fable51]
- **DAT-116** `documented` The temporary option for eligible customers to use Fable 5 and Fable 5.1 under ZDR changes only how stored data is retained and reviewed: Anthropic's enforcement systems, its real-time safety classifiers and the Usage Policy still cover all traffic, and Anthropic may change or withdraw the arrangement, for example in response to misuse. [covered]

## Feedback in the Claude app

- **DAT-130** `documented` Feedback given with the thumbs up or down button makes Anthropic store the entire conversation it belongs to, with its content and any custom styles or conversation preferences, in its secured back-end for up to five years; on commercial products the conversation's model settings are stored too. [train] [train-org]
- **DAT-131** `documented` The retention articles count bug reports as feedback too and keep the data tied to any feedback submission for 5 years. [priv] [priv-org]
- **DAT-132** `documented` Feedback data leaves out raw content from connectors such as Google Drive and from remote and local MCP servers, though what was copied directly into the conversation may be included. [train] [train-org]
- **DAT-133** `documented` Before using feedback, Anthropic unlinks it from the user's ID, and on commercial plans also from the customer ID, and it does not combine feedback with the user's other conversations. [train] [train-org]
- **DAT-134** `documented` Anthropic may use feedback to analyze how well its services work, for research, to study user behaviour and, as far as applicable law permits, to train its models. [train] [train-org]
- **DAT-135** `documented` On Team and Enterprise, the "Rate chats" setting decides whether members can send feedback to Anthropic with the thumbs up and down buttons; a Primary Owner or Owner changes it in Organization settings > Data and Privacy. [fb-org] [train-org]

## Feedback in Claude Code

- **DAT-140** `documented` In Claude Code, `/feedback` sends Anthropic a copy of the conversation history, code included, and `/bug` and `/share` report through the same path; transcripts shared this way are retained for 5 years. [cc-data]
- **DAT-141** `documented` In Claude Code's feedback dialog the user chooses how much history a report includes: by default only the current session, or in addition the project's other sessions of the past 24 hours or 7 days. [cc-data]
- **DAT-142** `documented` Claude Code's feedback reports are stored in Google Cloud Storage, a GitHub issue in the public repository can optionally be created, and setting `DISABLE_FEEDBACK_COMMAND` to `1` turns `/feedback` reports off. [cc-data]
- **DAT-143** `documented` When Claude Code runs on a third-party provider, for example Google Cloud's Agent Platform or Amazon Bedrock, or has no Anthropic credentials, `/feedback` saves the report in a local archive in `~/.claude/feedback-bundles/` rather than uploading it, with known API key and token patterns redacted, and nothing leaves the machine until the user sends that file on. [cc-data]
- **DAT-144** `documented` In Claude Code, Claude can prepare a feedback report itself and hold it on the machine for the user to review; Claude Code transmits nothing unless the user decides to send it, and a sent draft is handled and retained like any other report. [cc-data]
- **DAT-145** `documented` Answering Claude Code's "How is Claude doing this session?" survey, "Dismiss" included, records only the rating; nothing else from the session, no transcript, inputs or outputs, is collected with it. [cc-data]
- **DAT-146** `documented` After the rating, Claude Code may ask whether Anthropic may look at the session transcript; without a Yes to that question, nothing is uploaded. [cc-data]
- **DAT-155** `documented` Except on the third-party platforms and gateway sessions where it produces a local archive, a Yes to the transcript question uploads the session's transcript, the transcripts of its subagents and the raw session log, with known API key and token patterns redacted and everything else unchanged. [cc-data]
- **DAT-153** `documented` Anthropic keeps the session transcripts that Claude Code users share through the follow-up question about the session transcript for up to 6 months. [cc-data]
- **DAT-154** `documented` Session transcripts that Claude Code users share through the follow-up question about the session transcript cannot be used to train Anthropic's models. [cc-data]
- **DAT-147** `documented` On Microsoft Foundry, Google Cloud's Agent Platform and Amazon Bedrock, and in signed-in Claude apps gateway sessions, a Yes to the transcript question writes the same material to a local archive in `~/.claude/feedback-bundles/` instead of uploading it, and nothing leaves the machine until the user forwards that file. [cc-data]
- **DAT-148** `documented` Claude Code never asks the transcript question in organizations that have zero data retention or whose policy disables product feedback, nor when the variable `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` has been set. [cc-data]
- **DAT-149** `documented` Claude Code's session surveys are turned off with `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1`, and also when one of `DISABLE_TELEMETRY`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` or `DO_NOT_TRACK` is set; the setting `feedbackSurveyRate` controls how often they appear. [cc-data]
- **DAT-150** `documented` An organization that blocks nonessential traffic but collects survey responses with its own OpenTelemetry collector can bring the survey back with `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL=1`, after which the ratings go only to that collector, and the transcript question and all other feedback traffic to Anthropic stay off. [cc-data]

## Location data

- **DAT-160** `documented` When a feature benefits from location data, for example web search asked for local results, Claude may use the IP address to work out a coarse location at city or region level; this holds for consumer accounts and for members of Team and Enterprise organizations. [loc] [loc-org]
- **DAT-161** `documented` Anthropic currently collects no precise location data, such as a location inferred from GPS, Wi-Fi or Bluetooth. [loc-org]
- **DAT-162** `documented` A consumer user can turn off the use of location data for features such as web search in the privacy dashboard; on non-web surfaces such as the mobile app and the browser extension, Claude's access to location is managed at the device level. [loc]
- **DAT-163** `documented` In a Team or Enterprise organization, an administrator can turn off the use of location data for features such as web search in the organization's settings, and each member can also turn it off for their own use. [loc-org]
- **DAT-164** `documented` Separately, Anthropic infers a coarse location at country or region level from the IP address together with other signals, to make sure Claude is used in line with its terms, to prevent abuse and to show the features available in the user's region; this use cannot be turned off. [loc] [loc-org]

## The 2025 update to the consumer terms

- **DAT-180** `documented` On 2025-08-28, Anthropic announced an update of its Consumer Terms and Privacy Policy that lets users of Free, Pro and Max, Claude Code used from those accounts included, choose whether their data is used to improve Claude. [news-terms]
- **DAT-181** `documented` The 2025 update of the consumer terms does not cover services under the Commercial Terms, among them Claude for Work with its Team and Enterprise plans, Claude Gov, Claude for Education, and API use, through Google Cloud's Vertex AI or Amazon Bedrock as well. [news-terms]
- **DAT-182** `documented` According to the announcement, new users make the choice when signing up, while existing users were asked in an in-app notification and had until 2025-10-08 to accept the updated terms and choose, after which a choice was required to keep using Claude. [news-terms]

## Sources

[api-ret]: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
[cc-data]: https://code.claude.com/docs/en/data-usage
[covered]: https://support.claude.com/en/articles/15425695-covered-models
[covered-ret]: https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models
[cw-org]: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
[del]: https://support.claude.com/en/articles/8230524-delete-or-rename-a-conversation
[fb-org]: https://support.claude.com/en/articles/10504844-manage-user-feedback-settings-on-team-and-enterprise-plans
[loc]: https://privacy.claude.com/en/articles/11186740-does-claude-use-my-location
[loc-org]: https://privacy.claude.com/en/articles/11186730-does-claude-use-my-team-members-location
[news-fable51]: https://www.anthropic.com/claude-fable-and-mythos-5-1
[news-terms]: https://www.anthropic.com/news/updates-to-our-consumer-terms
[priv]: https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
[priv-org]: https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
[ret]: https://privacy.claude.com/en/articles/10440198-configure-custom-data-retention-controls-for-enterprise-plans
[roles]: https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans
[train]: https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training
[train-org]: https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
[train-set]: https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings

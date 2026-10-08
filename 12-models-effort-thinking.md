# 12 Models, effort and thinking

Prefix: MOD · Scope: Claude's models in the Claude app, Claude Code and the API: lineup, identifiers and lifecycle, specifications, thinking, effort, how a model is chosen, safeguards and fallback, pricing and availability by plan · Last checked: 2026-10-06

## Lineup and tiers

- **MOD-001** `documented` The models overview compares four current models: Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 4.5. [api-models]
- **MOD-002** `documented` The models overview and the guide on optimizing for cost and intelligence both give Sonnet 5.5 as the current Sonnet model; the guide lists the current models, from lowest to highest cost and capability, as Haiku 5.5, Sonnet 5.5, Opus 5.5 and Fable 5.1. [api-models] [api-cost]
- **MOD-003** `documented` Fable 5.1 was released on 2026-09-01, together with Claude Mythos 5.1. [api-fable51] [rn]
- **MOD-004** `documented` Opus 5.5 was released on 2026-09-22 as the first model of the Claude 5.5 family. [api-opus55] [news-opus55]
- **MOD-005** `documented` Sonnet 5.5 was released on 2026-09-28 as the second model of the Claude 5.5 family. [api-sonnet55] [rn]
- **MOD-006** `documented` Haiku 4.5 was released on 2025-10-15. [api-haiku45]
- **MOD-007** `documented` The announcement of Opus 5.5, which the release notes place on 2026-09-22, said that Sonnet 5.5 and Haiku 5.5 were to be released in the weeks after it. [news-opus55] [rn]
- **MOD-008** `documented` Fable 5.1 and Mythos 5.1 are one and the same model, differing only in how strict their safeguards are: Fable 5.1 is the generally available version, and Mythos 5.1 loosens the safeguards for vetted people and organizations whose work the cybersecurity and life-sciences restrictions of Fable 5.1 affect. [news-fable51]
- **MOD-009** `documented` According to the platform documentation, Mythos 5.1 is available only to organizations verified through one of Anthropic's verification programs, such as the Cyber Verification Program, and is requested by applying to the program for the use case or through an Anthropic, AWS or Google Cloud account team; it has the specifications and pricing of Fable 5.1. [api-fable51] [api-fable51-new] [api-mythos51]
- **MOD-010** `documented` The Fable 5.1 announcement names two trusted access programs as the way to Mythos 5.1, the Cyber Verification Program and the Life Sciences Verification Program, and says that at the time of the announcement only a set of US organizations had access. [news-fable51]
- **MOD-399** `documented` Every tier of the Cyber Verification Program includes Mythos 5.1, together with Opus 5.5 and Sonnet 5.5; organizations already in Project Glasswing need not reapply and move to the program's Specialized Access tier, which requires an in-depth review in collaboration with the US government. [cvp]
- **MOD-400** `documented` Through the Cyber Verification Program, Mythos 5.1 is available on Pro only with usage credits, and on Max it shares with Fable an allowance of up to 50% of the weekly usage limit. [cvp]
- **MOD-011** `documented` The model selection guide describes Fable 5.1 as the most capable model that Anthropic makes available to every customer. [api-choose]
- **MOD-012** `documented` The release notes introduce Fable 5, launched on 2026-06-09, as a "Mythos-class" model made safe for general use, and the Fable product page calls Fable 5.1 a "Mythos-level" model. [rn] [fable-page]
- **MOD-013** `documented` On 2026-06-12 Anthropic switched off Fable 5 and Mythos 5 for every customer in order to follow an export control directive of the US government that suspended foreign nationals' access to the two models; its statement of that day said that access to its other models would not be affected. [news-fable-access] [rn]
- **MOD-014** `documented` Fable 5 and Mythos 5 became available again on 2026-07-01. [rn] [fable-page]
- **MOD-015** `documented` Opus 4.6 was released on 2026-02-05. [rn]
- **MOD-016** `documented` Sonnet 4.6 was released on 2026-02-17. [rn]
- **MOD-017** `documented` Opus 4.7 was released on 2026-04-16. [rn]
- **MOD-018** `documented` Opus 4.8 was released on 2026-05-28. [rn]
- **MOD-019** `documented` Sonnet 5 was released on 2026-06-30. [rn]
- **MOD-401** `documented` Opus 5 was released on 2026-07-24. [rn]

## Which model for what

- **MOD-020** `documented` The documentation advises starting most workloads on Opus 5.5. [api-models] [api-choose]
- **MOD-021** `documented` The documentation advises using Fable 5.1 for demanding reasoning and for agentic work with a long horizon, and also when one's evaluations on Opus 5.5 still come up short at higher effort; the model selection guide names `xhigh` and `max` as that effort. [api-models] [api-choose]
- **MOD-022** `documented` In the one-line descriptions of the models overview, Fable 5.1 is for demanding reasoning and for agentic work with a long horizon, Opus 5.5 for agentic coding and knowledge work that runs for a long time, Sonnet 5.5 the model that best combines speed with intelligence, and Haiku 4.5 the fastest one, with intelligence close to the frontier. [api-models]
- **MOD-023** `documented` The model selection matrix sends a reader who needs the highest capability on offer to Fable 5.1; its example uses are agent sessions lasting hours, deep research in many steps, and analysis that ends in a finished document, spreadsheet or slide deck. [api-choose]
- **MOD-024** `documented` The matrix sends complex agentic coding and enterprise work to Opus 5.5; its example uses are coding agents that work on their own for several hours, refactoring at large scale, complex systems engineering, workflows that lean heavily on vision, and computer use. [api-choose]
- **MOD-025** `documented` The matrix assigns everyday coding, agent and enterprise workloads that need both speed and capability to Sonnet 5.5, and the lowest latency and price to Haiku 4.5, with real-time applications, high-volume processing, cost-sensitive deployments and sub-agent tasks as example uses for Haiku 4.5. [api-choose]
- **MOD-026** `documented` The model selection guide describes two approaches to choosing the first model: efficiency-first, which starts with Haiku 4.5 and upgrades only for capability gaps, and capability-first, which starts with Opus 5.5 and later lowers effort or moves to a smaller model. [api-choose]
- **MOD-027** `documented` The model selection guide says that changing the effort level of one model is often the better tool than moving to a different model. [api-choose]
- **MOD-028** `documented` Anthropic states that on most work Opus 5.5 does as well as Fable 5.1. [news-opus55] [rn]
- **MOD-029** `documented` Anthropic describes the writing of Opus 5.5 as clearer than that of Opus 5: the key information comes first, jargon is less likely, and the model keeps to the writing rules it is given. [news-opus55]
- **MOD-030** `documented` The documentation describes two multi-model patterns: an executor model that runs the agent loop and escalates hard decisions to a more capable advisor model, and an orchestrator model that holds the loop and delegates bulk work to lower-cost worker models. [api-choose] [api-cost]
- **MOD-031** `documented` The cost guide advises a reader who is unsure not to build a multi-model setup yet: first try the effort levels of the model already in use, and if that leaves a gap, work out what the stronger model would cost by itself at `low` effort. [api-cost]

## Identifiers and lifecycle

- **MOD-040** `documented` On the Claude API, the model ID is `claude-fable-5-1` for Fable 5.1, `claude-opus-5-5` for Opus 5.5, `claude-sonnet-5-5` for Sonnet 5.5 and `claude-haiku-4-5-20251001` for Haiku 4.5. [api-models]
- **MOD-041** `documented` From the Claude 4.6 generation on, model IDs carry no date; such an ID is one fixed snapshot, not a pointer to the latest version, and an updated model ships under a new ID. [api-ids]
- **MOD-042** `documented` Before the 4.6 generation, a model ID ends in a snapshot date, and on the Claude API a dateless alias such as `claude-sonnet-4-5` resolves to that minor version's newest dated snapshot. [api-ids]
- **MOD-043** `documented` `claude-haiku-4-5` is an alias; the snapshot behind it is `claude-haiku-4-5-20251001`. [api-haiku45]
- **MOD-044** `documented` The weights and configuration behind a model ID stay fixed, yet the infrastructure serving the model, such as its request routing, safety classifiers and sampling logic, can change, and such updates now and then cause slight differences in behaviour. [api-ids]
- **MOD-045** `documented` Deprecation and retirement are scheduled separately for each model ID. [api-ids]
- **MOD-046** `documented` Anthropic describes the model lifecycle with four states: Active (fully supported and recommended), Legacy (no further updates, may be deprecated later), Deprecated (still works, with a recommended replacement and a retirement date) and Retired (requests fail). [api-deprec]
- **MOD-047** `documented` For a publicly released model, Anthropic gives customers with active deployments at least 60 days of notice before the model is retired. [api-deprec]
- **MOD-048** `documented` The deprecations page lists Fable 5.1 and Mythos 5.1 as Active, with no deprecation date and a retirement no earlier than 2027-09-01. [api-deprec] [api-models]
- **MOD-057** `documented` The deprecations page lists Opus 5.5 as Active, with no deprecation date and a retirement no earlier than 2027-09-22. [api-deprec] [api-models]
- **MOD-058** `documented` The deprecations page lists Sonnet 5.5 as Active, with no deprecation date and a retirement no earlier than 2027-09-28. [api-deprec] [api-models]
- **MOD-059** `documented` When the page was read on 2026-10-06, the deprecations page listed Haiku 4.5 as Active, with no deprecation date and a retirement no earlier than 2026-10-15. [api-deprec] [api-models]
- **MOD-049** `documented` The retirement dates are a commitment that Anthropic makes for the platforms it operates itself (the Claude API, Microsoft Foundry, Claude Platform on AWS); the two platforms that partners operate, Google Cloud and Amazon Bedrock, decide their retirement dates themselves. [api-models] [api-deprec]
- **MOD-050** `inferred` Haiku 4.5, which the deprecations page still listed as Active without a deprecation date on 2026-10-06, is not due for retirement on the Anthropic-operated platforms before 2026-12-05, because a retirement needs at least 60 days' notice. Basis: MOD-047, MOD-049, MOD-059.
- **MOD-051** `documented` The deprecations page lists these older models as Active: Fable 5, Mythos 5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Opus 4.5, Sonnet 5 and Sonnet 4.6. [api-deprec]
- **MOD-052** `documented` The models overview calls Fable 5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Opus 4.5, Sonnet 5 and Sonnet 4.6 legacy models that are still available, while the status table of the deprecations page shows no model in the Legacy state. [api-models] [api-deprec]
- **MOD-053** `documented` Sonnet 4.5 was deprecated on 2026-09-30 and is to be retired on 2026-11-30, with Sonnet 5.5 as the recommended replacement. [api-deprec]
- **MOD-054** `documented` Mythos Preview has been deprecated since 2026-06-09, with a retirement date still to be announced. [api-deprec]
- **MOD-055** `documented` Opus 3 was retired on the Anthropic-operated platforms on 2026-01-05. [api-deprec]
- **MOD-402** `documented` Sonnet 3.7 and Haiku 3.5 were retired on the Anthropic-operated platforms on 2026-02-19. [api-deprec]
- **MOD-403** `documented` Haiku 3 was retired on the Anthropic-operated platforms on 2026-04-20. [api-deprec]
- **MOD-404** `documented` Opus 4 and Sonnet 4 were retired on the Anthropic-operated platforms on 2026-06-15. [api-deprec]
- **MOD-405** `documented` Opus 4.1 was retired on the Anthropic-operated platforms on 2026-08-05. [api-deprec]
- **MOD-056** `documented` The release notes of 2026-01-16 report that Opus 4 and Opus 4.1 were removed from the Claude app's model selector and from Claude Code; on the API the two models were retired on 2026-06-15 and 2026-08-05. [rn] [api-deprec]

## Specifications

- **MOD-060** `documented` On the API, the context window is 1M tokens for Fable 5.1, Opus 5.5 and Sonnet 5.5 and 200K tokens for Haiku 4.5. [api-models]
- **MOD-061** `documented` The API documentation also gives a 1M-token window to Mythos 5.1, Fable 5, Mythos 5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, Sonnet 4.6 and Mythos Preview, and a 200K-token window to the other models, Sonnet 4.5 among them. [api-ctx]
- **MOD-062** `documented` On the API, a model that has a 1M-token window offers the full window by default, without a beta header. [api-ctx]
- **MOD-063** `documented` The maximum output on the synchronous Messages API is 128K tokens for Fable 5.1, Opus 5.5 and Sonnet 5.5 and 64K tokens for Haiku 4.5. [api-models]
- **MOD-064** `documented` On the Message Batches API, the beta header `output-300k-2026-03-24` raises the output limit to 300K tokens for Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5.5, Sonnet 5 and Sonnet 4.6; the Fable and Mythos models are not among them. [api-models] [api-thinking]
- **MOD-065** `documented` The reliable knowledge cutoff is June 2026 for Fable 5.1, Opus 5.5 and Sonnet 5.5 and February 2025 for Haiku 4.5. [api-models]
- **MOD-066** `documented` The models overview separates two cutoffs: the reliable knowledge cutoff, the date up to which a model's knowledge is at its fullest and most dependable, and the training data cutoff, which covers a wider range of data and is June 2026 for the three newer models and July 2025 for Haiku 4.5. [api-models]
- **MOD-067** `documented` The help center gives the month up to which each model was trained and calls it the knowledge cutoff: June 2026 for Sonnet 5.5, Opus 5.5 and Fable 5.1, May 2026 for Opus 5, January 2026 for Sonnet 5, Fable 5, Opus 4.8 and Opus 4.7, August 2025 for Sonnet 4.6 and Opus 4.6, and July 2025 for Haiku 4.5. [training-data]
- **MOD-068** `documented` The models overview rates latency within the current lineup as Slower for Fable 5.1, Moderate for Opus 5.5, Fast for Sonnet 5.5 and Fastest for Haiku 4.5. [api-models]
- **MOD-069** `documented` Each of the current models takes text and images as input, answers in text and can use tools. [api-models]
- **MOD-070** `documented` On the tokenizer in use since Opus 4.7, 1M tokens hold roughly 555,000 words; on the models before it, 1M tokens held about 750,000 words. [api-models]
- **MOD-071** `documented` Opus 4.7 and later models use a newer tokenizer that turns a given text into roughly 30% more tokens than the tokenizer of Sonnet 4.6 and earlier models does; Fable 5.1 has the tokenizer of Fable 5. [api-pricing] [api-fable51-new]
- **MOD-072** `documented` Non-default values of `temperature`, `top_p` or `top_k` return a 400 error on Fable 5.1 and Fable 5, on Mythos 5.1, Mythos 5 and Mythos Preview, on Opus 5.5, Opus 5, Opus 4.8 and Opus 4.7 and on Sonnet 5.5 and Sonnet 5, whether or not thinking is used. [api-thinking] [api-deprec]
- **MOD-073** `documented` Prefilling the assistant's response is impossible while thinking is on; on Fable 5.1 a request with a prefill returns a 400 error. [api-thinking] [api-fable51-new]
- **MOD-074** `documented` Fable 5.1, Mythos 5.1, Opus 5.5 and Sonnet 5.5 reject forced tool use, that is a `tool_choice` whose type is `any` or `tool`, with a 400 error on every request; the documentation's reason for Fable 5.1 and Mythos 5.1 is that their thinking is always on and forcing a tool call would bypass it. [api-thinking] [api-fable51-new] [api-opus55-new]
- **MOD-075** `documented` On 2026-03-13 the 1M-token window of Opus 4.6 and Sonnet 4.6 came out of beta: since that date requests above 200K tokens have run on these two models at the standard price and without a beta header, while on Sonnet 4.5 and Sonnet 4 the window remained a beta feature. [api-rn]
- **MOD-076** `documented` The 1M-token beta of Sonnet 4.5 and Sonnet 4 ended on 2026-04-30: from that date the beta header `context-1m-2025-08-07` had no effect on these two models, and a request beyond their 200K window was answered with an error. [api-rn]

## Documented behaviour of Fable 5.1

- **MOD-080** `documented` Where Fable 5 put several tool calls into one turn, Fable 5.1 may make them one per turn; this is seen in long agent loops in which the next reads, though independent of each other, are implied and not named, and the extra turns take tokens, round trips and time without lowering the quality of the answer. [api-fable51-new]
- **MOD-081** `documented` Between its tool calls, Fable 5.1 addresses less text to the user than Fable 5 did, above all when effort is high. [api-fable51-new]
- **MOD-082** `documented` In some cases Fable 5.1 writes denser prose than Fable 5: its sentences run longer and it breaks paragraphs less often. [api-fable51-new]
- **MOD-083** `documented` Compared with earlier Claude models, Fable 5.1 formats its chat answers more sparingly, with less bold type and fewer headers and lists. [api-fable51-new]
- **MOD-084** `documented` In summaries of documents, Fable 5.1 more often than Fable 5 takes over wording from the source and does not mark it as a quotation. [api-fable51-new]
- **MOD-085** `documented` For a small change to a text file, Fable 5.1 more often than Fable 5 writes the whole file anew where an edit of the affected lines would do; the outcome mostly does not differ, but a full rewrite takes more output tokens and more time. [api-fable51-new]
- **MOD-086** `documented` The multilingual abilities of Fable 5.1 equal those of Fable 5. [api-fable51-new]

## Thinking

- **MOD-100** `documented` With thinking on, Claude reasons about a problem in `thinking` blocks before it answers; that reasoning is charged at the output-token price whether or not its text comes back, and it uses up part of the request's `max_tokens`. [api-thinking]
- **MOD-101** `documented` In adaptive thinking, Claude itself judges from each request whether to think and how much, and the effort level steers that decision. [api-thinking] [api-models]
- **MOD-102** `documented` Earlier models think in a manual mode called extended thinking, which a request switches on with a token budget (`budget_tokens`); Opus 4.6 and Sonnet 4.6 still accept it as a deprecated mode, Mythos Preview accepts it, and the Opus models from Opus 4.7 on, the Sonnet models from Sonnet 5 on, and the Fable and Mythos 5 models reject it. [api-thinking] [api-models]
- **MOD-103** `documented` On the API, thinking is on without any configuration on Fable 5.1 and Fable 5, on Mythos 5.1, Mythos 5 and Mythos Preview, on Opus 5.5 and Opus 5 and on Sonnet 5.5 and Sonnet 5; it stays off until the request asks for it on Opus 4.8, Opus 4.7, Opus 4.6 and Opus 4.5, on Sonnet 4.6 and Sonnet 4.5 and on Haiku 4.5. [api-thinking]
- **MOD-104** `documented` Thinking cannot be turned off on Fable 5.1 and Fable 5, on Mythos 5.1, Mythos 5 and Mythos Preview or on Opus 5.5: a request that disables it returns a 400 error. [api-thinking] [api-models]
- **MOD-105** `documented` Sonnet 5.5 rejects a request that disables thinking; the least thinking it allows is the setting `between_tools`, which leaves out the thinking at the start of a response and is accepted only at `low`, `medium` and `high` effort. [api-thinking] [api-sonnet55] [api-effort]
- **MOD-106** `documented` Opus 5 accepts a request that disables thinking up to `high` effort; at `xhigh` and `max` such a request returns a 400 error. [api-thinking] [api-effort]
- **MOD-107** `documented` Haiku 4.5 does not think adaptively: it has the manual extended thinking of earlier models, and it does not support the effort setting. [api-haiku45] [api-models]
- **MOD-108** `documented` Because thinking cannot be turned off on Opus 5.5, the documentation calls effort the main control over that model's amount of reasoning and over the cost of a request. [api-effort]
- **MOD-109** `documented` The higher the effort level, the sooner and the longer Claude thinks; at the lower levels it may answer a simple problem without thinking at all. [api-effort]
- **MOD-110** `documented` The API never returns Claude's unprocessed reasoning: a thinking block shows a summary as its text and holds the complete reasoning in encrypted form in its `signature` field, which the caller sends back as received in later requests. [api-thinking]
- **MOD-111** `documented` The `display` setting decides whether that summary comes back: with `summarized` the block contains it, and with `omitted` the block's text is empty; the default is `omitted` on the Fable and Mythos models (Fable 5.1, Fable 5, Mythos 5.1, Mythos 5, Mythos Preview), on Opus 5.5, Opus 5, Opus 4.8 and Opus 4.7 and on Sonnet 5.5 and Sonnet 5, and `summarized` on Sonnet 4.6, Opus 4.6 and the models before them. [api-thinking]
- **MOD-112** `documented` A model other than the one the request addresses writes the thinking summaries, and the caller is billed for the full thinking tokens, not for the summary. [api-thinking]
- **MOD-113** `documented` On the Fable and Mythos models (Fable 5.1, Fable 5, Mythos 5.1, Mythos 5 and Mythos Preview), on Opus 5.5, Opus 5, Opus 4.8 and Opus 4.7 and on Sonnet 5.5, what the model reasons between two tool calls always goes into thinking blocks and not into the text of the response. [api-thinking] [api-fable51-new]
- **MOD-114** `documented` Between two tool calls, Fable 5.1, Fable 5, Mythos 5.1, Opus 5.5 and Sonnet 5.5 can address a progress update to whoever is following the agent, saying what they have just learned and what comes next; every update is delivered as a thinking block of its own, placed directly ahead of the tool call. [api-thinking]
- **MOD-115** `documented` The beta setting `display: "updates"` returns these progress updates in readable form and keeps the reasoning itself hidden. [api-thinking] [api-fable51-new]
- **MOD-116** `documented` Models that write progress updates produce them less often when effort is high and when a chain of tool calls is long. [api-thinking]

## Preserved thinking

- **MOD-130** `documented` The newer Claude models protect themselves against distillation through preserved thinking, which keeps API users from extracting Claude's reasoning by editing the earlier context of a conversation. [api-preserved] [news-opus55]
- **MOD-131** `documented` From Fable 5.1 on, the API checks two things about the signature of each thinking block that a request sends back: whether the model now in use is able to read the block, and whether anything that preceded the block has been altered. [api-preserved] [api-thinking]
- **MOD-132** `documented` A thinking block of Fable 5.1, Opus 5.5 or Sonnet 5.5 is valid only as long as its prefix, which is made up of the tools, the top-level system prompt and every earlier message, is sent again unaltered; this prefix check does not run on Mythos 5.1 or on models older than Fable 5.1. [api-preserved]
- **MOD-133** `documented` A change to the prefix of a thinking block invalidates that block and all thinking blocks after it; by default the request then fails with a 400 error, and when the request carries the beta setting `prefix_mismatch_behavior: "drop_block"`, the invalid blocks are discarded instead. [api-preserved]
- **MOD-134** `documented` The prefix check covers nothing but the messages, the tools and the system prompt, so other request parameters such as effort and `max_tokens` may change; nor does any of the following count as an edit: appending messages, moving cache markers, compaction on the server and context editing. [api-preserved] [api-fable51-new]
- **MOD-135** `documented` For accounts created at 00:00 UTC on 2026-08-31 or later, the prefix check is enforced by default; for an account older than that, it is enforced only on requests that set the mismatch behaviour. [api-preserved] [api-thinking] [news-opus55]
- **MOD-136** `documented` The Fable 5.1 announcement words the restriction as applying to new API accounts "from today onwards", and the Fable page lists that announcement as 2026-09-01, while the preserved thinking documentation and the Opus 5.5 announcement name 2026-08-31 as the first account-creation date. [api-preserved] [news-opus55] [news-fable51] [fable-page]
- **MOD-137** `documented` A user whose requests are built by claude.ai, Claude Code, the Claude Agent SDK or Claude Managed Agents has nothing to change, because these products keep the prefix intact. [api-preserved] [api-fable51-new]
- **MOD-138** `documented` Thinking blocks are readable in one direction: Fable 5.1 and Mythos 5.1 can each read the other's blocks and the blocks of earlier models, while an earlier model can read neither's. [api-preserved] [api-fable51-new]
- **MOD-139** `documented` Opus 5.5 can read thinking blocks that come from Opus 5 or from an older Opus, Sonnet or Haiku model, and cannot read those of the Fable and Mythos lines; its own blocks can be read by Fable 5.1 and Mythos 5.1 on the Claude API. [api-preserved] [api-thinking]
- **MOD-140** `documented` Sonnet 5.5 can read the thinking blocks of Haiku 4.5, Opus 4.8, Sonnet 5 and the models before them, and cannot read those of Opus 5.5, Opus 5 or any model of the Fable and Mythos lines; its own blocks are readable by no other model except Opus 5.5, and by Opus 5.5 only on the Claude API and on Google Cloud. [api-preserved] [api-thinking]
- **MOD-141** `documented` When a conversation moves to a model that cannot read the earlier thinking blocks, for example from Fable 5.1 to an Opus model after a fallback, the API removes those blocks from the prompt without an error, so the turns that run there lack that reasoning. [api-preserved] [api-fable51-new]
- **MOD-142** `documented` Thinking blocks dropped this way are not billed and do not count toward input tokens. [api-preserved] [api-fable51-new]
- **MOD-143** `documented` The API drops unreadable blocks only from what the model receives and never alters the caller's history, so Fable 5.1 can read its own thinking blocks again when a request with that history comes back to it. [api-preserved]
- **MOD-144** `documented` A thinking block from Sonnet 5.5 is bound to the account in which it was produced and to accounts linked with that one; when any other account sends the block, the API takes it out before it reaches the model and still completes the request. [api-preserved]

## Effort

- **MOD-150** `documented` With the effort setting a caller trades the thoroughness of a response against the number of tokens it takes: the setting governs how many tokens Claude spends. [api-effort]
- **MOD-151** `documented` Effort affects all tokens of a response, that is text, tool calls and thinking, and it has its effect with thinking on or off. [api-effort]
- **MOD-152** `documented` There are five effort levels: `low`, `medium`, `high`, `xhigh` and `max`. [api-effort]
- **MOD-153** `documented` Effort steers behaviour and does not set a fixed number of tokens; the hard limit on total output, thinking included, remains `max_tokens`. [api-effort]
- **MOD-154** `documented` On the API, Opus 5.5 defaults to `medium` effort, and every other model with an effort setting defaults to `high`. [api-effort] [api-models]
- **MOD-155** `documented` A request that names the model's default effort level behaves exactly like a request without the effort parameter. [api-effort]
- **MOD-156** `documented` `xhigh` exists on Fable 5.1 and Fable 5, on Mythos 5.1 and Mythos 5, on Opus 5.5, Opus 5, Opus 4.8 and Opus 4.7 and on Sonnet 5.5 and Sonnet 5; `max` exists on those models and also on Mythos Preview, Opus 4.6 and Sonnet 4.6, which have no `xhigh`. [api-effort]
- **MOD-157** `documented` `max` sets no limit on how many tokens Claude spends, and the effort table lists `xhigh` for long-running agentic and coding tasks of more than 30 minutes with token budgets in the millions. [api-effort]
- **MOD-158** `documented` With tools, lower effort tends to mean fewer tool calls, several operations merged into one call, no introduction before acting and only a brief confirmation afterwards; at higher effort Claude may call more tools, lay out its plan first, summarize its changes in detail and comment code more fully. [api-effort]
- **MOD-159** `documented` Each model has its own calibration of the effort scale, so a level with the same name does not correspond to the same underlying value on another model. [cc-model] [api-prompt-fable51] [api-effort]
- **MOD-160** `documented` For Fable 5.1 the documentation advises `high` as the starting level, `xhigh` or `max` where agentic or coding work depends most on capability, and `medium` or `low` for routine work or work where latency matters, as soon as one's evaluations confirm that quality does not suffer. [api-effort]
- **MOD-161** `documented` For Opus 5.5 the documentation advises testing the effort levels against one's own evaluations and not reusing the setting that suited an earlier model. [api-effort]
- **MOD-162** `documented` For Opus 4.8 and Opus 4.7 the documentation advises beginning coding and agentic work at `xhigh`. [api-effort] [api-choose]
- **MOD-163** `documented` For Sonnet 5.5 the documentation advises `high` as the starting level for workloads that are neither agentic nor sensitive to latency, `medium` for agentic coding tasks that are well specified, and `medium` or `low` for chat and other work in which latency matters. [api-effort]
- **MOD-164** `documented` On Opus 5, a lower effort level reduces thinking but cannot be counted on to make the visible response shorter; for a shorter response the documentation advises asking for the length in the prompt. [api-effort]
- **MOD-165** `documented` Opus 5.5 tends to spend more thinking on a turn than Opus 5 does when both run at one effort level, and the difference is largest at `xhigh` and `max`. [api-opus55-new] [cc-model]
- **MOD-166** `documented` Anthropic reports from its own tests that Opus 5.5 run at `medium` does at least as well in evaluations of coding and knowledge work as Opus 5 run at `high`. [cc-model]
- **MOD-167** `documented` Fable 5.1 gains most over Fable 5 at the higher effort levels; at `medium` it delivers about the same results as Fable 5 for less money. [api-fable51-new] [api-prompt-fable51]
- **MOD-168** `documented` Fable 5.1 at `low` effort relies on what it already knows more often than Fable 5 did, and correspondingly less often calls a tool for search or retrieval. [api-fable51-new] [api-prompt-fable51]
- **MOD-169** `documented` When effort is `xhigh` or, even more, `max`, Fable 5.1 may think for a longer time before it writes and, for a long deliverable, may compose much of the text while thinking and then produce it a second time as the reply, which costs time and output tokens; the prompting guide advises running such requests at `high` unless a quality gain was measured. [api-prompt-fable51]
- **MOD-170** `documented` A per-message effort change (beta) alters the effort level within a conversation and keeps the prompt cache; it is supported on Fable 5.1, Mythos 5.1, Sonnet 5.5, Opus 5.5 and Opus 5. [api-effort]
- **MOD-171** `documented` When the top-level effort value differs from one request of a conversation to the next, the cached prefixes of the earlier turns are not kept, because this value influences how the prompt is rendered. [api-effort]
- **MOD-172** `documented` After a top-level effort change, Fable 5.1 follows the new level less reliably: the replies already in the conversation were produced at the old level, and the model tends to keep to their pattern. [api-effort]

## Model, effort and thinking in the Claude app

- **MOD-190** `documented` In the Claude app, the model menu beside the send button holds three settings: the model, the effort level and whether Claude uses thinking; the model and effort level in use are displayed at the same place. [model-menu]
- **MOD-191** `documented` The model, effort and thinking settings of the Claude app can be changed in the middle of a conversation, and a change takes effect with Claude's next response. [model-menu]
- **MOD-192** `documented` The Claude app offers the effort selector for Fable 5.1 and Fable 5, for Opus 5.5, Opus 5, Opus 4.7 and Opus 4.6, and for Sonnet 5.5, Sonnet 5 and Sonnet 4.6. [model-menu]
- **MOD-193** `documented` The effort menu labels one level per model "Default"; this is the level recommended for that model. [model-menu]
- **MOD-194** `documented` The default effort level of Fable 5.1 is High in Claude Code and Medium on claude.ai and in Claude Cowork. [news-fable51]
- **MOD-195** `documented` The help center describes the effort level as the control over how much Claude thinks about a response: a higher level makes responses more thorough, slower and more expensive in tokens, so usage limits are reached sooner. [model-menu]
- **MOD-196** `documented` The help center describes Low and Medium as suited to routine tasks, High as the level that best balances quality against speed overall, Extra high (`xhigh`) as built for coding and agentic tasks that run for a long time, and Max as the most thorough level. [model-menu]
- **MOD-197** `documented` According to the help center, the Extra high level is offered on Opus 4.7 and on newer models. [model-menu]
- **MOD-198** `documented` Effort and thinking are set independently of each other and in any combination: effort decides how thorough every response is, and the thinking toggle decides whether Claude reasons first, in a section above the answer that can be expanded. [model-menu]
- **MOD-199** `documented` In the Claude app, thinking cannot be turned off on Fable 5.1, Opus 5.5, Opus 5 and Sonnet 5.5. [model-menu]
- **MOD-200** `documented` For models with effort levels, the thinking toggle sits in the Effort submenu of the model menu; for other models the model menu itself has an "Extended" toggle. [model-menu]
- **MOD-201** `documented` With thinking on, the app shows a "Thinking" indicator with a timer and an expandable section above the response that holds a summary of Claude's thought process. [model-menu]
- **MOD-202** `documented` Claude's displayed thinking can end before it is complete, with a note that the remainder is not available; the cause is thinking that touches information which Anthropic's safety systems rate as a possibly elevated risk of harm or misuse under the Usage Policy. [model-menu]

## Organization controls on Enterprise plans

- **MOD-215** `documented` On Enterprise plans, the organization's model settings sit under Organization settings > Models; they can be managed by Primary Owners and Owners and by any member with a custom role that includes the Identity & Access permission. [org-default] [org-models]
- **MOD-216** `documented` Model entitlements, released in beta for Enterprise plans on 2026-07-01, let an organization's admins decide which models and which effort levels are open to their users. [rn]
- **MOD-217** `documented` Model access is set at two levels: the organization switches each model on or off for all members, Owners and Admins included, and can limit the effort level of each model; a custom role passes on some of the models the organization has enabled and can lower a model's effort limit further but never raise it above the organization's. [org-models] [rbac]
- **MOD-218** `documented` The model settings of a role apply only to members with the role "Custom"; a member whose role is User, Admin or Owner has all models that the organization has enabled, each within the effort cap the organization has set. [org-models]
- **MOD-219** `documented` The Haiku models cannot be disabled, so every member always has access to them. [org-models] [rbac] [cc-model]
- **MOD-220** `documented` For a member with several custom roles, model access is additive and the highest effort cap among the roles applies, never above the organization's cap. [org-models] [cc-model]
- **MOD-221** `documented` A member's model picker lists only the models that member may use, and the effort menu leaves out levels above a cap. [org-models] [model-menu]
- **MOD-222** `documented` If a model is disabled while a member has it in an open conversation, the conversation continues on the member's default model when the member next opens it; if an effort cap is lowered below the level a member has selected, that member's following message on the model runs at the new cap. [org-models]
- **MOD-223** `documented` Model access settings are enforced in chat, Cowork, Claude Code, Claude Design, Claude Tag and Claude for Microsoft 365, and not yet in Claude in Chrome or Claude Security. [org-models]
- **MOD-224** `documented` An Enterprise organization can set a default model for all members or for a custom role, whose default takes precedence; that model is then the one on which new conversations begin in chat, Cowork, Claude Code, Claude Design, Claude Science and Claude for Office. [org-default]
- **MOD-225** `documented` Setting or changing a default model overwrites the selection in the model picker of every member; a user can still pick another model for any conversation, and unless the organization decides otherwise, the model a user picked last is also the one that user's next conversation starts on. [org-default]
- **MOD-226** `documented` A beta setting in Organization settings > Models, and in the role editor for a role's default, makes each new conversation begin with the default model and the default effort level, whatever the user chose last. [org-default]
- **MOD-227** `documented` The default is either a specific model or "Anthropic's recommended default", which follows new model releases by itself; a default effort level can be set with it, no higher than the effort cap for that model. [org-default]
- **MOD-228** `documented` When a member has several custom roles whose default models differ, the member gets the most capable of them; capability is ranked by model family first (Haiku, then Sonnet, then Opus) and by release date second. [org-default] [cc-model]
- **MOD-229** `documented` Claude Code receives an organization's model restrictions as part of the account's entitlements at authentication, and the server applies the same restrictions independently whenever a session is created; the `/model` picker does not list a restricted model. [cc-model]
- **MOD-230** `documented` In Claude Code the organization default only sets where a user starts and restricts nothing: it is outranked by the `--model` flag, by `ANTHROPIC_MODEL` and by any `model` value from managed settings, from `--settings` or from user, project or local settings, including one saved with `/model`; an admin can configure the default to override only the values from user, project and local settings. [cc-model]
- **MOD-231** `documented` A `model` value in Claude Code's managed settings takes precedence over the organization default in the Claude Code CLI and IDE. [org-default] [cc-model]
- **MOD-232** `conflicting` The Claude Code documentation gives v2.1.196 as the first Claude Code version that supports the organization default model, while the help center says CLI versions earlier than 2.1.199 do not pick up the organization default. [cc-model] [org-default]
- **MOD-233** `conflicting` The Claude Code documentation says organization model restrictions, which hide a restricted model from the picker, require Claude Code v2.1.187 or later and effort limits v2.1.195 or later, while the help center gives CLI version 2.1.199 or later and says that on earlier versions the picker still offers models and effort levels that have been disabled. [cc-model] [org-models]

## Model and effort in Claude Code

- **MOD-240** `documented` In Claude Code the `model` setting takes a model alias or a model name; the aliases are `best`, `fable`, `opus`, `sonnet`, `haiku` and `opusplan`, with 1M-context variants of `sonnet` and `opus`, and the special value `default` clears any override. [cc-model]
- **MOD-241** `documented` `best` selects the model behind `fable` for accounts that can use Fable and the model behind `opus` for all others. [cc-model]
- **MOD-242** `documented` On the Anthropic API, `opus` resolves to Opus 5.5 from Claude Code v2.1.280, `sonnet` to Sonnet 5.5 from v2.1.284 and `fable` to Fable 5.1 from v2.1.257; on other providers the aliases can resolve to older versions, for example to Opus 4.6 and Sonnet 4.5 on Microsoft Foundry. [cc-model]
- **MOD-243** `documented` The help center lists these models as supported in Claude Code: Fable 5.1 and Fable 5; Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6 and Opus 4.5; Sonnet 5.5, Sonnet 5, Sonnet 4.6 and Sonnet 4.5; and Haiku 4.5. [cc-model-help]
- **MOD-244** `documented` In Claude Code, `default` stands for Opus 5.5 for every plan (Pro, Max, Team, Enterprise) and for the Anthropic API, Google Cloud's Agent Platform, Amazon Bedrock and Claude Platform on AWS; on Microsoft Foundry it stands for Sonnet 4.5. [cc-model]
- **MOD-245** `documented` In versions of Claude Code older than v2.1.280, `default` stood for Sonnet 5 on Pro plans and Team Standard seats, and, from v2.1.219, for Opus 5 on Max plans, Team Premium seats, Enterprise plans and the Anthropic API; from v2.1.154 until v2.1.219 it stood for Opus 4.8 on Max plans, Team Premium seats, pay-as-you-go Enterprise plans and the Anthropic API. [cc-model]
- **MOD-246** `documented` In Claude Code, no plan and no provider has a Fable model as its default; a Fable model has to be selected explicitly, for example with `/model fable`. [cc-model]
- **MOD-247** `documented` According to the help center, Fable 5 requires Claude Code version 2.1.170 or later. [fable-plan]
- **MOD-248** `conflicting` The help center says Fable 5.1 requires Claude Code version 2.1.255 or later, while the Claude Code documentation says v2.1.257 or later. [fable-plan] [cc-model]
- **MOD-249** `documented` The model is chosen, in order of priority, by `/model` during a session, the `--model` flag at startup, the environment variable `ANTHROPIC_MODEL`, the `model` field of a settings file and, as the default for new sessions, `ANTHROPIC_DEFAULT_MODEL`. [cc-model]
- **MOD-250** `documented` `/model` makes the chosen model the default of future sessions: it writes the `model` field into the user settings; pressing `s` in the picker switches the model for the current session only, and `--model` and `ANTHROPIC_MODEL` apply only to the session launched with them. [cc-model]
- **MOD-251** `documented` `opusplan` assigns plan mode to `opus` and the execution that follows to `sonnet`. [cc-model]
- **MOD-252** `documented` Claude Code warns the user if the model asked for has a retirement date set, or if that model is mapped to a newer version automatically. [cc-model]
- **MOD-253** `documented` Administrators can restrict the selectable models with `availableModels` in managed settings; the list applies wherever a model can be specified, including the main session model and subagent, skill and advisor models, and excluded models are hidden from the `/model` picker. [cc-model]
- **MOD-254** `documented` Besides the per-role effort limits of Enterprise organizations, under which a request for a higher level through `--effort` or `/effort` is carried out at the cap, the managed setting `maxEffortLevel` caps effort on any plan and provider; where a model falls under both, the lower of the two caps counts. [cc-model]
- **MOD-255** `documented` In Claude Code, all five effort levels are offered by Fable 5.1 and Fable 5, by Opus 5.5, Opus 5, Opus 4.8 and Opus 4.7 and by Sonnet 5.5 and Sonnet 5; Opus 4.6 and Sonnet 4.6 offer them without `xhigh`, and the other models do not support effort. [cc-model]
- **MOD-256** `documented` If the active model lacks the chosen level, Claude Code steps down to the next lower level that the model supports, so a session set to `xhigh` runs at `high` on Opus 4.6. [cc-model]
- **MOD-257** `documented` The default effort in Claude Code is `medium` on Opus 5.5 and Sonnet 5.5, `xhigh` on Opus 4.7 and `high` on every other model that supports effort. [cc-model]
- **MOD-258** `documented` The effort level of a Claude Code session comes from the first of these that applies: a level chosen explicitly (through the `CLAUDE_CODE_EFFORT_LEVEL` variable, `--effort` or `/effort`), then the level saved in settings, then the model's default. [cc-model]
- **MOD-259** `documented` Effort is set with `/effort`, with the arrow keys in the `/model` picker, with `--effort`, with `CLAUDE_CODE_EFFORT_LEVEL` or in settings; a level of `low`, `medium`, `high` or `xhigh` confirmed with Enter in the slider or picker, or typed after `/effort`, is saved per model in the user settings, while `s` applies it to the current session only. [cc-model]
- **MOD-260** `documented` `max` applies to the current session only unless it is set through `CLAUDE_CODE_EFFORT_LEVEL`. [cc-model]
- **MOD-261** `documented` An `effort` value in a subagent's frontmatter takes the place of the session's effort level while that subagent is active; frontmatter effort, whether of a subagent or of a skill, yields to `CLAUDE_CODE_EFFORT_LEVEL` and stays under any effort cap. [cc-model]
- **MOD-262** `documented` Beside the model name, the session header displays the effort level that currently applies. [cc-model]
- **MOD-263** `documented` The word `ultrathink` anywhere in a prompt makes Claude Code add an in-context instruction for deeper reasoning on that turn; the API request carries the same effort level as before, and phrases such as "think hard" are not recognized as keywords. [cc-model]
- **MOD-264** `documented` Ultracode is not one of the effort levels but a setting of Claude Code: while it is on, Claude orchestrates dynamic workflows for tasks of some substance, at whatever effort level the session has. [cc-model]
- **MOD-265** `documented` In Claude Code, thinking cannot be switched off on the Fable models, Opus 5.5 or Sonnet 5.5; on other models it is toggled for the session with Option+T or Alt+T and globally in `/config`. [cc-model]
- **MOD-266** `documented` By default Claude Code shows thinking output collapsed, and in interactive sessions on the Anthropic API the thinking blocks arrive redacted unless `showThinkingSummaries` is set; collapsing or redacting does not reduce the charge, which covers every thinking token generated. [cc-model]
- **MOD-267** `documented` In Claude Code, adaptive reasoning is the only mode on the Fable models, on Sonnet 5 and later and on Opus 4.7 and later; Sonnet 4.6 and Opus 4.6 can be switched back to a fixed thinking budget with `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING`. [cc-model]

## Safeguards

- **MOD-280** `documented` Safety classifiers that are able to decline a request are built into Fable 5.1, Fable 5, Opus 5.5, Opus 5 and Sonnet 5.5. [api-refusals]
- **MOD-281** `documented` These classifiers run on every request and examine all that the model reads and not just the newest message, so memory, connector content, results of web searches and files are covered, and content the user never typed can cause a block or a fallback. [switch-fable] [switch-opus] [switch-sonnet]
- **MOD-282** `documented` The help center names four areas in which the classifiers of Fable 5 and Fable 5.1 are meant to hand a request to an Opus model: offensive cybersecurity techniques; much of what Anthropic regards as dual-use biology, with virology, toxicology and the design of drugs and molecules as examples; distillation attacks; and a narrow range of tasks in frontier LLM development. [switch-fable]
- **MOD-283** `documented` Fable 5.1 may be used to find vulnerabilities in software but not to write exploits for them; its safeguards still pass several kinds of dual-use security work on to Opus models, among them penetration tests, the generation of exploits and vulnerability scans that work on binaries. [news-fable51]
- **MOD-284** `documented` Anthropic states that the newest cybersecurity safeguards, those of Fable 5.1, produce 60% fewer false positives than their predecessors and that Claude Code users will on average see around 60% fewer interventions by them in a session than under the earlier safeguards of Fable 5. [news-fable51]
- **MOD-285** `documented` Opus 5.5 launched with safeguards of the class used on Fable 5.1, covering cybersecurity, biology and distillation, which no Opus model before it had at launch. [news-opus55]
- **MOD-286** `documented` Opus 5.5 itself still handles the finding and fixing of bugs in a user's own code that belongs to ordinary software development, while most cybersecurity tasks are passed to Opus 4.8. [news-opus55]
- **MOD-287** `documented` For biology, the safeguards of Opus 5.5 are those of Fable 5.1. [news-opus55]
- **MOD-288** `documented` Cybersecurity fallbacks came to the Sonnet line with Sonnet 5.5; in biology the model has the safeguards that Sonnet 5 already had. [switch-sonnet]
- **MOD-289** `documented` An organization that these safeguards hinder in its biology research can apply to the Life Sciences Verification Program; once vetted, it works under safeguards that are built to allow biology-related work in its whole range. [news-opus55] [switch-opus]
- **MOD-290** `documented` The biology classifier of the Fable models was updated on 2026-08-06 on Claude, the Claude apps and the Claude Platform, with the cloud providers to follow; Anthropic states that on harmless requests about basic biology and about medical questions the current biology safeguards of Fable 5.1 and Fable 5 trigger 85% less often than the safeguards Fable 5 started with. [switch-fable] [fable-page] [news-fable51]

## Model fallback in the Claude app and Claude Code

- **MOD-295** `documented` In the Claude app and Claude Code, automatic model switching is on by default: a request flagged in a category that has a fallback model is re-run on that model in the same conversation, the user is told of the switch in a notice, and a label on the response names the model that wrote it. [switch-fable] [switch-opus] [switch-sonnet] [cc-model]
- **MOD-296** `documented` From Opus 5.5, Fable 5.1 and Fable 5, a biology-flagged request falls back to Opus 5 and a cybersecurity-flagged request to Opus 4.8. [cc-model] [switch-fable] [switch-opus]
- **MOD-297** `documented` From Sonnet 5.5, a cybersecurity-flagged request falls back to Sonnet 5, and a biology-flagged request is refused, since no fallback model exists for biology on Sonnet 5.5. [cc-model] [switch-sonnet]
- **MOD-298** `documented` From Opus 5, a cybersecurity-flagged request falls back to Opus 4.8, and a biology-flagged request is refused. [cc-model] [switch-opus]
- **MOD-299** `documented` A request flagged for frontier LLM development moves from Opus 5.5 to Opus 5 and from Sonnet 5.5 to Sonnet 5; Opus 5 does not fall back in this category. [switch-opus] [switch-sonnet]
- **MOD-300** `documented` According to the help center, Opus 5, Opus 5.5 and Sonnet 5.5 block attempts to draw out the model's internal reasoning and do not hand such a request to a fallback model. [switch-opus] [switch-sonnet]
- **MOD-301** `conflicting` The Opus 5.5 announcement says that model's cybersecurity, biology and distillation safeguards all fall back to another model, while the help center says distillation blocks on Opus 5.5 do not fall back. [news-opus55] [switch-opus]
- **MOD-302** `documented` After a fallback, the model picker keeps showing the fallback model until the conversation ends or the user switches back, which is possible at any time; a Claude Code session likewise continues on the fallback model until the user returns with `/model`. [switch-fable] [switch-opus] [switch-sonnet] [cc-model]
- **MOD-303** `documented` A Claude Code session that has moved to a fallback model goes on at the effort level of the flagged request instead of the fallback model's default effort, unless a level from settings or an organization default for that model applies, or the user has since chosen a level or model or resumed the session. [cc-model]
- **MOD-304** `documented` Even the opening request of a Claude Code session can cause a fallback: it includes workspace context, for example the content of CLAUDE.md and the git status, and that context alone can set off a classifier. [cc-model]
- **MOD-305** `documented` The setting "Switch models when a message is flagged", under Settings > Capabilities in the Claude app and in `/config` in Claude Code, where the settings key is `switchModelsOnFlag`, turns automatic switching off; a flagged request then pauses the conversation, and the user can edit the message and retry or switch to the fallback model. [switch-fable] [switch-opus] [switch-sonnet] [cc-model]
- **MOD-306** `documented` In Claude Code, a flagged request ends with a refusal when the fallback model is excluded by `availableModels`, and also in non-interactive mode when automatic switching is turned off. [cc-model]
- **MOD-307** `documented` Automatic model switching works in Claude Desktop, Claude Mobile and Claude on the web, in Cowork, Claude Code, Claude for Microsoft 365, Claude Design and Claude Tag, and for Opus 5, Opus 5.5 and Sonnet 5.5 also in Claude Science. [switch-fable] [switch-opus] [switch-sonnet]
- **MOD-308** `documented` Separately from this content-based fallback, Claude Code can move to a configured fallback model if the primary model is unavailable or overloaded or answers with another server error that cannot be retried; the chain is set with `--fallback-model` or the `fallbackModel` setting, holds at most three models, and each switch is limited to the turn in which it happens. [cc-model]

## Refusals and fallback on the API

- **MOD-315** `documented` On the API a refusal is not an error but a response with HTTP status 200 whose `stop_reason` is `refusal`; the `category` in its `stop_details` object names the policy area, which is `cyber`, `bio`, `frontier_llm`, `reasoning_extraction` or `general_harms`, or is `null` when the refusal maps to no named category. [api-refusals]
- **MOD-316** `documented` A refusal comes either at the very start, with no output yet, or in the middle of a stream, when part of the output has already been sent. [api-refusals]
- **MOD-317** `documented` On Opus 5.5, Opus 5, Sonnet 5.5, Fable 5.1 and Fable 5, a request that pushes the model to put its internal reasoning into the visible answer can be refused under the category `reasoning_extraction`; the API documentation names no fallback model for this category and advises rewording the prompt rather than sending the request again. [api-thinking] [api-refusals] [api-opus55-new]
- **MOD-318** `documented` On the API nothing switches models automatically: a caller has to opt in and configure fallbacks, and until then a declined request comes back as a refusal. [switch-fable] [fable-page]
- **MOD-319** `documented` Server-side fallback, in beta on the Claude API, runs a declined request again inside the same API call, on the model that Anthropic recommends for the category of the refusal (`fallbacks: "default"`) or on up to three models the caller names; the Message Batches API, Microsoft Foundry, Google Cloud and Amazon Bedrock do not offer it. [api-refusals]
- **MOD-320** `documented` Server-side fallback reacts only to a decline by a safety classifier; if the requested model answers with a rate limit, an overload or a server error, the caller receives that result unchanged. [api-refusals]
- **MOD-321** `documented` On the API, Opus 4.8 and Opus 5 are the only models that a Fable 5.1 request is permitted to fall back to. [api-fable51-new]
- **MOD-322** `documented` In a response served by server-side fallback after a decline, the top-level `model` field names the model that answered and the content contains a `fallback` block at the point of the handoff; a turn routed straight to the fallback model carries no such block. [api-refusals]
- **MOD-323** `documented` After a conversation has fallen back, later requests for it that include `fallbacks` go straight to the fallback model for about an hour, which the documentation calls sticky routing. [api-refusals]
- **MOD-324** `documented` If a refusal comes before the model has produced output, it is charged only in the categories `bio`, `frontier_llm` and `reasoning_extraction`, in which Anthropic measured few false positives as of September 2026, and the charge follows the prices of the model that handled the request. [api-refusals] [api-fable51-new]
- **MOD-329** `documented` A refusal before any output in another category or with no category is not charged, but it still counts against rate limits. [api-refusals]
- **MOD-325** `documented` The help center states the same rule for the Claude app: when the classifier for biology, for distillation or for frontier LLM development stops a request or makes it fall back before any output, the refusal is billed. [switch-fable] [switch-opus] [switch-sonnet]
- **MOD-326** `documented` From 2026-06-02 the Claude API did not charge for a refusal that came before any output; since 2026-09-24 such refusals have been charged again in the categories `bio`, `frontier_llm` and `reasoning_extraction`, on every platform. [api-rn] [api-fable51-new]
- **MOD-327** `documented` For a refusal in the middle of a stream, the caller pays the regular price for the input tokens and for the output that had been streamed up to that point. [api-refusals] [api-fable51-new]
- **MOD-328** `documented` The fallback request is billed separately, at the prices of the model that answers, and a fallback credit compensates for its prompt-cache miss. [api-refusals] [api-fable51-new] [switch-fable]

## Watermark and data retention

- **MOD-335** `documented` On every platform where Fable 5.1 and Mythos 5.1 are offered, the text they generate contains Anthropic's statistical watermark for text, and Opus 5.5 comes with the same watermarking measures. [api-fable51-new] [news-opus55]
- **MOD-336** `documented` The watermark alters neither what the output means nor how good or readable it is, inserts neither tokens nor hidden characters, and encodes nothing about the user or the organization. [api-fable51-new] [news-fable51]
- **MOD-337** `documented` According to the Fable 5.1 announcement, Anthropic added the watermark to the output of models released after 2026-08-02 because the code of practice on the transparency of AI-generated content under the EU AI Act, which it has signed, requires this; nobody without the detection API can see the watermark. [news-fable51]
- **MOD-340** `documented` Opus 5.5, Opus 5 and Sonnet 5.5 are available with zero data retention. [news-opus55] [switch-opus] [switch-sonnet]

## Pricing

- **MOD-350** `documented` On the API, the prices per million input and output tokens are $10 and $50 for Fable 5.1, $4 and $20 for Opus 5.5, $2 and $10 for Sonnet 5.5, and $1 and $5 for Haiku 4.5. [api-models] [api-pricing]
- **MOD-351** `documented` Among the older models, the prices per million input and output tokens are $10 and $50 for Fable 5, $5 and $25 for Opus 5, Opus 4.8, Opus 4.7, Opus 4.6 and Opus 4.5, $2 and $10 for Sonnet 5, and $3 and $15 for Sonnet 4.6 and Sonnet 4.5. [api-pricing]
- **MOD-352** `documented` Cache reads cost $0.25 per million tokens on Fable 5.1, $0.20 on Opus 5.5, $0.20 on Sonnet 5.5 and $0.10 on Haiku 4.5. [api-pricing]
- **MOD-353** `documented` Relative to a model's base input price, a cache read costs 0.025 times as much on Fable 5.1 and Mythos 5.1, 0.05 times as much on Opus 5.5 and 0.1 times as much on the other models. [api-pricing] [api-models]
- **MOD-354** `documented` Cache writes cost 1.25 times the base input price for the 5-minute cache and 2 times for the 1-hour cache, which is $12.50 and $20 per million tokens on Fable 5.1 and $5 and $8 on Opus 5.5. [api-pricing]
- **MOD-355** `documented` The Batch API halves the input and output prices, to $5 and $25 per million tokens on Fable 5.1, $2 and $10 on Opus 5.5, $1 and $5 on Sonnet 5.5 and $0.50 and $2.50 on Haiku 4.5. [api-pricing]
- **MOD-356** `documented` There is no long-context surcharge: on Claude 4.6 and later models, tokens anywhere in the 1M-token window are billed at the same standard per-token prices. [api-pricing] [api-ctx]
- **MOD-357** `documented` US-only inference, requested with `inference_geo`, costs 1.1 times the standard price on Claude 4.6 and later models. [api-pricing]
- **MOD-358** `documented` Anthropic states, on the basis of its tests, that typical workloads at default settings cost 40% less on Opus 5.5 than on Opus 5: its input and output prices are 20% lower, its cache reads 60% lower, and it uses fewer tokens per task. [news-opus55]
- **MOD-359** `documented` Fable 5.1 kept the input and output prices of Fable 5, and its cache reads cost 75% less, $0.25 instead of $1 per million tokens; by Anthropic's estimate this makes typical workloads about 25% cheaper and highly agentic workloads up to about 45% cheaper. [news-fable51] [api-pricing]
- **MOD-360** `documented` The prices of $2 and $10 for Sonnet 5, announced as introductory pricing through 2026-08-31, became its standard prices; the increase to $3 and $15 that was scheduled for 2026-09-01 did not take place. [api-pricing]

## Fast mode

- **MOD-365** `documented` Fast mode is a research preview that delivers up to 2.5 times more output tokens per second at premium prices; the gain is in output speed, not in the time to the first token. [api-fast]
- **MOD-366** `documented` The models that support fast mode are Opus 5.5, Opus 5 and Opus 4.8; a fast-mode request to Opus 4.7 returns an error, and one to Opus 4.6 runs at standard speed and is billed at standard rates. [api-fast] [api-choose]
- **MOD-367** `documented` In fast mode, a million input tokens cost $8 and a million output tokens $40 on Opus 5.5; on Opus 5 and Opus 4.8 the prices are $10 and $50. [api-fast] [api-pricing] [news-opus55]
- **MOD-368** `documented` Fast mode is offered through the Claude API, Claude Managed Agents included, and, according to the Opus 5.5 announcement, in Claude Code; it is absent from Microsoft Foundry, Google Cloud, Amazon Bedrock and Claude Platform on AWS, and it cannot be combined with the Batch API. [api-fast] [news-opus55]
- **MOD-369** `documented` In fast mode the model weights are the same and neither intelligence nor capabilities change, and a prompt cached at one speed, fast or standard, cannot be used by a request at the other. [api-fast]

## Availability by plan

- **MOD-375** `documented` Every paid plan, that is Pro, Max, Team and Enterprise, lets its users work with Fable 5 and Fable 5.1, and the help center says Fable 5 is not available on the Free plan; the same article names an organization that has not enabled the Fable models as one reason a user does not see them. [fable-plan] [fable-page]
- **MOD-376** `documented` On Max plans and on premium seats of Team and seat-based Enterprise plans, the Fable models are part of the plan: as much as half of the weekly usage limits may go to them without additional charge. [fable-plan]
- **MOD-377** `documented` Where Fable is part of a plan, Fable usage and the use of other models are counted against one and the same weekly limit, which Fable uses up faster; the 50% share is not an addition to that limit. [fable-plan]
- **MOD-378** `documented` A user who has used up the Fable part of a plan can go on with the Fable models by paying with usage credits, or change to a different model and remain inside the plan's limits. [fable-plan]
- **MOD-379** `documented` On Pro plans and on standard seats of Team and seat-based Enterprise plans, the plan's usage limits do not cover the Fable models, so every use of them is paid with usage credits; on Enterprise standard seats this requires the organization to have enabled usage credits. [fable-plan]
- **MOD-380** `documented` Fable usage costs the standard API rates on usage-based Enterprise plans and on the API. [fable-plan]
- **MOD-381** `documented` A promotion under which subscribers could spend up to 50% of their weekly limit on Fable 5 without paying extra ended on 2026-07-19; since then Fable 5 has run on usage credits on Pro plans and on Team standard seats, and the promotion never covered Fable 5.1. [fable-plan]
- **MOD-382** `documented` Fable models can be used in Claude Desktop, Claude Mobile and Claude on the web, in Cowork, Claude Code, Claude for Microsoft 365, Claude Design and Claude Tag; in Cowork they work only with the newest version of Claude Desktop. [fable-plan]
- **MOD-383** `documented` Depending on plan and seat tier, Fable usage in Claude Code is charged to usage credits and not taken from the limits included in the plan. [cc-model]
- **MOD-387** `documented` When Fable usage is charged to usage credits, the `/model` picker of Claude Code marks the Fable row "Requires usage credits". [cc-model]
- **MOD-388** `documented` An interactive Claude Code session asks for consent before a Fable request is charged to usage credits, except for members of Enterprise plans with organization billing. [cc-model]
- **MOD-384** `documented` Claude Code does not ask for this consent in non-interactive mode (`-p`) or inside an Agent SDK application that leaves the prompt out; a Fable request is then charged to usage credits unasked. [cc-model]
- **MOD-385** `documented` The consent prompt is not shown to Enterprise members whose plan uses organization billing, and after a user has chosen to continue on Fable with usage credits, Claude Code does not show it again. [cc-model]
- **MOD-386** `documented` In the Claude app, users on the Pro, Max, Team and Enterprise plans have Opus 5.5. [opus-page]

## Anthropic's own comparisons of Opus 5.5 and Fable 5.1

- **MOD-390** `documented` In the benchmark table of Anthropic's Opus 5.5 announcement, Opus 5.5 scores higher than Fable 5.1 on all nine benchmarks that list both models. [news-opus55]
- **MOD-391** `documented` Anthropic's figures in that table, for Opus 5.5 and Fable 5.1 in this order, are 66.4% and 55.8% on Terminal-Bench 4.0, 54.4% and 50.3% on FrontierCode v1.1, 57.8% and 51.8% on CursorBench 4.0, 1846 and 1735 Elo on GDPval-AA v2.1, 40.0% and 31.4% on AutomationBench, 67.7% and 65.6% on Humanity's Last Exam with tools, 58.7% and 52.6% on Terminal-Bench-Science 0.1, 81.8% and 80.7% on OSWorld 2.1, and 89.0% and 88.4% on Chartography. [news-opus55]
- **MOD-392** `documented` For that table Opus 5.5 ran with adaptive thinking at `max` effort on every benchmark except Terminal-Bench 4.0, where the reported result is at `xhigh`. [news-opus55]
- **MOD-393** `documented` Anthropic ran the Opus 5.5 benchmarks with the model's production safeguards switched on: a task on which they stepped in was finished by Opus 4.8 if it concerned cybersecurity and by Opus 5 if it concerned biology or frontier LLM development, which according to Anthropic likely lowers the scores; the Fable 5.1 announcement carries a similar note. [news-opus55] [news-fable51]
- **MOD-394** `documented` Anthropic states that between models this capable a lead in a benchmark says less than it used to about differences in real use, and that in Anthropic's own work Opus 5.5 and Fable 5.1 lie closer together than their scores indicate. [news-opus55]
- **MOD-395** `documented` On CursorBench 4.0, according to Anthropic, Opus 5.5 scores 52.5% at `medium`, its default effort, against 51.8% for Fable 5.1 at `max` and 46.6% for Opus 5 at `max`. [news-opus55]
- **MOD-396** `documented` In an internal Anthropic test, Opus 5.5 and Fable 5.1 each translated HAProxy from C to Rust, and the regression tests of HAProxy passed almost completely on both results; Opus 5.5 needed 9.5 hours and Fable 5.1 12 hours, and the Opus 5.5 run was 51% cheaper. [news-opus55]
- **MOD-397** `documented` In an internal Anthropic test of research reports written from web sources, 16 of 18 reports by Opus 5.5 cleared a quality bar under which any invented figure or quote fails; no attempt by Fable 5.1 or Opus 5 cleared it. [news-opus55]
- **MOD-398** `documented` On a 478-problem subset of SWE-bench Pro, whose scores Anthropic says cannot be compared with the public leaderboard, Opus 5.5 at `medium`, its default effort, solved 92.8% and Fable 5.1 at its own default 92.3%, which is within the variation between runs; a solved task cost $0.22 on Opus 5.5 and $1.19 on Fable 5.1, roughly five times as much. [api-cost]

## Sources

[api-choose]: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
[api-cost]: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
[api-ctx]: https://platform.claude.com/docs/en/build-with-claude/context-windows
[api-deprec]: https://platform.claude.com/docs/en/about-claude/model-deprecations
[api-effort]: https://platform.claude.com/docs/en/build-with-claude/effort
[api-fable51]: https://platform.claude.com/docs/en/models/fable-5-1/overview
[api-fable51-new]: https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
[api-fast]: https://platform.claude.com/docs/en/build-with-claude/fast-mode
[api-haiku45]: https://platform.claude.com/docs/en/models/haiku-4-5/overview
[api-ids]: https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions
[api-models]: https://platform.claude.com/docs/en/models/overview
[api-mythos51]: https://platform.claude.com/docs/en/models/mythos-5-1/overview
[api-opus55]: https://platform.claude.com/docs/en/models/opus-5-5/overview
[api-opus55-new]: https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5
[api-preserved]: https://platform.claude.com/docs/en/build-with-claude/preserved-thinking
[api-pricing]: https://platform.claude.com/docs/en/about-claude/pricing
[api-prompt-fable51]: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
[api-refusals]: https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback
[api-rn]: https://platform.claude.com/docs/en/release-notes/overview
[api-sonnet55]: https://platform.claude.com/docs/en/models/sonnet-5-5/overview
[api-thinking]: https://platform.claude.com/docs/en/build-with-claude/thinking
[cc-model]: https://code.claude.com/docs/en/model-config
[cc-model-help]: https://support.claude.com/en/articles/11940350-claude-code-model-configuration
[cvp]: https://support.claude.com/en/articles/14604842-cyber-verification-program
[fable-page]: https://www.anthropic.com/claude/fable
[fable-plan]: https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
[model-menu]: https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings
[news-fable-access]: https://www.anthropic.com/news/fable-mythos-access
[news-fable51]: https://www.anthropic.com/claude-fable-and-mythos-5-1
[news-opus55]: https://www.anthropic.com/claude-opus-5-5
[opus-page]: https://www.anthropic.com/claude/opus
[org-default]: https://support.claude.com/en/articles/15330088-set-a-default-model-for-your-organization
[org-models]: https://support.claude.com/en/articles/15694740-manage-model-access-for-your-organization
[rbac]: https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans
[rn]: https://support.claude.com/en/articles/12138966-release-notes
[switch-fable]: https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5-or-fable-5-1
[switch-opus]: https://support.claude.com/en/articles/16049681-why-claude-switched-models-in-your-conversation-with-opus-5-or-opus-5-5
[switch-sonnet]: https://support.claude.com/en/articles/17161993-why-claude-switched-models-in-your-conversation-with-sonnet-5-5
[training-data]: https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data

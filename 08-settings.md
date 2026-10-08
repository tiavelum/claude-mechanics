# 08 Settings

Prefix: SET · Scope: account, project, per-chat and organization settings in the Claude app, including roles and account administration · Last checked: 2026-10-07

## Account settings

- **SET-001** `documented` Settings > Memory > "Generate memory from chats" turns memory on or off for the account, with "Pause memory" and "Reset memory" as the ways to turn it off. [mem]
- **SET-002** `documented` Settings > Memory > "Search and reference chats" turns chat search on or off. [mem]
- **SET-003** `documented` Settings > Memory > "Include sensitive topics in memory" lets Claude store sensitive topics from then on. [mem]
- **SET-004** `documented` Settings > Memory lists everything remembered under Topics, editable one by one. [mem]
- **SET-005** `documented` Settings > Memory > "Start import" adds pasted memory from another assistant; memory import is offered on Free, Pro, Max and Team, on the web and Claude Desktop. [imp]
- **SET-006** `documented` In the new Claude experience, Settings > General > "Instructions for Claude" holds the instructions that apply to every conversation, including the former Cowork Global instructions. [one]
- **SET-007** `documented` Settings > General > "Only on your computer" for Cowork tasks is removed from 2026-10-06 for Pro and Max. [cw-web]
- **SET-008** `documented` On Free, Pro and Max, an account's data export is started in Settings > Privacy in Claude Desktop or on the web, not in the iOS or Android apps; members of Team and Enterprise organizations have no export of their own. [exp] [exp-org]
- **SET-009** `documented` On Pro, Max, Team and seat-based Enterprise plans, Settings > Usage shows how much of the five-hour session limit and the weekly limits has been used; on usage-based Enterprise plans it tracks consumption instead. [usage]
- **SET-010** `documented` In the legacy memory experience, memory and chat search were in Settings > Capabilities instead of Settings > Memory. [mem]
- **SET-011** `documented` Settings > Reflect shows a monthly recap of how the account has used Claude; it is in beta on Free, Pro and Max on the web and Claude Desktop, and is not available on Team, Enterprise or Claude Mobile. [recap] [rn]
- **SET-012** `documented` The monthly recap is built from the same chat history as memory and appears only while memory is on; it has no toggle of its own, so turning memory off hides it. [recap] [rn]
- **SET-013** `documented` In the legacy memory experience, pausing or resetting memory also hides the monthly recap. [mem]
- **SET-014** `conflicting` The monthly recap article says the recap is turned off by switching off "Generate memory from chat history" in Settings > Capabilities, while the memory article puts the current switch, "Generate memory from chats", in Settings > Memory and places memory in Settings > Capabilities only for the legacy experience. [recap] [mem]
- **SET-015** `documented` Break reminders and quiet hours, a beta for Free, Pro and Max, are set under Settings > Time and focus in Claude Desktop or on the web, and then apply on the web, in Claude Desktop and in Claude Mobile. [focus]

## Per-project settings

- **SET-020** `documented` A project has its own instructions and knowledge, set on the project's page. [proj]
- **SET-021** `observed` Claude's runtime instructions describe a per-project memory setting, connected or separate, that is changed on the project's page on the web and that Claude itself cannot change. (session 2026-10-06, claude.ai, outside projects)

## Per-chat settings

- **SET-030** `documented` "+" > "Memory" turns memory off for one chat or task, before the first message only. [mem]
- **SET-031** `documented` The ghost icon in a new chat outside a project starts an incognito chat. [inc]
- **SET-032** `documented` In a conversation, "+" > Connectors lists each connected connector with a toggle that decides whether Claude can use it in that conversation. [conn]

## Capabilities that change context behaviour

- **SET-042** `documented` On Free, Pro and Max, "Code execution and file creation" is on by default and is switched in Settings > Capabilities, on the web, in Claude Desktop and in Claude Mobile. [files]
- **SET-043** `documented` On Team, and in new Enterprise organizations, code execution and file creation is on by default for the organization, and an owner can turn it off for everyone. [files]

## Organization settings (Team and Enterprise)

- **SET-050** `documented` Owners and Primary Owners switch organization memory on in Organization settings > Capabilities; turning it off deletes all members' memory. [mem]
- **SET-051** `documented` The project sharing switches sit in the Sharing section of Organization settings > Data and privacy; on Enterprise, the per-role switch is the Share projects toggle on a role's Capabilities tab under Organization settings > Roles. [share-org]
- **SET-052** `conflicting` Both export articles say only the Primary Owner of a Team or Enterprise organization can export its data, in Claude Desktop or on the web under Organization settings > Data and privacy, while the incognito article says organizational exports are available to account Owners. [exp-org] [exp] [inc]
- **SET-053** `documented` On Team and Enterprise, Cowork is on by default, and an Owner or Primary Owner can switch it off for all members with the "Enable for your organization" toggle in Organization settings > Cowork. [cw-org]
- **SET-054** `documented` In an organization that has enabled HIPAA, Cowork starts off, and an Owner switches it on in Organization settings > Cowork. [cw-org]
- **SET-055** `documented` On Enterprise, a feature that custom roles control reaches a member only if it is on for the organization and one of the member's custom roles grants it; no custom role can grant a feature that is off for the organization. [roles] [rbac]

## Account administration

- **SET-070** `documented` On the web, an account is deleted from Settings > Account with the "Delete account" button. [del]
- **SET-071** `documented` Members of Claude for Work or Claude for Enterprise organizations, and Console users, must ask the account's Primary Owner, an Owner or their account manager to have their account deleted. [del-org]
- **SET-072** `documented` When a personal account is moved into a Team or Enterprise workspace, the memory that Claude holds from chats and projects moves with it, unless the organization has turned memory off. [migrate]
- **SET-073** `documented` Moving a personal account's content into a Team or Enterprise workspace cannot be reversed: the moved content cannot return to a personal account. [migrate]

## Identity and access (Team and Enterprise)

- **SET-080** `documented` Single sign-on is available to Team, Enterprise and Console organizations; on Team and Enterprise an Owner or Primary Owner sets it up under Organization settings > Organization and access, and in the Console an Admin does so under Identity and access. [sso]
- **SET-081** `documented` SSO needs the organization's domains verified first, each by a DNS TXT record whose value begins with `anthropic-domain-verification-`; an organization can verify several domains, all managed by one identity provider, and verifying a domain alone does not affect existing users. [sso]
- **SET-082** `documented` SSO becomes mandatory only through two separate toggles, "Require SSO for Claude" and "Require SSO for Console"; without them, users may sign in with SSO or with email. [sso]
- **SET-083** `documented` Domain verification, SSO and provisioning belong to a parent organization, which several Claude and Console organizations under one identity provider can share, while billing and usage tracking stay with each organization; Enterprise gets a parent organization automatically, Team when it first turns on SSO, and the Console on request. [sso-prep]
- **SET-084** `documented` Once a domain is verified, the "Restrict organization creation" toggle stops anyone from creating new Claude or Console organizations, personal accounts included, with that domain. [sso] [sso-prep]
- **SET-085** `documented` Members join by invitation only by default; just-in-time provisioning, on Team, Enterprise and Console, creates an account with the User role at a user's first SSO login, and SCIM, on Enterprise and Console but not Team, adds and removes members from the identity provider's assignments without waiting for a login. [scim] [sso-prep]
- **SET-086** `documented` With group mappings on, groups in the identity provider set each member's role and seat tier: under just-in-time provisioning at each login, with the highest role among the member's groups, and under SCIM as group membership changes. [scim]
- **SET-087** `documented` Under just-in-time provisioning, a user unassigned in the identity provider can no longer sign in but keeps membership and seat until an admin removes them, and a member removed only in Claude returns at the next SSO login; under SCIM, removal in the identity provider removes the member. [scim]
- **SET-088** `documented` The roles that provisioning assigns are Owner, Admin and User on Team, with Custom added on seat-based Enterprise, and Admin, Developer, Limited Developer, Billing, Claude Code User and User in the Console; the one Primary Owner is exempt from SCIM and is changed only by the current Primary Owner under Organization settings > Members. [scim] [members]
- **SET-089** `documented` With "Require SSO for Claude" on, users not added to the SSO application can no longer reach their personal accounts on the domain, which are not deleted; users who are added keep their Free, Pro, Max or Team accounts alongside the organization and switch between them. [sso-prep]
- **SET-090** `documented` A removed member loses access at once and frees the seat, without the plan's seat count changing, and a member re-added with the same email address keeps the account history; Owners and Primary Owners cannot remove themselves. [members]
- **SET-091** `documented` Domain capture, the setting "Migrate accounts using your domain" under Organization settings > Organization and access > Security, is available on Enterprise only, requires a verified domain with restricted organization creation, enforced SSO and just-in-time or SCIM provisioning, cannot be undone, and allows no non-Enterprise accounts on the domain. [claim]
- **SET-092** `documented` When a claim starts, the owners of personal Free, Pro and Max accounts on the domain are notified and get one 30-day window to merge their chats, projects, files and memory into a new Enterprise account or to join with a clean one; at the deadline the remaining accounts are deactivated, their data is emailed to them, and their Pro and Max subscriptions are cancelled with a prorated refund. [claim]
- **SET-093** `documented` Team organizations can verify a domain and block new personal accounts on it, but cannot claim existing ones; in HIPAA-ready organizations and those with customer-managed encryption keys, claimed users can only join with a clean account. [claim]

## Audit logs

- **SET-100** `documented` Audit logs exist on Enterprise only: Owners and Primary Owners export them with "Export logs" under Organization settings > Data and privacy, and receive an email whose download link works for 24 hours. [audit]
- **SET-101** `documented` An audit log export covers the past 180 days, and each record gives the time, the actor, the event and its details, the entity, the IP address, the device ID, the user agent and the client platform. [audit]
- **SET-102** `documented` Audit logs record sign-ins and sign-outs, changes to projects and their knowledge documents, the creation, renaming and deletion of chats, file uploads, invitations and member removals, and changes to SSO, just-in-time provisioning, domain verification and data exports; chats and projects appear only by identifier, without titles or content. [audit]
- **SET-103** `documented` An Enterprise organization that uses customer-managed encryption keys cannot export audit logs; audit log events are also available through the Compliance API. [audit]
- **SET-104** `documented` The Activity Feed of the Compliance API, for Enterprise and Console organizations, returns per-event activity records within a minute of the event and keeps them for 6 years; recording begins when the Compliance API is first enabled for the organization and earlier activity is not backfilled. [compliance-feed]
- **SET-105** `documented` The Compliance API documentation calls the audit log export significantly narrower than the Activity Feed, with a capped lookback window. [compliance]

## What Claude is told about settings

- **SET-060** `observed` Claude could not change any of these settings itself; when asked to stop using memory or past chats, it was instructed to name the setting and stop using the tools for the rest of the conversation. (session 2026-10-06, claude.ai, outside projects)
- **SET-061** `observed` The session's instructions carried a "Preferred browser" line naming the built-in browser and said it comes from a user setting of that name, which the user can change at any time. (session 2026-10-06, claude.ai, outside projects)
- **SET-062** `observed` The session's instructions listed web search, searching and referencing past chats, and generating memory from chat history as features the user can turn on or off in the conversation or in settings. (session 2026-10-06, claude.ai, outside projects)

## Sources

[audit]: https://support.claude.com/en/articles/9970975-access-audit-logs
[claim]: https://support.claude.com/en/articles/14625619-claim-and-migrate-accounts-on-your-domain
[compliance]: https://platform.claude.com/docs/en/manage-claude/compliance-api
[compliance-feed]: https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed
[conn]: https://claude.com/docs/connectors/getting-started
[cw-org]: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
[cw-web]: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
[del]: https://support.claude.com/en/articles/9028421-delete-your-claude-account
[del-org]: https://privacy.claude.com/en/articles/7996865-deleting-commercial-anthropic-accounts
[exp]: https://support.claude.com/en/articles/9450526-export-your-claude-data
[exp-org]: https://support.claude.com/en/articles/13346720-export-your-organization-s-data
[files]: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
[focus]: https://support.claude.com/en/articles/15672868-set-break-reminders-and-quiet-hours
[imp]: https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude
[inc]: https://support.claude.com/en/articles/12260368-use-incognito-chats
[members]: https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans
[migrate]: https://support.claude.com/en/articles/9267400-move-your-personal-claude-account-to-a-team-or-enterprise-organization
[mem]: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[one]: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
[proj]: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
[rbac]: https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans
[recap]: https://support.claude.com/en/articles/15672559-see-your-monthly-recap
[rn]: https://support.claude.com/en/articles/12138966-release-notes
[roles]: https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans
[scim]: https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning
[share-org]: https://support.claude.com/en/articles/9927533-control-project-sharing-for-your-organization
[sso]: https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso
[sso-prep]: https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning
[usage]: https://support.claude.com/en/articles/9797557-usage-limit-best-practices

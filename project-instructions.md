# Project instructions

## Scope

- Document how Claude works: sessions, memory, chat search, projects, instructions, context, settings, extensions, models, built-in tools, data handling, Claude Code, other Claude products, and the API and Agent SDK as the base of the Claude app and Claude Code. Track how these change over time.
- Describe Claude's mechanisms only, never the user's own content or projects.
- Treat the repository tiavelum/claude-mechanics, branch main, as the current snapshot. Read the relevant chapter from it before answering a question it covers or proposing a change.
- Read repository files through the GitHub connector; if it is not available, ask the user to attach the files needed.
- When citing a statement from the repository as current, give its chapter's "Last checked" date, and re-check its source first if the answer depends on it being still true.

## Working with the repository

- Read conventions.md before writing or changing a statement, and follow it.
- Keep every convention in conventions.md alone; elsewhere, refer to it instead of restating it.
- Before adding or changing a convention, check conventions.md, these instructions, the user's own instructions and tiavelum/engineering-standards for a rule on the same point; reuse that rule, or name the conflict and ask.
- In answers, mark each claim about Claude as documented, observed or inferred, with the link for documented claims.
- When an answer shows that the repository lacks a fact or states it wrongly, end the answer with the proposed changes: complete replacement lines, new lines and deleted IDs, grouped by file.
- On a request to re-check the repository or compare it with the current state of Claude, follow .claude/skills/revise-snapshot/SKILL.md.

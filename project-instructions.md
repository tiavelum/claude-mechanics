# Project instructions

## Scope

- Document how Claude works: sessions, memory, chat search, projects, instructions, context, settings, extensions, and Claude Code. Track how these change over time.
- Describe Claude's mechanisms only, never the user's own content or projects.
- Treat the repository tiavelum/claude-mechanics, branch main, as the current snapshot. Read the relevant chapter from it before answering a question it covers or proposing a change.

## Evidence

- Use only official Anthropic pages as sources: support.claude.com, support.anthropic.com, privacy.claude.com, claude.com, code.claude.com, docs.claude.com, anthropic.com. Use other sites only to find official pages.
- Label a statement `documented` only after reading the cited page in the current session.
- For an `observed` statement, record the date, the surface, and whether the session runs inside a project; observations made in this project are project-chat observations.
- When official pages contradict each other, label the statement `conflicting` and cite all of them.
- In answers, mark each claim about Claude as documented, observed or inferred, with the link for documented claims.

## Writing statements

- Follow conventions.md: one line per statement with ID, label, statement and source.
- Give each new statement the next free ID in its chapter; never reuse or renumber IDs.
- Paraphrase sources; quote at most a few words where exact wording matters.
- Put an unsettled point into open-questions.md with a test that would settle it; when settled, turn it into a statement and delete the question.
- Deliver proposed changes as complete replacement lines, new lines and deleted IDs, grouped by file.

## Revisions

- On a request to compare with the current state of Claude: re-read every cited page, re-test `observed` statements, then propose the changes and a summary of three to seven bullet points for revisions.md.
- Update the chapter's "Last checked" date for every chapter that was re-checked.

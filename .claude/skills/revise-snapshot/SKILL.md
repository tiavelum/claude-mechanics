---
name: revise-snapshot
description: Re-check every statement of the claude-mechanics knowledge base against the current state of Claude, deliver the result as a pull request, and publish it as a snapshot release with change notes. Use when asked to revise, re-check or update the repository, or to find out how Claude has changed since the last snapshot.
---

# Revise snapshot

Follow conventions.md throughout. The scripts are in `scripts/` next to this file and run with `python3` from any directory.

## 1. Prepare

1. Find the previous snapshot: the newest tag matching `v*` (`git tag --list 'v*' --sort=-creatordate | head -1`).
2. Set the new snapshot name to `v` plus today's date as `YYYY.MM.DD`.
3. Create the branch `revision/<snapshot name>` from an up-to-date `main`.
4. Run `scripts/check-statements.py`; fix any problem before starting, in a separate commit.

## 2. Re-check documented and conflicting statements

1. Run `scripts/list-sources.py` to get every cited page with the statements that cite it.
2. Read each page once in this session and check every statement that cites it.
3. Per statement, keep it, reword it, change its label, or delete it, as conventions.md defines.
4. Classify each change as either a change in Claude (the page now says something different) or a correction (the repository misread the page or overstated it). Keep that classification for the release notes.
5. Add new facts the pages now state that fall within a chapter's scope.
6. List pages that no longer load, and the statements that depend on them; do not delete those statements for that reason alone.
7. Search the official domains for pages that newly cover a chapter's scope or an open question, and use them in the same way.

## 3. Re-test observed statements

1. Take the observed statements from the output of `scripts/list-sources.py`.
2. Check each one against this session and update it with a new session note. If this session cannot show it (wrong surface, inside or outside a project), leave it unchanged and list it as not re-tested.

## 4. Settle what follows

1. Re-check every `inferred` and scenario statement whose basis changed.
2. Re-check each open issue labelled `open-question`; settle the ones the new evidence answers, and open new issues for points that remain unsettled.
3. Add dated changes found on the release notes page or elsewhere to `11-timeline.md`.
4. Update *Last checked* in every chapter header.
5. Run `scripts/check-statements.py` until it reports no problems.

## 5. Draft the release notes

1. Run `scripts/diff-statements.py <previous snapshot>` for the statement-level change list.
2. Write the release notes with these sections, in this order:
   - **What changed in Claude**: three to seven bullets, each naming the affected statement IDs.
   - **Corrections**: mistakes of the previous snapshot that were fixed, one bullet each, kept apart from changes in Claude.
   - **Not re-checked**: pages that did not load and observed statements that could not be re-tested.
   - **Open questions**: issues settled by this snapshot, with links, and new issues opened.
   - **Statement changes**: the output of `scripts/diff-statements.py`.
3. For the first snapshot, replace the sections on changes, corrections and statement changes with "Initial snapshot" and the statement counts per label.

## 6. Open the pull request

1. Commit the changes on the revision branch and push it.
2. Open a pull request into `main` titled `Snapshot <snapshot name>`, with the release notes as its description and `Closes #<number>` for each settled issue.
3. Tell the user that the changed documents can be reviewed and commented in the pull request, and stop until they have reviewed it.
4. Apply requested changes on the same branch, re-run step 5, and update the pull request description.

## 7. Publish the snapshot

After the user has merged the pull request and asked for the snapshot to be published:

1. Tag the merge commit on `main` with the snapshot name and push the tag.
2. Create a GitHub release for that tag, titled `Snapshot <snapshot name>`, with the final release notes: `gh release create <snapshot name> --title "Snapshot <snapshot name>" --notes-file <file>`.
3. If no tool in the session can create a release, give the user the release notes in a code block and the link `https://github.com/tiavelum/claude-mechanics/releases/new?tag=<snapshot name>`.

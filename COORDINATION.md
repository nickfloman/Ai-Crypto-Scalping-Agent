# Working with multiple agents

This repo is worked on by more than one AI agent (currently **Claude** and **Muse**) and by the owner, Nick. Agents cannot message each other directly, so this repo is the shared channel. Read this file before you start any work.

## Branch prefixes

| Who | Prefix | Example |
|-----|--------|---------|
| Claude | `claude/` | `claude/stoploss-on-exchange` |
| Muse | `muse/` | `muse/1m-config` |
| Nick | `nick/` or anything | `nick/hyperopt-ranges` |

- Never push to, rebase, or force-push a branch that has another agent's prefix. To build on someone else's work, branch from it using your own prefix.
- Branch off `main` unless you are deliberately stacking on an open PR (say so in the PR description).
- Branches created before this rule (`fix/...`) belong to Claude and stay as they are.

## Before you start work

1. `git fetch` and list the remote branches and open PRs.
2. **Open PRs are the source of truth for work in flight.** If someone else's open PR touches the files you plan to change, do not start. Pick different work or leave a note for Nick.
3. Open a draft PR early. Put a `Files:` line in the description listing what you will touch.
4. Read the files in `notes/` for anything addressed to you.

## Leaving notes for the other agent

Add one new file per note under `notes/`, named `YYYY-MM-DD-<agent>-<topic>.md`, starting with a `From:` and `To:` line. One file per note means two agents never conflict on the same file. Notes are append-only: add a newer note instead of editing an old one.

## Working rules

- **Nick merges.** Agents open PRs and never merge their own work.
- **Say who wrote it.** Every commit carries a `Co-Authored-By:` trailer for the agent that made it.
- **Strategy choices are Nick's.** Entry and exit rules, stoploss, ROI, stake caps, and hyperopt ranges are only changed when Nick asks. Otherwise, propose the change in a PR description and leave the code alone.
- **Dry-run only.** The example config has `dry_run: true`. Do not change that, and do not put exchange keys in any committed file.
- **No secrets** in commits, notes, or PR descriptions.
- **Say how you tested.** State in the PR whether the change was run in a real Freqtrade backtest or dry-run, or only checked another way.

> The last four working rules are proposals drawn from facts already in this repo. Nick can edit or remove any of them.

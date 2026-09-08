# The forge

This declaration binds repository and publication operations to the destinations below. Authorization comes from the user's actual request and established conversation scope. Configuring an operation does not request its execution. Missing bindings block the affected operation while authorized local preparation may continue.

## The repository

**GitHub** — `ca77y/agentic-codex`.
<https://github.com/ca77y/agentic-codex>

One remote, `origin` — `git@github.com:ca77y/agentic-codex.git`, over SSH. There is no
fork or upstream. The checkout is canonical, and `origin` is the only push destination.

## Reaching it

The **`gh` CLI**, already authenticated on this machine as `ca77y`; git operations use
SSH. The connected GitHub connector is deliberately unused by these bindings. No
credentials live in this repository or belong in this file.

## Branches and worktrees

- **Default working checkout** — ordinary repository work happens directly on
  `master` in the repository root. Create or use a separate branch and worktree only
  for a requested commit/PR endpoint or an explicit isolation request. Ordinary local edits may remain in the existing checkout.
- **Target branch** — `master`. Every story branches from it and every PR targets it.
  Automated operations never commit to it, check it out in a story worktree, or push it.
- **Story worktrees** — `.worktrees/<branch>` at the repository root, covered by the
  committed `.gitignore` entry `.worktrees/`.
- **Temp folder** — `.tmp/` at the root of the current checkout or worktree, covered
  by the committed `/.tmp/` entry. Store workflow ledgers in `.tmp/ledgers/`;
  preserve ledgers and their required evidence during scratch cleanup and after completion.
- **Branch name** — the issue's `gitBranchName`, read through [`BOARD.md`](./BOARD.md).
  Linear supplies a legal ref such as
  `tokwieci/smr-200-card-content-access`. Without
  an issue, use `<type>/<lowercase-kebab-slug>`.
- **Removal** — after the PR merges, the human runs `git worktree remove <path>` and
  deletes the branch. Neither operation has an automated grant.

## Commits

The commit convention is **Conventional Commits**. Use `docs:` or `docs(<area>):` for
specification and documentation, `feat:` or `feat(<area>):` for a build, and `fix:` or
`fix(<area>):` for a fix round. A message names the issue when it adds the spec, and a
pre-ship fix names the round whose findings it applies. Illustrative subjects:

```text
docs(spec): add SMR-200 spec for card-content access
feat(cards): support scoped card-content refinement
fix(cards): correct the reference target for review round 1
```

Push once when the PR opens. Before that, the spec, build, and pre-ship round commits
stay local in the worktree. After the PR exists, push each fix round once its affected
validation and acceptance checks pass. Intermediate repair checkpoints stay local;
an unresolved blocking finding prevents publication.
Never force-push, amend or rebase pushed history, or push `master`.

## Operations

- **branch** — create new work with
  `git worktree add .worktrees/<branch> -b <branch> master`; recover a missing worktree
  for an existing story branch with `git worktree add .worktrees/<branch> <branch>`.
- **remove a worktree** — `git worktree remove <path>` — *the human's, after merge*.
- **commit** — `git -C <worktree> add <paths>` (never `-f`), then
  `git -C <worktree> commit`.
- **push** — `git -C <worktree> push -u origin <branch>` the first time, immediately
  before the PR opens; `git -C <worktree> push` on each later verified fix round.
- **open the change** —
  `gh pr create --repo ca77y/agentic-codex --base master --head <branch> --title <title> --body-file <path>`.
  Its output is the PR URL; that output is the link, never a constructed pattern.
- **update the change** —
  `gh pr edit <number> --repo ca77y/agentic-codex --body-file <path>`, with `--title`
  when the title changes.
- **comment on the change** —
  `gh pr comment <number> --repo ca77y/agentic-codex --body <text>`.
- **read the change** —
  `gh pr view <number> --repo ca77y/agentic-codex --json title,body,url,baseRefName,headRefName`
  and `gh pr diff <number> --repo ca77y/agentic-codex`.
- **re-fire the review** —
  `gh pr comment <number> --repo ca77y/agentic-codex --body '@codex review'`.
  After a validated fix push, use only when that review message is authorized.
- **merge** — *not available*. Merging and the merge method are the human's.

## The change artifact

A **GitHub pull request**, one per story, opened against `master`. A fix run reuses the
same PR and branch.

- **Title** — an imperative sentence naming the outcome, not a commit subject.
- **Description** — Markdown under applicable `##` headings, in this order:
  `## Task` · `## Spec` · `## What was built` · `## Tests` ·
  `## Gates and rounds` · `## Acceptance gate` · `## Docs` ·
  `## Production hazards / blockers` · `## Board follow-ups` ·
  `## Commits (<n>)` · `## Card status` · `## Review` ·
  `## Remaining risks / follow-ups`. Drop inapplicable sections rather than leaving
  them empty. A fix run appends `## Review round <n> — addressed`.
- **Link** — exactly the URL printed by `gh pr create`; attaching it to Linear is
  governed by [`BOARD.md`](./BOARD.md).
- **Labels, reviewers, assignees, milestones, and draft state** — unused here.

## The review

Codex reviews pull requests through the GitHub integration. Opening a PR for review triggers the initial review; posting the literal comment `@codex review` requests another review. Use that trigger after a validated fix push only when the user authorized the review request. Report the observed request result without unsolicited polling or waiting. Later findings resume through a user request concerning the same PR. Merging remains the user's decision.

No CI or required status check is currently defined in the repository.

## Operation conditions

- **Read PR or diff** — the requested task requires that information from the bound repository.
- **Create or recover workspace** — a requested commit/PR endpoint or explicit isolation request authorizes one story branch and worktree under `.worktrees/`, following the configured derivation. Recover the existing story branch/worktree for repair; do not create a second workspace.
- **Commit** — the user requested a commit or PR endpoint. Stage only attributable paths in the authorized story worktree, without forced staging, and use Conventional Commits. A local-change-only request does not authorize commits.
- **Push** — publication of the same change is requested and required validation and acceptance have passed. Push only the story branch to `origin`; first push when opening the PR, later pushes for verified repairs. Keep intermediate checkpoints local; blocking findings prevent a push.
- **Open PR** — the user requested a PR. Open one against `master` in the bound repository and retain its real returned URL. Reuse the existing PR for story repair.
- **Update PR** — the requested publication/repair scope includes that same PR; title/body must reflect the same change and preserve unused metadata restrictions. Do not widen scope or create another PR.
- **Comment or trigger review** — the user explicitly authorized the message or review request on that PR. Configuration alone does not authorize communication. Record the observed result; later findings resume through a user request.
- **Remove worktree or branch** — user-controlled cleanup after merge; no automated grant.

The following operations have no automated grant:

- Never merge or enable auto-merge.
- Never force-push, amend a pushed commit, rebase a pushed branch, or delete a branch,
  tag, or remote ref.
- Never push `master`, commit to it, or check it out in a story worktree.
- Never open a second PR for a story, and never close one.
- Never cut a release or tag.
- Never touch another repository or add another remote.

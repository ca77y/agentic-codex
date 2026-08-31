# The forge

How this project gets a story from a branch to a reviewed change, read directly at this
fixed path — `docs/FORGE.md` — by the `lead`, before it creates a workspace. Keep it
true, because the pipeline binds real commands to what it says, and because a run stops
rather than guess when this file is missing.

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

- **Target branch** — `master`. Every story branches from it and every PR targets it.
  The pipeline never commits to it, checks it out in a story worktree, or pushes it.
- **Story worktrees** — `.worktrees/<branch>` at the repository root, covered by the
  committed `.gitignore` entry `.worktrees/`. Run-local scratch at the root of each
  worktree is covered by the committed `/tmp/` entry.
- **Branch name** — the issue's `gitBranchName`, read through [`BOARD.md`](./BOARD.md).
  Linear supplies a legal ref such as
  `tokwieci/smr-200-state-the-writers-spec-pass-board-access-includes-whatever`. Without
  an issue, use `<type>/<lowercase-kebab-slug>`.
- **Removal** — after the PR merges, the human runs `git worktree remove <path>` and
  deletes the branch. The pipeline does neither.

## Commits

The migrated convention is **Conventional Commits**. Use `docs:` or `docs(<area>):` for
specification and documentation, `feat:` or `feat(<area>):` for a build, and `fix:` or
`fix(<area>):` for a fix round. A message names the issue when it adds the spec, and a
pre-ship fix names the round whose findings it applies. Examples from the source
repository's story branches:

```text
docs(spec): add SMR-200 spec for the writer's spec-pass board access
feat(writer): state spec-pass board access as read, search, and the declaration's card-content authority
fix(writer): name the pointer's target instead of its position
```

Push once when the PR opens. Before that, the spec, build, and pre-ship round commits
stay local in the worktree. After the PR exists, push each fix round when committed.
Never force-push, amend or rebase pushed history, or push `master`.

## Operations

- **branch** — `git worktree add .worktrees/<branch> -b <branch> master`.
- **remove a worktree** — `git worktree remove <path>` — *the human's, after merge*.
- **commit** — `git -C <worktree> add <paths>` (never `-f`), then
  `git -C <worktree> commit`.
- **push** — `git -C <worktree> push -u origin <branch>` the first time, immediately
  before the PR opens; `git -C <worktree> push` on each later fix round.
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
- **re-fire the review** — *not available*. No automated review is configured.
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

No automated reviewer or review workflow is configured in this repository. A human
reviews the open PR. The lead opens it, reports it as open and not yet reviewed, and
does not poll or wait. Findings re-enter the pipeline when a human invokes
`ca77y-engineering:lead` again with the PR or its findings.

No CI or required status check is currently defined in the repository.

## What the pipeline may write

The `lead` alone may write:

- one story branch and one worktree under `.worktrees/`;
- commits in that worktree;
- the story branch on `origin`, once when opening the PR and once per later fix round;
- one PR against `master`; and
- updates and comments on that same PR.

Everything else is the human's:

- Never merge or enable auto-merge.
- Never force-push, amend a pushed commit, rebase a pushed branch, or delete a branch,
  tag, or remote ref.
- Never push `master`, commit to it, or check it out in a story worktree.
- Never open a second PR for a story, and never close one.
- Never cut a release or tag.
- Never touch another repository or add another remote.

No worker receives forge write access. Workers may only read the worktree and the commit
references the lead gives them.

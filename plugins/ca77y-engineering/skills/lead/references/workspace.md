# Workspace setup and run state

Read when creating a story worktree or recovering one for repair.

1. Create the branch/worktree only through FORGE's binding, using its target, naming rule, and directory. Recovery reuses the existing branch. Verify the absolute path with `git -C <repository> worktree list`.
2. Provision using the main checkout's already-resolved dependencies when compatible, otherwise the project's documented install/bootstrap step. Never re-resolve casually, modify root dependencies, or substitute a fetched CLI. Only the lead provisions; this is setup, not QA.
3. Record **provisioned**, **no dependencies required** (the project affirmatively requires none), or **provisioning failed** with the reason. On repair, verify reused dependencies still match the checkout or reestablish them through this same procedure; do not inherit an old success blindly. Continue evidence-independent work after failure, but dependent commands are untrustworthy and cannot establish a clean result.
4. Ensure committed ignore rules cover `/tmp/` and the declared worktree directory before writing scratch state. If missing, make only an authorized scoped ignore correction through the story worktree; otherwise report the blocker. Never write the root ignore file as a workaround.
5. Create `tmp/ledger.md` with the file-editing tool. It records task/card, authority, worktree/status, current step, spec path/commit and saved copy, worker targets/ownership/models, coder score/tier/promotion, attempt counts, reported gate outcomes and inspected commits, pending work, transitions, and board follow-ups. Update before each dispatch, wait, and turn end. Long findings stay in ignored `tmp/findings-round-<N>.md`.
6. For a new story only, apply the declared work-started transition from its expected from-value. A repo-local board write lands uncommitted in the root checkout according to BOARD's visibility rule; it is the sole root-write exception and never part of a story commit. Hosted writes use the bound call. Do not invent a card or transition, or overwrite a status someone else moved.

The root checkout is otherwise read-only. Every dispatch carries the absolute worktree path, provisioning status, expected edit paths, and other live ownership. Never stage scratch files or another worker's unrelated edits. If scratch writes fail, follow [recovery](recovery.md).

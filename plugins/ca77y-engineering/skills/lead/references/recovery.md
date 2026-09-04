# Recovery — missing reports and session continuation

Read this when a worker yields no usable report, when `spawn_agent` rejects before returning a target, or when the lead continues after compaction or a session interruption. Everything in `SKILL.md` still binds.

## A worker yields no usable report

Check ground truth before any replacement dispatch:

1. Use `list_agents` to inspect the worker target, then use `wait_agent` once to
   collect its final report even when the target already reads completed or errored. A
   terminal status does not prove the report has been delivered. If collection yields a
   usable report, route it as a worker or gate result; do not classify the dispatch as
   infrastructure. A target that is terminally errored before reporting remains a
   failed-dispatch candidate; continue the checks below before classifying it.
2. For a synchronous `spawn_agent` rejection that returned no target, record the
   targetless result and host error, inspect `list_agents` for any new live target in
   the story worktree, and collect any target that could belong to this dispatch before
   proceeding. Do not invent a target or call `followup_task`; if no target can be
   associated, the no-target branch has no worker report to collect.
3. Inspect `git -C <worktree> status --short --untracked-files=all` and the files the
   worker was asked to produce against that dispatch's ledger baseline. Exclude the
   lead's ledger update itself. Only a newly present path or a changed content
   fingerprint is attributable to the dispatch; pre-existing modified paths and
   artifacts do not establish worker work.
4. If the worker is stuck and must be stopped, use `interrupt_agent`, then inspect the tree again against the same baseline before deciding whether to continue it with `followup_task` or replace it.

Post-baseline work present on disk means the worker may still be live or may have
completed without a useful final report. Collect and preserve that work; never silently
spawn a replacement onto files another live worker may still be editing. A baseline
artifact that predates the dispatch does not block the infrastructure classification.
Only after the terminal-report collection check yields no usable report, the worker is
no longer active (or no target can be associated after the targetless check), and no
post-baseline change accounts for the task may you return a confirmed pre-work fault to
`SKILL.md`.

## A scratch-file write fails

Workers and the lead address the story worktree by absolute path. A permission failure writing `tmp/ledger.md` or a findings file is a blocker for this story: report the exact path and failure to the user. Do not switch to shell redirection or move run-local state outside the worktree.

## After compaction or interruption

The ledger (`tmp/ledger.md`) plus `git log` are the source of truth. Before acting, re-establish:

- the current workflow step and what is awaited;
- whether the run is `--fast`, including every model fallback;
- the coder tier, any senior fallback, and any promotion already made;
- the worker targets still available for `followup_task`;
- the durable agent-definition state, either its no-definition-change determination or
  refresh proof including source revision, installer result for every managed TOML,
  managed names, and post-install new-task confirmation;
- the absolute story worktree and `tmp/ledger.md` paths, plus each dispatch's target
  status, host error, and artifact baseline;
- commits and round counters, so the 3x rule includes every attempt;
- card transitions and retained board follow-ups.

A user prompt that arrived mid-pipeline is a pause, not an abort: handle it, then resume from the ledger.

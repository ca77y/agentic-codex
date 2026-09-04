# Recovery — missing reports and session continuation

Read this when a worker yields no usable report or when the lead continues after compaction or a session interruption. Everything in `SKILL.md` still binds.

## A worker yields no usable report

Check ground truth before any replacement dispatch:

1. Use `list_agents` to inspect the worker target, then use `wait_agent` once to
   collect its final report even when the target already reads completed or errored. A
   terminal status does not prove the report has been delivered. If collection yields a
   usable report, route it as a worker or gate result; do not classify the dispatch as
   infrastructure.
2. Inspect `git -C <worktree> status --short` and the files the worker was asked to produce.
3. If the worker is stuck and must be stopped, use `interrupt_agent`, then inspect the tree again before deciding whether to continue it with `followup_task` or replace it.

Work present on disk means the worker may still be live or may have completed without a
useful final report. Collect and preserve that work; never silently spawn a replacement
onto files another live worker may still be editing. Only after the terminal-report
collection check yields no usable report, the worker is no longer active, and nothing
on disk accounts for the task may you spawn a fresh role worker.

## A scratch-file write fails

Workers and the lead address the story worktree by absolute path. A permission failure writing `tmp/ledger.md` or a findings file is a blocker for this story: report the exact path and failure to the user. Do not switch to shell redirection or move run-local state outside the worktree.

## After compaction or interruption

The ledger (`tmp/ledger.md`) plus `git log` are the source of truth. Before acting, re-establish:

- the current workflow step and what is awaited;
- whether the run is `--fast`, including every model fallback;
- the coder tier, any senior fallback, and any promotion already made;
- the worker targets still available for `followup_task`;
- commits and round counters, so the 3x rule includes every attempt;
- card transitions and retained board follow-ups.

A user prompt that arrived mid-pipeline is a pause, not an abort: handle it, then resume from the ledger.

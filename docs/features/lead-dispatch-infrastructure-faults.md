---
title: Lead dispatch infrastructure faults
scope: ca77y-engineering lead dispatch and collection policy
---

# Lead dispatch infrastructure faults

The `lead` separates a dispatch infrastructure fault from a worker or gate problem so
the 3× rule measures repeated inability to close work rather than a failure to start
work.

## Classification and ledger

A dispatch is an infrastructure fault only when the fresh `spawn_agent` call or a
`followup_task` delivery fails before the worker has supplied any report of work, or a
target returned by either call later reaches an errored terminal state without
reporting; the recovery procedure must first rule out a live worker, a delayed final
report after terminal status, and an attributable post-baseline worktree artifact,
with no worker report remaining to route. This includes a synchronous `spawn_agent`
rejection before a target exists. This **targetless** branch records the host error,
checks for any live target that could belong to the dispatch, and never invents a
target or retries immediately. The lead performs the final-report collection check
even for a completed or errored worker. A worker's lack of any report is the
classification boundary.

The lead records a confirmed infrastructure fault separately from gate rounds, coder
attempts, and the 3× counter. It consumes no attempt.

Before every `spawn_agent` or `followup_task`, the lead records a dispatch id and an
artifact baseline in the ledger: the absolute worktree path, the
`git -C <worktree> status --short --untracked-files=all` path/status set and a content
fingerprint for every path in that set, and the existence and content fingerprint of
every expected output path, including ignored paths. The lead's own ledger update is
excluded from the comparison. A path is attributable to the dispatch only when it is
newly present or its fingerprint changes after the baseline; a pre-existing modified
path or artifact does not prove that the failed worker did work.

## Current custom-agent definitions

A selectable custom-agent name proves that the catalog has a TOML for that role; it
does not prove that the TOML contains the current role procedure. When a
ca77y-engineering update changes `agents/` or the `install-subagents` resources, the
user runs `ca77y-engineering:install-subagents` from the updated plugin and starts a
new Codex task before the lead's first dispatch. The invoking task follows the exact
sequence `--check`, installation with `--ledger-path
<absolute-story-worktree>/tmp/ledger.md`, and proof-write confirmation before the
restart; the installer writes the pre-restart proof. The refresh state is durable in
the ledger: each session, including a replacement task, reads an agent-definition
state entry that either ties a no-definition-change check to the last valid proof or
records the current source identity, absolute installer path, successful
`--check` and install result for every managed TOML, refreshed names, and confirmation
that the replacement task started after installation. The source identity combines
the Git revision with a deterministic package digest when Git is available, and uses
the package digest alone for a packaged copy without `.git`; an unavailable identity
cannot produce a successful proof. The replacement lead runs the installer's read-only
ledger verifier against that identity and appends confirmation only after it passes,
after opening the same worktree and ledger and before its first dispatch. A new run
with no prior proof cannot use a prompt-local acknowledgment or no-change claim.
Until that state is confirmed, the lead stops rather than dispatching a legacy
definition that may refer to a removed role skill.

## First confirmed fault

For the first confirmed infrastructure fault, the lead stops retrying in the current
session and escalates to the user. The diagnosis includes the requested custom-agent
name; the model and reasoning effort submitted to `spawn_agent`, or recorded for the
continued target; and non-secret host error or returned target metadata. It includes a
host-reported effective model and session-versus-disk source when available, and marks
each unavailable fact explicitly when the host does not expose it. The lead does not
inspect `.env` files or infer a configuration-precedence cause. The escalation also
includes the dispatch id, the post-dispatch baseline comparison, and the actual
absolute story worktree and `<worktree>/tmp/ledger.md` paths. The replacement task
opens that same worktree, reads that ledger and `git log`, verifies the durable
agent-definition state, and resumes the pending dispatch from the recorded state
without creating a second worktree or relying on prompt-only recollection.

When a host diagnostic or the user establishes that an inherited bad value is live in
the current session, a settings-file edit alone does not change that value without an
explicitly documented process-level reload. The new session starts with corrected
configuration and its lead resumes the pending dispatch from the absolute ledger path;
retrying the same dispatch in the existing session is not a remedy. This relies on the process
environment behavior described by [POSIX Issue 8's `exec`
specification](https://pubs.opengroup.org/onlinepubs/9799919799/functions/exec.html): a
new process image receives its environment through `envp`, while changing the running
process environment is an in-process operation.

## Worker and gate failures

A worker that has reported any work remains on the ordinary route. Its reported
failure, or a gate rejection of its work, is a worker or gate problem under the normal
routing and counted 3× rule, including when it happens early.

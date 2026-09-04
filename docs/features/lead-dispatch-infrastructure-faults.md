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
`followup_task` delivery fails before the worker has supplied any report of work, the
recovery procedure has ruled out a live worker, delayed final report, and attributable
worktree artifact, and no worker report remains to route. A worker's lack of any
report is the classification boundary.

The lead records a confirmed infrastructure fault separately from gate rounds, coder
attempts, and the 3× counter. It consumes no attempt.

## First confirmed fault

For the first confirmed infrastructure fault, the lead stops retrying in the current
session and escalates to the user. The diagnosis includes the requested custom-agent
name; the model and reasoning effort submitted to `spawn_agent`, or recorded for the
continued target; and non-secret host error or returned target metadata. It includes a
host-reported effective model and session-versus-disk source when available, and marks
each unavailable fact explicitly when the host does not expose it. The lead does not
inspect `.env` files or infer a configuration-precedence cause.

When a host diagnostic or the user establishes that an inherited bad value is live in
the current session, a settings-file edit alone does not change that value without an
explicitly documented process-level reload. The new session starts with corrected
configuration and its lead resumes the pending dispatch from the ledger; retrying the
same dispatch in the existing session is not a remedy. This relies on the process
environment behavior described by [POSIX Issue 8's `exec`
specification](https://pubs.opengroup.org/onlinepubs/9799919799/functions/exec.html): a
new process image receives its environment through `envp`, while changing the running
process environment is an in-process operation.

## Worker and gate failures

A worker that has reported any work remains on the ordinary route. Its reported
failure, or a gate rejection of its work, is a worker or gate problem under the normal
routing and counted 3× rule, including when it happens early.

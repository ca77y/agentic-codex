# Orchestrator ledger

Read on every invocation, before production or delegation. The main agent maintains one durable ledger for the outcome, including trivial work, answer-only work, bootstrap, and installation. Leaves report progress and failures; they never write the shared ledger. Initial context reading and ledger/spec preparation need no recursive specification gate.

## Open and own the ledger

Follow a supplied ledger path or a ledger reference in the task, spec, or PR. Otherwise search the project's declared ledger directory, defaulting to `docs/ledgers/` under the project root, for the same project identity, outcome, and acceptance source. Match project identity separately from the current checkout so entry-point or worktree changes do not create a new history. For work without a project, search `$CODEX_HOME/ledgers/` (default `~/.codex/ledgers/`). Use the actual project root, never the installed skill's working directory.

Reuse the matching ledger across skills and turns. Only when no existing record matches, copy [the template](../assets/ledger.md) into that directory as `<run-id>.md`, using a supplied run ID or a unique date-and-outcome ID. Record its absolute path and available owner/task handle. Missing runtime IDs are explicitly unavailable, never invented. If records conflict or failure history is incomplete, report the recovery gap before more production.

The current task is the sole writer. A different task must obtain an explicit release/handoff from the owner or user before claiming an active ledger. The outgoing owner saves state, releases ownership, and records the destination and next owner. The incoming owner confirms the previous owner has stopped writing, records the transfer, and then resumes. Uncertain ownership blocks production; a resumed current task retains ownership.

Keep ledgers outside the research library, plugin source/cache, and disposable scratch. Local operational bookkeeping does not authorize library content changes, commits, or external writes. If persistence is explicitly forbidden or unavailable, return the ledger content and unmet persistence condition in the conversation; do not silently continue without the required durable record.

## Maintain progress and subagent identities

Fill the template with the acceptance source, authority/endpoint, spec and candidate identities, current phase, completed/pending/blocked work, artifacts, decisions, evidence, and next action. Use `none`, `not applicable`, or `unavailable` explicitly instead of pretending a spec, worker, or result exists.

- Before `spawn_agent`, record the assignment, configured role, allowed paths, problem identity, model/effort and selection rationale, and any reserved solution slot.
- Immediately after dispatch, save every returned agent ID and canonical task name when exposed. A canonical `task_name`/`agent_name` is a valid coordination handle if no opaque ID is returned; mark the opaque ID unavailable. Failed dispatches remain recorded without fabricated IDs.
- Give each worker the absolute ledger path as read-only context, require meaningful progress, results and all evaluated failures, and reserve ledger writes to the orchestrator.
- Update assignments/status before `followup_task`, and progress, results, evidence and next actions when worker updates arrive. Keep old worker records when replacing a worker.
- Save current state before `wait_agent` or another wait, after every gate verdict/evaluated failure, and before the final response, planned interruption, handoff or stop. On an unexpected interruption, reconcile the last saved state before resuming.

Keep the current summary concise and retain gate and failure history. Link evidence to its acceptance source, exact spec/candidate revision, observation/check, and pass/fail/unverified result. Mark affected evidence stale after product edits. Ledger-only status updates do not change the validated product candidate or require recursive validation. Record failures across all workers and gates under the same unresolved problem; maintain reserved slots, remaining budget and any explicit additional-attempt authorization. A passed gate, replacement worker, or changed entry point never resets failures.

## Resume and close

Read the existing ledger before another solution attempt. Reconcile its progress, reservations and worker statuses with available runtime state and actual artifacts. A stored ID is a handle, not proof that its worker is still live or that its work passed. Mark stale/unavailable workers honestly; preserve their IDs and recover their artifacts/results before deciding what needs replacement. Unknown attempt history is a recovery gap, not zero. A fresh validation assignment always gets a newly spawned validator.

At the third failed attempt for any unresolved problem, stop the entire run and active workers using available interruption tools, save their actual statuses and useful work, and return the blocking evidence and required decision or explicit additional-attempt authorization. Record any inability to stop a worker; do not report it as stopped.

Before checkout/task handoff or worktree removal, carry the ledger and its required evidence to the durable destination, pass the absolute path, and complete the ownership transfer. Do not assume an untracked file travels with git state. Retain the ledger after completion, record the authorized endpoint reached or the unmet condition and next action, and link it in the final response. Completion never deletes failure history.

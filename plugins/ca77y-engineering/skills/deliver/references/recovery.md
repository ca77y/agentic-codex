# Recovery state

Read when resuming interrupted work or when failure history needs durable preservation. The core three-attempt rule always applies, even if this reference was never needed earlier.

Find the project-approved durable record associated with the outcome, spec, or existing PR before another attempt. Use an existing task record or another permitted durable artifact; do not depend on live worker targets, ignored worktree scratch, or a new unapproved service. Keep only enough state to resume soundly:

- Outcome/problem identity, acceptance source, user authority and endpoint.
- Spec and candidate identities, current paths, useful completed work, and evidence still valid.
- Each evaluated failed approach, its observations, model/effort where applicable, and why it failed; aggregate failures and remaining budget.
- Current ownership, any reserved parallel solution slots, unresolved findings, and plausible next approach.
- Any explicit user-granted additional attempts, alongside the original history.

Recover records across entry points and turns. Treat uncertain history as an unmet recovery condition, not zero failures. A verified resolution closes only that problem; restore its history if evidence later shows it never held. Saving a draft or obtaining a passing spec gate does not close an unresolved implementation outcome.

At three failures, stop all active delegated work with the available interruption tool, preserve state, and return control. Further production is prohibited until explicit additional attempt authorization arrives. If a runtime lacks a stopping mechanism for active work, report that limitation and do not dispatch more work. Saving state is permitted; a fourth experiment disguised as recovery is not.

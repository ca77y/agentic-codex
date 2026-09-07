# Recovery state

Read when resuming interrupted work or recovering failed attempts. The [ledger procedure](ledger.md) applies on every invocation; this reference adds delivery-specific recovery context.

For a continuation of the same unfinished request, open its existing run ledger using its discovery and ownership rules before another attempt. Reconcile it with the spec, candidate and existing PR; never create a fresh history because the entry point, checkout or worker changed. Recover:

- Initiating request/run and outcome/problem identity, acceptance source, user authority and endpoint.
- Spec and candidate identities, current paths, useful completed work, and evidence still valid.
- Each evaluated failed approach, its observations, model/effort where applicable, and why it failed; aggregate failures and remaining budget.
- Current ownership, any reserved parallel solution slots, unresolved findings, and plausible next approach.
- Any explicit user-granted additional attempts, alongside the original history.

Recover same-run records across entry points and turns. Treat uncertain history for that run as an unmet recovery condition, not zero failures. A separate later user request starts a new run; previous PR or artifact failures remain context and do not enter its count. A verified resolution closes that problem; restore its history only if evidence within the same run shows it never held. Saving a draft or obtaining a passing spec gate does not close an unresolved implementation outcome.

At three failures, stop all active delegated work with the available interruption tool, preserve state, and return control. Further production is prohibited until explicit additional attempt authorization arrives. If a runtime lacks a stopping mechanism for active work, report that limitation and do not dispatch more work. Saving state is permitted; a fourth experiment disguised as recovery is not.

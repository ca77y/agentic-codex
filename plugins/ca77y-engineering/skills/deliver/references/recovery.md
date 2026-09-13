# Recovery state

Read when resuming interrupted work or recovering failed attempts. The [ledger procedure](ledger.md) applies on every invocation; this reference adds delivery-specific recovery context.

For a continuation of the same unfinished request, open its existing run ledger using its discovery and ownership rules before another attempt. Reconcile it with the spec, candidate and existing PR; never create a fresh history because the entry point, checkout or worker changed. Recover:

- Initiating request/run and outcome/problem identity, acceptance source, user authority and endpoint.
- Spec and candidate identities, overall and per-task complexity with rationales, current paths, useful completed work, and evidence still valid.
- Each evaluated failed approach, its observations, intended and actual production model/effort and selection/deviation rationale, and why it failed; owning retry policy, starting/current solution tier, aggregate and per-tier failures, remaining initial and higher-tier slots, skipped/forfeited slots, next escalation and terminal stop condition. Validator model/effort remains separate from solution tier.
- Current ownership, any reserved parallel solution slots, unresolved findings, and plausible next approach.
- Any explicit user-granted additional attempts, alongside the original history.

Recover same-run records across entry points and turns. Treat uncertain history for that run as an unmet recovery condition, not zero failures. A separate later user request starts a new run; previous PR or artifact failures remain context and do not enter its count. A verified resolution closes that problem; restore its history only if evidence within the same run shows it never held. Saving a draft or obtaining a passing spec gate does not close an unresolved implementation outcome.

Follow the [delivery tier escalation policy](../SKILL.md#tier-escalation-and-stop-gate): after three initial failures, use one corrective attempt at each higher tier; after escalated Astra failure (or three failures for an Astra start), stop all active work, preserve state and return control. Early promotion forfeits unused slots; no demotion or fresh allowance is permitted. Settle or stop active attempts before promotion and retain uncertain reservations until reconciled. Preserve this policy across same-run shaping; unrelated standalone runs keep their own recorded policy. At terminal stop, further production requires explicit additional-attempt authorization. If a runtime lacks a stopping mechanism, report that limitation and do not dispatch more work. Saving state is permitted; another experiment disguised as recovery is not.

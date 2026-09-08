# Dispatch fault recovery

Read on a `spawn_agent` error or uncertain target execution, before retrying or changing attempt accounting. This applies to every configured production and validation target.

## Establish whether assigned work began

Classify a dispatch as a **pre-work infrastructure fault** only when host or target evidence establishes that the target never began its assigned work. Retain that evidence in the run ledger. A proven pre-work fault consumes no solution attempt; release only that dispatch's reserved solution slot, preserving all prior failures.

A target report of assigned work establishes that work started. Its evaluated approach remains subject to the shared attempt rules, including an approach that proves unworkable before a candidate exists. Starting work alone is not a failed solution attempt. Do not relabel started work as a pre-work fault because its error mentions infrastructure or a model.

An error plus an absent target report does not prove pre-work failure or an evaluated failed solution. If evidence is missing, conflicting, or inconclusive, record execution as **uncertain**, preserve unresolved reservations and history, and reconcile available host/target facts before a replacement dispatch or budget decision. Do not assert that no work occurred. A returned target handle alone proves neither execution nor acceptance.

## Diagnose the first fault

On the first pre-work fault, record:

- Requested custom-agent name and submitted model and reasoning effort, preserving an omitted/inherited request as such.
- Host-reported effective model, or `unavailable` when not exposed.
- Host-reported session-versus-disk source, or `unavailable` when not exposed, independently of effective-model availability.
- Actual error and host/target evidence of whether assigned work began, classification, and its effect on failures/reservations.

Diagnose the actual submitted request and available runtime facts. Do not infer effective settings or their source from a disk file, model name, or missing report. Escalate the fault with the evidence, the concrete recovery requirement, and who can resolve it; do not blindly repeat the same dispatch. A diagnosed correction within existing authority may proceed. If cause or required access remains unresolved, stop dependent dispatches and report the blocker instead of entering a retry loop.

When diagnosis identifies a value retained by the active session, editing its source on disk does not change that running session. Require a corrected session before retrying and preserve the same run ledger and failure history across that correction. Make no universal claim about which configuration source wins. If the current agent cannot correct the session, return that specific requirement to the user.

Before retrying, record the diagnosed correction and evidence that the precondition is met. A dispatch exemption supplies no acceptance evidence: required fresh validation still needs a passing verdict from a successfully executing fresh validator. The shared stop gate still halts the whole run on its third actual failed solution attempt.

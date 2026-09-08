# SMR-311: Pre-work dispatch faults

## Acceptance source and problem

[SMR-311](https://linear.app/ca77y/issue/SMR-311/keep-pre-work-dispatch-faults-outside-the-shared-attempt-limit), retrieved 2026-09-08, requires proven pre-work `spawn_agent` failures to remain outside the shared three-failure solution budget. Its current scope is Engineering shape/deliver, Library research/ask, and reporting/recovery for all configured production and validation agents. Closed PR #5 addressed obsolete contracts and is not acceptance evidence for this change.

## Intended behavior

The four orchestrators retain the shared three-attempt stop gate. Before applying an exception to a failed dispatch of any configured production or validation target, require host or target evidence that assigned work never began. A proven pre-work fault is infrastructure diagnosis, consumes no solution attempt, and releases any solution-slot reservation for that dispatch without resetting previous failures.

On the first such fault, record the requested custom agent, submitted model and effort, host-reported effective model, host-reported session-versus-disk source, and the evidence supporting classification in the run ledger. Mark effective model and source independently `unavailable` if not exposed. Diagnose the actual request and available runtime facts, escalate the blocker with a concrete recovery requirement, and never blindly repeat the same dispatch. A diagnosed correction within existing authority may proceed; unresolved causes stop dependent dispatches.

If diagnosis identifies a value retained by the active session, explain that editing its source on disk does not change that running session; require a corrected session before retrying. Do not prescribe universal configuration precedence or assume tools expose effective settings.

A target report of assigned work establishes that work started. Its evaluated approach remains governed by the existing shared attempt rules, including approaches that prove unworkable before a candidate. Merely starting work is not itself a failed solution attempt. An error plus no report establishes neither pre-work failure nor an evaluated failed solution. Record uncertain execution and preserve unresolved reservations/history until evidence reconciles them; do not assert no work occurred or bypass required validation with an exemption.

Each configured leaf reports available facts about whether assigned work began, what it did, errors, and any runtime settings actually exposed. Leaves neither invent host facts nor decide/reset the main agent's budget. A worker that never starts cannot be required to produce a report.

## Scope and approach

Keep a short classification boundary and conditional reference in each of the four workflow manuals. Place full diagnosis/recovery guidance in a reference owned by each plugin's existing orchestrator reference directory, shared within that plugin by relative link. Add concise factual-reporting instructions to all eight AGENT.md core procedures. Align both existing ledger procedures/templates and delivery recovery guidance so failed dispatch history survives resume. Agent TOML resources already point to core manuals, which the managed installer embeds; do not duplicate procedures in TOML.

No changes to library content, workflow authority, model selection policy, fixed model settings, attempt limit, installer logic, plugin versions, installed agents, publication, or historical PR. This is a local instruction change, not a release.

## Observable acceptance criteria

1. Across all four workflows and all eight configured production/validation roles, only host or target proof that assigned work never began permits a pre-work infrastructure classification and no solution-attempt charge.
2. First-fault guidance records custom agent, submitted model/effort, effective model and session-versus-disk source; independently missing effective model/source become `unavailable`. Diagnosis and escalation replace blind repeated dispatch.
3. A diagnosed active-session retained value requires a corrected session before retry; a disk edit alone is insufficient. No universal precedence claim appears.
4. Started-work reports retain normal evaluated-approach accounting. Error/no-report and conflicting or inconclusive evidence remain uncertain, with no unsupported no-work assertion or budget reset.
5. Ledger and recovery preserve fault facts, uncertainty, reservations and prior failure history. Required fresh validation remains mandatory; no exemption supplies missing gate evidence.
6. Both plugins remain independently distributable, references resolve, all skill quick validators and both plugin validators pass, and isolated managed-agent installation demonstrates the updated reporting contract is embedded for every configured role without fixed model/effort fields.

## Verification

A fresh engineering auditor validates readiness against the retrieved card and current contracts before implementation. A different fresh engineering auditor evaluates final document acceptance and packaging (no executable implementation changed), mapping each criterion to exact candidate digests. Walk through proven host rejection, target-confirmed no work, started-work failure, silent/ambiguous error, missing individual host fields, session-retained value, and third actual solution failure across the four workflow routes. Run the required quick/plugin validators, inspect local links, and use isolated installer output plus existing installer regression suites to verify packaging. Record actual commands, results, and any unavailable check in durable evidence outside the product candidate. Do not claim runtime execution of a host fault from an instruction walkthrough.

# Delivery complexity and model routing

## Outcome and scope

Complexity: **6/10**. The change coordinates specification, dispatch, failure accounting and recovery across existing manuals; it adds no executable scheduler.

Delivery should favor smaller models using an explicit complexity score, model/effort matrix and bounded escalation. This specification supersedes previous no-score/no-fixed-table requirements and the fixed three-failure stop for engineering delivery and its same-run shaping work. Standalone library, bootstrap and installation workflows retain their current retry policies. Preserve gates, fresh validators, authority boundaries, role names and model-free custom-agent definitions. Local source edits are the endpoint; release, live installation and publication are excluded. Update the delivery-policy descriptions in `README.md` and `plugins/ca77y-engineering/.codex-plugin/plugin.json`; preserve the manifest version unchanged.

## Intended behavior

Every execution spec carries an integer complexity from 1 to 10 and a short rationale, as does each task within it. A one-task spec may have one explicitly identified task; no board card or fixed document template is required. Overall complexity reflects integration, uncertainty and consequences, not an average or a model inherited by every task. Existing specs gain scores before their next delivery gate. Trivial work remains exempt from a written spec, but its ledger assignment is scored.

Default routing by task complexity: 1–4 Luna, 5–6 Terra, 7–8 Sol, 9–10 Astra. Default model/effort progression is `gpt-5.6-luna` / `max` → `gpt-5.6-terra` / `xhigh` → `gpt-5.6-sol` / `high` → `gpt-6-astra` / `medium`. Sol medium is the calibration anchor, not the mandatory effort for all Sol work. The matrix may allow overlapping effort configurations: Luna low through max, Terra medium/high/xhigh, Sol medium/high/xhigh, Astra medium/high/xhigh. Select supported combinations from actual host capabilities. This is a user-selected operating policy, not a benchmark-derived universal ranking.

The orchestrator scores each bounded assignment, including validation, independently of role and parent spec. Prefer the smaller capable model, including high-effort Luna over unnecessary promotion. Allow a reasoned stronger start or early escalation for material ambiguity, coupling, error consequences or observed failure; record why. Never downgrade validation scope to fit a model. The main session does not claim to switch models; when a scored solution requires another model, delegate to the configured production role. Record direct main-agent work with its actual model and the reason for any routing deviation.

Preparatory/evidence-only work and validator model selection are recorded but do not establish or consume a solution tier. The first evaluated solution attempt establishes the problem’s starting tier from the actual solution model. A submitted specification evaluated for acceptance is a solution attempt; a failed spec gate counts at its production model’s tier, while unsubmitted preparation is not an attempt. Once established, that problem’s solution tier cannot decrease, including after a passing gate. Separate genuinely independent problem identities may start at their own score-derived tiers; splitting a problem to evade its history is forbidden.

For each unresolved problem in a run, allow three evaluated solution attempts at the starting tier, then one corrective attempt at each successively higher tier. A Luna start permits at most six failures, Terra five, Sol four, Astra three. An escalated Astra failure stops the whole run and returns to the user. An Astra start stops after its third failure. Early promotion closes unused allowance at the previous tier, allows one attempt at the newly selected higher tier, and cannot return to skipped/lower tiers to reclaim slots. Effort changes never add slots. Stronger validator models do not change the solution tier or mint attempts; failed acceptance belongs to the evaluated solution attempt. A model switch alone is not an evaluated attempt.

Preserve existing accounting: one candidate evaluation is one attempt across its checks; diagnosis, baseline defects, review findings, and dispatch failures before work are not attempts. Gates, workers, entry points and resumptions share history; a passing spec gate does not erase unresolved implementation history. Explicit additional authorization after terminal stop is recorded alongside existing history. Separate later requests have separate runs. Reserve parallel alternative solution slots before dispatch; settle or stop active attempts before promotion so unreported work cannot overrun the allowance. If no next supported tier, essential prerequisite or plausible corrective approach exists, return earlier with the concrete limitation.

The ledger records overall and task/assignment complexity with rationale, intended and actual model/effort, selection/deviation reasons, owning entrypoint retry policy, initial and current solution tier, failures and reservations per tier, remaining initial and escalation slots, skipped/forfeited tiers, next escalation and terminal condition. Resuming cannot reset these fields. Shared ledger resources honor the initiating workflow policy rather than forcing delivery's escalation on unrelated workflows.

## Tasks

| Task | Complexity | Rationale |
| --- | --- | --- |
| T1: Delivery matrix and failure progression | 6 | Stateful policy with early promotion, validation and concurrency edges |
| T2: Spec production and readiness guidance | 4 | Bounded requirements propagated to writer, shape and auditor |
| T3: Ledger, recovery and shared leaf contracts | 6 | Preserve accounting across entry points without changing unrelated workflows |
| T4: Public descriptions (`README.md`, engineering manifest), documentation acceptance and packaging checks | 6 | Independently exercise routing/recovery and inspect consistency |

## Acceptance and verification

1. Delivery contains the exact complexity bands and default model/effort progression above, supports effort overlap, anchors calibration on Sol medium, favors smaller capable models, and records justified deviations and availability limits.
2. Both the whole spec and every task require complexity/rationale in production and readiness guidance. Assignment scoring is independent of role and parent score; trivial work uses the ledger.
3. Failed-attempt scenarios from Luna, Terra, Sol and Astra yield maximum totals 6, 5, 4 and 3 respectively. Each tier after the starting tier has one attempt; an escalated Astra failure stops the run.
4. Early promotion forfeits unused initial slots, effort changes add none, stronger validators do not promote solution tier, parallel reservations cannot overrun the tier, and unavailable higher tiers return honestly.
5. Ledger template/procedure and recovery persist the model, effort, complexity and complete escalation state, including main-agent work. A same-run shape/deliver transition preserves delivery policy and allowance. Unrelated workflows retain their existing policy.
6. Engineering leaf agents honor the supplied allocation without a conflicting hardcoded three-failure cap, independent model choices or private retries. Their TOML definitions retain no fixed model/effort.
7. README and the engineering manifest describe delivery-specific escalation without claiming a universal three-failure limit; standalone policies and the existing manifest version remain unchanged.
8. Fresh spec validation precedes production; a different fresh auditor reviews final docs and runs quick validation for every skill directory, then plugin validation for both roots. Exercise policy scenarios by tracing documented decisions, clearly distinguishing these from runtime enforcement. No new executable behavior or redundant string-matching tests are needed.

Evidence: the initiating user requirements in task `01a09bdf-3bb1-72a1-995a-bd2dda0ec2e8`; existing delivery, spec, ledger and leaf manuals are the implementation baseline. The supplied chart motivates considering model and effort together but does not label individual effort points, so it does not establish an empirical ranking for this policy.

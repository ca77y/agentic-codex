# Ledger: <outcome>

## Identity and authority

- Run ID:
- Initiating user request and resolution/endpoint:
- Related prior run ledgers (context only; no inherited attempt count):
- Absolute ledger path:
- Project identity / project root:
- Current checkout:
- Owner/task handle (record unavailable identifiers explicitly):
- Ownership: active / released / transferred / closed
- Prior owner, release evidence, destination and next owner:
- Outcome/problem identity:
- Acceptance source:
- User authority and authorized endpoint:
- Entry points used:
- Spec path and exact revision (or not applicable):
- Overall spec complexity (1–10) / rationale (or no execution spec):
- Owning workflow / retry policy: delivery tier escalation or standalone fixed-three; preserve on resume
- Candidate/artifact paths and exact revision or snapshot:
- Last updated:

## Current progress

- Phase/status:
- Completed work:
- In progress:
- Pending work:
- Blockers and unresolved findings:
- Next action / owner:
- Endpoint reached or unmet condition:

## Tasks and model choices

Record every task/assignment, including direct main-agent work and validation. Keep task scores independent of the overall spec. Trivial work without a spec still has a scored ledger task. Distinguish planned settings from observed settings; mark unavailable actual effort explicitly.

| Task / problem identity | Complexity (1–10) / rationale | Intended model / effort | Actual model / effort / owner | Selection or deviation rationale | Solution tier or evidence-only |
| --- | --- | --- | --- | --- | --- |
| <task> | <score and reason> | <planned> | <observed> | <reason, availability or stronger-start evidence> | <tier or evidence-only> |

## Subagents

Use `none` when no workers exist. Copy one record per dispatch, including validators; retain replaced and failed workers.

### <assignment>

- Returned agent ID: <actual ID, or unavailable if not exposed>
- Canonical task name / coordination handle:
- Configured role:
- Assignment and allowed paths:
- Task complexity (1–10) / rationale:
- Intended and actual model / effort / selection or deviation rationale:
- Problem identity / reserved attempt slot (or evidence-only):
- Status: planned / running / waiting / completed / failed / stopped / unavailable
- Last progress and returned artifacts/results:
- Next action / last updated:

## Gates and evidence

| Acceptance criterion / gate | Spec and candidate identity | Validator handle | Observation/check and evidence path | Result / unresolved findings |
| --- | --- | --- | --- | --- |
| <criterion or gate> | <exact revision/snapshot> | <handle or not applicable> | <observation or command/result link> | <pass / fail / unverified / stale> |

## Attempts and reservations

- Problem identity:
- Governing policy: delivery tier escalation / standalone fixed-three
- Starting solution tier (actual first evaluated solution model; unestablished before evaluation):
- Current solution tier / actual model and effort:
- Current-run aggregate failed attempts:
- Initial allowance / failures / remaining unreserved slots:
- Higher-tier slots remaining (delivery only; one each above the starting tier):
- Skipped or forfeited slots and reason:
- Reserved solution slots and owners: none
- Next escalation / availability / terminal stop condition:
- Explicit additional-attempt authorization: none

| Tier | Allowance under governing policy | Evaluated failures | Reservations / owners | Available slots | Status (initial / future / active / exhausted / skipped / forfeited) |
| --- | --- | --- | --- | --- | --- |
| <tier> | <initial 3 or higher 1; standalone total 3> | 0 | none | <remaining> | <status> |

| Attempt | Task complexity / approach / worker / actual model / effort | Solution tier / candidate or spec identity | Failure evidence and reason | Remaining allowance / escalation decision |
| --- | --- | --- | --- | --- |
| None yet | | | | |

Preserve evaluated failures across gates, workers, turns and entry points within this run. Preparatory work, comment review, baseline defect discovery and pre-work dispatch failures consume no attempts. A submitted spec failing acceptance is a solution failure at its actual production tier; a validator's model alone never changes that tier. Under delivery policy, allow three initial attempts then one per higher tier, with no demotion; early promotion forfeits unused/skipped slots. Under standalone policy, keep the total limit of three. Repeat for genuinely independent problems without splitting an unresolved outcome to reset it. A terminal stop on any problem stops the whole run. Separate later user requests start separate ledgers; retain this history as context.

## Decisions and handoff

- Material decisions / scope changes:
- Invalidated evidence:
- Runtime reconciliation: <live/stale workers, recovered results, uncertain history>
- Useful artifacts and durable evidence paths:
- Ownership transfer / ledger destination:
- Recovery action or required user decision:

---
name: deliver
description: Deliver a change through a verified pull request. Use only when the user explicitly invokes this skill; never invoke it automatically.
---

Explicit invocation of this skill requests delivery through a pull request. It authorizes the task branch/worktree, attributable commits, push after the required gates pass, and creation or update of the same task PR; do not require a separate publication request. Follow the project’s board and forge bindings. Resolve routine design details without requiring a separate `shape` invocation.

Without an explicit deliver invocation, a generic implementation request may remain a local change in the project’s default checkout, including master; it does not imply commits or publication. Deliver invocation does not authorize unrelated messages, review-trigger comments, releases, or merging.

## Ledger ownership

On every invocation, open or create the run's durable ledger using the [ledger procedure](references/ledger.md) and [template](assets/ledger.md) before production or delegation. The main agent is its sole writer, including for trivial work and runs without subagents. Record returned subagent IDs/canonical handles, assignments and progress; update before dispatch and waits, immediately after dispatch, on results and gate/failure changes, and before handoff or the final response. Reuse the ledger on resume and across entry points within the same run, preserving its failure history. A separate later user request gets a new run ledger; prior run history remains context, not its attempt count. Link the ledger in the final response.

## Context and authority

Read the request and acceptance source, relevant code/docs, current checkout and working changes, and any existing PR or prior verification. Reuse a suitable current environment and preserve unrelated work. Read `docs/BOARD.md` and `docs/FORGE.md` when their operations apply. Missing configuration blocks the corresponding operation, not already-authorized investigation or local preparation. Use the actual request and the declaration’s operation-based conditions to determine authorization. Require applicable bindings before the corresponding board/forge writes; do not rewrite declarations to grant yourself authority.

For a documentation-accuracy finding, prepare the correction brief using [claim-wide corrections](references/claim-corrections.md) before production, including direct work. Supply the whole candidate inventory and source evidence, then hand the final correction records to a fresh document auditor.

For repair of an existing PR, read [PR repair](references/pr-repair.md); reuse that PR and branch when authorized. For interrupted work or failed attempts needing persisted recovery, read [recovery](references/recovery.md) before another solution attempt. Load only references relevant to the requested work.

## Required gate order

Every nontrivial change follows **specification + validation → implementation + validation**. Nontrivial means introducing or meaningfully altering behavior, contracts, data, architecture, configuration semantics, or operational procedures, or needing material design decisions. File count and edit size do not decide it: a one-line authorization change still needs the gate. Typographical, formatting, and equally bounded changes with established intent and no material semantic impact are trivial; they can skip a written spec but still require fresh validation. When uncertain, use the specification gate.

Before nontrivial implementation, read [specification and acceptance](references/specification.md). Create or update a durable written spec in the project's location, normally `docs/specs/`, identifying the problem, scope, intended behavior/approach, constraints, observable acceptance criteria, and verification. Require an overall integer complexity score from 1 to 10 with rationale and the same for every task; score integration and uncertainty overall, then each task independently. Reuse a suitable existing spec only after fresh validation against the current request and repository context. A fresh validator must assess feasibility, consistency, product fit, and verifiable acceptance; high-risk or materially uncertain designs require independent challenge in that validation. Record the validated spec revision and gate evidence. Resolve blocking ambiguity and obtain a fresh passing verdict before implementation; human approval is not automatically required when implementation is already authorized.

Investigation, baseline reproduction, and bounded exploratory experiments may establish specification evidence before that gate. They must not become production implementation or bypass the gate under another label.

Implement the validated spec, then use another fresh validator on the final candidate, including affected documentation. Validation covers independent correctness and acceptance review, appropriate required checks, and the relevant criteria. Record candidate and spec identities, results, and unresolved findings. Resolve blocking findings and obtain fresh validation for a correction. Do not claim full completion or publish a completed change with a failed gate or missing required evidence.

If implementation exposes a material spec flaw or requires a material spec change, revise and revalidate the spec before implementing the affected change. Do not weaken criteria to make the candidate pass. Spec or candidate edits invalidate affected evidence and require refreshed validation. Both gates share the same problem history and tier escalation allowance below; a passing gate does not reset failures or permit demotion.

## Completion

Complete delivery by opening the task PR or updating its existing PR after the required gates pass. A local change or local commit alone does not complete an invoked deliver run. The final candidate satisfies relevant acceptance criteria, required checks pass, affected documentation is current, and blocking findings are resolved. Report the artifact, supporting verification, and material limitations. If a gate or endpoint cannot be reached, preserve useful work and state the unmet condition instead of reporting completion.

Optionally assign disjoint implementation/test production to `ca77y_engineering_coder` and bounded spec/doc production to `ca77y_engineering_writer`. Production agents author tests but leave execution and completion checks to fresh validators.

## Ownership and evidence

The main agent owns interpretation, decisions, production, integration, evidence, and the final response. Work directly or delegate bounded production when parallelism or context isolation helps. Use the configured production roles named here when helpful; delegation is optional. Work directly within scope if an optional production role is unavailable. Give each worker the bounded outcome, acceptance source, absolute project and allowed paths, concurrent owners, and problem identity with remaining attempt allocation. Give writers exclusive paths, identify concurrent owners, and require preservation of others' work. Use `followup_task` only for continued production, and `wait_agent` to collect results. Never create another user-owned Codex task unless requested.

Infer the outcome from the request and conversation. Discussion alone does not authorize implementation. Compose explicitly requested outcomes in the same task, meeting each contract; completion of one does not authorize the next. Record scope changes and decisions; preserve failure history for continuations of the same run, and keep a separate later request’s attempt count independent. Ask a focused question only when a missing decision prevents sound progress; continue independent authorized work.

Tie completion evidence to its acceptance source, exact artifact or candidate revision, observation/check, and result. A content digest or an identified unchanged snapshot can identify uncommitted work. Keep this evidence in the mandatory ledger, linking larger artifacts instead of duplicating them. Later edits invalidate affected evidence. Missing, failed, and unrunnable checks remain visible and are never passes.

## Fresh validation

Delegate **every audit and validation** with `fork_turns: "none"` to a newly spawned `ca77y_engineering_auditor` for spec readiness or document acceptance, or `ca77y_engineering_qa` for executable behavior, code review, tests, and implementation acceptance. Select by evidence needed, not command name. QA may cover affected docs/mechanical checks adequately in the same candidate evaluation. Split mixed review only for materially different expertise or unresolved concerns; do not impose QA then auditor as two mandatory final gates. This includes specification gates, correctness and acceptance review, tests, mechanical validators, documentation, citation, link and formatting checks, optional checks, and revalidation. There is no small-edit or documentation exception. Ordinary reading and diagnosis for production may be done directly; evidence used to establish completion belongs to a validator. Do not self-certify or rename checks to avoid delegation.

Fresh means no prior participation in authoring, implementation, or validation of the work examined. Never reuse an implementer, a spec validator for implementation acceptance, or an earlier validator after corrections; use `spawn_agent`, not `followup_task`, for every new verdict. Supply the user requirements and authority, absolute project path and relevant rules, exact candidate and spec identity where applicable, raw evidence, applicable checks, and bounded validation scope. Previous findings identify rechecks, not the answer. The validator reports without editing the candidate. Integrate findings and corrections without overriding a failed gate. If the configured validator is unavailable, preserve prepared work and report the unmet condition; do not substitute a generic worker or validate in the main agent. The plugin's `install-subagents` interface supplies this role.

## Complexity and model selection

Score every bounded assignment from **1 to 10**, including direct work and validation, and record its rationale in the brief and ledger. Score the whole execution spec and every task within it; overall complexity reflects integration, uncertainty and consequences rather than an average. Do not inherit the whole spec's score or model for a simple child task. Trivial work still gets a ledger score even when no written spec is required.

Use **Sol medium as the calibration anchor** for substantial but understood work. Start with the score-derived tier below, preferring the smaller capable model when work lies between tiers. These are operating defaults, not a universal benchmark ranking; high-effort Luna is a first-class option.

| Task complexity | Typical scope | Model | Preferred effort | Other useful efforts when supported |
| --- | --- | --- | --- | --- |
| 1–4 | Clear, bounded work with limited coupling | `gpt-5.6-luna` | `max` | `low`, `medium`, `high`, `xhigh` |
| 5–6 | Several interacting parts or moderate uncertainty | `gpt-5.6-terra` | `xhigh` | `medium`, `high` |
| 7–8 | Substantial design, integration or consequential uncertainty | `gpt-5.6-sol` | `high` | `medium`, `xhigh` |
| 9–10 | Exceptional ambiguity, system-wide coupling or consequences | `gpt-6-astra` | `medium` | `high`, `xhigh` |

The preferred progression is **Luna/max → Terra/xhigh → Sol/high → Astra/medium**. Effort configurations can overlap in capability; exhausting all efforts is not required before promotion. Select only model/effort combinations supported by the actual host. Record unavailable choices and the reason for any supported substitute; never silently invent availability. If no capable supported option exists, return the limitation.

The main agent may choose a stronger start or escalate early when ambiguity, coupling, context needs, error consequences or observed failure justify it. Record the evidence and selection/deviation rationale, rather than promoting by role identity or habit. Never shrink validation scope to fit a model. Keep custom-agent definitions free of fixed model/effort settings; pass explicit selections at dispatch with a fresh context (`fork_turns: "none"`, or a bounded context supported by the tool; validators always use `"none"`).

The main session remains on its selected model. Delegate model-routed solution work to the configured production role when another model is needed; do not claim the session switched itself. Record intended and actual model/effort for direct work too, including why direct work deviates from the matrix. If an optional production role is unavailable, direct work remains allowed but its actual tier governs evaluated attempts. A validator's model is recorded separately and does not promote the solution tier.

## Tier escalation and stop gate

For each unresolved problem in the current prompt-to-resolution run, allow **three evaluated attempts at the starting solution tier, then one corrective attempt at each higher tier through Astra**. The first evaluated solution establishes the starting tier from its actual production model. Preparatory/evidence-only work, unevaluated dispatches and validator model choice do not establish or consume a solution tier. A specification submitted for acceptance is a solution: a failed spec gate counts at its production model's tier. Once established, the same problem's solution tier cannot decrease, even after a passing gate.

| Starting tier | Initial allowance | Higher-tier corrective allowance | Maximum failed attempts |
| --- | --- | --- | --- |
| Luna | 3 | Terra: 1; Sol: 1; Astra: 1 | 6 |
| Terra | 3 | Sol: 1; Astra: 1 | 5 |
| Sol | 3 | Astra: 1 | 4 |
| Astra | 3 | None | 3 |

After the third initial failure, stop further work at that tier and dispatch one evidence-informed corrective approach at the next higher available tier. After an escalated attempt fails, advance again, one attempt per higher tier. An **escalated Astra failure stops the entire run and returns to the user**; an Astra start stops after its third failure. Return earlier when a prerequisite, capable supported higher tier or plausible next approach is absent. If a tier is unavailable, record it as skipped; its slot is not transferable.

Early promotion is allowed with a recorded reason: close/forfeit unused slots at the old tier, skip any bypassed tiers, and allow only one attempt at the new higher tier and each remaining higher tier. Never return to lower/skipped tiers, reset the initial allowance or gain attempts by changing effort. A model switch alone is not an evaluated solution attempt. Stronger validation alone never consumes or grants a solution slot; a failed acceptance verdict belongs to the solution it evaluated.

An attempt is an approach carried far enough to evaluate acceptance, including one that proves unworkable before a candidate. Several edits or checks in one candidate evaluation are one attempt; a corrective approach after an evaluated failure is the next. Exploration, baseline reproduction, comment reading, discovering/reporting defects, and dispatch failures before work are not failed solution attempts. Count evaluated internal failures too; no private repair loops. Specification and implementation failures share the same unresolved problem history.

The allowance belongs to the run from the initiating request to resolution, not the PR, branch, artifact or conversation lifetime. Separate later requests get separate runs. Continuations retain history across workers, models, effort, gates, entry points, checkouts and interruptions, including after a stop. Merely asking to continue grants no extra allowance. A passing gate does not reset an unresolved problem. Close it on verified resolution and restore its history if same-run evidence shows resolution never held. Genuinely independent problems may have separate allowances; never split or rename a problem to evade its failures. Reaching a terminal stop on any problem stops the whole run, including background work.

Before dispatch, record the problem's complexity, production tier, model/effort, remaining allowance and a reservation for each parallel alternative solution. Prefer one owner for successive attempts. Evidence-only validation has no separate solution reservation. Settle results or stop active solution attempts before promotion; retain uncertain reservations until reconciled so parallel work cannot overrun a tier. The main agent aggregates every evaluated failure and owns promotion; leaves receive only their assigned remaining allocation. Recover the durable ledger before resuming; uncertain history is a recovery gap, never a fresh allowance.

At terminal stop, interrupt active workers and execution, preserve their actual status and useful artifacts, and return the unresolved outcome, blocking evidence, approaches/models/efforts and failures at each tier, current candidate, and the specific decision, access, information or explicit additional-attempt authorization needed. Record inability to stop a worker honestly. Further attempts require explicit user authorization recorded alongside the existing history. Saving state is allowed; another experiment disguised as recovery is not. These are workflow instructions, not a hard runtime counter.

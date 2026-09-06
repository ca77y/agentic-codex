---
name: deliver
description: Use only when the user explicitly invokes this skill. Never invoke it automatically.
---

Deliver the requested change through its authorized endpoint. A generic implementation request means a local change; it does not silently authorize committing, pushing, opening a PR, or sending messages. Resolve routine design details without requiring a separate `shape` invocation.

## Context and authority

Read the request and acceptance source, relevant code/docs, current checkout and working changes, and any existing PR or prior verification. Reuse a suitable current environment and preserve unrelated work. Read `docs/BOARD.md` and `docs/FORGE.md` when their operations apply. Missing configuration blocks the corresponding operation, not already-authorized investigation or local preparation. Use the actual request and the declaration’s operation-based conditions to determine authorization. Require applicable bindings before the corresponding board/forge writes; do not rewrite declarations to grant yourself authority.

For repair of an existing PR, read [PR repair](references/pr-repair.md); reuse that PR and branch when authorized. For interrupted work or failed attempts needing persisted recovery, read [recovery](references/recovery.md) before another solution attempt. Load only references relevant to the requested work.

## Required gate order

Every nontrivial change follows **specification + validation → implementation + validation**. Nontrivial means introducing or meaningfully altering behavior, contracts, data, architecture, configuration semantics, or operational procedures, or needing material design decisions. File count and edit size do not decide it: a one-line authorization change still needs the gate. Typographical, formatting, and equally bounded changes with established intent and no material semantic impact are trivial; they can skip a written spec but still require fresh validation. When uncertain, use the specification gate.

Before nontrivial implementation, read [specification and acceptance](references/specification.md). Create or update a durable written spec in the project's location, normally `docs/specs/`, identifying the problem, scope, intended behavior/approach, constraints, observable acceptance criteria, and verification. Reuse a suitable existing spec only after fresh validation against the current request and repository context. A fresh validator must assess feasibility, consistency, product fit, and verifiable acceptance; high-risk or materially uncertain designs require independent challenge in that validation. Record the validated spec revision and gate evidence. Resolve blocking ambiguity and obtain a fresh passing verdict before implementation; human approval is not automatically required when implementation is already authorized.

Investigation, baseline reproduction, and bounded exploratory experiments may establish specification evidence before that gate. They must not become production implementation or bypass the gate under another label.

Implement the validated spec, then use another fresh validator on the final candidate, including affected documentation. Validation covers independent correctness and acceptance review, appropriate required checks, and the relevant criteria. Record candidate and spec identities, results, and unresolved findings. Resolve blocking findings and obtain fresh validation for a correction. Do not claim full completion or publish a completed change with a failed gate or missing required evidence.

If implementation exposes a material spec flaw or requires a material spec change, revise and revalidate the spec before implementing the affected change. Do not weaken criteria to make the candidate pass. Spec or candidate edits invalidate affected evidence and require refreshed validation. Both gates share the same three-attempt failure budget.

## Completion

Deliver the local change, commit, or existing/new PR only to the extent requested and authorized. The final candidate satisfies relevant acceptance criteria, required checks pass, affected documentation is current, and blocking findings are resolved. Report the artifact, supporting verification, and material limitations. If a gate or endpoint cannot be reached, preserve useful work and state the unmet condition instead of reporting completion.

Optionally assign disjoint implementation/test production to `ca77y_engineering_coder` and bounded spec/doc production to `ca77y_engineering_writer`. Production agents author tests but leave execution and completion checks to fresh validators.

## Ownership and evidence

The main agent owns interpretation, decisions, production, integration, evidence, and the final response. Work directly or delegate bounded production when parallelism or context isolation helps. Use the configured production roles named here when helpful; delegation is optional. Work directly within scope if an optional production role is unavailable. Give each worker the bounded outcome, acceptance source, absolute project and allowed paths, concurrent owners, and problem identity with remaining attempt allocation. Give writers exclusive paths, identify concurrent owners, and require preservation of others' work. Use `followup_task` only for continued production, and `wait_agent` to collect results. Never create another user-owned Codex task unless requested.

Infer the outcome from the request and conversation. Discussion alone does not authorize implementation. Compose explicitly requested outcomes in the same task, meeting each contract; completion of one does not authorize the next. Preserve scope, decisions, and failure history when the requested outcome materially changes. Ask a focused question only when a missing decision prevents sound progress; continue independent authorized work.

Tie completion evidence to its acceptance source, exact artifact or candidate revision, observation/check, and result. A content digest or an identified unchanged snapshot can identify uncommitted work. Keep the smallest recoverable record; no universal evidence table is required. Later edits invalidate affected evidence. Missing, failed, and unrunnable checks remain visible and are never passes.

## Fresh validation

Delegate **every audit and validation** with `fork_turns: "none"` to a newly spawned `ca77y_engineering_auditor` for spec readiness or document acceptance, or `ca77y_engineering_qa` for executable behavior, code review, tests, and implementation acceptance. Select by evidence needed, not command name. QA may cover affected docs/mechanical checks adequately in the same candidate evaluation. Split mixed review only for materially different expertise or unresolved concerns; do not impose QA then auditor as two mandatory final gates. This includes specification gates, correctness and acceptance review, tests, mechanical validators, documentation, citation, link and formatting checks, optional checks, and revalidation. There is no small-edit or documentation exception. Ordinary reading and diagnosis for production may be done directly; evidence used to establish completion belongs to a validator. Do not self-certify or rename checks to avoid delegation.

Fresh means no prior participation in authoring, implementation, or validation of the work examined. Never reuse an implementer, a spec validator for implementation acceptance, or an earlier validator after corrections; use `spawn_agent`, not `followup_task`, for every new verdict. Supply the user requirements and authority, absolute project path and relevant rules, exact candidate and spec identity where applicable, raw evidence, applicable checks, and bounded validation scope. Previous findings identify rechecks, not the answer. The validator reports without editing the candidate. Integrate findings and corrections without overriding a failed gate. If the configured validator is unavailable, preserve prepared work and report the unmet condition; do not substitute a generic worker or validate in the main agent. The plugin's `install-subagents` interface supplies this role.

## Model selection

For each delegated task select an available model and supported reasoning effort from the current host's capabilities. Consider responsibility, ambiguity, context needs, consequences of error, reliable capability guidance, and observed outcomes; role identity does not determine the model. Keep a brief selection rationale in the brief. Between two plausible capability tiers, try the lower capable tier first; clearly demanding work can start stronger. Do not infer a universal ranking from names, reduce validation scope, invent availability, or silently substitute an unsupported combination. Custom-agent definitions must omit fixed model and reasoning settings so dispatch selections apply.

After failure, use evidence to improve the approach, increase effort, or select greater capability within the remaining budget. A model change alone is not a new solution. The main agent remains on its task's selected model; it can delegate a bounded harder problem, but cannot promise to switch itself.

## Three-attempt stop gate

Track at most **three failed solution attempts for the same unresolved problem across the main agent and all workers**. An attempt is an approach carried far enough to evaluate acceptance, including an approach that proves unworkable before producing a candidate. Multiple edits or individual checks in one candidate evaluation are one attempt; a corrective approach after an evaluated failure is the next. Exploration and baseline reproduction do not each consume attempts. Evaluated specification and implementation failures share the count; a passed spec gate does not reset it.

The count follows the unresolved outcome across changed errors, hypotheses, models, effort, agents, gates, entry points, checkouts, interruptions, and conversation turns. Unrelated success does not reset it. Close a problem only on verified resolution; restore its history if later evidence shows resolution never held. Independent problems may have separate counts, but reaching three on any problem stops the entire run, including background work.

Give delegated solution work the problem identity and remaining budget, and require all evaluated internal failures to be reported without hidden repair loops. Prefer one owner for successive attempts. Reserve an attempt slot for each parallel alternative solution before dispatch; evidence gathering alone does not consume solution slots. The main agent aggregates failures and escalation decisions. Recover existing history before resuming; persist it in a project-approved durable location when recovery needs it, never only worker handles or disposable scratch. If durable storage is unavailable, return the recovery record and the unmet persistence condition instead of silently resuming without history.

On the third failure, stop active workers and execution: no fourth attempt, further escalation, or publication as complete. Saving artifacts and recovery state is permitted. Return the unresolved outcome and blocking evidence, all three approaches with models/efforts where applicable and why each failed, current candidate and useful completed work, and the specific decision, information, access, or explicit additional attempt authorization needed. Return earlier if essential access, authority, information, or a plausible next approach is absent. Further attempts require explicit user authorization recorded alongside, never replacing, the history. These instructions define workflow behavior, not a hard tool-level runtime counter.

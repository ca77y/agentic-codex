---
name: shape
description: Turn an idea, problem, or evidence into a durable proposal, specification, or board-ready story with observable acceptance criteria. Use for shaping an outcome; implementation requires a delivery request.
---

Produce the requested proposal artifact. Stop at shaping unless implementation was also requested; do not silently create a card.

## Context and authority

Read the goal, relevant product/repository constraints, existing proposals or cards, and supplied evidence. Consult an existing library when relevant, following its conventions; engineering also works without the library plugin. Demonstrate product fit to the degree the proposal needs. Keep factual premises linked to evidence, with assumptions and product decisions identified separately.

Read `docs/BOARD.md` only when a board operation applies. Card creation or updates require the requested scope and an applicable grant to `shape`. Grants to `analyst`, `writer`, or `lead` do not transfer by renaming. Missing or unreconciled bindings block the board operation, while authorized local preparation can continue. Do not rewrite a declaration to grant yourself authority. Read [card authoring](references/cards.md) before preparing an authorized card operation. A board-ready request alone does not authorize filing it.

## Completion and specification gate

The proposal states the problem and intended outcome, scope and exclusions, observable acceptance criteria, material constraints/dependencies, unresolved decisions, and supporting evidence. For a specification intended for execution, use the project spec location, normally `docs/specs/`, and include the intended approach and how criteria will be verified.

A nontrivial change alters behavior, contracts, data, architecture, configuration semantics, or operational procedures, or needs material design decisions. Even a one-line authority change qualifies; when uncertain, use the gate. Every such change follows **written specification + fresh validation → implementation + fresh validation**. A proposal is preparation of that specification, not authority to implement it. An existing spec can be reused after fresh validation against the current request and context; no duplicate is required. High-risk or materially uncertain designs need independent challenge within specification validation.

Have a fresh validator assess the proposal's fit, consistency, feasibility, evidence, and verifiable acceptance criteria before labeling it ready. A material ambiguity or failed gate requires correction and another fresh validator. Do not label an unresolved material decision ready for delivery. Trivial edits with established intent and no semantic impact need no separate written spec but still need fresh validation. Report the artifact, readiness result and evidence, and material open decisions; a clearly labeled draft can be a useful shaping outcome.

## Ownership and evidence

The main agent owns interpretation, decisions, production, integration, evidence, and the final response. Work directly or delegate bounded production when parallelism or context isolation helps. Choose compatible configured custom-agent names; do not import a legacy role pipeline. A production role that mandates auditing or validating its own output is incompatible: do not dispatch it or try to override its core procedure in a task brief. Work directly when no compatible production role is available, within applicable write authority. Give writers exclusive paths, identify concurrent owners, and require preservation of others' work. Use `followup_task` only for continued production, and `wait_agent` to collect results. Never create another user-owned Codex task unless requested.

Infer the outcome from the request and conversation. Discussion alone does not authorize implementation. Compose explicitly requested outcomes in the same task, meeting each contract; completion of one does not authorize the next. Preserve scope, decisions, and failure history when the requested outcome materially changes. Ask a focused question only when a missing decision prevents sound progress; continue independent authorized work.

Tie completion evidence to its acceptance source, exact artifact or candidate revision, observation/check, and result. A content digest or an identified unchanged snapshot can identify uncommitted work. Keep the smallest recoverable record; no universal evidence table is required. Later edits invalidate affected evidence. Missing, failed, and unrunnable checks remain visible and are never passes.

## Fresh validation

Delegate **every audit and validation** to a newly spawned `ca77y_engineering_validator` with `fork_turns: "none"`. This includes specification gates, correctness and acceptance review, tests, mechanical validators, documentation, citation, link and formatting checks, optional checks, and revalidation. There is no small-edit or documentation exception. Ordinary reading and diagnosis for production may be done directly; evidence used to establish completion belongs to a validator. Do not self-certify or rename checks to avoid delegation.

Fresh means no prior participation in authoring, implementation, or validation of the work examined. Never reuse an implementer, a spec validator for implementation acceptance, or an earlier validator after corrections; use `spawn_agent`, not `followup_task`, for every new verdict. Supply the user requirements and authority, absolute project path and relevant rules, exact candidate and spec identity where applicable, raw evidence, applicable checks, and bounded validation scope. Previous findings identify rechecks, not the answer. The validator reports without editing the candidate. Integrate findings and corrections without overriding a failed gate. If the configured validator is unavailable, preserve prepared work and report the unmet condition; do not substitute a generic worker or validate in the main agent. The plugin's `install-subagents` interface supplies this role.

## Model selection

For each delegated task select an available model and supported reasoning effort from the current host's capabilities. Consider responsibility, ambiguity, context needs, consequences of error, reliable capability guidance, and observed outcomes; role identity does not determine the model. Keep a brief selection rationale in the brief. Between two plausible capability tiers, try the lower capable tier first; clearly demanding work can start stronger. Do not infer a universal ranking from names, reduce validation scope, invent availability, or silently substitute an unsupported combination. Custom-agent definitions must omit fixed model and reasoning settings so dispatch selections apply.

After failure, use evidence to improve the approach, increase effort, or select greater capability within the remaining budget. A model change alone is not a new solution. The main agent remains on its task's selected model; it can delegate a bounded harder problem, but cannot promise to switch itself.

## Three-attempt stop gate

Track at most **three failed solution attempts for the same unresolved problem across the main agent and all workers**. An attempt is an approach carried far enough to evaluate acceptance, including an approach that proves unworkable before producing a candidate. Multiple edits or individual checks in one candidate evaluation are one attempt; a corrective approach after an evaluated failure is the next. Exploration and baseline reproduction do not each consume attempts. Evaluated specification and implementation failures share the count; a passed spec gate does not reset it.

The count follows the unresolved outcome across changed errors, hypotheses, models, effort, agents, gates, entry points, checkouts, interruptions, and conversation turns. Unrelated success does not reset it. Close a problem only on verified resolution; restore its history if later evidence shows resolution never held. Independent problems may have separate counts, but reaching three on any problem stops the entire run, including background work.

Give delegated solution work the problem identity and remaining budget, and require all evaluated internal failures to be reported without hidden repair loops. Prefer one owner for successive attempts. Reserve an attempt slot for each parallel alternative solution before dispatch; evidence gathering alone does not consume solution slots. The main agent aggregates failures and escalation decisions. Recover existing history before resuming; persist it in a project-approved durable location when recovery needs it, never only worker handles or disposable scratch. If durable storage is unavailable, return the recovery record and the unmet persistence condition instead of silently resuming without history.

On the third failure, stop active workers and execution: no fourth attempt, further escalation, or publication as complete. Saving artifacts and recovery state is permitted. Return the unresolved outcome and blocking evidence, all three approaches with models/efforts where applicable and why each failed, current candidate and useful completed work, and the specific decision, information, access, or explicit additional attempt authorization needed. Return earlier if essential access, authority, information, or a plausible next approach is absent. Further attempts require explicit user authorization recorded alongside, never replacing, the history. These instructions define workflow behavior, not a hard tool-level runtime counter.

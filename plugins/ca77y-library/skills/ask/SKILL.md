---
name: ask
description: Answer a question, comparison, or synthesis from the existing project library, citing its evidence and exposing gaps or staleness. Does not initiate internet research, persist content, or perform maintenance.
---

Answer in the conversation using the existing library. Stay within retrieval: do not initiate internet research, persist new library content, or perform maintenance merely to fill a gap. Maintain only the separate operational ledger outside the library as required below. Move to `research` only when new investigation is authorized by the request or later steering.

## Ledger ownership

On every invocation, open or create the outcome's durable ledger using the [ledger procedure](../research/references/ledger.md) and [template](../research/assets/ledger.md) before production or delegation. The main agent is its sole writer, including for trivial work and runs without subagents. Record returned subagent IDs/canonical handles, assignments and progress; update before dispatch and waits, immediately after dispatch, on results and gate/failure changes, and before handoff or the final response. Reuse the ledger on resume and across entry points, preserving failure history. Link the ledger in the final response.

## Context and answer

If the library is missing, report the missing setup without writing it. Optionally delegate bounded read-only retrieval to `ca77y_library_librarian`. Read `library/_meta/librarian.md` before library work, then the relevant index/pages and supporting raw evidence. Use focused local retrieval; load only material needed to support the answer. Respect library conventions and distinguish library-supported facts from inference. A missing library or local search gap establishes what was not found, not that a topic or capability does not exist.

Prepare a direct answer with links to the material supporting consequential claims. Include relevant gaps, conflicting accounts, staleness, and uncertainty. Have a fresh validator assess the answer and its cited local evidence within that scope before presenting it as supported; this is answer validation, not permission for a maintenance audit. Give the validator the exact draft in its brief or an existing permitted artifact; do not create library files for an answer-only task. A valid retrieval outcome may be that the library cannot support the requested answer: name the missing evidence without silently starting research.

Answer-only work requires no written specification. Every nontrivial change would require **written specification + fresh validation → implementation + fresh validation**, including material behavioral, data, configuration, or procedural changes even if one line. Such changes are outside this answer-only endpoint and need an authorized contract before production. Trivial changes may skip a spec but never fresh validation. Do not mutate project bindings to expand this endpoint.

Return the supported answer and citations, inference labels, and material limitations. If required evidence validation cannot run, report that unmet condition without claiming a validated answer. No conditional procedural reference is needed for this bounded retrieval workflow.

## Ownership and evidence

The main agent owns interpretation, decisions, production, integration, evidence, and the final response. Work directly or delegate bounded production when parallelism or context isolation helps. Use the configured production roles named here when helpful; delegation is optional. Work directly within scope if an optional production role is unavailable. Give each worker the bounded outcome, acceptance source, absolute project and allowed paths, concurrent owners, and problem identity with remaining attempt allocation. Give writers exclusive paths, identify concurrent owners, and require preservation of others' work. Use `followup_task` only for continued production, and `wait_agent` to collect results. Never create another user-owned Codex task unless requested.

Infer the outcome from the request and conversation. Discussion alone does not authorize implementation. Compose explicitly requested outcomes in the same task, meeting each contract; completion of one does not authorize the next. Preserve scope, decisions, and failure history when the requested outcome materially changes. Ask a focused question only when a missing decision prevents sound progress; continue independent authorized work.

Tie completion evidence to its acceptance source, exact artifact or candidate revision, observation/check, and result. A content digest or an identified unchanged snapshot can identify uncommitted work. Keep this evidence in the mandatory ledger, linking larger artifacts instead of duplicating them. Later edits invalidate affected evidence. Missing, failed, and unrunnable checks remain visible and are never passes.

## Fresh validation

Delegate **every audit and validation** to a newly spawned `ca77y_library_clerk` with `fork_turns: "none"`. This includes specification gates, correctness and acceptance review, tests, mechanical validators, documentation, citation, link and formatting checks, optional checks, and revalidation. There is no small-edit or documentation exception. Ordinary reading and diagnosis for production may be done directly; evidence used to establish completion belongs to a validator. Do not self-certify or rename checks to avoid delegation.

Fresh means no prior participation in authoring, implementation, or validation of the work examined. Never reuse an implementer, a spec validator for implementation acceptance, or an earlier validator after corrections; use `spawn_agent`, not `followup_task`, for every new verdict. Supply the user requirements and authority, absolute project path and relevant rules, exact candidate and spec identity where applicable, raw evidence, applicable checks, and bounded validation scope. Previous findings identify rechecks, not the answer. The validator reports without editing the candidate. Integrate findings and corrections without overriding a failed gate. If the configured validator is unavailable, preserve prepared work and report the unmet condition; do not substitute a generic worker or validate in the main agent. The plugin's `install-subagents` interface supplies this role.

## Model selection

For each delegated task select an available model and supported reasoning effort from the current host's capabilities. Consider responsibility, ambiguity, context needs, consequences of error, reliable capability guidance, and observed outcomes; role identity does not determine the model. Keep a brief selection rationale in the brief. Between two plausible capability tiers, try the lower capable tier first; clearly demanding work can start stronger. Do not infer a universal ranking from names, reduce validation scope, invent availability, or silently substitute an unsupported combination. Custom-agent definitions must omit fixed model and reasoning settings so dispatch selections apply.

After failure, use evidence to improve the approach, increase effort, or select greater capability within the remaining budget. A model change alone is not a new solution. The main agent remains on its task's selected model; it can delegate a bounded harder problem, but cannot promise to switch itself.

## Three-attempt stop gate

Track at most **three failed solution attempts for the same unresolved problem across the main agent and all workers**. An attempt is an approach carried far enough to evaluate acceptance, including an approach that proves unworkable before producing a candidate. Multiple edits or individual checks in one candidate evaluation are one attempt; a corrective approach after an evaluated failure is the next. Exploration and baseline reproduction do not each consume attempts. Evaluated specification and implementation failures share the count; a passed spec gate does not reset it.

The count follows the unresolved outcome across changed errors, hypotheses, models, effort, agents, gates, entry points, checkouts, interruptions, and conversation turns. Unrelated success does not reset it. Close a problem only on verified resolution; restore its history if later evidence shows resolution never held. Independent problems may have separate counts, but reaching three on any problem stops the entire run, including background work.

Give delegated solution work the problem identity and remaining budget, and require all evaluated internal failures to be reported without hidden repair loops. Prefer one owner for successive attempts. Reserve an attempt slot for each parallel alternative solution before dispatch; evidence gathering alone does not consume solution slots. The main agent aggregates failures and escalation decisions. Recover the existing ledger before resuming; preserve failure history there throughout the run, never only in worker handles or files subject to scratch cleanup. If durable storage is unavailable, return the ledger and the unmet persistence condition instead of silently resuming without history.

On the third failure, stop active workers and execution: no fourth attempt, further escalation, or publication as complete. Saving artifacts and recovery state is permitted. Return the unresolved outcome and blocking evidence, all three approaches with models/efforts where applicable and why each failed, current candidate and useful completed work, and the specific decision, information, access, or explicit additional attempt authorization needed. Return earlier if essential access, authority, information, or a plausible next approach is absent. Further attempts require explicit user authorization recorded alongside, never replacing, the history. These instructions define workflow behavior, not a hard tool-level runtime counter.

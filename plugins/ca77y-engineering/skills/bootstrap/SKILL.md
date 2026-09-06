---
name: bootstrap
description: Create, complete, or explicitly repair a project's local board and forge declarations from project facts and user choices. Use for one-time engineering setup, not ordinary implementation or external board/forge operations.
---

Create or complete `docs/BOARD.md` and `docs/FORGE.md` locally. This setup works without the library plugin or existing board/forge bindings. It does not create external projects, cards, branches, commits, PRs, or messages. Normal `shape` and `deliver` tasks consume declarations without loading or running setup.

## Ledger ownership

On every invocation, open or create the outcome's durable ledger using the [ledger procedure](../deliver/references/ledger.md) and [template](../deliver/assets/ledger.md) before production or delegation. The main agent is its sole writer, including for trivial work and runs without subagents. Record returned subagent IDs/canonical handles, assignments and progress; update before dispatch and waits, immediately after dispatch, on results and gate/failure changes, and before handoff or the final response. Reuse the ledger on resume and across entry points, preserving failure history. Link the ledger in the final response.

Read [board authoring](references/board.md) only when preparing the board declaration and [forge authoring](references/forge.md) only for the forge declaration. Use their bundled templates with repository facts and supplied choices. A project may explicitly choose no board or no forge; record that instead of inventing integrations.

The main agent may draft directly or use `ca77y_engineering_writer`. A fresh `ca77y_engineering_auditor` validates the setup spec and a different fresh auditor validates the generated declarations. Give each the explicit bootstrap scope so missing output declarations are not mistaken for missing production prerequisites.

## Setup gates and ownership

Read existing files before writes and preserve unrelated content. Infer supported facts from the request and repository; ask a focused question for unresolved choices affecting authority or destinations. A request to configure an operation does not authorize executing it. A fully configured project needs no changes; a rerun fills missing files within the requested scope and repairs existing content only when that repair is authorized. Report conflicts instead of broadening permissions.

Nontrivial setup follows **written setup specification + fresh validation → scaffold production + different fresh validation**. Draft a proportionate spec in the project’s durable spec location, normally `docs/specs/`, recording setup scope, facts and their sources, choices, artifacts, preservation constraints, acceptance, and verification. The setup spec itself needs no recursively validated spec. On a clean project, supplied facts and bundled templates are inputs; the missing declarations or library conventions being created are expected outputs, not prerequisites. Existing applicable project rules still bind.

The main agent owns the result and may produce it directly. Give any optional production worker the absolute project and exclusive paths, bounded outcome, acceptance source, concurrent ownership, and remaining attempt allocation. Preserve others’ changes. Production workers return artifacts and unexecuted checks, not a verdict. Use `followup_task` only for production continuation and `wait_agent` to collect results. Missing production roles permit direct scoped work; a missing required validator blocks the gate without generic substitution or main-agent validation.

Every check, including optional mechanical checks and corrections, uses a newly spawned validator with `fork_turns: "none"`. Supply exact artifacts, spec identity, source facts, scope, and actual checks without an expected verdict. The validator establishes any missing digest and reports pass/fail/unverified without editing. Later candidate changes invalidate affected evidence; a new validator evaluates corrections. Material spec changes return to the spec gate before affected production. Trivial edits with settled intent and no material semantic impact may skip a written spec, never final validation.

## Models, attempts, and completion

Select an available model and supported reasoning effort for each bounded assignment from actual host capabilities, independently of role identity. Between plausible tiers start on the lower capable tier; demanding work may start stronger. State a short rationale. Escalation changes capability, not scope or the allowance.

Track at most three failed solution attempts for the same unresolved outcome across specification, implementation, validators, workers, models, and resumptions. An evaluated approach, including one that proves unworkable, consumes an attempt; individual edits/checks in one candidate evaluation do not. Share problem identity and remaining allocation; no private worker loops. Restore failure history from the mandatory ledger before resuming and keep it current throughout the run. At the third failure stop the entire run and background work; preserve useful artifacts and evidence and report the three approaches and required decision/access or explicit additional-attempt authorization. No fourth attempt without that authorization, recorded alongside the history.

Return created/updated paths, preserved existing content, validation evidence tied to the exact spec and candidate, and unresolved setup gaps. Do not claim completion while a required gate is failed or unverified. Report missing tools as concrete prerequisites, without inventing access or provisioning replacement tools.

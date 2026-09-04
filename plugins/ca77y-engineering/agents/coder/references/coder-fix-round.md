# Findings round

Read the supplied spec, full findings set, fix/round references and current tree. A fresh dispatch has no earlier reasoning to rely on. Apply all findings within scope in one round. For each, state the general property, inspect all applicable instances, and report any you cannot close. A conflict with the spec goes to the lead; rejecting a finding requires a concrete input/state traced through the actual implementation to its output.

For a behavioral bug fix, prefer a focused test-first reproduction: observe the relevant assertion fail before the fix, then pass after it. If implementation already exists and sensitivity still matters, use an isolated disposable copy/check-out with a known baseline and the same provisioned toolchain; do not undo source in the shared worktree or source served by a live browser/device lane. Ask the lead to supply an isolated environment if needed; do not install dependencies or create branches yourself. Never overwrite unexplained edits to prepare a probe.

Report each behavioral fix as **demonstrated** (test, baseline, observed failing assertion, passing result), **not demonstrated** (including named tests that could not run, with reason), or **nothing can reach it** (concrete reason no test seam exists). Missing evidence means not demonstrated. Isolation unavailable means not demonstrated, never permission to revert shared source. A passing test alone does not establish regression sensitivity.

For document behavior, provide the exact changed passage, stable region, finding it answers and what would be missing without it; use artifact inspection even when unrelated code tests exist. Routine documentation, naming, comments, test-quality edits and behavior-preserving refactors need appropriate checks, not forced red/green demonstrations. No demonstration is required for a rejected finding with a supported trace.

Return all fixes, evidence outcomes, rejection traces, unresolved instances and production hazards in the final report. The lead routes affected QA/acceptance again; old approval does not cover the changed revision.

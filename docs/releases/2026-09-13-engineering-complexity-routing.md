# Engineering 3.2.0

Delivery now records complexity for the whole execution spec and each task, and chooses models per assignment with a bias toward smaller capable models. The default bands are 1–4 Luna/max, 5–6 Terra/xhigh, 7–8 Sol/high and 9–10 Astra/medium. Sol medium anchors calibration; supported effort alternatives and evidence-backed stronger choices remain available.

Each predeclared delivery task/problem gets three attempts at its own starting model tier, then one corrective attempt at each higher tier through Astra. Spec production has separate history from its implementation tasks, so an Astra-authored spec can contain a complexity-2 task starting on Luna. Revalidating a reused spec is evidence-only and does not require a historical author model. Within the same task/problem, early promotion forfeits unused slots; effort changes, stronger validators and resumptions do not reset the allowance. An escalated Astra failure returns control to the user. Standalone shaping, library and setup retain their existing limits.

The ledger preserves overall/task complexity, stable task/problem identities, intended and actual model/effort, selection rationale, per-task tier failures and reservations, skipped slots and recovery state. Supported substitutions use another listed model or a host-confirmed alias; an unresolved model identity is reported rather than assigned a guessed tier. Agent definitions remain free of fixed model settings. These are workflow instructions, not an enforced runtime counter.

Engineering 3.2.0 packages [delivery complexity routing](../specs/delivery-complexity-routing.md) through PR #8 and supports local plugin/managed-agent installation. The library plugin version is unchanged. Delivery retains its PR endpoint and claim-wide correction procedures.

After updating the plugin, run its managed installer from the updated source and start a new Codex task to load the new skills and agent definitions. The installer reads the manifest version for generated metadata; do not edit those comments by hand.

# Engineering 3.2.0

Delivery now records complexity for the whole execution spec and each task, and chooses models per assignment with a bias toward smaller capable models. The default bands are 1–4 Luna/max, 5–6 Terra/xhigh, 7–8 Sol/high and 9–10 Astra/medium. Sol medium anchors calibration; supported effort alternatives and evidence-backed stronger choices remain available.

An unresolved delivery problem gets three attempts at its starting model tier, then one corrective attempt at each higher tier through Astra. Early promotion forfeits unused slots; effort changes, stronger validators and resumptions do not reset the allowance. An escalated Astra failure returns control to the user. Standalone shaping, library and setup retain their existing limits.

The ledger preserves overall/task complexity, intended and actual model/effort, selection rationale, per-tier failures and reservations, skipped slots and recovery state. Agent definitions remain free of fixed model settings. These are workflow instructions, not an enforced runtime counter.

This minor release packages [delivery complexity routing](../specs/delivery-complexity-routing.md). The user's release request authorizes publication and installation and supersedes that implementation spec's local-only endpoint and unchanged-version acceptance condition. The library plugin version is unchanged. The release also retains the upstream PR endpoint and claim-wide correction procedures.

After updating the plugin, run its managed installer from the updated source and start a new Codex task to load the new skills and agent definitions. The installer reads the manifest version for generated metadata; do not edit those comments by hand.

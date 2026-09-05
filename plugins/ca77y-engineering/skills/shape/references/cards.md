# Card authoring

Read only when a requested card operation applies. The main skill's authority and validation rules remain mandatory.

Read the project's `docs/BOARD.md` for tracker identity, tool bindings, card schema, statuses, human gates, and role-specific write grants. Establish the exact target from the request; use bound read/search operations to locate related cards when relevant. A product-fit or duplicate audit is validation and must use a fresh validator. Missing access is a disclosed evidence gap.

Prepare the requested card content using the board's shape: problem and intended outcome, scope/exclusions, observable acceptance criteria, material dependencies, and evidence. Keep assumptions and decisions separate. Inspect existing content before proposing an update and preserve unrelated fields. A proposal with unresolved material decisions remains a draft.

Create/update only if the request authorizes that operation and the declaration explicitly grants it to `shape`. Legacy role names do not transfer authority. If this binding is absent, preserve a local proposal and name the missing operation; do not run the legacy analyst merely to obtain its grants. Reconciliation requires an authorized declaration change before enabling writes, not a per-run inferred alias.

Use the declared initial status for creation. Never cross a human gate, change product intent, or rewrite acceptance criteria to match an implementation. Comments or notifications to other people require explicit user authorization. Give the validator the proposed content and acceptance source; validation does not grant permission to submit. Any post-write content or round-trip check also belongs to a fresh validator. Return the actual saved identity or the prepared artifact and blocked operation.

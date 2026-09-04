---
name: board
description: Write, repair, or inspect a project's `docs/BOARD.md` declaration — how the pipeline tracks work. Invoked by the user; never a per-run step for the `lead` or the `analyst`, which read the declaration directly. Does not move, edit, or create cards.
---

Inspect, write, or repair `docs/BOARD.md`, the project's declaration of work tracking. This skill manages the declaration, not cards. Board and card are roles: repository files, a hosted tracker, or no board are all valid.

## Choose the requested action

- **Inspect:** read the existing declaration and report its bindings, authority, and gaps. Do not interview the user or load authoring guidance for a routine inspection.
- **Write or repair:** when the user authorizes it, read [authoring BOARD](references/authoring-board.md), inspect existing project evidence, and complete the change. Ask only for unresolved decisions that affect authority or correct bindings; bundle them.
- **Discovered during a delivery run:** report the gap or a draft. Do not create a declaration merely because an orchestrator found it missing. Existing explicit user authorization to author/repair still applies.

## Declaration contract

The fixed path is `docs/BOARD.md`. It binds locate, read, search, create, and transition; comment/update exist only where authorized. Each operation names a concrete mechanism or is explicitly unbound. It also records card shape, initial status, full status vocabulary, work-started/awaiting-review from/to values, human-reserved transitions, where writes become visible, and exhaustive write authority.

If the declaration lives elsewhere, use the authoring reference during an authorized repair to move it or add a fixed-path pointer without duplicating bindings. Inspection simply reports the location gap.

## Boundaries and report

Verify bindings read-only against available real cards. Never create, edit, transition, or comment on cards, and never invent endpoints, fields, statuses, or locations. Mark unresolved or unreachable facts. Use configured authentication; do not read `.env` or output credentials.

Report the file path, what it declares or what changed, evidence verified, and material unresolved decisions. Routine inspection ends with that report; authoring does not require a second invocation for readback.

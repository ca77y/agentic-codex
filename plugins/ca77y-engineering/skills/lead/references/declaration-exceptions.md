# Declaration exceptions

Read when a declared operation is unbound, a board transition cannot apply, or extra board authority is relevant.

- No forge: complete the pipeline and end at the final commit, pushed only if push is bound. Put the change description in the report and authorized card handoff.
- Update unbound: report the description changes needed. Review trigger unbound: state that a human must fire it. No review configured: report that human review is pending.
- No card, board absent, or transition unbound: do not transition. A different current status is left alone and reported. Only work-started and awaiting-review transitions are defaults; human-reserved states stay human-owned.
- Apply comments, attachments, and writer-reported corrections only where BOARD grants that authority. Preserve the affected card, stale sentence, and replacement in the ledger; report reserved follow-ups. Respect the declaration's visibility rule for every write.
- BOARD authorizes board operations; FORGE authorizes repository/change operations. Neither supplies guessed bindings for the other. Missing FORGE still stops before any run side effect.

### Keep the forge review declaration aligned with the active GitHub reviewer

**Area:** flow

**Observed:** `docs/FORGE.md` declares that no automated reviewer or review re-fire binding exists, but PR #2 received a Codex review and its GitHub review summary names `@codex review` as a trigger. The fix run therefore had review findings to address but was forbidden from using the trigger the active reviewer advertised.

**Suggested change:** Reconcile `docs/FORGE.md` with the repository's active review integration and bind the exact supported re-fire operation when it is intentionally available; otherwise disable or remove the integration so the declaration remains authoritative.

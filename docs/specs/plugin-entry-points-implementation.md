# Entry-point implementation boundary

Implements [the entry-point contract](plugin-redesign-entry-points.md) in the current repository. The user authorized local implementation directly on `master`, without using the current engineering plugin to perform the work.

## Approach and scope

- Add `shape` and `deliver` to engineering, and `research` and `ask` to library, with implicit discovery and conditional references beside each skill. Each core manual carries its applicable authority, evidence, independent validation, model selection, and aggregate recovery requirements.
- Preserve existing public workflows, specialist manuals, setup interfaces, and scripts. Their migration is outside this change. Describe the new entry points as the recommended interface and identify the retained workflows separately.
- Supply one small, report-only `validator` leaf per plugin, with managed TOML source metadata and no model or effort fields. This is the minimum integration needed for standalone fresh validation: existing engineering acceptance requires old pipeline artifacts, and the library plugin must not depend on engineering. Do not redesign other specialists or the installer.
- Keep board and forge declarations unchanged. A new entry point cannot inherit grants to `analyst`, `writer`, or `lead`; absent an explicit applicable grant, it prepares local artifacts and reports that the external operation is unavailable. Do not enable writes by rewriting authority during a run.
- Update README and plugin presentation metadata to expose the outcomes. Leave release versions, marketplace registration, personal installation, and compatibility migration for a release request.

## Observable acceptance and verification

The scenarios in the source specification are the behavioral acceptance source. A fresh reviewer assesses all four manuals and their applicable references against those scenarios, including required gate order, corrected-candidate freshness, shared failure counts, unavailable validators/providers, and the proposal/answer/publication boundaries. Report static instruction coverage separately from exercised behavior; instruction files do not enforce a tool-level retry counter.

Run the skill quick validator for every skill directory and the plugin validator for both roots. Run the existing installer tests and source checks because new validator resources must be distributable; use temporary install destinations to inspect generated validator instructions and their independence from the other plugin. Do not install into the user's live configuration.

Use focused independent scenario exercises for ambiguous selection or recovery behavior when useful. Any test outputs belong in a temporary workspace. Preserve the provided specification and unrelated working files. Record the spec and candidate identities with the validation results; any affected correction requires a new validator.

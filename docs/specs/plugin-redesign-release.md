# Plugin redesign audit and release

## Scope

Audit the implementation at `b83f1da` against [the specialist integration specification](plugin-specialists-and-skill-integration.md), repair concrete defects, and release both independently installable plugins. The user's release request authorizes the commits, publication of the audited master history, tags, and GitHub releases needed for this release; it does not change the repository's standing forge declaration or authorize unrelated operations.

The accepted specialist specification remains the behavior contract. Any repair that materially changes that contract requires a specification correction and fresh validation before implementation. Audit findings that restore the existing contract may be repaired after a fresh readiness verdict on that contract and this release scope. Preserve existing research content and unrelated edits.

## Release behavior

- Bump Engineering from `2.10.0` to `3.0.0` and Library from `1.6.0` to `2.0.0`, once, using plain semantic versions. Removal of old workflows and agent identities is breaking.
- Before publication, a fresh validator resolves `origin/master`, confirms it is an ancestor of the accepted candidate, and checks that both intended tags are absent locally and remotely and both GitHub release records are absent. Existing names or changed/diverged remote history require reconciliation before publication; never overwrite them.
- Create `ca77y-engineering-v3.0.0` and `ca77y-library-v2.0.0` tags at the validated commit. Publish that commit to the existing `origin` master and both tags in one atomic, fast-forward git push. Never force-push. If the server rejects atomic publication, preserve the local candidate and report the blocker.
- Create corresponding GitHub releases in `ca77y/agentic-codex` using the published tags. GitHub release creation is separate from git publication: if one API operation fails, report partial state and recover only the missing record at the same validated tag. Do not move an existing tag or overwrite a release.
- Release notes describe the new entry points, bounded specialists, independent validation, model selection, shared failure limit, bootstrap, and the breaking interface removal. Include the plugin version and ordinary agent-installation/catalog-reload guidance. Do not install into the user's live configuration as part of release.
- Keep the existing marketplace identity and paths; a version bump does not need a marketplace rewrite.

## Acceptance and evidence

Fresh agents audit engineering behavior, library behavior, installer safety, package contents, and documentation. Report instruction inspection separately from behavior actually exercised. All selected validation, including corrected candidates and release verification, is delegated to newly spawned agents with no inherited conversation.

Before publication, resolve blocking findings and obtain fresh acceptance of the corrected candidate. Run every skill quick validator, both plugin validators, both installer suites, and meaningful actual-resource temporary installation checks; include safe stale cleanup, unmanaged/other-plugin preservation, and installed reference survival. Inspect applicable specialist-spec acceptance scenarios, including bootstrap reruns and missing prerequisites. Record exact candidate identity and any limits of evidence.

After publication, a fresh read-only validator checks that remote master and both tags identify the accepted commit, both published release records reference the expected tags, and released manifests contain the intended versions. Report the actual release URLs and remaining limitations. Three failed solution attempts for the same unresolved outcome stop the run across repairs, agents, and gates; no fourth attempt or publication while blocked.

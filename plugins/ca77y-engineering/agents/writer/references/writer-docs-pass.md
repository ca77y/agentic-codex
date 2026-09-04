# Docs pass

Run after QA and before final acceptance. Read the spec, project documentation conventions and any project docs-writing skill, nearby docs, and stated product principles if present. Update existing homes rather than duplicate them; do not assume Obsidian, a particular architecture file, or a commit-message format.

## Establish the result

Read `git -C <worktree> diff <spec-commit>..HEAD` to locate changes and `git -C <worktree> log <spec-commit>..HEAD` for intent. Then inspect the **resulting tree**, including unchanged callers/configuration relevant to each durable claim. The final tree establishes behavior; the diff alone does not. Report missing commit references and distinguish inspected tree evidence from claims resting on spec intent alone.

Reconcile each spec claim against that evidence. Document intended behavior that exists; when the tree reveals a regression against the accepted contract, report it for repair instead of making it correct by documenting it. The lead routes behavioral defects back through affected QA and acceptance.

## Convert and reconcile

Fold capability contracts and requirements into the project’s feature docs, journeys into flow docs, and design rationale into design/architecture docs, using the categories the project actually has. Every paragraph, list item, table row and diagram touched must agree with the resulting tree and stated principles. Check surrounding docs for stale links, duplication, and contradictions introduced by the conversion. If a principle itself may be stale, report rather than rewrite the product’s purpose; if none exist, say that only the tree standard was available.

Before removing the converted live spec, confirm the lead preserved the approved spec at `tmp/accepted-spec.md` in ignored run state with its recorded source commit. If the snapshot is missing, ask the lead to preserve it and continue independent docs work; do not delete the only acceptance standard. Once durable content has a home and the snapshot is confirmed, remove the live spec rather than archive it. Report conversion destinations, removal and snapshot path. Existing-PR repairs use the historical temporary spec recovered by the lead; do not remove that temporary acceptance input. Report unresolved claims before acceptance.

## Self-check

Run project formatting/lint/loader checks applicable to your changed documents, path-scoped or check-only; never a repository-wide write. Match semantic checks to the document even if the repository has code tests. No applicable command is **not defined**, not a failure. A defined command that cannot run or depends on unavailable provisioning is **unrunnable**.

Fix failures in your own files and rerun. Report unrelated failures without modifying them. Report **ran clean**, **failures found in this pass’s own files and re-run clean**, **not defined**, **unrunnable**, or **not clean** with file, failure and attempted remedy. This self-check covers your output; final acceptance follows it. Later contract/behavior changes invalidate affected QA and acceptance evidence; later docs changes invalidate affected acceptance evidence.

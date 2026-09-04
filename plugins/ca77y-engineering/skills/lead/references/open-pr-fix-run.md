# Open-PR repair

Read when the user supplies an existing PR or its review findings. Use the same branch and PR. The lead's authority, evidence rules, and attempt limit still apply.

## Recover inputs

1. Read BOARD and FORGE, then the PR and card handoff through their read bindings and `git -C <repository> log`. Recover the branch, original spec path and commit, completed rounds, and current findings. A surviving ledger is a cross-check, not the only durable record.
2. Reuse the worktree or recreate it on the existing branch through the declared binding. Follow [workspace setup](workspace.md), including verification/reestablishment of dependency provisioning and ignored scratch state, before dispatch. Never assume a recovered worktree is provisioned.
3. The docs pass normally deleted the live spec. Read its exact historical contents with `git -C <worktree> show <spec-commit>:<spec-path>` and save them, unchanged, with the file-editing tool as ignored `tmp/accepted-spec.md`. Record provenance in the ledger. Do not restore it to the live specs area or commit this historical copy. If refs are missing, locate the spec commit from branch history; if it cannot be recovered, ask the writer to reconstruct a live spec from durable task/card evidence and obtain readiness before implementation. Do not invent historical criteria or complexity.
4. For unchanged scope, the historical copy is the repair baseline and supplies the complexity score. For changed scope/approach, dispatch the writer to create a live revision in the project's specs area, gate it, commit it, and use that live revision for downstream work. Keep the historical original untouched; before docs, save the newly approved revision separately as the current acceptance input and record its provenance. Retain the writer's board follow-ups.

## Repair and verify

Start fresh workers in this new run, carrying spec path/provenance, worktree/status, prior commit refs, findings, and ownership. Route code to the scored coder, docs to a fresh docs writer, and scope changes through readiness. Later rounds follow the lead's normal resume rules.

Commit repairs and QA-added tests before fresh reviewers. Code/executable changes require affected QA and acceptance; docs changes require affected acceptance. Run docs against changed behavior before acceptance, passing the saved spec when no live one exists. If a revised live spec was created, the docs pass converts and removes it; acceptance reads the saved approved revision against the final tree. Never claim old evidence covers a changed revision.

Push only after required evidence is current and blockers closed, at FORGE's declared timing. Update the existing description through its update binding to reflect the final result, validation, hazards, spec provenance, and follow-ups. If update is unbound, report the needed changes. Re-fire review only through its declared binding; otherwise report that a human must trigger it. Do not wait for the response.

Leave the card at awaiting review; do not repeat start/review transitions. Return the existing PR link, repair outcome, evidence, and remaining limitations. A returning unresolved finding keeps its attempt count within this run; the three-attempt rule still stops publication.

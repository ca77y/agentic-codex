# Repair an existing PR

Read when the requested change repairs an existing PR or responds to its findings.

Read applicable forge bindings and inspect the existing PR, branch/base, working changes, original acceptance source, and findings. Reuse the current suitable environment and existing PR/branch. Do not reset or discard unexplained changes, create a replacement PR.

Determine which findings are defects, missing evidence, or requests for a material scope change. Resolve routine design details within the authorized repair. A material contract change requires a revised spec and fresh specification validation before the affected implementation; an existing relevant spec also requires fresh validation before nontrivial work. Reconstruct missing acceptance evidence from authoritative artifacts, and report what cannot be recovered rather than inventing it.

Identify the current user request before recovering attempts. A separate request to check or address PR comments starts a new run with its own ledger and zero failed attempts, even when the PR has prior failures. Inspecting comments and discovering or reporting findings do not consume solution attempts. When continuing the same unfinished run, recover its attempt history before a correction; changed errors, reviewers, entry points, or checkouts do not reset that run's count. Use the core skill's fresh validation for the final candidate, including repaired findings, affected regressions, and documentation. Failed candidates and failed spec approaches consume the same aggregate budget within the current run.

Push or update the PR only when that endpoint was requested, the forge operation’s binding and conditions apply, and the required gates pass. Follow the bound operations; avoid unrelated history changes. User authorization to implement does not by itself authorize comments or review-trigger messages to others. Report addressed findings, current verification, the existing PR identity, and any remaining blocked endpoint.

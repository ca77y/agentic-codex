# SMR-299: Correct false claims across the whole change

Acceptance source: [SMR-299](https://linear.app/ca77y/issue/SMR-299/correct-false-claims-across-the-whole-change), retrieved 2026-09-08.

## Problem and scope

The writer's documentation procedure preserves facts and references, and the auditor compares documents against evidence, but neither defines the evidence and search needed to correct a false claim throughout a candidate. Add that procedure to the writer documentation reference, correction-brief routing under deliver, and the auditor acceptance reference. This is an operational documentation change requiring both gates.

The authorized endpoint is a PR for SMR-299. The user also requires the deliver and forge endpoint rules below. Library content, historical hangboard sources, releases, installed agents, and merging are out of scope. Preserve unrelated working files. No runtime code or fixed evidence schema is required.

## Intended behavior

When a documentation-accuracy finding identifies a false claim, deliver briefs name the claim, corrected meaning and material qualifier, exact candidate file inventory and baseline, supplied source evidence, bounded write ownership, and durable evidence output. Put detailed correction instructions in a conditionally loaded deliver reference. The procedure also applies when the orchestrator produces the correction directly.

The writer records sentence-level source evidence, enumerates restatements, and performs a production search over every candidate file after wording settles. This search is evidence gathering, not independent validation. Candidate inventory includes committed, staged, unstaged, and attributable untracked changes relative to the run's baseline, including renamed paths; unrelated work is excluded explicitly. Deleted or unreadable files are accounted for instead of silently skipped. Reading across the inventory does not grant writes: non-document/code/test corrections go to the main agent or the appropriate authorized owner. Re-run affected evidence and the whole candidate search after correction changes.

A fresh auditor evaluates the exact final candidate and supplied records against sources, including coverage and material qualifiers. Missing support or incomplete evidence blocks the affected acceptance. Existing freshness and failure-budget rules remain in force.

## Acceptance criteria

The following preserve the card's requirements:

1. A false-claim finding defines the unit of correction as the claim across the candidate change, including prose, tests, identifiers, comments, tables, and source documentation.
2. The writer supplies a structured sentence-by-sentence evidence record for the affected passage; every sentence, including connective and summary sentences, cites the supporting `path:line` and observed value. A table is acceptable but not a fixed schema.
3. The evidence record separately dispositions every restatement of the claim in sibling paragraphs, related tables, and source docstrings.
4. After settling wording, the writer searches all files in the candidate change for the claim's distinctive terms and meaningful negations without an extension filter, then records a keep/change disposition and reason for every hit, including test names, identifiers, and inline comments.
5. When wording is qualified rather than removed, every retained restatement carries the same material qualifier.
6. The fresh document auditor grades the supplied sentence and restatement evidence item by item against source rather than accepting the prose rewrite by appearance.

## Verification

A fresh document auditor maps each criterion to the final instructions and follows a tabletop correction spanning a summary, sibling paragraph, table, docstring, test name, identifier, and inline comment. Check that out-of-scope writes are routed, unsupported sentences and missed hits cannot pass, and qualifiers survive all retained restatements. Check relative links and packaging inclusion for the changed references. Run the skill quick validator for every skill directory and the plugin validator for both plugin roots, as required by AGENTS.md. Record exact candidate/spec digests and actual results in the run ledger or linked evidence. Runtime tests are not needed for this instructions-only change.

## Delivery endpoint rules

Acceptance source: the user clarified that manually invoking deliver always ends in a PR, while implementation requested without the skill may be done locally on master.

Update deliver and docs/FORGE.md so explicit invocation authorizes the task branch/worktree, attributable commits, push after passing gates, and creation or update of the same task PR. No additional publication request is required. Keep explicit-only invocation, fresh gates, bindings, branch protections, and user-controlled merge intact. An ordinary implementation request without deliver may remain an uncommitted local change on master unless the user requests another endpoint. Invocation does not authorize unrelated comments, review-trigger messages, releases, or merges.

Reconcile the current README, deliver PR-repair reference, bootstrap forge template, and plugin suggested implementation prompt so they do not advertise local-only deliver completion or require a second PR request. Historical specs describe prior contracts and are not rewritten. The installed plugin cache is not an edit site; publication updates repository source without a release or reinstall.

Additional acceptance criteria:

7. Explicit deliver invocation is itself a PR endpoint request, including branch/worktree, commits, verified push, and open/update of one PR for the requested change.
8. Without deliver, a generic implementation request may remain local on master; no automatic commit or publication is implied.
9. Current affected descriptions and references consistently express those endpoints, while independent gates, bound destinations, protected master, and user-controlled merge remain intact.

Verification adds tabletop requests for explicit deliver work on an issue, generic implementation without the skill, and deliver repair of an existing PR. Grade endpoint and branch choice and confirm no second publication permission is required. Validate all skills and both plugins on the isolated final candidate before commit and push; retain exact snapshot evidence and real PR URL in the ledger.

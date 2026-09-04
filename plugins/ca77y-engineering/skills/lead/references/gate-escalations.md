# Gate escalations

Read when a criterion is mis-worded, a problem reaches three unresolved attempts, or junior work needs promotion.

## Attempt limit and promotion

After three unresolved attempts on the same blocking problem, stop and report it before publication. Commit attributable completed repairs under FORGE, but do not open/push a failed result around the blocker. No fourth attempt by the same tier.

The single exception is a junior coder's implementation problem: replace it with a fresh `ca77y_engineering_senior_coder`, using the run's senior model and `high` effort. Pass the findings, what junior tried, why it failed, spec and commit refs, worktree/status, and ownership. Record promotion; senior gets three attempts and remains the coder for the run. No further promotion or concurrent coder. Spec, QA-owned, and wording problems do not gain a coder promotion budget.

## Mis-worded acceptance

A mis-worded criterion is an unresolved acceptance-wording handoff, **not accepted work**. Do not quietly rewrite a post-build card or ask the coder to make the wording pass. Once every other criterion is met and no behavioral blocker remains, the run may proceed with this explicit exception.

Name the `ACn`, sub-case, evidence, and unresolved wording in the PR description, authorized card handoff, and final report. The human owns correction in a later run's spec pass. Keep the auditor's not-ready verdict visible; never relabel it passed. Any unverified or defective behavior remains subject to the normal blocking rules.

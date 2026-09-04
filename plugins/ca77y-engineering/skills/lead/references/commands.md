# Project commands and late changes

Read when running spec formatting, the initial lint floor, or final validation. Discover commands from project context; do not invent a checker.

| Outcome | Action |
| --- | --- |
| Defined and runnable | Run and inspect its result |
| Not defined, including CI-only with no local equivalent | Record the limitation; skip |
| Dependencies unavailable/untrusted, or command cannot start | Report unrunnable; do not attribute its output as a defect |

Settle trustworthiness before file attribution. `no dependencies required` is as trustworthy as `provisioned`. Never use a fetch-and-run CLI.

Format only attributable changed paths; use check-only if the command cannot accept paths. Capture the changed-file set first. Unexpected writes outside the allowed set stop staging: preserve them and report, never sweep them into the commit. A check-only failure goes to its owner. Format spec changes before readiness; never alter the passed spec before committing it without another readiness review.

Run the initial lint floor once after the spec commit. Failures on paths that commit landed go to the writer, are reformatted, and receive readiness review if they change the spec contract. Commit the fix before coding. A failure confined to untouched paths is a baseline limitation; relay it without widening scope unless a causal connection makes it necessary to the requested outcome. Escalate a required scope change through the writer.

Run final validation before final acceptance. Trusted failures on this run's paths go to the coder for code or writer for docs; rerun the affected command after repair. Preserve reports on unrelated baseline failures. A required but unverified check is handled by the explicit declared release policy; absent permission for that limitation, stop publication.

Any later correction invalidates the affected evidence: behavior or executable content returns through QA and acceptance; prose-only changes through affected acceptance. Commit repairs before fresh reviewers. Apply the lead's three-attempt limit. A surviving blocking defect stops before publication; mentioning it in the description never licenses shipping it.

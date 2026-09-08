# Installed agent version metadata evidence

Problem: `version-metadata`. Shared failed attempts: 0 of 3.

Specification: `agent-install-version-metadata.md`, SHA-256
`d055b70897bf5653727ed4ac9e10c51d5093c101a9867c1211dfd263fa2c8e3b`.
Fresh `ca77y_engineering_auditor` (`version_spec_review`, GPT-5.6 Sol,
medium effort) returned **pass** with no findings. Ownership compatibility,
manifest provenance, drift, scope, and observable acceptance were reviewed.
Baseline installer suites passed with 16 tests per plugin; these do not establish
implementation acceptance.

Implementation acceptance: **pass**, fresh `ca77y_engineering_qa`
(`version_implementation_qa`, GPT-5.6 Sol, medium effort), no findings.
The candidate remained stable during review. SHA-256 prefixes: both installers
`d6b53b0e`, both test suites `fbfd0e31`, engineering installation skill
`3712848d`, library installation skill `4386a9bc`; specification identity above.

Both isolated installer suites passed 20 tests each. All eight skill quick
validators, both plugin validators, and `git diff --check` passed. QA reviewed
version provenance and exact comments, schema preservation, version-only drift
and idempotence, legacy upgrades and stale cleanup, invalid-version refusal,
ownership/conflict safety, and affected documentation. No live agent directory
was used as a test target.

After acceptance, both repository installers completed successfully against
`~/.codex/agents/`. Engineering reported 10 installed/updated files and library
reported 11; neither reported unchanged or removed files. These carry manifest
versions 3.0.0 and 2.0.0 respectively. Plugin caches and manifests were not
modified; this is an unreleased local installer change. Installation results are
production output, not an independent live-directory audit.

Patch publication acceptance: **pass**, fresh `ca77y_engineering_qa`
(`version_release_qa`, GPT-5.6 Sol, medium effort). Candidate composite SHA-256
before this verdict append:
`3af5b9490cab44122813c12c96ed2a11834beb4f2dd2b52c3e86ffef1ee7d38c`.
Engineering 3.0.1 and library 2.0.1 manifests, canonical names, root release rule,
and release note were accepted. Both installer suites passed 20 tests each; all
eight skill validators, both plugin validators, and whitespace checks passed.
No findings; failed attempts remain zero. Publication of the patch versions is
authorized by the user's request to push the new version.

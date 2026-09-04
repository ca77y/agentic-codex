# Regression evidence in findings rounds

Read the coder’s report per behavioral fix. Trust a **demonstrated** test-first or isolated red/green result unless contrary evidence appears; do not repeat it mechanically. Treat missing outcomes as **not demonstrated**. Carry **nothing can reach it** as a known gap, but report any concrete reachable seam that contradicts that claim.

Investigate material not-demonstrated fixes with a focused meaningful test. Prefer the coder’s pre-fix reproduction or an isolated disposable checkout/copy supplied by the lead with a trustworthy toolchain. Observe the claimed assertion fail without the fix and pass with it; record baseline/revisions and result. Do not revert shared story source, run a probe in a source tree served by a live watch server, install dependencies, or add coordination machinery. If isolation is unavailable, report unverified evidence and why.

A green baseline test does not pin the fix: report the gap and add coverage where within scope. A runner/provisioning failure is **probe unrunnable**, not a test failure attributable to the coder. For prose, inspect the quoted passage and whether it answers the finding, independent of code runner availability.

Report each fix’s evidence as **trusted**, **probed** (outcome and any added test), or **inherited gap**. New tests that were only observed green are not demonstrated regression tests. For unexplained failures in a live browser/device run, investigate possible source changes; a later green run alone does not prove flakiness or hot-reload contamination.

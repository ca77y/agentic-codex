### Make packaged refresh-proof checks repeatable

**Area:** flow

**Observed:** QA had to recreate the packaged no-Git refresh-proof mutation matrix
manually across several rounds to check truncated, malformed, duplicate, stale-path,
wrong-hash, and tampered-content cases.

**Suggested change:** Add a small standard-library regression suite beside the
engineering subagent installer that builds an isolated packaged copy and exercises
the valid proof plus each rejected mutation.

# Readiness and advice

Read the whole artifact and enough code/docs/product context to assess scope and intent. Check clarity, observable requirements, missing assumptions, duplication, contradictions, stale references, and excessive complexity. Prefer a concrete simplification over another rule or abstraction.

For card-backed specs, before semantic grading compare the `AC1`…`ACn` transcription with the card’s acceptance section through the read binding. Preserve wording and order; normalize only the binding’s known formatting-only rewrites (for Linear, bullet `-`/`*` and angle-wrapped bare URLs). Mismatch or unavailable comparison blocks readiness; route to the writer, not implementation. Retain transcription even when all criteria need work.

Every criterion needs a requirement/scenario, verified Already satisfied entry, or explicit non-coder owning mechanism and timing with a task. Requirements outside criteria must be marked deliberate scope. Open each Already satisfied file/region and verify the exact criterion; missing/nonspecific evidence blocks readiness. Docs-owned work must precede final acceptance. Every scenario must be reachable within Boundary and detect the required change, using inspection for documents and appropriate tests for code.

Dependency mechanisms need installed-version source citations or explicit assumptions. Alternative causes for an observable result must be addressed by direct mechanism observation or declared citation/assumption coverage. A design contradicting a criterion is a readiness finding; do not quietly narrow the criterion.

With search access, check board duplicates/clashes independently. If search is absent/unbound, report the sweep not run. For advisor proposals without a spec transcription, judge the proposal’s own criteria and product evidence; do not demand a build spec from the analyst.

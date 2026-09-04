# researcher — fan-out

Loaded on demand by `ca77y-library:researcher` when the topic genuinely divides into independent subquestions, or when it was dispatched as a child by a parent researcher. Everything here binds exactly as if it were written in the role skill, alongside the skill's own rules, which keep binding.

The step numbers below are the role skill's workflow steps; *You do the research yourself* and *Evidence discipline* are its sections. The same mechanics apply when step 4 fans out on two or more independent lead clusters mid-dive: those children are dispatched, run, and return exactly as the subquestion children here.

## Step 3 — decompose complex topics (fan-out)

- Spawn one `ca77y_library_researcher` custom subagent per independent subquestion as a parallel batch, using the model, effort, and context settings from the parent skill and naming `references/researcher-fanout.md` in each self-contained task. Respect the collaboration slot limit: dispatch only the children that fit, then run any remainder in a later batch. Each child runs steps 2, 4, and 5 and returns its synthesis, cited evidence, raw-note paths, any payload it could not persist, absence labels with their queries, and fallback-used notes.
- **Step 6's label rules bind every tier that synthesizes subordinate findings** — *(parent only)* scopes only the wiki write and shared-meta updates. A child that fanned out applies the carry-through and no-silent-upgrade rule to what it returns upward, and forwards its children's un-indexed raw-note paths with its own, so the top parent's set is complete across every tier.
- Run independent subquestions in parallel; sequence only where one depends on another's findings. If nested dispatch is unavailable, research the subquestions sequentially yourself. You own the final synthesis and the single wiki write (step 6).

## Step 5 — what a child persists and returns

- A child never dispatches a full-ingest `scribe`: raw-note-only mode keeps it off the wiki page and shared meta files, which the parent writes once. If no collaboration slot is available for a raw-note-only `scribe`, the child returns the complete raw-note payload and provenance; the parent persists it through a serialized `scribe` after the child batch completes. It returns every path left un-indexed.

## Step 6 — synthesize and write once (parent only)

Step 6 is **parent only**: a child returns its synthesis, evidence, labels, and un-indexed raw-note paths upward and never writes the wiki entry or the shared meta files.

- **Carry every subordinate's absence labels through unchanged.** Promote `unretrieved, not absent` to `confirmed absent` only by re-running **that subordinate's actual subject query** (the one returned with the label, else the subquestion you dispatched) — **not** a control term — on a path your own control query proved healthy, relabelling from *that* result; a healthy control alone never promotes. Anything you cannot re-run stays `unretrieved, not absent` and surfaces in your report.
- The wiki write and the shared-meta updates happen **once, serialized at the parent**.

# Spec pass

Read the prompt, the card and linked material through granted bindings, relevant code, and nearby docs. Follow the project’s spec format and lifecycle; if none is supplied, use the schema below in a clearly named specs directory. With no card/declaration, state that the prompt is the standard. Do not invent a tracker or product principles.

## Schema

1. **Metadata:** title, task/card identity and read state, then Coding complexity after drafting.
2. **Goal:** intended outcome.
3. **Acceptance criteria:** when a card exists, transcribe its acceptance section verbatim in order as `AC1`…`ACn`, after any authorized correction. Always retain this transcription, even when every criterion needs work. Explain that the auditor compares it with the card to detect drift; a paraphrase is not the standard.
4. **Design:** chosen approach, Boundary with changed artifacts and test scope, validation consumers, and any Coordination or Deviations.
5. **Requirements:** map each criterion needing work to runnable WHEN/THEN scenarios with observable outcomes. Map deliberate additional scope explicitly.
6. **Tasks:** implementation and evidence tasks, with a named owner and pipeline timing for anything the coder cannot close, including docs or manual reproduction. Docs-owned criteria close before final acceptance.
7. **Already satisfied criteria:** omit only this section when empty. Per `ACn`, name existing files, stable heading/quoted region, supporting commit if available, the concrete post-build observation QA repeats, and whether this task touches that surface. Anything requiring a change belongs in Requirements.

Score **Coding complexity** 1–10 with one sentence naming the driving factors: surface area, blast radius, novelty, dependency/API reasoning, unknowns. Score the scoped work, including document work, after Requirements and Tasks. The lead routes below 5 to junior-coder, otherwise senior-coder.

## Scenarios and validation

Every scenario must run within Boundary. Scope the owning test infrastructure or state precisely which wrapper is inspection-only. For a document, write “the deliverable is a non-code artifact: `<what>`”; each THEN names an observation in that artifact. Match evidence to each changed artifact in mixed tasks. A repository’s unrelated test runner does not turn prose assertions into code tests.

Check each scenario against today’s tree: if it already passes, move a wholly satisfied criterion to Already satisfied, or rewrite the scenario to detect the required change. Promote behavioral claims from Design/Deviations to scenarios, or mark them untested-by-design with a reason. If another mechanism could yield the outcome, identify that alternative and directly observe the claimed mechanism, or explicitly rely on its citation/assumption.

Validation reaches actual consumers: changed build/config files or files named by Docker/compose/CI require checks through those consumers; document changes reach their manifests, frontmatter, loaders, and changed-file set. Include a definition file’s frontmatter description among edit sites if the change falsifies it; otherwise record it checked. Name an owner for all non-coder tasks, then sweep every criterion for missing ownership.

Only when dependency behavior, absent capabilities, or baseline-based exclusions matter, read `writer-evidence.md`.

## Corrections and coordination

When revising, state the general property behind the finding and enumerate its instances across the spec. Search the whole spec for superseded decisions, including negations and identifiers; reconcile Goal, Design, Boundary, Deviations, scenarios, Validation and Tasks in the same pass. Report any unresolved instance.

Never silently narrow an unsatisfiable card criterion. Record its exact sentence, reasoned proposed override, and follow-up in Deviations. Correct the card only with both dispatch and declaration write authority, before implementation; otherwise report the needed correction for the lead to settle before readiness. The transcription still matches the card as read.

With search access, check sibling cards for duplication and contradictory coordination/dependency prose, including the source card. For shared infrastructure additions, record “if <sibling> lands first, detect and reuse <infrastructure>.” Report both sides of stale relationships with sentence and correction; apply only authorized corrections that preserve the story’s purpose. If search is unavailable, report these sweeps **not run**.

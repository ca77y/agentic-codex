# Report 1: Streamline the existing ca77y system

Review date: 2026-09-05. Baseline: `master` at `30562c84126a126437e5713f1e41e37498f278d9`, fetched and fast-forwarded from `origin/master`. Scope: both plugins, all eight skills, all eight leaf-agent manuals, their references, nine agent resource definitions, both installers, manifests, README, and project declarations. This is a static workflow and packaging review; no delivery pipeline or research benchmark was executed.

**Recommendation: repair the workflow contracts first, then shorten the instructions.** The useful core is already present: explicit write authority, independent checks, scoped worktrees, evidence-based findings, and research provenance. Much of the surrounding complexity comes from repeating those contracts and accumulating special cases in prose. Keep the current roles and public commands for this cleanup; evaluate structural changes separately in [Report 2](/Users/catty/Workspace/agentic-codex/docs/reports/2026-09-05-codex-redesign.md).

## 1. What the current content costs

Counts use whitespace-separated words, not model tokens. Templates, generated installed copies, README, and project declarations are excluded from the authored-content totals.

| Surface | Engineering | Library |
|---|---:|---:|
| Discoverable skills | 5 | 3 |
| Leaf-agent manuals | 5 | 3 |
| Custom-agent resource definitions | 5 | 4 |
| Words in skills and agent manuals | 19,600 | 5,656 |
| Words in role references | 8,500 | 1,080 |

There are **34,836 authored instruction words** across those manuals and references. They are distributed across contexts, not loaded together. The library's ninth combined agent is a researcher compiled from the researcher skill, rather than a ninth leaf manual.

The engineering happy path spawns six workers: spec writer, readiness auditor, coder, QA, acceptance auditor, and documentation writer. Their compiled instructions total approximately **18,003 words across those six contexts**, before project instructions, source files, task prompts, tool output, or retries. The main session also reads the 5,729-word lead skill. These are instruction-volume measurements, not billable-token or latency estimates.

| Compiled role | Instruction words per spawn |
|---|---:|
| Writer | 4,484 |
| Auditor | 2,351 |
| Either coder | 2,444 |
| QA | 1,889 |
| Researcher | 2,608 |
| Scribe | 1,751 |
| Clerk | 785 |
| Librarian | 427 |

Two especially clear maintenance opportunities:

- The junior and senior coder manuals are byte-identical; their fix-round references are also identical. Their difference is model routing, not operating procedure.
- The same 93-word process-feedback paragraph appears 11 times. Five engineering workers repeat the same preservation and attribution rules, alongside near-identical worktree instructions.

## 2. Fix these contracts before cutting prose

These findings follow explicit paths through the instructions. Their consequences have not been measured in live runs.

| Priority | Evidence and concrete trigger | Recommended correction |
|---|---|---|
| High | The [docs pass](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/agents/writer/references/writer-docs-pass.md) removes the spec. The [open-PR fix procedure](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/skills/lead/references/open-pr-fix-run.md) then requires a spec path and reads its complexity score, but gives no explicit restoration procedure. A normal post-ship review can therefore lack its required input. | Recover the spec from its recorded commit into ignored run state, preserving the historical version. For changed scope, create and gate a new revision. State how fix-only work obtains provisioning status as well; that recovery procedure currently requests the status without explicitly establishing it. |
| High | [Lead steps 6–8](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/skills/lead/SKILL.md:132) put the last acceptance gate before docs and allow ship-time fixes afterwards. [Writer rules](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/agents/writer/AGENT.md) explicitly allow criteria owned by the later docs pass. | Define evidence invalidation: docs-owned criteria are checked after docs; subsequent behavioral changes return through affected QA and acceptance checks. A gate only covers the artifact revision it inspected. Keep the existing agents, but remove the claim that acceptance is unconditionally the last gate. |
| High | The [three-attempt rule](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/skills/lead/SKILL.md:154) says stop without shipping; [ship-time validation](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/skills/lead/SKILL.md:162) says a surviving failure is named in the PR description and then proceeds to commit/push. | Use one outcome table: resolved → continue; unverified → state limitation and apply the declared release policy; surviving blocking defect → stop before publication. Remove the conflicting continuation sentence. |
| High | The [writer](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/agents/writer/AGENT.md:44) says “Drop the section, like the transcription, when every criterion needs work.” The auditor requires that transcription whenever a card supplies criteria. | Drop only the empty Already satisfied section. Retain the transcription for every card-backed spec. Add a fixture where all criteria require implementation. |
| Medium | The [lead introduction](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/skills/lead/SKILL.md:6) says code review runs on the PR, “never as a local gate”; step 5 and [QA step 6](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/agents/qa/AGENT.md) explicitly gate a local diff review. | Name the actual distinction: local QA review plus separately configured PR review. If both stay, explain their distinct purpose once. |
| Medium | [Acceptance rules](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/agents/auditor/references/auditor-acceptance-gate.md) mark a conditional criterion met when its antecedent simply did not arise in this run. An unexercised failure path can receive a passing label. | Distinguish evidence proving the conditional behavior from a run that never exercised it. Report the latter as unverified unless other evidence establishes it. This changes grading policy and should be explicit. |
| Medium | [Writer baseline rules](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/agents/writer/AGENT.md:58) place failing baseline files “in scope by definition,” whereas lead rules generally relay unrelated pre-existing failures. | Require a causal connection to the requested outcome before adding scope. Record unrelated baseline failures without silently expanding the task. |
| Medium | [Docs authoring](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/agents/writer/references/writer-docs-pass.md) treats the diff as authoritative for shipped behavior. A diff alone omits unchanged implementations, configuration, and callers. | Inspect the resulting tree for behavior; use the diff to locate changes and commits to explain intent. Never turn a regression into correct documentation merely because it appears in the diff. |

Also resolve the deliberately unusual `mis-worded` contract. The auditor returns **not ready**, while lead explicitly proceeds to a PR. This is a documented exception, not an accidental contradiction. Preserve its intent as a distinct **handoff with unresolved acceptance wording** state, visibly different from accepted work. Do not describe it as an ordinary passed gate.

## 3. Clean up every skill and agent surface

| Surface | Keep | Simplify |
|---|---|---|
| `lead` | Ownership, write authority, worker targets, recoverable state, explicit blocker handling | Keep a short main flow and one transition table. Move workspace setup, validation attribution, and final-output details into narrowly loaded references. Eliminate repeated explanations of why each exception exists. |
| `analyst` | Product fit, observable acceptance, current board reconciliation | Keep the six fit dimensions in one evidence table. Separate unresolved product decisions from unavailable documentation. Missing optional docs should yield stated assumptions or draft proposals, not require an invented vision before any story can exist. |
| `board` and `forge` | Independent project declarations; verified bindings; no guessed remote writes | Retain short entry points and authoring templates. Remove repeated interviews and “invoke again” instructions when the current request already authorizes completion. Read-only inspection must not enter the authoring interview. |
| Both install skills | Ownership markers, collision refusal, stale-managed-file handling | Expose source validation, installed-parity checking, and installation as distinct operations. State the Python 3.11+ requirement implied by `tomllib`. |
| `bootstrap` | Non-overwriting scaffold, optional Obsidian support | Infer the project name from existing files, permit an empty initial taxonomy, and bundle genuinely necessary questions. Domain description and optional UI configuration need not create several sequential pauses. |
| `researcher` | Library-first retrieval, primary sources, eager provenance, serialized shared writes | Add a decision-based stopping rule: answer the requested questions, resolve material contradictions, and report remaining retrieval limits. “Every lead” and “until provably unanswerable” are open-ended. Batch raw-note persistence instead of spawning a scribe for each valuable finding. |
| Writer | Buildable requirements, scope reconciliation, docs matching the final product | Make spec mode and docs mode explicit inputs. Remove the unconditional “project is an Obsidian vault” assumption from engineering. Replace long prose about section relationships with a compact spec schema and examples. |
| Junior/senior coders | Scoped implementation, meaningful evidence, production-hazard reporting | Maintain one authoritative coder procedure and derive both role artifacts from it. Keep current agent names and routing for compatibility. |
| QA | Independent validation and missing coverage | Separate standard verification from expensive regression-sensitivity probes. Prefer test-first reproduction or an isolated disposable checkout over repeatedly reverting source served to browsers. Preserve the new live-server exclusion until an alternative is implemented and verified. |
| Auditor | Independent acceptance and concrete evidence | Use one verdict contract with mode-specific checklists. Move exact criterion comparison to a deterministic helper; keep semantic acceptance with the agent. |
| Librarian | Small, focused retrieval procedure | Keep mostly as-is. Remove unrelated process-feedback writing from a read-oriented role. |
| Scribe | Provenance preservation and single ownership of shared metadata | Turn repeated frontmatter, link, anchor, and taxonomy checks into one validator. Renumber ingestion in its actual execution order; it currently says step 3 precedes step 2. |
| Clerk | Semantic citation and library-quality judgment | Consume mechanical-validator findings and spend agent attention on contradictory evidence, weak synthesis, and genuine duplication. Default to changed files plus affected references, with a full-vault audit when requested. |

Repair stale portability assumptions too: the docs-pass reference names `docs/ARCHITECTURE.md`, which this repo does not contain; bootstrap mentions an `init` skill that these plugins do not ship; clerk cites numbered convention sections that do not match the bundled librarian guide. The [research evidence reference](/Users/catty/Workspace/agentic-codex/plugins/ca77y-library/skills/researcher/references/researcher-evidence.md) hardcodes transient provider behavior and calls a healthy-but-empty search “confirmed absent.” Replace that label with “no results on a working search path”; it does not prove absence. Respect the project's required search provider when choosing any fallback.

## 4. Deduplicate without hiding required instructions

The [installer compiler](/Users/catty/Workspace/agentic-codex/plugins/ca77y-engineering/skills/install-subagents/scripts/install_agents.py) recursively embeds every Markdown reference beside a manual. Consequently, moving a paragraph into a worker reference reduces neither that worker's initial context nor its compiled instruction size.

Use two distinct techniques:

1. **Shared source for maintenance.** Keep a short shared contract for worktree ownership, reporting, and authority. Compile it into each worker once. This eliminates multiple editable copies but does not itself reduce runtime context. Keep role-specific references beside their owner as repository rules require. Generate duplicate coder artifacts from one canonical source, and verify parity.
2. **Actual conditional loading for context.** To make rare procedures genuinely lazy, the installer must copy them to a stable managed location and emit resolvable pointers, or produce separate mode-specific definitions. Never point installed agents at an ephemeral plugin cache and assume it survives upgrades. This is an installer change, not a Markdown rearrangement.

The installers differ in only three lines identifying the plugin. Maintain one canonical implementation with packaging-time copies and a parity check, so each plugin remains independently installable. Avoid a runtime dependency from one plugin's installer into the other plugin's directory.

Move process feedback into worker reports and let the coordinator write one deduplicated entry. The existing paragraph both adds roughly 1,000 repeated words and creates a shared writable file for otherwise isolated agents. In library raw-note-only mode it also conflicts with the instruction to write only raw notes.

## 5. Add small checks where prose currently acts as a program

Good candidates are criterion normalization/comparison, source-to-installed-agent parity, duplicate generated-artifact detection, frontmatter parsing, internal-link resolution, and explicit run-state validation. Keep product fit, evidence quality, scope judgment, and release decisions in instructions.

Do not make the first cleanup a general workflow engine. Start with checks that produce a short result and actionable file references. Add behavioral fixtures for the important branches:

- Card-backed work where all criteria need implementation; trackerless work; absent forge declaration.
- Acceptance containing documentation; a behavior change after a passing audit.
- A third unresolved blocker; the explicit wording-escalation exception.
- Review repair after spec deletion and after worktree loss.
- Unrunnable dependencies; concurrent edits and a live browser server during a probe.
- Raw-note-only persistence and unavailable search.

These exercise failure modes; simple word-presence tests would only mirror the instructions.

## 6. Delivery order and expected benefits

1. **Correctness patch:** settle the contract gaps and stale references; preserve roles and public names. Highest benefit is predictable behavior, even before shortening anything.
2. **Content cleanup:** remove duplicate source, standardize outputs, centralize transitions, and shorten the main lead/writer procedures. Use an initial editorial target of 25–35% fewer authored words, measured against 34,836; this is a target, not a proven saving.
3. **Packaging and deterministic checks:** add installed parity and shared-source checks, then conditional reference loading if measurements justify it.
4. **Evaluate:** replay representative tasks and compare completion quality, pauses, repeated checks, wall time, and actual token use. Accept fewer instructions only if protection against the fixture failures remains.

The cleanup should primarily reduce maintenance effort, contradictory interpretation, and repeated reading. It will leave the six-worker happy path in place, so do not expect it to remove most orchestration latency. That requires the redesign.

## Verification and local installation finding

All eight skill quick validators passed. Both plugin validators passed. Both installer `--check` runs passed, covering five engineering and four library custom agents. These checks establish packaging validity, not workflow correctness.

A read-only comparison of compiled source with `~/.codex/agents/` found all five engineering agents differ in their actual instructions; they lack recent preservation/attribution guidance, and QA also lacks the fetched live-server exclusion. All four library agents match. Fetching source does not update installed agents. Add a read-only parity command so this is visible during normal upgrades. No installed definitions were changed by this review.

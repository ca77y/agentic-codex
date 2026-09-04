---
task: SMR-303
card: https://linear.app/ca77y/issue/SMR-303/name-concurrent-workers-files-in-each-dispatch-and-forbid-reverting-a
card_state_read: In Progress (2026-09-04)
Coding complexity: 5 — One orchestrator and five installed custom-agent manuals must adopt a shared dispatch contract and preservation rule; the behavior crosses every pipeline role, though it uses established Markdown and installer patterns and has no unresolved external dependency.
---

# Preserve deliberate edits in a shared story worktree

## Goal

Make a shared-worktree dispatch safe by having the lead either identify every live
worker's expected file edits to each new worker or sequence the work. Give every
engineering worker the same rule for an unexplained modification: preserve it or
report it, and verify a tool-attribution claim before recording it as fact.

## Acceptance criteria (verbatim transcription)

This checked copy transcribes SMR-303's acceptance criteria rather than paraphrasing
them, so the auditor can mechanically prove it has not drifted from the card. The
Linear card was read in `In Progress` on 2026-09-04.

- AC1: When the `lead` dispatches concurrent workers into one worktree, each dispatch names the files the other live worker is expected to modify — or the dispatches are sequenced instead.
- AC2: Every worker is told that an unexplained modification in a shared worktree is not self-evidently spurious: report it or leave it, never `git checkout --` a file you did not write. The `writer`'s existing rule about the improvements log is generalised to any path in the tree, since the reasoning is not special to that file.
- AC3: A diagnosis that a tool mutated a file is verified against that tool's actual behaviour before it is recorded as fact.
- AC4: Nothing in the change makes a worker responsible for detecting concurrency it was not told about.

## Design

### Boundary

The deliverable is a non-code artifact: the engineering lead's dispatch procedure and
the five engineering custom-agent operating manuals.

The migrated tree provides these canonical sources, which the existing
install-subagents loader compiles into the installed custom-agent TOML files:

- `plugins/ca77y-engineering/agents/writer/AGENT.md`
- `plugins/ca77y-engineering/agents/auditor/AGENT.md`
- `plugins/ca77y-engineering/agents/junior-coder/AGENT.md`
- `plugins/ca77y-engineering/agents/senior-coder/AGENT.md`
- `plugins/ca77y-engineering/agents/qa/AGENT.md`
- `plugins/ca77y-engineering/skills/install-subagents/scripts/install_agents.py`

In scope is the dispatch contract in
`plugins/ca77y-engineering/skills/lead/SKILL.md` and the shared-worktree preservation
and diagnosis rule in every listed `AGENT.md`. The manuals have no YAML frontmatter.
Their five managed resource TOMLs' `description` fields were checked and describe the
roles, not this internal preservation policy, so they remain unchanged. This temporary
task spec remains in `docs/specs/` until the docs pass converts and removes it.

Measured baseline: at HEAD `f29c0a9`, the installer resources resolve the five listed
`AGENT.md` files and compile their manuals into each installed custom-agent TOML. The
lead skill is not a leaf manual and remains the canonical in-scope orchestrator skill.

Do not change the migration itself, the custom-agent names or resource metadata, the
installer's compilation behavior, the board or forge declarations, the role-specific
work flows, or a worker's existing narrowly owned temporary revert used to demonstrate
its own fix. The preservation rule covers a change the worker did not author and cannot
attribute, not a controlled temporary edit that the manual already scopes and restores.

Measured baseline: `README.md` and `AGENTS.md` define the skill quick-validator and
the two plugin validators, but define no format or lint command. The documented
commands are therefore the validation floor for this document artifact; no effective
configuration renderer exists for a separate format/lint baseline.

### Concurrent-dispatch contract

Before the lead starts or resumes work that would overlap another live worker in the
same story worktree, it records the expected edit paths for every live worker. Each
dispatch includes a concrete shared-worktree notice: the role and expected paths of
every other live worker, or an explicit statement that no other worker will touch the
worktree while this dispatch runs. Expected paths are the planned ownership set, not a
claim that a worker has already changed them.

If the lead cannot name the other worker's expected paths, it waits for that worker to
finish before dispatching the next one. It does not delegate discovery of concurrent
workers to a worker. A worker receives only the notice in its own dispatch and acts on
it; it has no duty to inspect the coordinator's ledger, process list, or worktree status
to infer unannounced concurrency.

The contract applies to both a fresh `spawn_agent` dispatch and a resumed
`followup_task` dispatch. It complements the existing one-coder-at-a-time rule and
only governs overlap the lead deliberately creates, such as a writer docs pass and a
coder working simultaneously.

### Preservation and attribution rule

Each of the five worker manuals must state the same general rule for the whole story
worktree. When a worker sees a modification it did not write and cannot explain from
its assigned work, the modification may be another live worker's deliberate work.
The worker leaves it in place or reports it to the lead; it never uses `git checkout
--`, `git restore`, `git clean`, or an equivalent revert to remove or overwrite that
unexplained change. The rule applies to every path, including
`docs/AGENTS_IMPROVEMENTS.md`, rather than treating the improvements log as a special
case.

A worker may say that a tool changed a file only after verifying that tool's actual
behavior through its local source, its installed implementation, or a controlled
observation that does not alter the shared story worktree. Until then it reports the
cause as unknown or possible, and does not record an improvement entry or final report
as though the attribution were established. This requirement deliberately does not make
workers detect an unannounced concurrent worker; it only gives them the safe response
when a change is unexplained.

The worker-manual passages are the mechanisms under test. A nearby generic prohibition
on reverting another agent's change is insufficient if it does not cover the observed
case where the worker cannot identify the author, and an outcome where the modification
survives is insufficient if the manual still permits an unverified tool diagnosis.

### Coordination

SMR-151 is related but governs collisions between separate concurrent stories and the
durable re-homing of deferred shared-document edits. SMR-303 governs concurrent workers
within one story worktree before a change is lost. The two cards do not make conflicting
claims, so no board correction is needed.

The board search for `shared worktree`, `concurrent workers`, and `dispatch` found
SMR-311 and SMR-312 as active adjacent dispatch-lifecycle stories. Neither claims this
lead/worker file-ownership disclosure or preservation contract, so neither card needs a
relationship correction. No shared test or runtime infrastructure is introduced.

### Validation

Open the changed lead skill and each of the five changed `AGENT.md` files. Confirm the
exact passages in R1–R4, and confirm the five managed resource descriptions remain
unchanged because they do not state the new preservation policy.

Run the installer check, which loads each worker manual through the distributed
custom-agent resource and rejects missing or invalid compiled agent definitions:

```sh
python3 /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-303-name-concurrent-workers-files-in-each-dispatch-and-forbid/plugins/ca77y-engineering/skills/install-subagents/scripts/install_agents.py --check
```

Run the repository's required quick validator for every current skill directory and
both plugin validators. The quick validator covers the changed lead skill and the
plugin validators check the engineering manifest, packaged skills, and resource
structure that loads the changed manuals. The library plugin validator remains part of
the repository-wide validation floor:

```sh
for smr303_skill_dir in \
  /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-303-name-concurrent-workers-files-in-each-dispatch-and-forbid/plugins/ca77y-engineering/skills/* \
  /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-303-name-concurrent-workers-files-in-each-dispatch-and-forbid/plugins/ca77y-library/skills/*; do
  python3 /Users/catty/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$smr303_skill_dir"
done
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-303-name-concurrent-workers-files-in-each-dispatch-and-forbid/plugins/ca77y-engineering
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-303-name-concurrent-workers-files-in-each-dispatch-and-forbid/plugins/ca77y-library
```

No format or lint command is defined, as recorded in the measured baseline. The
inspections provide the semantic assertions; the installer and validators prove the
changed manuals remain loadable through their consumers.

## Requirements

### R1 — Identify live workers' expected edits before an overlapping dispatch

Maps to: AC1, AC4.

**WHEN** the lead creates a `spawn_agent` or `followup_task` dispatch that will overlap
another live worker in the same story worktree

**THEN** the changed lead skill requires that dispatch to name each other live worker's
role and expected edit paths, and requires sequencing if the lead cannot name them;
it visibly keeps responsibility for detecting and deciding that overlap with the lead.

An ordinary one-at-a-time pipeline step cannot establish this mechanism, so the
inspection must read the lead's rule that governs an overlapping dispatch directly.

### R2 — Preserve a modification of unknown origin

Maps to: AC2, AC4.

**WHEN** a reader opens the shared-worktree rule in each of the writer, auditor,
junior-coder, senior-coder, and QA manuals

**THEN** every manual says a modification the worker did not write and cannot explain
may be deliberate concurrent work; tells the worker to leave it or report it; forbids
`git checkout --` and equivalent removal or overwrite of the change; and applies the
rule to all paths, including the improvements log, without imposing a duty to discover
unannounced concurrency.

The named five manuals are each independently inspected because a rule in the lead or
one sibling manual cannot prevent a differently dispatched worker from reverting the
file.

### R3 — Verify an attribution before reporting it as fact

Maps to: AC3.

**WHEN** a reader opens the same shared-worktree rule in each of the five worker
manuals

**THEN** every manual requires a claim that a tool changed a file to be verified against
the tool's local or installed implementation or a controlled observation outside the
shared worktree, and requires an unverified cause to be reported as unknown or
possible rather than recorded as fact.

The direct-manual observation distinguishes this mechanism from a coincidental clean
worktree: a preserved modification alone would not show whether a worker was still
licensed to blame an unverified tool.

### R4 — Preserve existing owned temporary-revert workflows

Maps to: AC2.

**WHEN** a reader compares the new preservation rule with the coder and QA manuals'
existing scoped demonstration or probe procedure

**THEN** the preservation rule governs only a change the worker did not author and
cannot explain, while the existing procedure may still make and restore its own
explicitly scoped temporary change.

This direct comparison prevents an overbroad wording from disabling the restoration
mechanism that those manuals already require.

## Tasks

- [ ] **Coder:** update `plugins/ca77y-engineering/skills/lead/SKILL.md` with the
  concurrent-dispatch contract in R1, applying it to fresh and resumed dispatches and
  preserving the lead's ownership of concurrency detection.
- [ ] **Coder:** add the R2 and R3 shared-worktree rule to each of the five canonical
  engineering `AGENT.md` manuals; preserve the managed resource descriptions because
  none states behavior the new rule falsifies.
- [ ] **Coder:** retain the coder and QA manuals' existing temporary owned-revert
  workflow while making the general preservation rule apply to an unexplained change
  from any path.
- [ ] **QA:** perform the R1–R4 document inspections and the installer, all-skill
  quick-validator, and both plugin-validator checks in Validation; report a missing
  manual, lost consumer, or divergent worker wording as the affected AC finding.
- [ ] **Writer docs pass, not the coder:** reconcile the shipped dispatch and worker
  behavior with durable engineering documentation if the shipped diff changes a
  reader-facing workflow, then convert and remove this spec from `docs/specs/`.

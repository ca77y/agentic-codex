---
task: SMR-200
card: https://linear.app/ca77y/issue/SMR-200/state-the-writers-spec-pass-board-access-includes-whatever-card
card_state_read: In Review (2026-08-31)
Coding complexity: 4 — The change reconciles a phase-sensitive authority policy across two role manuals, the board declaration contract and template, and the current declaration; it has no external dependency but repo-local visibility is a high-consequence boundary.
---

# State the writer's spec-pass board access

## Goal

Make the Codex-native engineering pipeline unambiguous about a writer's board
authority: the initial pre-build spec pass receives the declaration's explicit
writer card-content grant, while every later respec remains read/search-only unless
the declaration separately grants that later phase. Make the declaration name that
grant and define the only safe visibility route for a repo-local correction.

## Acceptance criteria (verbatim transcription)

This checked copy transcribes SMR-200's acceptance criteria rather than
paraphrasing them so the auditor can mechanically prove it has not drifted from the
card. The Linear card was read in `In Review` on 2026-08-31.

- AC1: The writer's fixed spec-pass access is stated as read, search, and whatever card-content authority the tracking declaration grants the writer — one clause in the same sentence that fixes read and search.
- AC2: The `lead` skill's restatement of the writer's grant is edited to agree.
- AC3: The caller-granted default-deny is unchanged for every other dispatch; this applies only to the spec pass, the one window `docs/BOARD.md` names as legal for a criterion correction.

## Design

### Boundary

The deliverable is a non-code artifact: the engineering role procedures and the
board-declaration contract that supplies their authority.

In scope:

- `plugins/ca77y-engineering/skills/writer/SKILL.md`, including its fixed
  spec-pass access clause and the repository-root rule it must qualify for a
  repo-local card correction.
- `plugins/ca77y-engineering/skills/lead/SKILL.md`, including its matching
  worker-access restatement and the root-checkout visibility exception it owns.
- `plugins/ca77y-engineering/skills/board/SKILL.md` and
  `plugins/ca77y-engineering/skills/board/references/authoring-board.md`, so a
  board declaration must state the writer-specific grant, its phase, and any
  repo-local execution route rather than leave them implicit in pipeline-wide
  authority.
- `docs/BOARD.md`, the current declaration, to supply that explicit grant for this
  project and continue binding Linear as the correction surface.
- This temporary task spec under `docs/specs/` until the docs pass converts and
  removes it.

The YAML `description` fields in the three affected `SKILL.md` definition files were
checked. None describes writer card-content authority or the board-declaration
contract, so their descriptions do not change.

Out of scope are custom-agent TOML resources, other role skills, a card mutation in
this post-build respec, and any change to the card's acceptance criteria.

Measured baseline: at `e3dadffb95d75e0fcfeef7c24fc987e963b52682`, the writer and
lead grant the declaration's authority in **every** spec pass; the board declaration
and its authoring template state only pipeline-level write authority; and the common
worktree rule permits the repository root to be read but not written. The loaded
artifacts have no generated form: the engineering plugin manifest loads `./skills/`.

### Authority phases and declaration contract

The policy decision is that a **writer card-content authority** is an explicit
declaration grant with two independent dimensions: the exact card fields it permits
and the phase in which it applies. The standard initial phase is the first,
pre-build spec pass. It is the only default phase that may correct a criterion. A
post-build respec after QA, acceptance, or PR review has read and search only unless
the declaration explicitly names authority for that later phase; a broad
pipeline-level `update` capability is not a substitute for either grant.

Amend the board skill and its declaration template so every declaration says whether
the writer has card-content authority, names the allowed fields, limits it to the
initial pre-build spec pass by default, and says whether any later respec has a
separate grant. `docs/BOARD.md` must follow that contract. Its current Linear grant
allows the initial writer spec pass to correct the card's description, acceptance
criteria, labels, priority, and relations; it grants no later-respec mutation.

### Repo-local correction visibility

For a hosted board, the writer applies an authorised initial-pass correction through
the declaration's bound update call. For a repo-local board whose visibility rule
requires the repository root checkout, the writer may write only the named card in
that root checkout, on its base branch, uncommitted and without checking the story
branch out there. This narrowly overrides the normal writer root-read-only rule only
for an initial-pass correction the declaration explicitly grants. The lead's
root-checkout visibility exception must state the same route, so the root write is
neither declined nor put in the story worktree. A later respec has no such exception
unless its declaration explicitly grants that later phase.

### Access wording

Amend the writer's fixed access sentence so its one clause still says the access is
read and search plus whatever card-content authority the tracking declaration grants
the writer, while identifying the **initial pre-build spec pass** as the phase in
which that authority applies. The same passage must reserve later respecs to
read/search-only absent an explicit later-phase grant and retain the established
default and sibling-sweep rationale.

Amend the lead's worker-access restatement to mirror that phase boundary and the
declaration's writer-specific grant. Leave its separate auditor, coder, and QA grants
unchanged. The writer's caller-granted paragraph continues to govern every other
dispatch, including an absent declaration or unbound operation.

The fixed access clauses and the declaration's explicit grant are the mechanisms
under test. A nearby generic statement that the pipeline may update a card would not
satisfy this design if it leaves the writer, fields, phase, or repo-local execution
surface implicit.

### Coordination

The declared Linear sibling sweep searched `writer board access card correction`,
`repo-local board writer correction`, `writer card-content authority`, and
`post-build respec`. It found the source story and completed foundation work such as
SMR-188, but no independent active story that changes this authority boundary. No
shared infrastructure or card relationship needs a coordination note.

## Requirements

### R1 — State the writer's phase-bounded full grant (AC1)

**WHEN** a reader opens the fixed spec-pass board-access sentence in
`plugins/ca77y-engineering/skills/writer/SKILL.md`,
**THEN** that one sentence states read, search, and whatever card-content authority
the tracking declaration grants the writer for the initial pre-build spec pass,
while retaining the established read-and-search default and sibling-sweep rationale.

### R2 — Keep the lead's grant in agreement (AC2)

**WHEN** a reader opens the worker-access restatement in
`plugins/ca77y-engineering/skills/lead/SKILL.md`,
**THEN** it gives the writer the same fixed access and initial-pass phase boundary,
and says a later respec remains read/search-only unless `docs/BOARD.md` explicitly
grants that later phase.

### R3 — Preserve default-deny and the correction window (AC3)

**WHEN** a reader compares the amended writer and lead passages with the
caller-granted paragraph and the board declaration,
**THEN** only an initial pre-build writer spec pass receives a declaration-granted
card-content correction window; the auditor's read/search or read-only grants and
the coder and QA's no-access grants remain as written.

### R4 — Make the declaration's writer grant explicit

**WHEN** a reader opens the board skill, its declaration template, and this
project's `docs/BOARD.md`,
**THEN** each names a writer-specific card-content grant (or its absence), the card
fields it covers, the initial pre-build phase, and any separately granted later
respec phase instead of relying on an undifferentiated pipeline `update` authority.

### R5 — Write a repo-local correction where it is visible

**WHEN** an initial pre-build writer spec pass has an explicitly authorised
repo-local card correction,
**THEN** the writer and lead procedures direct that one card write to the root
checkout's base branch, left uncommitted and outside the story worktree; a later
respec does not receive the exception without its own declared grant.

## Validation

- Open the three changed `SKILL.md` files, the board authoring template, and
  `docs/BOARD.md`. Confirm R1–R5 as document observations, including that the
  writer-specific grant has fields and phase and that neither later respecs nor
  non-writer dispatches inherit it.
- Run the repository's skill quick validator for every skill directory, including
  the changed `writer`, `lead`, and `board` directories, as required by `AGENTS.md`.
- Run `python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-engineering`
  and the same validator for `plugins/ca77y-library`. The engineering manifest's
  `skills: "./skills/"` loader consumes the changed definitions; validating both
  plugin roots preserves the repository's declared validation floor.

## Tasks

- [ ] Coder: amend the writer's fixed spec-pass clause and root-access rule to
  satisfy R1, R3, and R5 without broadening any post-build respec or other dispatch.
- [ ] Coder: amend the lead's matching worker-access and repo-local visibility
  passages to satisfy R2, R3, and R5, preserving its distinct auditor, coder, and QA
  grants.
- [ ] Coder: amend the board skill, its `authoring-board.md` contract/template, and
  this project's `docs/BOARD.md` to satisfy R4 and name the explicit initial-pass
  grant, fields, later-phase default, and repo-local route.
- [ ] Coder: preserve the checked YAML `description` fields in the affected
  `SKILL.md` files; none states the authority policy or board-contract behaviour.
- [ ] QA: perform the document observations and validator runs in **Validation**;
  report any implicit writer grant, phase leak, repo-local write outside the declared
  visibility surface, or unintended non-writer access as an AC1–AC3 finding.
- [ ] Writer docs pass (not the coder): convert the delivered policy clarification
  into durable engineering documentation if the shipped diff warrants it, then
  remove this spec from `docs/specs/`.

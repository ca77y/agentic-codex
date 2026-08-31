---
task: SMR-200
card: https://linear.app/ca77y/issue/SMR-200/state-the-writers-spec-pass-board-access-includes-whatever-card
card_state_read: In Progress (2026-08-31)
Coding complexity: 2 — Two adjacent Markdown skill manuals need one precise, established access-policy amendment; the plugin manifest already loads their directory and no external API or new pattern is involved.
---

# State the writer's spec-pass board access

## Goal

Make the Codex-native engineering pipeline unambiguous: during a writer's spec
pass, its fixed board access includes read, search, and the card-content authority
that the tracking declaration grants the writer. Preserve caller-granted,
default-deny access for every other dispatch.

## Acceptance criteria (verbatim transcription)

This checked copy transcribes SMR-200's acceptance criteria rather than
paraphrasing them so the auditor can mechanically prove it has not drifted from the
card. The Linear card was read in `In Progress` on 2026-08-31.

- AC1: The writer's fixed spec-pass access is stated as read, search, and whatever card-content authority the tracking declaration grants the writer — one clause in the same sentence that fixes read and search.
- AC2: The `lead` skill's restatement of the writer's grant is edited to agree.
- AC3: The caller-granted default-deny is unchanged for every other dispatch; this applies only to the spec pass, the one window `docs/BOARD.md` names as legal for a criterion correction.

## Design

### Boundary

The deliverable is a non-code artifact: the writer and lead operating procedures.

In scope:

- `plugins/ca77y-engineering/skills/writer/SKILL.md`, specifically its fixed
  spec-pass board-access sentence.
- `plugins/ca77y-engineering/skills/lead/SKILL.md`, specifically its matching
  worker-access restatement.
- This temporary task spec under `docs/specs/` until the docs pass converts and
  removes it.

The YAML `description` fields in both affected definition files were checked. Neither
description states the fixed board-access policy, so neither description changes in
this task.

Out of scope are changes to `docs/BOARD.md`, custom-agent TOML resources, other role
skills, and any further card mutation. During this spec pass, the writer corrects
SMR-200's migrated `docs/ISSUE_TRACKING.md` and legacy writer-path references to their
current `docs/BOARD.md` and `skills/writer/SKILL.md` forms. `docs/BOARD.md` is already
the authority for card-content writes and says they are permitted during the writer's
spec pass; this task otherwise only makes the two operating procedures convey that
authority consistently.

Measured baseline: at HEAD `2294764ccbcb6e3fee3eeb90465583740d02d338`, the source
artifacts that Codex loads directly state the writer's fixed access as only "read and
search" (`skills/writer/SKILL.md:12`; `skills/lead/SKILL.md:20`). The manifest at
`plugins/ca77y-engineering/.codex-plugin/plugin.json` loads `./skills/` and introduces
no generated or resolved form to inspect.

### Deviations from the card

The card originally stated AC3 with `docs/ISSUE_TRACKING.md`, a declaration that does
not exist in this Codex-native repository. The card's own *Agentic Codex migration*
section requires its replacement with `docs/BOARD.md`, so the writer corrected AC3
and the associated stale path references on SMR-200 before recording the checked
transcription. No later card correction is implied unless the tracking declaration's
write authority changes.

### Access wording

Amend the writer's fixed spec-pass sentence so its one access clause says the access
is "read and search, plus whatever card-content authority the tracking declaration
grants the writer." Keep the sentence's existing statement that the `lead` supplies
read and search by default and that sibling sweeps depend on them.

Amend the lead's worker-access restatement to say that, in every spec pass, the
writer carries its fixed read-and-search access plus whatever card-content authority
`docs/BOARD.md` grants the writer. Leave its separate auditor, coder, and QA grants
unchanged. The writer's general caller-granted paragraph continues to govern every
other dispatch, including the outcome where a declaration grants no board or leaves
an operation unbound.

The access sentence itself is the mechanism under test. A generic nearby statement
that the writer may update a card would not satisfy the design if the fixed spec-pass
sentence still restricts the grant to read and search, so each scenario observes that
specific sentence in its owning manual.

### Coordination

The board-side sibling sweep used the declared Linear search binding with the query
`writer board access card correction`. It found the source story and related completed
pipeline improvements, but no independent active story that changes this same
fixed-grant wording. No shared infrastructure or card relationship needs a
coordination note.

## Requirements

### R1 — State the writer's full spec-pass grant (AC1)

**WHEN** a reader opens the fixed spec-pass board-access sentence in
`plugins/ca77y-engineering/skills/writer/SKILL.md`,
**THEN** that one sentence states read, search, and whatever card-content authority
the tracking declaration grants the writer, while retaining the established
read-and-search default and sibling-sweep rationale.

### R2 — Keep the lead's grant in agreement (AC2)

**WHEN** a reader opens the worker-access restatement in
`plugins/ca77y-engineering/skills/lead/SKILL.md`,
**THEN** it gives a writer in every spec pass the same fixed read-and-search access
plus whatever card-content authority `docs/BOARD.md` grants the writer.

### R3 — Constrain the broadened grant to the spec pass (AC3)

**WHEN** a reader compares the amended writer and lead access passages with the
unchanged caller-granted paragraph in the writer manual,
**THEN** only the writer's spec pass gains declaration-granted card-content authority;
the auditor's stated read/search or read-only grants and the coder and QA's no-access
grants remain as written.

## Validation

- Open both changed `SKILL.md` files and their YAML frontmatter, then inspect the
  full amended access paragraphs against R1–R3. This directly validates the two
  loaded document artifacts rather than a generated substitute.
- Run the repository's skill quick validator for every skill directory, including
  the changed `writer` and `lead` directories, as required by `AGENTS.md`.
- Run `python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-engineering`
  and the same validator for `plugins/ca77y-library`. The engineering manifest's
  `skills: "./skills/"` loader consumes the changed files; validating both plugin
  roots preserves the repository's declared validation floor.

## Tasks

- [ ] Coder: update the fixed spec-pass access sentence in
  `plugins/ca77y-engineering/skills/writer/SKILL.md` to satisfy R1 without changing
  the surrounding default-deny policy.
- [ ] Coder: update the matching worker-access restatement in
  `plugins/ca77y-engineering/skills/lead/SKILL.md` to satisfy R2 and R3, leaving
  every non-writer dispatch grant unchanged.
- [ ] Coder: preserve the checked YAML `description` fields in both affected
  `SKILL.md` files; neither describes the changed board-access policy and neither
  requires an edit.
- [ ] QA: perform the document observations and validator runs in **Validation**;
  report any unintended access-policy change as an AC1–AC3 finding.
- [ ] Writer docs pass (not the coder): convert the delivered policy clarification
  into the durable engineering documentation if the shipped diff warrants it, then
  remove this spec from `docs/specs/`.

---
Task: SMR-196
Card state read: In Progress (2026-08-31)
Coding complexity: 2 — One established Markdown instruction gains a precisely scoped rule; it has one consumer skill, no external dependencies, and no unresolved implementation design.
---

# Require already-satisfied entries to cite reader-findable regions

## Goal

Make the Codex-native writer skill require every *Already satisfied criteria* entry to
point a later reader to a stable, human-findable region of the cited post-build artifact,
instead of a line number that the same build can move.

## Acceptance criteria

This checked transcription is licensed because the acceptance gate must compare the
card's current wording rather than a paraphrase that could drift toward the shipped
instruction. The auditor performs that equality check.

Card: `SMR-196`, read in `In Progress` on 2026-08-31.

- **AC1.** Each already-satisfied entry addresses its region the way a reader finds it — the section heading, the bold lead-in, or a phrase quoted from the text itself.
- **AC2.** A line number is forbidden for this purpose, with the reason stated: these entries are read against the post-build tree, where the same pass's own edits can move any cited line.
- **AC3.** Line citations pinned to an immutable commit (the spec's own Edit sites, which cite a fixed pre-build state) remain allowed and are named as the exception, so the two cases are not confused.

## Design

### Boundary

The deliverable is a non-code artifact:
`plugins/ca77y-engineering/skills/writer/SKILL.md`.

Update only its *Already satisfied criteria* authoring rule. Preserve that rule's
existing requirements to identify the satisfying file(s) and settling commit, name the
post-build observation QA re-validates, and say whether the task touches that surface.
The new wording must add the citation form, the reason line numbers are unsuitable for
this use, and the fixed-commit exception in the same rule so a writer receives one
unambiguous instruction when composing an entry.

The file's frontmatter `description` was checked and needs no change: it describes the
writer's broad ownership of specs and docs, not the internal citation form for one spec
section.

Do not change the general dependency-citation rule, other engineering skills, the
custom-agent TOML, or introduce a mechanical line-citation checker. SMR-295 owns
mechanical closure of already-existing in-repository `path:line` findings; this task
prevents this particular kind of new citation from being authored.

### Citation rule

Within the *Already satisfied criteria* rule, require the writer to cite a stable region
using one of these reader-facing anchors:

- the section heading;
- the bold lead-in; or
- a phrase quoted verbatim from the cited text.

Forbid a line number as the region address. State why: QA and the acceptance gate open
the cited artifact in the post-build tree, while the task's own edits may have added or
removed lines, leaving a still-resolvable number aimed at unrelated text.

Name the narrow exception in the same passage: a line citation pinned to an immutable
commit remains valid for a spec's own *Edit sites*, because that citation deliberately
identifies a fixed pre-build revision rather than a region a later reader must locate in
the post-build tree.

### Coordination

SMR-295's related-card prose already describes this task as the adjacent authoring-side
rule and reserves its own scope for a QA-owned mechanical resolver check. The two cards
do not conflict, so no board correction is needed.

### Validation

Open the changed writer skill and confirm its *Already satisfied criteria* rule:

1. retains the three pre-existing entry duties;
2. names the heading, bold lead-in, and quoted-phrase region forms;
3. forbids a line number and gives the post-build-tree/edit-shift reason; and
4. names immutable-commit *Edit sites* citations as the exception.

Run these exact checks from any directory; every target path is absolute:

```sh
for smr196_skill_dir in \
  /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-196-require-already-satisfied-entries-to-cite-a-region-readers/plugins/ca77y-engineering/skills/* \
  /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-196-require-already-satisfied-entries-to-cite-a-region-readers/plugins/ca77y-library/skills/*; do
  python3 /Users/catty/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$smr196_skill_dir"
done
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-196-require-already-satisfied-entries-to-cite-a-region-readers/plugins/ca77y-engineering
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-196-require-already-satisfied-entries-to-cite-a-region-readers/plugins/ca77y-library
```

The first command is the installed skill-creator quick validator; its loop covers every
current engineering and library skill directory, including the changed writer skill. It
opens each directory's `SKILL.md` and reports invalid YAML frontmatter, missing required
`name` or `description` fields, invalid skill names, or unfinished TODO markers. The two
plugin-validator invocations then validate the manifest and packaged skill structure for
both plugin roots. These loaders and manifests consume the changed skill and its
frontmatter; no build or runtime package is in scope.

## Requirements

### R1 — Cite already-satisfied evidence by a reader-findable region

Maps to: AC1, AC2, AC3.

**WHEN** a writer puts a card criterion in *Already satisfied criteria* and cites the
file or prose that already satisfies it

**THEN** the changed writer skill visibly requires the entry to identify that region by
its section heading, bold lead-in, or a phrase quoted from the cited text; visibly
forbids a line number because QA and the acceptance gate read the post-build tree after
the same pass can move lines; and visibly allows an immutable-commit line citation for a
spec's fixed pre-build *Edit sites*.

The exact changed passage, rather than a validator result, is the observation: the
validators can establish that the skill remains loadable but cannot establish that all
three semantic cases are present.

## Tasks

- [ ] In `plugins/ca77y-engineering/skills/writer/SKILL.md`, extend the *Already
  satisfied criteria* authoring rule with the three stable region forms, the post-build
  line-number prohibition and rationale, and the immutable-commit *Edit sites*
  exception; retain its existing per-entry evidence and QA duties.
- [ ] Run the exact all-skill quick-validator loop and both absolute plugin-validator
  commands from *Validation* after the Markdown edit. This is validation of the
  non-code artifact, not a new test or a task for another pipeline role.

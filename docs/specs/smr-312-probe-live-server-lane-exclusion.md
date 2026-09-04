---
title: Forbid a pin probe from overlapping a live-server validation lane
story: SMR-312
status: proposed
Coding complexity: 2
Complexity rationale: One agent manual gains a constrained prose rule; the change has no new API, dependency behaviour, or implementation unknowns.
---

# Forbid a pin probe from overlapping a live-server validation lane

## Goal

Make the QA pin-probe procedure prevent temporary source reverts from changing an app while a browser or device validation lane is driving that app through a watch-mode development server. The rule preserves the existing revert-run-restore proof while making its safe scheduling and recognizable contamination signature explicit.

## Acceptance criteria

This is the checked, verbatim transcription of Linear issue `SMR-312`, read in `In Progress` on 2026-09-04. It is licensed here because the auditor mechanically compares it with the card; a paraphrase could drift toward the implementation.

- AC1: `qa` is told that a probe's temporary revert may not overlap a running lane served by a live dev server, and why: the lane's app reloads from the file being reverted.
- AC2: The permitted orders are stated — finish the lane and probe after, or probe first and start the lane once every file is restored.
- AC3: The rule is generalised beyond mobile to any watch-mode dev server backing a browser or device suite.
- AC4: The failure signature is named, so an overlap that did happen is recognisable rather than dismissed as flake.
- AC5: Optionally, a project may serialise the lane with a lock agents check before editing tracked source, so an accidental overlap is refused rather than silently corrupting a run.

## Design

### Boundary

The deliverable is a non-code artifact: the QA custom-agent procedure at `plugins/ca77y-engineering/agents/qa/AGENT.md`.

This story changes only `plugins/ca77y-engineering/agents/qa/AGENT.md`. The installer resource, installer script, plugin manifest, lead procedure, and user-facing README are consumers and are outside this story's changed-file set. The installed QA resource already names `../../../agents/qa/AGENT.md`; the obsolete `skills/qa/SKILL.md` is absent from the current worktree and must not be recreated.

Measured baseline: against the unmodified SMR-312 worktree at `f29c0a9`, `rg -n -i 'watch-mode|live dev server|validation lane|hot.reload|hot reload|seriali[sz]|lock.*agent|agent.*lock' plugins/ca77y-engineering/agents/qa/AGENT.md` returned no matches. The current QA procedure therefore has no live-lane exclusion, failure signature, or serialization guidance.

The target has no frontmatter `description`; there is no definition-file description to update.

### Live-lane exclusion

Add one clearly labelled paragraph to the existing findings-round probe procedure. It must retain the existing one-fix-at-a-time revert, run, restore, and green re-run sequence, then require QA to schedule that sequence wholly before or wholly after an affected live-server lane. A lane is affected when its browser or device suite drives an app from a watch-mode server and the probe temporarily changes source the app reads.

The paragraph must name exactly two safe schedules: finish the lane before starting the probe, or finish the probe and restore every changed file before starting the lane. It applies to watch-mode servers behind browser suites as well as device suites.

It must also instruct QA to treat a failure during an overlap as a possible hot-reload contamination signature when a source revert reloads the running app, an in-flight flow fails on changed content, and the same flow passes after restoration and a serialized re-run. QA reports that evidence and investigates it as overlap contamination; the signature is not proof that every intermittent failure is harmless flake.

Projects may add a stronger guard in their own rules: before a pin probe edits tracked source, a required lane lock or active-agent check may refuse the probe while the lane is active. The generic QA manual does not invent a lock protocol or require one where project rules provide none.

### Validation

This is a prose deliverable. QA validates each scenario by opening the changed `AGENT.md` and inspecting the labelled paragraph; no product test file is added.

The validation also reaches the installed-agent consumer: run `python3 plugins/ca77y-engineering/skills/install-subagents/scripts/install_agents.py --check`. The check must validate the QA resource and compile the referenced manual without error. Run the repository's documented engineering-plugin validator from `README.md` over `plugins/ca77y-engineering` as the package-level check. No format or lint command is defined for this Markdown-only change.

## Requirements

### R1 — Exclude an affected live-server lane

**WHEN** QA is about to temporarily revert tracked source for a pin probe while a running validation lane drives that source through a watch-mode development server,

**THEN** the labelled probe paragraph in `AGENT.md` says that the probe may not overlap that lane and explains that the app reloads from the file being reverted.

This fails on the measured baseline because the committed QA procedure contains no live-lane exclusion.

### R2 — State both permitted schedules

**WHEN** a reader opens the live-lane exclusion paragraph to decide when to run a probe and its validation lane,

**THEN** it states both allowed orders: finish the lane and run the probe afterwards, or run the probe first and start the lane only after every changed file is restored.

This fails on the measured baseline because neither schedule is present.

### R3 — Cover browser and device suites

**WHEN** a watch-mode server backs a browser suite rather than a mobile/device suite,

**THEN** the same paragraph explicitly applies the exclusion to browser and device suites, rather than limiting it to mobile validation.

This fails on the measured baseline because the procedure does not mention watch-mode servers or either suite type in connection with probes.

### R4 — Name and qualify the overlap signature

**WHEN** a flow fails while a probe temporarily reverts source under a live lane, then passes after the source is restored and the flow is re-run serially,

**THEN** the paragraph names that sequence as possible hot-reload contamination to report and investigate rather than dismissing it as flake, while preserving that the sequence alone does not prove the cause.

The qualifying language rules out an alternative explanation: ordinary intermittent failures can also pass on a later run, so the manual must not label every retry pass as contamination.

This fails on the measured baseline because it gives no overlap-specific failure signature.

### R5 — Permit a project-defined refusal guard

**WHEN** a project's rules require a lane lock or active-agent check before tracked source is edited,

**THEN** the paragraph permits that stronger guard to refuse the pin probe while the lane is active, without inventing or requiring a lock protocol for projects that define none.

This fails on the measured baseline because no serialization guard is mentioned.

## Tasks

1. **Coder:** update the existing findings-round probe section of `plugins/ca77y-engineering/agents/qa/AGENT.md` with the labelled live-lane exclusion described in R1–R5. Preserve the existing probe's restore-verification rules and all unrelated QA guidance.
2. **QA:** inspect the changed paragraph against R1–R5, run the installer `--check` consumer validation, and run the repository-documented engineering-plugin validator. Treat the scenarios as prose assertions; no new test file is in scope.

## Already satisfied criteria

None. All five criteria require text absent from the measured baseline.

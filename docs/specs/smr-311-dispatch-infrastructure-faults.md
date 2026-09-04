---
task: SMR-311
card: https://linear.app/ca77y/issue/SMR-311/do-not-count-a-dispatch-that-fails-before-any-work-against-the-3-rule
card_state_read: In Progress (2026-09-04)
Coding complexity: 4 — One central Markdown skill changes an established dispatch and recovery policy that every pipeline worker uses; the behaviour is prose-defined, has no external API integration, and the only remaining implementation choice is precise placement within the existing policy.
---

# Do not count pre-work dispatch infrastructure faults

## Goal

Keep the 3× rule focused on an agent's repeated inability to close a problem. When
the dispatch infrastructure fails before a worker reports work, stop and diagnose the
dispatch configuration instead of consuming a worker attempt through identical
retries.

## Acceptance criteria (verbatim transcription)

This checked copy transcribes SMR-311's acceptance criteria rather than paraphrasing
them, so the auditor can mechanically prove that the build did not drift from the
card. The Linear card was read in `In Progress` on 2026-09-04.

- AC1: A dispatch that fails **before the worker reports any work** is classified as an infrastructure fault and does not count against the 3× rule.
- AC2: On the first such failure the `lead` diagnoses the dispatch path itself — the requested custom agent plus the model and effort submitted to `spawn_agent`; it includes a host-reported effective model and session-versus-disk source when available, and reports either fact as unavailable when the host cannot expose it — and escalates with that diagnosis instead of retrying.
- AC3: The `lead` is told that a settings-file edit does not reach an already-running session, so the remedy for an inherited bad value is a new session, not a retry in the current one.
- AC4: The rule distinguishes an infrastructure fault from a worker that started and failed, by the worker having reported nothing at all.

## Design

### Boundary

The deliverable is a non-code artifact:
`plugins/ca77y-engineering/skills/lead/SKILL.md`.

In scope:

- the lead's fresh-dispatch and collection policy;
- its 3× rule and ledger duties where they distinguish a pre-work infrastructure
  fault from a worker attempt; and
- this temporary task spec under `docs/specs/` until the docs pass converts and
  removes it.

The lead skill's YAML `description` was checked. It describes the skill's end-to-end
ownership rather than dispatch-failure classification, so it remains unchanged.

Out of scope are the custom-agent TOML resources and their `agents/<role>/AGENT.md`
source manuals, the `writer`, `coder`, `qa`, and `auditor` procedures,
`docs/BOARD.md`, and changes to host configuration or a running session. The existing
`references/recovery.md` remains the procedure for a worker whose report is missing or
whose status must be resolved; this task adds the lead's classification and escalation
policy in the consumer skill rather than duplicating that procedure.

Measured baseline: at merged commit `f29c0a9`, the loaded lead skill says that a
failed dispatch is “retried or escalated”
(`plugins/ca77y-engineering/skills/lead/SKILL.md`, opening pipeline paragraph), sends
a missing report to recovery, and applies the 3× cap to “anything” (its *Dispatch,
resume, and collection* and *When a gate finds a problem* sections). Its current
*Spawn* rule passes the selected role model and reasoning effort explicitly to
`spawn_agent` and records them in the ledger; `followup_task` keeps that prior
selection. It contains no pre-work infrastructure classification, model/session
diagnostic, or non-counting rule. The engineering manifest's `"skills": "./skills/"`
loads this source file directly; no generated or resolved skill artifact or
configuration-rendering command is defined in the worktree, so this source reading is
the measured effective baseline.

### Deviations from the card

The original AC2 said: “On the first such failure the `lead` diagnoses the dispatch
path itself — the resolved subagent model, and whether the value is live in the
session's environment rather than merely on disk — and escalates with that diagnosis
instead of retrying.” The Codex dispatch contract in this worktree gives the lead the
requested custom-agent name and the model and effort it passes to `spawn_agent`, plus
the returned target or host error. It binds no safe command or tool that exposes an
effective runtime model or the source of current-session configuration; the lead also
forbids `.env` inspection. Treating the old wording as an always-available diagnostic
would therefore assert an unmeasured Codex precedence rule.

The card now requires the lead to report the requested agent, model, and effort;
include effective-model and session-source facts when the host reports them; and name
either unavailable fact explicitly. This preserves the incident diagnosis while making
the boundary truthful. No new implementation work follows from the correction. A
future supported, non-secret runtime diagnostic that reports effective model and
session source would settle the currently unavailable facts and permit a later card
refinement.

### Pre-work infrastructure fault

Add one policy adjacent to the existing dispatch and collection rules. A dispatch is
an infrastructure fault only after the lead has established all of the following:

1. the fresh `spawn_agent` call or a `followup_task` delivery failed before the worker
   supplied a report of work for that dispatch;
2. the established recovery checks have ruled out a live worker, a delayed final
   report, and an attributable worktree artifact; and
3. the lead has no report from the worker to route as a worker or gate problem.

The no-report condition is the classification boundary required by the card. The
recovery checks are necessary because a lost completion notification could also leave
the lead with no report while the worker is still live or has edited its assigned
file. That alternative cause must preserve the existing recovery path rather than
turning a live worker into a duplicate dispatch.

Record a confirmed fault in the ledger separately from gate rounds, coder attempts,
and the 3× counter. It does not consume an attempt. On the first confirmed occurrence,
do not retry it in the current session; escalate to the user with the diagnostic and
the next action needed to start a clean session. Once that session is available, its
lead resumes from the ledger and makes the pending dispatch with the normal routing
rules.

### Dispatch diagnosis and session remedy

The evidence the lead can observe is the requested custom-agent name, the model and
reasoning effort passed to a fresh `spawn_agent` call, the model and effort already
recorded for a `followup_task` target, and the target metadata or non-secret host error
returned by that call. When the host error itself names model resolution, the lead
reports that host statement; any other error does not establish a model or
session-source cause.

**Assumption — unavailable runtime introspection.** The Codex mechanisms bound by the
current lead skill do not document a safe result for the effective subagent model or
the provenance of a live session value. This pass cannot measure either through the
worktree or those bound calls. A supported host diagnostic returning those non-secret
facts would settle the assumption. Until then, the escalation reports the requested
dispatch inputs and raw host error, includes an effective model or session source only
when the host returns it, and otherwise labels that fact **unavailable**. It neither
reads `.env` files nor assumes a configuration-precedence rule.

When a host diagnostic or the user confirms that an inherited bad model value is live
in the current session, the policy states that a settings-file edit does not alter
that already running session. The remedy is a new session with the corrected
configuration, then ledger-based continuation; repeating the same dispatch in the
existing session is not a remedy. **Assumption — session replacement:** this
card-required remedy is not reproducible from the worktree; a host-supported
configuration test would settle it. The changed artifact must state the conditional
remedy, not claim that Codex gives an unobserved precedence explanation.

### Worker failure boundary

Keep a worker that has reported any work on the ordinary path. Its reported failure,
or a gate finding against its work, remains a problem that the usual routing and 3×
rule bound. This rule does not excuse a worker failure merely because it occurred
early, and it does not let the lead do the worker's work. The direct distinction is
whether the worker reported work at all, after recovery has eliminated the
no-report-but-live-worker alternative.

### Coordination

The declared Linear search binding was used for `3× rule`, `infrastructure fault`, and
`failed dispatch`. SMR-167 is the completed main-session dispatch/collection policy
that this task preserves; SMR-193 is a backlog story about findings-file ownership.
SMR-303 is **In Progress** and changes the same lead dispatch policy to declare
concurrent workers' file ownership and forbid reverting unexplained edits.

The two stories have different behaviour but overlapping edit territory. If SMR-303
lands first, this task's coder starts from its changed `lead/SKILL.md`, retains its
concurrency and no-revert policy, and adds only the pre-work fault policy. If SMR-311
lands first, SMR-303 must integrate this task's no-report recovery boundary rather
than replace the dispatch section. Before either task commits, its lead checks the
other story's landed diff and reports a merge conflict instead of discarding an
unexplained rule. Neither card records a dependency or relationship sentence that is
stale, so no board correction is authorised or needed.

This ordering check is run coordination, not a behaviour the shipped `lead` skill
needs to state. It is untested by design: the spec's document scenarios inspect only
the pre-work dispatch policy, while the lead performs the cross-story diff inspection
before it commits.

## Requirements

### R1 — Classify a confirmed pre-work dispatch failure separately (AC1, AC4)

**WHEN** a reader opens the changed dispatch/collection policy after a dispatch has
produced no worker report, **THEN** the policy requires the existing recovery checks
to rule out a live worker, delayed report, and attributable worktree artifact before
calling the result an infrastructure fault; it states that the worker's lack of any
report is the boundary and records the fault outside the 3× attempt counter.

The recovery checks rule out the alternative cause of a lost report from a worker that
is still working or already changed a file. A nearby statement that merely says a
dispatch “failed” would not prove this mechanism because it could cover an ordinary
worker failure.

### R2 — Diagnose and escalate the first infrastructure fault (AC2)

**WHEN** a reader opens the first-fault response in the changed lead skill,
**THEN** it tells the lead to stop retrying and escalate with the requested custom
agent, the model and effort supplied to `spawn_agent` (or recorded for a follow-up),
and the non-secret host error or target metadata; it includes an effective model or
session-versus-disk source only when the host reports that fact and otherwise labels
it **unavailable**, without reading `.env` files or asserting configuration
precedence.

### R3 — Require a new session for a live inherited bad value (AC3)

**WHEN** a reader opens the session-remedy passage in the changed lead skill,
**THEN** it states that, when a host diagnostic or the user has established an
inherited bad value is live in the current session, a settings-file edit does not
change that session; it directs the user to start a new session with corrected
configuration and directs its lead to continue from the ledger instead of retrying.

### R4 — Keep reported worker failures under the ordinary 3× rule (AC4)

**WHEN** a reader compares the infrastructure-fault passage with the unchanged 3×
rule in the changed lead skill, **THEN** it states that a worker which has reported
work and then fails, or has work rejected by a gate, is routed and counted by the
ordinary 3× rule rather than classified as infrastructure.

## Validation

- Open the changed `plugins/ca77y-engineering/skills/lead/SKILL.md` and inspect the
  dispatch/collection, 3×, and ledger passages against R1–R4. The observable result
  is the required policy text in the loaded Markdown artifact; no test runner output
  can establish those prose semantics.
- Confirm the unchanged `description` frontmatter does not claim a contradicted
  dispatch policy, and inspect
  `plugins/ca77y-engineering/.codex-plugin/plugin.json` to confirm its `./skills/`
  loader still consumes the changed file.
- Run the repository-required skill quick validator for every engineering and library
  skill directory, then validate both plugin roots:

  ```sh
  for smr311_skill_dir in \
    /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-311-do-not-count-a-dispatch-that-fails-before-any-work-against/plugins/ca77y-engineering/skills/* \
    /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-311-do-not-count-a-dispatch-that-fails-before-any-work-against/plugins/ca77y-library/skills/*; do
    python3 /Users/catty/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$smr311_skill_dir"
  done
  python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-311-do-not-count-a-dispatch-that-fails-before-any-work-against/plugins/ca77y-engineering
  python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/catty/Workspace/agentic-codex/.worktrees/tokwieci/smr-311-do-not-count-a-dispatch-that-fails-before-any-work-against/plugins/ca77y-library
  ```

## Tasks

- [ ] Coder: update the fresh-dispatch and collection policy in
  `plugins/ca77y-engineering/skills/lead/SKILL.md` to define and ledger a confirmed
  pre-work infrastructure fault, preserving the existing recovery checks and excluding
  that fault from the 3× counter.
- [ ] Coder: add the first-fault diagnostic and session-remedy wording in that same
  skill, including the model and effort passed on a fresh spawn, the recorded selection
  on a follow-up, host-returned evidence, explicit **unavailable** labels for
  effective-model/session-source facts the host does not expose, and the conditional
  new-session continuation path.
- [ ] Coder: state in the 3× rule's vicinity that a worker which has reported work
  remains on the ordinary counted route; do not alter the hard cap or the junior-to-
  senior promotion carve-out.
- [ ] Coder: before editing the lead skill, inspect whether SMR-303's concurrent-
  worker policy has landed and preserve it if present; report an overlapping-text
  conflict instead of replacing either policy.
- [ ] Coder: preserve the checked YAML `description` and leave the custom-agent TOML
  resources, agent manuals, and `references/recovery.md` unchanged.
- [ ] QA: perform the artifact observations and commands in **Validation**; report any
  conflict between the new no-report boundary and the ordinary worker-failure route as
  an AC1–AC4 finding.
- [ ] Writer docs pass (not the coder): fold the shipped dispatch policy into the
  durable engineering documentation if the run's diff warrants it, then remove this
  temporary spec from `docs/specs/`.

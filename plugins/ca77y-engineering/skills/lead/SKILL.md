---
name: lead
description: Take one task end to end, from a prompt (optionally naming a story card) to a single PR — the pipeline run flat from the main session, then handed off without waiting on the review. Invoke it again with the review's findings to fix them. Accepts an optional `--fast` flag.
---

You coordinate one task from the main session: writer → readiness auditor → coder → QA → docs writer → acceptance auditor → ship. Local QA reviews the diff and validates the result; the separately configured PR reviewer reviews the published change. Keep those outcomes distinct.

Dispatch the work; do not author specs, code, tests, docs, or acceptance judgments yourself. Trust worker reports. Your project-command exceptions are formatting, the initial lint floor, and final validation described below. One story has one worktree, branch, active coder, and PR. Workers are leaves; you own dispatch, commits, and publication.

## Authority and inputs

Read `docs/BOARD.md` and `docs/FORGE.md` before creating anything. Use only their declared bindings, status vocabulary, visibility rules, and write authority. Project context supplies layout and documentation conventions; FORGE owns git and forge decisions.

- Missing BOARD: proceed trackerless from the prompt and spec; report that no card transitions were possible.
- Missing FORGE: stop before worktree creation, provisioning, scratch files, card transitions, or dispatch. Recommend `ca77y-engineering:forge`; do not author a declaration to unblock yourself.
- A declaration explicitly naming no board/forge or an unbound operation is valid. When this affects the run, read [declaration exceptions](references/declaration-exceptions.md).

A `lead` invocation authorizes branch/worktree creation, commits, push, and one PR within FORGE's bindings. It does not authorize other writes. Read a named card and its links through BOARD. When the input names an open PR or its findings, read [open-PR repair](references/open-pr-fix-run.md) before creating anything; reuse that branch and PR.

## Dispatch contract

Dispatch configured custom agents with `fork_turns: "none"`, the model table below, and a self-contained prompt containing:

- mode and task, spec path, absolute worktree path, provisioning status;
- relevant commit refs and findings (long findings go in ignored `tmp/findings-round-<N>.md`);
- expected edit paths, other live workers' roles and concrete ownership paths, and preservation of their edits; explicitly say when no other worker is active;
- board access: writer spec pass and readiness auditor **read/search**, acceptance auditor **read**, coder and QA **none**. No worker gets forge writes.

The installed definition supplies the role's core procedure and conditional reference links. Do not paste manuals or card bodies into prompts. If a configured engineering role is missing, stop and recommend `ca77y-engineering:install-subagents`; never substitute a generic worker.

Record targets and ownership before introducing overlap; wait when ownership cannot be stated. Resume available coder/spec-writer targets with `followup_task`; otherwise dispatch fresh with prior findings and refs. Docs starts with a fresh writer, which may be resumed for docs findings. QA and auditors are fresh every round. Collect final reports using `wait_agent`; before waiting, update the ledger and give the user a brief progress note. For missing reports, interruption, or compaction, read [recovery](references/recovery.md).

## The `--fast` flag

Only the user's invocation sets `--fast`. Strip it from task content; it changes spawn models only, never effort, role, gates, or the main session. Do not pass it into worker prompts. Record agent, model, effort, and target for each dispatch.

| Role | Custom agent | Default model | With `--fast` | Effort |
| --- | --- | --- | --- | --- |
| writer | `ca77y_engineering_writer` | `gpt-5.6-terra` | `gpt-5.6-luna` | `high` |
| auditor | `ca77y_engineering_auditor` | `gpt-5.6-terra` | `gpt-5.6-luna` | `high` |
| junior coder | `ca77y_engineering_junior_coder` | `gpt-5.6-luna` | `gpt-5.6-luna` | `xhigh` |
| senior coder | `ca77y_engineering_senior_coder` | `gpt-5.6-sol` | `gpt-5.6-terra` | `high` |
| qa | `ca77y_engineering_qa` | `gpt-5.6-sol` | `gpt-5.6-terra` | `high` |


## Workflow

1. **Workspace.** Read [workspace setup](references/workspace.md) when creating or recovering the worktree. Establish dependencies, ignored scratch state, and a ledger before dispatch. Pass absolute paths; use `git -C <worktree>` and file paths under it. Only the lead provisions dependencies. Never fetch-and-run a substitute project CLI. Keep the repository root read-only except declared repo-local board writes.
2. **Spec and readiness.** Dispatch the writer in spec mode. Format its changed paths before a fresh readiness auditor examines them; use [command handling](references/commands.md) when running project commands. The auditor owns card-transcription equality and semantic readiness, including every re-audit; do not compare or grade criteria yourself. Route findings to the writer, reformat, and re-audit. Commit the passed spec without changing its audited bytes; record its path and commit. Run the project's lint floor once before coding, routing failures through the same command reference. Retain writer board follow-ups and apply only those BOARD authorizes.
3. **Build.** Read the spec's Coding complexity: 1–4 selects junior, 5–10 senior; absent, invalid, or unreadable selects senior with a recorded reason. Dispatch one coder. Keep that tier for subsequent rounds unless promoted under the escalation reference.
4. **QA.** Commit the build, dispatch fresh QA for validation and local diff review, route findings by owner, commit repairs and any QA-added tests, then repeat with fresh QA until clean. Give each reviewer the before/after commits; when there is no new change, supply HEAD rather than an empty commit.
5. **Docs.** Preserve the approved spec from its recorded commit, unchanged, as ignored `tmp/accepted-spec.md`; record the source commit and original path. Dispatch a fresh docs writer with the live spec, spec commit, round refs, and QA report. It converts the spec into durable docs and removes the live spec. There is no separate docs-only gate.
6. **Final validation and acceptance.** Run final project validation through [command handling](references/commands.md), route fixes, and commit the resulting tree including docs and spec removal. Dispatch a fresh acceptance auditor with the saved spec, its source commit and original path, current HEAD, board read access, and validation reports. Acceptance now covers documentation-owned criteria as well as the implementation. It checks equality before grading. Act on its verdict, using the transition table below.
7. **Publish.** With required evidence current and blocking findings closed, push and open the single PR through FORGE, or finish at the final commit where no forge is declared. Include the task/result, tests and limitations, acceptance status, docs, hazards, follow-ups, and the spec's historical path **and commit** so future repair can recover it. Transition the card to awaiting review only after opening, from the declared from-value; attach/comment only where authorized. Do not poll or wait for PR review. Hand off its link and review status.

## Findings and evidence

| Finding or change | Next action |
| --- | --- |
| Code defect | Active coder, then affected QA and acceptance checks |
| Docs defect | Docs writer, then affected acceptance checks |
| Wrong approach, changed scope, or criterion transcription mismatch | Writer revises live spec; readiness before building; refresh the spec commit, saved copy, and downstream evidence |
| Gate passes, then behavior/contract changes | Previous evidence for affected behavior is stale: fresh QA and acceptance before publishing |
| Gate passes, then docs change | Fresh acceptance for affected criteria; QA too if executable content changed |
| Unmet, partially met, or unverified criterion | Resolve the finding or missing evidence; no ordinary accepted handoff |
| Mis-worded criterion, junior promotion, or third unresolved problem | Read [gate escalations](references/gate-escalations.md) |

A gate covers only the revision and behavior it inspected. No repeat is needed for unrelated unchanged evidence, but the fresh reviewer must receive prior evidence and the new diff. Unverified evidence is a limitation, not a pass; apply an explicit declared release policy if one allows it, otherwise stop before publication. Never silently waive a blocking defect.

Give a problem at most three resolution attempts. A third unresolved blocking problem stops publication; the only extra budget is the junior-to-senior promotion in the escalation reference. Commit completed repairs before stopping, subject to FORGE, but do not publish around the failure.

Commit the passed spec, then each build/fix round before fresh QA or acceptance, and the final docs/validation state including converted-spec removal. Name findings and QA-added tests in round messages using FORGE's convention. Push only at its declared timing; never rewrite pushed history, merge, tag, or perform any unbound operation. Stage only attributable task changes; preserve unrelated and concurrent edits. Do not inspect `.env` or expose secrets.

## Handoff

Lead with the outcome and PR link (or branch/commit if local), then validation and acceptance status, material limitations, docs, and follow-ups. Say review is pending and give its declared trigger when useful. Name unresolved wording explicitly; do not call that accepted. Mention skipped transitions or unavailable operations only when they affect the user. Keep routing/model/round detail in the ledger unless requested.

Workers report concrete process friction in their final reports. If useful, the lead may consolidate one deduplicated entry in the worktree's `docs/AGENTS_IMPROVEMENTS.md` with Area, Observed, and Suggested change. No mandatory shared worker writes or speculative improvement checklist.

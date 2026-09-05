# Plugin redesign: evidence-based entry points

Status: proposed specification. Scope: the four main entry points and their shared operating contract. This document does not implement or activate the redesign.

## Purpose

Give the main agent ownership of the requested outcome and let it choose the work needed to establish completion. Replace the mandatory sequence of organizational roles with explicit scope, authority, evidence, and stopping conditions. Delegation, model selection, and procedural references support that judgment.

The design builds on the [redesign report](../reports/2026-09-05-codex-redesign.md). The model-selection and retry rules below define the intended behavior for this specification.

## Scope

Keep two independently installable plugins with four normal entry points:

| Plugin | Entry point | Outcome |
| --- | --- | --- |
| `ca77y-engineering` | `shape` | A scoped proposal with observable acceptance criteria, ready for a delivery decision. |
| `ca77y-engineering` | `deliver` | A verified change through the requested, authorized endpoint, including repair of existing work. |
| `ca77y-library` | `research` | An investigated question with reusable evidence and cited synthesis persisted in the library. |
| `ca77y-library` | `ask` | An answer supported by the existing library, with gaps and uncertainty made explicit. |

This pass specifies entry-point contracts, selection boundaries, reference organization, model selection, and bounded recovery. Specialist manuals, exact model inventories, scripts, setup and maintenance interfaces, compatibility aliases, installers, release migration, and detailed board/forge operations are outside this pass. Existing public skills remain unchanged until implementation and migration are separately undertaken.

## Entry-point selection

Every entry point lives in its plugin at `skills/<name>/SKILL.md`. Its description identifies the user outcome and any boundary needed to distinguish it from another entry point. Support normal implicit selection and explicit invocation; the user does not need to remember command names.

The main agent infers the requested outcome from the current request and conversation. Discussion alone does not authorize implementation. A missing detail does not require routing through `shape` before `deliver`; delivery can resolve routine design questions itself. A clear material change in the requested outcome can justify using another entry point, while preserving the existing scope, decisions, and failure history.

For an explicitly combined request, such as researching a question and shaping a proposal from it, compose the relevant contracts in the same task. Each output must meet its own completion conditions. Completing one entry point does not automatically authorize the next. Do not create another user-owned Codex task unless requested.

## Shared operating contract

The main agent owns interpretation, decisions, integration, evidence, and the final response. It may perform production work directly or delegate bounded responsibilities when parallel work or context isolation makes delegation useful. Every audit or validation is delegated to a fresh subagent; the main agent does not perform that work itself. Every nontrivial change must follow **specification + validation → implementation + validation**, with a separate fresh validator for each gate. The agent chooses the production activities and additional delegation needed within these requirements.

Each entry point must make the following clear in its `SKILL.md`:

- The requested outcome and applicable authority boundaries.
- The context needed to interpret and verify that outcome.
- The evidence required for completion and how to handle missing evidence.
- Mandatory fresh-subagent delegation for every audit or validation, when other delegation is useful, and how models are selected.
- The three-attempt stop rule and the information returned when blocked.
- Which conditional references apply and when to read them.

Read project bindings when the corresponding operation needs them. Missing board or publication configuration blocks that operation, while allowing already-authorized investigation and preparation. Role names in existing declarations do not automatically transfer write authority to renamed entry points; implementation must reconcile those bindings before enabling such writes.

Evidence must identify its acceptance source, relevant artifact or candidate revision, observation or check, and result. Use the smallest representation that remains clear and recoverable. A written spec is required for nontrivial changes; trivial changes and answer-only tasks do not require one. A separate ledger or evidence table is not mandatory for every task. A test result applies to the candidate it checked; later changes invalidate affected evidence. Missing evidence must remain visible rather than being reported as a pass.

Ask a focused question when a missing decision prevents sound progress, and continue independent authorized work when useful. Return sooner than the retry limit when essential access, information, authority, or a plausible next approach is unavailable.

### Fresh audit and validation agents

This rule applies across all four entry points to every audit or validation the main agent needs or chooses to perform, whether required by a gate or initiated at its own discretion. It includes specification checks, implementation acceptance, documentation validation, evidence and citation audits, tests, mechanical validators, link and formatting checks, and revalidation after corrections. There is no exception for documentation-only work, optional checks, or checks considered too small to delegate. Trivial changes may skip a written spec, but their validation still requires a fresh subagent. Scope the delegated check proportionally; a small edit can have one brief validation task that groups relevant checks.

Fresh means a newly spawned agent with no prior participation in authoring, implementation, or validation of the work under examination. Use `spawn_agent` with the configured custom-agent name and a focused task brief, without inheriting the main conversation history. Do not reuse an implementer, the spec validator for final implementation validation, or a previous validator for a corrected candidate. A follow-up that assigns another audit or validation must also use a newly spawned agent, not `followup_task` on an existing worker.

Supply the user requirements and authority, relevant project rules, the exact artifact or candidate revision, supporting raw evidence, and the validation scope. Previous findings can identify required rechecks, but neither earlier verdicts nor the main agent's preferred conclusion substitute for independent examination. The validator inspects the evidence, runs applicable checks, and returns its own findings and gate result. It reports rather than editing the candidate it evaluates.

The main agent integrates findings, arranges corrections, preserves the evidence and failure count, and coordinates the next action. It must not self-certify, override a failed validation as passed, or rename validation work to bypass delegation. Ordinary reading and diagnosis needed to author a solution remain production activities; audit, regression checks, and evidence used to establish completion belong to the validator.

If a required fresh validator cannot be dispatched, report the unmet condition and preserve the prepared work. Do not fall back to main-agent validation. Fresh agents use the same dynamic model-selection policy and shared three-attempt budget as other delegated work; fresh context never means a fresh failure allowance.

## Entry-point contracts

### `shape`

**Use when:** the user wants an idea, problem, or existing evidence turned into a durable proposal, specification, or board-ready story.

**Context:** the user's goal, relevant product and repository constraints, existing proposals or cards, and supplied research. Consult the existing library when applicable; engineering must also work without it. Use board bindings only when a board operation is requested and authorized.

**Completion evidence:** the proposal states the problem and intended outcome, scope and exclusions, observable acceptance criteria, material constraints or dependencies, and unresolved decisions. Important factual premises point to evidence; assumptions and product decisions are identified separately. Demonstrate fit with the existing product to the degree needed for the proposal. A specification intended for execution must satisfy the specification gate below before being labeled ready.

**Endpoint:** write the requested proposal artifact. Create or update a card only within the requested scope and applicable authority. A proposal with unresolved material decisions may be a useful draft, but must not be labeled ready for delivery. Stop at the shaping outcome unless implementation was also requested.

### `deliver`

**Use when:** the user wants a change implemented or repaired, including small fixes, features, documentation changes, or findings on an existing PR. One entry point covers these cases.

**Context:** the request and acceptance source, relevant code and documentation, current checkout and working changes, and any existing PR or prior verification evidence. Read board and forge bindings when their operations apply. Reuse a suitable current environment and preserve unrelated work.

**Completion evidence:** for every nontrivial change, a fresh subagent validates the written specification before implementation begins, and another fresh subagent validates the final implementation against that specification. The final candidate satisfies the relevant acceptance criteria, required checks pass, documentation affected by the change is current, and blocking findings are resolved. Verification is proportional to the change. Implementation validation covers correctness and acceptance. High-risk or materially uncertain designs require independent challenge as part of specification validation. Trivial changes still receive proportionate validation from a fresh subagent.

The specification and implementation gates have a required order; the agent chooses the activities and delegation within them. If a gate cannot pass, preserve the prepared artifacts and report the unmet condition rather than proceeding past it or claiming full completion.

**Endpoint:** the requested, authorized local change, commit, or PR. Generic implementation requests do not silently imply publication. Reuse an existing PR when repairing it. Report the delivered artifact, supporting verification, and remaining material limitations.

### `research`

**Use when:** the user wants a question investigated using new source retrieval, with reusable findings persisted in the library.

**Context:** the research question, existing relevant library knowledge, the library's metadata and authoring conventions, and the configured source provider. In this repository, read `library/_meta/librarian.md` before library work and use `webtools` for internet research. If the provider is unavailable, report the limitation instead of substituting another provider.

**Completion evidence:** the synthesis addresses the question to the degree supported by available evidence, cites consequential claims, records material uncertainty and contradictions, and distinguishes retrieved facts from inference and product decisions. Persist source identity, access date, supporting passages, and provenance according to library conventions. Check touched artifacts and affected links.

The main agent may delegate independent source questions. Assign exclusive raw-note ownership when children write; one owner integrates the synthesis and shared metadata. No mandatory librarian, scribe, or full-library audit chain applies.

**Endpoint:** persisted evidence and synthesis, with a cited answer and links to the artifacts. A supported conclusion that the available evidence is inconclusive can complete research. Failed retrieval alone is not evidence that a capability or fact does not exist. Do not conceal a blocked investigation as a completed answer.

### `ask`

**Use when:** the user wants an answer from the existing library, including comparison or synthesis of its contents.

**Context:** the question, library conventions, and the relevant existing pages and raw evidence. Retrieve only the material needed to support the answer.

**Completion evidence:** the answer addresses the question, links its material claims to existing evidence, and identifies relevant gaps, conflicts, or staleness. Distinguish a library-supported fact from an inference.

**Endpoint:** the answer in the conversation. Do not initiate internet research, persist new library content, or perform maintenance merely to fill a gap. If the library does not support an answer, say what is missing; that is a valid retrieval outcome. Move to `research` only when new investigation is authorized by the request or later steering.

## Specification and implementation gates

A nontrivial change introduces or meaningfully alters behavior, contracts, data, architecture, configuration semantics, or operational procedures, or needs material design decisions. File count and edit size do not determine triviality: a one-line authorization change can be nontrivial. Typographical corrections, formatting, and equally bounded edits with established intent and no material semantic impact are trivial. When uncertain whether the exemption applies, use the specification gate.

**Specification + validation:** create or update a durable written spec before implementation. Use the project's spec location, normally `docs/specs/`. The spec identifies the problem, scope, intended behavior or approach, constraints, observable acceptance criteria, and how those criteria will be verified. Keep its detail proportional to the change. An existing spec can be reused if it covers the current request and passes validation against the current context; invoking `shape` separately is not required.

Delegate specification validation to a fresh subagent, which evaluates the spec against the user request, product and repository evidence, feasibility, internal consistency, and the ability to verify its acceptance criteria. Resolve material ambiguities and blocking findings, then use another fresh subagent for revalidation. Record the validated spec revision and the evidence supporting the gate result. The main agent cannot validate its own spec. Validation does not automatically require human approval; continue when the request already authorizes implementation and the gate passes.

Investigation, baseline reproduction, and bounded exploratory experiments may establish specification evidence before the gate passes. They must not become unvalidated production implementation or bypass the gate by being labeled exploration.

**Implementation + validation:** implement the validated spec, then delegate validation of the final candidate to another fresh subagent. It evaluates the candidate against the spec's acceptance criteria with appropriate checks and independent review. Record the candidate revision, spec revision, results, and unresolved findings. Do not claim completion or publish a completed change while blocking findings remain.

If implementation reveals a material flaw or needed change in the spec, revise and revalidate the spec before implementing the affected change. Preserve user intent and authority; do not weaken acceptance criteria simply to make the candidate pass. Changes to either artifact invalidate the evidence they affect. A corrected implementation must pass validation again.

Both gates use the existing three-attempt rule. An evaluated specification that fails to resolve the problem is a failed solution attempt, just as an evaluated implementation can be. Passing specification validation does not erase failures for an outcome that remains unresolved; moving between gates or revising the spec does not grant another three attempts.

## Model selection and escalation

The main agent selects an available model and supported reasoning effort for every delegated task. Selection is based on the particular responsibility, ambiguity, context needs, consequences of error, and available capability evidence. Role identity does not determine the model. Omit fixed model and reasoning assignments from custom-agent definitions so they cannot override the main agent's selection.

Prefer the model judged best suited to produce an accepted result. When a task falls between two plausible capability tiers and the lower tier is reasonably capable of meeting its contract, try the lower tier first. This is a tie-break for borderline complexity, not a requirement to start every task with the smallest model. Clearly demanding work can start on a stronger model. Do not reduce a required review's scope or evidence standard to accommodate the chosen model.

“Lower” and “stronger” describe supported capability tiers for the workload, not an assumption about published parameter counts. Use current host availability and reliable model guidance or observed task outcomes; do not infer a universal ranking from names. Select reasoning effort as well as the model, and validate the combination against what the host supports. Do not invent or silently substitute an unavailable selection.

After a failed attempt, the main agent evaluates the failure evidence. It may improve the approach, increase reasoning effort, select a more capable model, or combine those changes within the remaining attempt budget. Escalation must address a plausible cause; changing models is not itself a new solution. No fixed three-model ladder is required, and the strongest available model does not receive a fourth attempt.

Keep a brief selection rationale with delegated work; record failed attempts and escalation decisions in recovery state. Routine selections need no user confirmation. The current main agent remains on the model selected for its Codex task; this contract does not promise self-switching of the running model. It can delegate a bounded problem to a stronger available model while retaining ownership.

## Three-attempt stop gate

The limit is **three failed solution attempts for the same unresolved problem across the main agent and all delegated agents**. On the third failure, stop execution and return control to the user. A gate or review is an evidence check, not a new allowance of three attempts.

### Counting attempts

An attempt is an approach carried through far enough to evaluate whether it resolves the problem. Multiple edits, tool calls, and checks may belong to one attempt. Failure means the attempted solution does not satisfy its intended acceptance or verification condition, or cannot be completed because the approach fails.

Ordinary exploration, a baseline reproduction, and individual checks within one candidate evaluation do not each consume an attempt. Conversely, evaluating a failed candidate and then trying another corrective approach consumes the next attempt, even within one uninterrupted worker turn. A deliberately tried approach that proves unworkable counts even if it never produces a candidate artifact.

The counter follows the unresolved outcome, not the current error message. A patch that replaces one blocking failure with another has not resolved the problem. Changing the hypothesis, model, reasoning effort, worker, entry point, checkout, or conversation turn does not reset the count. Successful unrelated work also does not reset it.

Distinct problems may have distinct counts only when they are genuinely independent. Once any problem reaches three failures, the current run stops; do not keep executing other work in the background. A verified resolution closes that problem's record. If later evidence shows that the claimed resolution never held, restore its existing failure history.

For delegated repair, give the worker the problem identity and remaining budget. Require it to report evaluated failures and not hide internal repair loops. The main agent owns the aggregate count. Prefer one owner for successive solution attempts; if parallel alternative solutions are useful, reserve an attempt slot for each before dispatch so combined failures cannot exceed the limit. Parallel evidence gathering does not independently consume solution slots.

### At the gate

After the third failure, do not start a fourth solution attempt, escalate again, or publish the unresolved result as complete. Stop active delegated work, preserve useful artifacts and recovery state, and return a concise explanation containing:

- The unresolved outcome and current blocking evidence.
- The three attempted approaches, models and reasoning efforts where applicable, and why each failed.
- The state of the candidate and any useful completed work.
- The specific decision, information, access, or explicitly authorized further attempt needed to proceed.

Saving state and stopping workers are permitted after the gate; continued solution work is not. Persist failure history in a project-approved durable location when recovery requires it. Do not rely solely on live worker handles or disposable worktree scratch. A restored task must retain the count. Further attempts after the gate require explicit user authorization; a new worker or automatic continuation cannot grant it. Record any user-granted additional budget without deleting the previous attempts.

This is a required workflow behavior. Instruction files alone do not enforce a runtime counter; a future implementation must not claim a hard tool-level limit without a mechanism that provides it.

## Where workflows live

Keep each outcome contract in `SKILL.md`. Put substantial conditional workflow detail in references beside the owning manual, using relative links and explicit read conditions. References may describe preferred approaches and must identify any operation-specific constraints that are actually mandatory.

Examples of useful conditional references are PR repair and recovery for `deliver`, card authoring for `shape`, or source persistence formats for `research`. These are illustrative responsibilities, not a requirement to create all those files. A short self-contained procedure can remain in the entry point.

Use this division:

| Location | Content |
| --- | --- |
| `SKILL.md` | Outcome, scope, authority, completion evidence, applicable specification/implementation gates, mandatory fresh audit/validation agents, model-selection rule, three-attempt gate, and reference routing. |
| `references/` beside the owning manual | Substantial conditional procedures, schemas, examples, and recovery details needed only for particular work. |
| `scripts/` | Deterministic operations where executable behavior materially improves reliability; implementation is outside this pass. |
| `agents/<role>/AGENT.md` | A leaf specialist's bounded contract; specialist redesign is outside this pass. |

Do not hide universal safeguards in optional references, load all references by default, or move the old mandatory role pipeline into a reference unchanged. Keep the nontrivial-change rule and the required order of specification validation before implementation explicit in `deliver/SKILL.md`; substantial spec-authoring and validation guidance may live in a conditional reference. Do not add a catalog of separate small/standard/high-risk workflows.

The shared requirements in this spec must be explicit in every applicable entry point. Keep them concise and consistent; do not add another always-loaded router solely to deduplicate a few rules. References owned by a specialist must remain beside that specialist's manual.

## Acceptance scenarios for implementation

These scenarios define observable behavior for a later implementation; no behavioral evaluation has been run as part of this specification.

| Scenario | Required observation |
| --- | --- |
| User asks for a proposal only | `shape` produces the requested proposal and does not begin implementation or silently create a card. |
| User asks for a small documentation fix | `deliver` completes the edit without a separate spec and delegates proportionate validation to a fresh subagent. |
| User asks for a substantive feature | `deliver` writes and validates a spec before implementation, then validates the final candidate against it with independent correctness and acceptance review. |
| A nontrivial configuration or procedural change touches only one line | The specification gate still applies because the change has material semantic impact. |
| A relevant spec already exists | A fresh subagent validates its fit with the current request and context before reuse; no separate `shape` invocation or duplicate is needed. |
| Specification validation passes and implementation is ready | A newly spawned subagent validates the implementation; the spec validator is not reused. |
| A validator finds a defect and the candidate is corrected | A newly spawned subagent validates the correction; the earlier worker is not continued for another verdict. |
| A mechanical validator, documentation validation, or evidence audit is needed | A fresh subagent runs and assesses it; the main agent does not perform the validation itself. |
| The main agent chooses an optional link, formatting, or other validation check | It delegates the check to a fresh subagent even when no formal gate requires it. |
| A fresh validator cannot be dispatched | The main agent reports the unmet condition rather than self-certifying. |
| Specification validation identifies a blocking ambiguity | Implementation does not begin until the spec is corrected and passes validation. |
| Implementation requires a material spec change | The affected spec is revised and revalidated before implementing that change; affected final evidence is refreshed. |
| Two specification attempts fail and an implementation attempt then fails for the same unresolved outcome | The third failure stops execution; passing the specification gate did not reset the budget. |
| An architectural decision remains materially uncertain | `deliver` obtains independent design challenge before committing to the approach. |
| A task sits between two plausible model tiers | The main agent starts the delegated task on the lower capable tier and retains the full completion standard. |
| A task is clearly demanding | The main agent may select a stronger available model immediately. |
| First attempt exposes inadequate reasoning | A revised approach and increased effort or model capability may be used within the remaining two attempts. |
| Three solutions fail across different workers or models | The aggregate count reaches three; execution stops and the user receives evidence and recovery information. |
| A worker privately retries two evaluated failures | Both failures count; its replacement does not receive a fresh three-attempt budget. |
| The visible blocking error changes after a failed repair | The unresolved outcome retains its failure count. |
| A task resumes after interruption or context loss | Existing failure history is recovered before another solution attempt. |
| A baseline test fails before implementation | The reproduction establishes evidence and does not consume a solution attempt. |
| Missing access prevents any viable next approach | The agent returns early with the specific blocker rather than manufacturing three failures. |
| Existing library evidence is insufficient | `ask` reports the gap without triggering research or writing library files. |
| User requests research and a proposal | Relevant contracts compose within the same task; research provenance and proposal acceptance both remain explicit. |
| New research has multiple source questions | Bounded research may be delegated; one owner integrates synthesis and shared metadata. |
| Internet research provider is unavailable | The agent reports the limitation and does not substitute a different provider. |
| A conditional reference is irrelevant | It is not loaded merely because the entry point was invoked. |
| Publication bindings are missing | Authorized preparation may proceed; publication waits for the missing authority or configuration. |

## Design sources

- [OpenAI: Using GPT-6 Astra](https://learn.chatgpt.com/api/docs/guides/latest-model#prompting-best-practices), retrieved 2026-09-05: outcome persistence, instruction sensitivity, explicit delegation guidance, and calibrated verification.
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills), retrieved 2026-09-05: focused skills, implicit selection, progressive disclosure, and explicit inputs and outputs.
- [OpenAI: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents), retrieved 2026-09-05: model inheritance and override precedence, bounded specialists, and coordination costs.
- The specification/implementation gates, mandatory fresh audit/validation agents, three-attempt limit, and lower-tier-first rule for borderline complexity are product requirements for this redesign, not claims that OpenAI prescribes those policies.

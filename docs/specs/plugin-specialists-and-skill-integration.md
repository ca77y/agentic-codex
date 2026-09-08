# Supporting agents and skill integration

Status: proposed implementation specification. This task produces and validates the spec only; implementation is a subsequent task.

Baseline: `master` at `0e7a9968b0e7d8436e936de7c5c102095cb9f591`. The four entry points and per-plugin validators already exist. This spec extends the [entry-point contract](plugin-redesign-entry-points.md). It supersedes the [earlier implementation boundary](plugin-entry-points-implementation.md) for specialist scope, generic validator identities, and preservation of legacy interfaces. That boundary describes the completed entry-point-only pass; its preservation requirements do not constrain this replacement. Where specialist inventory or compatibility proposals in either earlier document differ, this spec controls; the accepted gate, freshness, authority, model-selection, and retry requirements remain in force.

## Outcome and scope

Make `shape`, `deliver`, `research`, and `ask` usable with compatible bounded production agents and independent validators. Build only the new system: remove the old public workflows and obsolete roles rather than preserving aliases or compatibility behavior. Keep the main agent responsible for the requested outcome, evidence, model selection, and aggregate retry limit.

The implementation includes specialist manuals and their conditional references, distributable agent resources, entry-point integration, one-time project bootstrap for each plugin, role-neutral board/forge declarations, removal of legacy plugin contents, installation support, and current documentation. It also removes the agent-improvement and process-feedback mechanism throughout the distributed plugins. Existing names or useful scaffolding may be used under the new contracts; no old pipeline must be retained for compatibility.

Keep engineering and library independently installable. Keep the four normal entry points plus `bootstrap` and `install-subagents` in each plugin: eight skill directories total, with four used for normal work. Bootstrap is a separate one-time setup capability, not part of every delivery or research run. Do not add an external agent service, model-routing scores, fixed model tables, or a second orchestration framework. Preserve project artifacts and existing research provenance. Publication, release/version changes, marketplace updates, and installation into the user's live configuration are outside this implementation task unless separately requested. The local implementation is the endpoint.

## Current integration gaps

- The entry points have suitable report-only validators, but no compatible engineering production leaf. Existing coders and writers assume legacy pipeline artifacts and perform their own checks.
- The installed library researcher currently embeds `skills/researcher/SKILL.md`, which launches a library crew. The new `research` entry point explicitly rejects it as a leaf; the existing scribe also requires self-validation.
- Legacy `lead`, `analyst`, and `researcher` retain fixed sequencing and model tables. Keeping them as separate implementations would preserve conflicting behavior under familiar names.
- Library conventions and bootstrap resources still describe the retired library roles and can prevent direct owner integration. Installer and other supporting skills also contain instructions for coordinator-run validation.
- Distributed manuals still request process-friction reporting, suggested agent improvements, or a shared improvement file.

## Specialist inventory

Use the domain-specific names: engineering has **coder, qa, writer, and auditor**; library has **researcher, librarian, scribe, and clerk**. These are eight bounded custom agents, four per independently installable plugin. Familiar names do not restore the old orchestration pipeline. All models and reasoning efforts are selected at dispatch.

| Plugin | Configured custom-agent name | Core manual | Responsibility |
| --- | --- | --- | --- |
| Engineering | `ca77y_engineering_coder` | `agents/coder/AGENT.md` | Bounded implementation and test authoring. |
| Engineering | `ca77y_engineering_qa` | `agents/qa/AGENT.md` | Fresh, report-only code review, test execution, regression and implementation validation. |
| Engineering | `ca77y_engineering_writer` | `agents/writer/AGENT.md` | Bounded proposal, specification, and documentation production. |
| Engineering | `ca77y_engineering_auditor` | `agents/auditor/AGENT.md` | Fresh, report-only specification readiness, document and acceptance audits. |
| Library | `ca77y_library_researcher` | `agents/researcher/AGENT.md` | Bounded investigation of new sources. |
| Library | `ca77y_library_librarian` | `agents/librarian/AGENT.md` | Read-only retrieval and cited draft answers from existing library knowledge. |
| Library | `ca77y_library_scribe` | `agents/scribe/AGENT.md` | Research-spec drafting, assigned raw-note persistence, synthesis, and metadata production. |
| Library | `ca77y_library_clerk` | `agents/clerk/AGENT.md` | Fresh, report-only research-spec, answer, evidence, provenance, and library-integrity validation. |

Replace the generic `validator` definitions with the qa/auditor/clerk contracts below and update every caller. Bind the library researcher resource to its new leaf `AGENT.md`; remove the old public `researcher` skill. No installed agent compiles an orchestration skill as its core manual.

Rewrite the engineering coder, qa, writer, and auditor manuals and the library researcher, librarian, scribe, and clerk manuals for the new contracts. Replace junior/senior coder resources with one coder resource and remove both generic validator resources/manuals. Retaining a name does not retain a procedure: remove old mandatory role chains, self-validation, and fixed model policy. No generic worker may stand in for a configured role that is missing.

### Coder

Accept a bounded implementation assignment with an absolute project path, authorized write paths, concurrent ownership, relevant requirements, and a validated specification. Work in the supplied checkout; a story worktree, board card, fixed spec template, or commit lifecycle is not a prerequisite. A nontrivial implementation assignment without a validated spec returns the missing prerequisite rather than starting production. Trivial changes follow the entry-point exemption.

Implement the assigned behavior and author its tests. Material changes to an existing validated contract return to the specification gate before affected implementation; do not silently turn implementation into spec revision.

Author regression tests when needed, but leave their execution and all audit/validation to a fresh validator. Ordinary source reading and diagnosis are allowed; test runs, diff audits, lint, and checks used to establish completion are not production-agent tasks. Return test paths and suggested commands as unexecuted when appropriate. Do not report a produced artifact as verified.

Preserve unrelated edits and other writers' paths. Do not expand scope, mutate acceptance criteria to fit an implementation, spawn agents, choose models, publish, or write board state. Report a material design mismatch to the main agent, which owns spec correction and fresh validation.

Return the produced paths, what changed, relevant source locations, intended verification, blockers, and any attempted approach that proved unworkable. Use `followup_task` only to continue production within the remaining allowance; there are no private repair/validation loops.

### Writer

The engineering writer drafts or revises proposals, specifications, and documentation within a bounded brief. It does not independently research a new question, implement code, or validate its output.

Drafting the spec that will receive validation does not require a recursively prevalidated spec. Nontrivial artifact changes governed by an existing specification require its validated scope; material spec revisions return to a fresh auditor before affected implementation. Trivial edits retain the entry-point exemption.

Give the writer the requested artifact, source material, absolute allowed paths, concurrent ownership, and relevant conventions. Preserve facts, citations, and user intent. Report missing material instead of inventing it. The engineering writer does not depend on the library plugin. Return produced paths, unresolved decisions, and unexecuted verification needs. All checks and readiness judgments go to a fresh auditor.

### Scribe

The library scribe drafts or revises a research specification, persists supplied evidence into assigned raw notes, or integrates supplied evidence into synthesis and shared metadata when designated as the sole integration writer. It does not independently research a new question or validate its output. Read the project's own templates and conventions; preserve source passages, provenance, and uncertainty.

Research-spec drafting needs no recursively prevalidated spec. Nontrivial persistence requires the validated scope; changes to that scope require a fresh clerk's verdict before affected writes. The research spec defines the question, evidence standards, and planned artifacts, not a predetermined conclusion.

For raw-note-only assignments, write only exclusive raw-note paths and return deferred metadata needs. For integration, one owner writes synthesis, index, taxonomy, and provenance log after outstanding raw-note writes finish. That owner may be the main agent or one designated scribe; never both concurrently. Return produced paths, source relationships, unresolved decisions, and unexecuted verification needs. All checks and readiness judgments go to a fresh clerk.

### Researcher

Operate as a leaf on one bounded question. Read the project's library conventions and the supplied scope. Do not spawn agents, run full-library maintenance, make product decisions, or audit or validate output. Source reading to build an answer is production; an independent verdict about an answer or its evidence belongs to a validator.

Retrieve new sources through the configured provider; in this repository use `webtools`. Return source identity, dates, supporting passages, claim-to-source relationships, uncertainties, contradictions, and retrieval limitations. Read relevant existing material when it informs the assigned investigation. Missing provider access is a limitation, not permission to substitute another provider.

Return findings and provenance to the main agent; persistence belongs to the main agent or a bounded scribe assignment. Do not write library raw notes, wiki synthesis, taxonomy, navigation indexes, or shared logs. Missing evidence must not become a claim of absence. Separating retrieval from writing does not require a scribe dispatch when the main agent can produce the artifact directly.

No research assignment inherits a fresh three-attempt allowance. Return failures and useful evidence promptly; the main agent chooses a revised approach or capability escalation.

### Librarian

Retrieve from the existing library and prepare a cited draft answer or bounded evidence summary. Use relevant wiki and raw notes, identify conflicting accounts, uncertainty, and coverage gaps, and distinguish retrieved facts from inference. Source reading to produce the answer is not an independent validation verdict.

The librarian is read-only: no internet requests, content persistence, index repair, or other maintenance. A gap stays a gap until the user authorizes new investigation. It does not audit its answer, dispatch researchers or scribes, select models, or reset the failure allowance. A fresh clerk validates the final answer. This role supports `ask` and optional existing-knowledge retrieval during `shape` or `research`.

### QA, auditor, and clerk

QA owns engineering validation that centers on executable behavior: code review, running tests, regressions, test adequacy, and implementation acceptance. It reports missing tests to the coder; it does not add or repair tests itself. QA may include affected documentation and mechanical checks in the same bounded candidate evaluation when it can assess them adequately.

The engineering auditor owns proposal/spec readiness, independent design challenge, document correctness, and acceptance audits that center on requirements and supporting evidence. The library clerk owns research-spec readiness, answer support, provenance, inference labels, contradictions, frontmatter, citations, affected links, and shared metadata. Auditor and clerk may run mechanical checks within their scope, including package and documentation validators.

Select qa or auditor according to the evidence needed, not simply the command name. A code change normally uses QA for implementation validation; a documentation-only change uses the auditor. Split mixed validation only when materially different expertise or an unresolved concern requires it. Do not add a mandatory QA-then-auditor sequence: one adequately scoped fresh verdict can satisfy the final gate.

Keep the existing report-only contract and specialize conditional references by plugin. Every validation assignment uses a newly spawned agent with `fork_turns: "none"`, including small, optional, documentation, test, mechanical, and post-correction checks. Never reuse a spec validator for implementation acceptance or an earlier validator for a changed candidate. A single bounded assignment may group related checks for the same candidate.

The validator independently inspects the requirements, artifact identity, and relevant source evidence. It may establish a missing artifact digest itself. It reports pass, fail, or unverified with commands or observations, artifact/spec identities, acceptance coverage, findings, and actual limitations. It never edits the candidate, writes corrective tests, dispatches workers, selects its own model, or overrides the retry budget.

Engineering's auditor and library's clerk validate their respective plugin's installation and packaging artifacts without requiring the other plugin. “Validator” elsewhere in this spec describes the validation assignment performed by qa, auditor, or clerk; it is not another agent name. The clerk is always report-only; it never repairs the library it is validating.

Run available checks and report their actual results. An absent provisioning-status label alone does not invalidate a successful command. Missing runtime, dependencies, access, or required evidence makes the affected check unverified. Do not install dependencies or fetch-and-run a replacement tool to manufacture a pass; give the coordinator the concrete prerequisite. Distinguish baseline failures from introduced defects.

The validator treats the supplied candidate as stable. If it changes during evaluation, identify affected evidence and return without certifying the new version. Corrections go to the production owner; a new validator evaluates the corrected candidate. This is behavioral separation, not a claim that prose instructions enforce tool isolation.

## Entry-point and installation integration

| Entry point | Production options | Required validation |
| --- | --- | --- |
| `shape` | Main agent drafts; optionally delegate a bounded draft or revision to the engineering writer. Library assistance is optional and must not become a dependency. | Fresh engineering auditor evaluates proposal or spec readiness. |
| `deliver` | Main agent implements; optionally assign disjoint code/test work to the coder and spec/doc production to the engineering writer. | Fresh engineering auditor for the nontrivial spec, then fresh QA for code or a fresh auditor for document implementation validation. |
| `research` | Main agent researches and integrates; optionally delegate existing knowledge to the librarian, new source questions to the researcher, and research-spec drafting or persistence to the scribe. | Nontrivial persistence requires a fresh clerk to validate the spec before writes. Every final answer/artifact validation uses a fresh clerk; after a spec gate, this must be a different clerk. Trivial changes skip the spec gate, not final validation. |
| `ask` | Main agent prepares the answer; optionally delegate bounded read-only retrieval to the librarian. | Fresh clerk checks the exact draft against existing evidence, without new source retrieval or library writes. |

Update all four manuals to name these compatible agents. Remove temporary legacy-incompatibility instructions once their named roles are retired. Optional production delegation remains optional: an unavailable production leaf permits direct work within scope, while an unavailable required validator blocks the gate. Do not silently substitute a generic agent.

The main agent owns integration decisions and assigns exactly one active writer for library wiki content and shared metadata: itself or a designated scribe. Wait for outstanding raw-note writers before integration, and finish deferred index, taxonomy, and log work before final validation. A source batch does not imply one agent per source. Existing-library answers never become library writes or new investigation merely because delegated retrieval finds a gap. Their main agent maintains the separate operational ledger outside the library. Librarian, researcher, and scribe dispatches are optional production choices, not a mandatory chain. The specification and final validation gates remain mandatory wherever their entry-point conditions apply, and each uses a fresh clerk.

Replace the separate `board` and `forge` skills with one engineering `bootstrap`; provide a library `bootstrap` for its scaffold. Each owns its setup references and templates. The four normal entry points consume the configured project; they do not load bootstrap instructions or run setup during ordinary work.

Each `install-subagents` skill installs its plugin's specified agents and references. Trust users to perform installation and reload the catalog as documented. Do not add an installation-certification gate, a verification-pending state, or a mandatory post-reload audit before use. Successful installation reports the installer result without claiming an independent audit occurred. Internal parsing, ownership checks, and atomic writes remain normal installation safeguards.

Source `--check`, drift comparison, and installer tests remain available for explicit diagnostics and plugin development; they are not mandatory first-install steps. Any such validation the main agent requests still goes to a fresh engineering auditor or library clerk. Actual unavailability of a required role during work remains a reported execution prerequisite; trust in installation does not permit inventing a dispatch or self-validation. Keep the direct CLI installation instructions and ordinary catalog-reload guidance.

## One-time project bootstrap

Both bootstrap skills create project configuration locally. They may be rerun to complete or explicitly repair setup, but ordinary tasks do not invoke them as a prerequisite ritual. Read existing files before writing, preserve unrelated content, and make reruns non-destructive. A fully configured project needs no changes. Material uncertainty about project choices is a focused user question, not an invented default or a request to approve work already authorized.

The ordinary nontrivial-change rule applies to setup: write a proportionate setup spec, have a fresh auditor or clerk validate it, create the declared artifacts, and obtain a different fresh validation of those artifacts. The setup spec can be produced without recursively requiring another spec. Installation trust does not waive validation of generated project configuration. No board or forge binding is required to author the setup that the user has requested; setup itself does not perform external board/forge operations.

On a clean project, use the user-approved setup scope, repository facts, and bundled bootstrap templates as inputs for drafting and spec validation. The declarations or library conventions being created are expected outputs, not missing prerequisites for that setup. Writer, scribe, auditor, and clerk briefs must make this bootstrap scope explicit. Existing-project work continues to follow its current applicable rules.

### Engineering bootstrap

`ca77y-engineering:bootstrap` creates or completes `docs/BOARD.md` and `docs/FORGE.md`. The main agent may author the files or delegate drafting to the engineering writer; a fresh engineering auditor validates the setup spec and another validates the result.

Infer supported facts from the repository and supplied context, including repository identity, remotes, existing conventions, tracker configuration, and known tools. Ask for unresolved choices that affect authority or destinations. A project can explicitly use no board or no forge; record that instead of fabricating integrations. Do not create external projects, cards, branches, commits, or PRs merely to establish configuration.

`BOARD.md` records the board identity and access mechanism, lookup and mutation operations, item schema and acceptance format, statuses and legal transitions, user-owned decisions, and the limits on automated writes. `FORGE.md` records repository/remotes, branch and workspace conventions, commit conventions, permitted operations and destinations, change-artifact shape, review triggers, and user-owned publication decisions. Concrete tool and service bindings belong in these declarations; agent orchestration does not.

Creation and authorized setup repair must preserve existing project restrictions. Report unresolved conflicts rather than silently broadening permissions. Put detailed authoring guidance and templates under this bootstrap skill, with board and forge references read only for the declaration being prepared. Remove the standalone board/forge skills rather than making them aliases.

### Library bootstrap

`ca77y-library:bootstrap` creates or safely completes the Markdown library: `raw/`, `wiki/`, metadata instructions, index, taxonomy, provenance log, and raw/wiki/topic templates, with the required library overview and instruction files. Include configured source-provider guidance when supplied by the project; this repository uses `webtools`. Do not create source content or run research as part of setup.

The main agent may author the scaffold or delegate a bounded assignment to the scribe. A fresh clerk validates the setup spec and another validates the generated scaffold. Preserve existing raw notes, wiki pages, metadata, and user customizations on rerun. Complete missing files without rewriting settled content; material repairs require the user's setup scope.

Keep the scaffold useful as plain Markdown. Obsidian configuration is optional, requested separately from the basic scaffold, and described in a conditional reference. Any root instruction-file pointer is merged into an existing appropriate section without duplication. The new bootstrap resources must follow the redesigned ownership and fresh-validation contracts and contain no agent-improvement mechanism.

`research` reads the resulting conventions, not bootstrap's manual or implementation. If the library is missing, report that library bootstrap is needed and permit authorized investigation/preparation; do not silently scaffold or call setup. `ask` reports the missing library without writing one. Bootstrap is independently invocable when the user chooses to initialize the project.

### Project conventions and authority

Update this repository's `library/_meta/librarian.md` and the library bootstrap convention template to allow the library entry-point owner or its sole designated scribe to integrate synthesis and metadata, with bounded retrieval/research leaves and fresh clerks. Express conventions by responsibility without requiring the old role chain. Permit explicit raw-note-only batches to defer shared metadata to the integration owner; require that owner to finish it before completion. Preserve the existing project's templates, raw evidence, taxonomy, and navigation semantics.

Do not rewrite unrelated library content or delete historical raw notes. Other users' existing libraries are not automatically migrated: if their rules conflict with the new writer responsibilities, report the specific binding conflict and request an authorized convention update. Missing setup can be completed through an explicitly requested library bootstrap; ordinary research does not repair or rewrite its own authority.

Rewrite this repository's `docs/BOARD.md` and `docs/FORGE.md` as project declarations with no specific custom-agent or skill names, invocation commands, model routing, or orchestration sequences. Apply the same rule to generated declarations and templates. Replace role-named authority with operation-based conditions, such as “creating a card requires an authorized request” or “automated changes may move Todo to In Progress; terminal transitions require the user.” Record who may authorize an operation in general terms, not which plugin role happens to execute it.

Preserve the existing repository/tracker identities, tools, destinations, status transitions, branch/commit rules, and restrictions on merge, deletion, force push, and terminal board states. Normalize role-specific wording around the corresponding operation without expanding authority or changing product scope. Tool identifiers and configured review-service triggers remain valid binding data; they are not plugin-role assignments. Do not leave references to retired skill procedures or encode “the coordinator” as an indirect name-based permission system.

`shape` and `deliver` read the relevant operation's conditions and use the user's actual request to determine authorization. Remove their obsolete requirement for a grant naming the entry point itself. Their own delegation contracts continue to restrict leaf actions; a role-neutral project declaration does not authorize a coder or auditor to publish. Missing bindings block the affected operation while allowing authorized local preparation; an explicitly requested engineering bootstrap can create or repair the declarations. An ordinary delivery run must not rewrite a declaration to grant itself new authority.

### Current-project authority normalization

Use the following mapping when rewriting this repository's declarations. It replaces named executors with operation conditions, preserving the limits below. User authorization comes from the actual request and established conversation scope, never from invocation of a particular skill. A request to configure an operation is not a request to execute it. These project-specific bindings are examples for bootstrap authoring, not hardcoded defaults for other repositories.

| Board operation | Existing constraint retained | Replacement condition and authorization source |
| --- | --- | --- |
| Locate, read, search | Bound Linear project and connector; no mutations. | Relevant read access follows the requested task; query only its authorized scope. |
| Create | New issue in the configured project/team at Backlog, using the existing card schema. | The user requested filing a card; a proposal-only request does not suffice. |
| Todo → In Progress | Only the first automated middle transition, when work starts; verify current state is Todo. | Authorized implementation of the identified card has started and its workspace is established. Do not move Backlog through the user-owned readiness gate. |
| In Progress → In Review | Only the second automated middle transition; verify current state is In Progress and the PR exists. | The requested publication endpoint has been reached for that same card. |
| Attach PR link | Add the real URL returned by the bound PR-creation operation to the matching card's links. | Attaching the PR is within the authorized card/publication task; do not invent a URL or attach another task's PR. |
| Comment | Progress, hazards, and handoff information on the in-scope issue. | Posting these messages is explicitly authorized; configuration alone does not authorize communication. |
| Edit description, criteria, labels, priority, relations | Corrections within the existing goal during specification preparation; criteria are not changed between implementation and acceptance to fit the result. | The user authorized card refinement and the correction preserves the goal. Record criterion corrections before implementation; a mis-worded criterion found during acceptance returns to the user for correction in a later run. |
| Apply retained card follow-ups | After acceptance, apply only previously identified, authorized follow-ups. | Existing authorization covers the exact update; no criteria rewrite, new goal, or terminal-state transition is introduced. |
| Readiness, terminal states, goal changes | Backlog → Todo, Done, Canceled, Duplicate, and changed product goals remain user decisions. | No automated grant. Ambiguous correction-versus-goal changes are reported, not written. |

| Forge operation | Existing constraint retained | Replacement condition and authorization source |
| --- | --- | --- |
| Read PR or diff | Bound repository and existing change; read-only. | The requested task requires the information. |
| Create/recover branch and worktree | One branch/worktree per story under the configured path, from the target branch; reuse the existing branch/PR for repair. | A commit/PR endpoint or explicit isolation request authorizes the needed workspace operations. Ordinary local edits may remain in the existing checkout. Keep the configured branch derivation and do not create a second story workspace. |
| Commit | Only attributable changes in the authorized story worktree; Conventional Commits; no forced staging or commit to master. | The user requested a commit or PR endpoint. A local-change-only request does not authorize commits. |
| Push | Only the story branch to origin; first push when opening the PR, later pushes after affected validation and acceptance pass. | Publication of the same change is requested; unresolved blocking findings prevent the push. Preserve local-only intermediate checkpoints and never rewrite pushed history. |
| Open PR | One PR per story, bound repository, target master, real returned URL. | The user requested a PR; reuse an existing one when repairing that story. |
| Update PR | Existing PR's title/body reflect the same requested change; existing metadata restrictions remain. | The requested publication/repair scope includes updating that PR, without adding a second PR or widening the task. |
| Comment or trigger review | Same PR, configured review trigger, and no unsolicited polling. | The user authorized the message or review request. Record the observed result; later findings resume through a user request without naming a skill. |
| Remove worktree/branch | User-controlled cleanup after merge. | No automated grant. |
| Merge, auto-merge, close PR, release/tag, force push, amend/rebase pushed history, delete refs, add remotes, act on another repository | Existing explicit prohibitions remain. | No automated grant; a change to these project restrictions is outside this normalization. |

Keep target-branch protection, the single origin destination, real URL usage, no second PR, and user-owned cleanup visible in the rewritten declarations. Keep execution responsibility in plugin contracts: delegated production and validation leaves still do not receive external write authority. Replace role-specific examples and headings in the declarations with operation-focused examples; they must not smuggle the old role or skill names back into otherwise neutral policy.

## Clean replacement

The finished plugin skill inventory is:

| Plugin | Skills |
| --- | --- |
| Engineering | `shape`, `deliver`, `bootstrap`, `install-subagents` |
| Library | `research`, `ask`, `bootstrap`, `install-subagents` |

Delete `lead`, `analyst`, the public `researcher` skill, and the standalone `board` and `forge` skills. Rewrite library bootstrap and add engineering bootstrap under the new setup contracts. Keep only the references and resources needed by the new inventory. Do not leave aliases, forwarding stubs, compatibility flags, old role/model tables, or archived manuals in the distributed plugins.

The new entry points interpret the actual request under their own contracts. A delivery request does not silently mean publication, and shaping does not silently mean filing a card. Explicit requested endpoints remain subject to applicable project bindings. The old `--fast` flag is not part of the new interface; model preferences are expressed in the request and handled by the existing dynamic selection policy.

Current README, plugin presentation, installation instructions, and linked operating guidance describe the new system only. Remove legacy catalogs and compatibility explanations. Historical reports and superseded design specs outside the plugins may remain as source context; they are not runtime instructions and need not be rewritten into a migration history.

## Model selection, ownership, and attempts

Keep the accepted policy in the canonical entry points: the main agent selects available model and supported reasoning effort for each bounded assignment. Start on the lower capable tier when complexity lies between plausible tiers; demanding work can start stronger. Selection is independent of role identity. Do not put model or reasoning fields in distributable or generated agent definitions.

Give each production worker a bounded outcome, acceptance source, permitted paths, concurrent owners, and problem identity with its remaining attempt allocation. Give validators exact artifacts and evidence scope without supplying an expected verdict. Production continuations may reuse a worker; all validation dispatches are fresh.

After failure, the main agent may revise the approach and escalate model or effort within the existing budget. The budget covers one run from the initiating user prompt through resolution of that request. A separate later request, including PR comment review, has its own count; reading comments and discovering or reporting defects do not consume attempts. Continuing unfinished work retains its count. Three failed solution attempts for the same unresolved outcome within that run stop the entire run across specification, implementation, validation, workers, models, and resumptions. No specialist may extend the allowance or treat a role transition as resolution. Keep ordinary task findings and recovery evidence in the main-agent-owned ledger required by [orchestrator ledgers](orchestrator-ledgers.md); do not introduce another agent-level reporting channel.

## Reference organization

Core manuals retain purpose, input/output contract, authority, production/validation separation, and applicable stop rules. Load substantial conditional references only when the assignment needs them. Keep each role's references beside its own `AGENT.md`; keep coordinator procedures beside the owning `SKILL.md`.

Suggested responsibilities to place in references where substantial:

- Coder: implementing a validated change and correcting code/test findings.
- QA: code review, meaningful regression evidence, and unverified-check handling.
- Engineering writer: proposal/spec drafting and documentation production, without the old scoring/template lifecycle.
- Engineering auditor: specification readiness, design challenge, and document/acceptance audits.
- Researcher: new sources and retrieval limitations.
- Librarian: existing-knowledge retrieval and cited draft answers, when substantial guidance is needed.
- Scribe: research-spec drafting, raw-note production, and sole-writer integration, selected by the assigned scope.
- Clerk: research-spec readiness, evidence support and uncertainty, library integrity, and affected-link checks.

Write focused procedures for the new contracts without inheriting retired dispatch chains, self-validation, or model policy. The shared ledger procedure required by [orchestrator ledgers](orchestrator-ledgers.md) applies on every invocation. Keep other conditional procedures scoped to their actual need; do not add a general always-loaded router. Existing new-entry-point references continue to own PR repair, recovery, cards, and final synthesis integration.

## Remove the improvement mechanism

Remove instructions to read, write, consolidate, or report agent-process improvements. This includes `docs/AGENTS_IMPROVEMENTS.md`, process-friction sections, suggested simplifications, shared or per-agent feedback, and instructions explaining that such feedback should go somewhere else. Do not replace the removed text with prohibitions, transcript-review instructions, or an alternative feedback mechanism inside the plugins.

Removal covers surviving skills, agent manuals, references, resources, templates, and generated installed instructions. Retiring an old file is sufficient only if no remaining installed resource compiles its content. Remove any distributed file solely serving that mechanism; preserve unrelated user-owned files and historical reports outside the plugin packages.

Keep task-specific findings, unresolved blockers, source provenance, and the shared failure record needed to finish or recover the user's task. Those are completion evidence, not an invitation to evaluate or improve individual agents. The provenance `_meta/log.md` remains part of the library.

The future validator must inspect the distributed text and temporary generated instructions for remnants. Keep this removal requirement and its audit record outside the plugin's operating instructions; do not add a negative fixture in the distributed plugin that reinstates the removed messages as agent-facing guidance.

## Distribution and file scope

Engineering's `skills/install-subagents/resources/` contains `ca77y-engineering-coder.toml`, `ca77y-engineering-qa.toml`, `ca77y-engineering-writer.toml`, and `ca77y-engineering-auditor.toml`. Library's resource directory contains `ca77y-library-researcher.toml`, `ca77y-library-librarian.toml`, `ca77y-library-scribe.toml`, and `ca77y-library-clerk.toml`. Each points to its matching `../../../agents/<role>/AGENT.md`. Remove the retired resource TOMLs, including both generic validators. Each source has only the managed marker, `name`, `description`, and `manual` fields.

Provide one managed installation path per plugin. The existing installer can be used where it meets the new design; its old implementation is not a compatibility requirement. Installation must produce the four engineering and four library agents listed above, embed only each leaf's core manual, and copy references separately with paths that survive source/cache removal. Require marker-based updates, stale managed-file cleanup, conflict refusal, cross-plugin isolation, and read-only drift checking. Do not retain obsolete agents for compatibility.

Add or adapt meaningful coverage that exercises the actual plugin resources and temporary install destinations so a passing synthetic unit suite cannot conceal a dangling manual or a retained orchestration core. Test clean installation, stale managed role/reference removal, and preservation of unmanaged and other-plugin files. Stale-file cleanup is installation hygiene, not support for the old roles. Never use the live `~/.codex/agents/` as a test target.

The planned changed areas are the four canonical skills, two bootstrap skills, two installation skills, their relevant references/resources, new-system agent manuals, managed resource inventories, installer and bootstrap coverage, README and plugin presentation, the targeted library convention file, and this repository's board/forge declarations, plus deletion of obsolete plugin contents. Board/forge changes remove role coupling while preserving operation-level authority and project bindings; this spec does not authorize new external permissions, changes to research content, marketplace registration, or release versions. When a release is later requested, account for the breaking removal with a plain semantic major-version change.

## Acceptance criteria and validation

The implementation must satisfy the following observable outcomes. A fresh validator evaluates the implementation against this spec; no validation work is performed by its production owner.

| ID | Required outcome | Evidence |
| --- | --- | --- |
| A1 | Exactly the eight specified custom-agent definitions are produced: coder/qa/writer/auditor in engineering and researcher/librarian/scribe/clerk in library, independently installable. | Temporary installation using actual source resources; inspect generated names and manuals. |
| A2 | Every installed agent is a bounded leaf; the researcher does not compile a skill or launch a crew. | Inspect compiled instructions and exercise a bounded source-question assignment. |
| A3 | Writer and scribe can draft their respective specs without recursive spec prerequisites; coder implementation and nontrivial scribe persistence require validated scope. | Separate engineering/research spec-drafting and missing-spec scenario exercises. |
| A4 | Production agents author artifacts and tests but do not run validation or certify completion. | Exercise an implementation assignment requesting test coverage; inspect actions and returned unexecuted checks. |
| A5 | Each validation and revalidation uses a new report-only agent, including documentation and optional mechanical checks. | Trace specification, implementation, and corrected-candidate scenarios. |
| A6 | Borderline tasks can start on the lower capable tier, while escalation does not add attempts. | Dispatch-policy inspection and a bounded failure/escalation scenario. |
| A7 | A third failed solution attempt stops work across workers and gates. | Scenario with failures shared across a spec and implementation; no fourth attempt. |
| A8 | `ask` performs no internet requests or library writes and maintains only its separate operational ledger; its librarian remains read-only; a fresh clerk validates the answer. | Existing-library fixture with an evidence gap; return a cited draft or bounded gap. |
| A9 | New research uses the configured provider and preserves retrieved evidence and uncertainty. | Available-source and unavailable-provider scenarios, including an unfetched lead. |
| A10 | Researchers return source evidence; raw-note scribes have disjoint paths, and only the main agent or its sole designated scribe updates synthesis and shared metadata. | Two bounded source assignments followed by assigned persistence, integration, and fresh clerk validation. |
| A11 | Project and bootstrap library conventions support owner integration without changing existing evidence; missing setup is reported without implicit scaffolding. | Targeted convention diff, synthesis fixture, and missing-library scenario. |
| A12 | Only the eight specified skill directories remain: four normal entry points, two bootstrap skills, and two installation utilities; no aliases, old pipelines, compatibility flags, or stale links remain. | Package inventory and discovery inspection; inspect current README and representative missing-binding outcomes. |
| A13 | Missing production agents permit direct scoped work; missing required validators are reported and never replaced with main-agent validation. | Two capability-availability scenarios. |
| A14 | The improvement/feedback mechanism is absent from distributed and compiled instructions. | Semantic inspection of surviving plugin text and temporary generated agents, with targeted searches. |
| A15 | Installation removes stale managed definitions/references and preserves unmanaged and other-plugin files. | Temporary stale-file test, conflict test, and installed-state comparison. |
| A16 | Skills, plugin packaging, references, and installer behavior remain valid. | All skill quick validators, both plugin validators, both installer test suites and actual-resource checks. |
| A17 | QA and auditor have clear validation scopes without imposing two final gates on every change. | Code-change and documentation-only scenarios, each using a suitable fresh final reviewer; mixed scope splits only when needed. |
| A18 | Engineering bootstrap creates board and forge declarations from project facts and user choices without performing the declared external operations. | Clean-project, no-board/no-forge, missing-choice, and non-destructive rerun scenarios with fresh spec/artifact audits. |
| A19 | Library bootstrap creates a usable scaffold once and preserves content on rerun; research consumes conventions without loading or running bootstrap. | Empty-library and existing-library fixtures, optional Obsidian fixture, and ordinary research trace. |
| A20 | Current and generated board/forge declarations contain operation-based authority without specific agents or skills, while preserving project permissions and destinations. | Compare operation semantics before/after normalization; exercise an authorized card/PR request and a restricted operation using the new declarations. |
| A21 | Agent installation introduces no certification, verification-pending, or mandatory post-reload gate; requested diagnostics remain freshly delegated. | First-install instructions and normal task trace, plus an explicit drift-check scenario. |

Use fresh validators to run repository-required mechanical checks: skill quick validation for every skill directory, then plugin validation for both roots, followed by both installer test suites and temporary actual-resource installation checks. Dependencies are Python 3.11+ and the validators' required packages, including PyYAML; report actual unavailable prerequisites rather than claiming success.

Keep scenario exercises bounded and isolated, using minimal fixtures and controlled tool availability. They may be grouped by a compatible candidate and validation scope; do not require a new worker per command. Report instruction coverage separately from behavior actually exercised. Do not claim runtime-enforced retry limits, universally optimal model choices, or checks that were only proposed.

For this specification-only task, validation covers readiness, consistency with user requirements and the current repository, local links, document integrity, and required repository validators. Implementation scenarios above remain pending until the implementation task.

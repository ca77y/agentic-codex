# ca77y-agentic for Codex

This repository implements the ca77y agentic toolkit as two native Codex plugins using Codex skills, first-class custom subagents, and collaboration primitives.

## Plugins

### `ca77y-engineering`

An idea-to-open-PR pipeline:

`analyst → writer → auditor → junior-coder or senior-coder → qa → writer → auditor → lead handoff`

- `analyst` shapes board-ready stories and runs product-fit checks.
- `lead` orchestrates one task, one worktree, one branch, and one PR.
- `board` authors or inspects `docs/BOARD.md`, the declaration for tracker bindings and write authority.
- `forge` authors or inspects `docs/FORGE.md`, the declaration for git, remote, PR, and review bindings.
- `writer`, `auditor`, `junior-coder`, `senior-coder`, and `qa` are first-class Codex custom subagents. The two coder tiers share one source manual; their names and model routing remain distinct.

Documentation is part of the candidate judged by final acceptance. Later changes repeat the checks they invalidate before handoff.

The pipeline never guesses a board or forge. A missing board means trackerless operation; a missing `docs/FORGE.md` stops the lead before any branch, worktree, or remote write.

### `ca77y-library`

A project-local Markdown research crew:

- `bootstrap` creates the fixed `library/` structure and its `AGENTS.md` guidance.
- `researcher` runs deep dives and orchestrates bounded parallel research.
- `librarian`, `scribe`, and `clerk` are isolated, agent-only roles: they answer from the wiki, persist research, and audit library health without appearing as callable skills.

The library plugin is standalone. Engineering uses it when installed and falls back to reading wiki pages directly when it is absent.

## Codex-native orchestration

User workflows live in discoverable skills; leaf procedures live under `agents/`. Core manuals hold the normal workflow and essential constraints. Mode-specific procedures and edge cases live in references with explicit conditions for reading them.

The managed installer embeds only the core manual in each TOML's `developer_instructions`. It copies references beneath `~/.codex/agents/.ca77y-engineering/` or `.ca77y-library/` and supplies their absolute base path. Agents read a reference only when its condition applies. Installed references remain available independently of the source checkout or plugin cache.

Orchestrators use `spawn_agent` with the configured custom-agent name, explicit model and effort, `fork_turns: "none"`, and a self-contained task. They continue workers with `followup_task` and collect final reports with `wait_agent`. A missing required agent is reported rather than replaced by a generic worker.

The engineering lead assigns edit paths and tells workers about any concurrent owners. It sequences work when ownership is unclear. Workers preserve unexplained changes and return process feedback in their reports; the coordinator records useful feedback once.

Skills appear in the workflow catalog. Custom agents appear in the app's **Subagents** activity when spawned.

Installed custom-agent names:

- Engineering: `ca77y_engineering_writer`, `ca77y_engineering_auditor`, `ca77y_engineering_junior_coder`, `ca77y_engineering_senior_coder`, and `ca77y_engineering_qa`.
- Library: `ca77y_library_researcher`, `ca77y_library_librarian`, `ca77y_library_scribe`, and `ca77y_library_clerk`.

The model ladder is:

| Tier | Codex model |
| --- | --- |
| high-capability | `gpt-5.6-sol` |
| balanced | `gpt-5.6-terra` |
| fast | `gpt-5.6-luna` |

The user-owned `--fast` flag makes the orchestrator pass a model one tier lower to the same custom-agent name while preserving its reasoning effort. There are no duplicate fast agent definitions.

## Install locally

Add this repository's marketplace, then install either or both plugins:

```bash
codex plugin marketplace add /Users/catty/Workspace/agentic-codex
codex plugin add ca77y-engineering@personal
codex plugin add ca77y-library@personal
```

Install the plugins' custom subagents with Python 3.11 or newer:

```bash
python3 plugins/ca77y-engineering/skills/install-subagents/scripts/install_agents.py
python3 plugins/ca77y-library/skills/install-subagents/scripts/install_agents.py
```

Run the same commands after updating the source. Add `--check` to validate source without installing, or `--check-installed` to check whether installed definitions and references match it. The installer updates only files it owns and refuses conflicts with unmanaged files.

Start a new Codex task after installation so both the plugin skills and custom-agent catalog reload. Invoke orchestrator skills by their qualified names, for example `$ca77y-engineering:lead` or `$ca77y-library:researcher`, or describe the matching task naturally. The orchestrators then dispatch agents such as `ca77y_engineering_writer`, `ca77y_engineering_qa`, and `ca77y_library_researcher`.

## Validate

```bash
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-engineering
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-library
```

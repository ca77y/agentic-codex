# ca77y-agentic for Codex

This repository rebuilds the ca77y agentic toolkit as two native Codex plugins. The source capabilities are preserved, but Claude-only agent manifests, path variables, tool calls, and model names are replaced with Codex skills, first-class custom subagents, and collaboration primitives.

## Plugins

### `ca77y-engineering`

An idea-to-open-PR pipeline:

`analyst → writer → auditor → junior-coder or senior-coder → qa → auditor → writer → lead handoff`

- `analyst` shapes board-ready stories and runs product-fit checks.
- `lead` orchestrates one task, one worktree, one branch, and one PR.
- `board` authors or inspects `docs/BOARD.md`, the declaration for tracker bindings and write authority.
- `forge` authors or inspects `docs/FORGE.md`, the declaration for git, remote, PR, and review bindings.
- `writer`, `auditor`, `junior-coder`, `senior-coder`, and `qa` are first-class Codex custom subagents whose operating manuals are the matching role skills.

The pipeline never guesses a board or forge. A missing board means trackerless operation; a missing `docs/FORGE.md` stops the lead before any branch, worktree, or remote write.

### `ca77y-library`

A project-local Markdown research crew:

- `bootstrap` creates the fixed `library/` structure and its `AGENTS.md` guidance.
- `researcher` runs deep dives and orchestrates bounded parallel research.
- `librarian` answers from the local wiki with provenance.
- `scribe` persists raw notes and synthesized wiki pages.
- `clerk` audits duplicates, broken links, citations, tags, and library hygiene.

The library plugin is standalone. Engineering uses it when installed and falls back to reading wiki pages directly when it is absent.

## Codex-native orchestration

Each former Claude agent has two Codex-native parts:

- a standalone custom-agent TOML, installed under `~/.codex/agents/`, which gives the subagent its stable name, model, reasoning effort, and identity;
- a plugin role skill under `skills/<role>/SKILL.md`, which supplies the detailed operating procedure and packaged references.

Orchestrators spawn those named custom subagents, continue resumable workers with `followup_task`, and collect final reports with `wait_agent`. They explicitly refuse to replace a missing named agent with a generic worker.

The plugin/skill catalog at the top of a Codex task still lists the packaged skills; that catalog is not the subagent registry. The installed TOML definitions are selected through `spawn_agent`'s agent type and appear in the app's **Subagents** activity only after a role is spawned.

Installed custom-agent names:

- Engineering: `ca77y_engineering_writer`, `ca77y_engineering_auditor`, `ca77y_engineering_junior_coder`, `ca77y_engineering_senior_coder`, and `ca77y_engineering_qa`, plus the writer, auditor, senior-coder, and QA `*_fast` variants.
- Library: `ca77y_library_researcher`, `ca77y_library_librarian`, `ca77y_library_scribe`, and `ca77y_library_clerk`, plus `ca77y_library_clerk_fast`.

The translated model ladder is:

| Tier | Codex model |
| --- | --- |
| high-capability | `gpt-5.6-sol` |
| balanced | `gpt-5.6-terra` |
| fast | `gpt-5.6-luna` |

The user-owned `--fast` flag steps a role down one model tier while preserving its reasoning effort.

## Install locally

Add this repository's marketplace, then install either or both plugins:

```bash
codex plugin marketplace add /Users/catty/Workspace/agentic-codex
codex plugin add ca77y-engineering@personal
codex plugin add ca77y-library@personal
```

Install the plugins' custom subagents:

```bash
python3 plugins/ca77y-engineering/skills/install-subagents/scripts/install_agents.py
python3 plugins/ca77y-library/skills/install-subagents/scripts/install_agents.py
```

Start a new Codex task after installation so both the plugin skills and custom-agent catalog reload. Invoke orchestrator skills by their qualified names, for example `$ca77y-engineering:lead` or `$ca77y-library:researcher`, or describe the matching task naturally. The orchestrators then dispatch agents such as `ca77y_engineering_writer`, `ca77y_engineering_qa`, and `ca77y_library_researcher`.

## Validate

```bash
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-engineering
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-library
```

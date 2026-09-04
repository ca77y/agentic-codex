# ca77y-agentic for Codex

This repository implements the ca77y agentic toolkit as two native Codex plugins using Codex skills, first-class custom subagents, and collaboration primitives.

## Plugins

### `ca77y-engineering`

An idea-to-open-PR pipeline:

`analyst → writer → auditor → junior-coder or senior-coder → qa → auditor → writer → lead handoff`

- `analyst` shapes board-ready stories and runs product-fit checks.
- `lead` orchestrates one task, one worktree, one branch, and one PR.
- `board` authors or inspects `docs/BOARD.md`, the declaration for tracker bindings and write authority.
- `forge` authors or inspects `docs/FORGE.md`, the declaration for git, remote, PR, and review bindings.
- `writer`, `auditor`, `junior-coder`, `senior-coder`, and `qa` are isolated first-class Codex custom subagents. They are not callable skills; their complete operating manuals are embedded in their installed agent definitions.

The pipeline never guesses a board or forge. A missing board means trackerless operation; a missing `docs/FORGE.md` stops the lead before any branch, worktree, or remote write.

### `ca77y-library`

A project-local Markdown research crew:

- `bootstrap` creates the fixed `library/` structure and its `AGENTS.md` guidance.
- `researcher` runs deep dives and orchestrates bounded parallel research.
- `librarian`, `scribe`, and `clerk` are isolated, agent-only roles: they answer from the wiki, persist research, and audit library health without appearing as callable skills.

The library plugin is standalone. Engineering uses it when installed and falls back to reading wiki pages directly when it is absent.

## Codex-native orchestration

User entry points and orchestration live in discoverable plugin skills. Leaf execution roles do not: each lives under the plugin's separate `agents/` tree with a non-discoverable `AGENT.md` source manual, and the managed installer compiles that manual plus every role reference into the installed TOML's `developer_instructions`.

Orchestrators spawn those named, self-contained custom subagents with an explicit model and reasoning effort, continue resumable workers with `followup_task`, and collect final reports with `wait_agent`. Fresh custom-agent dispatches use `fork_turns: "none"` and a self-contained task instead of copying the main conversation. The parent sees only the agent's routing metadata; the full worker procedure exists only in the child context. Orchestrators explicitly refuse to replace a missing named agent with a generic worker.

Before deliberately overlapping workers in one story worktree, the engineering lead records each live worker's planned edit paths and tells every new or resumed worker what the others are expected to edit. If it cannot name those paths, it sequences the dispatches. The five engineering delivery workers preserve and report modifications outside their assigned work instead of reverting them, and they verify a tool-attribution claim before recording it as fact. Workers act on the notice they receive; the lead remains responsible for detecting and deciding concurrency.

The plugin/skill catalog at the top of a Codex task lists only user-callable workflows and orchestrators; it is not the subagent registry. The installed TOML definitions are selected through `spawn_agent`'s agent type and appear in the app's **Subagents** activity only after a role is spawned.

Installed custom-agent names:

- Engineering: `ca77y_engineering_writer`, `ca77y_engineering_auditor`, `ca77y_engineering_junior_coder`, `ca77y_engineering_senior_coder`, and `ca77y_engineering_qa`.
- Library: `ca77y_library_researcher`, `ca77y_library_librarian`, `ca77y_library_scribe`, and `ca77y_library_clerk`.

The translated model ladder is:

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

---
name: install-subagents
description: Install or refresh ca77y-engineering's first-class Codex custom subagents under `~/.codex/agents/`. Use after plugin installation or when the agent definitions change. Validates managed TOML files and never overwrites an unrelated agent definition.
---

# Install ca77y engineering subagents

This plugin carries first-class Codex custom-agent source metadata plus non-discoverable manuals under the plugin's separate `agents/` tree because plugin manifests do not install custom agents directly. The installer compiles each complete manual and every role reference into one self-contained TOML under the personal Codex agent directory.

## Workflow

1. From this skill directory, run `python3 scripts/install_agents.py --check`.
2. If validation passes, run `python3 scripts/install_agents.py --ledger-path <absolute-story-worktree>/tmp/ledger.md`. The installer appends the source revision, per-agent install result, managed names, and content fingerprints to that ledger; it is the producer of the refresh proof, not the invoking lead's memory.
3. Confirm that the installer reported the ledger path and that its refresh-proof entry was written. Only then start a new Codex task, carrying the same absolute story-worktree and ledger paths. The replacement lead reads that proof and appends `post-install new-task confirmation` before its first dispatch; a prompt-local acknowledgment never substitutes for either record.

The installer validates that source metadata contains no model, reasoning, or `developer_instructions` override; those are owned by the orchestrator and compiler. It may update files carrying this plugin's `managed-by` marker and remove marked definitions that the plugin no longer ships. It must refuse a same-named file it does not own and must never remove an unmarked definition. Never edit `~/.codex/config.toml` as part of this workflow.

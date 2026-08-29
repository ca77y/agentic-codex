---
name: install-subagents
description: Install or refresh ca77y-library's first-class Codex custom subagents under `~/.codex/agents/`. Use after plugin installation or when the agent definitions change. Validates managed TOML files and never overwrites an unrelated agent definition.
---

# Install ca77y library subagents

This plugin carries first-class Codex custom-agent definitions as resources because plugin manifests do not install custom agents directly. Install them into the personal Codex agent directory so they are available across projects.

## Workflow

1. From this skill directory, run `python3 scripts/install_agents.py --check`.
2. If validation passes, run `python3 scripts/install_agents.py`.
3. Report every installed or unchanged agent and tell the user to start a new Codex task so the custom-agent catalog reloads.

The installer may update files carrying this plugin's `managed-by` marker. It must refuse a same-named file it does not own. Never edit `~/.codex/config.toml` as part of this workflow.

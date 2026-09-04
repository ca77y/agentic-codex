---
name: install-subagents
description: Install or refresh ca77y-engineering's first-class Codex custom subagents under `~/.codex/agents/`. Use after plugin installation or when the agent definitions change. Validates managed files and never overwrites unrelated content.
---

# Install engineering subagents

Requires Python 3.11 or newer. The installer embeds each agent's core manual in its TOML and copies role references into `~/.codex/agents/.ca77y-engineering/<resource-stem>/references/`. The agent reads those files only when its procedure calls for them. Installed references survive removal of the source checkout or plugin cache.

## Workflow

1. From this skill directory, run `python3 scripts/install_agents.py --check`.
2. If validation passes, run `python3 scripts/install_agents.py`.
3. Report installed, unchanged, and removed files. Start a new Codex task to reload the custom-agent catalog.

For a read-only comparison with installed files, run `python3 scripts/install_agents.py --check-installed`. For a temporary installation, supply `--target /absolute/test/directory`. Run focused installer tests with `python3 scripts/test_install_agents.py`.

Source metadata accepts only `name`, `description`, and `manual`; model, reasoning, and instruction overrides are rejected. Each plugin installs independently. The installer updates or removes only files with its ownership marker and refuses unmanaged destination conflicts before writing. Unmanaged files and other plugins' agents are preserved. Never edit `~/.codex/config.toml` as part of this workflow.

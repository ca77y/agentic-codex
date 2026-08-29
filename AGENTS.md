# Repository instructions

This repository contains the Codex-native rebuild of the ca77y agentic toolkit.

## Layout

- `.agents/plugins/marketplace.json` is the repo-local marketplace catalog.
- `plugins/ca77y-engineering/` contains the delivery-pipeline skills.
- `plugins/ca77y-library/` contains the research-library skills and bootstrap resources.

## Editing rules

- Keep each plugin name identical across its folder, marketplace entry, and `.codex-plugin/plugin.json`.
- Put every callable role's operating procedure in `skills/<role>/SKILL.md`.
- Put distributable custom-agent TOML resources under the plugin's `install-subagents/resources/`, then install them into `~/.codex/agents/` with the managed installer. Plugin manifests do not install project or personal custom agents directly.
- Keep role-specific references under that role's skill directory and use relative paths from `SKILL.md`.
- Orchestrators must dispatch the configured custom-agent name, never a generic worker standing in for a missing role. Use Codex collaboration terms and tools: `spawn_agent`, `followup_task`, `wait_agent`, and worker targets.
- Do not reintroduce `CLAUDE.md`, `.claude-plugin`, `${CLAUDE_PLUGIN_ROOT}`, Claude model names, or Claude-only tool calls.

## Validation

Run the skill quick validator for every skill directory, then run the plugin validator for both plugin roots. After a marketplace-backed update, use the plugin-creator cachebuster and reinstall flow.

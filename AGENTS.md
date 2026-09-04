# Repository instructions

This repository contains the Codex-native rebuild of the ca77y agentic toolkit.

## Layout

- `.agents/plugins/marketplace.json` is the repo-local marketplace catalog.
- `plugins/ca77y-engineering/` contains the delivery-pipeline skills.
- `plugins/ca77y-library/` contains the research-library skills and bootstrap resources.
- `library/` contains the Markdown research wiki, raw sources, synthesis, and metadata.

## Editing rules

- Keep each plugin name identical across its folder, marketplace entry, and `.codex-plugin/plugin.json`.
- Put every user-callable workflow and orchestrator in `skills/<role>/SKILL.md`.
- Put an isolated leaf custom-agent's operating procedure in `agents/<role>/AGENT.md`; never put an agent-only role under `skills/`. The managed installer compiles that manual and its references into the installed agent TOML.
- Put distributable custom-agent TOML resources under the plugin's `install-subagents/resources/`, then install them into `~/.codex/agents/` with the managed installer. Plugin manifests do not install project or personal custom agents directly.
- Keep role-specific references beside the owning `SKILL.md` or `AGENT.md` and use relative paths from that manual.
- Add code comments only when the code itself cannot clearly explain the behavior or rationale; do not narrate self-explanatory code.
- Keep documentation focused on the system as it exists now. It may briefly identify gaps or future plans, but it is neither a historical record nor a record of the discussions that led to a decision.
- Orchestrators must dispatch the configured custom-agent name, never a generic worker standing in for a missing role. Use Codex collaboration terms and tools: `spawn_agent`, `followup_task`, `wait_agent`, and worker targets.
- Use Codex-native manifests, path conventions, model names, and tool calls throughout the repository.

## Validation

Run the skill quick validator for every skill directory, then run the plugin validator for both plugin roots. After a marketplace-backed update, use the plugin-creator cachebuster and reinstall flow.

## Library

Read `library/_meta/librarian.md` before library work. Preserve raw notes and cite durable claims back to sources; no always-on service is required for the library to work.

# Agent version metadata patch releases

ca77y-engineering 3.0.1 and ca77y-library 2.0.1 add source-version comments to
installed agent definitions and Markdown references. Each installer reads the
version from its plugin's `.codex-plugin/plugin.json`; this manifest is the single
source of truth documented in the root `AGENTS.md`.

The `managed-by` marker remains unchanged, so unversioned installations upgrade
normally. Version-only changes appear in `--check-installed`; rerunning the
installer refreshes the comments. Version metadata adds no agent runtime fields.

After updating plugin source, run its `skills/install-subagents/scripts/install_agents.py`
with Python 3.11 or newer, then start a new Codex task to reload the agent catalog.

These patch releases package the behavior specified in
`docs/specs/agent-install-version-metadata.md`. Publication is authorized for this
change; the implementation specification's local-only endpoint does not limit
this release. Validation covers both installer suites, every skill directory,
both plugin manifests, and the root release instructions.

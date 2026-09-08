---
name: install-subagents
description: Install or refresh ca77y-library's managed Codex custom agents and their supporting references. Use after plugin installation or agent-definition updates.
---

# Install ca77y-library agents

## Ledger ownership

On every invocation, open or create the run's durable ledger using the [ledger procedure](../research/references/ledger.md) and [template](../research/assets/ledger.md) before production or delegation. The main agent is its sole writer, including for trivial work and runs without subagents. Record returned subagent IDs/canonical handles, assignments and progress; update before dispatch and waits, immediately after dispatch, on results and gate/failure changes, and before handoff or the final response. Reuse the ledger on resume and across entry points within the same run, preserving its failure history. A separate later user request gets a new run ledger; prior run history remains context, not its attempt count. Link the ledger in the final response.

## Installation

Requires Python 3.11 or newer. From this skill directory run `python3 scripts/install_agents.py`. Report the installer’s installed, unchanged, and removed files. Start a new Codex task to reload the custom-agent catalog; normal use can then dispatch the available roles. This installs researcher, librarian, scribe, and clerk.

The installer embeds each leaf's core `AGENT.md` and copies references into `~/.codex/agents/.ca77y-library/<resource-stem>/references/`, preserving paths after source/cache removal. References load only when their core procedure calls for them. Source metadata contains only the managed marker, `name`, `description`, and `manual`; generated definitions have no fixed model or reasoning fields.

Generated definitions include a `# plugin-version: <version>` comment after the ownership marker; copied references include `<!-- plugin-version: <version> -->`. The version comes from `.codex-plugin/plugin.json` and must be plain `major.minor.patch`. It identifies the source manifest release, not a content digest. Ownership remains independent of version, so existing unversioned files upgrade normally and version-only changes are reported by `--check-installed`.

Marker-based updates and stale-file cleanup affect only this plugin’s owned files. Unmanaged conflicts are refused before writes; other-plugin and unmanaged files are preserved. Do not edit `~/.codex/config.toml`.

## Requested diagnostics

For explicit diagnostics or plugin development, `--check` parses source without installing, `--check-installed` reports drift without writes, and `--target /absolute/temporary/directory` selects an isolated destination. `python3 scripts/test_install_agents.py` exercises the installer. These diagnostics are optional and are not installation steps. If requested through this workflow, delegate their evaluation to a fresh `ca77y_library_clerk` with `fork_turns: "none"`; never use the live agent directory as a test target.

Choose an available model and supported effort for that bounded diagnostic according to complexity; between plausible tiers start on the lower capable tier. Give the validator the actual source, target, scope, and remaining shared attempt allocation, without an expected verdict. It reports pass/fail/unverified without repair. Corrections go to production and require a new validator. The budget covers one run from the initiating user prompt through resolution of that request, not the lifetime of a PR or artifact. A separate later request starts a new run with its own budget; reviewing comments or discovering defects does not itself consume attempts. Continuations and interruptions of the same unfinished run retain its count. Track at most three failed solution attempts for the same unresolved outcome across the main agent, workers, specification, implementation, validation, models, and resumptions; escalation never resets that count and a third failure stops the entire run. Installation itself reports its result without claiming an independent audit.

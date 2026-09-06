# ca77y agentic toolkit for Codex

Two independently installable plugins provide four normal entry points. The main agent owns the requested outcome, evidence, dynamic model selection, and a shared limit of three failed solution attempts for an unresolved problem.

| Plugin | Normal work | One-time setup | Supporting agents |
| --- | --- | --- | --- |
| Engineering | `shape` produces proposals/specs; `deliver` implements or repairs through the authorized local, commit, or PR endpoint. | `bootstrap` creates or completes board and forge declarations. | coder, QA, writer, auditor |
| Library | `research` investigates and saves cited evidence; `ask` answers from existing library knowledge without internet requests or library writes. | `bootstrap` creates or safely completes the Markdown library; Obsidian is optional. | researcher, librarian, scribe, clerk |

Both plugins also provide `install-subagents`. Nontrivial changes require a written spec and fresh validation before production, then a different fresh validator for the candidate. Trivial changes can skip the written spec but still require fresh validation. Production delegation is optional. Missing production roles permit direct scoped work; missing required validators block the affected gate.

Engineering uses a fresh auditor for spec readiness and document acceptance, or fresh QA for code behavior and tests. One adequate final evaluation can include affected documentation and mechanical checks. Library uses fresh clerks for research specs, answers, evidence, and integrity. Production leaves author artifacts and tests; validators report findings and execute checks without repairing the candidate.

Researchers return new-source findings and provenance. Librarians retrieve existing knowledge read-only. The main agent or one designated scribe integrates synthesis and shared metadata after raw-note writers finish. Research follows project conventions and the configured provider; this repository requires `webtools` for internet research and reports its absence without provider substitution.

Every entry point, including bootstrap and installation, keeps a durable ledger owned by the main agent. It records progress, returned subagent IDs/canonical handles, assignments, gate evidence, and failure history before waits and handoffs. Reuse it across skills and resumptions. Project ledgers use `<temp-folder>/ledgers/<run-id>.md`, with the temp folder read from the forge declaration (normally `docs/FORGE.md`) and defaulting to `.tmp/` under the project root. Without a project, use `$CODEX_HOME/ledgers/` (default `~/.codex/ledgers/`). Keep ledgers outside the research library and installed plugin caches, and preserve them through scratch cleanup and completion. Each plugin ships a template: [engineering](plugins/ca77y-engineering/skills/deliver/assets/ledger.md) and [library](plugins/ca77y-library/skills/research/assets/ledger.md).

Project authority lives in [`docs/BOARD.md`](docs/BOARD.md), [`docs/FORGE.md`](docs/FORGE.md), and [`library/_meta/librarian.md`](library/_meta/librarian.md). A local implementation request does not imply commits or publication; a proposal does not imply filing a card. Normal work consumes setup without running bootstrap.

## Install locally

Add this repository's marketplace, then install either or both plugins:

```bash
codex plugin marketplace add /Users/catty/Workspace/agentic-codex
codex plugin add ca77y-engineering@personal
codex plugin add ca77y-library@personal
```

Install the selected plugins' custom agents with Python 3.11 or newer:

```bash
python3 plugins/ca77y-engineering/skills/install-subagents/scripts/install_agents.py
python3 plugins/ca77y-library/skills/install-subagents/scripts/install_agents.py
```

Run the same installer after source updates. It embeds each leaf's `agents/<role>/AGENT.md` and copies conditional references under `~/.codex/agents/.ca77y-engineering/` or `.ca77y-library/`, so installed references survive checkout/cache removal. Only marked files are updated or removed; unmanaged conflicts are refused and other-plugin files are preserved. Agent definitions contain no fixed model or reasoning settings.

Start a new Codex task after installation to reload skills and the custom-agent catalog. `deliver` requires explicit invocation, such as `$ca77y-engineering:deliver`, and is never selected automatically. Other skills can be invoked by their qualified name, such as `$ca77y-library:research`, or by describing matching work naturally. Engineering dispatches `ca77y_engineering_coder`, `ca77y_engineering_qa`, `ca77y_engineering_writer`, and `ca77y_engineering_auditor`. Library dispatches `ca77y_library_researcher`, `ca77y_library_librarian`, `ca77y_library_scribe`, and `ca77y_library_clerk`.

## Development validation

Diagnostics are optional installation utilities: `--check` inspects source without installing; `--check-installed` reports read-only drift; `--target` selects a temporary destination. Checks requested through a skill are delegated to a fresh engineering auditor or library clerk.

Use Python 3.11 or newer with PyYAML available. Run every skill quick validator, then both plugin validators and installer suites:

```bash
(
  for skill in plugins/*/skills/*/; do
    python3 /Users/catty/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill" || exit $?
  done
  python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-engineering || exit $?
  python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-library || exit $?
  python3 plugins/ca77y-engineering/skills/install-subagents/scripts/test_install_agents.py || exit $?
  python3 plugins/ca77y-library/skills/install-subagents/scripts/test_install_agents.py || exit $?
)
```

The installer suites exercise real plugin resources and isolated destinations, including stale cleanup, unmanaged conflicts, drift, and reference survival after source removal. Mechanical checks establish format and packaging validity; bounded scenarios assess instruction behavior separately. The acceptance sources are [supporting agents and skill integration](docs/specs/plugin-specialists-and-skill-integration.md) and [orchestrator ledgers](docs/specs/orchestrator-ledgers.md).

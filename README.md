# ca77y-agentic for Codex

Two independently installable Codex plugins provide four recommended entry points. Describe the desired outcome naturally or invoke its qualified skill name.

| Plugin | Entry point | Outcome |
| --- | --- | --- |
| `ca77y-engineering` | [`shape`](plugins/ca77y-engineering/skills/shape/SKILL.md) | A scoped proposal or specification with observable acceptance criteria. |
| `ca77y-engineering` | [`deliver`](plugins/ca77y-engineering/skills/deliver/SKILL.md) | An implemented or repaired change through the requested, authorized local, commit, or PR endpoint. |
| `ca77y-library` | [`research`](plugins/ca77y-library/skills/research/SKILL.md) | New investigation with reusable source evidence and cited synthesis saved in the library. |
| `ca77y-library` | [`ask`](plugins/ca77y-library/skills/ask/SKILL.md) | An answer grounded in the existing library, with gaps and uncertainty made explicit. |

The main agent owns the outcome and chooses production activities. A proposal does not authorize implementation; a local change does not imply publication; an existing-library answer does not initiate research or maintenance. Explicitly combined requests compose within one task. Engineering can work without a library, and library can work without engineering.

## Evidence and delegation

Every nontrivial change follows written specification and fresh validation, then implementation and another fresh validation. Existing specs can be reused after validation of current fit. Every audit or validation—including tests, mechanical checks, citations, and optional formatting checks—uses a newly spawned report-only validator with no prior participation in the work. Corrected candidates require another fresh validator. Trivial changes can omit a written spec but still need fresh validation. Answer-only work needs no written spec.

Each plugin supplies its own validator: `ca77y_engineering_validator` and `ca77y_library_validator`. These leaves evaluate the assigned artifacts and run checks without editing the candidate or requiring legacy pipeline artifacts. Their procedures live at `agents/validator/AGENT.md`, with distributable TOML resources under `skills/install-subagents/resources/`.

New entry points select a currently available model and supported reasoning effort for each delegated responsibility, with a brief rationale. Borderline work starts with the lower capable tier; demanding work may start stronger. Custom-agent definitions omit fixed model settings. Production can happen directly or through compatible bounded custom agents. Every validator uses `spawn_agent` with its configured name and `fork_turns: "none"`; `followup_task` continues production only, and `wait_agent` collects results.

Three failed solution attempts for the same unresolved outcome stop the entire run across gates, agents, models, and resumptions. The main agent preserves failure evidence and recovery state; another attempt requires explicit user authorization. This is an instruction-level workflow requirement, not a tool-enforced runtime counter.

## Project bindings and supporting workflows

Board and forge operations use `docs/BOARD.md` and `docs/FORGE.md` only when needed. Missing bindings block that operation while allowing authorized preparation. Role-specific grants to `analyst`, `writer`, or `lead` do not transfer to `shape` or `deliver`. This repository's declarations still name legacy roles, so the new entry points cannot use those grants for external writes until an authorized binding update makes them explicit.

Engineering's `board` and `forge` skills author or inspect declarations. Library's `bootstrap` creates the Markdown vault and optional Obsidian configuration. Both plugins retain `install-subagents`. Research follows the project's library conventions and configured provider; this repository requires `webtools` for internet research and reports its absence rather than substituting a provider.

User-callable procedures live in `skills/<name>/SKILL.md`; bounded specialist procedures live in `agents/<role>/AGENT.md`. Substantial conditional instructions live beside their owning manual and are loaded only when their stated condition applies. The managed installer embeds core manuals and copies supporting references under `~/.codex/agents/.ca77y-engineering/` or `.ca77y-library/`, so installed references survive removal of the checkout or plugin cache.

## Retained legacy interfaces

`analyst`, `lead`, and `researcher` remain available with their existing behavior while compatibility migration is outside this implementation. They retain their earlier role sequencing and model tables; the four new entry points do not run those workflows. Explicit invocation selects the intended interface while both generations remain discoverable.

The existing engineering agents are `ca77y_engineering_writer`, `ca77y_engineering_auditor`, `ca77y_engineering_junior_coder`, `ca77y_engineering_senior_coder`, and `ca77y_engineering_qa`. The existing library agents are `ca77y_library_researcher`, `ca77y_library_librarian`, `ca77y_library_scribe`, and `ca77y_library_clerk`. Their core procedures remain intact. In particular, the legacy researcher agent embeds an orchestration chain; the new `research` entry point performs source work directly unless a compatible bounded research leaf is configured.

## Install locally

Add this repository's marketplace, then install either or both plugins:

```bash
codex plugin marketplace add /Users/catty/Workspace/agentic-codex
codex plugin add ca77y-engineering@personal
codex plugin add ca77y-library@personal
```

Install the plugins' custom subagents with Python 3.11 or newer:

```bash
python3 plugins/ca77y-engineering/skills/install-subagents/scripts/install_agents.py
python3 plugins/ca77y-library/skills/install-subagents/scripts/install_agents.py
```

Run the same commands after updating the source. Add `--check` to validate source without installing, or `--check-installed` to check whether installed definitions and references match it. The installer updates only files it owns and refuses conflicts with unmanaged files.

Start a new Codex task after installation so both the plugin skills and custom-agent catalog reload. Invoke orchestrator skills by their qualified names, for example `$ca77y-engineering:deliver` or `$ca77y-library:research`, or describe the matching task naturally. The new entry points dispatch `ca77y_engineering_validator` or `ca77y_library_validator` for fresh validation. If a required role is absent from the current catalog, the task reports that unmet condition instead of substituting another role.

## Validate

Use Python 3.11 or newer with PyYAML available. Run the skill quick validator for every directory containing a `SKILL.md`, then both plugin validators:

```bash
for skill in plugins/*/skills/*/; do
  python3 /Users/catty/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill" || break
done
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-engineering
python3 /Users/catty/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/ca77y-library
python3 plugins/ca77y-engineering/skills/install-subagents/scripts/test_install_agents.py
python3 plugins/ca77y-library/skills/install-subagents/scripts/test_install_agents.py
```

When running through a new entry point, delegate these checks to a fresh validator. Mechanical checks establish packaging and format validity; scenario evaluation is needed to assess instruction behavior. The acceptance source and implementation boundary are in [`docs/specs/plugin-redesign-entry-points.md`](docs/specs/plugin-redesign-entry-points.md) and [`docs/specs/plugin-entry-points-implementation.md`](docs/specs/plugin-entry-points-implementation.md).

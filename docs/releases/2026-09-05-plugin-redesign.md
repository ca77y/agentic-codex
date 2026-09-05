# Engineering 3.0.0 and Library 2.0.0

The plugins now use evidence-based workflows with four normal entry points and eight bounded supporting agents. The main agent owns the requested outcome, integration, model selection, and recovery.

| Plugin | Normal skills | Supporting agents |
| --- | --- | --- |
| Engineering 3.0.0 | `shape`, `deliver` | coder, qa, writer, auditor |
| Library 2.0.0 | `research`, `ask` | researcher, librarian, scribe, clerk |

Both plugins also provide a one-time `bootstrap` skill and the `install-subagents` utility. Engineering bootstrap creates project board and forge declarations. Library bootstrap creates the Markdown scaffold and can add requested Obsidian configuration. Reruns preserve existing project content.

Nontrivial changes require a written spec and independent validation before implementation, followed by fresh validation of the result. All audits and checks are delegated to fresh report-only agents. Production agents can author tests; validators execute them. Models and supported reasoning efforts are selected per assignment, with the lower capable tier tried first for borderline complexity. Three failed approaches to the same unresolved outcome stop the whole run, across agents, phases, model changes, and resumptions.

`ask` stays within existing local knowledge. Research separates source retrieval from persistence, preserves provenance and uncertainty, and gives one owner responsibility for synthesis and shared metadata. Project board and forge declarations express operation permissions without depending on specific plugin roles.

## Breaking changes and installation

The old workflow interfaces and agent identities are removed without aliases. Use the entry points above. Separate board/forge setup is replaced by engineering bootstrap; new source investigation uses library research. Agent definitions no longer fix a model or reasoning effort.

Update the installed plugin from the repository marketplace, then run its managed agent installer from the updated repository root:

```bash
python3 plugins/ca77y-engineering/skills/install-subagents/scripts/install_agents.py
python3 plugins/ca77y-library/skills/install-subagents/scripts/install_agents.py
```

Run only the command for each plugin you use. Python 3.11 or newer is required. The installer replaces marked definitions, removes stale managed roles, and preserves unmanaged and other-plugin files. Start a new Codex task to load the updated skills and agent catalog. Installation does not require a separate certification step.

## Audit repairs and evidence

The release audit corrected a broken reference in the QA agent description, made the documented validation recipe preserve failures, and made the installation utilities explicitly carry the shared failure count across the main agent and every phase.

Validation covers all eight skill directories, both plugin manifests, both installer suites, and actual-resource installations in temporary destinations. Installer coverage includes stale-file cleanup, conflict refusal, drift detection, coexistence, and reference survival after source removal. Isolated library scaffold exercises cover preservation on rerun and optional Obsidian merging. Independent instruction review and bounded decision exercises cover the workflow contracts and project authority.

These checks do not establish universal model adherence or a runtime-enforced failure counter. Live end-to-end execution through a reloaded custom-agent catalog and live source-provider calls are not part of this release audit. No live personal agent configuration or research content was changed by the audit.

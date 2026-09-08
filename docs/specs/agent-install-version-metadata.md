# Installed agent version metadata

## Request and outcome

The user wants version metadata in installed plugin agent files so their source
release can be identified without retaining the plugin cache. Apply this to both
ca77y-engineering and ca77y-library.

## Behavior and scope

Read the plugin name and version from `.codex-plugin/plugin.json`. Generated
agent TOML starts with the existing `# managed-by: <name>` line followed by
`# plugin-version: <version>`. Copied Markdown references use the corresponding
two HTML comments: `<!-- managed-by: <name> -->` and
`<!-- plugin-version: <version> -->`. Version means the source manifest version,
not a content digest. Require a plain major.minor.patch version before writes.

Keep the ownership marker unchanged and independent of version, so legacy
unversioned files and files from older versions remain updatable and eligible for
owned stale-file cleanup. Preserve unmanaged and other-plugin files and existing
unsafe-path/conflict protections. Add no TOML runtime settings, source-resource
metadata fields, fixed models, timestamps, or cache paths.

Update both installer implementations, their regression tests, and installation
skill documentation. After independent acceptance, refresh the user's installed
agents using these repository installers, as a continuation of the authorized
installation work. This is local work: no release/version bump, plugin cache
mutation, config.toml change, commit, or publication is requested.

## Acceptance and verification

1. Every generated TOML and copied reference records its source manifest version;
   parsed TOML retains exactly name, description, and developer_instructions.
2. A version-only manifest change changes both output types. Read-only drift
   detection reports that change; reinstall updates it and a repeat is unchanged.
3. Existing unversioned owned files upgrade; stale owned files with and without
   version metadata are removed. Unmanaged and other-plugin files are preserved.
4. Missing or malformed manifest versions fail before destination writes.
5. Both installer suites pass using isolated temporary sources and targets. Run
   the skill quick validator for every repository skill and the plugin validator
   for both plugin roots, as required by AGENTS.md.
6. Installation docs describe metadata and backward-compatible ownership. After
   accepted implementation, production installation reports the affected files;
   no independent live-directory test is required.

Use a fresh auditor for specification readiness and a separate fresh QA agent
for implementation acceptance. Record gate identities/results in a companion
evidence file. Shared failed-attempt count starts at zero, with a limit of three.

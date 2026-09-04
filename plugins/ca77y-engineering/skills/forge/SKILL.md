---
name: forge
description: Help a project write, repair, or inspect its `docs/FORGE.md` declaration — how it uses git and its forge. Invoked by the user by name, never per-run by the `lead`. Never branches, commits, pushes, or opens, updates, or comments on anything.
---

Inspect, write, or repair `docs/FORGE.md`, the project's declaration of git and change publication. This skill manages the declaration; it never performs repository or forge writes. A forge may be a hosted service, a self-hosted system, or explicitly none.

## Choose the requested action

- **Inspect:** read the declaration and report bindings, authority, and gaps. No authoring interview or reference is needed.
- **Write or repair:** when requested by the user, read [authoring FORGE](references/authoring-forge.md), inspect project evidence read-only, then complete and read back the change. Ask only for unresolved material decisions; bundle them.
- **Missing during lead delivery:** the lead stops before creating anything and recommends this skill. Do not author guessed bindings on its behalf. If the user explicitly requests authoring or repair, complete that authorized request.

## Declaration contract

The fixed path is `docs/FORGE.md`. Record repository/remote, target branch, worktree directory and ignore coverage, branch naming, commit convention, push timing, change-description requirements, reviewer/trigger, and exhaustive write authority.

Bind branch, remove-worktree, commit, push, open/update/comment/read-change, re-fire-review, and merge explicitly, or mark each unbound. Missing FORGE stops lead delivery; explicit no-forge or unbound operations are valid declarations. No forge ends delivery at the final commit; no update or review trigger yields a reported manual follow-up, never an invented command.

For an authorized repair of another declaration location, use the authoring reference to move it or add a fixed-path pointer without duplicating bindings. Inspection reports the location gap.

## Boundaries and report

Verify read-only against repository state and an existing change where available. Never branch, create/remove worktrees, commit, push, open/update/comment on changes, trigger review, or merge. Never invent remotes, branches, conventions, commands, or checks. Missing ignore coverage is reported; change an ignore file only if separately authorized. Use configured authentication; never inspect `.env` or output tokens or credentialed URLs.

Report the file path, what it declares or what changed, evidence verified read-only, and material unresolved decisions. Do not require a second invocation to finish an authorized repair.

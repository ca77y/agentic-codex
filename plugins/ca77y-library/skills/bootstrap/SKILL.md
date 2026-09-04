---
name: bootstrap
description: Create a project's non-overwriting library research scaffold, with optional Obsidian configuration. Use before first research or to fill explicitly requested scaffold gaps; does not research, populate wiki pages, or manage project boards.
---

Create the fixed `library/` layout from this skill's `resources/library/`. The library works as plain Markdown and does not require the engineering plugin.

1. Inspect the target library and project README/AGENTS metadata. If the librarian guide already exists, report the existing scaffold; fill gaps only when requested. For a partial scaffold, create missing files within the authorized scope and preserve every existing file. Report conflicting or incomplete existing content instead of repairing it implicitly.
2. Infer project name and research scope from reliable project text or the user's request. Use a neutral “Research for <project>” scope if no domain is established. Start domain tags empty unless supplied or already established in project taxonomy. Bundle genuinely necessary questions; do not reconfirm choices already authorized.
3. Read [scaffold details](references/scaffold.md), copy the missing resource files, and replace tokens in new copies only. Preserve Templater expressions. Inspect the result for unresolved scaffold tokens and valid links/frontmatter using available tools; report any check that cannot run.
4. Link the library from an existing root `AGENTS.md`, merging the resource section without duplication. Do not create a root instruction file merely to add this pointer.
5. Configure Obsidian only when requested or already authorized. Otherwise leave it optional in the report. For that path, read [Obsidian setup](references/obsidian.md).

Do not overwrite library content or existing Obsidian settings. Stay off `docs/`, boards, research content, and agent dispatch; this pass creates a scaffold only. A repair or restructure needs explicit scope, not another bootstrap by implication.

Report files created, existing files preserved and remaining gaps, inferred fields and their sources, root pointer changes, optional Obsidian status, and the next step: `ca77y-library:researcher`.

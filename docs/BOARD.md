# The board

How this project tracks work, read directly at this fixed path — `docs/BOARD.md` — by
every board-touching agent, with no per-run resolution step in between. Keep it true,
because the pipeline binds real calls to what it says.

## The board

**Linear** — the `Agentic Codex` project in the `Smerfy` team (`SMR`).
<https://linear.app/ca77y/project/agentic-codex-f198bf80e38c>

Work is not tracked in this repository. Stories use their `SMR-<number>` identity and
belong to the `Agentic Codex` Linear project.

## Reaching it

The **Linear connector**, already connected in this workspace. Its tools are named
`mcp__codex_apps__linear_*`; no credentials live in this repository.

## Operations

- **locate** — `mcp__codex_apps__linear_get_issue` by identifier (`SMR-200`) or URL;
  `mcp__codex_apps__linear_list_issues` with `project: "Agentic Codex"` and
  `query: <title or slug>` when only a name is known.
- **read** — `mcp__codex_apps__linear_get_issue`, with `includeRelations: true` when
  dependencies matter.
- **search** — `mcp__codex_apps__linear_list_issues` with
  `project: "Agentic Codex"` plus `query`, `state`, `label`, or `priority`.
- **create** — `mcp__codex_apps__linear_save_issue` with `team: "Smerfy"`,
  `project: "Agentic Codex"`, and `state: "Backlog"`.
- **transition** — `mcp__codex_apps__linear_save_issue` with the issue `id` and target
  `state`.
- **comment** — `mcp__codex_apps__linear_save_comment` with the issue identifier as
  `issueId` and a Markdown `body`.
- **update** — `mcp__codex_apps__linear_save_issue` with the issue `id` and only the
  fields being changed (`description`, `labels`, `priority`, `links`, or relations).

## Card shape

A Linear issue. The title is an action-verb story title; the body is Markdown in the
`description` field.

- **Type** — exactly one label: `Bug`, `Improvement`, or `Feature`.
- **Priority** — `1` Urgent · `2` High · `3` Medium · `4` Low.
- **Identity** — the issue identifier (`SMR-200`). It is the stable name across board,
  branch, PR, and spec. A spec uses the lowercase identifier and a concise slug, for
  example `docs/specs/smr-200-writer-spec-pass-board-access.md`. Branch derivation is
  owned by [`FORGE.md`](./FORGE.md).
- **Dependencies** — Linear blocking relations, supplied as `blockedBy` and `blocks` to
  `mcp__codex_apps__linear_save_issue`. There are no sub-issues: one story is one issue
  is one PR.
- **Body** — a summary paragraph, then the applicable sections from `## Why`,
  `## Scope`, `## Out of scope`, `## Acceptance criteria`, and `## References`.
  Sections that do not apply are omitted rather than left empty. The body has no `#`
  heading because the Linear title is the heading.

Acceptance criteria are recorded **one observable behaviour per line** under
`## Acceptance criteria`; the acceptance gate reads and grades them individually.

Linear rewrites `-` bullets to `*` and wraps bare URLs in `<…>` on save. This is a
cosmetic round-trip quirk, not a content change.

## Statuses

`Backlog` · `Todo` · `In Progress` · `In Review` · `Done` · `Canceled` · `Duplicate`.

| From → to | Who | When |
| --- | --- | --- |
| `Backlog` → `Todo` | **human** | the story is refined and ready to start |
| `Todo` → `In Progress` | `lead` | the run starts, at workspace creation |
| `In Progress` → `In Review` | `lead` | the PR is open |
| `In Review` → `Done` | **human** | the work is verified |
| anything → `Canceled` / `Duplicate` | **human** | abandoning or folding work is a product call |

- **work started** → `In Progress` (expect `Todo` before writing)
- **awaiting review** → `In Review` (expect `In Progress` before writing)
- Terminal values — `Done`, `Canceled`, and `Duplicate` — are the human's.

## Visibility

A status write is the Linear call itself and is visible immediately. No checkout is
involved; never write a board transition into a repository, worktree, or branch.

## What the pipeline may write

Permitted and expected:

- **create** — the `analyst` files new issues at `Backlog`.
- **transition** — the `lead` makes only the two middle transitions above.
- **attach the PR** — the `lead` adds the URL returned by [`FORGE.md`](./FORGE.md)'s
  *open the change* binding to the issue through the `links` field.
- **comment** — progress, production hazards, and the handoff summary may be posted to
  the issue.
- **edit card content** — during the writer's spec pass, the description, acceptance
  criteria, labels, priority, and relations may be corrected when the declaration and
  role instructions authorise it. After the acceptance gate passes, the lead may apply
  board follow-ups the writer retained.

The pipeline never moves a status through a human gate. It never changes an acceptance
criterion to match an implementation, and it never changes criteria between the build
and the acceptance gate. A writer may correct a defective criterion during the spec
pass and record the deviation; a criterion found mis-worded during the acceptance gate
is escalated to the human for correction in a later run.

Everything outside the authority listed above — especially terminal states and a
rewrite of the product goal — is the human's. When it is unclear whether an edit is a
correction or a changed goal, the pipeline reports it instead of writing.

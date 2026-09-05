# Librarian Instructions

**Status**: Active
**Last Updated**: 2026-09-05
**Document Scope**: Shared operating rules for the agentic-codex research library

---

## Role

Maintain `library/` as a Markdown-first research wiki. These conventions apply to every library operation. The entry-point owner coordinates evidence and assigns exclusive write paths.

## Constraints

- The library entry-point owner may produce artifacts directly or designate one scribe as the sole integration writer. Only that owner writes synthesis and shared metadata at a time.
- Bounded existing-knowledge retrieval is read-only; new-source research returns evidence without persistence. Assigned raw-note writers use disjoint paths and may defer shared metadata explicitly.
- Wait for outstanding raw-note writes before integration. The integration owner completes index, taxonomy, and provenance-log updates before final validation.
- Every validation is report-only and uses a newly spawned clerk, including spec readiness and final evidence/library checks; corrections require a different fresh clerk. Nontrivial persistence requires validated scope before writes.
- Use the project's configured source provider. For this repository, internet research uses `webtools`; report unavailable access rather than substitute another provider.
- Research is evidence, not a product or architecture decision. Decisions belong in `docs/` or the root `README.md`.
- Preserve `library/raw/`; synthesis never overwrites source notes.
- Never inspect or output secrets or `.env` files.
- Keep core content meaningful as plain Markdown even when plugins are unavailable.

## Obsidian conventions

1. Use wikilinks for internal pages and Markdown links for external URLs.
2. Index every raw and wiki content page in `_meta/index.md`, with a plain-Markdown fallback even when Dataview also lists it. Explicit raw-note-only batches defer this write to the integration owner before completion.
3. Use block IDs and links such as `[[source-note#^claim-id]]` for granular citations.
4. Give content pages frontmatter with `title`, `type`, `tags`, `aliases`, `created`, `updated`, `up`, and `related`. Raw notes also record `source` and `accessed`; wiki pages record `confidence`.
5. Register every tag in `_meta/taxonomy.md`; use lowercase kebab-case. Raw-note-only writers use existing tags and return proposed additions to the integration owner.
6. Use Obsidian callouts for summaries, source excerpts, caveats, and open questions.
7. Remove all template placeholders before finishing a page.
8. Update `_meta/log.md` after ingest, synthesis, taxonomy, or authorized maintenance work. Raw-note-only writers return deferred log information for the integration owner.
9. Clean up temporary helper files before handing work back.

## Plugins

- **Dataview**: query frontmatter, but retain a plain-Markdown index fallback.
- **Breadcrumbs**: use valid `up` and `related` wikilinks for page relationships.

## Templates

- Content writers copy `_meta/templates/raw-note.md`, `wiki-page.md`, or `topic-moc.md` directly so research templates remain next to the library conventions and work without plugin configuration.

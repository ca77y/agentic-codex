# Targeted library checks

Use these when the audited changes or findings involve the corresponding mechanism.

- Resolve wikilinks and embeds to real note paths/basenames or declared aliases. A matching `title` alone is insufficient. Check referenced headings and block IDs as well as the page.
- An anchor's textual presence does not prove valid placement. Paragraph/heading anchors belong at line end; list, quote, callout, and table anchors use a separate blank-line-separated line. Report missing and misplaced anchors distinctly.
- Reconcile index/relationship links against existing pages, and tags against the taxonomy. Check completion claims in the log against the actual named files. Scope negative findings to the set inspected.
- Inspect authored prose for dispatch conditionals, instructions to the writer, and promises about a page's future writing state. Exempt preserved source quotations and templates. Rank the consequence rather than treating every wording issue as critical.
- For duplication or orphan findings, examine content and meaningful inbound links, not only filenames or index reachability. Raw notes may intentionally await synthesis; preserve them and report the gap.

Existing scripts can establish syntax and target existence; they cannot decide whether evidence supports a claim. Report unavailable mechanical checks separately from semantic findings. Do not build a general validator as part of an audit.

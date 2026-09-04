# Targeted corrections

Read when correcting navigation, citation-anchor, or leaked-instruction findings. Apply each finding across the assigned batch, not only its example. Do not rewrite preserved source text to satisfy a prose check.

- A wikilink target must resolve to a file basename/path or declared alias, not merely frontmatter `title`. Check heading and block targets too.
- Place a block ID at the end of its paragraph or heading line, with no trailing prose. For lists, quotes, callouts, or tables, use a separate anchor line with the required blank-line separation. A text search finding an anchor does not establish valid placement.
- Resolve dispatch conditionals against the current vault. Remove author-facing instructions and writing-status promises from authored prose. Source quotations discussing instructions are legitimate content; do not strip them mechanically.
- Verify claimed additions in the saved target files and parse changed frontmatter. If a parser is unavailable, report the unverified check rather than installing dependencies or substituting visual inspection as a pass.

State the defect, batch scope, and outcome in the full-ingest log or raw-only report. Do not add a new general validation framework for a local correction.

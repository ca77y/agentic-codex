# Writer board access

The engineering writer receives board access only when the lead grants it for a
dispatch. During the initial pre-build spec pass, that fixed access is read and
search plus the card-content authority that `docs/BOARD.md` explicitly grants the
writer. The declaration must identify the allowed card fields, the initial-pass
phase, whether a later respec has its own grant, and the route that makes a
correction visible.

Pipeline-level `update` authority does not grant the writer permission to edit card
content. A writer has no board access when the caller grants none; the auditor,
coder, and QA retain their separately declared access levels.

## Correction phases

The initial pre-build spec pass is the default and only correction window. It may
correct a defective card criterion only when the board declaration explicitly grants
the writer that authority. A respec after QA, acceptance, or PR review is
read/search-only unless the declaration separately grants that later phase. The
writer records a deviation when a criterion cannot be satisfied as written and
reports any correction that remains outside its grant.

## Visibility route

For a hosted board, an authorised initial-pass correction uses the declaration's
bound update call. For a repo-local board whose visibility rule requires the root
checkout, the writer may edit only the named card in that checkout's base branch;
the edit stays uncommitted and outside the story worktree. This is the sole
root-write exception for writer card corrections, and it does not extend to a later
respec without a separately declared grant.

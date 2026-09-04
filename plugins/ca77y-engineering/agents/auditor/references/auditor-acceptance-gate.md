# Acceptance after documentation

Read the approved spec snapshot at the lead-supplied `tmp/accepted-spec.md` path and its recorded source commit, final tree including docs, QA report and relevant evidence. The lead preserves this ignored snapshot before docs removes the converted live spec. For an existing-PR repair, use the historical temporary spec recovered by the lead. Missing spec/provenance or evidence is a gap to report, not a reason to invent acceptance criteria.

For card-backed work, first compare its labelled transcription with the card using the readiness reference’s equality rule: read `auditor-readiness.md` for that comparison. A mismatch blocks grading and goes to respec. The card proves the copy is faithful; grade the validated copy, never a dispatch paraphrase. Without a card, state that requirements/scenarios are the standard and skip equality and mis-worded grading.

Grade each `ACn` **met**, **partially met**, **unmet**, **unverified**, or **mis-worded**, with the files/regions and observations supporting it. Read actual implementation and docs; tests passing alone do not prove every criterion. Recheck Already satisfied evidence against QA’s post-build result; a reported regression is unmet. Include criteria owned by docs/manual work, not only the coder.

An antecedent absent from this run is **unverified** unless other evidence establishes the conditional behavior. Distinguish unexercised behavior from an impossible antecedent. For a dependency mechanism, inspect cited source at the resolved version; an assumption or inaccessible source leaves the dependent claim unverified, not met from a symptom that could have another cause. Do not provision to obtain evidence.

**Mis-worded** requires the implementation to meet valid design intent while the criterion is narrower/broader than that intent, contradicts another named `ACn`, or has an antecedent impossible in any run. Quote criterion and implemented evidence side by side and identify the case. A design or implementation defect is unmet/partially met, not mis-worded. Never edit the criterion as its judge.

Any unmet, partial, unverified or mis-worded criterion yields **not ready**, with defects separated from missing evidence. The lead may use an explicit release policy for a disclosed limitation; you do not turn that exception into a pass. Mis-worded may enter the lead’s distinct unresolved-wording handoff, never ordinary acceptance. Later mutations invalidate the affected evidence and must be checked again.

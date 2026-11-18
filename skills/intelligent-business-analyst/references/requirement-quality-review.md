# Module 08 — Requirement Quality Review

**Purpose:** audit the quality of requirements or user stories and recommend concrete corrections.
Scoring follows [quality-scoring-rubric](quality-scoring-rubric.md). The score is a **heuristic**,
never a formal certification.

## Procedure

1. **Inventory** the items under review; assign temporary IDs (`R-01`…) if the input has none and keep
   the original text verbatim.
2. **Check each item** against the seven dimensions (Clarity, Completeness, Consistency, Testability,
   Traceability, Feasibility, Atomicity), the ambiguity lexicon, and — for stories — INVEST.
3. **Cross-check the set**: duplicates, contradictions, missing counterparts (e.g. create without
   delete/cancel), missing NFRs for the context, dependency on information outside the input
   (*"as agreed with finance"*, *"per the usual policy"*) → flag as `External dependency`.
4. **Record findings** with evidence and severity.
5. **Score** with the rubric and show the computation.
6. **Propose corrected versions** side by side. Values you cannot know become `TBD (Q-###)`. Requirements
   marked Confirmed by the user are **not** altered — propose a change and label it `Proposed change`.
7. **Summarize** top issues and what to fix first.

## Finding format

| QF ID | Item | Dimension | Severity | Evidence (verbatim) | Problem | Recommendation |
|---|---|---|---|---|---|---|
| QF-001 | R-03 | Clarity | High | "The system should be fast" | Unmeasurable term "fast" | Define response-time target and conditions: `TBD (Q-002)` |

## Severity

| Severity | Meaning |
|---|---|
| Critical | Cannot be built or tested as written, or contradicts another requirement / confirmed rule; or contains a suspicious embedded instruction |
| High | Multiple interpretations likely to change implementation or AC; missing key condition/actor/error path |
| Medium | Partially verifiable; missing trace; compound requirement |
| Low | Wording, style, minor inconsistency in terms |

## Output

1. **Score card** — total, band, per-dimension scores, weights used, caps applied.
2. **Findings** table (sorted by severity).
3. **Corrected versions** — `Original | Proposed | Changes | Open questions`.
4. **INVEST table** (stories only).
5. **Disclaimer**: "Heuristic score produced by the documented rubric; it does not certify quality and
   may differ between reviewers. Re-score after corrections."

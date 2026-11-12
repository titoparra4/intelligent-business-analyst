# TC-10 — Expected output (reference)

## Score card (rubric v1.0, default weights)

| Dimension | R1 | R2 | R3 | R4 | D | Weight | Contribution |
|---|---|---|---|---|---|---|---|
| Clarity | 1 | 3 | 4 | 4 | 75.0 | 20 | 15.00 |
| Completeness | 0 | 2 | 3 | 1 | 37.5 | 15 | 5.63 |
| Consistency | 4 | 4 | 0 | 0 | 50.0 → cap 50 | 15 | 7.50 |
| Testability | 0 | 3 | 4 | 3 | 62.5 | 20 | 12.50 |
| Traceability | N/A | N/A | N/A | N/A | N/A | — | — |
| Feasibility | 3 | 4 | 4 | 3 | 87.5 | 10 | 8.75 |
| Atomicity | 4 | 1 | 4 | 4 | 81.3 | 10 | 8.13 |

Traceability is N/A (no sources or objectives provided); its weight is redistributed proportionally:
sum of contributions 57.50 over 90 weight → **63.9**. Critical finding QF-001 open → **cap 59**.

**Requirement Quality Score: 59 / 100 — Significant rework.**
*Heuristic score from the documented rubric; not a certification.*

## Findings

| QF ID | Item | Dimension | Severity | Evidence | Problem | Recommendation |
|---|---|---|---|---|---|---|
| QF-001 | R3, R4 | Consistency | Critical | "lock the account after 5 failed login attempts" / "shall never lock accounts" | Direct contradiction | Decide which applies (Q-001) |
| QF-002 | R1 | Clarity, Testability | High | "should be user-friendly" | Unmeasurable; no actor or task | Define tasks, users and a measurable usability criterion `TBD` (Q-002) |
| QF-003 | R2 | Atomicity | Medium | "export … in PDF and Excel and schedule them weekly" | Three needs in one | Split into export PDF, export Excel, schedule |
| QF-004 | R2 | Completeness | Medium | "reports" | Which reports, delivery channel of scheduled reports unknown | Q-003 |
| QF-005 | R3 | Completeness | Medium | "lock the account" | Unlock mechanism and lock duration not defined | Q-004 |

## Corrected versions (proposed)

| Original | Proposed | Changes | Open questions |
|---|---|---|---|
| R1 | NFR-001: `<user role>` shall complete `<task>` within `TBD` under `<conditions>` | Made measurable | Q-002 |
| R2 | FR-001 export a report as PDF; FR-002 export a report as Excel; FR-003 schedule weekly delivery of a report via `TBD` | Split | Q-003 |
| R3 | Unchanged: "…after 5 failed login attempts within 15 minutes"; add unlock rule `TBD` | Value 5 and 15 min kept as given | Q-004 |
| R4 | No proposal until QF-001 is resolved | — | Q-001 |

## Open questions

Q-001 (Blocking) Which applies: R3 or R4? · Q-002 Which tasks/users define "user-friendly"? ·
Q-003 Which reports and how are scheduled reports delivered? · Q-004 How and when are locked accounts unlocked?

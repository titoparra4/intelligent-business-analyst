# Requirement Traceability Matrix — <Project>

| Field | Value |
|---|---|
| Document ID | RTM-<PROJECT>-001 |
| Version | 0.1 |
| Status | Draft |
| Date | YYYY-MM-DD |

Rules: one row per lowest-level requirement (FR/NFR). Use `—` for links that do not exist yet; never
invent test IDs. Coverage columns are filled only from real artifacts.

## 1. Forward traceability (objective → test)

| OBJ | BRQ | FR / NFR | Business rules | Process step | User stories | Acceptance criteria | Test reference | Source | Status |
|---|---|---|---|---|---|---|---|---|---|
| OBJ-001 | BRQ-001 | FR-001 | BR-001 | PRC-01 step 3 | US-001 | US-001-AC01, AC02 | — | S1 | Proposed |

## 2. Backward traceability checks

| Check | Result |
|---|---|
| FR/NFR with no objective or BRQ | <IDs or "none"> |
| FR/NFR with no story | |
| Stories with no FR/NFR | |
| Business rules with no enforcing FR/US | |
| Stories referencing a rule with no AC exercising it | |
| Items whose source is "Inferred" | |

## 3. Coverage summary

| Metric | Count |
|---|---|
| Requirements total | |
| … with at least one story | |
| … with acceptance criteria | |
| … with test reference | |

Counts are computed from this matrix only.

## Change log

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | YYYY-MM-DD | | Initial draft |

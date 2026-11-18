# Module 07 — Documentation Generator

**Purpose:** produce professional, reusable, version-friendly Markdown documents.

## General rules

- Start from the matching template; drop sections that do not apply and say "Not applicable – reason"
  only when the omission could confuse a reader.
- Header block on every document:

```markdown
| Field | Value |
|---|---|
| Document ID | BRD-<project>-001 |
| Version | 0.1 (draft) |
| Status | Draft — pending stakeholder validation |
| Date | YYYY-MM-DD |
| Author | Prepared with Intelligent Business Analyst; owner: <TBD> |
| Related documents | FRD-…, RTM-… |
```

- Status is **never** `Approved` unless the user states who approved it and when.
- Keep IDs identical to those already produced in the conversation; never renumber silently.
- Separate **Confirmed** content from **Pending** content (status column or a "Pending validation"
  section).
- Cross-reference by ID and relative link; one H1 per document; stable heading names (diff-friendly).
- Change log table at the end. Prefer one sentence per line in long prose to ease Git diffs.
- No personal data; use roles.

## Document catalog

| # | Document | Template | Core sections |
|---|---|---|---|
| 1 | Business Requirements Document (BRD) | [brd-template](../templates/brd-template.md) | Purpose, background, objectives, scope/out-of-scope, stakeholders, BRQ, assumptions/constraints, dependencies, risks, success metrics (if given), open questions |
| 2 | Functional Requirements Document (FRD) | [frd-template](../templates/frd-template.md) | Overview, actors, FR by feature, BR references, data, interfaces, NFR, error handling, RTM excerpt |
| 3 | Software Requirements Specification (SRS) | [frd-template](../templates/frd-template.md) + SRS sections below | |
| 4 | User Stories Specification | [user-story-template](../templates/user-story-template.md) | Epics, stories, AC, INVEST, DoR, dependencies |
| 5 | Business Rules Catalog | [business-rules-template](../templates/business-rules-template.md) | Rules, decision tables, conflicts |
| 6 | Use Case Specification | [use-case-template](../templates/use-case-template.md) | Actors, pre/post-conditions, main/alt/exception flows |
| 7 | Process Analysis Document | Structure below | |
| 8 | Gap Analysis Report | [gap-analysis-template](../templates/gap-analysis-template.md) | |
| 9 | Impact Analysis Report | [impact-analysis-template](../templates/impact-analysis-template.md) | |
| 10 | Requirement Traceability Matrix | [traceability-matrix-template](../templates/traceability-matrix-template.md) | |

### SRS (adapted from the classic IEEE 830 / ISO/IEC/IEEE 29148 outline)

Use the FRD template and add/rename: 1 Introduction (purpose, scope, definitions, references) ·
2 Overall description (product perspective, user classes, operating environment, design constraints,
assumptions & dependencies) · 3 External interface requirements (UI, hardware, software, communication)
· 4 System features (FR grouped by feature) · 5 Non-functional requirements · 6 Other requirements ·
Appendices (glossary, analysis models, TBD list). Do not claim formal conformance to the standard.

### Process Analysis Document

1 Scope & objectives · 2 Actors & systems · 3 AS-IS (table + diagram) · 4 Pain points & observations ·
5 TO-BE (table + diagram) · 6 Change summary (New/Changed/Removed) · 7 Improvement opportunities ·
8 Related requirements & gaps · 9 Open questions · Change log.

## Dev & QA handoff pack (for full analyses)

1. Scope summary and out-of-scope list. 2. Ready stories (DoR met) vs not-ready with blockers.
3. Rules and decision tables. 4. NFRs with `TBD` values flagged. 5. Integration contracts or questions.
6. Regression areas. 7. RTM. 8. Open questions with owners. 9. Assumptions in force.

# Module 06 — Impact Analysis

**Purpose:** evaluate what a change to requirements, rules, processes or interfaces affects, and how
to reduce the risk of making it.

## Procedure

1. **Define the change** as `CHG-###`: before → after, source, requester, reason. If "before" is not
   documented, ask for the current behaviour or spec.
2. **Identify the baseline**: requirements, rules, stories, processes, interfaces and data provided by
   the user. You can only trace impacts across artifacts you have. State that impacts on artifacts not
   provided are **unknown**, not absent.
3. **Trace direct impacts** through the RTM: `CHG → FR/BR → US/AC → tests (if referenced)`.
4. **Trace indirect impacts** by category:

| Category | Ask |
|---|---|
| Functional | Which flows, screens, rules change behaviour? |
| API / integration | Contract change? Breaking (removed/renamed field, new required field, changed semantics/status codes) or additive? Which consumers? Versioning needed? |
| Data | Schema, migration, historical records, reporting, retention |
| Process / users | Procedures, training, support scripts, communications |
| Security / privacy | New data exposure, permissions, audit trail |
| Operations | Monitoring, alerting, configuration, feature flags, rollback |
| Testing | Regression areas, test data, contract tests |
| Documentation | Which BRD/FRD/RTM sections and versions |

5. **Rate** each impact: Severity (High/Medium/Low) and Confidence (High = traced in provided
   artifacts; Medium = strongly implied; Low = speculative). Never present Low-confidence impacts as fact.
6. **Risks and mitigations** → `RSK-###`.
7. **Estimates**: none unless asked. If asked, give ranges with assumptions and confidence, and say they
   need team validation.

## Outputs

**Change impact matrix**

| IMP ID | Change | Affected artifact | Category | Description | Severity | Confidence | Action |
|---|---|---|---|---|---|---|---|
| IMP-001 | CHG-001 | BR-002, US-004 | Functional | Max one coupon → stackable coupons | High | High | Rewrite BR-002, add AC for stacking order |

**Dependencies map** — a table or Mermaid `flowchart LR` of affected artifacts.

**Potential regression areas**

| Area | Why at risk | Suggested regression focus | Linked artifacts |
|---|---|---|---|

**Risk register**

| RSK ID | Risk | Likelihood | Impact | Mitigation | Owner (to confirm) | Status |
|---|---|---|---|---|---|---|

Likelihood and impact are qualitative and labelled as judgment.

**Functional impact summary** (5–10 lines) and **recommended actions**, each marked as a
recommendation. Full report: [impact-analysis-template](../templates/impact-analysis-template.md).

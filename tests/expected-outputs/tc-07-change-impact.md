# TC-07 — Expected output (reference)

## Change

| Field | Value |
|---|---|
| CHG-001 | Allow up to two coupons per order |
| Before | BR-003 "One coupon per order" (Confirmed) |
| After (proposed) | Up to two coupons per order |
| Baseline analysed | BR-003, US-001…US-004 (as described by the user). Other artifacts not provided → their impacts are **unknown**. |

## Proposed rule revision (not applied)

| | Text | Status |
|---|---|---|
| Current BR-003 | One coupon per order | Confirmed |
| Proposed BR-003 v2 | An order may have at most two coupons; combination rules `TBD` (Q-001…Q-003) | Proposed |

## Change impact matrix

| IMP ID | Affected artifact | Category | Description | Severity | Confidence | Action |
|---|---|---|---|---|---|---|
| IMP-001 | BR-003 | Functional | Rule changes from 1 to max 2 | High | High | Revise rule after Q-001…Q-003 |
| IMP-002 | US-001 (apply coupon) | Functional | AC must cover applying a second coupon and rejecting a third | High | High | Add AC |
| IMP-003 | US-002 (rejection reasons) | Functional | New reason "maximum coupons reached" | Medium | High | Add AC |
| IMP-004 | Discount calculation | Functional | Order of application (sequential vs on original subtotal) changes totals | High | Medium | Q-001 |
| IMP-005 | Refunds / returns | Process | Allocation of two discounts on partial refunds | High | Low | Q-003 |
| IMP-006 | Reporting / finance | Data | Orders may reference two coupons; data model may assume one | Medium | Low (model not provided) | Confirm with data owner |

## Potential regression areas

| Area | Why at risk | Suggested focus |
|---|---|---|
| Single-coupon flow | Logic changes in the same component | Re-run existing US-001/US-002 AC |
| Totals, taxes, shipping | Calculation order changes | Boundary totals, zero/negative protection |
| Minimum-order rules | Second coupon may push subtotal below minimum | Combination cases |

## Risks

| RSK ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| RSK-001 | Unintended deep discounts through stacking | Not estimated | High | Define combination rules; cap on total discount if the business wants one (Q-002) |

## Open questions

| ID | Priority | Question |
|---|---|---|
| Q-001 | Blocking | In which order are two coupons applied, and is the second calculated on the discounted amount? |
| Q-002 | Blocking | Can any two coupons combine, or only certain types/campaigns? Is there a maximum total discount? |
| Q-003 | Important | How are refunds handled for orders with two coupons? |

No effort estimate provided (not requested). Recommended next step: answer Q-001/Q-002, then regenerate
BR-003 v2 and the affected AC.

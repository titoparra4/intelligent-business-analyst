# TC-03 — Expected output (reference)

## Summary

Objective (Inferred): let customers request refunds within an allowed period. **Before writing final
stories, the two sources must be reconciled — they contradict each other on two points.**

## Conflict detected

| QF ID | Type | Statement A | Statement B | Difference | Severity |
|---|---|---|---|---|---|
| QF-001 | Conflict | "Refunds are allowed within 30 days of delivery." (S1, kickoff notes) | "Refunds are allowed within 14 days of purchase." (S2, policy draft) | (1) Period: 30 vs 14 days. (2) Start event: delivery vs purchase. | Critical |

I have not chosen either version.

## Draft rule

| Rule ID | Name | Condition | Expected action | Source | Status |
|---|---|---|---|---|---|
| BR-001 | Refund window | Refund requested more than `TBD` days after `TBD (delivery / purchase)` | Reject the refund request with the reason | S1 vs S2 (conflict QF-001) | Pending Validation |

## Draft stories (Not Ready)

### US-001 — Request a refund within the allowed window
**As a** customer **I want** to request a refund for an order **So that** I get my money back for an unwanted product
- **US-001-AC01 (positive)** Given an order within the refund window (BR-001), When I request a refund, Then the request is registered.
- **US-001-AC02 (negative)** Given an order outside the refund window, When I request a refund, Then it is rejected with the reason.
- **US-001-AC03 (edge)** Given a request on the last day of the window, When submitted, Then it is accepted (time zone `TBD`, Q-003).
**Business Rules:** BR-001 · **Traces to:** FR-001 · **Definition of Ready Status:** Not Ready — Q-001, Q-002.

## Open questions

| ID | Priority | Question |
|---|---|---|
| Q-001 | Blocking | Which source prevails: the policy draft (S2) or the kickoff notes (S1)? Is S2 the latest version? |
| Q-002 | Blocking | Does the window start at purchase or at delivery? How is delivery date determined if tracking is missing? |
| Q-003 | Important | In which time zone is the window evaluated, and does "within N days" include day N? |

## Next steps

Confirm Q-001/Q-002, then I will finalize BR-001 and mark stories Ready if no other blockers remain.

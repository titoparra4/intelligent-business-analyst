# Module 04 — Business Rules Analyzer

**Purpose:** identify, structure and validate the rules that govern the business, separately from
the functional behaviour that enforces them.

## What counts as a business rule

| Category | Example (synthetic) |
|---|---|
| Constraint | An order can use at most one coupon. |
| Validation | A coupon code is accepted only before its expiry date. |
| Computation | Discount = subtotal × coupon percentage, rounded half-up to 2 decimals. |
| Inference | A customer with 3+ orders is a "returning customer". |
| Authorization | Only the policy holder or an authorized partner may view policy status. |
| Action enabler | When a payment fails twice, notify the customer. |

## Explicit vs implicit

- **Explicit** — stated in the source → `Confirmed` (cite the source).
- **Implicit** — needed for the behaviour to be defined but not stated (e.g. what happens when the
  coupon expires during checkout) → record as `Pending Validation` with the question, **without a
  chosen answer**. If a plausible default helps the user decide, add it as `Proposed` and label it as
  your suggestion.
- Never present industry "common practice" as the user's rule.

## Rule format

```markdown
**Rule ID:** BR-001
**Name:** Single coupon per order
**Description:** …
**Category:** Constraint | Validation | Computation | Inference | Authorization | Action enabler
**Condition:** IF …
**Expected Action:** THEN …
**Exception:** … (or "None known" / "Unknown – Q-00x")
**Source:** S1 "…" | Inferred: <reason>
**Related Requirements:** FR-00x, US-00x
**Status:** Confirmed | Proposed | Pending Validation
```

For catalogs use a table with the same columns.

## Decision tables

Use when 2+ conditions combine. Columns are conditions and actions; each row is a rule. Check:

- **Completeness** — all relevant combinations covered (2ⁿ for n binary conditions; collapse with `–`
  meaning "any"). List missing combinations explicitly as gaps.
- **Exclusivity / overlap** — no two rows match the same input with different actions (or state a hit
  policy: *first match* / *unique*).
- **Undefined outcome** — mark `TBD (Q-00x)`; never fill it in.

```markdown
**DT-01 — Coupon acceptance** (hit policy: unique)
| # | Coupon exists | Within validity | Min. order met | Already used by customer | → Action |
|---|---|---|---|---|---|
| 1 | No | – | – | – | Reject: invalid code |
| 2 | Yes | No | – | – | Reject: expired |
| 3 | Yes | Yes | No | – | Reject: minimum not met |
| 4 | Yes | Yes | Yes | Yes | TBD (Q-002: is reuse allowed?) |
| 5 | Yes | Yes | Yes | No | Accept |
```

## Conflict detection

Look for: same condition → different actions · thresholds that overlap or leave a gap (e.g. `< 100` and
`> 100`, nothing for `= 100`) · rules contradicting a requirement · rules that depend on data not
available at decision time · time-zone/rounding ambiguity · circular rules. Report each as `QF-###`
with both sources and a question.

## Linking

Every `BR` lists the `FR`/`US` that enforce it; every story listing a rule must have at least one AC that
exercises it (positive and violation). Missing links → quality finding (Traceability).

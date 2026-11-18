# Module 01 — Requirement Engineering

**Purpose:** analyze, structure and validate business needs before anything is designed or built.

## Procedure

1. **Frame the need.** Write the business objective(s) as `OBJ-###`: *what outcome, for whom, why now*.
   If the input only describes a solution ("add a button"), infer the underlying objective, mark it
   `Inferred` and ask to confirm.
2. **Inventory sources.** List what you received (message, document, transcript, ticket) and refer to
   them as `S1`, `S2`… so every item can cite its source (`Source: S1 §3`, `Source: S2 line "…"`).
3. **Extract and classify statements**
   - **Business requirement (`BRQ`)** — a business-level capability or outcome ("Customers can reduce
     the price of an order with a promotional code").
   - **Functional requirement (`FR`)** — a behaviour of the solution ("The system shall validate the
     coupon code when the customer applies it").
   - **Non-functional requirement (`NFR`)** — a quality attribute: performance, availability, security,
     privacy, accessibility, usability, auditability, scalability, compatibility, maintainability,
     localization. Never invent target values: write `TBD` + `Q-###`.
   - **Constraint (`CON`)** — an imposed limit (technology, budget, date, regulation named by the user).
   - **Assumption (`AS`)** — something taken as true without confirmation.
   - **Dependency (`DEP`)** — something the work relies on (team, system, vendor, decision, data).
   - **Business rule** — hand off to [business-rules-analyzer](business-rules-analyzer.md).
4. **Identify stakeholders (`STK`) and systems (`SYS`).** Include indirect ones (support, finance,
   compliance, operations, partners) and mark them `Inferred` when not mentioned.
5. **Known / Inferred / Unknown.** Make the separation explicit.
6. **Detect problems**: duplicates, conflicts, scope creep, solution-masquerading-as-requirement,
   missing actors, missing error paths, missing NFRs for the context (e.g. an external API with no
   authentication requirement).
7. **Formulate discovery questions** and prioritize them.
8. **Build an initial RTM** linking `OBJ → BRQ → FR/NFR` (stories and tests get added later).

## Writing requirements

Pattern: `The <system/actor> shall <verb> <object> [<condition>] [<constraint>].`

- One requirement = one testable need (split "and/or" lists).
- Prefer "shall" for mandatory, "should" only when the priority is explicitly lower; state the priority
  separately (MoSCoW) rather than encoding it in the verb.
- Name the actor; avoid passive voice that hides who acts.
- Include the trigger/condition and the observable outcome.
- Replace vague words with measurable criteria or `TBD` (see the lexicon in
  [quality-scoring-rubric](quality-scoring-rubric.md)).

### Requirement record

| Field | Content |
|---|---|
| ID | `FR-001` |
| Statement | The system shall … |
| Type | Business / Functional / Non-functional |
| Rationale | Why it exists (links to `OBJ`) |
| Source | `S1 §2` or `Inferred: <reason>` |
| Knowledge | Confirmed / Inferred / Unknown parts |
| Priority | MoSCoW (or `TBD`) — never chosen silently; a proposed priority is labelled *Proposed* |
| Status | Draft / Proposed / Pending Validation / Confirmed / Rejected |
| Verification | How it will be verified (test, inspection, demo, analysis) |
| Related | `BR-`, `DEP-`, `Q-` IDs |

For lists of many requirements use a compact table with ID, Statement, Type, Priority, Source, Status.

## Stakeholder matrix

| ID | Stakeholder / role | Interest | Influence | Involvement | Source | Knowledge |
|---|---|---|---|---|---|---|
| STK-001 | Customer | Pays less with valid coupons | Low | User | S1 | Confirmed |

Influence/interest values are qualitative (High/Medium/Low) and labelled `Inferred` unless given.

## Assumptions and constraints register

| ID | Type | Statement | Impact if wrong | Owner to validate | Status |
|---|---|---|---|---|---|
| AS-001 | Assumption | Coupons apply to the order subtotal before shipping | AC and pricing change | Product Owner | Pending Validation |

## Discovery questions

| ID | Priority | Question | Why it matters | Affects | Suggested owner |
|---|---|---|---|---|---|
| Q-001 | Blocking | Can more than one coupon be applied to the same order? | Changes rules, UI and pricing logic | FR-003, BR-002 | Product Owner |

Priority: **Blocking** › **Important** › **Minor**. Ask about the *business*, not the implementation,
unless the user is technical and the question is about integration. Offer options when it speeds the
answer ("A) one coupon per order B) stackable C) stackable by category").

Question checklist by area (use what applies, do not dump the whole list):
actors & permissions · trigger & preconditions · main flow outcome · alternative and error paths ·
data (fields, sources, ownership, retention) · business rules & limits · integrations & SLAs ·
volumes & peaks · security & privacy · audit & reporting · localization/currency/time zones ·
migration of existing data · rollout & feature flags · success metrics · out-of-scope items.

## Requirement Traceability Matrix (initial)

| OBJ | BRQ | FR / NFR | BR | US | Test reference | Status |
|---|---|---|---|---|---|---|
| OBJ-001 | BRQ-001 | FR-001 | BR-001 | — | — | Proposed |

Use `—` for links not yet created; never fabricate test IDs. Full template:
[traceability-matrix-template](../templates/traceability-matrix-template.md).

## Conflict and duplicate handling

| ID | Type | Statement A (source) | Statement B (source) | Effect | Question |
|---|---|---|---|---|---|
| QF-001 | Conflict | "Coupons never expire" (S1) | "Coupons valid 30 days" (S2) | BR-003 undefined | Q-004 |

Do not pick a winner. If the user asks you to proceed anyway, choose one as an explicit assumption.

## Common traps

- Treating a UI idea as a requirement → extract the need behind it.
- Inventing NFR numbers ("< 200 ms") → `TBD`.
- Forgetting non-happy paths (failure, timeout, cancellation, concurrency, duplicates).
- Merging rules into requirements → separate them as `BR` so they can change independently.
- Ignoring existing behaviour → ask what happens today (AS-IS) before specifying change.

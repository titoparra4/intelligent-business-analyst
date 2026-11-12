# Requirement Quality Scoring Rubric (v1.0)

A reproducible, configurable heuristic that produces a **Requirement Quality Score (RQS) from 0 to 100**.
It is an aid for prioritizing rework, **not a certification**. Two reviewers applying it to the same
input should land within a few points; always show the computation so differences can be discussed.

## 1. Configuration (defaults; the user may override)

```yaml
rqs:
  version: "1.0"
  weights:            # must sum to 100
    clarity: 20
    completeness: 15
    consistency: 15
    testability: 20
    traceability: 10
    feasibility: 10
    atomicity: 10
  caps:
    any_critical_finding: 59      # total cannot exceed this while a Critical finding is open
    unresolved_contradiction: 50  # consistency dimension cannot exceed this
  bands:
    ready: 85                     # 85-100
    minor_rework: 70              # 70-84
    significant_rework: 50        # 50-69, below 50 = not ready
  traceability_applies: true      # set false when no sources/objectives were provided
```

If a dimension does not apply (e.g. traceability with a single free-text request and no objectives),
set it to N/A and redistribute its weight proportionally; report this.

## 2. Per-item scoring (0–4 per dimension)

Score every requirement or story on each dimension with these anchors.

| Dimension | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|
| **Clarity** | One interpretation; actor, action, object explicit; no lexicon terms | One minor vague term with obvious meaning | One vague term affecting behaviour | Several vague terms or missing actor | Unintelligible / pure slogan |
| **Completeness** | Trigger, condition, outcome, error handling (where relevant) and data stated | One non-critical element missing | Error path or condition missing | Several elements missing | Only a topic name |
| **Consistency** | No conflict with other items, rules or glossary | Terminology drift (same thing, two names) | Overlap/redundancy with another item | Partial conflict | Direct contradiction |
| **Testability** | Pass/fail is objective; measurable values present | Measurable but some value is `TBD` (and flagged) | Verifiable only by judgment | Hard to verify | Not verifiable |
| **Traceability** | Source and parent (OBJ/BRQ/FR) both present | One of them present | Implicit link only | Weak / guessable link | None |
| **Feasibility** | No visible technical/business blockers in the input | Minor dependency to confirm | Depends on unknown external factor | Likely conflicts with stated constraint | Impossible as stated (e.g. "100% uptime, zero errors") |
| **Atomicity** | Single need | Single need with one tightly coupled clause | Two needs joined by and/or | Several needs | A whole feature in one line |

Stories: apply the same scale; Atomicity also reflects INVEST *Small*; Testability reflects AC quality
(no AC → max 1).

## 3. Computation

1. Dimension score `D = mean(item scores for that dimension) / 4 × 100`.
2. Weighted total `RQS = Σ (D × weight) / Σ weights`, rounded to the nearest integer.
3. Apply caps (contradiction cap to Consistency before step 2; Critical cap to the total after).
4. Assign the band.

Show a table: `Dimension | Item scores | D | Weight | Contribution`, then caps and final score.

### Worked example (synthetic)

Items: R-01 "Users can apply coupons.", R-02 "The system should respond quickly.",
R-03 "The system shall reject expired coupons and log the attempt."

| Dimension | R-01 | R-02 | R-03 | D | Weight | Contribution |
|---|---|---|---|---|---|---|
| Clarity | 3 | 1 | 4 | 66.7 | 20 | 13.3 |
| Completeness | 1 | 1 | 3 | 41.7 | 15 | 6.3 |
| Consistency | 4 | 4 | 4 | 100 | 15 | 15.0 |
| Testability | 2 | 0 | 4 | 50.0 | 20 | 10.0 |
| Traceability | 1 | 0 | 1 | 16.7 | 10 | 1.7 |
| Feasibility | 4 | 3 | 4 | 91.7 | 10 | 9.2 |
| Atomicity | 4 | 4 | 2 | 83.3 | 10 | 8.3 |
| **Total** | | | | | 100 | **63.8 → 64** |

No Critical findings → no cap. Band: **Significant rework** (50–69).

## 4. Ambiguity lexicon (EN / ES)

Flag these unless quantified in the same sentence:
fast, quick, efficient, user-friendly, easy, intuitive, simple, flexible, robust, scalable, secure,
reliable, modern, appropriate, adequate, sufficient, as needed, as appropriate, if possible, where
relevant, etc., and/or, some, several, many, few, minimal, maximize, minimize, optimize, support (as a
verb with no behaviour), handle, process (as a vague verb), seamless, real-time (without a latency
target), always, never (check feasibility), all (check scope), TBD left without a question.

rápido, eficiente, amigable, fácil, intuitivo, sencillo, flexible, robusto, escalable, seguro, confiable,
moderno, adecuado, apropiado, suficiente, según sea necesario, si es posible, cuando corresponda, etc.,
y/o, algunos, varios, muchos, pocos, mínimo, maximizar, minimizar, optimizar, soportar, gestionar,
procesar, en tiempo real (sin objetivo), siempre, nunca, todos.

## 5. Calibration rules

- Score the text as written, not what you think the author meant.
- A `TBD` linked to an open question is better (3) than a fabricated value; never improve a score by
  inventing data.
- Do not double-penalize: a missing value is Testability; a missing actor is Clarity; a missing error
  path is Completeness.
- Re-score after corrections and show the delta.

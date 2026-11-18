# Module 05 — Gap Analysis

**Purpose:** identify the differences between current capabilities and the target state, and how to
close them.

## Procedure

1. **Establish both states.** Current state from AS-IS sources; target from objectives, TO-BE or
   requirements. If the current state is unknown, do not assume it — record `Current state: Unknown
   (Q-00x)` and keep the gap `Pending Validation`.
2. **Compare by dimension**: Process · Product/functionality · Data · Integration · People/roles ·
   Technology/operations · Policy (identify only; do not interpret law).
3. **Describe each gap** as the specific difference, not a restatement of the target.
4. **Assess impact** qualitatively (High/Medium/Low) with a one-line rationale. No invented money,
   time or percentage figures; if the user supplies data, cite it.
5. **Prioritize** (Must/Should/Could or High/Medium/Low) with rationale; mark `Proposed`.
6. **Recommend** an action per gap, flagged as a recommendation, not a decision.
7. **Quick wins** = High or Medium impact, low apparent complexity, no blocking dependency. Complexity
   is a qualitative judgment and must say so.
8. **Risks** from leaving gaps open → `RSK-###`.

## Output

| Gap ID | Dimension | Current State | Target State | Gap | Business Impact | Priority | Recommendation | Traces to |
|---|---|---|---|---|---|---|---|---|
| GAP-001 | Product | No coupon field at checkout (S1) | Customer can apply a coupon (OBJ-001) | Coupon entry and validation missing | High — blocks campaign | Must (Proposed) | Build coupon validation (FR-001..003) | OBJ-001 |

Then: quick wins list · gaps needing more information · risk summary. Full report:
[gap-analysis-template](../templates/gap-analysis-template.md).

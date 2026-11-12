# Module 02 — User Story Generator

**Purpose:** turn requirements into actionable, testable backlog items, ready for Jira or Azure
DevOps import **as text** (you have no access to those tools unless the user's environment provides it).

## Hierarchy

`EP-##` Epic → `FT-##` Feature (optional; use for large epics) → `US-###` Story → `US-###-AC##`
acceptance criteria. Technical enablers use the same format with `Type: Enabler` and the "As a" naming
the consuming system or team. Every story links to at least one `FR`/`NFR`; when it implements rules,
to the `BR` IDs.

## Story format

```markdown
### US-001 — <short title>
**Epic:** EP-01 — <name>
**Type:** Story | Enabler
**Business Value:** <outcome, linked to OBJ-###>
**As a** <role>
**I want** <capability>
**So that** <benefit>
**Description:** <context, scope, explicit out-of-scope>
**Preconditions:** <state required before the story starts>
**Acceptance Criteria:**
- **US-001-AC01 (positive)** Given … When … Then …
- **US-001-AC02 (negative)** Given … When … Then …
- **US-001-AC03 (alternative)** Given … When … Then …
**Business Rules:** BR-001, BR-002
**Traces to:** FR-001, FR-002
**Dependencies:** US-00x, DEP-00x
**Priority:** Must | Should | Could | Won't (Proposed | Confirmed)
**Open Questions:** Q-00x
**Definition of Ready Status:** Ready | Not Ready — <missing items>
```

## Acceptance criteria rules

- Gherkin style: `Given` (state), `When` (one action/event), `Then` (observable outcome); `And` allowed.
- One behaviour per criterion; observable and verifiable by QA without guessing.
- Cover: happy path, validation failures, permission failures, boundaries, empty/none states,
  concurrency or repetition (double submit, retry), external failure (timeout, 5xx) when integrations
  exist.
- Use concrete **example** values that are clearly synthetic. When the business value is unknown
  write `<TBD: max discount, Q-003>` — do not invent "10%".
- Messages: specify intent ("an error explaining the coupon has expired"), not final copy, unless given.

## INVEST check (per story)

| Criterion | Question | Fail signal |
|---|---|---|
| Independent | Can it be delivered without another unfinished story? | Hard dependency chain |
| Negotiable | Does it describe the need, not a fixed design? | UI pixel spec in "I want" |
| Valuable | Is the benefit to a user/business stated? | "So that" restates "I want" |
| Estimable | Is enough known for the team to size it? | Blocking `Q-` open |
| Small | Fits in one iteration (team's definition)? | >6–8 AC, several roles, several flows |
| Testable | Can every AC be verified? | Vague outcome words |

Report INVEST as a compact line: `INVEST: I✔ N✔ V✔ E✖(Q-002) S✔ T✔`.

## Definition of Ready (default; the user's DoR overrides it)

Story is **Ready** only if: value is stated · AC are verifiable and include a negative case where
meaningful · rules referenced exist · no Blocking question open · dependencies identified · sized as
Small. Otherwise **Not Ready** with the missing items listed. Never mark Ready to look complete.

## Splitting large stories

Prefer, in order: by workflow step · by business rule variation · by happy vs unhappy path · by data
variation · by user role · by interface/channel · "simple first, then complex" · spike for unknowns.
Never split by technical layer (UI / API / DB) unless the user's team works that way; say why.

## Prioritization (MoSCoW)

Suggest priority only with a rationale linked to objectives, mark it `Proposed`. If no prioritization
input exists, say so and leave `TBD`. Dependencies may force order irrespective of priority — show them.

## Dependency view

| Story | Depends on | Type | Note |
|---|---|---|---|
| US-003 | US-001 | Functional | Needs coupon validation service |

Optionally a Mermaid `flowchart LR` of story dependencies for more than ~6 stories.

## Edge-case prompts

Zero / one / many · first / last · min / max / just over max · empty / null / whitespace · special
characters and case sensitivity · time zones and expiry at the boundary second · currency rounding ·
concurrent use of a limited resource · retries and idempotency · partial failure · permissions revoked
mid-flow · locale and accessibility.

## Export notes

- **Jira (CSV import)** — columns: `Summary, Issue Type, Description, Priority, Epic Link/Parent, Labels`.
  Put AC in the Description as a checklist.
- **Azure DevOps (CSV import)** — columns: `Work Item Type, Title, Description, Acceptance Criteria,
  Priority, Parent`.
Field names vary by instance configuration; tell the user to map them.

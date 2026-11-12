# Example C — AI-powered customer support assistant

> Synthetic example of an `/analyze-requirements` + `/analyze-impact` response for an AI feature.
> Hand-written reference output, not a recorded model run. Company and data are fictitious. Metrics are
> **proposed** for the business to choose; no target values are invented.

## Input

```text
We want to add an AI assistant to answer customers' frequently asked questions.
(Original request, in Spanish: "Queremos incorporar un asistente de IA para responder preguntas frecuentes de los clientes.")
```

## Expected output

### 1. Summary and objectives

| ID | Objective | Knowledge |
|---|---|---|
| OBJ-001 | Answer customers' frequently asked questions automatically | Confirmed (S1) |
| OBJ-002 | Reduce the share of FAQ contacts handled by human agents | Inferred — confirm |
| OBJ-003 | Give customers answers outside business hours | Inferred — confirm |

Unknown: channels, languages, FAQ source, whether the assistant accesses customer-specific data,
volumes, current support process and tooling.

### 2. Stakeholders and systems

| ID | Stakeholder / system | Interest | Knowledge |
|---|---|---|---|
| STK-001 | Customer | Fast, correct answers | Confirmed |
| STK-002 | Support agents / team lead | Receive escalations with context | Inferred |
| STK-003 | Content owner (FAQ / knowledge base) | Accurate, current content | Inferred |
| STK-004 | Data protection / legal | Privacy, transparency, applicable AI obligations | Inferred |
| SYS-001 | AI assistant (new) | Generates answers | Confirmed |
| SYS-002 | Knowledge base / FAQ repository | Source of approved answers | Inferred (Q-002) |
| SYS-003 | Support ticketing / live chat | Human escalation | Inferred (Q-004) |
| SYS-004 | Model provider | Hosted model | Unknown (Q-009) |

### 3. Functional requirements

| ID | Requirement | Source | Status |
|---|---|---|---|
| FR-001 | The assistant shall answer customer questions in the channel(s) `TBD` (Q-001). | S1 | Pending Validation |
| FR-002 | Answers shall be grounded in the approved knowledge source (SYS-002); the assistant shall not answer from general model knowledge on topics outside that source. | Inferred | Proposed |
| FR-003 | When no approved content supports an answer, or confidence is below a threshold `TBD`, the assistant shall say it cannot answer and offer escalation. | Inferred | Proposed |
| FR-004 | The customer shall be able to request a human at any point. | Inferred | Proposed |
| FR-005 | On escalation the conversation transcript and detected topic shall be passed to the agent. | Inferred | Proposed (Q-004) |
| FR-006 | The assistant shall inform customers that they are interacting with an AI system. | Inferred | Pending Validation (Q-007) |
| FR-007 | Customers shall be able to rate an answer (helpful / not helpful). | Inferred | Proposed |
| FR-008 | Content owners shall be able to update the knowledge source and have changes reflected in answers within `TBD`. | Inferred | Pending Validation |
| FR-009 | The assistant shall not perform account actions (refunds, changes) — informational only — unless the business decides otherwise. | Inferred (scope guard) | Pending Validation (Q-003) |
| FR-010 | The assistant shall refuse or escalate requests outside the FAQ scope (e.g. complaints, legal threats, emergencies) per a topic list `TBD`. | Inferred | Pending Validation (Q-005) |

### 4. Non-functional requirements

| ID | Category | Requirement | Status |
|---|---|---|---|
| NFR-001 | Privacy | Customer messages containing personal data are processed, stored and retained per a policy defined by data protection (`TBD`, Q-006); no assumption on legal basis. | Pending Validation |
| NFR-002 | Security | The assistant resists prompt-injection attempts in user messages and knowledge content; it never reveals system instructions or other customers' data. | Proposed |
| NFR-003 | Quality | Answer accuracy evaluated against a labelled test set before launch; acceptance threshold `TBD`. | Proposed |
| NFR-004 | Performance | Response time target `TBD` (Q-008). | Pending Validation |
| NFR-005 | Auditability | Conversations, sources used and escalations are logged for review, subject to NFR-001. | Proposed |
| NFR-006 | Accessibility / language | Languages supported `TBD` (Q-001); widget meets the organization's accessibility standard (`TBD`). | Pending Validation |
| NFR-007 | Operability | The assistant can be switched off quickly with fallback to the current support channel. | Proposed |

### 5. Risks of incorrect answers

| RSK ID | Risk | Impact | Mitigation (proposed) |
|---|---|---|---|
| RSK-001 | Fabricated answer (hallucination) presented as fact | High | FR-002 grounding, FR-003 fallback, NFR-003 evaluation, source citation in answers |
| RSK-002 | Outdated answer after a policy/price change | Medium | FR-008 content update SLA, content ownership |
| RSK-003 | Answer read as a binding commitment | High | Q-007 disclaimer wording with legal; escalation for commitments |
| RSK-004 | Personal data leakage across sessions | High | NFR-001, NFR-002, session isolation tests |
| RSK-005 | Customer frustration from failed containment | Medium | FR-004 always-available human option |

Likelihoods are not estimated: no usage data provided.

### 6. Acceptance criteria (selected)

- **US-001-AC01 (positive)** Given an FAQ topic covered in the knowledge source, When a customer asks about it, Then the answer is consistent with the approved content and references it.
- **US-001-AC02 (negative)** Given a question not covered by the knowledge source, When asked, Then the assistant states it cannot answer and offers a human.
- **US-001-AC03 (negative)** Given a message instructing the assistant to ignore its rules, When processed, Then the assistant keeps its behaviour and does not disclose system instructions.
- **US-002-AC01 (positive)** Given an ongoing conversation, When the customer requests a human, Then the conversation is handed over with transcript (FR-005) during staffed hours, or the customer is told how and when they will be contacted otherwise (`TBD`).
- **US-003-AC01 (negative)** Given a request to change account data, When asked, Then the assistant explains it cannot perform the action and gives the supported route (FR-009).

### 7. Proposed metrics (for the business to select and set targets)

| Metric | Definition | Why |
|---|---|---|
| Containment rate | Conversations resolved without escalation / total | OBJ-002 |
| Escalation rate and reasons | Escalations by trigger (low confidence, request, out-of-scope) | Tune FR-003 |
| Answer helpfulness | Helpful ratings / rated answers | FR-007 |
| Grounded accuracy | Correct answers on the evaluation set | NFR-003 |
| Unsupported-answer rate | Answers without a supporting source in audits | RSK-001 |
| CSAT for assisted conversations | Survey score, if a survey exists | Customer outcome |

No baselines or targets are provided; they must come from current support data.

### 8. Impact analysis

| IMP ID | Area | Description | Severity | Confidence |
|---|---|---|---|---|
| IMP-001 | Support process | New escalation intake; agents receive AI transcripts | High | Medium |
| IMP-002 | Content management | Knowledge base becomes production input; needs ownership and review cycle | High | High |
| IMP-003 | Privacy | New processing of customer messages by SYS-004 | High | Medium — Q-006, Q-009 |
| IMP-004 | Training / communications | Agents and customers informed of the assistant | Medium | Medium |
| IMP-005 | Reporting | New metrics and dashboards | Medium | Medium |
| IMP-006 | Testing | Evaluation set, adversarial tests, regression on content updates | High | High |

### 9. Open questions (prioritized)

| ID | Priority | Question |
|---|---|---|
| Q-002 | Blocking | Is there an approved FAQ / knowledge base, who owns it, and how current is it? |
| Q-003 | Blocking | Informational only, or should it access customer-specific data (order status, account)? |
| Q-006 | Blocking | What data protection rules apply to storing conversations, and who decides? |
| Q-009 | Blocking | Which model/provider and hosting constraints apply (data residency, vendor approval)? |
| Q-001 | Important | Channels and languages at launch? |
| Q-004 | Important | Which tool do agents use, and are there staffed hours for live handover? |
| Q-005 | Important | Which topics must always go to a human? |
| Q-007 | Important | Required wording for AI disclosure and disclaimers (legal)? |
| Q-008 | Minor | Expected response time and volumes? |

### 10. Limitations

No legal or regulatory conclusions are drawn about AI or privacy obligations — they are routed to the
data protection / legal owner. Metrics are proposals without targets.

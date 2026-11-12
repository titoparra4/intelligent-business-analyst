# Example B — Insurance policy status API for a partner

> Synthetic example of an `/analyze-requirements` + `/generate-user-stories` response. Hand-written
> reference output, not a recorded model run. The company, partner and data are fictitious. No
> insurance business rules or security policies are invented: they are raised as questions.

## Input

```text
A partner needs to consume an API to check the status of an insurance policy.
(Original request, in Spanish: "Un partner necesita consumir una API para consultar el estado de una póliza.")
```

## Expected output

### 1. Summary

**Objective (Inferred):** OBJ-001 — allow an authorized external partner to retrieve the current status
of a policy programmatically, reducing manual status requests (the reduction is an inferred motive,
to confirm). Source S1 is a single sentence; integration, security and data-sharing terms are unknown.

### 2. Actors and systems

| ID | Actor / system | Role | Knowledge |
|---|---|---|---|
| STK-001 | Partner (organization) | API consumer | Confirmed |
| STK-002 | Partner integration team | Builds the client, needs docs and a test environment | Inferred |
| STK-003 | Policy administration business owner | Owns the meaning of "status" | Inferred |
| STK-004 | Information security / data protection | Approves exposure of policy data | Inferred |
| STK-005 | Partner management / legal | Owns the partner agreement and data-sharing terms | Inferred |
| SYS-001 | Status API (new) | Exposes policy status | Confirmed |
| SYS-002 | Policy administration system | Source of truth for policy status | Inferred |
| SYS-003 | API gateway / identity provider | AuthN/AuthZ, rate limiting | Inferred — Unknown if exists (Q-004) |

### 3. Requirements

| ID | Requirement | Type | Source | Status |
|---|---|---|---|---|
| BRQ-001 | An authorized partner shall be able to obtain the current status of a policy through an API. | Business | S1 | Proposed |
| FR-001 | The API shall return the status of a policy identified by `TBD` (policy number and/or other keys, Q-002). | Functional | S1 | Pending Validation |
| FR-002 | The API shall return only policies the calling partner is authorized to see (authorization model `TBD`, Q-003). | Functional | Inferred | Pending Validation |
| FR-003 | The response shall contain the fields agreed in the contract (`TBD`, Q-005) and the timestamp of the status. | Functional | Inferred | Pending Validation |
| FR-004 | The API shall return distinct, documented error responses for: unauthenticated, unauthorized, policy not found, invalid request, rate limit exceeded, upstream unavailable. | Functional | Inferred | Proposed |
| FR-005 | Responses for "not found" and "not authorized for this policy" shall not allow a partner to infer the existence of policies it cannot access (behaviour `TBD` with security, Q-008). | Functional / Security | Inferred | Pending Validation |
| FR-006 | Each request shall be logged with partner identity, policy reference, timestamp and outcome. | Functional | Inferred | Proposed |
| NFR-001 | Authentication mechanism: `TBD` (e.g. OAuth 2.0 client credentials, mTLS, API key — options only; decision by security, Q-004). | Security | — | Pending Validation |
| NFR-002 | Availability and response-time targets: `TBD` (Q-006). | Performance / Availability | — | Pending Validation |
| NFR-003 | Rate limit per partner: `TBD` (Q-006). | Capacity | — | Pending Validation |
| NFR-004 | Data exposure shall follow the data-sharing agreement and applicable data-protection obligations as determined by the data protection owner (no assumption made here). | Privacy / Compliance | Inferred | Pending Validation (Q-007) |
| NFR-005 | The API shall be versioned and documented in a machine-readable contract (e.g. OpenAPI). | Maintainability | Inferred | Proposed |
| NFR-006 | Data freshness: maximum acceptable delay between a status change and its visibility in the API = `TBD` (Q-009). | Data quality | — | Pending Validation |

### 4. Business rules (all pending — none stated by the business)

| Rule ID | Name | Condition | Expected action | Status |
|---|---|---|---|---|
| BR-001 | Status catalog | A policy status is returned | Value belongs to the agreed status list (`TBD`, Q-001), mapped from SYS-002 internal statuses | Pending Validation |
| BR-002 | Partner–policy entitlement | Partner requests a policy | Allowed only if the partner is linked to that policy under `TBD` criteria (Q-003) | Pending Validation |
| BR-003 | Non-disclosure on denial | Partner not entitled | Response does not reveal policy existence (Q-008) | Proposed |

### 5. Authentication and authorization scenarios

| # | Scenario | Expected behaviour |
|---|---|---|
| A1 | Missing or invalid credentials | Rejected as unauthenticated; no policy data |
| A2 | Valid credentials, expired/revoked | Rejected as unauthenticated |
| A3 | Valid partner, policy not entitled | Response per BR-003 (Q-008) |
| A4 | Valid partner, entitled policy | Status returned |
| A5 | Valid partner exceeds rate limit | Rejected as rate-limited with retry guidance |
| A6 | Credentials of partner X used to query partner Y's policies | Treated as A3; logged (FR-006) |

### 6. Error handling requirements

| Situation | Expected behaviour | HTTP status (proposed, REST convention) |
|---|---|---|
| Malformed request / invalid identifier format | Validation error with field detail | 400 |
| Not authenticated | Error without data | 401 |
| Authenticated, not authorized | Per BR-003 | 403 or 404 (Q-008) |
| Policy not found | Not found | 404 |
| Rate limit exceeded | Error + retry hint | 429 |
| Policy system unavailable / timeout | Error, no stale data unless allowed (Q-009) | 503 / 504 |

Status codes are proposals following common REST practice; the final contract is decided with the API owner.

### 7. Stories

**EP-01 — Partner policy status API**

#### US-001 — Query status of an entitled policy
**Type:** Story · **As a** partner system **I want** to request the status of a policy I am entitled to
**So that** I can inform my customers without contacting the insurer manually (benefit Inferred, Q-010)
**Acceptance Criteria:**
- **US-001-AC01 (positive)** Given an authenticated partner entitled to policy `POL-TEST-0001`, When it requests its status, Then the response contains the status (from BR-001 catalog) and the status timestamp.
- **US-001-AC02 (negative)** Given a policy identifier with an invalid format, When requested, Then a validation error is returned and no lookup is performed.
- **US-001-AC03 (negative)** Given an identifier that matches no policy, When requested, Then a not-found error is returned.
- **US-001-AC04 (negative)** Given the policy system does not respond within `TBD`, When requested, Then an upstream-unavailable error is returned.
**Business Rules:** BR-001, BR-002 · **Traces to:** FR-001, FR-003, FR-004 · **Priority:** Must (Proposed)
**Definition of Ready Status:** Not Ready — Q-001, Q-002, Q-005 open.

#### US-002 — Reject unauthenticated and unauthorized requests (Enabler)
**As a** insurer security owner **I want** only authenticated, entitled partners to get policy data **So that** policy information is not exposed
**Acceptance Criteria:**
- **US-002-AC01 (negative)** Given no credentials, When a request is made, Then it is rejected as unauthenticated and logged.
- **US-002-AC02 (negative)** Given valid credentials for a partner not entitled to the policy, When requested, Then the response follows BR-003 and is logged.
- **US-002-AC03 (negative)** Given revoked credentials, When a request is made, Then it is rejected as unauthenticated.
**Traces to:** FR-002, FR-005, FR-006, NFR-001 · **Priority:** Must (Proposed)
**Definition of Ready Status:** Not Ready — authentication mechanism (Q-004) and entitlement model (Q-003).

#### US-003 — Enforce rate limits per partner (Enabler)
**Acceptance Criteria:** **US-003-AC01 (negative)** Given a partner over its limit `TBD`, When it sends another request, Then the request is rejected as rate-limited with retry guidance.
**Traces to:** NFR-003 · **Definition of Ready Status:** Not Ready — Q-006.

#### US-004 — Publish the API contract and sandbox for the partner (Enabler)
**Acceptance Criteria:** **US-004-AC01** Given the contract is approved, When the partner team accesses the developer documentation, Then it finds the versioned contract, error catalog and test credentials for a non-production environment.
**Traces to:** NFR-005 · **Dependencies:** US-001, US-002 · **Definition of Ready Status:** Not Ready — sandbox availability unknown (Q-011).

### 8. Dependencies, constraints and risks

| ID | Item | Type |
|---|---|---|
| DEP-001 | Mapping of internal statuses to the partner catalog by the policy business owner | Decision |
| DEP-002 | Security approval of the authentication mechanism | Decision |
| DEP-003 | Data-sharing agreement with the partner | Legal / commercial |
| RSK-001 | Exposure of policy data to the wrong partner — Impact High, Likelihood unknown; mitigation: US-002, entitlement tests, logging | Risk |
| RSK-002 | Internal status changes break the partner contract — Medium/Medium; mitigation: mapping layer + versioning | Risk |
| RSK-003 | Policy system load from partner traffic — unknown; mitigation: rate limits, capacity check | Risk |

### 9. Open questions (prioritized)

| ID | Priority | Question |
|---|---|---|
| Q-001 | Blocking | Which statuses may be shared with partners and what does each mean? |
| Q-003 | Blocking | How is a partner entitled to a policy (intermediary of record, contract, product line)? |
| Q-004 | Blocking | Which authentication mechanism does security mandate for partner APIs? Is there a gateway? |
| Q-005 | Blocking | Which fields beyond status may be returned (if any)? |
| Q-007 | Blocking | Is there a data-sharing agreement, and who confirms data-protection obligations? |
| Q-002 | Important | Which identifier(s) does the partner have — policy number, customer reference? |
| Q-008 | Important | Should unauthorized and not-found be indistinguishable to the partner? |
| Q-006 | Important | Expected volumes, peaks, rate limits and availability targets? |
| Q-009 | Important | How fresh must the status be? Is cached data acceptable during outages? |
| Q-010 | Minor | What will the partner do with the status (confirms the business value)? |
| Q-011 | Minor | Is there a sandbox environment for partners? |

### 10. Limitations

Analysis from a single sentence. No regulatory conclusions are drawn; security mechanisms are listed
only as options for the security owner. HTTP codes are proposals.

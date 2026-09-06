# RAW OS v1.0 — System Design Specification
## 1. API Specification

**Status:** Draft System Design Specification  
**Layer:** Technology-Agnostic API Contract  
**Depends on:** RAW OS v0.1–v0.8  
**Principle:** API implements RAW OS semantics; API does not redefine RAW OS governance.

---

## 1. Purpose

This specification defines the API layer for RAW OS v1.0. The API exposes core RAW OS objects, decision flows, authority checks, risk/control gates, events, evidence and integration interfaces in a machine-readable contract.

The API is an implementation boundary between RAW OS core logic and applications, external systems, user interfaces, AI agents and operational services.

**Core principle:**

`RAW OS CORE → API CONTRACT → IMPLEMENTATION / CLIENTS`

---

## 2. API Design Principles

1. **Semantic Fidelity** — API objects must map to RAW OS ontology.
2. **Explicit Authority** — every protected operation is evaluated against authority.
3. **Least Privilege** — clients receive only required capabilities.
4. **Traceability** — significant requests, decisions and actions are attributable.
5. **Idempotency** — repeatable operations must not create uncontrolled duplicate effects.
6. **Versioning** — contracts evolve without silently changing existing semantics.
7. **Fail Securely** — ambiguous identity, authority or critical control state defaults to deny/hold/escalate.
8. **Observable by Default** — security, performance and governance events are measurable.
9. **Domain-Neutrality** — the API core remains reusable across domains.
10. **Separation of Concerns** — governance logic remains distinct from transport and UI concerns.

---

## 3. API Logical Layers

### 3.1 Identity & Access Layer
Handles authentication, client identity, actor identity, role and token/session context.

### 3.2 Governance Layer
Resolves purpose, scope, policy, authority, rule and governance status.

### 3.3 Decision Layer
Creates, evaluates, approves, escalates and records decisions.

### 3.4 Risk & Control Layer
Assesses risk and applies controls, thresholds and intervention logic.

### 3.5 Action Layer
Authorises and executes bounded actions.

### 3.6 Event & State Layer
Receives events and maintains state transitions.

### 3.7 Evidence & Audit Layer
Records evidence, traceability and audit information.

### 3.8 Integration Layer
Connects external systems through adapters and canonical objects.

---

## 4. Canonical Resource Model

The API should expose the following canonical resources:

- `/systems`
- `/actors`
- `/roles`
- `/capabilities`
- `/authorities`
- `/purposes`
- `/boundaries`
- `/rules`
- `/policies`
- `/inputs`
- `/decisions`
- `/actions`
- `/events`
- `/states`
- `/risks`
- `/controls`
- `/outcomes`
- `/evidence`
- `/feedback`
- `/integrations`
- `/audit`

Not every implementation must expose every resource publicly. Internal APIs may remain private while preserving the same semantic model.

---

## 5. Base Request Context

Every significant API request should carry or resolve a request context containing:

```json
{
  "request_id": "string",
  "correlation_id": "string",
  "actor_id": "string",
  "client_id": "string",
  "system_id": "string",
  "role_id": "string",
  "authority_context": "object",
  "timestamp": "datetime",
  "purpose_context": "string",
  "source": "string"
}
```

`request_id` identifies the individual request. `correlation_id` connects related requests/events across systems.

---

## 6. Authentication

Authentication answers **who is communicating with RAW OS**.

Supported conceptual identity types:

- Human user
- Service account
- AI agent
- External organisation
- External system
- Internal process

Authentication implementation is intentionally technology-neutral at v1.0 design stage.

---

## 7. Authorisation

Authorisation answers **what the identified actor is allowed to do**.

Evaluation sequence:

`IDENTITY → ROLE → CAPABILITY → AUTHORITY → SCOPE → CONDITION → DECISION`

A successful authentication must never be treated as automatic authorisation.

### 7.1 Authorisation Result

```json
{
  "authorised": true,
  "actor_id": "ACT-001",
  "authority_id": "AUTH-021",
  "scope": "defined-scope",
  "constraints": [],
  "expires_at": "datetime|null",
  "reason": "string"
}
```

---

## 8. Purpose & Scope APIs

### `POST /purposes`
Creates a purpose definition.

### `GET /purposes/{purpose_id}`
Retrieves a purpose.

### `POST /boundaries`
Creates or updates system boundaries.

### `GET /systems/{system_id}/boundary`
Retrieves system scope, exclusions and escalation boundaries.

Purpose and boundary changes are governance-controlled operations.

---

## 9. Actor & Authority APIs

### `POST /actors`
Register an actor.

### `POST /roles`
Create a role.

### `POST /capabilities`
Define a capability.

### `POST /authorities`
Create a bounded authority assignment.

### `GET /actors/{actor_id}/authorities`
Retrieve applicable authority.

### `POST /authorisation/check`
Evaluate whether an actor can perform an operation.

Example request:

```json
{
  "actor_id": "ACT-001",
  "action_type": "ACTION_TYPE",
  "resource": "RESOURCE_ID",
  "scope": "SCOPE_ID",
  "context": {}
}
```

---

## 10. Rule & Policy APIs

### `POST /rules`
Create a rule.

### `GET /rules/{rule_id}`
Retrieve a rule.

### `POST /policies`
Create a policy.

### `POST /policies/{policy_id}/publish`
Publish an approved version.

### `POST /policies/{policy_id}/retire`
Retire a policy.

Rules should support explicit conditions, permissions, requirements, constraints and precedence.

Conceptual rule form:

```text
IF condition
THEN decision/action
SUBJECT TO constraint
WITH authority
```

---

## 11. Decision APIs

### `POST /decisions`
Create a decision request.

### `POST /decisions/{decision_id}/assess`
Attach assessment, evidence, rule and risk context.

### `POST /decisions/{decision_id}/authorise`
Perform authority check and approval.

### `POST /decisions/{decision_id}/reject`
Reject a decision.

### `POST /decisions/{decision_id}/escalate`
Escalate to a higher authority.

### `GET /decisions/{decision_id}`
Retrieve complete decision record.

Decision lifecycle:

`PROPOSED → ASSESSED → AUTHORISED → CONTROLLED → EXECUTING → COMPLETED`

Alternative states:

`REJECTED | ESCALATED | ON_HOLD | FAILED | OVERRIDDEN | CANCELLED`

---

## 12. Risk APIs

### `POST /risks`
Register a risk.

### `POST /risks/{risk_id}/assess`
Assess probability, impact, exposure and severity.

### `GET /risks/{risk_id}`
Retrieve current risk state.

### `POST /risks/{risk_id}/mitigate`
Record mitigation/control treatment.

Risk gate:

`DECISION → RISK ASSESSMENT → THRESHOLD → CONTROL REQUIREMENT → PROCEED / ESCALATE / STOP`

---

## 13. Control APIs

### `POST /controls`
Register a control.

### `POST /controls/{control_id}/evaluate`
Evaluate control status.

### `POST /controls/{control_id}/trigger`
Trigger an intervention.

### `GET /controls/{control_id}/history`
Retrieve control execution history.

Control types include:

- Preventive
- Detective
- Corrective
- Compensating
- Escalation
- Approval
- Constraint

---

## 14. Action APIs

### `POST /actions`
Submit an action for execution.

### `POST /actions/{action_id}/execute`
Execute an authorised action.

### `POST /actions/{action_id}/cancel`
Cancel a pending action.

Before execution, system should verify:

`AUTHORITY + RULE + RISK + CONTROL + THRESHOLD + APPROVAL`

Action responses must provide an execution result and evidence reference.

---

## 15. Event APIs

### `POST /events`
Receive or record an event.

### `GET /events/{event_id}`
Retrieve an event.

### `POST /events/{event_id}/process`
Process event against applicable rules and state transition logic.

Canonical event:

```json
{
  "event_id": "EVT-001",
  "event_type": "string",
  "source": "string",
  "timestamp": "datetime",
  "actor_id": "string|null",
  "correlation_id": "string",
  "payload": {},
  "authority_context": {}
}
```

---

## 16. State APIs

### `GET /states/{object_type}/{object_id}`
Retrieve current state.

### `POST /state-transitions/evaluate`
Evaluate whether a requested transition is valid.

State logic:

`CURRENT STATE → EVENT → CONTROL CHECK → AUTHORISED TRANSITION → NEW STATE`

Invalid transitions are rejected or escalated according to policy.

---

## 17. Evidence & Audit APIs

### `POST /evidence`
Record evidence.

### `GET /evidence/{evidence_id}`
Retrieve evidence metadata/content reference.

### `GET /audit/{object_type}/{object_id}`
Retrieve audit trail.

Minimum evidence metadata:

- Evidence ID
- Source
- Timestamp
- Actor/system
- Related request
- Decision ID
- Action ID
- Event ID
- Integrity metadata
- Retention classification

Evidence should allow reconstruction of significant system activity.

---

## 18. Feedback APIs

### `POST /feedback`
Submit feedback.

### `POST /reviews`
Create a governance or operational review.

### `POST /adaptations`
Propose a rule, policy, control or capability update.

Adaptation lifecycle:

`FEEDBACK → REVIEW → PROPOSAL → IMPACT ASSESSMENT → APPROVAL → VERSION UPDATE → MONITOR`

---

## 19. Integration APIs

### `POST /integrations`
Register an external integration.

### `POST /integrations/{integration_id}/validate`
Validate configuration and trust boundary.

### `POST /integrations/{integration_id}/events`
Receive an external event through the integration adapter.

### `POST /integrations/{integration_id}/actions`
Request a bounded external action.

Integration pattern:

`EXTERNAL SYSTEM → ADAPTER → CANONICAL OBJECT → RAW OS GOVERNANCE → ACTION → EXTERNAL SYSTEM`

---

## 20. API Error Model

Errors should be machine-readable and governance-relevant.

```json
{
  "error": {
    "code": "AUTHORITY_DENIED",
    "message": "Action is outside actor authority.",
    "request_id": "REQ-001",
    "correlation_id": "CORR-001",
    "retryable": false,
    "escalation_required": true
  }
}
```

Recommended error classes:

- `AUTHENTICATION_FAILED`
- `AUTHORISATION_DENIED`
- `AUTHORITY_EXPIRED`
- `BOUNDARY_VIOLATION`
- `RULE_VIOLATION`
- `RISK_THRESHOLD_EXCEEDED`
- `CONTROL_FAILED`
- `APPROVAL_REQUIRED`
- `ESCALATION_REQUIRED`
- `INVALID_STATE_TRANSITION`
- `CONFLICT`
- `DUPLICATE_REQUEST`
- `DEPENDENCY_UNAVAILABLE`
- `VALIDATION_FAILED`
- `INTERNAL_GOVERNANCE_ERROR`

---

## 21. Idempotency & Transaction Safety

Significant write operations should support an idempotency mechanism.

Example:

`Idempotency-Key: unique-client-generated-key`

A repeated request with the same key and equivalent payload should return the original result rather than silently execute the action again.

For multi-step operations, the system should preserve transaction state and reconcile partial failures.

---

## 22. Concurrency & Consistency

The API must explicitly handle competing changes to decision, state, authority and policy objects.

Recommended conceptual mechanisms:

- Version number
- Optimistic concurrency
- Effective timestamp
- State transition validation
- Conflict detection
- Reconciliation

A stale client must not overwrite a newer governance state silently.

---

## 23. Webhooks / Event Delivery

External consumers may receive events such as:

- `decision.created`
- `decision.authorised`
- `decision.escalated`
- `action.executed`
- `risk.threshold_exceeded`
- `control.failed`
- `boundary.violated`
- `policy.published`
- `state.changed`
- `integration.failed`

Event delivery must include correlation identifiers and replay/retry handling appropriate to implementation.

---

## 24. AI Agent API Contract

An AI agent may call RAW OS only through explicit capabilities and authority.

Minimum agent context:

```json
{
  "agent_id": "AGENT-001",
  "role_id": "ROLE-AGENT",
  "capability_set": [],
  "authority_id": "AUTH-AGENT-001",
  "scope": {},
  "risk_class": "medium",
  "human_oversight_mode": "human-on-the-loop"
}
```

AI actions should be classified as:

- Advisory
- Decision-support
- Delegated action
- Monitoring
- Orchestration

AI-generated recommendation does not itself constitute authorisation.

---

## 25. Human Oversight API Contract

The API must support explicit human intervention states where configured.

Operations may include:

- `approve`
- `reject`
- `request_more_information`
- `escalate`
- `override`
- `hold`
- `resume`
- `cancel`

Overrides require stronger evidence and auditability than ordinary operations.

---

## 26. Security & Governance Requirements

API implementation must address:

- Authentication
- Authorisation
- Least privilege
- Input validation
- Output validation
- Secure transport
- Credential protection
- Rate limiting
- Abuse detection
- Audit logging
- Data minimisation
- Secret rotation
- Revocation
- Incident handling

Security controls must not silently remove governance evidence.

---

## 27. Observability Requirements

Minimum operational signals:

- Request latency
- Error rates
- Authorisation denials
- Escalation frequency
- Control failures
- Risk threshold events
- State-transition failures
- Integration failures
- Audit/evidence write failures

Governance signals should be distinguishable from ordinary technical telemetry.

---

## 28. API Versioning

Recommended initial external contract:

`/api/v1/...`

Versioning rules:

1. No breaking semantic change within the same major version.
2. Deprecations must be documented.
3. Object ontology changes require impact assessment.
4. Rule/policy versions are independent from API versions.
5. Adapter versions must be traceable.

---

## 29. API Compatibility Requirement

An implementation is API-compatible with RAW OS when it preserves the semantic chain:

`PURPOSE → SCOPE → ACTOR → AUTHORITY → RULE → DECISION → RISK → CONTROL → ACTION → EVENT → OUTCOME → EVIDENCE → FEEDBACK`

A different transport technology is acceptable if this semantic chain remains intact.

---

## 30. API Governance Gate

Before an API operation is exposed as production-capable, verify:

`PURPOSE → ACTOR → AUTHORITY → RULE → RISK → CONTROL → EVIDENCE → FAILURE PATH`

If any required governance element is unresolved, the operation should remain unavailable, constrained or require escalation.

---

## 31. Implementation Boundary

This v1.0 API specification does **not** prescribe:

- REST as the only protocol
- GraphQL as an alternative or mandatory protocol
- a particular programming language
- a particular database
- a particular cloud provider
- a particular identity provider
- a particular AI model

These are implementation decisions beneath the API contract.

---

## 32. Reference Architecture

```text
CLIENTS / UI / AI AGENTS / EXTERNAL SYSTEMS
                    ↓
              API GATEWAY
                    ↓
          IDENTITY + AUTHORISATION
                    ↓
        ┌──────── RAW OS CORE ────────┐
        │ Governance                  │
        │ Decision                    │
        │ Risk                        │
        │ Control                     │
        │ State / Event               │
        │ Evidence / Audit            │
        └─────────────────────────────┘
                    ↓
             SERVICE / ADAPTER
                    ↓
       DATABASE / MESSAGE / TOOLING
```

The diagram is conceptual. Concrete deployment architecture belongs to subsequent system design specifications.

---

## 33. Design Freeze Criteria for API

API design may proceed to implementation when:

- Canonical objects are stable.
- Authority semantics are stable.
- Decision states are stable.
- Risk/control gates are stable.
- Evidence requirements are stable.
- Integration boundary is stable.
- Error classes cover major governance failures.
- Versioning strategy is defined.
- Security baseline is defined.
- Evaluation tests can be written against the contract.

---

## 34. Traceability

Every implemented endpoint should map back to the framework:

`RAW OS INVARIANT → ONTOLOGY OBJECT → GOVERNANCE REQUIREMENT → API ENDPOINT → IMPLEMENTATION → TEST → EVIDENCE`

This traceability chain is mandatory for high-impact operations.

---

## 35. Next System Design Specifications

After API design, the recommended sequence is:

**2. Database Architecture**  
**3. UI/UX Architecture**  
**4. AI / Agent Architecture**  
**5. Security Architecture**  
**6. Event & Integration Implementation**  
**7. SOP / Operational Specification**  
**8. Deployment & Infrastructure Specification**

**Status:** RAW OS v1.0 — API Specification, Draft for implementation planning.

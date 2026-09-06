# RAW OS v1.0 — System Design Specification
## 4. Event & State Architecture

**Status:** Foundational System Design Specification  
**Depends on:** RAW OS v0.1–v0.8, v1.0 API, v1.0 Algorithm Architecture, v1.0 Database Architecture

---

## 1. Purpose

The Event & State Architecture defines how RAW OS represents change over time. It establishes the relationship between events, state transitions, decisions, actions, outcomes and evidence.

The architecture is designed to make significant system behaviour observable, traceable, replayable, recoverable and auditable.

Core principle:

> **Events describe what happened; state describes what is true now.**

---

## 2. Core Model

```text
ENVIRONMENT / INPUT
        ↓
      EVENT
        ↓
   EVENT VALIDATION
        ↓
   CONTEXT RESOLUTION
        ↓
   RULE / CONTROL CHECK
        ↓
  STATE TRANSITION
        ↓
 DECISION / ACTION
        ↓
      OUTCOME
        ↓
     NEW EVENT
        ↓
     EVIDENCE
```

State is therefore not an isolated record. It is the current representation resulting from a sequence of authorised transitions.

---

## 3. Event Definition

An **Event** is an observable occurrence that may cause, represent or confirm a change in the system.

Typical event categories:

- Input event
- Request event
- Decision event
- Authorisation event
- Action event
- State transition event
- Risk event
- Control event
- Exception event
- Integration event
- Failure event
- Recovery event
- Outcome event
- Audit event
- Governance event

Minimum conceptual event object:

```text
Event ID
Event Type
Source
Actor / System
Timestamp
Correlation ID
Causation ID
Payload
Context
Authority Context
Schema Version
Integrity Metadata
```

---

## 4. Event Principles

### 4.1 Event Immutability

Once a significant event has been committed to the authoritative event history, the historical event should not be silently rewritten.

Corrections should be represented through compensating or corrective events.

### 4.2 Event Ordering

Events require deterministic ordering within their relevant scope.

Where absolute ordering cannot be guaranteed, RAW OS should use timestamps, sequence numbers, correlation IDs and causation IDs to establish reconstructable relationships.

### 4.3 Event Identity

Every event must have a unique identifier.

### 4.4 Event Causality

Where practical, an event should identify what caused it.

```text
CAUSE EVENT → CAUSATION ID → RESULT EVENT
```

### 4.5 Event Correlation

Multiple events belonging to one transaction, case or workflow should share a correlation identifier.

---

## 5. State Definition

A **State** is the authoritative representation of the condition of a system or object at a specific point in time.

Examples:

```text
Decision: PROPOSED
Decision: AUTHORISED
Decision: REJECTED

Action: PENDING
Action: EXECUTING
Action: COMPLETED
Action: FAILED

Integration: CONNECTED
Integration: DEGRADED
Integration: DISCONNECTED
```

A state should be:

- Explicit
- Validated
- Transitionable
- Observable
- Versioned where required
- Recoverable

---

## 6. State Transition Model

Core transition:

```text
CURRENT STATE
     ↓
EVENT / TRIGGER
     ↓
PRECONDITION CHECK
     ↓
AUTHORITY CHECK
     ↓
CONTROL CHECK
     ↓
VALID TRANSITION?
   ↙          ↘
 YES           NO
 ↓              ↓
NEW STATE    REJECT / ESCALATE
```

Formal conceptual expression:

```text
S(t+1) = Transition(S(t), E, Rules, Authority, Controls)
```

A transition must not occur merely because a technically possible action exists.

---

## 7. State Machine Principles

### 7.1 Valid Transition

A transition is valid only when its preconditions are satisfied.

### 7.2 Invalid Transition

Invalid transitions should be rejected, held or escalated according to governance configuration.

### 7.3 Terminal State

Some states cannot be exited except through explicit recovery, override or correction logic.

Examples:

```text
REJECTED
CANCELLED
CLOSED
COMPLETED
```

### 7.4 Recovery State

A system may enter a recovery state after failure.

```text
FAILED → RECOVERY → VERIFIED → RESUMED / CLOSED
```

---

## 8. Decision State Machine

Reference decision lifecycle:

```text
DRAFT / PROPOSED
       ↓
    ASSESSED
       ↓
  AUTHORISATION
     ↙     ↘
 APPROVED  REJECTED
    ↓
 CONTROLLED
    ↓
 EXECUTED
    ↓
 COMPLETED
```

Alternative paths:

```text
ASSESSED → ESCALATED
AUTHORISATION → ON HOLD
EXECUTING → FAILED
COMPLETED → REVIEWED
```

---

## 9. Action State Machine

```text
REQUESTED
   ↓
VALIDATED
   ↓
AUTHORISED
   ↓
SCHEDULED
   ↓
EXECUTING
   ↓
COMPLETED
```

Failure path:

```text
EXECUTING → FAILED → RETRY / COMPENSATE / ESCALATE
```

Cancellation path:

```text
REQUESTED / SCHEDULED → CANCELLED
```

---

## 10. Event Sourcing Principle

For suitable high-value domains, RAW OS may use event sourcing where the sequence of authoritative events forms the historical record and current state is derived from those events.

```text
EVENT 1 → EVENT 2 → EVENT 3 → EVENT 4
                  ↓
             STATE REBUILD
```

Event sourcing is an implementation option, not a mandatory requirement for every RAW OS deployment.

---

## 11. State Snapshot Principle

Where replaying a long event history is inefficient, a system may maintain snapshots.

```text
EVENT 1 → EVENT 2 → EVENT 3 → SNAPSHOT A
                                  ↓
                         EVENT 4 → EVENT 5
                                  ↓
                              SNAPSHOT B
```

Snapshots must never destroy the authoritative history where auditability requires preservation.

---

## 12. Event Replay

Replay allows the system to reconstruct state from historical events.

```text
HISTORICAL EVENTS
       ↓
VALIDATE VERSION / RULE CONTEXT
       ↓
REPLAY TRANSITIONS
       ↓
RECONSTRUCT STATE
       ↓
COMPARE WITH STORED STATE
```

Replay can support:

- Audit
- Investigation
- Recovery
- Simulation
- Debugging
- Regression testing
- Historical analysis

Historical replay must preserve the distinction between **what happened then** and **what current rules would do now**.

---

## 13. Temporal Logic

RAW OS systems should distinguish at least three temporal concepts where relevant:

- **Event Time** — when something happened in the represented domain.
- **Processing Time** — when RAW OS processed the event.
- **Effective Time** — when a rule, policy, state or decision became effective.

This enables historical reconstruction without confusing delayed processing with the original occurrence.

---

## 14. Causation & Correlation

### Causation

Describes direct or logical cause.

```text
EVENT A → CAUSED → EVENT B
```

### Correlation

Groups related events that belong to a common workflow or case.

```text
CORRELATION ID = CASE / TRANSACTION / WORKFLOW
```

A correlation does not prove causation.

---

## 15. Event Validation

Before an event is accepted into the governed system:

```text
RECEIVE
  ↓
IDENTIFY SOURCE
  ↓
VALIDATE STRUCTURE
  ↓
VALIDATE IDENTITY
  ↓
VALIDATE AUTHORITY / TRUST
  ↓
VALIDATE TIMESTAMP / VERSION
  ↓
DEDUPLICATE
  ↓
ACCEPT / REJECT / QUARANTINE
```

Validation requirements depend on event criticality.

---

## 16. Idempotency

A repeated delivery of the same event must not unintentionally produce repeated side effects.

RAW OS should support an idempotency mechanism for significant externally triggered operations.

```text
EVENT ID / IDEMPOTENCY KEY
        ↓
ALREADY PROCESSED?
   ↙           ↘
 YES            NO
 ↓               ↓
RETURN RESULT   PROCESS
```

---

## 17. Duplicate Event Handling

Duplicate event detection may use:

- Event ID
- Source transaction ID
- Idempotency key
- Sequence number
- Content fingerprint
- Correlation context

Duplicates should be safely ignored, reconciled or flagged according to event semantics.

---

## 18. Out-of-Order Events

When events arrive out of order:

```text
DETECT ORDER CONFLICT
        ↓
ASSESS BUFFER WINDOW
        ↓
REORDER / WAIT / RECONCILE
        ↓
APPLY TRANSITION
        ↓
RECORD DECISION
```

The system must not silently apply an event to an incompatible state merely because the event arrived late.

---

## 19. Concurrency & Race Conditions

Multiple actors or systems may attempt to change the same state.

RAW OS should support appropriate concurrency control, such as:

- Version checks
- Optimistic locking
- Transaction boundaries
- State preconditions
- Conflict detection
- Serialisation for critical transitions

Conceptual logic:

```text
READ STATE VERSION
      ↓
PROPOSE TRANSITION
      ↓
VERSION STILL VALID?
   ↙          ↘
 YES           NO
 ↓              ↓
COMMIT       CONFLICT
               ↓
           RETRY / REVIEW
```

---

## 20. State Consistency

State must be consistent with authoritative events and the applicable governance context.

Consistency checks may compare:

```text
CURRENT STATE
     ↕
EVENT HISTORY
     ↕
DECISION RECORD
     ↕
ACTION RECORD
     ↕
EXTERNAL SYSTEM STATE
```

Detected inconsistencies enter a reconciliation path.

---

## 21. Reconciliation

```text
STATE CONFLICT
     ↓
IDENTIFY SOURCES OF TRUTH
     ↓
ASSESS AUTHORITY / FRESHNESS
     ↓
COMPARE EVIDENCE
     ↓
RESOLVE / ESCALATE
     ↓
WRITE RECONCILIATION EVENT
     ↓
UPDATED STATE
```

Reconciliation decisions must be auditable for material conflicts.

---

## 22. Failure Semantics

Failures should be explicit events, not merely missing records.

Examples:

```text
ACTION_FAILED
CONTROL_FAILED
AUTHORIZATION_FAILED
INTEGRATION_FAILED
TIMEOUT
DATA_VALIDATION_FAILED
STATE_CONFLICT
```

Every material failure should produce sufficient evidence for recovery and review.

---

## 23. Recovery Logic

```text
FAILURE EVENT
     ↓
CONTAIN
     ↓
PRESERVE STATE / EVIDENCE
     ↓
ASSESS RECOVERABILITY
     ↓
RETRY / ROLLBACK / COMPENSATE / ESCALATE
     ↓
VERIFY
     ↓
RESUME / CLOSE
```

Where rollback is not technically or operationally possible, compensating actions should restore an acceptable governed state.

---

## 24. Event → Decision → Action Trace

A complete significant workflow should be reconstructable as:

```text
TRIGGER EVENT
     ↓
ASSESSMENT
     ↓
DECISION
     ↓
AUTHORITY
     ↓
CONTROL
     ↓
ACTION
     ↓
OUTCOME
     ↓
EVIDENCE
```

Each step should be linked using identifiers and timestamps sufficient to establish lineage.

---

## 25. External Event Integration

External events enter through the Integration Framework:

```text
EXTERNAL EVENT
     ↓
ADAPTER
     ↓
VALIDATION
     ↓
CANONICAL EVENT
     ↓
RAW OS STATE / DECISION LOGIC
```

RAW OS should not assume that an external event is trustworthy merely because it was received through a connected interface.

---

## 26. Event Versioning

Event schemas must be versioned when changes may affect interpretation.

```text
EVENT TYPE
SCHEMA VERSION
PAYLOAD VERSION
PRODUCER VERSION
RAW OS VERSION
```

Consumers must either support the version or fail safely.

---

## 27. Event Retention

Retention is determined by:

- Legal requirements
- Governance requirements
- Audit requirements
- Operational requirements
- Privacy requirements
- Data sensitivity
- Business continuity needs

Retention policy must not silently destroy evidence needed for accountability or legally required records.

---

## 28. State Security

State and event access should respect:

- Identity
- Role
- Authority
- Data sensitivity
- Purpose
- Segregation of duties

Read access and write/transition authority should be treated separately where appropriate.

---

## 29. Observability

The Event & State layer should expose sufficient telemetry to understand system behaviour.

Key observability dimensions:

- Event throughput
- Event latency
- Transition success/failure
- State conflicts
- Retry frequency
- Escalations
- Control failures
- External integration failures
- Evidence gaps

---

## 30. Simulation & Testing

Event and state architecture supports deterministic scenario testing.

```text
INITIAL STATE
     ↓
EVENT SEQUENCE
     ↓
EXPECTED TRANSITIONS
     ↓
OBSERVED TRANSITIONS
     ↓
COMPARE
     ↓
PASS / FAIL
```

Test cases should include normal, boundary, invalid, adversarial, delayed, duplicated and conflicting events.

---

## 31. Determinism & Reproducibility

Where deterministic behaviour is required, the system should preserve sufficient context to reproduce a decision or state transition, including relevant:

- Input
- Rule version
- Policy version
- Authority context
- Model / algorithm version
- Configuration
- Timestamp context
- External dependencies

Not every AI or probabilistic process will be perfectly reproducible; in those cases, RAW OS should preserve the relevant execution evidence and uncertainty metadata.

---

## 32. Event & State Security Boundary

A state transition is a privileged operation.

Therefore:

```text
EVENT ≠ AUTOMATIC PERMISSION
```

An incoming event may trigger evaluation, but only a valid decision/control path may authorise a governed transition where required.

---

## 33. Minimum Event Contract

```text
EVENT_ID
EVENT_TYPE
SOURCE
ACTOR
TIMESTAMP
CORRELATION_ID
CAUSATION_ID
PAYLOAD
SCHEMA_VERSION
AUTHORITY_CONTEXT
INTEGRITY_STATUS
```

---

## 34. Minimum State Contract

```text
OBJECT_ID
OBJECT_TYPE
CURRENT_STATE
STATE_VERSION
LAST_EVENT_ID
LAST_UPDATED
STATE_OWNER
AUTHORITY_CONTEXT
VALID_FROM
VALID_TO / NULL
```

---

## 35. Canonical Event-State Loop

```text
REAL WORLD
    ↓
EVENT
    ↓
VALIDATE
    ↓
INTERPRET
    ↓
CHECK RULE / AUTHORITY / CONTROL
    ↓
TRANSITION
    ↓
STATE UPDATE
    ↓
ACTION
    ↓
OUTCOME
    ↓
NEW EVENT
    ↓
EVIDENCE
    ↓
FEEDBACK
    ↺
```

---

## 36. Design Invariants

The following invariants should remain stable across implementations:

1. Significant state change must be attributable to a trigger or governed transition.
2. Invalid state transitions must not silently succeed.
3. Significant events must be traceable.
4. Historical evidence must not be silently overwritten.
5. Duplicate delivery must not unintentionally duplicate governed side effects.
6. Authority must be checked at the transition boundary where required.
7. Material state conflicts must enter reconciliation or escalation.
8. Recovery must preserve sufficient evidence for review.
9. Event and state semantics must remain version-aware.
10. Current state must remain reconcilable with its authoritative history.

---

## 37. Integration with Previous RAW OS Layers

```text
v0.1 CORE LOGIC
      ↓
v0.2 ONTOLOGY
      ↓
v0.3 DECISION & CONTROL
      ↓
v0.4 OPERATING ARCHITECTURE
      ↓
v0.5 GOVERNANCE
      ↓
v0.6 INTEGRATION
      ↓
v0.7 EVALUATION
      ↓
v0.8 REFERENCE FRAMEWORK
      ↓
v1.0 API
      ↓
v1.0 ALGORITHM
      ↓
v1.0 DATABASE
      ↓
4. EVENT & STATE
```

Event & State Architecture operationalises the temporal dimension of the previous layers.

---

## 38. Boundary of Component 4

This specification does not mandate a particular:

- Event broker
- Database engine
- Message queue
- Streaming platform
- Programming language
- Cloud provider
- Workflow engine

Those decisions belong to implementation-specific architecture.

---

## 39. Next Component

**RAW OS v1.0 — 5. AI / Agent Architecture**

This component will define how AI models and agents become RAW OS actors, how capability is separated from delegated authority, how tools are controlled, how confidence and uncertainty are handled, and how human oversight is integrated into the event/state lifecycle.

---

## 40. Status

**Version:** RAW OS v1.0  
**Component:** 4 — Event & State Architecture  
**Status:** System Design Specification  
**Principle:** Event-driven, state-aware, traceable, recoverable, auditable and governance-controlled

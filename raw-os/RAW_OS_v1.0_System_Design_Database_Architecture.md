# RAW OS v1.0 — System Design Specification
## 3. Database Architecture

### 1. Purpose

This document defines the database architecture for RAW OS v1.0. It translates the RAW OS framework and system ontology into a persistent data architecture without allowing the database to redefine the governance semantics.

**Principle:** RAW OS semantics → canonical data model → database implementation.

The database must support traceability, authority, decisions, risk, controls, state transitions, integration, evidence, auditability and adaptation.

### 2. Design Principles

1. **Ontology-first** — database entities derive from RAW OS objects.
2. **Governance-preserving** — persistence must not silently bypass governance rules.
3. **Traceability-by-design** — significant actions and decisions remain reconstructable.
4. **Separation of concerns** — operational data, governance data and evidence are logically distinguishable.
5. **Temporal awareness** — important objects and relationships may change over time and require version/effective dates.
6. **Least privilege** — data access follows authority and purpose.
7. **Integrity over convenience** — invalid authority, state or relationship transitions must be rejected or escalated.
8. **Portable semantics** — the canonical model is database-engine agnostic.
9. **Auditability** — critical mutations generate appropriate audit/evidence records.
10. **Adaptability** — schema and configuration can evolve without destroying historical meaning.

### 3. Logical Data Domains

The RAW OS database is organised into the following logical domains:

- **Identity & Actors**
- **Governance & Authority**
- **Rules & Policies**
- **Decision & Action**
- **Risk & Control**
- **State & Events**
- **Evidence & Audit**
- **Integration**
- **Performance & Outcomes**
- **Feedback & Change**
- **Configuration & Versioning**

### 4. Core Entities

#### 4.1 System

Represents a bounded RAW OS implementation or governed external system.

Core fields:
- system_id
- system_name
- purpose_id
- boundary_definition
- status
- owner_actor_id
- created_at
- updated_at
- version

#### 4.2 Actor

Represents a human, AI/agent, organisation, process or external system capable of participating in a workflow.

Core fields:
- actor_id
- actor_type
- identity_reference
- status
- organisation_id
- created_at
- updated_at

#### 4.3 Role

Defines the contextual function of an actor.

Core fields:
- role_id
- role_name
- description
- scope
- effective_from
- effective_to
- status

#### 4.4 Capability

Defines what an actor or component can technically or operationally perform.

Core fields:
- capability_id
- capability_type
- description
- risk_class
- status

#### 4.5 Authority

Defines what an actor is legitimately permitted to do.

Core fields:
- authority_id
- actor_id
- role_id
- scope
- authority_level
- conditions
- delegated_by
- effective_from
- effective_to
- revocation_status

**Critical invariant:** capability does not imply authority.

#### 4.6 Purpose

Defines why the system, process or action exists.

Core fields:
- purpose_id
- statement
- objectives
- desired_outcomes
- owner_actor_id
- status

#### 4.7 Boundary

Defines system and action limits.

Core fields:
- boundary_id
- system_id
- in_scope
- out_of_scope
- escalation_conditions
- external_dependencies
- version

#### 4.8 Rule

Defines machine-operationalisable governance logic.

Core fields:
- rule_id
- rule_type
- condition
- effect
- constraint
- priority
- effective_from
- effective_to
- status
- policy_version

#### 4.9 Policy

Defines higher-level governance requirements from which rules and procedures are derived.

Core fields:
- policy_id
- policy_name
- owner_actor_id
- version
- effective_from
- review_date
- status

#### 4.10 Request / Input

Represents incoming demand, signal, data, event or trigger entering a process.

Core fields:
- input_id
- source_actor_id
- source_system_id
- input_type
- payload_reference
- received_at
- validation_status
- correlation_id

#### 4.11 Decision

Represents a significant decision made or proposed by a system or actor.

Core fields:
- decision_id
- decision_type
- actor_id
- role_id
- input_id
- context_reference
- applicable_rule_id
- authority_id
- risk_assessment_id
- rationale
- decision_value
- decision_status
- timestamp
- correlation_id

#### 4.12 Approval / Escalation

Represents governance intervention in the decision path.

Core fields:
- approval_id
- decision_id
- approving_actor_id
- authority_id
- approval_type
- status
- rationale
- timestamp

#### 4.13 Action

Represents an executable activity associated with a decision.

Core fields:
- action_id
- decision_id
- actor_id
- authorisation_reference
- action_type
- target_reference
- constraints
- execution_status
- started_at
- completed_at
- result_reference

#### 4.14 Event

Represents a system occurrence or change.

Core fields:
- event_id
- event_type
- source
- actor_id
- occurred_at
- payload_reference
- correlation_id
- causation_id

#### 4.15 State

Represents the state of a system/object at a point in time.

Core fields:
- state_id
- object_type
- object_id
- state_name
- state_version
- effective_from
- effective_to
- transition_event_id

#### 4.16 Risk

Represents uncertainty or threat with potential impact.

Core fields:
- risk_id
- risk_type
- description
- likelihood
- impact
- exposure
- risk_level
- owner_actor_id
- treatment
- residual_risk
- status

#### 4.17 Control

Represents a preventive, detective, corrective or compensating control.

Core fields:
- control_id
- control_type
- description
- trigger
- threshold
- owner_actor_id
- implementation_reference
- effectiveness_status

#### 4.18 Outcome

Represents measured result or consequence of an action/decision.

Core fields:
- outcome_id
- decision_id
- action_id
- expected_value
- actual_value
- variance
- impact
- measured_at

#### 4.19 Evidence

Represents information needed to demonstrate what happened.

Core fields:
- evidence_id
- evidence_type
- source_reference
- event_id
- decision_id
- action_id
- integrity_reference
- created_at
- retention_class

#### 4.20 Audit Record

Represents a durable record of significant system mutation, governance activity or review.

Core fields:
- audit_id
- event_type
- actor_id
- object_type
- object_id
- action
- before_reference
- after_reference
- timestamp
- correlation_id

### 5. Relationship Model

Core relationships:

```text
SYSTEM
 ├── PURPOSE
 ├── BOUNDARY
 ├── ACTOR
 │    ├── ROLE
 │    ├── CAPABILITY
 │    └── AUTHORITY
 ├── POLICY
 │    └── RULE
 ├── INPUT
 │    └── DECISION
 │         ├── RISK
 │         ├── CONTROL
 │         ├── APPROVAL / ESCALATION
 │         └── ACTION
 │              └── EVENT
 │                   └── STATE
 ├── OUTCOME
 ├── EVIDENCE
 ├── AUDIT
 ├── INTEGRATION
 └── FEEDBACK / CHANGE
```

### 6. Referential Integrity

The database must enforce logical relationships where technically appropriate.

Examples:

- Every significant decision must reference an identifiable actor.
- Every authorised action must reference an authority or approved execution context.
- Every authority must identify its scope and validity period.
- Every risk must have an owner.
- Every control must be associated with the relevant risk, rule or process where applicable.
- Every state transition must reference an event or valid system operation.
- Every critical audit record must reference an object and actor.

### 7. Temporal & Versioned Data

RAW OS requires temporal handling for governance-sensitive objects.

Minimum versionable objects:

- Policy
- Rule
- Authority
- Role assignment
- Control
- Integration contract
- Configuration
- Decision logic
- Schema

Recommended fields:

- version
- effective_from
- effective_to
- created_at
- updated_at
- supersedes_id
- status

Historical records must remain interpretable under the rules that were effective when the event occurred.

### 8. State & Event Persistence

RAW OS uses an event-aware state model.

```text
CURRENT STATE
      ↑
   EVENT LOG
      ↑
ACTION / DECISION
      ↑
INPUT / TRIGGER
```

For critical domains, event history should be append-oriented so the system can reconstruct material state changes.

### 9. Evidence & Audit Store

Evidence and audit data must be logically protected from ordinary operational mutation.

Recommended characteristics:

- append-oriented records
- immutable references where appropriate
- integrity checks
- retention classification
- access logging
- correlation identifiers
- source references
- timestamps
- chain-of-custody metadata where required

### 10. Data Access Model

Data access follows:

```text
IDENTITY → ROLE → AUTHORITY → PURPOSE → DATA ACCESS
```

Access decisions should consider:

- actor identity
- role
- authority scope
- purpose of access
- data classification
- action sensitivity
- environment
- time validity

### 11. Data Classification

A configurable implementation may use classes such as:

- Public
- Internal
- Confidential
- Restricted
- Highly Restricted

Classification itself must be configurable by domain and legal/regulatory requirements.

### 12. Database Integrity Rules

The following are proposed RAW OS invariants:

1. Invalid authority cannot authorise a valid action.
2. Expired authority cannot authorise a new action unless an explicit exception path allows it.
3. A prohibited transition cannot be stored as a successful transition.
4. Critical decision records cannot be silently overwritten.
5. Audit records cannot be modified through ordinary user workflows.
6. Evidence references must remain resolvable for their retention period.
7. Version conflicts must be detected rather than silently accepted.
8. Referentially significant deletions require defined retention/deletion policy.
9. Cross-system transactions require correlation identifiers.
10. Configuration changes require version and ownership metadata.

### 13. Transaction Logic

Critical workflows should use transactional boundaries appropriate to the risk and consistency requirements.

Conceptual pattern:

```text
BEGIN
 → VALIDATE INPUT
 → RESOLVE AUTHORITY
 → EVALUATE RULES
 → ASSESS RISK
 → APPLY CONTROLS
 → COMMIT DECISION / ACTION
 → WRITE EVENT
 → WRITE AUDIT / EVIDENCE REFERENCE
COMMIT
```

If a critical transaction cannot safely complete, the system should fail closed where appropriate and preserve enough evidence to support recovery and reconciliation.

### 14. Concurrency & Idempotency

The database design must support safe handling of duplicate or concurrent requests.

Required concepts:

- idempotency key
- correlation ID
- causation ID
- version / optimistic concurrency token
- transaction status
- conflict state

Duplicate requests must not accidentally create duplicate significant actions.

### 15. Security Architecture

Security controls should be layered across storage and access paths.

- encryption in transit
- encryption at rest where appropriate
- least privilege database roles
- secret management external to source code
- row/object-level access where required
- backup protection
- audit logging
- environment separation
- controlled administrative access

### 16. Integration Persistence

External integrations require persistent mapping records for:

- external system identity
- adapter
- external object ID
- RAW OS object ID
- mapping version
- correlation ID
- sync state
- last known external state
- reconciliation status

### 17. AI / Agent Persistence

AI-related persistence should distinguish:

- agent identity
- model identity/version
- tool permissions
- delegated authority
- prompt/context reference where retention is permitted
- decision output
- confidence / uncertainty indicators
- human review status
- tool invocation records
- execution evidence

The database must never infer authority solely from model or agent capability.

### 18. Feedback & Learning Data

RAW OS should persist feedback loops needed for adaptation:

```text
OUTCOME → FEEDBACK → REVIEW → CHANGE PROPOSAL → APPROVAL → NEW VERSION
```

Relevant objects:

- feedback
- observation
- issue
- change proposal
- review
- approved change
- implementation version
- validation result

### 19. Backup, Recovery & Resilience

The implementation should define:

- recovery point objective (RPO)
- recovery time objective (RTO)
- backup frequency
- backup retention
- restore testing
- disaster recovery location/strategy
- evidence preservation requirements
- reconciliation procedure after recovery

These are implementation/configuration requirements, not fixed RAW OS values.

### 20. Retention & Deletion

Retention must be driven by purpose, risk, legal requirements and governance policy.

```text
CREATE → USE → RETAIN → REVIEW → ARCHIVE / DELETE
```

Deletion must not destroy evidence that is legally or governance-required to remain traceable.

### 21. Performance & Scaling

The database must distinguish between:

- transactional workloads
- event workloads
- analytical workloads
- evidence/audit workloads
- configuration workloads

Scaling strategy may use separate stores, read replicas, queues or analytical systems while preserving canonical identifiers and traceability.

### 22. Polyglot Storage Principle

RAW OS does not mandate one database technology.

A production implementation may use:

- relational database for transactional integrity
- event store for event history
- object storage for large evidence
- search index for retrieval
- analytical warehouse/lakehouse for analytics

The canonical RAW OS data semantics must remain stable across these implementations.

### 23. Database-to-API Mapping

The database should support the API resources without coupling API naming blindly to physical tables.

```text
API RESOURCE
   ↓
DOMAIN SERVICE
   ↓
CANONICAL OBJECT MODEL
   ↓
DATA ACCESS LAYER
   ↓
DATABASE / STORAGE
```

A single API resource may span several physical tables/stores, and one logical object may require several persistence structures.

### 24. Migration & Schema Evolution

Schema changes require:

- migration identifier
- change owner
- rationale
- impact assessment
- backward compatibility assessment
- migration test
- rollback/recovery plan
- version update
- evidence

Production migration must not silently alter the interpretation of historical governance evidence.

### 25. Database Evaluation Criteria

A database implementation is RAW OS compatible when it can demonstrate:

- ontology coverage
- referential integrity
- authority traceability
- decision traceability
- risk/control traceability
- state/event reconstruction
- auditability
- versioning
- integration correlation
- access governance
- recovery capability
- migration discipline

### 26. Recommended Initial Logical Schema

```text
identity
 ├── actors
 ├── roles
 ├── capabilities
 └── authorities

governance
 ├── systems
 ├── purposes
 ├── boundaries
 ├── policies
 ├── rules
 └── controls

operations
 ├── inputs
 ├── decisions
 ├── approvals
 ├── actions
 ├── events
 ├── states
 └── outcomes

risk
 ├── risks
 └── risk_assessments

evidence
 ├── evidence
 └── audit_records

integration
 ├── external_systems
 ├── adapters
 ├── mappings
 └── sync_states

adaptation
 ├── feedback
 ├── reviews
 ├── change_proposals
 └── versions
```

### 27. Boundary of This Specification

This document does not select:

- PostgreSQL, MySQL, MongoDB or another specific engine
- cloud vendor
- hosting model
- exact physical schema
- exact partitioning strategy
- specific ORM
- final data retention periods

Those decisions belong to the implementation design and should be justified against RAW OS requirements.

### 28. Dependency & Traceability

Database Architecture depends on:

- RAW OS v0.1 — Core Logic System Foundation
- RAW OS v0.2 — System Ontology
- RAW OS v0.3 — Decision & Control Logic
- RAW OS v0.4 — Operating Architecture
- RAW OS v0.5 — Governance Framework
- RAW OS v0.6 — Integration Framework
- RAW OS v0.7 — Evaluation Framework
- RAW OS v0.8 — Reference Framework
- RAW OS v1.0 — API Specification
- RAW OS v1.0 — Algorithm Architecture

Traceability chain:

```text
RAW OS OBJECT
 → LOGICAL ENTITY
 → RELATIONSHIP
 → PERSISTENCE RULE
 → API RESOURCE
 → ALGORITHM INPUT / OUTPUT
 → EVIDENCE
```

### 29. Next Component

**RAW OS v1.0 — 4. Event & State Architecture**

This component should define the formal event model, state machine, transition rules, event sourcing boundaries, correlation/causation logic, replay/reconciliation and state integrity.

### 30. Status

- Version: RAW OS v1.0
- Component: 3. Database Architecture
- Status: System Design Specification — Foundational Technical Draft
- Architecture Principle: Technology-agnostic, ontology-first, governance-preserving, traceable and auditable

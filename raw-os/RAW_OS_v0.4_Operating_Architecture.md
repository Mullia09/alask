# RAW OS v0.4 — Operating Architecture

**Status:** Foundational Draft  
**Depends on:** RAW OS v0.1 Core Logic System Foundation + RAW OS v0.2 System Ontology + RAW OS v0.3 Decision & Control Logic  
**Design principle:** Domain-neutral, modular, composable, auditable, risk-aware and adaptive.

## 1. Purpose

RAW OS v0.4 translates the core logic, ontology and decision/control logic into an operating architecture. It defines the major layers, engines, registries, interfaces and execution loops required for RAW OS to operate as a governance layer across different domains.

## 2. Architecture Principle

RAW OS is not intended to replace the underlying domain system. It operates as a governance and decision-control layer that can be mapped onto an existing system.

```text
DOMAIN SYSTEM
      |
      v
RAW OS INTERFACE / ADAPTER
      |
      v
+-------------------------------+
|        RAW OS CORE             |
| Purpose / Scope / Authority    |
| Rules / Risk / Controls        |
| Decision / Evidence / Feedback |
+-------------------------------+
      |
      v
DOMAIN EXECUTION SYSTEM
      |
      v
REAL-WORLD OUTCOME
      |
      +------> EVIDENCE / FEEDBACK ------+
                                      |
                                      v
                                   ADAPTATION
```

## 3. RAW OS Architecture Layers

### 3.1 Layer 0 — Environment

The real-world environment in which the system operates.

Inputs include events, people, resources, constraints, signals and external changes.

### 3.2 Layer 1 — Foundation

The infrastructure required by all higher layers:

- Data
- People
- Technology
- Capability
- Change / Adaptation

### 3.3 Layer 2 — System Context

Defines:

- Purpose
- Scope
- Boundary
- Stakeholders
- Actors
- Roles
- Dependencies

### 3.4 Layer 3 — Governance Registry

Stores the normative structure of the system:

- Principles
- Policies
- Rules
- Authorities
- Permissions
- Constraints
- Thresholds

### 3.5 Layer 4 — Intelligence & Assessment

Converts raw inputs into decision-ready context:

- Input validation
- Context assembly
- Classification
- Risk assessment
- Confidence assessment
- Impact assessment
- Recommendation generation

### 3.6 Layer 5 — Decision Engine

Applies rules, authority and assessment to determine the permitted decision path.

```text
INPUT
  -> CONTEXT
  -> ASSESSMENT
  -> RULE MATCH
  -> AUTHORITY CHECK
  -> RISK GATE
  -> DECISION
```

Decision classes:

- Auto
- Assisted
- Approval Required
- Escalation Required
- Prohibited

### 3.7 Layer 6 — Control Engine

Applies controls before, during and after execution.

```text
PREVENT -> DETECT -> INTERVENE -> CORRECT -> LEARN
```

Control points:

- Input Control
- Process Control
- Decision Control
- Action Control
- Output Control

### 3.8 Layer 7 — Execution / Orchestration

Coordinates authorised actions across humans, processes, AI agents and external systems.

The orchestration layer must respect:

- Authority
- Sequence
- Dependencies
- Constraints
- Time limits
- Escalation conditions

### 3.9 Layer 8 — Evidence & Audit

Captures the trace of significant system activity.

```text
EVENT -> RECORD -> TRACE -> EVIDENCE -> AUDIT
```

Minimum trace should allow reconstruction of:

- What happened
- Who/what acted
- When it happened
- Which input was used
- Which rule applied
- Which authority was used
- What decision was made
- What action occurred
- What outcome resulted

### 3.10 Layer 9 — Feedback & Adaptation

Converts outcomes and evidence into system learning.

```text
OUTCOME
  -> FEEDBACK
  -> REVIEW
  -> LEARNING
  -> RULE / CONTROL / CAPABILITY UPDATE
  -> NEW OPERATING STATE
```

## 4. Core Engines

RAW OS v0.4 is organised around interoperable engines rather than one monolithic process.

### 4.1 Context Engine

Builds the current system context from available inputs, actors, state and environment.

### 4.2 Rule Engine

Matches conditions to applicable rules and constraints.

### 4.3 Authority Engine

Determines whether an actor is authorised to perform a decision or action in the current context.

### 4.4 Risk Engine

Classifies risk, determines required controls and identifies escalation conditions.

### 4.5 Decision Engine

Selects the valid decision path based on context, rules, authority, risk and evidence.

### 4.6 Control Engine

Determines which controls must be applied and whether execution can proceed.

### 4.7 Orchestration Engine

Coordinates the execution of approved actions across internal and external actors/systems.

### 4.8 Evidence Engine

Creates and maintains traceable records for significant events, decisions, actions and outcomes.

### 4.9 Feedback Engine

Collects operational, performance, risk, audit and stakeholder feedback.

### 4.10 Adaptation Engine

Determines whether feedback requires changes to rules, thresholds, controls, capabilities or system configuration.

## 5. Core Registries

RAW OS requires structured registries so that governance objects are explicit rather than hidden inside undocumented processes.

### 5.1 System Registry

Contains system identity, purpose, scope, boundary and status.

### 5.2 Actor Registry

Contains actors, roles, capabilities and status.

### 5.3 Authority Registry

Contains authority scopes, levels, conditions and delegation rules.

### 5.4 Rule Registry

Contains active rules, conditions, priorities, effective dates and owners.

### 5.5 Risk Registry

Contains risks, severity, likelihood, controls, residual risk and owners.

### 5.6 Control Registry

Contains controls, control type, trigger, owner, evidence requirement and failure response.

### 5.7 Decision Registry

Contains decision classes, decision rules, approval requirements and escalation paths.

### 5.8 Evidence Registry

Contains evidence references, timestamps, provenance and linkage to system events.

### 5.9 Change Registry

Records material changes to rules, authorities, controls, capabilities and system configuration.

## 6. Standard Interface

A domain system connects to RAW OS through a common conceptual interface:

```text
PURPOSE
SCOPE
ACTOR
AUTHORITY
RULE
INPUT
STATE
DECISION
RISK
CONTROL
ACTION
EVENT
OUTCOME
EVIDENCE
FEEDBACK
```

The adapter maps the domain's native objects to these RAW OS primitives.

## 7. Operating Cycle

```text
1. OBSERVE
2. INGEST
3. CONTEXTUALISE
4. ASSESS
5. DECIDE
6. AUTHORISE
7. CONTROL
8. EXECUTE
9. MEASURE
10. RECORD
11. REVIEW
12. ADAPT
13. RECONFIGURE
14. RETURN TO OBSERVE
```

This creates a closed-loop governance operating system rather than a one-time approval workflow.

## 8. State Management

Every significant process should have an explicit state.

```text
PROPOSED
   -> ASSESSED
   -> AUTHORISED
   -> CONTROLLED
   -> EXECUTING
   -> COMPLETED
```

Alternative states:

- REJECTED
- ESCALATED
- ON HOLD
- FAILED
- OVERRIDDEN
- CANCELLED

Invalid state transitions must be rejected or escalated.

## 9. Escalation Architecture

Escalation is a controlled route to a higher authority or a human decision point.

```text
TRIGGER
  -> HOLD / CONTAIN
  -> PACKAGE CONTEXT
  -> IDENTIFY AUTHORITY
  -> REVIEW
  -> DECIDE
  -> RESUME / REJECT / STOP
```

Typical triggers:

- Authority exceeded
- Risk threshold exceeded
- Confidence below threshold
- Rule conflict
- Boundary breach
- Unknown condition
- Control failure
- Exceptional impact

## 10. Control Plane vs Execution Plane

RAW OS should conceptually separate governance from execution.

**Control Plane:**

- Purpose
- Rules
- Authority
- Risk
- Controls
- Thresholds
- Decision policy
- Audit policy

**Execution Plane:**

- Tasks
- Workflows
- Human actions
- AI agent actions
- Transactions
- External system calls

The control plane determines what is permissible. The execution plane performs the authorised work.

## 11. Human Governance Layer

Human oversight is dynamic rather than binary.

- Human-in-the-Loop: approval required before action.
- Human-on-the-Loop: system operates within boundary while human monitors and may intervene.
- Human-out-of-the-Loop: tightly bounded automation with predefined controls.

Human involvement should increase with risk, impact, uncertainty and authority sensitivity.

## 12. Failure Architecture

RAW OS treats failure as a first-class system state.

```text
FAILURE
  -> DETECT
  -> CONTAIN
  -> CLASSIFY
  -> ESCALATE
  -> RECOVER
  -> RECORD
  -> LEARN
```

Control failure must not silently become normal execution.

## 13. Governance Change Management

Any material change to rules, authority, controls or capability should follow:

```text
CHANGE REQUEST
  -> IMPACT ASSESSMENT
  -> RISK REVIEW
  -> AUTHORITY REVIEW
  -> APPROVAL
  -> IMPLEMENTATION
  -> VALIDATION
  -> EVIDENCE
  -> VERSION UPDATE
```

## 14. Versioning Principle

RAW OS governance objects should be versioned.

Examples:

- Rule v1.2
- Control v2.0
- Authority Policy v1.4
- System Configuration v3.1

Historical evidence must remain interpretable against the rules and controls that were active at the time of the event.

## 15. Domain Adapter Model

RAW OS becomes domain-neutral through adapters.

```text
                RAW OS CORE
                    |
        +-----------+-----------+
        |           |           |
     AI ADAPTER  ORG ADAPTER  COMMUNITY ADAPTER
        |           |           |
     AI SYSTEM   ORG SYSTEM  COMMUNITY SYSTEM
```

Potential adapters:

- AI Agent Governance
- Community Programme Governance
- Business Operations
- Public Service
- Political Operations
- Education Systems
- Project Management

The adapter changes the vocabulary and configuration; the core governance logic remains stable.

## 16. Minimum Operating Architecture

A RAW OS-compatible implementation should contain, at minimum:

1. System Context
2. Actor & Authority Model
3. Rule Registry
4. Decision Logic
5. Risk Gate
6. Control Mechanism
7. Execution Path
8. Evidence / Audit Trail
9. Feedback Loop
10. Adaptation Mechanism

## 17. Architectural Axiom

> **Governance must sit between capability and consequential action.**

Capability answers what a system can do. Governance determines what it may do, under which conditions, with which controls, and with what evidence.

## 18. RAW OS v0.4 Master Architecture

```text
                         ENVIRONMENT
                              |
                              v
                        [OBSERVATION]
                              |
                              v
                        [CONTEXT ENGINE]
                              |
               +--------------+--------------+
               |                             |
               v                             v
          [RULE ENGINE]                 [RISK ENGINE]
               |                             |
               +--------------+--------------+
                              v
                       [DECISION ENGINE]
                              |
                       [AUTHORITY ENGINE]
                              |
                       [CONTROL ENGINE]
                              |
                       [ORCHESTRATOR]
                              |
                              v
                         [EXECUTION]
                              |
                              v
                           OUTCOME
                              |
                     [EVIDENCE ENGINE]
                              |
                     [FEEDBACK ENGINE]
                              |
                    [ADAPTATION ENGINE]
                              |
                              +------> RULE / CONTROL / CAPABILITY
```

## 19. Boundary of v0.4

v0.4 does not yet define:

- Concrete programming language
- Database schema
- API endpoints
- UI/UX
- Authentication implementation
- Specific AI models
- Domain-specific legal/policy rules
- Production deployment architecture

These belong to later implementation layers.

## 20. Next Layer — RAW OS v0.5

Recommended next step: **Implementation Specification**.

v0.5 should convert the architecture into implementable specifications:

- Canonical data objects
- Machine-readable schemas
- Rule syntax
- Decision schema
- Authority schema
- Risk/control schema
- Event/evidence schema
- API/interface contract
- Versioning model
- Test cases
- Reference implementation

## 21. Status

**RAW OS v0.4 — Operating Architecture**  
Status: Foundational Architecture Draft  
Layer sequence: v0.1 Core Logic → v0.2 Ontology → v0.3 Decision & Control → v0.4 Operating Architecture

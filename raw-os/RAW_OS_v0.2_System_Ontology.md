# RAW OS v0.2 — System Ontology

**Status:** Foundational Draft  
**Depends on:** RAW OS v0.1 — Core Logic System Foundation  
**Purpose:** Define the objects, states, relationships and logic of the RAW OS system.

---

## 1. Purpose

RAW OS v0.2 defines the ontology that sits between the core logic and later implementation. It establishes the canonical objects, their attributes, relationships and state-transition logic so different domains can be mapped to a common system language.

The ontology is domain-neutral. It does not prescribe a specific programming language, database, API, AI model or organisational structure.

## 2. Ontology Principles

### 2.1 Object Before Module
Identify the fundamental objects of a system before creating modules or applications.

### 2.2 Relationship Matters
The meaning of an object is determined not only by its attributes but also by its relationships with other objects.

### 2.3 State Changes
A system is a network of state changes, not merely a collection of static objects.

### 2.4 Authority Is Explicit
Authority must be explicit and cannot be inferred solely from technical capability.

### 2.5 Evidence Is Native
Significant events, decisions and actions must be capable of producing traceable evidence.

## 3. Core System Objects

### 3.1 SYSTEM
A bounded environment with a defined purpose, actors, resources, rules and outcomes.

Core attributes:
- System ID
- Purpose
- Boundary
- State
- Rules
- Actors
- Resources
- Interfaces

### 3.2 ACTOR
An entity capable of receiving input, making a decision, performing an action, or influencing a process.

Possible actor types:
- Human
- AI / Agent
- Organisation
- Process
- External System

### 3.3 ROLE
A function or position assigned to an actor within a defined context.

**Actor → Role → Responsibility**

### 3.4 CAPABILITY
What an actor or system is technically or operationally able to do.

**Capability answers: CAN DO WHAT?**

### 3.5 AUTHORITY
The legitimate permission to use a capability within defined limits.

**Authority = Scope + Level + Condition**

### 3.6 PURPOSE
The reason a system, process or action exists.

**Purpose → Objective → Desired Outcome**

### 3.7 BOUNDARY
The limits of the system, process or actor's operating domain.

Includes:
- In Scope
- Out of Scope
- Escalation Boundary
- External Dependency

### 3.8 RULE
A logical constraint, requirement or permission governing behaviour.

**Rule = Condition + Requirement / Permission + Constraint**

### 3.9 INPUT
Information, request, signal, resource or trigger entering a process or system.

### 3.10 DECISION
A selection or determination made from input, context, rules, risk, evidence and authority.

**Input → Assessment → Decision**

### 3.11 ACTION
An operation performed by an actor or process after a decision or trigger.

### 3.12 EVENT
A significant occurrence or change that happens within or to the system.

### 3.13 STATE
The current condition of a system or object at a point in time.

**State(t) → Event → State(t+1)**

### 3.14 RISK
The uncertainty or possibility that an event or action produces an unwanted impact.

**Risk = Uncertainty / Threat + Exposure + Impact**

### 3.15 CONTROL
A mechanism that prevents, detects, constrains, corrects or stops unwanted behaviour or outcomes.

### 3.16 EVIDENCE
A record or data artifact capable of demonstrating that an event, decision, action or outcome occurred.

### 3.17 OUTCOME
The effect or result produced by an action.

### 3.18 FEEDBACK
Information generated from outcomes, operations or the environment and used for review and improvement.

## 4. Canonical Relationship Chain

The basic relationship chain is:

**PURPOSE → BOUNDARY → ACTOR → ROLE → CAPABILITY → AUTHORITY → RULE → INPUT → DECISION → CONTROL → ACTION → EVENT → STATE → OUTCOME → EVIDENCE → FEEDBACK → ADAPTATION**

Not every implementation needs every object at every step, but significant systems must be capable of mapping their relevant elements to the canonical ontology.

## 5. Authority Model

RAW OS distinguishes four related but non-identical concepts:

**Capability → Authority → Permission → Action**

A capability indicates what an actor can technically perform. Authority determines whether the actor may perform it in the current context.

Therefore:

> Capability ≠ Authority

## 6. Decision Object

A significant decision should be representable using at least:

- Decision ID
- Actor / Decision Maker
- Input
- Context
- Applicable Rule
- Authority
- Risk Assessment
- Decision
- Rationale
- Approval / Escalation
- Timestamp
- Expected Outcome

## 7. Action Object

A significant action should be representable using:

- Action ID
- Actor
- Authorising Decision
- Input / Trigger
- Constraint
- Execution Time
- Result
- Evidence

## 8. State Machine Logic

RAW OS treats the system as a state machine. An object is in a state and can move to another state only when a valid event and transition condition are satisfied.

**STATE A → EVENT → CONTROL CHECK → AUTHORISED TRANSITION → STATE B**

Invalid transitions should be rejected. Uncertain transitions should be escalated. High-risk transitions may require additional human or higher-authority review.

## 9. Risk-Control Relationship

**RISK → CONTROL → RESIDUAL RISK → ACCEPT / MITIGATE / ESCALATE / STOP**

Control types may include:
- Preventive
- Detective
- Corrective
- Compensating
- Escalation

## 10. Evidence Chain

**INPUT → DECISION → AUTHORISATION → ACTION → EVENT → OUTCOME → RECORD**

Evidence should be sufficient to reconstruct significant system behaviour without relying entirely on human memory.

## 11. Feedback & Adaptation

**OUTCOME → FEEDBACK → REVIEW → LEARNING → RULE / CONTROL / CAPABILITY UPDATE → NEW STATE**

Adaptation is a system property and must remain governed rather than becoming uncontrolled drift.

## 12. Minimum Viable System Definition

A RAW OS-compatible system should be able to identify, at minimum:

- Purpose
- Boundary
- Actor
- Capability
- Authority
- Rule
- Input
- Decision
- Risk
- Control
- Action
- Event
- State
- Outcome
- Evidence
- Feedback

## 13. Compatibility Principle

Different systems may use different terminology, organisational structures and technologies. They remain compatible when their relevant semantics can be mapped to the RAW OS canonical objects and relationships.

**Core logic same → Domain configuration different.**

## 14. Boundary of v0.2

v0.2 does not prescribe:

- Database technology
- API implementation
- User interface
- AI model
- Cloud infrastructure
- Domain-specific SOP

Its purpose is to establish the ontology and relationships that later implementations must respect.

## 15. Next Layer — RAW OS v0.3

RAW OS v0.3 extends the ontology into **Decision & Control Logic**, defining decision classes, authority checks, risk gates, thresholds, escalation, exceptions, human oversight and control-failure behaviour.

## 16. Status

**Version:** RAW OS v0.2  
**Status:** System Ontology — Foundational Draft  
**Design Principle:** Domain-neutral, composable, explicit, auditable and adaptable.

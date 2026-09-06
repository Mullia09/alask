# RAW OS v0.8 — Reference Framework

## The Domain-Neutral Reference Architecture for RAW OS

**Status:** Foundational Reference Draft  
**Depends on:** RAW OS v0.1–v0.7  
**Purpose:** Consolidate the RAW OS framework before System Design / v1.0 implementation.

---

## 1. Executive Definition

RAW OS is a domain-neutral governance and operating logic designed to help a system define purpose, understand its actors, regulate authority, make and control decisions, execute actions, preserve evidence, evaluate outcomes, and adapt to change.

RAW OS is not itself an AI model, database, API, user interface, SOP manual, or single organisational structure. Those are implementation choices that should realise the RAW OS logic without redefining its constitutional constraints.

**Core proposition:**

> Technology implements RAW OS; technology does not define RAW OS.

---

## 2. Framework Lineage

```text
v0.1  Core Logic System Foundation
   ↓
v0.2  System Ontology
   ↓
v0.3  Decision & Control Logic
   ↓
v0.4  Operating Architecture
   ↓
v0.5  Governance Framework
   ↓
v0.6  Integration Framework
   ↓
v0.7  Evaluation & Validation Framework
   ↓
v0.8  Reference Framework
   ↓
v1.0  System Design Specification
```

v0.8 is the consolidation layer. It does not replace v0.1–v0.7; it establishes their relationships and defines the reference state from which implementation specifications can be produced.

---

## 3. RAW OS Core Model

The complete RAW OS operating cycle is:

**PURPOSE → SCOPE → ACTOR → AUTHORITY → RULE → INPUT → ASSESSMENT → DECISION → RISK → CONTROL → ACTION → EVENT → STATE → OUTCOME → EVIDENCE → FEEDBACK → ADAPTATION**

The cycle is recursive. Adaptation may change rules, thresholds, controls, capabilities, scope, or—where formally justified—purpose.

---

## 4. Core Ontology

The reference ontology consists of the following primary objects:

1. **System** — bounded environment containing purpose, actors, resources, rules, states and outcomes.
2. **Purpose** — reason for the system's existence.
3. **Boundary / Scope** — what is inside, outside, or conditionally inside system authority.
4. **Actor** — entity capable of receiving information, making decisions, executing actions, or performing governance functions.
5. **Role** — contextual function assigned to an actor.
6. **Capability** — what an actor or system can technically or operationally do.
7. **Authority** — what an actor is legitimately permitted to do.
8. **Rule** — prescribed or permitted behaviour under defined conditions.
9. **Input** — information, request, signal, resource or trigger entering a process.
10. **Assessment** — interpretation and evaluation of context, evidence, risk and constraints.
11. **Decision** — selection or determination of a course of action.
12. **Action** — execution of an authorised operation.
13. **Event** — significant occurrence or change within or affecting the system.
14. **State** — condition of an object/system at a point in time.
15. **Risk** — uncertainty or exposure that may produce undesired impact.
16. **Control** — mechanism that prevents, detects, limits, corrects or stops behaviour.
17. **Outcome** — result or effect produced by action.
18. **Evidence** — record sufficient to establish what happened and support accountability/audit.
19. **Feedback** — information used to assess system performance and change the system.
20. **Adaptation** — controlled change resulting from learning, review or environmental change.

---

## 5. Constitutional Axioms

These are the highest-level RAW OS invariants.

### A1 — Purpose
No system without a defined purpose.

### A2 — Boundary
No authority without a defined boundary.

### A3 — Authority
No significant action without defined authority.

### A4 — Accountability
No significant decision without attributable responsibility.

### A5 — Evidence
No critical process without observable evidence.

### A6 — Proportionality
Governance and control intensity should be proportionate to risk, impact and uncertainty.

### A7 — Separation
Where risk requires it, decision, execution, monitoring and assurance functions should not be concentrated in one actor.

### A8 — Adaptation
No governance arrangement remains permanently valid without feedback and review.

### A9 — Traceability
Significant actions and decisions must be reconstructable from their evidence chain.

### A10 — Revocability
Delegated authority and high-impact permissions must be capable of being limited, suspended or revoked.

---

## 6. Governance Constitution

RAW OS governance follows the hierarchy:

**PRINCIPLES → POLICIES → RULES → PROCEDURES → CONTROLS → OPERATIONS**

Lower-level implementation must not contradict higher-level constraints.

Governance defines:

- mandate
- authority
- accountability
- decision rights
- risk appetite
- control requirements
- oversight
- challenge/review
- exception handling
- policy lifecycle
- change governance

---

## 7. Authority Model

RAW OS explicitly separates:

**MANDATE ≠ AUTHORITY ≠ CAPABILITY ≠ RESPONSIBILITY**

Reference authority model:

**Authority = Scope + Level + Condition**

Authority should also support:

- delegation
- limits
- expiry
- revocation
- escalation
- override conditions
- auditability

Capability alone never grants authority.

---

## 8. Decision & Control Architecture

The reference decision pipeline is:

**INPUT → CONTEXT → ASSESSMENT → DECISION → AUTHORITY CHECK → RISK CHECK → CONTROL CHECK → ACTION → OUTCOME**

Decision classes:

1. **AUTO** — fully automated within defined boundaries.
2. **ASSISTED** — recommendation generated, authorised actor decides.
3. **APPROVAL REQUIRED** — action requires prior approval.
4. **ESCALATION REQUIRED** — current level lacks authority, confidence or risk tolerance.
5. **PROHIBITED** — action is outside permissible boundaries.

---

## 9. Risk-Control Architecture

Reference risk flow:

**IDENTIFY → ASSESS → TREAT → RESIDUAL RISK → ACCEPT / MITIGATE / ESCALATE / STOP**

Controls may be:

- preventive
- detective
- corrective
- compensating
- escalation
- containment

Control points may operate at input, process, decision, action and output layers.

---

## 10. State & Event Architecture

RAW OS treats systems as dynamic state machines.

**STATE(t) → EVENT → VALIDATION → AUTHORISED TRANSITION → STATE(t+1)**

Invalid or ambiguous transitions should be rejected, held or escalated depending on context.

Events should preserve enough metadata to support correlation, traceability and reconciliation across systems.

---

## 11. Evidence Architecture

Reference evidence chain:

**REQUEST → ASSESSMENT → DECISION → AUTHORISATION → ACTION → EVENT → OUTCOME → RECORD**

Critical evidence should permit reconstruction of:

- who/what acted
- when
- under which role and authority
- using which rule/version
- using which input/evidence
- what action occurred
- what outcome resulted
- what review followed

---

## 12. Integration Architecture

RAW OS is designed to operate as:

- governance overlay
- decision layer
- control layer
- orchestration layer
- intelligence layer
- full operating layer

Reference integration pattern:

**EXTERNAL SYSTEM → ADAPTER → CANONICAL RAW OBJECTS → GOVERNANCE / DECISION / CONTROL → EXTERNAL ACTION → EVENT → EVIDENCE**

The adapter protects the RAW OS core from external schema differences.

---

## 13. Canonical Integration Contract

An external system should be mappable to the following canonical fields:

**PURPOSE | SCOPE | ACTOR | ROLE | CAPABILITY | AUTHORITY | RULE | INPUT | DECISION | ACTION | EVENT | STATE | RISK | CONTROL | OUTCOME | EVIDENCE | FEEDBACK**

Identity is separate from authority.

Authority must not be assumed to propagate across a system boundary without verification and explicit mapping.

---

## 14. Oversight Architecture

RAW OS supports three broad oversight layers:

1. **Operational Oversight** — day-to-day monitoring and execution control.
2. **Governance Oversight** — authority, risk, policy and accountability review.
3. **Independent Assurance** — audit, assurance or equivalent independent examination.

For high-impact systems, independent or functionally independent review should be considered where appropriate.

---

## 15. Exception & Escalation Architecture

Reference exception path:

**DETECT → CLASSIFY → JUSTIFY → RISK REVIEW → AUTHORITY REVIEW → APPROVE / REJECT → EXECUTE → RECORD → POST-REVIEW**

Reference escalation path:

**TRIGGER → HOLD / CONTAIN → PACKAGE CONTEXT → IDENTIFY HIGHER AUTHORITY → REVIEW → DECIDE → RESUME / REJECT**

Repeated exceptions should be treated as potential signals of weak rules, wrong thresholds or changing conditions.

---

## 16. Change & Adaptation Architecture

Reference change cycle:

**CHANGE SIGNAL → IMPACT ASSESSMENT → REVIEW → DECISION → VERSION UPDATE → IMPLEMENT → MONITOR → REASSESS**

Change signals may arise from:

- audit
- incidents
- risk
- performance
- stakeholder feedback
- technology changes
- regulatory changes
- environmental changes

Every material change should preserve version lineage.

---

## 17. Evaluation Architecture

RAW OS validation must evaluate both the framework and implementations.

Reference validation layers:

**CONFORMANCE → FUNCTIONALITY → BOUNDARY → AUTHORITY → RISK → CONTROL → FAILURE → SECURITY → HUMAN OVERSIGHT → OUTCOME → CROSS-DOMAIN GENERALISATION**

The core universality test is:

> Can the same RAW OS primitives and invariants govern materially different domains without changing the core semantics?

A domain adaptation that repeatedly changes core invariants indicates that the framework is not yet sufficiently domain-neutral.

---

## 18. Maturity Model

### Level 0 — Undefined
Purpose, authority, rules and evidence are unclear.

### Level 1 — Defined
Core objects and rules exist.

### Level 2 — Controlled
Authority, risk and controls are operational.

### Level 3 — Auditable
Decisions, actions and evidence are traceable.

### Level 4 — Adaptive
Feedback systematically updates rules, controls and capabilities.

### Level 5 — Composable
The system can integrate with multiple domains while preserving RAW OS invariants.

Maturity level is an assessment result, not an inherent property of an implementation.

---

## 19. Mandatory vs Configurable

### Mandatory Core
These should remain invariant across implementations:

- purpose declaration
- boundary definition
- actor identification
- authority distinction
- significant decision attribution
- risk/control logic appropriate to impact
- evidence traceability
- escalation for invalid/high-risk conditions
- change/version traceability
- evaluation mechanism

### Configurable Layer
These may vary by domain:

- actor names
- governance bodies
- thresholds
- policies
- workflows
- risk appetite
- data fields
- UI
- API technology
- database technology
- AI model
- SOP detail
- metrics

This distinction is central to RAW OS universality.

---

## 20. Reference Architecture

```text
                   RAW OS REFERENCE FRAMEWORK
                              │
                ┌─────────────┴─────────────┐
                │      CONSTITUTION         │
                │ Principles / Invariants  │
                └─────────────┬─────────────┘
                              │
                    GOVERNANCE LAYER
                              │
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
          ONTOLOGY        AUTHORITY         POLICY
              │               │               │
              └───────────────┼───────────────┘
                              ↓
                  DECISION & CONTROL
                              │
                    RISK / THRESHOLD
                              │
                        ORCHESTRATION
                              │
                  ┌───────────┼───────────┐
                  ↓           ↓           ↓
                ACTOR       DATA      EXTERNAL SYSTEM
                  │           │           │
                  └───────────┼───────────┘
                              ↓
                         EXECUTION
                              ↓
                        EVENT / STATE
                              ↓
                         OUTCOME
                              ↓
                      EVIDENCE / AUDIT
                              ↓
                         FEEDBACK
                              ↓
                       ADAPTATION
                              ↺
```

---

## 21. Technology Neutrality

RAW OS v0.8 intentionally does not prescribe:

- programming language
- API protocol
- database engine
- cloud platform
- AI model vendor
- front-end framework
- authentication product
- deployment environment

Those choices belong to System Design at v1.0 and later.

The implementation must be evaluated against RAW OS requirements, not the other way around.

---

## 22. Reference Implementation Mapping

At v1.0, the core can be mapped into implementation components such as:

**RAW OS OBJECTS → DATA MODEL**

**RULES / AUTHORITY → POLICY & DECISION ENGINE**

**EVENTS / STATE → EVENT & STATE STORE**

**EVIDENCE → AUDIT / EVIDENCE STORE**

**INTEGRATION CONTRACT → API / ADAPTER LAYER**

**OVERSIGHT → ADMIN / GOVERNANCE UI**

**AI ACTOR → MODEL / AGENT LAYER**

**OPERATING LOGIC → SOP / WORKFLOW LAYER**

This is a mapping hypothesis for v1.0, not a technology commitment.

---

## 23. Framework Freeze Gate

Before moving from v0.x to v1.0, RAW OS should pass a framework freeze gate:

1. Core terminology is stable.
2. Core ontology has no unresolved contradictions.
3. Constitutional axioms are explicit.
4. Mandatory vs configurable elements are separated.
5. Authority and accountability models are coherent.
6. Decision and control logic is internally consistent.
7. Integration model is domain-neutral.
8. Evaluation model can test implementations.
9. At least several materially different domains can be mapped without changing core semantics.
10. Known limitations and unresolved assumptions are documented.

Only after this gate should implementation specifications become authoritative.

---

## 24. RAW OS Design Laws

The following laws summarise the reference framework:

**Law 1 — Purpose precedes operation.**

**Law 2 — Boundary precedes authority.**

**Law 3 — Capability does not imply authority.**

**Law 4 — Significant action requires attributable authority.**

**Law 5 — Risk should influence control intensity.**

**Law 6 — Critical decisions require evidence.**

**Law 7 — Exceptions require governance, not bypass.**

**Law 8 — System boundaries require explicit trust and authority mapping.**

**Law 9 — Governance must be measurable.**

**Law 10 — Governance must be able to learn and adapt.**

**Law 11 — Technology implements the framework; it does not redefine it.**

**Law 12 — Universality must be demonstrated by validation, not assumed by design.**

---

## 25. What RAW OS Is Not

RAW OS is not:

- a single AI product
- a generic chatbot framework
- an ERP replacement
- a database schema
- an API specification
- a workflow tool
- a political ideology
- an organisational chart
- a fixed SOP library
- a claim that one governance configuration fits every domain

It is a **reference logic and governance architecture** from which domain-specific systems can be designed.

---

## 26. Next Phase — RAW OS v1.0

The next phase is **System Design Specification**.

v1.0 should translate the frozen reference framework into explicit technical and operational specifications:

- API specification
- database/data model
- identity and access model
- UI/UX architecture
- AI/agent architecture
- security architecture
- event architecture
- audit/evidence architecture
- integration contracts
- SOP architecture
- deployment architecture
- test architecture

These components must trace back to the RAW OS reference requirements.

---

## 27. Traceability Requirement

Every v1.0 implementation requirement should be traceable to one or more RAW OS principles, ontology objects, governance rules, decision/control requirements, integration requirements or evaluation criteria.

Reference traceability chain:

**RAW OS INVARIANT → REQUIREMENT → DESIGN → IMPLEMENTATION → TEST → EVIDENCE**

This creates a controlled relationship between the abstract framework and the physical system.

---

## 28. Final Reference Statement

RAW OS v0.8 establishes the reference state of the framework before implementation.

The objective is not to produce one rigid system, but a stable governance logic capable of being instantiated across different systems while preserving its constitutional principles.

**ONE CORE LOGIC → MANY SYSTEM CONFIGURATIONS → MANY IMPLEMENTATIONS**

The framework is considered mature enough for System Design only when its invariants, ontology, governance, decision/control, integration and evaluation mechanisms are coherent and testable.

---

## 29. Status

**Version:** RAW OS v0.8  
**Title:** Reference Framework  
**Status:** Consolidated Foundational Reference Draft  
**Scope:** Domain-neutral  
**Dependencies:** RAW OS v0.1–v0.7  
**Next:** RAW OS v1.0 — System Design Specification  
**Primary principle:** Preserve the framework; vary the implementation.

# RAW OS v1.0 — System Design Specification
## 6. UI/UX Architecture

**Status:** System Design Specification  
**Layer:** Human-System Interface  
**Depends on:** RAW OS v0.1–v0.8, v1.0 API, Algorithm, Database, Event & State, AI/Agent Architecture

---

## 1. Purpose

RAW OS UI/UX Architecture defines how humans and authorised actors interact with RAW OS without allowing the interface itself to redefine governance, authority, decision logic or system truth.

The UI is an interaction layer, not the constitutional layer.

**Principle:**

`RAW OS GOVERNANCE → SYSTEM LOGIC → UI PRESENTATION → HUMAN INTERACTION`

Not:

`UI → IMPLIED AUTHORITY`

---

## 2. Core UI/UX Principles

### 2.1 Governance First

The interface must reflect governance constraints already defined by RAW OS.

### 2.2 Explainability

Significant decisions should expose relevant rationale, rule, authority, risk and evidence context according to access rights.

### 2.3 Proportionality

Interface complexity and intervention requirements should increase with decision risk and impact.

### 2.4 Role-Based Experience

Different actors see functions appropriate to their role and authority.

### 2.5 Explicit Authority

A button, screen or visual affordance must not create authority that the user does not possess.

### 2.6 Traceability

Significant user actions must remain attributable and auditable.

### 2.7 Safe Defaults

Where ambiguity exists, the interface should favour review, clarification or hold rather than unsafe execution.

### 2.8 Accessibility

Critical functions should remain usable across appropriate devices, accessibility needs and operating environments.

---

## 3. UI Architecture Layers

1. **Presentation Layer** — visual representation and interaction.
2. **Interaction Layer** — user commands, forms, navigation and confirmations.
3. **Permission Layer** — role and authority-aware presentation.
4. **Decision Context Layer** — rules, risk, evidence and state context.
5. **API Layer** — machine-readable communication with RAW OS services.
6. **Evidence Layer** — action and interaction records where required.

`USER → UI → PERMISSION CONTEXT → API → RAW OS LOGIC`

---

## 4. Actor-Centred UX

UI experiences are configured around actor roles rather than around arbitrary screens.

Possible experience classes:

- Operator
- Decision Maker
- Approver
- Risk Reviewer
- Auditor
- Administrator
- AI/Agent Supervisor
- External Stakeholder
- Public / Affected User

Each experience maps to:

`ACTOR → ROLE → CAPABILITY → AUTHORITY → AVAILABLE INTERACTION`

---

## 5. Core UI Domains

### 5.1 System Overview

Shows current system state, health, active issues, important events and governance alerts.

### 5.2 Work / Task Workspace

Shows requests, assigned actions, pending approvals and workflow status.

### 5.3 Decision Console

Provides context required for significant decisions:

- Request
- Context
- Evidence
- Applicable Rules
- Authority
- Risk
- Recommended Action
- Alternatives
- Escalation Requirement
- Decision Record

### 5.4 Risk & Control Console

Shows active risks, thresholds, control status, control failures and residual risk.

### 5.5 Event & State Viewer

Displays event chronology, current state and state transitions.

### 5.6 Evidence / Audit Console

Allows authorised users to inspect decision, action, event and evidence chains.

### 5.7 Governance Console

Provides controlled management of policies, rules, authority assignments and governance configuration.

### 5.8 Integration Console

Shows connected systems, adapter status, data/event flows, failures and reconciliation state.

### 5.9 AI / Agent Console

Shows active agents, delegated authority, tools, tasks, confidence, risk state, interventions and escalations.

---

## 6. Decision UX

The Decision Console should prevent the user from treating a recommendation as an already-authorised action.

Recommended presentation order:

`WHAT → WHY → EVIDENCE → RULE → AUTHORITY → RISK → OPTIONS → RECOMMENDATION → DECISION → CONFIRMATION`

### Decision States

- Draft
- Assessed
- Awaiting Approval
- Approved
- Rejected
- Escalated
- On Hold
- Executing
- Completed
- Failed
- Overridden
- Cancelled

---

## 7. Authority-Aware Interface

UI components should dynamically reflect authority state.

Examples:

- **Allowed** — action can proceed.
- **Approval Required** — action is available but requires approval.
- **Escalation Required** — current actor cannot decide.
- **Read Only** — actor can observe but cannot modify.
- **Prohibited** — action is unavailable.

The system should explain significant restrictions where appropriate:

`ACTION → AUTHORITY CHECK → UI STATE`

---

## 8. Risk-Aware UX

Risk should influence the interaction pattern.

### Low Risk

Normal workflow with standard confirmation.

### Medium Risk

Additional context, evidence or confirmation.

### High Risk

Enhanced review, explicit authorisation and stronger evidence requirements.

### Critical Risk

Stop, escalation or restricted pathway.

`RISK LEVEL → CONTROL INTENSITY → INTERACTION INTENSITY`

---

## 9. Human-in-the-Loop UX

Human involvement must be explicit.

### Human-in-the-Loop

UI presents decision context and requires an explicit human approval action.

### Human-on-the-Loop

UI shows active execution, allows intervention and surfaces exceptions.

### Human-out-of-the-Loop

UI focuses on monitoring, alerts, audit and exception handling.

The interface must never imply that an AI recommendation equals human approval.

---

## 10. AI Interaction Pattern

For agent-assisted workflows, recommended presentation is:

`TASK → AGENT PLAN → TOOLS → EVIDENCE → CONFIDENCE → RISK → PROPOSED ACTION → AUTHORISATION → EXECUTION`

Users should be able to distinguish:

- AI-generated content
- System-derived data
- Human decisions
- External-system information
- Recorded evidence

---

## 11. Confirmation Architecture

Confirmation strength should be proportional to impact.

### Informational

No confirmation required.

### Reversible Action

Simple confirmation.

### Material Action

Explicit confirmation with context.

### High-Impact Action

Explicit authority verification and potentially secondary approval.

### Irreversible / Critical Action

Strong confirmation, required approvals, evidence capture and escalation controls.

Avoid dark patterns, hidden defaults or ambiguous action labels.

---

## 12. Explainability Pattern

For significant system-generated recommendations, UI should present an appropriate explanation summary:

- What happened?
- What information was considered?
- Which rule was applied?
- What authority applies?
- What risk was detected?
- Why was this option recommended?
- What alternatives exist?
- What evidence supports the recommendation?

This is an explanation interface, not a requirement to expose confidential internal model reasoning.

---

## 13. State Visibility

Users should be able to distinguish at minimum:

`CURRENT STATE`

`PENDING STATE`

`FAILED STATE`

`CONFLICT STATE`

`RECONCILED STATE`

`UNKNOWN / UNVERIFIED STATE`

Unknown information should not be visually presented as confirmed fact.

---

## 14. Event Timeline UX

A significant transaction should be reconstructable through a timeline such as:

`REQUEST → ASSESSMENT → DECISION → APPROVAL → ACTION → EVENT → OUTCOME → REVIEW`

Each timeline item may expose:

- Timestamp
- Actor
- Source
- State
- Rule
- Authority
- Evidence reference
- Correlation ID

---

## 15. Notifications & Alerts

Notifications are governed signals, not merely messages.

Alert classes:

- Information
- Attention
- Warning
- Escalation
- Critical

Alerts should include context, source, required action and expiry/review state when relevant.

The UI should avoid alert overload by prioritising actionable signals.

---

## 16. Governance-Sensitive Actions

Actions affecting governance configuration should use stronger interaction controls.

Examples:

- Changing authority
- Changing policy
- Changing thresholds
- Disabling controls
- Granting permissions
- Overriding decisions
- Modifying evidence retention
- Activating or disabling agents

These actions should normally require explicit confirmation, appropriate authority and audit evidence.

---

## 17. Auditability of Human Interaction

Where material, the system should record:

- Actor identity
- Action
- Time
- Interface/context
- Object affected
- Previous state
- New state
- Authority context
- Relevant decision ID
- Evidence reference

A UI event is not automatically an audit event; retention and audit requirements are determined by RAW OS governance configuration.

---

## 18. Data Presentation Principles

UI should distinguish:

- Source data
- Derived data
- Calculated values
- Recommendations
- Decisions
- Confirmed outcomes
- Unknowns

Visual hierarchy should not make a low-confidence recommendation appear more authoritative than verified evidence.

---

## 19. Error & Failure UX

Errors should state:

`WHAT FAILED → WHY / KNOWN CAUSE → CURRENT STATE → USER ACTION → ESCALATION PATH`

For external-system failures:

`EXTERNAL FAILURE → RAW OS STATE PRESERVATION → RETRY / FALLBACK / ESCALATION`

Do not silently convert failed operations into apparent success.

---

## 20. Accessibility & Resilience

Design requirements should include, as applicable:

- Keyboard accessibility
- Screen-reader compatibility
- Clear focus states
- Sufficient text alternatives
- Responsive layouts
- Low-bandwidth considerations
- Graceful degradation
- Recovery after interruption
- Clear status indicators

Accessibility is a system requirement, not a cosmetic enhancement.

---

## 21. Multi-Channel Architecture

The same RAW OS logic may be surfaced through:

- Web
- Mobile
- Desktop
- Command line
- Embedded workflows
- External applications
- Conversational / AI interfaces

The presentation channel may change; core authority and governance semantics must not.

`ONE GOVERNANCE MODEL → MULTIPLE INTERFACES`

---

## 22. UI Configuration vs Core Logic

Configurable:

- Layout
- Labels
- Branding
- Dashboard composition
- User preferences
- Notification preferences
- Visual density

Not freely configurable at UI level:

- Core authority semantics
- Governance invariants
- Audit requirements
- Mandatory safety controls
- Core decision constraints

---

## 23. Design Tokens & Semantic States

UI design should use semantic states rather than relying on colour alone.

Examples:

- Allowed
- Pending
- Blocked
- Escalated
- Failed
- Verified
- Unverified
- Critical

Semantic state should be represented through text, iconography, structure and accessible cues.

---

## 24. Frontend Security Boundary

UI is never a security authority by itself.

A hidden button or disabled UI element is not sufficient enforcement.

Security sequence:

`UI PERMISSION → API AUTHORISATION → SERVER-SIDE CONTROL → ACTION`

The backend must independently enforce authority and controls.

---

## 25. UX Compatibility Test

A RAW OS implementation passes the UI/UX compatibility test when:

- Users can understand relevant system state.
- Material decisions expose appropriate context.
- Authority is explicit.
- AI recommendations are distinguishable from human decisions.
- Restricted actions are controlled by backend enforcement.
- Critical events are traceable.
- Errors do not masquerade as success.
- Risk affects interaction intensity.
- Governance-sensitive changes require appropriate controls.
- Accessibility requirements are addressed.

---

## 26. Reference UI Flow

`LOGIN / IDENTITY`

↓

`ROLE + AUTHORITY CONTEXT`

↓

`SYSTEM / WORKSPACE`

↓

`REQUEST / EVENT`

↓

`CONTEXT + EVIDENCE`

↓

`RULE + RISK + AUTHORITY`

↓

`DECISION / RECOMMENDATION`

↓

`APPROVAL / ESCALATION`

↓

`ACTION`

↓

`OUTCOME + EVIDENCE`

↓

`REVIEW / FEEDBACK`

---

## 27. Boundary of Component 6

This specification does not yet prescribe a specific frontend framework, design system, device, visual brand or UI technology.

Those decisions belong to implementation design and product/domain configuration, provided they remain compliant with RAW OS semantics and governance.

---

## 28. Next Component — 7. Security Architecture

The next component should formalise identity, authentication, authorisation, least privilege, trust boundaries, secrets, encryption, threat modelling, secure execution, audit security and incident response.

---

## 29. Design Principle

> **The interface may reveal, guide and request action; it must never manufacture authority.**

**Version:** RAW OS v1.0 — Component 6  
**Status:** UI/UX Architecture — System Design Specification

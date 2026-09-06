# RAW OS v1.0 — System Design Specification
## 8. SOP Architecture

**Status:** Foundational System Design Specification  
**Depends on:** RAW OS v0.1–v0.8; v1.0 components 1–7  
**Principle:** SOPs operationalise governance; they do not redefine it.

---

## 1. Purpose

RAW OS SOP Architecture defines how the framework, governance rules, decision logic, controls, security requirements and system behaviours are translated into repeatable operational procedures.

SOPs are the execution layer between system design and real-world operation.

**Governance → Policy → Rule → SOP → Execution → Evidence → Review**

---

## 2. SOP Design Principles

### 2.1 Traceability
Every critical SOP step must trace back to a policy, rule, control, authority or requirement.

### 2.2 Explicit Ownership
Every SOP has an owner responsible for correctness, currency and effectiveness.

### 2.3 Authority-Bounded Execution
An SOP must never grant authority beyond the system's defined authority model.

### 2.4 Repeatability
Two authorised operators following the same applicable SOP should reach materially consistent process outcomes, subject to documented judgement points.

### 2.5 Evidence by Design
Critical SOP steps must define what evidence is produced and retained.

### 2.6 Exception-Aware Operation
SOPs must define what happens when normal conditions are not met.

### 2.7 Human Escalation
Where judgement, risk or authority exceeds defined thresholds, the SOP must route the case to the appropriate human or higher authority.

### 2.8 Version Control
Operational instructions must be versioned and linked to their effective dates and superseded versions.

---

## 3. SOP Hierarchy

RAW OS uses a procedural hierarchy:

**Principle → Policy → Rule → Standard → SOP → Work Instruction → Checklist / Form**

- **Principle:** highest-level governance constraint.
- **Policy:** formal institutional requirement.
- **Rule:** executable decision condition.
- **Standard:** required operating level or specification.
- **SOP:** repeatable end-to-end procedure.
- **Work Instruction:** detailed task-level instruction.
- **Checklist / Form:** execution and evidence instrument.

Lower-level documents must not contradict higher-level requirements.

---

## 4. SOP Object Model

Every SOP should have a canonical identity:

- SOP ID
- Title
- Purpose
- Scope
- Owner
- Approver
- Version
- Effective Date
- Review Date
- Applicable Roles
- Required Authority
- Preconditions
- Inputs
- Tools / Systems
- Procedure Steps
- Decision Points
- Controls
- Escalation Conditions
- Exceptions
- Outputs
- Evidence Requirements
- Records / Retention
- KPIs / Quality Criteria
- Related Policies / Rules
- Change History

---

## 5. SOP Lifecycle

**NEED → DRAFT → RISK REVIEW → CONTROL REVIEW → APPROVAL → PUBLISH → TRAIN → EXECUTE → MONITOR → REVIEW → REVISE / RETIRE**

No critical SOP should enter operation without an identified owner and approval status.

---

## 6. SOP Classification

### 6.1 Governance SOP
Defines governance and approval processes.

### 6.2 Operational SOP
Defines routine execution processes.

### 6.3 Decision SOP
Defines how significant decisions are evaluated and routed.

### 6.4 Risk SOP
Defines risk identification, treatment and escalation.

### 6.5 Control SOP
Defines verification, approval, intervention and control activities.

### 6.6 Security SOP
Defines identity, access, incident and secure-operation procedures.

### 6.7 AI / Agent SOP
Defines agent operation, tool access, supervision, escalation and shutdown.

### 6.8 Data SOP
Defines data intake, validation, access, quality, lineage, retention and deletion.

### 6.9 Integration SOP
Defines interaction with external systems, interfaces and failure handling.

### 6.10 Change SOP
Defines how policies, rules, configurations, algorithms and system components are changed.

### 6.11 Incident / Recovery SOP
Defines detection, containment, response, restoration and post-incident review.

### 6.12 Audit / Assurance SOP
Defines evidence collection, review, testing and corrective action.

---

## 7. SOP Execution Model

Each SOP should be executable as:

**TRIGGER → PRECONDITION → INPUT → VALIDATE → DECISION → AUTHORISE → EXECUTE → VERIFY → RECORD → CLOSE**

Where applicable, execution returns to a decision or escalation path rather than continuing blindly.

---

## 8. Preconditions

Before execution, the SOP must establish:

- Request or trigger is valid.
- Actor identity is known.
- Actor role is known.
- Required authority is available.
- Required inputs exist.
- Required controls are operational.
- Relevant system state is compatible.
- No blocking incident or prohibition exists.

Failure of a critical precondition must result in **HOLD / REJECT / ESCALATE**, depending on the configured rule.

---

## 9. Decision Points in SOPs

SOPs may contain deterministic and judgement-based decision points.

### Deterministic Decision
A known condition produces a defined result.

**IF condition → THEN action**

### Controlled Judgement
An authorised actor assesses evidence within a defined boundary.

**EVIDENCE → ASSESSMENT → AUTHORISED JUDGEMENT → DECISION → RECORD**

### Escalated Decision
A case exceeds local authority, risk, confidence or boundary.

**TRIGGER → HOLD → CONTEXT PACKAGE → ESCALATE → REVIEW → DECIDE**

---

## 10. Control Points

Critical SOPs should identify control points explicitly:

- Input validation
- Identity verification
- Authority verification
- Separation of duties
- Approval
- Threshold check
- Dual control
- Output validation
- Evidence capture
- Post-action review

Controls must have an owner or accountable function.

---

## 11. Exception Handling

An exception must not silently bypass the SOP.

**EXCEPTION DETECTED → CLASSIFY → ASSESS → AUTHORISE EXCEPTION → EXECUTE → RECORD → REVIEW**

Exception records should include:

- Reason
- Requesting actor
- Affected process
- Risk impact
- Authorising authority
- Time limit where applicable
- Action taken
- Outcome
- Follow-up requirement

Repeated exceptions should be analysed as signals for process or policy redesign.

---

## 12. Escalation Architecture

Escalation triggers may include:

- Authority exceeded
- High / critical risk
- Low confidence
- Rule conflict
- Boundary breach
- Control failure
- Security concern
- Unknown condition
- External system failure
- Material stakeholder impact

Standard path:

**DETECT → HOLD / CONTAIN → PRESERVE CONTEXT → ROUTE → REVIEW → DECIDE → RESUME / REJECT / RECOVER**

---

## 13. Human Oversight in SOPs

Human oversight level should be explicitly specified:

- **Human-in-the-Loop:** approval required before action.
- **Human-on-the-Loop:** system operates within bounds with active monitoring and intervention capability.
- **Human-out-of-the-Loop:** fully automated execution within tightly constrained low-risk boundaries.

The SOP must state which conditions move a process from one oversight mode to another.

---

## 14. AI / Agent SOP Pattern

For AI or autonomous agents:

**IDENTIFY AGENT → LOAD POLICY CONTEXT → CHECK AUTHORITY → LOAD TOOLS → SET LIMITS → EXECUTE → MONITOR → VERIFY → RECORD → ESCALATE / CLOSE**

Minimum controls:

- Tool allow-list
- Scope restriction
- Action budget / resource limit
- Confidence or uncertainty threshold
- Risk threshold
- Human escalation path
- Kill / shutdown mechanism
- Prompt / configuration version
- Evidence and provenance

AI capability never grants authority by itself.

---

## 15. Security SOP Pattern

**IDENTIFY → AUTHENTICATE → AUTHORISE → EXECUTE → MONITOR → AUDIT → REVOKE / RECOVER**

Critical security procedures should cover:

- Account lifecycle
- Privileged access
- Credential / secret handling
- Access review
- Suspicious activity
- Incident response
- Evidence preservation
- Recovery

---

## 16. Data SOP Pattern

**COLLECT → VALIDATE → CLASSIFY → AUTHORISE → PROCESS → STORE → USE → MONITOR → RETAIN / DELETE**

The SOP should specify data owner, source, purpose, quality criteria, access restrictions, lineage and retention requirement.

---

## 17. Integration SOP Pattern

**REQUEST → AUTHENTICATE → VALIDATE → MAP → AUTHORISE → TRANSMIT → CONFIRM → RECORD**

Failure path:

**FAILURE → DETECT → CONTAIN → RETRY / FALLBACK → ESCALATE → RECONCILE → RECORD**

Cross-system actions must preserve correlation IDs and evidence continuity.

---

## 18. Evidence & Audit Trail

Each critical procedure should define a minimum evidence chain:

**TRIGGER → DECISION → AUTHORISATION → ACTION → RESULT → REVIEW**

Evidence should allow an authorised reviewer to reconstruct the material sequence of events.

Evidence should be protected against unauthorised alteration and linked to relevant object IDs, transaction IDs and versions.

---

## 19. SOP Quality Criteria

A mature SOP should be:

- Clear
- Complete
- Executable
- Authority-aligned
- Risk-aware
- Exception-aware
- Auditable
- Measurable
- Version-controlled
- Trainable

A procedure that cannot be executed consistently, audited or safely escalated is not a complete SOP.

---

## 20. SOP Metrics

Possible performance measures include:

- Process completion rate
- Error / rework rate
- Control failure rate
- Exception frequency
- Escalation frequency
- Escalation resolution time
- Compliance rate
- Evidence completeness
- Incident rate
- Outcome quality
- Time to update after identified change
- Training / competency coverage

Metrics should measure both efficiency and governance quality.

---

## 21. Training & Competency Link

SOP publication does not automatically imply operational competence.

Operational readiness path:

**SOP → TRAINING → PRACTICE → ASSESSMENT → AUTHORISED COMPETENCE → EXECUTION → REVIEW**

Where required, authority to execute a procedure should depend on verified competency.

---

## 22. Change Management

Any material change to a policy, rule, algorithm, API, database schema, AI model, integration or control may require SOP impact assessment.

Change path:

**CHANGE REQUEST → IMPACT ASSESSMENT → SOP REVIEW → APPROVAL → UPDATE → TRAIN / COMMUNICATE → EFFECTIVE DATE → MONITOR**

No material system change should silently invalidate an operational SOP.

---

## 23. Incident & Recovery SOP

Generic incident pattern:

**DETECT → CLASSIFY → CONTAIN → PRESERVE EVIDENCE → ESCALATE → REMEDIATE → RECOVER → VERIFY → CLOSE → LESSONS LEARNED**

Recovery must verify not only system availability but also governance state, evidence integrity and control effectiveness.

---

## 24. Audit & Assurance SOP

Audit procedure:

**DEFINE SCOPE → SELECT EVIDENCE → TEST CONTROL → TEST DECISION → TEST AUTHORITY → IDENTIFY GAP → REPORT → REMEDIATE → VERIFY CLOSURE**

Audit findings should feed into the RAW OS feedback and adaptation cycle.

---

## 25. SOP Dependency Graph

**GOVERNANCE → POLICY → RULE → CONTROL → SOP → WORK INSTRUCTION → OPERATION → EVIDENCE → AUDIT → FEEDBACK**

Changes can propagate upward when operational evidence reveals that a rule, policy or governance assumption is no longer adequate.

---

## 26. SOP Compatibility Test

An SOP is RAW OS-compatible when it can answer:

1. Why does the procedure exist?
2. What is its scope and boundary?
3. Who may execute it?
4. What authority is required?
5. What inputs are required?
6. What rules apply?
7. What controls apply?
8. Where are decisions made?
9. When must it escalate?
10. What exceptions are allowed?
11. What evidence is captured?
12. What outcome is expected?
13. How is performance measured?
14. How is the SOP changed or retired?

---

## 27. SOP as Execution Contract

RAW OS treats a critical SOP as an operational contract between governance and execution.

**Governance says what must be protected and why.**  
**SOP says how authorised actors are expected to operate within those constraints.**  
**Evidence proves what actually happened.**

Therefore:

**GOVERNANCE → SOP → ACTION → EVIDENCE → ASSURANCE**

---

## 28. Boundary of v1.0 — SOP Architecture

This specification does not yet define:

- Domain-specific operating procedures.
- Jurisdiction-specific legal procedures.
- Organisation-specific job descriptions.
- Vendor-specific manuals.
- Final workflow UI.
- Final automation engine.

Those belong to implementation and deployment configurations.

---

## 29. System Design Traceability

SOP Architecture maps the preceding v1.0 layers into operation:

- API → API usage procedures
- Algorithm → algorithm execution / review procedures
- Database → data handling procedures
- Event & State → state transition and incident procedures
- AI / Agent → agent operation and supervision procedures
- UI / UX → human operation procedures
- Security → security and incident procedures

All critical procedures must remain traceable to the RAW OS v0.x framework.

---

## 30. Next Layer — RAW OS v1.0

Recommended next system-design component:

**9. Deployment & Infrastructure Architecture**

This should define environments, runtime topology, observability, backup, recovery, configuration management, release flow, infrastructure boundaries and operational resilience.

---

## 31. Status

**Version:** RAW OS v1.0  
**Component:** 8. SOP Architecture  
**Status:** System Design Specification — Foundational Draft  
**Depends on:** RAW OS v0.1–v0.8 + v1.0 components 1–7  
**Design Principle:** SOPs implement governance and system design; they do not redefine the RAW OS constitution.

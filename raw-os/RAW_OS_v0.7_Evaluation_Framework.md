# RAW OS v0.7 — Evaluation Framework

**Status:** Foundational Draft  
**Depends on:** RAW OS v0.1–v0.6  
**Purpose:** Define how RAW OS itself, and any RAW OS-compatible implementation, is tested, evaluated, validated, audited, and improved before moving to implementation design.

---

## 1. Purpose of v0.7

RAW OS v0.7 establishes the evaluation constitution for the framework. It answers a central question:

> **How do we know that RAW OS is working, coherent, safe, governable, integrable and fit for purpose?**

The evaluation layer must test both the **framework** and its **implementation** without confusing the two.

**Framework correctness → Implementation correctness → Operational effectiveness → Outcome validity**

---

## 2. Evaluation Principles

### 2.1 Fitness for Purpose
A system is evaluated against its declared purpose, not against arbitrary performance alone.

### 2.2 Traceability
Every important evaluation claim should be traceable to evidence.

### 2.3 Repeatability
A meaningful test should be repeatable under defined conditions.

### 2.4 Independence
High-impact assessments should include review independent from the operator where appropriate.

### 2.5 Proportionality
Evaluation depth should correspond to risk, authority, complexity and impact.

### 2.6 Adversarial Readiness
The system must be tested not only under normal conditions but also under hostile, abnormal and failure conditions.

### 2.7 Continuous Evaluation
Passing one evaluation does not make a system permanently valid.

---

## 3. Evaluation Domains

RAW OS evaluates eight major dimensions:

1. **Purpose Alignment** — does the system serve its declared purpose?
2. **Ontology Integrity** — are system objects and relationships correctly represented?
3. **Decision Integrity** — are decisions valid, authorised and evidence-based?
4. **Control Effectiveness** — do controls actually constrain behaviour as intended?
5. **Governance Integrity** — are accountability, authority and oversight functioning?
6. **Integration Integrity** — do external connections preserve RAW OS semantics and controls?
7. **Operational Resilience** — can the system tolerate failure, uncertainty and change?
8. **Outcome Performance** — does the system produce meaningful desired outcomes?

---

## 4. Evaluation Layers

Evaluation occurs at four levels:

### 4.1 Framework Validation
Tests whether RAW OS logic itself is coherent.

### 4.2 Architecture Validation
Tests whether a proposed system architecture correctly implements RAW OS concepts.

### 4.3 Implementation Verification
Tests whether the actual software, procedures or organisational processes match their specifications.

### 4.4 Operational Validation
Tests whether the implementation performs effectively in the real operating environment.

**Logic:**

`FRAMEWORK → ARCHITECTURE → IMPLEMENTATION → OPERATION → OUTCOME`

---

## 5. Evaluation Lifecycle

`DEFINE → BASELINE → TEST → OBSERVE → ANALYSE → SCORE / CLASSIFY → REMEDIATE → RETEST → ACCEPT / REJECT / CONDITIONAL ACCEPTANCE`

Every evaluation should declare its scope, method, evidence requirements and acceptance criteria before execution where practicable.

---

## 6. Evaluation Criteria

An evaluation criterion should define:

- What is being tested.
- Why it matters.
- What evidence is required.
- What constitutes pass.
- What constitutes failure.
- What action follows failure.

Generic pattern:

`CRITERION → TEST METHOD → EVIDENCE → RESULT → FINDING → ACTION`

---

## 7. Maturity Levels

RAW OS-compatible systems may be classified using a maturity model:

### Level 0 — Unstructured
Purpose and governance are undefined or informal.

### Level 1 — Defined
Core purpose, roles, rules and boundaries exist.

### Level 2 — Controlled
Decision, authority, risk and controls are operational.

### Level 3 — Auditable
Evidence, traceability and independent review are established.

### Level 4 — Adaptive
Feedback and change management are systematic.

### Level 5 — Optimised
The system continuously improves using evidence, testing and outcome data.

Maturity level is descriptive, not a claim of absolute quality.

---

## 8. Conformance Model

RAW OS conformance should distinguish:

### 8.1 Core Conformance
The implementation preserves mandatory RAW OS concepts and invariants.

### 8.2 Governance Conformance
Authority, accountability, controls and oversight are implemented appropriately.

### 8.3 Integration Conformance
External interfaces preserve identity, authority, state and evidence semantics.

### 8.4 Operational Conformance
Actual behaviour remains within defined boundaries.

### 8.5 Outcome Conformance
The implementation produces outcomes consistent with declared objectives.

Possible statuses:

`CONFORMANT | PARTIALLY CONFORMANT | NON-CONFORMANT | NOT ASSESSED`

---

## 9. Invariants

Invariants are conditions that should remain true unless an explicitly governed exception exists.

Core examples:

- Significant action has attributable authority.
- Significant decision has an identifiable decision maker or decision mechanism.
- Critical process has evidence requirements.
- Prohibited actions cannot be silently enabled.
- Control failures trigger defined handling.
- Boundary breaches trigger rejection, containment or escalation.
- Material changes are versioned.
- Delegated authority is bounded and revocable.

A failed invariant is automatically a significant finding and may require escalation depending on risk.

---

## 10. Functional Testing

Functional tests verify that the system performs intended actions correctly.

Examples:

- Valid request acceptance.
- Invalid request rejection.
- Authority validation.
- Rule execution.
- Threshold triggering.
- Escalation.
- Approval.
- Evidence capture.
- State transition.
- External integration response.

Generic logic:

`INPUT + CONTEXT → EXPECTED STATE / ACTION`

The actual result is compared with the expected result.

---

## 11. Boundary Testing

Boundary tests verify behaviour at and beyond declared limits.

Test categories:

- Minimum boundary.
- Maximum boundary.
- Just-inside boundary.
- Just-outside boundary.
- Missing boundary data.
- Conflicting boundary conditions.
- Boundary crossing through external integration.

Expected behaviours include `ALLOW`, `RESTRICT`, `ESCALATE`, `HOLD` or `REJECT`.

---

## 12. Authority Testing

Authority tests answer:

> **Can the actor do exactly what the system says it can do — and no more?**

Test:

`IDENTITY → ROLE → CAPABILITY → AUTHORITY → SCOPE → CONDITION → ACTION`

Negative tests must attempt actions beyond authority.

A system fails authority testing if an actor can execute significant actions outside authorised scope without a valid governance path.

---

## 13. Decision Testing

Decision testing evaluates whether decision outputs are:

- Valid.
- Rule-compliant.
- Authorised.
- Evidence-supported.
- Risk-aware.
- Consistent with declared purpose.

Decision test pattern:

`INPUT → CONTEXT → RULE → ASSESSMENT → DECISION → AUTHORITY → EXPECTED OUTCOME`

Edge cases and ambiguous cases must be tested separately.

---

## 14. Risk Testing

Risk tests determine whether the risk engine correctly identifies and handles relevant risk states.

Test progression:

`LOW → MEDIUM → HIGH → CRITICAL`

Verify that appropriate control and escalation behaviour occurs at each threshold.

Also test:

- Underestimation.
- Overestimation.
- Missing risk data.
- Risk conflict.
- Residual risk.
- New / unknown risk.

---

## 15. Control Testing

Controls must be tested for actual effectiveness rather than merely documented existence.

Control tests include:

- Preventive effectiveness.
- Detective effectiveness.
- Intervention effectiveness.
- Corrective effectiveness.
- Recovery effectiveness.

A control that exists in policy but does not alter system behaviour when triggered is considered an ineffective control.

---

## 16. Adversarial / Red-Team Testing

Red-team evaluation deliberately attempts to break or bypass governance.

Examples:

- Privilege escalation.
- Authority spoofing.
- Rule bypass.
- Boundary manipulation.
- Malformed input.
- Conflicting instructions.
- Evidence deletion or tampering.
- False identity.
- Control evasion.
- Repeated exception abuse.
- Prompt / instruction manipulation for AI implementations.

The red-team objective is not merely to find defects, but to identify **governance failure modes**.

---

## 17. Failure Testing

Failure tests evaluate system behaviour when components do not behave normally.

`FAILURE → DETECT → CONTAIN → PRESERVE STATE → ESCALATE / RECOVER → RECONCILE → RECORD`

Test:

- System outage.
- Partial outage.
- API timeout.
- Invalid external response.
- Data corruption.
- Duplicate events.
- State conflict.
- Authentication failure.
- Control failure.
- Human override failure.

---

## 18. Scenario & Simulation Testing

Scenario tests reproduce realistic situations involving multiple objects and actors.

A scenario should define:

- Starting state.
- Actors.
- Inputs.
- Constraints.
- Expected decisions.
- Expected controls.
- Possible failure paths.
- Expected outcome.

Simulation becomes especially important for complex, high-uncertainty systems.

---

## 19. AI-Specific Evaluation

Where AI is used, additional evaluation dimensions apply:

- Output validity.
- Instruction adherence.
- Hallucination / unsupported-claim rate.
- Confidence calibration.
- Tool-use correctness.
- Authority adherence.
- Refusal / escalation behaviour.
- Prompt injection resilience.
- Data leakage resistance.
- Consistency under adversarial inputs.

The key principle remains:

`AI CAPABILITY ≠ AI AUTHORITY`

AI evaluation must test not only whether the model can perform a task, but whether it knows when **not** to perform it.

---

## 20. Human Oversight Evaluation

Human-in-the-loop systems must test:

- Whether humans receive sufficient context.
- Whether approvals are meaningful.
- Whether reviewers can detect relevant risks.
- Whether intervention can stop action in time.
- Whether workload makes oversight practically ineffective.

A human approval button that is routinely bypassed, ignored or impossible to exercise in time is not effective oversight.

---

## 21. Evidence Quality Evaluation

Evidence must be assessed for:

- Completeness.
- Accuracy.
- Integrity.
- Timestamp validity.
- Attribution.
- Traceability.
- Retention.
- Reconstructability.

A critical event should be reconstructable from available evidence to a reasonable level appropriate to its risk.

---

## 22. Audit Framework

Audit evaluates whether the system operates according to its declared governance and controls.

Audit sequence:

`SCOPE → CRITERIA → EVIDENCE → TEST → FINDING → SEVERITY → CORRECTIVE ACTION → FOLLOW-UP`

Findings can be classified as:

- Observation.
- Minor non-conformity.
- Major non-conformity.
- Critical failure.

Severity classification must be tied to impact and risk, not merely to administrative inconvenience.

---

## 23. Evaluation Severity

A generic severity model:

### Critical
Immediate or potentially catastrophic governance, safety, legal, security or control failure.

### High
Material failure requiring prompt remediation or restricted operation.

### Medium
Meaningful weakness requiring controlled remediation.

### Low
Localised weakness with limited immediate impact.

### Observation
Improvement opportunity without established non-conformance.

---

## 24. Acceptance Logic

Possible evaluation outcomes:

### PASS
All mandatory criteria met.

### CONDITIONAL PASS
Minor defined gaps accepted with remediation plan and constraints.

### HOLD
Evidence insufficient or unresolved issue prevents safe acceptance.

### FAIL
Mandatory criteria or critical invariants are not met.

### REJECT
The system is fundamentally incompatible with required RAW OS governance or purpose.

---

## 25. Remediation Logic

`FINDING → ROOT CAUSE → CORRECTIVE ACTION → OWNER → DEADLINE → RETEST → CLOSE`

Repeated findings must trigger investigation of structural causes rather than repeated local fixes.

---

## 26. Root Cause Analysis

When a failure occurs, evaluation should distinguish:

- Event.
- Immediate cause.
- Contributing causes.
- Systemic cause.
- Governance cause.
- Control failure.
- Human / organisational factor.

This prevents symptoms from being mistaken for root causes.

---

## 27. Regression Testing

Any material change to rules, authority, controls, ontology, adapters, models, APIs, policies or workflows may affect previous behaviour.

Therefore:

`CHANGE → IMPACT ASSESSMENT → REGRESSION SUITE → TEST → REVIEW → RELEASE`

Critical controls must remain covered by regression tests.

---

## 28. Change Evaluation

Every material change should be evaluated for:

- Purpose impact.
- Boundary impact.
- Authority impact.
- Risk impact.
- Control impact.
- Integration impact.
- Evidence impact.
- Stakeholder impact.

No material change should be considered complete solely because the new software or procedure works technically.

---

## 29. Evaluation Metrics

Possible framework-level metrics include:

- Conformance rate.
- Critical invariant pass rate.
- Decision validity rate.
- Authority violation rate.
- Control effectiveness rate.
- Escalation accuracy.
- False acceptance / false rejection rate.
- Evidence completeness rate.
- Mean time to detect.
- Mean time to contain.
- Mean time to remediate.
- Regression failure rate.
- Repeated finding rate.
- Outcome effectiveness.

Metrics must be interpreted together; a single score must not conceal critical failures.

---

## 30. Evaluation Independence

Independence should be proportional to risk.

Low-risk systems may use internal review.

Higher-risk systems should introduce increasing separation between:

`OPERATOR → EVALUATOR → ASSURANCE`

The party responsible for executing a control should not always be the sole party deciding whether the control is effective.

---

## 31. Evidence Pack

A RAW OS evaluation should produce a structured evidence pack containing, as appropriate:

- Evaluation plan.
- Scope.
- Version information.
- Architecture / configuration.
- Test cases.
- Test results.
- Logs.
- Decision records.
- Risk assessments.
- Control results.
- Red-team results.
- Audit findings.
- Remediation records.
- Retest results.
- Acceptance decision.

This becomes the historical institutional memory of system assurance.

---

## 32. Framework-Level Validation

Before RAW OS itself is frozen, the framework must be tested against multiple domains.

Recommended test domains:

1. AI Agent System.
2. Community Programme.
3. Organisational Process.
4. Business Operations.
5. Political / Campaign Operations.

The test is successful when the same core primitives remain usable while domain-specific configuration changes.

---

## 33. Universality Test

The claim of domain neutrality should be treated as a hypothesis until demonstrated.

Test:

`SAME CORE OBJECTS + SAME GOVERNANCE LOGIC + DIFFERENT DOMAIN CONFIGURATION`

Evaluate whether the framework can represent each domain without excessive exceptions or domain-specific rewrites.

If the core requires repeated exceptions, the ontology or logic may not yet be sufficiently universal.

---

## 34. Stress Test of the Framework

RAW OS itself should be stress-tested for:

- Ambiguous concepts.
- Overlapping concepts.
- Circular dependencies.
- Contradictory rules.
- Missing authority.
- Unobservable events.
- Untraceable decisions.
- Excessive complexity.
- Implementation ambiguity.
- Domain-specific assumptions hidden inside the core.

This is a **meta-evaluation**: evaluating the evaluator.

---

## 35. Framework Acceptance Criteria

RAW OS should not proceed to full system-design freeze unless it demonstrates:

- Coherent ontology.
- Consistent decision logic.
- Explicit authority model.
- Functional risk/control model.
- Governance accountability.
- Integration compatibility.
- Testability.
- Auditability.
- Adaptation capability.
- Cross-domain applicability.

---

## 36. Evaluation Principle of Last Resort

When evaluation cannot establish sufficient evidence for a high-impact action, the system should prefer:

`HOLD → ESCALATE → REVIEW`

over unsupported certainty.

Uncertainty is itself an evaluation finding when it materially affects safe or legitimate operation.

---

## 37. Boundary of v0.7

v0.7 does **not** yet define:

- A specific software testing framework.
- A specific database test suite.
- A specific AI benchmark.
- A legal certification scheme.
- A specific audit standard.
- A numerical universal score.

Those belong to implementation and domain-specific validation layers.

---

## 38. Next Layer — RAW OS v0.8

**RAW OS v0.8 — Complete Framework / Reference Framework** should consolidate v0.1–v0.7 into one coherent reference architecture, resolve terminology conflicts, define mandatory versus configurable elements, establish framework invariants, and prepare a formal **Framework Freeze Gate** before v1.0 System Design.

---

## 39. RAW OS Version Sequence

`v0.1 Core Logic`

→ `v0.2 System Ontology`

→ `v0.3 Decision & Control Logic`

→ `v0.4 Operating Architecture`

→ `v0.5 Governance Framework`

→ `v0.6 Integration Framework`

→ `v0.7 Evaluation Framework`

→ `v0.8 Complete RAW OS Framework`

→ `v1.0 System Design Specification`

→ `API / Database / UI / AI / SOP / Deployment`

---

## 40. Status

**Version:** RAW OS v0.7  
**Title:** Evaluation Framework  
**Status:** Foundational Draft  
**Depends on:** v0.1–v0.6  
**Primary function:** Verify, validate, audit, stress-test and continuously improve RAW OS and its implementations.  
**Design principle:** Evidence-driven, risk-proportionate, repeatable, adversarially tested, auditable and adaptive.

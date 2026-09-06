# RAW OS v0.9 — AI/UX Prototype Design

**Status:** Prototype Design
**Domain:** Abang Sayur Pilot
**Purpose:** Translate RAW OS governance, decision, control, evidence and actor logic into a usable human-facing interface with an AI assistant that operates within explicit authority.

## 1. Design Principle

The interface may reveal, guide and request action; it must never manufacture authority.

UI/UX is a Human-System Interface Layer. It exposes RAW OS state and available actions according to identity, role, authority, context and policy.

## 2. Primary Users

1. URK / Programme Operator
2. Pioneer / Actor
3. Programme / Area Owner
4. Compliance / Risk Reviewer
5. Auditor / Assurer
6. System Administrator

## 3. Core Navigation

- Dashboard
- Actors
- Transactions
- Authority
- Areas & Scope
- Inventory
- Rules & Policies
- Risk & Compliance
- Audit & Evidence
- AI Assistant
- Reports
- Settings

## 4. Dashboard

Dashboard provides:
- Active actors
- Transactions
- Recognised sales
- Void transactions
- Items under review
- Recent transactions
- Area coverage
- Compliance alerts
- Tasks and approvals
- System status

The dashboard must distinguish operational metrics from governance metrics.

## 5. Actor Profile

Minimum sections:
- Identity
- Role
- Capability
- Authority
- Credit limit / exposure
- Geographic scope
- Current status
- Transaction history
- Compliance history
- Evidence history

The UI must visually distinguish:
**Identity → Capability → Authority → Actual Activity.**

## 6. Transaction View

Transaction states:
- Draft
- Submitted
- Pending validation
- Valid
- Blocked
- Void
- Disputed
- Under review
- Approved / resolved

A transaction detail screen should show:
- Actor
- Transaction type
- Amount
- Area
- Related purchase
- Permission
- Rules evaluated
- Risk checks
- Decision
- Evidence
- Reviewer actions

## 7. Authority & Scope View

Show authority as bounded permissions rather than binary access.

Example:
- Purchase authority: ≤ RM1,000
- Sales authority: Area A
- Permission status: none / active / expired
- Validity period

The UI must never imply that a role automatically grants unrestricted authority.

## 8. Compliance Alert UX

Example alert:

**Actor 1 — Multiple Violations**
- Credit limit exceeded
- Sale outside authorised area
- No prior permission

Available actions:
- View evidence
- Notify actor
- Create compliance case
- Escalate
- Review

Punitive actions require explicit authority and should not appear as automatic consequences of a rule breach.

## 9. Void Transaction UX

A void transaction must remain visible in audit/evidence views.

Operational ledger:
- Recognised sales exclude void transaction.

Governance ledger:
- Original submission preserved.
- Void reason preserved.
- Decision and rule evidence preserved.

UI label:
**VOID — Not recognised operationally; evidence preserved.**

## 10. AI Assistant

AI Assistant roles:
- Explain system decisions
- Summarise actor / transaction history
- Surface relevant rules
- Recommend next actions
- Detect anomalies
- Prepare review packages

AI does not independently grant authority, change credit limits, expand geographic scope, delete evidence or bypass controls.

## 11. AI Decision Trace

Every AI recommendation should expose:
1. Input received
2. Context used
3. Relevant rules
4. Authority context
5. Risk considerations
6. Recommendation
7. Required human approval, if any
8. Evidence references

AI explanation is not a substitute for authoritative system records.

## 12. AI Interaction Pattern

User question:
“Why was Actor 1’s sales submission void?”

AI should answer using structured evidence:
- Credit breach
- Geographic scope breach
- Missing permission
- Resulting decision
- Evidence reference
- Available remediation options

## 13. Recommended Actions

AI recommendations must be separated from executable actions.

Example:
**Recommendation:** Review Actor 1 compliance case.

**Action:** Create Case

The action button must trigger an authority check before execution.

## 14. Approval UX

Approval screen must show:
- Requested action
- Actor
- Scope
- Authority required
- Current authority
- Risk level
- Applicable policy/rule
- Evidence
- Expected outcome
- Expiry / validity when relevant

Primary controls:
- Approve
- Reject
- Escalate
- Request More Information

## 15. Area & Scope UX

Map or structured view should show:
- Authorised areas
- Pending extensions
- Restricted areas
- Breach events

Area extensions should be explicitly time-bound and separately scoped from other permissions.

## 16. Human Oversight

The UI supports three oversight patterns:
- Human-in-the-loop: approval required
- Human-on-the-loop: monitoring and intervention
- Human-out-of-the-loop: bounded automation

The interface must clearly indicate which mode applies to the current action.

## 17. Evidence UX

Evidence panel should provide:
- Decision ID
- Event ID
- Actor
- Timestamp
- Rule version
- Authority version
- Control applied
- Outcome
- Related transaction
- Related external IDs

Evidence records must be read-only for normal operators.

## 18. Error / Exception UX

When a system action cannot proceed:
- Explain why
- Show which rule/control failed
- Show whether retry is possible
- Show escalation path
- Preserve failed attempt evidence when required

Example:
**Blocked: Credit authority exceeded by RM500.**

## 19. Accessibility & Clarity

UI should not rely on colour alone for status. Every status should include text and an icon/semantic marker.

Critical states should use explicit language:
- VALID
- BLOCKED
- VOID
- UNDER REVIEW
- ESCALATED
- EXPIRED

## 20. Security UX

Sensitive information should be minimised by role.

The UI must enforce server-side authorisation; hiding a button is not a security control.

## 21. UX State Machine

USER INTENT → UI REQUEST → AUTHORITY CHECK → CONTROL CHECK → ACTION → EVENT → STATE UPDATE → EVIDENCE

## 22. Prototype Test — Actor 1

Scenario:
- Credit limit RM1,000
- Purchase RM1,500
- Authorised area A
- Sale area C
- No prior permission

Expected UI state:
- Purchase: BLOCKED
- Area C sales: VOID
- Actor: COMPLIANCE REVIEW
- Evidence: PRESERVED
- AI: Explain + recommend; no unauthorised execution

## 23. AI/UX Invariants

1. UI cannot grant authority.
2. AI recommendation cannot equal execution authority.
3. Void cannot mean delete.
4. Evidence cannot disappear because an operational transaction is invalid.
5. High-impact actions require explicit authority and appropriate oversight.
6. Every actionable recommendation must resolve to a permission/control check.

## 24. Prototype Success Criteria

Prototype passes when:
- Actors can see only permitted actions.
- Invalid transactions are clearly blocked or voided.
- Operators can reconstruct why a decision occurred.
- AI explanations reference actual system evidence.
- Approval flows enforce authority.
- Audit evidence remains preserved.
- No UI shortcut bypasses governance.

## 25. Next Implementation Layer

This document is a UX and AI interaction contract for prototype implementation. It does not yet specify the final frontend framework, production design system or production AI provider.

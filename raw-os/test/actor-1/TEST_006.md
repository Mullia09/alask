# RAW OS Test 006 — Actor 1 Compound Violation

Status: SIMULATED

## Scenario
Actor 1 (Pioneer) has an authorised geographic scope of Area A and a credit limit of RM1,000. Actor 1 attempts a purchase of RM1,500, conducts sales in Area C without prior permission, and submits the Area C daily sales for recognition.

## Expected Evaluation
- Credit authority: FAIL — request exceeds credit limit by RM500.
- Geographic authority: FAIL — Area C is outside authorised Area A.
- Permission: FAIL — no prior permission was obtained.
- Risk: ELEVATED due to combined credit, scope, and permission breaches.

## Expected Decision
- Purchase transaction: BLOCKED.
- Area C sales submission: VOID for operational recognition.
- Original submission and decision evidence: PRESERVED.
- Actor status: COMPLIANCE REVIEW / ESCALATION AVAILABLE.

## Accounting Expectation
Reported sales may remain in the audit record, but only valid transactions enter the recognised sales ledger. Example test value: reported RM500; recognised RM0; void RM500.

## Assertions
1. Capability does not imply authority.
2. Independent constraints are evaluated independently before decision aggregation.
3. VOID removes operational validity; it does not delete historical evidence.
4. Blocking a transaction does not automatically create punitive authority over the actor.

# RAW OS v0.3 — Decision & Control Logic

**Status:** Foundational Draft  
**Depends on:** RAW OS v0.1 Core Logic System Foundation + RAW OS v0.2 System Ontology  
**Design principle:** Domain-neutral, modular, composable, auditable, risk-aware and adaptive.

## 1. Tujuan
RAW OS v0.3 mengubah ontology v0.2 kepada decision-and-control logic yang boleh digunakan untuk mengawal tingkah laku sesuatu sistem. Fokus utama ialah bagaimana input dinilai, keputusan dibuat, authority disahkan, action dikawal, exception ditangani dan escalation berlaku.

## 2. Core Decision Principle
`INPUT → CONTEXT → ASSESSMENT → DECISION → AUTHORITY CHECK → CONTROL CHECK → ACTION → OUTCOME`

Tiada tindakan significant sepatutnya berlaku hanya kerana capability wujud. Action mesti melalui logic yang menghubungkan purpose, rule, authority, risk dan control.

## 3. Decision Pipeline
### 3.1 INPUT
Terima request, event, signal, data atau trigger.

### 3.2 CONTEXT
Tentukan keadaan, scope, actor, environment dan relevant constraints.

### 3.3 ASSESSMENT
Nilai fakta, confidence, impact, risk dan applicable rules.

### 3.4 DECISION
Pilih keputusan yang sesuai berdasarkan evidence dan rules.

### 3.5 AUTHORITY CHECK
Sahkan actor mempunyai authority yang mencukupi.

### 3.6 CONTROL CHECK
Sahkan action mematuhi controls, thresholds dan constraints.

### 3.7 ACTION
Laksanakan action yang telah diluluskan.

### 3.8 OUTCOME
Ukur dan rekod hasil action.

## 4. Decision Classes
### 4.1 AUTO
Decision boleh dibuat dan dilaksanakan secara automatik dalam predefined boundary.

### 4.2 ASSISTED
System membuat recommendation; human atau authorised actor membuat keputusan.

### 4.3 APPROVAL REQUIRED
Decision mesti mendapat approval sebelum action.

### 4.4 ESCALATION REQUIRED
Decision berada di luar threshold, authority atau confidence yang dibenarkan.

### 4.5 PROHIBITED
Action tidak dibenarkan walaupun capability wujud.

## 5. Decision Conditions
Decision rule boleh dinyatakan sebagai:

`IF [CONDITION] → THEN [DECISION/ACTION] → SUBJECT TO [CONSTRAINT] → WITH [AUTHORITY]`

Komponen minimum: condition, threshold, exception, constraint, required evidence dan required authority.

## 6. Authority Logic
`REQUEST → IDENTIFY ACTOR → CHECK ROLE → CHECK CAPABILITY → CHECK AUTHORITY → CHECK SCOPE → PROCEED / ESCALATE / REJECT`

**Capability menjawab “boleh buat secara teknikal”; Authority menjawab “dibenarkan buat dalam konteks ini”.**

## 7. Risk-Gated Decision
`DECISION → RISK ASSESSMENT → RISK LEVEL → CONTROL REQUIREMENT → ACTION / ESCALATE / STOP`

- Low Risk → standard control
- Medium Risk → enhanced control
- High Risk → approval / human review
- Critical Risk → stop / prohibited unless exceptional authority exists

## 8. Control Logic
Control boleh beroperasi pada lima titik:

- Input Control
- Process Control
- Decision Control
- Action Control
- Output Control

Control sequence:
`PREVENT → DETECT → INTERVENE → CORRECT → LEARN`

## 9. Threshold Logic
Threshold menentukan apabila behaviour normal mesti berubah kepada review, escalation atau stop.

Threshold boleh meliputi confidence, risk, authority, value/financial, impact, time dan performance.

`IF VALUE ≤ THRESHOLD → NORMAL FLOW`  
`IF VALUE > THRESHOLD → ENHANCED CONTROL / ESCALATION`

## 10. Escalation Logic
`TRIGGER → FREEZE / HOLD → PACKAGE CONTEXT → IDENTIFY HIGHER AUTHORITY → REVIEW → DECIDE → RESUME / REJECT`

Triggers termasuk insufficient authority, insufficient confidence, high/critical risk, rule conflict, boundary breach, unknown condition dan control failure.

## 11. Exception Logic
`NORMAL RULE → EXCEPTION DETECTED → CLASSIFY → APPLY EXCEPTION RULE → AUTHORISE → RECORD → REVIEW`

Exception bukan bypass governance. Significant exceptions memerlukan justification, authority dan evidence; exception berulang patut mencetuskan policy/rule review.

## 12. Human-in-the-Loop Logic
- **Human-in-the-Loop:** human mesti approve sebelum action.
- **Human-on-the-Loop:** system acts within boundary while human monitors and can intervene.
- **Human-out-of-the-Loop:** fully automated action within tightly defined controls.

Semakin tinggi risk, impact, uncertainty atau authority requirement, semakin tinggi tahap human involvement.

## 13. Decision Record
Minimum Decision Record:
- Decision ID
- Timestamp
- Actor
- Role
- Input
- Context
- Applicable Rule
- Authority
- Risk Level
- Control Applied
- Decision
- Rationale
- Approval / Escalation
- Expected Outcome
- Actual Outcome
- Evidence Reference

## 14. Control Failure Logic
`CONTROL FAILURE → DETECT → CONTAIN → ASSESS IMPACT → ESCALATE → RECOVER → RECORD → REVIEW`

Control failure mesti diperlakukan sebagai governance event, bukan sekadar technical error.

## 15. Conflict Resolution
Apabila rules, authorities atau objectives bercanggah, precedence logic ialah:

`SAFETY / LEGAL / HARD CONSTRAINT → AUTHORITY → POLICY → OBJECTIVE → OPTIMISATION`

Jika conflict tidak boleh diselesaikan secara sah, default behaviour ialah HOLD / ESCALATE.

## 16. Decision Quality
Decision boleh dinilai melalui:
- Validity
- Evidence
- Authority
- Risk
- Outcome

Decision yang technically correct tetapi tidak authorised tetap governance failure.

## 17. Control Architecture
`RULES → PERMISSIONS → THRESHOLDS → VALIDATION → APPROVAL → EXECUTION → MONITORING → AUDIT`

## 18. Core Decision Loop
`OBSERVE → INTERPRET → ASSESS → DECIDE → AUTHORISE → CONTROL → ACT → MEASURE → RECORD → REVIEW`

Review menghasilkan feedback untuk rule, threshold, control dan capability update.

## 19. Decision State Machine
Normal path:
`PROPOSED → ASSESSED → AUTHORISED → CONTROLLED → EXECUTING → COMPLETED`

Alternative states:
`REJECTED`, `ESCALATED`, `ON HOLD`, `FAILED`, `OVERRIDDEN`, `CANCELLED`.

## 20. Minimum Decision Gate
Sebelum significant action dilaksanakan, system perlu menjawab:

- What is being requested?
- Why is it being done?
- Who is acting?
- Does the actor have capability?
- Does the actor have authority?
- Which rule applies?
- What is the risk?
- What controls apply?
- Does the action cross a threshold?
- Is escalation required?
- What evidence must be recorded?

## 21. RAW OS Decision Formula
`DECISION QUALITY ≈ PURPOSE ALIGNMENT + RULE COMPLIANCE + AUTHORITY VALIDITY + EVIDENCE QUALITY + RISK CONTROL + OUTCOME PERFORMANCE`

Ini ialah conceptual model, bukan mathematical scoring model pada tahap v0.3.

## 22. Integration Logic
`DOMAIN SYSTEM → MAP OBJECTS → DEFINE RULES → DEFINE AUTHORITY → DEFINE THRESHOLDS → DEFINE CONTROLS → DEFINE ESCALATION → CAPTURE EVIDENCE`

Boleh digunakan untuk AI Agent, Community Program, Organisation, Political Operation, Business Process atau Public Service.

## 23. Boundary of v0.3
v0.3 belum menentukan platform, database engine, API specification, domain-specific policy, scoring algorithm atau UI. Fokusnya ialah logic keputusan dan kawalan yang boleh diterjemahkan kemudian kepada implementation.

## 24. Next Layer
**RAW OS v0.4 — Operating Architecture**

## 25. Status Dokumen
**Version:** RAW OS v0.3  
**Status:** Decision & Control Logic — Foundational Draft  
**Depends on:** v0.1–v0.2  
**Design Principle:** Domain-neutral, modular, composable, auditable, risk-aware and adaptive.

# RAW OS v0.1 — Core Logic System Foundation

**Status:** Core Logic System Foundation — Raw Draft  
**Nature:** Domain-neutral / experimental

## 1. Premis Asas
Setiap sistem yang mempunyai tujuan, aktor, keputusan dan tindakan memerlukan mekanisme untuk menentukan apa yang boleh berlaku, siapa yang boleh melakukannya, bagaimana ia dikawal, bagaimana ia dibuktikan, dan bagaimana ia diperbaiki.

## 2. Core Logic Primitives

### 2.1 PURPOSE
Sistem mesti tahu kenapa ia wujud.
- Input: Need, Problem, Objective, Desired Outcome
- Logic: WHY → OBJECTIVE → OUTCOME
- Tanpa Purpose, sistem hanya melakukan aktiviti.

### 2.2 BOUNDARY
Sistem mesti tahu sempadannya.
- Apa yang sistem boleh lakukan?
- Apa yang sistem tidak boleh lakukan?
- Dalam keadaan apa kuasanya berubah?
- Bila perlu menyerahkan keputusan kepada pihak lain?
- Logic: IN → WITHIN AUTHORITY → OUT
- Kuasa tanpa boundary = uncontrolled system.

### 2.3 ACTOR
Setiap tindakan mesti mempunyai actor.
- Actor: Human / AI / Organisation / Process / External System
- Logic: ACTOR → ROLE → CAPABILITY → RESPONSIBILITY

### 2.4 AUTHORITY
Siapa boleh membuat keputusan apa?
- Authority = Scope + Level + Condition
- Capability ≠ Authority.
- Sesuatu actor mungkin mampu melakukan sesuatu tetapi tidak semestinya mempunyai kuasa untuk melakukannya.

### 2.5 RULE
Bagaimana sistem sepatutnya bertindak?
- IF CONDITION → THEN ACTION → SUBJECT TO CONSTRAINT
- Rule bukan sekadar polisi; rule mesti boleh diterjemahkan kepada decision logic.

### 2.6 DECISION
Sistem perlu mempunyai mekanisme memilih tindakan.
- INPUT → ASSESS → DECIDE → AUTHORISE → ACT
- Decision ≠ Action.
- Intelligence, Judgement, Authority dan Execution perlu boleh dibezakan.

### 2.7 RISK
Setiap tindakan mempunyai kemungkinan menghasilkan outcome yang tidak dikehendaki.
- ACTION → RISK → IMPACT
- IDENTIFY → ASSESS → MITIGATE → ACCEPT / ESCALATE
- Residual Risk mesti direkod dan diurus.

### 2.8 CONTROL
Control memastikan sistem tidak bergerak melebihi authority dan rules.
- Input Control
- Process Control
- Decision Control
- Action Control
- Output Control
- Validation, Permission, Threshold, Constraint, Approval, Escalation, Override, Shutdown

### 2.9 EVIDENCE
Sistem mesti boleh menjawab: “Apa sebenarnya yang berlaku?”
- EVENT → RECORD → TRACE → EVIDENCE
- Siapa/apa bertindak, bila, berdasarkan input apa, authority apa, rule apa, keputusan apa, tindakan apa dan outcome apa.
- Evidence menghasilkan Auditability + Accountability + Institutional Memory.

### 2.10 LEARNING / ADAPTATION
Sistem mesti boleh belajar daripada realiti.
- OUTCOME → FEEDBACK → REVIEW → LEARN → UPDATE → NEW BEHAVIOUR
- Cycle kembali kepada Purpose, Rules dan Controls.

## 3. Core Loop
PURPOSE → SCOPE → ACTOR + AUTHORITY → RULE → INPUT → DECISION → RISK → CONTROL → ACTION → OUTCOME → EVIDENCE → FEEDBACK → ADAPTATION

## 4. Foundation Layer
- **DATA** — apa yang sistem tahu.
- **PEOPLE** — siapa yang mempunyai agency.
- **TECHNOLOGY** — infrastructure yang sistem gunakan.
- **CAPABILITY** — apa yang sistem mampu lakukan.
- **CHANGE / ADAPTATION** — mekanisme perkembangan sistem.

## 5. Fundamental System Logic
REAL WORLD → OBSERVE → INTERPRET → DECIDE → AUTHORISE → ACT → MEASURE → RECORD → REVIEW → ADAPT

## 6. Governance Layer
Governance mengawal keseluruhan cycle melalui Purpose, Rules, Authority, Decision, Control, Evidence dan Learning.

## 7. Composability & Integration
RAW OS bukan sistem yang menggantikan sistem lain. Ia menjadi governance layer / protocol yang boleh dipasang kepada AI, organisasi, komuniti, political operation, business process atau public service.

Standard mapping interface:
PURPOSE | SCOPE | ACTOR | AUTHORITY | RULE | DECISION | RISK | CONTROL | ACTION | EVIDENCE | FEEDBACK

Core logic kekal; configuration berubah mengikut domain.

## 8. Core Axioms
1. **Purpose:** No system without a defined purpose.
2. **Authority:** No action without defined authority.
3. **Accountability:** No significant decision without attributable responsibility.
4. **Evidence:** No critical process without observable evidence.
5. **Adaptation:** No governance system remains valid without feedback and adaptation.

## 9. Working Definition
RAW OS ialah universal governance logic yang menyediakan primitive, hubungan dan cycle asas untuk memahami, mengawal, melaksanakan, merekod dan menyesuaikan sesuatu sistem.

## 10. Status Dokumen
- Version: RAW OS v0.1
- Status: Core Logic System Foundation — Raw Draft
- Design Principle: Domain-neutral, modular, composable, auditable, adaptive
- Next: RAW OS v0.2 — System Ontology

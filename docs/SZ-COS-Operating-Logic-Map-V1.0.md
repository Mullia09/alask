# SZ-COS — Constituency Operating System
## Operating Logic Map V1.0

**Status:** Working Architecture Draft 1.0  
**Parent Foundation:** SZ-COS Governance Foundation V1.0  
**Scope:** Pejabat Wakil Rakyat — DUN / Parlimen  
**Purpose:** Memetakan perjalanan kerja sebenar dalam Pejabat YB daripada interaksi awal sehingga tindakan, penyelarasan kerajaan, outcome dan pembelajaran institusi.

---

## 0. Operating Premise

SZ-COS melihat Pejabat Wakil Rakyat sebagai **interface institution** antara constituency, YB, organisasi masyarakat dan sistem kerajaan.

Prinsip operasi:

> **Capture once → Classify correctly → Route to the right owner → Act → Coordinate where necessary → Escalate by threshold → Record outcome → Learn.**

Tidak semua rekod perlu melalui semua langkah. Namun setiap urusan substantif mesti mempunyai tahap rekod, ownership dan outcome yang sesuai.

---

# 1. MASTER OPERATING LOGIC

```text
REAL-WORLD INTERACTION
        ↓
CAPTURE
        ↓
CLASSIFY
        ↓
CREATE / LINK RECORD
        ↓
ASSIGN OWNER
        ↓
ASSESS
        ↓
┌─────────────────────────────────────┐
│ Apa bentuk tindakan yang diperlukan?│
└─────────────────────────────────────┘
        ↓
  ┌─────┼────────┬────────┬─────────┐
  ↓     ↓        ↓        ↓         ↓
OFFICE AGENCY COMMUNITY YB/POLICY  NO ACTION
ACTION  ACTION  ACTION    ACTION      /
                                  MONITOR
  ↓     ↓        ↓        ↓         ↓
  └─────┴────────┴────────┴─────────┘
        ↓
FOLLOW-UP / COORDINATION
        ↓
ESCALATE IF THRESHOLD MET
        ↓
OUTCOME
        ↓
CLOSE / KEEP OPEN
        ↓
INTELLIGENCE / LEARNING
```

---

# 2. ENTRY LOGICS

## 2.1 Walk-in

**Trigger:** Individu/organisasi hadir di pejabat.

**Flow:**

`Walk-in → Intake → Identity/Organisation capture → Purpose → Classification → Record → Routing`

Minimum capture:
- siapa;
- organisasi jika berkaitan;
- lokasi;
- tujuan;
- isu/permintaan;
- dokumen/bukti jika perlu;
- action required.

---

## 2.2 Digital / WhatsApp / Phone / Online

**Trigger:** Maklumat diterima melalui saluran digital atau telefon.

**Flow:**

`Message/Call → Intake → Validate enough information → Record → Follow-up if incomplete → Classify`

Prinsip: saluran masuk boleh banyak, tetapi **rekod operasi mesti berpusat**.

---

## 2.3 Surat / Memo / Official Referral

`Document Received → Register → Link Person/Organisation → Classify → Assign → Process → Archive`

---

## 2.4 YB / Staff Encounter

Interaksi spontan semasa lawatan atau pertemuan juga boleh menghasilkan rekod.

`Encounter → Quick Capture → Tag → Link to Person/Organisation/Location → Determine whether Actionable → Monitor / Convert to Case/Concern`

---

# 3. CASE LOGIC

Digunakan apabila seseorang atau komuniti mempunyai masalah yang memerlukan tindakan.

```text
CASE INTAKE
   ↓
VERIFY / UNDERSTAND
   ↓
CLASSIFY
   ↓
ASSIGN CASE OWNER
   ↓
ASSESS REQUIRED ACTION
   ↓
ACTION / REFERRAL / COORDINATION
   ↓
FOLLOW-UP
   ↓
OUTCOME
   ↓
CLOSE OR ESCALATE
```

### Case states

`NEW → TRIAGED → ASSIGNED → IN PROGRESS → PENDING → ESCALATED → RESOLVED → CLOSED`

`PENDING` mesti mempunyai sebab/status, bukan menjadi tempat kes “hilang”.

---

# 4. APPLICATION / REQUEST LOGIC

Digunakan untuk permohonan bantuan, barangan, sokongan atau perkhidmatan.

```text
APPLICATION
   ↓
VERIFY
   ↓
ASSESS
   ↓
RECOMMEND
   ↓
DECISION
   ↓
┌──────────────┬──────────────┐
↓              ↓              ↓
APPROVED     REFERRED      NOT APPROVED
↓              ↓              ↓
FULFIL        AGENCY        RECORD REASON
MENT           ROUTE             ↓
↓              ↓             ALTERNATIVE
PROOF OF       RESPONSE        OPTION
RECEIPT        ↓
↓              ↓
CLOSE          CLOSE
```

### Special application objects

Pemohon boleh terdiri daripada:
- individu/keluarga;
- peniaga/microbusiness;
- institusi agama;
- NGO/persatuan;
- komuniti;
- organisasi/institusi lain yang berkaitan.

Person dan Organisation mesti disimpan sebagai objek berbeza tetapi boleh saling berhubung.

---

# 5. GOODS / ASSISTANCE FULFILMENT LOGIC

Untuk permohonan barang:

`Request → Item Definition → Quantity → Assessment → Approval → Source (Inventory / Procurement / Referral) → Allocation → Delivery → Proof of Receipt → Close`

### Control points

- item;
- quantity;
- estimated/actual value where applicable;
- approval authority;
- source;
- delivery date;
- recipient;
- acknowledgement;
- outstanding commitment.

---

# 6. GOVERNMENT REFERRAL LOGIC

Apabila pejabat tidak mempunyai bidang kuasa atau penyelesaian terletak pada kerajaan/agensi lain:

```text
CASE / ISSUE
    ↓
AUTHORITY CLASSIFICATION
    ↓
SELECT RESPONSIBLE AGENCY
    ↓
FORMAL / APPROPRIATE REFERRAL
    ↓
ACKNOWLEDGEMENT / RESPONSE
    ↓
FOLLOW-UP
    ↓
OUTCOME
```

Pejabat tidak mengambil alih fungsi agensi.

**Objective:** memastikan kes tidak tersekat kerana sempadan organisasi.

---

# 7. GOVERNMENT COORDINATION LOGIC

Digunakan apabila satu isu memerlukan lebih daripada satu organisasi atau agensi.

`Issue → Stakeholder Map → Coordination Request → Joint Discussion → Action Matrix → PIC + Deadline → Follow-up → Outcome`

### Action Matrix minimum

| Action | Owner | Supporting Agency | Due Date | Status | Evidence | Outcome |
|---|---|---|---|---|---|---|

---

# 8. DISTRICT / AGENCY INTERFACE LOGIC

Jabatan Daerah atau agensi berfungsi sebagai **government-side interface/node** apabila sesuai dengan bidang kuasa dan struktur pentadbiran.

```text
PEJABAT YB
    ↓
CASE / ISSUE BRIEF
    ↓
DISTRICT / LEAD AGENCY
    ↓
COORDINATION
    ↓
RESPONSIBLE AGENCIES
    ↓
ACTION
    ↓
STATUS / RESPONSE
    ↓
PEJABAT YB
    ↓
CONSTITUENT / STAKEHOLDER
```

Nota: Tidak semua kes perlu melalui Jabatan Daerah; routing sentiasa berdasarkan bidang kuasa sebenar.

---

# 9. COMMUNITY ENGAGEMENT LOGIC

Tidak semua interaksi ialah aduan.

```text
ENGAGEMENT
   ↓
PURPOSE
   ↓
PARTICIPANTS
   ↓
DISCUSSION / OBSERVATION
   ↓
CONCERNS / OPPORTUNITIES
   ↓
CAPTURE
   ↓
LINK TO ISSUE / PERSON / ORGANISATION
   ↓
ACTION OR MONITOR
```

Engagement boleh menghasilkan:
- case;
- concern;
- issue;
- stakeholder commitment;
- programme requirement;
- intelligence;
- no-action record.

---

# 10. INFORMAL / SOCIAL CONTACT LOGIC

Interaksi santai boleh direkodkan secara **lightweight** apabila mempunyai nilai operasi atau intelligence.

`Contact → Quick Note → Tag → Location → Theme → Link if necessary → Monitor / Convert to Structured Record`

Tidak semua percakapan perlu direkod secara terperinci.

Prinsip: **capture signal without manufacturing bureaucracy.**

---

# 11. FIELD VISIT LOGIC

```text
FIELD VISIT
   ↓
PURPOSE / LOCATION
   ↓
OBSERVE
   ↓
PHOTOS / EVIDENCE WHERE APPROPRIATE
   ↓
CAPTURE OBSERVATION
   ↓
CLASSIFY
   ↓
LINK CASE / ISSUE
   ↓
ACTION / REFERRAL / MONITOR
   ↓
OUTCOME
```

Field observation yang berulang boleh menjadi input kepada Constituency Intelligence.

---

# 12. MEETING LOGIC

Setiap meeting yang mempunyai nilai operasi hendaklah menghasilkan action record.

`Meeting → Agenda → Participants → Issues → Decisions → Action Items → Owner → Deadline → Follow-up → Closure`

Meeting tanpa action boleh direkod sebagai **information/engagement**, bukan dipaksa menjadi action meeting.

---

# 13. CONCERN / ISSUE LOGIC

Concern ialah signal. Issue ialah pattern/masalah yang sudah cukup jelas untuk diurus sebagai isu kawasan.

```text
SIGNALS
  ↓
CONCERNS
  ↓
REPEATED / MATERIAL PATTERN
  ↓
CONSTITUENCY ISSUE
  ↓
ANALYSIS
  ↓
INTERVENTION
  ↓
OUTCOME
```

Contoh:

`1 concern tentang banjir → observation → 8 concerns → recurring pattern → ISSUE: flood hotspot`

---

# 14. CONSTITUENCY INTELLIGENCE LOGIC

```text
MULTIPLE RECORDS
      ↓
DATA CLEANING / LINKING
      ↓
PATTERN DETECTION
      ↓
ISSUE FORMATION
      ↓
CONTEXT / CAUSE ANALYSIS
      ↓
PRIORITY
      ↓
RECOMMENDATION
      ↓
DECISION / INTERVENTION
      ↓
OUTCOME
      ↓
LEARNING
```

Intelligence bukan profiling partisan. Ia adalah pemahaman tentang keadaan constituency untuk membantu service delivery, policy dan strategic decision-making.

---

# 15. YB ESCALATION LOGIC

YB tidak perlu menerima semua urusan.

### Level 0 — Routine

Diselesaikan oleh pegawai mengikut mandat.

### Level 1 — Management

Memerlukan keputusan/koordinasi Ketua Pejabat.

### Level 2 — Strategic

Memerlukan keputusan YB kerana:
- impak besar;
- cross-agency;
- high visibility;
- sensitive;
- recurring systemic issue;
- resource/policy implication.

### Level 3 — Political / Policy

Memerlukan judgement politik, representasi kerajaan atau tindakan legislatif/polisi.

```text
RECORD
 ↓
TRIAGE
 ↓
THRESHOLD
 ├─ Routine → Staff
 ├─ Management → Chief of Staff
 ├─ Strategic → YB
 └─ Political/Policy → YB + Policy Support
```

---

# 16. CRISIS / INCIDENT LOGIC

Crisis tidak mengikuti workflow rutin.

```text
DETECT
 ↓
VERIFY
 ↓
CLASSIFY SEVERITY
 ↓
ACTIVATE RESPONSE
 ↓
COORDINATE AGENCIES
 ↓
PUBLIC COMMUNICATION IF REQUIRED
 ↓
MONITOR
 ↓
RECOVERY
 ↓
POST-INCIDENT REVIEW
 ↓
LEARNING / SYSTEM UPDATE
```

---

# 17. PROGRAMME / ACTIVITY LOGIC

Program pejabat direkod sebagai operational activity apabila berkaitan dengan skop pejabat.

`Need / Objective → Design → Approval → Resources → Delivery → Attendance / Participation → Outputs → Outcomes → Documentation → Review`

Program tidak boleh menjadi “closed” hanya kerana acara telah berlangsung jika masih ada commitment atau follow-up.

---

# 18. COMMUNICATION LOGIC

```text
OFFICE ACTION / VERIFIED INFORMATION
            ↓
MESSAGE PURPOSE
            ↓
APPROVAL / ACCURACY CHECK
            ↓
PUBLISH / RESPOND
            ↓
PUBLIC REACTION / FEEDBACK
            ↓
CAPTURE SIGNALS
```

Media communication ialah satu lagi input kepada intelligence, tetapi tidak menggantikan field evidence atau official records.

---

# 19. CORPORATE OPERATING LOGIC

Untuk operasi dalaman:

`Requirement → Request → Approval → Procurement / Action → Record → Reconciliation → Archive`

Merangkumi:
- HR;
- finance;
- procurement;
- asset;
- records;
- logistics;
- compliance.

---

# 20. CROSS-RECORD LINKING LOGIC

Setiap jenis rekod boleh berkait dengan rekod lain.

```text
PERSON
  ↕
ORGANISATION
  ↕
LOCATION
  ↕
CASE / REQUEST / CONCERN / ENGAGEMENT / FIELD / MEETING
  ↕
ISSUE
  ↕
ACTION
  ↕
AGENCY
  ↕
OUTCOME
```

### Rule

**No unnecessary duplicate record. Link existing entities whenever possible.**

---

# 21. UNIVERSAL STATUS LOGIC

Semua record utama perlu mempunyai status yang difahami bersama.

Cadangan master states:

`NEW → TRIAGED → ASSIGNED → IN PROGRESS → PENDING → ESCALATED → RESOLVED → CLOSED`

Tidak semua jenis rekod memerlukan semua state. Model khusus boleh menggunakan subset.

---

# 22. OWNERSHIP LOGIC

Setiap actionable record mesti mempunyai:

- **Owner** — siapa melakukan kerja;
- **Accountable authority** — siapa bertanggungjawab memastikan ia bergerak;
- **Deadline** jika perlu;
- **Escalation path**;
- **Outcome owner**.

Ini menghapuskan keadaan “semua orang tahu isu tetapi tiada siapa memilikinya”.

---

# 23. CLOSURE LOGIC

Sesuatu rekod hanya boleh ditutup apabila terdapat keadaan closure yang munasabah.

Contoh closure:
- resolved;
- fulfilled;
- referred and no further office action required;
- applicant withdrew;
- duplicate;
- outside scope with documented referral;
- no actionable information after reasonable verification;
- monitoring completed.

Closure reason wajib direkodkan.

---

# 24. NO-ACTION LOGIC

Tidak semua interaction memerlukan intervention.

`Capture → Assess → No Action Required → Reason → Monitor/Archive`

“No Action” bukan bermaksud data dibuang. Ia masih menjadi institutional record jika mempunyai nilai operasi.

---

# 25. FEEDBACK LOOP

Setiap outcome boleh menjadi input kepada sistem.

```text
OUTCOME
  ↓
WAS IT EFFECTIVE?
  ↓
YES → Standardise / Close
NO  → Reassess / Escalate / Redesign
  ↓
UPDATE KNOWLEDGE
  ↓
IMPROVE WORKFLOW
```

---

# 26. OPERATING RHYTHM

### Daily
- urgent cases;
- critical incidents;
- overdue exceptions;
- immediate YB matters.

### Weekly
- new cases;
- backlog;
- applications;
- referrals;
- actions;
- upcoming engagements.

### Monthly
- workload;
- agency response;
- assistance/request patterns;
- recurring issues;
- operational bottlenecks.

### Quarterly
- constituency issue map;
- strategic priorities;
- systemic problems;
- programme/outcome review;
- manpower/capacity.

### Annual
- constituency state review;
- architecture review;
- policy priorities;
- institutional memory/handover review.

---

# 27. CORE OPERATING LOGIC MATRIX

| Logic | Trigger | Primary Output | Main Owner | External Interface |
|---|---|---|---|---|
| Citizen Intake | Interaction received | Structured record | Front/Case Officer | — |
| Case Management | Problem requiring action | Case outcome | Case Owner | Agency if needed |
| Application | Request submitted | Decision + fulfilment/referral | Request Officer | Supplier/Agency |
| Goods Assistance | Goods requested | Delivered/declined | Request + Corporate | Supplier/Agency |
| Referral | Outside office authority | Agency response | Government Liaison | Agency |
| Coordination | Multi-party issue | Action matrix | Government Liaison/CoS | District/Agencies |
| Community Engagement | Meeting/contact | Concerns/commitments | Community Officer | Community |
| Informal Contact | Social/field interaction | Signal/observation | Any staff | Community |
| Field Visit | Physical observation | Field record/action | Field owner | Agency/community |
| Meeting | Formal discussion | Decisions/actions | Meeting owner | Stakeholders |
| Concern/Issue | Repeated signal | Issue record | Intelligence | Relevant stakeholders |
| Policy/Legislative | Strategic issue | Brief/action | Policy Officer | Legislature/Government |
| YB Escalation | Threshold met | Strategic decision | CoS → YB | Relevant authority |
| Crisis | Incident | Coordinated response | Crisis lead | Emergency/Agencies |
| Programme | Planned activity | Output/outcome | Programme owner | Partners |
| Communication | Action/info | Public information | Comms | Media/Public |
| Corporate | Internal need | Controlled operation | Corporate | Vendors/authorities |

---

# 28. DESIGN RULES

1. **One interaction, one primary record.** Link rather than duplicate.
2. **Capture at source.** The person receiving the information records the minimum viable data.
3. **Classify early.** Wrong routing creates delay.
4. **Owner every action.** No orphan tasks.
5. **Track exceptions, not everything equally.** Attention follows risk and priority.
6. **Outcome beats activity.** A completed event is not automatically a solved problem.
7. **YB is an escalation layer, not a helpdesk.**
8. **Agency referral must remain traceable.**
9. **Informal intelligence is captured lightly.**
10. **Data must support service, not partisan profiling.**
11. **System must survive staff turnover.**
12. **Every recurring problem should be capable of becoming an Issue.**

---

# 29. NEXT DESIGN DEPENDENCIES

This Operating Logic Map becomes the input for:

1. Real-Life Constituency Service Journey Map
2. Organizational Architecture refinement
3. Manpower/workload model
4. Detailed workflows and SOPs
5. Data Model / Database Schema
6. Role & permission model
7. KPI and performance framework
8. Dashboard architecture
9. Training/capability framework

---

**Document control**

Version: V1.0  
System: SZ-COS — Constituency Operating System  
Layer: Operating Logic  
Parent: Governance Foundation V1.0  
Scope: Pejabat Wakil Rakyat — DUN / Parlimen

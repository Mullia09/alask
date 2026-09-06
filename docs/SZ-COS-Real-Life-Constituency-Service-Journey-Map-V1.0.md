# SZ-COS — Real-Life Constituency Service Journey Map V1.0

**System:** SZ-COS — Constituency Operating System  
**Scope:** Pejabat Wakil Rakyat — DUN / Parlimen  
**Status:** Journey Architecture Draft V1.0  
**Purpose:** Memetakan perjalanan sebenar urusan antara rakyat/organisasi, Pejabat YB, jabatan/agensi kerajaan dan outcome, dengan satu rekod data yang menghubungkan keseluruhan perjalanan.

---

## 1. Design Premise

Pejabat YB berfungsi sebagai **constituency service institution**, bukan pengganti jabatan/agensi kerajaan.

Journey Map ini berasaskan prinsip:

> **Capture Once → Classify Correctly → Route to the Right Owner → Track the Journey → Escalate When Necessary → Record Outcome → Learn.**

Semua urusan substantif yang melalui Pejabat YB menghasilkan rekod dalam **Constituency Master Database** mengikut jenis interaksi yang sesuai.

---

## 2. Universal Journey

```text
REAL-WORLD INTERACTION
        ↓
CAPTURE
        ↓
IDENTIFY PERSON / ORGANISATION / LOCATION
        ↓
CLASSIFY RECORD
        ↓
ASSESS
        ↓
ASSIGN OWNER
        ↓
ACTION / REFERRAL / COORDINATION / NO ACTION
        ↓
FOLLOW-UP
        ↓
ESCALATE WHEN REQUIRED
        ↓
OUTCOME
        ↓
CLOSE / KEEP OPEN FOR MONITORING
        ↓
LEARNING / INTELLIGENCE
```

Tidak semua journey menggunakan semua langkah. Tetapi setiap journey mesti mempunyai **minimum viable record** dan status yang boleh dijejaki.

---

## 3. Entry Points

Urusan boleh bermula melalui:

- kaunter / walk-in;
- telefon;
- WhatsApp / digital channel rasmi;
- surat / dokumen;
- program atau aktiviti pejabat;
- lawatan/turun padang;
- pertemuan komuniti;
- engagement tidak rasmi yang menghasilkan concern substantif;
- rujukan daripada organisasi atau pihak lain;
- mesyuarat dengan jabatan/agensi.

**Rule:** Channel bukan rekod utama. Semua channel perlu dinormalisasikan ke dalam satu sistem rekod.

---

## 4. Journey A — Individual Case

Contoh: isu bantuan kebajikan, dokumen, pekerjaan atau masalah perkhidmatan.

```text
INDIVIDU
  ↓
INTAKE
  ↓
CASE CREATED
  ↓
VERIFY FACTS / DOCUMENTS
  ↓
CLASSIFY
  ↓
ASSIGN CASE OWNER
  ↓
OFFICE ACTION OR AGENCY REFERRAL
  ↓
FOLLOW-UP
  ↓
OUTCOME
  ↓
CLOSE
```

### Decision Points

1. Boleh diselesaikan terus oleh pejabat?
2. Perlu rujukan agensi?
3. Perlu koordinasi rentas agensi?
4. Perlu keputusan YB?
5. Adakah isu ini sebenarnya sebahagian daripada recurring issue?

---

## 5. Journey B — Assistance / Goods Request

Bagi individu atau organisasi seperti peniaga, masjid, surau, kuil, gereja, NGO, persatuan dan institusi komuniti:

```text
APPLICANT
   ↓
APPLICATION / REQUEST
   ↓
VERIFY APPLICANT
   ↓
VERIFY PURPOSE / NEED
   ↓
ASSESS ELIGIBILITY / PRIORITY
   ↓
RECOMMENDATION
   ↓
DECISION
   ├── APPROVED → FULFILMENT
   │                 ↓
   │             PROOF OF RECEIPT
   │                 ↓
   │               CLOSE
   │
   └── NOT APPROVED → RECORD REASON
                       ↓
                  REFERRAL / ALTERNATIVE
                       ↓
                     CLOSE
```

### Minimum Data

- applicant/person;
- organisation, if relevant;
- request category;
- item/service requested;
- quantity;
- purpose;
- location;
- previous related request;
- assessment;
- decision;
- fulfilment details;
- acknowledgement/proof of receipt;
- outcome.

**Person ≠ Organisation.** A person may represent an organisation; the organisational record remains independently traceable.

---

## 6. Journey C — Government Referral

```text
CASE / ISSUE
    ↓
AUTHORITY CLASSIFICATION
    ↓
RIGHT AGENCY
    ↓
FORMAL REFERRAL
    ↓
AGENCY RESPONSE
    ↓
FOLLOW-UP
    ↓
RESOLUTION?
 ┌──YES──────────────┐
 ↓                   │
OUTCOME              │
 ↓                   │
CLOSE                 │
                     │
NO                    │
 ↓                    │
ESCALATE / COORDINATE
 ↓
OUTCOME
 ↓
CLOSE / MONITOR
```

Pejabat YB tidak mengambil alih bidang kuasa agensi. Peranan utama ialah **routing, tracking, coordination dan escalation**.

---

## 7. Journey D — District / Multi-Agency Coordination

Untuk isu seperti banjir, infrastruktur, pembangunan atau masalah rentas agensi:

```text
ISSUE DETECTED
      ↓
INITIAL ASSESSMENT
      ↓
IDENTIFY MULTIPLE ACTORS
      ↓
COORDINATION BRIEF
      ↓
DISTRICT / LEAD AGENCY / RELEVANT AGENCIES
      ↓
ACTION PLAN
      ↓
ACTION TRACKING
      ↓
STATUS REVIEW
      ↓
OUTCOME
```

### Coordination Record

Mesti menyimpan:

- issue ID;
- agencies involved;
- lead agency;
- action items;
- PIC;
- target date;
- decisions;
- dependencies;
- status;
- outcome.

---

## 8. Journey E — Community Concern / Emerging Issue

Tidak semua isu datang sebagai aduan formal.

Contoh: concern yang muncul semasa perbualan komuniti atau engagement.

```text
CONVERSATION / ENGAGEMENT
        ↓
QUICK CAPTURE
        ↓
TAG CONCERN
        ↓
RECORD IN DATABASE
        ↓
WATCH FOR RECURRENCE
        ↓
PATTERN DETECTED?
   ├── NO → MONITOR
   └── YES
         ↓
   CONSTITUENCY ISSUE
         ↓
      ANALYSIS
         ↓
   INTERVENTION / POLICY
```

Prinsipnya: **informal tidak bermaksud tidak bernilai.** Tetapi capture mesti minimum dan berfokus kepada maklumat operasi, bukan rekod politik peribadi.

---

## 9. Journey F — Field Visit / Down to Ground

```text
FIELD VISIT
    ↓
OBSERVATION CAPTURE
    ↓
LOCATION + EVIDENCE
    ↓
CLASSIFY
    ↓
LINK TO EXISTING CASE / ISSUE
       OR
CREATE NEW RECORD
    ↓
ACTION / REFERRAL / MONITOR
    ↓
OUTCOME
```

Lawatan lapangan tidak boleh berakhir pada gambar dan laporan sahaja. Penemuan substantif mesti disambungkan kepada rekod operasi.

---

## 10. Journey G — Meeting / Community / Agency Engagement

```text
MEETING / ENGAGEMENT
        ↓
AGENDA / PURPOSE
        ↓
DISCUSSION
        ↓
ISSUES IDENTIFIED
        ↓
COMMITMENTS / ACTION ITEMS
        ↓
ASSIGN OWNER
        ↓
TRACK
        ↓
OUTCOME
```

Meeting record boleh menghasilkan beberapa linked records:

**Meeting → Issue → Action → Agency → Outcome**

---

## 11. Journey H — Programme / Activity

```text
NEED / OBJECTIVE
      ↓
PROGRAMME DESIGN
      ↓
APPROVAL
      ↓
DELIVERY
      ↓
PARTICIPATION / REACH
      ↓
DOCUMENTATION
      ↓
OUTCOME / FEEDBACK
      ↓
DATABASE
```

Program yang hanya selesai dari sudut logistik tetapi tidak mempunyai outcome atau feedback dianggap **operationally incomplete**.

---

## 12. Journey I — Escalation to YB

YB bukan approval point untuk semua urusan.

```text
STAFF / UNIT
   ↓
ASSESSMENT
   ↓
THRESHOLD CHECK
   ├── ROUTINE → UNIT HANDLE
   ├── COORDINATION → CHIEF OF STAFF / RELEVANT LEAD
   └── STRATEGIC / POLITICAL / POLICY → YB
                                      ↓
                                   DECISION
                                      ↓
                                  EXECUTION
                                      ↓
                                   OUTCOME
```

### Typical YB Escalation Triggers

- impak kawasan tinggi;
- isu berulang dan struktural;
- memerlukan keputusan strategik;
- memerlukan political representation;
- melibatkan policy/legislative issue;
- reputational atau crisis risk yang material;
- perkara yang melepasi delegated authority.

---

## 13. Journey J — No Action / Monitor

Tidak semua perkara perlu tindakan segera.

```text
INTAKE
 ↓
ASSESSMENT
 ↓
NO IMMEDIATE ACTION
 ↓
REASON RECORDED
 ↓
MONITOR / WATCH
 ↓
TRIGGER OCCURS?
 ├── NO → ARCHIVE / MONITOR
 └── YES → REOPEN / ESCALATE
```

Ini penting untuk mengelakkan pejabat mencipta kerja hanya untuk menunjukkan aktiviti.

---

## 14. Common Status Model

Status standard merentasi journey:

**NEW → TRIAGED → ASSIGNED → IN PROGRESS → WAITING FOR APPLICANT → WAITING FOR AGENCY → ESCALATED → RESOLVED → CLOSED → MONITORING / REOPENED**

Status boleh disesuaikan mengikut record type, tetapi istilah teras perlu distandardkan.

---

## 15. Common Ownership Model

Setiap record mesti mempunyai:

**Record Owner** — pegawai/unit yang bertanggungjawab menggerakkan rekod.

**Decision Authority** — siapa yang mempunyai kuasa membuat keputusan tertentu.

**External Owner** — agensi/pihak luar yang mempunyai bidang kuasa penyelesaian.

**Escalation Owner** — siapa yang menerima perkara apabila threshold dicapai.

---

## 16. Single Master Record Principle

Satu interaksi boleh menghasilkan banyak aktiviti, tetapi **tidak boleh menghasilkan rekod yang terpisah tanpa link**.

Contoh:

```text
CASE-00124
   │
   ├── FIELD-0042
   ├── REFERRAL-0037
   ├── MEETING-0019
   ├── ACTION-0081
   └── OUTCOME-0055
```

Semua sejarah boleh ditelusuri melalui satu relationship chain.

---

## 17. Person–Organisation–Issue Relationship

```text
PERSON
  │
  ├── REPRESENTS → ORGANISATION
  │
  ├── SUBMITS → APPLICATION
  │
  ├── RAISES → CASE / CONCERN
  │
  └── PARTICIPATES → ENGAGEMENT

ORGANISATION
  │
  ├── HAS → REQUESTS
  ├── EXPERIENCES → ISSUES
  └── PARTICIPATES → MEETINGS / PROGRAMMES

ISSUE
  │
  ├── LINKS → CASES
  ├── LINKS → FIELD VISITS
  ├── LINKS → MEETINGS
  └── LINKS → POLICY / ACTION
```

---

## 18. Universal Closing Rule

Sesuatu urusan tidak dianggap selesai hanya kerana:

- surat telah dihantar;
- WhatsApp telah dihantar;
- agensi telah dihubungi;
- YB telah turun padang;
- program telah dijalankan.

Ia hanya mencapai **CLOSED** apabila outcome atau reason for closure direkodkan mengikut jenis record.

---

## 19. Intelligence Feedback Loop

Selepas closure, rekod tidak semestinya "mati".

```text
CLOSED RECORD
      ↓
PATTERN ANALYSIS
      ↓
RECURRING ISSUE?
 ├── NO → RETAIN AS HISTORY
 └── YES
      ↓
CONSTITUENCY ISSUE
      ↓
POLICY / SERVICE DESIGN
      ↓
INTERVENTION
      ↓
NEW OUTCOME
      ↓
DATABASE
```

Ini menjadikan pejabat sebuah **learning institution**, bukan hanya transaction office.

---

## 20. Real-Life Master Journey

```text
                         RAKYAT / ORGANISASI
                                  │
                ┌─────────────────┼─────────────────┐
                │                 │                 │
             REQUEST           CASE             CONCERN
                │                 │                 │
                └─────────────────┼─────────────────┘
                                  ↓
                              CAPTURE
                                  ↓
                          MASTER DATABASE
                                  ↓
                           CLASSIFICATION
                                  ↓
                     ┌────────────┼────────────┐
                     │            │            │
                  OFFICE       AGENCY       COMMUNITY
                   ACTION      REFERRAL      ENGAGE
                     │            │            │
                     └────────────┼────────────┘
                                  ↓
                         COORDINATION / ACTION
                                  ↓
                              ESCALATION
                                  ↓
                                  YB
                                  ↓
                               DECISION
                                  ↓
                              EXECUTION
                                  ↓
                               OUTCOME
                                  ↓
                              DATABASE
                                  ↓
                              LEARNING
                                  ↓
                         FUTURE INTERVENTION
```

---

## 21. Design Rule for Future SZ-COS Layers

Semua pembangunan selepas Journey Map ini mesti boleh menjawab lima soalan:

1. **Bagaimana urusan masuk?**
2. **Siapa memilikinya?**
3. **Apa decision point?**
4. **Bagaimana status/outcome dijejak?**
5. **Bagaimana data itu digunakan semula tanpa mengulangi capture?**

Jika suatu proses tidak mampu menjawab kelima-lima soalan ini, proses tersebut perlu direka semula sebelum dijadikan SOP atau sistem.

---

## 22. Relationship to SZ-COS Governance Foundation

Journey Map ini melaksanakan prinsip Foundation V1.0 khususnya:

- Single Source of Truth;
- One Office, One Record;
- Right Issue, Right Channel;
- YB Leads, Office Operates;
- Evidence Before Escalation;
- Traceability;
- Closure Matters;
- Learning Institution;
- Data Minimisation & Protection.

---

**Document control**  
Version: V1.0  
Status: Journey Architecture Draft  
System: SZ-COS — Constituency Operating System  
Scope: Pejabat Wakil Rakyat — DUN / Parlimen

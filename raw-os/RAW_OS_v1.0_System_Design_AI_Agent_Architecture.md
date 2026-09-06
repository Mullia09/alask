# RAW OS v1.0 — System Design Specification
## 5. AI / Agent Architecture

**Status:** System Design Specification — Foundational Draft  
**Depends on:** RAW OS v0.1–v0.8 + v1.0 API, Algorithm, Database, Event & State Architecture

## 1. Tujuan

AI / Agent Architecture mentakrifkan bagaimana AI dan autonomous agents menjadi sebahagian daripada RAW OS tanpa mengambil alih governance constitution. AI boleh bertindak sebagai advisor, decision-support component, monitor atau delegated execution agent, tetapi setiap capability, authority, tool access, action dan escalation mesti explicit, bounded dan auditable.

## 2. Core Principle

> AI capability does not imply AI authority.

Architecture principle:

`MODEL → AGENT → CAPABILITY → AUTHORITY → POLICY → TOOL ACCESS → ACTION → EVIDENCE`

AI ialah implementation component. RAW OS governance, ontology, decision logic dan control logic kekal sebagai sumber kuasa normative.

## 3. AI Roles

### 3.1 AI as Advisor
AI menghasilkan analysis, recommendation atau draft. Human membuat keputusan.

### 3.2 AI as Decision Support
AI menjalankan assessment dalam defined scope tetapi tidak mempunyai final authority.

### 3.3 AI as Monitor
AI mengesan anomaly, threshold breach, pattern atau risk signal.

### 3.4 AI as Agent
AI boleh merancang dan melaksanakan actions menggunakan delegated authority dan approved tools.

### 3.5 AI as Orchestrator
AI menyelaras tools, services atau agents dalam workflow yang telah ditakrifkan.

## 4. Separation of Concerns

RAW OS membezakan:

- **Model** — engine yang menghasilkan inference/generation.
- **Agent** — runtime entity yang mempunyai role, state, objective dan tool context.
- **Capability** — apa yang agent secara teknikal boleh lakukan.
- **Authority** — apa yang agent dibenarkan lakukan.
- **Policy** — rules yang mengikat behaviour.
- **Tool** — interface kepada external action.
- **Control** — mekanisme pencegahan, pengesanan atau intervention.

`MODEL ≠ AGENT ≠ CAPABILITY ≠ AUTHORITY`

## 5. Agent Identity

Setiap persistent atau action-capable agent mesti mempunyai identity yang boleh dijejaki.

Minimum:

- Agent ID
- Agent type
- Model reference
- Version
- Owner
- Role
- Environment
- Status
- Authority profile
- Capability profile
- Policy profile

Identity mengenal pasti agent; ia tidak memberi authority secara automatik.

## 6. Agent Lifecycle

`REGISTER → CONFIGURE → VALIDATE → AUTHORISE → ACTIVATE → OPERATE → MONITOR → REVIEW → SUSPEND / RETIRE`

Agent yang belum lulus validation atau authorisation tidak boleh mempunyai execution authority production.

## 7. Goal & Task Model

Agent task mesti boleh dipetakan kepada purpose dan scope.

`SYSTEM PURPOSE → AGENT OBJECTIVE → TASK → SUBTASK → ACTION`

Setiap task sekurang-kurangnya mempunyai:

- Task ID
- Requester
- Objective
- Scope
- Constraints
- Risk class
- Authority context
- Deadline / TTL apabila relevan
- Required evidence
- Completion criteria

## 8. Planning Boundary

Agent boleh menghasilkan plan, tetapi plan tidak secara automatik menjadi authority untuk execution.

`GOAL → PLAN → VALIDATE → AUTHORISE → EXECUTE`

Plan yang melibatkan high-impact action perlu melalui applicable governance gate sebelum execution.

## 9. Tool Access Architecture

Tools ialah titik yang menghubungkan AI kepada dunia luar.

`AGENT → TOOL POLICY → PERMISSION CHECK → TOOL → EXTERNAL SYSTEM`

Setiap tool mesti mempunyai:

- Tool ID
- Description
- Input schema
- Output schema
- Required permissions
- Risk class
- Side-effect class
- Authentication method
- Audit requirements
- Timeout / retry policy

## 10. Tool Permission Classes

### 10.1 Read
Membaca data tanpa side effect.

### 10.2 Analyse
Memproses data tanpa external mutation.

### 10.3 Write
Mengubah data atau state.

### 10.4 Execute
Menyebabkan external action.

### 10.5 Privileged Execute
High-impact execution yang memerlukan elevated authority atau human approval.

## 11. Least-Privilege Model

Agent hanya menerima capabilities dan tools yang diperlukan untuk task.

`MINIMUM CAPABILITY → MINIMUM AUTHORITY → MINIMUM TOOL ACCESS`

Authority mesti boleh dihadkan mengikut:

- resource
- operation
- scope
- value
- time
- environment
- condition

## 12. Agent Decision Loop

`OBSERVE → CONTEXTUALISE → ASSESS → PLAN → POLICY CHECK → AUTHORITY CHECK → RISK CHECK → CONTROL CHECK → ACT → OBSERVE RESULT`

Loop boleh diulang hanya dalam batas task, budget, time dan authority yang ditentukan.

## 13. Model / Agent Uncertainty

Uncertainty perlu menjadi input kepada control logic.

`LOW CONFIDENCE / HIGH UNCERTAINTY → REVIEW / ESCALATE`

Confidence sahaja tidak boleh digunakan sebagai bukti bahawa decision itu benar atau authorised. Confidence ialah signal; evidence dan governance tetap diperlukan.

## 14. Human Oversight Modes

### 14.1 Human-in-the-Loop
Human perlu approve sebelum significant action.

### 14.2 Human-on-the-Loop
Agent bertindak dalam boundary; human memonitor dan boleh intervene.

### 14.3 Human-out-of-the-Loop
Fully automated execution hanya dalam tightly constrained, low-risk atau explicitly approved domain.

Human oversight level hendaklah dipengaruhi oleh impact, risk, uncertainty, reversibility dan authority level.

## 15. Escalation Triggers

Agent mesti berhenti, hold atau escalate apabila berlaku:

- authority insufficient
- rule conflict
- boundary breach
- high / critical risk
- low confidence pada critical decision
- missing evidence
- control failure
- tool anomaly
- unexpected state
- prompt / instruction conflict
- policy violation

## 16. Prompt & Instruction Governance

Instructions kepada agent perlu mempunyai hierarchy dan precedence.

Cadangan precedence:

`SYSTEM GOVERNANCE → POLICY → TASK AUTHORITY → USER / OPERATOR REQUEST → OPTIONAL CONTEXT`

Instruction yang bercanggah dengan higher-level governance tidak boleh mengatasi governance hanya kerana datang kemudian dalam conversation atau workflow.

## 17. Context Architecture

Agent context hendaklah dipisahkan kepada:

- System context
- Governance context
- Identity context
- Task context
- Tool context
- Data context
- Conversation / interaction context
- Temporary working state

Sensitive atau unnecessary context tidak patut diberikan melebihi purpose dan authority yang diperlukan.

## 18. Memory Architecture

Jenis memory:

### 18.1 Working Memory
State sementara bagi current task.

### 18.2 Episodic Memory
Records interaction atau event tertentu.

### 18.3 Semantic Memory
Knowledge yang distrukturkan untuk retrieval.

### 18.4 Governance Memory
Policies, rules, decisions, exceptions dan authority versions yang relevan.

Memory retrieval tidak mengatasi authority atau policy controls.

## 19. Multi-Agent Architecture

Apabila lebih daripada satu agent digunakan:

`ORCHESTRATOR → SPECIALIST AGENTS → VALIDATION / CONTROL → ACTION`

Setiap agent mesti mempunyai identity, role dan authority sendiri.

Agent-to-agent communication perlu mempunyai:

- sender identity
- receiver identity
- message type
- correlation ID
- authority context
- provenance
- timestamp

## 20. Agent-to-Agent Authority

Agent A tidak boleh mewariskan authority kepada Agent B secara implicit.

`AGENT A AUTHORITY → DELEGATION CHECK → AGENT B AUTHORITY → LIMITED EXECUTION`

Delegation mesti mempunyai scope, constraints, expiry dan evidence apabila relevan.

## 21. Guardrail Architecture

Guardrails hendaklah berlapis:

1. Input guardrail
2. Context guardrail
3. Policy guardrail
4. Authority guardrail
5. Tool guardrail
6. Action guardrail
7. Output guardrail
8. Monitoring guardrail

Tiada satu guardrail patut dianggap sebagai single point of safety untuk high-risk systems.

## 22. Sandboxing & Environment Separation

AI execution hendaklah membezakan environment:

`SIMULATION / SANDBOX → TEST → STAGING → PRODUCTION`

Capabilities dan authorities perlu berubah mengikut environment. Production authority tidak boleh muncul secara lalai dalam sandbox atau development context.

## 23. Transaction & Action Safety

Untuk tool/action yang mempunyai side effects:

`PREVIEW → VALIDATE → AUTHORISE → EXECUTE → VERIFY → RECORD`

Reversible operations diutamakan apabila sesuai. High-impact irreversible actions memerlukan stronger controls.

## 24. Budget & Resource Controls

Agent runtime mesti boleh dihadkan melalui:

- token / compute budget
- tool-call budget
- financial budget
- execution time
- task count
- API rate
- external action count

`BUDGET EXCEEDED → HOLD / STOP / ESCALATE`

## 25. Action Classification

### Low Impact
Boleh auto-execute dalam defined boundary.

### Moderate Impact
Enhanced control atau monitoring.

### High Impact
Human approval atau higher authority.

### Critical Impact
Default stop / prohibited kecuali governance secara jelas membenarkan exceptional path.

## 26. Safety & Failure Handling

`ANOMALY → CONTAIN → FREEZE / ROLLBACK → ASSESS → ESCALATE → RECOVER → RECORD → REVIEW`

Agent tidak boleh terus meningkatkan privilege sebagai response kepada failure tanpa explicit governance path.

## 27. Output Provenance

Critical AI outputs perlu menyimpan provenance yang mencukupi:

- Agent ID
- Model/version
- Task ID
- Input references
- Context version
- Tools used
- Decision / policy references
- Timestamp
- Output
- Human approval apabila ada

## 28. AI Evaluation Requirements

Sebelum production, agent perlu dinilai terhadap:

- instruction adherence
- policy adherence
- authority adherence
- tool-use safety
- hallucination / factual reliability
- uncertainty handling
- escalation behaviour
- refusal behaviour
- boundary adherence
- robustness to adversarial inputs
- reproducibility / traceability apabila diperlukan

## 29. Adversarial & Red-Team Interface

Agent architecture mesti menyediakan ruang untuk testing terhadap:

- prompt injection
- instruction conflict
- data poisoning
- tool misuse
- privilege escalation attempts
- unsafe autonomy
- context manipulation
- malicious external inputs
- unexpected tool responses

Red-team result menjadi input kepada risk, control dan adaptation layers.

## 30. Observability

Minimum telemetry:

`AGENT → TASK → DECISION → TOOL CALL → ACTION → OUTCOME → ERROR → ESCALATION`

Observability mesti boleh dihubungkan melalui correlation ID dan evidence references.

## 31. Auditability

Setiap significant agent action mesti boleh dijawab:

- Agent siapa?
- Model/version apa?
- Task apa?
- Authority apa?
- Rule apa?
- Tool apa?
- Input apa?
- Decision apa?
- Action apa?
- Outcome apa?
- Siapa approve jika diperlukan?

## 32. Agent Configuration Versioning

Versioned objects sekurang-kurangnya:

- Agent version
- Model version
- System prompt / policy reference
- Tool permissions
- Authority profile
- Risk profile
- Guardrail configuration
- Evaluation version

Perubahan material memerlukan regression evaluation sebelum deployment.

## 33. AI Governance Gate

`REGISTER → RISK CLASSIFY → DEFINE CAPABILITY → DEFINE AUTHORITY → CONFIGURE CONTROLS → TEST → APPROVE → DEPLOY → MONITOR → REVIEW`

## 34. AI Agent Contract

Minimum machine-readable contract secara konseptual:

`AgentIdentity + Role + Capability + Authority + Policy + ToolSet + RiskClass + Limits + OversightMode + EvidencePolicy`

## 35. Example Agent Decision Contract

```text
REQUEST
  ↓
IDENTIFY AGENT
  ↓
CHECK TASK SCOPE
  ↓
CHECK CAPABILITY
  ↓
CHECK AUTHORITY
  ↓
APPLY POLICY
  ↓
ASSESS RISK + UNCERTAINTY
  ↓
SELECT OVERSIGHT LEVEL
  ↓
ALLOW / LIMIT / ESCALATE / REJECT
  ↓
EXECUTE TOOL (IF AUTHORISED)
  ↓
VERIFY RESULT
  ↓
RECORD EVIDENCE
```

## 36. AI / Agent Invariants

1. AI capability never implies authority.
2. Agent identity must be attributable.
3. Significant actions require traceable authority.
4. Tool access must be explicitly governed.
5. High-impact actions require stronger control and oversight.
6. Agent delegation must be bounded and revocable.
7. Failure must not silently expand privilege.
8. Critical actions require evidence.
9. Governance takes precedence over local instructions.
10. Material changes require evaluation and versioning.

## 37. Integration with Existing RAW OS Architecture

`AI / AGENT → API → ALGORITHM → GOVERNANCE → DATABASE / EVENT-STATE → EXTERNAL SYSTEM`

Dengan event/state architecture, setiap meaningful transition agent boleh direkod, direplay, diaudit dan direconcile.

Dengan algorithm architecture, decision logic boleh diuji secara berasingan daripada model.

Dengan governance framework, model tidak boleh mengubah authority secara implicit.

## 38. Boundary of AI / Agent Architecture

Dokumen ini belum memilih vendor model, cloud provider, agent framework, vector database atau specific runtime. Pemilihan technology hanya dibuat pada implementation layer berdasarkan requirements dan constraints RAW OS.

## 39. Next Component

**RAW OS v1.0 — 6. UI / UX Architecture** boleh menentukan bagaimana manusia melihat state, decisions, risks, controls, evidence dan AI activity tanpa menjadikan UI sebagai sumber authority.

## 40. Status

- Version: RAW OS v1.0
- Component: 5. AI / Agent Architecture
- Status: System Design Specification — Foundational Draft
- Design principle: Governed autonomy, explicit authority, bounded capability, layered controls, human oversight, traceability and adaptability.

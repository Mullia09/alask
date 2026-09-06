# RAW OS v1.0 — System Design Specification
## 7. Security Architecture

### 1. Tujuan
RAW OS Security Architecture mentakrifkan mekanisme untuk melindungi identity, data, authority, decisions, actions, interfaces, agents, integrations dan evidence sepanjang lifecycle sistem.

Security dalam RAW OS ialah sebahagian daripada governance dan control architecture, bukan lapisan tambahan yang hanya diletakkan selepas sistem dibina.

Core principle:

> SECURITY MUST PRESERVE PURPOSE, AUTHORITY, INTEGRITY, CONFIDENTIALITY, AVAILABILITY AND ACCOUNTABILITY.

### 2. Security Design Principles

1. **Least Privilege** — actor menerima privilege minimum yang diperlukan.
2. **Explicit Trust** — trust tidak boleh diandaikan semata-mata kerana actor berada dalam system.
3. **Explicit Authority** — authentication tidak sama dengan authorisation.
4. **Defense in Depth** — critical controls tidak bergantung kepada satu mekanisme sahaja.
5. **Fail Secure** — apabila uncertainty atau security control failure berlaku, default behaviour mestilah mengehadkan exposure.
6. **Assume Breach** — architecture direka dengan andaian bahawa sebahagian boundary boleh ditembusi.
7. **Separation of Duties** — critical responsibilities dipisahkan apabila risk memerlukannya.
8. **Traceability** — significant security events mesti menghasilkan evidence.
9. **Revocability** — credentials, sessions, permissions dan delegated authority mesti boleh ditarik balik.
10. **Secure by Design** — security requirements ditentukan sebelum implementation, bukan selepas incident.

### 3. Security Domains

RAW OS security meliputi:

- Identity Security
- Authentication
- Authorisation
- Data Security
- Application Security
- API Security
- AI / Agent Security
- Integration Security
- Infrastructure Security
- Operational Security
- Audit & Evidence Security
- Incident Response
- Recovery & Resilience

### 4. Identity Architecture

Identity mengenal pasti actor; authority menentukan apa yang actor dibenarkan lakukan.

Jenis identity:

- Human identity
- Service identity
- AI / Agent identity
- Organisation identity
- External system identity
- Device / workload identity

Minimum identity properties:

- Unique identifier
- Identity type
- Status
- Owner
- Authentication method
- Associated roles
- Authority references
- Lifecycle state

### 5. Authentication

Authentication menjawab:

> “Adakah actor benar-benar siapa yang dinyatakan?”

Architecture mesti menyokong authentication yang sesuai dengan risk, termasuk:

- Strong credentials
- Multi-factor authentication where required
- Service-to-service authentication
- Short-lived credentials where appropriate
- Session control
- Credential rotation
- Revocation

Authentication success tidak memberikan permission secara automatik.

### 6. Authorisation

Authorisation menjawab:

> “Adakah actor dibenarkan melakukan action ini dalam context ini?”

Decision logic:

`IDENTITY → ROLE → CAPABILITY → AUTHORITY → SCOPE → CONDITION → POLICY → ALLOW / LIMIT / ESCALATE / DENY`

Authorisation mesti mempertimbangkan:

- Resource
- Action
- Actor
- Role
- Scope
- Context
- Time
- Policy
- Risk

### 7. Authority & Privilege Model

RAW OS membezakan:

`IDENTITY ≠ CAPABILITY ≠ AUTHORITY ≠ PRIVILEGE`

Privilege ialah technical permission untuk menggunakan capability. Authority ialah governance permission untuk bertindak.

Delegated privilege mesti:

- Bounded
- Time-aware where appropriate
- Revocable
- Traceable
- Least-privileged

### 8. Access Control Model

RAW OS boleh menyokong gabungan model access control bergantung kepada implementation:

- RBAC — role-based
- ABAC — attribute-based
- ReBAC — relationship-based
- Policy-based access control
- Context-aware controls

Canonical logic tetap:

`REQUEST → POLICY EVALUATION → AUTHORISATION DECISION → ENFORCEMENT`

### 9. Data Security

Data protection merangkumi:

- Classification
- Encryption at rest
- Encryption in transit
- Access control
- Data minimisation
- Retention
- Secure deletion
- Backup protection
- Data lineage
- Integrity validation

Sensitive data hendaklah hanya accessible kepada actor yang mempunyai legitimate need dan authority.

### 10. Data Integrity

Critical data mesti dilindungi daripada unauthorized modification.

Mechanisms boleh termasuk:

- Integrity checks
- Versioning
- Immutable audit records where appropriate
- Transaction controls
- Digital signatures where appropriate
- Checksums / hashes
- Write restrictions

Security architecture mesti dapat membezakan:

`ORIGINAL → MODIFIED → VERIFIED → COMPROMISED`

### 11. API Security

Setiap API surface mesti mempunyai:

- Authentication
- Authorisation
- Input validation
- Output validation where appropriate
- Rate limiting
- Abuse protection
- Request tracing
- Audit logging
- Versioning
- Error handling

Sensitive operations perlu menggunakan stronger authorisation atau step-up controls.

### 12. Event & State Security

Security state ialah sebahagian daripada system state.

Contoh security states:

- Trusted
- Unverified
- Restricted
- Suspended
- Compromised
- Revoked

State transition mesti dikawal:

`EVENT → SECURITY CHECK → AUTHORISED TRANSITION → NEW STATE → EVIDENCE`

### 13. AI / Agent Security

AI agents dianggap governed actors.

Core chain:

`AGENT IDENTITY → CAPABILITY → AUTHORITY → TOOL PERMISSION → POLICY CHECK → ACTION → EVIDENCE`

Controls termasuk:

- Tool allowlists
- Tool-specific permissions
- Action scopes
- Sandboxing
- Secrets isolation
- Prompt / context boundary controls
- Output validation
- Human approval for high-risk actions
- Budget / rate limits
- Kill switch / revocation

AI model access tidak boleh dianggap sebagai unrestricted system access.

### 14. Agent Tool Security

Setiap tool hendaklah mempunyai contract yang mentakrifkan:

- Tool identity
- Allowed actors
- Required authority
- Input schema
- Output schema
- Side effects
- Risk level
- Rate / budget limits
- Evidence requirements
- Revocation path

Sensitive tools hendaklah mempunyai enhanced controls.

### 15. Prompt / Context Security

Apabila AI digunakan, RAW OS perlu membezakan:

- Trusted system instructions
- Governance policies
- Authorised context
- Untrusted external content
- User-provided content
- Retrieved data
- Tool outputs

Untrusted content tidak boleh secara automatik menukar governance policy atau authority context.

### 16. Secrets Management

Secrets termasuk:

- API keys
- Access tokens
- Passwords
- Signing keys
- Encryption keys
- Service credentials

Prinsip:

- Never hard-code secrets.
- Restrict access.
- Rotate credentials.
- Revoke compromised credentials.
- Record security-relevant access without exposing secret values.

### 17. Network & Infrastructure Security

Architecture boleh menggunakan:

- Segmentation
- Private network boundaries
- Firewall rules
- Service isolation
- Secure gateways
- Zero-trust principles
- Infrastructure identity
- Secure configuration baselines

External connectivity mesti dianggap sebagai trust boundary.

### 18. Integration Security

External system integration flow:

`IDENTIFY → AUTHENTICATE → AUTHORISE → VALIDATE → TRANSFER → VERIFY → RECORD`

Untuk external systems:

- Trust must be explicit.
- Credentials must be scoped.
- Payloads must be validated.
- External authority must not automatically override RAW OS authority.
- Failures must be contained.

### 19. Security Event Model

Security-significant events termasuk:

- Login / authentication event
- Authorisation decision
- Permission change
- Privilege escalation
- Credential issue / rotation / revocation
- Policy change
- Security alert
- Data access
- Data export
- Agent tool call
- Control failure
- Incident declaration

Minimum evidence:

`EVENT ID + ACTOR + TIMESTAMP + RESOURCE + ACTION + DECISION + RESULT + CORRELATION ID`

### 20. Audit & Evidence Security

Audit records sendiri ialah protected assets.

Requirements:

- Integrity protection
- Access restriction
- Retention policy
- Traceability
- Time consistency
- Tamper detection
- Backup / recovery

Audit evidence tidak boleh mudah diubah oleh actor yang sedang diaudit.

### 21. Monitoring & Detection

Security monitoring hendaklah mengesan sekurang-kurangnya:

- Anomalous access
- Failed authentication spikes
- Privilege escalation
- Unusual API behaviour
- Unusual data access
- Agent behaviour anomalies
- Policy violations
- Repeated control failures
- Unexpected state transitions

Detection flow:

`SIGNAL → CLASSIFY → CORRELATE → ASSESS → ALERT / CONTAIN / ESCALATE`

### 22. Incident Response

Core incident lifecycle:

`DETECT → TRIAGE → CONTAIN → INVESTIGATE → ERADICATE → RECOVER → VERIFY → REVIEW`

Incident response mesti preserve evidence dan mencegah containment action memusnahkan forensic context apabila preservation diperlukan.

### 23. Security Escalation

Escalation triggers boleh termasuk:

- Critical vulnerability
- Suspected compromise
- Authority bypass
- Data breach
- Credential compromise
- Control failure
- Repeated suspicious behaviour
- Unknown security condition

Flow:

`TRIGGER → HOLD / CONTAIN → PRESERVE EVIDENCE → ESCALATE → AUTHORISED RESPONSE`

### 24. Recovery & Resilience

Security architecture mesti mempunyai recovery strategy untuk:

- Data corruption
- Credential compromise
- Service compromise
- System outage
- Malicious modification
- Integration failure

Recovery principles:

- Known-good state
- Verified backups
- Credential reset / rotation
- Integrity validation
- Reconciliation
- Post-recovery review

### 25. Secure Development Lifecycle

Security requirements perlu masuk sepanjang lifecycle:

`REQUIREMENTS → THREAT MODEL → DESIGN → IMPLEMENT → TEST → DEPLOY → MONITOR → PATCH → RETIRE`

Security testing boleh termasuk:

- Static analysis
- Dependency review
- Dynamic testing
- API testing
- Access-control testing
- Penetration testing
- AI red-team testing
- Configuration review

### 26. Threat Model

RAW OS implementation perlu mengenal pasti:

- Assets
- Threat actors
- Attack surfaces
- Trust boundaries
- Threat scenarios
- Existing controls
- Residual risk

Model ini perlu dikemas kini apabila architecture atau threat environment berubah.

### 27. Security by Failure

Default behaviour untuk security uncertainty:

`UNKNOWN → RESTRICT → PRESERVE → ESCALATE`

Bukan:

`UNKNOWN → ALLOW`

Tetapi fail-secure mesti dipertimbangkan bersama availability supaya controls tidak menghasilkan unsafe operational deadlock.

### 28. Security Governance

Setiap security control mesti mempunyai:

- Owner
- Purpose
- Scope
- Requirement
- Implementation
- Monitoring method
- Evidence
- Review interval
- Exception process
- Retirement condition

### 29. Security Exceptions

Security exception process:

`REQUEST → JUSTIFICATION → RISK ASSESSMENT → APPROVAL → COMPENSATING CONTROL → TIME LIMIT → REVIEW`

Temporary exception tidak boleh berubah menjadi permanent weakness tanpa governance review.

### 30. Security Invariants

RAW OS security invariants:

1. No actor receives authority merely through authentication.
2. No privilege exceeds defined scope.
3. No critical action occurs without attributable identity.
4. No security-critical transition occurs without enforceable control.
5. No critical evidence is freely mutable by the actor being audited.
6. Revocation must be possible for delegated access.
7. High-risk agent actions require stronger controls.
8. Unknown security conditions default to restricted handling.
9. Security controls must be testable.
10. Security failures must feed back into governance and design.

### 31. Security Compatibility Test

Implementation dianggap security-compatible jika mampu menjawab:

- Who is the actor?
- How is identity verified?
- What capability exists?
- What authority exists?
- What resource is being accessed?
- What policy applies?
- What risk exists?
- What control is enforced?
- What happens on failure?
- What evidence is recorded?
- How is access revoked?
- How is the system recovered?

### 32. Relationship to Other v1.0 Components

Security Architecture merentasi semua komponen:

`API ↔ SECURITY ↔ ALGORITHM ↔ DATABASE ↔ EVENT/STATE ↔ AI/AGENT ↔ UI/UX ↔ INTEGRATIONS`

Security bukan endpoint terakhir. Ia cross-cutting architecture.

### 33. Boundary of v1.0 Security Architecture

Dokumen ini belum memilih specific vendor, cloud platform, identity provider, database engine, cryptographic library atau security product.

Implementation choices mesti mematuhi RAW OS security requirements dan tidak mengubah constitutional constraints.

### 34. Next Layer

Cadangan selepas Security Architecture:

**8. SOP Architecture** — menterjemahkan governance, security, decision, incident, change dan operational requirements kepada procedural operating model yang boleh dilaksanakan.

### 35. Status

- Version: RAW OS v1.0
- Component: System Design Specification — 7. Security Architecture
- Depends on: RAW OS v0.1–v0.8 + v1.0 components 1–6
- Design principle: Secure-by-design, least-privilege, explicit-authority, auditable, resilient and adaptive

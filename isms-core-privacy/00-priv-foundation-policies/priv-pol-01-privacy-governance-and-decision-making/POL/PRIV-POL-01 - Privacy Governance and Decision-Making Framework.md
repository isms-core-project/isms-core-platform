<!-- ISMS-CORE:POLICY:PRIV-POL-01:privacy:POL:01 -->
**PRIV-POL-01 — Privacy Governance and Decision-Making Framework**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Governance and Decision-Making Framework |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-01 |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date - 4 weeks] | DPO | Initial draft — PIMS governance boundaries and decision-making framework |

**Review Cycle**: Annual (or upon significant PIMS or regulatory changes)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: Chief Information Security Officer (CISO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework — mandatory co-reference)
- ISMS-POL-01 (ISMS Governance and Decision-Making Framework — parent governance document)
- ISO/IEC 27701:2025 Clause 4.3 (Determining the scope of the PIMS)
- ISO/IEC 27701:2025 Clause 5.1 (Leadership and commitment)
- ISO/IEC 27701:2025 Clause 5.2 (Policy)
- ISO/IEC 27701:2025 Clause 9.2 (Internal audit)
- ISO/IEC 27701:2025 Clause 9.3 (Management review)
- ISO/IEC 27701:2025 Clause 10.2 (Nonconformity and corrective action)
- GDPR Article 37–39 (Data Protection Officer)
- CH FADP (DPO obligations — voluntary but recommended)

**Distribution**: All PIMS stakeholders, privacy champions, data owners, system owners, processors, internal/external auditors
**Referenced By**: All PIMS policy documents, Privacy Control Applicability Statement (PCAS), Privacy Risk Treatment Plan

---

## Executive Summary

This policy establishes **where professional judgment is exercised** in the organisation's Privacy Information Management System (PIMS), ensuring that:

- **PIMS design decisions are documented and authorised** (control interpretation, regulatory applicability, privacy risk acceptance)
- **Decision-making authority is clearly assigned** (DPO, CISO, Legal, Executive Management — competence and scope)
- **Privacy criteria evolve through controlled processes** (regulatory changes, new standards, DPA guidance, audit feedback)
- **Audit verification is objective and evidence-based** (auditors verify documented design, not reinterpret requirements)

**Purpose**: Enable **objective audit verification** by moving professional judgment to the **PIMS design phase** (documented policies, risk assessments, applicability decisions) rather than the **audit discussion phase** (subjective interpretation during certification).

**Scope**: All PIMS decision-making authority, privacy regulatory applicability determinations, control exception handling, privacy criteria evolution, and governance review processes.

**Key Principle**: **ISO/IEC 27701:2025 certification requires professional judgment at two stages:**

1. **PIMS Design** (Organisation's responsibility): Interpreting 27701 for organisational context, determining controller/processor roles, selecting risk-based controls, defining evidence sufficiency
2. **PIMS Verification** (Auditor's responsibility): Assessing whether organisational interpretation satisfies 27701, verifying implementation matches documentation

This policy documents organisational professional judgment (Stage 1) to enable objective audit verification (Stage 2).

**Relationship to ISMS-POL-01**: This policy is the privacy-specific companion to ISMS-POL-01. Where governance principles overlap (decision escalation, competence requirements, change control), ISMS-POL-01 takes precedence for information security governance. PRIV-POL-01 establishes privacy-specific governance extensions and the DPO's distinct authority.

---

## Policy Authority and Governance Boundaries

### Purpose and Scope

This policy defines **decision-making authority** for PIMS governance, ensuring:

- Clear assignment of responsibility for privacy compliance interpretation
- Documented processes for applicability, exceptions, and evolution
- Competence requirements for privacy decision-makers
- Objective criteria for audit verification

**This policy establishes:**

- Authority boundaries for PIMS decisions (Section 2: who decides what, with what competence)
- Privacy regulatory and control applicability authority (Section 3: who determines what applies)
- Privacy exception and risk acceptance processes (Section 4: how privacy risks that cannot be mitigated are handled)
- Privacy criteria change control (Section 5: how the PIMS evolves over time)
- Governance effectiveness monitoring (Section 6: how governance quality is assessed)

**This policy does NOT establish:**

- Specific privacy control implementation requirements (addressed in 21 control group POLs and IMPs)
- Privacy risk assessment methodologies (addressed in PIMS Risk Assessment Procedure)
- Document control procedures (addressed in Document Control Procedure per Clause 7.5)
- Internal audit programme (addressed in Internal Audit Procedure per Clause 9.2)

**Boundary Principle**: This policy establishes **decision-making authority and processes**. The decisions themselves are documented in **PRIV-POL-00 (regulatory applicability), PCAS (control applicability), and Privacy Risk Acceptance Register (risk treatment decisions)**.

**Integration with ISO 27701:2025**:

- **Clause 4.2 (Interested Parties)**: This policy formalises authority for interpreting interested party (regulatory) requirements
- **Clause 4.3 (Scope)**: DPO and CISO jointly approve PIMS scope determination; Executive Management formally approves
- **Clause 5.1 (Leadership)**: Establishes decision escalation path ensuring top management commitment
- **Clause 5.2 (Policy)**: DPO owns the PIMS policy suite; CISO co-owns where privacy and security obligations overlap
- **Clause 9.3 (Management Review)**: Provides governance framework for annual PIMS review
- **Clause 10.1 (Continual Improvement)**: Enables governance process improvement through lessons learned

---

## Authority Boundaries and Competence

### Decision-Making Authority

**Authority Assignment**:

| Authority Level | Role | Decision Scope | Competence Requirement |
|----------------|------|----------------|----------------------|
| **Primary** | Data Protection Officer (DPO) | Privacy control design, GDPR/FADP interpretation, DPIA authority, data subject rights procedures, regulatory applicability (Tier 1/2 privacy laws), day-to-day PIMS decisions | GDPR/FADP expertise (CIPP/E, CIPM or equivalent), 3+ years data protection experience, independence per GDPR Article 38, direct reporting to CEO/Board |
| **Secondary** | Chief Information Security Officer (CISO) | Technical privacy measures (encryption, access control, pseudonymisation), security architecture supporting PIMS, A.3 shared security controls, ISO 27701 Annex A.3 implementation | Information security expertise (CISSP/CISM or equivalent), ISO 27001/27701 knowledge, technical background |
| **Tertiary** | Legal/Compliance Officer | Legal interpretation of data protection obligations, processor agreement review, international transfer mechanism selection, supervisory authority engagement | Legal training or compliance certification, data protection regulatory knowledge, access to external privacy counsel |
| **Approval** | Executive Management (CEO/Board) | Strategic privacy decisions, PIMS scope changes, resource allocation, privacy risk acceptance, major architecture decisions affecting PII | Fiduciary responsibility for organisational privacy risk, understanding of GDPR/FADP accountability obligation (Art. 24/5(2)), budget authority |

**DPO Independence**:

The DPO SHALL operate with independence per GDPR Article 38.3 and ISO 27701:2025:

- The DPO reports directly to the highest level of management
- The DPO is not instructed how to perform DPO tasks
- The DPO is not dismissed or penalised for performing DPO duties
- The DPO has no conflict of interest (does not hold a position that requires determining purposes and means of processing)
- The organisation provides resources and access necessary to perform DPO duties

**DPO independence verification** is documented in the organisational chart and DPO appointment letter maintained in the PIMS document repository.

**Decision Escalation Path**:

1. **Routine Decisions** (privacy control design, evidence format, DPIA methodology):
   - **Authority**: DPO
   - **Documentation**: PIMS POL/IMP documents, DPIA records
   - **Review**: Internal audit (Clause 9.2), annual management review (Clause 9.3)

2. **Regulatory Interpretation** (PRIV-POL-00 Tier assignments, contract privacy requirements, DPA guidance interpretation):
   - **Authority**: DPO determines privacy applicability; CISO implements technical measures; Legal reviews contractual dimensions
   - **Documentation**: PRIV-POL-00 Regulatory Applicability Matrix
   - **Review**: Quarterly monitoring, annual comprehensive review

3. **Privacy Risk Acceptance** (privacy control exclusion or residual risk acceptance):
   - **Authority**: DPO proposes (with privacy risk assessment); Executive Management approves
   - **Documentation**: Privacy Risk Acceptance Register
   - **Review**: Annual management review (Clause 9.3)

4. **Strategic Changes** (PIMS scope change, role determination change controller↔processor, certification body change):
   - **Authority**: Executive Management approval (DPO + CISO recommend; CEO/Board decides)
   - **Documentation**: Management review records (Clause 9.3), board minutes where applicable
   - **Review**: As part of organisational strategic planning cycle

**Mandatory Requirements**:

1. The DPO **shall** approve all privacy control implementations before deployment.
2. The DPO **shall** approve all regulatory applicability determinations (PRIV-POL-00 Tier assignments) before publication or update.
3. Executive Management **shall** approve all privacy risk acceptance decisions per ISO 27701:2025 Clause 7 and GDPR Article 24 (accountability).
4. The DPO **shall** be consulted on any new processing activity, system change, or product development that involves PII (privacy by design trigger).
5. Decision escalation **shall** follow the path defined above.

---

### Professional Judgment in ISO 27701:2025 Certification

**Stage 1: PIMS Design (Organisation's Responsibility)**

Professional judgment exercised by the organisation includes:

1. **Role Determination** (controller vs. processor per processing activity):
   - Identifying for each processing activity whether the organisation acts as controller, processor, or both
   - Documenting the determination per processing activity in the ROPA (GDPR Art. 30 / FADP Art. 12)
   - Selecting the applicable control set: Annex A.1 (controller), A.2 (processor), A.3 (shared)
   - Documented in: ROPA, PCAS (Privacy Control Applicability Statement)

2. **Scope Determination** (Clause 5.3):
   - Which PII processing activities are within PIMS scope
   - Whether PIMS is integrated with ISO 27001 ISMS or standalone
   - Geographic and organisational boundaries
   - Documented in: PIMS Scope Document

3. **Control Selection** (Clause 7 / Annex A):
   - Selecting controls based on privacy risk assessment
   - Determining controller-specific, processor-specific, and shared control applicability
   - Deciding implementation approach
   - Documented in: PCAS, Privacy Risk Treatment Plan, control POL/IMP documents

4. **Evidence Sufficiency**:
   - Defining what evidence demonstrates control effectiveness (DPIA records, consent logs, data subject rights response records)
   - Determining evidence frequency and retention
   - Documented in: Control IMP documents (evidence section)

5. **Privacy Regulatory Applicability** (PRIV-POL-00):
   - Determining which privacy laws apply (Tier 1/2/3 framework per PRIV-POL-00)
   - Assessing conditional regulation triggers (ISO 27018, UK GDPR, LGPD, PIPL)
   - Documented in: PRIV-POL-00 Regulatory Applicability Matrix

**Stage 2: PIMS Verification (Auditor's Responsibility)**

Professional judgment exercised by the auditor includes:

1. **Process Quality Assessment**:
   - Is privacy risk assessment methodology sound and consistently applied?
   - Are role determinations (controller/processor) reasonable given processing activities?
   - Are decision-makers competent per Section 2.1 competence requirements?

2. **ISO 27701:2025 Alignment**:
   - Does organisational interpretation of Annex A controls satisfy 27701 control objectives?
   - Is the PCAS complete and justified (all applicable Annex A controls documented)?
   - Are mandatory clauses (5–11) addressed?

3. **Implementation Effectiveness** (Stage 2):
   - Does actual implementation match documented design (POL → IMP → Evidence chain)?
   - Is evidence sufficient to demonstrate control operation?
   - Are nonconformities and corrective actions handled per Clause 10.2?

**Collaboration Principle**: Where auditor identifies potential gaps, resolution follows the Applicability Challenge Protocol (Section 3.3). Discussion focuses on ISO 27701:2025 clause alignment and documented reasoning.

---

### Applicability Challenge Protocol

**Purpose**: Structured process for resolving disagreements on privacy applicability determinations between organisation and auditor.

**When This Protocol Applies**:

- Auditor questions regulatory applicability (e.g., "Is GDPR truly applicable given your data flows?")
- Auditor challenges controller/processor role determination for a processing activity
- Auditor challenges control exclusion in the PCAS
- Auditor believes alternative control does not achieve ISO 27701:2025 objective

**Protocol Steps**:

**Step 1 — Auditor Raises Concern**: Documents specific concern — which determination, what evidence conflicts, which 27701 clause or control objective may not be satisfied.

**Step 2 — Organisation Provides Documentation**:

- For **regulatory applicability**: Assessment per PRIV-POL-00 methodology; trigger evaluation; DPO + Legal approval record
- For **role determination**: Processing activity description; ROPA entry; DPO rationale for controller/processor classification
- For **control exclusion**: Privacy risk assessment showing why risk does not apply; PCAS justification; organisational context documentation

**Step 3 — Collaborative Assessment**: Organisation and auditor jointly assess whether documented rationale satisfies ISO 27701:2025 requirements. Discussion is fact-based — organisational context documentation vs. standard requirements.

**Step 4 — Resolution**:

| Outcome | Action |
|---------|--------|
| Organisation rationale accepted | Document in audit working papers; no change required |
| Gap confirmed | Organisation triggers corrective action (Clause 10.2); update PCAS/PRIV-POL-00 as applicable |
| Disagreement unresolved | Escalate to certification body dispute resolution process |

---

## Compliance Applicability Authority

### Privacy Regulatory Applicability

**Framework**: Privacy regulatory applicability is determined per **PRIV-POL-00**, which establishes:

- **Tier 1 (Mandatory)**: EU GDPR, CH FADP, ISO 27701:2025 (for certification)
- **Tier 2 (Conditional)**: ISO 27018:2025, UK GDPR, LGPD, PIPL, other jurisdictions
- **Tier 3 (Informational)**: ISO 27017:2019, ISO 27002:2022, NIST Privacy Framework

**Decision Authority**:

1. **Tier Determination**: DPO determines privacy regulatory applicability per PRIV-POL-00 Section (Assessment Process), with Legal review for complex cross-border situations
2. **Control Implementation**: DPO + CISO implement controls to satisfy applicable regulations (CISO leads on A.3 shared security controls; DPO leads on A.1/A.2 privacy-specific controls)
3. **Approval**: Executive Management approves PRIV-POL-00 Regulatory Applicability Matrix annually

**Review Cycle**: Quarterly monitoring (DPO + Legal) + Annual comprehensive review (Executive Management approval) + Triggered reassessment on business or regulatory changes.

---

### Privacy Control Applicability (ISO 27701:2025 Annex A)

**Framework**: Privacy control applicability is determined per ISO 27701:2025 Clause 7 (Planning) and documented in the **Privacy Control Applicability Statement (PCAS)** — the PIMS equivalent of the SoA.

**PCAS Documentation**:

For each Annex A control (78 total across A.1/A.2/A.3):

| Field | Content |
|-------|---------|
| **Control Reference** | e.g., A.1.3.5 — A.1.3.10 (Data Subject Rights) |
| **Role Applicability** | Controller / Processor / Both |
| **Implementation Status** | Applicable (implemented) / Not Applicable (justified) / Alternative Control |
| **Justification** | Technical/operational rationale |
| **Reference** | Control group POL + IMP documents |

**Control Applicability Decision Criteria**:

| Status | Criteria | Documentation Required |
|--------|----------|------------------------|
| **Applicable** | Privacy risk exists; control mitigates it; organisation acts in the applicable role | Control group POL + IMP documents + evidence |
| **Not Applicable** | Risk does not exist given organisational context; or role (controller/processor) does not apply to this processing activity | PCAS justification + role determination + privacy risk assessment |
| **Alternative Control** | Standard control not feasible; alternative achieves same privacy objective | PCAS justification + control objective mapping + DPO approval |
| **Risk Accepted** | Privacy risk exists; control not implemented; residual risk accepted by Executive Management | PCAS justification + Privacy Risk Acceptance Register entry (Executive Management signature) |

**Decision Authority**:

1. DPO proposes control applicability determination per processing activity role assessment
2. CISO reviews A.3 shared security control determinations for technical feasibility
3. Executive Management approves risk acceptance entries

---

## Exception Handling and Privacy Risk Acceptance

### Privacy Control Exceptions

**Definition**: A privacy control exception occurs when an applicable Annex A control cannot be implemented as designed (technical constraint, operational limitation, or proportionality assessment).

**Exception Types**:

| Type | Definition | Example |
|------|-----------|---------|
| **Technical Exception** | Control cannot be implemented due to technical system constraint | Legacy system cannot enforce purpose limitation at query level |
| **Operational Exception** | Control creates disproportionate operational burden relative to privacy risk | Full re-consent campaign for low-risk legacy data processing |
| **Temporary Exception** | Control will be implemented within defined timeframe; interim risk accepted | Data minimisation controls on roadmap for next release cycle |

**Exception Process**:

1. **Identify**: DPO identifies control exception during PCAS review or DPIA
2. **Assess**: DPO documents privacy risk without the control (likelihood × impact on PII principals)
3. **Mitigate**: DPO identifies compensating controls or alternative measures where possible
4. **Approve**: Executive Management approves exceptions where residual privacy risk is material
5. **Document**: Privacy Risk Acceptance Register entry with rationale, compensating controls, review date
6. **Monitor**: Exceptions reviewed quarterly by DPO; closed when underlying constraint resolved

### Privacy Risk Acceptance

**Scope**: Privacy risk acceptance applies where:

- A control is excluded from the PCAS without alternative implementation
- Residual privacy risk remains after all feasible controls are implemented
- A DPIA identifies residual high risk and prior DPA consultation is not triggered or is completed

**Authority**: Executive Management (per GDPR Article 24 accountability obligation — ultimate responsibility for TOMs rests with the controller/processor's highest management level).

**Documentation Requirements** (Privacy Risk Acceptance Register entry):

| Field | Content |
|-------|---------|
| Processing Activity | Affected processing activity (ROPA reference) |
| Control Reference | Which Annex A control is excluded or insufficient |
| Privacy Risk | Risk to PII principals (likelihood × impact; rights and freedoms impact) |
| Justification | Why control cannot be implemented (technical/operational rationale) |
| Compensating Controls | Alternative measures partially mitigating the risk |
| Residual Risk Level | Low / Medium / High (after compensating controls) |
| DPO Recommendation | Accept / Escalate to DPA prior consultation |
| Executive Approval | Signature of CEO or delegated Executive Management member |
| Review Date | Maximum 12 months; sooner if processing activity changes |

**Escalation Trigger**: Where residual risk remains HIGH after compensating controls, the DPO **shall** assess whether GDPR Article 36 prior consultation with the supervisory DPA is required before proceeding.

---

## Privacy Criteria Change Control

### When Change Control Applies

Privacy compliance criteria change when:

| Trigger | Example | Action Required |
|---------|---------|----------------|
| Regulatory change | GDPR implementing regulation published; FADP amended | PRIV-POL-00 update + PCAS review |
| New DPA guidance | EDPB Guidelines update (e.g., consent, legitimate interest) | Assess impact on A.1.2.2-5 and A.1.3 packs |
| Standard edition update | ISO 27701:2025 → future edition; ISO 27017:2025 published | PCAS review; control pack IMP updates |
| Role determination change | Organisation moves from pure processor to controller | PCAS scope change; A.1 controller packs activated |
| Business activity change | New product category; new jurisdiction; new data category | Triggered applicability assessment per PRIV-POL-00 |
| DPIA outcome | DPIA identifies new risk requiring additional controls | PCAS update; control group IMP update |

### Change Assessment Process

1. **Identify Change**: DPO monitors sources per PRIV-POL-00 (EDPB, FDPIC, ISO, national DPAs)
2. **Impact Assessment**: DPO + CISO assess which PCAS controls, control group POLs, and IMPs are affected
3. **Update PRIV-POL-00**: If Tier assignment changes, update Regulatory Applicability Matrix (DPO + Legal approval)
4. **Update PCAS**: If control applicability changes, update PCAS (DPO approval)
5. **Update Control Packs**: DPO + control group owner update affected POL/IMP documents
6. **Management Review**: Material changes reported at next management review (Clause 9.3) or triggered extraordinary review
7. **Communication**: DPO communicates changes to all affected stakeholders (privacy champions, data owners, processors)

### Document Version Control

All PIMS policy documents follow the version control standard established in ISMS-POL-01:

- Version increments on material changes (X.0 → major revision; X.1 → minor update)
- Changes documented in Version History table
- Prior versions retained per document retention schedule
- DPO approves all version updates to PIMS policy documents
- Changes communicated to document holders within 5 business days of publication

---

## Governance Effectiveness Monitoring

### Annual PIMS Management Review

**Frequency**: Annual (Q4) — aligned with ISMS management review where possible

**Participants**: DPO (lead), CISO, Legal/Compliance Officer, Executive Management

**Agenda** (per ISO 27701:2025 Clause 9.3):

| Input | Source |
|-------|--------|
| Status of actions from previous reviews | DPO action log |
| Changes in external/internal issues affecting PIMS | Regulatory monitoring log (PRIV-POL-00) |
| Privacy performance indicators | Audit results, DPIA count, data subject rights response times, breach statistics |
| Nonconformities and corrective actions | Clause 10.2 register |
| Risk acceptance register review | Privacy Risk Acceptance Register |
| Opportunities for improvement | DPO recommendations |
| Processor performance | Annual processor compliance reviews |

**Outputs** (per Clause 9.3.3):

- Decisions on continual improvement opportunities
- Resource allocation decisions
- PIMS scope changes (if any)
- Updated risk acceptance approvals
- Management Review Record (signed by Executive Management)

### Key Privacy Performance Indicators

| Indicator | Target | Measurement |
|-----------|--------|-------------|
| DPIA completion rate | 100% of high-risk processing activities | DPO DPIA register |
| Data subject rights response time | Within GDPR/FADP deadline (30 days standard; 3 months extended) | Rights request log |
| Breach notification compliance | 100% within 72 hours to DPA (where required) | Incident log |
| Processor agreement coverage | 100% of processors under Art. 28 DPA | Processor register |
| Privacy training completion | 100% of staff with PII access annually | Training records |
| PIMS internal audit completion | Full coverage of all 21 control groups within each 3-year certification cycle (rolling schedule); at minimum 7 control groups per year | Audit schedule |

### Quarterly DPO Monitoring

**Frequency**: Quarterly

**Participants**: DPO + Legal (CISO as needed)

**Focus**:

- Regulatory changes detected (new guidance, enforcement actions, DPA decisions)
- Business trigger events (new processing, new markets, new systems)
- Open data subject rights requests (backlogs, escalations)
- Open privacy incidents (investigation status, breach notifications)
- Processor compliance issues flagged

**Deliverable**: Quarterly DPO monitoring log maintained in PIMS document repository.

---

## Integration with PIMS Processes

### Privacy by Design (PbD) Integration

**Trigger**: DPO **shall** be consulted before:

- Any new product or service involving PII is designed or launched
- Any existing processing system is substantially modified
- Any new vendor / processor is engaged for PII processing
- Any new data category or processing purpose is introduced

**DPO Authority in PbD**:

- Recommend privacy-protective design choices (data minimisation, pseudonymisation, purpose limitation)
- Require DPIA where processing is likely to result in high risk (GDPR Art. 35; FADP Art. 24)
- Escalate to Executive Management where privacy risk cannot be designed out

### DPIA Process

**Authority**:

| Decision | Authority |
|---------|---------|
| Determine whether DPIA is required | DPO |
| Approve DPIA methodology | DPO |
| Sign off completed DPIA | DPO + relevant data owner |
| Approve residual high risk acceptance | Executive Management |
| Assess whether Art. 36 prior consultation required (where DPIA identifies unmitigatable residual high risk) | DPO |
| Decide whether prior DPA consultation required | DPO |

**DPIA Trigger Criteria** (mandatory per GDPR Art. 35):

- Systematic and extensive profiling with significant effects
- Large-scale processing of special category data
- Systematic monitoring of publicly accessible areas
- Any processing on the national DPA's "blacklist" (published by EDPB / FDPIC)
- New technology or novel processing with inherent uncertainty

**DPIA Documentation**: Maintained in PIMS document repository. DPIAs retained for the life of the processing activity + 3 years.

### Data Subject Rights Integration

**Authority**: DPO owns the data subject rights process.

**Response Authority**:

| Right | Handler | DPO Role | Escalation |
|-------|---------|---------|-----------|
| Access (Art. 15) | DPO / Privacy Champion | Review complex cases | Legal where identity verification issues |
| Erasure (Art. 17) | DPO / Privacy Champion + IT | Approve erasure exceptions | Executive Management for legally disputed requests |
| Restriction (Art. 18) | DPO / Privacy Champion + IT | Approve restriction | DPO direct handling for complex cases |
| Portability (Art. 20) | DPO / Privacy Champion + IT | Approve format | Technical where format disputed |
| Objection (Art. 21) | DPO (primary) | Direct handling | Legal for compelling legitimate grounds assessment |
| Automated decisions (Art. 22) | DPO (primary) | Direct handling | Legal + Executive Management for high-impact cases |

### Processor Oversight Integration

**Authority**: DPO oversees processor compliance; Legal negotiates processor agreements.

**Processor Governance**:

| Activity | Frequency | Authority |
|---------|-----------|---------|
| Processor agreement review (Art. 28 DPA) | At onboarding; then annually (high-risk processors) or every 3 years (standard processors) | Legal (DPO review for privacy clauses) |
| Processor audit / assessment | Annual (risk-based) | DPO + CISO |
| Sub-processor disclosure review | Quarterly | DPO |
| Processor incident notifications | On receipt | DPO (coordinates response) |

---

## Evidence for This Policy

The following evidence demonstrates operation of PIMS governance per this policy:

| Evidence Type | Description | Retention |
|--------------|-------------|-----------|
| DPO appointment record | DPO appointment letter + organisational chart showing independence | Duration of appointment + 3 years |
| PCAS (Privacy Control Applicability Statement) | Completed and approved statement for all 78 Annex A controls | PIMS certification cycle + 3 years |
| Privacy Risk Acceptance Register | Entries with Executive Management signatures | 3 years minimum |
| DPIA register | List of all DPIAs conducted with status and outcome | Life of processing + 3 years |
| Data subject rights log | All rights requests with response dates and outcomes | 3 years |
| Quarterly DPO monitoring logs | DPO monitoring records (regulatory changes, trigger events) | 3 years |
| Annual management review records | Signed management review minutes | 3 years |
| Privacy training records | Training completion by role | 3 years |
| Processor register + DPAs | List of processors + signed Art. 28 agreements | Duration of processing + 3 years |
| Breach notification log | All incidents assessed; notifications made | 3 years |

---

## Closing Statement

This policy establishes the governance framework for the organisation's Privacy Information Management System.

**What this policy establishes:**

- Decision-making authority for PIMS governance (DPO, CISO, Legal, Executive Management)
- Professional judgment framework enabling objective audit verification
- Privacy control applicability authority (PCAS)
- Privacy risk acceptance authority and documentation requirements
- Privacy criteria change control processes
- Governance effectiveness monitoring

**What this policy does NOT establish:**

- Specific privacy control implementation requirements (addressed in 21 control group POLs and IMPs)
- Privacy risk assessment methodology (addressed in PIMS Risk Assessment Procedure)
- Document control (addressed in Document Control Procedure per Clause 7.5)
- Internal audit programme (addressed in Internal Audit Procedure per Clause 9.2)

**Separation of Concerns:**

- **PRIV-POL-00**: Defines WHICH privacy regulations apply
- **This Policy (PRIV-POL-01)**: Defines WHO decides, HOW decisions are made, and HOW the PIMS evolves
- **Control Group POLs (21 packs)**: Define WHAT the organisation must do per control domain
- **Control Group IMPs**: Define HOW to implement the control requirements
- **Compliance Monitoring**: Verifies and tracks COMPLIANCE status

---

**END OF PRIV-POL-01**

*"Privacy governance is not bureaucracy — it is the documented judgment that turns regulatory obligations into operational reality."*

<!-- QA_VERIFIED: [Date] -->

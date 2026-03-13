<!-- ISMS-CORE:POLICY:ISMS-POL-01:framework:POL:01 -->
**ISMS-POL-01 — ISMS Governance and Decision-Making Framework**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | ISMS Governance and Decision-Making Framework |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-01 |
| **Document Creator** | Chief Information Security Officer (CISO) |
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
| 1.0 | [Date - 4 weeks] | CISO | Initial draft - governance boundaries framework |

**Review Cycle**: Annual (or upon significant ISMS changes)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.1 (Policies for Information Security)
- Statement of Applicability (SoA)
- Risk Treatment Plan (ISO 27001 Clause 6.1.3)
- Risk Acceptance Register (Clause 6.1.3d)
- ISO 27001:2022 Clause 4.1 (Understanding the organisation and its context)
- ISO 27001:2022 Clause 5.3 (Roles, responsibilities and authorities)
- ISO 27001:2022 Clause 6.1.3 (Information security risk treatment)
- ISO 27001:2022 Clause 7.5.3 (Control of documented information)
- ISO 27001:2022 Clause 9.2 (Internal audit)
- ISO 27001:2022 Clause 9.3 (Management review)
- ISO 27001:2022 Clause 10.2 (Nonconformity and corrective action)

**Distribution**: All ISMS stakeholders, policy authors, system owners, internal/external auditors
**Referenced By**: All ISMS policy documents, Statement of Applicability, Risk Treatment Plan

## Executive Summary

This policy establishes **where professional judgment is exercised** in the organisation's Information Security Management System (ISMS), ensuring that:

- **Model design decisions are documented and authorised** (control interpretation, regulatory applicability, risk acceptance)
- **Decision-making authority is clearly assigned** (CISO, Legal/Compliance, Executive Management competence and scope)
- **Compliance criteria evolve through controlled processes** (regulatory changes, threat evolution, audit feedback)
- **Audit verification is objective and evidence-based** (auditors verify documented design, not reinterpret requirements)

**Purpose**: Enable **objective audit verification** by moving professional judgment to **model design phase** (documented policies, risk assessments, applicability decisions) rather than **audit discussion phase** (subjective interpretation during certification).

**Scope**: All ISMS decision-making authority, regulatory applicability determinations, control exception handling, compliance criteria evolution, and governance review processes.

**Key Principle**: **ISO 27001 certification requires professional judgment at two stages:**

1. **Model Design** (Organisation's responsibility): Interpreting ISO 27001 for organisational context, selecting risk-based controls, defining evidence sufficiency
2. **Model Verification** (Auditor's responsibility): Assessing whether organisational interpretation satisfies ISO 27001, verifying implementation matches documentation

This policy documents organisational professional judgment (Stage 1) to enable objective audit verification (Stage 2).

## Policy Authority and Governance Boundaries

### Purpose and Scope

This policy defines **decision-making authority** for ISMS governance, ensuring:

- Clear assignment of responsibility for compliance interpretation
- Documented processes for applicability, exceptions, and evolution
- Competence requirements for decision-makers
- Objective criteria for audit verification

**This policy establishes:**

- Authority boundaries for ISMS decisions (Section 2: who decides what, with what competence)
- Regulatory and control applicability authority (Section 3: who determines what applies)
- Exception and risk acceptance processes (Section 4: how controls that cannot be implemented are handled)
- Compliance criteria change control (Section 5: how model evolves over time)
- Governance effectiveness monitoring (Section 6: how governance quality is assessed)

**This policy does NOT establish:**

- Specific control implementation requirements (addressed in Annex A control policies: ISMS-POL-A.X.XX series)
- Risk assessment methodologies (addressed in Risk Assessment Procedure: Clause 6.1.2)
- Document control procedures (addressed in Document Control Procedure: Clause 7.5.3)
- Internal audit program (addressed in Internal Audit Procedure: Clause 9.2)

**Boundary Principle**: This policy establishes **decision-making authority and processes**. The decisions themselves (which controls, which regulations, which risks to accept) are documented in **POL-00 (regulatory applicability), SoA (control applicability), and Risk Acceptance Register (risk treatment decisions)**.

**Integration with ISO 27001**:

- **Clause 4.1 (Context)**: This policy supports understanding external context (how regulations and standards are interpreted for organisational context)
- **Clause 5.3 (Roles and responsibilities)**: Formalises authority structure for ISMS decision-making
- **Clause 6.1.3 (Risk treatment)**: Supports risk-based control selection, alternative controls, and risk acceptance authority
- **Clause 7.5.3 (Document control)**: Establishes governance for compliance criteria changes
- **Clause 9.3 (Management review)**: Provides framework for reviewing governance effectiveness
- **Clause 10.1 (Continual improvement)**: Enables governance process improvement through lessons learned

## Authority Boundaries and Competence

### Decision-Making Authority

**Authority Assignment**:

The following roles exercise decision-making authority for ISMS governance:

| Authority Level | Role | Decision Scope | Competence Requirement |
|----------------|------|----------------|----------------------|
| **Primary** | Chief Information Security Officer (CISO) | Technical control design, operational feasibility, evidence sufficiency, day-to-day implementation decisions | Information security expertise (CISSP/CISM or equivalent, 5+ years experience), technical background, ISO 27001 knowledge |
| **Secondary** | Legal/Compliance Officer | Regulatory requirements interpretation, contractual obligations, legal risk assessment, POL-00 Tier determinations | Legal training or compliance certification, regulatory monitoring capability, access to external legal counsel where needed |
| **Tertiary** | Data Protection Officer (DPO) | Privacy-specific controls (A.5.34, GDPR/nDSG compliance), data subject rights, privacy impact assessments | GDPR/nDSG expertise, data protection certification (CIPP/E or equivalent), independence per GDPR Article 38 |
| **Approval** | Executive Management (CEO/Board) | Strategic risk decisions, resource allocation, risk acceptance (Clause 6.1.3d), ISMS scope changes, major architecture decisions | Fiduciary responsibility for organisational risk, ultimate accountability for ISO 27001 certification, budget authority |

**Decision Escalation Path**:

1. **Routine Decisions** (technical implementation, evidence format, control design):
   - **Authority**: CISO
   - **Documentation**: POL/IMP documents, control design decisions
   - **Review**: Internal audit (Clause 9.2), annual management review (Clause 9.3)

2. **Regulatory Interpretation** (POL-00 Tier 1/2 applicability, contract compliance requirements):
   - **Authority**: Legal/Compliance Officer (determines applicability) + CISO (implements controls)
   - **Documentation**: POL-00 Section 8 (Regulatory Applicability Matrix)
   - **Review**: Quarterly monitoring (POL-00 Section 4.3), annual comprehensive review

3. **Risk Acceptance** (control exclusion without alternative, residual risk acceptance per Clause 6.1.3d):
   - **Authority**: CISO proposes (with risk assessment), Executive Management approves
   - **Documentation**: Risk Acceptance Register (Clause 6.1.3d documentation requirement)
   - **Review**: Annual management review (Clause 9.3), risk treatment plan updates

4. **Strategic Changes** (ISMS scope expansion, major control architecture shift, certification body change):
   - **Authority**: Executive Management approval required (CISO recommends, CEO/Board decides)
   - **Documentation**: Management review records (Clause 9.3.3), board meeting minutes where applicable
   - **Review**: As part of organisational strategic planning cycle

**Mandatory Requirements**:

1. The CISO **shall** approve all technical control implementations before deployment.
2. Legal/Compliance Officer **shall** approve all regulatory applicability determinations (POL-00 Tier assignments) before POL-00 publication or update.
3. Executive Management **shall** approve all risk acceptance decisions (control exclusions, residual risk acceptance) per ISO 27001 Clause 6.1.3d.
4. Decision escalation **shall** follow the path defined above. Decisions made outside designated authority require retroactive approval or corrective action per Clause 10.2.

**Evidence of Authority Exercise**:

- **Technical controls**: Approval signatures on POL/IMP documents (document control section)
- **Regulatory applicability**: Approval signatures on POL-00 Section 8 (Regulatory Applicability Matrix)
- **Risk acceptance**: Executive Management signature on Risk Acceptance Register entries
- **Strategic decisions**: Management review meeting minutes (Clause 9.3) or board resolutions

### Professional Judgment in ISO 27001 Certification

**ISO 27001 certification requires professional judgment at two distinct stages:**

**Stage 1: Model Design (Organisation's Responsibility)**

Professional judgment exercised by the organisation includes:

1. **Context Interpretation** (Clause 4.1):
   - Determining which external factors (regulations, threats, industry practices) are relevant to ISMS scope
   - Assessing organisational constraints (resources, architecture, risk appetite)
   - Documented in: Organisational Context Document, POL-00 (regulatory applicability)

2. **Control Selection** (Clause 6.1.3):
   - Selecting controls based on risk assessment (which risks require which controls)
   - Determining control applicability (applicable, not applicable, alternative control)
   - Deciding implementation approach (technical architecture, operational processes)
   - Documented in: Statement of Applicability (SoA), Risk Treatment Plan, control POL/IMP documents

3. **Evidence Sufficiency**:
   - Defining what evidence demonstrates control effectiveness (Python workbooks, logs, configurations)
   - Determining evidence frequency (real-time, daily, monthly, quarterly)
   - Establishing evidence retention periods (12 months, 3 years, certification cycle)
   - Documented in: Control IMP documents (evidence section), Python script design

4. **Regulatory Applicability** (POL-00):
   - Determining which regulations apply to the organisation (Tier 1/2/3 framework)
   - Assessing conditional regulation triggers (DORA, NIS2, PCI DSS applicability)
   - Deciding when reassessment is required (quarterly monitoring, triggered events)
   - Documented in: POL-00 Section 8 (Regulatory Applicability Matrix)

**Stage 2: Model Verification (Auditor's Responsibility)**

Professional judgment exercised by the auditor includes:

1. **Process Quality Assessment**:
   - Is risk assessment methodology sound and consistently applied? (Clause 6.1.2)
   - Are control selection decisions reasonable given organisational context? (Clause 6.1.3)
   - Are decision-makers competent per Section 2.1 competence requirements?
   - Are governance processes documented and followed? (this policy)

2. **ISO 27001 Alignment**:
   - Does organisational interpretation of Annex A controls satisfy ISO 27001 control objectives?
   - Are mandatory requirements addressed? (Clause 4-10 requirements, documented information per Clause 7.5)
   - Is Statement of Applicability complete and justified? (all 93 controls documented)

3. **Implementation Effectiveness** (Stage 2):
   - Does actual implementation match documented design? (POL → IMP → Python → Evidence chain)
   - Is evidence sufficient to demonstrate control operation? (completeness, currency, traceability)
   - Are nonconformities and corrective actions handled appropriately? (Clause 10.2)

4. **Continual Improvement**:
   - Is ISMS evolving? (internal audit findings addressed, management review effective, lessons learned implemented)
   - Are changes controlled? (document version control, reassessment after changes)

**Collaboration Principle**:

Where auditor identifies potential gaps in organisational judgment (e.g., control interpretation may not fully satisfy ISO 27001 objective, evidence may be insufficient), resolution follows **Section 3.3 Applicability Challenge Protocol**: discussion focuses on ISO 27001 clause alignment and documented reasoning, not personal preferences or authority contest.

**Outcome**: Auditor judgment focuses on **verifying quality of organisational judgment**, not **replacing organisational decisions**. If auditor assessment identifies genuine gaps, organisation triggers corrective action per Clause 10.2 (Nonconformity and Corrective Action).

### Competence Requirements for Decision-Makers

**Rationale**: Authority without competence undermines governance credibility. This section establishes minimum competence expectations for roles exercising ISMS decision-making authority.

**Competence Requirements**:

+----------------------------------------+----------------------------------------------------------------+----------------------------------------------------+
| **Role**                               | **Minimum Competence**                                         | **Verification**                                   |
+========================================+================================================================+====================================================+
| **CISO**                               | - Information security certification                           | - Resume/CV documenting experience                 |
|                                        |   (CISSP, CISM, or equivalent)                                 | - Professional certifications                      |
|                                        | - 5+ years information security experience                     |   (current, not expired)                           |
|                                        | - Technical background (infrastructure,                        | - ISO 27001 training records                       |
|                                        |   development, or security operations)                         |   (Lead Implementer or equivalent)                 |
|                                        | - ISO 27001 knowledge (training or                             |                                                    |
|                                        |   implementation experience)                                   |                                                    |
+----------------------------------------+----------------------------------------------------------------+----------------------------------------------------+
| **Legal/Compliance Officer**           | - Legal training (law degree or compliance                     | - Legal credentials or compliance                  |
|                                        |   certification such as CCEP, CRCM)                            |   certifications                                   |
|                                        | - Regulatory monitoring capability                             | - External legal counsel engagement                |
|                                        |   (legal databases, external counsel access)                   |   records (complex interpretations)                |
|                                        | - Contract review experience                                   | - Documented regulatory monitoring                 |
|                                        | - Understanding of ISO 27001 scope                             |   process (POL-00 Section 4.3)                     |
|                                        |   and applicability                                            |                                                    |
+----------------------------------------+----------------------------------------------------------------+----------------------------------------------------+
| **Data Protection Officer (DPO)**      | - GDPR/nDSG expertise                                          | - Data protection certifications                   |
|                                        |   (CIPP/E, CIPM, or equivalent)                                |   (IAPP or equivalent)                             |
|                                        | - Independence from operational management                     | - Organisational chart showing                     |
|                                        |   (per GDPR Article 38.3)                                      |   reporting line (independence verification)       |
|                                        | - Direct reporting to highest management level                 | - GDPR/nDSG training records                       |
|                                        | - Understanding of technical data                              |                                                    |
|                                        |   protection measures                                          |                                                    |
+----------------------------------------+----------------------------------------------------------------+----------------------------------------------------+
| **Executive Management**               | - Fiduciary responsibility for                                 | - Role verification (employment contract,          |
|                                        |   organisational risk (CEO, CFO, Board)                        |   board appointment)                               |
|                                        | - Understanding of ISO 27001                                   | - ISO 27001 executive briefing                     |
|                                        |   certification implications                                   |   (recorded in management review)                  |
|                                        | - Authority to allocate budget and resources                   | - Budget authority documentation                   |
|                                        | - Accountability for risk acceptance decisions                 |                                                    |
+----------------------------------------+----------------------------------------------------------------+----------------------------------------------------+


**Competence Verification**:

- **Initial Appointment**: Competence verified before role assumes ISMS decision-making authority (HR records, credential verification)
- **Annual Review**: Competence reassessed annually during management review (Clause 9.3) - certifications current, training up-to-date, external counsel engaged where needed
- **Competence Gaps**: If competence gaps identified → Addressed through training, external support (consultants, legal counsel), or role reassignment

**Auditor Verification**:

During Stage 1 and Stage 2 audits, auditor may request:
- Evidence of decision-maker competence (certifications, training records, experience documentation)
- Verification that decisions align with assigned authority (e.g., risk acceptances approved by Executive Management, not CISO self-approval)
- Assessment whether decision-makers demonstrate competence in practice (review decision quality in SoA justifications, risk assessments, regulatory determinations)

**Note**: Competence requirements are **minimum expectations**, not exhaustive qualifications. Organisations may exceed these requirements. Competence verification demonstrates to auditors that professional judgment (Section 2.2) is exercised by **qualified individuals**, not arbitrary decision-making.

## Compliance Applicability Authority

### Regulatory Applicability

**Framework**: Regulatory applicability is determined per **ISMS-POL-00 (Regulatory Applicability Framework)**, which establishes:

- **Tier 1 (Mandatory)**: Legal or contractual obligations (Swiss nFADP, GDPR where applicable, ISO 27001:2022 for certification)
- **Tier 2 (Conditional)**: Requirements that apply only when specific triggers are met (DORA, NIS2, PCI DSS, FINMA, EU AI Act)
- **Tier 3 (Informational)**: Voluntary best practices and technical guidance (NIST SP 800-series, CIS Controls, OWASP)

**Decision Authority**:

1. **Tier Determination**: Legal/Compliance Officer determines regulatory applicability per POL-00 Section 5 (Assessment Process)
2. **Control Implementation**: CISO implements controls to satisfy applicable regulations
3. **Approval**: Executive Management approves POL-00 Regulatory Applicability Matrix annually (POL-00 Section 7: Annual Review)

**Documentation**:

- **POL-00 Section 8.1**: Tier 1 (Mandatory Compliance) - current status and applicability rationale
- **POL-00 Section 8.2**: Tier 2 (Conditional Applicability) - assessment status, triggers, monitoring approach
- **POL-00 Section 8.3**: Tier 3 (Informational Reference) - frameworks used for technical guidance

**Review Cycle**:

- **Quarterly Monitoring** (POL-00 Section 4.3): Legal/Compliance + CISO review regulatory changes and organisational trigger events
- **Annual Comprehensive Review** (POL-00 Section 7): Executive Management approval of regulatory applicability determinations
- **Triggered Reassessment** (POL-00 Section 5): Business expansion, regulatory changes, customer contract requirements

**Auditor Verification**:

Auditor verifies:
- Applicability assessment methodology is sound (POL-00 Section 5 process is documented and rational)
- Reassessment triggers are monitored (quarterly monitoring logs exist, triggered assessments are documented)
- Tier determinations are reasonable given organisational context (e.g., "Not processing payment cards" → PCI DSS Tier 2 Not Applicable is justified)

Auditor does NOT substitute judgment on applicability decisions (organisation determines business activities, auditor verifies assessment process quality).

### Control Applicability (ISO 27001 Annex A)

**Framework**: Control applicability is determined per **ISO 27001 Clause 6.1.3 (Risk Treatment)**, which requires:

- Risk-based control selection (controls selected to address identified risks per Clause 6.1.2 risk assessment)
- Statement of Applicability (SoA) documentation (all 93 Annex A controls documented with implementation status and justification)
- Risk treatment decisions (implement control, alternative control, accept risk per Clause 6.1.3d)

**Decision Authority**:

1. **Control Selection**: CISO proposes control implementation approach based on risk assessment (Clause 6.1.2)
2. **Risk Acceptance**: Executive Management approves control exclusions (when control is "Not Applicable" or risk is accepted without mitigation per Clause 6.1.3d)
3. **Alternative Controls**: CISO determines alternative control equivalence (achieving same ISO 27001 control objective through different means)

**Documentation**:

- **Statement of Applicability (SoA)**: All 93 controls documented with:
  - **Implementation Status**: Applicable (implemented), Not Applicable (justified exclusion), Alternative Control (different implementation achieving same objective)
  - **Justification**: Technical/operational rationale (why control applies, why excluded, or why alternative used)
  - **Reference**: POL/IMP documents for implemented controls, risk assessment for exclusions
- **Risk Treatment Plan** (Clause 6.1.3): Risk-based rationale for control selection, priority, and implementation timeline
- **Risk Acceptance Register** (Clause 6.1.3d): Executive Management approval for controls excluded without alternative mitigation

**Control Applicability Decision Criteria**:

| Status | Criteria | Example | Documentation Required |
|--------|----------|---------|----------------------|
| **Applicable** | Risk exists, control mitigates risk, implementation feasible | A.8.15 (Logging): Organisation operates servers, logging required for incident detection | POL-A.8.15 + IMP-A.8.15 + Python workbook |
| **Not Applicable** | Risk does not exist due to organisational context | A.8.23 (Web filtering): Organisation infrastructure is server-only, no user web browsing | SoA justification: "No web browsing services provided to users, infrastructure is API/backend only. Control objective (prevent malicious website access) not applicable." + Risk assessment confirming no web browsing risk |
| **Alternative Control** | Standard control not feasible, alternative achieves same objective | A.7.4 (Physical monitoring): Infrastructure in colocation facility, CCTV operated by provider per contract | SoA justification: "Physical security monitoring implemented via colocation provider contract (24/7 CCTV, quarterly audit reports). Achieves same objective (detect unauthorised physical access)." + Contract clause reference |
| **Risk Accepted** | Risk exists, control not implemented, residual risk accepted by Executive Management | A.8.11 (Data masking): Production data used in development (technical limitation), residual risk accepted with compensating controls (access restrictions, encryption) | SoA justification: "Data masking not implemented due to [technical constraint]. Residual risk accepted by Executive Management [Date]. Compensating controls: A.5.18 (Access rights restricted), A.8.24 (Encryption at rest)." + Risk Acceptance Register entry with Executive Management signature |

**Auditor Verification**:

Auditor verifies:
- All 93 controls are documented in SoA (completeness check)
- Justifications are reasonable and align with organisational context (Clause 4.1)
- Risk treatment decisions follow documented process (Clause 6.1.3)
- Risk acceptances have Executive Management approval (Clause 6.1.3d requirement)
- Alternative controls achieve ISO 27001 control objectives (effectiveness assessment)

### Applicability Challenge Protocol

**Purpose**: Structured process for resolving disagreements on applicability determinations (regulatory Tier assignments, control exclusions) between organisation and auditor.

**When This Protocol Applies**:

- Auditor questions regulatory applicability determination (e.g., "Is GDPR truly applicable given your customer base?")
- Auditor challenges control exclusion (e.g., "Control A.8.15 marked Not Applicable but risk assessment shows logging requirement")
- Auditor believes alternative control does not achieve ISO 27001 objective (e.g., "Colocation provider CCTV may not satisfy A.7.4 control objective")

**Protocol Steps**:

**Step 1: Auditor Raises Concern**

Auditor documents specific concern:
- Which applicability determination is questioned? (POL-00 Tier assignment, SoA control status)
- What evidence suggests determination may be incorrect? (conflicting information, risk not addressed)
- Which ISO 27001 requirement or control objective is potentially not satisfied?

**Step 2: Organisation Provides Documentation**

Organisation provides documented rationale:

- **For Regulatory Applicability** (POL-00 Tier challenge):
  - Assessment per POL-00 Section 5 (methodology followed)
  - Trigger evaluation (objective criteria assessed)
  - Approval record (Legal/Compliance + Executive Management sign-off)
  - Supporting evidence (e.g., customer data processing agreements confirming no EU personal data → GDPR Not Applicable)
- **For Control Exclusion** (SoA "Not Applicable"):
  - Risk assessment showing why risk does not exist (Clause 6.1.2)
  - SoA justification (technical/operational rationale)
  - Organisational context documentation (Clause 4.1 - e.g., infrastructure architecture confirming no web browsing capability)
- **For Alternative Control**:
  - Control objective mapping (ISO 27001 Annex A objective vs. alternative implementation)
  - Effectiveness evidence (alternative control operates and achieves objective)
  - Approval record (CISO approval of alternative approach)

**Step 3: Collaborative Assessment**

Organisation and auditor assess:

1. **Is documented rationale reasonable given organisational context?**
   - Does rationale align with ISO 27001 Clause 4.1 (context understanding)?
   - Is decision documented and approved per Section 2.1 authority boundaries?
2. **Is there conflicting evidence?**
   - Does organisation claim "no EU data" but privacy policy mentions GDPR?
   - Does SoA claim "no logging requirement" but incident response plan references logs?
3. **Does interpretation satisfy ISO 27001 requirements?**
   - If control excluded, is ISO 27001 control objective genuinely not applicable?
   - If alternative control used, does it achieve same security outcome?

**Step 4: Resolution**

**Outcome A: Auditor Accepts Rationale**
- Documented rationale is reasonable and supported by evidence
- No conflicting information exists
- ISO 27001 requirements are satisfied
- **Result**: Applicability determination stands, no finding issued

**Outcome B: Organisation Acknowledges Gap**
- Auditor provides specific ISO 27001 clause or control objective not satisfied
- Organisation reviews and agrees determination was incorrect or insufficient
- **Result**: Organisation triggers corrective action per ISO 27001 Clause 10.2:
  - Root cause analysis (why was applicability incorrectly determined?)
  - Remediation (update POL-00, SoA, implement missing control, or reassess risk)
  - Verification (internal audit confirms correction implemented)
  - Timeline (corrective action plan with target completion date)

**Outcome C: Disagreement Persists**
- Organisation maintains rationale is sound, auditor maintains concern is valid
- Both parties have documented reasoning
- **Result**: Escalate to certification body technical review:
  - Organisation provides: Documented rationale, ISO 27001 clause alignment argument, evidence supporting determination
  - Auditor provides: Specific concern, ISO 27001 requirement potentially not satisfied, alternative interpretation
  - Certification body: Reviews both positions, issues technical ruling
  - Organisation: Accepts ruling (if against organisation → triggers corrective action per Outcome B)

**Principles**:

- **Evidence-Based**: Disagreements resolved through documented reasoning and ISO 27001 reference, not authority or seniority
- **Collaborative**: Goal is shared understanding of ISO 27001 requirements, not adversarial debate
- **Proportionate**: Minor clarifications handled in Step 2 (documentation exchange), major gaps escalate through formal process
- **Improvement-Oriented**: If applicability determination was genuinely incorrect, organisation learns and improves (Clause 10.1 continual improvement)

**Documentation of Challenge Protocol Execution**:

When challenge protocol is invoked:
- Document in audit findings log (even if resolved at Step 3 without formal finding)
- Record rationale provided and resolution outcome
- If corrective action triggered → Track in gap register per Clause 10.2
- Review during annual governance review (Section 6.1) - pattern of challenges may indicate systematic issue

## Exception Handling and Risk Acceptance

### Exception Scenarios

**Definition**: An exception occurs when an ISO 27001 Annex A control cannot be implemented as documented in the control policy (POL-A.X.XX), requiring alternative approach or risk acceptance.

**Common Exception Scenarios**:

| Scenario | Description | Example | Resolution Path |
|----------|-------------|---------|----------------|
| **Technical Infeasibility** | Control assumes technology/architecture not present in organisation | A.8.22 (Network segregation): Infrastructure is single flat network by design decision | Alternative Control: Implement host-based isolation, application-level access controls |
| **Disproportionate Cost** | Control cost exceeds risk reduction benefit given organisational scale | A.8.16 (SIEM deployment): 3-server infrastructure, manual log review achieves same objective at lower cost | Alternative Control: Documented manual log review process with defined frequency |
| **Risk Already Mitigated** | Alternative implementation achieves same ISO 27001 control objective | A.8.5 (MFA for all accounts): Service accounts use certificate-based authentication (functionally equivalent to MFA) | Alternative Control: Certificate authentication documented as MFA equivalent |
| **Regulatory Conflict** | Control implementation would violate higher-priority legal requirement (rare) | A.8.10 (Data deletion): GDPR requires deletion, but Swiss law requires 10-year retention for financial records | Risk Acceptance: Document legal obligation supersedes control, implement data segregation to minimise scope |
| **Resource Constraint** | Organisation lacks capacity to implement control fully (temporary state) | A.6.3 (Annual security training): Training program designed but not yet delivered to all staff | Deferred Implementation: Control scheduled for completion within [timeline], interim measures documented |

**Not Valid Exception Scenarios**:
- "We didn't know about this requirement" → Training gap, not exception (address through awareness)
- "It's too difficult" → Resource planning issue, not exception (schedule implementation or accept risk formally)
- "Our previous auditor didn't require this" → Audit interpretation variance, not exception (ISO 27001 requirements haven't changed)

### Exception Process

**Mandatory Process** (per ISO 27001 Clause 6.1.3 Risk Treatment):

All exceptions **shall** follow this 5-step process:

**Step 1: Document Reason**

Provide clear explanation:
- **Technical Explanation**: Why control cannot be implemented as written (technology limitation, architecture constraint, operational incompatibility)
- **Impact Assessment**: What security objective is not fully achieved (which part of ISO 27001 control objective is affected)
- **Context Justification**: Why this limitation exists (business decision, regulatory constraint, cost-benefit analysis)

Documentation format: Exception request form or SoA justification entry

**Step 2: Assess Residual Risk** (ISO 27001 Clause 6.1.2)

Quantify risk without control:
- **Likelihood**: Probability threat will exploit vulnerability (Low/Medium/High or numeric scale per organisation's risk methodology)
- **Impact**: Consequence if threat materialises (Confidentiality/Integrity/Availability impact, financial/reputational/operational impact)
- **Residual Risk Level**: Combined risk rating per organisation's risk assessment methodology
- **Risk Appetite Comparison**: Is residual risk within acceptable risk appetite? (per risk treatment plan criteria)

Documentation: Risk assessment entry linked to exception, residual risk calculation

**Step 3: Propose Solution**

Select one of three paths:

**Option A: Alternative Control**
- Implement different control achieving same ISO 27001 control objective
- Document: Control objective mapping (ISO 27001 Annex A objective → alternative implementation)
- Document: Effectiveness evidence (how alternative control operates and achieves objective)
- Example: A.7.4 (Physical monitoring) → Colocation provider CCTV instead of self-operated cameras

**Option B: Risk Acceptance** (ISO 27001 Clause 6.1.3d)
- Accept residual risk without additional mitigation
- Requires: Risk is within acceptable risk appetite AND Executive Management approval
- Document: Risk acceptance justification, compensating controls (if any), review timeline
- Example: A.8.11 (Data masking) not implemented, residual risk accepted with access controls as compensating measure

**Option C: Deferred Implementation**
- Control scheduled for future implementation (temporary exception)
- Requires: Implementation timeline documented, interim measures defined, periodic review
- Document: Target completion date, interim risk mitigation, progress tracking
- Example: A.6.3 (Security training) program under development, targeted completion Q2 2025, interim: security awareness emails

**Step 4: Obtain Approval** (per Section 2.1 Authority Boundaries)

Authority required based on solution:

| Solution | Approval Authority | Evidence Required |
|----------|-------------------|-------------------|
| **Alternative Control** | CISO | Control objective mapping, effectiveness documentation, technical feasibility assessment |
| **Risk Acceptance** | Executive Management (CEO/CFO) | Risk assessment showing residual risk, justification for acceptance, compensating controls documentation |
| **Deferred Implementation** | CISO (timeline) + Executive Management (residual risk during deferral period) | Implementation plan, interim measures, resource allocation commitment |

Documentation: Approval signature on exception request or Risk Acceptance Register entry

**Step 5: Document in Statement of Applicability**

Update SoA with:
- **Control Status**: "Alternative Control" or "Risk Accepted" or "Implementation Deferred"
- **Justification**: Summary of Steps 1-3 (reason, risk, solution)
- **Approval**: Reference to approval authority and date (Step 4)
- **Review**: Next review date (annual minimum, or per deferred implementation timeline)

Example SoA entry:

Control A.8.22 (Network Segregation)
Status: Alternative Control
Justification: Infrastructure is single flat network by design (cloud-native architecture with application-level isolation).
Alternative: Host-based firewall rules + Kubernetes network policies achieve same objective (prevent unauthorised lateral movement).
Approved By: CISO [Name], [Date]
Next Review: [Date + 12 months]
Reference: POL-A.8.22 Section 6 (Alternative Implementation), IMP-A.8.22 (Network Policy Configuration)

### Exception Register

**Purpose**: Centralised tracking of all exceptions to control implementation.

**Maintained By**: CISO (owner), updated as exceptions are processed

**Contents**:

| Field | Description | Example |
|-------|-------------|---------|
| Exception ID | Unique identifier | EXC-2025-001 |
| Control | Annex A control reference | A.8.22 (Network Segregation) |
| Reason | Why exception required (Step 1) | Infrastructure is single flat network by design |
| Residual Risk | Risk level without control (Step 2) | Medium (Likelihood: Low, Impact: High) |
| Solution | Alternative control / Risk acceptance / Deferred (Step 3) | Alternative Control: Kubernetes network policies |
| Approved By | Authority per Section 2.1 (Step 4) | CISO [Name] |
| Approval Date | Date of approval | 2025-01-15 |
| Review Date | Next exception review date | 2026-01-15 (annual) |
| Status | Open / Resolved / Closed | Open (alternative control implemented) |

**Review Cycle**:
- **Quarterly**: CISO reviews open exceptions, assesses whether resolution is progressing (deferred implementations on track)
- **Annually**: All exceptions reviewed during management review (Section 6.1), assess exception volume trend

**Closure Criteria**:
- **Alternative Control**: Control implemented and verified effective → Status: Closed
- **Risk Acceptance**: Risk reviewed annually, remains acceptable → Status: Open (ongoing acceptance)
- **Deferred Implementation**: Control implemented per timeline → Status: Resolved, exception removed from SoA

**Location**: Exception Register maintained in [GRC Platform / Compliance Register / Document Management System path]

### Exception Volume Monitoring

**Purpose**: Exception volume is a governance health metric. High exception volume indicates systematic issues (resource constraints, architecture mismatch with ISO 27001, unrealistic control expectations).

**Metrics**:

| Metric | Target | Escalation Threshold | Action if Threshold Exceeded |
|--------|--------|---------------------|----------------------------|
| **Total Exceptions** | <5% of total controls (4-5 exceptions out of 93 controls) | >10% (10+ exceptions) | Executive Management review: Is ISMS scope realistic? Are resources sufficient? Is architecture fundamentally incompatible with ISO 27001? |
| **Risk Acceptances** (no alternative control) | <3% of total controls (2-3 risk acceptances) | >5% (5+ risk acceptances) | Risk appetite reassessment: Is organisation accepting too much residual risk? Should certification scope be narrowed? |
| **Deferred Implementations** | <2% of total controls (1-2 deferrals) | >5% (5+ deferrals) or any deferral >180 days overdue | Resource allocation review: Are implementation timelines realistic? Are deferrals becoming permanent (indicating hidden risk acceptance)? |
| **Exceptions Pending >90 Days** | 0 (all exceptions resolved within 90 days of identification) | Any exception unresolved >90 days without approved extension | Escalate to Executive Management: Why is exception unresolved? Is this operational delay or systematic issue? |

**Review Frequency**:
- **Quarterly**: CISO reports exception metrics during ISMS review meeting
- **Annually**: Exception volume trend analysis during management review (Section 6.1), comparison to previous year

**Rationale**: Low exception volume (<5%) indicates:
- Controls are well-matched to organisational context (good scoping)
- Implementation is feasible with available resources
- Risk acceptance is used sparingly (not as avoidance mechanism)

High exception volume (>10%) indicates systematic problem requiring strategic intervention (scope adjustment, resource increase, architecture redesign, or risk appetite realignment).

### Auditor Interaction on Exceptions

**Auditor Verification Focus**:

Auditor verifies:
1. **Process Compliance**: Was exception processed per Section 4.2 (5-step process documented, approvals obtained)?
2. **Residual Risk Assessment**: Is risk assessment reasonable? (Step 2 completed, risk quantified per organisation's methodology)
3. **Alternative Control Effectiveness**: If alternative control used, does it achieve ISO 27001 control objective? (Step 3 mapping is sound)
4. **Approval Authority**: Are approvals from correct authority per Section 2.1? (Alternative control: CISO, Risk acceptance: Executive Management)
5. **Exception Volume**: Is exception volume within healthy range (<5%), or does high volume indicate systematic issue?

**Auditor Does NOT**:
- Dictate which solution (alternative control vs. risk acceptance vs. deferred) organisation must choose (organisation's risk-based decision per Clause 6.1.3)
- Reject risk acceptance based on personal risk appetite (Executive Management decides risk appetite, auditor verifies process and reasonableness)
- Require "gold standard" implementations (proportionality is acceptable - controls must be effective given context, not perfect)

**If Auditor Challenges Exception**:

Auditor concern typically falls into one of these categories:

| Concern Type | Organisation Response | Resolution |
|--------------|----------------------|------------|
| **Process not followed** | Acknowledge gap, provide evidence of approval (if exists) or retroactively complete Step 4 approval | If process violation confirmed → Corrective action per Clause 10.2 (document why process bypassed, prevent recurrence) |
| **Residual risk appears high** | Provide risk assessment detail (Step 2), explain why residual risk is acceptable per organisation's risk appetite | If auditor has specific ISO 27001 concern → Challenge Protocol (Section 3.3), focus on whether control objective is satisfied |
| **Alternative control doesn't achieve objective** | Provide control objective mapping (Step 3), demonstrate effectiveness with evidence | If gap confirmed → Implement additional measures or accept residual risk formally (triggers Step 2-4 re-execution) |
| **Approval authority incorrect** | Verify approval signature, escalate to correct authority if needed | If approval missing/incorrect → Obtain correct approval retroactively (CISO for alternative control, Executive Management for risk acceptance) |

**Escalation**: If exception handling dispute cannot be resolved through documentation and reasoning → Challenge Protocol (Section 3.3) applies.

---

## Compliance Criteria Change Control

### Change Triggers

**Purpose**: Compliance criteria (what we must comply with, how we demonstrate compliance) evolve over time due to external and internal factors. This section establishes when and how compliance criteria changes are identified and managed.

**External Change Triggers**:

| Trigger Category | Description | Examples | Detection Method |
|-----------------|-------------|----------|------------------|
| **Regulatory Changes** | New laws, regulations, or official guidance affecting ISMS requirements | GDPR implementing acts, ISO 27001 amendments, nDSG guidance updates, NIS2 national transposition | POL-00 quarterly monitoring (Section 4.3), legal counsel alerts, regulatory authority subscriptions |
| **Standard Revisions** | ISO 27001 or related standards updated (corrigenda, new versions) | ISO 27001:2022 → potential future ISO 27001:202X, ISO 27002 guidance updates | ISO publication monitoring, certification body notifications |
| **Contract Changes** | Customer contracts add new security requirements or regulatory obligations | New customer requires SOC 2 Type II, PCI DSS scope expansion, contractual SLA changes | Contract review process (legal + CISO review before signature) |
| **Threat Landscape Evolution** | New attack classes emerge requiring control updates | Ransomware targeting backups → A.8.13 (Backup) requires offline/immutable copies, supply chain attacks → A.5.19-23 enhanced scrutiny | Threat intelligence monitoring (A.5.7), incident trend analysis, industry security bulletins |
| **Technology Changes** | Infrastructure or architecture shifts affecting control implementation | Cloud migration → A.5.23 (Cloud services) now applicable, legacy system retirement → A.8.19 (Software installation) scope reduced | IT change management process, architecture review board decisions |

**Internal Change Triggers**:

| Trigger Category | Description | Examples | Detection Method |
|-----------------|-------------|----------|------------------|
| **Audit Findings** | External auditor identifies control gap or interpretation issue | Stage 2 finding: "Logging retention insufficient for A.8.15 objective", surveillance audit: "Alternative control for A.7.4 not achieving objective" | Audit findings log (Clause 10.2), audit report review |
| **Internal Audit Discoveries** | Internal audit (Clause 9.2) identifies nonconformity or improvement opportunity | Internal audit: "Exception approval missing Executive Management signature", control effectiveness testing reveals gap | Internal audit reports, nonconformity register |
| **Security Incidents** | Incident response reveals control weakness requiring policy/implementation update | Incident: Phishing attack successful → A.6.3 (Training) frequency increased, incident: Unauthorised access → A.5.18 (Access rights) review process tightened | Incident response process (A.5.24-28), lessons learned (Section 6.2) |
| **Management Review** | Clause 9.3 management review identifies strategic improvement or risk appetite change | Management review: "Accept higher residual risk for low-impact controls", "Increase automation to reduce manual verification burden" | Management review meeting minutes (Clause 9.3.3), continual improvement actions |
| **Continuous Improvement** | Proactive identification of efficiency gains, automation opportunities, or enhanced security measures | CISO proposal: "Automate A.8.15 log analysis with SIEM", "Enhance A.8.24 cryptography to post-quantum algorithms proactively" | ISMS review meetings, technology evaluation, benchmarking against industry practices |

**Trigger Event Documentation**:

All change triggers **shall** be documented in **Change Trigger Log**:
- Date trigger identified
- Trigger category (external/internal per tables above)
- Description of change required
- Affected policies/controls
- Assessment status (under review, approved, implemented, verified)

**Location**: Change Trigger Log maintained in [GRC Platform / Compliance Register / Change Management System]

---

### Change Assessment and Implementation Process

**Mandatory 6-Step Process**:

All compliance criteria changes **shall** follow this process:

**Step 1: Change Identified**

Trigger event detected per Section 5.1 sources:
- Quarterly POL-00 regulatory monitoring (Legal/Compliance reviews)
- Internal audit findings (Clause 9.2)
- Management review decisions (Clause 9.3)
- Incident response lessons learned (Section 6.2)
- Ad-hoc trigger event (customer contract, threat intelligence, technology change)

**Responsible**: CISO (coordinates assessment), Legal/Compliance (regulatory changes), Internal Audit (audit findings)

**Output**: Change Trigger Log entry documenting trigger event

---

**Step 2: Impact Assessed**

Evaluate change scope and implications:

**Assessment Questions**:
1. **Which policies/controls are affected?**
   - Direct impact: Which POL/IMP documents must be updated? (e.g., GDPR encryption guidance update affects POL-A.8.24)
   - Indirect impact: Which related controls require reassessment? (e.g., A.8.24 change may affect A.8.10 deletion, A.8.13 backup encryption)

2. **What compliance gap exists?**
   - Current state: What does current implementation provide? (e.g., AES-128 encryption)
   - Required state: What does new requirement mandate? (e.g., AES-256 minimum per updated GDPR guidance)
   - Gap: Specific difference between current and required (e.g., key length insufficient, must upgrade)

3. **What remediation is required?**
   - Policy updates: Which POL documents require revision? (version change, requirement text updates)
   - Technical changes: Infrastructure upgrades, configuration changes, new tools/systems
   - Evidence regeneration: Python workbooks, logs, verification procedures updated to match new criteria
   - Timeline: How long will remediation take? (hours, weeks, months)

4. **What is risk during transition?**
   - If change implementation takes time (e.g., 3 months to upgrade encryption), what is residual risk during transition?
   - Are interim measures needed? (temporary controls, monitoring, restrictions)

**Responsible**: CISO (technical assessment), Legal/Compliance (regulatory impact), affected Control Owners (implementation feasibility)

**Output**: Change Impact Assessment document covering above questions

---

**Step 3: Change Proposal Documented**

Formalise change recommendation:

**Change Proposal Contents**:
1. **Rationale**: Why change is needed (regulatory requirement, threat evolution, audit finding, improvement opportunity)
2. **Affected Controls**: List of Annex A controls requiring update (POL/IMP/Python changes)
3. **Implementation Plan**:
   - Technical tasks: Infrastructure changes, configuration updates, tool deployments
   - Documentation tasks: POL/IMP updates, SoA revisions, evidence mechanism adjustments
   - Timeline: Target completion date, milestones if phased implementation
   - Resources: Personnel, budget, external support (consultants, vendors) if needed
4. **Risk During Transition**: Assessment from Step 2, interim measures if applicable
5. **Verification Plan**: How will change implementation be confirmed? (internal audit scope, evidence review, testing)

**Responsible**: CISO (proposal author), Control Owners (implementation detail)

**Output**: Change Proposal document or GRC platform change request entry

---

**Step 4: Approval Obtained** (per Section 2.1 Authority Boundaries)

Authority required based on change type:

| Change Type | Approval Authority | Approval Criteria |
|-------------|-------------------|-------------------|
| **Technical Changes** (control implementation, evidence format) | CISO | Change is technically sound, resources available, timeline realistic |
| **Regulatory Changes** (Tier 1/2 applicability shift) | CISO + Legal/Compliance (joint) | Regulatory interpretation is correct, compliance approach satisfies requirement |
| **Strategic Changes** (ISMS scope expansion, major architecture shift) | Executive Management | Resource allocation approved, risk appetite alignment confirmed, certification timeline acceptable |
| **Emergency Changes** (critical security vulnerability, regulatory deadline) | CISO (implement immediately) + Executive Management (retroactive approval within 7 days) | Urgency justified, risk of not implementing exceeds risk of expedited implementation |

**Approval Evidence**: Signature on Change Proposal, meeting minutes documenting approval decision, email approval (for routine technical changes)

**Responsible**: Per authority table above

**Output**: Approved Change Proposal with signature/approval record

---

**Step 5: Implementation Executed**

Execute change per implementation plan (Step 3):

**Policy Updates** (ISO 27001 Clause 7.5.3 Document Control):
- Update POL document with new requirements (version increment per Section 5.3)
- Update IMP document if implementation approach changes
- Update Python scripts if evidence generation logic changes
- Regenerate assessment workbooks to match new criteria
- Document version change in policy header "Version History" table

**Control Reassessment**:
- Review affected controls against new requirements
- Conduct gap analysis: Does current implementation satisfy new requirement? (Yes/No/Partial)
- If gap identified → Implement remediation (technical changes, configuration updates)
- If no gap → Document confirmation that existing implementation satisfies new requirement

**Evidence Regeneration**:
- Run updated Python workbooks to generate new evidence baseline
- Review generated evidence for completeness (no #REF! errors, formulas calculating correctly)
- Verify evidence demonstrates compliance with updated requirements

**Change Log Update** (Section 5.3):
- Record change in document control system or policy change log
- Note: Date of change, author, summary of changes, approval authority
- Archive previous version (audit trail for "what did we comply with before this change?")

**Responsible**: CISO (coordinates), Control Owners (execute technical changes), Policy Authors (document updates)

**Output**: Updated policies/controls, regenerated evidence, change log entries

---

**Step 6: Verification Completed**

Confirm change implemented correctly:

**Internal Audit Verification** (ISO 27001 Clause 9.2):
- Add changed controls to next internal audit scope (verify new requirements are met)
- Conduct evidence review: Does regenerated evidence demonstrate compliance with new criteria?
- Test control effectiveness: Do technical changes achieve intended security objective?

**Gap Closure**:
- If change was triggered by gap (audit finding, incident), verify gap is closed
- Update gap register: Mark gap "Resolved", document verification date and method
- If gap remains partially unresolved → Document residual gap, plan additional remediation

**Management Review** (ISO 27001 Clause 9.3):
- Report change implementation to management review (Clause 9.3.2 input: changes to ISMS)
- Assess change effectiveness: Did change achieve intended improvement?
- Identify lessons learned: What went well? What could improve in future changes?

**Responsible**: Internal Audit (verification), CISO (gap closure confirmation), Executive Management (review)

**Output**: Internal audit report covering changed controls, gap register updates, management review record

---

### Version Control and Change Tracking

**Document Versioning Standard**:

All ISMS policies **shall** follow standardised versioning:

**Version Format**: `v[Major].[Minor]`

**Version Increment Rules**:

| Change Type | Version Increment | Example | Trigger |
|-------------|------------------|---------|---------|
| **Major Version** | Increment major number, reset minor to 0 | v1.3 → v2.0 | Significant requirement change affecting compliance assessment (new control added, requirement tightened, standard revised) |
| **Minor Version** | Increment minor number | v1.3 → v1.4 | Clarification, formatting, or non-substantive change (typo correction, cross-reference update, example added) |

**Major Version Triggers** (examples):
- Regulatory requirement change (GDPR guidance mandates AES-256, previously AES-128 acceptable)
- ISO 27001 standard amendment (new Annex A control added or objective clarified)
- Control implementation approach change (manual process → automated, alternative control adopted)
- Audit finding remediation that changes control requirements

**Minor Version Triggers** (examples):
- Clarification of existing requirement (adding example to existing "shall" statement without changing requirement)
- Cross-reference correction (updating POL-00 section reference after POL-00 restructure)
- Formatting improvement (table layout, section numbering)
- Placeholder completion (filling in [Organisation Name], [Date] fields - no substantive change)

**Version History Documentation**:

All policy documents **shall** maintain version history table in Document Control section:

```markdown
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | CISO | Initial approved release |
| 1.1 | 2024-03-20 | CISO | Clarified evidence retention period (Section 7), no requirement change |
| 2.0 | 2024-09-10 | CISO | Updated encryption minimum to AES-256 per GDPR guidance (Section 4.2), major requirement change |
```

**Change Summary Requirements**:
- **Major version**: Detailed change description (what requirement changed, why, regulatory reference if applicable)
- **Minor version**: Brief change description (what was clarified, no impact on compliance assessment)

---

**Central Change Log**:

In addition to individual policy version histories, organisation **shall** maintain central **ISMS Change Log**:

**Purpose**: Single source of truth for all compliance criteria changes across entire ISMS (not just individual policies)

**Contents**:

| Field | Description | Example |
|-------|-------------|---------|
| Change ID | Unique identifier | CHG-2024-015 |
| Change Date | Date change implemented | 2024-09-10 |
| Trigger | What triggered change (per Section 5.1) | GDPR guidance update (external regulatory change) |
| Affected Policies/Controls | Which documents updated | POL-A.8.24 v1.5 → v2.0, IMP-A.8.24 v1.2 → v2.0 |
| Change Summary | Brief description of change | Encryption minimum updated from AES-128 to AES-256 |
| Rationale | Why change was necessary | GDPR guidance now requires AES-256 minimum for personal data protection |
| Approval | Authority who approved (per Section 2.1) | CISO + Legal/Compliance (regulatory change) |
| Verification Status | Is change verified effective? (Step 6) | Verified - Internal audit Q4 2024 confirmed AES-256 deployment |

**Review**: Central change log reviewed during:
- Surveillance audits (auditor assesses change volume and verification completeness)
- Management review (Clause 9.3 - changes to ISMS reported as input per Clause 9.3.2)
- Annual governance review (Section 6.1 - change management effectiveness assessed)

**Location**: ISMS Change Log maintained in [GRC Platform / Document Management System / Compliance Register path]

---

### Reassessment Tracking

**Purpose**: When compliance criteria change, affected controls must be reassessed to confirm they meet new requirements. This section establishes reassessment tracking and completion monitoring.

**Reassessment Requirements**:

When compliance criteria change (per Section 5.2 implementation):

1. **Gap Analysis**: Compare current implementation to new requirements (Step 2 impact assessment)
2. **Remediation**: Implement changes to close gap (Step 5 technical changes, policy updates)
3. **Verification**: Confirm new requirements are met (Step 6 internal audit, evidence review)
4. **Timeline**: Complete reassessment within **90 days** of change identification (extendable to 180 days with Executive Management approval for complex changes)

**Reassessment Tracking**:

Reassessment progress **shall** be tracked in **Gap Register** or GRC platform:

| Field | Description | Example |
|-------|-------------|---------|
| Gap ID | Linked to Change ID | GAP-2024-042 (linked to CHG-2024-015) |
| Control | Affected Annex A control | A.8.24 (Use of Cryptography) |
| Gap Description | What doesn't meet new requirement | Current implementation uses AES-128, new requirement is AES-256 minimum |
| Owner | Responsible for remediation | Infrastructure Team Lead |
| Target Closure | Remediation deadline | 2024-12-10 (90 days from 2024-09-10 change date) |
| Status | Current state | In Progress (encryption upgrade 60% complete) |
| Verification | How closure will be confirmed | Internal audit evidence review + Python workbook regeneration |

**Reassessment Completion Metrics**:

| Metric | Target | Escalation Threshold |
|--------|--------|---------------------|
| **Reassessment completion rate** | >95% within 90 days | <80% → Executive Management review (resource constraints? complexity underestimated?) |
| **Overdue reassessments** | 0 items >90 days overdue | Any item >90 days overdue without approved extension → Escalate to Executive Management |
| **Failed verifications** | <5% (reassessment implemented but verification fails) | >10% failed verifications → Process review (are impact assessments accurate? implementation quality issue?) |

**Reviewed**: Quarterly during ISMS review meeting, reported in management review (Clause 9.3)

---

### Compliance Model Currency Verification

**Purpose**: Demonstrate compliance model remains current (not static snapshot from Year 1 certification).

**Currency Indicators**:

The organisation demonstrates compliance model currency through:

**1. Regulatory Monitoring Activity** (POL-00 Section 4.3):
- **Evidence**: Quarterly monitoring logs showing regulatory landscape review
- **Content**: Regulatory changes detected (or "no changes detected"), trigger assessments, actions taken
- **Expectation**: Logs exist for every quarter, signed by Legal/Compliance + CISO

**2. Standard Update Monitoring**:
- **Activity**: Monitor ISO 27001 amendments, corrigenda, new guidance publications
- **Sources**: ISO publication database, certification body notifications, ISMS consultant newsletters
- **Assessment**: Does change affect Annex A control interpretation or certification requirements?
- **Timeline**: Assess impact within 30 days of publication, implement updates within 6 months if substantive

**3. Threat Landscape Evolution**:
- **Activity**: Incorporate lessons learned from security incidents (Section 6.2), threat intelligence (A.5.7), industry trend analysis
- **Assessment**: Do emerging threats require control updates? (e.g., ransomware targeting backups → A.8.13 offline/immutable requirement)
- **Update Triggers**: Significant incident affecting organisation, industry-wide threat pattern, technology vulnerability (Log4j, supply chain attacks)

**4. Change Log Population**:
- **Evidence**: ISMS Change Log (Section 5.3) has entries showing model evolution over time
- **Expectation**: At least 2-4 changes per year (mix of external regulatory changes, internal improvements)
- **Red Flag**: Empty change log for >12 months suggests model is static (no evolution)

**Auditor Verification**:

During surveillance audits, auditor reviews:
- Change log: Are changes documented? Is change process (Section 5.2) followed?
- Quarterly monitoring records: Is regulatory landscape actively monitored?
- Reassessment completion: Are changed controls verified effective? (Step 6 completed)
- Currency indicators: Does evidence show model is evolving, not dormant?

**Outcome**: Auditor confirms compliance model is current relative to regulatory landscape, threat environment, and organisational context. Model evolution demonstrates continual improvement (Clause 10.1).

---

## Governance Effectiveness Monitoring

### Annual Governance Review

**Frequency**: Annually (aligned with ISO 27001 Clause 9.3 Management Review)

**Timing**: Q4 of each year (or as scheduled in management review calendar)

**Participants**:
- Executive Management (CEO/CFO - decision authority)
- CISO (governance owner, presents findings)
- Legal/Compliance Officer (regulatory assessment)
- Internal Audit (process verification perspective)
- Representative Control Owners (operational insight)

**Purpose**: Assess whether governance processes defined in this policy are effective, identify improvement opportunities, and ensure decision-making authority structure remains appropriate.

---

**Review Topics**:

**1. Authority Boundaries (Section 2.1)**

**Assessment Questions**:
- Are roles and responsibilities clearly understood? (confusion incidents, unauthorised decisions)
- Are escalation processes working? (decisions reaching correct authority level, timely approvals)
- Do disputes require process improvement? (Section 3.3 Challenge Protocol invoked frequently? Pattern of disagreements?)
- Is competence maintained? (Section 2.3 - certifications current, training up-to-date, external counsel engaged appropriately)

**Metrics to Review**:
- Number of decisions made outside designated authority (should be 0, or retroactively approved)
- Average approval time by authority level (CISO: target <7 days, Executive Management: target <14 days)
- Competence verification status (all decision-makers meet Section 2.3 requirements)

**Output**: Confirmation authority structure is effective, or recommendations for adjustment (role clarification, competence development, escalation process improvement)

---

**2. Applicability Framework (Section 3)**

**Assessment Questions**:
- Is POL-00 Tier 1/2/3 framework effective? (applicability determinations clear and defensible)
- Are conditional regulation triggers monitored appropriately? (quarterly monitoring per POL-00 Section 4.3 executed consistently)
- Are SoA justifications sufficient? (audit feedback on control exclusions, alternative controls)
- Challenge Protocol usage? (Section 3.3 invoked? How many times? Outcomes?)

**Metrics to Review**:
- POL-00 quarterly monitoring completion rate (target: 100% - 4 quarters reviewed)
- Triggered assessments completed (business changes, regulatory updates assessed per POL-00 Section 5)
- SoA completeness (all 93 controls documented with justification)
- Applicability challenges by auditors (count, resolution outcomes per Section 3.3)

**Output**: Confirmation applicability framework is operating effectively, or recommendations for POL-00 updates, SoA clarification, monitoring process improvement

---

**3. Exception Handling (Section 4)**

**Assessment Questions**:
- How many exceptions processed in past year? (total count, breakdown by type: alternative control, risk acceptance, deferred implementation)
- Are exceptions trending up (systematic issue) or stable? (increasing exceptions may indicate resource constraints, architecture mismatch)
- Are risk acceptances appropriate, or do they indicate resource constraints? (Executive Management review of risk acceptance justifications)
- Exception process compliance? (all exceptions followed 5-step process per Section 4.2)

**Metrics to Review**:
- Exception volume (Section 4.4 targets):
  - Total exceptions: <5% of controls (target: 4-5 exceptions, escalation threshold: >10%)
  - Risk acceptances: <3% of controls (target: 2-3, escalation threshold: >5%)
  - Deferred implementations: <2% of controls (target: 1-2, escalation threshold: >5%)
  - Overdue exceptions: 0 items >90 days (escalation: any >90 days)
- Exception process compliance: 100% followed 5-step process (audit Step 4 approvals obtained)
- Exception closure rate: >80% of deferred implementations completed within timeline

**Output**: Exception volume assessment (healthy or requires strategic intervention), process compliance confirmation, recommendations for resource allocation or scope adjustment if volume exceeds thresholds

---

**4. Change Management (Section 5)**

**Assessment Questions**:
- How many compliance criteria changes in past year? (change log volume, change types per Section 5.1)
- What is reassessment completion rate? (target: >95% within 90 days per Section 5.4)
- Are changes proactive (regulatory monitoring) or reactive (audit findings)? (maturity indicator - proactive is preferable)
- Change process compliance? (all changes followed 6-step process per Section 5.2)

**Metrics to Review**:
- Change volume and breakdown:
  - External triggers (regulatory, standard revisions, contract, threat, technology): count per category
  - Internal triggers (audit findings, incidents, management review, continuous improvement): count per category
  - Change type mix: Major versions (requirement changes) vs. minor versions (clarifications)
- Reassessment completion (Section 5.4 targets):
  - Completion rate within 90 days: >95%
  - Overdue reassessments: 0 items >90 days overdue
  - Failed verifications: <5%
- Change process compliance: 100% followed 6-step process (Step 4 approvals, Step 6 verification completed)

**Output**: Change management effectiveness assessment, reassessment tracking performance, recommendations for process improvement if metrics below targets

---

**5. Auditor Feedback**

**Assessment Questions**:
- What did external auditors comment on governance? (audit report findings, observations, recommendations)
- Were any interpretations challenged? (Section 3.3 Challenge Protocol usage by auditors)
- How were challenges resolved? (outcomes per Section 3.3: accepted rationale, acknowledged gap, escalated to certification body)
- Are auditor interactions improving (fewer disputes) or degrading? (increasing challenges may indicate communication gap or interpretation drift)

**Metrics to Review**:
- Governance-related audit findings: count by severity (Critical, High, Medium, Low per SSE review methodology)
- Challenge Protocol invocations: count, outcomes (rationale accepted, gap acknowledged, certification body escalation)
- Audit preparation effectiveness: time to assemble documentation package (Section 3.2, target: <5 days)
- Auditor feedback on ISMS structure: qualitative assessment (positive comments, areas for improvement)

**Output**: Audit relationship assessment, identification of recurring auditor concerns (may indicate documentation gap or interpretation difference requiring clarification), recommendations for audit preparation or communication improvements

---

**6. Governance Efficiency**

**Assessment Questions**:
- Are governance processes efficient? (time to obtain approvals, decision-making speed)
- Are there bureaucratic bottlenecks? (approvals delayed, decisions stuck in escalation)
- Can processes be streamlined without reducing control quality? (automation opportunities, delegation where appropriate)

**Metrics to Review**:
- Average decision approval time by authority level (CISO, Legal/Compliance, Executive Management)
- Exception processing time: trigger to closure (target: <90 days per Section 4.4)
- Change implementation time: identification to verification (target: 90 days per Section 5.4)
- Governance meeting frequency and duration (are reviews consuming excessive time?)

**Output**: Process efficiency assessment, recommendations for streamlining (delegation, automation, approval workflow optimisation)

---

**Annual Governance Review Outputs**:

1. **Governance Health Report**: Document covering above 6 topics with metrics, trends, findings
2. **Continual Improvement Actions**: Specific actions to improve governance effectiveness (process updates, training, tool deployment)
3. **Policy Updates**: If review identifies governance process gaps → Update POL-GOVERNANCE (this policy) per Section 5.2 change process
4. **Management Review Record**: Governance review incorporated into Clause 9.3 management review as input (Clause 9.3.2: results of audits, changes to ISMS)

**Approval**: Executive Management approves governance health report and continual improvement actions

**Documentation**: Meeting minutes, governance health report, action register

**Next Review**: Scheduled for Q4 [Year+1]

---

### Lessons Learned Register

**Purpose**: Capture improvements from governance process execution, enabling continual improvement (ISO 27001 Clause 10.1)

**Maintained By**: CISO (updates quarterly or when lesson learned identified)

**Update Triggers**:
- Governance process executed with unexpected outcome (exception approval delayed, change verification failed)
- Auditor challenge reveals documentation gap or communication issue
- Internal feedback from control owners (process unclear, approval bottleneck)
- Best practice identified from external sources (industry guidance, peer benchmarking)

**Register Contents**:

| Date | Event | Lesson Learned | Action Taken | Status | Verified |
|------|-------|----------------|--------------|--------|----------|
| Q1 2025 | Auditor challenged A.8.15 interpretation (Section 3.3 invoked) | Provide more explicit rationale in SoA justifications - auditor needed specific ISO 27001 control objective mapping | Enhanced SoA template: added mandatory "ISO 27001 Objective Mapping" field for all "Not Applicable" controls | Implemented | Internal Audit Q2 2025 confirmed SoA updates |
| Q2 2025 | Exception approval delayed 30 days (Executive Management unavailable during approval cycle) | Establish backup approval authority for urgent exceptions to prevent delays | Updated Section 4.2: CFO can approve risk acceptances in CEO absence, documented in exception register | Implemented | Policy updated v1.2, approval workflow tested Q3 2025 |
| Q3 2025 | Change reassessment missed 90-day target (gap register tracking manual, reminder missed) | Improve gap register tracking with automated reminders | Integrated gap register with GRC platform, configured weekly email reminders for items approaching 90-day deadline | In Progress | GRC platform deployment 80% complete, target Q4 2025 |
| Q4 2025 | Quarterly POL-00 monitoring skipped Q3 (Legal/Compliance resource constraint) | Build monitoring redundancy - CISO can conduct interim monitoring if Legal unavailable | Updated POL-00 Section 4.3: CISO authorised to conduct monitoring with Legal/Compliance review when available, documented in monitoring log | Planned | POL-00 update drafted, pending Legal approval |

**Review Frequency**:
- **Quarterly**: CISO reviews register during ISMS review meeting, assesses action status
- **Annually**: Lessons learned incorporated into annual governance review (Section 6.1), inform policy updates and continual improvement

**Integration with Annual Review**:
Lessons learned register feeds Section 6.1 annual governance review:
- Common themes? (multiple lessons in same category indicate systematic issue)
- Actions completed? (verify "Status: Implemented" items actually improved process)
- Effectiveness? (did action solve problem, or did issue recur?)

**Location**: Lessons Learned Register maintained in [GRC Platform / Compliance Register / Document Management System path]

---

## Integration with ISMS Processes

**Purpose**: This section clarifies how POL-GOVERNANCE integrates with core ISO 27001 processes (Clauses 6, 9.2, 9.3, 10.2) without duplicating process documentation.

### Risk Assessment and Treatment (Clause 6)

**Integration Points**:

- **Clause 6.1.2 (Risk Assessment)**: Risk assessment methodology informs control selection decisions (documented in SoA per Section 3.2)
- **Clause 6.1.3 (Risk Treatment)**: Risk treatment plan documents control implementation approach, alternative controls (Section 4.2), and risk acceptances (Section 4.2 Step 3 Option B)
- **Governance Authority** (Section 2.1): CISO proposes risk treatment, Executive Management approves risk acceptance per Clause 6.1.3d

**Exception Handling Connection** (Section 4):
- Controls that cannot be implemented trigger risk treatment process (Clause 6.1.3)
- Risk acceptance requires Executive Management approval (Section 2.1, documented in Risk Acceptance Register)
- Auditor verifies risk treatment process followed, does not substitute judgment on risk acceptance decision (Section 4.5)

**Reference**: Risk Treatment Plan (separate document, not duplicated in this policy)

---

### Internal Audit (Clause 9.2)

**Integration Points**:

- **Internal Audit Programme**: Includes verification of governance process compliance:
  - Are applicability decisions documented per Section 3? (POL-00 quarterly monitoring, SoA justifications)
  - Are exceptions processed per Section 4? (5-step process followed, approvals obtained)
  - Are changes controlled per Section 5? (6-step process followed, reassessments completed)

- **Pre-Audit Verification**: Internal audits conducted before external audits verify:
  - Governance documentation is current (POL-GOVERNANCE, POL-00, SoA, Risk Acceptance Register)
  - Change logs are complete (Section 5.3 ISMS Change Log populated)
  - Gap register is accurate (reassessment tracking per Section 5.4)
  - Exception approvals are documented (Section 4.2 Step 4 evidence exists)

- **Audit Scope Adjustment**: When compliance criteria change (Section 5.2), changed controls added to next internal audit scope (verify new requirements are met per Section 5.2 Step 6)

**Reference**: Internal Audit Programme (Clause 9.2 procedure, not duplicated in this policy)

---

### Management Review (Clause 9.3)

**Integration Points**:

**Management Review Inputs** (Clause 9.3.2) - Governance contributions:
- **Changes to ISMS**: Change log summary (Section 5.3), compliance criteria changes implemented since last review
- **Results of audits**: Governance-related audit findings (Section 6.1 topic 5), Challenge Protocol outcomes (Section 3.3)
- **Continual improvement opportunities**: Lessons learned (Section 6.2), governance process improvements identified
- **Governance effectiveness**: Annual governance review findings (Section 6.1), exception volume metrics (Section 4.4), reassessment completion rates (Section 5.4)

**Management Review Outputs** (Clause 9.3.3) - Governance decisions:
- **Approval of risk acceptances**: Executive Management reviews and approves risk acceptances per Section 4.2 Step 4
- **Approval of strategic changes**: ISMS scope expansion, major architecture decisions per Section 2.1 escalation path
- **Resource allocation for remediation**: Budget/personnel for gap register closure (Section 5.4), exception resolution (Section 4.4)
- **Governance process improvements**: Actions from annual governance review (Section 6.1), lessons learned implementation (Section 6.2)

**Reference**: Management Review Procedure (Clause 9.3 process, not duplicated in this policy)

---

### Nonconformity and Corrective Action (Clause 10.2)

**Integration Points**:

**Nonconformity Triggers** - Governance-related:
- Governance process not followed (e.g., exception approved without Executive Management sign-off per Section 4.2 Step 4)
- Audit finding reveals interpretation gap (control does not satisfy ISO 27001 objective per Section 3.3 Outcome B)
- Incident reveals control weakness requiring policy update (triggers Section 5.1 internal change trigger)

**Corrective Action Process**:
- **Root cause analysis**: Is this governance process failure (process bypassed, approval missing) or isolated incident (one-time mistake)?
- **Remediation**: Update policy per Section 5.2 change process, or improve process execution (training, automation, approval workflow)
- **Verification**: Internal audit confirms corrective action effective (Clause 9.2, Section 7.2)

**Governance Evolution**: Corrective actions may trigger governance policy updates:
- If nonconformity reveals POL-GOVERNANCE gap → Update this policy per Section 5.2 (governance policy itself evolves)
- If pattern of nonconformities → Annual governance review (Section 6.1) investigates systematic issue

**Reference**: Nonconformity and Corrective Action Procedure (Clause 10.2 process, not duplicated in this policy)

---

## Evidence for This Policy

### Stage 1 (Documentation Review) Evidence

**Purpose**: Demonstrate POL-GOVERNANCE is adequately documented and approved

**Evidence Required**:

- [X] This policy document (ISMS-POL-01 v1.0)
- [X] Approval signatures from CISO, Legal/Compliance, Executive Management (Document Control section)
- [X] Governance structure documented (Section 2.1 Authority Boundaries table)
- [X] Competence requirements defined (Section 2.3)
- [X] Exception handling process documented (Section 4.2 5-step process)
- [X] Change management process documented (Section 5.2 6-step process)
- [X] Annual review process defined (Section 6.1)

**Auditor Verification**: Auditor confirms policy exists, is approved, and comprehensively addresses governance decision-making authority per ISO 27001 Clause 5.3 (Roles, responsibilities and authorities)

---

### Stage 2 (Operational Effectiveness) Evidence

**Purpose**: Demonstrate governance processes defined in this policy are operationally effective (actually followed, not just documented)

**Evidence Required**:

**Authority Boundaries Evidence** (Section 2):
- [ ] Competence verification records (Section 2.3): Certifications, training records, experience documentation for CISO, Legal/Compliance, DPO, Executive Management
- [ ] Decision approval evidence: Signatures on POL documents (CISO approvals), POL-00 matrix (Legal/Compliance approvals), Risk Acceptance Register (Executive Management approvals)

**Applicability Authority Evidence** (Section 3):
- [ ] POL-00 quarterly monitoring logs (4 quarters, signed by Legal/Compliance + CISO)
- [ ] Triggered assessment records (business changes, regulatory updates assessed per POL-00 Section 5)
- [ ] SoA with justifications for all 93 controls (Section 3.2 applicability decisions documented)
- [ ] Challenge Protocol execution records (if Section 3.3 invoked - auditor challenges, resolutions)

**Exception Handling Evidence** (Section 4):
- [ ] Exception Register (Section 4.3) with entries showing 5-step process followed
- [ ] Risk Acceptance Register with Executive Management signatures (Section 4.2 Step 4)
- [ ] Exception volume metrics (Section 4.4 quarterly tracking)
- [ ] Exception closure records (deferred implementations completed, alternative controls verified)

**Change Management Evidence** (Section 5):
- [ ] ISMS Change Log (Section 5.3) showing compliance criteria changes over time
- [ ] Change Impact Assessments (Section 5.2 Step 2) for major changes
- [ ] Change approvals (Section 5.2 Step 4) from appropriate authority
- [ ] Reassessment tracking (Section 5.4 Gap Register) showing 90-day completion
- [ ] Internal audit reports verifying changed controls (Section 5.2 Step 6)

**Governance Effectiveness Evidence** (Section 6):
- [ ] Annual governance review meeting minutes (Section 6.1) with Executive Management attendance
- [ ] Governance health report covering 6 review topics (Section 6.1)
- [ ] Lessons learned register (Section 6.2) with entries and action tracking
- [ ] Continual improvement actions from governance review (implemented and verified)

**Current Evidence Status**:
- Templates exist for registers (Exception, Change Log, Lessons Learned, Gap Register)
- Processes defined but execution evidence accumulates over time (quarterly logs, annual reviews)
- First annual governance review scheduled for [Date]

---

### Assessment Workbook

**Governance Compliance Assessment Workbook**: ISMS-CHK-POL-01

**Purpose**: Quarterly assessment of governance process compliance (verify processes defined in this policy are followed)

**Workbook Structure**:

**Domain 1: Authority Boundaries** (Section 2)
- Requirement GOV-01: Technical control implementations approved by CISO (verify POL approval signatures)
- Requirement GOV-02: Regulatory applicability determinations approved by Legal/Compliance (verify POL-00 approvals)
- Requirement GOV-03: Risk acceptance decisions approved by Executive Management (verify Risk Acceptance Register signatures)
- Requirement GOV-04: Competence requirements verified (verify Section 2.3 criteria met for all decision-makers)

**Domain 2: Applicability Decisions** (Section 3)
- Requirement GOV-05: POL-00 quarterly monitoring completed (verify 4 quarters have logs)
- Requirement GOV-06: Triggered assessments documented (verify business changes assessed per POL-00 Section 5)
- Requirement GOV-07: SoA justifications complete (verify all 93 controls documented)
- Requirement GOV-08: Challenge Protocol followed if invoked (verify Section 3.3 execution if applicable)

**Domain 3: Exception Handling** (Section 4)
- Requirement GOV-09: Exceptions follow 5-step process (verify Exception Register entries complete Steps 1-5)
- Requirement GOV-10: Residual risk assessed for all exceptions (verify Step 2 risk assessments exist)
- Requirement GOV-11: Risk acceptances approved by Executive Management (verify Step 4 approvals)
- Requirement GOV-12: Exception volume within targets (verify Section 4.4 metrics: <5% total, <3% risk acceptances)

**Domain 4: Change Management** (Section 5)
- Requirement GOV-13: Compliance criteria changes documented (verify Change Log entries exist)
- Requirement GOV-14: Changes follow 6-step process (verify Steps 1-6 completed for each change)
- Requirement GOV-15: Reassessments completed within 90 days (verify Section 5.4 Gap Register completion rates >95%)
- Requirement GOV-16: Changes verified by internal audit (verify Step 6 internal audit reports)

**Domain 5: Governance Review** (Section 6)
- Requirement GOV-17: Annual governance review completed (verify Section 6.1 meeting minutes exist)
- Requirement GOV-18: Review covers all required topics (verify 6 topics from Section 6.1 addressed)
- Requirement GOV-19: Continual improvement actions documented (verify actions assigned, owners designated, due dates set)
- Requirement GOV-20: Lessons learned register maintained (verify Section 6.2 register has entries and actions tracked)

**Assessment Frequency**: Quarterly (Q1, Q2, Q3, Q4)

**Python Script**: ISMS-SCR-CHK-POL-01.py (generates workbook, prepopulates with evidence checks)

**Location**: Assessment workbooks archived in [GRC Platform / Compliance Evidence Repository]

---

## Audit Preparation and Documentation Package

### Documents Provided to Auditors

**Stage 1 Audit** (Documentation Review):

Core Governance Documents:
- [ ] ISMS-POL-01 (this policy - explains governance boundaries and processes)
- [ ] ISMS-POL-00 (Regulatory Applicability Framework - explains Tier 1/2/3 determinations)
- [ ] Statement of Applicability (SoA - control-by-control implementation status and justifications)
- [ ] Risk Treatment Plan (Clause 6.1.3 - risk-based control decisions)
- [ ] Risk Acceptance Register (Clause 6.1.3d - Executive Management approvals for risk acceptances)
- [ ] Organisational Context Document (Clause 4.1/4.2 - scope, interested parties)
- [ ] ISMS Change Log (Section 5.3 - compliance criteria evolution since last audit)

**Stage 2 Audit** (Implementation Verification):

Governance Execution Evidence:
- [ ] Governance Compliance Assessment Workbook (ISMS-CHK-POL-01 - quarterly assessments)
- [ ] Exception Register (Section 4.3 - all exceptions with 5-step process documentation)
- [ ] POL-00 Quarterly Monitoring Logs (4 quarters - regulatory landscape reviews)
- [ ] Triggered Assessment Records (POL-00 Section 5 - business changes, regulatory updates assessed)
- [ ] Internal Audit Reports (Clause 9.2 - most recent reports covering governance topics)
- [ ] Management Review Records (Clause 9.3 - most recent review with governance inputs/outputs)
- [ ] Annual Governance Review Report (Section 6.1 - most recent governance health assessment)
- [ ] Lessons Learned Register (Section 6.2 - governance improvements tracked)
- [ ] Competence Verification Records (Section 2.3 - certifications, training for decision-makers)

---

### Audit Coordination

**Pre-Audit Coordination** (2 weeks before audit):

**Purpose**: Provide auditor with ISMS structure overview to facilitate efficient audit execution

**Coordination Activities**:
1. **Documentation package assembly**: Gather documents per Section 9.1 (Stage 1 or Stage 2 list)
2. **ISMS structure briefing**: Provide auditor with overview of governance framework:
   - Authority boundaries (Section 2.1 - who decides what)
   - Applicability framework (Section 3 - how Tier 1/2/3 and SoA decisions are made)
   - Exception handling (Section 4 - how controls that cannot be implemented are addressed)
   - Change management (Section 5 - how compliance criteria evolve)
3. **Evidence location guide**: Inform auditor where evidence is maintained (GRC platform, document repository, workbook archives)
4. **Point of contact**: Designate CISO or delegate as primary auditor contact for questions

**Tone**: Collaborative and informative (not restrictive or adversarial)

**Communication**: Email, pre-audit call, or document package cover letter

---

## Closing Statement

This policy establishes **where professional judgment is exercised** in the organisation's ISMS, enabling:

**Objective Audit Verification**: Compliance is assessed against documented organisational decisions (POL-00 regulatory applicability, SoA control justifications, Risk Acceptance Register), not auditor discretion.

**Clear Decision Authority**: Roles (CISO, Legal/Compliance, Executive Management) have explicit authority boundaries with competence requirements, ensuring decisions are made by qualified individuals.

**Controlled Evolution**: Compliance criteria change through documented 6-step process (Section 5.2) with reassessment tracking, verification, and approval - model evolves, not stagnates.

**Collaborative Audit Relationship**: Auditor judgment focuses on verifying quality of organisational judgment (process compliance, ISO 27001 alignment, documentation completeness), not replacing organisational decisions.

---

**What this policy achieves:**

✅ **Clarity**: Compliance criteria are explicit (POL-00, SoA, Risk Treatment Plan, documented policies)
✅ **Consistency**: Changes are controlled (Section 5 change process, version control, reassessment tracking)
✅ **Defensibility**: Decisions are documented and justified (authority signatures, risk assessments, approval records)
✅ **Auditability**: Evidence demonstrates governance processes are followed (quarterly assessments, Exception Register, Change Log, annual reviews)
✅ **Improvement**: Lessons learned and governance reviews enable continual enhancement (Clause 10.1)

---

**The paradigm shift:**

**Traditional ISMS**: Professional judgment exercised during audit (auditor interprets requirements, organisation defends after the fact)

**This ISMS**: Professional judgment exercised during model design (organisation documents interpretation, auditor verifies quality and ISO 27001 alignment)

**Result**: Audit becomes objective verification of documented design, not subjective interpretation contest.

---

**Governance Review**: This policy itself is subject to continual improvement. Annual governance review (Section 6.1) assesses whether governance processes are effective and identifies improvements. If governance gaps are identified, this policy is updated per Section 5.2 change control process.

---

**Approval and Maintenance**:

This policy is approved by Executive Management and maintained by the CISO. Review cycle is annual, or upon significant ISMS changes requiring governance process updates.

---

**END OF ISMS-POL-01**

<!-- QA_VERIFIED: 2026-03-01 -->
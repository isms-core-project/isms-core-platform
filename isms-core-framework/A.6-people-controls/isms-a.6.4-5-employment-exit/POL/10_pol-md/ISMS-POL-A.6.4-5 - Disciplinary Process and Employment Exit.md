**ISMS-POL-A.6.4-5 — Disciplinary Process and Employment Exit**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Disciplinary Process and Employment Exit |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.6.4-5 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Human Resources Officer (CHRO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO/CHRO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Human Resources Officer (CHRO)
- Secondary: Chief Information Security Officer (CISO)
- Legal: Legal Counsel
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles)
- ISMS-POL-A.5.15-16-18 (Identity & Access Management)
- ISMS-POL-A.6.6 (Confidentiality and Non-Disclosure Agreements)
- ISMS-IMP-A.6.4-5.S1-UG/TG (Disciplinary Process Assessment)
- ISMS-IMP-A.6.4-5.S2-UG/TG (Employment Exit Assessment)
- ISMS-IMP-A.6.4-5.S3-UG/TG (Post Employment Obligations)
- ISMS-IMP-A.6.4-5.S4-UG/TG (Employment Exit Dashboard)
- ISO/IEC 27001:2022 Controls A.6.4, A.6.5

---

## Executive Summary

This policy establishes [Organization]'s requirements for handling security policy violations through disciplinary processes and ensuring secure termination of employment including protection of organisational information and assets.

**Scope**: This policy applies to all employees, contractors, and temporary workers throughout the disciplinary process and employment termination lifecycle, regardless of reason for termination.

**Purpose**: Define organisational requirements for disciplinary actions related to information security and secure employment exit. This policy establishes WHAT processes apply and WHO is responsible. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.6.4-5 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss employment law, Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA) apply where [Organization]'s business activities trigger applicability.

**Combined Control Approach**: Controls A.6.4 (Disciplinary Process) and A.6.5 (Responsibilities After Termination) are implemented together because security-related disciplinary actions often precede termination, and both require coordinated HR-Security processes.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Controls A.6.4 and A.6.5**

**ISO/IEC 27001:2022 Annex A.6.4 - Disciplinary Process**

> *A disciplinary process should be formalized and communicated to take actions against personnel who have committed an information security policy violation.*

**ISO/IEC 27001:2022 Annex A.6.5 - Responsibilities After Termination or Change of Employment**

> *Information security responsibilities and duties that remain valid after termination or change of employment should be defined, enforced and communicated to relevant personnel and other interested parties.*

**Control Objectives**:

- Ensure appropriate response to information security policy violations
- Protect organisational assets and information during and after employment changes
- Maintain confidentiality obligations beyond employment
- Prevent unauthorized access upon termination

**Control Type**: Preventive, Corrective
**Control Category**: People

**This Policy Addresses**:

- Disciplinary framework and violation categories
- Disciplinary procedures and due process
- Access revocation requirements and timelines
- Asset return requirements
- Post-employment obligations

## What This Policy Does

This policy:

- **Defines** disciplinary framework for security policy violations
- **Establishes** secure exit process requirements and timelines
- **Specifies** post-employment confidentiality obligations
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Define pre-employment screening procedures** (see ISMS-POL-A.5.1-2-6.1-2)
- **Specify ongoing security training requirements** (see A.6.3)
- **Detail third-party/vendor termination procedures** (see ISMS-POL-A.5.19-23)
- **Provide NDA template content** (see ISMS-POL-A.6.6)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite procedural changes
- Flexibility for different HR systems
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All personnel types (employees, contractors, temporary workers, interns)
- All termination types (voluntary, involuntary, retirement, contract end, role change)
- All security violation types (policy breaches, acceptable use violations, data handling)
- All asset types (physical, logical, information, intellectual property)

**Out of Scope**:

- Pre-employment screening (covered by A.6.1)
- Ongoing security training (covered by A.6.3)
- Third-party/vendor termination (covered by A.5.19-23)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss OR (Code of Obligations)** | All employment | Art. 328 - Employee protection, Art. 337 - Termination procedures |
| **Swiss nDSG** | All personal data processing | Data subject rights, access revocation |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.6.4, A.6.5 |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Requirements |
|-----------|-------------------|--------------|
| **EU GDPR** | Processing personal data of EU/EEA data subjects as determined in ISMS-POL-00 | Access control measures (Art. 32); proportionate offboarding procedures for personal data access |
| **FINMA** | Swiss regulated financial institution | Enhanced exit procedures for key personnel |
| **DORA/NIS2** | EU financial services or essential/important entity | Enhanced access revocation and verification for critical systems |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- SHRM (Society for Human Resource Management) best practices
- ISACA employee offboarding guidelines
- Employment law best practice guides

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

---

# Policy Statements

## Disciplinary Process (A.6.4)

### Disciplinary Framework

[Organisation] SHALL maintain a formal disciplinary process for information security violations:

**Principles**:

- Fair and consistent application across all personnel
- Proportionate to severity of violation
- Aligned with applicable employment law
- Documented with appropriate evidence
- Progressive where circumstances allow
- Timely response to violations

### Violation Categories

| Category | Examples | Typical Response |
|----------|----------|------------------|
| **Minor/Inadvertent** | Accidental policy breach, first-time minor violation | Verbal warning, additional training |
| **Moderate** | Repeated minor violations, negligent data handling | Written warning, remedial training |
| **Serious** | Deliberate policy violation, significant data exposure | Final warning, suspension, termination |
| **Gross Misconduct** | Malicious data theft, sabotage, criminal activity | Immediate dismissal, legal action |

### Disciplinary Procedures

[Organisation] SHALL follow structured disciplinary procedures:

**Investigation**:

1. Incident reported to HR and Security Team
2. Preliminary assessment of severity
3. Evidence collection and preservation
4. Investigation (interviews, log review, forensics if needed)
5. Findings documented

**Decision and Action**:

1. Violation severity determined
2. Mitigating/aggravating factors considered
3. Appropriate disciplinary action selected
4. Decision communicated to employee
5. Action implemented
6. Follow-up monitoring where appropriate

**Due Process**:

- Employee informed of allegations
- Opportunity to respond provided
- Right to representation per employment law
- Appeals process available
- Documentation maintained confidentially

### Security Team Involvement

Security Team SHALL be involved in disciplinary matters when:

- Violation involves information security policy breach
- Technical investigation required (log analysis, forensics)
- Access revocation or monitoring recommended
- Potential for ongoing security risk
- Legal or regulatory notification may be required

### Escalation and Notification

| Violation Severity | Internal Notification | External Notification |
|-------------------|----------------------|----------------------|
| Minor | Line Manager, HR | None |
| Moderate | HR, CISO | None typically |
| Serious | HR, CISO, Legal | Regulators if required |
| Gross Misconduct | HR, CISO, Legal, Executive Management | Police, regulators as required |

## Employment Exit (A.6.5)

### Exit Process Requirements

[Organisation] SHALL implement secure exit processes for all employment terminations:

**Access Revocation Timeline**:

| Termination Type | Access Revocation Timing |
|------------------|-------------------------|
| **Immediate dismissal** (gross misconduct) | Within 1 hour of decision |
| **Termination for cause** | Same business day, before notification where possible |
| **Voluntary resignation** | Last working day, end of shift |
| **Retirement** | Last working day |
| **Contract end** | Contract end date |
| **Role change (mover)** | Previous role access within 2 business days |

**SLA Trigger & Coverage**: The access-revocation timer starts when the termination decision is recorded in the authorized HR/ticketing system and the IAM/IT offboarding request is submitted through the approved channel. Urgent terminations (immediate dismissal, termination for cause) are supported via the on-call offboarding process defined in ISMS-IMP-A.6.4-5. **If full revocation cannot be completed within the SLA**, compensating controls (e.g., IdP disable, VPN disable, badge disable) are applied immediately, and a nonconformity/exception is recorded with remediation tracked to closure. The offboarding checklist is generated from the authoritative application/service inventory and identity access catalog (see ISMS-POL-A.5.9 and IAM procedures).

**Access Revocation Scope**:

| Access Type | Revocation Requirement |
|-------------|----------------------|
| **Physical Access** | Badge disabled, keys returned, biometrics removed |
| **Logical Access** | All accounts disabled (AD, email, applications, VPN, cloud) |
| **Remote Access** | VPN, remote desktop, mobile device management |
| **Third-Party Access** | Vendor portals, partner systems |
| **Delegated Access** | Mailbox access, shared accounts, API keys |
| **Data Access** | File shares, databases, cloud storage |

### Asset Return

[Organisation] SHALL recover all organisational assets:

**Physical Assets**:

- Laptops, computers, monitors
- Mobile devices (phones, tablets)
- Storage media (USB drives, external drives)
- Access badges, keys, tokens
- Documents, printed materials
- Company credit cards

**Logical Assets**:

- Licensed software (removal from personal devices if BYOD)
- Data on personal devices (verified deletion)
- Access credentials (password resets for shared systems)
- Authentication tokens/devices

**Asset Return Process**:

1. Asset inventory provided to departing employee
2. Return appointment scheduled
3. Assets verified against inventory
4. Condition documented
5. Missing/damaged assets recorded for follow-up
6. Clearance signed by IT and HR

### Post-Employment Obligations

[Organisation] SHALL communicate and enforce continuing obligations:

**Confidentiality**:

- NDA obligations continue per agreement terms (per ISMS-POL-A.6.6)
- Trade secrets remain protected indefinitely
- Client/customer information remains confidential
- Classified information restrictions continue

**Return/Destruction of Information**:

- All organisational information SHALL be returned or certified destroyed
- Personal copies prohibited
- Verification of return or deletion of organisational information from non-organisational locations (e.g., personal devices or accounts), where applicable, is performed using lawful, documented procedures approved by HR and Legal, limited to what is necessary and proportionate
- Work product belongs to [Organisation]

### Exit Interview

[Organisation] SHALL conduct security-focused exit interviews:

**Interview Components**:

- Reminder of continuing confidentiality obligations
- Acknowledgment of NDA terms
- Confirmation of data return/deletion
- Identification of any concerns or outstanding matters
- Final documentation signing

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Disciplinary and Exit Responsibilities |
|------|---------------------------------------|
| **CHRO/HR** | Disciplinary process ownership, exit process coordination, employment law compliance |
| **CISO** | Security violation assessment, access revocation verification, forensic support |
| **Legal Counsel** | Employment law compliance, disciplinary appeal support, NDA enforcement |
| **Line Managers** | Initiate disciplinary matters, asset return verification, handover coordination |
| **IT Operations** | Access revocation execution, asset recovery, technical verification |
| **IAM Team** | Account disablement, access audit, leaver process execution |
| **All Personnel** | Report violations, follow exit procedures, return assets |

## Escalation Path

- Disciplinary matters: Manager → HR → CISO (if security-related) → Legal → Executive Management
- Exit process issues: HR → IT Operations → CISO

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Exit process compliance audit | Quarterly | Internal Audit | Sample of completed exits |
| Access revocation timeliness | Monthly | IAM Team | Termination-to-disable metrics |
| Asset recovery rate | Quarterly | IT Operations | Asset return records |
| Disciplinary process review | Annual | HR | Case documentation, outcomes |

**Exit Compliance Audit**: The quarterly audit uses a documented checklist and sampling approach defined in ISMS-IMP-A.6.4-5, including: sample population (all leavers in period), required timestamps (termination date, access revocation date per system), pass/fail criteria, and how findings are recorded. Findings are tracked per Clause 10.2.

**Governance Metrics**:

- Access revoked within SLA (target: 100%)
- Assets recovered within 5 business days (target: >95%)
- Exit interviews completed (target: 100%)
- Orphaned accounts from leavers (target: 0)
- Outstanding asset returns >30 days (target: 0)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Employment law changes, security incidents, audit findings
- **Reviewers**: CHRO, CISO, Legal Counsel
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- Accelerated exit with garden leave and immediate access revocation
- Extended access for documented business need (time-limited)
- Asset write-off for lost/damaged items

**Exception Process**:

1. Document business justification
2. Risk assessment of exception impact
3. CISO + HR approval
4. Time-limited approval
5. Documentation in exception register

**Not Permissible**:

- Permanent exceptions to access revocation timelines
- Exceptions without compensating controls
- Waiver of post-employment confidentiality obligations

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., delayed access revocation, unreturned assets, incomplete exit process, orphaned accounts) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Insider threat risks inform disciplinary and exit requirements
- Access revocation delays represent security risk
- Risk treatment plans document personnel security controls

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Controls A.6.4 and A.6.5 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.5.1-2-6.1-2** | Secure Employment - Pre-employment and during employment |
| **A.5.15-16-18** | IAM - Leaver process, access revocation |
| **A.6.6** | NDAs - Post-employment confidentiality obligations |
| **A.5.24-28** | Incident Management - Security violations may be incidents |

**Stacked Control Integration**:

A.6.4-5 (Disciplinary and Exit) stacks with related controls:

| Stacked Control | Integration Point | A.6.4-5 Contribution |
|-----------------|-------------------|----------------------|
| **A.5.15-16-18** (IAM) | Access lifecycle | A.6.4-5 triggers leaver process; IAM executes revocation |
| **A.6.6** (NDAs) | Post-employment | A.6.4-5 enforces NDA; A.6.6 defines agreement terms |
| **A.5.24-28** (Incident Management) | Violations | A.6.4-5 handles personnel actions; A.5.24-28 handles technical response |

Assessment of A.6.4-5 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.6.4-5 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.6.4-5.S1-UG/TG** | Disciplinary Process Guide | Investigation procedures, documentation templates |
| **ISMS-IMP-A.6.4-5.S2-UG/TG** | Employment Exit Procedures | Leaver process, checklists, verification |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- This policy document (ISMS-POL-A.6.4-5 v1.0)
- Recorded approval by CHRO, CISO, Legal Counsel, Executive Management
- Evidence of communication to relevant roles
- Disciplinary framework with violation categories defined (Disciplinary Process)
- Access revocation timelines specified (Employment Exit)
- Asset return requirements documented (Asset Return)
- Post-employment obligations defined (Post-Employment Obligations)
- Roles and responsibilities assigned (Roles and Responsibilities)

Evidence presence and status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Disciplinary case records (anonymised) showing process compliance
- Access revocation logs showing timeliness metrics
- Asset return records with sign-off documentation
- Exit interview records showing completion and acknowledgments
- NDA acknowledgment records for departed personnel
- Orphaned account reports (monthly reconciliation)
- Sample leaver process tickets showing full completion
- Training records for managers on disciplinary procedures

---

# Definitions

| Term | Definition |
|------|------------|
| **Disciplinary Action** | Formal response to employee misconduct or policy violation |
| **Gross Misconduct** | Serious violation warranting immediate dismissal without notice |
| **Leaver Process** | Procedures for offboarding departing personnel |
| **Garden Leave** | Notice period where employee is paid but not working |
| **Exit Interview** | Meeting to document departure and confirm obligations |
| **Orphaned Account** | User account remaining after employment termination |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Human Resources Officer (CHRO)** | [Name] | [Date to be set] |
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Legal Counsel** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for disciplinary processes and employment exit. Implementation procedures are documented in ISMS-IMP-A.6.4-5 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-04 -->

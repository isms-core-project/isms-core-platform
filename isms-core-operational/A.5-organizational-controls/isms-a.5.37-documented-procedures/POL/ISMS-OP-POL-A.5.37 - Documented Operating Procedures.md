<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.37:operational:OP-POL:a.5.37 -->
**ISMS-OP-POL-A.5.37 — Documented Operating Procedures**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Documented Operating Procedures |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.37 |
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
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.5.37 — Documented operating procedures
- ISO/IEC 27001:2022 Clause 7.5 — Documented information

**Related Annex A Controls**:

| Control | Relationship to Documented Operating Procedures |
|---------|------------------------------------------------|
| A.5.1 Policies for information security | Policies define requirements; procedures implement them |
| A.5.24–28 Incident management | Incident response procedures documented per this policy |
| A.6.3 Information security awareness, education, and training | Personnel trained on relevant procedures |
| A.8.32 Change management | Procedures updated via change management process |
| A.8.9 Configuration management | Configuration procedures documented |

**Related Internal Policies**:

- Information Security Policy
- Change Management Policy
- Incident Management Policy
- Information Security Awareness and Training Policy

---

# Documented Operating Procedures Policy

## Purpose

The purpose of this policy is to ensure that operating procedures for information processing facilities are documented, maintained, and made available to personnel who need them, enabling consistent, secure, and auditable operations.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing documented technical and organisational measures appropriate to risk. Documented procedures demonstrate the organisation's commitment to systematic data protection and security controls. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.

All operating procedures for information processing facilities, systems, applications, and security controls operated by or on behalf of the organisation.

All environments: production, test, development, and disaster recovery.

## Principle

Operating procedures for information processing facilities shall be documented and made available to personnel who need them. Documents required for the information security management system are controlled, managed, and available. You cannot operate securely without documented, tested, and maintained procedures.

---

## Mandatory Documented Procedures

The organisation shall document operating procedures for the following categories:

### Security Operations

| Procedure Category | Examples |
|--------------------|----------|
| **Access management** | User provisioning, access review, emergency access, deprovisioning |
| **Incident response** | Detection, triage, escalation, communication, evidence preservation |
| **Vulnerability management** | Scanning, assessment, prioritisation, remediation |
| **Backup and recovery** | Backup execution, verification, restoration testing |
| **Monitoring and log review** | Log review, alert response, escalation |
| **Patch management** | Assessment, testing, deployment, verification |

### System Operations

| Procedure Category | Examples |
|--------------------|----------|
| **Startup and shutdown** | System startup, graceful shutdown, emergency shutdown |
| **Batch processing** | Job scheduling, monitoring, failure handling |
| **Error handling** | Error detection, logging, escalation |
| **Media handling** | Storage, transport, disposal of removable media |
| **System maintenance** | Routine maintenance, housekeeping, health checks |

### Administrative Operations

| Procedure Category | Examples |
|--------------------|----------|
| **User support** | Request handling, problem resolution |
| **Change implementation** | Pre-change checks, execution, post-change verification |
| **Disaster recovery** | DR invocation, recovery execution, return to normal operations |

---

## Creating and Updating Procedures

### Documentation Standards

All operating procedures shall include the following mandatory elements:

| Element | Requirement |
|---------|-------------|
| **Document ID** | Unique identifier following the organisation's naming convention: **[Specify format, e.g., "PROC-[CATEGORY]-[###]" where CATEGORY = SEC (security), OPS (operations), ADM (administrative), DR (disaster recovery)]**. Examples: PROC-SEC-001 (User Provisioning), PROC-DR-005 (Backup Restore) |
| **Title** | Clear, descriptive title |
| **Version** | Version number and date |
| **Owner** | Designated procedure owner (name and role) responsible for accuracy and currency |
| **Backup Owner** | Designated backup owner for critical procedures to avoid single point of failure |
| **Approval** | Approver name and date |
| **Purpose** | Why the procedure exists |
| **Scope** | What the procedure covers |
| **Prerequisites** | Required conditions, access, tools |
| **Steps** | Sequential, numbered steps |
| **Expected outputs** | What the operator should see at key steps |
| **Verification** | How to confirm successful completion |
| **Rollback** | Recovery steps if the procedure fails |
| **References** | Related documents and contacts |

### Quality Requirements

- Written clearly for the target audience's skill level.
- Sufficient detail that an unfamiliar but competent operator could execute the procedure.
- Free of ambiguity and unstated assumptions.
- Tested before production use.
- Reviewed and approved before publication.

### Format and Media

Procedures shall be created in electronic format using standard, supported office applications or native operational systems. The organisation shall ensure appropriate identification and description (title, date, author, reference number), consistent format (language, software version, graphics), and review and approval for suitability and adequacy.

---

## Document Storage and Availability

### Authoritative Repository

Procedures shall be stored in the organisation's document management system: **[Specify: SharePoint, Confluence, Notion, or equivalent]**.

**Repository location**: [URL or path: e.g., "https://company.sharepoint.com/sites/ISMS/Procedures"]

**Access**: Document repository access is restricted to authorised personnel per the Access Control Policy. All employees can view procedures relevant to their role; only procedure owners and designated personnel can edit.

This repository is the single source of truth for operating procedures. Local copies and duplicates are prohibited except approved offline emergency copies.

### Availability Requirements

| Procedure Type | Availability Requirement |
|----------------|-------------------------|
| **Emergency and DR procedures** | Printed copies + offline digital copy, tested quarterly |
| **Critical operations** | Available 24/7 with redundant access |
| **Standard operations** | Available 24/7 where supporting customer-facing infrastructure; business hours minimum for others |
| **Reference procedures** | Available on demand |

### Emergency Offline Pack

For critical services, the organisation shall maintain an offline pack containing, at minimum:

- Disaster recovery invocation procedure.
- Break-glass / emergency access procedure.
- Core network access procedure.
- Backup restore procedures for critical systems.

**Storage and Access**:

- **Primary location**: [Specify: Locked safe in server room / fireproof cabinet in office / secure off-site facility]
- **Backup location**: [Specify: IT Operations Manager's secure home safe / off-site backup facility]
- **Custodian**: IT Operations Manager ([Name or "Current holder: see contact list"])
- **Access authorisation**: CISO, CEO, IT Operations Manager, and [designated emergency contacts]
- **Access procedure**: Break-glass envelope or sealed container; access logged with date, accessor, and reason

Currency shall be verified **quarterly** with a recorded checklist confirming version alignment with the authoritative repository.

**Annual audit**: During annual internal audit, the offline pack shall be opened and verified against the authoritative repository (100% version match required).

---

## Version Control and Approval

### Policy Documents

- Policy documents are subject to change as a result of the continual improvement process.
- Changes to policy documents are made by the information security management team and approved by the Management Review Team.
- Version control history is maintained, capturing as a minimum: author, date, change description, and new version number.

### Operational Documents and Records

- Operational documents and records are updated by the process owner as part of day-to-day operations and as required.
- Version control history is maintained, capturing as a minimum: author, date, change description, and new version number.
- Only the latest approved version shall be presented to users.
- Previous versions shall be archived (not deleted) for audit trail.
- Updates shall be notified to affected personnel.

---

## Procedure Review and Maintenance

### Review Schedule

| Review Type | Frequency | Scope |
|-------------|-----------|-------|
| **Scheduled review** | Annual (minimum) | All procedures |
| **Post-incident review** | After relevant incident | Affected procedures |
| **Change-triggered review** | After system changes | Affected procedures |
| **Regulatory review** | After regulatory changes | Affected procedures |

### Review Activities

- Verify accuracy against current systems and processes.
- Update for technology changes and personnel changes.
- Improve based on user feedback and lessons learned.
- Align with current security requirements.
- Update references to related documents.

### Continuous Improvement and User Feedback

Personnel using procedures shall report:

- **Inaccuracies**: Steps that do not match current systems or produce unexpected results.
- **Ambiguities**: Unclear instructions or missing prerequisites.
- **Improvements**: Suggestions for efficiency or clarity.

**Feedback mechanism**: [Specify: Email to procedure owner, ticket in [system], comment function in document repository, quarterly procedure user survey].

**Feedback handling**:

- All feedback logged and reviewed by procedure owner within **14 days**.
- Feedback incorporated into next scheduled review or addressed immediately if critical.
- Submitter notified of disposition (accepted / deferred / rejected with rationale).

### Procedure Testing

Critical procedures shall be tested at defined intervals:

| Procedure Type | Testing Requirement |
|----------------|---------------------|
| **Disaster recovery** | Annual full test; quarterly tabletop exercise |
| **Incident response** | Semi-annual exercise |
| **Backup and restore** | Monthly restore test |
| **Emergency access** | Annual break-glass test |
| **Critical operations** | After significant changes |

Testing shall be documented, including: test date and participants, test scenario, results (success/partial/failure), issues identified, and remediation actions.

**Test result classification**:

- **Success**: Procedure completed as written with expected outcomes; no remediation required.
- **Partial success**: Procedure completed with minor deviations or workarounds; updates needed but procedure is usable.
- **Failure**: Procedure could not be completed as written, or resulted in incorrect outcome; immediate revision required before next use.

**Action upon test failure**:

- Procedure marked "Under Review" in repository (visible flag to users).
- Revised within **14 days** for critical procedures, **30 days** for non-critical.
- Re-tested after revision before "Approved" status restored.

---

## Procedure Documentation Metrics

The organisation shall track the following procedure documentation metrics:

| Metric | Target | Review Frequency |
|--------|--------|------------------|
| **Procedure inventory completeness** (all mandatory categories documented) | 100% | Quarterly |
| **Review currency** (procedures reviewed within scheduled period) | 100% | Quarterly |
| **Documentation standard compliance** (sample procedures meet mandatory elements) | 100% | Annually (via internal audit sample) |
| **Test completion rate** (critical procedures tested per schedule) | 100% | Quarterly |
| **Training completion** (critical procedure operators trained) | 100% | Quarterly |
| **Procedure test success rate** | ≥95% | Annually |

Metrics breaching targets shall be escalated to the CISO and reported at the next Management Review.

---

## Records Management

### Examples of Records

Records are evidence of an event and used for operational management and auditing. They include but are not limited to:

- Meeting minutes.
- Training records.
- Audit reports.
- Incident reports.
- Change records.
- Risk assessment records.

### Obsolete Documents and Records

**Archival (required for audit/legal/regulatory purposes)**:

- Obsolete documents and records shall be archived in line with data retention requirements:
  - **Operational records** (change logs, incident reports): **3 years** after obsolescence.
  - **Audit evidence** (procedure version history): **7 years** after obsolescence.
  - **Legal/regulatory** (compliance evidence): Per legal counsel or regulatory requirement (typically **7–10 years**).
- Archived documents removed from general accessibility; accessible only to authorised audit/compliance personnel.

**Secure deletion (not required for retention)**:

- Obsolete documents and records that are not required for audit and/or legal and regulatory purposes shall be securely deleted per the Information Classification and Handling Policy within **90 days** of obsolescence determination.

### Documents of External Origin

Documented information of external origin determined by the organisation to be necessary for the planning and operation of the Information Security Management System shall be identified and controlled (e.g., ISO standards, vendor documentation, regulatory guidance).

**Control requirements for external documents**:

- **Identification**: External documents marked as "External" in repository metadata.
- **Version control**: External document version and publication date recorded.
- **Review**: Reviewed annually for currency; updated versions obtained when available.
- **Accessibility**: Stored in the same repository as internal procedures for ease of reference.
- **No editing**: External documents shall not be modified; annotations or summaries created as separate internal documents.

**Examples**: ISO/IEC 27001:2022 standard, vendor product manuals, regulatory guidance from FDPIC, NIST frameworks.

### Document Classification

Documents shall be classified in line with the Information Classification and Handling Policy.

**Typical procedure classifications**:

- **Public**: None (procedures are operational details, not for public disclosure).
- **Internal**: Standard operating procedures, non-sensitive administrative procedures.
- **Confidential**: Security procedures (incident response, vulnerability management), DR procedures, break-glass procedures, procedures containing credentials or security architecture details.

Classified procedures shall be handled, stored, and transmitted according to their classification level. Confidential procedures shall have restricted access (role-based, need-to-know).

---

## Training and Competence

### Operator Training

Personnel shall be trained on relevant procedures before performing them independently.

- Training records shall be maintained.
- Competence shall be verified through observation, assessment, or supervisor sign-off.
- Refresher training shall be provided when procedures are significantly updated.
- Cross-training shall be implemented for critical procedures to avoid single points of failure.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; security procedure standards; approval of security procedures |
| **IT Operations Manager** | Infrastructure procedure ownership; offline pack custodian; coordination of procedure testing |
| **Procedure Owners** | Accuracy, currency, and quality of owned procedures; conducting reviews; approving updates |
| **Backup Procedure Owners** | Competent to review and approve updates in the primary owner's absence; cross-trained on procedure content; notified of all procedure updates (required for critical procedures) |
| **Quality / Records Manager** | Procedure template standards; review tracking; repository governance |
| **All Technical Personnel** | Follow procedures; report issues and inaccuracies; suggest improvements |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Procedure inventory** with metadata (owner, version, last reviewed, next review) | Quality / Records Manager | *Maintained continuously; full audit annually; target: 100% with current owner* |
| 2 | **Sample procedures** meeting documentation standards (mandatory elements present) | Quality / Records Manager | *Sample of 5–10 procedures reviewed annually during internal audit* |
| 3 | **Review completion records** (procedures reviewed within scheduled period) | Quality / Records Manager | *Tracked quarterly; target: 100% within review period* |
| 4 | **Procedure test results** (DR, incident response, backup restore, break-glass) | IT Operations Manager | *Per testing schedule; retained 3 years* |
| 5 | **Training records** for procedure operators (completion, competence verification) | HR / IT Operations | *Per event; target: 100% of critical procedure operators trained* |
| 6 | **Version control evidence** from repository (audit trail of changes) | Quality / Records Manager | *Continuous; verified during annual audit* |
| 7 | **Emergency offline pack** currency verification records | IT Operations Manager | *Quarterly; checklist signed and retained* |
| 8 | **Obsolete document** archival and deletion records | Quality / Records Manager | *Per event; retained per retention schedule* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, procedure inventory audits, sample quality reviews, review completion tracking, procedure test result analysis, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum 90 days, renewable). Exceptions shall be reported to the Management Review Team. Critical procedures and security procedures shall not be operated without documentation.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to operational standards, technology changes, audit findings, regulatory changes, and lessons learned from incidents and procedure test failures.

---

# Areas of the ISO 27001 Standard Addressed

Documented Operating Procedures Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | **5.37 Documented operating procedures** |
| Clause 7.5.1 Documented information — General | 5.13 Labelling of information |
| Clause 7.5.2 Creating and updating documents | 6.3 Information security awareness, education, and training |
| Clause 7.5.3 Control of documented information | 6.4 Disciplinary process |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures (documented procedures as organisational measure) |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security (documented processes) |
| EU GDPR (where applicable) | Art. 5(2) — Accountability principle (documented procedures demonstrate compliance); Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Control 5.37; Clauses 7.5.1, 7.5.2, 7.5.3 — Documented information |
| ISO/IEC 27002:2022 | Section 5.37 — Implementation guidance |
| NIST SP 800-53 Rev 5 | PL-2 (System Security and Privacy Plans), SA-5 (System Documentation), PS-1 (Policy and Procedures) |
| CIS Controls v8 | Control 16 (Application Software Security — Safeguard 16.1: Establish and Maintain a Secure Application Development Process — requires documented procedures) |

---

<!-- QA_VERIFIED: 2026-02-07 -->

**ISMS-OP-POL-A.5.3 — Segregation of Duties**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Segregation of Duties |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.3 |
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

- ISO/IEC 27001:2022 Control A.5.3 — Segregation of duties
- ISO/IEC 27002:2022 Section 5.3 — Implementation guidance
- Swiss Code of Obligations Art. 728a — Internal control system
- NIST SP 800-53 Rev 5 AC-5 — Separation of Duties

**Related Annex A Controls**:

| Control | Relationship to Segregation of Duties |
|---------|---------------------------------------|
| A.5.1 Policies for information security | Overarching policy framework governing SoD requirements |
| A.5.2 Information security roles and responsibilities | Role definitions that enable duty segregation |
| A.5.15 Access control | Access control rules enforce segregation boundaries |
| A.5.16 Identity management | Unique identities ensure individual accountability |
| A.5.18 Access rights | Access provisioning implements mutual exclusion constraints |
| A.8.2 Privileged access rights | Privileged accounts segregated from standard operations |
| A.8.3 Information access restriction | Technical enforcement of segregation rules |
| A.8.5 Secure authentication | Authentication verifies actor identity at each process stage |
| A.8.15 Logging | Audit trails record segregated activities for verification |
| A.8.32 Change management | Change process enforces developer/tester/deployer separation |

**Related Internal Policies**:

- Identity and Access Management Policy
- Authentication and Privileged Access Policy
- Change Management Policy
- Logging and Monitoring Policy
- Information Classification and Handling Policy

---

# Segregation of Duties Policy

## Purpose

The purpose of this policy is to reduce the risk of fraud, error, and circumvention of information security controls by ensuring that conflicting duties and conflicting areas of responsibility are separated across different individuals or roles. Segregation of duties prevents any single person from having end-to-end control over a critical process — from initiation through authorisation through execution to verification.

This policy supports Swiss nFADP (revDSG) by implementing organisational measures appropriate to risk to protect personal data processing integrity. Segregation of duties is a recognised internal control under Swiss Code of Obligations Art. 728a, which requires companies subject to ordinary audit to maintain an internal control system. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees, contractors, and third-party users involved in business processes where conflicting duties could enable fraud, error, or security breaches if performed by a single individual.

This includes:

- Financial transactions, approvals, and disbursements.
- Information system administration, development, and deployment.
- Access provisioning, review, and revocation.
- Security monitoring, log review, and incident response.
- Procurement, vendor management, and contract administration.
- Backup, recovery, and data restoration operations.

**Out of scope**: Non-sensitive operational processes with adequate supervision; fully automated processes with built-in segregation controls (where segregation is achieved through automation, the control configuration and audit trails shall be validated at least annually by the CISO or designated reviewer).

## Principle

Conflicting duties and conflicting areas of responsibility should be segregated. Where full segregation is not achievable due to the size of the organisation, compensating controls — including enhanced monitoring, management review, independent audit, and tamper-protected audit trails — shall be implemented and formally documented.

All segregation decisions shall be risk-based, considering the value and classification of assets involved, the potential for financial loss or reputational damage, and regulatory requirements.

---

## Definitions

| Term | Definition |
|------|------------|
| **Segregation of Duties (SoD)** | The practice of dividing tasks and privileges among multiple individuals to prevent any single person from having complete control over a critical process |
| **Conflicting Duties** | Responsibilities that, if combined in one individual, would allow that person to commit and conceal errors or fraud without detection |
| **Compensating Control** | An alternative control measure implemented when primary segregation cannot be achieved, providing equivalent risk reduction |
| **Mutual Exclusion** | A technical control preventing a user from being assigned conflicting roles simultaneously in an access control system |
| **Four-Eyes Principle** | A requirement that critical actions require approval or verification by at least two authorised individuals before execution |
| **SoD Matrix** | A documented mapping of roles, duties, and identified conflicts used to plan and verify duty segregation |

---

## Segregation Principles

All business processes and information systems shall implement segregation of duties where:

- Activities involve financial transactions **greater than CHF 10,000**, unless a lower threshold is defined in a department-specific procedure approved by the CFO and CISO based on risk assessment.
- Access to confidential or restricted information is required.
- System administration or privileged access is exercised.
- Security controls can be bypassed, modified, or disabled.
- Audit logs or compliance evidence can be modified or deleted.

**Financial threshold determination**:
- **CHF 10,000** is the organisation's baseline threshold based on risk assessment considering organisational size, transaction volume, and fraud exposure history.
- Lower thresholds may be defined for high-risk categories (e.g., CHF 5,000 for cash disbursements, CHF 2,000 for employee expense reimbursements) by the CFO and CISO based on department-specific risk assessment.
- Higher thresholds are not permitted without Executive Management approval and compensating controls.

**Threshold review**: Financial thresholds shall be reviewed annually by the CFO and CISO and adjusted based on inflation, organisational growth, and fraud risk reassessment.

### Minimum Segregation Standards

The following minimum segregation requirements apply:

| Process Type | Minimum Segregation Requirement |
|-------------|--------------------------------|
| **Financial transactions** >CHF 10,000 | Initiator shall not be the Approver |
| **System access requests** | Requestor shall not be the Approver; Approver shall not be the Provisioner |
| **Change management** | Developer shall not be the Tester; Tester shall not be the Deployer |
| **Security monitoring** | System Administrator shall not be the Log Reviewer |
| **Backup and recovery** | Backup Operator shall not be the Restoration Verifier |

Where an individual currently holds conflicting duties, the conflict shall be resolved within 30 calendar days of identification — either through reassignment, technical mutual exclusion, or formal compensating control documentation.

---

## Conflicting Duties Identification

The organisation shall maintain a documented SoD matrix identifying duty combinations that require segregation. The following categories provide the baseline:

### Financial Processes

The following duty combinations shall be segregated:

- Initiating payments AND approving payments.
- Creating vendor records AND processing payments to vendors.
- Recording transactions AND reconciling accounts.
- Managing payroll AND approving payroll disbursements.
- Budget preparation AND budget approval.

### IT Operations

The following duty combinations shall be segregated:

- Developing code AND deploying to production.
- Administering systems AND reviewing system logs.
- Creating user accounts AND approving access requests.
- Managing backups AND authorising data restoration.
- Configuring security controls AND auditing security effectiveness.
- Managing firewall rules AND reviewing firewall compliance.

### Procurement and Contracts

The following duty combinations shall be segregated:

- Selecting vendors AND negotiating contracts.
- Approving purchases AND receiving goods or services.
- Managing contracts AND verifying contract compliance.

### Human Resources

The following duty combinations shall be segregated:

- Hiring decisions AND background check verification.
- Setting compensation AND approving payroll.
- Terminating access AND confirming access revocation.

Department heads shall review the SoD matrix annually for their area and report any newly identified conflicts to the CISO. The CISO shall maintain the consolidated organisational SoD matrix in [GRC Tool] or equivalent register.

> **SoD Matrix location**: [Specify: ServiceNow GRC module, Archer, MetricStream, SharePoint register, or "In selection; interim: Excel register in controlled shared drive"]
>
> **Exception Register location**: [Same system as SoD Matrix or specify separately]
>
> Where a dedicated GRC tool is not yet deployed, the organisation shall maintain registers in controlled shared storage with version control, access logging, and quarterly integrity verification by the CISO.

---

## Small Team and SME Compensating Controls

Where segregation cannot be fully achieved due to limited personnel — a common situation in small and medium-sized organisations — compensating controls shall be implemented to provide equivalent risk mitigation.

### Required Compensating Controls

When full duty segregation is not feasible, **all five** of the following compensating controls shall be implemented for each identified conflict:

| # | Compensating Control | Implementation |
|---|---------------------|----------------|
| 1 | **Enhanced monitoring and logging** | All activities in the conflicting process shall be logged with immutable audit trails. Logs shall capture user identity, action, timestamp, and affected records |
| 2 | **Management review of transactions** | A manager or senior colleague not involved in the process shall review all transactions weekly at minimum |
| 3 | **Periodic independent review** | An independent party (internal audit, external auditor, or senior management) shall review the process quarterly at minimum |
| 4 | **Automated alerts for anomalies** | [SIEM] or equivalent monitoring shall generate alerts for unusual patterns such as transactions outside normal hours, amounts exceeding thresholds, or bulk operations |
| 5 | **Post-transaction audit trail with tamper protection** | Transaction records shall be stored in a manner that prevents modification or deletion by the individual performing the transaction |

### Periodic Independent Review Scope (Compensating Control #3)

An independent party shall review the process **quarterly** at minimum. The review shall include:

**Review scope**:
- **Sample transactions** (minimum 10% of transaction volume or 20 transactions, whichever is greater).
- **Audit trail verification** (confirm all activities logged; logs immutable).
- **Management review completion** (verify weekly management reviews occurred with documented sign-off).
- **Anomaly detection** (verify automated alerts functioning; review triggered alerts and resolution).
- **Process compliance** (confirm process followed as documented).

**Review documentation**: Each quarterly review shall produce a written report documenting scope, findings, issues identified, and recommendations. Reports retained for 3 years.

**Issue escalation**: Issues identified during independent review shall be escalated to the CISO within 5 business days and resolved within 30 calendar days.

### Documentation Requirement

Each compensating control arrangement shall be formally documented with:

- The specific conflicting duties that cannot be segregated.
- The business justification for the inability to segregate.
- The compensating controls in place (all five above).
- Formal risk acceptance signed by Executive Management.
- A defined review schedule (quarterly minimum).

Compensating control documentation shall be maintained in [GRC Tool] or an equivalent register accessible to the CISO and Internal Audit.

### Re-evaluation Triggers

Compensating control arrangements shall be re-evaluated when:

- Additional personnel are hired who could assume segregated duties.
- Organisational structure changes.
- Risk assessment identifies increased exposure.
- Audit findings indicate control weaknesses.
- A security incident occurs related to the compensating control area.

### Compensating Control Effectiveness Verification

The effectiveness of compensating controls shall be verified through:

**Quarterly independent review** (Compensating Control #3):
- Verify all five compensating controls are functioning as documented.
- Sample transactions to confirm audit trail integrity.
- Confirm management review completion with documented sign-off.
- Test automated alert configuration and response.

**Annual effectiveness assessment** by CISO:
- Review all compensating control arrangements.
- Assess whether controls adequately mitigate segregation risk.
- Identify opportunities to achieve full segregation (e.g., new hire can assume segregated duty).
- Update risk acceptance documentation.

**Compensating control failure**: If a compensating control is found ineffective, immediate notification to Executive Management and remediation within 14 calendar days or formal re-acceptance of residual risk.

---

## Technical Segregation Controls

Information systems supporting segregated processes shall implement the following technical controls:

> **Logging and monitoring system**: [Specify: Splunk, Elastic SIEM, Azure Sentinel, or "Selection in progress; interim: centralised logging to syslog server with manual review"]
>
> **Identity provider**: [Specify: Azure AD, Okta, Google Workspace, or "Active Directory on-premises"]
>
> **ERP/Financial system**: [Specify: SAP, Oracle, NetSuite, or applicable system]
>
> Where systems are in selection or transition, document interim approach and target deployment date.

### Access Control Enforcement

- **Role-based access control (RBAC)**: Roles shall be defined in the identity provider or application to enforce duty separation. Conflicting roles shall be documented as mutually exclusive.
- **Mutual exclusion constraints**: The access control system ([Identity Provider / ERP / HR System]) shall prevent a single user from holding conflicting roles simultaneously. Where the system does not natively support mutual exclusion, a manual review shall be conducted at every access provisioning event.
- **Workflow controls**: Multi-step business processes shall require different authorised individuals at each approval stage. Self-approval shall be technically blocked where feasible and prohibited by policy in all cases.
- **Privileged access management**: Privileged accounts shall be separate from standard accounts. No individual shall approve their own elevated access requests.

**Mutual exclusion constraint verification**:
- **Automated systems**: Mutual exclusion constraints shall be tested **annually** by attempting to assign conflicting roles to a test user and verifying the system blocks the assignment. Test results documented.
- **Manual review systems**: Access provisioning checklists shall include SoD conflict check with documented verification before access grant. Provisioner shall reference SoD matrix and confirm no conflicts.
- **Quarterly access review**: All user role assignments shall be compared against SoD matrix to detect any conflicts that bypassed provisioning controls. Findings resolved within 30 calendar days.

### Audit Trail Requirements

- **Immutable logging**: All activities in segregated processes shall be logged to a centralised logging platform ([SIEM] or equivalent) that the process participants cannot modify or delete.
- **Actor identification**: Logs shall clearly identify the individual performing each action at every stage of the process.
- **Timestamp and action recording**: All approvals, modifications, and process completions shall be recorded with accurate timestamps.
- **Log protection**: Audit logs shall be protected against modification or deletion per the Logging and Monitoring Policy. Acceptable implementations include write-once storage, restricted administrator access with separate log reviewer, retention locks, or centralised log aggregation with integrity verification.

---

## Exception Management

Exceptions to segregation requirements shall be managed through a formal process. Self-approval of segregation exceptions is never permitted.

### Emergency Exceptions (duration 24 hours or less)

When operational urgency requires temporarily bypassing segregation controls:

1. **Verbal authorisation** from Department Head and CISO (or CISO delegate) — record who authorised, when, and the specific exception granted.
2. **Documented within 4 hours** of exception use via [emergency exception form / ticket system / email to CISO] including:
   - Exception ID (unique identifier).
   - Requester name and role.
   - Verbal authorisers (names, time of authorisation).
   - Business justification (specific operational urgency).
   - Exception granted (specific duties combined; duration).
   - Actions taken during exception period.
   - Compensating controls active (enhanced monitoring, immediate post-review).
3. **Full review within 24 hours** of exception end — the CISO or delegate shall verify that compensating controls were effective and no irregularities occurred. Review sign-off documented.
4. **Compensating controls active** during the exception period — enhanced monitoring and post-activity review at minimum.

**Emergency exception log**: All emergency exceptions shall be logged in the Exception Register with "Emergency" flag.

### Planned Exceptions (duration greater than 24 hours)

When a longer-term exception is required (e.g., staff absence, project constraints):

1. **Formal exception request** submitted to the CISO with business justification.
2. **Risk assessment** of the exception impact on fraud and error prevention.
3. **Compensating controls** documented and approved before the exception takes effect.
4. **CISO and Executive Management approval** — both required.
5. **Maximum duration**: 90 calendar days. Renewal requires re-assessment and re-approval.

### Not Permissible

The following exceptions shall not be granted under any circumstances:

- Permanent exceptions to financial segregation requirements.
- Exceptions that eliminate or bypass audit trail capabilities.
- Self-approval of one's own segregation exception.

### Exception Register

All exceptions shall be recorded in the Exception Register maintained in [GRC Tool] or equivalent. Each record shall include:

- Affected system(s) and process(es).
- Identity and role(s) granted the exception.
- Time window (start date and end date).
- Approving authority with evidence of approval.
- Compensating controls active during the exception.
- Post-exception review outcome.
- Closure date.

The CISO shall review the Exception Register monthly and report active exceptions to Executive Management quarterly.

---

## SoD Matrix Maintenance

### Annual Review

The organisational SoD matrix shall be reviewed and updated annually. The review shall:

- Confirm all documented conflicts remain valid and complete.
- Identify new conflicts arising from organisational changes, new systems, or new processes.
- Verify that compensating controls remain effective for unresolved conflicts.
- Update the matrix to reflect current organisational structure.

### Quarterly Access Rights Verification

IT Operations shall generate access reports quarterly from the identity provider and application access systems. The CISO shall compare these reports against the SoD matrix to verify:

- No individual holds conflicting roles in production systems.
- Mutual exclusion constraints are functioning correctly.
- New role assignments since the last review do not create undocumented conflicts.

Findings shall be documented and conflicts resolved within 30 calendar days of discovery.

---

## Roles and Responsibilities

| Role | Segregation of Duties Responsibilities |
|------|----------------------------------------|
| **Executive Management** | Approve segregation policy; accept residual risks; approve compensating controls; approve planned exceptions |
| **CISO** | Define and maintain SoD matrix; monitor compliance; approve emergency and planned exceptions; review Exception Register monthly |
| **CFO** | Oversee financial process segregation; approve financial control exceptions jointly with CISO; set financial threshold adjustments |
| **Department Heads** | Implement segregation within departments; identify new conflicts; request exceptions; ensure weekly management review of compensating controls |
| **HR** | Maintain organisational structure supporting segregation; notify IT of role changes affecting duty assignments |
| **IT Operations** | Implement technical controls (RBAC, mutual exclusion, workflow); generate quarterly access reports; maintain audit trails |
| **Internal Audit** | Verify segregation effectiveness; assess compensating control adequacy; report violations; conduct quarterly independent reviews |

### Escalation Path

- **Segregation conflicts identified**: Department Head notifies CISO. CISO escalates to Executive Management if resolution requires organisational change.
- **Exception requests**: Requestor submits to Department Head. Department Head submits to CISO. CISO obtains Executive Management approval for planned exceptions.
- **Violation detected**: Immediate notification to CISO and Internal Audit. Investigation initiated within 24 hours.

### Violation Investigation Process

When a segregation violation is detected:

1. **Immediate notification** to CISO and Internal Audit (within 4 hours of detection).
2. **Investigation initiated** within 24 hours by Internal Audit or CISO-designated investigator.
3. **Investigation scope**:
   - Determine if violation was inadvertent (system misconfiguration, access provisioning error) or intentional.
   - Review all transactions performed under the violation period.
   - Assess whether fraud or error occurred.
   - Identify root cause (process failure, training gap, intentional circumvention).
4. **Investigation timeline**: Complete within 10 business days for administrative violations; within 5 business days for suspected fraud.
5. **Remediation**: Immediate access revocation if violation ongoing; corrective action plan within 14 calendar days.
6. **Reporting**: Investigation report to CISO, CFO, and Executive Management (for financial violations or suspected fraud).

**Disciplinary action**: Per policy Non-Compliance section and organisation's disciplinary procedures.

---

## Training and Awareness

**Annual SoD awareness training** shall be provided to all employees covering:
- Purpose of segregation of duties (fraud and error prevention).
- Examples of conflicting duties (financial, IT, procurement).
- Individual responsibilities (do not approve your own work, report conflicts).
- Exception process (how to request exceptions properly).
- Consequences of SoD violations (disciplinary action, potential fraud implications).

**Role-specific training**:
- **Department Heads**: Weekly management review procedures for compensating control areas; how to identify new conflicts.
- **IT Operations**: RBAC configuration, mutual exclusion implementation, audit trail protection.
- **Finance team**: Financial segregation requirements, approval workflow compliance.

Training completion tracked; target: **100% of employees with segregation responsibilities trained annually**.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **SoD matrix** documenting all identified conflicting duty combinations and segregation status | CISO | *Reviewed annually; updated upon organisational change* |
| 2 | **Access rights reports** showing role assignments across systems, verified against SoD matrix | IT Operations | *Generated quarterly; reviewed by CISO* |
| 3 | **Compensating control register** with risk acceptance sign-off by Executive Management | CISO | *Reviewed quarterly; updated upon trigger events* |
| 4 | **Exception Register** with approval evidence, compensating controls, and closure records | CISO | *Reviewed monthly; reported quarterly to Executive Management* |
| 5 | **Management review records** for compensating control areas (weekly transaction reviews) | Department Heads | *Weekly; retained for 3 years* |
| 6 | **Independent review reports** for areas where segregation is not achievable | Internal Audit | *Quarterly; retained for 3 years* |
| 7 | **RBAC configuration evidence** showing mutual exclusion constraints in access control systems | IT Operations | *Captured annually or upon change; retained for 3 years* |
| 8 | **Workflow approval records** showing multi-party control for financial and system changes | IT Operations | *Per transaction; retained per retention schedule* |
| 9 | **Audit log integrity verification** records for segregated process logging | IT Operations | *Monthly; retained for 3 years* |
| 10 | **Annual SoD matrix review** sign-off and updated matrix | CISO | *Annually; retained for 3 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, SoD matrix reviews, access rights analysis against the conflict matrix, compensating control effectiveness assessments, exception register audits, internal and external audits, and feedback to the policy owner.

The following metrics shall be tracked and reported to the CISO quarterly:

| Metric | Target | Red Threshold |
|--------|--------|---------------|
| Segregation conflicts identified and documented | 100% of processes reviewed | <80% coverage |
| Time to resolve identified conflicts | 30 calendar days | >60 calendar days |
| Active exceptions | Minimised; trending downward | >5 concurrent or any >90 days |
| Compensating control quarterly review completion | 100% | <80% |
| SoD matrix annual review completed on schedule | Yes | Overdue >30 days |

**Reporting requirements**:
- **Monthly CISO dashboard**: Exception Register status, active exceptions, overdue conflict resolutions.
- **Quarterly Executive Management report**: Metrics status, trend analysis (conflicts resolved vs. new conflicts identified), compensating control effectiveness assessment.
- **Annual Management Review**: Full SoD programme effectiveness assessment including metrics trends, significant findings, and improvement recommendations.

Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk acceptance, compensating controls, and a defined review date. Planned exceptions require joint CISO and Executive Management approval. Exceptions shall be reported to the Management Review Team. Permanent exceptions to financial segregation and exceptions eliminating audit trail capabilities are not permitted.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Segregation violations involving financial processes shall be reported to the CFO and may trigger additional investigation under the organisation's fraud response procedures.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to organisational structure, new systems or processes, audit findings, regulatory changes, exception trends, compensating control effectiveness, and lessons learned from segregation-related incidents. Nonconformities related to this policy shall be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Areas of the ISO 27001 Standard Addressed

Segregation of Duties Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.2 Information security roles and responsibilities |
| Clause 5.3 Organisational roles, responsibilities and authorities | **5.3 Segregation of duties** |
| Clause 6.1 Actions to address risks and opportunities | 5.4 Management responsibilities |
| Clause 7.3 Awareness | 5.15 Access control |
| Clause 8.1 Operational planning and control | 5.16 Identity management |
| Clause 9.1 Monitoring, measurement, analysis and evaluation | 5.18 Access rights |
| Clause 10.2 Nonconformity and corrective action | 8.2 Privileged access rights |
| | 8.3 Information access restriction |
| | 8.15 Logging |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures (segregation of duties as organisational measure protecting data processing integrity) |
| Swiss DSV (Data Protection Ordinance) | Art. 1-3 — Minimum requirements for data security |
| Swiss CO Art. 728a | Internal control system — auditors shall examine existence of ICS including duty segregation controls |
| EU GDPR (where applicable) | Art. 32 — Security of processing (appropriate technical and organisational measures) |
| ISO/IEC 27001:2022 | Annex A Control 5.3 — Segregation of duties |
| ISO/IEC 27002:2022 | Section 5.3 — Implementation guidance for segregation of duties |
| NIST SP 800-53 Rev 5 | AC-5 (Separation of Duties) — Dividing mission functions among different individuals or roles |
| CIS Controls v8 | Control 5 (Account Management) and Control 6 (Access Control Management) — Safeguards supporting duty segregation through access governance |
| COSO Internal Control Framework | Principle 10 — Segregation of duties as part of control activities |

---

<!-- QA_VERIFIED: 2026-02-07 -->

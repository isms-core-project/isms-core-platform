**ISMS-OP-POL-A.8.33-34 — Test Information and Audit Testing Protection**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Test Information and Audit Testing Protection |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.33-34 |
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

- ISO/IEC 27001:2022 Control A.8.33 — Test information
- ISO/IEC 27001:2022 Control A.8.34 — Protection of information systems during audit testing
- ISO/IEC 27002:2022 Sections 8.33 and 8.34 — Implementation guidance
- NIST SP 800-53 Rev 5 — SA-11 (Developer Testing and Evaluation), CA-8 (Penetration Testing), AU-11 (Audit Record Retention)
- CIS Controls v8 — Safeguard 3.1–3.14 (Data Protection), Safeguard 18.1–18.5 (Penetration Testing)

**Related Annex A Controls**:

| Control | Relationship to Test Information and Audit Protection |
|---------|------------------------------------------------------|
| A.5.9 Inventory of information and other associated assets | Test environments and audit tools included in asset inventory |
| A.5.15–16–18 Identity and access management | Auditor and tester access provisioning, time-bound access controls |
| A.5.24–28 Incident management lifecycle | Incident handling during audit testing; vulnerability discovery escalation |
| A.5.34 Privacy and PII | PII protection in test data; anonymisation and pseudonymisation requirements |
| A.8.2–3–5 Authentication and privileged access | MFA requirements for test environment access; auditor authentication |
| A.8.8 Vulnerability management | Vulnerability handling for findings from penetration testing and audit |
| A.8.11 Data masking | Data masking techniques applied to production data used in testing |
| A.8.15 Logging | Audit trail for test data handling and auditor access activities |
| A.8.16 Monitoring | Real-time monitoring during active audit and penetration testing |
| A.8.31 Separation of development, test and production environments | Environment isolation for test data protection |

**Related Internal Policies**:

- Identity and Access Management Policy
- Data Masking Policy
- Logging Policy
- Monitoring Activities Policy (A.8.16)
- Vulnerability Management Policy
- Incident Management Policy
- Information Classification and Handling Policy
- Environment Separation Policy

---

# Test Information and Audit Testing Protection Policy

## Purpose

The purpose of this policy is to ensure that test information is appropriately selected, protected, and managed, and that audit tests and other assurance activities involving assessment of operational systems are planned and agreed to minimise disruption while maintaining system integrity.

This policy addresses two complementary concerns: protecting sensitive data from exposure through test environments (A.8.33), and protecting operational systems from unintended impact during audit and security testing (A.8.34).

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data used in or exposed through test environments. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 25 (data protection by design and by default) and Art. 32 (security of processing) requirements also apply. Test data management is a key technical measure for demonstrating that personal data is not unnecessarily exposed through non-production environments.

## Scope

This policy applies to all test data selection, creation, protection, and disposal activities, and to all audit, penetration testing, and assurance activities involving assessment of operational systems.

This includes:

- All test data used in development, QA, staging, UAT, training, sandbox, and demonstration environments.
- All production data copies, extracts, or derivatives used for testing purposes.
- All synthetic, anonymised, pseudonymised, and masked test datasets.
- All internal security audits and assessments.
- All external certification audits (ISO 27001 and equivalent).
- All penetration testing, vulnerability assessments, and active security testing.
- All third-party security assessments and regulatory compliance audits.
- All personnel involved in testing, audit, or assurance activities, including employees, contractors, internal auditors, external auditors, and penetration testers.

**Out of scope**: Production environment operations (covered under operational policies); routine automated monitoring (covered under A.8.16); data masking technique specifications and tool configuration (covered under A.8.11); environment architecture and separation requirements (covered under A.8.31); secure coding and development testing practices (covered under A.8.25–26–29).

## Principle

Test data shall be treated as a potential vector for data breach. The default position is that production data containing personal data, sensitive information, or confidential business data shall not be used in test environments. Where production-derived data is required, it shall be anonymised, pseudonymised, or masked before use.

Audit and assurance activities shall be conducted with the minimum access and impact necessary to achieve their objectives. Auditors shall receive read-only access by default, testing shall be time-bound and scope-limited, and operational systems shall be protected from unintended disruption.

---

## Test Data Selection

The organisation shall establish a clear hierarchy of preference for test data sources.

**Test Data Source Hierarchy** (in order of preference):

| Priority | Data Source | Description | Approval Required |
|----------|-------------|-------------|-------------------|
| 1 | **Synthetic data** | Artificially generated data with no relation to real individuals or business records | Development Manager |
| 2 | **Anonymised data** | Irreversibly de-identified production data where re-identification is not reasonably possible | Information Security Manager |
| 3 | **Pseudonymised data** | Production data with identifiers replaced by pseudonyms; re-identifiable with separate key | Information Security Manager + Data Owner |
| 4 | **Masked production data** | Production data with sensitive fields obscured using approved masking techniques | CISO + Data Owner |
| 5 | **Direct production copy** | Unmodified production data (exceptional circumstances only) | CISO + DPO + Data Owner |

Direct production copies shall only be permitted where all other options are demonstrably inadequate, with documented justification, time-limited approval (maximum 30 days), enhanced access controls, and mandatory deletion upon completion.

**Test Data Source Decision Tree**:

To determine the appropriate test data source, apply the following decision logic:

```
Does the test require real data characteristics (distributions, edge cases)?
+-- NO --> Use Synthetic Data (Priority 1)
+-- YES
    +-- Can you generate synthetic data with those characteristics?
        +-- YES --> Use Synthetic Data (Priority 1)
        +-- NO
            +-- Is the data personal data under nFADP/GDPR?
                +-- NO --> Use Masked Production Data (Priority 4)
                +-- YES
                    +-- Can re-identification be made impossible?
                        +-- YES --> Use Anonymised Data (Priority 2)
                        +-- NO --> Use Pseudonymised Data (Priority 3)
                            (Requires Information Security Manager + Data Owner approval)
```

Where a decision results in Priority 3 or higher, the Data Owner and Information Security Manager shall be consulted before proceeding.

**Test Data Classification**: Test data shall be classified according to the organisation's information classification scheme. Production-derived test data inherits the classification of the source data until masking or anonymisation is validated. Synthetic data shall be classified based on business context (typically Internal). Classification determines the protection controls required.

---

## Test Data Protection

### Anonymisation and Pseudonymisation

When production data is required for testing, the organisation shall apply data protection techniques before the data is accessible in any test environment.

**Anonymisation Requirements**:

- Anonymisation shall render re-identification not reasonably possible, considering available means of re-identification, cost of re-identification, and intended purpose.
- Anonymised data is no longer personal data under nFADP or GDPR and may be classified at a lower level with Data Owner approval.
- Anonymisation techniques shall be validated before use and reviewed annually for continued effectiveness, accounting for advances in re-identification techniques including AI-assisted methods.

**Pseudonymisation Requirements**:

- Pseudonymised data remains personal data and shall be protected accordingly.
- The mapping key (pseudonym-to-identity) shall be stored separately from the pseudonymised dataset, with access restricted to authorised personnel.
- Pseudonymised test data shall be subject to the same access controls as the original data classification.

### Data Masking

Data masking shall be applied using [Data Masking Tool] (e.g., Informatica, Delphix, IBM InfoSphere Optim, or equivalent) or approved scripted methods.

**Masking Requirements**:

| Data Type | Masking Technique | Validation |
|-----------|-------------------|------------|
| Personal names | Substitution with synthetic names | Verify no original names remain |
| Email addresses | Domain replacement (e.g., @example.com) | Verify format preserved, no real addresses |
| National identifiers (AHV/SSN) | Format-preserving randomisation | Verify format valid but non-existent |
| Financial data (IBAN, account numbers) | Format-preserving encryption or randomisation | Verify format preserved, referential integrity maintained |
| Dates of birth | Date shifting (consistent offset per record) | Verify age distributions preserved for testing |
| Free-text fields | Redaction or synthetic replacement | Verify no PII leakage in unstructured text |
| Addresses | Substitution with synthetic addresses | Verify geographic distribution preserved if needed |

**Data Masking Quick Reference**:

The following table provides a quick reference for common data types and recommended masking approaches:

| Data Type | Recommended Technique | Tool/Method Example |
|-----------|----------------------|---------------------|
| Names | Substitution | Faker library: `fake.name()` (Swiss locale) |
| Emails | Domain swap | `user123@testdomain.example` |
| Phone numbers | Format-preserving randomisation | Faker library: `fake.phone_number()` |
| Dates | Consistent offset | All dates shift by random +/- 1-3 years |
| Addresses | Substitution | Faker library: `fake.address()` (Swiss locale) |
| Free text | Redaction or NER + replacement | Cloud NLP service + custom replacement logic |
| Financial values | Format-preserving encryption | FPE algorithm with approved key management |

**Masking Validation**: Masked data shall be validated before release to test environments to confirm that original sensitive values are not recoverable, data format is preserved for application compatibility, referential integrity is maintained across related datasets, and no plaintext personal data exists in the masked output. Validation results shall be documented and approved by the Information Security Manager.

### Synthetic Data Generation

Where synthetic data is used, it shall be generated to preserve the statistical properties, data distributions, and referential integrity required for effective testing without containing any real personal or business data.

Synthetic data generators shall be documented, version-controlled, and reviewed periodically to ensure generated data remains fit for purpose. The organisation shall maintain records of synthetic data generation parameters and validation results.

---

## Test Data Lifecycle

### Creation and Provisioning

- Test data creation or refresh shall be requested through a documented process.
- Data Owner approval is required before any production-derived data enters a test environment.
- Masking or anonymisation shall be applied before data is accessible in the test environment (not after).
- All data provisioning activities shall be logged for audit purposes.

### Retention and Disposal

Test data containing masked or pseudonymised production data shall be retained only for the duration of the testing requirement. Upon project completion, test data shall be deleted within 30 days.

For continuous testing environments:

- Test data shall be reviewed quarterly for continued need.
- Data older than 90 days without documented active usage shall be flagged for deletion.
- Retention beyond 90 days requires Data Owner approval with documented business justification.
- Automated retention monitoring shall alert when data exceeds thresholds.

**Disposal**: Test data disposal shall follow the same secure deletion procedures as production data of equivalent classification. Disposal shall be verified and documented.

### Data Refresh

When test data is refreshed from production sources:

- Fresh masking shall be applied to each refresh cycle (prior masking does not carry over).
- Refresh procedures shall be documented and approved by the Data Owner.
- Refresh activities shall be logged, including source system, volume, masking method, and operator.
- Previous test data shall be securely deleted before or immediately after refresh completion.

---

## Audit Planning and Governance

### Pre-Audit Agreement

Before any audit testing commences, the organisation shall establish formal agreement between the tester and appropriate management covering:

- **Scope**: Systems, networks, applications, and data to be tested.
- **Methodology**: Testing methods, tools, and techniques to be used.
- **Timing**: Start and end dates, testing windows, and any blackout periods.
- **Boundaries**: Systems and data explicitly excluded from testing.
- **Escalation**: Procedures for issues, incidents, or critical findings during testing.
- **Confidentiality**: Non-disclosure requirements for audit findings and accessed data.
- **Reporting**: Expected deliverables, format, and timelines for findings.

Pre-audit agreements shall be documented, signed by both parties, and retained as evidence.

### Scheduling and Coordination

Audit testing activities shall be scheduled to minimise operational impact:

- Critical business periods (e.g., month-end close, peak trading, system maintenance windows) shall be avoided unless specifically testing resilience during those periods.
- Testing windows shall be coordinated with IT Operations and relevant system owners.
- Affected stakeholders shall be notified of planned testing activities, including timing, scope, and potential impact.
- Emergency or unscheduled testing shall follow an expedited approval process with post-facto review within 48 hours.

---

## Auditor Access Control

Access granted to auditors, assessors, and penetration testers shall follow the principle of least privilege.

**Access Requirements**:

| Requirement | Standard |
|-------------|----------|
| Default access level | Read-only to information and software |
| Write or admin access | Only when read-only is insufficient; administrator performs access on behalf of auditor where feasible |
| Authentication | MFA required for access to any system containing sensitive data |
| Duration | Time-bound to the agreed audit period; automatic expiration |
| Scope | Limited to systems and data defined in the pre-audit agreement |
| Logging | All auditor access logged and monitored throughout the engagement |

Where read-only access is not feasible, an administrator with the necessary access rights shall perform system or data access on behalf of the auditor, with the auditor observing and directing.

**Device Security**: Before granting access, the organisation shall verify that auditor devices meet minimum security requirements, including current operating system patches, active endpoint protection, full disk encryption, and no known malware. Auditors using non-compliant devices shall be provided with organisation-managed devices or virtual desktop access.

**Access Deprovisioning**: Auditor access shall be revoked within 24 hours of audit completion or the agreed access expiration date, whichever is earlier. Deprovisioning shall be verified and documented.

---

## Penetration Testing Controls

### Authorisation and Rules of Engagement

Penetration testing and active security testing shall be authorised in writing by the CISO (or delegate) and relevant system owners before testing begins.

**Rules of Engagement** shall document:

- Authorised testing scope (IP ranges, applications, accounts, physical locations).
- Prohibited activities (denial of service, social engineering of specific individuals, data exfiltration of real data).
- Testing methodology and framework (e.g., OWASP Testing Guide, PTES, NIST SP 800-115).
- Communication protocols (primary contact, emergency contact, status reporting frequency).
- Data handling requirements for any data accessed during testing.
- Incident procedures if testing causes unintended operational impact.
- Evidence handling and secure destruction of test artifacts.

### Operational Safeguards

During penetration testing:

- IT Operations shall be on standby with the ability to intervene if operational systems are affected.
- Testing shall be conducted in isolated or non-production environments where possible.
- Where production testing is required, rollback and recovery procedures shall be prepared in advance.
- Testing shall be suspended immediately if unintended operational impact occurs, and shall not resume without explicit approval from the IT Operations Manager and CISO.

### Findings Management

- Critical vulnerabilities discovered during testing shall be reported to the Security Team immediately (not deferred to the final report).
- Vulnerabilities shall be handled per the organisation's vulnerability management process (A.8.8).
- Testers shall not exploit vulnerabilities beyond the scope necessary for verification and risk assessment.
- Penetration testing reports shall be classified as Confidential and distributed only to authorised recipients.

### Testing Status Communication

During active penetration testing or extended audit engagements, the tester shall provide daily status updates to the designated organisational contact. Status updates shall include:

- Summary of activities completed during the reporting period.
- Summary of findings identified (by severity: Critical, High, Medium, Low).
- Planned activities for the next reporting period.
- Any issues, concerns, or operational impacts observed.

Critical findings shall be reported immediately by phone to the CISO, in addition to any daily status update. The format and frequency of status reporting shall be agreed in the pre-audit agreement.

---

## Audit Tool Management

### Tool Approval and Control

Audit and testing tools used to assess the organisation's systems shall be:

- Pre-approved by the Information Security Manager before use on organisational systems.
- Verified as free from malware or unauthorised functionality.
- Documented in the pre-audit agreement (tool name, version, purpose).
- Restricted to the agreed scope of testing.

Audit tools shall not be installed on production systems without explicit CISO approval. Where possible, audit tools shall be run from dedicated audit workstations or isolated virtual environments.

### Tool Protection

Audit tools, scripts, and configuration files shall be protected from unauthorised access both during and after the engagement. Tools capable of exploiting vulnerabilities or bypassing security controls shall be removed from organisational systems upon audit completion.

---

## Audit Log Protection

Logs generated during audit and testing activities shall be protected from unauthorised modification or deletion to maintain the integrity of the audit trail.

**Log Protection Requirements**:

- Audit logs shall be written to tamper-evident storage (e.g., write-once media, SIEM with integrity controls, or equivalent).
- Logs shall capture: timestamp (UTC), user identity, source IP, action performed, system affected, and outcome (success/failure).
- Logs generated during audit testing shall be retained per the organisation's log retention policy (minimum 1 year for access events, 3 years for security events).
- Logs shall be available for review if audit findings are disputed or require clarification.
- During active penetration testing, enhanced monitoring shall be enabled to distinguish authorised testing activity from genuine security events.

---

## Incident Handling During Audit Testing

If audit or penetration testing causes unintended operational impact:

1. **Immediate suspension**: Testing shall cease immediately upon detection of unintended impact.
2. **Notification**: IT Operations shall be notified for containment and recovery.
3. **Root cause analysis**: The cause of the unintended impact shall be documented.
4. **Remediation**: Affected systems shall be restored to normal operation.
5. **Resumption approval**: Testing shall not resume without explicit approval from the IT Operations Manager.
6. **Lessons learned**: Incident shall be documented and incorporated into future pre-audit planning.

Genuine security incidents discovered during audit testing (e.g., evidence of prior compromise, active threats) shall be escalated immediately per the organisation's incident management process (A.5.24-28).

---

## Definitions

| Term | Definition |
|------|------------|
| **Anonymisation** | Irreversible process removing all identifying information such that re-identification is not reasonably possible |
| **Audit testing** | Systematic examination of systems, controls, and processes to verify compliance and effectiveness |
| **Data masking** | Process of obscuring original data with modified content while maintaining format and usability for testing |
| **Grey box testing** | Penetration testing approach where the tester has partial knowledge of the target environment |
| **Penetration testing** | Authorised simulated attack on systems to identify exploitable security vulnerabilities |
| **Production data** | Live operational data from business systems containing real personal or business information |
| **Pseudonymisation** | Replacement of direct identifiers with pseudonyms; re-identifiable with a separately stored mapping key |
| **Rules of engagement** | Documented agreement defining the scope, boundaries, methods, and constraints for penetration testing |
| **Synthetic data** | Artificially generated data containing no real personal or business information, designed to mimic production data characteristics |
| **Test environment** | Non-production system used for development, testing, training, or demonstration purposes |

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; penetration testing authorisation; exception approval for direct production data use; oversight of audit testing governance; annual policy review; reporting to Executive Management |
| **Information Security Manager** | Policy maintenance; audit coordination; masking validation approval; exception review; compliance monitoring; quarterly reporting to CISO |
| **Data Protection Officer** | Test data privacy compliance; anonymisation adequacy review; nFADP and GDPR alignment; approval for pseudonymised data use |
| **IT Operations Manager** | Production system protection during audit testing; scheduling coordination; incident response during testing; auditor device verification |
| **Data Owners** | Test data authorisation; masking approval; data classification decisions; retention review for test data derived from their systems |
| **Development Manager / QA Manager** | Test environment management; test data provisioning procedures; developer and tester compliance; synthetic data generation oversight |
| **Security Team** | Audit tool management; penetration testing coordination; vulnerability finding handling; enhanced monitoring during testing |
| **Internal Audit** | Audit planning and engagement management; pre-audit agreement preparation; findings reporting and follow-up |
| **External Auditors and Penetration Testers** | Compliance with access restrictions, rules of engagement, and confidentiality requirements; scope adherence; immediate reporting of critical findings |
| **All Testing Personnel** | Compliance with test data handling requirements; no use of unmasked production data without approval; incident reporting; secure disposal of test artifacts |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Test data inventory** listing all test datasets, source type (synthetic/anonymised/masked), classification, and owning team | Development Manager / QA Manager | Maintained continuously; reviewed quarterly | Life of dataset + 1 year |
| 2 | **Test data request and approval records** (requests, justifications, Data Owner approvals, masking method used) | Data Owners / Information Security Manager | Per request | 3 years |
| 3 | **Data masking validation records** (validation test results, Information Security Manager approval, date) | Information Security Manager / Security Team | Per masking operation | 3 years |
| 4 | **Synthetic data generation records** (generator parameters, validation results, version) | Development Manager | Per generation | 2 years |
| 5 | **Test data retention and disposal records** (quarterly reviews, deletion confirmations, disposal method) | Development Manager / QA Manager | Quarterly review; per disposal event | 3 years |
| 6 | **Pre-audit and penetration testing agreements** (scope, methodology, timing, rules of engagement, signatures) | CISO / Internal Audit | Per engagement | 3 years |
| 7 | **Auditor and tester access records** (access provisioning, scope, duration, deprovisioning confirmation) | IT Operations / Information Security Manager | Per engagement | 3 years |
| 8 | **Auditor device compliance verification records** (security check results, approval) | IT Operations | Per engagement | 1 year |
| 9 | **Penetration testing reports and findings** (full reports, remediation tracking, closure evidence) | CISO / Security Team | Per engagement | 3 years |
| 10 | **Audit tool approval records** (tool name, version, purpose, Information Security Manager approval) | Information Security Manager | Per engagement | 2 years |
| 11 | **Audit and testing activity logs** (auditor access logs, testing activity records, monitoring alerts) | IT Operations / Security Team | Continuous | Per log retention policy (1-3 years) |
| 12 | **Incident reports from testing activities** (unintended impacts, root cause, remediation, lessons learned) | IT Operations / CISO | Per incident | 3 years |
| 13 | **Exception register** (requests for direct production data use, approvals, compensating controls, expiration) | Information Security Manager | Maintained continuously; reviewed quarterly | Exception duration + 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, test data inventories, masking validation records, audit engagement documentation, access logs, penetration testing reports, internal and external audits, and feedback to the policy owner.

**Compliance Metrics**:

| Metric | Target | Measurement Frequency |
|--------|--------|-----------------------|
| Test environments using synthetic or anonymised data (no unmasked production data) | >= 95% | Quarterly |
| Masking validation completed and approved before test data release | 100% | Per masking operation |
| Pre-audit agreements signed before testing commences | 100% | Per engagement |
| Auditor access deprovisioned within 24 hours of audit completion | 100% | Per engagement |
| Penetration testing findings remediated within SLA | >= 90% | Per engagement |
| Test data disposed within 30 days of project completion | >= 90% | Quarterly |

**Compliance Scoring**:

| Component | Weight | Calculation |
|-----------|--------|-------------|
| Test Data Protection Compliance | 40% | (Test environments with approved data sources + masking validations completed) / Total test environments x 100 |
| Audit Governance Compliance | 30% | (Engagements with signed pre-audit agreements + access properly provisioned and deprovisioned) / Total engagements x 100 |
| Findings Management Compliance | 20% | (Penetration testing and audit findings remediated within SLA) / Total findings x 100 |
| Data Lifecycle Compliance | 10% | (Test datasets disposed within policy timelines) / Total datasets requiring disposal x 100 |

**Non-Compliance Handling**: Below 70% requires immediate CISO escalation and remediation plan. 70-89% requires Information Security Manager oversight with monthly reviews. 90% and above follows standard quarterly monitoring.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk acceptance, compensating controls (enhanced logging, reduced retention, additional access restrictions), and a defined review date (maximum 12 months). Exceptions for direct production data use in test environments additionally require DPO approval. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Use of unmasked production data in test environments without approval shall be treated as a data handling incident and investigated accordingly. Policy violations shall be documented, investigated by the Information Security Manager, and reported to the CISO.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider advances in anonymisation and synthetic data generation techniques, emerging re-identification risks (including AI-assisted de-anonymisation), changes to penetration testing methodologies and threat landscape, regulatory changes (particularly nFADP guidance and GDPR enforcement precedent), audit findings and lessons learned from testing incidents, and feedback from development, QA, and audit teams.

---

# Areas of the ISO 27001 Standard Addressed

Test Information and Audit Testing Protection Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| Clause 9.2 Internal audit | 8.11 Data masking |
| | **8.33 Test information** |
| | **8.34 Protection of information systems during audit testing** |
| | 8.31 Separation of development, test, and production environments |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data protection; anonymisation and pseudonymisation as data protection measures; test data containing personal data subject to nFADP requirements |
| Swiss DSV (Data Protection Ordinance) | Art. 1-3 — Minimum requirements for data security, including test environment controls |
| EU GDPR (where applicable) | Art. 5(1)(c) — Data minimisation (no unnecessary production data in test environments); Art. 25 — Data protection by design and by default; Art. 32 — Security of processing (pseudonymisation as a security measure) |
| ISO/IEC 27001:2022 | Annex A Controls 8.33 and 8.34 |
| ISO/IEC 27002:2022 | Sections 8.33 and 8.34 — Implementation guidance |
| NIST SP 800-53 Rev 5 | SA-11 (Developer Testing and Evaluation), CA-8 (Penetration Testing), AU-11 (Audit Record Retention), SI-12 (Information Management and Retention) |
| CIS Controls v8 | 3.1-3.14 (Data Protection), 18.1-18.5 (Penetration Testing) |

---

<!-- QA_VERIFIED: 2026-02-08 -->

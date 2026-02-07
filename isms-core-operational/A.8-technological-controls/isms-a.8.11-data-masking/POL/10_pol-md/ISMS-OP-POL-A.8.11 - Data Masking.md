**ISMS-OP-POL-A.8.11 — Data Masking**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Masking |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.11 |
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

- ISO/IEC 27001:2022 Control A.8.11 — Data masking

**Related Internal Policies**:

- Information Classification and Handling Policy
- Access Control Policy
- Privacy and Protection of PII Policy
- Use of Cryptography Policy
- Secure Development Policy
- Information Deletion Policy

**Related Annex A Controls**:

| Control | Relationship to Data Masking |
|---------|------------------------------|
| A.5.12 Classification of information | Data classification drives masking requirements per sensitivity level |
| A.5.15 Access control | Masking provides defence in depth beyond access controls |
| A.5.34 Privacy and protection of PII | Pseudonymisation and anonymisation as privacy safeguards |
| A.8.3 Information access restriction | Privileged users may access unmasked data with monitoring |
| A.8.10 Information deletion | Deletion is separate from masking; both reduce exposure |
| A.8.24 Use of cryptography | Encryption protects data at rest/in transit; masking obscures data in use |
| A.8.25 Secure development lifecycle | Developers use masked data in non-production environments |

---

# Data Masking Policy

## Purpose

The purpose of this policy is to ensure the proper use of data masking to protect sensitive information — including personally identifiable information (PII), financial data, and credentials — by obscuring data when full visibility is not required for legitimate business purposes.

This policy supports Swiss nFADP (revDSG) Art. 7 (data protection by design and by default) and Art. 8 (data security through technical and organisational measures). Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 25 (data protection by design and default) and Art. 32 (security of processing, including pseudonymisation) also apply. Data masking is a key technical measure for demonstrating compliance with data minimisation obligations under both frameworks.

## Scope

This policy applies to:

- All sensitive data categories: PII, financial data, health information, authentication credentials, proprietary business information, and any data classified as Confidential or Restricted.
- All environments: production (where operationally appropriate), test/QA, development, analytics, training, sandbox, and backup/archive systems.
- All masking use cases: non-production data provisioning, report generation, third-party data sharing, application development and testing, analytics, and machine learning model training.
- All employees, contractors, and third-party service providers handling sensitive data.

Data classified as Public per the organisation's classification scheme is out of scope. Encrypted data protection is covered under A.8.24 (Use of Cryptography). Data deletion and destruction are covered under A.8.10 (Information Deletion).

## Principle

Data masking is applied based on the principle of data minimisation: personnel shall only have access to real sensitive data when it is strictly necessary for their role and task. In all other cases, data shall be masked, pseudonymised, or anonymised to the extent that business utility is preserved.

Only organisation-approved masking techniques and tools shall be used. The selection of masking technique shall consider data sensitivity, regulatory requirements, reversibility needs, format preservation, and referential integrity.

---

## Data Classification and Masking Requirements

Masking requirements are determined by the organisation's information classification scheme (per Control A.5.12). The following table defines the masking obligation per classification level:

| Classification | Masking Requirement | Rationale |
|----------------|---------------------|-----------|
| **Restricted** | Mandatory masking in ALL non-production environments | Highest sensitivity — exposure causes severe harm |
| **Confidential** | Mandatory masking in non-production; risk-based in production | High sensitivity — exposure causes substantial harm |
| **Internal** | Risk-based masking where PII or regulatory requirements apply | Moderate sensitivity — selective masking based on content |
| **Public** | No masking required | No confidentiality requirement |

### Sensitive Data Categories Requiring Assessment

| Category | Examples | Typical Classification |
|----------|----------|------------------------|
| **Personally Identifiable Information (PII)** | Name, AHV/SSN, passport number, email, phone, address | Restricted / Confidential |
| **Financial Data** | Credit card number (PAN), IBAN, account balance, salary, tax ID | Restricted / Confidential |
| **Health Information** | Medical record number, diagnoses, prescriptions, lab results | Restricted |
| **Authentication Credentials** | Passwords, API keys, tokens, private keys, connection strings | Restricted |
| **Proprietary Business Data** | Trade secrets, pricing strategies, customer contracts | Confidential |
| **Special Category Data** (GDPR Art. 9 / nFADP sensitive data) | Racial/ethnic origin, political opinions, religious beliefs, biometric data | Restricted |

### Data Discovery and Inventory

The organisation shall maintain an inventory of sensitive data requiring masking, including:

- Systems and databases containing sensitive data.
- Data elements (tables, columns, fields) requiring masking.
- Data classification per element and applicable regulatory requirements.
- Data owner responsible for masking decisions.

Data discovery shall be automated for all environments containing Restricted or Confidential data, using [Data Discovery Tool] or equivalent. Automated discovery shall scan for known sensitive data patterns (PII patterns, credit card numbers, AHV/SSN formats, health identifiers) on at least a quarterly basis. Manual inventory is acceptable for organisations with limited data estates and no Restricted data, but shall be supplemented by automated discovery as the data estate grows.

Data Owners are accountable for classifying data in their domains, determining masking requirements, approving masking techniques for their data, and validating masking effectiveness.

---

## Approved Masking Techniques

The following masking techniques are approved for organisational use:

| Technique | Description | Reversibility | Primary Use Cases |
|-----------|-------------|---------------|-------------------|
| **Static Data Masking (SDM)** | Permanent replacement of data in non-production databases before data leaves the production environment | Irreversible | Non-production environments, external data sharing |
| **Dynamic Data Masking (DDM)** | Real-time masking at query time based on user role; original data remains unchanged in storage | N/A (original unchanged) | Production role-based access, compliance display rules |
| **Redaction / Nullification** | Complete removal or replacement with placeholder characters (e.g., `****`, `[REDACTED]`) | Irreversible | Reports, exports, screenshots, UI display |
| **Substitution** | Replacement with realistic fictitious data preserving format and distribution | Irreversible | Test data generation, maintaining data utility |
| **Tokenisation** | Replacement with non-sensitive tokens; original data stored in secure token vault | Reversible (with vault access) | Payment systems, referential integrity, PCI DSS |
| **Pseudonymisation** | Replacement with pseudonyms; re-identifiable only with separately held key | Reversible (with key) | GDPR/nFADP compliance, research, analytics |
| **Anonymisation** | Irreversible removal of all identifying information; no keys or mappings retained | Irreversible | Public data release, statistical analysis, open datasets |

### Technique Selection Criteria

When selecting a masking technique, the following factors shall be considered:

1. **Data sensitivity**: higher sensitivity requires stronger, less reversible masking.
2. **Regulatory requirements**: GDPR pseudonymisation (Art. 32, Art. 89), PCI DSS display masking (Req. 3.4–3.5), nFADP data minimisation (Art. 6).
3. **Business use case**: development/testing, analytics, external sharing, or training.
4. **Reversibility need**: whether a legitimate need exists to recover original data.
5. **Format preservation**: whether the application requires data format to be maintained.
6. **Referential integrity**: whether cross-table relationships and foreign keys must remain valid.
7. **Performance impact**: real-time DDM overhead versus batch SDM processing.

New masking techniques or significant modifications to approved techniques shall be proposed to the Security Team, undergo security review and testing, and be approved by the CISO before use.

### Pseudonymisation vs. Anonymisation (Regulatory Distinction)

Under both GDPR and nFADP, pseudonymised data remains personal data because re-identification is possible with the separately held key. Anonymised data — where re-identification is no longer reasonably possible — falls outside the scope of data protection regulation. The organisation shall ensure the correct technique is applied based on whether the data must remain within data protection scope (pseudonymisation) or can be removed from scope entirely (anonymisation).

**Anonymisation data utility assessment**: Before applying anonymisation, the Data Owner shall assess whether the anonymised data retains sufficient business utility for its intended purpose. The assessment shall consider:

- Whether statistical properties (distributions, correlations, trends) are preserved.
- Whether the anonymised data supports the intended analysis, training, or testing use case.
- Whether excessive generalisation or suppression renders the data unusable.
- Trade-offs between privacy protection (higher k-anonymity) and data utility (less generalisation).

Where anonymisation excessively reduces data utility, pseudonymisation with appropriate access controls may be a preferable alternative.

Pseudonymisation keys shall be stored separately from the pseudonymised data, with the following separation requirements:

- **Physical or logical separation**: Keys shall be stored in a different system, database, or security domain from the pseudonymised data. Co-locating keys and data on the same server or in the same database is prohibited.
- **Access separation**: Personnel with access to pseudonymised data shall not have access to re-identification keys unless specifically authorised for a documented purpose. Dual-control (two-person authorisation) shall be required for re-identification of Restricted data.
- **Re-identification logging**: All re-identification events shall be logged with requestor identity, justification, data scope, and approval reference.

Key management shall follow the Use of Cryptography Policy (A.8.24).

---

## Prohibited Practices

The following are NOT acceptable as masking techniques:

| Prohibited Practice | Reason |
|---------------------|--------|
| **ROT13 or Caesar cipher** | Trivially reversible; not cryptographically secure |
| **Reversible encoding only** (Base64, URL encoding, hex) | Not masking — just encoding; easily reversed by anyone |
| **Simple character substitution** (A=1, B=2) | Predictable pattern; trivially reversible |
| **Client-side masking only** (JavaScript / UI layer) | Bypassable — data remains unmasked in the backend |
| **Self-designed "encryption"** | Unvalidated security; not accepted for compliance |
| **Production data in non-production without any masking** | Core policy violation |
| **Using same masked dataset indefinitely without refresh** | Stale data; potential for circumvention over time |

These practices provide an appearance of security without actual protection. They are not acceptable under any circumstances, and no exception may be granted for their use.

---

## Environment Coverage Requirements

Sensitive data shall be masked in environments where full data visibility is not required for legitimate business operations.

| Environment | Masking Requirement | Rationale |
|-------------|---------------------|-----------|
| **Production** | Risk-based; apply DDM where operationally feasible | Business operations may require some real data; document justification for unmasked data |
| **Test / QA** | Mandatory for Restricted and Confidential data | No business need for real sensitive data in testing |
| **Development** | Mandatory for Restricted and Confidential data | Developers do not need real sensitive data |
| **Analytics / BI** | Mandatory unless data is aggregated or anonymised | Analytics can function with masked or aggregated data |
| **Training / Demo** | Mandatory for ALL sensitive data — no exceptions | Training environments must use non-sensitive data |
| **Sandbox / Experimental** | Mandatory for ALL sensitive data — no exceptions | Uncontrolled environments are high risk |
| **Backup / Archive** | Same protection as source environment | Backups mirror source data sensitivity |

### SDM Implementation Requirements

- SDM shall be applied BEFORE data leaves the production environment.
- SDM shall maintain referential integrity across related tables. Where multi-table relationships exist, masking shall be applied consistently using the same masking key or mapping to preserve foreign key relationships, join integrity, and cross-table business rules. Referential integrity shall be validated through automated testing after each masking cycle.
- SDM shall preserve data format for application compatibility. Note: format preservation may reduce the masking entropy (number of possible masked values), which increases re-identification risk. For Restricted data, the organisation shall assess whether format-preserving masking provides sufficient security or whether non-format-preserving techniques with application-layer adaptation are required.
- Masked data shall be realistic enough for application testing.
- **Masked data refresh**: Non-production environments using SDM shall be refreshed with newly masked data at a defined frequency — at minimum quarterly for active development environments and semi-annually for less active environments. Refresh frequency shall account for production data changes that may affect test validity and for reducing the risk of masking circumvention through accumulated knowledge of stale masked datasets.

### DDM Implementation Requirements

- DDM shall be enforced at the database or application layer — not client-side.
- DDM rules shall be based on documented user roles and least privilege.
- DDM shall not be bypassable by users without appropriate authorisation. Bypass prevention controls shall include:
  - Direct database access (bypassing the application layer) shall be restricted to authorised database administrators.
  - DDM rules shall be enforced at the database engine level where supported, not solely at the application layer.
  - Attempts to query underlying unmasked data through views, stored procedures, or alternate access paths shall be blocked or logged and alerted.
  - Periodic testing shall verify that DDM cannot be circumvented through SQL injection, privilege escalation, or schema manipulation.
- Performance impact shall be assessed and kept within defined thresholds:
  - **Query latency**: DDM shall not add more than 15% latency to baseline query response times for standard queries.
  - **Throughput**: DDM shall not reduce database throughput by more than 10% under normal operating conditions.
  - **Baseline measurement**: Performance baselines shall be established before DDM deployment and re-measured quarterly.
  - **Escalation**: Where DDM exceeds performance thresholds, the Security Team shall evaluate alternative masking approaches (SDM pre-processing, application-layer masking, or DDM rule optimisation).

### Tokenisation Requirements

- The token vault shall be secured with access controls and encryption. Vault encryption keys shall be:
  - Generated and stored in a hardware security module (HSM) or [KMS] where available.
  - Rotated at least annually, with automated rotation preferred.
  - Backed up and recoverable per the organisation's key management procedures (A.8.24).
  - Access-controlled separately from the tokenised data — vault administrators shall not have direct access to tokenised datasets, and vice versa.
- Tokens shall be format-preserving where required (e.g., credit card format for PCI DSS).
- De-tokenisation shall require explicit authorisation and be logged. De-tokenisation access shall be reviewed quarterly as part of privileged access reviews.
- Vault key management shall follow the Use of Cryptography Policy (A.8.24).

---

## Testing and Validation

Masking implementations shall be tested before deployment and after any changes to masking configuration.

| Test Type | Purpose | When Required |
|-----------|---------|---------------|
| **Effectiveness testing** | Verify original data is not recoverable from masked output | Before deployment; after changes |
| **Referential integrity testing** | Verify cross-table relationships are preserved | Before deployment |
| **Format validation testing** | Verify masked data passes application validation rules | Before deployment |
| **Performance testing** | Verify DDM overhead is within acceptable limits | Before DDM deployment |
| **Re-identification risk assessment** | Verify anonymised/pseudonymised data cannot be re-identified | Annually; after data structure changes |
| **Regression testing** | Verify masking continues to function after system changes | After masking configuration changes |

### Validation Methods

- Sample data inspection: manual comparison of masked versus unmasked data.
- Automated pattern detection: scanning non-production environments for unmasked sensitive data patterns (e.g., credit card numbers, AHV numbers, email addresses).
- Reverse engineering attempts: attempting to recover original data from masked output.
- For anonymisation: statistical analysis with risk-based thresholds:
  - **Restricted data**: k-anonymity >= 20, l-diversity >= 5 where applicable.
  - **Confidential data**: k-anonymity >= 10, l-diversity >= 3 where applicable.
  - **Internal data**: k-anonymity >= 5 minimum.
  - Where k-anonymity thresholds cannot be met, data utility shall be assessed against the risk of re-identification, and alternative techniques (generalisation, suppression, noise addition) shall be applied to achieve the target threshold.

### Acceptance Criteria

Masking is acceptable when:

- Original sensitive data values are NOT present in masked datasets.
- Data format and referential integrity are preserved.
- Application functionality is not impaired.
- Performance impact is within acceptable limits.
- Regulatory requirements are met.

When testing identifies failures, implementation shall be corrected before production use, root cause documented, and re-testing performed.

### Assessment Frequency

- **Comprehensive assessment**: annually (aligned with internal audit programme).
- **Periodic verification**: quarterly for high-risk systems and recently changed environments.
- **Triggered assessment**: within 30 days of a significant data exposure incident, major system change affecting sensitive data, deployment of a new masking solution, or regulatory requirement change.

---

## Logging and Monitoring

The following masking-related events shall be logged where technically feasible:

- Masking process execution (start, completion, errors).
- Masking configuration changes (technique changes, rule updates). Configuration changes shall follow the organisation's change management process: requested by authorised personnel, reviewed by the Security Team, tested in a non-production environment, approved by the Data Owner and Security Team Lead before production deployment, and logged with before/after configuration states.
- Masking exceptions and bypasses (approved or attempted).
- Dynamic masking policy application (who accessed what data with which masking rule).
- Masking failures (processes that failed to complete).

**Log retention**:

| Event Type | Minimum Retention |
|------------|-------------------|
| Masking process logs | 90 days |
| Configuration changes | 12 months |
| Exception and bypass events | 12 months |
| Dynamic masking access logs | 90 days (Confidential+) |

Extended retention applies where regulatory requirements mandate longer periods.

The organisation shall monitor for masking process failures, repeated bypass attempts, unauthorised configuration changes, and DDM performance degradation. Alerts shall be integrated with the organisation's security monitoring programme.

**Re-identification attempt detection**: The organisation shall implement monitoring to detect potential re-identification attempts, including:

- Unusual query patterns against pseudonymised or anonymised datasets (e.g., systematic enumeration, cross-referencing with external data sources).
- Bulk data extraction from environments containing masked data.
- Attempts to access pseudonymisation keys or token vaults by unauthorised personnel.
- Correlation queries joining masked datasets with unmasked reference data.

Detected re-identification attempts shall be treated as High-severity security incidents and investigated immediately.

---

## Incident Response for Masking Failures

Data masking security incidents include:

| Incident Type | Severity | Response |
|---------------|----------|----------|
| Unmasked sensitive data discovered in non-production | High | Containment within 1 hour — stop data flow, delete exposed data, notify Data Owner |
| Masking process failure exposing sensitive data | Critical | Containment within 15 minutes — stop exposure, isolate affected systems, notify CISO |
| Successful re-identification of masked data | High | Assess technique weakness, strengthen masking |
| Masking bypass or circumvention attempt | High | Investigate, prevent recurrence |
| Unauthorised access to token vault or pseudonymisation keys | Critical | Key compromise response per A.8.24 |
| Data exfiltration from insufficiently masked environment | Critical | Full incident response, assess breach notification |

### Response Process

1. **Detect and report**: via monitoring, user reports, or testing.
2. **Classify**: severity based on data sensitivity and exposure scope.
3. **Contain**: stop data flow, isolate systems, prevent further exposure.
4. **Investigate**: root cause analysis, scope determination, impact assessment.
5. **Remediate**: fix masking, validate effectiveness, prevent recurrence.
6. **Notify**: internal escalation; assess regulatory breach notification requirements.
7. **Review**: lessons learned, control improvements.

### Breach Notification Assessment

Data exposure incidents shall be assessed for breach notification requirements:

- **Swiss nFADP**: Notification to FDPIC if high risk to personality or fundamental rights (Art. 24).
- **EU GDPR** (where applicable): Notification within 72 hours if risk to rights and freedoms (Art. 33–34).
- **Sector-specific**: PCI DSS breach notification, HIPAA breach notification (if applicable).

The DPO and Legal/Compliance shall be involved in all breach notification decisions.

---

## Exception Management

Exceptions to data masking requirements require:

- Documented business justification explaining why masking cannot be implemented.
- Risk assessment covering likelihood and impact of data exposure.
- Compensating controls (enhanced access controls, encryption, monitoring).
- Defined duration and path to achieving full compliance.
- Data Owner approval for the affected data domain.
- CISO approval for Confidential/Restricted data exceptions.

| Exception Type | Approval Required | Maximum Duration |
|----------------|-------------------|------------------|
| Single system (low sensitivity) | Security Team Lead + Data Owner | 12 months, with milestone review at 6 months |
| Single system (high sensitivity) | CISO + Data Owner | 6 months, with milestone review at 3 months |
| Environment-wide exception | CISO + Data Owner | 6 months, with monthly progress reporting |
| Production masking waiver | CISO + Executive Management | Annual re-approval, with quarterly milestone reviews |
| Prohibited technique override | NOT PERMITTED | N/A |

Active exceptions shall be reviewed quarterly, revoked if business justification changes, and automatically expired at end of approved duration (no implicit renewal).

---

## Optional: Payment Card Data Controls (PCI DSS)

*Applicable only if payment card data is processed and PCI scope exists.*

If PCI scope exists, the following additional data masking requirements apply:

- Primary Account Numbers (PANs) shall be rendered unreadable anywhere they are stored, per PCI DSS Req. 3.4 (tokenisation, truncation, hashing, or strong encryption).
- When PANs are displayed, masking shall show at most the first six and last four digits, per PCI DSS Req. 3.5.1.
- Full PANs shall not be present in non-production environments unless the non-production environment meets all applicable PCI DSS controls. SDM or tokenisation shall be applied before data leaves the cardholder data environment.
- Non-production use of payment card data shall be governed by a documented data usage policy per PCI DSS Req. 12.3.

---

## Training and Awareness

**All personnel** shall receive annual security awareness training that includes:

- The obligation to use masked data in non-production environments.
- How to recognise and report unmasked sensitive data.
- The prohibition on attempting to re-identify masked, pseudonymised, or anonymised data.

**Technical staff** (Security Team, IT Operations, developers) shall receive training on:

- Approved masking techniques and tool operation.
- Testing and validation procedures.
- Incident response for masking failures.

**Data Owners** shall be briefed on:

- Data classification and masking decision responsibilities.
- Exception request evaluation and approval criteria.
- Validation of masking effectiveness for their data domains.

---

## Definitions

| Term | Definition |
|------|------------|
| **Anonymisation** | Irreversible removal of all identifying information such that re-identification is not possible. Anonymised data is no longer personal data under GDPR/nFADP. |
| **Data Masking** | Process of obscuring original data with modified content to protect sensitive information while maintaining data format and usability. |
| **Dynamic Data Masking (DDM)** | Real-time masking applied at the point of data access based on user role or context. Original data remains unchanged in storage. |
| **Pseudonymisation** | Replacing direct identifiers with pseudonyms such that data cannot identify individuals without additional information (key) held separately. Pseudonymised data remains personal data. |
| **Re-identification** | Process of determining the original identity of a data subject from masked, pseudonymised, or anonymised data. |
| **Referential Integrity** | Maintaining valid relationships between related data across tables or datasets after masking. |
| **Static Data Masking (SDM)** | Permanent replacement of sensitive data with masked values in non-production databases. Original data is irreversibly replaced. |
| **Tokenisation** | Replacing sensitive data with non-sensitive tokens; original data stored in secure token vault enabling controlled reversibility. |

---

## Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **Executive Management** | Approve data masking policy; ensure adequate resources; accept residual risk where masking is not feasible |
| **CISO** | Accountable for masking policy and programme effectiveness; approve high-risk exceptions and new techniques; annual policy review |
| **DPO** | Advise on GDPR/nFADP compliance for masking implementations; review pseudonymisation and anonymisation techniques for regulatory adequacy |
| **Data Owners** | Classify data; determine masking requirements; approve techniques and exceptions for their data domains; validate masking effectiveness |
| **Security Team** | Implement masking policy; evaluate and select tools; configure and maintain solutions; conduct effectiveness testing |
| **IT Operations** | Deploy and maintain masking infrastructure; execute SDM batch jobs and DDM configuration; monitor masking process performance |
| **Development Teams** | Use masked data in non-production; implement DDM in applications where required; report masking issues; prohibited from bypassing controls |
| **All Personnel** | Comply with masking policy; report suspected unmasked sensitive data in non-production; prohibited from attempting re-identification |

---

## Evidence

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | Sensitive data inventory (systems, data elements, classification, masking status) | Data Owners / Security Team | Annual review, continuous update | 3 years |
| 2 | Masking technique inventory (approved techniques, tools, configurations) | Security Team | Annual review | 3 years |
| 3 | Environment coverage assessment (which environments are masked, gaps, exceptions) | Security Team | Annual, quarterly for high-risk | 3 years |
| 4 | Masking effectiveness test results (sample inspections, pattern scans) | Security Team | Before deployment; after changes | 3 years |
| 5 | Exception register (active exceptions, approvals, compensating controls, expiry dates) | CISO / Security Team | Quarterly review | 3 years |
| 6 | Masking process logs and configuration change records | IT Operations | Continuous | Per log retention table |
| 7 | Incident records for masking failures | Security Team | Per incident | 3 years |
| 8 | **Third-party data sharing agreements** (masking requirements, re-identification prohibition, audit rights) | Legal / Security Team | Per sharing arrangement; annual review | Active + 3 years |
| 9 | **Re-identification risk assessment results** (k-anonymity measurements, l-diversity, data utility assessments) | Security Team / Data Owners | Annually; after data structure changes | 3 years |
| 10 | **Masking configuration change records** (change requests, approvals, before/after states, test results) (SOC 2: CC8.1) | Security Team / IT Operations | Per change | 3 years |
| 11 | **DDM performance monitoring records** (baseline measurements, quarterly performance reports, threshold alerts) | IT Operations | Quarterly | 12 months |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, automated sensitive data scanning of non-production environments, masking effectiveness testing, exception register reviews, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team. Prohibited techniques cannot be excepted under any circumstances.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Deliberate attempts to bypass masking controls or re-identify masked data are treated as serious security violations.

## Third-Party Data Sharing Requirements

Where the organisation shares masked, pseudonymised, or anonymised data with third parties (vendors, partners, researchers, customers):

- **Contractual requirements**: Data sharing agreements shall specify:
  - The masking technique applied and the classification of the original data.
  - Prohibition on attempting to re-identify masked, pseudonymised, or anonymised data.
  - Return or destruction obligations upon termination of the sharing arrangement.
  - Right-to-audit provisions to verify the third party's data handling practices.
  - Breach notification obligations if the third party discovers data has been re-identified or exposed.
- **Risk assessment**: A data sharing risk assessment shall be performed before initial sharing, evaluating re-identification risk, the third party's data handling maturity, and regulatory implications.
- **Ongoing monitoring**: Data sharing arrangements shall be reviewed annually and upon material changes to the third party's environment or the shared data scope.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to data protection regulations, emerging re-identification techniques, new masking technologies, audit findings, and lessons learned from masking incidents.

---

# Areas of the ISO 27001 Standard Addressed

Data Masking Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.12 Classification of information |
| Clause 6.1 Actions to address risks | 5.15 Access control |
| Clause 6.2 Information security objectives | 5.34 Privacy and protection of PII |
| Clause 7.3 Awareness | 8.3 Information access restriction |
| | 8.10 Information deletion |
| | **8.11 Data masking** |
| | 8.24 Use of cryptography |

**Regulatory and Legal Framework**:

| Framework | Relevance | Applicability |
|-----------|-----------|---------------|
| Swiss nFADP (revDSG) | Art. 7 — Data protection by design and by default; Art. 8 — Data security (technical and organisational measures) | Mandatory |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security | Mandatory |
| EU GDPR (where applicable) | Art. 25 — Data protection by design and default; Art. 32 — Security of processing (pseudonymisation); Art. 89 — Safeguards for research/statistics | Where EU/EEA personal data is processed |
| ISO/IEC 27001:2022 | Annex A Control 8.11 — Data masking | Certification scope |
| ISO/IEC 27002:2022 | Section 8.11 — Implementation guidance for data masking controls | Guidance |
| PCI DSS v4.0 | Req. 3.4–3.5 — PAN masking and rendering unreadable; Req. 12.3 — Non-production data policies | If payment card data is processed |
| HIPAA Privacy Rule | §164.514 — De-identification standards (Expert Determination / Safe Harbor) | If US healthcare data (ePHI) is processed |
| FINMA | Client data protection; outsourcing risk management (Circular 2018/3) | If Swiss regulated financial institution |

---

<!-- QA_VERIFIED: 2026-02-07 -->

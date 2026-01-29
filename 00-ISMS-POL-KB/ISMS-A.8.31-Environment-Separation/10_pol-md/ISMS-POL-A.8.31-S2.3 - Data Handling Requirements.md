# ISMS-POL-A.8.31-S2.3
## Environment Separation - Data Handling Requirements

**Document ID**: ISMS-POL-A.8.31-S2.3  
**Title**: Data Handling Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / Data Protection Officer | Initial data handling requirements |

**Review Cycle**: Annual (or upon data protection regulation changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- DPO Review: Data Protection Officer
- Legal Review: Legal/Compliance Officer

**Distribution**: Security team, developers, QA team, operations, DPO  
**Related Documents**: 
- ISMS-POL-A.8.31-S1 (Executive Summary)
- ISMS-POL-00 (Regulatory Framework - GDPR, FADP)
- ISMS-POL-Data-Protection (if exists)
- ISMS-POL-A.8.31-Annex-B (Data Anonymization Techniques)

---

## 2.3.1 Purpose and Scope

This section establishes **mandatory data handling requirements** to prevent production data exposure in non-production environments.

**Core Principle**: **PRODUCTION DATA SHALL NEVER BE USED IN DEVELOPMENT OR TESTING** (unless properly anonymized/masked per this policy).

**Why This Matters**:
- Development/test environments have weaker security controls than production
- Developers/testers have broader access than production operations
- Production data often contains personal information subject to GDPR/FADP
- Data breaches in dev/test environments violate data protection regulations
- Regulatory fines for misuse of personal data in testing

**In Scope**: All data types in all environments  
**Primary Stakeholder**: Development, QA, Operations, DPO  
**Implementation Evidence**: ISMS-IMP-A.8.31-S1 (Data Separation Assessment)

---

## 2.3.2 Production Data in Development/Testing - PROHIBITION

### 2.3.2.1 Absolute Prohibition

[Organization] **SHALL PROHIBIT** the use of production data in development and testing environments:

**Prohibited Activities**:
- Copying production databases to development/test environments
- Restoring production database backups to dev/test
- Exporting production data for testing purposes
- Using production API keys in development code
- Connecting dev/test applications to production databases
- Screen scraping or downloading production data for testing
- Using production user accounts for testing

**Enforcement Mechanisms**:
- Network isolation prevents dev/test → production data access
- Database credentials separate per environment (dev cannot connect to prod DB)
- Code review checks for production credentials or data exports
- Automated scanning for production data patterns in dev/test
- Security awareness training on data handling requirements

**Audit Verification Criteria** (CRITICAL):
- ✅ **Zero production data** found in dev/test environments (scanned monthly)
- ✅ Network isolation prevents prod data access from dev/test
- ✅ No production database credentials in dev/test code
- ✅ Developers trained on prohibition (100% completion rate)

### 2.3.2.2 Exception Process (Anonymized Data Only)

[Organization] **MAY** permit use of production-derived data in dev/test IF AND ONLY IF properly anonymized:

**Exception Criteria**:
- Production data is required for realistic testing (synthetic data insufficient)
- Data is properly anonymized per Section 2.3.4 (DPO approval required)
- Anonymization process documented and verified
- Re-identification risk assessed and accepted by DPO
- Exception approved by CISO and DPO in writing

**Exception Documentation**:
- Business justification for production data use
- Anonymization technique applied (masking, tokenization, synthetic generation)
- Re-identification risk assessment
- Data retention and deletion schedule
- Approval signatures (CISO, DPO)

**Audit Verification Criteria**:
- ✅ All production data usage exceptions documented and approved
- ✅ Anonymization effectiveness verified by DPO
- ✅ Exception data deleted per schedule
- ✅ Exceptions reviewed annually

---

## 2.3.3 Test Data Management

### 2.3.3.1 Synthetic Test Data

[Organization] **SHALL** use synthetic (artificially generated) test data as the primary testing approach:

**Synthetic Data Characteristics**:
- Realistic but fake (mimics production data structure without real values)
- No relationship to actual customers or users
- Generated programmatically or manually created
- Covers edge cases and boundary conditions
- Sufficient volume for performance testing

**Synthetic Data Generation Methods**:
- **Manual creation**: Developers create test records (John Doe, jane.smith@example.com)
- **Data generation tools**: Faker, Mockaroo, GenerateData.com
- **Programmatic generation**: Scripts generate random but valid data
- **AI-generated**: ML models generate realistic synthetic data

**Synthetic Data Examples**:
- Customer names: "Alice Anderson", "Bob Brown", "Charlie Chen"
- Email addresses: test1@example.com, qa-user@example.org
- Phone numbers: +41 00 000 0000 (invalid but correctly formatted)
- Addresses: "123 Test Street, 9999 Example City"
- Credit cards: Use test card numbers (4111111111111111 for Visa test)

**Audit Verification Criteria**:
- ✅ Synthetic data generation process documented
- ✅ Test data generation tools identified and approved
- ✅ Developers trained on synthetic data creation
- ✅ Synthetic data covers functional and edge case testing requirements

### 2.3.3.2 Test Data Lifecycle Management

[Organization] **SHALL** manage test data lifecycle to prevent accumulation and misuse:

**Test Data Creation**:
- Test data created as needed for testing (not copied from production)
- Test data ownership assigned (developer/QA responsible for their test data)
- Test data documented (what is it, why was it created, when can it be deleted)

**Test Data Retention**:
- Test data retained only while needed for active testing
- Test data deleted at project completion (unless documented reason for retention)
- Quarterly test data cleanup (delete unused test data)

**Test Data Deletion**:
- Automated test data cleanup (delete data >90 days old if not used)
- Manual test data deletion before environment refresh
- Test data deletion verified (not just marked deleted, actually removed)

**Audit Verification Criteria**:
- ✅ Test data retention policy documented
- ✅ Quarterly test data cleanup executed
- ✅ Test data volume monitored (not growing indefinitely)
- ✅ Deleted test data not recoverable

---

## 2.3.4 Data Anonymization and Masking

### 2.3.4.1 When Anonymization is Required

[Organization] **SHALL** anonymize production data when:

**Mandatory Anonymization Scenarios**:
- Production data needed for testing (realistic data required, synthetic insufficient)
- Performance testing requires production-scale data volumes
- Data migration testing (migrating production to new system)
- Troubleshooting production issues in staging environment
- Third-party vendor testing (vendor requires realistic data)

**Anonymization vs. Pseudonymization**:
- **Anonymization**: Irreversible removal of personal data (cannot re-identify individuals)
- **Pseudonymization**: Reversible substitution (can re-identify with additional information)
- **GDPR/FADP Requirement**: Use anonymization (irreversible) for dev/test, not pseudonymization

**Audit Verification Criteria**:
- ✅ Anonymization required scenarios documented
- ✅ DPO approves anonymization approaches
- ✅ Anonymization vs. pseudonymization distinction clear

### 2.3.4.2 Data Anonymization Techniques

[Organization] **SHALL** apply appropriate anonymization techniques based on data sensitivity:

**Data Masking** (replace sensitive data with realistic but fake values):
- **Full masking**: Replace entire value (e.g., "John Smith" → "XXXXX XXXXX")
- **Partial masking**: Mask part of value (e.g., "john.smith@example.com" → "j***.s*****@example.com")
- **Format-preserving**: Maintain data format (e.g., credit card 1234-5678-9012-3456 → 8765-4321-0987-6543)

**Tokenization** (replace real values with random tokens):
- Consistent tokenization (same real value always maps to same token)
- One-way tokenization (cannot reverse token to original value)
- Example: Customer ID "CUST-12345" → Token "TKN-A7B9C2"

**Generalization** (reduce precision to prevent identification):
- Age: "42 years old" → "40-49 years"
- Location: "Sursee, Lucerne" → "Central Switzerland"
- Date: "2024-03-15" → "March 2024"

**Synthetic Data Replacement** (replace with generated data maintaining relationships):
- Maintain referential integrity (customer ID same across tables)
- Preserve statistical distribution (anonymized data has same patterns as production)
- Example: Replace all customer names with generated names, but keep purchase patterns

**Data Subsetting** (use small sample, not full dataset):
- Extract 1-5% of production records for testing
- Anonymize the subset
- Reduces risk (smaller dataset, less comprehensive)

**Audit Verification Criteria**:
- ✅ Anonymization technique selected per data type
- ✅ Anonymization effectiveness tested (cannot re-identify)
- ✅ DPO approves anonymization approach
- ✅ Anonymization documented in data processing records

### 2.3.4.3 Anonymization Effectiveness Verification

[Organization] **SHALL** verify that anonymized data cannot be re-identified:

**Re-Identification Risk Assessment**:
- Can individuals be identified from anonymized data alone? (should be NO)
- Can individuals be identified by combining anonymized data with other available data? (assess risk)
- Could specialized knowledge re-identify individuals? (assess risk)
- DPO assesses re-identification risk and approves or rejects anonymization approach

**Anonymization Testing**:
- Sample anonymized records reviewed by DPO
- Attempt to re-identify individuals using public information
- Statistical analysis (k-anonymity, l-diversity) if appropriate
- Anonymization effectiveness documented

**Continuous Verification**:
- Anonymization process audited annually
- Re-identification risk reassessed when new data sources available
- Anonymization techniques updated as needed

**Audit Verification Criteria**:
- ✅ Re-identification risk assessment documented
- ✅ DPO approves anonymization effectiveness
- ✅ Anonymization tested (re-identification attempts)
- ✅ Annual re-assessment conducted

---

## 2.3.5 Data Handling Per Environment

### 2.3.5.1 Development Environment Data

[Organization] **SHALL** use ONLY synthetic or heavily anonymized data in development:

**Permitted Development Data**:
- Synthetic data (programmatically generated or manually created)
- Heavily anonymized production data (DPO approved, re-identification impossible)
- Publicly available data (open datasets, public APIs)
- Developer-created test data

**PROHIBITED Development Data**:
- Production customer data (personal information)
- Production business data (financial records, contracts)
- Production credentials (API keys, passwords, certificates)
- Production configuration (unless sanitized)

**Development Data Handling**:
- Developers create their own test data
- Shared test datasets maintained in dev data repository
- Development data reset periodically (monthly or quarterly)
- Development data never promoted to staging or production

**Audit Verification Criteria**:
- ✅ Development databases contain no production personal data
- ✅ Development data generation documented
- ✅ Development data reset schedule followed
- ✅ Code commits do not include production data

### 2.3.5.2 Testing Environment Data

[Organization] **SHALL** use synthetic or anonymized data in testing:

**Permitted Testing Data**:
- Synthetic data optimized for test scenarios
- Anonymized production data (DPO approved) for realistic testing
- Test data covering edge cases and boundary conditions
- Performance test data (large volumes, anonymized)

**PROHIBITED Testing Data**:
- Production personal data (unanonymized)
- Production credentials
- Live payment card details (use test cards: 4111111111111111)

**Testing Data Handling**:
- QA team maintains curated test datasets
- Test data version controlled (test data changes tracked)
- UAT data separate from QA data (business users see sanitized data only)
- Testing data refreshed before major test cycles

**Audit Verification Criteria**:
- ✅ Testing databases contain no production personal data
- ✅ Test datasets documented and version controlled
- ✅ UAT data appropriate for business user access
- ✅ Performance test data anonymized

### 2.3.5.3 Staging Environment Data

[Organization] **SHOULD** use heavily anonymized or synthetic data in staging:

**Permitted Staging Data**:
- Synthetic data matching production scale (for performance validation)
- Heavily anonymized production data (for production-equivalent testing)
- Production configuration data (sanitized - no secrets)

**Staging Data Considerations**:
- Staging mirrors production configuration (but uses anonymized data)
- Performance testing requires production-scale volumes
- Security testing uses anonymized data (to avoid exposing real data in test reports)
- Data refresh aligns with production deployment cadence

**Audit Verification Criteria**:
- ✅ Staging data anonymized or synthetic
- ✅ Staging data volume mirrors production (for realistic performance testing)
- ✅ Staging configuration sanitized (no production secrets)
- ✅ DPO approves staging data approach

### 2.3.5.4 Production Environment Data

[Organization] **SHALL** protect production data with highest security controls:

**Production Data Characteristics**:
- Real customer data (personal information)
- Real business data (financial records, contracts)
- Live operational data
- Subject to GDPR, FADP, and other data protection regulations

**Production Data Protection**:
- Encryption at rest (databases, file storage, backups)
- Encryption in transit (TLS for all connections)
- Access controls (operations team only, see S2.2)
- Audit logging (all access to sensitive data logged)
- Data minimization (collect only necessary data)
- Retention limits (delete data when no longer needed)

**Production Data CANNOT be Exported** to non-production without:
- CISO and DPO approval
- Anonymization per Section 2.3.4
- Business justification
- Legal review (if contractual or regulatory implications)

**Audit Verification Criteria**:
- ✅ Production data encrypted (at rest and in transit)
- ✅ Production data access logged and monitored
- ✅ Production data exports approved and anonymized
- ✅ Data retention policies enforced

---

## 2.3.6 Sensitive Data Identification and Classification

### 2.3.6.1 Data Classification

[Organization] **SHALL** classify data to apply appropriate handling requirements:

**Data Classification Levels**:

**Public Data**:
- Publicly available information (website content, press releases)
- No special handling required
- Can be used in any environment

**Internal Data**:
- Business information not for public disclosure
- Standard security controls
- Can be used in dev/test if no personal information

**Confidential Data**:
- Sensitive business information (financial data, contracts, intellectual property)
- Enhanced security controls
- CANNOT be used in dev/test unless anonymized

**Personal Data (GDPR/FADP)**:
- Information relating to identified or identifiable individuals
- Data protection regulations apply
- **CANNOT be used in dev/test** unless anonymized (DPO approved)

**Special Category Personal Data (GDPR Art. 9)**:
- Health data, biometric data, racial/ethnic origin, political opinions, etc.
- Highest protection level
- **PROHIBITED in dev/test** (even anonymization may be insufficient)

**Audit Verification Criteria**:
- ✅ Data classification policy documented
- ✅ Systems and datasets classified
- ✅ Personal data identified and flagged
- ✅ Special category data handling procedures defined

### 2.3.6.2 Personal Data Handling

[Organization] **SHALL** handle personal data per GDPR/FADP requirements:

**Personal Data in Production ONLY**:
- Customer names, addresses, contact information
- Employee personal information
- User credentials and authentication data
- IP addresses, device identifiers
- Location data, browsing history
- Any information that identifies or could identify a person

**Development/Testing Without Personal Data**:
- Use synthetic names: "Alice Anderson", "Bob Brown"
- Use example.com email domains: test@example.com
- Use invalid but formatted phone numbers: +41 00 000 0000
- Use test addresses: "123 Test St, 9999 Example City"
- Use testing IP ranges: 192.0.2.0/24 (RFC 5737 TEST-NET)

**Audit Verification Criteria**:
- ✅ Personal data inventory maintained
- ✅ Personal data NOT in dev/test (verified monthly)
- ✅ Synthetic alternatives documented
- ✅ GDPR/FADP compliance verified

---

## 2.3.7 Third-Party Data Sharing

### 2.3.7.1 Vendor Testing Data

[Organization] **SHALL** provide vendors with synthetic or anonymized data only:

**Vendor Data Requirements**:
- Vendors request sample data for integration testing
- [Organization] provides synthetic data (never production data)
- If production-derived data required, anonymize per Section 2.3.4
- Data sharing agreement includes data protection clauses

**Vendor Data Restrictions**:
- Vendor cannot request production personal data
- Vendor must delete data after testing complete
- Vendor data handling audited
- Data breach notification obligations in contract

**Audit Verification Criteria**:
- ✅ Vendor data requests documented
- ✅ Vendor receives synthetic/anonymized data only
- ✅ Data sharing agreements include protection clauses
- ✅ Vendor data deletion verified

---

## 2.3.8 Data Leakage Detection and Prevention

### 2.3.8.1 Automated Data Leakage Detection

[Organization] **SHOULD** implement automated scanning for production data in dev/test:

**Detection Techniques**:
- **Pattern matching**: Scan for production data patterns (names, addresses, email domains)
- **Database comparison**: Compare dev/test databases to production (detect copies)
- **Credential scanning**: Scan code repositories for production credentials
- **DLP (Data Loss Prevention)**: Monitor data movement between environments

**Scanning Frequency**:
- Code repositories: On every commit (pre-commit hooks)
- Databases: Monthly full scan
- File systems: Weekly scan
- Network traffic: Continuous monitoring

**Audit Verification Criteria**:
- ✅ Data leakage detection tools deployed
- ✅ Scans executed per schedule
- ✅ Detected leakage incidents investigated
- ✅ Leakage remediated within defined SLA

### 2.3.8.2 Incident Response for Data Leakage

[Organization] **SHALL** respond promptly to detected data leakage incidents:

**Data Leakage Incident Process**:
1. **Detection**: Automated scan or manual discovery of production data in dev/test
2. **Triage**: Security team assesses severity (personal data? how much? how long exposed?)
3. **Containment**: Immediately delete production data from dev/test
4. **Investigation**: Determine how data entered dev/test (accidental copy? deliberate?)
5. **Notification**: DPO notified, breach assessment (reportable to authorities?)
6. **Remediation**: Implement controls to prevent recurrence
7. **Documentation**: Incident documented for audit and learning

**Data Breach Notification** (if personal data exposed):
- DPO assesses if breach reportable (GDPR: 72 hours to authority)
- Legal team involved
- Affected individuals notified if high risk
- Regulatory authority notified per GDPR/FADP

**Audit Verification Criteria**:
- ✅ Data leakage incidents logged and investigated (100%)
- ✅ Incident response time <24 hours
- ✅ DPO notified of all personal data leakage incidents
- ✅ Breach notifications submitted per regulations

---

## 2.3.9 Data Retention and Deletion

### 2.3.9.1 Test Data Retention Limits

[Organization] **SHALL** delete test data when no longer needed:

**Test Data Retention**:
- **Active project data**: Retained while project active
- **Completed project data**: Deleted 30 days after project closure
- **Shared test datasets**: Reviewed quarterly, delete if unused
- **Performance test data**: Deleted after test completion

**Automated Deletion**:
- Test databases refreshed monthly (deletes all data, recreates from templates)
- Temporary test data auto-deleted after 90 days
- Anonymized production data deleted after 180 days (or when no longer needed)

**Audit Verification Criteria**:
- ✅ Test data retention policy documented
- ✅ Automated deletion executed per schedule
- ✅ Manual deletion for completed projects verified
- ✅ Test data volume trending (not growing indefinitely)

---

## 2.3.10 Measurable Compliance Criteria

For audit and compliance verification, [Organization] must demonstrate:

**Data Handling Compliance Metrics** (CRITICAL):
- **0 production personal data** found in dev/test environments (scanned monthly)
- **100%** of production data usage exceptions approved by CISO + DPO
- **100%** of anonymization approaches approved by DPO
- **0** data leakage incidents unresolved >24 hours
- **100%** of developers trained on data handling requirements (annual)
- **100%** of test data deletion executed per retention schedule
- **0** production database connections from dev/test environments
- **100%** of vendor data sharing includes data protection agreements

**Verification Methods**:
- Monthly automated scans (production data detection in dev/test)
- Quarterly data handling audits (DPO led)
- Semi-annual GDPR/FADP compliance assessment
- Annual penetration test (attempt data exfiltration from prod to dev)
- Continuous monitoring (database connection attempts, data transfers)

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | [Name] | ________________ | [Date] |
| Data Protection Officer | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |
| Development Manager | [Name] | ________________ | [Date] |
| Legal/Compliance Officer | [Name] | ________________ | [Date] |

---

*End of Document ISMS-POL-A.8.31-S2.3*

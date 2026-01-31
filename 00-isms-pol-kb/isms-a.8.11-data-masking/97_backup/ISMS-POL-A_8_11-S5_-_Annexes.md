# ISMS-POL-A.8.11-S5 – Annexes
## ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document ID**: ISMS-POL-A.8.11-S5  
**Title**: Data Masking - Annexes (Templates, Forms, Quick Reference)  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Information Security Officer (ISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Technical Documentation Team / CISO Office | Initial section document |

**Review Cycle**: As needed (when referenced standards, tools, or templates change), minimum annual review  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical: Information Security Manager
- Documentation: Technical Documentation Manager

**Distribution**: Technical teams, auditors, implementation teams  
**Parent Document**: ISMS-POL-A.8.11 - Data Masking Policy (Master)  
**Related Standards**: ISO/IEC 27001:2022, ISO/IEC 27002:2022, relevant regulatory frameworks

---

## 1. Purpose

This section contains **practical templates, forms, and quick reference materials** 
to support implementation of the data masking policy. These are the "grab and use" 
documents that make policy implementation easier.

**What this section contains:**

- **S5.A:** Masking Requirements Template
- **S5.B:** Exception Request Form
- **S5.C:** Testing Validation Checklist
- **S5.D:** Incident Response Playbook
- **S5.E:** Quick Reference Guide (one-pager)
- **S5.F:** Data Flow Mapping Template
- **S5.G:** Re-identification Risk Assessment Template

**Usage:** These templates are starting points. Customize to your organization's needs.

---

## 2. Annex Structure

Each annex is **standalone** and can be used independently:
```
S5.A - Masking Requirements Template
S5.B - Exception Request Form
S5.C - Testing Validation Checklist
S5.D - Incident Response Playbook
S5.E - Quick Reference Guide
S5.F - Data Flow Mapping Template
S5.G - Re-identification Risk Assessment Template
```

---

# ANNEX S5.A – Masking Requirements Template

## Data Masking Requirements Specification

**Document ID:** MASK-REQ-[System/Database Name]-[DD.MM.YYYY]  
**System/Database:** [Name]  
**Data Owner:** [Name, Role]  
**System Owner:** [Name, Role]  
**Prepared By:** [Name, Role]  
**Date:** [DD.MM.YYYY]  
**Status:** [Draft / Approved / Implemented]

---

### 1. System Overview

**System Name:** [e.g., Customer Relationship Management (CRM)]  
**System Type:** [Production / Non-Production / Analytics / Backup]  
**Data Classification:** [Public / Internal / Confidential / Restricted]  
**Business Purpose:** [Describe why this system exists]  
**Regulatory Requirements:** [GDPR / HIPAA / PCI-DSS / None]

---

### 2. Sensitive Data Inventory

**Instructions:** List all tables and fields containing sensitive data.

| Table Name | Field Name | Data Type | Sensitivity | Example Value | PII? |
|------------|-----------|-----------|-------------|---------------|------|
| customers | customer_id | INT | Low | 12345 | No |
| customers | first_name | VARCHAR | High | John | Yes |
| customers | last_name | VARCHAR | High | Smith | Yes |
| customers | email | VARCHAR | High | john.smith@example.com | Yes |
| customers | phone | VARCHAR | High | +41791234567 | Yes |
| customers | ssn | VARCHAR | Critical | 123-45-6789 | Yes |
| customers | address | VARCHAR | High | 123 Main St, Zurich | Yes |
| customers | date_of_birth | DATE | High | 1985-03-15 | Yes |
| customers | credit_card_number | VARCHAR | Critical | 4111-1111-1111-1111 | Yes |
| transactions | transaction_id | INT | Low | 98765 | No |
| transactions | transaction_amount | DECIMAL | Medium | 150.00 | No |
| transactions | transaction_date | DATE | Low | 2025-01-02 | No |

**Total Tables:** [Count]  
**Total Sensitive Fields:** [Count]  
**Total PII Fields:** [Count]

---

### 3. Masking Requirements per Field

**Instructions:** Define specific masking technique for each sensitive field.

| Table | Field | Masking Technique | Format Preserved? | Referential Integrity? | Notes |
|-------|-------|-------------------|-------------------|------------------------|-------|
| customers | first_name | Substitution (fake names) | Yes | No | Use realistic names |
| customers | last_name | Substitution (fake names) | Yes | No | Use realistic names |
| customers | email | Substitution (fake emails) | Yes | No | Must be valid email format |
| customers | phone | Substitution (fake phones) | Yes | No | Must match country format |
| customers | ssn | Redaction | No | No | Replace with "***-**-****" |
| customers | address | Substitution (fake addresses) | Yes | No | Use realistic addresses |
| customers | date_of_birth | Shuffling | Yes | No | Preserve age distribution |
| customers | credit_card_number | Tokenization | Yes (format-preserving) | Yes | Use tokenization vault |
| customers | customer_id | Deterministic Substitution | Yes | Yes | Maintain relationships |

---

### 4. Environment-Specific Requirements

**Target Environment:** [Development / Testing / UAT / Training / Analytics]  
**Masking Frequency:** [Daily / Weekly / Per-refresh / On-demand]  
**Data Refresh Source:** [Production DB / Production Backup / Other]

#### 4.1 Data Flow
```
[Production DB] → [Backup/Snapshot] → [MASKING CHECKPOINT] → [Target Environment]
```

**Masking Checkpoint Details:**
- **Tool/Method:** [Tool name or script]
- **Execution Schedule:** [Cron schedule or manual]
- **Responsible Role:** [DBA / DevOps / System Owner]
- **Validation:** [Automated script / Manual review]

#### 4.2 Performance Requirements

| Metric | Requirement |
|--------|-------------|
| **Masking Duration** | < 2 hours (for full database refresh) |
| **Data Availability** | Target environment ready within 4 hours of request |
| **Resource Usage** | < 50% CPU, < 60% Memory during masking |

---

### 5. Validation Requirements

#### 5.1 Pre-Deployment Validation

- [ ] All sensitive fields masked (100% coverage)
- [ ] Masking techniques applied correctly
- [ ] Data format preserved where required
- [ ] Referential integrity maintained where required
- [ ] No production data matches in masked dataset

#### 5.2 Post-Deployment Validation

- [ ] Masked data deployed to target environment
- [ ] Applications function correctly with masked data
- [ ] Users cannot see sensitive data
- [ ] Re-identification testing performed (PASS)

---

### 6. Exception and Special Cases

**Exceptions (if any):**

| Field | Reason for Exception | Compensating Controls | Approval |
|-------|---------------------|----------------------|----------|
| [Field name] | [Why masking not applied] | [Encryption, Access control, etc.] | [CISO, Date] |

**Special Handling:**

| Scenario | Handling Procedure |
|----------|-------------------|
| Null values | [Leave as NULL / Mask anyway] |
| Empty strings | [Leave empty / Replace with masked value] |
| Referential integrity violations | [Report as error / Auto-correct] |

---

### 7. Implementation Plan

| Task | Responsible | Target Date | Status |
|------|-------------|-------------|--------|
| Define masking requirements | Data Owner | [Date] | [Complete / In Progress] |
| Select masking tool/technique | Security Architect | [Date] | [Complete / In Progress] |
| Develop masking script | DBA | [Date] | [Complete / In Progress] |
| Test masking effectiveness | System Owner | [Date] | [Complete / In Progress] |
| Deploy to target environment | DevOps | [Date] | [Complete / In Progress] |
| Validate post-deployment | QA Team | [Date] | [Complete / In Progress] |

---

### 8. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Data Owner** | [Name] | ____________ | ______ |
| **System Owner** | [Name] | ____________ | ______ |
| **ISO** | [Name] | ____________ | ______ |
| **CISO** (if exceptions) | [Name] | ____________ | ______ |

---

# ANNEX S5.B – Exception Request Form

## Data Masking Exception Request Form

**Form ID:** MASK-EXC-[YYYY]-[Sequential Number]  
**Submission Date:** [DD.MM.YYYY]  
**Requestor:** [Name, Role, Department]

---

### 1. Exception Details

**System/Database:** [Name]  
**Environment:** [Production / Non-Production / Analytics / Backup / Other]  
**Table(s) Affected:** [List tables]  
**Field(s) Affected:** [List fields]  
**Data Classification:** [Internal / Confidential / Restricted]

---

### 2. Current Policy Requirement

**According to ISMS-POL-A.8.11, the requirement is:**

[Quote the specific policy requirement that would apply, e.g., "All non-production 
environments SHALL have sensitive data masked per S2.3"]

---

### 3. Requested Exception

**I am requesting an exception to:**

- [ ] NOT mask data in a non-production environment
- [ ] Use weaker masking technique than required
- [ ] Delay masking implementation
- [ ] Other: [Describe]

**Specific Request:**

[Describe exactly what you want to do differently from policy]

---

### 4. Business Justification

**Why is this exception necessary?**

[Explain the business need. Examples:
- Application functionality broken with masked data
- Third-party tool requires real data
- Performance testing requires production-like data
- Training scenario requires real data]

**What business impact if exception NOT granted?**

[Describe impact. Be specific. Quantify if possible.]

---

### 5. Risk Assessment

#### 5.1 Risk Identification

**What sensitive data will be exposed if exception granted?**

[List specific data types: names, emails, SSNs, credit cards, etc.]

**Who will have access to unmasked data?**

[List roles, number of people, internal/external]

**How long will exception be in effect?**

- [ ] Temporary (specify end date: __________)
- [ ] Permanent (requires quarterly re-approval)

#### 5.2 Risk Level (to be completed by ISO)

| Risk Factor | Assessment |
|-------------|------------|
| **Data Sensitivity** | [Low / Medium / High / Critical] |
| **Number of Users with Access** | [Count] |
| **External Access?** | [Yes / No] |
| **Regulatory Risk** | [GDPR / HIPAA / PCI-DSS / None] |
| **Re-identification Risk** | [Low / Medium / High] |

**Overall Risk Rating:** [Low / Medium / High / Critical]

---

### 6. Compensating Controls

**What controls will mitigate the risk?**

- [ ] Encryption at rest (specify algorithm: ________)
- [ ] Encryption in transit (TLS 1.2+)
- [ ] Access controls (MFA required)
- [ ] Audit logging (all access logged)
- [ ] User training and NDA
- [ ] Data minimization (only necessary fields)
- [ ] Time-limited access (auto-expire after: _____ days)
- [ ] Geographic restrictions (access only from: ________)
- [ ] Other: [Describe]

**Compensating Controls Effectiveness:**

[Describe how these controls reduce risk to acceptable level]

---

### 7. Alternatives Considered

**What alternatives were considered?**

| Alternative | Reason NOT Chosen |
|-------------|------------------|
| [Alternative 1] | [Why not feasible] |
| [Alternative 2] | [Why not feasible] |
| [Alternative 3] | [Why not feasible] |

---

### 8. Implementation Plan (if approved)

| Task | Responsible | Target Date |
|------|-------------|-------------|
| Implement compensating controls | [Role] | [Date] |
| Configure access controls | [Role] | [Date] |
| Enable audit logging | [Role] | [Date] |
| User training | [Role] | [Date] |
| Document exception | ISO | [Date] |

---

### 9. Review and Approval

#### 9.1 Data Owner Review

**Data Owner Assessment:**

- [ ] Approve
- [ ] Reject
- [ ] Request More Information

**Comments:** ___________________________________________

**Data Owner Signature:** ____________ **Date:** ______

---

#### 9.2 ISO Review

**ISO Risk Assessment:**

[Detailed risk assessment by ISO]

**ISO Recommendation:**

- [ ] Approve (risk acceptable with compensating controls)
- [ ] Approve with conditions: [Specify conditions]
- [ ] Reject (risk too high)
- [ ] Request More Information

**ISO Signature:** ____________ **Date:** ______

---

#### 9.3 Compliance Officer Review (if applicable)

**Regulatory Impact:**

[Assessment of regulatory compliance impact]

**Compliance Officer Recommendation:**

- [ ] Approve
- [ ] Reject
- [ ] Request More Information

**Compliance Officer Signature:** ____________ **Date:** ______

---

#### 9.4 CISO Approval

**Final Decision:**

- [ ] **APPROVED** (Exception granted)
- [ ] **REJECTED** (Exception denied)
- [ ] **CONDITIONAL APPROVAL** (Conditions: _____________)

**Approval Valid Until:** [Date] (maximum 1 year, quarterly review required)

**CISO Signature:** ____________ **Date:** ______

---

### 10. Exception Register Entry

**Exception ID:** [Auto-generated]  
**Status:** [Approved / Rejected / Pending]  
**Next Review Date:** [Date]

---

# ANNEX S5.C – Testing Validation Checklist

## Data Masking Testing & Validation Checklist

**Test ID:** MASK-TEST-[System]-[DD.MM.YYYY]  
**System/Database:** [Name]  
**Environment:** [Development / Testing / UAT / Training / Analytics]  
**Tested By:** [Name, Role]  
**Test Date:** [DD.MM.YYYY]  
**Test Type:** [ ] Pre-Deployment  [ ] Post-Deployment  [ ] Periodic Re-Test

---

### 1. Pre-Deployment Testing (Before masked data deployed)

#### 1.1 Masking Execution

- [ ] Masking script executed successfully
- [ ] No errors in masking logs
- [ ] Masking completion time: _____ minutes (Target: < 120 min)
- [ ] Resource usage acceptable (CPU: __%, Memory: __%)

**Evidence:** [Screenshot of successful execution, log file location]

---

#### 1.2 Visual Inspection

**Instructions:** Manually review sample records (minimum 20 records)

- [ ] Sensitive fields are NOT visible in plaintext
- [ ] Masked data appears realistic (if substitution used)
- [ ] No obviously identifiable data visible
- [ ] Data format preserved where required

**Sample Review:**

| Field | Original (Prod) | Masked (Non-Prod) | Format OK? | Realistic? |
|-------|----------------|-------------------|------------|------------|
| first_name | John | [Not visible] | ✓ | ✓ |
| email | john@example.com | [Not visible] | ✓ | ✓ |
| ssn | 123-45-6789 | ***-**-**** | ✓ | N/A |

**Evidence:** [Screenshots of masked data sample - REDACT production data in evidence!]

---

#### 1.3 Completeness Testing

- [ ] All sensitive fields listed in requirements are masked
- [ ] No NEW sensitive fields added since last assessment (schema drift check)
- [ ] Masking coverage: ___% (Target: 100%)

**Gap Analysis:**

| Table | Field | Expected Masking | Actual Masking | Gap? |
|-------|-------|-----------------|----------------|------|
| [Table] | [Field] | [Technique] | [Technique] | [Yes/No] |

**Evidence:** [Coverage report, schema comparison output]

---

#### 1.4 Format and Integrity Testing

- [ ] Data types preserved (VARCHAR→VARCHAR, INT→INT, etc.)
- [ ] Data formats valid (emails pass email regex, phones pass phone regex, etc.)
- [ ] NULL values handled correctly
- [ ] Referential integrity maintained (foreign keys still valid)
- [ ] No orphaned records created

**Validation Queries:**
```sql
-- Example integrity check (pseudocode)
SELECT COUNT(*) FROM customers WHERE email NOT LIKE '%@%.%';
-- Result: 0 (all emails valid format)

SELECT COUNT(*) FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.customer_id 
WHERE c.customer_id IS NULL;
-- Result: 0 (no orphaned orders)
```

**Evidence:** [SQL query results, validation script output]

---

#### 1.5 Re-identification Testing

**Instructions:** Attempt to re-identify individuals using masked data

**Test Scenarios:**

- [ ] Direct matching: Can masked data be matched to production? (Result: FAIL = Good)
- [ ] Quasi-identifier combination: Can age + ZIP + gender identify someone? (Result: FAIL = Good)
- [ ] External data correlation: Can masked data be correlated with public data? (Result: FAIL = Good)
- [ ] Statistical inference: Can original values be inferred from patterns? (Result: FAIL = Good)

**Re-identification Success Rate:** ___% (Target: 0%)

**Evidence:** [Re-identification test report]

---

#### 1.6 Production Data Leakage Check

- [ ] NO exact matches between production and masked data (for sensitive fields)
- [ ] Sample comparison: 100 random records checked, 0 matches found

**Comparison Test:**
```sql
-- Example (pseudocode)
SELECT COUNT(*) FROM production.customers p
INNER JOIN masked.customers m ON p.email = m.email;
-- Result: 0 (no email matches)
```

**Evidence:** [Comparison script output]

---

### 2. Post-Deployment Testing (After masked data deployed to target)

#### 2.1 Deployment Verification

- [ ] Masked data successfully loaded to target environment
- [ ] Record count matches expected (production count or subset)
- [ ] No data corruption during deployment
- [ ] Deployment completion time: _____ minutes

**Evidence:** [Deployment log, record count verification]

---

#### 2.2 Application Functionality Testing

- [ ] Application starts successfully with masked data
- [ ] Core functionality tested: [List key functions tested]
  - [ ] Function 1: [Description] - Result: PASS / FAIL
  - [ ] Function 2: [Description] - Result: PASS / FAIL
  - [ ] Function 3: [Description] - Result: PASS / FAIL
- [ ] No errors in application logs related to masked data
- [ ] Reports generate correctly

**Evidence:** [Test case results, application screenshots]

---

#### 2.3 User Acceptance Testing (if applicable)

- [ ] Users can complete assigned test scenarios
- [ ] Users do NOT see sensitive production data
- [ ] Users report masked data is realistic and usable
- [ ] No user complaints about data quality

**User Feedback:** [Summary of UAT feedback]

---

#### 2.4 Access Control Verification

- [ ] Only authorized users can access masked environment
- [ ] Unauthorized access attempts are logged and blocked
- [ ] MFA enforced (if required)
- [ ] Session timeouts configured

**Evidence:** [Access control test results, access log sample]

---

#### 2.5 Monitoring Verification

- [ ] Audit logging enabled for masked environment
- [ ] Logs capture data access events
- [ ] Alerts configured for suspicious activity
- [ ] Logs retained per policy (minimum: ____ days)

**Evidence:** [Sample audit log entries]

---

### 3. Performance Testing

#### 3.1 Query Performance

- [ ] Query performance acceptable (< 10% degradation vs. unmasked)
- [ ] No performance-related user complaints
- [ ] Resource usage within limits (CPU: __%, Memory: __%, Disk I/O: __%)

**Performance Metrics:**

| Query Type | Unmasked (ms) | Masked (ms) | Degradation (%) |
|-----------|---------------|-------------|-----------------|
| Simple SELECT | 50 | 52 | 4% |
| Complex JOIN | 200 | 215 | 7.5% |
| Aggregation | 150 | 160 | 6.7% |

**Evidence:** [Performance test results]

---

### 4. Documentation Review

- [ ] Masking requirements document exists and is current
- [ ] Masking procedures documented
- [ ] Evidence stored in designated location
- [ ] Test results documented (this checklist completed)

**Evidence Location:** [Path to documentation repository]

---

### 5. Periodic Re-Testing (for ongoing validation)

**Re-Test Frequency:** [ ] Monthly  [ ] Quarterly  [ ] Per Data Refresh  [ ] Annual

- [ ] Re-run visual inspection (sample check)
- [ ] Re-run completeness check (schema drift)
- [ ] Re-run re-identification testing
- [ ] Review access logs for anomalies
- [ ] Verify no new exceptions created without approval

**Last Re-Test Date:** [Date]  
**Next Re-Test Due:** [Date]

---

### 6. Test Summary

**Overall Result:**

- [ ] **PASS** – All tests passed, masking effective
- [ ] **PASS WITH MINOR ISSUES** – Minor issues documented, acceptable for deployment
- [ ] **FAIL** – Critical issues found, DO NOT DEPLOY, remediate immediately

**Issues Found:**

| Issue ID | Severity | Description | Remediation | Status |
|----------|----------|-------------|-------------|--------|
| [ID] | [Critical/High/Medium/Low] | [Description] | [Action] | [Open/Closed] |

---

### 7. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Tester** | [Name] | ____________ | ______ |
| **System Owner** | [Name] | ____________ | ______ |
| **ISO** | [Name] | ____________ | ______ |

---

# ANNEX S5.D – Incident Response Playbook

## Data Masking Failure – Incident Response Playbook

**Playbook ID:** MASK-IRP-001  
**Version:** 1.0  
**Last Updated:** 2025-01-02  
**Owner:** ISO

---

### 1. Incident Scenarios Covered

This playbook applies to:

1. **Unmasked data in non-production environment**
2. **Visible PII in masked environment** (masking failed)
3. **Re-identification successful** (masked data de-anonymized)
4. **Data leakage** (masked data shared externally but re-identified)
5. **Masking tool failure** (job failed, partial masking)

---

### 2. Incident Severity Classification

| Severity | Criteria | Response Time | Escalation |
|----------|----------|---------------|------------|
| **Critical** | Unmasked PII accessible to unauthorized users, External data breach | 1 hour | CISO + Executive Team |
| **High** | Unmasked PII in non-production but access-controlled, Re-identification possible | 4 hours | CISO |
| **Medium** | Masking ineffectiveness detected in testing (no exposure yet) | 24 hours | ISO |
| **Low** | Masking tool performance issue (no security impact) | 5 business days | System Owner |

---

### 3. Incident Response Process

#### Phase 1: DETECTION (T+0)

**Who:** Anyone (User, System Owner, DBA, Monitoring System, Security Analyst)

**Actions:**

1. **Detect anomaly:**
   - User reports seeing sensitive data in non-production
   - Monitoring alert on masking job failure
   - Security testing reveals re-identification vulnerability

2. **Initial assessment:**
   - What data is affected? (Tables, fields, records)
   - What environment? (Dev, Test, UAT, Analytics)
   - Who has access? (Internal, External, Number of users)

3. **IMMEDIATELY notify ISO:**
   - Email: [ISO email]
   - Phone: [ISO phone]
   - Slack/Teams: [Channel]

**Timeline:** Within 15 minutes of detection

---

#### Phase 2: CONTAINMENT (T+1 hour for Critical, T+4 hours for High)

**Who:** ISO (leads), System Owner, DBA

**Actions:**

1. **ISOLATE affected environment (if Critical/High):**
   - [ ] Disable user access to affected system
   - [ ] Shut down affected database/application (if necessary)
   - [ ] Block network access to environment

2. **ASSESS scope:**
   - [ ] How much data affected? (Query database, count records)
   - [ ] How many users had access? (Review access logs)
   - [ ] Was data exported/downloaded? (Check export logs, DLP alerts)
   - [ ] External parties involved? (Check data sharing logs)

3. **PRESERVE evidence:**
   - [ ] Take snapshot of affected environment (before cleanup)
   - [ ] Save logs (access logs, masking job logs, application logs)
   - [ ] Document timeline (who accessed what, when)

4. **NOTIFY CISO:**
   - [ ] Brief CISO on situation (phone call or in-person)
   - [ ] Provide initial assessment (scope, severity, impact)
   - [ ] Recommendation on next steps

**Timeline:** Complete within 1 hour (Critical) or 4 hours (High)

---

#### Phase 3: INVESTIGATION (T+4 hours for Critical, T+24 hours for High)

**Who:** ISO (leads), Security Architect, DBA, System Owner

**Actions:**

1. **ROOT CAUSE ANALYSIS:**
   - [ ] Why did masking fail? (Script error, config issue, schema change, human error)
   - [ ] When did it fail? (First occurrence timestamp)
   - [ ] Why wasn't it detected earlier? (Monitoring gap, validation gap)

2. **IMPACT ASSESSMENT:**
   - [ ] What data was exposed? (List specific fields and sample records)
   - [ ] Who accessed unmasked data? (List users, roles, timestamps)
   - [ ] Was data exfiltrated? (Export logs, DLP alerts, email attachments)
   - [ ] Re-identification risk? (Assess if exposed data can identify individuals)

3. **REGULATORY ASSESSMENT (if applicable):**
   - [ ] Compliance Officer consulted
   - [ ] GDPR breach notification required? (within 72 hours if yes)
   - [ ] HIPAA breach notification required?
   - [ ] PCI-DSS breach notification required?

**Timeline:** Complete within 24 hours

---

#### Phase 4: REMEDIATION (T+24 hours for Critical, T+48 hours for High)

**Who:** System Owner, DBA, Security Architect

**Actions:**

1. **FIX masking process:**
   - [ ] Correct masking script/configuration
   - [ ] Re-test masking effectiveness (per Annex S5.C)
   - [ ] Verify fix resolves root cause

2. **RE-DEPLOY masked data:**
   - [ ] Delete unmasked data from affected environment
   - [ ] Deploy correctly masked data
   - [ ] Validate masking (100% coverage, no leakage)

3. **RESTORE access (if environment was isolated):**
   - [ ] Enable user access
   - [ ] Notify users environment is available
   - [ ] Monitor for issues

4. **REVOKE compromised data (if exported):**
   - [ ] Contact users who downloaded unmasked data
   - [ ] Instruct them to delete local copies
   - [ ] Confirm deletion (if possible)

**Timeline:** Complete within 48 hours (or 5 business days for Medium)

---

#### Phase 5: RECOVERY (T+5 business days)

**Who:** ISO, System Owner

**Actions:**

1. **MONITOR for recurrence:**
   - [ ] Enhanced monitoring on affected system (30 days)
   - [ ] Review logs daily (first week)
   - [ ] Validate masking effectiveness weekly (first month)

2. **USER COMMUNICATION:**
   - [ ] Notify users of incident (if they were affected)
   - [ ] Explain what happened, what was done
   - [ ] Reinforce data protection awareness

3. **DOCUMENTATION:**
   - [ ] Complete incident report (see template below)
   - [ ] Update incident register
   - [ ] File evidence for audit

**Timeline:** Ongoing for 30 days

---

#### Phase 6: POST-INCIDENT REVIEW (T+30 days)

**Who:** ISO, CISO, System Owner, Security Architect, affected stakeholders

**Actions:**

1. **LESSONS LEARNED SESSION:**
   - What went well?
   - What went poorly?
   - What should change?

2. **PROCESS IMPROVEMENTS:**
   - [ ] Update masking policy (if policy gap identified)
   - [ ] Update masking procedures
   - [ ] Enhance monitoring/alerting
   - [ ] Additional training (if human error contributed)

3. **CLOSE INCIDENT:**
   - [ ] Final incident report approved by CISO
   - [ ] Incident status updated to "Closed"
   - [ ] Improvements tracked in improvement register

**Timeline:** Complete within 30 days of incident

---

### 4. Communication Templates

#### 4.1 Initial Notification (to ISO)
```
Subject: URGENT: Data Masking Failure Detected - [System Name]

ISO Team,

I am reporting a potential data masking failure:

System: [Name]
Environment: [Dev/Test/UAT/etc.]
Detected By: [Name]
Detection Time: [DD.MM.YYYY HH:MM]

Issue Description:
[Brief description of what was observed]

Affected Data:
[Tables, fields, approximate record count]

Users with Access:
[Approximate number, internal/external]

Immediate Actions Taken:
[What was done so far, if anything]

Contact: [Your name, phone]
```

---

#### 4.2 Notification to CISO
```
Subject: [CRITICAL/HIGH] Data Masking Incident - [System Name]

CISO,

A data masking incident has occurred:

Severity: [Critical / High / Medium / Low]
System: [Name]
Environment: [Dev/Test/UAT/etc.]
Detection Time: [DD.MM.YYYY HH:MM]

Summary:
[2-3 sentence summary of what happened]

Scope:
- Data Affected: [Tables, fields, record count]
- Users with Access: [Count, internal/external]
- Data Exported: [Yes/No - if yes, details]
- External Parties: [Yes/No - if yes, who]

Current Status:
[Contained / Under Investigation / Remediation in Progress]

Next Steps:
[Immediate actions planned]

Regulatory Impact:
[GDPR breach notification required: Yes/No/TBD]

Recommendation:
[Proposed response plan]

Contact: [ISO name, phone]
```

---

#### 4.3 User Notification (if required)
```
Subject: Data Security Incident Notification - [System Name]

Dear [User],

We are writing to inform you of a data security incident that may have 
affected data you accessed in [System Name - Environment].

What Happened:
On [Date], we discovered that sensitive data in [System Name] was not 
properly masked. This means you may have seen production data that should 
have been masked.

What Data Was Affected:
[List data types: customer names, email addresses, etc.]

What We Are Doing:
- We have corrected the masking process
- We have removed the unmasked data from the environment
- We are investigating the root cause

What You Should Do:
1. If you downloaded or exported data from [System], please DELETE all 
   local copies immediately.
2. Do NOT share this data with anyone.
3. Confirm deletion by replying to this email.

We apologize for this incident and are taking steps to prevent recurrence.

Contact: [ISO contact information]
```

---

### 5. Incident Report Template
```markdown
# Data Masking Incident Report

**Incident ID:** MASK-INC-[YYYY]-[Sequential]  
**Severity:** [Critical / High / Medium / Low]  
**Status:** [Open / Under Investigation / Remediated / Closed]

---

## 1. Incident Summary

**System/Database:** [Name]  
**Environment:** [Dev/Test/UAT/etc.]  
**Detection Date/Time:** [DD.MM.YYYY HH:MM]  
**Detected By:** [Name, Role]  
**Closed Date/Time:** [DD.MM.YYYY HH:MM] (if closed)

**Brief Description:**
[1-2 paragraph summary of what happened]

---

## 2. Timeline

| Time | Event |
|------|-------|
| T+0 | Incident detected by [Name] |
| T+15min | ISO notified |
| T+1h | Environment isolated, CISO notified |
| T+4h | Root cause identified |
| T+24h | Remediation completed |
| T+48h | Environment restored |

---

## 3. Root Cause Analysis

**Root Cause:**
[Detailed explanation of why masking failed]

**Contributing Factors:**
- [Factor 1]
- [Factor 2]
- [Factor 3]

---

## 4. Impact Assessment

**Data Affected:**
- Tables: [List]
- Fields: [List]
- Record Count: [Approximate]
- Sensitivity: [PII / Confidential / Restricted]

**Users Affected:**
- Internal: [Count]
- External: [Count]
- Total: [Count]

**Data Exfiltration:**
- Downloads: [Count, if known]
- External Sharing: [Yes/No]

**Regulatory Impact:**
- GDPR Breach Notification: [Required / Not Required]
- HIPAA Breach Notification: [Required / Not Required]

---

## 5. Response Actions

**Containment:**
- [List actions taken]

**Remediation:**
- [List actions taken]

**Recovery:**
- [List actions taken]

---

## 6. Lessons Learned

**What Went Well:**
- [Positive aspects]

**What Went Poorly:**
- [Problems identified]

**Improvements Required:**

| Improvement | Owner | Target Date | Status |
|-------------|-------|-------------|--------|
| [Action] | [Role] | [Date] | [Open/Closed] |

---

## 7. Approvals

**Reviewed By:**
- ISO: [Name, Date]
- CISO: [Name, Date]
- Compliance Officer: [Name, Date] (if applicable)

**Incident Closed:** [Yes / No]
```

---

# ANNEX S5.E – Quick Reference Guide

## Data Masking Quick Reference Guide (One-Pager)

**Version:** 1.0 | **Last Updated:** 2025-01-02 | **Owner:** ISO

---

### What is Data Masking?

**Data masking** = Replacing sensitive data with realistic but fake data to protect privacy 
while maintaining data utility.

---

### When to Mask? (Environment-Based)

| Environment | Masking Required? | Technique |
|-------------|-------------------|-----------|
| **Production** | Conditional (role-based) | Dynamic Data Masking (DDM) |
| **Non-Production** (Dev/Test/UAT) | **MANDATORY** ✓ | Static Data Masking (SDM) |
| **Analytics** | **MANDATORY** ✓ | Substitution, Aggregation |
| **Backups (Production)** | Conditional (Encrypt) | Encryption |
| **External Sharing** | **MANDATORY** ✓ | Redaction, Tokenization |
| **Cloud (Non-Prod)** | **MANDATORY** ✓ | SDM before upload |
| **Endpoints/Downloads** | **MANDATORY** ✓ | Redaction, Partial Masking |

---

### Approved Masking Techniques

| Technique | Reversible? | Use Case | Example |
|-----------|-------------|----------|---------|
| **Static Masking (SDM)** | ❌ No | Non-production data refresh | "John Smith" → "Jane Doe" |
| **Dynamic Masking (DDM)** | ❌ No (real-time) | Production role-based access | CSR sees "****1234" for card |
| **Redaction** | ❌ No | Reports, exports | "SSN: 123-45-6789" → "***-**-****" |
| **Tokenization** | ✅ Yes (with vault) | Payment systems | "4111-1111-1111-1111" → "8765-4321-9876-5432" |
| **Substitution** | ❌ No | Testing, analytics | Real names → Fake realistic names |
| **Shuffling** | ❌ No | Analytics preserving distribution | Salaries shuffled among employees |
| **Hashing** | ❌ No | Matching without exposure | "john@example.com" → "a3b5c7..." |
| **Encryption** | ✅ Yes (with key) | Data at rest, backups | Encrypted with AES-256 |

---

### Data Masking Workflow (Non-Production)
```
[1. Production DB] → [2. Backup/Snapshot] → [3. MASKING CHECKPOINT] → [4. Non-Production DB]
                                                      ↓
                                            [Validation: 100% coverage]
```

**Checkpoint:** ALL sensitive data MUST be masked before deployment to non-production.

---

### Testing Checklist (Quick)

Before deploying masked data:

- [ ] All sensitive fields masked? (100% coverage)
- [ ] No production data matches? (comparison test)
- [ ] Data format preserved? (email format, phone format, etc.)
- [ ] Referential integrity maintained? (foreign keys valid)
- [ ] Re-identification impossible? (re-ID test FAIL = Good)
- [ ] Applications work? (functionality test PASS)

---

### Roles & Responsibilities (Quick)

| Role | Key Responsibility |
|------|-------------------|
| **CISO** | Approve policy, accept risks, approve exceptions |
| **ISO** | Maintain policy, monitor compliance, manage exceptions |
| **Data Owner** | Classify data, define masking requirements |
| **System Owner** | Implement masking in their systems |
| **DBA** | Execute masking scripts, data refresh |
| **Security Architect** | Design masking architecture |
| **End Users** | Comply with policy, report issues |

---

### Exception Process (Quick)

**Need exception to masking requirement?**

1. Submit Exception Request Form (Annex S5.B)
2. Data Owner reviews
3. ISO conducts risk assessment
4. CISO approves (or rejects)
5. Implement compensating controls
6. Quarterly re-approval required

**Compensating Controls:**
- Encryption + Access controls + Audit logging + User training

---

### Incident Response (Quick)

**See unmasked data in non-production?**

1. **IMMEDIATELY notify ISO:** [Email/Phone]
2. **DO NOT access further** (preserve evidence)
3. ISO will:
   - Isolate environment (if critical)
   - Assess scope
   - Remediate masking
   - Conduct root cause analysis

**Response Times:**
- Critical: 1 hour
- High: 4 hours
- Medium: 24 hours

---

### Common Mistakes to AVOID ❌

- ❌ Cloning production to test WITHOUT masking
- ❌ "We'll mask it later" (mask BEFORE deployment)
- ❌ Relying on NDAs instead of technical controls
- ❌ Assuming complexity = security
- ❌ Using weak techniques (simple character replacement, truncation only)
- ❌ Not testing re-identification risk

---

### Key Performance Indicators (KPIs)

| KPI | Target |
|-----|--------|
| **Masking Coverage** (% environments masked) | 100% |
| **Masking Effectiveness** (% tests passed) | 100% |
| **Incident Rate** (failures per quarter) | 0 |
| **Compliance Rate** (% systems compliant) | ≥95% |
| **Re-identification Risk** | 0% |

---

### Contacts

| Role | Name | Email | Phone |
|------|------|-------|-------|
| **ISO** | [Name] | [Email] | [Phone] |
| **CISO** | [Name] | [Email] | [Phone] |
| **Security Architect** | [Name] | [Email] | [Phone] |

---

### Resources

- **Full Policy:** ISMS-POL-A.8.11 (all sections)
- **Masking Requirements Template:** Annex S5.A
- **Exception Request Form:** Annex S5.B
- **Testing Checklist:** Annex S5.C
- **Incident Playbook:** Annex S5.D

---

**Remember:** *Data masking is NOT optional for non-production environments. If you have questions, contact ISO BEFORE deploying unmasked data.*

---

# ANNEX S5.F – Data Flow Mapping Template

## Data Flow Mapping Template (for Masking Checkpoints)

**Document ID:** MASK-FLOW-[System]-[DD.MM.YYYY]  
**System/Application:** [Name]  
**Prepared By:** [Name, Role]  
**Date:** [DD.MM.YYYY]

---

### 1. Purpose

This template helps identify **WHERE masking checkpoints are required** by mapping 
data flows from production to non-production, analytics, external parties, etc.

---

### 2. Data Flow Diagram

**Instructions:** Document all data flows involving sensitive data.

**Example Flow:**
```
┌──────────────────┐
│  Production DB  │ (Unmasked - Real Customer Data)
└────────┬─────────┘
         │
         ├─────────────────────────────────────┐
         │                                     │
    [BACKUP]                              [EXPORT]
         │                                     │
         ▼                                     ▼
┌──────────────────┐              ┌───────────────────┐
│ Backup Storage  │              │  Data Warehouse  │
│  (Encrypted)    │              │   (Analytics)    │
└────────┬─────────┘              └────────┬──────────┘
         │                                 │
         │                        [MASKING CHECKPOINT]
         │                                 │
         │                                 ▼
         │                        ┌───────────────────┐
         │                        │   Masked Data    │
         │                        │    Repository    │
         │                        └────────┬──────────┘
         │                                 │
    [RESTORE TO                       [DEPLOY]
   ISOLATED ZONE]                          │
         │                                 │
         ▼                                 │
┌──────────────────┐                       │
│  Restore Zone   │                       │
│   (Isolated)    │                       │
└────────┬─────────┘                       │
         │                                 │
  [MANDATORY MASKING]                      │
         │                                 │
         ▼                                 │
┌──────────────────┐                       │
│  Masked Backup  │                       │
└────────┬─────────┘                       │
         │                                 │
         └─────────────┬───────────────────┘
                       │
                  [VALIDATION]
                       │
                       ▼
              ┌──────────────────┐
              │ Non-Production  │
              │   Environment   │
              └────────┬─────────┘
                       │
                  [ACCESS]
                       │
                       ▼
              ┌──────────────────┐
              │ Developers/QA   │
              │  (No Real PII)  │
              └──────────────────┘

┌─────────────────────────────────────────────────────────┐
│ TECHNICAL CONTROLS REQUIRED:                            │
├─────────────────────────────────────────────────────────┤
│ 1. Network Isolation: Restore Zone cannot reach Non-Prod│
│ 2. RBAC: Production backups require elevated privileges │
│ 3. Automated Masking: No manual bypass allowed          │
│ 4. Validation Gates: PII scan before non-prod deployment│
│ 5. Audit Logging: All restore operations logged         │
└─────────────────────────────────────────────────────────┘
```

---

### 3. Data Flow Inventory

| Flow ID | Source | Destination | Data Type | Sensitivity | Frequency | Current Masking? | Required Masking? |
|---------|--------|-------------|-----------|-------------|-----------|-----------------|------------------|
| FLOW-001 | Production DB | Development DB | Customer data | High (PII) | Weekly | ❌ No | ✅ Yes |
| FLOW-002 | Production DB | Testing DB | Customer data | High (PII) | Daily | ❌ No | ✅ Yes |
| FLOW-003 | Production DB | Analytics Platform | Transaction data | Medium | Hourly | ❌ No | ✅ Yes |
| FLOW-004 | Production DB | Backup Storage | All data | High (PII) | Daily | ⚠️ Encrypted | ⚠️ Conditional |
| FLOW-005 | Production DB | External Vendor | Anonymized reports | Low | Monthly | ✅ Yes | ✅ Yes |
| FLOW-006 | Production DB | User Download | Customer reports | High (PII) | On-demand | ❌ No | ✅ Yes |

---

### 4. Masking Checkpoint Details

**For each data flow requiring masking, define checkpoint:**

#### Checkpoint: FLOW-001 (Production → Development)

**Checkpoint Location:** Data refresh ETL process  
**Masking Technique:** Static Data Masking (SDM) - Substitution  
**Responsible Role:** DBA  
**Execution Frequency:** Weekly (every Monday 2:00 AM)  
**Validation:** Automated script (post-masking validation)  
**Monitoring:** Masking job logs reviewed daily  
**Fallback:** If masking fails, do NOT deploy to Development

**Masking Process:**

1. Snapshot production database (Sunday 11:00 PM)
2. Run masking script (Monday 1:00 AM)
3. Validate masking effectiveness (Monday 2:00 AM)
4. Deploy to Development database (Monday 3:00 AM)
5. Notify Development team (Monday 8:00 AM)

---

#### Checkpoint: FLOW-003 (Production → Analytics)

**Checkpoint Location:** Data warehouse ETL pipeline  
**Masking Technique:** Substitution + Aggregation  
**Responsible Role:** Data Engineer  
**Execution Frequency:** Hourly (real-time pipeline)  
**Validation:** Automated validation in ETL  
**Monitoring:** Pipeline monitoring dashboard  
**Fallback:** If masking fails, alert Data Engineer immediately

**Masking Process:**

1. Extract data from production (every hour)
2. Apply masking transformation in ETL
3. Validate no PII in output
4. Load to analytics platform
5. Log masking activity

---

### 5. Data Flow Risk Assessment

**For each data flow, assess risk:**

| Flow ID | Risk Factor | Assessment | Mitigation |
|---------|-------------|------------|------------|
| FLOW-001 | Unmasked data deployed | High | Mandatory masking checkpoint, validation |
| FLOW-002 | Unmasked data deployed | High | Mandatory masking checkpoint, validation |
| FLOW-003 | Re-identification risk | Medium | Aggregation + masking + re-ID testing |
| FLOW-004 | Backup media stolen | Medium | Encryption at rest, physical security |
| FLOW-005 | External data leakage | Low | Contractual obligations, anonymization |
| FLOW-006 | User downloads to laptop | High | Enforce masking, DLP monitoring |

---

### 6. Masking Checkpoint Map

**Summary of all checkpoints:**
```
Production DB
   │
   ├─[CHECKPOINT 1: Backup]─────────→ Backup Storage (Encrypted)
   │
   ├─[CHECKPOINT 2: Dev Refresh]────→ Development DB (Masked)
   │
   ├─[CHECKPOINT 3: Test Refresh]───→ Testing DB (Masked)
   │
   ├─[CHECKPOINT 4: Analytics ETL]──→ Data Warehouse (Masked)
   │
   ├─[CHECKPOINT 5: External Share]─→ External Vendor (Anonymized)
   │
   └─[CHECKPOINT 6: User Export]────→ User Download (Masked/Redacted)
```

---

### 7. Exception Flows (If Any)

**Flows where masking is NOT applied (with justification):**

| Flow ID | Source | Destination | Reason for No Masking | Compensating Controls | Approval |
|---------|--------|-------------|----------------------|----------------------|----------|
| FLOW-007 | Production DB | DR Site | Disaster recovery requires real data | Encryption, Physical security, Limited access | CISO, 2025-01-02 |

---

### 8. Validation and Monitoring

**How masking effectiveness is validated:**

- [ ] Automated validation scripts run post-masking
- [ ] Weekly manual spot-checks of masked environments
- [ ] Quarterly re-identification testing
- [ ] Monthly review of masking logs and alerts
- [ ] Annual comprehensive audit

**Monitoring Mechanisms:**

- Masking job logs (daily review)
- Data lineage tracking (automated)
- Access logs for masked environments (weekly review)
- Data export logs (real-time monitoring)
- DLP alerts for sensitive data movement (real-time)

---

### 9. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Data Owner** | [Name] | ____________ | ______ |
| **System Owner** | [Name] | ____________ | ______ |
| **Security Architect** | [Name] | ____________ | ______ |
| **ISO** | [Name] | ____________ | ______ |

---

# ANNEX S5.G – Re-identification Risk Assessment Template

## Re-identification Risk Assessment Template

**Assessment ID:** MASK-REID-[System]-[DD.MM.YYYY]  
**System/Dataset:** [Name]  
**Environment:** [Development / Testing / Analytics / External Sharing]  
**Assessed By:** [Name, Role]  
**Assessment Date:** [DD.MM.YYYY]

---

### 1. Purpose

This template assesses **whether masked data can be re-identified** (linked back to 
real individuals). Re-identification risk must be minimized to acceptable levels.

---

### 2. Dataset Overview

**Dataset Name:** [e.g., Masked Customer Database]  
**Record Count:** [Approximate number of records]  
**Data Sensitivity:** [Public / Internal / Confidential / Restricted]  
**Intended Use:** [Testing / Analytics / Training / External Sharing]  
**Retention Period:** [How long will data exist in this environment]

---

### 3. Data Fields Inventory

**List all fields in dataset, categorized:**

| Field Name | Data Type | Category | Example Masked Value | Masking Technique |
|-----------|-----------|----------|---------------------|------------------|
| customer_id | INT | Identifier | 99999 | Deterministic Substitution |
| first_name | VARCHAR | Direct Identifier (PII) | Jane | Substitution |
| last_name | VARCHAR | Direct Identifier (PII) | Doe | Substitution |
| email | VARCHAR | Direct Identifier (PII) | jane.doe@example.com | Substitution |
| date_of_birth | DATE | Quasi-Identifier | 1985-03-15 | Shuffling |
| gender | CHAR | Quasi-Identifier | F | Unmasked |
| zip_code | VARCHAR | Quasi-Identifier | 8001 | Unmasked |
| city | VARCHAR | Quasi-Identifier | Zurich | Unmasked |
| salary | DECIMAL | Sensitive Attribute | 85000 | Shuffling |
| diagnosis | VARCHAR | Sensitive Attribute | [Not in dataset] | N/A |

**Categories:**
- **Direct Identifiers:** Fields that directly identify individuals (names, emails, SSN)
- **Quasi-Identifiers:** Fields that can identify someone when combined (age, ZIP, gender)
- **Sensitive Attributes:** Fields that are sensitive but don't identify (salary, diagnosis)

---

### 4. Direct Identifier Assessment

**Direct identifiers should be MASKED or REMOVED.**

| Direct Identifier | Masked? | Technique | Re-identification Risk |
|------------------|---------|-----------|----------------------|
| first_name | ✅ Yes | Substitution (fake names) | Low (if substitution realistic) |
| last_name | ✅ Yes | Substitution (fake names) | Low (if substitution realistic) |
| email | ✅ Yes | Substitution (fake emails) | Low |
| ssn | ✅ Yes | Redaction (***-**-****) | Low |
| phone | ✅ Yes | Substitution (fake phones) | Low |

**Assessment:** ✅ All direct identifiers are masked. Risk from direct identifiers: **LOW**

---

### 5. Quasi-Identifier Assessment (K-Anonymity)

**Quasi-identifiers can identify someone when combined.**

**Quasi-Identifiers in Dataset:**
- date_of_birth (or age)
- gender
- zip_code
- city

**K-Anonymity Test:**

K-Anonymity = Each record is indistinguishable from at least (k-1) other records 
based on quasi-identifiers.

**Example:**
```
Record 1: Age=35, Gender=F, ZIP=8001 → How many other records have same combo?
Record 2: Age=35, Gender=F, ZIP=8001 → Same combo (Record 1 and 2 are indistinguishable)
Record 3: Age=35, Gender=F, ZIP=8001 → Same combo (3 total)
```

**K-Anonymity = 3** (each record with this combination has 2 others)

**K-Anonymity Calculation:**

| Quasi-Identifier Combination | Record Count | K-Value |
|-----------------------------|--------------|---------|
| Age=35, Gender=F, ZIP=8001 | 3 | 3 |
| Age=42, Gender=M, ZIP=8002 | 1 | 1 ⚠️ UNIQUE! |
| Age=28, Gender=F, ZIP=8003 | 5 | 5 |
| Age=50, Gender=M, ZIP=8001 | 2 | 2 |

**Minimum K-Value:** 1 ⚠️ (some records are unique)  
**Target K-Value:** ≥5 (industry best practice)

**Assessment:**  
❌ K-Anonymity insufficient. Some records are unique based on quasi-identifiers.  
**Re-identification Risk:** HIGH

---

### 6. Re-identification Attack Scenarios

**Test various attack scenarios:**

#### Scenario 1: Direct Matching Attack

**Attack:** Attempt to match masked dataset to production dataset using unmasked fields.

**Test:**
```sql
-- Can we match records between production and masked based on quasi-identifiers?
SELECT COUNT(*) 
FROM production.customers p
INNER JOIN masked.customers m 
  ON p.date_of_birth = m.date_of_birth 
  AND p.gender = m.gender 
  AND p.zip_code = m.zip_code;
```

**Result:** [Number of matches found]

**Assessment:**
- 0 matches: ✅ Good (likely due to shuffling)
- 1-10% matches: ⚠️ Medium risk
- >10% matches: ❌ High risk (masking insufficient)

---

#### Scenario 2: External Data Correlation Attack

**Attack:** Correlate masked data with publicly available data (e.g., voter registration, 
social media, LinkedIn).

**Test:**
- Is there public data with similar quasi-identifiers available?
- Example: Public voter registration data contains name, age, gender, ZIP
- Can masked dataset be correlated using these fields?

**Public Data Sources Checked:**
- [ ] Voter registration databases
- [ ] Social media profiles (LinkedIn, Facebook)
- [ ] Public directories
- [ ] Census data
- [ ] Other: [List]

**Result:**  
[Describe if correlation was possible]

**Assessment:**
- No correlation possible: ✅ Low risk
- Correlation possible but difficult: ⚠️ Medium risk
- Easy correlation: ❌ High risk

---

#### Scenario 3: Statistical Inference Attack

**Attack:** Use statistical properties to infer original values.

**Test:**
- If salaries are shuffled, is the HIGHEST masked salary likely to be the CEO?
- If ages are shuffled, can we infer age distribution by job title?

**Result:**  
[Describe if inference was possible]

**Assessment:**
- No inference possible: ✅ Low risk
- Limited inference: ⚠️ Medium risk
- Strong inference possible: ❌ High risk

---

#### Scenario 4: Record Linkage Attack

**Attack:** Link multiple masked datasets to identify individuals.

**Test:**
- If organization has multiple masked datasets, can they be linked?
- Example: Masked HR dataset + Masked Sales dataset → Can we identify employees?

**Result:**  
[Describe if linkage was possible]

**Assessment:**
- No linkage possible: ✅ Low risk
- Limited linkage: ⚠️ Medium risk
- Strong linkage possible: ❌ High risk

---

### 7. Overall Re-identification Risk Score

**Risk Scoring:**

| Risk Factor | Score (1-5) | Weight | Weighted Score |
|-------------|-------------|--------|----------------|
| Direct Identifiers Masked | 1 (Low) | 30% | 0.3 |
| K-Anonymity Level | 4 (High) | 25% | 1.0 |
| External Correlation Risk | 3 (Medium) | 20% | 0.6 |
| Statistical Inference Risk | 2 (Low-Med) | 15% | 0.3 |
| Record Linkage Risk | 2 (Low-Med) | 10% | 0.2 |
| **TOTAL** | | | **2.4** |

**Risk Interpretation:**

| Score | Risk Level | Action |
|-------|-----------|--------|
| 1.0 - 2.0 | **Low** | Acceptable, continue monitoring |
| 2.1 - 3.0 | **Medium** | Mitigation recommended |
| 3.1 - 4.0 | **High** | Immediate mitigation required |
| 4.1 - 5.0 | **Critical** | Do NOT deploy, redesign masking |

**Overall Risk Level:** MEDIUM (Score: 2.4)

---

### 8. Risk Mitigation Recommendations

**Based on assessment, recommend mitigations:**

| Issue | Mitigation | Responsible | Target Date |
|-------|-----------|-------------|-------------|
| K-Anonymity too low (k=1 for some records) | Apply generalization (age → age ranges, ZIP → broader regions) | DBA | [Date] |
| External correlation possible | Add noise to quasi-identifiers, further masking | Security Architect | [Date] |
| Statistical inference risk | Apply differential privacy techniques | Data Scientist | [Date] |
| Record linkage possible across datasets | Use different masking keys per dataset | DBA | [Date] |

---

### 9. Residual Risk Acceptance

**After mitigations, residual risk:**

**Residual Risk Level:** [Low / Medium / High]  
**Residual Risk Score:** [Recalculated score after mitigations]

**Risk Acceptance:**

- [ ] **Accepted** by Data Owner and CISO (if Low/Medium)
- [ ] **Not Accepted** → Further mitigation required (if High)

**Acceptance Signature:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Data Owner** | [Name] | ____________ | ______ |
| **ISO** | [Name] | ____________ | ______ |
| **CISO** | [Name] | ____________ | ______ |

---

### 10. Monitoring and Re-Assessment

**Re-identification risk SHALL be re-assessed:**

- [ ] Quarterly (minimum)
- [ ] When new public data sources become available
- [ ] When dataset structure changes (new fields added)
- [ ] When new re-identification techniques emerge

**Next Assessment Due:** [Date]

---

## References

- **ISMS-POL-A.8.11-S1:** Purpose, Scope, Definitions
- **ISMS-POL-A.8.11-S2.2:** Masking Techniques
- **ISMS-POL-A.8.11-S2.3:** Environment Requirements
- **ISMS-POL-A.8.11-S2.4:** Testing & Validation
- **ISMS-POL-A.8.11-S3:** Roles & Responsibilities
- **ISMS-POL-A.8.11-S4:** Policy Governance
- **ISO/IEC 27001:2022 Control A.8.11**
- **ISO/IEC 27002:2022 Guidance for A.8.11**

---

**END OF SECTION S5 – ANNEXES**
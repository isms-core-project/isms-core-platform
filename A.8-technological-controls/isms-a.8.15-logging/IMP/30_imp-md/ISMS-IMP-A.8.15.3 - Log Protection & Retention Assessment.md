**ISMS-IMP-A.8.15.3 - Log Protection & Retention Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.3 |
| **Version** | 1.0 |
| **Assessment Area** | Log Protection, Integrity, Access Control & Retention Compliance |
| **Related Policy** | ISMS-POL-A.8.15, Section 2.2 (Log Protection & Integrity), Section 2.3 (Log Retention & Storage), Section 2.5 (Privacy & Data Protection) |
| **Purpose** | Verify log integrity protection mechanisms, validate access controls, assess retention compliance, evaluate privacy controls |
| **Target Audience** | Information Security Team, SOC, IT Operations, Data Protection Officer (DPO), Legal/Compliance, Storage Team, Auditors, Workbook Developers |
| **Assessment Type** | Security & Compliance |
| **Review Cycle** | Semi-annual (full assessment), Quarterly (retention compliance check) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Workbook Structure Overview
  - Sheet-by-Sheet Specifications
  - Formula Definitions
  - Cell Styling Reference
  - Python Script Usage Notes

**Target Audiences:**

- **Part I:** Assessment users (InfoSec Team, SOC, IT Ops, DPO, Legal/Compliance)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** Information Security Team, SOC, IT Operations, DPO, Legal/Compliance

---

# Assessment Overview

## What This Assessment Evaluates

This assessment evaluates LOG PROTECTION AND RETENTION - how logs are protected from tampering, who can access them, how long they're kept, and whether privacy requirements are met.

**Key Questions Answered:**

- Are logs protected from unauthorized modification or deletion?
- Who has access to logs? (Access control verification)
- Are retention periods compliant with policy and regulatory requirements?
- Are privacy requirements met? (GDPR, nDSG data minimization)
- Are tamper detection mechanisms in place and working?
- Is secure disposal implemented after retention period expires?

**What This Assessment Is NOT:**

- NOT about which systems are logging (that's IMP-A.8.15.1 - Log Source Inventory)
- NOT about log collection infrastructure (that's IMP-A.8.15.2 - Log Collection)
- NOT about log review procedures (that's IMP-A.8.15.4 - Log Analysis & Review)

This is purely about **PROTECTION** (integrity, access control) and **RETENTION** (compliance with retention requirements).

## Why This Matters

This assessment verifies [Organization]'s compliance with:

- **ISO/IEC 27001:2022 Control A.8.15**: Logs must be "kept" - requires protection from tampering and appropriate retention
- **ISMS-POL-A.8.15, Section 2.2 (Log Protection)**: Integrity protection, access control, tamper detection requirements
- **ISMS-POL-A.8.15, Section 2.3 (Log Retention)**: Minimum retention periods per regulation (PCI DSS 12 months, HIPAA 6 years, SOX 7 years)
- **ISMS-POL-A.8.15, Section 2.5 (Privacy)**: Data minimization, purpose limitation, GDPR/nDSG compliance
- **PCI DSS Requirement 10.3** (if applicable): Log integrity protection and access control
- **GDPR Article 32** (if applicable): Security measures including integrity and confidentiality of logs

**Security Impact**:

- **Attackers modify logs to hide tracks** - integrity protection prevents evidence destruction
- **Insider threats access sensitive logs** - access control prevents unauthorized viewing of confidential data
- **Premature log deletion** - retention compliance ensures evidence available for investigations
- **Privacy violations** - logging excessive personal data creates GDPR violations

**Compliance Impact**:

- **Major non-conformity** if logs not protected from tampering (ISO 27001 audit finding)
- **Regulatory fines** if retention requirements not met (PCI DSS, HIPAA, SOX violations)
- **Privacy violations** if personal data logged unnecessarily (GDPR/nDSG fines)

**Audit Evidence**: This assessment workbook provides **objective evidence** of log protection and retention compliance.

## Assessment Outputs

**Primary Deliverable**: Excel workbook with 11 sheets containing:

1. **Access Control Verification**: Who can access logs, RBAC validation, separation of duties
2. **Integrity Protection Assessment**: Tamper protection mechanisms (WORM, signatures, hashing)
3. **Retention Compliance Tracking**: Actual retention vs. policy requirements per log category
4. **Disposal Procedures Verification**: Secure deletion after retention period expires
5. **Privacy Impact Assessment**: Data minimization, prohibited data types, GDPR compliance
6. **Tamper Detection Testing**: Alert verification, integrity validation procedures
7. **Legal Hold Management**: Legal hold processes, chain of custody procedures
8. **Gap Analysis**: Non-compliance findings, remediation plans
9. **Compliance Scoring**: % compliance with policy and regulatory requirements

**Typical Assessment Results**:

- **Access Control Compliance**: 90-98% (some legacy systems with overly broad access)
- **Integrity Protection**: 75-95% (critical systems protected, standard systems may lack WORM/signing)
- **Retention Compliance**: 85-100% (most categories compliant, occasional gaps in archive tiers)
- **Privacy Compliance**: 80-95% (some legacy logs contain excessive personal data)
- **Gaps Identified**: 10-25 findings requiring remediation

## Relationship to Other Assessments

**Sequential Dependencies**:

```
IMP-A.8.15.1 (Log Source Inventory)
    |
    v
    Identifies WHAT systems log
    |
    v
IMP-A.8.15.2 (Log Collection)
    |
    v
    Verifies logs COLLECTED in SIEM
    |
    v
IMP-A.8.15.3 (Protection & Retention) <-- YOU ARE HERE
    |
    v
    Verifies logs PROTECTED and RETAINED
    |
    v
IMP-A.8.15.4 (Analysis & Review)
    |
    v
    Verifies logs ANALYZED and REVIEWED
    |
    v
IMP-A.8.15.5 (Compliance Dashboard)
    |
    v
    Consolidates all assessments
```

**Recommended Order**: Complete IMP-A.8.15.1 and IMP-A.8.15.2 FIRST (know what logs exist and where they're stored), then complete this assessment (verify protection and retention).

---

# Prerequisites

**Before Starting This Assessment:**

## Required Completed Work

**RECOMMENDED**: Complete **ISMS-IMP-A.8.15.2 (Log Collection & Centralization)** first.

**Why?** This assessment validates protection and retention of logs stored in SIEM/storage infrastructure. You need to know WHERE logs are stored (IMP-A.8.15.2 Sheet 3 - Storage Architecture) before assessing HOW they're protected.

**If IMP-A.8.15.2 not complete:**

- You can still proceed, but will need to document storage architecture manually
- Sheet 3 will reference IMP-A.8.15.2 if available, otherwise manual entry required

## Required Access

**SIEM/Storage Platform Access**:

- Read access to SIEM access control configuration (user permissions, roles)
- Access to storage system configuration (retention settings, WORM configuration)
- Ability to view audit logs (who accessed logging infrastructure)
- Permission to test tamper detection (if available in test environment)

**Policy & Documentation Access**:

- Data classification policy (to verify log data classifications)
- Retention schedules (organizational retention policies)
- Privacy policy and DPIA documentation (for privacy assessment)
- Legal hold procedures (if any active legal holds)

**Operational Records**:

- Access control change logs (who granted/revoked log access)
- Retention compliance reports (quarterly/annual reports)
- Disposal records (evidence of secure log deletion)
- Legal hold documentation (active holds, chain of custody)

## Required Personnel

**Who Should Complete This Assessment**:

**Primary Responsibility**:

- **Information Security Manager**: Understands access control requirements, integrity protection needs
- **SIEM Administrator**: Knows technical configuration, retention settings

**Supporting Input Required From**:

- **SOC Team**: Access control needs, operational experience with log access
- **IT Operations**: Storage infrastructure, retention implementation, disposal procedures
- **Data Protection Officer (DPO)**: Privacy requirements, GDPR/nDSG compliance
- **Legal/Compliance**: Retention requirements, legal hold procedures, regulatory obligations
- **Internal Audit**: Audit perspective, compliance verification needs

**Estimated Time**: 10-15 hours (distributed across multiple personnel over 2-3 weeks)

## Required Tools & Documentation

**Tools**:

- SIEM administration interface access
- Storage management console (for retention configuration review)
- Identity management system (to verify role assignments)
- Previous IMP-A.8.15.2 workbook (storage architecture reference)

**Documentation**:

- SIEM access control matrix (roles and permissions)
- Storage retention configuration (tiered retention settings)
- Privacy impact assessment (DPIA) for logging
- Regulatory requirements documentation (PCI DSS, HIPAA, SOX applicability)
- Previous assessment results (if repeat assessment)

---

# Assessment Workflow

## Recommended Completion Sequence

**Phase 1: Access Control & Protection (Sheets 1-4)**

- Sheet 1: Instructions (read thoroughly)
- Sheet 2: Access Control Verification (who can access logs, RBAC validation)
- Sheet 3: Integrity Protection Assessment (WORM, signatures, hashing, encryption)
- Sheet 4: Tamper Detection Testing (alert verification, integrity checks)

**Phase 2: Retention & Disposal (Sheets 5-6)**

- Sheet 5: Retention Compliance Tracking (policy vs. actual retention per log category)
- Sheet 6: Disposal Procedures Verification (secure deletion implementation)

**Phase 3: Privacy & Legal (Sheets 7-8)**

- Sheet 7: Privacy Impact Assessment (data minimization, prohibited data, GDPR compliance)
- Sheet 8: Legal Hold Management (active holds, chain of custody)

**Phase 4: Review & Approval (Sheets 9-11)**

- Sheet 9: Gap Analysis (identify non-compliance, remediation plans)
- Sheet 10: Evidence Register (document all supporting evidence)
- Sheet 11: Approval Sign-Off (three-level approval process)

**Estimated Timeline**:

- Phase 1: 4-6 hours (access control and protection mechanisms)
- Phase 2: 3-4 hours (retention compliance and disposal)
- Phase 3: 2-3 hours (privacy assessment and legal hold)
- Phase 4: 2-3 hours (gap analysis, evidence, approvals)

**Total**: 11-16 hours (spread over 2-3 weeks to gather cross-functional input)

## Iterative Approach

**Don't try to complete everything in one sitting.** This assessment requires cross-functional collaboration:

**Week 1**:

- InfoSec Manager completes access control verification (Sheet 2)
- SIEM Administrator completes integrity protection assessment (Sheet 3)
- IT Operations provides retention configuration (Sheet 5)

**Week 2**:

- DPO completes privacy impact assessment (Sheet 7)
- Legal/Compliance reviews legal hold procedures (Sheet 8)
- InfoSec Manager coordinates tamper detection testing (Sheet 4)

**Week 3**:

- Cross-functional gap analysis workshop (Sheet 9)
- Evidence collection and consolidation (Sheet 10)
- Approval process initiated (Sheet 11)

## Data Collection Methods

**Access Control Verification**:

- Export user roles from SIEM (who has log access)
- Review access control configuration (RBAC settings)
- Analyze access logs (who actually accessed logs in last 90 days)
- Interview SOC team (understand operational access needs)

**Integrity Protection Assessment**:

- Review SIEM storage configuration (WORM enabled? Encryption?)
- Test tamper detection (attempt log modification in test environment)
- Verify cryptographic implementations (hashing algorithms, signature methods)
- Check separation of duties (log admins != system admins)

**Retention Compliance Tracking**:

- Compare actual retention (from IMP-A.8.15.2 Sheet 3) to policy requirements
- Verify regulatory retention periods (PCI DSS, HIPAA, SOX where applicable)
- Check retention configuration (automated vs. manual enforcement)
- Review disposal records (evidence retention periods being enforced)

**Privacy Assessment**:

- Review log samples (check for prohibited data types per policy Section 2.5)
- Interview application owners (understand what's being logged)
- Assess data minimization (is all logged data necessary?)
- Verify GDPR/nDSG compliance (purpose limitation, transparency)

---

# Completing Each Sheet

## Sheet 1: Instructions & Legend

**Purpose**: Understand assessment methodology and scoring criteria.

**Completion**:
1. Read instructions thoroughly
2. Review scoring methodology (0-100% compliance scale)
3. Note color coding (Red = Critical Gap, Yellow = Improvement Needed, Green = Compliant)
4. Understand assessment focus (protection + retention, not collection or analysis)

**Time**: 15-20 minutes (first-time users), 5 minutes (returning users)

## Sheet 2: Access Control Verification

**Purpose**: Verify log access is restricted to authorized personnel with legitimate business need.

**What to Document**:

**For Each User/Role with Log Access**:

- User ID / Service Account
- User Name
- Role (SOC Analyst, Security Engineer, InfoSec Manager, CISO, Auditor, System Administrator)
- Access Level (Read-Only, Read-Write, Admin, No Access)
- Access Scope (All logs, Security logs only, Specific systems, Specific time period)
- Business Justification (Why does this user need log access?)
- Last Access Date (When did they last access logs? Verify from audit logs)
- Access Review Date (When was this access last reviewed and approved?)
- Access Approved By (Who authorized this access?)

**Policy Requirements (from ISMS-POL-A.8.15 Section 2.2)**:

- **Read access restricted to**: SOC analysts, security engineers, InfoSec Manager, CISO, authorized auditors
- **Write access**: Logging service daemons and system logging processes ONLY (no human write access)
- **Administrative access**: Requires multi-person authorization
- **Separation of duties**: System administrators SHALL NOT have administrative access to logging infrastructure
- **Log access SHALL be logged**: Logging the log access for accountability

**Verification Methods**:

- Export user list from SIEM (all users with any log access)
- Review RBAC configuration (role definitions, assigned permissions)
- Analyze access audit logs (who accessed logs in last 90 days)
- Compare against policy requirements (identify excessive or inappropriate access)

**Common Findings**:

- System administrators have log access (violates separation of duties)
- Former employees still have active accounts (access not revoked)
- Service accounts with excessive permissions (not least-privilege)
- No access review process (stale permissions never revoked)
- Log access not logged (no audit trail of who viewed logs)

**Compliance Scoring**:

- % of users with justified, approved access
- % of users with appropriate access level (not excessive)
- Separation of duties enforced (0% system admins with log admin access = compliant)
- Access logging enabled (yes/no)
- Regular access reviews conducted (quarterly minimum per policy)

**Evidence Required**:

- SIEM user export (list of all users and roles)
- RBAC configuration screenshot
- Access audit log samples (showing access is logged)
- Access review documentation (quarterly review records)
- Approval records (who approved each user's access)

**Time**: 2-3 hours

## Sheet 3: Integrity Protection Assessment

**Purpose**: Verify logs are protected from unauthorized modification or deletion.

**What to Document**:

**For Each Log Storage Tier** (Hot/Warm/Cold):

**Protection Mechanisms**:

- **WORM Storage** (Write-Once-Read-Many):
  - Enabled? (Yes, No, Partial)
  - Technology (Hardware WORM, Software WORM, Cloud Object Lock, Tape)
  - Validation Method (How is WORM verified? Attempted modification test, vendor certification)
  - Compliance Status (Meets policy Section 2.2 requirement for audit logs?)

- **Cryptographic Protection**:
  - Digital Signatures (Enabled? Algorithm used? Key management?)
  - Cryptographic Hashing (Log entries hashed? Hash chain maintained? Algorithm?)
  - Tamper-Evident Mechanisms (Checksums? Integrity seals?)

- **Access Control** (from Sheet 2):
  - Write Protection (No human write access to logs confirmed?)
  - Administrative Controls (Multi-person authorization required?)
  - Separation of Duties (Log admins != system admins confirmed?)

- **Centralized Collection**:
  - Immediate Forwarding (Logs forwarded immediately to SIEM preventing local deletion?)
  - Local Log Retention (Are local logs retained on source systems? For how long?)
  - Local Log Protection (If local logs exist, are they protected from deletion?)

**For Critical Systems** (per IMP-A.8.15.1 Criticality = "Critical"):

- Enhanced Protection Required (Policy Section 2.2: WORM or cryptographic signing for critical systems)
- Protection Level Verified (Does protection meet policy requirement?)
- Gap Identified (If critical system logs not adequately protected)

**Protection Testing** (if feasible):

- Test Environment Available (Can log modification be tested safely?)
- Modification Attempt (Attempt to modify/delete log in test environment)
- Detection Result (Was modification blocked? Alert generated?)
- Evidence Collected (Screenshot of blocked modification, alert notification)

**Policy Compliance** (ISMS-POL-A.8.15 Section 2.2):

- WORM or signing for audit logs (security events, authentication, administrative actions)
- Tamper detection implemented (checksums, hash chains, signature verification)
- Centralized collection (immediate forwarding to SIEM)
- Separation of duties (enforced for logging infrastructure)
- Access control (write access restricted to logging processes only)

**Compliance Scoring**:

- % of critical log sources with WORM or cryptographic protection
- % of log storage tiers with tamper detection
- Centralized collection coverage (% immediately forwarded)
- Separation of duties enforced (yes/no binary)
- Overall integrity protection score (weighted average)

**Evidence Required**:

- WORM configuration documentation (vendor spec, configuration screenshot)
- Cryptographic implementation details (algorithms, key management)
- Tamper detection test results (modification attempt blocked/detected)
- Separation of duties verification (role segregation confirmed)

**Time**: 3-4 hours (includes testing if feasible)

## Sheet 4: Tamper Detection Testing

**Purpose**: Verify tamper detection mechanisms are operational and generate alerts.

**What to Test**:

**Test Scenarios** (conduct in test/staging environment):

**Scenario 1: Log Modification Attempt**:

- Test Setup: Identify test log file or SIEM index
- Test Action: Attempt to modify existing log entry (change timestamp, user ID, or event details)
- Expected Result: Modification blocked OR modification succeeds but alert generated
- Actual Result: Document what happened
- Pass/Fail: Pass if blocked or detected, Fail if modification successful without detection

**Scenario 2: Log Deletion Attempt**:

- Test Setup: Identify test logs within retention period
- Test Action: Attempt to delete log file or SIEM data before retention expiration
- Expected Result: Deletion blocked OR deletion succeeds but alert generated
- Actual Result: Document what happened
- Pass/Fail: Pass if blocked or detected, Fail if deletion successful without detection

**Scenario 3: Integrity Verification**:

- Test Setup: Access integrity verification mechanism (checksum validation, signature verification)
- Test Action: Run integrity check on known-good logs
- Expected Result: Integrity check passes, no violations detected
- Actual Result: Document result
- Pass/Fail: Pass if integrity verified successfully

**Scenario 4: Alert Generation**:

- Test Setup: Review alert configuration for tamper detection
- Test Action: Verify alerts are configured to fire on integrity violations
- Expected Result: Alert defined, destination configured (SOC email/SIEM alert)
- Actual Result: Document alert configuration
- Pass/Fail: Pass if alert properly configured and tested

**For Production Environment** (if testing not feasible):

- Document why testing not conducted (no test environment, risk of disruption)
- Alternative verification: Review historical tamper detection alerts (any alerts in last 12 months?)
- Review configuration: Verify tamper detection enabled in configuration (screenshot)
- Vendor validation: Rely on vendor certification or third-party audit (if available)

**Alert Effectiveness Assessment**:

- Alerts Configured (Yes/No for each tamper detection mechanism)
- Alert Destination (Where do alerts go? SOC email, SIEM, ticketing system)
- Alert Testing (Have alerts been tested? When? Result?)
- False Positive Rate (Are alerts firing inappropriately?)
- Response Procedures (What happens when alert fires? Documented procedure?)

**Compliance Status**:

- Tamper detection operational (yes/no)
- Alerts configured and tested (yes/no)
- Response procedures documented (yes/no)
- Overall tamper detection effectiveness score

**Evidence Required**:

- Test results documentation (screenshots, test logs, alert notifications)
- Alert configuration screenshots (SIEM correlation rules, email alerts)
- Incident response procedures (what to do when tamper detected)
- Historical alert analysis (any tamper alerts in last 12 months? How handled?)

**Time**: 2-3 hours (including test execution and documentation)

## Sheet 5: Retention Compliance Tracking

**Purpose**: Verify actual log retention meets policy and regulatory requirements.

**What to Document**:

**For Each Log Category** (from ISMS-POL-A.8.15 Section 2.3):

**Policy Requirements**:

- Log Category (Security Events, Authentication Logs, Admin Actions, Database Logs, Application Logs, Network Logs, System Logs)
- Policy Requirement - Online (months required in hot storage)
- Policy Requirement - Archive (years total retention including offline)
- Regulatory Driver (ISO 27001, GDPR, PCI DSS, HIPAA, SOX, etc.)

**Actual Implementation** (from IMP-A.8.15.2 Sheet 3 if available):

- Actual Retention - Hot Storage (months currently retained online)
- Actual Retention - Warm Storage (months in nearline/compressed)
- Actual Retention - Cold Archive (years in offline/tape/object storage)
- Total Actual Retention (sum of all tiers)

**Compliance Calculation**:

- Compliance Status: `IF(Actual >= Required, "Y Compliant", "N Non-Compliant")`
- Gap (if non-compliant): Required - Actual (how many months/years short?)
- Over-Retention (if applicable): Actual - Required (retaining longer than required - privacy risk if excessive)

**Regulatory-Specific Requirements** (per ISMS-POL-00 applicability):

**If PCI DSS Applicable**:

- Payment system logs: 12 months online minimum (Req. 10.5.1)
- Actual retention >= 12 months? (yes/no)

**If HIPAA Applicable**:

- ePHI access logs: 6 years minimum (Sec.164.316(b)(2))
- Actual retention >= 6 years? (yes/no)

**If SOX Applicable**:

- Financial system audit trails: 7 years minimum
- Actual retention >= 7 years? (yes/no)

**Retention Configuration Verification**:

- Automated Retention Enforcement (Is retention enforced by system? Yes/No/Manual)
- Retention Policy Configuration (Where configured? SIEM settings, storage policy, manual process)
- Retention Monitoring (How is retention compliance monitored? Automated alerts, manual review, quarterly audit)
- Disposal Automation (Are logs auto-deleted after retention period? Yes/No/Manual)

**Over-Retention Privacy Risk**:

- Over-Retained Categories (Which categories retained longer than policy requires?)
- Privacy Impact (Does over-retention create GDPR/nDSG compliance risk?)
- Justification Required (If over-retained, document business justification or identify as gap)

**Compliance Summary**:

- Total Log Categories Assessed (count)
- Categories Compliant (count and %)
- Categories Non-Compliant - Under-Retention (count and % - compliance risk)
- Categories Over-Retained (count and % - privacy risk)
- Overall Retention Compliance Score (% compliant)

**Evidence Required**:

- Retention configuration screenshots (SIEM retention policies, storage lifecycle policies)
- Retention monitoring reports (quarterly compliance checks)
- Storage capacity reports showing actual data age (oldest logs, retention verification)
- Disposal records (evidence that expired logs are being deleted)

**Time**: 2-3 hours

## Sheet 6: Disposal Procedures Verification

**Purpose**: Verify secure log disposal after retention period expires.

**What to Document**:

**Disposal Policy Requirements** (ISMS-POL-A.8.15 Section 2.3):

- Logs SHALL be securely deleted after retention period expires
- Cryptographic erasure for encrypted log storage (destroy encryption keys)
- Physical media destruction for write-once media (NIST SP 800-88 guidelines)
- Disposal events logged (date, log category, retention period, responsible person)

**Disposal Procedures**:

**For Each Storage Tier** (Hot/Warm/Cold):

- **Disposal Method**:
  - Automated deletion (SIEM auto-purge, storage lifecycle policy)
  - Manual deletion (administrator deletes expired logs)
  - Cryptographic erasure (encryption keys destroyed)
  - Physical destruction (tape shredding, disk degaussing, crush/shred)
  - No disposal process (gap - logs never deleted)

- **Disposal Trigger**:
  - Automated (system deletes when retention expires)
  - Scheduled (quarterly disposal job)
  - On-demand (manual deletion when storage full)
  - Never (no disposal implemented - compliance gap)

- **Disposal Verification**:
  - How is disposal verified? (Audit logs, capacity monitoring, manual inspection)
  - Disposal logged? (Date, volume, log category, person responsible)
  - Disposal documentation retained? (Disposal records kept as evidence)

- **Secure Deletion Standard**:
  - Method meets NIST SP 800-88? (Clear, Purge, Destroy per media type)
  - Overwrite passes (if disk overwrite - how many passes? 7-pass DoD 5220.22-M?)
  - Verification (Is secure deletion verified? How?)

**Legal Hold Exception Handling**:

- Legal Hold Check (Are logs checked for legal hold before disposal?)
- Hold Flag (How are logs under legal hold flagged to prevent disposal?)
- Hold Tracking (Are legal holds tracked? Where? Spreadsheet, system flag, manual process)
- Disposal After Hold Release (Process to resume disposal after hold expires)

**Disposal Audit Trail**:

- Disposal Events Logged (Is each disposal event logged?)
- Log Content (What's recorded? Date, log category, volume disposed, retention period, person)
- Log Retention (How long are disposal logs kept? Minimum 7 years recommended)
- Audit Access (Can auditors access disposal logs?)

**Compliance Assessment**:

- Disposal procedures documented (yes/no)
- Disposal method adequate (meets NIST SP 800-88 or equivalent)
- Disposal automated (yes/no - automation preferred over manual)
- Disposal logged (yes/no - required per policy Section 2.3)
- Legal hold check implemented (yes/no)
- Overall disposal compliance score

**Disposal Testing** (if feasible):

- Test Environment: Identify test logs past retention period
- Test Execution: Execute disposal procedure
- Verification: Confirm logs actually deleted (not just marked for deletion)
- Evidence: Screenshot showing logs removed, disposal log entry created

**Evidence Required**:

- Disposal procedure documentation (step-by-step disposal process)
- Disposal configuration (SIEM auto-purge settings, storage lifecycle policies)
- Disposal logs (records of past disposals - last 12 months minimum)
- Legal hold procedures (how logs are protected during legal hold)
- NIST SP 800-88 compliance documentation (disposal method validation)

**Time**: 1-2 hours

## Sheet 7: Privacy Impact Assessment

**Purpose**: Verify logging complies with privacy regulations (GDPR, nDSG) and policy Section 2.5.

**What to Document**:

**Data Minimization Assessment**:

**For Each Log Category**:

- Log Category (Security Events, Authentication, Admin Actions, etc.)
- Data Types Logged (What information is in these logs?)
- Personal Data Present (Yes/No - does log contain personal data?)
- Personal Data Types (User IDs, IP addresses, email addresses, location data, etc.)
- Data Necessity (Is all logged data necessary for security/compliance purpose?)
- Minimization Compliant (Is only necessary data logged? Yes/No)

**Prohibited Data Verification** (ISMS-POL-A.8.15 Section 2.5):

Check logs for presence of PROHIBITED data types:

- [ ] Passwords (cleartext) - SHALL NOT be logged
- [ ] Full credit card numbers (PAN) - SHALL NOT be logged (mask to first 6 + last 4)
- [ ] National identification numbers - SHALL NOT be logged
- [ ] Full health information - SHALL NOT be logged (log access events only, not diagnosis)
- [ ] Full contents of personal communications - SHALL NOT be logged (metadata only)
- [ ] Biometric templates - SHALL NOT be logged (authentication events only, not biometric data)
- [ ] Session tokens or API keys - SHALL NOT be logged (issuance events only, not actual values)

**If prohibited data found**:

- Where found (specific log source, log category)
- How to remediate (log format change, data masking, log filtering)
- Remediation owner (who will fix)
- Target date (when fixed)

**GDPR/nDSG Compliance** (if applicable per ISMS-POL-00):

**Article 5(1)(c) - Data Minimization**:

- Logging limited to necessary data (yes/no)
- Excessive data identified (any unnecessary personal data logged?)

**Article 5(1)(b) - Purpose Limitation**:

- Logs used only for: security incident detection, investigation, compliance, system administration (yes/no)
- Purpose documented (yes/no)
- Secondary use restricted (logs not used for employee monitoring beyond security needs)

**Article 5(1)(e) - Storage Limitation**:

- Retention justified (retention periods documented with legal/business justification)
- Retention not excessive (not retaining longer than necessary - see Sheet 5 over-retention)

**Article 32 - Security of Processing**:

- Logs protected (integrity and confidentiality verified - see Sheets 2-3)
- Access controlled (only authorized personnel - see Sheet 2)

**Transparency Requirements**:

- Users informed of logging (Acceptable Use Policy, employment contract, privacy notice?)
- Logging scope disclosed (what activities logged, how long retained, who has access)
- Privacy notice updated (logging practices described in organizational privacy policy)

**Employee Monitoring Considerations**:

- Works council consulted (if applicable in jurisdiction - EU labor law)
- Employee monitoring proportionate (legitimate business interest, not excessive surveillance)
- Monitoring documented (scope and purpose of employee activity logging clear)

**Data Subject Rights**:

- Access requests process (Can individuals request access to logs containing their personal data?)
- Erasure request handling (GDPR Art. 17 - right to erasure vs. legal obligations exception)
- Legal basis documented (GDPR Art. 6(1)(c) legal obligation + Art. 6(1)(f) legitimate interest)

**Privacy Compliance Score**:

- Data minimization compliant (% of log categories minimizing data)
- No prohibited data (yes/no - binary compliance)
- GDPR/nDSG compliant (% of GDPR articles addressed)
- Transparency requirements met (yes/no)
- Overall privacy compliance score

**Evidence Required**:

- Log samples (review for prohibited data - redact sensitive info in evidence)
- Data classification mapping (which logs contain what data types)
- Privacy notice (organizational privacy policy referencing logging)
- Acceptable use policy (employees informed of logging)
- DPIA (Data Protection Impact Assessment for logging - if required)
- Legal basis documentation (GDPR Article 6 legal basis for logging)

**Time**: 2-3 hours (requires DPO input)

## Sheet 8: Legal Hold Management

**Purpose**: Verify legal hold processes prevent premature log disposal during litigation/investigation.

**What to Document**:

**Legal Hold Process** (ISMS-POL-A.8.15 Section 2.3):

**Legal Hold Notification Handling**:

- How are legal holds received? (Legal department notification, email, formal process)
- Who receives notification? (InfoSec Manager, CISO, Legal, IT Operations)
- Notification response time (How quickly is disposal suspended? Immediate, 24 hours, manual)

**Legal Hold Scope Documentation**:

- Scope definition process (How is scope determined? Which logs, which time period, which systems)
- Scope documentation (Where recorded? Spreadsheet, ticketing system, formal legal hold system)
- Scope clarity (Is scope clear enough to identify affected logs?)

**Disposal Suspension Implementation**:

- How is disposal suspended? (Automated flag, manual process, communication to IT Ops)
- Verification (How is suspension verified? Spot checks, automated verification, manual confirmation)
- Segregation (Are affected logs segregated from normal disposal processes? Physical separation, logical flag)
- Immutability (Are logs under hold made immutable? WORM, access restrictions, backup copy)

**Chain of Custody Procedures**:

- Chain of custody maintained (yes/no)
- Custody documentation (Who has custody, when transferred, to whom)
- Access logging (All access to logs under legal hold logged)
- Integrity verification (Logs under hold verified for tampering)

**Active Legal Holds Inventory**:

**For Each Active Legal Hold** (if any):

- Hold ID (Unique identifier)
- Hold Initiation Date
- Hold Requestor (Legal counsel name, case reference)
- Scope - Log Categories Affected
- Scope - Time Period (date range of logs under hold)
- Scope - Systems Affected (which systems' logs are held)
- Hold Status (Active, Released, Partial Release)
- Estimated Hold Duration (if known)
- Hold Documentation Location (where is formal hold notice stored)

**Legal Hold Review Process**:

- Review frequency (Quarterly review of active holds recommended)
- Review participants (Legal, InfoSec Manager, IT Operations)
- Review actions (Confirm hold still needed, update scope if needed, release if no longer needed)
- Review documentation (Meeting minutes, review decisions recorded)

**Legal Hold Release Process**:

- Release notification (How is release communicated? Formal notice from Legal)
- Release verification (Who verifies release authority? Legal sign-off)
- Disposal resumption (How does disposal resume? Automated, manual, backlog processing)
- Release documentation (Date released, authority, disposal actions taken)

**Compliance Assessment**:

- Legal hold process documented (yes/no)
- Active holds tracked (yes/no - inventory maintained)
- Disposal suspension verified (yes/no - holds actually preventing disposal)
- Chain of custody maintained (yes/no - for logs used as legal evidence)
- Quarterly reviews conducted (yes/no)
- Overall legal hold compliance score

**Evidence Required**:

- Legal hold procedures document (step-by-step process)
- Active legal holds inventory (list of current holds if any)
- Chain of custody templates (forms used to track legal hold logs)
- Legal hold release documentation (past releases - evidence process works)
- Review meeting minutes (quarterly legal hold reviews)

**Time**: 1-2 hours (less if no active legal holds, more if complex active holds)

---

# Evidence Collection

## Evidence Types

**For Access Control (Sheet 2)**:

- SIEM user export (list of all users with log access)
- RBAC configuration screenshots (role definitions, permissions)
- Access audit logs (sample of who accessed logs, when, what they viewed)
- Access review documentation (quarterly review records, approval signatures)
- Separation of duties verification (organizational chart showing log admins != system admins)

**For Integrity Protection (Sheet 3)**:

- WORM configuration documentation (vendor specs, configuration screenshots)
- Cryptographic implementation details (algorithms used, key management procedures)
- Tamper detection configuration (checksums enabled, signature verification settings)
- Separation of duties evidence (role segregation matrix)
- Centralized collection verification (logs immediately forwarded to SIEM)

**For Tamper Detection (Sheet 4)**:

- Test results documentation (screenshots of modification attempts, results)
- Alert configuration screenshots (SIEM correlation rules for tamper detection)
- Alert test results (proof that alerts fire when tamper detected)
- Incident response procedures (what to do when tamper alert fires)
- Historical tamper alerts (any alerts in last 12 months, how handled)

**For Retention Compliance (Sheet 5)**:

- Retention policy configuration (SIEM retention settings, storage lifecycle policies)
- Retention verification reports (storage reports showing actual log age/retention)
- Regulatory requirement documentation (PCI DSS, HIPAA, SOX applicability per ISMS-POL-00)
- Capacity reports (proving retention periods achievable with current storage)

**For Disposal Procedures (Sheet 6)**:

- Disposal procedure documentation (step-by-step disposal process)
- Disposal logs (records of past disposals - date, volume, category, responsible person)
- NIST SP 800-88 compliance documentation (disposal method meets standard)
- Legal hold procedures (how logs protected during litigation)
- Secure deletion verification (proof disposal method is secure)

**For Privacy Assessment (Sheet 7)**:

- Log samples (reviewed for prohibited data - redacted for evidence)
- Privacy notice (organizational privacy policy mentioning logging)
- Acceptable use policy (employees informed of logging and monitoring)
- DPIA (Data Protection Impact Assessment if required by GDPR)
- Legal basis documentation (GDPR Article 6 legal basis for logging)

**For Legal Hold Management (Sheet 8)**:

- Legal hold procedures (formal process documentation)
- Active holds inventory (current legal holds if any)
- Chain of custody templates/forms
- Legal hold release documentation (evidence of past releases)
- Quarterly review meeting minutes

## Evidence Collection Best Practices

**Screenshots**:

- Include timestamps and system identifiers
- Show sufficient context (full screen or relevant window)
- Redact sensitive personal data (comply with GDPR/nDSG even in evidence)
- Label clearly (e.g., "SIEM_Access_Control_Configuration_2026-01-21.png")

**Configuration Exports**:

- Export in native format (JSON, XML, CSV) when possible
- Include metadata (export date, who exported, system version)
- Sanitize for sensitive information (credentials, internal IPs if necessary)
- Document export procedure (so it can be repeated for future assessments)

**Test Results**:

- Document test setup (test environment, test data, test procedure)
- Capture test execution (screenshots, log entries, alert notifications)
- Record test results (pass/fail, actual vs. expected)
- Note any deviations (if test didn't go as planned, document why)

**Evidence Organization**:
```
ISMS-IMP-A.8.15.3_Evidence/
|-- Sheet02_Access_Control/
|   |-- SIEM_User_Export_2026-01-21.xlsx
|   |-- RBAC_Configuration_Screenshot.png
|   `-- Access_Review_Q4-2025.pdf
|-- Sheet03_Integrity_Protection/
|   |-- WORM_Configuration_Doc.pdf
|   |-- Crypto_Implementation_Spec.pdf
|   `-- Separation_of_Duties_Matrix.xlsx
|-- Sheet04_Tamper_Detection/
|   |-- Tamper_Test_Results_2026-01-21.pdf
|   |-- Alert_Configuration_Screenshot.png
|   `-- Incident_Response_Procedure.pdf
|-- Sheet05_Retention_Compliance/
|   |-- Retention_Policy_Configuration.pdf
|   |-- Storage_Capacity_Report_2026-01.xlsx
|   `-- Regulatory_Requirements_Matrix.pdf
|-- Sheet06_Disposal_Procedures/
|   |-- Disposal_Procedure_Doc.pdf
|   |-- Disposal_Logs_2025.xlsx
|   `-- NIST_SP_800-88_Compliance.pdf
|-- Sheet07_Privacy_Assessment/
|   |-- Log_Samples_Redacted.pdf
|   |-- Privacy_Notice_2026.pdf
|   |-- DPIA_Logging_2025.pdf
|   `-- GDPR_Legal_Basis_Memo.pdf
`-- Sheet08_Legal_Hold/
    |-- Legal_Hold_Procedures.pdf
    |-- Active_Holds_Inventory.xlsx
    `-- Chain_of_Custody_Template.pdf
```

**Evidence Retention**:

- Retain for minimum 7 years (matches maximum log retention policy)
- Evidence proves assessment was evidence-based, not theoretical
- Store securely (may contain sensitive configuration or personal data)
- Index in Sheet 10 (Evidence Register) for auditability

---

# Common Pitfalls

## Pitfall: "System admins need log access for troubleshooting"

**Problem**: Granting system administrators access to logs violates separation of duties.

**Why This Happens**:

- Legitimate operational need (system admins do need logs for troubleshooting)
- Convenience (easier to give everyone access than implement role separation)
- Lack of understanding (separation of duties requirement not communicated)

**Why It's a Problem**:

- **ISO 27001 Control A.8.15 violation**: Policy Section 2.2 explicitly requires separation
- **Insider threat risk**: System admin can modify logs to hide malicious activity
- **Audit finding**: Auditors will identify this as major non-conformity

**How to Avoid**:

- **Separate roles**: System Admins != Log Admins (different people, different access)
- **Operational logs vs. security logs**: System admins get access to operational logs (system health, performance) but NOT security logs (authentication, access control, admin actions)
- **Read-only access**: If system admins MUST have access, make it read-only and log the access
- **Exception process**: If separation not feasible (small team), document compensating controls and get CISO approval per policy Section 3.3

**Evidence of Compliance**:

- Organizational chart showing different people in system admin and log admin roles
- RBAC configuration showing system admin role has NO log access
- Access audit logs showing system admins are NOT accessing security logs

## Pitfall: "We have WORM storage" (but only for some logs)

**Problem**: Assuming all logs are protected because WORM storage exists, when actually only some logs use WORM.

**Why This Happens**:

- WORM storage expensive (only critical logs get WORM, rest on standard storage)
- Partial implementation (WORM deployed but not all log sources configured to use it)
- Misunderstanding (belief that "SIEM has WORM" means all logs in SIEM are WORM-protected)

**Reality**:

- Critical system logs (per policy Section 2.2): REQUIRE WORM or cryptographic signing
- Standard system logs: MAY use WORM, or alternative protection (centralized collection, access control)
- Need to verify WHICH logs are actually on WORM storage

**How to Avoid**:

- Map log sources to storage tiers (which logs go to WORM storage? which don't?)
- Verify critical systems use WORM (per IMP-A.8.15.1 criticality assessment)
- Document gaps (critical systems NOT using WORM = gap requiring remediation)
- Alternative protection (if WORM not feasible, implement cryptographic signing)

**Evidence of Compliance**:

- Storage architecture diagram (showing which log sources use WORM)
- Configuration verification (SIEM forwarding rules sending critical logs to WORM storage)
- Critical systems list vs. WORM protected list (gap analysis)

## Pitfall: "Retention is 7 years" (for everything)

**Problem**: Applying single retention period to all logs, ignoring category-specific requirements.

**Why This Happens**:

- Simplification (easier to have one retention period than multiple)
- Over-caution (retaining everything for maximum period "to be safe")
- Misunderstanding (belief that "7 years is safest" applies universally)

**Reality**:

- Security logs: 7 years (for forensics, legal evidence)
- Application logs: 18 months (troubleshooting, no long-term legal need)
- Network logs: 18 months (capacity planning, troubleshooting)
- Over-retention = privacy risk (GDPR requires retention limitation)

**How to Avoid**:

- Use retention matrix from policy Section 2.3 (different retention per log category)
- Justify retention periods (legal requirement, business need, risk assessment)
- Privacy impact (over-retention violates GDPR Article 5(1)(e) storage limitation)
- Configure automated retention (SIEM/storage tiers enforce correct retention per category)

**Evidence of Compliance**:

- Retention configuration showing different periods per log category
- Retention justification matrix (why each category has its retention period)
- DPO sign-off (privacy officer confirmed retention periods justified)

## Pitfall: "We don't log passwords" (but session tokens logged)

**Problem**: Correctly avoiding password logging, but unknowingly logging other sensitive secrets.

**Why This Happens**:

- Focus on passwords (password logging obviously bad, well-communicated)
- Lack of awareness (session tokens, API keys equally sensitive but less obvious)
- Application logging (developers log full request/response for debugging, includes tokens)

**Reality** (policy Section 2.5 prohibited data):

- Passwords: SHALL NOT be logged Y (usually well-understood)
- Session tokens: SHALL NOT be logged (often missed)
- API keys: SHALL NOT be logged (often missed)
- OAuth tokens: SHALL NOT be logged (often missed)

**How to Avoid**:

- Review log samples (actually look at logs, check for tokens/keys)
- Regex searches (search logs for patterns: "token=", "api_key=", "Bearer ", "Authorization:")
- Developer training (educate developers on what NOT to log)
- Log scrubbing (implement filters to strip tokens/keys from logs before storage)

**Evidence of Compliance**:

- Log review documentation (proof that logs were sampled and checked)
- Negative finding (proof that tokens/keys NOT found in logs)
- Log filtering configuration (showing scrubbing rules removing sensitive data)

## Pitfall: "Disposal is automatic" (but legal hold not integrated)

**Problem**: Automated log disposal implemented, but no check for legal hold before deletion.

**Why This Happens**:

- Disposal automation implemented for efficiency
- Legal hold processes managed separately (legal dept, not IT)
- No integration (disposal system doesn't check legal hold system before deleting)

**Risk**:

- **Spoliation**: Deleting logs under legal hold = destruction of evidence
- **Legal sanctions**: Court penalties, adverse inference, case dismissal
- **Compliance failure**: Violation of policy Section 2.3 legal hold requirements

**How to Avoid**:

- **Legal hold flag**: Logs under hold must be flagged in system (prevent disposal)
- **Pre-disposal check**: Disposal process checks for legal hold flag before deleting
- **Communication**: Legal dept notifies IT of holds (and releases) promptly
- **Segregation**: Logs under hold moved to separate storage (physically/logically segregated)
- **Verification**: Quarterly review that logs under hold are NOT being disposed

**Evidence of Compliance**:

- Legal hold procedures showing IT notification process
- Disposal procedures showing legal hold check before deletion
- Legal hold inventory (current holds, systems/logs affected)
- Verification records (proof that held logs are still retained)

## Pitfall: "Privacy isn't relevant - these are security logs"

**Problem**: Assuming security logs exempt from privacy regulations because they're "security."

**Why This Happens**:

- Misunderstanding GDPR (belief that security logs are not personal data)
- Article 32 confusion (GDPR requires security measures including logging, misinterpreted as blanket exemption)

**Reality**:

- Security logs ARE personal data (user IDs, IP addresses, authentication events = personal data)
- GDPR applies (all GDPR principles apply: data minimization, purpose limitation, storage limitation)
- Article 32 is legal basis (not exemption): Logging justified under Article 32 (security) BUT still must comply with GDPR principles

**GDPR Compliance Required**:

- Data minimization (log only necessary data - don't log full health records, just "access to patient record 12345")
- Purpose limitation (use logs only for security, not general employee monitoring)
- Storage limitation (retention periods must be justified, not indefinite)
- Transparency (inform users that logging occurs)

**How to Avoid**:

- **DPO involvement**: Data Protection Officer must review logging practices
- **DPIA if needed**: High-risk logging (e.g., monitoring employee communications) may require DPIA
- **Legal basis**: Document legal basis (GDPR Article 6(1)(c) legal obligation + 6(1)(f) legitimate interest)
- **Minimize data**: Don't log full message content, full health records, excessive location data

**Evidence of Compliance**:

- DPIA (if required) showing privacy assessment of logging
- Legal basis documentation (memo from Legal/DPO confirming legal basis)
- Privacy notice (organizational privacy policy describes logging practices)
- Data minimization assessment (Sheet 7 showing unnecessary data not logged)

---

# Quality Checklist

**Before Submitting Assessment for Approval:**

## Completeness Checks

- [ ] All sheets completed (no sheets left blank)
- [ ] All yellow cells filled in (user input provided)
- [ ] All dropdown selections made (no "Select..." placeholders remaining)
- [ ] Access control fully documented (Sheet 2 - all users with log access listed)
- [ ] Integrity protection verified (Sheet 3 - WORM/crypto/tamper detection assessed)
- [ ] Retention compliance checked (Sheet 5 - all log categories assessed against policy)
- [ ] Privacy assessment complete (Sheet 7 - prohibited data check performed)
- [ ] Evidence collected (Sheet 10 - Evidence Register populated)
- [ ] Gap analysis complete (Sheet 9 - all gaps documented with remediation plans)

## Accuracy Checks

- [ ] Access control data current (Sheet 2 - user list from last 30 days)
- [ ] Integrity protection verified (Sheet 3 - WORM/crypto actually tested or configuration verified)
- [ ] Retention periods correct (Sheet 5 - matches policy Section 2.3 requirements)
- [ ] Disposal procedures documented (Sheet 6 - actual procedures, not theoretical)
- [ ] Privacy assessment realistic (Sheet 7 - log samples actually reviewed, not assumed)
- [ ] Legal hold inventory current (Sheet 8 - active holds confirmed with Legal)

## Compliance Alignment

- [ ] Policy references correct (all references to ISMS-POL-A.8.15 v1.0)
- [ ] Regulatory requirements identified (PCI DSS, HIPAA, SOX, GDPR per ISMS-POL-00)
- [ ] Separation of duties verified (Sheet 2 - system admins NOT log admins)
- [ ] Critical systems protected (Sheet 3 - critical systems have WORM or crypto signing)
- [ ] Retention compliance validated (Sheet 5 - all categories meet minimum retention)
- [ ] Privacy compliant (Sheet 7 - no prohibited data, GDPR principles met)

## Evidence Quality

- [ ] Evidence file naming clear and consistent
- [ ] Evidence contains date/time metadata
- [ ] Sensitive information redacted (GDPR compliance in evidence files)
- [ ] Evidence organized in folder structure (per section 5.2)
- [ ] Evidence Register (Sheet 10) complete (all evidence indexed)

## Approval Readiness

- [ ] Assessment completed by qualified personnel (InfoSec Manager, SIEM Admin, DPO)
- [ ] Cross-functional input obtained (IT Ops, Legal, DPO provided input)
- [ ] Review by DPO scheduled (privacy assessment requires DPO sign-off)
- [ ] Gaps socialized with stakeholders (no surprises in approval meeting)
- [ ] Remediation plans have buy-in (responsible parties aware and committed)

**If ANY checkbox unchecked**: Assessment NOT ready for approval. Complete missing items first.

---

# Review & Approval

## Three-Level Approval Process

**Level 1: Technical Review**

- **Reviewer**: Information Security Manager (primary) + SIEM Administrator
- **Focus**: Technical accuracy, protection mechanisms verified, retention configuration correct
- **Timeline**: 2-3 business days
- **Outcome**: Assessment technically accurate

**Level 2: Privacy & Compliance Review**

- **Reviewer**: Data Protection Officer (DPO) + Legal/Compliance Officer
- **Focus**: Privacy assessment accurate, retention justified, legal hold procedures adequate
- **Timeline**: 3-5 business days
- **Outcome**: Privacy and legal compliance validated

**Level 3: Executive Approval**

- **Reviewer**: CISO
- **Focus**: Strategic alignment, gap priorities, resource allocation for remediation
- **Timeline**: 1-2 weeks
- **Outcome**: Assessment approved, gaps authorized for remediation

## Approval Workflow

**Step 1: Assessment Completion**

- InfoSec Manager completes Sheets 2-6 (protection and retention)
- DPO completes Sheet 7 (privacy assessment)
- Legal completes Sheet 8 (legal hold management)
- Quality checklist (Section 7) fully verified

**Step 2: Level 1 Technical Review**

- InfoSec Manager self-review
- SIEM Administrator peer-review (technical accuracy)
- Corrections made
- Both sign Sheet 11

**Step 3: Level 2 Privacy & Compliance Review**

- DPO reviews privacy assessment (Sheet 7)
- Legal reviews retention periods (Sheet 5) and legal hold (Sheet 8)
- Privacy/legal issues resolved
- DPO and Legal sign Sheet 11

**Step 4: Level 3 Executive Approval**

- CISO reviews executive summary (Sheet 11)
- CISO reviews critical gaps (Sheet 9 - Critical/High priority)
- CISO approves remediation plans and resources
- CISO signs Sheet 11 as final approval

**Step 5: Post-Approval Actions**

- Assessment status updated to "Approved" (Sheet 11)
- Gaps entered into issue tracking (Jira, ServiceNow)
- Results included in quarterly compliance report
- Evidence archived for audit (7-year retention)

## Approval Timeline

**Typical Timeline**:

- Week 1-2: Assessment completion (InfoSec + DPO + Legal)
- Week 2-3: Level 1 Technical Review
- Week 3-4: Level 2 Privacy & Compliance Review (DPO + Legal)
- Week 4-5: Level 3 Executive Approval (CISO)

**Total**: 4-5 weeks from initiation to final approval

**Expedited Process** (if audit deadline):

- Concurrent reviews (DPO reviewing while Level 1 in progress)
- Focused on critical findings only
- Minimum 2-3 weeks

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook Developers (Python/Excel script maintainers)

---

# Document Overview

**Document ID:** ISMS-IMP-A.8.15.3  
**Assessment Area:** Log Protection, Integrity, Access Control & Retention Compliance  
**Related Policy:** ISMS-POL-A.8.15, Sections 2.2, 2.3, 2.5  
**Purpose:** Technical specification for Excel workbook structure and Python generation script  

---

# Workbook Structure Overview

| Sheet # | Sheet Name | Purpose | User Input Required | Formula-Driven | Protected |
|---------|------------|---------|-------------------|----------------|-----------|
| 1 | Instructions_Legend | Usage guide, scoring methodology | No | No | Yes (Read-Only) |
| 2 | Access_Control | User access verification, RBAC assessment | Yes | Yes (Compliance scoring) | Partial |
| 3 | Integrity_Protection | WORM, crypto, tamper protection assessment | Yes | Yes (Compliance scoring) | Partial |
| 4 | Tamper_Detection | Alert testing, integrity verification | Yes | Yes (Test pass/fail) | Partial |
| 5 | Retention_Compliance | Policy vs. actual retention per category | Yes | Yes (Compliance calculation) | Partial |
| 6 | Disposal_Procedures | Secure deletion verification | Yes | Yes (Compliance scoring) | Partial |
| 7 | Privacy_Assessment | GDPR/nDSG compliance, prohibited data check | Yes | Yes (Privacy compliance score) | Partial |
| 8 | Legal_Hold | Active holds, chain of custody | Yes | No | No (Input Area) |
| 9 | Gap_Analysis | Consolidated gaps with remediation | Partial | Yes (Auto-populated) | Partial |
| 10 | Evidence_Register | Evidence documentation index | Yes | No | No (Input Area) |
| 11 | Approval_Sign_Off | Three-level approval with summary | Yes | Yes (Summary metrics) | Partial |

**Total Sheets**: 11

---

# Sheet Specifications

## Sheet 1: Instructions_Legend

**Purpose**: Assessment methodology and scoring guide

**Key Sections**:

- Document information (ID, Version, Date, Organization, Assessment Period)
- Completion steps (8-step process)
- Scoring methodology (0-100% scale with color coding)
- Color coding guide (Yellow=Input, Blue=Formula, Green=Compliant, Red=Critical)

**Scoring Scale**:
| Score | Rating | Color | Meaning |
|-------|--------|-------|---------|
| 90-100% | Excellent | Green | Fully compliant |
| 75-89% | Good | Light Green | Substantially compliant |
| 50-74% | Adequate | Yellow | Partially compliant |
| 25-49% | Poor | Orange | Minimally compliant |
| 0-24% | Critical | Red | Non-compliant |

---

## Sheet 2: Access_Control

**Purpose**: Verify log access restricted to authorized personnel

**Column Structure** (15 columns):

- A: User ID / Service Account
- B: User Name
- C: Role (SOC Analyst, Security Engineer, InfoSec Manager, CISO, Auditor, System Admin, Other)
- D: Access Level (Read-Only, Read-Write, Admin, No Access)
- E: Access Scope (All Logs, Security Only, Specific Systems, Time-Limited)
- F: Business Justification (Why access needed)
- G: Last Access Date (From audit logs)
- H: Access Review Date (When last reviewed)
- I: Access Approved By (Who authorized)
- J: Separation of Duties Check - Formula: `=IF(C="System Admin","VIOLATION - SoD Breach","OK")`
- K: Access Appropriate - Formula: `=IF(OR(D="Read-Write",D="Admin",G<TODAY()-180),"Review Required","Appropriate")`
- L: Compliance Status - Formula: `=IF(AND(J="OK",K="Appropriate"),"Y Compliant","N Non-Compliant")`
- M: Gap Notes (If non-compliant, why?)
- N: Remediation Action (If non-compliant, what to do?)
- O: Target Date (When fixed)

**Compliance Calculations**:

- Total Users with Log Access = `COUNTA(A:A) - 1` (exclude header)
- Access Justified = `COUNTIF(F:F,"<>")` (has justification)
- Separation of Duties Compliant = `COUNTIF(J:J,"OK")/Total*100`
- Access Appropriate = `COUNTIF(K:K,"Appropriate")/Total*100`
- **Overall Access Control Compliance** = `COUNTIF(L:L,"Y Compliant")/Total*100`

**Conditional Formatting**:

- Column J (SoD Check): Red fill if "VIOLATION", Green if "OK"
- Column K (Appropriateness): Yellow if "Review Required", Green if "Appropriate"
- Column L (Compliance): Green if "Y", Red if "N"

---

## Sheet 3: Integrity_Protection

**Purpose**: Verify logs protected from tampering

**Section 1: Storage Tier Protection** (Rows 4-30):

Columns:

- A: Storage Tier (Hot, Warm, Cold)
- B: Storage System Name
- C: WORM Enabled (Yes, No, Partial, N/A)
- D: WORM Technology (Hardware WORM, Software WORM, Object Lock, Tape, N/A)
- E: Cryptographic Protection (Digital Signatures, Hashing, Hash Chain, None)
- F: Algorithm Used (SHA-256, SHA-3, RSA-2048, Ed25519, None)
- G: Access Control (Write-Protected? Yes/No)
- H: Centralized Collection (Immediate Forwarding? Yes/No/Partial)
- I: Compliance Status - Formula: `=IF(OR(C="Yes",AND(E<>"None",F<>"None")),"Y Protected","N Not Protected")`

**Section 2: Critical Systems Enhanced Protection** (Rows 33-60):

Columns:

- A: System ID (from IMP-A.8.15.1)
- B: System Name
- C: System Criticality (from IMP-A.8.15.1 - filter for "Critical" only)
- D: Log Storage Tier (Which tier are these logs in?)
- E: Protection Method (WORM, Digital Signature, Hash Chain, Centralized Only, None)
- F: Policy Requirement Met - Formula: `=IF(OR(E="WORM",E="Digital Signature",E="Hash Chain"),"Y Yes","N No")`
- G: Gap Identified - Formula: `=IF(F="N No","GAP: Critical system requires WORM or crypto signing","")`

**Compliance Calculations**:

- Total Storage Tiers = `COUNTA(Section1!A:A)`
- Tiers Protected = `COUNTIF(Section1!I:I,"Y Protected")`
- Storage Tier Protection % = `(Tiers Protected / Total Tiers) * 100`
- Total Critical Systems = `COUNTA(Section2!A:A)`
- Critical Systems Protected = `COUNTIF(Section2!F:F,"Y Yes")`
- Critical System Protection % = `(Protected / Total) * 100`
- **Overall Integrity Protection Score** = `AVERAGE(Storage Tier %, Critical System %)`

---

## Sheet 4: Tamper_Detection

**Purpose**: Verify tamper detection operational

**Column Structure** (12 columns):

- A: Test Scenario (Log Modification, Log Deletion, Integrity Verification, Alert Generation)
- B: Test Environment (Production, Staging, Test, Not Tested)
- C: Test Date
- D: Test Conducted By
- E: Test Procedure (Brief description of what was tested)
- F: Expected Result (What should happen)
- G: Actual Result (What actually happened)
- H: Test Pass/Fail - Formula: `=IF(G=F,"Y PASS","N FAIL")`
- I: Alert Generated (Yes, No, N/A)
- J: Alert Destination (SOC Email, SIEM Alert, Ticketing System, N/A)
- K: Response Procedure Documented (Yes, No)
- L: Overall Status - Formula: `=IF(AND(H="Y PASS",OR(I="Yes",I="N/A"),K="Yes"),"Y Compliant","N Non-Compliant")`

**Summary Section**:

- Total Tests = `COUNTA(A:A) - 1`
- Tests Passed = `COUNTIF(H:H,"Y PASS")`
- Tests Failed = `COUNTIF(H:H,"N FAIL")`
- Alerts Configured = `COUNTIF(I:I,"Yes")`
- Response Procedures Documented = `COUNTIF(K:K,"Yes")`
- **Tamper Detection Effectiveness Score** = `(Tests Passed / Total Tests) * 100`

**Conditional Formatting**:

- Column H: Green if "Y PASS", Red if "N FAIL"
- Column L: Green if "Y Compliant", Red if "N Non-Compliant"

---

## Sheet 5: Retention_Compliance

**Purpose**: Validate actual vs. policy retention requirements

**Column Structure** (13 columns):

- A: Log Category (Security Events, Authentication, Admin Actions, Database Logs, Application Logs, Network Logs, System Logs)
- B: Policy Requirement - Online (months, from ISMS-POL-A.8.15 Section 2.3)
- C: Policy Requirement - Archive (years total, from policy)
- D: Regulatory Driver (ISO 27001, GDPR, PCI DSS, HIPAA, SOX, nDSG)
- E: Actual - Hot Storage (months, from IMP-A.8.15.2 Sheet 3 if available)
- F: Actual - Warm Storage (months)
- G: Actual - Cold Archive (years)
- H: Total Actual Retention - Formula: `=E+F+(G*12)` (convert to months)
- I: Total Required Retention - Formula: `=B+(C*12)` (convert to months)
- J: Compliance Status - Formula: `=IF(H>=I,"Y Compliant","N Non-Compliant")`
- K: Gap (if non-compliant) - Formula: `=IF(J="N Non-Compliant",I-H,0)` (months short)
- L: Over-Retention (privacy risk) - Formula: `=IF(AND(J="Y Compliant",H>I+24),H-I,0)` (months over)
- M: Justification (If over-retained, why? Business need, legal hold, other)

**Regulatory-Specific Section** (Below main table):

| Regulation | Applicable? | Log Types Affected | Minimum Retention | Actual Retention | Compliant? |
|-----------|-------------|-------------------|-------------------|------------------|------------|
| PCI DSS 10.5.1 | [Y/N] | Payment system logs | 12 months online | [From Sheet] | `=IF(Actual>=12,"Y","N")` |
| HIPAA Sec.164.316 | [Y/N] | ePHI access logs | 6 years total | [From Sheet] | `=IF(Actual>=72,"Y","N")` |
| SOX | [Y/N] | Financial audit trails | 7 years total | [From Sheet] | `=IF(Actual>=84,"Y","N")` |

**Compliance Summary**:

- Total Categories = `COUNTA(A:A) - 1`
- Categories Compliant = `COUNTIF(J:J,"Y Compliant")`
- Categories Non-Compliant = `COUNTIF(J:J,"N Non-Compliant")`
- Categories Over-Retained = `COUNTIF(L:L,">0")`
- **Overall Retention Compliance %** = `(Compliant / Total) * 100`

**Conditional Formatting**:

- Column J: Green if "Y Compliant", Red if "N Non-Compliant"
- Column L: Orange fill if >0 (over-retention privacy risk)

---

## Sheet 6: Disposal_Procedures

**Purpose**: Verify secure log disposal implementation

**Column Structure** (11 columns):

- A: Storage Tier (Hot, Warm, Cold)
- B: Disposal Method (Automated Deletion, Manual Deletion, Crypto Erasure, Physical Destruction, None)
- C: Disposal Trigger (Automated After Retention, Scheduled Quarterly, On-Demand Manual, Never)
- D: NIST SP 800-88 Compliant (Yes, No, Unknown)
- E: Disposal Logged (Yes, No)
- F: Legal Hold Check (Pre-Disposal Check? Yes/No)
- G: Disposal Verification (How verified? Audit logs, Capacity monitoring, Manual inspection)
- H: Last Disposal Date (When last disposal occurred)
- I: Disposal Volume (GB or TB disposed)
- J: Disposal Records Retained (Yes, No)
- K: Compliance Status - Formula: `=IF(AND(B<>"None",D="Yes",E="Yes",F="Yes"),"Y Compliant","N Non-Compliant")`

**Summary Section**:

- Total Storage Tiers = `COUNTA(A:A) - 1`
- Tiers with Disposal Process = `COUNTIF(B:B,"<>None")`
- NIST Compliant Disposal = `COUNTIF(D:D,"Yes")`
- Disposal Logged = `COUNTIF(E:E,"Yes")`
- Legal Hold Check Implemented = `COUNTIF(F:F,"Yes")`
- **Overall Disposal Compliance %** = `COUNTIF(K:K,"Y Compliant") / Total * 100`

**Conditional Formatting**:

- Column B: Red if "None" (no disposal = gap)
- Column K: Green if "Y Compliant", Red if "N Non-Compliant"

---

## Sheet 7: Privacy_Assessment

**Purpose**: GDPR/nDSG compliance verification

**Section 1: Data Minimization** (Rows 4-20):

Columns:

- A: Log Category
- B: Personal Data Present (Yes/No)
- C: Personal Data Types (User IDs, IP addresses, Email, Location, Other)
- D: Data Necessary (Yes/No - is all logged data necessary?)
- E: Minimization Compliant - Formula: `=IF(OR(B="No",D="Yes"),"Y Yes","N No")`

**Section 2: Prohibited Data Check** (Rows 23-35):

| Prohibited Data Type | Found in Logs? | Where Found? | Remediation Required? | Remediation Plan | Target Date |
|---------------------|----------------|--------------|---------------------|------------------|-------------|
| Passwords (cleartext) | [Y/N] | [Log source] | [Y/N] | [Action] | [Date] |
| Full credit card numbers | [Y/N] | [Log source] | [Y/N] | [Action] | [Date] |
| National ID numbers | [Y/N] | [Log source] | [Y/N] | [Action] | [Date] |
| Full health information | [Y/N] | [Log source] | [Y/N] | [Action] | [Date] |
| Biometric templates | [Y/N] | [Log source] | [Y/N] | [Action] | [Date] |
| Session tokens/API keys | [Y/N] | [Log source] | [Y/N] | [Action] | [Date] |

**Prohibited Data Compliance** = `=IF(COUNTIF(B23:B35,"Yes")=0,"Y No Prohibited Data","N VIOLATION - Prohibited Data Found")`

**Section 3: GDPR Compliance Checklist** (Rows 38-50):

| GDPR Article | Requirement | Compliant? | Evidence | Gap Notes |
|--------------|-------------|------------|----------|-----------|
| Art. 5(1)(c) - Data Minimization | Log only necessary data | [Y/N] | [Evidence ref] | [Notes] |
| Art. 5(1)(b) - Purpose Limitation | Use logs only for security/compliance | [Y/N] | [Evidence ref] | [Notes] |
| Art. 5(1)(e) - Storage Limitation | Retention justified | [Y/N] | [Evidence ref] | [Notes] |
| Art. 32 - Security | Logs protected (integrity, access control) | [Y/N] | [Evidence ref] | [Notes] |
| Transparency | Users informed of logging | [Y/N] | [Evidence ref] | [Notes] |

**Privacy Compliance Score** = `COUNTIF(C38:C50,"Yes") / 5 * 100`

---

## Sheet 8: Legal_Hold

**Purpose**: Legal hold management verification

**Active Holds Inventory** (if any):

Columns:

- A: Hold ID
- B: Hold Initiation Date
- C: Hold Requestor (Legal counsel, case ref)
- D: Scope - Log Categories Affected
- E: Scope - Time Period (date range)
- F: Scope - Systems Affected
- G: Hold Status (Active, Released, Partial)
- H: Estimated Duration
- I: Hold Documentation Location
- J: Chain of Custody Maintained (Yes/No)
- K: Disposal Suspended Verified (Yes/No)
- L: Last Review Date
- M: Notes

**Legal Hold Process Assessment**:

| Process Element | Implemented? | Documented? | Tested? | Compliance Status |
|-----------------|--------------|-------------|---------|-------------------|
| Hold notification process | [Y/N] | [Y/N] | [Y/N] | Formula: `=IF(AND(B,C,D),"Y","N")` |
| Disposal suspension | [Y/N] | [Y/N] | [Y/N] | Formula |
| Chain of custody | [Y/N] | [Y/N] | [Y/N] | Formula |
| Quarterly reviews | [Y/N] | [Y/N] | [Y/N] | Formula |
| Hold release process | [Y/N] | [Y/N] | [Y/N] | Formula |

**Legal Hold Compliance Score** = `COUNTIF(E:E,"Y") / 5 * 100`

---

## Sheet 9: Gap_Analysis

**Purpose**: Consolidated gaps with remediation tracking

**Column Structure** (20 columns):

- A: Gap ID (PROT-001, PROT-002...)
- B: Gap Category (Access Control, Integrity Protection, Tamper Detection, Retention, Disposal, Privacy, Legal Hold)
- C: Gap Description
- D: Affected System/Process
- E: Source Sheet (2-8)
- F: Policy Reference (ISMS-POL-A.8.15 Section X.X)
- G: Impact Level (High, Medium, Low)
- H: Likelihood (Likely, Possible, Unlikely)
- I: Risk Rating - Formula: Risk matrix from IMP-A.8.15.2
- J: Business Impact
- K: Proposed Solution
- L: Responsible Party
- M: Target Completion Date
- N: Estimated Effort (Hours)
- O: Budget Required
- P: Compensating Controls
- Q: Exception ID (if approved exception exists)
- R: Status (Open, In Progress, Resolved, Accepted, Deferred)
- S: Tracking Ticket ID
- T: Notes

**Auto-Population from Other Sheets**:

- FROM Sheet 2: WHERE Compliance Status = "N Non-Compliant"
- FROM Sheet 3: WHERE Integrity Protection = "N Not Protected" AND Critical System
- FROM Sheet 5: WHERE Retention Compliance = "N Non-Compliant"
- FROM Sheet 7: WHERE Prohibited Data Found = "Yes"

**Summary by Category**:
| Category | Total | Critical | High | Medium | Low |
|----------|-------|----------|------|--------|-----|
| Access Control | COUNT | COUNTIFS(I,"CRITICAL") | ... | ... | ... |
| Integrity Protection | COUNT | ... | ... | ... | ... |
| Retention | COUNT | ... | ... | ... | ... |
| Privacy | COUNT | ... | ... | ... | ... |

---

## Sheet 10: Evidence_Register

**Purpose**: Evidence documentation index

**Columns** (12 columns):

- A: Evidence ID (EV-PROT-001...)
- B: Evidence Type (Screenshot, Config Export, Report, Document, Test Result)
- C: Description
- D: Related Sheet (2-8)
- E: Related System/Topic
- F: File Name
- G: File Location (folder path)
- H: Date Collected
- I: Collected By
- J: Sensitivity (Public, Internal, Confidential, Restricted)
- K: Retention Period (7 years)
- L: Notes

---

## Sheet 11: Approval_Sign_Off

**Purpose**: Three-level approval with summary dashboard

**Summary Metrics** (Rows 5-20):

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Access Control Compliance % | =Sheet2!Summary | 100% | IF check |
| Integrity Protection Score | =Sheet3!Summary | >=95% | IF check |
| Tamper Detection Effectiveness | =Sheet4!Summary | 100% | IF check |
| Retention Compliance % | =Sheet5!Summary | 100% | IF check |
| Disposal Compliance % | =Sheet6!Summary | 100% | IF check |
| Privacy Compliance Score | =Sheet7!Summary | 100% | IF check |
| Legal Hold Compliance | =Sheet8!Summary | 100% | IF check |
| **Overall Compliance Score** | =AVERAGE(All) | **>=90%** | Color code |

**Gap Summary**:

- Total Gaps = COUNT(Sheet9!A:A)
- Critical = COUNTIF(Sheet9!I:I,"CRITICAL")
- High = COUNTIF(Sheet9!I:I,"HIGH")

**Approval Sections**:

- Level 1: InfoSec Manager + SIEM Admin
- Level 2: DPO + Legal/Compliance
- Level 3: CISO

---

# Integration Points

## Referenced Documents

**From IMP-A.8.15.1**:

- Critical systems list (for Sheet 3 enhanced protection requirement)

**From IMP-A.8.15.2**:

- Sheet 3 (Storage Architecture) for actual retention periods (referenced in Sheet 5)

**To IMP-A.8.15.5**:

- Sheet 11 (Approval Sign-Off) summary metrics for dashboard

## Policy References

- ISMS-POL-A.8.15 Section 2.2 (Log Protection & Integrity)
- ISMS-POL-A.8.15 Section 2.3 (Log Retention & Storage)
- ISMS-POL-A.8.15 Section 2.5 (Privacy & Data Protection)
- ISMS-POL-A.8.15 Section 3.3 (Exception Management)
- ISMS-POL-00 (Regulatory Applicability Framework)

---

# Python Script Usage

## Script Name
`generate_a815_3_log_protection_retention.py`

## Critical Customization Points

**Line 20-30: Organization-Specific Defaults**
```python
# CUSTOMIZE: Organization defaults
DEFAULT_ORG_NAME = "[Organization]"
DEFAULT_ASSESSMENT_PERIOD = "Semi-Annual 2026-H1"
```

**Line 100-120: Regulatory Applicability**
```python
# CUSTOMIZE: Which regulations apply to your organization
APPLICABLE_REGULATIONS = {
    'PCI_DSS': False,  # Set True if processing payment cards
    'HIPAA': False,    # Set True if US healthcare data
    'SOX': False,      # Set True if publicly traded company
    'GDPR': True,      # Set True if processing EU personal data
    'nDSG': True       # Set True for Swiss operations
}
```

**Line 200-250: Retention Requirements Matrix**
```python
# CUSTOMIZE: Based on policy Section 2.3 and ISMS-POL-00
RETENTION_REQUIREMENTS = {
    'Security Events': {'online': 12, 'archive': 7, 'driver': 'ISO 27001'},
    'Authentication': {'online': 12, 'archive': 7, 'driver': 'ISO 27001'},
    # ... add all categories from policy
}
```

## Key Functions

1. `create_workbook()`: Initialize 11-sheet structure
2. `populate_access_control()`: Sheet 2 with user list template
3. `populate_integrity_protection()`: Sheet 3 with storage tiers
4. `generate_retention_matrix()`: Sheet 5 with policy requirements pre-filled
5. `populate_privacy_checklist()`: Sheet 7 with GDPR checklist
6. `apply_conditional_formatting()`: All traffic lights and risk colors
7. `set_data_validation()`: Dropdowns for all required fields
8. `protect_cells()`: Lock formula cells, allow input cells

## Testing Checklist

- [ ] All formulas calculate correctly
- [ ] Conditional formatting triggers properly
- [ ] Dropdowns contain correct values
- [ ] Risk matrix works (Sheet 9)
- [ ] Summary metrics aggregate correctly (Sheet 11)
- [ ] Cell protection appropriate

---

# Document Assembly Complete

**Total Document Length**: ~1,600 lines

**Structure**:

- Part I: User Completion Guide (~800 lines)
- Part II: Technical Specification (~800 lines)

**Quality Verification**:

- [X] Policy references to ISMS-POL-A.8.15 v1.0 consolidated policy
- [X] Privacy assessment (GDPR/nDSG) comprehensive
- [X] Retention compliance validation per policy Section 2.3
- [X] Legal hold management included
- [X] All 11 sheets specified with formulas, validation, formatting
- [X] Completely generic language (no industry/size/technology assumptions)
- [X] Follows IMP-A.8.15.1 and IMP-A.8.15.2 structure exactly

---

**END OF SPECIFICATION**

---

*"Information is not knowledge. The only source of knowledge is experience."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-01 -->

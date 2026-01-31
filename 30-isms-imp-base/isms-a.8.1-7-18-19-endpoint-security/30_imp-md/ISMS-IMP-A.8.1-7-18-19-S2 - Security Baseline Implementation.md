# ISMS-IMP-A.8.1-7-18-19-S2 - Security Baseline Implementation
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Controls A.8.1, A.8.7, A.8.18, A.8.19: Endpoint Security Framework

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S2 |
| **Version** | 1.0 |
| **Assessment Area** | Security Baseline Compliance and Enforcement |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.1.3 (Security Baselines), Section 2.1.4 (Encryption), Section 2.1.5 (Endpoint Management) |
| **Purpose** | Document security baseline configurations per endpoint type, assess baseline compliance, verify encryption status, and identify configuration drift to support endpoint device security requirements |
| **Target Audience** | Endpoint Administrators, Security Engineers, IT Operations, Compliance Officers, Configuration Managers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Weekly (automated compliance scans), Monthly (manual review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for security baseline assessment | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Sheet-by-Sheet Completion Guide
  - Evidence Collection
  - Common Pitfalls (10 Mistakes)
  - Quality Checklist (50+ Items)
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Instructions for Workbook Developers
  - Common Column Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Appendix: Technical Notes for Python Developers

---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.1-7-18-19-S2 - Security Baseline Implementation

#### What This Assessment Covers

This assessment documents security BASELINES applied to endpoints and verifies COMPLIANCE with those baselines. This is the critical "ARE endpoints properly configured?" assessment that answers:

- What security baselines are defined? (Windows, macOS, Linux, iOS, Android)
- Are baselines applied to all endpoints? (via GPO, MDM profiles, configuration management)
- Is baseline compliance being monitored? (weekly scans, configuration drift detection)
- Is encryption properly deployed? (full disk encryption, key escrow, container encryption)
- Are endpoints enrolled in management platforms? (MDM, domain join, cloud managed)
- What configuration drift exists? (deviations from approved baselines)

#### Key Principle

**Security baselines are meaningless without compliance verification.** Having a Windows security baseline document is worthless if you don't verify endpoints actually comply with it. This assessment forces honest measurement of baseline compliance rates.

**Target Compliance:** ≥90% baseline compliance across all endpoints

#### What You'll Document

- **Baseline_Inventory** (Baseline_Inventory worksheet): All security baselines defined (Windows, macOS, Linux, iOS, Android, custom)
- **Compliance_Status** (Compliance_Status worksheet): Per-endpoint baseline compliance assessment
- **Encryption_Status** (Encryption_Status worksheet): Encryption verification (FDE, container, key escrow)
- **Management_Enrollment** (Management_Enrollment worksheet): MDM/agent enrollment status per endpoint
- **Configuration_Drift** (Configuration_Drift worksheet): Detected configuration deviations from baselines
- **Gaps** (Gaps worksheet): Non-compliant endpoints and remediation plans

#### How This Relates to Other A.8.1-7-18-19 Assessments

| Assessment | Focus | Relationship to S2 |
|------------|-------|-------------------|
| ISMS-IMP-A.8.1-7-18-19-S1 | Endpoint Discovery | S1 discovers endpoints, S2 assesses their security configurations |
| **ISMS-IMP-A.8.1-7-18-19-S2** | **Security Baselines** | **Verifies endpoints meet security configuration requirements** |
| ISMS-IMP-A.8.1-7-18-19-S3 | Malware Protection | S3 verifies anti-malware (one component of S2 baseline) |
| ISMS-IMP-A.8.1-7-18-19-S4 | Software Controls | S4 verifies application control (one component of S2 baseline) |
| ISMS-IMP-A.8.1-7-18-19-S5 | Privileged Utilities | S5 monitors privileged tools (restricted by S2 baseline) |
| ISMS-IMP-A.8.1-7-18-19-S6 | Assessment & Compliance | S6 consolidates S2 compliance data with other controls |

This assessment (S2) verifies that discovered endpoints (S1) have proper security configurations before assessing specific security controls (S3-S5).

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Endpoint Administrators** - GPO management, MDM profile deployment, baseline enforcement
2. **Security Engineers** - Baseline definition, compliance monitoring, drift detection
3. **IT Operations** - Configuration management (Ansible, Puppet, Chef), agent deployment
4. **Compliance Officers** - Audit readiness, regulatory compliance verification
5. **Encryption Administrators** - Encryption deployment, key escrow management

#### Required Skills

- Understanding of security hardening concepts (CIS Benchmarks, vendor security guides)
- Familiarity with endpoint management platforms (Intune, Jamf, SCCM, etc.)
- Knowledge of Group Policy (Windows), configuration profiles (macOS/iOS), configuration management (Linux)
- Encryption technology knowledge (BitLocker, FileVault, LUKS, mobile encryption)
- Compliance scanning tools (Microsoft Defender for Endpoint, Jamf Compliance, third-party scanners)

#### Time Commitment

- **Initial baseline definition:** 40-80 hours (depends on OS diversity and baseline complexity)
- **Initial compliance assessment:** 10-20 hours (automated scans + manual verification)
- **Weekly updates:** 2-4 hours (automated scan review, drift investigation)
- **Monthly review:** 4-8 hours (compliance reporting, gap remediation tracking)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Documented security baselines** - Windows, macOS, Linux, iOS, Android baselines defined
2. ✅ **Baseline compliance assessment** - Per-endpoint compliance scores (≥90% target)
3. ✅ **Encryption verification** - All corporate endpoints encryption status verified (≥98% target)
4. ✅ **Management enrollment verification** - MDM/agent enrollment verified (≥98% target)
5. ✅ **Configuration drift identification** - Deviations from baselines detected and documented
6. ✅ **Gap remediation plans** - Non-compliant endpoints with remediation owners and target dates
7. ✅ **Evidence register** - Baseline documents, GPO exports, MDM profiles, compliance scan results
8. ✅ **Approved assessment** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Baseline Documentation

- **Windows Security Baseline**: Microsoft Security Baseline for Windows 10/11, CIS Benchmark Level 1
- **macOS Security Baseline**: Apple Platform Security Guide, CIS Benchmark for macOS
- **Linux Security Baseline**: CIS Benchmark for specific distribution (Ubuntu, RHEL, etc.)
- **iOS/Android Security Baseline**: Apple iOS Configuration, Android Enterprise security guidelines
- **Industry-Specific Baselines**: NIST SP 800-53, DISA STIGs (if applicable)

#### 2. System Access

- **Group Policy Management**: Access to GPO creation/editing (Windows)
- **MDM Platform Access**: Administrator access to Intune, Jamf, SCCM, Google Workspace MDM, etc.
- **Configuration Management**: Access to Ansible, Puppet, Chef (for Linux baselines)
- **Compliance Scanning Tools**: Access to Microsoft Defender for Endpoint, Jamf Compliance, Tenable, Qualys, etc.
- **Encryption Management**: Access to BitLocker management (MBAM, Intune), FileVault key escrow (Jamf), etc.

#### 3. Documentation

- Endpoint inventory from S1 (prerequisite: ISMS-IMP-A.8.1-7-18-19-S1 must be complete)
- Current GPO structure and documentation
- MDM configuration profile inventory
- Encryption deployment status reports

#### 4. Tools & Software

- **Compliance Scanning Tools**: Microsoft Defender for Endpoint, Jamf Pro, SCAP scanners, OpenSCAP, etc.
- **PowerShell/Bash/Python**: For scripting and automation
- **Excel Workbook**: Baseline_Compliance.xlsx (generated by generate_a817_2_security_baseline.py script)

#### 5. Approvals & Authorizations

- **Baseline Approval**: Security baselines approved by CISO (before enforcement)
- **Compliance Scanning Authorization**: Permission to run automated compliance scans
- **Encryption Deployment Approval**: Authorization for full disk encryption rollout

---

## Assessment Workflow

### High-Level Process

The security baseline assessment follows a **six-phase approach**:

```
Phase 1: Baseline Definition & Documentation
   ↓
Phase 2: Baseline Deployment (GPO, MDM, Config Mgmt)
   ↓
Phase 3: Compliance Scanning (Automated + Manual)
   ↓
Phase 4: Encryption Verification
   ↓
Phase 5: Configuration Drift Detection
   ↓
Phase 6: Gap Remediation & Ongoing Monitoring
```

**Estimated Timeline**: 4-8 weeks for initial deployment and assessment

### Detailed Workflow Steps

#### Phase 1: Baseline Definition & Documentation (1-2 weeks)

**Activities:**
1. Select appropriate baseline sources (Microsoft, Apple, CIS Benchmarks)
2. Document baseline requirements per endpoint type (Windows, macOS, Linux, mobile)
3. Customize baselines for organizational requirements (add/remove controls)
4. Obtain CISO approval for baselines before deployment
5. Document baseline rationale (why each control required)

**Deliverable:** Approved security baseline documents for each endpoint OS

#### Phase 2: Baseline Deployment (2-4 weeks)

**Activities:**
1. **Windows**: Create GPOs or Intune configuration profiles implementing baseline
2. **macOS**: Create Jamf configuration profiles or Intune profiles
3. **Linux**: Create Ansible playbooks, Puppet manifests, or Chef recipes
4. **Mobile**: Create MDM configuration profiles (iOS, Android)
5. Pilot baseline deployment to test group (1 week)
6. Phased rollout to production endpoints (1-3 weeks depending on scope)

**Deliverable:** Baselines deployed to ≥95% of endpoints

#### Phase 3: Compliance Scanning (1 week)

**Activities:**
1. **Automated Scanning**: Run compliance scans via Microsoft Defender, Jamf, SCAP scanners
2. **Manual Verification**: Spot-check random sample (20 endpoints per OS) for accuracy
3. **Data Collection**: Export compliance scan results to CSV/Excel
4. **Import to Workbook**: Populate Baseline_Compliance.xlsx with scan results
5. **Calculate Compliance Scores**: Per-endpoint compliance percentage

**Deliverable:** Complete compliance assessment data in Baseline_Compliance.xlsx

#### Phase 4: Encryption Verification (2-3 days)

**Activities:**
1. **Windows BitLocker**: Verify encryption status via Intune, MBAM, or AD
2. **macOS FileVault**: Verify encryption status via Jamf, Intune, or recovery key escrow
3. **Linux LUKS**: Verify encryption status via configuration management or manual check
4. **Mobile Encryption**: Verify device encryption via MDM compliance policies
5. **Key Escrow Verification**: Confirm recovery keys escrowed for corporate devices

**Deliverable:** Encryption status verified for all corporate laptops/desktops/mobile

#### Phase 5: Configuration Drift Detection (Ongoing)

**Activities:**
1. **Weekly Drift Scans**: Automated scanning detects configuration changes
2. **Drift Investigation**: Determine root cause (user modification, software update, policy conflict)
3. **Automatic Remediation**: Re-apply baseline configurations where possible
4. **Manual Remediation**: Fix drift that cannot be auto-remediated within 7 days

**Deliverable:** Configuration drift tracked and remediated

#### Phase 6: Gap Remediation & Ongoing Monitoring (Continuous)

**Activities:**
1. **Gap Identification**: Identify non-compliant endpoints from compliance scans
2. **Gap Prioritization**: Prioritize by criticality (critical endpoints first)
3. **Remediation Planning**: Assign owners, set target dates
4. **Remediation Execution**: Fix non-compliance issues
5. **Verification**: Re-scan after remediation to verify compliance
6. **Ongoing Monitoring**: Weekly compliance scans, monthly compliance reporting

**Deliverable:** ≥90% baseline compliance maintained, gaps remediated within SLA

---

## Sheet-by-Sheet Completion Guide

### Sheet 1: Baseline_Inventory

**Purpose:** Document all security baselines defined

**Completion Steps:**

1. **For Each Baseline (Windows, macOS, Linux, iOS, Android, custom):**
   - **Baseline_Name**: Name of baseline (e.g., "Windows 11 Corporate Baseline")
   - **Platform**: Operating system (Windows 11, macOS 14, Ubuntu 22.04, iOS 17, Android 13)
   - **Baseline_Source**: Source document (Microsoft Security Baseline, CIS Benchmark Level 1, Apple Platform Security Guide)
   - **Version**: Baseline version (e.g., "CIS Windows 11 Benchmark v2.0.0")
   - **Approval_Date**: Date baseline approved by CISO
   - **Approval_Authority**: Who approved (CISO, Security Committee)
   - **Enforcement_Method**: How baseline applied (GPO, Intune Profile, Jamf Profile, Ansible)
   - **Control_Count**: Number of security controls in baseline
   - **Applicable_Endpoints**: Which endpoints use this baseline (All Windows 11 corporate laptops/desktops)

2. **Document Baseline Controls** (sample - not exhaustive):
   - Firewall enabled (all network profiles)
   - Automatic updates enabled
   - Password complexity (≥12 chars, complexity)
   - Screen lock timeout (≤15 minutes idle)
   - Full disk encryption enabled
   - Anti-malware installed and enabled
   - Application control (AppLocker, Gatekeeper, etc.)
   - Audit logging enabled
   - Remote Desktop disabled (or restricted)
   - Unnecessary services disabled

3. **Baseline Customization Notes:**
   - Document deviations from baseline source (controls added/removed)
   - Rationale for customization (business requirement, technical limitation)

**Quality Target:** All endpoint OS types have documented, approved baselines

### Sheet 2: Compliance_Status

**Purpose:** Per-endpoint baseline compliance assessment

**Completion Steps:**

1. **Import Endpoint Inventory** (from S1):
   - Device_ID, Hostname, Device_Type, Operating_System, Ownership_Model, Criticality

2. **Run Compliance Scans:**
   - **Windows**: Microsoft Defender for Endpoint compliance scans, Intune compliance policies
   - **macOS**: Jamf Pro compliance policies, Intune compliance policies
   - **Linux**: OpenSCAP scans, Ansible compliance checks, manual verification
   - **Mobile**: MDM compliance policies (Intune, Jamf, Google Workspace)

3. **Populate Compliance Data** (for each endpoint):
   - **Baseline_Applied**: Which baseline applied (Windows 11 Corporate, macOS 14 Corporate, etc.)
   - **Compliance_Scan_Date**: Date of last compliance scan
   - **Total_Controls**: Total security controls in applicable baseline
   - **Compliant_Controls**: Number of controls endpoint complies with
   - **Non_Compliant_Controls**: Number of controls endpoint fails
   - **Compliance_Percentage**: (Compliant / Total) × 100%
   - **Compliance_Status**: 🟢 Green (≥90%), 🟡 Yellow (70-89%), 🔴 Red (<70%)
   - **Top_Failures**: Top 3 failed controls (most common issues)

4. **Manual Spot-Check Validation:**
   - Select random sample (20 endpoints per OS type)
   - Manually verify compliance scan accuracy
   - Document spot-check results in Notes column

**Quality Target:** ≥90% endpoints in Green status, compliance scans current (≤7 days old)

### Sheet 3: Encryption_Status

**Purpose:** Verify endpoint encryption status and key escrow

**Completion Steps:**

1. **For Each Corporate Laptop/Desktop:**
   - **Encryption_Required**: Yes/No (based on policy - corporate laptops/desktops = Yes)
   - **Encryption_Technology**: BitLocker, FileVault, LUKS, Third-Party (Symantec, etc.)
   - **Encryption_Status**: Enabled, Disabled, Not Supported
   - **Encryption_Algorithm**: AES-256, AES-128, etc.
   - **Pre_Boot_Auth**: Enabled (password/PIN required), Disabled, TPM-Only
   - **Key_Escrow_Required**: Yes (corporate), No (BYOD - privacy)
   - **Key_Escrow_Status**: Escrowed, Not Escrowed, N/A
   - **Key_Escrow_Location**: Active Directory, Intune, Jamf, MBAM, Key Management System
   - **Verification_Date**: Date encryption status verified
   - **Encryption_Compliance**: 🟢 Compliant, 🔴 Non-Compliant

2. **For Each Mobile Device:**
   - **Device_Encryption**: Enabled (built-in iOS/Android), Disabled
   - **Container_Encryption**: Enabled (for BYOD - corporate container encrypted), N/A
   - **Encryption_Compliance**: 🟢 Compliant, 🔴 Non-Compliant

3. **Exceptions:**
   - **Exception_Reason**: Desktop in secure facility, legacy hardware incompatible, etc.
   - **Exception_Approved_By**: CISO (required for encryption exceptions)
   - **Exception_Approval_Date**: Date exception approved
   - **Compensating_Controls**: No sensitive data storage, enhanced physical security, etc.

**Quality Target:** ≥98% encryption coverage (corporate laptops/desktops), 100% key escrow for encrypted corporate devices

### Sheet 4: Management_Enrollment

**Purpose:** Verify endpoint management platform enrollment

**Completion Steps:**

1. **For Each Endpoint:**
   - **Management_Required**: Yes (corporate), MAM Only (BYOD), No (guest)
   - **Management_Platform**: Intune, Jamf Pro, SCCM, Google Workspace MDM, VMware Workspace ONE, etc.
   - **Enrollment_Status**: Enrolled, Not Enrolled, Enrollment Failed
   - **Enrollment_Date**: Date device enrolled
   - **Last_Check_In**: Date/time of last management platform check-in
   - **Agent_Version**: Management agent version (if agent-based)
   - **Agent_Status**: Running, Stopped, Not Installed
   - **Management_Capabilities**: Full MDM, MAM Only, Domain Joined, Cloud Managed
   - **Enrollment_Compliance**: 🟢 Compliant, 🔴 Non-Compliant

2. **Stale Management Status:**
   - Flag endpoints not checked in >7 days (🟡 Yellow)
   - Flag endpoints not checked in >30 days (🔴 Red - likely lost/stolen/disposed)

3. **BYOD Enrollment:**
   - **BYOD_Enrollment_Type**: MAM (Mobile App Management - container only)
   - **User_Consent**: Documented (required for BYOD)
   - **Privacy_Notice_Provided**: Yes/No (required for BYOD)

**Quality Target:** ≥98% enrollment (corporate endpoints), ≥80% enrollment (BYOD), <5% stale check-ins

### Sheet 5: Configuration_Drift

**Purpose:** Track configuration deviations from approved baselines

**Completion Steps:**

1. **Drift Detection:**
   - Run weekly compliance scans
   - Compare current configuration vs. approved baseline
   - Identify configuration changes (manual user changes, software updates, policy conflicts)

2. **For Each Drift Incident:**
   - **Drift_ID**: Unique identifier (DRIFT-001, DRIFT-002, etc.)
   - **Endpoint**: Device_ID experiencing drift
   - **Baseline_Control**: Which baseline control drifted (e.g., "Firewall enabled")
   - **Expected_Value**: Approved baseline value (e.g., "Enabled")
   - **Actual_Value**: Current detected value (e.g., "Disabled")
   - **Drift_Detected_Date**: When drift detected
   - **Root_Cause**: Why drift occurred (user disabled, software update, policy conflict, malware)
   - **Severity**: Critical, High, Medium, Low (based on security impact)
   - **Remediation_Action**: Re-apply GPO, Re-deploy MDM profile, Manual fix, Investigate further
   - **Remediation_Owner**: Person/team responsible
   - **Target_Date**: Target remediation date (Critical ≤24h, High ≤7 days, Medium ≤30 days)
   - **Remediation_Status**: Not Started, In Progress, Completed, Deferred
   - **Verification_Date**: Date drift remediation verified

3. **Automatic Remediation:**
   - GPO: Automatic re-application on next Group Policy refresh
   - MDM: Automatic re-deployment on next device check-in
   - Document automatic remediation attempts

4. **Manual Remediation:**
   - Configuration drift requiring manual intervention
   - Investigate root cause before remediation
   - Prevent recurrence (policy change, user training, technical control)

**Quality Target:** <5% endpoints with active drift, drift remediated within SLA (Critical ≤24h, High ≤7 days)

### Sheet 6: Gaps

**Purpose:** Non-compliant endpoints and remediation plans

**Completion Steps:**

1. **Gap Identification** (from Compliance_Status sheet):
   - Endpoints with compliance <90% (Yellow or Red status)
   - Endpoints with encryption disabled (when required)
   - Endpoints not enrolled in management (when required)
   - Endpoints with critical configuration drift

2. **For Each Gap:**
   - **Gap_ID**: Unique identifier (GAP-S2-001, GAP-S2-002, etc.)
   - **Gap_Type**: Baseline Non-Compliance, Encryption Missing, Management Not Enrolled, Configuration Drift
   - **Affected_Endpoint**: Device_ID
   - **Endpoint_Criticality**: Critical, High, Medium, Low (from endpoint classification)
   - **Gap_Description**: Specific issue (e.g., "Endpoint not encrypted, 15 baseline controls failed")
   - **Impact**: Critical, High, Medium, Low (severity of gap)
   - **Priority**: 🔴 Critical, 🟡 High, 🟢 Medium, ⚪ Low
   - **Root_Cause**: Why gap exists (legacy device, technical incompatibility, deployment delay, user action)
   - **Remediation_Plan**: Specific actions (Deploy encryption, apply baseline via GPO, enroll in MDM, investigate drift)
   - **Remediation_Owner**: Person/team responsible
   - **Target_Date**: Target completion date (Critical ≤24h, High ≤7 days, Medium ≤30 days, Low ≤90 days)
   - **Remediation_Status**: Not Started, In Progress, Completed, Deferred
   - **Exception_Required**: Yes/No (if cannot remediate, exception approval needed)
   - **Exception_Approved_By**: CISO (if exception granted)

**Quality Target:** All Critical/High gaps remediated within SLA, <10% endpoints in gap status

---

## Evidence Collection

### Required Evidence Types

For audit purposes, maintain the following evidence:

#### 1. Baseline Documentation Evidence

- **Baseline Documents**: Windows Security Baseline, macOS Security Baseline, Linux Security Baseline, iOS/Android Security Baseline
- **Baseline Approval**: CISO approval documentation for each baseline
- **Baseline Sources**: CIS Benchmark PDFs, Microsoft Security Baseline documentation, Apple Platform Security Guide

#### 2. Baseline Deployment Evidence

- **Group Policy Objects**: GPO exports showing baseline implementation (Windows)
- **MDM Configuration Profiles**: Intune/Jamf profile exports (macOS, iOS, Android)
- **Configuration Management**: Ansible playbooks, Puppet manifests showing Linux baseline
- **Deployment Logs**: Evidence of baseline deployment to endpoints

#### 3. Compliance Scanning Evidence

- **Compliance Scan Results**: Microsoft Defender for Endpoint compliance reports, Jamf compliance reports, SCAP scan results
- **Compliance Dashboards**: Screenshots of compliance status dashboards
- **Spot-Check Results**: Manual verification of random sample (20 endpoints per OS)

#### 4. Encryption Evidence

- **Encryption Status Reports**: BitLocker reports (Intune, MBAM), FileVault reports (Jamf), LUKS verification
- **Key Escrow Verification**: Evidence that recovery keys escrowed for corporate devices
- **Encryption Exceptions**: CISO-approved exceptions for desktop computers in secure facilities

#### 5. Management Enrollment Evidence

- **MDM Enrollment Reports**: Intune enrollment report, Jamf enrollment report, device count per platform
- **Agent Status Reports**: Management agent version distribution, agent health status

#### 6. Configuration Drift Evidence

- **Drift Detection Logs**: Weekly drift scan results, drift incidents tracked
- **Remediation Logs**: Evidence of drift remediation (GPO re-application, MDM profile re-deployment)

### Evidence Retention

- **Retention Period**: 12 months minimum
- **Storage Location**: Centralized repository (SharePoint, network share, document management system)
- **Access Controls**: Restrict access to authorized personnel (endpoint administrators, auditors)

---

## Common Pitfalls (10 Mistakes to Avoid)

### 1. Generic Baselines Not Tailored to OS

**Mistake:** Using same baseline requirements for Windows, macOS, Linux  
**Why It's Wrong:** Different OS have different hardening mechanisms (GPO vs. Jamf profiles vs. Ansible), generic baselines are unenforceable  
**Solution:** Create OS-specific baselines based on vendor security guides and CIS Benchmarks

### 2. Baselines Not Actually Deployed

**Mistake:** Documenting security baseline requirements without deploying via GPO/MDM  
**Why It's Wrong:** Baseline document is meaningless if not enforced - endpoints remain insecure  
**Solution:** Deploy baselines via GPO (Windows), MDM profiles (macOS/mobile), configuration management (Linux), verify deployment

### 3. No Compliance Monitoring

**Mistake:** Deploying baselines but never scanning for compliance  
**Why It's Wrong:** Cannot verify baselines are effective, drift goes undetected, users can bypass controls  
**Solution:** Weekly automated compliance scans, monthly compliance reporting, automatic remediation where possible

### 4. Encryption Without Key Escrow

**Mistake:** Deploying BitLocker/FileVault without escrowing recovery keys  
**Why It's Wrong:** User forgets password → data permanently lost, cannot recover encrypted device  
**Solution:** Centralized key escrow (Active Directory, Intune, Jamf) for all corporate devices, verify escrow before encryption deployment

### 5. BYOD Same Baseline as Corporate

**Mistake:** Applying full corporate baseline to BYOD devices  
**Why It's Wrong:** Violates user privacy (full device control), GDPR/FADP violation, users reject BYOD program  
**Solution:** BYOD baseline limited to corporate container (MAM), no full device encryption requirement, user privacy protections

### 6. No Exception Process

**Mistake:** Blanket baseline enforcement with no exceptions  
**Why It's Wrong:** Legacy devices, technical incompatibilities, business requirements require exceptions  
**Solution:** Documented exception request process, CISO approval required, compensating controls mandatory

### 7. Compliance Calculated Incorrectly

**Mistake:** Calculating compliance as "all controls pass" (binary) vs. percentage  
**Why It's Wrong:** Endpoint with 89% compliance (45/50 controls) marked "non-compliant" same as 10% compliance (5/50)  
**Solution:** Calculate compliance percentage, set thresholds (Green ≥90%, Yellow 70-89%, Red <70%)

### 8. Configuration Drift Ignored

**Mistake:** Detecting configuration drift but not investigating or remediating  
**Why It's Wrong:** Drift indicates security control failure, potential malware, user bypassing controls  
**Solution:** Weekly drift scans, investigate root cause, automatic remediation, prevent recurrence

### 9. Spot-Check Not Performed

**Mistake:** Trusting automated compliance scans without manual verification  
**Why It's Wrong:** Compliance scanners have false positives/negatives, scan tools can be bypassed  
**Solution:** Random sample spot-check (20 endpoints), manually verify compliance scan accuracy

### 10. No Remediation Tracking

**Mistake:** Identifying non-compliant endpoints but not tracking remediation to completion  
**Why It's Wrong:** Gaps identified but never fixed, compliance does not improve over time  
**Solution:** Gap register with remediation owners, target dates, status tracking, monthly review

---

## Quality Checklist (50+ Items)

### Baseline Definition (10 Items)

- [ ] 1. Windows security baseline documented
- [ ] 2. macOS security baseline documented
- [ ] 3. Linux security baseline documented (if Linux endpoints exist)
- [ ] 4. iOS security baseline documented (if iOS endpoints exist)
- [ ] 5. Android security baseline documented (if Android endpoints exist)
- [ ] 6. Baselines based on vendor guidance (Microsoft, Apple) and CIS Benchmarks
- [ ] 7. Baselines approved by CISO before deployment
- [ ] 8. Baseline approval date documented
- [ ] 9. Baseline customizations documented with rationale
- [ ] 10. Baseline control count documented per platform

### Baseline Deployment (10 Items)

- [ ] 11. Windows baseline deployed via GPO or Intune
- [ ] 12. macOS baseline deployed via Jamf or Intune
- [ ] 13. Linux baseline deployed via Ansible/Puppet/Chef or manual
- [ ] 14. Mobile baseline deployed via MDM profiles
- [ ] 15. Baseline deployment verified (pilot group tested before production)
- [ ] 16. Baseline deployment evidence collected (GPO exports, MDM profiles)
- [ ] 17. Baseline enforcement method documented per OS
- [ ] 18. Deployment logs show successful baseline application
- [ ] 19. Baseline deployment reaches ≥95% of applicable endpoints
- [ ] 20. Deployment failures investigated and resolved

### Compliance Monitoring (10 Items)

- [ ] 21. Compliance scans run weekly minimum (daily preferred)
- [ ] 22. Compliance scan results imported to Baseline_Compliance.xlsx
- [ ] 23. Per-endpoint compliance percentage calculated
- [ ] 24. Compliance status (Green/Yellow/Red) assigned correctly
- [ ] 25. Overall compliance rate ≥90% achieved (or gaps documented)
- [ ] 26. Spot-check validation performed (20 endpoints per OS)
- [ ] 27. Spot-check accuracy ≥95%
- [ ] 28. Compliance scan tool documented (Microsoft Defender, Jamf, SCAP, etc.)
- [ ] 29. Compliance scan date current (≤7 days old)
- [ ] 30. Top baseline failures identified per endpoint

### Encryption Verification (10 Items)

- [ ] 31. Encryption status verified for all corporate laptops
- [ ] 32. Encryption status verified for all corporate desktops
- [ ] 33. Encryption status verified for all corporate mobile devices
- [ ] 34. Encryption coverage ≥98% (corporate endpoints)
- [ ] 35. Encryption algorithm verified (AES-256 minimum)
- [ ] 36. Pre-boot authentication enabled (BitLocker, FileVault)
- [ ] 37. Encryption keys escrowed for corporate devices (100% coverage)
- [ ] 38. Key escrow location documented (AD, Intune, Jamf, MBAM)
- [ ] 39. Encryption exceptions approved by CISO (if any)
- [ ] 40. Compensating controls documented for encryption exceptions

### Management Enrollment (10 Items)

- [ ] 41. Management enrollment verified for all corporate endpoints
- [ ] 42. Management enrollment ≥98% (corporate endpoints)
- [ ] 43. BYOD enrollment (MAM) ≥80% (if BYOD program exists)
- [ ] 44. Management platform documented per endpoint
- [ ] 45. Last check-in date verified (≤7 days for active endpoints)
- [ ] 46. Stale check-ins flagged (>7 days Yellow, >30 days Red)
- [ ] 47. Management agent version tracked
- [ ] 48. Agent health status monitored (Running, Stopped, Not Installed)
- [ ] 49. BYOD user consent documented (if BYOD program exists)
- [ ] 50. BYOD privacy notice provided (if BYOD program exists)

### Configuration Drift & Gaps (10 Items)

- [ ] 51. Configuration drift scans run weekly
- [ ] 52. Drift incidents documented with root cause
- [ ] 53. Drift remediation SLA met (Critical ≤24h, High ≤7 days)
- [ ] 54. Automatic remediation configured where possible
- [ ] 55. Active drift <5% of endpoints
- [ ] 56. Gaps identified and documented (non-compliant endpoints)
- [ ] 57. Gap remediation owners assigned
- [ ] 58. Gap target dates set based on priority
- [ ] 59. Gap remediation status tracked
- [ ] 60. Critical/High gaps remediated within SLA

---

## Review & Approval

### Three-Level Approval Workflow

#### Level 1: Data Owner Review

**Reviewer:** Endpoint Administrator, Security Engineer  
**Focus:** Data completeness and technical accuracy

**Review Checklist:**
- [ ] All baselines documented and deployed
- [ ] Compliance scans current (≤7 days old)
- [ ] Encryption status verified
- [ ] Management enrollment verified
- [ ] Configuration drift tracked

**Approval Criteria:**
- Compliance scans performed weekly
- Compliance data complete for ≥95% endpoints
- Encryption verification complete

**Action:** Sign and date in workbook approval section

#### Level 2: IT Security Manager Review

**Reviewer:** IT Security Manager, Information Security Officer  
**Focus:** Compliance rates, gap remediation, risk acceptance

**Review Checklist:**
- [ ] Overall compliance rate ≥90% (or gaps documented with remediation plans)
- [ ] Encryption coverage ≥98% (or exceptions approved)
- [ ] Critical/High gaps have remediation plans
- [ ] Configuration drift remediated within SLA

**Approval Criteria:**
- Compliance threshold met (≥90%) OR gap remediation plans approved
- All Critical gaps remediated OR risk accepted by CISO
- Evidence collection complete

**Action:** Sign and date in workbook approval section

#### Level 3: CISO Review

**Reviewer:** Chief Information Security Officer (or delegated authority)  
**Focus:** Risk acceptance, strategic gaps, regulatory compliance

**Review Checklist:**
- [ ] Baseline compliance supports A.8.1 requirements
- [ ] Encryption coverage meets policy requirements (≥98%)
- [ ] Exceptions documented and compensating controls implemented
- [ ] Audit readiness verified

**Approval Criteria:**
- Compliance rate ≥90% OR risk accepted
- All encryption exceptions approved with compensating controls
- Assessment supports ISO 27001 audit

**Action:** Sign and date in workbook approval section

### Post-Approval Actions

1. **Archive Approved Version:** Save approved workbook with date stamp
2. **Communicate Results:** Share compliance summary with stakeholders
3. **Schedule Ongoing Scans:** Ensure weekly compliance scanning continues
4. **Track Remediation:** Monitor gap remediation progress monthly
5. **Plan Next Review:** Schedule monthly compliance review

---

# PART II: TECHNICAL SPECIFICATION

## Instructions for Workbook Developers

This section provides detailed specifications for developers creating the `Baseline_Compliance.xlsx` workbook (via Python script `generate_a817_2_security_baseline.py` or manual creation).

### Workbook Overview

**Workbook Name:** `Baseline_Compliance.xlsx`  
**Purpose:** Document security baseline compliance and encryption verification  
**Target Users:** Endpoint Administrators, Security Engineers, Compliance Officers, Auditors  
**Creation Method:** Python script (`generate_a817_2_security_baseline.py`) or manual Excel creation

### Sheet Structure

The workbook contains 6 worksheets:

1. **Baseline_Inventory** - Security baselines defined
2. **Compliance_Status** - Per-endpoint baseline compliance
3. **Encryption_Status** - Encryption verification
4. **Management_Enrollment** - MDM/agent enrollment status
5. **Configuration_Drift** - Configuration deviations
6. **Gaps** - Non-compliant endpoints and remediation

---

## Common Column Structure

### Data Types

Consistent with Endpoint_Inventory.xlsx (ISMS-IMP-A.8.1-7-18-19-S1):

| Data Type | Description | Example | Validation |
|-----------|-------------|---------|------------|
| **Text** | Free-form text | "Windows 11 Baseline" | Max 255 chars |
| **Text (Constrained)** | Dropdown list | "Enabled" | Must be from approved list |
| **Date** | Date value | 2026-01-25 | ISO format YYYY-MM-DD |
| **DateTime** | Date and time | 2026-01-25 14:30:00 | ISO format |
| **Integer** | Whole number | 42 | No decimals |
| **Percentage** | Percentage value | 95% | 0-100, formatted as % |
| **Status** | Status indicator | 🟢 Green | Emoji-based visual |

### Status Columns

Same as S1 (Endpoint_Inventory):

| Status | Emoji | Color | Threshold |
|--------|-------|-------|-----------|
| Green | 🟢 | Green fill (#C6EFCE), dark green text (#006100) | ≥90% |
| Yellow | 🟡 | Yellow fill (#FFEB9C), dark yellow text (#9C6500) | 70-89% |
| Red | 🔴 | Red fill (#FFC7CE), dark red text (#9C0006) | <70% |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Baseline_Inventory

**Purpose:** Document all security baselines defined

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Baseline_Name | Text | 30 | Required | None | Windows 11 Corporate Baseline, macOS 14 Corporate Baseline |
| B: Platform | Text (Constrained) | 20 | Dropdown | None | Windows 11, macOS 14, Ubuntu 22.04, iOS 17, Android 13 |
| C: Baseline_Source | Text | 40 | Optional | None | Microsoft Security Baseline, CIS Benchmark Level 1 |
| D: Version | Text | 20 | Optional | None | v2.0.0, Jan 2026 |
| E: Approval_Date | Date | 15 | Optional | None | Date CISO approved |
| F: Approval_Authority | Text | 20 | Optional | None | CISO, Security Committee |
| G: Enforcement_Method | Text (Constrained) | 20 | Dropdown | None | GPO, Intune Profile, Jamf Profile, Ansible |
| H: Control_Count | Integer | 15 | Optional | None | Number of security controls |
| I: Applicable_Endpoints | Text | 40 | Optional | None | All Windows 11 corporate laptops/desktops |
| J: Notes | Text | 40 | Optional | None | Baseline customization notes |

#### Dropdown Values

**Platform:** Windows 11, Windows 10, macOS 14, macOS 13, Ubuntu 22.04, RHEL 9, iOS 17, Android 13, Other  
**Enforcement_Method:** GPO, Intune Profile, Jamf Profile, Ansible, Puppet, Chef, SCCM, Manual

---

### Sheet 2: Compliance_Status

**Purpose:** Per-endpoint baseline compliance assessment

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Device_ID | Text | 20 | Required | From Inventory | Import from S1 |
| B: Hostname | Text | 25 | Required | From Inventory | Import from S1 |
| C: Device_Type | Text | 15 | Optional | From Inventory | Import from S1 |
| D: Operating_System | Text | 20 | Required | From Inventory | Import from S1 |
| E: Criticality | Text | 12 | Optional | From Inventory | Import from S1 |
| F: Baseline_Applied | Text | 30 | Required | None | Which baseline (Windows 11 Corporate, etc.) |
| G: Compliance_Scan_Date | DateTime | 20 | Required | None | Date of last scan |
| H: Total_Controls | Integer | 15 | Required | None | Total controls in baseline |
| I: Compliant_Controls | Integer | 18 | Required | None | Passed controls |
| J: Non_Compliant_Controls | Integer | 22 | None | `=H2-I2` | Failed controls |
| K: Compliance_Percentage | Percentage | 20 | None | `=I2/H2` | Compliance % |
| L: Compliance_Status | Status | 18 | None | `=IF(K2>=0.9,"🟢 Green",IF(K2>=0.7,"🟡 Yellow","🔴 Red"))` | Visual status |
| M: Top_Failures | Text | 50 | Optional | None | Top 3 failed controls |
| N: Scan_Tool | Text | 20 | Optional | None | Microsoft Defender, Jamf, SCAP |
| O: Notes | Text | 40 | Optional | None | Additional notes |

#### Conditional Formatting

Apply to column L (Compliance_Status):
- Green: Contains "Green" → Green fill, dark green text
- Yellow: Contains "Yellow" → Yellow fill, dark yellow text
- Red: Contains "Red" → Red fill, dark red text

Apply to column G (Compliance_Scan_Date):
- Stale scans (>7 days): `=TODAY()-G2>7` → Yellow fill
- Very stale (>30 days): `=TODAY()-G2>30` → Red fill

---

### Sheet 3: Encryption_Status

**Purpose:** Verify encryption status and key escrow

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Device_ID | Text | 20 | Required | From Inventory | Import from S1 |
| B: Hostname | Text | 25 | Required | From Inventory | Import from S1 |
| C: Device_Type | Text | 15 | Optional | From Inventory | Laptop, Desktop, Smartphone, Tablet |
| D: Ownership_Model | Text | 18 | Optional | From Inventory | Corporate-Owned, BYOD |
| E: Encryption_Required | Text (Constrained) | 20 | Dropdown | None | Yes, No |
| F: Encryption_Technology | Text (Constrained) | 22 | Dropdown | None | BitLocker, FileVault, LUKS, Built-in Mobile |
| G: Encryption_Status | Text (Constrained) | 18 | Dropdown | None | Enabled, Disabled, Not Supported |
| H: Encryption_Algorithm | Text | 18 | Optional | None | AES-256, AES-128 |
| I: Pre_Boot_Auth | Text (Constrained) | 15 | Dropdown | None | Enabled, Disabled, TPM-Only |
| J: Key_Escrow_Required | Text (Constrained) | 20 | Dropdown | None | Yes, No, N/A |
| K: Key_Escrow_Status | Text (Constrained) | 18 | Dropdown | None | Escrowed, Not Escrowed, N/A |
| L: Key_Escrow_Location | Text | 25 | Optional | None | Active Directory, Intune, Jamf, MBAM |
| M: Verification_Date | Date | 18 | Required | None | Date verified |
| N: Encryption_Compliance | Status | 20 | None | `=IF(AND(E2="Yes",G2="Enabled",OR(J2="No",K2="Escrowed")),"🟢 Compliant","🔴 Non-Compliant")` | Compliance status |
| O: Exception_Reason | Text | 40 | Optional | None | If not encrypted |
| P: Exception_Approved_By | Text | 20 | Optional | None | CISO |
| Q: Notes | Text | 40 | Optional | None | Additional notes |

#### Dropdown Values

**Encryption_Required:** Yes, No  
**Encryption_Technology:** BitLocker, FileVault, LUKS, Built-in Mobile (iOS/Android), Symantec, McAfee, Other  
**Encryption_Status:** Enabled, Disabled, Not Supported, Unknown  
**Pre_Boot_Auth:** Enabled, Disabled, TPM-Only, N/A  
**Key_Escrow_Required:** Yes, No, N/A  
**Key_Escrow_Status:** Escrowed, Not Escrowed, N/A, Unknown

---

### Sheet 4: Management_Enrollment

**Purpose:** Verify MDM/agent enrollment

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Device_ID | Text | 20 | Required | From Inventory | Import from S1 |
| B: Hostname | Text | 25 | Required | From Inventory | Import from S1 |
| C: Ownership_Model | Text | 18 | Optional | From Inventory | Corporate-Owned, BYOD |
| D: Management_Required | Text (Constrained) | 20 | Dropdown | None | Yes, MAM Only, No |
| E: Management_Platform | Text | 25 | Optional | None | Intune, Jamf Pro, SCCM, Google Workspace MDM |
| F: Enrollment_Status | Text (Constrained) | 18 | Dropdown | None | Enrolled, Not Enrolled, Enrollment Failed |
| G: Enrollment_Date | Date | 15 | Optional | None | Date enrolled |
| H: Last_Check_In | DateTime | 20 | Required | None | Last management check-in |
| I: Agent_Version | Text | 15 | Optional | None | Management agent version |
| J: Agent_Status | Text (Constrained) | 15 | Dropdown | None | Running, Stopped, Not Installed |
| K: Management_Capabilities | Text | 25 | Optional | None | Full MDM, MAM Only, Domain Joined |
| L: Enrollment_Compliance | Status | 20 | None | `=IF(AND(D2="Yes",F2="Enrolled"),"🟢 Compliant",IF(AND(D2="MAM Only",F2="Enrolled"),"🟢 Compliant","🔴 Non-Compliant"))` | Compliance |
| M: Check_In_Status | Status | 18 | None | `=IF(DAYS(TODAY(),H2)<=7,"🟢 Current",IF(DAYS(TODAY(),H2)<=30,"🟡 Stale","🔴 Very Stale"))` | Stale check-in flag |
| N: Notes | Text | 40 | Optional | None | Additional notes |

#### Dropdown Values

**Management_Required:** Yes, MAM Only, No  
**Enrollment_Status:** Enrolled, Not Enrolled, Enrollment Failed, Pending  
**Agent_Status:** Running, Stopped, Not Installed, Unknown

---

### Sheet 5: Configuration_Drift

**Purpose:** Track configuration deviations

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Drift_ID | Text | 15 | Required | None | DRIFT-001, DRIFT-002 |
| B: Endpoint | Text | 20 | Required | From Inventory | Device_ID experiencing drift |
| C: Baseline_Control | Text | 40 | Required | None | Control that drifted |
| D: Expected_Value | Text | 20 | Required | None | Approved baseline value |
| E: Actual_Value | Text | 20 | Required | None | Current detected value |
| F: Drift_Detected_Date | DateTime | 20 | Required | None | When drift detected |
| G: Root_Cause | Text | 50 | Optional | None | Why drift occurred |
| H: Severity | Text (Constrained) | 12 | Dropdown | None | Critical, High, Medium, Low |
| I: Priority | Status | 12 | None | `=IF(H2="Critical","🔴 Critical",IF(H2="High","🟡 High",IF(H2="Medium","🟢 Medium","⚪ Low")))` | Visual priority |
| J: Remediation_Action | Text | 60 | Required | None | What to do |
| K: Remediation_Owner | Text | 20 | Optional | None | Responsible person |
| L: Target_Date | Date | 15 | Optional | None | Target completion |
| M: Remediation_Status | Text (Constrained) | 18 | Dropdown | None | Not Started, In Progress, Completed, Deferred |
| N: Verification_Date | Date | 18 | Optional | None | Date verified fixed |
| O: Notes | Text | 40 | Optional | None | Additional notes |

#### Dropdown Values

**Severity:** Critical, High, Medium, Low  
**Remediation_Status:** Not Started, In Progress, Completed, Deferred

---

### Sheet 6: Gaps

**Purpose:** Non-compliant endpoints and remediation

Same structure as Sheet 6 in Endpoint_Inventory (S1), adapted for baseline compliance gaps.

---

## Cell Styling Reference

Same as ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint_Inventory):
- Header Row: Dark blue (#002060), white text, bold, center aligned
- Freeze Panes: Row 2
- AutoFilter: Enabled
- Alternating Rows: White / Light gray (#F2F2F2)
- Status Columns: Conditional formatting (Green/Yellow/Red)

---

## Appendix: Technical Notes for Python Developers

### Script: `generate_a817_2_security_baseline.py`

Same Python libraries and patterns as `generate_a817_1_endpoint_inventory.py`.

**Key Differences:**
- Import endpoint data from Endpoint_Inventory.xlsx (S1 must exist)
- Generate 6 worksheets focused on baseline compliance
- Calculate compliance percentages, encryption coverage, enrollment coverage
- Apply conditional formatting for compliance status, encryption compliance, enrollment compliance

**Sample Code Snippet (Compliance Percentage Calculation):**

```python
# Add formula for Compliance_Percentage (column K)
for row in range(2, max_row + 1):
    ws_compliance[f'K{row}'] = f'=I{row}/H{row}'  # Compliant / Total
    
# Add formula for Compliance_Status (column L)
for row in range(2, max_row + 1):
    ws_compliance[f'L{row}'] = f'=IF(K{row}>=0.9,"🟢 Green",IF(K{row}>=0.7,"🟡 Yellow","🔴 Red"))'
```

---

**END OF IMPLEMENTATION GUIDE**

---

*This implementation guide provides comprehensive instructions for completing the Security Baseline Implementation assessment. For policy requirements, refer to ISMS-POL-A.8.1-7-18-19, Section 2.1.3-2.1.5. For baseline configuration details, refer to vendor documentation (Microsoft Security Baseline, Apple Platform Security Guide, CIS Benchmarks).*
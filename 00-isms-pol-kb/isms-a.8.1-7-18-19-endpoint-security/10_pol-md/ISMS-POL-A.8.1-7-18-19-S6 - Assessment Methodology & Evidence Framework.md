# ISMS-POL-A.8.1-7-18-19-S6
## Assessment Methodology & Evidence Framework
### Endpoint Security Assessment and Compliance Verification

---

**Document ID**: ISMS-POL-A.8.1-7-18-19-S6  
**Title**: Assessment Methodology & Evidence Framework  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial assessment methodology framework |

**Review Cycle**: Annual  
**Parent Document**: ISMS-POL-A.8.1-7-18-19 (Master Framework)  
**Related Documents**: S2 (A.8.1 Requirements), S3 (A.8.7 Requirements), S4 (A.8.18 Requirements), S5 (A.8.19 Requirements)

---

## 1. Purpose and Scope

### 1.1 Purpose

This document defines the **unified assessment methodology** for evaluating compliance with ISO/IEC 27001:2022 Controls A.8.1 (User Endpoint Devices), A.8.7 (Protection Against Malware), A.8.18 (Use of Privileged Utility Programs), and A.8.19 (Installation of Software on Operational Systems).

The assessment methodology provides:
- Systematic approach to endpoint security evaluation
- Standardized evidence collection procedures
- Consistent compliance scoring methodology
- Clear audit trail for certification/compliance verification
- Continuous improvement framework
- Integration across all four endpoint security controls

### 1.2 Scope

This assessment framework covers:
- **Endpoint Discovery**: Systematic identification of all endpoints (laptops, desktops, mobile devices)
- **Endpoint Security Assessment**: Evaluation of endpoint device security (A.8.1)
- **Malware Protection Assessment**: Evaluation of malware protection coverage and effectiveness (A.8.7)
- **Privileged Utility Assessment**: Evaluation of privileged utility controls (A.8.18)
- **Software Control Assessment**: Evaluation of software installation controls (A.8.19)
- **Evidence Collection**: Documentation and artifact gathering for audit purposes
- **Compliance Scoring**: Quantitative measurement of control implementation
- **Gap Management**: Identification, prioritization, and remediation tracking

### 1.3 Systems Engineering Approach

This framework employs a **Systems Engineering methodology**:

```
Discovery → Classification → Evaluation → Gap Identification → Remediation → Verification
    ↑                                                                            ↓
    └──────────────────────── Continuous Improvement ──────────────────────────┘
```

**Key Principles**:
1. **Systematic**: Structured, repeatable processes
2. **Evidence-Based**: Objective verification over subjective claims
3. **Technology-Agnostic**: Works across any endpoint environment (Windows, macOS, Linux, mobile)
4. **Automation-First**: Python-generated workbooks for consistency
5. **Continuous**: Not just point-in-time, but ongoing assessment
6. **Integrated**: Single assessment process serves all four controls

---

## 2. Assessment Methodology Overview

### 2.1 Assessment Lifecycle

**Phase 1: Planning (Week 0)**
- Define assessment scope (which endpoints, which controls)
- Identify stakeholders and responsibilities
- Schedule assessment activities
- Prepare assessment tools and workbooks
- Communicate assessment to users

**Phase 2: Discovery (Weeks 1-2)**
- Execute automated endpoint discovery (MDM APIs, network scanning, SCCM inventory)
- Execute manual discovery (user surveys, documentation review)
- Classify endpoints (type, OS, ownership, criticality)
- Map endpoint management infrastructure
- Inventory software on endpoints
- Identify privileged utilities on endpoints

**Phase 3: Data Collection (Weeks 2-3)**
- Gather endpoint configurations (baselines, GPOs, MDM profiles)
- Collect malware protection status (agent status, signature versions, scan logs)
- Collect software inventory (approved software, installed software)
- Gather privileged utility access records (approvals, usage logs)
- Collect logs (endpoint events, SIEM logs)
- Gather incident reports (malware detections, lost/stolen devices)

**Phase 4: Evaluation (Weeks 3-4)**
- Assess endpoint baseline compliance (against defined baselines)
- Assess malware protection coverage and effectiveness
- Assess privileged utility access controls and logging
- Assess software control effectiveness
- Calculate compliance scores per control
- Identify gaps and deviations

**Phase 5: Gap Analysis (Week 4)**
- Classify gaps by severity (Critical, High, Medium, Low)
- Prioritize remediation based on risk
- Document compensating controls (if applicable)
- Create remediation plans with timelines and owners

**Phase 6: Reporting (Week 5)**
- Generate assessment workbooks (WB1-WB6)
- Generate executive dashboard
- Present findings to management
- Present evidence to auditors (if audit cycle)

**Phase 7: Remediation (Weeks 6-12)**
- Execute remediation plans
- Track remediation progress weekly
- Verify remediation effectiveness
- Update assessment workbooks

**Phase 8: Continuous Monitoring (Ongoing)**
- Automated configuration drift detection (daily)
- Real-time malware detection monitoring (continuous)
- Software inventory updates (daily)
- Periodic re-assessment (quarterly refresh)

### 2.2 Assessment Types

**Initial Assessment (Comprehensive)**:
- Full endpoint discovery across all endpoint types
- Complete evaluation of all requirements (A.8.1, A.8.7, A.8.18, A.8.19)
- Baseline establishment for future comparisons
- **Executed**: Upon framework implementation
- **Duration**: 4-5 weeks (depending on endpoint count)

**Annual Assessment (Full Re-Assessment)**:
- Scheduled comprehensive re-assessment
- Full re-discovery and re-evaluation
- Trend analysis (compare to previous assessments)
- **Executed**: Annually (scheduled)
- **Duration**: 3-4 weeks

**Quarterly Assessment (Targeted)**:
- Focused assessment on high-risk areas
- Update assessment workbooks
- Verify remediation of previous gaps
- **Executed**: Quarterly
- **Duration**: 1-2 weeks

**Continuous Assessment (Ongoing)**:
- Daily: Software inventory updates, malware detection monitoring
- Weekly: Baseline compliance scans
- Monthly: Comprehensive metrics reporting
- **Executed**: Continuous via automated tools
- **Duration**: N/A (ongoing)

**Incident-Driven Assessment (Ad-Hoc)**:
- Triggered by security incidents (malware outbreak, data breach)
- Focused on affected endpoints and related controls
- **Executed**: As needed
- **Duration**: 1-3 days

### 2.3 Assessment Roles and Responsibilities

| Role | Responsibilities | Assessment Activities |
|------|------------------|----------------------|
| **CISO** | Overall accountability, risk acceptance | Review findings, approve remediation plans |
| **Information Security Manager** | Assessment coordination, gap analysis | Lead assessment, coordinate data collection, analyze results |
| **IT Operations Manager** | Endpoint management support, remediation | Provide endpoint data, execute remediation |
| **Endpoint Administrators** | Data collection, technical support | Run discovery tools, collect configurations |
| **Security Analysts** | Data analysis, evidence collection | Analyze logs, verify compliance, document evidence |
| **Auditors** | Independent verification | Review evidence, test controls, issue findings |

---

## 3. Control-Specific Assessment Methodologies

### 3.1 A.8.1 - User Endpoint Devices Assessment

**Assessment Objectives**:
- Verify complete endpoint inventory (≥95% coverage)
- Verify endpoint classification (100% of endpoints classified)
- Verify baseline compliance (≥90% compliant)
- Verify encryption coverage (≥98% corporate laptops/desktops)
- Verify endpoint management enrollment (≥98% corporate devices)
- Verify lost/stolen procedures effectiveness
- Verify disposal procedures compliance

**Assessment Methods**:

1. **Endpoint Inventory Verification**:
   - **Automated Discovery**: Network scanning (nmap, Lansweeper), MDM inventory pull
   - **Manual Verification**: Spot-check random sample (20 endpoints) - physically verify existence
   - **Reconciliation**: Compare automated inventory vs. network discovery vs. asset register
   - **Acceptance Criteria**: Inventory accuracy ≥95%

2. **Baseline Compliance Assessment**:
   - **Automated Scanning**: MDM compliance reports, Microsoft Defender secure score, CIS-CAT
   - **Manual Verification**: Spot-check sample endpoints (10 per OS type) - manual configuration review
   - **Configuration Drift Detection**: Compare current config vs. baseline GPO/MDM profile
   - **Acceptance Criteria**: Average baseline compliance ≥90%

3. **Encryption Verification**:
   - **Automated Status Check**: BitLocker/FileVault status reports from MDM/management tools
   - **Key Escrow Verification**: Verify recovery keys escrowed for sample endpoints (20 devices)
   - **Manual Verification**: Spot-check encryption active (boot endpoint, verify pre-boot auth)
   - **Acceptance Criteria**: Encryption coverage ≥98% (corporate laptops/desktops)

4. **Management Enrollment Verification**:
   - **MDM Enrollment Reports**: Pull enrollment status from MDM platform
   - **Agent Health Check**: Verify endpoint management agent active and communicating
   - **Manual Verification**: Test management capabilities (deploy config, verify applied)
   - **Acceptance Criteria**: Enrollment coverage ≥98% (corporate devices)

5. **Lost/Stolen Procedure Verification**:
   - **Incident Review**: Review all lost/stolen incidents (last 12 months)
   - **Timeline Verification**: Verify remote wipe executed within 4 hours (SLA compliance)
   - **Documentation Review**: Verify incident reports complete
   - **Acceptance Criteria**: 100% incidents have wipe attempted within SLA

6. **Disposal Procedure Verification**:
   - **Disposal Record Review**: Review all disposed endpoints (last 12 months)
   - **Certificate Verification**: Verify 100% have certificate of destruction/sanitization
   - **Process Observation**: Observe disposal process (if assessment period coincides)
   - **Acceptance Criteria**: 100% disposed devices have certificate

**Evidence Requirements**:
- Endpoint_Inventory.xlsx (9 worksheets)
- MDM console screenshots
- Baseline compliance scan reports
- Encryption management console reports
- Lost/stolen incident reports
- Disposal certificates

**Assessment Frequency**:
- Inventory: Weekly automated, quarterly reconciliation
- Baseline compliance: Weekly automated, monthly reporting
- Encryption: Monthly verification
- Management enrollment: Monthly verification
- Lost/stolen: Review each incident, quarterly trend analysis
- Disposal: Review each disposal, annual audit

### 3.2 A.8.7 - Protection Against Malware Assessment

**Assessment Objectives**:
- Verify protection coverage (≥98% corporate, ≥80% BYOD)
- Verify signature currency (≥98% updated within 24 hours)
- Verify scan compliance (≥95% weekly full scans, ≥90% daily quick scans)
- Verify detection effectiveness (remediation success rate)
- Verify incident response effectiveness (SLA compliance)
- Verify user awareness program effectiveness

**Assessment Methods**:

1. **Protection Coverage Assessment**:
   - **Automated Coverage Reports**: Pull protection status from anti-malware console
   - **Agent Health Check**: Verify agents active and communicating
   - **Manual Verification**: Spot-check sample endpoints (20) - verify agent running
   - **Gap Identification**: Identify unprotected endpoints, determine root cause
   - **Acceptance Criteria**: Coverage ≥98% (corporate), ≥80% (BYOD)

2. **Signature Currency Assessment**:
   - **Signature Version Reports**: Pull signature versions from anti-malware console
   - **Outdated Signature Identification**: Flag endpoints >24 hours outdated
   - **Root Cause Analysis**: Why are signatures outdated? (network issues, agent issues)
   - **Acceptance Criteria**: ≥98% endpoints have signatures updated within 24 hours

3. **Scan Compliance Assessment**:
   - **Scan Log Analysis**: Pull scan completion logs (last 30 days)
   - **Full Scan Compliance**: Calculate percentage completing weekly full scans
   - **Quick Scan Compliance**: Calculate percentage completing daily quick scans
   - **Failed Scan Investigation**: Why did scans fail? (endpoint offline, scan errors)
   - **Acceptance Criteria**: ≥95% full scan, ≥90% quick scan compliance

4. **Detection Effectiveness Assessment**:
   - **Detection Log Analysis**: Review all malware detections (last 90 days)
   - **Remediation Success Rate**: (Successful remediations / Total detections) × 100
   - **False Positive Rate**: (False positives / Total detections) × 100
   - **Re-Infection Rate**: (Re-infections / Total infections) × 100
   - **Acceptance Criteria**: Remediation success ≥95%, false positive <10%, re-infection <5%

5. **Incident Response Assessment**:
   - **Incident Timeline Review**: Review sample incidents (10 critical/high incidents)
   - **SLA Compliance**: Verify investigation, containment, remediation within SLAs
   - **Post-Incident Review Verification**: Verify lessons learned documented
   - **Acceptance Criteria**: 100% SLA compliance for critical/high incidents

6. **User Awareness Assessment**:
   - **Training Completion**: Verify ≥98% users completed annual training
   - **Phishing Simulation Results**: Review quarterly phishing simulation metrics
   - **Click Rate Trends**: Analyze click rate trends (improving or degrading)
   - **Acceptance Criteria**: Training ≥98%, phishing click rate <10% or improving trend

**Evidence Requirements**:
- Protection_Coverage.xlsx (11 worksheets)
- Anti-malware console screenshots
- Detection logs and incident reports
- Signature update compliance reports
- Scan completion logs
- Training records and phishing simulation results

**Assessment Frequency**:
- Protection coverage: Daily automated, monthly reporting
- Signature currency: Daily automated, monthly reporting
- Scan compliance: Weekly monitoring, monthly reporting
- Detection effectiveness: Monthly analysis
- Incident response: Per-incident review, quarterly trend analysis
- User awareness: Quarterly (phishing sims), annual (training)

### 3.3 A.8.18 - Use of Privileged Utility Programs Assessment

**Assessment Objectives**:
- Verify privileged utility inventory completeness (≥90% accuracy)
- Verify access controls configured (100% of utilities)
- Verify approval workflows compliance (100% access grants approved)
- Verify MFA enforcement (≥90% of privileged access)
- Verify logging coverage (≥95% of endpoints)
- Verify SIEM integration (≥95% of endpoints)
- Verify quarterly access reviews completed

**Assessment Methods**:

1. **Inventory Completeness Assessment**:
   - **Automated Discovery**: Software inventory scan for known privileged utilities
   - **Manual Discovery**: Administrator survey (what privileged utilities do you use?)
   - **Spot-Check Verification**: Manually check sample endpoints (20) for undiscovered utilities
   - **Inventory Accuracy**: (Correctly inventoried / Actual utilities) × 100
   - **Acceptance Criteria**: Inventory accuracy ≥90%

2. **Access Control Assessment**:
   - **Configuration Review**: Review AppLocker/WDAC policies, file permissions
   - **Testing**: Attempt to execute privileged utilities as unauthorized user (should be blocked)
   - **RBAC Verification**: Verify access granted through roles, not direct user assignment
   - **Coverage**: (Utilities with access controls / Total utilities) × 100
   - **Acceptance Criteria**: Access controls configured for 100% of privileged utilities

3. **Approval Workflow Assessment**:
   - **Approval Record Review**: Review sample access approvals (20 approvals)
   - **Documentation Completeness**: Verify business justification, approver, date documented
   - **Approval Authority Verification**: Verify approvals by appropriate authority (Security Manager, CISO)
   - **Acceptance Criteria**: 100% of access grants have documented approval

4. **MFA Enforcement Assessment**:
   - **Configuration Review**: Review MFA configuration for privileged access
   - **Authentication Log Analysis**: Verify MFA used for privileged sessions
   - **Testing**: Test privileged access requires MFA
   - **Coverage**: (Privileged access requiring MFA / Total privileged access) × 100
   - **Acceptance Criteria**: MFA required for ≥90% of privileged access

5. **Logging Coverage Assessment**:
   - **Logging Configuration Review**: Verify logging enabled (Windows Event Log, auditd, etc.)
   - **Log Sample Verification**: Execute privileged utility, verify log generated
   - **Log Completeness**: Verify mandatory fields present (who, what, when, where)
   - **Coverage**: (Endpoints with logging / Endpoints with privileged utilities) × 100
   - **Acceptance Criteria**: Logging coverage ≥95%

6. **SIEM Integration Assessment**:
   - **Log Forwarding Verification**: Verify logs forwarding to SIEM
   - **SIEM Correlation Rules Review**: Verify SIEM rules configured for privileged utility usage
   - **Alert Testing**: Trigger high-risk utility usage, verify SIEM alert generated
   - **Coverage**: (Endpoints forwarding to SIEM / Endpoints with privileged utilities) × 100
   - **Acceptance Criteria**: SIEM integration ≥95%

7. **Access Review Verification**:
   - **Review Documentation**: Verify quarterly access reviews conducted (last 4 quarters)
   - **Manager Attestations**: Verify managers attested to access appropriateness
   - **Access Removals**: Verify access no longer needed was removed
   - **Review Completeness**: (Privileged access reviewed / Total privileged access) × 100
   - **Acceptance Criteria**: Quarterly reviews documented, 100% access reviewed

**Evidence Requirements**:
- Privileged_Utilities.xlsx (9 worksheets)
- Access control configuration (AppLocker exports, file permissions)
- Approval records
- MFA configuration and authentication logs
- Logging configuration and log samples
- SIEM configuration and alert logs
- Quarterly access review reports

**Assessment Frequency**:
- Inventory: Quarterly discovery, annual comprehensive review
- Access controls: Annual review, post-change verification
- Approvals: Per-approval review, quarterly audit sample
- MFA: Semi-annual configuration review
- Logging: Monthly log coverage verification
- SIEM integration: Monthly verification
- Access reviews: Quarterly (ongoing), annual audit

### 3.4 A.8.19 - Installation of Software on Operational Systems Assessment

**Assessment Objectives**:
- Verify approved software list maintained and current
- Verify software approval process compliance (100% new software approved)
- Verify unauthorized software detection (daily scans, <1% unauthorized software)
- Verify application control deployment (≥90% endpoints)
- Verify change control integration (100% software installations via change control)
- Verify patch management effectiveness (critical patches within 7 days)

**Assessment Methods**:

1. **Approved Software List Assessment**:
   - **List Review**: Review approved software list for completeness and currency
   - **Annual Review Verification**: Verify list reviewed and updated within last 12 months
   - **Obsolete Software Identification**: Verify obsolete/deprecated software removed from list
   - **Acceptance Criteria**: Approved software list exists, reviewed within 12 months

2. **Approval Process Compliance Assessment**:
   - **Approval Record Review**: Review sample software approvals (20 approvals)
   - **Documentation Completeness**: Verify security review, vulnerability assessment, business justification documented
   - **Approval Authority Verification**: Verify approvals by appropriate authority
   - **Unauthorized Installation Investigation**: Investigate any software installed without approval
   - **Acceptance Criteria**: 100% of new software has documented approval

3. **Unauthorized Software Detection Assessment**:
   - **Software Inventory Analysis**: Compare installed software vs. approved software list
   - **Unauthorized Software Rate**: (Unauthorized software / Total installed software) × 100
   - **Detection Frequency**: Verify daily automated scans running
   - **Remediation Effectiveness**: Verify unauthorized software removed within 24 hours
   - **Acceptance Criteria**: <1% unauthorized software, daily scans, 100% remediated within 24 hours

4. **Application Control Deployment Assessment**:
   - **Configuration Review**: Review AppLocker/WDAC/Gatekeeper configuration
   - **Enforcement Mode Verification**: Verify enforcement mode (not just audit mode)
   - **Testing**: Attempt to execute unauthorized software (should be blocked)
   - **Coverage**: (Endpoints with application control / Total endpoints) × 100
   - **Acceptance Criteria**: Application control deployed to ≥90% endpoints, enforcement mode

5. **Change Control Integration Assessment**:
   - **Change Record Review**: Review sample software installations (20 changes)
   - **Change Ticket Verification**: Verify each installation has change ticket
   - **Testing Documentation**: Verify testing performed before production deployment
   - **Rollback Plan Verification**: Verify rollback plan documented
   - **Acceptance Criteria**: 100% software installations via change control

6. **Patch Management Assessment**:
   - **Vulnerability Scan Analysis**: Review software vulnerability scan results
   - **Critical Patch SLA Compliance**: Verify critical patches deployed within 7 days
   - **High Patch SLA Compliance**: Verify high patches deployed within 30 days
   - **EOL Software Identification**: Identify end-of-life software requiring replacement
   - **Acceptance Criteria**: Critical patches ≥95% within 7 days, high patches ≥90% within 30 days

**Evidence Requirements**:
- Software_Controls.xlsx (10 worksheets)
- Approved software list (current version)
- Software approval records
- Software inventory reports
- Unauthorized software detection reports
- Application control configuration
- Change control records
- Vulnerability scan reports

**Assessment Frequency**:
- Approved software list: Annual review
- Approval process: Per-approval review, quarterly audit sample
- Unauthorized software: Daily detection, monthly reporting
- Application control: Quarterly configuration review
- Change control: Per-change review, quarterly audit sample
- Patch management: Weekly monitoring, monthly reporting

---

## 4. Evidence Collection Framework

### 4.1 Evidence Categories

**Category 1: Automated System Outputs**
- MDM inventory exports (CSV, JSON, XML)
- Anti-malware console reports (coverage, detections, scans)
- Software inventory reports (SCCM, Intune, Jamf)
- Compliance scan results (Microsoft Defender, CIS-CAT)
- SIEM logs and alert exports

**Category 2: Manual Documentation**
- Approval records (email, ticketing system)
- Incident reports (malware, lost/stolen devices)
- Disposal certificates
- Training records
- Access review attestations

**Category 3: Configuration Artifacts**
- GPO exports (Windows baseline configurations)
- MDM profile exports (macOS, iOS, Android configurations)
- Application control policies (AppLocker, WDAC exports)
- Firewall configurations (host firewall rules)

**Category 4: Testing Evidence**
- Manual verification screenshots (encryption verification, agent verification)
- Control testing results (attempt unauthorized software execution - blocked)
- Penetration testing reports (if applicable)

### 4.2 Evidence Requirements Per Control

**A.8.1 Evidence Requirements** (8 types):
1. Endpoint inventory (Endpoint_Inventory.xlsx)
2. MDM enrollment status reports
3. Baseline compliance scan results
4. Encryption verification reports
5. Lost/stolen incident reports
6. Disposal certificates
7. BYOD user agreements
8. Manual verification samples (spot-checks)

**A.8.7 Evidence Requirements** (8 types):
1. Malware protection coverage reports (Protection_Coverage.xlsx)
2. Anti-malware console screenshots
3. Detection logs and incident reports
4. Signature update compliance reports
5. Scan completion logs
6. Training completion records
7. Phishing simulation results
8. Manual verification samples (agent checks)

**A.8.18 Evidence Requirements** (9 types):
1. Privileged utility inventory (Privileged_Utilities.xlsx)
2. Access control configuration (AppLocker, file permissions)
3. Approval records
4. MFA configuration
5. Authentication logs showing MFA usage
6. Logging configuration (Windows Event Log, auditd)
7. SIEM configuration and logs
8. Quarterly access review reports
9. Manual verification samples (access control testing)

**A.8.19 Evidence Requirements** (8 types):
1. Approved software list (Software_Controls.xlsx)
2. Software approval records
3. Software inventory reports
4. Unauthorized software detection reports
5. Application control configuration
6. Change control records
7. Vulnerability scan reports
8. Manual verification samples (application control testing)

### 4.3 Evidence Storage and Retention

**Evidence Register**:
- Each assessment workbook includes Evidence_Register worksheet
- Documents all evidence with:
  - Evidence ID (auto-generated: EVD-001, EVD-002, etc.)
  - Evidence type (automated report, manual doc, configuration, testing)
  - Description
  - Related assessment worksheet/row
  - Location (file path, URL, physical location)
  - Collection date
  - Collected by
  - Verification status

**Evidence Storage**:
- **Automated Reports**: Stored in assessment evidence folder (network share or SharePoint)
- **Configurations**: Version-controlled (Git repository for GPO/profile exports)
- **Logs**: Retained in SIEM (12 months minimum)
- **Manual Documentation**: Scanned and stored in evidence folder

**Evidence Retention**:
- **Current Assessment Evidence**: Retained until next assessment (minimum 12 months)
- **Historical Evidence**: Retained for 3 years (for trend analysis)
- **Audit Evidence**: Retained per regulatory requirements (may be longer than 3 years)

**Evidence Access Controls**:
- Read access: Security team, IT operations management, auditors
- Write access: Information Security Manager, designated security analysts
- Evidence integrity: Hash verification for critical evidence, access logging

---

## 5. Compliance Scoring Methodology

### 5.1 Per-Control Scoring

**A.8.1 - User Endpoint Devices Compliance Score**:
```
A.8.1 Score = (Inventory Completeness × 20%) + 
              (Baseline Compliance × 30%) + 
              (Encryption Coverage × 30%) + 
              (Management Enrollment × 20%)
```

**Components**:
- Inventory Completeness = (Inventoried endpoints / Actual endpoints) × 100
- Baseline Compliance = Average baseline compliance score across all endpoints
- Encryption Coverage = (Encrypted laptops/desktops / Total corporate laptops/desktops) × 100
- Management Enrollment = (Enrolled corporate devices / Total corporate devices) × 100

**A.8.7 - Protection Against Malware Compliance Score**:
```
A.8.7 Score = (Protection Coverage × 40%) + 
              (Signature Currency × 20%) + 
              (Scan Compliance × 20%) + 
              (Detection Effectiveness × 20%)
```

**Components**:
- Protection Coverage = (Protected endpoints / Total endpoints) × 100
- Signature Currency = (Current signatures / Protected endpoints) × 100
- Scan Compliance = Average of (Full scan compliance + Quick scan compliance) / 2
- Detection Effectiveness = Remediation success rate

**A.8.18 - Privileged Utility Programs Compliance Score**:
```
A.8.18 Score = (Inventory Completeness × 30%) + 
               (Access Control Effectiveness × 40%) + 
               (Logging Coverage × 30%)
```

**Components**:
- Inventory Completeness = (Inventoried utilities / Actual utilities) × 100
- Access Control Effectiveness = (Utilities with access controls / Total utilities) × 100
- Logging Coverage = (Endpoints with logging / Endpoints with privileged utilities) × 100

**A.8.19 - Software Installation Compliance Score**:
```
A.8.19 Score = (Approval Compliance × 40%) + 
               (Unauthorized Software Rate × 30%) + 
               (Application Control Deployment × 30%)
```

**Components**:
- Approval Compliance = (Approved software installations / Total installations) × 100
- Unauthorized Software Rate = (1 - Unauthorized software %) × 100 [inverted - lower is better]
- Application Control Deployment = (Endpoints with app control / Total endpoints) × 100

### 5.2 Integrated Endpoint Security Score

**Overall Endpoint Security Compliance Score**:
```
Endpoint Security Score = (A.8.1 Score × 30%) + 
                          (A.8.7 Score × 35%) + 
                          (A.8.18 Score × 15%) + 
                          (A.8.19 Score × 20%)
```

**Rationale for Weighting**:
- A.8.1: 30% - Foundation control (inventory, baselines, encryption)
- A.8.7: 35% - Highest risk (malware is primary threat vector)
- A.8.18: 15% - Specialized control (smaller scope than others)
- A.8.19: 20% - Important control (unauthorized software is significant risk)

### 5.3 Compliance Thresholds

| Score Range | Status | Color Code | Action Required |
|-------------|--------|------------|-----------------|
| **≥90%** | Compliant | 🟢 Green | Maintain, continuous improvement |
| **70-89%** | Partial Compliance | 🟡 Yellow | Remediation plan required, target 90% within 90 days |
| **<70%** | Non-Compliant | 🔴 Red | Immediate remediation plan, executive escalation |

**Per-Endpoint Risk Scoring**:
For risk prioritization, endpoints scored on combination of gaps:
- **Critical Risk**: Unencrypted + unprotected (no malware protection)
- **High Risk**: Single critical control failure on high-criticality endpoint
- **Medium Risk**: Single control failure on standard endpoint
- **Low Risk**: Partial compliance, planned remediation

---

## 6. Gap Analysis and Remediation

### 6.1 Gap Classification

**Gap Severity Levels**:

| Severity | Definition | Examples | Remediation SLA |
|----------|------------|----------|-----------------|
| **Critical** | Complete control failure on high-criticality endpoint, multiple control failures creating critical risk | Unencrypted + unprotected executive laptop, ransomware on unprotected server | 7 days |
| **High** | Single critical control failure, widespread non-compliance | 20% of endpoints unprotected, privileged utilities with no access controls | 30 days |
| **Medium** | Single control failure on standard endpoint, partial compliance | Single endpoint missing encryption, outdated malware signatures >48 hours | 60 days |
| **Low** | Minor deviation, low-risk non-compliance | Baseline config drift on non-critical setting, unused privileged utility access | 90 days |

### 6.2 Gap Remediation Framework

**Remediation Process**:

1. **Gap Identification** (Assessment Phase):
   - Assessment identifies gap
   - Gap documented in Compliance_Matrix.xlsx (Gap_Analysis worksheet)
   - Gap assigned severity (Critical/High/Medium/Low)
   - Gap assigned unique ID (GAP-001, GAP-002, etc.)

2. **Risk Assessment** (Week 1):
   - Information Security Manager assesses risk (likelihood, impact)
   - Determine if gap requires immediate remediation or can be scheduled
   - Determine if compensating controls exist

3. **Remediation Planning** (Week 1-2):
   - Assign remediation owner (usually IT Operations Manager)
   - Remediation owner develops plan:
     - Root cause analysis
     - Remediation approach
     - Timeline and milestones
     - Resources required
   - Plan reviewed and approved by Information Security Manager

4. **Remediation Execution** (Per SLA):
   - Remediation owner executes plan
   - Progress tracked weekly (status updates in Compliance_Matrix.xlsx)
   - Blockers escalated to Information Security Manager

5. **Remediation Verification** (Post-Implementation):
   - Security Analyst verifies gap closed
   - Re-run relevant assessment (e.g., re-scan for malware protection)
   - Update assessment workbooks

6. **Documentation and Closure** (Final Step):
   - Document remediation in Compliance_Matrix.xlsx
   - Update gap status to "Closed"
   - Lessons learned captured

**Remediation Tracking**:
- **Weekly**: Remediation owner provides status update
- **Monthly**: Information Security Manager reviews all open gaps, escalates overdue gaps
- **Quarterly**: Executive dashboard includes gap remediation metrics

### 6.3 Remediation Metrics

**Key Metrics**:
- **Total Open Gaps**: Count by severity (Critical/High/Medium/Low)
- **Gap Age**: Days since gap identified (track overdue gaps)
- **Remediation Time**: Average days from gap identification to closure
- **Gap Recurrence Rate**: Percentage of gaps that recur after closure
- **Remediation Success Rate**: Percentage of gaps closed successfully vs. risk-accepted

**Target Metrics**:
- Zero critical gaps (target)
- High gaps remediated within 30 days (≥95% compliance)
- Medium gaps remediated within 60 days (≥90% compliance)
- Average remediation time trending down (continuous improvement)

---

## 7. Assessment Workbook Framework

### 7.1 Workbook Generation Approach

**Python-Generated Workbooks**:
- All assessment workbooks generated via Python scripts (not manual Excel creation)
- Ensures consistency, repeatability, version control
- Scripts located in: 50_scripts-excel/

**Standard Workbook Features** (All 13 A.8.23 Enhancements):
1. Instructions & Legend worksheet (first sheet)
2. Evidence Register worksheet
3. Capability Requirements mapping
4. Integration Architecture (where applicable)
5. Performance Metrics (where applicable)
6. Licensing & Support tracking
7. Enhanced Gap Analysis (with budget, status tracking)
8. Approval Sign-Off workflow
9. Comprehensive data validations (60+ dropdowns)
10. Visual consistency (standard color palette)
11. Standard formulas (compliance rates, coverage %, gap counts)
12. Technology comparison support
13. Exception handling (multi-state statuses)

### 7.2 Assessment Workbooks

**Workbook 1: Endpoint Inventory (A.8.1)**  
**Script**: generate_assessment_1_endpoint_inventory.py  
**Output**: Endpoint_Inventory.xlsx

**Worksheets** (9):
1. Instructions_Legend: How to use workbook, status legend, evidence examples
2. Inventory: Complete endpoint inventory (Device ID, Hostname, Type, OS, Owner, etc.)
3. Classification: Device type distribution, ownership model analysis
4. Baseline_Compliance: Per-endpoint baseline compliance (OS hardening, firewall, encryption, etc.)
5. Encryption_Status: Encryption technology, status, key escrow
6. Management_Enrollment: MDM platform, enrollment status, capabilities
7. Capability_Requirements: Policy requirements → implementation mapping
8. Evidence_Register: All evidence documented (EVD-001, EVD-002, etc.)
9. Summary: Executive dashboard (KPIs, charts, compliance metrics)

**Workbook 2: Protection Coverage (A.8.7)**  
**Script**: generate_assessment_2_protection_coverage.py  
**Output**: Protection_Coverage.xlsx

**Worksheets** (11):
1. Instructions_Legend
2. Coverage_Analysis: Per-endpoint protection status (agent installed, agent version, signatures)
3. Agent_Status: Agent health, communication status
4. Scan_Compliance: Full scan compliance, quick scan compliance
5. Detection_Metrics: Malware detections by type, severity
6. Incident_Response: Malware incidents, response times, SLA compliance
7. Performance_Metrics: False positives, scan performance impact
8. User_Awareness: Training completion, phishing simulation results
9. Licensing_Support: License status, support contracts, expirations
10. Evidence_Register
11. Summary: Executive dashboard

**Workbook 3: Software Controls (A.8.19)**  
**Script**: generate_assessment_3_software_controls.py  
**Output**: Software_Controls.xlsx

**Worksheets** (10):
1. Instructions_Legend
2. Approved_Software: Approved software list (name, version, approval date, approver)
3. Installed_Software: Installed software per endpoint (from inventory tools)
4. Unauthorized_Detection: Unauthorized software identified (daily scans)
5. Application_Control: Application control deployment status per endpoint
6. Software_Approvals: Approval workflow tracking (requests, approvals, denials)
7. Patch_Management: Software vulnerability status, patch compliance
8. Licensing_Support: Software licenses, expirations
9. Evidence_Register
10. Summary: Executive dashboard

**Workbook 4: Privileged Utilities (A.8.18)**  
**Script**: generate_assessment_4_privileged_utilities.py  
**Output**: Privileged_Utilities.xlsx

**Worksheets** (9):
1. Instructions_Legend
2. Utility_Inventory: Privileged utility inventory (name, platform, risk level, location)
3. Access_Controls: Access control configuration per utility (RBAC, AppLocker, file permissions)
4. Approval_Workflow: Access approvals (standing, temporary, JIT, emergency)
5. Usage_Logs: Privileged utility usage summary (who, what, when, where)
6. SIEM_Integration: Log forwarding status, SIEM correlation rules
7. Security_Bypass_Tools: Tools that bypass security controls (identified, restricted)
8. Evidence_Register
9. Summary: Executive dashboard

**Workbook 5: Compliance Matrix (Integrated)**  
**Script**: generate_assessment_5_compliance_status.py  
**Output**: Compliance_Matrix.xlsx

**Worksheets** (11):
1. Instructions_Legend
2. Endpoint_Compliance: Per-endpoint compliance across all 4 controls (A.8.1, A.8.7, A.8.18, A.8.19)
3. Control_Scores: Compliance scores per control
4. Gap_Analysis: All gaps identified (GAP-001, GAP-002, etc.), severity, status
5. Remediation_Tracking: Gap remediation progress (owner, plan, timeline, status)
6. Risk_Prioritization: Endpoints prioritized by risk (combination of gaps)
7. Trend_Analysis: Compliance trends over time (if historical data available)
8. Integration_Architecture: How endpoint controls integrate with other ISMS controls
9. Approval_Sign_Off: Assessment approval workflow (Assessor → ISO → CISO)
10. Evidence_Register
11. Summary: Integrated executive dashboard

**Workbook 6: Endpoint Security Dashboard (Consolidated)**  
**Script**: generate_dashboard_endpoint_security.py  
**Output**: Endpoint_Security_Dashboard.xlsx

**Worksheets** (7):
1. Instructions_Legend
2. Executive_Summary: High-level compliance across all 4 controls, critical gaps
3. Control_Breakdown: Detailed metrics per control (A.8.1, A.8.7, A.8.18, A.8.19)
4. Endpoint_Overview: Total endpoints, by type, by ownership model, by criticality
5. Gap_Status: Gap remediation status (open, in progress, closed, risk accepted)
6. Trends: Compliance trends over time, gap remediation trends
7. Evidence_Summary: Evidence collected, evidence register summary

### 7.3 Workbook Data Flow

**Data Sources → Workbooks**:
```
MDM APIs (Intune, Jamf, SCCM) → Workbook 1 (Endpoint Inventory)
Anti-malware Console → Workbook 2 (Protection Coverage)
Software Inventory Tools → Workbook 3 (Software Controls)
Software Approval System + PAM Logs → Workbook 4 (Privileged Utilities)
Workbooks 1-4 → Workbook 5 (Compliance Matrix - consolidation)
Workbook 5 → Workbook 6 (Dashboard - executive view)
```

**Normalization Script**:
- `normalize_endpoint_security_assessments.py`
- Normalizes data from various tools (different MDMs, different EDRs)
- Converts vendor-specific formats to standardized assessment format
- Validates data integrity before workbook generation

---

## 8. Continuous Assessment Approach

### 8.1 Continuous Monitoring

**Daily Monitoring**:
- Software inventory updates (detect new software installations)
- Malware detection monitoring (SIEM alerts)
- Signature update monitoring (flag outdated signatures)
- Privileged utility usage monitoring (SIEM correlation)

**Weekly Monitoring**:
- Baseline compliance scans (configuration drift detection)
- Scan compliance verification (full scans completed)
- Protection coverage monitoring (unprotected endpoints)
- New endpoint discovery (network scans)

**Monthly Monitoring**:
- Comprehensive metrics reporting (all controls)
- Gap remediation progress review
- Trend analysis (compliance improving or degrading)
- Evidence collection and documentation

**Quarterly Monitoring**:
- Targeted re-assessment (high-risk areas)
- Access reviews (privileged utilities)
- Software list review (approved software)
- Executive dashboard update

### 8.2 Automated vs. Manual Assessment

**Automated Assessment** (Preferred):
- Endpoint inventory (MDM APIs, network scans)
- Baseline compliance (MDM compliance reports, CIS-CAT)
- Malware protection coverage (anti-malware console APIs)
- Software inventory (SCCM, Intune APIs)
- Logging coverage (SIEM integration status)

**Manual Assessment** (When Necessary):
- Spot-check verification (sample endpoints)
- Encryption verification (visual verification)
- Control effectiveness testing (attempt unauthorized software execution)
- Incident investigation (malware incidents)
- Gap root cause analysis

**Balance**:
- Automated assessment: 80% (continuous, consistent, scalable)
- Manual assessment: 20% (verification, edge cases, investigation)

### 8.3 Continuous Improvement Cycle

**Improvement Process**:
```
1. Collect Metrics (Monthly)
2. Analyze Trends (Quarterly)
   ↓
3. Identify Improvement Opportunities
   ↓
4. Develop Improvement Plans
   ↓
5. Implement Improvements
   ↓
6. Measure Effectiveness
   ↓
[Loop back to Collect Metrics]
```

**Improvement Examples**:
- **Compliance Declining**: Why? Root cause analysis → Remediation
- **Specific Gap Recurring**: Process gap? → Process improvement
- **Malware Detections Increasing**: Why? User training? Email filtering? → Targeted improvement
- **Unauthorized Software Rate High**: Application control not working? → Technology or process improvement

**Improvement Tracking**:
- Improvement opportunities documented
- Improvement plans with owners and timelines
- Improvement effectiveness measured
- Results reported to management

---

## 9. Audit Verification Procedures

### 9.1 Internal Audit Procedures

**Internal Audit Frequency**: Annual minimum

**Internal Audit Scope**:
- Verify assessment methodology followed
- Verify evidence complete and accurate
- Verify compliance scores calculated correctly
- Verify gap remediation tracking
- Spot-check sample endpoints for compliance

**Internal Audit Process**:
1. **Planning**: Define audit scope, select sample endpoints/evidence
2. **Evidence Review**: Review assessment workbooks, evidence register
3. **Sample Testing**: Spot-check sample (20 endpoints, 10 approvals, 5 incidents)
4. **Interviews**: Interview security team, endpoint administrators
5. **Findings**: Document findings (compliance, observations, opportunities)
6. **Reporting**: Present findings to CISO, management
7. **Follow-Up**: Track remediation of audit findings

### 9.2 External Audit Procedures (ISO 27001 Certification)

**External Audit Frequency**: Annual surveillance audit, triennial recertification

**External Audit Preparation**:
- Generate all 6 assessment workbooks (current data)
- Update evidence register (ensure all evidence documented and accessible)
- Prepare sample of key evidence (spot-check materials)
- Brief personnel on audit process and expectations

**Auditor Verification Steps** (Typical):

1. **Policy Review**:
   - Review Master Framework, S1-S6 policy documents
   - Verify policy completeness and currency

2. **Evidence Review**:
   - Review all 6 assessment workbooks
   - Review evidence register
   - Spot-check evidence samples (certificates, logs, approvals)

3. **Sample Testing**:
   - Select random sample of endpoints (20 endpoints)
   - Verify inventory accuracy (endpoint exists, attributes correct)
   - Verify baseline compliance (manual configuration check)
   - Verify malware protection (agent running, signatures current)
   - Verify encryption (boot endpoint, verify pre-boot auth)

4. **Control Testing**:
   - Test access controls (attempt unauthorized software execution - should be blocked)
   - Test privileged utility access controls (unauthorized user - should be blocked)
   - Verify MFA enforcement (test privileged access requires MFA)

5. **Process Review**:
   - Review approval workflows (sample approvals - properly documented?)
   - Review incident response (sample incidents - properly handled?)
   - Review gap remediation (gaps remediated per SLA?)

6. **Interviews**:
   - Security team: Understanding of assessment methodology
   - Endpoint administrators: Knowledge of baseline requirements
   - Users: Awareness of security responsibilities (sample 5 users)

**Auditor Acceptance Criteria**:
- All evidence available and complete
- Compliance scores meet thresholds (≥90% target)
- Sample testing confirms automated reporting accuracy
- Personnel demonstrate understanding of procedures
- Processes followed per documented methodology
- Gaps remediated per SLAs
- Continuous improvement demonstrated

### 9.3 Assessment Quality Assurance

**Quality Assurance Process**:
- **Pre-Assessment Review**: Ensure assessment tools prepared, stakeholders briefed
- **Data Validation**: Verify data integrity before workbook generation (normalization script)
- **Workbook Review**: Information Security Manager reviews workbooks for completeness before distribution
- **Evidence Verification**: Spot-check evidence samples (10% of evidence) for accuracy
- **Calculation Verification**: Verify compliance score calculations correct (manual check of formulas)
- **Stakeholder Review**: Stakeholders review draft workbooks before final publication
- **Final Approval**: CISO approves final assessment before distribution to management/auditors

**Quality Metrics**:
- Assessment completion on schedule (target: 100%)
- Evidence completeness (target: 100% of required evidence collected)
- Assessment accuracy (spot-check verification: target ≥95% accuracy)
- Stakeholder satisfaction (survey after assessment: target ≥4/5)

---

## 10. Summary and Next Steps

### 10.1 Assessment Framework Summary

This assessment framework provides:
- **Systematic Methodology**: Repeatable process for endpoint security assessment
- **Integrated Approach**: Single assessment serves all 4 controls (A.8.1, A.8.7, A.8.18, A.8.19)
- **Technology-Agnostic**: Works across any endpoint environment
- **Automation-First**: Python-generated workbooks for consistency
- **Evidence-Based**: Comprehensive evidence collection and documentation
- **Continuous**: Ongoing monitoring, not just point-in-time assessment
- **Audit-Ready**: Structured evidence for certification audits

### 10.2 Implementation Roadmap

**Initial Implementation** (Months 1-3):
1. Prepare assessment tools (Python scripts, data collection procedures)
2. Execute initial comprehensive assessment
3. Generate all 6 workbooks
4. Identify gaps and create remediation plans
5. Present findings to management

**Continuous Operation** (Ongoing):
1. Daily/weekly/monthly automated monitoring
2. Quarterly targeted re-assessments
3. Annual comprehensive re-assessments
4. Continuous gap remediation
5. Continuous improvement

**Annual Cycle**:
- Q1: Annual comprehensive assessment, gap remediation planning
- Q2: Quarterly refresh, remediation execution
- Q3: Quarterly refresh, mid-year management review
- Q4: Quarterly refresh, year-end reporting, audit preparation

### 10.3 Success Criteria

**Assessment Program Success Indicators**:
- Assessments completed on schedule (100% on-time completion)
- Evidence completeness (100% required evidence collected)
- Compliance scores improving over time (year-over-year improvement)
- Gap remediation on track (≥95% gaps remediated within SLA)
- Audit findings decreasing (fewer findings each audit)
- Management satisfaction (effective use of assessment data for decisions)

**Control Implementation Success Indicators**:
- A.8.1 compliance ≥90%
- A.8.7 compliance ≥90%
- A.8.18 compliance ≥90%
- A.8.19 compliance ≥90%
- Overall endpoint security compliance ≥90%
- Zero critical gaps
- ISO 27001 certification audit passed (no non-conformances)

---

**END OF SECTION 6**

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial assessment methodology framework |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

**Policy Layer Complete**: This completes the policy layer for the Endpoint Security Framework (A.8.1, A.8.7, A.8.18, A.8.19)

**Next Phase**: Implementation documents (ISMS-IMP-A.8.1-7-18-19-S1 through S6)
# ISMS-IMP-A.8.12.4 - Monitoring & Response Assessment

## DOC CONTROL

| **Attribute**           | **Details**                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Document ID**         | ISMS-IMP-A.8.12.4                                                          |
| **Document Title**      | Monitoring & Response Assessment Workbook Specification                     |
| **Control Reference**   | ISO/IEC 27001:2022 - Control A.8.12 (Data Leakage Prevention)             |
| **Related Policy**      | ISMS-POL-A.8.12-S2.3 (Monitoring & Detection), ISMS-POL-A.8.12-S2.4 (Incident Response) |
| **Document Type**       | Implementation Assessment Specification                                     |
| **Version**             | 1.0                                                                        |
| **Status**              | Draft                                                                      |
| **Effective Date**      | 2025-01-06                                                                 |
| **Review Cycle**        | Quarterly                                                                  |
| **Document Owner**      | Chief Information Security Officer (CISO)                                  |
| **Approved By**         | CISO, SOC Lead, DPO                                                        |
| **Classification**      | Internal Use                                                               |

### Revision History

| **Version** | **Date**   | **Author**        | **Changes**                          |
|-------------|------------|-------------------|--------------------------------------|
| 1.0         | 2025-01-06 | ISMS Project Team | Initial specification for Domain 4   |

### Related Documents

| **Document ID**              | **Title**                                      | **Relationship**        |
|------------------------------|------------------------------------------------|-------------------------|
| ISMS-POL-A.8.12              | Data Leakage Prevention Policy (Master)        | Parent Policy           |
| ISMS-POL-A.8.12-S2.3         | Monitoring & Detection Requirements            | Direct Mapping          |
| ISMS-POL-A.8.12-S2.4         | Incident Response & Remediation                | Direct Mapping          |
| ISMS-IMP-A.8.12.1            | DLP Infrastructure Assessment                  | Related Assessment      |
| ISMS-IMP-A.8.12.3            | Channel Coverage Assessment                    | Related Assessment      |
| ISMS-IMP-A.8.12.5            | Compliance Dashboard                           | Consolidation Target    |

---

## 1. PURPOSE & SCOPE

### 1.1 Purpose

This document specifies the structure and requirements for the **Monitoring & Response Assessment Workbook**, which evaluates the organization's capability to detect, alert, triage, investigate, and respond to DLP policy violations.

**Key Assessment Areas:**
- DLP logging configuration and completeness
- Alert rule configuration and severity classification
- SIEM integration and correlation rules
- False positive management and tuning processes
- Incident response workflows and SLA compliance
- SOC integration and escalation procedures
- Dashboard and reporting capabilities

**Critical Principle (Feynman):**  
*"Detection without response is security theater. Monitoring without tuning is alert fatigue."*

Organizations that deploy DLP without effective monitoring generate thousands of alerts that nobody investigates - creating a false sense of security while actual data leakage goes undetected.

### 1.2 Scope

**In Scope:**
- All DLP alerting and monitoring capabilities
- SOC triage and escalation workflows
- SIEM correlation rules and use cases
- False positive tracking and tuning procedures
- Incident response SLA compliance
- Executive and operational dashboards
- User notification and education processes

**Out of Scope:**
- General SOC operations (covered by ISMS-POL-A.8.16)
- General logging policy (covered by ISMS-POL-A.8.15)
- Network monitoring (covered by ISMS-POL-A.8.16)
- DLP technology deployment (covered by ISMS-IMP-A.8.12.1)

### 1.3 Relationship to DLP Framework

Domain 4 is the **operational effectiveness layer** of the DLP framework:
```
ISMS-IMP-A.8.12.1 (Infrastructure) → What DLP tools exist
ISMS-IMP-A.8.12.2 (Classification) → What data to protect
ISMS-IMP-A.8.12.3 (Channels) → Where to protect data
ISMS-IMP-A.8.12.4 (Monitoring) ← YOU ARE HERE → Detect violations
ISMS-IMP-A.8.12.5 (Dashboard) → Overall compliance
```

**Dependency Chain:**
- Requires DLP infrastructure (Domain 1) to generate alerts
- Requires channel coverage (Domain 3) to have monitoring points
- Feeds into compliance dashboard (Domain 5) for KPI tracking

---

## 2. ASSESSMENT METHODOLOGY

### 2.1 Assessment Approach

**System Engineering Principle:**  
Each assessment criterion evaluates **operational effectiveness**, not checkbox compliance.

**Response Values:**
- **Yes** = Fully implemented, documented, measured with evidence
- **No** = Not implemented or significant gaps exist
- **Partial** = Partially implemented, some gaps remain
- **Planned** = Scheduled for implementation (provide target date)
- **N/A** = Not applicable (provide justification)

**FORBIDDEN VALUE:** "Maybe" is NOT allowed (Feynman principle: either you know or you don't).

### 2.2 Evidence Requirements

All assessment responses SHALL be supported by evidence:

**Mandatory Evidence Types:**
- **Logging Evidence:** SIEM screenshots showing DLP log ingestion
- **Alert Evidence:** Sample alerts (Critical/High/Medium/Low severity)
- **SIEM Correlation Rules:** Screenshots or config exports
- **False Positive Metrics:** FP rate dashboard or reports
- **Incident Response Documentation:** Sample IR tickets with timestamps
- **SOC Playbooks:** Alert triage procedures and escalation workflows
- **Dashboard Screenshots:** Executive and operational dashboards
- **SLA Compliance Reports:** MTTD/MTTR metrics and trending

**Evidence Naming Convention:**
```
A812-4-[CATEGORY]-[###]

Examples:
A812-4-LOG-001  (Logging evidence)
A812-4-ALT-001  (Alert configuration)
A812-4-SIEM-001 (SIEM integration)
A812-4-FP-001   (False positive management)
A812-4-IR-001   (Incident response)
A812-4-DASH-001 (Dashboard evidence)
```

### 2.3 Assessment Frequency

- **Initial Assessment:** During DLP implementation (Months 3-6)
- **Quarterly Reviews:** Update metrics, FP rate, SLA compliance
- **Post-Incident:** After significant DLP incidents or breaches
- **Annual Audit:** Comprehensive review for ISO 27001 compliance

---

## 3. WORKBOOK STRUCTURE

### 3.1 Sheet Overview

| **#** | **Sheet Name**              | **Purpose**                                    | **Rows** |
|-------|-----------------------------|------------------------------------------------|----------|
| 1     | Instructions_Legend         | How to use workbook, legend, metadata         | 50       |
| 2     | Logging_Configuration       | DLP logging requirements per channel           | 25       |
| 3     | Alert_Rules_Inventory       | All configured DLP alert rules                 | 30       |
| 4     | Alert_Volume_Metrics        | Daily/weekly/monthly alert statistics          | 20       |
| 5     | SIEM_Integration            | Log forwarding, correlation rules, use cases   | 25       |
| 6     | False_Positive_Management   | FP rate tracking, tuning procedures            | 20       |
| 7     | Incident_Response_Workflow  | Triage, containment, investigation procedures  | 25       |
| 8     | SOC_Integration             | Alert workflow, escalation, SLAs               | 20       |
| 9     | Dashboards_Reporting        | Executive, operational, compliance dashboards  | 20       |
| 10    | Gap_Analysis                | Identified deficiencies and remediation plans  | 40       |
| 11    | Evidence_Register           | Audit trail and evidence tracking              | 100      |
| 12    | Summary_Dashboard           | KPIs, compliance score, executive summary      | 30       |

**Total Assessment Items:** ~70 monitoring and response checkpoints

---

## 4. SHEET SPECIFICATIONS

### 4.1 Sheet: Instructions_Legend

**Purpose:** Provide user guidance and assessment metadata.

**Content Sections:**

1. **Document Header**
   - Workbook ID: ISMS-IMP-A.8.12.4
   - Assessment Area: Monitoring & Response
   - Related Policies: ISMS-POL-A.8.12-S2.3, ISMS-POL-A.8.12-S2.4
   - Version: 1.0

2. **Organization Metadata** (Yellow input fields)
   - Assessment Date
   - Completed By (Name, Role)
   - Organization Name
   - Review Cycle: Quarterly

3. **How to Use This Workbook**
   - Complete Logging_Configuration first (foundational)
   - Then complete Alert_Rules_Inventory (what alerts exist)
   - Document SIEM_Integration (log forwarding, correlation)
   - Track False_Positive_Management metrics (FP rate, tuning)
   - Verify Incident_Response_Workflow and SOC_Integration
   - Review Dashboards_Reporting capabilities
   - Identify gaps and create remediation plans
   - Evidence ID format: A812-4-[CATEGORY]-[###]

4. **Legend - Response Values**
   - Yes = ✅ Green (Fully implemented, measured, evidence available)
   - No = ❌ Red (Not implemented or significant gaps)
   - Partial = ⚠️ Yellow (Partially implemented, gaps remain)
   - Planned = 📋 Blue (Scheduled, provide target date)
   - N/A = ⚪ Gray (Not applicable, provide justification)

5. **Alert Severity Classification** (from ISMS-POL-A.8.12-S2.3)
   - Critical: Active data exfiltration, credentials detected (SLA: 15 min)
   - High: PII/IP transferred externally without encryption (SLA: 1 hour)
   - Medium: Confidential data transfer requiring review (SLA: 4 hours)
   - Low: Policy violation, tuning needed (SLA: 24 hours)
   - Informational: Monitoring-only events (No SLA)

**Layout:** Informational only, no data entry rows.

---

### 4.2 Sheet: Logging_Configuration

**Purpose:** Document DLP logging requirements per channel.

**Assessment Questions (25 rows):**

| # | Requirement | Yes/No/Partial/Planned/N/A | Evidence ID | Notes |
|---|-------------|----------------------------|-------------|-------|
| 1 | Are all DLP channels configured to log events? | | | |
| 2 | Email DLP: Logs sent/received/blocked emails with metadata? | | | |
| 3 | Web DLP: Logs uploads/downloads/blocked web traffic? | | | |
| 4 | Endpoint DLP: Logs USB/print/screen capture/clipboard events? | | | |
| 5 | Network DLP: Logs file transfers (FTP/SMB/SCP)? | | | |
| 6 | Application DLP: Logs database exports/API calls? | | | |
| 7 | Mobile DLP: Logs mobile app usage and data transfers? | | | |
| 8 | Do logs include user identity (username, email, employee ID)? | | | |
| 9 | Do logs include timestamp (ISO 8601 format)? | | | |
| 10 | Do logs include source (IP, hostname, device ID)? | | | |
| 11 | Do logs include destination (recipient, URL, file path)? | | | |
| 12 | Do logs include data classification level (if available)? | | | |
| 13 | Do logs include policy violated (rule ID, rule name)? | | | |
| 14 | Do logs include action taken (allow/alert/block/quarantine)? | | | |
| 15 | Do logs include file metadata (filename, size, hash)? | | | |
| 16 | Are logs retained for minimum 12 months (FADP requirement)? | | | |
| 17 | Are logs protected from unauthorized modification? | | | |
| 18 | Are logs encrypted in transit (TLS to SIEM)? | | | |
| 19 | Are logs encrypted at rest (SIEM storage)? | | | |
| 20 | Is log integrity verified (checksums, digital signatures)? | | | |
| 21 | Are logs reviewed for completeness (missing log gaps)? | | | |
| 22 | Are logs backed up (separate from production logs)? | | | |
| 23 | Is log access restricted (RBAC, audit trail of log access)? | | | |
| 24 | Are logs parsed correctly by SIEM (no parsing errors)? | | | |
| 25 | Are logs correlated with other security events (IAM, EDR, Network)? | | | |

**Columns:**
- A: Requirement ID (1-25)
- B: Requirement Description (wrap text)
- C: Compliance Status (Dropdown: Yes/No/Partial/Planned/N/A)
- D: Evidence ID (A812-4-LOG-###)
- E: Notes (free text, issues, target dates)

**Pre-Populated Examples:** 3 gray rows showing sample responses.

---

### 4.3 Sheet: Alert_Rules_Inventory

**Purpose:** Complete inventory of all configured DLP alert rules.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Alert Rule ID             | Text         | User input (ALT-001, ALT-002)      | 15        |
| B       | Rule Name                 | Text         | User input                         | 30        |
| C       | Channel                   | Dropdown     | Email/Web/Endpoint/Network/App/Mobile | 18        |
| D       | Severity                  | Dropdown     | Critical/High/Medium/Low/Info      | 12        |
| E       | Detection Method          | Dropdown     | Pattern/Keyword/Fingerprint/Contextual/ML | 18        |
| F       | Policy Action             | Dropdown     | Allow/Alert/Block/Quarantine/Encrypt | 15        |
| G       | Alert Destination         | Dropdown     | SIEM/Email/SMS/Ticketing/Dashboard | 18        |
| H       | Response SLA              | Dropdown     | 15min/1hr/4hr/24hr/No SLA          | 12        |
| I       | Last Tuned Date           | Date         | User input                         | 15        |
| J       | False Positive Rate %     | Number       | User input (e.g., 5.2%)            | 15        |
| K       | Alert Volume (Last 30d)   | Number       | User input                         | 15        |
| L       | Rule Status               | Dropdown     | Active/Disabled/Testing/Deprecated | 15        |
| M       | Evidence ID               | Text         | User input (A812-4-ALT-###)        | 18        |

**Data Rows:** 30 rows (5 pre-populated examples + 25 blank)

**Pre-Populated Alert Rule Examples:**

1. **ALT-001 | Credentials Detected - Email | Email | Critical | Pattern | Block | SIEM,SMS | 15min | 2025-01-01 | 2.1% | 45 | Active**
2. **ALT-002 | PII to External Domain | Email | High | Fingerprint | Alert | SIEM,Email | 1hr | 2024-12-15 | 8.5% | 230 | Active**
3. **ALT-003 | Source Code to GitHub | Web | High | Keyword | Block | SIEM,Ticketing | 1hr | 2025-01-03 | 1.2% | 12 | Active**
4. **ALT-004 | Mass USB Copy (>1GB) | Endpoint | Critical | Contextual | Block | SIEM,SMS | 15min | 2024-11-20 | 0.5% | 3 | Active**
5. **ALT-005 | Bulk Database Export | Application | High | ML | Alert | SIEM,Email | 1hr | 2024-12-28 | 4.3% | 67 | Active**

---

### 4.4 Sheet: Alert_Volume_Metrics

**Purpose:** Track DLP alert volume over time (daily, weekly, monthly).

**Content Sections:**

1. **Alert Volume by Severity (Last 30 Days)**

| Severity | Total Alerts | Avg per Day | Blocked | Alerted | False Positives | FP Rate % |
|----------|--------------|-------------|---------|---------|-----------------|-----------|
| Critical | [Formula: SUM from Alert_Rules_Inventory] | [Formula: /30] | | | | [Formula] |
| High | [Formula] | [Formula] | | | | [Formula] |
| Medium | [Formula] | [Formula] | | | | [Formula] |
| Low | [Formula] | [Formula] | | | | [Formula] |
| Info | [Formula] | [Formula] | | | | [Formula] |
| **TOTAL** | [Formula: SUM] | [Formula] | | | | [Formula] |

2. **Alert Volume by Channel (Last 30 Days)**

| Channel | Total Alerts | Blocked | Alerted | FP Rate % | Top Rule Name |
|---------|--------------|---------|---------|-----------|---------------|
| Email | | | | | |
| Web | | | | | |
| Endpoint | | | | | |
| Network | | | | | |
| Application | | | | | |
| Mobile | | | | | |

3. **Alert Trend Analysis**

| Week | Critical | High | Medium | Low | Total | FP Rate % | Notes |
|------|----------|------|--------|-----|-------|-----------|-------|
| Week 1 (Dec 2-8) | | | | | | | |
| Week 2 (Dec 9-15) | | | | | | | |
| Week 3 (Dec 16-22) | | | | | | | |
| Week 4 (Dec 23-29) | | | | | | | |

**Calculation Formulas:**
- FP Rate % = (False Positives / Total Alerts) × 100
- Avg per Day = Total Alerts / 30

---

### 4.5 Sheet: SIEM_Integration

**Purpose:** Assess SIEM integration, log forwarding, and correlation rules.

**Assessment Questions (25 rows):**

| # | Requirement | Yes/No/Partial/Planned/N/A | Evidence ID | Notes |
|---|-------------|----------------------------|-------------|-------|
| 1 | Are DLP logs forwarded to organizational SIEM? | | | |
| 2 | Is log forwarding encrypted (TLS/SSL)? | | | |
| 3 | Is log forwarding reliable (no dropped logs >1%)? | | | |
| 4 | Are DLP logs parsed correctly in SIEM (no parsing errors)? | | | |
| 5 | Are DLP logs normalized (common schema: CEF, Syslog, JSON)? | | | |
| 6 | Are DLP events indexed for search and analysis? | | | |
| 7 | Is log retention in SIEM ≥12 months? | | | |
| 8 | Are SIEM correlation rules configured for DLP events? | | | |
| 9 | Correlation: DLP + Malware detection = compromised endpoint? | | | |
| 10 | Correlation: DLP + Failed logins = credential theft? | | | |
| 11 | Correlation: DLP + VPN from foreign country = account compromise? | | | |
| 12 | Correlation: DLP + HR termination record = insider threat? | | | |
| 13 | Are SIEM use cases documented (insider threat, compromised creds)? | | | |
| 14 | Are SIEM dashboards configured for DLP (real-time alert queue)? | | | |
| 15 | Are SIEM alerts integrated with ticketing system (ServiceNow, Jira)? | | | |
| 16 | Are DLP Critical alerts automatically escalated to SOC? | | | |
| 17 | Are DLP High alerts automatically assigned to analysts? | | | |
| 18 | Is DLP log ingestion monitored (alerts for log failures)? | | | |
| 19 | Is SIEM performance adequate (query response time <10 sec)? | | | |
| 20 | Are SIEM search queries documented (common investigations)? | | | |
| 21 | Is SIEM access restricted (RBAC, SOC analysts only)? | | | |
| 22 | Are SIEM searches audited (who searched for what)? | | | |
| 23 | Is SIEM backup configured (disaster recovery)? | | | |
| 24 | Are SIEM correlation rules tested (validation, false positive rate)? | | | |
| 25 | Are SIEM correlation rules tuned quarterly? | | | |

**Pre-Populated Examples:** 3 gray rows.

---

### 4.6 Sheet: False_Positive_Management

**Purpose:** Track false positive rate and tuning procedures.

**Assessment Questions (20 rows):**

| # | Requirement | Yes/No/Partial/Planned/N/A | Evidence ID | Notes |
|---|-------------|----------------------------|-------------|-------|
| 1 | Is false positive rate measured per alert rule? | | | |
| 2 | Is overall FP rate <10% (target from ISMS-POL-A.8.12-S2.3)? | | | |
| 3 | Are false positives tracked in ticketing system? | | | |
| 4 | Is FP rate trended over time (monthly)? | | | |
| 5 | Are users able to report false positives (self-service portal)? | | | |
| 6 | Are false positive reports triaged within 24 hours? | | | |
| 7 | Are false positives investigated (root cause analysis)? | | | |
| 8 | Are DLP rules tuned based on FP analysis? | | | |
| 9 | Are legitimate business flows whitelisted (permanent exceptions)? | | | |
| 10 | Are whitelists documented (justification, approver, review date)? | | | |
| 11 | Are whitelists reviewed annually (remove stale exceptions)? | | | |
| 12 | Are high-FP rules disabled or re-tuned? | | | |
| 13 | Are users educated when FP is user error (not DLP issue)? | | | |
| 14 | Is FP tuning tracked (before/after FP rate improvement)? | | | |
| 15 | Are tuning changes tested before production deployment? | | | |
| 16 | Are tuning changes documented (change request, approval)? | | | |
| 17 | Are tuning changes rolled back if new issues arise? | | | |
| 18 | Is FP rate included in SOC performance metrics? | | | |
| 19 | Are FP trends reported to management (monthly)? | | | |
| 20 | Are FP reduction targets set and tracked? | | | |

**FP Rate Calculation Table:**

| Alert Rule ID | Rule Name | Total Alerts (30d) | False Positives | FP Rate % | Target FP % | Status |
|---------------|-----------|--------------------|-----------------|-----------|-----------|----|
| ALT-001 | Credentials - Email | 45 | 1 | 2.2% | <5% | ✅ On Target |
| ALT-002 | PII to External | 230 | 20 | 8.7% | <10% | ✅ On Target |
| ALT-003 | Source Code GitHub | 12 | 0 | 0.0% | <5% | ✅ On Target |
| ALT-004 | Mass USB Copy | 3 | 0 | 0.0% | <5% | ✅ On Target |
| ALT-005 | Bulk DB Export | 67 | 3 | 4.5% | <10% | ✅ On Target |

---

### 4.7 Sheet: Incident_Response_Workflow

**Purpose:** Document DLP incident response procedures and SLA compliance.

**Assessment Questions (25 rows):**

| # | Requirement | Yes/No/Partial/Planned/N/A | Evidence ID | Notes |
|---|-------------|----------------------------|-------------|-------|
| 1 | Are DLP alerts integrated with incident response workflow? | | | |
| 2 | Is incident response procedure documented (playbook)? | | | |
| 3 | Critical alerts: Are alerts triaged within 15 minutes? | | | |
| 4 | High alerts: Are alerts triaged within 1 hour? | | | |
| 5 | Medium alerts: Are alerts triaged within 4 hours? | | | |
| 6 | Low alerts: Are alerts triaged within 24 hours? | | | |
| 7 | Is alert triage documented (who, when, decision)? | | | |
| 8 | Are false positives closed with justification? | | | |
| 9 | Are true positives escalated to incident response team? | | | |
| 10 | Are users contacted for business justification (High alerts)? | | | |
| 11 | Are user managers contacted for approval (policy exceptions)? | | | |
| 12 | Are incidents assigned severity based on data classification? | | | |
| 13 | Are incidents assigned to appropriate team (SOC, IR, Legal)? | | | |
| 14 | Is containment performed (block user, disable account, isolate endpoint)? | | | |
| 15 | Is investigation performed (correlate with other events)? | | | |
| 16 | Is evidence collected (logs, screenshots, file samples)? | | | |
| 17 | Is evidence preserved (chain of custody)? | | | |
| 18 | Are incidents reported to management (Critical/High)? | | | |
| 19 | Are incidents reported to DPO (personal data breaches)? | | | |
| 20 | Are incidents reported to CISO (all Critical incidents)? | | | |
| 21 | Are incidents reported to Legal (potential litigation)? | | | |
| 22 | Is remediation tracked (close incident when resolved)? | | | |
| 23 | Is Mean Time to Detect (MTTD) measured? | | | |
| 24 | Is Mean Time to Respond (MTTR) measured? | | | |
| 25 | Are lessons learned documented (post-incident review)? | | | |

**SLA Compliance Tracking Table:**

| Severity | SLA Target | Incidents (30d) | Within SLA | SLA Compliance % |
|----------|------------|-----------------|------------|-----------------|
| Critical | 15 minutes | 8 | 7 | 87.5% |
| High | 1 hour | 35 | 32 | 91.4% |
| Medium | 4 hours | 120 | 115 | 95.8% |
| Low | 24 hours | 450 | 448 | 99.6% |

---

### 4.8 Sheet: SOC_Integration

**Purpose:** Assess SOC alert workflow, escalation, and staffing.

**Assessment Questions (20 rows):**

| # | Requirement | Yes/No/Partial/Planned/N/A | Evidence ID | Notes |
|---|-------------|----------------------------|-------------|-------|
| 1 | Are DLP alerts integrated with SOC workflow? | | | |
| 2 | Are Critical alerts delivered to SOC (SIEM + SMS/PagerDuty)? | | | |
| 3 | Are High alerts delivered to SOC (SIEM + Email)? | | | |
| 4 | Are SOC analysts trained on DLP alert triage? | | | |
| 5 | Is DLP training part of SOC analyst onboarding? | | | |
| 6 | Is DLP triage playbook documented (step-by-step)? | | | |
| 7 | Is escalation matrix documented (L1 → L2 → IR → Management)? | | | |
| 8 | Are SOC analysts able to escalate to DLP admin? | | | |
| 9 | Are SOC analysts able to escalate to user manager? | | | |
| 10 | Are SOC analysts able to escalate to Legal/DPO? | | | |
| 11 | Is SOC coverage 24/7 (for Critical DLP alerts)? | | | |
| 12 | Is SOC coverage business hours only (9-5) for Medium/Low alerts? | | | |
| 13 | Is on-call rotation defined (after-hours Critical alerts)? | | | |
| 14 | Are SOC metrics tracked (alert volume, triage time, SLA compliance)? | | | |
| 15 | Are SOC metrics reported to management (monthly)? | | | |
| 16 | Is SOC staffing adequate (not overwhelmed by alert volume)? | | | |
| 17 | Is SOC burnout monitored (high alert volume, turnover rate)? | | | |
| 18 | Are SOC tools adequate (SIEM, ticketing, communication)? | | | |
| 19 | Is SOC performance reviewed quarterly? | | | |
| 20 | Are SOC improvements implemented (based on performance review)? | | | |

---

### 4.9 Sheet: Dashboards_Reporting

**Purpose:** Assess dashboard and reporting capabilities.

**Assessment Questions (20 rows):**

| # | Requirement | Yes/No/Partial/Planned/N/A | Evidence ID | Notes |
|---|-------------|----------------------------|-------------|-------|
| 1 | Is real-time SOC dashboard configured (alert queue)? | | | |
| 2 | SOC Dashboard: Shows Critical/High/Medium alerts pending triage? | | | |
| 3 | SOC Dashboard: Shows alert volume over time (hourly)? | | | |
| 4 | SOC Dashboard: Shows top blocked users (last 24 hours)? | | | |
| 5 | SOC Dashboard: Shows top blocked channels (email, USB, web)? | | | |
| 6 | SOC Dashboard: Shows false positive rate (rolling 7-day average)? | | | |
| 7 | Is executive dashboard configured (updated daily)? | | | |
| 8 | Executive Dashboard: Shows Critical incidents (last 30 days)? | | | |
| 9 | Executive Dashboard: Shows DLP effectiveness (prevented incidents)? | | | |
| 10 | Executive Dashboard: Shows compliance metrics (coverage %, enforcement rate)? | | | |
| 11 | Executive Dashboard: Shows risk heatmap (users, departments, channels)? | | | |
| 12 | Are weekly reports generated (Security Team)? | | | |
| 13 | Weekly Report: Alert summary (Critical/High/Medium/Low counts)? | | | |
| 14 | Weekly Report: Top users by alert volume? | | | |
| 15 | Weekly Report: False positive trend? | | | |
| 16 | Are monthly reports generated (Management)? | | | |
| 17 | Monthly Report: Executive summary (1-page, business language)? | | | |
| 18 | Monthly Report: Incident summary (critical events, resolved vs ongoing)? | | | |
| 19 | Are quarterly reports generated (CISO/Board)? | | | |
| 20 | Quarterly Report: Strategic risk assessment, ROI analysis? | | | |

---

### 4.10 Sheet: Gap_Analysis

**Purpose:** Identify monitoring and response gaps and create remediation plans.

**Standard Format (40 rows):**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Gap ID                    | Text         | Auto-generated (GAP-A812-4-###)    | 18        |
| B       | Gap Description           | Text         | User input                         | 40        |
| C       | Affected Area             | Dropdown     | Logging/Alerting/SIEM/FP/IR/SOC/Dashboards | 20        |
| D       | Risk Level                | Dropdown     | Critical/High/Medium/Low           | 15        |
| E       | Business Impact           | Text         | User input                         | 30        |
| F       | Remediation Plan          | Text         | User input                         | 40        |
| G       | Owner                     | Text         | User input (name, role)            | 25        |
| H       | Target Date               | Date         | User input                         | 15        |
| I       | Status                    | Dropdown     | Not Started/In Progress/Complete/Blocked | 15        |
| J       | Evidence ID               | Text         | User input (A812-4-GAP-###)        | 18        |

**Data Rows:** 40 blank rows for gap tracking.

---

### 4.11 Sheet: Evidence_Register

**Purpose:** Track all evidence collected for Domain 4 assessment.

**Standard Format (100 rows):**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Evidence ID               | Text         | User input (A812-4-XXX-###)        | 18        |
| B       | Evidence Type             | Dropdown     | Config/Screenshot/Log/Report/Dashboard/Other | 20        |
| C       | Description               | Text         | User input                         | 35        |
| D       | Location/Link             | Text         | User input (file path/URL)         | 30        |
| E       | Date Collected            | Date         | User input                         | 15        |
| F       | Collected By              | Text         | User input                         | 20        |
| G       | Related Requirement       | Text         | User input (sheet reference)       | 25        |
| H       | Verification Status       | Dropdown     | Verified/Pending/Rejected          | 15        |

**Data Rows:** 100 blank rows.

---

### 4.12 Sheet: Summary_Dashboard

**Purpose:** KPIs and compliance scoring for Domain 4.

**Content Sections:**

1. **Workbook Metadata**
   - Assessment Date: [Input]
   - Completed By: [Input]
   - Approved By: [Input]
   - Next Review: [Formula: Assessment Date + 90 days]

2. **Overall Domain 4 Compliance Score**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Logging Configuration Complete % | [Formula: COUNT(Logging_Configuration!C:C="Yes")/25×100] | 90% | ✅/⚠️/❌ |
| Alert Rules Documented % | [Formula: COUNTA(Alert_Rules_Inventory!A:A)/30×100] | 80% | ✅/⚠️/❌ |
| SIEM Integration Complete % | [Formula: COUNT(SIEM_Integration!C:C="Yes")/25×100] | 90% | ✅/⚠️/❌ |
| False Positive Rate % | [Formula: AVERAGE(Alert_Rules_Inventory!J:J)] | <10% | ✅/⚠️/❌ |
| Incident Response SLA Compliance % | [Formula: from Incident_Response_Workflow] | >90% | ✅/⚠️/❌ |
| SOC Integration Complete % | [Formula: COUNT(SOC_Integration!C:C="Yes")/20×100] | 85% | ✅/⚠️/❌ |
| Dashboards Deployed % | [Formula: COUNT(Dashboards_Reporting!C:C="Yes")/20×100] | 80% | ✅/⚠️/❌ |
| **Overall Domain 4 Compliance** | [Formula: AVERAGE of above] | >85% | ✅/⚠️/❌ |

**Traffic Light Logic:**
- ✅ Green: Value ≥ Target
- ⚠️ Yellow: Value ≥ (Target - 10%)
- ❌ Red: Value < (Target - 10%)

3. **Key Findings**
   - Total alerts per day: [Formula: from Alert_Volume_Metrics]
   - False positive rate: [Formula: from False_Positive_Management]
   - MTTD (Mean Time to Detect): [Input]
   - MTTR (Mean Time to Respond): [Input]
   - Critical gaps count: [Formula: COUNTIF(Gap_Analysis!D:D,"Critical")]
   - Evidence completeness: [Formula: COUNTA(Evidence_Register!A:A)/100×100%]

4. **Approval Workflow**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| DLP Administrator | [Input] | [Input] | [Input] |
| SOC Lead | [Input] | [Input] | [Input] |
| CISO | [Input] | [Input] | [Input] |
| DPO | [Input] | [Input] | [Input] |

---

## 5. ASSESSMENT CRITERIA & SCORING

### 5.1 Scoring Methodology

Each assessment criterion is scored as:
- **Yes** = 1.0 (Full compliance)
- **Partial** = 0.5 (Partial compliance)
- **No** = 0.0 (Non-compliance)
- **Planned** = 0.25 (Credit for planning)
- **N/A** = Excluded from calculation

**Domain 4 Compliance Score** = (Sum of scores / Total applicable criteria) × 100

### 5.2 Pass/Fail Criteria

- **Pass:** Overall Domain 4 Compliance ≥ 85%
- **Conditional Pass:** 70-84% (gaps must be addressed within 90 days)
- **Fail:** <70% (significant remediation required)

### 5.3 Critical Gaps

The following are **CRITICAL** gaps that require immediate remediation:

1. DLP logs not forwarded to SIEM (no centralized monitoring)
2. Critical alerts not delivered to SOC within 15 minutes (SLA breach)
3. No incident response workflow (alerts not investigated)
4. False positive rate >20% (alert fatigue, SOC overwhelmed)
5. No SOC coverage for Critical alerts (24/7 gap)
6. No dashboards or reporting (management blind to DLP status)

---

## 6. COMPLIANCE MAPPING

### 6.1 ISO/IEC 27001:2022 Mapping

| ISO Control | Title | Domain 4 Mapping |
|-------------|-------|------------------|
| A.8.12 | Data Leakage Prevention | All sheets (monitoring/response layer) |
| A.8.15 | Logging | Logging_Configuration, SIEM_Integration |
| A.8.16 | Monitoring activities | Alert_Volume_Metrics, SOC_Integration |
| A.5.24 | Information security incident management planning | Incident_Response_Workflow |
| A.5.26 | Response to information security incidents | Incident_Response_Workflow |

### 6.2 Regulatory Mapping

**Swiss FADP (Federal Act on Data Protection):**
- Article 8: Security of data processing → SIEM integration, incident response
- Article 24: Data breach notification → Incident response workflow (DPO escalation)
- Article 26: Employee monitoring → SOC integration (proportionality)

**EU GDPR (General Data Protection Regulation):**
- Article 32: Security of processing → Logging, monitoring, incident response
- Article 33: Breach notification (72 hours) → Incident response workflow
- Article 5(1)(f): Integrity and confidentiality → SIEM correlation rules

**Swiss Employment Law:**
- Article 328b CO: Proportionality in employee monitoring → Alert volume, false positive management

---

## 7. EVIDENCE REQUIREMENTS

### 7.1 Mandatory Evidence

**For Logging Configuration:**
- SIEM screenshot showing DLP log ingestion
- Log sample (anonymized) showing required fields
- Log retention policy documentation

**For Alert Rules:**
- Alert rule configuration export (CSV/JSON)
- Sample alerts (Critical, High, Medium)
- Alert tuning history (before/after FP rate)

**For SIEM Integration:**
- SIEM correlation rule screenshots
- SIEM dashboard screenshots (SOC, executive)
- SIEM search queries documentation

**For False Positive Management:**
- FP rate dashboard or report
- Whitelist documentation (approved exceptions)
- Tuning change requests (before/after comparison)

**For Incident Response:**
- Sample IR tickets (anonymized) with timestamps
- SOC playbook documentation
- SLA compliance report (MTTD/MTTR)

**For SOC Integration:**
- Escalation matrix documentation
- SOC training materials (DLP triage)
- On-call rotation schedule

**For Dashboards:**
- SOC dashboard screenshot (real-time alert queue)
- Executive dashboard screenshot (monthly summary)
- Sample reports (weekly, monthly, quarterly)

### 7.2 Evidence Naming Convention
```
A812-4-[CATEGORY]-[###]

Examples:
A812-4-LOG-001 = SIEM log ingestion screenshot
A812-4-ALT-001 = Critical alert sample
A812-4-SIEM-001 = Correlation rule config
A812-4-FP-001 = False positive rate dashboard
A812-4-IR-001 = Incident response ticket
A812-4-SOC-001 = SOC playbook document
A812-4-DASH-001 = Executive dashboard screenshot
```

---

## 8. APPROVAL & SIGN-OFF

### 8.1 Approval Workflow

1. **DLP Administrator** completes workbook
2. **SOC Lead** reviews alert configuration, SLA compliance
3. **CISO** reviews overall compliance score, critical gaps
4. **DPO** reviews incident response, FADP/GDPR compliance
5. **Approval** documented in Summary_Dashboard

### 8.2 Sign-Off Requirements

- Minimum 3 signatures: DLP Admin, SOC Lead, CISO
- DPO signature required if personal data processing involved
- Sign-off indicates: Assessment complete, gaps identified, remediation planned

---

**END OF DOCUMENT**

*"The first principle of SOC operations: You must not fool yourself into thinking alerts are being investigated. Without SLA metrics, you have no idea if your monitoring is effective."*  
*— Feynman-inspired ISMS Wisdom* 🎯
# ISMS-IMP-A.8.23.4 - Monitoring & Response Assessment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.8.23: Web Filtering

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.23.4 |
| **Version** | 1.0 |
| **Assessment Area** | Web Filtering Monitoring, Logging & Incident Response |
| **Related Policy** | ISMS-POL-A.8.23-S2.3 (Logging & Monitoring Requirements), ISMS-POL-A.8.23-S5.C (Incident Response Procedures) |
| **Purpose** | Assess operational monitoring, alerting, logging, and incident response capabilities for web filtering infrastructure |
| **Target Audience** | SOC Analysts, Security Engineers, IT Operations, Incident Responders, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Technical |
| **Review Cycle** | Quarterly or After Major Incidents/Infrastructure Changes |
| **Date** | 15.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 15.01.2026 | Initial technical specification for Web Filtering Monitoring & Incident Response assessment workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- # PART I: USER COMPLETION GUIDE (Current Section)
  - Assessment Overview
  - Prerequisites
  - Workflow
  - Question-by-Question Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- # PART II: TECHNICAL SPECIFICATION
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Definitions
  - Cell Styling Reference

---

# PART I: USER COMPLETION GUIDE

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.23.4 - Monitoring & Response Assessment

### What This Assessment Covers

This assessment evaluates your organization's operational capabilities for monitoring, logging, alerting, and responding to web filtering events. This is the **"operations"** assessment - verifying that your web filtering infrastructure (assessed in A.8.23.1) with proper policy configuration (assessed in A.8.23.3) is actually being monitored and that incidents are being detected and handled appropriately.

### What You'll Document

- **Logging:** What web filtering logs are collected, where they're stored, retention periods
- **Alerting:** What alert rules are configured, thresholds, notification methods
- **Monitoring:** What dashboards exist, what KPIs are tracked, who reviews them
- **Incident Response:** How web filtering incidents are handled, SLAs, escalation paths
- **Blocked Events Analysis:** Trends in blocked attempts, threat intelligence
- **False Positive Management:** How FPs are identified, tracked, and resolved
- **Reporting:** What regular reports are generated, for whom, how often
- **Gaps:** Any identified deficiencies in monitoring or response capabilities

**Key Principle:** This assessment is evidence-based. You're documenting *what actually happens* in your environment - not what should happen in theory. If dashboards exist but nobody looks at them, that's a gap. If alerts fire but response times are 10x the SLA, that's a finding. Be honest with yourself (Feynman: "The first principle is that you must not fool yourself").

### How This Relates to Other A.8.23 Assessments

 | Assessment | Focus | Relationship to A.8.23.4 | 
|------------|-------|-------------------## Document Overview


All four must align for complete web filtering compliance. You can have the best filtering infrastructure in the world, but if nobody monitors it or responds to alerts, it's security theater.

## Who Should Complete This Assessment

**Primary Stakeholders:**

1. **Security Operations Center (SOC)** - Log collection, SIEM integration, alert handling
2. **Security Engineers** - Alert rule configuration, dashboard design
3. **IT Operations** - Log storage infrastructure, system monitoring
4. **Incident Response Team** - Incident handling procedures, escalation paths
5. **Compliance Officer** - Retention requirements, regulatory compliance

### Required Skills

- Understanding of logging architecture (syslog, SIEM, log servers)
- Familiarity with alert configuration and threshold tuning
- Knowledge of incident response procedures
- Access to monitoring dashboards and reporting tools

**Time Commitment:**

- **Initial assessment:** 8-12 hours (spread over 1-2 weeks)
- **Quarterly updates:** 2-3 hours (mainly updating metrics and reviewing gaps)

## Expected Outputs

Upon completion, you will have:

1. ✅ **Complete log inventory** - All web filtering log sources documented
2. ✅ **Alert rule catalog** - All alerting rules with thresholds and recipients
3. ✅ **Dashboard inventory** - All monitoring dashboards with KPIs tracked
4. ✅ **Incident response documentation** - Procedures, SLAs, escalation paths
5. ✅ **Blocked events analysis** - Trends and threat intelligence insights
6. ✅ **False positive tracking** - FP management process and resolution history
7. ✅ **Reporting schedule** - Regular reports generated and their audiences
8. ✅ **Gap analysis** - Identified deficiencies with remediation plans
9. ✅ **Evidence register** - Supporting documentation for audit
10. ✅ **Approved assessment** - Three-level approval workflow completed

---

# Prerequisites

## Required Information

Before starting, gather the following information:

### Logging Infrastructure
- [ ] List of all systems generating web filtering logs
- [ ] SIEM or log management platform details
- [ ] Log retention policies and actual retention periods
- [ ] Regulatory/compliance retention requirements
- [ ] Log storage capacity and usage statistics

### Alerting Configuration
- [ ] Access to SIEM or alerting platform
- [ ] List of configured alert rules
- [ ] Alert notification configurations
- [ ] Escalation matrix and on-call schedules
- [ ] Recent alert history (last 90 days recommended)

### Monitoring & Dashboards
- [ ] Access to all monitoring dashboards
- [ ] KPI definitions and target values
- [ ] Dashboard review schedules and responsibilities
- [ ] Screenshots of key dashboards for evidence

### Incident Response
- [ ] Incident response procedures/runbooks
- [ ] SLA definitions for web filtering incidents
- [ ] Recent incident history (last 6-12 months)
- [ ] Incident ticketing system access
- [ ] Post-incident review reports

### Reporting
- [ ] List of regular reports generated
- [ ] Report templates or examples
- [ ] Distribution lists for reports
- [ ] Report generation tools/scripts

## Required Access

Ensure you have access to:

- **SIEM Platform** - To review log sources and alert rules
- **Filtering Consoles** - To verify logging configuration
- **Monitoring Dashboards** - To document KPIs and review frequency
- **Incident Management System** - To review incident handling
- **File Shares/Documentation Repositories** - To gather evidence

## Required Documents

Have the following documents ready:

- ISMS-POL-A.8.23-S2.3 (Logging & Monitoring Requirements)
- ISMS-POL-A.8.23-S5.C (Incident Response Procedures)
- ISMS-IMP-A.8.23.1 (Filtering Infrastructure Assessment - completed)
- ISMS-IMP-A.8.23.3 (Policy Configuration Assessment - completed)
- Organizational log retention policy
- Incident response plan/runbook
- SOC procedures documentation

## Stakeholder Coordination

Schedule working sessions with:

1. **SOC Team** (2-3 hours) - Log collection, alerting, incident handling
2. **Security Engineering** (1-2 hours) - Dashboard design, alert tuning
3. **IT Operations** (1 hour) - Log storage infrastructure
4. **Compliance** (30 mins) - Retention requirements verification

---

# Workflow

## Assessment Process Overview

```plaintext
Step 1: Preparation (1-2 hours)
  ├─ Gather prerequisites
  ├─ Schedule stakeholder sessions
  └─ Generate Excel workbook

Step 2: Data Collection (6-8 hours)
  ├─ Sheet 2: Log Collection Inventory
  ├─ Sheet 3: Alert Configuration
  ├─ Sheet 4: Monitoring Dashboards
  ├─ Sheet 5: Incident Response Procedures
  ├─ Sheet 6: Blocked Events Analysis
  ├─ Sheet 7: False Positive Management
  └─ Sheet 8: Reporting Schedule

Step 3: Gap Analysis (1-2 hours)
  ├─ Review completed sheets
  ├─ Identify deficiencies
  └─ Document gaps in Sheet 9

Step 4: Evidence Collection (1-2 hours)
  ├─ Gather supporting documentation
  ├─ Take screenshots of dashboards
  ├─ Export configuration files
  └─ Document in Sheet 10 (Evidence Register)

Step 5: Internal Review (1 hour)
  ├─ Validate data accuracy
  ├─ Verify completeness
  └─ Run quality checklist

Step 6: Approval Workflow (1-2 days)
  ├─ Level 1: Operational Approval (SOC Manager)
  ├─ Level 2: Technical Approval (Security Engineering Lead)
  └─ Level 3: Executive Approval (CISO)

Step 7: Integration (30 mins)
  └─ Feed data into Dashboard (A.8.23.5)
```

**Total Time:** 10-15 hours spread over 1-2 weeks

## Detailed Workflow Steps

### Step 1: Preparation

1. **Generate the Excel Workbook:**
   ```bash
   python generate_a823_4_monitoring_response.py
   ```
   Output: `ISMS-IMP-A.8.23.4_Monitoring_Response_YYYYMMDD.xlsx`

2. **Review Instructions Sheet:**

   - Read Sheet 1 (Instructions_Legend) completely
   - Familiarize yourself with dropdown values
   - Understand the status color codes

3. **Fill in Document Information:**

   - Assessment Date
   - Completed By
   - Organization Name

### Step 2: Data Collection (Sheet by Sheet)

**Sheet 2: Log Collection** (2-3 hours with SOC)

- Document all log sources generating web filtering events
- Verify collection methods (syslog, API, agent)
- Confirm log destinations (SIEM, log server, cloud)
- Validate retention periods against requirements
- Identify any missing log sources

**Sheet 3: Alert Configuration** (2 hours with Security Engineering)

- List all configured alert rules
- Document thresholds and trigger conditions
- Verify notification methods and recipients
- Check response SLAs
- Review recent alert history

**Sheet 4: Monitoring Dashboards** (1-2 hours)

- Inventory all monitoring dashboards
- Document KPIs tracked on each dashboard
- Verify review frequency and responsibilities
- Take screenshots for evidence
- Assess dashboard effectiveness

**Sheet 5: Incident Response** (1-2 hours with Incident Response Team)

- Document incident categorization and severity definitions
- Review SLA compliance for recent incidents
- Verify escalation paths
- Check post-incident review process
- Identify any incident handling gaps

**Sheet 6: Blocked Events Analysis** (1 hour with SOC)

- Analyze trends in blocked attempts
- Document threat categories observed
- Review geographic distribution of threats
- Assess effectiveness of threat protection

**Sheet 7: False Positive Management** (1 hour)

- Document FP identification process
- Review FP resolution procedures
- Track chronic FP issues
- Assess tuning effectiveness

**Sheet 8: Reporting Schedule** (30 mins)

- List all regular reports generated
- Document recipients and frequency
- Verify report generation methods
- Review report effectiveness

### Step 3: Gap Analysis

1. **Review all completed sheets systematically**
2. **Identify gaps in three categories:**

   - **Technical Gaps:** Missing log sources, misconfigured alerts
   - **Process Gaps:** Missing procedures, undefined SLAs
   - **Operational Gaps:** Dashboards not reviewed, reports not used
3. **Prioritize gaps** using Critical/High/Medium/Low
4. **Develop remediation plans** with owners and target dates
5. **Document in Sheet 9**

### Step 4: Evidence Collection

For each assessment item, gather supporting evidence:

- **Log Collection:** Configuration screenshots, SIEM screenshots
- **Alerts:** Alert rule exports, notification configuration
- **Dashboards:** Dashboard screenshots, KPI definitions
- **Incident Response:** Runbook documents, incident tickets
- **Reporting:** Report examples, distribution lists

Document all evidence in Sheet 10 (Evidence Register) with:

- Evidence ID
- Evidence Type
- Description
- Location/Reference
- Verification Status

### Step 5: Internal Review

Run through the quality checklist (Section 7 below) to verify:

- All required sections completed
- Data accuracy validated
- Evidence linked properly
- Gaps properly documented
- Metrics calculated correctly

### Step 6: Approval Workflow

**Level 1: Operational Approval** (SOC Manager or Security Operations Lead)

- Review operational accuracy
- Verify log collection and alert configuration
- Approve or request corrections

**Level 2: Technical Approval** (Security Engineering Lead)

- Review technical completeness
- Validate monitoring and response capabilities
- Approve or request enhancements

**Level 3: Executive Approval** (CISO or Information Security Manager)

- Review strategic alignment
- Accept identified gaps and remediation plans
- Final approval for audit readiness

Document approvals in Sheet 11 with:

- Approver Name
- Approver Role
- Approval Date
- Comments

### Step 7: Integration with Dashboard

Once approved:
1. Run the normalization script (if using long filenames)
2. The consolidated dashboard (A.8.23.5) will pull data automatically
3. Verify data appears correctly in the dashboard
4. Schedule quarterly update reminder

---

# Question-by-Question Guidance

## Sheet 2: Log Collection

**Purpose:** Document what web filtering logs are collected, where they're stored, and whether retention requirements are met.

### Section A: Log Source Inventory (30 log sources)

**For each log source, answer:**

**Q1: Log_Source_ID**

- **Pre-filled:** LOG-001 through LOG-030
- **Action:** Use the pre-filled ID or add more rows if needed

**Q2: Log_Source_Name**

- **Question:** What is the descriptive name of this log source?
- **Examples:**
  - "Web Proxy Blocked Requests"
  - "DNS Filter Query Logs"
  - "Firewall URL Filtering Logs"
  - "SWG Policy Violations"
- **Tip:** Use consistent naming - it helps when reviewing logs later

**Q3: Log_Type**

- **Question:** What type of events does this log source capture?
- **Dropdown Options:**
  - **Blocked_Requests** - Web requests that were denied/blocked
  - **Allowed_Requests** - Permitted requests (if you log them)
  - **Bypass_Attempts** - Attempts to circumvent filtering
  - **Policy_Violations** - Actions violating acceptable use
  - **Authentication** - User authentication to filtering services
  - **Configuration_Changes** - Admin changes to filtering config
  - **System_Events** - System health, errors, service status
- **Auditor Expects:** At minimum, Blocked_Requests logs must exist
- **Common Mistake:** Logging everything wastes storage. Focus on security-relevant events.

**Q4: Source_System**

- **Question:** What system/device generates these logs?
- **Examples:**
  - "Zscaler Internet Access"
  - "Palo Alto PA-5220 Firewall"
  - "Cisco Umbrella DNS Security"
  - "Squid Proxy Server"
- **Tip:** Be specific - include model numbers for hardware appliances

**Q5: Collection_Method**

- **Question:** How are logs collected from the source to the destination?
- **Dropdown Options:**
  - **Syslog** - Traditional syslog protocol (UDP/TCP 514)
  - **API** - RESTful API calls to vendor platform
  - **Agent** - Software agent on the system
  - **File_Transfer** - SFTP, SCP, file copy
  - **Direct_Query** - Manual or scripted database queries
  - **SNMP** - SNMP traps
  - **Other** - Specify in Notes
- **Auditor Expects:** Secure, reliable collection methods (API/Syslog preferred)
- **Common Mistake:** "File_Transfer" without automation = manual = unreliable

**Q6: Destination**

- **Question:** Where do these logs ultimately end up?
- **Dropdown Options:**
  - **SIEM** - Security Information and Event Management platform
  - **Log_Server** - Dedicated log management server
  - **Cloud_SIEM** - Cloud-based SIEM (Splunk Cloud, Sumo Logic, etc.)
  - **Local_Storage** - Stored locally on the filtering device
  - **Archive** - Long-term archive storage
  - **Multiple** - Logs go to more than one destination
- **Auditor Expects:** Centralized log management (SIEM preferred)
- **Red Flag:** "Local_Storage" only = no centralized monitoring

**Q7: Format**

- **Question:** In what format are logs stored?
- **Dropdown Options:**
  - **CEF** - Common Event Format (ArcSight standard)
  - **JSON** - JavaScript Object Notation
  - **Syslog** - Traditional syslog format
  - **CSV** - Comma-separated values
  - **Proprietary** - Vendor-specific format
  - **XML** - Extensible Markup Language
  - **Other** - Specify in Notes
- **Auditor Expects:** Structured format (CEF/JSON preferred for parsing)
- **Tip:** Proprietary formats make SIEM integration harder

**Q8: Retention_Days**

- **Question:** How many days are these logs retained?
- **Format:** Number of days (e.g., 90, 365, 2555 for 7 years)
- **Common Requirements:**
  - PCI DSS: 90 days online, 1 year in archive
  - GDPR: Depends on data processing purposes
  - General security best practice: 90-365 days
  - Forensic investigations: 1-7 years
- **Tip:** Check your organization's retention policy and regulatory requirements

**Q9: Retention_Compliant**

- **Question:** Does the retention period meet your requirements?
- **Dropdown Options:**
  - **Yes** - Meets all requirements
  - **No** - Does not meet requirements (specify why in Notes)
  - **Partial** - Meets some but not all requirements
- **Auditor Expects:** "Yes" for all log sources or documented plans to remediate
- **Red Flag:** Multiple "No" answers = compliance risk

**Q10: Volume_Daily**

- **Question:** What's the daily volume of logs from this source?
- **Format:** Free text (be specific)
- **Examples:**
  - "15 GB/day"
  - "2.5 million events/day"
  - "500 MB compressed"
  - "Approximately 10K events/hour"
- **Why This Matters:** Helps with capacity planning and identifies high-volume sources

**Q11: Status**

- **Question:** What is the operational status of this log source?
- **Dropdown Options:**
  - **Implemented** - Fully operational, logs flowing correctly
  - **Partial** - Some logs collected but gaps exist
  - **Planned** - Scheduled but not yet operational
  - **Not_Implemented** - Not currently collecting
  - **N/A** - Not applicable to this environment
- **Auditor Expects:** Most sources = "Implemented"
- **Red Flag:** Critical logs (Blocked_Requests) = "Not_Implemented"

**Q12: Evidence_Ref**

- **Question:** What evidence supports this log source configuration?
- **Format:** Reference to Evidence_Register (e.g., "EVID-004")
- **Evidence Types:**
  - Screenshot of SIEM showing log ingestion
  - Configuration export from filtering device
  - Log sample file
  - SIEM data source configuration screenshot
- **Auditor Expects:** Evidence for ALL "Implemented" sources

**Q13: Notes**

- **Question:** Any additional context or issues?
- **Examples:**
  - "Retention only 30 days due to storage constraints - upgrade planned Q2"
  - "Logs contain PII - handled per GDPR retention policy"
  - "High volume source - compressed before forwarding to SIEM"
  - "Legacy system scheduled for decommission in 6 months"

### Section B: Retention Requirements (10 requirements)

**For each retention requirement, document:**

**Q14: Requirement_ID**

- **Pre-filled:** RET-001 through RET-010
- **Action:** Use pre-filled or add more if you have many requirements

**Q15: Requirement_Source**

- **Question:** Where does this retention requirement come from?
- **Dropdown Options:**
  - **Regulatory** - Law, regulation (GDPR, PCI DSS, SOX)
  - **Policy** - Internal organizational policy
  - **Contractual** - Customer/vendor contract requirement
  - **Best_Practice** - Industry best practice (NIST, CIS)
- **Examples:**
  - "PCI DSS v4.0 Requirement 10.5.1"
  - "Swiss nDSG Art. 8"
  - "ISMS-POL-A.8.23-S2.3"
  - "Customer contract clause 7.3"

**Q16: Log_Type_Affected**

- **Question:** Which log types must meet this requirement?
- **Format:** Free text
- **Examples:**
  - "All authentication logs"
  - "Blocked_Requests only"
  - "All web filtering logs"
  - "Policy_Violations and Bypass_Attempts"
- **Tip:** Be specific - this helps verify compliance in Section A

**Q17: Min_Retention_Days**

- **Question:** What is the minimum retention period required?
- **Format:** Number of days
- **Common Values:**
  - 30 days - Very short-term
  - 90 days - PCI DSS minimum
  - 365 days - 1 year (common)
  - 2555 days - 7 years (long-term compliance)
- **Tip:** If requirement says "1 year", use 365 days for consistency

**Q18: Current_Retention**

- **Question:** What is the current actual retention period?
- **Format:** Number of days
- **Source:** Get this from Section A (Retention_Days column)
- **Tip:** This should match what you documented in Section A

**Q19: Compliant**

- **Question:** Does current retention meet the minimum requirement?
- **Dropdown Options:**
  - **Yes** - Current ≥ Required
  - **No** - Current < Required (gap!)
  - **Partial** - Some log sources compliant, others not
- **Formula:** You can use Excel formula: =IF(E39>=D39,"Yes","No")
- **Auditor Expects:** All "Yes" or documented remediation plans

**Q20: Notes**

- **Question:** Any additional context about compliance status?
- **Examples:**
  - "Storage upgrade approved for Q2 2026 to extend retention"
  - "Partial: DNS logs 90 days, proxy logs 365 days"
  - "Compliant but approaching storage capacity limits"
  - "Requirement waived for legacy system (decommission in progress)"

### Section C: Summary Metrics

These are **calculated automatically** based on your data in Sections A and B:

- **Total log sources configured** - Counts non-empty entries
- **Blocked request log sources** - Critical for threat detection
- **Sources meeting retention** - Compliance percentage
- **Retention compliance rate** - Overall health metric
- **Implemented sources** - Operational readiness
- **Sources needing attention** - Action items

**Auditor Will Review:**

- Are critical log types being collected? (Blocked_Requests = mandatory)
- Is retention compliance >95%? (Target: 100%)
- Are most sources "Implemented"? (Target: >90%)
- Are there documented plans for "Partial" or "Not_Implemented" sources?

---

## Sheet 3: Alert Configuration

**Purpose:** Document all alerting rules for web filtering events, ensuring timely detection and response.

### Section A: Alert Rules Inventory (40 alert rules)

**For each alert rule, answer:**

**Q1: Alert_ID**

- **Pre-filled:** ALR-001 through ALR-040
- **Action:** Use pre-filled ID

**Q2: Alert_Name**

- **Question:** What is the descriptive name of this alert?
- **Examples:**
  - "Malware Download Attempt"
  - "Excessive Blocked Requests from Single User"
  - "Filtering Service Offline"
  - "Policy Bypass Detected"
  - "Critical Threat Category Block"
- **Tip:** Names should be clear and actionable for SOC analysts

**Q3: Alert_Category**

- **Question:** What category does this alert fall into?
- **Dropdown Options:**
  - **Threat_Detection** - Malware, phishing, C2 communication detected
  - **Policy_Violation** - User violated acceptable use policy
  - **System_Health** - Filtering service health, performance issues
  - **Threshold_Breach** - Volume/rate threshold exceeded
  - **Anomaly** - Unusual behavior detected (ML/baseline)
  - **Compliance** - Regulatory/compliance requirement triggered
- **Auditor Expects:** Balanced coverage across categories, with emphasis on Threat_Detection
- **Common Mistake:** Only System_Health alerts = reactive, not proactive security

**Q4: Trigger_Condition**

- **Question:** What specific condition triggers this alert?
- **Format:** Free text - be specific and technical
- **Examples:**
  - "URL categorized as 'Malware' is accessed"
  - ">100 blocked requests from single user in 10 minutes"
  - "Web proxy service stops responding to health checks"
  - "User accesses blocked site via VPN bypass"
  - "5+ failed authentication attempts in 5 minutes"
- **Auditor Expects:** Clear, measurable trigger conditions
- **Red Flag:** Vague conditions like "when something bad happens"

**Q5: Threshold_Value**

- **Question:** What is the specific threshold (if applicable)?
- **Format:** Free text
- **Examples:**
  - ">100/hour"
  - "Any occurrence" (for critical threats)
  - ">50% failure rate"
  - "Response time >3 seconds"
  - "N/A" (no threshold, binary alert)
- **Tip:** Document the rationale for threshold values in Notes if it's non-obvious

**Q6: Severity**

- **Question:** What is the severity level of this alert?
- **Dropdown Options:**
  - **Critical** - Immediate threat, requires urgent action (malware download, C2)
  - **High** - Significant risk, respond within SLA (policy violation, service outage)
  - **Medium** - Notable event, investigate when capacity allows
  - **Low** - Informational, routine review
  - **Informational** - FYI only, no action required
- **Auditor Expects:** Severity aligns with organizational risk appetite
- **Common Mistake:** Everything is "Critical" = alert fatigue

**Q7: Notification_Method**

- **Question:** How are relevant personnel notified when this alert fires?
- **Dropdown Options:**
  - **Email** - Email to distribution list
  - **SMS** - Text message
  - **SIEM_Alert** - Alert visible in SIEM console
  - **Ticket** - Automated ticket creation (ServiceNow, Jira)
  - **Dashboard** - Visible on monitoring dashboard
  - **Webhook** - API webhook to external system
  - **PagerDuty** - PagerDuty alert
  - **Teams** - Microsoft Teams notification
  - **Slack** - Slack channel notification
- **Auditor Expects:** Critical/High alerts = active notification (not just dashboard)
- **Best Practice:** Multi-channel for Critical (e.g., "Email + SMS + PagerDuty")

**Q8: Recipients**

- **Question:** Who receives this alert?
- **Format:** Free text - use roles/groups, NOT individual names
- **Examples:**
  - "SOC Team"
  - "Security Engineering + IT Operations"
  - "Web Filtering Admin Group"
  - "CISO (for Critical only)"
  - "Security Operations Manager + On-Call Engineer"
- **Why Roles Not Names:** Personnel change, roles don't
- **Auditor Expects:** Clear ownership, appropriate escalation

**Q9: Response_SLA_Minutes**

- **Question:** What is the maximum time to begin response?
- **Format:** Number (minutes)
- **Common SLAs:**
  - Critical: 15-30 minutes
  - High: 60-120 minutes (1-2 hours)
  - Medium: 240-480 minutes (4-8 hours)
  - Low: 1440 minutes (24 hours)
- **Tip:** SLA should align with severity
- **Auditor Expects:** Defined SLAs for at least Critical/High alerts

**Q10: Escalation_Path**

- **Question:** If initial response doesn't resolve the issue, who is escalated to?
- **Format:** Free text
- **Examples:**
  - "SOC Analyst → SOC Manager → Security Engineering Lead"
  - "On-Call Engineer → IT Operations Manager → CISO"
  - "Tier 1 → Tier 2 → Vendor Support"
  - "None (resolved at first level)"
- **Auditor Expects:** Clear escalation for Critical/High severity alerts
- **Red Flag:** No escalation path for Critical alerts

**Q11: Auto_Response**

- **Question:** Does this alert trigger any automated response actions?
- **Dropdown Options:**
  - **Yes** - Fully automated response (e.g., block IP, isolate user)
  - **No** - Manual response only
  - **Partial** - Some automation (e.g., enrich alert, create ticket)
- **Examples of Automation:**
  - Block source IP at firewall
  - Disable user account
  - Quarantine endpoint
  - Create incident ticket
  - Enrich with threat intelligence
- **Auditor Expects:** High-confidence threats = auto-response when possible
- **Caution:** Auto-response requires careful tuning to avoid false positive impact

**Q12: Status**

- **Question:** What is the current operational status of this alert?
- **Dropdown Options:**
  - **Implemented** - Alert is active and firing correctly
  - **Partial** - Alert exists but needs tuning or is partially functional
  - **Planned** - Alert is designed but not yet implemented
  - **Not_Implemented** - Alert is needed but not configured
  - **N/A** - Not applicable to this environment
- **Auditor Expects:** Most alerts = "Implemented", especially Threat_Detection
- **Red Flag:** Critical threats without corresponding alerts

**Q13: Last_Triggered**

- **Question:** When did this alert last fire?
- **Format:** Date or "Never"
- **Examples:**
  - "15.01.2026"
  - "Never"
  - "10.01.2026"
- **Why This Matters:**
  - "Never" might mean alert is misconfigured OR threat hasn't occurred (both worth investigating)
  - Frequent triggering might indicate tuning needed
- **Auditor Will Ask:** If alert hasn't triggered in 6+ months, how do you know it works?
- **Best Practice:** Test alerts quarterly

**Q14: Evidence_Ref**

- **Question:** What evidence supports this alert configuration?
- **Format:** Reference to Evidence_Register (e.g., "EVID-015")
- **Evidence Types:**
  - Screenshot of alert rule in SIEM
  - Alert configuration export
  - Sample alert notification (email/Teams message)
  - Test alert results
- **Auditor Expects:** Evidence for all "Implemented" alerts

### Section B: Alert Categories Summary

This section provides a **rollup summary** by alert category. It's calculated automatically but you should review it for completeness:

**For each category (Threat_Detection, Policy_Violation, etc.), the summary shows:**

- **Count** - How many alerts in this category
- **Active** - How many are "Implemented"
- **Critical_Count** - How many are Critical severity

**Auditor Will Review:**

- **Threat_Detection count:** Should be highest (this is your primary security function)
- **Zero in a category:** Why? Is that category truly N/A or is it a gap?
- **Critical_Count:** Should be proportional to your threat landscape

### Common Findings

- Too many Critical alerts = alert fatigue
- Too few Threat_Detection alerts = gaps in coverage
- High count of Planned alerts = implementation backlog

### Section C: Summary Metrics

These are **calculated automatically:**

- **Total alert rules configured** - Overall alerting coverage
- **Implemented alerts** - Operational readiness
- **Critical severity alerts** - High-priority monitoring
- **High severity alerts** - Important events
- **Alerts with auto-response** - Automation maturity
- **Alert coverage score** - Percentage implemented

**Target Metrics (Auditor Benchmarks):**

- Alert coverage score: >90% (most alerts implemented)
- At least 10-15 Threat_Detection alerts for comprehensive coverage
- Critical severity alerts should have auto-response or <15 min SLA
- Zero "Not_Implemented" for critical threat types

---

## Sheet 4: Monitoring Dashboard

**Purpose:** Document monitoring dashboards, KPIs tracked, and review processes.

### Section A: Dashboard Inventory (20 dashboards)

**For each dashboard, answer:**

**Q1: Dashboard_ID**

- **Pre-filled:** DSH-001 through DSH-020

**Q2: Dashboard_Name**

- **Question:** What is the name of this dashboard?
- **Examples:**
  - "Web Filtering Executive Summary"
  - "SOC Operational Dashboard"
  - "Blocked Threats - Real-Time"
  - "User Activity Monitoring"
  - "Filtering Service Health"
- **Tip:** Names should indicate audience and purpose

**Q3: Platform**

- **Question:** What platform/tool is this dashboard built in?
- **Dropdown Options:**
  - **SIEM** - Native SIEM dashboard (Splunk, QRadar)
  - **Filtering_Console** - Vendor's native console
  - **Custom** - Custom-built dashboard
  - **PowerBI** - Microsoft Power BI
  - **Grafana** - Grafana OSS or Enterprise
  - **Splunk** - Splunk (if distinct from SIEM)
  - **Cloud_Native** - Cloud provider dashboard (AWS CloudWatch, Azure Monitor)
  - **Excel** - Excel-based dashboard
  - **Other** - Specify in Notes
- **Auditor Expects:** Professional tools (SIEM/BI platforms preferred)
- **Red Flag:** Critical metrics in "Excel" without automation

**Q4: Primary_Audience**

- **Question:** Who is the intended audience for this dashboard?
- **Dropdown Options:**
  - **SOC** - Security Operations Center analysts
  - **Management** - Executive/Management team
  - **IT_Ops** - IT Operations team
  - **Compliance** - Compliance officers, auditors
  - **CISO** - Information Security leadership
  - **All** - Organization-wide dashboard
  - **Security_Team** - Broader security team
- **Best Practice:** Tailor dashboard complexity to audience
  - SOC = technical, real-time, drill-down capable
  - Management = high-level, trends, red/yellow/green
  - Compliance = metrics aligned with requirements

**Q5: Update_Frequency**

- **Question:** How often is the dashboard data refreshed?
- **Dropdown Options:**
  - **Real-Time** - Continuously updated (streaming)
  - **Hourly** - Updates every hour
  - **Daily** - Updates once per day
  - **Weekly** - Updates weekly
  - **Monthly** - Updates monthly
- **Auditor Expects:**
  - SOC dashboards = Real-Time or Hourly
  - Executive dashboards = Daily or Weekly
- **Red Flag:** SOC dashboard updated "Weekly" = not operational

**Q6: Review_Frequency**

- **Question:** How often is this dashboard actively reviewed?
- **Dropdown Options:**
  - **Continuous** - Monitored constantly (24/7 SOC)
  - **Daily** - Reviewed daily
  - **Weekly** - Weekly review meetings
  - **Monthly** - Monthly governance meetings
- **Critical Question:** Is this dashboard USED or just exists?
- **Auditor Will Verify:** Who reviews it? When was last review? Meeting notes?
- **Common Gap:** Beautiful dashboards that nobody looks at = theater

**Q7: Key_Metrics**

- **Question:** What are the main KPIs/metrics shown on this dashboard?
- **Format:** Free text - list 3-5 key metrics
- **Examples:**
  - "Total blocked requests, top threats, user activity, service uptime"
  - "Policy violations by user, by category, trend over 30 days"
  - "MTTR, alert volume, false positive rate, SOC efficiency"
  - "Compliance score, gaps, evidence completeness, audit readiness"
- **Tip:** Be specific - "various metrics" is not acceptable
- **Auditor Expects:** Metrics align with dashboard purpose and audience

**Q8: Alerting_Integrated**

- **Question:** Does this dashboard have alerting capability?
- **Dropdown Options:**
  - **Yes** - Dashboard can generate alerts based on thresholds
  - **No** - Display only, no alerting
- **Examples of Integration:**
  - Dashboard shows "Blocked Requests >1000/hour" and triggers alert if threshold breached
  - KPI turns red AND sends notification
- **Best Practice:** Operational dashboards should integrate with alerting
- **Auditor Expects:** At least SOC/operational dashboards = Yes

**Q9: Status**

- **Question:** What is the operational status of this dashboard?
- **Dropdown Options:**
  - **Implemented** - Dashboard is live and being used
  - **Partial** - Dashboard exists but needs enhancement
  - **Planned** - Dashboard is designed but not built yet
  - **Not_Implemented** - Dashboard needed but doesn't exist
  - **N/A** - Not applicable
- **Auditor Expects:** Most dashboards = "Implemented"
- **Red Flag:** Critical operational dashboards = "Not_Implemented"

**Q10: Evidence_Ref**

- **Question:** What evidence demonstrates this dashboard exists and is used?
- **Format:** Reference to Evidence_Register (e.g., "EVID-025")
- **Evidence Types:**
  - Screenshot of dashboard
  - Meeting notes showing dashboard review
  - Dashboard URL or access path
  - Review schedule documentation
- **Auditor Expects:** Screenshots for all "Implemented" dashboards
- **Tip:** Take screenshots showing actual data, not empty dashboards

### Section B: Key Performance Indicators (20 KPIs)

**For each KPI tracked, document:**

**Q11: KPI_ID**

- **Pre-filled:** KPI-001 through KPI-020

**Q12: KPI_Name**

- **Question:** What is the name of this KPI?
- **Examples:**
  - "Total Blocked Requests per Day"
  - "Malware Block Rate"
  - "False Positive Rate"
  - "Mean Time to Detect (MTTD)"
  - "Mean Time to Respond (MTTR)"
  - "Filtering Service Availability %"
  - "User Exceptions Granted"
  - "Policy Violation Rate"
- **Tip:** Use industry-standard KPI names where possible

**Q13: KPI_Category**

- **Question:** What category does this KPI fall into?
- **Dropdown Options:**
  - **Volume** - Counts, throughput (requests blocked, events logged)
  - **Security** - Security effectiveness (threats blocked, incidents detected)
  - **Performance** - Service performance (uptime, latency, MTTR)
  - **Compliance** - Compliance metrics (policy adherence, audit readiness)
  - **Operational** - Operational efficiency (FP rate, tuning effectiveness)
- **Best Practice:** Balanced KPIs across all categories
- **Auditor Expects:** Not just Volume - need Security and Compliance KPIs

**Q14: Measurement_Unit**

- **Question:** How is this KPI measured?
- **Format:** Free text
- **Examples:**
  - "Events per day"
  - "Percentage (0-100%)"
  - "Minutes"
  - "Count"
  - "Gigabytes"
  - "Requests/second"
- **Tip:** Be specific about units for clarity

**Q15: Target_Value**

- **Question:** What is the target/acceptable value for this KPI?
- **Format:** Free text
- **Examples:**
  - ">99.5%" (for availability)
  - "<2%" (for false positive rate)
  - "<30 minutes" (for MTTR)
  - "0" (for Critical severity incidents)
  - "5000-8000 per day" (for blocked requests - baseline)
- **Auditor Expects:** Defined targets based on risk assessment or industry benchmarks
- **Red Flag:** No targets defined = can't measure effectiveness

**Q16: Current_Value**

- **Question:** What is the current measured value?
- **Format:** Free text - actual measurement
- **Examples:**
  - "99.8%" (exceeds target)
  - "3.5%" (misses target)
  - "22 minutes" (meets target)
  - "6800 per day" (within acceptable range)
- **Source:** Get from dashboards, SIEM reports, or filtering console
- **Auditor Will Verify:** Can you demonstrate how this value was measured?

**Q17: KPI_Status**

- **Question:** Is this KPI meeting its target?
- **Dropdown Options:**
  - **Met** - Current value meets or exceeds target
  - **Not_Met** - Current value below target
  - **At_Risk** - Trending toward missing target
  - **New** - Recently implemented, not enough data
- **Red Flag:** Many "Not_Met" without remediation plans
- **Best Practice:** Monthly KPI review to track trends

**Q18: Trend**

- **Question:** What is the trend over the last 90 days?
- **Dropdown Options:**
  - **Improving** - KPI trending positively
  - **Stable** - KPI relatively constant
  - **Degrading** - KPI trending negatively
  - **New** - Not enough history for trend
  - **Increasing** - For volume metrics that are growing
  - **Decreasing** - For volume metrics that are shrinking
- **Why This Matters:** Trend is often more important than absolute value
- **Example:** "Blocked Requests = Stable at 5K/day" (good) vs "Increasing 50% month-over-month" (investigate!)

**Q19: Tracked_On**

- **Question:** Which dashboard(s) display this KPI?
- **Format:** Free text - reference Dashboard_IDs
- **Examples:**
  - "DSH-001, DSH-003"
  - "SOC Operational Dashboard"
  - "Executive Summary Dashboard"
- **Tip:** Cross-reference to Section A (Dashboard Inventory)
- **Auditor Expects:** Every KPI visible somewhere

**Q20: Evidence_Ref**

- **Question:** What evidence shows this KPI is being tracked?
- **Format:** Reference to Evidence_Register
- **Evidence Types:**
  - Dashboard screenshot showing KPI
  - Report showing KPI values over time
  - KPI definition document
- **Auditor Expects:** Evidence for all actively tracked KPIs

### Section C: Summary Metrics

These are **calculated automatically:**

- **Total KPIs defined** - Breadth of monitoring
- **KPIs meeting target** - Effectiveness
- **KPIs at risk** - Early warning indicators
- **KPIs trending positive** - Improvement trajectory
- **Real-time KPIs** - Operational monitoring depth

**Target Metrics:**

- >80% of KPIs meeting target
- <10% of KPIs "Not_Met" without action plans
- Balanced across categories (not all Volume metrics)

---

## Sheet 5: Incident Response

**Purpose:** Document how web filtering incidents are categorized, handled, and resolved.

### Section A: Incident Categories (10 categories)

**For each incident category, define:**

**Q1: Incident_Category_ID**

- **Pre-filled:** INC-CAT-001 through INC-CAT-010

**Q2: Category_Name**

- **Question:** What is the incident category name?
- **Examples:**
  - "Malware Download Attempt"
  - "Policy Violation - Excessive Blocked Requests"
  - "Filtering Service Outage"
  - "VPN Bypass Detected"
  - "Suspected Data Exfiltration Attempt"
  - "Phishing Site Access"
  - "Configuration Error"
- **Tip:** Categories should align with your alert categories (Sheet 3)

**Q3: Severity_Criteria**

- **Question:** What defines the severity of incidents in this category?
- **Format:** Free text
- **Examples:**
  - "Critical: Confirmed malware downloaded | High: Blocked malware attempt | Medium: Malware URL accessed (no download)"
  - "Critical: Service down >1 hour | High: Degraded performance | Medium: Brief outage <5 minutes"
  - "Critical: Policy violation + data loss | High: Policy violation, no data loss"
- **Auditor Expects:** Clear, objective criteria for severity assignment
- **Best Practice:** Include examples for each severity level

**Q4: Response_SLA_Critical**

- **Question:** What is the SLA for Critical incidents in this category?
- **Format:** Minutes
- **Common Values:**
  - 15 minutes (immediate threats)
  - 30 minutes (serious security events)
  - 60 minutes (urgent but not immediate)
- **Auditor Expects:** Defined SLAs for all categories

**Q5-Q7: Response_SLA for High, Medium, Low**

- **Similar to Q4, but for different severity levels**
- **Typical Progression:**
  - Critical: 15-30 min
  - High: 60-120 min (1-2 hours)
  - Medium: 240-480 min (4-8 hours)
  - Low: 1440 min (24 hours)
- **Tip:** SLAs should be realistic and measurable

**Q8: Escalation_Path**

- **Question:** What is the escalation path for this incident category?
- **Format:** Free text
- **Examples:**
  - "SOC Analyst → SOC Manager → Security Engineering → CISO"
  - "Tier 1 Support → Tier 2 → Vendor Support → Emergency Response Team"
  - "On-Call Engineer → IT Ops Manager → Service Delivery Manager"
- **Auditor Expects:** Clear escalation, especially for Critical/High incidents

**Q9: Runbook_Link**

- **Question:** Where is the incident response runbook/procedure?
- **Format:** Free text - file path, URL, or document reference
- **Examples:**
  - "SharePoint: /SOC/Procedures/Malware_Incident_Response_v3.2.docx"
  - "Confluence: https://wiki.example.com/soc/runbooks/web-filtering-outage"
  - "ISMS-IMP-A.8.23-S5.C Annex B"
  - "ServiceNow KB Article #12345"
- **Auditor Expects:** Documented procedures for at least Critical/High categories
- **Red Flag:** "None" for Critical incidents

**Q10: Evidence_Ref**

- **Question:** What evidence demonstrates this incident category is defined and used?
- **Format:** Reference to Evidence_Register
- **Evidence Types:**
  - Incident categorization matrix
  - Sample incident tickets
  - Runbook document
  - Training materials

### Section B: Incident Handling Procedures (verification)

This section is a **checklist** to verify incident handling procedures exist:

**Q11-Q20: Procedure Verification**

For each procedure element, answer **Yes/No/Partial:**

1. **Incident Detection:** Are procedures defined for how incidents are detected?
2. **Incident Logging:** Is there a standard process for logging incidents?
3. **Initial Assessment:** Is there a triage procedure for new incidents?
4. **Containment:** Are containment actions documented?
5. **Eradication:** Are procedures for removing threats documented?
6. **Recovery:** Are recovery procedures defined?
7. **Post-Incident Review:** Is there a PIR (Post-Incident Review) process?
8. **Documentation Requirements:** Are documentation standards defined?
9. **Communication Plan:** Is there a communication plan for incidents?
10. **Lessons Learned Integration:** Are lessons learned fed back into processes?

**Auditor Expects:** "Yes" for all elements, or documented plans to implement
**Best Practice:** Reference specific sections of ISMS-POL-A.8.23-S5.C (Incident Response Procedures)

### Section C: Recent Incidents (20 recent incidents)

**For each incident, document:**

**Q21: Incident_ID**

- **Pre-filled:** INC-001 through INC-020
- **Tip:** Use your ticketing system's incident numbers if possible

**Q22: Incident_Date**

- **Question:** When did the incident occur?
- **Format:** Date (DD.MM.YYYY)
- **Source:** Incident ticket, SIEM alert timestamp

**Q23: Incident_Category**

- **Question:** What category does this incident fall into?
- **Dropdown:** Should match categories from Section A
- **Tip:** Consistent categorization helps with trend analysis

**Q24: Severity**

- **Question:** What severity was assigned?
- **Dropdown:** Critical, High, Medium, Low
- **Auditor Will Verify:** Does assigned severity match criteria from Section A?

**Q25: Detection_Method**

- **Question:** How was this incident detected?
- **Dropdown Options:**
  - **Alert** - Automated alert
  - **User_Report** - User reported the issue
  - **SOC_Review** - Found during SOC monitoring
  - **Audit** - Discovered during audit/review
  - **Vendor_Notification** - Vendor informed us
  - **Threat_Intel** - Threat intelligence feed
- **Auditor Expects:** Most incidents = "Alert" (proactive detection)
- **Red Flag:** Many "User_Report" = detection gaps

**Q26: Time_to_Detect_Minutes**

- **Question:** How long from event occurrence to detection?
- **Format:** Number (minutes)
- **How to Calculate:** Incident timestamp - Event timestamp
- **Example:** Malware download at 10:05, alert fired at 10:07 = 2 minutes
- **Auditor Expects:** Real-time detection for Critical threats (<5 minutes)
- **Best Practice:** Track MTTD (Mean Time to Detect) as KPI

**Q27: Time_to_Respond_Minutes**

- **Question:** How long from detection to initial response?
- **Format:** Number (minutes)
- **How to Calculate:** First response action timestamp - Detection timestamp
- **Auditor Will Compare:** Did you meet the SLA from Section A?
- **Red Flag:** Many SLA breaches without documented reasons

**Q28: Containment_Actions**

- **Question:** What actions were taken to contain the incident?
- **Format:** Free text - brief description
- **Examples:**
  - "Blocked source IP at firewall, isolated user endpoint"
  - "Disabled user account, cleared browser cache"
  - "Added domain to block list, notified affected users"
  - "No containment needed - threat automatically blocked"
- **Auditor Expects:** Documented containment for High/Critical incidents

**Q29: Resolution_Status**

- **Question:** What is the current status of this incident?
- **Dropdown Options:**
  - **Resolved** - Incident fully resolved
  - **Open** - Still being worked
  - **Escalated** - Escalated to next level
  - **Pending** - Waiting for external input
  - **Closed** - Resolved and closed after PIR
- **Auditor Expects:** Old incidents should be Resolved/Closed
- **Red Flag:** Many incidents stuck in "Open" for weeks

**Q30: PIR_Completed**

- **Question:** Was a Post-Incident Review completed?
- **Dropdown:** Yes, No, N/A
- **Auditor Expects:** "Yes" for all Critical/High incidents
- **PIR Should Include:**
  - Root cause analysis
  - Timeline of events
  - Lessons learned
  - Recommendations for improvement
- **Evidence:** PIR report document

**Q31: Evidence_Ref**

- **Question:** What evidence supports this incident documentation?
- **Format:** Reference to Evidence_Register
- **Evidence Types:**
  - Incident ticket
  - SIEM alert log
  - PIR report
  - Email threads
  - Containment action logs

### Section D: Summary Metrics

These are **calculated automatically:**

- **Total incidents in period** - Incident volume
- **Critical/High incidents** - Serious event count
- **Average MTTD** - Mean Time to Detect
- **Average MTTR** - Mean Time to Respond
- **SLA compliance rate** - Percentage of incidents meeting SLA
- **PIR completion rate** - Percentage of High/Critical with PIR

**Target Metrics:**

- SLA compliance >95%
- MTTD <5 minutes for Critical
- MTTR within defined SLAs
- PIR completion 100% for Critical incidents

---

## Sheet 6: Blocked Events Analysis

**Purpose:** Analyze trends in blocked web requests to assess threat landscape and filtering effectiveness.

### Section A: Blocked Events by Category (10 threat categories)

**For each threat category, document:**

**Q1: Threat_Category**

- **Question:** What threat category is this?
- **Pre-defined Categories:**
  - Malware
  - Phishing
  - Command & Control (C2)
  - Exploit Kits
  - Cryptomining
  - Ransomware
  - Botnets
  - Data Exfiltration
  - Adult Content (if blocked per policy)
  - Unauthorized Cloud Apps (if blocked per policy)
- **Tip:** Categories should align with your filtering policies (A.8.23.3)

**Q2: Total_Blocks_Last_30_Days**

- **Question:** How many requests in this category were blocked in the last 30 days?
- **Format:** Number
- **Source:** SIEM query, filtering console statistics
- **Example:** "47,392" (forty-seven thousand malware blocks)
- **Auditor Will Ask:** How did you obtain this number? (must be verifiable)

**Q3: Total_Blocks_Last_90_Days**

- **Question:** How many requests in this category were blocked in the last 90 days?
- **Format:** Number
- **Why This Matters:** Trend analysis - is threat increasing or decreasing?

**Q4: Trend_Direction**

- **Question:** What is the trend over time?
- **Dropdown Options:**
  - **Increasing** - Block count growing
  - **Stable** - Relatively constant
  - **Decreasing** - Block count declining
  - **Seasonal** - Varies by time period
  - **New** - Category recently added
- **How to Determine:** Compare 30-day vs 90-day averages
- **Auditor Expects:** Explanation for significant increases

**Q5: Top_Blocked_Domains**

- **Question:** What are the top 3-5 domains blocked in this category?
- **Format:** Free text - comma-separated list
- **Examples:**
  - "malicious-example.com, evil-site.net, badactor.org"
  - "Various phishing sites (no repeating domains)"
  - "Multiple C2 domains (threat intel feed)"
- **Why This Matters:**
  - Recurring domains = possible false positive
  - Diverse domains = legitimate threat blocking
  - One domain = possible misclassification

**Q6: False_Positive_Suspected**

- **Question:** Are any of these blocks suspected false positives?
- **Dropdown:** Yes, No, Possible
- **If Yes:** You should have FP tracking in Sheet 7
- **Auditor Will Ask:** What is your FP investigation process?

**Q7: Actionable_Intelligence**

- **Question:** Did this category provide any actionable threat intelligence?
- **Format:** Free text
- **Examples:**
  - "Detected employee visiting known phishing kit hosting site - security awareness gap"
  - "C2 traffic from legacy server - compromised system identified and isolated"
  - "No actionable intel - routine blocking of known bad sites"
  - "Identified need to update browser security settings for cryptomining protection"
- **Auditor Expects:** Evidence that you're LEARNING from blocked events, not just counting them

**Q8: Evidence_Ref**

- **Question:** What evidence supports this analysis?
- **Format:** Reference to Evidence_Register
- **Evidence Types:**
  - SIEM report showing block statistics
  - Filtering console screenshot
  - Threat intelligence report
  - SQL query results

### Section B: Geographic Analysis (10 countries)

**For the top 10 source countries, document:**

**Q9: Country**

- **Question:** What country is this?
- **Format:** Country name or ISO code
- **Examples:** "United States", "China", "Russia", "Unknown/VPN"
- **Source:** GeoIP data from logs

**Q10: Total_Blocks**

- **Question:** How many blocks from this country in last 30 days?
- **Format:** Number
- **Why This Matters:**
  - High volume from unexpected countries = investigate
  - All blocks from one country = possible attack campaign
  - Distributed globally = normal threat landscape

**Q11: Primary_Threat_Type**

- **Question:** What type of threats primarily originate from this country?
- **Examples:**
  - "Malware distribution"
  - "Phishing campaigns"
  - "C2 traffic"
  - "Mixed threats"
- **Tip:** This helps identify attack patterns

**Q12: Action_Taken**

- **Question:** What action (if any) was taken based on this analysis?
- **Examples:**
  - "Added country-level block for non-business traffic"
  - "Increased monitoring for this region"
  - "No action - within expected threat profile"
  - "Investigated - found compromised VPN exit node"
- **Auditor Expects:** Evidence that analysis leads to action

### Section C: Summary Metrics

These are **calculated automatically:**

- **Total blocked requests (30 days)** - Overall volume
- **Total blocked requests (90 days)** - Trend baseline
- **Categories with increasing trends** - Emerging threats
- **Suspected false positive categories** - Tuning needed
- **Top 3 threat categories** - Primary threats
- **Geographic diversity score** - Threat distribution

### What Good Looks Like

- Blocked volume consistent with threat landscape
- No single category dominating (unless expected)
- Few suspected FPs (<5% of categories)
- Analysis leading to actionable improvements

---

## Sheet 7: False Positive Management

**Purpose:** Track false positives, document resolution, and improve filtering accuracy.

### Section A: False Positive Inventory (30 FPs)

**For each false positive case, document:**

**Q1: FP_ID**

- **Pre-filled:** FP-001 through FP-030

**Q2: Date_Reported**

- **Question:** When was this false positive reported?
- **Format:** Date (DD.MM.YYYY)
- **Source:** User report, SOC investigation

**Q3: Blocked_URL**

- **Question:** What URL was incorrectly blocked?
- **Format:** Full URL or domain
- **Examples:**
  - "https://legitimate-vendor.com/api/endpoint"
  - "internal-app.company.com"
  - "cdn.example-cloud-service.net"
- **Privacy Note:** Mask PII if URL contains sensitive parameters

**Q4: Category_Assigned**

- **Question:** What category was this URL incorrectly classified as?
- **Examples:**
  - "Malware" (but it's a legitimate software download)
  - "Phishing" (but it's a security training site)
  - "Adult Content" (but it's a medical information site)
- **Auditor Expects:** Clear documentation of misclassification

**Q5: Legitimate_Purpose**

- **Question:** What is the legitimate business purpose for this URL?
- **Format:** Free text
- **Examples:**
  - "Vendor API endpoint for payment processing - business critical"
  - "Cloud storage used by Marketing team for campaigns"
  - "Security awareness training platform (simulates phishing)"
  - "Partner extranet for supply chain collaboration"
- **Auditor Expects:** Documented justification for ALL exceptions
- **Red Flag:** "User wanted access" without business rationale

**Q6: Reported_By**

- **Question:** Who reported this FP?
- **Format:** Free text - role/department, not individual names
- **Examples:**
  - "Finance Department"
  - "SOC Analyst"
  - "IT Helpdesk (user escalation)"
  - "Security Engineering (proactive review)"
- **Why Not Names:** Privacy, personnel changes
- **Pattern Analysis:** If one department reports many FPs, investigate policy alignment

**Q7: Investigation_Findings**

- **Question:** What did investigation reveal?
- **Format:** Free text - detailed findings
- **Examples:**
  - "Confirmed FP - URL categorized incorrectly by vendor feed"
  - "Confirmed FP - Internal application not in allow list"
  - "Not FP - URL recently compromised, correct block"
  - "Partial FP - Legitimate site but hosting malicious ad network"
- **Auditor Expects:** Evidence of thorough investigation
- **Best Practice:** Document investigation process and tools used

**Q8: FP_Result**

- **Question:** What was the final determination?
- **Dropdown Options:**
  - **Confirmed_FP** - Definitively a false positive
  - **True_Positive** - Block was correct, not a FP
  - **Inconclusive** - Cannot determine definitively
  - **Pending** - Investigation ongoing
- **Auditor Expects:** Clear determination before resolution
- **Red Flag:** Many "Inconclusive" = poor investigation process

**Q9: Resolution_Action**

- **Question:** What action was taken to resolve this FP?
- **Dropdown Options:**
  - **Whitelist** - Added to allow list
  - **Policy_Tuning** - Adjusted policy to reduce FPs
  - **Category_Update** - Requested vendor to recategorize
  - **No_Action** - Determined to be true positive after all
  - **Escalated** - Escalated to vendor support
  - **Vendor_Update** - Waiting for vendor database update
- **Examples:**
  - "Whitelist: Added *.vendor.com to allow list for Finance team only"
  - "Policy_Tuning: Adjusted threshold for 'suspicious' category"
  - "Category_Update: Submitted recategorization request to vendor (ticket #12345)"

**Q10: Resolution_Date**

- **Question:** When was this FP resolved?
- **Format:** Date (DD.MM.YYYY)
- **How to Calculate Time to Resolution:** Resolution_Date - Date_Reported
- **Auditor Expects:** Timely resolution (target: <48 hours for business-critical)

**Q11: FP_Recurrence**

- **Question:** Is this a recurring FP or first occurrence?
- **Dropdown Options:**
  - **First_Time** - First occurrence
  - **Recurring** - Happened before
  - **Chronic** - Persistent issue (3+ occurrences)
- **Red Flag:** Many "Chronic" FPs = policy tuning problem
- **Best Practice:** Root cause analysis for recurring FPs

**Q12: Root_Cause**

- **Question:** What was the root cause of this FP?
- **Format:** Free text
- **Common Root Causes:**
  - "Vendor categorization error"
  - "Internal application not in custom allow list"
  - "Policy too restrictive for department needs"
  - "CDN/hosting provider hosting mixed content"
  - "New legitimate site mistakenly flagged"
  - "Threat intelligence false positive"
- **Auditor Expects:** Root cause for Recurring/Chronic FPs
- **Why This Matters:** Enables systemic improvements

**Q13: Prevention_Measure**

- **Question:** What measure was implemented to prevent recurrence?
- **Format:** Free text
- **Examples:**
  - "Added wildcard whitelist for all vendor subdomains"
  - "Updated policy to use less aggressive blocking for 'Suspicious' category"
  - "Implemented weekly vendor feed review process"
  - "Created exception process for new internal applications"
  - "None required - legitimate new threat that has since been resolved"
- **Auditor Expects:** Prevention measures for Recurring/Chronic FPs
- **Best Practice:** Document prevention in FP management procedures

**Q14: FP_Status**

- **Question:** What is the current status of this FP case?
- **Dropdown Options:**
  - **Open** - Being investigated
  - **Resolved** - Fixed and verified
  - **Escalated** - Escalated to vendor
  - **Pending** - Waiting for external action (vendor recategorization)
- **Auditor Expects:** Old FPs should be Resolved
- **Red Flag:** Many FPs stuck in "Pending" = poor vendor relationship

**Q15: Evidence_Ref**

- **Question:** What evidence supports this FP case?
- **Format:** Reference to Evidence_Register
- **Evidence Types:**
  - User report ticket
  - Investigation notes
  - Screenshot of block page
  - Whitelist configuration change
  - Vendor support ticket
  - Post-resolution verification test

### Section B: FP Analysis Summary

These are **calculated automatically:**

- **Total FPs reported (30 days)** - FP volume
- **Confirmed FPs** - Actual false positives
- **Average time to resolution** - FP handling efficiency
- **Recurring FPs** - Tuning effectiveness
- **Chronic FPs** - Systemic issues
- **FP rate** - FPs as percentage of total blocks

**Target Metrics:**

- FP rate <1% (ideally <0.5%)
- Time to resolution <48 hours for business-critical
- Recurring FPs <10% of total FPs
- Chronic FPs = 0 (all resolved with prevention)

**Auditor Will Ask:**

- Do you track FPs systematically?
- Is there a documented FP investigation process?
- Are recurring FPs being addressed at root cause level?
- What is your FP trend over the last 6 months?

---

## Sheet 8: Reporting Schedule

**Purpose:** Document regular reports generated from web filtering monitoring.

### Section A: Report Inventory (20 reports)

**For each report, document:**

**Q1: Report_ID**

- **Pre-filled:** RPT-001 through RPT-020

**Q2: Report_Name**

- **Question:** What is the name of this report?
- **Examples:**
  - "Daily SOC Web Filtering Summary"
  - "Weekly Executive Web Security Report"
  - "Monthly Compliance Metrics Report"
  - "Quarterly Trend Analysis"
  - "Incident Summary Report (Ad-hoc)"
- **Tip:** Names should indicate content, audience, and frequency

**Q3: Report_Type**

- **Question:** What type of report is this?
- **Dropdown Options:**
  - **Operational** - Daily/routine operations
  - **Compliance** - Regulatory/audit requirements
  - **Executive** - Leadership/board reporting
  - **Incident** - Incident-specific reports
  - **Trend** - Trend analysis and forecasting
  - **Audit** - Audit-specific reports
  - **Ad-hoc** - On-demand reporting
- **Best Practice:** Mix of Operational, Compliance, and Executive reports

**Q4: Frequency**

- **Question:** How often is this report generated?
- **Dropdown Options:**
  - **Daily** - Every day
  - **Weekly** - Once per week
  - **Monthly** - Once per month
  - **Quarterly** - Every 3 months
  - **Annual** - Once per year
  - **Ad-hoc** - On-demand
- **Auditor Expects:** Frequency appropriate to report type and audience
- **Best Practice:** Operational = Daily/Weekly, Executive = Monthly/Quarterly

**Q5: Primary_Audience**

- **Question:** Who receives this report?
- **Format:** Free text - roles/groups
- **Examples:**
  - "SOC Team, Security Engineering"
  - "CISO, IT Director"
  - "Compliance Officer, Internal Audit"
  - "Board of Directors (quarterly only)"
  - "All Managers (monthly)"
- **Why Roles Not Names:** Personnel change, roles don't
- **Auditor Expects:** Audience appropriate to report content

**Q6: Key_Metrics_Included**

- **Question:** What are the main metrics in this report?
- **Format:** Free text - list key metrics
- **Examples:**
  - "Total blocks, top threats, FP rate, SLA compliance, open incidents"
  - "Compliance score, audit readiness, gaps, evidence status"
  - "Threat trends, geographic analysis, policy violations, service uptime"
- **Tip:** Be specific - helps evaluate report effectiveness

**Q7: Generation_Method**

- **Question:** How is this report generated?
- **Dropdown Options:**
  - **Automated** - Fully automated (script, SIEM, BI tool)
  - **Manual** - Manually created
  - **Semi-Automated** - Partial automation (data gathered automatically, formatted manually)
- **Auditor Expects:** Operational reports = Automated or Semi-Automated
- **Red Flag:** Daily/Weekly reports = Manual (not sustainable)
- **Best Practice:** Automate wherever possible to reduce errors and save time

**Q8: Delivery_Method**

- **Question:** How is this report delivered to recipients?
- **Dropdown Options:**
  - **Email** - Emailed as attachment or body
  - **Portal** - Posted to portal/SharePoint
  - **Dashboard** - Always-on dashboard
  - **File_Share** - Saved to shared drive
  - **Meeting** - Presented in meeting
  - **API** - Delivered via API to another system
- **Best Practice:** Multiple delivery methods for different audiences
- **Example:** Operational reports = Dashboard, Executive reports = Email + Meeting

**Q9: Last_Generated**

- **Question:** When was this report last generated?
- **Format:** Date (DD.MM.YYYY)
- **Auditor Will Verify:** Is "Last_Generated" consistent with "Frequency"?
- **Red Flag:** Weekly report last generated 2 months ago = not being used

**Q10: Report_Effectiveness**

- **Question:** Is this report effective and used by recipients?
- **Dropdown Options:**
  - **High** - Report actively used, drives decisions
  - **Medium** - Report read but limited action
  - **Low** - Report rarely used or read
  - **Unknown** - No feedback from recipients
- **Auditor Expects:** Evidence that reports are USED, not just generated
- **Best Practice:** Periodic review with recipients to assess effectiveness

**Q11: Status**

- **Question:** What is the operational status of this report?
- **Dropdown Options:**
  - **Implemented** - Report active and being generated
  - **Partial** - Report exists but needs improvement
  - **Planned** - Report designed but not yet implemented
  - **Not_Implemented** - Report needed but doesn't exist
  - **Discontinued** - Report no longer generated
- **Auditor Expects:** Most reports = "Implemented"
- **Tip:** If "Discontinued", document why in Notes

**Q12: Evidence_Ref**

- **Question:** What evidence demonstrates this report exists and is used?
- **Format:** Reference to Evidence_Register
- **Evidence Types:**
  - Sample report (most recent version)
  - Email distribution proof
  - Meeting minutes where report was presented
  - Recipient feedback
- **Auditor Expects:** Sample reports for all "Implemented" reports

### Section B: Summary Metrics

These are **calculated automatically:**

- **Total reports defined** - Reporting breadth
- **Active reports** - Operational reports
- **Automated reports** - Automation maturity
- **Daily/Weekly reports** - Operational monitoring depth
- **Executive reports** - Leadership visibility
- **Report effectiveness score** - Percentage "High" effectiveness

**Target Metrics:**

- >80% of reports Implemented
- >50% of Operational reports Automated
- >70% report effectiveness "High" or "Medium"
- At least one Executive report monthly or quarterly

---

## Sheet 9: Gap Analysis

**Purpose:** Identify and track gaps in monitoring and response capabilities.

### Gap Inventory (30 gaps)

**For each identified gap, document:**

**Q1: Gap_ID**

- **Pre-filled:** GAP-001 through GAP-030

**Q2: Gap_Category**

- **Question:** What category does this gap fall into?
- **Dropdown Options:**
  - **Logging** - Missing log sources, retention issues
  - **Alerting** - Missing alerts, misconfigured rules
  - **Monitoring** - Dashboard gaps, missing KPIs
  - **Incident_Response** - Procedure gaps, SLA compliance
  - **Reporting** - Missing or ineffective reports
  - **Integration** - Integration gaps between systems
  - **Retention** - Log retention compliance
  - **Process** - Process/procedure gaps
- **Tip:** Category helps prioritize and assign ownership

**Q3: Gap_Description**

- **Question:** What specifically is the gap?
- **Format:** Free text - be specific
- **Good Examples:**
  - "DNS filtering logs not being forwarded to SIEM - no visibility into DNS-layer threats"
  - "No alert for excessive blocked requests from single user (>100/hour) - potential compromise indicator not detected"
  - "SOC operational dashboard not reviewed daily - defeats purpose of real-time monitoring"
  - "No documented runbook for 'Filtering Service Outage' incident category"
  - "Log retention only 30 days but PCI DSS requires 90 days"
- **Bad Examples:**
  - "Monitoring could be better" (too vague)
  - "Need more logs" (not specific)
  - "Alerts not working" (which alerts? how not working?)

**Q4: Impact**

- **Question:** What is the business/security impact of this gap?
- **Format:** Free text
- **Examples:**
  - "Cannot detect DNS tunneling or DNS-based C2 communication"
  - "Compromised accounts may go undetected for days"
  - "Dashboards exist but provide no operational value"
  - "Incident response delayed due to lack of procedures"
  - "Regulatory compliance risk - non-compliant with PCI DSS"
- **Auditor Expects:** Clear articulation of risk
- **Tip:** Impact should justify the priority level

**Q5: Priority**

- **Question:** What is the priority for remediating this gap?
- **Dropdown Options:**
  - **Critical** - Address within 30 days
  - **High** - Address within 90 days
  - **Medium** - Address within 180 days
  - **Low** - Address within 12 months
- **How to Determine Priority:**
  - Regulatory compliance gap = Critical or High
  - Detection/alerting gap for Critical threats = Critical
  - Process improvement = Medium or Low
  - Nice-to-have enhancement = Low
- **Auditor Expects:** Priority aligns with impact and risk

**Q6: Remediation_Plan**

- **Question:** What is the plan to remediate this gap?
- **Format:** Free text - specific action steps
- **Good Examples:**
  - "Configure DNS filtering appliance to forward logs to SIEM via syslog (port 514/TCP). Test connectivity. Create SIEM parser. Validate log ingestion. ETA: 2 weeks."
  - "Create alert rule: 'Blocked Requests >100/hour per user'. Set threshold. Configure notification to SOC email + SIEM alert. Test rule. Document in alert inventory. ETA: 1 week."
  - "Update SOC procedures to include daily dashboard review as first task. Assign responsibility to SOC Shift Lead. Add checklist item. Track compliance weekly. ETA: Immediate."
  - "Draft runbook for filtering service outage. Include detection, containment, escalation, recovery steps. Review with SOC. Obtain approval. Publish to wiki. ETA: 1 month."
- **Bad Examples:**
  - "Fix the problem" (not a plan)
  - "Look into it" (no action steps)
  - "TBD" (not acceptable for High/Critical gaps)
- **Auditor Expects:** Specific, actionable plan with steps

**Q7: Owner**

- **Question:** Who is responsible for remediating this gap?
- **Format:** Free text - role/department
- **Examples:**
  - "Security Engineering"
  - "SOC Manager"
  - "IT Operations + Security Engineering (joint)"
  - "CISO (approve budget), Security Engineering (implement)"
- **Auditor Expects:** Clear ownership
- **Red Flag:** "TBD" or "Unknown" for High/Critical gaps

**Q8: Target_Date**

- **Question:** When is remediation expected to be complete?
- **Format:** Date (DD.MM.YYYY)
- **How to Determine:** Based on priority:
  - Critical: Within 30 days
  - High: Within 90 days
  - Medium: Within 180 days
  - Low: Within 12 months
- **Auditor Will Verify:** Is target date realistic given resources?
- **Red Flag:** Critical gap with target date 6 months out

**Q9: Gap_Status**

- **Question:** What is the current status of remediation?
- **Dropdown Options:**
  - **Open** - Not yet started
  - **In_Progress** - Actively being worked
  - **Resolved** - Remediation complete, verified
  - **Accepted** - Risk accepted, no remediation planned
  - **Deferred** - Remediation postponed (document reason in Notes)
- **Auditor Expects:**
  - Recent gaps = Open or In_Progress
  - Old gaps = Resolved or documented reason for delay
- **Red Flag:** Many "Open" gaps with missed target dates

**Q10: Resolution_Date**

- **Question:** When was this gap resolved? (if applicable)
- **Format:** Date (DD.MM.YYYY) or blank if not yet resolved
- **Auditor Will Calculate:** Time to resolution = Resolution_Date - Date_Identified
- **Best Practice:** Track closure time for continuous improvement

**Q11: Evidence_Ref**

- **Question:** What evidence demonstrates gap resolution?
- **Format:** Reference to Evidence_Register
- **Evidence Types for Resolved Gaps:**
  - Configuration change ticket
  - Updated procedure document
  - Test results
  - Before/after screenshots
  - Approval email
- **Auditor Expects:** Evidence for ALL "Resolved" gaps
- **Tip:** Gather evidence during remediation, not later

**Q12: Notes**

- **Question:** Any additional context?
- **Examples:**
  - "Dependent on Q2 budget approval for storage upgrade"
  - "Risk accepted by CISO due to low probability and residual controls"
  - "Deferred until after infrastructure migration project"
  - "Root cause: Vendor changed default log format in v3.2 upgrade"

### Gap Analysis Summary

These are **calculated automatically:**

- **Total gaps identified** - Breadth of gap analysis
- **Critical gaps** - High-priority items
- **High gaps** - Urgent items
- **Gaps in remediation** - In_Progress count
- **Resolved gaps** - Closure rate
- **Gap closure rate** - Percentage resolved
- **Average time to resolve** - Efficiency metric

**Target Metrics:**

- Critical gaps = 0 (or in-progress with target dates)
- Gap closure rate >80% (most gaps resolved)
- Average time to resolve: <90 days for High, <30 days for Critical

---

## Sheet 10: Evidence Register

**Purpose:** Catalog all supporting evidence for audit traceability.

### Evidence Inventory (100 evidence items)

**For each evidence item, document:**

**Q1: Evidence_ID**

- **Pre-filled:** EVID-001 through EVID-100

**Q2: Evidence_Type**

- **Question:** What type of evidence is this?
- **Dropdown Options:**
  - **Screenshot** - Screenshot of configuration, dashboard, logs
  - **Configuration_Export** - Configuration file export
  - **Log_Sample** - Sample log file or log entries
  - **Report** - Generated report document
  - **Procedure_Document** - SOP, runbook, procedure
  - **Email_Confirmation** - Email thread or approval
  - **Audit_Report** - Audit findings, assessment results
  - **Test_Results** - Test execution results
  - **Policy_Document** - Policy or standard document
  - **Meeting_Minutes** - Meeting notes, decisions
  - **Other** - Specify in Description

**Q3: Description**

- **Question:** What does this evidence show?
- **Format:** Free text - clear, descriptive
- **Examples:**
  - "SIEM screenshot showing DNS filter logs being ingested - 15.01.2026"
  - "Alert rule configuration export for 'Malware Download Attempt' alert"
  - "Sample of blocked requests log showing threat categorization"
  - "Weekly SOC Web Filtering Summary report for week of 06.01.2026"
  - "Post-Incident Review report for INC-2025-00234 (malware incident)"
  - "Email approval from CISO for whitelist exception request EXC-045"

**Q4: Referenced_By**

- **Question:** Which assessment items reference this evidence?
- **Format:** Free text - sheet name and row or item ID
- **Examples:**
  - "Sheet 2, LOG-003 (DNS Filter logs)"
  - "Sheet 3, ALR-015 (Malware alert)"
  - "Sheet 5, INC-007 (Incident PIR)"
  - "Sheet 8, RPT-002 (Weekly report)"
  - "Multiple: LOG-005, ALR-020, DSH-003"
- **Auditor Will Verify:** Cross-reference between sheets and evidence

**Q5: File_Location**

- **Question:** Where is this evidence stored?
- **Format:** Free text - file path or URL
- **Examples:**
  - "SharePoint: /ISMS/Evidence/A.8.23/Monitoring/SIEM_DNS_Logs_20260115.png"
  - "Network Drive: Z:\\Security\\Audit Evidence\\2026\\Q1\\alert_config_export.json"
  - "Confluence: https://wiki.example.com/security/evidence/a823/pir-inc-234"
  - "Email: CISO approval email dated 15.01.2026, Subject: 'RE: Whitelist Exception Request'"
  - "Attached to this workbook as embedded file"
- **Best Practice:** Centralized evidence repository (SharePoint, Confluence)
- **Auditor Expects:** Evidence readily accessible and retrievable

**Q6: Date_Collected**

- **Question:** When was this evidence collected/created?
- **Format:** Date (DD.MM.YYYY)
- **Tip:** Evidence should be recent and reflect current state
- **Auditor Will Check:** Is evidence current or outdated?

**Q7: Collected_By**

- **Question:** Who collected/created this evidence?
- **Format:** Free text - role/name
- **Examples:**
  - "SOC Analyst (J. Smith)"
  - "Security Engineering Team"
  - "SIEM Administrator"
  - "Assessment Coordinator"
- **Why This Matters:** Traceability and accountability

**Q8: Verification_Status**

- **Question:** Has this evidence been verified as accurate and current?
- **Dropdown Options:**
  - **Verified** - Evidence confirmed accurate
  - **Pending** - Awaiting verification
  - **Not_Verified** - Not yet verified
  - **Expired** - Evidence outdated, needs refresh
- **Auditor Expects:** All evidence = "Verified" before final approval
- **Best Practice:** Evidence review during internal QA phase

**Q9: Notes**

- **Question:** Any additional context about this evidence?
- **Examples:**
  - "Screenshot taken during production hours showing real data"
  - "Configuration export sanitized to remove sensitive IPs"
  - "Report covers period 01.01.2026 - 07.01.2026"
  - "Evidence shows 'before' state - 'after' screenshot in EVID-046"

### Evidence Summary Metrics

These are **calculated automatically:**

- **Total evidence items** - Evidence breadth
- **Verified evidence** - Quality assurance completion
- **Evidence by type** - Evidence type distribution
- **Pending verification** - Outstanding items
- **Expired evidence** - Items needing refresh

**Auditor Benchmarks:**

- Evidence completeness >95%
- All evidence = "Verified" before final approval
- Evidence organized and accessible
- Evidence current (within last 90 days for most items)

---

## Sheet 11: Approval Sign-Off

**Purpose:** Document three-level approval workflow.

### Approval Workflow

**Level 1: Operational Approval**

**Q1: Approver Name**

- **Format:** Full name
- **Role:** SOC Manager or Security Operations Lead
- **Responsibility:** Verify operational accuracy and completeness

**Q2: Approver Role**

- **Format:** Job title
- **Example:** "SOC Manager", "Security Operations Lead"

**Q3: Approval Date**

- **Format:** Date (DD.MM.YYYY)

**Q4: Approval Status**

- **Dropdown:** Approved, Conditionally_Approved, Rejected, Pending
- **Conditionally_Approved:** Minor corrections needed
- **Rejected:** Significant issues, return for rework

**Q5: Comments**

- **Format:** Free text
- **Examples:**
  - "Approved - operational data accurate and complete"
  - "Conditionally approved - update FP resolution timeline for FP-015 and FP-022, then resubmit"
  - "Rejected - missing log sources for remote workers, incomplete incident data"

---

**Level 2: Technical Approval**

**Q6: Approver Name**

- **Format:** Full name
- **Role:** Security Engineering Lead or Infrastructure Manager
- **Responsibility:** Verify technical completeness and architecture alignment

**Q7: Approver Role**

- **Format:** Job title
- **Example:** "Security Engineering Lead", "Infrastructure Security Manager"

**Q8: Approval Date**

- **Format:** Date (DD.MM.YYYY)

**Q9: Approval Status**

- **Dropdown:** Approved, Conditionally_Approved, Rejected, Pending

**Q10: Comments**

- **Format:** Free text
- **Examples:**
  - "Approved - monitoring and response capabilities well-documented"
  - "Conditionally approved - add evidence for ALR-025 and ALR-030 alert rules"
  - "Approved with recommendation to prioritize GAP-003 and GAP-007 for Q2"

---

**Level 3: Executive Approval**

**Q11: Approver Name**

- **Format:** Full name
- **Role:** CISO or Information Security Manager
- **Responsibility:** Final strategic review, risk acceptance for gaps

**Q12: Approver Role**

- **Format:** Job title
- **Example:** "CISO", "Information Security Manager"

**Q13: Approval Date**

- **Format:** Date (DD.MM.YYYY)

**Q14: Approval Status**

- **Dropdown:** Approved, Conditionally_Approved, Rejected, Pending

**Q15: Comments**

- **Format:** Free text
- **Examples:**
  - "Approved - assessment ready for audit. Well done team."
  - "Approved with noted acceptance of GAP-012 (DNS log retention 30 days) until budget approval in Q2."
  - "Conditionally approved - remediation plans for Critical gaps must have specific budget allocations and resources assigned before final approval."

---

**Assessment Metadata**

**Q16: Assessment Completion Date**

- **Question:** When was data collection completed?
- **Format:** Date (DD.MM.YYYY)

**Q17: Next Review Date**

- **Question:** When is next quarterly review scheduled?
- **Format:** Date (DD.MM.YYYY)
- **Calculation:** Assessment Completion Date + 90 days

**Q18: Overall Assessment Status**

- **Dropdown:** Draft, Under_Review, Approved, Audit_Ready
- **Progression:**
  - Draft → Under_Review (after submission for approval)
  - Under_Review → Approved (after all three levels approve)
  - Approved → Audit_Ready (after evidence verified and gaps documented)

**Q19: Audit Readiness Confirmation**

- **Dropdown:** Yes, No, Pending
- **Criteria for "Yes":**
  - All three approval levels = "Approved"
  - All evidence = "Verified" status
  - All High/Critical gaps have documented remediation plans
  - Evidence register is complete and accessible

**Q20: Final Notes**

- **Format:** Free text
- **Purpose:** Any final comments for the record
- **Examples:**
  - "Assessment aligns with Stage-2 ISO 27001 certification preparation"
  - "Identified 12 gaps, 3 Critical, 5 High - all with remediation plans"
  - "Monitoring and response capabilities assessed as mature and audit-ready"

---

# Evidence Collection

## Evidence Strategy

**For each sheet, collect supporting evidence:**

### Sheet 2: Log Collection
- **SIEM screenshots** showing log ingestion from filtering sources
- **Configuration exports** from filtering devices showing logging enabled
- **Log retention policies** (documented)
- **Sample log files** (sanitized) showing format and content

### Sheet 3: Alert Configuration
- **Alert rule exports** from SIEM (JSON, XML, or screenshots)
- **Sample alert notifications** (email, Teams, Slack)
- **Alert testing results** (triggered test alerts)
- **Escalation matrix** document

### Sheet 4: Monitoring Dashboard
- **Dashboard screenshots** showing KPIs and real-time data
- **Dashboard access logs** (proof of regular review)
- **KPI definition documents**
- **Meeting notes** from dashboard review sessions

### Sheet 5: Incident Response
- **Incident tickets** (sample from each category)
- **Runbook/procedure documents**
- **Post-Incident Review reports**
- **SLA compliance reports**

### Sheet 6: Blocked Events Analysis
- **SIEM reports** showing block statistics
- **Trend analysis graphs/charts**
- **Threat intelligence reports** (if used)
- **SQL query results** from SIEM

### Sheet 7: False Positive Management
- **FP investigation notes**
- **Whitelist configuration changes**
- **Vendor support tickets** (for recategorization requests)
- **Before/after testing** (URL now accessible after FP resolution)

### Sheet 8: Reporting Schedule
- **Sample reports** (one from each type)
- **Distribution list** confirmation
- **Report generation scripts** or BI report definitions
- **Recipient feedback** (email or meeting notes)

## Evidence Quality Standards

**All evidence must meet these criteria:**

✅ **Current** - Collected within last 90 days (unless historical trend data)
✅ **Complete** - Shows all relevant information, not cut off or partial
✅ **Clear** - Readable, legible, not blurry
✅ **Contextual** - Includes date/timestamp, system identifier
✅ **Verifiable** - Auditor can independently verify if needed
✅ **Sanitized** - PII/sensitive data removed or masked
✅ **Organized** - Stored in logical folder structure
✅ **Accessible** - Easily retrievable during audit

## Evidence Storage

### Recommended structure

```plaintext
/Evidence/A.8.23/
├── Monitoring/
│   ├── Log_Collection/
│   │   ├── SIEM_Screenshots/
│   │   ├── Config_Exports/
│   │   └── Sample_Logs/
│   ├── Alert_Configuration/
│   │   ├── Alert_Rules/
│   │   ├── Notifications/
│   │   └── Test_Results/
│   ├── Dashboards/
│   │   ├── Screenshots/
│   │   ├── KPI_Definitions/
│   │   └── Review_Notes/
│   ├── Incident_Response/
│   │   ├── Incident_Tickets/
│   │   ├── Runbooks/
│   │   └── PIR_Reports/
│   ├── Analysis/
│   │   ├── Blocked_Events/
│   │   ├── False_Positives/
│   │   └── Trends/
│   └── Reporting/
│       └── Sample_Reports/
└── Assessment_Workbooks/
    └── ISMS-IMP-A.8.23.4_Monitoring_Response_20260115.xlsx
```

---

# Common Pitfalls

## Pitfall #1: Theater Over Substance
**Problem:** Beautiful dashboards that nobody reviews, alerts that fire but nobody responds.
**Solution:** Document ACTUAL review frequency and response times, not aspirational ones. If a dashboard isn't being reviewed, that's a Gap (Sheet 9), not a success.
**Auditor Test:** "Show me meeting notes from last month's dashboard review" or "Pull up an alert from last week and show me the response ticket."

## Pitfall #2: Log Collection Without Purpose
**Problem:** Collecting every possible log ("just in case") without understanding what you'll do with the data.
**Solution:** Start with "What threats do we need to detect?" then work backwards to "What logs do we need?" Document the linkage between log sources and threat detection capabilities.
**Feynman Check:** Can you explain WHY you collect each log type and what you'd do if it stopped flowing?

## Pitfall #3: Alert Fatigue
**Problem:** 500 alerts per day, 95% false positives, nobody pays attention anymore.
**Solution:** Track FP rate (Sheet 7), tune aggressively. Target: <2% FP rate. Critical alerts should be rare and always actionable.
**Best Practice:** Better 10 high-confidence alerts than 100 low-confidence ones.

## Pitfall #4: Incident Response on Paper Only
**Problem:** Beautiful runbooks that nobody has ever used, SLAs that are routinely breached.
**Solution:** Track ACTUAL incident handling (Sheet 5, Section C), not theoretical. Document SLA breaches and root causes. Test runbooks quarterly.
**Auditor Question:** "Show me the last 3 incidents and how they were handled."

## Pitfall #5: False Positive Whack-a-Mole
**Problem:** Resolving FPs one-by-one without addressing root causes. Same FPs recur monthly.
**Solution:** Track recurrence (Sheet 7), do root cause analysis for recurring FPs, implement prevention measures. Chronic FPs should be zero.
**Systems Engineering:** Fix the system, not just the symptom.

## Pitfall #6: Reports Nobody Reads
**Problem:** Generating weekly reports that go directly to everyone's spam folder.
**Solution:** Survey recipients quarterly - is report useful? If "Low" effectiveness, discontinue or redesign. Don't waste effort on unused outputs.
**Auditor Insight:** 3 highly effective reports > 15 reports nobody reads.

## Pitfall #7: Evidence Collection as Afterthought
**Problem:** "The auditor is coming next week, quick gather all the screenshots!"
**Solution:** Evidence collection is ONGOING. As you complete each section, immediately gather evidence. Link evidence immediately in Evidence_Ref fields.
**Time Savings:** 10 minutes per section during assessment vs 8 hours in panic mode before audit.

## Pitfall #8: Gap Analysis Theater
**Problem:** Identifying gaps but no real remediation. Every quarter, same gaps in "Open" status.
**Solution:** Gaps without action are just documented failures. Either remediate, accept the risk formally, or resource-plan credibly. No eternal "In_Progress" gaps.
**Auditor Red Flag:** Chronic "Open" gaps with missed target dates = poor governance.

## Pitfall #9: Monitoring Without Context
**Problem:** "We blocked 50,000 requests last month!" - Is that good? Bad? Increasing? Decreasing?
**Solution:** Always provide context - trends, baselines, comparisons. "50K blocked requests, up 15% from baseline, primarily malware category, no SLA breaches" tells a story.
**Best Practice:** Sheet 6 (Blocked Events Analysis) provides this context.

## Pitfall #10: Approval as Rubber Stamp
**Problem:** Approvers sign off without actually reviewing, defeats the purpose of multi-level approval.
**Solution:** Approvers should have SPECIFIC responsibilities (Sheet 11 guidance). L1=Operational accuracy, L2=Technical completeness, L3=Strategic/risk acceptance. Approvers should comment substantively, not just "Approved."
**Quality Check:** If all three approvers sign off in same day, did they really review independently?

---

# Quality Checklist

## Pre-Submission Checklist

Before submitting for Level 1 approval, verify:

### Sheet 2: Log Collection
- [ ] All critical log sources documented (Blocked_Requests = mandatory)
- [ ] Retention periods verified against requirements (Section B)
- [ ] At least 80% of log sources = "Implemented" status
- [ ] Evidence linked for all "Implemented" sources
- [ ] Summary metrics calculated correctly

### Sheet 3: Alert Configuration
- [ ] At least 10-15 Threat_Detection alerts documented
- [ ] Critical/High severity alerts have defined SLAs <30 minutes
- [ ] All alerts have clear trigger conditions (not vague)
- [ ] Alert categories balanced (not all System_Health)
- [ ] Evidence of alert testing (Last_Triggered dates populated)

### Sheet 4: Monitoring Dashboard
- [ ] At least one SOC operational dashboard (Real-Time update)
- [ ] At least one executive dashboard (Daily or Weekly update)
- [ ] Review_Frequency matches actual practice (not aspirational)
- [ ] KPIs have defined targets and current values
- [ ] Dashboard screenshots collected as evidence

### Sheet 5: Incident Response
- [ ] Incident categories align with alert categories
- [ ] SLAs defined for all severity levels
- [ ] Escalation paths documented
- [ ] Recent incidents tracked with ACTUAL response times
- [ ] Post-Incident Reviews completed for Critical/High incidents

### Sheet 6: Blocked Events Analysis
- [ ] Blocked events by category populated with real data
- [ ] Trends identified (not just raw numbers)
- [ ] False positives flagged for investigation (Sheet 7)
- [ ] Actionable intelligence documented (what you learned)

### Sheet 7: False Positive Management
- [ ] All recent FPs documented systematically
- [ ] Investigation findings recorded for each FP
- [ ] Resolution actions taken (not just "investigating")
- [ ] Recurring/Chronic FPs have root cause analysis
- [ ] Prevention measures implemented for recurring FPs

### Sheet 8: Reporting Schedule
- [ ] Mix of Operational, Compliance, and Executive reports
- [ ] Last_Generated dates consistent with Frequency
- [ ] Sample reports collected as evidence
- [ ] Report effectiveness assessed (not all "Unknown")

### Sheet 9: Gap Analysis
- [ ] All identified gaps documented with specificity
- [ ] Priority aligns with impact
- [ ] Remediation plans are specific and actionable (not "TBD")
- [ ] Owners assigned for all High/Critical gaps
- [ ] Target dates realistic based on priority

### Sheet 10: Evidence Register
- [ ] Evidence collected for ALL "Implemented" items across all sheets
- [ ] Evidence_Type accurately reflects content
- [ ] File_Location accessible and specific
- [ ] All evidence = "Verified" status (or verification in progress)
- [ ] Evidence current (within 90 days)

### Sheet 11: Approval Sign-Off
- [ ] Assessment completion date set
- [ ] Next review date calculated (Assessment Date + 90 days)
- [ ] Overall Assessment Status = "Under_Review"
- [ ] All metadata fields completed

## Auditor-Readiness Checklist

For final audit readiness (after all approvals), verify:

- [ ] **Traceability:** Can trace from any alert to corresponding log source to evidence
- [ ] **Completeness:** No critical gaps left unaddressed without risk acceptance
- [ ] **Currency:** All evidence within 90 days (unless historical trend)
- [ ] **Consistency:** KPIs in Sheet 4 match metrics in Sheet 8 reports
- [ ] **Realism:** Documented practices match actual practices (no aspirational claims)
- [ ] **Evidence Quality:** All screenshots clear, complete, contextual
- [ ] **Gap Remediation:** All Critical gaps have target dates within 30 days
- [ ] **Approval Chain:** Three-level approval completed with substantive comments

---

# Review & Approval

## Internal Review (Before Submission)

### Recommended Reviewers

1. **Peer Review** (SOC Analyst or Security Engineer)

   - Review data accuracy
   - Verify operational details
   - Check for completeness
   - Time: 1-2 hours

2. **Self-Review Using Checklist**

   - Run through Section 7 quality checklist
   - Fix any gaps or missing data
   - Verify evidence links work
   - Time: 30-60 minutes

## Approval Process

**Timeline:**

 | Level | Role | Expected Duration | Focus | 
 | ------- | ------ | ------------------- | ------- | 
 | Level 1 | SOC Manager | 2-3 days | Operational accuracy, log collection, alerts | 
 | Level 2 | Security Engineering Lead | 2-3 days | Technical architecture, monitoring depth | 
 | Level 3 | CISO | 3-5 days | Strategic alignment, gap acceptance, risk | 

**Total Approval Time:** 1-2 weeks (assuming no major revisions)

## Handling Rejections or Conditional Approvals

**If Conditionally Approved:**
1. Review approver comments carefully
2. Make requested corrections/additions
3. Document changes made
4. Resubmit with change summary
5. Typical turnaround: 24-48 hours for minor corrections

**If Rejected:**
1. Schedule meeting with rejecting approver to understand issues
2. Assess scope of rework needed
3. Develop revision plan
4. Communicate revised timeline to stakeholders
5. Resubmit when issues resolved (may take 1-2 weeks)

## Post-Approval Actions

Once all three levels approve:

1. **Update Assessment Status** (Sheet 11)

   - Set Overall Assessment Status = "Approved"
   - Set Audit Readiness Confirmation = "Yes" (if criteria met)

2. **Finalize Evidence**

   - Ensure all evidence is verified
   - Upload to final evidence repository
   - Test evidence accessibility

3. **Prepare for Dashboard Integration**

   - Run file normalization script if needed
   - Verify assessment data feeds correctly into Dashboard (A.8.23.5)

4. **Schedule Next Review**

   - Set calendar reminder for Next Review Date
   - Assign responsible party for quarterly update

5. **Celebrate! 🎉**

   - You've documented a mature monitoring and response program
   - Assessment is audit-ready
   - You've contributed to genuine security improvement

---

# Final Notes

## Assessment Philosophy

**Evidence Over Theater:**  
This assessment is about documenting ACTUAL capabilities, not aspirational ones. If you can't demonstrate it with evidence, it doesn't count.

**Feynman Test:**  
If you can't explain to an outsider WHY you monitor something and HOW you'd respond, you're fooling yourself. This assessment forces that clarity.

**Systems Engineering:**  
Monitoring without response is theater. Alerts without resolution tracking is noise. Incidents without PIRs is wasted experience. This assessment ensures the SYSTEM works, not just individual components.

## What Success Looks Like

**For SOC:**

- Log sources comprehensive and ingestion verified
- Alerts tuned (<2% FP rate), SLAs defined and tracked
- Dashboards reviewed regularly with documented actions
- Incidents handled systematically with PIRs

**For Security Engineering:**

- Monitoring architecture documented and justified
- Integration between systems verified
- KPIs defined and tracked
- Technical gaps identified with remediation plans

**For CISO:**

- Visibility into monitoring effectiveness
- Risk-based gap prioritization
- Audit-ready documentation
- Confidence in operational capability

**For Auditor:**

- Clear traceability: Policy → Implementation → Monitoring → Response
- Objective evidence for all claims
- Gaps documented with credible remediation
- Mature operational practices

---

# END OF PART I

**Next Section:** Part II - Technical Specification (Excel Workbook Structure, Sheet-by-Sheet Specifications, Formula Definitions)

---

**Remember:** *"Theater says 'we monitor.' Engineering says 'we detected 1,247 threats last month, blocked 98.7%, resolved 15 incidents with 92% SLA compliance, identified 3 chronic FPs and implemented prevention, average MTTD 3 minutes, MTTR 18 minutes.' Evidence ÷ Theater = Audit Score."* ✅

---


---

# PART II: TECHNICAL SPECIFICATION

# Excel Workbook Layout Specification

---

# Document Overview

 | Attribute | Value | 
|-----------|## Document Overview

**Document ID:** ISMS-IMP-A.8.23.4  
**Assessment Area:** Monitoring, Logging & Incident Response  
**Related Policy:** ISMS-POL-A.8.23-S2.3 (Logging & Monitoring), S5.C (Incident Response)  
**Purpose:** Assess operational monitoring, alerting, and incident response for web filtering  
**Target Audience:** SOC Analysts, Security Engineers, IT Operations, Auditors  

---

# Workbook Structure Overview

 | Sheet # | Sheet Name | Purpose | Row Estimate | 
 | --------- | ------------ | --------- | -------------- | 
 | 1 | Instructions_Legend | Usage guide, color codes, dropdowns | ~50 | 
 | 2 | Log_Collection | What logs collected, where, retention | ~60 | 
 | 3 | Alert_Configuration | Alert rules, thresholds, recipients | ~60 | 
 | 4 | Monitoring_Dashboard | Metrics tracked, dashboards, review cycles | ~50 | 
 | 5 | Incident_Response | Incident handling process, SLAs | ~60 | 
 | 6 | Blocked_Events_Analysis | Analysis of blocked attempts, trends | ~50 | 
 | 7 | False_Positive_Management | FP tracking, tuning, resolution | ~50 | 
 | 8 | Reporting_Schedule | Regular reports, recipients, frequency | ~40 | 
 | 9 | Gap_Analysis | Monitoring/response gaps identified | ~50 | 
 | 10 | Evidence_Register | Evidence catalog (100 rows) | ~110 | 
 | 11 | Approval_Sign_Off | 3-level approval workflow | ~30 | 

**Total Sheets:** 11  
**Estimated Checklist Items:** 70-90

---

# Sheet 1: Instructions_Legend

## Header Section
- **Title:** "ISMS-IMP-A.8.23.4 – Monitoring & Response Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.23: Web Filtering"
- **Styling:** Dark blue header (#003366), white text, 40px height

## Document Information Block
```plaintext
Document ID:           ISMS-IMP-A.8.23.4
Assessment Area:       Monitoring, Logging & Incident Response
Related Policy:        ISMS-POL-A.8.23-S2.3, S5.C
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

## Status Dropdown Values
 | Value | Color | Meaning | 
 | ------- | ------- | --------- | 
 | Implemented | Green (#C6EFCE) | Fully operational and documented | 
 | Partial | Yellow (#FFEB9C) | Partially implemented, gaps exist | 
 | Planned | Blue (#BDD7EE) | Scheduled, not yet implemented | 
 | Not Implemented | Red (#FFC7CE) | Not in place | 
 | N/A | Gray (#D9D9D9) | Not applicable to environment | 

## Priority Values (for Gaps/Actions)
 | Value | Meaning | 
 | ------- | --------- | 
 | Critical | Must address within 30 days | 
 | High | Address within 90 days | 
 | Medium | Address within 180 days | 
 | Low | Address within 12 months | 

## Instructions Summary
1. Complete each sheet for your web filtering monitoring environment
2. Use dropdown menus for standardized entries
3. Fill yellow-highlighted cells with organization-specific data
4. Link evidence for each assessment item
5. Identify gaps in Sheet 9
6. Obtain approvals in Sheet 11

---

# Sheet 2: Log_Collection

## Purpose
Document what web filtering logs are collected, storage locations, and retention.

## Section A: Log Source Inventory (Rows 6-35, 30 log sources)

 | Column | Header | Width | Validation | 
 | -------- | -------- | ------- | ------------ | 
 | A | Log_Source_ID | 15 | Auto: LOG-001 to LOG-030 | 
 | B | Log_Source_Name | 25 | Free text | 
 | C | Log_Type | 20 | Dropdown: Blocked_Requests, Allowed_Requests, Bypass_Attempts, Policy_Violations, Authentication, Configuration_Changes, System_Events | 
 | D | Source_System | 25 | Free text (e.g., "Web Proxy", "DNS Filter", "Firewall") | 
 | E | Collection_Method | 20 | Dropdown: Syslog, API, Agent, File_Transfer, Direct_Query, SNMP | 
 | F | Destination | 25 | Dropdown: SIEM, Log_Server, Cloud_SIEM, Local_Storage, Archive | 
 | G | Format | 15 | Dropdown: CEF, JSON, Syslog, CSV, Proprietary, XML | 
 | H | Retention_Days | 15 | Number (days) | 
 | I | Retention_Compliant | 15 | Dropdown: Yes, No, Partial | 
 | J | Volume_Daily | 15 | Free text (e.g., "50 GB", "10M events") | 
 | K | Status | 15 | Status dropdown | 
 | L | Evidence_Ref | 20 | Free text (link to Evidence_Register) | 
 | M | Notes | 30 | Free text | 

## Section B: Retention Requirements (Rows 40-50)

 | Column | Header | Purpose | 
 | -------- | -------- | --------- | 
 | A | Requirement_ID | Auto: RET-001 to RET-010 | 
 | B | Requirement_Source | Regulatory, Policy, Contractual, Best_Practice | 
 | C | Log_Type | Which logs this applies to | 
 | D | Min_Retention_Days | Minimum required retention | 
 | E | Current_Retention_Days | Actual retention configured | 
 | F | Compliant | Yes/No/Partial | 
 | G | Notes | Gap explanation if non-compliant | 

## Summary Metrics (Row 55-60)
- Total log sources configured: =COUNTA(B6:B35)
- Log sources collecting blocked requests: =COUNTIF(C6:C35,"Blocked_Requests")
- Sources meeting retention requirements: =COUNTIF(I6:I35,"Yes")
- Retention compliance rate: =COUNTIF(I6:I35,"Yes")/COUNTA(I6:I35)

---

# Sheet 3: Alert_Configuration

## Purpose
Document alerting rules, thresholds, escalation, and notification recipients.

## Section A: Alert Rules Inventory (Rows 6-45, 40 alert rules)

 | Column | Header | Width | Validation | 
 | -------- | -------- | ------- | ------------ | 
 | A | Alert_ID | 12 | Auto: ALR-001 to ALR-040 | 
 | B | Alert_Name | 30 | Free text | 
 | C | Alert_Category | 20 | Dropdown: Threat_Detection, Policy_Violation, System_Health, Threshold_Breach, Anomaly, Compliance | 
 | D | Trigger_Condition | 35 | Free text (describe what triggers alert) | 
 | E | Threshold_Value | 15 | Free text (e.g., ">100/hour", "any occurrence") | 
 | F | Severity | 12 | Dropdown: Critical, High, Medium, Low, Informational | 
 | G | Notification_Method | 20 | Dropdown: Email, SMS, SIEM_Alert, Ticket, Dashboard, Webhook, PagerDuty | 
 | H | Recipients | 25 | Free text (roles/groups, not names) | 
 | I | Response_SLA_Minutes | 18 | Number | 
 | J | Escalation_Path | 25 | Free text | 
 | K | Auto_Response | 15 | Dropdown: Yes, No, Partial | 
 | L | Status | 12 | Status dropdown | 
 | M | Last_Triggered | 15 | Date or "Never" | 
 | N | Evidence_Ref | 15 | Link to Evidence_Register | 

## Section B: Alert Categories Summary (Rows 50-58)

 | Category | Count | Active | Tested | 
 | ---------- | ------- | -------- | -------- | 
 | Threat_Detection | =COUNTIF(...) | formula | Yes/No | 
 | Policy_Violation | =COUNTIF(...) | formula | Yes/No | 
 | System_Health | =COUNTIF(...) | formula | Yes/No | 
 | Threshold_Breach | =COUNTIF(...) | formula | Yes/No | 
 | Anomaly | =COUNTIF(...) | formula | Yes/No | 

## Summary Metrics (Row 62-68)
- Total alert rules configured: =COUNTA(B6:B45)
- Critical/High severity alerts: =COUNTIFS(F6:F45,"Critical")+COUNTIFS(F6:F45,"High")
- Alerts with auto-response: =COUNTIF(K6:K45,"Yes")
- Alert coverage score: percentage calculation

---

# Sheet 4: Monitoring_Dashboard

## Purpose
Document monitoring dashboards, metrics tracked, and review frequency.

## Section A: Dashboard Inventory (Rows 6-25, 20 dashboards)

 | Column | Header | Width | Validation | 
 | -------- | -------- | ------- | ------------ | 
 | A | Dashboard_ID | 12 | Auto: DSH-001 to DSH-020 | 
 | B | Dashboard_Name | 30 | Free text | 
 | C | Platform | 20 | Dropdown: SIEM, Filtering_Console, Custom, PowerBI, Grafana, Splunk, Cloud_Native, Other | 
 | D | Primary_Audience | 20 | Dropdown: SOC, Management, IT_Ops, Compliance, CISO, All | 
 | E | Update_Frequency | 18 | Dropdown: Real-Time, Hourly, Daily, Weekly | 
 | F | Review_Frequency | 18 | Dropdown: Continuous, Daily, Weekly, Monthly | 
 | G | Key_Metrics | 40 | Free text (list main KPIs shown) | 
 | H | Alerting_Integrated | 15 | Yes/No | 
 | I | Status | 12 | Status dropdown | 
 | J | Evidence_Ref | 15 | Screenshot reference | 

## Section B: Key Performance Indicators (Rows 30-50, 20 KPIs)

 | Column | Header | Purpose | 
 | -------- | -------- | --------- | 
 | A | KPI_ID | Auto: KPI-001 to KPI-020 | 
 | B | KPI_Name | Metric name | 
 | C | KPI_Category | Dropdown: Volume, Security, Performance, Compliance, Operational | 
 | D | Measurement_Unit | Events, Percentage, Time, Count, Bytes | 
 | E | Target_Value | Expected value | 
 | F | Current_Value | Actual value | 
 | G | Met_Target | Yes/No/At_Risk | 
 | H | Trend | Dropdown: Improving, Stable, Degrading | 
 | I | Tracked_On | Dashboard reference | 
 | J | Evidence_Ref | Link | 

## Summary Metrics (Row 55-60)
- Total KPIs tracked: =COUNTA(B30:B50)
- KPIs meeting target: =COUNTIF(G30:G50,"Yes")
- KPIs at risk: =COUNTIF(G30:G50,"At_Risk")
- Real-time monitoring KPIs: formula based on Update_Frequency

---

# Sheet 5: Incident_Response

## Purpose
Document incident handling procedures, SLAs, and recent incidents.

## Section A: Incident Categories (Rows 6-25, 20 categories)

 | Column | Header | Width | Validation | 
 | -------- | -------- | ------- | ------------ | 
 | A | Category_ID | 12 | Auto: INC-CAT-001 to INC-CAT-020 | 
 | B | Category_Name | 30 | Free text | 
 | C | Severity_Criteria | 35 | How severity determined | 
 | D | Response_SLA_Critical | 12 | Minutes | 
 | E | Response_SLA_High | 12 | Minutes | 
 | F | Response_SLA_Medium | 12 | Minutes | 
 | G | Response_SLA_Low | 12 | Minutes | 
 | H | Escalation_Path | 30 | Who escalates to whom | 
 | I | Runbook_Reference | 25 | Link to procedure | 
 | J | Evidence_Ref | 15 | Link | 

## Section B: Recent Incidents (Rows 30-55, 25 incidents)

 | Column | Header | Purpose | 
 | -------- | -------- | --------- | 
 | A | Incident_ID | Auto: INC-001 to INC-025 | 
 | B | Incident_Date | Date | 
 | C | Category | Dropdown from Section A | 
 | D | Severity | Critical, High, Medium, Low | 
 | E | Detection_Method | Alert, User_Report, SOC_Review, Audit | 
 | F | Time_to_Detect_Minutes | Number | 
 | G | Time_to_Respond_Minutes | Number | 
 | H | Met_SLA | Yes/No | 
 | I | Containment_Action | Free text | 
 | J | Resolution_Status | Open, Resolved, Escalated | 
 | K | PIR_Completed | Yes/No/N/A | 
 | L | Evidence_Ref | Link | 

## Summary Metrics (Row 60-68)
- Total incidents: =COUNTA(A30:A55)
- Critical/High incidents: =COUNTIFS(D30:D55,"Critical")+COUNTIFS(D30:D55,"High")
- Average MTTD: =AVERAGE(F30:F55)
- Average MTTR: =AVERAGE(G30:G55)
- SLA compliance rate: =COUNTIF(H30:H55,"Yes")/COUNTA(H30:H55)
- PIR completion rate: formula for High/Critical with PIR

---

# Sheet 6: Blocked_Events_Analysis

## Purpose
Analyze blocked web filtering events to identify threats and trends.

## Section A: Blocked Events by Category (Rows 6-25, 20 categories)

 | Column | Header | Width | 
 | -------- | -------- | ------- | 
 | A | Category_ID | 12 | 
 | B | Category_Name | 30 | 
 | C | Events_Last_30_Days | Count | 
 | D | Events_Last_90_Days | Count | 
 | E | Trend | Increasing/Stable/Decreasing | 
 | F | Top_Source | Most common source (user group, network, etc.) | 
 | G | Risk_Level | High/Medium/Low | 
 | H | Action_Required | Yes/No | 
 | I | Notes | Analysis notes | 

## Section B: Top Blocked Threats (Rows 30-45)

 | Rank | Threat_Type | Count_30_Days | Percentage | Mitigation_Status | 
 | ------ | ------------- | --------------- | ------------ | ------------------- | 
 | 1 | [input] | [input] | formula | [dropdown] | 
 | ... | ... | ... | ... | ... | 

## Section C: Trend Analysis (Rows 50-60)

 | Month | Total_Blocked | Malware | Phishing | Policy_Violation | Other | 
 | ------- | --------------- | --------- | ---------- | ------------------ | ------- | 
 | [Month-6] | [input] | [input] | [input] | [input] | [input] | 
 | ... | ... | ... | ... | ... | ... | 
 | [Current] | [input] | [input] | [input] | [input] | [input] | 

---

# Sheet 7: False_Positive_Management

## Purpose
Track false positives, tuning actions, and resolution effectiveness.

## Section A: False Positive Log (Rows 6-55, 50 entries)

 | Column | Header | Width | Validation | 
 | -------- | -------- | ------- | ------------ | 
 | A | FP_ID | 12 | Auto: FP-001 to FP-050 | 
 | B | Date_Reported | 12 | Date | 
 | C | Reported_By | 20 | Free text (role, not name) | 
 | D | Blocked_URL_Category | 25 | Free text | 
 | E | Business_Justification | 35 | Why access needed | 
 | F | Investigation_Result | 20 | Dropdown: Confirmed_FP, True_Positive, Inconclusive | 
 | G | Resolution_Action | 25 | Dropdown: Whitelist, Policy_Tuning, Category_Update, No_Action, Escalated | 
 | H | Resolution_Date | 12 | Date | 
 | I | Resolution_Time_Hours | 18 | Number (calculated) | 
 | J | Recurrence | 15 | Dropdown: First_Time, Recurring, Chronic | 
 | K | Status | 12 | Dropdown: Open, Resolved, Escalated | 
 | L | Evidence_Ref | 15 | Link | 

## Section B: False Positive Metrics (Rows 60-70)

 | Metric | Value | Target | Status | 
 | -------- | ------- | -------- | -------- | 
 | Total FPs reported (last 90 days) | =COUNTIF(...) | <50 | formula | 
 | Average resolution time (hours) | =AVERAGE(...) | <24 | formula | 
 | FP rate (FPs / total blocks) | calculation | <1% | formula | 
 | Recurring FP percentage | calculation | <10% | formula | 
 | Open FPs | =COUNTIF(...) | <10 | formula | 

---

# Sheet 8: Reporting_Schedule

## Purpose
Document regular reports generated for web filtering operations.

## Section A: Report Inventory (Rows 6-25, 20 reports)

 | Column | Header | Width | Validation | 
 | -------- | -------- | ------- | ------------ | 
 | A | Report_ID | 12 | Auto: RPT-001 to RPT-020 | 
 | B | Report_Name | 30 | Free text | 
 | C | Report_Type | 20 | Dropdown: Operational, Compliance, Executive, Incident, Trend, Audit | 
 | D | Frequency | 15 | Dropdown: Daily, Weekly, Monthly, Quarterly, Annual, Ad-hoc | 
 | E | Generation_Method | 18 | Dropdown: Automated, Manual, Semi-Automated | 
 | F | Distribution_List | 25 | Roles (not names) | 
 | G | Delivery_Method | 18 | Dropdown: Email, Portal, Dashboard, File_Share, Meeting | 
 | H | Content_Summary | 40 | Brief description of report contents | 
 | I | Last_Generated | 12 | Date | 
 | J | Status | 12 | Status dropdown | 
 | K | Evidence_Ref | 15 | Sample report reference | 

## Section B: Reporting Coverage Assessment (Rows 30-40)

 | Stakeholder | Required_Reports | Reports_Received | Coverage | 
 | ------------- | ------------------ | ------------------ | ---------- | 
 | CISO | [input] | [input] | formula | 
 | IT Management | [input] | [input] | formula | 
 | Compliance | [input] | [input] | formula | 
 | SOC | [input] | [input] | formula | 
 | Auditors | [input] | [input] | formula | 

---

# Sheet 9: Gap_Analysis

## Purpose
Identify and prioritize monitoring and response gaps.

## Gap Register (Rows 6-35, 30 gaps)

 | Column | Header | Width | Validation | 
 | -------- | -------- | ------- | ------------ | 
 | A | Gap_ID | 12 | Auto: GAP4-001 to GAP4-030 | 
 | B | Gap_Category | 20 | Dropdown: Logging, Alerting, Monitoring, Incident_Response, Reporting, Integration, Retention | 
 | C | Gap_Description | 40 | Free text | 
 | D | Current_State | 30 | What exists today | 
 | E | Target_State | 30 | What should exist | 
 | F | Risk_Impact | 15 | Dropdown: Critical, High, Medium, Low | 
 | G | Affected_Systems | 25 | Which systems impacted | 
 | H | Remediation_Action | 35 | What needs to be done | 
 | I | Owner | 20 | Role responsible | 
 | J | Target_Date | 12 | Date | 
 | K | Status | 15 | Dropdown: Open, In_Progress, Resolved, Accepted | 
 | L | Priority | 12 | Priority dropdown | 
 | M | Evidence_Ref | 15 | Link | 

## Summary Metrics (Row 40-45)
- Total gaps identified: =COUNTA(B6:B35)
- Critical/High gaps: =COUNTIF(F6:F35,"Critical")+COUNTIF(F6:F35,"High")
- Open gaps: =COUNTIF(K6:K35,"Open")
- Gaps past due: formula based on Target_Date

---

# Sheet 10: Evidence_Register

## Standard 100-row evidence catalog

 | Column | Header | Width | 
 | -------- | -------- | ------- | 
 | A | Evidence_ID | 15 | 
 | B | Evidence_Title | 35 | 
 | C | Evidence_Type | 20 | 
 | D | Related_Sheet | 20 | 
 | E | Related_Item_ID | 15 | 
 | F | Date_Collected | 12 | 
 | G | Collected_By | 20 | 
 | H | Storage_Location | 35 | 
 | I | Retention_Until | 12 | 
 | J | Verification_Status | 18 | 
 | K | Notes | 30 | 

**Evidence_ID Format:** EV4-001 to EV4-100  
**Evidence_Type Dropdown:** Screenshot, Configuration_Export, Log_Sample, Report, Procedure_Document, Email_Confirmation, Audit_Report, Test_Results, Policy_Document, Other

---

# Sheet 11: Approval_Sign_Off

## 3-Level Approval Workflow

 | Role | Name | Date | Signature | Comments | 
 | ------ | ------ | ------ | ----------- | ---------- | 
 | Completed By | [yellow] | [yellow] | [yellow] | [yellow] | 
 | Reviewed By | [yellow] | [yellow] | [yellow] | [yellow] | 
 | Approved By (CISO) | [yellow] | [yellow] | [yellow] | [yellow] | 

## Assessment Summary (auto-populated)
- Assessment Date: =Instructions_Legend!B7
- Total Log Sources: =Log_Collection summary
- Total Alert Rules: =Alert_Configuration summary
- Open Gaps: =Gap_Analysis summary
- Evidence Items: =COUNTA(Evidence_Register!A:A)-1

## Certification Statement
> "This assessment accurately reflects the current state of web filtering
> monitoring, logging, and incident response capabilities. All findings
> have been verified and gaps have been documented for remediation."

---

# Validation Dropdowns Summary

 | Dropdown Name | Values | 
 | --------------- | -------- | 
 | Status | Implemented, Partial, Planned, Not_Implemented, N/A | 
 | Priority | Critical, High, Medium, Low | 
 | Severity | Critical, High, Medium, Low, Informational | 
 | Yes_No | Yes, No | 
 | Yes_No_Partial | Yes, No, Partial | 
 | Log_Type | Blocked_Requests, Allowed_Requests, Bypass_Attempts, Policy_Violations, Authentication, Configuration_Changes, System_Events | 
 | Collection_Method | Syslog, API, Agent, File_Transfer, Direct_Query, SNMP | 
 | Destination | SIEM, Log_Server, Cloud_SIEM, Local_Storage, Archive | 
 | Alert_Category | Threat_Detection, Policy_Violation, System_Health, Threshold_Breach, Anomaly, Compliance | 
 | Notification_Method | Email, SMS, SIEM_Alert, Ticket, Dashboard, Webhook, PagerDuty | 
 | Report_Type | Operational, Compliance, Executive, Incident, Trend, Audit | 
 | Frequency | Daily, Weekly, Monthly, Quarterly, Annual, Ad-hoc | 
 | Gap_Category | Logging, Alerting, Monitoring, Incident_Response, Reporting, Integration, Retention | 
 | Gap_Status | Open, In_Progress, Resolved, Accepted | 
 | FP_Result | Confirmed_FP, True_Positive, Inconclusive | 
 | FP_Resolution | Whitelist, Policy_Tuning, Category_Update, No_Action, Escalated | 
 | Trend | Improving, Stable, Degrading, New, Increasing, Decreasing | 

---

**END OF SPECIFICATION**

*"We don't just monitor - we measure, analyze, and improve."*  
*— Not Cargo Cult ISMS*
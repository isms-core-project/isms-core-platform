**ISMS-IMP-A.8.15.4-UG - Log Analysis & Review Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.4-UG |
| **Version** | 1.0 |
| **Assessment Area** | Log Analysis, Review Process, Threat Detection & SOC Effectiveness |
| **Related Policy** | ISMS-POL-A.8.15, Section 2.4 (Log Review & Analysis Requirements), Section 2.1 (Event Logging Requirements) |
| **Purpose** | Assess log review process effectiveness, SIEM use case maturity, alert management, SOC performance metrics, threat detection coverage |
| **Target Audience** | Security Operations Center (SOC), Threat Detection Team, Security Engineers, InfoSec Manager, CISO, Incident Response Team, Auditors, Workbook Developers |
| **Assessment Type** | Operational Effectiveness & Process Maturity |
| **Review Cycle** | Quarterly (full assessment), Monthly (SOC metrics review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.15.4-TG.

---

**Audience:** SOC Team, Threat Detection, Security Engineers, InfoSec Manager

---

# Assessment Overview

## What This Assessment Evaluates

This assessment evaluates LOG ANALYSIS AND REVIEW EFFECTIVENESS - whether logs are actually being analyzed, alerts are actionable, threats are detected, and the SOC is performing effectively.

**Key Questions Answered:**

- Are logs being reviewed as required by policy Section 2.4?
- What SIEM use cases are implemented? (Maturity level per use case)
- How effective is alert management? (False positive rate, tuning effectiveness)
- How well is the SOC performing? (MTTD, MTTR, investigation quality)
- What level of automation exists? (Manual vs. automated analysis)
- What threat detection coverage exists? (MITRE ATT&CK mapping)
- How well integrated is log analysis with incident response?

**What This Assessment Is NOT:**

- NOT about which systems are logging (that's IMP-A.8.15.1)
- NOT about log collection infrastructure (that's IMP-A.8.15.2)
- NOT about log protection or retention (that's IMP-A.8.15.3)

This is purely about **OPERATIONAL EFFECTIVENESS** - are we actually getting security value from the logs we're collecting?

## Why This Matters

This assessment verifies [Organization]'s compliance with:

- **ISO/IEC 27001:2022 Control A.8.15**: Logs must be reviewed - collection without analysis provides no security benefit
- **ISMS-POL-A.8.15, Section 2.4 (Log Review)**: Regular review required, frequency defined per log category
- **ISMS-POL-A.8.15, Section 2.1 (Event Logging)**: Seven event categories must be logged AND reviewed
- **PCI DSS Requirement 10.6** (if applicable): Daily review of security events required
- **DORA/NIS2** (if applicable): ICT monitoring and detection capabilities required

**Security Impact**:

- **Unreviewed logs = wasted investment** - collecting logs without analysis provides no security value
- **Slow detection = larger breaches** - poor SOC performance means attackers have more time
- **Alert fatigue = missed threats** - high false positive rates cause analysts to ignore alerts
- **Coverage gaps = blind spots** - missing use cases mean entire attack classes go undetected

**Compliance Impact**:

- **Major non-conformity** if logs not reviewed per policy requirements (ISO 27001 audit finding)
- **PCI DSS failure** if daily review not performed and documented
- **Ineffective control** = wasted resources, poor security posture

**Audit Evidence**: This assessment workbook provides **objective evidence** that logs are being analyzed and reviewed effectively.

## Assessment Outputs

**Primary Deliverable**: Excel workbook with 11 sheets containing:

1. **Review Process Assessment**: Who reviews, how often, procedures documented, evidence of reviews
2. **SIEM Use Case Maturity**: Implemented use cases, maturity level per MITRE ATT&CK tactics
3. **Alert Management**: Alert volume, false positive rate, tuning effectiveness, escalation process
4. **SOC Performance Metrics**: MTTD, MTTR, investigation quality, case closure rates
5. **Automation Assessment**: Manual vs. automated analysis, SOAR integration, playbook maturity
6. **Threat Detection Coverage**: MITRE ATT&CK coverage, detection gaps, threat hunting capabilities
7. **Investigation Procedures**: IR integration, forensics capabilities, evidence collection procedures
8. **Gap Analysis**: Process gaps, capability gaps, remediation priorities
9. **Compliance Scoring**: % compliance with policy Section 2.4 requirements

**Typical Assessment Results**:

- **Review Process Compliance**: 70-95% (some log categories reviewed less frequently than required)
- **Use Case Maturity**: 40-70% (basic use cases implemented, advanced use cases lacking)
- **Alert Management**: 60-85% (moderate false positive rates, tuning ongoing)
- **SOC Performance**: MTTD 4-48 hours, MTTR 1-7 days (varies widely by organization maturity)
- **Automation Level**: 20-60% (some automation, much manual work remains)
- **Gaps Identified**: 15-30 findings (process gaps, capability gaps, training needs)

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
IMP-A.8.15.3 (Protection & Retention)
    |
    v
    Verifies logs PROTECTED and RETAINED
    |
    v
IMP-A.8.15.4 (Analysis & Review) <-- YOU ARE HERE
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

**Recommended Order**: Complete IMP-A.8.15.1, .2, and .3 FIRST (ensure logs exist, are collected, and are protected), then assess whether they're being analyzed effectively.

---

# Prerequisites

## Required Completed Work

**RECOMMENDED**: Complete **ISMS-IMP-A.8.15.1, A.8.15.2, and A.8.15.3** first.

**Why?** This assessment evaluates analysis of logs that exist, are collected, and are accessible. Need to verify earlier stages work before assessing analysis effectiveness.

**If earlier assessments not complete:**

- You can still proceed, but may identify gaps that are actually collection/access issues, not analysis issues

## Required Access

**SIEM Platform Access**:

- Access to SIEM use case/correlation rule configuration
- Access to alert history (last 90 days minimum)
- Access to SOC metrics dashboards (MTTD, MTTR, alert volume)
- Access to investigation case management system

**SOC Operational Data**:

- Alert logs (volume, categories, dispositions)
- Investigation case records (open, closed, escalated)
- SOC shift logs or handoff reports
- Incident response records (escalations from log analysis)

**Documentation Access**:

- SOC procedures and runbooks
- SIEM use case documentation
- Alert tuning records (when alerts tuned, why)
- Threat detection strategy documentation (if exists)

## Required Personnel

**Who Should Complete This Assessment**:

**Primary Responsibility**:

- **SOC Manager/Lead**: Understands review processes, SOC performance, operational challenges
- **Threat Detection Lead**: Understands use case development, detection engineering

**Supporting Input Required From**:

- **SOC Analysts**: Front-line experience with alerts, tuning needs, false positives
- **Security Engineers**: SIEM configuration, automation development
- **Incident Response**: IR integration, escalation effectiveness
- **InfoSec Manager**: Strategic perspective, resource prioritization

**Estimated Time**: 12-18 hours (distributed across multiple personnel over 2-3 weeks)

## Required Tools & Documentation

**Tools**:

- SIEM administration/analytics interface
- Case management system (ServiceNow, Jira, TheHive, etc.)
- Alert tracking/metrics dashboards
- Previous assessment workbooks (IMP-A.8.15.1, .2, .3)

**Documentation**:

- SOC procedures manual
- SIEM use case library
- Alert tuning history
- SOC performance reports (monthly/quarterly metrics)
- Incident response escalation records

---

# Assessment Workflow

## Recommended Completion Sequence

**Phase 1: Review Process Assessment (Sheets 1-2)**

- Sheet 1: Instructions
- Sheet 2: Review Process Assessment (who reviews, how often, procedures)

**Phase 2: Detection Capabilities (Sheets 3-5)**

- Sheet 3: SIEM Use Case Maturity (implemented use cases, coverage)
- Sheet 4: Alert Management (volume, false positives, tuning)
- Sheet 5: SOC Performance Metrics (MTTD, MTTR, quality)

**Phase 3: Advanced Capabilities (Sheets 6-8)**

- Sheet 6: Automation Assessment (SOAR, playbooks, automated response)
- Sheet 7: Threat Detection Coverage (MITRE ATT&CK, threat hunting)
- Sheet 8: Investigation Procedures (IR integration, forensics)

**Phase 4: Review & Approval (Sheets 9-11)**

- Sheet 9: Gap Analysis (process gaps, capability gaps)
- Sheet 10: Evidence Register
- Sheet 11: Approval Sign-Off

**Estimated Timeline**:

- Phase 1: 3-4 hours (review process documentation)
- Phase 2: 5-7 hours (use cases, alerts, SOC metrics - most time-consuming)
- Phase 3: 3-4 hours (automation, advanced capabilities)
- Phase 4: 2-3 hours (gap analysis, evidence, approval)

**Total**: 13-18 hours (spread over 2-3 weeks)

## Iterative Approach

**Week 1**:

- SOC Manager completes review process assessment (Sheet 2)
- Threat Detection Lead documents use cases (Sheet 3)
- SOC Analyst Lead analyzes alert metrics (Sheet 4)

**Week 2**:

- SOC Manager compiles performance metrics (Sheet 5)
- Security Engineer assesses automation (Sheet 6)
- Threat Detection Lead maps ATT&CK coverage (Sheet 7)

**Week 3**:

- Incident Response reviews IR integration (Sheet 8)
- Cross-functional gap analysis workshop (Sheet 9)
- Evidence collection and approval process (Sheets 10-11)

## Data Collection Methods

**Review Process Documentation**:

- SOC procedures review (documented vs. actual practice)
- Review logs/records (evidence reviews actually happening)
- Interview SOC analysts (understand actual practice vs. documented)

**SIEM Use Case Analysis**:

- Export use case/correlation rule list from SIEM
- Categorize by MITRE ATT&CK tactics/techniques
- Assess maturity (basic detection, tuned, well-documented, regularly tested)

**Alert Metrics Analysis**:

- Query SIEM for alert volume (last 90 days)
- Calculate false positive rate (alerts investigated vs. true positives)
- Review tuning history (when alerts tuned, effectiveness)

**SOC Performance Data**:

- Extract metrics from case management system
- Calculate MTTD (Mean Time To Detect - event to alert)
- Calculate MTTR (Mean Time To Respond - alert to containment)
- Review investigation quality (thoroughness, documentation)

---

# Completing Each Sheet

## Sheet 1: Instructions & Legend

**Purpose**: Assessment methodology and scoring guide

**Time**: 15-20 minutes (first-time), 5 minutes (returning users)

## Sheet 2: Review Process Assessment

**Purpose**: Verify logs are being reviewed per policy Section 2.4 requirements

**For Each Log Category**:

- Log Category (from policy Section 2.1: Security Events, Authentication, Admin Actions, Database, Application, Network, System)
- Policy Requirement - Review Frequency (from policy Section 2.4: Daily, Weekly, Monthly)
- Actual Review Frequency (What's actually happening)
- Reviewer Role (Who performs review - SOC Analyst, Security Engineer, etc.)
- Review Procedure Documented (Yes/No)
- Review Evidence Available (Yes/No - are review records kept?)
- Last Review Date (When was last review performed)
- Review Tool/Method (SIEM dashboard, manual log review, automated report)
- Compliance Status - Formula: `=IF(Actual_Frequency >= Policy_Frequency, "Y Compliant", "N Non-Compliant")`

**Evidence of Reviews**:

- Review logs/checklists (documented evidence reviews occurred)
- SIEM dashboard access logs (proof dashboards being viewed)
- Investigation tickets (reviews leading to investigations)
- Shift handoff reports (SOC shift logs mentioning review activities)

**Compliance Calculation**:

- Total Log Categories = 7
- Categories Reviewed Per Policy = COUNT(Compliance = "Y")
- **Review Process Compliance %** = (Compliant / Total) * 100

**Time**: 2-3 hours

## Sheet 3: SIEM Use Case Maturity

**Purpose**: Assess detection capabilities and use case maturity

**For Each Use Case**:

- Use Case ID / Name
- MITRE ATT&CK Tactic (Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Exfiltration, Command & Control, Impact)
- MITRE ATT&CK Technique(s) Detected
- Use Case Description (What threat does this detect?)
- Data Sources Required (Which logs feed this use case?)
- Detection Method (Signature, Anomaly, Behavioral, Correlation, Threat Intel)
- Maturity Level:
  - Level 1: Basic - Rule exists, not tuned, high false positives
  - Level 2: Developing - Rule tuned, documented, moderate effectiveness
  - Level 3: Defined - Well-tuned, low false positives, documented procedures
  - Level 4: Managed - Regularly tested, metrics tracked, continuous improvement
  - Level 5: Optimized - Automated response, threat hunting integration, best-in-class
- False Positive Rate (High >20%, Medium 5-20%, Low <5%)
- True Positive Count (Last 90 days)
- Last Tuned Date
- Last Tested Date
- Documentation Status (None, Basic, Comprehensive)

**Use Case Coverage by ATT&CK Tactic**:
| Tactic | Use Cases | Avg Maturity | Coverage % |
|--------|-----------|--------------|------------|
| Initial Access | COUNT | AVERAGE(Maturity) | Formula |
| Execution | ... | ... | ... |
| ... | ... | ... | ... |

**Overall Maturity Score** = AVERAGE(all use case maturity levels)

**Time**: 4-6 hours (requires detailed use case analysis)

## Sheet 4: Alert Management

**Purpose**: Assess alert effectiveness and tuning

**Alert Volume Metrics** (Last 90 days):

- Total Alerts Generated
- Alerts by Severity (Critical, High, Medium, Low, Informational)
- Alerts Investigated (count)
- True Positives (actual security events)
- False Positives (benign events incorrectly flagged)
- False Negative Estimate (missed detections - from incidents not caught by alerts)

**Alert Disposition**:

- Closed - True Positive (escalated to IR)
- Closed - False Positive (alert tuned/suppressed)
- Closed - Benign (legitimate activity, no tuning needed)
- Open/In Progress
- Escalated to Incident Response

**Alert Performance Metrics**:

- False Positive Rate = False Positives / Total Alerts * 100 (Target: <10%)
- Alert Investigation Rate = Investigated / Total * 100 (Target: 100% for High/Critical)
- True Positive Rate = True Positives / Investigated * 100 (Target: >30%)
- Alert Tuning Effectiveness = (FP_Before - FP_After) / FP_Before * 100

**Top Alert Sources** (by volume):

- Alert Name, Count (Last 90 days), False Positive %, Status (Tuned, Under Review, Accepted)

**Alert Tuning History**:

- Date Tuned, Alert Name, Reason for Tuning, FP Reduction Achieved, Tuned By

**Compliance Assessment**:

- Alert volume manageable (Target: <500 alerts/day/analyst)
- False positive rate acceptable (Target: <10%)
- Critical/High alerts all investigated (Target: 100%)
- Tuning process active (Evidence: tuning in last 90 days)

**Time**: 3-4 hours (data extraction and analysis)

## Sheet 5: SOC Performance Metrics

**Purpose**: Measure SOC operational effectiveness

**Detection Metrics**:

- Mean Time To Detect (MTTD): Event occurrence -> Alert generation
  - Critical Severity: Target <15 minutes
  - High Severity: Target <1 hour
  - Medium Severity: Target <4 hours
- Detection Coverage: % of incidents detected by logs/SIEM vs. external notification

**Response Metrics**:

- Mean Time To Acknowledge (MTTA): Alert generated -> Analyst starts investigation
  - Critical: Target <15 minutes
  - High: Target <1 hour
- Mean Time To Respond (MTTR): Alert -> Containment/remediation
  - Critical: Target <4 hours
  - High: Target <24 hours

**Investigation Quality**:

- % of investigations with complete documentation
- % of investigations with root cause identified
- % of investigations resulting in findings/recommendations
- Average investigation depth score (1-5 scale)

**Case Management**:

- Cases Opened (last 90 days)
- Cases Closed (last 90 days)
- Open Case Backlog (current)
- Average Case Age (days from open to close)
- % Cases Closed Within SLA

**SOC Staffing & Efficiency**:

- FTE Count (Full-Time Equivalent analysts)
- Alerts Per Analyst Per Day (Target: <50)
- Cases Per Analyst Per Week (Target: <20)
- Burnout Indicators (Overtime hours, turnover rate, open position duration)

**Compliance Scoring**:

- MTTD meets targets (% of cases meeting MTTD targets)
- MTTR meets targets (% of cases meeting MTTR targets)
- Investigation quality acceptable (% meeting quality standards)
- **Overall SOC Performance Score** = Weighted average

**Time**: 2-3 hours (metrics extraction from case management system)

## Sheet 6: Automation Assessment

**Purpose**: Assess automation maturity and SOAR effectiveness

**Automation Level by Process**:
| Process | Current State | Target State | Gap |
|---------|---------------|--------------|-----|
| Log Ingestion | Manual/Automated/Partial | Fully Automated | ... |
| Alert Triage | Manual/Semi-Auto/Automated | ... | ... |
| Enrichment | Manual/Semi-Auto/Automated | ... | ... |
| Containment Actions | Manual/Semi-Auto/Automated | ... | ... |
| Ticket Creation | Manual/Semi-Auto/Automated | ... | ... |
| Notification/Escalation | Manual/Semi-Auto/Automated | ... | ... |

**SOAR Integration**:

- SOAR Platform Implemented (Yes/No/Planned)
- Platform Name (if yes)
- Integration Level (Basic, Intermediate, Advanced)
- Playbook Count (automated playbooks)
- Playbooks by Category (Phishing, Malware, Unauthorized Access, Data Exfiltration, etc.)
- Playbook Execution Volume (last 90 days)
- Playbook Success Rate (% successful executions)

**Automated Response Actions**:

- User Account Disable (Automated? Yes/No/Partial)
- IP/Domain Blocking (Automated? Yes/No/Partial)
- Malware Quarantine (Automated? Yes/No/Partial)
- Network Segmentation (Automated? Yes/No/Partial)
- Evidence Collection (Automated? Yes/No/Partial)

**Time Savings from Automation**:

- Estimated Manual Hours Saved Per Month
- ROI Calculation (if automation investment known)

**Automation Maturity Score**:

- % of processes automated
- SOAR integration level
- Playbook coverage
- **Overall Automation Score** = Weighted average

**Time**: 2-3 hours

## Sheet 7: Threat Detection Coverage

**Purpose**: Map detection capabilities to threat landscape

**MITRE ATT&CK Coverage**:

- Total Techniques in ATT&CK (193 as of v14)
- Techniques Detected (count from Sheet 3 use cases)
- Coverage % = (Detected / Total) * 100
- Coverage by Tactic (% coverage per tactic)

**Detection Gaps** (Tactics/Techniques NOT detected):

- Tactic, Technique ID, Technique Name, Severity (if gap exploited), Mitigation Priority

**Threat Hunting Capabilities**:

- Threat Hunting Program Exists (Yes/No/Developing)
- Hunts Per Quarter (count)
- Findings Per Hunt (average)
- Hunts Leading to New Use Cases (count)
- Threat Intel Integration (feeds integrated into SIEM)
- Threat Intel Sources (commercial, open-source, ISAC, internal)

**Detection Engineering Maturity**:

- Detection Engineering Team Exists (Yes/No)
- Use Case Development Process (Ad-hoc, Defined, Managed, Optimized)
- Use Case Testing Process (None, Manual, Automated)
- Purple Team Exercises (Frequency: Never, Annual, Quarterly, Monthly)

**Coverage Score**:

- ATT&CK Coverage %
- Threat Hunting Maturity (0-5 scale)
- Detection Engineering Maturity (0-5 scale)
- **Overall Threat Detection Coverage Score** = Weighted average

**Time**: 2-3 hours (requires ATT&CK mapping)

## Sheet 8: Investigation Procedures

**Purpose**: Assess IR integration and investigation capabilities

**Investigation Process Documentation**:

- Investigation procedures documented (Yes/No)
- Procedures include escalation criteria (Yes/No)
- Procedures include evidence collection (Yes/No)
- Procedures regularly updated (Last update date)

**IR Integration**:

- Escalation criteria defined (Yes/No)
- Escalation path documented (SOC -> IR -> Management -> Legal)
- Escalation SLA defined (timeframe for escalation)
- % of incidents escalated appropriately (retrospective analysis)
- IR team feedback loop (IR provides feedback to SOC on investigation quality)

**Forensics Capabilities**:

- Disk Forensics (Capability: None, Basic, Advanced)
- Memory Forensics (Capability: None, Basic, Advanced)
- Network Forensics (PCAP analysis capability)
- Cloud Forensics (Cloud environment investigation capability)
- Tools Available (EnCase, FTK, Volatility, Wireshark, cloud-native tools, etc.)
- Trained Personnel (# of analysts with forensics training)

**Evidence Collection & Chain of Custody**:

- Evidence collection procedures documented (Yes/No)
- Chain of custody forms used (Yes/No)
- Evidence retention policy defined (Yes/No - how long evidence kept)
- Evidence storage secure (Yes/No - access controlled)

**Investigation Quality Assessment** (Sample recent investigations):

- Timeline completeness (Were all events sequenced?)
- Root cause identified (Yes/No per investigation)
- Impact assessment performed (Yes/No)
- Recommendations provided (Yes/No)
- Documentation quality (1-5 scale)

**Compliance Scoring**:

- Investigation procedures comprehensive (yes/no)
- IR integration effective (% appropriate escalations)
- Forensics capabilities adequate (based on organization needs)
- Evidence handling compliant (yes/no)
- **Overall Investigation Effectiveness Score** = Weighted average

**Time**: 2-3 hours

---

# Evidence Collection

**For Review Process (Sheet 2)**:

- SOC shift logs (proof reviews occurring)
- Review checklists (documented review records)
- Dashboard access logs (SIEM usage evidence)
- Investigation tickets originated from log review

**For Use Cases (Sheet 3)**:

- SIEM use case export (correlation rules, alerts)
- Use case documentation (descriptions, procedures)
- Testing records (when use cases last tested)
- Tuning history (when rules tuned, why)

**For Alert Management (Sheet 4)**:

- Alert volume reports (last 90 days)
- False positive analysis (FP rate calculations)
- Tuning records (evidence of tuning activities)
- Alert disposition reports (TP vs. FP breakdown)

**For SOC Metrics (Sheet 5)**:

- Case management reports (MTTD, MTTR, case age)
- Investigation quality assessments (sample investigations)
- SOC dashboard screenshots (metrics visualization)
- Monthly/quarterly SOC performance reports

**For Automation (Sheet 6)**:

- SOAR platform screenshots (playbook library)
- Automation execution logs (playbook run history)
- Time savings calculations (before/after automation)

**For Threat Detection (Sheet 7)**:

- MITRE ATT&CK coverage mapping
- Threat hunting reports (findings from hunts)
- Detection gap analysis
- Threat intel feed configurations

**For Investigations (Sheet 8)**:

- Investigation procedure documents
- Sample investigation reports (quality examples)
- IR escalation records
- Forensics tool inventory

---

# Common Pitfalls

## Pitfall: "We have SIEM, so we're reviewing logs"

**Problem**: SIEM deployed != logs actually reviewed

**Reality**: Many organizations have SIEM with hundreds of use cases but limited SOC coverage, resulting in alerts going uninvestigated.

**How to Avoid**:

- Track actual review activity (Sheet 2 - evidence of reviews)
- Measure alert investigation rate (Sheet 4 - % alerts investigated)
- Assess SOC capacity (Sheet 5 - alerts per analyst)

## Pitfall: "100 use cases = good detection coverage"

**Problem**: Use case count != detection effectiveness

**Reality**: 10 well-tuned, high-maturity use cases more effective than 100 noisy, untuned rules.

**How to Avoid**:

- Assess use case maturity (Sheet 3 - maturity level 1-5)
- Measure false positive rate (Sheet 4 - FP%)
- Map to ATT&CK (Sheet 7 - actual threat coverage)

## Pitfall: "Daily review means automated dashboard check"

**Problem**: Policy requires review, but automated dashboard != analysis

**Reality**: Glancing at dashboard with green lights != meaningful log review. Analysts must investigate anomalies, trends, outliers.

**How to Avoid**:

- Define review procedures (Sheet 2 - what review entails)
- Evidence meaningful review (investigation tickets, findings)
- Quality over checkbox compliance

## Pitfall: "False positives are inevitable"

**Problem**: Accepting high FP rate as "normal"

**Reality**: >10% FP rate indicates inadequate tuning. Alert fatigue causes missed threats.

**How to Avoid**:

- Target <10% FP rate (Sheet 4 - FP% measurement)
- Active tuning program (Sheet 4 - tuning history)
- Regular use case review (Sheet 3 - last tuned date)

## Pitfall: "MTTR is 4 hours" (measured from IR, not log detection)

**Problem**: Measuring response time from IR engagement, not from initial log event

**Reality**: Event occurred Monday, detected Friday = 4-day MTTD (not 4 hours). Response clock starts at event occurrence, not analyst awareness.

**How to Avoid**:

- Measure MTTD from event to alert (Sheet 5)
- Separate MTTD from MTTR (detection vs. response)
- Include dwell time in metrics

## Pitfall: "We'll automate everything later"

**Problem**: Deferring automation while SOC drowns in manual work

**Reality**: Alert volume grows faster than SOC staffing. Without automation, backlog accumulates, burnout increases.

**How to Avoid**:

- Assess automation gaps (Sheet 6 - current vs. target state)
- Prioritize high-volume, low-complexity tasks for automation
- Incremental automation (don't wait for perfect SOAR)

---

# Quality Checklist

- [ ] All sheets completed
- [ ] Review process evidence collected (Sheet 2)
- [ ] Use case maturity assessed (Sheet 3)
- [ ] Alert metrics calculated (Sheet 4)
- [ ] SOC performance data extracted (Sheet 5)
- [ ] Automation assessment complete (Sheet 6)
- [ ] Threat detection coverage mapped (Sheet 7)
- [ ] Investigation procedures verified (Sheet 8)
- [ ] Gap analysis complete (Sheet 9)
- [ ] Evidence documented (Sheet 10)

---

# Review & Approval

**Level 1: Technical Review**

- SOC Manager + Threat Detection Lead
- Timeline: 2-3 days
- Focus: Accuracy of metrics, use case assessment

**Level 2: Management Review**

- Information Security Manager
- Timeline: 3-5 days
- Focus: Gap prioritization, resource needs

**Level 3: Executive Approval**

- CISO
- Timeline: 1-2 weeks
- Focus: Strategic alignment, capability investment

**Total Timeline**: 3-4 weeks from initiation to final approval

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->

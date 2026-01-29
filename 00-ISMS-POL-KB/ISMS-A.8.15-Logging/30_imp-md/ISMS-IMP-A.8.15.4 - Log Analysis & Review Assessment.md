# ISMS-IMP-A.8.15.4
## Log Analysis & Review Assessment
### Excel Workbook Layout Specification

**Document ID**: ISMS-IMP-A.8.15.4  
**Assessment Area**: Log Review, Analysis, and Detection Effectiveness  
**Related Policy**: ISMS-POL-A.8.15-S2.4 (Log Review & Analysis)  
**Purpose**: Assess log analysis capabilities and review process effectiveness  
**Python Generator**: `generate_a815_4_log_analysis_review.py`

---

## Workbook Structure

### Sheet 1: Instructions & Legend

**Header**: "Log Analysis & Review Assessment - ISO/IEC 27001:2022 Control A.8.15"

**Document Information Block**:
```
Document ID:           ISMS-IMP-A.8.15.4
Assessment Area:       Log Analysis & Review
Related Policy:        ISMS-POL-A.8.15-S2.4
Version:               1.0
Assessment Date:       [USER INPUT]
Assessment Period:     [USER INPUT - e.g., Q4 2025]
Completed By:          [USER INPUT]
Organization:          [USER INPUT]
Review Cycle:          Quarterly
```

**How to Use**:
1. Document review schedule compliance (daily/weekly/monthly)
2. Track detection use cases and effectiveness
3. Assess alert quality and false positive rates
4. Record incident detection metrics
5. Evaluate SOC analyst performance
6. Track investigation completeness
7. Review dashboard for effectiveness summary

---

### Sheet 2: Review Schedule Compliance

**Purpose**: Track compliance with required review schedule per S2.4.1-2

**Column Structure** (15 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Review Period | 20 | Date Range: Week of DD.MM.YYYY |
| B | Review Type | 18 | Dropdown: Daily, Weekly, Monthly |
| C | Scheduled Date | 15 | Date: DD.MM.YYYY |
| D | Actual Date | 15 | Date: DD.MM.YYYY |
| E | Completed On Time | 18 | Formula: =IF(D<=C,"Yes","Late") |
| F | Reviewer Name | 25 | Dropdown: List of authorized reviewers |
| G | Time Spent (minutes) | 20 | Number |
| H | Logs Reviewed | 30 | Text: Which log sources |
| I | Findings Count | 18 | Number: Issues identified |
| J | Incidents Created | 18 | Number: Tickets opened |
| K | False Positives | 18 | Number |
| L | Documentation Complete | 20 | Dropdown: Yes, Partial, No |
| M | Escalations Made | 18 | Number |
| N | Review Quality Score | 20 | Formula: Based on completeness |
| O | Notes | 40 | Text |

**Data Rows**: 60-180 (quarterly = ~90 daily reviews + 12 weekly + 3 monthly)

**Compliance Targets**:
- Daily reviews: 100% completion (Mon-Fri or 7 days/week)
- Weekly reviews: 100% completion
- Monthly reviews: 100% completion

**Metrics to Calculate**:
- % reviews completed on time
- Average time per review type
- Average findings per review

---

### Sheet 3: Detection Use Cases Inventory

**Purpose**: Document all detection use cases per S2.4.3.3

**Column Structure** (18 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Use Case ID | 15 | Auto: UC-001, UC-002 |
| B | Use Case Name | 30 | Text |
| C | Threat Category | 25 | Dropdown: Authentication Attack, Privilege Abuse, Data Exfiltration, Malware, Policy Violation, System Anomaly, Other |
| D | MITRE ATT&CK Technique | 25 | Text: T1078, T1566, etc. |
| E | Data Sources Required | 30 | Text: Log types needed |
| F | Detection Logic | 50 | Text: How it detects |
| G | Detection Method | 25 | Dropdown: Correlation Rule, Threshold, Anomaly Detection, Signature, ML/AI, Manual Query |
| H | Alert Severity | 15 | Dropdown: Critical, High, Medium, Low, Info |
| I | Status | 15 | Dropdown: Active, Testing, Disabled, Retired |
| J | Implemented Date | 15 | Date: DD.MM.YYYY |
| K | Last Tuned Date | 15 | Date: DD.MM.YYYY |
| L | True Positives (30d) | 20 | Number |
| M | False Positives (30d) | 20 | Number |
| N | False Positive Rate % | 20 | Formula: =M/(L+M) |
| O | Effectiveness Rating | 20 | Dropdown: Excellent, Good, Fair, Poor |
| P | Owner | 25 | Text: Who maintains this |
| Q | Next Review Date | 15 | Date |
| R | Notes | 40 | Text |

**Data Rows**: 50-200 (use cases)

**Recommended Minimum Use Cases** (from S2.4.3.3):
- Failed authentication threshold (10+ failures in 1 hour)
- Privileged account usage outside business hours
- New user account creation
- Unusual data access volume
- Malware detection
- Critical system configuration changes

---

### Sheet 4: Alert Quality Analysis

**Purpose**: Analyze alert effectiveness and false positive rates

**Column Structure** (16 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Alert Source / Rule Name | 30 | Text |
| B | Alert Type | 25 | Dropdown: Security, Operational, Compliance, Performance |
| C | Severity | 15 | Dropdown: Critical, High, Medium, Low |
| D | Total Alerts (30d) | 20 | Number |
| E | True Positives | 18 | Number |
| F | False Positives | 18 | Number |
| G | Unreviewed | 15 | Number |
| H | True Positive Rate % | 20 | Formula: =E/D |
| I | False Positive Rate % | 20 | Formula: =F/D |
| J | Alert Quality Score | 20 | Formula: TP/(TP+FP) - target >50% |
| K | Status | 15 | Formula: Green if >50%, Yellow 20-50%, Red <20% |
| L | Average Investigation Time | 22 | Number: Minutes |
| M | Tuning Required | 18 | Dropdown: Yes (urgent), Yes, No |
| N | Tuning Action | 40 | Text: How to improve |
| O | Last Tuned | 15 | Date |
| P | Notes | 40 | Text |

**Data Rows**: 50-200 (alert sources)

**Analysis Section** (below data):
- Top 10 worst performers (highest false positive rate)
- Top 10 by volume (most alerts generated)
- Alerts requiring immediate tuning (FP rate >50%)

**Target Alert Quality**:
- Critical alerts: >80% true positive rate
- High alerts: >60% true positive rate
- Medium alerts: >50% true positive rate
- Overall: <10% false positive rate

---

### Sheet 5: Incident Detection Metrics

**Purpose**: Track security incident detection effectiveness

**Column Structure** (17 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Incident ID | 15 | Text: INC-2025-001 |
| B | Detection Date | 15 | Date: DD.MM.YYYY |
| C | Incident Type | 25 | Dropdown: Malware, Intrusion, Data Breach, Policy Violation, Unauthorized Access, Other |
| D | Severity | 15 | Dropdown: Critical, High, Medium, Low |
| E | Detected By | 25 | Dropdown: Automated Alert, Manual Review, User Report, External Notification |
| F | Detection Method | 25 | Dropdown: SIEM Rule, Anomaly Detection, Threat Intelligence, Manual Query |
| G | Incident Occurred Date | 18 | Date: When attack happened |
| H | Time to Detect (hours) | 20 | Formula: =A-G (MTTD) |
| I | Response Start Time | 18 | Datetime |
| J | Time to Respond (hours) | 20 | Formula: =I-A (MTTR) |
| K | Containment Time | 18 | Datetime |
| L | Time to Contain (hours) | 20 | Formula: =K-I |
| M | Resolution Date | 15 | Date |
| N | Total Resolution Time | 20 | Formula: =M-A |
| O | Investigation Complete | 18 | Dropdown: Yes, No, In Progress |
| P | Lessons Learned Captured | 22 | Dropdown: Yes, No |
| Q | Notes | 40 | Text |

**Data Rows**: Variable (all incidents in assessment period)

**Metrics to Calculate**:
- **Mean Time to Detect (MTTD)**: Average of column H
- **Mean Time to Respond (MTTR)**: Average of column J
- **Mean Time to Contain**: Average of column L
- **Detection by Method**: COUNT by detection method

**Targets** (from S2.4.8):
- MTTD: <1 hour (critical), <24 hours (high)
- MTTR: <4 hours (critical), <24 hours (high)

---

### Sheet 6: Investigation Quality Assessment

**Purpose**: Assess investigation thoroughness per S2.4.6

**Column Structure** (16 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Incident ID | 15 | Text (links to Sheet 5) |
| B | Investigator | 25 | Text: Name |
| C | Timeline Documented | 18 | Dropdown: Yes, No, Partial |
| D | Root Cause Identified | 20 | Dropdown: Yes, No, Unknown |
| E | Scope Assessed | 18 | Dropdown: Complete, Partial, None |
| F | Evidence Collected | 18 | Dropdown: Complete, Partial, None |
| G | Logs Analyzed | 30 | Text: Which sources reviewed |
| H | IOCs Documented | 18 | Dropdown: Yes, No, N/A |
| I | Actions Documented | 18 | Dropdown: Complete, Partial, None |
| J | Report Completeness | 20 | Dropdown: Complete, Partial, Incomplete |
| K | Lessons Learned | 18 | Dropdown: Yes, No |
| L | Post-Incident Review Done | 22 | Dropdown: Yes, No, Scheduled |
| M | Investigation Quality Score | 22 | Formula: % of Yes answers |
| N | Status | 15 | Formula: Green >80%, Yellow >60%, Red <60% |
| O | Improvement Areas | 40 | Text |
| P | Notes | 40 | Text |

**Data Rows**: Variable (matches incidents from Sheet 5)

**Quality Targets**:
- Investigation completeness: >90% for Critical/High incidents
- Root cause identification: >80% overall
- Documentation completeness: 100% for all incidents

---

### Sheet 7: SOC Analyst Performance

**Purpose**: Track SOC analyst workload and effectiveness

**Column Structure** (16 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Analyst Name | 25 | Text |
| B | Role | 20 | Dropdown: Tier 1, Tier 2, Tier 3, Lead |
| C | Assessment Period | 20 | Text: Month/Quarter |
| D | Shifts Worked | 15 | Number |
| E | Alerts Reviewed | 18 | Number |
| F | Alerts per Shift | 18 | Formula: =E/D |
| G | Incidents Investigated | 20 | Number |
| H | Incidents Escalated | 20 | Number |
| I | True Positives Identified | 22 | Number |
| J | False Positives Flagged | 22 | Number |
| K | Accuracy Rate % | 18 | Formula: =I/(I+J) |
| L | Avg Investigation Time (min) | 25 | Number |
| M | Reviews Completed On Time | 22 | Number / Total |
| N | Training Hours | 18 | Number |
| O | Performance Rating | 20 | Dropdown: Exceeds, Meets, Needs Improvement |
| P | Notes | 40 | Text |

**Data Rows**: 5-20 (SOC analysts)

**Performance Benchmarks**:
- Alerts per shift: 20-50 (depends on alert quality)
- Accuracy rate: >85%
- On-time reviews: >95%
- Training: Minimum 8 hours per quarter

---

### Sheet 8: Anomaly Detection Assessment

**Purpose**: Assess behavioral analytics and anomaly detection per S2.4.4

**Column Structure** (15 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Anomaly Detection Type | 30 | Dropdown: User Behavior, System Behavior, Network Behavior, Data Access Patterns |
| B | Implementation Status | 20 | Dropdown: Implemented, Testing, Planned, Not Implemented |
| C | Technology Used | 25 | Dropdown: SIEM Native, UEBA Tool, Custom Script, ML/AI Platform, None |
| D | Baseline Established | 18 | Dropdown: Yes, No, In Progress |
| E | Baseline Period (days) | 20 | Number: 30-90 days typical |
| F | Last Baseline Update | 18 | Date: DD.MM.YYYY |
| G | Anomalies Detected (30d) | 22 | Number |
| H | True Anomalies | 18 | Number: Actual issues |
| I | False Positives | 18 | Number |
| J | Detection Accuracy % | 20 | Formula: =H/G |
| K | Actionable Alerts | 18 | Number: Led to investigation |
| L | Value Rating | 15 | Dropdown: High, Medium, Low, None |
| M | Tuning Required | 18 | Dropdown: Yes, No |
| N | Next Review Date | 15 | Date |
| O | Notes | 40 | Text |

**Data Rows**: 10-30 (anomaly detection methods)

**Assessment Questions**:
- Are behavioral baselines established?
- Are baselines updated regularly?
- Is anomaly detection providing value?
- What's the false positive rate?

---

### Sheet 9: Threat Intelligence Integration

**Purpose**: Assess threat intelligence usage per S2.4.9.2

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Threat Feed Name | 30 | Text |
| B | Feed Type | 25 | Dropdown: Commercial, Government, Open Source, Industry ISAC, Internal |
| C | Feed Category | 25 | Dropdown: IOC (IP/Domain/Hash), Vulnerability, Threat Actor, Campaign, General |
| D | Integration Method | 25 | Dropdown: SIEM Native, API, Manual Import, TAXII/STIX, Other |
| E | Update Frequency | 20 | Dropdown: Real-time, Hourly, Daily, Weekly |
| F | Last Update | 15 | Date: DD.MM.YYYY |
| G | IOCs Active | 18 | Number: Currently in SIEM |
| H | Matches (30d) | 18 | Number: Hits on IOCs |
| I | True Positives | 18 | Number |
| J | False Positives | 18 | Number |
| K | Feed Quality Score | 20 | Formula: TP/(TP+FP) |
| L | Status | 15 | Dropdown: Active, Inactive, Evaluating |
| M | Value Assessment | 20 | Dropdown: High, Medium, Low, None |
| N | Notes | 40 | Text |

**Data Rows**: 5-20 (threat feeds)

**Key Questions**:
- Are threat feeds integrated into detection?
- Are IOCs being matched against logs?
- Which feeds provide most value?
- Are false positives from feeds managed?

---

### Sheet 10: Detection Coverage Matrix

**Purpose**: Map detection coverage to MITRE ATT&CK framework

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | ATT&CK Tactic | 25 | Dropdown: Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Exfiltration, C2, Impact |
| B | ATT&CK Technique | 30 | Text: T#### - Technique name |
| C | Technique Relevance | 20 | Dropdown: High, Medium, Low, N/A |
| D | Detection Implemented | 20 | Dropdown: Yes, Partial, No |
| E | Detection Method | 25 | Dropdown: SIEM Rule, Anomaly, Signature, Manual, None |
| F | Use Case ID | 15 | Text: Links to Sheet 3 |
| G | Log Sources Required | 30 | Text |
| H | Log Sources Available | 30 | Text |
| I | Coverage Gap | 18 | Dropdown: None, Partial, Complete |
| J | Detection Tested | 18 | Dropdown: Yes, No |
| K | Last Test Date | 15 | Date |
| L | Priority | 15 | Dropdown: Critical, High, Medium, Low |
| M | Remediation Plan | 40 | Text: If gap exists |
| N | Notes | 40 | Text |

**Data Rows**: 100-200 (MITRE techniques)

**Coverage Analysis**:
- % of high-relevance techniques with detection
- % of techniques with complete coverage
- Priority gaps requiring detection development

---

### Sheet 11: Review Process Effectiveness

**Purpose**: Assess overall review process quality

**Column Structure** (13 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Process Element | 30 | Dropdown: Daily Review, Weekly Review, Monthly Review, Alert Triage, Investigation, Documentation, Escalation, Training, Tools |
| B | Process Owner | 25 | Text: Role responsible |
| C | Process Documented | 18 | Dropdown: Yes, No, Partial |
| D | Staff Trained | 18 | Dropdown: All, Most, Some, None |
| E | Tools Adequate | 18 | Dropdown: Yes, No, Partial |
| F | Process Followed | 18 | Dropdown: Always, Usually, Sometimes, Rarely |
| G | Quality Score | 15 | Number: 1-5 rating |
| H | Effectiveness Rating | 20 | Dropdown: Excellent, Good, Fair, Poor |
| I | Issues Identified | 40 | Text |
| J | Improvement Actions | 40 | Text |
| K | Action Owner | 25 | Text |
| L | Target Date | 15 | Date |
| M | Notes | 40 | Text |

**Data Rows**: 10-20 (process elements)

---

### Sheet 12: Gap Analysis

**Purpose**: Consolidated gaps in analysis and review

**Column Structure** (12 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 12 | Auto: GAP-001 |
| B | Gap Category | 25 | Dropdown: Review Process, Detection Coverage, Alert Quality, Investigation Quality, Tools/Technology, Staffing, Training, Documentation |
| C | Description | 50 | Text |
| D | Impact | 20 | Dropdown: Critical, High, Medium, Low |
| E | Current State | 40 | Text |
| F | Target State | 40 | Text |
| G | Remediation Action | 50 | Text |
| H | Owner | 25 | Text |
| I | Target Date | 15 | Date |
| J | Budget Required | 18 | Dropdown: Yes, No |
| K | Status | 15 | Dropdown: Open, In Progress, Resolved |
| L | Notes | 40 | Text |

---

### Sheet 13: Summary Dashboard

**Section 1: Review Compliance Summary** (Rows 3-12):

| Review Type | Required Count | Completed | On Time % | Avg Time | Target |
|-------------|----------------|-----------|-----------|----------|--------|
| Daily | Formula (business days) | COUNT | Formula | AVG | 100% |
| Weekly | Formula (weeks in period) | COUNT | Formula | AVG | 100% |
| Monthly | Formula (months) | COUNT | Formula | AVG | 100% |
| Overall | SUM | SUM | Formula | N/A | 100% |

**Section 2: Detection Effectiveness** (Rows 14-25):

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Use Cases | COUNT(Sheet3) | N/A | Info |
| Active Use Cases | COUNTIF(Sheet3, "Active") | N/A | Info |
| Avg False Positive Rate | AVERAGE(Sheet3) | <10% | Status |
| True Positive Rate | Formula | >50% | Status |
| Use Cases Needing Tuning | COUNT | 0 | Status |
| Detection Coverage % | From Sheet 10 | >90% | Status |
| MTTD - Critical (hours) | AVG(Sheet5) | <1 | Status |
| MTTR - Critical (hours) | AVG(Sheet5) | <4 | Status |

**Section 3: Alert Quality Summary** (Rows 27-38):

| Severity | Total Alerts | True Pos | False Pos | FP Rate % | Quality Score |
|----------|--------------|----------|-----------|-----------|---------------|
| Critical | SUM | SUM | SUM | Formula | Formula |
| High | SUM | SUM | SUM | Formula | Formula |
| Medium | SUM | SUM | SUM | Formula | Formula |
| Low | SUM | SUM | SUM | Formula | Formula |
| Total | SUM | SUM | SUM | Formula | Formula |

**Section 4: Incident Metrics** (Rows 40-50):

| Incident Type | Count | Avg MTTD | Avg MTTR | Detection Method (most common) |
|---------------|-------|----------|----------|-------------------------------|
| Malware | COUNT | AVG | AVG | MODE |
| Intrusion | COUNT | AVG | AVG | MODE |
| Data Breach | COUNT | AVG | AVG | MODE |
| Policy Violation | COUNT | AVG | AVG | MODE |
| Other | COUNT | AVG | AVG | MODE |

**Section 5: Charts** (Rows 52-75):
- Alert volume trend (last 90 days)
- False positive rate trend
- Detection coverage heat map (MITRE ATT&CK)
- Incident detection time distribution

**Section 6: Top Gaps** (Rows 77-90):
Top 10 gaps from Sheet 12 by impact

**Section 7: Recommendations** (Rows 92-105):
Key improvement recommendations

---

### Sheet 14: Approval & Sign-Off

**Approval Table**:

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| SOC Lead | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |
| Security Engineers | [Names] | DD.MM.YYYY | _____ | [ ] Reviewed |
| Information Security Manager | [Name] | DD.MM.YYYY | _____ | [ ] Approved |

---

## File Naming Convention

**Filename**: `ISMS-IMP-A_8_15_4_Log_Analysis_Review_YYYYMMDD.xlsx`

---

**END OF IMP SPECIFICATION A.8.15.4**
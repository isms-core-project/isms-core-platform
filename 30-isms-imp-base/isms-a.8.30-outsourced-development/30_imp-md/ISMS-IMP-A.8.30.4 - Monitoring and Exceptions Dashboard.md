# ISMS-IMP-A.8.30.4 – Monitoring and Exceptions Dashboard

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.4 |
| **Document Title** | Monitoring and Exceptions Dashboard Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

---

## 1. Workbook Purpose

This dashboard consolidates outsourced development security status, tracks exceptions, and provides executive reporting on vendor security compliance.

**Primary Use Cases**:
- Executive visibility into outsourced development security
- Exception tracking and management
- Vendor performance monitoring
- Compliance scoring and trend analysis
- Audit evidence consolidation

---

## 2. Workbook Structure

### Sheet 1: Executive Dashboard

| Metric | Description | Target | Current | Trend |
|--------|-------------|--------|---------|-------|
| Approved Vendors | Vendors in approved registry | N/A | [Count] | [↑↓→] |
| Active Contracts | Contracts currently active | N/A | [Count] | [↑↓→] |
| Pending Assessments | Vendors awaiting assessment | 0 | [Count] | [↑↓→] |
| Overdue Reassessments | Annual reassessments overdue | 0 | [Count] | [↑↓→] |
| Contract Clause Compliance | Contracts with all security clauses | 100% | [%] | [↑↓→] |
| SLA Compliance (Critical) | Critical vulns fixed within SLA | ≥95% | [%] | [↑↓→] |
| SLA Compliance (High) | High vulns fixed within SLA | ≥90% | [%] | [↑↓→] |
| Security Testing Completion | Deliverables with complete testing | 100% | [%] | [↑↓→] |
| SBOM Compliance | Deliverables with SBOM received | 100% | [%] | [↑↓→] |
| Active Exceptions | Open security exceptions | [Track] | [Count] | [↑↓→] |
| Overdue Exceptions | Exceptions past expiry | 0 | [Count] | [↑↓→] |
| Overall Compliance Score | Weighted compliance score | ≥90% | [%] | [↑↓→] |

### Sheet 2: Vendor Performance

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Vendor_ID | Vendor identifier | Reference | Valid Vendor_ID |
| Vendor_Name | Vendor name | Text | From registry |
| Risk_Tier | Vendor risk classification | Dropdown | Critical, High, Standard |
| Active_Contracts | Number of active contracts | Number | Integer |
| Total_Deliverables | Deliverables received (12 months) | Number | Integer |
| Security_Findings_Total | Total security findings | Number | Integer |
| Critical_Findings | Critical findings | Number | Integer |
| High_Findings | High findings | Number | Integer |
| SLA_Compliance_Rate | Percentage of SLAs met | Percentage | 0-100% |
| Avg_Remediation_Days | Average days to remediate | Number | Decimal |
| Security_Incidents | Security incidents (12 months) | Number | Integer |
| Last_Assessment_Date | Most recent assessment | Date | DD.MM.YYYY |
| Performance_Score | Calculated performance score | Number | 0-100 |
| Performance_Trend | Trend vs previous period | Dropdown | Improving, Stable, Declining |
| Notes | Performance notes | Text | Optional |

**Performance Score Calculation**:
- SLA Compliance (40%)
- Findings Severity (30%)
- Assessment Currency (15%)
- Incident History (15%)

### Sheet 3: Exception Register

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Exception_ID | Unique exception identifier | Text | EXC-XXXX format |
| Exception_Type | Type of exception | Dropdown | Vendor Assessment, Contract Clause, SLA, Testing, Training |
| Related_Entity | Vendor/Contract/Deliverable | Text | ID reference |
| Requirement_Reference | Policy requirement being excepted | Text | POL section reference |
| Exception_Description | Description of exception | Text | Required |
| Risk_Level | Risk of exception | Dropdown | Critical, High, Medium, Low |
| Business_Justification | Reason for exception | Text | Required |
| Compensating_Controls | Controls in place | Text | Required |
| Requested_By | Person requesting | Text | Name |
| Request_Date | Date requested | Date | DD.MM.YYYY |
| Approved_By | Approver | Text | Name + Role |
| Approval_Date | Date approved | Date | DD.MM.YYYY |
| Expiry_Date | Exception expiration | Date | DD.MM.YYYY |
| Status | Current status | Dropdown | Pending, Approved, Rejected, Expired, Renewed |
| Renewal_Count | Times renewed | Number | Integer |
| Last_Review_Date | Last review date | Date | DD.MM.YYYY |
| Next_Review_Date | Next scheduled review | Date | DD.MM.YYYY |
| Closure_Date | Date closed | Date | DD.MM.YYYY |
| Closure_Reason | How closed | Dropdown | Remediated, Risk Accepted, Terminated, N/A |

### Sheet 4: Monitoring Log

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Log_ID | Unique log entry | Text | LOG-XXXX format |
| Log_Date | Date of activity | Date | DD.MM.YYYY |
| Vendor_ID | Vendor being monitored | Reference | Valid Vendor_ID |
| Contract_ID | Related contract | Reference | Valid Contract_ID |
| Activity_Type | Type of monitoring activity | Dropdown | Status Meeting, Security Review, Audit, Incident Review, Ad-hoc |
| Activity_Description | Description of activity | Text | Required |
| Participants | People involved | Text | Names |
| Findings | Key findings/observations | Text | Optional |
| Actions_Required | Follow-up actions | Text | Optional |
| Action_Owner | Person responsible | Text | Name |
| Action_Due_Date | Due date for actions | Date | DD.MM.YYYY |
| Action_Status | Action completion status | Dropdown | Open, In Progress, Complete, Overdue |
| Evidence_Reference | Meeting notes/documents | Text | File path/URL |

### Sheet 5: Incident Log

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Incident_ID | Unique incident identifier | Text | INC-XXXX format |
| Incident_Date | Date of incident | Date | DD.MM.YYYY |
| Vendor_ID | Vendor involved | Reference | Valid Vendor_ID |
| Contract_ID | Related contract | Reference | Valid Contract_ID |
| Incident_Type | Type of security incident | Dropdown | Data Breach, Vulnerability Exploited, Unauthorized Access, Policy Violation, Other |
| Severity | Incident severity | Dropdown | Critical, High, Medium, Low |
| Description | Incident description | Text | Required |
| Root_Cause | Root cause analysis | Text | After investigation |
| Impact_Assessment | Impact on [Organization] | Text | Description |
| Notification_Date | When [Organization] notified | Date | DD.MM.YYYY |
| Notification_SLA_Met | Notified within 24 hours | Dropdown | Yes, No |
| Remediation_Actions | Actions taken | Text | Description |
| Remediation_Date | Date remediated | Date | DD.MM.YYYY |
| Lessons_Learned | Lessons learned | Text | Optional |
| Status | Incident status | Dropdown | Open, Investigating, Remediated, Closed |
| Closed_Date | Date closed | Date | DD.MM.YYYY |
| Contract_Impact | Impact on contract | Dropdown | None, Warning, Review, Suspension, Termination |

### Sheet 6: Compliance Score Calculation

| Component | Weight | Scoring Criteria | Data Source |
|-----------|--------|------------------|-------------|
| Vendor Assessment | 20% | % vendors with current assessment | Workbook 1 |
| Contract Compliance | 25% | % contracts with all security clauses | Workbook 2 |
| SLA Compliance | 25% | Weighted avg of Critical (40%) + High (60%) SLA compliance | Workbook 2 |
| Security Testing | 20% | % deliverables with complete testing | Workbook 3 |
| Exception Management | 10% | 100% - (Overdue exceptions × 10%) | Sheet 3 |

**Score Calculation**:
```
Overall Score = (Vendor × 0.20) + (Contract × 0.25) + (SLA × 0.25) + (Testing × 0.20) + (Exception × 0.10)
```

**Score Interpretation**:
- ≥90%: Compliant (Green)
- 70-89%: Needs Improvement (Yellow)
- <70%: Non-Compliant (Red) - Escalation required

---

## 3. Data Sources

| Data Element | Source System | Collection Method |
|--------------|---------------|-------------------|
| Vendor data | Workbook 1 | Automated aggregation |
| Contract data | Workbook 2 | Automated aggregation |
| Testing data | Workbook 3 | Automated aggregation |
| Exception data | Manual entry | Approval workflow |
| Monitoring log | Manual entry | Meeting records |
| Incident data | Incident management system | Manual entry / Import |

---

## 4. Reporting Cadence

| Report | Audience | Frequency |
|--------|----------|-----------|
| Executive Dashboard | CISO, Executive Management | Monthly |
| Vendor Performance | IT Security Manager, Procurement | Quarterly |
| Exception Status | CISO, Risk Committee | Monthly |
| Compliance Score Trend | CISO, Audit Committee | Quarterly |
| Incident Summary | CISO, Executive Management | As needed + Quarterly |

---

## 5. Automation Requirements

**Automated Aggregation**:
- Pull metrics from Workbooks 1-3
- Calculate performance scores
- Generate compliance score

**Automated Alerts**:
- Compliance score drops below 80%
- Exception approaching expiry (30 days)
- Exception overdue (immediate)
- Incident reported (immediate)
- Vendor performance declining (quarterly)

**Automated Reports**:
- Monthly executive dashboard PDF
- Quarterly vendor performance summary
- Annual compliance trend report

---

## 6. Evidence Package

For ISO 27001 audit, generate:
- 12-month compliance score trend
- Vendor performance summary
- Exception register (current + closed in period)
- Monitoring activity log
- Incident summary
- Sample monthly executive reports

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-01 -->

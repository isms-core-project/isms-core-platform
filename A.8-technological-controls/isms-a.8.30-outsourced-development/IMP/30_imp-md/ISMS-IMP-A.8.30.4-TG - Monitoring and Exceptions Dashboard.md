**ISMS-IMP-A.8.30.4-TG - Monitoring and Exceptions Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.4-TG |
| **Document Title** | Monitoring and Exceptions Dashboard Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

# Technical Specification

This section provides technical details for the Monitoring and Exceptions Dashboard implementation.

---

## 9. Workbook Technical Structure

### 9.1 Workbook Properties

| Property | Value |
|----------|-------|
| File Format | .xlsx (Excel 2016+) |
| Sheet Protection | Structure protected, cells unlocked for input |
| Workbook Protection | Structure only |
| File Naming | ISMS-IMP-A.8.30.4_Monitoring_Dashboard_YYYYMMDD.xlsx |

### 9.2 Sheet Configuration

| Sheet | Tab Colour | Protection Level | Hidden |
|-------|------------|------------------|--------|
| Executive Dashboard | Dark Blue (#002060) | Full (display only) | No |
| Vendor Performance | Green (#70AD47) | Input cells unlocked | No |
| Exception Register | Orange (#ED7D31) | Input cells unlocked | No |
| Monitoring Log | Blue (#4472C4) | Input cells unlocked | No |
| Incident Log | Red (#C00000) | Input cells unlocked | No |
| Compliance Score | Purple (#7030A0) | Input cells unlocked | No |
| Validation Lists | Grey (#A6A6A6) | Full protection | Yes |

---

## 10. Sheet Specifications

### 10.1 Sheet 1: Executive Dashboard – Technical Specification

**Layout Configuration:**

| Section | Position | Content |
|---------|----------|---------|
| Header | Row 1-3 | Title, Report Period |
| Overall Score | Row 5 | Compliance score with trend |
| Vendor Metrics | Row 7-12 | Vendor management KPIs |
| Contract Metrics | Row 7-12 | Contract compliance KPIs |
| Testing Metrics | Row 14-18 | Security testing KPIs |
| Exception Metrics | Row 14-18 | Exception management KPIs |
| Commentary | Row 20-25 | Key observations |

**Data Links:**

| Metric | Source Reference |
|--------|------------------|
| Overall Score | ='Compliance Score'!B15 |
| Approved Vendors | =[Workbook1]'Vendor Registry'!COUNT(Status="Approved") |
| Active Contracts | =[Workbook2]'Contract Inventory'!COUNT(Status="Active") |
| Active Exceptions | =COUNTIF('Exception Register'!L:L,"Approved") |

### 10.2 Sheet 2: Vendor Performance – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Vendor_ID | 15 | Reference | Must exist | Yes |
| B | Vendor_Name | 35 | Text | From registry | Yes |
| C | Risk_Tier | 12 | List | Critical,High,Standard | Yes |
| D | Active_Contracts | 10 | Number | Integer >= 0 | Yes |
| E | Total_Deliverables | 10 | Number | Integer >= 0 | Yes |
| F | Security_Findings_Total | 10 | Number | Integer >= 0 | Yes |
| G | Critical_Findings | 10 | Number | Integer >= 0 | Yes |
| H | High_Findings | 10 | Number | Integer >= 0 | Yes |
| I | SLA_Compliance_Rate | 12 | Percentage | 0-100% | Yes |
| J | Avg_Remediation_Days | 10 | Number | Decimal >= 0 | Yes |
| K | Security_Incidents | 10 | Number | Integer >= 0 | Yes |
| L | Last_Assessment_Date | 15 | Date | DD.MM.YYYY | Yes |
| M | Performance_Score | 10 | Number | 0-100 calculated | Auto |
| N | Performance_Trend | 12 | List | Improving,Stable,Declining | Yes |
| O | Notes | 40 | Text | Optional | No |

**Formulas:**

```excel
Performance_Score (M2):
=(I2*40)+(MAX(0,100-(G2*20+H2*10+F2*2))/100*30)+
(IF(L2>=TODAY()-365,100,MAX(0,100-(DATEDIF(L2,TODAY(),"M")-12)*5))/100*15)+
(MAX(0,100-K2*25)/100*15)
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Performance_Score >= 90 | Green fill |
| Performance_Score >= 70 | No fill |
| Performance_Score >= 60 | Yellow fill |
| Performance_Score < 60 | Red fill |
| Performance_Trend = "Declining" | Red text |

### 10.3 Sheet 3: Exception Register – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Exception_ID | 15 | Text | Format: EXC-#### | Yes |
| B | Exception_Type | 20 | List | Vendor Assessment,Contract Clause,SLA,Testing,Training | Yes |
| C | Related_Entity | 20 | Text | ID reference | Yes |
| D | Requirement_Reference | 25 | Text | POL section | Yes |
| E | Exception_Description | 50 | Text | Required | Yes |
| F | Risk_Level | 12 | List | Critical,High,Medium,Low | Yes |
| G | Business_Justification | 50 | Text | Required | Yes |
| H | Compensating_Controls | 50 | Text | Required | Yes |
| I | Requested_By | 20 | Text | Name | Yes |
| J | Request_Date | 15 | Date | DD.MM.YYYY | Yes |
| K | Approved_By | 25 | Text | Name + Role | Conditional |
| L | Approval_Date | 15 | Date | DD.MM.YYYY | Conditional |
| M | Expiry_Date | 15 | Date | DD.MM.YYYY | Yes |
| N | Status | 15 | List | Pending,Approved,Rejected,Expired,Renewed | Yes |
| O | Renewal_Count | 10 | Number | Integer >= 0 | Yes |
| P | Last_Review_Date | 15 | Date | DD.MM.YYYY | Conditional |
| Q | Next_Review_Date | 15 | Date | DD.MM.YYYY | Conditional |
| R | Closure_Date | 15 | Date | DD.MM.YYYY | Conditional |
| S | Closure_Reason | 20 | List | Remediated,Risk Accepted,Terminated,N/A | Conditional |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Status = "Pending" | Yellow fill |
| Status = "Approved" AND Expiry_Date < TODAY() | Red fill |
| Status = "Approved" AND Expiry_Date < TODAY()+30 | Orange fill |
| Renewal_Count >= 3 | Red border |
| Risk_Level = "Critical" | Red text |

### 10.4 Sheet 4: Monitoring Log – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Log_ID | 15 | Text | Format: LOG-#### | Yes |
| B | Log_Date | 15 | Date | DD.MM.YYYY | Yes |
| C | Vendor_ID | 15 | Reference | Must exist | Yes |
| D | Contract_ID | 15 | Reference | Must exist | Conditional |
| E | Activity_Type | 20 | List | Status Meeting,Security Review,Audit,Incident Review,Ad-hoc | Yes |
| F | Activity_Description | 50 | Text | Required | Yes |
| G | Participants | 30 | Text | Names | Yes |
| H | Findings | 50 | Text | Optional | No |
| I | Actions_Required | 50 | Text | Optional | No |
| J | Action_Owner | 20 | Text | Name | Conditional |
| K | Action_Due_Date | 15 | Date | DD.MM.YYYY | Conditional |
| L | Action_Status | 15 | List | Open,In Progress,Complete,Overdue | Conditional |
| M | Evidence_Reference | 40 | Text | File path/URL | Yes |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Action_Status = "Overdue" | Red fill |
| Action_Status = "Open" AND Action_Due_Date < TODAY() | Red fill |
| Action_Status = "Complete" | Green fill |

### 10.5 Sheet 5: Incident Log – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Incident_ID | 15 | Text | Format: INC-#### | Yes |
| B | Incident_Date | 15 | Date | DD.MM.YYYY | Yes |
| C | Vendor_ID | 15 | Reference | Must exist | Yes |
| D | Contract_ID | 15 | Reference | Must exist | Conditional |
| E | Incident_Type | 25 | List | Data Breach,Vulnerability Exploited,Unauthorized Access,Policy Violation,Other | Yes |
| F | Severity | 12 | List | Critical,High,Medium,Low | Yes |
| G | Description | 50 | Text | Required | Yes |
| H | Root_Cause | 50 | Text | After investigation | Conditional |
| I | Impact_Assessment | 50 | Text | Description | Yes |
| J | Notification_Date | 15 | Date | DD.MM.YYYY | Yes |
| K | Notification_SLA_Met | 12 | List | Yes,No | Yes |
| L | Remediation_Actions | 50 | Text | Description | Yes |
| M | Remediation_Date | 15 | Date | DD.MM.YYYY | Conditional |
| N | Lessons_Learned | 50 | Text | Optional | No |
| O | Status | 15 | List | Open,Investigating,Remediated,Closed | Yes |
| P | Closed_Date | 15 | Date | DD.MM.YYYY | Conditional |
| Q | Contract_Impact | 20 | List | None,Warning,Review,Suspension,Termination | Yes |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Severity = "Critical" | Red fill |
| Severity = "High" | Orange fill |
| Status = "Open" | Yellow row |
| Notification_SLA_Met = "No" | Red text |
| Contract_Impact = "Termination" | Red border |

### 10.6 Sheet 6: Compliance Score Calculation – Technical Specification

**Score Components:**

| Row | Component | Weight | Formula |
|-----|-----------|--------|---------|
| 3 | Vendor Assessment | 20% | =[Workbook1 calc] |
| 5 | Contract Compliance | 25% | =[Workbook2 calc] |
| 7 | SLA Compliance | 25% | =[Workbook2 calc] |
| 9 | Security Testing | 20% | =[Workbook3 calc] |
| 11 | Exception Management | 10% | =100-COUNTIF(Sheet3!M:M,"<"&TODAY())*10 |
| 15 | **Overall Score** | 100% | =SUM weighted components |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Overall Score >= 90 | Green fill |
| Overall Score >= 70 | Yellow fill |
| Overall Score < 70 | Red fill |

---

## 11. Automation Requirements

### 11.1 Automated Alerts

| Trigger | Alert Type | Recipients | Timing |
|---------|------------|------------|--------|
| Compliance score < 80% | Email | CISO | Immediate |
| Exception expiry approaching | Email | Exception owner | 30 days |
| Exception overdue | Email + Dashboard | CISO | Immediate |
| Incident reported | Email | CISO, IT Security Manager | Immediate |
| Vendor performance declining | Email | IT Security Manager | Quarterly |
| Action overdue | Email | Action owner | Daily |

### 11.2 Data Refresh Automation

| Data Element | Refresh Method | Frequency |
|--------------|----------------|-----------|
| Source workbook links | Manual refresh | Weekly |
| Compliance score | Auto-calculate | Real-time |
| Dashboard metrics | Manual update | Weekly |
| Vendor scores | Manual update | Monthly |
| Exception status | Manual review | Weekly |

### 11.3 Report Generation

| Report | Format | Generation | Distribution |
|--------|--------|------------|--------------|
| Monthly Dashboard | PDF | Manual export | Email to management |
| Quarterly Performance | PDF/Excel | Manual | Email to stakeholders |
| Annual Compliance | PDF | Manual | Formal distribution |

---

## 12. Metrics and KPIs

### 12.1 Dashboard Metrics

| Metric | Target | Threshold | Owner |
|--------|--------|-----------|-------|
| Overall Compliance Score | ≥90% | <70% critical | CISO |
| Vendor Assessment Currency | 100% | <90% warning | IT Security |
| Contract Clause Compliance | 100% | <95% warning | IT Security |
| SLA Compliance (Critical) | ≥95% | <90% critical | IT Security |
| Active Exceptions | Minimal | Track trend | CISO |

### 12.2 Exception Metrics

| Metric | Target | Threshold | Owner |
|--------|--------|-----------|-------|
| Overdue Exceptions | 0 | >0 critical | IT Security |
| Average Exception Duration | <90 days | >180 days warning | CISO |
| Renewal Rate | <20% | >50% warning | CISO |
| Exception Closure Rate | >80% | <50% warning | IT Security |

### 12.3 Incident Metrics

| Metric | Target | Threshold | Owner |
|--------|--------|-----------|-------|
| Vendor Incidents (Annual) | 0 | Any tracking | CISO |
| Notification SLA Compliance | 100% | <90% critical | IT Security |
| Average Resolution Time | <30 days | >60 days warning | IT Security |
| Contract Impact Rate | 0% | >10% warning | CISO |

---

## 13. Evidence Package for ISO 27001 Audit

### 13.1 Standard Evidence Package

| Document | Purpose | Preparation |
|----------|---------|-------------|
| 12-month compliance trend | Compliance demonstration | Score history export |
| Vendor performance summary | Vendor management evidence | Sheet 2 annual summary |
| Exception register (current + closed) | Exception governance | Sheet 3 export |
| Monitoring activity log | Active monitoring evidence | Sheet 4 12-month export |
| Incident summary | Incident management evidence | Sheet 5 summary |
| Sample monthly reports | Reporting evidence | PDF archives |

### 13.2 Audit Preparation Checklist

- [ ] Export 12-month compliance score history
- [ ] Generate vendor performance trend analysis
- [ ] Compile exception register with approvals
- [ ] Export monitoring log for period
- [ ] Summarise incident history
- [ ] Gather sample monthly reports
- [ ] Prepare governance meeting minutes

---

## 14. Generator Script Reference

### 14.1 Script Location

```
10-isms-scr-base/
└── isms-a.8.30-outsourced-development/
    └── 10_generator-master/
        └── generate_a830_4_monitoring_dashboard.py
```

### 14.2 Script Execution

```bash
cd 10-isms-scr-base/isms-a.8.30-outsourced-development/10_generator-master
python3 generate_a830_4_monitoring_dashboard.py
mv *.xlsx ../90_workbooks/
```

### 14.3 Output

```
ISMS-IMP-A.8.30.4_Monitoring_Dashboard_YYYYMMDD.xlsx
```

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->

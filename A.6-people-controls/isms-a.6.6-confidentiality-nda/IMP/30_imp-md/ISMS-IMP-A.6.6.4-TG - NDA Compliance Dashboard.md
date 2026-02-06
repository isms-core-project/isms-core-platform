**ISMS-IMP-A.6.6.4-TG - NDA Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.6: Confidentiality or Non-Disclosure Agreements

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.4-TG |
| **Document Title** | NDA Compliance Dashboard Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.6.6: Confidentiality or Non-Disclosure Agreements |
| **Parent Policy** | ISMS-POL-A.6.6 (Confidentiality and Non-Disclosure Agreements) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

# Technical Specification

This section provides technical details for the NDA Compliance Dashboard workbook implementation.

---

## 9. Workbook Technical Structure

### 9.1 Workbook Properties

| Property | Value |
|----------|-------|
| File Format | .xlsx (Excel 2016+) |
| Sheet Protection | Structure protected, cells unlocked for input |
| Workbook Protection | Structure only |
| File Naming | ISMS-IMP-A.6.6.4_NDA_Compliance_Dashboard_YYYYMMDD.xlsx |

### 9.2 Sheet Configuration

| Sheet | Tab Colour | Protection Level | Hidden |
|-------|------------|------------------|--------|
| Instructions | Grey (#A6A6A6) | Full protection | No |
| Executive_Summary | Dark Blue (#002060) | Full (display only) | No |
| Coverage_Metrics | Green (#70AD47) | Input cells unlocked | No |
| Expiration_Status | Orange (#ED7D31) | Input cells unlocked | No |
| Compliance_Scorecard | Purple (#7030A0) | Input cells unlocked | No |
| KPI_Tracker | Blue (#4472C4) | Input cells unlocked | No |
| Trend_Analysis | Teal (#00B0F0) | Input cells unlocked | No |
| Approval_SignOff | Gold (#FFC000) | Input cells unlocked | No |
| Validation Lists | Grey (#A6A6A6) | Full protection | Yes |

---

## 10. Sheet Specifications

### 10.1 Sheet 2: Executive_Summary – Technical Specification

**Layout Configuration:**

| Section | Position | Content |
|---------|----------|---------|
| Header | Row 1-3 | Title, Report Period |
| KPI Boxes | Row 5-8 | 4 key metric boxes |
| Summary Table | Row 10-18 | Metric summary |
| Key Messages | Row 20-25 | Management messages |
| Footer | Row 27-28 | Prepared by, Date |

**KPI Box Structure:**

```
┌─────────────────┐
│ [METRIC NAME]   │
│ [VALUE] [TREND] │
│ Target: [TARGET]│
│ Status: [RAG]   │
└─────────────────┘
```

**Data Links:**

| Metric | Source Formula |
|--------|----------------|
| Overall Coverage | =Coverage_Metrics!$E$12 |
| Active NDAs | =COUNTIF(Source!Status,"Active") |
| Expiring 30 Days | =Expiration_Status!$B$3 |
| Open Gaps | =COUNTIF(Gap_Register!Status,"Open") |

### 10.2 Sheet 3: Coverage_Metrics – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Category | 25 | Text | Fixed | Yes |
| B | Sub_Category | 20 | Text | Fixed | Yes |
| C | Total_Population | 10 | Number | Integer >= 0 | Yes |
| D | NDA_Required | 10 | Number | Integer >= 0 | Yes |
| E | NDA_Signed | 10 | Number | Integer >= 0 | Yes |
| F | Coverage_Rate | 10 | Percentage | Calculated | Auto |
| G | Gap_Count | 10 | Number | Calculated | Auto |
| H | Expired_Count | 10 | Number | Integer >= 0 | Yes |
| I | Status | 12 | List | Green,Amber,Red | Auto |
| J | Action_Required | 40 | Text | If not Green | Conditional |
| K | Owner | 20 | Text | If action needed | Conditional |
| L | Target_Date | 15 | Date | DD.MM.YYYY | Conditional |

**Formulas:**

```excel
Coverage_Rate (F2):
=IF(D2=0,0,E2/D2)

Gap_Count (G2):
=MAX(0,D2-E2)

Status (I2):
=IF(F2>=1,"Green",IF(F2>=0.95,"Amber","Red"))
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Status = "Red" | Red fill |
| Status = "Amber" | Yellow fill |
| Status = "Green" | Green fill |

### 10.3 Sheet 4: Expiration_Status – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Expiration_Bucket | 20 | Text | Fixed buckets | Yes |
| B | Count | 10 | Number | Integer >= 0 | Yes |
| C | Percentage | 10 | Percentage | Calculated | Auto |
| D | Status | 12 | List | Green,Amber,Red | Auto |
| E | Priority | 12 | List | Immediate,Urgent,High,Medium,Low | Auto |

**Bucket Definitions (Row 2-8):**

```
Row 2: Expired (Red, Immediate)
Row 3: <30 Days (Red, Urgent)
Row 4: 30-60 Days (Amber, High)
Row 5: 60-90 Days (Amber, Medium)
Row 6: 90-180 Days (Green, Low)
Row 7: >180 Days (Green, Monitor)
Row 8: Perpetual (Green, N/A)
```

**Critical Expirations List (Row 12+):**

| Column | Header | Width | Data Type | Required |
|--------|--------|-------|-----------|----------|
| A | NDA_ID | 15 | Text | Yes |
| B | Counterparty | 30 | Text | Yes |
| C | Category | 20 | Text | Yes |
| D | Expiry_Date | 15 | Date | Yes |
| E | Days_Remaining | 10 | Number | Calculated |
| F | Owner | 20 | Text | Yes |
| G | Renewal_Status | 15 | List | Yes |

### 10.4 Sheet 5: Compliance_Scorecard – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Compliance_Area | 30 | Text | Fixed | Yes |
| B | Target | 10 | Percentage | Fixed | Yes |
| C | Actual | 10 | Percentage | Calculated | Yes |
| D | Score | 10 | Number | 0-100 | Calculated |
| E | Weight | 10 | Percentage | Fixed | Yes |
| F | Weighted_Score | 10 | Number | Calculated | Auto |
| G | Status | 12 | List | Green,Amber,Red | Auto |
| H | Trend | 10 | List | ↑,→,↓ | Yes |
| I | Notes | 40 | Text | Optional | No |

**Formulas:**

```excel
Score (D2):
=MIN(100,C2/B2*100)

Weighted_Score (F2):
=D2*E2

Overall_Score (F12):
=SUM(F2:F9)

Status (G2):
=IF(D2>=100,"Green",IF(D2>=90,"Amber","Red"))
```

### 10.5 Sheet 6: KPI_Tracker – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | KPI_ID | 10 | Text | Format: KPI-## | Yes |
| B | KPI_Name | 30 | Text | Name | Yes |
| C | Target | 12 | Text | Target value | Yes |
| D | Jan | 10 | Varies | By KPI | Yes |
| E | Feb | 10 | Varies | By KPI | Yes |
| F | Mar | 10 | Varies | By KPI | Yes |
| ... | ... | ... | ... | ... | ... |
| O | Dec | 10 | Varies | By KPI | Yes |
| P | YTD_Avg | 10 | Calculated | Average | Auto |
| Q | Trend | 10 | List | ↑,→,↓ | Calculated |
| R | Status | 12 | List | On Track,At Risk,Behind | Calculated |

### 10.6 Sheet 7: Trend_Analysis – Technical Specification

**Quarterly Data Table:**

| Column | Header | Width | Data Type | Required |
|--------|--------|-------|-----------|----------|
| A | Metric | 25 | Text | Yes |
| B | Q1 | 10 | Varies | Yes |
| C | Q2 | 10 | Varies | Yes |
| D | Q3 | 10 | Varies | Yes |
| E | Q4 | 10 | Varies | Yes |
| F | YoY_Change | 15 | Calculated | Auto |
| G | Trend | 10 | List | Auto |

**Year-Over-Year Table:**

| Column | Header | Width | Data Type | Required |
|--------|--------|-------|-----------|----------|
| A | Metric | 25 | Text | Yes |
| B | Prior_Year | 15 | Varies | Yes |
| C | Current_Year | 15 | Varies | Yes |
| D | Change | 15 | Calculated | Auto |
| E | Status | 12 | List | Auto |

---

## 11. Automation Requirements

### 11.1 Automated Alerts

| Trigger | Alert Type | Recipients | Timing |
|---------|------------|------------|--------|
| Coverage < 95% | Email | ISM, Category Owner | Daily |
| Expired NDA count > 0 | Email | ISM, CISO | Daily |
| Compliance Score < 80% | Email | ISM, CISO | Weekly |
| Dashboard update overdue | Email | ISM | 3 days after due |

### 11.2 Data Refresh Automation

| Data Element | Refresh Method | Frequency |
|--------------|----------------|-----------|
| Source workbook links | Manual refresh | Weekly |
| Coverage calculations | Auto-calculate | Real-time |
| Expiration counts | Manual update | Weekly |
| Compliance scores | Auto-calculate | Real-time |
| Trend data | Manual entry | Quarterly |

### 11.3 Report Generation

| Report | Format | Generation | Distribution |
|--------|--------|------------|--------------|
| Monthly Dashboard | PDF | Manual export | Email |
| Executive Summary | PowerPoint | Manual | Presentation |
| Quarterly Report | PDF | Manual | Management meeting |

---

## 12. Metrics and KPIs

### 12.1 Coverage KPIs

| KPI | Target | Threshold | Owner |
|-----|--------|-----------|-------|
| Overall Coverage | 100% | <95% critical | ISM |
| Employee Coverage | 100% | <98% warning | HR |
| Vendor Coverage | 100% | <90% critical | Procurement |
| New Joiner Completion | 100% | <95% warning | HR |

### 12.2 Compliance KPIs

| KPI | Target | Threshold | Owner |
|-----|--------|-----------|-------|
| Compliance Score | >90% | <80% critical | ISM |
| Expired NDA Count | 0 | >0 critical | ISM |
| Template Currency | 100% | <90% warning | Legal |
| Secure Storage | 100% | <95% warning | ISM |

### 12.3 Process KPIs

| KPI | Target | Threshold | Owner |
|-----|--------|-----------|-------|
| Renewal Rate | >95% | <90% warning | ISM |
| Gap Closure SLA | >95% | <90% warning | ISM |
| Review Completion | 100% | <90% warning | ISM |
| Dashboard Timeliness | 100% | Late = warning | ISM |

---

## 13. Evidence Package for ISO 27001 Audit

### 13.1 Standard Evidence Package

| Document | Purpose | Preparation |
|----------|---------|-------------|
| 12-month dashboard archive | Program monitoring evidence | Monthly PDF exports |
| Coverage trend analysis | Coverage management evidence | Sheet 7 export |
| Compliance score history | Compliance tracking | Sheet 5 history |
| KPI reports | Performance management | Sheet 6 export |
| Approval records | Governance evidence | Sheet 8 export |
| Executive presentations | Management engagement | Presentation archive |

### 13.2 Audit Preparation Checklist

- [ ] Archive current dashboard state
- [ ] Export 12-month trend data
- [ ] Compile KPI history
- [ ] Gather approval records
- [ ] Prepare coverage analysis summary
- [ ] Document methodology

---

## 14. Generator Script Reference

### 14.1 Script Location

```
10-isms-scr-base/
└── isms-a.6.6-confidentiality-nda/
    └── 10_generator-master/
        └── generate_a66_4_nda_dashboard.py
```

### 14.2 Script Execution

```bash
cd 10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master
python3 generate_a66_4_nda_dashboard.py
mv *.xlsx ../90_workbooks/
```

### 14.3 Output

```
ISMS-IMP-A.6.6.4_NDA_Compliance_Dashboard_YYYYMMDD.xlsx
```

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->

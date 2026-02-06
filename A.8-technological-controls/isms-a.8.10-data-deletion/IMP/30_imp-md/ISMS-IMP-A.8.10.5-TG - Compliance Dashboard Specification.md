**ISMS-IMP-A.8.10.5-TG - Compliance Dashboard Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.10.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Aggregate Deletion Compliance Metrics & Executive Dashboard |
| **Related Policy** | ISMS-POL-A.8.10 (Master Policy), ISMS-POL-A.8.10, Section 3.5 (Policy Governance) |
| **Purpose** | Provide executive visibility into A.8.10 compliance status by consolidating metrics from all four assessment workbooks into a single dashboard |
| **Target Audience** | Executives (CISO, CIO, CEO), Board of Directors, Audit Committee, Management, External Auditors, Compliance Officers, Regulators |
| **Assessment Type** | Reporting Dashboard & Trend Analysis (NOT data collection) |
| **Review Cycle** | Quarterly Updates (Minimum) or After Major Remediation Milestones |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Compliance Dashboard consolidation workbook | ISMS Implementation Team |

---

# Technical Specification
**Audience:** ISMS Implementation Teams, Python Developers, Excel Power Users

---

# Excel Workbook Structure

## Overview

**Workbook Name:** `ISMS_A_8_10_5_Compliance_Dashboard_YYYYMMDD.xlsx`

**Sheet Count:** 9 sheets total

**Design Philosophy:** REPORTING DASHBOARD (not data collection tool)

- Manual entry of summary metrics from source workbooks (no external file links)
- Heavy use of formulas for calculations and aggregations
- Visual indicators (RAG status, trend arrows) for executive consumption
- Quarterly snapshot capability (Q1-Q4 columns in Sheet 8)

## Sheet Organization

| Sheet # | Sheet Name | Purpose | Data Entry Type | Protected? |
|---------|------------|---------|-----------------|------------|
| 1 | Instructions & Data Mapping | User guidance and source cell references | N/A (read-only) | Yes |
| 2 | Overall A.8.10 Compliance | Highest-level summary (5 metrics) | Manual entry (5 cells) | Formulas protected |
| 3 | Retention Schedule Health | A.8.10.1 deep dive (8-10 metrics) | Manual entry (10 cells) | Formulas protected |
| 4 | Deletion Method Effectiveness | A.8.10.2 deep dive (10 metrics) | Manual entry (10 cells) | Formulas protected |
| 5 | Third-Party Deletion Performance | A.8.10.3 deep dive (8-10 metrics) | Manual entry (10 cells) | Formulas protected |
| 6 | Verification & Evidence Quality | A.8.10.4 deep dive (8-10 metrics) | Manual entry (10 cells) | Formulas protected |
| 7 | Critical Gaps Dashboard | Top 5 gaps from all assessments | Manual entry (15 cells) | No |
| 8 | Trend Analysis | Quarterly comparison Q1-Q4 | Manual entry (40 cells/quarter) | Formulas protected |
| 9 | Executive Summary & Approval | Narrative summary and sign-off | Manual entry (text + 3 approvals) | No |

**Total Manual Entry Cells:** ~100-120 cells (vs. 260+ cells in assessment workbooks)

**Total Formula Cells:** ~200-300 cells (calculations, aggregations, RAG status)

---

# Sheet 1: Instructions & Data Mapping

## Purpose
Provide comprehensive guidance on dashboard completion and exact source cell references for manual data entry.

## Content Sections

**Section 1: Dashboard Overview (Rows 1-15)**

- Document ID, Version, Date
- Dashboard purpose and scope
- Target audience (executives, board, auditors)
- Update frequency (quarterly)
- Manual entry workflow explanation

**Section 2: Data Source Mapping Table (Rows 17-80)**

This is the CRITICAL table that prevents manual entry errors. For each dashboard cell, document:

- Dashboard Sheet Name
- Dashboard Cell Reference
- Source Workbook Filename
- Source Sheet Name
- Source Cell Reference
- Metric Description
- Expected Data Type (%, count, score, text)

**Example Data Source Mapping Table:**

| Dashboard Sheet | Dashboard Cell | Source Workbook | Source Sheet | Source Cell | Metric Description | Data Type |
|-----------------|----------------|-----------------|--------------|-------------|-------------------|-----------|
| Sheet 2 (Overall) | B5 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B7 | Retention Schedule Coverage % | Percentage |
| Sheet 2 (Overall) | B6 | A.8.10.2_Deletion_Methods_[Date].xlsx | Sheet 7 (Dashboard) | B7 | NIST Compliance % | Percentage |
| Sheet 2 (Overall) | B7 | A.8.10.3_Third_Party_[Date].xlsx | Sheet 7 (Dashboard) | B7 | Vendor SLA Compliance % | Percentage |
| Sheet 2 (Overall) | B8 | A.8.10.4_Verification_[Date].xlsx | Sheet 7 (Dashboard) | B18 | Audit Readiness Score | Text |
| Sheet 3 (Retention) | B5 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B5 | Total Data Categories | Count |
| Sheet 3 (Retention) | B6 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B6 | Categories with Schedules | Count |
| Sheet 3 (Retention) | B8 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B8 | Overdue Reviews Count | Count |
| Sheet 3 (Retention) | B12 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B12 | Avg DSR Response Time (days) | Number |
| Sheet 4 (Methods) | B5 | A.8.10.2_Deletion_Methods_[Date].xlsx | Sheet 7 (Dashboard) | B5 | Total Deletion Methods | Count |
| Sheet 4 (Methods) | B6 | A.8.10.2_Deletion_Methods_[Date].xlsx | Sheet 7 (Dashboard) | B6 | NIST-Compliant Methods | Count |
| Sheet 4 (Methods) | B8 | A.8.10.2_Deletion_Methods_[Date].xlsx | Sheet 7 (Dashboard) | B8 | Forensic Test Pass Rate % | Percentage |
| Sheet 5 (Third-Party) | B5 | A.8.10.3_Third_Party_[Date].xlsx | Sheet 7 (Dashboard) | B5 | Total Vendors with Data | Count |
| Sheet 5 (Third-Party) | B8 | A.8.10.3_Third_Party_[Date].xlsx | Sheet 7 (Dashboard) | B8 | Shadow IT Tier 9/10 Count | Count |
| Sheet 6 (Verification) | B5 | A.8.10.4_Verification_[Date].xlsx | Sheet 7 (Dashboard) | B5 | Deletion Logging Maturity | Score 1-5 |
| Sheet 6 (Verification) | B11 | A.8.10.4_Verification_[Date].xlsx | Sheet 7 (Dashboard) | B11 | Certificate Quality Avg | Score 1-5 |

**Section 3: Maturity Scoring Model (Rows 82-110)**

Explanation of how Overall A.8.10 Maturity Score is calculated:
```
Overall Score = (Retention Health × 25%) 

              + (Deletion Effectiveness × 25%) 
              + (Third-Party Performance × 25%) 
              + (Verification Quality × 25%)

Where:
  Retention Health = Based on A.8.10.1 metrics (coverage, DSR, legal basis)
  Deletion Effectiveness = Based on A.8.10.2 metrics (NIST, testing, SSD)
  Third-Party Performance = Based on A.8.10.3 metrics (SLA, Shadow IT, DPA)
  Verification Quality = Based on A.8.10.4 metrics (audit readiness, certificates, logs)
```

**Section 4: RAG Status Color Coding (Rows 112-125)**

| Color | Threshold | Meaning | Action |
|-------|-----------|---------|--------|
| **Green** | ≥90% / Score ≥80 / "Fully Ready" | Low risk, compliant | Maintain current controls |
| **Amber** | 70-89% / Score 60-79 / "Mostly Ready" | Moderate risk, gaps exist | Monitor and plan improvements |
| **Red** | <70% / Score <60 / "Partially/Not Ready" | High risk, non-compliant | Immediate remediation required |

**Section 5: Quarterly Update Workflow (Rows 127-145)**

Step-by-step guide to quarterly dashboard updates:
1. Ensure all 4 source assessments (A.8.10.1-4) completed and approved
2. Open this dashboard workbook
3. Open Data Source Mapping Table (Section 2)
4. For each row in mapping table:

   - Open source workbook specified
   - Navigate to source sheet specified
   - Copy value from source cell specified
   - Paste into dashboard cell specified

5. Validate formulas calculate correctly (no errors)
6. Complete Sheet 7 (Critical Gaps) - manual entry
7. Complete Sheet 8 (Trend Analysis) - manual entry + formulas
8. Complete Sheet 9 (Executive Summary) - narrative text
9. Three-level approval workflow
10. Archive completed dashboard

## Formatting

- Mapping table: Alternating row colors, borders, wrapped text
- Manual entry cells: Yellow fill (same as assessment workbooks)
- Formula cells: Light blue fill, locked
- Source cell references: Monospace font for clarity

---

# Sheet 2: Overall A.8.10 Compliance

## Purpose
Provide the 30-second executive summary - highest-level compliance status across all 4 assessment areas.

## Layout Structure

**Section 1: Summary Metrics (Rows 3-12, Columns A-F)**

| Row | Column A (Metric) | Column B (Value) | Column C (Target) | Column D (Status) | Column E (Trend) | Column F (Notes) |
|-----|-------------------|------------------|-------------------|-------------------|------------------|------------------|
| 5 | Overall A.8.10 Maturity Score | =Formula | ≥80/100 | =RAG Formula | =Trend Formula | Auto-text |
| 6 | Retention Schedule Coverage | [Manual] | 100% | =RAG Formula | =Trend Formula | From A.8.10.1 |
| 7 | Deletion Method NIST Compliance | [Manual] | 100% | =RAG Formula | =Trend Formula | From A.8.10.2 |
| 8 | Vendor SLA Compliance | [Manual] | ≥95% | =RAG Formula | =Trend Formula | From A.8.10.3 |
| 9 | Audit Readiness Score | [Manual] | Fully Ready | =RAG Formula | =Trend Formula | From A.8.10.4 |

**Column B Formula Examples:**

**Row 5 (Overall Maturity Score):**
```excel
=ROUND(
  ('Retention Health'!B20 * 0.25) +
  ('Deletion Effectiveness'!B20 * 0.25) +
  ('Third-Party Performance'!B20 * 0.25) +
  ('Verification Quality'!B20 * 0.25),
  0
)
```
*Note: B20 in each sheet contains that area's component score (0-100)*

**Column D (RAG Status) Formulas:**

**For Percentages (Rows 6-8):**
```excel
=IF(B6>=90,"Green",IF(B6>=70,"Amber","Red"))
```

**For Scores (Row 5):**
```excel
=IF(B5>=80,"Green",IF(B5>=60,"Amber","Red"))
```

**For Text Values (Row 9 - Audit Readiness):**
```excel
=IF(B9="Fully Ready","Green",IF(B9="Mostly Ready","Amber","Red"))
```

**Column E (Trend) Formulas:**

*Compares current value (Column B) vs. previous quarter value (Sheet 8 Trend Analysis)*
```excel
=IF(ISBLANK('Trend Analysis'!B5),"→",
   IF(B5>='Trend Analysis'!B5*1.05,"↑",
      IF(B5<='Trend Analysis'!B5*0.95,"↓","→")))
```

**Section 2: Critical Gaps Summary (Rows 14-22, Columns A-E)**

| Row | Column A (Area) | Column B (Critical Gaps Count) | Column C (Highest Priority Gap) | Column D (Target Date) |
|-----|-----------------|-------------------------------|--------------------------------|----------------------|
| 16 | A.8.10.1 Retention | =Formula | [Manual from Sheet 7] | [Manual] |
| 17 | A.8.10.2 Methods | =Formula | [Manual from Sheet 7] | [Manual] |
| 18 | A.8.10.3 Third-Party | =Formula | [Manual from Sheet 7] | [Manual] |
| 19 | A.8.10.4 Verification | =Formula | [Manual from Sheet 7] | [Manual] |

**Column B Formula (Critical Gaps Count):**
```excel
='Critical Gaps'!B5
```
*Where Critical Gaps Sheet B5 = count of A.8.10.1 critical gaps*

**Section 3: Compliance Readiness by Standard (Rows 24-31, Columns A-D)**

| Row | Column A (Standard) | Column B (Compliance Status) | Column C (Evidence Gaps) | Column D (Next Action) |
|-----|-------------------|----------------------------|------------------------|----------------------|
| 26 | ISO 27001:2022 A.8.10 | =Formula | =Formula | [Manual] |
| 27 | GDPR Article 17 | =Formula | =Formula | [Manual] |
| 28 | FADP Article 6 | =Formula | =Formula | [Manual] |
| 29 | NIST SP 800-88 | =Formula | =Formula | [Manual] |

**Column B Formula (Compliance Status):**
```excel
=IF(B5>=90,"Fully Compliant",
   IF(B5>=70,"Substantially Compliant",
      IF(B5>=50,"Partially Compliant","Non-Compliant")))
```

**Column C Formula (Evidence Gaps Count):**
```excel
=SUMIF('Critical Gaps'!C5:C9,"Evidence*")
```
*Counts gaps in Critical Gaps sheet where gap description contains "Evidence"*

## Conditional Formatting

**Column D (Status) - Text Color Based on Value:**

- Green text for cells containing "Green"
- Orange text for cells containing "Amber"
- Red bold text for cells containing "Red"

**Column E (Trend) - Icon Sets:**

- Green up arrow (↑) for "↑"
- Orange right arrow (→) for "→"
- Red down arrow (↓) for "↓"

**Row 5 (Overall Maturity Score) - Cell Fill:**

- Green fill if B5 ≥ 80
- Orange fill if B5 60-79
- Red fill if B5 < 60

---

# Sheet 3: Retention Schedule Health

## Purpose
Deep dive into retention schedule coverage and data subject rights performance from A.8.10.1 assessment.

## Layout Structure

**Section 1: Retention Schedule Coverage Metrics (Rows 3-13, Columns A-E)**

| Row | Column A (Metric) | Column B (Current Value) | Column C (Target) | Column D (Status) | Column E (Notes) |
|-----|-------------------|------------------------|-------------------|-------------------|------------------|
| 5 | Total Data Categories Identified | [Manual from A.8.10.1] | Baseline | Info | [Auto] |
| 6 | Categories with Retention Schedules | [Manual from A.8.10.1] | 100% | =RAG | [Auto] |
| 7 | Retention Schedule Coverage % | =B6/B5*100 | 100% | =RAG | Calculated |
| 8 | Overdue Schedule Reviews | [Manual from A.8.10.1] | 0 | =RAG | [Auto] |
| 9 | Schedules Aligned with FADP | [Manual from A.8.10.1] | All | =RAG | [Auto] |
| 10 | Schedules Aligned with GDPR | [Manual from A.8.10.1] | All | =RAG | [Auto] |
| 11 | Avg Schedule Review Age (months) | [Manual from A.8.10.1] | <12 | =RAG | [Auto] |
| 12 | Categories Without Legal Basis | [Manual from A.8.10.1] | 0 | =RAG | [Auto] |

**Row 7 Formula (Retention Coverage %):**
```excel
=IF(B5=0,0,ROUND(B6/B5*100,1))
```

**Column D (Status) Formulas:**

**Row 7 (Coverage %):**
```excel
=IF(B7=100,"Green",IF(B7>=95,"Amber","Red"))
```

**Row 8 (Overdue Reviews):**
```excel
=IF(B8=0,"Green",IF(B8<=5,"Amber","Red"))
```

**Row 11 (Review Age):**
```excel
=IF(B11<12,"Green",IF(B11<18,"Amber","Red"))
```

**Row 12 (No Legal Basis):**
```excel
=IF(B12=0,"Green",IF(B12<=3,"Amber","Red"))
```

**Section 2: GDPR DSR Response Performance (Rows 15-20, Columns A-E)**

| Row | Column A (Metric) | Column B (Performance) | Column C (GDPR Requirement) | Column D (Status) |
|-----|-------------------|----------------------|---------------------------|-------------------|
| 17 | Average DSR Response Time (days) | [Manual from A.8.10.1] | <30 days | =RAG |
| 18 | DSR Requests Completed On Time % | [Manual from A.8.10.1] | 100% | =RAG |
| 19 | DSR Backlog Count | [Manual from A.8.10.1] | 0 | =RAG |

**Column D Formulas:**

**Row 17 (DSR Response Time):**
```excel
=IF(B17<20,"Green",IF(B17<30,"Amber","Red"))
```

**Row 18 (On Time %):**
```excel
=IF(B18=100,"Green",IF(B18>=90,"Amber","Red"))
```

**Row 19 (Backlog):**
```excel
=IF(B19=0,"Green",IF(B19<=3,"Amber","Red"))
```

**Section 3: Component Score Calculation (Row 20, Column B)**

*This feeds into Sheet 2 Overall Maturity Score*

**Formula:**
```excel
=ROUND(
  (B7*0.4) +                    /* Retention Coverage 40% weight */
  ((30-MIN(B17,30))/30*100*0.3) + /* DSR Response 30% weight (inverse - lower is better) */
  ((B5-B12)/B5*100*0.3),           /* Legal Basis 30% weight */
  0
)
```

**Section 4: Reference - Retention Compliance Benchmarks (Rows 22-28, Table)**

| Benchmark | Value | Source |
|-----------|-------|--------|
| Industry Average Retention Coverage | 85% | ISO 27001 Survey 2024 |
| Regulatory Minimum (GDPR) | 100% | Article 5.1(e) Storage Limitation |
| Best Practice Target | 100% | NIST SP 800-88 R1 |
| GDPR DSR Response Deadline | 30 days | Article 17 |
| Swiss OR Business Records Retention | 7 years | Article 958f |

---

# Sheet 4: Deletion Method Effectiveness

## Purpose
Evaluate deletion method compliance and effectiveness from A.8.10.2 assessment.

## Layout Structure

**Section 1: NIST SP 800-88 Compliance Metrics (Rows 3-17, Columns A-E)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 5 | Total Deletion Methods in Use | [Manual from A.8.10.2] | Documented | Info |
| 6 | NIST-Compliant Methods Count | [Manual from A.8.10.2] | 100% of total | =RAG |
| 7 | NIST Compliance % | =B6/B5*100 | 100% | =RAG |
| 8 | Forensic Test Pass Rate % | [Manual from A.8.10.2] | ≥95% | =RAG |
| 9 | Methods Tested vs. Untested | [Manual] / [Manual] | All tested | =RAG |
| 10 | Clear Methods % | [Manual from A.8.10.2] | Per classification | Info |
| 11 | Purge Methods % | [Manual from A.8.10.2] | Per classification | Info |
| 12 | Destroy Methods % | [Manual from A.8.10.2] | Per classification | Info |
| 13 | NIST Category Sum Check | =B10+B11+B12 | 100% | Validation |
| 14 | SSD-Specific Issues Count | [Manual from A.8.10.2] | 0 | =RAG |
| 15 | Crypto-Erasure Implemented | [Manual from A.8.10.2] | Yes/No | Info |

**Row 7 Formula:**
```excel
=IF(B5=0,0,ROUND(B6/B5*100,1))
```

**Row 13 Formula (Validation):**
```excel
=IF(ABS(B10+B11+B12-100)<0.1,"✓ Valid","⚠ Check percentages")
```

**Column D Formulas:**

**Row 7 (NIST Compliance):**
```excel
=IF(B7=100,"Green",IF(B7>=90,"Amber","Red"))
```

**Row 8 (Test Pass Rate):**
```excel
=IF(B8>=95,"Green",IF(B8>=80,"Amber","Red"))
```

**Row 14 (SSD Issues):**
```excel
=IF(B14=0,"Green",IF(B14<=3,"Amber","Red"))
```

**Section 2: Deletion Method Testing Coverage (Rows 19-25)**

| Row | Column A (Metric) | Column B (Count) | Column C (Target) | Column D (Status) |
|-----|-------------------|------------------|-------------------|-------------------|
| 21 | Methods with Annual Testing | [Manual] | All methods | =RAG |
| 22 | Methods Tested in Last 12 Months | [Manual] | 100% | =RAG |
| 23 | Methods Never Tested | =B5-B22 | 0 | =RAG |
| 24 | Test Failures Requiring Remediation | [Manual] | 0 | =RAG |

**Section 3: Component Score Calculation (Row 20, Column B)**
```excel
=ROUND(
  (B7*0.5) +          /* NIST Compliance 50% */
  (B8*0.3) +          /* Test Pass Rate 30% */
  ((B5-B14)/B5*100*0.2), /* SSD Issues 20% (inverse) */
  0
)
```

**Section 4: Reference - NIST Media Categories (Rows 27-35, Table)**

| Media Type | Clear | Purge | Destroy |
|------------|-------|-------|---------|
| HDD (magnetic) | 1-pass overwrite | 3-pass overwrite | Degauss or shred |
| SSD (flash) | TRIM/Secure Erase | Crypto Erase | Physical destruction |
| Cloud/VM | API delete | Crypto Erase | N/A (provider-managed) |
| Paper | Shred (strip) | Cross-cut shred | Pulverize/incinerate |
| Optical (CD/DVD) | Not possible | Not possible | Physical destruction |

---

# Sheet 5: Third-Party Deletion Performance

## Purpose
Monitor vendor compliance with deletion SLAs and identify Shadow IT exposure from A.8.10.3 assessment.

## Layout Structure

**Section 1: Vendor Deletion Management Metrics (Rows 3-15, Columns A-E)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 5 | Total Vendors with Data | [Manual from A.8.10.3] | Documented | Info |
| 6 | Vendors with Deletion SLAs | [Manual from A.8.10.3] | 100% | =RAG |
| 7 | Vendor SLA Coverage % | =B6/B5*100 | 100% | =RAG |
| 8 | Vendor SLA Compliance % | [Manual from A.8.10.3] | ≥95% | =RAG |
| 9 | Vendors Breaching SLAs | [Manual from A.8.10.3] | 0 | =RAG |
| 10 | DPA Coverage % | [Manual from A.8.10.3] | 100% | =RAG |
| 11 | Strong Deletion Clauses % | [Manual from A.8.10.3] | ≥80% | =RAG |
| 12 | Certificate Quality Score (Avg) | [Manual from A.8.10.3] | ≥4.0 | =RAG |

**Section 2: Shadow IT Exposure (Rows 17-23)**

| Row | Column A (Metric) | Column B (Count) | Column C (Target) | Column D (Status) |
|-----|-------------------|------------------|-------------------|-------------------|
| 19 | Total Shadow IT Instances | [Manual from A.8.10.3] | Documented | Info |
| 20 | Shadow IT Tier 9/10 (High Risk) | [Manual from A.8.10.3] | 0 | =RAG |
| 21 | Shadow IT with Sensitive Data | [Manual from A.8.10.3] | 0 | =RAG |
| 22 | Shadow IT Remediation in Progress | [Manual from A.8.10.3] | All high-risk | Info |

**Column D Formulas:**

**Row 7 (SLA Coverage):**
```excel
=IF(B7=100,"Green",IF(B7>=90,"Amber","Red"))
```

**Row 8 (SLA Compliance):**
```excel
=IF(B8>=95,"Green",IF(B8>=85,"Amber","Red"))
```

**Row 10 (DPA Coverage):**
```excel
=IF(B10=100,"Green",IF(B10>=90,"Amber","Red"))
```

**Row 11 (Strong Clauses):**
```excel
=IF(B11>=80,"Green",IF(B11>=60,"Amber","Red"))
```

**Row 12 (Certificate Quality):**
```excel
=IF(B12>=4,"Green",IF(B12>=3,"Amber","Red"))
```

**Row 20 (Shadow IT Tier 9/10):**
```excel
=IF(B20=0,"Green",IF(B20<=3,"Amber","Red"))
```

**Section 3: Component Score Calculation (Row 20, Column B)**
```excel
=ROUND(
  (B8*0.4) +              /* SLA Compliance 40% */
  ((B5-B20)/B5*100*0.3) + /* Shadow IT 30% (inverse) */
  (B10*0.3),              /* DPA Coverage 30% */
  0
)
```

**Section 4: Reference - Cloud Provider Deletion SLAs (Rows 25-32, Table)**

| Provider | Standard Deletion SLA | Verification Method | Certificate Provided |
|----------|---------------------|-------------------|-------------------|
| AWS | 30 days after termination | API logs, support ticket | On request |
| Azure | 90 days after termination | Compliance Manager | On request |
| Google Cloud | 30 days after deletion request | Admin Console logs | On request |
| Salesforce | Immediate + 90-day recycle bin | Data Export API | On request |
| Microsoft 365 | 30 days after deletion | Admin Center logs | On request |

---

# Sheet 6: Verification & Evidence Quality

## Purpose
Assess audit readiness and evidence quality for proving deletion occurred (from A.8.10.4 assessment).

## Layout Structure

**Section 1: Verification Infrastructure Metrics (Rows 3-15, Columns A-E)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 5 | Deletion Logging Maturity (1-5) | [Manual from A.8.10.4] | ≥4.0 | =RAG |
| 6 | Log Completeness Score (%) | [Manual from A.8.10.4] | ≥80% | =RAG |
| 7 | Log Retention Period (years) | [Manual from A.8.10.4] | ≥7 years | =RAG |
| 8 | Centralized Logging Implemented | [Manual from A.8.10.4] | Yes/No | =RAG |
| 9 | Tamper Protection Implemented | [Manual from A.8.10.4] | Advanced/Immutable | =RAG |

**Section 2: Forensic Testing & Verification (Rows 17-23)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 19 | Forensic Testing Program Exists | [Manual from A.8.10.4] | Yes/No | =RAG |
| 20 | Testing Frequency | [Manual from A.8.10.4] | Annual minimum | =RAG |
| 21 | Test Pass Rate (%) | [Manual from A.8.10.4] | ≥95% | =RAG |
| 22 | Methods Tested vs. Total | [Manual] / [Manual] | 100% | =RAG |

**Section 3: Evidence Repository & Audit Readiness (Rows 25-32)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 27 | Evidence Repository Security (1-5) | [Manual from A.8.10.4] | ≥4.0 | =RAG |
| 28 | Evidence Retention Compliance | [Manual from A.8.10.4] | 100% | =RAG |
| 29 | Certificate Quality Average (1-5) | [Manual from A.8.10.4] | ≥4.0 | =RAG |
| 30 | Audit Trail Completeness (%) | [Manual from A.8.10.4] | 100% | =RAG |
| 31 | Audit Trail Reconstruction Time (hrs) | [Manual from A.8.10.4] | <2 hours | =RAG |
| 32 | Audit Readiness Status | [Manual from A.8.10.4] | Fully Ready | =RAG |

**Column D Formulas:**

**Row 5, 27, 29 (1-5 Scores):**
```excel
=IF(B5>=4,"Green",IF(B5>=3,"Amber","Red"))
```

**Row 6, 30 (Percentages):**
```excel
=IF(B6>=90,"Green",IF(B6>=70,"Amber","Red"))
```

**Row 7 (Retention Years):**
```excel
=IF(B7>=7,"Green",IF(B7>=3,"Amber","Red"))
```

**Row 8 (Yes/No - Centralized):**
```excel
=IF(B8="Yes","Green",IF(B8="Partial","Amber","Red"))
```

**Row 9 (Tamper Protection):**
```excel
=IF(OR(B9="Advanced",B9="Immutable"),"Green",IF(B9="Basic","Amber","Red"))
```

**Row 19 (Testing Program Exists):**
```excel
=IF(B19="Yes","Green","Red")
```

**Row 31 (Reconstruction Time):**
```excel
=IF(B31<1,"Green",IF(B31<4,"Amber","Red"))
```

**Row 32 (Audit Readiness):**
```excel
=IF(B32="Fully Ready","Green",IF(B32="Mostly Ready","Amber","Red"))
```

**Section 4: Component Score Calculation (Row 20, Column B)**
```excel
=ROUND(
  (IF(B32="Fully Ready",100,IF(B32="Mostly Ready",75,IF(B32="Partially Ready",50,25)))*0.4) + /* Audit Readiness 40% */
  (B29*20*0.3) +  /* Certificate Quality 30% (convert 1-5 to 0-100) */
  (B30*0.3),      /* Audit Trail Completeness 30% */
  0
)
```

---

# Sheet 7: Critical Gaps Dashboard

## Purpose
Highlight top 5 gaps requiring immediate management attention from all four assessments.

## Layout Structure

**Critical Gaps Summary Table (Rows 3-12, Columns A-F)**

| Row | Column A (Priority) | Column B (Gap Description) | Column C (Source Assessment) | Column D (Risk Level) | Column E (Responsible Party) | Column F (Target Date) |
|-----|-------------------|--------------------------|---------------------------|--------------------|----------------------------|---------------------|
| 5 | 1 (Highest) | [Manual entry] | Dropdown: A.8.10.1/2/3/4 | Dropdown: Critical/High | [Manual] | [Date] |
| 6 | 2 | [Manual entry] | Dropdown | Dropdown | [Manual] | [Date] |
| 7 | 3 | [Manual entry] | Dropdown | Dropdown | [Manual] | [Date] |
| 8 | 4 | [Manual entry] | Dropdown | Dropdown | [Manual] | [Date] |
| 9 | 5 (Lowest) | [Manual entry] | Dropdown | Dropdown | [Manual] | [Date] |

**Column C Dropdown Values:**

- A.8.10.1 - Retention & Deletion Triggers
- A.8.10.2 - Deletion Methods
- A.8.10.3 - Third-Party & Cloud Deletion
- A.8.10.4 - Verification & Evidence

**Column D Dropdown Values:**

- Critical (Regulatory violation risk)
- High (Operational risk, audit failure)
- Medium (Efficiency gap)

**Section 2: Gap Statistics by Assessment Area (Rows 14-22, Formulas)**

| Row | Column A (Assessment) | Column B (Critical Gaps) | Column C (High Gaps) | Column D (Total) |
|-----|---------------------|------------------------|-------------------|----------------|
| 16 | A.8.10.1 Retention | =COUNTIF(C5:C9,"A.8.10.1*") | [Manual if needed] | =B16+C16 |
| 17 | A.8.10.2 Methods | =COUNTIF(C5:C9,"A.8.10.2*") | [Manual] | =B17+C17 |
| 18 | A.8.10.3 Third-Party | =COUNTIF(C5:C9,"A.8.10.3*") | [Manual] | =B18+C18 |
| 19 | A.8.10.4 Verification | =COUNTIF(C5:C9,"A.8.10.4*") | [Manual] | =B19+C19 |
| 20 | **TOTAL** | =SUM(B16:B19) | =SUM(C16:C19) | =SUM(D16:D19) |

## Conditional Formatting

**Column D (Risk Level):**

- Red bold text for "Critical"
- Orange text for "High"

**Column F (Target Date):**

- Red fill if date < TODAY() (overdue)
- Orange fill if date < TODAY()+30 (due within 30 days)
- Green fill if date >= TODAY()+30

---

# Sheet 8: Trend Analysis

## Purpose
Show quarterly progress or decline to identify systemic issues requiring management attention.

## Layout Structure

**Quarterly Metrics Tracking (Rows 3-50, Columns A-F)**

**Column Structure:**

- Column A: Metric Name
- Column B: Q1 Value (Baseline)
- Column C: Q2 Value
- Column D: Q3 Value
- Column E: Q4 Value
- Column F: Trend Explanation

**Key Metrics Tracked (40 total):**

**From Sheet 2 (Overall):**
1. Overall A.8.10 Maturity Score
2. Retention Coverage %
3. NIST Compliance %
4. Vendor SLA Compliance %
5. Audit Readiness Score

**From Sheet 3 (Retention):**
6. Total Data Categories
7. Categories with Schedules
8. Overdue Reviews Count
9. Avg DSR Response Time (days)
10. DSR On-Time %

**From Sheet 4 (Methods):**
11. Total Deletion Methods
12. NIST-Compliant Methods
13. Forensic Test Pass Rate %
14. SSD Issues Count
15. Clear/Purge/Destroy Distribution

**From Sheet 5 (Third-Party):**
16. Total Vendors
17. Vendors with SLAs
18. SLA Compliance %
19. Shadow IT Count (Tier 9/10)
20. DPA Coverage %

**From Sheet 6 (Verification):**
21. Logging Maturity Score
22. Log Completeness %
23. Forensic Testing Exists
24. Certificate Quality Avg
25. Audit Readiness Status

## Trend Calculation Formulas

**For each metric row, add a calculated column G (Trend Arrow):**

**Formula (assuming metric in row 5):**
```excel
=IF(ISBLANK(B5),"N/A",
   IF(ISBLANK(C5),"→",
      IF(C5>=B5*1.05,"↑ +"&TEXT((C5-B5)/B5,"0%"),
         IF(C5<=B5*0.95,"↓ "&TEXT((C5-B5)/B5,"0%"),"→ "&TEXT((C5-B5)/B5,"0%")))))
```

*This shows both arrow and percentage change*

**Column F (Trend Explanation) - Manual Entry Examples:**

| Metric | Q1 | Q2 | Trend | Explanation |
|--------|----|----|-------|-------------|
| Retention Coverage % | 85% | 100% | ↑ +18% | Completed retention schedule project for 15 remaining data categories (Mar-Apr 2024) |
| Shadow IT Count | 12 | 5 | ↑ -58% | Formalized 4 instances with DPAs, decommissioned 3 unauthorized systems |
| Forensic Test Pass Rate | 88% | 95% | ↑ +8% | Replaced HDD overwrite on SSDs with crypto-erase (7 systems) |
| Vendor SLA Compliance | 92% | 87% | ↓ -5% | AWS delayed deletion by 15 days (incident #INC-2024-045), escalated to account manager |

## Conditional Formatting

**Columns B-E (Quarterly Values):**

- Green fill if value improves vs. previous quarter (for metrics where higher is better)
- Red fill if value declines >5% vs. previous quarter
- Yellow fill if value stable (±5%)

**Column G (Trend Arrows):**

- Green text for ↑
- Red text for ↓
- Gray text for →

---

# Sheet 9: Executive Summary & Approval

## Purpose
Provide narrative summary for board presentation and capture three-level approval.

## Section 1: Executive Summary Narrative (Rows 3-40, Merged Cells)

**Structure (Text Entry Field, ~500-750 words):**
```
EXECUTIVE SUMMARY - [Quarter] [Year] A.8.10 COMPLIANCE DASHBOARD

[Organization]: [Organization Name]
Reporting Period: [Q1/Q2/Q3/Q4] [Year]
Prepared by: [Name, Title]
Date: [DD.MM.YYYY]

---

OVERALL STATUS:
[2-3 sentences: Maturity score, overall compliance status, trend vs. previous quarter]

KEY ACHIEVEMENTS:

- [Achievement 1 - quantified improvement]
- [Achievement 2 - milestone completed]
- [Achievement 3 - positive metric change]
- [Achievement 4 - regulatory compliance milestone]

KEY CONCERNS REQUIRING BOARD ATTENTION:

- [Concern 1 - critical gap with regulatory risk quantification]
- [Concern 2 - declining metric with impact analysis]
- [Concern 3 - resource constraint impeding progress]

NEXT QUARTER PRIORITIES:

- [Priority 1 - remediation initiative with timeline]
- [Priority 2 - resource requirement with budget]
- [Priority 3 - expected improvement target]

BOARD ACTION REQUESTED:

- [Action 1 - budget approval / resource allocation]
- [Action 2 - policy decision / strategic direction]
- [Action 3 - escalation support / vendor management]

---

DETAILED METRICS SUMMARY:
[Reference to Sheets 2-6 for detailed breakdowns]

REGULATORY COMPLIANCE STATUS:

- ISO 27001:2022 A.8.10: [Fully/Substantially/Partially Compliant]
- GDPR Article 17: [Compliant/Non-Compliant + evidence]
- Swiss FADP Article 6: [Compliant/Non-Compliant + evidence]

AUDIT READINESS:
[Organization] can demonstrate A.8.10 compliance to external auditors within [X] hours
with [complete/partial] evidence. [Gaps if any].

---

Prepared by: [Compliance Officer Name]
Reviewed by: [CISO Name]
Approved by: [Executive Sponsor Name]
```

**Formatting:**

- Font: Arial 11pt
- Line spacing: 1.5
- Bold headers for sections
- Bullet points for lists
- Merged cells for easy reading

## Section 2: Three-Level Approval (Rows 42-52, Table)

| Row | Column A (Level) | Column B (Role) | Column C (Name) | Column D (Signature) | Column E (Date) | Column F (Comments) |
|-----|------------------|----------------|----------------|---------------------|----------------|-------------------|
| 44 | Level 1 | Compliance Officer / Preparer | [Manual] | [Manual/Digital] | =TODAY() | [Manual] |
| 45 | Level 2 | Information Security Officer / CISO | [Manual] | [Manual/Digital] | [Manual] | [Manual] |
| 46 | Level 3 | Executive Sponsor / Audit Committee | [Manual] | [Manual/Digital] | [Manual] | [Manual] |

**Column E (Date) Validation:**

- Must be chronological: Level 2 date >= Level 1 date, Level 3 date >= Level 2 date
- Cannot be future dated
- Warning if >30 days between levels (delays)

## Section 3: Board Presentation Export (Rows 54-58)

**Instructions for exporting to PowerPoint:**

1. Copy Executive Summary (Rows 3-40)
2. Paste into PowerPoint slide (Blank layout)
3. Add charts/visuals from Sheets 2-6 if desired
4. Include data source reference: "Source: ISMS A.8.10 Compliance Dashboard Q[X] 2024"
5. Archive PDF of completed dashboard with board presentation materials

---

# Conditional Formatting Summary

## Global Rules (All Dashboard Sheets)

**RAG Status Cells (Column D in Sheets 2-6):**

- Green text + light green fill for "Green"
- Orange text + light orange fill for "Amber"
- Red bold text + light red fill for "Red"

**Percentage Metrics (Various cells):**

- Green fill if ≥90%
- Yellow fill if 70-89%
- Red fill if <70%

**Score Metrics (1-5 scale):**

- Green fill if ≥4.0
- Yellow fill if 3.0-3.9
- Red fill if <3.0

**Count Metrics (Gap counts, Shadow IT counts):**

- Green fill if 0
- Yellow fill if 1-5
- Red fill if >5

## Sheet-Specific Rules

**Sheet 2 (Overall Compliance):**

- Overall Maturity Score cell (B5): Large font (20pt), bold, colored fill based on RAG

**Sheet 7 (Critical Gaps):**

- Target Date column: Red fill if overdue, orange if <30 days, green if >30 days

**Sheet 8 (Trend Analysis):**

- Trend arrow cells: Icon sets (up/right/down arrows with colors)
- Quarterly value cells: Color scale (green = improvement, red = decline)

---

# Python Script Integration Notes

## Script: `generate_a810_5_compliance_dashboard.py`

**CRITICAL DIFFERENCE from A.8.10.1-4 Scripts:**

This workbook is a **DASHBOARD**, not an assessment workbook. Key differences:

1. **Fewer Data Entry Cells:** ~100-120 manual entry cells (vs. 260+ in assessments)
2. **More Formula Cells:** ~200-300 formulas for calculations, aggregations, RAG status
3. **No External File Links:** All data entry is manual (no `=VLOOKUP('[OtherFile.xlsx]Sheet'!A1)`)
4. **Quarterly Snapshot Structure:** Sheet 8 has Q1-Q4 columns (not just current state)

**Key Customization Areas for A.8.10.5:**

**1. Data Source Mapping Table (Sheet 1):**

- **DO NOT** hardcode source cell references in formulas
- **DO** create reference table showing manual entry instructions
- Table structure (in Sheet 1, Rows 17-80):

```
  Dashboard Sheet | Dashboard Cell | Source Workbook | Source Sheet | Source Cell | Metric | Data Type
```

**2. Manual Entry Cells (Yellow Fill):**

- Sheets 2-6: ~40-60 cells total (not 260+ like assessments)
- All cells UNPROTECTED (allow user entry)
- Data validation where applicable (percentages 0-100, scores 1-5)

**3. Formula Cells (Light Blue Fill, Protected):**

- RAG status formulas (IF statements based on thresholds)
- Aggregation formulas (AVERAGE, SUM, COUNTIF)
- Trend calculation formulas (comparing current vs. previous quarter)
- Component score calculations (weighted averages)
- **PROTECT** all formula cells to prevent accidental overwrites

**4. Maturity Scoring Formulas:**

- Overall Score (Sheet 2, B5):

```python
  formula = "=ROUND(('Sheet3'!B20*0.25)+('Sheet4'!B20*0.25)+('Sheet5'!B20*0.25)+('Sheet6'!B20*0.25),0)"
```

- Component Scores (Each sheet, Row 20, Column B): Weighted average per assessment area

**5. Trend Analysis Structure (Sheet 8):**

- Columns B-E: Q1, Q2, Q3, Q4 (manual entry)
- Column G: Trend formula comparing current vs. previous quarter

```python
  trend_formula = '=IF(ISBLANK(B5),"→",IF(C5>=B5*1.05,"↑",IF(C5<=B5*0.95,"↓","→")))'
```

**6. Conditional Formatting:**

- More extensive than assessments (RAG visualization critical for executive audience)
- Use `openpyxl` conditional formatting for:
  - Color scales (green-yellow-red)
  - Icon sets (arrows for trends)
  - Data bars (optional for percentages)

**7. Sheet Protection:**

- Sheet 1: Fully protected (instructions, read-only)
- Sheets 2-6: Protect formulas, leave manual entry cells unlocked
- Sheet 7: Fully unprotected (critical gaps manual entry)
- Sheet 8: Protect trend formulas, leave quarterly values unlocked
- Sheet 9: Fully unprotected (narrative text, approval)

## Script Validation Checks

**Before generating workbook, validate:**
```python
# Check 1: Data source mapping table has all required metrics
required_metrics = [
    'Retention Coverage %',
    'NIST Compliance %',
    'Vendor SLA Compliance %',
    'Audit Readiness Score',
    # ... (40-60 total)
]
assert len(data_source_mapping) >= 40, "Missing metrics in mapping table"

# Check 2: Formula cells are protected, manual entry cells are not
for sheet in [sheet2, sheet3, sheet4, sheet5, sheet6]:
    for row in sheet.iter_rows():
        for cell in row:
            if cell.fill.fgColor.rgb == 'FFFFFF00':  # Yellow = manual entry
                assert cell.protection.locked == False
            elif 'FORMULA' in str(cell.value):
                assert cell.protection.locked == True

# Check 3: RAG status formulas use correct thresholds
rag_formula_pattern = r'IF\(.*>=90.*Green.*IF\(.*>=70.*Amber.*Red'
assert re.search(rag_formula_pattern, sheet2['D5'].value)

# Check 4: Maturity score formula references all 4 component scores
maturity_formula = sheet2['B5'].value
assert "'Sheet3'!B20" in maturity_formula
assert "'Sheet4'!B20" in maturity_formula
assert "'Sheet5'!B20" in maturity_formula
assert "'Sheet6'!B20" in maturity_formula
assert "*0.25" in maturity_formula  # 25% weight each

# Check 5: Trend analysis has Q1-Q4 columns
assert sheet8['B4'].value == "Q1 [Year]"
assert sheet8['C4'].value == "Q2 [Year]"
assert sheet8['D4'].value == "Q3 [Year]"
assert sheet8['E4'].value == "Q4 [Year]"
```

## Common Mistakes to Avoid in Script

**1. ❌ CRITICAL ERROR: Creating External File Links**
```python
# WRONG - creates external file link (breaks if source file moved)
cell.value = "='[A_8_10_1_Retention.xlsx]Sheet7'!B5"

# CORRECT - manual entry instruction in mapping table
mapping_table.append([
    'Sheet 3', 'B5', 
    'A.8.10.1_Retention_[Date].xlsx', 'Sheet 7', 'B5',
    'Total Data Categories', 'Count'
])
cell.fill = yellow_fill  # Mark for manual entry
```

**2. ❌ Forgetting to Protect Formula Cells**
```python
# WRONG - formulas unprotected, user can accidentally overwrite
formula_cell.value = "=B5/B6*100"

# CORRECT - formulas protected
formula_cell.value = "=B5/B6*100"
formula_cell.protection = Protection(locked=True)
ws.protection.sheet = True
ws.protection.password = None  # Allow unlocking yellow cells
```

**3. ❌ Hardcoding Year in Trend Analysis**
```python
# WRONG - hardcoded 2024
sheet8['B4'].value = "Q1 2024"

# CORRECT - placeholder for user to fill
sheet8['B4'].value = "Q1 [Year]"
```

**4. ❌ Incorrect RAG Threshold Formulas**
```python
# WRONG - backwards logic (green for <70%)
formula = "=IF(B5<70,'Green',IF(B5<90,'Amber','Red'))"

# CORRECT - green for ≥90%
formula = "=IF(B5>=90,'Green',IF(B5>=70,'Amber','Red'))"
```

## Integration with Source Assessment Generators

**A.8.10.5 Dashboard is DEPENDENT on A.8.10.1-4:**

When developing/testing `generate_a810_5_compliance_dashboard.py`:

1. **First generate sample source workbooks:**
```python
   # Generate source assessments with test data
   exec(open('generate_a810_1_retention_triggers.py').read())
   exec(open('generate_a810_2_deletion_methods.py').read())
   exec(open('generate_a810_3_third_party_cloud.py').read())
   exec(open('generate_a810_4_verification_evidence.py').read())
```

2. **Manually populate sample data in source workbooks** (or use test data generator)

3. **Then generate dashboard workbook:**
```python
   exec(open('generate_a810_5_compliance_dashboard.py').read())
```

4. **Test manual entry workflow:**

   - Open dashboard workbook
   - Follow Data Source Mapping Table instructions
   - Manually copy values from source workbooks
   - Verify formulas calculate correctly

**Test Scenario:**
```
Source A.8.10.1 Sheet 7, B7 = 95% (Retention Coverage)
→ Copy to Dashboard Sheet 3, B7
→ Dashboard Sheet 3, D7 formula should show "Amber" (95% is 90-100 range but target is 100%)
→ Dashboard Sheet 2, B6 should show 95%
→ Overall Maturity Score should incorporate this value
```

---

# Version Control & Change Management

## Workbook Versioning

**Filename Format:**
```
ISMS_A_8_10_5_Compliance_Dashboard_YYYYMMDD_Qn.xlsx
```

**Example:** `ISMS_A_8_10_5_Compliance_Dashboard_20260130_Q1.xlsx`

**Quarterly Snapshots:**

- Keep separate file for each quarter (Q1, Q2, Q3, Q4)
- Archive previous quarters (read-only)
- Current quarter = working copy

**Version Tracking in Sheet 1:**

- Document ID: ISMS-IMP-A.8.10.5
- Version: 1.0
- Quarter: Q1/Q2/Q3/Q4 [Year]
- Date: DD.MM.YYYY

## Change Log

**Version 1.0 → 2.0 Changes:**

- Added PART I: USER COMPLETION GUIDE (comprehensive user documentation)
- Enhanced PART II: TECHNICAL SPECIFICATION (detailed Excel structure)
- Added Data Source Mapping Table (prevents manual entry errors)
- Strengthened Maturity Scoring Model (weighted component scoring)
- Added Quarterly Trend Analysis (Q1-Q4 comparison)
- Improved Executive Summary guidance (board presentation focus)
- Enhanced conditional formatting (RAG visualization)
- Updated approval workflow (three-level sign-off)

## Backward Compatibility

**v2.0 Workbooks:**

- Compatible with Excel 2016+
- Compatible with LibreOffice Calc 6.0+ (minor formatting differences)
- Not compatible with Google Sheets (use Excel Online for cloud access)

**v1.0 to v2.0 Migration:**

- No automated migration (different structure)
- Manually transfer Q1 baseline from v1.0 to v2.0 Sheet 8 if upgrading mid-year
- Recommend starting v2.0 at beginning of new fiscal year or quarter

---

# Quality Assurance Checklist

## Pre-Deployment Validation

Before using generated dashboard workbook, verify:

**Data Source Mapping (Sheet 1):**

- [ ] All 40-60 metrics documented in mapping table
- [ ] Source cell references match actual source workbook structure
- [ ] No broken references or TBD placeholders

**Formula Accuracy (Sheets 2-6):**

- [ ] RAG status formulas use correct thresholds (≥90% green, 70-89% amber, <70% red)
- [ ] Component score formulas use correct weightings (sum to 100%)
- [ ] Overall Maturity Score formula references all 4 component scores
- [ ] No #REF!, #DIV/0!, #VALUE! errors in any formula cells

**Manual Entry Cells:**

- [ ] All manual entry cells have yellow fill
- [ ] Manual entry cells are UNLOCKED (not protected)
- [ ] Data validation applied where appropriate (percentages 0-100, dates)

**Protection:**

- [ ] Formula cells are LOCKED (protected)
- [ ] Instructions sheet fully protected
- [ ] Manual entry cells remain editable when sheet protection enabled

**Conditional Formatting:**

- [ ] RAG status colors apply correctly
- [ ] Trend arrows display correctly (↑↓→)
- [ ] Overdue dates highlighted in red

## Post-Completion Validation

After manual data entry, verify:

- [ ] All yellow cells populated (no blanks)
- [ ] NIST category percentages sum to 100% (Sheet 4, B10+B11+B12=100)
- [ ] Component scores calculate correctly (Sheets 3-6, Row 20)
- [ ] Overall Maturity Score matches manual calculation
- [ ] Trend Analysis shows realistic quarter-over-quarter changes
- [ ] Critical Gaps Dashboard has remediation dates for all gaps
- [ ] Executive Summary narrative matches quantitative data
- [ ] Three-level approval completed with dates

---

# Integration with ISMS Management Review

## ISO 27001 Clause 9.3 Requirement

**ISO 27001:2022 Clause 9.3.2:**
> *"The management review shall include consideration of... the results of monitoring and measurement."*

**A.8.10.5 Dashboard fulfills this requirement** by providing:

- Systematic monitoring results (quarterly assessments)
- Measurable compliance metrics (percentages, scores, counts)
- Trend analysis (improvement or decline identification)
- Performance evaluation (maturity scoring model)

## Dashboard Integration into Management Review

**Recommended Agenda Item:**
```
ISMS MANAGEMENT REVIEW - Control A.8.10 (Information Deletion)

1. Overall Compliance Status

   - Present Sheet 2 (Overall A.8.10 Compliance)
   - Highlight maturity score and trend vs. previous quarter

2. Assessment Area Deep Dives (if significant changes)

   - Retention Schedule Health (Sheet 3) - if coverage changed ±5%
   - Deletion Method Effectiveness (Sheet 4) - if NIST compliance changed ±5%
   - Third-Party Performance (Sheet 5) - if Shadow IT or SLA issues
   - Verification Quality (Sheet 6) - if audit readiness changed

3. Critical Gaps Requiring Management Decision

   - Present Sheet 7 (Critical Gaps Dashboard)
   - Request budget approval for remediation
   - Assign accountability for high-priority gaps

4. Regulatory Compliance Status

   - GDPR Article 17: [Compliant/Non-Compliant + evidence]
   - Swiss FADP Article 6: [Compliant/Non-Compliant + evidence]
   - ISO 27001 A.8.10: [Conformity statement]

5. Management Decisions & Actions

   - Approve remediation budgets
   - Set target maturity score for next quarter
   - Escalate vendor performance issues (if applicable)

```

## Documentation Requirements

**Archive with Management Review Minutes:**

- PDF export of completed dashboard (Sheets 2-6 summary + Executive Summary)
- Quarter designation (Q1/Q2/Q3/Q4 [Year])
- Management decisions and action items
- Link to source assessment workbooks (A.8.10.1-4) for detailed evidence

---

**END OF SPECIFICATION**

---

*"We have to accept that nature behaves in a way that seems strange to us, because we evolved to understand the macroscopic world."*
— Alain Aspect

<!-- QA_VERIFIED: 2026-02-06 -->

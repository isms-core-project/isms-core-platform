<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.6.2-TG:framework:TG:a.8.6.2 -->
**ISMS-IMP-A.8.6.2-TG - Capacity Forecasting & Planning**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.6: Capacity Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Capacity Forecasting Planning |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.6.2-TG |
| **Related Policy** | ISMS-POL-A.8.6 (Capacity Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.6 (Capacity Management) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.6 (Capacity Management)
- ISMS-IMP-A.8.6.1 (Capacity Monitoring Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a86_2_capacity_forecasts.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.6-Assessment-2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Historical Utilization |
| 2 | Trend Analysis |
| 3 | Capacity Forecasts |
| 4 | Capacity Exhaustion |
| 5 | Planned Expansions |
| 6 | Forecast Accuracy |
| 7 | Budget Planning |
| 8 | Instructions & Legend |
| 9 | Summary Dashboard |
| 10 | Evidence Register |
| 11 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | HISTORICAL CAPACITY UTILIZATION DATA |
| 2 | CAPACITY TREND ANALYSIS |
| 3 | CAPACITY EXHAUSTION PROJECTIONS |
| 4 | PLANNED CAPACITY EXPANSIONS |
| 5 | FORECAST ACCURACY VALIDATION |
| 6 | CAPACITY BUDGET PLANNING |
| 7 | Total Critical/Immediate Exhaustion Risks: |
| 8 | Symbol |
| 9 | Status |
| 10 | Description |
| 11 | Month/Date |
| 12 | Resource Name |
| 13 | Utilization (%) |
| 14 | Peak Utilization (%) |
| 15 | Notes |
| 16 | Data Source |
| 17 | Trend Method |
| 18 | Growth Rate (% per month) |
| 19 | R-Squared |
| 20 | Seasonal Pattern |
| 21 | Analyst |
| 22 | Current Utilization (%) |
| 23 | Growth Rate (%/month) |
| 24 | 6-Month Forecast (%) |
| 25 | 12-Month Forecast (%) |
| 26 | 24-Month Forecast (%) |
| 27 | Confidence |
| 28 | Assumptions |
| 29 | Forecast Date |
| 30 | Current (%) |
| 31 | Threshold (%) |
| 32 | Growth Rate (%/mo) |
| 33 | Months to Threshold |
| 34 | Exhaustion Date |
| 35 | Urgency |
| 36 | Action Required |
| 37 | Current Capacity |
| 38 | Expansion Amount |
| 39 | New Total Capacity |
| 40 | Planned Date |
| 41 | Lead Time (days) |
| 42 | Cost Estimate |
| 43 | Approval Status |
| 44 | Owner |
| 45 | Forecasted Value |
| 46 | Actual Value |
| 47 | Absolute Error |
| 48 | Percentage Error (%) |
| 49 | Accuracy Rating |
| 50 | Lessons Learned |
| 51 | Resource/Project |
| 52 | Quarter |
| 53 | CapEx (CHF) |
| 54 | OpEx (CHF/month) |
| 55 | 3-Year TCO (CHF) |
| 56 | Evidence ID |
| 57 | Assessment Area |
| 58 | Evidence Type |
| 59 | Location/Path |
| 60 | Date Collected |
| 61 | Collected By |
| 62 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Linear Regression, Growth Rate, Seasonal Model, Business-Driven
Manual Estimate, None, Weekly, Monthly, Quarterly, Annual, Custom, High
Medium, Low, Planned, In Procurement, Ordered, Delivered, Installed, Completed
Cancelled, Pending, Approved, Rejected, Deferred, Q1, Q2, Q3, Q4
Capacity report, Screenshot, Monitoring export, Documentation, Vendor spec
Budget approval, Forecast model, Compliance report, Other, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required, Approved with Conditions
```

**Extracted:** 11 sheets, 62 columns, 47 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"In cryptography, we must always assume the worst about our adversaries."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->

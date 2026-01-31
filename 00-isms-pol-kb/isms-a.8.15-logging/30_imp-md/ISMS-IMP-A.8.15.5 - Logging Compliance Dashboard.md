# ISMS-IMP-A.8.15.5
## Logging Compliance Dashboard
### Excel Workbook Layout Specification

**Document ID**: ISMS-IMP-A.8.15.5  
**Assessment Area**: Overall Logging Program Compliance Dashboard  
**Related Policy**: All ISMS-POL-A.8.15 sections  
**Purpose**: Executive summary dashboard consolidating all logging assessments  
**Python Generator**: `generate_a815_5_compliance_dashboard.py`

---

## Workbook Structure

### Sheet 1: Executive Dashboard

**Purpose**: Single-page executive view of entire logging program

**Header**: "Logging Program Compliance Dashboard - ISO/IEC 27001:2022 Control A.8.15"

**Document Information Block** (Rows 1-7):
```
Organization:          [USER INPUT]
Reporting Period:      [USER INPUT - Q4 2025]
Dashboard Date:        [AUTO - Today's date]
Program Owner:         CISO
Program Manager:       Information Security Manager
Last Full Assessment:  [Date of last IMP 1-4 completion]
Next Assessment Due:   [Calculated: Last + Review Cycle]
```

---

**Section 1: Overall Compliance Summary** (Rows 9-18, prominent display):

Large KPI boxes with conditional formatting:

| Metric | Value | Status | Target |
|--------|-------|--------|--------|
| **Overall Compliance Score** | Formula: Weighted avg of all assessments | Color: Green >95%, Yellow 85-95%, Red <85% | >95% |
| **Log Source Coverage** | From IMP 1: % systems logging | Color coded | 100% |
| **Collection Reliability** | From IMP 2: % uptime | Color coded | >99% |
| **Protection Compliance** | From IMP 3: % protected | Color coded | >95% |
| **Retention Compliance** | From IMP 3: % meeting retention | Color coded | 100% |
| **Review Compliance** | From IMP 4: % reviews completed | Color coded | 100% |
| **Detection Effectiveness** | From IMP 4: MTTD + alert quality | Color coded | >90% |
| **Critical Gaps Open** | From all IMPs: Critical priority gaps | Red if >0 | 0 |

---

**Section 2: Compliance by Assessment Area** (Rows 20-32):

Bar chart with data table:

| Assessment Area | Document ID | Completion Date | Compliance % | Status | Next Due |
|-----------------|-------------|-----------------|--------------|--------|----------|
| Log Source Inventory | IMP-A.8.15.1 | DD.MM.YYYY | Formula | Status | Date |
| Log Collection | IMP-A.8.15.2 | DD.MM.YYYY | Formula | Status | Date |
| Protection & Retention | IMP-A.8.15.3 | DD.MM.YYYY | Formula | Status | Date |
| Analysis & Review | IMP-A.8.15.4 | DD.MM.YYYY | Formula | Status | Date |

---

**Section 3: Compliance Trend** (Rows 34-48):

Line chart showing compliance over time (if historical data available):
- X-axis: Assessment periods (Q1 2025, Q2 2025, etc.)
- Y-axis: Compliance percentage
- Multiple lines: Overall, Log Sources, Collection, Protection, Analysis

---

**Section 4: Risk Heat Map** (Rows 50-65):

Matrix view:

|  | Log Sources | Collection | Protection | Retention | Review |
|--|-------------|------------|------------|-----------|--------|
| **Critical Systems** | Status | Status | Status | Status | Status |
| **High Systems** | Status | Status | Status | Status | Status |
| **Medium Systems** | Status | Status | Status | Status | Status |
| **Low Systems** | Status | Status | Status | Status | Status |

Color coding: Green = compliant, Yellow = partial, Red = non-compliant

---

**Section 5: Top 10 Gaps Requiring Attention** (Rows 67-82):

| Gap ID | Category | Description | Priority | Impact | Owner | Target Date | Status | Days Overdue |
|--------|----------|-------------|----------|--------|-------|-------------|--------|--------------|
| [From IMP gap sheets, sorted by priority] ||||||||

---

**Section 6: Key Metrics Summary** (Rows 84-100):

Three-column layout:

**Log Sources** | **Collection & Protection** | **Analysis & Detection**
- Total systems: ### | - Events/day: ### | - Use cases active: ###
- Logging enabled: ##% | - Storage used: ##% | - Alerts/day: ###
- SIEM integrated: ##% | - Collection uptime: ##% | - True positive rate: ##%
- Missing sources: ### | - Parse success rate: ##% | - MTTD: ## hours
- Priority 1 compliant: ##% | - Backup success: ##% | - MTTR: ## hours

---

**Section 7: Regulatory Compliance Summary** (Rows 102-115):

| Regulation | Applicable Systems | Compliance Status | Key Requirements Met | Gaps |
|------------|-------------------|-------------------|---------------------|------|
| ISO 27001 | All | Status % | List | Count |
| PCI DSS | Payment systems | Status % | List | Count |
| GDPR | EU data systems | Status % | List | Count |
| HIPAA | Healthcare systems | Status % | List | Count |
| SOX | Financial systems | Status % | List | Count |
| DORA | Financial ICT | Status % | List | Count |
| NIS2 | Critical infra | Status % | List | Count |

---

**Section 8: Resource Utilization** (Rows 117-128):

| Resource Type | Allocated | Used | % Used | Status | Forecast Need (+12m) |
|---------------|-----------|------|--------|--------|---------------------|
| Storage (TB) | ## | ## | Formula | Status | ## |
| SIEM Licenses | ## | ## | Formula | Status | ## |
| SOC FTE | ## | ## | Formula | Status | ## |
| Budget (Annual) | $### | $### | Formula | Status | $### |

---

**Section 9: Program Maturity Assessment** (Rows 130-145):

Maturity scorecard (1-5 scale):

| Capability | Maturity Level | Description | Target | Gap |
|------------|----------------|-------------|--------|-----|
| Log Coverage | 1-5 | Ad-hoc / Defined / Managed / Optimized | 4-5 | +/- |
| Collection Reliability | 1-5 | "" | 4-5 | +/- |
| Protection & Integrity | 1-5 | "" | 4-5 | +/- |
| Analysis & Detection | 1-5 | "" | 4-5 | +/- |
| Incident Response | 1-5 | "" | 4-5 | +/- |
| Process Documentation | 1-5 | "" | 4-5 | +/- |
| Staff Training | 1-5 | "" | 4-5 | +/- |
| Continuous Improvement | 1-5 | "" | 4-5 | +/- |

Radar chart visualization of maturity levels

---

**Section 10: Action Items Summary** (Rows 147-160):

| Priority | Open | This Month | Next Month | Next Quarter | Overdue |
|----------|------|------------|------------|--------------|---------|
| Critical | COUNT | COUNT | COUNT | COUNT | COUNT |
| High | COUNT | COUNT | COUNT | COUNT | COUNT |
| Medium | COUNT | COUNT | COUNT | COUNT | COUNT |
| Total | SUM | SUM | SUM | SUM | SUM |

---

### Sheet 2: Detailed Metrics

**Purpose**: Detailed breakdown of all compliance metrics

**Section 1: Log Source Metrics** (from IMP 1):
- Total systems assessed
- Systems by type breakdown
- Systems by environment breakdown
- Logging enabled rate
- Event type coverage percentages
- Compliance by system criticality

**Section 2: Collection Metrics** (from IMP 2):
- Daily event volume
- Parse success rates
- Collection reliability by source
- Storage capacity metrics
- SIEM performance metrics
- Integration health

**Section 3: Protection Metrics** (from IMP 3):
- Access control implementation rate
- Integrity protection implementation rate
- Encryption in transit rate
- Backup success rate
- Separation of duties compliance
- Legal holds active

**Section 4: Retention Metrics** (from IMP 3):
- Retention compliance by log type
- Storage tier utilization
- Disposal process compliance
- Over/under retention issues

**Section 5: Analysis Metrics** (from IMP 4):
- Review schedule compliance
- Alert volumes and quality
- Detection effectiveness
- Investigation quality scores
- SOC analyst performance
- Detection coverage percentages

---

### Sheet 3: Gap Register (Consolidated)

**Purpose**: All gaps from all assessments in one place

**Column Structure** (15 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 15 | Text: Source-###  (e.g., IMP1-001) |
| B | Source Assessment | 20 | Dropdown: IMP 1, IMP 2, IMP 3, IMP 4 |
| C | Gap Category | 25 | Text |
| D | Description | 50 | Text |
| E | Policy Requirement | 25 | Text: S2.x.x reference |
| F | Priority | 15 | Dropdown: Critical, High, Medium, Low |
| G | Business Impact | 20 | Dropdown: Critical, High, Medium, Low |
| H | Affected Systems Count | 20 | Number |
| I | Remediation Action | 50 | Text |
| J | Owner | 25 | Text |
| K | Target Date | 15 | Date: DD.MM.YYYY |
| L | Budget Required | 15 | Number: $ amount |
| M | Status | 15 | Dropdown: Open, In Progress, Resolved, Deferred |
| N | Days Open | 12 | Formula: TODAY() - First identified |
| O | Notes | 40 | Text |

**Data Import**: Pull gaps from IMP 1-4 gap sheets

**Auto-Calculations**:
- Days overdue (if past target date and not resolved)
- Total budget required
- Gaps by priority/status

---

### Sheet 4: Trend Analysis

**Purpose**: Historical trend tracking (populated over multiple assessment cycles)

**Column Structure** (Variable columns based on quarters):

| Assessment Period | Q1 2025 | Q2 2025 | Q3 2025 | Q4 2025 | Target |
|-------------------|---------|---------|---------|---------|--------|
| Overall Compliance % | ## | ## | ## | ## | >95% |
| Log Source Coverage % | ## | ## | ## | ## | 100% |
| Collection Reliability % | ## | ## | ## | ## | >99% |
| Protection Compliance % | ## | ## | ## | ## | >95% |
| Retention Compliance % | ## | ## | ## | ## | 100% |
| Review Compliance % | ## | ## | ## | ## | 100% |
| Alert True Positive % | ## | ## | ## | ## | >50% |
| MTTD (hours) | ## | ## | ## | ## | <1 |
| MTTR (hours) | ## | ## | ## | ## | <4 |
| Open Critical Gaps | ## | ## | ## | ## | 0 |

**Charts**:
- Trend lines for each metric
- Gap closure velocity
- Improvement trajectory

---

### Sheet 5: Regulatory Mapping

**Purpose**: Map logging requirements to regulatory obligations

**Column Structure** (12 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Regulation / Standard | 25 | Dropdown: ISO 27001, PCI DSS, HIPAA, GDPR, SOX, DORA, NIS2 |
| B | Requirement ID | 20 | Text: Specific clause |
| C | Requirement Description | 50 | Text |
| D | Policy Section | 20 | Text: S2.x.x |
| E | Implementation Assessment | 25 | Text: Which IMP covers this |
| F | Applicable Systems | 30 | Text: Which systems must comply |
| G | Compliance Status | 18 | Dropdown: Compliant, Partial, Non-Compliant |
| H | Evidence Location | 40 | Text: Where evidence is |
| I | Last Verified | 15 | Date: DD.MM.YYYY |
| J | Next Verification | 15 | Date |
| K | Gaps | 40 | Text |
| L | Notes | 40 | Text |

**Data Rows**: 50-150 (regulatory requirements)

**Key Regulatory Requirements Mapped**:
- ISO 27001:2022 A.8.15
- PCI DSS 4.0 Requirement 10
- HIPAA § 164.312(b)
- GDPR Article 32
- SOX Section 404
- DORA Article 17
- NIS2 Article 21

---

### Sheet 6: Action Plan & Roadmap

**Purpose**: Strategic roadmap for logging program improvements

**Column Structure** (13 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Initiative ID | 15 | Auto: INIT-001 |
| B | Initiative Name | 30 | Text |
| C | Description | 50 | Text |
| D | Strategic Goal | 30 | Dropdown: Improve Coverage, Enhance Detection, Reduce Gaps, Compliance, Optimization, Other |
| E | Related Gaps | 25 | Text: Gap IDs addressed |
| F | Priority | 15 | Dropdown: Critical, High, Medium, Low |
| G | Start Date | 15 | Date |
| H | Target End Date | 15 | Date |
| I | Status | 15 | Dropdown: Not Started, Planning, In Progress, Completed, On Hold |
| J | % Complete | 12 | Number: 0-100 |
| K | Budget | 15 | Number: $ |
| L | Owner | 25 | Text |
| M | Notes | 40 | Text |

**Roadmap Visualization** (Gantt chart style):
Timeline showing initiatives across quarters

---

### Sheet 7: Management Report Template

**Purpose**: Pre-formatted report for management presentation

**Report Structure**:

**Page 1: Executive Summary** (Rows 1-40)
- Overall compliance status (Green/Yellow/Red)
- Key achievements this period
- Critical issues requiring attention
- Resource requirements
- Recommended actions

**Page 2: Detailed Findings** (Rows 42-80)
- Compliance by assessment area
- Gap summary by priority
- Regulatory compliance status
- Metric trends

**Page 3: Action Plan** (Rows 82-120)
- Priority gaps and remediation plans
- Resource requests (budget, personnel, tools)
- Timeline for improvements
- Expected outcomes

**Formatting**: Professional report layout with:
- Headers/footers
- Page numbers
- Print-friendly formatting
- Charts embedded
- Executive-appropriate language

---

### Sheet 8: Instructions & Data Sources

**Purpose**: Explain how to use and update the dashboard

**Content**:

**Data Sources**:
- IMP-A.8.15.1: Log Source Inventory (Sheet 2 pulls from IMP 1)
- IMP-A.8.15.2: Log Collection (Sheet 2 pulls from IMP 2)
- IMP-A.8.15.3: Protection & Retention (Sheet 2 pulls from IMP 3)
- IMP-A.8.15.4: Analysis & Review (Sheet 2 pulls from IMP 4)

**Update Frequency**:
- Quarterly: Full dashboard refresh with new IMP assessments
- Monthly: Update metrics that change monthly (events/day, storage, etc.)
- Weekly: Update action item status
- Daily: Update if real-time SIEM metrics integrated

**How to Update**:
1. Complete IMP assessments (1-4) for the period
2. Export summary data from each IMP
3. Paste into "Data Import" section (hidden sheet)
4. Dashboard auto-refreshes with formulas
5. Review calculated metrics for accuracy
6. Update status of gaps/actions manually
7. Generate management report (Sheet 7)
8. Present to CISO/management

**Customization Notes**:
- Adjust targets based on organizational risk appetite
- Add/remove regulatory sections as applicable
- Customize maturity model definitions
- Add organization-specific KPIs

---

## Formulas & Logic

**Overall Compliance Score**:
```excel
= (IMP1_Score * 0.25) + (IMP2_Score * 0.25) + (IMP3_Score * 0.25) + (IMP4_Score * 0.25)
```

**Status Color Coding**:
```excel
Green: >=95%
Yellow: >=85% AND <95%
Red: <85%
```

**Days Overdue** (Gap Register):
```excel
=IF(AND(K2<TODAY(), M2<>"Resolved"), TODAY()-K2, 0)
```

**Trend Calculation**:
```excel
=IF(Current_Period > Previous_Period, "Improving", IF(Current_Period < Previous_Period, "Declining", "Stable"))
```

---

## Conditional Formatting Rules

**Apply across dashboard**:
- Compliance percentages: Red <85%, Yellow 85-95%, Green >95%
- Status indicators: Red = Non-Compliant, Yellow = Partial, Green = Compliant
- Days overdue: Red if >0
- Priority: Red = Critical, Orange = High, Yellow = Medium, Green = Low
- Trend indicators: Up arrow (green) = improving, Down arrow (red) = declining

---

## File Naming Convention

**Filename**: `ISMS-IMP-A_8_15_5_Compliance_Dashboard_YYYYMMDD.xlsx`

Example: `ISMS-IMP-A_8_15_5_Compliance_Dashboard_20260106.xlsx`

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.5 |
| **Version** | 1.0 |
| **ISO 27001 Control** | A.8.15 (Logging) |
| **Related Policy** | All ISMS-POL-A.8.15 sections |
| **Sheet Count** | 8 |
| **Update Frequency** | Quarterly (full), Monthly (metrics) |
| **Target Audience** | Executive Management, CISO, Audit |

---

**END OF IMP SPECIFICATION A.8.15.5**
**ISMS-IMP-A.7.12-13.S4: Infrastructure Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Controls A.7.12 & A.7.13: Cabling Security and Equipment Maintenance

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.12-13.S4 |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Dashboard - Cabling Security and Equipment Maintenance |
| **Related Policy** | ISMS-POL-A.7.12-13 (Full Policy) |
| **Purpose** | Provide consolidated compliance view across cabling security and equipment maintenance domains |
| **Target Audience** | CISO, IT Management, Compliance Officers, Internal Audit, External Auditors |
| **Assessment Type** | Executive Summary and Compliance Dashboard |
| **Review Cycle** | Quarterly or On-Demand |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Infrastructure Compliance Dashboard | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Dashboard Overview
  - Data Sources
  - Interpreting the Dashboard
  - Executive Reporting
  - Gap Remediation Tracking

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - External Workbook Links
  - Integration Points


---

# PART I: USER COMPLETION GUIDE

## Dashboard Overview

### Purpose & Scope

**Dashboard Name:** ISMS-IMP-A.7.12-13.S4 - Infrastructure Compliance Dashboard

#### What This Dashboard Provides

This dashboard provides a **consolidated executive view** of compliance across cabling security (A.7.12) and equipment maintenance (A.7.13). It aggregates data from the detailed assessments (S1, S2, S3) to provide:

- Overall infrastructure compliance score
- Domain-level compliance breakdown
- Key risk indicators
- Gap summary with remediation status
- Trend analysis over time
- Audit-ready compliance summary


#### Key Principle

This dashboard **pulls data from the detailed assessments** (S1, S2, S3). It is NOT a standalone assessment - it requires the underlying assessments to be completed first. The dashboard auto-calculates compliance scores and highlights areas requiring attention.


#### Data Sources

| Source Assessment | Data Pulled |
|-------------------|-------------|
| ISMS-IMP-A.7.12-13.S1 (Cabling Security) | Pathway compliance, protection status, access controls, documentation |
| ISMS-IMP-A.7.12-13.S2 (Equipment Maintenance) | Equipment inventory, personnel verification, security controls, remote access |
| ISMS-IMP-A.7.12-13.S3 (Maintenance Schedule) | Schedule compliance %, overdue items, critical equipment status |


### Who Should Use This Dashboard

#### Primary Audience

1. **CISO** - Executive oversight of infrastructure security
2. **IT Management** - Operational compliance monitoring
3. **Compliance Officers** - Audit preparation and compliance tracking
4. **Internal Audit** - Control effectiveness assessment
5. **External Auditors** - ISO 27001 certification evidence

#### Use Frequency

- **Monthly:** Review overall compliance status
- **Quarterly:** Full review with trend analysis
- **On-Demand:** Audit preparation, executive reporting


### Expected Outputs

Using this dashboard provides:

1. ✅ **Single compliance score** - Overall A.7.12-13 compliance percentage
2. ✅ **Domain breakdown** - Cabling vs. Maintenance compliance
3. ✅ **Risk indicators** - Critical gaps highlighted
4. ✅ **Gap register** - All non-compliant items with remediation status
5. ✅ **Trend visibility** - Compliance changes over time
6. ✅ **Audit evidence** - Executive summary for audit

---

## Data Sources

### S1: Cabling Security Assessment

**Data Elements:**

| Metric | Source Sheet | Formula/Reference |
|--------|--------------|-------------------|
| Pathway Compliance % | Sheet 2 | Count Compliant / Total |
| Protection Score % | Sheet 3 | Weighted average |
| Access Control Score % | Sheet 4 | Count Compliant / Total |
| Documentation Score % | Sheet 5 | Count Current / Total |
| Gap Count | Sheets 2-5 | Count Non-Compliant |

### S2: Equipment Maintenance Assessment

**Data Elements:**

| Metric | Source Sheet | Formula/Reference |
|--------|--------------|-------------------|
| Equipment Coverage % | Sheet 2 | In Programme / Total |
| Personnel Compliance % | Sheet 4 | Verified / Total |
| Security Controls % | Sheet 5 | Compliant items / Total |
| Remote Access Compliance % | Sheet 6 | Compliant / Total |
| Gap Count | All Sheets | Count Non-Compliant |

### S3: Maintenance Schedule Tracking

**Data Elements:**

| Metric | Source Sheet | Formula/Reference |
|--------|--------------|-------------------|
| Schedule Compliance % | Sheet 2 | Current / Total |
| Overdue Count | Sheet 2 | Count Overdue |
| Critical Overdue | Sheet 2 | Count Tier 1 Overdue |
| Average Days Overdue | Sheet 3 | Average of overdue days |

---

## Interpreting the Dashboard

### Overall Compliance Score

**Calculation:**

```
Overall Score = (Cabling Score × 40%) + (Maintenance Score × 60%)
```

**Thresholds:**

| Score | Status | Interpretation |
|-------|--------|----------------|
| ≥90% | 🟢 Excellent | Controls effective, audit-ready |
| 75-89% | 🟡 Good | Minor gaps, remediation in progress |
| 60-74% | 🟠 Acceptable | Significant gaps, requires attention |
| <60% | 🔴 Non-Compliant | Major gaps, immediate action required |


### Domain Scores

**Cabling Security Score (40% weight):**

```
Cabling Score = (Pathways × 30%) + (Protection × 25%) + (Access × 25%) + (Documentation × 20%)
```

**Equipment Maintenance Score (60% weight):**

```
Maintenance Score = (Schedule Compliance × 40%) + (Programme × 30%) + (Personnel × 15%) + (Security × 15%)
```


### Key Risk Indicators

**Red Flags (Require Immediate Action):**

- Critical equipment maintenance overdue >14 days
- Cabling infrastructure with no protection
- Wiring closets with no access control
- Remote access without session logging
- Personnel without verification


**Amber Warnings (Require Attention):**

- Standard equipment overdue 7-14 days
- Partial protection measures
- Documentation not current
- Remote access always enabled


### Gap Priority Matrix

| Priority | Criteria | SLA |
|----------|----------|-----|
| Critical | Tier 1 equipment affected, no compensating control | 7 days |
| High | Security control gap, compliance requirement | 14 days |
| Medium | Non-critical gap, compensating control in place | 30 days |
| Low | Documentation/administrative gap | 60 days |

---

## Executive Reporting

### Monthly Executive Summary

**Report Contents:**

1. **Overall Compliance Status**
   - Score with trend indicator (↑↓→)
   - Status colour (Green/Amber/Red)

2. **Domain Highlights**
   - Cabling Security: Score, key issues
   - Equipment Maintenance: Score, overdue count

3. **Key Risks**
   - Top 3 risks requiring attention
   - Remediation status

4. **Actions Required**
   - Resource requests
   - Executive decisions needed


### Quarterly Review Report

**Report Contents:**

1. **Trend Analysis**
   - 6-month compliance trend chart
   - Domain trend comparison

2. **Gap Remediation Progress**
   - Gaps opened vs. closed
   - Average remediation time

3. **Audit Readiness**
   - Evidence completeness
   - Assessment currency

4. **Improvement Recommendations**
   - Process improvements
   - Investment needs


### Audit Evidence Pack

**Evidence Package:**

1. Dashboard (this workbook) - S4
2. Cabling Security Assessment - S1
3. Equipment Maintenance Assessment - S2
4. Maintenance Schedule Tracking - S3
5. Evidence files referenced in Evidence Registers
6. Gap remediation evidence (closure documentation)

---

## Gap Remediation Tracking

### Gap Register

**What to Track:**

| Field | Description |
|-------|-------------|
| Gap ID | Unique identifier |
| Source | Which assessment (S1, S2, S3) |
| Description | What is the gap |
| Priority | Critical/High/Medium/Low |
| Owner | Who is responsible for remediation |
| Target Date | When remediation due |
| Status | Open/In Progress/Closed/Accepted |
| Remediation Plan | How it will be fixed |
| Evidence | Proof of remediation |


### Gap Closure Criteria

**To close a gap:**

1. Remediation action completed
2. Evidence collected (screenshot, document, etc.)
3. Verification performed (independent check)
4. Source assessment updated (S1, S2, or S3)
5. Dashboard reflects updated status


### Risk Acceptance

**If gap cannot be remediated:**

1. Document business justification
2. Document compensating controls
3. Assess residual risk
4. Obtain CISO approval
5. Set review date (maximum 6 months)
6. Record in Gap Register with "Accepted" status


---

## Common Pitfalls

### Pitfall 1: Stale Source Data

❌ **MISTAKE:** Dashboard shows excellent compliance, but source assessments (S1, S2, S3) have not been updated in months.

**Impact:** False sense of security, audit findings, inaccurate management reporting.

**How to Avoid:**
- Check "Last Updated" dates on all source assessments before dashboard review
- Establish minimum update frequency (monthly for S3, quarterly for S1/S2)
- Include source currency check in dashboard review procedure
- Add automated alerts for stale source data (>30 days without update)


### Pitfall 2: Broken External Links

❌ **MISTAKE:** Source workbook files renamed or moved, breaking dashboard formulas.

**Impact:** Dashboard shows #REF! errors or zero values, misleading compliance picture.

**How to Avoid:**
- Use standardised file naming (do not add dates to linked file names)
- Store all related workbooks in same directory
- Test links after any file operations (move, rename, copy)
- Document file location requirements in instructions sheet


### Pitfall 3: Gap Register Not Updated After Remediation

❌ **MISTAKE:** Gaps fixed but still showing "Open" status in register.

**Impact:** Inflated gap count, unnecessary management concern, audit confusion.

**How to Avoid:**
- Include dashboard update in gap closure procedure
- Require evidence reference before changing status to "Closed"
- Monthly reconciliation of gap register against source assessments
- Assign single owner for gap register maintenance


### Pitfall 4: Inconsistent Scoring Methodology

❌ **MISTAKE:** Different assessors interpret compliance differently, leading to inconsistent scores.

**Impact:** Trend data meaningless, cannot compare periods, audit challenges.

**How to Avoid:**
- Document scoring criteria explicitly in source assessments
- Use objective measures (counts, dates) rather than subjective ratings where possible
- Train all assessors on consistent methodology
- Perform calibration exercises quarterly


### Pitfall 5: Missing Weighting Documentation

❌ **MISTAKE:** Domain weights (40% cabling, 60% maintenance) changed without documentation.

**Impact:** Historical trends invalid, audit trail broken, management confusion.

**How to Avoid:**
- Document weighting rationale in Instructions sheet
- Require approval for weighting changes
- Note any weighting changes in Trend Analysis with effective date
- Maintain version history of methodology changes


### Pitfall 6: Trend Data Entry Errors

❌ **MISTAKE:** Monthly compliance scores entered incorrectly or in wrong month row.

**Impact:** Trend analysis misleading, management decisions based on false data.

**How to Avoid:**
- Double-check entries before saving
- Cross-reference entered values against source dashboards
- Use data validation to prevent out-of-range values
- Review trend for logical consistency (no sudden 50% swings unexplained)


### Pitfall 7: Ignoring Amber Warnings

❌ **MISTAKE:** Focus only on red (non-compliant) items, ignoring amber (acceptable) areas declining.

**Impact:** Problems escalate to critical before action taken, reactive rather than proactive.

**How to Avoid:**
- Include amber items in executive reporting
- Track trend direction for all domains, not just score
- Set threshold alerts for declining trends (two consecutive months down)
- Investigate root cause of any score decline >5%


### Pitfall 8: No Gap Ownership Assigned

❌ **MISTAKE:** Gaps identified but no owner assigned, remediation stalls.

**Impact:** Gaps remain open indefinitely, compliance deteriorates, audit findings.

**How to Avoid:**
- Require owner assignment before gap can be saved
- Default owner to assessment area manager if not specified
- Escalate unowned gaps after 7 days
- Include owner in gap status reporting


### Pitfall 9: Accepted Risks Not Reviewed

❌ **MISTAKE:** Gaps marked "Accepted" and then forgotten, compensating controls degrade.

**Impact:** Residual risk increases unnoticed, compensating controls may fail.

**How to Avoid:**
- Maximum 6-month review period for accepted risks
- Calendar reminders for review dates
- Quarterly report of all accepted risks to CISO
- Re-validate compensating controls at each review


### Pitfall 10: Audit Evidence Pack Incomplete

❌ **MISTAKE:** Dashboard presented to auditors without supporting source assessments and evidence.

**Impact:** Auditor cannot verify scores, extended audit duration, potential findings.

**How to Avoid:**
- Maintain evidence pack checklist (Sheet 6)
- Verify all source files accessible before audit
- Sample-check evidence references are valid
- Prepare evidence pack at least 2 weeks before audit


### Pitfall 11: Dashboard Not Reviewed Before Submission

❌ **MISTAKE:** Dashboard sent to executives with formula errors or incomplete data.

**Impact:** Loss of credibility, management distrust of ISMS metrics.

**How to Avoid:**
- Complete quality checklist before any distribution
- Peer review by second person
- Check for #REF!, #DIV/0!, #N/A errors
- Verify totals and percentages sum correctly


### Pitfall 12: Single Point of Failure for Dashboard

❌ **MISTAKE:** Only one person knows how to update and maintain the dashboard.

**Impact:** Dashboard not updated during absence, knowledge loss if person leaves.

**How to Avoid:**
- Document procedures in this specification
- Cross-train at least two people
- Include dashboard maintenance in role handover
- Store workbooks in shared location with access controls


### Pitfall 13: Overcomplicating the Dashboard

❌ **MISTAKE:** Adding excessive detail that obscures key messages for executives.

**Impact:** Executives ignore dashboard, key risks not communicated effectively.

**How to Avoid:**
- Executive summary should fit on one screen
- Use traffic light colours for quick status recognition
- Limit key indicators to top 5-7 items
- Detail available in subsequent sheets for those who need it


### Pitfall 14: Not Aligning with ISMS Calendar

❌ **MISTAKE:** Dashboard review not synchronised with management review schedule.

**Impact:** Outdated data presented to management, missed reporting deadlines.

**How to Avoid:**
- Align dashboard update with management review cycle
- Update completed 1 week before management review
- Include dashboard in ISMS calendar as recurring activity
- Set reminders for update deadlines


### Pitfall 15: Inconsistent Gap Closure Verification

❌ **MISTAKE:** Gaps closed based on verbal confirmation without evidence.

**Impact:** Audit findings for inadequate evidence, gaps may reopen.

**How to Avoid:**
- Require evidence reference (document, screenshot, ticket) for closure
- Independent verification for critical gaps
- Source assessment must show improvement before gap closed
- Document verification in Notes column


### Pitfall 16: Historical Data Lost During Updates

❌ **MISTAKE:** Previous period data overwritten instead of archived when updating.

**Impact:** Cannot perform trend analysis, audit trail incomplete.

**How to Avoid:**
- Enter new data in new rows, do not overwrite previous periods
- Archive previous versions before major updates
- Use version naming with date: Dashboard_20260201.xlsx
- Maintain minimum 12 months historical data


### Pitfall 17: Misinterpreting Compliance Percentages

❌ **MISTAKE:** Treating 80% compliance as "mostly good" when critical items are non-compliant.

**Impact:** Critical risks overlooked, false confidence in security posture.

**How to Avoid:**
- Always review critical/Tier 1 items separately
- Include "Critical Items Non-Compliant" as key indicator
- Weight scoring to emphasise critical items
- Narrative explanation required for any critical gap


### Pitfall 18: No Baseline Established

❌ **MISTAKE:** Tracking trends without establishing a baseline compliance level.

**Impact:** Cannot measure improvement, no target for remediation efforts.

**How to Avoid:**
- Document initial baseline when dashboard first populated
- Set target compliance levels (e.g., 90% overall)
- Track progress against targets, not just period-over-period
- Review and adjust targets annually


---

## Quality Checklist

### Sheet 1: Executive Summary Quality

- [ ] Assessment period correctly displayed
- [ ] Overall compliance score calculating (no errors)
- [ ] Status text matches score threshold (Excellent/Good/Acceptable/Non-Compliant)
- [ ] Cabling and Maintenance domain scores displaying
- [ ] Key risk indicators populated
- [ ] Gap summary counts match Gap Register
- [ ] Charts rendering correctly
- [ ] Trend indicator (arrow) showing correct direction
- [ ] No #REF!, #DIV/0!, or #N/A errors visible
- [ ] Colour coding correct for score levels


### Sheet 2: Cabling Security Quality

- [ ] All four sub-domain scores calculated
- [ ] Weights sum to 100%
- [ ] Domain score formula correct (weighted average)
- [ ] Detailed metrics populated from S1
- [ ] Gap list complete and current
- [ ] External links to S1 working
- [ ] Conditional formatting applied correctly
- [ ] Totals match S1 source data


### Sheet 3: Equipment Maintenance Quality

- [ ] All four sub-domain scores calculated
- [ ] Weights sum to 100%
- [ ] Domain score formula correct (weighted average)
- [ ] Schedule metrics from S3 accurate
- [ ] Overdue detail list current
- [ ] External links to S2 and S3 working
- [ ] Critical overdue count matches S3
- [ ] Conditional formatting applied correctly


### Sheet 4: Gap Register Quality

- [ ] All gaps from S1, S2, S3 captured
- [ ] No duplicate gap IDs
- [ ] All gaps have assigned owners
- [ ] All gaps have target dates
- [ ] Overdue gaps highlighted (target date < today, status not Closed)
- [ ] Closed gaps have closure dates and evidence
- [ ] Accepted gaps have approval documentation
- [ ] Priority assignments appropriate
- [ ] Status values valid (Open/In Progress/Closed/Accepted only)
- [ ] No blank required fields


### Sheet 5: Trend Analysis Quality

- [ ] Data entered for all available months
- [ ] Values within valid range (0-100%)
- [ ] No data entry errors (e.g., 800 instead of 80)
- [ ] Trend direction logical (no unexplained large swings)
- [ ] Charts displaying correctly
- [ ] Chart axes scaled appropriately
- [ ] Notes provided for significant changes
- [ ] At least 3 months data for meaningful trend


### Sheet 6: Audit Evidence Quality

- [ ] All source assessment files listed
- [ ] File locations accurate and accessible
- [ ] Last updated dates current
- [ ] Status (Current/Outdated) accurate
- [ ] Evidence registers referenced
- [ ] Gap closure evidence documented
- [ ] Approval documentation listed
- [ ] Evidence retention periods noted


### Source Data Verification

- [ ] S1 (Cabling Security) updated within last 90 days
- [ ] S2 (Equipment Maintenance) updated within last 90 days
- [ ] S3 (Maintenance Schedule) updated within last 30 days
- [ ] External links refresh successfully
- [ ] Source file versions match expected
- [ ] No pending updates to source assessments


### Overall Dashboard Quality

- [ ] Workbook opens without errors
- [ ] All sheets accessible
- [ ] External links prompt for update on open
- [ ] Conditional formatting working throughout
- [ ] Print areas set correctly for reporting
- [ ] Version date current
- [ ] Backup copy exists
- [ ] File stored in designated location


---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.12-13.S4_Compliance_Dashboard_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a712_4_compliance_dashboard.py)

**Sheet Count:** 6 worksheets

**Styling:** Navy blue headers, colour-coded status indicators, charts

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type |
|---------|------------|---------|------|
| 1 | Executive Summary | High-level compliance overview | Dashboard |
| 2 | Cabling Security | A.7.12 domain compliance | Formula-driven |
| 3 | Equipment Maintenance | A.7.13 domain compliance | Formula-driven |
| 4 | Gap Register | All gaps with remediation status | Data Entry |
| 5 | Trend Analysis | Historical compliance data | Data Entry + Charts |
| 6 | Audit Evidence | Evidence pack summary | Reference |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Executive Summary

**Purpose:** One-page executive view of infrastructure compliance

**Structure:**

**Section A: Overall Compliance (Rows 1-10)**

| Row | Content | Style |
|-----|---------|-------|
| 1 | Header: "A.7.12-13 Infrastructure Compliance Dashboard" | Navy blue |
| 3 | Assessment Period | Input |
| 5 | Overall Compliance Score | Large number, colour-coded |
| 6 | Status: Excellent/Good/Acceptable/Non-Compliant | Text |
| 8 | Cabling Security Score (40%) | Medium number |
| 9 | Equipment Maintenance Score (60%) | Medium number |


**Section B: Domain Summary (Rows 12-25)**

| Row | Content |
|-----|---------|
| 12 | Header: "Domain Breakdown" |
| 14-17 | Cabling: Pathways, Protection, Access, Documentation |
| 19-22 | Maintenance: Schedule, Programme, Personnel, Security |


**Section C: Key Indicators (Rows 27-40)**

| Row | Content |
|-----|---------|
| 27 | Header: "Key Risk Indicators" |
| 29 | Critical Overdue Count |
| 30 | Unprotected Cabling % |
| 31 | Remote Access Gaps |
| 33 | Header: "Gap Summary" |
| 34 | Open Gaps (Critical/High/Medium/Low) |
| 36 | Oldest Open Gap (days) |


**Section D: Charts (Columns F-L)**

- Compliance gauge chart
- Domain comparison bar chart
- 6-month trend line chart


### Sheet 2: Cabling Security

**Purpose:** Detailed A.7.12 compliance breakdown

**Structure:**

**Section A: Score Summary (Rows 1-15)**

| Metric | Weight | Score | Status |
|--------|--------|-------|--------|
| Cable Pathways | 30% | Formula | Colour |
| Physical Protection | 25% | Formula | Colour |
| Access Controls | 25% | Formula | Colour |
| Documentation | 20% | Formula | Colour |
| **Domain Score** | 100% | **Weighted** | **Colour** |


**Section B: Detailed Metrics (Rows 17-40)**

- Pathways: Total, Compliant, Partial, Non-Compliant
- Protection: Total areas, Protected, Partially protected, Unprotected
- Access: Total locations, Secured, Partial, Unsecured
- Documentation: Total docs, Current, Outdated, Missing


**Section C: Gap List (Rows 42+)**

- List of non-compliant items from S1


**External Links:**

```excel
=COUNTIF('[ISMS-IMP-A.7.12-13.S1_Cabling_Security.xlsx]Cable Pathways'!L:L,"✅ Compliant")
```


### Sheet 3: Equipment Maintenance

**Purpose:** Detailed A.7.13 compliance breakdown

**Structure:**

**Section A: Score Summary**

| Metric | Weight | Score | Status |
|--------|--------|-------|--------|
| Schedule Compliance | 40% | Formula | Colour |
| Maintenance Programme | 30% | Formula | Colour |
| Personnel Verification | 15% | Formula | Colour |
| Security Controls | 15% | Formula | Colour |
| **Domain Score** | 100% | **Weighted** | **Colour** |


**Section B: Schedule Metrics**

- Total equipment in programme
- Current: X (X%)
- Due Soon: X (X%)
- Overdue: X (X%)
- Critical Overdue: X


**Section C: Overdue Detail**

- List of overdue equipment from S3
- Days overdue
- Escalation status


**External Links:**

```excel
=COUNTIF('[ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule.xlsx]Equipment Schedule'!K:K,"✅ Current")
```


### Sheet 4: Gap Register

**Purpose:** Central gap tracking and remediation management

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Gap ID | Text | 12 | Auto-generate |
| B | Source | Dropdown | 15 | S1, S2, S3 |
| C | Description | Text | 50 | None |
| D | Priority | Dropdown | 12 | Critical, High, Medium, Low |
| E | Owner | Text | 20 | None |
| F | Identified Date | Date | 15 | Date |
| G | Target Date | Date | 15 | Date |
| H | Status | Dropdown | 15 | Open, In Progress, Closed, Accepted |
| I | Remediation Plan | Text | 50 | None |
| J | Evidence | Text | 30 | None |
| K | Closure Date | Date | 15 | Date |
| L | Notes | Text | 40 | None |

**Conditional Formatting:**

- Priority Critical: Red background
- Priority High: Orange background
- Status Overdue (Target Date < Today AND Status not Closed): Red text


### Sheet 5: Trend Analysis

**Purpose:** Track compliance trends over time

**Structure:**

**Section A: Monthly Data Entry (Rows 1-20)**

| Month | Overall % | Cabling % | Maintenance % | Open Gaps | Notes |
|-------|-----------|-----------|---------------|-----------|-------|
| Jan 2026 | Input | Input | Input | Input | Input |
| Feb 2026 | Input | Input | Input | Input | Input |
| ... | ... | ... | ... | ... | ... |


**Section B: Trend Charts (Rows 22+)**

- Line chart: Compliance trend (Overall, Cabling, Maintenance)
- Bar chart: Gap count trend


### Sheet 6: Audit Evidence

**Purpose:** Summary of evidence for audit

**Structure:**

**Assessment Evidence:**

| Assessment | File Name | Location | Last Updated | Status |
|------------|-----------|----------|--------------|--------|
| S1 - Cabling | ISMS-IMP-A.7.12-13.S1_*.xlsx | [Path] | [Date] | Current/Outdated |
| S2 - Maintenance | ISMS-IMP-A.7.12-13.S2_*.xlsx | [Path] | [Date] | Current/Outdated |
| S3 - Schedule | ISMS-IMP-A.7.12-13.S3_*.xlsx | [Path] | [Date] | Current/Outdated |


**Supporting Evidence:**

- Evidence registers from S1, S2, S3
- Gap closure evidence
- Approval documentation

---

## External Workbook Links

### Link Configuration

**Source Files Must Be Named:**

- ISMS-IMP-A.7.12-13.S1_Cabling_Security.xlsx
- ISMS-IMP-A.7.12-13.S2_Equipment_Maintenance.xlsx
- ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule.xlsx

**Location:**

All files should be in same directory as dashboard for links to work.

**Link Formulas:**

```excel
' Cabling Pathways Compliant
=[ISMS-IMP-A.7.12-13.S1_Cabling_Security.xlsx]'Summary Dashboard'!B5

' Maintenance Schedule Compliance
=[ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule.xlsx]Dashboard!B3

' Equipment Overdue Count
=[ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule.xlsx]Dashboard!B7
```

**Link Update:**

- Open dashboard, click "Update Links" when prompted
- Or: Data → Edit Links → Update Values

---

## Cell Styling Reference

### Colour Palette

**Headers:**

- Primary: #003366 (Navy blue)
- Section: #4472C4 (Medium blue)

**Status Colours:**

- Excellent (≥90%): #C6EFCE (Light green)
- Good (75-89%): #FFEB9C (Light amber)
- Acceptable (60-74%): #FFD966 (Yellow)
- Non-Compliant (<60%): #FFC7CE (Light red)

**Priority Colours:**

- Critical: #FFC7CE (Light red)
- High: #FFE4B5 (Light orange)
- Medium: #FFFFCC (Light yellow)
- Low: #FFFFFF (White)

---

## Integration Points

### Integration with Source Assessments

| Dashboard Element | Source | Link Type |
|-------------------|--------|-----------|
| Cabling Scores | S1 Sheets 2-5 | External formula |
| Maintenance Scores | S2 Sheets 2-6 | External formula |
| Schedule Compliance | S3 Sheet 2, 5 | External formula |
| Gap Details | S1, S2, S3 Gap lists | Manual consolidation |

### Integration with ISMS

**Feeds Into:**

- Management Review reporting
- Internal Audit planning
- Risk Register (high-priority gaps)
- Corrective Action Register

**Related Controls:**

- A.7.4-5-11 (Physical Infrastructure) - Related physical controls
- A.5.9 (Asset Management) - Equipment inventory
- A.8.32 (Change Management) - Infrastructure changes


---

## Formula Reference

### Overall Compliance Calculation

**Overall Score Formula:**

```excel
=B8*0.4+B9*0.6
```
Where B8 = Cabling Security Score, B9 = Equipment Maintenance Score

**Status Determination:**

```excel
=IF(B5>=90,"Excellent",IF(B5>=75,"Good",IF(B5>=60,"Acceptable","Non-Compliant")))
```


### Cabling Security Domain Formulas

**Domain Score:**

```excel
=(PathwaysScore*0.3)+(ProtectionScore*0.25)+(AccessScore*0.25)+(DocumentationScore*0.2)
```

**Sub-Domain Scores:**

```excel
' Pathways Compliance
=IFERROR(COUNTIF('[S1]Cable Pathways'!L:L,"Compliant")/COUNTA('[S1]Cable Pathways'!A:A)*100,0)

' Protection Score
=IFERROR(COUNTIF('[S1]Physical Protection'!H:H,"Protected")/COUNTA('[S1]Physical Protection'!A:A)*100,0)

' Access Control Score
=IFERROR(COUNTIF('[S1]Access Controls'!G:G,"Secured")/COUNTA('[S1]Access Controls'!A:A)*100,0)

' Documentation Score
=IFERROR(COUNTIF('[S1]Documentation'!E:E,"Current")/COUNTA('[S1]Documentation'!A:A)*100,0)
```


### Equipment Maintenance Domain Formulas

**Domain Score:**

```excel
=(ScheduleScore*0.4)+(ProgrammeScore*0.3)+(PersonnelScore*0.15)+(SecurityScore*0.15)
```

**Sub-Domain Scores:**

```excel
' Schedule Compliance
=IFERROR('[S3]Dashboard'!B3,0)

' Programme Coverage
=IFERROR(COUNTIF('[S2]Equipment Inventory'!F:F,"In Programme")/COUNTA('[S2]Equipment Inventory'!A:A)*100,0)

' Personnel Verification
=IFERROR(COUNTIF('[S2]Personnel'!E:E,"Verified")/COUNTA('[S2]Personnel'!A:A)*100,0)

' Security Controls
=IFERROR(COUNTIF('[S2]Security Controls'!G:G,"Compliant")/COUNTA('[S2]Security Controls'!A:A)*100,0)
```


### Gap Register Formulas

**Gap Count by Priority:**

```excel
' Critical Gaps
=COUNTIF('Gap Register'!D:D,"Critical")

' High Gaps
=COUNTIF('Gap Register'!D:D,"High")

' Open Gaps Total
=COUNTIFS('Gap Register'!H:H,"<>Closed",'Gap Register'!H:H,"<>Accepted")
```

**Oldest Open Gap:**

```excel
=IFERROR(TODAY()-MIN(IF('Gap Register'!H:H<>"Closed",'Gap Register'!F:F)),0)
```
(Enter as array formula with Ctrl+Shift+Enter)

**Overdue Gap Highlighting:**

```excel
=AND(G2<TODAY(),H2<>"Closed",H2<>"Accepted")
```


### Trend Analysis Formulas

**Month-over-Month Change:**

```excel
=B3-B2
```

**Trend Direction:**

```excel
=IF(B3>B2,"↑",IF(B3<B2,"↓","→"))
```

**Rolling 3-Month Average:**

```excel
=AVERAGE(B2:B4)
```


---

## Conditional Formatting Specifications

### Executive Summary Score Colours

**Overall Score (Cell B5):**

| Score Range | Background | Font Colour |
|-------------|------------|-------------|
| ≥90 | #C6EFCE (Light green) | #006100 (Dark green) |
| 75-89 | #FFEB9C (Light amber) | #9C6500 (Dark amber) |
| 60-74 | #FFD966 (Yellow) | #9C5700 (Brown) |
| <60 | #FFC7CE (Light red) | #9C0006 (Dark red) |

**Domain Scores (Cells B8, B9):**

Apply same colour rules as Overall Score.


### Gap Register Formatting

**Priority Column (D):**

| Priority | Background |
|----------|------------|
| Critical | #FFC7CE (Light red) |
| High | #FFE4B5 (Light orange) |
| Medium | #FFFFCC (Light yellow) |
| Low | #FFFFFF (White) |

**Overdue Gap Row:**

```
Condition: =AND($G2<TODAY(),$H2<>"Closed",$H2<>"Accepted")
Format: Red italic font, light red background
```


### Trend Chart Formatting

**Compliance Line Chart:**

| Series | Colour | Line Width |
|--------|--------|------------|
| Overall | #003366 (Navy) | 2.5pt |
| Cabling | #4472C4 (Blue) | 1.5pt |
| Maintenance | #70AD47 (Green) | 1.5pt |

**Target Line:**

| Element | Colour | Style |
|---------|--------|-------|
| 90% Target | #FF0000 (Red) | Dashed |


---

## Data Validation Rules

### Gap Register Validations

**Source Field (Column B):**

```
Type: List
Source: S1,S2,S3
Allow blank: No
Error: Source must be S1, S2, or S3
```

**Priority Field (Column D):**

```
Type: List
Source: Critical,High,Medium,Low
Allow blank: No
Error: Select valid priority level
```

**Status Field (Column H):**

```
Type: List
Source: Open,In Progress,Closed,Accepted
Allow blank: No
Error: Select valid status
```

**Date Fields (Columns F, G, K):**

```
Type: Date
Operator: Greater than or equal to
Formula: =DATE(2020,1,1)
Error: Enter valid date in DD.MM.YYYY format
```


### Trend Analysis Validations

**Compliance Percentage Fields:**

```
Type: Decimal
Operator: Between
Minimum: 0
Maximum: 100
Error: Compliance must be between 0 and 100%
```

**Gap Count Fields:**

```
Type: Whole number
Operator: Greater than or equal to
Formula: 0
Error: Gap count must be zero or positive
```


---

## Print Settings

### Executive Summary Print Area

- Range: A1:L45
- Orientation: Landscape
- Fit to: 1 page wide by 1 page tall
- Margins: Normal
- Include gridlines: No
- Include headers: Yes (page numbers)

### Gap Register Print Area

- Range: A1:L (all rows with data)
- Orientation: Landscape
- Fit to: 1 page wide
- Repeat rows at top: Row 1 (headers)
- Include gridlines: Yes

### Trend Analysis Print Area

- Range: A1:F25 (data) + Charts
- Orientation: Portrait
- Fit to: 1 page wide by 2 pages tall
- Include charts: Yes


---

## Error Handling

### External Link Errors

**When Source Files Not Found:**

- Formulas display #REF! error
- Status shows "Link Error" text via IFERROR wrapper
- Manual intervention required to reconnect links

**IFERROR Wrapper Pattern:**

```excel
=IFERROR('[S1]Sheet'!Cell,"Link Error - Check Source File")
```


### Division by Zero Prevention

**All Percentage Calculations:**

```excel
=IFERROR(numerator/denominator*100,0)
```
Returns 0 if denominator is zero.


### Missing Data Handling

**When Source Data Not Available:**

- Use "N/A" text for display
- Exclude from calculations using IFERROR
- Flag in Notes for investigation


---

**END OF SPECIFICATION**

---

*"You cannot improve what you cannot measure."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-03 -->

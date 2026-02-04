**ISMS-IMP-A.7.8-9-S3: Equipment Protection Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Controls A.7.8 & A.7.9: Equipment Siting and Protection

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.8-9-S3 |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Dashboard - Equipment Siting (A.7.8) and Off-Premises Security (A.7.9) |
| **Related Policy** | ISMS-POL-A.7.8-9 (Equipment Siting and Protection) |
| **Purpose** | Provide consolidated compliance view across equipment siting and off-premises security, track gaps, and monitor remediation |
| **Target Audience** | CISO, Compliance Officers, Security Management, Internal Audit, Executive Management |
| **Assessment Type** | Management Dashboard |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial dashboard specification for Equipment Protection compliance | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Dashboard Overview
  - Prerequisites
  - Using the Dashboard
  - Interpreting Metrics
  - Gap Management
  - Reporting

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Data Integration
  - Formula Reference
  - Automation

---

# PART I: USER COMPLETION GUIDE

## Dashboard Overview

### Purpose & Scope

**Dashboard Name:** ISMS-IMP-A.7.8-9-S3 - Equipment Protection Compliance Dashboard

#### What This Dashboard Provides

This dashboard consolidates compliance data from the Equipment Siting (A.7.8-9-S1) and Off-Premises Asset Security (A.7.8-9-S2) assessments into a single executive view. It answers:

- What is our overall equipment protection compliance score?
- Which areas have the highest compliance gaps?
- What remediation actions are required?
- How are we trending over time?
- Are we audit-ready?

#### Key Principle

This dashboard **aggregates data from source assessments** - it does not replace detailed assessments. Use S1 (Equipment Siting) and S2 (Off-Premises Assets) for detailed findings; use this dashboard for executive reporting and strategic planning.

#### What the Dashboard Shows

**Overall Compliance Score:**

- Combined score for A.7.8 and A.7.9 compliance
- Colour-coded status (Green >90%, Amber 75-89%, Red <75%)
- Trend over last 4 quarters

**Control Area Scores:**

- Equipment Siting (A.7.8) - locations, environment, security, power
- Off-Premises Security (A.7.9) - authorisation, protection, remote work, permanent installations

**Gap Summary:**

- Critical and high priority gaps requiring attention
- Gap aging (how long gaps have been open)
- Remediation status and target dates

**Incident Metrics:**

- Equipment security incidents (loss, theft, damage)
- Incident trends over time
- Recovery rates

**Audit Readiness:**

- Documentation completeness
- Evidence availability
- Assessment currency

### Who Should Use This Dashboard

#### Primary Users

1. **CISO** - Strategic oversight and resource allocation
2. **Compliance Officers** - Audit preparation and regulatory reporting
3. **Security Management** - Operational monitoring and remediation tracking
4. **Internal Audit** - Control effectiveness assessment
5. **Executive Management** - Risk awareness and governance

#### Use Cases

- **Quarterly Management Review** - Present overall compliance status
- **Audit Preparation** - Identify and close gaps before audit
- **Board Reporting** - High-level security posture reporting
- **Budget Justification** - Support remediation investment requests
- **Trend Analysis** - Track improvement over time

---

## Prerequisites

### Source Assessments Required

This dashboard requires completed assessments:

1. **ISMS-IMP-A.7.8-9-S1** (Equipment Siting Assessment)
   - Equipment location inventory
   - Environmental assessment
   - Physical security evaluation
   - Power infrastructure review
   - Workstation security assessment

2. **ISMS-IMP-A.7.8-9-S2** (Off-Premises Asset Security Assessment)
   - Equipment inventory for off-premises use
   - Authorisation and tracking processes
   - Protection measures assessment
   - Remote working evaluation
   - Permanent installation review
   - Incident documentation

### Data Integration Options

**Option 1: Manual Data Entry**

- Enter summary data from S1 and S2 assessments manually
- Suitable for initial setup or low-volume updates
- Time required: 30-45 minutes per update

**Option 2: External Workbook Links**

- Link to S1 and S2 workbook files
- Automatic data refresh when source files updated
- Requires files in same directory or accessible network location
- Time required: 5-10 minutes per update (verify links)

**Option 3: Automated Data Collection**

- Python script consolidates data from source assessments
- Scheduled execution for regular updates
- Time required: Configuration only, then automatic

---

## Using the Dashboard

### Dashboard Navigation

**Sheet 1: Executive Summary**

- Overall compliance score and trend
- Key metrics at a glance
- Critical alerts and actions required

**Sheet 2: Control Area Details**

- Breakdown by control area (Equipment Siting, Off-Premises)
- Sub-domain scores (Environment, Security, Power, etc.)
- Comparison against targets

**Sheet 3: Gap Register**

- All identified compliance gaps
- Priority, owner, due date, status
- Gap aging and escalation indicators

**Sheet 4: Incident Tracker**

- Equipment security incidents
- Trend analysis
- Lessons learned

**Sheet 5: Remediation Plan**

- Planned remediation actions
- Resource requirements
- Timeline and milestones

**Sheet 6: Audit Readiness**

- Documentation checklist
- Evidence availability
- Assessment currency

**Sheet 7: Trend Analysis**

- Historical compliance scores
- Quarter-over-quarter comparison
- Improvement trajectory

**Sheet 8: Data Input**

- Manual data entry for source assessment results
- OR external workbook link configuration

### Updating the Dashboard

**Quarterly Update Process:**

1. Ensure S1 and S2 assessments are current
2. Update data in Sheet 8 (manual or verify links)
3. Review Sheet 1 for overall score
4. Update gap status in Sheet 3
5. Update incident data in Sheet 4
6. Adjust remediation plan in Sheet 5 as needed
7. Generate reports for management review

---

## Interpreting Metrics

### Overall Compliance Score

**Score Calculation:**

```
Overall Score = (A.7.8 Score x 50%) + (A.7.9 Score x 50%)
```

**Thresholds:**

| Score | Status | Interpretation |
|-------|--------|----------------|
| >90% | Green - Compliant | Meets all requirements, minor improvements only |
| 75-89% | Amber - Partial | Most requirements met, remediation needed |
| 60-74% | Amber - Attention | Significant gaps, prioritised remediation required |
| <60% | Red - Non-Compliant | Major gaps, immediate action required |

### Control Area Scores

**A.7.8 Equipment Siting Score Components:**

| Component | Weight | Source |
|-----------|--------|--------|
| Equipment Locations | 25% | S1 Sheet 2 |
| Environmental Assessment | 25% | S1 Sheet 3 |
| Physical Security | 25% | S1 Sheet 4 |
| Power Infrastructure | 15% | S1 Sheet 5 |
| Workstation Security | 10% | S1 Sheet 6 |

**A.7.9 Off-Premises Security Score Components:**

| Component | Weight | Source |
|-----------|--------|--------|
| Equipment Inventory | 20% | S2 Sheet 2 |
| Authorisation & Tracking | 20% | S2 Sheet 3 |
| Protection Measures | 25% | S2 Sheet 4 |
| Remote Working | 20% | S2 Sheet 5 |
| Permanent Installations | 15% | S2 Sheet 6 |

### Gap Priority Levels

| Priority | Definition | Target Remediation |
|----------|------------|-------------------|
| Critical | Significant risk of data breach or regulatory non-compliance | 30 days |
| High | Material gap that could impact audit outcome | 60 days |
| Medium | Process improvement opportunity | 90 days |
| Low | Minor enhancement or documentation improvement | 180 days |

### Incident Metrics

**Key Metrics:**

- **Loss Rate**: Equipment losses per 1,000 devices per year
- **Recovery Rate**: Percentage of lost devices recovered
- **Mean Time to Report**: Average hours from incident to report
- **Remote Wipe Success Rate**: Percentage of successful remote wipes

---

## Gap Management

### Gap Identification

Gaps are identified from:

1. Non-compliant items in S1 and S2 assessments (Red status)
2. Partial compliance items requiring attention (Amber status)
3. Audit findings and recommendations
4. Incident root cause analysis
5. Policy changes requiring implementation

### Gap Register Fields

| Field | Description |
|-------|-------------|
| Gap ID | Unique identifier (GAP-001, GAP-002) |
| Control Area | A.7.8 or A.7.9 |
| Sub-domain | Specific area (Environment, Security, Remote Work, etc.) |
| Description | Clear description of the gap |
| Risk Impact | Business impact if gap not addressed |
| Priority | Critical, High, Medium, Low |
| Owner | Person responsible for remediation |
| Target Date | Planned completion date |
| Status | Open, In Progress, Completed, Deferred |
| Evidence | Documentation that gap has been closed |

### Gap Remediation Workflow

```
1. GAP IDENTIFIED
   |
2. PRIORITY ASSIGNED (based on risk)
   |
3. OWNER ASSIGNED
   |
4. REMEDIATION PLAN DEVELOPED
   |
5. IMPLEMENTATION
   |
6. VERIFICATION
   |
7. GAP CLOSED
   |
8. EVIDENCE DOCUMENTED
```

### Gap Escalation

**Escalation Triggers:**

- Gap past target date by >30 days
- Critical gap open >60 days
- High gap open >90 days
- Resource constraints blocking remediation

**Escalation Path:**

- Day 30 overdue: Notify gap owner and their manager
- Day 60 overdue: Escalate to CISO
- Day 90 overdue: Escalate to Executive Management

---

## Reporting

### Standard Reports

**1. Executive Summary Report**

- Audience: Executive Management, Board
- Frequency: Quarterly
- Content: Overall score, key metrics, critical gaps, remediation progress

**2. Compliance Status Report**

- Audience: CISO, Compliance Officers
- Frequency: Monthly
- Content: Detailed scores by control area, gap status, incident summary

**3. Gap Remediation Report**

- Audience: Security Management, IT Operations
- Frequency: Weekly/Monthly
- Content: Open gaps, status updates, resource requirements

**4. Audit Readiness Report**

- Audience: Compliance Officers, Internal Audit
- Frequency: Pre-audit
- Content: Documentation completeness, evidence availability, gap closure status

### Report Generation

**From Dashboard:**

1. Navigate to relevant sheet
2. Apply filters if needed
3. Print or export to PDF

**Automated Reports:**

- Configure Python script for scheduled report generation
- Email distribution to stakeholders

---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.8-9.S3_Compliance_Dashboard_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a78_3_compliance_dashboard.py)

**Sheet Count:** 8 worksheets

**Styling:** Navy blue headers, colour-coded compliance status, charts for visual presentation

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type |
|---------|------------|---------|------|
| 1 | Executive Summary | High-level compliance overview | Dashboard |
| 2 | Control Area Details | Breakdown by control domain | Dashboard |
| 3 | Gap Register | Compliance gaps tracking | Data Entry |
| 4 | Incident Tracker | Equipment security incidents | Data Entry |
| 5 | Remediation Plan | Planned remediation actions | Data Entry |
| 6 | Audit Readiness | Documentation and evidence checklist | Checklist |
| 7 | Trend Analysis | Historical compliance data | Charts |
| 8 | Data Input | Source data from S1 and S2 | Data Entry |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Executive Summary

**Purpose:** High-level compliance overview for executive audience

**Structure:**

**Row 1:** Header
- "ISMS Equipment Protection Compliance Dashboard"
- "ISO/IEC 27001:2022 Controls A.7.8 & A.7.9"

**Rows 3-8:** Overall Compliance Score
- Large font display of overall percentage
- Colour-coded background (Green/Amber/Red)
- Status text (Compliant/Partial/Non-Compliant)
- Trend arrow (up/down/stable)

**Rows 10-18:** Key Metrics Summary
- A.7.8 Equipment Siting Score
- A.7.9 Off-Premises Security Score
- Total Open Gaps (Critical/High/Medium/Low)
- Incidents This Quarter
- Audit Readiness Status

**Rows 20-30:** Critical Alerts
- Critical gaps requiring immediate attention
- Overdue remediation items
- Upcoming audit milestones

**Rows 32-45:** Compliance Trend Chart
- Line chart showing quarterly scores
- Last 4 quarters displayed

### Sheet 2: Control Area Details

**Purpose:** Detailed breakdown by control domain

**Structure:**

**A.7.8 Equipment Siting Section:**

| Sub-domain | Score | Items Assessed | Compliant | Partial | Non-Compliant |
|------------|-------|----------------|-----------|---------|---------------|
| Equipment Locations | Formula | Formula | Formula | Formula | Formula |
| Environmental Assessment | Formula | Formula | Formula | Formula | Formula |
| Physical Security | Formula | Formula | Formula | Formula | Formula |
| Power Infrastructure | Formula | Formula | Formula | Formula | Formula |
| Workstation Security | Formula | Formula | Formula | Formula | Formula |
| **A.7.8 Total** | **Formula** | **Formula** | **Formula** | **Formula** | **Formula** |

**A.7.9 Off-Premises Security Section:**

| Sub-domain | Score | Items Assessed | Compliant | Partial | Non-Compliant |
|------------|-------|----------------|-----------|---------|---------------|
| Equipment Inventory | Formula | Formula | Formula | Formula | Formula |
| Authorisation & Tracking | Formula | Formula | Formula | Formula | Formula |
| Protection Measures | Formula | Formula | Formula | Formula | Formula |
| Remote Working | Formula | Formula | Formula | Formula | Formula |
| Permanent Installations | Formula | Formula | Formula | Formula | Formula |
| **A.7.9 Total** | **Formula** | **Formula** | **Formula** | **Formula** | **Formula** |

### Sheet 3: Gap Register

**Purpose:** Track all compliance gaps

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Gap ID | Text | 12 | None |
| B | Control | Dropdown | 12 | A.7.8, A.7.9 |
| C | Sub-domain | Text | 25 | None |
| D | Description | Text | 50 | None |
| E | Risk Impact | Text | 40 | None |
| F | Priority | Dropdown | 12 | Critical, High, Medium, Low |
| G | Owner | Text | 20 | None |
| H | Identified Date | Date | 12 | Date |
| I | Target Date | Date | 12 | Date |
| J | Status | Dropdown | 15 | Open, In Progress, Completed, Deferred |
| K | Days Open | Formula | 12 | Yes |
| L | Overdue | Formula | 10 | Yes |
| M | Evidence Reference | Text | 25 | None |
| N | Notes | Text | 40 | None |

**Formulas:**

- Days Open: `=IF(J2="Completed",DATEDIF(H2,TODAY(),"d"),DATEDIF(H2,TODAY(),"d"))`
- Overdue: `=IF(AND(J2<>"Completed",I2<TODAY()),"Yes","No")`

### Sheet 4: Incident Tracker

**Purpose:** Track equipment security incidents

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Incident ID | Text | 12 | None |
| B | Date | Date | 12 | Date |
| C | Equipment Type | Dropdown | 18 | Laptop, Mobile, Tablet, Storage, Edge Device, Other |
| D | Incident Type | Dropdown | 15 | Lost, Stolen, Damaged, Compromised |
| E | Location | Text | 20 | None |
| F | Data Sensitivity | Dropdown | 15 | High, Medium, Low, None |
| G | Remote Wipe | Dropdown | 18 | Yes-Success, Yes-Failed, No-Not Needed, No-Not Possible |
| H | Hours to Report | Number | 15 | Integer |
| I | Recovery Status | Dropdown | 15 | Recovered, Not Recovered, Replaced, Insurance |
| J | Root Cause | Text | 30 | None |
| K | Lesson Learned | Text | 40 | None |

**Summary Metrics (calculated):**

- Total Incidents This Quarter
- Incidents by Type (pie chart)
- Average Time to Report
- Recovery Rate
- Remote Wipe Success Rate

### Sheet 5: Remediation Plan

**Purpose:** Track planned remediation actions

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Action ID | Text | 12 | None |
| B | Related Gap ID | Text | 12 | None |
| C | Description | Text | 50 | None |
| D | Action Type | Dropdown | 18 | Technical, Process, Training, Documentation |
| E | Owner | Text | 20 | None |
| F | Start Date | Date | 12 | Date |
| G | Target Date | Date | 12 | Date |
| H | Status | Dropdown | 15 | Not Started, In Progress, Completed, Blocked |
| I | % Complete | Number | 12 | Integer 0-100 |
| J | Resources Required | Text | 30 | None |
| K | Cost Estimate | Number | 15 | Currency |
| L | Notes | Text | 40 | None |

### Sheet 6: Audit Readiness

**Purpose:** Checklist for audit preparation

**Structure:**

**Documentation Checklist:**

| Document | Required | Available | Current | Evidence Location |
|----------|----------|-----------|---------|-------------------|
| Equipment Siting Policy (ISMS-POL-A.7.8-9) | Yes | Dropdown | Dropdown | Text |
| Equipment Siting Assessment (S1) | Yes | Dropdown | Dropdown | Text |
| Off-Premises Security Assessment (S2) | Yes | Dropdown | Dropdown | Text |
| Equipment Removal Authorisation Forms | Yes | Dropdown | Dropdown | Text |
| Remote Working Policy | Yes | Dropdown | Dropdown | Text |
| MDM Compliance Reports | Yes | Dropdown | Dropdown | Text |
| Environmental Monitoring Reports | Yes | Dropdown | Dropdown | Text |
| Physical Security Incident Reports | Yes | Dropdown | Dropdown | Text |
| Equipment Loss/Theft Reports | Yes | Dropdown | Dropdown | Text |
| UPS and Generator Test Records | Yes | Dropdown | Dropdown | Text |

**Audit Readiness Score:**

- Formula calculates percentage of items with "Yes" for Available and Current

### Sheet 7: Trend Analysis

**Purpose:** Historical compliance data and trends

**Structure:**

**Quarterly Compliance Data:**

| Quarter | A.7.8 Score | A.7.9 Score | Overall Score | Open Gaps | Incidents |
|---------|-------------|-------------|---------------|-----------|-----------|
| Q1 2025 | Input | Input | Formula | Input | Input |
| Q2 2025 | Input | Input | Formula | Input | Input |
| Q3 2025 | Input | Input | Formula | Input | Input |
| Q4 2025 | Input | Input | Formula | Input | Input |
| Q1 2026 | Input | Input | Formula | Input | Input |

**Charts:**

- Line chart: Compliance score trend over time
- Bar chart: Gap closure rate per quarter
- Line chart: Incident trend over time

### Sheet 8: Data Input

**Purpose:** Source data entry from S1 and S2 assessments

**Structure:**

**A.7.8 Equipment Siting Data (from S1):**

| Sub-domain | Items Assessed | Compliant | Partial | Non-Compliant |
|------------|----------------|-----------|---------|---------------|
| Equipment Locations | Input | Input | Input | Input |
| Environmental Assessment | Input | Input | Input | Input |
| Physical Security | Input | Input | Input | Input |
| Power Infrastructure | Input | Input | Input | Input |
| Workstation Security | Input | Input | Input | Input |

**A.7.9 Off-Premises Security Data (from S2):**

| Sub-domain | Items Assessed | Compliant | Partial | Non-Compliant |
|------------|----------------|-----------|---------|---------------|
| Equipment Inventory | Input | Input | Input | Input |
| Authorisation & Tracking | Input | Input | Input | Input |
| Protection Measures | Input | Input | Input | Input |
| Remote Working | Input | Input | Input | Input |
| Permanent Installations | Input | Input | Input | Input |

**External Workbook Links (Optional):**

```excel
='[ISMS-IMP-A.7.8.S1_Equipment_Siting.xlsx]Summary Dashboard'!B5
='[ISMS-IMP-A.7.9.S2_Off_Premises_Assets.xlsx]Summary Dashboard'!B5
```

---

## Cell Styling Reference

### Colour Palette

**Headers:**

- Primary Header: #003366 (Navy blue), #FFFFFF (White text)
- Section Header: #4472C4 (Medium blue), #FFFFFF (White text)

**Compliance Status:**

- >90% Compliant: #C6EFCE (Light green)
- 75-89% Partial: #FFEB9C (Light amber)
- <75% Non-Compliant: #FFC7CE (Light red)

**Gap Priority:**

- Critical: #FF0000 (Red text)
- High: #FFA500 (Orange text)
- Medium: #0000FF (Blue text)
- Low: #808080 (Gray text)

**Overdue Indicators:**

- Overdue: #FFC7CE background (Light red)
- Due within 7 days: #FFEB9C background (Light amber)
- On track: #FFFFFF background (White)

### Font Specifications

**Dashboard Metrics:**

- Font: Calibri
- Size: 24pt for scores, 12pt for labels
- Weight: Bold for scores

**Data Tables:**

- Font: Calibri
- Size: 10pt
- Weight: Normal

---

## Integration Points

### Data Sources

**From S1 (Equipment Siting Assessment):**

- Sheet 2: Equipment Locations - compliance counts
- Sheet 3: Environmental Assessment - compliance counts
- Sheet 4: Physical Security - compliance counts
- Sheet 5: Power Infrastructure - compliance counts
- Sheet 6: Workstation Security - compliance counts
- Sheet 8: Summary Dashboard - aggregated scores

**From S2 (Off-Premises Asset Security Assessment):**

- Sheet 2: Equipment Inventory - compliance counts
- Sheet 3: Authorisation & Tracking - compliance counts
- Sheet 4: Protection Measures - compliance counts
- Sheet 5: Remote Working - compliance counts
- Sheet 6: Permanent Off-Site - compliance counts
- Sheet 9: Summary Dashboard - aggregated scores

### Formula Reference

**Overall Compliance Score:**

```excel
=(A78_Score*0.5)+(A79_Score*0.5)
```

**A.7.8 Score:**

```excel
=('Data Input'!C5/('Data Input'!C5+'Data Input'!D5+'Data Input'!E5)+
  'Data Input'!C6/('Data Input'!C6+'Data Input'!D6+'Data Input'!E6)+
  'Data Input'!C7/('Data Input'!C7+'Data Input'!D7+'Data Input'!E7)+
  'Data Input'!C8/('Data Input'!C8+'Data Input'!D8+'Data Input'!E8)+
  'Data Input'!C9/('Data Input'!C9+'Data Input'!D9+'Data Input'!E9))/5*100
```

**Gap Overdue Count:**

```excel
=COUNTIFS('Gap Register'!J:J,"<>Completed",'Gap Register'!L:L,"Yes")
```

**Incident Rate (per 1000 devices):**

```excel
=COUNTIFS('Incident Tracker'!B:B,">="&DATE(YEAR(TODAY()),1,1))/('Data Input'!TotalDevices/1000)
```

---

## Automation

### Python Script Integration

The dashboard can be automatically populated using the consolidator script:

```
python3 consolidate_a78_dashboard.py
```

**Script Functions:**

1. Read S1 and S2 workbook files
2. Extract compliance counts from each domain
3. Calculate aggregated scores
4. Write to dashboard Data Input sheet
5. Update timestamp and version

### Scheduled Updates

Configure cron job for weekly dashboard updates:

```bash
0 6 * * 1 cd /path/to/scripts && python3 consolidate_a78_dashboard.py
```

---

**END OF SPECIFICATION**

---

*"In preparing for battle I have always found that plans are useless, but planning is indispensable."*
-- Dwight D. Eisenhower

<!-- QA_VERIFIED: 2026-02-03 -->

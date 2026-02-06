**ISMS-IMP-A.7.10.4-TG - Storage Media Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.10.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Dashboard & KPIs |
| **Related Policy** | ISMS-POL-A.7.10, Section 4 (Governance & Compliance) |
| **Purpose** | Consolidate storage media compliance data from assessments A.7.10.1-3, provide executive overview, track KPIs, and manage remediation roadmap |
| **Target Audience** | CISO, IT Management, Executive Leadership, Compliance Officers, Internal Audit |
| **Assessment Type** | Consolidated Dashboard & Executive Reporting |
| **Review Cycle** | Quarterly (minimum) or Monthly for Active Remediation |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Storage Media Compliance Dashboard | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Python Developers, Excel Workbook Designers, ISMS Implementation Technical Teams

---

# Workbook Structure Overview

## Sheet Organisation (11 Sheets Total)

| Sheet # | Sheet Name | Purpose | Linking |
|---------|------------|---------|---------|
| 1 | Instructions & Legend | Dashboard guidance | None |
| 2 | Executive Summary | High-level overview | External to A.7.10.1-3 |
| 3 | Domain 1 Summary | Inventory highlights | External to A.7.10.1 |
| 4 | Domain 2 Summary | Handling highlights | External to A.7.10.2 |
| 5 | Domain 3 Summary | Lifecycle highlights | External to A.7.10.3 |
| 6 | Consolidated Gap Analysis | All gaps | Manual consolidation |
| 7 | Risk Register | Risk tracking | Manual entry |
| 8 | Remediation Roadmap | Action tracking | Manual entry |
| 9 | Evidence Master Index | Evidence catalog | Manual + links |
| 10 | KPI Dashboard | Metrics and trends | Mixed |
| 11 | CISO Approval | Executive sign-off | Manual entry |

---

# Sheet 1: Instructions & Legend

## Layout Structure

**Header Section (Rows 1-5)**
- Document title and ID
- Dashboard date and version
- Organisation name placeholder

**Purpose Section (Rows 7-15)**
- Dashboard objectives
- Scope definition
- Related policy reference

**Legend Section (Rows 17-40)**
- Traffic light status definitions
- Risk level colour coding
- Compliance status colours
- Trend indicator meanings

**Navigation Guide (Rows 42-55)**
- Sheet descriptions
- Update responsibilities
- Contact information

**Column Width Specifications:**
| Column | Width | Content |
|--------|-------|---------|
| A | 20 | Section headers |
| B | 60 | Description text |
| C | 15 | Status/Values |

---

# Sheet 2: Executive Summary

## Layout Structure

**Section 1: Compliance Overview (Rows 3-15)**

| Cell | Content | Formula/Entry |
|------|---------|---------------|
| B5 | Overall Compliance % | External link or calculated |
| B6 | Domain 1 (Inventory) % | External link |
| B7 | Domain 2 (Handling) % | External link |
| B8 | Domain 3 (Lifecycle) % | External link |
| D5 | Status Indicator | Conditional (Green/Amber/Red) |
| D6-8 | Domain Status | Conditional |

**Section 2: Critical Metrics (Rows 17-28)**

| Metric | Source | Update |
|--------|--------|--------|
| Total Media Items | A.7.10.1 Summary | Quarterly |
| Unregistered Media | A.7.10.1 Summary | Quarterly |
| Encryption Compliance % | A.7.10.1 Summary | Quarterly |
| Disposal with Certificate % | A.7.10.3 Summary | Quarterly |
| Open Critical Gaps | Gap Analysis sheet | Monthly |
| Remediation On Track % | Roadmap sheet | Monthly |

**Section 3: Period Comparison (Rows 30-40)**

| Metric | Current | Previous | Trend |
|--------|---------|----------|-------|
| Overall Compliance | Formula | Manual | Calculated |
| Critical Gaps | Formula | Manual | Calculated |
| Remediation Progress | Formula | Manual | Calculated |

**Section 4: Executive Attention (Rows 42-55)**
- Top 3 critical items requiring attention
- Upcoming deadlines
- Resource constraints
- Key recommendations

## Conditional Formatting

**Compliance Percentage:**
- >80%: Green (#C6EFCE)
- 60-80%: Yellow (#FFEB9C)
- <60%: Red (#FFC7CE)

**Trend Indicators:**
- Improving: Green arrow up
- Stable: Yellow dash
- Declining: Red arrow down

---

# Sheet 3-5: Domain Summaries

## Standard Domain Summary Layout

**Header Section (Rows 1-5)**
- Domain title
- Source document reference
- Last updated date
- Next review date

**Compliance Metrics (Rows 7-20)**

| Metric | Cell | Source |
|--------|------|--------|
| Domain Compliance % | B9 | External or manual |
| Items Assessed | B10 | External or manual |
| Compliant Items | B11 | External or manual |
| Partial Items | B12 | External or manual |
| Non-Compliant Items | B13 | External or manual |
| N/A Items | B14 | External or manual |

**Key Findings (Rows 22-35)**
- Finding 1-5 with severity
- Evidence reference
- Remediation owner

**Domain-Specific Metrics (Rows 37-50)**
- Domain 1: Inventory metrics (registration, encryption, custody)
- Domain 2: Handling metrics (access, transport, storage)
- Domain 3: Lifecycle metrics (acquisition, re-use, disposal)

**External Formula Pattern:**
```
='[ISMS-IMP-A.7.10.1.xlsx]Summary Dashboard'!$B$10
```

---

# Sheet 6: Consolidated Gap Analysis

## Column Structure

| Column | Header | Width | Purpose |
|--------|--------|-------|---------|
| A | Gap ID | 12 | Unique identifier (GAP-001) |
| B | Source Domain | 15 | Domain 1/2/3 |
| C | Source Sheet | 20 | Original assessment sheet |
| D | Gap Description | 40 | Detailed gap description |
| E | Control Reference | 15 | A.7.10 sub-control |
| F | Risk Level | 12 | Critical/High/Medium/Low |
| G | Gap Category | 18 | Policy/Procedure/Technical/People |
| H | Current Status | 15 | Open/In Progress/Closed |
| I | Remediation Owner | 18 | Assigned person/role |
| J | Target Date | 12 | Planned closure date |
| K | Evidence Reference | 15 | Link to evidence |
| L | Notes | 30 | Additional context |

## Data Validation

**Column F - Risk Level:**
```
Dropdown: Critical, High, Medium, Low
```

**Column G - Gap Category:**
```
Dropdown: Policy Gap, Procedure Gap, Technical Gap, People Gap, Documentation Gap, Multiple
```

**Column H - Current Status:**
```
Dropdown: Open, In Progress, Pending Verification, Closed, Accepted Risk
```

## Conditional Formatting

**Risk Level Column (F):**
- Critical: Dark red fill (#8B0000), white text
- High: Red fill (#FF6B6B)
- Medium: Orange fill (#FFB347)
- Low: Yellow fill (#FFEB9C)

**Status Column (H):**
- Open: Red fill
- In Progress: Yellow fill
- Pending Verification: Light blue fill
- Closed: Green fill
- Accepted Risk: Grey fill

---

# Sheet 7: Risk Register

## Column Structure

| Column | Header | Width | Purpose |
|--------|--------|-------|---------|
| A | Risk ID | 10 | Unique identifier (RISK-001) |
| B | Related Gap(s) | 15 | Reference to Gap ID(s) |
| C | Risk Description | 35 | What could go wrong |
| D | Risk Category | 18 | Data Breach/Compliance/Operational |
| E | Impact | 12 | 1-5 scale |
| F | Likelihood | 12 | 1-5 scale |
| G | Risk Score | 10 | Impact x Likelihood |
| H | Risk Rating | 12 | Critical/High/Medium/Low |
| I | Risk Owner | 18 | Accountable person |
| J | Treatment Option | 15 | Mitigate/Accept/Transfer/Avoid |
| K | Treatment Plan | 30 | How risk will be treated |
| L | Treatment Status | 15 | Not Started/In Progress/Complete |
| M | Residual Risk | 12 | Post-treatment rating |
| N | Review Date | 12 | Next review scheduled |

## Data Validation

**Column D - Risk Category:**
```
Dropdown: Data Breach, Regulatory Compliance, Operational Continuity, Reputational, Financial, Legal, Multiple
```

**Column E - Impact:**
```
Dropdown: 1 - Negligible, 2 - Minor, 3 - Moderate, 4 - Significant, 5 - Severe
```

**Column F - Likelihood:**
```
Dropdown: 1 - Rare, 2 - Unlikely, 3 - Possible, 4 - Likely, 5 - Almost Certain
```

**Column J - Treatment Option:**
```
Dropdown: Mitigate, Accept, Transfer, Avoid
```

**Column L - Treatment Status:**
```
Dropdown: Not Started, In Progress, On Hold, Complete, Ongoing
```

## Calculated Fields

**Column G - Risk Score:**
```
=E2*F2
```

**Column H - Risk Rating:**
```
=IF(G2>=20,"Critical",IF(G2>=12,"High",IF(G2>=6,"Medium","Low")))
```

---

# Sheet 8: Remediation Roadmap

## Column Structure

| Column | Header | Width | Purpose |
|--------|--------|-------|---------|
| A | Action ID | 10 | Unique identifier (ACT-001) |
| B | Related Gap/Risk | 15 | Reference to Gap or Risk ID |
| C | Action Description | 35 | What needs to be done |
| D | Action Owner | 18 | Responsible person |
| E | Priority | 12 | P1/P2/P3/P4 |
| F | Start Date | 12 | Planned start |
| G | Target Date | 12 | Planned completion |
| H | Actual Completion | 12 | When actually completed |
| I | Progress % | 10 | Percentage complete |
| J | Status | 15 | Not Started/In Progress/Complete |
| K | Dependencies | 20 | Other actions required first |
| L | Budget Required | 12 | Yes/No/Amount |
| M | Notes | 25 | Additional context |

## Data Validation

**Column E - Priority:**
```
Dropdown: P1 - Critical (30 days), P2 - High (90 days), P3 - Medium (180 days), P4 - Low (365 days)
```

**Column J - Status:**
```
Dropdown: Not Started, In Progress, On Hold, Complete, Cancelled
```

## Gantt Chart Section (Rows 50+)

Simple timeline visualization:
- Row headers: Action IDs
- Column headers: Months (next 12)
- Cell fill: Blue = planned, Green = complete, Red = overdue, Yellow = in progress

**Gantt Conditional Formatting:**
- Planned period: Light blue fill
- Completed: Green fill
- Overdue: Red fill
- Current period in progress: Yellow fill

---

# Sheet 9: Evidence Master Index

## Column Structure

| Column | Header | Width | Purpose |
|--------|--------|-------|---------|
| A | Evidence ID | 12 | Unique identifier (EV-001) |
| B | Source Domain | 15 | Domain 1/2/3/Dashboard |
| C | Related Control | 15 | A.7.10 reference |
| D | Related Gap/Risk | 15 | Gap or Risk ID |
| E | Evidence Type | 18 | Category of evidence |
| F | Evidence Description | 35 | What the evidence shows |
| G | Document/File Name | 25 | Actual filename |
| H | Location/Link | 30 | Where evidence is stored |
| I | Date Collected | 12 | When evidence gathered |
| J | Collected By | 18 | Who gathered evidence |
| K | Retention Period | 15 | How long to keep |
| L | Review Date | 12 | Next review scheduled |

## Data Validation

**Column E - Evidence Type:**
```
Dropdown: Policy Document, Procedure Document, Assessment Workbook, Certificate of Destruction, Training Record, Audit Report, System Configuration, Screenshot, Photograph, Contract, Other
```

---

# Sheet 10: KPI Dashboard

## KPI Structure

**Section 1: Media Inventory KPIs (Rows 5-20)**

| KPI ID | KPI Name | Target | Current | Previous | Trend |
|--------|----------|--------|---------|----------|-------|
| KPI-01 | Registered media % | 100% | Formula | Manual | Calc |
| KPI-02 | Encrypted CONFIDENTIAL % | 100% | Formula | Manual | Calc |
| KPI-03 | Authorised removable % | 100% | Formula | Manual | Calc |
| KPI-04 | Custodian assigned % | 100% | Formula | Manual | Calc |

**Section 2: Handling KPIs (Rows 22-35)**

| KPI ID | KPI Name | Target | Current | Previous | Trend |
|--------|----------|--------|---------|----------|-------|
| KPI-05 | Chain of custody % | 100% | Manual | Manual | Calc |
| KPI-06 | Approved courier usage % | 100% | Manual | Manual | Calc |
| KPI-07 | Environmental compliance % | 100% | Manual | Manual | Calc |

**Section 3: Lifecycle KPIs (Rows 37-50)**

| KPI ID | KPI Name | Target | Current | Previous | Trend |
|--------|----------|--------|---------|----------|-------|
| KPI-08 | Disposal with certificate % | 100% | Manual | Manual | Calc |
| KPI-09 | Vendor certification current % | 100% | Manual | Manual | Calc |
| KPI-10 | Re-use verification % | 100% | Manual | Manual | Calc |

**Section 4: Incident KPIs (Rows 52-60)**

| KPI ID | KPI Name | Target | Current | Previous | Trend |
|--------|----------|--------|---------|----------|-------|
| KPI-11 | Media loss incidents | 0 | Manual | Manual | Calc |
| KPI-12 | Overdue media returns | <3 | Manual | Manual | Calc |

**Trend Calculation:**
```
=IF(Current>Previous, "Improving", IF(Current<Previous, "Declining", "Stable"))
```

## Sparkline Charts

**For each KPI:**
- Trend sparkline showing last 4 quarters
- Data range from historical sheet (if maintained)

---

# Sheet 11: CISO Approval

## Layout Structure

**Document Control (Rows 3-12)**
- Dashboard version
- Period covered
- Overall compliance %
- Critical gaps count
- Prepared by
- Preparation date

**Executive Summary (Rows 14-30)**
- Key findings (top 5)
- Significant improvements
- Areas of concern
- Resource requirements

**Risk Acceptance Section (Rows 32-45)**
- Risks proposed for acceptance
- Justification for acceptance
- Compensating controls
- Acceptance expiry date

**Approvals (Rows 47-75)**

**Level 1: CISO Approval**
- Statement: "I have reviewed this dashboard and confirm..."
- Name, Title, Date, Signature
- Conditions/Comments

**Level 2: Executive Approval**
- Statement: "Executive Management acknowledges..."
- Name, Title, Date, Signature
- Risk acceptance decisions

**Next Steps (Rows 77-90)**
- Action items from review
- Owner, Due Date, Status table

**Next Review (Rows 92-100)**
- Scheduled review date
- Review owner
- Review scope

---

**END OF SPECIFICATION**

---

*"In God we trust; all others must bring data."*
— W. Edwards Deming

<!-- QA_VERIFIED: 2026-02-06 -->

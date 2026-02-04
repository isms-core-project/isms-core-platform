# ISMS-IMP-A.5.12-13.5 - Consolidation Dashboard

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.5 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.12-13 Classification and Labelling |
| **Parent Policy** | ISMS-POL-A.5.12-13 - Information Classification and Labelling |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Workbook Structure](#14-workbook-structure)
   - [1.5 Completion Walkthrough](#15-completion-walkthrough)
   - [1.6 Evidence Collection](#16-evidence-collection)
   - [1.7 Common Pitfalls](#17-common-pitfalls)
   - [1.8 Quality Checklist](#18-quality-checklist)
   - [1.9 Review and Approval](#19-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Integration Points](#24-integration-points)
   - [2.5 Related Documents](#25-related-documents)

---

# PART I: USER COMPLETION GUIDE

---

## 1.1 Assessment Overview

### Purpose

This workbook consolidates data from all four A.5.12-13 assessment domains into a unified executive view, providing comprehensive visibility into the organisation's information classification and labelling program.

The consolidation dashboard serves multiple purposes:
- **Aggregate**: Bring together data from all source workbooks
- **Summarise**: Provide executive-level overview of entire control area
- **Cross-Reference**: Link gaps, risks, and remediation across domains
- **Track Trends**: Monitor compliance improvements over time
- **Support Audit**: Single point of reference for A.5.12-13 evidence

### Scope

The Consolidation Dashboard aggregates data from:

| Source Workbook | Domain | Key Data |
|-----------------|--------|----------|
| **A.5.12-13.1** | Classification Scheme | Scheme approval, levels defined, handling requirements |
| **A.5.12-13.2** | Labelling Procedures | Standards defined, digital/physical labelling status |
| **A.5.12-13.3** | Asset Inventory | Classification coverage, labelling compliance |
| **A.5.12-13.4** | Compliance Dashboard | Metrics, maturity, risks, remediation |

**Dashboard Outputs:**

| Output Area | Purpose | Audience |
|-------------|---------|----------|
| **Executive Summary** | Overall compliance at a glance | Executive Management |
| **Domain Overview** | Status of each assessment domain | CISO, Management |
| **Classification Compliance** | Scheme implementation status | Control Owners |
| **Labelling Compliance** | Labelling standards adherence | IT Operations |
| **Inventory Compliance** | Asset classification coverage | Data Governance |
| **Cross-Domain Gaps** | Gaps spanning multiple domains | Risk Managers |
| **KPI Summary** | Key metrics across all domains | Dashboard Users |
| **Trend Dashboard** | Historical compliance trends | Strategic Planning |

### Business Value

| Value Area | Benefit |
|------------|---------|
| **Single View** | One dashboard for entire classification program |
| **Executive Reporting** | Board-ready compliance summary |
| **Audit Efficiency** | Consolidated evidence for auditors |
| **Strategic Planning** | Trend data for roadmap decisions |
| **Cross-Domain Visibility** | Identify systemic issues |

### Assessment Frequency

| Assessment Type | Frequency | Trigger Events |
|-----------------|-----------|----------------|
| Full Consolidation | Quarterly | Management review, audit |
| Metric Roll-up | Monthly | Operational reporting |
| Trend Update | Quarterly | Period close |
| Ad-hoc Consolidation | As needed | Executive request, audit |

---

## 1.2 Control Requirements

### ISO 27001:2022 Controls A.5.12 & A.5.13

This consolidation dashboard supports demonstration of compliance with:

**Control A.5.12 - Classification of Information:**
> *"Information should be classified according to the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements."*

**Control A.5.13 - Labelling of Information:**
> *"An appropriate set of procedures for information labelling should be developed and implemented in accordance with the information classification scheme adopted by the organization."*

### What Auditors Look For

| Audit Focus | This Dashboard Provides |
|-------------|------------------------|
| **Complete Implementation** | Consolidated view of all A.5.12-13 domains |
| **Evidence Trail** | Cross-reference to source workbooks |
| **Trend Analysis** | Historical compliance data |
| **Gap Management** | Consolidated gap tracking |
| **Management Oversight** | Executive approval records |

---

## 1.3 Prerequisites

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| A.5.12-13.1-4 Workbooks | Source data | Read access |
| Evidence Library | Linked evidence | Read access |
| Previous Consolidations | Trend data | Read access |

### Required Documents

- [ ] ISMS-IMP-A.5.12-13.1 - Classification Scheme Definition (completed)
- [ ] ISMS-IMP-A.5.12-13.2 - Labelling Procedures (completed)
- [ ] ISMS-IMP-A.5.12-13.3 - Asset Classification Inventory (completed)
- [ ] ISMS-IMP-A.5.12-13.4 - Compliance Dashboard (completed)
- [ ] Prior consolidation dashboards (for trend data)

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Assessment Lead** | Aggregate and consolidate | 4-6 hours |
| **CISO** | Review and approve | 2-3 hours |
| **Data Owners** | Validate domain data | 1 hour each |
| **Executive Sponsor** | Final sign-off | 1 hour |

---

## 1.4 Workbook Structure

### Sheet Overview

| Sheet | Purpose | Assessor Action |
|-------|---------|-----------------|
| **Instructions** | Dashboard guidance | Read before starting |
| **Executive_Summary** | High-level overview | Complete from sources |
| **Domain_Overview** | Per-domain status | Roll up from A.5.12-13.1-4 |
| **Classification_Compliance** | Scheme implementation | Extract from A.5.12-13.1 |
| **Labelling_Compliance** | Labelling adherence | Extract from A.5.12-13.2 |
| **Inventory_Compliance** | Asset coverage | Extract from A.5.12-13.3 |
| **Cross_Domain_Gaps** | Cross-cutting issues | Consolidate gaps |
| **Remediation_Tracker** | Consolidated actions | Roll up from A.5.12-13.4 |
| **KPI_Summary** | All key metrics | Aggregate metrics |
| **Evidence_Index** | Evidence cross-reference | Link to sources |
| **Trend_Dashboard** | Historical trends | Update quarterly |
| **Approval_SignOff** | Executive approval | Obtain signatures |

### Data Flow

```
A.5.12-13.1 ────────────────────────────────────────┐
(Classification Scheme)                              │
                                                     │
A.5.12-13.2 ─────────────────────────────────────►  Executive_Summary
(Labelling Procedures)                               │        │
                                                     │        ▼
A.5.12-13.3 ─────────────────────────────────────►  Domain_Overview
(Asset Inventory)                                    │        │
                                                     │        ├──► Classification_Compliance
A.5.12-13.4 ─────────────────────────────────────►  │        ├──► Labelling_Compliance
(Compliance Dashboard)                               │        ├──► Inventory_Compliance
                                                     │        │
                                                     │        ▼
                                                     │  Cross_Domain_Gaps
                                                     │        │
                                                     │        ▼
                                                     │  Remediation_Tracker
                                                     │        │
                                                     │        ▼
                                                     └──► KPI_Summary
                                                              │
                                                              ▼
                                                     Evidence_Index
                                                              │
                                                              ▼
                                                     Trend_Dashboard
                                                              │
                                                              ▼
                                                     Approval_SignOff
```

---

## 1.5 Completion Walkthrough

### Step 1: Complete Executive Summary

**Time allocation:** 1-2 hours

**Purpose:** Create high-level overview from all source workbooks.

**Executive Summary Content:**

| Section | Source | Data to Extract |
|---------|--------|-----------------|
| Reporting Period | Current period | Start and end dates |
| Assessment Date | Current date | Consolidation date |
| Overall Status by Domain | A.5.12-13.1-4 | Status per workbook |
| Key Metrics | A.5.12-13.4 | Top-line metrics |
| Critical Gaps | Cross-domain | Count of critical items |

**Domain Status Summary:**

| Domain | Workbook | Status | Score % | Critical Gaps |
|--------|----------|--------|---------|---------------|
| Classification Scheme | A.5.12-13.1 | | | |
| Labelling Procedures | A.5.12-13.2 | | | |
| Asset Inventory | A.5.12-13.3 | | | |
| Compliance Monitoring | A.5.12-13.4 | | | |
| **OVERALL** | Consolidated | | | |

**Scoring Criteria:**
- ≥90% = Compliant (Green)
- 50-89% = Partial (Amber)
- <50% = Non-Compliant (Red)

### Step 2: Populate Domain Overview

**Time allocation:** 1-2 hours

**Purpose:** Document status of key requirements per domain.

**Domain 1: Classification Scheme (from A.5.12-13.1)**

| Requirement | Status | Evidence Ref | Gap | Remediation |
|-------------|--------|--------------|-----|-------------|
| Classification levels defined | | | | |
| Handling requirements documented | | | | |
| CIA matrix completed | | | | |
| Regulatory mapping done | | | | |

**Domain 2: Labelling Standards (from A.5.12-13.2)**

| Requirement | Status | Evidence Ref | Gap | Remediation |
|-------------|--------|--------------|-----|-------------|
| Digital labelling standards | | | | |
| Physical labelling standards | | | | |
| Automation tools assessed | | | | |
| Labelling procedures approved | | | | |

**Domain 3: Asset Inventory (from A.5.12-13.3)**

| Requirement | Status | Evidence Ref | Gap | Remediation |
|-------------|--------|--------------|-----|-------------|
| Asset inventory complete | | | | |
| Classification assignments current | | | | |
| Reclassification process defined | | | | |
| Gap analysis completed | | | | |

### Step 3: Extract Compliance Details

**Time allocation:** 1-2 hours

**Purpose:** Provide detailed compliance status for each domain.

**Classification Compliance (from A.5.12-13.1):**

| Classification Level | Definition Status | Handling Rules | Examples | Training | Compliance |
|---------------------|-------------------|----------------|----------|----------|------------|
| Public | | | | | |
| Internal | | | | | |
| Confidential | | | | | |
| Restricted | | | | | |

**Labelling Compliance (from A.5.12-13.2):**

| Asset Type | Digital Standard | Physical Standard | Automation | Compliance |
|------------|-----------------|-------------------|------------|------------|
| Documents | | | | |
| Emails | | | | |
| Databases | | | | |
| Files/Folders | | | | |
| Physical Media | | | | |
| Hardware | | | | |
| Cloud Storage | | | | |
| Source Code | | | | |

**Inventory Compliance (from A.5.12-13.3):**

| Asset Category | Total | Classified | Labelled | % Complete | Compliance |
|----------------|-------|------------|----------|------------|------------|
| Information Assets | | | | | |
| Software Assets | | | | | |
| Physical Assets | | | | | |
| Services | | | | | |
| Cloud Resources | | | | | |

### Step 4: Consolidate Cross-Domain Gaps

**Time allocation:** 1 hour

**Purpose:** Identify gaps that span multiple domains.

**Cross-Domain Gap Types:**
- Gap in scheme definition causes labelling issues
- Inventory gap affects compliance metrics
- Automation gap impacts multiple asset types
- Training gap affects all domains

**Gap Consolidation Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Gap_ID | Unique identifier | GAP-X-001 |
| Source_Domain | Where identified | A.5.12-13.2 |
| Gap_Description | What the gap is | Legacy systems cannot apply labels |
| Risk_Rating | Impact level | High |
| Priority | Fix urgency | High |
| Affected_Controls | Which controls | A.5.12, A.5.13 |
| Root_Cause | Why it exists | Technical limitation |
| Remediation_Action | How to fix | Implement compensating control |
| Owner | Who is responsible | IT Manager |
| Target_Date | When to fix by | 2026-03-31 |

### Step 5: Consolidate Remediation Actions

**Time allocation:** 1 hour

**Purpose:** Single view of all remediation actions across domains.

**Consolidation Process:**
1. Extract actions from A.5.12-13.4 Remediation_Tracker
2. Add any new cross-domain actions
3. Update status of all items
4. Identify overdue items for escalation

**Remediation Fields:**

| Field | Description |
|-------|-------------|
| Action_ID | Unique identifier |
| Related_Gap | Link to gap |
| Source_Domain | Which workbook |
| Action_Description | What to do |
| Priority | Critical/High/Medium/Low |
| Owner | Responsible person |
| Start_Date | When started |
| Target_Date | Deadline |
| Status | Current state |
| Progress_% | Completion percentage |
| Notes | Additional detail |

### Step 6: Summarise KPIs

**Time allocation:** 30 minutes

**Purpose:** Single view of all key metrics.

**Consolidated KPIs:**

| KPI | Target | Current | Previous | Trend | Status |
|-----|--------|---------|----------|-------|--------|
| % of classification levels defined | 100% | | | | |
| % of assets classified | 100% | | | | |
| % of assets labelled | 100% | | | | |
| % of staff trained | 100% | | | | |
| Classification scheme review currency | <12 months | | | | |
| Labelling standards compliance | ≥95% | | | | |

### Step 7: Update Trend Dashboard

**Time allocation:** 30 minutes

**Purpose:** Track compliance improvement over time.

**Quarterly Trend Data:**

| Period | Classification % | Labelling % | Inventory % | Overall % | Critical Gaps | Remediation Rate |
|--------|-----------------|-------------|-------------|-----------|---------------|------------------|
| Q1 2025 | | | | | | |
| Q2 2025 | | | | | | |
| Q3 2025 | | | | | | |
| Q4 2025 | | | | | | |
| Q1 2026 | | | | | | |
| Q2 2026 | | | | | | |

### Step 8: Obtain Executive Approval

**Time allocation:** 1 hour

**Purpose:** Secure formal approval of consolidated assessment.

**Approval Workflow:**
1. Assessment Lead prepares consolidation
2. Data owners validate their domain data
3. CISO reviews overall status
4. Executive sponsor provides final sign-off

---

## 1.6 Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| This consolidation workbook | Generated | 7 years |
| Source workbooks (A.5.12-13.1-4) | Referenced | 7 years |
| Prior consolidations (trend data) | Historical | 7 years |
| Approval signatures | This workbook | Duration + 2 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.12-13/Consolidation/[Year]/`

**Folder Structure:**
```
A.5.12-13/
|-- Consolidation/
|   |-- 2026/
|   |   |-- Q1/
|   |   |   |-- ISMS-IMP-A.5.12-13.5_Consolidation_Dashboard_20260331.xlsx
|   |   |-- Q2/
|   |   |-- Q3/
|   |   |-- Q4/
|   |   |-- Annual/
|   |   |   |-- Annual_Consolidation_2026.xlsx
```

---

## 1.7 Common Pitfalls

Avoid these common mistakes when completing the consolidation dashboard:

### Data Aggregation Pitfalls

❌ **MISTAKE**: Using outdated source workbooks
✅ **CORRECT**: Verify source workbooks are current before consolidating

❌ **MISTAKE**: Manual data entry instead of referencing sources
✅ **CORRECT**: Link to source data where possible; document data date

❌ **MISTAKE**: Inconsistent calculation methods between periods
✅ **CORRECT**: Document methodology; apply consistently

❌ **MISTAKE**: Counting same gap multiple times across domains
✅ **CORRECT**: Deduplicate cross-domain gaps; assign single ID

### Trend Analysis Pitfalls

❌ **MISTAKE**: Changing metrics definitions between periods
✅ **CORRECT**: Maintain consistent definitions; document any changes

❌ **MISTAKE**: Incomplete historical data gaps
✅ **CORRECT**: Note data gaps clearly; don't interpolate missing data

❌ **MISTAKE**: Comparing periods with different scope
✅ **CORRECT**: Normalise data when scope changes; document scope

### Reporting Pitfalls

❌ **MISTAKE**: Dashboard too detailed for executive audience
✅ **CORRECT**: Executive Summary first; detail in subsequent sheets

❌ **MISTAKE**: Status without supporting data
✅ **CORRECT**: Every status should trace to evidence

❌ **MISTAKE**: Missing approval for significant changes
✅ **CORRECT**: Any material changes require re-approval

---

## 1.8 Quality Checklist

Before submitting the consolidation, verify:

### Data Completeness Checks

- [ ] All four source workbooks current
- [ ] Executive Summary reflects latest data
- [ ] All domains included in Domain Overview
- [ ] Compliance details extracted accurately
- [ ] All gaps consolidated

### Consistency Checks

- [ ] Metrics match source workbooks
- [ ] Gap counts reconcile
- [ ] Remediation items complete
- [ ] Trend data consistent methodology
- [ ] Status indicators accurate

### Cross-Reference Checks

- [ ] Evidence references valid
- [ ] Gap-to-remediation links correct
- [ ] Domain data matches source
- [ ] KPIs trace to source metrics

### Approval Readiness Checks

- [ ] Executive Summary complete
- [ ] All sections populated
- [ ] Trend data updated
- [ ] Ready for signature

---

## 1.9 Review and Approval

### Review Workflow

```
Assessment Lead Consolidates Data
        │
        ▼
Domain Owners Validate (A.5.12-13.1-4)
        │
        ▼
CISO Review
        │
        ▼
Executive Sponsor Approval
        │
        ▼
Consolidation Approved
        │
        ▼
Archive and Distribute
```

### Approval Signatures

The Approval_SignOff sheet requires:

1. **Assessment Lead (Prepared By):**
   - Confirms data aggregated accurately
   - Confirms sources documented
   - Date and signature

2. **Data Governance (Reviewed By):**
   - Confirms data quality
   - Confirms completeness
   - Date and signature

3. **CISO (Approved By):**
   - Accepts overall compliance status
   - Approves for distribution
   - Date and signature

4. **Data Owner Sign-Off:**
   - Confirms domain accuracy
   - Date and signature

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.12-13.5_Consolidation_Dashboard_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_5_consolidation_dashboard.py` |
| Sheets | 12 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Dashboard guidance | 30 | 1 |
| 2 | Executive_Summary | High-level view | 25 | 8 |
| 3 | Domain_Overview | Per-domain status | 30 | 5 |
| 4 | Classification_Compliance | Scheme status | 15 | 8 |
| 5 | Labelling_Compliance | Labelling status | 20 | 8 |
| 6 | Inventory_Compliance | Asset coverage | 15 | 8 |
| 7 | Cross_Domain_Gaps | Cross-cutting gaps | 20 | 10 |
| 8 | Remediation_Tracker | All remediation | 20 | 11 |
| 9 | KPI_Summary | Consolidated KPIs | 15 | 6 |
| 10 | Evidence_Index | Evidence links | 20 | 8 |
| 11 | Trend_Dashboard | Historical trends | 15 | 8 |
| 12 | Approval_SignOff | Executive approval | 15 | 5 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title | Document identification |
| 3-6 | Purpose | Dashboard purpose |
| 8-12 | Source workbooks | Reference list |
| 14-18 | Compliance scoring | Scoring methodology |
| 20-22 | Generated info | Date and control reference |

### Sheet 2: Executive_Summary

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Domain / Metric | 35 | Text | Pre-populated |
| B | Workbook | 35 | Text | Pre-populated |
| C | Status | 18 | List | Compliant, Partial, Non-Compliant |
| D | Score % | 12 | Percent | Input |
| E | Critical Gaps | 15 | Number | Input |
| F | Last Updated | 15 | Date | Input |

**Sections:**
- Reporting Period (rows 3-5)
- Overall Compliance Status (rows 6-11)
- Key Metrics (rows 14-18)

### Sheet 3: Domain_Overview

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Requirement | 40 | Text | Pre-populated |
| B | Status | 18 | List | Complete, In Progress, Not Started, N/A |
| C | Evidence_Ref | 15 | Text | Input |
| D | Gap_Description | 35 | Text | Input |
| E | Remediation | 35 | Text | Input |

**Sections:**
- Domain 1: Classification Scheme (rows 3-8)
- Domain 2: Labelling Standards (rows 10-15)
- Domain 3: Asset Inventory (rows 17-22)

### Sheet 4: Classification_Compliance

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Classification_Level | 20 | Text | Pre-populated |
| B | Definition_Status | 18 | List | Complete, Partial, Missing |
| C | Handling_Rules | 18 | List | Complete, Partial, Missing |
| D | Examples_Documented | 20 | List | Yes, No |
| E | Training_Available | 18 | List | Yes, No |
| F | Compliance_Status | 18 | List | Compliant, Partial, Non-Compliant |
| G | Gap_Notes | 30 | Text | Input |
| H | Owner | 20 | Text | Input |

### Sheet 5: Labelling_Compliance

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_Type | 18 | Text | Pre-populated |
| B | Digital_Label_Standard | 22 | List | Defined, Partial, Not Defined |
| C | Physical_Label_Standard | 22 | List | Defined, Partial, Not Defined, N/A |
| D | Automation_Status | 18 | List | Deployed, Partial, Not Deployed, N/A |
| E | Compliance_Status | 18 | List | Compliant, Partial, Non-Compliant |
| F | Gap_Notes | 30 | Text | Input |
| G | Remediation | 25 | Text | Input |
| H | Owner | 18 | Text | Input |

### Sheet 6: Inventory_Compliance

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_Category | 22 | Text | Pre-populated |
| B | Total_Assets | 14 | Number | Input |
| C | Classified | 14 | Number | Input |
| D | Labelled | 14 | Number | Input |
| E | Percent_Complete | 12 | Percent | Formula |
| F | Compliance_Status | 18 | List | Compliant, Partial, Non-Compliant |
| G | Gap_Notes | 30 | Text | Input |
| H | Owner | 18 | Text | Input |

### Sheet 7: Cross_Domain_Gaps

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Gap_ID | 10 | Text | Auto-generated |
| B | Source_Domain | 22 | List | A.5.12-13.1, A.5.12-13.2, A.5.12-13.3, A.5.12-13.4, Cross-Domain |
| C | Gap_Description | 40 | Text | Input |
| D | Risk_Rating | 12 | List | Critical, High, Medium, Low |
| E | Priority | 10 | List | Critical, High, Medium, Low |
| F | Affected_Controls | 18 | Text | Input |
| G | Root_Cause | 30 | Text | Input |
| H | Remediation_Action | 35 | Text | Input |
| I | Owner | 18 | Text | Input |
| J | Target_Date | 15 | Date | Input |

### Sheet 8: Remediation_Tracker

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Action_ID | 10 | Text | None |
| B | Related_Gap | 12 | Text | None |
| C | Source_Domain | 20 | List | A.5.12-13.1, A.5.12-13.2, A.5.12-13.3, A.5.12-13.4, Cross-Domain |
| D | Action_Description | 40 | Text | None |
| E | Priority | 10 | List | Critical, High, Medium, Low |
| F | Owner | 18 | Text | None |
| G | Start_Date | 12 | Date | None |
| H | Target_Date | 12 | Date | None |
| I | Status | 12 | List | Not Started, In Progress, Complete, On Hold |
| J | Progress_% | 10 | List | 0%, 25%, 50%, 75%, 100% |
| K | Notes | 30 | Text | None |

### Sheet 9: KPI_Summary

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | KPI | 42 | Text | Pre-populated |
| B | Target | 15 | Text | Pre-populated |
| C | Current | 12 | Text/Number | Input |
| D | Previous | 12 | Text/Number | Input |
| E | Trend | 10 | List | ↑, →, ↓ |
| F | Status | 15 | List | On Target, At Risk, Below Target |

### Sheet 10: Evidence_Index

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 12 | Text | None |
| B | Source_Workbook | 25 | List | A.5.12-13.1, A.5.12-13.2, A.5.12-13.3, A.5.12-13.4 |
| C | Source_Sheet | 22 | Text | None |
| D | Evidence_Type | 18 | Text | None |
| E | Evidence_Description | 40 | Text | None |
| F | Location_Reference | 30 | Text | None |
| G | Date_Captured | 15 | Date | None |
| H | Validation_Status | 18 | List | Validated, Pending, Not Validated |

### Sheet 11: Trend_Dashboard

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Period | 12 | Text | Pre-populated |
| B | Classification_% | 16 | Percent | Input |
| C | Labelling_% | 14 | Percent | Input |
| D | Inventory_% | 14 | Percent | Input |
| E | Overall_% | 12 | Percent | Formula |
| F | Critical_Gaps | 15 | Number | Input |
| G | Remediation_Rate | 18 | Percent | Input |
| H | Notes | 35 | Text | Input |

### Sheet 12: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 30 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Date | 15 | Date | Input |
| D | Signature | 20 | Text | Input |
| E | Comments | 40 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Executive_Summary | C:C | ="Compliant" | Green fill (#C6EFCE) |
| Executive_Summary | C:C | ="Partial" | Yellow fill (#FFEB9C) |
| Executive_Summary | C:C | ="Non-Compliant" | Red fill (#FFC7CE) |
| Domain_Overview | B:B | ="Complete" | Green fill (#C6EFCE) |
| Domain_Overview | B:B | ="In Progress" | Yellow fill (#FFEB9C) |
| Domain_Overview | B:B | ="Not Started" | Red fill (#FFC7CE) |
| Classification_Compliance | F:F | ="Compliant" | Green fill (#C6EFCE) |
| Classification_Compliance | F:F | ="Non-Compliant" | Red fill (#FFC7CE) |
| Labelling_Compliance | E:E | ="Compliant" | Green fill (#C6EFCE) |
| Labelling_Compliance | E:E | ="Non-Compliant" | Red fill (#FFC7CE) |
| Inventory_Compliance | F:F | ="Compliant" | Green fill (#C6EFCE) |
| Inventory_Compliance | F:F | ="Non-Compliant" | Red fill (#FFC7CE) |
| Cross_Domain_Gaps | D:D | ="Critical" | Red fill (#FFC7CE), Bold |
| Cross_Domain_Gaps | D:D | ="High" | Orange fill (#FABF8F) |
| Remediation_Tracker | I:I | ="Complete" | Green fill (#C6EFCE) |
| Remediation_Tracker | I:I | ="Not Started" | Red fill (#FFC7CE) |
| KPI_Summary | F:F | ="On Target" | Green fill (#C6EFCE) |
| KPI_Summary | F:F | ="Below Target" | Red fill (#FFC7CE) |
| KPI_Summary | E:E | ="↑" | Green text |
| KPI_Summary | E:E | ="↓" | Red text |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| A.5.12-13.1 Workbook | Classification scheme data | A.5.12-13.1 -> Classification_Compliance |
| A.5.12-13.2 Workbook | Labelling data | A.5.12-13.2 -> Labelling_Compliance |
| A.5.12-13.3 Workbook | Inventory data | A.5.12-13.3 -> Inventory_Compliance |
| A.5.12-13.4 Workbook | Metrics and remediation | A.5.12-13.4 -> KPI_Summary, Remediation |
| GRC Platform | Compliance reporting | This workbook -> GRC |
| Executive Reporting | Management dashboards | This workbook -> Board reports |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.1 | Classification Scheme Definition | Source workbook |
| ISMS-IMP-A.5.12-13.2 | Labelling Procedures and Standards | Source workbook |
| ISMS-IMP-A.5.12-13.3 | Asset Classification Inventory | Source workbook |
| ISMS-IMP-A.5.12-13.4 | Compliance Dashboard | Source workbook |

---

**END OF SPECIFICATION**

---

*"The whole is greater than the sum of its parts."*
— Aristotle

<!-- QA_VERIFIED: 2026-02-04 -->

**ISMS-IMP-A.8.9.5-UG - Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.9: Configuration Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.9.5-UG |
| **Version** | 1.0 |
| **Assessment Area** | Configuration Management Compliance - Consolidated Maturity Dashboard Across All Four Domains |
| **Related Policy** | ISMS-POL-A.8.9 (All Sections - Baseline, Change Control, Monitoring, Hardening) |
| **Purpose** | Provide consolidated executive dashboard of configuration management maturity across all four domains (baseline, change, monitoring, hardening) with aggregated compliance metrics and trend analysis |
| **Target Audience** | CISO, Configuration Manager, IT Leadership, Executive Management, Risk Management, Compliance Officers, Auditors |
| **Assessment Type** | Executive Dashboard & Compliance Reporting |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Configuration Management Compliance Dashboard | ISMS Implementation Team |

---

**Audience:** Security assessors, Control owners, Compliance officers

---

## Document Purpose

This specification defines the consolidated compliance dashboard for Control A.8.9 
(Configuration Management). The dashboard aggregates compliance data from all four 
domain-specific assessments into a single executive-level view of overall configuration 
management posture.

**Dual Perspective Implementation:**

**As ISMS Implementer:**

- Provides single-pane-of-glass view of entire A.8.9 compliance
- Enables executive reporting without manual data aggregation
- Identifies cross-domain gaps and interdependencies
- Facilitates resource allocation decisions
- Tracks overall compliance trend over time

**As ISMS Auditor:**

- Delivers consolidated evidence of A.8.9 compliance
- Demonstrates systematic oversight across all configuration management domains
- Verifies that domain-specific assessments align with overall objectives
- Provides audit-ready executive summary
- Confirms governance and accountability framework

---

## Integration with Control A.8.9

The Compliance Dashboard is the apex of the A.8.9 assessment hierarchy, consolidating 
data from four domain-specific assessments:

**A.8.9.1 (Baseline Configuration):**

- Overall baseline documentation completeness
- Percentage of assets with documented baselines
- Version control compliance
- Baseline approval status

**A.8.9.2 (Change Control):**

- Change approval compliance rate
- Emergency change usage patterns
- Change success rate
- Backout effectiveness

**A.8.9.3 (Configuration Monitoring):**

- Drift detection coverage
- Mean time to detect (MTTD) drift
- Critical drift count
- Monitoring effectiveness score

**A.8.9.4 (Security Hardening):**

- Overall hardening compliance percentage
- High-risk gap count
- Exception rate
- Remediation progress

**Dashboard Value:**
The dashboard answers the executive question: "How well are we managing configurations 
across our information assets?" without requiring deep dive into domain details.

---

## Assessment Overview

### Assessment Objective

Provide consolidated oversight of Control A.8.9 compliance by:

1. **Aggregating Domain Compliance**: Combine metrics from all 4 domain assessments
2. **Calculating Overall Compliance**: Weighted average reflecting domain importance
3. **Identifying Critical Gaps**: Surface highest-priority issues across domains
4. **Tracking Trends**: Monitor compliance trajectory over time
5. **Reporting to Leadership**: Executive-level summary for governance
6. **Facilitating Audits**: Provide auditors with comprehensive compliance evidence

### Assessment Scope

**Data Sources (4 External Workbooks):**

All data is sourced from normalized assessment workbooks (date-free filenames):

- `ISMS-IMP-A.8.9.1.xlsx` (Baseline Configuration)
- `ISMS-IMP-A.8.9.2.xlsx` (Change Control)
- `ISMS-IMP-A.8.9.3.xlsx` (Configuration Monitoring)
- `ISMS-IMP-A.8.9.4.xlsx` (Security Hardening)

**CRITICAL - External Workbook Linking:**
This dashboard uses Excel external workbook formulas (e.g., 
`='[ISMS-IMP-A.8.9.1.xlsx]Asset_Inventory'!B5`). Dashboard and source workbooks must be 
in the same directory. Excel will prompt "Update Links" when opening dashboard.

**Compliance Calculation Methodology:**

Overall A.8.9 Compliance is calculated as weighted average:
```
Overall Compliance = 
  (Baseline Configuration × 20%) +
  (Change Control × 25%) +
  (Configuration Monitoring × 20%) +
  (Security Hardening × 25%) +
  (Process Maturity × 10%)
```

**Domain Weights (CUSTOMIZE for your organization):**

- **Baseline Configuration (20%)**: Foundation - must document before managing
- **Change Control (25%)**: Highest risk - uncontrolled changes cause incidents
- **Configuration Monitoring (20%)**: Detection capability - know when drift occurs
- **Security Hardening (25%)**: Security criticality - hardening prevents exploitation
- **Process Maturity (10%)**: Governance - ensures sustainability

Target: **≥95% overall compliance**

### Success Criteria

**Compliance Targets:**

- **Overall A.8.9 Compliance**: ≥95%
- **Domain Compliance**: All 5 domains ≥90%
- **Critical Gaps**: 0 across all domains
- **Domains Fully Compliant**: Target 4/5 (or 5/5)
- **Audit Readiness**: Evidence completeness ≥95%

**Process Maturity Indicators:**

- All 4 domain assessments completed within last 90 days
- Executive review of dashboard within last 30 days
- Documented remediation plans for all gaps
- Trend showing improvement (current > previous assessment)
- Integration with risk management process

---

## Excel Workbook Structure

**Workbook Name:** `ISMS_A_8_9_5_Compliance_Dashboard_YYYYMMDD.xlsx`

**Normalization Note:** After generation, run `normalize_assessment_files_a89.py` to 
create `ISMS-IMP-A.8.9.5.xlsx` (date-free) for consistent references in future cycles.

**Sheets:**
1. Instructions
2. Workbook_Integration_Settings
3. Overall_Compliance_Dashboard
4. Asset_Compliance_Summary
5. Gap_Prioritization
6. Trend_Analysis
7. Evidence_Register (100 rows)
8. Approval_Sign_Off

---

## Sheet 1: Instructions

### Purpose
Comprehensive guidance for using the consolidated compliance dashboard.

### Content Requirements

**Section 1: Dashboard Overview**

- Purpose of consolidated compliance dashboard
- Relationship to Control A.8.9 domain assessments
- How external workbook linking works
- Prerequisites (4 source workbooks normalized)

**Section 2: Key Concepts**

- **External Workbook Linking**: Formulas reference other Excel files in same directory
- **Normalized Filenames**: Source files must have date-free names (ISMS-IMP-A.8.9.X.xlsx)
- **Overall Compliance**: Weighted average across 5 domains
- **Domain Compliance**: Individual compliance percentage for each assessment area
- **Critical Gap**: High-severity issue requiring immediate attention
- **Compliance Trend**: Direction of compliance over time (improving/declining/stable)

**Section 3: Setup Workflow**
1. Complete all 4 domain assessments (A.8.9.1 through A.8.9.4)
2. Generate assessment workbooks with Python scripts
3. Run normalization script: `normalize_assessment_files_a89.py`
4. Verify normalized files exist:

   - ISMS-IMP-A.8.9.1.xlsx
   - ISMS-IMP-A.8.9.2.xlsx
   - ISMS-IMP-A.8.9.3.xlsx
   - ISMS-IMP-A.8.9.4.xlsx

5. Place dashboard workbook in same directory as normalized files
6. Open dashboard and click "Update Links" when prompted
7. Verify Workbook_Integration_Settings shows all 4 workbooks linked

**Section 4: Using the Dashboard**

- **Overall_Compliance_Dashboard**: Primary executive view, single-page summary
- **Asset_Compliance_Summary**: Per-asset view across all domains
- **Gap_Prioritization**: Consolidated gap list with risk ranking
- **Trend_Analysis**: Historical compliance tracking (requires multiple assessment cycles)
- **Evidence_Register**: Links to domain-specific evidence
- **Approval_Sign_Off**: Executive approval and governance

**Section 5: Understanding Overall Compliance**
Domain weights and calculation methodology:

- Baseline Configuration: 20% (foundation for management)
- Change Control: 25% (highest operational risk)
- Configuration Monitoring: 20% (detection capability)
- Security Hardening: 25% (security criticality)
- Process Maturity: 10% (governance and sustainability)

Formula: `Overall = (D1×0.20) + (D2×0.25) + (D3×0.20) + (D4×0.25) + (D5×0.10)`

**Section 6: External Workbook Linking**
How it works:

- Dashboard formulas reference source workbooks: `='[ISMS-IMP-A.8.9.1.xlsx]Sheet'!Cell`
- Excel automatically updates when source workbooks change
- Links are relative - files must be in same directory
- If workbook not found: Formula shows #REF! error

Troubleshooting broken links:

- Verify all 4 normalized workbooks exist in same directory as dashboard
- Excel: Data → Edit Links → Update Values
- Check filenames match exactly (case-sensitive on some systems)
- Ensure workbooks are not open in exclusive mode

**Section 7: Update Frequency**

- **Domain Assessments**: Quarterly minimum (or when major changes occur)
- **Dashboard**: Updates automatically when source workbooks change
- **Executive Review**: Monthly minimum
- **Trend Analysis**: Requires 3+ assessment cycles for meaningful insights

**Section 8: Roles and Responsibilities**

- **Dashboard Owner**: Coordinates assessment schedule, ensures dashboard currency
- **Domain Assessors**: Complete domain-specific assessments per schedule
- **Executive Sponsor**: Reviews dashboard, approves remediation priorities
- **ISMS Manager**: Oversees overall A.8.9 compliance, reports to leadership
- **Auditor**: Verifies dashboard accuracy, validates evidence links

**Section 9: Critical Success Factors**

- All 4 domain assessments completed and current (<90 days old)
- Source workbooks normalized and co-located with dashboard
- External workbook links functional (no #REF! errors)
- Executive review documented in Approval_Sign_Off
- Remediation plans exist for all gaps
- Compliance trend is stable or improving

**Section 10: Integration with ISMS**
Dashboard feeds:

- **Management Review**: Overall compliance status, trend, critical gaps
- **Risk Assessment**: Configuration management risks and controls
- **Audit Preparation**: Comprehensive evidence package for A.8.9
- **Continuous Improvement**: Gap analysis drives improvement initiatives

**Formatting:**

- Professional layout with clear section headers
- Use tables for structured information
- Include examples where helpful (generic examples only)
- Hyperlinks to other sheets for easy navigation

---

## Sheet 2: Workbook_Integration_Settings

### Purpose
Configuration and validation of external workbook links. Provides visibility into which 
source workbooks are linked and their status.

### Structure

**Section 1: Source Workbook Configuration**

Table showing linked workbooks:

| Domain | Document ID | Expected Filename | Status | Last Modified | Link Status |
|--------|-------------|-------------------|--------|---------------|-------------|
| Baseline Configuration | ISMS-IMP-A.8.9.1 | ISMS-IMP-A.8.9.1.xlsx | [formula] | [formula] | [formula] |
| Change Control | ISMS-IMP-A.8.9.2 | ISMS-IMP-A.8.9.2.xlsx | [formula] | [formula] | [formula] |
| Configuration Monitoring | ISMS-IMP-A.8.9.3 | ISMS-IMP-A.8.9.3.xlsx | [formula] | [formula] | [formula] |
| Security Hardening | ISMS-IMP-A.8.9.4 | ISMS-IMP-A.8.9.4.xlsx | [formula] | [formula] | [formula] |

**Column Definitions:**

- **Domain**: Configuration management domain area
- **Document ID**: Unique identifier for assessment
- **Expected Filename**: Normalized filename (no dates)
- **Status**: Link validation status (Linked/Not Found/Error)
- **Last Modified**: Last modification date from source workbook (if accessible)
- **Link Status**: Detailed status message

**Status Formula Logic:**
```excel
Status = 
  IF(ISERROR(external_reference), "Not Found",
  IF(ISREF(external_reference), "Linked", "Error"))
```

**Link Status Messages:**

- "✅ Linked and current" - Workbook found, link functional
- "⚠️ Workbook not found" - File missing from directory
- "⚠️ Workbook opened read-only" - File is open exclusively
- "❌ Link broken (#REF!)" - Formula error, workbook may be renamed
- "⏳ Workbook not updated (>90 days)" - Assessment is stale

**Section 2: Link Validation Summary**

| Metric | Value | Status |
|--------|-------|--------|
| Total Source Workbooks Expected | 4 | - |
| Workbooks Successfully Linked | [count] | [Red if <4] |
| Workbooks Missing | [count] | [Red if >0] |
| Workbooks Stale (>90 days) | [count] | [Yellow if >0] |
| Dashboard Link Health | [percentage] | [Green/Yellow/Red] |

**Dashboard Link Health Logic:**

- Green: All 4 workbooks linked and current (<90 days)
- Yellow: All 4 linked but 1+ stale (>90 days)
- Red: Any workbook not linked

**Section 3: Data Pull Test**

Test formulas to verify data can be pulled from each source:

| Source | Test Cell | Expected Value Type | Actual Value | Test Result |
|--------|-----------|---------------------|--------------|-------------|
| A.8.9.1 | Compliance_Dashboard!B5 | Percentage | [formula] | [Pass/Fail] |
| A.8.9.2 | Change_Summary!B10 | Percentage | [formula] | [Pass/Fail] |
| A.8.9.3 | Compliance_Dashboard!B8 | Percentage | [formula] | [Pass/Fail] |
| A.8.9.4 | Compliance_Dashboard!B5 | Percentage | [formula] | [Pass/Fail] |

**Test Result Logic:**
```excel
Test Result = 
  IF(ISERROR(formula), "Fail - Link Broken",
  IF(AND(formula>=0, formula<=1), "Pass", "Fail - Invalid Data"))
```

**Section 4: Troubleshooting Guide**

| Issue | Possible Cause | Resolution |
|-------|---------------|------------|
| "Workbook not found" | File not in same directory | Move dashboard to source workbook directory |
| "#REF! error" | Workbook renamed | Restore original filename or update formulas |
| "Read-only" | File open exclusively | Close source workbook, refresh dashboard |
| "Stale data" | Assessment outdated | Complete fresh assessment for domain |
| "Invalid data" | Source sheet structure changed | Verify source workbook is correct version |

**Section 5: Refresh Instructions**

Step-by-step refresh process:
1. Save and close dashboard workbook
2. Update one or more source workbooks (complete assessments)
3. Save source workbooks
4. Re-open dashboard workbook
5. Click "Update Links" when Excel prompts
6. Verify Workbook_Integration_Settings shows "Linked and current"
7. Review Overall_Compliance_Dashboard for updated metrics

**Conditional Formatting:**

- Link Status = "Linked and current": Green background
- Link Status contains "not found" or "broken": Red background
- Link Status contains "stale" or "read-only": Yellow background
- Dashboard Link Health < 100%: Red background
- Test Result = "Fail": Red background

### Usage Notes

**Purpose (Implementer Perspective):**
Diagnostic sheet to verify dashboard is correctly linked to source workbooks. Identifies 
issues before attempting to use dashboard for reporting.

**Purpose (Auditor Perspective):**
Provides traceability - auditor can verify dashboard is pulling from current, complete 
assessments. Documents data lineage.

**When to Check This Sheet:**

- Immediately after opening dashboard (before viewing other sheets)
- After updating any source workbook
- Before generating executive reports
- If any dashboard metric shows unexpected values
- During audit preparation

**Key Principle - Fail Fast:**
Dashboard should clearly indicate broken links, not silently show stale/incorrect data. 
This sheet surfaces problems immediately.

---

## Sheet 3: Overall_Compliance_Dashboard

### Purpose
Primary executive summary view - single page showing overall A.8.9 compliance posture, 
domain breakdowns, critical gaps, and key metrics.

### Structure

**Layout:** Executive dashboard format optimized for printing/PDF

**Section 1: Header**

| Attribute | Value |
|-------|-------|
| Assessment Control | ISO/IEC 27001:2022 Annex A.8.9 - Configuration Management |
| Dashboard Date | [Current Date] |
| Assessment Period | [Earliest to Latest assessment date from 4 sources] |
| Dashboard Owner | [Name from config] |
| Review Status | [Pending/Reviewed/Approved] |

**Section 2: Overall Compliance Summary (Prominent Display)**

Large, visually prominent display:
```
┌─────────────────────────────────────┐
│                                     │
│   OVERALL COMPLIANCE: XX.X%         │  ← Large font, color-coded
│                                     │
│   Target: ≥95%                      │
│   Status: [Compliant/At Risk/...]  │
│                                     │
└─────────────────────────────────────┘
```

**Overall Compliance Formula:**
```excel
Overall_Compliance = 
  (A891_Compliance * 0.20) +
  (A892_Compliance * 0.25) +
  (A893_Compliance * 0.20) +
  (A894_Compliance * 0.25) +
  (Process_Maturity * 0.10)

Where:
  A891_Compliance = '[ISMS-IMP-A.8.9.1.xlsx]Compliance_Dashboard'!B5
  A892_Compliance = '[ISMS-IMP-A.8.9.2.xlsx]Change_Summary'!B10
  A893_Compliance = '[ISMS-IMP-A.8.9.3.xlsx]Compliance_Dashboard'!B8
  A894_Compliance = '[ISMS-IMP-A.8.9.4.xlsx]Compliance_Dashboard'!B5
  Process_Maturity = [calculated from maturity indicators]
```

**Status Color Logic:**

- **Compliant** (Green): Overall ≥95% AND Critical Gaps = 0
- **Substantially Compliant** (Light Green): Overall ≥90%
- **At Risk** (Yellow): Overall 80-89% OR Critical Gaps > 0
- **Non-Compliant** (Red): Overall <80%

**Section 3: Domain Compliance Breakdown**

Table showing each domain:

| Domain | Weight | Compliance % | Target | Status | Critical Gaps | Last Assessed |
|--------|--------|--------------|--------|--------|---------------|---------------|
| Baseline Configuration | 20% | [formula] | ≥90% | [Green/Yellow/Red] | [count] | [date] |
| Change Control | 25% | [formula] | ≥90% | [Green/Yellow/Red] | [count] | [date] |
| Configuration Monitoring | 20% | [formula] | ≥90% | [Green/Yellow/Red] | [count] | [date] |
| Security Hardening | 25% | [formula] | ≥90% | [Green/Yellow/Red] | [count] | [date] |
| Process Maturity | 10% | [formula] | ≥80% | [Green/Yellow/Red] | [count] | [N/A] |

**Domain Formulas (External References):**
```excel
Baseline_Configuration = '[ISMS-IMP-A.8.9.1.xlsx]Compliance_Dashboard'!B5
Change_Control = '[ISMS-IMP-A.8.9.2.xlsx]Change_Summary'!B10
Configuration_Monitoring = '[ISMS-IMP-A.8.9.3.xlsx]Compliance_Dashboard'!B8
Security_Hardening = '[ISMS-IMP-A.8.9.4.xlsx]Compliance_Dashboard'!B5

Critical_Gaps_Baseline = '[ISMS-IMP-A.8.9.1.xlsx]Compliance_Dashboard'!B15
Critical_Gaps_Change = '[ISMS-IMP-A.8.9.2.xlsx]Change_Summary'!B18
Critical_Gaps_Monitoring = '[ISMS-IMP-A.8.9.3.xlsx]Compliance_Dashboard'!B20
Critical_Gaps_Hardening = '[ISMS-IMP-A.8.9.4.xlsx]Compliance_Dashboard'!B13
```

**Last Assessed Formulas (from source metadata if available):**
Attempt to pull assessment date from source, else show "Unknown"

**Section 4: Critical Gaps (Top 10)**

Consolidated list of highest-priority issues across all domains:

| Rank | Domain | Gap Description | Risk Rating | Asset/Area | Owner | Target Date |
|------|--------|-----------------|-------------|------------|-------|-------------|
| 1 | [Domain] | [Description] | Critical | [Asset] | [Owner] | [Date] |
| ... | ... | ... | ... | ... | ... | ... |

**Data Source:**
Pull from Gap_Prioritization sheet (which aggregates from all 4 sources)

**Section 5: Key Performance Indicators**

| KPI | Current | Target | Status | Trend |
|-----|---------|--------|--------|-------|
| Overall Compliance % | [formula] | ≥95% | [indicator] | [↑/↓/→] |
| Domains Compliant (≥90%) | [count]/5 | 5/5 | [indicator] | [↑/↓/→] |
| Total Critical Gaps | [sum] | 0 | [indicator] | [↑/↓/→] |
| Assets Fully Compliant | [%] | ≥90% | [indicator] | [↑/↓/→] |
| Evidence Completeness | [%] | ≥95% | [indicator] | [↑/↓/→] |
| Audit Readiness Score | [calc] | ≥90% | [indicator] | [↑/↓/→] |

**Trend Indicators:**

- ↑ (Improving): Current > Previous assessment
- → (Stable): Current ≈ Previous (within 2%)
- ↓ (Declining): Current < Previous assessment
- N/A: First assessment, no historical data

**Audit Readiness Score:**
```excel
Audit_Readiness = 
  (Overall_Compliance * 0.40) +
  (Evidence_Completeness * 0.30) +
  (Process_Maturity * 0.20) +
  (Executive_Oversight * 0.10)

Where:
  Evidence_Completeness = Implemented controls with evidence / Total implemented
  Executive_Oversight = 100% if Approval_Sign_Off complete, else 0%
```

**Section 6: Assessment Currency**

| Domain | Last Assessment | Days Since | Status |
|--------|----------------|------------|--------|
| Baseline Configuration | [date] | [days] | [Current/Due Soon/Overdue] |
| Change Control | [date] | [days] | [Current/Due Soon/Overdue] |
| Configuration Monitoring | [date] | [days] | [Current/Due Soon/Overdue] |
| Security Hardening | [date] | [days] | [Current/Due Soon/Overdue] |

**Status Logic:**

- **Current** (Green): <60 days since assessment
- **Due Soon** (Yellow): 60-90 days since assessment
- **Overdue** (Red): >90 days since assessment

**Section 7: Executive Summary (Text Box)**

Narrative summary (2-3 paragraphs):

- Overall compliance status and trajectory
- Key achievements since last review
- Critical gaps requiring attention
- Recommended actions for executive sponsor
- Resource requirements (if any)

This section is **manually populated** by Dashboard Owner based on quantitative data.

**Section 8: Next Steps**

Checklist format:

- [ ] All domain assessments current (<90 days)
- [ ] Critical gaps have remediation plans
- [ ] Resources allocated for gap closure
- [ ] Executive review completed
- [ ] Approval sign-off obtained
- [ ] Next assessment cycle scheduled

### Dashboard Notes

**Purpose (Implementer Perspective):**
Single-page executive summary for leadership reporting. Answers: "How well are we 
managing configurations?" without requiring deep dive into domains.

**Purpose (Auditor Perspective):**
Evidence of systematic oversight and executive engagement. Demonstrates that A.8.9 is 
governed at appropriate level.

**Conditional Formatting:**

- Overall Compliance ≥95%: Dark green background
- Overall Compliance 90-94%: Light green background
- Overall Compliance 80-89%: Yellow background
- Overall Compliance <80%: Red background
- Critical Gaps > 0: Red text, bold
- Any domain <90%: Yellow background in domain table
- Assessment >90 days old: Red background in currency table

**Print Optimization:**
Dashboard should fit on single page when printed/PDF'd. Use landscape orientation, 
adjust font sizes and spacing for optimal layout.

---

## Sheet 4: Asset_Compliance_Summary

### Purpose
Provide per-asset compliance view across all configuration management domains, enabling 
identification of assets with systemic compliance issues.

### Structure

**Columns:**

| Column | Description | Data Type | Source/Formula |
|--------|-------------|-----------|----------------|
| Asset_ID | Unique identifier | Text | From A.8.9.1 |
| Asset_Name | Descriptive name | Text | From A.8.9.1 |
| Asset_Type | Category from taxonomy | Text | From A.8.9.1 |
| Asset_Tier | Criticality | Text | From A.8.9.1 |
| Asset_Owner | Responsible person | Text | From A.8.9.1 |
| Baseline_Documented | Is baseline documented | Yes/No | From A.8.9.1 |
| Baseline_Version_Current | Is version current | Yes/No | From A.8.9.1 |
| Change_Control_Compliance | Change compliance % | Percentage | From A.8.9.2 |
| Emergency_Changes_Last_30d | Count of emergency changes | Number | From A.8.9.2 |
| Monitoring_Coverage | Is monitoring configured | Yes/No | From A.8.9.3 |
| Critical_Drift_Count | Count of critical drift | Number | From A.8.9.3 |
| Hardening_Compliance | Hardening compliance % | Percentage | From A.8.9.4 |
| High_Risk_Hardening_Gaps | Count of high-risk gaps | Number | From A.8.9.4 |
| Overall_Asset_Compliance | Aggregate compliance | Percentage | Formula |
| Compliance_Status | Status indicator | Text | Formula |
| Critical_Issues_Count | Total critical issues | Number | Formula |
| Primary_Gap_Domain | Domain with lowest score | Text | Formula |
| Remediation_Priority | Risk-based priority | Text | Formula |
| Notes | Additional information | Text | Free text |

**Overall_Asset_Compliance Formula:**
```excel
Overall_Asset_Compliance = 
  (Baseline_Score * 0.20) +
  (Change_Control_Compliance * 0.25) +
  (Monitoring_Score * 0.20) +
  (Hardening_Compliance * 0.25) +
  (Process_Score * 0.10)

Where:
  Baseline_Score = 100% if both Documented=Yes AND Version_Current=Yes, else 50% if one, else 0%
  Monitoring_Score = 100% if Coverage=Yes AND Critical_Drift_Count=0, else 50% if one, else 0%
  Process_Score = 100% if Emergency_Changes_Last_30d ≤ 2, else decreasing scale
```

**Compliance_Status Logic:**
```excel
Compliance_Status = 
  IF(Overall >= 95% AND Critical_Issues_Count = 0, "Fully Compliant",
  IF(Overall >= 90%, "Compliant", 
  IF(Overall >= 80%, "Substantially Compliant",
  IF(Overall >= 70%, "Partially Compliant", "Non-Compliant"))))
```

**Critical_Issues_Count Formula:**
```excel
Critical_Issues_Count = 
  (IF(Baseline_Documented="No", 1, 0)) +
  (IF(Critical_Drift_Count > 0, 1, 0)) +
  (IF(High_Risk_Hardening_Gaps > 0, 1, 0)) +
  (IF(Emergency_Changes_Last_30d > 5, 1, 0))
```

**Primary_Gap_Domain Formula:**

Identifies which domain has lowest compliance for this asset:
```excel
Primary_Gap_Domain = 
  IF(Baseline_Score = MIN(domain_scores), "Baseline Configuration",
  IF(Change_Control_Compliance = MIN(domain_scores), "Change Control",
  IF(Monitoring_Score = MIN(domain_scores), "Configuration Monitoring",
  "Security Hardening")))
```

**Remediation_Priority Formula:**
```excel
Remediation_Priority = 
  IF(Asset_Tier="Critical" AND Critical_Issues_Count>0, "P0 - Immediate",
  IF(Critical_Issues_Count>0, "P1 - High",
  IF(Overall<90%, "P2 - Medium", "P3 - Low")))
```

**Data Source Notes:**

This sheet aggregates data from all 4 source workbooks. For each asset:

- Pull Asset_ID from A.8.9.1 (master asset list)
- Use VLOOKUP/XLOOKUP to find same Asset_ID in A.8.9.2, A.8.9.3, A.8.9.4
- Extract relevant metrics from each domain
- Calculate aggregate compliance

**CRITICAL - External Workbook VLOOKUP:**
```excel
Change_Control_Compliance = 
  IFERROR(
    VLOOKUP(Asset_ID, 
            '[ISMS-IMP-A.8.9.2.xlsx]Change_Asset_Summary'!A:Z, 
            [column_index], 
            FALSE),
    "N/A")
```

**Row Count:** 100 rows (matches A.8.9.1 asset inventory capacity)

### Conditional Formatting

- Compliance_Status = "Fully Compliant": Dark green background
- Compliance_Status = "Compliant": Light green background
- Compliance_Status = "Substantially Compliant": Yellow background
- Compliance_Status = "Partially Compliant": Orange background
- Compliance_Status = "Non-Compliant": Red background
- Critical_Issues_Count > 0: Red text, bold
- Asset_Tier = "Critical" AND Overall < 100%: Red border
- Emergency_Changes_Last_30d > 5: Orange background
- Critical_Drift_Count > 0: Red background
- High_Risk_Hardening_Gaps > 0: Red background

### Usage Notes

**Purpose (Implementer Perspective):**
Identify assets with systemic compliance issues. Enables targeted remediation efforts 
rather than domain-by-domain approach.

**Purpose (Auditor Perspective):**
Demonstrates asset-level oversight. Auditor can sample high-risk assets and verify 
remediation plans exist.

**Key Insights:**

- **Assets with multiple domain gaps**: Need comprehensive remediation, not piecemeal fixes
- **Critical assets with any gaps**: Highest priority for immediate attention
- **Primary_Gap_Domain**: Shows which domain needs most improvement for each asset
- **Remediation_Priority**: Risk-based sequencing of remediation efforts

**Analysis Questions This Sheet Answers:**

- Which assets have compliance issues across multiple domains?
- Are critical assets fully compliant?
- Which domain is the weakest link for specific assets?
- What is the distribution of compliance across asset portfolio?

---

## Sheet 5: Gap_Prioritization

### Purpose
Consolidated gap list from all 4 domains with risk-based prioritization for remediation 
sequencing.

### Structure

**Columns:**

| Column | Description | Data Type | Source/Formula |
|--------|-------------|-----------|----------------|
| Gap_ID | Unique identifier | Text | Auto-generated |
| Source_Domain | Which domain identified gap | Dropdown | From source |
| Source_Document | Which workbook | Text | Document ID |
| Asset_ID | Affected asset | Text | From source |
| Asset_Name | Asset name | Text | From source |
| Asset_Tier | Asset criticality | Text | From source |
| Gap_Category | Type of gap | Dropdown | See below |
| Gap_Description | Description | Text | From source |
| Gap_Risk_Rating | Inherent risk | Dropdown | Critical/High/Medium/Low |
| Business_Impact | Impact description | Text | From source |
| Exploitation_Likelihood | Likelihood of exploitation | Dropdown | Very High to Very Low |
| Current_State | Current status | Text | From source |
| Required_State | Target state | Text | From source |
| Risk_Score | Calculated risk | Number | Formula |
| Priority_Rank | Overall priority | Number | Formula |
| Remediation_Owner | Person responsible | Text | From source |
| Remediation_Strategy | How to fix | Text | From source |
| Target_Date | Target completion | Date | From source |
| Days_Until_Target | Days remaining | Number | Formula |
| Status | Current status | Dropdown | From source |
| Dependencies | Prerequisites | Text | From source |
| Quick_Win | Can fix quickly | Yes/No | Formula |
| Cross_Domain_Impact | Affects multiple domains | Yes/No | Analysis |
| Notes | Additional info | Text | Free text |

**Gap_Category Dropdown Values:**

- Baseline Not Documented
- Baseline Out of Date
- Change Control Non-Compliance
- Unauthorized Change
- Configuration Drift
- Monitoring Gap
- Hardening Control Missing
- Exception Without Justification
- Process Deficiency

**Risk_Score Formula:**
```excel
Risk_Score = 
  (Asset_Tier_Weight * 10) +
  (Gap_Risk_Rating_Weight * 8) +
  (Exploitation_Likelihood_Weight * 6) +
  (Cross_Domain_Penalty * 4) +
  (Days_Overdue_Penalty * 2)

Weights same as A.8.9.4 (RISK_WEIGHTS config)
Cross_Domain_Penalty = 5 if Cross_Domain_Impact = Yes, else 0
Days_Overdue_Penalty = IF(Days_Until_Target < 0, ABS(Days_Until_Target)/7, 0)
```

**Priority_Rank Formula:**

Rank gaps by Risk_Score descending (highest risk = Rank 1)

**Quick_Win Formula:**
```excel
Quick_Win = 
  IF(AND(
    OR(Gap_Risk_Rating="Medium", Gap_Risk_Rating="High", Gap_Risk_Rating="Critical"),
    OR(Remediation_Strategy contains "Configuration Change",
       Remediation_Strategy contains "Policy Update",
       Estimated effort < 1 day)),
    "Yes", "No")
```

**Cross_Domain_Impact Analysis:**

Manual or formula-based determination of whether gap affects multiple domains:

- Baseline not documented → Impacts monitoring and hardening
- Unauthorized change → Impacts baseline, monitoring, and hardening
- Monitoring gap → Cannot detect drift or hardening violations

**Data Source:**

This sheet aggregates gaps from all 4 source workbooks:
```excel
// Pseudo-logic for data aggregation
FOR EACH domain IN [A.8.9.1, A.8.9.2, A.8.9.3, A.8.9.4]:
  Pull gaps from domain's Gap/Remediation sheet
  Append to consolidated list with Source_Domain tag
  Calculate Risk_Score
  Determine Cross_Domain_Impact

SORT by Risk_Score descending
ASSIGN Priority_Rank (1 to N)
```

**Row Count:** 150 rows (aggregate capacity across all domains)

### Conditional Formatting

- Priority_Rank 1-10: Red background (top 10 priorities)
- Priority_Rank 11-30: Orange background
- Priority_Rank 31-50: Yellow background
- Quick_Win = "Yes": Green border (highlight quick wins)
- Asset_Tier = "Critical": Bold text
- Days_Until_Target < 0: Red text (overdue)
- Cross_Domain_Impact = "Yes": Blue background
- Status = "Blocked": Gray background

### Usage Notes

**Purpose (Implementer Perspective):**
Single prioritized work list for remediation teams. Answers: "What should we fix first?" 
across all configuration management domains.

**Purpose (Auditor Perspective):**
Demonstrates systematic gap management. Shows organization prioritizes based on risk, 
not arbitrary factors.

**Remediation Strategies:**

**Strategy 1: Quick Wins First**

- Filter for Quick_Win = "Yes" AND Priority_Rank ≤ 50
- Target: Close all quick wins within 30 days
- Benefit: Rapid compliance improvement, team momentum

**Strategy 2: Critical Asset Focus**

- Filter for Asset_Tier = "Critical"
- Target: Zero gaps on critical assets
- Benefit: Highest business risk mitigation

**Strategy 3: Cross-Domain Impact**

- Filter for Cross_Domain_Impact = "Yes"
- Target: Close multi-domain gaps first
- Benefit: One fix improves multiple domains

**Strategy 4: Top 20**

- Focus on Priority_Rank 1-20 regardless of other factors
- Target: Close top 20 within 60 days
- Benefit: Addresses highest aggregate risk

**Key Insights:**

- **Gap distribution by domain**: Which domain has most gaps?
- **Quick win percentage**: How many easy fixes available?
- **Cross-domain gaps**: Systemic issues vs. isolated problems
- **Overdue gap count**: Are we keeping pace with remediation?

---

## Sheet 6: Trend_Analysis

### Purpose
Track compliance trajectory over time to demonstrate continuous improvement and identify 
concerning trends.

### Structure

**CRITICAL NOTE:** This sheet requires historical data. For first assessment cycle, 
sheet will contain minimal data with instructions to populate in future cycles.

**Section 1: Assessment History**

Table documenting each assessment cycle:

| Cycle | Assessment Date | Baseline % | Change % | Monitoring % | Hardening % | Process % | Overall % |
|-------|----------------|------------|----------|--------------|-------------|-----------|-----------|
| 1 | [date] | [%] | [%] | [%] | [%] | [%] | [%] |
| 2 | [date] | [%] | [%] | [%] | [%] | [%] | [%] |
| 3 | [date] | [%] | [%] | [%] | [%] | [%] | [%] |
| ... | ... | ... | ... | ... | ... | ... | ... |

**Data Entry:** Manually populated after each assessment cycle. Copy current compliance 
percentages from Overall_Compliance_Dashboard.

**Row Capacity:** 20 cycles (5 years at quarterly assessments)

**Section 2: Trend Indicators**

| Domain | Current % | Previous % | Change | Trend | Status |
|--------|-----------|------------|--------|-------|--------|
| Baseline Configuration | [current] | [previous] | [delta] | [↑/↓/→] | [Green/Yellow/Red] |
| Change Control | [current] | [previous] | [delta] | [↑/↓/→] | [Green/Yellow/Red] |
| Configuration Monitoring | [current] | [previous] | [delta] | [↑/↓/→] | [Green/Yellow/Red] |
| Security Hardening | [current] | [previous] | [delta] | [↑/↓/→] | [Green/Yellow/Red] |
| Process Maturity | [current] | [previous] | [delta] | [↑/↓/→] | [Green/Yellow/Red] |
| **Overall Compliance** | [current] | [previous] | [delta] | [↑/↓/→] | [Green/Yellow/Red] |

**Trend Calculation:**
```excel
Trend = 
  IF(Current - Previous > 2%, "↑ Improving",
  IF(Current - Previous < -2%, "↓ Declining",
  "→ Stable"))
```

**Status Logic:**

- Green: Current ≥90% AND (Improving OR Stable)
- Yellow: Current 80-89% OR Declining <5%
- Red: Current <80% OR Declining ≥5%

**Section 3: Gap Trend Analysis**

Track gap count over time:

| Cycle | Total Gaps | Critical Gaps | High Gaps | Gaps Closed | Gaps Opened | Net Change |
|-------|------------|---------------|-----------|-------------|-------------|------------|
| 1 | [count] | [count] | [count] | - | - | - |
| 2 | [count] | [count] | [count] | [count] | [count] | [+/-] |
| 3 | [count] | [count] | [count] | [count] | [count] | [+/-] |

**Net Change Formula:**
```excel
Net_Change = Gaps_Closed - Gaps_Opened
```

**Target:** Positive net change each cycle (more gaps closed than opened)

**Section 4: Compliance Trajectory Chart**

**Chart Type:** Line chart with multiple series

**X-Axis:** Assessment cycle (or date)

**Y-Axis:** Compliance percentage (0-100%)

**Series:**

- Overall Compliance (bold line)
- Baseline Configuration
- Change Control
- Configuration Monitoring
- Security Hardening
- Process Maturity
- Target line at 95% (horizontal reference)

**Section 5: Time to Remediate Analysis**

Track remediation efficiency:

| Cycle | Gaps Identified | Gaps Closed | Days to Close (Avg) | Closure Rate |
|-------|----------------|-------------|---------------------|--------------|
| 1 | [count] | [count] | [days] | [%] |
| 2 | [count] | [count] | [days] | [%] |
| 3 | [count] | [count] | [days] | [%] |

**Closure Rate Formula:**
```excel
Closure_Rate = Gaps_Closed / Gaps_Identified * 100%
```

**Target:** Closure rate ≥80%, Days to Close trending downward

**Section 6: Predictive Analysis (Optional)**

If sufficient historical data (6+ cycles):

| Metric | Current | Projected (Next Cycle) | Projection Basis |
|--------|---------|------------------------|------------------|
| Overall Compliance | [%] | [%] | Linear regression |
| Critical Gap Count | [count] | [count] | Moving average |
| Time to 100% Compliance | - | [months] | Trend extrapolation |

**Projection Note:** "Projections based on historical trend. Actual results may vary."

**Section 7: First Assessment Guidance**

For organizations completing first assessment:

**Message Box:**
```
TREND ANALYSIS - FIRST ASSESSMENT

This is your baseline assessment. Trend analysis requires 3+ assessment cycles to 
generate meaningful insights.

Next Steps:
1. Schedule next assessment (recommend quarterly)
2. After 2nd assessment: Compare Current vs. Baseline
3. After 3rd assessment: Begin trend analysis
4. After 4th assessment: Predictive analysis becomes available

Maintain consistency in assessment methodology across cycles to ensure valid comparisons.

Current assessment establishes your baseline:
  • Overall Compliance: [X.X%]
  • Total Gaps: [count]
  • Critical Gaps: [count]
  
Target for next cycle: Improve by ≥5 percentage points or close ≥50% of gaps.
```

### Usage Notes

**Purpose (Implementer Perspective):**
Demonstrates continuous improvement to leadership. Shows that configuration management 
is improving over time, not static.

**Purpose (Auditor Perspective):**
Evidence of ongoing monitoring and improvement. Auditor can verify organization is not 
just compliant now, but getting better.

**Maintaining Historical Data:**

**After Each Assessment Cycle:**
1. Open Trend_Analysis sheet
2. Add new row to Assessment History table
3. Copy current domain compliance percentages from Overall_Compliance_Dashboard
4. Update gap counts from Gap_Prioritization
5. Calculate trends and net changes
6. Update chart data range if needed
7. Save as new version of dashboard

**Best Practice - Version Control:**

- Keep previous dashboard versions: `ISMS-IMP-A.8.9.5_CycleN.xlsx`
- Maintains historical audit trail
- Allows comparison if discrepancies arise
- Supports trend validation

**Data Integrity:**

- Use consistent assessment methodology across cycles
- Same assessors if possible (reduces measurement bias)
- Same target populations (adjust for new/decommissioned assets)
- Document any methodology changes that affect comparability

---

## Sheet 7: Evidence_Register

### Purpose
Consolidated evidence index linking to domain-specific evidence in source workbooks.

### Structure

**Columns:**

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Evidence_ID | Unique identifier | Text | Auto-generated |
| Source_Domain | Which domain | Dropdown | 4 domains |
| Source_Document | Document ID | Text | ISMS-IMP-A.8.9.X |
| Source_Evidence_ID | ID in source workbook | Text | From source |
| Evidence_Type | Category | Dropdown | See below |
| Evidence_Description | What this shows | Text | From source |
| Related_Control_Area | A.8.9 subdomain | Text | Free text |
| Collection_Date | When collected | Date | Valid date |
| Evidence_Location | Where stored | Text | From source |
| Evidence_Status | Current status | Dropdown | Active/Expired/Superseded |
| Verification_Status | Has been verified | Dropdown | Verified/Pending/Failed |
| Audit_Reference | Audit tracking | Text | Free text |
| Notes | Additional info | Text | Free text |

**Evidence_Type Dropdown Values:**

- Baseline Documentation
- Configuration Export
- Change Record
- Approval Documentation
- Monitoring Report
- Alert Configuration
- Drift Detection Log
- Hardening Assessment Report
- Exception Approval
- Risk Assessment
- Process Documentation
- Training Records

**Data Source:**

This sheet consolidates evidence references from all 4 source workbooks:
```excel
// Pseudo-logic
FOR EACH domain IN [A.8.9.1, A.8.9.2, A.8.9.3, A.8.9.4]:
  Pull evidence records from domain's Evidence_Register
  Append to consolidated list with Source_Domain and Source_Document tags
  Create hyperlink to source evidence record if possible
```

**Row Count:** 100 rows

**Hyperlink to Source Evidence:**

If possible, create Excel hyperlinks to jump directly to source evidence:
```excel
Hyperlink_Formula = 
  HYPERLINK(
    "[" & Source_Document & ".xlsx]Evidence_Register!A" & [source_row],
    "View in " & Source_Domain)
```

### Conditional Formatting

- Evidence_Status = "Expired": Red background
- Evidence_Status = "Superseded": Gray background
- Verification_Status = "Failed": Red background
- Verification_Status = "Pending": Yellow background

### Usage Notes

**Purpose (Implementer Perspective):**
Quick reference index of all evidence supporting A.8.9 compliance. Facilitates audit 
preparation by providing consolidated evidence list.

**Purpose (Auditor Perspective):**
Evidence roadmap for audit sampling. Auditor can select evidence items to review without 
searching through 4 separate workbooks.

**Audit Preparation:**
1. Generate Evidence_Register from all 4 sources
2. Review for completeness (no expired/failed evidence)
3. Ensure evidence locations are accessible
4. Prepare evidence packages for auditor sampling
5. Link evidence to specific A.8.9 control requirements

**Evidence Quality Checks:**

- All "Implemented" controls have supporting evidence
- Evidence is recent (within validity period)
- Evidence location is documented and accessible
- Verification status is "Verified" for all audit-critical evidence

---

## Sheet 8: Approval_Sign_Off

### Purpose
Document executive review and approval of overall A.8.9 compliance status.

### Structure

**Section 1: Dashboard Summary**

| Attribute | Value |
|-------|-------|
| Assessment Period | [date range] |
| Overall Compliance | [percentage] |
| Compliance Status | [Compliant/At Risk/Non-Compliant] |
| Total Critical Gaps | [count] |
| Domains Compliant | [count]/5 |
| Assessment Currency | [All Current/Some Stale/Stale] |

**Section 2: Executive Summary**

**Narrative (manually entered by Dashboard Owner):**

Template structure:
```
OVERALL STATUS:
[Summary of overall compliance posture]

KEY ACHIEVEMENTS:

- [Achievement 1]
- [Achievement 2]
- [Achievement 3]

CRITICAL GAPS:

- [Gap 1 with impact and remediation plan]
- [Gap 2 with impact and remediation plan]
- [Gap 3 with impact and remediation plan]

RESOURCE REQUIREMENTS:
[Any additional resources needed for remediation]

RECOMMENDATIONS:
[Actions recommended for executive approval]

NEXT ASSESSMENT:
Scheduled for [date]
```

**Section 3: Risk Assessment**

| Risk Category | Current Status | Description | Mitigation |
|---------------|---------------|-------------|------------|
| Configuration Integrity | [Green/Yellow/Red] | [Description] | [Plan] |
| Change Management | [Green/Yellow/Red] | [Description] | [Plan] |
| Drift Detection | [Green/Yellow/Red] | [Description] | [Plan] |
| Security Hardening | [Green/Yellow/Red] | [Description] | [Plan] |
| Governance & Oversight | [Green/Yellow/Red] | [Description] | [Plan] |

**Section 4: Three-Tier Approval**

**Tier 1 - Operational Review:**

| Role | Name | Date | Signature | Comments |
|------|------|------|-----------|----------|
| Dashboard Owner | [Name] | [Date] | [Signature] | Dashboard complete |
| ISMS Manager | [Name] | [Date] | [Signature] | Metrics validated |

**Tier 2 - Management Review:**

| Role | Name | Date | Signature | Comments |
|------|------|------|-----------|----------|
| IT Manager | [Name] | [Date] | [Signature] | Resources committed |
| Security Manager | [Name] | [Date] | [Signature] | Gaps prioritized |

**Tier 3 - Executive Acceptance:**

| Role | Name | Date | Signature | Comments |
|------|------|------|-----------|----------|
| CISO / CIO | [Name] | [Date] | [Signature] | Risk accepted |

**Approval Thresholds:**

- Overall ≥95%: Tier 2 approval sufficient
- Overall 90-94%: Tier 3 review recommended
- Overall <90% OR Critical Gaps >0: Tier 3 approval REQUIRED

**Section 5: Action Items**

| Action | Owner | Target Date | Status | Notes |
|--------|-------|-------------|--------|-------|
| [Action 1] | [Owner] | [Date] | [Status] | [Notes] |
| [Action 2] | [Owner] | [Date] | [Status] | [Notes] |
| [Action 3] | [Owner] | [Date] | [Status] | [Notes] |

**Section 6: Next Steps**

Checklist:

- [ ] All 4 domain assessments refreshed for next cycle
- [ ] Critical gaps remediated or risk accepted
- [ ] Resources allocated per action items
- [ ] Trend analysis updated with current cycle data
- [ ] Next executive review scheduled
- [ ] Dashboard distributed to stakeholders

**Section 7: Distribution List**

Document distributed to:

- Executive Leadership (CISO, CIO, CEO)
- IT Management
- Security Team
- Risk Management
- Internal Audit
- External Auditors (upon request)
- [Other stakeholders as appropriate]

**Section 8: Revision History**

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [date] | Initial dashboard | [name] |
| 1.1 | [date] | Q2 update | [name] |
| 1.2 | [date] | Q3 update | [name] |

### Usage Notes

**Purpose (Implementer Perspective):**
Formal closure of assessment cycle. Ensures executive accountability and commitment to 
remediation.

**Purpose (Auditor Perspective):**
Evidence of governance. Shows configuration management is overseen at appropriate level 
and risk is formally accepted by executives.

**When to Complete:**

- After all 4 domain assessments are current
- After dashboard metrics are validated
- Before presenting to external auditors
- Before next assessment cycle begins

**Governance Cadence:**

- **Dashboard Review**: Monthly by ISMS Manager
- **Management Review**: Quarterly by IT/Security Managers  
- **Executive Review**: Quarterly by CISO/CIO (or when Overall <90%)

---

## Dashboard Operation & Maintenance

### Initial Setup (First Time)

1. **Complete All Domain Assessments**

   - Generate A.8.9.1 through A.8.9.4 workbooks
   - Complete all assessment sheets
   - Validate data quality

2. **Normalize Source Workbooks**
```bash
   python3 normalize_assessment_files_a89.py --source ./assessments --output ./dashboard
```
   
   This creates date-free copies:

   - ISMS-IMP-A.8.9.1.xlsx
   - ISMS-IMP-A.8.9.2.xlsx
   - ISMS-IMP-A.8.9.3.xlsx
   - ISMS-IMP-A.8.9.4.xlsx

3. **Generate Dashboard**
```bash
   python3 generate_a89_5_dashboard.py
```

4. **Place Dashboard with Sources**

   - Move generated dashboard to same directory as normalized workbooks
   - Ensure all 5 files are in same folder

5. **Open and Link**

   - Open dashboard workbook
   - Excel prompts: "Update Links?" → Click "Update"
   - Verify Workbook_Integration_Settings shows all 4 sources linked

6. **Validate Data**

   - Check Overall_Compliance_Dashboard for reasonable metrics
   - Verify no #REF! errors in any sheet
   - Spot-check a few external formulas resolve correctly

7. **Complete Narrative Sections**

   - Fill in Executive Summary in Overall_Compliance_Dashboard
   - Complete Risk Assessment in Approval_Sign_Off
   - Document any manual adjustments

8. **Obtain Approvals**

   - Present to management
   - Obtain three-tier sign-offs
   - Distribute to stakeholders

### Refresh Process (Subsequent Cycles)

1. **Update Domain Assessments**

   - Re-run domain assessment scripts with current data
   - Or update existing domain workbooks manually
   - Save domain workbooks

2. **Re-Normalize**
```bash
   python3 normalize_assessment_files_a89.py --source ./assessments --output ./dashboard --auto-confirm
```
   
   This overwrites normalized files with current data

3. **Refresh Dashboard**

   - Close dashboard if open
   - Re-open dashboard
   - Click "Update Links" when prompted
   - Excel automatically pulls latest data from source workbooks

4. **Update Trend Analysis**

   - Manually add new row to Assessment_History table
   - Copy current compliance percentages
   - Update gap counts
   - Verify chart updates automatically

5. **Review and Approve**

   - Review updated metrics
   - Update Executive Summary if needed
   - Obtain fresh approvals
   - Update Revision History

### Troubleshooting

**Problem: #REF! errors in dashboard**

Cause: External workbook links broken

Solution:
1. Verify all 4 normalized workbooks are in same directory as dashboard
2. Check filenames match exactly: `ISMS-IMP-A.8.9.X.xlsx` (no dates)
3. Excel → Data → Edit Links → Check Status
4. If "Source not found": Update link to correct path
5. Click "Update Values"

**Problem: Metrics seem incorrect**

Cause: Source workbook structure changed or data entry error

Solution:
1. Check Workbook_Integration_Settings → Data Pull Test
2. Identify which source has issue
3. Open problematic source workbook
4. Verify expected sheets exist with correct names
5. Verify expected cells contain expected data types
6. Re-save source workbook
7. Refresh dashboard links

**Problem: "This workbook contains links to other data sources"**

Cause: Normal Excel behavior for external links

Solution:

- This is expected - dashboard uses external links by design
- Click "Update" to refresh from current source data
- Click "Don't Update" to keep stale data (not recommended)
- To suppress warning: File → Options → Advanced → General → "Ask to update automatic links" (uncheck)

**Problem: Dashboard shows stale data**

Cause: Links not updated or source workbooks not refreshed

Solution:
1. Save and close dashboard
2. Verify source workbooks are current (check Last_Modified dates)
3. If sources are stale: Update source assessments, re-normalize
4. Re-open dashboard
5. Click "Update Links"

**Problem: Trend_Analysis shows no data**

Cause: First assessment cycle (no historical data)

Solution:

- This is expected for first assessment
- Review "First Assessment Guidance" message in Trend_Analysis sheet
- Populate historical data after 2nd and subsequent cycles
- Maintain consistent assessment schedule for valid trends

---

## Quality Assurance & Validation

### Pre-Release Validation

Before distributing dashboard to stakeholders:

1. **Link Validation**

   - [ ] All 4 source workbooks linked (Workbook_Integration_Settings)
   - [ ] No #REF! errors in any sheet
   - [ ] Data Pull Test shows all "Pass"
   - [ ] Overall_Compliance_Dashboard shows reasonable metrics

2. **Data Integrity**

   - [ ] Overall compliance aligns with domain averages
   - [ ] Gap counts match sum of domain gaps
   - [ ] Asset counts consistent across sheets
   - [ ] Dates are current (not test dates)

3. **Narrative Completeness**

   - [ ] Executive Summary populated
   - [ ] Risk Assessment completed
   - [ ] Action Items documented
   - [ ] Approval Sign-Off ready for signatures

4. **Formula Accuracy**

   - [ ] Spot-check weighted average calculation
   - [ ] Verify external reference formulas resolve
   - [ ] Test conditional formatting triggers correctly
   - [ ] Validate Risk_Score calculations

5. **Presentation Quality**

   - [ ] Overall_Compliance_Dashboard fits on one page
   - [ ] Charts display correctly
   - [ ] Conditional formatting visible
   - [ ] No truncated text or ###### column width errors

### Post-Approval Validation

After executive sign-off:

1. **Audit Trail**

   - [ ] Approval_Sign_Off has all signatures
   - [ ] Revision History updated
   - [ ] Distribution List complete
   - [ ] Dashboard saved with appropriate version number

2. **Archival**

   - [ ] Copy saved to archive directory with date
   - [ ] Normalization manifest saved with dashboard
   - [ ] Source workbooks archived for audit trail

3. **Stakeholder Distribution**

   - [ ] PDF version generated for email distribution
   - [ ] Dashboard distributed per distribution list
   - [ ] SharePoint/document repository updated

4. **Next Cycle Planning**

   - [ ] Next assessment dates scheduled
   - [ ] Assessors assigned
   - [ ] Reminder calendar entries created

---

## Implementation Guidance

### Phased Rollout

**Phase 1: Initial Assessment (Month 1)**

- Complete all 4 domain assessments
- Generate and normalize workbooks
- Create first dashboard
- Establish baselines

**Phase 2: Process Refinement (Month 2-3)**

- Review dashboard with stakeholders
- Refine data collection processes
- Address initial gaps
- Document lessons learned

**Phase 3: Second Cycle (Month 4)**

- Refresh domain assessments
- Update dashboard
- Begin trend analysis
- Demonstrate improvement

**Phase 4: Steady State (Month 5+)**

- Quarterly assessment cycles
- Continuous gap remediation
- Regular executive reporting
- Trend-based optimization

### Success Indicators

**You're doing it right if:**

- Dashboard updates are quick (<1 hour to refresh all data)
- Executive reviews happen on schedule
- Compliance trend is upward
- Gap closure rate > gap identification rate
- Auditors require minimal explanation of dashboard
- Stakeholders use dashboard for decision-making
- Process feels systematic, not ad-hoc

**Red flags:**

- Dashboard shows stale data (>90 days old)
- External links frequently broken
- Metrics seem implausible or inconsistent
- Gaps persist across multiple cycles without remediation
- Executive reviews are cursory or skipped
- Dashboard used only for audit prep (not ongoing management)

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.9.5 |
| **Version** | 1.0 |
| **Document Type** | Implementation Dashboard - Configuration Management Compliance |
| **Related Policy** | ISMS-POL-A.8.9 (All Sections) |
| **Purpose** | Provide consolidated view of configuration management maturity across all four domains with executive dashboard and compliance metrics |
| **Target Audience** | CISO, Configuration Manager, IT Leadership, Executive Management, Risk Management, Compliance Officers, Auditors |
| **Review Cycle** | Annual (or upon significant infrastructure/tool changes) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial implementation specification with user completion guide | ISMS Implementation Team |

### Approvers

- Primary: Configuration Manager
- Technical Review: Security Architect
- Security Review: Chief Information Security Officer (CISO)

### Distribution

Configuration management team, system administrators, IT operations, security engineers, auditors

### Related Documents

- ISMS-POL-A.8.9: Configuration Management Policy (Consolidated)
- ISMS-CTX-A.8.9: Configuration Management Reference (NOT ISMS)

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->

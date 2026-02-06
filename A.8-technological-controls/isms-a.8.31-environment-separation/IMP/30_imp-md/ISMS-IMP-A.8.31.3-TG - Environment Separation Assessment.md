**ISMS-IMP-A.8.31.3-TG - Environment Separation Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production Environments

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.31.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard & Executive Summary |
| **Related Policy** | ISMS-POL-A.8.31, Section 3 (Assessment & Evidence Framework) |
| **Purpose** | Consolidate architecture and access control assessments, calculate compliance scores, generate executive dashboard, and track remediation progress |
| **Target Audience** | CISO, Executive Management, Information Security Team, IT Operations, Auditors |
| **Assessment Type** | Consolidated Dashboard |
| **Review Cycle** | Quarterly (after completing A.8.31.1 and A.8.31.2) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Compliance Dashboard workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.31.3-UG.

---

# Technical Specification

## Workbook Structure

### Overview

The Environment Separation Compliance Dashboard workbook consists of 8 sheets:

1. **Executive_Summary** - 1-page dashboard for CISO/executives with key metrics
2. **Environment_Separation_Status** - Consolidated view of environment separation compliance from A.8.31.1
3. **Access_Control_Summary** - Consolidated view of access control compliance from A.8.31.2
4. **Gap_Analysis_Remediation** - All gaps from A.8.31.1 + A.8.31.2 with remediation tracking
5. **Risk_Register** - Risk-prioritized gap tracking and risk treatment
6. **Evidence_Summary** - Consolidated evidence package from both source assessments
7. **Trend_Analysis** - Historical compliance tracking (if available)
8. **Approval_Sign_Off** - Multi-level approval workflow and signatures

---

## Sheet 1: Instructions & Legend

### Header Section

- **Row 1 (Merged A1:G1):** Title
  - Text: "ISMS-IMP-A.8.31.3 — Environment Separation Compliance Dashboard"
  - Style: Dark blue header (003366), white text, bold, centered, 40px height
  
- **Row 2 (Merged A2:G2):** Subtitle
  - Text: "ISO/IEC 27001:2022 - Control A.8.31: Executive Compliance Summary & Trend Analysis"
  - Style: Medium blue header (4472C4), white text, centered, 30px height

### Document Information Block (Rows 4-12)

| Row | Column A (Label) | Column B (Value) | Column B Style |
|-----|------------------|------------------|----------------|
| 4 | Document ID: | ISMS-IMP-A.8.31.3 | Plain text |
| 5 | Dashboard Area: | Compliance Dashboard & Executive Summary | Plain text |
| 6 | Related Policy: | ISMS-POL-A.8.31, Section 3 | Plain text |
| 7 | Version: | 1.0 | Plain text |
| 8 | Assessment Quarter: | [USER INPUT: Q1 2026] | Yellow fill (FFEB9C), bold |
| 9 | Dashboard Date: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 10 | Completed By: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 11 | Organization: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 12 | Review Cycle: | Quarterly | Plain text |

### How to Use This Dashboard (Rows 14-23)

- **Row 14:** "How to Use This Dashboard" (bold, underlined)
- **Rows 15-23:** Numbered instructions (1-9)

```
1. PREREQUISITE: Complete ISMS-IMP-A.8.31.1 and ISMS-IMP-A.8.31.2 FIRST
2. Import gap data from both source assessments (Sheet 2)
3. Import compliance status from all domains (Sheet 3)
4. Verify compliance scoring calculations (Sheet 4 - mostly auto-calculated)
5. Complete Executive Summary with commentary (Sheet 5)
6. If historical data available, complete Trend Analysis (Sheet 6)
7. Create risk-prioritized Remediation Action Plan (Sheet 7)
8. Complete Audit Readiness Checklist (Sheet 8)
9. Present to CISO for executive approval
```

### Compliance Grading Scale (Rows 25-30)

| Score Range | Grade | Description | Color Code |
|-------------|-------|-------------|------------|
| 95-100% | ✅ Excellent | Minor refinements only | Dark Green (00B050) |
| 90-94% | ✅ Compliant | Some gaps, manageable | Green (C6EFCE) |
| 70-89% | ⚠️ Partial | Significant gaps, remediation needed | Yellow (FFEB9C) |
| <70% | ❌ Non-Compliant | Major gaps, immediate action | Red (FFC7CE) |

### Critical Metrics (Rows 32-36)

- **Row 32:** "Critical Compliance Metrics" (bold, underlined)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Developer Production Access | 0 | [From A.8.31.2, Sheet 4] | [✅ if 0, 🔴 if >0] |
| Data Separation Compliance | 100% | [From A.8.31.1, Sheet 5] | [✅/⚠️/❌] |
| Overall Compliance Score | ≥90% | [Calculated in Sheet 4] | [✅/⚠️/❌] |

---

## Sheet 2: Consolidated_Gap_Analysis

### Purpose
Consolidate all gaps from both source assessments (A.8.31.1 + A.8.31.2) into single inventory.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:K1):** "CONSOLIDATED GAP ANALYSIS"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:K2):** "Import ALL gaps from A.8.31.1 (Architecture) + A.8.31.2 (Access Control) - deduplicate if necessary"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Gap Count Summary (Rows 4-9)

| Row | Metric | Formula | Display |
|-----|--------|---------|---------|
| 4 | Total Gaps | =COUNTA(A12:A1000)-1 | Bold, large font |
| 5 | 🔴 Critical | =COUNTIF(E12:E1000,"🔴 Critical") | Red text |
| 6 | 🟡 High | =COUNTIF(E12:E1000,"🟡 High") | Orange text |
| 7 | 🟢 Medium | =COUNTIF(E12:E1000,"🟢 Medium") | Yellow text |
| 8 | ⚪ Low | =COUNTIF(E12:E1000,"⚪ Low") | Gray text |
| 9 | Open Gaps | =COUNTIF(G12:G1000,"Open")+COUNTIF(G12:G1000,"Assigned")+COUNTIF(G12:G1000,"In Progress") | Bold |

### Column Headers (Row 11)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Gap ID | 15 | Text |
| B | Source Assessment | 20 | Dropdown |
| C | Gap Description | 50 | Text |
| D | Policy Requirement Violated | 35 | Text |
| E | Risk Severity | 15 | Dropdown |
| F | Current Risk | 35 | Text |
| G | Status | 15 | Dropdown |
| H | Owner | 20 | Text |
| I | Target Date | 15 | Date |
| J | % Complete | 12 | Number (%) |
| K | Source Sheet | 20 | Text |

**Row 11 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column B: Source Assessment**

- ISMS-IMP-A.8.31.1 (Architecture)
- ISMS-IMP-A.8.31.2 (Access Control)

**Column E: Risk Severity**

- 🔴 Critical
- 🟡 High
- 🟢 Medium
- ⚪ Low

**Column G: Status**

- Open
- Assigned
- In Progress
- Pending Verification
- Resolved
- Risk Accepted

### Sample Data (Rows 12-17)

| Gap ID | Source | Description | Policy Violated | Severity | Current Risk | Status | Owner | Target | % Complete | Source Sheet |
|--------|--------|-------------|-----------------|----------|--------------|--------|-------|--------|------------|--------------|
| ARCH-GAP-001 | A.8.31.1 | Developer workstations can ping production database | ISMS-POL-A.8.31, S2.1 | 🔴 Critical | Network isolation violation | In Progress | Network Admin | 2026-01-30 | 75% | A.8.31.1, Sheet 8 |
| ACCESS-GAP-001 | A.8.31.2 | 1 developer has production read-only access | ISMS-POL-A.8.31, S2.2 | 🔴 Critical | Security violation | In Progress | IAM Admin | 2026-01-25 | 90% | A.8.31.2, Sheet 8 |
| ARCH-GAP-002 | A.8.31.1 | Production credentials not in PAM vault | ISMS-POL-A.8.31, S2.1 | 🟡 High | Credential management gap | Assigned | Security Eng | 2026-02-28 | 0% | A.8.31.1, Sheet 8 |

### Import Instructions

**From A.8.31.1, Sheet 8 (Gap_Analysis):**

- Copy all gap rows
- Prefix Gap ID with "ARCH-" (e.g., ARCH-GAP-001)
- Set Source Assessment = "ISMS-IMP-A.8.31.1 (Architecture)"
- Document Source Sheet = "A.8.31.1, Sheet 8"

**From A.8.31.2, Sheet 8 (Gap_Analysis):**

- Copy all gap rows
- Prefix Gap ID with "ACCESS-" (e.g., ACCESS-GAP-001)
- Set Source Assessment = "ISMS-IMP-A.8.31.2 (Access Control)"
- Document Source Sheet = "A.8.31.2, Sheet 8"

**Deduplication:**

- If same gap appears in both assessments, keep one and note both sources

### Conditional Formatting

**Row highlighting by severity:**

- 🔴 Critical: Red fill (FFC7CE)
- 🟡 High: Orange fill (FFD966)
- 🟢 Medium: Yellow fill (FFEB9C)
- ⚪ Low: Light gray fill (F2F2F2)

---

## Sheet 3: Compliance_Status_by_Domain

### Purpose
Extract compliance status from all domains across both source assessments.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:F1):** "COMPLIANCE STATUS BY DOMAIN"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:F2):** "Extract compliance status from ALL domains in A.8.31.1 and A.8.31.2"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Overall Summary (Rows 4-7)

| Row | Metric | Formula | Display |
|-----|--------|---------|---------|
| 4 | Total Domains | =COUNTA(A10:A1000)-1 | Bold |
| 5 | ✅ Compliant Domains (≥90%) | =COUNTIF(D10:D1000,"≥90%") | Green text |
| 6 | ⚠️ Partial Domains (70-89%) | =COUNTIFS(D10:D1000,"<90%",D10:D1000,"≥70%") | Yellow text |
| 7 | ❌ Non-Compliant Domains (<70%) | =COUNTIF(D10:D1000,"<70%") | Red text |

### Column Headers (Row 9)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Domain | 30 | Text |
| B | Compliant Count | 18 | Number |
| C | Total Count | 15 | Number |
| D | Compliance % | 15 | Number (%) |
| E | Status | 18 | Dropdown |
| F | Source Sheet | 25 | Text |

**Row 9 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column E: Status**

- ✅ Compliant (≥90%)
- ⚠️ Partial (70-89%)
- ❌ Non-Compliant (<70%)

### Domain Structure (Rows 10+)

**Architecture Domains (from A.8.31.1):**

| Domain | Compliant | Total | % | Status | Source |
|--------|-----------|-------|---|--------|--------|
| Network Separation | [Manual count from A.8.31.1, Sheet 3] | [Total environments] | [Calculated] | [Auto from %] | A.8.31.1, Sheet 3 |
| Infrastructure Separation | [Manual count from A.8.31.1, Sheet 4] | [Total environments] | [Calculated] | [Auto from %] | A.8.31.1, Sheet 4 |
| Data Separation | [Manual count from A.8.31.1, Sheet 5] | [Total environments] | [Calculated] | [Auto from %] | A.8.31.1, Sheet 5 |
| Credential Separation | [Manual count from A.8.31.1, Sheet 6] | [Total credential types] | [Calculated] | [Auto from %] | A.8.31.1, Sheet 6 |
| Configuration Consistency | [Manual count from A.8.31.1, Sheet 7] | [Total config items] | [Calculated] | [Auto from %] | A.8.31.1, Sheet 7 |

**Access Control Domains (from A.8.31.2):**

| Domain | Compliant | Total | % | Status | Source |
|--------|-----------|-------|---|--------|--------|
| Access Matrix Compliance | [Manual count from A.8.31.2, Sheet 3] | [Total users] | [Calculated] | [Auto from %] | A.8.31.2, Sheet 3 |
| Production Access Restrictions | [Developer count from A.8.31.2, Sheet 4, Row 9] | N/A (Target: 0) | [100% if 0, 0% if >0] | [✅ if 0, ❌ if >0] | A.8.31.2, Sheet 4 |
| MFA Enforcement | [Manual count from A.8.31.2, Sheet 5] | [Total prod users] | [Calculated] | [Auto from %] | A.8.31.2, Sheet 5 |
| Break-Glass Controls | [Usage frequency assessment from A.8.31.2, Sheet 6] | N/A | [100% if Rare, 50% if Occasional, 0% if Frequent] | [Auto from %] | A.8.31.2, Sheet 6 |
| Access Monitoring | [Manual count from A.8.31.2, Sheet 7] | [Total environments] | [Calculated] | [Auto from %] | A.8.31.2, Sheet 7 |

### Compliance % Formula

**Column D (Compliance %):**
```excel
= (B[row] / C[row]) * 100
```

**Special Cases:**

- **Production Access Restrictions**: =IF(B[row]=0,100%,0%)
  - 0 developers = 100% compliant
  - >0 developers = 0% compliant (MAJOR VIOLATION)
  
- **Break-Glass Controls**: Based on frequency assessment
  - "Rare" = 100%
  - "Occasional" = 50%
  - "Frequent" = 0%

### Status Auto-Assignment

**Column E (Status):**
```excel
= IF(D[row] >= 90%, "✅ Compliant", 
     IF(D[row] >= 70%, "⚠️ Partial", 
        "❌ Non-Compliant"))
```

### Conditional Formatting

**Compliance % column:**

- ≥90%: Green fill (C6EFCE)
- 70-89%: Yellow fill (FFEB9C)
- <70%: Red fill (FFC7CE)

---

## Sheet 4: Compliance_Scoring

### Purpose
Calculate weighted overall compliance score from domain scores.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:E1):** "COMPLIANCE SCORING"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:E2):** "Weighted compliance score calculation - Critical domains weighted higher"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Overall Compliance Summary (Rows 4-8)

| Row | Metric | Value | Display Style |
|-----|--------|-------|---------------|
| 4 | **Overall Compliance Score** | [Weighted average formula] | Extra large, bold, conditional color |
| 5 | **Compliance Grade** | [✅/⚠️/❌ based on score] | Large, bold, conditional color |
| 6 | **Assessment Quarter** | [From Sheet 1, Row 8] | Bold |
| 7 | **Assessment Date** | [From Sheet 1, Row 9] | Bold |
| 8 | **Critical Gaps** | [From Sheet 2, Row 5] | Red if >0, green if 0 |

**Overall Compliance Score Formula (Row 4):**
```excel
= SUMPRODUCT(D12:D[last_row], C12:C[last_row])
```
Where:

- Column C = Domain Weight (%)
- Column D = Domain Compliance Score (%)

**Compliance Grade Formula (Row 5):**
```excel
= IF(B4 >= 95%, "✅ Excellent",
     IF(B4 >= 90%, "✅ Compliant",
        IF(B4 >= 70%, "⚠️ Partial",
           "❌ Non-Compliant")))
```

### Domain Weights & Scores (Rows 10+)

**Column Headers (Row 10):**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Domain | 30 | Text |
| B | Domain Compliance Score (%) | 25 | Number (from Sheet 3) |
| C | Domain Weight (%) | 20 | Number (user adjustable) |
| D | Weighted Score | 18 | Formula (B × C) |
| E | Notes | 30 | Text |

**Row 10 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Default Domain Weights (Rows 11+)

| Domain | Score (%) | Weight (%) | Weighted Score | Notes |
|--------|-----------|------------|----------------|-------|
| Network Separation | [From Sheet 3] | 15% | [Auto-calc] | Foundational control |
| Infrastructure Separation | [From Sheet 3] | 15% | [Auto-calc] | Foundational control |
| **Data Separation** | [From Sheet 3] | **20%** | [Auto-calc] | **CRITICAL - no prod data in dev/test** |
| Credential Separation | [From Sheet 3] | 15% | [Auto-calc] | Security risk |
| Configuration Consistency | [From Sheet 3] | 5% | [Auto-calc] | Operational |
| Access Matrix Compliance | [From Sheet 3] | 5% | [Auto-calc] | User permissions |
| **Production Access Restrictions** | [From Sheet 3] | **25%** | [Auto-calc] | **CRITICAL - zero developer access** |
| MFA Enforcement | [From Sheet 3] | 5% | [Auto-calc] | Security hygiene |
| Break-Glass Controls | [From Sheet 3] | 3% | [Auto-calc] | Emergency access |
| Access Monitoring | [From Sheet 3] | 2% | [Auto-calc] | Detective control |
| **TOTAL** | | **100%** | [Sum] | **Must equal 100%** |

**Weight Validation (Row after last domain):**
```excel
= IF(SUM(C11:C[last_row]) = 100%, "✅ Weights Valid", "❌ ERROR: Weights must equal 100%")
```

### Weighted Score Calculation

**Column D (Weighted Score):**
```excel
= B[row] × C[row]
```

**Example:**
```
Data Separation: 100% × 20% = 20.0
Production Access: 100% × 25% = 25.0
MFA Enforcement: 80% × 5% = 4.0
```

### Conditional Formatting

**Overall Compliance Score (Row 4):**

- ≥95%: Dark green fill (00B050), white text
- 90-94%: Green fill (C6EFCE), dark text
- 70-89%: Yellow fill (FFEB9C), dark text
- <70%: Red fill (FFC7CE), dark text

**Domain Scores (Column B):**

- Same as overall score

---

## Sheet 5: Executive_Summary

### Purpose
1-page executive dashboard for CISO presentation.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:F1):** "EXECUTIVE SUMMARY - ENVIRONMENT SEPARATION COMPLIANCE"
  - Style: Dark blue (003366), white text, bold, centered, 45px height
  
- **Row 2 (Merged A2:F2):** "Quarter: [Q1 2026] | Assessment Date: [Date]"
  - Style: Medium blue (4472C4), white text, centered, 30px height

### Key Metrics Dashboard (Rows 4-15)

**Large Visual Metrics:**

| Row Range | Metric | Value Source | Display Style |
|-----------|--------|--------------|---------------|
| 4-6 | **OVERALL COMPLIANCE** | Sheet 4, Row 4 | Extra large (36pt), conditional color |
| 7-8 | Compliance Grade | Sheet 4, Row 5 | Large (24pt), conditional color |
| 9-10 | **Total Gaps** | Sheet 2, Row 4 | Large (20pt) |
| 11-12 | Critical Gaps | Sheet 2, Row 5 | Large (20pt), red if >0 |
| 13-15 | **Developer Prod Access** | Sheet 3 (Production Access row) | Extra large (28pt), red if >0, green if 0 |

**Layout (visual representation):**
```
┌─────────────────────────────────────────────┐
│ OVERALL COMPLIANCE: 95.5%                   │ ← Extra large, green
│ Grade: ✅ Compliant                        │ ← Large, green
├─────────────────────────────────────────────┤
│ Total Gaps: 8  |  Critical: 2              │ ← Large
├─────────────────────────────────────────────┤
│ DEVELOPER PRODUCTION ACCESS: 0              │ ← Extra large, green (target: 0)
│ Status: ✅ Compliant (Zero Access)         │
└─────────────────────────────────────────────┘
```

### Compliance by Domain (Rows 17-30)

**Table Format:**

| Domain | Score | Status | Trend (vs Last Quarter) |
|--------|-------|--------|------------------------|
| Data Separation | [Sheet 3] | [✅/⚠️/❌] | [↑/→/↓ or N/A if first assessment] |
| Production Access | [Sheet 3] | [✅/⚠️/❌] | [↑/→/↓] |
| Network Separation | [Sheet 3] | [✅/⚠️/❌] | [↑/→/↓] |
| Infrastructure Separation | [Sheet 3] | [✅/⚠️/❌] | [↑/→/↓] |
| Credential Separation | [Sheet 3] | [✅/⚠️/❌] | [↑/→/↓] |
| MFA Enforcement | [Sheet 3] | [✅/⚠️/❌] | [↑/→/↓] |
| Access Monitoring | [Sheet 3] | [✅/⚠️/❌] | [↑/→/↓] |

**Trend Symbols:**

- ↑ Improving (score increased vs last quarter)
- → Stable (±2% change)
- ↓ Declining (score decreased)
- N/A (first assessment, no comparison)

### Executive Commentary (Rows 32-40)

**Row 32:** "Executive Summary" (bold, underlined)

**Rows 33-40:** User input text area (yellow fill)

```
[1-2 paragraphs summarizing:

- Overall compliance status
- Key achievements this quarter
- Critical concerns
- Business impact

Example:
"Environment separation compliance improved to 95.5% this quarter, 
up from 88% in Q4 2025. We successfully eliminated all developer 
production access (zero developers with production access), meeting 
our critical compliance requirement. Two critical gaps remain related 
to network isolation, targeted for closure by end of February 2026."]
```

### Top 3 Achievements (Rows 42-47)

**Row 42:** "Top 3 Achievements" (bold, green background)

**Rows 43-47:** User input (yellow fill)

```
1. [Achievement 1]
2. [Achievement 2]
3. [Achievement 3]

Example:
1. Eliminated developer production access (0 developers)
2. Achieved 100% data separation compliance
3. Implemented automated access monitoring
```

### Top 3 Concerns (Rows 49-54)

**Row 49:** "Top 3 Concerns" (bold, red background)

**Rows 50-54:** User input (yellow fill)

```
1. [Concern 1]
2. [Concern 2]
3. [Concern 3]

Example:
1. 2 critical network isolation gaps (developer → production)
2. MFA enforcement at 80% (target: 100%)
3. Break-glass usage frequency increasing
```

### Next Steps (Rows 56-61)

**Row 56:** "Next Steps & Action Items" (bold, blue background)

**Rows 57-61:** User input (yellow fill)

```
1. [Action item 1 with date]
2. [Action item 2 with date]
3. [Action item 3 with date]

Example:
1. Close 2 critical network gaps by February 28, 2026
2. Enforce mandatory MFA for all production users by March 15, 2026
3. Implement read-only production troubleshooting by April 30, 2026
```

### Approval Section (Rows 63-68)

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Information Security Manager | [Name] | [Date] | _____________ |
| CISO | [Name] | [Date] | _____________ |

---

## Sheet 6: Trend_Analysis

### Purpose
Track compliance trends over multiple quarters (requires historical data).

**NOTE:** Skip this sheet if this is the first assessment (no historical data available).

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:G1):** "COMPLIANCE TREND ANALYSIS"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:G2):** "Historical compliance tracking - minimum 2 quarters required for trend analysis"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Historical Compliance Scores (Rows 4+)

**Column Headers (Row 4):**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Quarter | 15 | Text |
| B | Overall Compliance (%) | 20 | Number |
| C | Change from Previous (%) | 20 | Number (formula) |
| D | Total Gaps | 15 | Number |
| E | Gaps Closed | 15 | Number |
| F | Gaps Opened | 15 | Number |
| G | Net Gap Change | 15 | Number (formula) |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Sample Historical Data (Rows 5-9)

| Quarter | Overall % | Change | Total Gaps | Closed | Opened | Net Change |
|---------|-----------|--------|------------|--------|--------|------------|
| Q2 2025 | 75% | - | 18 | - | - | - |
| Q3 2025 | 82% | +7% | 15 | 5 | 2 | -3 |
| Q4 2025 | 88% | +6% | 12 | 4 | 1 | -3 |
| Q1 2026 | 95.5% | +7.5% | 8 | 5 | 1 | -4 |

### Change Formula

**Column C (Change from Previous):**
```excel
= B[row] - B[row-1]
```

**Column G (Net Gap Change):**
```excel
= E[row] - F[row]
```

- Negative = improvement (more closed than opened)
- Positive = degradation (more opened than closed)

### Trend Analysis Summary (Rows 11-16)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Trend Direction | [Formula] | ✅ Improving / ⚠️ Stable / ❌ Declining |
| Average Quarterly Change | [Formula] | [+X.X%] |
| Average Gap Closure Rate | [Formula] | [X gaps per quarter] |
| Quarters to Target (90%) | [Formula] | [X quarters] or [✅ Target Achieved] |

**Trend Direction Formula:**
```excel
= IF(AND(B[latest] > B[previous], B[previous] > B[2nd_previous]), 
     "✅ Improving",
     IF(AND(B[latest] = B[previous], B[previous] = B[2nd_previous]), 
        "⚠️ Stable",
        "❌ Declining"))
```

**Average Quarterly Change:**
```excel
= AVERAGE(C5:C[last_row])
```

### Trend Visualization

**Chart (embedded in sheet):**

- Type: Line chart
- X-axis: Quarter
- Y-axis: Overall Compliance (%)
- Target line: 90% (horizontal reference line)
- Data series: Overall Compliance (%)

**Chart Title:** "Environment Separation Compliance Trend"

---

## Sheet 7: Remediation_Action_Plan

### Purpose
Risk-prioritized remediation plan for all open gaps.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:K1):** "REMEDIATION ACTION PLAN"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:K2):** "Risk-prioritized action plan - Critical gaps must be closed within 30 days"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Prioritization Summary (Rows 4-9)

| Row | Priority | Count | Target Timeline |
|-----|----------|-------|-----------------|
| 4 | 🔴 P0 - Critical | [Count from Sheet 2] | ≤30 days |
| 5 | 🟡 P1 - High | [Count from Sheet 2] | ≤90 days |
| 6 | 🟢 P2 - Medium | [Count from Sheet 2] | ≤180 days |
| 7 | ⚪ P3 - Low | [Count from Sheet 2] | As resources allow |
| 8 | **Total Open Gaps** | [Sum] | |

### Column Headers (Row 11)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Priority | 12 | Dropdown |
| B | Gap ID | 15 | Text (from Sheet 2) |
| C | Gap Description | 40 | Text (from Sheet 2) |
| D | Risk Severity | 15 | Dropdown (from Sheet 2) |
| E | Owner | 20 | Text |
| F | Target Date | 15 | Date |
| G | Remediation Approach | 45 | Text |
| H | Status | 15 | Dropdown |
| I | % Complete | 12 | Number (%) |
| J | Last Updated | 15 | Date |
| K | Notes | 30 | Text |

**Row 11 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column A: Priority**

- 🔴 P0 - Critical (≤30 days)
- 🟡 P1 - High (≤90 days)
- 🟢 P2 - Medium (≤180 days)
- ⚪ P3 - Low (as resources allow)

**Column D: Risk Severity** (from Sheet 2)

- 🔴 Critical
- 🟡 High
- 🟢 Medium
- ⚪ Low

**Column H: Status** (from Sheet 2)

- Open
- Assigned
- In Progress
- Pending Verification
- Resolved
- Risk Accepted

### Sample Data (Rows 12-16)

| Priority | Gap ID | Description | Severity | Owner | Target | Remediation Approach | Status | % | Updated | Notes |
|----------|--------|-------------|----------|-------|--------|---------------------|--------|---|---------|-------|
| 🔴 P0 | ACCESS-GAP-001 | Developer has prod access | 🔴 Critical | IAM Admin | 2026-01-25 | Revoke access, audit logs | In Progress | 90% | 2026-01-20 | Nearly complete |
| 🔴 P0 | ARCH-GAP-001 | Dev → prod network access | 🔴 Critical | Network Admin | 2026-01-30 | Update firewall rules | Assigned | 0% | 2026-01-18 | Scheduled for Jan 28 |
| 🟡 P1 | ARCH-GAP-002 | Prod creds not in PAM | 🟡 High | Security Eng | 2026-02-28 | Migrate to CyberArk | Assigned | 0% | 2026-01-18 | Planning phase |

### Auto-Prioritization Rules

**Priority Assignment Logic:**
1. Gap Severity = Critical → Priority = P0 (≤30 days)
2. Gap Severity = High → Priority = P1 (≤90 days)
3. Gap Severity = Medium → Priority = P2 (≤180 days)
4. Gap Severity = Low → Priority = P3 (as resources allow)

**Can be manually overridden if needed (e.g., business priority)**

### Target Date Calculation

**Suggested Target Date (informational, user can override):**
```excel
= TODAY() + [Days based on priority]

P0: TODAY() + 30
P1: TODAY() + 90
P2: TODAY() + 180
P3: No auto-calculation
```

### Conditional Formatting

**Row highlighting by priority:**

- P0 (Critical): Red fill (FFC7CE)
- P1 (High): Orange fill (FFD966)
- P2 (Medium): Yellow fill (FFEB9C)
- P3 (Low): Light gray fill (F2F2F2)

**Target Date column:**

- Past due (date < TODAY()): Red text, bold
- Due within 7 days: Orange text, bold
- Future: Normal

**% Complete column:**

- 0-33%: Red fill
- 34-66%: Yellow fill
- 67-99%: Light green fill
- 100%: Dark green fill

---

## Sheet 6: Evidence_Summary (includes Audit Readiness)

### Purpose
Consolidated evidence package from both source assessments and audit readiness verification.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:D1):** "AUDIT READINESS CHECKLIST"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:D2):** "Evidence package verification - Must achieve ≥95% for audit readiness"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Audit Readiness Score (Rows 4-6)

| Row | Metric | Formula | Display |
|-----|--------|---------|---------|
| 4 | **Total Checklist Items** | =COUNTA(A9:A100)-1 | Bold |
| 5 | **Items Complete** | =COUNTIF(C9:C100,"✅ Yes") | Bold |
| 6 | **Audit Readiness Score** | =(B5/B4)*100% | Extra large, conditional color |
| 7 | **Audit Readiness Status** | [Formula based on score] | Large, conditional color |

**Audit Readiness Status Formula (Row 7):**
```excel
= IF(B6 >= 95%, "✅ Audit Ready",
     IF(B6 >= 85%, "⚠️ Minor Gaps",
        "❌ Not Ready"))
```

**Conditional Formatting (Row 6):**

- ≥95%: Green fill (C6EFCE), bold
- 85-94%: Yellow fill (FFEB9C), bold
- <85%: Red fill (FFC7CE), bold

### Column Headers (Row 8)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Checklist Item | 50 | Text |
| B | Required Evidence | 40 | Text |
| C | Complete? | 15 | Dropdown |
| D | Evidence Location | 35 | Text |

**Row 8 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column C: Complete?**

- ✅ Yes
- ❌ No
- ⚠️ Partial
- N/A

### Checklist Categories

#### Assessment Completeness (Rows 9-15)

| Item | Required Evidence | Complete? | Location |
|------|------------------|-----------|----------|
| ISMS-IMP-A.8.31.1 completed | Completed workbook with all sheets | [Dropdown] | [Path/URL] |
| ISMS-IMP-A.8.31.1 approved | Approval signatures present | [Dropdown] | [Path/URL] |
| ISMS-IMP-A.8.31.2 completed | Completed workbook with all sheets | [Dropdown] | [Path/URL] |
| ISMS-IMP-A.8.31.2 approved | Approval signatures present | [Dropdown] | [Path/URL] |
| ISMS-IMP-A.8.31.3 completed | This dashboard complete | [Dropdown] | [Path/URL] |
| No missing data | All cells filled, no TBD | [Dropdown] | N/A |
| No broken formulas | All formulas calculating correctly | [Dropdown] | N/A |

#### Evidence Package (Rows 17-28)

| Item | Required Evidence | Complete? | Location |
|------|------------------|-----------|----------|
| Evidence register complete | All gaps have evidence documented | [Dropdown] | A.8.31.1 Sheet 9, A.8.31.2 Sheet 9 |
| Network diagrams current | Within 90 days | [Dropdown] | [Path/URL] |
| Firewall rule exports | Current quarter | [Dropdown] | [Path/URL] |
| Cloud configuration exports | AWS/Azure/GCP configs | [Dropdown] | [Path/URL] |
| IAM policy exports | Production access policies | [Dropdown] | [Path/URL] |
| Access logs available | Minimum 90 days retention | [Dropdown] | [Path/URL] |
| Break-glass logs | Last 90 days usage | [Dropdown] | [Path/URL] |
| Penetration test reports | Within 12 months | [Dropdown] | [Path/URL] |
| Data anonymization docs | Procedures if used | [Dropdown] | [Path/URL] |
| MFA configuration docs | Policy + enrollment status | [Dropdown] | [Path/URL] |

#### Approvals (Rows 30-36)

| Item | Required Evidence | Complete? | Location |
|------|------------------|-----------|----------|
| A.8.31.1 approved by Cloud Architect | Signature present | [Dropdown] | A.8.31.1 approval section |
| A.8.31.1 approved by CISO | Signature present | [Dropdown] | A.8.31.1 approval section |
| A.8.31.2 approved by IAM Admin | Signature present | [Dropdown] | A.8.31.2 approval section |
| A.8.31.2 approved by CISO | Signature present | [Dropdown] | A.8.31.2 approval section |
| A.8.31.3 approved by Info Sec Manager | Signature present | [Dropdown] | This dashboard, Sheet 5 |
| A.8.31.3 approved by CISO | Signature present | [Dropdown] | This dashboard, Sheet 5 |

#### Remediation Tracking (Rows 38-43)

| Item | Required Evidence | Complete? | Location |
|------|------------------|-----------|----------|
| All gaps have owners | Owner assigned for each gap | [Dropdown] | Sheet 2, Sheet 7 |
| Critical gaps have dates ≤30 days | Target dates appropriate | [Dropdown] | Sheet 7 |
| Remediation approach documented | Specific actions for each gap | [Dropdown] | Sheet 7 |
| Risk acceptance documented | If gaps accepted, approval present | [Dropdown] | [Path/URL] |

#### Historical Data (Rows 45-47)

| Item | Required Evidence | Complete? | Location |
|------|------------------|-----------|----------|
| Previous quarter dashboard archived | Q4 2025 dashboard | [Dropdown] | [Path/URL] |
| Trend analysis complete | If 2+ quarters data available | [Dropdown] | Sheet 6 |

---

## Sheet 8: Approval_Sign_Off

### Purpose
Multi-level approval workflow and formal executive sign-off for the compliance dashboard.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:F1):** "APPROVAL & SIGN-OFF"
  - Style: Dark blue (003366), white text, bold, centered, 35px height

- **Row 2 (Merged A2:F2):** "Executive approval workflow - Dashboard requires CISO sign-off before distribution"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Dashboard Summary (Rows 4-12)

| Row | Attribute | Value |
|-----|-----------|-------|
| 4 | Dashboard ID: | ISMS-IMP-A.8.31.3 |
| 5 | Dashboard Name: | Environment Separation Compliance Dashboard |
| 6 | Assessment Quarter: | [From Sheet 1] |
| 7 | Dashboard Date: | [From Sheet 1] |
| 8 | Completed By: | [From Sheet 1] |
| 9 | Overall Compliance Score: | [From Sheet 4 - Compliance_Scoring] |
| 10 | Compliance Grade: | [From Sheet 4] |
| 11 | Total Gaps: | [From Sheet 2 - Consolidated_Gap_Analysis] |
| 12 | Critical Gaps: | [From Sheet 2] |

### Source Assessment Verification (Rows 14-18)

| Source Assessment | Completed? | Approved? | Approval Date |
|-------------------|------------|-----------|---------------|
| ISMS-IMP-A.8.31.1 (Environment Architecture) | [✅/❌] | [✅/❌] | [Date] |
| ISMS-IMP-A.8.31.2 (Environment Access Control) | [✅/❌] | [✅/❌] | [Date] |

### Critical Compliance Verification (Rows 20-24)

**Row 20:** "CRITICAL COMPLIANCE VERIFICATION" (bold, red background)

| Check | Target | Actual | Status |
|-------|--------|--------|--------|
| Developer Production Access Count | 0 | [From A.8.31.2] | [✅ if 0, 🔴 MAJOR VIOLATION if >0] |
| Data Separation Compliance | 100% | [From A.8.31.1] | [✅/⚠️/❌] |
| Overall Compliance Score | ≥90% | [From Sheet 4] | [✅/⚠️/❌] |

### Approval Workflow (Rows 26-36)

**Level 1: Information Security Team Review (Rows 28-30)**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Reviewer Role | 30 | Text |
| B | Reviewer Name | 25 | Text (user input) |
| C | Review Date | 15 | Date (user input) |
| D | Decision | 15 | Dropdown |
| E | Comments | 50 | Text (user input) |
| F | Signature | 20 | Text (user input) |

**Dropdown for Decision:**
- Approved
- Approved with Comments
- Request Changes
- Rejected

**Level 1 Reviewers:**
| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| Information Security Manager | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

**Level 2: Executive Approval (Rows 32-36)**

| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| CISO | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |
| CTO (optional) | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

### Approval Status Summary (Rows 38-41)

| Metric | Value | Status |
|--------|-------|--------|
| Level 1 (Info Sec) Status | [Auto-calculated] | [✅/⚠️/❌] |
| Level 2 (Executive) Status | [Auto-calculated] | [✅/⚠️/❌] |
| **Overall Approval Status** | [Auto-calculated] | [✅ Approved / ⚠️ Pending / ❌ Not Approved] |

### Distribution List (Rows 43-50)

**Row 43:** "Approved Dashboard Distribution" (bold, underlined)

| Recipient | Role | Distribution Date | Method |
|-----------|------|-------------------|--------|
| CISO | Executive Sponsor | [Date] | Email + SharePoint |
| CTO | Executive Management | [Date] | Email + SharePoint |
| IT Operations Manager | Remediation Owner | [Date] | Email + SharePoint |
| Cloud Architect | Technical Lead | [Date] | Email + SharePoint |
| IAM Administrator | Access Control Lead | [Date] | Email + SharePoint |
| Compliance Officer | Audit Coordination | [Date] | Email + SharePoint |

### Next Dashboard Schedule (Rows 52-55)

| Attribute | Value |
|-----------|-------|
| Next Scheduled Dashboard: | [User Input: Q2 2026] |
| Dashboard Frequency: | Quarterly |
| Source Assessments Due: | [2 weeks before dashboard date] |
| Executive Presentation: | [1 week after dashboard completion] |

---

## Compliance Scoring Methodology

### Scoring Approach

**Domain-Level Scoring:**
```
Domain Compliance % = (Compliant Items / Total Items) × 100
```

**Overall Compliance Score:**
```
Overall Score = Σ (Domain Score × Domain Weight)
```

### Default Weights Rationale

| Domain | Weight | Rationale |
|--------|--------|-----------|
| Data Separation | 20% | **CRITICAL** - Production data in dev/test = major risk |
| Production Access | 25% | **CRITICAL** - Developer production access = major violation |
| Network Separation | 15% | Foundational infrastructure control |
| Infrastructure Separation | 15% | Foundational infrastructure control |
| Credential Separation | 15% | Security risk (credentials compromise) |
| MFA Enforcement | 5% | Security hygiene (important but not critical) |
| Configuration Consistency | 5% | Operational efficiency |
| Access Matrix Compliance | 5% | User permission management |
| Break-Glass Controls | 3% | Emergency access (infrequent use) |
| Access Monitoring | 2% | Detective control (important but reactive) |

**Total:** 100%

### Compliance Grade Assignment

| Score | Grade | Action Required |
|-------|-------|----------------|
| 95-100% | ✅ Excellent | Minor refinements only |
| 90-94% | ✅ Compliant | Acceptable, some gaps remain |
| 70-89% | ⚠️ Partial | Active remediation needed |
| <70% | ❌ Non-Compliant | Immediate executive escalation |

---

## Cell Styling Reference

### Color Codes

| Style | Background | Font Color | Usage |
|-------|------------|------------|-------|
| Header (dark blue) | #003366 | White (#FFFFFF) | Sheet titles |
| Header (medium blue) | #4472C4 | White (#FFFFFF) | Column headers |
| Subheader (light blue) | #B4C7E7 | Dark (#000000) | Instructions |
| User Input | #FFEB9C (yellow) | Dark (#000000) | User-editable cells |
| Excellent (95-100%) | #00B050 (dark green) | White (#FFFFFF) | Excellent compliance |
| Compliant (90-94%) | #C6EFCE (green) | Dark (#000000) | Compliant status |
| Partial (70-89%) | #FFEB9C (yellow) | Dark (#000000) | Partial compliance |
| Non-Compliant (<70%) | #FFC7CE (red) | Dark (#000000) | Non-compliant status |
| Critical Priority (P0) | #FFC7CE (red) | Dark (#000000) | Critical gaps |
| High Priority (P1) | #FFD966 (orange) | Dark (#000000) | High priority gaps |
| Medium Priority (P2) | #FFEB9C (yellow) | Dark (#000000) | Medium priority |
| Low Priority (P3) | #F2F2F2 (light gray) | Dark (#000000) | Low priority |

### Font Styles

| Element | Font | Size | Weight | Alignment |
|---------|------|------|--------|-----------|
| Sheet Title | Calibri | 18pt | Bold | Center |
| Subtitle | Calibri | 12pt | Regular | Center |
| Overall Compliance Score | Calibri | 36pt | Bold | Center |
| Compliance Grade | Calibri | 24pt | Bold | Center |
| Critical Metrics | Calibri | 28pt | Bold | Center |
| Column Headers | Calibri | 11pt | Bold | Center |
| Data Cells | Calibri | 10pt | Regular | Left |
| Executive Commentary | Calibri | 11pt | Regular | Left (wrapped) |

---

## Integration Points

### Input from Other Assessments

**From ISMS-IMP-A.8.31.1 (Environment Architecture):**

- Sheet 8: Gap_Analysis → All architecture gaps
- Sheets 2-7: Compliance status → Domain scores

**From ISMS-IMP-A.8.31.2 (Access Control):**

- Sheet 8: Gap_Analysis → All access control gaps
- Sheet 4: Production access verification → Developer count
- Sheets 2-7: Compliance status → Domain scores

### Output to Stakeholders

**To CISO / Executive Management:**

- Sheet 5: Executive_Summary (1-page dashboard)
- Overall compliance score and grade
- Top gaps and remediation plan

**To IT Operations:**

- Sheet 7: Remediation_Action_Plan
- Prioritized gaps with owners and dates

**To Auditors:**

- All sheets (complete assessment package)
- Sheet 6: Evidence_Summary (includes audit readiness checklist)
- Evidence register references

**To Risk Management:**

- Sheet 2: Consolidated_Gap_Analysis
- Risk severity and remediation status

### Output to Python Scripts

**generate_a831_3_dashboard.py** generates this workbook:

- Creates all 8 sheets with structure
- Auto-calculates compliance scores
- Applies conditional formatting
- Generates embedded charts (trend analysis)
- Exports to `.xlsx` format

---

## Workbook Metadata

**File Name:** `A831-3-Compliance-Dashboard-[Quarter]-YYYY-MM-DD.xlsx`

Example: `A831-3-Compliance-Dashboard-Q1-2026-01-25.xlsx`

**Properties:**

- Title: ISMS-IMP-A.8.31.3 - Environment Separation Compliance Dashboard
- Subject: ISO/IEC 27001:2022 Control A.8.31 - Executive Summary
- Author: [Organization] ISMS Team
- Comments: Consolidated dashboard from A.8.31.1 (Architecture) + A.8.31.2 (Access Control)
- Keywords: ISO27001, A.8.31, compliance dashboard, executive summary, trend analysis

**Protection:**

- Sheet structure protected
- User input cells unlocked (yellow cells)
- Formula cells locked (auto-calculations)
- Header rows locked

---

**END OF SPECIFICATION**

---

*"A hash function is any function that can be used to map data of arbitrary size to fixed-size values."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->

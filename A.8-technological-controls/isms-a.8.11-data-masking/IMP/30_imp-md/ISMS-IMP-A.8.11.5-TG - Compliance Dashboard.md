**ISMS-IMP-A.8.11.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Master Compliance Dashboard & Consolidation |
| **Related Policy** | ISMS-POL-A.8.11 (All Sections) |
| **Purpose** | Consolidate all assessment domains into executive-level compliance dashboard |
| **Target Audience** | CISO, DPO, Security Managers, Compliance Officers |
| **Review Cycle** | Monthly or After Major Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.11.5-TG  
**Assessment Area:** Master Compliance Dashboard & Consolidation  
**Related Policies:** All ISMS-POL-A.8.11-S2.x policies  
**Purpose:** Consolidate all assessment domains into executive-level compliance dashboard

**Scope:** This MASTER workbook provides:

- Executive summary (one-page CISO/Board view)
- Consolidated data from Domains 1-4
- Gap analysis aggregation
- Risk register (masking-related risks)
- Remediation roadmap (prioritized action plan)
- KPI dashboard (20+ key metrics)
- Evidence master index
- CISO/DPO approval sign-off

**Assessment Philosophy:**

- **Executive-focused:** High-level view for CISO, DPO, Board
- **Data-driven:** Pull actual data from assessment workbooks
- **Action-oriented:** Clear gaps, risks, and remediation priorities
- **Evidence-based:** Link to comprehensive evidence trail
- **Audit-ready:** Complete compliance picture in one workbook

**CRITICAL FEATURE:** This workbook uses **external workbook formulas** to pull data from:

- ISMS-IMP-A.8.11.1 (Data Inventory)
- ISMS-IMP-A.8.11.2 (Masking Techniques)
- ISMS-IMP-A.8.11.3 (Environment Coverage)
- ISMS-IMP-A.8.11.4 (Testing & Validation)

---

## Workbook Structure

### Sheet Overview (12 Sheets)

1. **Instructions_Legend** - Dashboard usage guidance
2. **Executive_Summary** - One-page CISO/Board overview
3. **Domain_1_Summary** - Data Inventory rollup
4. **Domain_2_Summary** - Masking Techniques rollup
5. **Domain_3_Summary** - Environment Coverage rollup
6. **Domain_4_Summary** - Testing & Validation rollup
7. **Consolidated_Gap_Analysis** - All gaps from all domains
8. **Risk_Register** - Masking-related risks
9. **Remediation_Roadmap** - Prioritized action plan
10. **Evidence_Master_Index** - All evidence from all domains
11. **KPI_Dashboard** - 20+ key metrics with targets
12. **CISO_DPO_Approval** - Executive sign-off

---

## Cell Styling Reference

### Header Styles

- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Centered
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (medium blue), Centered
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (light gray), Centered

### Input Cell Styles

- **Fill:** FFFFCC (light yellow) - User input required
- **Alignment:** Left for text, center for dropdowns, wrapped
- **Border:** Thin black on all sides

### Status Color Coding

- **Green (Compliant):** C6EFCE
- **Yellow (Partial):** FFEB9C
- **Red (Non-Compliant):** FFC7CE
- **Blue (Planned):** B4C7E7

### KPI Traffic Lights

- **Green:** ≥90% of target
- **Yellow:** 70-89% of target
- **Red:** <70% of target

---

## Sheet 1: Instructions_Legend

### Header Section
**Title:** "ISMS Control A.8.11.5 - Master Compliance Dashboard"  
**Subtitle:** "ISO/IEC 27001:2022 - Data Masking Policy Compliance Overview"  
**Styling:** Dark blue header (003366), white text, centered, 40px height

### Document Information Block
```
Document ID:           ISMS-IMP-A.8.11.5
Assessment Area:       Master Compliance Dashboard
Related Policies:      All ISMS-POL-A.8.11-S2.x
Version:               1.0
Dashboard Date:        [USER INPUT - yellow cell]
Prepared By:           [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

### How to Use This Dashboard (12 instructions)
1. This is the MASTER workbook consolidating all Domain 1-4 assessments
2. Ensure all 4 assessment workbooks are completed first:

   - ISMS-IMP-A.8.11.1 (Data Inventory & Classification)
   - ISMS-IMP-A.8.11.2 (Masking Technique Selection)
   - ISMS-IMP-A.8.11.3 (Environment Coverage Assessment)
   - ISMS-IMP-A.8.11.4 (Testing & Validation Framework)

3. Place all 4 workbooks in the SAME directory as this dashboard
4. Review Executive Summary sheet for one-page CISO view
5. Check Domain Summary sheets for detailed rollups
6. Review Consolidated Gap Analysis for all gaps across domains
7. Examine Risk Register for masking-related risks
8. Use Remediation Roadmap to prioritize actions
9. Check KPI Dashboard for compliance metrics (target: ≥90%)
10. Review Evidence Master Index for audit trail
11. Obtain CISO and DPO approval using sign-off sheet
12. Update quarterly or after major changes

### Dashboard Architecture
**This workbook pulls data from 4 source workbooks using external formulas:**

```
[ISMS-IMP-A.8.11.1_...xlsx]Summary_Dashboard!$B$5  → Domain 1 data
[ISMS-IMP-A.8.11.2_...xlsx]Summary_Dashboard!$B$5  → Domain 2 data
[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$5  → Domain 3 data
[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$5  → Domain 4 data
```

**Note:** If source workbooks are not present, formulas will show #REF! errors.

### Color Legend

- 🟩 **Green** = Compliant (≥90% of target)
- 🟨 **Yellow** = Partial compliance (70-89% of target)
- 🟥 **Red** = Non-compliant (<70% of target)
- 🟦 **Blue** = Planned (remediation in progress)

---

## Sheet 2: Executive_Summary

### Header
**Title:** "EXECUTIVE SUMMARY - DATA MASKING COMPLIANCE"  
**Subtitle:** "One-Page Overview for CISO, DPO, and Board"

### Section 1: Overall Compliance Status (Rows 3-8)

**OVERALL COMPLIANCE SCORECARD**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Overall Compliance Score** | [Formula: Weighted avg] | ≥90% | [Conditional Format] |
| Data Inventory Coverage | [Link to Domain 1] | 100% | [Conditional Format] |
| Masking Technique Deployment | [Link to Domain 2] | ≥90% | [Conditional Format] |
| Environment Coverage | [Link to Domain 3] | 100% | [Conditional Format] |
| Testing Pass Rate | [Link to Domain 4] | ≥95% | [Conditional Format] |
| Re-Identification Risk | [Link to Domain 4] | 0% | [Conditional Format] |

### Section 2: Quick Stats (Rows 12-18)

| Domain | Compliant | Partial | Non-Compliant | Coverage % |
|--------|-----------|---------|---------------|------------|
| 1. Data Inventory | [Formula] | [Formula] | [Formula] | [Formula] |
| 2. Masking Techniques | [Formula] | [Formula] | [Formula] | [Formula] |
| 3. Environment Coverage | [Formula] | [Formula] | [Formula] | [Formula] |
| 4. Testing & Validation | [Formula] | [Formula] | [Formula] | [Formula] |
| **TOTAL** | [Formula] | [Formula] | [Formula] | [Formula] |

### Section 3: Critical Gaps (Top 5) (Rows 22-28)

| Priority | Gap Description | Domain | Risk | Owner | Target Date |
|----------|----------------|--------|------|-------|-------------|
| P1 | [Auto-pull from Gap Analysis] | [Auto] | [Auto] | [Auto] | [Auto] |
| P1 | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] |
| P2 | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] |
| P2 | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] |
| P3 | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] |

### Section 4: Risk Summary (Rows 32-38)

| Risk Category | High | Medium | Low | Mitigation Status |
|---------------|------|--------|-----|-------------------|
| Unmasked Environments | [Formula] | [Formula] | [Formula] | [Formula] |
| Re-Identification Risk | [Formula] | [Formula] | [Formula] | [Formula] |
| Schema Drift (Unmasked Fields) | [Formula] | [Formula] | [Formula] | [Formula] |
| Performance Impact | [Formula] | [Formula] | [Formula] | [Formula] |
| **TOTAL RISKS** | [Formula] | [Formula] | [Formula] | [Formula] |

### Section 5: Executive Recommendations (Rows 42-50)

**KEY ACTIONS REQUIRED:**

1. [If Overall Score <90%] → Immediate attention required: [Gap summary]
2. [If Re-ID Risk >0%] → CRITICAL: Re-identification risk detected
3. [If Non-Prod Coverage <100%] → URGENT: Unmasked non-production environments
4. [If High Risks >0] → High-risk gaps require CISO escalation
5. [If Testing Pass Rate <95%] → Testing failures need remediation

**CISO DECISION POINTS:**

- Accept residual risk? [Yes/No - yellow cell]
- Approve remediation roadmap? [Yes/No - yellow cell]
- Additional budget required? [Yes/No - yellow cell]
- Target completion date: [Date - yellow cell]

---

## Sheet 3: Domain_1_Summary

### Header
**Title:** "DOMAIN 1 SUMMARY - DATA INVENTORY & CLASSIFICATION"  
**Source:** ISMS-IMP-A.8.11.1

### Summary Metrics (Rows 3-15)

| Metric | Value | Source Formula |
|--------|-------|----------------|
| Total Systems Inventoried | [Formula] | =[ISMS-IMP-A.8.11.1_...xlsx]Summary_Dashboard!$B$5 |
| Total Sensitive Data Categories | [Formula] | =[ISMS-IMP-A.8.11.1_...xlsx]Summary_Dashboard!$B$6 |
| Total Sensitive Fields Identified | [Formula] | =[ISMS-IMP-A.8.11.1_...xlsx]Summary_Dashboard!$B$7 |
| Data Classification Coverage % | [Formula] | =[ISMS-IMP-A.8.11.1_...xlsx]Summary_Dashboard!$B$8 |
| Data Owners Assigned % | [Formula] | =[ISMS-IMP-A.8.11.1_...xlsx]Summary_Dashboard!$B$9 |
| Regulatory Mapping Complete % | [Formula] | =[ISMS-IMP-A.8.11.1_...xlsx]Summary_Dashboard!$B$10 |
| Masking Priority Matrix Complete | [Formula] | =[ISMS-IMP-A.8.11.1_...xlsx]Summary_Dashboard!$B$11 |
| **Compliance Status** | [Formula] | Based on above metrics |

### Key Findings (Rows 18-25)

- Top 3 data categories by volume: [Auto-pull]
- Highest priority masking requirements: [Auto-pull]
- Unassigned data owners: [Auto-pull]
- Gaps identified: [Auto-pull from Domain 1 Gap Analysis]

---

## Sheet 4: Domain_2_Summary

### Header
**Title:** "DOMAIN 2 SUMMARY - MASKING TECHNIQUE SELECTION"  
**Source:** ISMS-IMP-A.8.11.2

### Summary Metrics (Rows 3-15)

| Metric | Value | Source Formula |
|--------|-------|----------------|
| Approved Masking Techniques Count | [Formula] | =[ISMS-IMP-A.8.11.2_...xlsx]Summary_Dashboard!$B$5 |
| Techniques Deployed Count | [Formula] | =[ISMS-IMP-A.8.11.2_...xlsx]Summary_Dashboard!$B$6 |
| Technique Deployment % | [Formula] | =[ISMS-IMP-A.8.11.2_...xlsx]Summary_Dashboard!$B$7 |
| SDM Coverage % | [Formula] | =[ISMS-IMP-A.8.11.2_...xlsx]Summary_Dashboard!$B$8 |
| DDM Coverage % | [Formula] | =[ISMS-IMP-A.8.11.2_...xlsx]Summary_Dashboard!$B$9 |
| Tokenization Coverage % | [Formula] | =[ISMS-IMP-A.8.11.2_...xlsx]Summary_Dashboard!$B$10 |
| Masking Tools Deployed Count | [Formula] | =[ISMS-IMP-A.8.11.2_...xlsx]Summary_Dashboard!$B$11 |
| Configuration Standards Complete | [Formula] | =[ISMS-IMP-A.8.11.2_...xlsx]Summary_Dashboard!$B$12 |
| **Compliance Status** | [Formula] | Based on above metrics |

### Key Findings (Rows 18-25)

- Most deployed technique: [Auto-pull]
- Technique gaps: [Auto-pull]
- Tool inventory complete: [Auto-pull]
- Configuration issues: [Auto-pull from Domain 2 Gap Analysis]

---

## Sheet 5: Domain_3_Summary

### Header
**Title:** "DOMAIN 3 SUMMARY - ENVIRONMENT COVERAGE ASSESSMENT"  
**Source:** ISMS-IMP-A.8.11.3

### Summary Metrics (Rows 3-20)

| Metric | Value | Source Formula |
|--------|-------|----------------|
| Total Environments Inventoried | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$5 |
| Production Environments | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$6 |
| Non-Production Environments | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$7 |
| Analytics Environments | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$8 |
| Cloud Environments | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$9 |
| Production DDM Coverage % | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$10 |
| **Non-Production Masking Coverage %** | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$11 |
| Analytics Masking Coverage % | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$12 |
| External Sharing Masked % | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$13 |
| Cloud Environment Compliance % | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$14 |
| Data Flow Mapping Complete % | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$15 |
| Exception Count | [Formula] | =[ISMS-IMP-A.8.11.3_...xlsx]Summary_Dashboard!$B$16 |
| **Compliance Status** | [Formula] | Based on above metrics |

### Key Findings (Rows 23-30)

- **CRITICAL:** Non-prod coverage: [Auto-pull - must be 100%]
- Unmasked environments: [Auto-pull]
- Cloud compliance gaps: [Auto-pull]
- Exception justifications: [Auto-pull from Domain 3 Gap Analysis]

---

## Sheet 6: Domain_4_Summary

### Header
**Title:** "DOMAIN 4 SUMMARY - TESTING & VALIDATION FRAMEWORK"  
**Source:** ISMS-IMP-A.8.11.4

### Summary Metrics (Rows 3-20)

| Metric | Value | Source Formula |
|--------|-------|----------------|
| Total Tests Performed | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$5 |
| Tests Passed | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$6 |
| Tests Failed | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$7 |
| Overall Test Pass Rate % | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$8 |
| Pre-Deployment Tests Pass % | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$9 |
| Post-Deployment Validation % | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$10 |
| Masking Coverage % | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$11 |
| **Re-Identification Risk %** | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$12 |
| Data Utility Score % | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$13 |
| Performance Impact % | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$14 |
| Schema Drift Detection Rate % | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$15 |
| Failed Tests Remediated % | [Formula] | =[ISMS-IMP-A.8.11.4_...xlsx]Summary_Dashboard!$B$16 |
| **Compliance Status** | [Formula] | Based on above metrics |

### Key Findings (Rows 23-30)

- **CRITICAL:** Re-ID risk: [Auto-pull - must be 0%]
- Test failures: [Auto-pull]
- Utility issues: [Auto-pull]
- Performance concerns: [Auto-pull from Domain 4 Gap Analysis]

---

## Sheet 7: Consolidated_Gap_Analysis

### Header
**Title:** "CONSOLIDATED GAP ANALYSIS - ALL DOMAINS"

### Column Headers (Row 3)

| Column | Header | Width |
|--------|--------|-------|
| A | Gap ID | 12 |
| B | Domain | 15 |
| C | Gap Category | 20 |
| D | Gap Description | 35 |
| E | Current State | 25 |
| F | Target State | 25 |
| G | Risk Level | 12 |
| H | Business Impact | 30 |
| I | Remediation Action | 35 |
| J | Owner | 20 |
| K | Target Date | 15 |
| L | Status | 15 |
| M | Dependencies | 25 |
| N | Evidence ID | 15 |

### Data Entry Strategy
**This sheet consolidates gaps from all 4 domains:**

**Manual Entry (Rows 5-50):**

- Copy/paste critical gaps from each domain's Gap_Analysis sheet
- Or use formulas to pull top gaps from each domain
- Total capacity: 50 gap entries

**Prioritization Logic:**
1. P1 (Critical): Non-prod unmasked, Re-ID risk >0%, Failed tests
2. P2 (High): Coverage <90%, Utility <95%, Performance >10%
3. P3 (Medium): Documentation gaps, Process improvements
4. P4 (Low): Nice-to-have enhancements

### Summary Metrics (Rows 55-65)

| Gap Category | Total | P1 | P2 | P3 | P4 | % Remediated |
|--------------|-------|----|----|----|----|--------------|
| Data Inventory Gaps | [Count] | [Count] | [Count] | [Count] | [Count] | [Formula] |
| Masking Technique Gaps | [Count] | [Count] | [Count] | [Count] | [Count] | [Formula] |
| Environment Coverage Gaps | [Count] | [Count] | [Count] | [Count] | [Count] | [Formula] |
| Testing & Validation Gaps | [Count] | [Count] | [Count] | [Count] | [Count] | [Formula] |
| **TOTAL GAPS** | [Count] | [Count] | [Count] | [Count] | [Count] | [Formula] |

---

## Sheet 8: Risk_Register

### Header
**Title:** "MASKING RISK REGISTER"

### Column Headers (Row 3)

| Column | Header | Width |
|--------|--------|-------|
| A | Risk ID | 12 |
| B | Risk Category | 20 |
| C | Risk Description | 35 |
| D | Related Domain(s) | 20 |
| E | Likelihood | 12 |
| F | Impact | 12 |
| G | Risk Score | 12 |
| H | Current Controls | 30 |
| I | Control Effectiveness | 18 |
| J | Residual Risk | 15 |
| K | Mitigation Plan | 35 |
| L | Owner | 20 |
| M | Target Date | 15 |
| N | Status | 15 |

### Pre-Populated Risk Categories (Rows 5-25)

| Risk ID | Risk Category | Description |
|---------|---------------|-------------|
| RISK-001 | Unmasked Non-Production | Production data in non-prod without masking |
| RISK-002 | Re-Identification Risk | Masked data can be re-identified |
| RISK-003 | Schema Drift | New columns added without masking |
| RISK-004 | Incomplete Coverage | Not all sensitive fields masked |
| RISK-005 | Failed Validation | Masking tests failing |
| RISK-006 | Performance Impact | Masking degrades performance >10% |
| RISK-007 | Data Utility Loss | Masked data breaks applications |
| RISK-008 | External Data Sharing | Unmasked data shared externally |
| RISK-009 | Cloud Compliance | Cloud environments not masked per policy |
| RISK-010 | Backup Exposure | Unencrypted backups with unmasked data |
| ... | ... | ... |

(20 pre-populated risk entries + 20 blank rows for custom risks)

### Risk Scoring Matrix (Starting Row 50)

| Likelihood × Impact | Negligible (1) | Minor (2) | Moderate (3) | Major (4) | Severe (5) |
|---------------------|----------------|-----------|--------------|-----------|------------|
| **Rare (1)** | 1 (Low) | 2 (Low) | 3 (Low) | 4 (Medium) | 5 (Medium) |
| **Unlikely (2)** | 2 (Low) | 4 (Medium) | 6 (Medium) | 8 (High) | 10 (High) |
| **Possible (3)** | 3 (Low) | 6 (Medium) | 9 (High) | 12 (High) | 15 (Critical) |
| **Likely (4)** | 4 (Medium) | 8 (High) | 12 (High) | 16 (Critical) | 20 (Critical) |
| **Almost Certain (5)** | 5 (Medium) | 10 (High) | 15 (Critical) | 20 (Critical) | 25 (Critical) |

---

## Sheet 9: Remediation_Roadmap

### Header
**Title:** "REMEDIATION ROADMAP - PRIORITIZED ACTION PLAN"

### Column Headers (Row 3)

| Column | Header | Width |
|--------|--------|-------|
| A | Action ID | 12 |
| B | Priority | 10 |
| C | Action Description | 35 |
| D | Related Gap/Risk ID | 15 |
| E | Domain | 15 |
| F | Owner | 20 |
| G | Start Date | 15 |
| H | Target Date | 15 |
| I | Status | 15 |
| J | % Complete | 12 |
| K | Dependencies | 25 |
| L | Budget Required | 15 |
| M | Resources Needed | 25 |
| N | Notes | 30 |

### Data Entry Rows (5-50)

- **50 rows** for remediation actions
- Sorted by priority (P1 → P2 → P3 → P4)
- Yellow-highlighted cells for user input

### Roadmap Summary (Rows 55-65)

| Metric | Value | Target |
|--------|-------|--------|
| Total Actions | [Count] | N/A |
| P1 Actions | [Count] | 0 (all remediated) |
| P2 Actions | [Count] | <5 |
| Completed Actions | [Count] | [Formula: % complete] |
| In Progress Actions | [Count] | |
| Not Started Actions | [Count] | |
| Overdue Actions | [Count] | 0 |
| On-Track Actions | [Count] | |
| Average Days to Complete | [Formula] | ≤90 days |
| Budget Estimate (Total) | [Sum] | |

### Timeline View (Starting Row 70)

**Gantt-style roadmap (optional - manual entry):**

| Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 | Status |
|---------|---------|---------|---------|--------|
| [Action 1] | | | | [Status] |
| | [Action 2] | | | [Status] |
| | | [Action 3] | | [Status] |
| ... | ... | ... | ... | ... |

---

## Sheet 10: Evidence_Master_Index

### Header
**Title:** "EVIDENCE MASTER INDEX - ALL DOMAINS"

### Column Headers (Row 3)

| Column | Header | Width |
|--------|--------|-------|
| A | Evidence ID | 15 |
| B | Domain | 15 |
| C | Evidence Type | 20 |
| D | Description | 35 |
| E | Related Assessment | 25 |
| F | Document Name/Link | 30 |
| G | Date Created | 15 |
| H | Owner | 20 |
| I | Retention Period | 15 |
| J | Location | 25 |

### Data Entry Strategy
**This sheet consolidates evidence from all 4 domains:**

**Option 1: Manual Consolidation**

- Copy evidence from each domain's Evidence_Register
- Total capacity: 100 entries

**Option 2: Formula-Based (Advanced)**

- Use formulas to pull evidence from each domain workbook
- Requires complex INDIRECT() or named range references

### Evidence Summary by Domain (Starting Row 110)

| Domain | Evidence Count | Complete % |
|--------|----------------|------------|
| Domain 1: Data Inventory | [Count] | [Formula] |
| Domain 2: Masking Techniques | [Count] | [Formula] |
| Domain 3: Environment Coverage | [Count] | [Formula] |
| Domain 4: Testing & Validation | [Count] | [Formula] |
| **TOTAL EVIDENCE** | [Count] | [Formula] |

---

## Sheet 11: KPI_Dashboard

### Header
**Title:** "KEY PERFORMANCE INDICATORS - DATA MASKING COMPLIANCE"

### Section 1: Strategic KPIs (Rows 3-15)

| KPI | Current Value | Target | Status | Trend |
|-----|---------------|--------|--------|-------|
| **Overall Compliance Score** | [Formula: Weighted] | ≥90% | [Traffic Light] | [↑/↓/→] |
| Data Inventory Coverage | [From Domain 1] | 100% | [Traffic Light] | [↑/↓/→] |
| Sensitive Fields Classified | [From Domain 1] | 100% | [Traffic Light] | [↑/↓/→] |
| Masking Technique Deployment | [From Domain 2] | ≥90% | [Traffic Light] | [↑/↓/→] |
| Non-Production Masking Coverage | [From Domain 3] | 100% | [Traffic Light] | [↑/↓/→] |
| Production DDM Coverage | [From Domain 3] | ≥90% | [Traffic Light] | [↑/↓/→] |
| Environment Coverage | [From Domain 3] | 100% | [Traffic Light] | [↑/↓/→] |
| Testing Pass Rate | [From Domain 4] | ≥95% | [Traffic Light] | [↑/↓/→] |
| Re-Identification Risk | [From Domain 4] | 0% | [Traffic Light] | [↑/↓/→] |
| Data Utility Score | [From Domain 4] | ≥95% | [Traffic Light] | [↑/↓/→] |
| Performance Impact | [From Domain 4] | <10% | [Traffic Light] | [↑/↓/→] |

### Section 2: Operational KPIs (Rows 18-30)

| KPI | Current Value | Target | Status |
|-----|---------------|--------|--------|
| Exception Count (Total) | [Formula] | ≤5% of envs | [Traffic Light] |
| High-Risk Gaps | [Formula] | 0 | [Traffic Light] |
| Medium-Risk Gaps | [Formula] | <5 | [Traffic Light] |
| Gaps Remediated % | [Formula] | 100% | [Traffic Light] |
| Average Remediation Time (days) | [Formula] | ≤90 | [Traffic Light] |
| Schema Drift Detection Rate | [From Domain 4] | 100% | [Traffic Light] |
| Failed Tests Remediated | [From Domain 4] | 100% | [Traffic Light] |
| Evidence Documentation Rate | [Formula] | 100% | [Traffic Light] |
| External Sharing Masked | [From Domain 3] | 100% | [Traffic Light] |
| Cloud Environment Compliance | [From Domain 3] | 100% | [Traffic Light] |
| Backup Encryption Rate | [From Domain 3] | 100% | [Traffic Light] |
| Data Owner Assignment | [From Domain 1] | 100% | [Traffic Light] |

### Section 3: Compliance Trend (6-Month View) (Rows 35-45)

| Month | Overall Score % | Non-Prod Coverage % | Re-ID Risk % | Test Pass % | Gaps Count |
|-------|----------------|---------------------|--------------|-------------|------------|
| Month -5 | [Manual] | [Manual] | [Manual] | [Manual] | [Manual] |
| Month -4 | [Manual] | [Manual] | [Manual] | [Manual] | [Manual] |
| Month -3 | [Manual] | [Manual] | [Manual] | [Manual] | [Manual] |
| Month -2 | [Manual] | [Manual] | [Manual] | [Manual] | [Manual] |
| Month -1 | [Manual] | [Manual] | [Manual] | [Manual] | [Manual] |
| Current | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |

### Section 4: Compliance Score Calculation (Rows 50-60)

**Weighted Compliance Score Formula:**

| Component | Weight | Score | Weighted Score |
|-----------|--------|-------|----------------|
| Data Inventory & Classification | 20% | [Formula] | [Formula] |
| Masking Technique Deployment | 20% | [Formula] | [Formula] |
| Environment Coverage | 25% | [Formula] | [Formula] |
| Testing & Validation | 25% | [Formula] | [Formula] |
| Evidence & Documentation | 10% | [Formula] | [Formula] |
| **TOTAL COMPLIANCE SCORE** | 100% | | [SUM] |

**Score Interpretation:**

- 90-100% = Excellent (Green)
- 70-89% = Acceptable with gaps (Yellow)
- <70% = Significant gaps requiring immediate action (Red)

---

## Sheet 12: CISO_DPO_Approval

### Header
**Title:** "EXECUTIVE APPROVAL SIGN-OFF"

### Approval Workflow (Rows 3-25)

**1. INFORMATION SECURITY OFFICER (ISO)**

| Field | Value |
|-------|-------|
| Name: | [USER INPUT - yellow] |
| Title: | Information Security Officer |
| Review Date: | [USER INPUT - yellow] |
| Recommendation: | ☐ Approve ☐ Approve with Conditions ☐ Reject |
| Conditions/Comments: | [USER INPUT - yellow] |
| Signature: | _________________________ |

**2. CHIEF INFORMATION SECURITY OFFICER (CISO)**

| Field | Value |
|-------|-------|
| Name: | [USER INPUT - yellow] |
| Title: | Chief Information Security Officer |
| Review Date: | [USER INPUT - yellow] |
| Decision: | ☐ Approve ☐ Approve with Conditions ☐ Reject |
| Conditions/Comments: | [USER INPUT - yellow] |
| Signature: | _________________________ |

**3. DATA PROTECTION OFFICER (DPO)**

| Field | Value |
|-------|-------|
| Name: | [USER INPUT - yellow] |
| Title: | Data Protection Officer |
| Review Date: | [USER INPUT - yellow] |
| Decision: | ☐ Approve ☐ Approve with Conditions ☐ Reject |
| Privacy Impact Assessment: | [USER INPUT - yellow] |
| Conditions/Comments: | [USER INPUT - yellow] |
| Signature: | _________________________ |

**4. CHIEF INFORMATION OFFICER (CIO)**

| Field | Value |
|-------|-------|
| Name: | [USER INPUT - yellow] |
| Title: | Chief Information Officer |
| Review Date: | [USER INPUT - yellow] |
| Decision: | ☐ Approve ☐ Approve with Conditions ☐ Reject |
| Conditions/Comments: | [USER INPUT - yellow] |
| Signature: | _________________________ |

**5. EXECUTIVE MANAGEMENT / BOARD (If Required)**

| Field | Value |
|-------|-------|
| Name: | [USER INPUT - yellow] |
| Title: | [USER INPUT - yellow] |
| Review Date: | [USER INPUT - yellow] |
| Decision: | ☐ Approve ☐ Approve with Conditions ☐ Reject |
| Strategic Alignment: | [USER INPUT - yellow] |
| Budget Approval: | ☐ Approved ☐ Pending ☐ Denied |
| Conditions/Comments: | [USER INPUT - yellow] |
| Signature: | _________________________ |

### Final Approval Status (Row 50)

**OVERALL APPROVAL STATUS:** [Dropdown: Approved / Conditionally Approved / Rejected / Pending]

**Effective Date:** [USER INPUT - yellow]  
**Next Review Date:** [USER INPUT - yellow] (Default: +12 months)

---

## Implementation Notes

### Python Generator Requirements

1. **Sheet Creation:** All 12 sheets with exact names
2. **Styling:** Consistent color scheme (dark blue headers, yellow input cells)
3. **External Formulas:** Formula placeholders for linking to Domain 1-4 workbooks
4. **Conditional Formatting:** Traffic lights for KPI status
5. **Data Validation:** Dropdowns for approval workflow
6. **Freeze Panes:** Freeze at row 4 (summary sheets), row 3 (data sheets)
7. **Pre-Population:**

   - Risk register template (20 pre-defined risks)
   - KPI targets
   - Approval workflow structure
   - Formula templates (user must update with actual filenames)

### Formula Template Strategy

**Since exact filenames are not known at generation time, use placeholder formulas:**

```
="[ISMS-IMP-A.8.11.1_YYYYMMDD.xlsx]Summary_Dashboard!$B$5"
```

**User must update with actual filenames after generation.**

**Alternative:** Provide instructions for users to update formulas via Find & Replace:
1. Generate workbook with placeholder `[A811-1]`, `[A811-2]`, etc.
2. User opens dashboard, does Find & Replace:

   - Find: `[A811-1]`
   - Replace: `[ISMS-IMP-A.8.11.1_Data_Inventory_Classification_20260104.xlsx]`

### Assessment Totals

- **Total formulas:** 100+ external workbook links
- **KPIs tracked:** 23 key metrics
- **Gap capacity:** 50 consolidated gaps
- **Risk capacity:** 40 risks (20 pre-defined + 20 custom)
- **Remediation actions:** 50 action items
- **Evidence index:** 100 evidence entries

---

**END OF SPECIFICATION**

---

*"Logic will get you from A to Z; imagination will get you everywhere."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->

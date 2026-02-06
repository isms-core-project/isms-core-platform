**ISMS-IMP-A.8.28.5-TG - Compliance Dashboard (Master Aggregator) Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard & Master Aggregator |
| **Related Policy** | ISMS-POL-A.8.28 (All Sections) - Control A.8.28 Master Policy |
| **Purpose** | Aggregate compliance data from all four operational assessments (SDLC, Tools, Review/Testing, Supply Chain) to provide executive-level visibility and unified compliance tracking |
| **Target Audience** | CISO, CTO, Board of Directors, Audit Committee, Application Security Leadership, Risk Management, Auditors |
| **Assessment Type** | Consolidation & Reporting |
| **Review Cycle** | Quarterly (Aligned with Board Reporting Cycles) |
| **Date** | [Date]|

**Version History**:

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial dashboard specification |

**Approvers**:

- Application Security Lead (Technical Review)
- Chief Information Security Officer (Executive Approval)
- Chief Technology Officer (Stakeholder Review)

**Related Documents**:

- ISMS-POL-A.8.28 - Secure Coding Policy (Master Policy)
- ISMS-IMP-A.8.28.1 - SDLC Assessment
- ISMS-IMP-A.8.28.2 - Standards & Tools Assessment
- ISMS-IMP-A.8.28.3 - Code Review & Testing Assessment
- ISMS-IMP-A.8.28.4 - Third-Party & OSS Assessment

---

# Technical Specification

# Excel Workbook Structure

## Workbook Overview

**File Name**: `ISMS-IMP-A.8.28.5_Compliance_Dashboard_YYYYMMDD.xlsx`  
**Total Sheets**: 9  
**Python Generator**: `generate_a828_5_compliance_dashboard.py`

**CRITICAL**: This workbook uses **Excel external links** to pull data from source assessments.

**Sheet Structure**:
1. Executive Dashboard (main summary)
2. Gap Analysis (consolidated gaps)
3. Risk Register (high-risk items)
4. Remediation Roadmap (prioritized actions)
5. KPIs & Metrics (performance tracking)
6. Evidence Register (audit evidence)
7. Action Items & Follow-up (task tracking)
8. Audit & Compliance Log (audit history)
9. Approval Sign-Off (executive approval)

---

# Sheet-by-Sheet Technical Specifications

## Sheet 1: Executive Dashboard

**Purpose**: Single-page executive summary

**Layout**:

**Section 1: Overall Compliance (Rows 1-10)**
| Cell | Content | Formula/Value |
|------|---------|---------------|
| B3 | Overall Compliance % | `=(B5+0.5*B6)/(360-B8)*100` |
| B4 | Total Requirements | `360` (fixed: 90×4 assessments) |
| B5 | Implemented | `=SUM(links to all 4 Summary_Dashboard sheets)` |
| B6 | Partial | `=SUM(links to all 4 Summary_Dashboard sheets)` |
| B7 | Not Implemented | `=SUM(links to all 4 Summary_Dashboard sheets)` |
| B8 | N/A | `=SUM(links to all 4 Summary_Dashboard sheets)` |

**Section 2: Domain Breakdown (Rows 12-18)**
| Domain | Source Cell | Formula |
|--------|-------------|---------|
| SDLC Security | IMP-1 Summary B10 | `='[IMP1file]Summary_Dashboard'!B10` |
| Tools & Standards | IMP-2 Summary B10 | `='[IMP2file]Summary_Dashboard'!B10` |
| Review & Testing | IMP-3 Summary B10 | `='[IMP3file]Summary_Dashboard'!B10` |
| Supply Chain | IMP-4 Summary B10 | `='[IMP4file]Summary_Dashboard'!B10` |

**Conditional Formatting (Compliance %)**:

- ≥80%: Green (#C6EFCE)
- 60-79%: Yellow (#FFEB9C)
- <60%: Red (#FFC7CE)

**Section 3: Critical Findings (Rows 20-30)**

- Highest compliance domain (auto-identified with MAX formula)
- Lowest compliance domain (auto-identified with MIN formula)
- Total critical gaps (SUM from all Gap_Analysis sheets)
- Recommended focus areas (conditional text based on lowest domain)

**Section 4: Compliance Trend Chart (Rows 32-40)**

- Line chart showing quarterly compliance trajectory
- Manual data entry for historical quarters
- Auto-populated for current quarter

---

## Sheet 2: Gap Analysis

**Purpose**: Consolidated gaps from all assessments

**Column Structure**:
| Column | Header | Width | Type | Formula/Source |
|--------|--------|-------|------|----------------|
| A | Gap ID | 12 | Auto-number | G-001, G-002, etc. |
| B | Source | 15 | Text | IMP-1 / IMP-2 / IMP-3 / IMP-4 |
| C | Domain | 25 | Text | From source assessment |
| D | Req ID | 12 | Text | Original requirement ID |
| E | Gap Description | 50 | Text | From source Gap_Analysis |
| F | Priority | 12 | Text | Critical/High/Medium/Low |
| G | Owner | 20 | Text | From source Gap_Analysis |
| H | Target Date | 12 | Date | DD.MM.YYYY |
| I | Status | 15 | Text | From source Gap_Analysis |
| J | Notes | 40 | Text | Additional context |

**Data Population**:
Gaps are NOT linked via formulas (too complex). Instead:

- Manual consolidation from source assessments
- OR: Python script can extract gaps and populate

**Conditional Formatting (Priority)**:

- Critical: Dark red (#C00000) white bold
- High: Red (#FF6666)
- Medium: Yellow (#FFEB9C)
- Low: Green (#C6EFCE)

**Summary Metrics (Bottom of Sheet)**:

- Total Gaps: `=COUNTA(A:A)-1`
- Critical: `=COUNTIF(F:F,"Critical")`
- High: `=COUNTIF(F:F,"High")`
- Medium: `=COUNTIF(F:F,"Medium")`
- Low: `=COUNTIF(F:F,"Low")`

---

## Sheet 3: Risk Register

**Purpose**: High-risk items across all domains

**Column Structure**:
| Column | Header | Type |
|--------|--------|------|
| A | Risk ID | Auto-number |
| B | Source Assessment | Text (IMP-1/2/3/4) |
| C | Risk Category | Text |
| D | Risk Description | Text |
| E | Likelihood | Dropdown (Low/Medium/High) |
| F | Impact | Dropdown (Low/Medium/High) |
| G | Risk Score | Formula (`=LOOKUP...`) |
| H | Mitigation Status | Dropdown |
| I | Owner | Text |
| J | Target Mitigation Date | Date |

**Risk Score Calculation**:
| Likelihood | Impact | Risk Score |
|------------|--------|------------|
| Low | Low | 1 (Low) |
| Low | Medium | 2 (Low) |
| Low | High | 3 (Medium) |
| Medium | Low | 2 (Low) |
| Medium | Medium | 4 (Medium) |
| Medium | High | 6 (High) |
| High | Low | 3 (Medium) |
| High | Medium | 6 (High) |
| High | High | 9 (Critical) |

---

## Sheet 4: Remediation Roadmap

**Purpose**: Phased remediation plan

**Column Structure**:
| Column | Header | Type |
|--------|--------|------|
| A | Phase | Text (1/2/3/4) |
| B | Gap ID | Reference to Gap Analysis |
| C | Description | Text |
| D | Owner | Text |
| E | Target Completion | Date |
| F | Dependencies | Text |
| G | Resources Required | Text |
| H | Status | Dropdown |

**Phase Definitions**:

- **Phase 1** (0-30 days): Critical gaps
- **Phase 2** (31-90 days): High-priority gaps
- **Phase 3** (91-180 days): Medium-priority gaps
- **Phase 4** (181+ days): Low-priority/continuous improvement

**Filtering**: Enable auto-filter to view by phase, status, owner

---

## Sheet 5: KPIs & Metrics

**Purpose**: Track key performance indicators

**Metric Categories**:

**SDLC Metrics** (from IMP-1):

- Security requirements coverage (%)
- Threat modeling coverage (%)
- Security sign-off compliance (%)

**Tool Metrics** (from IMP-2):

- SAST coverage (%)
- DAST coverage (%)
- SCA coverage (%)
- Tool effectiveness (vulnerabilities found / false positives)

**Review/Testing Metrics** (from IMP-3):

- Code review coverage (%)
- Security test coverage (%)
- Vulnerabilities caught in review vs. production (ratio)

**Supply Chain Metrics** (from IMP-4):

- SBOM coverage (%)
- Vulnerability remediation MTTR (days)
- License compliance rate (%)

**Overall Maturity Score**:

- Calculated as weighted average of all metrics
- Trend chart showing quarterly improvement

**Formulas**: Link to specific cells in source assessment KPI sheets

---

## Sheet 6: Evidence Register

**Purpose**: Consolidated evidence inventory

**Column Structure**:
| Column | Header | Type |
|--------|--------|------|
| A | Evidence ID | Auto-number |
| B | Source Assessment | Text (IMP-1/2/3/4) |
| C | Requirement ID | Text |
| D | Evidence Type | Text |
| E | Description | Text |
| F | Location/Link | Text |
| G | Last Verified | Date |
| H | Verification Status | Dropdown |

**Evidence Types**:

- SBOM Export
- SCA Scan Report
- Code Review Log
- Pentest Report
- Vendor Contract
- Training Record
- Policy Document
- Configuration Screenshot

**Verification Status**:

- Current (verified within 90 days)
- Expiring Soon (91-180 days)
- Expired (>180 days)
- Not Verified

---

## Sheet 7: Action Items & Follow-up

**Purpose**: Track action items from dashboard reviews

**Column Structure**:
| Column | Header | Type |
|--------|--------|------|
| A | Action ID | Auto-number |
| B | Action Description | Text |
| C | Related Gap ID | Reference |
| D | Owner | Text |
| E | Due Date | Date |
| F | Status | Dropdown |
| G | Blockers | Text |
| H | Completion Date | Date |

**Status Options**:

- Not Started
- In Progress
- Complete
- Blocked

**Conditional Formatting (Due Date)**:

- Overdue: Red background
- Due within 7 days: Yellow background
- Future: No formatting

---

## Sheet 8: Audit & Compliance Log

**Purpose**: Track audit history

**Column Structure**:
| Column | Header | Type |
|--------|--------|------|
| A | Audit Date | Date |
| B | Audit Type | Text (Internal/External/Certification) |
| C | Auditor | Text |
| D | Findings - Critical | Number |
| E | Findings - High | Number |
| F | Findings - Medium | Number |
| G | Findings - Low | Number |
| H | Findings Remediated | Number |
| I | Next Audit Date | Date |
| J | Compliance Status | Text |

**Summary Metrics**:

- Total audits conducted
- Average findings per audit
- Remediation rate (%)
- Compliance trend

---

## Sheet 9: Approval Sign-Off

**Purpose**: Executive approval

**Required Approvers**:
1. Dashboard Compiler (Application Security Analyst)
2. Application Security Lead (Technical Review)
3. Chief Technology Officer (Resource Commitment)
4. Chief Information Security Officer (Executive Approval)

**Approval Criteria** (listed on sheet):

- All four source assessments complete and current
- Gap analysis accurate and complete
- Remediation roadmap has committed owners and dates
- Risk register reflects current risk posture
- CISO acknowledges compliance status

**Approval Statement Template**:
"I acknowledge the current Control A.8.28 compliance status as XX%. I approve the remediation roadmap and commit organizational resources to address identified gaps. Residual risks are accepted in accordance with organizational risk appetite."

---

# Python Script Integration

## Script: generate_a828_5_compliance_dashboard.py

**What the Script Does**:
1. Creates workbook with 9 sheets
2. Sets up external link formulas to source assessments
3. Creates chart templates
4. Applies conditional formatting
5. Protects formula cells, leaves input cells editable

**Output**: `ISMS-IMP-A.8.28.5_Compliance_Dashboard_YYYYMMDD.xlsx`

**Usage**:
```bash
python3 generate_a828_5_compliance_dashboard.py
```

**CRITICAL**: Script assumes source assessment files are in same directory with standardized names.

## External Link Formula Pattern

**Example** (Overall Compliance from IMP-1):
```excel
='[ISMS-IMP-A.8.28.1_SDLC_Assessment_20260125.xlsx]Summary_Dashboard'!$B$10
```

**Pattern**:

- `[filename]`: Source workbook file name
- `SheetName`: Sheet name in source workbook
- `$B$10`: Cell reference (absolute)

**Updating Links**:
When source files are updated:
1. Open dashboard
2. Excel prompts: "Update links?"
3. Click "Update"
4. Formulas auto-refresh with new data

---

# Quarterly Update Process (Technical)

## Automated Update Steps

**Step 1**: Refresh all source assessments (IMP 1-4)
**Step 2**: Save source assessments with new date suffix
**Step 3**: Open dashboard workbook
**Step 4**: Update external links

```
Data → Edit Links → Update Values
```

**Step 5**: Verify formulas recalculated
**Step 6**: Add new historical trend data point (manual entry)
**Step 7**: Update Gap Analysis sheet (manual consolidation or script)
**Step 8**: Save dashboard with new date suffix

## Historical Trend Data Entry

**Manual Entry Required** (Sheet: Executive Dashboard, Section 4):

| Quarter | Overall Compliance % |
|---------|----------------------|
| Q1 2025 | 72% |
| Q2 2025 | 75% |
| Q3 2025 | 78% |
| Q4 2025 | 81% |
| Q1 2026 | [auto-populated from current data] |

**Chart**: Line chart showing quarterly improvement

---

# Dashboard Customization

## Optional Enhancements

**Advanced Charts**:

- Radar chart showing domain-by-domain compliance
- Heat map for gap distribution
- Burndown chart for remediation progress

**Custom Metrics**:

- Security incident rate vs. compliance %
- Cost of security defects vs. prevention investment
- Developer productivity vs. tool adoption

**Executive Reporting**:

- One-page PDF export for board
- PowerPoint export with key charts
- Email summary automation

## Integration with Other Tools

**Export to**:

- JIRA (gap remediation tracking)
- ServiceNow (action item management)
- Power BI (advanced analytics)
- Tableau (executive dashboards)

---

**END OF SPECIFICATION**

---

*"Cryptographic systems should be designed to minimize the damage that can occur when they fail."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->

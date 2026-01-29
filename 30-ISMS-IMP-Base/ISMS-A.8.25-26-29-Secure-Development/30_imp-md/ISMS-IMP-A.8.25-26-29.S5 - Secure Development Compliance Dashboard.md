# ISMS-IMP-A.8.25-26-29-S5 - Secure Development Compliance Dashboard
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Controls A.8.25, A.8.26, A.8.29: Secure Development Framework

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.25-26-29-S5 |
| **Version** | 1.0 |
| **Assessment Area** | Secure Development Compliance Dashboard (A.8.25, A.8.26, A.8.29 Combined) |
| **Related Policy** | ISMS-POL-A.8.25-26-29 All Sections |
| **Purpose** | Executive dashboard aggregating security requirements (A.8.26), SDLC security activities (A.8.25), security testing (A.8.29), and vulnerability remediation metrics into unified compliance view |
| **Target Audience** | CISO, Security Leadership, Development Executives, Auditors, Compliance Officers |
| **Assessment Type** | Portfolio-level or application-level executive summary |
| **Review Cycle** | Quarterly for portfolio view, Monthly for critical applications |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial dashboard specification | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Dashboard Overview
  - Prerequisites
  - Dashboard Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION** (Separate section)
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formulas & Calculations
  - Data Validation & Conditional Formatting

---

# PART I: USER COMPLETION GUIDE

## 1. Dashboard Overview

### 1.1 Purpose & Scope

**Dashboard Name:** ISMS-IMP-A.8.25-26-29-S5 - Secure Development Compliance Dashboard

**What This Dashboard Provides:**
- **Executive Summary:** Single-page view of secure development compliance
- **Aggregated Metrics:** Combines data from all 4 assessment workbooks (IMP-S1, S2, S3, S4)
- **Maturity Scoring:** Overall secure development maturity level (Level 1-5)
- **Trend Analysis:** Progress over time (quarterly/annual)
- **Risk Identification:** Critical gaps and recommendations
- **Compliance Status:** A.8.25, A.8.26, A.8.29 compliance scores

**This Dashboard is For:**
- CISO and security leadership (strategic oversight)
- Development executives (resource allocation decisions)
- Auditors (compliance verification)
- Board reporting (executive summary)
- Portfolio-level assessment (all applications combined)

**This Dashboard is NOT For:**
- Detailed technical findings (see IMP-S1, S2, S3, S4)
- Individual vulnerability tracking (see IMP-S4)
- Operational security activities (see IMP-S2)

### 1.2 Dashboard Workbook Structure

**Total Sheets:** 5

**Completion Sequence:**

1. **Executive Summary** - One-page overview with key metrics and scores
2. **Control Compliance** - A.8.25, A.8.26, A.8.29 compliance status
3. **Maturity Assessment** - Secure development maturity level (1-5)
4. **Trend Analysis** - Progress over time (quarterly data)
5. **Recommendations** - Prioritized actions for improvement

**Estimated Completion Time:**
- Portfolio Dashboard (10+ applications): 2-3 hours
- Single Application Dashboard: 1 hour

### 1.3 Key Dashboard Questions

This dashboard answers:
- ✅ What is our overall secure development maturity level?
- ✅ Are we compliant with A.8.25, A.8.26, A.8.29?
- ✅ What are our critical gaps?
- ✅ Are we improving over time?
- ✅ What are the top priorities for investment?
- ✅ How do we compare to industry benchmarks?

---

## 2. Prerequisites

### 2.1 Required Assessment Data

**Before creating dashboard, complete these assessments:**

**For Each Application in Scope:**
- [ ] **IMP-S1:** Security Requirements Assessment (completed)
- [ ] **IMP-S2:** SDLC Security Activities Assessment (completed)
- [ ] **IMP-S3:** Security Testing Results Assessment (completed)
- [ ] **IMP-S4:** Vulnerability Remediation Assessment (completed)

**Data to Extract from Each Assessment:**

**From IMP-S1 (Security Requirements):**
- Application risk classification (High/Medium/Low)
- SRS completeness score (%)
- Threat modeling completeness score (%)
- Architecture review status
- Requirements traceability score (%)
- Overall compliance score (%)

**From IMP-S2 (SDLC Activities):**
- SDLC phase activities score (%)
- Secure coding standards maturity (%)
- Code review maturity (%)
- Security tools deployment score (%)
- Developer training completion (%)
- Overall SDLC security maturity (%)

**From IMP-S3 (Security Testing):**
- SAST execution status and findings
- DAST execution status and findings
- SCA execution status and findings
- Penetration testing status
- Testing coverage score (%)
- Critical/High vulnerabilities found

**From IMP-S4 (Vulnerability Remediation):**
- Open vulnerabilities (Critical, High, Medium, Low)
- SLA compliance rate (%)
- Overdue vulnerabilities count
- Average remediation time
- Technical debt count
- Remediation health score (%)

### 2.2 Required Tools

**Excel Workbook:**
- Excel 2016 or later (Office 365 recommended)
- Power Query (for data aggregation - optional but recommended)

**Data Sources:**
- Access to all completed assessment workbooks (IMP-S1, S2, S3, S4)
- Historical dashboard data (for trend analysis)

**Optional:**
- BI tool (Tableau, Power BI) for enhanced visualization
- Python/scripting for automated data extraction

### 2.3 Assessor Skills

**Required:**
- Understanding of ISO 27001:2022 Controls A.8.25, A.8.26, A.8.29
- Familiarity with all ISMS-POL-A.8.25-26-29 sections
- Executive communication skills (translating technical findings to business language)
- Data aggregation and analysis skills

**Helpful:**
- Experience with maturity models (CMMI, SAMM, BSIMM)
- Dashboard design and visualization
- Excel Power Query or BI tools

---

## 3. Dashboard Workflow

### 3.1 Dashboard Creation Process

**Phase 1: Data Collection** (30-60 minutes)
1. Gather all completed assessment workbooks (IMP-S1, S2, S3, S4)
2. Extract key metrics from each workbook (see Section 2.1)
3. Verify data accuracy and completeness
4. Identify any missing assessments

**Phase 2: Dashboard Population** (1-2 hours)
5. Complete Executive Summary (Sheet 1)
6. Calculate Control Compliance scores (Sheet 2)
7. Assess Maturity Level (Sheet 3)
8. Add historical data for Trend Analysis (Sheet 4)
9. Develop prioritized Recommendations (Sheet 5)

**Phase 3: Review & Validation** (30 minutes)
10. Verify all calculations correct
11. Cross-check against source workbooks
12. Validate maturity level assessment
13. Review recommendations with stakeholders

**Phase 4: Presentation** (varies)
14. Present to CISO and security leadership
15. Present to development executives
16. Board reporting (if applicable)
17. Audit submission (if applicable)

**Phase 5: Continuous Improvement** (ongoing)
18. Track recommendation implementation
19. Update quarterly with new assessment data
20. Monitor trend progress

### 3.2 Portfolio vs. Application Dashboard

**Portfolio Dashboard:**
- Aggregates data from ALL applications
- Shows organization-wide secure development maturity
- Used for strategic planning and resource allocation
- Updated quarterly

**Application Dashboard:**
- Focuses on single critical application
- Shows application-specific compliance and maturity
- Used for application-specific improvement plans
- Updated monthly for High-Risk applications

### 3.3 Maturity Model Reference

This dashboard uses a 5-level maturity model aligned with CMMI:

**Level 1 - Initial/Ad Hoc:**
- No formal secure development processes
- Security activities inconsistent or missing
- High vulnerability counts, poor remediation
- **Score:** <50%

**Level 2 - Managed:**
- Basic secure development processes documented
- Some security activities executed
- Moderate vulnerability management
- **Score:** 50-69%

**Level 3 - Defined:**
- Comprehensive secure development processes
- Security activities consistently executed
- Good vulnerability management and remediation
- **Score:** 70-84%

**Level 4 - Quantitatively Managed:**
- Metrics-driven secure development
- Security activities optimized and measured
- Excellent vulnerability management
- **Score:** 85-94%

**Level 5 - Optimizing:**
- Continuous improvement culture
- Security deeply embedded in SDLC
- Proactive vulnerability prevention
- **Score:** ≥95%

---

## 4. Completing Each Sheet

### 4.1 Sheet 1: Executive Summary

**Purpose:** One-page executive overview with key metrics and scores.

**Completion Time:** 15-20 minutes

**Key Sections:**

**A. Dashboard Header**
- **Assessment Date:** Date of this dashboard
- **Reporting Period:** Time period covered (e.g., Q4 2025)
- **Scope:** Portfolio (all applications) or specific application
- **Applications Assessed:** Count (for portfolio) or name (for application)

**B. Overall Compliance Score** (Large, prominent)

```
┌─────────────────────────────────────┐
│  Secure Development Compliance      │
│           85%                       │
│  Level 3: Defined                   │
└─────────────────────────────────────┘
```

**Calculation:**
```
Overall Score = Average of (A.8.26 Score, A.8.25 Score, A.8.29 Score, Remediation Score)
```

**C. Control Compliance Summary**

| Control | Score | Status |
|---------|-------|--------|
| A.8.26 - Security Requirements | 88% | ✅ Compliant |
| A.8.25 - Secure Development Lifecycle | 82% | ✅ Compliant |
| A.8.29 - Security Testing | 85% | ✅ Compliant |
| Vulnerability Remediation | 86% | ✅ Compliant |

**Status Logic:**
- ✅ Compliant: ≥70%
- ⚠️ Partial: 50-69%
- ❌ Non-Compliant: <50%

**D. Key Metrics At-a-Glance**

| Metric | Value | Trend |
|--------|-------|-------|
| Applications Assessed | 12 | - |
| High-Risk Applications | 4 | - |
| Security Requirements Coverage | 88% | ↑ |
| SDLC Security Maturity | 82% | ↑ |
| Security Testing Coverage | 85% | → |
| Open Critical Vulnerabilities | 3 | ↓ |
| SLA Compliance Rate | 86% | ↑ |

**Trend Symbols:**
- ↑ Improving (vs. last quarter)
- → Stable
- ↓ Degrading

**E. Critical Gaps (Top 3)**

1. **Gap:** 15 High vulnerabilities overdue >30 days
   **Impact:** Increased security risk, potential compliance violation
   **Priority:** P1

2. **Gap:** Penetration testing not conducted for 2 High-Risk applications
   **Impact:** Unknown vulnerabilities, audit finding risk
   **Priority:** P1

3. **Gap:** DAST coverage only 60% (target 90%)
   **Impact:** Runtime vulnerabilities not detected
   **Priority:** P2

**F. Executive Recommendation**

*Single paragraph summarizing top recommendation:*

"Immediate focus required on vulnerability remediation velocity. With 15 High-severity vulnerabilities overdue and SLA compliance at 86% (target 95%), recommend establishing dedicated security response team and implementing daily standup for overdue critical/high findings until backlog cleared."

**Completion Tips:**
- Keep Executive Summary to ONE PAGE (printable)
- Use large, clear fonts for key metrics
- Focus on business impact, not technical details
- Highlight trends (improving/degrading)
- Make top recommendation actionable

**Common Mistakes:**
- ❌ Too much detail (defeats purpose of executive summary)
- ❌ Technical jargon (executives want business impact)
- ❌ No trends (executives want progress visibility)
- ❌ Vague recommendations ("improve security")

### 4.2 Sheet 2: Control Compliance

**Purpose:** Detailed breakdown of A.8.25, A.8.26, A.8.29 compliance.

**Completion Time:** 20-30 minutes

**Structure:**

**Section A: ISO 27001:2022 Control A.8.26 - Application Security Requirements**

**Sub-Metrics:**
- Security requirements specification completeness: X%
- Threat modeling completion: X%
- Security architecture review: X%
- Requirements traceability: X%
- **Overall A.8.26 Score:** X%

**Compliance Status:** ✅/⚠️/❌

**Gap Summary:**
- Applications without SRS: X
- Applications without threat model: X (High-Risk apps)
- Applications without architecture review: X

**Section B: ISO 27001:2022 Control A.8.25 - Secure Development Lifecycle**

**Sub-Metrics:**
- SDLC phase security activities: X%
- Secure coding standards adoption: X%
- Code review execution: X%
- Security tools deployment: X%
- Developer training completion: X%
- **Overall A.8.25 Score:** X%

**Compliance Status:** ✅/⚠️/❌

**Gap Summary:**
- Applications without SAST: X
- Applications without code review: X
- Developers without training: X

**Section C: ISO 27001:2022 Control A.8.29 - Security Testing**

**Sub-Metrics:**
- SAST execution coverage: X%
- DAST execution coverage: X%
- SCA execution coverage: X%
- Penetration testing coverage: X%
- Security acceptance testing: X%
- **Overall A.8.29 Score:** X%

**Compliance Status:** ✅/⚠️/❌

**Gap Summary:**
- High-Risk applications without pen test: X
- Applications without DAST: X
- Applications without SCA: X

**Section D: Vulnerability Remediation (Operational Metric)**

**Sub-Metrics:**
- SLA compliance rate: X%
- Overdue vulnerabilities: X
- Average remediation time vs. SLA: X%
- Technical debt management: X%
- **Overall Remediation Score:** X%

**Compliance Status:** ✅/⚠️/❌

**Gap Summary:**
- Critical vulnerabilities overdue: X
- High vulnerabilities overdue: X
- Technical debt items >180 days: X

**Completion Tips:**
- Pull metrics from each IMP workbook (don't estimate)
- Calculate overall score as average of sub-metrics
- Document specific gaps with counts
- Compare against policy requirements

**Common Mistakes:**
- ❌ Averaging without weighting (some metrics more important)
- ❌ Not documenting gaps (just showing scores)
- ❌ Not comparing to policy requirements (what's required vs. achieved)

### 4.3 Sheet 3: Maturity Assessment

**Purpose:** Assess overall secure development maturity level (1-5).

**Completion Time:** 20-30 minutes

**Maturity Dimensions:**

**A. Requirements Management Maturity (A.8.26)**

| Level | Criteria | Score Range | Status |
|-------|----------|-------------|--------|
| Level 1 | No formal security requirements | <50% | - |
| Level 2 | Basic requirements documented | 50-69% | - |
| Level 3 | Comprehensive requirements with threat modeling | 70-84% | ← Current |
| Level 4 | Requirements validated and traceable | 85-94% | - |
| Level 5 | Continuous requirements improvement | ≥95% | - |

**Current Level:** 3 (based on 88% score)

**B. SDLC Security Maturity (A.8.25)**

| Level | Criteria | Score Range | Status |
|-------|----------|-------------|--------|
| Level 1 | No formal SDLC security | <50% | - |
| Level 2 | Basic security activities | 50-69% | - |
| Level 3 | Security integrated in SDLC | 70-84% | ← Current |
| Level 4 | Metrics-driven security | 85-94% | - |
| Level 5 | Continuous optimization | ≥95% | - |

**Current Level:** 3 (based on 82% score)

**C. Security Testing Maturity (A.8.29)**

| Level | Criteria | Score Range | Status |
|-------|----------|-------------|--------|
| Level 1 | Ad-hoc security testing | <50% | - |
| Level 2 | Basic SAST/DAST | 50-69% | - |
| Level 3 | Comprehensive testing suite | 70-84% | ← Current |
| Level 4 | Automated testing in CI/CD | 85-94% | - |
| Level 5 | Continuous testing & prevention | ≥95% | - |

**Current Level:** 3 (based on 85% score)

**D. Vulnerability Management Maturity**

| Level | Criteria | Score Range | Status |
|-------|----------|-------------|--------|
| Level 1 | Reactive, no SLAs | <50% | - |
| Level 2 | Basic tracking | 50-69% | - |
| Level 3 | SLA-driven remediation | 70-84% | ← Current |
| Level 4 | Proactive prevention | 85-94% | - |
| Level 5 | Predictive analytics | ≥95% | - |

**Current Level:** 3 (based on 86% score)

**Overall Maturity Level:**

**Calculation:** Average of all dimension levels

**Result:** Level 3 - Defined

**Level 3 Characteristics:**
- ✅ Formal secure development processes established
- ✅ Security activities consistently executed
- ✅ Good vulnerability management
- ⚠️ Room for automation and optimization
- ⚠️ Metrics collection improving

**Path to Level 4:**
- Automate security testing in CI/CD (currently manual/semi-automated)
- Implement metrics-driven decision making
- Reduce critical vulnerability discovery (shift left)
- Achieve 90%+ SLA compliance consistently

**Completion Tips:**
- Use objective score ranges (not subjective judgment)
- Document evidence for each level assessment
- Identify specific gaps preventing next level
- Create roadmap to next level

**Common Mistakes:**
- ❌ Inflating maturity level (wishful thinking)
- ❌ Not documenting evidence for level assignment
- ❌ Jumping levels (must progress sequentially)

### 4.4 Sheet 4: Trend Analysis

**Purpose:** Track progress over time (quarterly or annual).

**Completion Time:** 15-20 minutes

**Quarterly Trend Table:**

| Metric | Q1 2025 | Q2 2025 | Q3 2025 | Q4 2025 | Trend |
|--------|---------|---------|---------|---------|-------|
| Overall Compliance | 78% | 80% | 83% | 85% | ↑ |
| A.8.26 Score | 82% | 84% | 86% | 88% | ↑ |
| A.8.25 Score | 75% | 78% | 80% | 82% | ↑ |
| A.8.29 Score | 80% | 82% | 84% | 85% | ↑ |
| Remediation Score | 75% | 78% | 84% | 86% | ↑ |
| Open Critical Vulns | 8 | 6 | 4 | 3 | ↓ |
| SLA Compliance | 78% | 82% | 84% | 86% | ↑ |

**Trend Visualization:**

*Excel line chart showing quarterly progression*

**Year-over-Year Comparison:**

| Metric | Q4 2024 | Q4 2025 | Change |
|--------|---------|---------|--------|
| Overall Compliance | 70% | 85% | +15% |
| Maturity Level | Level 2 | Level 3 | +1 |
| Critical Vulns | 12 | 3 | -9 |

**Completion Tips:**
- Collect historical data from previous dashboards
- Use consistent metrics (don't change definitions)
- Show both quarterly and YoY trends
- Visualize trends (charts more impactful than tables)

**Common Mistakes:**
- ❌ Changing metric definitions (makes trends invalid)
- ❌ Cherry-picking favorable trends
- ❌ Not explaining anomalies (sudden spikes/drops)

### 4.5 Sheet 5: Recommendations

**Purpose:** Prioritized action plan for improvement.

**Completion Time:** 20-30 minutes

**Recommendation Structure:**

**For each recommendation, document:**

| # | Recommendation | Current State | Target State | Priority | Effort | Owner | Target Date |
|---|---------------|---------------|--------------|----------|--------|-------|-------------|
| 1 | Establish critical vulnerability response team | 15 Critical vulns overdue, avg 45 days to remediate | 0 Critical overdue, <7 days avg remediation | P1 | High | Development Manager | 2026-02-28 |
| 2 | Automate SAST/DAST in CI/CD pipeline | Manual execution, 70% coverage | Automated per-commit, 95% coverage | P1 | High | DevOps Lead | 2026-03-31 |
| 3 | Conduct pen testing for 2 High-Risk apps | No pen test in 12 months | Annual pen test completed | P1 | Medium | Security Architect | 2026-02-15 |
| 4 | Improve developer security training | 75% completion, annual only | 95% completion, quarterly refresher | P2 | Medium | Security Champion | 2026-04-30 |
| 5 | Implement SCA for all applications | 60% coverage | 100% coverage | P2 | Low | Development Leads | 2026-05-31 |

**Priority Legend:**
- **P1 (Immediate):** Critical gaps, compliance risk, High-Risk applications
- **P2 (High):** Important improvements, maturity advancement
- **P3 (Medium):** Optimization, Level 4 preparation
- **P4 (Low):** Nice-to-have, long-term strategic

**Effort Estimates:**
- **Low:** <40 hours, minimal budget
- **Medium:** 40-160 hours, moderate budget
- **High:** >160 hours, significant budget

**Quick Wins (Low Effort, High Impact):**

1. Enable SAST in CI/CD for top 5 applications (Low effort, P1)
2. Schedule pen test for 2 overdue High-Risk applications (Low effort, P1)
3. Create security bug template in Jira (Low effort, P2)

**Strategic Initiatives (High Effort, High Impact):**

1. Establish Security Champion program across all teams (High effort, P1)
2. Implement automated security testing in all CI/CD pipelines (High effort, P1)
3. Deploy SCA across entire application portfolio (High effort, P2)

**Completion Tips:**
- Prioritize by risk (compliance gaps = P1)
- Balance quick wins with strategic initiatives
- Assign realistic owners (get commitment)
- Set achievable target dates
- Link recommendations to specific gaps from Sheet 2

**Common Mistakes:**
- ❌ Too many recommendations (overwhelming)
- ❌ All recommendations P1 (no prioritization)
- ❌ Vague recommendations ("improve security")
- ❌ No owners or target dates (never happens)

---

## 5. Evidence Collection

**Dashboard Evidence:**
- All 4 completed assessment workbooks (IMP-S1, S2, S3, S4)
- Historical dashboard data (previous quarters)
- Calculation worksheets (showing how scores were derived)
- Executive presentation (if presented)

---

## 6. Common Pitfalls

### 6.1 Mistake 1: Creating Dashboard Without Completing Underlying Assessments

**Problem:** Dashboard created with estimated/guessed scores, not actual assessment data.

**Impact:** Inaccurate dashboard, misleading executives.

**Solution:** Complete all 4 IMP assessments FIRST, then create dashboard.

### 6.2 Mistake 2: Inconsistent Scoring

**Problem:** Different scoring methodologies across quarters, trends invalid.

**Impact:** Can't track progress accurately.

**Solution:** Document scoring methodology, use consistently.

### 6.3 Mistake 3: Dashboard Too Technical

**Problem:** Dashboard full of CWEs, CVEs, technical jargon.

**Impact:** Executives can't understand, dashboard ignored.

**Solution:** Translate to business language, focus on risk and impact.

### 6.4 Mistake 4: No Actionable Recommendations

**Problem:** Dashboard shows problems but no solutions.

**Impact:** Executives see problems but don't know what to do.

**Solution:** Always include specific, prioritized recommendations with owners.

### 6.5 Mistake 5: Inflating Scores

**Problem:** Assessor rounds up scores to make dashboard look better.

**Impact:** False sense of security, complacency.

**Solution:** Use actual scores, be honest about gaps.

---

## 7. Quality Checklist

- [ ] All 5 sheets completed
- [ ] All scores pulled from actual assessments (not estimated)
- [ ] Executive Summary fits on one page
- [ ] Maturity level justified with evidence
- [ ] Trends show historical data (not just current)
- [ ] Recommendations are specific and prioritized
- [ ] Dashboard reviewed by CISO before presentation
- [ ] Evidence package complete

---

## 8. Review & Approval

1. Self-review (quality checklist)
2. CISO review and approval
3. Executive presentation (if applicable)
4. Archive for historical trending

---

**END OF PART I: USER COMPLETION GUIDE**

This dashboard provides the executive visibility needed for strategic security decisions and continuous improvement! 📊✅
# ISMS-IMP-A.8.25-26-29-S5 - Secure Development Compliance Dashboard
## PART II: TECHNICAL SPECIFICATION

---

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Workbook Overview

### Workbook Metadata

**Filename Format:** `ISMS-A825-26-29-Dashboard-[Portfolio or APP-ID]-[YYYYMMDD].xlsx`

**Examples:**
- `ISMS-A825-26-29-Dashboard-Portfolio-20260123.xlsx` (portfolio view)
- `ISMS-A825-26-29-Dashboard-APP-CUST-20260123.xlsx` (application view)

**Total Sheets:** 5

**Excel Version:** Excel 2016+ (Office 365 recommended)

**File Size Estimate:** 200KB - 1MB

**Python Script:** `generate_a825_26_29_5_compliance_dashboard.py`

### Workbook Structure Summary

| Sheet # | Sheet Name | Purpose | Data Source | Complexity |
|---------|------------|---------|-------------|------------|
| 1 | Executive Summary | One-page overview | IMP-S1,S2,S3,S4 | High |
| 2 | Control Compliance | A.8.25/26/29 scores | IMP-S1,S2,S3,S4 | Medium |
| 3 | Maturity Assessment | Maturity level 1-5 | Calculated from scores | Medium |
| 4 | Trend Analysis | Quarterly progress | Historical dashboards | Low |
| 5 | Recommendations | Action plan | Gap analysis | Low |

---

## Common Structure Elements

### Standard Colors

**Headers:** `RGB(0, 51, 102)` Dark Blue, White text, 14pt Bold
**Metrics (Large):** `RGB(68, 114, 196)` Blue, 24pt Bold (for Executive Summary scores)
**Input Cells:** `RGB(255, 255, 204)` Light Yellow
**Auto-Calculated:** `RGB(217, 217, 217)` Light Gray

**Status Colors:**
- ✅ Compliant (≥70%): `RGB(198, 239, 206)` Light Green
- ⚠️ Partial (50-69%): `RGB(255, 235, 156)` Light Yellow
- ❌ Non-Compliant (<50%): `RGB(255, 199, 206)` Light Red

**Maturity Levels:**
- Level 5: `RGB(0, 176, 80)` Dark Green
- Level 4: `RGB(146, 208, 80)` Light Green
- Level 3: `RGB(255, 192, 0)` Orange
- Level 2: `RGB(255, 153, 0)` Dark Orange
- Level 1: `RGB(192, 0, 0)` Red

### Data Validation

**Status Dropdown:**
```excel
List: ✅ Compliant,⚠️ Partial,❌ Non-Compliant
```

**Trend Dropdown:**
```excel
List: ↑ Improving,→ Stable,↓ Degrading
```

**Priority Dropdown:**
```excel
List: P1 (Immediate),P2 (High),P3 (Medium),P4 (Low)
```

**Effort Dropdown:**
```excel
List: Low,Medium,High
```

---

## Sheet 1: Executive Summary

### Structure

**This sheet should fit on ONE PAGE (portrait orientation)**

#### Section A: Dashboard Header (Rows 1-5)

**Merged Cells:** A1:G5 (Large header block)

| Row | Content | Format |
|-----|---------|--------|
| 1-2 | "SECURE DEVELOPMENT COMPLIANCE DASHBOARD" | 18pt Bold, Centered |
| 3 | Assessment Date: [Date] | 12pt |
| 4 | Reporting Period: [Period] | 12pt |
| 5 | Scope: [Portfolio/Application] | 12pt |

#### Section B: Overall Compliance Score (Rows 7-12)

**Merged Cells:** A7:D12 (Large score display)

**Content:**
```
Secure Development Compliance
        85%
   Level 3: Defined
```

**Format:**
- "85%" → 36pt Bold, Blue
- "Level 3: Defined" → 14pt Bold

**Formula for Overall Score (Cell B9):**
```excel
=AVERAGE(Sheet2!B10, Sheet2!B20, Sheet2!B30, Sheet2!B40)
```
*Average of A.8.26, A.8.25, A.8.29, Remediation scores from Sheet 2*

**Formula for Maturity Level (Cell B11):**
```excel
=IF(B9>=95,"Level 5: Optimizing",IF(B9>=85,"Level 4: Quantitatively Managed",IF(B9>=70,"Level 3: Defined",IF(B9>=50,"Level 2: Managed","Level 1: Initial"))))
```

#### Section C: Control Compliance Summary (Rows 7-12, Columns F-G)

**Table:**

| Control | Score | Status |
|---------|-------|--------|
| A.8.26 - Security Requirements | =Sheet2!B10 | Formula |
| A.8.25 - Secure Development Lifecycle | =Sheet2!B20 | Formula |
| A.8.29 - Security Testing | =Sheet2!B30 | Formula |
| Vulnerability Remediation | =Sheet2!B40 | Formula |

**Status Formula (Cell G8):**
```excel
=IF(F8>=70,"✅ Compliant",IF(F8>=50,"⚠️ Partial","❌ Non-Compliant"))
```

#### Section D: Key Metrics At-a-Glance (Rows 14-22)

**Table:**

| Metric | Value | Trend |
|--------|-------|-------|
| Applications Assessed | User input | - |
| High-Risk Applications | User input | - |
| Security Requirements Coverage | =Sheet2!B6 | User selects |
| SDLC Security Maturity | =Sheet2!B16 | User selects |
| Security Testing Coverage | =Sheet2!B26 | User selects |
| Open Critical Vulnerabilities | User input | User selects |
| SLA Compliance Rate | =Sheet2!B36 | User selects |

#### Section E: Critical Gaps (Rows 24-30)

**Table:** User inputs top 3 gaps manually

| # | Gap | Impact | Priority |
|---|-----|--------|----------|
| 1 | [Description] | [Impact] | Dropdown: Priority |
| 2 | [Description] | [Impact] | Dropdown: Priority |
| 3 | [Description] | [Impact] | Dropdown: Priority |

#### Section F: Executive Recommendation (Rows 32-35)

**Merged Cells:** A32:G35

**Content:** User writes 2-3 sentence summary recommendation

---

## Sheet 2: Control Compliance

### Structure

**4 Main Sections (one per control/metric):**

#### Section A: ISO 27001:2022 Control A.8.26 - Application Security Requirements (Rows 5-12)

**Table:**

| Row | Sub-Metric | Score Source | Weight | Weighted Score |
|-----|-----------|--------------|--------|----------------|
| 6 | Security Requirements Specification | User input from IMP-S1 | 30% | =B6*C6 |
| 7 | Threat Modeling Completion | User input from IMP-S1 | 25% | =B7*C7 |
| 8 | Security Architecture Review | User input from IMP-S1 | 25% | =B8*C8 |
| 9 | Requirements Traceability | User input from IMP-S1 | 20% | =B9*C9 |
| 10 | **Overall A.8.26 Score** | **=SUM(D6:D9)** | **100%** | - |

**Gap Summary (Rows 11-12):** User documents gap counts

#### Section B: ISO 27001:2022 Control A.8.25 - Secure Development Lifecycle (Rows 14-22)

**Table:**

| Row | Sub-Metric | Score Source | Weight | Weighted Score |
|-----|-----------|--------------|--------|----------------|
| 15 | SDLC Phase Security Activities | User input from IMP-S2 | 25% | =B15*C15 |
| 16 | Secure Coding Standards | User input from IMP-S2 | 20% | =B16*C16 |
| 17 | Code Review Execution | User input from IMP-S2 | 20% | =B17*C17 |
| 18 | Security Tools Deployment | User input from IMP-S2 | 20% | =B18*C18 |
| 19 | Developer Training | User input from IMP-S2 | 15% | =B19*C19 |
| 20 | **Overall A.8.25 Score** | **=SUM(D15:D19)** | **100%** | - |

#### Section C: ISO 27001:2022 Control A.8.29 - Security Testing (Rows 24-32)

**Table:**

| Row | Sub-Metric | Score Source | Weight | Weighted Score |
|-----|-----------|--------------|--------|----------------|
| 25 | SAST Execution Coverage | User input from IMP-S3 | 25% | =B25*C25 |
| 26 | DAST Execution Coverage | User input from IMP-S3 | 25% | =B26*C26 |
| 27 | SCA Execution Coverage | User input from IMP-S3 | 20% | =B27*C27 |
| 28 | Penetration Testing | User input from IMP-S3 | 20% | =B28*C28 |
| 29 | Security Acceptance Testing | User input from IMP-S3 | 10% | =B29*C29 |
| 30 | **Overall A.8.29 Score** | **=SUM(D25:D29)** | **100%** | - |

#### Section D: Vulnerability Remediation (Rows 34-42)

**Table:**

| Row | Sub-Metric | Score Source | Weight | Weighted Score |
|-----|-----------|--------------|--------|----------------|
| 35 | SLA Compliance Rate | User input from IMP-S4 | 40% | =B35*C35 |
| 36 | Overdue Vulnerabilities (inverse) | User input from IMP-S4 | 30% | =B36*C36 |
| 37 | Avg Remediation Time vs SLA | User input from IMP-S4 | 20% | =B37*C37 |
| 38 | Technical Debt Management | User input from IMP-S4 | 10% | =B38*C38 |
| 40 | **Overall Remediation Score** | **=SUM(D35:D38)** | **100%** | - |

### Conditional Formatting

**Cells B10, B20, B30, B40** (Overall Scores):
- If ≥70% → Green background
- If 50-69% → Yellow background
- If <50% → Red background

---

## Sheet 3: Maturity Assessment

### Structure

**4 Maturity Dimensions (one per control/metric):**

#### Dimension A: Requirements Management Maturity (Rows 5-12)

**Table:**

| Level | Criteria | Score Range | Status |
|-------|----------|-------------|--------|
| Level 5 | Continuous improvement | ≥95% | Formula |
| Level 4 | Requirements validated | 85-94% | Formula |
| Level 3 | Comprehensive requirements | 70-84% | Formula |
| Level 2 | Basic requirements | 50-69% | Formula |
| Level 1 | No formal requirements | <50% | Formula |

**Current Level (Row 12):** Formula based on Sheet2!B10

**Formula for Status (Cell D6):**
```excel
=IF(AND(Sheet2!$B$10>=95),"← Current","")
```
*Repeat for each level with appropriate ranges*

**Current Level Formula (Cell B12):**
```excel
=IF(Sheet2!B10>=95,5,IF(Sheet2!B10>=85,4,IF(Sheet2!B10>=70,3,IF(Sheet2!B10>=50,2,1))))
```

#### Dimension B: SDLC Security Maturity (Rows 14-21)

*Same structure as Dimension A, references Sheet2!B20*

#### Dimension C: Security Testing Maturity (Rows 23-30)

*Same structure, references Sheet2!B30*

#### Dimension D: Vulnerability Management Maturity (Rows 32-39)

*Same structure, references Sheet2!B40*

#### Overall Maturity Level (Rows 41-45)

**Formula (Cell B42):**
```excel
=ROUND(AVERAGE(B12,B21,B30,B39),0)
```
*Average of all dimension levels, rounded to integer*

**Display (Cell B43):**
```excel
="Level " & B42 & ": " & IF(B42=5,"Optimizing",IF(B42=4,"Quantitatively Managed",IF(B42=3,"Defined",IF(B42=2,"Managed","Initial"))))
```

### Conditional Formatting

**Cell B42** (Overall Maturity Level):
- If 5 → Dark Green background
- If 4 → Light Green background
- If 3 → Orange background
- If 2 → Dark Orange background
- If 1 → Red background

---

## Sheet 4: Trend Analysis

### Structure

**Quarterly Trend Table (Rows 5-15):**

**Columns:** A (Metric), B (Q1), C (Q2), D (Q3), E (Q4), F (Trend)

**Rows:**

| Metric | Q1 | Q2 | Q3 | Q4 | Trend |
|--------|----|----|----|----|-------|
| Overall Compliance | User input | User input | User input | User input | Formula |
| A.8.26 Score | User input | User input | User input | User input | Formula |
| A.8.25 Score | User input | User input | User input | User input | Formula |
| A.8.29 Score | User input | User input | User input | User input | Formula |
| Remediation Score | User input | User input | User input | User input | Formula |
| Open Critical Vulns | User input | User input | User input | User input | Formula |
| SLA Compliance | User input | User input | User input | User input | Formula |

**Trend Formula (Cell F6):**
```excel
=IF(E6>D6,"↑ Improving",IF(E6=D6,"→ Stable","↓ Degrading"))
```

**Year-over-Year Comparison Table (Rows 17-25):**

| Metric | Q4 Last Year | Q4 This Year | Change |
|--------|--------------|--------------|--------|
| Overall Compliance | User input | User input | =C18-B18 |
| Maturity Level | User input | User input | =C19-B19 |
| Critical Vulns | User input | User input | =C20-B20 |

**Line Chart (Rows 27-45):**
- **Chart Type:** Line chart
- **Data Range:** B5:E12 (quarterly metrics)
- **X-Axis:** Quarters
- **Y-Axis:** Scores (%)

---

## Sheet 5: Recommendations

### Structure

**Recommendations Table (Rows 5-25):**

**Columns:**

| Col | Column Name | Width | Input Type |
|-----|-------------|-------|------------|
| A | # | 5 | Auto-number (1,2,3...) |
| B | Recommendation | 40 | Text |
| C | Current State | 30 | Text |
| D | Target State | 30 | Text |
| E | Priority | 15 | Dropdown: Priority |
| F | Effort | 12 | Dropdown: Effort |
| G | Owner | 20 | Text |
| H | Target Date | 15 | Date |

**Auto-numbering Formula (Cell A6):**
```excel
=ROW()-5
```
*Adjusts automatically when rows inserted*

**Quick Wins Section (Rows 27-32):**
User manually documents 3-5 quick wins (low effort, high impact)

**Strategic Initiatives Section (Rows 34-39):**
User manually documents 3-5 strategic initiatives (high effort, high impact)

### Conditional Formatting

**Column E (Priority):**
- "P1 (Immediate)" → Red background
- "P2 (High)" → Orange background
- "P3 (Medium)" → Yellow background
- "P4 (Low)" → Green background

**Column H (Target Date):**
- If past due (< TODAY()) → Red background
- If due soon (< TODAY()+30) → Yellow background

---

## Python Script Integration Notes

### Script Name
`generate_a825_26_29_5_compliance_dashboard.py`

### Key Functions

1. **create_workbook()**: Initialize 5 sheets
2. **populate_executive_summary()**: Create one-page summary with large fonts
3. **add_formulas()**: Add all cross-sheet references and calculations
4. **add_conditional_formatting()**: Status colors, maturity levels, trend indicators
5. **create_charts()**: Add trend line chart to Sheet 4
6. **protect_sheets()**: Lock all sheets

### Critical Notes

**Cross-Sheet References:**
- Executive Summary pulls from Control Compliance sheet
- Control Compliance pulls from user input (IMP-S1,S2,S3,S4 data)
- Maturity Assessment pulls from Control Compliance
- Verify all references work when sheets reordered

**Large Fonts for Executive Summary:**
- Overall score: 36pt
- Maturity level: 14pt
- Keep Executive Summary to ONE PAGE

**Trend Chart:**
- Auto-updates when quarterly data added
- Use professional color scheme
- Show data labels

---

## Quality Assurance Checklist

- [ ] All 5 sheets present
- [ ] Executive Summary fits on one page
- [ ] All cross-sheet formulas work
- [ ] Maturity level calculation correct
- [ ] Trend chart displays properly
- [ ] Conditional formatting applies correctly
- [ ] No #REF!, #VALUE!, #DIV/0! errors
- [ ] Test with sample data from all 4 IMP workbooks

---

**END OF PART II: TECHNICAL SPECIFICATION**
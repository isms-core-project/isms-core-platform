# ISMS-IMP-A.8.16.5 - Compliance Dashboard Specification
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.16.5  
**Assessment Area:** Overall Compliance Dashboard & Master Metrics  
**Related Policy:** All ISMS-POL-A.8.16 sections  
**Purpose:** Consolidated compliance dashboard aggregating all monitoring activity assessments  
**Generator Script:** `generate_a816_5_compliance_dashboard.py`  
**Output Filename:** `ISMS-IMP-A.8.16.5_Compliance_Dashboard_YYYYMMDD.xlsx`

---

## Workbook Structure

**Total Sheets:** 7
1. Instructions & Legend
2. Executive Summary
3. Detailed Compliance Matrix
4. Key Performance Indicators (KPIs)
5. Gap Analysis & Remediation Tracker
6. Trend Analysis
7. Evidence Register & Approvals

---

## Sheet 2: Executive Summary

### Header
**Title:** "MONITORING ACTIVITIES - EXECUTIVE SUMMARY"  
**Subtitle:** "ISO/IEC 27001:2022 Control A.8.16 Compliance Status"

### Section 1: Overall Compliance Score (Rows 3-12)

**Visual Compliance Gauge:**
```
Overall Compliance:  [XX%] ■■■■■■■■□□ 
Status:              [✅ Compliant / ⚠️ Partial / ❌ Non-Compliant]
Assessment Date:     DD.MM.YYYY
Next Review:         DD.MM.YYYY
```

**Compliance by Assessment Area:**
| Assessment | Domain | Compliance % | Status | Trend |
|------------|--------|--------------|--------|-------|
| IMP-A.8.16.1 | Infrastructure | Formula | Formula | ↑/→/↓ |
| IMP-A.8.16.2 | Baseline & Detection | Formula | Formula | ↑/→/↓ |
| IMP-A.8.16.3 | Coverage | Formula | Formula | ↑/→/↓ |
| IMP-A.8.16.4 | Alert Management | Formula | Formula | ↑/→/↓ |
| **OVERALL** | **All Domains** | **Formula** | **Formula** | **↑/→/↓** |

### Section 2: Critical Metrics Summary (Rows 16-30)

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| **Coverage Metrics** |
| Critical Systems Monitored | Formula | 100% | Formula |
| Overall System Coverage | Formula | >80% | Formula |
| Network Segment Coverage | Formula | 100% | Formula |
| **Detection Metrics** |
| Baseline Coverage (Critical) | Formula | 100% | Formula |
| Detection Rate | Formula | >90% | Formula |
| False Positive Rate | Formula | <25% | Formula |
| **Response Metrics** |
| MTTD (Critical Alerts) | Formula | <5 min | Formula |
| MTTR (Critical Incidents) | Formula | <8 hrs | Formula |
| SLA Compliance | Formula | >95% | Formula |
| **Operational Metrics** |
| Log Sources Integrated | Formula | Target | Formula |
| Active Detection Rules | Formula | Target | Formula |
| SOC Analyst Coverage | Formula | 24/7 | Formula |

### Section 3: Top 5 Strengths (Rows 34-42)
| Rank | Strength | Evidence |
|------|----------|----------|
| 1 | [Auto-populated from assessments] | [Link to evidence] |
| 2 | ... | ... |

### Section 4: Top 5 Gaps (Rows 45-53)
| Priority | Gap | Risk | Remediation Target |
|----------|-----|------|-------------------|
| Critical | [Auto-populated] | High | DD.MM.YYYY |

### Section 5: Management Recommendations (Rows 56-68)
- Investment priorities
- Resource needs
- Strategic improvements
- Compliance actions

---

## Sheet 3: Detailed Compliance Matrix

### Header
**Title:** "DETAILED COMPLIANCE MATRIX"

### Matrix Structure (Rows 3-150)

**Column Headers:**
| Col | Header | Width |
|-----|--------|-------|
| A | Policy Reference | 25 |
| B | Requirement | 40 |
| C | Control Type | 18 |
| D | Assessment Sheet | 22 |
| E | Evidence Location | 30 |
| F | Implementation Status | 20 |
| G | Compliance Status | 20 |
| H | Gap Description | 35 |
| I | Risk Level | 15 |
| J | Remediation Owner | 20 |
| K | Target Date | 14 |
| L | Notes | 25 |

**Requirements Mapped:**
- All requirements from S2.1 (Infrastructure) - ~25 requirements
- All requirements from S2.2 (Baseline & Detection) - ~30 requirements
- All requirements from S2.3 (Alert Management) - ~25 requirements
- All requirements from S2.4 (Retention) - ~15 requirements
- All requirements from S3 (Roles) - ~10 requirements
- **Total: ~105 requirement rows**

**Auto-Population from Assessment Workbooks:**
- Import compliance status from IMP-A.8.16.1 through IMP-A.8.16.4
- Aggregate to policy requirement level
- Flag gaps and non-compliance

### Compliance Scoring (Formula-driven)
```
Compliant Count: =COUNTIF(G:G,"✅ Compliant")
Partial Count: =COUNTIF(G:G,"⚠️ Partial")
Non-Compliant Count: =COUNTIF(G:G,"❌ Non-Compliant")
Overall %: =Compliant/(Compliant+Partial+Non-Compliant)*100
```

---

## Sheet 4: Key Performance Indicators (KPIs)

### Section 1: Coverage KPIs (Rows 3-20)

| KPI | Current | Target | Baseline | Trend (3mo) | Status |
|-----|---------|--------|----------|-------------|--------|
| **Asset Coverage** |
| Critical Systems Monitored % | [Input] | 100% | [Historical] | Chart | Status |
| High Priority Systems % | [Input] | >80% | [Historical] | Chart | Status |
| Overall Asset Coverage % | [Input] | >80% | [Historical] | Chart | Status |
| Network Segments Covered % | [Input] | 100% | [Historical] | Chart | Status |
| **Log Source Integration** |
| Log Sources Integrated (Count) | [Input] | Target | [Historical] | Chart | Status |
| Log Volume (GB/day) | [Input] | Capacity | [Historical] | Chart | Status |
| Log Collection Reliability % | [Input] | >99% | [Historical] | Chart | Status |

### Section 2: Detection KPIs (Rows 23-42)

| KPI | Current | Target | Baseline | Trend | Status |
|-----|---------|--------|----------|-------|--------|
| **Baseline Metrics** |
| Tier 1 Systems with Baselines % | [Input] | 100% | [Historical] | Chart | Status |
| Tier 2 Systems with Baselines % | [Input] | >80% | [Historical] | Chart | Status |
| Baseline Staleness (Avg Days Since Review) | [Input] | <90 | [Historical] | Chart | Status |
| **Detection Rule Health** |
| Active Detection Rules (Count) | [Input] | Target | [Historical] | Chart | Status |
| MITRE ATT&CK Coverage % | [Input] | >60% | [Historical] | Chart | Status |
| Detection Rate (Testing) % | [Input] | >90% | [Historical] | Chart | Status |
| False Positive Rate % | [Input] | <25% | [Historical] | Chart | Status |
| Rules Requiring Tuning (Count) | [Input] | <10 | [Historical] | Chart | Status |

### Section 3: Response KPIs (Rows 45-65)

| KPI | Current | Target | Baseline | Trend | Status |
|-----|---------|--------|----------|-------|--------|
| **Alert Metrics** |
| Total Alerts (30d) | [Input] | Target | [Historical] | Chart | Status |
| Alerts by Severity (Critical/High/Med/Low) | [Input] | Profile | [Historical] | Chart | Status |
| True Positive Rate % | [Input] | >20% | [Historical] | Chart | Status |
| Alert-to-Incident Ratio | [Input] | Target | [Historical] | Chart | Status |
| **Response Time Metrics** |
| MTTA - Critical (minutes) | [Input] | <15 | [Historical] | Chart | Status |
| MTTT - Critical (minutes) | [Input] | <60 | [Historical] | Chart | Status |
| MTTI - Critical (hours) | [Input] | <4 | [Historical] | Chart | Status |
| MTTR - Critical (hours) | [Input] | <8 | [Historical] | Chart | Status |
| SLA Compliance Rate % | [Input] | >95% | [Historical] | Chart | Status |
| **Escalation Metrics** |
| Escalation Rate % | [Input] | Target | [Historical] | Chart | Status |
| False Escalation Rate % | [Input] | <10% | [Historical] | Chart | Status |

### Section 4: Operational KPIs (Rows 68-85)

| KPI | Current | Target | Baseline | Trend | Status |
|-----|---------|--------|----------|-------|--------|
| **SOC Operations** |
| SOC Analyst Count | [Input] | Target | [Historical] | Chart | Status |
| Alerts per Analyst per Shift | [Input] | <50 | [Historical] | Chart | Status |
| SOC Coverage Model | [Input] | 24/7 | N/A | N/A | Status |
| Training Completion % | [Input] | 100% | [Historical] | Chart | Status |
| **Infrastructure Health** |
| SIEM Availability % | [Input] | >99.5% | [Historical] | Chart | Status |
| Search Performance (seconds) | [Input] | <10 | [Historical] | Chart | Status |
| Storage Utilization % | [Input] | <80% | [Historical] | Chart | Status |
| Indexing Lag (minutes) | [Input] | <5 | [Historical] | Chart | Status |

---

## Sheet 5: Gap Analysis & Remediation Tracker

### Section 1: Gap Inventory (Rows 3-60)

| Gap ID | Source Assessment | Gap Category | Description | Risk | Impact | Remediation Plan | Owner | Target Date | Budget | Status | % Complete | Last Updated |
|--------|-------------------|--------------|-------------|------|--------|------------------|-------|-------------|--------|--------|------------|--------------|
| [Auto-populated from IMP-A.8.16.1-4] | | | | | | | | | | | | |

**Gap Categories:**
- Infrastructure Gap
- Baseline Gap
- Coverage Gap
- Detection Gap
- Alert Management Gap
- Process Gap
- Resource Gap

### Section 2: Gap Summary by Category (Rows 63-75)
| Category | Total | Critical | High | Medium | Low | Open | In Progress | Resolved |
|----------|-------|----------|------|--------|-----|------|-------------|----------|
| Infrastructure | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| Baseline & Detection | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| Coverage | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| Alert Management | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| **TOTAL** | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |

### Section 3: Remediation Timeline (Rows 78-95)
- Gantt chart style timeline
- Gaps by month
- Critical path items highlighted
- Resource allocation

### Section 4: Risk Heat Map (Rows 98-110)
```
                Impact
            Low  Med  High
Likelihood:
High        [Count gaps by quadrant]
Med         
Low         
```

---

## Sheet 6: Trend Analysis

### Section 1: Compliance Trend (Rows 3-18)
**Monthly compliance % over 12 months**
| Month | Overall % | Infrastructure % | Baseline % | Coverage % | Alert Mgmt % |
|-------|-----------|------------------|------------|-----------|--------------|
| Jan 2025 | [Historical] | ... | ... | ... | ... |
| ... | | | | | |
| Dec 2025 | [Current] | ... | ... | ... | ... |

**Line chart showing trends**

### Section 2: KPI Trends (Rows 21-45)
**Key metrics over time (12 months):**
- Critical system coverage %
- Detection rate %
- False positive rate %
- MTTD (Critical)
- MTTR (Critical)
- SLA compliance %

### Section 3: Gap Closure Rate (Rows 48-60)
**Monthly gap remediation tracking:**
| Month | New Gaps | Closed Gaps | Net Change | Total Open |
|-------|----------|-------------|------------|------------|
| ... | | | | |

### Section 4: Incident Detection Effectiveness (Rows 63-75)
**Quarterly analysis:**
| Quarter | Incidents Detected by Monitoring | Incidents Missed | Detection Rate % | Lessons Learned |
|---------|----------------------------------|------------------|------------------|-----------------|
| ... | | | | |

---

## Sheet 7: Evidence Register & Approvals

### Section 1: Evidence Register (Rows 3-102)
**100 rows for evidence tracking**

| Evidence ID | Evidence Type | Description | Related Requirement | Source Assessment | Date Collected | Collected By | Location/Link | Verification Status | Verified By | Verification Date | Notes |
|-------------|---------------|-------------|-------------------|-------------------|----------------|--------------|---------------|-------------------|-------------|------------------|-------|

### Section 2: Approval Workflow (Rows 105-130)

**Assessment Prepared By:**
- Name: [Input]
- Title: [Input]
- Date: [Input]
- Signature: [Space for signature]

**Reviewed By (SOC Lead):**
- Name: [Input]
- Title: [Input]
- Review Comments: [Multi-line text]
- Date: [Input]
- Signature: [Space]

**Reviewed By (Security Engineering):**
- Name: [Input]
- Title: [Input]
- Review Comments: [Multi-line text]
- Date: [Input]
- Signature: [Space]

**Approved By (CISO):**
- Name: [Input]
- Title: [Input]
- Approval Decision: [Dropdown: Approved, Approved with Conditions, Rejected]
- Conditions/Comments: [Multi-line text]
- Date: [Input]
- Signature: [Space]

**Executive Acknowledgment (Optional):**
- Name: [Input]
- Title: [Input]
- Date: [Input]
- Signature: [Space]

---

## Data Import Instructions

**This workbook is designed to aggregate data from:**
- ISMS-IMP-A.8.16.1_Monitoring_Infrastructure_YYYYMMDD.xlsx
- ISMS-IMP-A.8.16.2_Baseline_Detection_YYYYMMDD.xlsx
- ISMS-IMP-A.8.16.3_Coverage_Assessment_YYYYMMDD.xlsx
- ISMS-IMP-A.8.16.4_Alert_Management_YYYYMMDD.xlsx

**Import Method:**
1. Manual copy-paste from Summary Dashboards
2. Excel Power Query (recommended for automation)
3. Python script to aggregate (advanced)

**Formula References:**
- Use INDIRECT() for dynamic workbook references
- Use INDEX/MATCH for lookups across workbooks
- Implement data validation to prevent manual errors

---

**END OF SPECIFICATION**
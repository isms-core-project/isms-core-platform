<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.7.4-UG:framework:UG:a.5.7.4 -->
**ISMS-IMP-A.5.7.4-UG - Threat Intelligence Effectiveness Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.4-UG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Program Effectiveness Dashboard with Automated Data Refresh |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements), Section 3.2 (Exception Management), Section 3.4 (Policy Governance) |
| **Purpose** | Provide executive and management-level visibility into threat intelligence program effectiveness by aggregating data from all A.5.7 workbooks |
| **Target Audience** | CISO, Security Managers, Executive Management, Board, Auditors |
| **Assessment Type** | Aggregated Dashboard |
| **Review Cycle** | Monthly (data refresh), Quarterly (full review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification (12 sheets) | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.7.4-TG.

---

## Dashboard Overview

### Purpose & Scope

**Dashboard Name:** ISMS-IMP-A.5.7.4 - Threat Intelligence Effectiveness Dashboard

#### What This Dashboard Provides

This dashboard **CONSOLIDATES** data from all operational Control A.5.7 workbooks into a single executive view. It answers:

- How effective is our threat intelligence program overall?
- Are we meeting policy targets across all KPIs?
- What trends are emerging (month-over-month, quarter-over-quarter)?
- Where are the program gaps requiring attention?
- **CRITICAL**: What prevented incidents demonstrate program value? (from A.5.7.3)
- **CRITICAL**: What intelligence-driven decisions show executive engagement? (from A.5.7.3)
- What is our audit evidence status?

#### Key Principle

This is an **AUTOMATED AGGREGATION DASHBOARD**. It uses Excel external references to pull data from:

- ISMS-IMP-A.5.7.1 (Sources Assessment)
- ISMS-IMP-A.5.7.2 (Collection & Analysis Assessment)
- ISMS-IMP-A.5.7.3 (Integration & Distribution Assessment)

**Data flows automatically when source workbooks are updated and this dashboard is refreshed.**

#### What You'll Document

**Automated (External References):**

- Program KPIs from all three assessments
- Source portfolio metrics
- Intelligence operations metrics
- Integration status metrics
- Stakeholder engagement metrics
- **Prevention tracking** (from A.5.7.3 Sheet 7)
- **Risk assessment updates** (from A.5.7.3 Sheet 13)
- **Incident-TI integration** (from A.5.7.3 Sheet 14)
- **Intelligence-driven decisions** (from A.5.7.3 Sheet 15)

**Manual Entry:**

- Risk indicators (program health warnings)
- Executive comments/notes
- Action item priorities
- Approval signatures

#### Target Audience & Usage

| Audience | Primary Use Case | Frequency |
|----------|-----------------|-----------|
| **CISO** | Program oversight, KPI tracking | Weekly |
| **Security Managers** | Operational effectiveness, gap identification | Bi-weekly |
| **Executive Management** | Strategic value demonstration, investment justification | Monthly |
| **Board** | Risk posture, program maturity, prevented incidents | Quarterly |
| **Auditors** | Compliance evidence, effectiveness measurement | Annual + quarterly |

---

## Prerequisites

### Source Workbooks Required (DEPENDENCIES)

**This dashboard CANNOT function without:**

1. ✅ **ISMS-IMP-A.5.7.1** - Sources Assessment workbook (current version)
2. ✅ **ISMS-IMP-A.5.7.2** - Collection & Analysis Assessment workbook (current version)
3. ✅ **ISMS-IMP-A.5.7.3** - Integration & Distribution Assessment workbook (current version)

**File Location Requirements:**

- All three source workbooks must be in same directory as dashboard OR
- Update external reference paths to correct locations

**Version Requirements:**

- Source workbooks must be current (within 30 days for monthly reporting)
- Quarterly reviews require source workbooks updated within quarter

### Information You'll Need

- Access to all three source workbooks
- Understanding of external references in Excel (how to refresh)
- Executive feedback on program performance
- Risk assessment for program health indicators

### Required Tools

- Microsoft Excel (2016 or later) with external data connections enabled
- File system access to source workbooks
- Screen capture tools for executive summary export (PDF/PowerPoint)

---

## Workflow

### High-Level Process

```
MONTHLY CYCLE:
1. Update Source Workbooks (A.5.7.1, A.5.7.2, A.5.7.3)
2. Open Dashboard (A.5.7.4)
3. Refresh External Data Connections
4. Review Auto-Populated Metrics
5. Update Risk Indicators (manual)
6. Generate Monthly Report (Sheet 10)
7. CISO Review & Approval

QUARTERLY CYCLE:
1. Complete Monthly Cycle Steps
2. Review Trends (Sheet 7)
3. Review Compliance Evidence (Sheet 9)
4. Generate Quarterly Report (Sheet 11)
5. Prepare Board Package
6. Executive/Board Presentation
7. Executive Approval
```

### Monthly Reporting Process (2-3 hours)

**Step 1: Update Source Workbooks (Week 1 of month)**

- Complete monthly updates to A.5.7.1 (if source changes occurred)
- Complete monthly updates to A.5.7.2 (intelligence production, VTL records, campaigns)
- Complete monthly updates to A.5.7.3 (IOC deployment, distribution tracking)
- **CRITICAL**: Ensure A.5.7.3 Sheet 7 (Prevention) updated with any incidents prevented
- Save all source workbooks

**Step 2: Open Dashboard & Refresh Data (Week 1 of month)**
1. Open ISMS-IMP-A.5.7.4 dashboard workbook
2. Excel will prompt: "This workbook contains links to other data sources"
3. Click **"Update"** to refresh all external references
4. Verify no broken references (#REF! errors)
5. If broken references: Fix file paths in Formulas → Edit Links

**Step 3: Review Auto-Populated Metrics (Week 1 of month)**

- **Sheet 1: Executive_Summary** - Verify all metrics populated
- **Sheet 2: Program_KPIs** - Verify calculations correct
- **Sheet 3: Source_Portfolio** - Verify source counts accurate
- **Sheet 4: Intelligence_Operations** - Verify production metrics
- **Sheet 5: Integration_Status** - Verify tool integration data
- **Sheet 6: Stakeholder_Engagement** - Verify distribution metrics

**Step 4: Update Risk Indicators (Week 1 of month)**

- **Sheet 8: Risk_Indicators** - Manual entry required
  * Identify any program health warnings (KPIs below target, critical gaps, resource constraints)
  * Document risk indicator severity (Critical, High, Medium, Low)
  * Document mitigation actions
  * Update risk indicator status

**Step 5: Generate Monthly Report (Week 2 of month)**

- **Sheet 10: Monthly_Report** - Auto-generated from other sheets
  * Review report completeness
  * Add executive commentary (manual text box or comments)
  * Export to PDF for distribution
  * Distribute to CISO, Security Managers

**Step 6: CISO Review & Approval (Week 2 of month)**

- CISO reviews dashboard and monthly report
- CISO provides feedback or approval
- Document approval in metadata

**Deliverable:** Monthly dashboard with current data, monthly report distributed

---

### Quarterly Reporting Process (4-6 hours)

**Step 1-6: Complete Monthly Reporting Process**

**Step 7: Review Quarterly Trends (Week 1 of quarter-end month)**

- **Sheet 7: Trend_Analysis**
  * Review 3-month trends for all KPIs
  * Identify improving vs. declining metrics
  * Document trend analysis commentary
  * Highlight significant changes for executive attention

**Step 8: Review Compliance Evidence (Week 1 of quarter-end month)**

- **Sheet 9: Compliance_Evidence**
  * Verify all MANDATORY audit evidence present:
    - Prevention tracking (A.5.7.3 Sheet 7): ≥3 per quarter
    - Risk assessment updates (A.5.7.3 Sheet 13): ≥3 per quarter
    - Incident-TI integration (A.5.7.3 Sheet 14): ≥70% P1/P2
    - Intelligence-driven decisions (A.5.7.3 Sheet 15): ≥5 per quarter
  * Document compliance status (Met, Not Met, Partial)
  * Prepare evidence package for auditors

**Step 9: Generate Quarterly Report (Week 2 of quarter-end month)**

- **Sheet 11: Quarterly_Report**
  * Auto-generated summary of quarter
  * Quarter-over-quarter comparison
  * Key achievements highlighted
  * Gaps and action items documented
  * Export to PDF/PowerPoint for board

**Step 10: Prepare Board Package (Week 2-3 of quarter-end month)**

- Create board-ready presentation from quarterly report
- Include:
  * Executive summary (1 slide)
  * Prevented incidents (demonstrates value)
  * Intelligence-driven decisions (shows executive engagement)
  * Program maturity trends
  * Key risks and mitigations
  * Budget/resource requests (if applicable)

**Step 11: Executive/Board Presentation (Quarter-end)**

- Present quarterly results to executive team or board
- Gather feedback
- Document decisions or approvals
- Update dashboard with feedback

**Step 12: Executive Approval (Quarter-end)**

- Executive or board approves quarterly report
- Document approval in metadata
- Archive quarterly report and evidence package

**Deliverable:** Quarterly report approved, board presentation delivered, compliance evidence package ready for audit

---

## Evidence Package for Audits

### What Auditors Need from This Dashboard

**Audit Objective:** Verify threat intelligence program effectiveness and compliance with policy requirements

**Evidence Required:**

1. **Program KPIs (Sheet 2):**

   - Quarterly snapshots showing KPI tracking
   - Evidence of targets met or gaps addressed
   - Trend analysis showing continuous improvement

2. **Compliance Evidence (Sheet 9):**

   - **CRITICAL**: Prevention tracking summary (≥3 per quarter)
   - **CRITICAL**: Risk assessment updates summary (≥3 per quarter - ISO 27001 Clause 6.1)
   - **CRITICAL**: Incident-TI integration summary (≥70% P1/P2 - Controls A.5.24-5.28)
   - **CRITICAL**: Intelligence-driven decisions summary (≥5 per quarter)
   - Links to detailed evidence in source workbooks (A.5.7.1, A.5.7.2, A.5.7.3)

3. **Monthly Reports (Sheet 10):**

   - Monthly reports for entire audit period (typically 12 months)
   - CISO approval documented

4. **Quarterly Reports (Sheet 11):**

   - Quarterly reports for audit period
   - Executive/board approval documented

5. **Risk Indicators (Sheet 8):**

   - Program health tracking
   - Risk mitigation actions documented and completed

**How to Prepare for Audit:**

1. **3 Months Before Audit:**

   - Review all quarterly reports for completeness
   - Ensure all MANDATORY evidence present (Sheets 7, 13, 14, 15 from A.5.7.3)
   - Fill any evidence gaps

2. **1 Month Before Audit:**

   - Generate compliance evidence package (from Sheet 9)
   - Create audit evidence index (what's where)
   - Export key sheets to PDF for auditor review

3. **During Audit:**

   - Provide dashboard (Sheet 1: Executive_Summary) as program overview
   - Walk through Sheet 9 (Compliance_Evidence) showing MANDATORY requirements met
   - Drill into source workbooks for detailed evidence
   - Demonstrate data flow (external references showing real operational data)

**Audit Success Criteria:**

- ✓ All MANDATORY quarterly targets met (Sheets 7, 13, 14, 15 from A.5.7.3)
- ✓ Monthly and quarterly reporting consistent throughout audit period
- ✓ KPI targets from policy met or gaps documented with action items
- ✓ CISO/Executive approvals documented
- ✓ Traceability from policy requirements → dashboard → source workbooks

---

## Review & Approval

### Monthly Review

**Level 1: CISO**

- Reviews monthly dashboard and report
- Verifies KPIs against targets
- Approves monthly report for distribution
- Timeline: Within 5 business days of month-end

### Quarterly Review

**Level 1: CISO**

- Reviews quarterly dashboard and report
- Verifies compliance evidence complete
- Reviews trend analysis
- Prepares for executive/board presentation

**Level 2: Executive Management / Board**

- Reviews quarterly report and dashboard summary
- Reviews prevented incidents (demonstrates value)
- Reviews intelligence-driven decisions (shows engagement)
- Approves program continuation or directs changes
- Timeline: Within 15 business days of quarter-end

**Approval Documentation:**

- Monthly: CISO signature in Sheet 10 (Monthly_Report)
- Quarterly: Executive/Board signature in Sheet 11 (Quarterly_Report)

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->

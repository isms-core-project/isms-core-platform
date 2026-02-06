**ISMS-IMP-A.5.1-2-6.1-2.S5-TG - Governance Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.1, A.5.2, A.6.1, A.6.2: Stacked Control Consolidation

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Governance Compliance Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S5-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.1, A.5.2, A.6.1, A.6.2 (Stacked Control Consolidation) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle:** Quarterly (aligned with source assessments)
**Next Review Date:** [Effective Date + 90 days]

**Source Assessments (MANDATORY prerequisites — all must be approved before this dashboard is populated):**
- ISMS-IMP-A.5.1-2-6.1-2.S1 — Policy Framework Assessment (Control A.5.1)
- ISMS-IMP-A.5.1-2-6.1-2.S2 — Roles & Responsibilities Assessment (Control A.5.2)
- ISMS-IMP-A.5.1-2-6.1-2.S3 — Screening & Vetting Assessment (Control A.6.1)
- ISMS-IMP-A.5.1-2-6.1-2.S4 — Employment Contract Assessment (Controls A.6.2, A.6.5)

**Related Documents:**
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles)
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.12 (Data Leakage Prevention) — monitoring transparency context
- Swiss Federal Data Protection Act (FADP / nDSG) — Articles 6, 19, 22
- ISO/IEC 27001:2022 Clause 9.3 (Management Review)

---

# Technical Specification

**Audience:** Workbook Developers (Python/Excel script maintainers)

---

## 1. Workbook Structure Overview

**Total Sheets:** 11

| Sheet # | Sheet Name | Purpose | User Input? | External Links? |
|---------|-----------|---------|-------------|-----------------|
| 1 | Instructions_Legend | Guidance, color legend, navigation | No | No |
| 2 | Executive_Summary | Board-facing single-page summary | Yes (narrative) | Yes |
| 3 | Maturity_Assessment | 5-level maturity model + trend | Yes (prev. quarter) | Yes |
| 4 | Policy_Summary | S1 (A.5.1) domain metrics | No | Yes |
| 5 | Roles_Summary | S2 (A.5.2) domain metrics | No | Yes |
| 6 | Screening_Summary | S3 (A.6.1) domain metrics + FADP | No | Yes |
| 7 | Contract_Summary | S4 (A.6.2/A.6.5) domain metrics + NDA | No | Yes |
| 8 | Gap_Analysis | Consolidated gaps with cross-domain flags | Yes (status updates) | Yes |
| 9 | Evidence_Register | Consolidated evidence index | No | Yes |
| 10 | Action_Items | Remediation tracker | Yes | No |
| 11 | Approval_Sign_Off | Three-level governance certification | Yes | No |

---

## 2. Source Workbook Schema

**Critical:** Document the actual cell locations in each source workbook before building formulas.

| Source | Workbook File | Key Metrics Cell Locations |
|--------|---------------|---------------------------|
| S1 | ISMS-IMP-A.5.1-2-6.1-2.S1.xlsx | Policy_Inventory total, Lifecycle compliance %, Governance gaps, Communication rate |
| S2 | ISMS-IMP-A.5.1-2-6.1-2.S2.xlsx | Role count, Fill rate, RACI coverage %, Training completion %, Competency gaps |
| S3 | ISMS-IMP-A.5.1-2-6.1-2.S3.xlsx | Screening completion rate, FADP consent status, DPIA status, Overdue count |
| S4 | ISMS-IMP-A.5.1-2-6.1-2.S4.xlsx | Template compliance rate, NDA rate, Post-employment status, DPA coverage |

---

## 3. External Workbook Link Management

**Implementation:** Relative file paths (source workbooks in same directory as dashboard)

```python
# Relative link formula pattern
link_formula = f"='[{filename}]{sheet_name}'!${col}${row}"

# Example: S1 total policies
s1_total = "='[ISMS-IMP-A.5.1-2-6.1-2.S1.xlsx]Policy_Inventory'!$D$4"

# Example: S4 NDA compliance rate
s4_nda = "='[ISMS-IMP-A.5.1-2-6.1-2.S4.xlsx]NDA_Tracking'!$H$106"
```

**File Normalization Script (inline):**
```python
import shutil, glob

# Auto-normalize long-name workbooks to short names
patterns = {
    'S1': 'ISMS-IMP-A.5.1-2-6.1-2.S1.xlsx',
    'S2': 'ISMS-IMP-A.5.1-2-6.1-2.S2.xlsx',
    'S3': 'ISMS-IMP-A.5.1-2-6.1-2.S3.xlsx',
    'S4': 'ISMS-IMP-A.5.1-2-6.1-2.S4.xlsx'
}

for key, short_name in patterns.items():
    matches = glob.glob(f'ISMS-IMP-A.5.1-2-6.1-2.{key}_*_*.xlsx')
    if matches and not os.path.exists(short_name):
        shutil.copy(matches[0], short_name)
        print(f"Normalized: {matches[0]} → {short_name}")
```

---

## 4. Sheet 1: Instructions_Legend

### Layout

**Title Block (Rows 1–3):**
- Row 1 (merged A1:L1): "ISMS-IMP-A.5.1-2-6.1-2.S5 — GOVERNANCE COMPLIANCE DASHBOARD"
- Row 2 (merged A2:L2): "Stacked Control Consolidation | ISO/IEC 27001:2022 Controls A.5.1, A.5.2, A.6.1, A.6.2"
- Row 3 (merged A3:L3): "Consolidation Dashboard — Read from S1–S4 source workbooks"
- Font: Arial 14pt Bold White (Row 1), Arial 11pt White (Rows 2–3)
- Background: Dark Blue (003366)

**Document Control Block (Rows 5–18):**

| Row | Label (Col A) | Value (Col B–C) |
|-----|---------------|-----------------|
| 5 | Dashboard ID: | ISMS-IMP-A.5.1-2-6.1-2.S5 |
| 6 | Controls Covered: | A.5.1, A.5.2, A.6.1, A.6.2, A.6.5 |
| 7 | Parent Policy: | ISMS-POL-A.5.1-2-6.1-2 |
| 8 | Generated Date: | [USER INPUT — date picker] |
| 9 | Generated By: | [USER INPUT] |
| 10 | Organization: | [USER INPUT] |
| 11 | Version: | 1.0 |
| 12 | Classification: | Internal |
| 13 | Source S1 Date: | [USER INPUT — date of S1 workbook] |
| 14 | Source S2 Date: | [USER INPUT — date of S2 workbook] |
| 15 | Source S3 Date: | [USER INPUT — date of S3 workbook] |
| 16 | Source S4 Date: | [USER INPUT — date of S4 workbook] |
| 17 | Data Freshness: | [Formula: =IF(MIN(S1date,S2date,S3date,S4date)<TODAY()-90,"⚠️ STALE DATA","✅ Current")] |
| 18 | Next Dashboard: | [Formula: Generated Date + 90 days] |

**Color Legend, Dropdown Reference, Navigation Guide:** Same structure as S1–S4 Instructions sheets.

---

## 5. Sheet 2: Executive_Summary

### Purpose
Board-facing single-page summary. All content within the print area must fit one page.

### Layout

**Classification Banner (Row 1):**
- Merged A1:I1: "INTERNAL — GOVERNANCE CERTIFICATION DASHBOARD"
- Background: Dark Blue (003366), White text, Arial 12pt Bold

**Header (Row 3):**
- Merged A3:I3: "SECURE EMPLOYMENT & ROLES — EXECUTIVE COMPLIANCE SUMMARY"
- Background: Blue (0070C0), White text, Arial 14pt Bold

**KPI Block (Rows 5–12):**

| Cell | Label | Value | Notes |
|------|-------|-------|-------|
| A5 | WEIGHTED COMPLIANCE SCORE | [Formula — see below] | Large font (22pt), traffic-light color |
| E5 | OVERALL STATUS | [Formula — Green/Yellow/Orange/Red] | Traffic-light indicator |
| A7 | Assessment Period: | [USER INPUT] | |
| E7 | Certification Status: | [Formula from Sheet 11] | |
| A9 | Critical Gaps: | [Formula] | Red if >0 |
| C9 | High Gaps: | [Formula] | Orange if >0 |
| E9 | NDA Compliance: | [Formula from S4] | Audit focal point — Bold |
| A11 | FADP Status: | [Formula from S3] | ✅ Compliant / ⚠️ Review Required |

**Weighted Score Formula (Cell B5):**
```excel
=(('[ISMS-IMP-A.5.1-2-6.1-2.S1.xlsx]...'!$compliance_pct * 0.35)
+ ('[ISMS-IMP-A.5.1-2-6.1-2.S2.xlsx]...'!$compliance_pct * 0.25)
+ ('[ISMS-IMP-A.5.1-2-6.1-2.S3.xlsx]...'!$compliance_pct * 0.20)
+ ('[ISMS-IMP-A.5.1-2-6.1-2.S4.xlsx]...'!$compliance_pct * 0.20))
```

**Compliance By Domain (Rows 14–20):**

| Column | Header | Width |
|--------|--------|-------|
| A | Domain | 28 |
| B | Control | 14 |
| C | Weight | 10 |
| D | Compliance % | 14 |
| E | Status | 12 |
| F | Key Metric | 30 |
| G | Trend | 10 |

| Row | Domain | Control | Weight | Compliance % | Key Metric |
|-----|--------|---------|--------|--------------|------------|
| 16 | Policy Framework | A.5.1 | 35% | [Link to S1] | Lifecycle compliance rate |
| 17 | Roles & Responsibilities | A.5.2 | 25% | [Link to S2] | RACI coverage rate |
| 18 | Screening & Vetting | A.6.1 | 20% | [Link to S3] | Screening completion rate |
| 19 | Employment Terms | A.6.2 | 20% | [Link to S4] | NDA compliance rate |
| 20 | **TOTAL** | — | 100% | **[Weighted formula]** | — |

**Trend Column (G):**
- Data Validation: ↑ / → / ↓
- Conditional Formatting: ↑ Green, → Yellow, ↓ Red
- User input: compare to previous quarter

**Top 3 Gaps (Rows 23–28):**

| Column | Header |
|--------|--------|
| A | # |
| B | Gap Description |
| C | Domain |
| D | Risk Level |
| E | Owner |
| F | Target Date |

Populated by formula referencing Sheet 8 (Gap_Analysis), sorted by risk level descending.

**Executive Narrative (Rows 30–40):**
- Merged A30:I30: "CISO COMMENTARY" header (Dark Blue)
- Rows 31–40: USER INPUT — free text area for CISO narrative
- Light Yellow background, Arial 10pt
- Placeholder text: *"[CISO to complete: Key findings, risk acceptance rationale, remediation priorities]"*

---

## 6. Sheet 3: Maturity_Assessment

### Purpose
Maps compliance posture to a 5-level maturity model. Provides trend tracking across quarters.

### Layout

**Header (Rows 1–2):**
- Row 1 (merged A1:H1): "MATURITY ASSESSMENT"
- Row 2 (merged A2:H2): "Personnel Security Control Framework Maturity Level"

**Maturity Model Reference (Rows 4–10):**

| Row | Level | Label | Description |
|-----|-------|-------|-------------|
| 4 | 1 | Initial | No documented policies. Screening informal. Contracts lack security clauses. |
| 5 | 2 | Developing | Policies exist but lifecycle gaps. Roles informal. Screening inconsistent. |
| 6 | 3 | Defined | All controls documented. Roles assigned. Screening performed. Contracts in place. Repeatable. |
| 7 | 4 | Managed | All controls measured. Gaps tracked and remediated on schedule. Evidence complete. |
| 8 | 5 | Optimized | Continuous improvement. Lessons learned feed policy. Automated monitoring. |

**Current Assessment (Rows 13–20):**

| Cell | Label | Value |
|------|-------|-------|
| A13 | Current Maturity Level: | [USER INPUT — Dropdown 1–5] |
| C13 | Weighted Compliance Score: | [Formula — link to Sheet 2] |
| A15 | Previous Quarter Level: | [USER INPUT — Dropdown 1–5] |
| C15 | Previous Quarter Score: | [USER INPUT — number] |
| A17 | Trend: | [Formula: IF(current>previous,"↑ Improving",IF(current=previous,"→ Stable","↓ Declining"))] |
| A19 | Maturity Justification: | [USER INPUT — free text] |

**Maturity Indicators (Rows 23–35):**

Checklist of indicators that support each maturity level. User confirms which indicators are met:

| Row | Indicator | Met? | Required For |
|-----|-----------|------|--------------|
| 23 | Information security policies documented and approved | [Dropdown] | Level 2+ |
| 24 | Security roles formally defined and assigned | [Dropdown] | Level 2+ |
| 25 | Pre-employment screening performed for all roles | [Dropdown] | Level 3+ |
| 26 | Employment contracts contain required security clauses | [Dropdown] | Level 3+ |
| 27 | Policy lifecycle (review, approval) is repeatable | [Dropdown] | Level 3+ |
| 28 | All gaps tracked with owners and target dates | [Dropdown] | Level 4+ |
| 29 | Evidence collection is systematic and complete | [Dropdown] | Level 4+ |
| 30 | Remediation is on schedule (>80% of High gaps addressed) | [Dropdown] | Level 4+ |
| 31 | Lessons learned from incidents/audits feed back into policies | [Dropdown] | Level 5+ |
| 32 | Screening and contract processes have automated elements | [Dropdown] | Level 5+ |
| 33 | Continuous monitoring of personnel security posture | [Dropdown] | Level 5+ |

**Conditional Formatting:** Indicator rows highlighted green if Met = "✅ Yes", gray if "❌ No".

---

## 7. Sheet 4: Policy_Summary (S1 — A.5.1)

### Purpose
Domain summary for the Policy Framework assessment. All data links to S1 source workbook.

### Layout

**Header (Rows 1–2):**
- Row 1 (merged A1:F1): "POLICY FRAMEWORK SUMMARY — A.5.1"
- Row 2 (merged A2:F2): "Source: ISMS-IMP-A.5.1-2-6.1-2.S1"
- Background: Dark Blue (003366)

**KPI Cards (Rows 4–12):**

| Cell | KPI Label | Formula / Link |
|------|-----------|----------------|
| A4 | Total Policies | Link to S1 Policy_Inventory total |
| C4 | Active | Link to S1 Active count |
| E4 | Lifecycle Compliance % | Calculated: (Approved + Current Reviews) / Total |
| A7 | Governance Gaps | Link to S1 Governance_Assessment gap count |
| C7 | Acknowledgment Rate | Link to S1 Communication_Tracking overall rate |
| E7 | Domain Compliance % | Weighted average of lifecycle + governance + communication |

**Detail Table (Rows 14–40):**

Per-policy summary with:
- Policy ID and Title
- Status (Active / Under Review / etc.)
- Lifecycle status (Approved ✅ / Overdue ⚠️ / Not Approved ❌)
- Governance status
- Acknowledgment rate %

All cells link to S1 source workbook.

**Source Workbook Link (Row 42):**
- "Full assessment: [link to ISMS-IMP-A.5.1-2-6.1-2.S1.xlsx]"

---

## 8. Sheet 5: Roles_Summary (S2 — A.5.2)

### Structure
Same pattern as Sheet 4, adapted for S2 metrics.

**KPIs:**

| KPI | Source |
|-----|--------|
| Total Security Roles | S2 Role_Registry |
| Filled / Vacant | S2 Role_Registry |
| RACI Coverage % | S2 RACI_Matrix |
| Training Completion % | S2 Training_Tracking |
| Competency Gaps | S2 Competency_Assessment |
| Domain Compliance % | Weighted average |

---

## 9. Sheet 6: Screening_Summary (S3 — A.6.1)

### Structure
Same pattern as Sheet 4, with additional FADP compliance section.

**KPIs:**

| KPI | Source |
|-----|--------|
| Screening Completion Rate | S3 summary |
| Overdue Screenings | S3 summary |
| FADP Consent Status | S3 Legal_Compliance |
| DPIA Status | S3 Legal_Compliance |
| Sensitive Data Flag | S3 Legal_Compliance |
| Domain Compliance % | Weighted average |

**FADP Compliance Block (Rows 35–45):**

| Cell | Label | Value |
|------|-------|-------|
| A35 | FADP COMPLIANCE INDICATOR | — |
| A37 | Criminal Record Processing? | [Link to S3] — Yes / No |
| A38 | Consent Records Complete? | [Link to S3] — ✅ / ❌ |
| A39 | DPIA Performed? | [Link to S3] — ✅ / ❌ / N/A |
| A40 | Overall FADP Status | [Formula: IF all required items ✅, "✅ Compliant", "⚠️ Review Required"] |

- FADP block header: Orange background (FFC000) if status = "⚠️ Review Required"
- FADP block header: Green background (C6EFCE) if status = "✅ Compliant"

---

## 10. Sheet 7: Contract_Summary (S4 — A.6.2 + A.6.5)

### Structure
Same pattern as Sheet 4, with NDA focal point and post-employment section.

**KPIs:**

| KPI | Source |
|-----|--------|
| Template Compliance Rate | S4 Contract_Template summary |
| **NDA Compliance Rate** | S4 NDA_Tracking summary — **Bold, highlighted** |
| Post-Employment Obligation Status | S4 Post_Employment summary |
| Contractor/Vendor DPA Coverage | S4 Contractor_Vendor_DPA summary |
| Outstanding Departures | S4 Post_Employment — exits without completion |
| Domain Compliance % | Weighted average |

**NDA Focal Point Block (Rows 14–18):**
- NDA compliance rate displayed in large font (16pt, Bold)
- If NDA rate < 95%: Red border, warning text "⚠️ NDA compliance below audit threshold"
- If NDA rate ≥ 95%: Green border, "✅ NDA compliance meets audit threshold"

**Post-Employment Block (Rows 35–45):**

| Cell | Label | Value |
|------|-------|-------|
| A35 | POST-EMPLOYMENT OBLIGATIONS | — |
| A37 | Total Departures (24 months) | [Link to S4] |
| A38 | Exit Procedures Completed | [Link to S4] |
| A39 | Outstanding Exits | [Link to S4] — Red if >0 |
| A40 | Post-Employment Obligation Tracking | [Link to S4] — % with obligations documented |

---

## 11. Sheet 8: Gap_Analysis (Consolidated)

### Purpose
Single consolidated register of all gaps from S1–S4. Adds cross-domain gap identification.

All gaps from S1–S4 consolidated, deduplicated, and prioritized.

**Structure:** 80 gap rows (rows 5–84), 14 columns (A–N).

**Columns:**

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Consolidated_Gap_ID | Text | Auto-generated: CGAP-001 through CGAP-080 |
| B | Source_Assessment | Dropdown | S1 / S2 / S3 / S4 |
| C | Source_Gap_ID | Text | Original Gap ID from the source assessment |
| D | Gap_Category | Dropdown | Policy / Role / Screening / Contract / Legal / Cross-Domain |
| E | Gap_Description | Text | From source assessment |
| F | Risk_Level | Dropdown | Critical / High / Medium / Low |
| G | Risk_Justification | Text | Why this risk level was assigned |
| H | Remediation_Action | Text | Specific action required |
| I | Owner | Text | Person/team responsible |
| J | Target_Date | Date | When remediation must be complete |
| K | Status | Dropdown | Not-Started / In-Progress / Blocked / Completed / Accepted-Risk |
| L | Priority_Rank | Text | Auto-calculated: 1–80 based on risk level and source |
| M | Dependencies | Text | What must happen first |
| N | Notes | Text | Free text |

**Priority Ranking Logic:**
All Critical gaps ranked first (by source assessment order S3 > S4 > S2 > S1), then High, then Medium, then Low. Within the same risk level, screening gaps (S3) are ranked before contract gaps (S4), then roles (S2), then policy (S1) — reflecting the operational impact hierarchy.

**Cross-Domain Gap Identification:**
Some gaps span multiple assessments. Examples:
- "Role tier changed in S2 but screening level not updated in S3" — Cross-Domain gap
- "Contract template missing clause that corresponds to policy requirement in S1" — Cross-Domain gap

These are flagged with Gap_Category = "Cross-Domain" and linked to both source assessments.

**Gap Summary (Rows 88–100):**

| Summary Row | Label | Value |
|-------------|-------|-------|
| 88 | Total Gaps | [Auto: COUNTA] |
| 89 | Critical | [Auto: COUNTIF] |
| 90 | High | [Auto: COUNTIF] |
| 91 | Medium | [Auto: COUNTIF] |
| 92 | Low | [Auto: COUNTIF] |
| 94 | Gaps from S1 | [Auto: COUNTIF] |
| 95 | Gaps from S2 | [Auto: COUNTIF] |
| 96 | Gaps from S3 | [Auto: COUNTIF] |
| 97 | Gaps from S4 | [Auto: COUNTIF] |
| 99 | Open Gaps | [Auto: COUNTIF Status<>"Completed"] |
| 100 | Completed Gaps | [Auto: COUNTIF Status="Completed"] |

**Dropdowns:**
- Source_Assessment: S1 / S2 / S3 / S4
- Gap_Category: Policy / Role / Screening / Contract / Legal / Cross-Domain
- Risk_Level: Critical / High / Medium / Low
- Status: Not-Started / In-Progress / Blocked / Completed / Accepted-Risk

---

## 12. Sheet 9: Evidence_Register

### Purpose
Master evidence catalog. Single reference point for all evidence across S1–S4. Auditors use this sheet to locate every piece of evidence.

**Structure:** 80 evidence rows (rows 5–84), 12 columns (A–L).

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Master_Evidence_ID | Text | Auto-generated: MEVD-001 through MEVD-080 |
| B | Source_Assessment | Dropdown | S1 / S2 / S3 / S4 |
| C | Source_Evidence_ID | Text | Original Evidence ID from source |
| D | Evidence_Category | Dropdown | Policy / Role-Definition / RACI / Training / Screening / NDA / Contract / DPA / Legal / Exit / Other |
| E | Description | Text | What the evidence is |
| F | Related_Personnel_ID | Text | Who it relates to (or "All" / "Process") |
| G | File_Location | Text | Full URL or file path — must be accessible |
| H | Date_Collected | Date | When gathered |
| I | Collected_By | Text | Name and role |
| J | Verification_Status | Dropdown | Verified / Pending / Not-Verified / Expired |
| K | Auditor_Notes | Text | Notes for audit trail |
| L | Priority | Dropdown | High / Medium / Low (audit priority) |

**Priority Guidance:**
- **High:** NDAs, screening consent forms, criminal check reports, DPIA, contract templates, DPAs — these are the first things an auditor requests
- **Medium:** Role definitions, RACI matrix, training records, exit checklists
- **Low:** Supporting documentation, process manuals, review records

**Evidence Summary (Rows 88–100):**

| Label | Value |
|-------|-------|
| Total Evidence Items | [Auto] |
| Verified | [Auto] |
| Pending Verification | [Auto] |
| Not Verified | [Auto] |
| Expired | [Auto] |
| Evidence from S1 | [Auto] |
| Evidence from S2 | [Auto] |
| Evidence from S3 | [Auto] |
| Evidence from S4 | [Auto] |
| High Priority — Verified | [Auto] |
| High Priority — Not Verified | [Auto] |

**Dropdowns:**
- Source_Assessment: S1 / S2 / S3 / S4
- Evidence_Category: Policy / Role-Definition / RACI / Training / Screening / NDA / Contract / DPA / Legal / Exit / Other
- Verification_Status: Verified / Pending / Not-Verified / Expired
- Priority: High / Medium / Low

---

## 13. Sheet 10: Action_Items

### Purpose
Prioritized remediation roadmap derived from Gap_Analysis. Translates gaps into executable actions with owners, timelines, and resource requirements.

**Structure:** 40 action rows (rows 5–44), 14 columns (A–N). Covers the top 40 gaps by priority.

| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Action_ID | Text | Auto-generated: ACT-001 through ACT-040 |
| B | Related_Gap_ID | Text | CGAP-xxx from Sheet 8 |
| C | Action_Description | Text | Specific, actionable task (not vague) |
| D | Priority | Dropdown | Critical / High / Medium / Low |
| E | Milestone | Dropdown | 0-30 days / 31-60 days / 61-90 days / 91-180 days / >180 days |
| F | Owner | Text | Person responsible |
| G | Supporting_Team | Text | Who assists |
| H | Start_Date | Date | When work begins |
| I | Target_Date | Date | When it must be complete |
| J | Status | Dropdown | Not Started / In Progress / Completed / Blocked |
| K | Progress_Pct | Number | 0–100 |
| L | Estimated_Effort | Dropdown | <1hr / 1-4hrs / 1day / 2-5days / >1week |
| M | Budget_Required | Dropdown | None / <CHF 1,000 / CHF 1,000–5,000 / >CHF 5,000 |
| N | Notes | Text | Free text |

**Milestone Guidance:**
- **0–30 days:** All Critical gaps. No exceptions. These represent active security risks.
- **31–60 days:** All High gaps. These are significant but do not represent immediate breach risk.
- **61–90 days:** High priority Medium gaps. Items needed for audit readiness.
- **91–180 days:** Remaining Medium and Low gaps. Routine improvement.
- **> 180 days:** Low priority items that can be deferred.

**Quick Wins Identification:**
At least 3 actions should be designated as "Quick Wins" — tasks that can be completed in < 1 day, demonstrate progress, and build organizational momentum. Examples:
- Schedule NDA signing for employees with missing NDAs (1 hour)
- Send screening consent forms to contractors pending consent (2 hours)
- Update contract template with missing clause (half day)

**Action Plan Summary (Rows 48–58):**

| Label | Value |
|-------|-------|
| Total Actions | [Auto] |
| Critical Actions | [Auto] |
| High Actions | [Auto] |
| Medium Actions | [Auto] |
| Low Actions | [Auto] |
| Actions in 0–30 Days | [Auto] |
| Actions in 31–60 Days | [Auto] |
| Actions in 61–90 Days | [Auto] |
| Completed Actions | [Auto] |
| Estimated Total Effort | [Auto: SUM] |

**Dropdowns:**
- Priority: Critical / High / Medium / Low
- Milestone: 0-30 days / 31-60 days / 61-90 days / 91-180 days / >180 days
- Status: Not Started / In Progress / Completed / Blocked
- Estimated_Effort: <1hr / 1-4hrs / 1day / 2-5days / >1week
- Budget_Required: None / <CHF 1,000 / CHF 1,000–5,000 / >CHF 5,000

---

## 14. Sheet 11: Approval_Sign_Off

### Purpose
Three-level governance certification. This sheet is the formal sign-off for the consolidated dashboard.

### Layout

**Classification Banner (Row 1):**
- Merged A1:H1: "INTERNAL — GOVERNANCE CERTIFICATION"
- Background: Dark Blue (003366), White text, Arial 14pt Bold

**Header (Row 3):**
- Merged A3:H3: "GOVERNANCE COMPLIANCE DASHBOARD — CERTIFICATION"
- Background: Blue (0070C0), White text

**Dashboard Summary (Rows 5–12):**

| Cell | Label | Value |
|------|-------|-------|
| A5 | Dashboard ID: | ISMS-IMP-A.5.1-2-6.1-2.S5 |
| A6 | Assessment Period: | [Link to Sheet 2] |
| A7 | Weighted Compliance Score: | [Link to Sheet 2] |
| A8 | Maturity Level: | [Link to Sheet 3] |
| A9 | Total Gaps: | [Link to Sheet 8] |
| A10 | Critical Gaps: | [Link to Sheet 8] |
| A11 | Cross-Domain Gaps: | [Link to Sheet 8] |
| A12 | NDA Compliance Rate: | [Link to Sheet 7] |

**Level 1 Approval — HR Manager / Personnel Security Officer (Rows 15–25):**

| Row | Content |
|-----|---------|
| 15 | "LEVEL 1: SOURCE DATA ACCURACY CONFIRMATION" (section header) |
| 17 | "I confirm that the source assessment data referenced by this dashboard is accurate and complete." |
| 19 | "I confirm that HR records are consistent with screening and contract data in S1–S4." |
| 21 | Name: [USER INPUT] |
| 22 | Role: [USER INPUT] |
| 23 | Date: [USER INPUT — date picker] |
| 24 | Signature: _________________________ |
| 25 | Decision: [Dropdown: Confirmed / Not Confirmed — Rework Required] |

**Level 2 Approval — Information Security Officer (Rows 28–38):**

| Row | Content |
|-----|---------|
| 28 | "LEVEL 2: COMPLETENESS AND CONSISTENCY REVIEW" (section header) |
| 30 | "I confirm that this dashboard is complete, logically consistent, and accurately represents the consolidated compliance posture." |
| 31 | "I confirm that cross-domain gaps are correctly identified and remediation plans are in place for all Critical and High gaps." |
| 33 | Name: [USER INPUT] |
| 34 | Role: [USER INPUT] |
| 35 | Date: [USER INPUT — date picker] |
| 36 | Signature: _________________________ |
| 37 | Recommendation: [Dropdown: Approve / Approve with Conditions / Reject / Require Rework] |
| 38 | Conditions (if applicable): [USER INPUT — free text] |

**Level 3 Certification — CISO (Rows 41–59):**

| Row | Content |
|-----|---------|
| 41 | "LEVEL 3: CISO GOVERNANCE CERTIFICATION" (section header — Dark Blue) |
| 43 | "I certify that:" |
| 44 | "☐ All four source assessments (S1–S4) have been completed, approved, and reviewed." |
| 45 | "☐ The consolidated compliance dashboard accurately represents the organization's personnel security posture." |
| 46 | "☐ All identified gaps are documented with appropriate risk levels and remediation plans." |
| 47 | "☐ The organization's processing of personal data in the screening process is compliant with the Swiss Federal Act on Data Protection (FADP / nDSG)." |
| 48 | "☐ Any gaps formally accepted (rather than remediated) are documented below with business justification." |
| 50 | "Risk Acceptance Statement (if applicable):" |
| 51–53 | [USER INPUT — free text area for risk acceptance rationale] |
| 55 | Name: [USER INPUT] |
| 56 | Role: Chief Information Security Officer |
| 57 | Date: [USER INPUT — date picker] |
| 58 | Signature: _________________________ |
| 59 | Decision: [Dropdown: Certified / Certified with Conditions / Rejected] |

**Print Area:** Rows 1–59. Sheet 11 header includes "INTERNAL — GOVERNANCE CERTIFICATION". Print area includes signature blocks with adequate space.

---

## 15. Sheet Protection and Cell Access

**Protected cells (read-only):**
- All formula cells
- All headers and labels
- All static reference text
- Classification banners

**Unprotected cells (user input):**
- All USER INPUT fields (light yellow fill)
- Narrative text areas
- Approval sign-off fields (name, date, decision)
- Trend indicators (Sheet 2)
- Maturity level selections (Sheet 3)
- Previous quarter data (Sheet 3)
- Gap status updates (Sheet 8)
- Action item fields (Sheet 10)

**Sheet Protection Password:** Set during workbook generation
**Allowed operations:** Format cells, Insert rows, Sort, Filter
**Disallowed operations:** Delete rows, Modify formulas, Unprotect sheet

---

## 16. Workbook Technical Specification

### 16.1 Workbook Metadata

**File Name:** `ISMS-IMP-A.5.1-2-6.1-2.S5_Governance_Dashboard_YYYYMMDD.xlsx`

**Workbook Properties:**
- **Title:** ISMS-IMP-A.5.1-2-6.1-2.S5 — Governance Compliance Dashboard
- **Subject:** ISO/IEC 27001:2022 Stacked Control A.5.1 + A.5.2 + A.6.1 + A.6.2 — Consolidated Compliance
- **Keywords:** Dashboard, Governance, Compliance, Maturity, CISO, Certification, Audit, Personnel-Security, ISMS, ISO27001
- **Comments:** Generated via `generate_a5_1_2_6_1_2_s5_governance_dashboard.py`

### 16.2 Sheet Structure Summary

| Sheet # | Sheet Name | Rows | Input | Formulas | Dropdowns |
|---------|------------|------|-------|----------|-----------|
| 1 | Instructions_Legend | 80 | 8 | 0 | 0 |
| 2 | Executive_Summary | 60 | 30 | 25 | 4 |
| 3 | Maturity_Assessment | 45 | 20 | 5 | 3 |
| 4 | Policy_Summary | 60 | 25 | 10 | 2 |
| 5 | Roles_Summary | 60 | 25 | 10 | 2 |
| 6 | Screening_Summary | 75 | 35 | 15 | 3 |
| 7 | Contract_Summary | 72 | 32 | 14 | 3 |
| 8 | Gap_Analysis | 100 | 640 | 90 | 5 |
| 9 | Evidence_Register | 100 | 720 | 16 | 4 |
| 10 | Action_Items | 60 | 480 | 12 | 5 |
| 11 | Approval_Sign_Off | 80 | 30 | 18 | 2 |

**Estimated Python Script Length:** ~1,050 lines

### 16.3 Color Scheme & Styling

**Consistent with S1–S4:**

| Element | Fill | Font |
|---------|------|------|
| User Input | Yellow (FFFF00) | Arial 10pt |
| Auto-Calculated | Light Blue (DCE6F1) | Arial 10pt |
| Labels | Gray (D9D9D9) | Arial 10pt Bold |
| Main Title | Dark Blue (003366) | Arial 18pt Bold White |
| Section Headers | Dark Blue (003366) | Arial 12pt White |

**Traffic Light Conditional Formatting:**

| Value | Fill | Font |
|-------|------|------|
| 🟢 Green / Ready / Excellent / Good | Green (92D050) | Black |
| 🟡 Yellow / Conditional / Acceptable | Yellow (FFFF00) | Black |
| 🟠 Orange / Needs Improvement | Orange (FFC000) | Black |
| 🔴 Red / Critical / Not Ready | Red (FF0000) | White |

### 16.4 Conditional Formatting Rules

**Sheet 2 (Executive_Summary):**
- Weighted Score cell: Green (≥95), Yellow (85–94), Orange (70–84), Red (<70) — large font 22pt
- Domain Status column: Green/Yellow/Orange/Red per row
- Critical Gaps count: Red fill if >0
- Trend column: ↑ Green, → Yellow, ↓ Red

**Sheet 3 (Maturity_Assessment):**
- Maturity Level cell: Green (4–5), Yellow (3), Red (1–2)
- Trend cell: ↑ Green, → Yellow, ↓ Red
- Indicator rows: Green if Met = "✅ Yes", Gray if "❌ No"

**Sheet 6 (Screening_Summary):**
- FADP block header: Orange (FFC000) if "⚠️ Review Required", Green (C6EFCE) if "✅ Compliant"

**Sheet 7 (Contract_Summary):**
- NDA block border: Red if rate <95%, Green if ≥95%

**Sheet 8 (Gap_Analysis):**
- Risk_Level column: Critical = Red fill / White text, High = Orange, Medium = Yellow, Low = Light Green
- Status column: Completed = Green, In-Progress = Blue, Not-Started = Gray, Blocked = Orange, Accepted-Risk = Purple

**Sheet 9 (Evidence_Register):**
- Verification_Status: Verified = Green, Pending = Yellow, Not-Verified = Orange, Expired = Red
- Priority: High = Red background, Medium = Yellow, Low = Green

**Sheet 10 (Action_Items):**
- Priority column: same as Gap risk levels
- Status: same as Gap status
- Progress_Pct: 0–30% Red, 31–70% Yellow, 71–99% Light Green, 100% Dark Green
- Milestone column: 0–30 days = Red (urgent), 31–60 = Orange, 61–90 = Yellow, >90 = Green

### 16.5 Freeze Panes

| Sheet | Freeze At | Rationale |
|-------|-----------|-----------|
| Instructions_Legend | None | Reference sheet |
| Executive_Summary | None | One-page layout |
| Maturity_Assessment | None | Compact layout |
| Policy_Summary | None | Short sheet |
| Roles_Summary | None | Short sheet |
| Screening_Summary | None | Short sheet |
| Contract_Summary | None | Short sheet |
| Gap_Analysis | A5 | 80 gap rows — keep headers |
| Evidence_Register | A5 | 80 evidence rows — keep headers |
| Action_Items | A5 | 40 action rows — keep headers |
| Approval_Sign_Off | A3 | Keep title visible |

### 16.6 Print Settings

All sheets: Landscape, fit 1 page wide × auto tall, narrow margins (0.5").

**Sheet 2 (Executive_Summary):** Designed to fit on a single page when printed. All content within print area must fit one page. If it exceeds, reduce font size or trim narrative sections.

**Sheet 11 (Approval_Sign_Off):** Header includes "INTERNAL — GOVERNANCE CERTIFICATION". Print area includes signature blocks with adequate space.

### 16.7 Python Script Generation

**Script:** `generate_a5_1_2_6_1_2_s5_governance_dashboard.py`

**Execution:**
```bash
python generate_a5_1_2_6_1_2_s5_governance_dashboard.py
```

**Output:** `ISMS-IMP-A.5.1-2-6.1-2.S5_Governance_Dashboard_20260131.xlsx`

---

**[END OF PART II: TECHNICAL SPECIFICATION]**

---

**Document Summary:**
- **Part I: User Guide** (~1,050 lines)
- **Part II: Technical Specification** (~550 lines)
- **Total:** ~1,600 lines

**Key Differentiators from A.8.24.5 (Cryptography Dashboard):**
- **Lifecycle-weighted scoring:** Domain weights reflect the personnel security lifecycle dependency chain (policy → roles → screening → contracts), not equal-weight technical domains
- **Legal compliance as a cross-cutting theme:** FADP compliance is surfaced explicitly in the Screening Summary (Sheet 6) and in the CISO certification statement — personnel security is the stacked control most likely to trigger FADP enforcement
- **Post-employment dimension:** Unique to personnel security — S4 post-employment obligations create an ongoing tracking requirement that persists beyond the quarterly assessment cycle
- **NDA focal point:** NDA compliance is called out as a dedicated metric in the Executive Summary and Contract Summary because it is the single most auditable element of the A.6.2 control
- **Cross-domain gap identification:** The stacked control framework creates dependencies between assessments (e.g., role tier changes must trigger screening level updates). The gap consolidation explicitly identifies and tracks these cross-domain gaps
- **CISO certification statement:** Formal certification language includes explicit FADP compliance acknowledgment and risk acceptance — tailored for the legal dimension of personnel security

---

**END OF SPECIFICATION**

---

*"Governance is the art of making decisions that stick."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->

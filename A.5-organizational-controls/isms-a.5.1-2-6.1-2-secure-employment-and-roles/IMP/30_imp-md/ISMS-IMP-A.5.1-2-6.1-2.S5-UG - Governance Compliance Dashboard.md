**ISMS-IMP-A.5.1-2-6.1-2.S5-UG - Governance Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.1, A.5.2, A.6.1, A.6.2: Stacked Control Consolidation

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Governance Compliance Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S5-UG |
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

**Audience:** CISO, Executive Management, Board / Governance Committee, Internal & External Auditors, Compliance Officer

---

## 1. Purpose and Scope

### 1.1 What This Dashboard Is

This dashboard **does not collect new data**. It aggregates, synthesizes, and presents the findings from assessments S1–S4 into a single executive-ready compliance view for the stacked personnel security control framework.

**The dashboard answers one question for leadership:**

> *"Are we compliant with ISO 27001:2022 Controls A.5.1, A.5.2, A.6.1, and A.6.2 — and if not, what is the plan to get there?"*

### 1.2 What This Dashboard Is NOT

- It is not a data entry workbook. Source data comes from S1–S4.
- It is not a risk register. It surfaces risk indicators derived from source assessments, but the detailed risk assessment lives in S1–S4.
- It is not an audit trail. Evidence documentation is in S1–S4 Evidence Registers.

### 1.3 Dashboard Design Philosophy

**Lifecycle-weighted scoring.** The four source assessments are not equal in architectural importance. The personnel security lifecycle has a dependency chain:

```
Policy Framework (A.5.1) → Roles & Responsibilities (A.5.2) → Screening (A.6.1) → Employment Terms (A.6.2)
```

Each stage depends on the integrity of the stage before it. The dashboard reflects this dependency structure in its scoring weights rather than treating all four controls equally.

**Domain Weights:**

| Domain | Control | Weight | Rationale |
|--------|---------|--------|-----------|
| Policy Framework | A.5.1 | 35% | Foundation — all other controls derive authority from policy |
| Roles & Responsibilities | A.5.2 | 25% | Defines the human structure that executes all controls |
| Screening & Vetting | A.6.1 | 20% | Pre-employment gate; failure here affects all subsequent stages |
| Employment Terms | A.6.2 | 20% | Contractual binding; important but downstream of the above |

**Legal compliance as a cross-cutting theme.** Personnel security is the stacked control most likely to trigger FADP (Swiss Federal Act on Data Protection) enforcement. Screening involves processing sensitive personal data; employment contracts must be transparent about monitoring. FADP compliance status is surfaced explicitly in the Screening Summary (Sheet 6) and in the CISO certification statement.

**Post-employment dimension.** S4 covers A.6.5 (responsibilities at termination) as a linked control. Post-employment obligations create tracking requirements that persist beyond the quarterly assessment cycle. The Contract Summary (Sheet 7) and the consolidated Gap Analysis (Sheet 8) both flag post-employment gaps separately.

**NDA as audit focal point.** NDAs are the single most auditable element of the A.6.2 control. NDA compliance rate is called out as a dedicated KPI in the Executive Summary and Contract Summary because auditors will examine it first.

---

## 2. Common Pitfalls

1. **Populating the dashboard before S1–S4 are final.** Scores will change and the dashboard will be inaccurate.
2. **Copying scores manually instead of referencing source workbooks.** Manual entry introduces transcription errors. Where possible, reference source workbook cells directly or use a documented extraction procedure.
3. **Ignoring maturity in favor of compliance score.** A 85% score with Level 2 maturity is a warning sign — the program will degrade without structural investment.
4. **Treating the dashboard as a static report.** It is a living management tool. Refresh quarterly.
5. **Understating gaps to improve the score.** Auditors will compare dashboard gaps to source assessment gaps. Discrepancies destroy credibility.
6. **Missing the legal compliance dimension.** The personnel security stacked control processes sensitive personal data (criminal records, employment history). FADP compliance is not optional — it is a legal obligation.
7. **Failing to track post-employment obligations.** S4 post-employment tracking is ongoing — departed employees' confidentiality obligations remain active. The dashboard must reflect this.

---

## 3. Dashboard Navigation

### Sheet 1: Instructions & Legend
Navigation guide, color coding, dropdown reference. Read this first.

### Sheet 2: Executive Summary
**This is the Board-facing sheet.** Designed to fit on a single printed page. Contains:
- Weighted compliance score (single number)
- Traffic-light status per domain
- Top 3 gaps requiring executive attention
- NDA compliance rate (audit focal point)
- FADP compliance indicator
- Narrative fields for CISO commentary

**Who reads this:** Board, Executive Management, External Auditors (first page)

### Sheet 3: Maturity Assessment
Maps the stacked control framework against a 5-level maturity model:

| Level | Description |
|-------|-------------|
| 1 — Initial | Ad hoc. No documented policies or processes. |
| 2 — Developing | Policies exist but are not consistently followed. Roles are informal. |
| 3 — Defined | Policies documented, roles assigned, screening performed, contracts in place. Processes are repeatable. |
| 4 — Managed | All controls measured. Gaps tracked and remediated on schedule. Evidence is complete. |
| 5 — Optimized | Continuous improvement. Lessons learned feed back into policy updates. Automated monitoring in place. |

**Current maturity level is calculated** from the aggregate compliance data across S1–S4. The user can also record the **previous quarter's maturity level** to track trend.

**Who reads this:** CISO, Auditors

### Sheet 4: Policy Summary (S1 — A.5.1)
Aggregates key metrics from S1:
- Total policies in scope vs. Active vs. Overdue for review
- Governance gap count
- Communication/acknowledgment rates
- Lifecycle compliance rate

Links to source workbook for drill-down.

### Sheet 5: Roles Summary (S2 — A.5.2)
Aggregates key metrics from S2:
- Total security roles defined vs. filled vs. vacant
- RACI coverage rate
- Training completion rate
- Competency gap count

### Sheet 6: Screening Summary (S3 — A.6.1)
Aggregates key metrics from S3:
- Screening completion rate by vetting tier
- **FADP compliance indicator** (consent records, DPIA status)
- Overdue screenings (employees whose screening has expired)
- Sensitive data processing flag (if criminal records are processed)

**FADP is called out explicitly here** because screening is the control most likely to trigger data protection enforcement.

### Sheet 7: Contract Summary (S4 — A.6.2 + A.6.5)
Aggregates key metrics from S4:
- Contract template compliance rate
- **NDA compliance rate** (dedicated KPI — audit focal point)
- Post-employment obligation tracking status
- Contractor/vendor DPA agreement coverage
- Outstanding departures without completed exit procedures

**Post-employment gaps are flagged separately** because they persist beyond the quarterly cycle.

### Sheet 8: Gap Analysis (Consolidated)
Merges all gaps from S1–S4 into a single prioritized register. Each gap shows:
- Source assessment and domain
- Risk level (Critical / High / Medium / Low)
- **Cross-domain flag** — identifies gaps that affect multiple assessments (e.g., a role tier change that should trigger a screening level update)
- Owner and target remediation date
- Current status

**Cross-domain gaps are unique to this stacked control.** The dependency chain means a failure in one domain can cascade. This sheet makes those dependencies visible.

### Sheet 9: Evidence Register
Consolidated evidence index across all 4 source assessments. Each entry links back to the source workbook's Evidence Register. This sheet enables auditors to find evidence quickly without opening each source workbook individually.

### Sheet 10: Action Items
Prioritized remediation tracker. Draws from gaps identified in Sheet 8. Tracks:
- Priority (aligned to gap risk level)
- Owner and target date
- Status (Not Started / In Progress / Completed / Blocked)
- Dependencies (which actions must complete before others can start)

### Sheet 11: Approval Sign-Off
Three-level governance certification:
- **Level 1:** HR Manager / Personnel Security Officer — confirms source data accuracy
- **Level 2:** Information Security Officer — confirms assessment completeness
- **Level 3:** CISO — final certification with explicit FADP compliance acknowledgment

The CISO certification statement includes:
- Confirmation that all four source assessments have been reviewed
- Explicit acknowledgment of FADP compliance status
- Risk acceptance statement (if any gaps are being formally accepted rather than remediated)
- Signature and date

---

## 4. Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|--------------|------------|
| #REF! errors everywhere | Source workbooks not in same directory | Place S1–S4 workbooks in same folder as S5. Filenames must match exactly. |
| Weighted score shows 0% | Source workbook compliance cells are empty | Complete source assessments first. Do not populate S5 until S1–S4 are populated. |
| External links broken | Source workbooks renamed or moved | Use the file normalization script to standardize filenames. See Part II §3. |
| Empty domain summaries | Source workbooks not populated | Complete and approve source assessments first |
| Cross-domain gaps empty | Source workbooks approved but gaps not logged | Verify Gap_Analysis sheets in S1–S4 are populated |

---

## 5. Interpreting Results

### 5.1 Reading the Weighted Compliance Score

The weighted compliance score on Sheet 2 is a single number (0–100%) calculated as:

```
Score = (S1_compliance × 0.35) + (S2_compliance × 0.25) + (S3_compliance × 0.20) + (S4_compliance × 0.20)
```

**Interpretation thresholds:**

| Score | Status | Meaning |
|-------|--------|---------|
| ≥95% | 🟢 Green | Fully compliant. Normal operations. |
| 85–94% | 🟡 Yellow | Minor gaps. Remediation in progress. Monitor. |
| 70–84% | 🟠 Orange | Significant gaps. Active remediation required. CISO attention needed. |
| <70% | 🔴 Red | Critical deficiencies. Immediate executive action required. |

### 5.2 Reading Cross-Domain Gaps

Cross-domain gaps indicate a cascade risk. Example scenarios:

- **Role tier upgraded but screening not re-performed:** A.5.2 gap triggers A.6.1 action. If an employee moves to a role requiring Enhanced screening but their screening record reflects Standard, both assessments are affected.
- **Contract clause updated but existing employees not re-signed:** A.6.2 template is correct but per-employee compliance lags. The gap exists in S4 but the root cause may be in S2 (role change process).
- **Policy updated but acknowledgment not re-collected:** A.5.1 gap. But if the policy change affects screening procedures (A.6.1), the Screening Summary should flag that new screening criteria apply.

### 5.3 Maturity vs. Compliance

A high compliance score does not necessarily mean high maturity. Maturity also considers:
- Whether processes are documented and repeatable (not just outcomes)
- Whether evidence collection is systematic
- Whether lessons learned feed back into policy
- Whether monitoring is proactive rather than reactive

A score of 90% with ad hoc evidence collection = Level 3 (Defined), not Level 4 (Managed).

---

## 6. Common Questions

**Q: Can I approve the dashboard if gaps exist?**
A: Yes. Gaps are expected and do not prevent approval. The certification confirms that gaps are identified, documented, and have remediation plans. Risk acceptance (accepting a gap without remediation) requires explicit CISO sign-off with written rationale.

**Q: How often should the dashboard be updated?**
A: Quarterly, aligned with the source assessment review cycle. Ad hoc updates are appropriate after significant organizational changes (restructuring, M&A, regulatory changes).

**Q: What if source workbooks have not been updated this quarter?**
A: The dashboard will reflect stale data. The generation script timestamps the data extraction. If source workbooks are older than 90 days, the Executive Summary should note this. Do not present stale data to the Board without flagging it.

**Q: Who owns the dashboard?**
A: The CISO owns the dashboard. The HR Manager / Personnel Security Officer provides source data accuracy confirmation at Level 1. The ISO provides completeness review at Level 2.

**Q: What is the difference between this dashboard and the consolidation script?**
A: This dashboard (S5) is the **specification** — it defines what the workbook must contain. The Python script (`generate_a5_1_2_6_1_2_s5_governance_dashboard.py`) is the **generator** — it creates the Excel workbook.

---

## 7. Dashboard Maintenance

### 7.1 Quarterly Cycle

| Task | When | Who | Time |
|------|------|-----|------|
| Complete/update S1–S4 | Week 1–2 | Security Team | 10–15 hours total |
| Regenerate S5 dashboard | Week 2 | Security Team | 2 minutes |
| Validate dashboard data | Week 2 | ISO | 15 minutes |
| Write Executive Summary narrative | Week 2–3 | CISO | 20–30 minutes |
| Level 1–2 approval | Week 3 | HR Manager, ISO | 3–5 days |
| CISO certification | Week 3–4 | CISO | 15 minutes |
| Board/management presentation | Week 4 | CISO | 5 minutes |

### 7.2 Version Control

- Filename includes date: `ISMS-IMP-A.5.1-2-6.1-2.S5_Governance_Dashboard_YYYYMMDD.xlsx`
- Previous quarter's dashboard is archived (do not delete)
- The Maturity Assessment sheet references previous quarter's score for trend tracking
- Instructions_Legend sheet contains version history

---

## 8. Quality Checklist

Before submitting for CISO certification:

**Data Integrity:**
- [ ] All external links resolve (no #REF! errors)
- [ ] Weighted compliance score matches manual calculation
- [ ] Domain summaries match source workbook metrics
- [ ] Cross-domain gaps are correctly identified
- [ ] NDA compliance rate is accurate
- [ ] FADP compliance indicator reflects current status

**Completeness:**
- [ ] Executive Summary narrative is written (not placeholder)
- [ ] Maturity Assessment current level is assigned
- [ ] Previous quarter's maturity level is recorded (for trend)
- [ ] All gaps from S1–S4 appear in consolidated Gap Analysis
- [ ] Action Items are populated for all Critical and High gaps
- [ ] Evidence Register has entries for all source assessments

**Approval Readiness:**
- [ ] Source workbooks are all approved (3-level sign-off complete)
- [ ] Source workbook dates are within 90 days
- [ ] No "TBD" placeholders remain in critical cells
- [ ] Classification header ("INTERNAL") is visible on all sheets

---

## 9. Review & Approval

### Approval Workflow

**Level 1 — HR Manager / Personnel Security Officer**
- Confirms that source assessment data is accurate and complete
- Verifies that HR records match screening and contract data
- Signs off in Sheet 11
- Typical turnaround: 2–3 business days

**Level 2 — Information Security Officer**
- Reviews dashboard for completeness and logical consistency
- Verifies cross-domain gaps are correctly identified
- Confirms remediation plans are in place for all Critical/High gaps
- Recommendation: Approve / Approve with Conditions / Reject / Require Rework
- Typical turnaround: 3–5 business days

**Level 3 — CISO (Governance Certification)**
- Reviews Executive Summary and Maturity Assessment
- Reviews all Critical gaps and risk acceptance decisions
- Acknowledges FADP compliance status explicitly
- Signs certification statement
- Decision: Certified / Certified with Conditions / Rejected
- Typical turnaround: 3–5 business days

### If Gaps Are Identified
Gaps do not prevent certification. The certification confirms that:
1. All four source assessments have been completed and approved
2. The consolidated view is accurate and complete
3. All gaps are documented with remediation plans
4. Risk levels are appropriate and accepted by management
5. The organization's personnel security posture is understood by leadership

---

## 10. Audit Readiness Checklist

**Use before declaring the dashboard audit-ready:**

### Documentation Completeness
- [ ] All 5 assessment documents exist (S1–S5)
- [ ] All documents have three-level approval sign-offs
- [ ] CISO certification signed on S5
- [ ] Governing policy (ISMS-POL-A.5.1-2-6.1-2) current and approved

### Data Integrity
- [ ] Domain scores on dashboard match source assessment dashboards
- [ ] Overall score calculated correctly (verify formula manually)
- [ ] All gaps from S1–S4 present in Gap_Consolidation (count must match sum of source gaps)
- [ ] No gaps removed or downgraded without documented justification
- [ ] Evidence file locations all tested and accessible

### Compliance Substance
- [ ] Overall score ≥ 70% (or documented risk acceptance)
- [ ] Maturity ≥ Level 3 (or documented improvement plan)
- [ ] Zero Critical gaps without remediation plans
- [ ] All High gaps have owners and target dates
- [ ] FADP legal compliance confirmed (screening consent, DPIA, retention)
- [ ] All individuals with Confidential+ data access have signed NDAs
- [ ] All individuals screened at required level (or gaps documented)
- [ ] All contractor/vendor security agreements in place (or gaps documented)
- [ ] Post-employment obligations tracked for all departed individuals

### Audit Presentation
- [ ] Executive Summary (Sheet 2) is board-ready — business language, no jargon
- [ ] Key Strength / Key Risk per domain are accurate and meaningful
- [ ] Top 3 gaps clearly stated with owners and dates
- [ ] Action plan demonstrates commitment to remediation
- [ ] Evidence index is the single reference point — auditor can find everything from here

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->

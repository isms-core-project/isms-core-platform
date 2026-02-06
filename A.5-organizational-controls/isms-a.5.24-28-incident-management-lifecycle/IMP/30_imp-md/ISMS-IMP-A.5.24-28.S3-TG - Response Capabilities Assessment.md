**ISMS-IMP-A.5.24-28.S3-TG - Incident Response Capabilities Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.26: Response to Information Security Incidents

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Incident Response Capabilities Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S3-TG |
| **Assessment Domain** | Domain 3 - Response Capabilities (A.5.26 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | CSIRT Manager / Incident Response Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CSIRT Manager | Initial response capabilities assessment specification |

**Review Cycle**: Annual (or after major incident response activities)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**: 
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISMS-IMP-A.5.29-30 (BC/DR Framework)
- ISO/IEC 27002:2022 Control A.5.26
- NIST SP 800-61 Rev. 2 Section 3.3 (Containment, Eradication, and Recovery)

---

# Technical Specification

Workbook Structure (11 Sheets)

Instructions & Legend
Containment Capabilities (30 Q)
Eradication & Remediation (20 Q)
Recovery & Restoration (20 Q)
Communication (20 Q)
Resources & Authority (20 Q)
Playbook Effectiveness (15 Q)
Gap Analysis (40 capacity)
Evidence Register (60 capacity)
Dashboard
Approval Sign-Off

Total Questions: 125
Key Metrics: MTTC, MTTR, SLA Compliance %, Playbook Usage Rate

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

## Document Overview

**Document ID:** ISMS-IMP-A.5.24-28.S3
**Assessment Area:** Incident Response Capabilities (Containment, Eradication, Recovery, Communication, Resources, Playbooks)
**Related Policy:** ISMS-POL-A.5.24-28, Section 2.3 (A.5.26 – Response to Information Security Incidents)
**Purpose:** Evaluate operational readiness and execution effectiveness across all response phases, using metrics extracted from recent incidents and capability assessments per response domain

**Key Principle:** This assessment is **metric-driven**. Where possible, assessors extract MTTC, MTTE, and MTTR from the last 6 months of incident tickets rather than self-reporting estimates. Capability questions validate that the procedures and tools backing those metrics actually exist.

---

## Instructions for Completing This Assessment

### How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Response Capabilities Assessment Excel workbook (`ISMS-IMP-A.5.24-28.S3_Response_Capabilities_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a524_28_s3_response_capabilities.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Extract metrics first** — pull MTTC, MTTE, MTTR from your ticketing/SIEM system for the last 6 months before completing any assessment sheet
2. **Work through each section** — Containment → Eradication → Recovery → Communication → Resources → Playbooks
3. **Select the answer from each dropdown** that most accurately reflects current capability
4. **Enter durations** in the unit shown (minutes or hours as labelled)
5. **Enter percentages** as whole numbers (e.g., 85 for 85%)
6. **Provide evidence references** — ticket IDs, runbook locations, tool names, documentation paths
7. **Review the Gap_Identified column** — formulas flag gaps automatically; add detail in Comments where needed
8. **Complete Gap Analysis** — transfer flagged items, prioritise, assign owners
9. **Obtain approval** via the Approval Sign-Off sheet

### Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| **✅** | **Compliant** | Capability fully operational, metrics within SLA |
| **⚠️** | **Partial** | Capability exists but gaps or SLA breaches present |
| **❌** | **Non-Compliant** | Capability missing or metrics significantly outside SLA |
| **N/A** | **Not Applicable** | Does not apply to this organisation's environment |

### Acceptable Evidence

- Incident ticket exports (last 6 months)
- Response playbook documents and version history
- EDR/SIEM tool configuration screenshots
- Network architecture diagrams showing segmentation
- Authority/escalation matrix documents
- Communication templates and approval records
- Tabletop or live exercise reports
- After-action / post-incident review reports
- Training completion records

---

## Sheet 1: Instructions & Legend

### Header Section
- **Title:** "ISMS-IMP-A.5.24-28.S3 — Incident Response Capabilities Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 – Control A.5.26: Response to Information Security Incidents"
- **Styling:** Dark blue header (#003366), white text, centred, row height 30

### Document Information Block
```plaintext
Document ID:           ISMS-IMP-A.5.24-28.S3
Assessment Area:       Response Capabilities
Related Policy:        ISMS-POL-A.5.24-28, Section 2.3
Version:               1.0
Assessment Date:       [USER INPUT – yellow cell]
Completed By:          [USER INPUT – yellow cell]
Organisation:          [USER INPUT – yellow cell]
Metrics Period:        [USER INPUT – yellow cell, e.g. "01.07.2025 – 31.12.2025"]
Review Cycle:          Annual (or after major incident)
```

### How to Use This Workbook
1. Extract response metrics from your ticketing system (6-month window) before starting
2. Complete Containment Capabilities sheet — network, endpoint, account, application layers
3. Complete Eradication & Remediation — malware removal, patching, root-cause identification
4. Complete Recovery & Restoration — backup restoration, service resumption, post-recovery monitoring
5. Complete Communication — internal coordination, external/customer notification, regulatory reporting
6. Complete Resources & Authority — budget, staffing, decision authority matrix
7. Complete Playbook Effectiveness — coverage, usage rates, update cadence
8. Review Dashboard for automated metric calculations and maturity scoring
9. Transfer gaps to Gap Analysis, prioritise, assign owners
10. Obtain approval via Approval Sign-Off

### Status Legend (rendered in workbook)

| Symbol | Status | Description | Colour Code |
|--------|--------|-------------|-------------|
| ✅ | Compliant | Capability operational, within SLA | Green (#C6EFCE) |
| ⚠️ | Partial | Capability exists, gaps present | Yellow (#FFEB9C) |
| ❌ | Non-Compliant | Capability missing or severely degraded | Red (#FFC7CE) |
| N/A | Not Applicable | Not relevant to this environment | Grey (#D9D9D9) |

---

## Sheet 2: Containment Capabilities (30 Questions)

### Purpose
Assess the organisation's ability to stop an active threat from spreading — network isolation, endpoint control, account suspension, and application-layer containment.

### Header
**Row 1:** "CONTAINMENT CAPABILITIES"
**Row 2:** "Network, Endpoint, Account, Application Containment (30 Questions)"

### Column Definitions

| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Question_ID | 12 | Static | Q1–Q30, prefixed by section header rows |
| B | Section | 25 | Static | Network / Endpoint / Account / Application / Metrics |
| C | Question | 60 | Static | Assessment question text (wrap text enabled) |
| D | Answer | 25 | **User Input** (yellow) | Dropdown or free-text per question type |
| E | Evidence_Reference | 30 | **User Input** (yellow) | Ticket ID, tool name, document path |
| F | Comments | 35 | **User Input** (yellow) | Free text — context, caveats, planned improvements |
| G | Gap_Identified | 12 | Formula (green) | Auto-calculated — see formula below |

### Section Breakdown

**Network (Q1–Q8):** Network segment isolation, emergency firewall rules, internet egress blocking, quarantine VLAN, containment authority, 24/7 availability, average network containment time.

**Endpoint (Q9–Q15):** EDR-based remote isolation, isolation speed, non-EDR fallback, percentage of endpoints isolatable, laptop remote isolation, production server isolation authority, isolation reversal procedure.

**Account (Q16–Q22):** Compromised account suspension speed, suspension authority, MFA/session revocation, service account credential rotation, forced password reset, privileged access revocation, average account suspension time.

**Application (Q23–Q27):** Application shutdown authority, individual service isolation, database connection blocking, emergency WAF rule deployment, cloud service containment.

**Metrics (Q28–Q30):** Mean Time to Contain (MTTC) overall (6-month window), MTTC for Critical-severity incidents, percentage of incidents meeting containment SLA.

### Answer Type Reference (Sheet 2)

| Q-Range | Answer Types Used |
|---------|-------------------|
| Q1 | Dropdown: Automated / Manual / Limited / No |
| Q2 | Dropdown: 24/7 / Business Hours / No |
| Q3 | Dropdown: Per System / Per Subnet / No |
| Q4 | Dropdown: Yes / No |
| Q5 | Duration (minutes) — free text number |
| Q6 | Text — name/role of authority holder |
| Q7 | Dropdown: Comprehensive / Basic / No |
| Q8 | Dropdown: 24/7 / On-Call / Business Hours / No |
| Q9 | Dropdown: Automated / Manual / No EDR / No |
| Q10 | Duration (minutes) — free text number |
| Q11–Q15 | Yes/No or capability-specific dropdowns |
| Q16 | Dropdown: Automated / Manual (Min) / Manual (Hours) / No |
| Q17 | Text — name/role |
| Q18–Q21 | Yes / No or capability-specific |
| Q22 | Duration (minutes) |
| Q23 | Text — name/role |
| Q24–Q27 | Capability-specific dropdowns |
| Q28–Q29 | Duration (hours) — free text number |
| Q30 | Percentage (0–100) — free text number |

### Compliance Checklist
```
☐ Network isolation capability verified (live or exercise)
☐ Quarantine VLAN documented and tested
☐ EDR endpoint isolation tested within last 90 days
☐ Account suspension procedure tested (tabletop or live)
☐ Containment authority matrix approved by management
☐ MTTC targets defined per severity level
☐ All containment procedures documented in playbooks
☐ 24/7 containment capability confirmed (or on-call SLA documented)
```

---

## Sheet 3: Eradication & Remediation (20 Questions)

### Purpose
Assess the organisation's ability to remove threats and restore a clean state — malware removal, vulnerability remediation, and root-cause identification.

### Header
**Row 1:** "ERADICATION & REMEDIATION"
**Row 2:** "Malware Removal, Vulnerability Patching, Root Cause Identification (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Malware (Q31–Q37):** Malware removal procedure documentation, EDR automated removal capability, system reimaging capability and speed, lateral movement containment during eradication, backup verification before restoration, eradication confirmation method, average time to eradicate.

**Vulnerability (Q38–Q43):** Emergency patching capability, patch deployment speed for critical CVEs, configuration hardening procedures, vulnerability scanning post-eradication, compensating control deployment for unpatched systems, patch rollback capability.

**Root Cause (Q44–Q46):** Root cause analysis capability, percentage of incidents with documented RCA (last 10), RCA integration into control improvements.

**Metrics (Q47–Q50):** Mean Time to Eradicate (MTTE) overall (6-month), MTTE for Critical incidents, eradication success rate (no recurrence within 30 days), percentage of incidents where root cause was identified before eradication declared complete.

### Compliance Checklist
```
☐ Malware removal procedures tested (EICAR/live exercise)
☐ Reimaging capability confirmed — target time documented
☐ Emergency patch process activated and tested within last 12 months
☐ Backup integrity verified before any restoration action (procedure exists)
☐ Root cause analysis mandatory for all Critical and High incidents
☐ MTTE targets defined and tracked
☐ Eradication confirmation criteria documented (not just symptom removal)
```

---

## Sheet 4: Recovery & Restoration (20 Questions)

### Purpose
Assess restoration procedures, service resumption capability, and post-recovery monitoring controls.

### Header
**Row 1:** "RECOVERY & RESTORATION"
**Row 2:** "System Restoration, Service Resumption, Post-Recovery Monitoring (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Restoration (Q51–Q57):** System restoration procedure documentation, backup availability for critical systems, average backup restoration time, backup integrity verification before restoration, clean rebuild capability, configuration restoration capability, data recovery testing frequency.

**Resumption (Q58–Q64):** Service resumption procedures, post-recovery validation scope, staged recovery capability, user communication during recovery, service degradation mode capability, RTOs defined for critical services, percentage of incidents meeting RTO (6-month).

**Monitoring (Q65–Q70):** Enhanced monitoring period after recovery (duration), active reinfection monitoring, IOC-based monitoring post-recovery, Mean Time to Recover (MTTR) overall (6-month), MTTR for Critical incidents, recovery success rate (no recurrence within 30 days).

### Compliance Checklist
```
☐ Backup restoration tested within last 12 months (critical systems)
☐ RTOs defined and approved for all critical services
☐ Staged recovery procedure documented
☐ Enhanced monitoring period (minimum 7 days) defined in playbooks
☐ IOC watchlists maintained and updated post-incident
☐ MTTR targets defined per severity level
☐ Post-recovery validation checklist exists and is mandatory
```

---

## Sheet 5: Communication (20 Questions)

### Purpose
Assess internal coordination, external stakeholder notification, and regulatory reporting capability during active incidents.

### Header
**Row 1:** "COMMUNICATION"
**Row 2:** "Internal Coordination, External Notification, Regulatory Reporting (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Internal (Q71–Q77):** Internal communication protocol documentation, management notification SLA compliance, affected user notification approach, IT Operations coordination channel, pre-approved communication templates, communication approval process, incident communication logging.

**External (Q78–Q84):** External communication procedure documentation, customer notification capability, regulatory notification templates readiness, media/press response procedure, third-party/supplier notification, legal counsel involvement timing, post-incident customer communication.

**Regulatory (Q85–Q90):** Regulatory notification timeline compliance (last 5 breaches), breach notification procedure documented, authority contacts maintained, notification drafting speed (hours from decision to submission), regulatory feedback incorporation, multi-jurisdiction notification handling.

### Compliance Checklist
```
☐ Internal communication templates pre-approved by Legal
☐ Management notification SLA defined (Critical: <1 hour)
☐ Regulatory notification procedure reviewed by Legal annually
☐ Authority contact list maintained and tested
☐ All incident communications logged (who, what, when, to whom)
☐ External communication approval chain documented
☐ Multi-jurisdiction breach notification matrix maintained (if applicable)
```

---

## Sheet 6: Resources & Authority (20 Questions)

### Purpose
Assess budget allocation, staffing adequacy, tool availability, and the decision-authority matrix that enables rapid response execution.

### Header
**Row 1:** "RESOURCES & AUTHORITY"
**Row 2:** "Budget, Staffing, Tools, Decision Authority (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Budget & Staffing:** Dedicated IR budget existence, budget adequacy (self-assessment), CSIRT staffing model (dedicated/on-call/hybrid), 24/7 coverage capability, external IR retainer existence, IR personnel training budget.

**Tools:** IR ticketing system, SIEM availability, EDR coverage percentage, forensic tooling availability, communication/war-room capability, automation/SOAR availability.

**Authority:** Emergency change authority matrix, containment authority without management approval, budget authority during active incidents, authority matrix tested (tabletop or live), authority gaps identified, authority documentation currency.

### Compliance Checklist
```
☐ IR budget line item exists and is reviewed annually
☐ CSIRT staffing model documented and approved
☐ Authority matrix approved by executive management
☐ Authority matrix exercised in at least one tabletop per year
☐ External IR retainer (if used) contracts reviewed annually
☐ Tool availability confirmed for all IR phases
```

---

## Sheet 7: Playbook Effectiveness (15 Questions)

### Purpose
Assess whether response playbooks exist for all critical incident categories, are actively used during incidents, and are kept current.

### Header
**Row 1:** "PLAYBOOK EFFECTIVENESS"
**Row 2:** "Coverage, Usage, Maintenance (15 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Coverage (Q106–Q110):** Playbooks exist for all primary incident categories, coverage percentage across categories, playbooks include containment + eradication + recovery steps, playbooks reference forensic evidence collection, playbooks include communication/notification steps.

**Usage (Q111–Q115):** Playbooks consulted during last 5 incidents, percentage of incidents where playbook was followed, playbook deviation documented when occurred, playbook feedback captured post-incident, playbook accessibility during active incidents (mobile/offline).

**Maintenance (Q116–Q120):** Playbook review frequency, last review date within cycle, lessons learned incorporated, playbook owner assigned and accountable, playbook version controlled.

### Compliance Checklist
```
☐ Playbooks exist for all incident categories identified in S2 taxonomy
☐ Playbooks reviewed and updated after every Critical incident
☐ Playbooks accessible offline (printed/cached) during network outages
☐ Playbook owners assigned and accountable for annual review
☐ Playbook usage tracked per incident for effectiveness measurement
```

---

## Sheet 8: Gap Analysis (40 Capacity)

### Purpose
Consolidate all gaps flagged by the Gap_Identified formula across Sheets 2–7. Prioritise, assign owners, and track remediation.

### Header
**Row 1:** "GAP ANALYSIS"
**Row 2:** "Prioritised remediation tracking — auto-populated from assessment sheets"

### Column Definitions

| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Gap_ID | 12 | Formula | Auto-numbered: `="GAP-"&TEXT(ROW()-4,"000")` |
| B | Source_Sheet | 28 | **User Input** (yellow) | Which sheet the gap originated from |
| C | Question_ID | 14 | **User Input** (yellow) | e.g. Q5, Q28 |
| D | Gap_Description | 55 | **User Input** (yellow) | Detailed description of the gap |
| E | Severity | 16 | **User Input** (yellow) | Dropdown: Critical / High / Medium / Low |
| F | Owner | 28 | **User Input** (yellow) | Name or role responsible |
| G | Target_Date | 16 | **User Input** (yellow) | DD.MM.YYYY |
| H | Status | 18 | **User Input** (yellow) | Dropdown: Open / In Progress / Completed / Deferred |
| I | Remediation_Notes | 40 | **User Input** (yellow) | Free text |

### Summary Formulas (Row 2, above headers)

```excel
Total Gaps:        =COUNTA(C5:C44)
Critical:          =COUNTIF(E5:E44,"Critical")
High:              =COUNTIF(E5:E44,"High")
Open:              =COUNTIF(H5:H44,"Open")+COUNTIF(H5:H44,"In Progress")
```

---

## Sheet 9: Evidence Register (60 Capacity)

### Purpose
Log all evidence collected to support this assessment and future audits.

### Header
**Row 1:** "EVIDENCE REGISTER"
**Row 2:** "Evidence supporting Response Capabilities assessment"

### Column Definitions

| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Evidence_ID | 14 | Formula | `="EV-"&TEXT(ROW()-4,"000")` |
| B | Related_Question | 18 | **User Input** (yellow) | Q-number(s) this evidence supports |
| C | Evidence_Type | 22 | **User Input** (yellow) | Dropdown: Ticket Export / Playbook / Tool Config / Exercise Report / Training Record / Other |
| D | Description | 50 | **User Input** (yellow) | Free text — what the evidence contains |
| E | Source_Location | 40 | **User Input** (yellow) | File path, URL, or system reference |
| F | Collected_By | 22 | **User Input** (yellow) | Name |
| G | Collection_Date | 16 | **User Input** (yellow) | DD.MM.YYYY |
| H | Valid_Until | 16 | **User Input** (yellow) | DD.MM.YYYY (or "Ongoing") |

---

## Sheet 10: Dashboard

### Purpose
Automated summary of response capability maturity across all six assessment domains, plus key SLA metrics.

### Header
**Row 1:** "RESPONSE CAPABILITIES DASHBOARD"
**Row 2:** "ISMS-IMP-A.5.24-28.S3 — Automated Maturity & Metrics Summary"

### Panel 1: Key Response Metrics

| Metric | Source | Formula |
|--------|--------|---------|
| MTTC (Overall) | Sheet 2, Q28 | `='Containment Capabilities'!D32` |
| MTTC (Critical) | Sheet 2, Q29 | `='Containment Capabilities'!D33` |
| MTTE (Overall) | Sheet 3, Q47 | `='Eradication & Remediation'!D51` |
| MTTE (Critical) | Sheet 3, Q48 | `='Eradication & Remediation'!D52` |
| MTTR (Overall) | Sheet 4, Q68 | `='Recovery & Restoration'!D72` |
| MTTR (Critical) | Sheet 4, Q69 | `='Recovery & Restoration'!D73` |
| Containment SLA % | Sheet 2, Q30 | `='Containment Capabilities'!D34` |
| Recovery Success Rate | Sheet 4, Q70 | `='Recovery & Restoration'!D74` |

### Panel 2: Domain Maturity Scores

Each domain scored 0–100 based on the ratio of non-gap answers to total questions:

```excel
Containment Score:  =COUNTIF('Containment Capabilities'!G5:G34,"No")/30*100
Eradication Score:  =COUNTIF('Eradication & Remediation'!G5:G24,"No")/20*100
Recovery Score:     =COUNTIF('Recovery & Restoration'!G5:G24,"No")/20*100
Communication Score:=COUNTIF(Communication!G5:G24,"No")/20*100
Resources Score:    =COUNTIF('Resources & Authority'!G5:G24,"No")/20*100
Playbook Score:     =COUNTIF('Playbook Effectiveness'!G5:G19,"No")/15*100
```

**Maturity Level Mapping:**

| Score Range | Maturity Level | Colour |
|-------------|----------------|--------|
| 90–100 | Level 5 – Optimised | Green (#C6EFCE) |
| 70–89 | Level 4 – Managed | Light Green (#E2EFDA) |
| 50–69 | Level 3 – Defined | Yellow (#FFEB9C) |
| 30–49 | Level 2 – Developing | Orange (#FCE4D6) |
| 0–29 | Level 1 – Initial | Red (#FFC7CE) |

### Panel 3: Gap Summary

```excel
Total Gaps Flagged:  =COUNTIF('Containment Capabilities'!G5:G34,"Yes")+COUNTIF('Eradication & Remediation'!G5:G24,"Yes")+COUNTIF('Recovery & Restoration'!G5:G24,"Yes")+COUNTIF(Communication!G5:G24,"Yes")+COUNTIF('Resources & Authority'!G5:G24,"Yes")+COUNTIF('Playbook Effectiveness'!G5:G19,"Yes")
Gaps Logged in Gap Analysis: =COUNTA('Gap Analysis'!C5:C44)
Gaps Requiring Attention:    =[Total Gaps Flagged] - [Gaps Logged]
```

---

## Sheet 11: Approval Sign-Off

### Purpose
Formal review and approval workflow for the completed assessment.

### Structure

| Field | Type |
|-------|------|
| Assessment Reviewer Name | User Input (yellow) |
| Reviewer Role | User Input (yellow) |
| Review Date | User Input (yellow) |
| Review Comments | User Input (yellow, multi-line) |
| Approval Decision | Dropdown: Approved / Approved with conditions / Rejected |
| Next Review Date | User Input (yellow) |
| Next Review Responsible | User Input (yellow) |

---

## Appendix A: Developer Technical Reference

### A.1 Workbook Structure Summary

| Sheet # | Name | Questions | Key Feature |
|---------|------|-----------|-------------|
| 1 | Instructions & Legend | — | Workflow guide, status legend, evidence types |
| 2 | Containment Capabilities | 30 | Network/Endpoint/Account/Application layers |
| 3 | Eradication & Remediation | 20 | Malware removal, patching, RCA |
| 4 | Recovery & Restoration | 20 | Backup restoration, RTOs, post-recovery monitoring |
| 5 | Communication | 20 | Internal/External/Regulatory notification |
| 6 | Resources & Authority | 20 | Budget, staffing, authority matrix |
| 7 | Playbook Effectiveness | 15 | Coverage, usage, maintenance |
| 8 | Gap Analysis | 40 cap | Prioritised remediation tracking |
| 9 | Evidence Register | 60 cap | Audit evidence log |
| 10 | Dashboard | — | Metrics, maturity scores, gap summary |
| 11 | Approval Sign-Off | — | Formal approval workflow |

**Total Assessment Questions:** 125
**Freeze Panes:** Row 5 on all assessment sheets (headers stay visible)

### A.2 Data Validation Rules

**Answer Column (D) — Assessment Sheets:**

Each question defines its own dropdown or input type. The most common validation sets:

| Validation Set | Applied To | Values |
|----------------|-----------|--------|
| Capability Level | Q1, Q7, Q9, Q16, Q31, Q32, etc. | Automated / Manual / Limited / No |
| Availability | Q2, Q8 | 24/7 / Business Hours / No |
| Yes/No | Q4, Q11, Q18, Q71, Q78, etc. | Yes / No |
| Duration | Q5, Q10, Q22, Q28, Q29, Q53, Q68, Q69 | Free text number (unit shown in question) |
| Percentage | Q12, Q30, Q64, Q70, Q90 | Free text number 0–100 |
| Text | Q6, Q17, Q23 | Free text (authority holder name/role) |
| Completeness | Q7, Q31, Q51, Q75 | Comprehensive / Basic / No |

**Gap Analysis Sheet:**

| Column | Validation |
|--------|------------|
| E (Severity) | Critical / High / Medium / Low |
| H (Status) | Open / In Progress / Completed / Deferred |

**Evidence Register Sheet:**

| Column | Validation |
|--------|------------|
| C (Evidence_Type) | Ticket Export / Playbook / Tool Config / Exercise Report / Training Record / Other |

### A.3 Conditional Formatting

**Gap_Identified Column (G) — All Assessment Sheets:**
- "Yes" → Red fill (#FFC7CE), bold text
- "No" → Green fill (#C6EFCE)

**Gap Analysis Severity (Column E):**
- Critical → Red fill (#FFC7CE)
- High → Orange fill (#FCE4D6)
- Medium → Yellow fill (#FFEB9C)
- Low → Light blue fill (#B4C7E7)

**Gap Analysis Status (Column H):**
- Open → Red fill (#FFC7CE)
- In Progress → Yellow fill (#FFEB9C)
- Completed → Green fill (#C6EFCE)
- Deferred → Grey fill (#D9D9D9)

**Dashboard Maturity Scores:**
- 90–100 (Level 5) → Green (#C6EFCE)
- 70–89 (Level 4) → Light Green (#E2EFDA)
- 50–69 (Level 3) → Yellow (#FFEB9C)
- 30–49 (Level 2) → Orange (#FCE4D6)
- 0–29 (Level 1) → Red (#FFC7CE)

**Dashboard Key Metrics — SLA Thresholds:**
- MTTC ≤ target → Green
- MTTC > target but ≤ 2× target → Yellow
- MTTC > 2× target → Red
- Same logic applies to MTTE and MTTR

### A.4 Cell Protection

**Protected Cells (Formula / Static):**
- Column headers (row 4 on all assessment sheets)
- Question_ID (column A) and Question text (column C)
- Section labels (column B)
- Gap_Identified formulas (column G)
- Dashboard formulas and labels
- Gap Analysis ID formulas (column A)
- Evidence Register ID formulas (column A)

**Unprotected Cells (User Input — yellow fill):**
- Answer (column D), Evidence_Reference (column E), Comments (column F) on all assessment sheets
- All user-input columns on Gap Analysis and Evidence Register
- All fields on Approval Sign-Off
- Document information fields on Instructions & Legend

**Sheet Protection:**
- Password: [Set during workbook generation]
- Allow: Format cells, Insert rows, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

### A.5 Gap_Identified Formula Logic

Applied to column G on every assessment sheet row (rows 5 through end of questions):

```excel
=IF(OR(D5="No", D5="Limited", D5<80), "Yes", "No")
```

**Logic breakdown:**
- If Answer = "No" → gap flagged (capability absent)
- If Answer = "Limited" → gap flagged (insufficient capability)
- If Answer is a number < 80 → gap flagged (metric below threshold — applies to percentage and duration fields where lower = worse)
- All other answers → no gap

**Note for duration fields (Q5, Q10, Q22, Q28, Q29, Q53, Q68, Q69):** The formula flags values < 80 which is appropriate for percentage fields. Duration fields will not trigger this numeric check unless the value happens to be < 80 in the unit shown. Assessors should manually flag duration gaps in the Comments column if the value exceeds the organisation's SLA target.

### A.6 Evidence Register Auto-Numbering

**Evidence ID Format:**
```excel
="EV-"&TEXT(ROW()-4,"000")
```
Produces: EV-001, EV-002, … EV-060

**Gap ID Format (Gap Analysis sheet):**
```excel
="GAP-"&TEXT(ROW()-4,"000")
```
Produces: GAP-001, GAP-002, … GAP-040

### A.7 Python Script Integration Points

**Workbook Generation Script:** `generate_a524_28_s3_response_capabilities.py`

**Key Functions:**
- `create_workbook()`: Initialise workbook, create all 11 sheets
- `setup_styles()`: Define cell styles (header fill #003366, input fill #FFFFCC, calculated fill #E2EFDA, border)
- `create_assessment_sheet(ws, styles, title, subtitle, questions)`: Generic sheet generator — applies headers, populates questions, sets column widths, adds data validation per question type, applies Gap_Identified formula, freezes panes
- `create_containment_capabilities(ws, styles)`: Sheet 2 — 30 questions across 5 sections
- `create_eradication_remediation(ws, styles)`: Sheet 3 — 20 questions across 4 sections
- `create_recovery_restoration(ws, styles)`: Sheet 4 — 20 questions across 3 sections
- `create_communication(ws, styles)`: Sheet 5 — 20 questions across 3 sections
- `create_resources_authority(ws, styles)`: Sheet 6 — 20 questions across 3 sections
- `create_playbook_effectiveness(ws, styles)`: Sheet 7 — 15 questions across 3 sections
- `create_gap_analysis(ws, styles)`: Sheet 8 — 40-row capacity with summary formulas
- `create_evidence_register(ws, styles)`: Sheet 9 — 60-row capacity
- `create_dashboard(ws, styles)`: Sheet 10 — 3 panels (metrics, maturity, gaps)
- `create_approval_signoff(ws, styles)`: Sheet 11 — approval workflow

**Customisation Points (marked with `# CUSTOMIZE:` in script):**
- Sheet names (if organisational naming differs)
- Question text (if wording needs adjustment for local context)
- Gap threshold value (currently 80 — adjust if organisation uses different SLA benchmarks)
- Maturity level boundaries (currently 90/70/50/30)
- Conditional formatting colour codes
- Gap Analysis and Evidence Register row capacity

**Quality Assurance:** After generation, verify:
- All 125 questions present across Sheets 2–7
- Gap_Identified formula returns "Yes" or "No" for every row
- Dashboard metrics pull from correct cell references
- Data validation dropdowns active on all Answer cells

### A.8 Version Control

**Workbook Versioning:**
- Filename format: `ISMS-IMP-A.5.24-28.S3_Response_Capabilities_YYYYMMDD.xlsx`
- Version tracking in Instructions & Legend sheet
- Document Control section updated with each revision

**Change Log:**
- v1.0: Initial workbook structure — 11 sheets, 125 questions, 3-panel dashboard

**Backward Compatibility:**
- v1.0 workbooks require Excel 2016+ (for dynamic array formulas in Dashboard)
- Previous assessments should be archived with date suffix before regenerating

---

## Document Assembly Instructions

**To create the complete ISMS-IMP-A.5.24-28.S3 v1.0 document:**

1. **Document Control** (from the S3 specification file header)
2. **PART I: USER COMPLETION GUIDE** (Assessment Overview through Assessment Timeline)
3. **PART II: TECHNICAL SPECIFICATION** (this section — Instructions through Appendix A.8)

**Final Document Structure:**
```
ISMS-IMP-A.5.24-28.S3 — Incident Response Capabilities Assessment v1.0

├── Document Control (Metadata, Version History, Related Documents)
│
├── PART I: USER COMPLETION GUIDE
│   ├── 1. Assessment Overview (Purpose, Scope, Prerequisites)
│   ├── 2. Assessment Workflow (High-Level Process, Timeline)
│   ├── 3. Section-by-Section Guidance (Q&A for all 125 questions)
│   ├── 4. Evidence Collection Guide
│   ├── 5. Common Mistakes to Avoid
│   └── 6. Assessment Timeline
│
└── PART II: TECHNICAL SPECIFICATION
    ├── Document Overview & Instructions
    ├── Sheet 1: Instructions & Legend
    ├── Sheet 2: Containment Capabilities (30Q)
    ├── Sheet 3: Eradication & Remediation (20Q)
    ├── Sheet 4: Recovery & Restoration (20Q)
    ├── Sheet 5: Communication (20Q)
    ├── Sheet 6: Resources & Authority (20Q)
    ├── Sheet 7: Playbook Effectiveness (15Q)
    ├── Sheet 8: Gap Analysis
    ├── Sheet 9: Evidence Register
    ├── Sheet 10: Dashboard
    ├── Sheet 11: Approval Sign-Off
    └── Appendix A (A.1–A.8: Developer Technical Reference)
```

**Quality Checks Before Finalising:**
- [ ] All 125 questions accounted for across sheet specifications
- [ ] Dashboard formulas reference correct sheet names and cell addresses
- [ ] Gap_Identified formula documented and matches script implementation
- [ ] Data validation rules match all dropdown options in script
- [ ] Conditional formatting colour codes match script implementation
- [ ] Python script function names match this specification
- [ ] Version Control section updated
- [ ] Cross-references to S1, S2, S4, S5 accurate

---

**END OF SPECIFICATION**

---

*"Study hard what interests you the most in the most undisciplined, irreverent and original manner possible."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->

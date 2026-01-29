# ISMS-IMP-A.5.23.S5 - Compliance Monitoring & Exit Planning
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.5.23: Cloud Services Security

---

## Document Overview

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S5 |
| **Assessment Area** | Compliance Monitoring & Exit Planning |
| **Related Policy** | ISMS-POL-A.5.19-23-S5 Section 8 (Exit Strategy) |
| **Evidence Prefix** | EV-CMP-### |
| **Approvers** | Compliance → Legal → CISO |
| **Review Cycle** | Quarterly (Compliance), Annual (Exit Planning) |

---

## Workbook Structure (9 Sheets)

| Sheet # | Name | Purpose |
|---------|------|---------|
| 1 | Instructions & Legend | Usage guidance, dropdowns, color legend |
| 2 | 2. Compliance Monitoring | Regulatory alignment, audit findings, cert tracking |
| 3 | 3. SLA Performance | SLA tracking, performance metrics, credits |
| 4 | 4. Exit Planning | Exit strategy, alternatives, migration estimates |
| 5 | 5. Data Portability | Export formats, migration complexity, lock-in |
| 6 | 6. Termination Readiness | Termination checklist, data deletion, revocation |
| 7 | 7. Summary Dashboard | Auto-calculated compliance metrics |
| 8 | 8. Evidence Register | Audit trail (EV-CMP-###) |
| 9 | 9. Approval Sign-Off | Compliance → Legal → CISO workflow |

---

## Sheet 1: Instructions & Legend

### Header Section
- **Title:** "ISMS-IMP-A.5.23.S5 – Compliance Monitoring & Exit Planning"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.5.23: Cloud Services Security"
- **Styling:** Dark blue header (003366), white text, centered

### Document Information Block (Row 4-11)
```
Document ID:           ISMS-IMP-A.5.23.S5
Assessment Area:       Compliance Monitoring & Exit Planning
Related Policy:        ISMS-POL-A.5.19-23-S5 Section 8
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly (Compliance) / Annual (Exit)
```

### How to Use This Workbook
1. Complete each assessment sheet (2-6) for all cloud services in scope
2. Use dropdown menus for standardized entries
3. Fill in yellow-highlighted cells with your information
4. If Status = Partial or Non-Compliant, complete Exception section
5. Provide evidence location/path for each assessment entry
6. Summary Dashboard auto-calculates compliance statistics
7. Maintain Evidence Register for audit traceability
8. Obtain sign-offs: Compliance → Legal → CISO

### Standard Dropdowns Reference
- **Service Type:** SaaS, IaaS, PaaS, Security Service, Cloud Storage, Other
- **Service Criticality:** Critical, High, Medium, Low
- **Data Classification:** Restricted, Confidential, Internal, Public, N/A
- **Compliance Framework:** GDPR, nFADP, SOX, HIPAA, PCI-DSS, ISO 27001, Multiple, N/A
- **Responsible Team:** Compliance, Legal, IT Ops, Procurement, Business Owners

---

## Base Columns (A-Q) - All Assessment Sheets

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | Cloud Service Name | 28 | Text | - |
| B | Vendor Name | 22 | Text | - |
| C | Service Type | 20 | Dropdown | SaaS, IaaS, PaaS, Security Service, Cloud Storage, Other |
| D | Compliance Framework | 20 | Dropdown | GDPR, nFADP, SOX, HIPAA, PCI-DSS, ISO 27001, Multiple, N/A |
| E | Service Criticality | 18 | Dropdown | Critical, High, Medium, Low |
| F | Data Classification | 20 | Dropdown | Restricted, Confidential, Internal, Public, N/A |
| G | *[Domain-specific]* | varies | varies | *See sheet specs* |
| H | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| I | Evidence Location | 30 | Text | - |
| J | Gap Description | 35 | Text | - |
| K | Remediation Needed | 16 | Dropdown | Yes, No |
| L | Exception ID | 14 | Text | - |
| M | Risk ID | 14 | Text | - |
| N | Compensating Controls | 30 | Text | - |
| O | Responsible Team/Owner | 20 | Dropdown | Compliance, Legal, IT Ops, Procurement, Business Owners |
| P | Target Remediation Date | 18 | Date | - |
| Q | Last Review Date | 18 | Date | - |

---

## Sheet 2: Compliance Monitoring

### Header
**Title:** "2. COMPLIANCE MONITORING"
**Policy Ref:** "Cloud services MUST maintain compliance with applicable regulations. Audit findings MUST be tracked to remediation. Certifications MUST be monitored for expiry. (Policy Section 8.1)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | Audit Status | 18 | Dropdown | Current, Findings Open, Overdue, Not Audited |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Last Audit Date | 16 | Date | - |
| S | Audit Findings Count | 18 | Number | - |
| T | Open Findings | 16 | Number | - |
| U | Remediation Status | 20 | Dropdown | Complete, In Progress, Not Started, Overdue |
| V | Next Audit Due | 16 | Date | - |
| W | Vendor Cert Status | 20 | Dropdown | Valid, Expiring Soon, Expired, Unknown |
| X | Cert Expiry Date | 16 | Date | - |

### Checklist Items (15 items)
```
☐ Applicable regulatory requirements identified per service
☐ Compliance requirements documented in service inventory
☐ Vendor compliance certifications obtained (SOC 2, ISO 27001, etc.)
☐ Certification validity periods tracked with alerts
☐ Audit schedule established for cloud services
☐ Audit findings tracked in central repository
☐ Remediation plans created for all findings
☐ Finding remediation tracked to closure
☐ Overdue findings escalated to management
☐ Compliance status reported to stakeholders
☐ Regulatory change monitoring in place
☐ Impact assessment performed for regulatory changes
☐ Evidence of compliance maintained and accessible
☐ Third-party audit reports reviewed annually
☐ Compliance dashboard available to stakeholders
```

---

## Sheet 3: SLA & Performance Monitoring

### Header
**Title:** "3. SLA & PERFORMANCE MONITORING"
**Policy Ref:** "Cloud service SLAs MUST be monitored continuously. SLA breaches MUST be documented and credits claimed where applicable. (Policy Section 8.2)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | SLA Status | 18 | Dropdown | Meeting SLA, At Risk, Breached, No SLA Defined |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Uptime SLA Target (%) | 18 | Number | - |
| S | Actual Uptime (%) | 18 | Number | - |
| T | SLA Breaches (YTD) | 18 | Number | - |
| U | Credits Claimed | 18 | Dropdown | Yes, No, N/A, Pending |
| V | Credit Amount | 16 | Text | - |
| W | Performance Review Freq | 20 | Dropdown | Monthly, Quarterly, Annual, Ad-Hoc |
| X | Last Performance Review | 18 | Date | - |

### Checklist Items (15 items)
```
☐ SLA targets documented for all critical services
☐ Uptime/availability SLA defined and measurable
☐ Response time SLAs defined for support tickets
☐ Resolution time SLAs defined for incidents
☐ SLA monitoring automated where possible
☐ SLA performance reported to service owners
☐ SLA breach notification process defined
☐ SLA breach root cause documented
☐ Credit claim process documented
☐ Credits tracked and claimed within timeframe
☐ SLA review included in vendor meetings
☐ SLA renegotiation triggers defined
☐ Performance trends analyzed quarterly
☐ Underperforming services flagged for review
☐ SLA documentation maintained and current
```

---

## Sheet 4: Exit Planning

### Header
**Title:** "4. EXIT PLANNING"
**Policy Ref:** "Exit strategies MUST be documented for all Critical/High services. Exit plans MUST be reviewed annually and tested where feasible. (Policy Section 8.3)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | Exit Plan Status | 20 | Dropdown | Documented, Draft, Not Started, N/A |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Exit Plan Documented | 18 | Dropdown | Yes, No, In Progress |
| S | Last Plan Review | 16 | Date | - |
| T | Alternative Identified | 20 | Dropdown | Yes, No, Multiple Options |
| U | Migration Estimate (Days) | 20 | Number | - |
| V | Migration Cost Estimate | 20 | Text | - |
| W | Exit Tested | 16 | Dropdown | Yes, No, Partial |
| X | Exit Complexity | 18 | Dropdown | Low, Medium, High, Critical |

### Checklist Items (15 items)
```
☐ Exit strategy documented for Critical/High services
☐ Exit triggers defined (vendor issues, cost, strategy change)
☐ Alternative providers/solutions identified
☐ Alternative provider assessment completed
☐ Migration effort estimated (time, cost, resources)
☐ Data extraction requirements documented
☐ Application dependencies mapped
☐ Integration points documented for migration
☐ Transition timeline template created
☐ Communication plan for exit scenarios
☐ Contract exit clauses reviewed and understood
☐ Notice period requirements documented
☐ Exit plan reviewed annually
☐ Exit plan tested or tabletop exercised
☐ Lessons learned from any exit incorporated
```

---

## Sheet 5: Data Portability

### Header
**Title:** "5. DATA PORTABILITY"
**Policy Ref:** "Data export capabilities MUST be verified and tested. Vendor lock-in risks MUST be assessed and mitigated. (Policy Section 8.4)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | Portability Rating | 18 | Dropdown | High, Medium, Low, Locked-In |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Export Format Available | 20 | Dropdown | Standard (CSV/JSON), Proprietary, API Only, None |
| S | Export Tested | 16 | Dropdown | Yes, No, Partial |
| T | Data Volume (GB) | 16 | Number | - |
| U | Migration Complexity | 18 | Dropdown | Low, Medium, High, Very High |
| V | Lock-In Risk | 16 | Dropdown | Low, Medium, High, Critical |
| W | Mitigation In Place | 18 | Dropdown | Yes, No, Partial |
| X | Last Export Test | 16 | Date | - |

### Checklist Items (15 items)
```
☐ Data export capabilities documented per service
☐ Export formats identified (CSV, JSON, XML, API, etc.)
☐ Proprietary format dependencies documented
☐ Data export tested and validated
☐ Export includes all required data fields
☐ Export includes metadata and audit trails
☐ Data transformation requirements documented
☐ API-based extraction capabilities verified
☐ Bulk export limitations documented
☐ Data volume growth projected for exit planning
☐ Vendor lock-in risks formally assessed
☐ Lock-in mitigation strategies documented
☐ Alternative data storage evaluated
☐ Data portability included in vendor contracts
☐ Regular export testing scheduled (annual minimum)
```

---

## Sheet 6: Service Termination Readiness

### Header
**Title:** "6. SERVICE TERMINATION READINESS"
**Policy Ref:** "Termination procedures MUST ensure complete data retrieval, secure deletion, and access revocation. Termination MUST be verified with evidence. (Policy Section 8.5)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | Termination Readiness | 20 | Dropdown | Ready, Partially Ready, Not Ready, N/A |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Notice Period (Days) | 18 | Number | - |
| S | Data Return SLA (Days) | 18 | Number | - |
| T | Deletion Cert Required | 18 | Dropdown | Yes, No, N/A |
| U | Deletion Cert Obtainable | 20 | Dropdown | Yes, No, Unknown |
| V | Access Revocation Plan | 20 | Dropdown | Documented, Not Documented |
| W | Termination Checklist | 20 | Dropdown | Complete, Partial, Not Created |
| X | Last Readiness Review | 18 | Date | - |

### Checklist Items (15 items)
```
☐ Contract termination notice period documented
☐ Termination for convenience clause verified
☐ Termination for cause triggers documented
☐ Data return process defined with vendor
☐ Data return timeline defined in contract
☐ Data deletion requirements specified
☐ Deletion certificate requirement in contract
☐ Deletion verification process defined
☐ Access revocation checklist created
☐ User account deprovisioning planned
☐ API key/service account revocation planned
☐ Integration disconnection sequence documented
☐ DNS/routing changes planned
☐ Post-termination audit planned
☐ Termination lessons learned process defined
```

---

## Sheet 7: Summary Dashboard

### Compliance Summary Table (Row 4-9)
| Assessment Area | Total Items | Compliant | Partial | Non-Compliant | N/A | Compliance % |
|-----------------|-------------|-----------|---------|---------------|-----|--------------|
| 2. Compliance Monitoring | =COUNTA(...) | =COUNTIF(...) | ... | ... | ... | =formula |
| 3. SLA Performance | ... | ... | ... | ... | ... | ... |
| 4. Exit Planning | ... | ... | ... | ... | ... | ... |
| 5. Data Portability | ... | ... | ... | ... | ... | ... |
| 6. Termination Readiness | ... | ... | ... | ... | ... | ... |
| **TOTAL** | =SUM(...) | =SUM(...) | ... | ... | ... | =AVERAGE(...) |

### Key Metrics Section
- Services with Open Audit Findings
- Services Breaching SLA
- Services Without Exit Plan
- High Lock-In Risk Services
- Services Not Termination Ready

### Exit Readiness Score
Formula-based weighted score across exit-related assessments.

---

## Sheet 8: Evidence Register

### Header
**Title:** "EVIDENCE REGISTER"
**Subtitle:** "Audit trail for compliance & exit assessments (EV-CMP-###)"

### Column Structure
| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Assessment Area | 22 |
| C | Cloud Service | 25 |
| D | Evidence Type | 22 |
| E | Description | 40 |
| F | Location/Path | 45 |
| G | Date Collected | 16 |
| H | Collected By | 20 |
| I | Verification Status | 20 |

**Evidence ID Format:** EV-CMP-001, EV-CMP-002, ... (auto-populated)
**Rows:** 5-104 (100 evidence entries)

---

## Sheet 9: Approval Sign-Off

### Workflow
```
Compliance Officer → Legal Counsel → CISO
```

### Sign-Off Blocks
Each block contains: Name, Title, Department, Date, Signature line, Comments

### Assessment Summary Fields
- Assessment Document: ISMS-IMP-A.5.23.S5 - Compliance Monitoring & Exit Planning
- Assessment Period: [USER INPUT]
- Overall Compliance Rate: ='Summary Dashboard'!G9
- Assessment Status: [Dropdown]

---

## Integration Points

### Related Documents
- ISMS-IMP-A.5.23.S1: Cloud Service Inventory
- ISMS-IMP-A.5.23.S2: Vendor Due Diligence
- ISMS-IMP-A.5.23.S3: Secure Configuration
- ISMS-IMP-A.5.23.S4: Ongoing Governance
- Contract Repository
- Regulatory Compliance Register

### Review Cycle
- Compliance Monitoring: Quarterly
- Exit Planning: Annual
- Triggered review on vendor changes or regulatory updates

---

**End of Specification**

*"Hope is not a strategy. Neither is an undocumented exit plan." — Every auditor ever*

--------------------------------------------------------------------------------------------------

# ISMS-IMP-A.5.23.S5 - Compliance Monitoring & Exit Planning
## Regulatory Update — DORA, NIS2, AI Act, CLOUD Act Enhancements

---

## Change Summary

| Change Type | Description |
|-------------|-------------|
| **Sheet Added** | NEW Sheet 7: Jurisdictional Risk Assessment (20 columns) |
| **Columns Added** | 3 new columns (Y-AA) on Exit Strategy sheet for DORA/NIS2 |
| **Checklists Updated** | +9 DORA items, +4 NIS2 items, +4 AI Act items, +9 Evaluation criteria |
| **Dashboard Updated** | +7 jurisdictional risk metrics, +5 exit readiness metrics |
| **Approval Updated** | +1 DPO sign-off section |
| **Instructions Updated** | Regulatory applicability guidance added |
| **Sheet Count** | 9 → 10 sheets |

---

## 1. New Dropdown Definitions

Add to Instructions & Legend sheet (after existing dropdown definitions):

### Regulatory Dropdown Lists
```
PROVIDER_HQ_JURISDICTION:
- Switzerland
- EU/EEA
- United Kingdom
- United States
- Other Adequate Country
- Non-Adequate Country

CLOUD_ACT_EXPOSURE:
- No Exposure
- Potential Exposure (US HQ)
- Mitigated (EU Data Boundary)
- Mitigated (Encryption + Key Control)
- Accepted Risk (Documented)
- Under Assessment

TRANSFER_MECHANISM:
- SCCs
- BCRs
- Adequacy Decision
- None
- N/A

RISK_LEVEL:
- Low
- Medium
- High
- Critical

YES_NO_PARTIAL_UNKNOWN:
- Yes
- No
- Partial
- Unknown

YES_NO_PLANNED:
- Yes
- No
- Planned

DORA_EXIT_READINESS:
- Full Exit Plan Documented
- Partial (In Progress)
- Not Started
- N/A (Not in scope)

NIS2_CONTINUITY_STATUS:
- Plan Tested & Validated
- Plan Documented (Untested)
- Plan In Progress
- No Plan
- N/A

AI_DECOMMISSION_STATUS:
- Ready (Data Extractable)
- Partial (Export Limitations)
- Not Ready (Vendor Lock-in)
- N/A (No AI Systems)
```

---

## 2. NEW Sheet: Jurisdictional Risk Assessment (Sheet 7)

**Insert as Sheet 7** — Existing sheets 7-9 become 8-10.

### Sheet Header
- **Title:** "JURISDICTIONAL RISK ASSESSMENT"
- **Subtitle:** "CLOUD Act, Data Sovereignty, and Cross-Border Transfer Analysis"
- **Warning text:** "⚠️ US-headquartered providers may be compelled to disclose data under CLOUD Act regardless of data location."

### Column Structure (A-T)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Assessment_ID | 14 | Text | Auto: JRA-001 |
| B | Cloud_Service_Name | 25 | Text | From Inventory |
| C | Provider_Name | 22 | Text | Free text |
| D | Provider_HQ_Country | 18 | Text | Free text |
| E | Provider_HQ_Jurisdiction | 20 | Dropdown | PROVIDER_HQ_JURISDICTION |
| F | US_Parent_Company | 14 | Dropdown | Yes/No/Unknown |
| G | CLOUD_Act_Applicability | 20 | Dropdown | CLOUD_ACT_EXPOSURE |
| H | Data_Processing_Locations | 25 | Text | Free text (list countries) |
| I | EU_Data_Boundary_Available | 18 | Dropdown | YES_NO_PLANNED |
| J | Customer_Managed_Keys | 16 | Dropdown | YES_NO_PLANNED |
| K | Legal_Challenge_Commitment | 18 | Dropdown | YES_NO_PARTIAL_UNKNOWN |
| L | Adequacy_Decision_Status | 18 | Text | Free text |
| M | Transfer_Mechanism | 16 | Dropdown | TRANSFER_MECHANISM |
| N | Risk_Level | 14 | Dropdown | RISK_LEVEL |
| O | Risk_Accepted_By | 18 | Text | Free text |
| P | Risk_Acceptance_Date | 16 | Date | Date picker |
| Q | Compensating_Controls | 28 | Text | Free text |
| R | Review_Date | 14 | Date | Date picker |
| S | Evidence_Reference | 20 | Text | EV-JRA-XXX |
| T | Notes | 30 | Text | Free text |

**Total Columns: 20 (A-T)**
**Data Rows: 7-30 (24 entries)**

### Jurisdictional Risk Checklist

| Item | Requirement | Status | Evidence |
|------|-------------|--------|----------|
| ☐ | Provider HQ jurisdiction identified and documented | ✅/⚠️/❌ | Vendor documentation |
| ☐ | US parent company status verified | ✅/⚠️/❌ | Corporate structure review |
| ☐ | CLOUD Act exposure assessed for US-nexus providers | ✅/⚠️/❌ | Legal review |
| ☐ | Data processing locations documented in DPA | ✅/⚠️/❌ | DPA review |
| ☐ | EU Data Boundary availability checked | ✅/⚠️/❌ | Vendor announcement/docs |
| ☐ | Customer-managed encryption keys option evaluated | ✅/⚠️/❌ | Technical documentation |
| ☐ | Legal challenge commitment verified | ✅/⚠️/❌ | Contract/Public statement |
| ☐ | Transfer mechanism documented (SCCs, BCRs, etc.) | ✅/⚠️/❌ | DPA |
| ☐ | Risk acceptance recorded if residual risk remains | ✅/⚠️/❌ | Risk register |
| ☐ | Compensating controls documented for high-risk providers | ✅/⚠️/❌ | Control documentation |

---

## 3. Exit Strategy Sheet Updates (Sheet 3)

### New Columns (Y-AA) — Add After Existing Column X

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| Y | DORA_Exit_Readiness | 20 | Dropdown | DORA_EXIT_READINESS |
| Z | NIS2_Continuity_Status | 20 | Dropdown | NIS2_CONTINUITY_STATUS |
| AA | AI_Decommission_Status | 22 | Dropdown | AI_DECOMMISSION_STATUS |

### Updated Exit Planning Checklist — Add DORA/NIS2/AI Act Items

**Existing items remain unchanged. ADD the following:**

#### DORA Exit Strategy Requirements (EXIT-DORA-01 to EXIT-DORA-09)

| Exit_ID | Requirement | DORA_Mandatory | NIS2_Mandatory |
|---------|-------------|----------------|----------------|
| EXIT-DORA-01 | Exit plan documented and maintained | Yes | No |
| EXIT-DORA-02 | Data portability mechanism tested | Yes | No |
| EXIT-DORA-03 | Service transition timeline defined (max 30 days) | Yes | No |
| EXIT-DORA-04 | Alternative provider identified | Yes | No |
| EXIT-DORA-05 | Exit costs estimated and budgeted | Yes | No |
| EXIT-DORA-06 | Data deletion procedure documented | Yes | Yes |
| EXIT-DORA-07 | Contract termination clauses reviewed | Yes | No |
| EXIT-DORA-08 | Exit plan tested within 12 months | Yes | No |
| EXIT-DORA-09 | Stakeholder communication plan prepared | Yes | Yes |

#### NIS2 Business Continuity Requirements (EXIT-NIS2-01 to EXIT-NIS2-04)

| Exit_ID | Requirement | DORA_Mandatory | NIS2_Mandatory |
|---------|-------------|----------------|----------------|
| EXIT-NIS2-01 | Business continuity plan covers cloud service failure | No | Yes |
| EXIT-NIS2-02 | Backup service provider identified | No | Yes |
| EXIT-NIS2-03 | Recovery time objective (RTO) defined and tested | No | Yes |
| EXIT-NIS2-04 | Annual continuity testing documented | No | Yes |

#### AI Act Decommissioning Requirements (EXIT-AI-01 to EXIT-AI-04)

| Exit_ID | Requirement | AI_Act_Mandatory |
|---------|-------------|------------------|
| EXIT-AI-01 | AI model data extraction procedure documented | Yes (if AI used) |
| EXIT-AI-02 | AI training data ownership verified | Yes (if AI used) |
| EXIT-AI-03 | AI system decommissioning impact assessed | Yes (if high-risk) |
| EXIT-AI-04 | Alternative AI system identified (if critical) | Yes (if high-risk) |

---

## 4. Evaluation Criteria Updates

### Add to Existing Evaluation Criteria (All Assessment Sheets)

#### Regulatory Evaluation Criteria (EVAL-REG-01 to EVAL-REG-06)

| Criteria_ID | Category | Requirement |
|-------------|----------|-------------|
| EVAL-REG-01 | Regulatory | Provider discloses HQ jurisdiction and legal entity structure |
| EVAL-REG-02 | Regulatory | Provider discloses all data processing locations |
| EVAL-REG-03 | Regulatory | Provider offers EU Data Boundary or regional commitment |
| EVAL-REG-04 | Regulatory | Provider supports customer-managed encryption keys |
| EVAL-REG-05 | Regulatory | Provider commits to challenge government data requests |
| EVAL-REG-06 | Regulatory | Provider discloses sub-processor jurisdictions |

#### AI Act Evaluation Criteria (EVAL-AI-01 to EVAL-AI-03)

| Criteria_ID | Category | Requirement |
|-------------|----------|-------------|
| EVAL-AI-01 | AI Act | AI system risk classification documented |
| EVAL-AI-02 | AI Act | High-risk AI system has conformity assessment |
| EVAL-AI-03 | AI Act | AI transparency requirements met |

---

## 5. Dashboard Updates (Sheet 8 — Previously Sheet 7)

### Add: Table 2 — Jurisdictional & CLOUD Act Risk Summary

Insert after Table 1 (Compliance by Assessment Area):

| Row | Metric | Formula | Status Formula |
|-----|--------|---------|----------------|
| Header | JURISDICTIONAL & CLOUD ACT RISK SUMMARY | (merged, dark blue) | |
| 1 | US-HQ Providers (CLOUD Act Scope) | `=COUNTIF('7. Jurisdictional Risk'!E7:E30,"United States")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 2 | Providers with US Parent Company | `=COUNTIF('7. Jurisdictional Risk'!F7:F30,"Yes")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 3 | CLOUD Act Potential Exposure (Unmitigated) | `=COUNTIF('7. Jurisdictional Risk'!G7:G30,"Potential*")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 4 | CLOUD Act Mitigated | `=COUNTIF('7. Jurisdictional Risk'!G7:G30,"Mitigated*")` | Info |
| 5 | High/Critical Jurisdictional Risk | `=COUNTIF('7. Jurisdictional Risk'!N7:N30,"High")+COUNTIF('7. Jurisdictional Risk'!N7:N30,"Critical")` | `=IF(B>0,"❌ Action","✅ OK")` |
| 6 | Providers Without EU Data Boundary | `=COUNTIF('7. Jurisdictional Risk'!I7:I30,"No")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 7 | Providers Without Customer-Managed Keys | `=COUNTIF('7. Jurisdictional Risk'!J7:J30,"No")` | `=IF(B>0,"⚠️ Review","✅ OK")` |

### Add: Table 3 — Exit Readiness & Continuity Status

Insert after Table 2:

| Row | Metric | Formula | Status Formula |
|-----|--------|---------|----------------|
| Header | EXIT READINESS & CONTINUITY STATUS | (merged, dark blue) | |
| 1 | DORA Exit Plans Not Started | `=COUNTIF('3. Exit Strategy'!Y7:Y30,"Not Started")` | `=IF(B>0,"❌ Action","✅ OK")` |
| 2 | DORA Exit Plans Untested (>12 months) | `=COUNTIF('3. Exit Strategy'!Y7:Y30,"Partial*")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 3 | NIS2 Continuity Plans Untested | `=COUNTIF('3. Exit Strategy'!Z7:Z30,"*Untested*")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 4 | NIS2 No Continuity Plan | `=COUNTIF('3. Exit Strategy'!Z7:Z30,"No Plan")` | `=IF(B>0,"❌ Action","✅ OK")` |
| 5 | AI Systems Not Ready for Decommission | `=COUNTIF('3. Exit Strategy'!AA7:AA30,"Not Ready*")` | `=IF(B>0,"⚠️ Review","✅ OK")` |

---

## 6. Instructions Sheet Updates

### Add: Regulatory Applicability Section

Insert after "Acceptable Evidence" section:
```
REGULATORY COMPLIANCE

This workbook includes updated requirements for:
- DORA (Digital Operational Resilience Act) - Exit strategy and portability
- NIS2 (Network and Information Security Directive 2) - Business continuity
- EU AI Act - AI system decommissioning procedures
- US CLOUD Act - Jurisdictional risk assessment (NEW Sheet 7)

REGULATORY APPLICABILITY GUIDANCE

| If You Are...                        | Complete These Fields              |
|--------------------------------------|------------------------------------|
| EU Financial Entity (DORA scope)     | All DORA fields (mandatory)        |
| EU Essential/Important Entity (NIS2) | All NIS2 fields (mandatory)        |
| Using AI Systems from cloud vendors  | All AI Act decommission fields     |
| Using US-HQ Providers                | Sheet 7 Jurisdictional Risk (all)  |
| None of the Above                    | Mark as "N/A" or "Not Applicable"  |

EXIT PLANNING CONSIDERATIONS

For compliance monitoring and exit planning:
- DORA: Exit plans must be tested within 12 months
- DORA: Service transition timeline max 30 days post-termination
- NIS2: Annual business continuity testing mandatory
- AI Act: Document AI model/data extraction procedures
- Maintain evidence of data portability testing
- Identify alternative providers BEFORE signing contracts
- Budget for exit costs (data migration, dual-running, etc.)
```

### Update: How to Use This Workbook

Change instruction count and update text:
```
5. Complete Jurisdictional Risk sheet (7) for all US-nexus providers (NEW)
6. Document DORA exit plan and test results if in scope
7. Test NIS2 business continuity plans annually if applicable
8. Document AI system decommissioning procedures if AI used
```

### Update: Acceptable Evidence

Add new items:
```
✓ DORA exit plan documentation (with test results)
✓ Data portability test report (successful extraction)
✓ Alternative provider identification (documented)
✓ NIS2 business continuity test report (annual)
✓ Recovery time objective (RTO) validation
✓ AI model extraction procedure (if AI systems used)
✓ AI training data ownership verification
✓ Jurisdictional risk assessment (for US-nexus providers)
✓ Risk acceptance form (signed by CISO/DPO)
```

---

## 7. Approval Sign-Off Updates (Sheet 10 — Previously Sheet 9)

### Add: Data Protection Officer Review Section

Insert between Compliance Review and CISO Approval:

| Field | Type |
|-------|------|
| **DATA PROTECTION OFFICER REVIEW** | Section header (blue) |
| Reviewed By (DPO): | Yellow input |
| Review Date: | Yellow input |
| Data Protection Compliance: | Dropdown: Compliant/Partially Compliant/Non-Compliant |
| Cross-Border Transfer Status: | Dropdown: Approved/Approved with SCCs/Requires TIA/Rejected |
| DPO Comments: | Yellow input |

### Update: Assessment Summary

Add new fields:

| Field | Formula/Value |
|-------|---------------|
| Jurisdictional Risks Identified: | `='8. Summary Dashboard'!B20` |
| DORA Exit Plans Not Started: | `='8. Summary Dashboard'!B28` |
| NIS2 Continuity Plans Untested: | `='8. Summary Dashboard'!B30` |
| AI Systems Not Exit-Ready: | `='8. Summary Dashboard'!B32` |

---

## 8. Updated Sheet Structure Summary

### Before (v1.0) — 9 Sheets

| Sheet | Name |
|-------|------|
| 1 | Instructions & Legend |
| 2 | Compliance Audit Log |
| 3 | Exit Strategy |
| 4 | Data Portability Testing |
| 5 | Vendor SLA Monitoring |
| 6 | Regulatory Reporting |
| 7 | Summary Dashboard |
| 8 | Evidence Register |
| 9 | Approval Sign-Off |

### After — 10 Sheets

| Sheet | Name | Change |
|-------|------|--------|
| 1 | Instructions & Legend | UPDATED |
| 2 | Compliance Audit Log | Unchanged |
| 3 | Exit Strategy | +3 columns (Y-AA), +17 checklist items |
| 4 | Data Portability Testing | Unchanged |
| 5 | Vendor SLA Monitoring | Unchanged |
| 6 | Regulatory Reporting | Unchanged |
| 7 | **Jurisdictional Risk** | **NEW** |
| 8 | Summary Dashboard | +12 metrics, renumbered |
| 9 | Evidence Register | +8 evidence types, renumbered |
| 10 | Approval Sign-Off | +DPO section, renumbered |

---

## 9. Validation Requirements (Updated)

**Pre-Distribution Checks:**

- [ ] ✅ All **10 sheets** present (was 9)
- [ ] ✅ Base 17 columns (A-Q) configured on assessment sheets
- [ ] ✅ Extended columns present per sheet type
- [ ] ✅ **NEW: Jurisdictional Risk sheet has 20 columns (A-T)**
- [ ] ✅ **NEW: Exit Strategy has columns Y-AA (DORA/NIS2/AI Act)**
- [ ] ✅ Dropdowns configured (25+ validation types) — was 19
- [ ] ✅ **NEW: 9 regulatory dropdowns configured**
- [ ] ✅ Dashboard formulas link to assessment sheets
- [ ] ✅ **NEW: Dashboard includes jurisdictional + exit readiness tables**
- [ ] ✅ Evidence Register has auto-generated IDs (EV-CME-XXX)
- [ ] ✅ **NEW: Evidence Register includes exit planning evidence types**
- [ ] ✅ Approval Sign-Off links to dashboard metrics
- [ ] ✅ **NEW: DPO sign-off section present**
- [ ] ✅ No Excel repair warnings (run style_object_checker.py)

---

## 10. Generator Script Impact

**File:** `generate_a523_5_compliance_exit.py`

**Changes Required:**

1. Add 9 new dropdown list constants (regulatory dropdowns)
2. Update `create_workbook()` — add "7. Jurisdictional Risk" sheet, renumber 8-10
3. Add new function `create_7_jurisdictional_risk()`
4. Add `get_jurisdictional_columns()` — 20 columns
5. Add `create_jurisdictional_validations()` — 7 validation types
6. Update `get_extended_columns_exit_strategy()` — add Y-AA
7. Update `get_checklist_exit_strategy()` — add DORA/NIS2/AI Act items
8. Update `create_8_summary_dashboard()` — add 2 new metrics tables
9. Update `create_9_evidence_register()` — add evidence types
10. Update `create_10_approval_signoff()` — add DPO section
11. Update `main()` — 10 sheets, version 2.0

---

## 11. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author Name] | Initial workbook specification |

---

**END OF REGULATORY UPDATE SPECIFICATION**

*"Exit planning: Because 'till death do us part' is not a valid cloud strategy." — Every IT architect who learned the hard way*
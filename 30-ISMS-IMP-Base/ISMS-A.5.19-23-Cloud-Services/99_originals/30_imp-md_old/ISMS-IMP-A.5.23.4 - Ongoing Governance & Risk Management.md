# ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.5.23: Cloud Services Security

---

## Document Overview

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S4 |
| **Assessment Area** | Ongoing Cloud Service Governance & Risk Management |
| **Related Policy** | ISMS-POL-A.5.19-23-S5 Section 6 (Operational Management) |
| **Evidence Prefix** | EV-GOV-### |
| **Approvers** | IT Ops → Compliance → CISO |
| **Review Cycle** | Quarterly |

---

## Workbook Structure (9 Sheets)

| Sheet # | Name | Purpose |
|---------|------|---------|
| 1 | Instructions & Legend | Usage guidance, dropdowns, color legend |
| 2 | 2. Access Review | Quarterly access reviews, privilege recertification |
| 3 | 3. Change Management | Provider/org changes, emergency changes |
| 4 | 4. Incident Management | Detection, response, lessons learned |
| 5 | 5. Business Continuity | BC/DR plans, failover testing, RTO/RPO |
| 6 | 6. Vendor Risk Monitoring | Ongoing risk assessment, security posture |
| 7 | 7. Summary Dashboard | Auto-calculated compliance metrics |
| 8 | 8. Evidence Register | Audit trail (EV-GOV-###) |
| 9 | 9. Approval Sign-Off | IT Ops → Compliance → CISO workflow |

---

## Sheet 1: Instructions & Legend

### Header Section
- **Title:** "ISMS-IMP-A.5.23.S4 – Ongoing Governance & Risk Management"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.5.23: Cloud Services Security"
- **Styling:** Dark blue header (003366), white text, centered

### Document Information Block (Row 4-11)
```
Document ID:           ISMS-IMP-A.5.23.S4
Assessment Area:       Ongoing Cloud Service Governance & Risk Management
Related Policy:        ISMS-POL-A.5.19-23-S5 Section 6
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

### How to Use This Workbook (Row 13+)
1. Complete each assessment sheet (2-6) for all cloud services in scope
2. Use dropdown menus for standardized entries
3. Fill in yellow-highlighted cells with your information
4. If Status = Partial or Non-Compliant, complete Exception section
5. Provide evidence location/path for each assessment entry
6. Summary Dashboard auto-calculates compliance statistics
7. Maintain Evidence Register for audit traceability
8. Obtain sign-offs: IT Ops → Compliance → CISO

### Status Legend
| Color | Status | Meaning |
|-------|--------|---------|
| Green | ✅ Compliant | Fully meets requirements |
| Yellow | ⚠️ Partial | Partially implemented, gaps exist |
| Red | ❌ Non-Compliant | Not implemented or major gaps |
| Gray | N/A | Not applicable to this service |

### Standard Dropdowns Reference
- **Service Type:** SaaS, IaaS, PaaS, Security Service, Cloud Storage, Other
- **Service Criticality:** Critical, High, Medium, Low
- **Data Classification:** Restricted, Confidential, Internal, Public, N/A
- **Review Period:** Q1, Q2, Q3, Q4, Annual, Ad-Hoc
- **Responsible Team:** IT Ops, Compliance, Risk Management, Security, Business Owners

---

## Base Columns (A-Q) - All Assessment Sheets

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | Cloud Service Name | 28 | Text | - |
| B | Vendor Name | 22 | Text | - |
| C | Service Type | 20 | Dropdown | SaaS, IaaS, PaaS, Security Service, Cloud Storage, Other |
| D | Review Period | 16 | Dropdown | Q1, Q2, Q3, Q4, Annual, Ad-Hoc |
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
| O | Responsible Team/Owner | 20 | Dropdown | IT Ops, Compliance, Risk Management, Security, Business Owners |
| P | Target Remediation Date | 18 | Date | - |
| Q | Last Review Date | 18 | Date | - |

---

## Sheet 2: Access Review & Recertification

### Header
**Title:** "2. ACCESS REVIEW & RECERTIFICATION"
**Policy Ref:** "Access to cloud services MUST be reviewed quarterly. Orphan accounts MUST be disabled within 24 hours of detection. (Policy Section 6.1)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | Review Type | 18 | Dropdown | Full Recertification, Privileged Access, Standard Access, Service Account |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Last Review Date | 16 | Date | - |
| S | Review Outcome | 18 | Dropdown | Passed, Issues Found, Overdue, Not Started |
| T | Total Accounts Reviewed | 18 | Number | - |
| U | Orphan Accounts Found | 18 | Number | - |
| V | Excessive Privileges Found | 20 | Number | - |
| W | Accounts Remediated | 18 | Number | - |
| X | Next Review Due | 16 | Date | - |

### Checklist Items (15 items)
```
☐ Quarterly access review schedule documented and communicated
☐ Access review covers all user types (employees, contractors, service accounts)
☐ Privileged access reviewed separately with enhanced scrutiny
☐ Review includes comparison against job role/least privilege
☐ Orphan account detection process automated or scheduled
☐ Orphan accounts disabled within 24 hours of detection
☐ Terminated user access revoked within SLA (24 hours)
☐ Service account ownership verified and documented
☐ Shared account usage minimized and justified
☐ MFA status verified during access review
☐ External/guest access reviewed and time-limited
☐ Access review findings documented with evidence
☐ Non-compliance escalated to service owner
☐ Review completion rates tracked and reported
☐ Access review process covers all cloud services in inventory
```

---

## Sheet 3: Change Management

### Header
**Title:** "3. CHANGE MANAGEMENT"
**Policy Ref:** "All cloud service changes MUST follow change management process. Emergency changes require post-implementation review within 48 hours. (Policy Section 6.2)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | Change Type | 18 | Dropdown | Provider Change, Config Change, Integration Change, Emergency Change, Scheduled Maintenance |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Change Count (Period) | 18 | Number | - |
| S | Impact Level | 16 | Dropdown | Critical, High, Medium, Low |
| T | Approval Status | 18 | Dropdown | Approved, Pending, Rejected, Emergency |
| U | Rollback Plan Documented | 20 | Dropdown | Yes, No, N/A |
| V | Rollback Tested | 16 | Dropdown | Yes, No, N/A |
| W | Post-Change Review Done | 20 | Dropdown | Yes, No, Pending |
| X | Security Impact Assessed | 20 | Dropdown | Yes, No, N/A |

### Checklist Items (15 items)
```
☐ Change management process documented for cloud services
☐ Provider change notifications monitored and assessed
☐ Configuration changes require security review before approval
☐ Integration changes assessed for data flow impact
☐ Emergency change process defined with post-review requirement
☐ Emergency changes reviewed within 48 hours
☐ Rollback procedures documented for critical changes
☐ Rollback procedures tested before go-live (critical changes)
☐ Change calendar maintained and communicated
☐ Change conflicts identified and resolved
☐ Security impact assessment required for all changes
☐ Change audit trail maintained in ticketing system
☐ Failed changes documented with root cause
☐ Change success metrics tracked (success rate, rollback rate)
☐ Provider maintenance windows tracked and planned for
```

---

## Sheet 4: Incident & Problem Management

### Header
**Title:** "4. INCIDENT & PROBLEM MANAGEMENT"
**Policy Ref:** "Cloud service incidents MUST be detected, reported, and resolved per incident management procedures. Lessons learned MUST be documented. (Policy Section 6.3)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | Incident Severity | 18 | Dropdown | P1-Critical, P2-High, P3-Medium, P4-Low |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Incident Count (Period) | 18 | Number | - |
| S | MTTR (Hours) | 14 | Number | - |
| T | Root Cause Documented | 20 | Dropdown | Yes, No, Pending |
| U | Playbook Updated | 16 | Dropdown | Yes, No, N/A |
| V | Vendor Notified | 16 | Dropdown | Yes, No, N/A |
| W | Customer Impact | 18 | Dropdown | Yes, No, Unknown |
| X | Lessons Learned Captured | 20 | Dropdown | Yes, No, Pending |

### Checklist Items (15 items)
```
☐ Incident detection mechanisms in place for cloud services
☐ Alerting thresholds defined and tuned
☐ Incident classification aligned with org severity matrix
☐ Escalation paths defined for cloud service incidents
☐ Vendor notification procedures documented
☐ Vendor incident response SLAs tracked
☐ Internal incident response playbooks exist per service
☐ Playbooks reviewed/updated after incidents
☐ Root cause analysis performed for P1/P2 incidents
☐ Lessons learned documented and shared
☐ Problem management process identifies recurring issues
☐ Known error database maintained for cloud services
☐ Incident metrics reported to management
☐ MTTR/MTTD tracked per service
☐ Post-incident reviews conducted within defined timeframe
```

---

## Sheet 5: Business Continuity

### Header
**Title:** "5. BUSINESS CONTINUITY"
**Policy Ref:** "BC/DR plans MUST exist for Critical and High services. Failover MUST be tested annually minimum. RTO/RPO MUST be verified. (Policy Section 6.4)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | BC Tier | 16 | Dropdown | Tier 1 (<4hr), Tier 2 (<24hr), Tier 3 (<72hr), Tier 4 (Best Effort) |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Last Test Date | 16 | Date | - |
| S | Test Result | 16 | Dropdown | Passed, Failed, Partial, Not Tested |
| T | RTO Target (Hours) | 16 | Number | - |
| U | RTO Achieved (Hours) | 18 | Number | - |
| V | RPO Target (Hours) | 16 | Number | - |
| W | RPO Achieved (Hours) | 18 | Number | - |
| X | Next Test Due | 16 | Date | - |

### Checklist Items (15 items)
```
☐ BC/DR plan documented for Critical/High services
☐ Vendor BC/DR capabilities verified and documented
☐ RTO requirements defined per service criticality
☐ RPO requirements defined per data classification
☐ Failover procedures documented and accessible
☐ Failover tested annually (minimum)
☐ Test results documented with evidence
☐ RTO achievement verified during tests
☐ RPO achievement verified during tests
☐ Data backup restoration tested
☐ Multi-region/availability zone strategy documented
☐ Single points of failure identified and mitigated
☐ Communication plan exists for BC events
☐ Vendor dependency chain mapped for BC planning
☐ BC plan reviewed after significant changes
```

---

## Sheet 6: Vendor Risk Monitoring

### Header
**Title:** "6. VENDOR RISK MONITORING"
**Policy Ref:** "Cloud vendor risk MUST be monitored continuously. Security posture changes MUST trigger reassessment. Certification expiry MUST be tracked. (Policy Section 6.5)"

### Column G Definition
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| G | Risk Rating | 16 | Dropdown | Critical, High, Medium, Low, Minimal |

### Extended Columns (R-X)
| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Risk Score Trend | 18 | Dropdown | Improving, Stable, Degrading, Unknown |
| S | Security Incidents (YTD) | 20 | Number | - |
| T | Cert Expiry Tracked | 18 | Dropdown | Yes, No, N/A |
| U | Next Cert Expiry | 16 | Date | - |
| V | Financial Health | 18 | Dropdown | Strong, Stable, Concerning, Unknown |
| W | Last Assessment Date | 18 | Date | - |
| X | Reassessment Trigger Met | 20 | Dropdown | Yes, No |

### Checklist Items (15 items)
```
☐ Vendor risk assessment performed at onboarding
☐ Annual vendor risk reassessment scheduled
☐ Risk scoring methodology documented and consistent
☐ Security certifications tracked (ISO 27001, SOC 2, etc.)
☐ Certification expiry dates monitored with alerts
☐ Vendor security incidents monitored via news/feeds
☐ Vendor breach notification process documented
☐ Financial health indicators monitored for critical vendors
☐ Vendor concentration risk assessed
☐ Sub-processor changes tracked and assessed
☐ Geopolitical risk factors considered
☐ Vendor security questionnaire refreshed periodically
☐ Risk rating changes trigger stakeholder notification
☐ High-risk vendors subject to enhanced monitoring
☐ Vendor risk dashboard available to stakeholders
```

---

## Sheet 7: Summary Dashboard

### Compliance Summary Table (Row 4-9)
| Assessment Area | Total Items | Compliant | Partial | Non-Compliant | N/A | Compliance % |
|-----------------|-------------|-----------|---------|---------------|-----|--------------|
| 2. Access Review | =COUNTA(...) | =COUNTIF(...) | ... | ... | ... | =formula |
| 3. Change Management | ... | ... | ... | ... | ... | ... |
| 4. Incident Management | ... | ... | ... | ... | ... | ... |
| 5. Business Continuity | ... | ... | ... | ... | ... | ... |
| 6. Vendor Risk Monitoring | ... | ... | ... | ... | ... | ... |
| **TOTAL** | =SUM(...) | =SUM(...) | ... | ... | ... | =AVERAGE(...) |

### Key Metrics Section (Row 12+)
- Total Cloud Services Assessed
- Services Requiring Remediation
- Overdue Access Reviews Count
- Open Incidents Count
- BC Tests Overdue Count
- High-Risk Vendors Count

### Overall Governance Health Score (Row 25+)
Formula-based weighted score across all assessment areas.

---

## Sheet 8: Evidence Register

### Header
**Title:** "EVIDENCE REGISTER"
**Subtitle:** "Audit trail for governance assessments (EV-GOV-###)"

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

**Evidence ID Format:** EV-GOV-001, EV-GOV-002, ... (auto-populated)
**Rows:** 5-104 (100 evidence entries)

---

## Sheet 9: Approval Sign-Off

### Workflow
```
IT Operations Manager → Compliance Officer → CISO
```

### Sign-Off Blocks
Each block contains: Name, Title, Department, Date, Signature line, Comments

### Assessment Summary Fields
- Assessment Document: ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management
- Assessment Period: [USER INPUT]
- Overall Compliance Rate: ='Summary Dashboard'!G9
- Assessment Status: [Dropdown: Draft, Final, Requires Remediation, Re-assessment Required]

---

## Integration Points

### Related Documents
- ISMS-IMP-A.5.23.S1: Cloud Service Inventory
- ISMS-IMP-A.5.23.S2: Vendor Due Diligence
- ISMS-IMP-A.5.23.S3: Secure Configuration
- ISMS-IMP-A.5.23.S5: Compliance & Exit Planning
- Risk Register (link Exception IDs)
- Change Management System
- Incident Management System

### Review Cycle
- Quarterly assessment updates
- Annual full reassessment
- Triggered reassessment on major changes/incidents

---

**End of Specification**

*"In God we trust. All others must bring data." — W. Edwards Deming*

--------------------------------------------------------------------------------------------------

# ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management
## Regulatory Update — DORA, NIS2, AI Act, CLOUD Act Enhancements

---

## Change Summary

| Change Type | Description |
|-------------|-------------|
| **Sheet Added** | NEW Sheet 8: Jurisdictional Risk Assessment (20 columns) |
| **Columns Added** | 4 new columns (Y-AB) on Risk Register sheet for DORA/NIS2/AI Act |
| **Checklists Updated** | +8 DORA items, +5 NIS2 items, +6 AI Act items, +9 Evaluation criteria |
| **Dashboard Updated** | +7 jurisdictional risk metrics, +4 regulatory risk metrics |
| **Approval Updated** | +1 DPO sign-off section |
| **Instructions Updated** | Regulatory applicability guidance added |
| **Sheet Count** | 10 → 11 sheets |

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

DORA_RISK_MONITORING:
- Continuous Monitoring
- Quarterly Reviews
- Annual Reviews
- Not Monitored
- N/A (Not in scope)

NIS2_INCIDENT_CLASSIFICATION:
- Significant (≤24h notification)
- Major (≤72h notification)
- Minor (No notification required)
- Under Assessment
- N/A

AI_RISK_MONITORING_STATUS:
- Active Monitoring
- Periodic Review
- No Monitoring Required
- Monitoring Pending
- N/A

REGULATORY_RISK_OWNER:
- CISO
- CRO (Chief Risk Officer)
- DPO
- Legal/Compliance
- Business Unit Owner
- Other
```

---

## 2. NEW Sheet: Jurisdictional Risk Assessment (Sheet 8)

**Insert as Sheet 8** — Existing sheets 8-10 become 9-11.

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

## 3. Risk Register Sheet Updates (Sheet 2)

### New Columns (Y-AB) — Add After Existing Column X

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| Y | DORA_Risk_Monitoring | 20 | Dropdown | DORA_RISK_MONITORING |
| Z | NIS2_Incident_Classification | 22 | Dropdown | NIS2_INCIDENT_CLASSIFICATION |
| AA | AI_Risk_Monitoring_Status | 22 | Dropdown | AI_RISK_MONITORING_STATUS |
| AB | Regulatory_Risk_Owner | 20 | Dropdown | REGULATORY_RISK_OWNER |

### Updated Risk Register Checklist — Add DORA/NIS2/AI Act Items

**Existing items remain unchanged. ADD the following:**

#### DORA Risk Management Requirements (RISK-DORA-01 to RISK-DORA-08)

| Risk_ID | Requirement | DORA_Mandatory | NIS2_Mandatory |
|---------|-------------|----------------|----------------|
| RISK-DORA-01 | ICT risk identification documented and maintained | Yes | No |
| RISK-DORA-02 | Third-party ICT risk assessment conducted | Yes | Yes |
| RISK-DORA-03 | ICT concentration risk assessed (vendor dependencies) | Yes | No |
| RISK-DORA-04 | Business continuity plans tested annually | Yes | Yes |
| RISK-DORA-05 | ICT risk register reviewed quarterly | Yes | No |
| RISK-DORA-06 | Critical ICT services identified and documented | Yes | Yes |
| RISK-DORA-07 | Recovery time objectives (RTO) defined and tested | Yes | Yes |
| RISK-DORA-08 | Vendor exit strategies documented | Yes | No |

#### NIS2 Risk Management Requirements (RISK-NIS2-01 to RISK-NIS2-05)

| Risk_ID | Requirement | DORA_Mandatory | NIS2_Mandatory |
|---------|-------------|----------------|----------------|
| RISK-NIS2-01 | Supply chain security risks assessed | No | Yes |
| RISK-NIS2-02 | Incident response plan tested and updated | No | Yes |
| RISK-NIS2-03 | Business continuity management system maintained | No | Yes |
| RISK-NIS2-04 | Cyber hygiene practices implemented | No | Yes |
| RISK-NIS2-05 | Security awareness training documented | No | Yes |

#### AI Act Risk Management Requirements (RISK-AI-01 to RISK-AI-06)

| Risk_ID | Requirement | AI_Act_Mandatory |
|---------|-------------|------------------|
| RISK-AI-01 | AI system risks identified and documented | Yes (if AI used) |
| RISK-AI-02 | High-risk AI systems under continuous monitoring | Yes (if high-risk) |
| RISK-AI-03 | AI system bias and discrimination risks assessed | Yes (if high-risk) |
| RISK-AI-04 | AI transparency and explainability documented | Yes (if AI used) |
| RISK-AI-05 | Human oversight mechanisms operational | Yes (if high-risk) |
| RISK-AI-06 | AI incident response procedures defined | Yes (if high-risk) |

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

## 5. Dashboard Updates (Sheet 9 — Previously Sheet 8)

### Add: Table 2 — Jurisdictional & CLOUD Act Risk Summary

Insert after Table 1 (Compliance by Assessment Area):

| Row | Metric | Formula | Status Formula |
|-----|--------|---------|----------------|
| Header | JURISDICTIONAL & CLOUD ACT RISK SUMMARY | (merged, dark blue) | |
| 1 | US-HQ Providers (CLOUD Act Scope) | `=COUNTIF('8. Jurisdictional Risk'!E7:E30,"United States")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 2 | Providers with US Parent Company | `=COUNTIF('8. Jurisdictional Risk'!F7:F30,"Yes")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 3 | CLOUD Act Potential Exposure (Unmitigated) | `=COUNTIF('8. Jurisdictional Risk'!G7:G30,"Potential*")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 4 | CLOUD Act Mitigated | `=COUNTIF('8. Jurisdictional Risk'!G7:G30,"Mitigated*")` | Info |
| 5 | High/Critical Jurisdictional Risk | `=COUNTIF('8. Jurisdictional Risk'!N7:N30,"High")+COUNTIF('8. Jurisdictional Risk'!N7:N30,"Critical")` | `=IF(B>0,"❌ Action","✅ OK")` |
| 6 | Providers Without EU Data Boundary | `=COUNTIF('8. Jurisdictional Risk'!I7:I30,"No")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 7 | Providers Without Customer-Managed Keys | `=COUNTIF('8. Jurisdictional Risk'!J7:J30,"No")` | `=IF(B>0,"⚠️ Review","✅ OK")` |

### Add: Table 3 — Regulatory Risk Monitoring Status

Insert after Table 2:

| Row | Metric | Formula | Status Formula |
|-----|--------|---------|----------------|
| Header | REGULATORY RISK MONITORING STATUS | (merged, dark blue) | |
| 1 | DORA Risks Not Monitored | `=COUNTIF('2. Risk Register'!Y7:Y30,"Not Monitored")` | `=IF(B>0,"❌ Action","✅ OK")` |
| 2 | NIS2 Significant Incidents (Require ≤24h notification) | `=COUNTIF('2. Risk Register'!Z7:Z30,"Significant*")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 3 | AI Systems Requiring Active Monitoring | `=COUNTIF('2. Risk Register'!AA7:AA30,"Active Monitoring")` | Info |
| 4 | Regulatory Risks Without Assigned Owner | `=COUNTIF('2. Risk Register'!AB7:AB30,"")` | `=IF(B>0,"❌ Action","✅ OK")` |

---

## 6. Instructions Sheet Updates

### Add: Regulatory Applicability Section

Insert after "Acceptable Evidence" section:
```
REGULATORY COMPLIANCE

This workbook includes updated requirements for:
- DORA (Digital Operational Resilience Act) - ICT risk management
- NIS2 (Network and Information Security Directive 2) - Incident management
- EU AI Act - AI system risk monitoring
- US CLOUD Act - Jurisdictional risk assessment (NEW Sheet 8)

REGULATORY APPLICABILITY GUIDANCE

| If You Are...                        | Complete These Fields              |
|--------------------------------------|------------------------------------|
| EU Financial Entity (DORA scope)     | All DORA fields (mandatory)        |
| EU Essential/Important Entity (NIS2) | All NIS2 fields (mandatory)        |
| Operating AI Systems from vendors    | All AI Act risk monitoring fields  |
| Using US-HQ Providers                | Sheet 8 Jurisdictional Risk (all)  |
| None of the Above                    | Mark as "N/A" or "Not Applicable"  |

RISK MONITORING CONSIDERATIONS

For ongoing governance of cloud services:
- DORA: Quarterly ICT risk register reviews mandatory
- NIS2: Significant incidents require ≤24h notification to authorities
- AI Act: High-risk AI systems require continuous monitoring
- Maintain audit trail of all risk assessments and decisions
- Document vendor concentration risks (single-vendor dependencies)
- Test business continuity plans annually minimum
```

### Update: How to Use This Workbook

Change instruction count and update text:
```
6. Complete Jurisdictional Risk sheet (8) for all US-nexus providers (NEW)
7. Document DORA ICT risk monitoring frequency if in scope
8. Classify NIS2 incidents according to severity thresholds
9. Monitor AI systems according to AI Act risk classification
10. Assign regulatory risk owners for all identified risks
```

### Update: Acceptable Evidence

Add new items:
```
✓ Quarterly ICT risk register reviews (DORA)
✓ Vendor concentration risk assessment
✓ Business continuity test reports (annual minimum)
✓ Incident notification records (NIS2 ≤24h threshold)
✓ AI system monitoring logs (for high-risk AI)
✓ Risk ownership assignments (signed by risk owners)
✓ Jurisdictional risk assessment (for US-nexus providers)
✓ Risk acceptance forms (signed by CISO/DPO/CRO)
```

---

## 7. Approval Sign-Off Updates (Sheet 11 — Previously Sheet 10)

### Add: Data Protection Officer Review Section

Insert between Risk Management Review and CISO Approval:

| Field | Type |
|-------|------|
| **DATA PROTECTION OFFICER REVIEW** | Section header (blue) |
| Reviewed By (DPO): | Yellow input |
| Review Date: | Yellow input |
| Data Protection Compliance: | Dropdown: Compliant/Partially Compliant/Non-Compliant |
| Cross-Border Transfer Status: | Dropdown: Approved/Approved with SCCs/Requires TIA/Rejected |
| DPO Comments: | Yellow input |

### Add: Chief Risk Officer Review Section

Insert after DPO Review:

| Field | Type |
|-------|------|
| **CHIEF RISK OFFICER REVIEW** | Section header (blue) |
| Reviewed By (CRO): | Yellow input |
| Review Date: | Yellow input |
| Enterprise Risk Acceptance: | Dropdown: Approved/Conditionally Approved/Rejected |
| Regulatory Risk Status: | Dropdown: Acceptable/Requires Mitigation/Unacceptable |
| CRO Comments: | Yellow input |

### Update: Assessment Summary

Add new fields:

| Field | Formula/Value |
|-------|---------------|
| Jurisdictional Risks Identified: | `='9. Summary Dashboard'!B20` |
| DORA Risks Not Monitored: | `='9. Summary Dashboard'!B28` |
| NIS2 Significant Incidents: | `='9. Summary Dashboard'!B29` |
| AI Monitoring Required: | `='9. Summary Dashboard'!B30` |

---

## 8. Updated Sheet Structure Summary

### Before (v1.0) — 10 Sheets

| Sheet | Name |
|-------|------|
| 1 | Instructions & Legend |
| 2 | Risk Register |
| 3 | Vendor Performance Review |
| 4 | Change Management Log |
| 5 | Incident Management |
| 6 | Service Review Meetings |
| 7 | Governance Metrics |
| 8 | Summary Dashboard |
| 9 | Evidence Register |
| 10 | Approval Sign-Off |

### After— 11 Sheets

| Sheet | Name | Change |
|-------|------|--------|
| 1 | Instructions & Legend | UPDATED |
| 2 | Risk Register | +4 columns (Y-AB), +19 checklist items |
| 3 | Vendor Performance Review | Unchanged |
| 4 | Change Management Log | Unchanged |
| 5 | Incident Management | Unchanged |
| 6 | Service Review Meetings | Unchanged |
| 7 | Governance Metrics | Unchanged |
| 8 | **Jurisdictional Risk** | **NEW** |
| 9 | Summary Dashboard | +11 metrics, renumbered |
| 10 | Evidence Register | +7 evidence types, renumbered |
| 11 | Approval Sign-Off | +DPO & CRO sections, renumbered |

---

## 9. Validation Requirements (Updated)

**Pre-Distribution Checks:**

- [ ] ✅ All **11 sheets** present (was 10)
- [ ] ✅ Base 17 columns (A-Q) configured on assessment sheets
- [ ] ✅ Extended columns present per sheet type
- [ ] ✅ **NEW: Jurisdictional Risk sheet has 20 columns (A-T)**
- [ ] ✅ **NEW: Risk Register has columns Y-AB (DORA/NIS2/AI Act/Owner)**
- [ ] ✅ Dropdowns configured (28+ validation types) — was 20
- [ ] ✅ **NEW: 10 regulatory dropdowns configured**
- [ ] ✅ Dashboard formulas link to assessment sheets
- [ ] ✅ **NEW: Dashboard includes jurisdictional + regulatory monitoring tables**
- [ ] ✅ Evidence Register has auto-generated IDs (EV-OGR-XXX)
- [ ] ✅ **NEW: Evidence Register includes regulatory risk evidence types**
- [ ] ✅ Approval Sign-Off links to dashboard metrics
- [ ] ✅ **NEW: DPO & CRO sign-off sections present**
- [ ] ✅ No Excel repair warnings (run style_object_checker.py)

---

## 10. Generator Script Impact

**File:** `generate_a523_4_ongoing_governance.py`

**Changes Required:**

1. Add 10 new dropdown list constants (regulatory dropdowns)
2. Update `create_workbook()` — add "8. Jurisdictional Risk" sheet, renumber 9-11
3. Add new function `create_8_jurisdictional_risk()`
4. Add `get_jurisdictional_columns()` — 20 columns
5. Add `create_jurisdictional_validations()` — 7 validation types
6. Update `get_extended_columns_risk_register()` — add Y-AB
7. Update `get_checklist_risk_register()` — add DORA/NIS2/AI Act items
8. Update `create_9_summary_dashboard()` — add 2 new metrics tables
9. Update `create_10_evidence_register()` — add evidence types
10. Update `create_11_approval_signoff()` — add DPO & CRO sections
11. Update `main()` — 11 sheets, version 2.0

---

## 11. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author Name] | Initial workbook specification |

---

**END OF REGULATORY UPDATE SPECIFICATION**

*"Risk management is what you do when you realize 'YOLO' isn't a valid governance strategy." — Every CRO, eventually*
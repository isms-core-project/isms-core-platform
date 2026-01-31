# ISMS-IMP-A.5.23.3 - Secure Configuration & Deployment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.5.23: Information security for use of cloud services

---

## Document Overview

**Document ID:** ISMS-IMP-A.5.23.3  
**Assessment Area:** Secure Configuration & Deployment  
**Related Policy:** ISMS-POL-A.5.19-23-S5 (Sections 5, 9)  
**Purpose:** Assess secure configuration of cloud services across identity, data protection, network, logging, and backup controls

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section
- **Title:** "ISMS-IMP-A.5.23.3 — Secure Configuration & Deployment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.5.23: Information security for use of cloud services"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.5.23.3
Assessment Area:       Secure Configuration & Deployment
Related Policy:        ISMS-POL-A.5.19-23-S5
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Reference ISMS-IMP-A.5.23.1 (Inventory) for authoritative cloud service list
2. Complete each worksheet tab (2–6) for all cloud services requiring configuration assessment
3. Use dropdown menus for standardized entries (Environment, Status, etc.)
4. Fill in yellow-highlighted cells with your configuration-specific information
5. For services with different configs per environment, create separate rows (same service, different Environment)
6. For services with identical config across all environments, use "All" in Environment column
7. Provide evidence: screenshots, config exports, security scan results
8. Summary Dashboard auto-calculates compliance by configuration area and environment
9. Obtain final approval from IT Operations, Security, and CISO

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Compliant | Configuration meets security requirements | Green (C6EFCE) |
| ⚠️ | Partial | Some settings correct, gaps exist | Yellow (FFEB9C) |
| ❌ | Non-Compliant | Configuration does not meet requirements | Red (FFC7CE) |
| N/A | Not Applicable | Control does not apply to this service | Gray |

#### Acceptable Evidence (Examples)
- ✓ Admin console screenshots (with timestamps)
- ✓ Configuration export files (JSON, YAML, XML)
- ✓ Security posture reports (Azure Secure Score, AWS Security Hub)
- ✓ API query results showing settings
- ✓ Infrastructure-as-Code (IaC) templates
- ✓ Penetration test results
- ✓ Vulnerability scan reports
- ✓ Access review reports
- ✓ Backup test results
- ✓ SIEM integration confirmation

---

## Assessment Sheets (2-6) - Standard Column Layout

### Base Columns (A-Q) - All Configuration Sheets

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Cloud Service Name | 28 | Text | Free text (reference ISMS-IMP-A.5.23.1) |
| B | Vendor Name | 22 | Text | Free text |
| C | Service Type | 20 | Dropdown | SaaS, IaaS, PaaS, Security Service, Cloud Storage, Other |
| D | Environment | 18 | Dropdown | Production, Staging, Development, Test, All |
| E | Service Criticality | 18 | Dropdown | Critical, High, Medium, Low |
| F | Data Classification | 20 | Dropdown | Restricted, Confidential, Internal, Public, N/A |
| G | Configuration Item | 30 | Text | Specific setting assessed |
| H | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| I | Evidence Location | 30 | Text | Screenshot path, config export location |
| J | Gap Description | 35 | Text | What's missing or misconfigured |
| K | Remediation Needed | 16 | Dropdown | Yes, No |
| L | Exception ID | 14 | Text | Link to exception register |
| M | Risk ID | 14 | Text | Link to risk register |
| N | Compensating Controls | 30 | Text | Mitigations if gap exists |
| O | Responsible Team | 20 | Dropdown | DevOpsSec, DevOps, Cloud Teams |
| P | Target Remediation Date | 18 | Date | Date picker |
| Q | Last Verified Date | 18 | Date | When configuration last checked |

---

## Sheet 2: Identity & Access Configuration

### Section Header
"IDENTITY & ACCESS CONFIGURATION\nPolicy Requirement: SSO integration, MFA enforced, RBAC implemented, privileged access controlled (Policy S5 Section 9.1)"

### Assessment Question
"Are identity and access controls properly configured for your cloud services?"

### Extended Columns (R-X) for Identity & Access

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | SSO Integrated | 16 | Dropdown | Yes, No, Partial, N/A |
| S | MFA Enforced | 16 | Dropdown | Yes (All Users), Yes (Admins Only), No, N/A |
| T | RBAC Implemented | 16 | Dropdown | Yes, Partial, No, N/A |
| U | Privileged Access JIT | 18 | Dropdown | Yes, No, Planned, N/A |
| V | Service Accounts Inventoried | 20 | Dropdown | Yes, Partial, No, Unknown |
| W | Last Access Review | 18 | Date | Date picker |
| X | Admin Account Count | 16 | Number | Numeric (≥0) |

### Checklist Items (Identity & Access)
| Item | Requirement | Evidence |
|------|-------------|----------|
| ☐ | SSO configured via organizational IdP (Entra ID, Okta, etc.) | SSO config screenshot |
| ☐ | MFA enforced for all users | MFA policy screenshot |
| ☐ | MFA mandatory for privileged accounts | Admin MFA verification |
| ☐ | RBAC roles documented and implemented | Role matrix document |
| ☐ | Least privilege principle applied | Permission audit |
| ☐ | Service accounts inventoried with owners | Service account register |
| ☐ | Privileged access is time-limited (JIT) | PAM configuration |
| ☐ | Access reviews performed quarterly | Access review report |
| ☐ | Default accounts disabled or renamed | Security baseline check |
| ☐ | Failed login alerting configured | Alert rule screenshot |

---

## Sheet 3: Data Protection Configuration

### Section Header
"DATA PROTECTION CONFIGURATION\nPolicy Requirement: Encryption at rest and in transit, key management, classification labels, DLP (Policy S5 Section 9.2)"

### Assessment Question
"Are data protection controls properly configured for your cloud services?"

### Extended Columns (R-X) for Data Protection

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Encryption At Rest | 18 | Dropdown | Yes (Provider Key), Yes (CMK), No, N/A |
| S | Encryption In Transit | 18 | Dropdown | Yes (TLS 1.3), Yes (TLS 1.2), No, N/A |
| T | Encryption Algorithm | 18 | Dropdown | AES-256, AES-128, ChaCha20, Other, Unknown |
| U | Key Management | 20 | Dropdown | Provider Managed, Customer Managed (HSM), Customer Managed (Software), N/A |
| V | Classification Labels | 18 | Dropdown | Yes (Enforced), Yes (Optional), No, N/A |
| W | DLP Configured | 16 | Dropdown | Yes, Partial, No, N/A |
| X | Key Rotation Period | 18 | Dropdown | 90 days, 180 days, 365 days, Manual, N/A |

### Checklist Items (Data Protection)
| Item | Requirement | Evidence |
|------|-------------|----------|
| ☐ | TLS 1.2+ enforced for all connections | TLS config, SSL scan |
| ☐ | AES-256 encryption at rest enabled | Encryption settings |
| ☐ | Encryption keys stored securely (HSM/KMS) | Key management config |
| ☐ | Key rotation policy implemented | Rotation schedule |
| ☐ | Data classification labels applied | Label policy screenshot |
| ☐ | DLP rules configured for sensitive data | DLP policy rules |
| ☐ | Data masking for non-production environments | Masking config |
| ☐ | Secure deletion process documented | Deletion procedures |

---

## Sheet 4: Network Security Configuration

### Section Header
"NETWORK SECURITY CONFIGURATION\nPolicy Requirement: Access restrictions, secure connectivity, network segmentation (Policy S5 Section 5.2)"

### Assessment Question
"Are network security controls properly configured for your cloud services?"

### Extended Columns (R-X) for Network Security

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | IP Restrictions | 16 | Dropdown | Yes (Allowlist), Yes (Geo), No, N/A |
| S | Private Connectivity | 18 | Dropdown | Yes (Private Link), Yes (VPN), Public Only, N/A |
| T | Network Segmentation | 18 | Dropdown | Yes, Partial, No, N/A |
| U | WAF Enabled | 14 | Dropdown | Yes, No, N/A |
| V | DDoS Protection | 16 | Dropdown | Yes (Advanced), Yes (Basic), No, N/A |
| W | Firewall Rules Documented | 20 | Dropdown | Yes, Partial, No, N/A |
| X | Public Endpoints Count | 18 | Number | Numeric (≥0) |

### Checklist Items (Network Security)
| Item | Requirement | Evidence |
|------|-------------|----------|
| ☐ | IP allowlisting configured for admin access | Firewall rules |
| ☐ | Private endpoints used where available | Network architecture |
| ☐ | VPN/ExpressRoute for sensitive workloads | Connectivity config |
| ☐ | Network segmentation between environments | Network diagram |
| ☐ | WAF configured for web applications | WAF rules export |
| ☐ | DDoS protection enabled | DDoS settings |
| ☐ | Firewall rules documented and reviewed | Rule documentation |
| ☐ | Public endpoints minimized and justified | Endpoint inventory |

---

## Sheet 5: Logging & Monitoring Configuration

### Section Header
"LOGGING & MONITORING CONFIGURATION\nPolicy Requirement: Audit logging, SIEM integration, alerting, retention ≥12 months (Policy S5 Section 9.3)"

### Assessment Question
"Are logging and monitoring controls properly configured for your cloud services?"

### Extended Columns (R-X) for Logging & Monitoring

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Audit Logging Enabled | 18 | Dropdown | Yes (All Events), Yes (Security Only), No, N/A |
| S | SIEM Integrated | 16 | Dropdown | Yes, Planned, No, N/A |
| T | Alerting Configured | 16 | Dropdown | Yes, Partial, No, N/A |
| U | Log Retention (Days) | 18 | Dropdown | 365+, 180, 90, 30, <30, Unknown |
| V | Threat Detection Active | 18 | Dropdown | Yes, Partial, No, N/A |
| W | Security Dashboard | 18 | Dropdown | Yes, No, N/A |
| X | Last Log Review Date | 18 | Date | Date picker |

### Checklist Items (Logging & Monitoring)
| Item | Requirement | Evidence |
|------|-------------|----------|
| ☐ | All security-relevant events logged | Audit policy config |
| ☐ | Logs exported to organizational SIEM | SIEM integration |
| ☐ | Log retention ≥12 months (365 days) | Retention settings |
| ☐ | Security alerts configured | Alert rules |
| ☐ | Alert notification to SOC/Security team | Notification config |
| ☐ | Threat detection enabled | Detection settings |
| ☐ | Security dashboard accessible | Dashboard access |
| ☐ | Logs reviewed regularly (quarterly minimum) | Review records |

---

## Sheet 6: Backup & Recovery Configuration

### Section Header
"BACKUP & RECOVERY CONFIGURATION\nPolicy Requirement: Automated backups, tested recovery, appropriate retention (Policy S5 Section 5.2)"

### Assessment Question
"Are backup and recovery controls properly configured for your cloud services?"

### Extended Columns (R-X) for Backup & Recovery

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Backup Enabled | 14 | Dropdown | Yes, No, N/A |
| S | Backup Frequency | 18 | Dropdown | Continuous, Daily, Weekly, Monthly, N/A |
| T | Backup Retention | 16 | Dropdown | 365 days, 90 days, 30 days, 7 days, N/A |
| U | Backup Encryption | 16 | Dropdown | Yes, No, Unknown, N/A |
| V | Last Recovery Test | 18 | Date | Date picker |
| W | RTO Achievable | 16 | Dropdown | Yes (Verified), Likely, No, Unknown |
| X | RPO Achievable | 16 | Dropdown | Yes (Verified), Likely, No, Unknown |

### Checklist Items (Backup & Recovery)
| Item | Requirement | Evidence |
|------|-------------|----------|
| ☐ | Automated backups enabled | Backup policy config |
| ☐ | Backup frequency meets RPO requirements | Backup schedule |
| ☐ | Backup retention meets compliance needs | Retention settings |
| ☐ | Backups encrypted | Encryption settings |
| ☐ | Recovery tested semi-annually | Test results report |
| ☐ | RTO achievable per BIA requirements | Recovery test timing |
| ☐ | RPO achievable per BIA requirements | Data loss measurement |
| ☐ | Geo-redundant backup for critical services | Replication config |

---

## Sheet 7: Summary Dashboard

### Section Header
"SECURE CONFIGURATION - COMPLIANCE SUMMARY DASHBOARD"

### Table 1: Compliance by Configuration Area

| Configuration Area | Total Items | ✅ Compliant | ⚠️ Partial | ❌ Non-Compliant | N/A | Compliance % |
|--------------------|-------------|--------------|------------|------------------|-----|--------------|
| Identity & Access | =COUNTA(...) | =COUNTIF(...) | ... | ... | ... | =formula |
| Data Protection | ... | ... | ... | ... | ... | ... |
| Network Security | ... | ... | ... | ... | ... | ... |
| Logging & Monitoring | ... | ... | ... | ... | ... | ... |
| Backup & Recovery | ... | ... | ... | ... | ... | ... |
| **TOTAL** | =SUM | =SUM | =SUM | =SUM | =SUM | =formula |

### Table 2: Compliance by Environment

| Environment | Total Items | ✅ Compliant | Compliance % |
|-------------|-------------|--------------|--------------|
| Production | =COUNTIF(D:D,"Production") | ... | ... |
| Staging | =COUNTIF(D:D,"Staging") | ... | ... |
| Development | =COUNTIF(D:D,"Development") | ... | ... |
| Test | =COUNTIF(D:D,"Test") | ... | ... |
| All | =COUNTIF(D:D,"All") | ... | ... |

### Table 3: Critical Gaps (Non-Compliant + Critical/High Services)

| Gap Type | Count | Priority |
|----------|-------|----------|
| Production + Non-Compliant | =COUNTIFS(...) | Critical |
| Critical Service + Non-Compliant | =COUNTIFS(...) | Critical |
| MFA Not Enforced (Production) | =COUNTIFS(...) | High |
| No Encryption at Rest | =COUNTIFS(...) | High |
| Logging Not Enabled | =COUNTIFS(...) | High |

---

## Sheet 8: Evidence Register

### Column Structure

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence ID | 18 | Formula (=CONCATENATE("EV-CFG-",TEXT(ROW()-3,"000"))) |
| B | Cloud Service Name | 25 | Text |
| C | Configuration Area | 22 | Dropdown | Identity, Data Protection, Network, Logging, Backup |
| D | Evidence Type | 22 | Dropdown | Screenshot, Config Export, Scan Report, Test Result, IaC Template, Other |
| E | Description | 35 | Text |
| F | File Location | 35 | Text |
| G | Capture Date | 16 | Date |
| H | Captured By | 18 | Text |
| I | Status | 14 | Dropdown | Current, Outdated, Pending |

---

## Sheet 9: Approval Sign-Off

### Approval Sections

**Assessment Completion:**
- Completed By, Date, Total Configs Assessed, Overall Compliance %

**IT Operations Review:**
- Reviewed By, Date, Technical Accuracy Status (Dropdown), Comments

**Security Team Review:**
- Reviewed By, Date, Security Compliance Status (Dropdown), Comments

**CISO Approval:**
- Approved By, Date, Approval Decision (Dropdown), Executive Comments

**Next Review:**
- Next Review Date, Responsible, Special Considerations

---

## Validation Requirements

**Pre-Distribution Checks:**
- [ ] All 9 sheets present
- [ ] Base 17 columns (A-Q) on assessment sheets
- [ ] Extended columns (R-X) per sheet type
- [ ] Environment dropdown includes: Production, Staging, Development, Test, All
- [ ] Responsible Team dropdown includes: DevOpsSec, DevOps, Cloud Teams
- [ ] Dashboard formulas reference assessment sheets
- [ ] Evidence Register has auto-generated IDs (EV-CFG-###)

---

**END OF SPECIFICATION**

**Document Status:** Ready for Python generator script development  
**Estimated Workbook Size:** ~65 KB (9 sheets)  
**Stakeholders:** DevOpsSec, DevOps, Cloud Teams, Security, CISO

--------------------------------------------------------------------------------------------------

# ISMS-IMP-A.5.23.3 - Secure Configuration & Deployment
## Regulatory Update — DORA, NIS2, AI Act, CLOUD Act Enhancements

---

## Change Summary

| Change Type | Description |
|-------------|-------------|
| **Sheet Added** | NEW Sheet 7: Jurisdictional Risk Assessment (20 columns) |
| **Columns Added** | 3 new columns (Y-AA) on Configuration Baseline sheet for DORA/NIS2/AI Act |
| **Checklists Updated** | +6 DORA items, +4 NIS2 items, +5 AI Act items, +9 Evaluation criteria |
| **Dashboard Updated** | +7 jurisdictional risk metrics, +3 regulatory compliance metrics |
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

DORA_COMPLIANCE_LEVEL:
- Full Compliance
- Partial Compliance
- Non-Compliant
- N/A (Not in scope)

NIS2_DEPLOYMENT_STATUS:
- Compliant
- Partial (In Progress)
- Non-Compliant
- N/A (Not in scope)

AI_SYSTEM_DEPLOYMENT:
- No AI Systems
- Low-Risk AI Only
- High-Risk AI (Assessed)
- High-Risk AI (Assessment Pending)
- N/A
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

## 3. Configuration Baseline Sheet Updates (Sheet 2)

### New Columns (Y-AA) — Add After Existing Column X

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| Y | DORA_Config_Documentation | 22 | Dropdown | DORA_COMPLIANCE_LEVEL |
| Z | NIS2_Secure_Deployment | 20 | Dropdown | NIS2_DEPLOYMENT_STATUS |
| AA | AI_System_Deployment_Controls | 24 | Dropdown | AI_SYSTEM_DEPLOYMENT |

### Updated Configuration Checklist — Add DORA/NIS2/AI Act Items

**Existing items remain unchanged. ADD the following:**

#### DORA Configuration Requirements (CFG-DORA-01 to CFG-DORA-06)

| Config_ID | Requirement | DORA_Mandatory | NIS2_Mandatory |
|-----------|-------------|----------------|----------------|
| CFG-DORA-01 | Configuration baseline documented and version-controlled | Yes | No |
| CFG-DORA-02 | Change management process for cloud configurations | Yes | Yes |
| CFG-DORA-03 | Configuration drift monitoring enabled | Yes | No |
| CFG-DORA-04 | Security configuration validated against CIS benchmarks | Yes | No |
| CFG-DORA-05 | Configuration backup and recovery tested | Yes | Yes |
| CFG-DORA-06 | Privileged access to configurations logged and monitored | Yes | Yes |

#### NIS2 Secure Deployment Requirements (CFG-NIS2-01 to CFG-NIS2-04)

| Config_ID | Requirement | DORA_Mandatory | NIS2_Mandatory |
|-----------|-------------|----------------|----------------|
| CFG-NIS2-01 | Security-by-default configurations applied | No | Yes |
| CFG-NIS2-02 | Network segmentation implemented | No | Yes |
| CFG-NIS2-03 | Multi-factor authentication enforced for admin access | No | Yes |
| CFG-NIS2-04 | Vulnerability scanning configured pre-deployment | No | Yes |

#### AI Act Deployment Controls (CFG-AI-01 to CFG-AI-05)

| Config_ID | Requirement | AI_Act_Mandatory |
|-----------|-------------|------------------|
| CFG-AI-01 | AI system risk classification documented | Yes (if AI used) |
| CFG-AI-02 | High-risk AI systems have conformity assessment | Yes (if high-risk) |
| CFG-AI-03 | AI system transparency notices configured | Yes (if AI used) |
| CFG-AI-04 | AI system logging and monitoring enabled | Yes (if high-risk) |
| CFG-AI-05 | Human oversight mechanisms configured | Yes (if high-risk) |

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

### Add: Table 3 — Regulatory Deployment Compliance

Insert after Table 2:

| Row | Metric | Formula | Status Formula |
|-----|--------|---------|----------------|
| Header | REGULATORY DEPLOYMENT COMPLIANCE | (merged, dark blue) | |
| 1 | DORA Non-Compliant Configurations | `=COUNTIF('2. Configuration Baseline'!Y7:Y30,"Non-Compliant")` | `=IF(B>0,"❌ Action","✅ OK")` |
| 2 | NIS2 Non-Compliant Deployments | `=COUNTIF('2. Configuration Baseline'!Z7:Z30,"Non-Compliant")` | `=IF(B>0,"❌ Action","✅ OK")` |
| 3 | High-Risk AI Systems Pending Assessment | `=COUNTIF('2. Configuration Baseline'!AA7:AA30,"*Pending*")` | `=IF(B>0,"⚠️ Review","✅ OK")` |

---

## 6. Instructions Sheet Updates

### Add: Regulatory Applicability Section

Insert after "Acceptable Evidence" section:
```
REGULATORY COMPLIANCE (NEW IN v2.0)

This workbook includes updated requirements for:
- DORA (Digital Operational Resilience Act) - Configuration documentation
- NIS2 (Network and Information Security Directive 2) - Secure deployment
- EU AI Act - AI system deployment controls
- US CLOUD Act - Jurisdictional risk assessment (NEW Sheet 7)

REGULATORY APPLICABILITY GUIDANCE

| If You Are...                        | Complete These Fields              |
|--------------------------------------|------------------------------------|
| EU Financial Entity (DORA scope)     | All DORA fields (mandatory)        |
| EU Essential/Important Entity (NIS2) | All NIS2 fields (mandatory)        |
| Deploying AI Systems from vendors    | All AI Act deployment controls     |
| Using US-HQ Providers                | Sheet 7 Jurisdictional Risk (all)  |
| None of the Above                    | Mark as "N/A" or "Not Applicable"  |

DEPLOYMENT-SPECIFIC CONSIDERATIONS

For secure deployment of cloud services:
- Document configuration baselines BEFORE deployment
- Validate against CIS benchmarks or equivalent standards
- Enable configuration drift monitoring
- Test backup and recovery procedures
- Implement network segmentation for sensitive workloads
- For AI systems: Complete risk classification BEFORE deployment
```

### Update: How to Use This Workbook

Change instruction count and update text:
```
5. Complete Jurisdictional Risk sheet (7) for all US-nexus providers (NEW)
6. Document DORA configuration requirements if in scope
7. Validate NIS2 secure deployment procedures if applicable
8. Complete AI Act deployment controls for AI-enabled services
```

### Update: Acceptable Evidence

Add new items:
```
✓ Configuration baseline documentation (version-controlled)
✓ CIS benchmark compliance report
✓ Configuration drift monitoring screenshots
✓ Network segmentation diagrams
✓ AI system risk classification (if applicable)
✓ AI conformity assessment (for high-risk systems)
✓ Jurisdictional risk assessment (for US-nexus providers)
✓ Risk acceptance form (signed by CISO/DPO)
```

---

## 7. Approval Sign-Off Updates (Sheet 10 — Previously Sheet 9)

### Add: Data Protection Officer Review Section

Insert between IT Operations Review and CISO Approval:

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
| DORA Config Non-Compliance: | `='8. Summary Dashboard'!B27` |
| NIS2 Deployment Non-Compliance: | `='8. Summary Dashboard'!B28` |

---

## 8. Updated Sheet Structure Summary

### Before (v1.0) — 9 Sheets

| Sheet | Name |
|-------|------|
| 1 | Instructions & Legend |
| 2 | Configuration Baseline |
| 3 | Access Control Setup |
| 4 | Network Security |
| 5 | Encryption Configuration |
| 6 | Deployment Checklist |
| 7 | Summary Dashboard |
| 8 | Evidence Register |
| 9 | Approval Sign-Off |

### After (v2.0) — 10 Sheets

| Sheet | Name | Change |
|-------|------|--------|
| 1 | Instructions & Legend | UPDATED |
| 2 | Configuration Baseline | +3 columns (Y-AA), +15 checklist items |
| 3 | Access Control Setup | Unchanged |
| 4 | Network Security | Unchanged |
| 5 | Encryption Configuration | Unchanged |
| 6 | Deployment Checklist | Unchanged |
| 7 | **Jurisdictional Risk** | **NEW** |
| 8 | Summary Dashboard | +10 metrics, renumbered |
| 9 | Evidence Register | +6 evidence types, renumbered |
| 10 | Approval Sign-Off | +DPO section, renumbered |

---

## 9. Validation Requirements (Updated)

**Pre-Distribution Checks:**

- [ ] ✅ All **10 sheets** present (was 9)
- [ ] ✅ Base 17 columns (A-Q) configured on assessment sheets
- [ ] ✅ Extended columns present per sheet type
- [ ] ✅ **NEW: Jurisdictional Risk sheet has 20 columns (A-T)**
- [ ] ✅ **NEW: Configuration Baseline has columns Y-AA (DORA/NIS2/AI Act)**
- [ ] ✅ Dropdowns configured (25+ validation types) — was 17
- [ ] ✅ **NEW: 9 regulatory dropdowns configured**
- [ ] ✅ Dashboard formulas link to assessment sheets
- [ ] ✅ **NEW: Dashboard includes jurisdictional + regulatory compliance tables**
- [ ] ✅ Evidence Register has auto-generated IDs (EV-SCD-XXX)
- [ ] ✅ **NEW: Evidence Register includes regulatory evidence types**
- [ ] ✅ Approval Sign-Off links to dashboard metrics
- [ ] ✅ **NEW: DPO sign-off section present**
- [ ] ✅ No Excel repair warnings (run style_object_checker.py)

---

## 10. Generator Script Impact

**File:** `generate_a523_3_secure_config.py`

**Changes Required:**

1. Add 9 new dropdown list constants (regulatory dropdowns)
2. Update `create_workbook()` — add "7. Jurisdictional Risk" sheet, renumber 8-10
3. Add new function `create_7_jurisdictional_risk()`
4. Add `get_jurisdictional_columns()` — 20 columns
5. Add `create_jurisdictional_validations()` — 7 validation types
6. Update `get_extended_columns_config_baseline()` — add Y-AA
7. Update `get_checklist_config_baseline()` — add DORA/NIS2/AI Act items
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

*"Configuration drift is just your cloud's way of saying 'I have trust issues with automation.'" — DevOps wisdom*
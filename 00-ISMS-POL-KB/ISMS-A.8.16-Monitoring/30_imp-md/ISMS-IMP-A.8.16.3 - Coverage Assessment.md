# ISMS-IMP-A.8.16.3 - Coverage Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.16.3  
**Assessment Area:** Monitoring Coverage (Assets, Networks, Users, Applications)  
**Related Policy:** ISMS-POL-A.8.16-S2.1.1, S2.1.2  
**Purpose:** Assess completeness of monitoring coverage across organizational assets  
**Generator Script:** `generate_a816_3_coverage_assessment.py`  
**Output Filename:** `ISMS-IMP-A.8.16.3_Coverage_Assessment_YYYYMMDD.xlsx`

---

## Workbook Structure

**Total Sheets:** 9
1. Instructions & Legend
2. 1. Asset Inventory & Coverage
3. 2. Network Segment Coverage
4. 3. User & Identity Coverage
5. 4. Application & Service Coverage
6. 5. Coverage Gap Analysis
7. Summary Dashboard
8. Evidence Register
9. Approval Sign-Off

---

## Sheet 2: 1. Asset Inventory & Coverage

### Header
**Title:** "1. ASSET INVENTORY & MONITORING COVERAGE"  
**Policy Reference:** "Assess asset coverage per ISMS-POL-A.8.16-S2.1.1"

### Assessment Question
"Are all organizational assets inventoried and appropriate assets monitored?"

### Column Headers - 23 Columns (A-W)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | Asset ID | 15 | Text | Free text |
| B | Asset Name | 28 | Text | Free text |
| C | Asset Type | 22 | Dropdown | Server, Network Device, Security Device, Endpoint, Cloud Resource, Database, Application, Container, IoT Device, Other |
| D | Operating System | 22 | Text | Free text |
| E | Location | 18 | Text | Free text |
| F | Business Unit | 20 | Text | Free text |
| G | Asset Owner | 20 | Text | Free text |
| H | Data Classification | 18 | Dropdown | Confidential, Internal, Public |
| I | Criticality | 15 | Dropdown | Critical, High, Medium, Low |
| J | Regulatory Scope | 22 | Dropdown | PCI-DSS, HIPAA, GDPR, SOX, Multiple, None |
| K | Monitoring Required | 16 | Dropdown | Mandatory, Recommended, Optional, N/A |
| L | Currently Monitored | 16 | Dropdown | Yes, No, Partial |
| M | Log Types Collected | 30 | Text | Free text |
| N | Monitoring Platform | 22 | Text | Free text |
| O | Baseline Established | 16 | Dropdown | Yes, No, N/A |
| P | Detection Rules Active | 18 | Text | Free text (count) |
| Q | Last Log Verified | 14 | Text | DD.MM.YYYY |
| R | Coverage Status | 18 | Dropdown | ✅ Full Coverage, ⚠️ Partial Coverage, ❌ No Coverage, N/A |
| S | Gap Reason | 30 | Text | Free text |
| T | Exception Approved | 16 | Dropdown | Yes, No, N/A |
| U | Target Coverage Date | 14 | Text | DD.MM.YYYY |
| V | Responsible Party | 20 | Text | Free text |
| W | Notes | 25 | Text | Free text |

### Data Entry Rows
- **Rows 8-50:** 43 data entry rows (comprehensive asset inventory)

### Compliance Checklist
1. Complete asset inventory maintained
2. Asset inventory updated at least quarterly
3. All assets classified by criticality
4. All Critical assets monitored (100%)
5. >80% of High priority assets monitored
6. >60% of Medium priority assets monitored
7. All PCI-DSS scope systems monitored
8. All HIPAA scope systems monitored
9. All systems handling confidential data monitored
10. Monitoring coverage gaps documented
11. Exceptions formally approved
12. Gap remediation plans exist
13. Coverage status reported monthly
14. Asset decommissioning process includes monitoring removal
15. New assets onboarded to monitoring within 30 days

### Reference Tables

**Table 1: Coverage Requirements by Criticality**
| Criticality | Coverage Requirement | Baseline Required | Detection Rules Required | Review Frequency |
|-------------|---------------------|-------------------|-------------------------|------------------|
| Critical | 100% mandatory | Yes | Yes (multiple) | Quarterly |
| High | >80% recommended | Yes | Yes | Semi-annually |
| Medium | >60% recommended | Recommended | Recommended | Annually |
| Low | Optional | No | No | As needed |

**Table 2: Coverage Requirements by Regulatory Scope**
| Regulation | Monitoring Requirement | Log Retention | Specific Controls |
|------------|----------------------|---------------|-------------------|
| PCI-DSS | Mandatory for CDE | 1 year minimum | File integrity, access control, network monitoring |
| HIPAA | Mandatory for PHI systems | 6 years | Access logs, audit trails, security events |
| GDPR | Recommended | Per data retention policy | Access logs, breach detection |
| SOX | Mandatory for financial systems | 7 years | Change management, access control |

---

## Sheet 3: 2. Network Segment Coverage

### Header
**Title:** "2. NETWORK SEGMENT COVERAGE ASSESSMENT"  
**Policy Reference:** "Assess network coverage per ISMS-POL-A.8.16-S2.1.1"

### Column Headers - 20 Columns (A-T)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Network Segment/Zone | 28 | Text |
| B | Segment Type | 22 | Dropdown: Production, DMZ, Internal, Management, Guest, Partner, Development, Test, Cloud VPC, Other |
| C | IP Range/CIDR | 20 | Text |
| D | VLAN ID | 12 | Text |
| E | Number of Assets | 15 | Text |
| F | Criticality | 15 | Dropdown: Critical, High, Medium, Low |
| G | Data Classification | 18 | Dropdown: Confidential, Internal, Public |
| H | Perimeter Monitoring | 18 | Dropdown: Firewall, IDS/IPS, Both, None |
| I | Flow Monitoring | 16 | Dropdown: Yes, No, Planned |
| J | DNS Monitoring | 16 | Dropdown: Yes, No, Planned |
| K | Endpoint Monitoring | 18 | Dropdown: Yes (EDR), Partial, No |
| L | Log Collection Active | 18 | Dropdown: Yes, Partial, No |
| M | Network Tap/SPAN | 16 | Dropdown: Yes, No, Planned |
| N | Isolation Status | 16 | Dropdown: Isolated, Semi-Isolated, Open |
| O | Coverage Status | 18 | Dropdown: ✅ Full, ⚠️ Partial, ❌ None, N/A |
| P | Gaps Identified | 30 | Text |
| Q | Exception Approved | 16 | Dropdown: Yes, No, N/A |
| R | Target Date | 14 | Text: DD.MM.YYYY |
| S | Responsible Party | 20 | Text |
| T | Notes | 25 | Text |

### Compliance Checklist
1. All network segments inventoried
2. All production segments monitored
3. All DMZ segments monitored
4. Critical segments have redundant monitoring
5. Perimeter traffic monitored (firewall + IDS/IPS)
6. Internal traffic monitored (flow data)
7. DNS queries monitored
8. Endpoints monitored (EDR/AV integration)
9. East-west traffic visibility (lateral movement detection)
10. Cloud network segments included

---

## Sheet 4: 3. User & Identity Coverage

### Header
**Title:** "3. USER & IDENTITY MONITORING COVERAGE"  
**Policy Reference:** "Assess user monitoring per ISMS-POL-A.8.16-S2.1.2"

### Column Headers - 19 Columns (A-S)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Identity System | 25 | Text |
| B | System Type | 22 | Dropdown: Active Directory, Azure AD, LDAP, SAML IdP, OAuth Provider, Database Auth, Application-Specific, Other |
| C | User Count | 15 | Text |
| D | Privileged Account Count | 20 | Text |
| E | Service Account Count | 20 | Text |
| F | Authentication Logs Collected | 22 | Dropdown: Yes, Partial, No |
| G | Authorization Logs Collected | 22 | Dropdown: Yes, Partial, No |
| H | Password Change Logs | 20 | Dropdown: Yes, No |
| I | Privilege Escalation Logs | 22 | Dropdown: Yes, No |
| J | MFA Events Logged | 18 | Dropdown: Yes, No, N/A |
| K | SSO Events Logged | 18 | Dropdown: Yes, No, N/A |
| L | Failed Login Monitoring | 20 | Dropdown: Yes, No |
| M | After-Hours Access Monitoring | 22 | Dropdown: Yes, No |
| N | Geographic Anomaly Detection | 22 | Dropdown: Yes, No, Planned |
| O | User Behavior Analytics | 22 | Dropdown: Yes (UEBA), Planned, No |
| P | Privileged Access Monitoring | 22 | Dropdown: Yes (PAM integrated), Partial, No |
| Q | Coverage Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| R | Gaps/Issues | 30 | Text |
| S | Priority | 16 | Dropdown: Critical, High, Medium, Low |

### Compliance Checklist
1. Primary identity system (AD/Azure AD) monitored
2. All authentication events logged
3. Failed login attempts monitored and alerted
4. Privileged account usage monitored
5. Service account usage monitored
6. Password changes logged
7. Privilege escalation logged
8. MFA events logged (if MFA deployed)
9. SSO events logged (if SSO deployed)
10. After-hours access monitored
11. Geographic anomalies detected
12. User behavior baselines established
13. Dormant accounts identified
14. Privileged access sessions recorded (PAM)
15. Identity correlation across systems

---

## Sheet 5: 4. Application & Service Coverage

### Header
**Title:** "4. APPLICATION & SERVICE MONITORING COVERAGE"  
**Policy Reference:** "Assess application coverage per ISMS-POL-A.8.16-S2.1.2"

### Column Headers - 21 Columns (A-U)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Application/Service Name | 28 | Text |
| B | Application Type | 22 | Dropdown: Web Application, Database, API, Microservice, SaaS, Mobile App, Desktop App, Other |
| C | Business Unit | 20 | Text |
| D | Application Owner | 20 | Text |
| E | Data Classification | 18 | Dropdown: Confidential, Internal, Public |
| F | Criticality | 15 | Dropdown: Critical, High, Medium, Low |
| G | User Base | 18 | Text |
| H | Application Logs Collected | 22 | Dropdown: Yes, Partial, No |
| I | API Logs Collected | 18 | Dropdown: Yes, No, N/A |
| J | Database Logs Collected | 22 | Dropdown: Yes, Partial, No |
| K | Error/Exception Logging | 20 | Dropdown: Yes, Partial, No |
| L | Transaction Logging | 18 | Dropdown: Yes, No |
| M | Access Control Logs | 20 | Dropdown: Yes, No |
| N | Data Export Monitoring | 20 | Dropdown: Yes, No |
| O | Performance Monitoring | 20 | Dropdown: Yes, No |
| P | WAF Integration | 16 | Dropdown: Yes, No, N/A |
| Q | APM Integration | 16 | Dropdown: Yes, No |
| R | Coverage Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| S | Gaps | 30 | Text |
| T | Target Date | 14 | Text: DD.MM.YYYY |
| U | Priority | 16 | Dropdown: Critical, High, Medium, Low |

### Compliance Checklist
1. All critical applications monitored
2. >80% of high-priority applications monitored
3. Application error/exception logs collected
4. API calls logged (if API-based)
5. Database queries logged (if database-backed)
6. User access logged
7. Data exports/downloads monitored
8. File uploads monitored
9. Configuration changes logged
10. WAF deployed for internet-facing apps
11. APM integrated for performance visibility
12. Cloud application logs collected (SaaS)
13. Mobile app backend logs collected
14. Third-party integrations monitored
15. Application security events forwarded to SIEM

---

## Sheet 6: 5. Coverage Gap Analysis

### Header
**Title:** "5. COVERAGE GAP ANALYSIS"  
**Policy Reference:** "Assess gaps per ISMS-POL-A.8.16-S2.1"

### Column Headers - 18 Columns (A-R)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Gap ID | 12 | Text |
| B | Gap Category | 22 | Dropdown: Asset Not Monitored, Log Source Missing, Network Segment Gap, User/Identity Gap, Application Gap, Detection Gap, Other |
| C | Affected Asset/System | 28 | Text |
| D | Gap Description | 35 | Text |
| E | Business Impact | 30 | Text |
| F | Risk Level | 15 | Dropdown: Critical, High, Medium, Low |
| G | Root Cause | 30 | Text |
| H | Exception Approved | 16 | Dropdown: Yes, No, Pending |
| I | Exception ID | 15 | Text |
| J | Compensating Controls | 30 | Text |
| K | Remediation Plan | 35 | Text |
| L | Remediation Owner | 20 | Text |
| M | Target Date | 14 | Text: DD.MM.YYYY |
| N | Budget Required | 15 | Dropdown: Yes, No, Unknown |
| O | Status | 18 | Dropdown: Open, In Progress, Resolved, Deferred, Accepted |
| P | Status Date | 14 | Text: DD.MM.YYYY |
| Q | Verification Method | 25 | Text |
| R | Notes | 30 | Text |

### Compliance Checklist
1. All coverage gaps identified
2. Gaps categorized by type
3. Risk level assessed for each gap
4. Root cause analysis conducted
5. Critical gaps remediated within 30 days
6. High gaps remediated within 90 days
7. Exceptions formally approved
8. Compensating controls documented
9. Remediation plans documented
10. Gap remediation tracked
11. Verification conducted post-remediation
12. Trends analyzed (recurring gaps?)
13. Gaps reported to CISO monthly
14. Improvement actions implemented
15. Coverage metrics improving over time

---

## Sheet 7: Summary Dashboard

### Section 1: Overall Coverage Summary (Rows 3-18)
- Total assets in inventory
- Assets monitored / total assets
- % Coverage by criticality (Critical/High/Medium/Low)
- % Coverage by asset type
- Assets without monitoring (count and %)

### Section 2: Network Coverage (Rows 21-30)
- Network segments total
- Segments fully monitored
- Segments partially monitored
- Segments not monitored
- % Coverage by segment type

### Section 3: User/Identity Coverage (Rows 33-42)
- Identity systems total
- Identity systems monitored
- Users covered
- Privileged accounts monitored %

### Section 4: Application Coverage (Rows 45-54)
- Applications total
- Applications monitored
- % Coverage by criticality
- % Coverage by type

### Section 5: Gap Analysis (Rows 57-69)
- Total gaps identified
- Gaps by severity (Critical/High/Medium/Low)
- Open gaps
- In-progress remediations
- Resolved gaps
- Accepted risks
- Overdue remediations

### Section 6: Compliance Summary (Rows 72-82)
| Assessment Area | Compliant | Partial | Non-Compliant | % Compliant |
|-----------------|-----------|---------|---------------|-------------|
| 1. Asset Coverage | Formula | Formula | Formula | Formula |
| 2. Network Coverage | Formula | Formula | Formula | Formula |
| 3. User/Identity Coverage | Formula | Formula | Formula | Formula |
| 4. Application Coverage | Formula | Formula | Formula | Formula |
| 5. Gap Remediation | Formula | Formula | Formula | Formula |
| **OVERALL** | Formula | Formula | Formula | Formula |

---

**END OF SPECIFICATION**
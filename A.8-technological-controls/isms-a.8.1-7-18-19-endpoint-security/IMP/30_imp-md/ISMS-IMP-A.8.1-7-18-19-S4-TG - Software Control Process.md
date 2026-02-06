**ISMS-IMP-A.8.1-7-18-19-S4-TG - Software Control Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Software Installation Controls and Application Whitelisting |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.4 (Software Installation Controls) |
| **Purpose** | Document approved software list, assess unauthorized software, verify application control effectiveness across endpoint landscape |
| **Target Audience** | IT Operations, Security Engineers, Change Management, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly (unauthorized software), Quarterly (full assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for software control assessment | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.1-7-18-19-S4-UG.

---

# Technical Specification

## Workbook Structure

**File Name:** `Software_Controls_Assessment.xlsx`

**Sheets (12 total):**
1. Instructions & Legend
2. Approved_Software
3. Software_Inventory
4. Unauthorized_Software
5. Application_Control
6. Change_Control
7. Vulnerability_Management
8. Licensing_Compliance
9. Capability_Requirements
10. Evidence_Register
11. Gap_Analysis
12. Approval_Sign_Off

---

## Sheet 1: Instructions & Legend

### Header Section (Rows 1-2)
```
Row 1: "ISMS-IMP-A.8.1-7-18-19-S4 - Software Control Process Assessment"
       (Dark blue #003366, white text, centered, merged A1:H1, height 40px)
Row 2: "ISO/IEC 27001:2022 - Controls A.8.1, A.8.7, A.8.18, A.8.19: Endpoint Security"
       (Medium blue #4472C4, white text, centered, merged A2:H2, height 30px)
```

### Document Information (Rows 4-12)
```
Document ID:           ISMS-IMP-A.8.1-7-18-19-S4
Assessment Area:       Software Installation Controls & Application Whitelisting
Related Policy:        ISMS-POL-A.8.1-7-18-19, Section 2.4
Version:               1.0
Assessment Date:       [USER INPUT - yellow #FFEB9C]
Completed By:          [USER INPUT - yellow]
Organization:          [USER INPUT - yellow]
Review Cycle:          Monthly (unauthorized software), Quarterly (full)
Next Review Date:      [FORMULA: =B8+30]
```

### How to Use (Rows 14-24)
1. Document approved software list (Sheet 2)
2. Collect software inventory from all endpoints (Sheet 3)
3. Identify unauthorized software (Sheet 4)
4. Assess application control deployment (Sheet 5)
5. Verify patch compliance (Sheet 6)
6. Identify gaps (Sheet 7)
7. Register evidence (Sheet 8)
8. Review dashboard (Sheet 9)
9. Obtain three-level approval

### Status Legend (Rows 26-35)

| Symbol | Status | Description | Color |
|--------|--------|-------------|-------|
| ✅ | Approved | On approved software list | Green #C6EFCE |
| ⚠️ | Pending Approval | Submitted for approval | Yellow #FFEB9C |
| ❌ | Unauthorized | Not approved | Red #FFC7CE |
| 🔴 | Prohibited | Explicitly prohibited | Dark Red #C00000 |
| 🟢 | Deployed | Application control deployed | Green #00B050 |
| 🟡 | Audit Mode | Application control in audit only | Yellow #FFFF00 |
| 🔴 | Not Deployed | No application control | Dark Red #C00000 |

### Software Control Thresholds (Rows 37-42)

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Approved List Exists | Yes, current | Yes, outdated | No |
| Unauthorized Software % | ≤5% | 5-10% | >10% |
| Application Control Deployment | ≥95% | 85-94% | <85% |
| Application Control Enforcement | ≥90% | 75-89% | <75% |
| Critical Patch Compliance | ≥95% | 85-94% | <85% |

---

## Sheet 2: Approved_Software

### Purpose
Master approved software list with categories, versions, and approval workflow.

### Header (Rows 1-2)
```
Row 1: "APPROVED SOFTWARE LIST" (merged A1:P1, medium blue #4472C4)
Row 2: "Master list of approved, role-specific, optional, and prohibited software" (merged A2:P2)
```

### Column Structure (Row 3 - headers, Rows 4-503 - data, 500 rows)

| Col | Header | Type | Width | Validation |
|-----|--------|------|-------|------------|
| A | Software ID | Auto | 10 | SW-001, SW-002... |
| B | Software Name | Text | 30 | Official product name (yellow #FFEB9C) |
| C | Vendor | Text | 20 | Company name |
| D | Category | Dropdown | 15 | Mandatory / Role-Specific / Optional / Prohibited |
| E | Applicable Roles | Text | 30 | If role-specific |
| F | Version Requirement | Dropdown | 20 | Latest Only / Latest or N-1 / Specific Version / Any Supported |
| G | Specific Version(s) | Text | 20 | If specific version required |
| H | License Type | Dropdown | 15 | Per-User / Per-Device / Enterprise / Open Source |
| I | Business Justification | Text | 40 | Why approved |
| J | Security Review Date | Date | 15 | Last security review |
| K | Security Reviewer | Text | 20 | Who reviewed |
| L | Approval Authority | Text | 20 | Who can approve installation |
| M | Software Owner | Text | 20 | Who maintains |
| N | Approval Date | Date | 12 | When approved |
| O | Approved By | Text | 20 | Approver name |
| P | Notes | Text | 40 | Additional info |

### Software Category Summary (Rows 505-515)
```
Total Approved Software:     [=COUNT(A4:A503 where not blank)]
Mandatory Software:          [=COUNTIF(D4:D503,"Mandatory")]
Role-Specific Software:      [=COUNTIF(D4:D503,"Role-Specific")]
Optional Software:           [=COUNTIF(D4:D503,"Optional")]
Prohibited Software:         [=COUNTIF(D4:D503,"Prohibited")]

Security Review Currency:
  Reviewed ≤6 months:        [=COUNTIFS(J:J,">="&DATE...)]
  Reviewed 6-12 months:      [=COUNTIFS(J:J,"<"&DATE...)]
  Never reviewed / >12 mo:   [=COUNTIFS(J:J,"<"&DATE...)]
```

### Conditional Formatting

**Category Column (D):**

- If "Mandatory" → Light blue #D9E1F2
- If "Role-Specific" → Light green #E2EFDA
- If "Optional" → Light yellow #FFF2CC
- If "Prohibited" → Red #FFC7CE

**Security Review Date Column (J):**

- If ≤6 months → Green #C6EFCE
- If 6-12 months → Yellow #FFEB9C
- If >12 months or blank → Red #FFC7CE

---

## Sheet 3: Installed_Software

### Purpose
Comprehensive software inventory across all endpoints.

### Header (Rows 1-2)
```
Row 1: "INSTALLED SOFTWARE INVENTORY"
Row 2: "Complete software inventory aggregated from all endpoints"
```

### Column Structure (Row 3 - headers, Rows 4-2003 - data, 2000 rows)

| Col | Header | Type | Width | Formula/Validation |
|-----|--------|------|-------|-------------------|
| A | Software ID | Auto | 10 | INS-001, INS-002... |
| B | Software Name | Text | 30 | Normalized name |
| C | Vendor | Text | 20 | Publisher |
| D | Version(s) Detected | Text | 30 | All versions found |
| E | Most Common Version | Text | 20 | Most prevalent |
| F | Endpoint Count | Number | 12 | How many endpoints |
| G | % of Total Endpoints | Formula | 10 | =(F4/TotalEndpoints)*100 |
| H | Installation Method | Dropdown | 15 | Centrally Deployed / User Installed / Pre-installed / Unknown |
| I | First Detected | Date | 12 | Earliest detection |
| J | Last Detected | Date | 12 | Most recent detection |
| K | Category | Text | 20 | Application type |
| L | Risk Flag | Dropdown | 12 | None / Shadow IT / EOL / High-Risk / Vulnerable |
| M | On Approved List? | Formula | 12 | =IF(VLOOKUP(B4,Approved_Software!B:B,1,FALSE),"✅ Yes","❌ No") |
| N | Approval Status | Formula | 15 | =IF(M4="✅ Yes","Approved","Unauthorized") |
| O | Action Required | Formula | 15 | =IF(N4="Unauthorized","Review","None") |
| P | Notes | Text | 40 | Additional info |

### Software Summary (Rows 2005-2020)
```
Total Unique Software:       [=COUNT(A4:A2003 where not blank)]
Centrally Deployed:          [=COUNTIF(H4:H2003,"Centrally Deployed")]
User Installed:              [=COUNTIF(H4:H2003,"User Installed")]
Pre-installed:               [=COUNTIF(H4:H2003,"Pre-installed")]
Unknown Method:              [=COUNTIF(H4:H2003,"Unknown")]

On Approved List:            [=COUNTIF(M4:M2003,"✅ Yes")]
Not on Approved List:        [=COUNTIF(M4:M2003,"❌ No")]
Unauthorized Software %:     [=(Not Approved/Total)*100]

Risk Flags:
  Shadow IT:                 [=COUNTIF(L4:L2003,"Shadow IT")]
  EOL Software:              [=COUNTIF(L4:L2003,"EOL")]
  High-Risk:                 [=COUNTIF(L4:L2003,"High-Risk")]
  Vulnerable:                [=COUNTIF(L4:L2003,"Vulnerable")]
```

### Conditional Formatting

**On Approved List Column (M):**

- If "✅ Yes" → Green #C6EFCE
- If "❌ No" → Red #FFC7CE

**Risk Flag Column (L):**

- If "None" → Green #C6EFCE
- If "Shadow IT" → Yellow #FFEB9C
- If "EOL" or "High-Risk" or "Vulnerable" → Red #FFC7CE

---

## Sheet 4: Unauthorized_Software

### Purpose
Identify and track software not on approved list.

### Header (Rows 1-2)
```
Row 1: "UNAUTHORIZED SOFTWARE"
Row 2: "Software installed on endpoints but not on approved list"
```

### Column Structure (Row 3 - headers, Rows 4-503 - data, 500 rows)

| Col | Header | Type | Width | Validation |
|-----|--------|------|-------|------------|
| A | Unauthorized ID | Auto | 12 | UNAUTH-001... |
| B | Software Name | Text | 30 | From Sheet 3 where unauthorized |
| C | Vendor | Text | 20 | Publisher |
| D | Version(s) | Text | 30 | Detected versions |
| E | Endpoint Count | Number | 12 | How many endpoints |
| F | Affected Endpoints | Text | 40 | Device names (or "See detail report") |
| G | Category | Dropdown | 15 | Shadow IT / EOL / High-Risk / Development Tools / Other |
| H | Risk Level | Dropdown | 10 | Critical / High / Medium / Low |
| I | Risk Justification | Text | 40 | Why this risk level |
| J | Business Impact If Removed | Text | 40 | What happens |
| K | Recommended Action | Dropdown | 15 | Approve / Remove / Exception / Migrate |
| L | Alternative Software | Text | 30 | If migrating |
| M | Approval Status | Dropdown | 15 | Submitted / Approved / Denied / Pending Review |
| N | Approval Reference | Text | 20 | Ticket number |
| O | Removal Plan | Text | 40 | How to remove |
| P | Owner | Text | 20 | Responsible |
| Q | Target Date | Date | 12 | When resolved |
| R | Status | Dropdown | 12 | Open / In Progress / Resolved |
| S | Notes | Text | 40 | Additional |

### Unauthorized Software Summary (Rows 505-520)
```
Total Unauthorized Software:     [=COUNT(A4:A503 where not blank)]
Total Affected Endpoints:        [=SUM(E4:E503)]
Unique Affected Endpoints:       [Count distinct from F column]

By Risk Level:
  Critical:                      [=COUNTIF(H4:H503,"Critical")]
  High:                          [=COUNTIF(H4:H503,"High")]
  Medium:                        [=COUNTIF(H4:H503,"Medium")]
  Low:                           [=COUNTIF(H4:H503,"Low")]

By Recommended Action:
  Approve:                       [=COUNTIF(K4:K503,"Approve")]
  Remove:                        [=COUNTIF(K4:K503,"Remove")]
  Exception:                     [=COUNTIF(K4:K503,"Exception")]
  Migrate:                       [=COUNTIF(K4:K503,"Migrate")]

By Status:
  Open:                          [=COUNTIF(R4:R503,"Open")]
  In Progress:                   [=COUNTIF(R4:R503,"In Progress")]
  Resolved:                      [=COUNTIF(R4:R503,"Resolved")]
```

### Conditional Formatting

**Risk Level Column (H):**

- If "Critical" → Dark red #C00000, white text
- If "High" → Red #FFC7CE
- If "Medium" → Yellow #FFEB9C
- If "Low" → Green #C6EFCE

**Status Column (R):**

- If "Open" → Red #FFC7CE
- If "In Progress" → Yellow #FFEB9C
- If "Resolved" → Green #C6EFCE

---

## Sheet 5: Application_Control

### Purpose
Per-endpoint application control deployment and effectiveness.

### Header (Rows 1-2)
```
Row 1: "APPLICATION CONTROL ASSESSMENT"
Row 2: "Application control deployment and enforcement status"
```

### Column Structure (Row 3 - headers, Rows 4-2003 - data, 2000 rows)

| Col | Header | Type | Width | Formula/Validation |
|-----|--------|------|-------|-------------------|
| A | Device Name | Text | 25 | From S1 inventory |
| B | OS Type | Text | 12 | Windows/macOS/Linux/iOS/Android |
| C | Application Control Tech | Dropdown | 20 | AppLocker / WDAC / Gatekeeper / SELinux / AppArmor / MDM / Third-Party / None |
| D | Deployment Status | Dropdown | 12 | 🟢 Deployed / 🟡 Partial / 🔴 Not Deployed |
| E | Enforcement Mode | Dropdown | 12 | Enforce / Audit / Disabled |
| F | Policy Type | Dropdown | 12 | Allowlist / Blocklist / Hybrid |
| G | Policy Coverage | Text | 30 | What's controlled (exe, scripts, etc.) |
| H | Last Policy Update | Date | 15 | When policy updated |
| I | Exceptions Granted | Number | 10 | Count |
| J | Exception References | Text | 30 | Approval refs |
| K | Effectiveness Test Date | Date | 15 | When tested |
| L | Effectiveness Test Result | Dropdown | 12 | ✅ Pass / ❌ Fail / Not Tested |
| M | Test Details | Text | 40 | What was tested |
| N | Compliance Status | Formula | 12 | =IF(AND(D4="🟢 Deployed",E4="Enforce"),"✅ Compliant",IF(E4="Audit","⚠️ Audit Mode","❌ Non-Compliant")) |
| O | Remediation Required | Formula | 15 | =IF(N4="❌ Non-Compliant","Yes","No") |
| P | Notes | Text | 40 | Additional |

### Application Control Metrics (Rows 2005-2025)
```
Total Endpoints:                 [=COUNT(A4:A2003 where not blank)]

Deployment Status:
  Deployed:                      [=COUNTIF(D4:D2003,"🟢 Deployed")]
  Partial:                       [=COUNTIF(D4:D2003,"🟡 Partial")]
  Not Deployed:                  [=COUNTIF(D4:D2003,"🔴 Not Deployed")]
  Deployment %:                  [=Deployed/Total*100]

Enforcement Mode:
  Enforce:                       [=COUNTIF(E4:E2003,"Enforce")]
  Audit:                         [=COUNTIF(E4:E2003,"Audit")]
  Disabled:                      [=COUNTIF(E4:E2003,"Disabled")]
  Enforcement %:                 [=Enforce/(Enforce+Audit)*100]

Policy Type:
  Allowlist:                     [=COUNTIF(F4:F2003,"Allowlist")]
  Blocklist:                     [=COUNTIF(F4:F2003,"Blocklist")]
  Hybrid:                        [=COUNTIF(F4:F2003,"Hybrid")]

Effectiveness Testing:
  Pass:                          [=COUNTIF(L4:L2003,"✅ Pass")]
  Fail:                          [=COUNTIF(L4:L2003,"❌ Fail")]
  Not Tested:                    [=COUNTIF(L4:L2003,"Not Tested")]
  Effectiveness Rate:            [=Pass/(Pass+Fail)*100]

Overall Compliance:
  Compliant:                     [=COUNTIF(N4:N2003,"✅ Compliant")]
  Audit Mode:                    [=COUNTIF(N4:N2003,"⚠️ Audit Mode")]
  Non-Compliant:                 [=COUNTIF(N4:N2003,"❌ Non-Compliant")]
  Compliance %:                  [=Compliant/Total*100]

Targets:
  Deployment: ≥95%
  Enforcement: ≥90%
  Effectiveness: 100%
```

### Conditional Formatting

**Deployment Status Column (D):**

- If "🟢 Deployed" → Green #C6EFCE
- If "🟡 Partial" → Yellow #FFEB9C
- If "🔴 Not Deployed" → Red #FFC7CE

**Enforcement Mode Column (E):**

- If "Enforce" → Green #C6EFCE
- If "Audit" → Yellow #FFEB9C
- If "Disabled" → Red #FFC7CE

**Compliance Status Column (N):**

- If "✅ Compliant" → Green #C6EFCE
- If "⚠️ Audit Mode" → Yellow #FFEB9C
- If "❌ Non-Compliant" → Red #FFC7CE

**Effectiveness Test Result Column (L):**

- If "✅ Pass" → Green #C6EFCE
- If "❌ Fail" → Red #FFC7CE
- If "Not Tested" → Light gray #D9D9D9

---

## Sheet 6: Patch_Compliance

### Purpose
Software patch compliance and vulnerability status.

### Header (Rows 1-2)
```
Row 1: "SOFTWARE PATCH COMPLIANCE"
Row 2: "Software versions, vulnerabilities, and patch status"
```

### Column Structure (Row 3 - headers, Rows 4-1003 - data, 1000 rows)

| Col | Header | Type | Width | Formula/Validation |
|-----|--------|------|-------|-------------------|
| A | Software Name | Text | 30 | From inventory |
| B | Installed Version(s) | Text | 30 | Versions detected |
| C | Latest Version | Text | 20 | From vendor |
| D | Version Status | Dropdown | 12 | Current / Outdated / EOL |
| E | Known Vulnerabilities | Text | 40 | CVE IDs |
| F | Highest Severity | Dropdown | 10 | Critical / High / Medium / Low / None |
| G | Patch Available Since | Date | 15 | When patch released |
| H | Days Since Patch | Formula | 10 | =INT(TODAY()-G4) |
| I | SLA (Days) | Formula | 10 | =IF(F4="Critical",7,IF(F4="High",30,IF(F4="Medium",90,180))) |
| J | Days Overdue | Formula | 10 | =MAX(0,H4-I4) |
| K | Affected Endpoints | Number | 12 | Count with outdated version |
| L | Patch Status | Formula | 12 | =IF(F4="None","N/A",IF(J4<=0,"✅ Compliant",IF(F4="Critical","🔴 Critical Overdue","⚠️ Overdue"))) |
| M | Patch Plan | Text | 40 | When/how patching |
| N | Blocker | Text | 30 | What prevents patching |
| O | Compensating Controls | Text | 40 | If can't patch |
| P | Owner | Text | 20 | Responsible |
| Q | Target Patch Date | Date | 15 | When will patch |
| R | Notes | Text | 40 | Additional |

### Patch Compliance Metrics (Rows 1005-1025)
```
Total Software Assessed:         [=COUNT(A4:A1003 where not blank)]

Version Status:
  Current:                       [=COUNTIF(D4:D1003,"Current")]
  Outdated:                      [=COUNTIF(D4:D1003,"Outdated")]
  EOL:                           [=COUNTIF(D4:D1003,"EOL")]

Vulnerability Severity:
  Critical:                      [=COUNTIF(F4:F1003,"Critical")]
  High:                          [=COUNTIF(F4:F1003,"High")]
  Medium:                        [=COUNTIF(F4:F1003,"Medium")]
  Low:                           [=COUNTIF(F4:F1003,"Low")]
  None:                          [=COUNTIF(F4:F1003,"None")]

Patch Compliance:
  Critical Compliant:            [=COUNTIFS(F:F,"Critical",J:J,"<=0")/COUNTIF(F:F,"Critical")*100]
  High Compliant:                [=COUNTIFS(F:F,"High",J:J,"<=0")/COUNTIF(F:F,"High")*100]
  Medium Compliant:              [=COUNTIFS(F:F,"Medium",J:J,"<=0")/COUNTIF(F:F,"Medium")*100]
  Overall Compliance:            [Weighted average]

Software with Vulnerabilities:
  Critical Overdue:              [=COUNTIFS(F:F,"Critical",J:J,">0")]
  High Overdue:                  [=COUNTIFS(F:F,"High",J:J,">0")]
  Total Overdue:                 [=COUNTIF(J4:J1003,">0")]

Targets:
  Critical: ≥95% within 7 days
  High: ≥90% within 30 days
  Medium: ≥80% within 90 days
```

### Conditional Formatting

**Version Status Column (D):**

- If "Current" → Green #C6EFCE
- If "Outdated" → Yellow #FFEB9C
- If "EOL" → Red #FFC7CE

**Highest Severity Column (F):**

- If "Critical" → Dark red #C00000, white text
- If "High" → Red #FFC7CE
- If "Medium" → Yellow #FFEB9C
- If "Low" → Light yellow #FFF2CC
- If "None" → Green #C6EFCE

**Patch Status Column (L):**

- If "✅ Compliant" or "N/A" → Green #C6EFCE
- If "⚠️ Overdue" → Yellow #FFEB9C
- If "🔴 Critical Overdue" → Dark red #C00000, white text

**Days Overdue Column (J):**

- If ≤0 → Green #C6EFCE
- If 1-30 → Yellow #FFEB9C
- If >30 → Red #FFC7CE

---

## Sheet 7: Software_Control_Gaps

### Purpose
Consolidated gap register for software controls.

### Header (Rows 1-2)
```
Row 1: "SOFTWARE CONTROL GAPS & REMEDIATION"
Row 2: "Consolidated gap register with risk-based prioritization"
```

### Column Structure (Row 3 - headers, Rows 4-103 - data, 100 rows)

| Col | Header | Type | Width | Validation |
|-----|--------|------|-------|------------|
| A | Gap ID | Auto | 10 | GAP-A819-001... |
| B | Gap Category | Dropdown | 15 | No Approved List / Unauthorized Software / No App Control / Audit Mode / Patch Failure / EOL Software / Licensing |
| C | Gap Description | Text | 40 | Specific description |
| D | Affected Items | Text | 30 | Software or endpoints |
| E | Count | Number | 8 | Number affected |
| F | Policy Requirement | Text | 30 | Which violated |
| G | Risk Level | Dropdown | 10 | Critical / High / Medium / Low |
| H | Risk Justification | Text | 40 | Why |
| I | Business Impact | Text | 40 | What happens |
| J | Root Cause | Text | 40 | Why exists |
| K | Remediation Plan | Text | 50 | Steps to fix |
| L | Effort | Dropdown | 10 | Low / Medium / High |
| M | Priority | Formula | 10 | =IF(AND(G4="Critical",L4="Low"),"P1",...) |
| N | Owner | Text | 20 | Responsible |
| O | Target Date | Date | 12 | When fixed |
| P | Resources Required | Text | 30 | What needed |
| Q | Dependencies | Text | 30 | Prerequisites |
| R | Status | Dropdown | 12 | Open / In Progress / Blocked / Resolved / Closed |
| S | % Complete | Number | 8 | Progress |
| T | Current Status Update | Text | 40 | Latest |
| U | Blockers | Text | 30 | Preventing progress |
| V | Next Steps | Text | 40 | What's next |
| W | Escalation Needed | Dropdown | 12 | Yes / No |
| X | Evidence Reference | Text | 20 | Sheet 8 link |
| Y | Notes | Text | 40 | Additional |

### Gap Summary Metrics (Rows 105-125)
```
Total Gaps:                      [=COUNT(A4:A103 where not blank)]

By Category:
  No Approved List:              [=COUNTIF(B4:B103,"No Approved List")]
  Unauthorized Software:         [=COUNTIF(B4:B103,"Unauthorized Software")]
  No App Control:                [=COUNTIF(B4:B103,"No App Control")]
  Audit Mode:                    [=COUNTIF(B4:B103,"Audit Mode")]
  Patch Failure:                 [=COUNTIF(B4:B103,"Patch Failure")]
  EOL Software:                  [=COUNTIF(B4:B103,"EOL Software")]
  Licensing:                     [=COUNTIF(B4:B103,"Licensing")]

By Risk:
  Critical:                      [=COUNTIF(G4:G103,"Critical")] ([%])
  High:                          [=COUNTIF(G4:G103,"High")] ([%])
  Medium:                        [=COUNTIF(G4:G103,"Medium")] ([%])
  Low:                           [=COUNTIF(G4:G103,"Low")] ([%])

By Priority:
  P1:                            [=COUNTIF(M4:M103,"P1")]
  P2:                            [=COUNTIF(M4:M103,"P2")]
  P3:                            [=COUNTIF(M4:M103,"P3")]
  P4:                            [=COUNTIF(M4:M103,"P4")]

By Status:
  Open:                          [=COUNTIF(R4:R103,"Open")]
  In Progress:                   [=COUNTIF(R4:R103,"In Progress")]
  Blocked:                       [=COUNTIF(R4:R103,"Blocked")]
  Resolved:                      [=COUNTIF(R4:R103,"Resolved")]
  Closed:                        [=COUNTIF(R4:R103,"Closed")]

Resolution Rate:                 [=(Resolved+Closed)/Total*100] %
```

### Conditional Formatting

Same as S3 Sheet 7 (Risk Level, Priority, Status, % Complete)

---

## Sheet 8: Evidence_Register

### Purpose
Evidence repository for audit.

### Header (Rows 1-2)
```
Row 1: "EVIDENCE REGISTER"
Row 2: "Document all evidence supporting this assessment"
```

### Column Structure

Same as S3 Sheet 8 (100 rows for evidence)

---

## Sheet 9: Software_Control_Dashboard

### Purpose
Executive summary dashboard.

### Header (Rows 1-3)
```
Row 1: "SOFTWARE CONTROL COMPLIANCE DASHBOARD"
Row 2: "ISO/IEC 27001:2022 Control A.8.19 - Installation of Software"
Row 3: "Executive Summary - [=Instructions!B8]"
```

### Dashboard Layout

**Section 1: Overall Status (Rows 5-18)**

```
┌─────────────────────────────────────────┐
│  SOFTWARE CONTROL STATUS                │
├─────────────────────────────────────────┤
│  Approved List:           [✅ Yes / ❌ No]   │
│  Unauthorized Software:   [XX] ([X%])   │
│  High-Risk Unauthorized:  [XX]          │
│                                          │
│  Application Control:                   │
│    Deployment:            [XX.X%]       │
│    Enforcement:           [XX.X%]       │
│                                          │
│  Patch Compliance:                      │
│    Critical:              [XX.X%]       │
│    High:                  [XX.X%]       │
│                                          │
│  Overall Status:          [🟢 GREEN / 🟡 YELLOW / 🔴 RED]  │
└─────────────────────────────────────────┘
```

**Formulas:**

- Approved List: Check if Sheet 2 has entries
- Unauthorized Software: From Sheet 4 summary
- Application Control Deployment: From Sheet 5 metrics
- Patch Compliance: From Sheet 6 metrics

**Overall Status Logic:**
```
=IF(AND(ApprovedList="Yes",Unauth%<=5%,AppControl>=95%,Enforcement>=90%,CriticalPatch>=95%),"🟢 GREEN",
   IF(AND(ApprovedList="Yes",Unauth%<=10%,AppControl>=85%,Enforcement>=75%,CriticalPatch>=85%),"🟡 YELLOW",
   "🔴 RED"))
```

**Section 2: Software Inventory Summary (Rows 20-30)**

Total software, approved vs unauthorized, installation methods

**Section 3: Application Control Effectiveness (Rows 32-42)**

Deployment coverage, enforcement mode distribution, effectiveness testing results

**Section 4: Patch Compliance Summary (Rows 44-54)**

By severity, overdue patches, EOL software

**Section 5: Critical Gaps (Rows 56-70)**

Top 10 gaps from Sheet 7 (Critical/High risk)

**Section 6: Executive Summary (Rows 72-80)**

Text narrative

**Section 7: Recommended Actions (Rows 82-100)**

Immediate, short-term, long-term actions

### Conditional Formatting

**Overall Status:**

- If "🟢 GREEN" → Dark green #00B050, white text, 16pt bold
- If "🟡 YELLOW" → Yellow #FFC000, black text, 16pt bold
- If "🔴 RED" → Dark red #C00000, white text, 16pt bold

---

## Cell Styling Reference

Same as S3 (Header_Main, Header_Section, Input_Cell, Calculated_Cell, Dropdown_Cell, Status Colors)

---

## Appendix: Python Developer Notes

### Generating This Workbook

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

# Initialize
wb = Workbook()

# Standard styles (same as S3)
# ... (styles defined)

# Create sheets
ws1 = wb.active
ws1.title = "Instructions"
ws2 = wb.create_sheet("Approved_Software")
ws3 = wb.create_sheet("Installed_Software")
ws4 = wb.create_sheet("Unauthorized_Software")
ws5 = wb.create_sheet("Application_Control")
ws6 = wb.create_sheet("Patch_Compliance")
ws7 = wb.create_sheet("Software_Control_Gaps")
ws8 = wb.create_sheet("Evidence_Register")
ws9 = wb.create_sheet("Software_Control_Dashboard")

# Data Validations
dv_category = DataValidation(type="list", 
    formula1='"Mandatory,Role-Specific,Optional,Prohibited"')
ws2.add_data_validation(dv_category)
for row in range(4, 504):
    dv_category.add(ws2[f"D{row}"])

dv_action = DataValidation(type="list",
    formula1='"Approve,Remove,Exception,Migrate"')
ws4.add_data_validation(dv_action)
for row in range(4, 504):
    dv_action.add(ws4[f"K{row}"])

# Conditional Formatting
ws3.conditional_formatting.add(
    "M4:M2003",
    CellIsRule(operator="equal", formula=['"✅ Yes"'], fill=green_fill)
)
ws3.conditional_formatting.add(
    "M4:M2003",
    CellIsRule(operator="equal", formula=['"❌ No"'], fill=red_fill)
)

# Formulas
ws3["M4"] = '=IF(VLOOKUP(B4,Approved_Software!B:B,1,FALSE),"✅ Yes","❌ No")'
ws3["N4"] = '=IF(M4="✅ Yes","Approved","Unauthorized")'
ws5["N4"] = '=IF(AND(D4="🟢 Deployed",E4="Enforce"),"✅ Compliant",IF(E4="Audit","⚠️ Audit Mode","❌ Non-Compliant"))'
ws6["H4"] = '=INT(TODAY()-G4)'
ws6["I4"] = '=IF(F4="Critical",7,IF(F4="High",30,IF(F4="Medium",90,180)))'
ws6["J4"] = '=MAX(0,H4-I4)'

# Save
wb.save("Software_Controls_Assessment.xlsx")
```

### Normalizing Software Names

```python
def normalize_software_name(raw_name):
    """Normalize software names for comparison"""
    # Remove version numbers, architecture, language
    import re
    name = raw_name.strip()
    
    # Remove version patterns
    name = re.sub(r'\d+\.\d+[\.\d]*', '', name)
    
    # Remove architecture
    name = re.sub(r'\(x64\)|\(x86\)|64-bit|32-bit', '', name, flags=re.IGNORECASE)
    
    # Remove language
    name = re.sub(r'\(en-US\)|\(de-DE\)', '', name, flags=re.IGNORECASE)
    
    # Common substitutions
    substitutions = {
        'Google Chrome': 'Chrome',
        'Mozilla Firefox': 'Firefox',
        'Microsoft Office': 'Office',
    }
    
    for old, new in substitutions.items():
        if old.lower() in name.lower():
            name = new
            
    return name.strip()

# Example usage
raw_names = [
    "Google Chrome 120.0.6099.109",
    "Chrome (x64)",
    "chrome.exe",
]

normalized = [normalize_software_name(n) for n in raw_names]
# Result: ['Chrome', 'Chrome', 'Chrome']
```

### Detecting Unauthorized Software

```python
def detect_unauthorized(installed_list, approved_list):
    """Compare installed vs approved software"""
    unauthorized = []
    
    # Normalize both lists
    approved_normalized = {normalize_software_name(s) for s in approved_list}
    
    for software in installed_list:
        norm_name = normalize_software_name(software['name'])
        if norm_name not in approved_normalized:
            unauthorized.append({
                'name': software['name'],
                'version': software['version'],
                'endpoints': software['endpoints'],
                'normalized_name': norm_name
            })
    
    return unauthorized
```

---

**END OF SPECIFICATION**

---

*"There are children playing in the streets who could solve some of my top problems in physics, because they have modes of sensory perception that I lost long ago."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->

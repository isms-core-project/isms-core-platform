**ISMS-IMP-A.8.2-3-5.S1-TG - Authentication Inventory & Methods**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Authentication Mechanisms Inventory |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Section 2.1 - Secure Authentication) |
| **Purpose** | Systematic inventory of authentication mechanisms across all systems, applications, and services to verify authentication security controls |
| **Target Audience** | Security Team, IT Operations, System Owners, IAM Team |
| **Assessment Type** | Technical Inventory & Configuration Review |
| **Review Cycle** | Monthly updates, Quarterly comprehensive review |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial assessment specification for authentication inventory | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.2-3-5.S1-UG.

---

# Technical Specification

# Excel Workbook Structure

## Workbook Overview

**Filename:** `ISMS-IMP-A.8.2-3-5.1_Authentication_Inventory_YYYYMMDD.xlsx`

**Sheet Structure:**

| Sheet # | Sheet Name | Purpose | Rows | Completion Method |
|---------|-----------|---------|------|-------------------|
| 1 | Instructions_Legend | User guide and reference | ~50 | Pre-populated |
| 2 | System_Auth_Inventory | System authentication mechanism inventory | 150+ | User completes |
| 3 | Auth_Protocol_Analysis | Authentication protocol security analysis | 50+ | User completes |
| 4 | SSO_Integration_Status | SSO adoption tracking | 100+ | User completes |
| 5 | Password_Policy_Compliance | Password policy per system | 30+ | User completes |
| 6 | MFA_Availability_Matrix | MFA method availability per system | ~30 | User completes |
| 7 | Legacy_Auth_Deprecation | Legacy authentication deprecation tracking | 40+ | User completes |
| 8 | Gap_Analysis | Authentication security gap analysis | 50+ | User completes |
| 9 | Evidence_Register | Evidence tracking | 30+ | User completes |
| 10 | Approval_Sign_Off | Three-level approval workflow | ~25 | User completes |

**Total Workbook:** 10 sheets for comprehensive authentication assessment

**Note:** The generator script creates all 10 sheets with proper structure, data validations, and formatting.

## Color Coding & Conditional Formatting

**Status Colors (Applied to Compliance Status columns)**:

- 🟢 **Green (Compliant)**: RGB(198, 239, 206) - Meets all policy requirements
- 🟡 **Yellow (Partial)**: RGB(255, 235, 156) - Meets some requirements, gaps exist
- 🔴 **Red (Non-Compliant)**: RGB(255, 199, 206) - Does not meet policy requirements
- ⚪ **Gray (N/A)**: RGB(217, 217, 217) - Not applicable

**Priority Colors (Applied to Gap Priority columns)**:

- 🔴 **Critical**: RGB(255, 0, 0) - Immediate action required
- 🟠 **High**: RGB(255, 153, 0) - Action within 90 days
- 🟡 **Medium**: RGB(255, 255, 0) - Action within 180 days
- 🟢 **Low**: RGB(146, 208, 80) - Ongoing improvement

---

# Sheet 2: Authentication Inventory (Primary Data Collection)

## Purpose

Comprehensive inventory of ALL authentication mechanisms across the organization.

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | System ID | 15 | Text | Free text | Unique system identifier (SYS-001, APP-WEB-001) |
| B | System Name | 25 | Text | Free text | Full system/application/service name |
| C | System Type | 18 | Dropdown | Web App, Database, API, Network Device, File Server, Email, VPN, Cloud Service, Other | System category |
| D | System Owner | 20 | Text | Free text | Person/team responsible for system |
| E | Authentication Provider | 20 | Dropdown | Entra ID, Okta, Google Workspace, Active Directory, LDAP, Local, RADIUS, TACACS+, Other | Where authentication happens |
| F | Authentication Method | 22 | Dropdown | Password Only, Password + MFA, SSO, SSO + MFA, Certificate, API Key, OAuth Token, Kerberos, Other | How users authenticate |
| G | Authentication Protocol | 20 | Dropdown | SAML 2.0, OAuth 2.0/OIDC, Kerberos, LDAP/LDAPS, RADIUS, TACACS+, SSH Keys, mTLS, Basic Auth, NTLM, Other | Technical protocol |
| H | Protocol Version | 15 | Text | Free text | Specific version if applicable (TLS 1.3, SAML 2.0, OAuth 2.0) |
| I | MFA Required | 12 | Dropdown | Yes, No, Partial | Is MFA enforced for this system? |
| J | Password Policy Enforced | 18 | Dropdown | Yes, No, N/A | If password-based, is policy enforced? |
| K | SSO Integrated | 15 | Dropdown | Yes, No, N/A | Is system integrated with SSO platform? |
| L | Compliance Status | 18 | Formula | Auto: Compliant, Partial, Non-Compliant | Calculated based on I, J, K |
| M | Configuration Notes | 30 | Text | Free text | Brief notes on authentication setup |
| N | Evidence Location | 25 | Text | Free text | Link to evidence (file path, URL) |

**Total Columns:** 14 (A-N)

## Data Validation Rules

**System Type (Column C):**
```
List: Web Application, Database, API, Network Device, File Server, Email Server, 
VPN, Cloud Service, Identity Provider, Other
```

**Authentication Provider (Column E):**
```
List: Entra ID, Okta, Google Workspace, Active Directory, LDAP, Local Authentication, 
RADIUS, TACACS+, AWS IAM, GCP IAM, Other
```

**Authentication Method (Column F):**
```
List: Password Only, Password + MFA, SSO, SSO + MFA, Certificate-Based, 
API Key, OAuth Token, Kerberos, Biometric, Other
```

**Authentication Protocol (Column G):**
```
List: SAML 2.0, OAuth 2.0/OIDC, Kerberos, LDAP/LDAPS, RADIUS, TACACS+, 
SSH Keys, mTLS, Basic Auth, NTLM, NTLM v2, Other
```

**MFA Required (Column I):**
```
List: Yes, No, Partial
```

**Password Policy Enforced (Column J):**
```
List: Yes, No, N/A
```

**SSO Integrated (Column K):**
```
List: Yes, No, N/A
```

## Compliance Status Calculation (Column L)

**Formula Logic:**
```excel
=IF(
    AND(I5="Yes", OR(J5="Yes", J5="N/A"), OR(K5="Yes", K5="N/A")),
    "Compliant",
    IF(
        OR(I5="Partial", AND(I5="No", J5="Yes")),
        "Partial",
        "Non-Compliant"
    )
)
```

**Compliance Rules:**

- **Compliant**: MFA = Yes AND (Password Policy = Yes OR N/A) AND (SSO = Yes OR N/A)
- **Partial**: MFA = Partial OR (MFA = No AND Password Policy = Yes)
- **Non-Compliant**: All other combinations

**Conditional Formatting:**

- Compliant → Green background
- Partial → Yellow background
- Non-Compliant → Red background

## Data Rows

**Header Row:** Row 4
**Data Rows:** Rows 5-103 (100 systems)
**Freeze Panes:** Row 5 (freeze header)

---

# Sheet 3: Password Policy Compliance

## Purpose

Track password policy compliance for systems using password-based authentication.

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | System ID | 15 | Text | Free text | Reference to Sheet 2 |
| B | System Name | 25 | Text | Free text | System name (from Sheet 2) |
| C | Minimum Length | 15 | Number | ≥8 | Password minimum length (characters) |
| D | Complexity Required | 18 | Dropdown | Yes, No | Uppercase, lowercase, numbers, symbols required? |
| E | Password Expiration | 18 | Number | ≥0 | Days until expiration (0 = no expiration) |
| F | Password History | 18 | Number | ≥0 | Number of passwords remembered |
| G | Breach Detection | 18 | Dropdown | Yes, No | Integration with HaveIBeenPwned or breach database? |
| H | Policy Compliance | 18 | Formula | Auto: Compliant, Non-Compliant | Meets ISMS-POL-A.8.2-3-5 requirements? |
| I | Gap Description | 30 | Text | Free text | If non-compliant, what's missing? |

**Total Columns:** 9 (A-I)

## Policy Compliance Calculation (Column H)

**Formula Logic:**
```excel
=IF(
    AND(C5>=12, G5="Yes"),
    "Compliant",
    "Non-Compliant"
)
```

**Policy Requirements (per ISMS-POL-A.8.2-3-5):**

- Minimum length: 12 characters (NIST SP 800-63B recommendation)
- Breach detection: Required (HaveIBeenPwned or similar)
- Expiration: No requirement (modern guidance: no forced expiration)
- Complexity: Optional (length more important than complexity)

**Conditional Formatting:**

- Compliant → Green
- Non-Compliant → Red

---

# Sheet 4: SSO Integration Status

## Purpose

Track SSO adoption across all web applications.

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Application Name | 25 | Text | Free text | Application name |
| B | Application Owner | 20 | Text | Free text | Person/team responsible |
| C | User Count | 12 | Number | ≥0 | Number of users |
| D | Business Criticality | 18 | Dropdown | High, Medium, Low | Application criticality |
| E | SSO Integrated | 15 | Dropdown | Yes, No | Is SSO implemented? |
| F | SSO Platform | 18 | Dropdown | Entra ID, Okta, Google, Other | SSO platform used |
| G | Integration Method | 18 | Dropdown | SAML 2.0, OIDC, Other | SSO protocol |
| H | Integration Date | 15 | Date | DD.MM.YYYY | When SSO was implemented |
| I | SSO Support | 15 | Dropdown | Yes, No, Unknown | Does app support SSO technically? |
| J | Planned Integration Date | 20 | Date | DD.MM.YYYY | If not integrated, when planned? |
| K | Blocking Issue | 30 | Text | Free text | Why not integrated? |

**Total Columns:** 11 (A-K)

## Conditional Formatting

**SSO Integrated (Column E):**

- Yes → Green
- No → Red

**Business Criticality (Column D):**

- High → Red (if SSO = No)
- Medium → Yellow (if SSO = No)
- Low → No special formatting

---

# Sheet 5: Summary Dashboard

## Purpose

Executive summary of authentication security posture with key metrics.

## Metrics Calculated

**Overall Authentication Security Score:**
```excel
=COUNTIF('Authentication Inventory'!L:L,"Compliant") / 
 COUNTA('Authentication Inventory'!L5:L103) * 100
```
Percentage of systems with compliant authentication.

**MFA Coverage:**
```excel
=COUNTIF('Authentication Inventory'!I:I,"Yes") / 
 COUNTA('Authentication Inventory'!I5:I103) * 100
```
Percentage of systems with MFA enforcement.

**Password Policy Compliance:**
```excel
=COUNTIF('Password Policy Compliance'!H:H,"Compliant") / 
 COUNTA('Password Policy Compliance'!H5:H103) * 100
```
Percentage of password-based systems with compliant policies.

**SSO Adoption:**
```excel
=COUNTIF('SSO Integration Status'!E:E,"Yes") / 
 COUNTA('SSO Integration Status'!E5:E103) * 100
```
Percentage of applications with SSO integration.

## Dashboard Layout

```
+------------------------------------------+
|  AUTHENTICATION SECURITY DASHBOARD       |
+------------------------------------------+
| Overall Security Score:        [XX%] 🟢  |
| MFA Coverage:                  [XX%] 🟢  |
| Password Policy Compliance:    [XX%] 🟡  |
| SSO Adoption:                  [XX%] 🟢  |
+------------------------------------------+
| CRITICAL GAPS (Immediate Action):        |
| - [Gap 1]                                |
| - [Gap 2]                                |
+------------------------------------------+
| REMEDIATION STATUS:                      |
| - In Progress: [X]                       |
| - Planned: [X]                           |
| - Blocked: [X]                           |
+------------------------------------------+
```

---

# Sheet 6: Evidence Register

## Purpose

Track all evidence collected for authentication assessment.

## Column Structure

| Col | Header | Width | Type | Description |
|-----|--------|-------|------|-------------|
| A | Evidence ID | 15 | Text | EV-A8235-1-001 |
| B | Evidence Type | 20 | Dropdown | Screenshot, Config Export, Report, Diagram, Document |
| C | System Reference | 20 | Text | System ID from Sheet 2 |
| D | Description | 30 | Text | Brief description of evidence |
| E | File Location | 30 | Text | Path to evidence file |
| F | Collection Date | 15 | Date | When evidence collected |
| G | Collected By | 18 | Text | Person who collected evidence |

---

# Sheet 7: Approval & Sign-Off

## Three-Level Approval

**Level 1 - Preparer:**

- Name, Title, Date, Signature

**Level 2 - Reviewer:**

- Name, Title, Date, Signature

**Level 3 - Approver (CISO):**

- Name, Title, Date, Signature

---

# Python Script Integration

## Script Purpose

Automated generation of authentication inventory workbook with pre-configured structure, validation rules, and formulas.

**Script:** `generate_a8235_1_authentication_inventory.py`

## Script Features

- Creates all 7 sheets with proper structure
- Applies data validation rules (dropdowns)
- Implements conditional formatting (color coding)
- Adds formulas for compliance calculations
- Sets column widths and freeze panes
- Generates professional formatting

## Running the Script

```bash
# Basic usage
python3 generate_a8235_1_authentication_inventory.py

# Custom date
python3 generate_a8235_1_authentication_inventory.py --date 2026-01-22

# Custom output path
python3 generate_a8235_1_authentication_inventory.py --output /path/to/file.xlsx
```

## Script Customization Points

Marked with `# CUSTOMIZE:` in script:

- Sheet names (organizational naming conventions)
- Dropdown options (additional authentication providers, methods)
- Data validation rules (custom compliance criteria)
- Conditional formatting thresholds (different scoring)

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly & Quality Checks

**Complete Document Structure:**
```
ISMS-IMP-A.8.2-3-5.1 - Authentication Inventory v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~500 lines)
│   ├── 1. Assessment Overview
│   ├── 2. Prerequisites
│   ├── 3. Assessment Workflow
│   ├── 4. Evidence Collection
│   ├── 5. Common Pitfalls
│   ├── 6. Quality Checklist
│   ├── 7. Interpreting Results
│   └── 8. Review & Approval
│
└── PART II: TECHNICAL SPECIFICATION (~350 lines)
    ├── 1. Workbook Structure
    ├── 2. Sheet 2: Authentication Inventory
    ├── 3. Sheet 3: Password Policy Compliance
    ├── 4. Sheet 4: SSO Integration Status
    ├── 5. Sheet 5: Summary Dashboard
    ├── 6. Sheet 6: Evidence Register
    ├── 7. Sheet 7: Approval & Sign-Off
    └── 8. Python Script Integration
```

**Quality Checks Before Finalizing:**

- [ ] All sections complete and accurate
- [ ] Cross-references correct (sheet numbers, policy references)
- [ ] No placeholder text ([TBD], [TODO])
- [ ] Dates in DD.MM.YYYY format
- [ ] Technical specification matches Python script
- [ ] User guide provides clear, actionable guidance
- [ ] Evidence requirements clearly documented

---

**END OF ISMS-IMP-A.8.2-3-5.1**

*Authentication is the gateway to all systems. Inventory it properly, secure it properly.*

*Remember Feynman: No checkbox compliance. Evidence-driven security.*

---

**END OF SPECIFICATION**

---

*"A man provided with paper, pencil, and rubber, and subject to strict discipline, is in effect a universal machine."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->

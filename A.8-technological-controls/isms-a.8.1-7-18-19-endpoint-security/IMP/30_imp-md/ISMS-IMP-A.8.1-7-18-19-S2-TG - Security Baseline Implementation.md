**ISMS-IMP-A.8.1-7-18-19-S2-TG - Security Baseline Implementation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Security Baseline Compliance and Enforcement |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.1.3 (Security Baselines), Section 2.1.4 (Encryption), Section 2.1.5 (Endpoint Management) |
| **Purpose** | Document security baseline configurations per endpoint type, assess baseline compliance, verify encryption status, and identify configuration drift to support endpoint device security requirements |
| **Target Audience** | Endpoint Administrators, Security Engineers, IT Operations, Compliance Officers, Configuration Managers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Weekly (automated compliance scans), Monthly (manual review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for security baseline assessment | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.1-7-18-19-S2-UG.

---

# Technical Specification

## Instructions for Workbook Developers

This section provides detailed specifications for developers creating the `Baseline_Compliance.xlsx` workbook (via Python script `generate_a817_2_security_baseline.py` or manual creation).

### Workbook Overview

**Workbook Name:** `Baseline_Compliance.xlsx`  
**Purpose:** Document security baseline compliance and encryption verification  
**Target Users:** Endpoint Administrators, Security Engineers, Compliance Officers, Auditors  
**Creation Method:** Python script (`generate_a817_2_security_baseline.py`) or manual Excel creation

### Sheet Structure

The workbook contains 6 worksheets:

1. **Baseline_Inventory** - Security baselines defined
2. **Compliance_Status** - Per-endpoint baseline compliance
3. **Encryption_Status** - Encryption verification
4. **Management_Enrollment** - MDM/agent enrollment status
5. **Configuration_Drift** - Configuration deviations
6. **Gaps** - Non-compliant endpoints and remediation

---

## Common Column Structure

### Data Types

Consistent with Endpoint_Inventory.xlsx (ISMS-IMP-A.8.1-7-18-19-S1):

| Data Type | Description | Example | Validation |
|-----------|-------------|---------|------------|
| **Text** | Free-form text | "Windows 11 Baseline" | Max 255 chars |
| **Text (Constrained)** | Dropdown list | "Enabled" | Must be from approved list |
| **Date** | Date value | 2026-01-25 | ISO format YYYY-MM-DD |
| **DateTime** | Date and time | 2026-01-25 14:30:00 | ISO format |
| **Integer** | Whole number | 42 | No decimals |
| **Percentage** | Percentage value | 95% | 0-100, formatted as % |
| **Status** | Status indicator | 🟢 Green | Emoji-based visual |

### Status Columns

Same as S1 (Endpoint_Inventory):

| Status | Emoji | Color | Threshold |
|--------|-------|-------|-----------|
| Green | 🟢 | Green fill (#C6EFCE), dark green text (#006100) | ≥90% |
| Yellow | 🟡 | Yellow fill (#FFEB9C), dark yellow text (#9C6500) | 70-89% |
| Red | 🔴 | Red fill (#FFC7CE), dark red text (#9C0006) | <70% |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Baseline_Inventory

**Purpose:** Document all security baselines defined

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Baseline_Name | Text | 30 | Required | None | Windows 11 Corporate Baseline, macOS 14 Corporate Baseline |
| B: Platform | Text (Constrained) | 20 | Dropdown | None | Windows 11, macOS 14, Ubuntu 22.04, iOS 17, Android 13 |
| C: Baseline_Source | Text | 40 | Optional | None | Microsoft Security Baseline, CIS Benchmark Level 1 |
| D: Version | Text | 20 | Optional | None | v2.0.0, Jan 2026 |
| E: Approval_Date | Date | 15 | Optional | None | Date CISO approved |
| F: Approval_Authority | Text | 20 | Optional | None | CISO, Security Committee |
| G: Enforcement_Method | Text (Constrained) | 20 | Dropdown | None | GPO, Intune Profile, Jamf Profile, Ansible |
| H: Control_Count | Integer | 15 | Optional | None | Number of security controls |
| I: Applicable_Endpoints | Text | 40 | Optional | None | All Windows 11 corporate laptops/desktops |
| J: Notes | Text | 40 | Optional | None | Baseline customization notes |

#### Dropdown Values

**Platform:** Windows 11, Windows 10, macOS 14, macOS 13, Ubuntu 22.04, RHEL 9, iOS 17, Android 13, Other  
**Enforcement_Method:** GPO, Intune Profile, Jamf Profile, Ansible, Puppet, Chef, SCCM, Manual

---

### Sheet 2: Compliance_Status

**Purpose:** Per-endpoint baseline compliance assessment

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Device_ID | Text | 20 | Required | From Inventory | Import from S1 |
| B: Hostname | Text | 25 | Required | From Inventory | Import from S1 |
| C: Device_Type | Text | 15 | Optional | From Inventory | Import from S1 |
| D: Operating_System | Text | 20 | Required | From Inventory | Import from S1 |
| E: Criticality | Text | 12 | Optional | From Inventory | Import from S1 |
| F: Baseline_Applied | Text | 30 | Required | None | Which baseline (Windows 11 Corporate, etc.) |
| G: Compliance_Scan_Date | DateTime | 20 | Required | None | Date of last scan |
| H: Total_Controls | Integer | 15 | Required | None | Total controls in baseline |
| I: Compliant_Controls | Integer | 18 | Required | None | Passed controls |
| J: Non_Compliant_Controls | Integer | 22 | None | `=H2-I2` | Failed controls |
| K: Compliance_Percentage | Percentage | 20 | None | `=I2/H2` | Compliance % |
| L: Compliance_Status | Status | 18 | None | `=IF(K2>=0.9,"🟢 Green",IF(K2>=0.7,"🟡 Yellow","🔴 Red"))` | Visual status |
| M: Top_Failures | Text | 50 | Optional | None | Top 3 failed controls |
| N: Scan_Tool | Text | 20 | Optional | None | Microsoft Defender, Jamf, SCAP |
| O: Notes | Text | 40 | Optional | None | Additional notes |

#### Conditional Formatting

Apply to column L (Compliance_Status):

- Green: Contains "Green" → Green fill, dark green text
- Yellow: Contains "Yellow" → Yellow fill, dark yellow text
- Red: Contains "Red" → Red fill, dark red text

Apply to column G (Compliance_Scan_Date):

- Stale scans (>7 days): `=TODAY()-G2>7` → Yellow fill
- Very stale (>30 days): `=TODAY()-G2>30` → Red fill

---

### Sheet 3: Encryption_Status

**Purpose:** Verify encryption status and key escrow

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Device_ID | Text | 20 | Required | From Inventory | Import from S1 |
| B: Hostname | Text | 25 | Required | From Inventory | Import from S1 |
| C: Device_Type | Text | 15 | Optional | From Inventory | Laptop, Desktop, Smartphone, Tablet |
| D: Ownership_Model | Text | 18 | Optional | From Inventory | Corporate-Owned, BYOD |
| E: Encryption_Required | Text (Constrained) | 20 | Dropdown | None | Yes, No |
| F: Encryption_Technology | Text (Constrained) | 22 | Dropdown | None | BitLocker, FileVault, LUKS, Built-in Mobile |
| G: Encryption_Status | Text (Constrained) | 18 | Dropdown | None | Enabled, Disabled, Not Supported |
| H: Encryption_Algorithm | Text | 18 | Optional | None | AES-256, AES-128 |
| I: Pre_Boot_Auth | Text (Constrained) | 15 | Dropdown | None | Enabled, Disabled, TPM-Only |
| J: Key_Escrow_Required | Text (Constrained) | 20 | Dropdown | None | Yes, No, N/A |
| K: Key_Escrow_Status | Text (Constrained) | 18 | Dropdown | None | Escrowed, Not Escrowed, N/A |
| L: Key_Escrow_Location | Text | 25 | Optional | None | Active Directory, Intune, Jamf, MBAM |
| M: Verification_Date | Date | 18 | Required | None | Date verified |
| N: Encryption_Compliance | Status | 20 | None | `=IF(AND(E2="Yes",G2="Enabled",OR(J2="No",K2="Escrowed")),"🟢 Compliant","🔴 Non-Compliant")` | Compliance status |
| O: Exception_Reason | Text | 40 | Optional | None | If not encrypted |
| P: Exception_Approved_By | Text | 20 | Optional | None | CISO |
| Q: Notes | Text | 40 | Optional | None | Additional notes |

#### Dropdown Values

**Encryption_Required:** Yes, No  
**Encryption_Technology:** BitLocker, FileVault, LUKS, Built-in Mobile (iOS/Android), Symantec, McAfee, Other  
**Encryption_Status:** Enabled, Disabled, Not Supported, Unknown  
**Pre_Boot_Auth:** Enabled, Disabled, TPM-Only, N/A  
**Key_Escrow_Required:** Yes, No, N/A  
**Key_Escrow_Status:** Escrowed, Not Escrowed, N/A, Unknown

---

### Sheet 4: Management_Enrollment

**Purpose:** Verify MDM/agent enrollment

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Device_ID | Text | 20 | Required | From Inventory | Import from S1 |
| B: Hostname | Text | 25 | Required | From Inventory | Import from S1 |
| C: Ownership_Model | Text | 18 | Optional | From Inventory | Corporate-Owned, BYOD |
| D: Management_Required | Text (Constrained) | 20 | Dropdown | None | Yes, MAM Only, No |
| E: Management_Platform | Text | 25 | Optional | None | Intune, Jamf Pro, SCCM, Google Workspace MDM |
| F: Enrollment_Status | Text (Constrained) | 18 | Dropdown | None | Enrolled, Not Enrolled, Enrollment Failed |
| G: Enrollment_Date | Date | 15 | Optional | None | Date enrolled |
| H: Last_Check_In | DateTime | 20 | Required | None | Last management check-in |
| I: Agent_Version | Text | 15 | Optional | None | Management agent version |
| J: Agent_Status | Text (Constrained) | 15 | Dropdown | None | Running, Stopped, Not Installed |
| K: Management_Capabilities | Text | 25 | Optional | None | Full MDM, MAM Only, Domain Joined |
| L: Enrollment_Compliance | Status | 20 | None | `=IF(AND(D2="Yes",F2="Enrolled"),"🟢 Compliant",IF(AND(D2="MAM Only",F2="Enrolled"),"🟢 Compliant","🔴 Non-Compliant"))` | Compliance |
| M: Check_In_Status | Status | 18 | None | `=IF(DAYS(TODAY(),H2)<=7,"🟢 Current",IF(DAYS(TODAY(),H2)<=30,"🟡 Stale","🔴 Very Stale"))` | Stale check-in flag |
| N: Notes | Text | 40 | Optional | None | Additional notes |

#### Dropdown Values

**Management_Required:** Yes, MAM Only, No  
**Enrollment_Status:** Enrolled, Not Enrolled, Enrollment Failed, Pending  
**Agent_Status:** Running, Stopped, Not Installed, Unknown

---

### Sheet 5: Configuration_Drift

**Purpose:** Track configuration deviations

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Drift_ID | Text | 15 | Required | None | DRIFT-001, DRIFT-002 |
| B: Endpoint | Text | 20 | Required | From Inventory | Device_ID experiencing drift |
| C: Baseline_Control | Text | 40 | Required | None | Control that drifted |
| D: Expected_Value | Text | 20 | Required | None | Approved baseline value |
| E: Actual_Value | Text | 20 | Required | None | Current detected value |
| F: Drift_Detected_Date | DateTime | 20 | Required | None | When drift detected |
| G: Root_Cause | Text | 50 | Optional | None | Why drift occurred |
| H: Severity | Text (Constrained) | 12 | Dropdown | None | Critical, High, Medium, Low |
| I: Priority | Status | 12 | None | `=IF(H2="Critical","🔴 Critical",IF(H2="High","🟡 High",IF(H2="Medium","🟢 Medium","⚪ Low")))` | Visual priority |
| J: Remediation_Action | Text | 60 | Required | None | What to do |
| K: Remediation_Owner | Text | 20 | Optional | None | Responsible person |
| L: Target_Date | Date | 15 | Optional | None | Target completion |
| M: Remediation_Status | Text (Constrained) | 18 | Dropdown | None | Not Started, In Progress, Completed, Deferred |
| N: Verification_Date | Date | 18 | Optional | None | Date verified fixed |
| O: Notes | Text | 40 | Optional | None | Additional notes |

#### Dropdown Values

**Severity:** Critical, High, Medium, Low  
**Remediation_Status:** Not Started, In Progress, Completed, Deferred

---

### Sheet 6: Gaps

**Purpose:** Non-compliant endpoints and remediation

Same structure as Sheet 6 in Endpoint_Inventory (S1), adapted for baseline compliance gaps.

---

## Cell Styling Reference

Same as ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint_Inventory):

- Header Row: Dark blue (#002060), white text, bold, center aligned
- Freeze Panes: Row 2
- AutoFilter: Enabled
- Alternating Rows: White / Light gray (#F2F2F2)
- Status Columns: Conditional formatting (Green/Yellow/Red)

---

## Appendix: Technical Notes for Python Developers

### Script: `generate_a817_2_security_baseline.py`

Same Python libraries and patterns as `generate_a817_1_endpoint_inventory.py`.

**Key Differences:**

- Import endpoint data from Endpoint_Inventory.xlsx (S1 must exist)
- Generate 6 worksheets focused on baseline compliance
- Calculate compliance percentages, encryption coverage, enrollment coverage
- Apply conditional formatting for compliance status, encryption compliance, enrollment compliance

**Sample Code Snippet (Compliance Percentage Calculation):**

```python
# Add formula for Compliance_Percentage (column K)
for row in range(2, max_row + 1):
    ws_compliance[f'K{row}'] = f'=I{row}/H{row}'  # Compliant / Total
    
# Add formula for Compliance_Status (column L)
for row in range(2, max_row + 1):
    ws_compliance[f'L{row}'] = f'=IF(K{row}>=0.9,"🟢 Green",IF(K{row}>=0.7,"🟡 Yellow","🔴 Red"))'
```

---

**END OF SPECIFICATION**

---

*"Any man whose errors take ten years to correct is quite a man."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->

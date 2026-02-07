**ISMS-IMP-A.8.12.3-TG - Channel Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention


---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | DLP Channel Coverage and Policy Effectiveness |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention Policy) - Section 2.2 |
| **Purpose** | Assess DLP deployment across all data egress channels to identify coverage gaps, verify policy enforcement, and ensure no data exfiltration bypass paths exist |
| **Target Audience** | DLP Administrators, Security Engineers, Network Engineers, SOC Analysts, CISO, Compliance Officers |
| **Assessment Type** | Technical Coverage & Policy Verification |
| **Review Cycle** | Quarterly or After Network/Application Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Channel Coverage assessment | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Python Developers, Excel Workbook Developers, Quality Assurance, ISMS Implementation Team

---

# Workbook Structure Overview

## Sheet List

**Total Sheets:** 12

| # | Sheet Name | Rows (approx) | Purpose | User Input |
|---|------------|---------------|---------|------------|
| 1 | Instructions_Legend | 50 | User guidance, metadata, legend | Metadata only (yellow cells) |
| 2 | Channel_Overview | 30 | Complete channel catalog overview | Yes (all egress channels) |
| 3 | Email_Channel | 20 | Email DLP assessment | Yes (email DLP config) |
| 4 | Web_Cloud_Channel | 30 | Web/proxy/cloud/CASB DLP assessment | Yes (web/cloud DLP config) |
| 5 | Endpoint_Channel | 30 | Endpoint DLP (USB, clipboard, print) | Yes (endpoint controls) |
| 6 | Network_Channel | 20 | Network protocols (FTP, SMB, etc.) | Yes (network DLP) |
| 7 | Application_Channel | 20 | Database, API, app-level controls | Yes (app controls) |
| 8 | Mobile_Channel | 25 | Mobile devices, MDM, MAM | Yes (mobile DLP) |
| 9 | Coverage_Metrics | 35 | Coverage metrics and testing results | Yes (test outcomes) |
| 10 | Gap_Analysis | 45 | Gaps and remediation | Yes (gap details) |
| 11 | Evidence_Register | 110 | Evidence tracking | Yes (evidence entries) |
| 12 | Summary_Dashboard | 40 | KPIs, coverage heatmap | No (formulas) |

**Total Assessment Items:** ~70 channel coverage checkpoints

---

# Detailed Sheet Specifications

## Sheet: Instructions_Legend

**Purpose:** User guidance, assessment metadata, response value legend

**Layout:**

- Rows 1-5: Document header
- Rows 7-12: Organization metadata (yellow cells)
- Rows 14-30: Instructions
- Rows 32-40: Response value legend
- Rows 42-50: Coverage status color coding

**Organization Metadata:**

| Row | Field | Type | Example |
|-----|-------|------|---------|
| 7 | Assessment Date | Date | 21.01.2026 |
| 8 | Completed By | Text | Jane Doe |
| 9 | Role | Text | DLP Administrator |
| 10 | Organization | Text | [Organization] |
| 11 | Review Cycle | Text | Quarterly |
| 12 | Next Review | Date | 21.04.2026 |

---

## Sheet: Channel_Inventory

**Purpose:** Comprehensive inventory of all data egress channels

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Channel ID | Text | 15 | None | Unique ID (CH-001) |
| B | Channel Category | Dropdown | 20 | 7 categories | Email/Web/Endpoint/etc. |
| C | Channel Sub-Type | Text | 25 | None | SMTP, USB, Dropbox, etc. |
| D | Technology/Service | Text | 30 | None | Exchange, Zscaler, etc. |
| E | User Population | Text | 20 | None | "All users", "Finance" |
| F | Business Criticality | Dropdown | 18 | Critical/High/Medium/Low | Impact if blocked |
| G | Data Sensitivity | Dropdown | 18 | Classification levels | Restricted/Confidential/etc. |
| H | Sanctioned Status | Dropdown | 18 | Pre-defined list | Sanctioned/Unsanctioned |
| I | DLP Coverage | Dropdown | 15 | Yes/No/Partial/Planned | Is DLP deployed? |
| J | Coverage Notes | Text (wrap) | 35 | None | Details, exceptions |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| L | Evidence ID | Text | 15 | None | A812-3-INV-001 |

**Pre-Populated Examples (Gray rows 6-12):**

| Channel ID | Category | Sub-Type | Technology |
|------------|----------|----------|------------|
| CH-001 | Email | SMTP Outbound | Microsoft Exchange |
| CH-002 | Web | HTTPS Upload | Zscaler Web Proxy |
| CH-003 | Endpoint | USB Storage | Endpoint DLP Agent |
| CH-004 | Cloud | Cloud Storage | Microsoft Purview |
| CH-005 | Mobile | iOS Devices | Intune MDM |
| CH-006 | Network | FTP Outbound | Network Firewall |
| CH-007 | Application | Database Export | Database ACLs |

**Data Rows:** 30 total (7 examples + 23 blank)

**Data Validation:**

```python
# Column B: Channel Category
validation_category = {
    'type': 'list',
    'formula1': '"Email,Web,Endpoint,Network,Cloud,Mobile,Application"',
    'allow_blank': False
}

# Column F: Business Criticality
validation_criticality = {
    'type': 'list',
    'formula1': '"Critical,High,Medium,Low"',
    'allow_blank': False
}

# Column G: Data Sensitivity
validation_sensitivity = {
    'type': 'list',
    'formula1': '=Classification_Levels!$A$2:$A$10',  # Dynamic reference
    'allow_blank': False
}

# Column H: Sanctioned Status
validation_sanctioned = {
    'type': 'list',
    'formula1': '"Sanctioned,Unsanctioned,Shadow IT,Under Review"',
    'allow_blank': False
}

# Column I: DLP Coverage
validation_coverage = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False
}

# Column K: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column I (DLP Coverage):
  - "Yes" = Green fill
  - "Partial" = Yellow fill
  - "No" = Red fill
  - "Planned" = Light blue fill
- Column K (Status): Standard status colors

---

## Sheet: Email_Channel

**Purpose:** Detailed email DLP assessment

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Email System | Text | 25 | None | Exchange, M365, Gmail |
| B | DLP Deployment | Dropdown | 22 | Gateway/Cloud/Both | Where DLP is |
| C | Coverage Scope | Text | 20 | None | "All users" or % |
| D | Enforcement Mode | Dropdown | 20 | Block/Encrypt/Prompt/Monitor | Action taken |
| E | Attachment Scanning | Dropdown | 20 | Yes/No/Partial | Files scanned |
| F | Encrypted Email Handling | Dropdown | 25 | Before/After/Not Scanned | S/MIME, PGP |
| G | External Domain Policy | Dropdown | 22 | Block/Allow+DLP/Allow | External send |
| H | Webmail Blocking | Dropdown | 18 | Yes/No/Partial | Gmail, Yahoo blocked |
| I | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test done? |
| J | Test Result | Dropdown | 15 | Blocked/Allowed/Alert Only | Test outcome |
| K | False Positive Rate (%) | Number | 18 | 0-100 | If measured |
| L | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| M | Evidence ID | Text | 15 | None | A812-3-EML-001 |

**Pre-Populated Examples (Gray rows 6-8):**

| System | DLP Deployment | Scope | Enforcement | Attachment Scanning |
|--------|----------------|-------|-------------|---------------------|
| Microsoft Exchange | Gateway + Cloud (Purview) | All users (100%) | Block | Yes |
| Google Workspace | Cloud Service (native DLP) | All users (100%) | User Prompt | Yes |

**Data Rows:** 20 total (2 examples + 18 blank for different email flows/systems)

**Data Validation:**

```python
# Column B: DLP Deployment
validation_deployment = {
    'type': 'list',
    'formula1': '"Gateway,Cloud Service,Both,None"',
    'allow_blank': False
}

# Column D: Enforcement Mode
validation_enforcement = {
    'type': 'list',
    'formula1': '"Block,Encrypt,User Prompt,Monitor Only,None"',
    'allow_blank': False
}

# Column E, H, I: Yes/No/Partial
validation_ynp = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,N/A"',
    'allow_blank': False
}

# Column F: Encrypted Email
validation_encrypted = {
    'type': 'list',
    'formula1': '"Scanned Before Encryption,Scanned After Decryption,Not Scanned,N/A"',
    'allow_blank': False
}

# Column G: External Domain
validation_external = {
    'type': 'list',
    'formula1': '"Blocked,Allowed with DLP,Allowed without DLP,Requires Approval"',
    'allow_blank': False
}

# Column J: Test Result
validation_testresult = {
    'type': 'list',
    'formula1': '"Blocked (Pass),Allowed (Fail),Alert Only (Partial),Not Tested"',
    'allow_blank': False
}

# Column K: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}
```

**Conditional Formatting:**

- Column D (Enforcement Mode):
  - "Block" or "Encrypt" = Green (compliant for Restricted data)
  - "User Prompt" = Yellow (acceptable for Confidential)
  - "Monitor Only" or "None" = Red (non-compliant for sensitive data)
- Column J (Test Result):
  - "Blocked (Pass)" = Green
  - "Alert Only (Partial)" = Yellow
  - "Allowed (Fail)" = Red

---

## Sheet: Web_Channel

**Purpose:** Web proxy, CASB, and cloud storage DLP assessment

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Web Technology | Text | 25 | None | Zscaler, Netskope, Forcepoint |
| B | Deployment Type | Dropdown | 20 | Proxy/CASB/Cloud Gateway | Architecture |
| C | SSL/TLS Inspection | Dropdown | 20 | Enabled/Partial/Disabled | HTTPS decrypt |
| D | Cloud Storage Blocking | Text (wrap) | 30 | None | Which services blocked |
| E | Webmail Blocking | Dropdown | 20 | Blocked/Allowed/Partial | Gmail, Yahoo, etc. |
| F | File Upload DLP | Dropdown | 20 | Block/Monitor/None | Upload scanning |
| G | Coverage Scope | Text | 20 | None | "All users" or % |
| H | Bypass Paths | Text (wrap) | 30 | None | VPN, direct, mobile |
| I | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test done? |
| J | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| L | Evidence ID | Text | 15 | None | A812-3-WEB-001 |

**Pre-Populated Examples (Gray rows 6-8):**

| Technology | Type | SSL Inspection | Cloud Blocking | Webmail Blocking |
|------------|------|----------------|----------------|------------------|
| Zscaler Internet Access | Cloud Proxy | Enabled | Dropbox, Box personal, WeTransfer | Blocked |
| Netskope CASB | CASB | Enabled | OneDrive personal, Google Drive personal | Allowed with DLP |

**Data Rows:** 25 total (2 examples + 23 blank)

**Data Validation:**

```python
# Column B: Deployment Type
validation_deployment = {
    'type': 'list',
    'formula1': '"On-Premise Proxy,Cloud Proxy,CASB,Cloud Gateway,None"',
    'allow_blank': False
}

# Column C: SSL/TLS Inspection
validation_ssl = {
    'type': 'list',
    'formula1': '"Enabled (All Traffic),Enabled (Selective),Disabled,N/A"',
    'allow_blank': False
}

# Column E: Webmail Blocking
validation_webmail = {
    'type': 'list',
    'formula1': '"Blocked,Allowed with DLP,Allowed without DLP,Partial"',
    'allow_blank': False
}

# Column F: File Upload DLP
validation_upload = {
    'type': 'list',
    'formula1': '"Block,Monitor Only,User Prompt,None"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column C (SSL Inspection):
  - "Enabled (All Traffic)" = Green (required for HTTPS DLP)
  - "Enabled (Selective)" = Yellow (gaps exist)
  - "Disabled" = Red (blind to encrypted uploads)
- Column F (File Upload DLP):
  - "Block" = Green
  - "Monitor Only" or "User Prompt" = Yellow
  - "None" = Red

---

## Sheet: Endpoint_Channel

**Purpose:** Endpoint DLP covering USB, clipboard, print, screen capture

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Endpoint Control | Text | 25 | None | USB, Clipboard, Print, etc. |
| B | DLP Agent Deployed | Dropdown | 18 | Yes/No/Partial | Agent coverage |
| C | Agent Coverage (%) | Number | 18 | 0-100 | % of endpoints |
| D | Control Type | Dropdown | 20 | Block/Encrypt/Log Only/None | Action |
| E | OS Coverage | Text | 25 | None | Windows, macOS, Linux |
| F | Offline Protection | Dropdown | 18 | Yes/No/Partial | Works when offline? |
| G | User Override Allowed | Dropdown | 18 | Yes/No/With Justification | Can users bypass? |
| H | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test done? |
| I | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| J | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| K | Evidence ID | Text | 15 | None | A812-3-EPT-001 |

**Pre-Populated Endpoint Controls (Gray rows 6-13):**

| Control | Description | Typical Policy |
|---------|-------------|----------------|
| USB Storage | USB drives, external HDDs | Block or Encrypt-Only |
| Clipboard | Copy/paste between apps | Block external paste |
| Print | Printing documents | Watermark or Require Justification |
| Screen Capture | Screenshots, screen recording | Block or Watermark |
| Bluetooth | File transfer via Bluetooth | Block |
| WiFi Direct / AirDrop | Peer-to-peer file transfer | Block |
| Local File Operations | File rename, move, delete | Log Only |
| CD/DVD Burning | Optical media writes | Block |

**Data Rows:** 30 total (8 pre-populated controls + 22 blank for custom controls)

**Data Validation:**

```python
# Column B: DLP Agent Deployed
validation_agent = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned"',
    'allow_blank': False
}

# Column C: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column D: Control Type
validation_control = {
    'type': 'list',
    'formula1': '"Block,Encrypt Only,Read-Only,Log Only,User Prompt,None"',
    'allow_blank': False
}

# Column F, G, H: Yes/No variations
validation_yesno = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,With Justification,N/A"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column C (Agent Coverage):
  - ≥95% = Green
  - 80-94% = Yellow
  - <80% = Red
- Column D (Control Type):
  - "Block" or "Encrypt Only" = Green
  - "Read-Only" or "Log Only" = Yellow
  - "User Prompt" or "None" = Red (for Restricted data channels)

---

## Sheet: Network_Channel

**Purpose:** Network protocol DLP (FTP, SMB, database connections)

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Protocol/Service | Text | 25 | None | FTP, SFTP, SMB, RDP |
| B | Network DLP Deployed | Dropdown | 20 | Yes/No/Partial | Is DLP monitoring? |
| C | Firewall Policy | Dropdown | 20 | Blocked/Allowed/Conditional | Outbound rule |
| D | DLP Action | Dropdown | 18 | Block/Monitor/None | If DLP deployed |
| E | Coverage Scope | Text | 20 | None | Which networks/sites |
| F | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test |
| G | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| H | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| I | Evidence ID | Text | 15 | None | A812-3-NET-001 |

**Pre-Populated Network Protocols (Gray rows 6-11):**

| Protocol | Typical Use | Common Policy |
|----------|-------------|---------------|
| FTP/FTPS (Port 21/990) | File transfer | Blocked outbound |
| SFTP (Port 22) | Secure file transfer | Allowed to known servers only |
| SMB/CIFS (Port 445) | File sharing | Blocked outbound (internal only) |
| RDP (Port 3389) | Remote desktop | Blocked outbound (VPN only) |
| Database Protocols (1433, 3306, 5432) | Direct DB access | Blocked from endpoints |
| rsync (Port 873) | File synchronization | Blocked outbound |

**Data Rows:** 20 total (6 pre-populated + 14 blank)

**Data Validation:**

```python
# Column B: Network DLP
validation_dlp = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False
}

# Column C: Firewall Policy
validation_firewall = {
    'type': 'list',
    'formula1': '"Blocked,Allowed (All),Allowed (Specific Destinations),Conditional,None"',
    'allow_blank': False
}

# Column D: DLP Action
validation_action = {
    'type': 'list',
    'formula1': '"Block,Monitor Only,Alert Only,None"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column C (Firewall Policy):
  - "Blocked" = Green (preferred for FTP, SMB outbound)
  - "Allowed (Specific Destinations)" = Yellow (acceptable with DLP)
  - "Allowed (All)" = Red (uncontrolled egress)

---

## Sheet: Cloud_Channel

**Purpose:** SaaS applications, cloud storage, API-based DLP

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Cloud Application | Text | 30 | None | M365, Salesforce, etc. |
| B | Application Type | Dropdown | 20 | SaaS/IaaS/PaaS | Service model |
| C | CASB Coverage | Dropdown | 18 | Yes/No/Partial | CASB monitoring |
| D | Native DLP Enabled | Dropdown | 20 | Yes/No/Partial | App's built-in DLP |
| E | DLP Policy Type | Dropdown | 25 | API-based/Proxy-based/Both | How DLP works |
| F | Data Classification Integration | Dropdown | 25 | Yes/No/Partial | Reads doc labels |
| G | Sharing Controls | Dropdown | 20 | Enforced/Advisory/None | External sharing |
| H | OAuth App Review | Dropdown | 20 | Enabled/Disabled | Third-party apps |
| I | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test |
| J | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| L | Evidence ID | Text | 15 | None | A812-3-CLD-001 |

**Pre-Populated Cloud Apps (Gray rows 6-10):**

| Application | Type | Native DLP | Typical Policy |
|-------------|------|------------|----------------|
| Microsoft 365 | SaaS | Yes (Purview) | Classification-based DLP |
| Google Workspace | SaaS | Yes (native DLP) | Context-aware policies |
| Salesforce | SaaS | Yes (Shield) | Sharing controls |
| Box | SaaS | Yes (Shield) | Classification-based |
| AWS S3 (if used) | IaaS | No (via CASB) | CASB monitoring |

**Data Rows:** 25 total (5 examples + 20 blank)

**Data Validation:**

```python
# Column B: Application Type
validation_apptype = {
    'type': 'list',
    'formula1': '"SaaS,IaaS,PaaS,Hybrid,Other"',
    'allow_blank': False
}

# Column C, D, F, H, I: Yes/No/Partial
validation_ynp = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False
}

# Column E: DLP Policy Type
validation_policytype = {
    'type': 'list',
    'formula1': '"API-based,Proxy-based,Inline,Hybrid,None"',
    'allow_blank': False
}

# Column G: Sharing Controls
validation_sharing = {
    'type': 'list',
    'formula1': '"Enforced (Block),Enforced (Approval),Advisory Only,None"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column D (Native DLP):
  - "Yes" = Green (preferred)
  - "Partial" = Yellow (some features enabled)
  - "No" = Red (requires CASB)
- Column G (Sharing Controls):
  - "Enforced (Block)" = Green
  - "Enforced (Approval)" = Yellow
  - "Advisory Only" or "None" = Red

---

## Sheet: Mobile_Channel

**Purpose:** Mobile device DLP, MDM/MAM, BYOD assessment

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Device Type | Dropdown | 20 | iOS/Android/Other | Platform |
| B | Ownership Model | Dropdown | 20 | Corporate/BYOD/Mixed | Who owns device |
| C | MDM Enrollment | Dropdown | 20 | Mandatory/Optional/None | Enrollment policy |
| D | Enrollment Rate (%) | Number | 18 | 0-100 | % of devices enrolled |
| E | MAM/DLP App Deployed | Dropdown | 20 | Yes/No/Partial | DLP app coverage |
| F | Containerization | Dropdown | 20 | Yes/No/Partial | Corporate data isolated |
| G | Copy/Paste Restrictions | Dropdown | 22 | Enforced/Advisory/None | Between apps |
| H | Save-As Blocking | Dropdown | 18 | Yes/No/Partial | Save to device storage |
| I | Sharing Controls | Dropdown | 20 | Enforced/Advisory/None | AirDrop, Bluetooth |
| J | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test |
| K | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| L | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| M | Evidence ID | Text | 15 | None | A812-3-MOB-001 |

**Pre-Populated Device Types (Gray rows 6-9):**

| Device Type | Ownership | MDM Mandatory | Typical DLP Controls |
|-------------|-----------|---------------|----------------------|
| iOS (iPhone/iPad) | Corporate-Owned | Yes | Full MDM + MAM + DLP app |
| iOS (iPhone/iPad) | BYOD | Yes | MAM + DLP app (container) |
| Android (Corporate) | Corporate-Owned | Yes | Full MDM + MAM + DLP app |
| Android (BYOD) | BYOD | Optional | MAM only (if enrolled) |

**Data Rows:** 25 total (4 examples + 21 blank)

**Data Validation:**

```python
# Column A: Device Type
validation_device = {
    'type': 'list',
    'formula1': '"iOS,Android,Windows Mobile,Other"',
    'allow_blank': False
}

# Column B: Ownership
validation_ownership = {
    'type': 'list',
    'formula1': '"Corporate-Owned,BYOD,Mixed"',
    'allow_blank': False
}

# Column C: MDM Enrollment
validation_mdm = {
    'type': 'list',
    'formula1': '"Mandatory (Blocked if Unenrolled),Mandatory (Advisory),Optional,None"',
    'allow_blank': False
}

# Column D: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column E, F, H: Yes/No/Partial
validation_ynp = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False
}

# Column G, I: Enforcement levels
validation_enforcement = {
    'type': 'list',
    'formula1': '"Enforced,Advisory Only,None"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column D (Enrollment Rate):
  - 100% = Green
  - 90-99% = Yellow
  - <90% = Red (gap in mobile coverage)
- Column G, I (Restrictions):
  - "Enforced" = Green
  - "Advisory Only" = Yellow
  - "None" = Red

---

## Sheet: Application_Channel

**Purpose:** Application-level DLP (database, API, reporting)

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Application/System | Text | 30 | None | Database name, API |
| B | Application Type | Dropdown | 20 | Database/API/Reporting/BI | System type |
| C | Export Restrictions | Dropdown | 22 | Enforced/Advisory/None | Can users export? |
| D | Row Limit (if DB) | Text | 18 | None | Max rows per query |
| E | API Rate Limiting | Dropdown | 20 | Enforced/None | Prevent bulk export |
| F | Approval Required | Dropdown | 20 | Yes/No/Conditional | For large exports |
| G | Output DLP Scanning | Dropdown | 20 | Yes/No/Partial | Scan exports |
| H | Audit Logging | Dropdown | 18 | Yes/No/Partial | Log all exports |
| I | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test |
| J | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| L | Evidence ID | Text | 15 | None | A812-3-APP-001 |

**Pre-Populated Systems (Gray rows 6-10):**

| System | Type | Export Restrictions | Row Limit |
|--------|------|---------------------|-----------|
| HR Database (Oracle) | Database | Enforced (HR only) | 10,000 rows |
| Salesforce CRM | SaaS/API | Advisory | API rate: 100K calls/day |
| Tableau Server | BI/Reporting | None | Unlimited |
| Customer Database (SQL) | Database | Enforced (Approval >100K rows) | 100,000 rows |
| REST API (Custom) | API | Rate limiting | 1000 calls/hour |

**Data Rows:** 20 total (5 examples + 15 blank)

**Data Validation:**

```python
# Column B: Application Type
validation_apptype = {
    'type': 'list',
    'formula1': '"Database,API,Reporting Tool,BI/Analytics,Data Warehouse,Other"',
    'allow_blank': False
}

# Column C, G, H: Enforcement
validation_enforcement = {
    'type': 'list',
    'formula1': '"Enforced,Advisory Only,None"',
    'allow_blank': False
}

# Column E: API Rate Limiting
validation_ratelimit = {
    'type': 'list',
    'formula1': '"Enforced (Hard Limit),Enforced (Soft Limit),Advisory Only,None"',
    'allow_blank': False
}

# Column F: Approval Required
validation_approval = {
    'type': 'list',
    'formula1': '"Yes (Always),Yes (Large Exports),Conditional,No"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column C (Export Restrictions):
  - "Enforced" = Green
  - "Advisory Only" = Yellow
  - "None" = Red (uncontrolled exports)
- Column E (API Rate Limiting):
  - "Enforced (Hard Limit)" = Green
  - "Enforced (Soft Limit)" or "Advisory Only" = Yellow
  - "None" = Red

---

## Sheet: Bypass_Testing

**Purpose:** Document bypass testing methodology and results

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Test ID | Text | 12 | Auto: TEST-001 |
| B | Channel Tested | Dropdown | 20 | Which channel |
| C | Test Date | Date | 15 | DD.MM.YYYY |
| D | Test Methodology | Text (wrap) | 40 | What you did |
| E | Expected Result | Dropdown | 20 | Should Block/Should Monitor |
| F | Actual Result | Dropdown | 20 | Blocked/Allowed/Alert Only |
| G | Bypass Successful | Dropdown | 18 | Yes (Failed)/No (Passed) |
| H | DLP Alert Generated | Dropdown | 18 | Yes/No |
| I | Severity | Dropdown | 15 | Critical/High/Medium/Low |
| J | Remediation Status | Dropdown | 18 | Fixed/In Progress/Open |
| K | Evidence ID | Text | 15 | A812-3-BYP-001 |

**Test ID Auto-Generation:**
```python
="TEST-"&TEXT(ROW()-5,"000")
```

**Data Rows:** 35 (all blank, populated during testing)

**Data Validation:**

```python
# Column B: Channel Tested
validation_channel = {
    'type': 'list',
    'formula1': '"Email,Web,Endpoint USB,Endpoint Clipboard,Endpoint Print,Network FTP,Cloud Storage,Mobile,API,Other"',
    'allow_blank': False
}

# Column E: Expected Result
validation_expected = {
    'type': 'list',
    'formula1': '"Should Block,Should Monitor,Should Encrypt,Should Alert"',
    'allow_blank': False
}

# Column F: Actual Result
validation_actual = {
    'type': 'list',
    'formula1': '"Blocked (Pass),Allowed (Fail),Alert Only (Partial),Encrypted (Pass),Not Tested"',
    'allow_blank': False
}

# Column G: Bypass Successful
validation_bypass = {
    'type': 'list',
    'formula1': '"Yes (Fail - DLP Bypassed),No (Pass - DLP Worked)"',
    'allow_blank': False
}

# Column H: DLP Alert
validation_alert = {
    'type': 'list',
    'formula1': '"Yes,No,Unknown"',
    'allow_blank': False
}

# Column I: Severity
validation_severity = {
    'type': 'list',
    'formula1': '"Critical,High,Medium,Low"',
    'allow_blank': False
}

# Column J: Status
validation_status = {
    'type': 'list',
    'formula1': '"Fixed (Retested Pass),In Progress,Open,Risk Accepted"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column G (Bypass Successful):
  - "No (Pass - DLP Worked)" = Green
  - "Yes (Fail - DLP Bypassed)" = Red
- Column J (Remediation Status):
  - "Fixed (Retested Pass)" = Green
  - "In Progress" = Yellow
  - "Open" = Red

---

## Sheet: Gap_Analysis

**Purpose:** Document coverage gaps and remediation plans

*(Same structure as IMP-A.8.12.1 and A.8.12.2)*

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Gap ID | Text | 12 | Auto: GAP-001 |
| B | Channel | Dropdown | 20 | Which channel |
| C | Gap Description | Text (wrap) | 40 | What's missing |
| D | Current State | Text (wrap) | 25 | Now |
| E | Required State | Text (wrap) | 25 | Target |
| F | Risk Level | Dropdown | 15 | Critical/High/Medium/Low |
| G | Regulatory Impact | Text | 25 | Which regulations |
| H | Remediation Action | Text (wrap) | 35 | What to do |
| I | Owner | Text | 20 | Who |
| J | Target Date | Date | 15 | When |
| K | Status | Dropdown | 15 | Open/In Progress/Resolved |
| L | Evidence ID | Text | 15 | A812-3-GAP-001 |

**Data Rows:** 45 total

---

## Sheet: Evidence_Register

*(Same structure as previous IMP documents)*

**Data Rows:** 110 total (1 example + 109 blank)

---

## Sheet: Summary_Dashboard

**Purpose:** Executive summary with channel coverage heatmap

**Layout:**

**Rows 1-5:** Header

**Rows 7-20: Key Metrics**

| Metric | Formula | Target |
|--------|---------|--------|
| Overall Channel Coverage % | Weighted average across 7 channels | ≥90% |
| Channels Fully Covered | COUNT of ✅ Compliant channels | 7/7 |
| Channels with Gaps | COUNT of ⚠️ Partial or ❌ Non-Compliant | 0 |
| Critical Gaps | COUNT of Critical risk gaps | 0 |
| Bypass Tests Passed | Tests where DLP blocked / Total tests × 100 | 100% |
| Shadow IT Channels Identified | COUNT of unsanctioned channels | Document all |
| Unprotected Restricted Data Channels | Critical risk | 0 |

**Rows 22-32: Channel Coverage Heatmap**

| Channel | Coverage Status | Enforcement Mode | Bypass Test | Overall Status |
|---------|----------------|------------------|-------------|----------------|
| Email | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Web | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Endpoint | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Network | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Cloud | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Mobile | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Application | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |

**Rows 34-42: Top 5 Critical Bypass Paths** (if any)

- Dynamically pulled from Gap_Analysis (filtered by "Critical")

**Key Formulas:**

```python
# Overall Channel Coverage %
=ROUND(
  (COUNTIF(Email_Channel!L:L,"✅ Compliant") / COUNTA(Email_Channel!L6:L20) * 14) +
  (COUNTIF(Web_Channel!K:K,"✅ Compliant") / COUNTA(Web_Channel!K6:K25) * 14) +
  (COUNTIF(Endpoint_Channel!J:J,"✅ Compliant") / COUNTA(Endpoint_Channel!J6:J30) * 15) +
  (COUNTIF(Network_Channel!H:H,"✅ Compliant") / COUNTA(Network_Channel!H6:H20) * 14) +
  (COUNTIF(Cloud_Channel!K:K,"✅ Compliant") / COUNTA(Cloud_Channel!K6:K25) * 14) +
  (COUNTIF(Mobile_Channel!L:L,"✅ Compliant") / COUNTA(Mobile_Channel!L6:L25) * 14) +
  (COUNTIF(Application_Channel!K:K,"✅ Compliant") / COUNTA(Application_Channel!K6:K20) * 15),
  0
)

# Bypass Tests Passed %
=IFERROR(
  ROUND(
    COUNTIF(Bypass_Testing!G6:G40,'No (Pass - DLP Worked)') /
    COUNTA(Bypass_Testing!G6:G40) * 100,
    0
  ),
  0
)

# Shadow IT Channels
=COUNTIF(Channel_Inventory!H6:H30,"Shadow IT") +
 COUNTIF(Channel_Inventory!H6:H30,"Unsanctioned")

# Unprotected Restricted Data Channels (CRITICAL)
=SUMPRODUCT(
  (Channel_Inventory!G6:G30="Restricted") *
  (Channel_Inventory!I6:I30="No") *
  1
)
```

**Conditional Formatting:**

- Overall Coverage %:
  - ≥90% = Dark green
  - 80-89% = Light green
  - 70-79% = Yellow
  - <70% = Red
- Unprotected Restricted Data Channels:
  - 0 = Green ("✅ No Critical Gaps")
  - ≥1 = Red ("❌ CRITICAL: [count] Unprotected Restricted Data Channels")

---

# 3-7. [Same as IMP-A.8.12.1 & A.8.12.2]

*Data Validation Rules, Conditional Formatting, Cell Protection, Summary Formulas, Evidence Auto-Numbering sections follow same patterns as previous IMP documents.*

---

# APPENDIX: Technical Notes

## A.1 Python Script Integration

**Script:** `generate_a812_3_channel_coverage_assessment.py`

**Key Customization Points:**

- 7 channel sheets (unique structures per channel)
- Bypass testing results tracking
- Channel coverage heatmap in dashboard
- Weighted compliance calculation (different weights per channel)

## A.2 Quality Assurance

**Validation Script:** `excel_sanity_check_a812_3.py`

**Critical Checks:**

- All 7 channel categories present
- Bypass testing sheet populated (at least 1 test per channel)
- Coverage heatmap calculates correctly
- No channels with Restricted data showing "No" DLP coverage

## A.3 Deployment

```bash
python3 generate_a812_3_channel_coverage_assessment.py
# Output: ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx

python3 excel_sanity_check_a812_3.py ISMS-IMP-A.8.12.3_Channel_Coverage_20260121.xlsx
```

---

**END OF PART II: TECHNICAL SPECIFICATION**

**Status:** Complete  
**Next Action:** Implement Python generator per specification

---

**END OF SPECIFICATION**

---

*"Life is like riding a bicycle. To keep your balance, you must keep moving."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->

# ISMS-IMP-A.8.12.3 - Channel Coverage Assessment

## DOC CONTROL

| **Attribute**           | **Details**                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Document ID**         | ISMS-IMP-A.8.12.3                                                          |
| **Document Title**      | Channel Coverage Assessment Workbook Specification                          |
| **Control Reference**   | ISO/IEC 27001:2022 - Control A.8.12 (Data Leakage Prevention)             |
| **Related Policy**      | ISMS-POL-A.8.12-S2.2 (Channel Protection Requirements)                     |
| **Document Type**       | Implementation Assessment Specification                                     |
| **Version**             | 1.0                                                                        |
| **Status**              | Draft                                                                      |
| **Effective Date**      | Approval Date                                                                 |
| **Review Cycle**        | Quarterly                                                                  |
| **Document Owner**      | Chief Information Security Officer (CISO)                                  |
| **Approved By**         | CISO, CIO, DPO                                                             |
| **Classification**      | Internal Use                                                               |

### Revision History

| **Version** | **Date**   | **Author**        | **Changes**                          |
|-------------|------------|-------------------|--------------------------------------|
| 1.0         | Approval Date | ISMS Project Team | Initial specification for Domain 3   |

### Related Documents

| **Document ID**              | **Title**                                      | **Relationship**        |
|------------------------------|------------------------------------------------|-------------------------|
| ISMS-POL-A.8.12              | Data Leakage Prevention Policy (Master)        | Parent Policy           |
| ISMS-POL-A.8.12-S2.2         | Channel Protection Requirements                | Direct Mapping          |
| ISMS-IMP-A.8.12.1            | DLP Infrastructure Assessment                  | Related Assessment      |
| ISMS-IMP-A.8.12.2            | Data Classification Assessment                 | Related Assessment      |
| ISMS-IMP-A.8.12.5            | Compliance Dashboard                           | Consolidation Target    |

---

## 1. PURPOSE & SCOPE

### 1.1 Purpose

This document specifies the structure and requirements for the **Channel Coverage Assessment Workbook**, which evaluates DLP protection across all data egress channels (email, web, endpoint, network, application, mobile).

**Assessment Focus:**
- DLP deployment status per channel (Yes/No/Partial/Planned)
- Detection capabilities (pattern matching, fingerprinting, ML/AI)
- Policy enforcement actions (Allow/Alert/Block/Quarantine/Encrypt)
- Coverage percentage (% of traffic/users/devices protected)
- Gap identification (unprotected channels, encryption blind spots)

### 1.2 Scope

**In Scope:**
- **Email Channel** - SMTP, M365, Gmail, webmail, encrypted email
- **Web/Cloud Channel** - HTTP/HTTPS, cloud storage, SaaS, code repositories
- **Endpoint Channel** - USB, print, clipboard, screen capture, Bluetooth
- **Network Channel** - SMB, FTP, NFS, SCP, WebDAV
- **Application Channel** - Database exports, API calls, reporting tools
- **Mobile Channel** - MDM/MAM, BYOD, camera, AirDrop, messaging apps

**Out of Scope:**
- DLP technology inventory (covered in ISMS-IMP-A.8.12.1)
- Data classification schema (covered in ISMS-IMP-A.8.12.2)
- Alert monitoring and incident response (covered in ISMS-IMP-A.8.12.4)

### 1.3 Target Audience

- **Primary:** DLP Administrators, IT Security Team, SOC Analysts
- **Secondary:** CISO, CIO, Network Operations
- **Reviewers:** Internal Audit, External Auditors, DPO

---

## 2. ASSESSMENT METHODOLOGY

### 2.1 Assessment Approach

**Channel-Centric Methodology:**
1. **Channel Inventory** - Identify all data egress channels in use
2. **Protection Assessment** - Evaluate DLP deployment per channel
3. **Capability Analysis** - Assess detection methods and policy actions
4. **Coverage Calculation** - Measure % of traffic/users/devices protected
5. **Gap Identification** - Identify unprotected channels and blind spots
6. **Risk Prioritization** - Rank gaps by exfiltration risk
7. **Remediation Planning** - Create channel protection roadmap

### 2.2 Assessment Frequency

- **Initial Assessment:** Complete baseline within 30 days of policy approval
- **Quarterly Review:** Update channel inventory, reassess coverage, track remediation
- **Ad-Hoc Assessment:** Upon new channel deployment (new SaaS app, BYOD program)

### 2.3 Response Values (Standard)

| **Value**   | **Meaning**                                          | **Visual**  |
|-------------|------------------------------------------------------|-------------|
| **Yes**     | Fully implemented, documented, evidence available    | ✅ Green    |
| **No**      | Not implemented, significant gap exists              | ❌ Red      |
| **Partial** | Partially implemented, some gaps remain              | ⚠️ Yellow   |
| **Planned** | Not yet implemented, scheduled with target date      | 📋 Blue     |
| **N/A**     | Not applicable to this organization (justification required) | ⚪ Gray |

**CRITICAL:** "Maybe" is **NOT** a valid response value.

---

## 3. WORKBOOK STRUCTURE

### 3.1 Sheet Overview

| **#** | **Sheet Name**              | **Purpose**                                    | **Rows** |
|-------|-----------------------------|------------------------------------------------|----------|
| 1     | Instructions_Legend         | How to use workbook, legend, metadata         | 50       |
| 2     | Channel_Overview            | Summary of all 6 channels                     | 15       |
| 3     | Email_Channel               | Email DLP deployment and coverage             | 30       |
| 4     | Web_Cloud_Channel           | Web/cloud DLP deployment and coverage         | 30       |
| 5     | Endpoint_Channel            | Endpoint DLP deployment and coverage          | 35       |
| 6     | Network_Channel             | Network DLP deployment and coverage           | 25       |
| 7     | Application_Channel         | Application-level DLP controls                | 25       |
| 8     | Mobile_Channel              | Mobile DLP (MDM/MAM) deployment               | 25       |
| 9     | Coverage_Metrics            | Channel coverage % calculations               | 20       |
| 10    | Gap_Analysis                | Identified deficiencies and remediation plans | 40       |
| 11    | Evidence_Register           | Audit trail and evidence tracking             | 100      |
| 12    | Summary_Dashboard           | KPIs, compliance score, executive summary     | 25       |

**Total Assessment Items:** ~90 channel protection checkpoints

---

## 4. SHEET SPECIFICATIONS

### 4.1 Sheet: Instructions_Legend

**Purpose:** Provide user guidance and assessment metadata.

**Content Sections:**
1. **Document Header**
   - Workbook ID: ISMS-IMP-A.8.12.3
   - Assessment Area: Channel Coverage
   - Related Policy: ISMS-POL-A.8.12-S2.2
   - Version: 1.0

2. **Organization Metadata** (Yellow input fields)
   - Assessment Date
   - Completed By
   - Organization Name
   - Review Cycle: Quarterly

3. **How to Use This Workbook**
   - Complete Channel_Overview first (high-level assessment)
   - Then complete each channel-specific sheet
   - Document all DLP policies and actions per channel
   - Calculate coverage metrics
   - Identify gaps and create remediation plans
   - Evidence ID format: A812-3-[CHANNEL]-[###] (e.g., A812-3-EMAIL-001)

4. **Legend - Response Values**
   - Standard Yes/No/Partial/Planned/N/A legend

5. **Channel Protection Tiers** (from ISMS-POL-A.8.12-S2.2)
   - Tier 1 (Critical): Email, Web, USB - Months 1-3
   - Tier 2 (High): Cloud, Mobile - Months 4-6
   - Tier 3 (Medium): Network shares, Print - Months 7-9
   - Tier 4 (Low): Bluetooth, Optical drives - Months 10-12

**Layout:** Informational only, no data entry rows.

---

### 4.2 Sheet: Channel_Overview

**Purpose:** High-level summary of DLP protection across all 6 channels.

**Header Section:**
- Row 1: "CHANNEL COVERAGE OVERVIEW"
- Row 2: "Summary of DLP protection across all data egress channels"
- Row 3: Assessment Date, Completed By (yellow input cells)

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Channel Name              | Text         | Pre-populated                      | 25        |
| B       | Priority Tier             | Text         | Pre-populated (Tier 1-4)           | 15        |
| C       | DLP Deployed?             | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| D       | Coverage %                | Number       | Formula (from channel sheets)      | 15        |
| E       | Users Protected           | Number       | User input                         | 15        |
| F       | Total Users               | Number       | User input                         | 15        |
| G       | Policy Action             | Dropdown     | Allow/Alert/Block/Quarantine/Encrypt| 18       |
| H       | Gap Status                | Formula      | Auto (based on coverage %)         | 18        |
| I       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Channels:**

| **Channel**   | **Tier** | **DLP?** | **Coverage** | **Users** | **Total** | **Action** | **Gap** |
|---------------|----------|----------|--------------|-----------|-----------|------------|---------|
| Email         | Tier 1   | [Input]  | [Formula]    | [Input]   | [Input]   | [Input]    | [Auto]  |
| Web/Cloud     | Tier 1   | [Input]  | [Formula]    | [Input]   | [Input]   | [Input]    | [Auto]  |
| Endpoint      | Tier 1   | [Input]  | [Formula]    | [Input]   | [Input]   | [Input]    | [Auto]  |
| Network       | Tier 3   | [Input]  | [Formula]    | [Input]   | [Input]   | [Input]    | [Auto]  |
| Application   | Tier 2   | [Input]  | [Formula]    | [Input]   | [Input]   | [Input]    | [Auto]  |
| Mobile        | Tier 2   | [Input]  | [Formula]    | [Input]   | [Input]   | [Input]    | [Auto]  |

**Formulas:**
- Coverage % (Col D): `=Email_Channel!B25` (pulls from each channel sheet's calculated coverage)
- Gap Status (Col H): `=IF(D6>=90,"✅ Compliant",IF(D6>=70,"⚠️ Partial","❌ Gap"))`

**Data Rows:** 6 (one per channel)

---

### 4.3 Sheet: Email_Channel

**Purpose:** Assess email DLP deployment across all email systems.

**Header Section:**
- Row 1: "EMAIL CHANNEL PROTECTION ASSESSMENT"
- Row 2: "Evaluate DLP coverage for SMTP, M365, Gmail, Webmail"

**Assessment Question (Row 3):**
"Does your organization have DLP protection for all email systems?"

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Email System              | Text         | User input                         | 25        |
| B       | System Type               | Dropdown     | SMTP/M365/Gmail/Webmail/Other      | 20        |
| C       | DLP Solution              | Text         | User input (vendor-agnostic)       | 25        |
| D       | Deployment Mode           | Dropdown     | Inline/Monitor/Cloud-Native/CASB   | 20        |
| E       | Content Inspection        | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| F       | Attachment Scanning       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| G       | Encrypted Email Handling  | Dropdown     | Decrypt/Quarantine/Allow/Block     | 18        |
| H       | Policy Action             | Dropdown     | Allow/Alert/Block/Quarantine/Encrypt| 18       |
| I       | External Email Protected  | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| J       | Users Covered             | Number       | User input                         | 15        |
| K       | SIEM Integration          | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| L       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Examples:**

| **System**      | **Type** | **Solution**        | **Mode**       | **Inspect** | **Attach** | **Encrypt** | **Action** |
|-----------------|----------|---------------------|----------------|-------------|------------|-------------|------------|
| Exchange Online | M365     | Microsoft Purview   | Cloud-Native   | Yes         | Yes        | Decrypt     | Block      |
| Gmail           | Gmail    | Google Workspace DLP| Cloud-Native   | Yes         | Yes        | Quarantine  | Alert      |
| SMTP Gateway    | SMTP     | Forcepoint DLP      | Inline         | Yes         | Yes        | Decrypt     | Block      |

**Summary Row (Row 25):**
- Col A: "Email Channel Coverage %"
- Col B: `=(COUNTIF(D6:D24,"Yes")/COUNTA(A6:A24))*100` (coverage calculation)

**Data Rows:** 20 (3 examples + 17 blank)

---

### 4.4 Sheet: Web_Cloud_Channel

**Purpose:** Assess web/cloud DLP deployment for HTTP/HTTPS and cloud services.

**Header Section:**
- Row 1: "WEB/CLOUD CHANNEL PROTECTION ASSESSMENT"
- Row 2: "Evaluate DLP coverage for web uploads, cloud storage, SaaS applications"

**Assessment Question (Row 3):**
"Does your organization protect against data exfiltration via web and cloud services?"

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Service/Application       | Text         | User input                         | 30        |
| B       | Service Type              | Dropdown     | Cloud Storage/SaaS/Web Upload/Code Repo/Social Media | 25 |
| C       | DLP Solution              | Text         | User input                         | 25        |
| D       | Protection Method         | Dropdown     | Proxy/CASB/Cloud-Native/Endpoint   | 20        |
| E       | SSL/TLS Inspection        | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| F       | Upload Blocking           | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| G       | Download Monitoring       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| H       | Policy Action             | Dropdown     | Allow/Alert/Block/Quarantine/Coach | 18        |
| I       | Users Covered             | Number       | User input                         | 15        |
| J       | SIEM Integration          | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| K       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Examples:**

| **Service**       | **Type**       | **Solution**          | **Method** | **SSL** | **Upload** | **Action** |
|-------------------|----------------|-----------------------|------------|---------|------------|------------|
| OneDrive          | Cloud Storage  | Microsoft Purview     | Cloud      | Yes     | Yes        | Block      |
| Dropbox           | Cloud Storage  | Netskope CASB         | CASB       | Yes     | Yes        | Alert      |
| GitHub            | Code Repo      | Forcepoint Web DLP    | Proxy      | Yes     | Yes        | Block      |
| Personal Webmail  | Web Upload     | Zscaler DLP           | Proxy      | Yes     | Yes        | Block      |

**Summary Row (Row 25):**
- Col A: "Web/Cloud Channel Coverage %"
- Col B: `=(COUNTIF(E6:E24,"Yes")/COUNTA(A6:A24))*100`

**Data Rows:** 20 (4 examples + 16 blank)

---

### 4.5 Sheet: Endpoint_Channel

**Purpose:** Assess endpoint DLP deployment for USB, print, clipboard, screen capture.

**Header Section:**
- Row 1: "ENDPOINT CHANNEL PROTECTION ASSESSMENT"
- Row 2: "Evaluate endpoint DLP agent coverage and controls"

**Assessment Question (Row 3):**
"Does your organization have endpoint DLP agents protecting USB, print, and other local channels?"

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Endpoint Type             | Dropdown     | Windows Desktop/macOS/Linux/VDI/Thin Client | 25 |
| B       | OS Version                | Text         | User input                         | 20        |
| C       | DLP Agent Installed       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| D       | USB Control               | Dropdown     | Block All/Allow Approved/Monitor/None | 18     |
| E       | Print Control             | Dropdown     | Block/Watermark/Monitor/None       | 18        |
| F       | Clipboard Control         | Dropdown     | Block/Monitor/None                 | 18        |
| G       | Screen Capture Control    | Dropdown     | Block/Watermark/Monitor/None       | 18        |
| H       | Bluetooth Control         | Dropdown     | Block/Monitor/None                 | 18        |
| I       | Application Control       | Dropdown     | Whitelist/Blacklist/Monitor/None   | 18        |
| J       | Devices Covered           | Number       | User input                         | 15        |
| K       | Total Devices             | Number       | User input                         | 15        |
| L       | Coverage %                | Formula      | `=(J/K)*100`                       | 15        |
| M       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Examples:**

| **Type**         | **OS**       | **Agent** | **USB**        | **Print**   | **Clipboard** | **Screen** | **Devices** | **Total** | **%** |
|------------------|--------------|-----------|----------------|-------------|---------------|------------|-------------|-----------|-------|
| Windows Desktop  | Win 11       | Yes       | Allow Approved | Watermark   | Block         | Block      | 850         | 900       | 94%   |
| macOS            | Sonoma 14    | Yes       | Block All      | Watermark   | Monitor       | Monitor    | 120         | 150       | 80%   |
| Linux            | Ubuntu 22.04 | No        | None           | None        | None          | None       | 0           | 50        | 0%    |
| VDI              | Win 11       | Yes       | Block All      | Block       | Block         | Block      | 200         | 200       | 100%  |

**Summary Row (Row 30):**
- Col A: "Endpoint Channel Coverage %"
- Col L: `=AVERAGE(L6:L29)` (average endpoint coverage)

**Data Rows:** 25 (4 examples + 21 blank)

---

### 4.6 Sheet: Network_Channel

**Purpose:** Assess network-based DLP for file transfer protocols.

**Header Section:**
- Row 1: "NETWORK CHANNEL PROTECTION ASSESSMENT"
- Row 2: "Evaluate network DLP coverage for SMB, FTP, NFS, SCP"

**Assessment Question (Row 3):**
"Does your organization monitor/block file transfers via network protocols?"

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Protocol                  | Dropdown     | SMB/CIFS/FTP/SFTP/NFS/SCP/WebDAV/Rsync | 20    |
| B       | Business Use Case         | Text         | User input                         | 30        |
| C       | DLP Solution              | Text         | User input                         | 25        |
| D       | Detection Method          | Dropdown     | Inline/TAP/SPAN/Endpoint/None      | 20        |
| E       | Content Inspection        | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| F       | Policy Action             | Dropdown     | Allow/Alert/Block/None             | 18        |
| G       | Encryption Handling       | Dropdown     | Decrypt/Allow/Block                | 18        |
| H       | SIEM Integration          | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| I       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Examples:**

| **Protocol** | **Use Case**           | **Solution**     | **Method** | **Inspect** | **Action** | **Encrypt** |
|--------------|------------------------|------------------|------------|-------------|------------|-------------|
| SMB/CIFS     | Internal file shares   | Forcepoint DLP   | Inline     | Yes         | Alert      | Allow       |
| FTP          | External file transfer | Network DLP      | TAP        | Yes         | Block      | Decrypt     |
| SFTP         | Secure file transfer   | Endpoint DLP     | Endpoint   | Partial     | Alert      | Allow       |

**Summary Row (Row 20):**
- Col A: "Network Channel Coverage %"
- Col E: `=(COUNTIF(E6:E19,"Yes")/COUNTA(A6:A19))*100`

**Data Rows:** 15 (3 examples + 12 blank)

---

### 4.7 Sheet: Application_Channel

**Purpose:** Assess application-level DLP controls.

**Header Section:**
- Row 1: "APPLICATION CHANNEL PROTECTION ASSESSMENT"
- Row 2: "Evaluate DLP controls in databases, APIs, reporting tools, CRM, ERP"

**Assessment Question (Row 3):**
"Does your organization have DLP controls for application-level data exports?"

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Application Name          | Text         | User input                         | 30        |
| B       | Application Type          | Dropdown     | Database/API/Reporting/CRM/ERP/BI/Other | 20   |
| C       | Data Export Capability    | Dropdown     | Yes/No/Limited                     | 18        |
| D       | DLP Control Method        | Dropdown     | DAM/API Gateway/App Control/Endpoint/None | 25 |
| E       | Bulk Export Detection     | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| F       | Export Policy Action      | Dropdown     | Allow/Alert/Block/Approval Required| 18        |
| G       | Audit Logging             | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| H       | SIEM Integration          | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| I       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Examples:**

| **Application** | **Type**   | **Export** | **Control**  | **Bulk Detect** | **Action**  | **Audit** |
|-----------------|------------|------------|--------------|-----------------|-------------|-----------|
| Oracle DB       | Database   | Yes        | DAM (Imperva)| Yes             | Alert       | Yes       |
| Salesforce      | CRM        | Yes        | CASB         | Yes             | Block       | Yes       |
| Power BI        | BI         | Yes        | App Control  | Partial         | Approval    | Partial   |

**Summary Row (Row 20):**
- Col A: "Application Channel Coverage %"
- Col E: `=(COUNTIF(E6:E19,"Yes")/COUNTA(A6:A19))*100`

**Data Rows:** 15 (3 examples + 12 blank)

---

### 4.8 Sheet: Mobile_Channel

**Purpose:** Assess mobile DLP (MDM/MAM) deployment.

**Header Section:**
- Row 1: "MOBILE CHANNEL PROTECTION ASSESSMENT"
- Row 2: "Evaluate MDM/MAM DLP controls for corporate and BYOD devices"

**Assessment Question (Row 3):**
"Does your organization have DLP controls for mobile devices with corporate data access?"

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Device Ownership          | Dropdown     | Corporate/BYOD                     | 18        |
| B       | Mobile Platform           | Dropdown     | iOS/Android/Windows Mobile         | 18        |
| C       | MDM/MAM Solution          | Text         | User input                         | 25        |
| D       | Work Profile Enabled      | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| E       | Copy-Paste Control        | Dropdown     | Block/Monitor/None                 | 18        |
| F       | Screenshot Control        | Dropdown     | Block/Watermark/Monitor/None       | 18        |
| G       | Camera Access Control     | Dropdown     | Block/Monitor/None                 | 18        |
| H       | Personal Cloud Block      | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| I       | AirDrop/NFC Control       | Dropdown     | Block/Monitor/None                 | 18        |
| J       | Devices Enrolled          | Number       | User input                         | 15        |
| K       | Total Mobile Devices      | Number       | User input                         | 15        |
| L       | Coverage %                | Formula      | `=(J/K)*100`                       | 15        |
| M       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Examples:**

| **Ownership** | **Platform** | **MDM**           | **Profile** | **Copy-Paste** | **Screenshot** | **Camera** | **Enrolled** | **Total** | **%** |
|---------------|--------------|-------------------|-------------|----------------|----------------|------------|--------------|-----------|-------|
| Corporate     | iOS          | Microsoft Intune  | Yes         | Block          | Block          | Block      | 200          | 200       | 100%  |
| BYOD          | Android      | Workspace ONE     | Yes         | Block          | Monitor        | Monitor    | 150          | 300       | 50%   |
| Corporate     | iOS          | Jamf Pro          | Yes         | Block          | Watermark      | Block      | 50           | 50        | 100%  |

**Summary Row (Row 20):**
- Col A: "Mobile Channel Coverage %"
- Col L: `=AVERAGE(L6:L19)` (average mobile coverage)

**Data Rows:** 15 (3 examples + 12 blank)

---

### 4.9 Sheet: Coverage_Metrics

**Purpose:** Calculate and visualize channel coverage percentages.

**Header Section:**
- Row 1: "CHANNEL COVERAGE METRICS"
- Row 2: "Weighted coverage analysis across all channels"

**Sections:**

#### Section 1: Channel Coverage Summary

| **Channel**   | **Target %** | **Actual %** (Formula) | **Gap** (Formula) | **Status** (Formula) |
|---------------|--------------|------------------------|-------------------|----------------------|
| Email         | 95%          | =Email_Channel!B25     | =B6-C6            | =IF(C6>=B6,"✅","❌") |
| Web/Cloud     | 90%          | =Web_Cloud_Channel!B25 | =B7-C7            | =IF(C7>=B7,"✅","❌") |
| Endpoint      | 95%          | =Endpoint_Channel!L30  | =B8-C8            | =IF(C8>=B8,"✅","❌") |
| Network       | 75%          | =Network_Channel!E20   | =B9-C9            | =IF(C9>=B9,"✅","❌") |
| Application   | 80%          | =Application_Channel!E20| =B10-C10         | =IF(C10>=B10,"✅","❌")|
| Mobile        | 90%          | =Mobile_Channel!L20    | =B11-C11          | =IF(C11>=B11,"✅","❌")|

#### Section 2: Weighted Average Coverage

| **Metric**                        | **Formula**                                          | **Target** |
|-----------------------------------|------------------------------------------------------|------------|
| Overall Channel Coverage %        | =AVERAGE(C6:C11)                                     | ≥85%       |
| Tier 1 Channels Avg (Critical)    | =AVERAGE(C6:C8)                                      | ≥90%       |
| Tier 2 Channels Avg (High)        | =AVERAGE(C10:C11)                                    | ≥80%       |
| Tier 3-4 Channels Avg (Med-Low)   | =C9                                                  | ≥70%       |

**Data Rows:** 20 total

---

### 4.10 Sheet: Gap_Analysis

**Purpose:** Identify channel protection gaps and remediation plans.

**Header Section:**
- Row 1: "CHANNEL PROTECTION GAP ANALYSIS"
- Row 2: "Document all unprotected channels and remediation plans"

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Gap ID                    | Text         | Auto-generated (GAP-A812-3-###)    | 20        |
| B       | Channel                   | Dropdown     | Email/Web/Endpoint/Network/App/Mobile | 18     |
| C       | Gap Description           | Text         | User input                         | 40        |
| D       | Risk Level                | Dropdown     | Critical/High/Medium/Low           | 15        |
| E       | Exfiltration Risk         | Dropdown     | Very High/High/Medium/Low          | 15        |
| F       | Current Coverage %        | Number       | User input                         | 15        |
| G       | Target Coverage %         | Number       | User input                         | 15        |
| H       | Remediation Plan          | Text         | User input                         | 40        |
| I       | Owner                     | Text         | User input                         | 25        |
| J       | Target Date               | Date         | User input                         | 15        |
| K       | Status                    | Dropdown     | Not Started/In Progress/Complete/Blocked | 18  |
| L       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Example Gaps:**

| **ID**        | **Channel** | **Description**                    | **Risk** | **Exfil** | **Current** | **Target** |
|---------------|-------------|------------------------------------|----------|-----------|-------------|------------|
| GAP-A812-3-001| Endpoint    | Linux endpoints not protected      | High     | High      | 0%          | 80%        |
| GAP-A812-3-002| Mobile      | BYOD enrollment <50%               | Medium   | Medium    | 50%         | 90%        |
| GAP-A812-3-003| Web         | Personal webmail not blocked       | Critical | Very High | 0%          | 100%       |

**Data Rows:** 40 (3 examples + 37 blank)

---

### 4.11 Sheet: Evidence_Register

**Purpose:** Track all evidence collected for channel protection assessment.

**Standard Evidence Register Format** (same as Domains 1 and 2):

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Evidence ID               | Text         | User input (A812-3-XXX-###)        | 20        |
| B       | Evidence Type             | Dropdown     | Config/Screenshot/Log/Report/Policy/Other | 20 |
| C       | Channel                   | Dropdown     | Email/Web/Endpoint/Network/App/Mobile | 18     |
| D       | Description               | Text         | User input                         | 40        |
| E       | Collection Date           | Date         | User input                         | 15        |
| F       | Collected By              | Text         | User input                         | 25        |
| G       | Storage Location          | Text         | User input (file path/URL)         | 35        |
| H       | Verification Status       | Dropdown     | Verified/Pending/Rejected          | 18        |
| I       | Verified By               | Text         | User input                         | 25        |
| J       | Verification Date         | Date         | User input                         | 15        |
| K       | Notes                     | Text         | User input                         | 40        |

**Data Rows:** 100 (all blank for user input)

---

### 4.12 Sheet: Summary_Dashboard

**Purpose:** Executive summary with KPIs and compliance scoring.

**Header Section:**
- Row 1: "CHANNEL COVERAGE ASSESSMENT - EXECUTIVE SUMMARY"
- Row 2: "ISO/IEC 27001:2022 - Control A.8.12: Data Leakage Prevention"

**Sections:**

#### Section 1: Document Information
- Assessment Date: [Input]
- Completed By: [Input]
- CISO Approval Status: [Dropdown]
- Last Review Date: [Input]

#### Section 2: Key Performance Indicators

| **KPI**                              | **Formula**                                    | **Target** | **Status** |
|--------------------------------------|------------------------------------------------|------------|------------|
| Overall Channel Coverage %           | =Coverage_Metrics!C15                          | ≥85%       | Auto       |
| Tier 1 Channels (Email/Web/Endpoint) | =Coverage_Metrics!C16                          | ≥90%       | Auto       |
| Email Channel Coverage               | =Email_Channel!B25                             | ≥95%       | Auto       |
| Web/Cloud Channel Coverage           | =Web_Cloud_Channel!B25                         | ≥90%       | Auto       |
| Endpoint Channel Coverage            | =Endpoint_Channel!L30                          | ≥95%       | Auto       |
| Network Channel Coverage             | =Network_Channel!E20                           | ≥75%       | Auto       |
| Application Channel Coverage         | =Application_Channel!E20                       | ≥80%       | Auto       |
| Mobile Channel Coverage              | =Mobile_Channel!L20                            | ≥90%       | Auto       |
| Total Gaps Identified                | =COUNTA(Gap_Analysis!A6:A45)-3                 | ≤10        | Auto       |
| Critical/High Gaps                   | =COUNTIFS(Gap_Analysis!D6:D45,"Critical")+COUNTIFS(Gap_Analysis!D6:D45,"High") | 0 | Auto |
| **Domain 3 Compliance Score**        | =B7                                            | **≥85%**   | **Auto**   |

#### Section 3: Gap Summary by Channel

| **Channel**   | **Gaps** (Formula)                                  | **Critical** (Formula)                    |
|---------------|-----------------------------------------------------|-------------------------------------------|
| Email         | =COUNTIF(Gap_Analysis!B6:B45,"Email")               | =COUNTIFS(Gap_Analysis!B6:B45,"Email",Gap_Analysis!D6:D45,"Critical") |
| Web/Cloud     | =COUNTIF(Gap_Analysis!B6:B45,"Web")                 | =COUNTIFS(Gap_Analysis!B6:B45,"Web",Gap_Analysis!D6:D45,"Critical")   |
| Endpoint      | =COUNTIF(Gap_Analysis!B6:B45,"Endpoint")            | =COUNTIFS(Gap_Analysis!B6:B45,"Endpoint",Gap_Analysis!D6:D45,"Critical") |
| Network       | =COUNTIF(Gap_Analysis!B6:B45,"Network")             | =COUNTIFS(Gap_Analysis!B6:B45,"Network",Gap_Analysis!D6:D45,"Critical") |
| Application   | =COUNTIF(Gap_Analysis!B6:B45,"App")                 | =COUNTIFS(Gap_Analysis!B6:B45,"App",Gap_Analysis!D6:D45,"Critical")     |
| Mobile        | =COUNTIF(Gap_Analysis!B6:B45,"Mobile")              | =COUNTIFS(Gap_Analysis!B6:B45,"Mobile",Gap_Analysis!D6:D45,"Critical")  |

#### Section 4: Evidence Completeness

| **Metric**                  | **Formula**                                      |
|-----------------------------|--------------------------------------------------|
| Evidence Items Collected    | =COUNTA(Evidence_Register!A2:A101)               |
| Evidence Items Verified     | =COUNTIF(Evidence_Register!H2:H101,"Verified")   |
| Evidence Completeness %     | =(B25/B24)*100                                   |

#### Section 5: Traffic Light Status

**Overall Status Formula:**
```excel
=IF(B17>=85,"✅ Compliant",IF(B17>=70,"⚠️ Partial","❌ Non-Compliant"))
```

#### Section 6: Approval Sign-Off

| **Approver**       | **Name** | **Signature** | **Date** | **Status**          |
|--------------------|----------|---------------|----------|---------------------|
| DLP Administrator  | [Input]  | [Input]       | [Auto]   | [Dropdown: Approved/Pending] |
| CISO               | [Input]  | [Input]       | [Auto]   | [Dropdown: Approved/Pending] |
| DPO                | [Input]  | [Input]       | [Auto]   | [Dropdown: Approved/Pending] |

---

## 5. ASSESSMENT CRITERIA & SCORING

### 5.1 Compliance Scoring Method

**Domain 3 Compliance Score** is calculated as weighted average:
```
Domain_3_Score = (
    Email_Coverage × 25% +
    Web_Coverage × 20% +
    Endpoint_Coverage × 25% +
    Network_Coverage × 10% +
    Application_Coverage × 10% +
    Mobile_Coverage × 10%
)
```

**Rationale for Weighting:**
- Email/Endpoint: Highest exfiltration risk (25% each)
- Web/Cloud: High risk, growing attack surface (20%)
- Application/Mobile: Medium risk (10% each)
- Network: Lower risk in modern environments (10%)

### 5.2 Maturity Levels

| **Score** | **Level**       | **Description**                                |
|-----------|-----------------|------------------------------------------------|
| 90-100%   | Optimized       | Comprehensive channel coverage, minimal gaps   |
| 80-89%    | Managed         | Strong coverage, some improvements needed      |
| 70-79%    | Defined         | Core channels protected, notable gaps          |
| 60-69%    | Developing      | Partial coverage, major gaps exist             |
| <60%      | Initial/Ad-Hoc  | Insufficient coverage, urgent action required  |

### 5.3 Pass/Fail Criteria

**PASS Criteria:**
- ✅ Overall Domain 3 Score ≥ 85%
- ✅ Zero Critical gaps
- ✅ High gaps ≤ 3
- ✅ Tier 1 channels (Email/Web/Endpoint) ≥ 90% each
- ✅ All channels have some DLP deployment (no channel = 0%)

**FAIL Criteria:**
- ❌ Overall Domain 3 Score < 70%
- ❌ Critical gaps > 0
- ❌ Any Tier 1 channel < 80%
- ❌ More than 2 channels with 0% coverage

---

## 6. COMPLIANCE MAPPING

### 6.1 ISO/IEC 27001:2022 Mapping

| **Control** | **Requirement**                              | **Evidence Location**        |
|-------------|----------------------------------------------|------------------------------|
| A.8.12      | Data leakage prevention (Master)             | All sheets                   |
| A.5.10      | Acceptable use of information                | Endpoint_Channel (USB policy)|
| A.5.14      | Information transfer                         | Channel_Overview             |
| A.8.11      | Data masking (related)                       | Application_Channel          |

### 6.2 Regulatory Mapping

| **Regulation** | **Requirement**                         | **Evidence Location**          |
|----------------|-----------------------------------------|--------------------------------|
| FADP Art. 8    | Data security                           | All channel sheets             |
| FADP Art. 26   | Employee monitoring (works council)     | Endpoint_Channel, Mobile_Channel|
| GDPR Art. 32   | Security of processing                  | Summary_Dashboard              |
| GDPR Art. 5(1)(f) | Integrity and confidentiality        | Coverage_Metrics               |

---

## 7. EVIDENCE REQUIREMENTS

### 7.1 Mandatory Evidence per Channel

**Email Channel:**
- Email gateway DLP policy configurations
- M365/Gmail DLP rule screenshots
- SIEM alert forwarding configs
- Exception approval logs

**Web/Cloud Channel:**
- Web proxy DLP policy configs
- CASB policy screenshots
- SSL inspection certificate configs
- Shadow IT discovery reports

**Endpoint Channel:**
- Endpoint agent deployment reports
- USB device approval lists
- Print job watermarking samples
- Application whitelist/blacklist

**Network Channel:**
- Network DLP appliance configs
- Protocol monitoring logs
- TAP/SPAN port configurations

**Application Channel:**
- DAM policy configurations
- API gateway DLP rules
- Bulk export alert examples

**Mobile Channel:**
- MDM/MAM enrollment reports
- Mobile DLP policy screenshots
- BYOD approval workflows

### 7.2 Evidence Naming Convention
```
A812-3-[CHANNEL]-[###]

Examples:
A812-3-EMAIL-001  (Email DLP config)
A812-3-WEB-001    (Web proxy policy)
A812-3-EPT-001    (Endpoint agent deployment)
A812-3-NET-001    (Network DLP config)
A812-3-APP-001    (DAM configuration)
A812-3-MOB-001    (MDM policy)
```

---

## 8. APPROVAL & SIGN-OFF

### 8.1 Review and Approval Workflow

| **Role**           | **Responsibility**                          | **Timeline**   |
|--------------------|---------------------------------------------|----------------|
| DLP Administrator  | Complete assessment, gather evidence        | Week 1-2       |
| IT Security Lead   | Review technical accuracy                   | Week 3         |
| Network Operations | Validate network channel data               | Week 3         |
| CISO               | Approve gaps, remediation plans             | Week 3         |
| DPO                | Review privacy impact (monitoring)          | Week 3         |
| Internal Audit     | Validate evidence completeness              | Week 4         |

### 8.2 Quarterly Review Process

- Update channel inventory (new SaaS apps, BYOD enrollments)
- Reassess coverage percentages
- Track gap remediation progress
- Update risk ratings based on threat landscape
- Adjust channel priorities if needed

---

**END OF SPECIFICATION: ISMS-IMP-A.8.12.3**

*"The problem with USB ports is they're everywhere, and users know where to find them."*  
— Murphy's Law of Endpoint DLP
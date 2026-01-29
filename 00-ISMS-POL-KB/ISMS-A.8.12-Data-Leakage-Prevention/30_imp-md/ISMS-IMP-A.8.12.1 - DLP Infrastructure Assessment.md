# ISMS-IMP-A.8.12.1 - DLP Infrastructure Assessment

## DOC CONTROL

| **Attribute**           | **Details**                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Document ID**         | ISMS-IMP-A.8.12.1                                                          |
| **Document Title**      | DLP Infrastructure Assessment Workbook Specification                        |
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
| 1.0         | Approval Date | ISMS Project Team | Initial specification for Domain 1   |

### Related Documents

| **Document ID**              | **Title**                                      | **Relationship**        |
|------------------------------|------------------------------------------------|-------------------------|
| ISMS-POL-A.8.12              | Data Leakage Prevention Policy (Master)        | Parent Policy           |
| ISMS-POL-A.8.12-S2.2         | Channel Protection Requirements                | Direct Mapping          |
| ISMS-IMP-A.8.12.2            | Data Classification Assessment                 | Related Assessment      |
| ISMS-IMP-A.8.12.3            | Channel Coverage Assessment                    | Related Assessment      |
| ISMS-IMP-A.8.12.5            | Compliance Dashboard                           | Consolidation Target    |

---

## 1. PURPOSE & SCOPE

### 1.1 Purpose

This document specifies the structure and requirements for the **DLP Infrastructure Assessment Workbook**, which evaluates the technical DLP solutions deployed across the organization's IT infrastructure.

**Assessment Focus:**
- Inventory of all DLP technologies (network, endpoint, cloud, email, web, database)
- Deployment architecture and coverage analysis
- Technical capabilities assessment (content inspection, pattern matching, ML/AI)
- Vendor management (licensing, support, EOL tracking)
- Integration status (SIEM, SOC, IAM, ticketing systems)

### 1.2 Scope

**In Scope:**
- All DLP technologies deployed in production, staging, and test environments
- Network DLP appliances (inline, TAP, span port configurations)
- Endpoint DLP agents (Windows, macOS, Linux, VDI, thin clients)
- Email gateway DLP (on-premise, cloud-based, M365 Purview, Google Workspace)
- Cloud Access Security Brokers (CASB) with DLP capabilities
- Web proxy DLP (forward/reverse proxy, SSL inspection)
- Database Activity Monitoring (DAM) solutions used for DLP
- Integration points with security ecosystem (SIEM, SOC, IAM)

**Out of Scope:**
- Data classification methodology (covered in ISMS-IMP-A.8.12.2)
- Policy configuration details (covered in ISMS-IMP-A.8.12.3)
- Incident response procedures (covered in ISMS-IMP-A.8.12.4)
- User awareness training programs

### 1.3 Target Audience

- **Primary:** IT Security Team, DLP Administrators, SOC Analysts
- **Secondary:** CISO, CIO, IT Infrastructure Teams
- **Reviewers:** Internal Audit, External Auditors, DPO

---

## 2. ASSESSMENT METHODOLOGY

### 2.1 Assessment Approach

**System Engineering Methodology:**
1. **Inventory Collection** - Document all DLP technologies currently deployed
2. **Architecture Review** - Analyze deployment models (inline, monitor, hybrid)
3. **Capability Assessment** - Evaluate technical features and maturity
4. **Gap Identification** - Compare current state vs. policy requirements
5. **Evidence Gathering** - Collect proof of implementation (configs, screenshots, logs)
6. **Compliance Scoring** - Calculate domain compliance percentage
7. **Remediation Planning** - Prioritize gaps for closure

### 2.2 Assessment Frequency

- **Initial Assessment:** Complete baseline within 30 days of policy approval
- **Quarterly Review:** Update inventory, reassess gaps, track remediation progress
- **Ad-Hoc Assessment:** Upon major infrastructure changes (new DLP deployment, vendor change)

### 2.3 Response Values (Standard)

| **Value**   | **Meaning**                                          | **Visual**  |
|-------------|------------------------------------------------------|-------------|
| **Yes**     | Fully implemented, documented, evidence available    | ✅ Green    |
| **No**      | Not implemented, significant gap exists              | ❌ Red      |
| **Partial** | Partially implemented, some gaps remain              | ⚠️ Yellow   |
| **Planned** | Not yet implemented, scheduled with target date      | 📋 Blue     |
| **N/A**     | Not applicable to this organization (justification required) | ⚪ Gray |

**CRITICAL:** "Maybe" is **NOT** a valid response value (Feynman principle: either you know or you don't).

---

## 3. WORKBOOK STRUCTURE

### 3.1 Sheet Overview

| **#** | **Sheet Name**              | **Purpose**                                    | **Rows** |
|-------|-----------------------------|------------------------------------------------|----------|
| 1     | Instructions_Legend         | How to use workbook, legend, metadata         | 50       |
| 2     | DLP_Technology_Inventory    | Complete inventory of all DLP solutions       | 30       |
| 3     | Network_DLP                 | Network-based DLP appliances                  | 20       |
| 4     | Endpoint_DLP                | Endpoint agent deployment                     | 25       |
| 5     | Email_DLP                   | Email gateway DLP solutions                   | 20       |
| 6     | Cloud_CASB_DLP              | Cloud and CASB DLP capabilities               | 20       |
| 7     | Web_DLP                     | Web proxy DLP configurations                  | 20       |
| 8     | Database_DAM                | Database Activity Monitoring for DLP          | 15       |
| 9     | Gap_Analysis                | Identified deficiencies and remediation plans | 40       |
| 10    | Evidence_Register           | Audit trail and evidence tracking             | 100      |
| 11    | Summary_Dashboard           | KPIs, compliance score, executive summary     | 25       |

**Total Assessment Items:** ~80 infrastructure checkpoints

---

## 4. SHEET SPECIFICATIONS

### 4.1 Sheet: Instructions_Legend

**Purpose:** Provide user guidance and assessment metadata.

**Content Sections:**
1. **Document Header**
   - Workbook ID: ISMS-IMP-A.8.12.1
   - Assessment Area: DLP Infrastructure
   - Related Policy: ISMS-POL-A.8.12-S2.2
   - Version: 1.0

2. **Organization Metadata** (Yellow input fields)
   - Assessment Date
   - Completed By
   - Organization Name
   - Review Cycle: Quarterly

3. **How to Use This Workbook**
   - Step-by-step instructions
   - Sheet completion order
   - Dropdown usage guidance
   - Evidence ID formatting (e.g., A812-1-INF-001)

4. **Legend - Response Values**
   - Yes = ✅ Green (Fully implemented)
   - No = ❌ Red (Not implemented)
   - Partial = ⚠️ Yellow (Partially implemented)
   - Planned = 📋 Blue (Scheduled)
   - N/A = ⚪ Gray (Not applicable)

5. **Color Coding Guide**
   - Yellow cells = User input required
   - Gray cells = Informational/examples
   - White cells = Assessment responses

**Layout:** No data entry, informational only.

---

### 4.2 Sheet: DLP_Technology_Inventory

**Purpose:** Complete inventory of all DLP solutions deployed.

**Columns:**

| **Col** | **Header**              | **Type**     | **Validation**                          | **Width** |
|---------|-------------------------|--------------|-----------------------------------------|-----------|
| A       | Technology ID           | Text         | User input (e.g., DLP-001)              | 15        |
| B       | Technology Name         | Text         | User input (e.g., Forcepoint DLP)       | 25        |
| C       | Deployment Type         | Dropdown     | Network/Endpoint/Cloud/Email/Web/Database | 20      |
| D       | Vendor                  | Text         | User input                              | 20        |
| E       | Version                 | Text         | User input                              | 15        |
| F       | Deployment Architecture | Dropdown     | Inline/Monitor/Hybrid/Cloud-based       | 20        |
| G       | Deployment Status       | Dropdown     | Production/Staging/Test/Decommissioned  | 18        |
| H       | License Type            | Dropdown     | Perpetual/Subscription/Open Source      | 18        |
| I       | License Expiry          | Date         | User input                              | 15        |
| J       | Support Contract        | Dropdown     | Active/Expired/N/A                      | 15        |
| K       | EOL Date                | Date         | User input (End of Life)                | 15        |
| L       | Primary Use Case        | Text         | User input (e.g., Email DLP, USB blocking) | 30     |
| M       | Integration Status      | Dropdown     | Integrated/Standalone/Partial           | 18        |
| N       | SIEM Integration        | Dropdown     | Yes/No/Partial/Planned/N/A              | 15        |
| O       | SOC Integration         | Dropdown     | Yes/No/Partial/Planned/N/A              | 15        |
| P       | Evidence ID             | Text         | User input (e.g., A812-1-INF-001)       | 18        |

**Pre-Populated Examples (Gray rows):**

| **ID**  | **Name**              | **Type**  | **Vendor**     | **Use Case**                    |
|---------|-----------------------|-----------|----------------|---------------------------------|
| DLP-001 | Forcepoint DLP        | Network   | Forcepoint     | Network traffic inspection      |
| DLP-002 | Forcepoint Endpoint   | Endpoint  | Forcepoint     | USB, clipboard, print blocking  |
| DLP-003 | Microsoft Purview DLP | Cloud     | Microsoft      | M365 email, OneDrive, Teams     |
| DLP-004 | Symantec DLP          | Email     | Broadcom       | SMTP gateway inspection         |
| DLP-005 | Netskope CASB         | Cloud     | Netskope       | SaaS application DLP            |

**Data Rows:** 30 (5 examples + 25 blank)

**Key Formula (Summary_Dashboard):**
```excel
Total_Technologies = COUNTA(DLP_Technology_Inventory!$B$6:$B$35) - 5  // Exclude example rows
Production_Count = COUNTIF(DLP_Technology_Inventory!$G$6:$G$35,"Production")
Coverage_Score = (Production_Count / Total_Technologies) * 100
```

---

### 4.3 Sheet: Network_DLP

**Purpose:** Assess network-based DLP appliances.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Appliance Name            | Text         | User input                         | 25        |
| B       | Deployment Mode           | Dropdown     | Inline/TAP/SPAN/Cloud Gateway      | 20        |
| C       | Network Segments Covered  | Text         | User input (e.g., DMZ, Internal)   | 25        |
| D       | Protocols Inspected       | Text         | User input (HTTP/HTTPS/SMTP/FTP)   | 25        |
| E       | SSL/TLS Inspection        | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| F       | Throughput Capacity       | Text         | User input (e.g., 10 Gbps)         | 15        |
| G       | Current Utilization %     | Number       | User input (0-100)                 | 15        |
| H       | Content Inspection        | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| I       | Pattern Matching (Regex)  | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| J       | Fingerprinting            | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| K       | Machine Learning/AI       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| L       | Blocking Capability       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| M       | High Availability         | Dropdown     | Yes/No/N/A                         | 15        |
| N       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Checklist Items:**

| **Appliance**           | **Mode**  | **Segments**      | **Protocols**        |
|-------------------------|-----------|-------------------|----------------------|
| Forcepoint DLP Gateway  | Inline    | DMZ, Internal     | HTTP, HTTPS, SMTP    |
| Symantec DLP Network    | TAP       | Internet Gateway  | HTTP, HTTPS, FTP     |
| McAfee DLP Prevent      | Inline    | Branch Offices    | HTTP, HTTPS          |

**Data Rows:** 20 (3 examples + 17 blank)

---

### 4.4 Sheet: Endpoint_DLP

**Purpose:** Assess endpoint DLP agent deployment.

**Columns:**

| **Col** | **Header**                  | **Type**     | **Validation**                     | **Width** |
|---------|-----------------------------|--------------|-------------------------------------|-----------|
| A       | Operating System            | Text         | User input (Windows/macOS/Linux)    | 20        |
| B       | OS Version                  | Text         | User input                          | 20        |
| C       | Agent Name                  | Text         | User input                          | 25        |
| D       | Agent Version               | Text         | User input                          | 15        |
| E       | Deployment Method           | Dropdown     | GPO/SCCM/Jamf/Manual/Cloud MDM      | 20        |
| F       | Total Endpoints             | Number       | User input                          | 15        |
| G       | Agents Deployed             | Number       | User input                          | 15        |
| H       | Deployment Coverage %       | Formula      | =(G/F)*100                          | 15        |
| I       | USB Blocking                | Dropdown     | Yes/No/Partial/Planned/N/A          | 15        |
| J       | Clipboard Monitoring        | Dropdown     | Yes/No/Partial/Planned/N/A          | 15        |
| K       | Print Blocking              | Dropdown     | Yes/No/Partial/Planned/N/A          | 15        |
| L       | Screen Capture Detection    | Dropdown     | Yes/No/Partial/Planned/N/A          | 15        |
| M       | Bluetooth Blocking          | Dropdown     | Yes/No/Partial/Planned/N/A          | 15        |
| N       | Cloud Sync App Monitoring   | Dropdown     | Yes/No/Partial/Planned/N/A          | 15        |
| O       | Evidence ID                 | Text         | User input                          | 18        |

**Pre-Populated Checklist Items:**

| **OS**          | **Version**     | **Agent**           | **Method** | **Total** | **Deployed** |
|-----------------|-----------------|---------------------|------------|-----------|--------------|
| Windows         | 10/11 Enterprise| Forcepoint Endpoint | GPO        | 2000      | 1950         |
| macOS           | 13.x Ventura    | Forcepoint Endpoint | Jamf       | 300       | 280          |
| Linux           | Ubuntu 22.04    | Custom Script       | Ansible    | 50        | 45           |
| VDI (Citrix)    | Windows 10      | Forcepoint Endpoint | Image      | 500       | 500          |

**Data Rows:** 25 (4 examples + 21 blank)

**Key Formula (Coverage %):**
```excel
H6 = (G6/F6)*100  // Deployment Coverage %
```

**Summary Formula (Summary_Dashboard):**
```excel
Overall_Endpoint_Coverage = AVERAGE(Endpoint_DLP!$H$6:$H$30)
```

---

### 4.5 Sheet: Email_DLP

**Purpose:** Assess email gateway DLP solutions.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Email System              | Text         | User input (Exchange/M365/Gmail)   | 25        |
| B       | DLP Solution              | Text         | User input                         | 25        |
| C       | Deployment Type           | Dropdown     | On-Premise/Cloud/Hybrid            | 18        |
| D       | SMTP Gateway Protection   | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| E       | Webmail Protection        | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| F       | Attachment Scanning       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| G       | Encrypted Email Handling  | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| H       | Internal Email Monitoring | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| I       | External Email Monitoring | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| J       | Quarantine Capability     | Dropdown     | Yes/No/Partial/N/A                 | 18        |
| K       | Auto-Encryption           | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| L       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Checklist Items:**

| **System**       | **DLP Solution**      | **Type**    | **SMTP** | **Webmail** | **Attachments** |
|------------------|-----------------------|-------------|----------|-------------|-----------------|
| Microsoft 365    | Microsoft Purview DLP | Cloud       | Yes      | Yes         | Yes             |
| On-Prem Exchange | Symantec Email DLP    | On-Premise  | Yes      | No          | Yes             |
| Gmail Workspace  | Google DLP            | Cloud       | Yes      | Yes         | Yes             |

**Data Rows:** 20 (3 examples + 17 blank)

---

### 4.6 Sheet: Cloud_CASB_DLP

**Purpose:** Assess Cloud Access Security Broker and cloud-native DLP.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Cloud Service             | Text         | User input (Dropbox/Box/OneDrive)  | 25        |
| B       | CASB Solution             | Text         | User input (Netskope/McAfee MVISION)| 25       |
| C       | Integration Type          | Dropdown     | API/Inline/Log Analysis            | 18        |
| D       | Upload Monitoring         | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| E       | Download Monitoring       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| F       | Sharing Controls          | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| G       | Content Inspection        | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| H       | Real-Time Blocking        | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| I       | Shadow IT Discovery       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| J       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Checklist Items:**

| **Service**       | **CASB**          | **Integration** | **Upload** | **Download** | **Sharing** |
|-------------------|-------------------|-----------------|------------|--------------|-------------|
| Microsoft OneDrive| Netskope          | API             | Yes        | Yes          | Yes         |
| Dropbox           | Netskope          | API             | Yes        | Yes          | Yes         |
| Box               | McAfee MVISION    | API             | Yes        | Partial      | Yes         |
| Google Drive      | Native Google DLP | API             | Yes        | Yes          | Yes         |
| GitHub            | Netskope          | API             | Yes        | Yes          | No          |

**Data Rows:** 20 (5 examples + 15 blank)

---

### 4.7 Sheet: Web_DLP

**Purpose:** Assess web proxy DLP configurations.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Proxy Solution            | Text         | User input (Zscaler/BlueCoat)      | 25        |
| B       | Proxy Type                | Dropdown     | Forward/Reverse/Cloud              | 18        |
| C       | SSL Inspection            | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| D       | HTTP/HTTPS Coverage       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| E       | Upload Monitoring         | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| F       | Download Monitoring       | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| G       | Cloud Storage Detection   | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| H       | Webmail Monitoring        | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| I       | URL Filtering Integration | Dropdown     | Yes/No/Partial/N/A                 | 18        |
| J       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Checklist Items:**

| **Proxy**         | **Type**  | **SSL Inspect** | **HTTP/HTTPS** | **Upload** | **Download** |
|-------------------|-----------|-----------------|----------------|------------|--------------|
| Zscaler           | Cloud     | Yes             | Yes            | Yes        | Yes          |
| Forcepoint Web    | Forward   | Yes             | Yes            | Yes        | Partial      |
| Squid Proxy       | Forward   | No              | Partial        | No         | No           |

**Data Rows:** 20 (3 examples + 17 blank)

---

### 4.8 Sheet: Database_DAM

**Purpose:** Assess Database Activity Monitoring for DLP.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Database System           | Text         | User input (Oracle/SQL Server/MySQL)| 25       |
| B       | DAM Solution              | Text         | User input (Imperva/IBM Guardium)  | 25        |
| C       | Monitoring Scope          | Dropdown     | Production/All/None                | 18        |
| D       | SELECT Query Monitoring   | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| E       | Bulk Export Detection     | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| F       | Privileged User Monitoring| Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| G       | DLP Policy Integration    | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| H       | Alert Triggering          | Dropdown     | Yes/No/Partial/Planned/N/A         | 18        |
| I       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Checklist Items:**

| **Database**      | **DAM Solution**  | **Scope**    | **SELECT** | **Bulk Export** | **Privileged** |
|-------------------|-------------------|--------------|------------|-----------------|----------------|
| Oracle 19c        | Imperva DAM       | Production   | Yes        | Yes             | Yes            |
| SQL Server 2019   | IBM Guardium      | Production   | Yes        | Yes             | Yes            |
| MySQL 8.0         | Native Audit Log  | All          | Partial    | No              | Partial        |

**Data Rows:** 15 (3 examples + 12 blank)

---

### 4.9 Sheet: Gap_Analysis

**Purpose:** Identify infrastructure gaps and remediation plans.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Gap ID                    | Text         | Auto (GAP-A812-1-001)              | 18        |
| B       | Gap Description           | Text         | User input                         | 35        |
| C       | Affected Technology       | Text         | User input                         | 25        |
| D       | Risk Level                | Dropdown     | Critical/High/Medium/Low           | 15        |
| E       | Business Impact           | Text         | User input                         | 30        |
| F       | Root Cause                | Text         | User input                         | 30        |
| G       | Remediation Plan          | Text         | User input                         | 35        |
| H       | Owner                     | Text         | User input                         | 20        |
| I       | Target Date               | Date         | User input                         | 15        |
| J       | Status                    | Dropdown     | Open/In Progress/Resolved/Closed   | 15        |
| K       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Example Gaps:**

| **Gap ID**        | **Description**                              | **Risk**  | **Impact**                     |
|-------------------|----------------------------------------------|-----------|--------------------------------|
| GAP-A812-1-001    | Endpoint DLP not deployed to Linux servers   | High      | Unmonitored data exfiltration  |
| GAP-A812-1-002    | No SSL inspection on web proxy               | High      | Encrypted channel bypass       |
| GAP-A812-1-003    | CASB missing for Dropbox                     | Medium    | Shadow IT data leakage         |

**Data Rows:** 40 (3 examples + 37 blank)

**Key Formulas (Summary_Dashboard):**
```excel
Total_Gaps = COUNTA(Gap_Analysis!$A$6:$A$45) - 3  // Exclude examples
Critical_Gaps = COUNTIF(Gap_Analysis!$D$6:$D$45,"Critical")
Open_Gaps = COUNTIF(Gap_Analysis!$J$6:$J$45,"Open")
```

---

### 4.10 Sheet: Evidence_Register

**Purpose:** Track all evidence collected during assessment.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Evidence ID               | Text         | User input (A812-1-INF-001)        | 18        |
| B       | Evidence Type             | Dropdown     | Screenshot/Config/Log/Report/Other | 20        |
| C       | Description               | Text         | User input                         | 35        |
| D       | Location/Link             | Text         | User input (file path/URL)         | 30        |
| E       | Date Collected            | Date         | User input                         | 15        |
| F       | Collected By              | Text         | User input                         | 20        |
| G       | Related Requirement       | Text         | User input (sheet reference)       | 25        |
| H       | Verification Status       | Dropdown     | Verified/Pending/Rejected          | 15        |

**Data Rows:** 100 blank rows for evidence entries

---

### 4.11 Sheet: Summary_Dashboard

**Purpose:** KPIs and compliance scoring for Domain 1.

**Sections:**

#### Section 1: Document Information
- Assessment Date
- Completed By
- CISO Approval Status
- Last Review Date

#### Section 2: Key Performance Indicators

| **KPI**                              | **Formula**                                    | **Target** | **Status** |
|--------------------------------------|------------------------------------------------|------------|------------|
| Total DLP Technologies Deployed      | =COUNTA(DLP_Technology_Inventory!B6:B35)-5     | ≥5         | Auto       |
| Production Technologies              | =COUNTIF(DLP_Technology_Inventory!G6:G35,"Production") | ≥4  | Auto       |
| Network DLP Coverage                 | =COUNTIF(Network_DLP!H6:H25,"Yes")/20*100      | ≥80%       | Auto       |
| Endpoint DLP Coverage %              | =AVERAGE(Endpoint_DLP!H6:H30)                  | ≥95%       | Auto       |
| Email DLP Coverage                   | =COUNTIF(Email_DLP!D6:D25,"Yes")/20*100        | ≥90%       | Auto       |
| Cloud/CASB DLP Coverage              | =COUNTIF(Cloud_CASB_DLP!D6:D25,"Yes")/20*100   | ≥70%       | Auto       |
| Web DLP Coverage                     | =COUNTIF(Web_DLP!C6:C25,"Yes")/20*100          | ≥75%       | Auto       |
| Database DAM Coverage                | =COUNTIF(Database_DAM!C6:C20,"Production")/15*100 | ≥80%    | Auto       |
| SIEM Integration Rate                | =COUNTIF(DLP_Technology_Inventory!N6:N35,"Yes")/Total_Tech*100 | ≥90% | Auto |
| Total Gaps Identified                | =COUNTA(Gap_Analysis!A6:A45)-3                 | ≤10        | Auto       |
| Critical/High Gaps                   | =COUNTIFS(Gap_Analysis!D6:D45,"Critical")+COUNTIFS(Gap_Analysis!D6:D45,"High") | 0 | Auto |
| **Overall Infrastructure Compliance**| =AVERAGE(B7:B15)                               | **≥85%**   | **Auto**   |

#### Section 3: Gap Summary

| **Risk Level** | **Count**                                  | **% of Total** |
|----------------|--------------------------------------------|----------------|
| Critical       | =COUNTIF(Gap_Analysis!D6:D45,"Critical")   | Auto           |
| High           | =COUNTIF(Gap_Analysis!D6:D45,"High")       | Auto           |
| Medium         | =COUNTIF(Gap_Analysis!D6:D45,"Medium")     | Auto           |
| Low            | =COUNTIF(Gap_Analysis!D6:D45,"Low")        | Auto           |

#### Section 4: Evidence Completeness

| **Metric**                  | **Formula**                                      |
|-----------------------------|--------------------------------------------------|
| Evidence Items Collected    | =COUNTA(Evidence_Register!A6:A105)               |
| Evidence Items Verified     | =COUNTIF(Evidence_Register!H6:H105,"Verified")   |
| Evidence Completeness %     | =(Evidence_Verified/Evidence_Collected)*100      |

#### Section 5: Traffic Light Indicators

**Overall Status Formula:**
```excel
=IF(B17>=85,"✅ Compliant",IF(B17>=70,"⚠️ Partial","❌ Non-Compliant"))
```

---

## 5. ASSESSMENT CRITERIA & SCORING

### 5.1 Compliance Scoring Method

**Domain 1 Compliance Score** is calculated as:
```
Domain_1_Score = AVERAGE(
    Network_DLP_Coverage,
    Endpoint_DLP_Coverage,
    Email_DLP_Coverage,
    Cloud_CASB_Coverage,
    Web_DLP_Coverage,
    Database_DAM_Coverage,
    SIEM_Integration_Rate,
    Technology_Maturity_Score,
    Gap_Remediation_Rate
)
```

**Maturity Levels:**

| **Score** | **Level**       | **Description**                                |
|-----------|-----------------|------------------------------------------------|
| 90-100%   | Optimized       | Comprehensive DLP infrastructure, minimal gaps |
| 80-89%    | Managed         | Strong infrastructure, some improvements needed|
| 70-79%    | Defined         | Core infrastructure present, notable gaps      |
| 60-69%    | Developing      | Partial infrastructure, major gaps exist       |
| <60%      | Initial/Ad-Hoc  | Insufficient infrastructure, urgent action     |

### 5.2 Pass/Fail Criteria

**PASS Criteria (Minimum Requirements):**
- ✅ Overall Domain 1 Score ≥ 80%
- ✅ Zero Critical gaps
- ✅ High gaps ≤ 2
- ✅ Endpoint coverage ≥ 90%
- ✅ Email DLP deployed
- ✅ SIEM integration ≥ 80%

**FAIL Criteria (Triggers Non-Compliance):**
- ❌ Overall Domain 1 Score < 70%
- ❌ Critical gaps > 0
- ❌ High gaps > 5
- ❌ Endpoint coverage < 80%
- ❌ No email DLP
- ❌ No SIEM integration

---

## 6. COMPLIANCE MAPPING

### 6.1 ISO/IEC 27001:2022 Mapping

| **Control** | **Requirement**                              | **Evidence Location**        |
|-------------|----------------------------------------------|------------------------------|
| A.8.12      | Data leakage prevention (Master)             | All sheets                   |
| A.5.1       | Policies for information security            | Instructions, related docs   |
| A.5.10      | Acceptable use of information                | Endpoint_DLP (USB, print)    |
| A.8.11      | Data masking                                 | Database_DAM                 |
| A.8.16      | Monitoring activities                        | Summary_Dashboard (SIEM)     |

### 6.2 Regulatory Mapping

| **Regulation** | **Requirement**                         | **Evidence Location**          |
|----------------|-----------------------------------------|--------------------------------|
| FADP Art. 8    | Data security                           | All DLP technologies           |
| GDPR Art. 32   | Security of processing                  | Network, Endpoint, Email DLP   |
| GDPR Art. 5(1)(f) | Integrity and confidentiality        | Summary_Dashboard (coverage)   |

---

## 7. EVIDENCE REQUIREMENTS

### 7.1 Mandatory Evidence

For EACH DLP technology, collect:
1. **Configuration Screenshots** - DLP policy settings, channels monitored
2. **Deployment Proof** - Agent deployment reports, coverage metrics
3. **Integration Logs** - SIEM forwarding configs, SOC ticket integration
4. **License Documentation** - Current license agreements, expiry dates
5. **Architecture Diagrams** - Network topology showing DLP placement
6. **Test Results** - DLP detection/blocking tests (attach logs)

### 7.2 Evidence Naming Convention
```
A812-1-[CATEGORY]-[###]

Examples:
A812-1-INF-001  (Infrastructure - Technology inventory)
A812-1-NET-001  (Network DLP - Configuration screenshot)
A812-1-EPT-001  (Endpoint DLP - Deployment report)
A812-1-EML-001  (Email DLP - Policy config)
A812-1-CLD-001  (Cloud/CASB - CASB dashboard)
```

---

## 8. APPROVAL & SIGN-OFF

### 8.1 Review and Approval Workflow

| **Role**           | **Responsibility**                          | **Timeline**   |
|--------------------|---------------------------------------------|----------------|
| DLP Administrator  | Complete assessment, gather evidence        | Week 1-2       |
| IT Security Lead   | Review technical accuracy                   | Week 3         |
| CISO               | Approve gaps, remediation plans             | Week 3         |
| DPO                | Review privacy impact (employee monitoring) | Week 3         |
| Internal Audit     | Validate evidence completeness              | Week 4         |

### 8.2 Sign-Off Section (in Summary_Dashboard)

| **Approver**       | **Name** | **Signature** | **Date** | **Status**          |
|--------------------|----------|---------------|----------|---------------------|
| DLP Administrator  | [Input]  | [Input]       | [Auto]   | [Dropdown: Approved/Pending] |
| CISO               | [Input]  | [Input]       | [Auto]   | [Dropdown: Approved/Pending] |
| DPO                | [Input]  | [Input]       | [Auto]   | [Dropdown: Approved/Pending] |

---

**END OF SPECIFICATION: ISMS-IMP-A.8.12.1**

*"If the infrastructure isn't documented, it doesn't exist. If it isn't measured, it can't be managed."*  
— W. Edwards Deming (adapted for ISMS by the Grand Guru)


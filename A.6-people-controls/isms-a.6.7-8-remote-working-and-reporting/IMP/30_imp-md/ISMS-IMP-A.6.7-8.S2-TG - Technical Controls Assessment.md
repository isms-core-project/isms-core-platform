**ISMS-IMP-A.6.7-8.S2-TG - Technical Controls Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | VPN, MFA, Encryption, Logging, and Session Management |
| **Related Policy** | ISMS-POL-A.6.7-8, Section 2.3 (Technical Security Requirements) |
| **Purpose** | Guide users through systematic assessment of technical security controls for remote access |
| **Target Audience** | IT Security Team, Network Engineers, Identity Management Team, Auditors |
| **Assessment Type** | Technical |
| **Review Cycle** | Semi-Annual |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for technical controls assessment | ISMS Implementation Team |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.6.7-8.S2-UG.

---

# Technical Specification

### 8. Workbook Architecture

#### 8.1 Sheet Structure

| Sheet Name | Purpose | Sheet Type |
|------------|---------|------------|
| Instructions | User guidance | Static |
| VPN_Infrastructure | VPN inventory | Assessment |
| VPN_Configuration | VPN security settings | Assessment |
| MFA_Deployment | MFA system coverage | Assessment |
| MFA_Compliance | MFA user compliance | Sample Testing |
| Encryption_Assessment | Encryption verification | Assessment |
| Logging_Monitoring | Log and monitor assessment | Assessment |
| Session_Management | Session controls | Assessment |
| Gap_Analysis | Consolidated gaps | Analysis |
| Evidence_Register | Evidence catalog | Register |
| Dashboard | Executive summary | Calculated |
| Approval_Sign_Off | Formal approvals | Governance |

### 9. Column Specifications

#### 9.1 VPN_Infrastructure Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Solution ID | 12 | Text | Auto (VPN-###) |
| B | Solution Name | 25 | Text | Free text |
| C | Vendor | 20 | Text | Free text |
| D | Version | 15 | Text | Free text |
| E | Solution Type | 15 | Dropdown | VPN/ZTNA/RDP Gateway/Other |
| F | Deployment Scope | 30 | Text | Free text |
| G | Users Covered | 12 | Number | Positive integer |
| H | Protocol | 20 | Text | Free text |
| I | Encryption | 20 | Text | Free text |
| J | Compliant | 10 | Dropdown | Yes/No |
| K | Notes | 40 | Text | Free text |

#### 9.2 MFA_Deployment Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Application/System | 30 | Text | Free text |
| B | MFA Required | 12 | Dropdown | Yes/No |
| C | MFA Enforced | 12 | Dropdown | Yes/No |
| D | MFA Method | 20 | Dropdown | See list below |
| E | Fallback Method | 20 | Dropdown | See list below |
| F | Enrollment % | 12 | Percentage | 0-100% |
| G | Exceptions | 30 | Text | Free text |
| H | Compliant | 12 | Formula | =AND(B="Yes",C="Yes",F>=95%) |
| I | Notes | 40 | Text | Free text |

**MFA Method Options**: Hardware Key, Authenticator App, Push Notification, SMS, Voice Call, Email, None

### 10. Formula Specifications

#### 10.1 Dashboard Calculations

**VPN Compliance Score**:
```
=COUNTIF(VPN_Infrastructure!J:J,"Yes")/COUNTA(VPN_Infrastructure!J2:J50)
```

**MFA Coverage**:
```
=AVERAGE(MFA_Deployment!F:F)
```

**MFA Enforcement Rate**:
```
=COUNTIF(MFA_Compliance!E:E,"Yes")/COUNTA(MFA_Compliance!E2:E100)
```

**Encryption Compliance**:
```
=COUNTIF(Encryption_Assessment!G:G,"Yes")/COUNTA(Encryption_Assessment!G2:G50)
```

### 11. Styling Specifications

#### 11.1 Compliance Status Colors

| Status | Fill Color | Use |
|--------|------------|-----|
| Compliant/Yes | #C6EFCE (Light Green) | Passing items |
| Non-Compliant/No | #FFC7CE (Light Red) | Failing items |
| Partial | #FFEB9C (Light Yellow) | Partial compliance |
| N/A | #D9D9D9 (Gray) | Not applicable |

#### 11.2 Risk/Priority Colors

| Level | Fill Color |
|-------|------------|
| High/Critical | #FF6B6B (Red) |
| Medium | #FFD93D (Yellow) |
| Low | #6BCB77 (Green) |

### 12. Data Validation Lists

#### 12.1 Dropdown Options

| Field | Options |
|-------|---------|
| Solution Type | VPN, ZTNA, RDP Gateway, SSH Gateway, Other |
| MFA Method | Hardware Key, Authenticator App, Push Notification, SMS, Voice Call, Email, None |
| User Type | Employee, Contractor, Administrator, Service Account |
| Effort Estimate | High, Medium, Low |
| Gap Status | Open, In Progress, Closed, Deferred, Accepted |
| Evidence Type | Config Export, Screenshot, Report, Test Result, Log Sample, Diagram |

### 13. Pre-Populated Content

#### 13.1 VPN Configuration Items

| Configuration Item | Requirement |
|--------------------|-------------|
| Encryption Algorithm | AES-256 or equivalent |
| Key Exchange | IKEv2 with DH Group 14+ or better |
| Perfect Forward Secrecy | Enabled |
| Split Tunneling | Disabled or controlled by policy |
| Idle Session Timeout | 30 minutes maximum |
| Failed Login Lockout | Lock after 5 failed attempts |
| Certificate Authentication | Enabled for machine auth |
| Weak Cipher Suites | Disabled (no DES, 3DES, RC4, MD5) |
| TLS Version | TLS 1.2 minimum, TLS 1.3 preferred |
| Logging | All connections and authentications logged |

#### 13.2 Encryption Domains

| Domain | Requirement |
|--------|-------------|
| VPN Tunnel | AES-256-GCM or AES-256-CBC |
| Web Applications (External) | TLS 1.2+ with strong cipher suites |
| Web Applications (Internal) | TLS 1.2+ recommended |
| Email (SMTP) | TLS 1.2+ with opportunistic encryption |
| File Transfer | SFTP or FTPS (not plain FTP) |
| API Communications | TLS 1.2+ |
| Database Connections | Encrypted connections or network segmentation |
| Disk Encryption | Full-disk encryption on remote devices |

#### 13.3 Log Categories

| Log Category | Minimum Content | Retention |
|--------------|-----------------|-----------|
| VPN Connections | User, timestamp, IP, duration | 90 days |
| Authentication Events | User, timestamp, result, source IP | 90 days |
| MFA Events | User, method, result, timestamp | 90 days |
| Failed Logins | User, timestamp, source IP, failure reason | 180 days |
| Privileged Access | User, action, target, timestamp | 1 year |
| Session Events | Session start/end, idle timeouts | 90 days |

---

## END OF SPECIFICATION

---

*"Complexity is the enemy of security."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-06 -->

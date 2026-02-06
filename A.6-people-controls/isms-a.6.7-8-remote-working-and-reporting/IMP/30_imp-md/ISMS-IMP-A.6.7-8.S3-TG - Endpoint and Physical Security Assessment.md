**ISMS-IMP-A.6.7-8.S3-TG - Endpoint and Physical Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Device Security, Encryption, Endpoint Protection, Physical Security |
| **Related Policy** | ISMS-POL-A.6.7-8, Sections 2.2 (Physical Security) & 2.5 (Device Security) |
| **Purpose** | Guide users through assessment of endpoint security controls and physical security for remote work |
| **Target Audience** | IT Security Team, Endpoint Management Team, Desktop Support, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly (technical), Annual (physical) |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for endpoint and physical security assessment | ISMS Implementation Team |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.6.7-8.S3-UG.

---

# Technical Specification

### 8. Workbook Architecture

#### 8.1 Sheet Structure

| Sheet Name | Purpose | Sheet Type |
|------------|---------|------------|
| Instructions | User guidance | Static |
| Device_Inventory | Device catalog | Inventory |
| Encryption_Status | Encryption assessment | Assessment |
| Endpoint_Protection | EDR/AV assessment | Assessment |
| Patch_Compliance | Patch status | Assessment |
| BYOD_Assessment | Personal device assessment | Assessment |
| Physical_Security | Physical security | Assessment |
| Lost_Stolen_Procedures | Incident procedures | Assessment |
| Gap_Analysis | Consolidated gaps | Analysis |
| Evidence_Register | Evidence catalog | Register |
| Dashboard | Executive summary | Calculated |
| Approval_Sign_Off | Formal approvals | Governance |

### 9. Column Specifications

#### 9.1 Device_Inventory Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Device ID | 15 | Text | Auto (DEV-####) |
| B | Device Type | 12 | Dropdown | Laptop/Desktop/Tablet/Mobile |
| C | Ownership | 12 | Dropdown | Corporate/BYOD/Contractor |
| D | OS | 15 | Text | Free text |
| E | OS Version | 12 | Text | Free text |
| F | Assigned User | 25 | Text | Free text |
| G | Department | 20 | Text | Free text |
| H | Remote Enabled | 12 | Dropdown | Yes/No |
| I | MDM Enrolled | 12 | Dropdown | Yes/No |
| J | Last Check-in | 12 | Date | Date format |
| K | Status | 12 | Dropdown | Active/Inactive/Lost/Retired |

### 10. Formula Specifications

#### 10.1 Dashboard Calculations

**Encryption Compliance Rate**:
```
=COUNTIF(Encryption_Status!G:G,"Yes")/COUNTA(Encryption_Status!G2:G500)
```

**Endpoint Protection Coverage**:
```
=COUNTIF(Endpoint_Protection!I:I,"Yes")/COUNTA(Endpoint_Protection!I2:I500)
```

**Patch Compliance Rate**:
```
=COUNTIF(Patch_Compliance!H:H,"Yes")/COUNTA(Patch_Compliance!H2:H500)
```

### 11. Pre-Populated Content

#### 11.1 Physical Security Requirements

| Requirement Category | Requirement |
|---------------------|-------------|
| Screen Privacy | Position screen away from windows and common areas |
| Screen Privacy | Use privacy screen filter in public spaces |
| Secure Storage | Lockable cabinet or drawer for sensitive documents |
| Device Security | Cable lock or secure storage for portable devices |
| Device Security | Never leave devices unattended in public |
| Document Handling | Shred sensitive documents (cross-cut shredder) |
| Document Handling | Clear desk when leaving workspace |
| Access Control | Prevent family/visitor access to work devices |
| Travel Security | Carry devices in hand luggage |
| Travel Security | Never leave devices in vehicles |

#### 11.2 Lost/Stolen Procedure Elements

| Element | Requirement |
|---------|-------------|
| Reporting Channel | 24/7 hotline or email for reporting |
| Account Disable | Ability to disable account within 1 hour |
| Remote Lock | Ability to lock device remotely within 1 hour |
| Remote Wipe | Ability to wipe device remotely within 4 hours |
| Recovery Key Access | Access to recovery keys for encrypted devices |
| Replacement Process | Process to issue replacement device |
| Incident Documentation | Record of incident details |
| Investigation | Follow-up investigation procedure |
| Insurance | Device covered by insurance (if applicable) |

---

## END OF SPECIFICATION

---

*"Physical security is the foundation upon which all other security measures are built."*
— ASIS International

<!-- QA_VERIFIED: 2026-02-06 -->

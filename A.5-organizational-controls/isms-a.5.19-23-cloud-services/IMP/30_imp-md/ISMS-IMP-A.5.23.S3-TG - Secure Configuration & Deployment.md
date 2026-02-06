**ISMS-IMP-A.5.23.S3-TG - Secure Configuration & Deployment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Secure Configuration & Deployment |
| **Related Policy** | ISMS-POL-A.5.19-23-S5 (Cloud Services Security - Sections 5, 9) |
| **Purpose** | Assess and document secure configuration of cloud services across identity, data protection, network, logging, and backup controls |
| **Target Audience** | IT Operations, Cloud Operations, DevOps Engineers, Cloud Security Engineers, Platform Engineering |
| **Assessment Type** | Technical Configuration Assessment |
| **Review Cycle** | Quarterly (with continuous monitoring) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.23.S3-UG.

---

# Technical Specification

## Workbook Structure Overview

**File:** `ISMS-IMP-A.5.23.S3_SecureConfig_YYYYMMDD.xlsx`

**Total Sheets:** 10

**Architecture:**
```
Sheet 1:  Instructions & Legend (read-only reference)
Sheet 2:  Identity & Access Configuration (IAM layer)
Sheet 3:  Data Protection Configuration (encryption, DLP)
Sheet 4:  Network Security Configuration (firewall, VPN, API)
Sheet 5:  Logging & Monitoring Configuration (audit logs, SIEM)
Sheet 6:  Backup & Recovery Configuration (BC/DR)
Sheet 7:  Jurisdictional Risk Configuration Alignment (links to IMP-5.23.2)
Sheet 8:  Summary Dashboard (formulas, auto-calculated)
Sheet 9:  Evidence Register (central evidence tracking)
Sheet 10: Approval Sign-Off (workflow, signatures)
```

---

## Standard Column Definitions (A-Q)

**Present in ALL configuration sheets (Sheets 2-6):**

| Col | Header | Type | Validation | Default/Formula |
|-----|--------|------|------------|-----------------|
| A | Cloud Service Name | Text | Dropdown (from IMP-5.23.1) | - |
| B | Vendor Name | Text | Dropdown (from IMP-5.23.1) | - |
| C | Service Type | Text | Dropdown: SaaS, IaaS, PaaS, Security Service | - |
| D | Service Criticality | Text | Dropdown: Critical, High, Medium, Low | From IMP-5.23.1 |
| E | Data Classification | Text | Dropdown: Restricted, Confidential, Internal, Public | From IMP-5.23.1 |
| F | Deployment Environment | Text | Dropdown: Production, Staging, Development, Test | - |
| G | IaC Managed? | Text | Dropdown: Yes (Terraform/CF/ARM), No (Manual), Partial | - |
| H | Status | Text | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | - |
| I | Evidence Location | Text | Hyperlink or file path | - |
| J | Gap Description | Text | Free text (required if H ≠ ✅) | - |
| K | Remediation Needed | Text | Dropdown: Yes, No | - |
| L | Exception ID | Text | Pattern: EXC-YYYY-NNN | - |
| M | Risk ID | Text | Pattern: RISK-YYYY-NNN | - |
| N | Compensating Controls | Text | Free text | - |
| O | Configuration Owner | Text | Free text (team/person) | - |
| P | Target Remediation Date | Date | Date picker (DD.MM.YYYY) | - |
| Q | Last Config Review Date | Date | Date picker (auto: today) | - |

---

## Sheet-Specific Extended Columns (Summary)

### Sheet 2: Identity & Access (Columns R-AA)

- R: SSO Integration, S: SSO Protocol, T: MFA Enforcement, U: MFA Methods
- V: RBAC Implemented, W: Privileged Access Mgmt, X: Access Review Frequency
- Y: Last Access Review Date, Z: Session Timeout, AA: Password Policy

### Sheet 3: Data Protection (Columns R-Z)

- R: Encryption At-Rest, S: Key Management, T: Key Rotation
- U: Encryption In-Transit, V: Certificate Validation, W: DLP Configured
- X: DLP Rules Count, Y: Classification Labels Applied, Z: Backup Encrypted

### Sheet 4: Network Security (Columns R-X)

- R: IP Access Control, S: IP Ranges Allowed, T: VPN Required
- U: Private Connectivity, V: API Authentication, W: API Rate Limiting, X: Network Segmentation

### Sheet 5: Logging & Monitoring (Columns R-W)

- R: Audit Logging Enabled, S: Events Logged, T: Log Retention (Days)
- U: SIEM Integration, V: SIEM Tool, W: Alerts Configured

### Sheet 6: Backup & Recovery (Columns R-Y)

- R: Backup Frequency, S: Backup Scope, T: Backup Encrypted
- U: Backup Storage Location, V: RTO (Hours), W: RPO (Hours)
- X: Last DR Test Date, Y: DR Test Result

**See Part I, Section 4 for detailed column definitions and validation rules.**

---

## Sheet 8: Summary Dashboard (Formulas)

**Auto-Calculated Metrics:**

| Metric | Formula Example | Description |
|--------|-----------------|-------------|
| Total Services Assessed | `=COUNTA(Sheet2!A:A)-1` | Row count |
| Overall Compliance % | `=(SUM(COUNTIF(Sheet2!H:H,"✅"), COUNTIF(Sheet3!H:H,"✅"), ...) / Total_Rows) * 100` | Avg compliance across all layers |
| Identity Compliance % | `=COUNTIF(Sheet2!H:H,"✅")/COUNTA(Sheet2!H:H)*100` | Sheet 2 specific |
| Data Protection Compliance % | `=COUNTIF(Sheet3!H:H,"✅")/COUNTA(Sheet3!H:H)*100` | Sheet 3 specific |
| Critical Services Compliant | `=COUNTIFS(Sheet2!D:D,"Critical", Sheet2!H:H,"✅")` | Critical + compliant |
| Services Without MFA | `=COUNTIF(Sheet2!T:T,"None")` | MFA gap count |
| Services Without Encryption | `=COUNTIF(Sheet3!R:R,"None")` | Encryption gap count |
| Services Not Logging to SIEM | `=COUNTIF(Sheet5!U:U,"None")` | SIEM integration gap |

---

## Python Generator Script Notes

**Script:** `generate_reg_a523_3_secure_config.py`

**Key Functions:**

- `create_2_identity_access()` - Sheet 2 with IAM columns
- `create_3_data_protection()` - Sheet 3 with encryption columns
- `create_4_network_security()` - Sheet 4 with network columns
- `create_5_logging_monitoring()` - Sheet 5 with logging columns
- `create_6_backup_recovery()` - Sheet 6 with BC/DR columns
- `create_8_dashboard()` - Sheet 8 with aggregation formulas

**Customization Points:**

- Dropdown lists (service names, vendors)
- Conditional formatting (risk-based coloring)
- Dashboard metrics (add custom KPIs)
- Compliance thresholds (≥90% vs ≥95%)

**Usage:**
```bash
python3 generate_reg_a523_3_secure_config.py
# Output: ISMS-IMP-A.5.23.S3_SecureConfig_20260120.xlsx
```

---

**END OF SPECIFICATION**

---

*"Know how to solve every problem that has been solved."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->

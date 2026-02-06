**ISMS-IMP-A.8.30.2-TG - Contract Compliance**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.2-TG |
| **Document Title** | Contract Compliance Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

# Technical Specification

This section provides technical details for the Contract Compliance workbook implementation, including Excel specifications, data validation rules, and automation requirements.

---

## 9. Workbook Technical Structure

### 9.1 Workbook Properties

| Property | Value |
|----------|-------|
| File Format | .xlsx (Excel 2016+) |
| Sheet Protection | Structure protected, cells unlocked for input |
| Workbook Protection | Structure only |
| File Naming | ISMS-IMP-A.8.30.2_Contract_Compliance_YYYYMMDD.xlsx |

### 9.2 Sheet Configuration

| Sheet | Tab Colour | Protection Level | Hidden |
|-------|------------|------------------|--------|
| Contract Inventory | Blue (#4472C4) | Input cells unlocked | No |
| Security Clause Checklist | Green (#70AD47) | Input cells unlocked | No |
| SLA Compliance Tracking | Orange (#ED7D31) | Input cells unlocked | No |
| Subcontractor Approvals | Purple (#7030A0) | Input cells unlocked | No |
| Termination Checklist | Red (#C00000) | Input cells unlocked | No |
| Validation Lists | Grey (#A6A6A6) | Full protection | Yes |
| Dashboard | Dark Blue (#002060) | Full protection | No |

---

## 10. Sheet Specifications

### 10.1 Sheet 1: Contract Inventory – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Contract_ID | 15 | Text | Format: CTR-#### | Yes |
| B | Vendor_ID | 15 | Reference | Must exist in Vendor Registry | Yes |
| C | Contract_Name | 40 | Text | Max 200 chars | Yes |
| D | Contract_Type | 20 | List | Fixed-price,T&M,Staff Aug,Managed Service | Yes |
| E | Start_Date | 15 | Date | DD.MM.YYYY | Yes |
| F | End_Date | 15 | Date | DD.MM.YYYY, > Start_Date | Yes |
| G | Project_Classification | 15 | List | Critical,High,Standard | Yes |
| H | Contract_Value | 15 | Currency | CHF, >= 0 | Yes |
| I | Primary_Contact | 25 | Text | Employee name | Yes |
| J | Legal_Review_Date | 15 | Date | DD.MM.YYYY | Yes |
| K | Security_Review_Date | 15 | Date | DD.MM.YYYY | Yes |
| L | Status | 15 | List | Active,Completed,Terminated | Yes |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| End_Date < TODAY() + 90 AND Status = "Active" | Yellow fill |
| End_Date < TODAY() + 30 AND Status = "Active" | Orange fill |
| Status = "Terminated" | Red fill |
| Security_Review_Date is empty | Red border |

### 10.2 Sheet 2: Security Clause Checklist – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Contract_ID | 15 | Reference | Must exist in Inventory | Yes |
| B | Clause_Category | 30 | Text | Pre-populated | Yes |
| C | Clause_Description | 50 | Text | Check description | Yes |
| D | Included | 12 | List | Yes,No,N/A,Modified | Yes |
| E | Clause_Reference | 20 | Text | Contract section | Conditional |
| F | Modification_Notes | 40 | Text | If Modified | Conditional |
| G | Reviewed_By | 20 | Text | Name | Yes |
| H | Review_Date | 15 | Date | DD.MM.YYYY | Yes |

**Pre-populated Clause Categories (70+ rows per contract):**

| Category | Check Items |
|----------|-------------|
| 1. Secure Coding Standards | 4 items |
| 2. Security Policy Compliance | 4 items |
| 3. Vulnerability Remediation SLAs | 5 items |
| 4. Security Testing Rights | 4 items |
| 5. Audit Rights | 5 items |
| 6. Incident Notification | 4 items |
| 7. Data Protection/Confidentiality | 5 items |
| 8. Subcontractor Restrictions | 4 items |
| 9. IP/Code Ownership | 4 items |
| 10. Source Code Escrow | 4 items |
| 11. Personnel Security | 4 items |
| 12. Termination/Transition | 4 items |
| 13. Insurance Requirements | 4 items |
| 14. Liability Provisions | 4 items |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Included = "No" | Red fill |
| Included = "Modified" | Yellow fill |
| Included = "N/A" | Grey fill |

### 10.3 Sheet 3: SLA Compliance Tracking – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | SLA_ID | 15 | Text | Format: SLA-#### | Yes |
| B | Contract_ID | 15 | Reference | Must exist in Inventory | Yes |
| C | Vulnerability_ID | 20 | Text | Vuln reference | Yes |
| D | Severity | 12 | List | Critical,High,Medium,Low | Yes |
| E | Discovery_Date | 15 | Date | DD.MM.YYYY | Yes |
| F | SLA_Days | 10 | Number | 7/30/90/180 based on severity | Auto |
| G | SLA_Due_Date | 15 | Date | Calculated | Auto |
| H | Remediation_Date | 15 | Date | DD.MM.YYYY | Conditional |
| I | SLA_Met | 12 | List | Met,Missed,Pending,Exception | Yes |
| J | Exception_Approved | 12 | List | Yes,No,N/A | Conditional |
| K | Exception_Approver | 25 | Text | Name + Role | Conditional |
| L | Notes | 40 | Text | Optional | No |

**Formulas:**

```excel
SLA_Days (F2):
=IF(D2="Critical",7,IF(D2="High",30,IF(D2="Medium",90,180)))

SLA_Due_Date (G2):
=E2+F2

SLA_Met (I2) - Suggested:
=IF(ISBLANK(H2),"Pending",IF(H2<=G2,"Met","Missed"))
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| SLA_Met = "Missed" | Red fill |
| SLA_Met = "Pending" AND SLA_Due_Date < TODAY() | Red fill |
| SLA_Met = "Pending" AND SLA_Due_Date < TODAY()+7 | Orange fill |
| SLA_Met = "Exception" | Yellow fill |
| SLA_Met = "Met" | Green fill |

### 10.4 Sheet 4: Subcontractor Approvals – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Approval_ID | 15 | Text | Format: SUB-#### | Yes |
| B | Contract_ID | 15 | Reference | Must exist in Inventory | Yes |
| C | Primary_Vendor_ID | 15 | Reference | Must exist in Registry | Yes |
| D | Subcontractor_Name | 35 | Text | Legal name | Yes |
| E | Subcontractor_Scope | 40 | Text | Work description | Yes |
| F | Access_Level | 15 | List | Direct,Via Vendor,None | Yes |
| G | Assessment_Level | 20 | List | Full,Abbreviated,Vendor Attested | Yes |
| H | Risk_Classification | 12 | List | High,Medium,Low | Yes |
| I | Approval_Status | 15 | List | Approved,Pending,Rejected | Yes |
| J | Approved_By | 25 | Text | Name + Role | Conditional |
| K | Approval_Date | 15 | Date | DD.MM.YYYY | Conditional |
| L | Expiry_Date | 15 | Date | DD.MM.YYYY | Yes |
| M | Flow_Down_Verified | 12 | List | Yes,No | Yes |
| N | Notes | 40 | Text | Optional | No |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Approval_Status = "Rejected" | Red fill |
| Approval_Status = "Pending" | Yellow fill |
| Expiry_Date < TODAY() AND Approval_Status = "Approved" | Orange fill |
| Expiry_Date < TODAY()+30 AND Approval_Status = "Approved" | Yellow fill |

### 10.5 Sheet 5: Termination Checklist – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Contract_ID | 15 | Reference | Must exist in Inventory | Yes |
| B | Termination_Type | 15 | List | Completion,Early,Breach | Yes |
| C | Termination_Date | 15 | Date | DD.MM.YYYY | Yes |
| D | Check_Item | 50 | Text | Pre-populated | Yes |
| E | Status | 12 | List | Complete,Pending,N/A | Yes |
| F | Completion_Date | 15 | Date | DD.MM.YYYY | Conditional |
| G | Verified_By | 20 | Text | Name | Conditional |
| H | Evidence_Reference | 40 | Text | File path/URL | Conditional |

**Pre-populated Check Items (10 standard items per contract):**

1. All access credentials revoked (within 24 hours)
2. Organisation data returned or destroyed
3. Destruction certificate received
4. Source code transferred (if applicable)
5. Documentation transferred
6. Escrow arrangements verified
7. Outstanding vulnerabilities addressed or risk accepted
8. Final security review completed
9. Lessons learned documented
10. Vendor removed from active registry

---

## 11. Automation Requirements

### 11.1 Automated Alerts

| Trigger | Alert Type | Recipients | Timing |
|---------|------------|------------|--------|
| Contract expiring | Email | Procurement, IT Security | 90, 60, 30 days |
| SLA approaching due date | Email | IT Security | 3 days before |
| SLA overdue | Email + Dashboard flag | IT Security Manager, CISO | Immediate |
| Subcontractor approval expiring | Email | IT Security | 30 days |
| Missing security review | Dashboard flag | IT Security | Continuous |

### 11.2 Data Validation Automation

| Validation | Action | Frequency |
|------------|--------|-----------|
| Contract_ID uniqueness | Prevent duplicate | On entry |
| Vendor_ID exists in Registry | Validation error | On entry |
| End_Date > Start_Date | Validation error | On entry |
| SLA calculation | Auto-calculate | On entry |
| Required field completion | Highlight | Real-time |

### 11.3 Dashboard Calculations

| Metric | Formula | Refresh |
|--------|---------|---------|
| Active contracts | COUNT where Status=Active | Daily |
| Clause compliance rate | Yes / (Yes + No + Modified) | Daily |
| SLA compliance rate | Met / (Met + Missed) | Daily |
| Pending subcontractors | COUNT where Status=Pending | Daily |
| Termination progress | Complete / Total items | Daily |

---

## 12. Metrics and KPIs

### 12.1 Contract Compliance Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| Security clause inclusion | 100% mandatory | Compliant contracts / Total | IT Security |
| Contracts with security review | 100% before execution | Reviewed / Total | IT Security |
| Clause compliance by category | 100% per category | Category compliant / Total | IT Security |

### 12.2 SLA Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| Critical SLA compliance | ≥95% | Met / Total Critical | IT Security |
| High SLA compliance | ≥90% | Met / Total High | IT Security |
| Average remediation time | Per SLA | Avg days to fix | IT Security |
| Exception rate | <10% | Exceptions / Total | CISO |

### 12.3 Subcontractor Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| Pre-approval compliance | 100% | Approved before work / Total | IT Security |
| Flow-down verification | 100% | Verified / Total | IT Security |
| Expired approval rate | 0% | Expired / Active | IT Security |

---

## 13. Evidence Package for ISO 27001 Audit

### 13.1 Standard Evidence Package Contents

| Document | Purpose | Preparation |
|----------|---------|-------------|
| Contract inventory | Active development contracts | Export Sheet 1 |
| Clause compliance summary | Security clause inclusion | Export Sheet 2 aggregated |
| SLA compliance report | Remediation performance | Sheet 3 12-month summary |
| Subcontractor register | Approved subcontractors | Export Sheet 4 |
| Sample termination packages | Contract closure evidence | Complete Sheet 5 examples |
| Non-compliance records | Exception handling | Exception register extract |

### 13.2 Audit Preparation Checklist

- [ ] Export current contract inventory
- [ ] Generate clause compliance summary
- [ ] Prepare SLA compliance statistics (12 months)
- [ ] Verify all subcontractor approvals current
- [ ] Prepare sample contract packages (3-5)
- [ ] Compile termination examples (if applicable)
- [ ] Document non-compliance handling

---

## 14. Generator Script Reference

### 14.1 Script Location

```
10-isms-scr-base/
└── isms-a.8.30-outsourced-development/
    └── 10_generator-master/
        └── generate_a830_2_contract_compliance.py
```

### 14.2 Script Execution

```bash
cd 10-isms-scr-base/isms-a.8.30-outsourced-development/10_generator-master
python3 generate_a830_2_contract_compliance.py
mv *.xlsx ../90_workbooks/
```

### 14.3 Output

```
ISMS-IMP-A.8.30.2_Contract_Compliance_YYYYMMDD.xlsx
```

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-06 -->

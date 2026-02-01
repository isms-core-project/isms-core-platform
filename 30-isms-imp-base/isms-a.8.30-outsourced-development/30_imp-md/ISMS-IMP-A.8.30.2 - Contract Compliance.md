# ISMS-IMP-A.8.30.2 – Contract Compliance

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.2 |
| **Document Title** | Contract Compliance Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

---

## 1. Workbook Purpose

This workbook tracks security clause inclusion in outsourced development contracts and monitors ongoing contract compliance.

**Primary Use Cases**:
- Verify contracts include mandatory security clauses
- Track vendor compliance with contractual obligations
- Monitor vulnerability remediation SLA compliance
- Document subcontractor approvals
- Evidence collection for audits

---

## 2. Workbook Structure

### Sheet 1: Contract Inventory

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Contract_ID | Unique contract identifier | Text | CTR-XXXX format |
| Vendor_ID | Link to approved vendor | Reference | Valid Vendor_ID |
| Contract_Name | Contract/project name | Text | Required |
| Contract_Type | Type of engagement | Dropdown | Fixed-price, T&M, Staff Aug, Managed Service |
| Start_Date | Contract start date | Date | DD.MM.YYYY |
| End_Date | Contract end date | Date | DD.MM.YYYY |
| Project_Classification | Risk classification | Dropdown | Critical, High, Standard |
| Contract_Value | Total contract value | Currency | CHF |
| Primary_Contact | [Organization] project manager | Text | Name |
| Legal_Review_Date | Date of legal review | Date | DD.MM.YYYY |
| Security_Review_Date | Date of security review | Date | DD.MM.YYYY |
| Status | Contract status | Dropdown | Active, Completed, Terminated |

### Sheet 2: Security Clause Checklist

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Contract_ID | Link to contract | Reference | Valid Contract_ID |
| Clause_Category | Security clause category | Text | Category name |
| Clause_Description | Specific clause requirement | Text | Clause description |
| Included | Clause included in contract | Dropdown | Yes, No, N/A, Modified |
| Clause_Reference | Section/paragraph reference | Text | Contract section |
| Modification_Notes | If modified, describe changes | Text | Optional |
| Reviewed_By | Person who verified | Text | Name |
| Review_Date | Date verified | Date | DD.MM.YYYY |

**Mandatory Security Clause Categories**:
1. Secure Coding Standards Compliance
2. Security Policy Compliance
3. Vulnerability Remediation SLAs
4. Security Testing Rights
5. Audit Rights
6. Incident Notification (24-hour)
7. Data Protection/Confidentiality
8. Subcontractor Restrictions
9. IP/Code Ownership
10. Source Code Escrow (if applicable)
11. Personnel Security Requirements
12. Termination/Transition Security
13. Insurance Requirements
14. Liability Provisions

### Sheet 3: SLA Compliance Tracking

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| SLA_ID | Unique SLA record | Text | SLA-XXXX format |
| Contract_ID | Link to contract | Reference | Valid Contract_ID |
| Vulnerability_ID | Vulnerability identifier | Text | From security testing |
| Severity | Vulnerability severity | Dropdown | Critical, High, Medium, Low |
| Discovery_Date | Date vulnerability identified | Date | DD.MM.YYYY |
| SLA_Days | Contractual SLA (days) | Number | 7/30/90/180 |
| SLA_Due_Date | Calculated due date | Date | Auto-calculated |
| Remediation_Date | Actual remediation date | Date | DD.MM.YYYY |
| SLA_Met | SLA compliance status | Dropdown | Met, Missed, Pending, Exception |
| Exception_Approved | If exception, approval status | Dropdown | Yes, No, N/A |
| Exception_Approver | Exception approver | Text | Name + Role |
| Notes | Additional notes | Text | Optional |

### Sheet 4: Subcontractor Approvals

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Approval_ID | Unique approval identifier | Text | SUB-XXXX format |
| Contract_ID | Link to primary contract | Reference | Valid Contract_ID |
| Primary_Vendor_ID | Primary vendor | Reference | Valid Vendor_ID |
| Subcontractor_Name | Subcontractor legal name | Text | Required |
| Subcontractor_Scope | Work to be subcontracted | Text | Description |
| Access_Level | Access to [Organization] systems | Dropdown | Direct, Via Vendor, None |
| Assessment_Level | Assessment conducted | Dropdown | Full, Abbreviated, Vendor Attested |
| Risk_Classification | Subcontractor risk | Dropdown | High, Medium, Low |
| Approval_Status | Current approval status | Dropdown | Approved, Pending, Rejected |
| Approved_By | Approver | Text | Name + Role |
| Approval_Date | Date approved | Date | DD.MM.YYYY |
| Expiry_Date | Approval expiration | Date | DD.MM.YYYY |
| Flow_Down_Verified | Security flow-down confirmed | Dropdown | Yes, No |
| Notes | Additional notes | Text | Optional |

### Sheet 5: Termination Checklist

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Contract_ID | Link to contract | Reference | Valid Contract_ID |
| Termination_Type | Type of termination | Dropdown | Completion, Early, Breach |
| Termination_Date | Effective termination date | Date | DD.MM.YYYY |
| Check_Item | Termination checklist item | Text | Check description |
| Status | Completion status | Dropdown | Complete, Pending, N/A |
| Completion_Date | Date completed | Date | DD.MM.YYYY |
| Verified_By | Person who verified | Text | Name |
| Evidence_Reference | Evidence document | Text | File path/URL |

**Standard Termination Checklist Items**:
1. All access credentials revoked (within 24 hours)
2. [Organization] data returned or destroyed
3. Destruction certificate received
4. Source code transferred (if applicable)
5. Documentation transferred
6. Escrow arrangements verified
7. Outstanding vulnerabilities addressed or risk accepted
8. Final security review completed
9. Lessons learned documented
10. Vendor removed from active registry

---

## 3. Data Sources

| Data Element | Source System | Collection Method |
|--------------|---------------|-------------------|
| Contract information | Contract Management System | Import/Manual |
| Clause verification | Legal review | Manual checklist |
| SLA data | Vulnerability tracking system | Import |
| Subcontractor approvals | Approval workflow | Manual entry |
| Termination status | Project management | Manual checklist |

---

## 4. Compliance Workflow

```
Contract Initiation:
1. Contract drafted by Procurement/Legal
         ↓
2. Security clause checklist completed
         ↓
3. Security review and approval
         ↓
4. Contract executed

Ongoing Compliance:
5. SLA compliance monitored (continuous)
         ↓
6. Subcontractor approvals processed (as needed)
         ↓
7. Quarterly compliance review

Termination:
8. Termination checklist initiated
         ↓
9. All security items verified
         ↓
10. Contract closed in registry
```

---

## 5. Metrics and KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Security clause inclusion | 100% mandatory clauses | Compliant contracts / Total contracts |
| Critical vulnerability SLA compliance | ≥95% | SLAs met / Total Critical SLAs |
| High vulnerability SLA compliance | ≥90% | SLAs met / Total High SLAs |
| Subcontractor approval compliance | 100% pre-approved | Approved before work / Total subcontractors |
| Termination checklist completion | 100% within 30 days | Complete terminations / Total terminations |

---

## 6. Automation Requirements

**Automated Alerts**:
- SLA approaching due date (3 days before)
- SLA overdue (immediate)
- Contract expiring (90/60/30 days)
- Subcontractor approval expiring (30 days)

**Data Validation**:
- Contract_ID uniqueness
- Valid vendor references
- Date logic (end > start)
- SLA calculation automation

---

## 7. Evidence Package

For ISO 27001 audit, generate:
- Contract inventory with clause compliance summary
- SLA compliance report (12 months)
- Subcontractor approval records
- Sample termination checklists
- Non-compliance incident log

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-01 -->

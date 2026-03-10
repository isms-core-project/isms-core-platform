<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.4.2-4-TG:privacy:TG:a.2.4.2-4 -->
**PRIV-IMP-A.2.4.2-4-TG — Processor Lifecycle Controls — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Processor Lifecycle Controls — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.2.4.2-4-TG |
| **Related Policy** | PRIV-POL-A.2.4.2-4 (Processor Lifecycle Controls) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.2.4.2-4 (Processor Lifecycle Controls — the governing policy)
- PRIV-IMP-A.2.4.2-4-UG (Processor Lifecycle Controls — User Guide)
- PRIV-IMP-A.1.4.6-10-TG (Controller PII Lifecycle — disposal methods reference)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and templates** for processor lifecycle controls. It covers:

- Processor Temporary File Register schema
- End-of-Service PII Handling Log schema
- Disposal Confirmation template (for customer delivery)
- Return/Transfer/Disposal Policy statement (for customer-facing availability)
- Processor Transmission Log schema

**Audience**: DPO, IT Security Team / CISO, Customer Success.

---

## 1. Processor Temporary File Register

Documents all categories of temporary files created during customer PII processing, with disposal periods and mechanism. Maintained by IT Security Team, reviewed annually with DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Temp File ID | Text | Unique reference (e.g., PTMP-001) |
| File Type / Description | Text | What the temporary file is (e.g., "Batch staging table — customer import") |
| Service / Processing Context | Text | Which [Organisation] service or processing activity generates this file |
| Customer PII Categories Contained | Text | What customer PII may be in this file |
| Maximum Retention Period | Text | Documented maximum retention after creation or processing completion |
| Disposal Trigger | Text | What event starts the clock (e.g., "Processing job completion", "Export delivery confirmation") |
| Disposal Mechanism | Enum | Automated Job / TTL / Manual / Overwrite |
| Mechanism Configured | Boolean | Yes / No |
| Configuration Reference | Text | System or job name implementing automated disposal |
| Last Verified | Date | Date disposal mechanism was last confirmed as operational |
| Notes | Text | Manual oversight requirements, pending automation |

### Reference: Standard Processor Temporary File Disposal Periods

| File Type | Maximum Retention | Trigger | Preferred Mechanism |
|-----------|-----------------|---------|---------------------|
| Processing cache / staging tables | 48 hours | Processing job completion | Post-job cleanup script |
| Customer export / delivery files | 72 hours | Confirmed delivery to customer | Scheduled deletion job |
| Error / exception logs with PII | 30 days | Continuous / log rotation | Log rotation with secure deletion |
| Debugging snapshots with PII | Immediate (same session) | End of debugging session | Manual with IT Security confirmation |

---

## 2. End-of-Service PII Handling Log

Records all end-of-service PII handling actions per customer. Maintained by Customer Success / DPO. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Record ID | Text | Unique reference (e.g., EOS-2026-001) |
| Customer Name | Text | Customer whose contract has ended |
| DPA Reference | Text | Linked Processor Agreement Register entry |
| Trigger Type | Enum | Contract Expiry / Customer Termination / In-Contract Deletion Request |
| Trigger Date | Date | Date the end-of-service trigger occurred |
| Customer Instruction Requested Date | Date | Date [Organisation] contacted customer to obtain instruction |
| Customer Instruction Received Date | Date | Date customer provided written instruction |
| Customer Instruction | Enum | Return / Transfer / Disposal |
| Action Scope | Text | Systems and data categories in scope for the action |
| Execution Start Date | Date | Date action commenced |
| Primary Systems Completion Date | Date | Date action completed in primary systems |
| Backup Handling | Text | Approach for backup data — scheduled overwrite date or out-of-cycle deletion date |
| Transfer Recipient (if applicable) | Text | Receiving processor name and confirmation details |
| Legal Retention Residuals | Text | Any PII retained under legal obligation — scope, basis, and expected retention period |
| Disposal Confirmation Sent | Boolean | Yes / No |
| Confirmation Sent Date | Date | Date Disposal Confirmation was sent to customer |
| Status | Enum | Open / Completed / Partial (legal residuals retained) |
| Notes | Text | Exceptional circumstances, customer-specific requirements |

---

## 3. Disposal Confirmation Template

Sent to the customer to confirm return, transfer, or disposal of their PII at end of service.

```
SUBJECT: PII End-of-Service Confirmation — [Customer Name] — [Service / Contract Reference]

Dear [Customer DPO / Legal Contact Name],

This letter confirms the handling of your organisation's personal data processed by
[Organisation] under the Data Processing Agreement dated [Date], reference [DPA-CUST-XXX],
in connection with the termination of services effective [Service End Date].

ACTION TAKEN
[ ] Return — your data was returned to you on [Date] via [method].
    Format: [Format description]
    Delivery confirmation: [confirmation reference]

[ ] Transfer — your data was transferred to [Receiving Processor Name] on [Date]
    via [method].
    Transfer confirmation: [confirmation reference]

[ ] Disposal — your data has been securely deleted as described below.

SCOPE OF ACTION
The following systems and data categories were included in this action:

| System | Data Categories | Action Date | Confirmed By |
|--------|----------------|-------------|--------------|
| | | | |
| | | | |

BACKUP DATA
[ ] Backup deletion is scheduled for the next backup overwrite cycle.
    Expected deletion date: [Date]
    We will confirm completion separately.

[ ] Backup deletion has been completed. Date: [Date]

[ ] No backup data applies to this engagement.

RETAINED DATA (if applicable)
[Organisation] is required by law to retain the following data beyond the service end date:

| Data Category | Retention Basis | Expected Retention Period |
|--------------|-----------------|--------------------------|
| | | |

All other data has been deleted as described above. The retained data will be deleted
at the end of the legally required retention period, and we will confirm at that time.

CONFIRMATION
[Organisation] confirms that, to the best of its knowledge and technical capability, all
personal data processed under the above Data Processing Agreement has been [returned /
transferred / deleted] as described, except for any retained data identified above.

If you have any questions or require further information, please contact:
[DPO Name] | privacy@[domain]

[Organisation Legal Name]
[Date]
```

---

## 4. Return, Transfer and Disposal Policy (Customer-Facing)

The following policy statement is made available to customers on request and may be included in or appended to processor agreements.

```
[ORGANISATION] — PII RETURN, TRANSFER AND DISPOSAL POLICY
Version: 1.0 | Effective: [Date]

SCOPE
This policy applies to all personal data processed by [Organisation] on behalf
of customer controllers under a Data Processing Agreement.

OPTIONS AT END OF SERVICE
Upon termination or expiry of services, or upon a customer's written request,
[Organisation] will, at the customer's choice:

1. RETURN — provide a complete, structured extract of all customer personal data
   in JSON or CSV format (or another agreed format) via secure encrypted transfer.

2. TRANSFER — transfer the customer's personal data to a new processor designated
   by the customer, via a mutually agreed secure transfer mechanism.

3. DISPOSE — securely delete all customer personal data from all [Organisation]
   primary systems, with backup deletion scheduled to the next backup cycle.

TIMELINE
[Organisation] will complete the chosen action and issue written confirmation within
30 days of receiving the customer's written instruction. Primary system deletion
or return is typically completed within 10 business days.

RESIDUAL RETENTION
Where [Organisation] is required by law to retain specific records, these will be
identified in the written confirmation, with the legal basis and expected retention period.

BACKUP DATA
Personal data in backups is deleted on the next scheduled backup overwrite following
the confirmed action. The expected date is communicated in the written confirmation.

CONFIRMATION
[Organisation] provides a written Disposal/Return Confirmation to the customer upon
completion, specifying the systems covered, the action taken, and the date.

Contact for end-of-service requests: privacy@[domain]
```

---

## 5. Processor Transmission Log

Records PII transmissions made on behalf of customers to third parties. Maintained by IT Security Team. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Log ID | Text | Unique reference (e.g., PTRANS-2026-001) |
| Date / Time | DateTime | Date and time of transmission |
| Customer | Text | Customer controller on whose behalf the transmission was made |
| Recipient | Text | Name of the receiving party |
| Recipient Type | Enum | Customer / Sub-processor / Regulatory Authority / Other |
| PII Categories | Text | Categories of PII transmitted |
| Classification | Enum | CONFIDENTIAL / RESTRICTED |
| Transmission Method | Enum | SFTP / HTTPS API / Encrypted Email / Portal / Other |
| Encryption Confirmed | Boolean | Yes / No |
| TLS Version (if applicable) | Text | TLS 1.2 / TLS 1.3 / Other |
| Delivery Confirmed | Boolean | Yes / No |
| Delivery Reference | Text | Log entry, confirmation email, or signed receipt |
| Purpose | Text | Why the transmission occurred |
| Notes | Text | Exceptions, failed deliveries |

---

<!-- QA_VERIFIED: [Date] -->

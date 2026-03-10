<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.4.2-4-UG:privacy:UG:a.2.4.2-4 -->
**PRIV-IMP-A.2.4.2-4-UG — Processor Lifecycle Controls — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Processor Lifecycle Controls — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.2.4.2-4-UG |
| **Related Policy** | PRIV-POL-A.2.4.2-4 (Processor Lifecycle Controls) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.2.4.2-4 (Processor Lifecycle Controls — the governing policy)
- PRIV-IMP-A.2.4.2-4-TG (Processor Lifecycle Controls — Technical Guide)
- PRIV-POL-A.2.2.2-7 (Processor Agreements — end-of-service obligations are contractual commitments)

---

## Purpose of This Guide

This guide explains **how to implement** the processor lifecycle controls of PRIV-POL-A.2.4.2-4 — specifically, how to manage temporary files containing customer PII, how to execute end-of-service PII return, transfer, or disposal, and how to confirm transmission security for customer PII.

**Who this guide is for**: DPO, IT Security Team / CISO, Customer Success.

**Processor-only**: This guide applies to processing activities where [Organisation] acts as PII Processor on behalf of customer controllers.

---

## Part 1 — Temporary Files from Customer PII Processing (A.2.4.2)

### 1.1 Identifying Temporary Files in Processor Contexts

When [Organisation] processes PII on behalf of customers, temporary files are generated as a byproduct of the processing operations. Common examples in processor contexts:

- **Processing cache files**: Intermediate results held in memory or on disk during batch processing runs
- **Staging tables**: Database staging areas used during data imports, transformations, or exports
- **Export files**: Files generated when producing a deliverable for the customer (e.g., a data extract or report)
- **Error/exception logs**: System logs that may capture PII from processing errors or stack traces
- **Debugging snapshots**: Development or support captures containing customer PII

These files are created incidentally and are not part of the customer's primary data store — but they contain customer PII and must be treated accordingly.

### 1.2 Temporary File Controls in Practice

The IT Security Team is responsible for confirming that automated disposal mechanisms are in place for each temporary file type:

- **Processing cache and staging files**: Purged within 48 hours of processing completion — automated post-processing cleanup jobs are the preferred implementation
- **Export files**: Deleted within 72 hours of confirmed delivery to the customer — the delivery confirmation triggers the deletion job
- **Error/exception logs containing PII**: Log rotation with automatic deletion at 30-day retention, or log scrubbing to remove PII before the 30-day mark
- **Debugging snapshots**: Must be deleted immediately after the debugging session — IT Security Team confirms deletion; no PII debugging snapshots are retained beyond the active investigation

Manual deletion processes are acceptable as a fallback but must be documented and scheduled — an unmonitored manual process is not adequate.

---

## Part 2 — End-of-Service PII Handling (A.2.4.3)

### 2.1 Triggering End-of-Service PII Handling

End-of-service PII handling is triggered by:

- **Contract expiry**: The service agreement reaches its end date
- **Customer termination**: The customer gives notice of contract termination
- **Customer-initiated data deletion**: The customer requests deletion of their data within an active contract (e.g., a specific data set is no longer needed)

Customer Success must notify the DPO and IT Security Team within 1 business day of any of these triggers so that the end-of-service process can be initiated promptly.

### 2.2 Obtaining the Customer's Instruction

Before taking any action, [Organisation] must obtain a written instruction from the customer specifying which option they want:

**Option A — Return**: The customer wants their PII returned to them in a specified format
**Option B — Transfer**: The customer wants their PII transferred to a new provider they are migrating to
**Option C — Disposal**: The customer wants [Organisation] to securely delete all their PII

**How to obtain the instruction**:

1. Customer Success contacts the customer's data protection or technical contact within 5 business days of the trigger
2. The customer is presented with the three options and a description of what each entails (format, timeline, confirmation)
3. The customer's instruction is documented in writing (email confirmation or signed request)
4. If the customer does not respond within 15 business days, Customer Success escalates to the DPO; the processor agreement default applies (typically disposal)

### 2.3 Executing Return (Option A)

1. IT Security Team generates a complete extract of all the customer's PII from all [Organisation] processing systems
2. Format is agreed with the customer — structured data (JSON, CSV) is the default; other formats by agreement
3. The extract is encrypted for transmission (AES-256 or equivalent) and transferred via a secure channel (SFTP, secure portal, or encrypted attachment with key sent separately)
4. Delivery is confirmed — customer acknowledges receipt
5. [Organisation] then deletes its copies of the PII (all systems + backup schedule) following confirmed delivery — confirmation is provided to the customer

### 2.4 Executing Transfer (Option B)

1. Customer identifies the receiving processor and provides their contact and technical details
2. [Organisation] and the receiving processor agree a secure transfer mechanism
3. Transfer is executed with full encryption; delivery is confirmed with the receiving processor
4. [Organisation] then deletes its copies following confirmed transfer
5. Written confirmation of transfer and deletion is provided to the customer

### 2.5 Executing Disposal (Option C)

1. IT Security Team executes deletion of all customer PII in primary systems
2. Deletion scope is confirmed — all systems where the customer's PII is stored are identified and cleared
3. Backup deletion is scheduled (natural overwrite cycle or out-of-cycle deletion depending on the processor agreement and customer's requirement); the expected timeline is confirmed to the customer
4. A written Disposal Confirmation is issued to the customer (see TG for template) within the period agreed in the processor agreement (typically within 30 days of service end)

### 2.6 Residual Legal Retention

In some cases, [Organisation] may be required by law to retain certain records even after the service ends (e.g., financial records, tax records, audit logs). Where this applies:

1. The DPO identifies the scope of legally required retention with Legal/Compliance input
2. The minimum necessary scope is retained — all other PII is deleted
3. The customer is informed in the Disposal Confirmation of any PII that must be retained, the legal basis, and the expected retention period
4. At the end of the legally required retention period, the remaining PII is deleted with confirmation

---

## Part 3 — PII Transmission Security (A.2.4.4)

### 3.1 Transmission Security Requirements

All PII transmitted over networks on behalf of customers must be encrypted. The IT Security Team is responsible for maintaining encryption configuration:

- **API connections**: TLS 1.2 minimum (TLS 1.3 preferred) for all customer API integrations
- **Web interfaces**: HTTPS enforced (HSTS enabled) for all web-accessible customer data
- **File transfers to customers**: SFTP or equivalent for structured data deliveries; password-protected encrypted files for email delivery (password communicated separately)
- **Internal service-to-service communication**: TLS for all internal services handling customer PII

Unencrypted transmission of customer PII over any network is prohibited.

### 3.2 Confirming Delivery for Sensitive Transmissions

For RESTRICTED (special category) customer PII transmitted to third parties:

- SFTP/portal: server-side delivery log confirms receipt
- API: HTTP 200/201 response logged
- Email with encrypted attachment: delivery receipt or explicit customer acknowledgment
- Physical media: signed delivery confirmation

All RESTRICTED transmission confirmations are recorded in the Processor Transmission Log (see TG).

---

## Evidence Checklist

- [ ] Temporary file disposal configuration — automated purge mechanisms in place and documented for each file type
- [ ] End-of-service disposal log — all customer contracts with return/transfer/disposal outcome recorded
- [ ] Disposal Confirmation records — written confirmations sent to customers within contracted timeframe
- [ ] Customer instruction records — written instructions obtained before end-of-service action taken
- [ ] Backup deletion schedule — approach and timeline documented per customer
- [ ] Legal retention residuals — documented where [Organisation] retained PII under legal obligation
- [ ] TLS configuration evidence — encryption in transit confirmed for all customer PII systems
- [ ] Return/disposal policy available to customers — confirmed accessible on request

---

<!-- QA_VERIFIED: [Date] -->

# ISMS-POL-A.8.10-S2.1
## Information Deletion - Retention & Deletion Triggers

**Document ID**: ISMS-POL-A.8.10-S2.1
**Title**: Information Deletion - Retention & Deletion Triggers  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Data Protection Officer / Information Security Manager | Initial retention and deletion trigger requirements |

**Review Cycle**: Annually (or upon significant regulatory changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Legal Review: Data Protection Officer (DPO) / Legal Counsel
- Business Review: Data Owners / Department Heads

**Distribution**: Data owners, IT operations, legal team, DPO, records management  
**Related Documents**: ISMS-IMP-A.8.10.1 (Retention & Deletion Assessment), ISMS-POL-A.8.10-S2.3 (Verification Requirements)

---

## 2.1.1 Purpose and Scope

This section establishes **mandatory requirements** for defining data retention periods and deletion triggers. These requirements ensure compliance with data minimization principles (GDPR Article 5, Swiss FADP) and enable timely deletion when retention purposes no longer apply.

**In Scope**: Retention period definitions, deletion trigger events, legal hold procedures, automated deletion requirements  
**Primary Stakeholders**: Data Protection Officer, Data Owners, Records Management, Legal  
**Implementation Evidence**: ISMS-IMP-A.8.10.1 (Retention & Deletion Triggers Assessment)

**Key Principle**: "Data shall not be kept in a form which permits identification of data subjects for longer than is necessary for the purposes for which the personal data are processed." — GDPR Article 5(1)(e)

---

## 2.1.2 Data Category Classification

### 2.1.2.1 Classification Requirement

Organizations **SHALL**:

- **Classify all data into defined categories** with documented retention requirements, including:
  - Personal data (data subject to GDPR/FADP rights)
  - Financial and accounting records
  - Contractual and legal documents
  - Operational and business records
  - Technical and system logs
  - Backup and archive data
  - Temporary and working data
- Assign each data category a designated **Data Owner** responsible for retention decisions
- Document the **business or legal purpose** justifying each retention period
- Review data classifications annually and when business processes change

### 2.1.2.2 Personal Data Special Requirements

For personal data subject to GDPR/Swiss FADP, organizations **SHALL**:

- Identify **lawful basis** for processing (GDPR Article 6)
- Document **specific purpose** for which data is collected
- Set retention period **tied directly to purpose** (not arbitrary "forever")
- Consider **data subject rights** when setting retention (right to erasure, portability)
- Flag **special category data** (GDPR Article 9) for enhanced deletion controls

**Cargo Cult Warning**: "We keep everything for 7 years because someone said that once" is not a retention policy. Document the actual legal or business requirement.

---

## 2.1.3 Retention Period Requirements

### 2.1.3.1 Standard Retention Periods

Organizations **SHALL** define retention periods considering:

| Factor | Requirement |
|--------|-------------|
| **Legal/Regulatory Minimum** | Comply with mandatory retention laws (tax, employment, financial) |
| **Statute of Limitations** | Consider potential legal claims (contract disputes, liability) |
| **Business Need** | Justify operational necessity (historical analysis, warranty support) |
| **Data Minimization** | Delete as soon as purpose no longer applies |

**Retention Period Documentation SHALL Include**:
- Data category name and description
- Retention period (in years, months, or event-based)
- Legal/business justification
- Responsible data owner
- Deletion trigger events
- Exceptions and special cases

### 2.1.3.2 Common Retention Periods (Informational Guidance)

**Note**: These are common industry practices. Organizations **MUST** verify compliance with applicable laws in their jurisdiction.

| Data Category | Typical Retention | Common Legal Basis |
|---------------|-------------------|-------------------|
| **Financial Records (Tax)** | 7-10 years | Tax authority requirements (varies by country) |
| **Employment Records** | 10 years after termination | Employment law, discrimination claims |
| **Contracts (Active)** | Duration + statute of limitations | Contract law (typically 6-10 years) |
| **Contracts (Expired)** | 6-10 years after expiry | Statute of limitations for breach claims |
| **Customer Personal Data** | Duration of relationship + 1-3 years | Legitimate interest, contract performance |
| **Marketing Consent** | Until consent withdrawn + 30 days | GDPR Article 7 (consent) |
| **System Logs (Security)** | 6-12 months | Security monitoring, incident investigation |
| **System Logs (Audit)** | 1-7 years | Compliance requirements (ISO 27001, PCI-DSS) |
| **Email (Business)** | 3-7 years | Business records, legal discovery |
| **Email (Personal/Transient)** | 30-90 days | Operational necessity only |
| **Backups** | Per backup schedule (see §2.1.5) | Disaster recovery, business continuity |

**Feynman Principle**: If you can't explain **why** you retain data for a specific period, you don't understand your retention policy. Fix that first.

### 2.1.3.3 Event-Based Retention

For data where retention is tied to events rather than fixed periods, organizations **SHALL**:

- Define the **triggering event** clearly (e.g., "contract termination," "customer account closure," "employee departure")
- Specify retention period **after the event** (e.g., "3 years after contract expiry")
- Implement **event tracking** to trigger deletion workflows
- Document exceptions where event-based retention doesn't apply

**Example**: Customer contract data retained for "contract duration + 6 years" to cover statute of limitations. Deletion trigger = 6 years after contract end date.

---

## 2.1.4 Deletion Trigger Events

### 2.1.4.1 Automatic Deletion Triggers

Organizations **SHALL** implement deletion triggers for:

| Trigger Event | Description | Action Required |
|---------------|-------------|-----------------|
| **Retention Period Expiry** | Data reaches end of defined retention period | Automatic deletion unless legal hold active |
| **Purpose Fulfillment** | Data processing purpose no longer applies | Evaluate for immediate deletion |
| **Consent Withdrawal** | Data subject withdraws consent (GDPR Article 7(3)) | Delete within 30 days unless other lawful basis |
| **Contract Termination** | Business relationship ends | Delete per retention schedule (typically retention period starts) |
| **Employee Termination** | Employment ends | Delete personal data per retention schedule |
| **Service Decommissioning** | System/service retired | Delete all data or migrate per retention rules |

### 2.1.4.2 Data Subject Deletion Requests

For GDPR Article 17 "Right to Erasure" requests, organizations **SHALL**:

- Provide **accessible mechanism** for data subjects to submit deletion requests
- **Acknowledge receipt** within 5 business days
- **Complete deletion within 30 days** of request (GDPR Article 12(3))
- **Extend deadline** only if request is complex (inform data subject, max 60 days total)
- **Verify identity** of requester before deletion (prevent malicious deletion)
- **Document all steps** taken to fulfill or deny request

**Valid Reasons to DENY Deletion Request** (GDPR Article 17(3)):
- Legal obligation requires retention (e.g., tax records)
- Exercise or defense of legal claims (e.g., ongoing litigation)
- Compliance with legal obligation (e.g., regulatory investigation)
- Public interest or official authority tasks
- Archiving in public interest, scientific/historical research (with safeguards)

Organizations **SHALL** document reason for denial and inform data subject of their right to complain to supervisory authority.

### 2.1.4.3 Business-Initiated Deletion

Organizations **SHOULD** proactively delete data when:

- **No longer needed**: Regular review identifies obsolete data
- **Quality issues**: Data is inaccurate and cannot be corrected
- **Duplicate data**: Redundant copies with no business justification
- **Test/development data**: After project completion
- **Temporary data**: Purpose-limited data (e.g., session data, cache)

**Best Practice**: Implement quarterly data review cycles where data owners evaluate data holdings for deletion candidates.

---

## 2.1.5 Backup and Archive Retention

### 2.1.5.1 Backup Retention vs. Active Data Retention

Organizations **SHALL** recognize that backups create a **retention paradox**:

- Active data may be deleted per retention schedule
- Backups containing that data may persist longer for disaster recovery
- Data subject deletion requests apply to backups (GDPR recital 65)

**Required Approach**:
- Define **backup retention period** separately from active data retention
- Document **maximum backup retention** (e.g., 90 days for operational backups, 7 years for archival)
- Implement **backup deletion schedules** aligned with retention policy
- For data subject deletion requests:
  - Delete from active systems immediately
  - Delete from backups on **next backup rotation cycle** (acceptable under GDPR if deletion is technically infeasible before rotation)
  - Document backup deletion timeline and communicate to data subjects

### 2.1.5.2 Backup Deletion Requirements

Organizations **SHALL**:

- **Automate backup deletion** at end of retention period
- **Verify backup deletion** through backup system reports
- **Secure erase backup media** when decommissioned (see ISMS-POL-A.8.10-S2.2)
- **Encrypt backups** so that deletion of encryption keys renders data irretrievable (cryptographic erasure)

### 2.1.5.3 Archive vs. Backup Distinction

Organizations **SHALL** differentiate:

| Type | Purpose | Retention | Deletion |
|------|---------|-----------|----------|
| **Backup** | Disaster recovery, short-term restoration | Days to months | Automatic rotation |
| **Archive** | Long-term preservation, compliance | Years to decades | Defined retention period |

**Archives are subject to the same retention and deletion rules as active data.** Organizations **MUST NOT** use "archive" as an excuse to retain data indefinitely without justification.

---

## 2.1.6 Legal Hold Procedures

### 2.1.6.1 Legal Hold Definition

A **legal hold** (litigation hold, preservation order) is a **suspension of normal deletion** to preserve data relevant to:
- Active or anticipated litigation
- Regulatory investigations
- Internal investigations (fraud, misconduct)
- eDiscovery requests

**Legal holds OVERRIDE normal retention and deletion schedules.**

### 2.1.6.2 Legal Hold Requirements

Organizations **SHALL**:

- **Designate authority** for issuing legal holds (typically Legal Counsel or DPO)
- **Document legal hold scope**:
  - Specific data categories affected
  - Systems and locations holding relevant data
  - Custodians (people whose data is on hold)
  - Reason for hold (litigation case number, investigation ID)
  - Start date and anticipated duration
- **Notify IT and data custodians** of legal hold within 2 business days of issuance
- **Implement technical controls** to prevent deletion:
  - Disable automated deletion for affected data
  - Flag data in deletion systems as "hold"
  - Restrict manual deletion permissions
  - Monitor for hold violations
- **Release legal hold** only upon authorization from Legal Counsel
- **Resume normal deletion** within 30 days of hold release

### 2.1.6.3 Legal Hold Conflicts with Data Subject Rights

When legal hold conflicts with GDPR deletion request, organizations **SHALL**:

- **Inform data subject** that deletion is suspended due to legal obligation (GDPR Article 17(3)(b))
- **Document legal basis** for denying deletion
- **Limit hold scope** to minimum necessary data
- **Resume deletion** as soon as legal hold is lifted

**Balance**: Legal holds are legitimate, but must be specific and time-bound. "We might get sued someday" is not a valid perpetual legal hold.

---

## 2.1.7 Automated Deletion Requirements

### 2.1.7.1 Automation Mandate

Organizations **SHALL** implement automated deletion where technically feasible to:
- Reduce human error and forgotten deletions
- Ensure consistent application of retention policies
- Demonstrate compliance through system-generated evidence
- Scale deletion across large data volumes

**Manual deletion is acceptable only where**:
- Automated deletion is technically infeasible
- Data volume is small (<100 records/year)
- Data sensitivity requires human review before deletion

### 2.1.7.2 Automated Deletion System Requirements

Automated deletion systems **SHALL**:

- **Trigger deletion** based on defined retention periods and events
- **Check for legal holds** before executing deletion
- **Log all deletion actions** with:
  - Timestamp of deletion
  - Data category/record identifier
  - Retention period expired
  - User/system performing deletion
  - Result (success, failure, skipped due to hold)
- **Generate deletion reports** for data owners and DPO
- **Alert on failures** when deletion cannot be completed
- **Support manual override** for emergency deletions (with approval workflow)

### 2.1.7.3 Deletion Scheduling

Organizations **SHOULD** schedule automated deletions:

- **Daily**: High-volume, short-retention data (session data, temporary files)
- **Weekly**: Standard operational data
- **Monthly**: Low-volume, long-retention data
- **Quarterly**: Archive and backup evaluations

**Off-hours scheduling** is recommended to minimize performance impact on production systems.

---

## 2.1.8 Third-Party and Cloud Data Triggers

### 2.1.8.1 Third-Party Deletion Coordination

For data processed by third parties (SaaS, cloud providers, processors), organizations **SHALL**:

- **Include deletion triggers** in contracts:
  - Automatic deletion at end of retention period
  - Deletion within 30 days of contract termination
  - Deletion upon customer request (for data subject requests)
- **Verify third-party deletion** through:
  - Deletion certificates
  - Audit reports (SOC 2, ISO 27001)
  - API-based deletion confirmations
- **Document deletion timelines** from third parties (may differ from internal timelines)

**See ISMS-POL-A.8.10-S2.4 for detailed third-party deletion requirements.**

### 2.1.8.2 Multi-Cloud and Hybrid Environments

Organizations **SHALL** account for data replication across:
- Multiple cloud regions
- Backup and disaster recovery sites
- Edge caching and CDN locations
- Development/test environments

**Deletion triggers must propagate** to all locations where data exists.

---

## 2.1.9 Deletion Trigger Metrics

Organizations **SHALL** measure deletion trigger effectiveness through:

| Metric | Target | Purpose |
|--------|--------|---------|
| **Retention period compliance rate** | >95% | Percentage of data deleted on schedule |
| **Data subject deletion request response time** | <30 days (GDPR) | Compliance with legal timelines |
| **Automated deletion success rate** | >99% | Reliability of deletion automation |
| **Legal hold accuracy** | 100% (no false deletions) | Prevent destruction of litigation-relevant data |
| **Overdue deletion backlog** | <5% of total data | Data past retention period not yet deleted |
| **Deletion failure rate** | <1% | Technical failures requiring intervention |

Metrics shall be reviewed **monthly** by Data Protection Officer and reported to CISO **quarterly**.

---

## 2.1.10 Retention Schedule Maintenance

### 2.1.10.1 Annual Review Requirement

Organizations **SHALL** review retention schedules **annually** to:
- Update for regulatory changes
- Remove obsolete data categories
- Add new data categories from business changes
- Validate retention periods still justified
- Update data owner assignments

### 2.1.10.2 Retention Schedule Change Management

Changes to retention schedules **SHALL**:
- Require **data owner approval**
- Include **legal/DPO review** for personal data changes
- Document **reason for change**
- Communicate to **affected stakeholders**
- Update **automated deletion systems** within 30 days

**Shortening retention periods**: Apply to all data (including existing data), trigger immediate deletion of data now past retention.

**Lengthening retention periods**: Document strong justification (new legal requirement, business necessity), avoid retroactive lengthening without clear legal basis.

---

## 2.1.11 Exceptions to Retention and Deletion Triggers

### 2.1.11.1 Valid Exceptions

Organizations **MAY** grant exceptions to standard retention/deletion for:
- **Legal/regulatory requirements** (mandatory longer retention)
- **Active legal matters** (litigation, investigations)
- **Archival preservation** (historical significance, public interest with appropriate safeguards)
- **Technical limitations** (deletion infeasible without disproportionate effort - GDPR recital 65)

### 2.1.11.2 Exception Approval Process

Exceptions **SHALL** require:
- Written request from data owner or department head
- Business/legal justification
- **DPO approval** for personal data exceptions
- **CISO approval** for information security exceptions
- **Legal counsel review** for compliance-related exceptions
- **Time-bound duration** (review annually)
- **Compensating controls** if deletion is deferred (enhanced access controls, encryption)

### 2.1.11.3 Exception Documentation

Organizations **SHALL** maintain exception register including:
- Data category affected
- Reason for exception
- Approver and approval date
- Exception expiry date
- Compensating controls applied
- Review date

**Exceptions are not permanent.** Review every 12 months for continued necessity.

---

## 2.1.12 Continuous Improvement

Organizations **SHALL**:
- Analyze **deletion failures** to identify systemic issues
- Review **data subject deletion requests** for patterns (frequent requests may indicate over-collection)
- Update retention schedules based on **regulatory changes** (GDPR guidance, data protection authority rulings)
- Conduct **annual retention policy training** for data owners
- Participate in **industry forums** on data retention best practices

---

## 2.1.13 Documentation Requirements

Organizations **SHALL** maintain:

- **Master retention schedule** (all data categories, retention periods, owners)
- **Deletion trigger procedures** (event definitions, workflows)
- **Legal hold register** (active holds, scope, responsible party)
- **Deletion logs** (evidence of deletions performed)
- **Exception register** (approved deviations from policy)
- **Data subject request log** (requests received, actions taken, timelines)

Documentation shall be **reviewed by DPO quarterly** and made available to data protection authorities upon request.

---

**END OF DOCUMENT**

*"The first principle is that you must not fool yourself about why you keep data—and you are the easiest person to fool."* — Feynman (paraphrased for data retention)
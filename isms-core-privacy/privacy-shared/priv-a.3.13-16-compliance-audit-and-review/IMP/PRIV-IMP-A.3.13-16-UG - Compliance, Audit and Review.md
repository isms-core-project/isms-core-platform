<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.13-16-UG:privacy:UG:a.3.13-16 -->
**PRIV-IMP-A.3.13-16-UG — Compliance, Audit and Review — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Compliance, Audit and Review — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.3.13-16-UG |
| **Related Policy** | PRIV-POL-A.3.13-16 (Compliance, Audit and Review) |
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

- PRIV-POL-A.3.13-16 (Compliance, Audit and Review — the governing policy)
- PRIV-IMP-A.3.13-16-TG (Compliance, Audit and Review — Technical Guide)
- PRIV-POL-00 (Privacy Regulatory Applicability Framework — source of regulatory obligations)
- PRIV-POL-01 (Privacy Governance and Decision-Making Framework)

---

## Purpose of This Guide

This guide explains **how to implement** the compliance, audit, and review requirements of PRIV-POL-A.3.13-16. It covers how to build and maintain the Privacy Legal Requirements Register, how to protect PII processing records, how to commission and conduct independent PIMS reviews, and how to run an ongoing compliance review programme.

**Who this guide is for**: DPO, PIMS Internal Auditor, Legal/Compliance, CISO, Executive Management.

---

## Part 1 — Privacy Legal Requirements Register (A.3.13)

### 1.1 Building the PLRR

The Privacy Legal Requirements Register (PLRR) is a structured document listing every legal, regulatory, and contractual obligation relevant to the organisation's PII processing activities, together with the controls or procedures that address each obligation.

**Initial build process**:
1. Start with the Tier 1 and Tier 2 regulations identified in PRIV-POL-00 (GDPR, CH FADP, ISO 27701:2025 — mandatory; UK GDPR, LGPD, PIPL — conditional where applicable)
2. For each regulation: list the specific articles or requirements that impose obligations on the organisation — cross-reference the PRIV-POL articles cited in each control group POL
3. For each material contract involving PII (processor agreements, joint controller arrangements, customer agreements with privacy provisions): list the contractual privacy obligations
4. For each requirement: identify the PRIV-POL, PRIV-IMP, or operational procedure that addresses it
5. Add the current compliance status and a review date
6. See PRIV-IMP-A.3.13-16-TG for the PLRR schema

### 1.2 Maintaining the PLRR

The PLRR must be reviewed at minimum annually and on the following triggers:

| Trigger | Action |
|---------|--------|
| New privacy legislation enacted or existing legislation materially amended | Add new requirements; update affected existing entries; update compliance approach |
| New DPA guidance or enforcement decision materially clarifying an obligation | Update the affected requirement entry; note the guidance reference |
| New processing activity or new contract with privacy obligations | Add entries for new obligations; cross-reference to processing activity |
| Existing regulation explicitly no longer applicable (e.g., market exit) | Mark as Not Applicable with rationale; retain in PLRR |

**Annual PLRR review process**:
1. DPO reviews each entry: is the regulatory citation still current? Is the compliance approach still in place and effective?
2. Legal/Compliance confirms no regulatory changes in the past 12 months that require updates
3. DPO updates the review date on all entries reviewed
4. Material gaps identified are escalated as compliance findings

### 1.3 PLRR Governance

The PLRR is a CONFIDENTIAL document, maintained by the DPO. It is provided to internal auditors and certification bodies on request. It is not published externally.

At the annual PIMS management review (ISO 27701:2025 Clause 9.3), the DPO presents a summary of PLRR currency and any material gaps to Executive Management.

---

## Part 2 — Protecting PII Processing Records (A.3.14)

### 2.1 What Records Must Be Protected

The mandatory PII processing records requiring formal protection are listed in PRIV-POL-A.3.13-16 (Records table). These include: RoPA, consent records, DPIAs, DPO appointment records, supervisory authority notifications, data subject rights response records, processor agreements, Privacy Breach Register, training records, audit reports, and management review records.

### 2.2 Access Controls for Records

Each record type must have documented access controls:

| Access Level | Who Has Access |
|-------------|----------------|
| RESTRICTED records (consent, supervisory notifications, breach register) | DPO + Legal/Compliance + designated deputies only |
| CONFIDENTIAL records (RoPA, DPIAs, audit reports, processor agreements) | DPO + CISO + relevant role + internal auditors on assignment |
| INTERNAL records (DPO appointment, training records) | HR + DPO + line management |

Access to records is reviewed annually as part of the access rights review (PRIV-POL-A.3.8-10).

### 2.3 Audit Trail for High-Significance Records

Records with regulatory significance (RoPA, consent records, DPIA, breach register, supervisory authority notifications) must be stored in systems that provide:
- Modification logging: who changed what, when
- Version history: prior versions retained for the full retention period
- Deletion protection: records cannot be deleted without DPO authorisation

If your document management system does not support these features natively, implement compensating controls:
- Version-named files in access-controlled folder (e.g., `ROPA_v1.0_20260101.xlsx`) with access log
- Change log document accompanying each record
- Periodic backup to write-protected archive

### 2.4 Backup and Recovery

All mandatory PII processing records are included in the organisation's backup programme. DPO confirms with IT Security Team at minimum annually that:
- All mandatory records are covered by backup
- Recovery of each record type has been tested within the last 12 months
- Backup retention meets or exceeds the records retention requirement

---

## Part 3 — Independent Review of PIMS (A.3.15)

### 3.1 Planning the Independent Review

The DPO commissions the annual independent PIMS review. The review may be:
- An internal PIMS audit conducted by the PIMS Internal Auditor (who must be independent of the functions being audited)
- An external third-party privacy audit
- The Stage 2 or surveillance audit under ISO/IEC 27701:2025 certification

**At least 6 weeks before the review**:
1. DPO defines the review scope (which control groups, which processing activities, which risk areas)
2. Reviewer's independence is confirmed — document that the reviewer has no operational involvement in the areas under review
3. Review schedule is communicated to DPO, CISO, and relevant process owners
4. Required evidence and documentation is prepared and made available to the reviewer

### 3.2 Conducting the Review

The reviewer examines the PIMS against the defined scope, using as minimum:

| Review Area | What to Examine |
|-------------|----------------|
| Documentation | PIMS policy register — current, complete, approved |
| Role assignments | Privacy Roles Register — all mandatory roles assigned, DPO conflict check current |
| Records | Mandatory records present, access controlled, retention observed |
| Technical controls | Access controls, encryption, logging in PII processing environments |
| Incident management | PIRP current, breach register up to date, notifications on file |
| Compliance status | PLRR currency, open non-conformities from previous review |
| Data subject rights | DSR process in place, response records available |
| Training | Training completion records — all PII-handling personnel covered |

### 3.3 Review Findings and Response

After the review:
1. Reviewer issues a formal review report: findings, non-conformities (major and minor), observations, and recommendations
2. DPO reviews the report and prepares a formal management response: accepting, challenging, or noting each finding
3. DPO prepares a remediation plan for all accepted non-conformities: action, owner, target date
4. Review findings and remediation plan are presented to Executive Management
5. Remediation is tracked to closure; DPO reports progress at the next management review

**Non-conformity classification**:
- **Major**: PIMS requirement not implemented; significant compliance gap with regulatory obligation
- **Minor**: PIMS requirement partially implemented; evidence incomplete but controls broadly in place
- **Observation / opportunity for improvement**: Not a non-conformity but a recommendation

---

## Part 4 — Ongoing Compliance Review (A.3.16)

### 4.1 Annual PIMS Compliance Self-Assessment

Each year, the DPO conducts (or commissions) a self-assessment of PIMS compliance across all 21 control group policies. This is distinct from (and less formal than) the independent review — it is an internal monitoring activity.

**Process**:
1. DPO works through each control group POL and asks: "Is the organisation implementing this policy?"
2. Evidence is checked (can we produce the required evidence items listed in each POL's Evidence Requirements section?)
3. Non-conformities and gaps are documented
4. Remediation actions are assigned with target dates
5. Results are summarised in the compliance review report (see PRIV-IMP-A.3.13-16-TG)

The self-assessment is a DPO activity. It provides the baseline for the independent review but does not satisfy the independence requirement of A.3.15.

### 4.2 Quarterly RoPA Accuracy Review

The RoPA must be reviewed quarterly for accuracy. DPO circulates the current RoPA to Data Owners and Privacy Champions and asks:

- Are any processing activities listed that have been discontinued?
- Are any new processing activities not yet listed?
- Have the purposes, legal bases, categories, or retention periods changed for any listed activity?

Updates to the RoPA are made within 10 business days of confirmed changes. The review is documented (date, attendees, changes made, sign-off).

### 4.3 Processor Agreement Inventory Review

Annually, DPO reviews the Transfer Agreement Register to confirm all active processor relationships have current, signed agreements. Findings:

| Finding | Action |
|---------|--------|
| Active processor without a signed agreement | Obtain agreement immediately; suspend PII transfer if agreement cannot be obtained within 10 business days |
| Agreement expired or not reviewed within 12 months | Schedule review/renewal |
| Processor agreement materially outdated (new processing, new legal requirements) | Flag for amendment |

---

## Evidence Checklist

- [ ] Privacy Legal Requirements Register (PLRR) — current, last reviewed within 12 months
- [ ] Mandatory PII processing records present and current (RoPA, consent, DPIAs, agreements, etc.)
- [ ] Records access controls documented and reviewed
- [ ] Independent PIMS review report — last 12 months, reviewer independence documented
- [ ] Remediation tracking from independent review — open actions with target dates
- [ ] Annual PIMS compliance self-assessment report
- [ ] Quarterly RoPA review records
- [ ] Annual processor agreement inventory review

---

<!-- QA_VERIFIED: [Date] -->

<!-- ISMS-CORE:IMP:CLD-IMP-A.8-TG:cloud:TG:a.8 -->
**CLD-IMP-A.8-TG — Openness, Transparency and Notice — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Openness, Transparency and Notice — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.8-TG |
| **Related Policy** | CLD-POL-A.8 (Openness, Transparency and Notice) |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | CISO / Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial technical guide for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon sub-processor or service model changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.8 (Openness, Transparency and Notice — the governing policy)
- CLD-IMP-A.8-UG (Openness, Transparency and Notice — User Guide)
- CLD-POL-A.11.12 (Sub-contracted PII processing)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for openness and transparency management. It covers:

- ISO 27018 Transparency Disclosure checklist (what must be published)
- Sub-Processor Register schema
- Controller Advance Notice log schema
- Service documentation update process

**Audience**: CISO, DPO, Legal/Compliance, Cloud Engineering.

---

## 1. ISO 27018 Transparency Disclosure Checklist

Completed by the DPO annually and following any material change to processing practices. Confirms that all required public disclosures are in place, current, and accessible.

| Disclosure Item | Required By | Location | Current Version | Last Updated | Status |
|----------------|------------|----------|----------------|-------------|--------|
| Sub-Processor List | CLD-POL-A.8 / GDPR Art. 28(2) | Trust portal (subscriber-accessible) | v___ | ___ | [ ] Current / [ ] Requires Update |
| Privacy Policy (processor-facing) | GDPR Art. 13–14 / FADP | [Organisation] website | v___ | ___ | [ ] Current / [ ] Requires Update |
| ISO 27018 Controls Summary | CLD-POL-A.8 / ISO 27018:2025 | Trust portal | v___ | ___ | [ ] Current / [ ] Requires Update |
| Geographic PII Processing Locations | CLD-POL-A.12 | Trust portal | v___ | ___ | [ ] Current / [ ] Requires Update |
| DPO Contact Details | GDPR Art. 37(7) | Website + DPA template | — | ___ | [ ] Current / [ ] Requires Update |
| Data Processing Agreement (DPA) template | GDPR Art. 28(3) | Trust portal / on request | v___ | ___ | [ ] Current / [ ] Requires Update |
| Certification or audit summary | ISO 27018:2025 | Trust portal (on request) | ___ | ___ | [ ] Current / [ ] Requires Update |

**DPO review completed**: _________________________ Date: _____________
**All items confirmed current**: [ ] Yes / [ ] No — items requiring update listed below

Items requiring update: _____________________________________________
Update target date: _____________

---

## 2. Sub-Processor Register Schema

Maintained by the DPO. Source of truth for all sub-processor disclosures. Access: DPO, Legal/Compliance, CISO. Classified RESTRICTED internally; Sub-Processor List (summary view) published externally.

| Field | Type | Description |
|-------|------|-------------|
| Sub-processor ID | Text | Unique reference (e.g., SP-001) |
| Legal Entity Name | Text | Full registered legal name |
| Trading Name (if different) | Text | Name used in service context |
| Services Provided | Text | Specific processing operations performed on [Organisation]'s behalf |
| PII Categories Accessed | Text | Categories of controller PII the sub-processor may access |
| Processing Location(s) | Text | Countries or regions where processing occurs |
| Data Centre Provider (if applicable) | Text | Hosting provider or facility name |
| Contract Reference | Text | Reference to the binding sub-processor agreement |
| Agreement Effective Date | Date | Date sub-processor agreement came into force |
| Agreement Expiry / Renewal Date | Date | Scheduled renewal or expiry date |
| GDPR Art. 28(4) Flow-Down Confirmed | Boolean | Yes / No — processor obligations mirrored in sub-processor agreement |
| Controller Consent Type | Enum | General authorisation / Specific consent |
| Controller Consent Date | Date | Date general/specific consent documented |
| Date Added to Register | Date | Date this sub-processor was onboarded |
| Last Security Assessment Date | Date | Date CISO last assessed sub-processor security posture |
| Status | Enum | Active / Pending onboarding / Being replaced / Terminated |
| Notes | Text | Pending contract renewals, jurisdiction concerns, restrictions |

---

## 3. Controller Advance Notice Log Schema

Maintained by the DPO. Records all advance notifications sent to PII controllers regarding sub-processor changes. Retention: 5 years.

| Field | Type | Description |
|-------|------|-------------|
| Notice ID | Text | Unique reference (e.g., SPN-2026-001) |
| Sub-processor Affected | Text | Sub-processor ID and name from Sub-Processor Register |
| Change Type | Enum | New engagement / Replacement / Scope change / Location change / Termination |
| Change Description | Text | Summary of the proposed change |
| Intended Change Date | Date | Date [Organisation] intends to implement the change |
| Notice Sent Date | Date | Date advance notice was dispatched |
| Notice Period (days) | Number | Number of days between notice sent and intended change date |
| Notification Channel | Enum | Email to DPO contact / Trust portal announcement / Direct letter |
| Controllers Notified | Text | List of controller names notified (or "All" where global notice published) |
| Objection Period Expiry | Date | Date by which controllers must object (= notice sent date + 30 days or service agreement period) |
| Objections Received | Boolean | Yes / No |
| Objection Details | Text | Controller name, grounds, and resolution (if Yes) |
| Change Implemented | Date | Date change was implemented |
| Sub-Processor Register Updated | Date | Date Sub-Processor Register was updated |
| Sub-Processor List Published | Date | Date updated public Sub-Processor List was published |
| Status | Enum | Notice sent / Objection in progress / Change implemented / Closed |

---

## 4. Service Documentation Update Process

Used by the DPO and Cloud Service Delivery to ensure public disclosures are updated correctly when processing practices change.

| Step | Responsible | Action |
|------|------------|--------|
| 1 | DPO | Identifies change requiring disclosure update (sub-processor, geographic location, new service, regulatory) |
| 2 | DPO + Legal/Compliance | Drafts updated disclosure content; confirms regulatory accuracy |
| 3 | CISO | Reviews technical accuracy of ISO 27018 controls content (if affected) |
| 4 | DPO | Obtains sign-off from Legal/Compliance and CISO |
| 5 | DPO | Schedules publication — at minimum 30 days prior to effective date for sub-processor changes; on or before effective date for other changes |
| 6 | Cloud Engineering / Web | Publishes updated disclosure to trust portal or website; archives previous version with effective date |
| 7 | DPO | Sends controller notification where required (see CLD-IMP-A.8-UG Part 2.3) |
| 8 | DPO | Updates Transparency Disclosure Checklist (Section 1); records review date |

### Privacy Notice Technical Fields and Versioning

All public-facing privacy and processing disclosure documents maintained by [Organisation] SHALL carry:

| Field | Description |
|-------|-------------|
| Document title | Identifies the document type |
| Version number | Incremented on each substantive change (e.g., v1.0, v1.1, v2.0) |
| Effective date | Date from which this version applies |
| Previous version reference | Link or reference to archived previous version |
| Change summary | Brief description of what changed in this version |
| DPO sign-off | Name of DPO who approved the published version |

Archived versions are retained for 5 years from the date the version was superseded, and are available to controllers on request.

---

<!-- QA_VERIFIED: [Date] -->

<!-- ISMS-CORE:IMP:AI-IMP-A.4.2-6-TG:ai:TG:a.4.2-6 -->
**AI-IMP-A.4.2-6-TG — AI System Resources — Technical Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI System Resources — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | AI-IMP-A.4.2-6-TG |
| **Related Policy** | AI-POL-A.4.2-6 (AI System Resources) |
| **Document Creator** | AI Governance Officer |
| **Document Owner** | AI Governance Officer |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | AI Governance Officer | Initial technical guide for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.4.2-6 (AI System Resources — governing policy)
- AI-IMP-A.4.2-6-UG (AI System Resources — User Guide)

---

## Purpose of This Guide

This guide provides the **full field schema for the AI System Resource Register** and supporting reference structures. The Register is the master record of all in-scope AI systems and their resources.

**Audience**: AI Governance Officer, IT/infrastructure, ML Engineers, AI System Owners.

---

## 1. AI System Resource Register — Full Schema

One register record per in-scope AI system. Fields marked **[M]** are mandatory; **[R]** recommended; **[C]** conditional.

---

### Block A — AI System Identification

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| System ID | Text | M | Unique identifier (e.g., AI-SYS-001) |
| System Name | Text | M | Human-readable system name |
| Current Version | Text | M | Version currently deployed in production |
| Previous Versions | Text | R | List of prior deployed versions still in retention period |
| Purpose Statement | Text | M | Clear statement of what the system does and for what purpose |
| AI System Type | Enum | M | Generative / Discriminative / Predictive / Recommendation / Classification / Clustering / Other |
| Output Type | Text | M | What the system produces (prediction, score, classification, generated text, image, ranking, decision, etc.) |
| Operational Status | Enum | M | Pre-deployment / Deployed-active / Deployed-limited / Suspended / Decommissioning / Decommissioned |
| AIMS In-Scope | Boolean | M | Yes — all records in this Register are in scope |
| Date Added to Register | Date | M | |
| Last Updated | Date | M | Date of most recent field update |

---

### Block B — Ownership and Governance

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| AI System Owner (Name) | Text | M | Named individual |
| AI System Owner (Role/Title) | Text | M | |
| AI System Owner (Contact) | Text | M | Email |
| AI Risk Owner (Name) | Text | M | Named individual |
| AI Risk Owner (Role/Title) | Text | M | |
| AI Risk Owner (Contact) | Text | M | Email |
| Business Unit | Text | M | Owning business unit / department |
| AISIA Document ID | Text | M | Reference to current AISIA record |
| AISIA Version | Text | M | Version of current approved AISIA |
| AISIA Status | Enum | M | Approved / Under review / Overdue / Not yet conducted |
| AISIA Approval Date | Date | M | Date of current AISIA approval |
| Next AISIA Review Date | Date | M | |
| Impact Classification | Enum | M | Low / Medium / High (from current AISIA) |
| EU AI Act Role | Enum | M | Provider / Deployer / Both / Not applicable |
| EU AI Act Risk Category | Enum | M | Unacceptable / High-risk / Limited-risk / Minimal-risk / GPAI / Not determined |

---

### Block C — Computing Resources

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Infrastructure Type | Enum | M | On-premises / Private cloud / Public cloud / Third-party hosted / Hybrid |
| Cloud Provider(s) | Text | C | If public cloud: provider name(s) and primary region(s) |
| Third-party AI platform | Text | C | If hosted by third party: platform name and vendor |
| Compute requirements | Text | R | Approximate (e.g., GPU-based / CPU-only / inference only) |
| Data storage location | Text | M | Where training data and operational data are stored; jurisdiction |
| Single-vendor dependency | Boolean | M | Yes / No — triggers supplier resilience assessment if Yes |
| Business continuity plan reference | Text | R | Reference to BCP/DRP entry for this AI system |

---

### Block D — Data Resources

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Training Dataset Name(s) | Text | M | One entry per dataset |
| Training Dataset Version(s) | Text | M | |
| Training Data Source Category | Enum | M | Internal / Licensed / Public / Synthetic / Combination |
| Training Data Record Reference | Text | M | Reference to full data record per AI-POL-A.7.2-6 |
| Training Data — Personal Data | Boolean | M | Does training data include personal data? |
| Training Data — Personal Data Legal Basis | Text | C | If Yes: GDPR Article 6 basis; Article 9 basis if special category |
| Operational Input Data Type | Text | M | What data is provided as input at inference time |
| Operational Input — Personal Data | Boolean | M | |
| Operational Input — Personal Data Legal Basis | Text | C | |
| DPIA Reference | Text | C | If DPIA conducted: document reference |
| Data Provenance Record Reference | Text | M | Reference to provenance record per AI-POL-A.7.2-6 |

---

### Block E — AI Tooling and Components

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Foundation Model / Pre-trained Model Used | Text | C | Name, provider, version — if applicable |
| Foundation Model API Endpoint | Text | C | API name/service (not credentials) |
| Third-party AI Component(s) | Text | C | Other AI components from third parties (name, provider, version) |
| MLOps Platform | Text | R | Training and deployment orchestration platform |
| Model Registry | Text | R | Where models are versioned and stored |
| Monitoring Tool | Text | M | Tool used for production monitoring |
| Logging Infrastructure | Text | M | Where logs are stored; retention period |
| Data Annotation Platform | Text | C | If annotated training data used |
| Development Language(s) | Text | R | Primary programming languages |
| Key Open-Source Libraries | Text | R | Critical dependencies (name, version, licence) |
| Vulnerability Management | Text | R | How CVEs in AI libraries are tracked and addressed |

---

### Block F — Human Resources and Competencies

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Number of Operational Users | Text | M | Approximate count of staff/operators using this system |
| Required Domain Competency | Text | M | Subject matter expertise required to validate AI outputs |
| Required AI/Technical Competency | Text | M | Understanding of AI system required to use responsibly |
| AIMS Policy Training Required | Text | M | Which AIMS policies operators must be trained on |
| Current Training Completion Rate | Text | R | % of current operators with completed training |
| Competency Gap (if any) | Text | R | Document gaps with remediation plan |

---

### Block G — Supplier Records (AI-POL-A.10.2-4 linkage)

*Complete for any AI supplier whose component is reflected in Block E.*

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Supplier Name | Text | C | |
| Component Provided | Text | C | |
| Supplier Assessment Status | Enum | C | Assessed / Assessment overdue / Pending / Not required |
| Supplier Assessment Date | Date | C | |
| Supplier Contract Reference | Text | C | Contract document reference |
| Incident Notification Obligation | Text | C | Agreed notification timeframe per contract |
| Change Notification Obligation | Text | C | Supplier's obligation to notify [Organisation] of material changes |
| Supplier Review Next Date | Date | C | |

---

## 2. AI System Inventory — Summary View

For management reporting, the AI Governance Officer maintains a summary view of the Register. Minimum fields for summary view:

| System ID | System Name | Owner | Classification | Status | AISIA Status | Next Review |
|-----------|-------------|-------|---------------|--------|-------------|------------|
| AI-SYS-001 | [Name] | [Owner] | Low/Med/High | Active | Approved | YYYY-MM-DD |
| AI-SYS-002 | | | | | | |

Systems with AISIA Status = Overdue shall be flagged in the summary and reported to the AI Governance Officer for immediate action.

---

## 3. New AI System Registration Checklist

Before a new AI system is added to the Register and cleared for deployment:

| Step | Required Action | Complete? |
|------|----------------|-----------|
| 1 | Assign System ID | ☐ |
| 2 | Confirm AI System Owner (named) | ☐ |
| 3 | Confirm AI Risk Owner (named) | ☐ |
| 4 | Complete Blocks A–G in Register | ☐ |
| 5 | AISIA initiated and approved | ☐ |
| 6 | Data records created per AI-POL-A.7.2-6 | ☐ |
| 7 | Supplier assessment completed (if third-party AI component used) | ☐ |
| 8 | User documentation prepared (AI-POL-A.8.2-5) | ☐ |
| 9 | User training completed | ☐ |
| 10 | Deployment gate approved by AI Governance Officer | ☐ |

---

<!-- QA_VERIFIED: [2026-04-15] -->

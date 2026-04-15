<!-- ISMS-CORE:IMP:AI-IMP-A.6.2-TG:ai:TG:a.6.2 -->
**AI-IMP-A.6.2-TG — AI System Lifecycle — Technical Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI System Lifecycle — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | AI-IMP-A.6.2-TG |
| **Related Policy** | AI-POL-A.6.2 (AI System Lifecycle) |
| **Document Creator** | AI Governance Officer / Chief Technology Officer |
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

- AI-POL-A.6.2 (AI System Lifecycle — governing policy)
- AI-IMP-A.6.2-UG (AI System Lifecycle — User Guide)

---

## Purpose of This Guide

This guide provides the **technical structures and schemas** for AI system lifecycle management — including the AI system specification template, operational monitoring schema, technical documentation structure, and the logging requirements specification.

**Audience**: ML Engineers, DevOps/MLOps engineers, AI System Owners, IT Operations.

---

## 1. AI System Specification Template (A.6.2.2)

Complete this template before development commences. Approved by AI Governance Officer.

---

```
AI SYSTEM SPECIFICATION
Document ID: SPEC-[System-ID]-v[X.X] | Date: [YYYY-MM-DD]
AI System Name: [Name]
Version Specified: [X.X (pre-development)]
Author: [AI System Owner]
Approved By: [AI Governance Officer] | Approval Date: [YYYY-MM-DD]

1. PURPOSE AND INTENDED USE
   System purpose: [What problem this solves; what function it performs]
   Intended use statement: [Clear, specific — who uses it, in what context, to what end]
   Intended users: [Role(s); competency requirements]
   Intended operational context: [Where deployed; conditions; environment]
   Output type and use: [What outputs are produced; how used; advisory vs. automated]
   
2. PERFORMANCE REQUIREMENTS
   Primary metric: [Metric name and minimum acceptable value]
   Secondary metrics: [List with thresholds]
   Fairness requirements: [Which demographic groups must be evaluated; parity requirements]
   Reliability requirements: [Uptime; latency; throughput]
   
3. CONSTRAINTS
   Out-of-scope uses: [Explicitly not covered]
   Prohibited uses: [Explicitly forbidden]
   Data constraints: [What data may / may not be used]
   Regulatory constraints: [Any regulatory requirements affecting design]
   
4. INTEGRATION REQUIREMENTS
   Input sources: [What systems or users provide input data]
   Output consumers: [What systems or users receive outputs]
   APIs / interfaces: [Key integration points]
   
5. RESPONSIBLE AI REQUIREMENTS
   Human oversight mechanism: [How and where human review is required]
   Explainability requirement: [Level required; mechanism to be implemented]
   Transparency to affected individuals: [What transparency is required; how delivered]
   Fairness constraints: [Fairness properties required in model design]
   
6. SENSITIVE USE ASSESSMENT
   Vulnerable populations affected: [Yes/No — if Yes: describe]
   Consequential decisions: [Yes/No — if Yes: describe]
   Personal data involved: [Yes/No — if Yes: categories; legal basis; DPO consulted? Yes/No]
   Preliminary AISIA reference: [Document reference]
   
7. CHANGE LOG
   [Track specification revisions]
```

---

## 2. Technical Documentation Structure (A.6.2.7)

ISO 42001:2023 requires technical documentation to be maintained for AI systems. This aligns with EU AI Act Article 11 for high-risk systems. The following structure defines what technical documentation is maintained per AI system version.

| Document | Description | Maintained By | Format |
|---------|-------------|--------------|--------|
| AI System Specification | See template above | AI System Owner | Document |
| Model Card | Concise system summary — see AI-IMP-A.6.1-TG | AI System Owner | Document |
| Data Records | Training and operational data documentation — see AI-POL-A.7.2-6 | Data Governance Lead | Register + documents |
| V&V Record | Validation and verification results — see AI-IMP-A.6.1-TG | AI System Owner | Document |
| AISIA | AI System Impact Assessment — see AI-IMP-A.5.2-5-TG | AI Governance Officer | Document |
| Architecture Diagram | System architecture showing components and data flows | ML Engineer | Diagram |
| API Documentation | Input/output schemas; endpoint specifications | ML Engineer | Technical spec |
| Deployment Configuration | Infrastructure config; environment variables (redacted credentials) | DevOps/MLOps | Config files in VCS |
| Operational Runbook | How to operate, monitor, restart, escalate issues with this system | AI System Owner | Document |
| Incident Register | Log of AI incidents and near-misses for this system | AI System Owner | Register |

All technical documentation shall be version-controlled and linked to the AI system version it documents. The AI System Resource Register (AI-POL-A.4.2-6) provides the index.

---

## 3. Operational Monitoring Schema

The AI System Owner defines a monitoring plan for each AI system before deployment. Minimum schema:

| Field | Type | Description |
|-------|------|-------------|
| System ID | Text | Reference to AI System Resource Register |
| Monitoring KPI | Text | Name of the metric being monitored |
| KPI Definition | Text | Exact calculation or data source |
| Normal Range | Text | Expected value range in normal operation |
| Alert Threshold | Text | Value that triggers escalation |
| Alert Action | Text | What happens when the threshold is breached |
| Monitoring Frequency | Enum | Continuous / Hourly / Daily / Weekly |
| Monitoring Tool | Text | Tool used to collect and display this metric |
| Responsible | Text | Who receives alerts; who investigates |
| Last Reviewed | Date | |

**Standard KPIs by AI system type**:

| System Type | Recommended KPIs |
|------------|-----------------|
| Classification | Precision, Recall, F1; class distribution of outputs; confidence score distribution |
| Regression / scoring | MAE / RMSE; score distribution; distribution shift (PSI) |
| Ranking / recommendation | NDCG; CTR; coverage; position bias |
| Generative (text) | Human evaluation sampling rate; refusal rate; output length distribution; topic drift |
| Any | Input data distribution vs. training distribution (PSI); error rate; latency; volume; null/error response rate |

---

## 4. Logging Technical Requirements

Logging must satisfy audit, incident investigation, and regulatory requirements. Technical configuration guidance:

### 4.1 Minimum Log Fields

Every AI system operational log record must include:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Timestamp | DateTime | M | UTC timestamp of the request |
| Session / Request ID | Text | M | Unique identifier for traceability |
| User / Operator ID | Text | M | Anonymised or pseudonymised identifier of the operator (not end-user where not applicable) |
| Input summary | Text | C | Hash or summary of input (not full personal data); for high-risk systems: sufficient for incident reconstruction |
| Output summary | Text | C | Hash or summary of output; for high-risk systems: sufficient for incident reconstruction |
| Model version | Text | M | Version identifier of the model that produced the output |
| Human review flag | Boolean | C | If applicable: whether human review was triggered; outcome |
| System result code | Enum | M | Success / Error / Timeout / Rejected (input validation) |
| Error details | Text | C | If error: error type and brief description |
| Latency (ms) | Integer | R | Response time |

### 4.2 Log Integrity

Logs must be stored where they cannot be modified by the AI system or its operators:
- Write-once or append-only storage
- Access restricted to: AI System Owner (read), CISO (read/manage), Auditors (read)
- Integrity verification: hash-based log integrity checking recommended for High-impact systems

### 4.3 Log Retention

| Impact Classification | Operational Log Retention |
|----------------------|--------------------------|
| Low | 90 days |
| Medium | 180 days |
| High | 365 days (or per regulatory requirement — whichever is longer) |
| Any — following AI incident | Extended to: resolution of any investigation or litigation + 2 years |

For EU AI Act high-risk systems: logs must be retained in accordance with Article 12 requirements (minimum 6 months from placing on market, or as otherwise specified).

---

## 5. AI System Version Control Requirements

For AI systems maintained under [Organisation]'s version control infrastructure:

| Artefact | Version Control Requirement |
|---------|---------------------------|
| Model training code | Full version history in Git; production models tagged |
| Data preparation pipeline | Full version history in Git; pipeline version linked to model version |
| Inference/serving code | Full version history in Git |
| Model weights / binaries | Stored in model registry with version metadata |
| Configuration files | Version-controlled; no secrets in VCS |
| Test/evaluation scripts | Full version history in Git |
| Deployment configuration | Version-controlled (IaC where applicable) |

**Model registry minimum metadata per model version**:
- Model ID and version
- Training dataset ID and version
- Training date
- Key performance metrics (from V&V record)
- V&V record reference
- AISIA reference
- Deployment status (development / staging / production / retired)
- Deployed by (name) and deployment date

---

<!-- QA_VERIFIED: [2026-04-15] -->

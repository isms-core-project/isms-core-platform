# ISMS-IMP-A.5.23.S3 - Secure Configuration & Deployment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.5.23: Cloud Services Security

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S3 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites & Preparation
  - Understanding the Assessment Sheets
  - Completing Each Sheet (Streamlined)
  - Evidence Collection Guide
  - Common Pitfalls & Quality Checklist
  - Review & Approval Process
  - Integration & Maintenance
  - Appendix

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure (10 Sheets)
  - Sheet-by-Sheet Column Specifications
  - Validation Rules & Formulas
  - Integration Points

**Key Changes in v2.1:**
- Section 4 uses configuration tables instead of step-by-step paragraphs
- ONE example per configuration area (removed redundant good/bad comparisons)
- Security baseline references point to industry standards (CIS, NIST)
- Evidence collection streamlined (removed screenshot tutorials)
- Top 10 pitfalls only (removed exhaustive lists)

---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.23.S3 - Secure Configuration & Deployment

#### What This Assessment Covers

This assessment evaluates the **security configuration** of ALL cloud services identified in your cloud service inventory (IMP-5.23.1). While the inventory tells you *what* services you use and vendor due diligence (IMP-5.23.2) tells you *who* provides them, this assessment answers the critical question:

**"Are your cloud services actually configured securely?"**

**Core Principle:**

**"A certified vendor does not guarantee a secure deployment - configuration is YOUR responsibility."**

This is NOT about:
- ❌ Assuming vendor defaults are secure
- ❌ Trusting vendor security without verification
- ❌ Checkbox compliance ("MFA exists in the UI, we're good")
- ❌ One-time configuration without ongoing monitoring

This IS about:
- ✅ Verifying security controls are actually enabled (not just available)
- ✅ Documenting configuration baselines for each service
- ✅ Identifying configuration drift and gaps
- ✅ Implementing defense-in-depth across 5 security layers
- ✅ Continuous monitoring and validation

#### What You'll Document

For EACH cloud service, across 5 security layers:

**Layer 1: Identity & Access Management (Sheet 2)**
- Single Sign-On (SSO) integration
- Multi-Factor Authentication (MFA) enforcement
- Role-Based Access Control (RBAC) implementation
- Privileged access management
- Access review frequency

**Layer 2: Data Protection (Sheet 3)**
- Encryption at-rest (algorithms, key management)
- Encryption in-transit (TLS versions, certificate validation)
- Data Loss Prevention (DLP) rules
- Data classification labels
- Backup encryption and retention

**Layer 3: Network Security (Sheet 4)**
- IP allowlisting/denylisting
- VPN/private connectivity requirements
- Firewall rules and segmentation
- API security (authentication, rate limiting)
- Network logging and monitoring

**Layer 4: Logging & Monitoring (Sheet 5)**
- Audit log enablement (admin actions, data access)
- Log retention periods (regulatory compliance)
- SIEM integration status
- Alert configuration (anomalies, security events)
- Log integrity protection

**Layer 5: Backup & Recovery (Sheet 6)**
- Backup frequency and scope
- Backup encryption and storage location
- Recovery Time Objective (RTO) validation
- Recovery Point Objective (RPO) validation
- Disaster recovery testing

#### How This Relates to Other A.5.23 Assessments

```
┌────────────────────────────────────────────────────────────────┐
│                 A.5.19-23 FRAMEWORK FLOW                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    │
│  │ IMP-5.23.1   │ →  │ IMP-5.23.2   │ →  │ IMP-5.23.3   │    │
│  │ INVENTORY    │    │ VENDOR DD    │    │  THIS DOC    │    │
│  │ "What?"      │    │ "Who/Terms?" │    │ "How?"       │    │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘    │
│         │                   │                   │             │
│         └───────────────────┼───────────────────┘             │
│                             ▼                                 │
│                   ┌──────────────────┐                        │
│                   │  IMP-5.23.4      │                        │
│                   │  GOVERNANCE      │                        │
│                   │  "Ongoing?"      │                        │
│                   └────────┬─────────┘                        │
│                            │                                  │
│                            ▼                                  │
│                   ┌──────────────────┐                        │
│                   │  IMP-5.23.5      │                        │
│                   │  DASHBOARD       │                        │
│                   │  "Reporting"     │                        │
│                   └──────────────────┘                        │
└────────────────────────────────────────────────────────────────┘
```

**Upstream Dependencies:**
- IMP-5.23.1 (Inventory) - Provides service list, criticality, data classification
- IMP-5.23.2 (Vendor DD) - Provides vendor capabilities (what CAN be configured)

**Key Insight:** Vendor may have ISO 27001 certification (IMP-5.23.2 verified), but if YOU don't enable MFA or encryption, the deployment is insecure. Configuration is the customer's responsibility.

**Downstream Consumers:**
- IMP-5.23.4 (Governance) - Uses configuration baselines for drift detection
- IMP-5.23.5 (Dashboard) - Aggregates configuration compliance metrics

### Who Should Complete This Assessment

#### Primary Stakeholders

| Role | Responsibility | Time Commitment |
|------|---------------|-----------------|
| **Cloud Operations Lead** | Coordinate assessment, consolidate results | 8-12 hours |
| **Cloud Security Engineer** | Complete Sheets 2-6 (technical configuration) | 16-24 hours |
| **DevOps / Platform Engineer** | Provide IaC templates, configuration exports | 12-16 hours |
| **IT Operations** | Validate network, logging configurations | 8-12 hours |
| **ISMS Coordinator** | Manage evidence, approvals | 6-8 hours |

#### Required Skills

**Cloud Operations:**
- Admin console access for all cloud services
- Understanding of cloud security controls (IAM, encryption, networking)
- Ability to export configuration settings

**Technical Skills:**
- Cloud platforms (AWS, Azure, GCP admin experience)
- Identity management (SAML, OAuth, MFA technologies)
- Networking (VPN, firewall, API security)
- Scripting (PowerShell, AWS CLI, Azure CLI for config exports)

#### Time Commitment

**Initial Assessment (First Time):**
- Configuration review: 2-3 weeks
- Evidence collection (screenshots, exports): 1-2 weeks
- Gap analysis: 1 week
- Review and approval: 1 week
- **Total:** 5-7 weeks

**Quarterly Updates:**
- Review configuration changes: 3-5 days
- Re-validate critical controls: 2-3 days
- Update evidence: 1-2 days
- Approval: 1-2 days
- **Total:** 1-2 weeks

**Assumptions:**
- ~15-25 cloud services to assess
- Admin console access available
- No major configuration changes since last review

#### Collaboration Model

**Week 1-2: Configuration Discovery**
- Export configuration settings (IaC, admin console exports)
- Document current state for each security layer
- Identify configuration standards/baselines

**Week 3-4: Gap Analysis**
- Compare actual config vs. security baselines
- Identify missing controls (MFA not enforced, encryption disabled)
- Assess compliance with DORA, NIS2, GDPR requirements

**Week 5: Evidence Collection**
- Screenshot critical configurations
- Export configuration files (JSON, YAML, XML)
- Document compensating controls for gaps

**Week 6-7: Remediation Planning**
- Prioritize gaps (Critical services first)
- Assign remediation owners
- Set target dates for fixes

**Week 7: Review & Approval**
- Cloud Ops review (technical accuracy)
- Security review (risk assessment)
- CISO approval (risk acceptance for gaps)

### Expected Outputs

**Primary Deliverable:**
- **ISMS-IMP-A.5.23.S3_SecureConfig_YYYYMMDD.xlsx** (10-sheet workbook)

**Workbook Contents:**

| Sheet | Title | Rows (Typical) | Purpose |
|-------|-------|----------------|---------|
| 1 | Instructions & Legend | N/A | How to use this workbook |
| 2 | Identity & Access Configuration | 15-25 | SSO, MFA, RBAC, privileged access |
| 3 | Data Protection Configuration | 15-25 | Encryption, DLP, classification |
| 4 | Network Security Configuration | 15-25 | IP controls, VPN, firewall, API security |
| 5 | Logging & Monitoring Configuration | 15-25 | Audit logs, SIEM, alerts, retention |
| 6 | Backup & Recovery Configuration | 15-25 | Backup freq, encryption, RTO/RPO testing |
| 7 | Jurisdictional Risk Configuration | 15-25 | Data residency, key mgmt alignment |
| 8 | Summary Dashboard | Auto-calc | Executive summary, compliance % |
| 9 | Evidence Register | 50-150 | Links to config exports, screenshots |
| 10 | Approval Sign-Off | N/A | Cloud Ops, Security, CISO approvals |

**Supporting Deliverables:**
- Evidence repository (config exports, screenshots)
- Configuration baseline documents (per service type)
- Gap analysis with remediation plan
- Risk register entries for accepted gaps

### Assessment Success Criteria

**Completeness:**
- ✅ All services from IMP-5.23.1 assessed (no gaps)
- ✅ All 5 security layers evaluated per service
- ✅ All required evidence collected (config exports, screenshots)
- ✅ All status flags set (✅/⚠️/❌/N/A)
- ✅ All gaps have remediation plans or risk exceptions

**Configuration Quality:**
- ✅ All Critical services: MFA enforced + Encryption enabled + Logs to SIEM
- ✅ All Confidential/Restricted data: Encryption at-rest + DLP configured
- ✅ All services: Audit logging enabled with ≥90-day retention
- ✅ Configuration documented in IaC (Infrastructure as Code) where possible
- ✅ Configuration drift monitoring enabled

**Compliance:**
- ✅ DORA requirements: Encryption + logging + BC testing for ICT services
- ✅ NIS2 requirements: Security measures implemented and documented
- ✅ GDPR/FADP: Encryption for personal data, audit trails
- ✅ Industry baselines: CIS Benchmarks or vendor best practices applied

**Traceability:**
- ✅ Every ✅ (Compliant) → Config export or screenshot exists
- ✅ Every gap → Remediation plan or risk exception
- ✅ Every service → Linked to IMP-5.23.1 inventory
- ✅ Evidence register → All links work, files accessible

### Common Use Cases

**Use Case 1: New Service Deployment**
*DevOps team wants to deploy Datadog for monitoring.*

**Configuration Assessment Flow:**
1. Add to IMP-5.23.1 inventory first
2. Complete IMP-5.23.2 vendor due diligence
3. Complete IMP-5.23.3 secure configuration assessment:
   - Sheet 2: Enable SSO (Okta integration), enforce MFA
   - Sheet 3: Enable encryption at-rest, configure DLP for API keys
   - Sheet 4: Restrict API access to corporate IP ranges
   - Sheet 5: Enable audit logging, forward logs to SIEM
   - Sheet 6: Configure backup of Datadog configuration (IaC)
4. Document configuration baseline in IaC (Terraform)
5. If approved → deploy with secure config, enable drift detection

**Use Case 2: Configuration Drift Detection**
*Quarterly review identifies MFA disabled on Salesforce.*

**Assessment Flow:**
1. Pull existing IMP-5.23.3 assessment (last quarter)
2. Re-export Salesforce configuration (admin console)
3. Compare: Last assessment showed MFA=Enforced, now MFA=Optional
4. Investigate: Who changed? When? Why?
5. Remediate: Re-enable MFA enforcement
6. Update IMP-5.23.3: Document drift incident, remediation action
7. Enhance: Add automated drift detection (AWS Config, Azure Policy)

**Use Case 3: Audit Preparation**
*External ISO 27001 auditor arriving in 30 days.*

**Assessment Flow:**
1. Verify all assessments complete and current (<90 days old)
2. Re-validate critical controls (MFA, encryption, logging)
3. Check all evidence links work (config exports, screenshots)
4. Ensure all gaps have documented risk exceptions
5. Generate compliance report from Sheet 8 (Dashboard)
6. Prepare evidence folder for auditor review

**Use Case 4: Regulatory Change Response**
*DORA Article 28.7 now requires annual BC/DR testing.*

**Assessment Flow:**
1. Identify all Critical ICT providers (DORA scope)
2. Review Sheet 6 (Backup & Recovery) for existing BC testing
3. Add new column: "Last BC Test Date" and "Test Result"
4. Plan annual BC/DR tests for all Critical services
5. Update assessment quarterly with test results
6. Report to risk committee on BC/DR readiness

---

**END OF SECTION 1: ASSESSMENT OVERVIEW**

## Prerequisites & Preparation

### Required Inputs

**From IMP-5.23.1 (Cloud Service Inventory):**
- ✅ Complete and approved inventory
- ✅ Service list with criticality ratings
- ✅ Data classification for each service
- ✅ Service owner assignments

**From IMP-5.23.2 (Vendor Due Diligence):**
- ✅ Vendor security capabilities (what CAN be configured)
- ✅ Vendor certifications (SOC 2, ISO 27001)
- ✅ Data residency requirements

**Admin Access Required:**
- ✅ Cloud service admin consoles (AWS, Azure, GCP, SaaS platforms)
- ✅ Identity provider (Okta, Azure AD, Google Workspace)
- ✅ SIEM system (Splunk, Datadog, Azure Sentinel)
- ✅ Infrastructure as Code repository (Terraform, CloudFormation)

### Required Tools & Access

**Configuration Export Tools:**

| Cloud Platform | Tool | Purpose |
|----------------|------|---------|
| **AWS** | AWS CLI, CloudFormation export | Export VPC, IAM, S3, CloudTrail configs |
| **Azure** | Azure CLI, Azure Resource Manager | Export resource configs, policies |
| **GCP** | gcloud CLI, Deployment Manager | Export project configs, IAM bindings |
| **Microsoft 365** | PowerShell (MSOnline, Exchange) | Export tenant configs, DLP rules |
| **SaaS (Generic)** | Admin console, API | Screenshot or JSON export |

**Evidence Collection Tools:**
- Screenshot tool (Snipping Tool, Greenshot, CleanShot)
- JSON/XML viewer (for config file review)
- Diff tool (compare configs over time)

**Analysis Tools:**
- Config compliance scanners (AWS Config, Azure Policy, GCP Security Command Center)
- CIS Benchmark tools (Prowler for AWS, ScoutSuite for multi-cloud)
- Infrastructure as Code linters (TFLint, Checkov, tfsec)

### Security Baselines & Standards

**Industry Benchmarks to Reference:**

| Benchmark | Scope | Where to Get It |
|-----------|-------|-----------------|
| **CIS Benchmarks** | AWS, Azure, GCP, Microsoft 365, etc. | https://www.cisecurity.org/cis-benchmarks |
| **AWS Security Best Practices** | AWS Well-Architected Framework | https://aws.amazon.com/architecture/well-architected |
| **Azure Security Baseline** | Azure Cloud Adoption Framework | https://learn.microsoft.com/azure/cloud-adoption-framework |
| **Google Cloud Security Best Practices** | GCP security foundations | https://cloud.google.com/security/best-practices |
| **NIST CSF** | Cross-cloud framework | https://www.nist.gov/cyberframework |

**Internal Baselines (Create If Not Exist):**
- Standard MFA enforcement policy (all users vs. privileged only)
- Encryption standards (AES-256, TLS 1.2+, key rotation)
- Logging requirements (which events, retention period)
- Network segmentation principles (zero trust, least privilege)

### Stakeholder Coordination

**Before Starting:**

1. **Kickoff Meeting** (90 minutes)
   - Cloud Ops, Security, DevOps, Platform Engineering
   - Present assessment scope and timeline
   - Assign configuration areas to teams
   - Establish evidence repository

2. **Configuration Baseline Agreement**
   - Define "secure configuration" for each service type
   - Reference CIS Benchmarks where applicable
   - Document exceptions (legacy services, technical limitations)

3. **Tool Access Verification**
   - Verify admin console access for all team members
   - Test configuration export scripts
   - Validate SIEM integration for log verification

### Evidence Repository Structure

**Folder Organization:**
```
/ISMS/Evidence/A.5.23.3/
    ├── AWS_Cloud/
    │   ├── IAM_Config_Export_20260120.json
    │   ├── S3_Encryption_Screenshot_20260120.png
    │   ├── CloudTrail_Config_20260120.json
    │   └── VPC_Security_Groups_20260120.csv
    ├── Microsoft_365/
    │   ├── MFA_Policy_Screenshot_20260120.png
    │   ├── DLP_Rules_Export_20260120.xml
    │   └── Audit_Log_Retention_20260120.png
    └── [Service_Name]/
        └── [Config_Evidence]
```

**Naming Convention:** `[Service]_[ConfigArea]_[Type]_YYYYMMDD.[ext]`

---

## Understanding the Assessment Sheets

### Workbook Structure Overview

**10-Sheet Architecture:**

```
┌──────────────────────────────────────────────────────────────┐
│         IMP-5.23.3 WORKBOOK STRUCTURE                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Sheet 1: Instructions & Legend                             │
│           [Read-only reference]                              │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │    CONFIGURATION ASSESSMENT SHEETS (2-6)               │ │
│  │    Base Columns A-Q + Config-Specific Columns          │ │
│  ├────────────────────────────────────────────────────────┤ │
│  │  Sheet 2: Identity & Access Configuration             │ │
│  │  Sheet 3: Data Protection Configuration               │ │
│  │  Sheet 4: Network Security Configuration              │ │
│  │  Sheet 5: Logging & Monitoring Configuration          │ │
│  │  Sheet 6: Backup & Recovery Configuration             │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  Sheet 7: Jurisdictional Risk Configuration Alignment       │
│           [Links to IMP-5.23.2 Sheet 7]                      │
│                                                              │
│  Sheet 8: Summary Dashboard                                 │
│           [Auto-calculated from Sheets 2-7]                  │
│                                                              │
│  Sheet 9: Evidence Register                                 │
│           [Central evidence tracking]                        │
│                                                              │
│  Sheet 10: Approval Sign-Off                                │
│            [Cloud Ops, Security, CISO approvals]             │
└──────────────────────────────────────────────────────────────┘
```

### Base Columns (A-Q) - Standard Across All Sheets

**All configuration sheets (2-6) share these base columns:**

| Column | Header | Source | Purpose |
|--------|--------|--------|---------|
| **A** | Cloud Service Name | IMP-5.23.1 | Service as YOU know it |
| **B** | Vendor Name | IMP-5.23.1 | Provider's legal name |
| **C** | Service Type | IMP-5.23.1 | SaaS, IaaS, PaaS, etc. |
| **D** | Service Criticality | IMP-5.23.1 | Critical, High, Medium, Low |
| **E** | Data Classification | IMP-5.23.1 | Restricted, Confidential, Internal, Public |
| **F** | Deployment Environment | Assessment | Production, Staging, Development, Test |
| **G** | IaC Managed? | Assessment | Yes (Terraform/CF/ARM), No (Manual), Partial |
| **H** | Status | Assessment | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / N/A |
| **I** | Evidence Location | Sheet 9 | Link/reference to config export or screenshot |
| **J** | Gap Description | Assessment | What's misconfigured or missing |
| **K** | Remediation Needed | Assessment | Yes/No |
| **L** | Exception ID | Risk Register | If gap accepted: risk exception reference |
| **M** | Risk ID | Risk Register | Risk register entry reference |
| **N** | Compensating Controls | Security | Mitigating measures for gaps |
| **O** | Configuration Owner | Team | Team/person responsible for this service's config |
| **P** | Target Remediation Date | Remediation Plan | When gap will be fixed |
| **Q** | Last Config Review Date | Assessment | When configuration was last validated |

**Important:**
- Columns A-E copied from IMP-5.23.1 (maintain consistency)
- Column F (Environment) is new - same service may have different configs in Prod vs. Dev
- Column G (IaC Managed) tracks configuration-as-code maturity
- Status (Column H) is **configuration-specific** (not vendor-level like IMP-5.23.2)

### Extended Columns (R+) - Configuration-Specific

Each configuration sheet has **extended columns** for specific security controls:

| Sheet | Extended Columns | Focus Area |
|-------|------------------|------------|
| **Sheet 2** | R-AA | SSO, MFA, RBAC, privileged access, access reviews |
| **Sheet 3** | R-Z | Encryption (rest/transit), DLP, classification, backup encryption |
| **Sheet 4** | R-X | IP controls, VPN, firewall, API security, network logging |
| **Sheet 5** | R-W | Audit logs, retention, SIEM, alerts, log integrity |
| **Sheet 6** | R-Y | Backup frequency, encryption, RTO/RPO, DR testing |

**See Part II (Technical Specification) for complete column definitions.**

### Configuration Assessment vs. Vendor Assessment

**Key Difference from IMP-5.23.2:**

| IMP-5.23.2 (Vendor DD) | IMP-5.23.3 (Secure Config) |
|------------------------|----------------------------|
| "Does vendor OFFER MFA?" | "Is MFA ENFORCED for this service?" |
| "Does vendor SUPPORT encryption?" | "Is encryption ENABLED with customer-managed keys?" |
| "Does vendor PROVIDE audit logs?" | "Are audit logs FLOWING to our SIEM?" |
| Vendor capability | Customer configuration |
| Vendor responsibility | Customer responsibility |

**Example:**
- IMP-5.23.2: AWS has ISO 27001 ✅ (vendor certified)
- IMP-5.23.3: AWS S3 bucket has public access ❌ (customer misconfigured)

### Data Flow & Dependencies

**Input Flow:**
```
IMP-5.23.1 Inventory (Columns A-E)
        ↓
    Sheets 2-6 (Base + Config columns)
        ↓
    Sheet 7 (Jurisdictional alignment - links to IMP-5.23.2 Sheet 7)
        ↓
    Sheet 8 (Dashboard - auto-calculated)
        ↓
    Sheet 9 (Evidence Register)
        ↓
    Sheet 10 (Approvals)
```

**Cross-Assessment Integration:**
- IMP-5.23.2 Sheet 5 (Data Sovereignty) → IMP-5.23.3 Sheet 3 (Data Protection)
  - If IMP-5.23.2 says "Encryption required", IMP-5.23.3 verifies it's enabled
- IMP-5.23.2 Sheet 2 (Vendor Certs) → IMP-5.23.3 All Sheets
  - Vendor has SOC 2 ≠ Automatically means you're secure

### Status Flag Meanings

**Consistent across all sheets:**

| Status | Symbol | Meaning | When to Use |
|--------|--------|---------|-------------|
| **Compliant** | ✅ | Control fully implemented and verified | Config matches security baseline, evidence exists |
| **Partial** | ⚠️ | Control partially implemented | Some elements configured but gaps exist |
| **Non-Compliant** | ❌ | Control not implemented or severely deficient | Control missing, disabled, or critically misconfigured |
| **N/A** | N/A | Not applicable to this service/environment | Control doesn't apply (document why in Gap Description) |

**Key Principle:** Every status requires evidence:
- ✅ → Config export or screenshot showing control enabled
- ⚠️ → Evidence + gap description
- ❌ → Gap description + remediation plan
- N/A → Rationale (why control doesn't apply)

### Sheet Completion Order

**Recommended Sequence:**

1. **Sheet 2 (Identity & Access)** - Start here (foundational control)
2. **Sheet 3 (Data Protection)** - Often dependent on Sheet 2 (who can decrypt?)
3. **Sheet 5 (Logging & Monitoring)** - Verify logging before network/backup
4. **Sheet 4 (Network Security)** - Network controls
5. **Sheet 6 (Backup & Recovery)** - Backup configurations
6. **Sheet 7 (Jurisdictional Risk)** - Config alignment with data sovereignty
7. **Sheet 9 (Evidence Register)** - As you complete Sheets 2-7
8. **Sheet 8 (Dashboard)** - Auto-calculated (verify formulas)
9. **Sheet 10 (Approvals)** - After all sheets complete

**Rationale:** Build from foundational controls (identity) to dependent controls (backup requires encryption from Sheet 3).

### Regulatory Applicability Guide

**Which sheets apply to which regulations:**

| Regulation | Applicable Sheets | Key Requirements |
|------------|-------------------|------------------|
| **GDPR / FADP** | Sheets 2, 3, 5 | Access controls, encryption, audit trails for personal data |
| **DORA** | Sheets 2, 3, 5, 6 | Strong auth, encryption, logging, BC/DR testing |
| **NIS2** | All Sheets | Comprehensive security measures across all layers |
| **PCI-DSS** | Sheets 2, 3, 4, 5 | MFA, encryption, network segmentation, logging |

**See ISMS-POL-00 (Regulatory Applicability Framework) for detailed requirements.**

### Configuration Drift Detection

**Why It Matters:**
- Today: Compliant configuration
- Tomorrow: Someone disables MFA "temporarily"
- Next quarter: Assessment shows drift

**How to Detect Drift:**
- **Cloud-Native:** AWS Config, Azure Policy, GCP Security Command Center
- **Third-Party:** Prisma Cloud, Wiz, Lacework, CloudCustodian
- **IaC-Based:** Terraform state comparison, CloudFormation drift detection
- **Manual:** Quarterly re-export and compare (least reliable)

**Best Practice:** Enable automated drift detection, alert on changes to critical configs.

---

**END OF SECTIONS 2-3: PREREQUISITES & UNDERSTANDING SHEETS**

## Completing Each Sheet - Configuration Guidance

### Overview

This section provides configuration assessment guidance for each security layer (Sheets 2-6).

**Structure for each sheet:**
1. Purpose - Why this control layer matters
2. What to Assess - Key configuration items
3. How to Assess - Assessment tables + evidence
4. Common Misconfigurations - Key gotchas
5. Example Entry - One good example

**Base Columns (A-Q):** See previous section. Standard across all sheets.

**Extended Columns (R+):** Configuration-specific, documented below.

---

## Sheet 2: Identity & Access Management Configuration

### Purpose

Verify that identity and access controls are properly configured to prevent unauthorized access. Strong IAM is the first line of defense - even encrypted data is useless if attackers can log in with stolen credentials.

**Success Criterion:** All Critical/High services enforce MFA for all users, use SSO for centralized identity, implement RBAC with least privilege, and conduct quarterly access reviews.

### What to Assess

For each service:
- Single Sign-On (SSO) integration status
- Multi-Factor Authentication (MFA) enforcement
- Role-Based Access Control (RBAC) implementation
- Privileged access management (admin accounts)
- Access review frequency and evidence
- Session timeout and password policies

### How to Assess

**Step 1: Verify SSO Integration**

| SSO Type | Assessment Method | Evidence |
|----------|-------------------|----------|
| **SAML 2.0** | Check IdP (Okta, Azure AD) for app integration | IdP console screenshot showing app |
| **OAuth/OIDC** | Check OAuth configuration in service | Service admin console, client ID config |
| **No SSO** | Users log in with service-specific passwords | Identify as gap (❌ for Critical services) |

**CIS Benchmark Reference:** CIS Azure AD 1.1.1 "Ensure multi-factor authentication is enabled for all users"

**Step 2: Verify MFA Enforcement**

| MFA Status | Assessment | When to Use | Evidence |
|------------|------------|-------------|----------|
| **Enforced (All Users)** | ✅ Compliant | All Critical/High services | Policy screenshot + user report showing 100% MFA |
| **Enforced (Admins Only)** | ⚠️ Partial | Medium/Low services acceptable | Admin MFA report |
| **Optional (Not Enforced)** | ❌ Non-Compliant | Never acceptable for Critical | Identify as gap |
| **Not Available** | ❌ Non-Compliant | Vendor limitation - consider alternative | Vendor documentation |

**How to Verify:**
- **Azure AD:** Conditional Access policies, user MFA status report
- **AWS:** IAM policy, MFA device report per user
- **Google Workspace:** Security → 2-Step Verification enforcement
- **SaaS:** Admin console → Security settings

**Step 3: Assess RBAC Implementation**

| RBAC Maturity | Description | Assessment | Evidence |
|---------------|-------------|------------|----------|
| **Role-Based** | Predefined roles (Viewer, Editor, Admin) assigned by job function | ✅ | Role assignment export |
| **Attribute-Based** | Dynamic rules (e.g., "Finance department = access to finance data") | ✅ | Policy rules export |
| **Group-Based** | Users assigned to groups, groups assigned permissions | ⚠️ Acceptable | Group membership export |
| **Direct Permissions** | Individual users granted permissions ad-hoc | ❌ | Security gap (no RBAC) |

**Least Privilege Check:**
- Are there more Admins than necessary? (Target: <5% of users)
- Are permissions granted "just in case"? (Should be "just in time")
- Are generic accounts used? (Should be individual accountability)

**Step 4: Complete Extended Columns**

| Column | Field | How to Assess | Evidence Type |
|--------|-------|---------------|---------------|
| R | SSO Integration | Enabled/Disabled/Partial | IdP screenshot |
| S | SSO Protocol | SAML/OAuth/OIDC/None | Integration config |
| T | MFA Enforcement | All Users/Admins Only/Optional/None | MFA policy + user report |
| U | MFA Methods | SMS/App/Hardware Token/Multiple | Supported methods list |
| V | RBAC Implemented | Yes/No/Partial | Role definition export |
| W | Privileged Access Mgmt | Just-in-Time/Approval Required/Permanent/None | PAM policy |
| X | Access Review Frequency | Quarterly/Semi-Annual/Annual/None | Last review report |
| Y | Last Access Review Date | Date | Review completion report |
| Z | Session Timeout (Minutes) | Number (e.g., 30, 60, 480) | Policy config screenshot |
| AA | Password Policy Adequate | Yes (complex+length)/No | Policy screenshot |

**Step 5: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| SSO + MFA (all users) + RBAC + Quarterly reviews | ✅ | - |
| SSO + MFA (admins only) + RBAC | ⚠️ | "MFA not enforced for regular users" |
| No SSO but MFA enforced + RBAC | ⚠️ | "No SSO (password sprawl risk)" |
| No MFA for Critical service | ❌ | "No MFA - unacceptable for Critical service" |
| No RBAC (direct permissions) | ❌ | "No role-based access control" |
| No access reviews | ⚠️ | "Access reviews not conducted" |

### Common Misconfigurations

❌ **MFA available but not enforced** - "Users can enable MFA" ≠ "MFA is required"  
❌ **SSO configured but fallback enabled** - Local accounts bypass SSO (backdoor)  
❌ **Over-privileged roles** - "Power Users" = Admin in practice  
❌ **Stale accounts** - Ex-employees still have access (no access review)  
❌ **Shared admin accounts** - No individual accountability  
❌ **Conditional Access misconfigured** - "MFA required" but exceptions for legacy apps  

### Example Entry

**Good Example:**

| A | B | C | D | E | F | G | H | I | R | S | T | U | V | W | X | Y | Z | AA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Microsoft 365 | Microsoft Corp. | SaaS | Critical | Confidential | Production | Yes (Terraform) | ✅ | /evidence/m365/iam_config.json | Enabled | SAML | All Users | App+Hardware | Yes | Approval Required | Quarterly | 15.12.2025 | 30 | Yes |

---

## Sheet 3: Data Protection Configuration

### Purpose

Verify that data is protected at rest, in transit, and during processing. Encryption is your last line of defense if access controls fail.

**Success Criterion:** All Restricted/Confidential data encrypted at-rest (AES-256 or equivalent) and in-transit (TLS 1.2+), with customer-managed keys where possible. DLP configured for sensitive data types.

### What to Assess

For each service:
- Encryption at-rest (algorithm, key management)
- Encryption in-transit (TLS version, certificate validation)
- Data Loss Prevention (DLP) rules
- Data classification labels applied
- Backup encryption
- Key rotation policies

### How to Assess

**Step 1: Verify Encryption at Rest**

| Encryption Type | Description | Assessment | Evidence |
|-----------------|-------------|------------|----------|
| **AES-256 (Customer-Managed Key)** | You control the key (BYOK/HYOK) | ✅ Best | Key vault screenshot + service config |
| **AES-256 (Vendor-Managed)** | Vendor controls the key | ⚠️ Acceptable | Service encryption status |
| **AES-128 or Weaker** | Outdated algorithm | ❌ Insufficient | Upgrade required |
| **No Encryption** | Data stored in plaintext | ❌ Unacceptable | Critical gap |

**Where to Check:**
- **AWS S3:** Bucket properties → Default encryption (SSE-S3, SSE-KMS, SSE-C)
- **Azure Storage:** Storage account → Encryption → Customer-managed keys
- **GCP Cloud Storage:** Bucket settings → Encryption type
- **SaaS:** Admin console → Security → Encryption settings

**CIS Benchmark Reference:**
- AWS: CIS 2.1.1 "Ensure S3 bucket has encryption enabled"
- Azure: CIS 3.1 "Ensure storage account encryption is enabled"

**Step 2: Verify Encryption in Transit**

| TLS Version | Assessment | When Acceptable | Evidence |
|-------------|------------|-----------------|----------|
| **TLS 1.3** | ✅ Best practice | All services | TLS scan report (SSL Labs) |
| **TLS 1.2** | ✅ Acceptable | Minimum for compliance | Connection test |
| **TLS 1.1 or older** | ❌ Deprecated | Never (PCI-DSS prohibits) | Upgrade required |
| **No TLS (HTTP)** | ❌ Unacceptable | Never for production | Critical gap |

**How to Test:**
- **Web Services:** https://www.ssllabs.com/ssltest/ (SSL Labs)
- **API Endpoints:** `openssl s_client -connect api.service.com:443 -tls1_2`
- **Database Connections:** Check connection string for `ssl=true` or `encrypt=true`

**Step 3: Assess DLP Configuration**

| DLP Maturity | Description | Assessment | Use Case |
|--------------|-------------|------------|----------|
| **Rule-Based DLP** | Detect PII, credit cards, secrets by pattern | ✅ | Email, file sharing, cloud storage |
| **ML-Based DLP** | Machine learning detects sensitive content | ✅ Best | Advanced threat protection |
| **No DLP** | No automated sensitive data detection | ❌ | Gap for Confidential data |

**Common DLP Rules to Check:**
- Credit card numbers (PCI-DSS requirement)
- Social security numbers (PII protection)
- API keys / passwords (secret scanning)
- Health records (HIPAA/privacy)
- Financial data (SOX, insider trading)

**Where to Configure:**
- **Microsoft 365:** Compliance Center → Data Loss Prevention
- **Google Workspace:** Security → Data Protection
- **AWS:** Amazon Macie (S3 DLP), CloudWatch Logs Insights
- **Slack, Box, Dropbox:** Enterprise DLP settings

**Step 4: Verify Data Classification**

| Classification Method | Description | Assessment |
|-----------------------|-------------|------------|
| **Labels Applied** | Files tagged (Public, Internal, Confidential, Restricted) | ✅ |
| **Labels Available but Not Applied** | Feature exists but users don't use it | ⚠️ |
| **No Classification** | No labeling capability | ❌ |

**Microsoft Information Protection (MIP) Example:**
- Sensitivity labels defined (IT configures)
- Labels applied to files (users select or auto-apply)
- DLP rules enforce label policy (IT enforces)

**Step 5: Complete Extended Columns**

| Column | Field | How to Assess | Evidence Type |
|--------|-------|---------------|---------------|
| R | Encryption At-Rest | AES-256 (CMK)/AES-256 (Vendor)/AES-128/None | Service config export |
| S | Key Management | Customer (BYOK)/Vendor/Hybrid | Key vault screenshot |
| T | Key Rotation Enabled | Auto/Manual/None | Key policy config |
| U | Encryption In-Transit | TLS 1.3/TLS 1.2/TLS 1.1/None | SSL Labs report |
| V | Certificate Validation | Strict/Permissive/None | Connection config |
| W | DLP Configured | Yes/No/Partial | DLP policy export |
| X | DLP Rules Count | Number | Policy list screenshot |
| Y | Classification Labels Applied | Yes/No/Partial | File metadata export |
| Z | Backup Encrypted | Yes/No | Backup policy config |

**Step 6: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| AES-256 (CMK) + TLS 1.3 + DLP + Labels | ✅ | - |
| AES-256 (Vendor) + TLS 1.2 + DLP | ⚠️ | "Vendor-managed keys (consider BYOK)" |
| AES-256 + TLS 1.2 + No DLP | ⚠️ | "No DLP configured for Confidential data" |
| No encryption at-rest | ❌ | "Data stored unencrypted - critical gap" |
| TLS 1.1 or older | ❌ | "Deprecated TLS version" |
| No encryption in-transit (HTTP) | ❌ | "Data transmitted in plaintext" |

### Common Misconfigurations

❌ **Encryption "available" but not enabled** - Feature exists but turned off  
❌ **Vendor-managed keys for Restricted data** - No control if vendor compromised  
❌ **DLP in audit mode only** - Detects but doesn't block (set to enforce!)  
❌ **Mixed TLS versions** - Accepts TLS 1.3 AND TLS 1.0 (downgrades possible)  
❌ **Backup not encrypted** - Encrypted production, plaintext backup  
❌ **Key rotation disabled** - Same key for years (should rotate annually)  

### Example Entry

**Good Example:**

| A | B | C | D | E | F | G | H | I | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AWS S3 (Finance Bucket) | Amazon Web Services | IaaS | Critical | Restricted | Production | Yes (Terraform) | ✅ | /evidence/aws/s3_encryption.json | AES-256 (CMK) | Customer (AWS KMS) | Auto (Annual) | TLS 1.3 | Strict | Yes | 15 | Yes | Yes |

---

**END OF SECTION 4 PART 1: IDENTITY & DATA PROTECTION**

## Sheet 4: Network Security Configuration

### Purpose

Verify network controls prevent unauthorized access and lateral movement. Defense-in-depth requires network segmentation, even with strong IAM.

**Success Criterion:** All Critical services restrict access to corporate IP ranges or VPN, implement API security controls, and log all network events.

### What to Assess

For each service:
- IP allowlisting/denylisting (restrict source IPs)
- VPN/private connectivity requirements
- API authentication and authorization
- API rate limiting (prevent abuse)
- Network segmentation (isolation between environments)
- Network logging and monitoring

### How to Assess

**Step 1: Verify IP Access Controls**

| Control Type | Description | Assessment | Use Case |
|--------------|-------------|------------|----------|
| **IP Allowlist** | Only specific IPs allowed | ✅ | Production databases, admin consoles |
| **IP Denylist** | Block known bad actors | ⚠️ Reactive | Public-facing services |
| **No IP Controls** | Accept connections from anywhere | ❌ | Unacceptable for Critical services |

**Where to Configure:**
- **AWS:** Security Groups, NACLs, WAF IP sets
- **Azure:** Network Security Groups, Firewall rules
- **SaaS:** Admin console → IP restrictions (Salesforce, Workday, etc.)

**CIS Benchmark:** AWS 5.1 "Ensure no security groups allow ingress from 0.0.0.0/0 to port 22 or 3389"

**Step 2: Assess VPN/Private Connectivity**

| Connectivity | Description | Assessment | When Required |
|--------------|-------------|------------|---------------|
| **Private Link** | AWS PrivateLink, Azure Private Endpoint | ✅ Best | Critical data in cloud |
| **VPN (Site-to-Site)** | IPsec tunnel to cloud | ✅ | Hybrid connectivity |
| **VPN (User)** | Users connect via VPN | ⚠️ Acceptable | Remote access |
| **Public Internet** | Direct internet access | ❌ | Only for Low criticality |

**Step 3: Verify API Security**

| API Control | What to Check | Evidence |
|-------------|---------------|----------|
| **Authentication** | API keys, OAuth tokens, mTLS | Auth config screenshot |
| **Authorization** | Scope limits, RBAC for APIs | Permission model export |
| **Rate Limiting** | Requests/second limits | Rate limit config |
| **Input Validation** | Reject malformed requests | WAF rules, API gateway config |
| **TLS for APIs** | All API calls over HTTPS | API endpoint test |

**Common API Vulnerabilities:**
- Unauthenticated endpoints (anyone can call)
- Over-privileged API keys (admin access when read-only needed)
- No rate limiting (DDoS amplification)
- API keys in code repositories (secret scanning gap)

**Step 4: Complete Extended Columns**

| Column | Field | How to Assess | Evidence |
|--------|-------|---------------|----------|
| R | IP Access Control | Allowlist/Denylist/None | Firewall rules export |
| S | IP Ranges Allowed | CIDR notation (e.g., 203.0.113.0/24) | Config export |
| T | VPN Required | Yes/No/Optional | Network policy doc |
| U | Private Connectivity | PrivateLink/VPN/Public | Connection config |
| V | API Authentication | OAuth/API Key/mTLS/None | API config |
| W | API Rate Limiting | Yes/No | Rate limit policy |
| X | Network Segmentation | Isolated/Shared/None | Network diagram |

**Step 5: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| IP Allowlist + VPN + API Auth + Rate Limit | ✅ | - |
| IP Allowlist + API Auth (no rate limit) | ⚠️ | "No API rate limiting" |
| No IP controls but VPN required | ⚠️ | "IP allowlist recommended" |
| Public internet access for Critical service | ❌ | "No network access controls" |
| Unauthenticated API endpoints | ❌ | "Public API without authentication" |

### Common Misconfigurations

❌ **0.0.0.0/0 in production** - "Allow from anywhere" for database access  
❌ **VPN configured but not enforced** - VPN exists but direct access also works  
❌ **API keys in client-side code** - Exposed in browser dev tools  
❌ **Rate limiting too permissive** - 10,000 req/sec allows DDoS  
❌ **Dev and Prod in same network** - No segmentation  
❌ **WAF in detection mode only** - Detects attacks but doesn't block  

### Example Entry

| A | B | C | D | E | F | G | H | I | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PostgreSQL (Production) | Amazon RDS | IaaS | Critical | Confidential | Production | Yes (Terraform) | ✅ | /evidence/aws/rds_security_groups.json | Allowlist | 203.0.113.0/24, 198.51.100.0/24 | Yes | PrivateLink | mTLS | Yes | Isolated VPC |

---

## Sheet 5: Logging & Monitoring Configuration

### Purpose

Verify comprehensive logging enables incident detection, investigation, and regulatory compliance. "If you don't log it, it didn't happen" - and you can't investigate what you can't see.

**Success Criterion:** All Critical services log administrative actions and data access, retain logs ≥90 days (≥365 for Restricted data), forward logs to SIEM, and configure alerts for anomalous activity.

### What to Assess

For each service:
- Audit logging enabled (what events are logged)
- Log retention period (regulatory requirements)
- SIEM integration (centralized log collection)
- Alert configuration (security events, anomalies)
- Log integrity protection (tamper-proof logs)

### How to Assess

**Step 1: Verify Audit Logging**

| Log Type | What to Log | Regulatory Requirement |
|----------|-------------|------------------------|
| **Admin Actions** | User creation, permission changes, config changes | ISO 27001, SOC 2 |
| **Data Access** | Who accessed what data, when | GDPR, FADP, SOX |
| **Authentication Events** | Login success/failure, MFA events | All regulations |
| **API Calls** | API requests, responses, errors | DORA, NIS2 |
| **Security Events** | Firewall blocks, malware detection, DLP violations | NIS2, DORA |

**Where to Enable:**
- **AWS:** CloudTrail (API logs), VPC Flow Logs, S3 Access Logs
- **Azure:** Activity Log, Diagnostic Settings, NSG Flow Logs
- **GCP:** Cloud Audit Logs, VPC Flow Logs
- **Microsoft 365:** Unified Audit Log, Azure AD Sign-in Logs
- **SaaS:** Admin console → Audit Logs

**CIS Benchmark:** AWS 3.1 "Ensure CloudTrail is enabled in all regions"

**Step 2: Verify Log Retention**

| Data Classification | Minimum Retention | Regulatory Basis |
|---------------------|-------------------|------------------|
| **Restricted** | 365 days | GDPR, SOX, HIPAA |
| **Confidential** | 180 days | Industry best practice |
| **Internal** | 90 days | ISO 27001 baseline |
| **Public** | 30 days | Operational only |

**How to Check:**
- **Cloud Platforms:** Log storage bucket lifecycle policies
- **SIEM:** Retention settings in Splunk, Datadog, Azure Sentinel
- **SaaS:** Admin console → Audit log retention

**Step 3: Verify SIEM Integration**

| Integration Status | Description | Assessment |
|--------------------|-------------|------------|
| **Real-Time Forwarding** | Logs stream to SIEM within minutes | ✅ |
| **Batch Export** | Logs exported daily/weekly | ⚠️ Acceptable for Low criticality |
| **Manual Export** | Admin downloads logs on request | ❌ |
| **No Integration** | Logs only in service console | ❌ |

**Common SIEM Tools:**
- Splunk, Datadog, Azure Sentinel, Sumo Logic, Elastic SIEM

**Step 4: Verify Alert Configuration**

| Alert Type | Example Triggers | Evidence |
|------------|------------------|----------|
| **Failed Login Attempts** | >5 failures in 10 minutes | Alert rule config |
| **Privilege Escalation** | User granted Admin role | SIEM alert screenshot |
| **Data Exfiltration** | Large data download | DLP alert config |
| **Config Changes** | Encryption disabled, firewall rule changed | CloudTrail + SNS alert |
| **Anomalous Access** | Access from new country, unusual time | UEBA alert (if available) |

**Step 5: Complete Extended Columns**

| Column | Field | How to Assess | Evidence |
|--------|-------|---------------|----------|
| R | Audit Logging Enabled | Yes/Partial/No | Service logging config |
| S | Events Logged | Admin/Data/Auth/API/Security (checkboxes) | Log config export |
| T | Log Retention (Days) | Number (90, 180, 365, etc.) | Retention policy config |
| U | SIEM Integration | Real-Time/Batch/Manual/None | SIEM data source config |
| V | SIEM Tool | Splunk/Datadog/Sentinel/Other | SIEM screenshot |
| W | Alerts Configured | Yes/No | Alert rules export |

**Step 6: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| Full logging + Real-time SIEM + Alerts + ≥90d retention | ✅ | - |
| Full logging + Batch SIEM + Alerts | ⚠️ | "SIEM integration not real-time" |
| Partial logging (auth only, no data access) | ⚠️ | "Incomplete logging coverage" |
| Retention <90 days | ⚠️ | "Log retention below minimum (90 days)" |
| No SIEM integration | ❌ | "Logs not centralized - blind spot" |
| No logging enabled | ❌ | "No audit trail - critical gap" |

### Common Misconfigurations

❌ **Logging enabled but not monitored** - Logs exist but no one reviews them  
❌ **SIEM integration but no alerts** - Data collected but no actionable notifications  
❌ **Retention set to "forever"** - Storage costs explode, no lifecycle policy  
❌ **Logs not encrypted** - Sensitive logs stored in plaintext  
❌ **Log tampering possible** - No integrity protection (CloudTrail Log File Validation)  
❌ **Critical services not logged** - "Too much data" excuse (wrong!)  

### Example Entry

| A | B | C | D | E | F | G | H | I | R | S | T | U | V | W |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salesforce CRM | Salesforce Inc. | SaaS | Critical | Confidential | Production | No (Manual) | ✅ | /evidence/sfdc/logging_config.pdf | Yes | Admin, Data, Auth, API | 365 | Real-Time | Datadog | Yes |

---

## Sheet 6: Backup & Recovery Configuration

### Purpose

Verify backup and disaster recovery controls ensure business continuity. Ransomware doesn't care about your encryption if you can't restore data.

**Success Criterion:** All Critical services have daily backups, encrypted backups, tested recovery procedures (RTO/RPO validated), and geographically separate backup storage.

### What to Assess

For each service:
- Backup frequency (daily, hourly, continuous)
- Backup scope (full, incremental, differential)
- Backup encryption (at-rest, in-transit)
- Backup storage location (geographic separation)
- RTO (Recovery Time Objective) validation
- RPO (Recovery Point Objective) validation
- Disaster recovery testing frequency

### How to Assess

**Step 1: Verify Backup Frequency**

| Frequency | RPO | Use Case | Assessment |
|-----------|-----|----------|------------|
| **Continuous (Point-in-Time)** | Seconds | Critical databases | ✅ Best |
| **Hourly** | <1 hour | High-criticality data | ✅ |
| **Daily** | 24 hours | Standard services | ⚠️ Acceptable |
| **Weekly** | 7 days | Low-criticality archives | ⚠️ |
| **No Backups** | ∞ (unrecoverable) | Unacceptable | ❌ |

**DORA Requirement:** Article 28.7 requires annual DR testing for critical ICT services.

**Step 2: Verify Backup Encryption**

| Encryption Status | Assessment | Evidence |
|-------------------|------------|----------|
| **Encrypted at-rest + in-transit** | ✅ | Backup policy config |
| **Encrypted at-rest only** | ⚠️ | Document transit risk |
| **No encryption** | ❌ | Critical gap |

**Why It Matters:** Unencrypted backups = data breach if stolen.

**Step 3: Verify RTO/RPO Testing**

| Test Type | Frequency | What to Test | Evidence |
|-----------|-----------|--------------|----------|
| **Full DR Test** | Annual | Restore entire service in alternate region | Test report with timestamps |
| **Partial Recovery** | Quarterly | Restore sample data, verify integrity | Recovery log |
| **Backup Integrity** | Monthly | Verify backup files readable | Automated validation script |

**RTO/RPO Definitions:**
- **RTO (Recovery Time Objective):** How long to restore service (e.g., 4 hours)
- **RPO (Recovery Point Objective):** How much data loss acceptable (e.g., 1 hour)

**Test Evidence Must Include:**
- Start time (when recovery initiated)
- End time (when service restored)
- Data loss (time gap between backup and incident)
- Issues encountered (and how resolved)

**Step 4: Complete Extended Columns**

| Column | Field | How to Assess | Evidence |
|--------|-------|---------------|----------|
| R | Backup Frequency | Continuous/Hourly/Daily/Weekly/None | Backup policy config |
| S | Backup Scope | Full/Incremental/Differential | Backup job config |
| T | Backup Encrypted | Yes/No | Backup encryption status |
| U | Backup Storage Location | Same Region/Different Region/Multi-Region | Storage config |
| V | RTO (Hours) | Number | SLA document or test report |
| W | RPO (Hours) | Number | Backup frequency implies RPO |
| X | Last DR Test Date | Date | Test report |
| Y | DR Test Result | Pass/Fail/Partial | Test outcome |

**Step 5: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| Daily+ backup + Encrypted + DR tested annual + Geo-separate | ✅ | - |
| Daily backup + Encrypted + No DR test | ⚠️ | "DR test required (DORA compliance)" |
| Weekly backup only | ⚠️ | "Backup frequency inadequate for criticality" |
| Backup not encrypted | ❌ | "Unencrypted backups - data breach risk" |
| No backups | ❌ | "No backup configured - data loss risk" |

### Common Misconfigurations

❌ **Backups in same region as primary** - Regional disaster affects both  
❌ **Backup exists but restore never tested** - "Works in theory" ≠ works  
❌ **RTO/RPO assumptions not validated** - "Should take 4 hours" vs. actual 48 hours  
❌ **Ransomware can delete backups** - Immutable backups not configured  
❌ **Backup retention too short** - Malware detected after 90 days, backups only 30 days  
❌ **No backup monitoring** - Backups failing silently for months  

### Example Entry

| A | B | C | D | E | F | G | H | I | R | S | T | U | V | W | X | Y |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PostgreSQL (Production) | Amazon RDS | IaaS | Critical | Confidential | Production | Yes (Terraform) | ✅ | /evidence/aws/rds_backup_config.json | Continuous | Full (Daily) + Incremental | Yes | Multi-Region (us-east-1 → eu-west-1) | 4 | 0.5 | 15.10.2025 | Pass |

---

**END OF SECTION 4 PART 2: NETWORK, LOGGING, BACKUP**

## Evidence Collection Guide

### Evidence Principles

**Core Requirement:** Every ✅ (Compliant) status MUST link to config export or screenshot showing control enabled.

**Evidence Quality Standards:**
- **Current:** Configuration snapshot from within last 30 days
- **Complete:** Shows all required settings (not partial screenshot)
- **Authentic:** From official admin console or CLI export
- **Attributable:** Clear which service/environment it applies to
- **Reproducible:** Another admin could verify same config

### Evidence Types by Configuration Layer

| Layer | Evidence Type | Example Filename | How to Obtain |
|-------|---------------|------------------|---------------|
| **Identity** | MFA policy export, user MFA status report | `[Service]_MFA_Policy_20260120.json` | IdP console, admin report |
| **Data Protection** | Encryption config export | `[Service]_Encryption_Config_20260120.json` | Cloud console, CLI export |
| **Network** | Firewall rules export | `[Service]_Firewall_Rules_20260120.csv` | Network config export |
| **Logging** | SIEM integration config | `[Service]_SIEM_Config_20260120.json` | SIEM data source settings |
| **Backup** | Backup policy export, DR test report | `[Service]_Backup_Policy_20260120.json` | Backup console, test report PDF |

### Configuration Export Methods

**AWS (CLI):**
```bash
# S3 Bucket Encryption
aws s3api get-bucket-encryption --bucket my-bucket > s3_encryption.json

# Security Group Rules
aws ec2 describe-security-groups --group-ids sg-12345 > security_groups.json

# CloudTrail Configuration
aws cloudtrail describe-trails > cloudtrail_config.json

# IAM Policies
aws iam get-policy --policy-arn arn:aws:iam::123456789012:policy/MyPolicy > iam_policy.json
```

**Azure (CLI):**
```bash
# Storage Account Encryption
az storage account show --name mystorageaccount > storage_encryption.json

# Network Security Group
az network nsg show --name myNSG --resource-group myRG > nsg_rules.json

# Activity Log Diagnostic Settings
az monitor diagnostic-settings show --resource /subscriptions/xxx > logging_config.json
```

**Microsoft 365 (PowerShell):**
```powershell
# MFA Status Report
Get-MsolUser -All | Select DisplayName,UserPrincipalName,StrongAuthenticationMethods | Export-Csv mfa_status.csv

# DLP Policies
Get-DlpCompliancePolicy | Export-Csv dlp_policies.csv

# Audit Log Retention
Get-AdminAuditLogConfig | Export-Csv audit_config.csv
```

**Screenshots (When CLI Not Available):**
- **Required Elements:** Full URL, timestamp, service name, relevant settings visible
- **Format:** PNG or PDF (not JPEG - compression artifacts)
- **Annotation:** Highlight critical settings (use red box/arrow)

### Evidence Repository Structure

**Folder Organization:**
```
/ISMS/Evidence/A.5.23.3/
    ├── [Service_Name]/
    │   ├── Identity/
    │   │   ├── SSO_Config_20260120.json
    │   │   ├── MFA_Policy_20260120.json
    │   │   └── RBAC_Roles_20260120.csv
    │   ├── Data_Protection/
    │   │   ├── Encryption_AtRest_20260120.json
    │   │   ├── TLS_Config_20260120.txt
    │   │   └── DLP_Rules_20260120.xml
    │   ├── Network/
    │   │   ├── Firewall_Rules_20260120.csv
    │   │   └── IP_Allowlist_20260120.json
    │   ├── Logging/
    │   │   ├── Audit_Log_Config_20260120.json
    │   │   └── SIEM_Integration_20260120.png
    │   └── Backup/
    │       ├── Backup_Policy_20260120.json
    │       └── DR_Test_Report_20251015.pdf
```

**Naming Convention:** `[Service]_[ConfigArea]_[Setting]_YYYYMMDD.[ext]`

### Evidence Collection Checklist

**For Each Service, Gather:**

```
☐ Sheet 2 - Identity & Access
    ☐ SSO integration config (SAML metadata or OAuth config)
    ☐ MFA enforcement policy + user MFA status report
    ☐ RBAC role definitions and assignments
    ☐ Last access review report

☐ Sheet 3 - Data Protection
    ☐ Encryption at-rest config (algorithm, key management)
    ☐ TLS configuration (version, cipher suites)
    ☐ DLP policy export
    ☐ Data classification labels applied (sample files)

☐ Sheet 4 - Network Security
    ☐ Firewall rules export (security groups, NSGs)
    ☐ IP allowlist configuration
    ☐ VPN/PrivateLink configuration
    ☐ API authentication config

☐ Sheet 5 - Logging & Monitoring
    ☐ Audit log configuration (what's logged)
    ☐ Log retention settings
    ☐ SIEM integration config (data source)
    ☐ Alert rules export

☐ Sheet 6 - Backup & Recovery
    ☐ Backup policy config (frequency, scope)
    ☐ Backup encryption status
    ☐ DR test report (last annual test)
    ☐ RTO/RPO validation evidence
```

---

## Common Pitfalls & How to Avoid Them

### Top 10 Configuration Mistakes

**1. Assuming Vendor Defaults Are Secure**
- ❌ Problem: "It's a reputable vendor, defaults must be secure"
- ✅ Solution: Explicitly verify and harden every service
- **Example:** AWS S3 buckets default to "Block Public Access: OFF" (insecure)

**2. Configuration Drift Goes Undetected**
- ❌ Problem: Secure today, someone disables MFA next month, no one notices
- ✅ Solution: Enable drift detection (AWS Config, Azure Policy, GCP Security Command Center)
- **Example:** Quarterly assessment shows compliant, but MFA was disabled 2 months ago

**3. Production Configured But Not Dev/Test**
- ❌ Problem: "It's just dev, doesn't need encryption"
- ✅ Solution: Apply same security baseline across all environments
- **Example:** Dev database has production data copy but no encryption

**4. Logging Enabled But Not Monitored**
- ❌ Problem: Logs collected but no one looks at them
- ✅ Solution: Configure SIEM alerts, assign SOC to monitor
- **Example:** Attacker accessed data for 6 months, logs showed it but no alerts

**5. Backup Exists But Never Tested**
- ❌ Problem: "We have backups" (but restore never attempted)
- ✅ Solution: Annual DR test with documented RTO/RPO validation
- **Example:** Ransomware hit, backups corrupted (never validated integrity)

**6. Over-Reliance on Perimeter Security**
- ❌ Problem: "Our VPN is secure, don't need MFA inside"
- ✅ Solution: Defense-in-depth - assume breach, secure each layer
- **Example:** VPN compromised, attacker has unrestricted internal access

**7. Shared Admin Accounts**
- ❌ Problem: "admin@company.com" used by entire IT team
- ✅ Solution: Individual accounts with RBAC, audit trail per person
- **Example:** Malicious insider uses shared account, no accountability

**8. API Keys in Code Repositories**
- ❌ Problem: API key hardcoded in GitHub repo (now public)
- ✅ Solution: Use secret managers (AWS Secrets Manager, Azure Key Vault), scan repos
- **Example:** GitGuardian found 10,000+ exposed secrets on GitHub daily

**9. Encryption With Vendor-Managed Keys (For Restricted Data)**
- ❌ Problem: "It's encrypted" (but vendor controls keys)
- ✅ Solution: BYOK (Bring Your Own Key) for Restricted data
- **Example:** Vendor compromised, attacker decrypts all data

**10. Treating Compliance as One-Time Activity**
- ❌ Problem: Pass audit, never review configs again
- ✅ Solution: Quarterly reviews, continuous monitoring
- **Example:** Compliant at audit, 6 months later configuration drift makes you non-compliant

### Configuration-Specific Gotchas

**Identity & Access:**
- ⚠️ MFA enforced for users but not service accounts (API keys bypass MFA)
- ⚠️ SSO configured but local accounts still enabled (backdoor)
- ⚠️ Access reviews conducted but stale accounts not disabled

**Data Protection:**
- ⚠️ Encryption at-rest enabled but backups not encrypted
- ⚠️ TLS 1.2+ enforced but older versions accepted (downgrade attack)
- ⚠️ DLP configured but in audit mode only (detects but doesn't block)

**Network:**
- ⚠️ IP allowlist exists but includes 0.0.0.0/0 (defeats purpose)
- ⚠️ PrivateLink configured but public endpoint still accessible
- ⚠️ API rate limiting set to 100,000 req/sec (effectively unlimited)

**Logging:**
- ⚠️ Logging enabled but retention set to 7 days (regulatory requires 90+)
- ⚠️ SIEM integration exists but logs not actually flowing (broken connector)
- ⚠️ Alerts configured but sent to unmonitored email address

**Backup:**
- ⚠️ Backups run daily but backup validation never runs
- ⚠️ Backup stored in same region/account as primary (single point of failure)
- ⚠️ Ransomware protection not enabled (attacker can delete backups)

---

## Quality Checklist

### Pre-Submission Checklist

**Before Submitting for Approval, Verify:**

```
☐ COMPLETENESS
    ☐ All services from IMP-5.23.1 assessed (cross-check inventory)
    ☐ All 5 configuration layers (Sheets 2-6) completed
    ☐ All base columns (A-Q) populated
    ☐ All extended columns (R+) completed for each sheet
    ☐ All status flags set (✅/⚠️/❌/N/A)

☐ EVIDENCE QUALITY
    ☐ Every ✅ status links to config export or screenshot
    ☐ All evidence files exist and accessible
    ☐ All evidence is current (<30 days old)
    ☐ Config exports show complete settings (not partial)
    ☐ Screenshots show URL + timestamp
    ☐ Evidence organized in folder structure

☐ CONFIGURATION ACCURACY
    ☐ IaC (Terraform/CloudFormation) matches actual deployed config
    ☐ Manual config screenshots match CLI exports (if both available)
    ☐ Multi-environment configs documented separately (Prod vs. Dev)
    ☐ Configuration drift since last assessment documented

☐ GAP ANALYSIS
    ☐ Every ⚠️/❌ has Gap Description (Column J)
    ☐ Every gap has Remediation Needed (Yes/No)
    ☐ If remediation needed, Target Date populated (Column P)
    ☐ If gap accepted, Exception ID populated (Column L)
    ☐ All exceptions documented in risk register

☐ CONSISTENCY
    ☐ Base columns match IMP-5.23.1 (A-E)
    ☐ Service names consistent across all sheets
    ☐ Configuration aligns with IMP-5.23.2 vendor capabilities
    ☐ Jurisdictional risk config (Sheet 7) aligns with IMP-5.23.2 Sheet 7

☐ REGULATORY COMPLIANCE
    ☐ All Restricted/Confidential data: Encryption enabled (Sheet 3)
    ☐ All Critical services: MFA enforced (Sheet 2)
    ☐ All services: Audit logging ≥90 days retention (Sheet 5)
    ☐ DORA in-scope: Annual DR testing (Sheet 6)
    ☐ NIS2 requirements: All security measures documented

☐ DASHBOARD VALIDATION
    ☐ Sheet 8 formulas calculate correctly
    ☐ Overall compliance % reasonable (cross-check manually)
    ☐ Risk distribution makes sense (not all green or all red)
    ☐ Top gaps list matches actual data in Sheets 2-6

☐ EVIDENCE REGISTER
    ☐ All evidence files linked in Sheet 9
    ☐ All hyperlinks work (click each one)
    ☐ File naming follows convention
    ☐ Folder permissions correct (auditors can access)

☐ APPROVAL READINESS
    ☐ Sheet 10 blank and ready for approvers
    ☐ Configuration baseline documentation prepared
    ☐ Remediation plan ready (if gaps exist)
    ☐ IaC repository updated (if config managed as code)
```

### Configuration-Specific Quality Checks

**Sheet 2 (Identity):**
- ☐ MFA enforcement verified with user report (not just policy screenshot)
- ☐ SSO integration tested (sample user login)
- ☐ RBAC roles match least privilege principle
- ☐ Access review evidence shows actual review (not just policy)

**Sheet 3 (Data Protection):**
- ☐ Encryption algorithm verified (AES-256 or equivalent)
- ☐ TLS version tested (not assumed from documentation)
- ☐ DLP rules tested (sample violation triggers alert)
- ☐ Key rotation policy documented and followed

**Sheet 4 (Network):**
- ☐ IP allowlist doesn't include 0.0.0.0/0
- ☐ VPN/PrivateLink actually enforced (public access disabled)
- ☐ API authentication tested (unauthenticated call fails)
- ☐ Rate limiting validated with load test

**Sheet 5 (Logging):**
- ☐ Logs actually flowing to SIEM (check SIEM, not just config)
- ☐ Retention period validated (check oldest logs)
- ☐ Alerts tested (trigger sample alert, verify notification)
- ☐ Log integrity protection enabled (if available)

**Sheet 6 (Backup):**
- ☐ Backup actually runs (check last backup timestamp)
- ☐ Restore tested (not just backup creation)
- ☐ RTO/RPO documented from actual test (not assumptions)
- ☐ Backup encryption verified (attempt unencrypted restore - should fail)

---

**END OF SECTIONS 5-7: EVIDENCE, PITFALLS, QUALITY**

## Review & Approval Process

### Approval Workflow

**Standard Approval Chain:**

```
Step 1: Cloud Operations Review (Technical Accuracy)
          ↓
Step 2: Security Review (Risk Assessment)
          ↓
Step 3: Compliance Review (Regulatory Alignment)
          ↓
Step 4: CISO Approval (Risk Acceptance)
          ↓
Step 5: Archive & Implement (Config remediation, IaC updates)
```

**Timeline:** 3-5 business days from submission to final approval

### Approval Criteria

**Cloud Operations (Quality Gate 1):**
- ✅ Configuration exports accurate and current
- ✅ All critical controls verified (MFA, encryption, logging, backup)
- ✅ IaC (Terraform/CloudFormation) matches deployed config
- ❌ Reject if: Inaccurate config data, missing evidence, outdated exports

**Security (Quality Gate 2):**
- ✅ All Critical services meet security baseline
- ✅ Configuration gaps acceptable or remediation planned
- ✅ Defense-in-depth implemented across all layers
- ❌ Reject if: Critical service without MFA/encryption, unacceptable risk gap

**Compliance (Quality Gate 3):**
- ✅ DORA/NIS2/GDPR requirements met
- ✅ Audit logging and retention compliant
- ✅ Encryption for personal data enabled
- ❌ Reject if: Regulatory non-compliance, missing audit trail

**CISO (Final Approval):**
- ✅ Overall security posture acceptable
- ✅ Residual risks formally accepted
- ✅ Remediation plan funded and resourced

---

## Integration & Maintenance

### Integration with Other ISMS Documents

**Upstream Dependencies:**

| Document | Provides | Integration Point |
|----------|----------|-------------------|
| **IMP-5.23.1 (Inventory)** | Service list | Base columns A-E |
| **IMP-5.23.2 (Vendor DD)** | Vendor capabilities | What CAN be configured |

**Downstream Consumers:**

| Document | Needs | How It Gets It |
|----------|-------|----------------|
| **IMP-5.23.4 (Governance)** | Config baselines | Uses Sheet 2-6 for drift detection |
| **IMP-5.23.5 (Dashboard)** | Compliance metrics | Aggregates Sheet 8 data |

### Quarterly Review Process

**Every Quarter:**

**Week 1: Configuration Re-Export**
- Re-export all configs (CLI, admin console)
- Compare with last quarter (identify drift)
- Document configuration changes

**Week 2: Gap Validation**
- Verify previous gaps remediated
- Identify new gaps (new services, config changes)
- Update remediation plan

**Week 3: Evidence Update**
- Update evidence repository
- Re-validate critical controls
- Test SIEM integration still working

**Week 4: Approval & Reporting**
- Cloud Ops review
- Security/Compliance approval
- Update IMP-5.23.5 dashboard

**Triggers for Out-of-Cycle Review:**
- Critical config change (MFA disabled, encryption turned off)
- Security incident (config vulnerability exploited)
- New service deployment
- Regulatory change (DORA technical standards updated)

### Configuration Drift Monitoring

**Automated Drift Detection (Recommended):**

| Platform | Tool | What It Detects |
|----------|------|-----------------|
| **AWS** | AWS Config Rules | S3 encryption, security group changes, CloudTrail disabled |
| **Azure** | Azure Policy | Storage encryption, NSG rules, diagnostic settings |
| **GCP** | Security Command Center | Firewall rules, IAM changes, logging disabled |
| **Multi-Cloud** | Prisma Cloud, Wiz, CloudCustodian | Cross-cloud config drift |

**Alert on Critical Changes:**
- MFA policy changed
- Encryption disabled
- Firewall rule added (0.0.0.0/0)
- Audit logging disabled
- Backup policy changed

---

## Appendix

### Glossary (IMP-Specific Terms)

| Term | Definition |
|------|------------|
| **BYOK** | Bring Your Own Key - customer-managed encryption keys |
| **CIS Benchmark** | Center for Internet Security - industry-standard config baselines |
| **Configuration Drift** | Unintended changes to system configuration over time |
| **DLP** | Data Loss Prevention - detect and block sensitive data exfiltration |
| **IaC** | Infrastructure as Code - manage infrastructure via code (Terraform, CloudFormation) |
| **RBAC** | Role-Based Access Control - permissions assigned by job function/role |
| **RTO** | Recovery Time Objective - max acceptable downtime |
| **RPO** | Recovery Point Objective - max acceptable data loss |

### Security Baseline References

**CIS Benchmarks (Download):**
- https://www.cisecurity.org/cis-benchmarks
- AWS Foundations Benchmark v1.5
- Azure Foundations Benchmark v2.0
- GCP Foundations Benchmark v1.3
- Microsoft 365 Foundations Benchmark v3.0

**Cloud Provider Security Best Practices:**
- **AWS:** Well-Architected Framework Security Pillar
- **Azure:** Security Best Practices & Patterns
- **GCP:** Security Foundations Blueprint

### Configuration Compliance Tools

**Open Source:**
- **Prowler** (AWS security assessment)
- **ScoutSuite** (multi-cloud security auditing)
- **CloudCustodian** (cloud governance as code)
- **Checkov** (IaC static analysis)

**Commercial:**
- **Prisma Cloud** (Palo Alto Networks)
- **Wiz** (Cloud security platform)
- **Lacework** (Cloud security + compliance)

### Regulatory References

**For detailed regulatory requirements, see:**
- **ISMS-POL-00:** Regulatory Applicability Framework
- **ISMS-POL-A.5.19-23:** Supplier and Cloud Services Security Policy

---

**END OF SECTIONS 8-10: REVIEW, INTEGRATION, APPENDIX**

**Lines:** ~200 lines

---

# PART II: TECHNICAL SPECIFICATION

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

**END OF PART II: TECHNICAL SPECIFICATION**

---

**END OF COMPLETE DOCUMENT**
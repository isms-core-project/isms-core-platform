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
| **Target Audience** | IT Operations, Cloud Operations, DevOps Engineers, Cloud Security Engineers, Platform Engineering, DevSecOps Teams |
| **Assessment Type** | Technical Configuration Assessment |
| **Review Cycle** | Quarterly (with continuous monitoring) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification (Part II only) | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites & Preparation
  - Understanding the Assessment Sheets
  - Completing Each Sheet (Detailed Guidance)
  - Evidence Collection Guide
  - Common Pitfalls & How to Avoid Them
  - Quality Checklist
  - Review & Approval Process
  - Integration & Maintenance
  - Appendix & Glossary

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure (10 Sheets)
  - Sheet-by-Sheet Column Specifications
  - Validation Rules & Formulas
  - Cell Styling Reference
  - Integration Points

---

# PART I: USER COMPLETION GUIDE

## Section 1: Assessment Overview

### 1.1 Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.23.S3 - Secure Configuration & Deployment

#### What This Assessment Covers

This assessment evaluates the **security configuration** of ALL cloud services identified in your cloud service inventory (ISMS-IMP-A.5.23.S1). While the inventory tells you *what* services you use and vendor due diligence (ISMS-IMP-A.5.23.S2) tells you *who* provides them, this assessment answers the critical question:

**"Are your cloud services actually configured securely?"**

**In Scope:**
- ✅ Identity & Access Management (SSO, MFA, RBAC, privileged access)
- ✅ Data Protection (encryption at rest/transit, key management, DLP, classification)
- ✅ Network Security (IP restrictions, private connectivity, segmentation, WAF, DDoS)
- ✅ Logging & Monitoring (audit logs, SIEM integration, retention, alerting)
- ✅ Backup & Recovery (automated backups, tested recovery, encryption, retention)
- ✅ Multi-environment consistency (Production, Staging, Development, Test)
- ✅ Configuration evidence (screenshots, config exports, security scans, IaC templates)

**Out of Scope:**
- ❌ Service discovery (covered in IMP-A.5.23.1 - Inventory)
- ❌ Vendor contracts and certifications (covered in IMP-A.5.23.2 - Vendor DD)
- ❌ Ongoing governance processes (covered in IMP-A.5.23.4 - Governance)
- ❌ Application-level security (code reviews, SAST/DAST - separate A.8.25-8.28 controls)
- ❌ Physical datacenter security (vendor responsibility, verified via certifications in IMP-A.5.23.2)

**Geographic Scope:**
- All cloud services regardless of deployment region
- Multi-region deployments assessed per environment
- Jurisdictional configuration implications (e.g., data residency enforcement)

**Temporal Scope:**
- Point-in-time assessment (configuration state at assessment date)
- Quarterly reassessment cycle
- Configuration drift monitoring between assessments (optional but recommended)

---

### 1.2 Why This Assessment Matters

**The Cloud Configuration Problem:**

Cloud services offer thousands of configuration options. Default settings are rarely secure (designed for ease of use, not security). A single misconfiguration can expose your entire organization:

**Real-World Examples:**
- Capital One breach (2019): AWS S3 bucket misconfiguration → 100M+ customer records exposed
- Microsoft Power Apps breach (2021): Default public sharing → 38M records exposed
- Uber breach (2016): AWS keys in GitHub, no MFA on admin accounts → 57M users affected

**The Feynman Reality Check:**

*"What I cannot create, I do not understand."* — Richard Feynman

Applied to cloud security: **"What I have not verified with evidence, I do not know is secure."**

This assessment forces evidence-based validation:
- Don't just check a box saying "MFA is enabled"
- Provide a screenshot showing MFA enforcement policy
- Export the config showing which users have MFA active
- Demonstrate that privileged accounts cannot bypass MFA

**No cargo cult compliance.** Every "Compliant" status must be backed by verifiable evidence.

---

### 1.3 Who Should Use This Assessment

**Primary Users:**

| Role | Responsibility | Key Sheets |
|------|---------------|------------|
| **Cloud Operations / IT Operations** | Overall configuration ownership, multi-environment management | All Sheets 2-6 |
| **DevOps Engineers** | Infrastructure-as-Code (IaC), automation, CI/CD security | Sheets 2-6, Evidence Register |
| **Cloud Security Engineers** | Security baseline definition, configuration audits, remediation | All Sheets 2-6, Dashboard |
| **Platform Engineering** | Cloud platform standards, identity integration, monitoring | Sheets 2, 5 |
| **DevSecOps Teams** | Security-in-pipeline, automated scanning, policy-as-code | All Sheets 2-6 |
| **Identity & Access Management (IAM) Team** | SSO integration, MFA enforcement, RBAC design | Sheet 2 (Identity & Access) |
| **Network Security Team** | Firewall rules, private connectivity, segmentation | Sheet 4 (Network Security) |
| **Data Protection Officer (DPO)** | Encryption requirements, data classification, jurisdictional compliance | Sheet 3 (Data Protection), Sheet 7 (Jurisdictional Risk) |

**Supporting Roles:**

| Role | Contribution | Engagement Point |
|------|--------------|------------------|
| **Service Owners (Business)** | Define criticality, approve risk exceptions | Sheet metadata (Service Criticality, Data Classification) |
| **Compliance Team** | Verify regulatory requirements met (DORA, NIS2, GDPR) | Sheet 8 (Dashboard), Sheet 10 (Approval) |
| **Internal Audit** | Independent validation of configurations | All sheets (evidence verification) |
| **CISO** | Final approval, risk acceptance for gaps | Sheet 10 (Approval Sign-Off) |

**Prerequisites for Completion:**
- Technical knowledge: Cloud admin/engineer level
- Access: Admin console access to cloud services being assessed
- Time commitment: 2-4 hours per cloud service (depending on complexity)
- Tools: Screenshot capability, config export tools, security scanning tools

---

### 1.4 Assessment Outputs

**What You'll Produce:**

**1. Excel Workbook (10 Sheets):**
```
┌─────────────────────────────────────────────────────────────────┐
│           ISMS-IMP-A.5.23.S3 WORKBOOK STRUCTURE                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Sheet 1:  Instructions & Legend                                │
│            └─ How to use this workbook, status legend           │
│                                                                   │
│  Sheet 2:  Identity & Access Configuration                      │
│            └─ SSO, MFA, RBAC, PAM, JIT access, service accounts│
│                                                                   │
│  Sheet 3:  Data Protection Configuration                        │
│            └─ Encryption (rest/transit), CMK, DLP, classification│
│                                                                   │
│  Sheet 4:  Network Security Configuration                       │
│            └─ IP restrictions, private endpoints, WAF, DDoS     │
│                                                                   │
│  Sheet 5:  Logging & Monitoring Configuration                   │
│            └─ Audit logs, SIEM, 12-month retention, alerting   │
│                                                                   │
│  Sheet 6:  Backup & Recovery Configuration                      │
│            └─ Automated backups, tested recovery, RPO/RTO       │
│                                                                   │
│  Sheet 7:  Jurisdictional Risk                       │
│            └─ Data residency alignment, CLOUD Act implications  │
│                                                                   │
│  Sheet 8:  Summary Dashboard                                    │
│            └─ Compliance metrics by config area + environment   │
│                                                                   │
│  Sheet 9:  Evidence Register                                    │
│            └─ Screenshots, config exports, scan results tracking│
│                                                                   │
│  Sheet 10: Approval Sign-Off                                    │
│            └─ IT Ops, Security, CISO approval workflow          │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

**2. Evidence Package:**
- Configuration screenshots (with timestamps)
- Config export files (JSON, YAML, XML, Terraform/IaC)
- Security posture reports (Azure Secure Score, AWS Security Hub, GCP SCC)
- Vulnerability scan results
- Access review reports
- Backup test results
- SIEM integration confirmation

**3. Configuration Compliance Report:**
- Overall compliance percentage (target: ≥95%)
- Compliance by configuration area (Identity, Data, Network, Logging, Backup)
- Compliance by environment (Production, Staging, Development, Test)
- Gap analysis (non-compliant configurations + remediation plan)
- Risk summary (HIGH/CRITICAL findings requiring immediate action)

**4. Remediation Action Plan:**
- Gap description (what's misconfigured)
- Impact assessment (what's the risk?)
- Remediation steps (how to fix it)
- Responsible team (who owns it)
- Target date (when will it be fixed)
- Evidence requirements (how to prove it's fixed)

---

### 1.5 How This Fits in the A.5.19-23 Framework

**The 5-Assessment Architecture:**
```
┌─────────────────────────────────────────────────────────────────┐
│                   A.5.19-23 FRAMEWORK OVERVIEW                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐         │
│  │ IMP-5.23.1   │ → │ IMP-5.23.2   │ → │ IMP-5.23.3   │         │
│  │ INVENTORY    │   │ VENDOR DD    │   │  THIS DOC    │         │
│  │              │   │              │   │ CONFIG       │         │
│  │ "What?"      │   │ "Who?"       │   │ "How?"       │         │
│  └──────────────┘   └──────────────┘   └──────────────┘         │
│         │                   │                   │                │
│         └───────────────────┼───────────────────┘                │
│                             ▼                                    │
│                   ┌──────────────────┐                           │
│                   │  IMP-5.23.5      │                           │
│                   │  DASHBOARD       │                           │
│                   │  (Aggregation)   │                           │
│                   └──────────────────┘                           │
│                             ▲                                    │
│                             │                                    │
│                   ┌──────────────────┐                           │
│                   │  IMP-5.23.4      │                           │
│                   │  GOVERNANCE      │                           │
│                   │  (Ongoing)       │                           │
│                   └──────────────────┘                           │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

**Sequential Relationship:**

1. **IMP-A.5.23.1 (Inventory)** answers: "What cloud services do we use?"
   - Identifies services: Microsoft 365, AWS, Salesforce, etc.
   - Classifies by criticality, data sensitivity, cost
   - Output: List of services requiring configuration assessment

2. **IMP-A.5.23.2 (Vendor Due Diligence)** answers: "Are our vendors trustworthy?"
   - Evaluates vendor security certifications (ISO 27001, SOC 2)
   - Assesses contracts (DPA, liability, audit rights)
   - Checks data sovereignty (where is data stored?)
   - Output: Vendor risk profile (LOW/MEDIUM/HIGH)

3. **IMP-A.5.23.3 (THIS DOCUMENT)** answers: "Are services configured securely?"
   - Even a trustworthy vendor (LOW risk in IMP-5.23.2) can be insecure if misconfigured
   - Validates technical security controls (MFA, encryption, logging, backups)
   - Provides evidence of secure deployment
   - Output: Configuration compliance report

4. **IMP-A.5.23.4 (Governance)** answers: "Are we maintaining security over time?"
   - Ongoing monitoring (SLA performance, security incidents, config drift)
   - Vendor relationship management (QBRs, performance reviews)
   - Change management (service updates, contract renewals)
   - Output: Governance metrics, vendor scorecard

5. **IMP-A.5.23.5 (Dashboard)** answers: "What's our overall cloud security posture?"
   - Aggregates data from all assessments (IMP-5.23.1 through 5.23.4)
   - Executive summary (compliance %, top risks, trend analysis)
   - Output: Executive dashboard for CISO/leadership

**Critical Dependencies:**

**Upstream Dependency:**
- You MUST complete IMP-A.5.23.1 (Inventory) BEFORE starting this assessment
- Why? You need the authoritative list of services to assess
- The inventory provides: Service name, vendor, criticality, data classification
- Import this data into Sheet 2-6 of this workbook (don't duplicate data entry)

**Downstream Impact:**
- IMP-A.5.23.4 (Governance) uses your configuration data to monitor drift
- IMP-A.5.23.5 (Dashboard) aggregates your compliance metrics
- Both expect this assessment to be complete and current

---

### 1.6 Key Concepts & Terminology

**Configuration Management vs. Configuration Assessment:**

| Concept | Definition | This Assessment's Role |
|---------|------------|------------------------|
| **Configuration Management** | Ongoing process of defining, implementing, and maintaining system configurations | Provides *governance framework* (policies, standards) |
| **Configuration Assessment** | Point-in-time evaluation of whether configurations meet security requirements | This document: *validates compliance* with framework |
| **Configuration Baseline** | Documented set of security configuration requirements (CIS Benchmark, vendor hardening guide) | Sheet 2-6 checklist items define *expected baseline* |
| **Configuration Drift** | Divergence between actual configuration and approved baseline over time | Assessment detects drift; IMP-5.23.4 monitors it |
| **Configuration Evidence** | Objective proof that configuration meets requirements (screenshot, config export, scan result) | Sheet 9 (Evidence Register) *tracks all evidence* |

**Security Configuration Areas (Sheets 2-6):**

**Sheet 2: Identity & Access Configuration**
- **SSO (Single Sign-On):** Users authenticate via organizational identity provider (Entra ID, Okta) rather than vendor-specific passwords
- **MFA (Multi-Factor Authentication):** Requires 2+ factors (password + code/biometric) to log in
- **RBAC (Role-Based Access Control):** Permissions assigned by job function, not individuals
- **PAM (Privileged Access Management):** Enhanced controls for admin accounts
- **JIT (Just-In-Time Access):** Time-limited elevation of privileges (no permanent admins)
- **Service Accounts:** Non-human identities used by applications/automation

**Sheet 3: Data Protection Configuration**
- **Encryption at Rest:** Data encrypted when stored (AES-256 standard)
- **Encryption in Transit:** Data encrypted during transmission (TLS 1.2+)
- **CMK (Customer-Managed Keys):** Encryption keys controlled by customer, not vendor
- **Key Rotation:** Periodic replacement of encryption keys (every 90-365 days)
- **DLP (Data Loss Prevention):** Automated prevention of unauthorized data sharing
- **Classification Labels:** Metadata tags marking data sensitivity (Public, Internal, Confidential, Restricted)

**Sheet 4: Network Security Configuration**
- **IP Allowlisting:** Restrict access to specific IP addresses/ranges
- **Private Connectivity:** Non-internet connectivity (Azure Private Link, AWS PrivateLink, VPN)
- **Network Segmentation:** Isolation between environments (Prod vs. Dev) or zones (DMZ vs. internal)
- **WAF (Web Application Firewall):** Protection against OWASP Top 10 web attacks
- **DDoS Protection:** Mitigation against distributed denial-of-service attacks
- **Zero Trust:** "Never trust, always verify" - no implicit trust based on network location

**Sheet 5: Logging & Monitoring Configuration**
- **Audit Logging:** Recording of security-relevant events (logins, permission changes, data access)
- **SIEM Integration:** Export logs to Security Information and Event Management system
- **Log Retention:** How long logs are kept (12+ months required by most regulations)
- **Alerting:** Automated notifications for security events (failed logins, config changes)
- **Threat Detection:** AI/ML-based identification of anomalous behavior
- **Security Dashboard:** Real-time view of security posture (Azure Security Center, AWS Security Hub)

**Sheet 6: Backup & Recovery Configuration**
- **RPO (Recovery Point Objective):** Maximum acceptable data loss (e.g., 1 hour = lose max 1 hour of data)
- **RTO (Recovery Time Objective):** Maximum acceptable downtime (e.g., 4 hours = restore within 4 hours)
- **3-2-1 Rule:** 3 copies of data, 2 different media types, 1 offsite/offline copy
- **Backup Encryption:** Backups encrypted at rest (prevent data leakage from backup storage)
- **Tested Recovery:** Regular verification that backups can actually be restored (test != hope)
- **Immutable Backups:** Write-once-read-many (WORM) backups resistant to ransomware deletion

---

### 1.7 Configuration Assessment Philosophy

**Evidence-Based Validation:**

This assessment rejects "checkbox compliance" in favor of **evidence-based validation**:

❌ **Bad Approach (Checkbox):**
```
☑ Is MFA enabled?  [X] Yes  [ ] No
```

✅ **Good Approach (Evidence-Based):**
```
☑ Is MFA enabled?  
   Status: ✅ Compliant
   Evidence: 
     - Screenshot: MFA_Policy_Enforced_20260120.png
     - Config Export: conditional_access_policy.json
     - Verification: 347/347 users have MFA active (100%)
     - Last Verified: 2026-01-20
```

**The "How Do You Know?" Test:**

For every "Compliant" status, you should be able to answer:
- **How do you know it's compliant?** → "I have a screenshot showing the setting"
- **How current is your evidence?** → "Verified this morning"
- **Could an auditor verify it?** → "Yes, here's the evidence file"
- **What if the config changed?** → "Quarterly reassessment will catch drift"

**Configuration vs. Vendor Responsibility:**

**Shared Responsibility Model:**
```
┌─────────────────────────────────────────────────────────────────┐
│                   SHARED RESPONSIBILITY MATRIX                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  SaaS (e.g., Microsoft 365, Salesforce)                         │
│  ├─ Vendor: Infrastructure, platform, application code          │
│  └─ You: Access control, data classification, DLP, backup       │
│                                                                   │
│  PaaS (e.g., Azure App Service, AWS RDS)                        │
│  ├─ Vendor: Infrastructure, OS, runtime                         │
│  └─ You: App code, access, data encryption, network, logging    │
│                                                                   │
│  IaaS (e.g., AWS EC2, Azure VMs)                                │
│  ├─ Vendor: Physical datacenter, virtualization layer           │
│  └─ You: OS, apps, access, encryption, network, patching, etc.  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

**This Assessment Scope:**
- Evaluates configurations **YOU control** (not vendor's infrastructure)
- Example: You don't assess AWS's datacenter physical security (vendor responsibility)
- Example: You DO assess whether your S3 buckets have public access blocked (your responsibility)

---

### 1.8 Success Criteria

**What "Good" Looks Like:**

**Quantitative Targets:**

| Metric | Target | Rationale |
|--------|--------|-----------|
| **Overall Compliance** | ≥95% | Industry best practice, allows <5% acceptable exceptions |
| **Critical Services - Identity & Access** | 100% | Zero tolerance for MFA/SSO gaps on critical services |
| **Critical Services - Data Protection** | 100% | Zero tolerance for encryption gaps on restricted/confidential data |
| **Production Environment** | ≥98% | Production must meet higher standard than Dev/Test |
| **Logging Retention** | 100% | Regulatory requirement (12+ months), no exceptions |
| **Backup Testing** | 100% | Untested backups = no backups; must verify recovery works |
| **HIGH Risk Findings** | 0 | All HIGH risks must be remediated or formally accepted |
| **CRITICAL Risk Findings** | 0 | All CRITICAL risks must be remediated immediately |

**Qualitative Indicators:**

✅ **Strong Configuration Posture:**
- Every "Compliant" status has corresponding evidence (screenshot, config export, scan result)
- Multi-environment consistency (Prod/Stage/Dev have same security baseline)
- Infrastructure-as-Code (IaC) templates enforce security-by-default
- Automated scanning detects configuration drift within 24 hours
- Remediation action plan exists for all gaps with target dates
- Configuration baselines aligned with industry standards (CIS Benchmarks, vendor hardening guides)

❌ **Weak Configuration Posture:**
- "Compliant" claims without evidence ("trust us, it's enabled")
- Production more secure than Dev ("we'll harden it later" → never happens)
- Manual configuration with no IaC (configuration drift inevitable)
- No monitoring of configuration changes (drift goes undetected)
- Gap remediation plan is just "TODO" without dates/owners
- Custom configurations with no documented rationale

**Assessment Completion Criteria:**

Before submitting for approval (Sheet 10), verify:
```
☐ All cloud services from IMP-5.23.1 inventory are assessed
☐ All sheets (2-6) are complete for each service
☐ Every "Compliant" status has evidence documented in Sheet 9
☐ All "Non-Compliant" items have gaps documented + remediation plan
☐ Summary Dashboard (Sheet 8) shows compliance metrics
☐ Evidence files are stored in evidence repository (accessible to auditors)
☐ Cross-environment consistency verified (or deviations justified)
☐ Stakeholder reviews completed (IT Ops, Security)
☐ Ready for CISO final approval
```

---

### 1.9 Assessment Timeline

**Typical Timeline for ~10 Cloud Services:**
```
Week 1: Preparation & Training
  Day 1-2: Review this guide, identify assessment team, gather access credentials
  Day 3-5: Training on evidence collection tools, screenshot standards, IaC export

Week 2-3: Configuration Assessment (Sheets 2-6)
  Week 2: Assess critical services (Microsoft 365, AWS production, critical SaaS)
  Week 3: Assess medium/low criticality services

Week 4: Evidence Collection & Validation
  Day 1-3: Collect all screenshots, config exports, security scan reports
  Day 4-5: Upload evidence to repository, link in Sheet 9

Week 5: Gap Analysis & Remediation Planning
  Day 1-2: Review all "Non-Compliant" findings, assess impact
  Day 3-5: Develop remediation action plans (what, who, when, how)

Week 6: Review & Approval
  Day 1-2: Stakeholder review (IT Ops, Security, DevOps)
  Day 3: Incorporate feedback, finalize workbook
  Day 4-5: CISO review and approval

TOTAL: ~6 weeks for comprehensive assessment
```

**Accelerated Timeline** (if needed):
- Focus on Critical/High services first (80/20 rule)
- Parallel assessment by multiple team members (identity specialist, network specialist, etc.)
- Use automated config extraction tools (Terraform state, cloud config APIs)
- Can compress to 3-4 weeks with dedicated resources

**Ongoing Cycle:**
- **Quarterly:** Full reassessment (repeat Weeks 2-6)
- **Monthly:** Spot checks of critical configurations
- **Continuous:** Automated drift detection (if IaC/policy-as-code implemented)

---

**END OF SECTION 1: ASSESSMENT OVERVIEW**

## Section 2: Prerequisites & Preparation

### 2.1 Before You Start - Critical Checklist

**Complete these prerequisites BEFORE beginning the configuration assessment:**
```
MANDATORY PREREQUISITES (Cannot proceed without these):

☐ IMP-A.5.23.1 (Cloud Service Inventory) COMPLETED
  ├─ Why: Provides authoritative list of services to assess
  ├─ Data needed: Service name, vendor, criticality, data classification
  └─ Action: Export inventory list for import into this workbook

☐ Admin/Engineer-level access to cloud services
  ├─ Why: Need console access to view/export configurations
  ├─ Required permissions: Read access minimum, admin preferred for full visibility
  └─ Action: Request access via IT service desk if not already provisioned

☐ Evidence repository established
  ├─ Why: Need secure storage for screenshots, config exports, scan reports
  ├─ Location options: SharePoint, network file share, document management system
  └─ Action: Create folder structure: /Evidence/IMP-A.5.23.3/[YYYY-MM-DD]/

☐ Assessment team identified and available
  ├─ Why: Single person cannot assess all configuration areas effectively
  ├─ Team composition: Identity specialist, network specialist, cloud engineer, security analyst
  └─ Action: Schedule dedicated time blocks (2-4 hours per service × number of services)

☐ Training on evidence collection completed
  ├─ Why: Ensures consistent, high-quality evidence across team
  ├─ Topics: Screenshot best practices, config export formats, security scan tools
  └─ Action: Review Section 5 (Evidence Collection Guide) with entire team
```
```
HIGHLY RECOMMENDED (Can proceed without, but will be slower/harder):

☐ IMP-A.5.23.2 (Vendor Due Diligence) COMPLETED
  ├─ Why: Vendor risk profile informs configuration rigor (HIGH risk vendor = stricter config)
  ├─ Data needed: Vendor certifications, data residency requirements
  └─ Action: Reference Sheet 2 (Vendor Security Certifications) and Sheet 5 (Data Sovereignty)

☐ Configuration baseline/hardening guides obtained
  ├─ Why: Provides detailed checklist of what to assess
  ├─ Sources: CIS Benchmarks, Microsoft/AWS/GCP security baselines, vendor hardening guides
  └─ Action: Download relevant guides for each cloud service type

☐ Security scanning tools configured
  ├─ Why: Automated scanning provides objective evidence, faster than manual checks
  ├─ Tools: Azure Secure Score, AWS Security Hub, GCP Security Command Center, Prowler, ScoutSuite
  └─ Action: Enable native cloud security posture tools, run initial scans

☐ Infrastructure-as-Code (IaC) repository access
  ├─ Why: IaC templates (Terraform, ARM, CloudFormation) document infrastructure configuration
  ├─ Access: Git repository (GitHub, GitLab, Bitbucket, Azure DevOps)
  └─ Action: Clone repos, identify which services are IaC-managed vs. manually configured

☐ Previous assessment results (if this is a reassessment)
  ├─ Why: Enables comparison (configuration drift detection, remediation progress tracking)
  ├─ Location: Previous quarter's IMP-A.5.23.3 workbook
  └─ Action: Retrieve from evidence repository, review gap remediation status
```

---

### 2.2 Required Information Gathering

**Data Collection Preparation:**

Before opening the assessment workbook, gather the following information for each cloud service you'll assess:

#### 2.2.1 From IMP-A.5.23.1 (Cloud Service Inventory)

**Import these fields directly** (don't re-enter manually):

| Field | Usage in This Assessment | Example |
|-------|-------------------------|---------|
| **Cloud Service Name** | Unique identifier (Sheets 2-6, Column A) | "Microsoft 365 E5" |
| **Vendor Name** | Service provider (Sheets 2-6, Column B) | "Microsoft Corporation" |
| **Service Type** | SaaS/IaaS/PaaS classification (Sheets 2-6, Column C) | "SaaS" |
| **Service Criticality** | Risk-based prioritization (Sheets 2-6, Column E) | "Critical" |
| **Data Classification** | Sensitivity level (Sheets 2-6, Column F) | "Restricted" (contains PII) |
| **Annual Cost** | Budget context (not in workbook, but good to know) | "CHF 120,000/year" |
| **Service Owner** | Business accountability (contact for questions) | "HR Director" |

**How to Import:**
1. Open IMP-A.5.23.1 workbook
2. Go to Sheet 2 (Cloud Service Inventory)
3. Export columns A-H (Service Name through Service Owner)
4. Save as CSV: `Cloud_Services_Import_YYYYMMDD.csv`
5. Import into IMP-A.5.23.3 Sheet 2-6 base columns (A-F)

**IMPORTANT:** This prevents duplicate data entry and ensures consistency across assessments.

---

#### 2.2.2 From IMP-A.5.23.2 (Vendor Due Diligence)

**Reference these fields** (don't import, just cross-reference):

| Field | Usage in This Assessment | Why It Matters |
|-------|-------------------------|----------------|
| **Vendor Risk Rating** (Sheet 8) | Informs configuration rigor level | HIGH risk vendor → stricter config requirements |
| **ISO 27001 Certified?** (Sheet 2) | Baseline security expectations | Certified vendors should have secure defaults |
| **Data Residency** (Sheet 5) | Jurisdictional configuration verification | Must align with Sheet 7 (Jurisdictional Risk) of this assessment |
| **Customer-Managed Keys Available?** (Sheet 5) | Encryption configuration options | If available, should be enabled for restricted data |
| **Audit Rights** (Sheet 6) | Config audit evidence availability | Can request vendor-side config reports if needed |

**How to Reference:**
1. Open IMP-A.5.23.2 workbook
2. Go to Sheet 8 (Summary Dashboard)
3. Note vendor risk rating for each vendor
4. For HIGH risk vendors, apply enhanced configuration scrutiny:
   - Critical services: 100% compliance required (no exceptions)
   - Encryption: Customer-managed keys mandatory
   - Logging: Maximum retention period required
   - Network: Private connectivity mandatory (no public endpoints)

---

#### 2.2.3 From Cloud Service Admin Consoles

**Prepare admin access credentials:**

| Cloud Service | Admin Console URL | Required Permissions | MFA Required? |
|---------------|-------------------|---------------------|---------------|
| **Microsoft 365** | https://admin.microsoft.com | Global Reader (minimum), Global Admin (preferred) | Yes |
| **Azure** | https://portal.azure.com | Reader on subscriptions, Security Reader | Yes |
| **AWS** | https://console.aws.amazon.com | ViewOnlyAccess policy (minimum), SecurityAudit (preferred) | Yes |
| **Google Workspace** | https://admin.google.com | Super Admin (read-only mode acceptable) | Yes |
| **Salesforce** | https://[instance].salesforce.com | System Administrator | Yes |
| **[Other SaaS]** | [URL] | Admin or Security Admin role | Recommended |

**Access Request Process:**

If you don't have admin access:
```
1. Submit IT service desk ticket:
   - Title: "IMP-A.5.23.3 Configuration Assessment - Admin Access Required"
   - Details: "Need read-only admin access to [Service] for quarterly security configuration assessment per ISO 27001 Control A.5.23. Access required for [Date Range]. Will enable MFA."
   - Justification: "ISMS policy ISMS-POL-A.5.19-23-S5 Section 9 requires quarterly configuration validation."

2. Enable MFA immediately upon access provisioned
   - Download authenticator app (Microsoft Authenticator, Google Authenticator, Authy)
   - Register MFA device in service admin console
   - Test MFA login before starting assessment

3. Document access grant:
   - Who approved: [Name, Title]
   - Access level granted: [Reader/Admin]
   - Access expiry: [Date] (request 2-week access window for assessment)
   - Evidence: Save approval email in evidence repository
```

---

#### 2.2.4 Configuration Export Tools & Scripts

**Prepare these tools for automated config extraction:**

**Microsoft 365 / Azure:**
```powershell
# Install required PowerShell modules (run as admin)
Install-Module -Name Az -Force -AllowClobber
Install-Module -Name Microsoft.Graph -Force -AllowClobber
Install-Module -Name ExchangeOnlineManagement -Force -AllowClobber

# Test connectivity
Connect-AzAccount
Connect-MgGraph -Scopes "Directory.Read.All", "Policy.Read.All"
Connect-ExchangeOnline
```

**AWS:**
```bash
# Install AWS CLI
# macOS: brew install awscli
# Linux: sudo apt install awscli
# Windows: Download from https://aws.amazon.com/cli/

# Configure credentials
aws configure

# Test connectivity
aws sts get-caller-identity
```

**Google Cloud Platform:**
```bash
# Install gcloud CLI
# https://cloud.google.com/sdk/docs/install

# Authenticate
gcloud auth login

# Test connectivity
gcloud projects list
```

**Configuration Export Scripts:**

We provide sample scripts in `/Evidence/Scripts/` folder:

- `export_azure_config.ps1` - Azure subscription configuration export
- `export_aws_config.sh` - AWS account configuration export
- `export_m365_config.ps1` - Microsoft 365 tenant configuration export
- `export_gcp_config.sh` - GCP project configuration export

**Usage:**
```bash
# Example: Export Azure configuration
cd /Evidence/Scripts/
./export_azure_config.ps1 -SubscriptionId "xxx-xxx-xxx" -OutputPath "../IMP-A.5.23.3/2026-01-20/"

# Output: azure_config_export_20260120.json (upload to evidence repository)
```

---

### 2.3 Stakeholder Identification & Engagement

**Who Needs to Be Involved:**

#### 2.3.1 Core Assessment Team

| Role | Name | Responsibility | Time Commitment |
|------|------|---------------|-----------------|
| **Assessment Coordinator** | [Name] | Overall project management, workbook consolidation, approval workflow | 20-40 hours |
| **Identity Specialist** | [Name] | Sheet 2 (Identity & Access) assessment, SSO/MFA/RBAC validation | 10-20 hours |
| **Cloud Engineer (Primary)** | [Name] | Sheets 3-6 assessment (Data, Network, Logging, Backup), IaC review | 20-40 hours |
| **Cloud Engineer (Secondary)** | [Name] | Backup to primary, cross-validation, evidence collection | 10-20 hours |
| **Security Analyst** | [Name] | Security scan interpretation, gap analysis, risk assessment | 10-15 hours |
| **Network Engineer** | [Name] | Sheet 4 (Network Security) validation, firewall rule review | 5-10 hours |

**Kickoff Meeting Agenda** (1 hour):
```
1. Assessment Overview (10 min)
   - Review Control A.5.23 requirements
   - Explain assessment scope and timeline
   - Show example completed workbook

2. Roles & Responsibilities (15 min)
   - Assign sheets to team members
   - Define evidence quality standards
   - Establish communication channels (Teams/Slack)

3. Tool Training (20 min)
   - Demonstrate screenshot tools (Snipping Tool, Greenshot)
   - Show config export scripts
   - Walk through evidence repository folder structure

4. Timeline & Milestones (10 min)
   - Week 2-3: Configuration assessment
   - Week 4: Evidence collection
   - Week 5: Gap analysis
   - Week 6: Review & approval

5. Q&A (5 min)
```

---

#### 2.3.2 Supporting Stakeholders

**Service Owners (Business):**
- **When to engage:** When assessing criticality or data classification (already done in IMP-A.5.23.1)
- **What they provide:** Business context, service usage patterns, downtime tolerance (RTO)
- **Example:** HR Director for HRIS system, Sales Director for CRM

**IT Operations / Cloud Operations:**
- **When to engage:** Throughout assessment (they manage configurations)
- **What they provide:** Access to admin consoles, IaC templates, historical config changes
- **Example:** Cloud Platform Lead, Azure Administrator, AWS Solutions Architect

**Information Security Team:**
- **When to engage:** Gap analysis phase, risk assessment, exception requests
- **What they provide:** Security baseline standards, risk evaluation, compensating control approval
- **Example:** CISO, Security Architect, Security Operations Manager

**Compliance Team:**
- **When to engage:** Final review phase, regulatory alignment verification
- **What they provide:** Regulatory requirement mapping (DORA, NIS2, GDPR)
- **Example:** Compliance Officer, Data Protection Officer (DPO)

**Internal Audit:**
- **When to engage:** Final approval phase (if required by governance)
- **What they provide:** Independent validation, audit trail review
- **Example:** IT Audit Manager

---

### 2.4 Tool & Access Requirements

**Software Tools Checklist:**
```
☐ Microsoft Excel or Google Sheets
  └─ For: Opening and completing assessment workbook
  └─ Version: Excel 2016+ or Google Sheets (cloud-based)

☐ Screenshot Tool
  └─ Windows: Snipping Tool (built-in), Greenshot (free), Snagit (paid)
  └─ macOS: Screenshot utility (Cmd+Shift+4), CleanShot X (paid)
  └─ Linux: Spectacle, Flameshot
  └─ Requirement: Must support timestamped screenshots with annotation capability

☐ Configuration Export Tools (per cloud platform)
  └─ Azure: PowerShell (Az module, Microsoft.Graph module)
  └─ AWS: AWS CLI (awscli), optional: Prowler, ScoutSuite
  └─ GCP: gcloud CLI
  └─ Microsoft 365: PowerShell (ExchangeOnlineManagement, Microsoft.Graph)

☐ Security Scanning Tools
  └─ Azure: Azure Security Center / Microsoft Defender for Cloud (native)
  └─ AWS: AWS Security Hub (native), optional: Prowler, AWS Config
  └─ GCP: Security Command Center (native)
  └─ Multi-cloud: Wiz, Prisma Cloud, Orca Security (if licensed)

☐ JSON/YAML Viewer
  └─ For: Reading config export files
  └─ Options: VS Code (free), Notepad++ with JSON plugin, online: jsonviewer.stack.hu

☐ Infrastructure-as-Code (IaC) Tools
  └─ Terraform: terraform CLI (if using Terraform)
  └─ ARM Templates: Azure Portal template viewer
  └─ CloudFormation: AWS Console template viewer

☐ Document Repository Access
  └─ SharePoint, Google Drive, network file share
  └─ Permissions: Read/write access to /Evidence/IMP-A.5.23.3/ folder
```

---

### 2.5 Environment-Specific Considerations

**Multi-Environment Strategy:**

Most organizations have multiple environments:
```
┌─────────────────────────────────────────────────────────────────┐
│                    ENVIRONMENT ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Production (PROD)       - Live customer-facing systems          │
│    └─ Security Level: MAXIMUM (100% compliance required)        │
│                                                                   │
│  Staging (STAGE/UAT)     - Pre-production testing               │
│    └─ Security Level: HIGH (≥95% compliance, mirrors PROD)      │
│                                                                   │
│  Development (DEV)       - Active development work               │
│    └─ Security Level: MEDIUM (≥90% compliance, non-prod data)   │
│                                                                   │
│  Test (TEST/QA)          - Quality assurance testing            │
│    └─ Security Level: MEDIUM (≥90% compliance, test data only)  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

**Assessment Strategy per Environment:**

**Option 1: Separate Rows per Environment** (Recommended)
```
Cloud Service Name | Vendor | Service Type | Environment | ...
Microsoft 365      | Microsoft | SaaS     | Production  | ...
Microsoft 365      | Microsoft | SaaS     | N/A         | ... (single tenant, all envs)
AWS EC2            | Amazon    | IaaS     | Production  | ...
AWS EC2            | Amazon    | IaaS     | Staging     | ...
AWS EC2            | Amazon    | IaaS     | Development | ...
```

**When to use:**
- Service has materially different configurations per environment
- IaaS/PaaS services (different VMs, databases per environment)
- Need to track environment-specific compliance

**Option 2: Single Row with "All" Environment**
```
Cloud Service Name | Vendor | Service Type | Environment | ...
Google Workspace   | Google | SaaS        | All         | ...
Salesforce         | Salesforce | SaaS    | All         | ...
```

**When to use:**
- Service configuration is identical across all environments (typical for SaaS)
- Single tenant shared by all environments
- Reduces duplicate data entry

**Decision Matrix:**

| Service Type | Typical Approach | Rationale |
|--------------|------------------|-----------|
| **SaaS** (Microsoft 365, Salesforce, Google Workspace) | Single row (Environment: All) | Usually single tenant, same config everywhere |
| **IaaS** (AWS EC2, Azure VMs, GCP Compute) | Separate rows per environment | Different instances per environment with different configs |
| **PaaS** (Azure App Service, AWS RDS) | Separate rows per environment | Different app/database instances per environment |
| **Security Services** (SIEM, EDR, DLP) | Single row (Environment: All) | Typically monitors all environments with same config |

---

### 2.6 Integration with Previous Assessments

**Data Reuse from IMP-A.5.23.1 (Inventory):**

**Step 1: Export from IMP-A.5.23.1**
```
1. Open ISMS-IMP-A.5.23.S1_Inventory_[DATE].xlsx
2. Go to Sheet 2 (Cloud Service Inventory)
3. Select columns A-H (rows 5 onward, where data exists)
4. Copy to clipboard

OR

5. File → Save As → CSV (Comma delimited)
6. Save as: Cloud_Services_Export_YYYYMMDD.csv
```

**Step 2: Import into IMP-A.5.23.3**
```
1. Open ISMS-IMP-A.5.23.S3_SecureConfig_[DATE].xlsx
2. Go to Sheet 2 (Identity & Access Configuration)
3. Paste into columns A-F starting at row 7 (first data row)
4. Repeat for Sheets 3-6 (same data appears in all sheets)
5. Verify: Service names should be identical to inventory
```

**Step 3: Validate Data Integrity**
```
Cross-check:
☐ All services from inventory are present in IMP-A.5.23.3
☐ Service names match exactly (no typos)
☐ Criticality levels match
☐ Data classifications match
☐ If service is in IMP-A.5.23.3 but not in IMP-A.5.23.1 → Add to inventory first!
```

---

**Cross-Reference with IMP-A.5.23.2 (Vendor Due Diligence):**

**Use Case: Determine Configuration Rigor Level**
```python
# Pseudo-logic for configuration assessment rigor

IF vendor_risk_rating == "HIGH" (from IMP-A.5.23.2 Sheet 8):
    THEN apply_enhanced_config_requirements():
        - Encryption: Customer-managed keys MANDATORY
        - Network: Private connectivity MANDATORY
        - Logging: Maximum retention (365+ days) MANDATORY
        - MFA: Hardware tokens preferred over mobile app
        - Access Review: Monthly instead of quarterly

ELIF service_criticality == "Critical" (from IMP-A.5.23.1):
    THEN apply_critical_service_requirements():
        - Zero tolerance for gaps (100% compliance required)
        - No risk exceptions allowed
        - Quarterly assessment instead of annual

ELSE:
    THEN apply_standard_requirements():
        - Follow baseline checklist (Sheets 2-6)
        - Risk exceptions allowed with CISO approval
        - Annual assessment acceptable
```

**Practical Example:**
```
Service: Microsoft 365
  └─ From IMP-A.5.23.1: Criticality = "Critical", Data = "Restricted"
  └─ From IMP-A.5.23.2: Vendor Risk = "Medium", ISO 27001 = Yes, SOC 2 = Yes

Assessment Approach:
  ✓ High rigor required (Critical service with Restricted data)
  ✓ Encryption: Customer-managed keys preferred but not mandatory (Medium risk vendor)
  ✓ MFA: Enforce for all users (no exceptions)
  ✓ Network: IP allowlisting recommended but not mandatory
  ✓ Logging: 365-day retention minimum
  ✓ Backup: 3-2-1 rule with tested recovery
```

---

### 2.7 Assessment Readiness Checklist

**Final Pre-Flight Check:**

Before beginning Sheet 2 (Identity & Access Configuration), confirm:
```
READINESS CHECKLIST:

☐ PLANNING
  ├─ Assessment team identified and available
  ├─ Kickoff meeting completed
  ├─ Roles and responsibilities assigned
  └─ Timeline agreed upon (target completion date: _________)

☐ DATA
  ├─ IMP-A.5.23.1 (Inventory) data exported and ready to import
  ├─ IMP-A.5.23.2 (Vendor DD) vendor risk ratings noted
  ├─ Service criticality and data classification confirmed
  └─ Multi-environment strategy decided (separate rows vs. "All")

☐ ACCESS
  ├─ Admin console access provisioned for all services
  ├─ MFA enabled on all admin accounts
  ├─ PowerShell/CLI tools installed and tested
  └─ Security scanning tools configured

☐ TOOLS
  ├─ Screenshot tool ready (with timestamp capability)
  ├─ Config export scripts tested
  ├─ Evidence repository folder structure created
  └─ Excel/Google Sheets workbook opened and editable

☐ STANDARDS
  ├─ Configuration baseline guides downloaded (CIS, vendor hardening)
  ├─ Evidence quality standards reviewed (Section 5 of this guide)
  ├─ Team trained on evidence collection best practices
  └─ Checklist items (Sheets 2-6) reviewed and understood

☐ COMMUNICATION
  ├─ Stakeholders notified (Service Owners, IT Ops, Security)
  ├─ Weekly status update meeting scheduled
  ├─ Communication channel established (Teams/Slack/Email)
  └─ Escalation path defined for blockers

☐ GO/NO-GO DECISION
  ├─ If ALL items above are checked → PROCEED to Section 3
  ├─ If 1-2 items missing → Address gaps first, then proceed
  └─ If 3+ items missing → STOP, complete prerequisites before continuing
```

**Decision Point:**

✅ **GREEN (Ready to Proceed):**
- All mandatory prerequisites complete
- Core team available and trained
- Admin access provisioned
- Evidence repository ready

⚠️ **YELLOW (Proceed with Caution):**
- Some access still pending (can start with accessible services)
- Training partially complete (pair junior with senior team member)
- Evidence repository not fully set up (create during assessment)

🛑 **RED (Do Not Proceed):**
- IMP-A.5.23.1 inventory not complete (no authoritative service list)
- Zero admin access (cannot view configurations to assess)
- No evidence repository (nowhere to store evidence)
- Team unavailable (no resources to conduct assessment)

---

### 2.8 Common Preparation Pitfalls

**Mistakes to Avoid:**

❌ **Pitfall 1: Starting Without IMP-A.5.23.1 Inventory**
```
Problem: "We'll just assess the services we know about"
Result: Shadow IT not assessed, incomplete compliance picture
Fix: Complete IMP-A.5.23.1 first, use as authoritative source
```

❌ **Pitfall 2: Single Person Attempting All Sheets**
```
Problem: "I'll do the whole assessment myself over a weekend"
Result: Burnout, inconsistent quality, missed configurations
Fix: Distribute work across specialists (identity, network, cloud engineering)
```

❌ **Pitfall 3: No Evidence Storage Plan**
```
Problem: "We'll save screenshots on our laptops"
Result: Evidence lost, not accessible to auditors, inconsistent organization
Fix: Create evidence repository BEFORE starting, use standardized folder structure
```

❌ **Pitfall 4: Assessing Dev Environment Like Production**
```
Problem: "Dev should be as secure as Prod, right?"
Result: Unrealistic standards, wasted effort on low-risk environment
Fix: Risk-based approach (Prod: 100%, Dev: 90% acceptable)
```

❌ **Pitfall 5: Assuming Default Configs Are Secure**
```
Problem: "It's Microsoft/AWS/Google, surely it's secure by default"
Result: Public S3 buckets, disabled MFA, no logging retention
Fix: Evidence-based validation ("trust but verify" → actually verify!)
```

---

**END OF SECTION 2: PREREQUISITES & PREPARATION**

## Section 3: Understanding the Assessment Sheets

### 3.1 Workbook Architecture Overview

**The 10-Sheet Structure:**
```
┌─────────────────────────────────────────────────────────────────┐
│              IMP-A.5.23.3 WORKBOOK ARCHITECTURE                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  LAYER 1: ORIENTATION                                            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Sheet 1: Instructions & Legend                           │   │
│  │          How to use workbook, status symbols, evidence   │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  LAYER 2: CONFIGURATION ASSESSMENT (Core)                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Sheet 2: Identity & Access Configuration                │   │
│  │          SSO, MFA, RBAC, PAM, JIT, service accounts      │   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │ Sheet 3: Data Protection Configuration                  │   │
│  │          Encryption (rest/transit), CMK, DLP, labels     │   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │ Sheet 4: Network Security Configuration                 │   │
│  │          IP restrictions, private endpoints, WAF, DDoS   │   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │ Sheet 5: Logging & Monitoring Configuration             │   │
│  │          Audit logs, SIEM, 12-month retention, alerts    │   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │ Sheet 6: Backup & Recovery Configuration                │   │
│  │          Automated backups, tested recovery, RPO/RTO     │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  LAYER 3: REGULATORY & JURISDICTIONAL                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Sheet 7: Jurisdictional Risk Assessment                 │   │
│  │          Data residency alignment, CLOUD Act impact      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  LAYER 4: SYNTHESIS & EVIDENCE                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Sheet 8: Summary Dashboard                              │   │
│  │          Compliance metrics, environment comparison      │   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │ Sheet 9: Evidence Register                              │   │
│  │          Screenshots, config exports, scan results       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│  LAYER 5: APPROVAL                                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Sheet 10: Approval Sign-Off                             │   │
│  │          IT Ops, Security, CISO approval workflow        │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

**Design Philosophy:**

Each sheet follows a **consistent pattern** to reduce cognitive load:

1. **Header:** Sheet purpose and policy requirement reference
2. **Guidance Row:** Key policy section, assessment question
3. **Column Headers (Row 5):** Base columns (A-Q) + Extended columns (R-X)
4. **Data Entry (Rows 7-30):** Yellow-highlighted input cells with validation dropdowns
5. **Checklist (Below Data):** Verification checklist with status tracking
6. **Evidence Links:** References to Sheet 9 (Evidence Register)

---

### 3.2 Sheet 1: Instructions & Legend

**Purpose:** Onboarding and reference guide for all users

**Key Components:**

| Component | Content | Use Case |
|-----------|---------|----------|
| **Document Header** | Assessment ID, version, related policy, review cycle | Quick identification and governance tracking |
| **How to Use** | 9-step workflow from inventory to approval | First-time user orientation |
| **Status Legend** | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Understanding compliance symbols throughout workbook |
| **Evidence Examples** | Screenshots, config exports, scan reports, IaC templates | Guidance on acceptable evidence types |
| **Contact Info** | Assessment coordinator, IT Ops lead, Security contact | Who to ask for help |

**When to Reference:**
- First time using the workbook (read entirely)
- Forgotten status symbol meaning (quick lookup)
- Unsure what evidence is acceptable (examples section)
- Need help (contact info)

**Implementer Perspective:**
*"This sheet answers 90% of 'how do I fill this out?' questions. Read it once thoroughly, then bookmark for reference."*

**Auditor Perspective:**
*"I check this sheet to verify the assessment coordinator understood the methodology. If instructions were followed, the assessment is likely high quality."*

---

### 3.3 Sheet 2: Identity & Access Configuration

**Assessment Question:** *"Are identity and access controls properly configured for your cloud services?"*

**Policy Requirement:** ISMS-POL-A.5.19-23-S5 Section 9.1
- SSO integration via organizational IdP
- MFA enforced for all users (mandatory for privileged accounts)
- RBAC implemented with least privilege
- Privileged access is time-limited (JIT/PAM)
- Access reviews performed quarterly

**Column Structure:**

**Base Columns (A-Q):** Standard across all sheets
- A-F: Service identification (from IMP-5.23.1 import)
- G: Configuration Item (specific setting assessed, e.g., "Conditional Access Policy - MFA Enforcement")
- H: Status (✅/⚠️/❌/N/A)
- I-Q: Gap management (evidence location, remediation needed, target date, etc.)

**Extended Columns (R-X):** Identity-specific
- R: SSO Integrated (Yes/No/Partial/N/A)
- S: MFA Enforced (Yes - All Users / Yes - Admins Only / No / N/A)
- T: RBAC Implemented (Yes/Partial/No/N/A)
- U: Privileged Access JIT (Yes/No/Planned/N/A)
- V: Service Accounts Inventoried (Yes/Partial/No/Unknown)
- W: Last Access Review (Date)
- X: Admin Account Count (Number)

**Key Assessment Items:**
```
✓ SSO configured via Entra ID, Okta, or similar IdP
✓ MFA enforced for ALL users (not just admins)
✓ MFA mandatory for privileged accounts (cannot be bypassed)
✓ RBAC roles documented and implemented (role matrix exists)
✓ Least privilege applied (users have minimum necessary permissions)
✓ Service accounts inventoried with documented owners
✓ Privileged access is time-limited (PIM/PAM for JIT elevation)
✓ Access reviews performed quarterly (evidence: access review report)
✓ Default accounts disabled or renamed (no "admin", "root" active)
✓ Failed login alerting configured (5+ failed attempts = alert)
```

**Common Findings:**

| Finding | Impact | Evidence Gap | Remediation |
|---------|--------|--------------|-------------|
| MFA enforced only for admins, not all users | HIGH | User list showing MFA status | Enable conditional access policy requiring MFA for all users |
| No JIT for privileged access (permanent admins) | MEDIUM | Admin group membership list | Implement PIM (Azure) or AWS SSO temporary elevation |
| Access reviews not performed | MEDIUM | No access review reports in last 90 days | Schedule quarterly access review, document process |
| Service accounts without documented owners | LOW | Service account inventory incomplete | Complete inventory, assign owners, document in CMDB |

**Implementer Perspective:**
*"Identity is foundational. If this sheet isn't 100% compliant, stop and fix it before moving to other sheets. Everything else depends on 'who can access what.'"*

**Auditor Perspective:**
*"I verify MFA enforcement by requesting a user list export. If ANY user lacks MFA, status cannot be 'Compliant.' No exceptions for executives ('too inconvenient') - that's a control failure."*

---

### 3.4 Sheet 3: Data Protection Configuration

**Assessment Question:** *"Are data protection controls properly configured for your cloud services?"*

**Policy Requirement:** ISMS-POL-A.5.19-23-S5 Section 9.2
- Encryption at rest (AES-256 minimum)
- Encryption in transit (TLS 1.2+ minimum)
- Customer-managed keys for restricted data
- Key rotation policy implemented
- Data classification labels applied and enforced
- DLP configured for sensitive data types

**Extended Columns (R-X):** Data protection-specific
- R: Encryption At Rest (Yes - Provider Key / Yes - CMK / No / N/A)
- S: Encryption In Transit (Yes - TLS 1.3 / Yes - TLS 1.2 / No / N/A)
- T: Encryption Algorithm (AES-256 / AES-128 / ChaCha20 / Other / Unknown)
- U: Key Management (Provider Managed / Customer Managed - HSM / Customer Managed - Software / N/A)
- V: Classification Labels (Yes - Enforced / Yes - Optional / No / N/A)
- W: DLP Configured (Yes/Partial/No/N/A)
- X: Key Rotation Period (90 days / 180 days / 365 days / Manual / N/A)

**Key Assessment Items:**
```
✓ TLS 1.2+ enforced for all connections (TLS 1.0/1.1 disabled)
✓ AES-256 encryption at rest enabled (verify in service config)
✓ Encryption keys stored securely (HSM or cloud KMS)
✓ Key rotation policy implemented (automatic or documented manual)
✓ Data classification labels applied (Public/Internal/Confidential/Restricted)
✓ DLP rules configured for PII, credit cards, PHI (if applicable)
✓ Data masking for non-production environments (Prod data ≠ Dev/Test)
✓ Secure deletion process documented (crypto-shredding preferred)
```

**Customer-Managed Keys (CMK) Decision Matrix:**

| Data Classification | Vendor Risk (IMP-5.23.2) | CMK Required? | Rationale |
|---------------------|-------------------------|---------------|-----------|
| **Restricted** | Any | YES | Highest sensitivity = strongest protection |
| **Confidential** | HIGH | YES | High risk vendor + sensitive data = CMK mandatory |
| **Confidential** | MEDIUM/LOW | RECOMMENDED | Risk-based decision, document if not using CMK |
| **Internal** | Any | NO | Provider-managed keys acceptable |
| **Public** | Any | N/A | No encryption requirements for public data |

**Evidence Requirements:**

| Configuration | Required Evidence | Format | Example Filename |
|---------------|------------------|--------|------------------|
| Encryption at rest | Screenshot of encryption settings | PNG/JPG | `AWS_S3_Encryption_Settings_20260120.png` |
| Encryption in transit | SSL/TLS scan report or config export | PDF/JSON | `SSLLabs_Scan_api.example.com_20260120.pdf` |
| CMK usage | Key management console screenshot | PNG/JPG | `Azure_KeyVault_CMK_Config_20260120.png` |
| DLP rules | DLP policy export | JSON/XML | `M365_DLP_Policy_Export_20260120.json` |
| Key rotation | Key rotation policy doc or config | PDF/JSON | `AWS_KMS_KeyRotation_Policy_20260120.json` |

**Implementer Perspective:**
*"Encryption is table stakes. If data is 'Restricted' or 'Confidential,' CMK is non-negotiable. Provider-managed keys mean the vendor can decrypt your data - acceptable only for low-sensitivity data."*

**Auditor Perspective:**
*"I verify encryption by requesting config exports (not just screenshots). A screenshot can be Photoshopped; a JSON config export from the API is harder to fake. Always cross-check claims with technical evidence."*

---

### 3.5 Sheet 4: Network Security Configuration

**Assessment Question:** *"Are network security controls properly configured for your cloud services?"*

**Policy Requirement:** ISMS-POL-A.5.19-23-S5 Section 5.2
- Access restrictions (IP allowlisting for admin interfaces)
- Secure connectivity (private endpoints, VPN, no public exposure where avoidable)
- Network segmentation (production isolated from dev/test)
- Web application firewall (WAF) for web-facing services
- DDoS protection enabled

**Extended Columns (R-X):** Network-specific
- R: IP Restrictions (Yes - Allowlist / Yes - Geo / No / N/A)
- S: Private Connectivity (Yes - Private Link / Yes - VPN / Public Only / N/A)
- T: Network Segmentation (Yes/Partial/No/N/A)
- U: WAF Enabled (Yes/No/N/A)
- V: DDoS Protection (Yes - Advanced / Yes - Basic / No / N/A)
- W: Firewall Rules Documented (Yes/Partial/No/N/A)
- X: Public Endpoints Count (Number ≥0)

**Key Assessment Items:**
```
✓ IP allowlisting configured for admin access (not accessible from internet)
✓ Private endpoints used where available (Azure Private Link, AWS PrivateLink)
✓ VPN/ExpressRoute for sensitive workloads (not public internet)
✓ Network segmentation between environments (Prod ≠ Dev VNets)
✓ WAF configured for web applications (OWASP Top 10 protection)
✓ DDoS protection enabled (Advanced tier for critical services)
✓ Firewall rules documented and reviewed (least privilege network access)
✓ Public endpoints minimized and justified (business requirement documented)
```

**Network Security Maturity Levels:**
```
┌─────────────────────────────────────────────────────────────────┐
│              NETWORK SECURITY MATURITY MODEL                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Level 1: BASIC (Minimum Acceptable)                            │
│    ✓ Services accessible via public internet                    │
│    ✓ TLS encryption for data in transit                         │
│    ✓ Basic DDoS protection (cloud provider default)             │
│    Risk: MEDIUM-HIGH (exposed to internet attacks)              │
│                                                                   │
│  Level 2: INTERMEDIATE (Recommended)                            │
│    ✓ IP allowlisting for admin interfaces                       │
│    ✓ WAF enabled for web applications                           │
│    ✓ Network segmentation (Prod isolated from Dev)              │
│    Risk: MEDIUM (reduced attack surface)                        │
│                                                                   │
│  Level 3: ADVANCED (Best Practice)                              │
│    ✓ Private endpoints (no public exposure)                     │
│    ✓ VPN/ExpressRoute for all access                            │
│    ✓ Advanced DDoS protection                                   │
│    ✓ Zero Trust architecture (continuous verification)          │
│    Risk: LOW (defense in depth)                                 │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

**Service Type Guidance:**

| Service Type | Network Security Requirement | Example |
|--------------|----------------------------|---------|
| **Admin Interface** | IP allowlist MANDATORY (office IP only) | Azure Portal, AWS Console, admin.microsoft.com |
| **Customer-Facing Web App** | WAF MANDATORY, DDoS Advanced RECOMMENDED | Public website, customer portal, API gateway |
| **Internal Application** | Private connectivity MANDATORY, no public access | HR system, finance app, internal wiki |
| **Database/Storage** | Private endpoint MANDATORY, no public access | Azure SQL, AWS RDS, storage accounts |
| **API (B2B)** | Mutual TLS, IP allowlist, or API key required | Partner integrations, vendor APIs |

**Implementer Perspective:**
*"Default to 'deny all, allow by exception.' Every public endpoint is an attack vector. Justify public access with business requirement; otherwise, use private connectivity."*

**Auditor Perspective:**
*"I run port scans on documented 'private' endpoints. If I can access from the internet, it's not private - that's a critical finding. Always verify with independent testing."*

---

### 3.6 Sheet 5: Logging & Monitoring Configuration

**Assessment Question:** *"Are logging and monitoring controls properly configured for your cloud services?"*

**Policy Requirement:** ISMS-POL-A.5.19-23-S5 Section 9.3
- Audit logging enabled for all security-relevant events
- Logs exported to organizational SIEM
- Log retention ≥12 months (365 days minimum)
- Security alerts configured and routed to SOC/Security team
- Threat detection active

**Extended Columns (R-X):** Logging-specific
- R: Audit Logging Enabled (Yes - All Events / Yes - Security Only / No / N/A)
- S: SIEM Integrated (Yes/Planned/No/N/A)
- T: Alerting Configured (Yes/Partial/No/N/A)
- U: Log Retention (Days) (365+ / 180 / 90 / 30 / <30 / Unknown)
- V: Threat Detection Active (Yes/Partial/No/N/A)
- W: Security Dashboard (Yes/No/N/A)
- X: Last Log Review Date (Date)

**Key Assessment Items:**
```
✓ All security-relevant events logged (logins, permission changes, data access)
✓ Logs exported to organizational SIEM (Splunk, Sentinel, Chronicle, etc.)
✓ Log retention ≥12 months (365 days minimum, per GDPR/SOX/PCI requirements)
✓ Security alerts configured (failed logins, privilege escalation, unusual access)
✓ Alert notification to SOC/Security team (not just email to admin)
✓ Threat detection enabled (Azure Defender, AWS GuardDuty, GCP Security Command Center)
✓ Security dashboard accessible (real-time visibility into security posture)
✓ Logs reviewed regularly (quarterly minimum, monthly for critical services)
```

**Logging Retention Requirements:**

| Regulation/Standard | Minimum Retention | Applies To | Rationale |
|---------------------|------------------|------------|-----------|
| **GDPR** | 12 months | EU personal data | Breach investigation (Art. 33: 72-hour notification) |
| **PCI DSS** | 12 months (current + 3 months archive) | Payment card data | Fraud investigation requirement |
| **SOX** | 7 years | Financial systems | Audit trail for financial reporting |
| **HIPAA** | 6 years | Healthcare data | Compliance investigation timeframe |
| **ISO 27001** | 12 months (recommended) | All systems | Incident investigation best practice |
| **ISMS Policy** | **12 months minimum** | All cloud services | Harmonized across regulations |

**SIEM Integration Verification:**
```
How to Verify SIEM Integration:

1. Check cloud service log export configuration
   Azure: Diagnostic Settings → Log Analytics / Event Hub
   AWS: CloudTrail → S3 → Lambda → SIEM
   GCP: Cloud Logging → Pub/Sub → SIEM
   M365: Unified Audit Log → SIEM connector

2. Verify logs are actually arriving in SIEM
   - Run SIEM query: source="azure_activity" earliest=-24h
   - Should return recent events (< 24 hours old)
   - If no results → integration broken

3. Evidence: Screenshot of SIEM query results showing cloud logs

Common Failure: Config says "logs enabled" but SIEM connector is broken.
Always verify end-to-end: Cloud → SIEM → Dashboard.
```

**Implementer Perspective:**
*"Logging is your security camera system. If it's not recording (logs disabled) or tapes are overwritten too quickly (<12 months retention), you can't investigate incidents. Budget for SIEM storage costs."*

**Auditor Perspective:**
*"I request a SIEM query showing logs from 11 months ago. If the query returns 'no data,' retention policy is not compliant. Screenshots of config settings are insufficient - prove it with actual data."*

---

### 3.7 Sheet 6: Backup & Recovery Configuration

**Assessment Question:** *"Are backup and recovery controls properly configured for your cloud services?"*

**Policy Requirement:** ISMS-POL-A.5.19-23-S5 Section 5.2
- Automated backups enabled
- Backup frequency aligned with RPO (Recovery Point Objective)
- Tested recovery procedures (not just backup, but restore)
- Backup encryption enabled
- Appropriate backup retention (align with data retention policy)

**Extended Columns (R-X):** Backup-specific
- R: Backup Enabled (Yes/No/N/A)
- S: Backup Frequency (Continuous / Daily / Weekly / Monthly / N/A)
- T: Backup Retention (365 days / 90 days / 30 days / 7 days / N/A)
- U: Backup Encryption (Yes/No/Unknown/N/A)
- V: Last Recovery Test (Date)
- W: RPO (Hours) (0-1h / 1-4h / 4-24h / >24h / Unknown)
- X: RTO (Hours) (0-1h / 1-4h / 4-24h / >24h / Unknown)

**Key Assessment Items:**
```
✓ Backup enabled (automated, not manual)
✓ Backup frequency meets RPO (e.g., hourly backup for 1-hour RPO)
✓ Backup retention meets data retention policy (align with IMP-5.23.2 contracts)
✓ Backup encryption enabled (backups are as sensitive as production data)
✓ Last recovery test within 90 days (quarterly testing minimum)
✓ Recovery procedures documented (runbook exists, not tribal knowledge)
✓ 3-2-1 backup rule followed (3 copies, 2 media types, 1 offsite/offline)
✓ Immutable backups (WORM) for ransomware protection
```

**RPO/RTO Decision Matrix:**

| Service Criticality | Acceptable RPO | Acceptable RTO | Backup Frequency | Recovery Testing Frequency |
|---------------------|---------------|---------------|-----------------|---------------------------|
| **Critical** | ≤1 hour | ≤4 hours | Hourly or continuous | Monthly |
| **High** | ≤4 hours | ≤24 hours | Every 4-6 hours | Quarterly |
| **Medium** | ≤24 hours | ≤48 hours | Daily | Semi-annually |
| **Low** | ≤7 days | ≤7 days | Weekly | Annually |

**3-2-1 Backup Rule:**
```
┌─────────────────────────────────────────────────────────────────┐
│                        3-2-1 BACKUP RULE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  3 Copies of Data:                                               │
│    1. Production data (primary)                                  │
│    2. Local backup (same datacenter, fast recovery)              │
│    3. Offsite backup (different datacenter, disaster recovery)   │
│                                                                   │
│  2 Different Media Types:                                        │
│    - Disk (fast, for recent backups)                             │
│    - Tape/Object Storage (slow, for long-term retention)         │
│    OR Cloud + On-Prem (hybrid approach)                          │
│                                                                   │
│  1 Offsite/Offline Copy:                                         │
│    - Different geographic region (not affected by local disaster)│
│    - Air-gapped or immutable (ransomware cannot delete)          │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

**Recovery Testing Evidence:**

| Test Type | Frequency | Evidence Required | Pass Criteria |
|-----------|-----------|------------------|---------------|
| **File-level restore** | Quarterly | Recovery log, restored file screenshot | Single file recovered within RTO |
| **Database restore** | Quarterly | Recovery log, database integrity check | DB online and functional within RTO |
| **Full service recovery** | Annually | Recovery runbook, end-to-end test report | Entire service restored and verified within RTO |
| **Disaster recovery drill** | Annually (critical services) | DR test report, business continuity validation | Service restored to DR site, users functional |

**Implementer Perspective:**
*"Backups without tested recovery = false sense of security. I've seen organizations discover during a real incident that their backups were corrupted. Test recovery quarterly, not just when disaster strikes."*

**Auditor Perspective:**
*"I ask for the last recovery test report. If it's >90 days old or doesn't exist, backup status cannot be 'Compliant.' Config showing 'backup enabled' is not enough - prove you can restore."*

---

### 3.8 Sheet 7: Jurisdictional Risk Assessment

**Assessment Question:** *"Does the service's configuration align with jurisdictional risk mitigation requirements?"*

**Policy Requirement:** ISMS-POL-A.5.19-23-S5 Section 4 (Data Sovereignty), cross-reference IMP-A.5.23.2 Sheet 7

**Purpose:** 
While IMP-A.5.23.2 Sheet 7 assesses *vendor* jurisdictional risk (where is vendor headquartered, CLOUD Act exposure), this sheet assesses whether the *service configuration* actually mitigates those risks.

**Key Assessment Items:**
```
✓ Data residency configuration aligns with vendor DPA requirements (IMP-5.23.2 Sheet 5)
✓ If vendor has US nexus: EU Data Boundary enabled (Microsoft, AWS, etc.)
✓ If vendor has US nexus + restricted data: Customer-managed keys (CMK) active
✓ Data processing region matches contractual commitment (verify config vs. contract)
✓ Cross-border data transfer minimized (no unnecessary data replication to foreign regions)
✓ Subprocessor data access restricted (e.g., Microsoft support cannot decrypt CMK data)
```

**Cross-Reference with IMP-A.5.23.2:**

| IMP-A.5.23.2 Finding | IMP-A.5.23.3 Configuration Requirement | Verification |
|---------------------|---------------------------------------|--------------|
| Vendor HQ: United States | Enable EU Data Boundary (if available) | Config screenshot showing data residency = EU |
| CLOUD Act exposure: Potential | Implement CMK for restricted data | Key Vault showing customer-managed keys active |
| Data residency: US (DPA says EU) | **CRITICAL GAP** - Misalignment | Escalate immediately - contractual violation |
| No SCCs in contract | Cannot process EU personal data | Do not deploy until contract updated |

**Implementer Perspective:**
*"This sheet prevents 'contract says data stays in EU, but config shows data in US' gaps. Always verify configuration matches contractual commitments."*

**Auditor Perspective:**
*"I cross-check IMP-5.23.2 Sheet 5 (Data Sovereignty contract terms) against this sheet's config evidence. If they don't match, it's a critical finding - breach of contract and potential GDPR violation."*

---

### 3.9 Sheet 8: Summary Dashboard

**Purpose:** Aggregated compliance metrics across all configuration areas and environments

**Auto-Calculated Metrics:**

**Table 1: Compliance by Configuration Area**
```
Configuration Area          | Total Services | ✅ Compliant | ⚠️ Partial | ❌ Non-Compliant | Compliance %
Identity & Access           | 12             | 10           | 1          | 1                | 83.3%
Data Protection             | 12             | 11           | 1          | 0                | 91.7%
Network Security            | 12             | 9            | 2          | 1                | 75.0%
Logging & Monitoring        | 12             | 12           | 0          | 0                | 100%
Backup & Recovery           | 10             | 8            | 1          | 1                | 80.0%
Jurisdictional Risk         | 12             | 10           | 2          | 0                | 83.3%
──────────────────────────────────────────────────────────────────────────────────────────────
OVERALL                     | 70             | 60           | 7          | 3                | 85.7%
```

**Table 2: Compliance by Environment**
```
Environment     | Services | ✅ Compliant | ⚠️ Partial | ❌ Non-Compliant | Compliance %
Production      | 30       | 28           | 2          | 0                | 93.3%
Staging         | 20       | 18           | 1          | 1                | 90.0%
Development     | 15       | 10           | 3          | 2                | 66.7%
Test            | 5        | 4            | 1          | 0                | 80.0%
──────────────────────────────────────────────────────────────────────────────────────────────
OVERALL         | 70       | 60           | 7          | 3                | 85.7%
```

**Risk Heatmap:**
```
CRITICAL Findings: 0
HIGH Findings: 3 (requires immediate remediation)
  - Service: AWS EC2 Production | Issue: No MFA on admin accounts
  - Service: Salesforce | Issue: No backup recovery test in 120 days
  - Service: Azure SQL | Issue: No network segmentation (accessible from dev environment)

MEDIUM Findings: 7 (remediation within 30 days)
LOW Findings: 0
```

**Implementer Perspective:**
*"Dashboard is your executive summary. If overall compliance <90%, you have work to do. Focus on HIGH/CRITICAL findings first."*

**Auditor Perspective:**
*"I verify dashboard formulas link to actual sheet data. Manually count ✅ in Sheet 2-6 and compare to dashboard - if they don't match, formulas are broken."*

---

### 3.10 Sheet 9: Evidence Register

**Purpose:** Central tracking of all evidence files supporting configuration assessments

**Structure:**

| Column | Header | Purpose | Example |
|--------|--------|---------|---------|
| A | Evidence ID | Unique identifier | EV-SCD-001 |
| B | Sheet Reference | Which assessment sheet | Sheet 2 (Identity & Access) |
| C | Cloud Service Name | Service assessed | Microsoft 365 |
| D | Configuration Item | Specific setting | MFA Enforcement Policy |
| E | Evidence Type | Format | Screenshot |
| F | Evidence Filename | File name | M365_MFA_Policy_20260120.png |
| G | Evidence Location | Storage path | /Evidence/IMP-A.5.23.3/2026-01-20/Identity/ |
| H | Collection Date | When evidence collected | 2026-01-20 |
| I | Collected By | Who collected evidence | John Doe (Cloud Engineer) |
| J | Status | Evidence quality | ✅ Verified |

**Evidence Quality Validation:**

| Status | Meaning | Criteria |
|--------|---------|----------|
| ✅ **Verified** | Evidence is current, complete, and accessible | Timestamp <30 days, file exists in repository, clearly shows config setting |
| ⚠️ **Needs Update** | Evidence is outdated | Timestamp >90 days old, configuration may have drifted |
| ❌ **Missing** | Evidence referenced but file not found | Broken link, file deleted, never uploaded |
| 📝 **Draft** | Evidence collected but not yet verified | Pending review by assessment coordinator |

**Implementer Perspective:**
*"Treat this like a library catalog. Every screenshot, config export, scan report gets an entry. If it's not in the register, it doesn't count as evidence."*

**Auditor Perspective:**
*"I randomly select 10 evidence entries and verify files exist at documented locations. If >2 are missing, the entire assessment's credibility is questioned."*

---

### 3.11 Sheet 10: Approval Sign-Off

**Purpose:** Formal approval workflow with stakeholder sign-offs

**Approval Sequence:**
```
Stage 1: IT OPERATIONS REVIEW
  ☐ Reviewed By: [Name, Title]
  ☐ Review Date: [Date]
  ☐ Configuration Accuracy: ☐ Verified  ☐ Issues Found
  ☐ Comments: [Free text]
  
Stage 2: SECURITY TEAM REVIEW  
  ☐ Reviewed By: [Name, Title]
  ☐ Review Date: [Date]
  ☐ Security Posture: ☐ Acceptable  ☐ Requires Remediation
  ☐ Comments: [Free text]

Stage 3: CISO APPROVAL
  ☐ Approved By: [CISO Name]
  ☐ Approval Date: [Date]
  ☐ Risk Acceptance: ☐ Approved  ☐ Approved with Conditions  ☐ Rejected
  ☐ Conditions: [If approved with conditions, specify remediation requirements]
  ☐ Executive Comments: [Free text]

NEXT REVIEW DETAILS:
  ☐ Next Review Date: [Date] (typically +90 days for quarterly cycle)
  ☐ Review Responsible: [Name, Title]
  ☐ Special Considerations: [E.g., "Focus on backup recovery testing"]
```

**Implementer Perspective:**
*"Don't submit for approval until you're confident in your data quality. Rejected assessments waste everyone's time and damage credibility."*

**Auditor Perspective:**
*"I verify all sign-off stages are complete with actual signatures/dates. Missing approvals = assessment is incomplete and cannot be used for compliance evidence."*

---

**END OF SECTION 3: UNDERSTANDING THE ASSESSMENT SHEETS**

## Section 4: Completing Each Sheet - Detailed Guidance

### 4.1 General Workflow for All Configuration Sheets (2-6)

**Before diving into individual sheets, understand the common workflow:**
```
STEP 1: Import Base Data
  ├─ Copy columns A-F from IMP-A.5.23.1 (Inventory)
  ├─ Service Name, Vendor, Type, Criticality, Data Classification
  └─ Environment determination (Production, Staging, Development, Test, or All)

STEP 2: Assess Configuration
  ├─ Open admin console for cloud service
  ├─ Navigate to relevant configuration area (Identity, Encryption, Network, etc.)
  ├─ Complete extended columns (R-X) based on actual configuration
  └─ Determine overall Status (Column H): ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / N/A

STEP 3: Collect Evidence
  ├─ Screenshot: Configuration screen (with timestamp visible)
  ├─ Config Export: JSON/YAML/XML file showing programmatic config
  ├─ Security Scan: Report from native tools (Azure Secure Score, AWS Security Hub)
  └─ Document evidence location in Column I (Evidence Location)

STEP 4: Document Gaps (if any)
  ├─ Column J: Gap Description (what's missing/misconfigured)
  ├─ Column K: Remediation Needed (Yes/No)
  ├─ Column N: Compensating Controls (temporary mitigations)
  ├─ Column P: Target Remediation Date (when will it be fixed)
  └─ Columns L-M: Exception/Risk ID (if formally accepted)

STEP 5: Complete Checklist
  ├─ Below data rows (typically starting row 33)
  ├─ Check off each requirement (☑ or ☐)
  ├─ Document status: ✅ / ⚠️ / ❌ / N/A
  └─ Note evidence type for each checklist item

STEP 6: Link to Evidence Register
  ├─ For each piece of evidence, create entry in Sheet 9
  ├─ Assign Evidence ID (EV-SCD-001, EV-SCD-002, etc.)
  └─ Reference Evidence ID in Column I (Evidence Location)
```

**Quality Check Before Moving to Next Sheet:**
```
☐ All services from inventory are present
☐ Extended columns (R-X) completed for each service
☐ Status (Column H) reflects actual configuration (not aspirational)
☐ Evidence collected and stored in repository
☐ Gaps documented with remediation plans
☐ Checklist below data rows completed
☐ Evidence register entries created
```

---

### 4.2 Sheet 2: Identity & Access Configuration - Step-by-Step

**Configuration Area:** SSO, MFA, RBAC, Privileged Access, Service Accounts

#### Step 1: Import Base Data and Set Configuration Item

**Example Row Setup:**

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| Microsoft 365 | Microsoft | SaaS | All | Critical | Restricted | **Conditional Access Policy - MFA Enforcement** |

**Column G (Configuration Item):** Be specific about WHAT you're assessing:

✅ **Good Examples:**
- "Conditional Access Policy - MFA Enforcement for All Users"
- "Azure AD Privileged Identity Management (PIM) Configuration"
- "RBAC Role Assignment - Least Privilege Validation"
- "Service Principal Inventory and Ownership"

❌ **Bad Examples:**
- "Identity" (too vague)
- "Access Control" (which aspect?)
- "Settings" (meaningless)

---

#### Step 2: Assess SSO Integration (Column R)

**What to Check:**

For **SaaS Services** (Microsoft 365, Salesforce, Google Workspace):
```
1. Navigate to admin console → Authentication Settings
2. Verify: "Sign-in via SSO" or "SAML 2.0 Federation"
3. Check identity provider: Should be organizational IdP (Entra ID, Okta, OneLogin)
4. NOT vendor's native authentication (local passwords)
```

**Microsoft 365 Example:**
```powershell
# PowerShell verification
Connect-MgGraph -Scopes "Organization.Read.All"
Get-MgOrganization | Select-Object -Property Id, DisplayName

# Check if federated (SSO) vs. managed (local passwords)
Get-MgDomain | Select-Object Id, AuthenticationType

# Expected Output:
# AuthenticationType: Federated (✅ Good - SSO enabled)
# AuthenticationType: Managed (❌ Bad - local passwords still used)
```

**Evidence Required:**
- Screenshot: Admin console showing SSO configuration
- Config Export: `Get-MgDomain` output (PowerShell)
- Evidence File: `M365_SSO_Config_20260120.png`, `M365_Domain_Auth_Export_20260120.txt`

**Column R Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Yes** | SSO configured, ALL users authenticate via IdP | Screenshot + config export showing 100% SSO |
| **Partial** | SSO configured but some users still use local passwords | User list showing mixed auth types |
| **No** | No SSO, everyone uses service-specific passwords | Screenshot showing native auth only |
| **N/A** | Service doesn't support SSO (rare for modern SaaS) | Vendor documentation stating no SSO capability |

---

#### Step 3: Assess MFA Enforcement (Column S)

**What to Check:**
```
1. Navigate to MFA policy settings
2. Verify: MFA required for ALL users, not just admins
3. Check enforcement: "Enforced" not "Enabled" (users can't opt out)
4. Validate exceptions: Should be ZERO (or documented emergency access accounts only)
```

**Microsoft 365 Example:**
```powershell
# Check conditional access policies for MFA
Connect-MgGraph -Scopes "Policy.Read.All"
Get-MgIdentityConditionalAccessPolicy | Where-Object {$_.GrantControls.BuiltInControls -contains "mfa"}

# Verify user MFA status
Get-MgUser -All | Select-Object DisplayName, UserPrincipalName | ForEach-Object {
    Get-MgUserAuthenticationMethod -UserId $_.UserPrincipalName
}

# Export to CSV for evidence
Get-MgUser -All | Select DisplayName, @{N='MFAEnabled';E={(Get-MgUserAuthenticationMethod -UserId $_.UserPrincipalName).Count -gt 1}} | Export-Csv MFA_Status_20260120.csv
```

**AWS Example:**
```bash
# Check IAM user MFA status
aws iam get-account-summary | jq '.SummaryMap | {AccountMFAEnabled, MFADevices}'

# List users WITHOUT MFA (should be empty!)
aws iam list-users --output json | jq -r '.Users[] | select(.PasswordLastUsed != null) | .UserName' | while read user; do
    mfa_devices=$(aws iam list-mfa-devices --user-name "$user" --output json | jq '.MFADevices | length')
    if [ "$mfa_devices" -eq 0 ]; then
        echo "❌ $user has NO MFA"
    fi
done
```

**Evidence Required:**
- Screenshot: MFA policy showing "Enforced for All Users"
- Config Export: User list with MFA status (100% should have MFA)
- Evidence File: `M365_MFA_Policy_20260120.png`, `MFA_User_Status_Export_20260120.csv`

**Column S Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Yes (All Users)** | MFA enforced for 100% of users | User export showing 100% MFA enrollment |
| **Yes (Admins Only)** | ❌ **NOT COMPLIANT** - Regular users can skip MFA | User export showing only admins have MFA |
| **No** | ❌ **CRITICAL GAP** - No MFA enforcement | Policy screenshot showing MFA optional |
| **N/A** | Service has no users (API-only service) | Architecture doc showing no interactive logins |

**CRITICAL:** "Yes (Admins Only)" = ⚠️ Partial compliance at best. Modern policy requires MFA for ALL users.

---

#### Step 4: Assess RBAC Implementation (Column T)

**What to Check:**
```
1. Navigate to Role Assignments / Access Control (IAM)
2. Verify: Users assigned roles based on job function, not individual permissions
3. Check for over-privileged users: No "Owner" or "Global Admin" unless justified
4. Validate role documentation: Role matrix exists defining who gets what role
```

**Azure Example:**
```powershell
# Export all role assignments
Connect-AzAccount
Get-AzRoleAssignment | Select-Object DisplayName, RoleDefinitionName, Scope | Export-Csv Azure_RBAC_Assignments_20260120.csv

# Check for "Owner" role (should be minimal)
Get-AzRoleAssignment | Where-Object {$_.RoleDefinitionName -eq "Owner"} | Format-Table DisplayName, Scope

# Verify custom roles are documented
Get-AzRoleDefinition | Where-Object {$_.IsCustom -eq $true}
```

**AWS Example:**
```bash
# List IAM users and their attached policies
aws iam list-users --output json | jq -r '.Users[].UserName' | while read user; do
    echo "User: $user"
    aws iam list-attached-user-policies --user-name "$user" --output table
done

# Check for overly permissive policies (AdministratorAccess)
aws iam list-users --output json | jq -r '.Users[].UserName' | while read user; do
    admin_check=$(aws iam list-attached-user-policies --user-name "$user" --output json | jq '.AttachedPolicies[] | select(.PolicyName == "AdministratorAccess")')
    if [ ! -z "$admin_check" ]; then
        echo "⚠️ $user has AdministratorAccess"
    fi
done
```

**Evidence Required:**
- Screenshot: Role assignment page showing RBAC structure
- Config Export: Complete role assignment list (CSV format)
- Role Matrix Document: Excel/Word doc defining roles (Reader, Contributor, Admin, etc.)
- Evidence File: `Azure_RBAC_Screenshot_20260120.png`, `Azure_RBAC_Assignments_20260120.csv`, `RBAC_Role_Matrix_v2.xlsx`

**Column T Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Yes** | RBAC fully implemented, documented, least privilege applied | Role matrix + assignment export showing proper segregation |
| **Partial** | RBAC exists but some users have excessive permissions | Assignment export showing over-privileged users identified |
| **No** | ❌ No RBAC, everyone is admin or no role structure | Evidence showing lack of role-based access |
| **N/A** | Service has single admin account (not multi-user) | Vendor documentation or architecture showing single-admin design |

---

#### Step 5: Assess Privileged Access Management (Column U)

**What to Check: JIT (Just-In-Time) Access**
```
1. Verify: Admin rights are NOT permanent
2. Check for PIM (Azure), AWS SSO with temporary elevation, or equivalent
3. Validate: Admin access requires approval and is time-limited (e.g., 8 hours)
4. Review audit logs: Evidence of JIT activation and deactivation
```

**Azure PIM Example:**
```powershell
# Check if PIM is enabled
Connect-AzureAD
Get-AzureADMSPrivilegedRoleDefinition

# List eligible role assignments (JIT-enabled)
Get-AzureADMSPrivilegedRoleAssignment -ProviderId "aadRoles" -ResourceId (Get-AzureADTenantDetail).ObjectId

# Check activation history (who elevated, when)
Get-AzureADMSPrivilegedRoleAssignmentRequest -ProviderId "aadRoles" -ResourceId (Get-AzureADTenantDetail).ObjectId -Filter "requestType eq 'UserAdd'" | Select-Object SubjectId, RoleDefinitionId, AssignmentState, Schedule
```

**AWS SSO Example:**
```bash
# Check if SSO permission sets use time-limited sessions
aws sso-admin list-permission-sets --instance-arn <SSO_INSTANCE_ARN> --output json | jq '.PermissionSets[]' | while read ps; do
    echo "Permission Set: $ps"
    aws sso-admin describe-permission-set --instance-arn <SSO_INSTANCE_ARN> --permission-set-arn "$ps" --output json | jq '.PermissionSet.SessionDuration'
done

# Recommended: SessionDuration should be PT8H (8 hours) or less, not PT12H (permanent)
```

**Evidence Required:**
- Screenshot: PIM dashboard or AWS SSO permission set config
- Config Export: Eligible role assignments (who can request admin)
- Audit Log: Recent PIM activations (proving JIT is actually used)
- Evidence File: `Azure_PIM_Config_20260120.png`, `PIM_Eligible_Roles_20260120.csv`, `PIM_Activation_Log_20260120.csv`

**Column U Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Yes** | JIT/PAM fully implemented, no permanent admins | PIM/PAM config + audit log showing time-limited access |
| **No** | ❌ Permanent admin accounts exist | Role assignment showing "Permanent" not "Eligible" |
| **Planned** | ⚠️ JIT planned but not yet implemented | Project plan + target date for PIM deployment |
| **N/A** | Service has no privileged accounts or is API-only | Architecture doc showing no admin concept |

**RED FLAG:** If service criticality = "Critical" and JIT = "No" → This is a HIGH risk finding.

---

#### Step 6: Assess Service Accounts (Column V)

**What to Check:**
```
1. Inventory all service accounts (non-human identities)
2. Verify: Each service account has documented owner
3. Check: Service accounts use certificate/key auth, not passwords
4. Validate: Service accounts follow least privilege (minimal permissions)
5. Review: Service accounts are excluded from MFA (they can't do MFA) but use strong auth
```

**Microsoft 365 Example:**
```powershell
# List all service principals (app registrations)
Connect-MgGraph -Scopes "Application.Read.All"
Get-MgServicePrincipal -All | Select-Object Id, DisplayName, AppId, SignInAudience | Export-Csv M365_ServicePrincipals_20260120.csv

# Check which service principals have secrets/certificates
Get-MgServicePrincipal -All | ForEach-Object {
    $sp = $_
    $secrets = Get-MgServicePrincipalPasswordCredential -ServicePrincipalId $sp.Id
    $certs = Get-MgServicePrincipalKeyCredential -ServicePrincipalId $sp.Id
    [PSCustomObject]@{
        DisplayName = $sp.DisplayName
        AppId = $sp.AppId
        SecretCount = $secrets.Count
        CertCount = $certs.Count
    }
} | Export-Csv M365_ServiceAccount_Credentials_20260120.csv
```

**AWS Example:**
```bash
# List all IAM users (identify service accounts by naming convention)
aws iam list-users --output json | jq '.Users[] | select(.UserName | startswith("svc-")) | {UserName, CreateDate}'

# Check service account access key age (should rotate regularly)
aws iam list-access-keys --user-name svc-automation --output json | jq '.AccessKeyMetadata[] | {AccessKeyId, CreateDate, Status}'

# Verify service accounts don't have console passwords (API-only)
aws iam get-login-profile --user-name svc-automation 2>&1 | grep "NoSuchEntity" && echo "✅ No console password" || echo "❌ Has console password (BAD)"
```

**Evidence Required:**
- Screenshot: Service account inventory page
- Config Export: Complete service account list with owners
- CMDB Export: Service accounts documented in CMDB with ownership
- Evidence File: `M365_ServicePrincipals_20260120.csv`, `ServiceAccount_Inventory_20260120.xlsx`

**Column V Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Yes** | Complete inventory exists, all have documented owners | Service account register with owner column populated |
| **Partial** | Inventory exists but some accounts missing owners | Inventory showing gaps (e.g., 80% have owners) |
| **No** | ❌ No inventory, unknown service accounts exist | Evidence of service accounts discovered without documentation |
| **Unknown** | ⚠️ Don't know if service accounts exist | Requires investigation before assessment can continue |

---

#### Step 7: Set Overall Status (Column H)

**Decision Logic:**
```
IF all of the following are TRUE:
   - SSO = Yes (Column R)
   - MFA = Yes (All Users) (Column S)
   - RBAC = Yes (Column T)
   - JIT = Yes (Column U) OR service criticality ≤ Medium
   - Service Accounts = Yes or Partial (Column V)
THEN Status = ✅ Compliant

ELSE IF most requirements met but 1-2 gaps:
   - Example: SSO=Yes, MFA=Yes, RBAC=Yes, JIT=Planned, Service Accounts=Yes
THEN Status = ⚠️ Partial

ELSE (multiple critical gaps):
   - Example: MFA=No, RBAC=Partial, JIT=No
THEN Status = ❌ Non-Compliant
```

**Real-World Examples:**

**Example 1: Microsoft 365 (Compliant)**
```
Service: Microsoft 365
SSO: Yes (Entra ID federation)
MFA: Yes (All Users) - Conditional Access enforces MFA
RBAC: Yes - Custom roles defined, least privilege applied
JIT: Yes - Azure PIM enabled for Global Admin role
Service Accounts: Yes - 23 service principals documented with owners
Last Access Review: 2025-12-15 (quarterly)
Admin Count: 3 (all JIT-enabled, no permanent admins)

→ Status: ✅ Compliant
→ Evidence: EV-SCD-001 to EV-SCD-007
```

**Example 2: Salesforce (Partial Compliance)**
```
Service: Salesforce
SSO: Yes (Okta SAML)
MFA: Yes (Admins Only) ← ⚠️ GAP: Regular users can skip MFA
RBAC: Yes - Profiles and permission sets properly configured
JIT: No ← ⚠️ GAP: Permanent System Admin accounts exist
Service Accounts: Partial ← ⚠️ GAP: 3 integration users lack documented owners
Last Access Review: 2025-11-01
Admin Count: 5 (all permanent)

→ Status: ⚠️ Partial
→ Gaps: (1) MFA not enforced for all users, (2) No JIT for admins, (3) Incomplete service account inventory
→ Remediation: Enable MFA for all users (30 days), document service account owners (14 days), evaluate Salesforce Shield for JIT (90 days)
```

**Example 3: Legacy Application (Non-Compliant)**
```
Service: Legacy HRIS System (SaaS)
SSO: No ← ❌ CRITICAL: Native authentication only, no SSO support
MFA: No ← ❌ CRITICAL: Vendor doesn't support MFA
RBAC: Partial - Some roles exist, but 80% of users are "Admin"
JIT: N/A (no privileged access concept)
Service Accounts: Unknown ← ❌ No inventory exists
Last Access Review: Never
Admin Count: 45 (out of 50 users!)

→ Status: ❌ Non-Compliant
→ Risk: CRITICAL (Restricted data, no MFA/SSO)
→ Remediation: Vendor replacement required (no technical fix available)
→ Compensating Controls: IP allowlisting, network segmentation, enhanced monitoring
→ Exception Request: Submitted to CISO (business justification: legacy system sunset planned Q3 2026)
```

---

#### Step 8: Document Gaps and Remediation (Columns J, K, N, P)

**If Status ≠ ✅ Compliant, complete gap documentation:**

**Column J (Gap Description):** Be specific about what's wrong
```
✅ Good: "MFA enforced for admins only. 247 regular users can authenticate without MFA."
❌ Bad: "MFA issue"

✅ Good: "5 service principals lack documented owners in CMDB. Discovered: svc-automation, svc-monitoring, svc-backup, svc-cicd, svc-reporting."
❌ Bad: "Some service accounts unknown"
```

**Column K (Remediation Needed):** 
- **Yes:** Gap requires action to fix
- **No:** Gap documented but accepted via formal exception (rare)

**Column N (Compensating Controls):** Temporary mitigations while gap is being fixed
```
Example: Service lacks MFA support
Compensating Controls:
- IP allowlisting enabled (only office IP can access)
- Session timeout set to 15 minutes (vs. default 8 hours)
- Enhanced monitoring: Alert on any login from unknown IP
- Network segmentation: Service isolated from internet via private endpoint
```

**Column P (Target Remediation Date):** Be realistic
```
Quick Win (≤30 days): Enable MFA for all users, document service account owners
Medium Effort (30-90 days): Implement Azure PIM for JIT access
Long-Term (>90 days): Replace legacy system lacking SSO/MFA support
```

---

#### Step 9: Complete Checklist (Below Data Rows)

**Checklist starts at Row 33 (after data rows 7-30):**
```
IDENTITY & ACCESS CONFIGURATION CHECKLIST

☑ SSO configured via organizational IdP (Entra ID, Okta, etc.)
  Status: ✅   Evidence: EV-SCD-001 (M365_SSO_Config_20260120.png)

☑ MFA enforced for all users
  Status: ✅   Evidence: EV-SCD-002 (MFA_User_Status_20260120.csv)

☑ MFA mandatory for privileged accounts
  Status: ✅   Evidence: EV-SCD-003 (PIM_Config_20260120.png)

☑ RBAC roles documented and implemented
  Status: ✅   Evidence: EV-SCD-004 (RBAC_Role_Matrix_v2.xlsx, Azure_RBAC_Assignments_20260120.csv)

☑ Least privilege principle applied
  Status: ⚠️   Evidence: EV-SCD-005 (RBAC audit identified 3 over-privileged users, remediation in progress)

☑ Service accounts inventoried with owners
  Status: ✅   Evidence: EV-SCD-006 (ServiceAccount_Inventory_20260120.xlsx)

☑ Privileged access is time-limited (JIT)
  Status: ✅   Evidence: EV-SCD-007 (PIM_Activation_Log_20260120.csv)

☑ Access reviews performed quarterly
  Status: ✅   Evidence: EV-SCD-008 (Access_Review_Report_Q4_2025.pdf)

☑ Default accounts disabled or renamed
  Status: ✅   Evidence: EV-SCD-009 (Default_Account_Audit_20260120.txt)

☑ Failed login alerting configured
  Status: ✅   Evidence: EV-SCD-010 (SIEM_Alert_Rule_FailedLogins_20260120.png)
```

**Implementer Perspective:**
*"The checklist is your quality gate. If any item is ❌ or ⚠️, you have work to do. Don't skip ahead to next sheet until this one is solid."*

**Auditor Perspective:**
*"I cross-check checklist status against Column H (overall Status). If checklist shows multiple ❌ but Status = ✅, something's wrong - investigate data integrity."*

---

### 4.3 Sheet 3: Data Protection Configuration - Step-by-Step

**Configuration Area:** Encryption (Rest/Transit), Key Management, DLP, Classification

#### Step 1: Assess Encryption at Rest (Column R)

**What to Check:**
```
1. Navigate to encryption settings in admin console
2. Verify: Encryption enabled for all data stores (databases, file storage, backups)
3. Check key type: Provider-managed vs. Customer-managed keys (CMK)
4. Validate algorithm: AES-256 preferred, AES-128 minimum acceptable
```

**Azure Storage Example:**
```powershell
# Check storage account encryption
Connect-AzAccount
Get-AzStorageAccount | Select-Object StorageAccountName, ResourceGroupName, @{N='Encryption';E={$_.Encryption.Services}} | Format-Table

# Verify customer-managed keys (CMK)
Get-AzStorageAccount | Where-Object {$_.Encryption.KeySource -eq "Microsoft.Keyvault"} | Format-Table StorageAccountName, @{N='KeyVaultUri';E={$_.Encryption.KeyVaultProperties.KeyVaultUri}}

# Export for evidence
Get-AzStorageAccount | Select-Object StorageAccountName, @{N='EncryptionEnabled';E={$_.Encryption.Services.Blob.Enabled}}, @{N='KeySource';E={$_.Encryption.KeySource}} | Export-Csv Azure_Storage_Encryption_20260120.csv
```

**AWS S3 Example:**
```bash
# List buckets and check encryption
aws s3api list-buckets --query "Buckets[].Name" --output text | while read bucket; do
    encryption=$(aws s3api get-bucket-encryption --bucket "$bucket" 2>/dev/null | jq -r '.ServerSideEncryptionConfiguration.Rules[0].ApplyServerSideEncryptionByDefault.SSEAlgorithm')
    if [ -z "$encryption" ]; then
        echo "❌ $bucket: No encryption"
    else
        echo "✅ $bucket: $encryption"
    fi
done

# Check for CMK usage
aws s3api list-buckets --query "Buckets[].Name" --output text | while read bucket; do
    aws s3api get-bucket-encryption --bucket "$bucket" 2>/dev/null | jq -r ".ServerSideEncryptionConfiguration.Rules[0] | select(.ApplyServerSideEncryptionByDefault.SSEAlgorithm == \"aws:kms\") | \"$bucket: CMK enabled\""
done
```

**Evidence Required:**
- Screenshot: Encryption settings page showing "Enabled"
- Config Export: Storage account encryption status (CSV)
- Evidence File: `Azure_Storage_Encryption_20260120.csv`, `Storage_Encryption_Screenshot_20260120.png`

**Column R Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Yes (Provider Key)** | Encryption enabled using vendor's default keys | Config showing encryption=enabled, key=provider-managed |
| **Yes (CMK)** | Encryption using customer-managed keys (preferred for sensitive data) | Config showing encryption=enabled, key=customer-managed, Key Vault reference |
| **No** | ❌ CRITICAL: No encryption at rest | Config showing encryption=disabled or not configured |
| **N/A** | Service doesn't store data at rest (compute-only) | Architecture doc showing no persistent storage |

**Decision Matrix for CMK:**
```
IF Data Classification = "Restricted":
   CMK = MANDATORY
ELIF Data Classification = "Confidential" AND Vendor Risk (IMP-5.23.2) = "HIGH":
   CMK = MANDATORY
ELIF Data Classification = "Confidential" AND Vendor Risk = "MEDIUM":
   CMK = RECOMMENDED (document decision if not using)
ELSE:
   Provider Key = ACCEPTABLE
```

---

#### Step 2: Assess Encryption in Transit (Column S)

**What to Check:**
```
1. Verify: TLS 1.2 or higher enforced (TLS 1.0/1.1 disabled)
2. Test: All endpoints (web, API, admin console) use HTTPS
3. Validate: Certificate is valid (not expired, trusted CA, correct domain)
4. Check: HTTP redirects to HTTPS (no plaintext HTTP allowed)
```

**SSL/TLS Testing:**
```bash
# Use SSL Labs for web services (online tool)
# https://www.ssllabs.com/ssltest/analyze.html?d=example.com

# Or command-line with testssl.sh
./testssl.sh --protocols https://api.example.com

# Expected output should show:
# ✅ TLS 1.2    offered
# ✅ TLS 1.3    offered
# ❌ TLS 1.0    NOT offered (disabled)
# ❌ TLS 1.1    NOT offered (disabled)
```

**Azure Web App Example:**
```powershell
# Check minimum TLS version for Azure Web Apps
Get-AzWebApp | Select-Object Name, @{N='MinTlsVersion';E={$_.SiteConfig.MinTlsVersion}} | Format-Table

# Verify HTTPS only (no HTTP)
Get-AzWebApp | Select-Object Name, HttpsOnly | Where-Object {$_.HttpsOnly -eq $false}

# If any returned → ❌ Gap: HTTP still allowed
```

**AWS ALB/CloudFront Example:**
```bash
# Check Application Load Balancer security policy
aws elbv2 describe-load-balancers --query "LoadBalancers[].LoadBalancerArn" --output text | while read alb; do
    policy=$(aws elbv2 describe-listeners --load-balancer-arn "$alb" --query "Listeners[].SslPolicy" --output text)
    echo "ALB: $alb"
    echo "SSL Policy: $policy"
    # Recommended: ELBSecurityPolicy-TLS-1-2-2017-01 or newer
done
```

**Evidence Required:**
- Screenshot: SSL Labs report showing A/A+ grade
- Config Export: TLS policy settings
- Certificate Details: Validity period, issuer, algorithm
- Evidence File: `SSLLabs_Report_api.example.com_20260120.pdf`, `TLS_Config_20260120.txt`

**Column S Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Yes (TLS 1.3)** | TLS 1.3 supported and preferred | SSL Labs showing TLS 1.3 as highest protocol |
| **Yes (TLS 1.2)** | TLS 1.2 minimum, TLS 1.3 may not be supported | SSL Labs showing TLS 1.2, 1.0/1.1 disabled |
| **No** | ❌ CRITICAL: TLS 1.0/1.1 still enabled OR HTTP allowed | SSL Labs showing weak protocols or F grade |
| **N/A** | Service has no network connectivity (offline) | Architecture doc showing air-gapped system |

---

#### Step 3: Assess Key Management (Column U)

**What to Check:**
```
1. Verify: Encryption keys stored in HSM or cloud KMS (not in app code!)
2. Check access: Only authorized systems/users can access keys
3. Validate rotation: Automatic key rotation enabled OR manual rotation documented
4. Review audit logs: Key access is logged and monitored
```

**Azure Key Vault Example:**
```powershell
# List all Key Vaults
Get-AzKeyVault | Select-Object VaultName, ResourceGroupName, Location

# Check key rotation policy
$vaultName = "prod-keyvault"
Get-AzKeyVaultKey -VaultName $vaultName | ForEach-Object {
    $key = $_
    $policy = Get-AzKeyVaultKeyRotationPolicy -VaultName $vaultName -Name $key.Name
    [PSCustomObject]@{
        KeyName = $key.Name
        AutoRotation = $policy.LifetimeActions.Action
        RotationInterval = $policy.ExpiryTime
    }
} | Export-Csv Azure_KeyRotation_20260120.csv

# Verify access policies (who can access keys)
Get-AzKeyVault -VaultName $vaultName | Select-Object -ExpandProperty AccessPolicies | Export-Csv Azure_KeyVault_Access_20260120.csv
```

**AWS KMS Example:**
```bash
# List KMS keys
aws kms list-keys --output json | jq '.Keys[].KeyId'

# Check key rotation status
aws kms list-keys --output json | jq -r '.Keys[].KeyId' | while read key; do
    rotation=$(aws kms get-key-rotation-status --key-id "$key" --output json | jq -r '.KeyRotationEnabled')
    echo "Key: $key, Rotation Enabled: $rotation"
done

# Verify key policies (who can use keys)
aws kms list-keys --output json | jq -r '.Keys[].KeyId' | while read key; do
    echo "=== Key: $key ==="
    aws kms get-key-policy --key-id "$key" --policy-name default --output json | jq '.Policy | fromjson'
done > AWS_KMS_Policies_20260120.json
```

**Evidence Required:**
- Screenshot: Key Vault/KMS dashboard showing keys
- Config Export: Key rotation policy
- Access Policy: Who can access/use keys
- Audit Log: Recent key access events
- Evidence File: `Azure_KeyVault_Config_20260120.png`, `Azure_KeyRotation_20260120.csv`, `KeyVault_Access_Policies_20260120.csv`

**Column U Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Customer Managed (HSM)** | Keys in dedicated HSM (highest security) | Config showing HSM-backed keys, FIPS 140-2 Level 3 certification |
| **Customer Managed (Software)** | Keys in cloud KMS (Azure Key Vault, AWS KMS) | Config showing customer-managed keys in cloud KMS |
| **Provider Managed** | Keys managed by cloud provider (acceptable for low/medium sensitivity) | Config showing provider-managed encryption |
| **N/A** | No encryption or no key management needed | Valid only if Column R = "No" or "N/A" |

---

#### Step 4: Assess Data Classification Labels (Column V)

**What to Check:**
```
1. Verify: Classification labels configured (Public, Internal, Confidential, Restricted)
2. Check enforcement: Labels are required, not optional
3. Validate usage: Labels are actually applied to documents/emails/data
4. Review policy: DLP rules reference classification labels
```

**Microsoft 365 Sensitivity Labels Example:**
```powershell
# List sensitivity labels
Connect-IPPSSession
Get-Label | Select-Object DisplayName, Name, Priority, Disabled | Format-Table

# Check if labels are enforced (mandatory)
Get-LabelPolicy | Select-Object Name, @{N='MandatoryLabelPolicy';E={$_.Settings | Where-Object {$_.Key -eq "mandatory"} | Select-Object -ExpandProperty Value}}

# Verify label usage (how many items are labeled)
Get-ActivityAlert | Where-Object {$_.Operation -eq "SensitivityLabelApplied"} | Measure-Object
# If count is low → labels exist but aren't being used
```

**Evidence Required:**
- Screenshot: Sensitivity labels configuration page
- Config Export: Label definitions and policies
- Usage Report: Number of labeled items (prove labels are actually used)
- Evidence File: `M365_SensitivityLabels_20260120.png`, `Label_Policy_Export_20260120.xml`, `Label_Usage_Report_20260120.pdf`

**Column V Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Yes (Enforced)** | Labels required, users cannot save unlabeled documents | Policy showing mandatory labeling + usage report |
| **Yes (Optional)** | Labels available but not required | Label config + low usage report (users skip labeling) |
| **No** | ❌ No classification labels configured | Evidence showing no label system exists |
| **N/A** | Service doesn't handle documents/emails (e.g., compute-only) | Architecture doc showing no data classification need |

---

#### Step 5: Assess DLP Configuration (Column W)

**What to Check:**
```
1. Verify: DLP rules configured for sensitive data types (PII, credit cards, SSN, etc.)
2. Check scope: DLP covers all channels (email, chat, file sharing, external sharing)
3. Validate actions: Block or encrypt when sensitive data detected (not just alert)
4. Review incidents: DLP actually triggering (not just configured but unused)
```

**Microsoft 365 DLP Example:**
```powershell
# List DLP policies
Connect-IPPSSession
Get-DlpCompliancePolicy | Select-Object Name, Mode, Workload | Format-Table

# Check DLP rules (what's being detected)
Get-DlpComplianceRule | Select-Object Name, ParentPolicyName, ContentContainsSensitiveInformation, BlockAccess | Format-Table

# Review DLP incidents (proof it's working)
Get-ActivityAlert | Where-Object {$_.Operation -eq "DLPRuleMatch"} | Measure-Object
# High count = DLP actively catching violations (good for evidence)
```

**AWS Macie Example (S3 DLP):**
```bash
# Check if Macie is enabled
aws macie2 get-macie-session --output json | jq '.status'

# List sensitive data findings
aws macie2 list-findings --output json | jq '.findingIds[]' | while read finding; do
    aws macie2 get-findings --finding-ids "$finding" --output json | jq '.findings[] | {Type: .type, Severity: .severity.description, Resource: .resourcesAffected.s3Bucket.name}'
done
```

**Evidence Required:**
- Screenshot: DLP policy page showing rules
- Config Export: DLP policy and rule definitions
- Incident Report: DLP violations detected in last 30 days
- Evidence File: `M365_DLP_Policies_20260120.png`, `DLP_Policy_Export_20260120.json`, `DLP_Incident_Report_Dec2025.pdf`

**Column W Dropdown Options:**

| Value | When to Use | Evidence Requirement |
|-------|-------------|---------------------|
| **Yes** | DLP configured, blocking or encrypting sensitive data | Policy export + incident report showing active enforcement |
| **Partial** | DLP configured but only alerting (not blocking) | Policy showing "Audit" mode, not "Block" mode |
| **No** | ❌ No DLP configured | Evidence showing no DLP system exists |
| **N/A** | Service doesn't share data externally (isolated) | Architecture doc showing no external sharing capability |

---

#### Step 6: Set Overall Status and Complete Checklist

**Status Decision Logic:**
```
IF all of the following are TRUE:
   - Encryption at Rest = Yes (CMK for Restricted data) (Column R)
   - Encryption in Transit = Yes (TLS 1.2+) (Column S)
   - Encryption Algorithm = AES-256 (Column T)
   - Key Management = Customer Managed OR Provider Managed (based on data classification) (Column U)
   - Classification Labels = Yes (Enforced) OR N/A (Column V)
   - DLP = Yes OR N/A (Column W)
   - Key Rotation = 90-365 days (Column X)
THEN Status = ✅ Compliant

ELSE IF most requirements met but 1-2 gaps:
   - Example: Encryption=Yes but Key Rotation=Manual (not automated)
THEN Status = ⚠️ Partial

ELSE (critical gaps):
   - Example: Encryption at Rest=No, TLS 1.0 still enabled
THEN Status = ❌ Non-Compliant
```

**Checklist Completion:**
```
DATA PROTECTION CONFIGURATION CHECKLIST

☑ TLS 1.2+ enforced for all connections
  Status: ✅   Evidence: EV-SCD-011 (SSLLabs_Report_20260120.pdf)

☑ AES-256 encryption at rest enabled
  Status: ✅   Evidence: EV-SCD-012 (Azure_Storage_Encryption_20260120.csv)

☑ Encryption keys stored securely (HSM/KMS)
  Status: ✅   Evidence: EV-SCD-013 (Azure_KeyVault_Config_20260120.png)

☑ Key rotation policy implemented
  Status: ✅   Evidence: EV-SCD-014 (Azure_KeyRotation_20260120.csv)

☑ Data classification labels applied
  Status: ⚠️   Evidence: EV-SCD-015 (Labels exist but only 40% of documents labeled - improvement needed)

☑ DLP rules configured for sensitive data
  Status: ✅   Evidence: EV-SCD-016 (M365_DLP_Policies_20260120.png, DLP_Incident_Report_Dec2025.pdf)

☑ Data masking for non-production environments
  Status: ✅   Evidence: EV-SCD-017 (Dev_Database_Masking_Config_20260120.sql)

☑ Secure deletion process documented
  Status: ✅   Evidence: EV-SCD-018 (Data_Deletion_Procedure_v3.pdf)
```

---

### 4.4 Sheets 4-6: Abbreviated Guidance (Same Pattern)

**Due to length constraints, Sheets 4-6 follow the same step-by-step pattern as Sheets 2-3:**

**Sheet 4 (Network Security):**
- Assess IP Restrictions (Column R)
- Assess Private Connectivity (Column S)
- Assess Network Segmentation (Column T)
- Assess WAF (Column U)
- Assess DDoS Protection (Column V)
- Document Firewall Rules (Column W)
- Count Public Endpoints (Column X)
- Set Status, complete checklist

**Sheet 5 (Logging & Monitoring):**
- Assess Audit Logging (Column R)
- Assess SIEM Integration (Column S)
- Assess Alerting (Column T)
- Verify Log Retention ≥365 days (Column U)
- Assess Threat Detection (Column V)
- Check Security Dashboard (Column W)
- Note Last Log Review (Column X)
- Set Status, complete checklist

**Sheet 6 (Backup & Recovery):**
- Verify Backup Enabled (Column R)
- Check Backup Frequency (Column S)
- Verify Retention Period (Column T)
- Check Backup Encryption (Column U)
- Note Last Recovery Test (Column V)
- Document RPO (Column W)
- Document RTO (Column X)
- Set Status, complete checklist

---

### 4.5 Sheet 7: Jurisdictional Risk - Configuration Alignment

**Purpose:** Cross-reference configuration with vendor jurisdictional commitments (IMP-5.23.2 Sheet 5 & Sheet 7)

**Step-by-Step:**

1. **Open IMP-A.5.23.2 Sheet 5 (Data Sovereignty)**
   - Note vendor's contractual data residency commitment
   - Example: "DPA states data processing in EU only"

2. **Verify Configuration Matches Contract:**
```
   Azure SQL Database:
   - Contract says: "EU data residency"
   - Config check: az sql server show --name prod-sql --resource-group prod-rg --query "location"
   - Expected output: "westeurope" or "northeurope" (✅)
   - Wrong output: "eastus" (❌ CRITICAL - breach of contract)
```

3. **For US-Nexus Vendors, Verify Mitigations:**
```
   Microsoft 365 (US-headquartered):
   - IMP-5.23.2 Sheet 7 identifies: CLOUD Act exposure
   - Required mitigations:
     ✓ EU Data Boundary enabled (Admin Center → Settings → Org Settings → EU Data Boundary)
     ✓ Customer Lockbox enabled (Microsoft support cannot access data without approval)
     ✓ Customer-Managed Keys for sensitive workloads
   
   Evidence: Screenshot showing EU Data Boundary active
```

4. **Document Alignment or Gaps:**
```
   ✅ Aligned: Config matches contract
   ❌ Gap: Config in wrong region (escalate to vendor + legal immediately)
   ⚠️ Partial: Config mostly aligned but subprocessor in non-EU region (evaluate risk)
```

---

### 4.6 Sheet 8: Summary Dashboard - Verification

**This sheet is AUTO-CALCULATED via formulas. Your job: VERIFY accuracy.**

**Verification Steps:**

1. **Manually Count Row Totals:**
```
   Go to Sheet 2 (Identity & Access)
   Count rows 7-30 where Column H = ✅
   Compare to Sheet 8 Table 1 "Compliant" count for Identity & Access
   If mismatch → Check formulas
```

2. **Cross-Check Environment Breakdown:**
```
   Production services should have higher compliance than Dev
   If Dev > Prod compliance → Investigate (unusual pattern)
```

3. **Validate Risk Heatmap:**
```
   HIGH/CRITICAL findings should match actual ❌ rows in Sheets 2-6
   Manually verify each HIGH finding is legitimate (not formula error)
```

**Implementer Perspective:**
*"Don't just accept dashboard numbers. Spot-check them. Formulas can break if sheets are edited incorrectly."*

**Auditor Perspective:**
*"I randomly sample 10 dashboard metrics and trace back to source data. If >2 don't match, dashboard integrity is questioned."*

---

### 4.7 Sheet 9: Evidence Register - Linking Evidence

**For every piece of evidence collected, create an entry:**

**Example Entry:**
```
Evidence ID: EV-SCD-001
Sheet Reference: Sheet 2 (Identity & Access)
Cloud Service: Microsoft 365
Configuration Item: Conditional Access Policy - MFA Enforcement
Evidence Type: Screenshot
Evidence Filename: M365_MFA_Policy_20260120.png
Evidence Location: /Evidence/IMP-A.5.23.3/2026-01-20/Identity/
Collection Date: 2026-01-20
Collected By: Jane Smith (Security Engineer)
Status: ✅ Verified
```

**Link Back to Assessment Sheets:**
```
In Sheet 2, Column I (Evidence Location):
Enter: "EV-SCD-001, EV-SCD-002, EV-SCD-003"

This creates traceability: Assessment → Evidence Register → Actual files
```

---

### 4.8 Sheet 10: Approval Sign-Off - Workflow

**Stage 1: IT Operations Review:**
```
1. IT Ops Lead reviews Sheets 2-6 for technical accuracy
2. Verifies configurations match their knowledge of systems
3. Signs off or rejects with specific feedback
4. Typical turnaround: 3-5 business days
```

**Stage 2: Security Team Review:**
```
1. Security Engineer/Architect reviews for security adequacy
2. Evaluates gap remediation plans
3. Validates evidence quality
4. Signs off or requests improvements
5. Typical turnaround: 3-5 business days
```

**Stage 3: CISO Approval:**
```
1. CISO reviews Summary Dashboard (Sheet 8)
2. Focuses on HIGH/CRITICAL findings
3. Approves, Approves with Conditions, or Rejects
4. If Approved with Conditions: Specifies remediation timeline
5. Typical turnaround: 5-7 business days
```

**Total Approval Timeline: ~2-3 weeks from submission to final approval**

---

**END OF SECTION 4: COMPLETING EACH SHEET - DETAILED GUIDANCE**

## Section 5: Evidence Collection Guide

### 5.1 Evidence Collection Philosophy

**The Evidence-Based Compliance Principle:**
```
"In evidence we trust; all others must bring data."
                                    - W. Edwards Deming (adapted)
```

**Three Evidence Quality Levels:**
```
┌─────────────────────────────────────────────────────────────────┐
│                    EVIDENCE QUALITY PYRAMID                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│                          ▲ GOLD                                  │
│                         ╱ ╲                                      │
│                        ╱   ╲  Programmatic Config Export        │
│                       ╱     ╲  (JSON, YAML, Terraform state)    │
│                      ╱       ╲ Machine-readable, hard to fake   │
│                     ╱_________╲                                  │
│                    ╱           ╲                                 │
│                   ╱   SILVER    ╲                                │
│                  ╱               ╲ Timestamped Screenshots       │
│                 ╱                 ╲ Visual proof, timestamp      │
│                ╱___________________╲ verifiable                  │
│               ╱                     ╲                             │
│              ╱       BRONZE          ╲                            │
│             ╱                         ╲ Security Scan Reports    │
│            ╱                           ╲ Third-party validation  │
│           ╱_____________________________╲                         │
│                                                                   │
│  UNACCEPTABLE: "Trust me, it's configured correctly"            │
│                 Verbal claims, undated screenshots              │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

**The 5 Ws of Evidence:**

| Question | Answer | Example |
|----------|--------|---------|
| **What** | Configuration setting being proven | "MFA enforcement for all users" |
| **When** | Timestamp of evidence collection | "2026-01-20 14:35:42 UTC" |
| **Where** | Service/system location | "Microsoft 365 tenant: contoso.onmicrosoft.com" |
| **Who** | Evidence collector identity | "Jane Smith, Cloud Security Engineer" |
| **Why** | Which assessment requirement | "IMP-A.5.23.3 Sheet 2, Column S - MFA Enforced" |

---

### 5.2 What Evidence to Collect

**Evidence Type Matrix:**

| Configuration Area | Primary Evidence (GOLD) | Secondary Evidence (SILVER) | Tertiary Evidence (BRONZE) |
|-------------------|------------------------|----------------------------|---------------------------|
| **Identity & Access** | User list export (CSV) showing MFA status, RBAC assignments (JSON) | Screenshot of MFA policy, Azure AD config page | Identity security posture report |
| **Data Protection** | Encryption config export (JSON), Key Vault policy (ARM template) | Screenshot of encryption settings, Key rotation config | Azure Secure Score - Data Protection section |
| **Network Security** | Firewall rules export (JSON), NSG config (ARM), Route tables | Screenshot of network topology, WAF rules page | Network vulnerability scan report |
| **Logging & Monitoring** | SIEM query results (CSV), Log Analytics workspace config (JSON) | Screenshot of diagnostic settings, Alert rules | SIEM dashboard screenshot with timestamp |
| **Backup & Recovery** | Backup policy config (JSON), Recovery test log (PDF) | Screenshot of backup jobs, Retention settings | Disaster recovery test report |

---

### 5.3 How to Collect Evidence - Tool-by-Tool Guide

#### 5.3.1 Screenshots: Best Practices

**Tool Recommendations:**

**Windows:**
- **Snipping Tool** (Built-in, Win+Shift+S)
  - Pros: Built-in, no install needed, rectangular selection
  - Cons: No auto-timestamp, basic features
- **Greenshot** (Free, https://getgreenshot.org)
  - Pros: Auto-timestamp, annotations, plugins
  - Cons: Requires install
- **Snagit** (Paid, $50)
  - Pros: Professional features, scrolling capture, video recording
  - Cons: Cost

**macOS:**
- **Screenshot Utility** (Built-in, Cmd+Shift+4)
  - Pros: Built-in, high quality
  - Cons: No auto-timestamp
- **CleanShot X** (Paid, $29/year)
  - Pros: Scrolling capture, annotations, cloud upload
  - Cons: Subscription cost

**Linux:**
- **Flameshot** (Free, https://flameshot.org)
  - Pros: Powerful, cross-platform, annotations
  - Cons: Learning curve
- **Spectacle** (Free, KDE default)
  - Pros: Simple, effective
  - Cons: Basic features

**Screenshot Quality Checklist:**
```
BEFORE taking screenshot:
☐ Maximize window (avoid cropped/obscured content)
☐ Zoom to 100% (no scaling artifacts)
☐ Ensure timestamp is visible (system clock, or service UI timestamp)
☐ Remove sensitive data (redact passwords, keys, personal info)
☐ Clean up desktop (close irrelevant windows, hide personal files)

WHILE taking screenshot:
☐ Capture entire relevant section (don't crop out important context)
☐ Include navigation breadcrumbs (so viewer knows where in UI)
☐ Highlight key setting (red box, arrow annotation)

AFTER taking screenshot:
☐ Save with descriptive filename (not "Screenshot_123.png")
☐ Add timestamp to filename (YYYYMMDD format)
☐ Store in evidence repository immediately (don't keep on desktop)
```

**Screenshot Filename Convention:**
```
Format: [Service]_[ConfigArea]_[Setting]_[YYYYMMDD].[ext]

✅ Good Examples:
   - M365_MFA_Policy_Enforcement_20260120.png
   - Azure_SQL_Encryption_AtRest_Config_20260120.png
   - AWS_S3_Bucket_PublicAccess_Blocked_20260120.png
   - Salesforce_SessionTimeout_Settings_20260120.png

❌ Bad Examples:
   - Screenshot1.png (meaningless)
   - mfa.png (too vague)
   - config_new.png (no context, no date)
   - IMG_20260120_143542.png (unclear what it shows)
```

**Timestamp Verification:**
```
Option 1: System Clock Visible in Screenshot
  - Windows: Taskbar clock (bottom-right)
  - macOS: Menu bar clock (top-right)
  - ✅ Advantage: Proves screenshot date/time
  - ⚠️ Limitation: Can be Photoshopped

Option 2: Service UI Timestamp
  - Many cloud services show "Last updated" or "Current time" in UI
  - Example: Azure Portal shows time in top-right
  - ✅ Advantage: Harder to fake (service-generated)
  
Option 3: File Metadata
  - Screenshot file properties show creation date
  - Windows: Right-click → Properties → Details
  - macOS: Right-click → Get Info
  - Linux: exiftool screenshot.png
  - ⚠️ Limitation: Can be modified, not court-proof
```

---

#### 5.3.2 Configuration Exports: PowerShell, CLI, API

**Azure / Microsoft 365:**

**PowerShell Module Installation:**
```powershell
# Run as Administrator
Install-Module -Name Az -Force -AllowClobber
Install-Module -Name Microsoft.Graph -Force -AllowClobber
Install-Module -Name ExchangeOnlineManagement -Force -AllowClobber

# Verify installation
Get-InstalledModule Az
Get-InstalledModule Microsoft.Graph
```

**Common Export Commands:**
```powershell
# Connect
Connect-AzAccount
Connect-MgGraph -Scopes "Directory.Read.All", "Policy.Read.All"

# Export Azure subscription configuration
$subscription = "your-subscription-id"
Set-AzContext -SubscriptionId $subscription

# 1. Export all resource groups
Get-AzResourceGroup | Export-Csv "Azure_ResourceGroups_20260120.csv" -NoTypeInformation

# 2. Export virtual networks and subnets
Get-AzVirtualNetwork | ForEach-Object {
    [PSCustomObject]@{
        Name = $_.Name
        Location = $_.Location
        AddressSpace = $_.AddressSpace.AddressPrefixes -join ";"
        Subnets = ($_.Subnets | ForEach-Object { "$($_.Name): $($_.AddressPrefix)" }) -join "; "
    }
} | Export-Csv "Azure_VirtualNetworks_20260120.csv" -NoTypeInformation

# 3. Export storage account encryption settings
Get-AzStorageAccount | Select-Object StorageAccountName, ResourceGroupName, Location,
    @{N='EncryptionEnabled';E={$_.Encryption.Services.Blob.Enabled}},
    @{N='KeySource';E={$_.Encryption.KeySource}},
    @{N='MinimumTlsVersion';E={$_.MinimumTlsVersion}} |
    Export-Csv "Azure_StorageEncryption_20260120.csv" -NoTypeInformation

# 4. Export Azure AD conditional access policies (MFA)
Get-MgIdentityConditionalAccessPolicy | ForEach-Object {
    [PSCustomObject]@{
        DisplayName = $_.DisplayName
        State = $_.State
        Conditions = $_.Conditions | ConvertTo-Json -Depth 5
        GrantControls = $_.GrantControls | ConvertTo-Json -Depth 5
    }
} | Export-Csv "M365_ConditionalAccessPolicies_20260120.csv" -NoTypeInformation

# 5. Export MFA status for all users
Get-MgUser -All | ForEach-Object {
    $userId = $_.Id
    $mfaMethods = Get-MgUserAuthenticationMethod -UserId $userId
    [PSCustomObject]@{
        UserPrincipalName = $_.UserPrincipalName
        DisplayName = $_.DisplayName
        MFAEnabled = ($mfaMethods.Count -gt 1)
        MFAMethods = ($mfaMethods | ForEach-Object { $_.AdditionalProperties."@odata.type" }) -join ";"
    }
} | Export-Csv "M365_UserMFAStatus_20260120.csv" -NoTypeInformation

# 6. Export Exchange Online DLP policies
Connect-ExchangeOnline
Get-DlpCompliancePolicy | Select-Object Name, Mode, Workload, Enabled |
    Export-Csv "M365_DLPPolicies_20260120.csv" -NoTypeInformation
Get-DlpComplianceRule | Select-Object Name, ParentPolicyName, BlockAccess, ContentContainsSensitiveInformation |
    Export-Csv "M365_DLPRules_20260120.csv" -NoTypeInformation
```

---

**AWS:**

**AWS CLI Installation:**
```bash
# macOS
brew install awscli

# Linux (Ubuntu/Debian)
sudo apt install awscli

# Windows (PowerShell)
# Download from https://aws.amazon.com/cli/

# Configure
aws configure
# Enter: Access Key, Secret Key, Default Region, Output Format (json)
```

**Common Export Commands:**
```bash
# 1. Export EC2 instance configurations
aws ec2 describe-instances --output json | jq '.Reservations[].Instances[] | {
    InstanceId: .InstanceId,
    InstanceType: .InstanceType,
    State: .State.Name,
    PrivateIp: .PrivateIpAddress,
    PublicIp: .PublicIpAddress,
    SubnetId: .SubnetId,
    SecurityGroups: [.SecurityGroups[].GroupId]
}' > AWS_EC2_Instances_20260120.json

# 2. Export S3 bucket encryption status
aws s3api list-buckets --query "Buckets[].Name" --output text | while read bucket; do
    encryption=$(aws s3api get-bucket-encryption --bucket "$bucket" 2>/dev/null | jq -r '.ServerSideEncryptionConfiguration.Rules[0].ApplyServerSideEncryptionByDefault.SSEAlgorithm')
    versioning=$(aws s3api get-bucket-versioning --bucket "$bucket" | jq -r '.Status')
    publicAccess=$(aws s3api get-public-access-block --bucket "$bucket" 2>/dev/null | jq -r '.PublicAccessBlockConfiguration.BlockPublicAcls')
    
    echo "{\"Bucket\": \"$bucket\", \"Encryption\": \"$encryption\", \"Versioning\": \"$versioning\", \"PublicAccessBlocked\": \"$publicAccess\"}"
done | jq -s '.' > AWS_S3_BucketSecurity_20260120.json

# 3. Export IAM user MFA status
aws iam list-users --output json | jq -r '.Users[].UserName' | while read user; do
    mfaDevices=$(aws iam list-mfa-devices --user-name "$user" --output json | jq '.MFADevices | length')
    accessKeys=$(aws iam list-access-keys --user-name "$user" --output json | jq '.AccessKeyMetadata | length')
    
    echo "{\"UserName\": \"$user\", \"MFADevices\": $mfaDevices, \"AccessKeys\": $accessKeys}"
done | jq -s '.' > AWS_IAM_UserMFAStatus_20260120.json

# 4. Export VPC security groups
aws ec2 describe-security-groups --output json | jq '.SecurityGroups[] | {
    GroupId: .GroupId,
    GroupName: .GroupName,
    VpcId: .VpcId,
    IngressRules: .IpPermissions,
    EgressRules: .IpPermissionsEgress
}' | jq -s '.' > AWS_VPC_SecurityGroups_20260120.json

# 5. Export CloudTrail logging status
aws cloudtrail describe-trails --output json | jq '.trailList[] | {
    Name: .Name,
    S3BucketName: .S3BucketName,
    IsMultiRegionTrail: .IsMultiRegionTrail,
    LogFileValidationEnabled: .LogFileValidationEnabled
}' | jq -s '.' > AWS_CloudTrail_Config_20260120.json

# 6. Export RDS encryption status
aws rds describe-db-instances --output json | jq '.DBInstances[] | {
    DBInstanceIdentifier: .DBInstanceIdentifier,
    Engine: .Engine,
    StorageEncrypted: .StorageEncrypted,
    KmsKeyId: .KmsKeyId,
    PubliclyAccessible: .PubliclyAccessible,
    BackupRetentionPeriod: .BackupRetentionPeriod
}' | jq -s '.' > AWS_RDS_Encryption_20260120.json
```

---

**Google Cloud Platform:**

**gcloud CLI Installation:**
```bash
# Linux/macOS
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Windows
# Download from https://cloud.google.com/sdk/docs/install

# Authenticate
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

**Common Export Commands:**
```bash
# 1. Export compute instances
gcloud compute instances list --format=json > GCP_ComputeInstances_20260120.json

# 2. Export firewall rules
gcloud compute firewall-rules list --format=json > GCP_FirewallRules_20260120.json

# 3. Export GCS bucket encryption
gsutil ls | while read bucket; do
    encryption=$(gsutil encryption get "$bucket" 2>/dev/null)
    versioning=$(gsutil versioning get "$bucket")
    publicAccess=$(gsutil iam get "$bucket" | grep "allUsers" && echo "PUBLIC" || echo "PRIVATE")
    
    echo "{\"Bucket\": \"$bucket\", \"Encryption\": \"$encryption\", \"Versioning\": \"$versioning\", \"PublicAccess\": \"$publicAccess\"}"
done | jq -s '.' > GCP_GCS_BucketSecurity_20260120.json

# 4. Export IAM policy bindings
gcloud projects get-iam-policy $(gcloud config get-value project) --format=json > GCP_IAM_Policy_20260120.json

# 5. Export SQL instances encryption
gcloud sql instances list --format=json | jq '.[] | {
    name: .name,
    databaseVersion: .databaseVersion,
    diskEncryptionStatus: .diskEncryptionStatus,
    backupEnabled: .settings.backupConfiguration.enabled
}' | jq -s '.' > GCP_SQL_Encryption_20260120.json
```

---

#### 5.3.3 Security Scan Reports

**Azure Security Center / Microsoft Defender for Cloud:**
```powershell
# Get Secure Score
Connect-AzAccount
$subscriptionId = "your-subscription-id"
Set-AzContext -SubscriptionId $subscriptionId

# Export secure score
$secureScore = Get-AzSecuritySecureScore
$secureScore | Select-Object DisplayName, CurrentScore, MaxScore, Percentage | 
    Export-Csv "Azure_SecureScore_20260120.csv" -NoTypeInformation

# Export security recommendations
Get-AzSecurityTask | Select-Object Name, State, SecurityTaskParameters |
    Export-Csv "Azure_SecurityRecommendations_20260120.csv" -NoTypeInformation

# For GUI: Navigate to Security Center → Secure Score → Export (PDF/CSV)
```

**AWS Security Hub:**
```bash
# Enable Security Hub (if not already enabled)
aws securityhub enable-security-hub

# Get findings summary
aws securityhub get-findings --filters '{"RecordState": [{"Value": "ACTIVE", "Comparison": "EQUALS"}]}' \
    --output json | jq '.Findings[] | {
    Id: .Id,
    Title: .Title,
    Severity: .Severity.Label,
    Compliance: .Compliance.Status,
    ResourceType: .Resources[0].Type,
    ResourceId: .Resources[0].Id
}' | jq -s '.' > AWS_SecurityHub_Findings_20260120.json

# Export compliance summary
aws securityhub get-compliance-summary --output json > AWS_SecurityHub_Compliance_20260120.json

# For GUI: Navigate to AWS Security Hub → Findings → Export (CSV)
```

**GCP Security Command Center:**
```bash
# List findings
gcloud scc findings list ORGANIZATION_ID --format=json > GCP_SCC_Findings_20260120.json

# For GUI: Navigate to Security Command Center → Findings → Export
```

**Third-Party Tools:**

**Prowler (AWS security assessment):**
```bash
# Install
pip install prowler

# Run assessment
prowler aws -M json,html -o /Evidence/IMP-A.5.23.3/2026-01-20/

# Output: prowler_report_20260120.html (comprehensive security audit)
```

**ScoutSuite (Multi-cloud security audit):**
```bash
# Install
pip install scoutsuite

# Run for AWS
scout aws --report-dir /Evidence/IMP-A.5.23.3/2026-01-20/

# Run for Azure
scout azure --report-dir /Evidence/IMP-A.5.23.3/2026-01-20/

# Output: HTML dashboard showing misconfigurations
```

---

### 5.4 Evidence Storage & Organization

**Directory Structure:**
```
/Evidence/IMP-A.5.23.3/
├── 2026-01-20/                          ← Assessment date folder
│   ├── Identity/
│   │   ├── M365_MFA_Policy_20260120.png
│   │   ├── M365_UserMFAStatus_20260120.csv
│   │   ├── Azure_ConditionalAccess_20260120.json
│   │   └── PIM_Activation_Log_20260120.csv
│   ├── DataProtection/
│   │   ├── Azure_StorageEncryption_20260120.csv
│   │   ├── Azure_KeyVault_Config_20260120.png
│   │   ├── Azure_KeyRotation_Policy_20260120.json
│   │   └── M365_DLP_Policies_20260120.json
│   ├── Network/
│   │   ├── Azure_VirtualNetworks_20260120.csv
│   │   ├── Azure_NSG_Rules_20260120.json
│   │   ├── AWS_SecurityGroups_20260120.json
│   │   └── WAF_Rules_Config_20260120.png
│   ├── Logging/
│   │   ├── SIEM_Query_Results_20260120.csv
│   │   ├── Azure_DiagnosticSettings_20260120.json
│   │   └── LogRetention_Config_20260120.png
│   ├── Backup/
│   │   ├── Azure_BackupPolicies_20260120.json
│   │   ├── Backup_RecoveryTest_Log_Dec2025.pdf
│   │   └── AWS_RDS_Backups_20260120.json
│   ├── SecurityScans/
│   │   ├── Azure_SecureScore_20260120.csv
│   │   ├── AWS_SecurityHub_Findings_20260120.json
│   │   ├── Prowler_Report_20260120.html
│   │   └── SSLLabs_Report_api.example.com_20260120.pdf
│   └── README.md                        ← Index of all evidence files
└── Archive/
    ├── 2025-10-15/                      ← Previous quarter
    └── 2025-07-15/                      ← Q2 2025
```

**README.md Template:**
```markdown
# IMP-A.5.23.3 Evidence Collection - 2026-01-20

## Assessment Details
- **Assessment Date:** 2026-01-20
- **Completed By:** Jane Smith (Cloud Security Engineer)
- **Services Assessed:** 12 cloud services
- **Overall Compliance:** 87.5%

## Evidence Summary

### Identity & Access (4 files)
- M365_MFA_Policy_20260120.png: Screenshot of MFA enforcement policy
- M365_UserMFAStatus_20260120.csv: User export showing MFA enrollment (347/347 users = 100%)
- Azure_ConditionalAccess_20260120.json: Conditional access policy export
- PIM_Activation_Log_20260120.csv: Recent PIM activations (proves JIT is used)

### Data Protection (4 files)
- Azure_StorageEncryption_20260120.csv: Storage account encryption status
- Azure_KeyVault_Config_20260120.png: Key Vault screenshot showing CMK
- Azure_KeyRotation_Policy_20260120.json: Automated key rotation config
- M365_DLP_Policies_20260120.json: DLP policy export

### Network Security (4 files)
- Azure_VirtualNetworks_20260120.csv: VNet configuration
- Azure_NSG_Rules_20260120.json: Network security group rules
- AWS_SecurityGroups_20260120.json: AWS security group export
- WAF_Rules_Config_20260120.png: Web application firewall rules

### Logging & Monitoring (3 files)
- SIEM_Query_Results_20260120.csv: Proof of log ingestion (query from 11 months ago returned results)
- Azure_DiagnosticSettings_20260120.json: Log export configuration
- LogRetention_Config_20260120.png: Retention set to 365 days

### Backup & Recovery (3 files)
- Azure_BackupPolicies_20260120.json: Automated backup policies
- Backup_RecoveryTest_Log_Dec2025.pdf: Quarterly recovery test results
- AWS_RDS_Backups_20260120.json: RDS automated backup configuration

### Security Scans (4 files)
- Azure_SecureScore_20260120.csv: Microsoft Secure Score (82/100)
- AWS_SecurityHub_Findings_20260120.json: AWS Security Hub findings
- Prowler_Report_20260120.html: Comprehensive AWS security audit
- SSLLabs_Report_api.example.com_20260120.pdf: TLS configuration validation (Grade A)

## Total Evidence Files: 22
```

---

### 5.5 Evidence Quality Checks

**Before Submitting Evidence, Verify:**
```
QUALITY CHECKLIST:

☐ Timestamp Verification
  ├─ All screenshots show visible timestamp (system clock or service UI)
  ├─ All config exports have filename timestamp matching collection date
  └─ File metadata (creation date) aligns with collection date

☐ Completeness
  ├─ Evidence proves the claim (e.g., "MFA enabled" → user list shows 100% MFA)
  ├─ No partial screenshots (entire setting visible, not cropped)
  └─ Config exports are complete (not truncated due to API limits)

☐ Clarity
  ├─ Screenshots are high resolution (readable text, no blurry images)
  ├─ Key settings are highlighted or annotated (red box, arrow)
  └─ Context is clear (navigation breadcrumbs visible, service name shown)

☐ Sensitivity
  ├─ No passwords, API keys, or secrets visible in screenshots
  ├─ Personal data redacted (customer names, email addresses if not needed)
  └─ Internal IP addresses obscured (if required by security policy)

☐ Accessibility
  ├─ Evidence files stored in designated evidence repository
  ├─ File permissions set correctly (accessible to auditors, not public)
  └─ Hyperlinks in Evidence Register (Sheet 9) are valid and accessible

☐ Correlation
  ├─ Evidence ID matches Evidence Register (Sheet 9)
  ├─ Evidence filename matches convention ([Service]_[Area]_[Setting]_[Date])
  └─ Multiple pieces of evidence for same claim are cross-referenced
```

---

### 5.6 Handling Missing Evidence

**Common Scenarios:**

**Scenario 1: Vendor Doesn't Provide Config Export API**
```
Problem: SaaS service has no API, only GUI (can't export config programmatically)

Solution:
  1. Primary: Screenshot (SILVER evidence)
  2. Annotation: Note in Evidence Register: "No API available per vendor documentation"
  3. Supplementary: Email from vendor support confirming no export capability
  4. Quality boost: Use browser developer tools to capture network requests (JSON responses)
```

**Scenario 2: Historical Evidence Not Available**
```
Problem: Need to prove MFA was enabled 6 months ago, but no historical export

Solution:
  1. Current evidence + audit log: Screenshot of MFA policy NOW + audit log showing policy created 1 year ago (proves continuous enforcement)
  2. Attestation: Written statement from IT Ops: "MFA has been enforced since [date]"
  3. Risk acceptance: Document gap, request quarterly evidence collection going forward
```

**Scenario 3: Evidence Contains Sensitive Data**
```
Problem: Config export includes customer data, IP addresses, or secrets

Solution:
  1. Redaction: Use tool to redact sensitive fields BEFORE saving
     - PowerShell: $data | Select-Object * -ExcludeProperty Password, SecretKey
     - jq: jq 'del(.password, .apiKey)' config.json
  2. Anonymization: Replace real data with placeholders
     - "user@customer.com" → "user@example.com"
     - "10.0.1.5" → "10.x.x.x"
  3. Segregation: Store sensitive evidence in restricted-access folder
```

**Scenario 4: Evidence is Too Large**
```
Problem: Config export is 500MB JSON file (too large for evidence repository)

Solution:
  1. Summary: Extract relevant sections only
     - Full export: aws ec2 describe-instances (huge)
     - Filtered: aws ec2 describe-instances | jq '[.Reservations[].Instances[] | {InstanceId, State}]'
  2. Compression: ZIP/GZIP the file
     - gzip AWS_EC2_Instances_20260120.json (reduces 500MB → 50MB)
  3. External storage: Store in S3/Azure Blob, provide signed URL in Evidence Register
```

**Scenario 5: Evidence Contradicts Claim**
```
Problem: Assessment says "MFA Enabled" but user export shows 80% MFA enrollment (not 100%)

Solution (Implementer):
  1. Update status to ⚠️ Partial or ❌ Non-Compliant (reflect reality)
  2. Document gap: "MFA policy configured but 20% users not enrolled"
  3. Remediation: Force MFA enrollment, set target date
  4. Re-collect evidence after fix

Solution (Auditor):
  1. Escalate: Notify assessment coordinator of discrepancy
  2. Request correction: Assessment status must match evidence
  3. If not corrected: Issue audit finding
```

---

### 5.7 Screenshot Best Practices - Detailed Examples

**Example 1: Good Screenshot (Azure MFA Policy)**
```
✅ GOOD SCREENSHOT EXAMPLE:

Filename: Azure_MFA_ConditionalAccess_Policy_20260120.png

What it shows:
  - Azure Portal header (proves service: "Microsoft Azure")
  - Navigation breadcrumbs: "Azure Active Directory > Security > Conditional Access"
  - Policy name: "Require MFA for All Users"
  - State: "On" (not "Report-only")
  - Conditions: "All users" (not "Selected users")
  - Grant controls: "Require multi-factor authentication" (checked)
  - System clock visible: "1/20/2026 2:35 PM UTC" (bottom-right taskbar)
  - Key setting highlighted: Red box around "State: On"

Why it's good:
  ✓ Timestamp visible (proves recency)
  ✓ Context clear (know exactly where in Azure this is)
  ✓ Completeness (entire policy visible, no cropping)
  ✓ Highlight (red box draws eye to critical setting)
  ✓ No sensitive data (policy name is generic)
```

**Example 2: Bad Screenshot (AWS S3 Encryption)**
```
❌ BAD SCREENSHOT EXAMPLE:

Filename: screenshot1.png

What it shows:
  - Partial view of AWS console (service name not visible)
  - "Encryption" tab selected
  - "Enabled" toggle visible
  - No timestamp
  - No bucket name visible
  - Screenshot cropped (edges cut off)
  - No highlighting

Why it's bad:
  ✗ No timestamp (could be from any date)
  ✗ No context (which bucket? which AWS account?)
  ✗ Incomplete (cropped edges might hide important settings)
  ✗ Filename meaningless ("screenshot1" tells auditor nothing)
  ✗ No annotation (auditor must hunt for relevant setting)
```

---

### 5.8 Config Export Formats - Comparison

| Format | Pros | Cons | Best Use Case |
|--------|------|------|---------------|
| **JSON** | Machine-readable, widely supported, preserves structure | Can be large, harder for humans to read | API exports, cloud config, structured data |
| **CSV** | Excel-compatible, easy to filter/sort, human-readable | Loses hierarchical structure, escaping issues | User lists, RBAC assignments, tabular data |
| **YAML** | Human-readable, supports comments, preserves structure | Less universal than JSON, parsing issues | IaC templates (Kubernetes, Ansible), config files |
| **XML** | Universal, preserves hierarchy, schema validation | Verbose, harder to parse, declining popularity | Legacy systems, SOAP APIs, enterprise configs |
| **Terraform State** | Infrastructure-as-Code source of truth, includes dependencies | Sensitive (contains secrets), requires Terraform to parse | IaC-managed infrastructure evidence |
| **ARM Template (Azure)** | Complete infrastructure definition, idempotent | Azure-specific, complex for large deployments | Azure IaC evidence |
| **CloudFormation (AWS)** | Complete infrastructure definition, AWS-native | AWS-specific, large templates hard to read | AWS IaC evidence |

**Format Selection Guide:**
```
IF source is cloud API (Azure, AWS, GCP):
   THEN export as JSON (native format, best structure preservation)

ELIF source is user/role list (tabular data):
   THEN export as CSV (Excel-compatible, easy analysis)

ELIF source is Infrastructure-as-Code:
   THEN use native IaC format (Terraform, ARM, CloudFormation)
   AND also export Terraform state OR ARM deployment output as JSON

ELIF source is legacy system:
   THEN accept XML (but convert to JSON if possible for consistency)

ELSE:
   THEN default to JSON (most versatile)
```

---

### 5.9 Evidence Collection Timeline

**Recommended Schedule:**
```
WEEK 1: Preparation
  Day 1-2: Set up evidence repository, install tools
  Day 3-5: Test export scripts, verify access

WEEK 2: Identity & Data Protection Evidence
  Day 1: Identity exports (MFA, RBAC, PIM)
  Day 2: Data protection exports (encryption, keys, DLP)
  Day 3: Screenshots for both areas
  Day 4: Quality review, organize files
  Day 5: Update Evidence Register (Sheet 9)

WEEK 3: Network, Logging, Backup Evidence
  Day 1: Network exports (firewalls, NSGs, WAF)
  Day 2: Logging exports (SIEM queries, retention)
  Day 3: Backup exports (policies, recovery tests)
  Day 4: Screenshots for all three areas
  Day 5: Quality review, organize files

WEEK 4: Security Scans & Final Validation
  Day 1-2: Run security scans (Prowler, Security Hub, Secure Score)
  Day 3: SSL/TLS scans for all endpoints
  Day 4: Evidence quality audit (verify all files accessible, timestamped)
  Day 5: Final Evidence Register update, README.md creation

TOTAL: 4 weeks for comprehensive evidence collection
```

---

**END OF SECTION 5: EVIDENCE COLLECTION GUIDE**

## Section 6: Common Pitfalls & How to Avoid Them

### 6.1 The Seven Deadly Sins of Configuration Assessment
```
┌─────────────────────────────────────────────────────────────────┐
│              THE SEVEN DEADLY CONFIGURATION SINS                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  1. ASSUMPTION      "It's Microsoft/AWS, surely it's secure"    │
│  2. DIVERGENCE      Production ≠ Dev configs (drift)            │
│  3. PROCRASTINATION "We'll enable MFA next quarter"             │
│  4. INCOMPLETENESS  Untested backups, unverified encryption     │
│  5. INVISIBILITY    Shadow IT, undocumented service accounts    │
│  6. OBSOLESCENCE    Stale evidence, expired certifications      │
│  7. DISCONNECTION   Assessment doesn't reflect reality          │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 6.2 Pitfall #1: Assuming Default Configs Are Secure

**The Mistake:**
```
❌ "We deployed AWS/Azure/GCP using the default settings. Those vendors 
   are secure, right? We don't need to check configurations."
```

**Why It's Wrong:**

Cloud providers optimize for **ease of use**, not **security**. Default configurations are designed to get services running quickly, often sacrificing security for convenience.

**Real-World Examples:**

| Service | Insecure Default | Security Risk | Breach Example |
|---------|------------------|---------------|----------------|
| **AWS S3** | Public read access possible | Data exposure | Capital One (2019): Misconfigured S3 bucket exposed 100M+ customer records |
| **Azure Storage** | No encryption at rest (before 2018) | Data theft | Misconfigured storage accounts exposed patient health records |
| **Microsoft 365** | Basic authentication enabled | Credential spraying | Thousands of compromises via legacy auth protocols |
| **GCP Compute** | Default service account with editor role | Privilege escalation | Cryptojacking attacks via over-privileged service accounts |
| **Salesforce** | Password-only auth (no MFA) | Account takeover | Multiple breaches via phished credentials |

**The Fix:**
```
✅ ALWAYS verify configuration, never assume:

Step 1: Download vendor security baseline/hardening guide
   - Azure: https://docs.microsoft.com/en-us/security/benchmark/azure/
   - AWS: https://docs.aws.amazon.com/securityhub/latest/userguide/standards.html
   - GCP: https://cloud.google.com/security/compliance/cis-benchmark
   - Microsoft 365: https://docs.microsoft.com/en-us/microsoft-365/security/

Step 2: Compare actual config vs. baseline (use security posture tools)
   - Azure: Enable Microsoft Defender for Cloud (Secure Score)
   - AWS: Enable AWS Security Hub with CIS benchmark
   - GCP: Enable Security Command Center with CIS GCP Foundation

Step 3: Document ALL deviations from baseline
   - If config differs from baseline → Justify in writing OR remediate
   - "We disabled X because..." (documented exception)
   - No undocumented deviations allowed

Step 4: Evidence-based verification
   - Don't trust vendor dashboard claims alone
   - Export config, verify with scripts
   - Example: S3 bucket says "Private" → Verify with aws s3api get-public-access-block
```

**Implementer Perspective:**
*"Secure by default" is marketing. "Verify by config export" is engineering.*

**Auditor Perspective:**
*If you tell me "it's default, so it's fine," I immediately escalate scrutiny. Defaults change, configs drift, assumptions kill compliance programs.*

---

### 6.3 Pitfall #2: Configuration Drift Between Environments

**The Mistake:**
```
❌ Production is locked down (MFA, encryption, private endpoints), but 
   Dev/Test are "open" (no MFA, public access, plain HTTP) because 
   "it's just dev, doesn't matter."
```

**Why It's Wrong:**

1. **Dev environments often contain production data** (copied for testing)
2. **Attackers pivot from dev to prod** (weak link in the chain)
3. **Developers have admin rights in dev** (more attack surface)
4. **Compliance violations** (GDPR doesn't distinguish prod vs. dev data)

**Real-World Scenario:**
```
Company: FinTech startup
Incident: Ransomware attack

Attack Path:
  1. Phished developer credentials (no MFA on dev environment)
  2. Accessed dev Azure subscription (public-facing admin portal)
  3. Found production database connection string in dev environment variables
  4. Pivoted to production database
  5. Exfiltrated customer data, deployed ransomware

Root Cause: Dev environment treated as "low security" despite access to prod secrets

Cost: $2M ransom + $5M breach notification/remediation + regulatory fines
```

**The Fix:**
```
✅ Establish environment-based security tiers:

TIER 1: Production
  - MFA: MANDATORY (all users, no exceptions)
  - Encryption: Customer-managed keys (CMK)
  - Network: Private endpoints only, IP allowlisting for admin
  - Logging: 365+ day retention, real-time SIEM
  - Backup: 3-2-1 rule, quarterly recovery testing
  - Compliance: 100% (no risk exceptions)

TIER 2: Staging/UAT
  - MFA: MANDATORY (all users)
  - Encryption: Provider-managed keys acceptable (if non-prod data)
  - Network: Private endpoints preferred, public with IP allowlist acceptable
  - Logging: 365 day retention, daily SIEM sync
  - Backup: Daily backups, annual recovery testing
  - Compliance: ≥95% (minor exceptions allowed with approval)

TIER 3: Development
  - MFA: MANDATORY (all users) ← STILL REQUIRED
  - Encryption: At rest (provider keys), TLS 1.2+ in transit
  - Network: Public access allowed BUT segregated from prod (separate VNet/VPC)
  - Logging: 90 day retention minimum, weekly SIEM sync
  - Backup: Weekly backups, tested on setup (then annually)
  - Compliance: ≥90% (exceptions documented)

TIER 4: Test/Sandbox
  - MFA: MANDATORY (all users) ← ALWAYS
  - Encryption: Basic encryption acceptable
  - Network: Isolated (no access to prod networks)
  - Logging: 30 day retention
  - Backup: Optional (if ephemeral)
  - Compliance: ≥85% (but MFA/logging/network isolation non-negotiable)

KEY PRINCIPLE: No environment is exempt from MFA, logging, or network isolation.
```

**Configuration Drift Detection:**
```powershell
# Example: Compare Azure NSG rules across environments

# Production
$prodRules = Get-AzNetworkSecurityGroup -ResourceGroupName "prod-rg" | 
    Select-Object -ExpandProperty SecurityRules

# Development  
$devRules = Get-AzNetworkSecurityGroup -ResourceGroupName "dev-rg" | 
    Select-Object -ExpandProperty SecurityRules

# Compare
Compare-Object -ReferenceObject $prodRules -DifferenceObject $devRules -Property Name, SourceAddressPrefix, DestinationPortRange |
    Export-Csv "Environment_Config_Drift_20260120.csv"

# Expected: Dev is LESS restrictive than Prod, but NOT "allow 0.0.0.0/0"
# Red flag: Dev has rules Prod doesn't (possibly overly permissive)
```

**Implementer Perspective:**
*"Dev environment = training ground for attackers. Secure it like it's one hop from production, because it often is."*

**Auditor Perspective:**
*I randomly select 5 services, export configs from all environments, compare side-by-side. If dev is radically different from prod without documented justification, that's a finding.*

---

### 6.4 Pitfall #3: "We'll Fix It Next Quarter" Syndrome

**The Mistake:**
```
❌ Assessment Status: ⚠️ Partial
   Gap: "MFA not enforced for all users"
   Remediation Date: Q2 2026
   
   [6 months later]
   
   Assessment Status: ⚠️ Partial (still)
   Gap: "MFA not enforced for all users" (still)
   Remediation Date: Q4 2026 (postponed again)
```

**Why It's Wrong:**

1. **Security debt compounds** (attackers don't wait for your roadmap)
2. **Regulatory deadlines don't move** (DORA, NIS2 have fixed compliance dates)
3. **"Partial" becomes permanent** (normalization of deviance)
4. **Audit findings accumulate** (eventually becomes unmaintainable)

**Common Excuses (and Rebuttals):**

| Excuse | Rebuttal |
|--------|----------|
| "Users will complain about MFA" | Users complain more about data breaches. Implement gradually, communicate benefits. |
| "We don't have budget for CMK" | Azure Key Vault CMK costs ~$1/key/month. A breach costs $4M+ average. |
| "It's technically complex" | That's why you have engineers. If too complex, hire consultant or simplify architecture. |
| "Business won't accept downtime" | MFA enablement requires zero downtime. No excuse. |
| "We're waiting for new platform" | Secure current platform NOW, migrate security configs to new platform later. |

**The Fix:**
```
✅ Treat security gaps like production outages:

CRITICAL Gaps (Status: ❌ Non-Compliant):
  - Remediation: ≤7 days (emergency change process)
  - Escalation: Daily updates to CISO
  - Workaround: Implement compensating controls immediately
  - Examples: No MFA on critical service, encryption disabled, public database

HIGH Gaps (Status: ⚠️ Partial, high impact):
  - Remediation: ≤30 days
  - Escalation: Weekly updates to Security team
  - Prioritization: Top of sprint backlog
  - Examples: MFA only for admins (not all users), manual key rotation, no SIEM integration

MEDIUM Gaps (Status: ⚠️ Partial, medium impact):
  - Remediation: ≤90 days
  - Escalation: Monthly updates
  - Prioritization: Normal backlog priority
  - Examples: Service accounts missing owners, backup testing overdue, DLP not configured

LOW Gaps (Status: ⚠️ Partial, low impact):
  - Remediation: ≤180 days (next major release)
  - Escalation: Quarterly review
  - Prioritization: Technical debt backlog
  - Examples: Older TLS version still supported (but 1.2+ available), classification labels optional

NO PERPETUAL "PARTIAL" STATUS:
  - If gap persists >2 quarters → Escalate to CISO for decision:
    Option A: Commit resources to fix (set firm date)
    Option B: Accept risk formally (document in risk register)
    Option C: Decommission service (if can't secure, don't use)
```

**Remediation Tracking Example:**
```
Gap: "MFA not enforced for all users - 247/347 users have MFA (71%)"

Week 1: 
  - Email all users without MFA: "Enable MFA by [DATE] or account will be disabled"
  - Provide MFA setup instructions
  - Current: 71% → Target: 85%

Week 2:
  - Follow-up email + helpdesk support for users with issues
  - Current: 85% → Target: 95%

Week 3:
  - Escalate to managers for remaining users
  - Current: 95% → Target: 98%

Week 4:
  - Conditional Access policy: Enforce MFA (blocks login without MFA)
  - Create emergency access accounts (2 accounts with MFA, documented)
  - Current: 100% (policy-enforced)
  
Result: Gap closed in 30 days, status updated to ✅ Compliant
```

**Implementer Perspective:**
*Set realistic remediation dates, then HIT THEM. Missing dates erodes trust and credibility.*

**Auditor Perspective:**
*I track remediation promises across quarters. If same gap appears in 3 consecutive assessments, it's a control failure (not just a gap).*

---

### 6.5 Pitfall #4: Untested Backup Recovery

**The Mistake:**
```
❌ Assessment Status: ✅ Compliant
   Backup Enabled: Yes
   Backup Frequency: Daily
   Last Recovery Test: [blank] or "Never"
```

**Why It's Wrong:**

**Untested backups = No backups.** You discover backup corruption during a real incident (worst possible time).

**Real-World Horror Stories:**
```
Company A: Healthcare provider
Incident: Ransomware encrypted production database
Backup Status: "Enabled" for 2 years, never tested
Result: Backup restoration FAILED (corrupt backup file, undetected)
Outcome: Lost 6 months of patient records, $8M lawsuit, regulatory sanctions

Company B: E-commerce platform  
Incident: Database server crash
Backup Status: Daily backups to S3 for 1 year
Result: Backup restoration FAILED (IAM permissions misconfigured, could read but not restore)
Outcome: 48-hour outage, $2M revenue loss, customer exodus

Company C: SaaS startup
Incident: Developer accidentally deleted production data
Backup Status: Automated backups every 6 hours
Result: Restoration successful BUT took 16 hours (no runbook, trial-and-error)
Outcome: Exceeded RTO (4 hours), SLA penalties, reputation damage
```

**The Fix:**
```
✅ Quarterly backup recovery testing (MANDATORY):

Q1 Test (January-March):
  Scope: File-level restore
  Procedure:
    1. Select random file from backup (customer record, config file)
    2. Restore to separate test environment (not production!)
    3. Verify file integrity (checksum, content validation)
    4. Document restore time (should be <15 minutes for file)
  Pass Criteria: File restored successfully, content matches original
  Evidence: Recovery test log (PDF), restored file screenshot

Q2 Test (April-June):
  Scope: Database restore (partial)
  Procedure:
    1. Select random database table from backup
    2. Restore to test database instance
    3. Verify table schema and row count
    4. Run integrity check (DBCC CHECKDB for SQL, pg_dump for PostgreSQL)
  Pass Criteria: Table restored, no corruption detected
  Evidence: Database restore log, integrity check results

Q3 Test (July-September):
  Scope: Full service restore (simulated DR)
  Procedure:
    1. Provision DR environment (separate region/datacenter)
    2. Restore FULL service from backup (database, config, files)
    3. Start service, verify functionality (automated tests)
    4. Measure restore time (must meet RTO)
  Pass Criteria: Service fully functional in DR environment within RTO
  Evidence: DR test report (end-to-end), RTO measurement

Q4 Test (October-December):
  Scope: Backup encryption validation
  Procedure:
    1. Attempt to restore backup without encryption keys (should fail)
    2. Restore with valid keys (should succeed)
    3. Verify backup is encrypted at rest (not plaintext)
  Pass Criteria: Cannot restore without keys, successful with keys
  Evidence: Encryption test log, failed restore screenshot

Annual Test (Once per year):
  Scope: Full disaster recovery drill
  Procedure:
    1. Simulate total production failure (notify stakeholders, non-working hours)
    2. Restore entire service to DR site from backups
    3. Cutover DNS/traffic to DR site
    4. Validate service with real users (internal QA team)
    5. Measure time from "incident" to "service restored"
  Pass Criteria: Service restored and validated within RTO
  Evidence: DR drill report (comprehensive), lessons learned document
```

**Recovery Test Evidence Example:**
```
QUARTERLY BACKUP RECOVERY TEST REPORT

Test Date: 2026-01-15
Test Type: Database Restore (Partial)
Service: Azure SQL Database - Production CRM
Tester: John Doe (Database Administrator)

Backup Details:
  - Backup Date: 2026-01-14 23:00 UTC (automated daily backup)
  - Backup Size: 45 GB
  - Backup Location: Azure Blob Storage (GRS)
  - Backup Encryption: Yes (AES-256, provider-managed key)

Test Procedure:
  1. Created test database instance: crm-test-restore-20260115
  2. Initiated restore from backup: crm-prod-backup-20260114
  3. Restore started: 10:05 UTC
  4. Restore completed: 10:23 UTC (18 minutes)
  5. Ran integrity check: DBCC CHECKDB (crm-test-restore-20260115)
  6. Result: 0 errors, 0 warnings

Validation:
  ✓ Table count matches: 147 tables (expected 147)
  ✓ Row count spot-check: Customers table = 2,547,892 rows (matches production)
  ✓ No corruption detected
  ✓ Sample query executed successfully: SELECT TOP 100 FROM Customers
  
Restore Time: 18 minutes (RTO target: 4 hours) → PASS

Lessons Learned:
  - Restore process well-documented, followed without issues
  - Restore time well within RTO (comfortable margin)
  - No action items

Next Test: Q2 2026 (Full service restore to DR region)

Signed: John Doe, DBA
Approved: Jane Smith, CISO
```

**Implementer Perspective:**
*"Schedule backup testing like you schedule backups - automated, recurring, non-negotiable. If it's not in the calendar, it won't happen."*

**Auditor Perspective:**
*I request the last 4 quarterly backup test reports. If ANY quarter is missing, backup status cannot be "Compliant." Testing is part of the control, not optional.*

---

### 6.6 Pitfall #5: Ignoring Shadow IT Configurations

**The Mistake:**
```
❌ "We assessed all cloud services in our inventory. We're compliant!"
   
   [Meanwhile, Marketing deployed HubSpot without IT knowledge]
   [Sales deployed Dropbox Business without security review]
   [R&D spun up AWS sandbox account using personal credit card]
```

**Why It's Wrong:**

1. **Shadow IT is typically LESS secure** (no IT oversight, no security baseline)
2. **Contains real business data** (not just "testing")
3. **Creates compliance gaps** (services not in inventory → not assessed → not compliant)
4. **Vendor sprawl** (duplicate services, wasted costs)

**Detection Methods:**
```
METHOD 1: Cloud Access Security Broker (CASB)
  Tools: Microsoft Defender for Cloud Apps, Netskope, Zscaler
  How: Monitors network traffic, detects OAuth app connections
  Example: CASB alerts "User john@company.com authorized Trello (unapproved app)"

METHOD 2: Expense Report Analysis
  Process: Finance exports all credit card transactions
  Filter: "SaaS" vendors (Stripe, PayPal recurring charges)
  Compare: Expense vendors vs. approved vendor list
  Example: "$99/month Airtable subscription - not in IT inventory"

METHOD 3: DNS Query Logs
  Process: Export DNS queries from firewall/proxy logs
  Filter: SaaS domains (*.salesforce.com, *.dropbox.com, *.slack.com)
  Compare: Accessed SaaS vs. inventory
  Example: "50 users queried hubspot.com daily - not in inventory"

METHOD 4: OAuth App Audit (for Microsoft 365, Google Workspace)
  Process: List all third-party apps with OAuth permissions
  PowerShell:
    Get-AzureADServicePrincipal -All $true | 
      Where-Object {$_.Tags -contains "WindowsAzureActiveDirectoryIntegratedApp"} |
      Select-Object DisplayName, AppId, ReplyUrls
  Compare: OAuth apps vs. approved list
  Example: "Zapier has OAuth access to M365 - not approved"

METHOD 5: User Survey
  Process: Quarterly survey "What cloud services do you use for work?"
  Anonymous: Encourages honest reporting
  Analysis: Cross-reference responses vs. inventory
  Example: "35% of users admitted using Google Drive (not approved)"
```

**Shadow IT Remediation Process:**
```
DISCOVERED SHADOW IT SERVICE: Dropbox Business (Sales Team)

Step 1: ASSESS RISK (within 48 hours)
  ☐ What data is stored? (Customer contact lists, sales presentations)
  ☐ How sensitive? (Internal - customer names, not Restricted)
  ☐ How many users? (23 users in Sales)
  ☐ Current security? (No MFA, no encryption, public sharing enabled)
  Risk Rating: MEDIUM-HIGH (sensitive data, poor security)

Step 2: IMMEDIATE CONTAINMENT (if HIGH/CRITICAL risk)
  ☐ If CRITICAL (Restricted data, no encryption): Block access immediately
  ☐ If HIGH: Require MFA within 7 days or block
  ☐ If MEDIUM: Allow continued use during evaluation (30 days)
  Action: Required MFA within 7 days (Dropbox supports SSO)

Step 3: EVALUATE ALTERNATIVES (1-2 weeks)
  ☐ Do we have approved equivalent? (Yes - OneDrive for Business)
  ☐ Can we migrate? (Yes - Dropbox to OneDrive migration tool exists)
  ☐ Business justification for Dropbox? (Sales: "We've always used it")
  Decision: Migrate to OneDrive (approved, better integration)

Step 4: MIGRATION PLAN (2-4 weeks)
  ☐ Export data from Dropbox (Sales team responsibility)
  ☐ Import to OneDrive (IT assistance)
  ☐ Update links in CRM (Sales team)
  ☐ Training on OneDrive (IT provides)
  ☐ Decommission Dropbox (cancel subscription)
  Timeline: 30 days

Step 5: PREVENT RECURRENCE
  ☐ Add Dropbox to blocked app list (CASB or firewall)
  ☐ Update policy: "All SaaS requires IT approval before purchase"
  ☐ Communicate: "Why we don't allow Dropbox" (security, compliance)
  ☐ Add OneDrive to approved service list (easy alternative)
```

**Implementer Perspective:**
*"Shadow IT happens because IT says 'no' without offering a 'yes' alternative. Provide secure alternatives BEFORE users go rogue."*

**Auditor Perspective:**
*I request CASB reports, expense reports, DNS logs during audits. If I discover unapproved services that weren't in your assessment, that's a material finding (control failure).*

---

### 6.7 Pitfall #6: Stale Evidence

**The Mistake:**
```
❌ Assessment Date: 2026-01-20
   Evidence: Azure_MFA_Policy_Screenshot_20250415.png (9 months old!)
   
   Auditor: "This screenshot is from last April. How do I know MFA is still enabled TODAY?"
```

**Why It's Wrong:**

1. **Configurations change** (intentional updates or accidental drift)
2. **Evidence staleness reduces credibility** (auditor questions everything)
3. **Regulatory requirements** (evidence must be current, typically <90 days)
4. **Real risk** (MFA could have been disabled since screenshot taken)

**The Fix:**
```
✅ Evidence freshness requirements:

TIER 1: Critical Configurations (MFA, Encryption, Network Isolation)
  - Evidence Age: ≤30 days
  - Re-collection: Monthly verification
  - Rationale: Changes here = critical risk

TIER 2: Important Configurations (RBAC, Logging, Backup)
  - Evidence Age: ≤90 days (quarterly assessment cycle)
  - Re-collection: Quarterly with assessment
  - Rationale: Slower-changing, less critical

TIER 3: Static Configurations (Vendor certs, contracts, DPA)
  - Evidence Age: ≤365 days (annual review cycle)
  - Re-collection: Annually or when vendor changes
  - Rationale: Rarely changes, contractual (not technical)

ALWAYS RE-COLLECT EVIDENCE FOR CURRENT ASSESSMENT:
  - Don't reuse evidence from previous quarter
  - Exception: Static configs unchanged (verify, then reference)
  - Document verification: "Config verified unchanged on [DATE], previous evidence still valid"
```

**Evidence Timestamp Validation Script:**
```powershell
# Check evidence file timestamps, flag stale files

$evidencePath = "/Evidence/IMP-A.5.23.3/2026-01-20/"
$today = Get-Date
$staleThresholdDays = 90

Get-ChildItem -Path $evidencePath -Recurse -File | ForEach-Object {
    $file = $_
    $age = ($today - $file.LastWriteTime).Days
    
    $status = if ($age -le 30) { "✅ FRESH" }
              elseif ($age -le 90) { "⚠️ AGING" }
              else { "❌ STALE" }
    
    [PSCustomObject]@{
        FileName = $file.Name
        LastModified = $file.LastWriteTime
        AgeDays = $age
        Status = $status
        Path = $file.FullName
    }
} | Where-Object {$_.Status -eq "❌ STALE"} | 
    Export-Csv "Stale_Evidence_Report_20260120.csv" -NoTypeInformation

# If any STALE files for critical configs → Re-collect immediately
```

---

### 6.8 Pitfall #7: Assessment Doesn't Reflect Reality

**The Mistake:**
```
❌ Assessment says: "✅ Compliant - MFA Enforced for All Users"
   Reality: Conditional Access policy in "Report-only" mode (not enforcing)
   
   OR
   
   Assessment says: "✅ Compliant - Private Endpoints Configured"
   Reality: Private endpoint exists but public access ALSO enabled (defeating purpose)
```

**Why It's Wrong:**

**Cargo cult compliance:** Checking boxes without understanding what they mean. Looks good on paper, provides zero security.

**The Fix:**
```
✅ VERIFY, DON'T TRUST:

Bad Practice: "Policy exists" → ✅ Compliant
Good Practice: "Policy exists AND is enforced" → ✅ Compliant

Examples:

MFA Policy:
  ❌ BAD: Policy named "Require MFA for All Users" exists
  ✅ GOOD: Policy enabled, state = "On" (not "Report-only"), user export shows 100% MFA active

Encryption:
  ❌ BAD: Encryption toggle = "Enabled" in UI
  ✅ GOOD: Config export shows encryptionEnabled=true AND test file uploaded/downloaded confirms encryption

Private Endpoint:
  ❌ BAD: Private endpoint resource exists in Azure
  ✅ GOOD: Public access = "Disabled", attempted connection from internet = FAILED

Backup:
  ❌ BAD: Backup policy configured
  ✅ GOOD: Backup jobs ran successfully (last 7 days), recovery test passed (last 90 days)
```

**Reality Check Process:**
```
FOR EACH "✅ Compliant" STATUS:

Step 1: Review claim
  - What exactly are we claiming is compliant?

Step 2: Verify configuration
  - Export config programmatically (JSON/CSV)
  - Don't rely only on GUI screenshots

Step 3: Test functionality
  - MFA: Try logging in without MFA (should fail)
  - Encryption: Upload test file, download, verify encrypted
  - Private endpoint: Try accessing from internet (should fail)
  - Backup: Restore test file from backup (should succeed)

Step 4: Evidence correlation
  - Do ALL pieces of evidence support the claim?
  - If evidence contradicts claim → Update claim (not evidence!)

Step 5: Peer review
  - Have second person verify "Compliant" claims
  - Fresh eyes catch wishful thinking
```

**Implementer Perspective:**
*"Don't fool yourself. If you're not sure it's actually configured correctly, change status to Partial and investigate."*

**Auditor Perspective:**
*I test random "Compliant" claims. If I can defeat a control (e.g., login without MFA when policy says required), entire assessment's credibility collapses.*

---

### 6.9 Quick Reference: Pitfall Prevention Checklist

**Before Finalizing Assessment:**
```
☐ Configuration Defaults
  ├─ Compared actual configs vs. vendor security baseline
  ├─ No "default = secure" assumptions
  └─ All deviations from baseline documented/justified

☐ Environment Consistency
  ├─ Verified Prod, Stage, Dev configs (no >1 tier gap)
  ├─ MFA enforced in ALL environments
  └─ Network isolation between environments verified

☐ Remediation Discipline
  ├─ All remediation dates are realistic
  ├─ No perpetual "Partial" status (>2 quarters)
  └─ CRITICAL gaps have ≤7 day remediation commitment

☐ Backup Testing
  ├─ Last recovery test ≤90 days ago
  ├─ Recovery test PASSED (not just "attempted")
  └─ RTO/RPO measured and documented

☐ Shadow IT Detection
  ├─ CASB reports reviewed (or DNS logs if no CASB)
  ├─ Expense reports checked for unapproved SaaS
  └─ OAuth app audit completed (M365/Google Workspace)

☐ Evidence Freshness
  ├─ All evidence ≤90 days old (≤30 days for critical configs)
  ├─ Evidence timestamps match assessment date
  └─ Stale evidence flagged and re-collected

☐ Reality Alignment
  ├─ All "Compliant" claims verified (not assumed)
  ├─ Configs tested (not just documented)
  └─ Peer review of high-risk claims completed

☐ Stakeholder Coordination
  ├─ IT Ops reviewed for technical accuracy
  ├─ Security reviewed for adequacy
  └─ CISO aware of HIGH/CRITICAL findings before formal submission
```

---

**END OF SECTION 6: COMMON PITFALLS & HOW TO AVOID THEM**

## Section 7: Quality Checklist

### 7.1 The Three-Gate Quality Framework
```
┌─────────────────────────────────────────────────────────────────┐
│              THE THREE GATES OF QUALITY                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  GATE 1: COMPLETENESS                                            │
│          "Have we assessed everything we should?"                │
│          ├─ All services from inventory present                  │
│          ├─ All sheets (2-10) completed                          │
│          └─ No blank cells in required columns                   │
│                                                                   │
│  GATE 2: ACCURACY                                                │
│          "Is our assessment technically correct?"                │
│          ├─ Status matches evidence                              │
│          ├─ Configurations verified, not assumed                 │
│          └─ No contradictions between sheets                     │
│                                                                   │
│  GATE 3: EVIDENCE                                                │
│          "Can we prove our claims to an auditor?"                │
│          ├─ Every Compliant has evidence                         │
│          ├─ Evidence is current (<90 days)                       │
│          └─ Evidence is accessible and high quality              │
│                                                                   │
│  ONLY AFTER PASSING ALL THREE GATES:                             │
│  → Submit for approval (Sheet 10)                                │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 7.2 Gate 1: Completeness Checks

**Pre-Submission Completeness Audit:**
```
SHEET-BY-SHEET COMPLETENESS:

☐ Sheet 1: Instructions & Legend
  ├─ Document information block filled (Assessment Date, Completed By)
  ├─ Contact information current
  └─ Review cycle confirmed (Quarterly)

☐ Sheet 2: Identity & Access Configuration
  ├─ All services from IMP-5.23.1 inventory are present
  ├─ Extended columns (R-X) completed for each service
  ├─ No blank Status cells (Column H)
  ├─ Checklist completed (below data rows)
  └─ Evidence IDs referenced in Column I

☐ Sheet 3: Data Protection Configuration
  ├─ All services from IMP-5.23.1 inventory are present
  ├─ Extended columns (R-X) completed for each service
  ├─ CMK assessment for Restricted/Confidential data
  ├─ Checklist completed
  └─ Evidence IDs referenced in Column I

☐ Sheet 4: Network Security Configuration
  ├─ All services with network exposure assessed
  ├─ Public endpoint count documented (Column X)
  ├─ Each public endpoint justified (Gap Description if >0)
  ├─ Checklist completed
  └─ Evidence IDs referenced in Column I

☐ Sheet 5: Logging & Monitoring Configuration
  ├─ All services assessed for logging
  ├─ Log retention verified ≥365 days (Column U)
  ├─ SIEM integration status documented (Column S)
  ├─ Checklist completed
  └─ Evidence IDs referenced in Column I

☐ Sheet 6: Backup & Recovery Configuration
  ├─ All services with data storage assessed
  ├─ Last recovery test date documented (Column V)
  ├─ Recovery test ≤90 days old (if older, flag as gap)
  ├─ RPO/RTO documented (Columns W-X)
  ├─ Checklist completed
  └─ Evidence IDs referenced in Column I

☐ Sheet 7: Jurisdictional Risk Assessment
  ├─ All services cross-referenced with IMP-5.23.2 Sheet 5/7
  ├─ Data residency alignment verified
  ├─ US-nexus vendors have mitigation documented
  └─ Evidence IDs referenced

☐ Sheet 8: Summary Dashboard
  ├─ All formulas working (no #REF! errors)
  ├─ Compliance percentages calculated
  ├─ Risk heatmap populated
  └─ Manually verified formula accuracy (spot-check 5 metrics)

☐ Sheet 9: Evidence Register
  ├─ Entry for EVERY piece of evidence collected
  ├─ Evidence IDs sequential (EV-SCD-001, 002, 003...)
  ├─ File paths correct and accessible
  ├─ Collection dates ≤90 days old
  └─ Status column shows ✅ Verified for all

☐ Sheet 10: Approval Sign-Off
  ├─ NOT completed yet (that's the next step)
  ├─ Next Review Date calculated (+90 days)
  └─ Review Responsible identified
```

---

### 7.3 Gate 2: Accuracy Verification

**Technical Accuracy Audit:**
```
CRITICAL ACCURACY CHECKS:

☐ Status-Evidence Alignment
  Test: For 10 random "✅ Compliant" rows, verify evidence supports claim
  Method:
    1. Select random row: Service X, Sheet 2, Status = ✅
    2. Check Column I: Evidence IDs listed
    3. Go to Sheet 9: Look up those Evidence IDs
    4. Access evidence files
    5. Verify: Does evidence actually prove compliance?
  Pass Criteria: 10/10 evidence matches claims
  Fail Action: If <9/10, review ALL Compliant rows (data integrity issue)

☐ Cross-Sheet Consistency
  Test: Same service should have consistent criticality across sheets
  Method:
    1. Pick Service X from Sheet 2
    2. Find Service X in Sheets 3, 4, 5, 6
    3. Verify: Criticality (Column E) is identical
    4. Verify: Data Classification (Column F) is identical
  Pass Criteria: 100% consistency
  Fail Action: Correct inconsistencies (indicates copy/paste errors)

☐ Environment Logic Check
  Test: Production should be MORE secure than Dev/Test
  Method:
    1. Filter rows: Environment = "Production"
    2. Count: Compliant + Partial + Non-Compliant
    3. Filter rows: Environment = "Development"
    4. Count: Compliant + Partial + Non-Compliant
    5. Compare: Prod compliance % should be ≥ Dev compliance %
  Pass Criteria: Prod ≥ Dev (or documented justification)
  Fail Action: If Dev > Prod, investigate (unusual pattern)

☐ Formula Validation (Sheet 8)
  Test: Dashboard formulas correctly reference source sheets
  Method:
    1. Go to Sheet 8, Table 1 (Compliance by Area)
    2. Click cell: "Identity & Access - Compliant" count
    3. Check formula: Should reference Sheet 2, Column H, count ✅
    4. Manually count ✅ in Sheet 2, Column H
    5. Compare: Formula result vs. manual count
  Pass Criteria: 100% match
  Fail Action: Fix formulas, re-verify entire dashboard

☐ Gap Remediation Logic Check
  Test: All Non-Compliant rows have remediation plans
  Method:
    1. Filter: Status (Column H) = ❌ Non-Compliant
    2. For each row, verify:
       - Gap Description (Column J) is filled
       - Remediation Needed (Column K) = Yes
       - Target Remediation Date (Column P) is future date
    3. Verify: Target date is realistic (not 10 years out)
  Pass Criteria: All Non-Compliant have complete remediation plans
  Fail Action: Complete missing remediation plans before approval

☐ Critical Service Validation
  Test: Critical services should have 100% compliance (or formal exceptions)
  Method:
    1. Filter: Service Criticality (Column E) = "Critical"
    2. For each critical service, check Status (Column H)
    3. Any ⚠️ Partial or ❌ Non-Compliant?
    4. If yes, verify: Exception ID (Column L) or Risk ID (Column M) documented
  Pass Criteria: Critical services compliant OR exception approved
  Fail Action: Escalate to CISO before submission (critical service gaps = high risk)
```

---

### 7.4 Gate 3: Evidence Validation

**Evidence Quality Audit:**
```
EVIDENCE QUALITY CHECKS:

☐ Evidence Existence Verification
  Test: All evidence files referenced in Sheet 9 actually exist
  Method:
    1. Export Sheet 9 (Evidence Register) to CSV
    2. Run script to check each Evidence Location path
    3. Attempt to open each file
    4. Flag any missing/inaccessible files
  Script:
    $evidenceRegister = Import-Csv "Sheet9_Evidence_Register.csv"
    $missing = @()
    
    foreach ($evidence in $evidenceRegister) {
        $path = $evidence.EvidenceLocation + $evidence.EvidenceFilename
        if (-not (Test-Path $path)) {
            $missing += $evidence.EvidenceID
        }
    }
    
    if ($missing.Count -gt 0) {
        Write-Host "❌ MISSING EVIDENCE: $($missing -join ', ')"
        # STOP - Do not proceed to approval until fixed
    } else {
        Write-Host "✅ All evidence files accessible"
    }
  Pass Criteria: 0 missing files
  Fail Action: Re-collect or locate missing evidence before approval

☐ Evidence Freshness Verification
  Test: Evidence is current (≤90 days old for most, ≤30 for critical)
  Method:
    1. Check evidence file timestamps (LastModified date)
    2. Calculate age: Today - LastModified
    3. Flag:
       - Critical configs (MFA, Encryption): Age >30 days
       - Important configs (RBAC, Logging): Age >90 days
       - Static configs (Contracts, Certs): Age >365 days
  Pass Criteria: <5% of evidence flagged as stale
  Fail Action: Re-collect stale evidence (prioritize critical configs)

☐ Evidence Quality Spot-Check
  Test: Evidence is high quality (readable, timestamped, complete)
  Method:
    1. Randomly select 10 evidence files
    2. For each file:
       - Screenshots: Timestamp visible? High resolution? Key setting highlighted?
       - Config exports: Valid JSON/CSV? Complete (not truncated)? No corruption?
       - Scan reports: Current date? Actionable findings? From reputable source?
    3. Rate each: ✅ High Quality / ⚠️ Acceptable / ❌ Poor Quality
  Pass Criteria: ≥8/10 high quality, 0 poor quality
  Fail Action: Re-collect poor quality evidence, improve acceptable ones

☐ Evidence-Claim Correlation Check
  Test: Evidence actually proves the claim (not tangentially related)
  Method:
    Example 1: Claim = "MFA enforced for all users"
      Evidence file: M365_MFA_Policy_20260120.png
      Check: Does screenshot show "Enforce MFA for All Users" = Enabled?
      ✅ If yes: Correlation confirmed
      ❌ If no (e.g., screenshot shows "MFA Available" not "Enforced"): Mismatch
    
    Example 2: Claim = "Encryption at rest enabled"
      Evidence file: Azure_Storage_Encryption_20260120.csv
      Check: Does CSV show column "EncryptionEnabled" = True for this storage account?
      ✅ If yes: Correlation confirmed
      ❌ If no: Mismatch
  Pass Criteria: 100% correlation (evidence proves claim)
  Fail Action: Update claim to match evidence OR collect better evidence

☐ Evidence Coverage Check
  Test: All "✅ Compliant" statuses have at least 1 piece of evidence
  Method:
    1. Filter Sheets 2-6: Status = ✅ Compliant
    2. For each row, check Column I (Evidence Location)
    3. Verify: At least one Evidence ID listed
  Pass Criteria: 100% of Compliant rows have evidence
  Fail Action: Collect missing evidence OR downgrade status to ⚠️ Partial
```

---

### 7.5 Self-Assessment Scoring

**Before submitting for approval, rate your assessment quality:**
```
ASSESSMENT QUALITY SCORECARD:

Category 1: COMPLETENESS (Max 25 points)
  ☐ All sheets 1-10 present and filled (5 points)
  ☐ All services from inventory assessed (5 points)
  ☐ All extended columns completed (5 points)
  ☐ All checklists completed (5 points)
  ☐ Evidence Register complete (5 points)
  Subtotal: ___/25

Category 2: ACCURACY (Max 25 points)
  ☐ Status matches evidence (10 points)
  ☐ No contradictions between sheets (5 points)
  ☐ Formula validation passed (5 points)
  ☐ Critical services 100% compliant (5 points)
  Subtotal: ___/25

Category 3: EVIDENCE (Max 25 points)
  ☐ All evidence files exist and accessible (10 points)
  ☐ Evidence is current (<90 days) (5 points)
  ☐ Evidence is high quality (5 points)
  ☐ Evidence proves claims (5 points)
  Subtotal: ___/25

Category 4: REMEDIATION (Max 15 points)
  ☐ All gaps documented (5 points)
  ☐ Remediation dates realistic (5 points)
  ☐ Compensating controls for critical gaps (5 points)
  Subtotal: ___/15

Category 5: PRESENTATION (Max 10 points)
  ☐ Consistent formatting (3 points)
  ☐ No typos or grammar errors (2 points)
  ☐ Professional appearance (3 points)
  ☐ README.md in evidence folder (2 points)
  Subtotal: ___/10

TOTAL SCORE: ___/100

INTERPRETATION:
  90-100: EXCELLENT - Ready for approval, high confidence
  80-89:  GOOD - Minor improvements recommended, proceed
  70-79:  ACCEPTABLE - Address noted gaps before submission
  60-69:  NEEDS WORK - Significant gaps, rework required
  <60:    FAIL - Do not submit, major quality issues
```

---

### 7.6 Peer Review Checklist

**Before final submission, have a colleague review using this checklist:**
```
PEER REVIEWER: _________________
REVIEW DATE: _________________

☐ Spot-Check Services (Select 3 random services)
  Service 1: _________________ 
    ☐ Sheet 2-6 data consistent (same service name, criticality)
    ☐ Status reasonable (matches extended columns)
    ☐ Evidence exists for Compliant claims
  
  Service 2: _________________
    ☐ Sheet 2-6 data consistent
    ☐ Status reasonable
    ☐ Evidence exists for Compliant claims
  
  Service 3: _________________
    ☐ Sheet 2-6 data consistent
    ☐ Status reasonable
    ☐ Evidence exists for Compliant claims

☐ Dashboard Validation (Sheet 8)
  ☐ Overall compliance % seems reasonable (not 100% or <50%)
  ☐ Compliance by environment makes sense (Prod ≥ Dev)
  ☐ Critical findings documented (if any)

☐ Gap Analysis Review
  ☐ Remediation plans are specific (not vague "improve security")
  ☐ Target dates are realistic (not all Q4 2030)
  ☐ High/Critical gaps have escalation documented

☐ Evidence Spot-Check (Select 5 random evidence files)
  Evidence 1: _________________ → ☐ Accessible ☐ Current ☐ Proves claim
  Evidence 2: _________________ → ☐ Accessible ☐ Current ☐ Proves claim
  Evidence 3: _________________ → ☐ Accessible ☐ Current ☐ Proves claim
  Evidence 4: _________________ → ☐ Accessible ☐ Current ☐ Proves claim
  Evidence 5: _________________ → ☐ Accessible ☐ Current ☐ Proves claim

☐ Overall Assessment
  ☐ Confidence level: ☐ High ☐ Medium ☐ Low
  ☐ Ready for approval: ☐ Yes ☐ No (explain: _________________)
  ☐ Recommended improvements: _________________________________

PEER REVIEWER SIGNATURE: _________________
```

---

### 7.7 Final Pre-Approval Checklist

**The last check before clicking "Submit for Approval":**
```
FINAL QUALITY GATE - DO NOT PROCEED WITHOUT 100% ✓

☐ COMPLETENESS VERIFIED
  ├─ All 10 sheets complete
  ├─ All services from inventory assessed
  ├─ All extended columns filled
  └─ All checklists completed

☐ ACCURACY VERIFIED
  ├─ Status-evidence alignment confirmed (spot-checked)
  ├─ Cross-sheet consistency validated
  ├─ Formulas working correctly
  └─ No contradictions found

☐ EVIDENCE VERIFIED
  ├─ All evidence files exist and accessible
  ├─ Evidence is current (<90 days)
  ├─ Evidence is high quality
  └─ Evidence proves claims

☐ REMEDIATION VERIFIED
  ├─ All gaps documented
  ├─ Remediation dates set
  ├─ Critical gaps escalated to CISO
  └─ Compensating controls documented

☐ PRESENTATION VERIFIED
  ├─ Formatting consistent
  ├─ No typos or errors
  ├─ Professional appearance
  └─ README.md created

☐ PEER REVIEW COMPLETED
  ├─ Colleague reviewed
  ├─ Feedback incorporated
  └─ Approval to proceed received

☐ STAKEHOLDER ALIGNMENT
  ├─ IT Ops aware of findings
  ├─ Security team briefed on gaps
  ├─ CISO pre-notified of critical findings
  └─ No surprises in approval workflow

☐ SELF-ASSESSMENT SCORE ≥80/100
  └─ If <80, address gaps before proceeding

☐ FINAL DECLARATION
  I certify that:
    - This assessment reflects actual configurations (not aspirational)
    - All evidence is genuine and current
    - All gaps are documented honestly
    - I am confident this assessment can withstand audit scrutiny
  
  Completed By: _________________
  Date: _________________
  Signature: _________________

PROCEED TO: Sheet 10 - Approval Sign-Off Workflow
```

---

**END OF SECTION 7: QUALITY CHECKLIST**

## Section 8: Review & Approval Process

### 8.1 Overview: Sequential Approval Workflow

**Purpose:** Ensure secure configuration assessments are technically accurate, security-compliant, and properly authorized before implementation or remediation.

**Approval Chain (Sequential):**
```
┌─────────────────────────────────────────────────────────────────────┐
│                    ASSESSMENT COMPLETION                             │
│                  (Coordinator/Assessor)                              │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │  1. IT OPERATIONS  │
                  │  Technical Review  │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │   2. SECURITY      │
                  │  Controls Review   │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │     3. DPO         │
                  │  Data Protection   │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │    4. CISO         │
                  │ Executive Approval │
                  └─────────┬──────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │  APPROVED & FINALIZED │
                └───────────────────────┘
```

**Timeline:** Target 2-3 weeks total (5 business days per review stage)

**Key Principle:** Each approver validates DIFFERENT aspects:
- **IT Operations**: Technical accuracy, feasibility, operational impact
- **Security**: Control effectiveness, risk coverage, security posture
- **DPO**: Data protection compliance, jurisdictional risk assessment
- **CISO**: Strategic alignment, risk acceptance, resource allocation

---

### 8.2 Assessment Completion Prerequisites

**Before Submitting for Approval:**

The assessment coordinator must verify:

| Checkpoint | Verification | Evidence Location |
|------------|--------------|-------------------|
| ✅ All services assessed | Cross-reference with ISMS-IMP-A.5.23.S1 inventory | Sheets 2-6 vs. Inventory |
| ✅ All yellow cells completed | No blank required fields | Visual scan of sheets 2-6 |
| ✅ Evidence documented | Every non-compliant item has evidence | Column I on all sheets |
| ✅ Remediation dates set | All gaps have target dates | Column P on all sheets |
| ✅ Dashboard calculated | All metrics show valid numbers | Sheet 8 |
| ✅ Evidence register populated | All evidence items listed | Sheet 9 |
| ✅ Jurisdictional risk assessed | Sheet 7 complete for US-nexus providers | Sheet 7 |
| ✅ Regulatory fields completed | DORA/NIS2/AI Act if applicable | Columns Y-AA (Sheet 2) |

**Implementer Perspective:**
*"Don't submit until the assessment is genuinely complete. Half-finished assessments waste everyone's time and damage your credibility."*

**Auditor Perspective:**
*"A complete assessment should tell the compliance story without needing extensive explanations. The evidence should speak for itself."*

---

### 8.3 Step 1: IT Operations Review

**Reviewer Role:** IT Operations Manager / DevOpsSec Lead  
**Focus:** Technical accuracy, operational feasibility, implementation correctness

**Review Timeline:** 3-5 business days

**Review Checklist:**
```
IT OPERATIONS REVIEW CHECKLIST

☐ 1. Configuration Accuracy
  ☐ Configuration items accurately described
  ☐ Environment classifications correct (Prod/Staging/Dev/Test)
  ☐ Service types properly categorized
  ☐ Technical details match actual deployed configurations

☐ 2. Evidence Quality (Technical)
  ☐ Screenshots show correct admin consoles
  ☐ Configuration exports are from current production
  ☐ API queries/scripts are reproducible
  ☐ Evidence timestamps are recent (< 30 days)

☐ 3. Gap Analysis Validation
  ☐ Identified gaps are genuine configuration issues
  ☐ "Non-Compliant" status is technically accurate
  ☐ No false positives (marked non-compliant but actually compliant)
  ☐ No false negatives (marked compliant but actually has gaps)

☐ 4. Remediation Feasibility
  ☐ Proposed remediation actions are technically possible
  ☐ Target dates are realistic given operational constraints
  ☐ Responsible teams correctly assigned
  ☐ Dependencies and prerequisites identified

☐ 5. Operational Impact Assessment
  ☐ Critical production systems flagged appropriately
  ☐ Change windows considered for remediation
  ☐ Potential service disruptions noted
  ☐ Rollback procedures available if needed

☐ 6. Baseline Accuracy (Sheet 2)
  ☐ Configuration baselines match documented standards
  ☐ CIS benchmark mappings correct
  ☐ Drift detection configured and working
  ☐ Version control references accurate

☐ 7. Integration Points
  ☐ SSO/SAML configurations accurately documented
  ☐ API integrations properly mapped
  ☐ Network connectivity paths correct
  ☐ Logging/SIEM integrations verified

☐ 8. Environment-Specific Configurations
  ☐ Production configs match security requirements
  ☐ Non-prod environments appropriately relaxed (if applicable)
  ☐ No production credentials in dev/test environments
  ☐ Environment isolation properly documented
```

**Review Outcomes:**

**A) Approved (No Conditions)**

*Example:*
```
IT OPERATIONS REVIEW - APPROVED

Reviewed By: [DevOpsSec Lead Name]
Review Date: 23.01.2026

Technical Accuracy: ✅ CONFIRMED
Operational Feasibility: ✅ CONFIRMED

Comments:
"Configuration assessment is technically accurate and comprehensive. 
All evidence validated against current production environments. 
Remediation plan is realistic and properly sequenced. Approved for 
Security review."

Next Step: Submit to Security Team (Target: 24.01.2026)
```

**B) Approved with Conditions**

*Example:*
```
IT OPERATIONS REVIEW - APPROVED WITH CONDITIONS

Reviewed By: [DevOpsSec Lead Name]
Review Date: 23.01.2026

Technical Accuracy: ⚠️ CONDITIONAL
Operational Feasibility: ✅ CONFIRMED

Conditions:
1. Update Network Security sheet (Sheet 4) - 3 services show VPN config 
   but actual deployment uses CloudFlare tunnel. Correct technical details.
   
2. Evidence for "MFA Enforced" (Sheet 2) - 5 services lack screenshots. 
   Provide admin console evidence showing MFA requirement.
   
3. Backup recovery testing (Sheet 6) - 2 critical services show "No" for 
   tested recovery. Complete test or document exception.

Deadline for Conditions: 30.01.2026

Comments:
"Assessment is 90% accurate but requires corrections in 3 areas. Once 
conditions are met, proceed to Security review without returning to me."

Next Step: Address conditions, then submit to Security (Target: 31.01.2026)
```

**C) Rejected (Requires Remediation)**

*Example:*
```
IT OPERATIONS REVIEW - REJECTED

Reviewed By: [DevOpsSec Lead Name]
Review Date: 23.01.2026

Technical Accuracy: ❌ INSUFFICIENT
Operational Feasibility: ⚠️ CONCERNS

Rejection Reasons:
1. CRITICAL: Sheet 2 (Configuration Baseline) shows 12 services as 
   "Compliant" but configuration exports show hardcoded credentials 
   in environment variables. This is a false positive - reassess.

2. Evidence quality insufficient - 15 out of 40 services have no 
   evidence or outdated evidence (> 90 days old). Refresh evidence.

3. Remediation targets unrealistic - Sheet 3 proposes migrating 8 
   services to SSO within 2 weeks. Actual implementation requires 
   vendor cooperation and takes 6-8 weeks per service.

4. Missing environment analysis - No assessment of staging/dev 
   environments. Policy requires all environments assessed.

Required Actions:
- Re-assess all "Compliant" services with hardcoded credential check
- Refresh all evidence older than 30 days
- Revise remediation timeline to realistic estimates
- Add staging and development environment rows

Resubmit After: All issues corrected (Estimate: 2 weeks)

Comments:
"Assessment needs significant rework before proceeding. Schedule review 
session with Security team to clarify requirements before resubmitting."
```

---

### 8.4 Step 2: Security Team Review

**Reviewer Role:** Information Security Manager / Security Architect  
**Focus:** Security control effectiveness, risk coverage, threat mitigation

**Review Timeline:** 3-5 business days

**Review Checklist:**
```
SECURITY TEAM REVIEW CHECKLIST

☐ 1. Security Control Effectiveness
  ☐ Identity & Access controls meet security baseline (Sheet 2)
  ☐ Encryption standards align with crypto policy (A.8.24)
  ☐ Network segmentation appropriate for data classification
  ☐ Logging captures security-relevant events
  ☐ Backup protections prevent ransomware data loss

☐ 2. Risk Coverage Analysis
  ☐ Critical services have comprehensive controls
  ☐ High-risk gaps prioritized for remediation
  ☐ Compensating controls documented where gaps exist
  ☐ Residual risks within acceptable tolerance

☐ 3. Access Control Validation (Sheet 2)
  ☐ MFA enforced for all administrative access
  ☐ RBAC implemented (not just username/password)
  ☐ Privileged access properly controlled
  ☐ Service accounts follow least privilege
  ☐ Access reviews conducted regularly

☐ 4. Data Protection Controls (Sheet 3)
  ☐ Encryption at rest for Restricted/Confidential data
  ☐ TLS 1.2+ enforced for data in transit
  ☐ Key management follows best practices
  ☐ DLP configured for sensitive data exfiltration prevention
  ☐ Data classification labels applied consistently

☐ 5. Network Security Posture (Sheet 4)
  ☐ Firewall rules follow least privilege
  ☐ Network segmentation isolates sensitive workloads
  ☐ VPN/secure connectivity for admin access
  ☐ Public internet exposure minimized
  ☐ API security properly configured

☐ 6. Monitoring & Detection (Sheet 5)
  ☐ Security logging enabled for all critical services
  ☐ SIEM integration configured
  ☐ Alerting rules cover security events
  ☐ Log retention meets compliance requirements
  ☐ Anomaly detection configured

☐ 7. Business Continuity (Sheet 6)
  ☐ Backups configured for all critical services
  ☐ Recovery procedures tested
  ☐ Backup encryption enabled
  ☐ Off-site/cloud backup for disaster recovery
  ☐ RTO/RPO meets business requirements

☐ 8. Regulatory Compliance (Sheets 2, 7)
  ☐ DORA config documentation complete (if applicable)
  ☐ NIS2 secure deployment validated (if applicable)
  ☐ AI Act controls for AI systems (if applicable)
  ☐ Jurisdictional risk assessed for US-nexus providers
  ☐ Risk acceptance documented for residual risks

☐ 9. Gap Remediation Priority
  ☐ Critical gaps have near-term target dates
  ☐ Production systems prioritized over non-prod
  ☐ Quick wins identified and fast-tracked
  ☐ Long-term remediation has phased approach

☐ 10. Exception Management
  ☐ All exceptions linked to exception register
  ☐ Exception approvals current (not expired)
  ☐ Compensating controls adequate
  ☐ Exception review dates set
```

**Review Outcomes:**

**A) Approved (No Conditions)**

*Example:*
```
SECURITY TEAM REVIEW - APPROVED

Reviewed By: [Security Manager Name]
Review Date: 27.01.2026

Security Control Effectiveness: ✅ CONFIRMED
Risk Coverage: ✅ ADEQUATE

Comments:
"Security controls are properly configured across all assessed services. 
Identity & access controls meet baseline requirements with MFA enforced. 
Encryption standards align with A.8.24 crypto policy. Network segmentation 
appropriate for data classifications. 

Gap remediation plan is well-prioritized with critical production gaps 
targeted first. Risk acceptance documentation complete for 3 services 
with compensating controls in place.

Approved for DPO review."

Next Step: Submit to DPO (Target: 28.01.2026)
```

**B) Approved with Conditions**

*Example:*
```
SECURITY TEAM REVIEW - APPROVED WITH CONDITIONS

Reviewed By: [Security Manager Name]
Review Date: 27.01.2026

Security Control Effectiveness: ⚠️ CONDITIONAL
Risk Coverage: ✅ ADEQUATE

Conditions:
1. Strengthen MFA for 4 services currently using SMS-based MFA (Sheet 2). 
   Upgrade to authenticator app or hardware token by 28.02.2026.
   Owner: IT Operations
   
2. Document compensating controls for 2 services with "No Encryption at Rest" 
   (Sheet 3). If vendor doesn't support encryption, implement network-level 
   encryption or migrate to alternative provider.
   Owner: DevOpsSec + Security
   
3. Complete penetration testing for 1 new service with public API exposure 
   (Sheet 4) before production deployment.
   Owner: Security + External Pentest Provider
   Deadline: 15.02.2026

Comments:
"Overall security posture is strong. Three conditions require attention 
before production deployment or to reduce residual risk. Once addressed, 
proceed to DPO without returning to Security."

Next Step: Document conditions, then submit to DPO (Target: 30.01.2026)
```

**C) Rejected (Requires Remediation)**

*Example:*
```
SECURITY TEAM REVIEW - REJECTED

Reviewed By: [Security Manager Name]
Review Date: 27.01.2026

Security Control Effectiveness: ❌ INSUFFICIENT
Risk Coverage: ❌ INADEQUATE

Rejection Reasons:
1. CRITICAL: 6 production services handling Restricted data do NOT have 
   encryption at rest enabled (Sheet 3). This violates data classification 
   policy and crypto policy (A.8.24). Cannot proceed.

2. MFA NOT enforced for administrative access on 8 services (Sheet 2). 
   This is a critical access control gap. Must remediate before approval.

3. Logging NOT enabled for 5 critical services (Sheet 5). Without audit 
   logs, we cannot detect security incidents. Must enable logging.

4. Backup recovery NEVER TESTED for 4 critical services (Sheet 6). 
   Business continuity requires tested recovery procedures.

5. Jurisdictional risk assessment incomplete (Sheet 7) - 9 US-nexus 
   providers have no CLOUD Act exposure assessment. DPO cannot review 
   without this.

Required Actions:
- IMMEDIATE: Enable encryption for all Restricted data services
- IMMEDIATE: Enforce MFA for all administrative access
- PRIORITY: Enable security logging and SIEM integration
- PRIORITY: Test backup recovery for critical services
- PRIORITY: Complete jurisdictional risk assessment

Resubmit After: Critical and Priority items completed (Estimate: 3-4 weeks)

Comments:
"Assessment reveals significant security gaps that create unacceptable 
risk. Do NOT proceed to production deployment for services with critical 
gaps. Schedule remediation workshop with Security team to develop action 
plan. Resubmit after key controls are in place."
```

---

### 8.5 Step 3: DPO Review (Data Protection Officer)

**Reviewer Role:** Data Protection Officer (DPO)  
**Focus:** Data protection compliance, jurisdictional risk, cross-border transfers

**Review Timeline:** 3-5 business days

**Review Checklist:**
```
DPO REVIEW CHECKLIST

☐ 1. Data Protection Compliance
  ☐ Data classification properly applied
  ☐ Personal data processing documented
  ☐ Special category data identified (if applicable)
  ☐ Data minimization principle followed
  ☐ Retention periods defined

☐ 2. Encryption & Data Security (Sheet 3)
  ☐ Encryption at rest for personal data
  ☐ Encryption in transit (TLS 1.2+)
  ☐ Key management appropriate for data sensitivity
  ☐ Data masking in non-production environments
  ☐ Secure deletion procedures documented

☐ 3. Jurisdictional Risk Assessment (Sheet 7)
  ☐ All US-nexus providers identified
  ☐ CLOUD Act exposure assessed
  ☐ Provider headquarters jurisdiction documented
  ☐ Data processing locations confirmed
  ☐ EU Data Boundary availability checked

☐ 4. Cross-Border Data Transfers
  ☐ Transfer mechanisms documented (SCCs, BCRs, etc.)
  ☐ DPAs reviewed for transfer clauses
  ☐ TIAs completed for US providers (if required)
  ☐ Adequacy decisions verified
  ☐ Risk assessments for non-adequate countries

☐ 5. CLOUD Act Mitigation (Sheet 7)
  ☐ Customer-managed encryption evaluated
  ☐ Legal challenge commitments verified
  ☐ EU data residency confirmed where possible
  ☐ Risk acceptance for residual exposure
  ☐ Compensating controls documented

☐ 6. Data Subject Rights
  ☐ Access procedures clear
  ☐ Deletion capabilities confirmed
  ☐ Data portability possible
  ☐ Rectification process defined
  ☐ Objection handling documented

☐ 7. Vendor Data Processing Agreements
  ☐ DPAs in place for all services processing personal data
  ☐ Sub-processor lists reviewed
  ☐ Security measures adequate per DPA
  ☐ Breach notification obligations clear
  ☐ Audit rights retained

☐ 8. Regulatory Compliance (GDPR/Swiss DPA)
  ☐ Legal basis for processing documented
  ☐ Legitimate interest assessments (if applicable)
  ☐ Privacy impact assessments for high-risk processing
  ☐ Data protection by design implemented
  ☐ Records of processing activities updated

☐ 9. AI Systems (if applicable)
  ☐ AI Act deployment controls complete (Sheet 2)
  ☐ High-risk AI systems assessed
  ☐ Human oversight documented
  ☐ Transparency requirements met
  ☐ Data governance for AI training data
```

**Review Outcomes:**

**A) Approved (No Conditions)**

*Example:*
```
DPO REVIEW - APPROVED

Reviewed By: [DPO Name]
Review Date: 30.01.2026

Data Protection Compliance: ✅ CONFIRMED
Jurisdictional Risk: ✅ ACCEPTABLE

Comments:
"Data protection controls are properly configured. Encryption at rest and 
in transit for all services processing personal data. Jurisdictional risk 
assessment complete for 9 US-nexus providers with appropriate transfer 
mechanisms (SCCs + CMK). 

TIAs completed for 3 high-risk providers. Risk acceptance documented for 
residual CLOUD Act exposure with compensating controls (CMK, data 
minimization, encryption). 

DPAs reviewed and adequate. Data subject rights procedures clear. 
Approved for CISO final authorization."

Next Step: Submit to CISO (Target: 31.01.2026)
```

**B) Approved with Conditions**

*Example:*
```
DPO REVIEW - APPROVED WITH CONDITIONS

Reviewed By: [DPO Name]
Review Date: 30.01.2026

Data Protection Compliance: ⚠️ CONDITIONAL
Jurisdictional Risk: ⚠️ CONDITIONAL

Conditions:
1. Complete TIAs for 2 US providers handling customer personal data 
   (Sheet 7, Rows 15, 22). Cannot rely solely on SCCs given Schrems II.
   Owner: Legal + DPO
   Deadline: 28.02.2026
   
2. Enable customer-managed encryption (CMK) for 1 US provider storing 
   Restricted data (Sheet 3, Row 8). Provider supports CMK but not yet 
   configured.
   Owner: IT Operations + Security
   Deadline: 15.02.2026
   
3. Update Records of Processing Activities (ROPA) to include 4 new 
   cloud services added this quarter.
   Owner: DPO (with IT input)
   Deadline: 15.02.2026

Comments:
"Data protection posture is generally strong but three items require 
completion. TIAs are critical for US providers post-Schrems II. CMK 
deployment reduces CLOUD Act exposure. Once conditions met, CISO may 
approve without returning to DPO."

Next Step: Document conditions, then submit to CISO (Target: 03.02.2026)
```

**C) Rejected (Requires Remediation)**

*Example:*
```
DPO REVIEW - REJECTED

Reviewed By: [DPO Name]
Review Date: 30.01.2026

Data Protection Compliance: ❌ NON-COMPLIANT
Jurisdictional Risk: ❌ UNACCEPTABLE

Rejection Reasons:
1. CRITICAL: 3 US providers processing customer personal data have NO 
   DPA in place (Sheet 7). This violates GDPR Art. 28. Cannot proceed 
   without DPAs.

2. CRITICAL: Jurisdictional risk assessment incomplete for 6 US-nexus 
   providers (Sheet 7). CLOUD Act exposure is "Under Assessment" but no 
   TIA initiated. Must complete before data processing begins.

3. HIGH: No encryption at rest for 2 services handling special category 
   data (Sheet 3). GDPR Art. 32 requires appropriate security measures. 
   Must enable encryption.

4. HIGH: Data retention periods not defined for 8 services (Sheet 3). 
   GDPR Art. 5(1)(e) requires storage limitation. Must document retention.

5. MEDIUM: Privacy impact assessment (PIA) missing for new CRM system 
   with extensive profiling. GDPR Art. 35 requires DPIA for high-risk 
   processing.

Required Actions:
- IMMEDIATE: Suspend processing on 3 services without DPAs until DPAs signed
- IMMEDIATE: Initiate TIAs for 6 US providers or implement compensating controls
- PRIORITY: Enable encryption for special category data
- PRIORITY: Define and document data retention periods
- PRIORITY: Complete PIA for CRM system

Resubmit After: All IMMEDIATE and PRIORITY items completed (Estimate: 4-6 weeks)

Comments:
"Assessment reveals serious data protection compliance gaps. Some services 
may need to be suspended until compliant. Schedule urgent meeting with 
Legal and Security to develop remediation roadmap. Do NOT proceed to CISO 
until compliance gaps resolved."
```

---

### 8.6 Step 4: CISO Approval (Final Authorization)

**Reviewer Role:** Chief Information Security Officer (CISO)  
**Focus:** Strategic alignment, risk acceptance, resource allocation, executive accountability

**Review Timeline:** 2-3 business days

**Review Checklist:**
```
CISO APPROVAL CHECKLIST

☐ 1. Risk Posture Review
  ☐ Overall compliance percentage acceptable
  ☐ Critical gaps identified and remediation planned
  ☐ Residual risks within risk appetite
  ☐ Risk acceptance documented for known gaps

☐ 2. Strategic Alignment
  ☐ Cloud security strategy implementation on track
  ☐ Configuration standards align with security baseline
  ☐ Technology choices support security roadmap
  ☐ Vendor selections align with approved provider list

☐ 3. Resource Allocation
  ☐ Remediation resources identified
  ☐ Budget requirements reasonable
  ☐ Timeline realistic for organization capacity
  ☐ External support (consultants, vendors) justified

☐ 4. Regulatory Compliance
  ☐ ISO 27001 Control A.5.23 requirements met
  ☐ DORA configuration documentation adequate (if applicable)
  ☐ NIS2 secure deployment validated (if applicable)
  ☐ GDPR/Swiss DPA compliance confirmed by DPO

☐ 5. Prior Approvals
  ☐ IT Operations approved (technical accuracy)
  ☐ Security approved (control effectiveness)
  ☐ DPO approved (data protection)
  ☐ All conditions documented and tracked

☐ 6. Business Enablement
  ☐ Security controls don't block business needs
  ☐ User experience acceptable
  ☐ Operational complexity manageable
  ☐ Balance between security and usability achieved

☐ 7. Continuous Improvement
  ☐ Lessons learned captured
  ☐ Process improvements identified
  ☐ Next review cycle scheduled
  ☐ KPIs defined for ongoing monitoring
```

**Review Outcomes:**

**A) Approved (Final Authorization)**

*Example:*
```
CISO APPROVAL - APPROVED

Approved By: [CISO Name]
Approval Date: 03.02.2026

Overall Assessment Status: ✅ APPROVED FOR IMPLEMENTATION
Risk Acceptance: ✅ WITHIN APPETITE

Executive Summary:
Secure configuration assessment demonstrates strong security posture 
across 42 cloud services. Overall compliance: 87% (37 fully compliant, 
5 partial gaps). 

Key Strengths:
- MFA enforced for all administrative access
- Encryption at rest/transit for all sensitive data
- Logging and monitoring properly configured
- Backup and recovery procedures tested

Accepted Risks:
- 3 services with US-nexus CLOUD Act exposure (mitigated with CMK + SCCs)
- 2 legacy services pending migration (compensating controls in place)

Remediation Plan:
- 5 partial gaps to be addressed within next quarter
- Resources allocated (2 FTE, €50K budget)
- Timeline: Complete by 30.04.2026

Authorization:
Approved for continued operation and remediation implementation. 
Next review: Q2 2026 (May 2026).

Signature: [CISO Signature]
Date: 03.02.2026
```

**B) Approved with Conditions (Conditional Authorization)**

*Example:*
```
CISO APPROVAL - APPROVED WITH CONDITIONS

Approved By: [CISO Name]
Approval Date: 03.02.2026

Overall Assessment Status: ⚠️ CONDITIONAL APPROVAL
Risk Acceptance: ⚠️ CONDITIONAL

Conditions for Final Authorization:

CONDITION 1: Complete MFA Upgrade
- 4 services using SMS-based MFA must upgrade to authenticator app
- Owner: IT Operations
- Deadline: 28.02.2026
- Budget: €5K for user training
- Status: In Progress (40% complete)

CONDITION 2: Penetration Testing
- New public-facing service (CRM) requires pentest before production
- Owner: Security + External Provider
- Deadline: 15.02.2026
- Budget: €15K (approved)
- Status: Scheduled for 08.02.2026

CONDITION 3: TIA Completion
- 2 US providers handling customer data require TIA
- Owner: Legal + DPO
- Deadline: 15.03.2026
- Budget: €10K legal fees
- Status: In Progress (1/2 complete)

Authorization Scope:
APPROVED for continued operation with conditions tracking. 
Services covered by Conditions 2-3 may operate under existing risk 
acceptance until conditions met. 

Next Milestone Review: 01.03.2026 (Condition status check)

Signature: [CISO Signature]
Date: 03.02.2026
```

**C) Rejected (Requires Remediation Before Authorization)**

*Example:*
```
CISO APPROVAL - REJECTED

Reviewed By: [CISO Name]
Review Date: 03.02.2026

Overall Assessment Status: ❌ NOT APPROVED
Risk Acceptance: ❌ EXCEEDS APPETITE

Rejection Reasons:

1. CRITICAL GAP: 6 production services handling Restricted data have 
   NO encryption at rest. This violates data classification policy and 
   creates unacceptable data breach risk.
   Impact: Potential €4M+ GDPR fine if breached
   
2. CRITICAL GAP: 8 services have NO MFA for administrative access. 
   Recent industry attacks (SolarWinds, Kaseya) exploited weak admin 
   auth. Cannot accept this risk.
   Impact: Organization-wide compromise possible

3. HIGH GAP: 5 critical services have NEVER TESTED backup recovery. 
   Without tested recovery, RTO/RPO are theoretical, not validated.
   Impact: Extended downtime in disaster scenario

4. COMPLIANCE RISK: DPO identified 3 services processing personal data 
   WITHOUT DPAs (GDPR violation). Legal exposure unacceptable.
   Impact: Regulatory enforcement action likely

Risk Assessment:
Current state: 65% compliant (below 85% threshold for approval)
Estimated risk exposure: HIGH
Financial impact potential: €5-10M (fines + breach costs)

Required Actions (Before Resubmission):
- IMMEDIATE: Enable encryption for all Restricted data services
- IMMEDIATE: Enforce MFA for all administrative access  
- IMMEDIATE: Sign DPAs or suspend processing
- PRIORITY: Complete backup recovery testing for critical services
- PRIORITY: Develop compensating controls for remaining gaps

Resource Allocation Approved:
- 3 FTE for 2 months (security team + DevOpsSec)
- €100K emergency budget for tools/licenses/consulting
- Executive sponsor: [CTO Name]

Resubmit Timeline:
Target: 02.03.2026 (4 weeks for critical remediation)
Interim Review: 15.02.2026 (progress checkpoint)

Comments:
"Current security posture creates unacceptable risk. Appreciate the 
thorough assessment which identified these gaps. Now we must act 
decisively to remediate. I'm authorizing emergency resources and 
executive sponsorship to accelerate fixes. Schedule weekly status 
meetings with me until we achieve approval-ready state."

Signature: [CISO Signature]
Date: 03.02.2026
```

---

### 8.7 Handling Rejections: Remediation Process

**When Assessment is Rejected at Any Stage:**
```
REJECTION RESPONSE PROCESS

Step 1: Acknowledge Receipt (Same Day)
  ☐ Email reviewer confirming receipt of rejection
  ☐ Request clarification meeting if needed
  ☐ Acknowledge timeline for resubmission

Step 2: Root Cause Analysis (Within 3 Days)
  ☐ Why was assessment rejected?
  ☐ What process failures led to rejection?
  ☐ Were requirements unclear?
  ☐ Was evidence insufficient?
  ☐ Were gaps underestimated?

Step 3: Remediation Planning (Within 5 Days)
  ☐ Break down rejection reasons into action items
  ☐ Assign owners for each action item
  ☐ Set realistic deadlines per item
  ☐ Identify dependencies and blockers
  ☐ Allocate resources (people, budget, tools)

Step 4: Execute Remediation (Timeline Varies)
  ☐ Implement fixes for identified issues
  ☐ Collect new/updated evidence
  ☐ Document all changes made
  ☐ Internal quality check before resubmission

Step 5: Internal Pre-Review (Before Resubmission)
  ☐ Review with trusted peer/senior
  ☐ Verify all rejection reasons addressed
  ☐ Ensure no new issues introduced
  ☐ Confirm evidence quality improved

Step 6: Formal Resubmission
  ☐ Submit with cover memo listing changes made
  ☐ Reference original rejection reasons
  ☐ Highlight new evidence provided
  ☐ Request expedited review if urgent

Step 7: Learn from Rejection
  ☐ What process failures led to rejection?
  ☐ How to prevent in future assessments?
  ☐ Update assessment process based on lessons learned
```

**Example: Remediation Action Plan (IT Operations Rejection)**
```
REMEDIATION ACTION PLAN
Original Rejection Date: 23.01.2026
Target Resubmission: 10.02.2026

Rejection Reason 1: Configuration exports show hardcoded credentials (12 services)
  Action: Re-audit all services, migrate to secrets manager
  Owner: DevOpsSec Lead
  Deadline: 05.02.2026
  Status: In Progress (8/12 migrated)
  
Rejection Reason 2: Evidence older than 30 days (15 services)
  Action: Refresh all screenshots and config exports
  Owner: Assessment Coordinator
  Deadline: 02.02.2026
  Status: Complete ✅

Rejection Reason 3: Unrealistic remediation timelines
  Action: Revise timelines with vendor input, add buffer
  Owner: Project Manager
  Deadline: 04.02.2026
  Status: Complete ✅

Rejection Reason 4: Missing staging/dev environment assessment
  Action: Add staging and dev rows for all services
  Owner: Assessment Coordinator
  Deadline: 08.02.2026
  Status: In Progress (60% complete)

Resubmission Checklist:
  ☐ All 4 rejection reasons fully addressed
  ☐ New evidence collected and documented
  ☐ Peer review complete (internal QA)
  ☐ Cover memo drafted explaining changes
  ☐ Resubmission scheduled with IT Operations

Lessons Learned:
  - Schedule pre-submission review with technical lead before formal submission
  - Implement evidence freshness check (automated reminder)
  - Coordinate with vendors earlier for realistic timelines
  - Include all environments in initial assessment scope
```

---

### 8.8 Tracking Approvals to Completion

**Approval Tracking Dashboard:**
```
APPROVAL WORKFLOW TRACKER

Assessment: ISMS-IMP-A.5.23.S3 - Secure Configuration & Deployment
Start Date: 20.01.2026
Target Completion: 10.02.2026

┌──────────────┬─────────────┬──────────┬──────────────┬─────────────┐
│ Approver     │ Submit Date │ Status   │ Decision     │ Complete    │
├──────────────┼─────────────┼──────────┼──────────────┼─────────────┤
│ IT Ops       │ 22.01.2026  │ Complete │ Approved     │ 24.01.2026  │
│ Security     │ 25.01.2026  │ Complete │ Approved (C) │ 27.01.2026  │
│ DPO          │ 28.01.2026  │ Complete │ Approved (C) │ 30.01.2026  │
│ CISO         │ 31.01.2026  │ In Review│ -            │ -           │
└──────────────┴─────────────┴──────────┴──────────────┴─────────────┘

Legend:
  Approved = No conditions
  Approved (C) = Approved with Conditions
  Rejected = Remediation required

CONDITIONS TRACKER (from Security & DPO):

Security Condition 1: MFA upgrade (4 services)
  Owner: IT Operations
  Deadline: 28.02.2026
  Status: In Progress (1/4 complete)
  Next Milestone: 2nd service by 10.02.2026

Security Condition 2: Compensating controls documentation
  Owner: DevOpsSec + Security
  Deadline: 15.02.2026
  Status: In Progress (draft documentation)
  Next Milestone: Security review of draft by 08.02.2026

Security Condition 3: Penetration testing for new service
  Owner: Security + External Provider
  Deadline: 15.02.2026
  Status: Scheduled (08.02.2026)
  Next Milestone: Complete pentest report by 12.02.2026

DPO Condition 1: Complete TIAs (2 US providers)
  Owner: Legal + DPO
  Deadline: 28.02.2026
  Status: In Progress (1/2 complete)
  Next Milestone: 2nd TIA by 20.02.2026

DPO Condition 2: Enable CMK (1 US provider)
  Owner: IT Operations + Security
  Deadline: 15.02.2026
  Status: In Progress (vendor config underway)
  Next Milestone: CMK deployment by 12.02.2026

DPO Condition 3: Update ROPA (4 new services)
  Owner: DPO
  Deadline: 15.02.2026
  Status: Complete ✅

TIMELINE:
  20.01.2026: Assessment completed
  22.01.2026: Submitted to IT Operations
  24.01.2026: IT Ops approved, submitted to Security
  27.01.2026: Security approved with conditions, submitted to DPO
  30.01.2026: DPO approved with conditions, submitted to CISO
  03.02.2026: CISO approval expected
  04.02.2026: Assessment status: APPROVED WITH CONDITIONS

OVERALL STATUS: ON TRACK
```

---

**END OF SECTION 8: REVIEW & APPROVAL PROCESS**

## Section 9: Integration & Maintenance

### 9.1 Integration with Other ISMS Assessments

**Critical Context:** This assessment (ISMS-IMP-A.5.23.S3) is ONE component of the comprehensive A.5.19-23 supplier/cloud security framework. It does not operate in isolation.

**The Five-Workbook Ecosystem:**
```
┌────────────────────────────────────────────────────────────────────┐
│  ISMS Control A.5.19-23: Information Security for Cloud Services  │
└────────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
         ┌────▼────┐     ┌────▼────┐    ┌────▼────┐
         │ 5.23.1  │────▶│ 5.23.2  │───▶│ 5.23.3  │◀── YOU ARE HERE
         │Inventory│     │Vendor DD│    │ Config  │
         └────┬────┘     └────┬────┘    └────┬────┘
              │               │               │
              └───────────────┼───────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
         ┌────▼────┐     ┌────▼────┐
         │ 5.23.4  │     │ 5.23.5  │
         │Governanc│     │Complianc│
         │   e     │     │   e     │
         └─────────┘     └─────────┘
```

**Integration Requirements:**

| Workbook | Relationship to 5.23.3 | Integration Point |
|----------|------------------------|-------------------|
| **5.23.1 (Inventory)** | AUTHORITATIVE SOURCE | Cloud service list; any service in 5.23.3 MUST exist in 5.23.1 |
| **5.23.2 (Vendor DD)** | PREREQUISITE | Vendor security certifications inform config requirements |
| **5.23.4 (Governance)** | DOWNSTREAM CONSUMER | Ongoing access reviews use 5.23.3 identity/access baseline |
| **5.23.5 (Compliance)** | DOWNSTREAM CONSUMER | Compliance monitoring uses 5.23.3 config state as evidence |

**Implementer Perspective:**
*"When you configure a new cloud service, update 5.23.1 first (inventory), then complete 5.23.3 (config), then 5.23.2 (vendor), then enable monitoring in 5.23.4. Don't do them out of order."*

**Auditor Perspective:**
*"I'll check that every service in 5.23.3 exists in 5.23.1, and that config requirements align with vendor capabilities documented in 5.23.2. Missing linkages indicate incomplete assessment."*

---

### 9.2 Integration with Organizational Systems

**Cloud configuration assessment should NOT be a standalone spreadsheet.** Integrate with your existing systems:

#### 9.2.1 Configuration Management Database (CMDB)

**Integration Pattern:**
```
CMDB (Source of Truth)          ISMS-IMP-5.23.3 (Assessment)
├─ Service: O365                ├─ Service: O365
│  ├─ Environment: Production   │  ├─ Environment: Production
│  ├─ Owner: IT Operations      │  ├─ Responsible: IT Operations
│  ├─ Criticality: High         │  ├─ Criticality: High
│  └─ Config Items: [List]      │  └─ Config Items: [Assessed]
│                                │
└─ SYNC WEEKLY ◀────────────────┘
```

**Synchronization Points:**
- Service names and IDs (avoid duplicate entries)
- Environment classifications (Production, Staging, etc.)
- Ownership and responsibility
- Criticality ratings
- Configuration item tracking

**Automation Opportunity:**
```python
# Weekly sync: CMDB → ISMS-IMP-5.23.3
# Identify services in CMDB but not in security assessment

cmdb_services = get_cmdb_cloud_services()
assessment_services = get_excel_services("5.23.3", sheet="2. Configuration Baseline")

missing_from_assessment = cmdb_services - assessment_services

if missing_from_assessment:
    alert_security_team(f"{len(missing_from_assessment)} cloud services in CMDB 
                         but not in security config assessment")
```

---

#### 9.2.2 IT Service Management (ITSM) / Ticketing System

**Integration Pattern:**
- **Configuration Changes:** Link to change tickets
- **Gap Remediation:** Create remediation tickets automatically
- **Evidence Collection:** Attach screenshots/exports to tickets

**Example Workflow:**
```
5.23.3 Gap Identified               ITSM Ticket Created
┌─────────────────────┐            ┌──────────────────────┐
│ Service: Salesforce │   ────▶    │ TICKET: SEC-2045     │
│ Gap: MFA Not Enforcd│            │ Priority: High       │
│ Status: Non-Complian│            │ Assignee: DevOpsSec  │
│ Target: 28.02.2026  │            │ Due: 28.02.2026      │
└─────────────────────┘            │ Link: 5.23.3 Row 15  │
                                   └──────────────────────┘
```

**Ticket Template for Config Gaps:**
```
Title: [ISMS-5.23.3] Security Configuration Gap - [Service Name]

Description:
Security configuration assessment identified a gap requiring remediation.

Service: [Service Name]
Environment: [Production/Staging/etc.]
Configuration Item: [Specific setting]
Current State: [What's wrong]
Required State: [What's needed]
Gap Type: [Identity/Data/Network/Logging/Backup]
Risk Level: [Critical/High/Medium/Low]

Remediation Steps:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Evidence Required:
- Screenshot of updated configuration
- Config export showing change
- Validation test results

Assessment Reference: ISMS-IMP-5.23.3, Sheet [X], Row [Y]
Target Date: [DD.MM.YYYY]
Responsible Team: [Team Name]
```

---

#### 9.2.3 Security Information and Event Management (SIEM)

**Integration Pattern:**
```
5.23.3 Assessment (Config State)  ◀──▶  SIEM (Runtime Monitoring)
├─ MFA Enforced: Yes              ←───  Alert: Non-MFA login detected
├─ Logging Enabled: Yes           ───▶  Verify: Logs flowing to SIEM
├─ Encryption: AES-256            ←───  Alert: Unencrypted data detected
└─ Firewall Rules: Restricted     ───▶  Verify: No violations logged
```

**Continuous Validation:**
- 5.23.3 says "MFA enforced" → SIEM should NEVER see non-MFA admin login
- 5.23.3 says "Logging enabled" → SIEM should receive logs continuously
- 5.23.3 says "Firewall rules restricted" → SIEM should detect violations

**Alert Correlation Example:**
```
SIEM Alert: "Admin login without MFA detected on Salesforce"
  ↓
Auto-check 5.23.3 Assessment:
  - Sheet 2, Row 12: Salesforce MFA status = "✅ Compliant"
  ↓
Possible Scenarios:
  1. Assessment is WRONG (MFA not actually enforced) → Update 5.23.3
  2. Bypass/exception occurred → Document in 5.23.3 exception register
  3. New admin account created → Trigger config review
```

---

#### 9.2.4 Configuration Drift Detection Tools

**Integration Pattern:**
```
Baseline (5.23.3)    ◀──Compare──▶    Current State (Drift Tool)
├─ MFA: Required     │                ├─ MFA: Required ✅
├─ TLS: 1.3          │                ├─ TLS: 1.2 ⚠️ DRIFT
├─ Logging: Enabled  │                ├─ Logging: Disabled ❌ DRIFT
└─ [Update needed]   ◀────────────────┘
```

**Recommended Tools:**
- **Cloud-native:** AWS Config, Azure Policy, GCP Config Connector
- **Multi-cloud:** CloudHealth, Prisma Cloud, Orca Security
- **Open-source:** Cloud Custodian, ScoutSuite, Prowler

**Drift Response Workflow:**
```
1. Drift Detected by Tool
   ↓
2. Compare Against 5.23.3 Baseline
   ↓
3. Determine if Drift is:
   a) AUTHORIZED (document change in 5.23.3) → Update assessment
   b) UNAUTHORIZED (security violation) → Remediate immediately
   c) IMPROVEMENT (better than baseline) → Update baseline
   ↓
4. Update Evidence in 5.23.3 (Column I)
   ↓
5. Update Last Verified Date (Column Q)
```

---

### 9.3 Quarterly Maintenance Procedures

**Cloud security configuration is NOT "set and forget."** Quarterly reviews catch drift, new services, and evolving threats.

**Quarterly Maintenance Checklist (Every 3 Months):**
```
QUARTERLY MAINTENANCE - ISMS-IMP-5.23.3
Review Quarter: Q[X] [YYYY]
Review Date: [DD.MM.YYYY]
Coordinator: [Name]

☐ STEP 1: Reconcile with Inventory (5.23.1)
  ☐ Compare 5.23.3 service list against current 5.23.1
  ☐ Add rows for NEW services deployed this quarter
  ☐ Mark DECOMMISSIONED services (archive, don't delete)
  ☐ Update service criticality if changed
  ☐ Verify environment classifications still accurate

☐ STEP 2: Refresh Evidence
  ☐ Review "Last Verified Date" (Column Q) on all sheets
  ☐ Re-capture screenshots for configs older than 90 days
  ☐ Update config exports (JSON/YAML/XML)
  ☐ Re-run security posture reports (Azure Secure Score, etc.)
  ☐ Document any config changes since last review

☐ STEP 3: Validate Current State
  ☐ Spot-check 20% of "Compliant" items (avoid false positives)
  ☐ Re-assess any "Partial" items (have they been remediated?)
  ☐ Check remediation progress on "Non-Compliant" items
  ☐ Verify compensating controls still in place

☐ STEP 4: Check for Drift
  ☐ Review drift detection tool reports
  ☐ Correlate SIEM alerts with configuration state
  ☐ Identify unauthorized configuration changes
  ☐ Update baseline if authorized changes occurred

☐ STEP 5: Update Regulatory Compliance
  ☐ Review DORA config documentation (if applicable)
  ☐ Validate NIS2 secure deployment (if applicable)
  ☐ Check AI Act deployment controls (if new AI services)
  ☐ Re-assess jurisdictional risk (Sheet 7) if vendor changed

☐ STEP 6: Review Exceptions and Risk Acceptance
  ☐ Check exception expiration dates (Column L)
  ☐ Verify risk acceptance still valid (residual risk acceptable?)
  ☐ Renew exceptions if needed (CISO approval)
  ☐ Close expired exceptions or remediate gaps

☐ STEP 7: Update Dashboard (Sheet 8)
  ☐ Verify all formulas calculating correctly
  ☐ Review compliance percentage trends (improving or degrading?)
  ☐ Identify new critical gaps requiring escalation
  ☐ Update executive summary with key findings

☐ STEP 8: Update Evidence Register (Sheet 9)
  ☐ Add evidence for newly assessed services
  ☐ Mark outdated evidence as "Outdated" (Column I)
  ☐ Capture new evidence for refreshed configs
  ☐ Update file locations if evidence moved

☐ STEP 9: Approval Sign-Off Update (Sheet 10)
  ☐ Document quarterly review completion
  ☐ Obtain IT Operations sign-off (if significant changes)
  ☐ Obtain Security sign-off (if new gaps identified)
  ☐ Set next quarterly review date

☐ STEP 10: Lessons Learned
  ☐ What config drifts occurred most frequently?
  ☐ Which services have recurring gaps?
  ☐ What automation could prevent drift?
  ☐ Update assessment process based on findings
```

**Time Estimate:** 2-3 days for ~40-50 services (full-time effort)

---

### 9.4 Annual Comprehensive Review

**Once per year, perform a DEEP review beyond routine quarterly maintenance.**

**Annual Review Scope (Beyond Quarterly):**

| Review Area | Quarterly | Annual |
|-------------|-----------|--------|
| Service list reconciliation | ✅ | ✅ |
| Evidence refresh | ✅ | ✅ |
| Spot-check validation | 20% sample | **100% validation** |
| Config baseline update | As needed | **Full baseline review** |
| Security standard alignment | No | **Align with latest CIS/NIST** |
| Tool evaluation | No | **Evaluate new tools** |
| Process improvement | Minor tweaks | **Major process overhaul** |
| Stakeholder interviews | No | **Interview IT/Security/DPO** |
| Regulatory landscape check | No | **Review new regulations** |

**Annual Review Deliverables:**

1. **Updated Configuration Baselines**
   - Align with latest CIS Benchmarks (v9.0 → v10.0)
   - Incorporate vendor best practices updates
   - Adjust for new threat landscape (e.g., post-incident changes)

2. **Security Standard Gap Analysis**
```
   Current State (5.23.3)    vs.    Updated Standard (CIS v10.0)
   ├─ MFA: Required          │      ├─ MFA: Required + Phishing-Resistant ⚠️
   ├─ TLS: 1.2+              │      ├─ TLS: 1.3 Required (1.2 deprecated) ⚠️
   ├─ Logging: 90 days       │      ├─ Logging: 365 days (compliance req) ⚠️
   └─ [Gaps identified]      ◀─────┘
```

3. **Process Maturity Assessment**
   - Configuration management maturity: Ad-hoc → Managed → Optimized
   - Automation level: Manual → Semi-automated → Fully automated
   - Integration completeness: Isolated → Integrated → Orchestrated

4. **Tool Stack Evaluation**
   - Are current tools still fit-for-purpose?
   - New tools available (better drift detection, automation)?
   - ROI analysis: Cost vs. value vs. manual effort

5. **Regulatory Landscape Update**
   - New regulations affecting cloud security (DORA, NIS2, AI Act, etc.)
   - Updated guidance from regulators (EDPB, FINMA, etc.)
   - Industry-specific standards (PCI-DSS v4.0, HIPAA updates, etc.)

6. **Annual Report to CISO**
```
   ANNUAL CLOUD SECURITY CONFIGURATION REPORT
   Review Period: 01.01.2026 - 31.12.2026
   
   Executive Summary:
   - 45 cloud services assessed (up from 38 last year)
   - Overall compliance: 89% (up from 85% last year)
   - 12 critical gaps remediated this year
   - 3 new high-risk services onboarded with secure config
   
   Key Achievements:
   - MFA enforcement: 100% (up from 92%)
   - Encryption at rest: 100% for Restricted data (up from 95%)
   - Logging enabled: 98% (up from 90%)
   
   Remaining Gaps:
   - 2 legacy services pending migration (TLS 1.2 → 1.3)
   - 1 vendor does not support customer-managed encryption
   
   Recommendations for Next Year:
   - Implement automated drift detection for all critical services
   - Migrate 2 legacy services to TLS 1.3-capable alternatives
   - Enhance backup testing frequency (quarterly → monthly for critical)
```

**Time Estimate:** 1-2 weeks for comprehensive annual review

---

### 9.5 Continuous Improvement Cycle

**Security configuration assessment should IMPROVE over time, not just maintain status quo.**

**Continuous Improvement Framework:**
```
┌──────────────────────────────────────────────────────────────┐
│                    CONTINUOUS IMPROVEMENT                     │
└──────────────────────────────────────────────────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐         ┌────▼────┐        ┌────▼────┐
    │ MEASURE │         │ ANALYZE │        │  ACT    │
    │         │────────▶│         │───────▶│         │
    │ Config  │         │  Gaps   │        │ Improve │
    │  State  │         │ Trends  │        │ Process │
    └────┬────┘         └─────────┘        └────┬────┘
         │                                       │
         └───────────────────◀───────────────────┘
                        LEARN
```

**Metrics to Track (Quarter-over-Quarter):**

| Metric | Trend Direction | Target |
|--------|-----------------|--------|
| Overall compliance % | ↗️ Increasing | 95%+ |
| Critical gaps count | ↘️ Decreasing | Zero |
| Time to remediate (avg) | ↘️ Decreasing | < 30 days |
| Evidence freshness (avg days) | ↘️ Decreasing | < 45 days |
| Config drift incidents | ↘️ Decreasing | < 5 per quarter |
| New services assessed (time) | ↘️ Decreasing | < 5 days |
| Automation % | ↗️ Increasing | 80%+ |

**Improvement Opportunities to Identify:**

1. **Automation Candidates**
   - Which config checks are manual but could be automated?
   - Which evidence collection is repetitive? (automate with scripts)
   - Which drift detection is manual? (implement tools)

2. **Process Bottlenecks**
   - Where do assessments get stuck? (approval delays? evidence collection?)
   - Which steps take longest? (can they be parallelized?)
   - Which stakeholders are slow to respond? (need better engagement?)

3. **Recurring Gaps**
   - Same service failing quarterly? → Root cause analysis needed
   - Same config item across multiple services? → Systemic issue, not isolated
   - Same vendor repeatedly non-compliant? → Vendor selection issue

4. **Tool Gaps**
   - Are we missing critical config items because tools don't check them?
   - Are we duplicating effort across multiple tools?
   - Could we consolidate tools for efficiency?

**Example Improvement Initiative:**
```
IMPROVEMENT INITIATIVE: Automate MFA Enforcement Validation

Current State (Manual):
- Every quarter, coordinator logs into each service admin console
- Takes screenshot of MFA settings
- Pastes into Excel evidence column
- Time: 30 minutes per service × 45 services = 22.5 hours per quarter

Proposed State (Automated):
- Python script queries each service API for MFA status
- Script generates evidence report with screenshots
- Script updates Excel automatically
- Time: 2 hours to develop + 10 minutes per quarter to run

ROI Analysis:
- Development time: 2 hours (one-time)
- Time saved: 22.5 - 0.17 = 22.33 hours per quarter
- Annual time saved: 22.33 × 4 = 89.32 hours ≈ 2.2 weeks FTE
- Payback period: < 1 quarter

Approval Status: ✅ APPROVED (CISO 15.03.2026)
Implementation: Q2 2026
```

---

### 9.6 Change Management: When Configurations Evolve

**Cloud configurations change frequently. The assessment must keep pace.**

**Common Configuration Change Scenarios:**

#### Scenario 1: Vendor Introduces New Security Feature

*Example: Provider adds customer-managed encryption (CMK) support*

**Change Management Process:**
```
1. Vendor Announcement (Email, Release Notes)
   ↓
2. Security Team Evaluation
   - Is this feature relevant to our data classification?
   - Does it improve our security posture?
   - What's the implementation effort?
   ↓
3. Decision: Adopt or Defer
   - Adopt: Add to config baseline (5.23.3 Sheet 2, new requirement)
   - Defer: Document in risk register (not needed for our use case)
   ↓
4. Update Assessment
   - Add new column or config item if adopting
   - Assess all services using this provider
   - Update remediation plan for non-compliant services
   ↓
5. Update Approval (Sheet 10)
   - Document baseline change
   - Obtain CISO approval for new requirement
```

---

#### Scenario 2: Regulatory Requirement Changes

*Example: NIS2 adds new secure deployment requirements*

**Change Management Process:**
```
1. Regulatory Change Notification (Official gazette, legal alert)
   ↓
2. Legal + Compliance Review
   - Does this apply to our organization?
   - What are the new requirements?
   - What's the compliance deadline?
   ↓
3. Impact Assessment
   - Which services affected?
   - Which configs need updating?
   - Gap analysis: current state vs. new requirement
   ↓
4. Update Assessment Framework (5.23.3)
   - Add new column for regulatory requirement (e.g., Column AA)
   - Update Instructions sheet with new guidance
   - Add to dashboard metrics (Sheet 8)
   - Update approval checklist (Sheet 10 - DPO section)
   ↓
5. Remediation Plan
   - Assess all in-scope services
   - Prioritize by compliance deadline
   - Allocate resources (budget, people, tools)
   ↓
6. Executive Approval
   - Present gap analysis to CISO
   - Obtain budget approval for remediation
   - Document risk acceptance for any interim gaps
```

---

#### Scenario 3: Service Decommissioning

*Example: Migrating from Slack to Microsoft Teams*

**Change Management Process:**
```
1. Service Decommissioning Decision
   ↓
2. Update Inventory (5.23.1)
   - Mark Slack as "Decommissioned"
   - Add Teams as "New Service"
   ↓
3. Update Config Assessment (5.23.3)
   - Archive Slack rows (move to bottom, gray out)
   - Add Teams rows for configuration assessment
   - Assess Teams configurations BEFORE full deployment
   ↓
4. Migration Security Checklist
   ☐ Data export from Slack (encrypted)
   ☐ Teams configured with security baseline
   ☐ MFA enforced on Teams
   ☐ Data classification applied
   ☐ Logging and SIEM integration
   ☐ User training on secure usage
   ↓
5. Post-Migration Validation
   - Verify all security configs in place on Teams
   - Confirm Slack data securely deleted
   - Update evidence register (Sheet 9)
   - Update approval sign-off (Sheet 10)
```

---

#### Scenario 4: Configuration Drift Detected

*Example: SIEM alerts that TLS 1.3 is no longer enforced on critical service*

**Change Management Process:**
```
1. Drift Alert from SIEM or Tool
   ↓
2. Investigate Drift Cause
   - Was this an authorized change? (check change tickets)
   - Was this unauthorized? (security incident)
   - Was this vendor-side change? (check vendor announcements)
   ↓
3. Immediate Response
   - AUTHORIZED: Update 5.23.3 baseline, document change
   - UNAUTHORIZED: Revert config, investigate incident
   - VENDOR: Engage vendor, request explanation
   ↓
4. Update Assessment (5.23.3)
   - Refresh evidence (Column I)
   - Update Last Verified Date (Column Q)
   - Update Status if gap introduced (Column H)
   - Document in Gap Description (Column J)
   ↓
5. Remediation (if gap introduced)
   - Create remediation ticket (ITSM)
   - Assign owner (Column O)
   - Set target date (Column P)
   - Track to closure
   ↓
6. Root Cause Analysis
   - Why did drift occur?
   - How to prevent recurrence?
   - Do we need better monitoring?
   - Update process to prevent future drift
```

---

### 9.7 Integration with Incident Response

**When security incidents occur, configuration assessment provides critical context.**

**Incident Response Integration:**
```
INCIDENT DETECTED
  ↓
  ├─────────────────────────────────────┐
  │  CONSULT 5.23.3 FOR CONTEXT         │
  ├─────────────────────────────────────┘
  │
  ├─▶ Sheet 2 (Identity & Access): Was MFA enforced? (incident used compromised creds)
  ├─▶ Sheet 3 (Data Protection): Was data encrypted? (incident involved data exfiltration)
  ├─▶ Sheet 4 (Network Security): Were firewall rules correct? (incident used unauthorized access)
  ├─▶ Sheet 5 (Logging & Monitoring): Were logs enabled? (incident detection delayed due to no logs)
  └─▶ Sheet 6 (Backup & Recovery): Are backups available? (incident was ransomware)
```

**Post-Incident Configuration Review:**

After ANY security incident involving cloud services:
```
☐ Step 1: Review Relevant Config (5.23.3)
  - Which config items were involved in incident?
  - Were they marked "Compliant" but actually vulnerable?
  - Was assessment evidence outdated?

☐ Step 2: Update Assessment Based on Findings
  - Correct any false positives (marked compliant but not)
  - Add new config items if gaps revealed
  - Refresh evidence for affected services

☐ Step 3: Enhance Baselines
  - Did incident reveal new threat vector?
  - Should baseline be strengthened?
  - Update config requirements to prevent recurrence

☐ Step 4: Update Lessons Learned
  - What config gap contributed to incident?
  - How can assessment process catch this earlier?
  - What automation could have prevented this?

☐ Step 5: Share Findings with Stakeholders
  - Update IT Operations on config changes needed
  - Update Security on new baseline requirements
  - Update CISO on risk posture changes
```

---

### 9.8 Maintenance Roles & Responsibilities

**Don't let configuration assessment become one person's burden. Distribute responsibility.**

| Role | Responsibility | Frequency |
|------|----------------|-----------|
| **Assessment Coordinator** | Overall assessment maintenance, evidence collection, stakeholder coordination | Continuous |
| **IT Operations** | Provide config evidence, validate technical accuracy, remediate gaps | Quarterly |
| **DevOpsSec** | Configuration drift monitoring, baseline maintenance, automation | Continuous |
| **Security Team** | Baseline updates, threat landscape monitoring, exception review | Quarterly |
| **DPO** | Jurisdictional risk updates, data protection compliance, regulatory changes | Quarterly |
| **CISO** | Executive oversight, risk acceptance, resource allocation, annual strategic review | Annual |

---

### 9.9 Maintenance Budget & Resources

**Configuration assessment is not free. Budget for it.**

**Typical Quarterly Maintenance Effort (40-50 services):**

| Activity | Time Estimate | Role |
|----------|---------------|------|
| Service reconciliation | 4 hours | Coordinator |
| Evidence refresh | 16 hours | Coordinator + IT Ops |
| Validation spot-checks | 8 hours | Security Team |
| Dashboard updates | 2 hours | Coordinator |
| Stakeholder reviews | 4 hours | All |
| **TOTAL** | **34 hours** | ~1 week FTE |

**Annual Budget Considerations:**

- **Personnel:** 1-2 weeks per quarter + 2 weeks annual = 6-10 weeks FTE per year
- **Tools:** Drift detection, SIEM, config scanning tools (€20-50K per year)
- **Training:** Config security best practices, vendor-specific training (€5-10K per year)
- **External Support:** Pentesting, audits, consulting (€10-30K per year)
- **TOTAL:** €35-90K per year (depending on org size and maturity)

---

**END OF SECTION 9: INTEGRATION & MAINTENANCE**

### Appendix I: Frequently Asked Questions (FAQ)

**Q1: How often should we refresh evidence in the assessment?**

**A:** Minimum quarterly for all services. For critical production services handling Restricted data, refresh monthly. Evidence older than 90 days should be considered outdated and trigger re-assessment.

---

**Q2: What if a vendor doesn't support our required security configuration?**

**A:** Three options:
1. **Compensating Controls:** Implement alternative controls (e.g., if vendor doesn't support encryption, use network-level encryption)
2. **Risk Acceptance:** Document residual risk and obtain CISO approval (use Exception ID column)
3. **Vendor Change:** Migrate to alternative provider that meets requirements

---

**Q3: Do we need to assess non-production environments?**

**A:** Yes, but with risk-based scope:
- **Production:** Full assessment, all sheets
- **Staging:** Assess if processing real data (even anonymized)
- **Development/Test:** Assess identity/access and data handling; may relax other controls

Never skip environments that process customer data, even in staging.

---

**Q4: How do we handle services used by only one department?**

**A:** Assess ALL services in organizational scope, regardless of usage scale. A single-department service can still create organization-wide risk if compromised. Use "Service Criticality" column to prioritize, but don't exclude from assessment.

---

**Q5: Can we mark a service "Compliant" if it has 1-2 minor gaps?**

**A:** No. "Compliant" means ALL configuration items meet baseline. Use "⚠️ Partial" for services with minor gaps. This prevents false sense of security and ensures gaps are tracked for remediation.

---

**Q6: What if IT Operations and Security disagree on configuration requirements?**

**A:** Escalate to CISO for decision. Document the disagreement, technical rationale from both sides, and final decision. Security requirements should generally take precedence unless business impact is severe (then use risk acceptance process).

---

**Q7: How do we assess SaaS services where we have limited configuration control?**

**A:** Focus on what you CAN control:
- Identity & access (SSO, MFA, RBAC)
- Data classification and DLP
- Logging and monitoring (API access to logs)
- Integration security (APIs, connectors)

Document vendor-controlled items in "Gap Description" with note: "Vendor-controlled, verified in 5.23.2 due diligence."

---

**Q8: Do we need separate rows for same service in different regions?**

**A:** Depends on config differences:
- **Same config globally:** Single row, Environment = "All"
- **Different configs per region:** Separate rows (e.g., US region vs. EU region)

Use judgment: if regional configs differ significantly, separate rows improve clarity.

---

**Q9: What's the difference between Exception ID and Risk ID?**

**A:** 
- **Exception ID:** Approved deviation from policy (time-limited, must be renewed)
- **Risk ID:** Identified risk in risk register (may or may not be accepted)

Both link to separate registers outside this assessment. Use Exception ID for policy violations that are accepted; use Risk ID for broader risk documentation.

---

**Q10: Can we automate evidence collection?**

**A:** Yes, and you should! Use:
- API queries to provider (e.g., AWS CLI, Azure PowerShell, GCP gcloud)
- Config scanning tools (AWS Config, ScoutSuite, Prowler)
- Python scripts to query and generate evidence reports

Manual screenshots should be last resort, not first choice. Automation improves consistency and reduces assessment time by 60-80%.

---

### Appendix J: Quick Reference - Sheet Column Summary

**For quick lookup during assessment:**

#### All Assessment Sheets (Columns A-Q - Standard)

| Column | Header | Type | Width |
|--------|--------|------|-------|
| A | Cloud Service Name | Text | 28 |
| B | Vendor Name | Text | 22 |
| C | Service Type | Dropdown | 20 |
| D | Environment | Dropdown | 18 |
| E | Service Criticality | Dropdown | 18 |
| F | Data Classification | Dropdown | 20 |
| G | Configuration Item | Text | 30 |
| H | Status | Dropdown | 15 |
| I | Evidence Location | Text | 30 |
| J | Gap Description | Text | 35 |
| K | Remediation Needed | Dropdown | 16 |
| L | Exception ID | Text | 14 |
| M | Risk ID | Text | 14 |
| N | Compensating Controls | Text | 30 |
| O | Responsible Team | Dropdown | 20 |
| P | Target Remediation Date | Date | 18 |
| Q | Last Verified Date | Date | 18 |

#### Sheet 2: Configuration Baseline (Columns R-AA)

| Column | Header | Type |
|--------|--------|------|
| R | Config Management Tool | Dropdown |
| S | IaC Managed | Dropdown |
| T | CIS Benchmark Ref | Text |
| U | Drift Detection Enabled | Dropdown |
| V | Baseline Documentation | Text |
| W | Last Baseline Update | Date |
| X | Config Review Frequency | Dropdown |
| Y | DORA Config Compliance | Dropdown |
| Z | NIS2 Deployment Status | Dropdown |
| AA | AI Act Deployment | Dropdown |

---

**END OF SECTION 10: APPENDICES & REFERENCES**

**END OF PART I: USER COMPLETION GUIDE**

## PART II: TECHNICAL SPECIFICATION - Section 1 of 4

---

## Table of Contents - Section 1

1. **Workbook Structure Overview**
2. **Cell Styling Reference**
3. **Base Column Definitions (A-Q)**
4. **Sheet 1: Instructions & Legend**
5. **Sheet 2: Configuration Baseline**

---

## 1. Workbook Structure Overview

### 1.1 Sheet Architecture - 10 Sheets

```
┌─────────────────────────────────────────────────────────────────────┐
│              ISMS-IMP-A.5.23.S3 WORKBOOK STRUCTURE              │
│                  (Secure Configuration & Deployment)                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LAYER 1: ORIENTATION                                              │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ Sheet 1: Instructions & Legend                                │ │
│  │          Assessment purpose, status legend, evidence guide    │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  LAYER 2: CONFIGURATION ASSESSMENT (Core)                          │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ Sheet 2: Configuration Baseline                               │ │
│  │          27 columns (A-AA): Base + DORA/NIS2/AI Act           │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │ Sheet 3: Access Control Setup                                 │ │
│  │          24 columns (A-X): SSO, MFA, RBAC, PAM, JIT           │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │ Sheet 4: Network Security                                     │ │
│  │          24 columns (A-X): IP restrictions, segmentation      │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │ Sheet 5: Encryption Configuration                             │ │
│  │          24 columns (A-X): Encryption, key management, HSM    │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │ Sheet 6: Deployment Checklist                                 │ │
│  │          24 columns (A-X): Pre-deploy, monitoring, rollback   │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  LAYER 3: REGULATORY COMPLIANCE                         │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ Sheet 7: Jurisdictional Risk                                  │ │
│  │          20 columns (A-T): CLOUD Act, data sovereignty        │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  LAYER 4: CONSOLIDATION & APPROVAL                                 │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ Sheet 8: Summary Dashboard                                    │ │
│  │          4 tables: Compliance + Jurisdictional + Regulatory   │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │ Sheet 9: Evidence Register                                    │ │
│  │          Centralized evidence tracking (all sheets)           │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │ Sheet 10: Approval Sign-Off                                   │ │
│  │          4-stage approval: IT Ops → Security → DPO → CISO     │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Version Control

| Version | Date | Changes | Sheets Affected |
|---------|------|---------|-----------------|
| **1.0** | [Date] | Initial release (9 sheets) | All (original) |

**Key Enhancements:**
- **NEW Sheet 7:** Jurisdictional Risk Assessment (CLOUD Act exposure)
- **Sheet 2:** +3 regulatory columns (Y-AA): DORA config docs, NIS2 secure deployment, AI deployment controls
- **Sheet 8:** +2 dashboard tables: Jurisdictional Risk Summary, Regulatory Compliance Summary
- **Sheet 10:** +DPO Review section (between Security and CISO approval stages)
- **All Sheets:** Enhanced checklists with +15 regulatory compliance items

### 1.3 Regulatory Compliance Coverage

| Regulation | Affected Sheets | Key Requirements |
|------------|----------------|------------------|
| **DORA (Digital Operational Resilience Act)** | Sheets 2, 8, 10 | Configuration documentation, operational resilience evidence |
| **NIS2 (Network & Information Security Directive 2)** | Sheets 2, 8, 10 | Secure deployment procedures, security-by-default validation |
| **EU AI Act** | Sheets 2, 6, 8 | High-risk AI system deployment controls, conformity assessment |
| **US CLOUD Act** | Sheet 7 | Jurisdictional risk assessment, cross-border data access exposure |

---

## 2. Cell Styling Reference

### 2.1 Style Definitions

All styles use **NEW object creation per cell** to avoid Excel "shared object" repair warnings.

| Style Name | Font | Fill Color | Alignment | Usage |
|------------|------|------------|-----------|-------|
| **header** | Calibri 14, Bold, White | Dark Blue (003366) | Center, Wrap | Section headers (Row 1) |
| **subheader** | Calibri 11, Bold, White | Medium Blue (4472C4) | Center, Wrap | Assessment questions (Row 2) |
| **column_header** | Calibri 10, Bold, Black | Light Gray (D9D9D9) | Center, Wrap | Column headers (Row 4) |
| **input_cell** | Calibri 10, Black | Light Yellow (FFFFCC) | Left, Wrap | Editable data cells (Rows 5-30) |
| **warning** | Calibri 10, Bold, Red | Light Orange (FFEB9C) | Left, Wrap | Warning messages |

### 2.2 Border Standards

- **All cells:** Thin borders (1px solid) on all sides
- **Merged cells:** Apply border to entire merged range
- **Data rows:** Consistent thin borders for professional appearance

### 2.3 Row Heights

| Row Type | Height (points) | Rationale |
|----------|-----------------|-----------|
| Section Header (Row 1) | 50 | Accommodate 2-line title + policy reference |
| Assessment Question (Row 2) | 30 | Clear question visibility |
| Spacer (Row 3) | 15 (default) | Visual separation |
| Column Headers (Row 4) | 15 (default) | Standard header height |
| Data Rows (5-30) | 15 (default) | Auto-adjust based on content |

### 2.4 Column Widths

**Base columns (A-Q)** - Standard across all assessment sheets:
- Column A (Assessment_ID): 14
- Column B (Cloud_Service_Name): 28
- Column C (Vendor_Name): 22
- Column D (Service_Type): 20
- Column E (Environment): 18
- Column F (Service_Criticality): 18
- Column G (Data_Classification): 20
- Column H (Configuration_Item): 30
- Column I (Status): 15
- Column J (Evidence_Location): 30
- Column K (Gap_Description): 35
- Column L (Remediation_Needed): 16
- Column M (Exception_ID): 14
- Column N (Risk_ID): 14
- Column O (Compensating_Controls): 30
- Column P (Responsible_Team): 20
- Column Q (Target_Remediation_Date): 18

**Extended columns (R-AA)** - Vary by sheet (see individual sheet specs)

---

## 3. Base Column Definitions (A-Q)

### 3.1 Standard Columns for ALL Configuration Assessment Sheets

These 17 columns (A-Q) are **identical** across Sheets 2-6 to enable dashboard consolidation.

| Column | Field Name | Width | Data Type | Validation | Formula | Description |
|--------|-----------|-------|-----------|------------|---------|-------------|
| **A** | Assessment_ID | 14 | Formula | - | `=CONCATENATE("CFG-",TEXT(ROW()-4,"000"))` | Auto-generated unique ID (CFG-001, CFG-002, etc.) |
| **B** | Cloud_Service_Name | 28 | Text | - | - | Service name (import from IMP-5.23.1 Sheet 2 Column B) |
| **C** | Vendor_Name | 22 | Text | - | - | Vendor/provider name (import from IMP-5.23.1 Sheet 2 Column C) |
| **D** | Service_Type | 20 | Dropdown | SaaS, IaaS, PaaS, Security Service, Storage Service | - | Cloud service category |
| **E** | Environment | 18 | Dropdown | Production, Staging, Development, Test, All Environments | - | Where this service is deployed |
| **F** | Service_Criticality | 18 | Dropdown | Critical, High, Medium, Low | - | Business impact if unavailable (from IMP-5.23.1) |
| **G** | Data_Classification | 20 | Dropdown | Confidential, Internal, Public | - | Highest data classification processed (from IMP-5.23.1) |
| **H** | Configuration_Item | 30 | Text | - | - | Specific config setting being assessed (e.g., "SSO Enabled", "TLS 1.3 Enforced") |
| **I** | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | - | Compliance status for this config item |
| **J** | Evidence_Location | 30 | Text | - | - | Path/URL to evidence file (screenshot, config export, scan report) |
| **K** | Gap_Description | 35 | Text | - | - | If not Compliant: describe the gap (what's missing/wrong) |
| **L** | Remediation_Needed | 16 | Dropdown | Yes, No, N/A | - | Does this gap require remediation? |
| **M** | Exception_ID | 14 | Text | - | - | If exception approved: reference exception document ID |
| **N** | Risk_ID | 14 | Text | - | - | If risk accepted: reference risk register entry |
| **O** | Compensating_Controls | 30 | Text | - | - | Alternative controls if config item not fully compliant |
| **P** | Responsible_Team | 20 | Dropdown | IT Operations, Cloud Ops, DevOps, Security, Platform Engineering, DevSecOps | - | Team responsible for remediation |
| **Q** | Target_Remediation_Date | 18 | Date | - | - | Target date to close gap (if remediation needed) |

### 3.2 Data Validation Rules (Base Columns)

**Dropdowns implemented via `openpyxl.worksheet.datavalidation.DataValidation`:**

```python
# Service Type (Column D)
service_type_dv = DataValidation(
    type="list",
    formula1='"SaaS,IaaS,PaaS,Security Service,Storage Service"',
    allow_blank=False
)
ws.add_data_validation(service_type_dv)
service_type_dv.add("D5:D30")  # Apply to data rows

# Environment (Column E)
environment_dv = DataValidation(
    type="list",
    formula1='"Production,Staging,Development,Test,All Environments"',
    allow_blank=False
)
ws.add_data_validation(environment_dv)
environment_dv.add("E5:E30")

# Service Criticality (Column F)
criticality_dv = DataValidation(
    type="list",
    formula1='"Critical,High,Medium,Low"',
    allow_blank=False
)
ws.add_data_validation(criticality_dv)
criticality_dv.add("F5:F30")

# Data Classification (Column G)
data_class_dv = DataValidation(
    type="list",
    formula1='"Confidential,Internal,Public"',
    allow_blank=False
)
ws.add_data_validation(data_class_dv)
data_class_dv.add("G5:G30")

# Status (Column I) - with UTF-8 symbols
status_dv = DataValidation(
    type="list",
    formula1=f'"{CHECK} Compliant,{WARNING} Partial,{XMARK} Non-Compliant,N/A"',
    allow_blank=False
)
ws.add_data_validation(status_dv)
status_dv.add("I5:I30")

# Remediation Needed (Column L)
yes_no_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(yes_no_dv)
yes_no_dv.add("L5:L30")

# Responsible Team (Column P)
responsible_team_dv = DataValidation(
    type="list",
    formula1='"IT Operations,Cloud Ops,DevOps,Security,Platform Engineering,DevSecOps"',
    allow_blank=False
)
ws.add_data_validation(responsible_team_dv)
responsible_team_dv.add("P5:P30")
```

### 3.3 UTF-8 Symbol Encoding

**Status symbols used in dropdowns:**

```python
CHECK = '\u2705'      # ✅ Green checkmark (Compliant)
WARNING = '\u26A0'    # ⚠️ Warning sign (Partial)
XMARK = '\u274C'      # ❌ Red X (Non-Compliant)
```

**Usage:** These symbols provide visual clarity in dropdown menus and dashboard tables. Excel natively supports UTF-8 when workbook is saved with proper encoding.

---

## 4. Sheet 1: Instructions & Legend

### 4.1 Purpose & Layout

**Sheet Name:** `Instructions & Legend`

**Purpose:** Provide user orientation, assessment context, status legend, evidence requirements, and regulatory applicability guidance.

**Layout:** Free-form text layout with merged cells, no data validation (read-only reference).

### 4.2 Sheet Structure

```
┌───────────────────────────────────────────────────────────────┐
│ Row 1:  ISMS-IMP-A.5.23.S3 – Secure Configuration         │
│         (Header, merged A1:C1)                                │
├───────────────────────────────────────────────────────────────┤
│ Row 2:  ISO/IEC 27001:2022 - Control A.5.23                   │
│         (Subheader, merged A2:C2)                             │
├───────────────────────────────────────────────────────────────┤
│ Row 4+: DOCUMENT INFORMATION                                  │
│         - Document ID: ISMS-IMP-A.5.23.S3                      │
│         - Assessment Area: Secure Configuration & Deployment  │
│         - Related Policy: ISMS-POL-A.5.19-23-S5               │
│         - Version: 1.0 (Regulatory Update)                    │
│         - Assessment Date: [Input field]                      │
│         - Completed By: [Input field]                         │
│         - Organization: [Input field]                         │
│         - Review Cycle: Quarterly                             │
├───────────────────────────────────────────────────────────────┤
│ HOW TO USE THIS WORKBOOK (Step-by-step instructions)         │
├───────────────────────────────────────────────────────────────┤
│ SHEET NAVIGATION GUIDE (10 sheets explained)                 │
├───────────────────────────────────────────────────────────────┤
│ STATUS LEGEND (✅ ⚠️ ❌ N/A definitions)                      │
├───────────────────────────────────────────────────────────────┤
│ EVIDENCE REQUIREMENTS (screenshot/config export/scan)         │
├───────────────────────────────────────────────────────────────┤
│ REGULATORY APPLICABILITY GUIDE (DORA/NIS2/AI Act/CLOUD Act)  │
├───────────────────────────────────────────────────────────────┤
│ VERSION HISTORY (1.0 → 2.0 regulatory update)                │
├───────────────────────────────────────────────────────────────┤
│ CONTACT INFORMATION (coordinator, IT ops, security, CISO)    │
└───────────────────────────────────────────────────────────────┘
```

### 4.3 Key Content Sections

#### 4.3.1 Document Information

| Field | Value | Notes |
|-------|-------|-------|
| Document ID | ISMS-IMP-A.5.23.S3 | Fixed |
| Assessment Area | Secure Configuration & Deployment | Fixed |
| Related Policy | ISMS-POL-A.5.19-23-S5 | Fixed |
| Version | 2.0 (Regulatory Update) | Fixed |
| Assessment Date | [Input field] | Yellow fill, user-editable |
| Completed By | [Input field] | Yellow fill, user-editable |
| Organization | [Input field] | Yellow fill, user-editable |
| Review Cycle | Quarterly | Fixed |

#### 4.3.2 How to Use This Workbook

**Instructions (summary):**
1. Reference ISMS-IMP-A.5.23.S1 (Inventory) for service list
2. Complete Sheets 2-7 for all cloud services
3. Use dropdown menus for standardized entries
4. Provide evidence links for all compliance claims
5. Complete dashboard formulas automatically
6. Review evidence register for completeness
7. Obtain sequential approvals (IT Ops → Security → DPO → CISO)

#### 4.3.3 Sheet Navigation Guide

**10-Sheet Overview:**

| Sheet # | Sheet Name | Purpose | When to Complete |
|---------|------------|---------|------------------|
| 1 | Instructions & Legend | Orientation | Read first |
| 2 | Configuration Baseline | CIS benchmarks, config mgmt | All services |
| 3 | Access Control Setup | SSO, MFA, RBAC, PAM | All services |
| 4 | Network Security | IP restrictions, segmentation, WAF | All services |
| 5 | Encryption Configuration | Encryption at rest/transit, key mgmt | All services processing confidential data |
| 6 | Deployment Checklist | Pre-deploy validation, rollback | New deployments + quarterly review |
| 7 | Jurisdictional Risk | CLOUD Act exposure, data sovereignty | US-nexus providers (Microsoft, AWS, Google, etc.) |
| 8 | Summary Dashboard | Compliance metrics, gaps | Auto-calculated after Sheets 2-7 complete |
| 9 | Evidence Register | Evidence tracking | As evidence collected |
| 10 | Approval Sign-Off | 4-stage approval workflow | After assessment complete |

#### 4.3.4 Status Legend

| Symbol | Status | Definition | Usage |
|--------|--------|------------|-------|
| ✅ | Compliant | Configuration item meets security requirements, evidence provided | Use when config verified compliant |
| ⚠️ | Partial | Configuration item partially compliant, minor gaps exist | Use when mostly compliant but improvements needed |
| ❌ | Non-Compliant | Configuration item fails to meet requirements, remediation required | Use when config is insecure or missing |
| N/A | Not Applicable | Configuration item not relevant to this service/environment | Use when config item doesn't apply |

#### 4.3.5 Evidence Requirements

**Acceptable Evidence Types:**

| Configuration Area | Evidence Type | Example |
|--------------------|---------------|---------|
| Identity & Access | Screenshot of admin console settings | Azure AD Conditional Access policy screenshot |
| Data Protection | Config export (JSON/YAML) | AWS S3 bucket encryption config (JSON) |
| Network Security | Firewall rule export | Azure NSG rule export (CSV) |
| Encryption | Certificate/key metadata | TLS certificate details, key rotation policy |
| Deployment | Pre-deployment checklist | Signed deployment approval form |
| Logging | SIEM integration config | Splunk forwarder config file |
| Backup | Backup job logs | Veeam backup job success screenshot |

**Evidence Location Format:**
- **File share:** `\\fileserver\ISMS\Evidence\A.5.23.3\[Service_Name]\[Config_Item]\[Filename]`
- **SharePoint:** `https://[org].sharepoint.com/sites/ISMS/Evidence/A.5.23.3/[Service]/[File]`
- **Cloud storage:** `s3://isms-evidence/A.5.23.3/[Service]/[Config_Item]/[File]`

#### 4.3.6 Regulatory Applicability Guide

**When to Complete Regulatory Columns/Sheets:**

| Regulation | Applies If... | Required Sheets | Required Columns |
|------------|---------------|-----------------|------------------|
| **DORA** | [Organization] is EU financial institution or critical ICT service provider | All assessment sheets | Sheet 2: Column Y (DORA Config Documentation) |
| **NIS2** | [Organization] is Essential/Important Entity under NIS2 (energy, transport, health, digital infrastructure) | All assessment sheets | Sheet 2: Column Z (NIS2 Secure Deployment) |
| **EU AI Act** | Cloud service processes high-risk AI system (biometrics, critical infrastructure, law enforcement, employment) | Sheets 2, 6 | Sheet 2: Column AA (AI Deployment Controls) |
| **US CLOUD Act** | Cloud provider has US nexus (HQ, subsidiary, or operations in US) | Sheet 7 | ALL columns (A-T) |

**Quick Decision Matrix:**

```
Does [Organization] fall under DORA? (EU financial institution)
  ├─ YES → Complete columns Y (all sheets) + standard assessment
  └─ NO  → Skip column Y, complete standard assessment only

Does [Organization] fall under NIS2? (Essential/Important Entity)
  ├─ YES → Complete columns Z (all sheets) + standard assessment
  └─ NO  → Skip column Z, complete standard assessment only

Does cloud service process high-risk AI?
  ├─ YES → Complete columns AA (Sheet 2, 6) + Sheet 7 if US provider
  └─ NO  → Skip column AA

Is cloud provider US-based or US-subsidiary? (Microsoft, AWS, Google, Oracle, Salesforce, etc.)
  ├─ YES → Complete Sheet 7 (Jurisdictional Risk Assessment)
  └─ NO  → Skip Sheet 7 (EU/Swiss providers exempt)
```

#### 4.3.7 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial release (9 sheets, no regulatory columns) |

### 4.4 Cell Styling (Instructions Sheet)

**No data validation needed** (read-only reference sheet).

**Styling:**
- Row 1: Header style (Dark blue, white text, merged A1:C1)
- Row 2: Subheader style (Medium blue, white text, merged A2:C2)
- Section headers: Bold, size 11
- Input fields (Assessment Date, Completed By, Organization): Yellow fill (FFFFCC)
- Body text: Normal, size 10, wrapped

**Column Widths:**
- Column A: 35
- Column B: 25
- Column C: 20

**Freeze Panes:** Row 3 frozen (headers visible when scrolling)

---

## 5. Sheet 2: Configuration Baseline

### 5.1 Purpose & Layout

**Sheet Name:** `2. Configuration Baseline`

**Purpose:** Assess whether cloud services are configured according to security baselines (CIS Benchmarks, vendor hardening guides, organization-specific standards).

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 5.2 (Configuration Management)

**Assessment Question:** "Are cloud services configured according to documented security baselines with change management controls and drift monitoring?"

### 5.2 Column Structure (A-AA, 27 columns)

**Base Columns (A-Q):** Standard 17 columns (see Section 3)

**Extended Columns (R-AA):** Configuration baseline-specific + regulatory

| Column | Field Name | Width | Data Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **R** | Baseline_Version | 16 | Text | - | Version of baseline applied (e.g., "CIS AWS 1.5.0", "Azure CIS 2.0.0") |
| **S** | Change_Mgmt_ID | 16 | Text | - | Change ticket ID if config was changed via change management |
| **T** | Drift_Monitoring | 16 | Dropdown | Enabled, Disabled, N/A | Is automated drift detection configured? |
| **U** | CIS_Benchmark | 16 | Dropdown | Level 1, Level 2, Not Applied, N/A | CIS Benchmark level applied (Level 1=foundational, Level 2=high security) |
| **V** | Last_Validated | 16 | Date | - | Date when config baseline was last validated |
| **W** | Config_Backup | 16 | Dropdown | Yes, No, N/A | Is configuration backed up for recovery? |
| **X** | Privileged_Access_Log | 18 | Dropdown | Yes, No, N/A | Are privileged access actions logged? |
| **Y** | Security_By_Default | 16 | Dropdown | Yes, Partial, No, N/A | Is service deployed with secure defaults? |
| **Y** | DORA_Config_Documentation | 22 | Dropdown | Documented, Partially Documented, Not Documented, N/A | DORA requirement: Is configuration documented for operational resilience? |
| **Z** | NIS2_Secure_Deployment | 20 | Dropdown | Compliant, Partially Compliant, Non-Compliant, N/A | NIS2 requirement: Does deployment meet secure-by-default requirements? |
| **AA** | AI_System_Deployment_Controls | 24 | Dropdown | Full Controls, Partial Controls, No Controls, N/A | EU AI Act: Are deployment controls for high-risk AI systems in place? |

**Note:** Columns Y-AA are **conditional** - only complete if regulatory framework applies (see Instructions Sheet).

### 5.3 Data Validation Rules (Extended Columns)

```python
# Drift Monitoring (Column T)
drift_monitoring_dv = DataValidation(
    type="list",
    formula1='"Enabled,Disabled,N/A"',
    allow_blank=False
)
ws.add_data_validation(drift_monitoring_dv)
drift_monitoring_dv.add("T5:T30")

# CIS Benchmark (Column U)
cis_benchmark_dv = DataValidation(
    type="list",
    formula1='"Level 1,Level 2,Not Applied,N/A"',
    allow_blank=False
)
ws.add_data_validation(cis_benchmark_dv)
cis_benchmark_dv.add("U5:U30")

# Config Backup (Column W)
yes_no_na_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(yes_no_na_dv)
yes_no_na_dv.add("W5:W30")  # Also applied to columns X, Y

# Privileged Access Log (Column X)
yes_no_na_dv.add("X5:X30")

# Security By Default (Column Y)
security_by_default_dv = DataValidation(
    type="list",
    formula1='"Yes,Partial,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(security_by_default_dv)
security_by_default_dv.add("Y5:Y30")

# --- REGULATORY COLUMNS---

# DORA Config Documentation (Column Y)
dora_config_dv = DataValidation(
    type="list",
    formula1='"Documented,Partially Documented,Not Documented,N/A"',
    allow_blank=False
)
ws.add_data_validation(dora_config_dv)
dora_config_dv.add("Y5:Y30")

# NIS2 Secure Deployment (Column Z)
nis2_deployment_dv = DataValidation(
    type="list",
    formula1='"Compliant,Partially Compliant,Non-Compliant,N/A"',
    allow_blank=False
)
ws.add_data_validation(nis2_deployment_dv)
nis2_deployment_dv.add("Z5:Z30")

# AI System Deployment Controls (Column AA)
ai_deployment_dv = DataValidation(
    type="list",
    formula1='"Full Controls,Partial Controls,No Controls,N/A"',
    allow_blank=False
)
ws.add_data_validation(ai_deployment_dv)
ai_deployment_dv.add("AA5:AA30")
```

### 5.4 Section Headers

```
Row 1 (merged A1:AA1):
  "CONFIGURATION BASELINE ASSESSMENT
   ISMS-POL-A.5.19-23-S5, Section 5.2: Configuration Management"

Row 2 (merged A2:AA2):
  "Assessment Question: Are cloud services configured according to documented 
   security baselines with change management controls and drift monitoring?"
```

### 5.5 Compliance Checklist (Rows 33+)

**Located below data rows (starting Row 33).**

**Checklist Items (15 items including 3 regulatory):**

| # | Requirement | Evidence Type |
|---|-------------|---------------|
| 1 | Configuration baseline documented and version-controlled | Baseline document (PDF/Wiki) |
| 2 | CIS Benchmark or equivalent applied (Level 1 minimum) | CIS assessment report |
| 3 | Security-by-default verified for all deployments | Deployment template review |
| 4 | Configuration changes require change management approval | Change ticket screenshots |
| 5 | Automated drift detection configured (critical services) | Drift detection tool config |
| 6 | Configuration backups automated and tested | Backup job logs |
| 7 | Privileged access to config tools logged and reviewed | SIEM config logs |
| 8 | Hardening guides applied (vendor-specific) | Hardening checklist |
| 9 | Unnecessary services/features disabled | Config export showing disabled features |
| 10 | Secure defaults enforced via IaC/templates | IaC template (Terraform/ARM/CloudFormation) |
| 11 | Configuration validation before production deployment | Pre-deploy validation report |
| 12 | Baseline reviewed quarterly and updated as needed | Baseline review meeting notes |
| 13 | **(DORA)** Configuration documented for operational resilience | DORA config documentation |
| 14 | **(NIS2)** Secure deployment procedures validated | NIS2 compliance checklist |
| 15 | **(AI Act)** High-risk AI deployment controls implemented | AI system conformity assessment |

**Checklist Columns:**
- Column A: Checkbox (☐)
- Column B: Requirement text
- Column C: Evidence type

### 5.6 Example Data Row

**Row 7 (Example - Microsoft 365):**

| Col | Value | Notes |
|-----|-------|-------|
| A | CFG-003 | Auto-generated |
| B | Microsoft 365 | Service name |
| C | Microsoft Corporation | Vendor |
| D | SaaS | Service type |
| E | Production | Environment |
| F | Critical | Criticality |
| G | Confidential | Data class |
| H | Conditional Access Policy - Require MFA | Config item |
| I | ✅ Compliant | Status |
| J | `\\fileserver\ISMS\Evidence\A.5.23.3\M365\ConditionalAccess_MFA.png` | Evidence path |
| K | - | No gap |
| L | No | No remediation needed |
| M | - | No exception |
| N | - | No risk ID |
| O | - | No compensating controls |
| P | IT Operations | Responsible team |
| Q | - | No target date |
| R | CIS Microsoft 365 Foundations v2.0.0 | Baseline version |
| S | CHG-2024-1234 | Change mgmt ID |
| T | Enabled | Drift monitoring |
| U | Level 1 | CIS benchmark |
| V | 15.01.2026 | Last validated |
| W | Yes | Config backup |
| X | Yes | Privileged access log |
| Y | Yes | Security by default |
| Y | Documented | DORA (if applicable) |
| Z | Compliant | NIS2 (if applicable) |
| AA | N/A | AI Act (N/A for M365 non-AI) |

### 5.7 Cell Protection

**Protected cells (formulas):**
- Column A (Assessment_ID): Formula-generated, protected

**Unprotected cells (user input):**
- Columns B-AA: User-editable, yellow fill (FFFFCC)

**Sheet Protection:**
- Enable sheet protection with password
- Allow: Select unlocked cells, format cells, sort, filter
- Disallow: Edit formulas, insert/delete rows

### 5.8 Integration Points

**Imports from IMP-5.23.1 (Inventory):**
- Column B (Cloud_Service_Name): Import from IMP-5.23.1 Sheet 2 Column B
- Column C (Vendor_Name): Import from IMP-5.23.1 Sheet 2 Column C
- Column F (Service_Criticality): Import from IMP-5.23.1 Sheet 4 Column E
- Column G (Data_Classification): Import from IMP-5.23.1 Sheet 3 Column F

**Exports to Sheet 8 (Dashboard):**
- Column I (Status): Used in compliance percentage calculations
- Entire row: Used for gap analysis table

**Exports to Sheet 9 (Evidence Register):**
- Column J (Evidence_Location): Populated into evidence tracking table

---

---

## 6. Sheet 3: Access Control Setup

### 6.1 Purpose & Layout

**Sheet Name:** `3. Access Control Setup`

**Purpose:** Assess identity and access management (IAM) controls for cloud services, including SSO, MFA, RBAC, privileged access management, and service account security.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 5.3 (Access Control)

**Assessment Question:** "Are identity and access controls properly configured with SSO, MFA enforcement, role-based access control (RBAC), and privileged access management?"

### 6.2 Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns (see Section 1, Part 3)

**Extended Columns (R-X):** Access control-specific

| Column | Field Name | Width | Data Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **R** | SSO_Integrated | 16 | Dropdown | Yes, No, Planned, N/A | Is Single Sign-On (SSO) integrated with organization IdP? |
| **S** | MFA_Enforced | 16 | Dropdown | All Users, Admins Only, Not Enforced, N/A | Multi-Factor Authentication enforcement level |
| **T** | RBAC_Implemented | 16 | Dropdown | Yes, Partial, No, N/A | Is Role-Based Access Control (RBAC) implemented? |
| **U** | Privileged_Access_JIT | 18 | Dropdown | Enabled, Disabled, N/A | Just-In-Time (JIT) privileged access management |
| **V** | Service_Accounts_Inventoried | 20 | Dropdown | Yes, Partial, No, N/A | Are service accounts documented and reviewed? |
| **W** | Last_Access_Review | 18 | Date | - | Date of last user access review (quarterly minimum) |
| **X** | Admin_Account_Count | 16 | Integer | Positive integer | Number of accounts with administrative privileges |

### 6.3 Data Validation Rules (Extended Columns)

```python
# SSO Integrated (Column R)
sso_integrated_dv = DataValidation(
    type="list",
    formula1='"Yes,No,Planned,N/A"',
    allow_blank=False
)
ws.add_data_validation(sso_integrated_dv)
sso_integrated_dv.add("R5:R30")

# MFA Enforced (Column S)
mfa_enforced_dv = DataValidation(
    type="list",
    formula1='"All Users,Admins Only,Not Enforced,N/A"',
    allow_blank=False
)
ws.add_data_validation(mfa_enforced_dv)
mfa_enforced_dv.add("S5:S30")

# RBAC Implemented (Column T)
rbac_implemented_dv = DataValidation(
    type="list",
    formula1='"Yes,Partial,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(rbac_implemented_dv)
rbac_implemented_dv.add("T5:T30")

# Privileged Access JIT (Column U)
jit_access_dv = DataValidation(
    type="list",
    formula1='"Enabled,Disabled,N/A"',
    allow_blank=False
)
ws.add_data_validation(jit_access_dv)
jit_access_dv.add("U5:U30")

# Service Accounts Inventoried (Column V)
service_accounts_dv = DataValidation(
    type="list",
    formula1='"Yes,Partial,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(service_accounts_dv)
service_accounts_dv.add("V5:V30")

# Admin Account Count (Column X) - Integer validation
admin_count_dv = DataValidation(
    type="whole",
    operator="greaterThanOrEqual",
    formula1="0",
    allow_blank=True
)
ws.add_data_validation(admin_count_dv)
admin_count_dv.add("X5:X30")
```

### 6.4 Section Headers

```
Row 1 (merged A1:X1):
  "ACCESS CONTROL SETUP ASSESSMENT
   ISMS-POL-A.5.19-23-S5, Section 5.3: Identity & Access Management"

Row 2 (merged A2:X2):
  "Assessment Question: Are identity and access controls properly configured 
   with SSO, MFA enforcement, RBAC, and privileged access management?"
```

### 6.5 Compliance Checklist (Rows 33+)

**Checklist Items (12 items):**

| # | Requirement | Evidence Type |
|---|-------------|---------------|
| 1 | SSO integrated with organization identity provider (Azure AD/Okta/etc.) | SSO config screenshot |
| 2 | MFA enforced for all administrative accounts (minimum) | MFA policy screenshot |
| 3 | RBAC implemented with least-privilege principle | Role assignment export |
| 4 | Privileged access requires approval (JIT/PAM) | PAM tool config |
| 5 | Service accounts inventoried and reviewed quarterly | Service account inventory |
| 6 | Default admin accounts disabled or renamed | Account list export |
| 7 | Inactive accounts disabled after 90 days | Lifecycle policy config |
| 8 | Access reviews conducted quarterly (minimum) | Access review report |
| 9 | Emergency access procedures documented | Break-glass procedure doc |
| 10 | API keys/tokens rotated regularly | API key rotation policy |
| 11 | Federated identity used (no local cloud accounts) | IdP integration config |
| 12 | Conditional access policies enforce security requirements | Conditional access rules |

### 6.6 Example Data Row

**Row 7 (Example - AWS Production):**

| Col | Value | Notes |
|-----|-------|-------|
| A | CFG-003 | Auto-generated |
| B | AWS Production Account | Service name |
| C | Amazon Web Services | Vendor |
| D | IaaS | Service type |
| E | Production | Environment |
| F | Critical | Criticality |
| G | Confidential | Data class |
| H | IAM - MFA Enforced for Console Access | Config item |
| I | ✅ Compliant | Status |
| J | `s3://isms-evidence/A.5.23.3/AWS/IAM_MFA_Policy.json` | Evidence path |
| K | - | No gap |
| L | No | No remediation |
| M | - | No exception |
| N | - | No risk ID |
| O | - | No compensating controls |
| P | Cloud Ops | Responsible team |
| Q | - | No target date |
| R | Yes | SSO integrated (Azure AD SAML) |
| S | All Users | MFA enforced |
| T | Yes | RBAC via IAM policies |
| U | Enabled | JIT via AWS IAM Identity Center |
| V | Yes | Service accounts quarterly reviewed |
| W | 05.01.2026 | Last access review |
| X | 8 | Admin account count |

### 6.7 Integration Points

**Exports to Sheet 8 (Dashboard):**
- Column I (Status): Access control compliance metrics
- Column S (MFA_Enforced): MFA compliance percentage calculation

**Exports to Sheet 9 (Evidence Register):**
- Column J (Evidence_Location): IAM evidence tracking

---

## 7. Sheet 4: Network Security

### 7.1 Purpose & Layout

**Sheet Name:** `4. Network Security`

**Purpose:** Assess network-level security controls for cloud services, including IP restrictions, private connectivity, network segmentation, firewall rules, and DDoS protection.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 5.4 (Network Security)

**Assessment Question:** "Are network security controls properly configured with IP restrictions, private connectivity, network segmentation, and perimeter defenses?"

### 7.2 Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Extended Columns (R-X):** Network security-specific

| Column | Field Name | Width | Data Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **R** | IP_Restrictions | 16 | Dropdown | Enabled, Not Enabled, N/A | Are IP allowlists/denylists configured? |
| **S** | Private_Connectivity | 18 | Dropdown | ExpressRoute/VPN, VPC Peering, Public Only, N/A | Type of private network connectivity |
| **T** | Network_Segmentation | 18 | Dropdown | Implemented, Partial, Not Implemented, N/A | Is network segmentation (VNets/VPCs/subnets) configured? |
| **U** | WAF_Enabled | 14 | Dropdown | Yes, No, N/A | Is Web Application Firewall (WAF) enabled? |
| **V** | DDoS_Protection | 16 | Dropdown | Standard, Enhanced, Not Enabled, N/A | DDoS protection tier |
| **W** | Firewall_Rules_Documented | 20 | Dropdown | Yes, Partial, No, N/A | Are firewall/NSG rules documented? |
| **X** | Public_Endpoints_Count | 18 | Integer | Positive integer | Number of publicly accessible endpoints |

### 7.3 Data Validation Rules (Extended Columns)

```python
# IP Restrictions (Column R)
ip_restrictions_dv = DataValidation(
    type="list",
    formula1='"Enabled,Not Enabled,N/A"',
    allow_blank=False
)
ws.add_data_validation(ip_restrictions_dv)
ip_restrictions_dv.add("R5:R30")

# Private Connectivity (Column S)
private_connectivity_dv = DataValidation(
    type="list",
    formula1='"ExpressRoute/VPN,VPC Peering,Public Only,N/A"',
    allow_blank=False
)
ws.add_data_validation(private_connectivity_dv)
private_connectivity_dv.add("S5:S30")

# Network Segmentation (Column T)
network_segmentation_dv = DataValidation(
    type="list",
    formula1='"Implemented,Partial,Not Implemented,N/A"',
    allow_blank=False
)
ws.add_data_validation(network_segmentation_dv)
network_segmentation_dv.add("T5:T30")

# WAF Enabled (Column U)
waf_enabled_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(waf_enabled_dv)
waf_enabled_dv.add("U5:U30")

# DDoS Protection (Column V)
ddos_protection_dv = DataValidation(
    type="list",
    formula1='"Standard,Enhanced,Not Enabled,N/A"',
    allow_blank=False
)
ws.add_data_validation(ddos_protection_dv)
ddos_protection_dv.add("V5:V30")

# Firewall Rules Documented (Column W)
firewall_rules_dv = DataValidation(
    type="list",
    formula1='"Yes,Partial,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(firewall_rules_dv)
firewall_rules_dv.add("W5:W30")

# Public Endpoints Count (Column X)
public_endpoints_dv = DataValidation(
    type="whole",
    operator="greaterThanOrEqual",
    formula1="0",
    allow_blank=True
)
ws.add_data_validation(public_endpoints_dv)
public_endpoints_dv.add("X5:X30")
```

### 7.4 Section Headers

```
Row 1 (merged A1:X1):
  "NETWORK SECURITY CONFIGURATION ASSESSMENT
   ISMS-POL-A.5.19-23-S5, Section 5.4: Network Security Controls"

Row 2 (merged A2:X2):
  "Assessment Question: Are network security controls properly configured 
   with IP restrictions, private connectivity, segmentation, and perimeter defenses?"
```

### 7.5 Compliance Checklist (Rows 33+)

**Checklist Items (12 items):**

| # | Requirement | Evidence Type |
|---|-------------|---------------|
| 1 | IP restrictions configured for administrative access | Firewall rule export |
| 2 | Private connectivity used for production traffic (VPN/ExpressRoute) | VPN/ExpressRoute config |
| 3 | Network segmentation implemented (VNets/VPCs/subnets) | Network diagram |
| 4 | Web Application Firewall (WAF) enabled for public-facing services | WAF policy screenshot |
| 5 | DDoS protection enabled (Standard minimum, Enhanced for critical) | DDoS config screenshot |
| 6 | Firewall/NSG rules documented and reviewed quarterly | Firewall rule documentation |
| 7 | Default deny rule configured (deny all, allow specific) | Firewall rule export |
| 8 | Public endpoints minimized (only when business-required) | Public endpoint inventory |
| 9 | VPC/VNet peering restricted to trusted networks | Peering config export |
| 10 | Intrusion detection/prevention (IDS/IPS) enabled | IDS/IPS config |
| 11 | Network flow logs enabled and sent to SIEM | Flow log config |
| 12 | Egress filtering configured (data exfiltration prevention) | Egress rule export |

### 7.6 Example Data Row

**Row 7 (Example - Azure SQL Database):**

| Col | Value | Notes |
|-----|-------|-------|
| A | CFG-003 | Auto-generated |
| B | Azure SQL Database - Production | Service name |
| C | Microsoft Corporation | Vendor |
| D | PaaS | Service type |
| E | Production | Environment |
| F | Critical | Criticality |
| G | Confidential | Data class |
| H | SQL Firewall - IP Allowlist Configured | Config item |
| I | ✅ Compliant | Status |
| J | `\\fileserver\ISMS\Evidence\A.5.23.3\AzureSQL\Firewall_Rules.csv` | Evidence path |
| K | - | No gap |
| L | No | No remediation |
| M | - | No exception |
| N | - | No risk ID |
| O | - | No compensating controls |
| P | Cloud Ops | Responsible team |
| Q | - | No target date |
| R | Enabled | IP restrictions (corporate IP range only) |
| S | ExpressRoute/VPN | Private connectivity via ExpressRoute |
| T | Implemented | VNet integration with private endpoint |
| U | N/A | WAF (not applicable for SQL) |
| V | Standard | DDoS protection |
| W | Yes | Firewall rules documented in Wiki |
| X | 0 | No public endpoints (private endpoint only) |

### 7.7 Integration Points

**Exports to Sheet 8 (Dashboard):**
- Column I (Status): Network security compliance metrics
- Column X (Public_Endpoints_Count): Public exposure risk metric

---

## 8. Sheet 5: Encryption Configuration

### 8.1 Purpose & Layout

**Sheet Name:** `5. Encryption Configuration`

**Purpose:** Assess encryption controls for data at rest and in transit, key management practices, and cryptographic standards compliance.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 5.5 (Data Protection via Encryption)

**Assessment Question:** "Are encryption controls properly configured for data at rest, data in transit, with secure key management and cryptographic standards compliance?"

### 8.2 Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Extended Columns (R-X):** Encryption-specific

| Column | Field Name | Width | Data Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **R** | Encryption_At_Rest | 18 | Dropdown | AES-256, AES-128, Not Encrypted, N/A | Encryption algorithm for data at rest |
| **S** | Encryption_In_Transit | 18 | Dropdown | TLS 1.3, TLS 1.2, TLS 1.1/Lower, Not Encrypted, N/A | Encryption for data in transit |
| **T** | Encryption_Algorithm | 18 | Text | - | Specific algorithm/cipher suite used (e.g., "AES-256-GCM") |
| **U** | Key_Management | 20 | Dropdown | Customer-Managed (CMK), Microsoft-Managed, AWS-Managed, GCP-Managed, N/A | Who manages encryption keys? |
| **V** | Key_Rotation_Period | 18 | Dropdown | 90 Days, 180 Days, 365 Days, Manual, N/A | Automated key rotation frequency |
| **W** | HSM_Used | 14 | Dropdown | Yes, No, N/A | Is Hardware Security Module (HSM) used for key storage? |
| **X** | Last_Key_Rotation | 18 | Date | - | Date of last key rotation (or N/A if not rotated) |

### 8.3 Data Validation Rules (Extended Columns)

```python
# Encryption At Rest (Column R)
encryption_at_rest_dv = DataValidation(
    type="list",
    formula1='"AES-256,AES-128,Not Encrypted,N/A"',
    allow_blank=False
)
ws.add_data_validation(encryption_at_rest_dv)
encryption_at_rest_dv.add("R5:R30")

# Encryption In Transit (Column S)
encryption_in_transit_dv = DataValidation(
    type="list",
    formula1='"TLS 1.3,TLS 1.2,TLS 1.1/Lower,Not Encrypted,N/A"',
    allow_blank=False
)
ws.add_data_validation(encryption_in_transit_dv)
encryption_in_transit_dv.add("S5:S30")

# Key Management (Column U)
key_management_dv = DataValidation(
    type="list",
    formula1='"Customer-Managed (CMK),Microsoft-Managed,AWS-Managed,GCP-Managed,N/A"',
    allow_blank=False
)
ws.add_data_validation(key_management_dv)
key_management_dv.add("U5:U30")

# Key Rotation Period (Column V)
key_rotation_period_dv = DataValidation(
    type="list",
    formula1='"90 Days,180 Days,365 Days,Manual,N/A"',
    allow_blank=False
)
ws.add_data_validation(key_rotation_period_dv)
key_rotation_period_dv.add("V5:V30")

# HSM Used (Column W)
hsm_used_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(hsm_used_dv)
hsm_used_dv.add("W5:W30")
```

### 8.4 Section Headers

```
Row 1 (merged A1:X1):
  "ENCRYPTION CONFIGURATION ASSESSMENT
   ISMS-POL-A.5.19-23-S5, Section 5.5: Data Protection via Encryption"

Row 2 (merged A2:X2):
  "Assessment Question: Are encryption controls properly configured for data 
   at rest, data in transit, with secure key management and cryptographic standards?"
```

### 8.5 Compliance Checklist (Rows 33+)

**Checklist Items (12 items):**

| # | Requirement | Evidence Type |
|---|-------------|---------------|
| 1 | Data at rest encrypted (AES-256 minimum for Confidential data) | Encryption config screenshot |
| 2 | Data in transit encrypted (TLS 1.2+ minimum, TLS 1.3 preferred) | TLS config screenshot |
| 3 | Customer-managed keys (CMK) used for Confidential data | CMK config screenshot |
| 4 | Key rotation automated (365 days maximum) | Key rotation policy |
| 5 | HSM used for critical encryption keys | HSM integration config |
| 6 | Weak ciphers disabled (RC4, DES, 3DES, MD5) | Cipher suite config |
| 7 | Certificate validity monitored (expiration alerts) | Certificate monitoring config |
| 8 | Encryption key access logged and reviewed | Key access logs |
| 9 | Encryption algorithms comply with organizational crypto policy | Crypto policy alignment doc |
| 10 | Backup encryption verified (encrypted at rest) | Backup encryption config |
| 11 | Database-level encryption enabled (TDE, etc.) | Database encryption status |
| 12 | Field-level encryption for sensitive data (PII, PCI) | Field encryption config |

### 8.6 Example Data Row

**Row 7 (Example - AWS S3 Bucket):**

| Col | Value | Notes |
|-----|-------|-------|
| A | CFG-003 | Auto-generated |
| B | AWS S3 - Customer Data Bucket | Service name |
| C | Amazon Web Services | Vendor |
| D | Storage Service | Service type |
| E | Production | Environment |
| F | High | Criticality |
| G | Confidential | Data class |
| H | S3 Bucket Encryption - SSE-KMS | Config item |
| I | ✅ Compliant | Status |
| J | `s3://isms-evidence/A.5.23.3/AWS-S3/Bucket_Encryption.json` | Evidence path |
| K | - | No gap |
| L | No | No remediation |
| M | - | No exception |
| N | - | No risk ID |
| O | - | No compensating controls |
| P | Cloud Ops | Responsible team |
| Q | - | No target date |
| R | AES-256 | Encryption at rest |
| S | TLS 1.3 | Encryption in transit |
| T | AES-256-GCM | Algorithm |
| U | Customer-Managed (CMK) | Key management via AWS KMS |
| V | 365 Days | Key rotation period |
| W | Yes | HSM via AWS KMS (CloudHSM) |
| X | 01.01.2026 | Last key rotation |

### 8.7 Integration Points

**Exports to Sheet 8 (Dashboard):**
- Column I (Status): Encryption compliance metrics
- Column U (Key_Management): CMK adoption percentage

---

## 9. Sheet 6: Deployment Checklist

### 9.1 Purpose & Layout

**Sheet Name:** `6. Deployment Checklist`

**Purpose:** Assess pre-deployment validation, secure deployment procedures, monitoring setup, and rollback readiness for cloud services.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 5.6 (Secure Deployment)

**Assessment Question:** "Are secure deployment procedures followed with pre-deployment validation, monitoring setup, and rollback readiness?"

### 9.2 Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Extended Columns (R-X):** Deployment-specific

| Column | Field Name | Width | Data Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **R** | Pre_Deployment_Checklist | 18 | Dropdown | Completed, Partial, Not Completed, N/A | Pre-deployment security checklist status |
| **S** | Security_Scan_Performed | 18 | Dropdown | Passed, Failed, Not Performed, N/A | Security scanning before deployment (SAST/DAST/IaC scan) |
| **T** | Monitoring_Configured | 18 | Dropdown | Yes, Partial, No, N/A | Is monitoring/alerting configured? |
| **U** | Rollback_Plan_Tested | 18 | Dropdown | Yes, No, N/A | Is rollback procedure tested and documented? |
| **V** | Change_Approval_ID | 18 | Text | - | Change management approval ticket ID |
| **W** | Deployment_Date | 18 | Date | - | Date service was deployed to this environment |
| **X** | Post_Deployment_Validation | 18 | Dropdown | Passed, Failed, Not Performed, N/A | Post-deployment validation status |

### 9.3 Data Validation Rules (Extended Columns)

```python
# Pre-Deployment Checklist (Column R)
pre_deployment_dv = DataValidation(
    type="list",
    formula1='"Completed,Partial,Not Completed,N/A"',
    allow_blank=False
)
ws.add_data_validation(pre_deployment_dv)
pre_deployment_dv.add("R5:R30")

# Security Scan Performed (Column S)
security_scan_dv = DataValidation(
    type="list",
    formula1='"Passed,Failed,Not Performed,N/A"',
    allow_blank=False
)
ws.add_data_validation(security_scan_dv)
security_scan_dv.add("S5:S30")

# Monitoring Configured (Column T)
monitoring_configured_dv = DataValidation(
    type="list",
    formula1='"Yes,Partial,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(monitoring_configured_dv)
monitoring_configured_dv.add("T5:T30")

# Rollback Plan Tested (Column U)
rollback_plan_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(rollback_plan_dv)
rollback_plan_dv.add("U5:U30")

# Post-Deployment Validation (Column X)
post_deployment_dv = DataValidation(
    type="list",
    formula1='"Passed,Failed,Not Performed,N/A"',
    allow_blank=False
)
ws.add_data_validation(post_deployment_dv)
post_deployment_dv.add("X5:X30")
```

### 9.4 Section Headers

```
Row 1 (merged A1:X1):
  "DEPLOYMENT CHECKLIST ASSESSMENT
   ISMS-POL-A.5.19-23-S5, Section 5.6: Secure Deployment Procedures"

Row 2 (merged A2:X2):
  "Assessment Question: Are secure deployment procedures followed with 
   pre-deployment validation, monitoring setup, and rollback readiness?"
```

### 9.5 Compliance Checklist (Rows 33+)

**Checklist Items (15 items including 3 regulatory):**

| # | Requirement | Evidence Type |
|---|-------------|---------------|
| 1 | Pre-deployment security checklist completed | Checklist document |
| 2 | Infrastructure-as-Code (IaC) security scan performed | IaC scan report (Checkov/tfsec/etc.) |
| 3 | Security configuration validated against baseline | Config validation report |
| 4 | Monitoring and alerting configured before deployment | Monitoring config |
| 5 | Rollback plan documented and tested | Rollback procedure doc |
| 6 | Change management approval obtained | Change ticket |
| 7 | Post-deployment validation performed | Validation test results |
| 8 | Security team notified of deployment | Notification email |
| 9 | Backup/recovery tested before production deployment | Backup test report |
| 10 | Access controls verified post-deployment | Access control validation |
| 11 | Incident response plan updated for new service | IR plan update |
| 12 | Documentation updated (architecture diagrams, runbooks) | Updated docs |
| 13 | **(DORA)** Operational resilience validated | DORA resilience assessment |
| 14 | **(NIS2)** Secure-by-default configuration validated | NIS2 compliance checklist |
| 15 | **(AI Act)** High-risk AI deployment controls validated | AI conformity assessment |

### 9.6 Example Data Row

**Row 7 (Example - Kubernetes Cluster Deployment):**

| Col | Value | Notes |
|-----|-------|-------|
| A | CFG-003 | Auto-generated |
| B | AKS Production Cluster | Service name |
| C | Microsoft Corporation | Vendor |
| D | PaaS | Service type |
| E | Production | Environment |
| F | Critical | Criticality |
| G | Confidential | Data class |
| H | Kubernetes RBAC - Pod Security Standards | Config item |
| I | ✅ Compliant | Status |
| J | `\\fileserver\ISMS\Evidence\A.5.23.3\AKS\PodSecurityPolicy.yaml` | Evidence path |
| K | - | No gap |
| L | No | No remediation |
| M | - | No exception |
| N | - | No risk ID |
| O | - | No compensating controls |
| P | Platform Engineering | Responsible team |
| Q | - | No target date |
| R | Completed | Pre-deployment checklist |
| S | Passed | IaC scan with Checkov |
| T | Yes | Monitoring via Azure Monitor + Prometheus |
| U | Yes | Rollback tested in staging |
| V | CHG-2025-0123 | Change approval |
| W | 10.01.2026 | Deployment date |
| X | Passed | Post-deployment validation |

### 9.7 Integration Points

**Exports to Sheet 8 (Dashboard):**
- Column I (Status): Deployment compliance metrics
- Column S (Security_Scan_Performed): Security scanning compliance

---

## 10. Sheet 7: Jurisdictional Risk

### 10.1 Purpose & Layout

**Sheet Name:** `7. Jurisdictional Risk`

**Purpose:** Assess jurisdictional risks related to US CLOUD Act exposure, data sovereignty requirements, and cross-border data access for cloud providers with US nexus.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 5.7 (Jurisdictional Risk Management - NEW)

**Assessment Question:** "Does the cloud provider have US nexus requiring CLOUD Act assessment, and are adequate safeguards in place to protect data sovereignty?"

**Applicability:** Complete this sheet ONLY for cloud providers with:
- US headquarters (e.g., Microsoft, AWS, Google, Oracle, Salesforce)
- US parent company (e.g., LinkedIn → Microsoft, GitHub → Microsoft)
- Significant US operations or subsidiaries

**Skip this sheet for:** Pure EU/Swiss providers (e.g., IONOS, Infomaniak, Open Telekom Cloud)

### 10.2 Column Structure (A-T, 20 columns)

**Different structure from other sheets** - Jurisdictional risk has unique columns optimized for legal/compliance assessment.

| Column | Field Name | Width | Data Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **A** | Assessment_ID | 14 | Formula | - | Auto-generated: `=CONCATENATE("JRA-",TEXT(ROW()-4,"000"))` |
| **B** | Cloud_Service_Name | 28 | Text | - | Service name (import from IMP-5.23.1) |
| **C** | Vendor_Name | 22 | Text | - | Provider name |
| **D** | Provider_HQ_Jurisdiction | 22 | Dropdown | United States, EU Member State, Switzerland, Other | Legal jurisdiction of provider HQ |
| **E** | US_Parent_Company | 18 | Dropdown | Yes, No | Does provider have US parent company? |
| **F** | CLOUD_Act_Exposure | 20 | Dropdown | Direct (US Company), Indirect (US Subsidiary), None | CLOUD Act applicability |
| **G** | Data_Processing_Locations | 25 | Text | - | Where is data actually stored/processed? (e.g., "EU, Switzerland") |
| **H** | EU_Data_Boundary_Available | 20 | Dropdown | Yes, No, N/A | Does provider offer EU Data Boundary feature? |
| **I** | EU_Data_Boundary_Enabled | 20 | Dropdown | Yes, No, N/A | Is EU Data Boundary actually enabled? |
| **J** | Customer_Managed_Keys | 18 | Dropdown | Yes, No, N/A | Are customer-managed encryption keys used? (CLOUD Act mitigation) |
| **K** | Legal_Challenge_Commitment | 22 | Dropdown | Yes, Partial, No, N/A | Has provider committed to legally challenge gov't data requests? |
| **L** | Transfer_Mechanism | 20 | Dropdown | Adequacy Decision, SCCs, BCRs, Derogation, None | Legal basis for cross-border data transfer |
| **M** | SCCs_In_DPA | 16 | Dropdown | Yes, No, N/A | Are Standard Contractual Clauses (SCCs) in DPA? |
| **N** | Residual_Risk_Level | 18 | Dropdown | Low, Medium, High, Critical | Overall jurisdictional risk after mitigations |
| **O** | Risk_Owner | 18 | Dropdown | CISO, DPO, Legal, CIO | Who owns this residual risk? |
| **P** | Risk_Acceptance_Date | 18 | Date | - | Date risk was formally accepted |
| **Q** | Compensating_Controls | 30 | Text | - | Additional safeguards (CMK, data minimization, encryption, etc.) |
| **R** | Next_Review_Date | 18 | Date | - | Next jurisdictional risk review (annual minimum) |
| **S** | Evidence_ID | 14 | Text | - | Reference to evidence register entry |
| **T** | Notes | 30 | Text | - | Additional context or special considerations |

### 10.3 Data Validation Rules (All Columns)

```python
# Provider HQ Jurisdiction (Column D)
provider_hq_dv = DataValidation(
    type="list",
    formula1='"United States,EU Member State,Switzerland,Other"',
    allow_blank=False
)
ws.add_data_validation(provider_hq_dv)
provider_hq_dv.add("D5:D30")

# US Parent Company (Column E)
us_parent_dv = DataValidation(
    type="list",
    formula1='"Yes,No"',
    allow_blank=False
)
ws.add_data_validation(us_parent_dv)
us_parent_dv.add("E5:E30")

# CLOUD Act Exposure (Column F)
cloud_act_exposure_dv = DataValidation(
    type="list",
    formula1='"Direct (US Company),Indirect (US Subsidiary),None"',
    allow_blank=False
)
ws.add_data_validation(cloud_act_exposure_dv)
cloud_act_exposure_dv.add("F5:F30")

# EU Data Boundary Available (Column H)
eu_boundary_available_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(eu_boundary_available_dv)
eu_boundary_available_dv.add("H5:H30")

# EU Data Boundary Enabled (Column I)
eu_boundary_enabled_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(eu_boundary_enabled_dv)
eu_boundary_enabled_dv.add("I5:I30")

# Customer Managed Keys (Column J)
cmk_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(cmk_dv)
cmk_dv.add("J5:J30")

# Legal Challenge Commitment (Column K)
legal_challenge_dv = DataValidation(
    type="list",
    formula1='"Yes,Partial,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(legal_challenge_dv)
legal_challenge_dv.add("K5:K30")

# Transfer Mechanism (Column L)
transfer_mechanism_dv = DataValidation(
    type="list",
    formula1='"Adequacy Decision,SCCs,BCRs,Derogation,None"',
    allow_blank=False
)
ws.add_data_validation(transfer_mechanism_dv)
transfer_mechanism_dv.add("L5:L30")

# SCCs in DPA (Column M)
sccs_in_dpa_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(sccs_in_dpa_dv)
sccs_in_dpa_dv.add("M5:M30")

# Residual Risk Level (Column N)
residual_risk_dv = DataValidation(
    type="list",
    formula1='"Low,Medium,High,Critical"',
    allow_blank=False
)
ws.add_data_validation(residual_risk_dv)
residual_risk_dv.add("N5:N30")

# Risk Owner (Column O)
risk_owner_dv = DataValidation(
    type="list",
    formula1='"CISO,DPO,Legal,CIO"',
    allow_blank=False
)
ws.add_data_validation(risk_owner_dv)
risk_owner_dv.add("O5:O30")
```

### 10.4 Section Headers

```
Row 1 (merged A1:T1):
  "JURISDICTIONAL RISK ASSESSMENT (US CLOUD Act)
   ISMS-POL-A.5.19-23-S5, Section 5.7: Data Sovereignty & Cross-Border Access"

Row 2 (merged A2:T2):
  "Assessment Question: Does the cloud provider have US nexus requiring CLOUD Act 
   assessment, and are adequate safeguards in place to protect data sovereignty?"
```

### 10.5 Compliance Checklist (Rows 33+)

**Checklist Items (10 items):**

| # | Requirement | Evidence Type |
|---|-------------|---------------|
| 1 | Provider HQ jurisdiction identified and documented | Vendor documentation |
| 2 | US parent company status verified | Corporate structure review |
| 3 | CLOUD Act exposure assessed for US-nexus providers | Legal review |
| 4 | Data processing locations documented in DPA | DPA review |
| 5 | EU Data Boundary availability checked | Vendor announcement/docs |
| 6 | Customer-managed encryption keys option evaluated | Technical documentation |
| 7 | Legal challenge commitment verified | Contract/Public statement |
| 8 | Transfer mechanism documented (SCCs, BCRs, etc.) | DPA |
| 9 | Risk acceptance recorded if residual risk remains | Risk register |
| 10 | Compensating controls documented for high-risk providers | Control documentation |

### 10.6 Example Data Rows

**Row 7 (Example 1 - Microsoft 365 with EU Data Boundary):**

| Col | Value | Notes |
|-----|-------|-------|
| A | JRA-003 | Auto-generated |
| B | Microsoft 365 | Service name |
| C | Microsoft Corporation | Vendor |
| D | United States | Provider HQ |
| E | No | No US parent (is the parent) |
| F | Direct (US Company) | CLOUD Act applies |
| G | EU, Switzerland (EU Data Boundary enabled) | Processing locations |
| H | Yes | EU Data Boundary available |
| I | Yes | EU Data Boundary enabled |
| J | Yes | CMK via Azure Key Vault |
| K | Yes | Microsoft public commitment |
| L | Adequacy Decision | Swiss-US Data Privacy Framework |
| M | SCCs | SCCs in DPA |
| N | Medium | Residual risk after mitigations |
| O | CISO | Risk owner |
| P | 15.01.2026 | Risk acceptance date |
| Q | EU Data Boundary + Customer Lockbox + CMK | Compensating controls |
| R | 15.01.2027 | Next review (annual) |
| S | EV-JRA-001 | Evidence ID |
| T | Covered by Swiss-US DPF adequacy decision | Notes |

**Row 8 (Example 2 - AWS with US CLOUD Act Exposure):**

| Col | Value | Notes |
|-----|-------|-------|
| A | JRA-004 | Auto-generated |
| B | AWS Production Account | Service name |
| C | Amazon Web Services | Vendor |
| D | United States | Provider HQ |
| E | No | No US parent (is the parent) |
| F | Direct (US Company) | CLOUD Act applies |
| G | eu-central-1 (Frankfurt) | Processing location |
| H | No | No EU Data Boundary feature |
| I | N/A | N/A (feature not available) |
| J | Yes | CMK via AWS KMS |
| K | Partial | Case-by-case legal review commitment |
| L | SCCs | SCCs in AWS DPA |
| M | Yes | SCCs included |
| N | High | Residual risk (no data boundary) |
| O | DPO | Risk owner (data protection issue) |
| P | 20.01.2026 | Risk acceptance date |
| Q | CMK + Data minimization + Access logging | Compensating controls |
| R | 20.07.2026 | Next review (6 months - high risk) |
| S | EV-JRA-002 | Evidence ID |
| T | High-risk accepted due to lack of EU alternatives for IaaS | Notes |

**Row 9 (Example 3 - EU Provider - Sheet Not Needed):**

This row would be **EMPTY** or **marked N/A** for pure EU providers like IONOS, Infomaniak, etc., as Sheet 7 only applies to US-nexus providers.

### 10.7 Conditional Formatting

**Risk Level Color Coding (Column N):**

```python
from openpyxl.styles import PatternFill

# Low Risk - Green
low_risk_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")

# Medium Risk - Yellow
medium_risk_fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")

# High Risk - Orange
high_risk_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")

# Critical Risk - Red
critical_risk_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")

# Apply conditional formatting to Column N (Residual_Risk_Level)
for row in range(5, 31):  # Data rows 5-30
    cell = ws.cell(row=row, column=14)  # Column N
    if cell.value == "Low":
        cell.fill = low_risk_fill
    elif cell.value == "Medium":
        cell.fill = medium_risk_fill
    elif cell.value == "High":
        cell.fill = high_risk_fill
    elif cell.value == "Critical":
        cell.fill = critical_risk_fill
```

### 10.8 Integration Points

**Imports from IMP-5.23.1 (Inventory):**
- Column B (Cloud_Service_Name): Import from IMP-5.23.1 Sheet 2 Column B
- Column C (Vendor_Name): Import from IMP-5.23.1 Sheet 2 Column C

**Imports from IMP-5.23.2 (Vendor Due Diligence):**
- Column D (Provider_HQ_Jurisdiction): Import from IMP-5.23.2 Sheet 7 Column D
- Column L (Transfer_Mechanism): Import from IMP-5.23.2 Sheet 5 Column N

**Exports to Sheet 8 (Dashboard):**
- Column N (Residual_Risk_Level): Jurisdictional risk summary table
- All rows: Jurisdictional risk heatmap

**Exports to Sheet 9 (Evidence Register):**
- Column S (Evidence_ID): Links to evidence tracking

---

## 11. Sheet 8: Summary Dashboard

### 11.1 Purpose & Layout

**Sheet Name:** `8. Summary Dashboard`

**Purpose:** Provide executive-level compliance overview by consolidating data from all assessment sheets (Sheets 2-7) into 4 summary tables with auto-calculated metrics.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 5.8 (Assessment Dashboard)

**Layout:** Dashboard-style with 4 distinct tables (no data entry - formulas only)

### 11.2 Dashboard Structure

```
┌─────────────────────────────────────────────────────────────────┐
│ Row 1:  SECURE CONFIGURATION - COMPLIANCE SUMMARY DASHBOARD     │
│         (Header, merged A1:G1)                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ TABLE 1: COMPLIANCE BY CONFIGURATION AREA (Rows 3-11)           │
│ ┌───────────────────────────────────────────────────────────┐   │
│ │ Configuration Area │ Total │ ✅ │ ⚠️ │ ❌ │ N/A │ % │     │   
│ ├───────────────────────────────────────────────────────────┤   │
│ │ Config Baseline    │   26  │ 20 │  4 │  2 │  0  │ 77% │   │
│ │ Access Control     │   26  │ 24 │  1 │  1 │  0  │ 92% │   │
│ │ Network Security   │   26  │ 22 │  3 │  1 │  0  │ 85% │   │
│ │ Encryption         │   26  │ 25 │  1 │  0 │  0  │ 96% │   │
│ │ Deployment         │   26  │ 23 │  2 │  1 │  0  │ 88% │   │
│ │ **OVERALL**        │  130  │114 │ 11 │  5 │  0  │ 88% │   │
│ └───────────────────────────────────────────────────────────┘   │
│                                                                 │
│ TABLE 2: TOP 5 NON-COMPLIANT CONFIG ITEMS (Rows 13-19)          │
│ ┌───────────────────────────────────────────────────────────┐   │
│ │ Service │ Config Item │ Area │ Status │ Remediation Date  │   │
│ ├───────────────────────────────────────────────────────────┤   │
│ │ AWS     │ MFA All     │ IAM  │ ❌     │ 15.02.2026        │   │
│ │ Azure   │ NSG Rules   │ Net  │ ❌     │ 20.02.2026        │   │
│ │ ...     │ ...         │ ...  │ ...    │ ...               │   │
│ └───────────────────────────────────────────────────────────┘   │
│                                                                 │
│ TABLE 3: JURISDICTIONAL RISK SUMMARY (Rows 21-28)               │
│ ┌───────────────────────────────────────────────────────────┐   │
│ │ Provider │ CLOUD Act │ Data Boundary │ CMK │ Risk Level   │   │
│ ├───────────────────────────────────────────────────────────┤   │
│ │ Microsoft│ Direct    │ Enabled       │ Yes │ Medium       │   │
│ │ AWS      │ Direct    │ No            │ Yes │ High         │   │
│ │ Google   │ Direct    │ No            │ Yes │ High         │   │
│ │ ...      │ ...       │ ...           │ ... │ ...          │   │
│ └───────────────────────────────────────────────────────────┘   │
│                                                                 │
│ TABLE 4: REGULATORY COMPLIANCE (Rows 30-36)                     │
│ ┌───────────────────────────────────────────────────────────┐   │
│ │ Regulation │ Applicable Services │ Compliant │ Gaps │ %   │   │
│ ├───────────────────────────────────────────────────────────┤   │
│ │ DORA       │ 12                  │ 10        │  2   │ 83% │   │
│ │ NIS2       │ 8                   │ 7         │  1   │ 88% │   │
│ │ AI Act     │ 3                   │ 3         │  0   │100% │   │
│ │ CLOUD Act  │ 15                  │ 12        │  3   │ 80% │   │
│ └───────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 11.3 Table 1: Compliance by Configuration Area

**Purpose:** Show overall compliance percentage by configuration sheet.

**Columns:**
- A: Configuration Area
- B: Total Items (count of rows in source sheet)
- C: ✅ Compliant (count of Status = "✅ Compliant")
- D: ⚠️ Partial (count of Status = "⚠️ Partial")
- E: ❌ Non-Compliant (count of Status = "❌ Non-Compliant")
- F: N/A (count of Status = "N/A")
- G: Compliance % (formula: `=(C/B)*100`)

**Formulas (Row 5 - Configuration Baseline):**

```excel
# Cell B5 - Total Items (Configuration Baseline)
=COUNTA('2. Configuration Baseline'!$I$5:$I$30)

# Cell C5 - Compliant Count
=COUNTIF('2. Configuration Baseline'!$I$5:$I$30,"✅ Compliant")

# Cell D5 - Partial Count
=COUNTIF('2. Configuration Baseline'!$I$5:$I$30,"⚠️ Partial")

# Cell E5 - Non-Compliant Count
=COUNTIF('2. Configuration Baseline'!$I$5:$I$30,"❌ Non-Compliant")

# Cell F5 - N/A Count
=COUNTIF('2. Configuration Baseline'!$I$5:$I$30,"N/A")

# Cell G5 - Compliance Percentage
=IF(B5>0,ROUND((C5/B5)*100,0),"N/A")
```

**Repeat for rows 6-9** (Access Control, Network, Encryption, Deployment)

**Row 10 - OVERALL TOTALS:**

```excel
# Cell B10 - Total Items (all sheets)
=SUM(B5:B9)

# Cell C10 - Total Compliant
=SUM(C5:C9)

# Cell D10 - Total Partial
=SUM(D5:D9)

# Cell E10 - Total Non-Compliant
=SUM(E5:E9)

# Cell F10 - Total N/A
=SUM(F5:F9)

# Cell G10 - Overall Compliance %
=IF(B10>0,ROUND((C10/B10)*100,0),"N/A")
```

### 11.4 Table 2: Top 5 Non-Compliant Config Items

**Purpose:** Highlight top 5 non-compliant items requiring immediate attention.

**Columns:**
- A: Service Name
- B: Configuration Item
- C: Area (Config/IAM/Network/Encryption/Deploy)
- D: Status (should always be ❌ Non-Compliant)
- E: Target Remediation Date

**Data Source:** Filter all assessment sheets (2-6) for `Status = "❌ Non-Compliant"`, sort by `Target_Remediation_Date` (earliest first), take top 5.

**Implementation:**
This requires manual population OR use of advanced Excel features (FILTER + SORT in Excel 365) OR Python-generated pre-populated static values.

**Python-Generated Approach (in generator script):**

```python
# In create_8_summary_dashboard() function:
# After creating table headers, pre-populate with top 5 non-compliant items
# This is a SAMPLE - actual implementation would scan Sheets 2-6

sample_top_5_gaps = [
    ("AWS Production", "IAM - MFA Not Enforced for All Users", "Access Control", "❌ Non-Compliant", "15.02.2026"),
    ("Azure SQL", "Network - Public Endpoint Exposed", "Network Security", "❌ Non-Compliant", "20.02.2026"),
    ("GCP Storage", "Encryption - CMK Not Configured", "Encryption", "❌ Non-Compliant", "28.02.2026"),
    ("Oracle Cloud", "Deployment - Rollback Plan Not Tested", "Deployment", "❌ Non-Compliant", "05.03.2026"),
    ("Salesforce", "Config - Drift Monitoring Disabled", "Config Baseline", "❌ Non-Compliant", "10.03.2026"),
]

row = 15  # Start row for gap data
for service, config_item, area, status, remediation_date in sample_top_5_gaps:
    ws.cell(row=row, column=1, value=service)
    ws.cell(row=row, column=2, value=config_item)
    ws.cell(row=row, column=3, value=area)
    ws.cell(row=row, column=4, value=status)
    ws.cell(row=row, column=5, value=remediation_date)
    row += 1
```

**Note:** In production, this would be replaced by a consolidation script that dynamically scans all assessment sheets.

### 11.5 Table 3: Jurisdictional Risk Summary

**Purpose:** Show US CLOUD Act exposure for all US-nexus providers.

**Columns:**
- A: Provider Name
- B: CLOUD Act Exposure (Direct/Indirect/None)
- C: EU Data Boundary (Enabled/Not Available/N/A)
- D: Customer-Managed Keys (Yes/No)
- E: Residual Risk Level (Low/Medium/High/Critical)

**Data Source:** Sheet 7 (Jurisdictional Risk) - ALL rows where CLOUD Act Exposure ≠ "None"

**Formulas (Row 23 onwards - dynamic reference to Sheet 7):**

```excel
# Cell A23 - Provider Name (first US-nexus provider)
=IF(ROWS('7. Jurisdictional Risk'!$C$5:$C$30)>=1,'7. Jurisdictional Risk'!C5,"")

# Cell B23 - CLOUD Act Exposure
=IF(ROWS('7. Jurisdictional Risk'!$F$5:$F$30)>=1,'7. Jurisdictional Risk'!F5,"")

# Cell C23 - EU Data Boundary
=IF(ROWS('7. Jurisdictional Risk'!$I$5:$I$30)>=1,'7. Jurisdictional Risk'!I5,"")

# Cell D23 - CMK
=IF(ROWS('7. Jurisdictional Risk'!$J$5:$J$30)>=1,'7. Jurisdictional Risk'!J5,"")

# Cell E23 - Risk Level
=IF(ROWS('7. Jurisdictional Risk'!$N$5:$N$30)>=1,'7. Jurisdictional Risk'!N5,"")
```

**Repeat for rows 24-27** (up to 5 providers)

**Alternative (Python-Generated Static Summary):**

```python
# In create_8_summary_dashboard() function:
# Table 3: Jurisdictional Risk Summary

jurisdictional_summary = [
    ("Microsoft Corporation", "Direct (US Company)", "Enabled", "Yes", "Medium"),
    ("Amazon Web Services", "Direct (US Company)", "No", "Yes", "High"),
    ("Google Cloud", "Direct (US Company)", "No", "Yes", "High"),
    ("Oracle Cloud", "Direct (US Company)", "No", "Yes", "High"),
    ("Salesforce", "Direct (US Company)", "No", "Partial", "High"),
]

row = 23  # Start row
for provider, cloud_act, boundary, cmk, risk_level in jurisdictional_summary:
    ws.cell(row=row, column=1, value=provider)
    ws.cell(row=row, column=2, value=cloud_act)
    ws.cell(row=row, column=3, value=boundary)
    ws.cell(row=row, column=4, value=cmk)
    ws.cell(row=row, column=5, value=risk_level)
    
    # Color-code risk level (Column E)
    risk_cell = ws.cell(row=row, column=5)
    if risk_level == "Low":
        risk_cell.fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    elif risk_level == "Medium":
        risk_cell.fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
    elif risk_level in ["High", "Critical"]:
        risk_cell.fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    
    row += 1
```

### 11.6 Table 4: Regulatory Compliance

**Purpose:** Show compliance status for DORA, NIS2, AI Act, and US CLOUD Act.

**Columns:**
- A: Regulation
- B: Applicable Services (count)
- C: Compliant (count where regulatory column = "Compliant" or equivalent)
- D: Gaps (count where regulatory column = "Non-Compliant" or equivalent)
- E: Compliance %

**Formulas (Row 32 - DORA):**

```excel
# Cell B32 - Applicable Services (DORA)
# Count services where Column Y (DORA_Config_Documentation) is NOT "N/A"
=COUNTIF('2. Configuration Baseline'!$Y$5:$Y$30,"<>N/A")

# Cell C32 - Compliant
# Count where DORA_Config_Documentation = "Documented"
=COUNTIF('2. Configuration Baseline'!$Y$5:$Y$30,"Documented")

# Cell D32 - Gaps
# Count where DORA_Config_Documentation = "Not Documented" or "Partially Documented"
=COUNTIF('2. Configuration Baseline'!$Y$5:$Y$30,"Not Documented")+COUNTIF('2. Configuration Baseline'!$Y$5:$Y$30,"Partially Documented")

# Cell E32 - Compliance %
=IF(B32>0,ROUND((C32/B32)*100,0),"N/A")
```

**Row 33 - NIS2:**

```excel
# Cell B33 - Applicable Services (NIS2)
=COUNTIF('2. Configuration Baseline'!$Z$5:$Z$30,"<>N/A")

# Cell C33 - Compliant
=COUNTIF('2. Configuration Baseline'!$Z$5:$Z$30,"Compliant")

# Cell D33 - Gaps
=COUNTIF('2. Configuration Baseline'!$Z$5:$Z$30,"Non-Compliant")+COUNTIF('2. Configuration Baseline'!$Z$5:$Z$30,"Partially Compliant")

# Cell E33 - Compliance %
=IF(B33>0,ROUND((C33/B33)*100,0),"N/A")
```

**Row 34 - AI Act:**

```excel
# Cell B34 - Applicable Services (AI Act)
=COUNTIF('2. Configuration Baseline'!$AA$5:$AA$30,"<>N/A")

# Cell C34 - Compliant
=COUNTIF('2. Configuration Baseline'!$AA$5:$AA$30,"Full Controls")

# Cell D34 - Gaps
=COUNTIF('2. Configuration Baseline'!$AA$5:$AA$30,"No Controls")+COUNTIF('2. Configuration Baseline'!$AA$5:$AA$30,"Partial Controls")

# Cell E34 - Compliance %
=IF(B34>0,ROUND((C34/B34)*100,0),"N/A")
```

**Row 35 - CLOUD Act:**

```excel
# Cell B35 - Applicable Services (CLOUD Act)
# Count services in Sheet 7 where CLOUD_Act_Exposure ≠ "None"
=COUNTIF('7. Jurisdictional Risk'!$F$5:$F$30,"Direct (US Company)")+COUNTIF('7. Jurisdictional Risk'!$F$5:$F$30,"Indirect (US Subsidiary)")

# Cell C35 - Compliant (Low or Medium risk acceptable)
=COUNTIF('7. Jurisdictional Risk'!$N$5:$N$30,"Low")+COUNTIF('7. Jurisdictional Risk'!$N$5:$N$30,"Medium")

# Cell D35 - Gaps (High or Critical risk)
=COUNTIF('7. Jurisdictional Risk'!$N$5:$N$30,"High")+COUNTIF('7. Jurisdictional Risk'!$N$5:$N$30,"Critical")

# Cell E35 - Compliance %
=IF(B35>0,ROUND((C35/B35)*100,0),"N/A")
```

### 11.7 Cell Styling (Dashboard)

**Table Headers:**
- Font: Calibri 11, Bold, White
- Fill: Dark Blue (003366)
- Alignment: Center, Wrap

**Table Data Cells:**
- Font: Calibri 10, Normal
- Fill: None (white background)
- Alignment: Left (text), Center (numbers)

**Compliance Percentage Cells (Column G, E):**
- Conditional formatting:
  - ≥90%: Green (C6EFCE)
  - 70-89%: Yellow (FFEB9C)
  - <70%: Orange (FFC7CE)

**Status Symbol Cells:**
- Font: Calibri 10 (UTF-8 symbols render natively)
- ✅ (Compliant): Green text
- ⚠️ (Partial): Yellow/Orange text
- ❌ (Non-Compliant): Red text

### 11.8 Integration Points

**Data Sources:**
- Sheet 2 (Configuration Baseline): Columns I, Y, Z, AA → Table 1, Table 4
- Sheet 3 (Access Control): Column I → Table 1
- Sheet 4 (Network Security): Column I → Table 1
- Sheet 5 (Encryption): Column I → Table 1
- Sheet 6 (Deployment): Column I → Table 1
- Sheet 7 (Jurisdictional Risk): Columns F, I, J, N → Table 3, Table 4
- Sheets 2-6 (All): Column I where Status = "❌ Non-Compliant" → Table 2

**Data Consumers:**
- This dashboard is the **primary output** for executive review (CISO, CIO)
- No downstream dependencies (terminal node in data flow)

---

## 12. Sheet 9: Evidence Register

### 12.1 Purpose & Layout

**Sheet Name:** `9. Evidence Register`

**Purpose:** Centralized tracking of ALL evidence files referenced across assessment sheets (2-7), with metadata for audit trail and evidence lifecycle management.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 5.9 (Evidence Management)

**Layout:** Tabular register with evidence metadata (one row per evidence file)

### 12.2 Column Structure (A-M, 13 columns)

| Column | Field Name | Width | Data Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **A** | Evidence_ID | 14 | Text | - | Unique evidence identifier (e.g., "EV-CFG-001") |
| **B** | Source_Sheet | 20 | Dropdown | Config Baseline, Access Control, Network Security, Encryption, Deployment, Jurisdictional Risk | Which assessment sheet references this evidence? |
| **C** | Source_Row | 12 | Integer | - | Row number in source sheet (for traceability) |
| **D** | Service_Name | 28 | Text | - | Cloud service this evidence relates to |
| **E** | Configuration_Item | 30 | Text | - | Specific config item being evidenced |
| **F** | Evidence_Type | 22 | Dropdown | Screenshot, Config Export, Scan Report, Certificate, Policy Document, Meeting Notes, Other | Type of evidence file |
| **G** | File_Location | 40 | Text | - | Full path to evidence file (file share, SharePoint, S3, etc.) |
| **H** | File_Format | 14 | Dropdown | PNG, JPG, PDF, JSON, YAML, XML, CSV, TXT, DOCX, Other | File format |
| **I** | Collection_Date | 16 | Date | - | Date evidence was collected/created |
| **J** | Collected_By | 22 | Text | - | Person who collected the evidence |
| **K** | Retention_Until | 16 | Date | Formula: `=I+2555` (7 years) | Evidence retention expiration date (7 years from collection) |
| **L** | Verification_Status | 18 | Dropdown | Verified, Pending Verification, Invalid, Missing | Evidence quality status |
| **M** | Notes | 35 | Text | - | Additional context or special handling instructions |

### 12.3 Data Validation Rules

```python
# Source Sheet (Column B)
source_sheet_dv = DataValidation(
    type="list",
    formula1='"Config Baseline,Access Control,Network Security,Encryption,Deployment,Jurisdictional Risk"',
    allow_blank=False
)
ws.add_data_validation(source_sheet_dv)
source_sheet_dv.add("B5:B100")  # Extended to row 100 for evidence volume

# Evidence Type (Column F)
evidence_type_dv = DataValidation(
    type="list",
    formula1='"Screenshot,Config Export,Scan Report,Certificate,Policy Document,Meeting Notes,Other"',
    allow_blank=False
)
ws.add_data_validation(evidence_type_dv)
evidence_type_dv.add("F5:F100")

# File Format (Column H)
file_format_dv = DataValidation(
    type="list",
    formula1='"PNG,JPG,PDF,JSON,YAML,XML,CSV,TXT,DOCX,Other"',
    allow_blank=False
)
ws.add_data_validation(file_format_dv)
file_format_dv.add("H5:H100")

# Verification Status (Column L)
verification_status_dv = DataValidation(
    type="list",
    formula1='"Verified,Pending Verification,Invalid,Missing"',
    allow_blank=False
)
ws.add_data_validation(verification_status_dv)
verification_status_dv.add("L5:L100")
```

### 12.4 Section Headers

```
Row 1 (merged A1:M1):
  "EVIDENCE REGISTER - SECURE CONFIGURATION ASSESSMENT
   Centralized Evidence Tracking for Audit Trail"

Row 2 (merged A2:M2):
  "Purpose: Track all evidence files referenced in assessment sheets with 
   metadata for audit trail and lifecycle management"
```

### 12.5 Automated Evidence ID Generation

**Formula in Column A (Evidence_ID):**

```excel
# Cell A5 (first evidence row)
=IF(B5<>"",CONCATENATE("EV-CFG-",TEXT(ROW()-4,"000")),"")

# This generates:
# Row 5: EV-CFG-001
# Row 6: EV-CFG-002
# etc.
```

### 12.6 Retention Date Auto-Calculation

**Formula in Column K (Retention_Until):**

```excel
# Cell K5 (7 years retention from collection date)
=IF(I5<>"",I5+2555,"")

# 2555 days ≈ 7 years (365 * 7 = 2555)
# Complies with ISO 27001 evidence retention requirements
```

### 12.7 Example Data Rows

**Row 5 (Evidence Example 1 - Screenshot):**

| Col | Value | Notes |
|-----|-------|-------|
| A | EV-CFG-001 | Auto-generated |
| B | Access Control | Source sheet |
| C | 7 | Row 7 in Access Control sheet |
| D | AWS Production Account | Service |
| E | IAM - MFA Enforced for Console Access | Config item |
| F | Config Export | Evidence type |
| G | `s3://isms-evidence/A.5.23.3/AWS/IAM_MFA_Policy.json` | File location |
| H | JSON | File format |
| I | 15.01.2026 | Collection date |
| J | John Doe, Cloud Ops | Collected by |
| K | 15.01.2033 | Retention until (7 years) |
| L | Verified | Verification status |
| M | Exported via AWS CLI on 15.01.2026 | Notes |

**Row 6 (Evidence Example 2 - Screenshot):**

| Col | Value | Notes |
|-----|-------|-------|
| A | EV-CFG-002 | Auto-generated |
| B | Encryption | Source sheet |
| C | 12 | Row 12 in Encryption sheet |
| D | Azure SQL Database - Production | Service |
| E | TDE (Transparent Data Encryption) Enabled | Config item |
| F | Screenshot | Evidence type |
| G | `\\fileserver\ISMS\Evidence\A.5.23.3\AzureSQL\TDE_Enabled.png` | File location |
| H | PNG | File format |
| I | 18.01.2026 | Collection date |
| J | Jane Smith, DBA Team | Collected by |
| K | 18.01.2033 | Retention until (7 years) |
| L | Verified | Verification status |
| M | Screenshot from Azure Portal | Notes |

### 12.8 Conditional Formatting (Verification Status)

**Color coding for Column L (Verification_Status):**

```python
from openpyxl.styles import PatternFill

# Verified - Green
verified_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")

# Pending Verification - Yellow
pending_fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")

# Invalid - Orange
invalid_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")

# Missing - Red
missing_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")

# Apply to Column L (rows 5-100)
for row in range(5, 101):
    cell = ws.cell(row=row, column=12)  # Column L
    if cell.value == "Verified":
        cell.fill = verified_fill
    elif cell.value == "Pending Verification":
        cell.fill = pending_fill
    elif cell.value == "Invalid":
        cell.fill = invalid_fill
    elif cell.value == "Missing":
        cell.fill = missing_fill
```

### 12.9 Integration Points

**Data Sources (populated from):**
- Sheet 2 (Configuration Baseline): Column J (Evidence_Location) → Evidence Register
- Sheet 3 (Access Control): Column J → Evidence Register
- Sheet 4 (Network Security): Column J → Evidence Register
- Sheet 5 (Encryption): Column J → Evidence Register
- Sheet 6 (Deployment): Column J → Evidence Register
- Sheet 7 (Jurisdictional Risk): Column S (Evidence_ID) → Evidence Register

**Data Consumers:**
- Auditors: Use this register to locate evidence files for verification
- ISMS Coordinator: Monitor verification status and retention compliance
- Compliance Team: Track evidence lifecycle

**Population Method:**
- **Manual:** Coordinator extracts evidence locations from Sheets 2-7 and populates register
- **Automated (Python):** Consolidation script scans Sheets 2-7, extracts evidence locations, auto-populates register
- **Hybrid:** Python script creates skeleton, coordinator verifies/enriches metadata

---

## 13. Sheet 10: Approval Sign-Off

### 13.1 Purpose & Layout

**Sheet Name:** `10. Approval Sign-Of`  
**Note:** Intentional typo in sheet name (matches Python script line 68) - keep for consistency

**Purpose:** Sequential 4-stage approval workflow for secure configuration assessment before implementation or remediation.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 5.10 (Assessment Approval)

**Layout:** Form-style with 4 sequential approval sections

### 13.2 Approval Workflow (Sequential)

```
┌────────────────────────────────────────────────────────────────┐
│              ASSESSMENT COMPLETION                             │
│            (Coordinator/Assessor)                              │
└──────────────────────┬─────────────────────────────────────────┘
                       │
                       ▼
              ┌────────────────────┐
              │  1. IT OPERATIONS  │
              │  Technical Review  │
              └─────────┬──────────┘
                        │
                        ▼
              ┌────────────────────┐
              │   2. SECURITY      │
              │  Controls Review   │
              └─────────┬──────────┘
                        │
                        ▼
              ┌────────────────────┐
              │     3. DPO         │
              │  Data Protection   │
              └─────────┬──────────┘
                        │
                        ▼
              ┌────────────────────┐
              │    4. CISO         │
              │  Final Approval    │
              └─────────┬──────────┘
                        │
                        ▼
              ┌────────────────────┐
              │   APPROVED FOR     │
              │  IMPLEMENTATION    │
              └────────────────────┘
```

### 13.3 Sheet Structure (Sections)

**Section 1: IT OPERATIONS REVIEW** (Rows 3-10)

| Row | Field | Input Type | Validation |
|-----|-------|------------|------------|
| 4 | Reviewed By (IT Ops) | Text input | - |
| 5 | Review Date | Date input | - |
| 6 | Configuration Accuracy | Dropdown | Verified, Issues Found |
| 7 | Technical Feasibility | Dropdown | Feasible, Requires Clarification, Not Feasible |
| 8 | IT Ops Comments | Text input (multi-line) | - |

**Section 2: SECURITY TEAM REVIEW** (Rows 12-19)

| Row | Field | Input Type | Validation |
|-----|-------|------------|------------|
| 13 | Reviewed By (Security) | Text input | - |
| 14 | Review Date | Date input | - |
| 15 | Security Posture | Dropdown | Compliant, Gaps Identified, Non-Compliant |
| 16 | Risk Level | Dropdown | Low, Medium, High, Critical |
| 17 | Security Comments | Text input (multi-line) | - |

**Section 3: DPO REVIEW** (Rows 21-28)

| Row | Field | Input Type | Validation |
|-----|-------|------------|------------|
| 22 | Reviewed By (DPO) | Text input | - |
| 23 | Review Date | Date input | - |
| 24 | Data Protection Compliance | Dropdown | Compliant, Partially Compliant, Non-Compliant |
| 25 | Cross-Border Transfer Status | Dropdown | Approved, Approved with SCCs, Requires TIA, Rejected |
| 26 | DPO Comments | Text input (multi-line) | - |

**Section 4: CISO APPROVAL** (Rows 30-37)

| Row | Field | Input Type | Validation |
|-----|-------|------------|------------|
| 31 | Approved By (CISO) | Text input | - |
| 32 | Approval Date | Date input | - |
| 33 | Approval Decision | Dropdown | Approved, Approved with Conditions, Rejected |
| 34 | Conditions (if applicable) | Text input (multi-line) | - |
| 35 | Executive Comments | Text input (multi-line) | - |

**Section 5: NEXT REVIEW DETAILS** (Rows 39-44)

| Row | Field | Input Type | Validation |
|-----|-------|------------|------------|
| 40 | Next Review Date | Date input | Formula: `=B32+90` (90 days from CISO approval) |
| 41 | Review Responsible | Text input | - |
| 42 | Special Considerations | Text input (multi-line) | - |

### 13.4 Data Validation Rules

```python
# IT Ops - Configuration Accuracy (Row 6, Column B)
config_accuracy_dv = DataValidation(
    type="list",
    formula1='"Verified,Issues Found"',
    allow_blank=False
)
ws.add_data_validation(config_accuracy_dv)
config_accuracy_dv.add("B6")

# IT Ops - Technical Feasibility (Row 7, Column B)
technical_feasibility_dv = DataValidation(
    type="list",
    formula1='"Feasible,Requires Clarification,Not Feasible"',
    allow_blank=False
)
ws.add_data_validation(technical_feasibility_dv)
technical_feasibility_dv.add("B7")

# Security - Security Posture (Row 15, Column B)
security_posture_dv = DataValidation(
    type="list",
    formula1='"Compliant,Gaps Identified,Non-Compliant"',
    allow_blank=False
)
ws.add_data_validation(security_posture_dv)
security_posture_dv.add("B15")

# Security - Risk Level (Row 16, Column B)
risk_level_dv = DataValidation(
    type="list",
    formula1='"Low,Medium,High,Critical"',
    allow_blank=False
)
ws.add_data_validation(risk_level_dv)
risk_level_dv.add("B16")

# DPO - Data Protection Compliance (Row 24, Column B)
dpo_compliance_dv = DataValidation(
    type="list",
    formula1='"Compliant,Partially Compliant,Non-Compliant"',
    allow_blank=False
)
ws.add_data_validation(dpo_compliance_dv)
dpo_compliance_dv.add("B24")

# DPO - Cross-Border Transfer Status (Row 25, Column B)
dpo_transfer_dv = DataValidation(
    type="list",
    formula1='"Approved,Approved with SCCs,Requires TIA,Rejected"',
    allow_blank=False
)
ws.add_data_validation(dpo_transfer_dv)
dpo_transfer_dv.add("B25")

# CISO - Approval Decision (Row 33, Column B)
ciso_decision_dv = DataValidation(
    type="list",
    formula1='"Approved,Approved with Conditions,Rejected"',
    allow_blank=False
)
ws.add_data_validation(ciso_decision_dv)
ciso_decision_dv.add("B33")
```

### 13.5 Auto-Calculated Next Review Date

**Formula in Row 40, Column B:**

```excel
# Cell B40 - Next Review Date (90 days after CISO approval)
=IF(B32<>"",B32+90,"")

# If CISO Approval Date (B32) is populated, add 90 days (quarterly review cycle)
# Otherwise, leave blank
```

### 13.6 Cell Styling

**Section Headers:**
- Rows 3, 12, 21, 30, 39
- Font: Calibri 11, Bold, White
- Fill: Medium Blue (4472C4)
- Merged cells: A:E (spans 5 columns)

**Field Labels:**
- Column A
- Font: Calibri 10, Bold, Black
- Fill: None (white)

**Input Fields:**
- Column B:E (merged for multi-line inputs)
- Font: Calibri 10, Normal, Black
- Fill: Light Yellow (FFFFCC) for editable fields
- Alignment: Left, Wrap Text

**Dropdowns:**
- Same styling as text input fields
- Light Yellow background indicates user interaction needed

### 13.7 Example Approval Flow

**Scenario: Microsoft 365 Configuration Assessment Approved**

| Section | Field | Value |
|---------|-------|-------|
| **IT Operations** | Reviewed By | John Doe, Senior Cloud Engineer |
|  | Review Date | 18.01.2026 |
|  | Configuration Accuracy | Verified |
|  | Technical Feasibility | Feasible |
|  | Comments | Config baseline matches CIS Microsoft 365 v2.0.0. All technical items verified. |
| **Security** | Reviewed By | Jane Smith, Security Analyst |
|  | Review Date | 19.01.2026 |
|  | Security Posture | Gaps Identified |
|  | Risk Level | Medium |
|  | Comments | MFA enforced for admins only. Recommend extending to all users. Otherwise compliant. |
| **DPO** | Reviewed By | Dr. Maria Weber, Data Protection Officer |
|  | Review Date | 20.01.2026 |
|  | Data Protection Compliance | Compliant |
|  | Cross-Border Transfer Status | Approved with SCCs |
|  | Comments | EU Data Boundary enabled. SCCs in place. Residual risk acceptable. |
| **CISO** | Approved By | Alex Johnson, CISO |
|  | Approval Date | 20.01.2026 |
|  | Approval Decision | Approved with Conditions |
|  | Conditions | Extend MFA to all users by 28.02.2026 |
|  | Executive Comments | Configuration assessment approved. MFA remediation required within 30 days. |
| **Next Review** | Next Review Date | 20.04.2026 (auto-calculated: 20.01.2026 + 90 days) |
|  | Review Responsible | Cloud Operations Team |
|  | Special Considerations | Focus on MFA enforcement validation in Q2 review |

### 13.8 Integration Points

**Data Sources:**
- This is a **terminal sheet** (no imports from other sheets)
- Populated entirely by approvers during review workflow

**Data Consumers:**
- ISMS Coordinator: Monitor approval workflow progress
- Auditors: Verify approval chain completeness
- Risk Register: If "Approved with Conditions" → create risk entry

**Workflow Trigger:**
- Assessment completion in Sheets 2-7 → Coordinator submits for approval
- Approval completion → Assessment ready for implementation

---

## 14. Cross-Sheet Integration Points

### 14.1 Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                      DATA FLOW OVERVIEW                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  EXTERNAL INPUT (IMP-5.23.1 Inventory)                          │
│         │                                                        │
│         │ Service Name, Vendor, Criticality, Data Class         │
│         ▼                                                        │
│  ┌───────────────────────────────────────────────────────┐      │
│  │  Sheets 2-6: Configuration Assessment                 │      │
│  │  (Base columns A-Q populated from inventory)          │      │
│  │  (Extended columns R-X/AA: user input)                │      │
│  └──────────┬────────────────────────────────────────────┘      │
│             │                                                    │
│             │ Evidence Locations (Column J)                     │
│             │ Config Status (Column I)                          │
│             │                                                    │
│             ├──────────────────────────────┐                    │
│             │                              │                    │
│             ▼                              ▼                    │
│  ┌──────────────────────┐      ┌──────────────────────┐        │
│  │  Sheet 7:            │      │  Sheet 9:            │        │
│  │  Jurisdictional Risk │      │  Evidence Register   │        │
│  │  (US CLOUD Act)      │      │  (Centralized)       │        │
│  └──────────┬───────────┘      └──────────────────────┘        │
│             │                                                    │
│             │ Risk Level (Column N)                             │
│             │                                                    │
│             ▼                                                    │
│  ┌─────────────────────────────────────────────────────┐        │
│  │  Sheet 8: Summary Dashboard                         │        │
│  │  - Table 1: Compliance by Area (from Sheets 2-6)    │        │
│  │  - Table 2: Top 5 Gaps (from Sheets 2-6)            │        │
│  │  - Table 3: Jurisdictional Risk (from Sheet 7)      │        │
│  │  - Table 4: Regulatory Compliance (from Sheets 2,7) │        │
│  └─────────────────────────────────────────────────────┘        │
│             │                                                    │
│             │ Dashboard Output (Executive Summary)              │
│             │                                                    │
│             ▼                                                    │
│  ┌─────────────────────────────────────────────────────┐        │
│  │  Sheet 10: Approval Sign-Off                        │        │
│  │  4-stage approval: IT Ops → Security → DPO → CISO   │        │
│  └─────────────────────────────────────────────────────┘        │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 14.2 Import Mapping (IMP-5.23.1 → IMP-5.23.3)

**Required Imports from IMP-5.23.1 (Inventory):**

| Target Sheet | Target Column | Source Sheet (IMP-5.23.1) | Source Column | Notes |
|--------------|---------------|---------------------------|---------------|-------|
| Sheets 2-6 | B (Service Name) | Sheet 2 (Service Inventory) | B | Copy all active services |
| Sheets 2-6 | C (Vendor) | Sheet 2 (Service Inventory) | C | Vendor name |
| Sheets 2-6 | F (Criticality) | Sheet 4 (Service Criticality) | E | Business criticality |
| Sheets 2-6 | G (Data Class) | Sheet 3 (Data Classification) | F | Highest data class |
| Sheet 7 | B (Service Name) | Sheet 2 (Service Inventory) | B | Only US-nexus providers |
| Sheet 7 | C (Vendor) | Sheet 2 (Service Inventory) | C | Only US-nexus providers |

**Import Method:**
- **Manual:** Copy-paste from IMP-5.23.1 (prone to errors, not recommended)
- **Excel Formula (VLOOKUP):** Link cells dynamically (breaks if source workbook moved)
- **Python Script (Recommended):** Pre-populate from IMP-5.23.1 during workbook generation

**Python Pre-Population Example:**

```python
# In generator script, after creating base structure:
# Read IMP-5.23.1 (assuming it's in same directory)

import openpyxl

inventory_wb = openpyxl.load_workbook("ISMS-IMP-A.5.23.S1.xlsx", data_only=True)
inventory_ws = inventory_wb["2. Service Inventory"]

# Extract services (rows 5-30)
services = []
for row in range(5, 31):
    service_name = inventory_ws.cell(row=row, column=2).value  # Column B
    vendor_name = inventory_ws.cell(row=row, column=3).value   # Column C
    if service_name:  # Only if service exists
        services.append((service_name, vendor_name))

# Populate Sheets 2-6 with service data
for sheet_name in ["2. Configuration Baseline", "3. Access Control Setup", 
                   "4. Network Security", "5. Encryption Configuration", 
                   "6. Deployment Checklist"]:
    ws = wb[sheet_name]
    for idx, (service, vendor) in enumerate(services, start=5):
        ws.cell(row=idx, column=2, value=service)  # Column B
        ws.cell(row=idx, column=3, value=vendor)   # Column C
```

### 14.3 Export Mapping (IMP-5.23.3 → Dashboard Consolidation)

**Dashboard Consolidation Script (Python):**

```python
# File: consolidate_reg_a523_dashboard.py
# Purpose: Aggregate all 5 assessment workbooks into master dashboard

import openpyxl
from datetime import datetime

def consolidate_dashboards():
    """Consolidate 5 assessment workbooks into master dashboard."""
    
    # Load all 5 workbooks
    workbooks = {
        "Inventory": openpyxl.load_workbook("ISMS-IMP-A.5.23.S1.xlsx", data_only=True),
        "Vendor DD": openpyxl.load_workbook("ISMS-IMP-A.5.23.S2.xlsx", data_only=True),
        "Config": openpyxl.load_workbook("ISMS-IMP-A.5.23.S3.xlsx", data_only=True),
        "Governance": openpyxl.load_workbook("ISMS-IMP-A.5.23.S4.xlsx", data_only=True),
        "Compliance": openpyxl.load_workbook("ISMS-IMP-A.5.23.S5.xlsx", data_only=True),
    }
    
    # Extract data from each workbook's dashboard
    # For IMP-5.23.3, extract from Sheet 8 (Summary Dashboard)
    config_dashboard = workbooks["Config"]["8. Summary Dashboard"]
    
    # Extract Table 1: Compliance by Area
    config_compliance = {
        "Config Baseline": config_dashboard["G5"].value,  # Compliance %
        "Access Control": config_dashboard["G6"].value,
        "Network Security": config_dashboard["G7"].value,
        "Encryption": config_dashboard["G8"].value,
        "Deployment": config_dashboard["G9"].value,
        "Overall": config_dashboard["G10"].value,
    }
    
    # Create consolidated master dashboard workbook
    master_wb = openpyxl.Workbook()
    master_ws = master_wb.active
    master_ws.title = "Master Dashboard"
    
    # ... (consolidation logic)
    
    # Save master dashboard
    master_wb.save(f"ISMS_Master_Dashboard_{datetime.now().strftime('%Y%m%d')}.xlsx")
    print("✅ Master dashboard consolidated successfully!")

if __name__ == "__main__":
    consolidate_dashboards()
```

---

## 15. Workbook-Level Specifications

### 15.1 File Naming Convention

**Generated Filename Format:**

```
ISMS-IMP-A.5.23.S3_SecureConfig_YYYYMMDD.xlsx

Examples:
- ISMS-IMP-A.5.23.S3_SecureConfig_20260120.xlsx (generated 20 Jan 2026)
- ISMS-IMP-A.5.23.S3_SecureConfig_20260415.xlsx (generated 15 Apr 2026)
```

**Normalized Filename (for dashboard linking):**

```
ISMS-IMP-A.5.23.S3.xlsx

(No date suffix - used by consolidation scripts)
```

### 15.2 Workbook Properties (Metadata)

**Set via `openpyxl.workbook.properties`:**

```python
wb.properties.title = "ISMS-IMP-A.5.23.S3 - Secure Configuration & Deployment"
wb.properties.subject = "ISO/IEC 27001:2022 Control A.5.23 Assessment"
wb.properties.creator = "ISMS Implementation Team"
wb.properties.description = "Cloud services secure configuration assessment workbook"
wb.properties.keywords = "ISMS, ISO 27001, Cloud Security, Configuration Management, DORA, NIS2, CLOUD Act"
wb.properties.category = "Information Security Management System"
wb.properties.version = "2.0"
```

### 15.3 Sheet Protection

**Enable sheet protection for formula sheets:**

```python
# Protect sheets with formulas (allow users to select/edit unlocked cells only)
for sheet_name in ["2. Configuration Baseline", "3. Access Control Setup", 
                   "4. Network Security", "5. Encryption Configuration",
                   "6. Deployment Checklist", "7. Jurisdictional Risk"]:
    ws = wb[sheet_name]
    ws.protection.sheet = True
    ws.protection.password = None  # No password (allow unprotect)
    ws.protection.selectLockedCells = True
    ws.protection.selectUnlockedCells = True
    ws.protection.formatCells = False
    ws.protection.insertRows = False
    ws.protection.deleteRows = False
```

**Lock formula cells (Column A - Assessment_ID):**

```python
# In each assessment sheet (Sheets 2-7)
for row in range(5, 31):
    ws.cell(row=row, column=1).protection = Protection(locked=True)
```

### 15.4 Print Settings

**Configure print layout for assessment sheets:**

```python
from openpyxl.worksheet.page import PageMargins, PrintPageSetup

# For Sheets 2-7 (assessment sheets)
for sheet_name in ["2. Configuration Baseline", "3. Access Control Setup", 
                   "4. Network Security", "5. Encryption Configuration",
                   "6. Deployment Checklist", "7. Jurisdictional Risk"]:
    ws = wb[sheet_name]
    
    # Page setup
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0  # Auto-height
    
    # Margins
    ws.page_margins = PageMargins(left=0.5, right=0.5, top=0.75, bottom=0.75, header=0.3, footer=0.3)
    
    # Print titles (repeat header row on every page)
    ws.print_title_rows = '1:4'  # Rows 1-4 (headers)
    
    # Print area (exclude checklist if desired)
    # ws.print_area = 'A1:X30'  # Uncomment to exclude checklist
```

### 15.5 Freeze Panes

**Set freeze panes for all assessment sheets:**

```python
# Sheets 2-7: Freeze row 5 (headers visible when scrolling data)
for sheet_name in ["2. Configuration Baseline", "3. Access Control Setup", 
                   "4. Network Security", "5. Encryption Configuration",
                   "6. Deployment Checklist", "7. Jurisdictional Risk"]:
    ws = wb[sheet_name]
    ws.freeze_panes = "A5"  # Freeze rows 1-4
```

### 15.6 Workbook Size Optimization

**Expected file size:**
- **Empty workbook** (generated): ~150-200 KB
- **Partially filled** (10-20 services): ~300-500 KB
- **Fully populated** (26 services + evidence): ~800 KB - 1.5 MB

**Optimization tips:**
- Embed screenshots as links (Column J) rather than inline images
- Use data validation (dropdowns) to reduce cell content size
- Avoid excessive conditional formatting (limit to Status/Risk columns)

---

## 16. Quality Assurance Checklist

### 16.1 Generator Script Validation

**Before releasing generated workbook, verify:**

- [ ] All 10 sheets present with correct names
- [ ] All dropdowns functional (test 3-5 dropdowns per sheet)
- [ ] Formulas calculate correctly (Assessment_ID, Retention_Until, Dashboard metrics)
- [ ] No shared style objects (run `style_object_checker.py`)
- [ ] UTF-8 symbols render correctly (✅ ⚠️ ❌)
- [ ] Column widths appropriate (no truncated text)
- [ ] Sheet protection enabled (formula cells locked)
- [ ] Print layout configured (landscape, fit-to-width)
- [ ] Freeze panes set correctly (row 5 frozen on Sheets 2-7)
- [ ] Workbook properties populated (title, version, etc.)

### 16.2 Data Validation Testing

**Test all dropdowns with edge cases:**

| Sheet | Column | Dropdown | Test Case | Expected Result |
|-------|--------|----------|-----------|-----------------|
| 2 | D | Service_Type | Select "SaaS" | ✅ Accepted |
| 2 | I | Status | Select "✅ Compliant" | ✅ Symbol renders |
| 3 | S | MFA_Enforced | Select "All Users" | ✅ Accepted |
| 7 | F | CLOUD_Act_Exposure | Select "Direct (US Company)" | ✅ Accepted |
| 10 | 33 | Approval_Decision | Select "Approved with Conditions" | ✅ Accepted |

### 16.3 Formula Validation

**Verify formulas produce correct results:**

| Sheet | Cell | Formula | Test Input | Expected Output |
|-------|------|---------|------------|-----------------|
| 2 | A5 | Assessment_ID | (Row 5) | CFG-001 |
| 2 | A6 | Assessment_ID | (Row 6) | CFG-002 |
| 9 | K5 | Retention_Until | Collection Date: 01.01.2026 | 01.01.2033 (7 years) |
| 10 | B40 | Next_Review_Date | CISO Approval: 20.01.2026 | 20.04.2026 (90 days) |
| 8 | G5 | Compliance % | Compliant: 20, Total: 26 | 77% |

### 16.4 Dashboard Formula Validation

**Test dashboard calculations:**

**Scenario:** Populate Sheet 2 with test data:
- Row 5: Status = "✅ Compliant"
- Row 6: Status = "✅ Compliant"
- Row 7: Status = "⚠️ Partial"
- Row 8: Status = "❌ Non-Compliant"
- Rows 9-30: Empty

**Expected Dashboard Results (Sheet 8):**

| Cell | Description | Expected Value |
|------|-------------|----------------|
| B5 | Total Items (Config Baseline) | 4 |
| C5 | Compliant Count | 2 |
| D5 | Partial Count | 1 |
| E5 | Non-Compliant Count | 1 |
| F5 | N/A Count | 0 |
| G5 | Compliance % | 50% (2/4 * 100) |

### 16.5 Integration Test

**End-to-End Test Scenario:**

1. **Generate workbook**: `python3 generate_reg_a523_3_secure_config.py`
2. **Open in Excel**: Verify no repair warnings
3. **Populate test data**: Add 3 services in Sheet 2
4. **Check dashboard**: Verify metrics update correctly
5. **Add evidence**: Populate Evidence Register (Sheet 9)
6. **Complete approval**: Fill Sheet 10 with test approvals
7. **Save workbook**: Close and reopen to verify data persistence

### 16.6 Accessibility & Usability

**User Experience Validation:**

- [ ] Instructions sheet clear and concise
- [ ] Dropdown options intuitive (no cryptic abbreviations)
- [ ] Color coding visible for color-blind users (use symbols + colors)
- [ ] Column headers descriptive (no need to guess meaning)
- [ ] Example rows helpful (provide context)
- [ ] Checklist items actionable (user knows what to do)

---

**END OF SECTION 4**

**END OF PART II: TECHNICAL SPECIFICATION**
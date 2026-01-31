# ISMS-POL-A.8.31 – Separation of Development, Test and Production Environments

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Separation of Development, Test and Production Environments |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.31 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / IT Operations / DevOps Lead | Initial consolidated policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager / DevOps Lead
- Compliance Review: Legal/Compliance Officer
- Final Authority: Executive Management (CEO)

**Related Documents**:
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.31-S1 (Environment Architecture Implementation)
- ISMS-IMP-A.8.31-S2 (Environment Access Control Implementation)
- ISMS-IMP-A.8.31-S3 (Environment Separation Assessment & Dashboard)
- ISMS-REF-A.8.31-Environment-Architecture-Patterns
- ISMS-REF-A.8.31-CICD-Pipeline-Integration
- ISMS-POL-A.8.25-26-29 (Secure Development Framework)
- ISMS-POL-A.8.32 (Change Management)
- ISMS-POL-A.5.15-16-18 (Identity and Access Management)
- ISO/IEC 27001:2022 Control A.8.31

---

## Executive Summary

This policy establishes [Organization]'s requirements for separating development, test, and production environments to reduce risks associated with unauthorized changes and data exposure in accordance with ISO/IEC 27001:2022 Control A.8.31.

**Scope**: This policy applies to all information systems and applications operated by [Organization], regardless of technology platform or deployment model.

**Purpose**: Define organizational requirements for environment separation control implementation and governance. This policy establishes WHAT environment separation is required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.31.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including ISO/IEC 27001:2022, Swiss FADP, EU GDPR, and sector-specific requirements (FINMA, DORA, NIS2) where applicable.

**Core Principle**: **Production environments must be protected from development/testing activities. Production data must never be used in development/testing environments.**

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.31

**ISO/IEC 27001:2022 Annex A.8.31 - Separation of Development, Test and Production Environments**

> *Development, test and production environments shall be separated and secured.*

**Control Objective**: Reduce risks associated with unauthorized changes to production systems and exposure of production data in less secure environments.

**Control Category**: Technical control (preventive and detective)

**Implementation Approach**: This control requires both **technical separation** (network, infrastructure, data) and **procedural controls** (access management, promotion workflows, approval gates).

The ISO 27001:2022 control recognizes that environment separation addresses multiple risk vectors:

**Unauthorized Production Changes**:
- Developers accidentally modifying production systems
- Untested code deployed to production
- Configuration changes bypassing change management

**Production Data Exposure**:
- Customer data copied to development/test environments
- Sensitive data accessible in less secure environments
- Data protection regulation violations

**Inadequate Testing**:
- Testing conducted in production (risking data corruption)
- Insufficient pre-production validation
- Production incidents from untested changes

**Access Control Gaps**:
- Excessive developer access to production
- Shared credentials across environments
- Insufficient audit trails for production access

### 1.2 What This Policy Does

This policy:
- **Defines** environment separation requirements based on organizational risk assessment
- **Establishes** governance framework for environment management
- **Specifies** accountability for environment separation implementation
- **References** applicable regulatory requirements per ISMS-POL-00

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation details** (see ISMS-IMP-A.8.31 Implementation Guides)
- **Define specific cloud architectures or tools** (see ISMS-REF-A.8.31 Reference Documents)
- **Provide CI/CD pipeline configurations** (see ISMS-REF-A.8.31-CICD-Pipeline-Integration)
- **Select technologies or vendors** (technology selection based on [Organization]'s risk assessment)
- **Replace risk assessment** (environment separation controls selected based on risk treatment)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving technology landscape
- Technical agility for infrastructure updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)

### 1.4 Risk Management Context

Environment separation serves as a **fundamental preventive control** within the organization's layered security architecture. It is not a standalone solution but works in concert with:

**Related Controls**:
- **A.8.25-26-29 (Secure Development)**: Environment separation supports the SDLC by providing isolated spaces for each development phase
- **A.8.32 (Change Management)**: Promotion between environments follows formal change control processes
- **A.5.15-16-18 (Identity and Access Management)**: Each environment has distinct access controls aligned with least privilege
- **A.8.2-3-5 (Authentication and PAM)**: Production access requires privileged access management
- **A.8.4 (Source Code Access)**: Code repositories separated by environment sensitivity

**Defense in Depth**:

Environment separation is most effective when combined with:
- Strong access controls (IAM, PAM, MFA)
- Automated deployment pipelines (CI/CD)
- Infrastructure as Code (IaC) for configuration consistency
- Monitoring and alerting for cross-environment access attempts
- Data classification and protection controls
- Regular security assessments and penetration testing

**Risk Treatment Strategy**:

This control **reduces likelihood** of security incidents by:
- Preventing accidental production changes through technical barriers
- Limiting production data exposure through data isolation
- Enforcing testing before production deployment
- Restricting production access to authorized operations personnel

The organization recognizes that **absolute separation is impractical** in some scenarios (shared infrastructure, resource constraints, legacy systems). Where complete separation is not feasible, **compensating controls** must be documented and approved by the CISO.

### 1.5 Scope

#### 1.5.1 In Scope - Environments Covered

This policy framework applies to **all information systems and applications** operated by [Organization], specifically:

**Environment Types (Minimum Required)**:

1. **Development Environment**:
   - **Purpose**: Active code development, experimentation, feature building
   - **Infrastructure**: Developer workstations, dev servers, dev databases, dev cloud accounts
   - **Data Allowed**: Synthetic test data, anonymized data ONLY. NO production data.
   - **Access**: Developers (full access), DevOps engineers (deployment), Operations (monitoring only)
   - **Network**: Isolated from production. May connect to test environment.
   - **Availability Target**: Best effort (downtime acceptable for maintenance)
   - **Change Control**: Minimal (developer discretion within project scope)

2. **Testing/QA Environment**:
   - **Purpose**: Quality assurance, integration testing, user acceptance testing (UAT)
   - **Infrastructure**: Test servers, QA databases, test cloud accounts, UAT environments
   - **Data Allowed**: Synthetic test data or anonymized production data ONLY. NO real production data.
   - **Access**: QA team (full testing access), Developers (limited/read-only), Business users (UAT only)
   - **Network**: Isolated from production. May connect to development and staging.
   - **Availability Target**: 95% during business hours
   - **Change Control**: Moderate (test plan required, QA approval)

3. **Staging/Pre-Production Environment**:
   - **Purpose**: Final validation before production deployment, production-like testing
   - **Infrastructure**: Mirrors production configuration (servers, databases, load balancers)
   - **Data Allowed**: Synthetic data or carefully anonymized production data ONLY.
   - **Access**: Operations team (full access), Senior developers (read-only), QA (limited testing)
   - **Network**: Isolated from production. No direct connectivity.
   - **Availability Target**: Matches production SLA during testing windows
   - **Change Control**: High (mirrors production change control)

4. **Production Environment**:
   - **Purpose**: Live business operations serving customers/users
   - **Infrastructure**: Production servers, production databases, customer-facing systems
   - **Data Allowed**: Real production data ONLY (customer data, business data).
   - **Access**: Operations team ONLY. Developers access ONLY via break-glass emergency procedures.
   - **Network**: Maximum isolation. DMZ, firewall rules, network segmentation.
   - **Availability Target**: Per SLA (typically 99.5%+)
   - **Change Control**: Maximum (formal change management, CAB approval required)

**Additional Environments (Organization-Specific)**:

Organizations may define additional environments based on complexity:
- **Sandbox**: Isolated experimentation (no connectivity to other environments)
- **Performance Testing**: Load/stress testing environment
- **Disaster Recovery**: Production replica for business continuity
- **Training**: User training environment (separate from production)

**Technology Scope**:

This policy applies to **all system types** regardless of technology:
- Traditional on-premises servers (Windows, Linux, Unix)
- Virtual machines (VMware, Hyper-V, KVM)
- Cloud infrastructure (AWS, Azure, GCP, Oracle Cloud, IBM Cloud)
- Container platforms (Docker, Kubernetes, OpenShift)
- Serverless/Function-as-a-Service (AWS Lambda, Azure Functions)
- Platform-as-a-Service (Heroku, Cloud Foundry)
- Database systems (relational, NoSQL, data warehouses)
- Web applications (internal and customer-facing)
- Mobile applications (iOS, Android, backend services)
- Integration platforms (API gateways, ESB, iPaaS)
- Data analytics platforms (BI tools, data lakes, ML platforms)

**Network Scope**:

Environment separation applies to systems across:
- On-premises data centers
- Colocation facilities
- Cloud providers (public, private, hybrid)
- Remote/distributed infrastructure
- Edge computing locations

#### 1.5.2 Out of Scope

This policy does NOT apply to:
- **Single-user research environments** (isolated from organizational network)
- **Proof-of-concept systems** (non-production, temporary, no real data)
- **Vendor demonstration systems** (vendor-managed, no organizational data)
- **Personal development laptops** (not connected to organizational environments)

However, once research/PoC systems transition to organizational use, they MUST comply with this policy.

### 1.6 Regulatory Framework

This section references the organization's **ISMS-POL-00 - Regulatory Applicability Framework** for detailed compliance context. The following summary highlights key regulatory drivers for environment separation:

#### 1.6.1 Mandatory Compliance (Tier 1)

**ISO/IEC 27001:2022 - Control A.8.31**:
- **Requirement**: Development, test and production environments shall be separated and secured
- **Applicability**: All organizations with ISO 27001 certification or commitment
- **Evidence Required**:
  - Environment architecture documentation
  - Access control matrices per environment
  - Promotion workflow documentation
  - Regular compliance assessments

**Swiss Federal Data Protection Act (FADP/nDSG)**:
- **Requirement**: Article 8 - Appropriate technical and organizational measures
- **Applicability**: All operations in or serving Switzerland
- **Relevance**: Using production data (personal data) in development/test environments violates data minimization and purpose limitation principles
- **Evidence Required**: Data handling procedures showing no production personal data in dev/test

**EU General Data Protection Regulation (GDPR)**:
- **Requirement**: Article 32 - Security of processing (appropriate technical measures)
- **Applicability**: Where processing EU personal data
- **Relevance**: Using production personal data in less secure dev/test environments violates security requirements
- **Evidence Required**: Data protection impact assessment, technical measures documentation

#### 1.6.2 Conditional Compliance (Tier 2)

**FINMA Circular 2023/1 - Operational Risks and Resilience (Switzerland Financial Institutions)**:
- **Applicability**: Swiss-regulated financial institutions (banks, insurance, securities dealers)
- **Requirement**: Margin 50-62 - Environment separation for operational resilience
- **Specific Requirement**: "Production systems shall be protected from development and testing activities through appropriate separation measures"
- **Evidence Required**:
  - Environment segregation documentation
  - Change management integration with environment promotion
  - Incident management procedures per environment

**DORA - Digital Operational Resilience Act (EU Financial Entities)**:
- **Applicability**: EU financial entities (banks, investment firms, insurance, payment institutions)
- **Requirement**: Article 9 - ICT risk management framework includes environment separation
- **Specific Requirement**: "Financial entities shall ensure proper separation of development, testing and production environments to minimize the risk of unauthorized changes or data breaches"
- **Evidence Required**:
  - ICT risk management documentation
  - Testing policies (no production data usage)
  - Third-party service provider environment separation verification

**NIS2 Directive (EU Essential and Important Entities)**:
- **Applicability**: Essential and important entities across EU (energy, transport, health, digital infrastructure, etc.)
- **Requirement**: Article 21(2) - Security measures including environment separation
- **Specific Requirement**: Technical and organizational measures to manage risks to security, including separation of environments to prevent unauthorized access
- **Evidence Required**:
  - Risk assessment including environment separation
  - Security measures documentation
  - Incident reporting procedures per environment

#### 1.6.3 Informational Reference (Tier 3 - Best Practices)

**NIST Special Publication 800-53 Rev. 5**:
- CM-7: Least Functionality - includes environment separation to limit functionality
- SA-11: Developer Testing and Evaluation - testing in non-production environments
- Not mandatory unless specifically required by US federal contracts

**OWASP Secure Coding Practices**:
- Recommendation: Separate development, testing, and production environments
- Best practice guidance for secure SDLC

**Center for Internet Security (CIS) Controls**:
- Control 16: Application Software Security - includes environment separation
- Voluntary best practice framework

**For complete regulatory categorization, refer to ISMS-POL-00.**

---

## 2. Environment Separation Requirements Framework

### 2.1 Environment Architecture Requirements

[Organization] **SHALL** implement the following architecture requirements to separate environments:

#### 2.1.1 Minimum Environment Tiers

Organizations **SHALL** maintain at minimum the following environment tiers for all systems in scope:

**Mandatory Tiers**: Development, Testing/QA, Production (minimum 3 tiers)

**Recommended**: Development, Testing/QA, Staging, Production (4 tiers)

Each environment tier **SHALL** have:
- Clear purpose statement
- Defined infrastructure resources
- Explicit data handling restrictions
- Documented access controls
- Network isolation mechanisms

#### 2.1.2 Environment Naming and Identification

[Organization] **SHALL** implement consistent environment naming to prevent confusion:

**Naming Standards**:
- Environment names clearly distinguish environment type (e.g., "dev-", "test-", "prod-")
- Hostnames, DNS records, cloud account names include environment identifier
- Application URLs include environment subdomain (dev.app.example.com, test.app.example.com, app.example.com)
- Database names include environment prefix (dev_database, test_database, prod_database)

**Visual Identification** (STRONGLY RECOMMENDED):
- Different color schemes per environment in admin interfaces (e.g., production = red banner)
- Warning banners in production systems ("PRODUCTION ENVIRONMENT - Changes affect live users")
- Browser extensions or profiles for environment identification

#### 2.1.3 Network Separation Requirements

[Organization] **SHALL** implement network segmentation to isolate environments:

**Network Isolation Mechanisms** (choose appropriate to infrastructure):

**On-Premises / Data Center**:
- Separate VLANs per environment tier
- Routing policies restrict inter-environment communication
- Firewall rules between environments (default deny)
- Physical network separation for highly sensitive systems (optional)

**Cloud Infrastructure**:
- Separate Virtual Private Clouds (VPCs) per environment (AWS)
- Separate Virtual Networks (VNets) per environment (Azure)
- Separate VPC networks per environment (GCP)
- VPC peering disabled between non-adjacent environments (dev ↔ prod direct connection PROHIBITED)

**Kubernetes / Container Platforms**:
- Separate namespaces per environment (minimum)
- Separate clusters per environment (recommended for production)
- Network policies enforce pod-to-pod isolation
- Service mesh segmentation (Istio, Linkerd) for fine-grained control

**Firewall Rules Between Environments**:

[Organization] **SHALL** implement firewall rules enforcing:
- **Default Deny**: All inter-environment traffic blocked unless explicitly allowed
- **Controlled Paths**: Promotion flows (dev → test → staging → prod) through deployment pipelines only
- **No Reverse Flows**: Production cannot initiate connections to dev/test
- **Logging**: All inter-environment connection attempts logged

**Audit Verification Criteria**:
- ✅ Network diagrams show environment segmentation
- ✅ Firewall rules documented and reviewed quarterly
- ✅ Penetration testing confirms network isolation
- ✅ No direct network connectivity from dev/test to production

#### 2.1.4 Infrastructure Separation Requirements

[Organization] **SHALL** implement infrastructure separation:

**Separate Infrastructure Resources** (at minimum):

**Compute**:
- Separate servers, virtual machines, or containers per environment
- No shared compute resources between production and non-production

**Storage**:
- Separate storage volumes, databases, object storage per environment
- No shared databases between production and non-production

**Cloud Accounts/Subscriptions**:
- Separate AWS accounts per environment (recommended: AWS Organizations structure)
- Separate Azure subscriptions per environment (recommended: Management Groups)
- Separate GCP projects per environment (recommended: Folder hierarchy)

**Why Separate Cloud Accounts**:
- Prevents accidental cross-environment access (IAM policies enforce)
- Separate billing (cost attribution per environment)
- Blast radius containment (dev environment compromise doesn't affect prod)
- Clear audit boundaries (CloudTrail, Azure Monitor logs per environment)

**Kubernetes / Containers**:
- Separate namespaces per environment (minimum)
- Separate clusters per environment (strongly recommended for production)
- Resource quotas prevent resource exhaustion attacks

**Audit Verification Criteria**:
- ✅ Infrastructure inventory shows separate resources per environment
- ✅ Cloud account/subscription structure documented
- ✅ No shared infrastructure components between prod and non-prod

#### 2.1.5 Credential Separation Requirements

[Organization] **SHALL** implement credential separation:

**Separate Credentials Per Environment**:
- Database passwords unique per environment
- API keys unique per environment
- Service account credentials unique per environment
- Cloud provider credentials (AWS keys, Azure service principals, GCP service accounts) unique per environment

**Production Credential Protection**:
- Production credentials stored in Privileged Access Management (PAM) vault
- Production credentials NEVER stored in code repositories or configuration files
- Production credentials rotated per organizational password policy (minimum: annually, recommended: quarterly)
- Production credentials require break-glass approval for developer access

**Development/Test Credentials**:
- Dev/test credentials may be less restrictive for operational efficiency
- Dev/test credentials MUST NOT work in production (separate accounts, separate systems)

**Audit Verification Criteria**:
- ✅ Credential inventory shows unique credentials per environment
- ✅ Production credentials stored in PAM vault
- ✅ No shared credentials between production and non-production

#### 2.1.6 Configuration Management and Drift Detection

[Organization] **SHALL** manage environment configuration:

**Infrastructure as Code (IaC)**:
- Environment configurations defined as code (Terraform, CloudFormation, ARM templates)
- Configuration version controlled (Git)
- Environment-specific configuration files (dev.tfvars, staging.tfvars, prod.tfvars)

**Configuration Consistency**:
- Staging environment configuration mirrors production (validates production changes)
- Configuration drift detection (manual quarterly review minimum, automated preferred)
- Configuration changes follow change management process

**Audit Verification Criteria**:
- ✅ IaC configurations documented and version controlled
- ✅ Staging mirrors production configuration
- ✅ Configuration drift monitoring in place

### 2.2 Environment Access Control Requirements

[Organization] **SHALL** implement the following access control requirements:

**Core Principle**: **Production access is restricted to operations personnel ONLY. Developers access production ONLY via break-glass emergency procedures.**

#### 2.2.1 Role-Based Access Control (RBAC) Per Environment

[Organization] **SHALL** implement RBAC aligned with least privilege:

**Development Environment Access**:
- **Developers**: Full access (create, read, update, delete)
- **DevOps Engineers**: Full access (infrastructure, deployments)
- **Operations Team**: Limited access (monitoring, support)
- **QA Team**: Read-only access (may read dev environment for early testing)

**Testing/QA Environment Access**:
- **QA Team**: Full testing access (execute tests, validate features)
- **Developers**: Limited access (deploy from dev, read logs, no direct system modification)
- **Business Users (UAT)**: Application access only (no infrastructure access)
- **Operations Team**: Limited access (monitoring, support)

**Staging/Pre-Production Environment Access**:
- **Operations Team**: Full access (deployment, configuration, troubleshooting)
- **Senior Developers**: Read-only access (validate before production, no write access)
- **QA Team**: Limited testing access (final validation)
- **Developers**: No access (except emergency with approval)

**Production Environment Access**:
- **Operations Team**: Full access via PAM (deploy, configure, troubleshoot)
- **Security Team**: Read-only access (monitoring, incident response, forensics)
- **Developers**: **NO ACCESS** (except break-glass emergency with CISO/Incident Commander approval)
- **Business Users**: Application access only (no infrastructure access)

**Audit Verification Criteria**:
- ✅ User-environment access matrix documented
- ✅ ZERO developers with standing production access
- ✅ Access reviews conducted quarterly
- ✅ Access granted per documented approval process

#### 2.2.2 Production Access Restrictions

[Organization] **SHALL** enforce production access restrictions:

**Developer Production Access Policy**:
- Developers **SHALL NOT** have standing access to production infrastructure
- Developers **SHALL NOT** have production database credentials
- Developers **SHALL NOT** have production cloud console access
- Developers **SHALL NOT** have production SSH/RDP access

**Why No Developer Production Access**:
- **Risk Reduction**: Prevents accidental production changes
- **Least Privilege**: Developers don't need production access for normal duties
- **Separation of Duties**: Development and operations are distinct functions
- **Compliance**: Required by many regulations (SOX, FINMA, DORA)
- **Audit Trail**: Operations access logged, controlled, auditable

**Production Access Channels** (Operations Team):
- Privileged Access Management (PAM) system (CyberArk, BeyondTrust, Thycotic)
- Just-in-Time (JIT) access provisioning (time-limited sessions)
- Multi-Factor Authentication (MFA) required for all production access
- Session recording (operations actions recorded for audit)

**Audit Verification Criteria**:
- ✅ Developer production access count = ZERO (except active break-glass)
- ✅ PAM system deployed and used for production access
- ✅ MFA enabled for all production accounts (100%)
- ✅ Production access sessions recorded

#### 2.2.3 Break-Glass Emergency Access Procedures

[Organization] **SHALL** implement break-glass procedures for emergency developer production access:

**When Break-Glass is Permitted**:
- **Severity 1 Production Incident**: Complete service outage, data loss, security breach
- **Operations Team Unable to Resolve**: Issue requires specialized developer knowledge
- **Customer Impact**: Significant customer/business impact if not resolved immediately
- **No Alternative**: Issue cannot be resolved through remote troubleshooting

**Break-Glass Approval Process**:

1. **Incident Declared**: Incident Commander declares Severity 1 incident
2. **Request Submitted**: Developer requests production access (incident ticket)
3. **Approval Required**: Incident Commander + CISO (or delegate) approve
4. **Time-Limited Access**: PAM vault provides time-limited credentials (4-8 hours maximum)
5. **Session Recorded**: All actions logged and session recorded
6. **Post-Incident Review (PIR)**: Mandatory review within 24 hours of incident resolution

**Break-Glass Access Restrictions**:
- Access is **time-limited** (expires automatically after session)
- Access is **purpose-limited** (only for specific incident resolution)
- Access is **logged and monitored** (SIEM alerts, SOC monitoring)
- Access requires **post-incident review** (PIR mandatory)

**Post-Incident Review (PIR) Requirements**:
- What was the incident and why was production access needed?
- Was break-glass access appropriate? (could it have been avoided?)
- What did the developer do in production? (session recording review)
- How can we prevent future need for break-glass? (runbook creation, tooling improvement)
- Lessons learned (update procedures, training)

**Audit Verification Criteria**:
- ✅ Break-glass procedure documented
- ✅ All break-glass activations approved and logged (<10 per year target)
- ✅ 100% of break-glass sessions have completed PIRs
- ✅ Break-glass usage trending down (improving maturity)

#### 2.2.4 Access Review and Recertification

[Organization] **SHALL** conduct periodic access reviews:

**Access Review Frequency**:
- **Production Environment**: Quarterly
- **Staging Environment**: Semi-annual
- **Development/Test Environments**: Annual

**Access Review Process**:
1. IAM system generates user-environment access report
2. Environment owners review access lists
3. Remove access for users no longer requiring it (role change, departure)
4. Document review results (who reviewed, date, changes made)
5. CISO or delegate approves review results

**Automated Access Revocation**:
- Terminated employees: Access revoked within 24 hours (HR → IAM integration)
- Role changes: Access reviewed within 30 days of role change
- Dormant accounts: Access revoked after 90 days of inactivity

**Audit Verification Criteria**:
- ✅ Access reviews completed per schedule (100%)
- ✅ Review results documented and approved
- ✅ Orphaned accounts removed (zero accounts without owner)

#### 2.2.5 Multi-Factor Authentication (MFA) Requirements

[Organization] **SHALL** enforce MFA:

**MFA Requirements by Environment**:
- **Production**: MFA **REQUIRED** for all access (100% enforcement)
- **Staging**: MFA **REQUIRED** for privileged access
- **Testing/QA**: MFA **RECOMMENDED** for privileged access
- **Development**: MFA **RECOMMENDED** (risk-based decision)

**MFA Methods** (in order of preference):
1. Hardware security keys (YubiKey, Titan Key) - strongest
2. Time-based One-Time Password (TOTP) apps (Google Authenticator, Microsoft Authenticator)
3. Push notifications (Duo, Okta Verify)
4. SMS-based OTP (weakest, avoid if possible due to SIM swapping attacks)

**Audit Verification Criteria**:
- ✅ Production MFA enforcement = 100%
- ✅ MFA method documented per user
- ✅ SMS-based MFA phased out for production access

### 2.3 Data Handling Requirements

[Organization] **SHALL** implement the following data handling requirements:

**Core Principle**: **PRODUCTION DATA SHALL NEVER BE USED IN DEVELOPMENT OR TESTING** (unless properly anonymized per this policy).

#### 2.3.1 Production Data Prohibition in Non-Production

[Organization] **SHALL** enforce:

**Absolute Prohibitions**:
- Production databases **SHALL NOT** be copied to development/test environments
- Production database dumps **SHALL NOT** be restored in development/test
- Production backup files **SHALL NOT** be used for development/test
- Production API credentials **SHALL NOT** be used in development/test
- Production configuration files **SHALL NOT** be committed to dev/test repositories

**Why This Matters**:
- **Data Protection Compliance**: Using production personal data in dev/test violates GDPR, FADP
- **Security Risk**: Dev/test environments have weaker security controls
- **Insider Threat**: Developers with production data access increases risk
- **Regulatory Fines**: GDPR violations can result in fines up to 4% of annual revenue

**Common Violations to Avoid**:
- "We need real data to test properly" → Use anonymized data or synthetic data
- "It's faster to copy production" → Fast but illegal and insecure
- "We'll be careful" → Not sufficient for compliance
- "We'll delete it after" → Violation occurred at time of copy

**Audit Verification Criteria**:
- ✅ Production data in dev/test = ZERO (automated scans quarterly)
- ✅ Data handling procedures documented
- ✅ Developer training on data handling completed (100%)
- ✅ No production database connection strings in dev/test code

#### 2.3.2 Approved Data Types for Non-Production Environments

[Organization] **SHALL** use only approved data types in non-production:

**Development Environment**:
- **Synthetic data** (generated, not derived from production): Preferred
- **Anonymized data** (irreversible, DPO-approved): Permitted with approval
- **Publicly available data**: Permitted
- **Test fixtures** (hard-coded test data): Permitted

**Testing/QA Environment**:
- **Synthetic data**: Preferred
- **Anonymized data** (irreversible, DPO-approved): Permitted with approval
- **Publicly available data**: Permitted

**Staging/Pre-Production Environment**:
- **Synthetic data**: Preferred
- **Anonymized data** (irreversible, DPO-approved, production-like volume): Permitted with approval
- **Note**: Staging tests production-like load, not production data content

**Data Generation Methods**:
- **Faker libraries** (Python Faker, JavaScript Faker) - generate realistic fake data
- **Data synthesis tools** (Gretel.ai, SDV) - generate statistically similar data
- **Manual test data creation** - developers create test scenarios

**Audit Verification Criteria**:
- ✅ Data sources documented per environment
- ✅ Synthetic data generation tools in use
- ✅ No production data derivatives without DPO approval

#### 2.3.3 Data Anonymization Requirements

**When Anonymization is Permitted**:
- Business justification exists (synthetic data insufficient for testing)
- Data Protection Officer (DPO) approves anonymization approach
- Anonymization is **irreversible** (not pseudonymization or encryption)
- Re-identification risk assessed and acceptable

**Anonymization vs. Pseudonymization vs. Encryption**:

| Method | Reversible? | Allowed in Dev/Test? | Example |
|--------|-------------|----------------------|---------|
| **Anonymization** | No (irreversible) | ✅ **YES** (with DPO approval) | "John Smith, 42, Zurich" → "Person A, Age 40-49, Switzerland" |
| **Pseudonymization** | Yes (with lookup) | ❌ **NO** (still personal data) | "John Smith" → "ID-12345" (with lookup table) |
| **Encryption** | Yes (with key) | ❌ **NO** (still personal data) | "John Smith" → encrypted (can be decrypted) |

**For detailed anonymization techniques, see Annex A: Data Anonymization Decision Framework.**

**Audit Verification Criteria**:
- ✅ All anonymization requests have DPO approval
- ✅ Anonymization techniques documented
- ✅ Re-identification testing performed and passed
- ✅ Anonymized data deleted after use (30-day retention max)

#### 2.3.4 Data Classification Per Environment

[Organization] **SHALL** apply data classification per environment:

| Environment | Allowed Data Classifications | Prohibited |
|-------------|----------------------------|------------|
| **Development** | Public, Internal (synthetic), Internal (anonymized with DPO approval) | Confidential, Restricted, Real Customer Data |
| **Testing/QA** | Public, Internal (synthetic), Internal (anonymized with DPO approval) | Confidential, Restricted, Real Customer Data |
| **Staging** | Public, Internal (synthetic), Internal (anonymized with DPO approval) | Confidential, Restricted, Real Customer Data |
| **Production** | All classifications (Public, Internal, Confidential, Restricted) | Synthetic test data (no test data in prod) |

**Audit Verification Criteria**:
- ✅ Data classification policy enforced
- ✅ Automated scanning detects Confidential/Restricted data in dev/test (quarterly)
- ✅ Violations remediated within 7 days

### 2.4 Environment Promotion Requirements

[Organization] **SHALL** implement controlled promotion between environments:

**Core Principle**: **Changes flow through environments in order (Dev → Test → Staging → Prod). Direct deployment to production is PROHIBITED.**

#### 2.4.1 Mandatory Promotion Path

[Organization] **SHALL** enforce:

**Standard Promotion Flow**:

```
Development → Testing → Staging → Production
    ↓            ↓         ↓          ↓
  (Auto)     (Auto/Semi)  (Manual)  (Manual + CAB)
```

**Promotion Path Requirements**:
- Changes **MUST** start in Development environment
- Changes **MUST** pass Testing before reaching Staging
- Changes **MUST** be validated in Staging before Production
- Direct deployment to Production is **PROHIBITED** (except emergency hot-fixes with CISO approval)

**Environment Skip Prohibition**:
- Cannot skip Testing (Dev → Staging directly) without documented exception
- Cannot skip Staging (Dev → Prod or Test → Prod directly) - STRICT PROHIBITION

**Why This Matters**:
- **Quality Assurance**: Each environment validates different aspects
- **Risk Reduction**: Staging validates production deployment before production
- **Rollback Capability**: Previous version available in staging if production fails

#### 2.4.2 Promotion Approval Requirements

[Organization] **SHALL** require approvals:

| Promotion Path | Approval Type | Who Approves | Additional Checks |
|----------------|---------------|--------------|-------------------|
| Dev → Test | Automatic | None (on successful build) | Unit tests pass |
| Test → Staging | Automatic | QA Lead (optional) | Integration tests pass |
| Staging → Production | **MANUAL** | Change Advisory Board (CAB) | All tests pass, CAB approval, deployment window |

**Production Deployment Gate**:
- Requires explicit approval from authorized personnel (operations team, change manager)
- Deployment only during approved change windows (not 24/7 deployment allowed)
- Rollback plan documented and available
- Smoke tests defined and ready for post-deployment validation

#### 2.4.3 CI/CD Pipeline Integration Principles

[Organization] **SHALL** integrate environment separation into deployment pipelines:

**Environment-Specific Pipelines**:
- Separate pipeline configurations per environment
- Environment validation before deployment (prevent wrong artifact → wrong environment)
- Secrets management (credentials separated per environment)

**Automated Deployment Principles** (implementation in ISMS-REF-A.8.31-CICD):
- Development deployments: Fully automated on git push
- Testing deployments: Automated with quality gates (tests must pass)
- Staging deployments: Semi-automated (trigger available, may require approval)
- Production deployments: Manual trigger + CAB approval required

**For detailed CI/CD pipeline configuration examples, see ISMS-REF-A.8.31-CICD-Pipeline-Integration.**

#### 2.4.4 Rollback Procedures

[Organization] **SHALL** maintain rollback capability:

**Rollback Requirements**:
- Previous version retained in staging (available for rollback)
- Rollback procedure documented per system
- Rollback tested periodically (DR exercises, quarterly)
- Rollback decision criteria defined (what constitutes rollback-worthy failure)

**Rollback Execution**:
- Operations team authorized to execute rollback
- Rollback does not require CAB approval (speed prioritized during incident)
- Rollback logged and post-incident review conducted

**Audit Verification Criteria**:
- ✅ Rollback procedures documented for critical systems (100%)
- ✅ Rollback tested in DR exercises (annual minimum)
- ✅ Rollback success rate >95% when executed

#### 2.4.5 Configuration Consistency

[Organization] **SHALL** maintain configuration consistency:

**Staging Mirrors Production**:
- Staging environment configuration identical to production (same versions, same parameters)
- Configuration drift between staging and production monitored
- Staging validates production deployment (if staging succeeds, production likely succeeds)

**Configuration Management**:
- Infrastructure as Code (IaC) used for environment configuration
- Environment-specific configuration files (dev.tfvars, staging.tfvars, prod.tfvars)
- Configuration version controlled (Git)
- Configuration changes follow same promotion path as code

**Audit Verification Criteria**:
- ✅ Staging configuration matches production
- ✅ Configuration drift detection in place
- ✅ IaC used for environment configuration

### 2.5 Production Support Requirements

[Organization] **SHALL** implement production support while maintaining environment separation:

**The Challenge**: Production issues require investigation, but developers should not have production access. Solution: Enable effective remote support without production access.

#### 2.5.1 Read-Only Monitoring Access

[Organization] **SHALL** provide read-only monitoring access:

**Permitted Monitoring Access**:
- **Operations Team**: Full monitoring access (metrics, logs, traces, dashboards)
- **Developers**: Limited monitoring access (application logs, metrics - NO system logs, NO sensitive data)
- **Security Team**: Full monitoring access (security events, audit logs)
- **Service Desk**: Dashboard access only (service status, basic metrics)

**Monitoring Tools**:
- Application Performance Monitoring (APM): New Relic, Datadog, Dynatrace - read-only dashboards
- Log aggregation (SIEM): Splunk, ELK, CloudWatch - query access with data masking
- Metrics/dashboards: Grafana, Prometheus - read-only viewing
- Distributed tracing: Jaeger, Zipkin - read-only trace viewing

**Data Sensitivity in Logs**:
- Personal data **REDACTED** from logs (email addresses, names, etc.)
- Credentials **NEVER** logged (passwords, API keys)
- Payment card data **NEVER** logged (PCI DSS requirement)

**Audit Verification Criteria**:
- ✅ Monitoring access documented per role
- ✅ Read-only access enforced (cannot modify logs/metrics)
- ✅ Sensitive data redacted from logs

#### 2.5.2 Remote Troubleshooting Without Production Access

[Organization] **SHALL** enable troubleshooting without production access:

**Remote Troubleshooting Methods**:

**1. Enhanced Logging and Monitoring**:
- Comprehensive application logging (capture errors, stack traces, context)
- Distributed tracing (trace requests across services)
- Error aggregation (Sentry, Rollbar - developers see application errors without system access)

**2. Synthetic Data Reproduction**:
- Reproduce issues in staging using sanitized production data
- Developers troubleshoot in staging (not production)
- Issue fixed in dev/test/staging, then promoted to production

**3. Screen Sharing and Remote Support**:
- Operations team shares screen with developer (read-only viewing)
- Developer guides operations team through troubleshooting steps
- Developer **DOES NOT** control operations team system
- Session recorded for audit

**4. Diagnostic Modes and Debug Logging**:
- Temporary debug logging enabled in production (specific module only)
- Debug logs automatically disabled after timeframe (4 hours)
- Debug logs sanitized (sensitive data removed before developer viewing)

**Audit Verification Criteria**:
- ✅ Troubleshooting procedures documented (no direct dev access required)
- ✅ Screen sharing sessions recorded
- ✅ Debug logging time-limited and sanitized

#### 2.5.3 Production Incident Response

[Organization] **SHALL** follow incident response procedures:

**Incident Response Tiers**:

**Tier 1 (Operations Team)**:
- Investigate using monitoring tools and logs
- Execute runbooks (documented troubleshooting procedures)
- Restart services, apply known fixes
- Escalate to Tier 2 if unresolved

**Tier 2 (Senior Operations + On-Call Developer - Remote)**:
- Operations shares screen, developer guides remotely
- Developer analyzes logs/metrics (read-only access)
- Developer proposes solutions (operations executes)
- Escalate to Tier 3 if developer access required

**Tier 3 (Emergency Break-Glass)**:
- Developer requires production access (cannot resolve remotely)
- Incident Commander + CISO approve break-glass
- Developer accesses production via PAM (time-limited)
- Session recorded, post-incident review mandatory

**Audit Verification Criteria**:
- ✅ Incident response procedures documented
- ✅ Tier 1/2 incidents resolved without developer production access (>80%)
- ✅ Tier 3 break-glass approved and documented

#### 2.5.4 Runbooks and Standard Operating Procedures

[Organization] **SHALL** maintain runbooks:

**Runbook Coverage**:
- Application restart procedures
- Log file analysis (where to find logs, how to interpret)
- Common error resolution (troubleshooting steps)
- Performance tuning (configuration changes for common issues)
- Health check procedures (validate system health)
- Rollback procedures (revert to previous version)
- Emergency contact list (who to call for specific issues)

**Runbook Maintenance**:
- Version controlled (Wiki, Git repository)
- Updated after incidents (lessons learned incorporated)
- Tested periodically (disaster recovery drills)
- Accessible to operations team 24/7 (online, offline copy)

**Runbook Security**:
- Runbooks **DO NOT** contain credentials (reference PAM vault instead)
- Runbooks accessible to operations team only (not developers)

**Audit Verification Criteria**:
- ✅ Runbooks documented for critical systems (100% coverage)
- ✅ Runbooks updated within 30 days of incidents
- ✅ No credentials in runbooks

#### 2.5.5 Continuous Improvement Metrics

[Organization] **SHALL** track production support metrics:

**Key Performance Indicators (KPIs)**:
- **Mean Time to Detect (MTTD)**: How quickly are issues detected? (target: <5 minutes)
- **Mean Time to Resolve (MTTR)**: How quickly are issues resolved? (target: <2 hours for Sev 1)
- **Break-Glass Usage Rate**: How often is developer production access needed? (target: <10/year, trending down)
- **Tier 1 Resolution Rate**: Percentage of incidents resolved by operations without escalation (target: >60%)
- **Remote Troubleshooting Effectiveness**: Incidents resolved remotely without production access (target: >80%)
- **Runbook Coverage**: Percentage of incident types with documented runbooks (target: >90%)

**Metrics Review**:
- Monthly operational review (operations manager + security team)
- Quarterly business review (present metrics to management)
- Annual trend analysis (year-over-year improvement)

**Audit Verification Criteria**:
- ✅ Production support metrics tracked
- ✅ Break-glass usage trending down
- ✅ Runbook coverage >90%

---

## 3. Assessment & Evidence Framework

[Organization] **SHALL** assess compliance with environment separation requirements:

### 3.1 Assessment Types and Frequency

[Organization] **SHALL** conduct multiple assessment types:

**1. Self-Assessment (Quarterly)**:
- **Who**: System owners, IT operations
- **Method**: Checklist-based (using ISMS-IMP-A.8.31 assessment workbooks)
- **Output**: Self-assessment report, gap analysis
- **Timeline**: Completed within first month of each quarter

**2. Independent Security Assessment (Semi-Annual)**:
- **Who**: Information Security team (independent from operations)
- **Method**: Technical testing (network scans, access reviews, configuration audits)
- **Output**: Security assessment report, findings and recommendations
- **Timeline**: Every 6 months

**3. Internal Audit (Annual)**:
- **Who**: Internal Audit team
- **Method**: Evidence review, interviews, technical testing
- **Output**: Internal audit report, compliance rating
- **Timeline**: Annually (aligned with ISO 27001 audit)

**4. External Audit (Annual)**:
- **Who**: External auditor (ISO 27001 certification body)
- **Method**: Evidence sampling, interviews, technical verification
- **Output**: ISO 27001 audit findings
- **Timeline**: Annual surveillance or recertification audit

**5. Continuous Monitoring (Ongoing)**:
- **Who**: Automated monitoring tools, Security Operations Center (SOC)
- **Method**: Automated scans, log analysis, anomaly detection
- **Output**: Continuous compliance dashboards, alerts for violations
- **Timeline**: 24/7 continuous monitoring

### 3.2 Assessment Scope and Coverage

[Organization] **SHALL** ensure comprehensive coverage:

**Systems In Scope**:
- All production systems (100% coverage mandatory)
- All staging systems (100% coverage mandatory)
- Sample of development/testing systems (minimum 25% coverage)
- High-risk systems (100% coverage - systems processing sensitive data)

**Assessment Areas**:
- Environment architecture (network, infrastructure, credentials)
- Environment access control (access provisioning, production restrictions, break-glass)
- Data handling (production data detection, anonymization effectiveness)
- Environment promotion (promotion path, deployment approval, rollback)
- Production support (break-glass usage, troubleshooting, runbooks)

### 3.3 Evidence Collection and Management

[Organization] **SHALL** collect and maintain evidence:

**Technical Evidence**:
- Network diagrams (environment architecture)
- Firewall rule exports (network separation)
- Cloud account/subscription configurations (infrastructure separation)
- Access control matrices (who has access to which environment)
- Deployment logs (promotion tracking)
- Monitoring dashboards (continuous compliance)

**Procedural Evidence**:
- Policy documents (this policy)
- Implementation guides (ISMS-IMP-A.8.31)
- Runbooks and SOPs
- Training records (completion rates)
- Access request approvals
- Change management approvals (CAB)

**Assessment Evidence**:
- Self-assessment reports
- Security assessment reports
- Internal audit reports
- External audit reports
- Penetration test reports
- Compliance dashboards

**Incident Evidence**:
- Incident reports
- Break-glass access logs
- Post-incident reviews (PIRs)
- Corrective action tracking

**Evidence Retention**:
- **Production evidence**: 3 years minimum (regulatory requirement)
- **Assessment reports**: 5 years (ISO 27001 certification lifecycle)
- **Incident evidence**: 5 years

### 3.4 Compliance Reporting

[Organization] **SHALL** maintain compliance dashboards:

**Dashboard Components**:
- Overall compliance score (percentage)
- Environments with proper separation (percentage)
- Developer production access count (should be ZERO)
- Production data in dev/test (incidents - should be ZERO)
- Break-glass usage (count - trending down)
- Promotion process adherence (percentage)

**Reporting Frequency**:
- **Quarterly**: CISO review, executive dashboard
- **Semi-Annual**: Board reporting
- **Annual**: ISO 27001 audit package

**For detailed assessment methodology and tools, see ISMS-IMP-A.8.31-S3.**

---

## 4. Roles, Governance & Compliance

### 4.1 Roles and Responsibilities

#### 4.1.1 Governance and Oversight

**Chief Information Security Officer (CISO)**:
- Policy owner and final approval authority
- Approves exceptions to environment separation requirements
- Reviews compliance assessment results quarterly
- Ensures integration with overall ISMS

**IT Operations Manager**:
- Responsible for production environment security
- Approves production access requests
- Manages PAM system for production credentials
- Reviews production access logs monthly

**Development Manager / DevOps Lead**:
- Responsible for development/test environment management
- Implements environment promotion workflows
- Ensures developers follow environment separation policies
- Coordinates with operations on staging environment

**Information Security Manager**:
- Conducts environment separation compliance assessments
- Reviews access control configurations
- Investigates policy violations
- Maintains this policy framework

#### 4.1.2 Operational Responsibilities

**System Owners**:
- Define environment architecture for their systems
- Document environment separation mechanisms
- Ensure compliance with this policy
- Report exceptions and compensating controls

**Developers**:
- Use only assigned development/test environments
- Never access production without break-glass approval
- Use synthetic/anonymized data in non-production
- Follow promotion workflows for code deployment

**QA Team**:
- Conduct testing in test/staging environments only
- Never test in production
- Validate environment separation controls during testing
- Report any production data in test environments

**Operations Team**:
- Exclusive production access (except break-glass)
- Manage production deployments via change control
- Monitor cross-environment access attempts
- Maintain PAM system for production

**Security Team**:
- Monitor environment access logs
- Investigate cross-environment access violations
- Conduct periodic environment separation assessments
- Provide guidance on compensating controls

### 4.2 Governance Procedures

#### 4.2.1 Policy Review and Maintenance

**Review Schedule**:
- **Annual review**: Policy content, regulatory updates, technology changes
- **Quarterly review**: Compliance assessment results, exception tracking
- **Ad-hoc review**: Major incidents, regulatory changes, platform changes

**Update Triggers**:
- New regulatory requirements (FINMA, DORA, NIS2)
- Major technology platform changes (cloud migration)
- Significant security incidents
- ISO 27001 audit findings
- SDLC or change management process changes

**Approval Process**:
1. Information Security Manager proposes updates
2. Technical review by IT Operations and DevOps
3. Compliance review by Legal/Compliance
4. CISO approval (final authority)
5. Communication to all stakeholders

#### 4.2.2 Exception Management

**Exception Criteria**:

Exceptions may be approved only for:
- Legacy systems scheduled for decommission within 12 months
- Technical limitations where separation not feasible (must document why)
- Business-critical systems where separation would cause severe operational impact
- Temporary exceptions during migration/transformation projects

**Exception Approval Process**:

1. **System Owner** documents:
   - System description and justification
   - Risk assessment (what risks accepted)
   - Compensating controls (how risks mitigated)
   - Remediation plan (how compliance will be achieved)
   - Exception duration (time-limited)

2. **Information Security Manager** reviews:
   - Validates justification
   - Assesses compensating controls adequacy
   - Recommends approval/denial

3. **CISO** approves or denies:
   - Final decision authority
   - Can impose additional compensating controls
   - Sets exception expiration date

4. **Exception Tracking**:
   - All exceptions tracked in risk register
   - Quarterly review of active exceptions
   - Automatic expiration (re-approval required)

**Compensating Controls Examples**:
- Enhanced access logging and monitoring
- Mandatory code review for all production changes
- Read-only production access (no write permissions)
- Data masking for all non-production data
- Increased change management rigor
- More frequent security assessments

### 4.3 Training and Awareness

**Policy Communication**:
- All stakeholders notified upon policy approval
- Policy published in organizational policy repository
- Annual awareness campaign (emails, town halls, training)

**Training Requirements**:

**Developers**:
- Environment separation policy overview
- Proper use of development/test environments
- Data handling requirements (no production data)
- Promotion workflows and approval processes

**Operations Team**:
- Production access control procedures
- PAM system usage
- Break-glass access procedures
- Incident response per environment

**QA Team**:
- Testing in appropriate environments
- Test data management
- UAT access procedures

**Management**:
- Business impact of environment separation
- Risk context and compliance requirements
- Exception approval responsibilities

**Training Frequency**:
- New hire onboarding (within first 30 days)
- Annual refresher training
- Role-specific training upon policy updates

### 4.4 Continuous Improvement

**Metrics and KPIs**:
- Overall compliance score
- Break-glass usage rate (trending down)
- Production incidents from environment violations
- Time to remediate gaps
- Training completion rate

**Review and Improvement**:
- Quarterly metrics review
- Annual trend analysis
- Lessons learned from incidents
- Feedback mechanisms (surveys, interviews)

---

## 5. Implementation & References

### 5.1 Related ISMS Documents

**Foundation Documents**:
- **ISMS-POL-00**: Regulatory Applicability Framework
- **ISMS-POL-A.8.25-26-29**: Secure Development Framework
- **ISMS-POL-A.8.32**: Change Management
- **ISMS-POL-A.5.15-16-18**: Identity and Access Management
- **ISMS-POL-A.8.2-3-5**: Authentication and Privileged Access Management

### 5.2 Implementation Guides

**Architecture Implementation**:
- **ISMS-IMP-A.8.31-S1**: Environment Architecture Implementation & Assessment
  - Network separation implementation
  - Infrastructure separation (cloud accounts, Kubernetes)
  - Configuration management

**Access Control Implementation**:
- **ISMS-IMP-A.8.31-S2**: Environment Access Control Implementation
  - RBAC configuration per environment
  - PAM system integration
  - Break-glass procedures

**Assessment and Dashboard**:
- **ISMS-IMP-A.8.31-S3**: Environment Separation Assessment & Compliance Dashboard
  - Assessment workbook generation (Python scripts)
  - Compliance scoring methodology
  - Executive dashboard

### 5.3 Reference Documents

**Architecture Patterns**:
- **ISMS-REF-A.8.31-Environment-Architecture-Patterns**
  - AWS multi-account architecture
  - Azure subscription patterns
  - Kubernetes namespace/cluster separation
  - On-premises VLAN architecture

**CI/CD Integration**:
- **ISMS-REF-A.8.31-CICD-Pipeline-Integration**
  - Jenkins pipeline examples
  - GitLab CI configuration
  - GitHub Actions workflows
  - Terraform environment patterns

### 5.4 External Standards and Frameworks

**ISO/IEC 27001:2022**:
- Control A.8.31: Separation of Development, Test and Production Environments
- Control A.8.32: Change Management (promotion workflows)

**NIST SP 800-53 Rev. 5**:
- CM-7: Least Functionality
- SA-11: Developer Testing and Evaluation

**OWASP**:
- Secure Coding Practices
- SAMM (Software Assurance Maturity Model) - Operations stream

---

## 6. Definitions

**Anonymization**: Irreversible process of removing or obscuring personal data such that individuals cannot be re-identified. Anonymized data is no longer considered personal data under GDPR/FADP.

**Break-Glass Access**: Emergency access procedure allowing developers temporary production access during Severity 1 incidents when operations team cannot resolve the issue.

**Environment**: A distinct set of infrastructure resources (servers, databases, networks) serving a specific purpose in the SDLC (development, testing, staging, production).

**Infrastructure as Code (IaC)**: Practice of managing infrastructure configuration as code files (Terraform, CloudFormation) that are version controlled and deployed automatically.

**Privileged Access Management (PAM)**: System for managing, monitoring, and securing privileged credentials (production passwords, root access, admin accounts).

**Production Environment**: Live operational environment serving real users/customers with real business data.

**Promotion**: Process of moving code, configuration, or infrastructure changes from one environment to another (e.g., dev → test → staging → prod).

**Pseudonymization**: Reversible process of replacing personal identifiers with pseudonyms. Pseudonymized data is still personal data under GDPR/FADP.

**Staging Environment**: Pre-production environment that mirrors production configuration for final validation before production deployment.

**Synthetic Data**: Artificially generated data that mimics production data characteristics but contains no real personal information.

---

## Annex A: Data Anonymization Decision Framework

### A.1 Purpose

This annex provides the **operational decision framework** for data anonymization when production-like data is required for development or testing. This annex is **critical operational guidance** that system owners and the Data Protection Officer (DPO) must reference when making data handling decisions.

**Scope**: Process for requesting, approving, and implementing data anonymization when synthetic data is insufficient.

**Key Principle**: Anonymization must be **irreversible** - individuals cannot be re-identified from anonymized data.

### A.2 When Anonymization is Required vs. Synthetic Data

**Decision Tree**:

```
1. Can you use synthetic data (generated, not from production)?
   ├─ YES → Use synthetic data (preferred, no DPO approval needed)
   └─ NO → Proceed to Step 2

2. Why is production-derived data needed?
   ├─ "We need realistic data patterns" → Try statistical synthesis first
   ├─ "We need production-like volume" → Use synthetic data at scale
   ├─ "We need actual business scenarios" → Consider anonymization
   └─ "We need to debug production issue" → Reproduce in staging

3. Can the issue be reproduced without production data?
   ├─ YES → Reproduce in staging with anonymized/synthetic data
   └─ NO → Proceed to anonymization request (DPO approval)

4. DPO Approval Required for Anonymization Request
```

**When Synthetic Data is Sufficient** (no anonymization needed):
- Unit testing (hard-coded test fixtures)
- Integration testing (generated test data)
- Performance testing (generated high-volume data)
- UI/UX testing (realistic but generated)

**When Anonymization May Be Justified** (DPO approval required):
- Complex data relationships (referential integrity testing)
- Statistical analysis (need production data distributions)
- Machine learning model training (need production patterns)
- Migration testing (need production data structure)

### A.3 Anonymization vs. Pseudonymization vs. Encryption

**Critical Legal Distinction**:

| Method | Reversible? | Personal Data? | Allowed in Dev/Test? | GDPR/FADP Compliance |
|--------|-------------|----------------|----------------------|---------------------|
| **Anonymization** | ❌ No (irreversible) | ❌ No (not personal data) | ✅ **YES** (with DPO approval) | Compliant (no longer personal data) |
| **Pseudonymization** | ✅ Yes (with lookup table) | ✅ Yes (still personal data) | ❌ **NO** | Non-compliant (still requires GDPR protections) |
| **Encryption** | ✅ Yes (with decryption key) | ✅ Yes (still personal data) | ❌ **NO** | Non-compliant (encrypted data is personal data) |

**Examples**:

**Anonymization** (Allowed):
- Original: "John Smith, 42 years old, lives in Zurich, earns CHF 120,000/year"
- Anonymized: "Person in age group 40-49, Central Switzerland, income bracket CHF 100,000-150,000"
- Cannot reverse to identify John Smith → No longer personal data

**Pseudonymization** (NOT Allowed):
- Original: "John Smith"
- Pseudonymized: "ID-12345" (with lookup table: ID-12345 = John Smith)
- Can reverse with lookup table → Still personal data → NOT allowed in dev/test

**Encryption** (NOT Allowed):
- Original: "John Smith"
- Encrypted: "Xf8k2Jm..." (with encryption key stored separately)
- Can decrypt with key → Still personal data → NOT allowed in dev/test

### A.4 DPO Approval Checklist

Before using production-derived data in dev/test, DPO verifies:

☐ **Business Justification**: Legitimate reason why synthetic data insufficient  
☐ **Anonymization Technique**: Appropriate technique selected (see A.5)  
☐ **Irreversibility**: Anonymization cannot be reversed (no lookup tables, no keys)  
☐ **Re-identification Risk**: K-anonymity assessment performed (k ≥ 3 minimum)  
☐ **Re-identification Testing**: Manual attempts to re-identify failed  
☐ **Data Minimization**: Only necessary data fields anonymized and used  
☐ **Retention Limitation**: Anonymized data will be deleted after use (30-day max)  
☐ **Access Controls**: Anonymized data treated as confidential (not public)  
☐ **Legal Review**: Cross-border transfer or contractual implications reviewed (if applicable)  
☐ **Documentation**: Anonymization process documented for audit  

**DPO Signature**: ________________ **Date**: ________

### A.5 Anonymization Techniques

[Organization] may use the following anonymization techniques (DPO selects appropriate technique based on data type and use case):

#### A.5.1 Data Masking

**Full Masking**: Replace entire value with fixed mask
- Example: "John Smith" → "XXXXX XXXXX"
- Use case: Complete obscurity, no utility needed

**Partial Masking**: Mask part of value, preserve format
- Example: "john.smith@example.com" → "j***.s*****@example.com"
- Use case: Format validation testing

**Format-Preserving Masking**: Replace with realistic value maintaining format
- Example: Credit card "4532-1234-5678-9010" → "4539-8765-4321-0987"
- Use case: Payment testing without real cards

#### A.5.2 Tokenization

**Consistent Tokenization**: Same value always maps to same token
- Example: Customer "CUST-12345" → Token "TKN-A7B9C2" (consistent across tables)
- Use case: Referential integrity testing (foreign keys work)

**One-Way Tokenization**: Cannot reverse token to original
- No lookup table stored
- Use case: De-identification for analytics

#### A.5.3 Generalization

**Reduce Precision**: Make data less specific
- Age: "42 years" → "40-49 years"
- Location: "Sursee, Lucerne" → "Central Switzerland"
- Date: "2024-03-15" → "March 2024"
- Salary: "CHF 125,000" → "CHF 100,000-150,000"

**Use case**: Statistical analysis while protecting individuals

#### A.5.4 Synthetic Data Replacement

**Generate New Data**: Replace with statistically similar generated data
- Maintain data distributions (ages follow same distribution)
- Preserve relationships (customers still have orders)
- Example: Replace all names with generated names, keep purchase patterns

**Use case**: Machine learning, analytics, testing

#### A.5.5 Data Subsetting

**Extract Small Sample**: Use 1-5% of production records
- Smaller dataset = lower risk
- Still anonymize the subset
- Example: 10,000 customers → Sample 500, then anonymize

**Use case**: Reduce data volume for testing

### A.6 Anonymization Effectiveness Verification

#### A.6.1 K-Anonymity Assessment

**K-Anonymity**: Each record indistinguishable from at least k-1 other records

**Example** (k=3):

Original data:
| Name | Age | Postal Code | Disease |
|------|-----|-------------|---------|
| Alice | 42 | 6210 | Diabetes |
| Bob | 43 | 6210 | Heart Disease |
| Charlie | 44 | 6210 | Diabetes |

Anonymized (k=3):
| Name | Age | Postal Code | Disease |
|------|-----|-------------|---------|
| * | 40-49 | 6210 | Diabetes |
| * | 40-49 | 6210 | Heart Disease |
| * | 40-49 | 6210 | Diabetes |

Each person indistinguishable from at least 2 others (k=3).

**Minimum K-Value**: k ≥ 3 (lower risk), k ≥ 5 (higher risk data)

#### A.6.2 Re-identification Testing

**Process**:
1. Attempt to re-identify individuals from anonymized dataset
2. Use publicly available information (LinkedIn, company website, social media)
3. Document re-identification attempts and results
4. If re-identification successful → Strengthen anonymization

**Example Test**:
- Anonymized: "Manager, Age 40-49, Central Switzerland, Joined 2010"
- Public LinkedIn search: Find matching profile
- Result: If unique match found → Re-identification possible → Need stronger anonymization

### A.7 Anonymization Workflow

**End-to-End Process**:

```
1. REQUEST
   Developer requests production-derived data for testing
   ↓
2. BUSINESS JUSTIFICATION
   Developer documents why synthetic data insufficient
   ↓
3. DPO REVIEW
   DPO reviews request and proposes anonymization approach
   ↓
4. EXTRACTION
   Operations extracts subset of production data (1-5% sample)
   ↓
5. ANONYMIZATION
   Automated anonymization pipeline applies approved techniques
   ↓
6. VALIDATION
   DPO validates anonymization (k-anonymity check, re-identification testing)
   ↓
7. APPROVAL
   DPO approves (signs checklist) + CISO approves
   ↓
8. TRANSFER
   Anonymized data provided to developer (in dev/test environment)
   ↓
9. USAGE
   Developer uses anonymized data (time-limited, purpose-limited)
   ↓
10. DELETION
    Anonymized data deleted after 30 days or project completion
```

### A.8 Tool Recommendations

#### A.8.1 Open Source Tools

**Faker** (Synthetic Data Generation):
- Languages: Python, JavaScript, Ruby, PHP
- Use: Generate realistic fake data (names, addresses, emails)
- URL: https://faker.readthedocs.io/

**ARX Data Anonymization Tool**:
- Language: Java (GUI application)
- Use: K-anonymity, L-diversity, differential privacy
- URL: https://arx.deidentifier.org/

**Gretel.ai Community Edition**:
- Language: Python
- Use: Statistical synthetic data generation
- URL: https://gretel.ai/

**SDV (Synthetic Data Vault)**:
- Language: Python
- Use: Generate synthetic data from real data models
- URL: https://sdv.dev/

#### A.8.2 Commercial Tools

**Delphix** (Data Masking and Subsetting):
- Enterprise data masking for databases
- Integrated with CI/CD pipelines

**Informatica Persistent Data Masking**:
- Enterprise-scale data anonymization
- Policy-based masking rules

**IBM InfoSphere Optim Data Privacy**:
- Data masking, subsetting, test data generation
- Compliance reporting (GDPR, CCPA)

### A.9 Common Pitfalls and Best Practices

#### A.9.1 What NOT to Do

❌ **Pseudonymization instead of Anonymization**:
- "ID-12345" with lookup table → STILL personal data → NOT ALLOWED

❌ **Weak Masking**:
- "alice.anderson@example.com" → "a.a@example.com" → Too short, re-identifiable

❌ **Inconsistent Tokenization**:
- Customer ID "CUST-001" → Different tokens in different tables → Breaks referential integrity

❌ **No Re-Identification Testing**:
- Assume anonymization works → Don't test → Risk re-identification

❌ **Encrypting instead of Anonymizing**:
- Encrypt production data for dev/test → Can be decrypted → NOT anonymization

❌ **Production Data in Logs/Errors**:
- Anonymize database, but application logs contain real names/emails → Data leakage

#### A.9.2 Best Practices

✅ Use established libraries (Faker, ARX) - don't reinvent the wheel  
✅ DPO approval BEFORE extraction (not after)  
✅ Minimize data volume (1-5% sample, not full dataset)  
✅ Delete after use (30-day maximum retention)  
✅ Test re-identification (attempt to find real people)  
✅ Document everything (technique, DPO approval, retention)  
✅ Prefer synthetic over production-derived (whenever possible)

---

## Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **IT Operations Manager** | [Name] | [Date] |
| **Development Manager / DevOps Lead** | [Name] | [Date] |
| **Data Protection Officer (DPO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (CEO)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.8.31.*

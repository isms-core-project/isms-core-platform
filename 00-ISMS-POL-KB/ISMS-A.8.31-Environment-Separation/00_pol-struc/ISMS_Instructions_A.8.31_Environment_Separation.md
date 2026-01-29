# PROJECT BRIEF: ISMS Control A.8.31 - Separation of Development, Test and Production Environments

## Standalone Control Approach

You are implementing **ONE ISO 27001:2022 Annex A control**:

- **A.8.31 - Separation of Development, Test and Production Environments**: Separating environments to reduce risks

**Why Standalone:**
This control addresses a specific operational security concern: **preventing unauthorized changes to production and protecting production data from development/testing activities**. While it relates to secure development (A.8.25/26/29) and change management (A.8.32), it focuses specifically on **environment isolation**.

**Reference Implementation**: 
- **Quality level**: ISMS-A.8.23-Web-Filtering (standalone control)
- **Approach**: Focused policy on environment separation

**Integration Note**: This control integrates with:
- A.8.25-26-29 (Secure Development) - SDLC security framework
- A.8.32 (Change Management) - Promotion between environments
- A.5.15-16-18 (IAM) - Environment-specific access control
- A.8.2-3-5 (Auth-PAM) - Privileged access per environment
- A.8.4 (Source Code Access) - Code repository separation

## Context & Approach

You are implementing **Environment Separation** using Systems Engineering methodology. This framework must be **completely generic** - applicable to any organization's SDLC environment architecture, regardless of technology or deployment model.

**Implementation Philosophy**: 
- Apply Feynman's "don't fool yourself" principle - no security theater
- System Engineering approach: Separate → Control → Monitor → Evidence
- Think with TWO hats simultaneously:
  * **ISMS Implementer**: Build practical environment separation
  * **ISMS Auditor**: Verify measurable separation effectiveness
- Focus on genuine risk reduction, not checkbox compliance

**Applicability**:
- All content must be **completely generic and technology-agnostic**
- Use "[Organization]" as placeholder throughout
- No assumptions about infrastructure (on-premises, cloud, hybrid)
- No assumptions about deployment technology (VMs, containers, serverless)
- Framework adapts to any environment architecture

## Core Requirements (Specific to A.8.31)

### 1. The Environment Separation Challenge

**Traditional approach (cargo cult):**
```
"We have dev and prod... somewhere. 
Developers can't access prod... I think?
Production data in dev? Yeah, for testing."
[No clear separation, shared credentials, production data in dev]
```
❌ This is meaningless checkbox compliance.

**What auditors and implementers actually need:**

**For A.8.31 (Separation of Development, Test and Production Environments):**
- Environment definition and architecture
  - **Development environment**: Developer workstations, dev servers, dev databases
    - Purpose: Active code development, experimentation
    - Data: Synthetic/test data only, NO production data
    - Access: Developers, limited operations access
  - **Testing/QA environment**: Test servers, test databases
    - Purpose: Quality assurance, integration testing, UAT
    - Data: Synthetic/test data or anonymized production data
    - Access: QA team, developers (read-only or limited), business users (UAT)
  - **Staging/Pre-production environment**: Mirrors production configuration
    - Purpose: Final validation before production deployment
    - Data: Synthetic data or anonymized production data
    - Access: Operations team, limited developer access
  - **Production environment**: Live systems serving users/customers
    - Purpose: Business operations, customer service
    - Data: Real production data
    - Access: Operations team only, NO developer access (except emergency)
- Environment separation mechanisms
  - **Network separation**:
    - Separate network segments/VLANs for each environment
    - Firewall rules preventing unauthorized cross-environment access
    - No direct network connectivity from dev/test to production
  - **Infrastructure separation**:
    - Separate servers/VMs/containers for each environment
    - Separate cloud accounts/subscriptions (AWS accounts, Azure subscriptions)
    - Separate Kubernetes namespaces or clusters
  - **Data separation**:
    - Separate databases for each environment
    - NO production data in dev/test (use synthetic or anonymized data)
    - Data anonymization/masking if production data needed for testing
  - **Credential separation**:
    - Different credentials for each environment
    - Production credentials stored in PAM vault, NOT in code or config files
    - No shared credentials between environments
  - **Configuration separation**:
    - Environment-specific configuration files
    - Configuration management (environment variables, config servers)
    - NO production configuration in dev/test code repositories
- Environment access control
  - **Development environment access**:
    - Developers: Full access (create, read, update, delete)
    - Operations: Limited access (monitoring, support)
  - **Testing environment access**:
    - QA team: Full access for testing
    - Developers: Read-only or limited write access
    - Business users: UAT access only
  - **Production environment access**:
    - Operations team: Admin access via PAM
    - Developers: NO access (except emergency break-glass)
    - Monitoring/observability: Read-only access for troubleshooting
- Environment promotion process
  - Code promotion workflow (dev → test → staging → production)
  - Approval requirements (code review, QA sign-off, change management approval)
  - Automated deployment pipelines (CI/CD)
  - Rollback procedures (if deployment fails)
- Data handling in non-production environments
  - Prohibition of production data in dev/test (unless anonymized)
  - Data anonymization/masking procedures
  - Synthetic data generation
  - Test data management
- Production support and troubleshooting
  - Read-only production access for monitoring/troubleshooting
  - Audit logging of production access
  - Emergency access procedures (break-glass)
  - Production debugging procedures (without exposing sensitive data)
- Environment separation monitoring
  - Access control monitoring (who accessed what environment)
  - Cross-environment access attempts (alert on dev → prod access)
  - Configuration drift detection (environments should be consistent)
  - Data leakage detection (production data in dev/test)

**Your SE Framework Must Provide:**
- **Environment Architecture Framework** - clear definition and separation of environments
- **Access Control Policy** - who can access which environment
- **Promotion Process** - controlled movement between environments
- **Evidence Collection Framework** - access logs, promotion records, separation verification

### 2. Document Length and Quality Guidelines

**Python Scripts:**
- Scripts should be **as long as required** to meet quality standards
- No arbitrary line limits - focus on correctness and robustness
- Environment separation assessment may require cloud API integration
- Quality > arbitrary length constraints

**Policy Document (POL):**
- Should be **comprehensive but not over-engineered**
- Include everything necessary for implementation and audit
- This is a single control, focused on environment separation
- Expected range: 400-600 lines total
- "Just right" - not too short (incomplete), not too long (overkill)

**Implementation Guide (IMP):**
- Should be **practical and focused**
- Step-by-step procedures without unnecessary elaboration
- Include examples for common architectures (AWS, Azure, Kubernetes)

**Annexes:**
- Environment architecture examples (AWS multi-account, Azure subscriptions, Kubernetes namespaces)
- Data anonymization techniques
- CI/CD pipeline examples

### 3. Document Structure (Adapted for A.8.31)

```
ISMS-A.8.31-Environment-Separation/
├── 00_pol-struc/
│   └── [Policy planning notes]
├── 10_pol-md/
│   ├── ISMS-POL-A.8.31-S1-Executive-Summary-Control-Alignment.md
│   ├── ISMS-POL-A.8.31-S2-Environment-Separation-Policy.md
│   ├── ISMS-POL-A.8.31-S3-Assessment-Evidence-Framework.md
│   └── ISMS-POL-A.8.31-Annex-[Topic].md [if needed]
├── 30_imp-md/
│   ├── ISMS-IMP-A.8.31-S1-Environment-Architecture-Implementation.md
│   ├── ISMS-IMP-A.8.31-S2-Environment-Access-Control.md
│   ├── ISMS-IMP-A.8.31-S3-Environment-Separation-Assessment.md
│   └── ISMS-IMP-A.8.31-Annex-[Topic].md [if needed]
└── 50_scripts-excel/
    ├── generate_assessment_1_environment_architecture.py
    ├── generate_assessment_2_environment_access.py
    └── generate_dashboard_environment_separation.py
```

### 4. Policy Content Requirements (Specific to A.8.31)

**Section 1 (S1): Executive Summary, Control Alignment, Scope**
- ISO 27001:2022 control text for A.8.31 (exact quote)
- Executive summary explaining environment separation
- Scope: All SDLC environments (dev, test, staging, production)
- Integration with other controls (SDLC, change management, access control)

**Section 2 (S2): Environment Separation Policy**
Focus on **A.8.31 - Separation of Development, Test and Production Environments** specifically:
- Environment definitions (dev, test, staging, production)
- Environment separation mechanisms (network, infrastructure, data, credentials)
- Environment access control (who can access which environment)
- Environment promotion process (dev → test → staging → prod)
- Data handling in non-production (prohibition of prod data, anonymization)
- Production support procedures (read-only access, emergency access)
- Environment separation monitoring (access logs, cross-environment attempts)
- Measurable requirements with audit verification criteria

**Section 3 (S3): Assessment Methodology and Evidence Framework**
- Environment architecture assessment
- Environment access control verification
- Data separation compliance (no prod data in dev/test)
- Promotion process adherence
- Evidence collection
- Compliance scoring

### 5. Implementation Guidance Requirements

**IMP-S1: Environment Architecture Implementation**
- Network separation (VLANs, subnets, firewall rules)
- Infrastructure separation (separate servers, cloud accounts, Kubernetes namespaces)
- Data separation (separate databases, data anonymization)
- Credential separation (separate credentials, PAM for production)

**IMP-S2: Environment Access Control**
- Access provisioning per environment
- Production access restrictions (no developer access)
- Emergency access procedures (break-glass)
- Access monitoring and alerting

**IMP-S3: Environment Separation Assessment**
- Architecture compliance verification
- Access control audit
- Data separation verification (scan for prod data in dev/test)
- Continuous compliance monitoring

### 6. Assessment Tools (Specific to A.8.31)

**Assessment Workbook 1: Environment Architecture Compliance**
- Environment inventory (dev, test, staging, production)
- Separation mechanism status (network, infrastructure, data, credentials)
- Configuration consistency (staging mirrors production?)
- Architecture compliance score

**Assessment Workbook 2: Environment Access Control**
- User → environment access matrix
- Developer production access (should be zero or break-glass only)
- Production credential usage (stored in PAM vault?)
- Cross-environment access attempts (alert log)
- Access compliance status

**Dashboard: Environment Separation Overview**
- Overall environment separation compliance score
- Environments with proper separation (%)
- Developers with production access (count - should be 0)
- Production data in dev/test (incidents - should be 0)
- Promotion process adherence (%)
- Trend analysis

### 7. Python Scripts Approach

Scripts should:
- Parse cloud infrastructure configurations (AWS, Azure, GCP APIs)
- Verify network separation (security groups, firewall rules)
- Analyze access control (IAM policies, RBAC)
- Detect production data in dev/test (pattern matching, heuristics)
- Generate compliance dashboards

**No arbitrary line limits** - cloud API integration can be complex.

### 8. Key Integration Points

**Integrates with:**
- A.8.25-26-29 (Secure Development) - SDLC framework
- A.8.32 (Change Management) - Promotion workflow
- A.5.15-16-18 (IAM) - Environment-specific access
- A.8.2-3-5 (Auth-PAM) - Production privileged access
- A.8.4 (Source Code Access) - Code repository separation
- A.5.24-27 (Incident Management) - Production incidents

### 9. Quality Checks

- [ ] Control text quoted correctly (A.8.31)
- [ ] Framework works for any infrastructure (on-prem, cloud, hybrid)
- [ ] No assumptions about technology stack
- [ ] Assessment workbooks comprehensive
- [ ] Data anonymization guidance clear
- [ ] Production access restrictions documented

### 10. Regulatory Framework (per ISMS-POL-00)

**Mandatory Compliance (Tier 1):**
- ISO/IEC 27001:2022: Control A.8.31

**Conditional Compliance (Tier 2):**
- **FINMA** (if Swiss financial institution):
  - FINMA Circular 2023/1 Margin 50-62: Environment separation for operational resilience
- **DORA** (if EU financial entity):
  - Article 9: ICT risk management includes environment separation
- **NIS2** (if essential/important entity):
  - Article 21(2): Security measures include environment separation

**Informational Reference (Tier 3):**
- NIST SP 800-53: CM-7 (Least Functionality - includes environment separation)
- OWASP SAMM: Operations stream includes environment management

For complete regulatory categorization, refer to ISMS-POL-00.

### 11. Special Considerations

**Cloud Architecture Patterns:**
- **AWS**: Separate AWS accounts per environment (AWS Organizations)
- **Azure**: Separate Azure subscriptions per environment
- **GCP**: Separate GCP projects per environment
- **Kubernetes**: Separate namespaces or clusters per environment

**Data Anonymization Techniques:**
- Data masking (replace sensitive fields with fake data)
- Tokenization (replace real values with tokens)
- Synthetic data generation (generate realistic but fake data)
- Subsetting (use small sample of production data)

**CI/CD Pipeline Integration:**
- Automated deployment from dev → test → staging → prod
- Environment-specific configuration (environment variables, config files)
- Approval gates (manual approval before production)
- Rollback automation

**Break-Glass Access:**
- Emergency developer access to production (documented, monitored, time-limited)
- Post-incident review of break-glass usage
- Break-glass credentials stored in PAM vault

**Production Data in Dev/Test - Common Violations:**
- Database dumps from production restored to dev/test
- Production backups used for testing
- Production API credentials in dev code
- Production configuration files committed to dev repositories

### 12. Autonomous Work Requirements

Follow standard autonomous work requirements:
- READ reference implementations
- UPDATE with environment separation context
- TEST (UTF-8, formulas, scripts)
- PRESENT complete deliverables

### 13. Deliverable Sequence

1. **Structure Plan** - Confirm approach
2. **Policy Sections** (S1→S2→S3) - Wait for approval
3. **Implementation Sections** (S1→S2→S3) - Wait for approval
4. **Assessment Scripts** - Test thoroughly
5. **Quality Review** - Self-assessment

---

## Your Mission for A.8.31

Create the **Environment Separation Framework** that provides:
- Clear environment architecture and separation mechanisms
- Strong environment access controls
- Prohibition of production data in dev/test
- Controlled promotion process between environments
- Infrastructure and technology-agnostic principles

Use Systems Engineering methodology for **systematic environment separation assessment**.

Make it completely generic - works for any infrastructure, any deployment model, any organization.

Think like a DevOps engineer AND an auditor.

**Ready? Let's start with the structure plan.**

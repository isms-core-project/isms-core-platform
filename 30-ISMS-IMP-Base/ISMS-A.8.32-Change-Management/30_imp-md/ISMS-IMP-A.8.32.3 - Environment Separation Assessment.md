# ISMS-IMP-A.8.32.3 - Environment Separation Assessment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.3 |
| **Version** | 1.0 |
| **Assessment Area** | Development, Test, Production Environment Separation |
| **Related Policy** | ISMS-POL-A.8.32, Section 2.3 (Testing & Validation Requirements), ISO/IEC 27001:2022 Control 8.31 |
| **Purpose** | Assess environment separation, promotion workflows, and access controls to ensure changes are properly tested before production deployment |
| **Target Audience** | Infrastructure Team, DevOps Engineers, System Administrators, Security Team, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Technical & Infrastructure |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial assessment specification for Environment Separation workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Definitions
  - Cell Styling Reference

**Target Audiences:**

- **Part I:** Assessment users (Infrastructure Team, DevOps, Security, System Administrators)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** Infrastructure Team, DevOps Engineers, System Administrators, Security Team

---

## Assessment Overview

### What This Assessment Evaluates

This assessment documents HOW your organization separates development, test, and production environments to ensure changes are properly validated before reaching production. It evaluates:

- **Environment Architecture:** Physical/logical separation of Dev/Test/Prod
- **Access Controls:** Who can access which environments
- **Promotion Workflows:** How code/changes move between environments
- **Data Protection:** How production data is protected in non-production
- **Environment Configuration:** How environments mirror production
- **Separation Enforcement:** Technical controls preventing unauthorized changes

### Why This Matters

This assessment verifies [Organization]'s compliance with:

- ISO/IEC 27001:2022 Control A.8.32: Change Management (element d - testing)
- ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Testing and Production
- ISMS-POL-A.8.32, Section 2.3 (Testing & Validation Requirements)

Testing changes in production is the #1 cause of production incidents. Proper environment separation ensures safe testing, prevents production contamination, and protects production data.

### Key Principle

This assessment is **technology-agnostic**. Whether you use physical servers, VMs, containers, cloud environments, or combinations - this evaluates separation effectiveness, not specific technology.

---

## Prerequisites

### Before Starting This Assessment

**Required:**
- [ ] Read ISMS-POL-A.8.32, Section 2.3 (Testing & Validation Requirements)
- [ ] Read ISO/IEC 27001:2022 Control 8.31 guidance
- [ ] Identify Infrastructure/DevOps lead (assessment owner)
- [ ] Access to network diagrams showing environment topology
- [ ] Access control documentation (who can access what)
- [ ] Deployment/promotion procedures
- [ ] Environment configuration documentation

**Recommended:**
- [ ] Interview DevOps team about deployment workflows
- [ ] Review access logs showing environment usage
- [ ] Gather incident reports involving environment issues
- [ ] Review data masking/anonymization procedures
- [ ] Identify environment monitoring dashboards

### Who Should Complete This Assessment

**Primary:** Infrastructure Manager or DevOps Lead

**Contributors:**
- Network Engineers (network separation, firewall rules)
- System Administrators (server/VM configuration)
- Security Team (access controls, data protection)
- DevOps Engineers (deployment pipelines, promotion workflows)
- Database Administrators (data protection in test)
- Application Owners (environment-specific configurations)

**Reviewers:**
- CISO (security controls validation)
- IT Operations Manager (operational readiness)

---

## Assessment Workflow

### Step-by-Step Process

**Step 1: Initial Setup (Day 1)**
- Assign assessment owner (Infrastructure/DevOps lead)
- Gather network diagrams and architecture documentation
- Review completion timeline (2-3 weeks)

**Step 2: Environment Inventory (Days 2-4)**
- Document all environments (Sheet 2: Environment_Inventory)
- Identify Dev, Test, Staging, Prod environments
- Document infrastructure type (physical/VM/container/cloud)
- Assess separation quality (physical vs logical)

**Step 3: Access Control Assessment (Days 3-6)**
- Document who can access each environment (Sheet 3: Access_Controls)
- Review access provisioning procedures
- Assess privileged access management
- Verify separation of duties (developers can't deploy to prod)

**Step 4: Promotion Workflow Documentation (Days 4-7)**
- Document how changes move between environments (Sheet 4: Promotion_Workflows)
- Map promotion checkpoints and approvals
- Assess automation level (manual vs automated)
- Review rollback capabilities

**Step 5: Data Protection Assessment (Days 5-8)**
- Assess production data usage in test (Sheet 5: Data_Protection)
- Review data masking/anonymization procedures
- Document synthetic data generation
- Verify no production credentials in non-prod

**Step 6: Environment Configuration (Days 6-9)**
- Compare environment configurations (Sheet 6: Environment_Config)
- Assess how closely test mirrors production
- Document configuration management approach
- Identify configuration drift issues

**Step 7: Separation Enforcement (Days 7-10)**
- Document technical controls enforcing separation (Sheet 7: Separation_Controls)
- Review network segmentation
- Assess deployment prevention controls
- Review monitoring and alerting

**Step 8: Evidence Collection (Days 8-11)**
- Compile supporting evidence (Sheet 8: Evidence_Register)
- Network diagrams, access logs, deployment logs

**Step 9: Summary Review (Days 9-12)**
- Review auto-calculated compliance (Sheet 9: Summary_Dashboard)
- Validate gap analysis

**Step 10: Quality Review (Days 10-13)**
- Self-review against checklist
- Peer review by Security Team

**Step 11: Final Approval (Days 11-15)**
- Infrastructure Manager approval
- CISO sign-off (Sheet 10: Approval_Sign_Off)

**Total Duration:** 2-3 weeks

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Pre-filled** - Read to understand status symbols, compliance levels, and evidence expectations.

### Sheet 2: Environment_Inventory

**What to document:**
- All environments used in change workflow
- Environment type (Dev/Test/Staging/Prod/DR)
- Infrastructure type (physical/VM/container/cloud)
- Separation method (physical, network, logical)
- Environment purpose and scope

**Tips:**
- Include ALL environments - personal dev environments, CI/CD agents, etc.
- If you only have Prod (no test), this is major gap - document honestly
- Staging/Pre-Prod environments are optional but recommended for high-risk systems
- Cloud environments (separate VPCs/VNets) count as logical separation

**Common Questions:**
- **Q:** "Is developer laptop a 'Dev environment'?"
  - **A:** Yes if used for development work. Document access controls for local dev.
- **Q:** "We have Dev and Prod but no Test - is that OK?"
  - **A:** Not compliant with policy. Mark as gap requiring remediation.
- **Q:** "Is Docker container separation adequate?"
  - **A:** Depends on isolation. Containers on same host = logical separation. Document honestly.

**Evidence to provide:**
- Network diagrams showing all environments
- Infrastructure documentation (cloud VPCs, VLANs, physical locations)
- Environment inventory list
- Architecture diagrams

### Sheet 3: Access_Controls

**What to document:**
- Who has access to each environment
- Access levels (read-only, deploy, admin)
- Access provisioning process (how access is granted)
- MFA requirements by environment
- Privileged access management
- Separation of duties enforcement

**Tips:**
- "Developers can't deploy to production" is key control - verify this
- Production access should be most restricted
- Break-glass emergency access is OK if logged and auditable
- Service accounts need same scrutiny as user accounts

**Common Questions:**
- **Q:** "Developers need production access for troubleshooting"
  - **A:** Read-only prod access for troubleshooting is acceptable. WRITE access for developers is policy violation.
- **Q:** "What about DevOps engineers?"
  - **A:** DevOps can have prod deploy rights IF they're not also developers on that system (separation of duties).
- **Q:** "We use shared credentials for deployment"
  - **A:** Major gap - individual accountability required. Document as finding.

**Evidence to provide:**
- Access control matrix (who can access what)
- Access provisioning procedures
- PAM system documentation
- Access logs showing who accessed what
- MFA configuration by environment

### Sheet 4: Promotion_Workflows

**What to document:**
- How changes move Dev -> Test -> Staging -> Prod
- Promotion checkpoints and approvals
- Automated vs manual promotion
- Deployment pipeline documentation
- Rollback procedures at each stage

**Tips:**
- Linear progression (Dev -> Test -> Prod) preferred over "wild west" deployment
- Automation reduces errors but doesn't eliminate need for checkpoints
- Skipping test and going Dev -> Prod should be rare (emergency only)
- Document ACTUAL workflow, not ideal workflow

**Common Questions:**
- **Q:** "Can we skip Test for small changes?"
  - **A:** Policy allows risk-based approaches. Document YOUR criteria for test skipping. Low-risk standard changes might skip full test cycle.
- **Q:** "We use CI/CD - does that count as controlled promotion?"
  - **A:** Yes IF pipeline has proper controls (automated testing, approvals, audit trail). Document pipeline stages.
- **Q:** "What if Test environment isn't available?"
  - **A:** Not an excuse to deploy untested. Document as process gap and remediation plan.

**Evidence to provide:**
- Promotion workflow diagrams
- CI/CD pipeline configurations
- Deployment logs showing progression
- Approval records at promotion checkpoints
- Rollback procedure documentation

### Sheet 5: Data_Protection

**What to document:**
- How production data is used (or not used) in non-production
- Data masking/anonymization procedures
- Synthetic test data generation
- Credential management (no prod credentials in test)
- Backup data protection

**Tips:**
- Production data in test is HIGH RISK - regulatory violation (GDPR, etc.)
- "We copy production to test" = policy violation unless properly masked
- Synthetic data is ideal but takes effort - masking is pragmatic middle ground
- Production credentials MUST NOT exist in non-production environments

**Common Questions:**
- **Q:** "We need real data for realistic testing"
  - **A:** Then MASK it properly. Real names, addresses, credit cards must be obfuscated.
- **Q:** "What about production-like data (similar but not real)?"
  - **A:** Synthetic data is best approach - document generation procedures.
- **Q:** "We have production database credentials in test for read-only queries"
  - **A:** Policy violation - test should NEVER have production credentials. Use test-specific accounts.

**Evidence to provide:**
- Data masking procedures and tools
- Sample test data (showing it's masked, not real)
- Synthetic data generation scripts
- Credential management documentation
- Data classification by environment

### Sheet 6: Environment_Config

**What to document:**
- How closely test/staging mirror production
- Configuration management approach (IaC, manual, hybrid)
- Environment-specific configuration handling
- Configuration drift detection and correction
- Infrastructure-as-Code usage

**Tips:**
- Test should closely mirror prod (OS, middleware, dependencies)
- Perfect mirror not always feasible (cost, scale) - document differences
- Configuration drift (test diverging from prod) causes "works in test, fails in prod"
- IaC (Terraform, CloudFormation, Ansible) helps maintain consistency

**Common Questions:**
- **Q:** "Test has older hardware than prod - is that OK?"
  - **A:** Hardware can differ. SOFTWARE stack should match (OS version, app version, middleware).
- **Q:** "Test has 1 server, Prod has 10 - does test need same scale?"
  - **A:** No - test can be smaller scale. But architecture should be similar (load balancer, DB, app tier).
- **Q:** "We manage environments manually"
  - **A:** Manual is higher risk (human error, drift). Document as improvement opportunity. IaC is recommended but not mandatory.

**Evidence to provide:**
- Environment configuration specifications
- IaC scripts (Terraform, CloudFormation, Ansible)
- Configuration management tool documentation
- Drift detection reports
- Environment comparison matrix

### Sheet 7: Separation_Controls

**What to document:**
- Technical controls enforcing separation
- Network segmentation (VLANs, firewalls, security groups)
- Deployment prevention (can't accidentally deploy to wrong environment)
- Monitoring and alerting for separation violations
- Automated controls vs manual procedures

**Tips:**
- Technical controls > manual procedures (humans make mistakes)
- Firewall rules between environments enforce network separation
- Deployment tools should require explicit environment selection
- "Accidentally deployed to prod" should be technically prevented, not just procedurally prohibited

**Common Questions:**
- **Q:** "What if all environments are on same network?"
  - **A:** Major gap - network segmentation required. Document as finding.
- **Q:** "We rely on developers not deploying to prod by accident"
  - **A:** Insufficient - need technical controls. Deployment tool should require explicit prod approval/MFA.
- **Q:** "Cloud environments in same VPC/VNet OK?"
  - **A:** Only if subnets and security groups properly segment. Flat network is violation.

**Evidence to provide:**
- Network diagrams showing segmentation
- Firewall rules between environments
- Deployment tool configuration (environment targeting)
- Monitoring dashboards for separation violations
- Access control lists

### Sheet 8: Evidence_Register

**What to document:**
- Evidence location for all requirements
- Evidence type and last verification
- Accessibility for auditors

**Tips:**
- Network diagrams are KEY evidence for this assessment
- Access logs prove who accessed what
- Deployment logs prove promotion workflow compliance

### Sheet 9: Summary_Dashboard

**Auto-calculated** - Review for accuracy:
- Overall compliance percentage
- Compliance by domain (inventory, access, promotion, data, config)
- Critical gaps requiring attention

### Sheet 10: Approval_Sign_Off

**What to complete:**
- Assessment completion date
- Infrastructure Manager sign-off
- CISO approval
- Next review date

---

## Evidence Collection

### Types of Evidence

**Architecture Evidence:**
- Network diagrams (all environments)
- Infrastructure topology documentation
- Cloud architecture diagrams (VPCs, VNets, subnets)
- Physical datacenter layouts (if applicable)

**Access Control Evidence:**
- Access control matrix
- IAM policies/role definitions
- Access provisioning audit logs
- MFA configuration documentation
- PAM system configuration

**Promotion Evidence:**
- CI/CD pipeline configurations
- Deployment logs showing environment progression
- Promotion approval records
- Rollback execution examples

**Data Protection Evidence:**
- Data masking tool configuration
- Sample test data (showing masking)
- Credential management procedures
- Data classification by environment

**Configuration Evidence:**
- IaC scripts (Terraform, CloudFormation, Ansible)
- Configuration management system documentation
- Environment comparison reports
- Drift detection alerts

**Control Evidence:**
- Firewall rules between environments
- Security group configurations
- Deployment tool access controls
- Monitoring dashboards and alerts

### Evidence Best Practices

**Do:**
- ? Include network diagrams with clear environment boundaries
- ? Provide access logs showing restricted prod access
- ? Show deployment logs proving Dev -> Test -> Prod progression
- ? Document automated controls (firewall rules, security groups)

**Don't:**
- ? Provide outdated network diagrams
- ? Hide the fact that developers have production access
- ? Claim "we have separation" without technical evidence
- ? Confuse logical separation with no separation

---

## Common Pitfalls

### Mistake #1: "We have Dev and Prod - that's good enough"

**Problem:** Policy requires separate TEST environment for validation before production.

**Solution:** Minimum: Dev + Test + Prod. Document gap if test is missing, with remediation plan.

### Mistake #2: "Developers need prod access to fix issues quickly"

**Problem:** Violates separation of duties. Developers with prod write access = uncontrolled changes.

**Solution:** Read-only prod access OK for troubleshooting. WRITE access only for designated deployers (DevOps, Ops).

### Mistake #3: "All environments on same network is fine"

**Problem:** No technical enforcement of separation. Accidental prod deployment is easy.

**Solution:** Network segmentation required (VLANs, firewalls, cloud security groups).

### Mistake #4: "We copy production database to test for realistic testing"

**Problem:** MAJOR data protection violation (GDPR, privacy regulations).

**Solution:** Mask/anonymize production data OR generate synthetic test data. NEVER use unprotected prod data in test.

### Mistake #5: "Test environment has older versions - saves money"

**Problem:** "Works in test" doesn't mean "works in prod" if versions differ.

**Solution:** Test should mirror prod software versions. Hardware can be smaller scale, but software stack must match.

### Mistake #6: "We only test in prod because test is always broken"

**Problem:** Test environment not maintained properly. Testing in prod is policy violation.

**Solution:** Fix test environment maintenance. Production is NOT a test environment.

### Mistake #7: "Configuration management is too complex, we do it manually"

**Problem:** Manual configuration leads to drift and inconsistencies.

**Solution:** Start simple - even scripted configs better than manual. Progress toward IaC over time.

### Mistake #8: "Shared service accounts are fine - we know who uses them"

**Problem:** No individual accountability. Can't prove who deployed what.

**Solution:** Individual accounts for deployment. Service accounts only for automated systems (CI/CD agents) with audit logging.

### Mistake #9: "Container isolation is the same as VM isolation"

**Problem:** Container escape vulnerabilities exist. Containers on same host share kernel.

**Solution:** Document container isolation model honestly. Additional controls for production containers.

### Mistake #10: "Cloud provider handles separation for us"

**Problem:** Cloud provides tools, but YOU configure them. Flat VPC/VNet = no separation.

**Solution:** Properly configure cloud security groups, VPC/VNet segmentation, IAM policies.

---

## Quality Checklist

### Assessment Completeness

**Environment Inventory:**
- [ ] All environments documented (Dev, Test, Staging, Prod, DR)
- [ ] Separation method documented for each
- [ ] Infrastructure type identified
- [ ] Minimum Dev + Test + Prod exists (or gap documented)

**Access Controls:**
- [ ] Access matrix complete (who can access what)
- [ ] Separation of duties verified (devs can't deploy to prod)
- [ ] Privileged access management documented
- [ ] MFA requirements by environment documented
- [ ] Access logs available as evidence

**Promotion Workflows:**
- [ ] Workflow documented (how changes progress)
- [ ] Checkpoints and approvals identified
- [ ] Automation level documented
- [ ] Rollback procedures defined
- [ ] Deployment logs available

**Data Protection:**
- [ ] Production data usage in test documented
- [ ] Data masking/anonymization procedures defined
- [ ] Credential management verified (no prod creds in test)
- [ ] Data protection evidence available

**Environment Configuration:**
- [ ] Test mirrors prod (or differences documented)
- [ ] Configuration management approach defined
- [ ] Drift detection mechanisms documented
- [ ] IaC usage documented (if applicable)

**Separation Controls:**
- [ ] Network segmentation documented
- [ ] Firewall rules/security groups documented
- [ ] Technical controls enforcing separation verified
- [ ] Monitoring and alerting defined

**Evidence:**
- [ ] Network diagrams current (<6 months)
- [ ] Access logs available
- [ ] Deployment logs available
- [ ] All evidence accessible to auditors

**Dashboard:**
- [ ] Compliance percentage validated
- [ ] Critical gaps identified
- [ ] Remediation priorities set

---

## Review & Approval

### Review Process

**Step 1: Self-Review (Infrastructure Manager)**
- Complete quality checklist
- Validate network diagrams current
- Verify access control matrix accurate

**Step 2: Peer Review (Security Team)**
- Review access controls for separation of duties
- Validate data protection procedures
- Assess technical control adequacy
- Typical turnaround: 3-5 days

**Step 3: Compliance Review (Compliance Officer)**
- Verify regulatory data protection compliance
- Check separation requirements met
- Typical turnaround: 2-3 days

**Step 4: CISO Approval**
- Overall separation effectiveness
- Data protection risk acceptance
- Critical gap remediation plans
- Typical turnaround: 2-3 days

**Step 5: Documentation & Communication**
- Set status to "Final"
- Set next review date (+3 months)
- File network diagrams and evidence
- Notify gap owners

**Approval Timeline:** 2-3 weeks

**Rejection Reasons:**
- Missing test environment (critical gap)
- Developers have production write access
- Production data in test without masking
- No network segmentation between environments
- Outdated or missing network diagrams

---

## Continuous Improvement

### Using Assessment Results

**Environment Maturity:**
- Only Dev+Prod -> Add Test environment
- Manual deployments -> Implement CI/CD automation
- No IaC -> Start with configuration scripts, progress to full IaC

**Access Control Refinement:**
- Review access logs - is prod access actually restricted?
- Implement PAM for privileged access
- Regular access reviews - remove unused access


# ISMS-IMP-A.8.32.3 - Environment Separation Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.32.3  
**Assessment Area:** Development, Test, and Production Environment Separation  
**Related Policy:** ISMS-POL-A.8.32-S2.3 (Testing & Validation Requirements)  
**Related Controls:** ISO 27001:2022 Control 8.31 (Separation of Environments), Control 8.33 (Test Information)  
**Purpose:** Assess environment separation controls, promotion procedures, and production data protection in non-production environments in a technology-agnostic manner

**Key Principle:** This assessment is **technology-independent**. Organizations document THEIR specific environment architecture and verify separation controls against generic requirements.

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section
- **Title:** "ISMS-IMP-A.8.32.3 – Environment Separation Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.32: Change Management (Environment Separation)"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.32.3
Assessment Area:       Environment Separation (Dev/Test/Prod)
Related Policy:        ISMS-POL-A.8.32-S2.3
Related Controls:      ISO 27001:2022 Control 8.31, 8.33
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [Organization]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Document YOUR development environment configuration and controls
2. Document YOUR test/QA environment configuration and controls
3. Document YOUR production environment configuration and controls
4. Define YOUR environment promotion procedures
5. Assess YOUR production data usage in non-production environments (Control 8.33)
6. Review the Summary_Dashboard for compliance metrics
7. Maintain the Evidence Register for audit traceability
8. Obtain final approval and sign-off

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| [YES] | Defined | Criteria/process clearly defined and documented | Green (C6EFCE) |
| [PARTIAL] | Partial | Partially defined or inconsistent application | Yellow (FFEB9C) |
| [NO] | Not Defined | Not defined or not documented | Red (FFC7CE) |
| [PLANNED] | Planned | Definition planned with target date | Blue (B4C7E7) |
| N/A | Not Applicable | Not applicable to this environment | Gray |


#### Environment Separation Principles
```
Development Environment:
├─ Purpose: Code development, experimentation, proof-of-concept
├─ Data: Synthetic/anonymized data ONLY
├─ Access: Developers (broad access for development work)
└─ Change Control: Minimal (developer-managed)

Test/QA Environment:
├─ Purpose: Functional testing, integration testing, UAT
├─ Data: Synthetic/anonymized data (production-like structure)
├─ Access: Testers, QA team, select business users
└─ Change Control: Moderate (controlled release cycles)

Production Environment:
├─ Purpose: Live business operations
├─ Data: Real production data (full protection required)
├─ Access: Restricted (least privilege, approved users only)
└─ Change Control: Full (formal change management per Control 8.32)

CRITICAL: Production data SHALL NOT be used in Dev/Test without:
  • Data anonymization/pseudonymization (Control 8.33)
  • Explicit approval by data owner/DPO
  • Documented business justification
  • Technical controls preventing re-identification
```

#### Acceptable Evidence (Examples)
- ✓ Network architecture diagrams (environment separation)
- ✓ Access control matrices (by environment)
- ✓ Environment promotion procedures
- ✓ Production data handling policy
- ✓ Data anonymization procedures
- ✓ Environment configuration baselines
- ✓ Change promotion logs/records
- ✓ Access review records (by environment)
- ✓ Segregation of duties matrix
- ✓ Test data generation procedures
- ✓ Data masking/anonymization tool configs
- ✓ Audit logs (environment access)

---

## Sheet 2: Development_Environment

### Purpose
Document development environment configuration, access controls, and separation measures.

### Header Section
**Row 1:** "DEVELOPMENT ENVIRONMENT ASSESSMENT"  
**Row 2:** "Code development, experimentation, and proof-of-concept environment"

### Environment Identification (Rows 4-20)

| Attribute | Value | Evidence Location |
|-----------|-------|-------------------|
| **Environment Identity** | | |
| Environment Name | Text (e.g., "Development", "DEV", "Engineering Lab") | Text |
| Purpose/Scope | Text | Text |
| Number of instances/deployments | Number | Text |
| Hosting model | Dropdown: On-Premises/Cloud/Hybrid/Virtual/Containerized | Text |
| Geographic location(s) | Text | Text |
| **Network Isolation** | | |
| Network segment/VLAN | Text (e.g., "VLAN 100", "10.10.x.x/16") | Text |
| Firewall rules isolate from production | Dropdown: ✅ Yes/⚠️ Partial/❌ No/📋 Planned | Text |
| Internet connectivity | Dropdown: Direct/Via Proxy/Restricted/None | Text |
| VPN access required | Dropdown: ✅ Yes/❌ No | Text |
| Network monitoring enabled | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| **Physical/Logical Separation** | | |
| Separate physical infrastructure | Dropdown: ✅ Yes/⚠️ Shared/❌ No | Text |
| Separate admin credentials | Dropdown: ✅ Yes/❌ No | Text |
| Separate DNS namespace | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| Separate backup systems | Dropdown: ✅ Yes/⚠️ Shared/❌ No | Text |

### Access Control Assessment (Rows 22-40)

| Control | Implemented | Implementation Details | Compliance | Evidence |
|---------|-------------|----------------------|------------|----------|
| **Authentication & Authorization** | | | | |
| Authentication method | Dropdown: SSO/LDAP/Local/MFA Required/Other | Text | Dropdown: ✅/⚠️/❌/📋 | Text |
| Role-based access control (RBAC) | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Privileged access management | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Access request/approval process | Dropdown: ✅ Formal/⚠️ Informal/❌ None | Text | Dropdown | Text |
| Access review frequency | Dropdown: Monthly/Quarterly/Annually/Ad-hoc/None | Text | Dropdown | Text |
| **Developer Access Rights** | | | | |
| Developers have admin/root access | Dropdown: ✅ Yes/⚠️ Limited/❌ No | Text (justification) | Dropdown | Text |
| Developers can deploy code directly | Dropdown: ✅ Yes/⚠️ Restricted/❌ No | Text | Dropdown | Text |
| Developers can modify infrastructure | Dropdown: ✅ Yes/⚠️ Restricted/❌ No | Text | Dropdown | Text |
| **Access Logging** | | | | |
| Access logs maintained | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Log retention period | Text (e.g., "90 days") | Text | Dropdown | Text |
| Log monitoring/alerting | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |

### Data Controls (Rows 42-58)

| Control | Implemented | Implementation Details | Compliance | Evidence |
|---------|-------------|----------------------|------------|----------|
| **Data Sources** | | | | |
| Production data prohibited | Dropdown: ✅ Strictly Enforced/⚠️ With Approval/❌ Allowed/📋 Policy Pending | Text | Dropdown: ✅/⚠️/❌ | Text |
| Synthetic data used | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text (data generation method) | Dropdown | Text |
| Anonymized data used | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text (anonymization method) | Dropdown | Text |
| Test data generators available | Dropdown: ✅ Yes/❌ No | Text | Dropdown | Text |
| **Data Protection** | | | | |
| Encryption at rest | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Encryption in transit | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Data backup procedures | Dropdown: ✅ Yes/⚠️ Minimal/❌ No | Text | Dropdown | Text |
| Data retention/disposal policy | Dropdown: ✅ Yes/⚠️ Informal/❌ No | Text | Dropdown | Text |

### Change Management Integration (Rows 60-68)

| Aspect | Implemented | Details | Compliance | Evidence |
|--------|-------------|---------|------------|----------|
| Changes tracked/logged | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text (tracking method) | Dropdown: ✅/⚠️/❌ | Text |
| Version control system used | Dropdown: ✅ Yes/❌ No | Text (e.g., "Git") | Dropdown | Text |
| Promotion to test requires approval | Dropdown: ✅ Yes/⚠️ Informal/❌ No | Text | Dropdown | Text |
| Code review required | Dropdown: ✅ Yes/⚠️ Recommended/❌ No | Text | Dropdown | Text |
| Automated testing in dev | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |

---

## Sheet 3: Test_QA_Environment

### Purpose
Document test/QA environment configuration, access controls, and separation measures.

### Header Section
**Row 1:** "TEST/QA ENVIRONMENT ASSESSMENT"  
**Row 2:** "Functional testing, integration testing, and user acceptance testing environment"

### Environment Identification (Rows 4-20)

| Attribute | Value | Evidence Location |
|-----------|-------|-------------------|
| **Environment Identity** | | |
| Environment Name | Text (e.g., "Test", "QA", "UAT", "Staging") | Text |
| Purpose/Scope | Text | Text |
| Number of instances/deployments | Number | Text |
| Hosting model | Dropdown: On-Premises/Cloud/Hybrid/Virtual/Containerized | Text |
| Geographic location(s) | Text | Text |
| **Network Isolation** | | |
| Network segment/VLAN | Text | Text |
| Firewall rules isolate from production | Dropdown: ✅ Yes/⚠️ Partial/❌ No/📋 Planned | Text |
| Firewall rules isolate from dev | Dropdown: ✅ Yes/⚠️ Partial/❌ No/📋 Planned | Text |
| Internet connectivity | Dropdown: Direct/Via Proxy/Restricted/None | Text |
| VPN access required | Dropdown: ✅ Yes/❌ No | Text |
| Network monitoring enabled | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| **Physical/Logical Separation** | | |
| Separate physical infrastructure | Dropdown: ✅ Yes/⚠️ Shared with Dev/⚠️ Shared with Prod/❌ No | Text |
| Separate admin credentials | Dropdown: ✅ Yes/❌ No | Text |
| Separate DNS namespace | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| Separate backup systems | Dropdown: ✅ Yes/⚠️ Shared/❌ No | Text |

### Access Control Assessment (Rows 22-42)

| Control | Implemented | Implementation Details | Compliance | Evidence |
|---------|-------------|----------------------|------------|----------|
| **Authentication & Authorization** | | | | |
| Authentication method | Dropdown: SSO/LDAP/Local/MFA Required/Other | Text | Dropdown: ✅/⚠️/❌/📋 | Text |
| Role-based access control (RBAC) | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Privileged access management | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Access request/approval process | Dropdown: ✅ Formal/⚠️ Informal/❌ None | Text | Dropdown | Text |
| Access review frequency | Dropdown: Monthly/Quarterly/Annually/Ad-hoc/None | Text | Dropdown | Text |
| **Tester/QA Access Rights** | | | | |
| Testers have admin access | Dropdown: ✅ Yes/⚠️ Limited/❌ No | Text (justification) | Dropdown | Text |
| Testers can deploy code | Dropdown: ✅ Yes/⚠️ Via Pipeline/❌ No | Text | Dropdown | Text |
| Testers can modify data | Dropdown: ✅ Yes/⚠️ Limited/❌ No | Text | Dropdown | Text |
| Business users access (UAT) | Dropdown: ✅ Yes/⚠️ Limited/❌ No | Text | Dropdown | Text |
| Developer access to test env | Dropdown: ✅ Yes/⚠️ Read-Only/❌ No | Text | Dropdown | Text |
| **Access Logging** | | | | |
| Access logs maintained | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Log retention period | Text (e.g., "90 days") | Text | Dropdown | Text |
| Log monitoring/alerting | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |

### Data Controls (Rows 44-62)

| Control | Implemented | Implementation Details | Compliance | Evidence |
|---------|-------------|----------------------|------------|----------|
| **Data Sources** | | | | |
| Production data prohibited | Dropdown: ✅ Strictly Enforced/⚠️ Anonymized Only/❌ Allowed/📋 Policy Pending | Text | Dropdown: ✅/⚠️/❌ | Text |
| Synthetic data used | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Anonymized production data used | Dropdown: ✅ With Approval/⚠️ Yes/❌ No/N/A | Text | Dropdown | Text |
| Anonymization controls verified | Dropdown: ✅ Yes/⚠️ Partial/❌ No/N/A | Text | Dropdown | Text |
| Data subset used (not full prod copy) | Dropdown: ✅ Yes/❌ No/N/A | Text | Dropdown | Text |
| Re-identification risk assessed | Dropdown: ✅ Yes/⚠️ Partial/❌ No/N/A | Text | Dropdown | Text |
| **Data Protection** | | | | |
| Encryption at rest | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Encryption in transit | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Data backup procedures | Dropdown: ✅ Yes/⚠️ Minimal/❌ No | Text | Dropdown | Text |
| Data retention/disposal policy | Dropdown: ✅ Yes/⚠️ Informal/❌ No | Text | Dropdown | Text |
| Test data refresh procedures | Dropdown: ✅ Yes/⚠️ Ad-hoc/❌ No | Text | Dropdown | Text |

### Testing Controls (Rows 64-74)

| Control | Implemented | Details | Compliance | Evidence |
|---------|-------------|---------|------------|----------|
| Test plans required | Dropdown: ✅ Yes/⚠️ Recommended/❌ No | Text | Dropdown: ✅/⚠️/❌ | Text |
| Test results documented | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Automated testing framework | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Performance testing capabilities | Dropdown: ✅ Yes/⚠️ Limited/❌ No | Text | Dropdown | Text |
| Security testing performed | Dropdown: ✅ Yes/⚠️ Occasional/❌ No | Text | Dropdown | Text |
| UAT sign-off required | Dropdown: ✅ Yes/⚠️ Informal/❌ No | Text | Dropdown | Text |

---

## Sheet 4: Production_Environment

### Purpose
Document production environment configuration, access controls, and separation measures.

### Header Section
**Row 1:** "PRODUCTION ENVIRONMENT ASSESSMENT"  
**Row 2:** "Live business operations environment with full protection controls"

### Environment Identification (Rows 4-22)

| Attribute | Value | Evidence Location |
|-----------|-------|-------------------|
| **Environment Identity** | | |
| Environment Name | Text (e.g., "Production", "PROD", "Live") | Text |
| Purpose/Scope | Text | Text |
| Number of instances/deployments | Number | Text |
| Hosting model | Dropdown: On-Premises/Cloud/Hybrid/Virtual/Containerized | Text |
| Geographic location(s) | Text | Text |
| High availability configured | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| Disaster recovery site exists | Dropdown: ✅ Yes/❌ No | Text |
| **Network Isolation** | | |
| Network segment/VLAN | Text | Text |
| Firewall rules strictly isolate from dev | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| Firewall rules strictly isolate from test | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| Internet connectivity | Dropdown: Direct/Via Proxy/DMZ/Restricted | Text |
| VPN access required | Dropdown: ✅ Yes/❌ No | Text |
| Network monitoring/IDS enabled | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| DDoS protection | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| **Physical/Logical Separation** | | |
| Dedicated physical infrastructure | Dropdown: ✅ Yes/⚠️ Shared/❌ No | Text |
| Separate admin credentials | Dropdown: ✅ Yes/❌ No | Text |
| Separate DNS namespace | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| Separate backup systems | Dropdown: ✅ Yes/⚠️ Shared/❌ No | Text |

### Access Control Assessment (Rows 24-48)

| Control | Implemented | Implementation Details | Compliance | Evidence |
|---------|-------------|----------------------|------------|----------|
| **Authentication & Authorization** | | | | |
| Authentication method | Dropdown: SSO with MFA/LDAP with MFA/MFA Required/Other | Text | Dropdown: ✅/⚠️/❌ | Text |
| Multi-factor authentication (MFA) | Dropdown: ✅ Mandatory/⚠️ Recommended/❌ No | Text | Dropdown | Text |
| Role-based access control (RBAC) | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Least privilege enforced | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Privileged access management | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Just-in-time (JIT) access | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Access request/approval process | Dropdown: ✅ Formal Required/⚠️ Informal/❌ None | Text | Dropdown | Text |
| Access review frequency | Dropdown: Monthly/Quarterly/Annually/Ad-hoc | Text | Dropdown | Text |
| **Production Access Restrictions** | | | | |
| Developers have production access | Dropdown: ❌ No/⚠️ Read-Only/⚠️ Emergency Only/✅ Yes (justify) | Text (justification required) | Dropdown | Text |
| Developers can deploy to production | Dropdown: ❌ No/⚠️ Via Pipeline Only/✅ Yes (justify) | Text | Dropdown | Text |
| Segregation of duties enforced | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Emergency access procedures | Dropdown: ✅ Yes/⚠️ Informal/❌ No | Text | Dropdown | Text |
| Break-glass accounts controlled | Dropdown: ✅ Yes/⚠️ Partial/❌ No/N/A | Text | Dropdown | Text |
| **Access Logging & Monitoring** | | | | |
| All access logged | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Log retention period | Text (e.g., "1 year minimum") | Text | Dropdown | Text |
| Real-time monitoring/alerting | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| SIEM integration | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Privileged access monitoring | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |

### Data Protection Controls (Rows 50-68)

| Control | Implemented | Implementation Details | Compliance | Evidence |
|---------|-------------|----------------------|------------|----------|
| **Production Data Protection** | | | | |
| Encryption at rest | Dropdown: ✅ Yes - All Data/⚠️ Partial/❌ No | Text | Dropdown: ✅/⚠️/❌ | Text |
| Encryption in transit | Dropdown: ✅ Yes - All Connections/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Data classification applied | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| PII/sensitive data identified | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Data backup procedures | Dropdown: ✅ Yes/⚠️ Minimal/❌ No | Text | Dropdown | Text |
| Backup testing performed | Dropdown: ✅ Regular/⚠️ Occasional/❌ No | Text | Dropdown | Text |
| Data retention policy enforced | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| **Production Data Copying Controls** | | | | |
| Prod data copy to non-prod prohibited | Dropdown: ✅ Yes - Strict/⚠️ With Approval/❌ No | Text | Dropdown | Text |
| Data extraction requires approval | Dropdown: ✅ Yes/⚠️ Informal/❌ No | Text | Dropdown | Text |
| Data anonymization mandatory | Dropdown: ✅ Yes/⚠️ Recommended/❌ No | Text | Dropdown | Text |
| Anonymization effectiveness tested | Dropdown: ✅ Yes/⚠️ Partial/❌ No/N/A | Text | Dropdown | Text |
| DPO approval required (GDPR) | Dropdown: ✅ Yes/❌ No/N/A | Text | Dropdown | Text |

### Change Management Integration (Rows 70-82)

| Aspect | Implemented | Details | Compliance | Evidence |
|--------|-------------|---------|------------|----------|
| All production changes logged | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown: ✅/⚠️/❌ | Text |
| Formal change management required | Dropdown: ✅ Yes - Mandatory/⚠️ Recommended/❌ No | Text | Dropdown | Text |
| CAB approval required | Dropdown: ✅ Yes/⚠️ Risk-Based/❌ No | Text | Dropdown | Text |
| Automated deployment pipelines | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |
| Manual production changes prohibited | Dropdown: ✅ Yes/⚠️ Emergency Only/❌ No | Text | Dropdown | Text |
| Rollback plan required | Dropdown: ✅ Yes - Mandatory/⚠️ Recommended/❌ No | Text | Dropdown | Text |
| Post-deployment verification | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Text |

---

## Sheet 5: Environment_Promotion_Process

### Purpose
Document procedures for promoting code/configuration from Dev → Test → Production.

### Header Section
**Row 1:** "ENVIRONMENT PROMOTION PROCEDURES"  
**Row 2:** "Code and configuration promotion from Development through Test to Production"

### Promotion Path Definition (Rows 4-15)

| Promotion Path | From Environment | To Environment | Approval Required | Automated | Documented | Evidence |
|----------------|-----------------|----------------|-------------------|-----------|------------|----------|
| Dev to Test | Text (e.g., "Development") | Text (e.g., "Test/QA") | Dropdown: ✅ Yes/⚠️ Peer Review/❌ No | Dropdown: ✅ Fully/⚠️ Partial/❌ Manual | Dropdown: ✅/⚠️/❌/📋 | Text |
| Test to Staging/Pre-Prod | Text | Text | Dropdown | Dropdown | Dropdown | Text |
| Staging to Production | Text | Text | Dropdown | Dropdown | Dropdown | Text |
| Direct Dev to Production | Text | Text | Dropdown: ❌ Prohibited/⚠️ Emergency Only/✅ Allowed (justify) | Dropdown | Dropdown | Text |
| Hotfix path (emergency) | Text | Text | Dropdown | Dropdown | Dropdown | Text |

### Promotion Controls (Rows 17-38)

| Control | Dev→Test | Test→Staging | Staging→Prod | Emergency Path | Compliance | Evidence |
|---------|----------|--------------|--------------|----------------|------------|----------|
| **Pre-Promotion Checks** | | | | | | |
| Code review completed | Dropdown: ✅ Yes/⚠️ Recommended/❌ No/N/A | Dropdown | Dropdown | Dropdown | Dropdown: ✅/⚠️/❌ | Text |
| Automated tests passed | Dropdown | Dropdown | Dropdown | Dropdown | Dropdown | Text |
| Security scan performed | Dropdown | Dropdown | Dropdown | Dropdown | Dropdown | Text |
| Change request approved | Dropdown | Dropdown | Dropdown: ✅ Mandatory | Dropdown | Dropdown | Text |
| Rollback plan prepared | Dropdown | Dropdown | Dropdown: ✅ Mandatory | Dropdown | Dropdown | Text |
| Communication sent | Dropdown | Dropdown | Dropdown: ✅ Mandatory | Dropdown | Dropdown | Text |
| **Promotion Execution** | | | | | | |
| Version control tag created | Dropdown | Dropdown | Dropdown | Dropdown | Dropdown | Text |
| Build artifacts stored | Dropdown | Dropdown | Dropdown | Dropdown | Dropdown | Text |
| Deployment automated | Dropdown | Dropdown | Dropdown | Dropdown | Dropdown | Text |
| Deployment logged | Dropdown | Dropdown | Dropdown: ✅ Mandatory | Dropdown | Dropdown | Text |
| Configuration management | Dropdown | Dropdown | Dropdown | Dropdown | Dropdown | Text |
| **Post-Promotion Checks** | | | | | | |
| Smoke tests executed | Dropdown | Dropdown | Dropdown: ✅ Mandatory | Dropdown | Dropdown | Text |
| Functionality verified | Dropdown | Dropdown | Dropdown: ✅ Mandatory | Dropdown | Dropdown | Text |
| Performance validated | Dropdown | Dropdown | Dropdown | Dropdown | Dropdown | Text |
| Rollback tested | Dropdown | Dropdown | Dropdown | Dropdown | Dropdown | Text |
| Documentation updated | Dropdown | Dropdown | Dropdown: ✅ Mandatory | Dropdown | Dropdown | Text |

### CI/CD Pipeline Assessment (Rows 40-54)

| Pipeline Stage | Implemented | Tool/Platform | Automated Checks | Manual Gates | Compliance | Evidence |
|----------------|-------------|---------------|-----------------|--------------|------------|----------|
| Source control | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text (e.g., "Git") | Text | Text | Dropdown: ✅/⚠️/❌ | Text |
| Build automation | Dropdown | Text | Text | Text | Dropdown | Text |
| Unit testing | Dropdown | Text | Text | Text | Dropdown | Text |
| Code quality analysis | Dropdown | Text | Text | Text | Dropdown | Text |
| Security scanning (SAST) | Dropdown | Text | Text | Text | Dropdown | Text |
| Dependency scanning | Dropdown | Text | Text | Text | Dropdown | Text |
| Integration testing | Dropdown | Text | Text | Text | Dropdown | Text |
| Performance testing | Dropdown | Text | Text | Text | Dropdown | Text |
| Security testing (DAST) | Dropdown | Text | Text | Text | Dropdown | Text |
| Approval gates | Dropdown | Text | Text | Text | Dropdown | Text |
| Deployment automation | Dropdown | Text | Text | Text | Dropdown | Text |
| Post-deployment verification | Dropdown | Text | Text | Text | Dropdown | Text |

---

## Sheet 6: Production_Data_in_NonProd

### Purpose
Assess controls for production data usage in non-production environments per Control 8.33.

### Header Section
**Row 1:** "PRODUCTION DATA IN NON-PRODUCTION ENVIRONMENTS (Control 8.33)"  
**Row 2:** "Assessment of production data protection and anonymization controls"

### Policy & Governance (Rows 4-18)

| Requirement | Defined | Implementation | Responsible Role | Compliance | Evidence |
|-------------|---------|----------------|------------------|------------|----------|
| Production data in non-prod prohibited | Dropdown: ✅ Yes - Policy/⚠️ With Exceptions/❌ No Policy | Text | Text | Dropdown: ✅/⚠️/❌ | Text |
| Exceptions require formal approval | Dropdown: ✅ Yes/⚠️ Informal/❌ No | Text | Text | Dropdown | Text |
| DPO/Privacy officer involvement | Dropdown: ✅ Mandatory/⚠️ Recommended/❌ No/N/A | Text | Text | Dropdown | Text |
| Business justification required | Dropdown: ✅ Mandatory/⚠️ Recommended/❌ No | Text | Text | Dropdown | Text |
| Risk assessment performed | Dropdown: ✅ Mandatory/⚠️ Recommended/❌ No | Text | Text | Dropdown | Text |
| Time-limited approvals | Dropdown: ✅ Yes/⚠️ Informal/❌ No | Text | Text | Dropdown | Text |
| Regular access reviews | Dropdown: Monthly/Quarterly/Annually/Ad-hoc/None | Text | Text | Dropdown | Text |

### Data Anonymization Controls (Rows 20-42)

| Control | Implemented | Method/Tool | Effectiveness Tested | Compliance | Evidence |
|---------|-------------|------------|---------------------|------------|----------|
| **Anonymization Techniques** | | | | | |
| Data masking | Dropdown: ✅ Yes/⚠️ Partial/❌ No/N/A | Text (tool/method) | Dropdown: ✅ Yes/⚠️ Limited/❌ No | Dropdown: ✅/⚠️/❌ | Text |
| Data pseudonymization | Dropdown | Text | Dropdown | Dropdown | Text |
| Data generalization | Dropdown | Text | Dropdown | Dropdown | Text |
| Data perturbation | Dropdown | Text | Dropdown | Dropdown | Text |
| Data swapping/shuffling | Dropdown | Text | Dropdown | Dropdown | Text |
| Data subsetting (not full copy) | Dropdown | Text | Dropdown | Dropdown | Text |
| **PII/Sensitive Data** | | | | | |
| PII identified and classified | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Dropdown | Text |
| Names anonymized | Dropdown: ✅ Always/⚠️ Partial/❌ No/N/A | Text | Dropdown | Dropdown | Text |
| Email addresses anonymized | Dropdown | Text | Dropdown | Dropdown | Text |
| Phone numbers anonymized | Dropdown | Text | Dropdown | Dropdown | Text |
| Addresses anonymized | Dropdown | Text | Dropdown | Dropdown | Text |
| Financial data anonymized | Dropdown | Text | Dropdown | Dropdown | Text |
| Health data anonymized | Dropdown | Text | Dropdown | Dropdown | Text |
| **Re-identification Risk** | | | | | |
| Re-identification risk assessed | Dropdown: ✅ Yes/⚠️ Informal/❌ No | Text | Dropdown | Dropdown | Text |
| Linking attacks prevented | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Dropdown | Text |
| Quasi-identifiers removed | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Dropdown | Dropdown | Text |
| K-anonymity achieved | Dropdown: ✅ Yes/⚠️ Partial/❌ No/N/A | Text (k value) | Dropdown | Dropdown | Text |

### Current Production Data Usage (Rows 44-60)

| System/Application | Contains Prod Data | Data Type | Anonymized | Approval Date | Approved By | Review Date | Compliant | Evidence |
|-------------------|-------------------|-----------|------------|---------------|-------------|-------------|-----------|----------|
| [User fills in] | Dropdown: ✅ Yes/❌ No | Text (e.g., "Customer records") | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Date (DD.MM.YYYY) | Text | Date | Dropdown: ✅/⚠️/❌ | Text |

[15 rows for documenting systems with production data]

### Synthetic Data Generation (Rows 62-72)

| Capability | Available | Tool/Method | Data Types Supported | Usage | Compliance | Evidence |
|------------|-----------|-------------|---------------------|-------|------------|----------|
| Synthetic data generator | Dropdown: ✅ Yes/⚠️ Limited/❌ No | Text | Text | Dropdown: ✅ Primary/⚠️ Supplemental/❌ Not Used | Dropdown: ✅/⚠️/❌ | Text |
| Maintains referential integrity | Dropdown: ✅ Yes/⚠️ Partial/❌ No/N/A | Text | Text | Dropdown | Dropdown | Text |
| Realistic data distributions | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Text | Dropdown | Dropdown | Text |
| Supports edge cases | Dropdown: ✅ Yes/⚠️ Limited/❌ No | Text | Text | Dropdown | Dropdown | Text |
| Automated generation | Dropdown: ✅ Yes/⚠️ Partial/❌ Manual | Text | Text | Dropdown | Dropdown | Text |

---

## Sheet 7: Summary_Dashboard

### Purpose
Aggregate compliance metrics and identify gaps across all environment assessments.

### Header Section
**Row 1:** "ENVIRONMENT SEPARATION - SUMMARY DASHBOARD"  
**Row 2:** "Overall compliance status and key findings"

### Overall Compliance Summary (Rows 4-12)

| Assessment Area | Total Controls | Implemented | Partial | Not Implemented | Compliance % | Status |
|-----------------|---------------|-------------|---------|----------------|--------------|--------|
| Development Environment | Formula | Formula | Formula | Formula | Formula | Formula: Green/Yellow/Red |
| Test/QA Environment | Formula | Formula | Formula | Formula | Formula | Formula |
| Production Environment | Formula | Formula | Formula | Formula | Formula | Formula |
| Environment Promotion | Formula | Formula | Formula | Formula | Formula | Formula |
| Production Data Controls (8.33) | Formula | Formula | Formula | Formula | Formula | Formula |
| **OVERALL TOTAL** | Formula | Formula | Formula | Formula | Formula | Formula |

### Control 8.31 & 8.33 Mapping (Rows 14-28)

| ISO Control | Requirement Summary | Status | Evidence Sheet | Evidence Row | Auditor Notes |
|-------------|-------------------|--------|----------------|--------------|---------------|
| 8.31 - Env Sep | Development environment isolated | Formula: ✅/⚠️/❌ | Text | Text | Text (editable) |
| 8.31 - Env Sep | Test environment isolated | Formula | Text | Text | Text |
| 8.31 - Env Sep | Production environment isolated | Formula | Text | Text | Text |
| 8.31 - Env Sep | Segregation of duties enforced | Formula | Text | Text | Text |
| 8.32 - Changes | Changes tested before production | Formula | Text | Text | Text |
| 8.32 - Changes | Promotion procedures documented | Formula | Text | Text | Text |
| 8.33 - Test Data | Prod data in non-prod prohibited/controlled | Formula | Text | Text | Text |
| 8.33 - Test Data | Anonymization performed | Formula | Text | Text | Text |
| 8.33 - Test Data | Re-identification risk assessed | Formula | Text | Text | Text |
| 8.33 - Test Data | DPO approval obtained | Formula | Text | Text | Text |

### Critical Findings (Rows 30-35)

| Finding Type | Count | Description |
|--------------|-------|-------------|
| Critical Gaps | Formula (count ❌) | Text area (auto-populate key gaps) |
| High-Priority Items | Formula (count ⚠️) | Text area |
| Planned Improvements | Formula (count 📋) | Text area |

### Environment Separation Metrics (Rows 37-46)

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Network isolation (all environments) | Text (e.g., "100%") | Formula | Formula | Text |
| MFA enforcement (production) | Text (e.g., "100%") | Formula | Formula | Text |
| Developer access to production | Text (e.g., "0% direct") | Formula | Formula | Text |
| Production data in non-prod (unauthorized) | Text (e.g., "0 instances") | Formula | Formula | Text |
| Anonymization effectiveness | Text (e.g., ">95%") | Text | Formula | Text |
| Change promotion success rate | Text (e.g., ">95%") | Text | Formula | Text |

### Audit Readiness Assessment (Rows 48-56)

| Criterion | Status | Notes |
|-----------|--------|-------|
| All environments documented | Formula: ✅/⚠️/❌ | Text |
| Network isolation verified | Formula | Text |
| Access controls implemented | Formula | Text |
| Promotion procedures documented | Formula | Text |
| Production data controls (8.33) compliant | Formula | Text |
| Evidence available for all controls | Formula | Text |
| Compliance ≥70% | Formula | Text |
| **OVERALL AUDIT READINESS** | Formula | Text |

---

## Sheet 8: Evidence_Register

### Purpose
Centralized evidence repository linking to all supporting documentation.

### Header Section
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document all evidence supporting this assessment"

### Evidence Inventory (Rows 4-103, 100 rows)

| Evidence ID | Evidence Type | Description | Related Sheet/Control | Location/Path | Date Collected | Collected By | Verification Status | Auditor Notes |
|-------------|---------------|-------------|----------------------|---------------|----------------|--------------|-------------------|---------------|
| EV-001 | Dropdown: Network Diagram/Access Matrix/Procedure/Config Export/Policy/Approval/Test Results/Audit Report/Other | Text | Dropdown: (all sheets + Controls 8.31/8.32/8.33) | Text | Date (DD.MM.YYYY) | Text | Dropdown: ✅ Verified/⚠️ Pending/❌ Not Verified | Text |

[100 rows for evidence tracking with alternating row colors]

**Column Widths:**
- Evidence ID: 12
- Evidence Type: 20
- Description: 40
- Related Sheet/Control: 25
- Location/Path: 30
- Date Collected: 15
- Collected By: 20
- Verification Status: 18
- Auditor Notes: 30

---

## Sheet 9: Approval_Sign_Off

### Purpose
Formal approval workflow for completed assessment.

### Assessment Summary Section (Rows 3-10)
```
Assessment Document:        ISMS-IMP-A.8.32.3 - Environment Separation Assessment
Assessment Period:          [USER INPUT - date range]
Assessment Scope:           [USER INPUT - text]
Overall Compliance Rate:    [Formula from Summary_Dashboard]
Critical Gaps:              [Formula from Summary_Dashboard]
Control 8.31 Compliance:    [Formula from Summary_Dashboard]
Control 8.33 Compliance:    [Formula from Summary_Dashboard]
Audit Readiness:            [Formula from Summary_Dashboard]
Assessment Status:          [Dropdown: ✅ Final/⚠️ Requires Remediation/📋 Draft/❌ Re-assessment Required]
```

### Assessment Completed By (Rows 12-20)
```
Name:               [USER INPUT]
Role/Title:         [USER INPUT]
Department:         [USER INPUT]
Email:              [USER INPUT]
Phone:              [USER INPUT]
Date Completed:     [USER INPUT - date picker, format DD.MM.YYYY]
Signature:          [USER INPUT]
```

### Reviewed By - Infrastructure/Security Manager (Rows 22-30)
```
Name:                   [USER INPUT]
Role/Title:             [USER INPUT]
Review Date:            [USER INPUT - date picker, format DD.MM.YYYY]
Review Notes:           [Text area - merged cells]
Recommendation:         [Dropdown: ✅ Approve/⚠️ Approve with Conditions/❌ Reject/📋 Require Rework]
Conditions (if any):    [Text area]
Signature:              [USER INPUT]
```

### Approved By - CISO (Rows 32-40)
```
Name:                   [USER INPUT]
Role/Title:             [USER INPUT]
Approval Date:          [USER INPUT - date picker, format DD.MM.YYYY]
Approval Decision:      [Dropdown: ✅ Approved/⚠️ Approved with Conditions/❌ Rejected]
Conditions/Notes:       [Text area]
Signature:              [USER INPUT]
```

### Next Review Details (Rows 42-48)
```
Next Review Date:               [Date - auto-calculate +3 months from Approval Date]
Review Responsible:             [USER INPUT]
Special Considerations:         [Text area]
Regulatory Review Required:     [Dropdown: Yes/No/To Be Determined]
External Audit Scheduled:       [Date]
```

---

## Cell Styling Reference

### Header Styles
- **Main Header (Row 1):** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Alignment: centered/wrapped, Height: 40px
- **Subheader (Row 2):** Font: Calibri 11pt bold white, Fill: 4472C4 (medium blue), Alignment: centered/wrapped, Height: 25px
- **Section Header:** Font: Calibri 11pt bold white, Fill: 4472C4 (light blue), Alignment: center, Height: 20px
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (light gray), Alignment: centered/wrapped, Border: thin all sides

### Input Cell Styles
- **Editable (User Input):** Fill: FFFFCC (light yellow), Border: thin black, Alignment: left/wrap
- **Calculated/Formula:** Fill: E0E0E0 (light gray), Border: thin black, Protection: locked
- **Dropdown:** Fill: FFFFCC (light yellow), Border: thin black, Data validation applied

### Status Color Coding
- **✅ Implemented/Compliant:** C6EFCE (light green)
- **⚠️ Partial/Requires Attention:** FFEB9C (light yellow)
- **❌ Not Implemented/Non-Compliant:** FFC7CE (light red)
- **📋 Planned:** B4C7E7 (light blue)
- **N/A:** F2F2F2 (light gray)

---

## Freeze Panes

- **All assessment sheets:** Freeze at row 4 (headers remain visible during scrolling)
- **Evidence Register:** Freeze at row 5
- **Approval Sign-Off:** Freeze at row 3

---

## File Naming Convention

**Format:** `ISMS_A_8_32_3_Environment_Separation_Assessment_YYYYMMDD.xlsx`

**Examples:**
- `ISMS_A_8_32_3_Environment_Separation_Assessment_20260115.xlsx`
- `ISMS_A_8_32_3_Environment_Separation_Assessment_20260401_FINAL.xlsx`

---

## Quarterly Review Cycle

### Review Checklist
1. ☐ Review environment architecture changes
2. ☐ Verify network isolation controls remain effective
3. ☐ Review access control matrices (all environments)
4. ☐ Validate production data controls (Control 8.33)
5. ☐ Review anonymization effectiveness
6. ☐ Update promotion procedures if changed
7. ☐ Recalculate compliance metrics
8. ☐ Add new evidence entries
9. ☐ Address any identified gaps
10. ☐ Update approval sign-off with quarterly review notes

### Triggers for Ad-Hoc Review
- New environment deployment
- Network architecture changes
- Access control policy changes
- Production data breach/incident
- Audit findings related to environment separation
- Control 8.33 exceptions granted
- Regulatory requirement changes (GDPR, etc.)

---

## Integration Points

### Related ISMS Documents
- **ISMS-POL-A.8.32-S2.3:** Testing & Validation Requirements
- **ISMS-POL-A.8.31:** Separation of Development, Test, and Production Environments
- **ISMS-POL-A.8.33:** Test Information (Production Data Protection)
- **ISMS-IMP-A.8.32.1:** Change Process Assessment
- **ISMS-IMP-A.8.32.2:** Change Types & Categories
- **ISMS-IMP-A.8.32.4:** Testing & Validation Assessment
- **ISMS-IMP-A.8.32.5:** Compliance Dashboard (consolidates this data)

### Related ISO 27001:2022 Controls
- **Control 5.18:** Access rights (environment-specific access control)
- **Control 8.2:** Privileged access rights (production access)
- **Control 8.3:** Information access restriction
- **Control 8.11:** Data masking (Control 8.33 implementation)
- **Control 8.19:** Software installation (production change control)

### External Integrations
- **Identity & Access Management (IAM):** Environment-specific role definitions
- **Network Security:** Firewall rules, VLAN configuration
- **Change Management System:** Promotion procedures
- **Data Loss Prevention (DLP):** Production data exfiltration detection
- **SIEM:** Environment access monitoring
- **CI/CD Pipeline:** Automated promotion controls

### Audit Trail Requirements
- All environment configurations documented and versioned
- Access control matrices maintained for each environment
- Promotion procedures documented with approval records
- Production data usage exceptions documented with DPO approval
- Anonymization testing results maintained
- Network isolation verified through penetration testing

---

**END OF SPECIFICATION**

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*  
— Richard Feynman

**Environment Separation Maturity Indicator:** If developers cannot directly access or deploy to production, and if production data never appears in non-production environments without proper anonymization, you've achieved operational security excellence. ✅
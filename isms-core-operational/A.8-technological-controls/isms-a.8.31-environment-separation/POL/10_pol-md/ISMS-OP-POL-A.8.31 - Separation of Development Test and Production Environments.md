**ISMS-OP-POL-A.8.31 — Separation of Development, Test and Production Environments**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Separation of Development, Test and Production Environments |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.31 |
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
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.8.31 — Separation of development, test and production environments
- ISO/IEC 27002:2022 Section 8.31 — Implementation guidance for environment separation
- NIST SP 800-53 Rev 5 — CM-4 (Impact Analyses), CM-7 (Least Functionality), SA-11 (Developer Testing), SC-32 (System Partitioning)
- CIS Controls v8 — Safeguard 16.1–16.14 (Application Software Security)

**Related Annex A Controls**:

| Control | Relationship to Environment Separation |
|---------|----------------------------------------|
| A.5.15–16–18 Identity and access management | Foundational IAM framework; role-based access per environment tier |
| A.5.34 Privacy and PII | Test data containing personal data requires anonymisation or synthetic substitution |
| A.8.2–3–5 Authentication and privileged access | MFA for production access; privileged access management for break-glass |
| A.8.4 Access to source code | Repository access controls and branch protection feed into promotion workflows |
| A.8.9 Configuration management | Environment-specific configuration baselines and drift detection |
| A.8.11 Data masking | Techniques for protecting data used in non-production environments |
| A.8.15 Logging | Audit logging for environment access, promotions, and break-glass events |
| A.8.25–26–29 Secure development lifecycle | SDLC integration; security testing gates between environments |
| A.8.32 Change management | Change Advisory Board approval for production deployments |
| A.8.33 Test information | Protection and management of test data across environments |

**Related Internal Policies**:

- Identity and Access Management Policy
- Secure Development Lifecycle Policy
- Change Management Policy
- Logging and Monitoring Policy
- Data Classification and Handling Policy
- Privacy and Personal Data Protection Policy

---

# Separation of Development, Test and Production Environments Policy

## Purpose

The purpose of this policy is to ensure that development, testing, and production environments are separated and secured to reduce the risk of unauthorised access to or changes in the production environment. Environment separation protects business operations from development and testing activities that may introduce errors, vulnerabilities, or unauthorised modifications to live systems and data.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data processed in production environments, and by prohibiting the use of production personal data in development and testing environments without equivalent protection controls. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements also apply. Environment separation is a key technical measure for demonstrating that systems processing personal data are subject to appropriate access restrictions and data handling controls.

## Scope

All information systems, applications, and infrastructure operated, managed, or controlled by the organisation and deemed in scope by the ISO 27001 scope statement. This includes:

- All environment tiers: development, testing/QA, staging/pre-production, and production.
- All hosting models: on-premises, cloud ([Cloud Provider] — e.g., AWS, Azure, GCP, or equivalent), hybrid, and container-based infrastructure ([Container Platform] — e.g., Kubernetes, Docker Swarm, or equivalent).
- All CI/CD pipelines ([CI/CD Platform] — e.g., GitHub Actions, GitLab CI, Jenkins, Azure DevOps, or equivalent) that promote changes between environments.
- Third-party managed systems processing organisational data where the organisation retains environment management responsibility.

All employees, contractors, and third-party users with access to any environment.

**Out of scope**: Single-user isolated research environments not connected to organisational networks; temporary proof-of-concept systems containing no organisational or personal data; vendor demonstration systems managed entirely by vendors. Once research or proof-of-concept systems transition to organisational use, they shall comply with this policy.

## Principle

Development, testing, and production environments shall be separated to protect the integrity, availability, and confidentiality of production systems and data. Changes shall flow through defined promotion paths with appropriate review and approval at each stage. No single individual shall have the ability to make changes to both development and production without prior review and approval. The level of separation shall be commensurate with the risk to business operations and the sensitivity of data processed.

The organisation shall centrally administer environment access using role-based access controls. Default access to production environments shall be "no access" — explicit grant is required for any access level. Developers shall not have standing access to production infrastructure.

---

## Environment Definitions

The organisation shall maintain the following environment tiers at minimum. Each tier shall have a defined purpose, dedicated infrastructure resources, documented data handling restrictions, and enforced access controls.

**Environment Tiers**:

| Environment | Purpose | Data Permitted | Access |
|-------------|---------|----------------|--------|
| **Development** | Active code development, experimentation, integration | Synthetic data only; no production data | Developers (full); QA (read); Operations (as needed) |
| **Testing / QA** | Quality assurance, integration testing, user acceptance testing | Synthetic or anonymised data (DPO-approved) | QA team (full); Developers (limited); Operations (as needed) |
| **Staging / Pre-production** | Final validation before production release; mirrors production configuration | Synthetic or anonymised data; production configuration (not data) | Operations (full); QA (read); Developers (read-only monitoring) |
| **Production** | Live business operations serving real users with real business data | Production data (real business and personal data) | Operations (full); Developers (no standing access; break-glass only) |
| **Sandbox** (optional) | Isolated experimentation, technology evaluation, proof-of-concept | Synthetic data only; no network connectivity to other environments | Developers (full); no connectivity to production networks |

Environment names and visual labels shall clearly identify the environment type (e.g., colour-coded banners, hostname prefixes, console labels) to prevent accidental operations in the wrong environment.

---

## Network Separation

Environments shall be isolated through network segmentation to prevent unintended cross-environment data flows and access.

**Network Separation Requirements**:

| Requirement | Standard |
|-------------|----------|
| Network isolation | Each environment on a separate network segment, VLAN, VPC, or equivalent |
| Default traffic rule | Deny-all between environments; only controlled promotion paths permitted |
| Production-to-development connectivity | Prohibited — no direct network path between production and development |
| Firewall rules | Documented, reviewed quarterly, and restricted to minimum necessary flows |
| DNS separation | Separate DNS zones or namespaces per environment to prevent cross-environment resolution |

**Cloud Environment Separation**:

Where the organisation uses cloud infrastructure, environment separation shall be implemented using the cloud provider's account or subscription boundary model:

| Cloud Provider | Separation Mechanism |
|----------------|---------------------|
| AWS | Separate AWS accounts per environment within an AWS Organisation |
| Azure | Separate subscriptions per environment within a Management Group |
| GCP | Separate projects per environment within an Organisation |
| Multi-cloud | Consistent separation model documented per provider |

**Container and Kubernetes Separation**:

Where the organisation uses container orchestration platforms, environments shall be separated using:

- Separate clusters per environment (preferred for production isolation).
- Namespace-level separation with enforced network policies for non-production environments.
- Production workloads shall not share a cluster with development or testing workloads.
- Container image registries shall be separated or access-controlled per environment.

---

## Access Control per Environment

Access to each environment shall follow the principle of least privilege. Access rights shall be defined per role and environment tier.

**Access Matrix**:

| Role | Development | Testing / QA | Staging | Production |
|------|-------------|-------------|---------|------------|
| **Developer** | Full access | Read + deploy to test | Read-only | No standing access |
| **QA Engineer** | Read | Full access | Read + execute tests | No access |
| **Operations / SRE** | As needed | As needed | Full access | Full access |
| **Database Administrator** | As needed | As needed | As needed | Full access (with PAM) |
| **Security Team** | Read (audit) | Read (audit) | Read (audit) | Read (audit + monitoring) |
| **External Contractor** | Scoped to project | Scoped to project | No access | No access |

**Production Access Restrictions**:

- Developers shall not have standing access to production infrastructure, databases, or application consoles.
- All production access shall require multi-factor authentication.
- Production access sessions shall be logged, recorded, and monitored.
- Privileged production access shall be managed through a Privileged Access Management (PAM) system ([PAM Tool] — e.g., CyberArk, HashiCorp Boundary, AWS SSM Session Manager, or equivalent).

**Emergency Access (Break-Glass)**:

Emergency developer access to production shall be permitted only during declared incidents where developer expertise is required for resolution. Break-glass access shall:

- Require approval from the Incident Commander and CISO (or delegate).
- Be time-limited to a maximum of 8 hours, renewable with re-approval.
- Be purpose-limited to the declared incident scope.
- Be logged with: incident identifier, requesting developer, approving authority, access duration, systems accessed, and actions performed.
- Trigger a mandatory post-incident review within 7 days of incident closure.

Break-glass activations shall be reviewed monthly by the Information Security Manager and reported in the quarterly CISO dashboard with trend analysis.

**Access Reviews**:

| Environment | Review Frequency |
|-------------|-----------------|
| Production | Quarterly |
| Staging | Semi-annually |
| Development / Testing | Annually |

Terminated employee access shall be revoked within the same business day across all environments. Automated deprovisioning via the identity management system is preferred.

---

## Data Handling Rules

Production data shall not be used in development or testing environments. This requirement protects business-critical data from exposure in less-controlled environments and supports nFADP compliance for personal data.

**Production Data Prohibition**:

- Production data shall not be copied, exported, restored, or replicated to development, testing, or staging environments.
- Production database backups shall not be restored in non-production environments.
- Production credentials, API keys, connection strings, and secrets shall not be used in non-production environments.
- Log files containing production personal data shall not be transferred to non-production environments without anonymisation.

**Approved Data Sources for Non-Production**:

| Data Source | Approval Required | Restrictions |
|-------------|-------------------|-------------|
| **Synthetic data** (generated, not derived from production) | No additional approval | Preferred method; structurally representative but entirely artificial |
| **Anonymised data** (irreversibly de-identified from production) | Data Protection Officer approval | Anonymisation shall be irreversible; validated against re-identification risk; deleted within 30 days of project completion |
| **Pseudonymised data** (reversibly de-identified) | CISO and DPO approval; treated as personal data under nFADP | Acceptable only where anonymisation or synthetic data is technically infeasible; equivalent security controls required |
| **Subset of production structure** (schema only, no data) | Development Manager approval | Database schemas, API contracts, configuration templates without data values |

Under the Swiss nFADP (revDSG), pseudonymised data remains personal data for any party that holds or can access the pseudonymisation key. Fully anonymised data — where re-identification is not possible by any reasonable means — falls outside the scope of the FADP.

**Data Classification Enforcement**:

- Confidential and Restricted data classifications shall be prohibited in development and testing environments.
- Automated scanning shall be implemented to detect prohibited production data patterns (e.g., real names, national identifiers, financial account numbers) in non-production environments. Scanning shall cover databases, file systems, log files, and container images.
- Violations shall be remediated within 7 days of detection and reported to the Information Security Manager.

---

## Test Data Management

Test data shall be managed as a controlled asset throughout the software development lifecycle.

**Test Data Principles**:

- Synthetic data shall be the default and preferred approach for all testing activities.
- Test data shall be structurally representative of production data (same schema, data types, relationships, and volume characteristics) without containing real personal or business data.
- Test data generation shall be automated where practicable using [Test Data Tool] (e.g., Faker, Mockaroo, Tonic.ai, Delphix, or equivalent).
- Test data shall be versioned and reproducible to support regression testing.
- Test data shall be purged from non-production environments within 30 days of project completion or test cycle conclusion.

**Anonymisation Validation**:

Where anonymised production data is approved for non-production use, the anonymisation process shall be validated before each use:

1. Data Protection Officer shall verify that direct identifiers have been removed or replaced.
2. Quasi-identifier combinations shall be assessed for re-identification risk.
3. Validation results shall be documented and retained for audit purposes.
4. Failed validation shall result in rejection and remediation before data can be used.

**Card Holder Data**: Card holder data (PAN, CVV, track data) shall never be used in development or testing environments, regardless of anonymisation status. Synthetic card numbers conforming to test ranges shall be used instead.

---

## Code Promotion Process

Changes shall follow a defined promotion path from development to production. Direct deployment to production shall be prohibited except for approved emergency fixes.

**Standard Promotion Path**:

```
Development → Testing / QA → Staging → Production
```

Each promotion step shall include defined quality and security gates.

**Promotion Gate Requirements**:

| Gate | From → To | Requirements |
|------|-----------|-------------|
| **Gate 1** | Development → Testing | Code review completed (minimum 1 reviewer, not the author); automated unit tests pass; static analysis scan pass; no critical or high vulnerabilities |
| **Gate 2** | Testing → Staging | Integration tests pass; QA sign-off; security testing complete (SAST, DAST where applicable); performance testing pass for critical systems |
| **Gate 3** | Staging → Production | Change Advisory Board approval (per A.8.32); rollback plan documented and tested; production backup verified; deployment runbook reviewed; approval from system owner |

**Separation of Duties in Promotion**:

- The developer who writes the code shall not be the same person who approves its promotion to production.
- The person who promotes code to staging shall not be the same person who promotes it to production, where team size permits.
- CI/CD pipeline credentials for production deployment shall be restricted to the operations team.

**CI/CD Pipeline Security**:

- Pipeline definitions shall be version-controlled and subject to code review.
- Pipeline credentials and secrets shall be stored in the pipeline platform's secret store — not hardcoded in pipeline definitions.
- Each environment shall have dedicated pipeline credentials with minimum required permissions.
- Pipeline execution logs shall be retained for audit purposes (minimum 1 year).
- Artifacts shall be built once and promoted through environments (immutable artifacts) — not rebuilt per environment.

**Emergency Deployments**:

Emergency fixes may bypass the standard promotion path under the following conditions:

- A declared incident or critical security vulnerability requiring immediate remediation.
- Approval from Incident Commander (or on-call manager) and CISO (or delegate).
- Post-implementation review within 48 hours, including retrospective testing in all skipped environments.
- Documentation of the emergency in the change management system with justification for bypassing gates.

**Rollback Capability**:

- Previous versions shall be retained to support rollback.
- Rollback procedures shall be documented and tested at least quarterly.
- The operations team shall be authorised to execute rollbacks without additional approval during incidents.
- Production environments shall be backed up before each deployment to facilitate rollback.
- Test data and development artefacts shall be removed before promotion to production.

---

## Configuration Separation

Environment configurations shall be managed to prevent credential leakage, cross-environment contamination, and configuration drift.

**Configuration Separation Requirements**:

| Requirement | Standard |
|-------------|----------|
| Credentials and secrets | Unique per environment; stored in a secrets manager ([Secrets Manager] — e.g., HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, or equivalent) |
| Database connection strings | Environment-specific; never shared across tiers |
| API endpoints | Environment-specific URLs; no hardcoded production endpoints in non-production code |
| Feature flags | Environment-specific configuration; production flags managed separately from development |
| Infrastructure as Code | Environment configurations stored in version control; changes follow the same promotion path as application code |

**Configuration Parity**:

- Staging environments shall mirror production configuration as closely as possible (same software versions, same infrastructure sizing within budget constraints, same security controls).
- Configuration drift between staging and production shall be detected and reported. Drift detection shall be performed at least weekly.
- Differences between staging and production shall be documented, justified, and approved by the IT Operations Manager.

**Environment Identification**:

- Each environment shall display clear visual identification to prevent accidental operations in the wrong environment.
- Hostname prefixes, console banners, browser tab labels, and colour-coded UI elements shall distinguish environment tiers.
- Production environments shall display prominent identification (e.g., red banners, "[PRODUCTION]" labels).

---

## Cloud Environment Separation

Where the organisation operates in a cloud or multi-cloud environment, the following additional controls apply.

**Account and Subscription Isolation**:

- Production workloads shall reside in dedicated cloud accounts, subscriptions, or projects — separate from all non-production workloads.
- IAM policies shall prevent cross-account access except through explicitly defined, audited roles.
- Service control policies (SCPs), Azure Policies, or organisation policies shall enforce environment boundaries at the organisational level.
- Billing shall be separated per environment to enable cost attribution and anomaly detection.

**Cloud Resource Tagging**:

All cloud resources shall be tagged with environment identification (e.g., `env:production`, `env:staging`, `env:development`) to support:

- Automated policy enforcement (e.g., prevent production data services from being accessed by development roles).
- Cost allocation and reporting per environment.
- Compliance scanning and audit reporting.

**Infrastructure as Code Governance**:

- Infrastructure definitions shall be stored in version-controlled repositories.
- Infrastructure changes shall follow the same promotion workflow as application code (develop, review, test, deploy).
- Manual changes to production infrastructure ("ClickOps") shall be prohibited; all changes shall be applied through the CI/CD pipeline.

---

## Definitions

| Term | Definition |
|------|------------|
| **Anonymisation** | Irreversible process of removing personal data such that individuals cannot be re-identified by any reasonable means; anonymised data is not personal data under nFADP |
| **Break-glass access** | Emergency procedure allowing time-limited, approved production access to personnel who do not have standing production access |
| **Change Advisory Board (CAB)** | Cross-functional group that reviews and approves changes to production environments |
| **CI/CD pipeline** | Automated workflow that builds, tests, and deploys software changes through environment tiers |
| **Configuration drift** | Unintended divergence between the intended configuration (as defined in code or documentation) and the actual running configuration of an environment |
| **Immutable artifact** | A software build artifact that is created once and promoted unchanged through all environments, ensuring consistency |
| **MFA** | Multi-factor authentication — requiring two or more verification factors to gain access |
| **PAM** | Privileged Access Management — system for managing, monitoring, and securing access to privileged accounts and credentials |
| **Production environment** | Live operational environment serving real users with real business data |
| **Promotion** | Process of moving changes from one environment tier to another through a defined, controlled workflow |
| **Pseudonymisation** | Reversible process of replacing identifying data with pseudonyms; pseudonymised data remains personal data under nFADP for any party that can access the re-identification key |
| **Staging environment** | Pre-production environment that mirrors production configuration for final validation before release |
| **Synthetic data** | Artificially generated data that maintains the statistical and structural properties of production data without containing any real personal or business information |

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; approval of environment separation exceptions; break-glass approval authority; quarterly compliance review; annual policy review; reporting to Executive Management |
| **CTO / Development Manager** | Development and testing environment management; CI/CD pipeline implementation; promotion workflow enforcement; developer training on environment separation; resource allocation for environment infrastructure |
| **IT Operations Manager** | Production environment security; production access approval; PAM management; deployment execution; rollback procedures; infrastructure monitoring; configuration drift detection |
| **Information Security Manager** | Policy maintenance; compliance assessments; break-glass review; exception review; security monitoring; incident investigation; quarterly compliance reporting to CISO |
| **Data Protection Officer (DPO)** | Anonymisation approval for non-production data use; re-identification risk assessment; test data compliance with nFADP; data handling audit |
| **QA Team Lead** | Testing environment management; test data lifecycle management; test environment integrity; QA sign-off for promotion gates |
| **System Owners** | Environment architecture documentation; compliance evidence for owned systems; exception reporting; promotion approval for their systems |
| **Developers** | Use assigned environments only; follow data handling requirements; use defined promotion workflows; report environment violations; complete environment separation training |
| **Security Team** | Environment access log monitoring; production data scanning in non-production; violation investigation; security assessment of environment separation controls |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Environment inventory** with tier classification, hosting model, network segmentation details, and responsible owner | IT Operations Manager | Maintained continuously; reviewed annually | Life of environment + 3 years |
| 2 | **Network segmentation documentation** (firewall rules, VPC configurations, VLAN assignments) with quarterly review records | IT Operations Manager / Network Team | Quarterly | 3 years |
| 3 | **Access control matrices** per environment tier with role-to-permission mappings | IT Operations Manager / Development Manager | Maintained continuously; reviewed per access review schedule | 3 years |
| 4 | **Access review records** (production quarterly, staging semi-annually, dev/test annually) | System Owners / IT Operations Manager | Per schedule | 3 years |
| 5 | **Break-glass activation logs** with incident identifier, approver, duration, actions, and post-incident review | Information Security Manager | Per event; monthly review | 3 years |
| 6 | **CI/CD pipeline configuration** showing promotion gates, approval requirements, and separation of duties | Development Manager / DevOps | Maintained continuously; reviewed quarterly | 2 years |
| 7 | **Production deployment records** with CAB approval, rollback plan, and deployment outcome | IT Operations Manager | Per deployment | 3 years |
| 8 | **Test data management records** (synthetic data generation logs, anonymisation approvals, data purge confirmations) | QA Team Lead / DPO | Per test cycle | 3 years |
| 9 | **Non-production data scanning results** showing no production data detected (or remediation records for violations) | Security Team | Weekly scan; monthly reporting | 2 years |
| 10 | **Configuration drift reports** between staging and production with resolution records | IT Operations Manager | Weekly detection; quarterly review | 2 years |
| 11 | **Cloud account/subscription separation documentation** with IAM policy exports and service control policies | IT Operations Manager / Cloud Team | Quarterly | 3 years |
| 12 | **Exception register** (requests, approvals, compensating controls, expiration dates, quarterly reviews) | Information Security Manager | Maintained continuously; reviewed quarterly | Exception duration + 3 years |
| 13 | **Environment separation training records** for developers, QA, and operations staff | CISO / HR | Annually | Employment duration + 3 years |
| 14 | **Emergency deployment records** with justification for bypassing standard promotion path and post-implementation review | IT Operations Manager / Development Manager | Per event | 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, environment access reports, network segmentation audits, CI/CD pipeline configuration reviews, data scanning reports, deployment approval records, access review completion records, internal and external audits, and feedback to the policy owner.

**Compliance Metrics**:

| Metric | Target | Measurement Frequency |
|--------|--------|-----------------------|
| Environments with compliant network separation (deny-all default, no dev-to-prod path) | 100% | Quarterly |
| Production access restricted to authorised operations personnel (no standing developer access) | 100% | Quarterly |
| Production deployments with CAB approval and documented rollback plan | >= 95% | Monthly |
| Non-production environments with no production data detected (scanning clean) | >= 95% | Monthly |
| Break-glass activations with complete documentation and post-incident review | 100% | Per event |
| Access reviews completed on schedule per environment tier | >= 90% | Quarterly |
| CI/CD pipelines enforcing promotion gates and separation of duties | >= 95% | Quarterly |
| Test data purged within 30 days of project completion | >= 90% | Quarterly |

**Compliance Scoring**:

| Component | Weight | Calculation |
|-----------|--------|-------------|
| Network Separation Compliance | 25% | (Environments with compliant network separation) / Total environments x 100 |
| Access Control Compliance | 25% | (Environments with correct role-based access + completed reviews) / Total x 100 |
| Promotion Process Compliance | 25% | (Compliant production deployments with approval + rollback plan) / Total deployments x 100 |
| Data Handling Compliance | 25% | (Non-production environments with no production data + test data purged on schedule) / Total x 100 |

**Non-Compliance Handling**: Below 70% requires immediate CISO escalation and remediation plan. 70-89% requires Information Security Manager oversight with monthly reviews. 90% and above follows standard quarterly monitoring.

**Remediation Ownership by Score Component**:

| Component | Below Target | Remediation Owner | Escalation |
|-----------|-------------|-------------------|------------|
| Network Separation Compliance | <100% | IT Operations Manager | CISO at 15 days overdue |
| Access Control Compliance | <100% (production) | IT Operations Manager / Development Manager | CISO at 15 days overdue |
| Promotion Process Compliance | <95% | Development Manager / DevOps | CISO at 30 days overdue |
| Data Handling Compliance | <95% | QA Team Lead / DPO | CISO immediately if production personal data found in non-production |

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum 12 months). Exceptions shall be reported to the Management Review Team.

Exceptions may be approved only for: legacy systems scheduled for decommission within 12 months; technical limitations where full separation is not feasible (with documented justification and compensating controls); and temporary exceptions during migration or transformation projects (with defined end date).

When exceptions are approved, compensating controls shall include one or more of: enhanced access logging and monitoring, mandatory code review for all changes, read-only access restrictions, data masking requirements, increased change management rigour, and more frequent security assessments.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Policy violations shall be documented, investigated by the Information Security Manager, and reported to the CISO.

Violations involving production data exposure in non-production environments shall be treated as data incidents and reported to the Data Protection Officer for assessment under nFADP breach notification requirements.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to cloud and container platform capabilities, emerging threats to environment separation (supply chain attacks, CI/CD pipeline compromise, container escape vulnerabilities), regulatory changes (nFADP, GDPR), audit findings, and lessons learned from break-glass activations and environment incidents.

---

# Areas of the ISO 27001 Standard Addressed

Separation of Development, Test and Production Environments Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 8.9 Configuration management |
| | 8.11 Data masking |
| | 8.25 Secure development lifecycle |
| | **8.31 Separation of development, test and production environments** |
| | 8.32 Change management |
| | 8.33 Test information |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data protection; environment separation as a technical measure; prohibition of production personal data in non-production environments without equivalent controls |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security; environment access controls as a security measure |
| EU GDPR (where applicable) | Art. 25 — Data protection by design and by default (environment separation); Art. 32 — Security of processing (access control per environment) |
| ISO/IEC 27001:2022 | Annex A Control 8.31 — Separation of development, test and production environments |
| ISO/IEC 27002:2022 | Section 8.31 — Implementation guidance for environment separation |
| NIST SP 800-53 Rev 5 | CM-4 (Impact Analyses), CM-7 (Least Functionality), SA-11 (Developer Testing and Evaluation), SC-32 (System Partitioning) |
| CIS Controls v8 | 4.1 (Secure Configuration of Enterprise Assets), 16.1–16.4 (Application Software Security) |

---

<!-- QA_VERIFIED: 2026-02-07 -->

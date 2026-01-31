# ISMS-POL-A.8.28-S2.4
## Secure Coding - Third-Party & Open Source Software Management

**Document ID**: ISMS-POL-A.8.28-S2.4
**Title**: Secure Coding - Third-Party & Open Source Software Management  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead / Legal/Compliance Officer | Initial third-party and OSS management requirements |

**Review Cycle**: Annual (or upon significant supply chain incidents or regulatory changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Application Security Lead
- Legal Review: Legal/Compliance Officer
- Procurement Review: Procurement/Vendor Management Lead

**Distribution**: Developers, security team, legal/compliance, procurement, architecture teams  
**Related Documents**: ISMS Vendor Management Policy, ISMS-POL-A.8.28-S2.3 (Testing Requirements - SCA), ISMS-IMP-A.8.28.4 (Third-Party & OSS Assessment)

---

## 2.4.1 Introduction

This section establishes requirements for managing **third-party and open-source software (OSS) components**, addressing supply chain security risks that have become a critical attack vector.

*"We shape our tools and thereafter our tools shape us."* - Marshall McLuhan

**Application to Software Supply Chain**: Modern applications are predominantly assembled from third-party components. A 2023 Synopsys study found that 96% of codebases contain open-source software, with an average of 76% of code being from external sources. We don't just write code anymore - we integrate, orchestrate, and maintain an ecosystem of dependencies. Supply chain security is not optional.

**Key Supply Chain Risks**:
- **Known Vulnerabilities**: Dependencies with publicly disclosed CVEs
- **Malicious Packages**: Intentionally compromised packages (typosquatting, dependency confusion)
- **Abandoned Projects**: Unmaintained components with unpatched vulnerabilities
- **License Violations**: Incompatible licenses creating legal/compliance risk
- **Transitive Dependencies**: Vulnerabilities in dependencies-of-dependencies
- **Build-Time Attacks**: Compromised build tools or package managers

**Primary Stakeholders**: Developers, Security Team, Legal/Compliance, Procurement

---

## 2.4.2 Software Composition Analysis (SCA)

### 2.4.2.1 SCA Tool Requirements

**REQ-2.4.2.1-A: SCA Tool Deployment**

Organizations **MUST** deploy Software Composition Analysis (SCA) tooling that:
- Identifies all direct and transitive dependencies
- Scans dependencies against vulnerability databases (NVD, GitHub Advisory, OSV, etc.)
- Detects license compliance issues
- Integrates with build/CI/CD pipeline for automated scanning
- Supports all package managers used (npm, Maven, pip, NuGet, Go modules, etc.)

**REQ-2.4.2.1-B: SCA Scan Frequency**

SCA scans **MUST** execute:
- **On every build**: Automated scan in CI/CD pipeline
- **Daily**: Scheduled scan of all active repositories (detects newly disclosed vulnerabilities)
- **On-demand**: Developers can trigger manual scans

**REQ-2.4.2.1-C: SCA Coverage**

SCA tools **MUST** scan:
- Application dependencies (package.json, requirements.txt, pom.xml, go.mod, Gemfile, etc.)
- Container images (base images and installed packages)
- Infrastructure-as-Code dependencies (Terraform modules, Helm charts)

### 2.4.2.2 Vulnerability Management for Dependencies

**REQ-2.4.2.2-A: Dependency Vulnerability Severity**

Dependency vulnerabilities **MUST** be classified using CVSS or equivalent scoring:
- **Critical (CVSS 9.0-10.0)**: Remote code execution, authentication bypass in widely-used libraries
- **High (CVSS 7.0-8.9)**: SQL injection, XSS, deserialization in dependencies
- **Medium (CVSS 4.0-6.9)**: Information disclosure, DoS vulnerabilities
- **Low (CVSS 0.1-3.9)**: Minor security weaknesses with low exploitability

**REQ-2.4.2.2-B: Dependency Vulnerability Remediation SLAs**

Dependency vulnerabilities **MUST** be remediated per defined SLAs:

| Severity | Remediation SLA | Acceptable Actions |
|----------|----------------|-------------------|
| **Critical** | 14 calendar days | Update dependency, remove dependency, apply workaround, risk acceptance with compensating controls |
| **High** | 30 calendar days | Update dependency, apply patch, implement mitigation |
| **Medium** | 90 calendar days | Update at next maintenance window |
| **Low** | Next major release | Update when convenient |

**Remediation Options** (in order of preference):
1. **Update to patched version** (preferred) - Update dependency to version with fix
2. **Apply vendor patch** - Apply security patch if available
3. **Remove dependency** - Replace with alternative library or reimplement functionality
4. **Implement workaround** - Disable vulnerable functionality or apply compensating control
5. **Accept risk** - Document justification, obtain approval, implement monitoring

**REQ-2.4.2.2-C: False Positive Management for SCA**

False positives in SCA findings **SHOULD** be managed systematically:
- Vulnerability does not affect application (unused code path, feature not enabled)
- Vulnerable version incorrectly identified (version detection error)
- Vulnerability only exploitable in non-production scenario (development dependencies)

Document false positive rationale and suppress in SCA tool (not in code).

### 2.4.2.3 Continuous Monitoring

**REQ-2.4.2.3-A: New Vulnerability Alerting**

Organizations **MUST** implement real-time alerting for new vulnerabilities:
- SCA tool monitors vulnerability databases for newly disclosed CVEs
- Alerts sent to Security Team and development teams when dependencies are affected
- Critical/High severity alerts trigger immediate assessment

**REQ-2.4.2.3-B: Vulnerability Dashboard**

Organizations **SHOULD** maintain centralized dashboard showing:
- Total number of dependencies across all applications
- Count of known vulnerabilities by severity
- Vulnerability age (time since disclosure)
- Remediation progress and SLA compliance
- Applications with highest risk (most Critical/High vulnerabilities)

---

## 2.4.3 Software Bill of Materials (SBOM)

### 2.4.3.1 SBOM Generation Requirements

**REQ-2.4.3.1-A: SBOM Creation**

Organizations **MUST** generate Software Bill of Materials (SBOM) for:
- All production applications
- Container images deployed to production
- Firmware/embedded software (if applicable)

SBOM **SHOULD** be generated for:
- Internal tools and utilities
- Test/staging environments

**REQ-2.4.3.1-B: SBOM Format Standards**

SBOMs **MUST** use industry-standard formats:
- **SPDX** (Software Package Data Exchange) - ISO/IEC 5962:2021 standard
- **CycloneDX** - OWASP-managed specification
- **SWID** (Software Identification Tags) - ISO/IEC 19770-2

**REQ-2.4.3.1-C: SBOM Content Requirements**

SBOMs **MUST** include:
- Component name and version
- Component supplier/publisher
- Component license(s)
- Known vulnerabilities (CVE IDs)
- Dependency relationships (direct vs. transitive)
- Cryptographic hashes for component integrity

**REQ-2.4.3.1-D: SBOM Generation Frequency**

SBOMs **MUST** be:
- Generated automatically during build process
- Updated whenever dependencies change
- Versioned and stored with application artifacts
- Made available for security assessments and audits

### 2.4.3.2 SBOM Usage and Maintenance

**REQ-2.4.3.2-A: SBOM for Vulnerability Management**

SBOMs **MUST** be used to:
- Identify affected applications when new vulnerabilities disclosed
- Prioritize remediation based on application criticality
- Track dependency usage across organization (which apps use vulnerable library X?)
- Support incident response (forensic analysis of compromised components)

**REQ-2.4.3.2-B: SBOM Retention**

SBOMs **MUST** be retained:
- For duration of application support lifecycle
- Minimum 3 years after application decommissioning (for audit/forensic purposes)
- Accessible to Security Team, compliance, and auditors

---

## 2.4.4 Component Selection and Approval

### 2.4.4.1 Component Evaluation Criteria

**REQ-2.4.4.1-A: Secure Component Selection**

Before introducing new third-party components, developers **SHOULD** evaluate:

| Criterion | Assessment | Risk Indicator |
|-----------|-----------|---------------|
| **Maintenance Status** | Active development, recent commits/releases | 🔴 No updates in 12+ months = abandoned |
| **Vulnerability History** | Past CVEs, response time to security issues | 🔴 History of critical vulnerabilities, slow fixes |
| **Community Health** | Number of contributors, active issue responses | 🔴 Single maintainer, unresponsive to issues |
| **License Compatibility** | License type (MIT, Apache, GPL, etc.) | 🔴 GPL/AGPL for proprietary software |
| **Security Reputation** | Known security practices, security policy | ✅ Has security.md, bug bounty program |
| **Dependencies** | Number and quality of transitive dependencies | 🔴 Many dependencies, includes other risky components |
| **Popularity/Adoption** | Download counts, GitHub stars, production use | ✅ Widely adopted, used by major organizations |

**REQ-2.4.4.1-B: Component Approval Process**

High-risk components **SHOULD** undergo formal approval:
- **High-risk components**: Cryptographic libraries, authentication/authorization frameworks, security controls
- **Approval required from**: Security Architect or Application Security Lead
- **Approval criteria**: Security evaluation completed, no known Critical vulnerabilities, compatible license

**REQ-2.4.4.1-C: Prohibited Components**

Organizations **MAY** maintain "prohibited components" list:
- Components with history of malicious code
- Abandoned components with unpatched Critical vulnerabilities
- Components with incompatible licenses
- Components violating organizational standards (e.g., cryptography using deprecated algorithms)

### 2.4.4.2 Component Version Management

**REQ-2.4.4.2-A: Dependency Pinning**

Dependencies **SHOULD** be pinned to specific versions:

✅ **CORRECT - Pinned Versions**:
```
# package.json
"dependencies": {
  "express": "4.18.2",      // Exact version
  "lodash": "4.17.21"
}
```

❌ **RISKY - Unpinned Versions**:
```
# package.json
"dependencies": {
  "express": "^4.18.0",     // Allows minor version updates (4.x.x)
  "lodash": "~4.17.0"       // Allows patch version updates (4.17.x)
}
```

**Rationale**: Unpinned versions may automatically update to versions with vulnerabilities or breaking changes. Pin versions for predictability and security.

**REQ-2.4.4.2-B: Dependency Lock Files**

Projects **MUST** use dependency lock files:
- **npm**: package-lock.json
- **Python**: requirements.txt with pinned versions or poetry.lock/Pipfile.lock
- **Maven**: Dependency Management with specific versions
- **Go**: go.sum
- **Ruby**: Gemfile.lock

Lock files ensure reproducible builds and prevent supply chain attacks via dependency confusion.

**REQ-2.4.4.2-C: Dependency Updates**

Dependencies **SHOULD** be updated regularly:
- **Security updates**: Immediate (per SLA in Section 2.4.2.2.B)
- **Minor updates**: Quarterly (bug fixes, new features)
- **Major updates**: Annual or as needed (breaking changes require testing)

Automated dependency update tools (Dependabot, Renovate Bot) **SHOULD** be used with:
- Automated PR creation for updates
- Required CI/CD checks before merge
- Security vulnerability prioritization

---

## 2.4.5 Open Source License Compliance

### 2.4.5.1 License Identification

**REQ-2.4.5.1-A: License Scanning**

Organizations **MUST** implement automated license scanning:
- SCA tool identifies licenses for all dependencies
- Licenses tracked in SBOM
- License compliance checked automatically during build

**REQ-2.4.5.1-B: License Categories**

Organizations **SHOULD** categorize licenses by risk:

| Category | License Types | Usage Policy |
|----------|--------------|-------------|
| **Permissive** | MIT, Apache 2.0, BSD | ✅ Approved for any use |
| **Weak Copyleft** | LGPL, MPL, EPL | ⚠️ Approved with restrictions (dynamic linking OK) |
| **Strong Copyleft** | GPL v2/v3, AGPL | 🔴 Requires legal review, generally prohibited for proprietary software |
| **Proprietary/Commercial** | Custom licenses, trial licenses | ⚠️ Requires contract review, license purchase |
| **Unknown/Unidentified** | No license, unclear license | 🔴 Prohibited until license clarified |

### 2.4.5.2 License Compliance Process

**REQ-2.4.5.2-A: License Approval**

Components with copyleft licenses (GPL, AGPL) **MUST**:
- Be reviewed by Legal/Compliance team
- Have documented approval for specific use case
- Be tracked in license compliance register
- Have source code availability plan (for GPL compliance)

**REQ-2.4.5.2-B: License Violation Remediation**

License violations discovered after deployment **MUST** be:
- Reported to Legal/Compliance within 5 business days
- Remediated by:
  - Removing component and replacing with compatible alternative, OR
  - Obtaining appropriate commercial license, OR
  - Making source code available (if GPL/AGPL compliant path chosen)
- Tracked until resolution

**REQ-2.4.5.2-C: License Attribution**

Organizations **MUST** provide license attribution:
- Include NOTICE or LICENSE files in distributed software
- Acknowledge open-source dependencies per license requirements
- Maintain attribution file listing all OSS components and their licenses

---

## 2.4.6 Supply Chain Security

### 2.4.6.1 Package Source Verification

**REQ-2.4.6.1-A: Trusted Package Repositories**

Organizations **SHOULD** use trusted package repositories:
- **Public repositories**: npm Registry, PyPI, Maven Central, RubyGems (verified publishers preferred)
- **Private repositories**: Organizational artifact repository (Artifactory, Nexus, Azure Artifacts)
- **Mirror/proxy**: Private mirror of public repositories with security scanning

**REQ-2.4.6.1-B: Package Integrity Verification**

When downloading packages, **VERIFY**:
- Cryptographic checksums/hashes (SHA-256 minimum)
- Digital signatures (GPG signatures where available)
- Package provenance (SLSA framework compliance where available)

**REQ-2.4.6.1-C: Private Package Repository**

Organizations **SHOULD** deploy private package repository that:
- Mirrors public repositories with security scanning
- Blocks download of packages with known vulnerabilities
- Provides approved-packages-only mode for critical applications
- Logs all package downloads for audit trail

### 2.4.6.2 Dependency Confusion Prevention

**REQ-2.4.6.2-A: Namespace Protection**

Organizations **MUST** prevent dependency confusion attacks:
- Reserve organization namespace in public repositories (npm scopes, PyPI namespaces)
- Use unique package names unlikely to be typosquatted
- Configure package manager to prioritize private registry

**REQ-2.4.6.2-B: Package Manager Configuration**

Package managers **SHOULD** be configured:
```
# npm .npmrc - Always check private registry first
registry=https://private-registry.company.com/
@company:registry=https://private-registry.company.com/
```

**REQ-2.4.6.2-C: Typosquatting Detection**

Organizations **SHOULD** monitor for typosquatting:
- Automated detection of similarly-named packages in public repositories
- Alerting when potential typosquat of organizational package detected
- Reporting to repository maintainers for takedown

### 2.4.6.3 Build-Time Supply Chain Security

**REQ-2.4.6.3-A: Build Tool Integrity**

Build toolchains **MUST** be secured:
- Build tools (compilers, package managers) obtained from official sources
- Build tools verified with cryptographic signatures
- Build environments regularly patched and updated

**REQ-2.4.6.3-B: Build Reproducibility**

Organizations **SHOULD** implement reproducible builds:
- Deterministic build process (same input → same output)
- Pinned tool versions in build configuration
- Documented build environment (container image, VM snapshot)
- Verification that built artifacts match expected hashes

**REQ-2.4.6.3-C: Build Provenance**

Organizations **SHOULD** generate build provenance attestations:
- SLSA (Supply chain Levels for Software Artifacts) framework
- Document what source code was built, when, by whom, using what tools
- Sign build artifacts with organizational signing key
- Store provenance metadata with artifacts

---

## 2.4.7 Vendor-Developed Software

### 2.4.7.1 Vendor Security Requirements

**REQ-2.4.7.1-A: Security Requirements in Contracts**

Contracts with third-party development vendors **MUST** include:
- Adherence to organizational secure coding standards
- SBOM delivery requirement (SPDX or CycloneDX format)
- Vulnerability disclosure and remediation SLAs
- Security testing requirements (SAST, DAST, penetration testing)
- Audit rights (organization can review vendor's development practices)
- Liability clauses for security vulnerabilities

**REQ-2.4.7.1-B: Vendor Security Assessment**

Before engaging development vendors, organizations **MUST** assess:
- Vendor's secure SDLC practices
- Developer security training programs
- Use of security testing tools (SAST, SCA)
- Incident response capabilities
- Past security track record

Vendor security assessments **SHOULD** use standardized questionnaires (CAIQ, VSA, custom).

### 2.4.7.2 Vendor Code Acceptance

**REQ-2.4.7.2-A: Code Review for Vendor Deliverables**

Vendor-developed code **MUST** undergo:
- Security-focused code review by organizational security team
- SAST/DAST scanning with organizational tools
- Penetration testing before production deployment
- SBOM validation (verify declared dependencies match actual)

**REQ-2.4.7.2-B: Vendor Code Remediation**

Vulnerabilities in vendor code **MUST**:
- Be reported to vendor with severity classification
- Follow same remediation SLAs as internal code
- Require vendor attestation that fix is complete
- Be retested by organization before acceptance

**REQ-2.4.7.2-C: Escrow Agreements**

For critical vendor-developed software, organizations **SHOULD**:
- Establish source code escrow agreements
- Ensure access to source code if vendor discontinues support
- Include access triggers (vendor bankruptcy, discontinuation, security incident)

---

## 2.4.8 Continuous Monitoring and Improvement

### 2.4.8.1 Supply Chain Threat Intelligence

**REQ-2.4.8.1-A: Threat Monitoring**

Organizations **SHOULD** monitor:
- Newly disclosed vulnerabilities (NVD, GitHub Security Advisories, vendor advisories)
- Supply chain attack incidents (typosquatting, compromised packages)
- Vulnerability exploits in the wild (CISA KEV - Known Exploited Vulnerabilities)
- Security advisories for commonly-used dependencies

**REQ-2.4.8.1-B: Threat Intelligence Integration**

Threat intelligence **SHOULD** be integrated with SCA tooling:
- Prioritize vulnerabilities with known exploits
- Alert on dependencies involved in supply chain attacks
- Correlate organizational usage with threat intelligence

### 2.4.8.2 Supply Chain Metrics

**REQ-2.4.8.2-A: Tracking Metrics**

Organizations **SHOULD** track:
- **Dependency count**: Total dependencies, direct vs. transitive
- **Vulnerability exposure**: Count of known vulnerabilities by severity
- **Component age**: Outdated dependencies (> 2 years old)
- **Remediation velocity**: Mean time to patch dependency vulnerabilities
- **License compliance rate**: % of dependencies with approved licenses
- **SBOM coverage**: % of applications with current SBOM

### 2.4.8.3 Supply Chain Incident Response

**REQ-2.4.8.3-A: Supply Chain Incident Plan**

Organizations **MUST** have incident response plan for:
- Compromised dependency discovered in use
- Malicious package introduced via dependency confusion
- Zero-day vulnerability in critical dependency
- Vendor security breach affecting delivered code

Incident response plan **MUST** include:
- Identification: Which applications are affected? (use SBOM)
- Containment: Block vulnerable dependency, deploy compensating controls
- Eradication: Remove/replace compromised dependency
- Recovery: Deploy patched version, verify integrity
- Lessons learned: Update approval process, improve detection

---

## 2.4.9 Compliance and Evidence

### 2.4.9.1 Third-Party/OSS Assessment

Compliance with third-party and OSS management requirements is assessed in:
- **ISMS-IMP-A.8.28.4**: Third-Party & OSS Assessment

Evidence includes:
- SCA tool scan reports (dependency vulnerabilities, licenses)
- SBOM files for production applications
- Component approval records (high-risk component reviews)
- Dependency update tracking (remediation of known vulnerabilities)
- License compliance register (GPL/AGPL approvals, attributions)
- Vendor security assessments and contracts
- Supply chain incident response records

### 2.4.9.2 Regulatory Alignment

This section addresses regulatory requirements including:
- **EU Cyber Resilience Act (CRA)**: SBOM requirements for software products
- **US Executive Order 14028**: Federal software supply chain security requirements (SBOM, secure SDLC)
- **NIST SP 800-218 SSDF**: Supply chain security practices
- **ISO/IEC 27036**: Supply chain security standard

Organizations exporting software or contracting with governments **MUST** comply with applicable supply chain regulations.

---

**END OF DOCUMENT**

*"Supply chains are only as strong as their weakest link. In software, we have thousands of links, most of which we didn't forge ourselves."* - Anonymous CISO

**Application to Supply Chain Security**: We cannot eliminate supply chain risk, but we can systematically identify, monitor, and mitigate it through SCA tooling, SBOM generation, continuous monitoring, and rapid response to supply chain incidents. Trust, but verify - especially your dependencies.
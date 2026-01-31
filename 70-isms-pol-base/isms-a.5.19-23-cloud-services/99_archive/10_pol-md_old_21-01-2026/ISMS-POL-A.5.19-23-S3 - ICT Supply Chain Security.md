# ISMS-POL-A.5.19-23-S3 — ICT Supply Chain Security
## Control A.5.21: Managing Information Security in the ICT Supply Chain

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | ICT Supply Chain Security |
| **Document Type** | Policy Section |
| **Document ID** | ISMS-POL-A.5.19-23-S3 |
| **Document Creator** | Information Security Officer (ISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISO | Initial section for ISO 27001:2022 Control A.5.21 |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Information Security Officer (ISO)
- Compliance: Legal/Compliance Officer
- Technical: Chief Information Officer (CIO)
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.19-23 (Parent Policy - Supplier & Cloud Services Security)
- ISMS-POL-A.5.19-23-S1 (Supplier Relationship Fundamentals)
- ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements)
- ISO/IEC 27001:2022 Control A.5.21
- ISO/IEC 27036-3 (ICT supply chain security)
- NIST SP 800-161 (Cybersecurity Supply Chain Risk Management)

---

## 1. Purpose

This section defines requirements for managing information security risks within the ICT supply chain, including sub-suppliers, component providers, and software dependencies. It addresses the "supplier's supplier" problem and supply chain attack vectors.

**Control Objective (ISO 27002:2022):**
> "Processes and procedures shall be defined and implemented to manage the information security risks associated with the ICT products and services supply chain."

---

## 2. Scope

### 2.1 Supply Chain Elements

| Element | Description | Examples |
|---------|-------------|----------|
| **Sub-suppliers** | Suppliers engaged by primary suppliers | Subcontractors, subprocessors |
| **Fourth parties** | Suppliers to sub-suppliers | Infrastructure providers to SaaS vendors |
| **Software components** | Code dependencies and libraries | Open source packages, SDKs, APIs |
| **Hardware components** | Physical components in ICT products | Processors, memory, firmware |
| **Service dependencies** | Services required by primary services | DNS, CDN, payment gateways |
| **Development tools** | Tools used to build/deliver products | CI/CD platforms, repositories |

### 2.2 Supply Chain Risk Categories

| Risk Category | Description | Impact |
|---------------|-------------|--------|
| **Compromise risk** | Malicious code or backdoors inserted | Data breach, system compromise |
| **Availability risk** | Supply chain disruption | Service outage, delivery delays |
| **Integrity risk** | Unauthorized modifications | Data corruption, system instability |
| **Compliance risk** | Regulatory violations via supply chain | Fines, legal liability |
| **Concentration risk** | Single points of failure | Widespread impact from single failure |

---

## 3. Sub-Supplier Management

### 3.1 Sub-Supplier Visibility Requirements

| Supplier Level | Visibility Requirement |
|----------------|------------------------|
| Level 1 | Full sub-supplier register for data-processing activities |
| Level 2 | Sub-supplier register for material services |
| Level 3 | Awareness of key sub-suppliers |
| Level 4 | Not required |

### 3.2 Sub-Supplier Register

For Level 1 and Level 2 suppliers, maintain visibility of:

| Field | Description |
|-------|-------------|
| Sub-supplier name | Legal entity |
| Services provided | What they do for primary supplier |
| Data access | Whether they access organization data |
| Location | Geographic location(s) of processing |
| Certification status | Security certifications held |
| Criticality | Impact if sub-supplier fails |

### 3.3 Sub-Supplier Control Requirements

**Primary suppliers shall:**

| Requirement | Level 1 | Level 2 | Level 3-4 |
|-------------|---------|---------|-----------|
| Notify organization of sub-supplier changes | ✓ Prior | ✓ Timely | — |
| Obtain approval for new sub-suppliers | ✓ Written | ✓ Reasonable | — |
| Flow security requirements to sub-suppliers | ✓ Required | ✓ Required | — |
| Remain liable for sub-supplier acts | ✓ Required | ✓ Required | ✓ Required |
| Provide sub-supplier audit reports on request | ✓ Required | ✓ Best effort | — |
| Allow objection to specific sub-suppliers | ✓ Required | ✓ Reasonable | — |

### 3.4 Sub-Supplier Change Process

```
┌─────────────────────────────────────────────────────────────────┐
│ SUB-SUPPLIER CHANGE NOTIFICATION PROCESS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Supplier notifies Organization of planned change            │
│                         ↓                                       │
│  2. Organization reviews sub-supplier details                   │
│     • Security certifications                                   │
│     • Data access scope                                         │
│     • Geographic location                                       │
│                         ↓                                       │
│  3. Organization responds (within 14 days)                      │
│     • Approve                                                   │
│     • Request more information                                  │
│     • Object (with valid reason)                                │
│                         ↓                                       │
│  4. If objection: Supplier proposes alternative or mitigation   │
│                         ↓                                       │
│  5. Update sub-supplier register                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Fourth-Party Risk Management

### 4.1 Fourth-Party Visibility

Fourth parties are suppliers to your suppliers (e.g., the cloud provider hosting your SaaS vendor).

| Approach | Description |
|----------|-------------|
| **Direct visibility** | Request fourth-party information from supplier |
| **Certification reliance** | Supplier's ISO 27001/SOC 2 covers fourth-party management |
| **Contractual flow-down** | Require supplier to impose requirements on fourth parties |

### 4.2 Critical Fourth-Party Dependencies

Identify and document fourth-party dependencies for:

- Infrastructure services (compute, storage, networking)
- Security services (identity, encryption, monitoring)
- Operational services (DNS, CDN, payment processing)

### 4.3 Fourth-Party Risk Indicators

| Indicator | Risk Signal |
|-----------|-------------|
| Supplier uses single fourth-party for critical function | Concentration risk |
| Fourth-party located in high-risk jurisdiction | Geopolitical risk |
| Fourth-party has history of incidents | Reliability risk |
| No contractual controls over fourth-party | Compliance risk |

---

## 5. Software Supply Chain Security

### 5.1 Software Component Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| Vulnerable dependencies | Known CVEs in libraries | Vulnerability scanning, patching |
| Malicious packages | Typosquatting, compromised packages | Package verification, trusted sources |
| Abandoned software | Unmaintained components | Lifecycle monitoring, alternatives |
| License compliance | Incompatible or viral licenses | License scanning, legal review |
| Build compromise | Tampered build pipelines | Secure CI/CD, code signing |

### 5.2 Requirements for Suppliers

**Level 1 & 2 suppliers providing software shall:**

| Requirement | Description |
|-------------|-------------|
| Dependency inventory | Maintain software bill of materials (SBOM) |
| Vulnerability management | Regular scanning and timely patching |
| Secure development | Follow secure SDLC practices |
| Code signing | Sign releases to verify integrity |
| Source verification | Use verified package sources |
| Update notification | Inform of security-relevant updates |

### 5.3 Software Bill of Materials (SBOM)

For critical software suppliers, request SBOM containing:

| Field | Description |
|-------|-------------|
| Component name | Package/library identifier |
| Version | Specific version in use |
| Source | Where component was obtained |
| License | License type |
| Dependencies | Transitive dependencies |
| Known vulnerabilities | Current CVE status |

### 5.4 Open Source Considerations

| Consideration | Guidance |
|---------------|----------|
| Source verification | Verify packages from official repositories |
| Maintenance status | Avoid abandoned projects for critical functions |
| Community health | Active maintainers, responsive to issues |
| Security track record | History of vulnerability handling |
| License compatibility | Verify license permits intended use |

---

## 6. Hardware Supply Chain Security

### 6.1 Hardware Supply Chain Risks

| Risk | Description | Examples |
|------|-------------|----------|
| Counterfeit components | Non-genuine parts | Fake chips, batteries |
| Tampered hardware | Malicious modifications | Implanted backdoors |
| Compromised firmware | Malicious firmware | Pre-installed malware |
| Component failure | Substandard components | Early failure, unreliability |
| End-of-life | Unsupported hardware | No security patches |

### 6.2 Hardware Procurement Requirements

**For Level 1 & 2 hardware suppliers:**

| Requirement | Description |
|-------------|-------------|
| Authorized channels | Purchase through authorized distributors |
| Chain of custody | Documentation of handling and transport |
| Integrity verification | Verify seals, packaging, serial numbers |
| Firmware verification | Validate firmware versions and signatures |
| Component authenticity | Anti-counterfeit measures for critical components |

### 6.3 Hardware Lifecycle Considerations

| Phase | Security Consideration |
|-------|------------------------|
| Procurement | Authorized source, integrity verification |
| Deployment | Secure configuration, firmware updates |
| Operation | Patch management, monitoring |
| End-of-life | Secure disposal, data destruction |

---

## 7. Service Dependency Management

### 7.1 Critical Service Dependencies

Identify services that suppliers depend on:

| Dependency Type | Examples | Risk if Unavailable |
|-----------------|----------|---------------------|
| Infrastructure | Cloud platforms, data centers | Complete service outage |
| Identity | Authentication providers | Access disruption |
| Security | Certificate authorities, security tools | Security degradation |
| Communication | Email, messaging platforms | Notification failure |
| Operational | DNS, CDN, load balancers | Performance/availability |

### 7.2 Dependency Documentation

For Level 1 suppliers, document:

| Field | Description |
|-------|-------------|
| Service dependency | What the supplier depends on |
| Criticality | Impact if dependency fails |
| Alternatives | Backup or failover options |
| SLA | Service level of dependency |
| Geographic scope | Regions affected |

---

## 8. Supply Chain Attack Mitigation

### 8.1 Common Attack Vectors

| Vector | Description | Mitigation |
|--------|-------------|------------|
| Compromised updates | Malicious software updates | Code signing, update verification |
| Credential theft | Supplier credentials stolen | MFA, privileged access management |
| Watering hole | Supplier tools/sites compromised | Network segmentation, monitoring |
| Social engineering | Targeting supplier personnel | Supplier security awareness |
| Insider threat | Malicious supplier employee | Background checks, access controls |

### 8.2 Supply Chain Security Controls

| Control | Description |
|---------|-------------|
| Supplier segmentation | Limit supplier access to necessary systems |
| Monitoring | Log and alert on supplier activities |
| Integrity verification | Verify updates, downloads, communications |
| Incident response | Include supply chain scenarios in IR plans |
| Backup suppliers | Identify alternatives for critical suppliers |

---

## 9. Flow-Down Requirements

### 9.1 Security Requirements Propagation

Primary suppliers shall propagate security requirements through the supply chain:

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Organization │ ───► │   Supplier   │ ───► │ Sub-supplier │
│              │      │  (Level 1)   │      │              │
│ Requirements │      │ Flow-down    │      │ Must comply  │
│ defined      │      │ required     │      │ with reqs    │
└──────────────┘      └──────────────┘      └──────────────┘
```

### 9.2 Minimum Flow-Down Requirements

| Requirement | Must Flow to Sub-suppliers |
|-------------|----------------------------|
| Confidentiality | ✓ Always |
| Data protection | ✓ If processing personal data |
| Security controls | ✓ If accessing organization data |
| Incident notification | ✓ Always |
| Audit cooperation | ✓ For critical sub-suppliers |

---

## 10. Monitoring & Review

### 10.1 Supply Chain Monitoring

| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| Sub-supplier register review | Quarterly | Procurement + Security |
| Fourth-party risk assessment | Annual | Security |
| Software dependency scan | Continuous | IT Operations |
| Supply chain incident review | Upon occurrence | Security |
| Critical dependency validation | Semi-annual | IT Operations |

### 10.2 Supply Chain Metrics

| Metric | Target |
|--------|--------|
| Sub-supplier visibility (Level 1) | 100% documented |
| Critical dependencies identified | 100% documented |
| SBOM coverage (critical software) | 100% available |
| Supply chain incidents | Track and trend |

---

## 11. References

| Document | Relationship |
|----------|--------------|
| ISMS-POL-A.5.19-23 | Parent policy framework |
| ISMS-POL-A.5.19-23-S1 | Supplier classification |
| ISMS-POL-A.5.19-23-S2 | Subcontractor contract requirements |
| ISMS-IMP-A.5.19-23.1 | Supplier inventory (includes sub-suppliers) |
| ISO/IEC 27036-3 | Guidelines for ICT supply chain security |

---

**Next Document:** ISMS-POL-A.5.19-23-S4 — Supplier Monitoring & Change Management (Control A.5.22)

---

*"Your security is only as strong as your weakest supplier's weakest supplier."*
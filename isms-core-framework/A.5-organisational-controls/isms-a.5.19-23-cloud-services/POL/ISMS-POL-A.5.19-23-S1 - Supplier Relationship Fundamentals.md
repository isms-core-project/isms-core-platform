<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S1:framework:POL:a.5.19-23-s1 -->
**ISMS-POL-A.5.19-23-S1 — Supplier Relationship Fundamentals**
**Control A.5.19: Information Security in Supplier Relationships**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Supplier Relationship Fundamentals |
| **Document Type** | Policy Section |
| **Document ID** | ISMS-POL-A.5.19-23-S1 |
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
| 1.0 | [Date] | ISO | Initial section for ISO 27001:2022 Control A.5.19 |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Information Security Officer (ISO)
- Compliance: Legal/Compliance Officer
- Procurement: Procurement Director
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.19-23 (Parent Policy - Supplier & Cloud Services Security)
- ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements)
- ISMS-IMP-A.5.19-23.S1-UG/TG (Cloud Service Inventory & Classification)
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- ISO/IEC 27001:2022 Control A.5.19
- ISO/IEC 27036-1 (Information security for supplier relationships - Overview and concepts)

---

# Purpose

This section defines the foundational requirements for managing information security risks in supplier relationships. It establishes the classification framework, risk assessment methodology, and due diligence requirements that apply to all external suppliers.

**Critical Principle - "Know Your Suppliers Before They Know Your Data"**: Supplier relationships shall begin with systematic risk assessment and evidence-based due diligence, not post-contract discovery. Granting supplier access without classification, allowing data access without due diligence, or signing contracts without security assessment creates unacceptable and potentially unrecoverable risks. Supplier selection is a security decision, not just a procurement decision.

**ISO/IEC 27001:2022 Control A.5.19 - Information Security in Supplier Relationships**

> *Processes and procedures should be defined and agreed upon with suppliers to manage information security risks associated with the use of supplier's products or services.*

**Control Objective**: Ensure information security risks associated with supplier relationships are identified, assessed, and managed throughout the relationship lifecycle.

**ISO/IEC 27002:2022 Guidance Summary**:

- Supplier relationships shall be managed through defined processes covering entire lifecycle (selection, onboarding, operation, exit)
- Suppliers shall be identified and classified based on type of access, data sensitivity, and service criticality
- Due diligence shall be conducted before granting supplier access to organisational information or systems
- Supplier security requirements shall be defined based on risk classification and data classification
- Supplier performance and security posture shall be monitored throughout relationship duration
- Supplier exit procedures shall be established to ensure safe termination and data return
- Shadow IT and unauthorised supplier usage shall be actively identified and managed
- Supplier dependency and concentration risk shall be assessed for critical services

---

# Scope

## Applicable Supplier Types

| Supplier Type | Description | Examples |
|---------------|-------------|----------|
| **Cloud Service Providers** | Providers of IaaS, PaaS, SaaS, XDR services | Compute, storage, email, security platforms |
| **Managed Service Providers** | Outsourced IT operations and support | Helpdesk, network management, SOC services |
| **Software Vendors** | Providers of licensed or subscription software | ERP, CRM, development tools |
| **Hardware Vendors** | Providers of physical IT equipment | Servers, network devices, endpoints |
| **Professional Services** | Consultants with system/data access | Auditors, integrators, developers |
| **Facilities Providers** | Data center and hosting services | Colocation, physical security |
| **Telecommunications** | Network and connectivity providers | Internet, WAN, voice services |

## Exclusions

This policy does not apply to:

- Suppliers providing goods/services without access to organisational information
- One-time purchases with no ongoing relationship
- Individual consumers of [Organisation]'s services

---

# Supplier Classification

## Classification Criteria

Suppliers shall be classified based on the following factors:

| Factor | Weight | Assessment Questions |
|--------|--------|---------------------|
| **Data Access** | High | What data classification levels can the supplier access? |
| **System Access** | High | Does the supplier have access to production systems? |
| **Service Criticality** | High | Would supplier failure impact business operations? |
| **Replaceability** | Medium | How easily can the supplier be replaced? |
| **Integration Depth** | Medium | How deeply integrated are supplier services? |
| **Regulatory Impact** | High | Does the supplier affect regulatory compliance? |

## Classification Levels

### Level 1: Critical Suppliers

**Criteria (any one triggers Level 1):**

- Access to Restricted or Confidential data
- Direct access to production systems or infrastructure
- Single point of failure for critical business processes
- Regulatory compliance dependency (DORA critical provider, NIS2 essential service, GDPR processor for high-risk processing)

**Requirements:**

- Annual on-site or detailed remote assessment
- Quarterly performance and security reviews
- Documented business continuity plan
- Right-to-audit clause mandatory
- Executive sponsor assigned
- SOC 2 Type II or ISO/IEC 27001 certification required
- Incident notification within 4 hours
- Sub-processor disclosure and approval

### Level 2: High-Risk Suppliers

**Criteria:**

- Access to Internal data classification
- Access to non-production systems (development, test)
- Important but not critical business function
- Multiple supplier options available
- GDPR processor for standard risk processing

**Requirements:**

- Annual security assessment (questionnaire + evidence)
- Semi-annual performance reviews
- Business continuity considerations documented
- Right-to-audit clause recommended
- SOC 2 or ISO/IEC 27001 certification required
- Incident notification within 24 hours
- Sub-processor disclosure

### Level 3: Medium-Risk Suppliers

**Criteria:**

- Limited data access (Public or minimal Internal)
- No direct system access
- Supporting business function
- Easily replaceable
- No regulatory compliance impact

**Requirements:**

- Biennial security assessment
- Annual performance review
- Standard contractual security clauses
- Certification preferred if handling any organisational data
- Incident notification within 72 hours

### Level 4: Low-Risk Suppliers

**Criteria:**

- No access to organisational data
- No system access
- Commodity services
- Multiple alternatives available
- No regulatory impact

**Requirements:**

- Initial due diligence only
- Standard terms and conditions
- Review upon contract renewal

## Classification Matrix

```
                    │ No System  │ Non-Prod   │ Production │
                    │ Access     │ Access     │ Access     │
────────────────────┼────────────┼────────────┼────────────┤
Restricted Data     │ Level 2    │ Level 1    │ Level 1    │
Confidential Data   │ Level 2    │ Level 1    │ Level 1    │
Internal Data       │ Level 3    │ Level 2    │ Level 2    │
Public Data Only    │ Level 4    │ Level 3    │ Level 3    │
No Data Access      │ Level 4    │ Level 4    │ Level 3    │
```

**Classification Re-Assessment**: Supplier classification shall be reassessed:

- Annually for all suppliers
- Upon significant change in service scope
- Upon merger/acquisition of supplier
- Upon material security incident
- Upon regulatory scope changes (e.g., DORA/NIS2 applicability)

---

# Supplier Risk Assessment

## Risk Categories

| Category | Description | Assessment Focus |
|----------|-------------|------------------|
| **Confidentiality Risk** | Unauthorised disclosure of information | Data handling, access controls, encryption |
| **Integrity Risk** | Unauthorised modification of data/systems | Change management, input validation, quality controls |
| **Availability Risk** | Service disruption or data loss | Redundancy, backup, disaster recovery, SLA commitments |
| **Compliance Risk** | Regulatory or contractual violations | Certifications, audit reports, attestations, regulatory alignment |
| **Concentration Risk** | Over-reliance on single supplier | Market alternatives, exit feasibility, vendor lock-in |
| **Geopolitical Risk** | Jurisdictional or political factors | Data residency, legal frameworks, US CLOUD Act exposure |

## Risk Assessment Process

**Step 1: Information Gathering**

- Supplier security questionnaire completion
- Documentation review (certifications, policies, procedures)
- Technical documentation analysis (architecture, data flow)
- Financial stability assessment (for Level 1 suppliers)
- Reference checks with existing customers

**Step 2: Risk Identification**

- Map supplier services to risk categories
- Identify potential threat scenarios per category
- Document existing controls (supplier-provided + organisational)
- Assess shared responsibility model (for cloud services)
- Evaluate sub-processor and supply chain risks

**Step 3: Risk Evaluation**

- Assess likelihood and impact per risk category
- Calculate risk score per category using matrix (Section 4.3)
- Determine overall supplier risk rating
- Compare against risk appetite and tolerance

**Step 4: Risk Treatment**

- **Accept**: Risk within tolerance, document acceptance with CISO approval
- **Mitigate**: Additional controls required (contractual clauses, technical controls, monitoring)
- **Transfer**: Insurance or contractual liability provisions
- **Avoid**: Do not proceed with supplier engagement

**Step 5: Documentation**

- Risk assessment report with findings and recommendations
- Risk treatment plan with assigned responsibilities and timelines
- Approval records (CISO for high/critical risk)
- Integration into supplier register

## Risk Scoring

| Likelihood | Impact: Low | Impact: Medium | Impact: High | Impact: Critical |
|------------|-------------|----------------|--------------|------------------|
| **Rare** | 1 | 2 | 3 | 4 |
| **Unlikely** | 2 | 4 | 6 | 8 |
| **Possible** | 3 | 6 | 9 | 12 |
| **Likely** | 4 | 8 | 12 | 16 |
| **Almost Certain** | 5 | 10 | 15 | 20 |

**Risk Rating Thresholds:**

- **1-4:** Low Risk → Standard controls, annual review
- **5-9:** Medium Risk → Enhanced controls, semi-annual review
- **10-15:** High Risk → Significant controls + CISO approval + quarterly review
- **16-20:** Critical Risk → Executive approval + continuous monitoring + mitigation plan mandatory

**Unacceptable Risk**: Risk scores 16-20 without feasible mitigation shall result in supplier rejection or relationship termination.

---

# Due Diligence Requirements

## Due Diligence by Classification Level

| Requirement | Level 1 | Level 2 | Level 3 | Level 4 |
|-------------|---------|---------|---------|---------|
| Security questionnaire | ✓ Detailed | ✓ Standard | ✓ Basic | — |
| Certification verification | ✓ Required | ✓ Required | ✓ If claimed | — |
| Policy document review | ✓ Required | ✓ Required | — | — |
| Technical assessment | ✓ Required | ✓ Risk-based | — | — |
| Financial stability check | ✓ Required | ✓ Recommended | — | — |
| Reference checks | ✓ Required | ✓ Recommended | — | — |
| On-site assessment | ✓ Risk-based | — | — | — |
| Penetration test review | ✓ Required | ✓ If available | — | — |
| Sub-processor evaluation | ✓ Required | ✓ If applicable | — | — |
| Data processing agreement | ✓ Required | ✓ Required | ✓ If data access | — |
| Business continuity review | ✓ Required | ✓ Required | ✓ If critical | — |

## Security Certifications

**Preferred Certifications (in order of preference):**

| Certification | Scope | Validity | Notes |
|---------------|-------|----------|-------|
| ISO/IEC 27001 | Information security management | 3 years (annual surveillance) | Global standard, comprehensive |
| SOC 2 Type II | Trust service criteria | 12 months | US-focused, detailed controls |
| SOC 2 Type I | Point-in-time assessment | Point-in-time | Less rigorous than Type II |
| ISO/IEC 27017 | Cloud security controls | 3 years | Cloud-specific extension |
| ISO/IEC 27018 | Cloud privacy | 3 years | Privacy in cloud |
| CSA STAR | Cloud security maturity | Varies by level | Self-assessment to certified |

**Certification Requirements by Level:**

- **Level 1:** ISO/IEC 27001 or SOC 2 Type II required (current within 12 months)
- **Level 2:** ISO/IEC 27001 or SOC 2 (Type I acceptable) required (current within 12 months)
- **Level 3:** Certification preferred but not mandatory if handling organisational data
- **Level 4:** No certification requirement

**Certification Acceptance Criteria:**

- Certificate must be current (within validity period)
- Scope must cover services provided to [Organisation]
- Issuing body must be accredited (ISO: accredited certification body; SOC: licensed CPA firm)
- For multi-year certificates (ISO), annual surveillance audits must be completed

**Alternative Attestations**: If ISO/SOC certifications unavailable, [Organisation] may accept:

- Government-issued certifications (FedRAMP, C5 in Germany)
- Industry-specific certifications (PCI DSS v4.0.1 for payment processors, HITRUST for healthcare)
- Detailed third-party security audit reports (requires CISO approval)

## Due Diligence Documentation

All due diligence activities shall be documented including:

- Completed security questionnaires with evidence
- Certification copies with validity verification
- Risk assessment results and scoring
- Decision rationale and approval records
- Identified gaps and remediation plans
- Compensating controls where applicable
- Supplier responses to findings
- Follow-up items and closure tracking

**Documentation Retention**: Due diligence documentation shall be retained for:

- Duration of supplier relationship + 7 years (regulatory requirement)
- Minimum 3 years after relationship termination
- Permanent retention for Level 1 suppliers with significant incidents

---

# Information Security Requirements

## Baseline Requirements (All Suppliers with Data Access)

| Requirement | Description |
|-------------|-------------|
| **Access Control** | Least privilege principle, unique accounts, role-based access, access logging |
| **Authentication** | Strong authentication (complex passwords or certificates), MFA for privileged access |
| **Encryption in Transit** | Data encrypted during transmission using TLS 1.2+ or equivalent |
| **Incident Reporting** | Security incidents reported to [Organisation] within 24 hours of awareness |
| **Personnel Security** | Background checks appropriate to access level for staff with access to [Organisation] data |
| **Confidentiality** | NDA or equivalent contractual confidentiality commitment |
| **Data Minimization** | Access only to data necessary for service delivery |
| **Data Residency** | Data processing within approved jurisdictions per contract |

## Enhanced Requirements (Level 1 & 2 Suppliers)

| Requirement | Description |
|-------------|-------------|
| **Encryption at Rest** | Data encrypted at rest using strong algorithms (AES-256 or equivalent) |
| **Vulnerability Management** | Regular vulnerability scanning, timely patching (critical within 30 days, high within 60 days) |
| **Security Monitoring** | Logging, alerting, SIEM integration where applicable, retention per regulatory requirements |
| **Business Continuity** | Documented BC/DR plans and annual testing with evidence provided |
| **Audit Rights** | [Organisation] may audit or review third-party audit reports (SOC 2, ISO 27001 surveillance) |
| **Subcontractor Controls** | Security requirements flow down to subcontractors, subcontractor disclosure required |
| **Change Management** | Formal change control with [Organisation] notification for material changes |
| **Data Segregation** | Logical or physical segregation from other customers (multi-tenancy controls) |
| **Secure Development** | SDLC with security testing for custom development or integrations |
| **Incident Response** | Documented incident response plan with contact information and escalation procedures |

## Requirements Communication

Security requirements shall be communicated to suppliers through:

- Security requirements appendix in contracts (see ISMS-POL-A.5.19-23-S2)
- Supplier security handbook (if applicable)
- Onboarding documentation and orientation
- Regular relationship reviews and performance discussions
- Ad-hoc communications for new security requirements or threat intelligence

**Verification**: Supplier compliance with security requirements shall be verified through:

- Self-assessment questionnaires
- Third-party certifications and audit reports
- Technical security testing (for Level 1 suppliers)
- Performance monitoring and SLA tracking
- Incident analysis and post-mortem reviews

---

# Supplier Register

## Register Requirements

[Organisation] shall maintain a comprehensive supplier register containing:

| Field | Description | Update Trigger |
|-------|-------------|----------------|
| Supplier name | Legal entity name | Contract change |
| Supplier type | Per Section 2.1 categories | Service change |
| Classification level | Level 1-4 per Section 3 | Annual review |
| Services provided | Description of services/products | Service change |
| Data access | Classification of data accessible | Access change |
| System access | Systems supplier can access | Access change |
| Contract reference | Link to agreement and amendments | Contract change |
| Business owner | Internal relationship owner | Organisational change |
| Security contact | Supplier security point of contact | Supplier change |
| Last assessment date | Most recent security assessment | Assessment completion |
| Next review date | Scheduled review date | Classification change |
| Risk rating | Current risk score per Section 4.3 | Assessment completion |
| Certifications | Current certifications with expiry dates | Certificate renewal |
| Regulatory scope | DORA/NIS2/GDPR applicability | Business change |
| Exit complexity | Ease of service replacement (Low/Medium/High) | Annual review |

## Register Maintenance

- Register updated upon new supplier onboarding (within 5 business days)
- Register updated upon contract changes (within 10 business days)
- Quarterly review for accuracy by Information Security Officer
- Annual completeness audit by Internal Audit or CISO
- Register availability: Accessible to Procurement, IT, Security, Legal, Audit

**Register Tools**: Supplier register may be maintained in:

- Dedicated GRC (Governance, Risk, Compliance) platform
- Procurement management system with security module
- Excel/database with version control (minimum acceptable)
- Assessment workbook ISMS-IMP-A.5.19-23-1 (Cloud Service Inventory)

**Register Reporting**: Quarterly supplier summary reports shall include:

- Total supplier count by classification level
- Certification status (current vs expired vs missing)
- Upcoming reviews and assessments
- High-risk suppliers requiring attention
- New suppliers onboarded this quarter
- Exited suppliers this quarter

---

# Shadow IT Prevention

## Shadow IT Definition

**Shadow IT**: Use of unauthorised suppliers, cloud services, or software without IT and Security approval. Shadow IT bypasses security controls, due diligence, and contract protections, creating unmanaged and often undetectable risks.

## Prevention Measures

| Measure | Description |
|---------|-------------|
| **Approved Service Catalog** | Maintain and communicate list of approved suppliers and services |
| **Procurement Integration** | Require IT/Security approval in procurement workflow |
| **Network Monitoring** | Monitor network traffic for unapproved cloud service usage |
| **Endpoint Controls** | Application whitelisting or monitoring for unapproved software |
| **User Awareness** | Regular training on supplier approval process and shadow IT risks |
| **Reporting Channel** | Easy mechanism for users to request new service evaluation |

## Shadow IT Discovery

**Discovery Methods:**

- Network traffic analysis (DNS queries, HTTPS SNI, cloud service IP ranges)
- Cloud Access Security Broker (CASB) monitoring
- Expense report analysis (software subscriptions, cloud service charges)
- User surveys and audits
- Credit card transaction monitoring (corporate cards)

**Discovery Response:**
1. Identify service and users
2. Assess risk (data access, criticality, compliance impact)
3. Decision: Approve retrospectively, migrate to approved alternative, or terminate
4. If approved: Execute expedited onboarding with risk acceptance
5. If terminated: Communicate to users, block access, migrate data if needed
6. Root cause analysis: Why did users bypass approval process?

---

# Roles & Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Business Owner** | Identify supplier need, maintain relationship, ensure service meets business requirements, budget approval |
| **Procurement** | Supplier selection process coordination, contract negotiation and management, competitive bidding |
| **Information Security Officer** | Risk assessment, security requirements definition, assessment review and approval, supplier register maintenance |
| **Legal/Compliance** | Contract review, regulatory compliance verification, data processing agreement review, dispute resolution |
| **IT Operations** | Technical implementation, access provisioning, integration support, performance monitoring |
| **CISO** | Policy approval, high-risk supplier approval, exception approval, executive reporting |
| **Data Protection Officer** | GDPR compliance verification, data processing agreement approval, privacy impact assessment |

**Responsibility Matrix** (RACI):

| Activity | Business Owner | Procurement | Security | Legal | IT Ops | CISO |
|----------|----------------|-------------|----------|-------|--------|------|
| Supplier identification | R | C | I | I | C | I |
| Risk assessment | C | C | R | C | C | A |
| Contract negotiation | I | R | C | R | I | I |
| Security review | I | I | R | C | C | A |
| Onboarding | C | C | C | I | R | I |
| Ongoing monitoring | A | C | R | I | C | I |
| Exception approval | I | I | C | C | I | A |

*R=Responsible, A=Accountable, C=Consulted, I=Informed*

---

# References

| Document | Relationship |
|----------|--------------|
| **ISMS-POL-A.5.19-23** | Parent policy framework |
| **ISMS-POL-A.5.19-23-S2** | Supplier agreement requirements (Control A.5.20) |
| **ISMS-POL-A.5.19-23-S3** | ICT supply chain security (Control A.5.21) |
| **ISMS-IMP-A.5.19-23.S1-UG/TG** | Cloud service inventory assessment workbook |
| **ISMS-IMP-A.5.19-23.S2-UG/TG** | Supplier due diligence assessment workbook |
| **ISO/IEC 27036-1:2021** | Information security for supplier relationships - Overview |
| **NIST SP 800-161** | Cybersecurity Supply Chain Risk Management |

---

**Next Document:** ISMS-POL-A.5.19-23-S2 — Supplier Agreement Requirements (Control A.5.20)

---

*"The strength of your security is only as strong as your weakest supplier."*
<!-- QA_VERIFIED: 2026-03-01 -->

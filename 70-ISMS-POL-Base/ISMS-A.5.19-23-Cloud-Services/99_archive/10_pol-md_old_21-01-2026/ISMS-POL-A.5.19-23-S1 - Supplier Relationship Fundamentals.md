# ISMS-POL-A.5.19-23-S1 — Supplier Relationship Fundamentals
## Control A.5.19: Information Security in Supplier Relationships

---

## Document Control

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
- ISMS-IMP-A.5.23-1 (Cloud Service Inventory & Classification)
- ISO/IEC 27001:2022 Control A.5.19
- ISO/IEC 27036-1 (Information security for supplier relationships - Overview and concepts)

---

## 1. Purpose

This section defines the foundational requirements for managing information security risks in supplier relationships. It establishes the classification framework, risk assessment methodology, and due diligence requirements that apply to all external suppliers.

**Control Objective (ISO 27002:2022):**
> "Processes and procedures shall be defined and implemented to manage the information security risks associated with the use of supplier's products or services."

---

## 2. Scope

### 2.1 Applicable Supplier Types

| Supplier Type | Description | Examples |
|---------------|-------------|----------|
| **Cloud Service Providers** | Providers of IaaS, PaaS, SaaS, XDR services | Compute, storage, email, security platforms |
| **Managed Service Providers** | Outsourced IT operations and support | Helpdesk, network management, SOC services |
| **Software Vendors** | Providers of licensed or subscription software | ERP, CRM, development tools |
| **Hardware Vendors** | Providers of physical IT equipment | Servers, network devices, endpoints |
| **Professional Services** | Consultants with system/data access | Auditors, integrators, developers |
| **Facilities Providers** | Data center and hosting services | Colocation, physical security |
| **Telecommunications** | Network and connectivity providers | Internet, WAN, voice services |

### 2.2 Exclusions

This policy does not apply to:

- Suppliers providing goods/services without access to organizational information
- One-time purchases with no ongoing relationship
- Individual consumers of the organization's services

---

## 3. Supplier Classification

### 3.1 Classification Criteria

Suppliers shall be classified based on the following factors:

| Factor | Weight | Assessment Questions |
|--------|--------|---------------------|
| **Data Access** | High | What data classification levels can the supplier access? |
| **System Access** | High | Does the supplier have access to production systems? |
| **Service Criticality** | High | Would supplier failure impact business operations? |
| **Replaceability** | Medium | How easily can the supplier be replaced? |
| **Integration Depth** | Medium | How deeply integrated are supplier services? |
| **Regulatory Impact** | High | Does the supplier affect regulatory compliance? |

### 3.2 Classification Levels

#### Level 1: Critical Suppliers

**Criteria (any one triggers Level 1):**
- Access to Restricted or Confidential data
- Direct access to production systems or infrastructure
- Single point of failure for critical business processes
- Regulatory compliance dependency

**Requirements:**
- Annual on-site or detailed remote assessment
- Quarterly performance and security reviews
- Documented business continuity plan
- Right-to-audit clause mandatory
- Executive sponsor assigned

#### Level 2: High-Risk Suppliers

**Criteria:**
- Access to Internal data classification
- Access to non-production systems (development, test)
- Important but not critical business function
- Multiple supplier options available

**Requirements:**
- Annual security assessment (questionnaire + evidence)
- Semi-annual performance reviews
- Business continuity considerations documented
- Right-to-audit clause recommended

#### Level 3: Medium-Risk Suppliers

**Criteria:**
- Limited data access (Public or minimal Internal)
- No direct system access
- Supporting business function
- Easily replaceable

**Requirements:**
- Biennial security assessment
- Annual performance review
- Standard contractual security clauses

#### Level 4: Low-Risk Suppliers

**Criteria:**
- No access to organizational data
- No system access
- Commodity services
- Multiple alternatives available

**Requirements:**
- Initial due diligence only
- Standard terms and conditions
- Review upon contract renewal

### 3.3 Classification Matrix

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

---

## 4. Supplier Risk Assessment

### 4.1 Risk Categories

| Category | Description | Assessment Focus |
|----------|-------------|------------------|
| **Confidentiality Risk** | Unauthorized disclosure of information | Data handling, access controls, encryption |
| **Integrity Risk** | Unauthorized modification of data/systems | Change management, input validation |
| **Availability Risk** | Service disruption or data loss | Redundancy, backup, disaster recovery |
| **Compliance Risk** | Regulatory or contractual violations | Certifications, audit reports, attestations |
| **Concentration Risk** | Over-reliance on single supplier | Market alternatives, exit feasibility |
| **Geopolitical Risk** | Jurisdictional or political factors | Data residency, legal frameworks |

### 4.2 Risk Assessment Process

**Step 1: Information Gathering**
- Supplier questionnaire completion
- Documentation review (certifications, policies)
- Technical documentation analysis

**Step 2: Risk Identification**
- Map supplier services to risk categories
- Identify potential threat scenarios
- Document existing controls (supplier + organization)

**Step 3: Risk Evaluation**
- Assess likelihood and impact
- Calculate risk score per category
- Determine overall supplier risk rating

**Step 4: Risk Treatment**
- Accept: Risk within tolerance
- Mitigate: Additional controls required
- Transfer: Insurance or contractual provisions
- Avoid: Do not proceed with supplier

### 4.3 Risk Scoring

| Likelihood | Impact: Low | Impact: Medium | Impact: High | Impact: Critical |
|------------|-------------|----------------|--------------|------------------|
| **Rare** | 1 | 2 | 3 | 4 |
| **Unlikely** | 2 | 4 | 6 | 8 |
| **Possible** | 3 | 6 | 9 | 12 |
| **Likely** | 4 | 8 | 12 | 16 |
| **Almost Certain** | 5 | 10 | 15 | 20 |

**Risk Rating Thresholds:**
- **1-4:** Low Risk → Standard controls
- **5-9:** Medium Risk → Enhanced controls
- **10-15:** High Risk → Significant controls + management approval
- **16-20:** Critical Risk → Executive approval + continuous monitoring

---

## 5. Due Diligence Requirements

### 5.1 Due Diligence by Classification Level

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

### 5.2 Security Certifications

**Preferred Certifications (in order of preference):**

| Certification | Scope | Validity |
|---------------|-------|----------|
| ISO/IEC 27001 | Information security management | 3 years (annual surveillance) |
| SOC 2 Type II | Trust service criteria | 12 months |
| SOC 2 Type I | Point-in-time assessment | Point-in-time |
| ISO/IEC 27017 | Cloud security controls | 3 years |
| ISO/IEC 27018 | Cloud privacy | 3 years |
| CSA STAR | Cloud security maturity | Varies by level |

**Certification Requirements by Level:**
- **Level 1:** ISO 27001 or SOC 2 Type II required
- **Level 2:** ISO 27001 or SOC 2 (Type I acceptable) required
- **Level 3:** Certification preferred but not mandatory
- **Level 4:** No certification requirement

### 5.3 Due Diligence Documentation

All due diligence activities shall be documented including:

- Completed security questionnaires
- Certification copies with validity dates
- Risk assessment results
- Decision rationale and approvals
- Identified gaps and remediation plans
- Compensating controls where applicable

---

## 6. Information Security Requirements

### 6.1 Baseline Requirements (All Suppliers with Data Access)

| Requirement | Description |
|-------------|-------------|
| **Access Control** | Least privilege, unique accounts, access logging |
| **Authentication** | Strong authentication, MFA for privileged access |
| **Encryption** | Data encrypted in transit (TLS 1.2+) |
| **Incident Reporting** | Security incidents reported within 24 hours |
| **Personnel Security** | Background checks for staff with access |
| **Confidentiality** | NDA or equivalent contractual commitment |

### 6.2 Enhanced Requirements (Level 1 & 2 Suppliers)

| Requirement | Description |
|-------------|-------------|
| **Encryption at Rest** | Data encrypted at rest with strong algorithms |
| **Vulnerability Management** | Regular scanning, timely patching |
| **Security Monitoring** | Logging, alerting, and retention |
| **Business Continuity** | Documented BC/DR plans and testing |
| **Audit Rights** | Organization may audit or review audit reports |
| **Subcontractor Controls** | Security requirements flow to subcontractors |

### 6.3 Requirements Communication

Security requirements shall be communicated to suppliers through:

- Security requirements appendix in contracts (see S2)
- Supplier security handbook (if applicable)
- Onboarding documentation
- Regular relationship reviews

---

## 7. Supplier Register

### 7.1 Register Requirements

The organization shall maintain a supplier register containing:

| Field | Description |
|-------|-------------|
| Supplier name | Legal entity name |
| Supplier type | Per Section 2.1 categories |
| Classification level | Level 1-4 per Section 3 |
| Services provided | Description of services/products |
| Data access | Classification of data accessible |
| System access | Systems supplier can access |
| Contract reference | Link to agreement |
| Business owner | Internal relationship owner |
| Security contact | Supplier security point of contact |
| Last assessment date | Most recent security assessment |
| Next review date | Scheduled review date |
| Risk rating | Current risk score |

### 7.2 Register Maintenance

- Register updated upon new supplier onboarding
- Register updated upon contract changes
- Quarterly review for accuracy
- Annual completeness audit

---

## 8. Roles & Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Business Owner** | Identify supplier need, maintain relationship, ensure compliance |
| **Procurement** | Supplier selection process, contract management |
| **Information Security** | Risk assessment, security requirements, assessment review |
| **Legal** | Contract review, regulatory compliance |
| **IT Operations** | Technical implementation, access provisioning |

---

## 9. References

| Document | Relationship |
|----------|--------------|
| ISMS-POL-A.5.19-23 | Parent policy framework |
| ISMS-POL-A.5.19-23-S2 | Supplier agreement requirements |
| ISMS-IMP-A.5.19-23.1 | Supplier inventory assessment workbook |
| ISMS-IMP-A.5.19-23.2 | Supplier evaluation workbook |

---

**Next Document:** ISMS-POL-A.5.19-23-S2 — Supplier Agreement Requirements (Control A.5.20)

---

*"The strength of your security is only as strong as your weakest supplier."*
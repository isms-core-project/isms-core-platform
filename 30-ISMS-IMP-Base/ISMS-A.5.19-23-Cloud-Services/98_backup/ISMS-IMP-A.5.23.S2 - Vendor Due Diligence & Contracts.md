# ISMS-IMP-A.5.23.S2 - Vendor Due Diligence & Contracts
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.5.23: Cloud Services Security

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S2 |
| **Version** | 1.0 |
| **Assessment Area** | Vendor Due Diligence & Contracts |
| **Related Policy** | ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements), ISMS-POL-A.5.19-23-S5 (Cloud Services Security), ISMS-POL-A.5.19-23-S6 (Assessment Methodology) |
| **Purpose** | Assess vendor security posture, contract adequacy, SLA compliance, data sovereignty, audit rights, and jurisdictional risks for all cloud service providers |
| **Target Audience** | Legal, Procurement, Finance, Security Teams, Compliance Officers, Risk Managers, Auditors |
| **Assessment Type** | Vendor Due Diligence & Contract Analysis |
| **Review Cycle** | Quarterly (with annual comprehensive review) |
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

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.23.S2 - Vendor Due Diligence & Contracts

#### What This Assessment Covers

This assessment evaluates the **security and contractual posture** of ALL cloud service providers identified in your cloud service inventory (ISMS-IMP-A.5.23.S1). This is where you verify that vendor claims match reality and that contracts protect [Organization]'s interests.

**Core Principle:**

**"Trust, but verify - every vendor relationship requires documented due diligence backed by objective evidence."**

This is NOT about collecting vendor marketing materials and checking boxes. This is about:
- ✅ Verifying vendor security certifications are CURRENT and VALID
- ✅ Analyzing contract terms to ensure adequate legal protection
- ✅ Tracking SLA performance against contractual commitments
- ✅ Documenting data residency and cross-border transfer compliance
- ✅ Establishing audit rights and forensic capabilities
- ✅ Assessing jurisdictional risks (especially for US-nexus providers)

This assessment answers critical questions:

- **Can we trust this vendor?** (Security posture, certifications, track record)
- **Are we protected legally?** (Contract terms, liability, indemnification)
- **Will they meet commitments?** (SLA performance, penalties, remediation)
- **Where is our data?** (Data residency, sovereignty, jurisdiction)
- **Can we audit them?** (Audit rights, forensic access, cooperation)
- **What are the legal risks?** (CLOUD Act exposure, regulatory conflicts)

#### What You'll Document

For EACH cloud service provider (from your A.5.23.1 inventory):

**Security Certifications (Sheet 2):**
- ISO 27001 certification (current, not expired)
- SOC 2 Type II reports (within last 12 months)
- FedRAMP authorization (if applicable)
- Industry-specific certifications (PCI-DSS, HIPAA, CSA STAR)
- Certificate scope verification
- Issuing body accreditation

**Contract Terms (Sheet 3):**
- Data Protection Agreement (DPA) adequacy
- Subprocessor disclosure and approval
- Liability caps and indemnification clauses
- Termination notice periods and exit rights
- Data return/deletion commitments
- Auto-renewal tracking
- DORA contract requirements (if EU financial entity)
- NIS2 supply chain security clauses (if EU essential/important entity)

**SLA Performance (Sheet 4):**
- Uptime commitments (monthly, annual)
- Support response times (by severity)
- Incident notification timeframes
- SLA penalty mechanisms (service credits)
- Actual performance vs. commitments
- Breach tracking and remediation

**Data Sovereignty (Sheet 5):**
- Data storage locations (geographic regions)
- Data processing locations
- Cross-border transfer mechanisms (SCCs, adequacy decisions)
- Data residency guarantees
- Encryption key custody (customer-managed vs. provider-managed)
- Regulatory compliance (GDPR, FADP, sector-specific)

**Forensics & Audit Rights (Sheet 6):**
- Right-to-audit clauses in contracts
- Audit frequency and scope
- Third-party audit report acceptance (alternative to direct audit)
- Forensic investigation support
- Log retention and access
- Incident investigation cooperation

**Jurisdictional Risk Assessment (Sheet 7):**
- Provider headquarters jurisdiction
- Parent company location (US-nexus detection)
- CLOUD Act potential exposure
- EU Data Boundary commitments
- Customer-managed encryption keys availability
- Jurisdictional risk rating (Low/Medium/High/Critical)
- Compensating controls documentation

**Compliance Metrics (Sheet 8):**
- Overall vendor compliance percentage
- Certification coverage (Critical/High services)
- Contract compliance (adequate terms)
- SLA performance trends
- Data sovereignty compliance
- Jurisdictional risk exposure

**Evidence Management (Sheet 9):**
- Master Service Agreements (MSAs)
- Data Processing Agreements (DPAs)
- Service Level Agreements (SLAs)
- Security certifications (ISO 27001, SOC 2)
- Audit reports (third-party)
- Vendor security questionnaires
- Incident response documentation
- Jurisdictional risk assessments

**Approval & Sign-Off (Sheet 10):**
- Legal review and approval
- Procurement review and approval
- Data Protection Officer (DPO) review
- CISO final approval
- Gap remediation tracking
- Risk acceptance documentation

#### How This Relates to Other A.5.23 Assessments

| Assessment | Focus | Relationship to A.5.23.2 |
|------------|-------|--------------------------|
| ISMS-IMP-A.5.23.S1 | Inventory & Classification | **PREREQUISITE** - Must complete FIRST to identify all vendors |
| **ISMS-IMP-A.5.23.S2** | **Vendor Due Diligence** | **WHO provides services, are they trustworthy, are contracts adequate** |
| ISMS-IMP-A.5.23.S3 | Secure Configuration | Uses vendor security capabilities documented here |
| ISMS-IMP-A.5.23.S4 | Ongoing Governance | Uses contract terms and SLAs documented here |
| ISMS-IMP-A.5.23.S5 | Compliance Dashboard | Aggregates vendor compliance metrics from this assessment |

**Critical Dependencies:**

**INPUT:** This assessment requires a completed and current ISMS-IMP-A.5.23.S1 (Cloud Service Inventory). You cannot assess vendors you haven't identified.

**OUTPUT:** Assessments A.5.23.3, A.5.23.4, and A.5.23.5 all depend on the vendor security posture, contract terms, and SLA commitments documented in THIS assessment.

**Workflow:** A.5.23.1 (Inventory) → **A.5.23.2 (Vendor DD)** → A.5.23.3 (Config) → A.5.23.4 (Governance) → A.5.23.5 (Dashboard)

### Who Should Complete This Assessment

#### Primary Stakeholders

This is a **CROSS-FUNCTIONAL assessment** requiring input from multiple teams:

1. **Legal** - Contract review, DPA adequacy, liability assessment, jurisdictional risk
2. **Procurement** - Vendor relationships, contract management, renewal tracking
3. **Finance** - Cost validation, SLA penalty tracking, financial stability assessment
4. **Security** - Certification verification, security posture assessment, risk rating
5. **Compliance** - Regulatory requirements (GDPR, FADP, DORA, NIS2), data sovereignty
6. **Data Protection Officer (DPO)** - Cross-border transfer approval, DPA review

#### Required Skills & Knowledge

**Technical Skills:**
- Understanding of security certifications (ISO 27001, SOC 2, FedRAMP)
- Contract analysis and negotiation experience
- Data protection regulations (GDPR, FADP, DORA, NIS2)
- SLA interpretation and performance measurement
- Jurisdictional risk assessment (CLOUD Act, data sovereignty)

**Process Skills:**
- Vendor relationship management
- Evidence collection and documentation
- Risk assessment and rating
- Cross-functional collaboration

**Access Requirements:**
- Contract management system (read access minimum, write preferred)
- Vendor portals (for certifications, SLA reports, audit reports)
- Financial systems (for cost validation)
- Legal document repository
- Procurement systems

#### Time Commitment

**Initial Assessment (from scratch):** 40-80 hours total

| Activity | Time (hours) |
|----------|--------------|
| Vendor identification (from A.5.23.1) | 2-4 |
| Contract collection and review | 12-20 |
| Certification verification | 8-12 |
| SLA analysis and performance tracking | 8-12 |
| Data sovereignty documentation | 6-10 |
| Audit rights verification | 4-6 |
| Jurisdictional risk assessment (NEW) | 6-10 |
| Evidence organization | 6-8 |
| Stakeholder approvals | 4-6 |

**Quarterly Updates:** 8-16 hours

| Activity | Time (hours) |
|----------|--------------|
| New vendor additions | 2-4 |
| Certificate renewal verification | 2-3 |
| SLA performance updates | 2-3 |
| Contract changes review | 1-2 |
| Jurisdictional risk updates | 1-2 |
| Evidence updates | 1-2 |

**Annual Comprehensive Review:** 20-30 hours
- Complete re-verification of all certifications
- Contract renewal analysis
- SLA performance trending
- Vendor risk re-assessment
- Jurisdictional risk re-evaluation

#### Collaboration Model

**This is NOT a solo activity.** Effective vendor due diligence requires orchestrated input:

**Recommended Approach:**

1. **Assessment Coordinator** (Security or Procurement)
   - Owns the assessment workbook
   - Coordinates input from all stakeholders
   - Tracks completion and evidence
   - Drives approval process

2. **Legal Team**
   - Reviews all contracts (MSA, DPA, SLA)
   - Assesses liability and indemnification clauses
   - Validates DORA/NIS2 regulatory clauses
   - Approves jurisdictional risk assessments

3. **Procurement Team**
   - Provides contract details and renewal dates
   - Tracks vendor relationships
   - Coordinates with vendors for missing documentation
   - Manages contract amendments

4. **Security Team**
   - Verifies security certifications
   - Assesses vendor security posture
   - Rates vendor risk (Low/Medium/High/Critical)
   - Reviews audit rights and forensic capabilities

5. **Compliance/DPO**
   - Validates data protection compliance
   - Approves cross-border data transfers
   - Reviews DPA adequacy
   - Assesses regulatory applicability (DORA, NIS2)

6. **Finance Team**
   - Validates costs and SLA penalties
   - Tracks financial impact of SLA breaches
   - Assesses vendor financial stability

### Expected Outputs

Upon completion, you will have:

1. ✅ **Verified vendor security posture** - Current certifications, validated scope, accredited issuers
2. ✅ **Analyzed contract terms** - DPA adequacy, liability protection, exit rights
3. ✅ **SLA performance baseline** - Commitments documented, penalties understood, performance tracked
4. ✅ **Data sovereignty compliance** - Data locations known, cross-border transfers approved
5. ✅ **Audit rights established** - Right-to-audit clauses verified, forensic capabilities documented
6. ✅ **Jurisdictional risks assessed** - CLOUD Act exposure evaluated, compensating controls identified
7. ✅ **Evidence repository** - All contracts, certifications, and audit reports organized
8. ✅ **Compliance dashboard** - Vendor-by-vendor compliance view with gap identification
9. ✅ **Approved assessment** - Multi-stakeholder approval (Legal, Procurement, DPO, CISO)
10. ✅ **Audit-ready documentation** - Objective evidence supporting all vendor relationships

### Assessment Success Criteria

You'll know this assessment is successful when:

**Completeness:**
- ✅ Every vendor from A.5.23.1 inventory has completed due diligence
- ✅ All required evidence collected (or gaps documented with remediation plans)
- ✅ All 10 sheets fully populated with current data
- ✅ No "Unknown" or "Not Assessed" statuses for Critical/High services

**Accuracy:**
- ✅ All certifications verified directly (not vendor claims)
- ✅ All contracts reviewed by Legal
- ✅ SLA performance data from authoritative sources (vendor dashboards, monitoring)
- ✅ Data residency confirmed in writing from vendors

**Currency:**
- ✅ Assessment completed within last 90 days
- ✅ Certificate expiry dates monitored (alerts for 60-day expiration)
- ✅ Contract renewal dates tracked (alerts for 90-day renewal)
- ✅ SLA performance updated monthly

**Auditability:**
- ✅ Every compliance status links to verifiable evidence
- ✅ Evidence Register includes document locations and retrieval methods
- ✅ Audit trail shows who assessed, when, and based on what evidence
- ✅ Gap remediation plans documented with target dates and owners

**Actionability:**
- ✅ Non-compliant vendors have remediation plans or risk acceptance
- ✅ Contract gaps identified with amendment requests
- ✅ SLA breaches tracked with vendor escalation
- ✅ Jurisdictional risks have documented compensating controls

**Stakeholder Approval:**
- ✅ Legal approved contract terms
- ✅ Procurement approved vendor relationships
- ✅ DPO approved cross-border data transfers
- ✅ CISO approved overall vendor risk posture

### Common Use Cases

**Use Case 1: New Vendor Onboarding**
- Security requires certification verification before approval
- Review vendor certifications (Sheet 2)
- Analyze proposed contract terms (Sheet 3)
- Assess jurisdictional risks (Sheet 7)
- Document in assessment workbook
- Route for Legal/CISO approval

**Use Case 2: Contract Renewal Preparation**
- Procurement needs to negotiate better terms
- Review current SLA performance (Sheet 4)
- Identify gaps in current contract (Sheet 3)
- Calculate SLA penalty utilization
- Prepare amendment requests
- Negotiate with evidence of underperformance

**Use Case 3: Audit Support**
- Auditor asks: "How do you verify vendor security?"
- Filter Sheet 2 by ISO 27001 = Yes (Current)
- Generate report with certification numbers and expiry dates
- Provide evidence from Evidence Register (Sheet 9)
- Demonstrate verification process and schedule

**Use Case 4: Data Breach Response**
- Vendor reports security incident
- Check contract notification requirements (Sheet 3)
- Verify incident response SLA (Sheet 4)
- Review audit rights (Sheet 6)
- Invoke forensic investigation clause
- Document incident and vendor response

**Use Case 5: Regulatory Compliance (DORA/NIS2)**
- Regulator requires supply chain security evidence
- Filter vendors by DORA/NIS2 applicability (Sheet 3, columns Y-Z)
- Generate report showing DORA contract clauses
- Demonstrate exit strategies (from A.5.23.1, Sheet 4)
- Provide evidence of ICT third-party risk management

**Use Case 6: CLOUD Act Risk Assessment**
- DPO requires jurisdictional risk analysis for US providers
- Filter Sheet 7 by Provider HQ = United States
- Review CLOUD Act exposure (Potential/Mitigated)
- Check EU Data Boundary commitment
- Verify customer-managed encryption keys
- Document compensating controls or risk acceptance

**Use Case 7: Vendor Consolidation**
- Finance wants to reduce vendor count
- Analyze vendor overlap (Sheet 8 Dashboard)
- Review contract terms for early termination penalties
- Assess migration feasibility (from A.5.23.1, Sheet 4)
- Calculate cost savings vs. migration costs
- Develop consolidation roadmap

**Use Case 8: SLA Performance Review**
- Business unit complains about vendor reliability
- Review historical SLA performance (Sheet 4)
- Calculate total service credits earned but not claimed
- Document pattern of SLA breaches
- Escalate to vendor management
- Consider alternative providers if pattern persists

---

**END OF SECTION 1: ASSESSMENT OVERVIEW**

## Section 2: Prerequisites & Preparation

### Before You Start

**Critical Dependencies - DO NOT START until these are in place:**

#### 1. Completed Cloud Service Inventory (MANDATORY)

**Requirement:** ISMS-IMP-A.5.23.S1 (Cloud Service Inventory) must be completed and current.

**Why:** You cannot assess vendors you haven't identified. The inventory provides:
- Complete list of cloud services
- Vendor names and service types
- Service criticality ratings
- Data classification per service
- Service owners and stakeholders

**Verification:**
```
✅ Check A.5.23.1 completion date (must be within 90 days)
✅ Verify all services have "Active" or "Production" status documented
✅ Confirm service owners identified for each cloud service
✅ Validate data classification assigned to each service
```

**If A.5.23.1 is incomplete:** STOP. Complete the inventory first. Attempting vendor due diligence without a complete service inventory results in:
- ❌ Missed vendors (shadow IT not assessed)
- ❌ Wasted effort (vendors for decommissioned services)
- ❌ Incorrect prioritization (criticality unknown)
- ❌ Audit failure (incomplete vendor coverage)

#### 2. Organizational Readiness

**Required Decisions:**

| Decision | Owner | Required Before Starting |
|----------|-------|--------------------------|
| Data classification scheme finalized | CISO | ✅ Yes - needed for data sovereignty assessment |
| Vendor risk rating methodology | Security | ✅ Yes - needed for consistent risk assessment |
| Acceptable certification types | Security/Compliance | ✅ Yes - ISO 27001, SOC 2, FedRAMP equivalency |
| Contract review standards | Legal | ✅ Yes - minimum acceptable terms |
| SLA penalty thresholds | Finance/Procurement | ✅ Yes - when to escalate/claim penalties |
| Jurisdictional risk tolerance | CISO/DPO/Legal | ✅ Yes - CLOUD Act acceptable risk level |

**Organizational Policies:**

Ensure these policies are approved and published:
- ✅ ISMS-POL-A.5.19-23-S2: Supplier Agreement Requirements
- ✅ ISMS-POL-A.5.19-23-S5: Cloud Services Security
- ✅ ISMS-POL-A.5.19-23-S6: Assessment Methodology & Automation

**If policies are in draft:** You can proceed with assessment but note policy status. Final approval may require policy-driven reassessment.

#### 3. Stakeholder Availability

**Confirm these stakeholders can commit time:**

| Stakeholder | Time Commitment | When Needed |
|-------------|-----------------|-------------|
| Legal Counsel | 12-20 hours | Week 1-2 (contract review) |
| Procurement Lead | 8-12 hours | Week 1 (contract collection), ongoing |
| Security Team | 10-15 hours | Week 2-3 (certification verification) |
| Compliance/DPO | 8-12 hours | Week 2-3 (data sovereignty, DORA/NIS2) |
| Finance | 4-6 hours | Week 3 (SLA penalty validation) |

**Scheduling Recommendation:**
- Week 1: Contract collection and initial review (Legal + Procurement)
- Week 2: Certification verification (Security + Compliance)
- Week 3: SLA analysis, data sovereignty, jurisdictional risk (All teams)
- Week 4: Evidence organization, gap remediation, approvals

#### 4. Tools & Systems Access

**Verify you have access to:**

| System | Access Level | Purpose |
|--------|--------------|---------|
| Contract Management System | Read (minimum), Write (preferred) | Contract retrieval, renewal tracking |
| Procurement System | Read | Vendor relationships, PO history |
| Finance System | Read | Vendor spend, invoice history |
| Legal Document Repository | Read | MSAs, DPAs, SLAs, amendments |
| Vendor Portals | Login credentials | Certifications, SLA reports, audit reports |
| SIEM/Monitoring Tools | Read | SLA performance data (uptime, incidents) |
| Ticketing System | Read | Vendor support response times |

**Access Provisioning Lead Time:** Request access 2-3 weeks before starting assessment if not already available.

### Required Access & Permissions

#### System Access Matrix

**Contract Management System:**
- **Read Access:** View all cloud vendor contracts
- **Write Access (preferred):** Update contract metadata, add renewal alerts
- **Export Access:** Generate contract reports, export attachments
- **Request From:** Procurement Manager or Contract Administrator

**Vendor Portals (Provider-Specific):**

| Vendor Type | Portal Access | What You'll Retrieve |
|-------------|---------------|----------------------|
| Major Cloud (AWS, Azure, GCP) | Admin or Billing console | Service health dashboard, SLA reports, compliance docs |
| SaaS Vendors | Admin portal | User analytics, uptime reports, security settings |
| Security Vendors | MSP/MSSP portal | SOC reports, incident logs, security analytics |

**Access Request Template:**
```
To: [Vendor Account Manager]
Subject: Request for Compliance Documentation Access

We are conducting our quarterly vendor security assessment per 
ISO 27001:2022 Control A.5.23. Please provide access to:

1. Customer portal for compliance documentation
2. Current ISO 27001 / SOC 2 certificates
3. SLA performance reports (last 12 months)
4. Third-party audit reports (if available)
5. Subprocessor list (current)
6. Data residency documentation

Required for: [Service Name] - Contract Reference: [CONTRACT-ID]
Requested by: [Name, Title]
Deadline: [Date - allow 2-3 weeks]
```

**Internal Documentation:**

| Document Type | Location | Custodian |
|---------------|----------|-----------|
| Master Service Agreements | Legal repository / Contract mgmt | Legal |
| Data Processing Agreements | Legal repository / Compliance | Legal / DPO |
| Service Level Agreements | Procurement / Contract mgmt | Procurement |
| Security certifications | Vendor management system | Procurement / Security |
| Vendor security questionnaires | Security / GRC platform | Security |
| Vendor risk assessments | GRC platform / Risk register | Risk Management |

### Information Sources

#### Primary Sources (Highest Trust)

**1. Direct Vendor Documentation:**
- Official security certifications (PDF from issuing body or vendor portal)
- Audit reports (SOC 2 Type II) - request directly from vendor
- Contract documents - signed/executed versions only
- SLA performance reports - from vendor customer portal
- Subprocessor lists - from vendor website or legal team

**2. Third-Party Verification:**
- ISO 27001 certificates - verify with issuing certification body (e.g., BSI, ANAB)
- FedRAMP authorization - verify on FedRAMP Marketplace (fedramp.gov)
- CSA STAR registry - verify on cloudsecurityalliance.org
- Trust service providers - vendor trust centers (e.g., trust.salesforce.com)

**3. Internal Records:**
- Contract management system (executed contracts)
- Procurement system (vendor onboarding records)
- Ticketing system (support response times, incident tickets)
- Monitoring systems (actual uptime data)
- Financial systems (costs, invoices, penalty claims)

#### Secondary Sources (Lower Trust - Verify)

**Vendor Marketing Materials:**
- Security white papers (claims require verification)
- Website compliance pages (check dates, verify certificates)
- Sales presentations (marketing claims, not evidence)
- RFP responses (requires contractual binding)

**⚠️ WARNING:** Never accept vendor self-attestation without verification. Example:

❌ **UNACCEPTABLE:** "Vendor website says 'ISO 27001 certified'" → Status: Compliant  
✅ **REQUIRED:** "ISO 27001 certificate #12345, issued by BSI, valid until 2026-06-30, verified on BSI website" → Status: Compliant

#### Prohibited Sources

**DO NOT USE:**
- ❌ Vendor sales claims without supporting evidence
- ❌ Outdated certifications (expired)
- ❌ Screenshots of certificates (forgery risk)
- ❌ Verbal assurances from vendor sales/account teams
- ❌ "Certification in progress" (not a certification)

**Evidence Standard:** If an auditor would reject it, don't use it.

### Discovery Methods

#### Contract Discovery

**Method 1: Contract Management System Query**
```
Query Parameters:
- Vendor Type: Cloud Services, SaaS, IaaS, PaaS, Security Services
- Status: Active, Pending Renewal
- Contract Type: MSA, DPA, SLA, Subscription Agreement
- Date Range: Current + Next 12 months (for renewal planning)

Expected Output: List of all active cloud vendor contracts
```

**Method 2: Procurement System Cross-Reference**
```
Query Parameters:
- Spend Category: Cloud Services, Software Subscriptions, IT Services
- Vendor Classification: Cloud Provider, SaaS Vendor
- Spend Amount: >$1,000 annually (captures meaningful relationships)
- Payment Method: All (credit card spend often indicates shadow IT)

Expected Output: Vendor spend report → cross-check against contract inventory
```

**Method 3: Finance System Invoice Analysis**
```
Analyze Last 12 Months:
- Recurring monthly charges to cloud vendors
- Annual subscription renewals
- Usage-based billing (AWS, Azure, GCP)

Cross-Reference: Compare against known contracts
Red Flag: Regular payments to vendors without executed contracts
```

**Method 4: Service Owner Interviews**

For each service from A.5.23.1 inventory:
```
Questions for Service Owner:
1. Who is the vendor? (Validate against A.5.23.1)
2. Do we have a signed contract? (Location?)
3. When does the contract renew? (Add to tracking)
4. What SLA commitments exist? (Document for Sheet 4)
5. Have we experienced SLA breaches? (Performance baseline)
6. Where is our data stored? (Data sovereignty - Sheet 5)
```

#### Certification Discovery

**Method 1: Direct Vendor Request**

**Email Template:**
```
Subject: Security Certification Request - [Service Name]

Dear [Vendor Account Manager],

As part of our ongoing compliance requirements (ISO 27001:2022), 
please provide current security certifications for [Service Name]:

Required Certifications:
☐ ISO 27001 certificate (PDF, current, not expired)
☐ SOC 2 Type II report (most recent, within 12 months)
☐ FedRAMP authorization (if applicable)
☐ Industry-specific certifications (PCI-DSS, HIPAA, etc.)

For each certification, please include:
- Certificate/report PDF (official copy)
- Certificate number and issuing body
- Scope of certification (which services covered)
- Expiration/report date
- Accreditation of issuing body (if not globally recognized)

Deadline: [Date + 14 days]
Internal Reference: [Organization] Vendor Assessment Q[X] 2026

Thank you,
[Name, Title]
```

**Method 2: Vendor Trust Centers**

Major vendors publish certifications on trust centers:
- AWS: https://aws.amazon.com/compliance/
- Azure: https://learn.microsoft.com/en-us/compliance/
- Google Cloud: https://cloud.google.com/security/compliance
- Salesforce: https://trust.salesforce.com/
- Microsoft 365: https://learn.microsoft.com/en-us/compliance/

**Verification Required:** Always verify certificate numbers with issuing bodies.

**Method 3: Third-Party Registries**

| Registry | Coverage | Verification Method |
|----------|----------|---------------------|
| FedRAMP Marketplace | US government cloud authorizations | Search provider, verify authorization level |
| CSA STAR Registry | Cloud security certifications | Search provider, verify STAR level |
| ISO 27001 Registrars | Global ISO certifications | Contact issuing body (BSI, ANAB, etc.) |

**Method 4: Contract Appendices**

Many MSAs include security certifications as appendices:
- Check Section: "Security and Compliance"
- Look For: "Exhibit A: Security Certifications"
- Verify: Certificate dates are current

#### SLA Discovery

**Method 1: Contract Review**

SLAs may be embedded in:
- Standalone SLA document (preferred)
- Schedule/Exhibit in MSA (common)
- Order form or Statement of Work
- Online terms of service (less common for enterprise)

**Search For:**
- Uptime commitments (e.g., "99.9% monthly uptime")
- Support response times (by severity level)
- Incident notification requirements
- Performance benchmarks (latency, throughput)
- Penalty mechanisms (service credits, refunds)

**Method 2: Vendor Customer Portal**

Most enterprise cloud vendors provide SLA reporting:
- AWS: Service Health Dashboard + Personal Health Dashboard
- Azure: Azure Status + Service Health
- Google Cloud: Cloud Status Dashboard
- SaaS vendors: Admin portal → Reports → SLA/Uptime

**Method 3: Monitoring Systems**

Cross-reference vendor SLA claims with actual monitoring:
- Uptime monitoring (Pingdom, UptimeRobot, Datadog)
- Application performance monitoring (APM)
- SIEM event logs (service availability, incidents)

**Discrepancy Example:**
```
Vendor Claim: 99.95% uptime SLA
Monitoring Data: 99.7% actual uptime (last 12 months)
Action: Calculate SLA penalties, escalate to vendor
```

### Stakeholder Coordination

#### Kick-Off Meeting Agenda

**Attendees:** Legal, Procurement, Security, Compliance/DPO, Finance, Assessment Coordinator

**Agenda (90 minutes):**

1. **Assessment Overview** (15 min)
   - Purpose and scope
   - Timeline and milestones
   - Expected outputs

2. **Roles & Responsibilities** (20 min)
   - Who completes which sheets
   - Evidence collection ownership
   - Approval workflow
   - Escalation paths

3. **Current State Review** (20 min)
   - A.5.23.1 inventory review (which vendors require assessment)
   - Known gaps or challenges
   - Vendor relationships requiring special handling

4. **Access & Tools** (15 min)
   - System access verification
   - Vendor portal credentials
   - Document repository access
   - Workbook distribution

5. **Evidence Standards** (15 min)
   - What constitutes acceptable evidence
   - Verification requirements
   - Documentation standards
   - Evidence storage

6. **Timeline & Milestones** (10 min)
   - Week-by-week plan
   - Deliverable deadlines
   - Review checkpoints
   - Final approval target

**Action Items:**
- [ ] Assign sheet completion owners
- [ ] Distribute vendor lists (by owner)
- [ ] Request system access (where needed)
- [ ] Schedule weekly status calls
- [ ] Establish shared evidence repository

#### Collaboration Tools

**Shared Workbook Management:**

**Option 1: Shared Network Drive**
- Pros: Simple, familiar, version control via filename
- Cons: Concurrent editing conflicts, manual merges
- Best For: Small teams (<5 people), sequential workflow

**Option 2: SharePoint / OneDrive**
- Pros: Real-time collaboration, version history, comments
- Cons: Excel Online limitations, formula performance
- Best For: Medium teams (5-15 people), collaborative workflow

**Option 3: Contract Management System Integration**
- Pros: Direct contract linking, automated updates, audit trail
- Cons: Requires system customization, IT involvement
- Best For: Large organizations, mature contract management

**Recommended:** SharePoint with check-out/check-in workflow for large updates.

**Evidence Repository Structure:**
```
/Vendor-Due-Diligence-Evidence/
├── Contracts/
│   ├── MSA-Vendor-AWS-2024.pdf
│   ├── DPA-Vendor-Azure-2025.pdf
│   └── SLA-Vendor-Salesforce-2024.pdf
├── Certifications/
│   ├── ISO27001-AWS-Cert-2024-2027.pdf
│   ├── SOC2-Salesforce-TypeII-2025.pdf
│   └── FedRAMP-Azure-Authorization-2024.pdf
├── Audit-Reports/
│   ├── SOC2-Report-Vendor-A-2025.pdf
│   └── Third-Party-Audit-Vendor-B-2024.pdf
├── SLA-Reports/
│   ├── AWS-SLA-Performance-Q1-2026.pdf
│   └── Azure-Uptime-Report-2025.xlsx
├── Jurisdictional-Assessments/
│   ├── CLOUD-Act-Assessment-AWS-2026.pdf
│   └── Data-Residency-Confirmation-Azure-2025.pdf
└── Vendor-Questionnaires/
    ├── Security-Questionnaire-Vendor-A-2025.pdf
    └── DORA-Vendor-Assessment-Vendor-B-2026.pdf
```

**Naming Convention:**
```
[Document-Type]-[Vendor-Name]-[Year]-[Version].pdf

Examples:
MSA-Salesforce-2024-v2.pdf
ISO27001-AWS-2024-2027.pdf (cert valid 2024-2027)
SOC2-TypeII-Google-2025.pdf
```

### Initial Data Collection

#### Week 1: Contract Collection

**Objective:** Locate and centralize all cloud vendor contracts.

**Tasks:**

1. **Query Contract Management System**
   - Export all cloud vendor contracts (active status)
   - Download PDFs and attachments
   - Note missing contracts (vendor has no executed agreement)

2. **Cross-Reference with A.5.23.1 Inventory**
   - For each cloud service, identify vendor
   - Check if contract exists
   - Flag gaps: Service in use but no contract

3. **Organize by Vendor**
   - Group all contracts per vendor (MSA, DPA, SLA, amendments)
   - Identify master vs. service-specific agreements
   - Note contract hierarchies (MSA governs all services)

4. **Missing Contract Action**
   - For vendors with no contract: Escalate to Procurement
   - For expired contracts: Flag for urgent renewal
   - For verbal agreements: Document and escalate (high risk)

**Deliverable:** Complete contract inventory with all PDFs centralized.

#### Week 2: Certification Verification

**Objective:** Collect and verify all vendor security certifications.

**Tasks:**

1. **Request Certifications from Vendors**
   - Send standardized request (template above)
   - Track responses in workbook
   - Follow up on non-responses at Day 7

2. **Download from Vendor Trust Centers**
   - Visit vendor compliance pages
   - Download current certificates
   - Note certificate numbers for verification

3. **Verify Certifications**
   - ISO 27001: Contact issuing body or check online registry
   - SOC 2: Verify report date (within 12 months)
   - FedRAMP: Check FedRAMP Marketplace
   - CSA STAR: Check CSA STAR Registry

4. **Document Findings**
   - Certificate number, issuer, expiry date
   - Scope of certification
   - Verification method and date
   - Flag expired or missing certifications

**Deliverable:** Verified certification status for all vendors.

#### Week 3: SLA & Data Sovereignty Collection

**Objective:** Extract SLA commitments and document data residency.

**Tasks:**

1. **Extract SLA Terms from Contracts**
   - Locate SLA document or section
   - Document uptime commitments
   - Note support response times
   - Identify penalty mechanisms

2. **Collect SLA Performance Data**
   - Download vendor SLA reports (last 12 months)
   - Export monitoring data (uptime, incidents)
   - Calculate actual performance vs. commitments

3. **Document Data Residency**
   - Identify data storage regions (from contract/vendor)
   - Confirm data processing locations
   - Note cross-border transfer mechanisms
   - Verify data residency guarantees

4. **Assess Jurisdictional Risks**
   - Identify US-headquartered providers
   - Check for US parent companies
   - Document CLOUD Act exposure
   - Verify EU Data Boundary commitments
   - Check customer-managed encryption key availability

**Deliverable:** Complete SLA and data sovereignty documentation.

---

**END OF SECTION 2: PREREQUISITES & PREPARATION**

## Section 3: Understanding the Assessment Sheets

### Workbook Structure Overview

The ISMS-IMP-A.5.23.S2 assessment workbook consists of **10 sheets** organized to support both **data collection** (Sheets 2-7) and **synthesis** (Sheets 8-10):
```
┌─────────────────────────────────────────────────────────────────┐
│           ISMS-IMP-A.5.23.S2 WORKBOOK STRUCTURE                  │
│                   (10 Sheets Total)                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  SHEET 1: INSTRUCTIONS & LEGEND                          │  │
│  │  - How to use the workbook                               │  │
│  │  - Status legend and color codes                         │  │
│  │  - Acceptable evidence examples                          │  │
│  │  - Regulatory applicability guide (DORA, NIS2, CLOUD)    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                          ↓                                      │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  DATA COLLECTION SHEETS (2-7)                            │  │
│  │                                                          │  │
│  │  Sheet 2: Vendor Security Certifications                │  │
│  │           ISO 27001, SOC 2, FedRAMP verification         │  │
│  │                                                          │  │
│  │  Sheet 3: Contract Terms Analysis                       │  │
│  │           DPA, liability, termination, DORA/NIS2         │  │
│  │                                                          │  │
│  │  Sheet 4: SLA Requirements & Performance                │  │
│  │           Uptime, support, penalties, tracking           │  │
│  │                                                          │  │
│  │  Sheet 5: Data Sovereignty & Jurisdiction               │  │
│  │           Data residency, cross-border transfers         │  │
│  │                                                          │  │
│  │  Sheet 6: Forensics & Audit Rights                      │  │
│  │           Right-to-audit, forensic capabilities          │  │
│  │                                                          │  │
│  │  Sheet 7: Jurisdictional Risk Assessment     │  │
│  │           CLOUD Act, US-nexus, EU Data Boundary          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                          ↓                                      │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  SYNTHESIS SHEETS (8-10)                                 │  │
│  │                                                          │  │
│  │  Sheet 8: Summary Dashboard                             │  │
│  │           Auto-calculated metrics, compliance stats      │  │
│  │                                                          │  │
│  │  Sheet 9: Evidence Register                             │  │
│  │           Document tracking, evidence locations          │  │
│  │                                                          │  │
│  │  Sheet 10: Approval Sign-Off                            │  │
│  │            Multi-stakeholder approval workflow           │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Sheet-by-Sheet Purpose

#### Sheet 1: Instructions & Legend

**Purpose:** Provides comprehensive guidance on workbook use, status definitions, and regulatory applicability.

**Key Sections:**
- Document information block (assessment date, completed by, organization)
- How to use this workbook (9-step process)
- Status legend (✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A)
- Acceptable evidence examples (MSA, DPA, SLA, certifications)
- Regulatory applicability guidance (DORA, NIS2, AI Act, CLOUD Act)
- CLOUD Act considerations

**Who Uses This:**
- ALL stakeholders (first-time users)
- Assessment coordinator (reference for evidence standards)
- Auditors (understanding methodology and compliance criteria)

**Critical Information:**
- Regulatory applicability matrix (which fields are mandatory for your organization)
- Evidence standards (what constitutes "acceptable evidence")
- Status definitions (objective criteria for each rating)

---

#### Sheet 2: Vendor Security Certifications

**Purpose:** Document and verify vendor security certifications (ISO 27001, SOC 2, FedRAMP, etc.).

**Assessment Question:** *"Do your cloud service vendors hold current security certifications?"*

**What You'll Document:**
- ISO 27001 certification status (current, expired, none)
- Certificate number and expiry date
- SOC 2 Type II report availability and date
- FedRAMP authorization level (if applicable)
- Other certifications (PCI-DSS, HIPAA, CSA STAR)

**Column Structure:**
- **Columns A-Q:** Standard vendor information (service name, vendor, criticality, status, evidence, gaps)
- **Columns R-X:** Certification-specific details (ISO 27001, SOC 2, FedRAMP, other)

**Key Verification Principle:**
> "Certificate on vendor website is a CLAIM. Certificate verified with issuing body is EVIDENCE."

**Common Gaps:**
- Expired ISO 27001 certificates (vendor hasn't renewed)
- SOC 2 reports older than 12 months (stale assurance)
- Certificate scope doesn't cover the service in use
- Issuing body not accredited (unrecognized certifier)

**Who Completes This:**
- **Primary:** Security Team (certification verification expertise)
- **Support:** Procurement (vendor contact for certificate requests)
- **Review:** Compliance (adequacy of certifications for regulatory needs)

**Typical Entry Count:** 20-50 vendors (one row per vendor, not per service)

**Completion Time:** 8-12 hours (including verification with issuing bodies)

---

#### Sheet 3: Contract Terms Analysis

**Purpose:** Analyze contract terms for security, data protection, liability, and regulatory compliance.

**Assessment Question:** *"Have all cloud service contracts been reviewed for security and data protection clauses?"*

**What You'll Document:**
- Data protection clause adequacy (GDPR, FADP compliant)
- Subprocessor disclosure (list provided, generic, none)
- Liability caps and indemnification clauses
- Termination notice period and data return commitments
- Auto-renewal tracking
- DORA contract requirements (Columns Y-Z)
- NIS2 supply chain security clauses

**Column Structure:**
- **Columns A-Q:** Standard vendor information
- **Columns R-X:** Contract term details (DPA, liability, termination, data return)
- **Columns Y-Z:** DORA/NIS2 regulatory clauses

**Key Analysis Principle:**
> "A contract protects you only to the extent its terms are enforceable and adequate for the data/service criticality."

**Critical Contract Elements to Verify:**

| Contract Element | What to Look For | Red Flag |
|------------------|------------------|----------|
| Data Protection Clause | Explicit GDPR/FADP compliance reference | Generic "reasonable care" without specifics |
| Subprocessor List | Named subprocessors with locations | "We may use subprocessors at our discretion" |
| Liability Cap | Reasonable for service criticality (e.g., 12 months fees) | $100 cap for Critical service |
| Indemnification | Covers data breaches, IP infringement | "To maximum extent permitted by law" (minimal) |
| Termination Period | ≤90 days for non-critical, ≤60 for critical | 180+ days (vendor lock-in risk) |
| Data Return | 30-day window with format specification | "Upon request" without timeline |

**DORA/NIS2 Applicability:**

If [Organization] is:
- **EU Financial Entity (DORA scope):** Columns Y-Z MANDATORY
- **EU Essential/Important Entity (NIS2):** Columns Y-Z MANDATORY  
- **Neither:** Mark columns as "N/A"

**Who Completes This:**
- **Primary:** Legal (contract interpretation, risk assessment)
- **Support:** Procurement (contract retrieval, vendor negotiation history)
- **Review:** Compliance/DPO (data protection adequacy)

**Typical Entry Count:** 20-50 vendors (one per unique contract, not per service)

**Completion Time:** 12-20 hours (detailed contract review is time-intensive)

---

#### Sheet 4: SLA Requirements & Performance

**Purpose:** Document SLA commitments and track actual performance against contractual obligations.

**Assessment Question:** *"Are vendor SLA commitments documented and is performance tracked?"*

**What You'll Document:**
- Uptime commitments (monthly percentage, e.g., 99.9%)
- Support response times (by incident severity)
- Incident notification timeframes
- SLA penalty mechanisms (service credits, refunds)
- Actual performance vs. commitments (last 12 months)
- SLA breach tracking and remediation

**Column Structure:**
- **Columns A-Q:** Standard vendor information
- **Columns R-AA:** SLA commitments and performance tracking

**Key Performance Principle:**
> "SLAs without performance tracking are vendor promises without accountability."

**SLA Performance Calculation Example:**
```
Vendor Commitment: 99.9% monthly uptime
Actual Performance: 99.7% (Jan-Dec 2025 average)

SLA Breach: Yes
  - Jan: 99.65% ❌ (below 99.9%)
  - Feb: 99.92% ✅
  - Mar: 99.50% ❌ (below 99.9%)
  - ... (10 more months)

Breaches: 4 months out of 12
Service Credits Owed: 4 months × [penalty per breach]
Service Credits Claimed: 0 (not escalated to vendor)

Action Required: 
  1. Calculate total credits owed
  2. Submit credit claim to vendor
  3. Review if pattern warrants vendor review/replacement
```

**Common SLA Gaps:**
- SLA exists but no performance tracking (vendor accountability missing)
- Uptime SLA but no support response time SLA (support quality unmeasured)
- SLA penalties too low to motivate vendor (e.g., 5% credit for 90% uptime)
- Performance data contradicts vendor SLA reports (independent monitoring needed)

**Who Completes This:**
- **Primary:** IT Operations (performance monitoring, incident tracking)
- **Support:** Procurement (SLA terms extraction from contracts)
- **Review:** Finance (penalty calculation, credit claims)

**Typical Entry Count:** 20-50 vendors

**Completion Time:** 8-12 hours (requires cross-referencing monitoring data with SLA terms)

---

#### Sheet 5: Data Sovereignty & Jurisdiction

**Purpose:** Document data storage/processing locations and assess cross-border transfer compliance.

**Assessment Question:** *"Is data residency documented and compliant with regulatory requirements?"*

**What You'll Document:**
- Data storage location (geographic region, country, data center)
- Data processing location (may differ from storage)
- Cross-border data transfer mechanisms (SCCs, adequacy decision, none)
- Data residency guarantees (contractual commitment)
- Encryption key custody (customer-managed vs. provider-managed)
- Regulatory compliance (GDPR, FADP, sector-specific)

**Column Structure:**
- **Columns A-Q:** Standard vendor information
- **Columns R-Y:** Data sovereignty details

**Key Sovereignty Principle:**
> "Data stored in the EU is not necessarily 'EU data' if provider can access it from US (CLOUD Act risk)."

**Data Residency Scenarios:**

| Scenario | Data Location | Provider HQ | Encryption | Risk Level | Assessment |
|----------|---------------|-------------|------------|------------|------------|
| 1 | EU (Frankfurt) | EU (Ireland) | Provider-managed | Low | ✅ Standard EU deployment |
| 2 | EU (Frankfurt) | US (Virginia) | Provider-managed | High | ⚠️ CLOUD Act exposure (see Sheet 7) |
| 3 | EU (Frankfurt) | US (Virginia) | Customer-managed | Medium | ⚠️ Keys mitigate but jurisdiction risk remains |
| 4 | US (Virginia) | US (Virginia) | Provider-managed | Critical | ❌ Non-compliant for EU Confidential/Restricted data |
| 5 | Multi-region | US (Virginia) | Customer-managed + EU Boundary | Low-Medium | ⚠️ Verify EU Data Boundary commitment (Sheet 7) |

**Cross-Border Transfer Mechanisms:**

| Mechanism | Adequacy | Use Case | Limitations |
|-----------|----------|----------|-------------|
| EU Adequacy Decision | High | Transfers to approved countries (UK, Switzerland post-Brexit) | Limited countries approved |
| Standard Contractual Clauses (SCCs) | Medium-High | Transfers to non-adequate countries | Requires supplementary measures assessment |
| Binding Corporate Rules (BCRs) | High | Intra-company transfers (multinational) | Only for internal group transfers |
| None (EU-only) | Highest | No cross-border transfer | Requires EU-only provider or deployment |

**Who Completes This:**
- **Primary:** Compliance/DPO (data protection expertise, regulatory interpretation)
- **Support:** IT Operations (technical verification of data locations)
- **Review:** Legal (cross-border transfer mechanism adequacy)

**Typical Entry Count:** 20-50 vendors

**Completion Time:** 6-10 hours (requires detailed vendor documentation review)

---

#### Sheet 6: Forensics & Audit Rights

**Purpose:** Verify contractual audit rights and vendor forensic investigation capabilities.

**Assessment Question:** *"Do contracts include adequate audit rights and forensic investigation support?"*

**What You'll Document:**
- Right-to-audit clause presence and scope
- Audit frequency allowed (annual, upon cause, unlimited)
- Third-party audit report acceptance (alternative to direct audit)
- Forensic investigation support commitments
- Log retention period and access
- Incident investigation cooperation clauses

**Column Structure:**
- **Columns A-Q:** Standard vendor information
- **Columns R-W:** Audit and forensic capability details

**Key Audit Principle:**
> "Without contractual audit rights, you have vendor assurances but no verification capability."

**Audit Rights by Vendor Criticality:**

| Vendor Level | Minimum Audit Rights | Acceptable Alternative |
|--------------|---------------------|------------------------|
| Critical (L1) | Full on-site/remote audit rights, annual + upon cause | NONE - direct audit rights required |
| High (L2) | Audit rights OR current third-party report (SOC 2) | SOC 2 Type II within 12 months |
| Medium (L3) | Third-party report acceptance | SOC 2 Type II or ISO 27001 cert |
| Low (L4) | No specific requirement | N/A |

**Forensic Investigation Scenarios:**

**Scenario 1: Data Breach at Vendor**
```
Requirement: Forensic log access for breach investigation
Contract Clause: "Vendor shall provide forensic-level access to relevant 
                 logs within 24 hours of breach notification"
Evidence: Contract section reference, log access procedure documented
Status: ✅ Compliant
```

**Scenario 2: Suspected Unauthorized Access**
```
Requirement: Incident investigation cooperation
Contract Clause: "Vendor will cooperate with reasonable investigation 
                 requests" (VAGUE)
Evidence: Generic cooperation clause, no SLA for response
Gap: No specific timeline or scope defined
Status: ⚠️ Partial - requires amendment for specificity
```

**Common Audit Gaps:**
- No audit clause in contract (no verification right)
- Audit "upon mutual agreement" (vendor can refuse)
- Audit only during business hours with 90-day notice (emergency incident unaddressed)
- Audit cost entirely borne by customer (discourages exercise of right)
- Third-party reports not required to be current (accepting 3-year-old SOC 2)

**Who Completes This:**
- **Primary:** Legal (contract clause interpretation)
- **Support:** Security (forensic capability assessment)
- **Review:** Compliance (adequacy for regulatory audit requirements)

**Typical Entry Count:** 20-50 vendors

**Completion Time:** 4-6 hours

---

#### Sheet 7: Jurisdictional Risk Assessment

**Purpose:** Assess legal jurisdiction risks, particularly CLOUD Act exposure for US-nexus providers.

**Assessment Question:** *"Have jurisdictional risks been assessed for vendors with US nexus?"*

**What You'll Document:**
- Provider headquarters jurisdiction
- Parent company location (US nexus detection)
- CLOUD Act potential exposure (unmitigated, mitigated, N/A)
- EU Data Boundary commitment (yes/no)
- Customer-managed encryption keys availability
- Jurisdictional risk rating (Low, Medium, High, Critical)
- Compensating controls (if risk accepted)

**Column Structure:**
- **Columns A-Q:** Standard vendor information
- **Columns R-T:** Jurisdictional risk assessment

**Key Jurisdictional Principle:**
> "The CLOUD Act allows US government access to data held by US companies worldwide, regardless of data location."

**CLOUD Act Exposure Matrix:**

| Provider HQ | Data Location | Keys | EU Boundary | Exposure | Risk Level |
|-------------|---------------|------|-------------|----------|------------|
| US | US | Provider | No | Direct | Critical ❌ |
| US | EU | Provider | No | Via CLOUD Act | High ⚠️ |
| US | EU | Customer | No | Mitigated (keys) | Medium ⚠️ |
| US | EU | Customer | Yes | Mitigated (keys + boundary) | Low-Medium ✅ |
| EU | EU | Provider | N/A | None (EU jurisdiction) | Low ✅ |
| EU | EU | Customer | N/A | None | Low ✅ |

**Understanding CLOUD Act Status:**

**"Potential Exposure (Unmitigated)":**
- US-headquartered provider OR US parent company
- Data stored/processed in EU
- Provider-managed encryption keys
- No EU Data Boundary commitment
- **Risk:** US government could compel provider to access EU data via CLOUD Act
- **Action Required:** Assess if acceptable for data classification, document compensating controls or migrate

**"Mitigated (Partial)":**
- Customer-managed encryption keys deployed
- Provider cannot technically access plaintext data
- **Limitation:** Metadata, backups, or key escrow may still be accessible
- **Action Required:** Verify key management architecture, assess residual risk

**"Mitigated (Strong)":**
- Customer-managed keys AND EU Data Boundary commitment
- Provider contractually commits to EU-only operations for your data
- **Limitation:** Contractual commitment strength depends on enforceability
- **Action Required:** Verify contract clause, monitor compliance

**Compensating Controls for CLOUD Act Risk:**

| Control | Effectiveness | Implementation |
|---------|---------------|----------------|
| Customer-Managed Encryption Keys (CMK) | High | Deploy Azure CMK, AWS KMS with customer keys, Google CMEK |
| EU Data Boundary Commitment | Medium | Contract clause requiring EU-only data processing |
| Data Minimization | Medium | Reduce volume/sensitivity of data in cloud |
| Alternative Provider (EU-HQ) | High | Migrate to EU-headquartered provider (OVH, Scaleway, T-Systems) |
| Risk Acceptance | Low | Document risk, obtain CISO/DPO sign-off |

**Who Completes This (NEW - requires multi-disciplinary team):**
- **Primary:** Compliance/DPO (jurisdictional risk expertise, CLOUD Act interpretation)
- **Support:** Legal (contract review, enforceability assessment)
- **Support:** Security (technical controls verification - CMK, encryption architecture)
- **Review:** CISO (risk acceptance for High/Critical exposures)

**Applicability:**
- **Mandatory:** For all US-headquartered providers (AWS, Azure, Google Cloud, Salesforce, etc.)
- **Mandatory:** For non-US providers with US parent companies
- **Optional:** For EU-headquartered providers (mark as "N/A - EU Jurisdiction")

**Typical Entry Count:** 10-30 vendors (only those with US nexus)

**Completion Time:** 6-10 hours (complex legal/technical assessment)

---

#### Sheet 8: Summary Dashboard

**Purpose:** Auto-calculate compliance metrics and provide executive summary view.

**Assessment Question:** *"What is the overall vendor compliance status?"*

**What This Sheet Provides (Auto-Calculated):**

**Section 1: Overall Compliance Statistics**
- Total vendors assessed
- Overall compliance percentage
- Vendors by status (Compliant, Partial, Non-Compliant)
- Critical/High services compliance rate

**Section 2: Compliance by Assessment Area**
- Security certifications coverage
- Contract terms compliance
- SLA performance compliance
- Data sovereignty compliance
- Audit rights adequacy
- Jurisdictional risk exposure

**Section 3: Gap Analysis**
- Vendors without ISO 27001 / SOC 2
- Contracts missing DPA or inadequate terms
- SLA breaches requiring escalation
- Data sovereignty violations
- Missing audit rights
- High/Critical jurisdictional risks

**Section 4: Jurisdictional Metrics**
- Providers with US nexus
- CLOUD Act potential exposure (unmitigated)
- CLOUD Act mitigated (with CMK/EU Boundary)
- High/Critical jurisdictional risks
- Providers without EU Data Boundary
- Providers without customer-managed keys

**Who Uses This:**
- **Executive Leadership:** High-level compliance view
- **CISO:** Risk concentration and gap prioritization
- **Auditors:** Compliance coverage verification
- **Assessment Coordinator:** Progress tracking

**Key Principle:**
> "This sheet tells you AT A GLANCE where you're compliant, where you have gaps, and what requires escalation."

**No Manual Entry Required:** All data flows from Sheets 2-7 via formulas.

---

#### Sheet 9: Evidence Register

**Purpose:** Track all evidence documents supporting vendor assessments (audit trail).

**What You'll Document:**
- Evidence ID (auto-generated: EV-VDD-001, EV-VDD-002, etc.)
- Evidence type (MSA, DPA, SLA, ISO 27001, SOC 2, etc.)
- Vendor name
- Document title
- Document date
- Storage location (file path, URL, contract management system ID)
- Collected by (person who obtained evidence)
- Collection date

**Evidence Types:**

| Type | Description | Typical Count per Vendor |
|------|-------------|--------------------------|
| MSA | Master Service Agreement | 1 |
| DPA | Data Processing Agreement | 1 |
| SLA | Service Level Agreement | 1-2 |
| ISO 27001 | ISO 27001 Certificate | 1 |
| SOC 2 | SOC 2 Type II Report | 1 |
| FedRAMP | FedRAMP Authorization | 0-1 |
| Audit Report | Third-party audit report | 0-2 |
| Vendor Questionnaire | Security questionnaire | 1 |
| SLA Report | SLA performance report | 1-4 (quarterly) |
| Jurisdictional Assessment | CLOUD Act risk assessment | 0-1 |

**Key Evidence Principle:**
> "Every 'Compliant' status in Sheets 2-7 MUST have corresponding evidence in Sheet 9."

**Who Completes This:**
- **Primary:** Assessment Coordinator (centralized evidence tracking)
- **Contributors:** All team members (as they collect evidence)

**Typical Entry Count:** 150-300 evidence items (for 30-50 vendors)

**Completion Time:** 6-8 hours (concurrent with evidence collection)

---

#### Sheet 10: Approval Sign-Off

**Purpose:** Multi-stakeholder approval workflow for final assessment validation.

**Approval Sequence:**
```
Legal Review
    ↓
Procurement Review
    ↓
Data Protection Officer (DPO) Review
    ↓
CISO Approval
    ↓
Assessment Complete
```

**What Each Approver Validates:**

| Approver | Focus | Key Questions |
|----------|-------|---------------|
| **Legal** | Contract adequacy, liability | Are contracts enforceable? Adequate liability protection? |
| **Procurement** | Vendor relationships, renewals | Are vendor relationships documented? Renewals tracked? |
| **DPO** | Data protection, cross-border transfers | Are DPAs adequate? Cross-border transfers approved? |
| **CISO** | Overall security posture, risk | Is vendor risk acceptable? Gaps have remediation plans? |

**Assessment Summary (Auto-Populated from Sheet 8):**
- Total vendors assessed
- Compliance percentage
- Non-compliant vendors count
- Gaps requiring remediation
- Jurisdictional risks identified

**Approval Status Tracking:**
- Reviewed by (name)
- Review date
- Status (Approved, Approved with Conditions, Rejected)
- Comments (gap concerns, remediation requirements)

**Who Completes This:**
- Each approver signs off sequentially
- Assessment Coordinator coordinates approval workflow

---

### Sheet Interconnections & Data Flow

**Primary Data Flow:**
```
Sheet 1 (Instructions)
    ↓ (provides guidance)
Sheets 2-7 (Data Collection)
    ↓ (data flows via formulas)
Sheet 8 (Summary Dashboard - auto-calculated)
    ↓ (evidence IDs referenced)
Sheet 9 (Evidence Register)
    ↓ (summary metrics flow to)
Sheet 10 (Approval Sign-Off)
```

**Cross-Sheet References:**

| Source Sheet | Target Sheet | Data Flowing |
|--------------|--------------|--------------|
| Sheet 2 (Certifications) | Sheet 8 (Dashboard) | Compliance statistics |
| Sheet 3 (Contracts) | Sheet 8 (Dashboard) | Contract adequacy metrics |
| Sheet 4 (SLAs) | Sheet 8 (Dashboard) | SLA performance trends |
| Sheet 5 (Data Sovereignty) | Sheet 8 (Dashboard) | Data residency compliance |
| Sheet 6 (Audit Rights) | Sheet 8 (Dashboard) | Audit rights coverage |
| Sheet 7 (Jurisdictional) | Sheet 8 (Dashboard) | Jurisdictional risk metrics (NEW) |
| All Sheets 2-7 | Sheet 9 (Evidence) | Evidence IDs (Column I references) |
| Sheet 8 (Dashboard) | Sheet 10 (Approval) | Summary statistics for approval review |

### Stakeholder View: Which Sheets Matter Most

**Legal Team:**
- **Primary:** Sheet 3 (Contract Terms), Sheet 7 (Jurisdictional Risk)
- **Secondary:** Sheet 6 (Audit Rights), Sheet 5 (Data Sovereignty)
- **Review:** Sheet 10 (Approval Sign-Off)

**Procurement Team:**
- **Primary:** Sheet 3 (Contract Terms), Sheet 4 (SLA Performance)
- **Secondary:** Sheet 2 (Certifications - for RFPs)
- **Review:** Sheet 8 (Dashboard), Sheet 10 (Approval)

**Security Team:**
- **Primary:** Sheet 2 (Certifications), Sheet 6 (Audit Rights)
- **Secondary:** Sheet 7 (Jurisdictional Risk - technical controls)
- **Review:** Sheet 8 (Dashboard)

**Compliance/DPO:**
- **Primary:** Sheet 5 (Data Sovereignty), Sheet 7 (Jurisdictional Risk)
- **Secondary:** Sheet 3 (Contract Terms - DPA review)
- **Review:** Sheet 8 (Dashboard), Sheet 10 (Approval Sign-Off)

**Finance Team:**
- **Primary:** Sheet 4 (SLA Performance - penalty tracking)
- **Secondary:** Sheet 8 (Dashboard - cost of non-compliance)
- **Review:** None (informational only)

**Executive Leadership / CISO:**
- **Primary:** Sheet 8 (Summary Dashboard)
- **Review:** Sheet 10 (Approval Sign-Off)
- **Drill-Down:** Any sheet for gap details

---

**END OF SECTION 3: UNDERSTANDING THE ASSESSMENT SHEETS**

## Section 4: Completing Each Sheet - Detailed Guidance

### Overview: Completing Assessment Sheets

This section provides **step-by-step guidance** for completing each data collection sheet (Sheets 2-7). Each subsection follows this structure:

1. **Sheet Purpose Recap** - Why this sheet matters
2. **Column-by-Column Guidance** - How to complete each field
3. **Evidence Requirements** - What documentation to collect
4. **Verification Steps** - How to validate information
5. **Common Mistakes** - What to avoid
6. **Quality Checks** - How to verify completion quality
7. **Example Entries** - Good vs. problematic entries

### General Column Structure (Sheets 2-7)

**All data collection sheets share a common base structure (Columns A-Q):**

| Column | Header | Purpose | Source |
|--------|--------|---------|--------|
| A | Cloud Service Name | Service as YOU know it | A.5.23.1 Inventory |
| B | Vendor Name | Provider's legal name | Contract, vendor website |
| C | Service Type | SaaS, IaaS, PaaS, etc. | A.5.23.1 Inventory |
| D | Service Criticality | Critical, High, Medium, Low | A.5.23.1 Inventory |
| E | Data Classification | Public, Internal, Confidential, Restricted | A.5.23.1 Inventory |
| F | Contract Type | MSA+DPA, Subscription, etc. | Contract review |
| G | Contract Start Date | When contract became effective | Contract (signature page) |
| H | Status | ✅/⚠️/❌/N/A | Assessment result |
| I | Evidence Location | Where evidence is stored | Evidence Register |
| J | Gap Description | What's missing or inadequate | Analysis |
| K | Remediation Needed | Yes/No | Gap analysis |
| L | Exception ID | Reference to risk acceptance | Exception register |
| M | Risk ID | Reference to risk register | Risk register |
| N | Compensating Controls | Mitigating measures | Security team |
| O | Vendor Contact (Legal) | Vendor legal/compliance contact | Contract, vendor portal |
| P | Target Remediation Date | When gap will be closed | Remediation plan |
| Q | Contract Owner | Internal person responsible | Procurement/Business owner |

**Key Principle for Base Columns:**
- Copy from A.5.23.1 inventory where applicable (Columns A-E)
- Do NOT re-assess criticality or data classification here (maintain consistency)
- Status (Column H) is assessment-specific (varies by sheet)
- Evidence Location (Column I) references Sheet 9 (Evidence Register)

---

### Sheet 2: Vendor Security Certifications

#### Purpose Recap

**Goal:** Verify that vendors hold current, valid security certifications appropriate for the criticality and data classification of services they provide.

**Why This Matters:**
- Certifications provide independent assurance of vendor security controls
- Expired certifications indicate potential control degradation
- Mismatched scope (certification doesn't cover your service) provides no assurance
- Unaccredited certifiers provide weak assurance

**Success Criterion:**
> All Critical and High services are provided by vendors with current ISO 27001 or SOC 2 Type II certification, verified directly with issuing bodies.

#### Column-by-Column Guidance

**Columns A-Q: Base Information**

Follow general guidance above. Key points:

**Column B (Vendor Name):**
- Use vendor's legal entity name (from contract)
- Example: "Microsoft Corporation" not "Microsoft 365"
- Example: "Amazon Web Services, Inc." not "AWS"
- **Why:** Certifications are issued to legal entities, not product brands

**Column H (Status):**
| Status | Criteria | When to Use |
|--------|----------|-------------|
| ✅ Compliant | Current ISO 27001 OR SOC 2 Type II (within 12 months), scope covers service, verified | Critical/High: ISO 27001/SOC 2 required AND verified |
| ⚠️ Partial | Has certification but expired, OR scope unclear, OR not verified | Certification exists but has issues |
| ❌ Non-Compliant | No certification, OR certification from unaccredited body | Critical/High service with no valid certification |
| N/A | Not applicable (e.g., Low criticality, no certification required by policy) | Low/Medium services where policy allows no certification |

**Columns R-X: Certification-Specific Details**

**Column R: ISO 27001 Certified**

**Options:**
- `Yes (Current)` - Certificate not expired, verified as current
- `Yes (Expired)` - Certificate exists but past expiry date
- `No` - No ISO 27001 certification
- `Unknown` - Vendor claims certification but not verified

**How to Complete:**
1. Request certificate PDF from vendor
2. Check expiry date (typically 3-year validity)
3. Note certificate number
4. Verify with issuing body (next column)

**Verification Method:**
```
Step 1: Obtain certificate PDF (from vendor or trust center)
Step 2: Extract details:
  - Certificate number: ISO27001-XXXXXX
  - Issuing body: BSI, ANAB, etc.
  - Issue date: DD.MM.YYYY
  - Expiry date: DD.MM.YYYY
Step 3: Verify with issuing body:
  - BSI: https://www.bsigroup.com/en-GB/validate-bsi-issued-certificates/
  - ANAB: Contact ANAB directly
  - Other: Check issuer's verification portal
Step 4: Confirm expiry date is in future
Step 5: Update status
```

**Common Mistakes:**
- ❌ Accepting "ISO 27001 compliant" claim without certificate
- ❌ Using certificate screenshot from vendor website (forgery risk)
- ❌ Not checking expiry date (expired certificate = no assurance)
- ❌ Not verifying issuing body is accredited (ISO requires accreditation)

**Column S: ISO 27001 Cert Number**

**Format:** Certificate number as shown on certificate

**Examples:**
- `ISO27001-12345-2024`
- `IS 750968` (BSI format)
- `27001-2024-001` (varies by issuer)

**How to Complete:**
1. Locate certificate number on certificate PDF
2. Copy exactly as shown (include any prefixes/suffixes)
3. Do NOT invent or guess format

**Why This Matters:**
- Certificate number enables verification with issuing body
- Auditors will verify certificate numbers independently
- Incorrect numbers indicate unverified certificates

**Column T: ISO 27001 Expiry Date**

**Format:** DD.MM.YYYY

**How to Complete:**
1. Locate expiry date on certificate (usually 3 years from issue)
2. Enter in DD.MM.YYYY format
3. Set up calendar reminder at Expiry Date - 60 days (renewal tracking)

**Critical Dates:**
- Expiry Date - 90 days: Notify vendor to initiate renewal
- Expiry Date - 60 days: Escalate if no renewal evidence
- Expiry Date - 30 days: Escalate to CISO, consider service suspension risk
- Expiry Date: Certificate invalid, status changes to ❌ Non-Compliant

**Column U: SOC 2 Type II Report**

**Options:**
- `Yes (< 6 months)` - Report issued within last 6 months (fresh assurance)
- `Yes (6-12 months)` - Report issued 6-12 months ago (acceptable but aging)
- `No` - No SOC 2 report available
- `Unknown` - Vendor claims SOC 2 but report not obtained

**How to Complete:**
1. Request SOC 2 Type II report from vendor
2. Check report date (not opinion date - look for "examination period ended")
3. Calculate age: Today - Report End Date
4. Select appropriate option

**SOC 2 vs SOC 3:**
- **SOC 2 Type II:** Detailed report (50-100+ pages), requires NDA, shows test results
- **SOC 3:** Summary report (2-5 pages), public, no test details
- **Policy:** SOC 2 Type II required for Critical/High services, SOC 3 insufficient

**Understanding Report Age:**

| Report Age | Assurance Level | Acceptability |
|------------|-----------------|---------------|
| 0-6 months | High | ✅ Preferred |
| 6-12 months | Medium | ⚠️ Acceptable, request refresh |
| 12-18 months | Low | ❌ Too old, require current report |
| 18+ months | Very Low | ❌ Unacceptable, outdated controls |

**Column V: SOC 2 Report Date**

**Format:** DD.MM.YYYY (examination period end date)

**How to Complete:**
1. Open SOC 2 Type II report PDF
2. Locate "examination period" (e.g., "1 January 2025 - 30 June 2025")
3. Use END date (30 June 2025 in example)
4. Enter in DD.MM.YYYY format (30.06.2025)

**Why End Date, Not Issue Date:**
- End date = controls were tested through this date
- Issue date (report publication) may be weeks/months after examination period
- Examination end date determines assurance currency

**Column W: FedRAMP Authorized**

**Options:**
- `Yes (High)` - FedRAMP High authorization
- `Yes (Moderate)` - FedRAMP Moderate authorization
- `Yes (Low)` - FedRAMP Low authorization (rare, mostly legacy)
- `No` - No FedRAMP authorization
- `N/A` - Not applicable (non-US government workloads)

**How to Complete:**
1. Check FedRAMP Marketplace: https://marketplace.fedramp.gov/
2. Search for vendor/product
3. Note authorization level
4. Verify authorization is current (not "In Process" or "Rescinded")

**When FedRAMP Matters:**
- US government customers (MANDATORY)
- Regulated industries often accept FedRAMP as strong security baseline
- Some EU organizations accept FedRAMP High as equivalent to ISO 27001

**When to Mark N/A:**
- No US government workloads
- Not processing US federal data
- Vendor doesn't offer FedRAMP-authorized services

**Column X: Other Certifications**

**Format:** Free text, comma-separated list

**Common Other Certifications:**
- `PCI-DSS` - Payment card data handling
- `HIPAA` - US healthcare data (note: no official "HIPAA certification", vendor may claim "HIPAA compliant")
- `CSA STAR Level 2` - Cloud Security Alliance certification
- `C5` - German BSI Cloud Computing Compliance Criteria
- `ISO 9001` - Quality management (not security, but indicates process maturity)
- `ISO 20000` - IT service management
- `TISAX` - Automotive industry security

**How to Complete:**
1. Review vendor trust center / compliance page
2. List certifications relevant to service/industry
3. Note if verification needed (e.g., PCI-DSS for payment processing)

**What NOT to Include:**
- ❌ "GDPR compliant" (not a certification, it's a legal requirement)
- ❌ "Best practices" or "industry standards" without specific certification
- ❌ Vendor internal audits (not third-party certifications)

**Example Entries:**
- ✅ `PCI-DSS Level 1, CSA STAR Level 2, ISO 9001`
- ✅ `C5 (Germany), MTCS (Singapore)`
- ❌ `GDPR, Best Practices, Internal Audit Passed`

#### Evidence Requirements

**For Each Vendor:**

**MUST HAVE (Critical/High Services):**
- ✅ ISO 27001 certificate PDF (official copy, not screenshot)
- ✅ OR SOC 2 Type II report (complete report, under NDA)
- ✅ Certificate verification record (email from issuing body, website verification screenshot)

**SHOULD HAVE:**
- ✅ Vendor trust center URL (for ongoing monitoring)
- ✅ Certificate scope statement (which services covered)
- ✅ Issuing body accreditation verification

**NICE TO HAVE:**
- ✅ Historical certificates (shows continuous certification)
- ✅ Surveillance audit confirmations (annual checks during 3-year cycle)

**Evidence Storage:**
```
/Evidence/Certifications/
├── ISO27001/
│   ├── Vendor-A-ISO27001-Cert-2024-2027.pdf
│   ├── Vendor-A-ISO27001-Verification-BSI-2024.pdf
│   └── Vendor-A-ISO27001-Scope-Statement.pdf
├── SOC2/
│   ├── Vendor-B-SOC2-TypeII-2025.pdf (under NDA)
│   └── Vendor-B-SOC2-Request-Email-2025.pdf
└── FedRAMP/
    └── Vendor-C-FedRAMP-High-Authorization-2024.pdf
```

#### Verification Steps

**Step-by-Step Verification Process:**

**1. Certificate Collection (Week 2, Days 1-3):**
```
For each vendor (from A.5.23.1 inventory):
  [ ] Request certificates via email (use template from Section 2)
  [ ] Download from vendor trust center
  [ ] Retrieve from contract appendices
  [ ] Log request in tracking spreadsheet
```

**2. Certificate Review (Week 2, Days 4-5):**
```
For each certificate received:
  [ ] Open PDF, visually inspect for authenticity markers
  [ ] Verify certificate number present
  [ ] Check issue and expiry dates
  [ ] Verify issuing body name
  [ ] Read scope statement (which services/locations covered)
  [ ] Note any exclusions or limitations
```

**3. Certificate Verification (Week 2-3):**
```
For ISO 27001:
  [ ] Visit issuing body website (BSI, ANAB, etc.)
  [ ] Use certificate verification tool
  [ ] Enter certificate number
  [ ] Confirm status = Valid, expiry date matches
  [ ] Take screenshot of verification result
  [ ] Save to Evidence Register

For SOC 2:
  [ ] Confirm report is Type II (not Type I)
  [ ] Verify examination period end date
  [ ] Check report is signed by CPA firm
  [ ] Verify CPA firm is AICPA member (if US)
  [ ] Review opinion (unqualified = clean, qualified = concerns)

For FedRAMP:
  [ ] Visit FedRAMP Marketplace
  [ ] Search provider and product
  [ ] Verify authorization status = Authorized (not In Process)
  [ ] Note authorization level (High, Moderate, Low)
  [ ] Verify authorization date and agency sponsor
```

**4. Gap Documentation (Week 3):**
```
For vendors without required certifications:
  [ ] Document gap in Column J
  [ ] Determine if compensating controls exist (Column N)
  [ ] Escalate to Security/CISO for risk assessment
  [ ] Decide: Require certification, accept risk, or replace vendor
  [ ] Document decision in Column L (Exception ID) or M (Risk ID)
  [ ] Set remediation date (Column P) if vendor will obtain cert
```

#### Common Mistakes & How to Avoid Them

**Mistake 1: Accepting Expired Certificates**

❌ **Wrong:**
```
Vendor: "We're ISO 27001 certified"
Assessor: Marks "Yes (Current)" without checking expiry
Reality: Certificate expired 8 months ago
```

✅ **Right:**
```
Vendor: "We're ISO 27001 certified"
Assessor: Requests certificate PDF
Assessor: Checks expiry date = 15.03.2025 (past)
Assessor: Marks "Yes (Expired)" → Status: ⚠️ Partial
Assessor: Requests renewal evidence
```

**Mistake 2: Not Verifying Scope**

❌ **Wrong:**
```
Certificate: "ISO 27001 for Company XYZ corporate offices (UK)"
Service Used: Cloud hosting (AWS re-sold by XYZ)
Assessor: Marks compliant (certificate exists)
Reality: Scope doesn't cover cloud services
```

✅ **Right:**
```
Certificate scope: Review scope statement
Scope covers: Corporate IT (UK offices only)
Service location: Cloud hosting (global)
Assessment: Scope mismatch
Status: ❌ Non-Compliant (certification doesn't cover service used)
Action: Request separate cloud services certification
```

**Mistake 3: Confusing SOC 2 Type I and Type II**

❌ **Wrong:**
```
Vendor provides: SOC 2 Type I report
Assessor: Marks "Yes (< 6 months)"
Reality: Type I = design review only, no testing
```

✅ **Right:**
```
Vendor provides: SOC 2 Type I report
Assessor: Recognizes Type I = design only, not operating effectiveness
Policy requires: Type II (controls tested over time)
Status: ❌ Non-Compliant (wrong SOC report type)
Action: Request SOC 2 Type II or accept risk
```

**Mistake 4: Accepting Unaccredited Certifiers**

❌ **Wrong:**
```
Certificate: "ISO 27001 Certified by ABC Audit Services Inc."
ABC Audit Services: Not an accredited certification body
Assessor: Marks compliant (certificate exists)
Reality: Worthless certificate (not from accredited body)
```

✅ **Right:**
```
Certificate from: ABC Audit Services Inc.
Verification: Check if ABC is accredited by IAF (International Accreditation Forum)
Result: Not found in accredited body list
Assessment: Certificate not valid (unaccredited issuer)
Status: ❌ Non-Compliant
Action: Require certification from accredited body (BSI, ANAB, TUV, etc.)
```

#### Quality Checks

**Self-Check Before Marking Sheet 2 Complete:**

**Completeness:**
- [ ] All vendors from A.5.23.1 inventory have entries
- [ ] All Critical/High vendors have certification status documented
- [ ] All certificate numbers recorded (where applicable)
- [ ] All expiry dates entered (where applicable)
- [ ] All gaps have remediation plans or risk acceptance

**Accuracy:**
- [ ] All ISO 27001 certificates verified with issuing bodies
- [ ] All SOC 2 reports are Type II (not Type I)
- [ ] All SOC 2 report dates are within 12 months
- [ ] FedRAMP authorizations verified on FedRAMP Marketplace
- [ ] Certificate scopes reviewed for service coverage

**Evidence:**
- [ ] All certificate PDFs saved to Evidence Register (Sheet 9)
- [ ] All verification records saved (screenshots, emails)
- [ ] Evidence Location (Column I) populated for all vendors

**Consistency:**
- [ ] Status (Column H) matches certification reality
- [ ] Gaps (Column J) explain all ⚠️ Partial and ❌ Non-Compliant statuses
- [ ] Compensating controls (Column N) documented for accepted risks

**Auditability:**
- [ ] Auditor could verify every "Compliant" status from evidence
- [ ] No "Unknown" statuses remain (all verified)
- [ ] Verification dates within last 90 days

#### Example Entries

**Example 1: Fully Compliant Vendor (AWS)**

| Column | Value |
|--------|-------|
| A | Amazon EC2 Compute |
| B | Amazon Web Services, Inc. |
| C | IaaS |
| D | Critical |
| E | Confidential |
| R | Yes (Current) |
| S | IS 750968 |
| T | 30.09.2026 |
| U | Yes (< 6 months) |
| V | 31.12.2025 |
| W | Yes (High) |
| X | PCI-DSS, CSA STAR Level 2 |
| H | ✅ Compliant |
| I | EV-VDD-001, EV-VDD-002 |
| J | (empty - no gaps) |

**Example 2: Partial Compliance (Expired ISO 27001)**

| Column | Value |
|--------|-------|
| A | CRM Platform |
| B | Vendor XYZ Ltd |
| C | SaaS |
| D | High |
| E | Confidential |
| R | Yes (Expired) |
| S | ISO27001-12345 |
| T | 15.08.2025 (EXPIRED) |
| U | Yes (6-12 months) |
| V | 30.06.2025 |
| W | No |
| X | None |
| H | ⚠️ Partial |
| I | EV-VDD-015 |
| J | ISO 27001 expired 15.08.2025, renewal pending |
| K | Yes |
| P | 28.02.2026 (vendor committed renewal date) |

**Example 3: Non-Compliant (No Certification)**

| Column | Value |
|--------|-------|
| A | Project Management Tool |
| B | Small Vendor Inc. |
| C | SaaS |
| D | High |
| E | Internal |
| R | No |
| S | (empty) |
| T | (empty) |
| U | No |
| V | (empty) |
| W | N/A |
| X | None |
| H | ❌ Non-Compliant |
| I | (no evidence available) |
| J | No security certifications, vendor claims "not needed for small company" |
| K | Yes |
| N | Alternative: Vendor questionnaire completed, annual pen test required |
| M | RISK-2026-042 |
| P | 30.06.2026 (obtain ISO 27001 or migrate to alternative) |

---

### Sheet 3: Contract Terms Analysis

#### Purpose Recap

**Goal:** Verify that contracts contain adequate security, data protection, liability, and regulatory compliance clauses.

**Why This Matters:**
- Contracts are your legal protection when things go wrong
- Inadequate DPAs expose you to GDPR/FADP violations
- Weak liability clauses mean vendors bear no consequences for failures
- Missing DORA/NIS2 clauses mean regulatory non-compliance

**Success Criterion:**
> All Critical and High vendors have contracts with adequate data protection clauses, liability provisions, termination rights, and (where applicable) DORA/NIS2 compliance.

#### Column-by-Column Guidance

**Columns A-Q: Base Information**

Follow general guidance. Key points:

**Column F (Contract Type):**

**Options:**
- `MSA + DPA` - Master Service Agreement + Data Processing Agreement (preferred for GDPR/FADP)
- `Subscription Agreement` - SaaS subscription (may include DPA as schedule)
- `Pay-As-You-Go` - Usage-based (AWS, Azure, GCP - DPA often separate)
- `Trial` - Pilot/proof-of-concept (temporary, limited terms)
- `Custom` - Negotiated bespoke agreement

**How to Determine:**
1. Review contract document title
2. Check for separate DPA document or DPA schedule/exhibit
3. Note if multiple documents govern relationship (MSA + DPA + SLA)

**Column G (Contract Start Date):**

**Format:** DD.MM.YYYY

**How to Complete:**
1. Locate signature page (usually end of contract)
2. Find "Effective Date" or "Commencement Date"
3. Use effective date, NOT signature date (may differ)
4. If no effective date specified, use later signature date

**Why This Matters:**
- Determines contract anniversary (renewal tracking)
- Establishes when terms became binding
- Used to calculate notice periods for termination

**Columns R-X: Contract Terms Details**

**Column R: Data Protection Clause**

**Options:**
- `Yes (Adequate)` - DPA meets GDPR/FADP requirements, clear processor obligations
- `Yes (Weak)` - DPA exists but generic, minimal commitments
- `No` - No data protection clause or DPA
- `Under Negotiation` - Contract being amended to add/improve DPA

**Assessment Criteria for "Adequate":**

| Requirement | Must Include |
|-------------|--------------|
| Roles defined | Clear designation: Controller vs. Processor |
| Processing purpose | Limited to service delivery (no secondary use) |
| Data categories | Specific types of personal data (not just "customer data") |
| Data subjects | Categories of individuals (employees, customers, etc.) |
| Processing location | Geographic restrictions if required (EU-only, Swiss-only) |
| Security measures | Reference to ISO 27001 or specific controls |
| Subprocessor rules | Prior written consent OR pre-approved list with notification |
| Data subject rights | Support for access, deletion, portability, objection |
| Breach notification | 24-48 hour notification requirement |
| Audit cooperation | Support for DPA audits, regulatory investigations |
| Data return/deletion | Process and timeline upon termination (30-60 days) |

**How to Complete:**
1. Locate DPA document or DPA section in MSA
2. Review against criteria above
3. Count how many requirements are met:
   - 10-11 met: `Yes (Adequate)`
   - 6-9 met: `Yes (Weak)` → requires amendment
   - 0-5 met: `No` or `Yes (Weak)` depending on gaps

**Red Flags:**
- ❌ No mention of GDPR or data protection regulations
- ❌ Vendor reserves right to use data for "improving services" (secondary use)
- ❌ No subprocessor disclosure or approval mechanism
- ❌ Breach notification "as soon as reasonably practicable" (too vague)

**Column S: Subprocessor Disclosure**

**Options:**
- `Yes (List Provided)` - Vendor provides specific list of subprocessors with names and locations
- `Yes (Generic)` - Vendor mentions subprocessors but no specific list
- `No` - No subprocessor information in contract

**Assessment:**

**"Yes (List Provided)" Example:**
```
Contract includes:
  Exhibit B: Subprocessors
    1. AWS (data hosting) - Ireland, Germany
    2. Zendesk (customer support) - US (EU Data Residency enabled)
    3. Stripe (payment processing) - US, EU
  
  Vendor commits to:
    - Notify 30 days before adding new subprocessors
    - Allow customer objection (vendor must find alternative or allow termination)
```

**"Yes (Generic)" Example:**
```
Contract states:
  "Vendor may engage subprocessors to perform certain processing activities."
  
  Problems:
    - No list of current subprocessors
    - No notification mechanism for new subprocessors
    - No objection right
```

**Why This Matters:**
- GDPR Art. 28 requires controller awareness of subprocessors
- You're responsible for subprocessor compliance (chain of responsibility)
- Subprocessors in non-adequate countries create transfer risk

**How to Complete:**
1. Search contract for "subprocessor", "sub-processor", "third party"
2. Check if Exhibit/Schedule with list exists
3. If list exists, verify it includes names and locations
4. If generic language only, mark `Yes (Generic)` → requires amendment

**Column T: Liability Cap (CHF)**

**Format:** Free text (describe cap)

**Examples:**
- `CHF 1M annual fees (greater of)`
- `CHF 5M or 12 months fees`
- `Unlimited (data breach, IP infringement)` (rare, negotiate if possible)
- `CHF 100 total` (unacceptable for Critical/High services)

**How to Complete:**
1. Locate "Limitation of Liability" or "Liability" section
2. Identify cap amount
3. Note if different caps for different breach types:
   - General liability (usually capped)
   - Data breach (often higher cap or uncapped)
   - IP infringement (often uncapped)
   - Gross negligence / willful misconduct (usually uncapped)

**Assessment Guidance:**

| Service Criticality | Minimum Acceptable Cap |
|---------------------|------------------------|
| Critical | Greater of: CHF 5M or 12 months fees |
| High | Greater of: CHF 2M or 12 months fees |
| Medium | Greater of CHF 500K or 6 months fees |
| Low | No minimum (standard terms acceptable) |

**Red Flags:**
- ❌ CHF 100 total liability cap (inadequate for any meaningful service)
- ❌ "To maximum extent permitted by law" (tries to minimize liability)
- ❌ Caps apply to ALL damages including data breaches (should be exception)

**Column U: Indemnification Clause**

**Options:**
- `Yes (Favorable)` - Vendor indemnifies for data breaches, IP infringement, regulatory fines
- `Yes (Limited)` - Vendor indemnifies only for IP infringement or narrow scenarios
- `No` - No indemnification clause

**What to Look For:**

**"Yes (Favorable)" Criteria:**
```
Vendor indemnifies Customer for:
  ✅ Third-party IP infringement claims (vendor's IP violates patents/copyrights)
  ✅ Data breaches caused by vendor's security failures
  ✅ Regulatory fines due to vendor's GDPR/data protection violations
  ✅ Subprocessor failures
  
Indemnification includes:
  ✅ Legal fees and costs
  ✅ Settlement amounts
  ✅ Judgments
  ✅ Regulatory penalties
```

**"Yes (Limited)" Example:**
```
Vendor indemnifies for:
  ✅ IP infringement only
  ❌ Data breaches excluded
  ❌ Regulatory fines excluded (customer bears risk)
```

**How to Complete:**
1. Locate "Indemnification" section
2. Read what triggers indemnification (IP, data breach, etc.)
3. Check if regulatory fines are covered
4. Assess if scope is adequate for service criticality

**Column V: Termination Notice Period**

**Options:**
- `≤30 days`
- `31-60 days`
- `61-90 days`
- `>90 days`

**How to Complete:**
1. Locate "Termination" or "Term and Termination" section
2. Find "Termination for Convenience" (customer's right to exit without cause)
3. Note notice period required
4. Enter appropriate option

**Assessment:**

| Service Criticality | Acceptable Notice Period |
|---------------------|--------------------------|
| Critical | ≤60 days (need exit flexibility) |
| High | ≤90 days |
| Medium | ≤90 days |
| Low | Any (not critical for operations) |

**Common Termination Scenarios:**
```
Scenario 1: Termination for Convenience
  Customer right: 60 days written notice
  Assessment: ✅ Acceptable

Scenario 2: Termination for Cause (Vendor Breach)
  Customer right: 30 days (after 15-day cure period)
  Assessment: ✅ Acceptable

Scenario 3: Termination Only at Renewal
  Customer right: 90 days notice before renewal date
  Initial term: 3 years
  Assessment: ⚠️ Problematic (locked in for 3 years)
```

**Red Flags:**
- ❌ No termination for convenience (locked in for full term)
- ❌ 180+ day notice period (excessive lock-in)
- ❌ Financial penalty for early termination (beyond wind-down costs)

**Column W: Data Return on Termination**

**Options:**
- `Yes (30 days)` - Vendor commits to return data within 30 days
- `Yes (60 days)` - Vendor commits within 60 days
- `Yes (90 days)` - Vendor commits within 90 days
- `No` - No data return commitment or timeline

**How to Complete:**
1. Locate "Data Return" or "Post-Termination" section in DPA or MSA
2. Find timeline for data return
3. Note format commitments (CSV, JSON, proprietary, API export)
4. Check deletion certification requirement

**Adequate Data Return Clause Example:**
```
Upon termination:
  ✅ Vendor will provide Customer data in standard format (CSV, JSON)
  ✅ Within 30 days of termination effective date
  ✅ At no additional cost to Customer
  ✅ Including all metadata, configurations, and attachments
  
After data return:
  ✅ Vendor will securely delete all Customer data within 60 days
  ✅ Vendor will provide deletion certification upon request
```

**Red Flags:**
- ❌ "Data available for 30 days via API" (no export assistance)
- ❌ "Export fees apply" (charging for your own data)
- ❌ No deletion commitment after return
- ❌ No format specification (may be unusable proprietary format)

**Column X: Auto-Renewal Clause**

**Options:**
- `Yes (Opt-Out)` - Contract auto-renews unless customer opts out (COMMON, requires tracking)
- `Yes (Opt-In)` - Contract requires mutual agreement to renew (RARE, customer-favorable)
- `No` - Contract expires without renewal action

**How to Complete:**
1. Locate "Renewal" or "Term" section
2. Determine renewal mechanism
3. Note renewal deadline (e.g., "notify 90 days before expiration")

**Auto-Renewal Risk Management:**
```
Contract: 3-year term, auto-renews for successive 1-year terms
Opt-out deadline: 90 days before renewal date
Contract start: 01.01.2024
First renewal: 01.01.2027

Critical Dates:
  ⚠️ 01.10.2026 (90 days before): Latest date to notify non-renewal
  ✅ 01.07.2026 (6 months before): Start renewal evaluation
  ✅ 01.04.2026 (9 months before): Schedule renewal review meeting

If you miss 01.10.2026:
  ❌ Contract auto-renews for 1 year (locked in until 01.01.2028)
```

**Renewal Tracking:**
- Set calendar reminders at Renewal Date - 180 days, -120 days, -100 days
- Track in contract management system
- Include in quarterly vendor review meetings

**Columns Y-Z: DORA/NIS2 Regulatory Clauses**

**Column Y: DORA Art. 30 Contractual Clauses**

**Applicability:** ONLY if [Organization] is an EU financial entity under DORA scope

**Options:**
- `Compliant` - All required DORA clauses present
- `Partial` - Some DORA clauses present, gaps exist
- `Not Present` - No DORA-specific clauses
- `Not Applicable` - [Organization] not subject to DORA

**Required DORA Contractual Elements (Article 30):**

| DORA Requirement | Contract Must Include |
|------------------|----------------------|
| Exit plan | Documented exit strategy, data portability commitments |
| Subcontracting | Written notice before subcontracting critical functions |
| Access rights | Right for [Organization], auditors, and competent authorities to access |
| Data security | Adequate data protection and security measures |
| Incident notification | Immediate notification of security incidents |
| Testing participation | Allow participation in threat-led penetration testing |
| Termination rights | Right to terminate if vendor fails regulatory requirements |

**How to Complete (If DORA Applicable):**
1. Review contract for DORA-specific language
2. Check if vendor acknowledges DORA applicability
3. Verify all 7 required elements present
4. Count gaps:
   - 7/7 present: `Compliant`
   - 4-6/7 present: `Partial` → requires amendment
   - 0-3/7 present: `Not Present` → urgent amendment needed

**If [Organization] is NOT subject to DORA:**
- Mark as `Not Applicable` for all vendors
- No further assessment needed

**Column Z: NIS2 Supply Chain Security**

**Applicability:** ONLY if [Organization] is an EU essential or important entity under NIS2

**Options:**
- `Compliant` - NIS2 supply chain security measures addressed
- `Partial` - Some measures present, gaps exist
- `Not Present` - No NIS2-specific clauses
- `Not Applicable` - [Organization] not subject to NIS2

**Required NIS2 Supply Chain Elements:**

| NIS2 Requirement | Contract Must Include |
|------------------|----------------------|
| Security measures | Adequate cybersecurity measures by supplier |
| Incident notification | Immediate notification of cybersecurity incidents |
| Vulnerability disclosure | Supplier's vulnerability management process |
| Security assessments | Regular security assessments and testing |
| Supply chain mapping | Transparency on supplier's own supply chain |

**How to Complete (If NIS2 Applicable):**
1. Assess if vendor is in your ICT supply chain (provides network/information systems)
2. Review contract for cybersecurity requirements
3. Verify incident notification clauses
4. Check vulnerability management commitments
5. Assess:
   - 5/5 present: `Compliant`
   - 3-4/5 present: `Partial`
   - 0-2/5 present: `Not Present`

**If [Organization] is NOT subject to NIS2:**
- Mark as `Not Applicable` for all vendors

#### Evidence Requirements

**For Each Vendor:**

**MUST HAVE:**
- ✅ Master Service Agreement (MSA) - complete executed copy
- ✅ Data Processing Agreement (DPA) - if processing personal data
- ✅ All amendments and addendums
- ✅ Contract signature page (proves execution)

**SHOULD HAVE:**
- ✅ Service Level Agreement (SLA) - if separate from MSA
- ✅ Order forms / Statements of Work
- ✅ Subprocessor list (if DPA requires)

**NICE TO HAVE:**
- ✅ Negotiation history (shows how current terms were reached)
- ✅ Legal review memo (internal Legal assessment of adequacy)

**Evidence Storage:**
```
/Evidence/Contracts/
├── MSA-Vendor-A-2024-Executed.pdf
├── DPA-Vendor-A-2024-Executed.pdf
├── SLA-Vendor-A-2024.pdf
├── Amendment-1-Vendor-A-2025.pdf
└── Subprocessor-List-Vendor-A-2025.pdf
```

#### Verification Steps

**Step 1: Contract Collection (Week 1)**
```
For each vendor:
  [ ] Query contract management system for executed contracts
  [ ] Request from Legal if not in system
  [ ] Obtain from Procurement if recently signed
  [ ] Verify execution (all parties signed)
  [ ] Save to evidence repository
```

**Step 2: Legal Review (Week 1-2)**
```
For each contract:
  [ ] Schedule Legal review session (4-8 hours)
  [ ] Review DPA against GDPR/FADP requirements
  [ ] Assess liability caps for adequacy
  [ ] Review indemnification scope
  [ ] Check termination and data return clauses
  [ ] Evaluate DORA/NIS2 compliance (if applicable)
  [ ] Document gaps and required amendments
```

**Step 3: Gap Remediation (Week 2-3)**
```
For contracts with gaps:
  [ ] Prioritize by vendor criticality (Critical/High first)
  [ ] Draft amendment language (Legal)
  [ ] Engage vendor account manager (Procurement)
  [ ] Negotiate amendments
  [ ] Track amendment status
  [ ] Obtain CISO approval for risk acceptance if vendor refuses
```

#### Common Mistakes

**Mistake 1: Accepting Generic "Reasonable Care" DPAs**

❌ **Wrong:**
```
DPA states: "Vendor will use reasonable care to protect data"
Assessor: Marks "Yes (Adequate)" (language sounds OK)
Reality: "Reasonable care" is too vague, no specific commitments
```

✅ **Right:**
```
DPA requirements: Must reference ISO 27001 or specific controls
Current DPA: Only says "reasonable care"
Assessment: Yes (Weak) → requires amendment to specify controls
Action: Request amendment referencing ISO 27001 or Annex listing controls
```

**Mistake 2: Ignoring Subprocessor Risks**

❌ **Wrong:**
```
Contract: "Vendor may use subprocessors at its discretion"
Assessor: Marks as acceptable (vendor has flexibility)
Reality: Vendor could subcontract to unapproved/risky parties
```

✅ **Right:**
```
GDPR requires: Subprocessor list + notification + objection right
Current contract: No list, no notification, no objection
Assessment: Non-compliant with GDPR Art. 28
Action: Urgent amendment required to add subprocessor controls
```

**Mistake 3: Accepting Inadequate Liability Caps**

❌ **Wrong:**
```
Service: Critical CRM (Confidential customer data)
Liability cap: CHF 100 total
Assessor: Marks as acceptable (contract exists)
Reality: CHF 100 is meaningless for data breach impact
```

✅ **Right:**
```
Service criticality: Critical
Data classification: Confidential
Current cap: CHF 100
Adequate cap: Minimum CHF 5M or 12 months fees
Assessment: Gap - liability cap inadequate for criticality
Action: Negotiate higher cap or escalate to CISO for risk acceptance
```

#### Quality Checks

**Before Marking Sheet 3 Complete:**

- [ ] All vendors have contract type identified
- [ ] All DPAs reviewed by Legal for adequacy
- [ ] All liability caps assessed against service criticality
- [ ] All termination periods documented
- [ ] All auto-renewal dates tracked in calendar
- [ ] DORA/NIS2 columns completed (or marked N/A if not applicable)
- [ ] All gaps have remediation plans or risk acceptance
- [ ] All contract PDFs saved to Evidence Register

---

### Sheet 4: SLA Requirements & Performance

#### Purpose Recap

**Goal:** Document vendor SLA commitments and track actual performance against contractual obligations.

**Why This Matters:**
- SLAs define vendor accountability (uptime, support, response times)
- Performance tracking reveals vendor reliability vs. promises
- SLA penalties provide financial leverage for underperformance
- Historical performance informs renewal decisions

**Success Criterion:**
> All Critical and High services have documented SLAs with uptime commitments ≥99.9%, and actual performance is tracked and meets or exceeds SLA commitments over the last 12 months.

#### Column-by-Column Guidance

**Columns R-AA: SLA Commitments and Performance**

**Column R: SLA Uptime Commitment**

**Format:** Percentage (e.g., "99.9%", "99.95%", "99.99%")

**How to Complete:**
1. Locate SLA document or uptime guarantee in contract
2. Find monthly or annual uptime commitment
3. Note if commitment is monthly (preferred) or annual only
4. Enter exact percentage

**Understanding Uptime SLAs:**

| SLA % | Allowed Downtime/Month | Allowed Downtime/Year | Typical Use |
|-------|------------------------|----------------------|-------------|
| 99.0% | 7.2 hours | 3.65 days | Low criticality |
| 99.5% | 3.6 hours | 1.83 days | Medium criticality |
| 99.9% | 43 minutes | 8.76 hours | High criticality (COMMON) |
| 99.95% | 22 minutes | 4.38 hours | Critical services |
| 99.99% | 4 minutes | 52 minutes | Mission-critical (expensive) |
| 99.999% | 26 seconds | 5.26 minutes | Ultra-critical (rare, very expensive) |

**How to Extract from Contract:**

**Example 1: Clear SLA**
```
Contract states:
  "Service Availability: 99.9% measured monthly"
  
Entry: 99.9%
```

**Example 2: Tiered SLA**
```
Contract states:
  - Standard tier: 99.0%
  - Professional tier: 99.5%
  - Enterprise tier: 99.9%
  
Your subscription: Enterprise
Entry: 99.9%
```

**Example 3: Component-Based SLA**
```
Contract states:
  - Compute: 99.95%
  - Storage: 99.99%
  - Network: 99.9%
  
Entry: List all (e.g., "Compute 99.95%, Storage 99.99%, Network 99.9%")
```

**Red Flags:**
- ❌ No specific percentage (e.g., "commercially reasonable efforts")
- ❌ Annual-only SLA (allows 8.76 hours downtime in one month if 99.9% annual)
- ❌ SLA excludes "scheduled maintenance" without defined windows
- ❌ SLA calculated by vendor without independent verification

**Column S: Support Response Time (Critical)**

**Format:** Time (e.g., "15 minutes", "1 hour", "4 hours")

**How to Complete:**
1. Locate support SLA in contract or support agreement
2. Find response time for "Critical" or "Severity 1" incidents
3. Note if commitment is response time or resolution time (response preferred)
4. Enter time commitment

**Severity Level Definitions (Typical):**

| Severity | Definition | Typical Response Time | Typical Resolution Time |
|----------|------------|----------------------|------------------------|
| Critical (P1/Sev1) | Complete outage, business impact | 15 min - 1 hour | 4-24 hours |
| High (P2/Sev2) | Major functionality broken | 1-4 hours | 1-3 days |
| Medium (P3/Sev3) | Minor functionality issue | 4-24 hours | 3-7 days |
| Low (P4/Sev4) | Question, enhancement request | 1-3 business days | No commitment |

**How to Extract:**

**Example 1: Clear Support SLA**
```
Contract states:
  Severity 1 (Critical): Initial response within 1 hour, 24/7
  
Entry: 1 hour
```

**Example 2: Business Hours Only**
```
Contract states:
  Critical issues: Response within 4 hours (business hours only)
  Business hours: 9AM-5PM EST, Monday-Friday
  
Entry: 4 hours (business hours)
Assessment: ⚠️ Gap if service is 24/7 (no after-hours support)
```

**Red Flags:**
- ❌ "Best efforts" with no time commitment
- ❌ Business hours only for 24/7 service
- ❌ No definition of "response" (acknowledgment vs. engineer assigned)
- ❌ Resolution time SLA only (vendor can "respond" quickly but not resolve)

**Column T: Incident Notification Timeframe**

**Format:** Time (e.g., "24 hours", "48 hours", "Immediate")

**How to Complete:**
1. Locate incident notification clause (usually in DPA or security addendum)
2. Find timeframe for notifying Customer of security incidents
3. Note if different timeframes for different incident types
4. Enter commitment

**Regulatory Requirements for Comparison:**

| Regulation | Notification Deadline | Applies To |
|------------|----------------------|-----------|
| GDPR Art. 33 | 72 hours | Data breaches (controller to DPA) |
| GDPR Art. 28 | "Without undue delay" | Vendor to customer (processor to controller) |
| FADP (Swiss) | "As soon as possible" | High risk data breaches |
| DORA Art. 19 | "Without undue delay" (typically interpreted as 24-48h) | Financial entities |

**How to Extract:**

**Example 1: Specific Timeframe**
```
DPA states:
  "Vendor shall notify Customer within 24 hours of becoming aware 
   of any Security Incident affecting Customer Data"
  
Entry: 24 hours
Assessment: ✅ Adequate (meets GDPR/DORA expectations)
```

**Example 2: Vague Language**
```
Contract states:
  "Vendor will notify Customer of security incidents without undue delay"
  
Entry: Without undue delay (vague)
Assessment: ⚠️ Weak (no specific timeframe, open to interpretation)
Action: Request amendment to specify 24-48 hours
```

**Red Flags:**
- ❌ "Upon request" (reactive, not proactive notification)
- ❌ "As soon as reasonably practicable" (too vague)
- ❌ No notification commitment at all
- ❌ Notification only if "material" (vendor decides materiality)

**Column U: SLA Penalty Mechanism**

**Format:** Description of penalties (e.g., "Service credits", "Refund", "None")

**Options:**
- `Service Credits` - Most common (credit toward future bills)
- `Refund` - Cash refund (rare, customer-favorable)
- `None` - No penalty (vendor not accountable)
- `Tiered Credits` - Escalating credits based on breach severity

**How to Complete:**
1. Locate "Service Credits" or "Remedies" section in SLA
2. Determine penalty type and calculation
3. Note maximum penalty cap (often 10-30% of monthly fees)
4. Document claim process (automatic vs. customer must claim)

**SLA Penalty Examples:**

**Example 1: Tiered Service Credits (COMMON)**
```
Monthly Uptime SLA: 99.9%

Actual Uptime | Service Credit
99.9% - 99.0% | 10% of monthly fees
98.9% - 95.0% | 25% of monthly fees
< 95.0%       | 50% of monthly fees (cap)

Claim Process: Customer must submit claim within 30 days
Entry: Tiered service credits (10-50% of monthly fees, capped)
```

**Example 2: No Penalties (PROBLEMATIC)**
```
SLA states:
  "Service Availability: 99.9% (target)"
  "Vendor will use best efforts to meet availability targets"
  No penalties or remedies section
  
Entry: None
Assessment: ❌ Gap - SLA has no enforcement mechanism
Action: Negotiate service credit mechanism or note as risk
```

**Example 3: Automatic Credits (RARE, CUSTOMER-FAVORABLE)**
```
SLA states:
  "Service credits automatically applied to next invoice if SLA missed"
  No claim required by Customer
  
Entry: Automatic service credits (10-25% of monthly fees)
Assessment: ✅ Preferred (vendor accountability, no claim burden)
```

**Assessment of Penalty Adequacy:**

| Penalty Level | Vendor Accountability | Acceptability |
|---------------|----------------------|---------------|
| 50%+ of monthly fees | High | ✅ Adequate |
| 25-49% of monthly fees | Medium | ⚠️ Acceptable for Medium/Low criticality |
| 10-24% of monthly fees | Low | ⚠️ Weak (vendor bears little cost) |
| <10% or None | None | ❌ Inadequate (no vendor accountability) |

**Red Flags:**
- ❌ "Sole and exclusive remedy" clause (limits Customer to service credits only, no other recourse)
- ❌ Credits capped at very low percentage (e.g., 5% monthly fees)
- ❌ Claim process onerous (30-page form, 15-day deadline)
- ❌ Credits expire if not used (e.g., 90-day expiration)

**Column V: Actual Uptime (Last 12 Months)**

**Format:** Percentage (e.g., "99.92%")

**How to Complete:**
1. Collect uptime data from monitoring systems (last 12 months)
2. Calculate average monthly uptime or use vendor SLA reports
3. Cross-reference vendor reports with independent monitoring (if available)
4. Enter actual performance percentage

**Data Sources:**

**Primary (Independent Monitoring):**
- Organization's APM tools (Datadog, New Relic, Dynatrace)
- Uptime monitoring (Pingdom, UptimeRobot, StatusCake)
- SIEM event logs (service availability events)

**Secondary (Vendor-Provided):**
- Vendor SLA dashboard (AWS Service Health, Azure Status)
- Monthly SLA reports (if vendor provides)
- Vendor status page historical data

**Calculation Method:**
```
Option 1: Average Monthly Uptime
  Jan: 99.95%
  Feb: 99.88%
  Mar: 99.92%
  ... (12 months)
  Dec: 99.91%
  
  Average: (Sum of 12 months) / 12 = 99.91%

Option 2: Total Uptime for Year
  Total minutes in year: 525,600
  Total downtime minutes: 473
  Uptime: (525,600 - 473) / 525,600 = 99.91%
```

**If No Monitoring Data Exists:**
- Mark as "Not Tracked"
- Note in Gap column: "No performance monitoring in place"
- Action: Implement monitoring for Critical/High services

**Column W: SLA Breaches (Count)**

**Format:** Number (e.g., "0", "2", "5")

**How to Complete:**
1. Compare actual uptime (Column V) to SLA commitment (Column R) for each month
2. Count months where actual < commitment
3. Enter total breach count for 12-month period

**Example:**
```
SLA Commitment: 99.9% monthly

Month-by-Month:
  Jan: 99.95% ✅ (exceeds SLA)
  Feb: 99.85% ❌ (breach: below 99.9%)
  Mar: 99.92% ✅
  Apr: 99.78% ❌ (breach)
  May-Dec: All ✅ (exceed SLA)

Breach Count: 2
Entry: 2
```

**Breach Threshold Assessment:**

| Breaches/Year | Vendor Performance | Action Required |
|---------------|-------------------|-----------------|
| 0 | Excellent | ✅ Continue monitoring |
| 1-2 | Good | ⚠️ Monitor trend, minor escalation |
| 3-4 | Concerning | ⚠️ Escalate to vendor, request improvement plan |
| 5+ | Poor | ❌ Escalate to CISO, consider vendor replacement |

**Column X: Credits Claimed (CHF)**

**Format:** Amount in CHF (e.g., "CHF 5,000", "CHF 0")

**How to Complete:**
1. For each SLA breach (Column W), calculate service credit owed
2. Track if credit was claimed from vendor
3. Sum total credits received for 12-month period
4. Enter total

**Calculation Example:**
```
Service: AWS EC2
Monthly fees: CHF 10,000
SLA: 99.95%

February Performance: 99.85% (breach)
SLA penalty tier: 99.0-99.94% = 10% credit
Credit owed: CHF 10,000 × 10% = CHF 1,000

April Performance: 99.70% (breach)
SLA penalty tier: 99.0-99.94% = 10% credit
Credit owed: CHF 10,000 × 10% = CHF 1,000

Total Credits Claimed: CHF 2,000
Entry: CHF 2,000
```

**If Credits NOT Claimed:**
```
Credits Owed: CHF 2,000
Credits Claimed: CHF 0

Gap: SLA breaches occurred but credits not claimed
Action: 
  1. Document unclaimed credits (Column J)
  2. Submit retroactive claim if within claim deadline
  3. Set up automated claim process for future
```

**Column Y: Breach Remediation Status**

**Format:** Dropdown: `Resolved`, `In Progress`, `Vendor Action Required`, `Not Addressed`

**How to Complete:**
1. For vendors with SLA breaches (Column W > 0):
   - Review if vendor provided root cause analysis
   - Check if vendor implemented corrective actions
   - Verify if breaches have stopped (recent months)
2. Select status based on vendor response

**Status Definitions:**

| Status | Meaning | When to Use |
|--------|---------|-------------|
| `Resolved` | Vendor identified root cause, implemented fix, no recent breaches | Breaches in months 1-6, none in months 7-12 |
| `In Progress` | Vendor acknowledged, working on fix | Vendor has improvement plan, monitoring progress |
| `Vendor Action Required` | Vendor has not adequately addressed breaches | Breaches continue, no satisfactory response |
| `Not Addressed` | Customer has not escalated to vendor | Breaches occurred but no formal escalation yet |

**Example:**
```
Breaches: 4 (Jan, Feb, Mar, Apr)
Vendor Response:
  - May: Root cause identified (database capacity issue)
  - June: Implemented auto-scaling
  - July-Dec: No breaches
  
Status: Resolved
```

**Column Z: Performance Trend**

**Format:** Dropdown: `Improving`, `Stable`, `Declining`, `Insufficient Data`

**How to Complete:**
1. Compare recent 6 months vs. previous 6 months
2. Assess if uptime is improving, stable, or declining
3. Select trend

**Trend Calculation:**
```
Months 1-6 Average: 99.85%
Months 7-12 Average: 99.93%

Change: +0.08% (improvement)
Trend: Improving

---

Months 1-6 Average: 99.92%
Months 7-12 Average: 99.91%

Change: -0.01% (minimal change)
Trend: Stable

---

Months 1-6 Average: 99.95%
Months 7-12 Average: 99.82%

Change: -0.13% (degradation)
Trend: Declining ⚠️ (requires investigation)
```

**Column AA: Next Review Date**

**Format:** DD.MM.YYYY

**How to Complete:**
1. Set based on service criticality:
   - Critical: Monthly review
   - High: Quarterly review
   - Medium: Semi-annual review
   - Low: Annual review
2. Enter next scheduled review date

**Example:**
```
Today: 20.01.2026
Service Criticality: Critical
Review Frequency: Monthly

Next Review Date: 20.02.2026
```

#### Evidence Requirements

**For Each Vendor:**

- ✅ SLA document or SLA section in contract
- ✅ Vendor SLA performance reports (last 12 months) - monthly preferred
- ✅ Independent monitoring data (if available)
- ✅ Service credit claim confirmations (if credits claimed)
- ✅ Vendor breach notifications (emails, incident reports)

#### Quality Checks

- [ ] All Critical/High services have SLA commitments documented
- [ ] Actual performance data populated (or marked "Not Tracked" with remediation plan)
- [ ] SLA breaches calculated correctly (actual vs. commitment)
- [ ] Service credits claimed where owed (or gap documented)
- [ ] Performance trends assessed
- [ ] Review dates scheduled based on criticality

---

**END OF SECTION 4 PART 1: COMPLETING SHEETS 2-4**

## Section 4: Completing Each Sheet - Detailed Guidance (Part 2)

### Sheet 5: Data Sovereignty & Jurisdiction

#### Purpose Recap

**Goal:** Document where vendor data is stored and processed, and ensure compliance with data residency requirements and cross-border transfer regulations.

**Why This Matters:**
- GDPR/FADP require knowing where personal data is processed
- Cross-border data transfers require legal mechanisms (SCCs, adequacy decisions)
- Data residency commitments may be contractual or regulatory requirements
- Encryption key custody determines who can access data (CLOUD Act risk)

**Success Criterion:**
> All Critical and High services have documented data storage/processing locations, appropriate cross-border transfer mechanisms in place, and data residency compliance verified.

#### Column-by-Column Guidance

**Columns R-Y: Data Sovereignty Details**

**Column R: Data Storage Location**

**Format:** Geographic regions (e.g., "EU (Frankfurt, Amsterdam)", "Switzerland (Zurich)")

**How to Complete:**
1. Review contract for data residency commitments
2. Check vendor technical documentation
3. Verify in vendor portal/console (if accessible)
4. Note primary and backup/DR locations if different

**Specificity Levels:**

| Specificity | Example | Adequacy |
|-------------|---------|----------|
| Country + City | "Switzerland (Zurich)" | ✅ Ideal |
| Country + Region | "Germany (EU-Central)" | ✅ Good |
| Multi-country region | "EU (multiple data centers)" | ⚠️ Acceptable if list provided |
| Continent only | "Europe" | ⚠️ Vague (includes non-EU countries) |
| Global/Unspecified | "Worldwide" or "Not specified" | ❌ Inadequate |

**How to Extract:**

**Example 1: Specific Commitment**
```
Contract states:
  "Customer Data stored exclusively in EU data centers (Frankfurt, Amsterdam)"
  
Entry: EU (Frankfurt, Amsterdam)
```

**Example 2: Customer-Selectable Region**
```
Vendor portal shows:
  Selected region: eu-central-1 (Frankfurt)
  
Technical documentation:
  eu-central-1 = Frankfurt, Germany
  
Entry: Germany (Frankfurt)
```

**Example 3: Multi-Region with DR**
```
Primary: Switzerland (Zurich)
Disaster Recovery: Germany (Frankfurt)

Entry: Switzerland (Zurich) - Primary; Germany (Frankfurt) - DR
```

**Red Flags:**
- ❌ "Data may be stored in any of our global data centers" (no commitment)
- ❌ Vendor can change data location without notice
- ❌ Contract says EU but vendor portal shows US region selected
- ❌ No contractual data residency commitment (vendor discretion)

**Column S: Data Processing Location**

**Format:** Geographic regions (same format as Column R)

**How to Complete:**
1. Identify if processing location differs from storage
2. Common scenarios:
   - Storage in EU, but management plane in US
   - Storage in Switzerland, but backups processed in EU
   - Data stored locally but analytics/ML processing in US
3. Document all processing locations

**Storage vs. Processing:**
```
Scenario 1: Storage = Processing (SIMPLE)
  Storage: EU (Frankfurt)
  Processing: EU (Frankfurt)
  Entry: EU (Frankfurt)

Scenario 2: Split Architecture (COMPLEX)
  Storage: EU (Frankfurt)
  Control Plane: US (Virginia) - metadata, logs, mgmt
  Analytics: US (Oregon) - ML/AI processing
  
  Entry: EU (Frankfurt) - Data; US (Virginia, Oregon) - Control/Analytics
  Assessment: ⚠️ Requires review - US processing may trigger CLOUD Act

Scenario 3: Vendor Subprocessors
  Primary Storage: Switzerland (Zurich)
  Backup Processing: Vendor's EU subprocessor (Ireland)
  Support: Vendor's support team (India - access to logs)
  
  Entry: Switzerland (Zurich) - Primary; EU (Ireland) - Backup; India - Support Logs
  Assessment: ⚠️ Multiple jurisdictions, review transfer mechanisms
```

**Key Questions to Ask Vendor:**
1. Where is data at rest stored?
2. Where are backups stored and processed?
3. Where are support/operations teams located (can they access data)?
4. Where are logs/metadata processed?
5. If using AI/ML features, where is processing performed?

**Column T: Cross-Border Transfer Mechanism**

**Options:**
- `EU Adequacy Decision` - Transfer to country with EU adequacy ruling
- `Standard Contractual Clauses (SCCs)` - GDPR-approved contract clauses
- `Binding Corporate Rules (BCRs)` - Intra-company transfers
- `EU-Only (No Transfer)` - No data leaves EU
- `Swiss-Only (No Transfer)` - No data leaves Switzerland
- `None / Unknown` - No documented transfer mechanism

**How to Complete:**
1. Review DPA for cross-border transfer clauses
2. Identify if data leaves EU/Switzerland
3. Determine legal mechanism used (if applicable)
4. Verify mechanism is current (SCCs updated post-Schrems II)

**Transfer Mechanism Details:**

**EU Adequacy Decisions (As of 2026):**
- ✅ UK (post-Brexit adequacy)
- ✅ Switzerland
- ✅ Japan
- ✅ Canada (commercial organizations)
- ✅ Several others (check current EU list)

**When to Use Each:**

| Mechanism | Use Case | Requirements |
|-----------|----------|--------------|
| `EU Adequacy Decision` | Transfer to UK, Switzerland, Japan, etc. | Verify country has current adequacy decision |
| `SCCs` | Transfer to US, other non-adequate countries | DPA must include SCCs (post-Schrems II version), Transfer Impact Assessment (TIA) required |
| `BCRs` | Multinational company, intra-group transfers | Vendor must have approved BCRs |
| `EU-Only` | No transfer outside EU | Contractual commitment + technical verification |
| `None` | Transfer occurring without legal basis | ❌ GDPR violation - immediate remediation required |

**How to Verify SCCs:**
```
Step 1: Locate SCCs in DPA
  - Check DPA Annex/Exhibit for "Standard Contractual Clauses"
  - Verify date: Post-Schrems II SCCs (2021 or later)
  
Step 2: Verify SCC Type
  - Controller-to-Processor (Module 2) - MOST COMMON
  - Controller-to-Controller (Module 1)
  - Processor-to-Processor (Module 3)
  - Processor-to-Controller (Module 4)
  
Step 3: Check Transfer Impact Assessment (TIA)
  - Post-Schrems II, SCCs alone insufficient
  - Vendor should provide TIA or Customer must perform
  - TIA assesses local laws (e.g., CLOUD Act) conflicting with GDPR
  
Step 4: Verify Supplementary Measures
  - Encryption (at rest, in transit)
  - Customer-managed keys
  - Data minimization
  - Access controls limiting non-EU access
```

**Example Entries:**
```
Example 1: EU Adequacy
  Storage: UK (London)
  Mechanism: EU Adequacy Decision
  Notes: UK has adequacy ruling, no additional mechanism needed

Example 2: SCCs with US Vendor
  Storage: EU (Frankfurt)
  Processing: US (control plane)
  Mechanism: Standard Contractual Clauses (SCCs)
  Notes: DPA includes post-Schrems II SCCs, TIA required

Example 3: No Transfer
  Storage: Switzerland (Zurich)
  Processing: Switzerland (Zurich)
  Mechanism: Swiss-Only (No Transfer)
  Notes: Contractual commitment to Swiss data residency
```

**Red Flags:**
- ❌ Transfer to US with no SCCs (GDPR violation)
- ❌ SCCs from pre-2021 (old SCCs invalidated by Schrems II)
- ❌ SCCs without Transfer Impact Assessment post-Schrems II
- ❌ "Vendor complies with Privacy Shield" (Privacy Shield invalidated 2020)

**Column U: Data Residency Guarantee**

**Options:**
- `Yes (Contractual)` - Contract guarantees data stays in specified location
- `Yes (Technical)` - Technical controls prevent data from leaving region
- `Yes (Both)` - Both contractual and technical guarantees
- `No Guarantee` - Vendor discretion on data location
- `Customer-Managed` - Customer controls data location via configuration

**How to Complete:**
1. Check if contract includes data residency clause
2. Verify if technical controls enforce residency (region lock)
3. Assess strength of guarantee

**Guarantee Strength Assessment:**

| Type | Strength | Example | Risk |
|------|----------|---------|------|
| `Yes (Both)` | Highest | Contract + region lock | Low - vendor cannot move data without breach |
| `Yes (Contractual)` | Medium-High | Contract clause only | Low-Medium - requires vendor compliance |
| `Yes (Technical)` | Medium | Region lock, no contract | Medium - vendor could change policy |
| `Customer-Managed` | High | Customer selects region | Low - Customer controls |
| `No Guarantee` | Lowest | Vendor discretion | High - data location can change anytime |

**Contractual Guarantee Example:**
```
Contract clause:
  "Vendor shall store and process Customer Data exclusively within the 
   European Union. Vendor shall not transfer Customer Data outside the EU 
   without prior written consent from Customer."
   
Entry: Yes (Contractual)
```

**Technical Guarantee Example:**
```
Vendor documentation:
  "EU Data Boundary: All customer data for EU customers is stored and 
   processed exclusively in EU data centers. Technical controls prevent 
   data from being accessed or transferred outside the EU."
   
Entry: Yes (Technical)
Verification: Confirmed in vendor portal - EU Data Boundary enabled
```

**No Guarantee Example:**
```
Contract states:
  "Vendor may store and process data in any of its global data centers"
  
Entry: No Guarantee
Assessment: ❌ Gap - no data residency protection
Action: Negotiate data residency clause or select different vendor
```

**Column V: Encryption Key Custody**

**Options:**
- `Customer-Managed Keys (CMK)` - Customer controls encryption keys
- `Provider-Managed (Default)` - Vendor controls keys
- `Shared Management` - Hybrid model (rare)
- `Unknown` - Key custody not documented

**How to Complete:**
1. Review vendor encryption documentation
2. Determine who controls encryption keys
3. Verify CMK implementation if claimed

**Key Custody Models:**

| Model | Who Controls Keys | Vendor Can Access Data? | CLOUD Act Protection |
|-------|-------------------|-------------------------|---------------------|
| `Customer-Managed Keys` | Customer | No (without Customer providing keys) | ✅ High (vendor cannot decrypt) |
| `Provider-Managed` | Vendor | Yes | ❌ None (vendor has keys, can be compelled) |
| `Shared Management` | Both | Depends on implementation | ⚠️ Partial (depends on design) |

**Customer-Managed Key (CMK) Implementations:**

**AWS:**
- Service: AWS KMS with Customer-Managed Keys
- Customer imports key or AWS generates with customer ownership
- Customer can revoke keys (data becomes inaccessible to AWS)

**Azure:**
- Service: Azure Key Vault with Customer-Managed Keys
- Customer controls key lifecycle
- "Bring Your Own Key (BYOK)" option

**Google Cloud:**
- Service: Cloud KMS with Customer-Managed Encryption Keys (CMEK)
- Customer controls key access and rotation

**How to Verify CMK:**
```
Step 1: Check vendor documentation
  - Does vendor offer CMK/BYOK?
  - What services support CMK?
  
Step 2: Verify configuration (if accessible)
  - Log into vendor portal
  - Navigate to encryption settings
  - Confirm CMK is enabled (not default vendor-managed)
  
Step 3: Test key revocation
  - Temporarily revoke keys
  - Verify vendor cannot access data (service fails)
  - Restore keys
  
Step 4: Document key custody
  - Entry: Customer-Managed Keys (CMK)
  - Evidence: Configuration screenshots, CMK policy
```

**Red Flags:**
- ❌ Vendor claims CMK but customer hasn't configured it (using default keys)
- ❌ CMK only for data at rest, not for backups (backups use vendor keys)
- ❌ Vendor has "emergency access" to customer-managed keys (defeats purpose)
- ❌ Key escrow to vendor (vendor retains copy of keys)

**Column W: Regulatory Compliance**

**Format:** Comma-separated list (e.g., "GDPR, FADP", "GDPR, HIPAA, FADP")

**How to Complete:**
1. Identify applicable regulations based on:
   - Data types processed (personal data → GDPR/FADP)
   - Industry (financial → DORA, healthcare → HIPAA)
   - Organization location (EU → GDPR, Switzerland → FADP)
2. Verify vendor compliance with each regulation
3. List all applicable regulations

**Common Regulations:**

| Regulation | Applicability | Vendor Compliance Evidence |
|------------|---------------|---------------------------|
| **GDPR** | EU personal data processing | DPA, SCCs, certifications |
| **FADP** | Swiss personal data processing | DPA, data residency commitment |
| **HIPAA** | US healthcare data | Business Associate Agreement (BAA) |
| **PCI-DSS** | Payment card data | PCI certification, AOC |
| **DORA** | EU financial entity ICT services | DORA-compliant contracts (Sheet 3) |
| **NIS2** | EU essential/important entity supply chain | NIS2 cybersecurity clauses |

**How to Verify:**

**GDPR Compliance:**
```
Required Evidence:
  ✅ DPA compliant with GDPR Art. 28
  ✅ SCCs if data leaves EU (or adequacy decision)
  ✅ Subprocessor list
  ✅ Data breach notification commitment (≤24-48 hours)
  ✅ Support for data subject rights (access, deletion, portability)

Entry: GDPR
```

**FADP Compliance:**
```
Required Evidence:
  ✅ DPA compliant with Swiss FADP
  ✅ Data storage in Switzerland or adequate country
  ✅ Cross-border transfer mechanisms if leaving Switzerland
  ✅ Data breach notification

Entry: FADP
```

**Multiple Regulations:**
```
Service processes:
  - EU customer personal data → GDPR applies
  - Swiss employee data → FADP applies
  - Payment data → PCI-DSS applies

Entry: GDPR, FADP, PCI-DSS
Evidence: DPA (GDPR/FADP), PCI AOC (payment processing)
```

**Column X: DPA Reviewed by DPO**

**Options:**
- `Yes (Approved)` - DPO reviewed and approved DPA
- `Yes (Approved with Conditions)` - DPO approved with compensating controls
- `No (Pending Review)` - DPA exists but not yet reviewed
- `No (Rejected)` - DPO rejected DPA as inadequate
- `N/A (No Personal Data)` - Service doesn't process personal data

**How to Complete:**
1. Submit DPA to Data Protection Officer for review
2. DPO assesses GDPR/FADP compliance
3. Document DPO decision
4. If conditions, document compensating controls

**DPO Review Checklist (from DPO perspective):**
```
DPA Review - [Vendor Name]

☐ Controller/Processor roles clearly defined
☐ Processing purposes limited to service delivery
☐ Data categories and data subjects specified
☐ Processing locations documented
☐ Cross-border transfer mechanism adequate (SCCs, adequacy, etc.)
☐ Subprocessor list provided and approved
☐ Security measures adequate (ISO 27001 or specific controls)
☐ Data subject rights support (access, deletion, portability)
☐ Breach notification ≤24-48 hours
☐ Audit rights included
☐ Data return/deletion upon termination (≤60 days)

DPO Decision:
  ☐ Approved
  ☐ Approved with Conditions: [specify]
  ☐ Rejected - requires renegotiation

DPO Signature: _______________ Date: _______________
```

**Example Entries:**
```
Example 1: Approved
  DPO reviewed: 15.01.2026
  DPO decision: Approved
  Entry: Yes (Approved)

Example 2: Approved with Conditions
  DPO reviewed: 10.01.2026
  DPO decision: Approved with condition - CMK must be enabled
  Action: Enable CMK by 28.02.2026
  Entry: Yes (Approved with Conditions)
  Compensating Control (Column N): "CMK enabled 20.01.2026"

Example 3: Rejected
  DPO reviewed: 05.01.2026
  DPO decision: Rejected - no SCCs for US data transfer
  Entry: No (Rejected)
  Action: Negotiate DPA amendment to add SCCs
```

**Column Y: Data Sovereignty Risk Rating**

**Options:**
- `Low` - Data stays in approved jurisdiction, adequate protections
- `Medium` - Minor gaps or acceptable transfer mechanisms
- `High` - Significant jurisdictional risks, compensating controls needed
- `Critical` - Non-compliant, immediate action required

**How to Complete:**
1. Assess data location against requirements
2. Evaluate cross-border transfer mechanisms
3. Consider encryption key custody
4. Rate overall risk

**Risk Rating Matrix:**

| Scenario | Rating | Example |
|----------|--------|---------|
| EU data in EU, CMK, no transfer | `Low` | Ideal configuration |
| EU data in EU, vendor keys, no transfer | `Low` | Standard configuration |
| EU data in EU, US vendor, CMK + SCCs | `Medium` | CLOUD Act mitigated by CMK |
| EU data in US, SCCs, vendor keys | `High` | CLOUD Act exposure |
| EU data in US, no SCCs | `Critical` | GDPR violation |
| Confidential data, no residency guarantee | `High` | Vendor can move data anytime |

**Rating Guidance:**

**Low Risk:**
- Data stored in required jurisdiction (EU for GDPR, CH for FADP)
- Contractual and/or technical data residency guarantees
- Customer-managed keys (if US vendor)
- Appropriate transfer mechanisms if any cross-border transfer

**Medium Risk:**
- Data in approved location but vendor keys
- SCCs in place for transfers but no CMK
- Data residency guarantee but not enforced technically

**High Risk:**
- US vendor with EU data and vendor-managed keys (CLOUD Act risk)
- Cross-border transfers without adequate mechanisms
- No data residency guarantee for sensitive data

**Critical Risk:**
- GDPR violations (transfers without SCCs/adequacy)
- Confidential/Restricted data in unapproved jurisdiction
- No encryption or weak encryption
- Vendor refuses to provide data location information

#### Evidence Requirements

**For Each Vendor:**

**MUST HAVE:**
- ✅ Data residency documentation (contract clause, technical doc)
- ✅ DPA with cross-border transfer mechanisms (if applicable)
- ✅ Vendor data center location list
- ✅ DPO approval memo (if processing personal data)

**SHOULD HAVE:**
- ✅ Vendor portal screenshots (region selection, data location)
- ✅ Encryption documentation (CMK configuration if applicable)
- ✅ Transfer Impact Assessment (if using SCCs to US)
- ✅ Subprocessor list with locations

**NICE TO HAVE:**
- ✅ Vendor data residency white paper
- ✅ Third-party data flow audit
- ✅ Independent verification of data location (e.g., network monitoring)

#### Verification Steps

**Step 1: Data Location Verification**
```
For each vendor:
  [ ] Request data center location documentation
  [ ] Check vendor trust center / compliance page
  [ ] Log into vendor portal (if accessible)
  [ ] Verify region selection matches contract
  [ ] Document primary and DR/backup locations
```

**Step 2: DPA Review (with Legal/DPO)**
```
For vendors processing personal data:
  [ ] Submit DPA to DPO for GDPR/FADP review
  [ ] Verify cross-border transfer mechanisms
  [ ] Check SCC version (post-Schrems II required)
  [ ] Assess if Transfer Impact Assessment needed
  [ ] Document DPO approval decision
```

**Step 3: CMK Verification (if applicable)**
```
For US vendors or high-risk scenarios:
  [ ] Check if vendor offers CMK/BYOK
  [ ] Verify CMK is configured (not just available)
  [ ] Test key revocation (vendor cannot access data)
  [ ] Document CMK architecture and controls
```

**Step 4: Risk Assessment**
```
For each vendor:
  [ ] Assess data location vs. requirements
  [ ] Evaluate transfer mechanisms
  [ ] Consider key custody
  [ ] Rate data sovereignty risk (Low/Medium/High/Critical)
  [ ] Escalate High/Critical risks to CISO/DPO
```

#### Common Mistakes

**Mistake 1: Trusting Vendor Region Selection Without Verification**

❌ **Wrong:**
```
Vendor portal shows: eu-central-1 selected
Assessor: Marks "EU (Frankfurt)" without verification
Reality: Logs/backups may still go to US (control plane)
```

✅ **Right:**
```
Step 1: Verify region selection in vendor portal
Step 2: Review vendor architecture docs (where are logs/backups?)
Step 3: Confirm contractual data residency guarantee
Step 4: Document all processing locations (storage + control plane)
Entry: "EU (Frankfurt) - Data; US (Virginia) - Control Plane"
Assessment: ⚠️ Requires review of control plane data access
```

**Mistake 2: Accepting Old SCCs**

❌ **Wrong:**
```
DPA includes: Standard Contractual Clauses (2010)
Assessor: Marks "SCCs" as transfer mechanism
Reality: Old SCCs invalidated by Schrems II (2020)
```

✅ **Right:**
```
DPA SCCs dated: 2010
Post-Schrems II SCCs required: 2021 or later
Assessment: ❌ Non-compliant - SCCs outdated
Action: Urgent DPA amendment to use current SCCs
```

**Mistake 3: Assuming CMK is Configured**

❌ **Wrong:**
```
Vendor offers: "Customer-Managed Keys available"
Assessor: Marks "Customer-Managed Keys (CMK)"
Reality: CMK feature exists but NOT configured (using default)
```

✅ **Right:**
```
Vendor capability: CMK available
Configuration check: Log into vendor portal
Result: Using default vendor-managed keys (CMK not configured)
Entry: Provider-Managed (Default)
Gap: CMK available but not enabled
Action: Configure CMK for High/Critical services
```

**Mistake 4: Overlooking Subprocessor Locations**

❌ **Wrong:**
```
Primary storage: EU (Frankfurt)
Assessor: Marks "EU-Only (No Transfer)"
Reality: Vendor uses US subprocessor for backups
```

✅ **Right:**
```
Primary storage: EU (Frankfurt)
Subprocessor review: Backup provider in US
Assessment: Cross-border transfer exists (EU → US)
Mechanism required: SCCs
Entry: "EU (Frankfurt) - Primary; US - Backups (Subprocessor)"
Transfer Mechanism: Standard Contractual Clauses (SCCs)
```

#### Quality Checks

**Before Marking Sheet 5 Complete:**

- [ ] All data storage locations documented (no "Unknown")
- [ ] Processing locations verified (including control planes, logs)
- [ ] Cross-border transfer mechanisms identified where applicable
- [ ] All DPAs reviewed by DPO (if processing personal data)
- [ ] CMK status verified (configured vs. just available)
- [ ] Regulatory compliance documented (GDPR, FADP, etc.)
- [ ] Data sovereignty risk ratings assigned
- [ ] All High/Critical risks escalated to CISO/DPO
- [ ] Evidence saved to Evidence Register

---

### Sheet 6: Forensics & Audit Rights

#### Purpose Recap

**Goal:** Verify that contracts include adequate audit rights and that vendors have forensic investigation capabilities to support incident response.

**Why This Matters:**
- Audit rights enable verification of vendor security controls
- Forensic capabilities are essential for security incident investigation
- Regulatory requirements (DORA, NIS2, sector-specific) may mandate audit rights
- Without audit rights, you rely solely on vendor self-reporting

**Success Criterion:**
> All Critical and High vendors have documented right-to-audit clauses OR provide current third-party audit reports, and forensic investigation capabilities are contractually committed.

#### Column-by-Column Guidance

**Columns R-W: Audit and Forensic Details**

**Column R: Right-to-Audit Clause**

**Options:**
- `Yes (Full Rights)` - On-site or remote audit rights, annual + upon cause
- `Yes (Limited)` - Audit rights with restrictions (notice period, scope limits)
- `Third-Party Report Alternative` - No direct audit, but vendor provides SOC 2/audit reports
- `No` - No audit rights in contract

**How to Complete:**
1. Locate "Audit Rights" or "Right to Audit" section in contract
2. Assess scope and limitations
3. Select appropriate option

**Full Rights Criteria:**
```
Contract includes:
  ✅ Right to conduct security audits (on-site or remote)
  ✅ Annual audit minimum (scheduled)
  ✅ Additional audits upon cause (security incident, breach)
  ✅ Reasonable notice (14-30 days for scheduled, immediate for cause)
  ✅ Access to systems, personnel, documentation
  ✅ Right to engage third-party auditors
  ✅ Vendor cooperation commitment
  
Entry: Yes (Full Rights)
```

**Limited Rights Example:**
```
Contract states:
  "Customer may audit Vendor upon 90 days written notice, maximum once 
   per year, during business hours only, at Customer's expense"
   
Limitations:
  - 90 days notice (long, limits emergency response)
  - Once per year maximum (no additional for cause)
  - Business hours only (not for 24/7 services)
  - Customer pays all costs (discourages audits)
  
Entry: Yes (Limited)
Assessment: ⚠️ Restrictions limit effectiveness for Critical services
```

**Third-Party Report Alternative:**
```
Contract states:
  "In lieu of Customer audit, Vendor shall provide SOC 2 Type II report 
   annually and upon request. Customer may review findings and require 
   Vendor to address any deficiencies."
   
Entry: Third-Party Report Alternative
Assessment: ✅ Acceptable for Medium/High (not ideal for Critical)
Requirement: Verify SOC 2 report is current (within 12 months)
```

**No Audit Rights:**
```
Contract: Silent on audit rights (no clause present)

Entry: No
Assessment: ❌ Gap - no verification mechanism
Action: Negotiate audit rights clause or third-party report alternative
```

**Column S: Audit Frequency Allowed**

**Options:**
- `Annual + Upon Cause` - Best (scheduled + incident-driven)
- `Annual Only` - Standard
- `Upon Cause Only` - Reactive only
- `Upon Mutual Agreement` - Vendor can refuse (weak)
- `Not Specified` - Contract silent or unclear

**Assessment by Service Criticality:**

| Criticality | Minimum Acceptable | Preferred |
|-------------|-------------------|-----------|
| Critical | Annual + Upon Cause | Quarterly + Upon Cause |
| High | Annual + Upon Cause | Annual + Upon Cause |
| Medium | Annual OR Third-Party Report | Annual |
| Low | Third-Party Report | No specific requirement |

**Example Entries:**
```
Contract: "Annual audit plus additional audits upon security incident"
Entry: Annual + Upon Cause

Contract: "Customer may audit with 60 days notice"
No frequency specified
Entry: Not Specified
Assessment: ⚠️ Clarify in amendment (annual minimum)
```

**Column T: Third-Party Audit Report Acceptance**

**Options:**
- `SOC 2 Type II Accepted` - Customer accepts SOC 2 in lieu of direct audit
- `ISO 27001 Certificate Accepted` - Certificate sufficient
- `Both Accepted` - SOC 2 OR ISO 27001
- `Not Specified` - Contract silent on alternative
- `Not Accepted` - Direct audit required, no alternative

**How to Complete:**
1. Check if contract allows third-party reports as audit alternative
2. Verify what report types are acceptable
3. Note any requirements (report age, scope)

**Typical Clause:**
```
"Customer may elect to accept Vendor's current SOC 2 Type II report 
 (dated within the prior 12 months) in lieu of conducting a direct audit. 
 Vendor shall provide report within 30 days of Customer request."
 
Entry: SOC 2 Type II Accepted
Requirement: Report must be <12 months old
```

**Best Practice:**
- For Critical services: Direct audit rights (third-party report as supplement, not replacement)
- For High services: Direct audit OR current third-party report
- For Medium/Low: Third-party report acceptable

**Column U: Forensic Investigation Support**

**Options:**
- `Yes (Contractual Commitment)` - Contract requires forensic support
- `Yes (Best Efforts)` - Vendor commits to "cooperate" but no specifics
- `No` - No forensic support clause
- `Unknown` - Not addressed in contract

**How to Complete:**
1. Search contract for "forensic", "investigation", "incident response"
2. Assess strength of commitment
3. Verify what support is included (log access, expert assistance, etc.)

**Strong Forensic Commitment:**
```
Contract clause:
  "In the event of a Security Incident, Vendor shall:
    - Provide Customer with forensic-level access to relevant logs
    - Preserve evidence in accordance with industry standards
    - Cooperate with Customer's forensic investigation team
    - Provide technical expert assistance upon request
    - Response time: Within 24 hours of Customer request
    - Duration: For the duration of investigation and 90 days thereafter"
    
Entry: Yes (Contractual Commitment)
```

**Weak Commitment:**
```
Contract: "Vendor will reasonably cooperate with security investigations"

Problems:
  - "Reasonably" is undefined
  - No response time commitment
  - No specific obligations (log access, preservation, etc.)
  
Entry: Yes (Best Efforts)
Assessment: ⚠️ Weak - lacks specificity for effective investigation
```

**Column V: Log Retention Period**

**Format:** Time period (e.g., "12 months", "90 days", "Not specified")

**How to Complete:**
1. Locate log retention commitment in contract or security documentation
2. Note retention period for security logs (authentication, access, changes)
3. Verify if logs are accessible to Customer

**Log Retention Requirements:**

| Service Type | Minimum Retention | Preferred Retention |
|--------------|-------------------|---------------------|
| Critical | 12 months | 24 months |
| High | 6 months | 12 months |
| Medium | 3 months | 6 months |
| Low | No minimum | 3 months |

**Regulatory Considerations:**

- **GDPR**: No specific retention, but logs needed for breach investigation/reporting
- **DORA**: Financial entities may require 5+ years for critical systems
- **PCI-DSS**: Minimum 1 year, 3 months immediately available
- **HIPAA**: Minimum 6 years for healthcare data access logs

**Example Entries:**
```
Contract: "Security logs retained for 12 months"
Entry: 12 months

Vendor documentation: "Logs available for 90 days via portal"
Contract: Silent on log retention
Entry: 90 days (documentation only, not contractual)
Assessment: ⚠️ Should be in contract for enforceability

Contract & documentation: No log retention specified
Entry: Not specified
Assessment: ❌ Gap - require contractual commitment
```

**Column W: Incident Investigation Cooperation**

**Options:**
- `Yes (Detailed SLA)` - Response times and cooperation defined
- `Yes (General Commitment)` - Cooperation commitment but vague
- `No` - No cooperation clause
- `Unknown` - Not addressed

**How to Complete:**
1. Review incident notification and response clauses
2. Assess cooperation commitments
3. Look for response time SLAs

**Strong Cooperation Clause:**
```
Contract:
  "Upon security incident:
    - Initial response: Within 4 hours
    - Forensic log provision: Within 24 hours
    - Root cause analysis: Within 72 hours of containment
    - Vendor technical expert availability: 24/7 for Critical incidents
    - Regular status updates: Every 4 hours until resolution"
    
Entry: Yes (Detailed SLA)
```

**Weak Cooperation:**
```
Contract: "Vendor will cooperate with incident investigations"

Entry: Yes (General Commitment)
Assessment: ⚠️ No SLA, no specifics - difficult to enforce
```

#### Evidence Requirements

**For Each Vendor:**

**MUST HAVE:**
- ✅ Contract sections on audit rights
- ✅ Forensic investigation clauses
- ✅ Log retention documentation

**SHOULD HAVE:**
- ✅ Most recent SOC 2 Type II report (if accepting as alternative)
- ✅ Vendor incident response plan documentation
- ✅ Log access procedure (how to request logs)

**NICE TO HAVE:**
- ✅ Sample audit reports (if audits previously conducted)
- ✅ Vendor forensic capabilities white paper
- ✅ Incident response exercise results

#### Verification Steps
```
For each vendor:
  [ ] Extract audit rights clauses from contract
  [ ] Verify audit frequency and scope
  [ ] Check third-party report availability (if applicable)
  [ ] Review forensic investigation commitments
  [ ] Confirm log retention periods
  [ ] Document incident cooperation SLAs
  [ ] Assess adequacy for service criticality
  [ ] Escalate gaps to Legal for amendment
```

#### Common Mistakes

**Mistake 1: Assuming "Reasonable Cooperation" is Sufficient**

❌ **Wrong:**
```
Contract: "Vendor will reasonably cooperate"
Assessor: Marks as adequate
Reality: No enforceable commitment, no SLA
```

✅ **Right:**
```
"Reasonable cooperation" is too vague
Requirement: Specific SLA for forensic support
Action: Negotiate amendment with defined response times
```

**Mistake 2: Not Verifying Third-Party Report Currency**

❌ **Wrong:**
```
Contract allows SOC 2 Type II as alternative
Vendor claims "we have SOC 2"
Assessor: Marks as compliant without seeing report
```

✅ **Right:**
```
Request actual SOC 2 Type II report
Verify examination period end date
Confirm <12 months old
Review for qualified opinions or significant findings
```

#### Quality Checks

- [ ] All Critical/High vendors have audit rights OR third-party reports
- [ ] Forensic investigation support documented
- [ ] Log retention periods meet requirements
- [ ] Incident cooperation SLAs specified
- [ ] Gaps escalated to Legal for contract amendments
- [ ] SOC 2 reports obtained and verified current (if used as alternative)

---

### Sheet 7: Jurisdictional Risk Assessment

#### Purpose Recap

**Goal:** Assess legal jurisdiction risks for vendors with US nexus, particularly CLOUD Act exposure, and document compensating controls.

**Why This Matters:**
- US CLOUD Act allows US government to compel US companies to provide data stored anywhere globally
- EU data stored with US providers may be accessible to US authorities
- GDPR Schrems II ruling requires assessment of conflicting laws (like CLOUD Act)
- Compensating controls (CMK, EU Data Boundary) can mitigate but not eliminate risk

**Success Criterion:**
> All vendors with US headquarters or US parent companies have documented jurisdictional risk assessment, with compensating controls implemented for High/Critical risk exposures.

#### Who Should Complete This Sheet

**This is a SPECIALIZED assessment requiring:**
- **Primary:** Compliance/DPO (CLOUD Act expertise, GDPR Schrems II interpretation)
- **Support:** Legal (jurisdictional law, enforceability)
- **Support:** Security (technical controls - CMK verification)
- **Review:** CISO (risk acceptance for High/Critical exposures)

#### Column-by-Column Guidance

**Columns R-T: Jurisdictional Risk Assessment**

**Column R: Provider Headquarters Jurisdiction**

**Format:** Country (e.g., "United States", "Ireland", "Switzerland")

**How to Complete:**
1. Research vendor's legal headquarters (not just office locations)
2. Verify on vendor website (About Us, Legal entity info)
3. Check company registration documents if available
4. Note parent company jurisdiction if different

**Critical Distinction:**
```
Legal Headquarters vs. Office Locations

Example: Vendor XYZ
  - Offices: Ireland, Germany, UK, US
  - Legal HQ: Ireland (registered in Ireland)
  - Parent Company: US (owned by US Corp)
  
Entry for Provider HQ: Ireland
Entry for Parent (next column): United States

Risk: US parent may be subject to CLOUD Act despite Irish subsidiary
```

**How to Verify:**

1. **Vendor Website:**
   - Look for "About Us" → "Company Information"
   - Check legal entity name (e.g., "XYZ Ireland Limited" vs. "XYZ Inc.")

2. **Contract:**
   - Signature page shows legal entity
   - Example: "Amazon Web Services EMEA SARL" (Luxembourg entity)

3. **Company Registry:**
   - Ireland: Companies Registration Office (CRO)
   - UK: Companies House
   - US: State business registries

**Example Entries:**
```
AWS: United States (Amazon Web Services, Inc.)
Microsoft Azure: United States (Microsoft Corporation)
Google Cloud: United States (Google LLC)
Salesforce: United States (Salesforce.com Inc.)
OVHcloud: France (OVH SAS)
```

**Column S: US Nexus (Parent Company or HQ)**

**Options:**
- `Yes - US HQ` - Headquartered in United States
- `Yes - US Parent` - Non-US HQ but US parent company
- `No` - No US connection
- `Unknown` - Ownership structure unclear

**How to Complete:**
1. If Column R = United States → `Yes - US HQ`
2. If Column R ≠ United States, research parent company
3. Check corporate ownership structure
4. Verify ultimate parent entity jurisdiction

**Why This Matters:**
```
CLOUD Act Application:
  - Applies to US companies (HQ in US)
  - Applies to non-US subsidiaries of US companies
  - Does NOT apply to EU companies with no US ownership
  
Example 1: Salesforce Ireland (subsidiary of Salesforce Inc.)
  - HQ: Ireland
  - Parent: United States
  - US Nexus: Yes - US Parent
  - CLOUD Act Risk: YES (US can compel parent, parent controls subsidiary)

Example 2: OVHcloud (French company, no US parent)
  - HQ: France
  - Parent: France
  - US Nexus: No
  - CLOUD Act Risk: NO
```

**How to Research Parent Company:**

1. **Vendor Website:**
   - Look for "Our Company" → "Corporate Structure"
   - Press releases about acquisitions

2. **LinkedIn Company Page:**
   - Often shows parent organization

3. **Business Databases:**
   - Crunchbase, Bloomberg, Reuters

4. **Annual Reports/SEC Filings:**
   - US public companies file with SEC
   - Ownership structure disclosed

**Column T: CLOUD Act Potential Exposure**

**Options:**
- `Potential Exposure (Unmitigated)` - US nexus + no compensating controls
- `Mitigated (CMK)` - Customer-managed keys deployed
- `Mitigated (CMK + EU Boundary)` - CMK AND EU Data Boundary commitment
- `Not Applicable (EU Provider)` - No US nexus
- `Not Assessed` - US nexus but not yet assessed

**How to Complete:**
1. If Column S = No → `Not Applicable (EU Provider)`
2. If Column S = Yes, assess compensating controls:
   - Check if CMK deployed (from Sheet 5, Column V)
   - Check if EU Data Boundary commitment (from Sheet 5, Column U)
   - Select appropriate mitigation level

**CLOUD Act Exposure Matrix:**

| US Nexus | Data Location | CMK | EU Boundary | Exposure Level | Entry |
|----------|---------------|-----|-------------|----------------|-------|
| No | Any | Any | N/A | None | Not Applicable (EU Provider) |
| Yes | US | No | No | Direct | Potential Exposure (Unmitigated) |
| Yes | EU | No | No | Via CLOUD Act | Potential Exposure (Unmitigated) |
| Yes | EU | Yes | No | Partially Mitigated | Mitigated (CMK) |
| Yes | EU | Yes | Yes | Strongly Mitigated | Mitigated (CMK + EU Boundary) |

**Understanding Mitigation Levels:**

**"Potential Exposure (Unmitigated)":**
```
Scenario: AWS with EU data, provider-managed keys, no EU Boundary

Risk: 
  - US government can issue CLOUD Act warrant to AWS
  - AWS has encryption keys, can decrypt data
  - AWS legally required to comply with warrant
  - Data may be provided to US government

Compensating Controls: None
Entry: Potential Exposure (Unmitigated)
Risk Rating (Column N): High or Critical
```

**"Mitigated (CMK)":**
```
Scenario: AWS with EU data, customer-managed keys

Risk Mitigation:
  - Customer controls encryption keys
  - AWS cannot decrypt data without customer providing keys
  - Even if CLOUD Act warrant issued, AWS cannot provide plaintext

Limitations:
  - Metadata still accessible (who accessed, when, file names)
  - Backups may not use CMK (verify)
  - Customer could be compelled to provide keys (rare)

Entry: Mitigated (CMK)
Risk Rating: Medium
```

**"Mitigated (CMK + EU Boundary)":**
```
Scenario: Microsoft Azure with CMK + EU Data Boundary commitment

Risk Mitigation:
  - Customer-managed keys (technical control)
  - Contractual commitment: EU data stays in EU, EU-only operations
  - Microsoft commits to challenge any conflicting US legal demands
  - Transparency commitment (notify customer of legal demands)

Limitations:
  - Contractual commitment strength depends on enforceability
  - Legal challenge may not succeed
  - "EU Data Boundary" implementation details vary by vendor

Entry: Mitigated (CMK + EU Boundary)
Risk Rating: Low-Medium
```

**Column U: Compensating Controls Documented**

**Format:** Free text description

**How to Complete:**
1. List all compensating controls for CLOUD Act risk
2. Include both technical and contractual controls
3. Provide evidence references

**Common Compensating Controls:**

| Control Type | Description | Effectiveness |
|--------------|-------------|---------------|
| **Customer-Managed Keys (CMK)** | Customer controls encryption keys | High (vendor cannot decrypt) |
| **EU Data Boundary** | Contractual commitment to EU-only ops | Medium (depends on enforcement) |
| **Data Minimization** | Reduce data volume/sensitivity in cloud | Medium (less exposure) |
| **Data Residency Guarantee** | Contract prohibits data leaving EU | Medium (contractual) |
| **Access Restrictions** | Limit non-EU personnel access | Low-Medium (procedural) |
| **Transparency Commitment** | Vendor commits to notify of legal demands | Low (information only, doesn't prevent) |
| **Legal Challenge Commitment** | Vendor commits to challenge conflicting demands | Low-Medium (outcome uncertain) |

**Example Entries:**
```
Example 1: Strong Compensating Controls (AWS)
  Compensating Controls:
    - Customer-Managed Keys (AWS KMS) - Enabled 15.01.2026
    - EU Data Boundary commitment (contract clause 8.4)
    - Data residency locked to eu-central-1 (Frankfurt)
    - AWS commits to legal challenge of conflicting demands
    - Transparency: AWS will notify of legal demands
    
  Evidence:
    - CMK configuration: EV-VDD-045
    - Contract clause: EV-VDD-046
    - AWS EU Data Boundary documentation: EV-VDD-047

Example 2: Partial Controls
  Compensating Controls:
    - Data classification: Only Internal data in cloud (no Confidential/Restricted)
    - Data minimization: PII removed before upload
    - Contractual data residency: EU-only storage
    
  Limitations:
    - Provider-managed keys (vendor can decrypt)
    - No EU Data Boundary commitment
    
  Evidence: EV-VDD-050, EV-VDD-051
  
Example 3: Risk Acceptance (No Controls)
  Compensating Controls: None
  
  Risk Acceptance:
    - Service criticality: Low
    - Data classification: Public only
    - Risk accepted by CISO on 10.01.2026
    - Risk ID: RISK-2026-055
```

**Column V: Jurisdictional Risk Rating**

**Options:**
- `Low` - No US nexus OR strong compensating controls
- `Medium` - US nexus with partial mitigation (CMK OR boundary)
- `High` - US nexus with weak/no mitigation, Confidential data
- `Critical` - US nexus, no mitigation, Restricted data

**How to Complete:**
1. Assess US nexus status
2. Evaluate compensating controls
3. Consider data classification
4. Assign risk rating

**Risk Rating Decision Matrix:**

| US Nexus | Data Classification | CMK | EU Boundary | Risk Rating |
|----------|---------------------|-----|-------------|-------------|
| No | Any | N/A | N/A | Low |
| Yes | Public | Any | Any | Low |
| Yes | Internal | Yes | Yes | Low |
| Yes | Internal | Yes | No | Medium |
| Yes | Internal | No | Any | Medium |
| Yes | Confidential | Yes | Yes | Medium |
| Yes | Confidential | Yes | No | High |
| Yes | Confidential | No | Any | High |
| Yes | Restricted | Yes | Yes | High |
| Yes | Restricted | Any | No | Critical |

**Example Risk Ratings:**
```
Example 1: AWS - Critical Service, Confidential Data
  US Nexus: Yes - US HQ
  Data: Confidential customer data
  CMK: Yes (enabled)
  EU Boundary: Yes (commitment)
  
  Risk Rating: Medium
  Rationale: Strong compensating controls mitigate CLOUD Act risk

Example 2: Small US SaaS - High Service, Confidential Data
  US Nexus: Yes - US HQ
  Data: Confidential
  CMK: No (not offered by vendor)
  EU Boundary: No
  
  Risk Rating: High
  Action: Escalate to CISO, consider alternative vendor

Example 3: OVHcloud - Critical Service, Restricted Data
  US Nexus: No (French company)
  
  Risk Rating: Low
  Rationale: No CLOUD Act exposure (EU jurisdiction)
```

#### Evidence Requirements

**For Each US-Nexus Vendor:**

**MUST HAVE:**
- ✅ Corporate structure documentation (HQ, parent company)
- ✅ Compensating controls evidence (CMK config, EU Boundary contract)
- ✅ Risk assessment memo
- ✅ CISO/DPO approval (for High/Critical risks)

**SHOULD HAVE:**
- ✅ Vendor CLOUD Act white paper (if available)
- ✅ Transfer Impact Assessment (TIA) per Schrems II
- ✅ Legal opinion on CLOUD Act applicability (for Critical services)

#### Verification Steps
```
Week 1: Identify US-Nexus Vendors
  [ ] Review vendor list from A.5.23.1
  [ ] Research HQ and parent company for each
  [ ] Flag all US-nexus vendors for assessment

Week 2: Assess Compensating Controls
  [ ] Verify CMK deployment (from Sheet 5)
  [ ] Review EU Data Boundary commitments (contracts)
  [ ] Document all compensating controls
  [ ] Collect evidence

Week 3: Risk Rating & Escalation
  [ ] Assign jurisdictional risk rating
  [ ] Escalate High/Critical risks to CISO/DPO
  [ ] Obtain risk acceptance or remediation plan
  [ ] Document decisions
```

#### Common Mistakes

**Mistake 1: Assuming EU Data Center = No CLOUD Act Risk**

❌ **Wrong:**
```
Vendor: US company
Data location: EU (Frankfurt)
Assessor: Marks "Not Applicable" (data in EU)
Reality: CLOUD Act applies regardless of data location
```

✅ **Right:**
```
Vendor: US company (or US parent)
US Nexus: Yes
CLOUD Act applies: YES (regardless of data location)
Assess compensating controls and rate risk appropriately
```

**Mistake 2: Accepting "EU Data Boundary" Without Verification**

❌ **Wrong:**
```
Vendor claims: "We offer EU Data Boundary"
Assessor: Marks as strong mitigation
Reality: Feature exists but not configured/contracted
```

✅ **Right:**
```
Vendor capability: EU Data Boundary available
Verification needed:
  1. Is it configured for your tenant?
  2. Is it in the contract (enforceable)?
  3. What data does it cover (all? or just some services)?
Document actual implementation, not just availability
```

#### Quality Checks

- [ ] All US-nexus vendors identified (HQ or parent)
- [ ] CLOUD Act exposure assessed for all US-nexus vendors
- [ ] Compensating controls documented with evidence
- [ ] Jurisdictional risk ratings assigned
- [ ] High/Critical risks escalated to CISO/DPO
- [ ] Risk acceptance or remediation plans documented
- [ ] Evidence saved to Evidence Register

---

**END OF SECTION 4 PART 2: COMPLETING SHEETS 5-7**

## Section 4: Completing Each Sheet - Detailed Guidance (Part 3)

### Sheet 8: Summary Dashboard

#### Purpose Recap

**Goal:** Provide executive-level summary of vendor compliance status through auto-calculated metrics and visualizations.

**Why This Matters:**
- Executive leadership needs high-level compliance view (not 50+ rows of vendor details)
- Identifies gaps and risks requiring escalation at a glance
- Tracks vendor compliance trends over time
- Supports board reporting and audit readiness demonstrations

**Key Principle:**
> "This sheet is READ-ONLY for users. All data flows automatically from Sheets 2-7 via formulas. Your job is to INTERPRET the results, not to edit them."

**Success Criterion:**
> Dashboard shows overall vendor compliance ≥85%, with no Critical/High services from non-compliant vendors, and all High/Critical jurisdictional risks have documented compensating controls.

#### Dashboard Structure Overview

**The dashboard is organized into 6 sections:**

1. **Overall Compliance Statistics** - Total vendors, overall compliance percentage
2. **Compliance by Assessment Area** - Certification, contracts, SLA, data sovereignty, audit rights, jurisdictional risk
3. **Gap Analysis** - Vendors requiring remediation
4. **Vendor Risk Distribution** - How many Critical/High/Medium/Low risk vendors
5. **Jurisdictional Risk Metrics** - CLOUD Act exposure summary
6. **Action Items** - Top priorities requiring escalation

#### Understanding Auto-Calculated Metrics

**Section 1: Overall Compliance Statistics**

**Metric 1: Total Vendors Assessed**
```
Formula: =COUNTA('2. Security Certifications'!B7:B200)
(Counts non-empty vendor names in Sheet 2)

Example Result: 47

Interpretation:
  - This should match your A.5.23.1 inventory count
  - If mismatch, vendors missing from assessment
```

**What to Check:**
- [ ] Count matches A.5.23.1 inventory (no vendors missed)
- [ ] Count is reasonable for organization size (~300 staff → expect 30-60 vendors)

**Metric 2: Overall Compliance Percentage**
```
Formula: =COUNTIF('2. Security Certifications'!H7:H200,"✅ Compliant") / 
         COUNTA('2. Security Certifications'!B7:B200)

Example Result: 87% (41 compliant out of 47 vendors)

Interpretation:
  85%+ = Good (some gaps acceptable)
  70-84% = Concerning (significant gaps)
  <70% = Poor (major compliance issues)
```

**What to Do Based on Result:**

| Percentage | Status | Action Required |
|------------|--------|-----------------|
| 90%+ | ✅ Excellent | Maintain, focus on continuous improvement |
| 85-89% | ✅ Good | Address remaining gaps in quarterly review |
| 70-84% | ⚠️ Concerning | Escalate to CISO, prioritize gap remediation |
| <70% | ❌ Poor | Executive escalation, vendor remediation program needed |

**Metric 3: Vendors by Status**
```
Compliant: =COUNTIF(Sheet2!H:H,"✅ Compliant")
Partial: =COUNTIF(Sheet2!H:H,"⚠️ Partial")
Non-Compliant: =COUNTIF(Sheet2!H:H,"❌ Non-Compliant")

Example Results:
  ✅ Compliant: 41 (87%)
  ⚠️ Partial: 4 (9%)
  ❌ Non-Compliant: 2 (4%)
```

**Interpretation:**
```
✅ Compliant (87%): Good baseline
⚠️ Partial (9%): Acceptable - minor gaps being addressed
❌ Non-Compliant (4%): 2 vendors require urgent attention

Action: 
  1. Review Partial vendors - verify remediation plans exist
  2. Escalate Non-Compliant vendors to CISO
  3. If Non-Compliant vendors are Critical/High services → URGENT
```

**Metric 4: Critical/High Services Compliance**
```
Formula: =COUNTIFS('2. Security Certifications'!D7:D200,"Critical",
                   '2. Security Certifications'!H7:H200,"✅ Compliant") +
         COUNTIFS('2. Security Certifications'!D7:D200,"High",
                   '2. Security Certifications'!H7:H200,"✅ Compliant")

Denominator: =COUNTIF('2. Security Certifications'!D7:D200,"Critical") +
              COUNTIF('2. Security Certifications'!D7:D200,"High")

Example: 18 out of 20 Critical/High services compliant = 90%
```

**Target:** 100% for Critical/High services (no exceptions without CISO risk acceptance)

**What to Do if <100%:**
```
IF Critical/High service is Non-Compliant:
  1. IMMEDIATE escalation to CISO
  2. Risk assessment required
  3. Options:
     a) Vendor must achieve compliance (set deadline)
     b) Formal risk acceptance (CISO sign-off)
     c) Replace vendor (migration plan)
     
DO NOT allow Critical/High services to remain non-compliant without formal risk acceptance.
```

---

**Section 2: Compliance by Assessment Area**

**This section shows compliance percentage for each assessment area:**

| Assessment Area | Source Sheet | Metric |
|-----------------|--------------|--------|
| Security Certifications | Sheet 2 | % vendors with ISO 27001 or SOC 2 Type II |
| Contract Terms | Sheet 3 | % contracts with adequate DPA and terms |
| SLA Performance | Sheet 4 | % vendors meeting SLA commitments |
| Data Sovereignty | Sheet 5 | % vendors compliant with data residency |
| Audit Rights | Sheet 6 | % vendors with audit rights or 3rd party reports |
| Jurisdictional Risk (NEW) | Sheet 7 | % vendors with Low/Medium risk (not High/Critical) |

**How to Interpret Results:**

**Example Dashboard Section 2:**
```
Assessment Area                  Compliance %    Status
─────────────────────────────────────────────────────────
Security Certifications          89% (42/47)     ✅ Good
Contract Terms                   83% (39/47)     ⚠️ Acceptable
SLA Performance                  91% (43/47)     ✅ Good
Data Sovereignty                 94% (44/47)     ✅ Excellent
Audit Rights                     87% (41/47)     ✅ Good
Jurisdictional Risk      79% (37/47)     ⚠️ Concerning
─────────────────────────────────────────────────────────
```

**Analysis:**
```
Security Certifications (89%): 
  - Good coverage
  - 5 vendors without ISO 27001/SOC 2
  - Action: Review if these 5 are Critical/High services

Contract Terms (83%):
  - 8 vendors with inadequate contracts
  - Action: Review Sheet 3 Column J (gaps) for these 8 vendors
  - Prioritize Critical/High for contract amendments

Jurisdictional Risk (79%):
  - 10 vendors with High/Critical jurisdictional risk
  - Action: Review Sheet 7 - likely US vendors without CMK
  - Implement compensating controls or accept risk
```

**What Each Percentage Represents:**

**Security Certifications:**
```
Formula: =COUNTIFS('2. Security Certifications'!R7:R200,"Yes (Current)",
                   '2. Security Certifications'!U7:U200,"Yes*") / 
         COUNTA('2. Security Certifications'!B7:B200)

Counts: Vendors with EITHER current ISO 27001 OR SOC 2 Type II (< 12 months)

Low %: Many vendors lack third-party security assurance
Action: Require certifications or accept risk for non-certified vendors
```

**Contract Terms:**
```
Formula: =COUNTIFS('3. Contract Terms'!R7:R200,"Yes (Adequate)",
                   '3. Contract Terms'!U7:U200,"Yes (Favorable)*") / 
         COUNTA('3. Contract Terms'!B7:B200)

Counts: Vendors with adequate DPA AND favorable indemnification

Low %: Contracts may not protect organization adequately
Action: Legal review and amendment negotiations
```

**SLA Performance:**
```
Formula: =COUNTIF('4. SLA Performance'!W7:W200,"0") / 
         COUNTA('4. SLA Performance'!B7:B200)

Counts: Vendors with ZERO SLA breaches in last 12 months

Low %: Many vendors failing to meet SLA commitments
Action: Escalate to vendors, claim service credits, consider replacements
```

**Data Sovereignty:**
```
Formula: =COUNTIF('5. Data Sovereignty'!Y7:Y200,"Low") + 
         COUNTIF('5. Data Sovereignty'!Y7:Y200,"Medium") / 
         COUNTA('5. Data Sovereignty'!B7:B200)

Counts: Vendors with Low or Medium data sovereignty risk

Low %: Many vendors have High/Critical data residency risks
Action: DPO review, implement CMK, require data residency commitments
```

**Jurisdictional Risk:**
```
Formula: =COUNTIF('7. Jurisdictional Risk'!V7:V200,"Low") + 
         COUNTIF('7. Jurisdictional Risk'!V7:V200,"Medium") / 
         COUNTA('7. Jurisdictional Risk'!B7:B200)

Counts: Vendors with Low or Medium jurisdictional risk (not High/Critical)

Low %: Many US vendors without adequate CLOUD Act mitigations
Action: Deploy CMK, negotiate EU Data Boundary, or accept risk
```

---

**Section 3: Gap Analysis**

**This section identifies specific vendors requiring attention:**

**Gap Type 1: Vendors Without ISO 27001 or SOC 2**
```
Formula: Lists vendors where:
  - ISO 27001 = "No" OR "Yes (Expired)" AND
  - SOC 2 Type II = "No"

Example Output:
  1. Small SaaS Vendor Inc. (Service: Project Management)
  2. Niche Provider LLC (Service: Data Analytics)
  3. ...

What to Do:
  For each vendor:
    1. Check service criticality (Sheet 2, Column D)
    2. If Critical/High: URGENT - require certification or replace
    3. If Medium/Low: Document risk, set timeline for certification
```

**Gap Type 2: Contracts Missing DPA or Inadequate Terms**
```
Lists vendors where:
  - DPA = "No" OR "Yes (Weak)" OR
  - Liability Cap inadequate for criticality OR
  - No termination rights

Example Output:
  1. Vendor A - No DPA (processing personal data)
  2. Vendor B - Liability cap CHF 100 (Critical service)
  3. ...

Action:
  Escalate to Legal for contract amendments
  Prioritize by service criticality
  Set amendment deadlines
```

**Gap Type 3: SLA Breaches Requiring Escalation**
```
Lists vendors where:
  - SLA breaches > 3 in last 12 months OR
  - Performance trend = "Declining"

Example Output:
  1. Vendor C - 5 breaches (Jan, Feb, Mar, Jun, Aug)
  2. Vendor D - Declining trend (99.95% → 99.82%)

Action:
  Escalate to vendor account manager
  Request root cause analysis and improvement plan
  Calculate unclaimed service credits
  Consider vendor replacement if no improvement
```

**Gap Type 4: Data Sovereignty Violations**
```
Lists vendors where:
  - Data sovereignty risk = "High" or "Critical" AND
  - No compensating controls documented

Example Output:
  1. Vendor E - US provider, Confidential data, no CMK
  2. Vendor F - Data in US, no SCCs

Action:
  DPO escalation (GDPR/FADP compliance risk)
  Implement compensating controls (CMK, data minimization)
  OR migrate to compliant vendor
```

**Gap Type 5: Missing Audit Rights**
```
Lists vendors where:
  - Service criticality = "Critical" OR "High" AND
  - Audit rights = "No" AND
  - Third-party report = "Not Specified" or not current

Example Output:
  1. Vendor G (Critical service, no audit rights)

Action:
  Negotiate audit rights clause
  OR require current third-party report (SOC 2 Type II)
  Cannot verify vendor security without audit capability
```

**Gap Type 6: High/Critical Jurisdictional Risks**
```
Lists vendors where:
  - Jurisdictional risk rating = "High" or "Critical" AND
  - Compensating controls = "None" or insufficient

Example Output:
  1. US Vendor H - Confidential data, no CMK, no EU Boundary
  2. US Vendor I - Restricted data, provider-managed keys

Action:
  CISO/DPO escalation
  Implement CMK immediately
  Negotiate EU Data Boundary commitment
  OR migrate to EU provider
  Document risk acceptance if controls not feasible
```

---

**Section 4: Vendor Risk Distribution**

**This section shows breakdown by risk rating:**
```
Risk Rating      Count    Percentage    Critical/High Services
──────────────────────────────────────────────────────────────
Low              30       64%           12 (60%)
Medium           12       26%           6 (30%)
High             4        8%            2 (10%)
Critical         1        2%            0 (0%)
──────────────────────────────────────────────────────────────
Total            47       100%          20 (100%)
```

**Interpretation:**

**Target Distribution:**
- Low: 60-80% (most vendors should be low risk)
- Medium: 15-30% (acceptable residual risk)
- High: 5-10% (managed with compensating controls)
- Critical: <5% (requires immediate remediation or CISO risk acceptance)

**Red Flags:**
- ❌ Critical/High services from High/Critical risk vendors
- ❌ >15% of vendors rated Critical/High
- ❌ Any Critical risk rating without formal risk acceptance

**What to Do:**
```
IF High/Critical Risk Vendors Exist:
  1. Review Sheet 2-7 to understand root cause of high risk
  2. Develop remediation plan:
     - Vendor achieves compliance (certifications, contract amendments)
     - Implement compensating controls
     - Migrate to lower-risk vendor
  3. If no remediation feasible:
     - Document risk thoroughly
     - Obtain CISO formal risk acceptance
     - Review risk quarterly (re-evaluate)
```

---

**Section 5: Jurisdictional Risk Metrics**

**This section provides CLOUD Act exposure summary:**
```
Metric                                          Count    Status
──────────────────────────────────────────────────────────────
Providers with US Nexus                         22       Info
Providers with US Parent Company                8        ⚠️ Review
CLOUD Act Potential Exposure (Unmitigated)      5        ⚠️ Review
CLOUD Act Mitigated (CMK)                       10       Info
CLOUD Act Mitigated (CMK + EU Boundary)         7        ✅ OK
High/Critical Jurisdictional Risk               3        ❌ Action
Providers Without EU Data Boundary              15       ⚠️ Review
Providers Without Customer-Managed Keys         18       ⚠️ Review
──────────────────────────────────────────────────────────────
```

**How to Interpret:**

**Providers with US Nexus (22):**
- Information only - shows how many vendors subject to CLOUD Act
- High count expected (AWS, Azure, Google, Salesforce, etc. all US-based)

**Providers with US Parent Company (8):**
- Non-US subsidiaries of US companies
- Example: Salesforce Ireland (subsidiary of Salesforce Inc.)
- Still subject to CLOUD Act through parent company

**CLOUD Act Potential Exposure - Unmitigated (5):**
- ⚠️ These vendors are US-nexus with NO compensating controls
- Provider-managed keys (vendor can decrypt)
- No EU Data Boundary commitment
- **Action Required:** Review Sheet 7 for these 5 vendors
  - Implement CMK
  - Negotiate EU Data Boundary
  - OR accept risk (CISO sign-off)

**CLOUD Act Mitigated - CMK (10):**
- Customer-managed keys deployed
- Partial mitigation (vendor cannot decrypt data)
- Metadata still potentially accessible

**CLOUD Act Mitigated - CMK + EU Boundary (7):**
- ✅ Strong mitigation
- CMK + contractual EU-only commitment
- Best practice for US vendors

**High/Critical Jurisdictional Risk (3):**
- ❌ **URGENT ACTION REQUIRED**
- 3 vendors with unacceptable jurisdictional risk
- Typically: Confidential/Restricted data + US vendor + no CMK
- **Action:** 
  1. Review these 3 vendors in Sheet 7
  2. Determine if Critical/High services
  3. If yes: IMMEDIATE escalation to CISO/DPO
  4. Implement controls or migrate

**Providers Without EU Data Boundary (15):**
- No contractual commitment to EU-only operations
- Consider for Critical/High services with Confidential data
- May be acceptable if CMK deployed

**Providers Without CMK (18):**
- Using provider-managed encryption keys
- Vendor can decrypt data (CLOUD Act vulnerability)
- Consider deploying CMK for Critical/High services

**Action Priority Matrix:**

| Risk Scenario | Priority | Action |
|---------------|----------|--------|
| Critical Risk + Confidential Data + No CMK | **P0 (Urgent)** | Deploy CMK within 30 days OR migrate |
| High Risk + Confidential Data + No CMK | **P1 (High)** | Deploy CMK within 60 days OR risk acceptance |
| Medium Risk + Internal Data + No CMK | **P2 (Medium)** | Plan CMK deployment, 90-day timeline |
| Low Risk OR Public Data | **P3 (Low)** | No immediate action, review annually |

---

**Section 6: Action Items (Executive Summary)**

**This section provides top priorities for executive attention:**
```
Priority  Action Item                                    Count  Owner
────────────────────────────────────────────────────────────────────
P0        Critical/High services without certifications  2      CISO
P0        GDPR violations (no DPA/SCCs)                 1      DPO/Legal
P0        Critical jurisdictional risks (no mitigation)  3      CISO/DPO
P1        Contract amendments required                   8      Legal
P1        SLA breaches requiring vendor escalation       4      Procurement
P1        Deploy CMK for High-risk vendors              5      Security
P2        Annual audit rights to be exercised            3      Compliance
P2        Expired certifications - renewal required      4      Procurement
────────────────────────────────────────────────────────────────────
```

**Priority Definitions:**

- **P0 (Urgent):** Immediate action required (days to weeks)
- **P1 (High):** Action required within 1-2 months
- **P2 (Medium):** Action required within quarter
- **P3 (Low):** Ongoing monitoring, address opportunistically

**Who Uses This Section:**

- **CISO:** Review P0/P1 items weekly
- **Executive Leadership:** Review in monthly security briefing
- **Board:** Review quarterly (focus on P0 trends)

---

#### How to Use the Dashboard

**Monthly Review Process:**
```
Step 1: Review Overall Compliance (Section 1)
  - Is compliance % improving or declining vs. last month?
  - Are there new Non-Compliant vendors?
  - Action: Investigate any drops in compliance

Step 2: Review Compliance by Area (Section 2)
  - Which area has lowest compliance?
  - Action: Prioritize that area for remediation

Step 3: Review Gap Analysis (Section 3)
  - Review each gap category
  - Verify remediation plans exist
  - Action: Update remediation deadlines

Step 4: Review Jurisdictional Risks (Section 5 - NEW)
  - Any increase in High/Critical jurisdictional risks?
  - CMK deployment progress?
  - Action: Track CMK rollout to US vendors

Step 5: Review Action Items (Section 6)
  - Any new P0 items?
  - P1 items becoming overdue?
  - Action: Escalate overdue items to responsible owners
```

**Quarterly Board Reporting:**

Extract from dashboard:
- Overall compliance % (trend over last 4 quarters)
- Number of Critical/High services from compliant vendors
- Top 3 vendor risks and mitigation plans
- Jurisdictional risk summary (CLOUD Act exposure)

---

#### Common Mistakes

**Mistake 1: Editing Dashboard Formulas**

❌ **Wrong:**
```
User sees: "Only 79% jurisdictional risk compliance"
User thinks: "I'll just change this to 95% for the report"
User edits formula to inflate number
```

✅ **Right:**
```
Dashboard shows reality, not desired state
If compliance is low, FIX THE GAPS (Sheets 2-7)
Dashboard will automatically update when gaps are resolved
DO NOT edit formulas - they're read-only for a reason
```

**Mistake 2: Ignoring Trends**

❌ **Wrong:**
```
Month 1: 85% compliance - "Good enough"
Month 2: 83% compliance - "Still acceptable"
Month 3: 80% compliance - "Not too bad"
(Declining trend ignored until compliance falls below threshold)
```

✅ **Right:**
```
Month 1: 85% compliance
Month 2: 83% compliance (-2% TREND ALERT)
Action: Investigate why compliance is declining
  - New non-compliant vendors added?
  - Existing vendors lost certifications?
  - Contract renewals with worse terms?
Address root cause before further decline
```

**Mistake 3: Focusing Only on Overall Percentage**

❌ **Wrong:**
```
Overall: 87% compliance - "We're good!"
(Misses: 2 Critical services from non-compliant vendors)
```

✅ **Right:**
```
Review BOTH:
  - Overall compliance (87%)
  - Critical/High service compliance (90%)
  
Drill down:
  - Which Critical/High services are non-compliant?
  - Are these acceptable risks or urgent gaps?
```

---

#### Quality Checks

**Before Using Dashboard for Reporting:**

- [ ] All formulas intact (no manual edits)
- [ ] Vendor count matches A.5.23.1 inventory
- [ ] All assessment areas show data (no #DIV/0! errors)
- [ ] Gap lists identify specific vendors (not just counts)
- [ ] Action items assigned to owners
- [ ] Dashboard last updated within 30 days

---

### Sheet 9: Evidence Register

#### Purpose Recap

**Goal:** Maintain complete inventory of all evidence supporting vendor assessments (audit trail).

**Why This Matters:**
- Auditors will ask: "Show me the evidence for this 'Compliant' status"
- Evidence must be retrievable within minutes (not days)
- Evidence Register creates traceability: Assessment → Evidence → Document
- Supports regulatory compliance documentation (GDPR, DORA, NIS2)

**Success Criterion:**
> Every "✅ Compliant" status in Sheets 2-7 has corresponding evidence in the Evidence Register with retrievable location.

#### Column-by-Column Guidance

**Column A: Evidence ID**

**Format:** EV-VDD-XXX (auto-generated sequence)

**How It Works:**
- Auto-increments: EV-VDD-001, EV-VDD-002, EV-VDD-003, etc.
- Formula: `="EV-VDD-" & TEXT(ROW()-6,"000")`
- User should NOT manually edit

**Purpose:**
- Unique identifier for each evidence item
- Referenced in Sheets 2-7, Column I (Evidence Location)
- Enables quick evidence lookup

**Column B: Evidence Type**

**Options (Dropdown):**
- `MSA` - Master Service Agreement
- `DPA` - Data Processing Agreement
- `SLA` - Service Level Agreement
- `ISO 27001 Certificate` - Security certification
- `SOC 2 Type II Report` - Audit report
- `FedRAMP Authorization` - US government authorization
- `Contract Amendment` - Changes to original contract
- `Vendor Questionnaire` - Security assessment questionnaire
- `SLA Performance Report` - Uptime/performance data
- `Subprocessor List` - DPA subprocessor disclosure
- `Audit Report` - Third-party audit findings
- `Certification Verification` - Issuing body confirmation
- `Jurisdictional Assessment` - CLOUD Act risk assessment
- `CMK Configuration` - Customer-managed key setup
- `EU Data Boundary Commitment` - Contractual commitment
- `Other` - Any other evidence type

**How to Complete:**
1. Select from dropdown based on document type
2. Use most specific type available
3. If unclear, use "Other" and describe in Document Title

**Evidence Type Usage by Sheet:**

| Sheet | Common Evidence Types |
|-------|----------------------|
| Sheet 2 (Certifications) | ISO 27001 Certificate, SOC 2 Type II Report, FedRAMP Authorization, Certification Verification |
| Sheet 3 (Contracts) | MSA, DPA, SLA, Contract Amendment, Subprocessor List |
| Sheet 4 (SLA Performance) | SLA, SLA Performance Report |
| Sheet 5 (Data Sovereignty) | DPA, Subprocessor List, EU Data Boundary Commitment |
| Sheet 6 (Audit Rights) | MSA (audit clause), SOC 2 Type II Report, Audit Report |
| Sheet 7 (Jurisdictional) | Jurisdictional Assessment, CMK Configuration, EU Data Boundary Commitment |

**Column C: Vendor Name**

**Format:** Vendor legal name (match Sheet 2-7, Column B)

**How to Complete:**
1. Copy vendor name exactly from assessment sheets
2. Maintain consistency (don't use abbreviations)
3. Example: "Amazon Web Services, Inc." (not "AWS")

**Why Consistency Matters:**
```
If inconsistent:
  Sheet 2: "AWS"
  Evidence Register: "Amazon Web Services, Inc."
  
Result: Evidence lookup by vendor name fails
```

**Column D: Cloud Service Name**

**Format:** Service name (match Sheet 2-7, Column A)

**How to Complete:**
1. List service(s) this evidence applies to
2. If evidence covers ALL vendor services (e.g., MSA), write "All Services"
3. If multiple specific services, comma-separate

**Examples:**
```
Single service: "Microsoft 365"
Multiple services: "EC2 Compute, S3 Storage, RDS Database"
All services: "All Services" (typical for MSA, DPA, certifications)
```

**Column E: Document Title**

**Format:** Descriptive title of evidence document

**How to Complete:**
1. Use descriptive, searchable title
2. Include date if document is versioned
3. Match filename where possible

**Good vs. Bad Titles:**

| ❌ Bad (Vague) | ✅ Good (Descriptive) |
|---------------|---------------------|
| "Contract" | "Master Service Agreement - Salesforce - Executed 2024-01-15" |
| "Certificate" | "ISO 27001 Certificate - AWS - IS 750968 - Valid 2024-2027" |
| "Report" | "SOC 2 Type II Report - Google Cloud - Exam Period Ended 2025-12-31" |
| "Document" | "Data Processing Agreement - Microsoft Azure - v3.2" |

**Column F: Document Date**

**Format:** DD.MM.YYYY

**How to Complete:**
1. For contracts: Effective date or signature date
2. For certificates: Issue date (not expiry date)
3. For reports: Examination period end date (SOC 2) or report date
4. For assessments: Assessment completion date

**Why This Matters:**
- Determines evidence currency (is it still valid?)
- Enables automated alerts (certificate expiring in 60 days)
- Audit trail (when was evidence obtained)

**Examples:**
```
MSA signed: 15.01.2024 → Entry: 15.01.2024
ISO 27001 cert issued: 30.09.2023, expires 30.09.2026 → Entry: 30.09.2023
SOC 2 exam period: 01.01.2025 - 31.12.2025 → Entry: 31.12.2025
```

**Column G: Storage Location**

**Format:** File path, URL, or system reference

**How to Complete:**
1. Provide EXACT location where evidence can be retrieved
2. Test link/path before saving (verify accessibility)
3. Use network paths for shared drives, URLs for cloud storage

**Location Format Examples:**

**Network Share:**
```
\\fileserver\Legal\Vendor-Contracts\AWS\MSA-AWS-2024-Executed.pdf
```

**SharePoint:**
```
https://company.sharepoint.com/sites/ISMS/Shared Documents/Evidence/Certifications/ISO27001-AWS-2024.pdf
```

**Contract Management System:**
```
ContractID: CNTR-2024-0042
(System: Agiloft Contract Management)
```

**Vendor Portal:**
```
https://aws.amazon.com/compliance/iso-27001-cert
(Login required: security@company.com)
```

**Google Drive:**
```
https://drive.google.com/file/d/[FILE_ID]/view
```

**Email:**
```
Email: security@company.com
Subject: "SOC 2 Type II Report - Vendor X"
Date: 15.01.2026
```

**Critical Requirements:**

- ✅ Location must be accessible to auditors (permissions granted)
- ✅ Location must be stable (not temporary links)
- ✅ Document retrieval time: <5 minutes
- ❌ Do NOT use personal drives (C:\Users\John\Desktop\...)
- ❌ Do NOT use temporary URLs (expire after 30 days)

**Column H: Collected By**

**Format:** Person name and role

**How to Complete:**
1. Name of person who obtained the evidence
2. Include role for context
3. Format: "FirstName LastName (Role)"

**Examples:**
```
"Jane Smith (Procurement Manager)"
"John Doe (Security Analyst)"
"Legal Team (Contract Review)"
"External Auditor (BSI Verification)"
```

**Why This Matters:**
- Enables follow-up questions about evidence
- Audit trail of who verified what
- Accountability for evidence quality

**Column I: Collection Date**

**Format:** DD.MM.YYYY

**How to Complete:**
1. Date evidence was obtained/verified
2. Not the document date (that's Column F)
3. This is when you collected it

**Example:**
```
ISO 27001 Certificate:
  - Issue Date (Column F): 30.09.2023
  - Collection Date (Column I): 15.01.2026
  (Certificate issued in 2023, but we obtained it in 2026)
```

**Why This Matters:**
- Shows evidence currency (when did we last verify?)
- If >1 year old, may need re-verification
- Audit trail of ongoing monitoring

**Column J: Evidence Status**

**Options (Dropdown):**
- `Current` - Evidence is valid and current
- `Expiring Soon` - Valid but expiring within 90 days
- `Expired` - No longer valid (certificate expired, contract ended)
- `Pending` - Requested from vendor but not yet received
- `Superseded` - Replaced by newer version

**How to Complete:**
1. For certificates: Check expiry date vs. today
   - Current: Expiry > 90 days away
   - Expiring Soon: Expiry within 90 days
   - Expired: Expiry date passed

2. For contracts: Check term end date
   - Current: Contract active
   - Expired: Contract terminated

3. For reports: Check age
   - Current: <12 months old (SOC 2)
   - Superseded: New report received

**Automated Status Updates:**
```
IF Certificate Expiry Date < TODAY: Status = "Expired"
IF Certificate Expiry Date < TODAY + 90 days: Status = "Expiring Soon"
ELSE: Status = "Current"
```

**Column K: Notes**

**Format:** Free text

**How to Complete:**
1. Document any special considerations
2. Note if evidence has limitations
3. Reference related evidence

**Examples:**
```
"Certificate scope covers EU regions only, not US deployments"

"SOC 2 report has qualified opinion - see management response on p.47"

"Contract under amendment - new version expected by 28.02.2026"

"Jurisdictional assessment performed by external legal counsel (see email dated 10.01.2026)"

"CMK configuration screenshots - verify quarterly for ongoing compliance"
```

#### Typical Evidence Register Entry

**Example: AWS ISO 27001 Certificate**

| Column | Value |
|--------|-------|
| A (Evidence ID) | EV-VDD-001 |
| B (Type) | ISO 27001 Certificate |
| C (Vendor) | Amazon Web Services, Inc. |
| D (Service) | All Services |
| E (Title) | ISO 27001 Certificate - AWS - IS 750968 - Valid 2024-2027 |
| F (Doc Date) | 30.09.2024 |
| G (Location) | \\fileserver\ISMS\Evidence\Certifications\ISO27001-AWS-2024-2027.pdf |
| H (Collected By) | John Doe (Security Analyst) |
| I (Collection Date) | 15.01.2026 |
| J (Status) | Current |
| K (Notes) | Verified with BSI on 15.01.2026 - certificate valid, scope covers all AWS services globally |

#### Evidence Register Maintenance

**Monthly Tasks:**
```
☐ Review "Expiring Soon" evidence
  - Contact vendors for renewal
  - Request updated certificates/reports
  - Update Evidence Register when received

☐ Archive "Superseded" evidence
  - Move to archive folder (retain for audit trail)
  - Update links to new evidence

☐ Follow up on "Pending" evidence
  - Re-send requests to vendors
  - Escalate if >30 days overdue
  - Document delays

☐ Verify "Current" status accurate
  - Spot-check random evidence items
  - Verify links still work
  - Test document retrieval time
```

**Quarterly Tasks:**
```
☐ Complete evidence audit
  - Verify all "✅ Compliant" statuses have evidence
  - Check for orphaned evidence (no longer needed)
  - Archive old/superseded evidence

☐ Test evidence retrieval
  - Select 10 random evidence items
  - Attempt to retrieve from storage location
  - Time retrieval (<5 minutes required)
  - Fix broken links
```

#### Common Mistakes

**Mistake 1: Generic Evidence Titles**

❌ **Wrong:**
```
Title: "Contract.pdf"
Problem: Which contract? Which vendor? Which year?
```

✅ **Right:**
```
Title: "Master Service Agreement - Salesforce - Executed 2024-01-15"
Anyone can understand what this is without opening it
```

**Mistake 2: Inaccessible Storage Locations**

❌ **Wrong:**
```
Location: "C:\Users\Jane\Documents\Contracts\AWS.pdf"
Problem: Only accessible from Jane's computer
```

✅ **Right:**
```
Location: "\\fileserver\Legal\Vendor-Contracts\AWS\MSA-AWS-2024.pdf"
Accessible to team members and auditors
```

**Mistake 3: Not Updating Evidence Status**

❌ **Wrong:**
```
ISO 27001 Certificate expired 30.09.2025
Evidence Register still shows: "Current"
Assessment Sheet 2 still shows: "✅ Compliant"
```

✅ **Right:**
```
Monthly review catches expiry:
  - Update Evidence Status: "Expired"
  - Update Sheet 2: "⚠️ Partial" (expired cert)
  - Request renewed certificate from vendor
  - Update when new cert received
```

#### Quality Checks

**Before Marking Evidence Register Complete:**

- [ ] Every "✅ Compliant" status in Sheets 2-7 has evidence entry
- [ ] All evidence locations tested (documents retrievable)
- [ ] No "Pending" evidence >30 days old (follow up)
- [ ] All "Expiring Soon" items have renewal plans
- [ ] Evidence collected within last 12 months (currency)
- [ ] Consistent vendor names across sheets

---

### Sheet 10: Approval Sign-Off

#### Purpose Recap

**Goal:** Obtain multi-stakeholder approval confirming assessment completeness, accuracy, and gap remediation plans.

**Why This Matters:**
- Approval creates accountability (each stakeholder owns their domain)
- Sign-off confirms assessment is audit-ready
- Documented approval trail for compliance verification
- Escalation mechanism for gaps requiring executive attention

**Success Criterion:**
> All four approvers (Legal, Procurement, DPO, CISO) have signed off, gaps have documented remediation plans, and assessment is marked "Complete and Approved."

#### Approval Workflow
```
Assessment Complete (Sheets 2-9 filled)
    ↓
Legal Review (contracts, audit rights)
    ↓
Procurement Review (vendor relationships, SLAs)
    ↓
Data Protection Officer Review (DPAs, cross-border transfers, jurisdictional risk)
    ↓
CISO Approval (overall risk posture, gap remediation)
    ↓
Assessment Status: APPROVED
```

#### Section-by-Section Guidance

**Section 1: Assessment Summary**

**This section auto-populates from Sheet 8 Dashboard:**

| Field | Formula/Source |
|-------|----------------|
| Total Vendors Assessed | `='8. Summary Dashboard'!B2` |
| Overall Compliance % | `='8. Summary Dashboard'!B3` |
| Non-Compliant Vendors | `='8. Summary Dashboard'!B4` |
| Critical/High Services from Compliant Vendors | `='8. Summary Dashboard'!B5` |
| Gaps Requiring Remediation | `='8. Summary Dashboard'!B6` |
| Jurisdictional Risks Identified | `='8. Summary Dashboard'!B20` |

**Purpose:**
- Provides approvers with quick assessment overview
- No manual entry required (read-only)
- Approvers see summary before detailed review

**Section 2: Legal Review**

**Fields:**

| Field | Type | Purpose |
|-------|------|---------|
| Reviewed By (Legal) | Text input | Legal counsel name |
| Review Date | Date input | When review completed |
| Contract Compliance | Dropdown | Compliant/Partially Compliant/Non-Compliant |
| DPA Adequacy | Dropdown | Adequate/Needs Amendment/Inadequate |
| Audit Rights Status | Dropdown | Adequate/Needs Improvement/Inadequate |
| Legal Comments | Text area | Specific concerns, required amendments |
| Legal Approval | Dropdown | Approved/Approved with Conditions/Rejected |

**How Legal Completes This:**
```
Step 1: Review Sheet 3 (Contract Terms)
  - Verify all DPAs reviewed
  - Check liability caps adequate
  - Review termination and data return clauses
  - Assess DORA/NIS2 compliance (if applicable)

Step 2: Review Sheet 6 (Audit Rights)
  - Verify audit clauses adequate for criticality
  - Check third-party report alternatives

Step 3: Document Findings
  - List vendors requiring contract amendments
  - Priority: Critical/High services first
  - Set amendment deadlines

Step 4: Approval Decision
  - Approved: All contracts adequate or minor gaps with plans
  - Approved with Conditions: Amendments required within X days
  - Rejected: Major gaps, assessment cannot proceed until fixed
```

**Example Legal Comments:**
```
"8 vendors require DPA amendments (see Sheet 3, rows 15, 22, 31, 38, 41, 45, 50, 52). 
Priority amendments for Critical services (rows 15, 31) to be completed by 28.02.2026.
Remaining amendments by 30.06.2026.

Vendor XYZ (row 38) has inadequate liability cap (CHF 100) for Critical service - 
requires urgent renegotiation or vendor replacement.

Status: Approved with Conditions (amendments in progress)"
```

**Section 3: Procurement Review**

**Fields:**

| Field | Type |
|-------|------|
| Reviewed By (Procurement) | Text input |
| Review Date | Date input |
| Vendor Relationship Status | Dropdown: Satisfactory/Needs Improvement/Unsatisfactory |
| Contract Renewals Tracked | Dropdown: Yes/Partially/No |
| SLA Performance Acceptable | Dropdown: Yes/Needs Escalation/Unacceptable |
| Procurement Comments | Text area |
| Procurement Approval | Dropdown: Approved/Approved with Conditions/Rejected |

**How Procurement Completes This:**
```
Step 1: Review Sheet 4 (SLA Performance)
  - Identify vendors with >3 SLA breaches
  - Check if service credits claimed
  - Verify vendor escalations for poor performance

Step 2: Review Contract Renewals (Sheet 3, Column X)
  - Confirm all auto-renewals tracked in contract management system
  - Verify renewal notifications set (90 days before)

Step 3: Document Actions
  - Vendors requiring performance escalation
  - Renewal deadlines in next 6 months
  - Unclaimed service credits

Step 4: Approval Decision
```

**Example Procurement Comments:**
```
"4 vendors require SLA performance escalation (AWS EC2, Vendor B, Vendor F, Vendor J).
Escalation meetings scheduled for week of 27.01.2026.

12 contracts renew in Q2 2026 - renewal evaluations to begin 01.03.2026.
All renewal dates tracked in Agiloft CMS with 90-day alerts.

Unclaimed service credits totaling CHF 8,500 identified - claims submitted 20.01.2026.

Status: Approved with Conditions (SLA escalations in progress)"
```

**Section 4: Data Protection Officer (DPO) Review**

**Fields:**

| Field | Type |
|-------|------|
| Reviewed By (DPO) | Text input |
| Review Date | Date input |
| Data Protection Compliance | Dropdown: Compliant/Partially Compliant/Non-Compliant |
| Cross-Border Transfer Status | Dropdown: Approved/Approved with SCCs/Requires TIA/Rejected |
| Jurisdictional Risk Acceptable | Dropdown: Yes/Acceptable with Controls/Unacceptable |
| DPO Comments | Text area |
| DPO Approval | Dropdown: Approved/Approved with Conditions/Rejected |

**How DPO Completes This:**
```
Step 1: Review Sheet 5 (Data Sovereignty)
  - Verify all DPAs adequate for GDPR/FADP
  - Check cross-border transfer mechanisms (SCCs, adequacy)
  - Confirm data residency compliance

Step 2: Review Sheet 7 (Jurisdictional Risk) - NEW
  - Assess CLOUD Act exposure for US vendors
  - Verify compensating controls (CMK, EU Data Boundary)
  - Evaluate if residual risk acceptable

Step 3: Transfer Impact Assessments
  - For US vendors with Confidential/Restricted data:
    - Verify TIA performed (Schrems II requirement)
    - Check supplementary measures adequate

Step 4: Approval Decision
  - Approved: Data protection compliant
  - Approved with Conditions: Controls needed (CMK, TIA, etc.)
  - Rejected: GDPR violations (no SCCs, inadequate DPA)
```

**Example DPO Comments:**
```
"5 US vendors processing Confidential data require Transfer Impact Assessment (TIA) 
per Schrems II (Sheet 7, rows 12, 18, 25, 33, 40). TIAs to be completed by 15.03.2026.

3 vendors have High jurisdictional risk with inadequate compensating controls:
  - Vendor A (row 12): Deploy CMK by 28.02.2026
  - Vendor B (row 18): Negotiate EU Data Boundary OR migrate to EU provider
  - Vendor C (row 25): Risk acceptance required from CISO (Confidential data exposure)

1 GDPR violation: Vendor D transferring to US without SCCs (Sheet 5, row 29) - 
URGENT contract amendment required by 31.01.2026 or suspend service.

Status: Approved with Conditions (TIAs and CMK deployment in progress, 
GDPR violation requires immediate remediation)"
```

**Section 5: CISO Approval**

**Fields:**

| Field | Type |
|-------|------|
| Reviewed By (CISO) | Text input |
| Review Date | Date input |
| Overall Security Posture | Dropdown: Acceptable/Acceptable with Gaps/Unacceptable |
| Risk Acceptance Required | Dropdown: Yes/No |
| Gap Remediation Plans Adequate | Dropdown: Yes/Partially/No |
| CISO Comments | Text area |
| CISO Final Approval | Dropdown: Approved/Approved with Conditions/Rejected |

**How CISO Completes This:**
```
Step 1: Review Sheet 8 (Summary Dashboard)
  - Overall compliance acceptable (target 85%+)?
  - Any Critical/High services from non-compliant vendors?
  - Jurisdictional risks acceptable?

Step 2: Review Legal/Procurement/DPO Comments
  - Are remediation plans realistic?
  - Are conditions acceptable?
  - Any P0 urgent items requiring immediate attention?

Step 3: Risk Acceptance Decisions
  - For High/Critical risks that cannot be remediated:
    - Vendor refuses to amend contract
    - Migration not feasible
    - Cost prohibitive
  - Formal risk acceptance required (document in risk register)

Step 4: Final Approval Decision
  - Approved: Assessment complete, audit-ready
  - Approved with Conditions: Specific actions required by deadlines
  - Rejected: Major gaps, assessment must be remediated before approval
```

**Example CISO Comments:**
```
"Overall vendor compliance at 87% - acceptable baseline.

Critical Issue: 2 Critical services from non-compliant vendors (Sheet 2, rows 15, 31):
  - Vendor XYZ (Critical CRM): No ISO 27001/SOC 2 - RISK ACCEPTANCE NOT GRANTED
    Action: Vendor must obtain ISO 27001 by 30.06.2026 OR we migrate to alternative
  - Vendor ABC (Critical backup): SOC 2 expired - renewal in progress (ETA 15.02.2026)
    Action: Acceptable if renewed by 28.02.2026, otherwise suspend service

Jurisdictional Risk: 3 High-risk vendors require CMK deployment (Sheet 7, rows 12, 18, 25).
Security team to deploy CMK by 28.02.2026. Progress review in weekly CISO meeting.

Approved with Conditions:
  1. Vendor XYZ ISO 27001 by 30.06.2026 (OR migration plan by 31.03.2026)
  2. Vendor ABC SOC 2 renewal by 28.02.2026
  3. CMK deployment for 3 vendors by 28.02.2026

Assessment re-review: 01.03.2026 (verify conditions met)
```

**Section 6: Assessment Status**

**Final Assessment Status (auto-calculated based on approvals):**
```
IF all approvals = "Approved" OR "Approved with Conditions":
  Status: "APPROVED - Audit Ready"
  
IF any approval = "Rejected":
  Status: "REJECTED - Remediation Required"
  
IF any approval = blank/pending:
  Status: "PENDING APPROVAL"
```

**Assessment Completion Date:** Date when CISO gives final approval

**Next Review Date:** Auto-calculated: Completion Date + 90 days (quarterly)

#### Common Mistakes

**Mistake 1: Rushing Through Approvals**

❌ **Wrong:**
```
All approvers sign off in 1 day without detailed review
No comments, no conditions, just "Approved"
Reality: Gaps exist but not identified
```

✅ **Right:**
```
Each approver takes 2-3 days for thorough review
Specific comments identifying gaps and remediation plans
Conditions documented with deadlines and owners
```

**Mistake 2: Approving With Unacceptable Gaps**

❌ **Wrong:**
```
DPO finds GDPR violation (no SCCs for US transfer)
DPO marks: "Approved with Conditions" 
Reality: GDPR violation is not "approvable" - requires immediate fix
```

✅ **Right:**
```
DPO finds GDPR violation
DPO marks: "REJECTED - URGENT remediation required"
Assessment cannot proceed until violation fixed
Re-submit for approval once remediated
```

**Mistake 3: No Follow-Up on Conditions**

❌ **Wrong:**
```
Approved with Conditions: "Deploy CMK by 28.02.2026"
28.02.2026 passes, no CMK deployed
No follow-up, condition ignored
```

✅ **Right:**
```
Approved with Conditions: "Deploy CMK by 28.02.2026"
Set calendar reminder: 21.02.2026 (1 week before deadline)
Track condition in separate tracking sheet
Escalate if deadline missed
Next quarterly review verifies condition met
```

#### Quality Checks

**Before Marking Sheet 10 Complete:**

- [ ] All four approval sections completed (Legal, Procurement, DPO, CISO)
- [ ] Each approver provided specific comments (not just "looks good")
- [ ] All conditions documented with deadlines and owners
- [ ] Risk acceptance decisions documented in risk register (if applicable)
- [ ] Assessment status reflects approval reality (not auto-approved)
- [ ] Next review date set (quarterly = 90 days from completion)

---

**END OF SECTION 4 PART 3: COMPLETING SHEETS 8-10**

## Section 5: Evidence Collection Guide

### Overview: The Evidence Collection Process

**Core Principle:**
> "In God we trust, all others bring data." - W. Edwards Deming

Every "✅ Compliant" status must be backed by objective, verifiable evidence. No vendor claims, no assumptions, no "trust us" - only documented proof.

**Evidence Hierarchy (from strongest to weakest):**

| Evidence Type | Strength | Example | Acceptability |
|---------------|----------|---------|---------------|
| **Official Documents** | Highest | ISO 27001 certificate from issuing body | ✅ Primary evidence |
| **Third-Party Reports** | High | SOC 2 Type II audit report | ✅ Primary evidence |
| **Executed Contracts** | High | Signed MSA/DPA with all parties | ✅ Primary evidence |
| **Vendor Documentation** | Medium | Technical white papers, data residency docs | ⚠️ Verify with contract/testing |
| **Vendor Portal Screenshots** | Medium-Low | Configuration screenshots with timestamps | ⚠️ Supplementary only |
| **Vendor Emails** | Low | Email claims about features/compliance | ⚠️ Confirm with formal documentation |
| **Vendor Verbal Claims** | Lowest | Sales calls, account manager statements | ❌ NOT acceptable evidence |

**Evidence Collection Timeline:**
```
Week 1: Mass Evidence Request
  → Send standardized evidence requests to all vendors
  → Track responses in Evidence Register

Week 2: Follow-Up and Verification
  → Follow up on non-responses
  → Begin verification (certificates with issuing bodies)
  → Download from vendor trust centers

Week 3: Gap Identification
  → Identify vendors with missing evidence
  → Escalate to procurement/legal for vendor engagement
  → Set deadlines for evidence provision

Week 4: Evidence Organization
  → File all evidence in repository
  → Update Evidence Register with locations
  → Link evidence to assessment sheets
```

---

### What Evidence to Collect

#### Evidence Requirements by Assessment Area

**Sheet 2: Vendor Security Certifications**

**For Each Vendor:**

| Evidence Item | Required For | Format | How to Obtain |
|---------------|--------------|--------|---------------|
| **ISO 27001 Certificate** | All Critical/High vendors | PDF | Vendor or issuing body website |
| **Certificate Verification** | All ISO 27001 claims | Screenshot/email | Issuing body verification portal |
| **SOC 2 Type II Report** | All Critical/High vendors (if no ISO 27001) | PDF (under NDA) | Direct vendor request |
| **FedRAMP Authorization** | US government workloads | PDF/URL | FedRAMP Marketplace |
| **Other Certifications** | Industry-specific (PCI, HIPAA, etc.) | PDF | Vendor compliance page |

**Critical Details to Capture:**

**ISO 27001 Certificate:**
```
Required Information:
✅ Certificate number
✅ Issue date and expiry date
✅ Issuing body (e.g., BSI, ANAB, TUV)
✅ Scope statement (which services/locations covered)
✅ Accreditation mark (proof issuing body is accredited)

Quality Check:
- Certificate is in color (not black & white photocopy)
- Contains issuing body logo and contact information
- Has security features (watermark, seal) if applicable
- Is NOT a screenshot from vendor website
```

**SOC 2 Type II Report:**
```
Required Information:
✅ Report type: Type II (NOT Type I)
✅ Examination period (start and end dates)
✅ Trust service criteria covered (Security, Availability, etc.)
✅ CPA firm name and signature
✅ Opinion type (unqualified = clean, qualified = concerns)
✅ Any exceptions or findings noted

Quality Check:
- Report is complete (50-100+ pages typical)
- Includes management assertion
- Contains independent auditor's report
- Has detailed test results (Type II)
- Dated within last 12 months
```

**Verification Record:**
```
For Each Certificate:
✅ Verification method (website, email, phone)
✅ Verification date
✅ Person who performed verification
✅ Verification result (screenshot, email confirmation)

Example:
"ISO 27001 Certificate IS 750968 verified with BSI on 15.01.2026 
via https://www.bsigroup.com/en-GB/validate-bsi-issued-certificates/
Screenshot saved: EV-VDD-002-Verification.png"
```

---

**Sheet 3: Contract Terms Analysis**

**For Each Vendor:**

| Evidence Item | Required For | Format | How to Obtain |
|---------------|--------------|--------|---------------|
| **Master Service Agreement (MSA)** | All vendors | PDF (executed) | Contract management system/Legal |
| **Data Processing Agreement (DPA)** | Vendors processing personal data | PDF (executed) | Contract management system/Legal |
| **Service Level Agreement (SLA)** | All vendors with uptime commitments | PDF | Contract management system/Vendor |
| **Contract Amendments** | Vendors with modified terms | PDF (executed) | Contract management system/Legal |
| **Subprocessor List** | Vendors with subprocessors | PDF/web page | DPA exhibit or vendor website |
| **DORA/NIS2 Addendum** | EU financial/essential entities | PDF | Contract management system |

**Critical Details to Capture:**

**Executed Contracts:**
```
Required Elements:
✅ Signature page with all parties' signatures
✅ Effective date (when contract became binding)
✅ All pages present (no missing sections)
✅ All exhibits/schedules/appendices included
✅ Version number (if contract has multiple versions)

Quality Check:
- Contract is "executed" (signed), not just a draft
- Signatures are present from both parties
- Dates are filled in (not "____________")
- Document is complete (all pages numbered and accounted for)
- If scanned, quality is readable (no blurry pages)
```

**Data Processing Agreement (DPA):**
```
Must Contain:
✅ Controller/Processor designation
✅ Processing purposes and data types
✅ Data retention period
✅ Subprocessor disclosure/approval mechanism
✅ Data subject rights support
✅ Security measures (reference to ISO 27001 or specific controls)
✅ Breach notification timeframe
✅ Cross-border transfer mechanism (SCCs if applicable)
✅ Data return/deletion upon termination
✅ Audit rights

Quality Check:
- DPA references current GDPR/FADP requirements
- SCCs (if present) are post-Schrems II version (2021+)
- Subprocessor list is specific (names & locations), not generic
- Breach notification ≤48 hours (reasonable timeframe)
```

**Subprocessor List:**
```
Required Information:
✅ Subprocessor legal name
✅ Service provided (e.g., "Cloud hosting", "Payment processing")
✅ Data processing location (country/region)
✅ Date of list (when was this current)

Example Format:
| Subprocessor | Service | Location | Added Date |
|--------------|---------|----------|------------|
| AWS Inc. | Cloud Hosting | Ireland (eu-west-1) | 2024-01-01 |
| Stripe | Payment Processing | US, EU | 2023-06-15 |

Quality Check:
- List is specific (not "various subprocessors may be used")
- Includes locations (not just company name)
- Has update date or version number
- Vendor commits to notify of changes (30+ days)
```

---

**Sheet 4: SLA Requirements & Performance**

**For Each Vendor:**

| Evidence Item | Required For | Format | How to Obtain |
|---------------|--------------|--------|---------------|
| **SLA Document** | All vendors | PDF | Contract or separate SLA agreement |
| **SLA Performance Reports** | All vendors | PDF/Excel/CSV | Vendor customer portal |
| **Incident Reports** | Vendors with SLA breaches | PDF/Email | Vendor notifications, ticketing system |
| **Service Credit Claims** | Vendors where credits claimed | Email/PDF | Correspondence with vendor |
| **Monitoring Data** | Critical/High services | Screenshots/Reports | Internal APM/monitoring tools |

**Critical Details to Capture:**

**SLA Performance Reports:**
```
Required Information:
✅ Reporting period (month/quarter/year)
✅ Uptime percentage achieved
✅ Incident count and duration
✅ Support ticket response times (by severity)
✅ Any SLA breaches and root causes
✅ Service credits issued (if applicable)

Data Sources (in order of preference):
1. Independent monitoring (Datadog, Pingdom, etc.) - MOST RELIABLE
2. Vendor SLA dashboard/portal - VERIFY INDEPENDENTLY
3. Vendor-provided reports - CROSS-CHECK WITH MONITORING

Quality Check:
- Data covers full 12-month period
- Granularity: Monthly preferred (not just annual average)
- Includes both committed SLA and actual performance
- Incident details available (not just percentages)
```

**SLA Breach Documentation:**
```
For Each Breach:
✅ Date and time of incident
✅ Duration of outage/degradation
✅ Services affected
✅ Root cause (vendor explanation)
✅ Remediation actions taken
✅ Service credit calculation (per SLA terms)

Example:
"March 2025 SLA Breach:
  Date: 15.03.2025, 02:30-06:15 UTC
  Duration: 3 hours 45 minutes
  Service: AWS EC2 (eu-central-1)
  Impact: Complete outage
  Uptime: 99.45% (below 99.9% SLA)
  Credit: 10% monthly fee = CHF 1,000
  Claim: Submitted 20.03.2025, approved 25.03.2025
  Evidence: AWS incident report (EV-VDD-125), credit confirmation email (EV-VDD-126)"
```

---

**Sheet 5: Data Sovereignty & Jurisdiction**

**For Each Vendor:**

| Evidence Item | Required For | Format | How to Obtain |
|---------------|--------------|--------|---------------|
| **Data Residency Documentation** | All vendors processing personal data | PDF/web page | Contract clause or vendor documentation |
| **Data Center Location List** | All vendors | PDF | Vendor trust center/compliance page |
| **DPA with SCCs** | Cross-border transfers | PDF | Contract management system |
| **Transfer Impact Assessment (TIA)** | US vendors with EU data | PDF/Word | DPO or external legal counsel |
| **CMK Configuration** | US vendors with CMK | Screenshots | Vendor console/portal |
| **EU Data Boundary Commitment** | US vendors | PDF | Contract addendum or vendor documentation |

**Critical Details to Capture:**

**Data Residency Commitment:**
```
Required Information:
✅ Geographic region(s) where data stored (country, city if available)
✅ Geographic region(s) where data processed
✅ DR/backup locations (if different from primary)
✅ Commitment type (contractual, technical, both)
✅ Customer control (can customer select/lock region?)

Evidence Sources:
1. Contract clause: "Customer Data shall be stored exclusively in [REGION]"
2. Vendor technical documentation: Data residency architecture
3. Vendor portal: Region selection screenshot
4. Vendor compliance page: Data center location list

Quality Check:
- Specificity: "EU (Frankfurt)" better than "Europe"
- Contractual enforceability: "shall" better than "may"
- No weasel words: Avoid "generally", "typically", "usually"
```

**Standard Contractual Clauses (SCCs):**
```
Verification Checklist:
☐ SCCs are post-Schrems II version (2021 or later)
☐ Correct module used:
   - Module 2: Controller-to-Processor (MOST COMMON for cloud)
   - Module 1: Controller-to-Controller
   - Module 3: Processor-to-Processor
☐ Annexes completed:
   - Annex I: Parties and processing details
   - Annex II: Technical and organizational measures
   - Annex III: Subprocessors (if applicable)
☐ Supplementary measures documented (if CLOUD Act risk)

Red Flags:
❌ SCCs dated 2010 or earlier (old version, invalidated)
❌ SCCs annexed but not executed (no signatures on SCCs themselves)
❌ Generic SCCs without specifics filled in
```

**Transfer Impact Assessment (TIA):**
```
Post-Schrems II Requirement:
When transferring EU personal data to US (or other non-adequate country),
SCCs alone are insufficient. A TIA must assess if local laws (like CLOUD Act)
conflict with GDPR protections.

TIA Should Include:
✅ Assessment of destination country laws (e.g., CLOUD Act in US)
✅ Likelihood of government access to data
✅ Supplementary measures to mitigate risk:
   - Technical: Encryption, CMK, data minimization
   - Contractual: Transparency commitments, legal challenge clauses
   - Organizational: Access controls, audit rights
✅ Conclusion: Transfer is adequate with supplementary measures OR not adequate

Evidence:
- TIA document prepared by DPO or external legal counsel
- Date: Should be current (within 12 months)
- Vendor-specific: Not generic template without customization
```

**Customer-Managed Key (CMK) Configuration:**
```
Evidence Required:
✅ Screenshot of CMK enabled in vendor portal
✅ Key ID or ARN (unique identifier)
✅ Key policy showing customer control (not vendor)
✅ Services using CMK (compute, storage, database, etc.)
✅ Backup encryption using CMK (not just primary data)

Example Evidence Set:
1. AWS KMS: Screenshot showing customer-managed key with alias "MyOrg-Production-Key"
2. Key policy: JSON export showing customer as key administrator
3. S3 bucket: Screenshot showing SSE-KMS encryption with customer key
4. RDS database: Screenshot showing encryption with customer-managed key

Quality Check:
- CMK is actually configured (not just "available")
- All critical services use CMK (not just some)
- Backups also encrypted with CMK
- Customer can revoke keys (test in non-prod if possible)
```

---

**Sheet 6: Forensics & Audit Rights**

**For Each Vendor:**

| Evidence Item | Required For | Format | How to Obtain |
|---------------|--------------|--------|---------------|
| **Audit Rights Clause** | Critical/High vendors | PDF | Extract from MSA/SLA |
| **SOC 2 Type II Report** | Alternative to direct audit | PDF | Vendor (under NDA) |
| **Audit Schedule** | Planned audits | Email/calendar | Internal planning |
| **Forensic Investigation Procedure** | All vendors | PDF | Vendor documentation or contract |
| **Log Retention Policy** | All vendors | PDF/web page | Vendor technical documentation |

**Critical Details to Capture:**

**Audit Rights Clause:**
```
Extract from Contract:
Section/Article: [e.g., "Section 8.5: Audit Rights"]
Full Text: [copy verbatim clause]

Key Elements to Highlight:
✅ Frequency allowed (e.g., "annual" or "upon cause")
✅ Notice period required (e.g., "30 days written notice")
✅ Scope (systems, processes, facilities, personnel)
✅ Cost allocation (who pays for audit)
✅ Auditor selection (customer's choice or mutual agreement)
✅ Report delivery timeline

Example:
"Customer may conduct security audits of Vendor's facilities and systems
annually upon 30 days written notice, and immediately in case of security
incident. Vendor shall provide reasonable cooperation and access to systems,
documentation, and personnel. Customer may use third-party auditors subject
to confidentiality obligations. Audit costs borne by Customer for scheduled
audits, by Vendor for cause-based audits."

Evidence: MSA Section 8.5, page 23
```

**SOC 2 Type II Report (as Audit Alternative):**
```
When accepting SOC 2 in lieu of direct audit:

Verification Checklist:
☐ Report is Type II (operating effectiveness tested)
☐ Examination period ≤12 months old
☐ Report scope covers services in use
☐ Opinion is unqualified (clean opinion)
☐ No significant exceptions or findings in testing
☐ CPA firm is reputable (Big 4 or recognized regional firm)

If Report Has Findings:
- Review management response
- Verify remediation completed
- Assess if findings impact our use case
- May require supplementary controls

Evidence:
- Complete SOC 2 report (all pages)
- NDA with vendor (required for SOC 2 access)
- Review notes documenting findings assessment
```

**Log Retention Documentation:**
```
Required Information:
✅ Log types covered (authentication, access, changes, security events)
✅ Retention period (e.g., "12 months")
✅ Log accessibility (can customer access logs?)
✅ Log format (syslog, JSON, proprietary)
✅ Log immutability (tamper-proof storage)

Evidence Sources:
1. Contract clause specifying log retention
2. Vendor security documentation
3. Vendor trust center (compliance page)

Example:
"Vendor Security Documentation - Logging & Monitoring:
  - Authentication logs: 24 months retention
  - Access logs: 12 months retention
  - Configuration change logs: 36 months retention
  - Security event logs: 24 months retention
  - Customer access: Available via SIEM integration or API
  - Storage: Immutable S3 with versioning enabled"

Evidence: Vendor security white paper (EV-VDD-145), page 15
```

---

**Sheet 7: Jurisdictional Risk Assessment**

**For Each US-Nexus Vendor:**

| Evidence Item | Required For | Format | How to Obtain |
|---------------|--------------|--------|---------------|
| **Corporate Structure Documentation** | All vendors | Web page/filing | Vendor website, business registry |
| **Jurisdictional Risk Assessment** | US-nexus vendors | PDF/Word | DPO or external legal counsel |
| **CMK Configuration Evidence** | US vendors with CMK mitigation | Screenshots | Vendor portal (see Sheet 5) |
| **EU Data Boundary Commitment** | US vendors | PDF | Contract clause or vendor documentation |
| **CLOUD Act White Paper** | US vendors (if available) | PDF | Vendor trust center |
| **Risk Acceptance Form** | High/Critical risks accepted | PDF | Internal risk management |

**Critical Details to Capture:**

**Corporate Structure:**
```
Required Information:
✅ Vendor legal entity name
✅ Headquarters country (legal registration)
✅ Parent company (if subsidiary)
✅ Ultimate parent company country
✅ Ownership structure (public, private, who owns)

Evidence Sources:
1. Vendor "About Us" page
2. Contract signature page (legal entity name)
3. LinkedIn company page
4. Business registry (Companies House, Secretary of State, etc.)
5. Annual reports / SEC filings (public companies)

Example:
"Salesforce Ireland Limited
  - Legal Entity: Ireland registered company (CRO #478764)
  - Headquarters: Ireland (Dublin)
  - Parent Company: Salesforce.com Inc. (United States)
  - Ultimate Parent: Salesforce.com Inc. (US public company, NYSE: CRM)
  - Conclusion: US NEXUS via parent company
  
Evidence: 
  - Contract signature page (EV-VDD-170)
  - Salesforce.com 10-K filing (EV-VDD-171)
  - Irish Companies Registration Office search (EV-VDD-172)"
```

**Jurisdictional Risk Assessment:**
```
DPO/Legal Assessment Document:

Required Sections:
✅ Vendor identification (name, HQ, parent company)
✅ US nexus determination (Yes/No, basis)
✅ Data involved (classification, volume, types)
✅ CLOUD Act applicability analysis
✅ Compensating controls evaluation:
   - Customer-managed keys (deployed/not deployed)
   - EU Data Boundary (contractual commitment/none)
   - Data minimization (implemented/not implemented)
   - Other controls
✅ Residual risk assessment (Low/Medium/High/Critical)
✅ Recommendation (Accept/Mitigate/Migrate)
✅ Approval (CISO/DPO signature)

Example Assessment:
"Jurisdictional Risk Assessment: Amazon Web Services (AWS)
  
Vendor: Amazon Web Services, Inc. (US company)
US Nexus: YES - headquartered in United States
Data: Confidential customer data, ~500GB
CLOUD Act Applicable: YES
  
Compensating Controls:
  ✅ Customer-Managed Keys (AWS KMS) - Deployed 15.01.2026
  ✅ EU Data Boundary - Contractual commitment (MSA Addendum 2024-12)
  ✅ Data region locked to eu-central-1 (Frankfurt)
  ✅ AWS transparency commitment - will notify of legal demands
  
Residual Risk: MEDIUM
Recommendation: ACCEPT with continued monitoring
  
Approval:
  DPO: Jane Smith, 20.01.2026
  CISO: John Doe, 20.01.2026
  
Evidence: EV-VDD-180"
```

**EU Data Boundary Commitment:**
```
Required Information:
✅ Contractual clause or vendor documentation
✅ Scope (which services covered)
✅ Operational details (how enforced)
✅ Transparency commitment (notification of conflicts)

Evidence Example:
"AWS EU Data Boundary Addendum (2024-12-15):
  
Clause 3.2: 'For Customer workloads designated as EU Data Boundary,
AWS commits to:
  (a) Store and process Customer Data exclusively within EU AWS Regions
  (b) Restrict administrative access to EU-based AWS personnel only
  (c) Maintain metadata within EU boundaries
  (d) Notify Customer within 72 hours of any legal demand conflicting 
      with EU data residency
  (e) Challenge any such demand and seek Customer consent before compliance'
  
Services Covered: EC2, S3, RDS, Lambda (all compute and storage)
Effective Date: 01.01.2025
Customer Configuration: Account flagged as 'EU Data Boundary' on 15.01.2026

Evidence: 
  - Contract addendum (EV-VDD-185)
  - AWS console screenshot showing EU Boundary enabled (EV-VDD-186)"
```

---

### How to Collect Evidence

#### Method 1: Direct Vendor Request

**When to Use:**
- Initial evidence collection (Week 1)
- Vendor has evidence but not publicly available
- Requires NDA or customer login (SOC 2 reports)

**Email Template:**
```
Subject: Compliance Documentation Request - [Service Name] - Q1 2026 Assessment

Dear [Vendor Account Manager],

[Organization] is conducting our quarterly vendor security assessment per 
ISO 27001:2022 requirements. Please provide the following documentation for 
[Service Name]:

SECURITY CERTIFICATIONS:
☐ Current ISO 27001 certificate (PDF)
☐ Most recent SOC 2 Type II report (last 12 months)
☐ FedRAMP authorization (if applicable)
☐ Other applicable certifications (PCI-DSS, HIPAA, etc.)

CONTRACTS & COMPLIANCE:
☐ Executed Master Service Agreement (MSA)
☐ Data Processing Agreement (DPA)
☐ Service Level Agreement (SLA)
☐ Current subprocessor list
☐ Any contract amendments since [Last Request Date]

DATA RESIDENCY & SOVEREIGNTY:
☐ Data center location documentation
☐ Data residency architecture diagram
☐ Cross-border data transfer documentation
☐ EU Data Boundary commitment (if applicable)

SLA & PERFORMANCE:
☐ SLA performance reports (last 12 months)
☐ Any incident reports or root cause analyses (if SLA breaches)

AUDIT & FORENSICS:
☐ Log retention policy
☐ Incident response plan summary
☐ Forensic investigation capabilities documentation

Please provide documents by [Date + 14 days]. If any documents require 
NDA or customer portal access, please provide instructions.

Internal Reference: ISMS-A.5.23.2 Vendor Assessment Q1 2026
Contact: [Your Name, Title, Email, Phone]

Thank you for your cooperation.

Best regards,
[Name]
[Title]
[Organization]
```

**Follow-Up Schedule:**
- Day 0: Send initial request
- Day 7: First follow-up (gentle reminder)
- Day 14: Second follow-up (escalate to account manager)
- Day 21: Escalate to Procurement (vendor non-responsive)

#### Method 2: Vendor Trust Centers & Compliance Pages

**When to Use:**
- Publicly available certifications
- Standard compliance documentation
- Initial research before formal request

**Major Vendor Trust Centers:**
```
AWS:
  - Compliance: https://aws.amazon.com/compliance/
  - Certifications: https://aws.amazon.com/compliance/iso-certified/
  - Services in Scope: https://aws.amazon.com/compliance/services-in-scope/

Microsoft Azure:
  - Trust Center: https://www.microsoft.com/en-us/trust-center
  - Compliance: https://learn.microsoft.com/en-us/compliance/
  - Audit Reports: https://servicetrust.microsoft.com/

Google Cloud:
  - Compliance: https://cloud.google.com/security/compliance
  - Certifications: https://cloud.google.com/security/compliance/offerings

Salesforce:
  - Trust: https://trust.salesforce.com/
  - Compliance: https://compliance.salesforce.com/

How to Use:
1. Visit vendor trust center
2. Navigate to certifications/compliance section
3. Download available certificates/reports
4. Save with descriptive filename: "ISO27001-AWS-2024-2027.pdf"
5. Note download date in Evidence Register
6. Still verify certificates with issuing bodies (don't just trust website)
```

#### Method 3: Third-Party Verification Services

**When to Use:**
- Verifying certificate authenticity
- Large-scale certificate verification
- Automated monitoring of certificate expiry

**Verification Services:**

**ISO 27001 Certificates:**
```
BSI (British Standards Institution):
  - URL: https://www.bsigroup.com/en-GB/validate-bsi-issued-certificates/
  - Input: Certificate number
  - Result: Valid/Invalid, expiry date

ANAB (ANSI National Accreditation Board):
  - URL: https://www.anab.org/
  - Contact: Direct inquiry (no online verification portal)

TUV, UKAS, and other accreditation bodies:
  - Most have online verification portals
  - Search: "[Issuing Body] certificate verification"
```

**FedRAMP:**
```
FedRAMP Marketplace:
  - URL: https://marketplace.fedramp.gov/
  - Search by: Cloud Service Provider or Cloud Service Offering
  - Verify: Authorization status, level (High/Moderate/Low), agency sponsor
```

**CSA STAR:**
```
CSA STAR Registry:
  - URL: https://cloudsecurityalliance.org/star/registry/
  - Search by: Provider name
  - Verify: STAR level (Self-Assessment/Certification/Attestation/Continuous)
```

#### Method 4: Contract Management System Extraction

**When to Use:**
- Retrieving executed contracts
- Pulling renewal dates and key terms
- Generating contract reports

**Typical CMS Workflow:**
```
Step 1: Query Contract Repository
  Filters:
    - Vendor Type: Cloud Services, SaaS, IaaS, PaaS
    - Status: Active, Pending Renewal
    - Contract Type: MSA, DPA, SLA

Step 2: Bulk Export
  - Export all contracts as PDFs
  - Export metadata to Excel (dates, values, owners)
  
Step 3: Organize by Vendor
  - Create vendor-specific folders
  - Group: MSA + DPA + SLA + Amendments
  
Step 4: Extract Key Clauses
  - Data Protection/DPA sections
  - Audit Rights sections
  - Liability and Indemnification
  - Termination and Data Return
  - Save as separate PDFs or annotated originals
```

#### Method 5: Vendor Portal Access

**When to Use:**
- Accessing SLA performance dashboards
- Downloading service health reports
- Verifying configuration (data residency, CMK, etc.)

**Portal Access Checklist:**
```
For Each Major Vendor:
☐ Request admin or billing access (needed for compliance docs)
☐ Enable MFA for portal security
☐ Document login credentials in password manager
☐ Set up access for Security team (not just Procurement)

What to Download from Portal:
☐ SLA/uptime reports (monthly, last 12 months)
☐ Service health dashboards (screenshot current status)
☐ Configuration settings (data region, encryption, access controls)
☐ Compliance documentation (certificates, audit reports if available)
☐ Subprocessor lists (often in trust center within portal)
```

---

### Evidence Storage & Organization

#### Folder Structure

**Recommended Repository Structure:**
```
/ISMS-Vendor-Due-Diligence-Evidence/
│
├── /Certifications/
│   ├── /ISO27001/
│   │   ├── Vendor-A-ISO27001-Cert-2024-2027.pdf
│   │   ├── Vendor-A-ISO27001-Verification-BSI-2024.pdf
│   │   └── Vendor-B-ISO27001-Cert-2023-2026.pdf
│   ├── /SOC2/
│   │   ├── Vendor-C-SOC2-TypeII-ExamEnded-2025-12-31.pdf
│   │   └── Vendor-D-SOC2-TypeII-ExamEnded-2025-06-30.pdf
│   └── /FedRAMP/
│       └── Vendor-E-FedRAMP-High-Authorization-2024.pdf
│
├── /Contracts/
│   ├── /Vendor-A/
│   │   ├── MSA-Vendor-A-Executed-2024-01-15.pdf
│   │   ├── DPA-Vendor-A-Executed-2024-01-15.pdf
│   │   ├── SLA-Vendor-A-2024.pdf
│   │   ├── Amendment-1-Vendor-A-2025-06-01.pdf
│   │   └── Subprocessor-List-Vendor-A-2025-01.pdf
│   ├── /Vendor-B/
│   │   └── ...
│   └── /Vendor-C/
│       └── ...
│
├── /SLA-Reports/
│   ├── /Vendor-A/
│   │   ├── SLA-Report-2025-01.pdf
│   │   ├── SLA-Report-2025-02.pdf
│   │   └── ...
│   └── /Vendor-B/
│       └── ...
│
├── /Data-Sovereignty/
│   ├── Vendor-A-Data-Residency-Documentation-2025.pdf
│   ├── Vendor-B-EU-Data-Boundary-Commitment-2024.pdf
│   ├── Vendor-C-CMK-Configuration-Screenshots-2026-01.pdf
│   └── Vendor-D-TIA-CLOUD-Act-Assessment-2025.pdf
│
├── /Audit-Rights/
│   ├── Vendor-A-Audit-Rights-Clause-Extracted.pdf
│   ├── Vendor-B-SOC2-TypeII-2025.pdf
│   └── Vendor-C-Log-Retention-Policy.pdf
│
└── /Jurisdictional-Risk/
    ├── Vendor-A-Corporate-Structure-Research-2026.pdf
    ├── Vendor-B-Jurisdictional-Risk-Assessment-2026-01.pdf
    ├── Vendor-C-CLOUD-Act-White-Paper.pdf
    └── Risk-Acceptance-Form-Vendor-D-2026-01.pdf
```

#### File Naming Convention

**Standard Format:**
```
[Evidence-Type]-[Vendor-Name]-[Specific-Details]-[Date/Version].[ext]

Examples:
✅ ISO27001-AWS-Cert-IS750968-2024-2027.pdf
✅ MSA-Salesforce-Executed-2024-01-15.pdf
✅ SOC2-TypeII-Google-ExamEnded-2025-12-31.pdf
✅ DPA-Microsoft-Azure-v3.2-2025.pdf
✅ SLA-Report-Zendesk-2025-Q4.pdf
✅ CMK-Config-AWS-Screenshot-2026-01-20.png
✅ Jurisdictional-Assessment-Salesforce-2026-01.pdf

❌ Avoid:
  contract.pdf (too generic)
  aws.pdf (what about AWS?)
  document (1).pdf (meaningless)
  FINAL-VERSION-2.pdf (ambiguous)
```

#### Version Control

**For Documents That Change:**
```
Approach 1: Date-Based Versions
  MSA-Vendor-A-2024-01-15.pdf (original)
  MSA-Vendor-A-2025-06-01.pdf (amended)
  
Approach 2: Version Numbers
  DPA-Vendor-B-v1.0-2024.pdf
  DPA-Vendor-B-v2.0-2025.pdf
  DPA-Vendor-B-v2.1-2025.pdf (minor amendment)

Approach 3: Archive Superseded
  /Current/
    MSA-Vendor-A-2025-06-01.pdf
  /Archive/
    MSA-Vendor-A-2024-01-15.pdf

Best Practice: Use date-based for contracts (execution date is key)
              Use version numbers for internal assessments/policies
```

#### Access Control

**Who Needs Access:**

| Role | Read | Write | Delete | Purpose |
|------|------|-------|--------|---------|
| Assessment Coordinator | ✅ | ✅ | ⚠️ | Manage evidence collection |
| Legal | ✅ | ✅ | ❌ | Add contracts, review DPAs |
| Security | ✅ | ✅ | ❌ | Add certifications, technical docs |
| Procurement | ✅ | ✅ | ❌ | Add vendor documentation |
| Compliance/DPO | ✅ | ⚠️ | ❌ | Review, limited additions |
| Auditors (External) | ✅ | ❌ | ❌ | Read-only for audit |
| IT Operations | ✅ | ❌ | ❌ | Reference only |

**Access Control Mechanisms:**
```
SharePoint/OneDrive:
  - Create security group: "ISMS-Vendor-Evidence-Contributors"
  - Assign permissions: Read/Write to contributors, Read-only to others
  - Enable version history (restore if accidental deletion)
  
Network Share:
  - NTFS permissions: Modify for contributors, Read for others
  - Enable shadow copies (file recovery)
  
Contract Management System:
  - Role-based access (Legal = full, others = read-only)
  - Audit trail (who accessed what, when)
```

---

### Evidence Quality Checks

**Before Accepting Evidence as Valid:**

#### Quality Check 1: Document Completeness
```
☐ All pages present (check page numbers)
☐ No missing exhibits/schedules (contract references "Exhibit A" - is it attached?)
☐ Signatures present (for executed contracts)
☐ Dates filled in (no blank "___________")
☐ Readable quality (no blurry scans)
☐ Correct document (matches what was requested)
```

#### Quality Check 2: Currency
```
☐ Certificate not expired (expiry date > today)
☐ SOC 2 report ≤12 months old (examination end date)
☐ Contract is current (not superseded)
☐ Subprocessor list dated within 6 months
☐ SLA report covers recent period (last quarter/year)
```

#### Quality Check 3: Authenticity
```
☐ Certificate from official source (issuing body letterhead, logo)
☐ SOC 2 from recognized CPA firm (not vendor internal audit)
☐ Contract is executed (signed by authorized parties)
☐ Evidence matches vendor website claim (cross-verify)
☐ Verification completed (certificate numbers checked with issuing bodies)
```

#### Quality Check 4: Relevance
```
☐ Certificate scope covers services in use
☐ SOC 2 report scope includes relevant systems
☐ Contract applies to services being assessed
☐ DPA covers personal data types we process
☐ SLA report for services we actually use
```

#### Quality Check 5: Adequacy
```
☐ ISO 27001: Current, from accredited body, scope appropriate
☐ SOC 2: Type II (not Type I), unqualified opinion, recent
☐ DPA: GDPR-compliant, includes SCCs if needed, specific not generic
☐ SLA: Specific percentages (not "best efforts"), penalty mechanism
☐ Audit rights: Allows verification (not just vendor self-reporting)
```

---

### Handling Missing Evidence

**When Evidence Cannot Be Obtained:**

#### Scenario 1: Vendor Refuses to Provide

**Example:** Vendor refuses to share SOC 2 report (claims proprietary)

**Actions:**
```
Step 1: Escalate to Vendor Account Manager
  "Our ISO 27001 compliance requires vendor security verification.
   SOC 2 Type II reports are standard for vendor assessments.
   Can we sign NDA to obtain access?"

Step 2: Escalate to Procurement
  "Vendor refusing standard compliance documentation.
   This may violate our procurement policies.
   Can Procurement engage vendor executive sponsor?"

Step 3: Risk Assessment
  "If vendor continues refusal:
    - Service Criticality: Critical/High → Cannot accept
    - Service Criticality: Medium/Low → Risk acceptance with conditions
    - Alternative: Vendor must obtain ISO 27001 (more transparent)"

Step 4: Document Decision
  "Gap: No SOC 2 report available (vendor refused)
   Compensating Control: Vendor has current ISO 27001
   Risk: Medium (no detailed testing evidence)
   Acceptance: CISO approved 2026-01-20 (Risk ID: RISK-2026-088)
   Next Review: 2026-Q2 (re-request SOC 2 or require ISO 27001 renewal)"
```

#### Scenario 2: Evidence Does Not Exist

**Example:** Small vendor has no ISO 27001 or SOC 2 certification

**Actions:**
```
Step 1: Assess Service Criticality
  Critical/High: ISO 27001 or SOC 2 is REQUIRED (no exceptions)
    → Vendor must obtain certification OR we migrate to certified vendor
  
  Medium/Low: May accept alternative evidence
    → Vendor security questionnaire (completed by vendor CISO)
    → Independent penetration test (annual)
    → Customer-conducted audit (if audit rights exist)

Step 2: Set Certification Timeline
  "Vendor X (Medium criticality service) does not have ISO 27001.
   
   Option 1: Vendor obtains ISO 27001 within 12 months
     - Vendor commits to certification by 2027-01-01
     - Interim: Annual pen test + security questionnaire
     - Review quarterly for progress
   
   Option 2: Accept risk with compensating controls
     - Service downgraded to Low criticality (limit data exposure)
     - Data classification: Public only (no Confidential/Restricted)
     - Additional monitoring (enhanced logging, alerting)
     - Annual review for recertification requirement
   
   Option 3: Migrate to certified vendor
     - Identify alternative with ISO 27001
     - Migration plan by Q3 2026"

Step 3: Document in Gap Register
  "Gap: No security certification (ISO 27001, SOC 2)
   Service: Project Management Tool (Medium criticality)
   Remediation: Vendor to obtain ISO 27001 by 2027-01-01
   Interim Controls: 
     - Annual pen test (next: 2026-06-01)
     - Security questionnaire (completed: 2026-01-15)
     - Data limited to Internal classification
   Owner: Procurement
   Status: In Progress"
```

#### Scenario 3: Evidence Expired / Outdated

**Example:** ISO 27001 certificate expired 6 months ago

**Actions:**
```
Immediate: Change vendor status to ❌ Non-Compliant
  Assessment Sheet 2, Column H: "❌ Non-Compliant"
  Gap: "ISO 27001 expired 2025-08-30, renewal overdue"

Urgent Vendor Engagement:
  "Your ISO 27001 certificate expired on 30.08.2025.
   
   Please provide by 31.01.2026:
     - Renewed ISO 27001 certificate OR
     - Surveillance audit confirmation (if mid-cycle) OR
     - Recertification timeline (if audit scheduled)
   
   If certification not renewed by 28.02.2026:
     - Risk escalation to CISO
     - Service suspension consideration (Critical/High services)
     - Vendor replacement evaluation"

If Vendor Renewal In Progress:
  "Vendor confirms recertification audit scheduled for 15.02.2026.
   
   Interim Status: ⚠️ Partial (renewal in progress)
   Condition: Certificate must be renewed by 28.02.2026
   Fallback: If not renewed, service suspended until certification obtained
   
   Evidence: Email from vendor confirming audit date (EV-VDD-XXX)"
```

#### Scenario 4: Evidence Incomplete

**Example:** SOC 2 report missing management response section

**Actions:**
```
Request Complete Report:
  "The SOC 2 Type II report provided is incomplete (missing pages 45-52:
   Management Response to Findings).
   
   Please provide complete report including all sections."

If Vendor Provides Explanation:
  "Vendor explains: Management response pages removed due to sensitive
   internal remediation details.
   
   Assessment:
     - Review report findings without management response
     - Assess if findings impact our use case
     - Request summary: Have findings been remediated? (Yes/No/In Progress)"

Document Limitation:
  "Evidence: SOC 2 Type II (partial - management response redacted)
   Limitation: Cannot verify vendor remediation of identified issues
   Compensating Control: Vendor provided separate attestation letter
     confirming all findings remediated as of 2025-12-31
   Status: ⚠️ Partial (complete report preferred)"
```

---

### Evidence Collection Checklist

**Weekly Evidence Collection Progress:**
```
Week 1 - Mass Evidence Request:
☐ Evidence request emails sent to all vendors
☐ Tracking spreadsheet created (vendor, request date, status)
☐ Auto-reminders set for Day 7 and Day 14

Week 2 - Download & Verification:
☐ Evidence downloaded from vendor trust centers
☐ Certificates verified with issuing bodies
☐ Evidence Register updated with all received items
☐ First follow-ups sent (vendors with no response)

Week 3 - Gap Identification:
☐ Vendors without evidence identified
☐ Escalation to Procurement for non-responsive vendors
☐ Gap remediation plans documented
☐ Second follow-ups sent

Week 4 - Organization & Documentation:
☐ All evidence filed in repository
☐ Evidence Register 100% populated
☐ Links tested (all evidence retrievable)
☐ Quality checks completed
☐ Evidence summary report for CISO
```

**Final Evidence Quality Scorecard:**
```
Evidence Quality Metrics:

Total Vendors: _____ 
Vendors with Complete Evidence: _____ ( _____ %)
Vendors with Partial Evidence: _____ ( _____ %)
Vendors with Missing Evidence: _____ ( _____ %)

Evidence Currency:
  Evidence <6 months old: _____ ( _____ %)
  Evidence 6-12 months old: _____ ( _____ %)
  Evidence >12 months old: _____ ( _____ %)

Evidence Verification:
  Certificates verified with issuing bodies: _____ ( _____ %)
  SOC 2 reports reviewed for completeness: _____ ( _____ %)
  Contracts verified as executed: _____ ( _____ %)

Target: 90%+ complete evidence, 80%+ verified

Status: ☐ Pass  ☐ Needs Improvement  ☐ Fail
```

---

**END OF SECTION 5: EVIDENCE COLLECTION GUIDE**

## Section 6: Common Pitfalls & How to Avoid Them

### Overview: Learning from Others' Mistakes

**Core Principle:**
> "Experience is a hard teacher because she gives the test first, the lesson afterward." - Vernon Law

This section identifies the most common mistakes organizations make when conducting vendor due diligence assessments, and provides practical guidance on avoiding them.

**Categories of Pitfalls:**

1. **Process Pitfalls** - How the assessment is conducted
2. **Evidence Pitfalls** - What evidence is accepted and verified
3. **Contract Analysis Pitfalls** - How contracts are reviewed
4. **Data Sovereignty Pitfalls** - Assumptions about data location
5. **Jurisdictional Risk Pitfalls** - Misunderstanding CLOUD Act and legal risks
6. **Approval Workflow Pitfalls** - Rubber-stamping and lack of follow-through
7. **Maintenance Pitfalls** - One-time assessment mentality

---

### Category 1: Process Pitfalls

#### Pitfall 1.1: Rushing Through the Assessment

**The Mistake:**
```
❌ Wrong Approach:
  "We need this done by Friday for the audit next week."
  
  Result:
    - Vendor claims accepted without verification
    - Evidence not collected or reviewed superficially
    - Gaps missed or documented inadequately
    - Assessment fails audit scrutiny
```

**Why This Happens:**
- Last-minute audit preparation (poor planning)
- Underestimating time required (40-80 hours for initial assessment)
- Pressure from management to "just get it done"
- Treating assessment as checkbox exercise

**How to Avoid:**
```
✅ Right Approach:
  Plan Assessment Timeline:
    - Initial assessment: 4-6 weeks minimum
    - Quarterly updates: 2-3 weeks
    - Start 2 months before audit deadline (buffer for gaps)
  
  Set Realistic Expectations:
    - Week 1: Evidence collection requests sent
    - Week 2-3: Vendor response time (they need time too)
    - Week 3-4: Verification and gap analysis
    - Week 5: Remediation planning
    - Week 6: Approvals and finalization
  
  Communicate Timeline:
    - Inform stakeholders of realistic duration
    - Explain why rushing compromises quality
    - Get executive buy-in for proper timeline
```

**Red Flags You're Rushing:**
- Marking vendors "✅ Compliant" without evidence
- Skipping certificate verification ("vendor website says ISO 27001 is enough")
- Not reading contracts ("Legal probably reviewed this already")
- Accepting first response without follow-up questions

#### Pitfall 1.2: One Person Trying to Do Everything

**The Mistake:**
```
❌ Wrong Approach:
  Security analyst attempts to:
    - Review all contracts (Legal's expertise)
    - Interpret DPAs and GDPR compliance (DPO's expertise)
    - Assess SLA adequacy (Procurement's expertise)
    - Evaluate financial liability (Finance/Legal expertise)
    - Make jurisdictional risk decisions (Legal + DPO expertise)
  
  Result:
    - Errors in interpretation
    - Missed nuances in contracts
    - Inadequate risk assessment
    - No stakeholder buy-in
```

**Why This Happens:**
- "No one else has time to help"
- Lack of understanding of cross-functional nature
- Fear of bothering other departments
- Organization silos (teams don't collaborate)

**How to Avoid:**
```
✅ Right Approach:
  Establish Assessment Team (from Section 1):
    - Coordinator: Security or Procurement (owns process)
    - Legal: Contract review, audit rights, jurisdictional risk
    - Procurement: Vendor relationships, SLA performance
    - DPO: Data protection, cross-border transfers, CLOUD Act
    - Security: Certifications, technical controls, CMK verification
    - Finance: Liability assessment, SLA penalty validation
  
  Divide and Conquer:
    - Each expert owns their domain (Sheets 2-7)
    - Coordinator integrates and ensures consistency
    - Weekly sync meetings (30 min) to align
  
  Get Executive Sponsorship:
    - CISO or CIO sponsors assessment
    - Ensures other teams prioritize participation
    - Removes organizational barriers
```

**How to Identify This Pitfall:**
- One person's name in all "Completed By" fields
- Assessment completed in 1-2 days (impossible for 40+ vendors)
- Generic comments ("contracts look OK") without specific analysis

#### Pitfall 1.3: Not Using the A.5.23.1 Inventory

**The Mistake:**
```
❌ Wrong Approach:
  "I'll just assess the vendors I know about."
  
  Result:
    - Shadow IT vendors missed (services used without IT approval)
    - Department-specific cloud services overlooked
    - Incomplete vendor coverage
    - Audit finding: "Vendor assessment doesn't cover all services"
```

**Why This Happens:**
- A.5.23.1 not completed yet (starting in wrong order)
- Assuming IT knows all cloud services (they don't)
- Not involving business units in discovery

**How to Avoid:**
```
✅ Right Approach:
  Prerequisites Check (Section 2):
    ✓ A.5.23.1 Cloud Service Inventory MUST be complete first
    ✓ Verify inventory includes shadow IT (expense report analysis, CASB)
    ✓ Cross-reference: Every vendor in A.5.23.1 appears in A.5.23.2
  
  Vendor Discovery Methods:
    1. Start with A.5.23.1 inventory (authoritative source)
    2. Cross-check with contract management system
    3. Review credit card statements (shadow IT detection)
    4. Interview department heads ("What cloud services does your team use?")
    5. CASB logs (if available - shows actual cloud usage)
  
  Validation:
    - Count vendors in A.5.23.2 = count vendors in A.5.23.1
    - If mismatch, investigate why
```

#### Pitfall 1.4: Treating All Vendors the Same

**The Mistake:**
```
❌ Wrong Approach:
  Same depth of assessment for:
    - AWS (Critical infrastructure, Restricted data, $100K/month)
    - Free email newsletter tool (Public data, $0/month)
  
  Result:
    - Time wasted on low-risk vendors
    - Insufficient depth on high-risk vendors
    - Resources exhausted before Critical vendors fully assessed
```

**Why This Happens:**
- "We need to be consistent and fair"
- Not understanding risk-based approach
- Treating compliance as checkbox (every box same importance)

**How to Avoid:**
```
✅ Right Approach:
  Risk-Based Assessment Depth:
  
  Critical Services (from A.5.23.1):
    ✓ Full assessment (all 10 sheets)
    ✓ Certificate verification with issuing bodies
    ✓ Contract line-by-line review (Legal)
    ✓ Transfer Impact Assessment (if US vendor)
    ✓ Audit rights exercised or SOC 2 required
    ✓ Quarterly reviews
  
  High Services:
    ✓ Full assessment
    ✓ Certificate verification
    ✓ Contract key sections review
    ✓ Jurisdictional risk assessment
    ✓ Semi-annual reviews
  
  Medium Services:
    ✓ Standard assessment
    ✓ Certificate existence check (may not verify)
    ✓ Contract spot-check
    ✓ Annual reviews
  
  Low Services:
    ✓ Minimal assessment (certifications optional)
    ✓ Basic contract review (terms reasonable?)
    ✓ As-needed reviews (or when service upgraded)
  
  Time Allocation Example:
    - 1 Critical vendor: 6-8 hours assessment time
    - 1 High vendor: 3-4 hours
    - 1 Medium vendor: 1-2 hours
    - 1 Low vendor: 30 minutes
```

---

### Category 2: Evidence Pitfalls

#### Pitfall 2.1: Accepting Vendor Claims Without Verification

**The Mistake:**
```
❌ Wrong Approach:
  Vendor website: "ISO 27001 Certified ✓"
  Assessor: Marks Sheet 2 as "✅ Compliant" without requesting certificate
  
  Reality:
    - Certificate expired 2 years ago (website not updated)
    - Certificate from unaccredited body (worthless)
    - Certificate scope doesn't include cloud services
    - Vendor never had ISO 27001 (fraudulent claim)
```

**Why This Happens:**
- Trusting vendor at face value
- Not wanting to "bother" vendor for proof
- Assuming vendor wouldn't lie
- Time pressure (verification takes effort)

**How to Avoid:**
```
✅ Right Approach:
  ALWAYS Verify Certifications:
  
  Step 1: Request Official Certificate
    - PDF from issuing body or vendor compliance portal
    - NOT screenshot from vendor website
  
  Step 2: Verify Certificate Details
    - Certificate number: [ISO27001-XXXXX]
    - Issuing body: [BSI, ANAB, TUV, etc.]
    - Issue date: [DD.MM.YYYY]
    - Expiry date: [DD.MM.YYYY] - must be future
    - Scope: Read scope statement - covers our services?
  
  Step 3: Independent Verification
    - Visit issuing body website (e.g., BSI certificate checker)
    - Enter certificate number
    - Confirm: Valid, current, matches vendor claim
    - Screenshot verification result
  
  Step 4: Evidence Register
    - Save certificate PDF: EV-VDD-XXX
    - Save verification screenshot: EV-VDD-XXX-Verification
    - Document verification date and method
  
  Only THEN mark as "✅ Compliant"
```

**Verification Resources:**
- BSI: https://www.bsigroup.com/en-GB/validate-bsi-issued-certificates/
- FedRAMP: https://marketplace.fedramp.gov/
- CSA STAR: https://cloudsecurityalliance.org/star/registry/

#### Pitfall 2.2: Not Reading SOC 2 Reports

**The Mistake:**
```
❌ Wrong Approach:
  Vendor provides 150-page SOC 2 Type II report
  Assessor: "We got the SOC 2, mark as compliant"
  
  Reality (if actually read):
    - Report is Type I (design only, no testing) ❌
    - Examination period ended 18 months ago (outdated) ❌
    - Opinion is qualified (auditor found significant issues) ❌
    - 15 control deficiencies noted affecting our use case ❌
```

**Why This Happens:**
- SOC 2 reports are long and technical (100+ pages)
- "Having SOC 2" is treated as pass/fail (it's not that simple)
- Not understanding difference between Type I and Type II
- Not knowing how to read audit reports

**How to Avoid:**
```
✅ Right Approach:
  SOC 2 Report Review Checklist:
  
  ☐ Report Type: Type II (NOT Type I)
     - Type I = design only (weak)
     - Type II = operating effectiveness tested (required)
  
  ☐ Examination Period:
     - End date ≤12 months ago
     - Longer period = better (6-12 month period typical)
  
  ☐ Trust Service Criteria Covered:
     - Security (always included)
     - Availability (for SaaS/critical services)
     - Confidentiality (if processing confidential data)
     - Processing Integrity (for data processing services)
     - Privacy (if processing personal data)
  
  ☐ Opinion Type:
     - Unqualified = Clean (vendor controls effective)
     - Qualified = Issues (auditor has concerns)
     - If qualified: Read why, assess if impacts us
  
  ☐ Test Results Section:
     - Review control tests performed
     - Note any exceptions or deviations
     - For exceptions: Read management response
     - Assess: Has issue been remediated since report?
  
  ☐ Scope:
     - Does report cover services we use?
     - Does it cover data centers we're deployed in?
  
  Key Pages to Read:
    - Page 1-5: Report type, period, opinion
    - Management Assertion: What vendor claims
    - Independent Auditor's Report: Auditor's opinion
    - Section IV: Test Results and Exceptions
    - User Entity Controls: Our responsibilities
```

**If You Find Issues:**
```
Qualified Opinion or Exceptions Found:
  1. Document specific findings
  2. Request vendor management response (if not in report)
  3. Verify remediation status
  4. Assess impact on our use case
  5. May require:
     - Compensating controls (our side)
     - Vendor remediation timeline
     - Risk acceptance (CISO)
     - Alternative vendor consideration
```

#### Pitfall 2.3: Accepting Screenshots as Evidence

**The Mistake:**
```
❌ Wrong Approach:
  Vendor sends screenshot: "See, we have ISO 27001!"
  Assessor: Saves screenshot as evidence
  
  Problem:
    - Screenshots easily forged (Photoshop)
    - No way to verify authenticity
    - Auditors will reject screenshot evidence
```

**Why This Happens:**
- Quick and convenient for vendor to send
- Looks official (has logo, certificate number)
- Assessor doesn't know better

**How to Avoid:**
```
✅ Right Approach:
  Acceptable Evidence Formats:
  
  ✅ Official PDF from issuing body
     - Contains digital signature (if applicable)
     - Watermarks, security features
     - Can be verified independently
  
  ✅ Direct download from vendor compliance portal
     - Logged-in access (shows it's real)
     - Document download link
     - Portal URL verifiable
  
  ✅ Third-party verification service
     - FedRAMP Marketplace entry
     - CSA STAR Registry listing
     - Issuing body verification portal
  
  ⚠️ Screenshot acceptable ONLY for:
     - Vendor portal configurations (CMK enabled, region locked)
     - Must include: URL, timestamp, username visible
     - Supplementary evidence (not primary)
  
  ❌ NEVER accept:
     - Screenshot of certificate (request PDF)
     - Cropped/edited images
     - Photos of printed certificates
     - Vendor "trust us" emails without attachments
```

#### Pitfall 2.4: Not Maintaining Evidence Currency

**The Mistake:**
```
❌ Wrong Approach:
  January 2025: ISO 27001 verified, marked compliant
  January 2026: Assessment updated, still marked compliant
  
  Reality:
    - Certificate expired September 2025 (6 months ago)
    - Vendor assessment shows "✅ Compliant" (wrong)
    - Auditor finds expired certificate → compliance failure
```

**Why This Happens:**
- Evidence collected once, never refreshed
- No tracking of certificate expiry dates
- Quarterly updates don't re-verify certifications
- Evidence Register not reviewed regularly

**How to Avoid:**
```
✅ Right Approach:
  Evidence Lifecycle Management:
  
  Certificate Expiry Tracking:
    - Extract expiry dates from all certificates
    - Set calendar reminders:
      * Expiry - 90 days: Notify vendor to start renewal
      * Expiry - 60 days: Request renewal timeline
      * Expiry - 30 days: Escalate to CISO if not renewed
      * Expiry date: Change status to ❌ Non-Compliant
  
  Quarterly Evidence Review:
    - Re-verify Critical/High vendor certifications (all)
    - Spot-check Medium vendors (sample 20%)
    - Review Evidence Register status column:
      * "Expiring Soon" → Follow up
      * "Expired" → Update assessment status
      * "Current" → Verify still accurate
  
  Annual Complete Re-Verification:
    - Request fresh certificates from ALL vendors
    - Verify ALL certificates with issuing bodies
    - Update Evidence Register completely
  
  Automation Where Possible:
    - Some CMS platforms track contract renewals (auto-alert)
    - Certificate monitoring services (third-party)
    - Internal scripts to check expiry dates weekly
```

---

### Category 3: Contract Analysis Pitfalls

#### Pitfall 3.1: Accepting Generic "Reasonable Care" Language

**The Mistake:**
```
❌ Wrong Approach:
  DPA states: "Vendor will use reasonable care to protect data"
  Assessor: "Sounds good, mark as adequate"
  
  Problem:
    - "Reasonable care" is undefined (vendor interpretation)
    - No specific security controls committed
    - No objective standard to measure compliance
    - Not GDPR-compliant (requires specific measures)
```

**Why This Happens:**
- Legal language sounds official and adequate
- Don't know what "adequate" DPA looks like
- Vendor resists specific commitments
- Legal team not reviewing

**How to Avoid:**
```
✅ Right Approach:
  DPA Must Specify Controls:
  
  Inadequate: "Reasonable care to protect data"
  
  Adequate: "Vendor shall implement the following security measures:
    (a) Encryption at rest (AES-256) and in transit (TLS 1.2+)
    (b) Access controls (role-based, principle of least privilege)
    (c) Multi-factor authentication for administrative access
    (d) Logging and monitoring (SIEM integration)
    (e) Vulnerability management (monthly scans, patch SLA)
    (f) Incident detection and response (24/7 SOC)
    (g) ISO 27001 certified controls OR equivalent
    (h) Annual third-party security assessment (SOC 2 Type II)"
  
  Alternative: Reference to Standard
    "Vendor shall maintain controls consistent with ISO/IEC 27001:2022
     Annex A, as evidenced by current ISO 27001 certification."
  
  Negotiation Strategy:
    - Start: Request specific controls (list above)
    - Vendor pushes back: Suggest ISO 27001 reference
    - Vendor still resists: "Reasonable care + annual SOC 2 Type II"
    - Minimum acceptable: ISO 27001/SOC 2 requirement in DPA
```

#### Pitfall 3.2: Ignoring Subprocessor Clauses

**The Mistake:**
```
❌ Wrong Approach:
  DPA states: "Vendor may use subprocessors at its discretion"
  Assessor: "OK, vendor needs flexibility"
  
  GDPR Violation:
    - Article 28: Processor needs prior authorization for subprocessors
    - No list = no awareness of data processing chain
    - No notification = surprise data transfers
    - No objection right = no control
```

**Why This Happens:**
- GDPR Article 28 requirements not understood
- "Standard vendor terms" accepted without challenge
- Don't realize subprocessors create compliance risk

**How to Avoid:**
```
✅ Right Approach:
  GDPR-Compliant Subprocessor Clause:
  
  Required Elements:
    1. Current subprocessor list (names + locations)
    2. Notification mechanism (new subprocessors)
    3. Advance notice period (minimum 30 days)
    4. Objection right (customer can refuse)
    5. Alternative if objection (vendor finds alternative OR allows termination)
  
  Example Clause:
    "Vendor shall provide Customer with current list of subprocessors
     (Exhibit B). Vendor shall notify Customer at least 30 days before
     engaging new subprocessors. Customer may object to new subprocessor
     on reasonable grounds. If Customer objects, Vendor shall either:
     (a) not engage that subprocessor, or
     (b) allow Customer to terminate without penalty."
  
  Exhibit B - Subprocessor List (MUST include):
    | Subprocessor | Service | Location | Added Date |
    |--------------|---------|----------|------------|
    | AWS Inc. | Infrastructure | Ireland | 2024-01-01 |
    | Zendesk | Support | US, EU | 2023-06-15 |
  
  Red Flags in Contracts:
    ❌ "Vendor may use subprocessors as needed"
    ❌ No subprocessor list
    ❌ "Vendor will update list on website" (no notification)
    ❌ No customer objection right
```

#### Pitfall 3.3: Not Understanding Liability Cap Implications

**The Mistake:**
```
❌ Wrong Approach:
  Critical CRM service (Confidential customer data, $50K/month)
  Contract: "Liability limited to CHF 100"
  Assessor: "At least there's a liability clause"
  
  Reality of Data Breach:
    - Regulatory fine: CHF 500,000 (FADP/GDPR)
    - Notification costs: CHF 50,000
    - Credit monitoring: CHF 100,000
    - Legal fees: CHF 75,000
    - Reputation damage: Immeasurable
    
    Vendor liability: CHF 100 (0.01% of actual costs)
    Organization bears: 99.99% of costs
```

**Why This Happens:**
- Not thinking through breach scenarios
- "Some cap is better than no cap"
- Procurement focuses on price, not liability
- Legal review doesn't consider data criticality

**How to Avoid:**
```
✅ Right Approach:
  Assess Liability Cap Adequacy:
  
  Step 1: Calculate Potential Breach Impact
    - Regulatory fines (GDPR: €20M or 4% revenue)
    - Notification costs (per-affected-person)
    - Customer impact (refunds, credits)
    - Legal and forensic costs
    - Reputation/business loss
  
  Step 2: Compare Cap to Service Value & Risk
    Service Criticality | Data Classification | Minimum Cap
    Critical            | Restricted         | CHF 10M or 24 months fees
    Critical            | Confidential       | CHF 5M or 12 months fees
    High                | Confidential       | CHF 2M or 12 months fees
    Medium              | Internal           | CHF 500K or 6 months fees
  
  Step 3: Negotiate or Accept Risk
    If Vendor Refuses Adequate Cap:
      Option 1: Cyber Insurance (cover the gap)
      Option 2: Reduce data exposure (lower classification)
      Option 3: Choose different vendor (higher cap)
      Option 4: Risk acceptance (CISO + CFO sign-off)
  
  Step 4: Exception Carve-Outs
    Even if general cap low, negotiate exceptions:
      - Data breaches: Uncapped OR higher cap
      - Gross negligence / willful misconduct: Uncapped
      - IP infringement: Uncapped
      - Regulatory fines: Vendor indemnifies
  
  Example Negotiated Structure:
    General Liability: CHF 1M or 12 months fees (whichever greater)
    
    Exceptions (uncapped):
      - Data breaches caused by vendor security failure
      - Violation of data protection laws (GDPR/FADP)
      - Gross negligence or willful misconduct
      - Intellectual property infringement
```

---

### Category 4: Data Sovereignty Pitfalls

#### Pitfall 4.1: Trusting Vendor Region Selection Without Verification

**The Mistake:**
```
❌ Wrong Approach:
  Vendor portal shows: "Region: EU-Central-1 (Frankfurt)"
  Assessor: "Data is in EU, mark compliant"
  
  Reality Check:
    - Primary data: EU (Frankfurt) ✓
    - Control plane: US (Virginia) ❌
    - Logs/metadata: US (Oregon) ❌
    - Backups: Replicated to US for DR ❌
    - Support team access: India, US, everywhere ❌
```

**Why This Happens:**
- Assuming "region selection" means ALL data stays there
- Not understanding cloud architecture (data plane vs. control plane)
- Vendor doesn't disclose full data flows
- Not reading technical documentation thoroughly

**How to Avoid:**
```
✅ Right Approach:
  Comprehensive Data Location Verification:
  
  Ask Vendor These Questions:
    1. Where is PRIMARY data stored? (answer: EU Frankfurt)
    2. Where is BACKUP data stored? (may be different)
    3. Where are LOGS stored? (often centralized in US)
    4. Where is METADATA stored? (account info, usage stats)
    5. Where is the CONTROL PLANE? (management, billing)
    6. Where are SUPPORT teams located? (can they access data?)
    7. Are there ANY data flows outside EU? (monitoring, analytics)
  
  Review Technical Architecture:
    - Request data flow diagram
    - Identify ALL data processing locations
    - Check vendor documentation (not just marketing)
  
  Contractual Commitment:
    "Customer Data shall be stored and processed exclusively within the
     European Union. No Customer Data (including metadata, logs, and backups)
     shall be transferred outside the EU without prior written consent."
  
  Technical Validation:
    - For critical services: Network monitoring
    - Check DNS lookups (what endpoints are contacted)
    - Review vendor API calls (do they go to US endpoints?)
```

#### Pitfall 4.2: Assuming EU Data Center = GDPR Compliant

**The Mistake:**
```
❌ Wrong Approach:
  US vendor (Salesforce, AWS, etc.)
  Data stored in EU (Ireland, Frankfurt)
  Assessor: "EU data = GDPR compliant"
  
  Missing Schrems II Analysis:
    - Data in EU ✓
    - BUT: US company subject to CLOUD Act
    - BUT: Provider-managed encryption keys
    - BUT: US government can compel access
    - Result: Schrems II requires Transfer Impact Assessment
```

**Why This Happens:**
- Misunderstanding GDPR (location ≠ compliance)
- Not aware of Schrems II ruling (2020)
- Thinking "EU data center" solves everything
- Not understanding CLOUD Act extraterritorial reach

**How to Avoid:**
```
✅ Right Approach:
  Full GDPR Compliance Assessment:
  
  Data Location: Just ONE factor, not the only factor
  
  GDPR Article 28 Checklist:
    ☐ DPA in place (processor obligations)
    ☐ Processing purposes limited
    ☐ Data retention defined
    ☐ Security measures specified
    ☐ Subprocessor list and approval
    ☐ Data subject rights support
    ☐ Breach notification (≤48 hours)
    ☐ Audit rights or SOC 2 alternative
  
  Cross-Border Transfer Analysis (if US vendor):
    ☐ Identify if ANY data leaves EU (logs, backups, support)
    ☐ If yes: Standard Contractual Clauses (SCCs) required
    ☐ SCCs must be post-Schrems II (2021 version)
    ☐ Transfer Impact Assessment (TIA) required:
       - Assess CLOUD Act risk
       - Evaluate supplementary measures (CMK, EU Boundary)
       - Document residual risk
    ☐ DPO approval of TIA
  
  Location + Legal Framework:
    Data in EU + US vendor = CLOUD Act exposure → TIA required
    Data in EU + EU vendor = No CLOUD Act → TIA not needed (usually)
```

---

### Category 5: Jurisdictional Risk Pitfalls

#### Pitfall 5.1: Thinking Customer-Managed Keys (CMK) Eliminate CLOUD Act Risk

**The Mistake:**
```
❌ Wrong Approach:
  "We deployed CMK, so CLOUD Act doesn't apply"
  
  Reality:
    CMK mitigates but does NOT eliminate risk:
      - Vendor cannot decrypt data ✓
      - BUT: Metadata still accessible ❌
      - BUT: Customer could be compelled to provide keys ❌
      - BUT: Backups may not use CMK ❌
      - BUT: Legal jurisdiction unchanged ❌
```

**Why This Happens:**
- Vendor marketing oversells CMK as "complete protection"
- Technical control (CMK) confused with legal protection
- Not understanding what CMK actually protects

**How to Avoid:**
```
✅ Right Approach:
  Realistic CMK Assessment:
  
  What CMK DOES Protect:
    ✓ Data at rest (encrypted with your keys)
    ✓ Vendor cannot decrypt without your keys
    ✓ CLOUD Act warrant to vendor yields encrypted data (useless)
  
  What CMK DOES NOT Protect:
    ❌ Metadata (who accessed, when, file names)
    ❌ Logs (unless also encrypted with CMK)
    ❌ Network traffic analysis (patterns visible)
    ❌ Legal requirement to provide keys (rare but possible)
  
  Correct Risk Rating:
    Provider-Managed Keys + US Vendor + Confidential Data = HIGH RISK
    CMK + US Vendor + Confidential Data = MEDIUM RISK (mitigated, not eliminated)
    CMK + EU Boundary + US Vendor = LOW-MEDIUM RISK (strong mitigation)
    EU Vendor + EU Data = LOW RISK (no CLOUD Act)
  
  Document Residual Risk:
    "CMK deployed, significantly mitigating CLOUD Act risk.
     Residual risk: Metadata potentially accessible.
     Compensating control: Data minimization (no PII in filenames/metadata).
     Risk Rating: MEDIUM (was HIGH before CMK)"
```

#### Pitfall 5.2: Not Considering Parent Company Jurisdiction

**The Mistake:**
```
❌ Wrong Approach:
  Vendor: "Salesforce Ireland Limited" (Irish company)
  Assessor: "Ireland = EU, no CLOUD Act risk"
  
  Missing:
    - Parent company: Salesforce.com Inc. (US)
    - US parent subject to CLOUD Act
    - Can compel subsidiary to provide data
    - Result: CLOUD Act applies despite Irish subsidiary
```

**Why This Happens:**
- Focusing on legal entity on contract (Salesforce Ireland)
- Not researching corporate ownership structure
- Vendor doesn't volunteer parent company info

**How to Avoid:**
```
✅ Right Approach:
  Corporate Structure Research:
  
  For EVERY Vendor:
    1. Identify legal entity (from contract signature page)
    2. Research parent company:
       - Check vendor website "About Us"
       - LinkedIn company page
       - Business registries (Companies House, etc.)
       - SEC filings (if US public company)
    3. Identify ultimate parent headquarters
  
  Example Research:
    Legal Entity: "Salesforce Ireland Limited"
    
    Research Results:
      - Registered: Ireland (CRO #478764)
      - Parent: Salesforce.com Inc.
      - Parent HQ: United States (California)
      - Stock: NYSE: CRM (US public company)
      - Conclusion: US NEXUS via parent → CLOUD Act applies
  
  Document in Sheet 7:
    Provider HQ Jurisdiction: Ireland
    US Nexus: Yes - US Parent (Salesforce.com Inc.)
    CLOUD Act Exposure: Potential (unmitigated) or Mitigated (if CMK)
```

---

### Category 6: Approval Workflow Pitfalls

#### Pitfall 6.1: Rubber-Stamping Approvals

**The Mistake:**
```
❌ Wrong Approach:
  Legal receives assessment: "Please approve by EOD"
  Legal: Glances at summary, sees 87% compliance
  Legal: "Approved" (without reading gaps or comments)
  
  Missed:
    - 2 Critical services without DPAs (GDPR violation)
    - 5 vendors with inadequate liability caps
    - 8 contracts missing DORA clauses (regulatory requirement)
```

**Why This Happens:**
- Time pressure to complete assessment
- Approvers too busy to review thoroughly
- Assuming coordinator did the work properly
- "Approval" treated as formality, not validation

**How to Avoid:**
```
✅ Right Approach:
  Meaningful Approval Process:
  
  1. Provide Approvers Adequate Time:
     - Legal: 3-5 business days minimum
     - Procurement: 2-3 business days
     - DPO: 3-5 business days (complex analysis)
     - CISO: 2-3 business days (after other approvals)
  
  2. Provide Focused Summaries:
     - Overall compliance: 87%
     - Critical gaps (require immediate attention):
       * 2 vendors without DPAs → URGENT amendment needed
       * 5 vendors inadequate liability caps → Renegotiate or risk acceptance
       * 8 vendors missing DORA clauses → Amendment required if applicable
     - What approver needs to decide:
       * Are gaps acceptable with documented remediation plans?
       * Are timelines realistic?
       * Are resources allocated to fix gaps?
  
  3. Require Specific Comments:
     Don't allow: "Approved"
     Require: "Approved with conditions: [List specific requirements]"
     Or: "Rejected: [Specific gaps that must be fixed]"
  
  4. Track Conditions:
     If "Approved with Conditions":
       - Document each condition with deadline
       - Assign owner for each condition
       - Follow up at next review (verify conditions met)
```

#### Pitfall 6.2: No Follow-Up on "Approved with Conditions"

**The Mistake:**
```
❌ Wrong Approach:
  January 2026: "Approved with conditions: Deploy CMK by 28.02.2026"
  March 2026: No one checked if CMK was deployed
  June 2026: Quarterly review, still no CMK
  Result: Condition ignored, risk remains
```

**Why This Happens:**
- Approval is treated as "end" not "beginning"
- No tracking system for conditions
- Coordinator moves on to other priorities
- Assumes responsible party will self-report completion

**How to Avoid:**
```
✅ Right Approach:
  Conditions Tracking Register:
  
  Create Separate Sheet/Tracker:
    | Condition | Owner | Deadline | Status | Evidence | Notes |
    |-----------|-------|----------|--------|----------|-------|
    | Deploy CMK for AWS | Security | 28.02.2026 | In Progress | - | 50% complete |
    | Amend Vendor X DPA | Legal | 31.03.2026 | Pending | - | Sent to vendor |
  
  Set Reminders:
    - Deadline - 2 weeks: Check with owner on progress
    - Deadline - 1 week: Escalate if not on track
    - Deadline: Mark as Met or Overdue
    - Overdue: Escalate to CISO (condition not met)
  
  Monthly Condition Review:
    - Standing agenda item in ISMO steering meeting
    - Review all open conditions
    - Update status
    - Escalate blockers
  
  Next Assessment Review:
    - Verify ALL conditions from last review were met
    - If not met: Explain why, extend deadline, or escalate
    - Do not approve new assessment if old conditions unfulfilled
```

---

### Category 7: Maintenance Pitfalls

#### Pitfall 7.1: One-Time Assessment Mentality

**The Mistake:**
```
❌ Wrong Approach:
  Complete assessment in January 2026 for audit
  Put it on shelf, never update
  January 2027: Pull out year-old assessment for next audit
  
  What Changed in 12 Months:
    - 8 new vendors added (not assessed)
    - 4 vendors decommissioned (waste in assessment)
    - 12 contracts renewed (new terms not reviewed)
    - 6 certificates expired (vendors now non-compliant)
    - 3 vendors acquired by US companies (new CLOUD Act risk)
```

**Why This Happens:**
- Treating assessment as "audit prep" not ongoing process
- No ownership after initial completion
- Resource constraints (no time for updates)
- "Set it and forget it" mentality

**How to Avoid:**
```
✅ Right Approach:
  Living Assessment Program:
  
  Quarterly Updates (Scheduled):
    Week 1 of Q2, Q3, Q4:
      ☐ Review vendor changes from A.5.23.1 (new/decommissioned)
      ☐ Add new vendors to assessment
      ☐ Archive decommissioned vendors
      ☐ Check certificate expirations (upcoming 90 days)
      ☐ Review SLA performance (last quarter)
      ☐ Update evidence register
      ☐ Run approval workflow (may be expedited if minor changes)
  
  Continuous Monitoring:
    ☐ Certificate expiry alerts (60 days before)
    ☐ Contract renewal alerts (90 days before)
    ☐ SLA breach notifications (from monitoring)
    ☐ Vendor security incident notifications
  
  Event-Driven Updates:
    Trigger assessment update when:
      - New Critical/High vendor added
      - Existing vendor changes criticality (Medium → High)
      - Vendor acquisition/merger announced
      - Major security incident at vendor
      - Regulatory change (new DORA/NIS2 requirements)
  
  Assign Ongoing Ownership:
    - Assessment Owner: Maintains and updates quarterly
    - Deputy: Backup owner (continuity if primary leaves)
    - Executive Sponsor: CISO or CIO (ensures resources)
```

#### Pitfall 7.2: Not Tracking Vendor Changes

**The Mistake:**
```
❌ Wrong Approach:
  Vendor X assessed January 2026:
    - HQ: Ireland (EU vendor, low CLOUD Act risk)
  
  June 2026: Vendor X acquired by US company (not noticed)
  
  January 2027: Assessment shows "Low risk" (now WRONG)
  Reality: Now US-owned, CLOUD Act applies, risk is MEDIUM-HIGH
```

**Why This Happens:**
- No monitoring of vendor M&A activity
- Vendor doesn't notify customers of ownership changes
- Assessment assumes static environment

**How to Avoid:**
```
✅ Right Approach:
  Vendor Change Monitoring:
  
  Monitor Sources:
    ☐ Vendor newsletters / email updates
    ☐ LinkedIn (vendor company page updates)
    ☐ Tech news (Crunchbase, TechCrunch, industry news)
    ☐ SEC filings (for public companies)
    ☐ Annual vendor review meetings ("any changes to your company?")
  
  Trigger Reassessment When:
    - Vendor acquired or merged
    - Vendor changes headquarters location
    - Vendor changes name (may indicate ownership change)
    - Major executive changes (new CEO, sold to PE firm)
    - Vendor announces new certifications (update assessment)
    - Vendor loses certifications (downgrade status)
  
  Contract Change Notification Clause:
    Negotiate into contracts:
      "Vendor shall notify Customer within 30 days of any change in:
       (a) Corporate ownership or control
       (b) Legal headquarters jurisdiction
       (c) Material changes to security certifications
       (d) Material changes to data processing locations
       (e) Subprocessor additions or changes"
  
  Quarterly "Significant Changes" Check:
    For Critical/High vendors:
      - Google vendor name + "acquisition"
      - Check vendor website "News" or "Press Releases"
      - Quick LinkedIn/Crunchbase check
      - Takes 2-3 minutes per vendor, catches major changes
```

---

### Prevention Summary: Your Assessment Quality Checklist

**Use this checklist to avoid common pitfalls:**
```
PROCESS:
☐ Assessment timeline: 4-6 weeks minimum (not rushed)
☐ Cross-functional team (not one person doing everything)
☐ A.5.23.1 inventory complete (prerequisite met)
☐ Risk-based approach (more depth on Critical/High)

EVIDENCE:
☐ All certifications independently verified (not just vendor claims)
☐ SOC 2 reports actually read (Type II, <12 months, reviewed for findings)
☐ Official documents collected (not screenshots)
☐ Evidence currency maintained (expiry tracking, quarterly refresh)

CONTRACTS:
☐ DPAs specify controls (not just "reasonable care")
☐ Subprocessor clauses GDPR-compliant (list + notification + objection)
☐ Liability caps assessed for adequacy (service criticality considered)
☐ Contract terms actually read by Legal (not rubber-stamped)

DATA SOVEREIGNTY:
☐ Full data flows understood (not just primary data location)
☐ GDPR compliance beyond location (DPA + SCCs + TIA if US vendor)
☐ Contractual commitments verified (not just portal settings)

JURISDICTIONAL RISK:
☐ CMK realistic assessment (mitigates, doesn't eliminate)
☐ Parent company jurisdiction researched (US parent = CLOUD Act)
☐ Risk rating based on full picture (location + keys + legal + data classification)

APPROVALS:
☐ Approvers given adequate time (3-5 days)
☐ Specific comments required (not just "Approved")
☐ Conditions tracked and followed up (not forgotten)

MAINTENANCE:
☐ Quarterly updates scheduled (living document)
☐ Vendor changes monitored (M&A, certifications)
☐ Ongoing ownership assigned (not abandoned after initial completion)
```

---

**END OF SECTION 6: COMMON PITFALLS & HOW TO AVOID THEM**

## Section 7: Quality Checklist

### Overview: Ensuring Assessment Quality

**Core Principle:**
> "Quality is not an act, it is a habit." - Aristotle

This section provides comprehensive checklists to ensure your vendor due diligence assessment is complete, accurate, and audit-ready before final approval.

**Quality Assurance Approach:**
```
┌─────────────────────────────────────────────────────────────┐
│              QUALITY ASSURANCE FRAMEWORK                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PRE-ASSESSMENT CHECKS                                      │
│  (Before you start)                                         │
│      ↓                                                      │
│  DURING-ASSESSMENT CHECKS                                   │
│  (Weekly progress validation)                               │
│      ↓                                                      │
│  POST-ASSESSMENT CHECKS                                     │
│  (Before approvals)                                         │
│      ↓                                                      │
│  AUDIT READINESS VALIDATION                                 │
│  (Final verification)                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**How to Use These Checklists:**

1. **Pre-Assessment:** Review before starting (confirms prerequisites)
2. **During Assessment:** Weekly self-check (track progress, catch issues early)
3. **Post-Assessment:** Complete before submitting for approval (final QA)
4. **Audit Readiness:** Final validation before auditor presentation

---

### Pre-Assessment Quality Checks

**Complete BEFORE starting the assessment:**

#### Prerequisites Verification
```
FOUNDATIONAL REQUIREMENTS:
☐ A.5.23.1 Cloud Service Inventory completed and current (<90 days old)
☐ Inventory vendor count matches expected range (30-60 for ~300 staff org)
☐ All services in inventory have criticality ratings (Critical/High/Medium/Low)
☐ All services have data classification (Public/Internal/Confidential/Restricted)
☐ Service owners identified for each cloud service

ORGANIZATIONAL READINESS:
☐ Policy ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements) approved
☐ Policy ISMS-POL-A.5.19-23-S5 (Cloud Services Security) approved
☐ Policy ISMS-POL-A.5.19-23-S6 (Assessment Methodology) approved
☐ Data classification scheme defined and documented
☐ Vendor risk rating methodology established
☐ Regulatory applicability determined (DORA, NIS2, etc.)

STAKEHOLDER COMMITMENT:
☐ Legal team committed to contract review (12-20 hours)
☐ Procurement team committed to vendor engagement (8-12 hours)
☐ Security team committed to certification verification (10-15 hours)
☐ DPO committed to data sovereignty review (8-12 hours)
☐ CISO sponsorship obtained (executive backing)
☐ Assessment coordinator assigned (owns process)

TOOLS & ACCESS:
☐ Contract management system access (read minimum, write preferred)
☐ Vendor portal credentials obtained (for major vendors)
☐ Evidence repository established (SharePoint, network share, etc.)
☐ Evidence Register template prepared (Sheet 9)
☐ Assessment workbook distributed to team (Excel or cloud-based)

TIMELINE:
☐ Assessment timeline defined (4-6 weeks for initial)
☐ Key milestones scheduled (evidence collection, reviews, approvals)
☐ Weekly sync meetings scheduled (30 min team alignment)
☐ Final approval target date set (realistic, not rushed)

PASS CRITERIA: All items checked = Ready to begin
FAIL CRITERIA: Any unchecked = Address before starting
```

---

### During-Assessment Quality Checks

**Weekly Progress Validation (Complete every Friday during assessment period):**

#### Week 1: Evidence Collection Launch
```
VENDOR COMMUNICATION:
☐ Evidence request emails sent to ALL vendors (from A.5.23.1 inventory)
☐ Tracking spreadsheet maintained (vendor, request date, response status)
☐ Auto-reminders configured (Day 7, Day 14 follow-ups)
☐ Evidence requests include all required documents (certs, contracts, SLAs)

INITIAL EVIDENCE GATHERING:
☐ Vendor trust centers reviewed (AWS, Azure, Google, major vendors)
☐ Publicly available certifications downloaded
☐ Contract management system queried (active cloud vendor contracts)
☐ Evidence repository folders created (Certifications, Contracts, SLA Reports, etc.)

TEAM COORDINATION:
☐ Kick-off meeting held (all stakeholders aligned)
☐ Roles and responsibilities confirmed (who owns which sheets)
☐ Evidence standards communicated (what constitutes acceptable proof)
☐ First weekly sync scheduled (progress review)

PROGRESS METRICS:
  Evidence requests sent: _____ / _____ vendors (target: 100%)
  Responses received: _____ / _____ (target: 20-30% Week 1)
  Public evidence collected: _____ vendors (major vendors)

ISSUES LOG:
  Blockers identified: _________________________________
  Escalations needed: _________________________________
  Risks to timeline: _________________________________
```

#### Week 2: Verification & Sheet Population
```
EVIDENCE COLLECTION:
☐ First follow-ups sent (vendors with no response after 7 days)
☐ Evidence organized by vendor (folder structure clean)
☐ Evidence Register (Sheet 9) populated with received items
☐ Evidence quality spot-checks (5-10 random items verified)

CERTIFICATE VERIFICATION:
☐ ISO 27001 certificates verified with issuing bodies (Critical/High vendors)
☐ Certificate numbers documented in Sheet 2
☐ Expiry dates tracked (alerts set for upcoming expirations)
☐ Certificate scope reviewed (covers services in use)

SHEET POPULATION:
☐ Sheet 2 (Certifications): 50%+ complete
☐ Sheet 3 (Contracts): Legal team engaged, key contracts reviewed
☐ Sheet 4 (SLAs): SLA commitments extracted from contracts
☐ Sheets 5-7: Initial data collection started

DATA QUALITY:
☐ Vendor names consistent across sheets (exact spelling)
☐ No "Unknown" or "TBD" entries for Critical/High vendors
☐ Status values (✅/⚠️/❌) based on evidence, not assumptions
☐ Evidence Location (Column I) populated for all assessments

PROGRESS METRICS:
  Evidence responses: _____ / _____ vendors (target: 60-70%)
  Sheet 2 completion: _____ % (target: 50%+)
  Certificate verifications: _____ / _____ (Critical/High vendors)

ISSUES LOG:
  Vendors not responding: _____________________________
  Missing evidence types: _____________________________
  Quality issues found: _______________________________
```

#### Week 3: Gap Analysis & Remediation Planning
```
EVIDENCE COMPLETION:
☐ Second follow-ups sent (vendors still unresponsive after 14 days)
☐ Escalations to Procurement (non-responsive vendors)
☐ Alternative evidence sources explored (contract clauses vs. missing docs)
☐ Evidence gaps documented with remediation plans

CONTRACT REVIEW:
☐ Legal completed contract reviews (DPA adequacy, liability, terms)
☐ Sheet 3 fully populated with contract analysis
☐ DORA/NIS2 columns completed (if applicable)
☐ Contract gaps identified (amendments needed)

DATA SOVEREIGNTY:
☐ DPO reviewed all DPAs (GDPR/FADP compliance)
☐ Cross-border transfer mechanisms documented (SCCs, adequacy)
☐ Data residency confirmed for Critical/High services
☐ Sheet 5 fully populated

JURISDICTIONAL RISK:
☐ US-nexus vendors identified (HQ or parent company research)
☐ CLOUD Act exposure assessed for all US vendors
☐ CMK deployment status verified (for mitigated vendors)
☐ Sheet 7 fully populated

GAP DOCUMENTATION:
☐ All gaps documented in Column J (specific, actionable)
☐ Remediation owners assigned (Column Q)
☐ Target remediation dates set (Column P)
☐ Risk IDs assigned for accepted risks (Column M)

PROGRESS METRICS:
  All sheets completion: _____ % (target: 80%+)
  Gaps identified: _____ (track count)
  Gaps with remediation plans: _____ / _____ (target: 100%)

ISSUES LOG:
  Critical gaps (urgent): _____________________________
  High-risk vendors: __________________________________
  Approval blockers: __________________________________
```

#### Week 4: Dashboard Review & Pre-Approval QA
```
FINAL EVIDENCE COLLECTION:
☐ All obtainable evidence collected (100% effort)
☐ Evidence gaps documented (vendor refusal, doesn't exist)
☐ Evidence Register complete (all items cataloged)
☐ Evidence storage tested (random retrieval check)

SHEET COMPLETION:
☐ All Sheets 2-7 100% complete (or gaps documented)
☐ Sheet 8 (Dashboard) formulas working correctly
☐ Sheet 9 (Evidence Register) links to all evidence
☐ Sheet 10 (Approval) ready for sign-off workflow

DATA QUALITY REVIEW:
☐ No blank cells in mandatory columns (A-Q base structure)
☐ All "✅ Compliant" statuses have evidence (Column I references)
☐ All "❌ Non-Compliant" have gap descriptions (Column J)
☐ Vendor names consistent (no spelling variations)

DASHBOARD VALIDATION:
☐ Overall compliance % calculated correctly
☐ Critical/High services compliance reviewed (target: 100%)
☐ Gap lists accurate (vendors match issues in Sheets 2-7)
☐ Jurisdictional risk metrics correct

PRE-APPROVAL PREPARATION:
☐ Summary prepared for Legal (contract gaps, required amendments)
☐ Summary prepared for Procurement (SLA issues, vendor escalations)
☐ Summary prepared for DPO (data sovereignty, CLOUD Act risks)
☐ Summary prepared for CISO (overall risk posture, top priorities)

PROGRESS METRICS:
  Assessment completion: _____ % (target: 100%)
  Evidence collection: _____ % (target: 95%+, some gaps OK)
  Ready for approvals: ☐ Yes  ☐ No

ISSUES LOG:
  Unresolved blockers: ________________________________
  Approval risks: _____________________________________
  Timeline concerns: __________________________________
```

---

### Post-Assessment Quality Checks

**Complete BEFORE submitting for approvals:**

#### Completeness Verification
```
MANDATORY FIELDS POPULATED:
☐ Every vendor has Cloud Service Name (Column A)
☐ Every vendor has Vendor Name (Column B)
☐ Every vendor has Service Type (Column C)
☐ Every vendor has Service Criticality (Column D)
☐ Every vendor has Data Classification (Column E)
☐ Every vendor has Contract Type (Column F)
☐ Every vendor has Status (Column H)

CRITICAL/HIGH SERVICES - 100% ASSESSMENT:
☐ All Critical services have security certifications (ISO 27001 OR SOC 2)
☐ All Critical services have DPAs reviewed and approved (if personal data)
☐ All Critical services have SLA commitments documented
☐ All Critical services have data residency confirmed
☐ All Critical services have audit rights or current SOC 2 alternative
☐ All US-nexus Critical services have jurisdictional risk assessment

EVIDENCE REGISTER:
☐ Every "✅ Compliant" has corresponding evidence entry
☐ All evidence IDs (EV-VDD-XXX) referenced from assessment sheets
☐ All evidence locations tested (documents retrievable)
☐ Evidence status current (no expired items marked "Current")
☐ Evidence collected within reasonable timeframe (<12 months)

DASHBOARD ACCURACY:
☐ Vendor count matches A.5.23.1 inventory
☐ Compliance percentages add up correctly
☐ Gap lists match issues in Sheets 2-7
☐ No #DIV/0! or #REF! formula errors
☐ Jurisdictional risk metrics accurate
```

#### Accuracy Verification
```
CERTIFICATION VERIFICATION:
☐ All ISO 27001 certificates verified with issuing bodies
☐ Certificate numbers documented and checked
☐ Expiry dates correct (future dates)
☐ SOC 2 reports are Type II (not Type I)
☐ SOC 2 examination periods within 12 months
☐ FedRAMP authorizations verified on FedRAMP Marketplace

CONTRACT ANALYSIS:
☐ Legal reviewed all Critical/High vendor contracts
☐ DPA adequacy assessed by DPO (if processing personal data)
☐ Liability caps assessed against service criticality
☐ Subprocessor lists obtained and reviewed
☐ Audit rights verified or SOC 2 alternative confirmed
☐ DORA/NIS2 columns accurate (if applicable)

SLA PERFORMANCE:
☐ SLA commitments extracted from contracts (not assumed)
☐ Actual performance data from monitoring systems (not vendor-only)
☐ SLA breach calculations verified
☐ Service credit calculations correct (per contract terms)
☐ Performance trends assessed (improving/stable/declining)

DATA SOVEREIGNTY:
☐ Data locations verified (not just vendor portal selection)
☐ Cross-border transfer mechanisms confirmed (SCCs version correct)
☐ DPO reviewed and approved all cross-border transfers
☐ CMK deployment verified (not just "available")
☐ EU Data Boundary commitments contractual (not just technical)

JURISDICTIONAL RISK:
☐ Corporate structure researched (parent company identified)
☐ US nexus correctly determined (HQ or parent)
☐ CLOUD Act exposure assessed realistically
☐ Compensating controls verified (not assumed)
☐ Risk ratings justified and documented
```

#### Consistency Verification
```
CROSS-SHEET CONSISTENCY:
☐ Vendor names identical across all sheets (Sheet 2-7)
☐ Service criticality consistent with A.5.23.1 inventory
☐ Data classification consistent with A.5.23.1 inventory
☐ Evidence IDs match between assessment sheets and Evidence Register
☐ Contract dates consistent across Sheets 3-6

STATUS LOGIC:
☐ "✅ Compliant" = All requirements met + evidence present
☐ "⚠️ Partial" = Some requirements met, minor gaps with remediation
☐ "❌ Non-Compliant" = Major gaps, no remediation plan OR vendor refusal
☐ "N/A" = Requirement legitimately not applicable (documented why)

GAP DOCUMENTATION:
☐ All "⚠️ Partial" have gap descriptions (Column J)
☐ All "❌ Non-Compliant" have gap descriptions
☐ All gaps have remediation owners (Column Q)
☐ All gaps have target dates (Column P) or risk acceptance (Column M)
☐ Gaps are specific and actionable (not vague)

EVIDENCE TRACEABILITY:
☐ Assessment → Evidence Register → Document (full chain)
☐ No orphaned evidence (evidence with no assessment reference)
☐ No broken links (evidence locations work)
☐ Evidence dates match assessment dates (reasonable currency)
```

#### Stakeholder Review Completion
```
LEGAL REVIEW:
☐ Legal reviewed Sheet 3 (Contract Terms) thoroughly
☐ Legal provided specific comments (not just "looks OK")
☐ Contract gaps identified and prioritized
☐ Amendment requests drafted (for critical gaps)
☐ Legal sign-off obtained (Sheet 10)

PROCUREMENT REVIEW:
☐ Procurement reviewed Sheet 4 (SLA Performance)
☐ Vendor escalations identified and scheduled
☐ Contract renewals tracked (auto-renewal alerts set)
☐ Service credit claims submitted (unclaimed credits pursued)
☐ Procurement sign-off obtained (Sheet 10)

DPO REVIEW:
☐ DPO reviewed Sheet 5 (Data Sovereignty)
☐ DPO reviewed Sheet 7 (Jurisdictional Risk)
☐ All DPAs assessed for GDPR/FADP compliance
☐ Cross-border transfers approved or remediation required
☐ Transfer Impact Assessments completed (if US vendors)
☐ DPO sign-off obtained (Sheet 10)

SECURITY REVIEW:
☐ Security reviewed Sheet 2 (Certifications)
☐ Security reviewed Sheet 6 (Audit Rights)
☐ Technical controls verified (CMK, encryption, etc.)
☐ Vendor security posture assessed
☐ Security input provided to CISO approval

CISO REVIEW:
☐ CISO reviewed Dashboard (Sheet 8)
☐ CISO reviewed all stakeholder comments
☐ Risk acceptances documented (for high/critical risks)
☐ Top priorities identified (P0/P1 actions)
☐ CISO final sign-off obtained (Sheet 10)
```

---

### Audit Readiness Validation

**Final checks before presenting to auditors:**

#### Documentation Completeness
```
POLICY & FRAMEWORK:
☐ ISMS-POL-A.5.19-23 (Master Policy) approved and current
☐ ISMS-POL-A.5.19-23-S2 (Supplier Agreements) referenced
☐ ISMS-POL-A.5.19-23-S5 (Cloud Services) referenced
☐ ISMS-POL-A.5.19-23-S6 (Assessment Methodology) referenced
☐ Policy version matches assessment version

ASSESSMENT WORKBOOK:
☐ All 10 sheets present and complete
☐ Document control information filled (date, version, assessor)
☐ Instructions sheet (Sheet 1) updated and accurate
☐ All formulas working (no errors)
☐ Assessment approved (Sheet 10 all sign-offs)

EVIDENCE REPOSITORY:
☐ Evidence organized and accessible
☐ Evidence Register complete and current
☐ All evidence retrievable (tested)
☐ Evidence storage permissions set (auditor read access)
☐ Evidence retention compliant (keep for audit period)

SUPPORTING DOCUMENTATION:
☐ A.5.23.1 Cloud Service Inventory (prerequisite)
☐ Risk register (for accepted risks referenced in Column M)
☐ Gap remediation tracking (for conditions from approvals)
☐ Stakeholder approval emails/memos (backup for Sheet 10)
```

#### Audit Trail Verification
```
TRACEABILITY:
☐ Control A.5.23 → Policy → Assessment → Evidence (complete chain)
☐ Every compliance status traceable to specific evidence
☐ Gap remediation tracked with dates and owners
☐ Approvals documented with signatures/emails/timestamps

OBJECTIVITY:
☐ No reliance on vendor self-attestation without verification
☐ All certifications independently verified
☐ All contracts reviewed by Legal (not just coordinator)
☐ All data sovereignty assessments reviewed by DPO
☐ Risk ratings justified with objective criteria

CURRENCY:
☐ Assessment completion date ≤90 days before audit
☐ Evidence collected ≤12 months before audit (preferably ≤6 months)
☐ Certificates current (not expired)
☐ SOC 2 reports ≤12 months old
☐ No outdated assessments (vendor changes addressed)

CONSISTENCY:
☐ Terminology consistent across documents
☐ Vendor names consistent (no variations)
☐ Data classification scheme consistent with policy
☐ Risk ratings consistent with methodology
☐ No contradictions between assessment and evidence
```

#### Common Auditor Questions - Preparation
```
EXPECT AUDITORS TO ASK:

"How do you ensure completeness of vendor inventory?"
☐ Prepared answer: A.5.23.1 discovery methods (CASB, expense reports, interviews)
☐ Evidence: A.5.23.1 inventory with discovery methodology documented

"How do you verify vendor security certifications?"
☐ Prepared answer: Independent verification with issuing bodies
☐ Evidence: Certificate verification records (screenshots, emails)

"What if a Critical vendor doesn't have ISO 27001 or SOC 2?"
☐ Prepared answer: Not acceptable - vendor must obtain OR we migrate
☐ Evidence: Remediation plan or migration project plan

"How do you assess CLOUD Act risk for US vendors?"
☐ Prepared answer: Jurisdictional risk assessment (Sheet 7), compensating controls (CMK)
☐ Evidence: DPO risk assessments, CMK configuration proofs

"How do you ensure contracts are adequate?"
☐ Prepared answer: Legal line-by-line review, DPO for DPAs, procurement for SLAs
☐ Evidence: Legal review memos, DPO sign-offs (Sheet 10)

"What's your process for ongoing monitoring?"
☐ Prepared answer: Quarterly updates, certificate expiry tracking, SLA monitoring
☐ Evidence: Update history (version control), tracking calendars/reminders

"Can you demonstrate evidence for Vendor X's compliance?"
☐ Test yourself: Pick 5 random vendors
☐ For each: Retrieve evidence in <5 minutes
☐ Explain compliance status based on evidence
```

#### Pre-Audit Dry Run
```
CONDUCT INTERNAL AUDIT SIMULATION:

Select Random Sample (10-15 vendors):
  ☐ 3 Critical services
  ☐ 3 High services
  ☐ 2 Medium services
  ☐ 2 Low services

For Each Vendor, Verify:
  ☐ Can find vendor in assessment (Sheet 2-7)
  ☐ Status makes sense (✅/⚠️/❌ justified)
  ☐ Evidence exists and retrievable (<5 min)
  ☐ Evidence supports compliance status
  ☐ Gaps (if any) have remediation plans
  ☐ Approvers signed off knowing the gaps

Practice Explaining:
  ☐ Why vendor is rated Critical/High/Medium/Low
  ☐ How compliance status was determined
  ☐ What evidence supports the status
  ☐ What gaps exist and remediation approach
  ☐ How this vendor is monitored ongoing

Identify Weak Points:
  ☐ Vendors with weak evidence: _____________________
  ☐ Inconsistencies found: __________________________
  ☐ Missing documentation: __________________________
  ☐ Explanation gaps: _______________________________

Remediate Before Audit:
  ☐ Strengthen weak evidence
  ☐ Fix inconsistencies
  ☐ Obtain missing documentation
  ☐ Practice explanations
```

---

### Self-Assessment Scoring

**Quantitative quality measurement:**

#### Scoring Methodology
```
CALCULATE YOUR ASSESSMENT QUALITY SCORE:

Category 1: COMPLETENESS (30 points)
  All vendors from A.5.23.1 assessed (10 pts) ............ _____
  All mandatory fields populated (10 pts) ................ _____
  All Critical/High vendors 100% assessed (10 pts) ....... _____

Category 2: EVIDENCE (25 points)
  All certifications verified (10 pts) ................... _____
  All evidence retrievable (10 pts) ...................... _____
  Evidence current (<12 months) (5 pts) .................. _____

Category 3: ACCURACY (20 points)
  Legal reviewed contracts (7 pts) ....................... _____
  DPO reviewed data sovereignty (7 pts) .................. _____
  Security verified certifications (6 pts) ............... _____

Category 4: CONSISTENCY (15 points)
  Vendor names consistent (5 pts) ........................ _____
  Status logic consistent (5 pts) ........................ _____
  Cross-sheet references accurate (5 pts) ................ _____

Category 5: AUDIT READINESS (10 points)
  Audit trail complete (5 pts) ........................... _____
  Can answer auditor questions (5 pts) ................... _____

TOTAL SCORE: _____ / 100

RATING:
  90-100: Excellent - Audit ready
  80-89:  Good - Minor improvements needed
  70-79:  Acceptable - Some gaps, address before audit
  60-69:  Poor - Significant rework required
  <60:    Failing - Major quality issues
```

#### Pass/Fail Criteria
```
MANDATORY REQUIREMENTS (Must pass ALL):

☐ A.5.23.1 prerequisite complete
☐ All Critical/High services assessed (100%)
☐ All "✅ Compliant" have evidence
☐ Legal reviewed contracts
☐ DPO reviewed data sovereignty
☐ CISO approved assessment
☐ Evidence retrievable (<5 min average)

IF ANY MANDATORY REQUIREMENT FAILS:
  → Assessment NOT audit-ready
  → Remediate failed items before proceeding
  → DO NOT submit to auditors until fixed

QUALITY GATES:

Gate 1: Completeness (MUST PASS)
  ☐ >95% vendors assessed (allows 5% edge cases)
  ☐ >99% Critical/High assessed (near-perfect)

Gate 2: Evidence (MUST PASS)
  ☐ >90% evidence collected (some vendor refusal OK)
  ☐ 100% Critical/High evidence (no exceptions)

Gate 3: Approvals (MUST PASS)
  ☐ All 4 approvers signed off (Legal, Procurement, DPO, CISO)
  ☐ Any conditions tracked with owners and deadlines

Gate 4: Audit Trail (MUST PASS)
  ☐ Control → Policy → Assessment → Evidence (traceable)
  ☐ Random evidence retrieval test passed (10 samples)
```

---

### Quality Improvement Tracking

**For assessments that don't initially pass quality checks:**
```
QUALITY ISSUE LOG:

Issue # | Category | Description | Severity | Owner | Due Date | Status
--------|----------|-------------|----------|-------|----------|-------
001     | Evidence | 5 vendors missing ISO certs | High | Security | [Date] | Open
002     | Accuracy | Contract dates inconsistent | Medium | Legal | [Date] | Fixed
...

SEVERITY DEFINITIONS:
  Critical: Prevents audit approval (fix immediately)
  High:     Significant gap (fix before approvals)
  Medium:   Quality concern (fix before audit)
  Low:      Minor improvement (fix when possible)

REMEDIATION WORKFLOW:
  1. Identify issue
  2. Assign severity
  3. Assign owner
  4. Set deadline (based on severity)
  5. Track to closure
  6. Re-run quality checks
  7. Verify issue resolved
```

---

### Final Quality Checklist Summary

**One-page checklist for final validation:**
```
ASSESSMENT QUALITY - FINAL VALIDATION

Prerequisites:
☐ A.5.23.1 complete
☐ Policies approved
☐ Team committed

Completeness:
☐ All vendors assessed
☐ All Critical/High 100%
☐ All fields populated

Evidence:
☐ Certifications verified
☐ Evidence retrievable
☐ Evidence current

Accuracy:
☐ Legal reviewed
☐ DPO reviewed
☐ Security verified

Approvals:
☐ Legal sign-off
☐ Procurement sign-off
☐ DPO sign-off
☐ CISO sign-off

Audit Ready:
☐ Audit trail complete
☐ Dry run passed
☐ Auditor questions prepared

Quality Score: _____ / 100

Assessment Status:
☐ APPROVED - Audit Ready
☐ CONDITIONAL - Minor fixes needed
☐ REJECTED - Major rework required

Approver: _________________ Date: _________
```

---

**END OF SECTION 7: QUALITY CHECKLIST**

## Section 8: Review & Approval Process

### Overview: Multi-Stakeholder Approval Workflow

**Core Principle:**
> "Approval without review is rubber-stamping. Review without expertise is theater. Both together create accountability."

This section defines the approval workflow, what each approver validates, how to handle conditions and rejections, and how to track approvals to completion.

**Approval Architecture:**
```
┌─────────────────────────────────────────────────────────────────┐
│              APPROVAL WORKFLOW (SEQUENTIAL)                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  STEP 1: COORDINATOR READINESS CHECK                            │
│           ↓ (Self-QA complete, quality checks passed)          │
│                                                                 │
│  STEP 2: LEGAL REVIEW                                          │
│           ↓ (Contracts, audit rights, liability)               │
│                                                                 │
│  STEP 3: PROCUREMENT REVIEW                                    │
│           ↓ (Vendor relationships, SLAs, renewals)             │
│                                                                 │
│  STEP 4: DATA PROTECTION OFFICER REVIEW             │
│           ↓ (Data sovereignty, GDPR, CLOUD Act)                │
│                                                                 │
│  STEP 5: CISO FINAL APPROVAL                                   │
│           ↓ (Overall risk posture, gap remediation)            │
│                                                                 │
│  OUTCOME: ASSESSMENT STATUS                                    │
│           • Approved - Audit Ready                             │
│           • Approved with Conditions                           │
│           • Rejected - Remediation Required                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key Principles:**

1. **Sequential Approval:** Each approver completes before next starts (prevents rework)
2. **Specific Comments Required:** No blank approvals (must explain decision)
3. **Conditions Tracked:** If "Approved with Conditions," conditions must be documented
4. **Rejections Explained:** Must specify what needs fixing
5. **Evidence-Based:** Approvers review evidence, not just summaries

---

### Step 1: Coordinator Readiness Check

**Before submitting to Legal (first approver):**

#### Pre-Submission Validation
```
COORDINATOR SELF-CHECK:

Quality Validation (from Section 7):
☐ Quality score ≥80 / 100
☐ All mandatory requirements passed
☐ Completeness ≥95%
☐ Evidence collection ≥90%
☐ All Critical/High vendors 100% assessed

Team Alignment:
☐ Weekly syncs completed (all 4 weeks)
☐ Team members provided input (Legal, Procurement, Security, DPO)
☐ No pending questions or data gaps
☐ All stakeholders aware approval process starting

Documentation Complete:
☐ All 10 sheets finalized
☐ Evidence Register 100% populated
☐ Dashboard metrics validated
☐ Evidence repository organized and accessible

Approver Preparation:
☐ Summary documents prepared for each approver
☐ Key findings highlighted (not buried in workbook)
☐ Approver-specific questions anticipated
☐ Adequate review time allocated (3-5 days per approver)
```

#### Preparing Approver Summaries

**Don't just send the workbook - provide focused summaries:**

**Legal Review Package:**
```
LEGAL REVIEW SUMMARY - ISMS-IMP-A.5.23.S2

Assessment Overview:
  Total Vendors: 47
  Critical/High Services: 20
  Overall Compliance: 87%

YOUR REVIEW FOCUS (Sheets 3 & 6):
  
CONTRACT TERMS (Sheet 3):
  ✅ Compliant: 39 vendors (83%)
  ⚠️ Requiring Review: 8 vendors
  
  CRITICAL ISSUES REQUIRING LEGAL ATTENTION:
  
  1. Vendor XYZ (Critical CRM):
     - Issue: Liability cap CHF 100 (inadequate for Critical service)
     - Recommendation: Negotiate minimum CHF 5M or 12 months fees
     - Priority: URGENT (Critical service, Confidential data)
  
  2. Vendor ABC (High Analytics):
     - Issue: No DPA (processing personal data)
     - Recommendation: Execute DPA immediately (GDPR violation risk)
     - Priority: URGENT
  
  3. Five vendors missing DORA contract clauses (Sheet 3, Column Y):
     - Vendors: [List]
     - Recommendation: Amendment required if DORA applicable
     - Priority: HIGH (if [Organization] is EU financial entity)
  
  MEDIUM PRIORITY:
  - 3 vendors with weak indemnification clauses
  - 2 vendors with vague termination rights
  
AUDIT RIGHTS (Sheet 6):
  - 2 Critical vendors with no audit rights or SOC 2 alternative
  - Recommendation: Negotiate audit clause OR require SOC 2 Type II
  
REQUESTED DECISION:
  ☐ Approved (contracts adequate or minor gaps with remediation plans)
  ☐ Approved with Conditions (specify amendments and deadlines)
  ☐ Rejected (major gaps must be fixed before proceeding)

REVIEW DEADLINE: [Date + 5 business days]

Workbook Location: [SharePoint link]
Evidence Repository: [Network path]
Questions: Contact [Coordinator Name, Email]
```

**Similar summaries for:**
- Procurement (focus: SLA performance, vendor escalations)
- DPO (focus: Data sovereignty, CLOUD Act, cross-border transfers)
- CISO (focus: Overall risk posture, top priorities)

---

### Step 2: Legal Review

**Legal's Role:** Ensure contracts protect [Organization] and comply with regulations

#### What Legal Reviews
```
LEGAL REVIEW CHECKLIST:

SHEET 3: CONTRACT TERMS ANALYSIS

For Each Vendor (prioritize Critical/High):

☐ Contract Type Appropriate
   - MSA + DPA for service type?
   - Subscription agreement adequate or need custom MSA?

☐ Data Protection Agreement (DPA)
   - GDPR Article 28 compliant (if EU/personal data)?
   - FADP compliant (if Swiss data)?
   - Processor obligations clear?
   - Subprocessor disclosure adequate?
   - Data breach notification ≤48 hours?
   - Data return/deletion upon termination?

☐ Liability & Indemnification
   - Liability cap adequate for service criticality?
   - Exceptions to cap (data breach, gross negligence)?
   - Indemnification covers data breaches?
   - Indemnification covers regulatory fines?

☐ Termination Rights
   - Termination for convenience allowed?
   - Notice period reasonable (≤90 days)?
   - Data return process defined?
   - No excessive early termination penalties?

☐ Regulatory Compliance (if applicable)
   - DORA Article 30 clauses (if EU financial entity)?
   - NIS2 supply chain clauses (if EU essential/important entity)?

SHEET 6: AUDIT RIGHTS

☐ Audit Rights Adequate
   - Critical/High vendors: Direct audit rights OR current SOC 2?
   - Audit frequency sufficient (annual minimum)?
   - Audit scope adequate (systems, processes, personnel)?
   - Reasonable notice period (not excessive delay)?

☐ Forensic Investigation Support
   - Incident investigation cooperation clause?
   - Log access upon security incident?
   - Timeline for forensic support (≤24 hours)?
```

#### Legal Review Outcomes

**Outcome 1: Approved**
```
Legal Review - APPROVED

Review Date: 25.01.2026
Reviewed By: Jane Smith, Legal Counsel

CONTRACT COMPLIANCE: Compliant

Findings:
  - 39/47 vendors have adequate contracts (83%)
  - 8 vendors have minor gaps with documented remediation plans
  - All Critical services have DPAs (if processing personal data)
  - Liability caps reviewed and adequate for most services

Minor Issues (Acceptable with Remediation):
  - 3 vendors: Weak indemnification clauses
    Remediation: Negotiate stronger indemnification at next renewal
    Timeline: Renewals in Q2/Q3 2026
  
  - 2 vendors: Termination period 120 days (prefer ≤90)
    Remediation: Renegotiate at renewal OR accept for Medium criticality
    Timeline: Q3 2026

STATUS: APPROVED

Comments:
  Contracts overall provide adequate legal protection. Minor gaps have
  reasonable remediation plans. Recommend prioritizing Critical service
  contract improvements at earliest renewal opportunities.

Next Legal Review: Q2 2026 (quarterly cycle)
```

**Outcome 2: Approved with Conditions**
```
Legal Review - APPROVED WITH CONDITIONS

Review Date: 25.01.2026
Reviewed By: Jane Smith, Legal Counsel

CONTRACT COMPLIANCE: Partially Compliant

CRITICAL ISSUES REQUIRING REMEDIATION:

CONDITION 1: Vendor XYZ DPA Execution (URGENT)
  Issue: Vendor XYZ (Critical CRM) has no DPA, processing personal data
  GDPR Risk: HIGH - violation of Article 28 (processor agreement required)
  Required Action: Execute DPA immediately
  Owner: Legal (negotiate with vendor)
  Deadline: 31.01.2026 (URGENT - 6 days)
  Evidence Required: Executed DPA with all required elements
  
CONDITION 2: Vendor ABC Liability Cap Renegotiation
  Issue: CHF 100 cap for Critical service (Confidential data)
  Risk: Inadequate protection in data breach scenario
  Required Action: Renegotiate minimum CHF 5M or 12 months fees
  Owner: Procurement (Legal support)
  Deadline: 28.02.2026 (30 days)
  Alternatives: If vendor refuses, escalate to CISO for risk acceptance
                OR initiate vendor replacement evaluation

CONDITION 3: DORA Contract Amendments (if applicable)
  Issue: 5 vendors missing DORA Article 30 clauses
  Applicability: ONLY if [Organization] is EU financial entity under DORA
  Required Action: Amend contracts to include DORA requirements
  Owner: Legal
  Deadline: 30.06.2026 (DORA compliance deadline)
  Evidence Required: Executed amendments or vendor confirmation

STATUS: APPROVED WITH CONDITIONS

Assessment may proceed to next approver, but CONDITIONS MUST BE MET by
specified deadlines. Legal will re-review at next quarterly update to
verify condition completion.

If CONDITIONS NOT MET by deadlines:
  - Vendor XYZ: Service suspension until DPA executed
  - Vendor ABC: Escalate to CISO, risk acceptance OR vendor replacement
  - DORA: Regulatory non-compliance risk (if applicable)

Next Legal Review: Q2 2026 + Condition verification
```

**Outcome 3: Rejected**
```
Legal Review - REJECTED

Review Date: 25.01.2026
Reviewed By: Jane Smith, Legal Counsel

CONTRACT COMPLIANCE: Non-Compliant

CRITICAL ISSUES PREVENTING APPROVAL:

ISSUE 1: Multiple Critical Services Without DPAs
  Vendors: Vendor A, Vendor B, Vendor C (3 Critical services)
  Problem: All processing personal data, no DPAs executed
  GDPR Violation: Article 28 requires processor agreements BEFORE processing
  Current State: Non-compliant, regulatory risk
  
  Required Before Re-Submission:
    ☐ Execute DPAs with all 3 vendors
    ☐ DPAs must include all required elements (subprocessors, breach notification, etc.)
    ☐ DPO review and approval of each DPA
    ☐ Evidence: Executed DPAs in Evidence Register

ISSUE 2: Contracts Not Actually Reviewed
  Evidence: Many contracts marked "Yes (Adequate)" without Legal review
  Problem: Coordinator assumed adequacy without Legal verification
  Assessment states: "Legal reviewed contracts" (FALSE)
  
  Required Before Re-Submission:
    ☐ Legal MUST review ALL Critical/High vendor contracts (line-by-line)
    ☐ Assessment must accurately reflect Legal review status
    ☐ Gaps identified and documented (not assumed adequate)
    ☐ Evidence: Legal review memos for each contract

ISSUE 3: Liability Caps Not Assessed
  Problem: All liability caps marked "adequate" without analysis
  Reality: Several Critical services have CHF 100 caps (clearly inadequate)
  
  Required Before Re-Submission:
    ☐ Assess each liability cap against service criticality
    ☐ Document inadequate caps with remediation plans
    ☐ Risk acceptance from CISO for caps that cannot be negotiated

STATUS: REJECTED - Remediation Required

Assessment cannot proceed to next approver until CRITICAL ISSUES resolved.
This is not a minor gap - these are fundamental compliance issues.

Re-submit to Legal when:
  ✓ All DPAs executed (Issue 1)
  ✓ Contracts actually reviewed by Legal (Issue 2)
  ✓ Liability caps properly assessed (Issue 3)

Estimated Remediation Time: 2-4 weeks (DPA negotiation + Legal review)

Do not submit to Procurement, DPO, or CISO until Legal re-approval obtained.
```

#### Legal Review Timeline
```
STANDARD LEGAL REVIEW TIMELINE:

Day 0: Assessment submitted to Legal
  - Legal receives summary + workbook access
  - Legal schedules review time (3-5 days)

Day 1-3: Legal conducts review
  - Reviews Sheet 3 (Contract Terms) in detail
  - Spot-checks contracts for Critical/High vendors
  - Reviews Sheet 6 (Audit Rights)
  - Documents findings

Day 4-5: Legal prepares decision
  - Writes comments (specific issues, recommendations)
  - Determines status (Approved / Approved with Conditions / Rejected)
  - If conditions: Specifies deadlines and owners

Day 5: Legal submits decision
  - Updates Sheet 10 (Approval Sign-Off)
  - Notifies Coordinator of decision
  - If Approved/Approved with Conditions: Triggers Procurement review
  - If Rejected: Assessment returns to Coordinator for remediation
```

---

### Step 3: Procurement Review

**Procurement's Role:** Ensure vendor relationships are managed and SLAs are adequate

#### What Procurement Reviews
```
PROCUREMENT REVIEW CHECKLIST:

SHEET 3: CONTRACT TERMS (Vendor Relationship Perspective)

☐ Contract Types Appropriate
   - Vendors have executed contracts (not just verbal agreements)?
   - Contract structure matches relationship (MSA vs. subscription)?

☐ Renewal Tracking
   - All auto-renewal dates documented?
   - Renewal alerts set in contract management system?
   - Adequate lead time for renewal negotiations (90+ days)?

☐ Contract Owner Assignment
   - Every vendor has internal owner (Column Q)?
   - Owners aware of their responsibilities?

SHEET 4: SLA REQUIREMENTS & PERFORMANCE

☐ SLA Commitments Documented
   - All Critical/High services have SLAs?
   - SLA percentages specific (not "best efforts")?
   - Support response times documented?

☐ SLA Performance Tracking
   - Actual performance tracked (not just vendor claims)?
   - SLA breaches calculated correctly?
   - Service credits claimed where owed?

☐ Vendor Escalations
   - Vendors with >3 breaches identified?
   - Vendor performance meetings scheduled?
   - Underperforming vendors have improvement plans?

☐ Unclaimed Service Credits
   - All SLA penalties calculated?
   - Credits submitted to vendors?
   - If unclaimed: Reasonable explanation (e.g., within claim window)?
```

#### Procurement Review Outcomes

**Outcome 1: Approved**
```
Procurement Review - APPROVED

Review Date: 27.01.2026
Reviewed By: Tom Anderson, Procurement Manager

VENDOR RELATIONSHIP STATUS: Satisfactory
CONTRACT RENEWALS TRACKED: Yes
SLA PERFORMANCE ACCEPTABLE: Yes

Findings:
  - All vendors have executed contracts (no verbal-only relationships)
  - Renewal tracking in place (Agiloft CMS with 90-day alerts)
  - SLA performance generally acceptable (87% meeting commitments)
  - Service credits claimed where owed (CHF 8,500 recovered Q4 2025)

Vendor Escalations Planned:
  - 4 vendors require performance discussions (SLA breaches):
    * AWS EC2 (2 breaches, root cause: capacity issue - now resolved)
    * Vendor B (5 breaches, ongoing issue)
    * Vendor F (3 breaches, improvement plan required)
    * Vendor J (4 breaches, considering replacement)
  
  - Escalation meetings scheduled: Week of 03.02.2026

Upcoming Renewals (Next 6 Months):
  - Q2 2026: 12 contracts renewing
  - Renewal evaluations start: 01.03.2026
  - Budget approved for renewals/replacements

STATUS: APPROVED

Comments:
  Vendor relationships are actively managed. SLA performance is tracked and
  underperforming vendors are being addressed. Recommend continuing quarterly
  vendor performance reviews to maintain oversight.

Next Procurement Review: Q2 2026
```

**Outcome 2: Approved with Conditions**
```
Procurement Review - APPROVED WITH CONDITIONS

Review Date: 27.01.2026
Reviewed By: Tom Anderson, Procurement Manager

VENDOR RELATIONSHIP STATUS: Needs Improvement
SLA PERFORMANCE ACCEPTABLE: Needs Escalation

CONDITIONS REQUIRING ATTENTION:

CONDITION 1: Vendor B Performance Escalation (URGENT)
  Issue: 5 SLA breaches in 12 months, declining trend
  Impact: High criticality service, user complaints increasing
  Required Action: 
    ☐ Executive escalation to Vendor B (VP level)
    ☐ Formal improvement plan with monthly milestones
    ☐ If no improvement by Q2: Initiate vendor replacement RFP
  Owner: Procurement
  Deadline: Executive meeting by 15.02.2026
  
CONDITION 2: Unclaimed Service Credits Recovery
  Issue: CHF 12,000 in service credits not claimed (6-12 months old)
  Risk: May exceed claim window (typically 12 months)
  Required Action:
    ☐ Review all unclaimed credits (identify claim deadlines)
    ☐ Submit all eligible claims immediately
    ☐ Implement automated claim process for future
  Owner: Procurement + Finance
  Deadline: Claims submitted by 15.02.2026

CONDITION 3: Contract Renewal Preparation (Q2 2026)
  Issue: 12 contracts renewing Q2, evaluations not yet started
  Risk: Insufficient time for vendor alternatives if needed
  Required Action:
    ☐ Start renewal evaluations immediately (not 01.03.2026)
    ☐ Identify vendors for renegotiation vs. replacement
    ☐ Allocate budget for migrations if vendor changes
  Owner: Procurement
  Deadline: Evaluations complete by 28.02.2026

STATUS: APPROVED WITH CONDITIONS

Assessment may proceed, but Procurement CONDITIONS must be addressed.
Vendor B performance is concerning and requires urgent attention.

Condition Tracking: Monthly Procurement review until all conditions met.
```

---

### Step 4: Data Protection Officer (DPO) Review

**DPO's Role:** Ensure GDPR/FADP compliance and assess jurisdictional risks

#### What DPO Reviews
```
DPO REVIEW CHECKLIST:

SHEET 5: DATA SOVEREIGNTY & JURISDICTION

☐ DPA Adequacy (GDPR Article 28)
   - All vendors processing personal data have DPAs?
   - DPAs include all required elements?
   - Processor obligations clear and enforceable?
   - Subprocessor lists reviewed and acceptable?
   - Data breach notification ≤48 hours committed?

☐ Cross-Border Data Transfers
   - All transfers outside EU/Switzerland identified?
   - Standard Contractual Clauses (SCCs) in place (if needed)?
   - SCCs are post-Schrems II version (2021+)?
   - Transfer Impact Assessments (TIA) completed (if US vendor)?

☐ Data Residency Compliance
   - Data storage locations documented?
   - Locations comply with regulatory requirements?
   - Contractual data residency guarantees (if required)?

☐ Regulatory Compliance
   - GDPR requirements met (if processing EU personal data)?
   - FADP requirements met (if processing Swiss data)?
   - Sector-specific requirements (HIPAA, etc.) addressed?

SHEET 7: JURISDICTIONAL RISK ASSESSMENT

☐ US-Nexus Identification
   - All US vendors identified (HQ or parent company)?
   - Corporate structure research complete?

☐ CLOUD Act Assessment
   - CLOUD Act exposure assessed for all US vendors?
   - Exposure level realistic (not understated)?
   - Transfer Impact Assessments completed?

☐ Compensating Controls
   - Customer-managed keys deployed where needed?
   - EU Data Boundary commitments obtained?
   - Supplementary measures adequate per Schrems II?

☐ Risk Ratings
   - Jurisdictional risk ratings justified?
   - High/Critical risks have CISO/DPO approval?
   - Risk acceptance documented (if accepting residual risk)?
```

#### DPO Review Outcomes

**Outcome 1: Approved**
```
DPO Review - APPROVED

Review Date: 29.01.2026
Reviewed By: Maria Garcia, Data Protection Officer

DATA PROTECTION COMPLIANCE: Compliant
CROSS-BORDER TRANSFER STATUS: Approved
JURISDICTIONAL RISK ACCEPTABLE: Yes

Findings:
  
DATA SOVEREIGNTY (Sheet 5):
  - All DPAs reviewed and adequate for GDPR/FADP
  - Cross-border transfers properly documented
  - 8 US vendors: All have post-Schrems II SCCs
  - Transfer Impact Assessments completed for all US vendors
  - Data residency compliance: 94% (excellent)

JURISDICTIONAL RISK (Sheet 7):
  - 22 US-nexus vendors identified correctly
  - CLOUD Act exposure assessed realistically
  - Compensating controls:
    * 7 vendors with CMK + EU Data Boundary (strong mitigation)
    * 10 vendors with CMK only (partial mitigation)
    * 5 vendors unmitigated (assessed and accepted)
  - Risk ratings appropriate and justified

APPROVED CROSS-BORDER TRANSFERS:
  - All transfers to US: SCCs + TIA + supplementary measures
  - All transfers to UK: Adequacy decision (no SCCs needed)
  - All transfers to Switzerland: Adequacy decision

RESIDUAL RISKS (Acceptable):
  - 5 US vendors without CMK (Medium criticality, Internal data only)
  - Risk accepted based on data classification (not Confidential/Restricted)
  - Recommend CMK deployment for future Confidential data use

STATUS: APPROVED

Comments:
  Data protection compliance is strong. CLOUD Act risks have been thoroughly
  assessed and appropriately mitigated. The organization demonstrates good
  understanding of Schrems II requirements.

  Recommendation: Continue quarterly reviews to ensure ongoing compliance,
  especially if data classification changes for any services.

Next DPO Review: Q2 2026
```

**Outcome 2: Approved with Conditions**
```
DPO Review - APPROVED WITH CONDITIONS

Review Date: 29.01.2026
Reviewed By: Maria Garcia, Data Protection Officer

DATA PROTECTION COMPLIANCE: Partially Compliant
CROSS-BORDER TRANSFER STATUS: Requires Action
JURISDICTIONAL RISK: Acceptable with Controls

CRITICAL CONDITIONS:

CONDITION 1: Complete Transfer Impact Assessments (URGENT)
  Issue: 5 US vendors missing TIAs (Schrems II requirement)
  Vendors: Vendor A, Vendor C, Vendor E, Vendor G, Vendor I
  Data: All processing Confidential personal data
  Risk: GDPR non-compliance (SCCs alone insufficient post-Schrems II)
  
  Required Action:
    ☐ Complete TIA for each vendor (assess CLOUD Act conflict with GDPR)
    ☐ Document supplementary measures (CMK, EU Boundary, data minimization)
    ☐ DPO review and approval of each TIA
  Owner: DPO (with Legal/Security support)
  Deadline: 15.03.2026 (45 days)
  Evidence: TIA documents in Evidence Register

CONDITION 2: Deploy Customer-Managed Keys (CMK)
  Issue: 3 vendors with High jurisdictional risk, no CMK
  Vendors: Vendor B, Vendor D, Vendor F
  Data: Confidential customer data
  Risk: CLOUD Act exposure, vendor can decrypt data
  
  Required Action:
    ☐ Deploy CMK for all 3 vendors
    ☐ Verify CMK covers primary data AND backups
    ☐ Test key revocation (vendor cannot access data)
  Owner: Security (DPO verification)
  Deadline: 28.02.2026 (30 days)
  Evidence: CMK configuration screenshots

CONDITION 3: GDPR Violation Remediation (URGENT)
  Issue: Vendor H transferring to US without SCCs
  Discovery: Data residency review revealed undocumented transfer
  Risk: Article 44 violation (transfer without adequate safeguards)
  
  Required Action:
    ☐ Execute SCCs with Vendor H immediately (within 7 days)
    ☐ Complete TIA for Vendor H transfer
    ☐ If vendor refuses SCCs: Suspend service until compliant
  Owner: Legal + DPO
  Deadline: 05.02.2026 (7 days - URGENT)
  Evidence: Executed SCCs

STATUS: APPROVED WITH CONDITIONS

Assessment may proceed to CISO, but DPO CONDITIONS are MANDATORY.
Condition 3 is URGENT (GDPR violation risk).

If CONDITIONS NOT MET:
  - Condition 1: Regulatory audit risk (Schrems II non-compliance)
  - Condition 2: High CLOUD Act exposure (data accessible to US government)
  - Condition 3: Active GDPR violation (must fix immediately)

Condition Tracking: DPO monthly review until all complete.

Next DPO Review: Q2 2026 + Condition verification
```

**Outcome 3: Rejected**
```
DPO Review - REJECTED

Review Date: 29.01.2026
Reviewed By: Maria Garcia, Data Protection Officer

DATA PROTECTION COMPLIANCE: Non-Compliant
CROSS-BORDER TRANSFER STATUS: Rejected
JURISDICTIONAL RISK: Unacceptable

CRITICAL ISSUES PREVENTING APPROVAL:

ISSUE 1: Multiple GDPR Violations
  Problem: 
    - 4 vendors processing EU personal data without DPAs
    - 3 vendors transferring to US without SCCs
    - 2 vendors with expired/old SCCs (pre-Schrems II)
  
  GDPR Articles Violated:
    - Article 28: Processor agreements missing
    - Article 44: Transfers without safeguards
    - Article 46: SCCs not current
  
  Regulatory Risk: HIGH - potential GDPR fines (up to €20M or 4% revenue)
  
  Required Before Re-Submission:
    ☐ Execute DPAs with all 4 vendors (Article 28)
    ☐ Execute SCCs with all 3 vendors transferring to US
    ☐ Update old SCCs to post-Schrems II version (2021+)
    ☐ DPO review and approval of all DPAs/SCCs
    ☐ Evidence: Executed agreements in Evidence Register

ISSUE 2: Jurisdictional Risk Underestimated
  Problem: Assessment rates vendors as "Low Risk" despite clear CLOUD Act exposure
  Example: US vendor, Restricted data, provider-managed keys → Rated "Low Risk" (WRONG)
  Reality: Should be "Critical Risk"
  
  Root Cause: Risk assessment methodology not followed
  
  Required Before Re-Submission:
    ☐ Re-assess ALL jurisdictional risks using proper methodology
    ☐ Risk ratings must be realistic (not optimistic)
    ☐ High/Critical risks require compensating controls OR risk acceptance
    ☐ CISO/DPO approval for all High/Critical jurisdictional risks

ISSUE 3: No Transfer Impact Assessments
  Problem: 15 US vendors, ZERO TIAs completed
  Schrems II Requirement: TIA required for ALL transfers to US
  Current State: Non-compliant with EDPB guidance
  
  Required Before Re-Submission:
    ☐ Complete TIA for ALL US vendors processing personal data
    ☐ TIAs must assess CLOUD Act conflict with GDPR
    ☐ Document supplementary measures for each vendor
    ☐ DPO approval of adequacy determination
    ☐ Evidence: TIA documents for all US vendors

STATUS: REJECTED - Major Data Protection Violations

Assessment has FUNDAMENTAL data protection compliance issues.
Cannot proceed to CISO approval - legal/regulatory risk too high.

DO NOT SUBMIT TO CISO until DPO re-approval obtained.

Estimated Remediation Time: 4-8 weeks
  - DPA/SCC execution: 2-4 weeks (vendor negotiation)
  - TIA completion: 2-3 weeks (legal analysis)
  - Jurisdictional risk re-assessment: 1 week

Re-submit to DPO when ALL ISSUES resolved with documented evidence.

This is not negotiable - data protection compliance is mandatory.
```

---

### Step 5: CISO Final Approval

**CISO's Role:** Overall security risk acceptance and strategic decision-making

#### What CISO Reviews
```
CISO REVIEW CHECKLIST:

SHEET 8: SUMMARY DASHBOARD

☐ Overall Compliance Acceptable
   - Compliance percentage ≥85%? (target)
   - Trend improving or stable (not declining)?

☐ Critical/High Services Compliance
   - 100% of Critical services compliant (or gaps with plans)?
   - High services compliance ≥90%?

☐ Risk Distribution
   - Critical risk vendors: 0 (or documented risk acceptance)
   - High risk vendors: <10%
   - Medium/Low risk: 90%+

☐ Gap Remediation
   - All gaps have owners and deadlines?
   - Remediation plans realistic?
   - Resources allocated for gap closure?

PREVIOUS APPROVER REVIEWS:

☐ Legal Comments Review
   - Legal raised concerns? (assess severity)
   - Legal conditions reasonable and tracked?
   - Any legal escalations requiring CISO decision?

☐ Procurement Comments Review
   - Vendor performance issues noted? (assess impact)
   - SLA breaches concerning? (pattern or isolated?)
   - Vendor replacements recommended? (assess feasibility)

☐ DPO Comments Review
   - Data protection compliance adequate?
   - CLOUD Act risks acceptable?
   - Any regulatory violations flagged?

RISK ACCEPTANCE DECISIONS:

☐ Review Risk Register References (Column M)
   - What risks are being accepted?
   - Are risk ratings appropriate?
   - Are compensating controls adequate?
   - Duration of risk acceptance (temporary vs. permanent)?

☐ High/Critical Jurisdictional Risks
   - US vendors with Confidential/Restricted data?
   - CMK deployed or migration planned?
   - Risk acceptance justified?

STRATEGIC CONSIDERATIONS:

☐ Vendor Concentration
   - Over-reliance on single vendor (AWS, Microsoft)?
   - Diversification strategy needed?

☐ Cost vs. Security Trade-Offs
   - Are we paying for security we don't use (overprovisioned)?
   - Are we under-invested in security (cheap but risky vendors)?

☐ Alignment with Organization Strategy
   - Cloud-first strategy supported?
   - Multi-cloud strategy viable?
   - Hybrid approach needed?
```

#### CISO Review Outcomes

**Outcome 1: Approved**
```
CISO Review - APPROVED

Review Date: 31.01.2026
Reviewed By: Dr. James Chen, Chief Information Security Officer

OVERALL SECURITY POSTURE: Acceptable
RISK ACCEPTANCE REQUIRED: No (all risks adequately mitigated)
GAP REMEDIATION PLANS ADEQUATE: Yes

ASSESSMENT SUMMARY:
  Total Vendors: 47
  Overall Compliance: 87%
  Critical/High Services Compliance: 95% (19/20)
  
  Risk Distribution:
    - Critical Risk: 0
    - High Risk: 3 (6%)
    - Medium Risk: 10 (21%)
    - Low Risk: 34 (72%)

PREVIOUS APPROVER REVIEWS:
  ✓ Legal: Approved with minor conditions (tracked)
  ✓ Procurement: Approved (SLA escalations in progress)
  ✓ DPO: Approved (data protection compliant)

KEY FINDINGS:

STRENGTHS:
  + Strong vendor certification coverage (89% ISO 27001 or SOC 2)
  + Good data sovereignty compliance (94%)
  + CLOUD Act risks properly assessed and mitigated
  + Comprehensive evidence collection (91% collected)
  + Active vendor management (SLA tracking, performance reviews)

AREAS FOR IMPROVEMENT:
  • 1 Critical service (Vendor XYZ) without certification
    - Remediation: Vendor obtaining ISO 27001 by 30.06.2026
    - Interim: Enhanced monitoring, penetration testing
    - Acceptable: Low-risk improvement timeline
  
  • 3 High-risk vendors (jurisdictional)
    - All have CMK deployed (mitigated)
    - Risk level acceptable with compensating controls

STRATEGIC OBSERVATIONS:
  - Vendor concentration: 60% spend on AWS/Azure/Microsoft (acceptable for infrastructure)
  - Security investment: Appropriate for organization size and risk appetite
  - Cloud strategy: Well-aligned with cloud-first approach

APPROVAL CONDITIONS (MINOR):
  1. Vendor XYZ ISO 27001 by 30.06.2026 OR vendor replacement
     - Progress review: Monthly CISO meeting
     - Fallback: Replacement vendor identified (migration plan ready if needed)
  
  2. Continue quarterly vendor assessments (maintain quality)
     - Next review: Q2 2026
     - Focus: Certificate renewals, SLA performance trends

STATUS: APPROVED - Assessment is Audit Ready

The vendor due diligence program is well-executed and demonstrates mature
vendor risk management. The organization has good visibility into vendor
security posture and data protection compliance.

Minor conditions do not prevent audit readiness - they are tracked improvement
items with reasonable timelines.

AUDIT READINESS: ✓ Approved for external audit presentation

Next CISO Review: Q2 2026 (quarterly cycle)
Condition Tracking: Monthly CISO meeting agenda
```

**Outcome 2: Approved with Conditions**
```
CISO Review - APPROVED WITH CONDITIONS

Review Date: 31.01.2026
Reviewed By: Dr. James Chen, Chief Information Security Officer

OVERALL SECURITY POSTURE: Acceptable with Gaps
RISK ACCEPTANCE REQUIRED: Yes (2 cases)
GAP REMEDIATION PLANS ADEQUATE: Partially

CRITICAL CONDITIONS REQUIRING CISO ATTENTION:

CONDITION 1: Critical Service Without Adequate Security (Risk Acceptance Required)
  Service: Vendor ABC (Critical Backup Service)
  Issue: No ISO 27001, no SOC 2, vendor refuses to obtain
  Data: Confidential backup data (entire organization)
  Current State: Non-compliant
  
  CISO Decision Required:
    Option A: ACCEPT RISK (document in risk register)
      - Compensating controls: Encryption, limited retention, monitoring
      - Risk acceptance duration: 12 months (re-evaluate annually)
      - Risk ID: RISK-2026-089
      - Sign-off: CISO + CIO (backup criticality)
    
    Option B: VENDOR REPLACEMENT (migration)
      - Timeline: 6-9 months (complex backup migration)
      - Cost: ~CHF 200K (migration + transition)
      - Alternative vendor: Vendor XYZ (ISO 27001 certified)
    
  CISO DECISION: _________________________ (Select A or B)
  
  If Option A: Risk Acceptance Form EV-VDD-190 (execute immediately)
  If Option B: Migration project charter by 28.02.2026

CONDITION 2: High Jurisdictional Risks - CMK Deployment Urgent
  Issue: 3 vendors with Confidential data, no CMK, High CLOUD Act risk
  Vendors: Vendor D, Vendor F, Vendor H
  DPO Condition: CMK deployment by 28.02.2026 (from DPO review)
  
  CISO Oversight Required:
    ☐ Security team assigned (resource allocation confirmed)
    ☐ CMK deployment project plan reviewed and approved
    ☐ Weekly progress reviews (CISO standing meeting)
    ☐ Escalation path if vendor technical issues
  
  Deadline: 28.02.2026 (FIRM - DPO requirement)
  Risk if Delayed: GDPR TIA inadequacy, regulatory audit risk

CONDITION 3: Vendor Performance - Escalation Required
  Issue: Vendor B (High criticality) - 5 SLA breaches, declining performance
  Procurement Condition: Executive escalation, improvement plan
  
  CISO Decision Point:
    - If no improvement by Q2 2026 → Vendor replacement
    - Replacement evaluation must start NOW (parallel track)
    - Budget: Allocate CHF 50K for potential migration
  
  Required Actions:
    ☐ Procurement: Vendor B executive escalation (complete)
    ☐ Procurement: Identify replacement vendors (by 15.02.2026)
    ☐ Security: Evaluate replacement vendor security (by 28.02.2026)
    ☐ CISO: Go/No-Go decision on replacement (01.03.2026)

STATUS: APPROVED WITH CONDITIONS

Assessment demonstrates good overall vendor management, but CRITICAL CONDITIONS
require CISO decision and active oversight.

Condition 1 is strategic (accept risk vs. vendor replacement)
Condition 2 is tactical (CMK deployment on tight timeline)
Condition 3 is operational (vendor performance management)

AUDIT READINESS: ✓ Conditional
  - Can present to auditors WITH risk acceptance documentation
  - Conditions do not prevent audit, but must be explained
  - Auditors will verify condition tracking and remediation progress

REQUIRED BEFORE Q2 2026 REVIEW:
  ☐ Condition 1: Risk acceptance executed OR migration started
  ☐ Condition 2: CMK deployed and verified (DPO sign-off)
  ☐ Condition 3: Vendor B improvement OR replacement in progress

Condition Tracking: Weekly CISO meeting (standing agenda item)
Next CISO Review: Q2 2026 + Condition verification milestone reviews
```

**Outcome 3: Rejected**
```
CISO Review - REJECTED

Review Date: 31.01.2026
Reviewed By: Dr. James Chen, Chief Information Security Officer

OVERALL SECURITY POSTURE: Unacceptable
GAP REMEDIATION PLANS: Inadequate

CRITICAL ISSUES PREVENTING APPROVAL:

ISSUE 1: Critical Services from Non-Compliant Vendors (UNACCEPTABLE RISK)
  Problem: 
    - 3 Critical services from vendors with NO security certifications
    - Vendors: Vendor A (CRM), Vendor C (Finance), Vendor E (HR)
    - Data: Confidential and Restricted organizational data
    - No ISO 27001, No SOC 2, No compensating controls
  
  Current Assessment: Gaps noted but marked "acceptable with remediation"
  CISO Assessment: NOT ACCEPTABLE - regulatory and business risk too high
  
  Required Before Re-Submission:
    Critical services MUST have:
      ☐ Vendor ISO 27001 OR SOC 2 Type II certification OR
      ☐ Formal risk acceptance (CISO + Board for Restricted data) OR
      ☐ Vendor replacement in progress (migration plan with timeline)
    
    "Remediation plan: vendor will get ISO 27001 eventually" is NOT sufficient.
    Need CONCRETE milestones, fallback plans, and executive accountability.

ISSUE 2: GDPR Violations Not Addressed (DPO Raised, Not Fixed)
  Problem:
    - DPO identified GDPR violations (missing DPAs, no SCCs)
    - Assessment marked "Approved" by Legal (but DPO concerns ignored)
    - Coordinator proceeded to CISO without fixing violations
  
  Process Failure: Cannot proceed to CISO if DPO rejects
  Legal/Regulatory Risk: Active GDPR violations = regulatory fines + audit failure
  
  Required Before Re-Submission:
    ☐ Return to DPO
    ☐ Fix ALL GDPR violations (DPAs, SCCs, TIAs)
    ☐ Obtain DPO approval
    ☐ THEN re-submit to CISO

ISSUE 3: Gap Remediation Plans Unrealistic
  Problem: 
    - 15 gaps identified
    - All marked "remediation in progress"
    - No owners, no deadlines, no milestones, no resources
  
  Example: "Vendor will improve SLA performance"
    - No improvement plan from vendor
    - No timeline
    - No escalation if vendor doesn't improve
    - No replacement vendor identified
  
  This is "hope-based remediation" not risk management.
  
  Required Before Re-Submission:
    For EACH gap:
      ☐ Specific remediation action (not vague "will improve")
      ☐ Assigned owner (person responsible, not "team")
      ☐ Target date (realistic, not aspirational)
      ☐ Resources allocated (budget, time, tools)
      ☐ Fallback plan if remediation fails
      ☐ CISO approval of remediation approach

ISSUE 4: Lack of Executive Accountability
  Problem: Assessment presented as "ready for audit" but has major gaps
  
  Indicates:
    - Coordinator doesn't understand risk severity
    - Stakeholders rubber-stamped without thorough review
    - No executive oversight of assessment quality
  
  Required Before Re-Submission:
    ☐ Executive sponsor (CIO or equivalent) reviews assessment
    ☐ Gaps triaged by severity (Critical/High/Medium/Low)
    ☐ Critical gaps have C-level owner (not mid-level manager)
    ☐ Realistic timeline for fixes (not "everything in 30 days")

STATUS: REJECTED - Major Remediation Required

This assessment has fundamental issues that prevent CISO approval:
  1. Unacceptable risks (Critical services without assurance)
  2. Regulatory violations (GDPR non-compliance)
  3. Inadequate remediation plans (no accountability)
  4. Process failures (DPO concerns ignored)

AUDIT READINESS: ✗ NOT READY
  - Would fail external audit in current state
  - Auditor would identify same issues CISO identified
  - Cannot present until major gaps remediated

REQUIRED TIMELINE:
  Estimated remediation: 6-12 weeks
    - Issue 1: Vendor certifications OR replacements (4-8 weeks)
    - Issue 2: GDPR compliance (DPA/SCC execution) (2-4 weeks)
    - Issue 3: Proper gap remediation plans (1-2 weeks)
    - Issue 4: Executive engagement and accountability (1 week)

DO NOT RE-SUBMIT until ALL ISSUES addressed.

Schedule CISO pre-review meeting before formal re-submission to validate
remediation approach.

This is not a "minor fix" - this requires substantial rework.
```

---

### Handling Rejections

**If assessment is rejected by any approver:**
```
REJECTION RESPONSE PROCESS:

Step 1: Understand the Rejection (24 hours)
  ☐ Read rejection comments thoroughly
  ☐ Identify all issues raised (categorize by severity)
  ☐ Clarify any unclear feedback (meet with approver if needed)
  ☐ Assess remediation effort (hours, weeks, resources)

Step 2: Triage Issues (48 hours)
  ☐ Critical issues (must fix to proceed)
  ☐ High issues (should fix, may negotiate)
  ☐ Medium issues (nice to fix, can document as limitation)
  
  Focus on CRITICAL issues first - don't get lost in minor details.

Step 3: Develop Remediation Plan (1 week)
  For EACH critical issue:
    ☐ Root cause (why did this happen?)
    ☐ Remediation action (specific, actionable)
    ☐ Owner (who will fix it)
    ☐ Timeline (realistic estimate)
    ☐ Resources needed (people, budget, access)
    ☐ Verification method (how to prove it's fixed)

Step 4: Execute Remediation (varies by issue)
  ☐ Fix issues systematically (don't rush)
  ☐ Document fixes (evidence of remediation)
  ☐ Track progress (update issue log)
  ☐ Test fixes (verify they work)

Step 5: Quality Check (before re-submission)
  ☐ All critical issues addressed?
  ☐ Evidence of fixes documented?
  ☐ Self-review against rejection criteria (did we actually fix it?)
  ☐ Internal review (have colleague verify fixes)

Step 6: Re-Submit with Remediation Summary
  Include cover memo:
    "Re-Submission: ISMS-IMP-A.5.23.S2 Vendor Due Diligence Assessment
     
     Previous Status: Rejected by [Legal/Procurement/DPO/CISO] on [Date]
     
     Rejection Issues Addressed:
       Issue 1: [Description]
         Remediation: [What we did to fix it]
         Evidence: [EV-VDD-XXX, updated Sheet Y]
       
       Issue 2: [Description]
         Remediation: [What we did]
         Evidence: [Reference]
     
     Changes Made:
       - Sheet 3: Updated contract analysis (Legal review complete)
       - Sheet 5: Added missing DPAs (all executed)
       - Evidence Register: Added 15 new items
     
     Request: Please re-review for approval.
     
     Thank you,
     [Coordinator]"

Step 7: Learn from Rejection
  ☐ What process failures led to rejection?
  ☐ How to prevent in future assessments?
  ☐ Update assessment process based on lessons learned
```

---

### Tracking Approvals to Completion

**Approval Tracking Dashboard:**
```
APPROVAL WORKFLOW TRACKER

Assessment: ISMS-IMP-A.5.23.S2 - Vendor Due Diligence & Contracts
Start Date: 20.01.2026
Target Completion: 10.02.2026

┌──────────────┬─────────────┬──────────┬──────────────┬─────────────┐
│ Approver     │ Submit Date │ Status   │ Decision     │ Complete    │
├──────────────┼─────────────┼──────────┼──────────────┼─────────────┤
│ Legal        │ 23.01.2026  │ Complete │ Approved     │ 25.01.2026  │
│ Procurement  │ 25.01.2026  │ Complete │ Approved     │ 27.01.2026  │
│ DPO          │ 27.01.2026  │ Complete │ Approved (C) │ 29.01.2026  │
│ CISO         │ 29.01.2026  │ In Review│ -            │ -           │
└──────────────┴─────────────┴──────────┴──────────────┴─────────────┘

Legend:
  Approved = No conditions
  Approved (C) = Approved with Conditions
  Rejected = Remediation required

CONDITIONS TRACKER (from DPO):

Condition 1: Complete TIAs for 5 US vendors
  Owner: DPO (with Legal/Security)
  Deadline: 15.03.2026
  Status: In Progress (2/5 complete)
  Next Milestone: 3rd TIA by 15.02.2026

Condition 2: Deploy CMK for 3 vendors
  Owner: Security
  Deadline: 28.02.2026
  Status: In Progress (1/3 complete)
  Next Milestone: Vendor B CMK by 15.02.2026

TIMELINE:
  20.01.2026: Assessment completed
  23.01.2026: Submitted to Legal
  25.01.2026: Legal approved, submitted to Procurement
  27.01.2026: Procurement approved, submitted to DPO
  29.01.2026: DPO approved with conditions, submitted to CISO
  31.01.2026: CISO approval expected
  01.02.2026: Assessment status: APPROVED WITH CONDITIONS

OVERALL STATUS: ON TRACK
```

---

**END OF SECTION 8: REVIEW & APPROVAL PROCESS**

## Section 9: Integration & Maintenance

### 9.1 Integration with Other ISMS Assessments

**Critical Context:** This assessment (ISMS-IMP-A.5.23.S2) is ONE component of the comprehensive A.5.19-23 supplier/cloud security framework. It does not operate in isolation.

#### Integration Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                   A.5.19-23 FRAMEWORK OVERVIEW                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐         │
│  │  IMP-5.23.1  │ → │  IMP-5.23.2  │ ← │  IMP-5.23.3  │         │
│  │  Inventory   │   │  THIS DOC    │   │  Secure      │         │
│  │              │   │  Vendor DD   │   │  Config      │         │
│  └──────────────┘   └──────────────┘   └──────────────┘         │
│         │                   │                   │                │
│         └───────────────────┼───────────────────┘                │
│                             ▼                                    │
│                   ┌──────────────────┐                           │
│                   │   IMP-5.23.5     │                           │
│                   │   Compliance     │                           │
│                   │   Dashboard      │                           │
│                   └──────────────────┘                           │
│                             ▲                                    │
│         ┌───────────────────┼───────────────────┐                │
│         │                   │                   │                │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐         │
│  │  IMP-5.23.4  │   │              │   │   Related    │         │
│  │  Governance  │   │              │   │   Controls   │         │
│  │  & Risk Mgmt │   │              │   │   (A.8.x)    │         │
│  └──────────────┘   └──────────────┘   └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
```

#### Upstream Dependencies (Data Flows IN)

**From IMP-A.5.23.1 (Cloud Service Inventory):**

| Data Element | Usage in This Assessment | Update Trigger |
|--------------|-------------------------|----------------|
| Cloud Service Name | Sheet 2: Vendor identification | New service added |
| Service Provider | Sheet 2: Vendor name | Provider change |
| Service Criticality | Sheet 3: Contract risk rating | Criticality reclassification |
| Data Classification | Sheet 5: Data sovereignty requirements | Data sensitivity change |
| Annual Spend | Sheet 4: SLA penalty proportionality | Budget revision |
| Service Owner | Sheet 10: Approval routing | Org chart change |

**Integration Process:**

1. **Weekly Automated Sync** (if systems integrated):
   - Export vendor list from IMP-5.23.1 → Import into IMP-5.23.2 Sheet 2
   - Flag new vendors requiring due diligence
   - Flag decommissioned vendors for contract termination

2. **Manual Sync** (if no integration):
   - Monthly export/import cycle
   - Use "Vendor Name" as unique key
   - Document sync date in Sheet 9 (Evidence Register)

**IMPLEMENTER PERSPECTIVE:**
*Create a simple CSV export from IMP-5.23.1 that can be imported into IMP-5.23.2. This prevents duplicate data entry and ensures consistency.*

**AUDITOR PERSPECTIVE:**
*Verify that ALL vendors in the inventory have corresponding due diligence records. Any vendor without a complete Sheet 2-7 assessment is a compliance gap.*

---

#### Downstream Dependencies (Data Flows OUT)

**To IMP-A.5.23.3 (Secure Configuration & Deployment):**

| Data Element | Downstream Usage | Quality Requirement |
|--------------|------------------|---------------------|
| Vendor Security Certifications (Sheet 2) | Baseline security posture for config standards | ISO 27001 or SOC 2 Type II verified |
| Contract Terms (Sheet 3) | Configuration change approval requirements | MSA change control clauses identified |
| SLA Requirements (Sheet 4) | Performance monitoring thresholds | Specific SLA metrics defined |
| Data Residency Rules (Sheet 5) | Regional deployment constraints | Data sovereignty requirements documented |
| Audit Rights (Sheet 6) | Configuration audit schedules | Right-to-audit clauses confirmed |

**Integration Process:**

**After completing IMP-5.23.2:**
1. Export Sheet 8 (Summary Dashboard) → Import into IMP-5.23.3 "Vendor Baseline" sheet
2. Flag HIGH risk vendors (Sheet 8 risk score ≥ 7) for enhanced configuration controls
3. Use Sheet 5 data residency rules as MANDATORY constraints in IMP-5.23.3 deployment planning

**IMPLEMENTER PERSPECTIVE:**
*Don't start deploying/configuring a cloud service until due diligence is complete. Sheet 8 risk score determines the level of configuration hardening required.*

**AUDITOR PERSPECTIVE:**
*Verify traceability: HIGH risk vendor → Enhanced configuration controls documented in IMP-5.23.3.*

---

**To IMP-A.5.23.4 (Ongoing Governance & Risk Management):**

| Data Element | Downstream Usage | Update Frequency |
|--------------|------------------|------------------|
| Contract Renewal Dates (Sheet 3) | Proactive renewal planning | 90 days before renewal |
| SLA Performance History (Sheet 4) | Vendor performance trending | Monthly |
| Jurisdictional Risk Assessment (Sheet 7) | Risk register updates | When geopolitical events occur |
| Approval Status (Sheet 10) | Governance oversight tracking | Per approval workflow |

**Integration Process:**

1. **Quarterly:** Export Sheet 4 SLA performance → Import into IMP-5.23.4 "Vendor Scorecard"
2. **Monthly:** Review Sheet 3 contract renewal dates → Trigger 90-day renewal process in IMP-5.23.4
3. **Event-Driven:** Sheet 7 jurisdictional risk changes → Update IMP-5.23.4 risk register

**IMPLEMENTER PERSPECTIVE:**
*Set calendar reminders based on Sheet 3 renewal dates. Use Sheet 4 SLA performance to drive vendor improvement discussions in IMP-5.23.4 governance meetings.*

**AUDITOR PERSPECTIVE:**
*Verify that SLA failures documented in Sheet 4 trigger formal remediation actions in IMP-5.23.4. Check that contract renewals don't happen automatically without due diligence refresh.*

---

**To IMP-A.5.23.5 (Compliance Monitoring Dashboard):**

| Data Element | Dashboard Usage | Aggregation Method |
|--------------|-----------------|-------------------|
| Overall Compliance % (Sheet 8) | Vendor due diligence compliance metric | Average across all vendors |
| HIGH Risk Vendors (Sheet 8) | Executive risk summary | Count + vendor names |
| Missing Evidence (Sheet 9) | Evidence gap tracking | Count per evidence type |
| Pending Approvals (Sheet 10) | Workflow bottleneck identification | Count per approver |

**Integration Process:**

**Weekly (or on-demand):**
1. Export Sheet 8 compliance metrics → Import into IMP-5.23.5 "Vendor DD Compliance" tile
2. Export HIGH risk vendors → Display in IMP-5.23.5 "Top Risks" dashboard section
3. Export missing evidence count → Track in IMP-5.23.5 "Evidence Gaps" KPI

**IMPLEMENTER PERSPECTIVE:**
*The compliance dashboard (IMP-5.23.5) should show vendor due diligence status at a glance. GREEN = all vendors assessed, AMBER = assessments in progress, RED = overdue assessments.*

**AUDITOR PERSPECTIVE:**
*The dashboard provides audit trail of continuous compliance monitoring. Verify that dashboard metrics match underlying data in this workbook.*

---

### 9.2 Integration with Organizational Systems

Beyond the ISMS assessment suite, this workbook integrates with operational systems.

#### 9.2.1 Configuration Management Database (CMDB)

**Integration Point:** Cloud services in the CMDB should reference this assessment.

**Data Flow:**
```
IMP-5.23.2 (This Workbook)          CMDB
┌────────────────────────┐         ┌────────────────────────┐
│ Vendor: AWS            │   →     │ CI: AWS EC2 Production │
│ Cert: ISO 27001 ✓      │         │ Attributes:            │
│ Risk: MEDIUM           │         │   - Vendor: AWS        │
│ Contract: 01.06.2026   │         │   - Risk Level: MEDIUM │
│ Data Residency: EU     │         │   - Cert Status: Valid │
└────────────────────────┘         │   - Contract Exp: DATE │
                                   └────────────────────────┘
```

**Integration Method:**

1. **Manual:** Export Sheet 2 vendor summary → Import into CMDB vendor table
2. **API-Driven (Advanced):** CMDB queries this Excel workbook via script
3. **Shared Database:** Both systems read/write to central vendor DB

**IMPLEMENTER PERSPECTIVE:**
*Keep CMDB vendor attributes synchronized with Sheet 2. When contract expires in this workbook, CMDB should reflect "Contract Review Required."*

**AUDITOR PERSPECTIVE:**
*Verify that CMDB vendor risk ratings match Sheet 8 risk scores. Inconsistency indicates stale data in one system.*

---

#### 9.2.2 Procurement/Vendor Management System

**Integration Point:** Contract lifecycle management.

**Data Flow:**
```
Procurement System              IMP-5.23.2 (This Workbook)
┌──────────────────────┐       ┌──────────────────────────┐
│ Purchase Order: PO123│  →    │ Sheet 3: Contract Terms  │
│ Vendor: Cloudflare   │       │   - MSA Reference: PO123 │
│ Contract Start: DATE │       │   - Term: 3 years        │
│ Renewal Date: DATE   │       │   - Auto-Renewal: NO     │
└──────────────────────┘       └──────────────────────────┘
          ↑                                   │
          └───────────────────────────────────┘
             Sheet 3 renewal alert triggers
             procurement workflow 90 days early
```

**Integration Method:**

1. **Sheet 3 Contract Reference Field:** Link to procurement system PO/contract number
2. **Renewal Alerts:** Export Sheet 3 renewal dates → Import into procurement calendar
3. **Two-Way Sync:** Procurement system updates contract terms → Refresh Sheet 3

**IMPLEMENTER PERSPECTIVE:**
*Use procurement system as source of truth for contract dates, but track security-specific clauses (DPA, audit rights) in Sheet 3 of this workbook.*

**AUDITOR PERSPECTIVE:**
*Verify that contracts referenced in Sheet 3 actually exist in procurement system. Missing contracts = unapproved vendor usage.*

---

#### 9.2.3 IT Service Management (ITSM) / Ticketing System

**Integration Point:** Vendor incidents and change requests.

**Data Flow:**
```
ITSM Incident                    IMP-5.23.2 (This Workbook)
┌──────────────────────┐        ┌──────────────────────────┐
│ INC-456: AWS Outage  │   →    │ Sheet 4: SLA Performance │
│ Vendor: AWS          │        │   - Incident: INC-456    │
│ Downtime: 3.2 hours  │        │   - SLA Breach: YES      │
│ Date: 15.11.2025     │        │   - Penalty: €5,000      │
└──────────────────────┘        └──────────────────────────┘
```

**Integration Method:**

1. **Monthly Export:** ITSM vendor incidents → Import into Sheet 4 SLA tracking
2. **Automated Alert:** ITSM SLA breach triggers Sheet 4 update + vendor escalation
3. **Performance Trending:** Sheet 4 quarterly report feeds back to ITSM for vendor performance dashboards

**IMPLEMENTER PERSPECTIVE:**
*Don't manually track SLA breaches if ITSM already captures them. Export ITSM data monthly and import into Sheet 4.*

**AUDITOR PERSPECTIVE:**
*Cross-check Sheet 4 SLA performance data against ITSM incident records. Verify that penalties were invoiced per Sheet 4 calculations.*

---

#### 9.2.4 Contract Management System

**Integration Point:** Legal document repository.

**Data Flow:**
```
Contract Mgmt System            IMP-5.23.2 (This Workbook)
┌──────────────────────┐       ┌──────────────────────────┐
│ MSA: AWS-2024-001    │  ↔    │ Sheet 9: Evidence Reg.   │
│ Location: SharePoint │       │   - MSA Link: [URL]      │
│ Version: 3.1         │       │   - DPA Link: [URL]      │
│ Last Review: DATE    │       │   - SLA Link: [URL]      │
└──────────────────────┘       └──────────────────────────┘
```

**Integration Method:**

1. **Sheet 9 Hyperlinks:** Link directly to contracts in document management system
2. **Version Control:** Sheet 9 tracks contract version numbers
3. **Renewal Workflow:** Contract system triggers Sheet 3 renewal process

**IMPLEMENTER PERSPECTIVE:**
*Store contracts in a central repository (SharePoint, legal system). Sheet 9 contains LINKS to contracts, not copies.*

**AUDITOR PERSPECTIVE:**
*Click every hyperlink in Sheet 9 to verify contracts are accessible and current. Broken links = evidence gap.*

---

### 9.3 Quarterly Maintenance Procedures

**Frequency:** Every 3 months (aligned with IMP-5.23.5 reporting cycle)

**Maintenance Owner:** Security Compliance Team (with Legal/Procurement support)

#### Quarterly Maintenance Checklist

**Week 1 of Quarter: Data Refresh**
```
☐ Import latest vendor list from IMP-5.23.1
  ├─ Identify new vendors requiring initial assessment
  ├─ Identify decommissioned vendors for archive
  └─ Update Sheet 2 vendor roster

☐ Review Sheet 3 contract renewal dates
  ├─ Flag contracts expiring in next 90 days
  ├─ Trigger renewal process for flagged contracts
  └─ Update procurement system with renewal schedule

☐ Refresh Sheet 2 vendor certifications
  ├─ Check vendor portals for updated certs (ISO, SOC 2)
  ├─ Download new certification PDFs
  ├─ Update Sheet 9 evidence links
  └─ Flag expired certifications for vendor follow-up
```

**Week 2 of Quarter: SLA Performance Review**
```
☐ Import ITSM incident data into Sheet 4
  ├─ Categorize by vendor
  ├─ Calculate SLA breach counts
  ├─ Compute penalty amounts per contract terms
  └─ Generate vendor performance trend report

☐ Vendor Performance Meetings
  ├─ Schedule quarterly business reviews (QBRs) with key vendors
  ├─ Present Sheet 4 performance data
  ├─ Document improvement commitments
  └─ Update Sheet 4 "Vendor Response" column
```

**Week 3 of Quarter: Risk & Compliance Updates**
```
☐ Review Sheet 7 jurisdictional risk assessments
  ├─ Check for geopolitical changes (sanctions, export controls)
  ├─ Update CLOUD Act risk ratings if US policy changes
  ├─ Re-assess vendors in high-risk jurisdictions
  └─ Escalate new HIGH risks to CISO

☐ Regulatory Compliance Check
  ├─ Verify DORA requirements for critical ICT vendors (Sheet 3)
  ├─ Verify NIS2 requirements for essential service vendors (Sheet 3)
  ├─ Update Sheet 6 audit schedules if reg requirements changed
  └─ Document compliance status in Sheet 8
```

**Week 4 of Quarter: Evidence Validation**
```
☐ Sheet 9 Evidence Register Audit
  ├─ Click all hyperlinks to verify documents accessible
  ├─ Check document modification dates (ensure current)
  ├─ Download missing evidence from vendors
  ├─ Update evidence repository with new documents
  └─ Mark evidence status: Complete / Pending / Expired

☐ Export to IMP-5.23.5 Dashboard
  ├─ Generate Sheet 8 summary metrics
  ├─ Export compliance % to dashboard
  ├─ Export HIGH risk vendor list
  └─ Archive snapshot of this quarter's workbook
```

**IMPLEMENTER PERSPECTIVE:**
*Set recurring calendar reminders for quarterly maintenance. Automate data imports where possible to reduce manual work.*

**AUDITOR PERSPECTIVE:**
*Review quarterly maintenance logs. Verify that maintenance actually occurred (evidence: updated workbook timestamps, meeting notes, vendor correspondence).*

---

### 9.4 Annual Comprehensive Review

**Frequency:** Once per year (recommended: Q4 to prepare for audit)

**Purpose:** 
- Full re-validation of all vendor assessments
- Major contract renegotiations
- Regulatory requirement updates
- Framework effectiveness review

#### Annual Review Process

**Month 1: Preparation**
```
☐ Inventory Check
  ├─ Cross-check IMP-5.23.1 against actual cloud usage
  ├─ Identify shadow IT (services in use but not in inventory)
  ├─ Add shadow IT to inventory and flag for immediate assessment
  └─ Document shadow IT findings in CISO report

☐ Stakeholder Survey
  ├─ Survey Legal: "Are contract terms still adequate?"
  ├─ Survey Procurement: "Are vendor costs optimized?"
  ├─ Survey Security: "Any new vendor security incidents?"
  ├─ Survey Compliance: "Any regulatory changes affecting vendors?"
  └─ Compile survey findings into improvement backlog
```

**Month 2: Deep-Dive Assessments**
```
☐ Re-assess ALL HIGH risk vendors (Sheet 8 risk ≥ 7)
  ├─ Request updated SOC 2 Type II reports
  ├─ Review past year's incident history
  ├─ Re-evaluate Sheet 7 jurisdictional risks
  ├─ Meet with vendor to discuss improvements
  └─ Update Sheet 2-7 with latest data

☐ Re-assess CRITICAL vendors (Tier 1 from IMP-5.23.1)
  ├─ Even if MEDIUM risk, critical vendors need annual review
  ├─ Verify disaster recovery plans still current
  ├─ Test audit rights (conduct sample vendor audit)
  ├─ Review SLA performance trends (Sheet 4)
  └─ Document findings in Sheet 8 "Annual Review Notes"

☐ Sample Audit of MEDIUM/LOW Risk Vendors
  ├─ Select 10% random sample
  ├─ Re-verify Sheet 2 certifications (download new certs)
  ├─ Spot-check Sheet 5 data residency (query vendor config)
  ├─ Confirm contracts still in force (check procurement system)
  └─ Document sample audit results
```

**Month 3: Framework Improvements**
```
☐ Policy/Process Updates
  ├─ Review ISMS-POL-A.5.19-23-S2 for needed updates
  ├─ Update assessment criteria if regulatory changes (DORA/NIS2)
  ├─ Revise Sheet column definitions if needed
  ├─ Update Python generator script if workbook structure changes
  └─ Version control: IMP-5.23.2 v2.1 → v3.0

☐ Integration Improvements
  ├─ Review integration points with CMDB/ITSM/Procurement
  ├─ Identify manual processes that could be automated
  ├─ Develop API integrations or scheduled exports
  ├─ Test integration workflows
  └─ Document integration procedures

☐ Training & Communication
  ├─ Train new Legal/Procurement/Security staff on workbook
  ├─ Refresh training for existing users
  ├─ Share annual review findings with leadership
  ├─ Present vendor performance trends to business units
  └─ Archive annual review report
```

**IMPLEMENTER PERSPECTIVE:**
*Annual review is time-consuming but critical. Plan for it. Don't do everything in December when everyone's on vacation. Start in October.*

**AUDITOR PERSPECTIVE:**
*Annual review provides the most comprehensive audit evidence. Verify that annual review actually happened (evidence: meeting minutes, updated workbook, stakeholder survey results, findings report).*

---

### 9.5 Continuous Improvement Cycle

**Philosophy:** This assessment framework is NOT static. It evolves based on:
- Lessons learned from vendor incidents
- Changes in regulatory requirements
- Feedback from stakeholders
- Technology evolution

#### Improvement Feedback Loop
```
┌──────────────────────────────────────────────────────────────┐
│                  CONTINUOUS IMPROVEMENT CYCLE                 │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐            │
│  │ COLLECT  │  →   │ ANALYZE  │  →   │ IMPROVE  │            │
│  │ FEEDBACK │      │ PATTERNS │      │ FRAMEWORK│            │
│  └──────────┘      └──────────┘      └──────────┘            │
│       ↑                                       │               │
│       │                                       ▼               │
│  ┌──────────┐                          ┌──────────┐          │
│  │IMPLEMENT │  ←                    ←  │  PLAN    │          │
│  │ CHANGES  │                          │ CHANGES  │          │
│  └──────────┘                          └──────────┘          │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

#### Feedback Collection Sources

**1. Vendor Incidents**

When a vendor security incident occurs:
```
Incident → Root Cause Analysis → Assessment Framework Review

Example:
  Incident: Vendor data breach (customer data exposed)
  Root Cause: DPA didn't require encryption at rest
  Framework Improvement: Add Sheet 3 column "Data Encryption Requirements"
  Implementation: Update Python generator, re-assess all vendors
```

**2. Audit Findings**

When internal/external auditors identify gaps:
```
Audit Finding → Gap Analysis → Framework Enhancement

Example:
  Finding: "No evidence of forensic readiness verification"
  Gap: Sheet 6 forensic rights documented but never tested
  Enhancement: Add Sheet 6 column "Last Forensic Test Date"
  Implementation: Conduct annual forensic readiness test
```

**3. Regulatory Changes**

When new regulations are enacted:
```
New Regulation → Requirement Mapping → Framework Update

Example:
  Regulation: DORA requires enhanced third-party risk management
  Requirement: ICT concentration risk assessment
  Framework Update: Add Sheet 7 "Vendor Concentration Risk" analysis
  Implementation: v1.0 release with DORA requirements
```

**4. Stakeholder Feedback**

When users of this workbook suggest improvements:
```
User Feedback → Usability Review → Framework Refinement

Example:
  Feedback: "Sheet 3 contract analysis takes too long"
  Usability Issue: Too many manual data entry fields
  Refinement: Pre-populate Sheet 3 with standard clauses, only exceptions need entry
  Implementation: Updated Python generator with clause templates
```

#### Improvement Prioritization

Not all improvements are equal. Prioritize based on:

| Priority | Criteria | Response Time |
|----------|----------|---------------|
| **CRITICAL** | Regulatory non-compliance, high risk to business | Immediate (within 1 week) |
| **HIGH** | Audit finding, major vendor incident | Within 1 month |
| **MEDIUM** | Usability improvement, process efficiency | Next quarterly update |
| **LOW** | Nice-to-have feature, cosmetic change | Next annual review |

**IMPLEMENTER PERSPECTIVE:**
*Track improvement requests in a backlog (Jira, Excel, whatever). Review backlog monthly. Don't let good ideas get lost.*

**AUDITOR PERSPECTIVE:**
*Verify that improvement backlog exists and is actively managed. Evidence of continuous improvement: version history, change logs, stakeholder meeting minutes.*

---

### 9.6 Change Management for Vendor Evolution

Vendors don't stay static. They get acquired, merge, sunset services, or radically change their offerings. This workbook must adapt.

#### Vendor Lifecycle Events

**Event 1: Vendor Acquisition / Merger**

**Scenario:** Microsoft acquires your vendor (e.g., GitHub, LinkedIn pattern)

**Assessment Impact:**
```
BEFORE Acquisition:
  Vendor: SmallCloudCo
  Certifications: ISO 27001, SOC 2
  Data Residency: EU only
  Risk Rating: LOW

AFTER Acquisition (Microsoft):
  Vendor: Microsoft (via SmallCloudCo)
  Certifications: Inherited from Microsoft (broader scope)
  Data Residency: NOW GLOBAL (Microsoft datacenters worldwide)
  Risk Rating: RE-ASSESS (jurisdictional risk increased?)

ACTION REQUIRED:
1. Update Sheet 2: Vendor name change
2. Re-assess Sheet 5: Data residency may have changed
3. Re-assess Sheet 7: If acquirer is US-based, CLOUD Act now applies
4. Review Sheet 3: Contract may have changed (novation clause?)
5. Re-approve in Sheet 10: New risk profile requires CISO re-approval
```

**Process:**
```
☐ Vendor sends acquisition notification
  ├─ Verify notification authenticity (phishing risk!)
  └─ Obtain formal transition plan from vendor

☐ Legal Review
  ├─ Check contract for "change of control" clauses
  ├─ Determine if novation required (new contract with acquirer)
  ├─ Assess if contract termination rights triggered
  └─ Document legal analysis in Sheet 3

☐ Re-Assessment
  ├─ Treat as NEW vendor assessment
  ├─ Complete full Sheet 2-7 evaluation
  ├─ Compare before/after risk ratings
  ├─ Escalate to CISO if risk increased
  └─ Update IMP-5.23.1 inventory (new vendor entity)

☐ Decision
  ├─ Accept new vendor (update workbook, continue service)
  ├─ Renegotiate terms (pause service until contract updated)
  ├─ Exit vendor (trigger IMP-5.23.4 exit planning)
  └─ Document decision in Sheet 10 approval notes
```

**IMPLEMENTER PERSPECTIVE:**
*Vendor M&A happens constantly in tech. Have a process ready. Don't assume "nothing changed" just because the service still works.*

**AUDITOR PERSPECTIVE:**
*Verify that vendor M&A events triggered re-assessment. Lack of re-assessment = potential compliance gap (old certifications no longer valid under new entity).*

---

**Event 2: Major Service Change (e.g., Cloud Region Shutdown)**

**Scenario:** Vendor announces "We're closing our EU datacenter, migrating to US"

**Assessment Impact:**
```
BEFORE:
  Data Residency (Sheet 5): EU only ✓
  GDPR Compliance (Sheet 5): Compliant ✓
  Jurisdictional Risk (Sheet 7): LOW ✓

AFTER:
  Data Residency (Sheet 5): US ✗ (violates data residency requirement)
  GDPR Compliance (Sheet 5): REQUIRES TIA (Transfer Impact Assessment)
  Jurisdictional Risk (Sheet 7): MEDIUM-HIGH (CLOUD Act exposure)

DECISION POINT: Can we continue using this vendor?
```

**Process:**
```
☐ Impact Assessment
  ├─ Review Sheet 5: Does new data location violate our policies?
  ├─ Review Sheet 7: Does new jurisdiction increase legal risk?
  ├─ Consult DPO: Is a TIA required for cross-border transfer?
  ├─ Consult Legal: Any contractual obligations violated?
  └─ Document impact analysis in Sheet 8 notes

☐ Risk Mitigation Options
  ├─ Option A: Implement additional safeguards (e.g., CMK encryption)
  ├─ Option B: Renegotiate contract (demand EU data residency)
  ├─ Option C: Exit vendor (find alternative provider)
  └─ Cost-benefit analysis of each option

☐ Stakeholder Decision
  ├─ Present options to Security Steering Committee
  ├─ DPO approves/rejects cross-border transfer
  ├─ CISO approves/rejects residual risk
  ├─ Business Owner decides: Continue vs. Exit
  └─ Document decision in Sheet 10

☐ Implementation
  ├─ If Continue: Update Sheet 5, Sheet 7, implement mitigations
  ├─ If Exit: Trigger vendor exit process (data migration, contract termination)
  └─ Monitor ongoing compliance with decision
```

**IMPLEMENTER PERSPECTIVE:**
*Vendor service changes can blindside you. Subscribe to vendor change notification lists. Review monthly. React proactively, not reactively.*

**AUDITOR PERSPECTIVE:**
*Verify that major service changes were documented and assessed. Evidence: vendor change notifications, impact assessments, steering committee decisions.*

---

**Event 3: Vendor Security Incident**

**Scenario:** Vendor suffers data breach, confidential data exposed

**Assessment Impact:**
```
IMMEDIATE:
  Sheet 4 SLA Performance: Incident logged
  Sheet 8 Risk Rating: Temporarily increased to HIGH
  Sheet 10 Approval: CISO review required

30-DAY POST-INCIDENT:
  Sheet 2 Certifications: Verify SOC 2 still valid (or suspended?)
  Sheet 3 Contract: Invoke liability clauses, penalties
  Sheet 6 Forensics: Exercise audit rights (demand forensic report)
  Sheet 7 Jurisdictional: If breach triggered foreign law enforcement, reassess

90-DAY POST-INCIDENT:
  Sheet 8 Risk Rating: Re-assess based on vendor remediation
  Decision: Continue, Enhanced Monitoring, or Exit
```

**Process:**
```
☐ Immediate Response (Day 0-7)
  ├─ Log incident in Sheet 4 SLA tracking
  ├─ Flag vendor as HIGH risk in Sheet 8
  ├─ Notify CISO, DPO, Legal (if personal data involved)
  ├─ Activate incident response plan
  └─ Document incident timeline

☐ Vendor Accountability (Day 7-30)
  ├─ Request formal incident report from vendor
  ├─ Invoke Sheet 6 audit rights (demand forensic investigation details)
  ├─ Review Sheet 3 contract: Liability, indemnification, penalty clauses
  ├─ Legal: Pursue contractual remedies if applicable
  └─ Document vendor's response and remediation plan

☐ Re-Assessment (Day 30-90)
  ├─ Re-assess Sheet 2: Are certifications still valid?
  ├─ Re-assess Sheet 6: Did vendor improve forensic capabilities?
  ├─ Re-assess Sheet 7: Any new jurisdictional risks from breach?
  ├─ Re-assess Sheet 8: Updated risk rating based on remediation
  └─ Decision: Restore confidence, Enhanced Monitoring, or Exit

☐ Lessons Learned (Day 90+)
  ├─ Update assessment framework based on incident
  ├─ Add new criteria to Sheet 2 (e.g., "Breach History" column)
  ├─ Enhance Sheet 6 forensic requirements
  ├─ Share lessons learned with peer organizations
  └─ Archive incident case study
```

**IMPLEMENTER PERSPECTIVE:**
*Vendor breaches are inevitable (assume breach, not if but when). Your assessment framework should facilitate rapid response, not hinder it.*

**AUDITOR PERSPECTIVE:**
*Verify that vendor incidents triggered workbook updates. Evidence: incident reports, vendor correspondence, updated risk ratings, decisions to continue/exit.*

---

### 9.7 Workbook Versioning & Archive Strategy

**Current Version:** ISMS-IMP-A.5.23.S2

**Version Numbering Scheme:**
```
X.Y Format

X = MAJOR version (breaking changes, new sheets, regulatory updates)
  Examples:
    - v1.0 → v2.0: Added Sheet 7 (Jurisdictional Risk) for DORA/NIS2/CLOUD Act
    - v2.0 → v3.0: Complete workbook redesign

Y = MINOR version (incremental improvements, new columns, bug fixes)
  Examples:
    - v2.0 → v2.1: Added "Subprocessor List" column to Sheet 3
    - v2.1 → v2.2: Fixed formula error in Sheet 8 compliance calculation
```

**Archive Strategy:**

| Frequency | Archive Trigger | Retention |
|-----------|----------------|-----------|
| **Quarterly** | End of quarter maintenance | 3 years |
| **Annual** | Annual comprehensive review | 7 years (regulatory requirement) |
| **Major Version** | Framework redesign (e.g., v2.0 → v3.0) | Permanent |
| **Incident-Driven** | Vendor breach, audit finding | Permanent (evidence preservation) |

**Archived Workbook Naming Convention:**
```
ISMS_IMP_A_5_23_2_Vendor_DD_[VERSION]_[YYYY-MM-DD]_ARCHIVE.xlsx

Examples:
  - ISMS_IMP_A_5_23_2_Vendor_DD_2026-01-20_ARCHIVE.xlsx  (Original)
  - ISMS_IMP_A_5_23_2_Vendor_DD_2026-03-31_Q1_ARCHIVE.xlsx  (Q1 snapshot)
  - ISMS_IMP_A_5_23_2_Vendor_DD_2026-12-31_ANNUAL_ARCHIVE.xlsx  (Annual review)
  - ISMS_IMP_A_5_23_2_Vendor_DD_2026-05-15_INCIDENT_AWS_ARCHIVE.xlsx  (Incident evidence)
```

**IMPLEMENTER PERSPECTIVE:**
*Archives are your audit trail. Don't delete old versions. Storage is cheap, re-creating historical evidence is expensive.*

**AUDITOR PERSPECTIVE:**
*Request archived workbooks to verify point-in-time compliance. Current workbook only shows current state, not historical compliance.*

---

### 9.8 Integration Summary Dashboard

**Purpose:** At-a-glance view of all integration points and their status.

**Location:** Create a "Integration Status" sheet in this workbook (or IMP-5.23.5 dashboard)

**Dashboard Structure:**
```
┌──────────────────────────────────────────────────────────────────────┐
│              IMP-A.5.23.2 INTEGRATION STATUS DASHBOARD               │
├──────────────────────────────────────────────────────────────────────┤
│ Last Updated: 20.01.2026                    Status: ● GREEN          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ UPSTREAM INTEGRATIONS (Data IN):                                     │
│ ┌────────────────────┬─────────────┬───────────┬────────────────┐    │
│ │ Source System      │ Last Sync   │ Status    │ Next Sync      │    │
│ ├────────────────────┼─────────────┼───────────┼────────────────┤    │
│ │ IMP-5.23.1         │ 15.01.2026  │ ● GREEN   │ 22.01.2026     │    │
│ │ (Inventory)        │             │           │ (Weekly)       │    │
│ └────────────────────┴─────────────┴───────────┴────────────────┘    │
│                                                                      │
│ DOWNSTREAM INTEGRATIONS (Data OUT):                                  │
│ ┌────────────────────┬─────────────┬───────────┬────────────────┐    │
│ │ Target System      │ Last Export │ Status    │ Next Export    │    │
│ ├────────────────────┼─────────────┼───────────┼────────────────┤    │
│ │ IMP-5.23.3         │ 18.01.2026  │ ● GREEN   │ 25.01.2026     │    │
│ │ (Secure Config)    │             │           │ (Weekly)       │    │
│ ├────────────────────┼─────────────┼───────────┼────────────────┤    │
│ │ IMP-5.23.4         │ 01.01.2026  │ ● AMBER   │ 01.02.2026     │    │
│ │ (Governance)       │             │ (Overdue) │ (Monthly)      │    │
│ ├────────────────────┼─────────────┼───────────┼────────────────┤    │
│ │ IMP-5.23.5         │ 19.01.2026  │ ● GREEN   │ 20.01.2026     │    │
│ │ (Dashboard)        │             │           │ (Daily)        │    │
│ └────────────────────┴─────────────┴───────────┴────────────────┘    │
│                                                                      │
│ ORGANIZATIONAL SYSTEM INTEGRATIONS:                                  │
│ ┌────────────────────┬─────────────┬───────────┬────────────────┐    │
│ │ System             │ Last Sync   │ Status    │ Integration    │    │
│ ├────────────────────┼─────────────┼───────────┼────────────────┤    │
│ │ CMDB               │ 10.01.2026  │ ● AMBER   │ Manual Export  │    │
│ │                    │             │ (Stale)   │ (Monthly)      │    │
│ ├────────────────────┼─────────────┼───────────┼────────────────┤    │
│ │ Procurement        │ 15.01.2026  │ ● GREEN   │ API Sync       │    │
│ │                    │             │           │ (Real-time)    │    │
│ ├────────────────────┼─────────────┼───────────┼────────────────┤    │
│ │ ITSM               │ 19.01.2026  │ ● GREEN   │ Monthly Export │    │
│ │                    │             │           │                │    │
│ ├────────────────────┼─────────────┼───────────┼────────────────┤    │
│ │ Contract Mgmt      │ 05.01.2026  │ ● RED     │ Broken Links   │    │
│ │                    │             │ (FAILED)  │ (FIX REQUIRED) │    │
│ └────────────────────┴─────────────┴───────────┴────────────────┘    │
│                                                                      │
│ MAINTENANCE STATUS:                                                  │
│ ┌────────────────────────────────────────────────────────────────┐   │
│ │ Last Quarterly Review: 01.01.2026                   ● COMPLETE │   │
│ │ Next Quarterly Review: 01.04.2026                   ● SCHEDULED│   │
│ │ Last Annual Review: 01.11.2025                      ● COMPLETE │   │
│ │ Next Annual Review: 01.11.2026                      ● SCHEDULED│   │
│ └────────────────────────────────────────────────────────────────┘   │
│                                                                      │
│ ISSUES REQUIRING ATTENTION:                                          │
│ ┌─────┬──────────────────────────────────────────────┬──────────┐    │
│ │ #   │ Issue                                        │ Owner    │    │
│ ├─────┼──────────────────────────────────────────────┼──────────┤    │
│ │ 1   │ CMDB sync overdue (10 days)                  │ IT Ops   │    │
│ │ 2   │ Contract Mgmt hyperlinks broken (SharePoint  │ Legal    │    │
│ │     │ migration)                                   │          │    │
│ │ 3   │ IMP-5.23.4 export failed (investigate)       │ Security │    │
│ └─────┴──────────────────────────────────────────────┴──────────┘    │
└──────────────────────────────────────────────────────────────────────┘

Status Legend:
  ● GREEN  = Healthy, on schedule
  ● AMBER  = Warning, action recommended
  ● RED    = Critical, immediate action required
```

**IMPLEMENTER PERSPECTIVE:**
*This dashboard is your weekly status check. If anything is RED or AMBER for more than 2 weeks, escalate.*

**AUDITOR PERSPECTIVE:**
*This dashboard provides audit evidence of continuous integration monitoring. Verify that issues were resolved, not just documented.*

---

### 9.9 Maintenance Schedule Calendar

**Purpose:** Never miss a maintenance deadline.

**Format:** Add to your ISMS calendar (Outlook, Google Calendar, etc.)
```
RECURRING EVENTS:

Weekly:
  ☐ Monday 09:00 - Sync IMP-5.23.1 Inventory → IMP-5.23.2 Sheet 2
  ☐ Friday 16:00 - Export IMP-5.23.2 metrics → IMP-5.23.5 Dashboard

Monthly:
  ☐ 1st Business Day - Review Sheet 3 contract renewal dates (90-day alerts)
  ☐ 15th - Export ITSM incidents → Sheet 4 SLA tracking
  ☐ Last Business Day - Archive monthly snapshot

Quarterly:
  ☐ Week 1 - Data refresh (inventory, certifications, contracts)
  ☐ Week 2 - SLA performance review, vendor QBRs
  ☐ Week 3 - Risk & compliance updates
  ☐ Week 4 - Evidence validation, export to dashboard

Annually:
  ☐ October - Begin annual comprehensive review
  ☐ November - Complete deep-dive assessments
  ☐ December - Framework improvements, training
  ☐ December 31 - Archive annual snapshot

Event-Driven:
  ☐ Vendor M&A announced → Trigger re-assessment process
  ☐ Major service change → Impact assessment within 7 days
  ☐ Vendor security incident → Immediate risk rating update
  ☐ Regulatory change → Framework update within 30 days
```

**IMPLEMENTER PERSPECTIVE:**
*Integrate this maintenance schedule into your team's calendar. Assign owners for each recurring task.*

**AUDITOR PERSPECTIVE:**
*Request calendar evidence (meeting invites, completed task logs). Verify maintenance actually occurred per schedule.*

---

### 9.10 Final Integration Checklist

Before going live with this assessment framework, verify all integrations are functioning:
```
☐ IMP-5.23.1 Integration (Upstream)
  ├─ Can export vendor list from IMP-5.23.1? (Test export)
  ├─ Can import into IMP-5.23.2 Sheet 2? (Test import)
  ├─ Do vendor names match exactly (no typos)? (Validate keys)
  └─ Is sync schedule documented? (Weekly)

☐ IMP-5.23.3 Integration (Downstream)
  ├─ Can export Sheet 8 summary to IMP-5.23.3? (Test export)
  ├─ Does IMP-5.23.3 consume the data correctly? (Validate import)
  ├─ Do risk ratings flow correctly? (Test HIGH risk flag)
  └─ Is sync schedule documented? (Weekly)

☐ IMP-5.23.4 Integration (Downstream)
  ├─ Can export Sheet 4 SLA performance to IMP-5.23.4? (Test export)
  ├─ Can export Sheet 3 renewal dates to IMP-5.23.4? (Test export)
  ├─ Does IMP-5.23.4 trigger renewal workflow? (Test trigger)
  └─ Is sync schedule documented? (Monthly)

☐ IMP-5.23.5 Integration (Dashboard)
  ├─ Can export Sheet 8 metrics to dashboard? (Test export)
  ├─ Does dashboard display correctly? (Visual validation)
  ├─ Are compliance percentages accurate? (Cross-check calculations)
  └─ Is sync schedule documented? (Daily/Weekly)

☐ CMDB Integration
  ├─ Can export vendor summary to CMDB? (Test export)
  ├─ Do CMDB records update? (Verify updates)
  ├─ Are risk ratings synchronized? (Cross-check)
  └─ Is sync schedule documented? (Monthly)

☐ Procurement System Integration
  ├─ Can link to procurement POs from Sheet 3? (Test hyperlinks)
  ├─ Can procurement system consume renewal alerts? (Test alerts)
  ├─ Are contract dates synchronized? (Cross-check dates)
  └─ Is sync schedule documented? (Real-time or monthly)

☐ ITSM Integration
  ├─ Can export vendor incidents from ITSM? (Test export)
  ├─ Can import into Sheet 4 SLA tracking? (Test import)
  ├─ Are SLA breach calculations accurate? (Validate formulas)
  └─ Is sync schedule documented? (Monthly)

☐ Contract Management System Integration
  ├─ Are all Sheet 9 hyperlinks working? (Click all links)
  ├─ Can users access linked contracts? (Permission check)
  ├─ Are contract versions up-to-date? (Version validation)
  └─ Is sync schedule documented? (N/A - manual links)

☐ Maintenance Processes
  ├─ Are recurring calendar events created? (Check calendar)
  ├─ Are task owners assigned? (Check assignments)
  ├─ Are procedures documented? (Check runbooks)
  └─ Is first quarterly maintenance scheduled? (Confirm date)

☐ Training & Documentation
  ├─ Are all stakeholders trained on workbook? (Training log)
  ├─ Is this IMP document accessible to all users? (SharePoint link)
  ├─ Are integration procedures documented? (Runbook complete)
  └─ Is support contact identified? (Help desk ticket category)

☐ Go-Live Approval
  ├─ Legal approval obtained? (Signed)
  ├─ Procurement approval obtained? (Signed)
  ├─ Security approval obtained? (Signed)
  ├─ CISO approval obtained? (Signed)
  └─ Go-live date confirmed? (________________)
```

**IMPLEMENTER PERSPECTIVE:**
*Don't skip the integration testing. A broken integration discovered during audit is embarrassing and time-consuming to fix under pressure.*

**AUDITOR PERSPECTIVE:**
*This checklist becomes audit evidence. Request the completed checklist with test results and approvals.*

---

**END OF SECTION 9: INTEGRATION & MAINTENANCE**

## Section 10: Appendices & Glossary

### 10.1 Glossary of Terms

**Comprehensive terminology reference for vendor due diligence and contract management.**

| Term | Definition | Context in This Assessment |
|------|------------|---------------------------|
| **Adequate Level of Protection** | Data protection standards equivalent to GDPR requirements, as determined by European Commission adequacy decisions | Used in Sheet 5 to assess if vendor's jurisdiction provides adequate data protection (EU, UK, Switzerland, Japan, etc.) |
| **Audit Rights** | Contractual provisions allowing [Organization] to audit vendor's security controls, either directly or via third-party assessor | Documented in Sheet 6; critical for regulatory compliance (DORA, NIS2) |
| **Availability SLA** | Service Level Agreement specifying minimum uptime percentage (e.g., 99.9% = 43.8 minutes downtime/month) | Tracked in Sheet 4; breaches trigger penalty calculations |
| **Business Associate Agreement (BAA)** | HIPAA-specific contract addendum for vendors processing healthcare data | Required for US healthcare data; variant of DPA concept |
| **Certification Validity Period** | Time period during which security certification remains valid before re-audit required (typically 1-3 years) | Sheet 2 tracks expiration dates; expired certs = compliance gap |
| **CLOUD Act** | US Clarifying Lawful Overseas Use of Data Act (2018) allowing US law enforcement to compel US-based cloud providers to disclose data stored anywhere globally | Assessed in Sheet 7 for US-nexus vendors; major GDPR conflict |
| **CMK (Customer-Managed Keys)** | Encryption keys generated and managed by customer, not cloud provider; provides strongest data protection against provider access | Sheet 5 mitigation for data sovereignty concerns |
| **Concentration Risk** | Risk arising from over-reliance on single vendor or small number of vendors for critical services | DORA requirement; assessed in Sheet 7 |
| **Critical ICT Third-Party Service Provider** | DORA designation for vendors providing services so essential that failure would materially impact [Organization]'s operations | Triggers enhanced due diligence requirements in Sheet 2, Sheet 3 |
| **Data Processing Agreement (DPA)** | GDPR-required contract addendum specifying data controller/processor relationship, processing scope, security obligations | Mandatory for all vendors processing personal data; Sheet 3 tracks DPA status |
| **Data Residency** | Legal/contractual requirement that data must be stored in specific geographic region (e.g., "EU only") | Sheet 5 primary assessment; violations = HIGH risk |
| **Data Sovereignty** | Principle that data is subject to laws of the country where it is physically located | Broader concept than residency; includes legal jurisdiction, government access |
| **Forensic Readiness** | Vendor's capability to preserve, collect, and provide digital evidence during security incident investigations | Sheet 6 assessment; critical for incident response |
| **FedRAMP (Federal Risk and Authorization Management Program)** | US government cloud security standardization program; three impact levels: Low, Moderate, High | Sheet 2 certification for vendors serving US government clients |
| **Financial Penalty Clause** | Contract provision specifying monetary penalties for SLA breaches or security failures | Sheet 4 tracks penalty amounts; must be proportionate to harm |
| **Indemnification** | Contractual obligation for vendor to compensate [Organization] for losses arising from vendor's breach or negligence | Sheet 3 legal requirement; critical for risk transfer |
| **ISO/IEC 27001** | International standard for information security management systems; certification demonstrates systematic security controls | Primary certification in Sheet 2; gold standard for vendor security |
| **Jurisdictional Risk** | Risk arising from vendor's legal jurisdiction (data access laws, government surveillance, political instability) | Sheet 7 comprehensive assessment; considers CLOUD Act, sanctions, export controls |
| **Liability Cap** | Maximum amount vendor will pay for damages; often limited to annual fees or lower | Sheet 3 negotiation point; inadequate caps = unacceptable risk |
| **NIS2 Directive** | EU Network and Information Security Directive 2 (2023); updated cybersecurity requirements for essential and important entities | Sheet 3 tracks NIS2-specific clauses (incident reporting, supply chain, governance) |
| **Novelation** | Legal term for replacing old contract with new contract, typically during vendor acquisition/merger | Sheet 3 change control; triggers re-assessment |
| **Right to Audit** | Contractual right to inspect vendor's facilities, processes, and controls; may be direct or via third-party | Sheet 6 critical assessment; "no audit rights" = deal-breaker for critical vendors |
| **SCC (Standard Contractual Clauses)** | EU Commission-approved contract templates for GDPR-compliant international data transfers (replacing Privacy Shield) | Sheet 5 requirement for non-adequate jurisdiction vendors |
| **Schrems II Decision** | CJEU ruling (July 2020) invalidating EU-US Privacy Shield; requires case-by-case Transfer Impact Assessment for US vendors | Sheet 7 triggers TIA requirement for US-nexus vendors |
| **SOC 2 Type II** | Service Organization Control 2 audit report assessing vendor's security, availability, confidentiality over 6-12 month period | Sheet 2 key certification; Type I (point-in-time) insufficient |
| **Subprocessor** | Third-party vendor used by primary vendor to process data (e.g., AWS using subcontractors for support) | Sheet 3 tracks subprocessor list; GDPR requires prior authorization |
| **Sunset Clause** | Contract provision specifying service end-of-life procedures, data return/deletion obligations | Sheet 3 exit planning; critical for vendor lock-in prevention |
| **Termination for Convenience** | Right to terminate contract without cause, subject to notice period | Sheet 3 flexibility assessment; prevents vendor lock-in |
| **TIA (Transfer Impact Assessment)** | GDPR requirement (post-Schrems II) to assess risks of transferring personal data to non-adequate jurisdictions | Sheet 7 requirement for US, China, Russia vendors processing EU personal data |
| **Uptime** | Percentage of time service is available and functioning (e.g., 99.95% uptime = 21.9 minutes downtime/month) | Sheet 4 primary SLA metric; calculated monthly/annually |

---

### 10.2 Acronyms and Abbreviations

**Quick reference for commonly used acronyms in vendor assessments.**

| Acronym | Full Form | Context |
|---------|-----------|---------|
| **API** | Application Programming Interface | Integration method for automated data exchange |
| **BAA** | Business Associate Agreement | HIPAA-required contract for healthcare data |
| **BCM** | Business Continuity Management | Vendor's resilience and disaster recovery capabilities |
| **CA** | Certification Authority | Entity issuing digital certificates (e.g., DigiCert, Let's Encrypt) |
| **CCM** | Cloud Controls Matrix | CSA framework for cloud security controls |
| **CISO** | Chief Information Security Officer | Approval authority in Sheet 10 |
| **CJEU** | Court of Justice of the European Union | Issued Schrems I/II decisions affecting data transfers |
| **CMK** | Customer-Managed Key | Encryption key controlled by customer, not vendor |
| **CSA** | Cloud Security Alliance | Industry body publishing cloud security standards |
| **CSP** | Cloud Service Provider | Generic term for IaaS/PaaS/SaaS vendors |
| **DLP** | Data Loss Prevention | Security control preventing unauthorized data exfiltration |
| **DORA** | Digital Operational Resilience Act | EU regulation for financial sector ICT risk management |
| **DPA** | Data Processing Agreement | GDPR-required contract addendum |
| **DPO** | Data Protection Officer | Privacy authority; approves Sheet 5, Sheet 7 assessments |
| **DRP** | Disaster Recovery Plan | Vendor's plan for recovering from catastrophic failures |
| **EDPB** | European Data Protection Board | EU body issuing GDPR guidance (e.g., TIA guidelines) |
| **EEA** | European Economic Area | EU + Iceland, Liechtenstein, Norway; "adequate" jurisdiction |
| **ENISA** | European Union Agency for Cybersecurity | Issues NIS2 guidance and cybersecurity recommendations |
| **FedRAMP** | Federal Risk and Authorization Management Program | US government cloud security certification |
| **FIPS 140-2/3** | Federal Information Processing Standard 140 | US cryptographic module validation standard |
| **GDPR** | General Data Protection Regulation | EU data protection law (2018); applies to EU personal data globally |
| **HIPAA** | Health Insurance Portability and Accountability Act | US healthcare data protection law |
| **IaaS** | Infrastructure as a Service | Cloud model providing virtualized compute/storage (AWS EC2, Azure VMs) |
| **ISMS** | Information Security Management System | ISO 27001 framework; this assessment is part of it |
| **ITSM** | IT Service Management | Service desk/ticketing system (e.g., ServiceNow, Jira) |
| **KPI** | Key Performance Indicator | Measurable metric (e.g., uptime %, incident response time) |
| **MSA** | Master Service Agreement | Primary contract governing vendor relationship |
| **MTPD** | Maximum Tolerable Period of Disruption | Business continuity metric; vendor RTO must be < MTPD |
| **NDA** | Non-Disclosure Agreement | Confidentiality contract; may be standalone or within MSA |
| **NIS2** | Network and Information Security Directive 2 | EU cybersecurity regulation (2023 update) |
| **PaaS** | Platform as a Service | Cloud model providing application platform (Heroku, Cloud Foundry) |
| **PCI DSS** | Payment Card Industry Data Security Standard | Required for vendors processing credit card data |
| **PII** | Personally Identifiable Information | Data identifying individuals (name, email, SSN, IP address) |
| **QBR** | Quarterly Business Review | Regular vendor performance review meeting |
| **RFI** | Request for Information | Pre-procurement questionnaire for vendor capabilities |
| **RFP** | Request for Proposal | Formal procurement process document |
| **RPO** | Recovery Point Objective | Maximum acceptable data loss (e.g., 1 hour) |
| **RTO** | Recovery Time Objective | Maximum acceptable downtime (e.g., 4 hours) |
| **SaaS** | Software as a Service | Cloud model providing applications (Salesforce, Office 365) |
| **SCC** | Standard Contractual Clauses | EU-approved contract templates for international data transfers |
| **SDLC** | Software Development Lifecycle | Vendor's development process; security integration critical |
| **SLA** | Service Level Agreement | Contract defining performance standards and penalties |
| **SOC 2** | Service Organization Control 2 | AICPA audit standard for service providers |
| **SOW** | Statement of Work | Project-specific contract addendum to MSA |
| **TIA** | Transfer Impact Assessment | GDPR risk assessment for international data transfers |
| **TLS** | Transport Layer Security | Encryption protocol for data in transit (successor to SSL) |
| **TPRM** | Third-Party Risk Management | Vendor risk management program; this workbook is core component |

---

### 10.3 Reference Documents

**Key documents and standards referenced in this assessment.**

#### Regulatory & Legal References

| Document | Issuing Body | Relevance | Access |
|----------|--------------|-----------|--------|
| **ISO/IEC 27001:2022** | International Organization for Standardization | Foundation standard for ISMS; Annex A Controls 5.19-5.23 govern supplier security | www.iso.org |
| **GDPR (Regulation 2016/679)** | European Union | Data protection requirements; Articles 28-29 (processor obligations), Article 44+ (international transfers) | eur-lex.europa.eu |
| **DORA (Regulation 2022/2554)** | European Union | ICT risk management for financial entities; Articles 28-30 (third-party risk), Article 31 (concentration risk) | eur-lex.europa.eu |
| **NIS2 Directive (Directive 2022/2555)** | European Union | Cybersecurity requirements for essential/important entities; Article 21 (supply chain security) | eur-lex.europa.eu |
| **CLOUD Act (H.R. 4943)** | United States Congress | US law enforcement data access to US companies' overseas data; conflicts with GDPR | congress.gov |
| **Schrems II Decision (C-311/18)** | Court of Justice of the European Union | Invalidated EU-US Privacy Shield; requires TIA for US data transfers | curia.europa.eu |
| **EDPB Recommendations 01/2020** | European Data Protection Board | Guidelines on Transfer Impact Assessment (TIA) methodology | edpb.europa.eu |
| **ENISA Guidelines on NIS2 Security Measures** | EU Agency for Cybersecurity | Implementation guidance for NIS2 technical requirements | www.enisa.europa.eu |

#### Internal ISMS Documents

| Document ID | Title | Relationship to This Document |
|-------------|-------|------------------------------|
| **ISMS-POL-A.5.19-23** | Supplier and Cloud Services Security Policy (Master) | Umbrella policy governing all supplier/cloud assessments |
| **ISMS-POL-A.5.19-23-S1** | Supplier Relationship Fundamentals (A.5.19) | Supplier classification, lifecycle, baseline requirements |
| **ISMS-POL-A.5.19-23-S2** | Supplier Agreement Requirements (A.5.20) | Contract clause requirements implemented in Sheet 3 |
| **ISMS-POL-A.5.19-23-S3** | ICT Supply Chain Security (A.5.21) | Supply chain risk requirements (subprocessors in Sheet 3) |
| **ISMS-POL-A.5.19-23-S4** | Supplier Monitoring & Change Management (A.5.22) | Ongoing monitoring requirements (SLA tracking in Sheet 4) |
| **ISMS-POL-A.5.19-23-S5** | Cloud Services Security (A.5.23) | Cloud-specific requirements (data residency in Sheet 5) |
| **ISMS-POL-A.5.19-23-S6** | Assessment Methodology & Automation | Assessment framework architecture (how this workbook fits) |
| **ISMS-IMP-A.5.23.S1** | Cloud Service Inventory & Classification | Upstream dependency; source of vendor list for Sheet 2 |
| **ISMS-IMP-A.5.23.S3** | Secure Configuration & Deployment | Downstream consumer; uses Sheet 2-5 data for config baselines |
| **ISMS-IMP-A.5.23.S4** | Ongoing Governance & Risk Management | Downstream consumer; uses Sheet 4 SLA data for vendor scorecards |
| **ISMS-IMP-A.5.23.S5** | Compliance Monitoring Dashboard | Aggregates Sheet 8 metrics for executive reporting |

#### Industry Standards & Frameworks

| Standard | Organization | Purpose | Relevance to Assessment |
|----------|--------------|---------|------------------------|
| **SOC 2 Trust Services Criteria** | AICPA | Defines security, availability, confidentiality, processing integrity, privacy controls | Sheet 2 certification verification standard |
| **ISO/IEC 27017** | ISO | Cloud-specific information security controls | Optional certification tracked in Sheet 2 |
| **ISO/IEC 27018** | ISO | Protection of PII in public clouds | Optional certification for vendors processing personal data |
| **CSA Cloud Controls Matrix (CCM)** | Cloud Security Alliance | Comprehensive cloud security control framework | Alternative/supplementary to ISO 27001 for cloud vendors |
| **FedRAMP Security Controls** | US GSA | US government cloud security baseline (based on NIST 800-53) | Sheet 2 certification for US government-focused vendors |
| **NIST Cybersecurity Framework** | NIST | US cybersecurity framework (Identify, Protect, Detect, Respond, Recover) | Optional vendor security program assessment framework |
| **CIS Controls v8** | Center for Internet Security | Prioritized cybersecurity best practices | Can be used as vendor security maturity benchmark |
| **ENISA Cloud Computing Security Risk Assessment** | ENISA | EU cloud security risk methodology | Useful for Sheet 7 jurisdictional risk assessment |

---

### 10.4 Sample Templates

**Ready-to-use templates for common assessment tasks.**

#### Template 1: Vendor Assessment Request Email
```
Subject: Information Security Due Diligence - [Vendor Name]

Dear [Vendor Contact Name],

As part of [Organization]'s Information Security Management System (ISO 27001:2022) compliance, we are conducting security due diligence on all cloud service providers.

We request the following documentation:

CERTIFICATIONS (Sheet 2):
☐ Current ISO/IEC 27001 certificate (with scope statement)
☐ Current SOC 2 Type II report (covering last 6-12 months)
☐ [If applicable] FedRAMP authorization letter
☐ [If applicable] Industry-specific certifications (PCI DSS, HIPAA, etc.)

CONTRACTUAL (Sheet 3):
☐ Current Master Service Agreement (MSA)
☐ Data Processing Agreement (DPA) / Business Associate Agreement (BAA)
☐ Service Level Agreement (SLA) with penalty clauses
☐ Subprocessor list (current as of [DATE])

DATA SOVEREIGNTY (Sheet 5):
☐ Data residency documentation (where is our data stored?)
☐ Customer-Managed Key (CMK) support confirmation
☐ Standard Contractual Clauses (if applicable for international transfers)

AUDIT RIGHTS (Sheet 6):
☐ Right-to-audit clause confirmation in MSA
☐ Forensic investigation support procedures
☐ Incident response and notification process

Please provide this documentation within 10 business days. If any requested items are not available or require negotiation, please notify us immediately.

Security Assessment Contact: [Name, Email, Phone]

Thank you for your cooperation.

Best regards,
[Your Name]
[Title]
[Organization]
```

---

#### Template 2: Transfer Impact Assessment (TIA) Summary

**Use this template for Sheet 7 when vendor is in non-adequate jurisdiction (e.g., US).**
```
TRANSFER IMPACT ASSESSMENT SUMMARY
Vendor: _______________________
Assessment Date: _______________
Assessed By: ___________________
DPO Approval: ☐ Approved  ☐ Rejected  ☐ Approved with Conditions

1. DATA TRANSFER DETAILS
   Data Types: ☐ Customer PII  ☐ Employee PII  ☐ Other: ___________
   Volume: ☐ Low (<1000 records)  ☐ Medium (1K-100K)  ☐ High (>100K)
   Sensitivity: ☐ Low  ☐ Medium  ☐ High  ☐ Special Categories (Art. 9 GDPR)
   
2. VENDOR JURISDICTION ANALYSIS
   Vendor Location: _______________________
   Data Storage Location(s): _______________________
   Adequacy Decision: ☐ Yes (Country: _______)  ☐ No
   
3. LEGAL RISKS (CLOUD Act, FISA 702, etc.)
   US Nexus: ☐ Yes (US-based or US parent company)  ☐ No
   Government Access Risk: ☐ Low  ☐ Medium  ☐ High
   Rationale: _______________________________________
   
4. SUPPLEMENTARY MEASURES (Sheet 5)
   ☐ Standard Contractual Clauses (SCCs) in place
   ☐ Customer-Managed Keys (CMK) implemented
   ☐ End-to-end encryption (vendor cannot decrypt)
   ☐ Data pseudonymization/anonymization
   ☐ Contractual restrictions on government access
   ☐ Vendor transparency reports reviewed
   
5. RESIDUAL RISK ASSESSMENT
   After supplementary measures, residual risk is:
   ☐ ACCEPTABLE (transfer may proceed)
   ☐ CONDITIONAL (additional mitigations required: _____________)
   ☐ UNACCEPTABLE (transfer not permitted, seek alternative vendor)
   
6. DECISION
   ☐ APPROVED - Transfer complies with GDPR Article 46
   ☐ APPROVED WITH CONDITIONS (specify): _______________________
   ☐ REJECTED - Alternative vendor required
   
   DPO Signature: ________________  Date: __________
```

---

#### Template 3: Vendor Quarterly Business Review (QBR) Agenda

**Use this template for Sheet 4 SLA performance reviews.**
```
QUARTERLY BUSINESS REVIEW (QBR) AGENDA
Vendor: _______________________
Quarter: Q__ 20__
Meeting Date: _________________
Attendees:
  [Organization]: _______________ (roles)
  [Vendor]: ____________________ (roles)

AGENDA:

1. EXECUTIVE SUMMARY (5 min)
   ☐ Relationship health: ☐ Excellent  ☐ Good  ☐ Needs Improvement
   ☐ Key accomplishments this quarter
   ☐ Key challenges/concerns

2. SLA PERFORMANCE REVIEW (15 min) [Sheet 4 Data]
   ☐ Uptime: Actual ___% vs. Target ___%
   ☐ SLA breaches: Count __ (vs. last quarter __)
   ☐ Incident response time: Avg __ mins (vs. SLA __ mins)
   ☐ Support ticket resolution: Avg __ days (vs. SLA __ days)
   ☐ Financial penalties: €______ (paid/waived/disputed)
   
   Action Items:
   ☐ _______________________________________
   ☐ _______________________________________

3. SECURITY POSTURE UPDATE (10 min) [Sheet 2 Data]
   ☐ Certification status:
      ├─ ISO 27001: Valid until __________
      ├─ SOC 2 Type II: Last audit __________
      └─ Other: _______________________
   ☐ Recent security incidents: [Description]
   ☐ Planned security enhancements: [Roadmap]
   
   Action Items:
   ☐ _______________________________________

4. CONTRACT & COMPLIANCE (10 min) [Sheet 3 Data]
   ☐ Contract renewal: Date __________ (__ months away)
   ☐ Regulatory updates: DORA/NIS2/Other
   ☐ Subprocessor changes: [List new/removed]
   ☐ Data residency compliance: ☐ Confirmed  ☐ Concerns: ________
   
   Action Items:
   ☐ _______________________________________

5. BUSINESS ROADMAP (10 min)
   ☐ Vendor product roadmap highlights
   ☐ [Organization] usage evolution (growth/contraction)
   ☐ Opportunities for optimization (cost, performance, features)
   
6. RISK & ISSUES (10 min) [Sheet 7, Sheet 8 Data]
   ☐ Current risk rating: ☐ Low  ☐ Medium  ☐ High
   ☐ Top 3 risks:
      1. ___________________________
      2. ___________________________
      3. ___________________________
   ☐ Mitigation plans:
      ☐ _______________________________________
   
7. ACTION ITEMS SUMMARY (5 min)
   | Action | Owner | Due Date | Status |
   |--------|-------|----------|--------|
   | ______ | _____ | ________ | ______ |
   
8. NEXT QBR: ________________

MEETING NOTES:
_____________________________________________
_____________________________________________

Attendees' Signatures:
[Organization]: _______________  Date: ______
[Vendor]: _____________________  Date: ______
```

---

#### Template 4: Vendor Exit Checklist

**Use when terminating vendor relationship (Sheet 3 exit planning).**
```
VENDOR EXIT CHECKLIST
Vendor: _______________________
Exit Date: ____________________
Exit Coordinator: ______________

PHASE 1: PRE-EXIT PLANNING (90 days before)
☐ Review contract termination clause (notice period, penalties)
☐ Identify replacement vendor or in-house solution
☐ Document all services/integrations provided by vendor
☐ Inventory all data stored with vendor
☐ Create data extraction/migration plan
☐ Budget for exit costs (migration, parallel running, etc.)

PHASE 2: VENDOR NOTIFICATION (60 days before)
☐ Send formal termination notice per contract terms
☐ Request data extraction in usable format (CSV, JSON, database dump)
☐ Schedule exit transition meetings with vendor
☐ Confirm data deletion timeline and certification process
☐ Review final billing/credits (prepaid services, penalties, refunds)

PHASE 3: DATA MIGRATION (30-60 days before)
☐ Extract all data from vendor systems
☐ Validate data integrity (no corruption, completeness)
☐ Import data into replacement system
☐ Test replacement system functionality
☐ Run parallel systems (if feasible) for validation period
☐ Document any data loss or migration issues

PHASE 4: SERVICE CUTOVER (Exit date)
☐ Deactivate user access to vendor system
☐ Redirect traffic/integrations to replacement system
☐ Monitor for service disruptions
☐ Verify all integrations functioning
☐ Communicate service change to users

PHASE 5: POST-EXIT CLEANUP (0-30 days after)
☐ Request vendor data deletion certificate
☐ Verify data deletion (if audit rights permit)
☐ Cancel billing/payment methods
☐ Remove vendor credentials from password vaults
☐ Update CMDB to reflect service decommission
☐ Update IMP-5.23.1 inventory (vendor status: EXITED)
☐ Archive vendor documentation for retention period (7 years)
☐ Conduct lessons learned review (why exited, what went well/poorly)

PHASE 6: FINAL SIGN-OFF (30 days after)
☐ Legal: Contract obligations fulfilled ☐ Yes  ☐ No (explain: _____)
☐ Finance: Final invoice reconciled  ☐ Yes  ☐ No (explain: _____)
☐ Security: Data deletion confirmed   ☐ Yes  ☐ No (explain: _____)
☐ IT Ops: Service migrated successfully ☐ Yes  ☐ No (explain: _____)

EXIT COORDINATOR SIGN-OFF:
Name: ________________  Signature: ___________  Date: ________

CISO APPROVAL:
Name: ________________  Signature: ___________  Date: ________
```

---

### 10.5 Regulatory Framework Summaries

**Quick reference for key regulatory requirements impacting vendor assessments.**

#### DORA (Digital Operational Resilience Act) - EU Regulation 2022/2554

**Applicability:** Financial entities (banks, insurance, investment firms) operating in EU

**Key Requirements for Vendor Assessment:**

| Article | Requirement | Implementation in This Assessment |
|---------|-------------|----------------------------------|
| **Art. 28** | Register of ICT third-party providers | All vendors tracked in IMP-5.23.1 + Sheet 2 |
| **Art. 28** | Contractual arrangements for ICT services | Sheet 3 contract analysis (SLAs, exit rights, audit rights) |
| **Art. 28.3** | Exit strategies for critical vendors | Sheet 3 "Sunset Clause" and "Termination Rights" columns |
| **Art. 28.5** | Right to access, inspect, and audit vendor | Sheet 6 audit rights verification (MANDATORY for critical vendors) |
| **Art. 28.9** | Monitor ICT concentration risk | Sheet 7 "Vendor Concentration Risk" assessment (DORA-specific) |
| **Art. 30** | Subcontracting (subprocessor management) | Sheet 3 "Subprocessor List" column |

**Risk Classification:**
- **Critical ICT Provider:** Failure materially impacts operations → Enhanced due diligence (all sheets 2-7)
- **Important ICT Provider:** Significant but not critical → Standard due diligence
- **Minor ICT Provider:** Limited impact → Simplified assessment

**IMPLEMENTER NOTE:** If [Organization] is DORA-subject, flag critical ICT providers in IMP-5.23.1 and ensure Sheet 6 audit rights are NON-NEGOTIABLE.

**AUDITOR NOTE:** Verify that ALL critical ICT providers have documented exit strategies (Sheet 3) and audit rights (Sheet 6).

---

#### NIS2 Directive - EU Directive 2022/2555

**Applicability:** Essential entities (energy, transport, healthcare, critical digital infrastructure) and important entities (postal, waste, chemicals, food, manufacturing) in EU

**Key Requirements for Vendor Assessment:**

| Article | Requirement | Implementation in This Assessment |
|---------|-------------|----------------------------------|
| **Art. 21.2(d)** | Supply chain security (vendor risk management) | Entire assessment framework implements this requirement |
| **Art. 21.2(e)** | Security in network and information systems acquisition, development, maintenance | Sheet 3 SDLC requirements, Sheet 6 change management clauses |
| **Art. 23** | Incident reporting (24h notification for significant incidents) | Sheet 3 "Incident Notification Timeline" column (must be ≤24h for NIS2 entities) |

**Vendor Risk Classification:**
- **Critical Supplier:** Provides essential services → Full assessment (Sheets 2-7)
- **Important Supplier:** Significant role → Standard assessment
- **Minor Supplier:** Limited role → Simplified assessment

**IMPLEMENTER NOTE:** If [Organization] is NIS2-subject, ensure Sheet 3 incident notification clause requires vendor to notify within 24 hours (NIS2 Art. 23 pass-through obligation).

**AUDITOR NOTE:** For NIS2 entities, verify that critical suppliers have 24-hour incident notification clauses in contracts (Sheet 3).

---

#### GDPR (General Data Protection Regulation) - EU Regulation 2016/679

**Applicability:** Any organization processing EU residents' personal data (global reach)

**Key Requirements for Vendor Assessment:**

| Article | Requirement | Implementation in This Assessment |
|---------|-------------|----------------------------------|
| **Art. 28** | Data Processing Agreement (DPA) required for processors | Sheet 3 "DPA Status" column (MANDATORY for vendors processing personal data) |
| **Art. 28.3** | Processor security obligations | Sheet 2 certifications verify processor security |
| **Art. 28.9** | Subprocessor authorization | Sheet 3 "Subprocessor List" + authorization process |
| **Art. 32** | Security of processing (appropriate technical/organizational measures) | Sheet 2 certification verification (ISO 27001, SOC 2) |
| **Art. 44-49** | International data transfers | Sheet 5 data residency + Sheet 7 TIA for non-adequate jurisdictions |
| **Art. 46** | Appropriate safeguards (SCCs) | Sheet 5 "SCC Status" for vendors in US, China, etc. |

**Data Transfer Mechanisms:**
1. **Adequacy Decision (Art. 45):** EU, UK, Switzerland, Japan, Canada (commercial), etc. → No additional safeguards needed
2. **Standard Contractual Clauses (Art. 46):** US, China, India, etc. → SCCs + TIA required
3. **Derogations (Art. 49):** One-off transfers, explicit consent → Use sparingly, high risk

**IMPLEMENTER NOTE:** ALL vendors processing EU personal data MUST have DPA (Sheet 3). Vendors in non-adequate jurisdictions (especially US) REQUIRE TIA (Sheet 7).

**AUDITOR NOTE:** Verify DPA exists and is GDPR-compliant (covers Art. 28.3 requirements). Verify TIA completed for non-adequate jurisdiction transfers.

---

#### CLOUD Act - US H.R. 4943 (2018)

**Applicability:** US-based companies and foreign companies with US nexus (US subsidiary, significant US operations)

**Key Impact on Vendor Assessment:**

**What is CLOUD Act?**
US law allowing law enforcement to compel US-based cloud providers to disclose data stored ANYWHERE IN THE WORLD, regardless of local data protection laws.

**GDPR Conflict:**
- GDPR forbids data disclosure to foreign governments without adequate legal basis
- CLOUD Act mandates disclosure upon US legal demand
- Result: **Direct conflict** → US vendors cannot guarantee GDPR compliance

**Assessment Implications:**

| Assessment Area | Impact | Mitigation |
|----------------|--------|------------|
| **Sheet 5: Data Residency** | US vendor with "EU-only" data residency still subject to CLOUD Act | EU data residency necessary but NOT sufficient |
| **Sheet 7: Jurisdictional Risk** | US-nexus vendors automatically MEDIUM-HIGH risk for EU data | Customer-Managed Keys (CMK) so vendor cannot decrypt |
| **Transfer Impact Assessment** | TIA required for ALL US vendors processing EU personal data | Document residual risk, seek DPO approval |

**US Nexus Determination (Sheet 7):**
- ☐ Vendor incorporated in US → YES (CLOUD Act applies)
- ☐ Vendor has US parent company → YES (CLOUD Act applies)
- ☐ Vendor has US subsidiary providing services → YES (CLOUD Act applies)
- ☐ Vendor uses US-based subprocessors → MAYBE (depends on data access)
- ☐ Vendor incorporated outside US, no US nexus → NO (CLOUD Act does not apply)

**IMPLEMENTER NOTE:** For US-nexus vendors processing sensitive EU data, CMK encryption is ESSENTIAL (Sheet 5). Vendor must NOT have decryption keys.

**AUDITOR NOTE:** Verify that Sheet 7 correctly identifies US nexus. Verify that high-risk US vendors have CMK implemented (evidence: encryption key management documentation).

---

### 10.6 Vendor Assessment Criteria Reference

**Detailed scoring criteria for Sheet 2 (Vendor Security Certifications).**

#### ISO/IEC 27001 Certification Verification

**What to Check:**
```
☐ Certificate Authenticity
  ├─ Issued by accredited certification body (look for accreditation logo)
  ├─ Certificate number traceable in CB's public register
  └─ Not expired (check "Valid Until" date)

☐ Scope of Certification
  ├─ Does scope cover the services [Organization] is using?
  ├─ Example: Certificate for "data center operations" doesn't cover SaaS application
  ├─ Scope should explicitly mention cloud services if vendor is cloud provider
  └─ Generic scope ("information security management") may be too broad

☐ Certificate Status
  ├─ Valid (within dates)
  ├─ Suspended (check CB website) → RED FLAG
  └─ Withdrawn → RED FLAG

☐ Surveillance Audit Schedule
  ├─ Annual surveillance audits required
  ├─ Last surveillance audit date (should be within 12 months)
  └─ Next surveillance audit date (should be scheduled)
```

**Scoring:**

| Condition | Score | Risk Level |
|-----------|-------|------------|
| Valid ISO 27001, scope matches, recent surveillance audit | 10 | LOW |
| Valid ISO 27001, scope partially matches | 7 | MEDIUM |
| Valid ISO 27001, scope unclear or too broad | 5 | MEDIUM |
| No ISO 27001, but has SOC 2 Type II | 6 | MEDIUM |
| No ISO 27001, no SOC 2 | 0 | HIGH |
| ISO 27001 expired or suspended | 0 | HIGH |

---

#### SOC 2 Type II Report Verification

**What to Check:**
```
☐ Report Type
  ├─ Type I: Point-in-time audit (snapshot) → INSUFFICIENT for vendor assessment
  ├─ Type II: 6-12 month audit (operational effectiveness) → REQUIRED
  └─ Bridge Letter: Extends validity between Type II reports → ACCEPTABLE if current Type II exists

☐ Trust Services Criteria Covered
  ├─ Security (MANDATORY)
  ├─ Availability (HIGHLY RECOMMENDED for critical services)
  ├─ Confidentiality (if vendor handles confidential data)
  ├─ Processing Integrity (if vendor processes transactions)
  └─ Privacy (if vendor processes personal data)

☐ Opinion
  ├─ Unqualified Opinion (no exceptions) → BEST
  ├─ Qualified Opinion (exceptions noted) → REVIEW EXCEPTIONS
  └─ Adverse Opinion → RED FLAG

☐ Exceptions / Findings
  ├─ Review Section IV: Tests of Controls Results
  ├─ Any failures/deviations noted?
  ├─ Are exceptions material to [Organization]'s use case?
  └─ Has vendor remediated exceptions? (request follow-up evidence)

☐ Audit Period
  ├─ Should cover last 6-12 months
  ├─ Report date should be within last 12 months
  └─ Gap coverage: If report is 11 months old, request bridge letter or new report
```

**Scoring:**

| Condition | Score | Risk Level |
|-----------|-------|------------|
| Type II, Security + Availability, Unqualified Opinion, <6 months old | 10 | LOW |
| Type II, Security only, Unqualified Opinion, <12 months old | 8 | LOW-MEDIUM |
| Type II, Qualified Opinion with minor exceptions | 6 | MEDIUM |
| Type II, Qualified Opinion with material exceptions | 4 | MEDIUM-HIGH |
| Type I only (point-in-time) | 3 | HIGH |
| No SOC report | 0 | HIGH |
| Adverse Opinion | 0 | CRITICAL |

---

### 10.7 Quick Reference Guides

**One-page cheat sheets for common tasks.**

#### Quick Reference 1: New Vendor Onboarding (Fast Track)
```
NEW VENDOR ONBOARDING - 10-DAY FAST TRACK

Day 1-2: INITIAL ASSESSMENT (Sheet 2)
  ☐ Obtain vendor name, website, primary contact
  ☐ Request ISO 27001 certificate + SOC 2 Type II report
  ☐ Verify certifications (check CB registers, AICPA portal)
  ☐ Initial risk scoring (LOW/MEDIUM/HIGH)

Day 3-4: CONTRACT REVIEW (Sheet 3)
  ☐ Obtain MSA, DPA, SLA
  ☐ Legal review (minimum required clauses checklist)
  ☐ Identify gaps/red flags
  ☐ If critical gaps → PAUSE, negotiate before proceeding

Day 5-6: DATA SOVEREIGNTY (Sheet 5)
  ☐ Confirm data storage location(s)
  ☐ If non-EU → Check adequacy decision
  ☐ If US vendor + EU personal data → TIA REQUIRED (Sheet 7)
  ☐ Document data residency configuration

Day 7: AUDIT RIGHTS (Sheet 6)
  ☐ Verify right-to-audit clause in MSA
  ☐ If critical vendor without audit rights → ESCALATE

Day 8: JURISDICTIONAL RISK (Sheet 7)
  ☐ If US nexus → CLOUD Act assessment
  ☐ If applicable → TIA completion (may require DPO input, could delay go-live)
  ☐ Risk mitigation: CMK, SCCs, etc.

Day 9: EVIDENCE COLLECTION (Sheet 9)
  ☐ Upload all documents to evidence repository
  ☐ Create hyperlinks in Sheet 9
  ☐ Verify all evidence accessible

Day 10: APPROVAL (Sheet 10)
  ☐ Submit for Legal, Procurement, Security, CISO review
  ☐ If approved → VENDOR READY FOR DEPLOYMENT
  ☐ If rejected → REMEDIATE or CANCEL

CRITICAL PATH:
  If vendor is HIGH RISK or requires TIA, 10 days is INSUFFICIENT.
  Budget 20-30 days for high-risk vendors.
```

---

#### Quick Reference 2: Monthly Maintenance (20-Minute Checklist)
```
MONTHLY VENDOR ASSESSMENT MAINTENANCE

Step 1: SYNC INVENTORY (5 min)
  ☐ Open IMP-5.23.1 (Cloud Service Inventory)
  ☐ Export vendor list
  ☐ Compare to Sheet 2 vendor list
  ☐ Add new vendors (trigger full assessment)
  ☐ Mark decommissioned vendors (archive)

Step 2: CERTIFICATION EXPIRY CHECK (5 min)
  ☐ Review Sheet 2 "Cert Expiry" column
  ☐ Flag certs expiring in next 60 days
  ☐ Email vendor: "Please provide updated certificate"
  ☐ If vendor doesn't respond in 14 days → ESCALATE to CISO

Step 3: CONTRACT RENEWAL ALERTS (5 min)
  ☐ Review Sheet 3 "Contract Renewal Date" column
  ☐ Flag contracts expiring in next 90 days
  ☐ Notify Procurement to begin renewal process
  ☐ Schedule vendor QBR if approaching renewal

Step 4: SLA BREACH REVIEW (5 min)
  ☐ Import ITSM incidents from last month
  ☐ Update Sheet 4 SLA performance
  ☐ Calculate penalties (if any)
  ☐ If penalties > €5,000 → Finance to invoice vendor
  ☐ If chronic breaches → QBR or vendor escalation

TOTAL TIME: ~20 minutes
SET CALENDAR REMINDER: 1st business day of each month
```

---

#### Quick Reference 3: Vendor Incident Response
```
VENDOR SECURITY INCIDENT - IMMEDIATE RESPONSE CHECKLIST

HOUR 0-1: INITIAL NOTIFICATION
  ☐ Vendor notifies [Organization] of breach/incident
  ☐ Log incident in Sheet 4 (SLA tracking)
  ☐ Notify CISO immediately
  ☐ If personal data involved → Notify DPO immediately
  ☐ Activate incident response team

HOUR 1-4: IMPACT ASSESSMENT
  ☐ Obtain vendor incident report (preliminary)
  ☐ Determine: What data was affected?
  ☐ Determine: How many users/records impacted?
  ☐ Determine: Is [Organization] data exposed?
  ☐ Update Sheet 8 risk rating to HIGH (temporary)

DAY 1-3: CONTAINMENT & COMMUNICATION
  ☐ Review Sheet 6: Invoke audit rights (demand forensic details)
  ☐ Review Sheet 3: Check incident notification SLA (was vendor compliant?)
  ☐ If GDPR breach → DPO to assess 72-hour notification requirement
  ☐ Communication plan: Internal stakeholders, customers (if needed)

DAY 7: VENDOR ACCOUNTABILITY
  ☐ Request formal incident report from vendor
  ☐ Review Sheet 3: Liability, indemnification clauses
  ☐ Legal assessment: Pursue damages/penalties?
  ☐ Document vendor's remediation plan

DAY 30: RE-ASSESSMENT
  ☐ Has vendor remediated root cause?
  ☐ Re-assess Sheet 2: Certifications still valid?
  ☐ Re-assess Sheet 8: Updated risk rating
  ☐ Decision: Continue, Enhanced Monitoring, or Exit

DAY 90: LESSONS LEARNED
  ☐ Incident post-mortem
  ☐ Update assessment framework (new criteria?)
  ☐ Archive incident case study
  ☐ Share with peer organizations (anonymized)
```

---

### 10.8 Troubleshooting Guide

**Common problems and solutions.**

| Problem | Symptoms | Solution |
|---------|----------|----------|
| **Vendor won't provide SOC 2 report** | "Our SOC 2 is confidential" | Explain SOC 2 is designed for customer sharing (standard practice). If vendor refuses, consider it RED FLAG. Alternative: Request alternative certification (ISO 27001) or accept higher risk with CISO approval. |
| **Vendor's ISO 27001 scope doesn't match services** | Certificate says "IT consulting" but we use their SaaS app | Request Letter of Applicability (LoA) from vendor explaining how SaaS is covered. If not covered, request re-scoping or alternative evidence. |
| **Contract has "no liability" clause** | MSA says "Vendor is not liable for any damages" | UNACCEPTABLE for critical vendors. Legal to negotiate liability cap (e.g., 12 months fees) or indemnification for gross negligence. |
| **Vendor refuses audit rights** | "We don't allow customer audits" | If critical vendor, this is DEAL-BREAKER (DORA requirement). Alternative: Accept third-party audit (e.g., SOC 2) in lieu of direct audit, but document this risk. |
| **US vendor claims "EU data residency = GDPR compliant"** | "We store your data in EU, so no problem" | FALSE. US vendor is still subject to CLOUD Act. Require TIA (Sheet 7) and CMK (Sheet 5) to mitigate. Document residual risk. |
| **Subprocessor list keeps changing** | Vendor adds/removes subprocessors monthly | Require contract clause: "Vendor must notify [Org] 30 days before adding subprocessor." Sheet 3 tracks. If vendor refuses, consider risk. |
| **SLA doesn't have financial penalties** | SLA says "99.9% uptime" but no penalty clause | Negotiate service credits or refunds for breaches. If vendor refuses, document this as risk (Sheet 4). Consider alternative vendors. |
| **Vendor acquired by US company mid-contract** | Microsoft buys EU vendor we're using | Trigger re-assessment. Check contract "change of control" clause (Sheet 3). If data now subject to CLOUD Act, require TIA and CMK or exit. |
| **Sheet formulas showing #REF! errors** | Cells display #REF! instead of values | Columns were deleted/moved. Re-run Python generator script to rebuild workbook with correct formulas. Do NOT manually fix. |
| **Import from IMP-5.23.1 fails** | "Vendor name not found" errors | Vendor names in IMP-5.23.1 and IMP-5.23.2 don't match exactly (typos, spaces). Standardize vendor names across both workbooks. |
| **DPO rejects TIA** | "Risk too high for US vendor" | Options: (1) Implement additional safeguards (CMK, data minimization), (2) Seek alternative vendor, (3) Escalate to executive decision if business-critical. |

---

### 10.9 Contact Information & Escalation Path

**Template - Customize for [Organization].**
```
VENDOR ASSESSMENT SUPPORT CONTACTS

GENERAL QUESTIONS:
  Security Compliance Team
  Email: security-compliance@[organization].com
  Teams: Security Compliance Channel
  Response Time: 1 business day

LEGAL/CONTRACT QUESTIONS (Sheet 3):
  Legal Department - Contracts
  Email: legal-contracts@[organization].com
  Phone: +XX XXX XXX XXXX
  Response Time: 2 business days
  Escalation: General Counsel

DATA PROTECTION QUESTIONS (Sheet 5, Sheet 7):
  Data Protection Officer (DPO)
  Email: dpo@[organization].com
  Phone: +XX XXX XXX XXXX
  Response Time: 3 business days (routine), 24 hours (urgent)
  Escalation: Privacy Steering Committee

PROCUREMENT/VENDOR MANAGEMENT (Sheet 4):
  Procurement Department
  Email: procurement@[organization].com
  Phone: +XX XXX XXX XXXX
  Response Time: 2 business days
  Escalation: CPO (Chief Procurement Officer)

TECHNICAL/CONFIGURATION QUESTIONS (Sheet 5, Sheet 6):
  Cloud Security Team
  Email: cloud-security@[organization].com
  Teams: Cloud Security Channel
  Response Time: 1 business day
  Escalation: Cloud Security Lead

EXECUTIVE APPROVALS (Sheet 10):
  CISO Office
  Email: ciso-office@[organization].com
  Response Time: 3 business days
  Escalation Path: CISO → CTO → CEO

VENDOR INCIDENT RESPONSE (24/7):
  Security Operations Center (SOC)
  Email: soc@[organization].com
  Phone: +XX XXX XXX XXXX (24/7 hotline)
  Response Time: Immediate
  Escalation: Incident Commander → CISO

AUDIT/COMPLIANCE QUESTIONS:
  Internal Audit
  Email: internal-audit@[organization].com
  Response Time: 3 business days
  Escalation: Chief Audit Executive

TOOL/WORKBOOK TECHNICAL ISSUES:
  ISMS Implementation Team
  Email: isms-admin@[organization].com
  Response Time: 1 business day
  Escalation: ISMS Program Manager
```

---

### 10.10 Document Revision History

**Tracking changes to this IMP document.**

| Version | Date | Section(s) Modified | Changes Summary | Author |
|---------|------|---------------------|-----------------|--------|
| 1.0 | [Date] | All | Initial release - Excel workbook specification only (Part II) | ISMS Team |

**Future Version Planning:**

| Planned Version | Target Date | Planned Changes |
|----------------|-------------|-----------------|
| 2.1 | Q2 2026 | Add automation examples (Python scripts for CMDB/ITSM integration) |
| 2.2 | Q3 2026 | Expand troubleshooting guide based on user feedback |
| 3.0 | Q1 2027 | Major update if regulatory landscape changes significantly (e.g., new EU-US data transfer framework) |

---

**END OF SECTION 10: APPENDICES & GLOSSARY**

**END OF PART I: USER COMPLETION GUIDE**

---

## PART II: TECHNICAL SPECIFICATION

### Excel Workbook Generation Specification

---

## Workbook Structure Overview

### Workbook Metadata

```python
WORKBOOK_CONFIG = {
    'filename': 'ISMS_A_5_23_2_Vendor_Due_Diligence_YYYYMMDD.xlsx',
    'sheet_count': 10,
    'base_columns': 'A-Q',  # Standard columns across all sheets
    'extended_columns': 'R-X',  # Sheet-specific columns
    'total_columns': 24,  # A-X
    'protection': True,  # Workbook protection enabled
    'formula_cells_locked': True,  # Formula cells locked
    'input_cells_unlocked': True  # User input cells unlocked
}
```

### Sheet Summary

| Sheet # | Name | Purpose | Rows (Est.) | Key Formulas |
|---------|------|---------|-------------|--------------|
| 1 | Instructions & Legend | User guidance, dropdown definitions | 50 | None |
| 2 | Vendor Security Certifications | ISO 27001, SOC 2, FedRAMP, CSA STAR tracking | 150 | Compliance % |
| 3 | Contract Terms Analysis | MSA, DPA, SLA clause adequacy assessment | 150 | Gap score |
| 4 | SLA Requirements & Performance | Uptime, support, breach notification tracking | 150 | Performance % |
| 5 | Data Sovereignty Compliance | Cross-border transfers, residency, SCCs | 150 | Compliance status |
| 6 | Forensics & Audit Rights | Right-to-audit, IR support, log access | 150 | Rights coverage % |
| 7 | Jurisdictional Risk Assessment | CLOUD Act, US nexus, EU data boundary | 150 | Risk rating |
| 8 | Summary Dashboard | Auto-calculated KPIs and compliance metrics | 100 | Multiple SUMIFs |
| 9 | Evidence Register | Audit trail with EV-VDD-### references | 200 | Auto-numbering |
| 10 | Approval Sign-Off | Legal → Procurement → DPO → CISO workflow | 80 | None |

**Total Estimated Rows:** ~1,230

---

## Standard Column Definitions (A-Q)

These columns appear in **Sheets 2-7** (assessment sheets):

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **A** | Vendor Name | Text | 20 | Dropdown (from 5.23.1) | Cloud service provider name |
| **B** | Service Name | Text | 25 | Free text | Specific service (e.g., "AWS EC2", "Microsoft 365") |
| **C** | Service Type | Text | 15 | Dropdown | SaaS/IaaS/PaaS/Security/Storage |
| **D** | Service Criticality | Text | 12 | Dropdown | Critical/High/Medium/Low |
| **E** | Assessment Date | Date | 12 | Date validation | DD.MM.YYYY |
| **F** | Assessor Name | Text | 18 | Free text | Person completing assessment |
| **G** | Status | Text | 12 | Dropdown | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / ⏸️ N/A |
| **H** | Compliance % | Number | 10 | Formula | Auto-calculated based on sheet criteria |
| **I** | Gap Description | Text | 30 | Free text | What's missing/inadequate |
| **J** | Remediation Required | Text | 15 | Dropdown | Yes/No/In Progress |
| **K** | Remediation Owner | Text | 18 | Free text | Person responsible for fix |
| **L** | Target Date | Date | 12 | Date validation | DD.MM.YYYY |
| **M** | Exception ID | Text | 15 | Free text | EXC-VDD-### if accepted risk |
| **N** | Risk ID | Text | 15 | Free text | RISK-### from risk register |
| **O** | Compensating Controls | Text | 30 | Free text | Alternative controls if gap exists |
| **P** | Evidence Location | Text | 40 | Free text | File path or URL |
| **Q** | Notes | Text | 30 | Free text | Additional context |

**Column Styling (A-Q):**
- Header row: Dark blue background (#003366), white bold text, centered
- Data rows: White background, black text, left-aligned (except dates/numbers)
- Status column (G): Conditional formatting based on value
- Compliance % column (H): Percentage format, conditional color coding

---

## Sheet 1: Instructions & Legend

### Purpose
Provide user guidance, define dropdown values, explain color coding, and document workbook usage.

### Structure

#### Section 1: Header (Rows 1-3)
```
Row 1: "ISMS-IMP-A.5.23.S2 – Vendor Due Diligence & Contracts"
       Font: Calibri 18pt Bold, Color: White, Background: Dark Blue (#003366)
       
Row 2: "ISO/IEC 27001:2022 - Control A.5.23: Cloud Services Security"
       Font: Calibri 12pt, Color: White, Background: Dark Blue (#003366)
       
Row 3: [Blank row for spacing]
```

#### Section 2: Document Information (Rows 4-13)
```
| Field | Value (Yellow highlight for user input) |
|-------|------------------------------------------|
| Document ID | ISMS-IMP-A.5.23.S2 |
| Assessment Area | Vendor Due Diligence & Contracts |
| Related Policy | ISMS-POL-A.5.19-23-S2, S5, S6 |
| Version | 2.0 |
| Assessment Date | [USER INPUT] |
| Completed By | [USER INPUT] |
| Organization | [USER INPUT] |
| Review Cycle | Quarterly (with annual comprehensive review) |
| Evidence Prefix | EV-VDD-### |
| Approvers | Legal → Procurement → DPO → CISO |
```

#### Section 3: How to Use This Workbook (Rows 15-30)
```
Instructions:
1. Start with Sheet 2 (Vendor Security Certifications)
2. Complete one vendor at a time across all relevant sheets
3. Use dropdown menus for standardized entries (prevents typos)
4. Yellow-highlighted cells require user input
5. If Status = "⚠️ Partial" or "❌ Non-Compliant", complete Gap Description
6. Provide evidence location for EVERY assessment entry
7. Summary Dashboard (Sheet 8) auto-calculates compliance metrics
8. Maintain Evidence Register (Sheet 9) for audit traceability
9. Complete Approval Sign-Off (Sheet 10) when assessment done

CRITICAL DEPENDENCIES:
- This assessment REQUIRES completed ISMS-IMP-A.5.23.S1 (Cloud Service Inventory)
- Vendor names MUST match exactly with inventory
- Service names MUST match exactly with inventory
```

#### Section 4: Status Legend (Rows 32-40)
```
| Symbol | Status | Meaning | Required Action |
|--------|--------|---------|----------------|
| ✅ | Compliant | Vendor meets all requirements | Maintain evidence |
| ⚠️ | Partial | Some requirements met, gaps exist | Document gaps, create remediation plan |
| ❌ | Non-Compliant | Requirements not met | Urgent remediation or risk acceptance |
| ⏸️ | N/A | Not applicable to this vendor/service | Document why N/A |
```

#### Section 5: Dropdown Value Definitions (Rows 42-80)

**Service Type:**
```
- SaaS: Software as a Service (complete applications)
- IaaS: Infrastructure as a Service (compute, storage, network)
- PaaS: Platform as a Service (development platforms)
- Security: Cloud security services (EDR, SIEM, WAF, etc.)
- Storage: Cloud storage/backup services
```

**Service Criticality:**
```
- Critical: Business停机 >4 hours = severe impact, financial loss
- High: Business停机 >1 day = significant impact
- Medium: Business停机 >1 week = moderate impact
- Low: Business停机 tolerable >1 week
```

**Certification Types (Sheet 2):**
```
- ISO 27001: Information security management
- SOC 2 Type II: Service organization controls (security)
- FedRAMP: US Federal cloud security authorization
- CSA STAR: Cloud Security Alliance certification
- PCI DSS: Payment card industry security
- HIPAA BAA: Healthcare data security
- ISO 27017: Cloud security controls
- ISO 27018: Cloud privacy controls
```

**Contract Clause Adequacy (Sheet 3):**
```
- Fully Adequate: Clause meets all requirements
- Partially Adequate: Clause exists but has gaps
- Inadequate: Clause missing or severely deficient
- Not Applicable: Clause not required for this vendor
```

**SLA Metrics (Sheet 4):**
```
Uptime Commitments:
- Tier 1: 99.99% (52 min/year downtime)
- Tier 2: 99.95% (4.38 hours/year)
- Tier 3: 99.9% (8.76 hours/year)
- Tier 4: 99.5% (1.83 days/year)
- Below Tier 4: <99.5% (inadequate for Critical/High services)

Support Response Times:
- P1 (Critical): < 1 hour
- P2 (High): < 4 hours
- P3 (Medium): < 8 hours
- P4 (Low): < 24 hours
```

**Data Transfer Mechanisms (Sheet 5):**
```
- Standard Contractual Clauses (SCCs): EU-approved
- Adequacy Decision: EU Commission approved jurisdiction
- Binding Corporate Rules (BCRs): Internal transfer mechanism
- Data Residency Guarantee: Data never leaves specified region
- Customer-Managed Keys: Organization controls encryption keys
```

**Jurisdictional Risk Levels (Sheet 7):**
```
- Low: EU/Swiss provider, data in EU/CH, no US nexus
- Medium: Non-US provider with some US connections (e.g., subprocessors)
- High: US-based provider OR parent company, mitigations exist
- Critical: US-based provider, no mitigations (CMK, EU boundary)
```

#### Section 6: Conditional Formatting Legend (Rows 82-95)
```
Status Column (G):
✅ Compliant       → Green background (#C6EFCE), dark green text (#006100)
⚠️ Partial         → Yellow background (#FFEB9C), dark yellow text (#9C6500)
❌ Non-Compliant   → Red background (#FFC7CE), dark red text (#9C0006)
⏸️ N/A             → Gray background (#D9D9D9), dark gray text (#7F7F7F)

Compliance % Column (H):
≥ 90%              → Green background
70-89%             → Yellow background
< 70%              → Red background

Risk Rating Column (Sheet 7):
Low                → Green background
Medium             → Yellow background
High               → Orange background
Critical           → Red background
```

#### Section 7: Evidence File Naming Convention (Rows 97-110)
```
Evidence files should follow this naming pattern:

[Evidence-Type]-[Vendor-Name]-[Document-Type]-[Year]-[Version].pdf

Examples:
CERT-AWS-ISO27001-2024-2027.pdf
CONTRACT-Microsoft-MSA-2024-v2.pdf
DPA-Salesforce-DPA-2025-Executed.pdf
SLA-Google-SLA-Report-Q4-2025.pdf
AUDIT-Azure-SOC2-TypeII-2025.pdf

Evidence Location Field (Column P):
Use relative paths from evidence repository root:
/Vendor-Due-Diligence-Evidence/Certifications/[filename]
/Vendor-Due-Diligence-Evidence/Contracts/[filename]
/Vendor-Due-Diligence-Evidence/SLA-Reports/[filename]
```

#### Section 8: Related Assessments (Rows 112-120)
```
Assessment Dependencies:

INPUT (Prerequisites):
✅ ISMS-IMP-A.5.23.S1 (Cloud Service Inventory)
   → Provides vendor list and service names

OUTPUT (Used By):
→ ISMS-IMP-A.5.23.S3 (Secure Configuration)
   → Uses vendor security capabilities documented here
→ ISMS-IMP-A.5.23.S4 (Ongoing Governance)
   → Uses contract terms and SLAs documented here
→ ISMS-IMP-A.5.23.S5 (Compliance Dashboard)
   → Aggregates vendor compliance metrics
```

#### Section 9: Quick Reference (Rows 122-140)
```
Common Scenarios:

Scenario 1: New Vendor Assessment
→ Complete Sheets 2-7 for new vendor
→ Focus on Sheet 2 (Certifications) and Sheet 3 (Contracts) first
→ Document evidence in Sheet 9
→ If gaps found, create remediation plan before contract signing

Scenario 2: Quarterly Review
→ Update Sheet 2 (check cert expiries)
→ Update Sheet 4 (SLA performance data)
→ Review Sheet 7 (jurisdictional changes?)
→ Refresh evidence in Sheet 9

Scenario 3: Contract Renewal
→ Review Sheet 3 (contract terms - any changes needed?)
→ Check Sheet 4 (SLA performance - negotiate improvements?)
→ Update Sheet 7 (jurisdictional risks changed?)
→ Obtain Legal/DPO approval (Sheet 10)

Scenario 4: Vendor M&A Event
→ IMMEDIATELY re-assess Sheet 7 (jurisdictional risk!)
→ Review Sheet 2 (certifications still valid?)
→ Check Sheet 3 (contract assignment clauses)
→ Update Sheet 6 (audit rights transferred?)
→ Escalate to CISO if risk profile changed significantly
```

---

## Sheet 2: Vendor Security Certifications

### Purpose
Track and verify vendor security certifications (ISO 27001, SOC 2, FedRAMP, CSA STAR, etc.)

### Structure

#### Header Row (Row 1)
Standard columns A-Q plus extended columns R-X:

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X |

**Standard Columns (A-Q):** As defined in Standard Column Definitions

**Extended Columns (R-X) - Certification-Specific:**

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **R** | ISO 27001 Status | Text | 18 | Dropdown | Yes - Valid / Yes - Expiring / No / Unknown |
| **S** | ISO 27001 Cert # | Text | 20 | Free text | Certificate number for verification |
| **T** | ISO 27001 Expiry | Date | 12 | Date validation | Certificate expiration date |
| **U** | SOC 2 Type II Status | Text | 18 | Dropdown | Yes - Valid / Yes - Expiring / No / Unknown |
| **V** | SOC 2 Report Date | Date | 12 | Date validation | Date of most recent SOC 2 report |
| **W** | FedRAMP Status | Text | 15 | Dropdown | Authorized / In Process / Not Authorized / N/A |
| **X** | Other Certifications | Text | 30 | Free text | CSA STAR, PCI DSS, HIPAA BAA, ISO 27017/27018 |

#### Formulas

**Compliance % (Column H):**
```excel
=ROUND(
  (COUNTIFS($R2,"Yes - Valid",$D2,"Critical")*1 +
   COUNTIFS($R2,"Yes - Valid",$D2,"High")*1 +
   COUNTIFS($U2,"Yes - Valid",$D2,"Critical")*0.5 +
   COUNTIFS($U2,"Yes - Valid",$D2,"High")*0.5) / 
  (COUNTIFS($D2,"Critical")*1 + COUNTIFS($D2,"High")*1) * 100
, 0)

Explanation:
- Critical services MUST have ISO 27001 (100% weight)
- High services MUST have ISO 27001 (100% weight)
- SOC 2 Type II provides 50% credit
- Medium/Low services: certifications recommended but not required
```

**Status (Column G) - Auto-Calculated:**
```excel
=IF(H2>=90,"✅ Compliant",
   IF(H2>=70,"⚠️ Partial",
      IF(H2<70,"❌ Non-Compliant","⏸️ N/A")))
```

#### Conditional Formatting

**ISO 27001 Expiry (Column T):**
```
Rule 1: <30 days from today → Red background, white text
Rule 2: 30-90 days from today → Yellow background, black text
Rule 3: >90 days from today → Green background, black text
```

**SOC 2 Report Date (Column V):**
```
Rule 1: >12 months old → Red background (expired)
Rule 2: 9-12 months old → Yellow background (refresh soon)
Rule 3: <9 months old → Green background (current)
```

#### Data Validation

**ISO 27001 Status (Column R):**
```
List: Yes - Valid, Yes - Expiring, No, Unknown
```

**SOC 2 Type II Status (Column U):**
```
List: Yes - Valid, Yes - Expiring, No, Unknown
```

**FedRAMP Status (Column W):**
```
List: Authorized, In Process, Not Authorized, N/A
```

#### Cell Protection
- Columns A-F, I-Q: Unlocked (user input)
- Columns G-H: Locked (formula cells)
- Columns R-X: Unlocked (user input)

---

## Sheet 3: Contract Terms Analysis

### Purpose
Assess adequacy of contract security clauses (MSA, DPA, SLA)

### Structure

#### Extended Columns (R-X) - Contract-Specific:

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **R** | MSA Exists | Text | 12 | Dropdown | Yes / No / In Negotiation |
| **S** | MSA Execution Date | Date | 15 | Date validation | Contract signature date |
| **T** | DPA Exists | Text | 12 | Dropdown | Yes / No / Not Required |
| **U** | DPA GDPR Compliant | Text | 18 | Dropdown | Fully Compliant / Partial / Non-Compliant / N/A |
| **V** | Liability Cap Adequate | Text | 18 | Dropdown | Adequate / Inadequate / No Cap |
| **W** | Indemnification Clause | Text | 18 | Dropdown | Comprehensive / Limited / None |
| **X** | Termination for Cause | Text | 18 | Dropdown | Yes / No / Unclear |

#### Additional Extended Columns (Y-AE) - Regulatory Compliance:

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **Y** | DORA Compliance (if applicable) | Text | 20 | Dropdown | Compliant / Partial / Not Present / N/A |
| **Z** | NIS2 Compliance (if applicable) | Text | 20 | Dropdown | Compliant / Partial / Not Present / N/A |
| **AA** | Data Return Clause | Text | 15 | Dropdown | Yes / No / Inadequate |
| **AB** | Subprocessor Approval | Text | 18 | Dropdown | Prior Written / General Authorization / None |
| **AC** | Breach Notification SLA | Text | 18 | Dropdown | <24h / <72h / >72h / Not Specified |
| **AD** | Security Incident Support | Text | 18 | Dropdown | Contractually Guaranteed / Best Effort / Not Specified |
| **AE** | Amendment Process | Text | 15 | Dropdown | Defined / Unclear / Not Addressed |

#### Formulas

**Compliance % (Column H):**
```excel
=ROUND(
  (COUNTIF(R2,"Yes")*10 +           // MSA exists
   COUNTIF(T2,"Yes")*10 +           // DPA exists  
   COUNTIF(U2,"Fully Compliant")*15 + // DPA GDPR compliant
   COUNTIF(V2,"Adequate")*10 +      // Liability cap
   COUNTIF(W2,"Comprehensive")*10 + // Indemnification
   COUNTIF(X2,"Yes")*10 +           // Termination clause
   COUNTIF(AA2,"Yes")*10 +          // Data return
   COUNTIF(AC2,"<72h")*15 +         // Breach notification
   COUNTIF(AD2,"Contractually Guaranteed")*10) / 100 * 100
, 0)

// Total possible: 100 points
```

#### Conditional Formatting

**DPA GDPR Compliant (Column U):**
```
Fully Compliant → Green
Partial → Yellow
Non-Compliant → Red
N/A → Gray
```

**Breach Notification SLA (Column AC):**
```
<24h → Green (exceeds GDPR requirement)
<72h → Yellow (meets GDPR requirement)
>72h → Red (fails GDPR requirement)
Not Specified → Red (non-compliant)
```

---

## Sheet 4: SLA Requirements & Performance

### Purpose
Track SLA commitments and actual performance metrics

### Structure

#### Extended Columns (R-X) - SLA-Specific:

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **R** | Uptime Commitment | Text | 15 | Dropdown | 99.99% / 99.95% / 99.9% / 99.5% / <99.5% / Not Specified |
| **S** | Actual Uptime (Last 12mo) | Number | 15 | Percentage | Actual measured uptime |
| **T** | SLA Met | Text | 10 | Formula | ✅ Yes / ❌ No |
| **U** | Support Response Time | Text | 18 | Dropdown | P1: <1h / P1: <4h / P1: <8h / Not Specified |
| **V** | Support SLA Met | Text | 10 | Dropdown | Yes / No / Not Measured |
| **W** | Service Credits Claimed | Text | 15 | Dropdown | Yes / No / Not Applicable |
| **X** | Performance Issues | Text | 30 | Free text | Description of SLA violations |

#### Additional Extended Columns (Y-AB):

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **Y** | Incident Count (Last 12mo) | Number | 15 | Integer | Number of service incidents |
| **Z** | Major Outages (Last 12mo) | Number | 15 | Integer | Outages >1 hour |
| **AA** | Root Cause Analysis Provided | Text | 20 | Dropdown | Always / Sometimes / Never / N/A |
| **AB** | SLA Improvement Needed | Text | 15 | Dropdown | Yes / No / Under Discussion |

#### Formulas

**SLA Met (Column T):**
```excel
=IF(S2>=VALUE(LEFT(R2,5))/100, "✅ Yes", "❌ No")

Explanation:
- Extracts percentage from Uptime Commitment (e.g., "99.99%" → 0.9999)
- Compares with Actual Uptime
- If actual ≥ commitment → ✅ Yes
- If actual < commitment → ❌ No
```

**Compliance % (Column H):**
```excel
=ROUND(
  (IF(T2="✅ Yes",50,0) +           // Uptime SLA met
   IF(V2="Yes",30,0) +             // Support SLA met
   IF(AA2="Always",20,0) +         // RCA provided
   IF(Z2=0,10,-10)) / 110 * 100    // No major outages (bonus/penalty)
, 0)

// Total possible: 110 points (can exceed 100%)
```

#### Conditional Formatting

**Actual Uptime (Column S):**
```
≥ Committed → Green
0.1-0.5% below → Yellow
>0.5% below → Red
```

**Major Outages (Column Z):**
```
0 outages → Green
1-2 outages → Yellow
>2 outages → Red
```

#### Data Validation

**Uptime Commitment (Column R):**
```
List: 99.99%, 99.95%, 99.9%, 99.5%, <99.5%, Not Specified
```

**Root Cause Analysis Provided (Column AA):**
```
List: Always, Sometimes, Never, N/A
```

---

## Sheet 5: Data Sovereignty Compliance

### Purpose
Assess data residency, cross-border transfers, and sovereignty compliance

### Structure

#### Extended Columns (R-X) - Data Sovereignty-Specific:

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **R** | Primary Data Location | Text | 20 | Dropdown | Switzerland / EU / USA / Asia-Pacific / Multi-Region / Unknown |
| **S** | Data Processing Locations | Text | 25 | Free text | All regions where data may be processed |
| **T** | Cross-Border Transfers | Text | 15 | Dropdown | Yes / No / Unknown |
| **U** | Transfer Mechanism | Text | 20 | Dropdown | SCCs / Adequacy Decision / BCRs / Data Residency Guarantee / CMK / None |
| **V** | DPA Covers Transfers | Text | 15 | Dropdown | Yes / No / Partial / N/A |
| **W** | Customer-Managed Keys | Text | 18 | Dropdown | Available & Enabled / Available Not Enabled / Not Available |
| **X** | Encryption Key Custody | Text | 18 | Dropdown | Customer / Provider / Shared / Unknown |

#### Additional Extended Columns (Y-AD):

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **Y** | Subprocessor Locations | Text | 25 | Free text | Jurisdictions of key subprocessors |
| **Z** | Data Residency Contractual | Text | 18 | Dropdown | Guaranteed / Best Effort / Not Specified |
| **AA** | Data Export Format | Text | 18 | Dropdown | Standard Format / Proprietary / Unknown |
| **AB** | GDPR Art 28 Compliant | Text | 15 | Dropdown | Yes / No / Partial / N/A |
| **AC** | FADP Compliant | Text | 15 | Dropdown | Yes / No / Partial / N/A |
| **AD** | Transfer Impact Assessment | Text | 18 | Dropdown | Completed / Not Required / Overdue |

#### Formulas

**Compliance % (Column H):**
```excel
=ROUND(
  (IF(OR(R2="Switzerland",R2="EU"),20,0) +                    // Data in safe jurisdiction
   IF(T2="No",20,IF(U2<>"None",10,0)) +                      // No transfers OR valid mechanism
   IF(V2="Yes",15,0) +                                        // DPA covers transfers
   IF(OR(W2="Available & Enabled",X2="Customer"),15,0) +     // CMK or customer key custody
   IF(AB2="Yes",15,0) +                                       // GDPR compliant
   IF(AC2="Yes",15,0)) / 100 * 100                           // FADP compliant
, 0)

// Total possible: 100 points
```

**Status (Column G) - Data Sovereignty-Specific:**
```excel
=IF(AND(OR(R2="Switzerland",R2="EU"), T2="No"), "✅ Compliant",
   IF(AND(T2="Yes", OR(U2="SCCs",U2="Adequacy Decision",U2="CMK")), "⚠️ Partial",
      IF(AND(T2="Yes", U2="None"), "❌ Non-Compliant", "⏸️ N/A")))

Explanation:
- Data in CH/EU with no transfers → Fully Compliant
- Transfers with valid mechanism (SCCs/Adequacy/CMK) → Partial
- Transfers with no mechanism → Non-Compliant
```

#### Conditional Formatting

**Primary Data Location (Column R):**
```
Switzerland → Dark Green
EU → Green
USA → Yellow
Asia-Pacific → Yellow
Multi-Region → Orange
Unknown → Red
```

**Transfer Mechanism (Column U):**
```
SCCs / Adequacy Decision / CMK → Green
BCRs / Data Residency Guarantee → Yellow
None → Red
```

**Transfer Impact Assessment (Column AD):**
```
Completed → Green
Not Required → Gray
Overdue → Red
```

#### Data Validation

**Primary Data Location (Column R):**
```
List: Switzerland, EU, USA, Asia-Pacific, Multi-Region, Unknown
```

**Transfer Mechanism (Column U):**
```
List: SCCs, Adequacy Decision, BCRs, Data Residency Guarantee, CMK, None
```

**Customer-Managed Keys (Column W):**
```
List: Available & Enabled, Available Not Enabled, Not Available
```

---

## Sheet 6: Forensics & Audit Rights

### Purpose
Assess incident investigation support, audit rights, and log access

### Structure

#### Extended Columns (R-X) - Forensics-Specific:

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **R** | Right to Audit Clause | Text | 15 | Dropdown | Yes / No / Limited |
| **S** | Audit Frequency Allowed | Text | 18 | Dropdown | Anytime / Annually / Biennially / On Request / Not Specified |
| **T** | Third-Party Audit Accepted | Text | 18 | Dropdown | Yes / No / With Approval |
| **U** | Forensic Investigation Support | Text | 20 | Dropdown | Contractual / Best Effort / Not Guaranteed |
| **V** | Log Retention Period | Text | 15 | Dropdown | 12+ months / 6-12 months / <6 months / Unknown |
| **W** | Log Access Method | Text | 18 | Dropdown | API / Portal / On Request / Not Provided |
| **X** | IR Cooperation SLA | Text | 15 | Dropdown | <24h / <72h / Best Effort / Not Specified |

#### Additional Extended Columns (Y-AC):

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **Y** | Forensic Data Preservation | Text | 20 | Dropdown | Guaranteed / On Request / Not Available |
| **Z** | Chain of Custody Support | Text | 18 | Dropdown | Yes / Limited / No |
| **AA** | Legal Hold Support | Text | 15 | Dropdown | Yes / No / Unknown |
| **AB** | E-Discovery Support | Text | 15 | Dropdown | Yes / Limited / No |
| **AC** | Audit Trail Integrity | Text | 18 | Dropdown | Cryptographically Protected / Logged / Unverified |

#### Formulas

**Compliance % (Column H):**
```excel
=ROUND(
  (IF(R2="Yes",20,IF(R2="Limited",10,0)) +         // Right to audit
   IF(T2="Yes",15,0) +                             // Third-party audit accepted
   IF(U2="Contractual",20,0) +                     // Forensic support guaranteed
   IF(V2="12+ months",15,0) +                      // Adequate log retention
   IF(W2<>"Not Provided",10,0) +                   // Log access available
   IF(X2="<24h",10,IF(X2="<72h",5,0)) +           // IR cooperation SLA
   IF(AC2="Cryptographically Protected",10,0))     // Audit trail integrity
/ 100 * 100
, 0)

// Total possible: 100 points
```

#### Conditional Formatting

**Right to Audit Clause (Column R):**
```
Yes → Green
Limited → Yellow
No → Red
```

**Log Retention Period (Column V):**
```
12+ months → Green
6-12 months → Yellow
<6 months → Orange
Unknown → Red
```

**IR Cooperation SLA (Column X):**
```
<24h → Green
<72h → Yellow
Best Effort → Orange
Not Specified → Red
```

#### Data Validation

**Right to Audit Clause (Column R):**
```
List: Yes, No, Limited
```

**Audit Frequency Allowed (Column S):**
```
List: Anytime, Annually, Biennially, On Request, Not Specified
```

**Forensic Investigation Support (Column U):**
```
List: Contractual, Best Effort, Not Guaranteed
```

**Log Retention Period (Column V):**
```
List: 12+ months, 6-12 months, <6 months, Unknown
```

**Audit Trail Integrity (Column AC):**
```
List: Cryptographically Protected, Logged, Unverified
```

#### Special Notes

**Critical Services:**
- Right to Audit: MUST be "Yes" (not "Limited")
- Log Retention: MUST be "12+ months"
- Forensic Support: MUST be "Contractual"
- IR Cooperation: SHOULD be "<24h"

**High Services:**
- Right to Audit: SHOULD be "Yes"
- Log Retention: SHOULD be "12+ months"
- Forensic Support: SHOULD be "Contractual"

**Audit Considerations:**
- If Right to Audit = "No" → Flag for contract renegotiation
- If Third-Party Audit = "No" → Ensure internal audit capability exists
- If Log Access = "Not Provided" → Major compliance gap for regulated industries

---

## Sheet 7: Jurisdictional Risk Assessment

### Purpose
Assess US CLOUD Act exposure, EU Data Boundary commitments, and jurisdictional risks

**NOTE:** This sheet was added to address DORA Article 30.2(j), NIS2 Article 21.2(h), and ongoing US-EU data transfer concerns.

### Structure

#### Extended Columns (R-X) - Jurisdictional Risk-Specific:

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **R** | Provider HQ Jurisdiction | Text | 20 | Dropdown | USA / EU / Switzerland / UK / Other / Unknown |
| **S** | Parent Company Location | Text | 20 | Dropdown | USA / EU / Switzerland / UK / Other / None / Unknown |
| **T** | US Nexus Detected | Text | 12 | Dropdown | Yes / No / Unclear |
| **U** | CLOUD Act Exposure | Text | 15 | Dropdown | Direct / Indirect / Minimal / None |
| **V** | EU Data Boundary Commitment | Text | 20 | Dropdown | Contractual Guarantee / Technical / Both / None |
| **W** | Customer-Managed Keys | Text | 15 | Dropdown | Enabled / Available / Not Available |
| **X** | Jurisdictional Risk Rating | Text | 15 | Formula | Low / Medium / High / Critical |

#### Additional Extended Columns (Y-AE):

| Col | Header | Type | Width | Validation | Description |
|-----|--------|------|-------|------------|-------------|
| **Y** | US Subprocessors | Text | 15 | Dropdown | Yes / No / Unknown |
| **Z** | EU-Only Infrastructure Option | Text | 18 | Dropdown | Yes / No / Planned |
| **AA** | Data Localization Controls | Text | 20 | Dropdown | Technical Guarantee / Contractual / None |
| **AB** | Compensating Controls | Text | 30 | Free text | CMK, EU boundary, encryption, etc. |
| **AC** | DORA Compliance Notes | Text | 30 | Free text | Concentration risk, jurisdiction notes |
| **AD** | Risk Acceptance Required | Text | 15 | Formula | Yes / No |
| **AE** | Risk Accepted By | Text | 18 | Free text | CISO / CRO / Board (if accepted) |

#### Formulas

**Jurisdictional Risk Rating (Column X):**
```excel
=IF(AND(U2="None", R2<>"USA", S2<>"USA"), "Low",
   IF(AND(OR(U2="Minimal",U2="Indirect"), OR(W2="Enabled",V2<>"None")), "Medium",
      IF(AND(U2="Direct", W2="Not Available"), "Critical",
         "High")))

Logic:
- Low: No US nexus, no CLOUD Act exposure
- Medium: Minimal/Indirect exposure WITH mitigations (CMK or EU boundary)
- High: Some US connection, limited mitigations
- Critical: Direct US exposure, no mitigations (CMK unavailable)
```

**Risk Acceptance Required (Column AD):**
```excel
=IF(AND(X2="Critical", D2="Critical"), "Yes - CISO Approval",
   IF(AND(X2="High", D2="Critical"), "Yes - CISO Approval",
      IF(AND(X2="High", D2="High"), "Yes - Security Team",
         "No")))

Logic:
- Critical risk + Critical service → CISO approval mandatory
- High risk + Critical service → CISO approval mandatory
- High risk + High service → Security team approval required
- All other combinations → No explicit approval needed
```

**Compliance % (Column H):**
```excel
=IF(X2="Low", 100,
   IF(AND(X2="Medium", LEN(AB2)>10), 80,  // Medium risk WITH compensating controls
      IF(AND(X2="High", LEN(AB2)>10), 60,  // High risk WITH compensating controls
         IF(X2="Critical", 20, 40))))       // Critical risk OR High/Medium without controls

Scoring:
- Low risk → 100% compliant
- Medium risk + compensating controls → 80%
- High risk + compensating controls → 60%
- Medium/High without controls → 40%
- Critical risk → 20% (requires urgent remediation)
```

#### Conditional Formatting

**CLOUD Act Exposure (Column U):**
```
None → Green
Minimal → Light Green
Indirect → Yellow
Direct → Red
```

**Jurisdictional Risk Rating (Column X):**
```
Low → Dark Green background (#006100), white text
Medium → Yellow background (#FFEB9C), black text
High → Orange background (#FFC000), white text
Critical → Red background (#C00000), white text
```

**Risk Acceptance Required (Column AD):**
```
"Yes - CISO Approval" → Red background
"Yes - Security Team" → Yellow background
"No" → Green background
```

#### Data Validation

**Provider HQ Jurisdiction (Column R):**
```
List: USA, EU, Switzerland, UK, Other, Unknown
```

**CLOUD Act Exposure (Column U):**
```
List: Direct, Indirect, Minimal, None
```

**EU Data Boundary Commitment (Column V):**
```
List: Contractual Guarantee, Technical, Both, None
```

**Customer-Managed Keys (Column W):**
```
List: Enabled, Available, Not Available
```

#### Special Assessment Logic

**US Nexus Decision Tree:**
```
1. Provider HQ = USA? 
   → Yes: US Nexus = "Yes", CLOUD Act Exposure = "Direct"
   
2. Parent Company = USA?
   → Yes: US Nexus = "Yes", CLOUD Act Exposure = "Direct"
   
3. US Subprocessors = "Yes"?
   → Yes: US Nexus = "Yes", CLOUD Act Exposure = "Indirect"
   
4. None of above?
   → US Nexus = "No", CLOUD Act Exposure = "Minimal" or "None"
```

**Mitigation Effectiveness:**
```
Best Mitigations (reduces risk by 2 levels):
- Customer-Managed Keys (CMK) + EU Data Boundary (Technical)
- EU-only infrastructure with contractual guarantee

Good Mitigations (reduces risk by 1 level):
- CMK enabled (without EU boundary)
- EU Data Boundary (contractual only)

Weak Mitigations (reduces risk by 0.5 levels):
- Encryption (provider-managed keys)
- Contractual assurances only
```

#### Critical Services Special Rules

For services where **Service Criticality = "Critical"**:

- If **CLOUD Act Exposure = "Direct"** AND **CMK = "Not Available"**
  → Assessment Status MUST be "❌ Non-Compliant"
  → Risk Acceptance = "Yes - CISO Approval"
  → Document in Compensating Controls or escalate

- If **CLOUD Act Exposure = "Direct"** AND **CMK = "Enabled"**
  → Assessment Status = "⚠️ Partial"
  → Document in Compensating Controls

- If **CLOUD Act Exposure = "None" or "Minimal"**
  → No special restrictions

#### DORA-Specific Fields

**DORA Compliance Notes (Column AC):**
Document the following for DORA entities:
- Concentration risk: How many Critical services with this provider?
- Jurisdiction risk: Does provider jurisdiction create compliance concerns?
- Exit strategy: Can we exit to non-US provider if needed?
- Regulatory reporting: Does this require notification to regulator?

---

## Sheet 8: Summary Dashboard

### Purpose
Auto-calculate compliance metrics across all assessment sheets

### Structure

#### Section 1: Overall Compliance Summary (Rows 1-15)

**Dashboard Header:**
```
Row 1: "VENDOR DUE DILIGENCE SUMMARY DASHBOARD"
       Font: Calibri 16pt Bold, Color: White, Background: Dark Blue (#003366)
       
Row 2: "Auto-calculated from Sheets 2-7"
       Font: Calibri 10pt Italic, Color: Gray
```

**Overall Metrics (Rows 4-15):**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| **Total Vendors Assessed** | `=COUNTA(Sheet2!A:A)-1` | N/A | Count |
| **Critical Services** | `=COUNTIF(Sheet2!D:D,"Critical")` | N/A | Count |
| **High Services** | `=COUNTIF(Sheet2!D:D,"High")` | N/A | Count |
| **Overall Compliance %** | `=AVERAGE(Sheet2!H:H,Sheet3!H:H,Sheet4!H:H,Sheet5!H:H,Sheet6!H:H,Sheet7!H:H)` | ≥80% | % |
| **Fully Compliant Vendors** | `=COUNTIF(Sheet2!G:G,"✅ Compliant")` | 100% | Count |
| **Partial Compliance** | `=COUNTIF(Sheet2!G:G,"⚠️ Partial")` | 0 | Count |
| **Non-Compliant Vendors** | `=COUNTIF(Sheet2!G:G,"❌ Non-Compliant")` | 0 | Count |

#### Section 2: Domain-Specific Compliance (Rows 17-30)

| Assessment Domain | Compliance % | Gaps | Status |
|-------------------|--------------|------|--------|
| **Vendor Security Certifications** | `=AVERAGE(Sheet2!H:H)` | `=COUNTIF(Sheet2!G:G,"❌ Non-Compliant")` | Conditional |
| **Contract Terms Analysis** | `=AVERAGE(Sheet3!H:H)` | `=COUNTIF(Sheet3!G:G,"❌ Non-Compliant")` | Conditional |
| **SLA Requirements** | `=AVERAGE(Sheet4!H:H)` | `=COUNTIF(Sheet4!G:G,"❌ Non-Compliant")` | Conditional |
| **Data Sovereignty** | `=AVERAGE(Sheet5!H:H)` | `=COUNTIF(Sheet5!G:G,"❌ Non-Compliant")` | Conditional |
| **Forensics & Audit Rights** | `=AVERAGE(Sheet6!H:H)` | `=COUNTIF(Sheet6!G:G,"❌ Non-Compliant")` | Conditional |
| **Jurisdictional Risk** | `=AVERAGE(Sheet7!H:H)` | `=COUNTIF(Sheet7!X:X,"Critical")` | Conditional |

**Conditional Formatting (Status Column):**
```
≥90% → Green "✅ Good"
70-89% → Yellow "⚠️ Needs Improvement"
<70% → Red "❌ Action Required"
```

#### Section 3: Top Risks (Rows 32-45)

**Critical Risk Vendors:**
```
Lists all vendors where:
- Sheet7!X = "Critical" (Jurisdictional risk)
- Sheet2!G = "❌ Non-Compliant" (No certifications)
- Sheet3!G = "❌ Non-Compliant" (Contract gaps)
- Sheet4!T = "❌ No" (SLA violations)

Formula: =FILTER(Sheet2!A:A, (Sheet7!X:X="Critical")+(Sheet2!G:G="❌ Non-Compliant"))
```

#### Section 4: Remediation Tracker (Rows 47-60)

| Priority | Vendor | Issue | Target Date | Owner | Status |
|----------|--------|-------|-------------|-------|--------|
| P1 | Auto-populated from sheets where G="❌" and D="Critical" | | | | |
| P2 | Auto-populated from sheets where G="❌" and D="High" | | | | |
| P3 | Auto-populated from sheets where G="⚠️" and D="Critical" | | | | |

#### Section 5: Certification Status Summary (Rows 62-75)

**Certification Coverage:**

| Certification Type | Critical Services | High Services | Total Coverage % |
|--------------------|-------------------|---------------|------------------|
| **ISO 27001** | `=COUNTIFS(Sheet2!R:R,"Yes*",Sheet2!D:D,"Critical")` | `=COUNTIFS(Sheet2!R:R,"Yes*",Sheet2!D:D,"High")` | Formula |
| **SOC 2 Type II** | `=COUNTIFS(Sheet2!U:U,"Yes*",Sheet2!D:D,"Critical")` | `=COUNTIFS(Sheet2!U:U,"Yes*",Sheet2!D:D,"High")` | Formula |
| **FedRAMP** | `=COUNTIFS(Sheet2!W:W,"Authorized",Sheet2!D:D,"Critical")` | `=COUNTIFS(Sheet2!W:W,"Authorized",Sheet2!D:D,"High")` | Formula |

**Expiring Certifications (Next 90 Days):**
```
=FILTER(Sheet2!A:T, Sheet2!T:T <= TODAY()+90, Sheet2!T:T >= TODAY())

Returns: Vendor Name, Service Name, ISO 27001 Cert #, Expiry Date
```

#### Section 6: Contract Gaps Summary (Rows 77-90)

**Most Common Gaps:**

| Gap Type | Count | Affected Services | Criticality |
|----------|-------|-------------------|-------------|
| **No DPA** | `=COUNTIF(Sheet3!T:T,"No")` | List | High |
| **Inadequate Liability Cap** | `=COUNTIF(Sheet3!V:V,"Inadequate")` | List | Medium |
| **No Breach Notification SLA** | `=COUNTIF(Sheet3!AC:AC,"Not Specified")` | List | Critical |
| **No Data Return Clause** | `=COUNTIF(Sheet3!AA:AA,"No")` | List | High |

#### Section 7: Data Sovereignty Risks (Rows 92-105)

**Cross-Border Transfer Summary:**

| Jurisdiction | Services | Transfer Mechanism | Risk Level |
|--------------|----------|-------------------|------------|
| **USA** | `=COUNTIF(Sheet5!R:R,"USA")` | `=COUNTIFS(Sheet5!R:R,"USA",Sheet5!U:U,"SCCs")` | Auto |
| **EU** | `=COUNTIF(Sheet5!R:R,"EU")` | N/A | Low |
| **Switzerland** | `=COUNTIF(Sheet5!R:R,"Switzerland")` | N/A | Low |
| **Multi-Region** | `=COUNTIF(Sheet5!R:R,"Multi-Region")` | Various | Medium-High |

**CLOUD Act Exposure:**
```
Critical Exposure: =COUNTIF(Sheet7!U:U,"Direct")
High Exposure: =COUNTIF(Sheet7!U:U,"Indirect")
Mitigated: =COUNTIFS(Sheet7!U:U,"Direct",Sheet7!W:W,"Enabled")
```

#### Section 8: SLA Performance Trends (Rows 107-120)

**Performance Summary:**

| Metric | Value | Trend |
|--------|-------|-------|
| **Vendors Meeting SLA** | `=COUNTIF(Sheet4!T:T,"✅ Yes")` | Target: 100% |
| **Vendors Below SLA** | `=COUNTIF(Sheet4!T:T,"❌ No")` | Target: 0 |
| **Major Outages (12mo)** | `=SUM(Sheet4!Z:Z)` | Target: <5 |
| **Unclaimed Service Credits** | `=COUNTIF(Sheet4!W:W,"No")` | Opportunity $ |

---

## Sheet 9: Evidence Register

### Purpose
Maintain audit trail of all evidence with EV-VDD-### references

### Structure

#### Columns (A-M):

| Col | Header | Type | Width | Description |
|-----|--------|------|-------|-------------|
| **A** | Evidence ID | Text | 15 | EV-VDD-001, EV-VDD-002, ... (auto-increment) |
| **B** | Vendor Name | Text | 20 | From Sheet 2-7 |
| **C** | Service Name | Text | 25 | From Sheet 2-7 |
| **D** | Evidence Type | Text | 20 | Certification / Contract / SLA Report / Audit Report / Other |
| **E** | Document Title | Text | 40 | Full document name |
| **F** | Document Date | Date | 12 | When document was created/issued |
| **G** | Upload Date | Date | 12 | When added to evidence repository |
| **H** | File Location | Text | 50 | Full path in repository |
| **I** | File Size | Text | 10 | MB/KB |
| **J** | Validity Period | Text | 15 | Start - End dates (for certs) |
| **K** | Next Review Date | Date | 12 | When evidence should be refreshed |
| **L** | Uploaded By | Text | 18 | Person who added evidence |
| **M** | Notes | Text | 30 | Additional context |

#### Formulas

**Evidence ID (Column A):**
```excel
="EV-VDD-" & TEXT(ROW()-1,"000")

Example outputs:
Row 2 → EV-VDD-001
Row 3 → EV-VDD-002
...
Row 101 → EV-VDD-100
```

**Next Review Date (Column K):**
```excel
=IF(D2="Certification", F2+365,           // Certifications: 1 year
   IF(D2="Contract", F2+1095,             // Contracts: 3 years
      IF(D2="SLA Report", F2+90,          // SLA reports: 90 days
         F2+365)))                         // Default: 1 year
```

#### Conditional Formatting

**Next Review Date (Column K):**
```
< TODAY() → Red (overdue)
< TODAY()+30 → Yellow (due soon)
> TODAY()+30 → Green (current)
```

#### Data Validation

**Evidence Type (Column D):**
```
List: Certification, Contract, SLA Report, Audit Report, DPA, Security Questionnaire, Other
```

#### Evidence Linking

Each row in Sheets 2-7 should reference evidence using:
```
Column P (Evidence Location): EV-VDD-001, EV-VDD-005, EV-VDD-017
```

This creates traceability:
- Sheet 2 (Certifications) Row 5 → "EV-VDD-023"
- Evidence Register Row 24 → Full details of certificate

---

## Sheet 10: Approval Sign-Off

### Purpose
Multi-stakeholder approval workflow (Legal → Procurement → DPO → CISO)

### Structure

#### Section 1: Assessment Summary (Rows 1-10)

```
Assessment Completion Date: [USER INPUT]
Total Vendors Assessed: [FORMULA from Sheet 8]
Compliance %: [FORMULA from Sheet 8]
Critical Gaps: [FORMULA from Sheet 8]
Recommended Action: [USER INPUT: Approve / Conditional Approval / Reject]
```

#### Section 2: Legal Review (Rows 12-20)

| Field | Value |
|-------|-------|
| **Reviewer Name** | [USER INPUT] |
| **Review Date** | [USER INPUT] |
| **Contract Adequacy** | [Dropdown: Adequate / Needs Amendment / Inadequate] |
| **DPA Compliance** | [Dropdown: Compliant / Non-Compliant / N/A] |
| **Key Legal Concerns** | [Free text] |
| **Approval Status** | [Dropdown: Approved / Conditional / Rejected] |
| **Signature** | [USER INPUT] |

#### Section 3: Procurement Review (Rows 22-30)

| Field | Value |
|-------|-------|
| **Reviewer Name** | [USER INPUT] |
| **Review Date** | [USER INPUT] |
| **SLA Adequacy** | [Dropdown: Adequate / Needs Improvement / Inadequate] |
| **Vendor Performance** | [Dropdown: Exceeds / Meets / Below Expectations] |
| **Cost Optimization Notes** | [Free text] |
| **Approval Status** | [Dropdown: Approved / Conditional / Rejected] |
| **Signature** | [USER INPUT] |

#### Section 4: DPO Review (Rows 32-42)

| Field | Value |
|-------|-------|
| **Reviewer Name** | [USER INPUT] |
| **Review Date** | [USER INPUT] |
| **Data Sovereignty Compliant** | [Dropdown: Yes / No / Conditional] |
| **Transfer Mechanisms Adequate** | [Dropdown: Yes / No / N/A] |
| **GDPR/FADP Risks** | [Free text] |
| **TIA Required** | [Dropdown: Completed / Not Required / Pending] |
| **Key DPO Concerns** | [Free text] |
| **Approval Status** | [Dropdown: Approved / Conditional / Rejected] |
| **Signature** | [USER INPUT] |

#### Section 5: CISO Final Approval (Rows 44-55)

| Field | Value |
|-------|-------|
| **Reviewer Name** | [USER INPUT] |
| **Review Date** | [USER INPUT] |
| **Security Posture Assessment** | [Dropdown: Strong / Adequate / Weak / Unacceptable] |
| **Residual Risk Level** | [Dropdown: Low / Medium / High / Critical] |
| **Risk Acceptance Decision** | [Dropdown: Accepted / Conditional / Rejected] |
| **Compensating Controls Required** | [Free text] |
| **Review Frequency Override** | [Dropdown: Quarterly / Semi-Annual / Annual] |
| **Final Approval Status** | [Dropdown: ✅ APPROVED / ⚠️ CONDITIONAL / ❌ REJECTED] |
| **CISO Signature** | [USER INPUT] |
| **Date** | [USER INPUT] |

#### Section 6: Approval Workflow Status (Rows 57-65)

```
Legal:       [ ] Pending  [ ] Approved  [ ] Conditional  [ ] Rejected
Procurement: [ ] Pending  [ ] Approved  [ ] Conditional  [ ] Rejected
DPO:         [ ] Pending  [ ] Approved  [ ] Conditional  [ ] Rejected
CISO:        [ ] Pending  [ ] Approved  [ ] Conditional  [ ] Rejected

Overall Status: [FORMULA]
```

**Overall Status Formula:**
```excel
=IF(COUNTIF(F12:F42,"Rejected")>0, "❌ REJECTED - See Comments",
   IF(COUNTIF(F12:F42,"Conditional")>0, "⚠️ CONDITIONAL APPROVAL - Action Required",
      IF(COUNTIF(F12:F42,"Approved")=4, "✅ FULLY APPROVED", "⏸️ PENDING REVIEW")))
```

#### Conditional Formatting

**Approval Status Fields:**
```
"Approved" → Green background
"Conditional" → Yellow background
"Rejected" → Red background
"Pending" → Gray background
```

**Final Approval Status:**
```
"✅ FULLY APPROVED" → Dark green background, white text
"⚠️ CONDITIONAL APPROVAL" → Yellow background, black text
"❌ REJECTED" → Red background, white text
"⏸️ PENDING REVIEW" → Gray background, black text
```

---

## Cell Protection & Workbook Security

### Protection Strategy

**Formula Cells (LOCKED):**
- All cells containing formulas in Sheets 2-8
- Prevents accidental deletion/modification
- User cannot edit these cells

**User Input Cells (UNLOCKED):**
- Yellow-highlighted cells in all sheets
- Evidence location fields
- Notes and description fields
- Approval sign-off fields

**Protection Password:**
```
Recommended: Set workbook protection password
- Prevents unauthorized unprotection
- Document password in secure location
- Change quarterly
```

### Workbook-Level Protection

```python
# In Python generator script:
workbook.protection.workbookPassword = 'SecurePassword123!'  # Change this
workbook.protection.lockStructure = True  # Prevent sheet deletion/reordering
workbook.protection.lockWindows = False  # Allow window resizing
```

### Sheet-Level Protection

```python
# For each sheet:
sheet.protection.sheet = True
sheet.protection.password = 'SecurePassword123!'  # Match workbook password
sheet.protection.formatCells = False
sheet.protection.formatColumns = False
sheet.protection.formatRows = False
sheet.protection.insertColumns = False
sheet.protection.insertRows = False
sheet.protection.deleteColumns = False
sheet.protection.deleteRows = False
```

---

## Integration Points

### Input Dependencies

**From ISMS-IMP-A.5.23.S1 (Cloud Service Inventory):**
- Vendor names (must match exactly)
- Service names (must match exactly)
- Service types (SaaS/IaaS/PaaS/Security/Storage)
- Service criticality (Critical/High/Medium/Low)

**Integration Method:**
```
Option 1: Manual - Copy vendor/service lists from A.5.23.1
Option 2: Automated - Python script reads A.5.23.1, pre-populates A.5.23.2
Option 3: Dropdown - A.5.23.2 dropdowns pull from A.5.23.1 (requires Excel data connections)
```

### Output Destinations

**To ISMS-IMP-A.5.23.S3 (Secure Configuration):**
- Vendor security capabilities (from Sheet 2)
- Contract security requirements (from Sheet 3)

**To ISMS-IMP-A.5.23.S4 (Ongoing Governance):**
- SLA commitments (from Sheet 4)
- Audit rights (from Sheet 6)
- Contract terms (from Sheet 3)

**To ISMS-IMP-A.5.23.S5 (Compliance Dashboard):**
- Overall compliance % (from Sheet 8)
- Vendor risk ratings (from Sheet 7)
- Gap counts (from Sheet 8)
- Evidence register (from Sheet 9)

---

## Python Generator Script Notes

### Key Considerations

1. **Dropdown Data Sources:**
   - Create named ranges for dropdown lists
   - Reference named ranges in data validation
   - Ensure lists are comprehensive

2. **Formula Cell Identification:**
   - Mark formula cells during generation
   - Lock formula cells automatically
   - Leave user input cells unlocked

3. **Conditional Formatting Rules:**
   - Apply after all data is populated
   - Test with sample data
   - Ensure rules don't conflict

4. **Performance Optimization:**
   - Avoid volatile functions (NOW(), TODAY()) in large datasets
   - Use COUNTIFS instead of multiple nested IFs where possible
   - Limit array formulas to necessary cells only

5. **Error Handling:**
   - Wrap formulas in IFERROR() where division might occur
   - Provide meaningful error messages
   - Test with missing/incomplete data

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

## Appendix: Complete Column Reference

### Master Column Map (All Assessment Sheets)

**Standard Columns (A-Q) - Present in Sheets 2-7:**
```
A: Vendor Name
B: Service Name
C: Service Type
D: Service Criticality
E: Assessment Date
F: Assessor Name
G: Status (Formula)
H: Compliance % (Formula)
I: Gap Description
J: Remediation Required
K: Remediation Owner
L: Target Date
M: Exception ID
N: Risk ID
O: Compensating Controls
P: Evidence Location
Q: Notes
```

**Extended Columns (R-X+) - Sheet-Specific:**

**Sheet 2 (Certifications): R-X**
- R: ISO 27001 Status
- S: ISO 27001 Cert #
- T: ISO 27001 Expiry
- U: SOC 2 Type II Status
- V: SOC 2 Report Date
- W: FedRAMP Status
- X: Other Certifications

**Sheet 3 (Contracts): R-AE**
- R: MSA Exists
- S: MSA Execution Date
- T: DPA Exists
- U: DPA GDPR Compliant
- V: Liability Cap Adequate
- W: Indemnification Clause
- X: Termination for Cause
- Y: DORA Compliance
- Z: NIS2 Compliance
- AA: Data Return Clause
- AB: Subprocessor Approval
- AC: Breach Notification SLA
- AD: Security Incident Support
- AE: Amendment Process

**Sheet 4 (SLA): R-AB**
- R: Uptime Commitment
- S: Actual Uptime
- T: SLA Met (Formula)
- U: Support Response Time
- V: Support SLA Met
- W: Service Credits Claimed
- X: Performance Issues
- Y: Incident Count
- Z: Major Outages
- AA: RCA Provided
- AB: SLA Improvement Needed

**Sheet 5 (Data Sovereignty): R-AD**
- R: Primary Data Location
- S: Data Processing Locations
- T: Cross-Border Transfers
- U: Transfer Mechanism
- V: DPA Covers Transfers
- W: Customer-Managed Keys
- X: Encryption Key Custody
- Y: Subprocessor Locations
- Z: Data Residency Contractual
- AA: Data Export Format
- AB: GDPR Art 28 Compliant
- AC: FADP Compliant
- AD: Transfer Impact Assessment

**Sheet 6 (Forensics): R-AC**
- R: Right to Audit Clause
- S: Audit Frequency
- T: Third-Party Audit Accepted
- U: Forensic Investigation Support
- V: Log Retention Period
- W: Log Access Method
- X: IR Cooperation SLA
- Y: Forensic Data Preservation
- Z: Chain of Custody Support
- AA: Legal Hold Support
- AB: E-Discovery Support
- AC: Audit Trail Integrity

**Sheet 7 (Jurisdictional Risk): R-AE**
- R: Provider HQ Jurisdiction
- S: Parent Company Location
- T: US Nexus Detected
- U: CLOUD Act Exposure
- V: EU Data Boundary Commitment
- W: Customer-Managed Keys
- X: Jurisdictional Risk Rating (Formula)
- Y: US Subprocessors
- Z: EU-Only Infrastructure Option
- AA: Data Localization Controls
- AB: Compensating Controls
- AC: DORA Compliance Notes
- AD: Risk Acceptance Required (Formula)
- AE: Risk Accepted By

---

**END OF SECTION 4**

**END OF PART II: TECHNICAL SPECIFICATION**
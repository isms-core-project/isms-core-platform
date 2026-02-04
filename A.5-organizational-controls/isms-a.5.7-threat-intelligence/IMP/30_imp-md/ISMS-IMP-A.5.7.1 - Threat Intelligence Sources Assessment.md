**ISMS-IMP-A.5.7.1 - Threat Intelligence Sources Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.1 |
| **Version** | 1.0 |
| **Assessment Area** | Threat Intelligence Source Portfolio Management |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.1 (Intelligence Collection Requirements), Section 2.7 (Effectiveness Measurement Requirements) |
| **Purpose** | Document threat intelligence source portfolio, assess source reliability using Admiralty Code, verify CVSS capability, and maintain audit evidence for quarterly validation |
| **Target Audience** | Threat Intelligence Analysts, Security Engineers, CISO, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial consolidated specification (15 sheets) | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Integration Points

---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.7.1 - Threat Intelligence Sources Assessment

#### What This Assessment Covers

This assessment documents the threat intelligence SOURCE PORTFOLIO deployed in [Organization]'s environment. This is the foundational "WHERE does our intelligence come from?" assessment that answers:

- What threat intelligence sources are used? (commercial platforms, OSINT, government feeds, ISACs)
- How reliable are these sources? (Admiralty Code methodology)
- Do sources support CVSS 4.0/3.1 for vulnerability intelligence?
- What coverage do sources provide? (geographic, sector, threat type, MITRE ATT&CK)
- What is the cost and ROI for subscription services?
- Are sources compliant with data protection requirements?
- What are the vendor relationships and SLA commitments?
- Is quarterly validation performed per policy requirements?
- Is business continuity documented for critical roles?

#### Key Principle

This assessment is **completely vendor-agnostic and technology-independent**. You document YOUR specific sources (whatever you use - CrowdStrike, Recorded Future, AlienVault OTX, government CERTs, internal honeypots, whatever), and verify capabilities against generic policy requirements.

#### What You'll Document

- Every threat intelligence source in your portfolio (commercial, OSINT, government, internal)
- Detailed reliability assessment using Admiralty Code methodology
- CVSS 4.0/3.1 capability verification for vulnerability intelligence
- Coverage analysis across geographic regions, industry sectors, and threat types
- Cost tracking and ROI calculation for subscription services
- Data protection compliance (GDPR, Swiss nDSG)
- Vendor integration points (APIs, feeds, formats)
- SLA tracking and vendor performance
- **AUDIT CRITICAL**: Quarterly source performance validation (Sheet 14)
- **AUDIT CRITICAL**: Business continuity plan for critical TI roles (Sheet 15)

#### How This Relates to Other A.5.7 Assessments

| Assessment | Focus | Relationship to A.5.7.1 |
|------------|-------|-------------------------|
| **ISMS-IMP-A.5.7.1** | **Source Portfolio** | **WHERE intelligence comes from (this assessment)** |
| ISMS-IMP-A.5.7.2 | Collection & Analysis | HOW intelligence is collected and analyzed |
| ISMS-IMP-A.5.7.3 | Integration & Distribution | WHERE intelligence is deployed and WHO receives it |
| ISMS-IMP-A.5.7.4 | Effectiveness Dashboard | OVERALL program metrics consolidation |
| ISMS-IMP-A.5.7.5 | Standalone Dashboard | EXECUTIVE summary (self-contained) |

This assessment (A.5.7.1) MUST be completed first - you can't assess collection, analysis, or distribution until you know what sources you have!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Threat Intelligence Team Lead** - Source selection, vendor relationships
2. **Threat Intelligence Analysts** - Day-to-day source usage, quality assessment
3. **Security Operations** - Source integration with SIEM, EDR, firewalls
4. **Procurement** - Licensing costs, contract management
5. **Compliance Officer** - Data protection compliance verification

#### Required Skills

- Understanding of threat intelligence source types and capabilities
- Familiarity with Admiralty Code intelligence evaluation methodology
- Knowledge of CVSS 4.0/3.1 for vulnerability intelligence assessment
- Understanding of data protection requirements (GDPR, Swiss nDSG)
- Basic vendor management and contract administration

#### Time Commitment

- **Initial assessment:** 8-12 hours (for comprehensive source portfolio review)
- **Quarterly updates:** 2-4 hours (update performance, validation, costs)
- **Quarterly validation:** 4-6 hours (Sheet 14 - AUDIT CRITICAL)
- **Annual BCP review:** 2-3 hours (Sheet 15 - AUDIT CRITICAL)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete source inventory** - Every TI source documented (Sheet 2)
2. ✅ **Reliability assessments** - Admiralty Code ratings for all sources (Sheet 3)
3. ✅ **CVSS capability tracking** - Know which sources support CVSS 4.0/3.1 (Sheets 2, 3)
4. ✅ **Coverage analysis** - Geographic, sector, threat type, MITRE ATT&CK gaps identified (Sheet 4)
5. ✅ **Cost and ROI tracking** - Know cost per source and value delivered (Sheet 5)
6. ✅ **Compliance verification** - Data protection and regulatory compliance confirmed (Sheet 6)
7. ✅ **Vendor management** - Integration points, SLAs, contacts documented (Sheets 9-13)
8. ✅ **Quarterly validation** - Source accuracy validated per policy (Sheet 14 - AUDIT CRITICAL)
9. ✅ **Business continuity** - Backup personnel and training documented (Sheet 15 - AUDIT CRITICAL)
10. ✅ **Action items** - Gaps and remediation plans tracked (Sheet 7)
11. ✅ **Approved assessment** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Source Access

- Access to all threat intelligence platforms (admin consoles or user accounts)
- Access to vendor management portals (for licensing, support, SLA data)
- Access to OSINT sources (Twitter, security blogs, GitHub, etc.)
- Access to government/CERT feeds (subscriptions, API keys)
- Access to internal telemetry sources (SIEM, EDR, honeypots)

#### 2. Documentation

- Threat intelligence platform contracts and licenses
- SLA agreements with commercial vendors
- Data Processing Agreements (DPAs) for GDPR/nDSG compliance
- Integration architecture documentation
- Historical performance reports (last 90 days minimum)

#### 3. Historical Data

- Source accuracy validation results (if previous assessments exist)
- False positive tracking data
- Incident reports where threat intelligence was used
- Prevented incident documentation
- Cost tracking and budget information

#### 4. Policy Requirements

- **ISMS-POL-A.5.7, Section 2.1** (Intelligence Collection Requirements) - Source categories, evaluation criteria
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements) - KPIs, audit evidence requirements
- **ISMS-POL-A.5.7, Section 3.1** (Roles & Responsibilities) - Business continuity requirements
- **ISMS-POL-A.5.7, Annex A** (Source Evaluation Framework) - Admiralty Code methodology

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to threat intelligence platform admin consoles
- OSINT collection tools (web browser, RSS readers, etc.)
- CVSS calculator (https://www.first.org/cvss/calculator/4.0 or 3.1)
- Screen capture tools (for evidence screenshots)

### Dependencies

This assessment has NO dependencies - it's the first assessment in the A.5.7 series and must be completed before others.

However, outputs from this assessment are INPUT to:

- A.5.7.2 (Collection & Analysis) - Needs source list and CVSS capabilities from Sheets 2, 3
- A.5.7.3 (Integration & Distribution) - Needs integration points from Sheets 9, 13
- A.5.7.4 (Effectiveness Dashboard) - Consolidates validation data from Sheet 14
- A.5.7.5 (Standalone Dashboard) - Uses source performance metrics

---

## Workflow

### High-Level Process

```
1. PREPARE (Gather Information)
   ↓
2. INVENTORY SOURCES (Sheet 2)
   ↓
3. EVALUATE RELIABILITY (Sheet 3: Admiralty Code + CVSS)
   ↓
4. ANALYZE COVERAGE (Sheet 4: Geographic, Sector, Threat, ATT&CK)
   ↓
5. TRACK COSTS (Sheet 5: ROI Analysis)
   ↓
6. VERIFY COMPLIANCE (Sheet 6: GDPR, nDSG)
   ↓
7. DOCUMENT INTEGRATION (Sheets 9-13: APIs, SLAs, Contacts)
   ↓
8. VALIDATE QUARTERLY (Sheet 14: AUDIT CRITICAL)
   ↓
9. DOCUMENT CONTINUITY (Sheet 15: AUDIT CRITICAL)
   ↓
10. TRACK GAPS (Sheet 7: Action Items)
   ↓
11. REVIEW & APPROVE
```

### Detailed Workflow

#### Phase 1: Preparation (2-3 hours)

**Objective:** Gather information and understand requirements

**Steps:**
1. Read this entire User Guide (Parts I and II)
2. Review **ISMS-POL-A.5.7, Section 2.1** (Intelligence Collection Requirements)
3. Review **ISMS-POL-A.5.7, Annex A** (Source Evaluation Framework - Admiralty Code)
4. Gather all prerequisites (see above)
5. Identify all threat intelligence sources in use
6. Schedule time with SMEs (TI analysts, security engineers, procurement)
7. Create working folder for evidence collection

**Deliverable:** Complete list of all threat intelligence sources with access credentials

#### Phase 2: Source Inventory (3-4 hours)

**Objective:** Complete Sheet 2 - Source_Inventory

**Steps:**
1. List EVERY threat intelligence source deployed
2. For each source:

   - Document vendor/provider, product/feed name, version
   - Identify source type (commercial, OSINT, government, internal)
   - Determine subscription status and contract dates
   - Verify CVSS 4.0/3.1 support capability
   - Document primary purpose and use cases
   - Identify responsible analyst/owner

3. Verify completeness with Threat Intelligence Team
4. Cross-check with procurement for missed subscription services

**Deliverable:** Complete Sheet 2 with all sources

**Quality Check:**

- ✓ All sources identified (commercial, OSINT, government, internal, peer sharing)
- ✓ No "unknown" or "TBD" values
- ✓ CVSS support verified for each source
- ✓ Contract dates accurate
- ✓ Responsible owner assigned

#### Phase 3: Reliability Evaluation (4-6 hours)

**Objective:** Complete Sheet 3 - Source_Evaluation using Admiralty Code

**Steps:**
For each source in Sheet 2:
1. **Assess Source Reliability** (A-F rating per Admiralty Code)

   - A = Completely reliable (≥95% accuracy)
   - B = Usually reliable (90-95%)
   - C = Fairly reliable (85-90%)
   - D = Not usually reliable (80-85%)
   - E = Unreliable (<80%)
   - F = Cannot be judged (new source, insufficient data)
   
2. **Assess Information Credibility** (1-6 rating per Admiralty Code)

   - 1 = Confirmed by other sources
   - 2 = Probably true
   - 3 = Possibly true
   - 4 = Doubtful
   - 5 = Improbable
   - 6 = Cannot be judged
   
3. **Score Quality Dimensions** (1-5 scale each):

   - Timeliness: How quickly does intelligence arrive?
   - Relevance: How relevant to [Organization]'s threat model?
   - Actionability: Can we operationalize this intelligence?
   
4. **Assess CVSS Accuracy** (if source provides CVSS):

   - Sample 10-20 CVEs from the source
   - Compare CVSS scores to NVD or vendor reference
   - Calculate accuracy rate (% within ±1.0 point)
   - Target: ≥90% accuracy per **ISMS-POL-A.5.7, Section 2.1**
   
5. **Document False Positive Rate**:

   - High: >10% false positives
   - Medium: 5-10% false positives
   - Low: <5% false positives
   - Unknown: No tracking data
   
6. **Provide Recommendation**:

   - Continue: Source meets requirements
   - Enhance: Source useful but needs improvement
   - Review: Source requires detailed investigation
   - Discontinue: Source does not meet requirements

**Deliverable:** Complete Sheet 3 with reliability assessment for all sources

**Quality Check:**

- ✓ Every source has Admiralty Code rating with justification
- ✓ Quality scores (1-5) provided for all sources
- ✓ CVSS accuracy assessed for sources claiming CVSS support
- ✓ Recommendations provided with rationale
- ✓ Evidence collected (screenshots, validation reports)

#### Phase 4: Coverage Analysis (3-4 hours)

**Objective:** Complete Sheet 4 - Coverage_Matrix

**Steps:**
1. **Geographic Coverage Assessment**:

   - Mark which regions each source covers (Global, North America, Europe, Asia-Pacific, Middle East, Latin America, Africa)
   - Identify gaps (regions with <2 sources)
   - Prioritize gaps based on [Organization]'s operating regions
   
2. **Sector Coverage Assessment**:

   - Mark which industry sectors each source covers (Financial, Healthcare, Government, Critical Infrastructure, Technology, Education, Retail, Manufacturing, All Sectors)
   - Identify gaps (sectors with <2 sources)
   - Prioritize gaps based on [Organization]'s business focus
   
3. **Threat Type Coverage Assessment**:

   - Mark which threat types each source covers (Malware, Phishing, Ransomware, Data Breach, DDoS, Insider, Supply Chain, Zero-Day, APT, Vulnerabilities)
   - Identify gaps (threat types with <2 sources)
   - Prioritize gaps based on [Organization]'s risk assessment
   
4. **MITRE ATT&CK Coverage Assessment**:

   - Document how many ATT&CK tactics (0-14) each source covers
   - Document how many ATT&CK techniques (0-200) each source covers
   - Calculate coverage percentage
   - Identify techniques with <2 sources
   - Prioritize based on organizational threat model

**Deliverable:** Complete Sheet 4 with coverage analysis and gap identification

**Quality Check:**

- ✓ All sources assessed across all coverage dimensions
- ✓ Gaps identified and prioritized
- ✓ Coverage percentages calculated
- ✓ Action items created for critical gaps

#### Phase 5: Cost Analysis (2-3 hours)

**Objective:** Complete Sheet 5 - Cost_Analysis

**Steps:**
1. Document annual costs for each subscription service
2. Calculate cost per analyst, cost per user, cost per IOC
3. Assess value delivered (prevented incidents, detection improvements)
4. Calculate ROI using formula: ROI = (Value - Cost) / Cost × 100%
5. Identify cost optimization opportunities
6. Track budget vs. actual spending

**Deliverable:** Complete Sheet 5 with cost and ROI data

**Quality Check:**

- ✓ All subscription costs documented accurately
- ✓ ROI calculated for each commercial source
- ✓ Value justification provided for high-cost sources
- ✓ Budget tracking current

#### Phase 6: Compliance Verification (2-3 hours)

**Objective:** Complete Sheet 6 - Compliance_Check

**Steps:**
1. **GDPR Compliance** (if source processes EU personal data):

   - Verify Data Processing Agreement (DPA) exists
   - Confirm Standard Contractual Clauses (SCCs) if non-EU vendor
   - Document lawful basis for processing (Art. 6)
   - Verify data subject rights procedures (Art. 12-23)
   - Check data retention compliance (Art. 5.1.e)
   
2. **Swiss nDSG Compliance** (all sources):

   - Verify appropriate security measures (Art. 8)
   - Document data processing records (Art. 12)
   - Check breach notification procedures (Art. 24)
   - Verify cross-border transfer safeguards (Art. 16)
   
3. **TLP Classification Compliance**:

   - Verify source properly marks intelligence with TLP (RED, AMBER, AMBER+STRICT, GREEN, CLEAR)
   - Confirm [Organization] follows TLP sharing restrictions
   - Document any TLP violations and remediation
   
4. **Export Control Compliance** (if applicable):

   - Verify source complies with export control regulations
   - Document any restricted intelligence handling procedures
   
5. **Contractual Compliance**:

   - Verify [Organization] complies with vendor terms of service
   - Document any usage restrictions
   - Check for unauthorized sharing of intelligence

**Deliverable:** Complete Sheet 6 with compliance verification

**Quality Check:**

- ✓ DPAs verified for all commercial sources
- ✓ GDPR/nDSG compliance confirmed
- ✓ TLP markings validated
- ✓ No compliance violations identified (or remediation plans in place)

#### Phase 7: Vendor Management Documentation (3-4 hours)

**Objective:** Complete Sheets 9-13 for vendor relationships

**Steps:**
1. **Sheet 9: Integration_Points**

   - Document API endpoints, feed URLs, authentication methods
   - List integration protocols (STIX/TAXII, REST API, CSV feed, etc.)
   - Verify integration health and connectivity
   
2. **Sheet 10: Update_Frequency**

   - Document how often each source updates (real-time, hourly, daily, weekly)
   - Verify update frequency meets operational needs
   - Track any delays or outages
   
3. **Sheet 11: Source_Contacts**

   - Document vendor account manager, technical support, escalation contacts
   - Include email, phone, support portal URLs
   - Track response times for support requests
   
4. **Sheet 12: Vendor_SLAs**

   - Document contractual SLA commitments (uptime, response time, accuracy)
   - Track vendor performance against SLAs
   - Document any SLA violations and credits/remediation
   
5. **Sheet 13: API_Integration**

   - Document API rate limits, quotas, authentication tokens
   - Track API health metrics (success rate, latency, errors)
   - Monitor approaching rate limit thresholds

**Deliverable:** Complete Sheets 9-13 with vendor management data

**Quality Check:**

- ✓ Integration points fully documented
- ✓ Contacts verified (test email/phone)
- ✓ SLA tracking current
- ✓ API health monitored

#### Phase 8: Quarterly Validation (4-6 hours) - AUDIT CRITICAL

**Objective:** Complete Sheet 14 - Source_Performance_Validation

**Policy Requirement:** **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements) mandates quarterly source accuracy validation with ≥85% target accuracy (≥90% for CVSS).

**Steps:**
1. **Select Validation Sample**:

   - Minimum 10 IOCs per source (IP addresses, domains, file hashes)
   - Minimum 10 CVEs per source (if source provides vulnerability intelligence)
   - Use random sampling or stratified sampling for statistical validity
   
2. **Validate IOC Accuracy**:

   - Verify IOCs detected actual threats (cross-reference with incident data)
   - Check for false positives (IOCs blocking legitimate activity)
   - Calculate accuracy rate: (Correct IOCs / Total IOCs) × 100%
   
3. **Validate CVSS Accuracy** (if applicable):

   - Compare source CVSS scores to NVD reference scores
   - Accept as "accurate" if within ±1.0 point of reference
   - Calculate CVSS accuracy: (Accurate CVEs / Total CVEs) × 100%
   
4. **Document Validation Results**:

   - Record validation date, sample size, accuracy rates
   - Note any patterns in false positives
   - Identify sources failing to meet ≥85% threshold (≥90% for CVSS)
   
5. **Generate Action Items**:

   - Sources below 80% accuracy → immediate review required
   - Sources below 70% accuracy → consider discontinuation
   - Create action items in Sheet 7 for remediation
   
6. **Obtain Approval**:

   - Threat Intelligence Team Lead reviews validation
   - CISO approves validation results
   - Document approval in Sheet 14

**Deliverable:** Complete Sheet 14 with quarterly validation results and approvals

**Audit Note:** Sheet 14 is PRIMARY EVIDENCE for ISO 27001 certification audits. Must be completed every quarter without exception.

**Quality Check:**

- ✓ Validation performed within last 90 days
- ✓ Minimum sample sizes met (10 IOCs + 10 CVEs per source)
- ✓ Accuracy rates calculated correctly
- ✓ Sources meeting ≥85% threshold (≥90% CVSS)
- ✓ Action items created for sources below threshold
- ✓ Approval signatures obtained

#### Phase 9: Business Continuity Planning (2-3 hours) - AUDIT CRITICAL

**Objective:** Complete Sheet 15 - Business_Continuity_Plan

**Policy Requirement:** **ISMS-POL-A.5.7, Section 3.1** (Roles & Responsibilities) mandates business continuity planning for critical threat intelligence roles with documented backup personnel.

**Steps:**
1. **Identify Critical Roles**:

   - Primary Threat Intelligence Analyst
   - Threat Intelligence Team Lead
   - Source Administrator (platform admin credentials)
   - CVSS Validator
   - IOC Deployment Operator
   
2. **Assign Backup Personnel**:

   - Each critical role requires designated backup
   - Backup must be different person than primary
   - Document backup name, email, training status
   
3. **Document Training Requirements**:

   - List skills/knowledge required for each role
   - Document training completion percentage for backup
   - Target: 100% training completion for critical roles
   - Identify training gaps and create remediation plans
   
4. **Document Continuity Procedures**:

   - How to access threat intelligence platforms (credentials, MFA)
   - How to perform daily operations (IOC deployment, report production)
   - Emergency contact procedures
   - Escalation procedures if both primary and backup unavailable
   
5. **Test Business Continuity**:

   - Perform annual continuity test (backup performs primary role for 1 week)
   - Document test date, participants, results
   - Identify gaps discovered during testing
   - Update procedures based on lessons learned
   
6. **Obtain Approval**:

   - Threat Intelligence Team Lead verifies backup assignments
   - CISO approves business continuity plan
   - Document approval in Sheet 15

**Deliverable:** Complete Sheet 15 with business continuity documentation and approvals

**Audit Note:** Sheet 15 is PRIMARY EVIDENCE for ISO 27001 certification audits. Demonstrates organizational resilience and risk management.

**Quality Check:**

- ✓ All critical roles identified
- ✓ Backup personnel assigned (100% coverage)
- ✓ Training status documented
- ✓ Critical roles have 100% backup training completion
- ✓ Continuity procedures documented
- ✓ Annual test performed (or scheduled if new BCP)
- ✓ Approval signatures obtained

#### Phase 10: Gap Tracking (1-2 hours)

**Objective:** Complete Sheet 7 - Action_Items

**Steps:**
1. Review all assessment sheets (2-6, 9-15) for identified gaps
2. For each gap, create action item with:

   - Description of gap
   - Impact assessment (High, Medium, Low)
   - Source sheet reference
   - Assigned owner
   - Target completion date
   - Status (Not Started, In Progress, Completed, Blocked)
   - Notes

3. Prioritize action items based on impact and policy requirements
4. Track progress toward remediation

**Deliverable:** Complete Sheet 7 with all action items

**Quality Check:**

- ✓ All gaps from Sheets 3-6, 9-15 captured
- ✓ High-impact gaps prioritized
- ✓ Owners assigned
- ✓ Realistic target dates
- ✓ Status current

#### Phase 11: Review & Approval (1-2 hours)

**Objective:** Obtain three-level approval for assessment

**Approval Workflow:**

**Level 1: Threat Intelligence Team Lead**

- Reviews assessment for completeness and accuracy
- Verifies all sheets populated correctly
- Confirms validation (Sheet 14) and continuity (Sheet 15) complete
- Signs off on operational accuracy

**Level 2: CISO**

- Reviews assessment for policy compliance
- Verifies quarterly validation performed (Sheet 14)
- Confirms business continuity documented (Sheet 15)
- Reviews high-impact action items
- Signs off on strategic approval

**Level 3: Executive Management (if required)**

- Reviews for high-cost sources or significant gaps
- Approves budget for source subscriptions
- Provides strategic direction on remediation priorities
- Signs off on executive approval

**Deliverable:** Fully approved assessment workbook

---

## Completing Each Sheet

### Sheet 1: Instructions

**User Action:** READ ONLY - No data entry required

**What's Provided:**

- Assessment purpose and scope
- Workflow and timeline
- Data validation rules explanation
- Admiralty Code rating definitions
- CVSS support level definitions
- Quarterly validation requirements (Sheet 14)
- Business continuity requirements (Sheet 15)
- Contact information for assistance
- Link to policy framework (ISMS-POL-A.5.7)

**Key Definitions:**

**Admiralty Code Ratings:**

- **Source Reliability (A-F):**
  - A = Completely reliable (≥95% accuracy)
  - B = Usually reliable (90-95%)
  - C = Fairly reliable (85-90%)
  - D = Not usually reliable (80-85%)
  - E = Unreliable (<80%)
  - F = Cannot be judged (new source, insufficient data)
  
- **Information Credibility (1-6):**
  - 1 = Confirmed by other sources
  - 2 = Probably true
  - 3 = Possibly true
  - 4 = Doubtful
  - 5 = Improbable
  - 6 = Cannot be judged

**CVSS Support Levels:**

- **4.0 Full:** Complete CVSS 4.0 vectors, base scores, temporal metrics
- **4.0 Basic:** CVSS 4.0 base scores only, no vectors
- **3.1 Full:** Complete CVSS 3.1 vectors, base scores, temporal metrics
- **3.1 Basic:** CVSS 3.1 base scores only, no vectors
- **2.0 Only:** Legacy CVSS 2.0 (flag for deprecation planning)
- **Proprietary:** Vendor-specific severity without CVSS
- **None:** No vulnerability severity assessment

**Quarterly Validation Requirement (AUDIT CRITICAL):**

- **Per ISMS-POL-A.5.7, Section 2.7:** Sheet 14 MUST be completed EVERY QUARTER
- **Minimum Sample:** 10 IOCs + 10 CVEs per source
- **Target Accuracy:** ≥85% overall, ≥90% CVSS accuracy
- **Validation Failure:** Triggers action items, potential source discontinuation

**Business Continuity Requirement (AUDIT CRITICAL):**

- **Per ISMS-POL-A.5.7, Section 3.1:** Sheet 15 MUST document backup personnel for ALL critical roles
- **Critical Role Coverage:** 100% backup assignments required
- **Training Target:** 100% backup training completion for critical roles
- **Annual Testing:** Required per **ISMS-POL-A.5.7, Section 3.1**

---

### Sheet 2: Source_Inventory

**User Action:** DATA ENTRY - Document every threat intelligence source

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Source_ID** | Unique identifier (auto-generated or manual) | SRC-2025-001 |
| **Source_Name** | Full name of source/platform | CrowdStrike Falcon Intelligence |
| **Vendor** | Provider/vendor name | CrowdStrike |
| **Source_Type** | Dropdown: Commercial, OSINT, Government, Internal, Peer | Commercial |
| **Subscription_Status** | Dropdown: Active, Trial, Inactive, Cancelled | Active |
| **Contract_Start** | Date format DD.MM.YYYY | 01.01.2025 |
| **Contract_End** | Date format DD.MM.YYYY | 31.12.2025 |
| **Auto_Renewal** | Dropdown: Yes, No, Unknown | Yes |
| **Primary_Purpose** | Free text (max 200 chars) | Ransomware intelligence and IOC feeds |
| **Responsible_Analyst** | Email address of owner | jane.analyst@example.com |
| **Integration_Method** | Dropdown: API, Feed, Manual, STIX/TAXII | API |
| **Update_Frequency** | Dropdown: Real-time, Hourly, Daily, Weekly, Monthly | Real-time |
| **Data_Classification** | Dropdown: TLP:RED, TLP:AMBER, TLP:AMBER+STRICT, TLP:GREEN, TLP:CLEAR | TLP:AMBER |
| **Annual_Cost** | Currency (CHF, EUR, USD) | CHF 50,000 |
| **CVSS_Support** | Dropdown: 4.0 Full, 4.0 Basic, 3.1 Full, 3.1 Basic, 2.0 Only, Proprietary, None | 4.0 Full |
| **Next_Review_Date** | Auto-calculated (Contract_End - 60 days) | 01.11.2025 |

**Data Validation:**

- Source_ID must be unique
- Dates must be valid DD.MM.YYYY format
- Contract_End must be >= Contract_Start
- Annual_Cost must be >= 0
- Responsible_Analyst must be valid email format
- CVSS_Support cannot be "None" for vulnerability-focused sources

**Conditional Formatting:**

- Subscription_Status "Inactive" or "Cancelled" → Gray background
- Contract_End within 30 days → Orange background
- Contract_End past → Red background
- Next_Review_Date overdue → Yellow background
- CVSS_Support "4.0 Full" → Dark green (#006100)
- CVSS_Support "4.0 Basic" or "3.1 Full" → Green (#00B050)
- CVSS_Support "3.1 Basic" → Yellow (#FFEB9C)
- CVSS_Support "2.0 Only" → Orange (#FFC7CE)
- CVSS_Support "Proprietary" or "None" → Red (#FFC7CE)

**Tips:**

- Start with commercial platforms (easiest to document)
- Don't forget OSINT sources (security blogs, Twitter feeds, GitHub)
- Include internal sources (honeypots, SIEM telemetry)
- Verify CVSS support by checking sample vulnerability reports
- Use consistent naming (e.g., "CrowdStrike Falcon Intelligence" not "CrowdStrike" or "Falcon")

---

### Sheet 3: Source_Evaluation

**User Action:** DATA ENTRY - Assess source reliability using Admiralty Code + CVSS accuracy

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Source_ID** | Dropdown from Sheet 2 | SRC-2025-001 |
| **Source_Name** | Auto-populated via VLOOKUP | CrowdStrike Falcon Intelligence |
| **Evaluation_Date** | Date format DD.MM.YYYY (default TODAY()) | 15.01.2026 |
| **Evaluator** | Email of person performing evaluation | jane.analyst@example.com |
| **Reliability_Rating** | Dropdown: A-F (Admiralty Code) | A - Completely Reliable |
| **Reliability_Justification** | Free text (max 300 chars) | Consistently accurate IOCs, verified through incident correlation, 97% validation accuracy |
| **Credibility_Rating** | Dropdown: 1-6 (Admiralty Code) | 1 - Confirmed by other sources |
| **Credibility_Justification** | Free text (max 300 chars) | Intelligence cross-referenced with internal SIEM telemetry and peer ISACs |
| **Timeliness_Score** | Number 1-5 | 5 |
| **Timeliness_Notes** | Free text | Real-time alerts, <1 hour latency for critical threats |
| **Relevance_Score** | Number 1-5 | 4 |
| **Relevance_Notes** | Free text | High relevance for ransomware and APT threats targeting hosting sector |
| **Actionability_Score** | Number 1-5 | 5 |
| **Actionability_Notes** | Free text | IOCs provided in STIX format, ready for SIEM/EDR import |
| **Overall_Quality_Score** | Auto-calculated: =AVERAGE(Timeliness, Relevance, Actionability) | 4.67 |
| **Quality_Rating** | Auto-calculated: IF >=4.5: Excellent, >=3.5: Good, >=2.5: Fair, <2.5: Poor | Excellent |
| **False_Positive_Rate** | Dropdown: High, Medium, Low, Unknown | Low |
| **CVSS_Accuracy_Rate** | Percentage 0-100% (1 decimal) | 92.5% |
| **CVSS_Sample_Size** | Integer >= 0 | 20 |
| **CVSS_Validation_Date** | Date format DD.MM.YYYY | 10.01.2026 |
| **Evidence_Link** | Hyperlink or file path | file://evidence/SRC-2025-001-validation.pdf |
| **Recommendation** | Dropdown: Continue, Enhance, Review, Discontinue | Continue |
| **Next_Evaluation** | Auto-calculated: Evaluation_Date + 90 days | 15.04.2026 |

**Scoring Scales:**

- **Timeliness**: 5=Real-time, 4=Hourly, 3=Daily, 2=Weekly, 1=Monthly+
- **Relevance**: 5=Highly relevant, 4=Relevant, 3=Moderately, 2=Somewhat, 1=Not relevant
- **Actionability**: 5=Immediately actionable, 4=Minor work, 3=Requires analysis, 2=Limited, 1=Not actionable

**CVSS Accuracy Validation:**
1. Sample 10-20 CVEs from source
2. Compare CVSS scores to NVD reference
3. Count CVEs within ±1.0 point as "accurate"
4. Calculate: (Accurate CVEs / Total CVEs) × 100%
5. **Target per ISMS-POL-A.5.7, Section 2.1:** ≥90% CVSS accuracy

**Conditional Formatting:**

- Quality_Rating "Excellent" → Green
- Quality_Rating "Good" → Light Green
- Quality_Rating "Fair" → Yellow
- Quality_Rating "Poor" → Red
- Recommendation "Discontinue" → Red background
- CVSS_Accuracy_Rate ≥95% → Dark green
- CVSS_Accuracy_Rate ≥90% → Green
- CVSS_Accuracy_Rate ≥85% → Yellow
- CVSS_Accuracy_Rate ≥80% → Orange
- CVSS_Accuracy_Rate <80% → Red (action required)

**Tips:**

- Be honest in reliability assessment (don't inflate ratings)
- Provide detailed justifications (auditors will review)
- Validate CVSS accuracy for all sources claiming CVSS support
- Update evaluations quarterly (or more frequently if source quality changes)
- Document evidence (screenshots, validation reports)

---

### Sheet 4: Coverage_Matrix

**User Action:** DATA ENTRY - Document coverage across multiple dimensions

**Sub-Table 1: Geographic Coverage**

| Source_ID | Source_Name | Global | North_America | Europe | Asia_Pacific | Middle_East | Latin_America | Africa |
|-----------|-------------|--------|---------------|--------|--------------|-------------|---------------|--------|
| [Dropdown] | [Auto] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |

**Instructions:**

- Check boxes for regions covered by each source
- "Global" means worldwide coverage (check this OR individual regions, not both)
- Review source documentation to verify coverage claims
- Summary row shows # sources per region and gap indicators

**Sub-Table 2: Sector Coverage**

| Source_ID | Source_Name | Financial | Healthcare | Government | Critical_Infra | Technology | Education | Retail | Manufacturing | All_Sectors |
|-----------|-------------|-----------|------------|------------|----------------|------------|-----------|--------|---------------|-------------|
| [Dropdown] | [Auto] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |

**Instructions:**

- Check boxes for industry sectors covered
- "All_Sectors" means generalist threat intelligence (not sector-specific)
- Identify gaps: Sectors with <2 sources may need additional coverage

**Sub-Table 3: Threat Type Coverage**

| Source_ID | Source_Name | Malware | Phishing | Ransomware | Data_Breach | DDoS | Insider | Supply_Chain | Zero_Day | APT | Vulnerabilities |
|-----------|-------------|---------|----------|------------|-------------|------|---------|--------------|----------|-----|-----------------|
| [Dropdown] | [Auto] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |

**Instructions:**

- Check boxes for threat types each source covers
- Most sources cover multiple threat types
- Identify gaps: Critical threats with <2 sources

**Sub-Table 4: MITRE ATT&CK Coverage**

**Reference:** MITRE ATT&CK Enterprise v18.1 (14 tactics, ~200 techniques)

| Source_ID | Source_Name | Tactics_Covered | Techniques_Covered | Coverage_Percentage |
|-----------|-------------|-----------------|--------------------|--------------------|
| [Dropdown] | [Auto] | [0-14] | [0-200] | [Formula] |

**Instructions:**
1. Review source documentation for ATT&CK mapping
2. Count how many of 14 tactics are covered (Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command & Control, Exfiltration, Impact)
3. Count how many techniques are covered (approximate if exact count not available)
4. Coverage_Percentage auto-calculated: (Techniques_Covered / 200) × 100%

**Conditional Formatting:**

- Coverage_Percentage ≥70% → Green
- Coverage_Percentage ≥50% → Yellow
- Coverage_Percentage <50% → Red

**Gap Analysis:**

- Identify tactics/techniques with <2 sources
- Prioritize based on [Organization]'s threat model
- Create action items for critical gaps (Sheet 7)

---

### Sheet 5: Cost_Analysis

**User Action:** DATA ENTRY - Track costs and calculate ROI

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Source_ID** | Dropdown from Sheet 2 | SRC-2025-001 |
| **Source_Name** | Auto-populated | CrowdStrike Falcon Intelligence |
| **Source_Type** | Auto-populated | Commercial |
| **Annual_Cost** | Currency (CHF) | CHF 50,000 |
| **Currency** | Dropdown: CHF, EUR, USD | CHF |
| **Cost_Per_Analyst** | Formula: Annual_Cost / # Analysts | CHF 25,000 |
| **Cost_Per_User** | Formula: Annual_Cost / # Protected Users | CHF 167 |
| **Cost_Per_IOC** | Formula: Annual_Cost / # IOCs Received | CHF 0.50 |
| **Prevented_Incidents** | Number of incidents prevented via this source | 8 |
| **Value_Per_Incident** | Estimated cost avoidance per prevented incident | CHF 50,000 |
| **Total_Value** | Formula: Prevented_Incidents × Value_Per_Incident | CHF 400,000 |
| **ROI_Percentage** | Formula: (Total_Value - Annual_Cost) / Annual_Cost × 100% | 700% |
| **Budget_Category** | Dropdown: Security Operations, Threat Intelligence, Infrastructure | Threat Intelligence |
| **Approved_Budget** | Annual budget allocated | CHF 50,000 |
| **Actual_Spend** | Actual spending YTD | CHF 50,000 |
| **Budget_Variance** | Formula: Approved_Budget - Actual_Spend | CHF 0 |
| **Cost_Trend** | Dropdown: Increasing, Stable, Decreasing | Stable |
| **Value_Rating** | Dropdown: Excellent, Good, Fair, Poor | Excellent |
| **Notes** | Free text | High ROI due to ransomware prevention, excellent source |

**ROI Calculation Methodology:**
1. **Determine Annual Cost:** Direct subscription cost
2. **Estimate Value Delivered:**

   - Count prevented incidents attributed to this source
   - Estimate cost avoidance per incident (breach costs, downtime, remediation)
   - Calculate total value: Prevented_Incidents × Value_Per_Incident

3. **Calculate ROI:** (Total_Value - Annual_Cost) / Annual_Cost × 100%
4. **Interpret:**

   - ROI >200%: Excellent value
   - ROI 100-200%: Good value
   - ROI 50-100%: Fair value
   - ROI <50%: Review or discontinue

**Conditional Formatting:**

- ROI_Percentage >200% → Green
- ROI_Percentage 100-200% → Light Green
- ROI_Percentage 50-100% → Yellow
- ROI_Percentage <50% → Orange (requires justification or discontinuation)
- Budget_Variance negative (over budget) → Red

**Tips:**

- Be conservative in prevented incident attribution
- Use actual incident cost data when available
- Review ROI quarterly as prevented incidents accumulate
- High-cost sources with low ROI should be reviewed carefully

---

### Sheet 6: Compliance_Check

**User Action:** DATA ENTRY - Verify legal/regulatory compliance

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Source_ID** | Dropdown from Sheet 2 | SRC-2025-001 |
| **Source_Name** | Auto-populated | CrowdStrike Falcon Intelligence |
| **GDPR_Applicable** | Dropdown: Yes, No, Unknown | Yes |
| **DPA_Exists** | Dropdown: Yes, No, N/A | Yes |
| **DPA_Date** | Date format DD.MM.YYYY | 01.01.2025 |
| **DPA_Review_Date** | Date format DD.MM.YYYY | 01.01.2026 |
| **SCC_Required** | Dropdown: Yes, No, N/A (if non-EU vendor) | No |
| **SCC_Executed** | Dropdown: Yes, No, N/A | N/A |
| **nDSG_Compliant** | Dropdown: Yes, No, Unknown (Swiss FADP) | Yes |
| **TLP_Markings_Used** | Dropdown: Always, Usually, Rarely, Never | Always |
| **TLP_Violations** | Number of violations in last 12 months | 0 |
| **Export_Control_Check** | Dropdown: Compliant, Not Applicable, Under Review | Not Applicable |
| **Terms_Compliance** | Dropdown: Compliant, Violations, Under Review | Compliant |
| **Data_Retention** | How long does source retain data? | 24 months |
| **Data_Location** | Where is data stored? (country/region) | EU (Ireland, Germany) |
| **Subprocessors_Listed** | Are all subprocessors documented? | Yes |
| **Privacy_Impact** | Dropdown: High, Medium, Low, None | Low |
| **DPIA_Required** | Dropdown: Yes, No, Completed (GDPR Art. 35) | No |
| **DPIA_Date** | Date if DPIA performed | N/A |
| **Compliance_Notes** | Free text | All GDPR requirements met, DPA reviewed annually |

**GDPR Compliance Checklist:**

- ✓ Data Processing Agreement (DPA) executed
- ✓ Standard Contractual Clauses (SCCs) if non-EU vendor
- ✓ Lawful basis documented (Art. 6 - typically "Legitimate Interest")
- ✓ Data subject rights procedures (Art. 12-23)
- ✓ Data retention aligned with purpose (Art. 5.1.e)
- ✓ Breach notification procedures (Art. 33)
- ✓ DPIA performed if high-risk processing (Art. 35)

**Swiss nDSG Compliance Checklist:**

- ✓ Appropriate security measures (Art. 8)
- ✓ Data processing records (Art. 12)
- ✓ Cross-border transfer safeguards (Art. 16)
- ✓ Breach notification capability (Art. 24)
- ✓ Data subject information rights (Art. 19)

**TLP Compliance:**

- Verify source marks intelligence with TLP (RED, AMBER, AMBER+STRICT, GREEN, CLEAR)
- Verify [Organization] follows TLP sharing restrictions
- Track any TLP violations (unauthorized sharing, incorrect marking)
- TLP violations trigger security incident response

**Conditional Formatting:**

- GDPR_Applicable "Yes" + DPA_Exists "No" → Red (critical compliance gap)
- TLP_Violations >0 → Orange (review required)
- nDSG_Compliant "No" or "Unknown" → Red
- Privacy_Impact "High" + DPIA_Required "No" → Orange

**Tips:**

- Request DPAs from all commercial vendors (mandatory for GDPR)
- Review DPAs annually (set DPA_Review_Date)
- Document any compliance exceptions or waivers
- Track TLP violations seriously (can result in source termination)

---

### Sheet 7: Action_Items

**User Action:** DATA ENTRY - Track gaps and remediation

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Action_ID** | Unique identifier (auto-generated) | ACT-2025-001 |
| **Source_Sheet** | Dropdown: Source where gap identified | Sheet 3: Source_Evaluation |
| **Source_ID** | Dropdown: Specific source if applicable | SRC-2025-005 |
| **Issue_Description** | Free text (max 500 chars) | Source reliability rating "D", below minimum threshold |
| **Impact** | Dropdown: Critical, High, Medium, Low | High |
| **Priority** | Dropdown: P1-Critical, P2-High, P3-Medium, P4-Low | P2-High |
| **Assigned_To** | Email of responsible person | jane.analyst@example.com |
| **Target_Date** | Date format DD.MM.YYYY | 28.02.2026 |
| **Status** | Dropdown: Not Started, In Progress, Completed, Blocked, Cancelled | In Progress |
| **Status_Notes** | Free text | Evaluating alternative sources, pilot in progress |
| **Completion_Date** | Date format DD.MM.YYYY | [blank until completed] |
| **Verification** | Free text | How will completion be verified? | Re-evaluate source in Sheet 3 |

**Action Item Sources:**

- **Sheet 3:** Sources with poor reliability ratings (D, E, F) or low CVSS accuracy (<90%)
- **Sheet 4:** Coverage gaps (regions, sectors, threats with <2 sources)
- **Sheet 5:** Sources with ROI <50% (cost optimization needed)
- **Sheet 6:** Compliance gaps (missing DPAs, TLP violations)
- **Sheet 9-13:** Integration issues (API failures, SLA violations)
- **Sheet 14:** Validation failures (accuracy <85%)
- **Sheet 15:** Business continuity gaps (no backup, incomplete training)

**Priority Definitions:**

- **P1-Critical:** Policy violation, regulatory non-compliance, complete capability gap
- **P2-High:** Significant gap impacting effectiveness, source quality issues
- **P3-Medium:** Optimization opportunity, non-critical gap
- **P4-Low:** Nice-to-have improvement, documentation gap

**Status Definitions:**

- **Not Started:** Action item created, not yet begun
- **In Progress:** Work actively underway
- **Completed:** Action resolved, verification performed
- **Blocked:** Cannot proceed due to dependency or obstacle
- **Cancelled:** No longer needed or deprioritized

**Conditional Formatting:**

- Priority "P1-Critical" → Red background
- Priority "P2-High" → Orange background
- Target_Date overdue + Status ≠ "Completed" → Red text
- Status "Blocked" → Yellow background

**Tips:**

- Create action items as you complete each sheet (don't save for end)
- Be specific in Issue_Description (what, why, impact)
- Assign to person with authority to resolve
- Set realistic target dates
- Update Status regularly (weekly minimum for P1/P2)
- Verify completion before marking "Completed"

---

### Sheet 8: Metadata

**User Action:** AUTO-POPULATED - Review only, no data entry

**What's Included:**

- Workbook generation date/time
- Generator script version
- Assessment version number
- Policy framework reference (ISMS-POL-A.5.7)
- IMP specification reference (ISMS-IMP-A.5.7.1 v2.0)
- Total sheets in workbook
- Named ranges defined
- Data validation rules summary
- Conditional formatting rules summary
- Change log from previous versions

**Purpose:**

- Document provenance for audit trail
- Track workbook version history
- Verify script execution completed successfully
- Reference for troubleshooting formatting or formula issues

---

### Sheets 9-13: Vendor Management

**Sheet 9: Integration_Points**

- Document API endpoints, feed URLs, authentication methods
- Track integration health (last successful connection, error rates)
- Monitor data formats (STIX, JSON, CSV, XML)

**Sheet 10: Update_Frequency**

- Document actual vs. expected update frequency
- Track delays or outages
- Monitor data freshness

**Sheet 11: Source_Contacts**

- Vendor account manager, technical support, escalation contacts
- Track response times for support tickets
- Document escalation procedures

**Sheet 12: Vendor_SLAs**

- Document contractual SLA commitments (uptime, accuracy, response time)
- Track performance against SLAs
- Document SLA violations and remediation

**Sheet 13: API_Integration**

- Document API rate limits, quotas, authentication tokens
- Monitor API health (success rate, latency, errors)
- Alert on approaching rate limits

**Cross-Reference:** See Part II (Technical Specification) for detailed column specifications for Sheets 9-13.

---

### Sheet 14: Source_Performance_Validation (AUDIT CRITICAL)

**User Action:** DATA ENTRY - Perform quarterly validation per **ISMS-POL-A.5.7, Section 2.7**

**Validation Process:**

**Step 1: Select Sample**

- Minimum 10 IOCs per source (IP addresses, domains, file hashes)
- Minimum 10 CVEs per source (if vulnerability intelligence)
- Use random sampling or stratified sampling

**Step 2: Validate IOC Accuracy**

- Check if IOCs detected actual threats (correlate with incidents)
- Identify false positives (blocked legitimate activity)
- Calculate: (Correct IOCs / Total IOCs) × 100%

**Step 3: Validate CVSS Accuracy** (if applicable)

- Compare source CVSS scores to NVD reference
- Accept ±1.0 point as "accurate"
- Calculate: (Accurate CVEs / Total CVEs) × 100%

**Step 4: Document Results**

- Record validation date, sample sizes, accuracy rates
- Note patterns or systemic issues
- Identify sources failing ≥85% threshold (≥90% for CVSS)

**Step 5: Generate Action Items**

- Sources <80% accuracy → immediate review (Sheet 7)
- Sources <70% accuracy → consider discontinuation
- Document remediation plans

**Step 6: Obtain Approvals**

- Threat Intelligence Team Lead reviews
- CISO approves
- Document signatures in Sheet 14

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Validation_Quarter** | Dropdown: Q1, Q2, Q3, Q4 | Q1 |
| **Validation_Year** | Year (YYYY) | 2026 |
| **Validation_Date** | Date format DD.MM.YYYY | 15.01.2026 |
| **Validator_Name** | Email of person performing validation | jane.analyst@example.com |
| **Source_ID** | Dropdown from Sheet 2 | SRC-2025-001 |
| **Source_Name** | Auto-populated | CrowdStrike Falcon Intelligence |
| **IOC_Sample_Size** | Integer (minimum 10) | 15 |
| **IOC_Correct** | Integer (how many IOCs accurate) | 14 |
| **IOC_False_Positive** | Integer (how many false positives) | 1 |
| **IOC_Accuracy_Rate** | Formula: (IOC_Correct / IOC_Sample_Size) × 100% | 93.3% |
| **CVE_Sample_Size** | Integer (minimum 10 if CVSS support) | 20 |
| **CVE_Accurate** | Integer (CVSS within ±1.0 of NVD) | 19 |
| **CVSS_Accuracy_Rate** | Formula: (CVE_Accurate / CVE_Sample_Size) × 100% | 95.0% |
| **Overall_Accuracy** | Formula: Weighted average of IOC + CVSS | 94.2% |
| **Meets_Target** | Formula: IF Overall ≥85% AND CVSS ≥90%: Yes, else: No | Yes |
| **Validation_Notes** | Free text | Excellent accuracy, one false positive on legitimate CDN |
| **Evidence_Link** | Hyperlink to validation report | file://evidence/2026-Q1-validation.xlsx |
| **Team_Lead_Approval** | Signature and date | J. Smith, 15.01.2026 |
| **CISO_Approval** | Signature and date | A. Johnson, 16.01.2026 |

**Conditional Formatting:**

- Overall_Accuracy ≥90% → Dark green
- Overall_Accuracy ≥85% → Green
- Overall_Accuracy ≥80% → Yellow
- Overall_Accuracy <80% → Red
- CVSS_Accuracy_Rate <90% → Orange (below target)
- Meets_Target "No" → Red background

**Frequency:**

- Perform EVERY QUARTER without exception
- Q1 validation by 31 January
- Q2 validation by 30 April
- Q3 validation by 31 July
- Q4 validation by 31 October

**Audit Evidence:**

- Sheet 14 is PRIMARY EVIDENCE for ISO 27001 audits
- Must show consistent quarterly validation
- Approvals required (Team Lead + CISO)
- Missing quarterly validation is MAJOR NON-CONFORMANCE

---

### Sheet 15: Business_Continuity_Plan (AUDIT CRITICAL)

**User Action:** DATA ENTRY - Document backup personnel per **ISMS-POL-A.5.7, Section 3.1**

**Business Continuity Requirements:**

Per **ISMS-POL-A.5.7, Section 3.1 (Roles & Responsibilities):**

- ALL critical threat intelligence roles require designated backup personnel
- Backup personnel MUST be different person than primary
- Backup personnel training MUST be 100% complete for critical roles
- Annual continuity test MUST be performed
- Test must include backup performing primary role for minimum 1 week

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Role_ID** | Unique identifier | TI-ROLE-001 |
| **Role_Name** | Name of critical role | Primary Threat Intelligence Analyst |
| **Criticality** | Dropdown: Critical, High, Medium | Critical |
| **Primary_Name** | Name of primary person | Jane Analyst |
| **Primary_Email** | Email of primary | jane.analyst@example.com |
| **Backup_Name** | Name of backup person (MUST be different) | John Analyst |
| **Backup_Email** | Email of backup | john.analyst@example.com |
| **Training_Required** | Free text list of required skills/knowledge | Admiralty Code, CVSS scoring, STIX/TAXII, IOC deployment |
| **Training_Status** | Dropdown: 0%, 25%, 50%, 75%, 100% | 100% |
| **Training_Completion_Date** | Date format DD.MM.YYYY | 10.12.2025 |
| **Last_Test_Date** | Date of last continuity test | 05.11.2025 |
| **Test_Duration** | How long backup performed role | 1 week |
| **Test_Results** | Dropdown: Successful, Issues Identified, Failed | Successful |
| **Test_Notes** | Free text | Backup performed all duties successfully, minor process clarifications needed |
| **Next_Test_Date** | Date format DD.MM.YYYY (Last_Test_Date + 12 months) | 05.11.2026 |
| **Continuity_Procedures** | Hyperlink to documented procedures | file://procedures/TI-continuity.docx |
| **Emergency_Contact** | Who to call if primary and backup unavailable | CISO: ciso@example.com |
| **Team_Lead_Approval** | Signature and date | J. Smith, 15.12.2025 |
| **CISO_Approval** | Signature and date | A. Johnson, 16.12.2025 |

**Critical Roles (Minimum Required):**
1. **Primary Threat Intelligence Analyst** - Day-to-day intelligence operations
2. **Threat Intelligence Team Lead** - Program management and vendor relationships
3. **Source Administrator** - Platform admin credentials and access management
4. **CVSS Validator** - Vulnerability severity assessment
5. **IOC Deployment Operator** - IOC deployment to SIEM, EDR, firewalls

**Training Completion Requirements:**

- **Critical Roles:** 100% training completion REQUIRED (per policy)
- **High Roles:** ≥75% training completion recommended
- **Medium Roles:** ≥50% training completion recommended

**Annual Testing Requirements:**

- **Frequency:** Annual minimum (per policy)
- **Duration:** Minimum 1 week (backup performs primary role)
- **Scope:** All critical duties performed by backup
- **Documentation:** Test report documenting results and lessons learned
- **Remediation:** Any gaps identified addressed within 60 days

**Conditional Formatting:**

- Criticality "Critical" + Training_Status <100% → Red (policy violation)
- Criticality "Critical" + Backup_Name = Primary_Name → Red (invalid backup)
- Last_Test_Date >12 months ago → Orange (test overdue)
- Test_Results "Failed" → Red
- Training_Status <50% → Yellow

**Audit Evidence:**

- Sheet 15 is PRIMARY EVIDENCE for ISO 27001 audits
- Demonstrates organizational resilience
- Shows risk management for key personnel dependencies
- Approvals required (Team Lead + CISO)
- Missing business continuity plan is MAJOR NON-CONFORMANCE

---

## Evidence Collection

### What Evidence to Collect

**Per Assessment Phase:**

**Phase 2 (Source Inventory):**

- Screenshots of source platform dashboards showing version, subscription status
- Contract documents (redact pricing if sensitive)
- License agreements
- Vendor account confirmation emails

**Phase 3 (Source Evaluation):**

- Admiralty Code evaluation worksheets
- CVSS validation reports (sample CVEs, score comparisons)
- False positive tracking reports
- Incident correlation demonstrating source accuracy

**Phase 4 (Coverage Analysis):**

- Source documentation showing geographic/sector coverage claims
- MITRE ATT&CK coverage matrices from vendor
- Gap analysis spreadsheets

**Phase 5 (Cost Analysis):**

- Invoice copies (redact if sensitive)
- ROI calculation spreadsheets
- Prevented incident reports with cost avoidance estimates

**Phase 6 (Compliance):**

- Data Processing Agreements (DPAs)
- Standard Contractual Clauses (SCCs)
- Privacy Impact Assessment (DPIA) if performed
- TLP violation reports and remediation

**Phase 8 (Quarterly Validation - AUDIT CRITICAL):**

- Validation sample selection methodology
- IOC validation results (true positive/false positive breakdown)
- CVSS validation report (NVD comparison spreadsheet)
- Prevented incident correlation report
- Approval signatures

**Phase 9 (Business Continuity - AUDIT CRITICAL):**

- Training completion certificates
- Continuity test report
- Backup personnel verification
- Procedures documentation
- Approval signatures

### Evidence Storage

**Organization:**
```
Evidence/
├── 2026-Q1/
│   ├── Source-Inventory/
│   │   ├── SRC-2025-001-CrowdStrike-screenshot.png
│   │   ├── SRC-2025-001-contract.pdf
│   │   └── ...
│   ├── Source-Evaluation/
│   │   ├── SRC-2025-001-admiralty-assessment.xlsx
│   │   ├── SRC-2025-001-cvss-validation.xlsx
│   │   └── ...
│   ├── Coverage/
│   │   ├── geographic-gap-analysis.xlsx
│   │   └── attack-coverage-matrix.xlsx
│   ├── Quarterly-Validation/ (AUDIT CRITICAL)
│   │   ├── 2026-Q1-validation-methodology.docx
│   │   ├── 2026-Q1-ioc-validation.xlsx
│   │   ├── 2026-Q1-cvss-validation.xlsx
│   │   └── 2026-Q1-validation-report-APPROVED.pdf
│   └── Business-Continuity/ (AUDIT CRITICAL)
│       ├── training-certificates/
│       ├── continuity-test-2025-report.pdf
│       └── procedures/
└── 2026-Q2/
    └── ...
```

**Retention:**

- **Quarterly assessments:** Retain for 3 years (ISO 27001 audit requirement)
- **Validation evidence:** Retain for 3 years (AUDIT CRITICAL)
- **Business continuity evidence:** Retain for 3 years (AUDIT CRITICAL)
- **Contracts and DPAs:** Retain for contract duration + 7 years (legal requirement)

**Access Control:**

- Evidence folder: Restricted to Threat Intelligence Team + CISO + Auditors
- Classification: Internal (some evidence may contain sensitive vendor data)
- Backup: Evidence backed up per standard backup policy

---

## Common Pitfalls

### Pitfall 1: Incomplete Source Inventory

**Problem:** Missing sources (especially OSINT, internal sources)

**Symptoms:**

- Sheet 2 shows only commercial platforms
- Coverage gaps (Sheet 4) for threat types actually covered by missing sources
- Audit finding: "Source inventory incomplete"

**Solution:**

- Review all intelligence collection points (not just subscriptions)
- Include OSINT sources (Twitter feeds, security blogs, GitHub)
- Include internal sources (honeypots, SIEM correlation, incident data)
- Include peer sharing (ISACs, informal sharing)
- Verify with analysts: "What sources do you actually use daily?"

---

### Pitfall 2: Inflated Reliability Ratings

**Problem:** Sources rated "A" (Completely Reliable) without validation evidence

**Symptoms:**

- Most/all sources rated A or B
- No documented validation methodology
- Audit finding: "Reliability ratings not supported by evidence"

**Solution:**

- Use Admiralty Code honestly (A rating means ≥95% validated accuracy)
- Perform actual validation (Sheet 14) - don't guess
- Ratings should spread across A-F based on real performance
- Document justification for each rating (required in Sheet 3)
- Lower ratings are OK - they drive improvement actions

---

### Pitfall 3: Missing CVSS Validation

**Problem:** Source claims CVSS 4.0 support but no accuracy validation performed

**Symptoms:**

- CVSS_Support marked "4.0 Full" but CVSS_Accuracy_Rate blank
- No CVSS validation evidence collected
- Policy requires ≥90% CVSS accuracy but never measured
- Audit finding: "CVSS capability claimed but not validated"

**Solution:**

- Actually validate CVSS scores vs. NVD reference (sample 10-20 CVEs)
- Document CVSS_Accuracy_Rate in Sheet 3
- Include CVSS validation in quarterly validation (Sheet 14)
- If source fails ≥90% threshold, mark as "does not meet CVSS requirements"

---

### Pitfall 4: Skipping Quarterly Validation (Sheet 14)

**Problem:** Sheet 14 not completed quarterly or approvals missing

**Symptoms:**

- Sheet 14 empty or outdated (>90 days old)
- No CISO approval signature
- Audit finding: "Quarterly validation not performed per policy - MAJOR NON-CONFORMANCE"

**Solution:**

- **CRITICAL:** Sheet 14 is MANDATORY per **ISMS-POL-A.5.7, Section 2.7**
- Set calendar reminders for quarterly validation (Q1, Q2, Q3, Q4)
- Budget 4-6 hours per quarter for validation work
- Obtain approvals (Team Lead + CISO) before quarter end
- Missing quarterly validation = audit failure

---

### Pitfall 5: No Business Continuity Documentation (Sheet 15)

**Problem:** Sheet 15 not completed or backup = primary person

**Symptoms:**

- Critical roles have no backup assigned
- Backup_Name = Primary_Name (same person)
- Training_Status <100% for critical roles
- No continuity testing performed
- Audit finding: "Business continuity not documented - MAJOR NON-CONFORMANCE"

**Solution:**

- **CRITICAL:** Sheet 15 is MANDATORY per **ISMS-POL-A.5.7, Section 3.1**
- Assign different person as backup (cannot be same person)
- Ensure 100% training completion for critical role backups
- Perform annual continuity test (backup performs role for 1 week)
- Document and approve (Team Lead + CISO)

---

### Pitfall 6: Inadequate Cost/ROI Justification

**Problem:** High-cost sources with no ROI calculation or prevented incident tracking

**Symptoms:**

- Annual costs >CHF 50,000 but ROI_Percentage blank
- Prevented_Incidents = 0 or unrealistically high
- Cannot justify cost to finance/executive management
- Source renewals questioned: "What value are we getting?"

**Solution:**

- Track prevented incidents rigorously (document in Sheet 14, ISMS-IMP-A.5.7.3 Sheet 7)
- Use conservative cost avoidance estimates (not inflated)
- Calculate ROI quarterly and update Sheet 5
- If ROI <50%, document specific value (early warning, executive briefings, etc.)
- High-cost sources need strong justification

---

### Pitfall 7: Compliance Gaps (Sheet 6)

**Problem:** Commercial sources without Data Processing Agreements (DPAs)

**Symptoms:**

- GDPR_Applicable = Yes but DPA_Exists = No
- Processing EU personal data without proper contracts
- Audit finding: "GDPR violation - missing DPAs"
- Potential regulatory fines

**Solution:**

- Request DPAs from ALL commercial vendors processing personal data
- Execute Standard Contractual Clauses (SCCs) for non-EU vendors
- Review DPAs annually (set DPA_Review_Date)
- Document in Sheet 6 with evidence
- No DPA = cannot use source for GDPR-covered intelligence

---

### Pitfall 8: Coverage Gaps Not Addressed

**Problem:** Coverage matrix (Sheet 4) shows gaps but no action items created

**Symptoms:**

- Critical threat types with 0 sources
- Geographic regions with no coverage but organization operates there
- MITRE ATT&CK coverage <50%
- Gaps identified but Sheet 7 (Action Items) empty

**Solution:**

- Review Sheet 4 coverage matrix for all gaps
- Prioritize gaps based on risk assessment
- Create action items (Sheet 7) for critical gaps
- Target: ≥2 sources for each critical dimension
- Review action items quarterly

---

## Quality Checklist

**Before submitting assessment for approval, verify:**

### Completeness

- [ ] **Sheet 1 (Instructions):** Read and understood
- [ ] **Sheet 2 (Source_Inventory):** All sources documented, CVSS support verified
- [ ] **Sheet 3 (Source_Evaluation):** All sources evaluated with Admiralty Code + CVSS accuracy
- [ ] **Sheet 4 (Coverage_Matrix):** All coverage dimensions assessed, gaps identified
- [ ] **Sheet 5 (Cost_Analysis):** All commercial sources have cost and ROI data
- [ ] **Sheet 6 (Compliance_Check):** All sources checked for GDPR, nDSG, TLP compliance
- [ ] **Sheet 7 (Action_Items):** All gaps documented with owners and target dates
- [ ] **Sheet 8 (Metadata):** Auto-generated, reviewed
- [ ] **Sheets 9-13 (Vendor Management):** Integration, SLAs, contacts documented
- [ ] **Sheet 14 (Quarterly Validation):** COMPLETED THIS QUARTER with approvals (AUDIT CRITICAL)
- [ ] **Sheet 15 (Business Continuity):** All critical roles have 100% trained backups (AUDIT CRITICAL)

### Data Quality

- [ ] No "TBD", "Unknown", or blank required fields
- [ ] All dates in DD.MM.YYYY format
- [ ] All email addresses valid format
- [ ] All percentages 0-100% with 1 decimal place
- [ ] All currency values ≥0
- [ ] No duplicate Source_IDs
- [ ] All formulas calculate correctly
- [ ] All conditional formatting applied

### Evidence

- [ ] Evidence collected for each source (screenshots, contracts, validation reports)
- [ ] Evidence organized in folder structure
- [ ] File naming convention consistent
- [ ] Evidence accessible to auditors
- [ ] **Sheet 14:** Validation evidence complete (IOC testing, CVSS validation)
- [ ] **Sheet 15:** Training certificates, test reports collected

### Policy Compliance

- [ ] All sources meet minimum reliability threshold (≥C3 Admiralty Code)
- [ ] CVSS accuracy ≥90% for all sources claiming CVSS support
- [ ] Overall source accuracy ≥85% per **ISMS-POL-A.5.7, Section 2.7**
- [ ] Critical coverage gaps have action items
- [ ] High-cost sources have ROI justification
- [ ] All commercial sources have DPAs if processing personal data
- [ ] **Quarterly validation (Sheet 14) completed per policy (AUDIT CRITICAL)**
- [ ] **Business continuity (Sheet 15) documented per policy (AUDIT CRITICAL)**

### Approvals

- [ ] Threat Intelligence Team Lead reviewed and approved
- [ ] CISO reviewed and approved
- [ ] Executive Management approved (if required for high-cost sources)
- [ ] **Sheet 14:** Team Lead + CISO approval signatures present
- [ ] **Sheet 15:** Team Lead + CISO approval signatures present
- [ ] Approval dates documented

### Integration

- [ ] Assessment ready for use by ISMS-IMP-A.5.7.2 (Collection & Analysis)
- [ ] Assessment ready for use by ISMS-IMP-A.5.7.3 (Integration & Distribution)
- [ ] Assessment ready for consolidation in ISMS-IMP-A.5.7.4 (Effectiveness Dashboard)

---

## Review & Approval

### Three-Level Approval Process

**Level 1: Threat Intelligence Team Lead**

**Responsibilities:**

- Review assessment for completeness
- Verify all sheets populated correctly
- Confirm source reliability ratings justified
- Verify CVSS accuracy validated
- Check coverage analysis for gaps
- **CRITICAL:** Verify Sheet 14 (quarterly validation) complete
- **CRITICAL:** Verify Sheet 15 (business continuity) complete
- Review action items for feasibility
- Provide feedback for corrections

**Approval Criteria:**

- All required data entered
- Quality checklist passed
- Evidence collected
- Action items documented

**Timeline:** 3-5 business days after submission

---

**Level 2: CISO**

**Responsibilities:**

- Review assessment for policy compliance
- Verify **ISMS-POL-A.5.7, Section 2.1** requirements met (source categories, evaluation methodology)
- Verify **ISMS-POL-A.5.7, Section 2.7** requirements met (quarterly validation, KPI targets)
- **CRITICAL:** Approve Sheet 14 (quarterly validation)
- **CRITICAL:** Approve Sheet 15 (business continuity)
- Review high-impact action items
- Review compliance gaps (Sheet 6)
- Assess budget vs. actual spend (Sheet 5)
- Provide strategic guidance on source portfolio

**Approval Criteria:**

- Policy compliance verified
- Quarterly validation performed (Sheet 14)
- Business continuity documented (Sheet 15)
- Critical gaps have remediation plans
- ROI justified for high-cost sources

**Timeline:** 5 business days after Team Lead approval

---

**Level 3: Executive Management (if required)**

**Trigger Conditions:**

- New high-cost source subscription (>CHF 50,000 annually)
- Discontinuation of major source
- Significant budget overrun (>10%)
- Critical capability gap requiring major investment

**Responsibilities:**

- Review business justification for major source investments
- Approve budget allocation for new sources
- Provide strategic direction on portfolio optimization
- Approve discontinuation of underperforming sources

**Approval Criteria:**

- Business case justified
- Budget approved
- Strategic alignment confirmed

**Timeline:** 10 business days after CISO approval

---

### Documentation of Approvals

**Approval Sign-Off Section** (in workbook):

| Approval Level | Name | Role | Signature | Date |
|----------------|------|------|-----------|------|
| Level 1: Team Lead | [Name] | Threat Intelligence Team Lead | [Signature] | [DD.MM.YYYY] |
| Level 2: CISO | [Name] | Chief Information Security Officer | [Signature] | [DD.MM.YYYY] |
| Level 3: Executive | [Name] | [Title] | [Signature] | [DD.MM.YYYY] |

**Post-Approval Actions:**
1. File approved assessment in document repository
2. Distribute to stakeholders (Security Team, Compliance, Auditors)
3. Update assessment register with approval date
4. Schedule quarterly review (3 months from approval)
5. Track action items in project management system
6. Provide assessment data to A.5.7.4 Dashboard consolidation

---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Properties

**File Name:** `ISMS_A_5_7_1_Sources_Assessment_YYYYMMDD.xlsx`

**Example:** `ISMS_A_5_7_1_Sources_Assessment_20260121.xlsx`

**Workbook Settings:**

- Format: Excel 2016+ (.xlsx)
- Calculation: Automatic
- Protection: Sheets protected (only yellow cells editable)
- Macros: None (VBA-free for security)
- External Links: None in this workbook

**Total Sheets:** 15

**Tab Colors:**

- Instructions: Blue (#4472C4)
- Data Entry (Sheets 2-7): Yellow (#FFD966)
- Metadata: Gray (#D9D9D9)
- Vendor Management (Sheets 9-13): Green (#70AD47)
- Audit Evidence (Sheets 14-15): Red (#C00000)

---

## Sheet-by-Sheet Technical Specifications

# Sheet Specifications

## Sheet 1: Instructions

**Purpose**: Provide completion guidance to stakeholders

**Content**:

- Assessment purpose and scope
- Completion timeline and responsibilities
- Data validation rules explanation
- Definitions of Admiralty Code ratings

CVSS support level definitions
Quarterly validation requirements (Sheet 14)
Business continuity requirements (Sheet 15)

- Contact information for assistance
- Link to policy framework (ISMS-POL-A.5.7)

**Format**: Rich text with hyperlinks, no data entry

**CVSS Support Levels**:

- 4.0 Full: Complete CVSS 4.0 vectors, base scores, temporal metrics
- 4.0 Basic: CVSS 4.0 base scores only, no vectors
- 3.1 Full: Complete CVSS 3.1 vectors, base scores, temporal metrics
- 3.1 Basic: CVSS 3.1 base scores only, no vectors
- 2.0 Only: Legacy CVSS 2.0 scoring (flag for deprecation planning)
- Proprietary: Vendor-specific severity without CVSS
- None: No vulnerability severity assessment

Quarterly Validation Requirement (AUDIT EVIDENCE):

- Sheet 14 must be completed EVERY QUARTER per ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements)
- Minimum sample size: 10 IOCs + 10 CVEs per source
- Target accuracy: ≥85% overall, ≥90% CVSS accuracy
- Validation failure triggers action items in Sheet 7

Business Continuity Requirement (AUDIT EVIDENCE):

- Sheet 15 must document backup personnel for ALL critical roles
- Critical roles require 100% backup training completion
- Annual continuity testing required per ISMS-POL-A.5.7, Section 3.1 (Roles & Responsibilities)

---

## Sheet 2: Source_Inventory

**Purpose**: Master inventory of all threat intelligence sources

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Text | Auto-generated (SRC-YYYY-NNN) | Yes | SRC-2025-001 |
| Source_Name | Text | Free text (max 100 chars) | Yes | CrowdStrike Falcon Intelligence |
| Source_Type | Dropdown | Commercial, OSINT, Government, Internal, Vendor, Peer_Sharing | Yes | Commercial |
| Source_Category | Dropdown | Threat_Feed, ISAC, Vendor_Advisory, Blog, Social_Media, Research_Report, Internal_Telemetry | Yes | Threat_Feed |
| Provider | Text | Free text (max 100 chars) | Yes | CrowdStrike Inc. |
| Contact_Email | Text | Email validation | No | ti-support@crowdstrike.com |
| Contract_Start | Date | DD.MM.YYYY | No | 15.01.2024 |
| Contract_End | Date | DD.MM.YYYY, must be > Contract_Start | No | 14.01.2025 |
| Auto_Renew | Dropdown | Yes, No, Under_Review | No | Yes |
| Status | Dropdown | Active, Inactive, Trial, Pending_Renewal, Cancelled | Yes | Active |
| **CVSS_Support** | **Dropdown** | **4.0 Full, 4.0 Basic, 3.1 Full, 3.1 Basic, 2.0 Only, Proprietary, None** | **Yes** | **4.0 Full** |
| Primary_Owner | Text | Free text (department/person) | Yes | SOC Team Lead |
| Backup_Owner | Text | Free text | No | Threat Analyst 2 |
| Last_Review_Date | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Review_Date | Date | Auto-calculated (Last_Review + 90 days) | Yes | 02.04.2025 |
| Notes | Text | Free text (max 500 chars) | No | Primary source for APT intelligence |

**NEW - CVSS_Support Column Details**:

**Position**: Column K (after "Status")

**Validation List**:
1. **4.0 Full** - Complete CVSS 4.0 implementation (vectors, base scores, temporal metrics)
2. **4.0 Basic** - CVSS 4.0 base scores only, no detailed vectors
3. **3.1 Full** - Complete CVSS 3.1 implementation (vectors, base scores, temporal metrics)
4. **3.1 Basic** - CVSS 3.1 base scores only, no detailed vectors
5. **2.0 Only** - Legacy CVSS 2.0 scoring (flag for deprecation planning)
6. **Proprietary** - Vendor-specific severity scoring without CVSS
7. **None** - No vulnerability severity assessment capability

**Conditional Formatting for CVSS_Support**:

- "4.0 Full" → Green background (#C6EFCE) - Preferred
- "4.0 Basic" → Light green background (#E7F4E4) - Acceptable
- "3.1 Full" → Yellow background (#FFEB9C) - Acceptable but consider upgrade
- "3.1 Basic" → Light yellow background (#FFF4CC) - Plan upgrade path
- "2.0 Only" → Orange background (#FFD966) - Deprecation planning required
- "Proprietary" → Orange background (#FFD966) - Limited interoperability
- "None" → Red background (#FFC7CE) - Not suitable for vulnerability tracking

**Rationale**: CVSS 4.0 provides improved accuracy for vulnerability severity assessment, particularly for OT/IoT environments. Sources with "None" or "Proprietary" scoring cannot integrate with Control 8.8 vulnerability management processes.

**Conditional Formatting** (Existing + New):

- Status "Inactive" or "Cancelled" → Gray background
- Contract_End within 30 days → Orange background
- Contract_End past → Red background
- Next_Review_Date overdue → Yellow background

CVSS_Support conditional formatting as defined above

**Named Ranges**:

- `SourceInventory_Data`: A2:P[LastRow] (expanded from O to P due to new column)
- `ActiveSources`: Filter where Status = "Active"

---

## Sheet 3: Source_Evaluation

**Purpose**: Assess reliability and credibility using Admiralty Code + CVSS accuracy

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Evaluation_Date | Date | DD.MM.YYYY, default TODAY() | Yes | 02.01.2025 |
| Evaluator | Text | Free text | Yes | jane.analyst@example.com |
| Reliability_Rating | Dropdown | A-F (Admiralty Code) | Yes | A - Completely Reliable |
| Reliability_Justification | Text | Free text (max 300 chars) | Yes | Consistently accurate, corroborated by incidents |
| Credibility_Rating | Dropdown | 1-6 (Admiralty Code) | Yes | 1 - Confirmed by other sources |
| Credibility_Justification | Text | Free text (max 300 chars) | Yes | Intelligence verified through internal telemetry |
| Timeliness_Score | Number | 1-5 scale | Yes | 5 |
| Timeliness_Notes | Text | Free text | No | Real-time alerts, <1 hour latency |
| Relevance_Score | Number | 1-5 scale | Yes | 4 |
| Relevance_Notes | Text | Free text | No | High relevance for financial sector threats |
| Actionability_Score | Number | 1-5 scale | Yes | 5 |
| Actionability_Notes | Text | Free text | No | Provides IOCs ready for SIEM import |
| Overall_Quality_Score | Formula | =AVERAGE(Timeliness, Relevance, Actionability) | Auto | 4.67 |
| Quality_Rating | Formula | IF Overall >= 4.5: Excellent, >=3.5: Good, >=2.5: Fair, <2.5: Poor | Auto | Excellent |
| False_Positive_Rate | Dropdown | High, Medium, Low, Unknown | No | Low |
| **CVSS_Accuracy_Rate** | **Percentage** | **0-100%, 1 decimal** | **No** | **92.5%** |
| **CVSS_Sample_Size** | **Number** | **Integer >= 0** | **No** | **20** |
| **CVSS_Validation_Date** | **Date** | **DD.MM.YYYY** | **No** | **15.12.2024** |
| Evidence_Link | Text | Hyperlink to supporting docs | No | file://evidence/SRC-2025-001.pdf |
| Recommendation | Dropdown | Continue, Enhance, Review, Discontinue | Yes | Continue |
| Next_Evaluation | Date | Auto-calculated (Evaluation_Date + 90 days) | Yes | 02.04.2025 |

**NEW - CVSS Accuracy Tracking Details**:

**CVSS_Accuracy_Rate**:

- Calculated as: (CVSS scores within ±1.0 point of NVD/vendor reference / CVSS_Sample_Size) × 100
- Minimum acceptable: 90% per ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements)
- Optional for sources with CVSS_Support = "None" or "Proprietary"

**CVSS_Sample_Size**:

- Recommended minimum: 20 CVEs for statistical significance
- Can be derived from Sheet 14 quarterly validation data
- Update after each quarterly validation cycle

**CVSS_Validation_Date**:

- Date of last CVSS accuracy assessment
- Should align with Sheet 14 quarterly validation cycles
- If > 90 days old, flag for re-validation

**Formula Example** (not in Excel, conceptual):

IF(CVSS_Sample_Size > 0, 
   (CVEs_Within_1_Point / CVSS_Sample_Size) * 100, 
   "N/A")

**Conditional Formatting for CVSS Accuracy**:

- CVSS_Accuracy_Rate >= 95% → Dark green background (#006100)
- CVSS_Accuracy_Rate >= 90% → Green background (#00B050)
- CVSS_Accuracy_Rate >= 85% → Yellow background (#FFEB9C)
- CVSS_Accuracy_Rate >= 80% → Orange background (#FFD966)
- CVSS_Accuracy_Rate < 80% → Red background (#FFC7CE) + Action_Required

**Scoring Scales** (Existing):

- **Timeliness**: 5=Real-time, 4=Hourly, 3=Daily, 2=Weekly, 1=Monthly+
- **Relevance**: 5=Highly relevant, 4=Relevant, 3=Moderately, 2=Somewhat, 1=Not relevant
- **Actionability**: 5=Immediately actionable, 4=Actionable with minor work, 3=Requires analysis, 2=Limited actionability, 1=Not actionable

**Conditional Formatting** (Existing + New):

- Quality_Rating "Excellent" → Green
- Quality_Rating "Good" → Light Green
- Quality_Rating "Fair" → Yellow
- Quality_Rating "Poor" → Red
- Recommendation "Discontinue" → Red background

CVSS_Accuracy_Rate conditional formatting as defined above

**Admiralty Code Reference Table** (separate area on sheet):

Reliability (Source):
A = Completely reliable
B = Usually reliable
C = Fairly reliable
D = Not usually reliable
E = Unreliable
F = Reliability cannot be judged

Credibility (Information):

1 = Confirmed by other sources
2 = Probably true
3 = Possibly true
4 = Doubtful
5 = Improbable
6 = Truth cannot be judged

---

## Sheet 4: Coverage_Matrix

**Purpose**: Identify coverage gaps across dimensions

**Structure**: Matrix format with multiple sub-tables

**NOTE**: This sheet specification is UNCHANGED from v1.0

### Geographic Coverage Sub-Table

| Source_ID | Source_Name | Global | North_America | Europe | Asia_Pacific | Middle_East | Latin_America | Africa |
|-----------|-------------|--------|---------------|--------|--------------|-------------|---------------|--------|
| [Dropdown] | [Formula] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] |

**Coverage Summary Row** (at bottom):

- Count of sources covering each region
- Percentage coverage (# sources / total active sources)
- Gap indicator (if < 2 sources for any region)

### Sector Coverage Sub-Table

| Source_ID | Source_Name | Financial | Healthcare | Government | Critical_Infra | Technology | Education | Retail | Manufacturing | All_Sectors |
|-----------|-------------|-----------|------------|------------|----------------|------------|-----------|--------|---------------|-------------|
| [Dropdown] | [Formula] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] |

### Threat Type Coverage Sub-Table

| Source_ID | Source_Name | Malware | Phishing | Ransomware | Data_Breach | DDoS | Insider | Supply_Chain | Zero_Day | APT | Vulnerabilities |
|-----------|-------------|---------|----------|------------|-------------|------|---------|--------------|----------|-----|-----------------|
| [Dropdown] | [Formula] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] |

### MITRE ATT&CK Coverage Sub-Table

**Reference**: MITRE ATT&CK v18.1 (enterpriseattackv18_1.xlsx in project files)

| Source_ID | Source_Name | Tactics_Covered | Techniques_Covered | Coverage_Percentage |
|-----------|-------------|-----------------|--------------------|--------------------|
| [Dropdown] | [Formula] | [Number 0-14] | [Number 0-200] | [Formula: (Techniques/200)*100] |

**MITRE ATT&CK Tactics** (14 total):

- Reconnaissance, Resource Development, Initial Access, Execution
- Persistence, Privilege Escalation, Defense Evasion, Credential Access
- Discovery, Lateral Movement, Collection, Command and Control
- Exfiltration, Impact

**Gap Analysis**:

- Identify techniques with <2 sources
- Prioritize based on organizational threat model
- Generate action items for critical gaps

**Conditional Formatting**:

- Coverage_Percentage >= 70% → Green
- Coverage_Percentage >= 50% → Yellow
- Coverage_Percentage < 50% → Red

---

## Sheet 5: Cost_Analysis

**Purpose**: Track costs and calculate ROI for subscription services

**NOTE**: This sheet specification is UNCHANGED from v1.0

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Source_Type | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | Commercial |
| Annual_Cost | Currency | Number >= 0 | No | CHF 50,000 |
| Currency | Dropdown | CHF, EUR, USD | No | CHF |
| Contract_Term | Dropdown | 1_Year, 2_Year, 3_Year, Monthly, Perpetual | No | 1_Year |
| Cost_Per_Month | Formula | =Annual_Cost / 12 | Auto | CHF 4,166.67 |
| Alerts_Per_Month | Number | Integer >= 0 | No | 150 |
| Cost_Per_Alert | Formula | =Cost_Per_Month / Alerts_Per_Month | Auto | CHF 27.78 |
| Incidents_Prevented | Number | Integer >= 0 | No | 2 |
| Avg_Incident_Cost | Currency | Number >= 0 | No | CHF 100,000 |
| Estimated_Savings | Formula | =Incidents_Prevented * Avg_Incident_Cost | Auto | CHF 200,000 |
| ROI_Ratio | Formula | =(Estimated_Savings / Annual_Cost) | Auto | 4.0 |
| ROI_Category | Formula | IF ROI > 5: Excellent, >3: Good, >1: Break-Even, <1: Negative | Auto | Good |
| Budget_Next_Year | Currency | Number >= 0 | No | CHF 55,000 |
| Budget_Change | Formula | =(Budget_Next_Year / Annual_Cost) - 1 | Auto | 10% |
| Cost_Justification | Text | Free text (max 300 chars) | No | Prevents APT incidents, high ROI |

**Summary Dashboard** (separate area):

- Total annual TI spend
- Average cost per source
- Total estimated savings
- Overall program ROI
- Budget variance analysis

**Conditional Formatting**:

- ROI_Category "Excellent" → Green
- ROI_Category "Good" → Light Green
- ROI_Category "Negative" → Red
- Budget_Change > 20% → Orange (requires justification)

---

## Sheet 6: Compliance_Check

**Purpose**: Verify legal and regulatory compliance (FADP, GDPR, ISO 27001)

**NOTE**: This sheet specification is UNCHANGED from v1.0

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Provider | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Inc. |
| Data_Contains_PII | Dropdown | Yes, No, Unknown | Yes | Yes |
| FADP_Applicable | Dropdown | Yes, No, Unknown | Yes | Yes |
| FADP_Compliant | Dropdown | Yes, No, In_Progress, Unknown | Conditional | Yes |
| FADP_Verification_Date | Date | DD.MM.YYYY | Conditional | 15.11.2024 |
| GDPR_Applicable | Dropdown | Yes, No, Unknown | Yes | Yes |
| GDPR_Compliant | Dropdown | Yes, No, In_Progress, Unknown | Conditional | Yes |
| GDPR_Verification_Date | Date | DD.MM.YYYY | Conditional | 15.11.2024 |
| DPA_Signed | Dropdown | Yes, No, In_Negotiation, N/A | Yes | Yes |
| DPA_Expiry_Date | Date | DD.MM.YYYY | Conditional | 14.01.2026 |
| DPA_Review_Date | Date | Auto (DPA_Expiry - 90 days) | Auto | 16.10.2025 |
| SCC_Applicable | Dropdown | Yes (EU-CH), Yes (EU-US), No, Unknown | Yes | Yes (EU-CH) |
| SCC_In_Place | Dropdown | Yes, No, In_Negotiation, N/A | Conditional | Yes |
| Data_Location | Text | Free text (countries) | No | Switzerland, Germany |
| Subprocessors | Text | Comma-separated list | No | AWS (Ireland), Azure (Netherlands) |
| ISO27001_Certified | Dropdown | Yes, No, Unknown | No | Yes |
| SOC2_Certified | Dropdown | Yes, No, Unknown | No | Yes |
| Privacy_Policy_Link | Text | URL | No | https://crowdstrike.com/privacy |
| Last_Compliance_Review | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Compliance_Review | Date | Auto (Last_Review + 180 days) | Auto | 01.07.2025 |
| Compliance_Status | Formula | IF all Yes: Compliant, any No: Non-Compliant, any Unknown: Review | Auto | Compliant |
| Risk_Notes | Text | Free text (max 300 chars) | No | All compliance requirements met |

**Conditional Formatting**:

- Compliance_Status "Non-Compliant" → Red background
- Compliance_Status "Review" → Orange background
- DPA_Expiry_Date within 90 days → Yellow
- DPA_Review_Date overdue → Orange
- Any "Unknown" values → Yellow

---

## Sheet 7: Action_Items

**Purpose**: Track remediation and improvement actions

**UPDATED**: Now links to new Sheets 9-15 as well

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Action_ID | Text | Auto-generated (ACT-YYYY-NNN) | Yes | ACT-2025-001 |
| Source_ID | Dropdown | From Source_Inventory | Yes | SRC-2025-001 |
| Issue_Type | Dropdown | Quality, Coverage_Gap, Cost, Compliance, Contract, Integration, CVSS_Accuracy, Continuity, Other | Yes | CVSS_Accuracy |
| Issue_Description | Text | Free text (max 300 chars) | Yes | CVSS accuracy below 90% threshold |
| Detected_In_Sheet | Dropdown | Sheet_3, Sheet_4, Sheet_5, Sheet_6, Sheet_9, Sheet_10, Sheet_11, Sheet_12, Sheet_13, Sheet_14, Sheet_15 | Yes | Sheet_14 |
| Priority | Dropdown | Critical, High, Medium, Low | Yes | High |
| Assigned_To | Text | Email or department | Yes | jane.analyst@example.com |
| Due_Date | Date | DD.MM.YYYY | Yes | 01.02.2025 |
| Status | Dropdown | Open, In_Progress, Blocked, Resolved, Closed | Yes | Open |
| Status_Notes | Text | Free text | No | Vendor contacted, awaiting improved IOC feed |
| Resolution_Date | Date | If Status=Resolved/Closed | Conditional | N/A |
| Evidence_Link | Text | Hyperlink | No | N/A |
| Created_Date | Date | Auto-fill TODAY() | Yes | 02.01.2025 |
| Created_By | Text | Auto-fill USER() | Yes | jane.analyst@example.com |
| Last_Updated | Date | Auto-update on any change | Yes | 02.01.2025 |

**NEW Issue Types**:

- **Integration**: API failures, feed connectivity issues (from Sheets 9, 13)
- **CVSS_Accuracy**: CVSS scoring accuracy below threshold (from Sheets 3, 14)
- **Continuity**: Business continuity gaps (from Sheet 15)

**Conditional Formatting**:

- Priority "Critical" → Red background
- Due_Date overdue → Red text
- Status "Blocked" → Orange background
- Status "Resolved" → Green background

**Summary Dashboard**:

- Count by Priority
- Count by Status
- Overdue actions count
- Completion rate
- Count by Issue_Type (NEW)
- Count by Detected_In_Sheet (NEW)

---

## Sheet 8: Metadata

**Purpose**: Workbook generation and version tracking

**UPDATED**: Now tracks 15-sheet structure

**Content**:

| Field | Example Value |
|-------|---------------|
| Workbook_Version | 2.0 |
| Total_Sheets | 15 |
| Generation_Date | 10.01.2025 14:30:00 |
| Generator_Script | generate_a57_1_sources.py |
| Script_Version | 2.0.0 |
| Python_Version | 3.12.1 |
| openpyxl_Version | 3.1.2 |
| Last_Modified_Date | [Auto-updated on save] |
| Last_Modified_By | [Auto-updated USER()] |
| Modification_Count | [Incremented on save] |
| Related_Policy | ISMS-POL-A.5.7 |
| Related_IMP_Spec | ISMS-IMP-A.5.7.1 v1.0 |
| CVSS_Support_Added | v1.0 (10.01.2025) |
| Vendor_Mgmt_Added | v1.0 (10.01.2025) |
| Audit_Evidence_Added | v1.0 (10.01.2025) |

**Validation Rules Applied**:

- List of all data validation rules
- List of all conditional formatting rules
- List of all cross-sheet formula references

**Changelog**:

v1.0 (10.01.2025):

- Expanded from 8 to 15 sheets
- Added CVSS_Support column to Sheet 2
- Added CVSS accuracy tracking to Sheet 3
- Added Sheets 9-13: Vendor management and integration tracking
- Added Sheet 14: Source_Performance_Validation (AUDIT CRITICAL)
- Added Sheet 15: Business_Continuity_Plan (AUDIT CRITICAL)
- Updated Sheet 7 to link to new sheets

v1.0 (Original):

- Initial 8-sheet implementation
- Source inventory, evaluation, coverage, cost, compliance

---

## Sheet 9: Integration_Points

**Purpose**: Document technical integration capabilities for each source

**Rationale**: Understanding how sources integrate technically enables automation, reduces manual effort, and ensures consistent data ingestion. This sheet supports operational efficiency and audit evidence for technical controls.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(A2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Integration_Type | Dropdown | API, STIX/TAXII, RSS, Email, Manual, Webhook, Syslog | Yes | API |
| Integration_Target_Type | Dropdown | TIP, SIEM, SOAR, Vuln_Scanner, EDR, Ticketing, Firewall, Proxy, Custom | Yes | TIP |
| Integration_Target_Name | Text | Free text (max 100 chars) | Yes | MISP Threat Intelligence Platform |
| API_Endpoint | Text | URL format | No | https://api.crowdstrike.com/intel/v2/indicators |
| Authentication_Method | Dropdown | API_Key, OAuth2, Certificate, Basic_Auth, SAML, None | No | API_Key |
| Data_Format | Dropdown | STIX_2.1, STIX_2.0, JSON, XML, CSV, PDF, HTML, CEF, LEEF | Yes | STIX_2.1 |
| CVSS_In_Feed | Dropdown | Yes_4.0, Yes_3.1, Yes_Both, No | Yes | Yes_Both |
| TLP_Support | Dropdown | Yes, No, Partial | Yes | Yes |
| IOC_Types_Supported | Text | Comma-separated (max 200 chars) | Yes | IP, Domain, URL, Hash_MD5, Hash_SHA256, Email |
| Bidirectional | Dropdown | Yes, No, N/A | No | No |
| Integration_Status | Dropdown | Active, Degraded, Failed, Inactive, Planned | Yes | Active |
| Last_Integration_Test | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Integration_Test | Date | Auto (Last_Test + 90 days) | Auto | 02.04.2025 |
| Integration_Owner | Text | Email or department | Yes | security-ops@example.com |
| Documentation_Link | Text | URL or file path | No | https://docs.crowdstrike.com/api/intel |
| Notes | Text | Max 300 chars | No | Rate limit: 1000 calls/hour, pagination: 1000 records/call |

**Integration_Type Definitions**:

- **API**: RESTful or SOAP API with programmatic access
- **STIX/TAXII**: Structured Threat Information Expression / Trusted Automated eXchange of Intelligence Information
- **RSS**: RSS/Atom feed subscription
- **Email**: Email-based alerts or reports
- **Manual**: Manual download from web portal
- **Webhook**: Push notifications to our endpoint
- **Syslog**: Syslog protocol forwarding

**Integration_Target_Type Definitions**:

- **TIP**: Threat Intelligence Platform (e.g., MISP, ThreatConnect, Anomali)
- **SIEM**: Security Information and Event Management (e.g., Splunk, QRadar, Sentinel)
- **SOAR**: Security Orchestration, Automation, and Response (e.g., Cortex XSOAR, Splunk Phantom)
- **Vuln_Scanner**: Vulnerability scanner (e.g., Qualys, Tenable, Rapid7) - for Control 8.8 integration
- **EDR**: Endpoint Detection and Response (e.g., CrowdStrike Falcon, SentinelOne)
- **Ticketing**: Ticketing system (e.g., Jira, ServiceNow)
- **Firewall**: Next-gen firewall for IOC blocking
- **Proxy**: Web proxy for URL/domain blocking
- **Custom**: Custom integration to proprietary system

**CVSS_In_Feed Definitions**:

- **Yes_4.0**: Feed includes CVSS 4.0 scores/vectors
- **Yes_3.1**: Feed includes CVSS 3.1 scores/vectors
- **Yes_Both**: Feed includes both CVSS 4.0 and 3.1 scores
- **No**: Feed does not include CVSS scoring

**Conditional Formatting**:

- Integration_Status "Failed" → Red background (#FFC7CE)
- Integration_Status "Degraded" → Orange background (#FFD966)
- Integration_Status "Inactive" → Gray background (#D9D9D9)
- CVSS_In_Feed "No" → Yellow background (#FFEB9C)
- Last_Integration_Test > 120 days old → Orange text (overdue)

**Cross-Sheet Integration**:

- Links to Sheet 13 (API_Integration) for API-specific health metrics
- Feeds into Sheet 7 (Action_Items) if Integration_Status = "Failed" or "Degraded"

---

## Sheet 10: Update_Frequency

**Purpose**: Track actual update frequency vs. contractual SLA

**Rationale**: Timely intelligence is critical for threat prevention. This sheet validates vendors meet their SLA commitments and identifies sources with degraded timeliness.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(A2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Contractual_Frequency | Dropdown | Real_Time, Hourly, Every_4_Hours, Every_12_Hours, Daily, Weekly, Monthly, Quarterly, Ad_Hoc | Yes | Hourly |
| Actual_Avg_Frequency | Text | Free text (describe actual) | Yes | Every 45 minutes |
| Last_Update_Received | DateTime | DD.MM.YYYY HH:MM | Yes | 09.01.2025 14:30 |
| Update_Count_Last_30_Days | Number | Integer >= 0 | Yes | 1200 |
| Expected_Update_Count | Number | Formula based on Contractual_Frequency | Auto | 720 |
| Update_Variance | Percentage | Formula: (Actual/Expected - 1) * 100 | Auto | +66.7% |
| SLA_Met | Dropdown | Yes, No, N/A | Yes | Yes |
| SLA_Met_Justification | Text | Free text if SLA_Met = No | Conditional | N/A |
| Outage_Count_Last_Quarter | Number | Integer >= 0 | Yes | 0 |
| Longest_Outage_Duration | Text | Free text (hours/minutes) | No | N/A |
| Average_Outage_Duration | Text | Free text (hours/minutes) | No | N/A |
| Timeliness_Score | Number | 1-5 scale | Yes | 5 |
| Timeliness_Trend | Dropdown | Improving, Stable, Degrading | Yes | Stable |
| Last_SLA_Review | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_SLA_Review | Date | Auto (Last_Review + 90 days) | Auto | 02.04.2025 |
| Notes | Text | Max 300 chars | No | Consistently exceeds SLA, high reliability |

**Expected_Update_Count Formula Logic** (conceptual):

Based on Contractual_Frequency over 30 days:

- Real_Time: 43200 (one per minute)
- Hourly: 720
- Every_4_Hours: 180
- Every_12_Hours: 60
- Daily: 30
- Weekly: 4
- Monthly: 1
- Ad_Hoc: N/A

**Timeliness_Score Scale** (1-5):

- **5**: Always meets or exceeds SLA, no outages
- **4**: Usually meets SLA, minor delays <10%
- **3**: Meets SLA 70-90% of time
- **2**: Frequently misses SLA, significant delays
- **1**: Rarely meets SLA, unreliable

**Conditional Formatting**:

- SLA_Met "No" → Red background (#FFC7CE)
- Outage_Count > 3 → Orange background (#FFD966)
- Timeliness_Score <= 2 → Red text
- Update_Variance < -20% → Yellow background (significantly under SLA)
- Last_Update_Received > 48 hours old → Red background (stale data)

**Integration with Sheet 12** (Vendor_SLAs):

- This sheet provides detailed update frequency data
- Sheet 12 aggregates SLA performance across all metrics
- Discrepancies should trigger action items in Sheet 7

---

## Sheet 11: Source_Contacts

**Purpose**: Maintain vendor contact information for escalations and support

**Rationale**: During incidents or integration failures, rapid escalation to the right vendor contact is critical. This sheet ensures contact information is current and accessible.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(A2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Contact_Type | Dropdown | Technical_Support, Account_Manager, Emergency_Contact, Billing, Executive, Data_Protection_Officer, Security_Team | Yes | Technical_Support |
| Contact_Name | Text | Free text | Yes | John Smith |
| Contact_Title | Text | Free text | No | Senior Support Engineer |
| Contact_Email | Text | Email validation | Yes | john.smith@crowdstrike.com |
| Contact_Phone | Text | Phone format (flexible) | No | +1-555-123-4567 |
| Contact_Region | Dropdown | Global, EMEA, Americas, APAC, Switzerland, Germany, Austria | No | EMEA |
| Availability | Text | Free text | No | 24/7 for P1/P2 issues, business hours for P3/P4 |
| Escalation_Path | Text | Free text (max 200 chars) | No | L1→L2 (4 hours)→Manager (8 hours)→Director (24 hours) |
| Preferred_Contact_Method | Dropdown | Email, Phone, Portal, Slack, Teams | No | Email |
| Language_Supported | Text | Comma-separated | No | English, German, French |
| Last_Contact_Date | Date | DD.MM.YYYY | No | 15.12.2024 |
| Last_Contact_Reason | Text | Free text (max 200 chars) | No | API rate limit troubleshooting |
| Response_Quality | Number | 1-5 scale | No | 5 |
| Response_Time | Text | Free text | No | <2 hours average |
| Contact_Status | Dropdown | Active, Inactive, Replaced | Yes | Active |
| Replacement_Contact | Text | If Contact_Status = Replaced | Conditional | jane.doe@crowdstrike.com |
| Last_Verified | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Verification | Date | Auto (Last_Verified + 180 days) | Auto | 02.07.2025 |
| Notes | Text | Max 300 chars | No | Escalate API issues to John directly; billing to account manager |

**Contact_Type Definitions**:

- **Technical_Support**: First-line technical troubleshooting
- **Account_Manager**: Commercial relationship, renewals, upsells
- **Emergency_Contact**: 24/7 critical incident escalation
- **Billing**: Invoice and payment issues
- **Executive**: Executive-level escalation (e.g., VP, Director)
- **Data_Protection_Officer**: GDPR/FADP compliance queries
- **Security_Team**: Vendor's security team for security incidents

**Response_Quality Scale** (1-5):

- **5**: Excellent - responsive, knowledgeable, resolves issues quickly
- **4**: Good - generally helpful, minor delays
- **3**: Adequate - meets basic needs, some gaps
- **2**: Poor - slow response, limited knowledge
- **1**: Unacceptable - non-responsive, unhelpful

**Conditional Formatting**:

- Contact_Status "Inactive" → Gray background (#D9D9D9)
- Response_Quality <= 2 → Orange background (#FFD966)
- Last_Verified > 180 days old → Yellow background (#FFEB9C)
- Contact_Type "Emergency_Contact" → Bold font (highlight importance)

**Validation Rules**:

- Each Source_ID must have at least one Technical_Support contact
- Sources marked "Active" in Sheet 2 must have at least one Active contact
- Email format validation enforced

**Usage Notes**:

- Review and verify contacts semi-annually (180 days)
- Update immediately after personnel changes at vendor
- Document all escalations in Last_Contact_Date/Reason for trend analysis
- Poor Response_Quality (<3) should trigger vendor review

---

## Sheet 12: Vendor_SLAs

**Purpose**: Track vendor Service Level Agreements and actual performance

**Rationale**: SLAs define the contractual obligations for TI sources. This sheet provides audit evidence that vendors meet their commitments and identifies underperformers requiring contract renegotiation or termination.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| SLA_Record_ID | Text | Auto-generated (SLA-YYYY-NNN) | Yes | SLA-2025-001 |
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| SLA_Metric | Dropdown | Uptime, Response_Time, Update_Frequency, Alert_Latency, False_Positive_Rate, CVSS_Accuracy, Support_Response_Time | Yes | Uptime |
| Contractual_Target | Text | Free text with units | Yes | 99.5% |
| Contractual_Target_Numeric | Number | For calculations | No | 99.5 |
| Actual_Performance | Text | Free text with units | Yes | 99.8% |
| Actual_Performance_Numeric | Number | For calculations | No | 99.8 |
| Performance_Variance | Formula | =Actual - Target | Auto | +0.3% |
| Measurement_Period | Dropdown | Last_30_Days, Last_Quarter, Last_6_Months, Last_Year, MTD, QTD, YTD | Yes | Last_Quarter |
| Measurement_Start_Date | Date | DD.MM.YYYY | Yes | 01.10.2024 |
| Measurement_End_Date | Date | DD.MM.YYYY | Yes | 31.12.2024 |
| SLA_Status | Dropdown | Met, Missed, Exceeded, N/A, Measuring | Yes | Exceeded |
| SLA_Breach_Count | Number | Integer >= 0 | Yes | 0 |
| Penalty_Clause | Dropdown | Yes, No, N/A | No | Yes |
| Penalty_Amount | Currency | Number >= 0 | No | CHF 0 |
| Penalty_Applied | Dropdown | Yes, No, Pending, N/A | No | No |
| Penalty_Application_Date | Date | If Penalty_Applied = Yes | Conditional | N/A |
| Credit_Received | Currency | Number >= 0 | No | CHF 0 |
| Escalated_To_Vendor | Dropdown | Yes, No, N/A | No | No |
| Escalation_Date | Date | If Escalated = Yes | Conditional | N/A |
| Vendor_Response | Text | Max 300 chars | No | N/A |
| Last_Review_Date | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Review_Date | Date | Auto based on Measurement_Period | Auto | 02.04.2025 |
| Reviewer | Text | Email or name | Yes | jane.analyst@example.com |
| Notes | Text | Max 300 chars | No | Consistently exceeds uptime SLA, excellent performance |

**SLA_Metric Definitions**:

- **Uptime**: Service availability (%, typically 99.5-99.99%)
- **Response_Time**: API response latency (ms, typically <500ms)
- **Update_Frequency**: Intelligence refresh rate (per Sheet 10)
- **Alert_Latency**: Time from threat emergence to alert (hours/minutes)
- **False_Positive_Rate**: Percentage of false positive IOCs (%, typically <5%)
- **CVSS_Accuracy**: CVSS score accuracy vs. NVD (%, per Sheet 14, typically >90%)
- **Support_Response_Time**: Vendor support ticket response time (hours, typically <4 hours P1)

**SLA_Status Logic**:

- **Met**: Actual_Performance meets or marginally exceeds target (within +10%)
- **Missed**: Actual_Performance below contractual target
- **Exceeded**: Actual_Performance significantly exceeds target (>10% better)
- **N/A**: Metric not applicable or not contractually defined
- **Measuring**: Measurement period ongoing, insufficient data

**Conditional Formatting**:

- SLA_Status "Missed" → Red background (#FFC7CE)
- SLA_Status "Exceeded" → Green background (#C6EFCE)
- SLA_Breach_Count > 0 → Orange background (#FFD966)
- Penalty_Applied "Yes" → Orange text (financial impact)
- Performance_Variance < 0 → Red text (underperformance)

**Summary Calculations** (separate area):

- Total SLA metrics tracked
- % SLAs Met vs. Missed
- Total penalty amount YTD
- Total credit received YTD
- Sources with >2 SLA breaches (escalation candidates)

**Integration Points**:

- Sheet 10 (Update_Frequency) → Update_Frequency SLA data
- Sheet 14 (Source_Performance_Validation) → CVSS_Accuracy and False_Positive_Rate SLA data
- Sheet 7 (Action_Items) → Missed SLAs trigger action items

**Audit Evidence**:
This sheet provides contractual compliance evidence for ISO 27001 audits, demonstrating:

- Vendor performance monitoring
- SLA breach identification and remediation
- Financial accountability (penalties/credits)

---

## Sheet 13: API_Integration

**Purpose**: Document API-specific integration details and health monitoring

**Rationale**: API-based intelligence feeds are critical infrastructure. This sheet tracks API health, rate limits, authentication status, and error rates to prevent service disruptions.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(A2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| API_Version | Text | Free text | Yes | v2.1 |
| API_Endpoint_Base | Text | URL | Yes | https://api.crowdstrike.com |
| API_Endpoint_Intel | Text | URL (specific endpoint) | No | /intel/v2/indicators |
| API_Documentation_Link | Text | URL | No | https://docs.crowdstrike.com/api |
| API_Key_Location | Text | Secret storage location | No | HashiCorp Vault: /secret/ti/crowdstrike/api_key |
| API_Key_Rotation_Frequency | Dropdown | Daily, Weekly, Monthly, Quarterly, Annually, On_Demand, Not_Rotated | No | Quarterly |
| Last_Key_Rotation | Date | DD.MM.YYYY | No | 01.10.2024 |
| Next_Key_Rotation | Date | Auto based on frequency | Auto | 01.01.2025 |
| Authentication_Method | Dropdown | API_Key, OAuth2, Bearer_Token, Certificate, Basic_Auth, SAML | Yes | API_Key |
| Authentication_Expiry | Date | DD.MM.YYYY | No | 01.06.2025 |
| Authentication_Status | Dropdown | Valid, Expiring_Soon, Expired, Unknown | Yes | Valid |
| Rate_Limit_Calls | Number | Integer (calls per hour) | Yes | 1000 |
| Rate_Limit_Data | Text | Data volume limit | No | 10 GB/day |
| Current_Usage_Calls | Number | Integer (avg calls/hour) | Yes | 400 |
| Current_Usage_Percentage | Formula | =(Current_Usage / Rate_Limit) * 100 | Auto | 40% |
| Rate_Limit_Status | Dropdown | OK, Warning, Critical | Yes | OK |
| Rate_Limit_Breaches_Last_30_Days | Number | Integer >= 0 | Yes | 0 |
| Last_Successful_Call | DateTime | DD.MM.YYYY HH:MM | Yes | 09.01.2025 15:00 |
| Last_Failed_Call | DateTime | DD.MM.YYYY HH:MM | No | N/A |
| Last_Failed_Reason | Text | Free text (max 200 chars) | No | N/A |
| Error_Rate_Last_7_Days | Percentage | 0-100%, 2 decimals | Yes | 0.05% |
| Error_Rate_Last_30_Days | Percentage | 0-100%, 2 decimals | Yes | 0.08% |
| Common_Error_Codes | Text | Comma-separated (max 100 chars) | No | N/A |
| API_Health_Status | Dropdown | Healthy, Degraded, Failed, Maintenance | Yes | Healthy |
| Last_Health_Check | DateTime | DD.MM.YYYY HH:MM | Yes | 09.01.2025 15:00 |
| Health_Check_Frequency | Dropdown | Real_Time, Every_5_Min, Every_15_Min, Hourly, Daily | Yes | Every_15_Min |
| Monitoring_Dashboard | Text | URL | No | https://monitor.example.com/crowdstrike |
| Alerting_Enabled | Dropdown | Yes, No | Yes | Yes |
| Alert_Threshold_Error_Rate | Percentage | 0-100% | No | 5% |
| Alert_Contacts | Text | Comma-separated emails | No | security-ops@example.com, jane.analyst@example.com |
| Retry_Policy | Text | Free text (max 200 chars) | No | Exponential backoff: 1s, 2s, 4s, 8s, 16s |
| Timeout_Setting | Text | Free text (seconds) | No | 30s connection, 60s read |
| Pagination_Limit | Number | Records per page | No | 1000 |
| Max_Concurrent_Requests | Number | Integer | No | 5 |
| Integration_Health_Score | Number | 1-5 scale | Yes | 5 |
| Last_Integration_Review | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Integration_Review | Date | Auto (Last_Review + 90 days) | Auto | 02.04.2025 |
| Notes | Text | Max 300 chars | No | Pagination limit: 1000 records/call; use cursor-based pagination |

**Rate_Limit_Status Logic**:

- **OK**: Current_Usage < 70% of Rate_Limit
- **Warning**: Current_Usage 70-90% of Rate_Limit
- **Critical**: Current_Usage > 90% of Rate_Limit

**API_Health_Status Definitions**:

- **Healthy**: Error_Rate < 1%, Last_Successful_Call within expected frequency
- **Degraded**: Error_Rate 1-5%, intermittent failures
- **Failed**: Error_Rate > 5%, or Last_Successful_Call > 2x expected frequency
- **Maintenance**: Vendor-announced planned maintenance

**Integration_Health_Score Scale** (1-5):

- **5**: Healthy, <0.1% error rate, zero rate limit breaches
- **4**: Healthy, <1% error rate, rare rate limit warnings
- **3**: Degraded, 1-5% error rate, occasional issues
- **2**: Poor, >5% error rate, frequent failures
- **1**: Failed, non-functional, requires immediate intervention

**Conditional Formatting**:

- Rate_Limit_Status "Critical" → Red background (#FFC7CE)
- Rate_Limit_Status "Warning" → Orange background (#FFD966)
- API_Health_Status "Failed" → Red background (#FFC7CE)
- API_Health_Status "Degraded" → Orange background (#FFD966)
- Error_Rate_Last_7_Days > 5% → Red text
- Authentication_Status "Expiring_Soon" → Yellow background (#FFEB9C)
- Authentication_Status "Expired" → Red background (#FFC7CE)
- Last_Successful_Call > 24 hours old → Orange text (stale)

**Monitoring Best Practices**:
1. Set up automated health checks (every 15 minutes recommended)
2. Configure alerting for:

   - Error_Rate > 5%
   - Rate_Limit_Status = "Critical"
   - API_Health_Status = "Failed" or "Degraded"
   - Authentication_Expiry within 30 days

3. Review authentication credentials quarterly (minimum)
4. Rotate API keys per vendor recommendations or organizational policy
5. Document all API failures in Last_Failed_Call/Reason for trend analysis

**Integration with Other Sheets**:

- Sheet 9 (Integration_Points) → Links API technical details to integration targets
- Sheet 10 (Update_Frequency) → API health impacts update timeliness
- Sheet 12 (Vendor_SLAs) → Error rates and uptime feed SLA tracking
- Sheet 7 (Action_Items) → Failed or Degraded status triggers action items

**Audit Evidence**:
This sheet demonstrates technical control implementation:

- Secure credential storage (API_Key_Location references Vault)
- Regular authentication rotation (Last/Next_Key_Rotation)
- Continuous monitoring (Health_Check_Frequency, Monitoring_Dashboard)
- Incident response (Alert_Contacts, Retry_Policy)

---

## Sheet 14: Source_Performance_Validation ⚠️ **AUDIT CRITICAL**

**Purpose**: Quarterly validation of source accuracy per ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements)

**Audit Requirement**: ISO 27001:2022 Control A.5.7 requires documented evidence that threat intelligence sources are validated for accuracy and reliability. This sheet provides that evidence.

**Policy Reference**: ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements) mandates:

- Quarterly source validation
- Minimum sample size: 10 IOCs + 10 CVEs per source
- Target accuracy: ≥85% overall, ≥90% CVSS accuracy
- Validation failure triggers remediation actions

**Rationale**: Without systematic validation, organizations cannot demonstrate due diligence in threat intelligence quality assurance. Poor-quality intelligence leads to missed threats or wasted resources on false positives.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Validation_ID | Text | Auto-generated (VAL-YYYYQQ-NNN) | Yes | VAL-2025Q1-001 |
| Source_ID | Dropdown | From Source_Inventory.Source_ID (Active only) | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(B2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Validation_Quarter | Text | YYYY-QQ format | Yes | 2025-Q1 |
| Validation_Date | Date | DD.MM.YYYY | Yes | 09.01.2025 |
| Validator | Text | Email or name | Yes | jane.analyst@example.com |
| Validation_Method | Text | Free text (max 200 chars) | Yes | Random sampling with cross-validation against NVD and internal SIEM logs |
| Total_Sample_Size | Number | Integer >= 20 | Yes | 20 |
| IOC_Sample_Size | Number | Integer >= 10 | Yes | 10 |
| IOC_True_Positives | Number | Integer >= 0, <= IOC_Sample_Size | Yes | 9 |
| IOC_False_Positives | Number | Integer >= 0, <= IOC_Sample_Size | Yes | 1 |
| IOC_Accuracy | Percentage | Formula: =(TP / IOC_Sample_Size) * 100 | Auto | 90.0% |
| CVE_Sample_Size | Number | Integer >= 10 | Yes | 10 |
| CVE_Accurate | Number | Integer >= 0, <= CVE_Sample_Size | Yes | 9 |
| CVE_Inaccurate | Number | Integer >= 0, <= CVE_Sample_Size | Yes | 1 |
| CVE_Accuracy | Percentage | Formula: =(Accurate / CVE_Sample_Size) * 100 | Auto | 90.0% |
| CVSS_Accurate_Count | Number | Integer >= 0, <= CVE_Sample_Size | Yes | 9 |
| CVSS_Inaccurate_Count | Number | Integer >= 0, <= CVE_Sample_Size | Yes | 1 |
| CVSS_Accuracy_Rate | Percentage | Formula: =(Accurate / CVE_Sample_Size) * 100 | Auto | 90.0% |
| CVSS_Accuracy_Method | Text | Free text (max 200 chars) | Yes | Compared against NVD CVSS scores; within ±1.0 point considered accurate |
| Overall_Accuracy_Rate | Percentage | Formula: =((IOC_TP + CVE_Accurate) / Total_Sample_Size) * 100 | Auto | 90.0% |
| Admiralty_Code_Source | Dropdown | A, B, C, D, E, F | Yes | A |
| Admiralty_Code_Info | Dropdown | 1, 2, 3, 4, 5, 6 | Yes | 1 |
| Admiralty_Combined | Formula | =CONCATENATE(Source, Info) | Auto | A1 |
| Validation_Pass | Dropdown | Pass, Conditional_Pass, Fail | Yes | Pass |
| Pass_Criteria_Met | Text | Auto-calculated summary | Auto | Overall ≥85% ✓, CVSS ≥90% ✓ |
| Action_Required | Dropdown | None, Review, Improve, Deprecate | Yes | None |
| Action_Notes | Text | Max 500 chars | No | Consistently high accuracy, maintain current usage |
| Action_Item_Created | Dropdown | Yes, No, N/A | Yes | No |
| Action_Item_ID | Text | Reference to Sheet 7 | No | N/A |
| Evidence_Location | Text | File path or URL | No | \\fileserver\ISMS\Evidence\5.7.1\VAL-2025Q1-001\ |
| Reviewed_By | Text | Email or name (supervisor) | Yes | team.lead@example.com |
| Review_Date | Date | DD.MM.YYYY | Yes | 10.01.2025 |
| Next_Validation_Date | Date | Auto: =Validation_Date + 90 days | Auto | 09.04.2025 |

**Critical Validation Rules**:

1. **Sample Size Enforcement**:

   Total_Sample_Size >= 20 (MANDATORY)
   IOC_Sample_Size >= 10 (MANDATORY)
   CVE_Sample_Size >= 10 (MANDATORY)
   Total_Sample_Size = IOC_Sample_Size + CVE_Sample_Size

2. **Accuracy Balance**:

   IOC_True_Positives + IOC_False_Positives = IOC_Sample_Size
   CVE_Accurate + CVE_Inaccurate = CVE_Sample_Size
   CVSS_Accurate_Count + CVSS_Inaccurate_Count = CVE_Sample_Size

3. **Validation_Pass Logic**:

   Pass: Overall_Accuracy >= 85% AND CVSS_Accuracy >= 90%
   Conditional_Pass: Overall_Accuracy >= 80% AND CVSS_Accuracy >= 85% (requires review)
   Fail: Overall_Accuracy < 80% OR CVSS_Accuracy < 85%

4. **Action_Required Logic**:

   None: Validation_Pass = Pass
   Review: Validation_Pass = Conditional_Pass
   Improve: Validation_Pass = Fail AND source has value (can be improved)
   Deprecate: Validation_Pass = Fail AND source cannot be improved or redundant

**Formulas**:

excel
# Column S: IOC_Accuracy
=IFERROR((K2/J2)*100, "N/A")

# Column W: CVE_Accuracy  
=IFERROR((O2/N2)*100, "N/A")

# Column Z: CVSS_Accuracy_Rate
=IFERROR((Q2/N2)*100, "N/A")

# Column AB: Overall_Accuracy_Rate
=IFERROR(((K2+O2)/H2)*100, "N/A")

# Column AE: Admiralty_Combined
=IF(AND(AC2<>"", AD2<>""), CONCATENATE(AC2, AD2), "")

# Column AF: Validation_Pass
=IF(AND(AB2>=85, Z2>=90), "Pass", 
   IF(AND(AB2>=80, Z2>=85), "Conditional_Pass", "Fail"))

# Column AG: Pass_Criteria_Met
=IF(AB2>=85, "Overall ≥85% ✓", "Overall <85% ✗") & ", " & 
 IF(Z2>=90, "CVSS ≥90% ✓", "CVSS <90% ✗")

# Column AH: Action_Required
=IF(AF2="Pass", "None",
   IF(AF2="Conditional_Pass", "Review", 
      IF(AC2="A" OR AC2="B", "Improve", "Deprecate")))

**Conditional Formatting**:

1. **Overall_Accuracy_Rate** (Column AB):

   - >= 95% → Dark green background (#006100), white text
   - >= 90% → Green background (#00B050)
   - >= 85% → Light green background (#C6EFCE)
   - >= 80% → Yellow background (#FFEB9C)
   - < 80% → Red background (#FFC7CE), bold red text

2. **CVSS_Accuracy_Rate** (Column Z):

   - >= 95% → Dark green background (#006100), white text
   - >= 90% → Green background (#00B050)
   - >= 85% → Yellow background (#FFEB9C)
   - < 85% → Red background (#FFC7CE), bold red text

3. **Validation_Pass** (Column AF):

   - "Pass" → Green background (#C6EFCE)
   - "Conditional_Pass" → Orange background (#FFD966)
   - "Fail" → Red background (#FFC7CE), bold text

4. **Action_Required** (Column AH):

   - "Deprecate" → Red background (#FFC7CE), bold text
   - "Improve" → Orange background (#FFD966)
   - "Review" → Yellow background (#FFEB9C)
   - "None" → No special formatting

5. **Next_Validation_Date** (Column AO):

   - Overdue (< TODAY()) → Red background (#FFC7CE)
   - Due within 14 days → Yellow background (#FFEB9C)

**Admiralty Code Integration**:

After validation, update Sheet 3 (Source_Evaluation) with the Admiralty Code assessment:

- A1: Excellent source (Overall ≥95%, CVSS ≥95%)
- B1: Good source (Overall ≥90%, CVSS ≥90%)
- C1-C2: Acceptable source (Overall ≥85%, CVSS ≥85%)
- D4-D5: Questionable source (Overall 80-85% or CVSS 80-90%)
- E5-F6: Poor source (Overall <80% or CVSS <85%, consider deprecation)

**Quarterly Validation Process**:

**Step 1: Sample Selection** (Week 1 of Quarter)
1. Identify all Active sources from Sheet 2
2. For each source, randomly select:

   - 10 IOCs (IP addresses, domains, hashes) from last 90 days
   - 10 CVEs from last 90 days

3. Document sample selection method

**Step 2: IOC Validation** (Week 2 of Quarter)
1. Cross-validate IOCs against:

   - Internal SIEM logs (confirmed malicious activity)
   - VirusTotal / Other TI sources
   - Incident response findings

2. Classify as True Positive or False Positive
3. Document evidence for audit

**Step 3: CVE Validation** (Week 3 of Quarter)
1. For each CVE:

   - Verify CVE exists in NVD
   - Compare CVSS score with NVD (±1.0 point tolerance)
   - Check CVE description accuracy

2. Classify as Accurate or Inaccurate
3. Document discrepancies

**Step 4: Documentation & Review** (Week 4 of Quarter)
1. Complete all columns in Sheet 14
2. Calculate accuracy rates (automated formulas)
3. Assign Admiralty Code (A-F, 1-6)
4. Determine Pass/Fail status
5. Create action items in Sheet 7 if required
6. Supervisor review and approval
7. Archive evidence in designated location

**Audit Trail Requirements**:

For each validation record, maintain:
1. **Sample List**: Spreadsheet with 20 items (10 IOCs + 10 CVEs)
2. **Validation Evidence**: Screenshots, SIEM queries, NVD comparisons
3. **Cross-Validation Results**: Secondary source confirmations
4. **Discrepancy Analysis**: Detailed notes on any inaccuracies
5. **Review Approval**: Email or document with supervisor sign-off

**Evidence Storage**:

- Location: `\\fileserver\ISMS\Evidence\5.7.1\VAL-YYYYQQ-NNN\`
- Retention: 3 years minimum (per ISO 27001 requirements)
- Format: ZIP archive with README.txt explaining contents

**Integration with Other Sheets**:

- **Sheet 2** (Source_Inventory): Source_ID dropdown, Active status filter
- **Sheet 3** (Source_Evaluation): Update CVSS_Accuracy_Rate, Admiralty Code
- **Sheet 7** (Action_Items): Create action items for Fail / Deprecate statuses
- **Sheet 12** (Vendor_SLAs): CVSS_Accuracy feeds SLA tracking

**Audit Interview Questions** (Preparedness):

Auditors will likely ask:
1. "Show me the last 4 quarters of source validation records." → This sheet
2. "How do you ensure statistical validity of samples?" → Sample_Size >= 20, random selection
3. "What happens when a source fails validation?" → Action_Required column → Sheet 7 action items
4. "How do you verify CVSS accuracy?" → CVSS_Accuracy_Method column documents process
5. "Who reviews and approves validations?" → Reviewed_By, Review_Date columns

---

## Sheet 15: Business_Continuity_Plan ⚠️ **AUDIT CRITICAL**

**Purpose**: Document business continuity for threat intelligence operations per ISMS-POL-A.5.7, Section 3.1 (Roles & Responsibilities)

**Audit Requirement**: ISO 27001:2022 Control A.5.7 requires organizations to ensure continuity of threat intelligence operations. This sheet demonstrates:

- Critical roles are identified
- Backup personnel are trained and ready
- Access credentials are documented and accessible
- Continuity testing is performed annually

**Policy Reference**: ISMS-POL-A.5.7, Section 3.1 (Roles & Responsibilities) mandates:

- 100% critical roles with trained backup personnel
- Annual continuity testing
- Documented access for critical sources
- Maximum 24-hour recovery time for TI operations

**Rationale**: If the primary threat intelligence analyst is unavailable (illness, departure, vacation), the organization must maintain capability to:

- Monitor critical threat intelligence sources
- Respond to high-severity threats
- Update security controls based on new intelligence
- Coordinate with incident response teams

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Role_ID | Text | Auto-generated (ROLE-NNN) | Yes | ROLE-001 |
| Role_Name | Text | Free text (max 100 chars) | Yes | Threat Intelligence Team Lead |
| Role_Description | Text | Free text (max 300 chars) | Yes | Manages TI program, evaluates sources, coordinates with SOC |
| Role_Category | Dropdown | Critical, Important, Standard | Yes | Critical |
| Primary_Person_Name | Text | Free text | Yes | Jane Analyst |
| Primary_Person_Email | Text | Email validation | Yes | jane.analyst@example.com |
| Primary_Employment_Status | Dropdown | Active, On_Leave, Departed, Other | Yes | Active |
| Primary_Training_Complete | Dropdown | Yes, No, In_Progress | Yes | Yes |
| Primary_Training_Date | Date | DD.MM.YYYY | No | 15.09.2024 |
| Primary_Cert_Valid_Until | Date | DD.MM.YYYY (if applicable) | No | 15.09.2026 |
| Backup_Person_Name | Text | Free text | Yes | John Researcher |
| Backup_Person_Email | Text | Email validation | Yes | john.researcher@example.com |
| Backup_Employment_Status | Dropdown | Active, On_Leave, Departed, Other | Yes | Active |
| Backup_Training_Complete | Dropdown | Yes, No, In_Progress | Yes | Yes |
| Backup_Training_Date | Date | DD.MM.YYYY | No | 20.09.2024 |
| Backup_Cert_Valid_Until | Date | DD.MM.YYYY (if applicable) | No | 20.09.2026 |
| Backup_Ready_Percentage | Number | 0-100% (assessor judgment) | Yes | 90 |
| Critical_Sources_Count | Number | Integer >= 0 | Yes | 5 |
| Critical_Sources_List | Text | Comma-separated Source_IDs | No | SRC-2025-001, SRC-2025-003, SRC-2025-007 |
| Access_Documented | Dropdown | Yes, No, Partial | Yes | Yes |
| Access_Documentation_Location | Text | File path or secret management system | No | HashiCorp Vault: /secret/ti/access_matrix |
| Access_Documentation_Format | Text | Free text | No | Excel spreadsheet with credentials, 2FA backup codes |
| Access_Last_Verified | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Access_Next_Verification | Date | Auto: =Last_Verified + 180 days | Auto | 02.07.2025 |
| Last_Continuity_Test_Date | Date | DD.MM.YYYY | Yes | 15.12.2024 |
| Last_Test_Duration | Text | Free text (hours/minutes) | No | 4 hours |
| Last_Test_Scenario | Text | Free text (max 200 chars) | No | Primary unavailable, backup assumes all TI duties for 1 day |
| Last_Test_Result | Dropdown | Pass, Partial_Pass, Fail, Not_Tested | Yes | Pass |
| Last_Test_Issues | Text | Free text (max 300 chars) | No | Minor delay accessing one source (resolved) |
| Last_Test_Evidence | Text | File path or URL | No | \\fileserver\ISMS\Evidence\5.7.1\Continuity\2024-12-15_Test_Report.pdf |
| Next_Test_Date | Date | Auto: =Last_Test + 365 days | Auto | 15.12.2025 |
| Compliance_Status | Formula | Complex logic (see below) | Auto | Compliant |
| Non_Compliance_Reasons | Text | Auto-populated if Non-Compliant | Auto | N/A |
| Remediation_Required | Dropdown | Yes, No | Yes | No |
| Remediation_Action_ID | Text | Reference to Sheet 7 | No | N/A |
| Last_Review_Date | Date | DD.MM.YYYY | Yes | 10.01.2025 |
| Next_Review_Date | Date | Auto: =Last_Review + 180 days | Auto | 10.07.2025 |
| Reviewer | Text | Email or name | Yes | ciso@example.com |
| Notes | Text | Max 500 chars | No | Both primary and backup attended external TI training in Q4 2024 |

**Role_Category Definitions**:

**Critical Roles** (100% backup + access required):

- Roles whose absence >24 hours would disrupt TI operations or incident response
- Examples:
  - Threat Intelligence Team Lead
  - Primary Threat Analyst
  - TI Platform Administrator
  - SOC Threat Intelligence Liaison

**Important Roles** (backup recommended but not mandatory):

- Roles whose absence could cause delays but not service disruption
- Examples:
  - Secondary Threat Analysts
  - TI Report Reviewers
  - Integration Specialists
  - Vulnerability Intelligence Analysts

**Standard Roles** (no continuity requirement):

- Read-only consumers of threat intelligence
- Recipients of TI reports
- Management stakeholders

**Compliance_Status Formula Logic**:

excel
=IF(
  AND(
    C2="Critical",
    G2="Active",
    I2="Yes",
    K2="Active",
    N2="Yes",
    Q2>=80,
    S2="Yes",
    Y2="Pass",
    Z2<>"",
    TODAY()-Y2<=365
  ),
  "Compliant",
  IF(
    C2="Critical",
    "Non-Compliant",
    "N/A"
  )
)

**Compliance Criteria for Critical Roles**:
1. Primary_Employment_Status = "Active"
2. Primary_Training_Complete = "Yes"
3. Backup_Employment_Status = "Active"
4. Backup_Training_Complete = "Yes"
5. Backup_Ready_Percentage >= 80%
6. Access_Documented = "Yes"
7. Last_Test_Result = "Pass" (or "Partial_Pass" with justification)
8. Last_Continuity_Test_Date within 365 days

**Non_Compliance_Reasons Formula** (auto-populated):

excel
=IF(
  AG2="Compliant" OR C2<>"Critical",
  "N/A",
  CONCATENATE(
    IF(G2<>"Active", "Primary not active; ", ""),
    IF(I2<>"Yes", "Primary training incomplete; ", ""),
    IF(K2<>"Active", "Backup not active; ", ""),
    IF(N2<>"Yes", "Backup training incomplete; ", ""),
    IF(Q2<80, "Backup readiness <80%; ", ""),
    IF(S2<>"Yes", "Access not documented; ", ""),
    IF(Y2="Fail", "Last test failed; ", ""),
    IF(TODAY()-Y2>365, "Annual test overdue; ", "")
  )
)

**Conditional Formatting**:

1. **Role_Category** (Column C):

   - "Critical" → Bold text, blue background (#D9E1F2)

2. **Primary/Backup_Training_Complete** (Columns I, N):

   - For Critical roles + "No" → Red background (#FFC7CE)
   - For Critical roles + "In_Progress" → Yellow background (#FFEB9C)

3. **Backup_Ready_Percentage** (Column Q):

   - >= 90% → Green background (#C6EFCE)
   - >= 80% → Light green background (#E7F4E4)
   - >= 70% → Yellow background (#FFEB9C)
   - < 70% AND Critical role → Red background (#FFC7CE)

4. **Access_Documented** (Column S):

   - For Critical roles + "No" or "Partial" → Red background (#FFC7CE)

5. **Last_Test_Result** (Column Y):

   - "Pass" → Green background (#C6EFCE)
   - "Partial_Pass" → Orange background (#FFD966)
   - "Fail" → Red background (#FFC7CE), bold text
   - "Not_Tested" AND Critical role → Red background (#FFC7CE)

6. **Next_Test_Date** (Column AA):

   - Overdue (< TODAY()) AND Critical role → Red background (#FFC7CE)
   - Due within 30 days → Yellow background (#FFEB9C)

7. **Compliance_Status** (Column AG):

   - "Compliant" → Green text, bold
   - "Non-Compliant" → Red text, bold, red background (#FFC7CE)
   - "N/A" → Gray text

**Annual Continuity Testing Process**:

**Pre-Test Planning** (30 days before):
1. Schedule test date (avoid peak operational periods)
2. Notify primary and backup personnel
3. Prepare test scenario (e.g., "Primary on unexpected leave")
4. Identify critical tasks backup must perform
5. Gather access credentials and documentation

**Test Execution** (Test Day):
1. Simulate primary unavailability (primary does not participate)
2. Backup assumes all critical role responsibilities:

   - Log into all critical TI sources
   - Retrieve latest threat intelligence
   - Generate sample threat report
   - Escalate mock high-severity threat
   - Update SIEM with new IOCs

3. Time-box test (e.g., 4 hours or full day)
4. Observe backup performance, document issues

**Post-Test Review** (Within 7 days):
1. Debrief with primary, backup, and supervisor
2. Document test results in Sheet 15
3. Identify gaps:

   - Missing credentials
   - Insufficient training
   - Documentation issues
   - Process ambiguities

4. Create action items in Sheet 7 for remediation
5. Update access documentation if needed
6. Archive test report in evidence folder

**Test Result Criteria**:

**Pass**:

- Backup successfully accessed all critical sources
- Backup completed all critical tasks within reasonable time
- No critical failures (minor issues acceptable)
- Evidence: Test report, backup logs, supervisor sign-off

**Partial_Pass**:

- Backup accessed most critical sources (≥80%)
- Backup completed critical tasks with assistance
- Minor failures that did not prevent mission completion
- Action items created for identified gaps

**Fail**:

- Backup could not access critical sources
- Backup unable to complete critical tasks
- Major failures that prevented mission completion
- Immediate remediation required

**Access Documentation Requirements**:

Critical sources (from Sheet 15, Column R) must have documented:
1. **Account Credentials**:

   - Username/email
   - Password location (e.g., Vault path)
   - 2FA backup codes location
   - API keys/tokens location

2. **Access Procedures**:

   - Login URLs
   - VPN requirements
   - Multi-factor authentication steps
   - Emergency contact procedures

3. **Operational Procedures**:

   - How to retrieve intelligence
   - How to escalate urgent threats
   - How to update SIEM/TIP
   - Communication protocols

**Storage**: 

- **Primary**: Secure password manager / secrets vault (e.g., HashiCorp Vault, 1Password, Keeper)
- **Backup**: Encrypted USB drive in secure safe (offline backup for vault failure)
- **Access**: Documented in Column T (Access_Documentation_Location)

**Integration with Other Sheets**:

- **Sheet 2** (Source_Inventory): Critical_Sources_List references Source_IDs
- **Sheet 7** (Action_Items): Failed tests or non-compliance create action items
- **Sheet 11** (Source_Contacts): Backup personnel need vendor contact information

**Audit Interview Questions** (Preparedness):

Auditors will likely ask:
1. "Show me evidence of your last business continuity test." → Last_Test_Evidence column
2. "Can your backup personnel access all critical sources?" → Access_Documented = Yes, test results
3. "What happens if your TI Team Lead departs suddenly?" → Backup_Person fields, training records
4. "How often do you test business continuity?" → Last/Next_Test_Date columns (annually)
5. "What defines a 'critical' role?" → Role_Category definitions above

---

# Assessment Methodology

## Admiralty Code Application

**Source Reliability (A-F)**:

- Review historical accuracy of source (Sheet 14 validation data)
- Assess corroboration with other sources
- Evaluate vendor reputation and expertise
- Consider false positive/negative rates

Factor in CVSS accuracy rate (Sheet 14)

**Information Credibility (1-6)**:

- Verify against internal telemetry
- Cross-reference with other TI sources
- Validate IOCs in test environment
- Assess plausibility and context

**Updated Admiralty Code Mapping** (incorporating CVSS accuracy):

| Overall Accuracy | CVSS Accuracy | Admiralty Code | Recommendation |
|------------------|---------------|----------------|----------------|
| ≥95% | ≥95% | A1 | Excellent - primary source |
| ≥90% | ≥90% | B1 | Very good - trusted source |
| ≥85% | ≥90% | B2 | Good - maintain usage |
| ≥85% | ≥85% | C2 | Acceptable - monitor closely |
| 80-85% | 80-85% | D3 | Questionable - review needed |
| <80% | <85% | E5-F6 | Poor - consider deprecation |

## Quality Scoring

**Timeliness**: How quickly does the source provide actionable intelligence?  
**Relevance**: How applicable is the intelligence to our threat landscape?  
**Actionability**: Can we immediately operationalize the intelligence?

**Overall Quality**: Average of three scores, weighted equally

**NEW - CVSS Accuracy Assessment**:

- Sample minimum 20 CVEs per quarter
- Compare against NVD CVSS scores
- Tolerance: ±1.0 point considered accurate
- Document methodology in Sheet 14

## Coverage Gap Analysis

1. Map current sources to coverage matrix (Sheet 4)
2. Identify categories with <2 sources
3. Prioritize gaps based on organizational risk profile
4. Recommend new sources or enhance existing coverage
5. **NEW**: Ensure CVSS 4.0 support for vulnerability coverage

## Vendor Management Assessment

**Integration Health** (Sheets 9, 13):

- API availability and error rates
- Rate limit compliance
- Authentication status
- Data format compatibility

**SLA Compliance** (Sheets 10, 12):

- Update frequency vs. contractual commitments
- Uptime performance
- Support response times
- CVSS accuracy (per Sheet 14)

**Vendor Relationship** (Sheet 11):

- Contact accessibility and responsiveness
- Escalation procedures documented
- Multi-region support availability

## Audit Evidence Collection

**Quarterly Validation** (Sheet 14):

- Sample selection methodology
- Cross-validation sources
- Evidence storage and retention
- Supervisor review and approval

**Business Continuity** (Sheet 15):

- Role criticality definitions
- Training completion records
- Annual test execution and results
- Access documentation verification

---

# Integration Points

## Internal Integration (ISMS Control A.5.7)

**To ISMS-IMP-A.5.7.2** (Collection & Analysis):

- Sheet 2: Source_Inventory.Source_ID → Analysis input sources
- Sheet 3: Source_Evaluation.Quality_Rating → Intelligence weighting
- Sheet 14: Validation_Quarter data → Quarterly quality trends

**To ISMS-IMP-A.5.7.3** (Integration & Distribution):

- Sheet 9: Integration_Points → TIP/SIEM/SOAR integration status
- Sheet 13: API_Integration → Technical integration health
- Sheet 11: Source_Contacts → Vendor escalation procedures

**To ISMS-IMP-A.5.7.4** (Effectiveness Dashboard):

- All sheets → External references for KPI calculations
- Sheet 7: Action_Items.Status → Program health metrics
- Sheet 14: Overall_Accuracy_Rate → Quality KPIs
- Sheet 15: Compliance_Status → Continuity KPIs

**To ISMS-IMP-A.5.7.5** (Standalone Dashboard):

- Subset of critical KPIs for executive visibility
- Sheet 14: Quarterly validation pass/fail rates
- Sheet 12: SLA compliance summary

## External Integration (Other ISMS Controls)

**From Control 8.8** (Management of Technical Vulnerabilities):

- Vulnerability scanner findings → Coverage_Matrix verification
- CVSS 4.0 requirements → Source_Inventory.CVSS_Support filtering
- Emergency patching needs → Update_Frequency SLA validation
- VulnerabilityThreatLink schema → Cross-control data exchange

**To SIEM/SOC Operations**:

- Sheet 2: Active source list → SIEM feed configuration
- Sheet 9: Integration_Points → Feed health monitoring
- Sheet 13: API_Integration → Alert configuration for failures
- Sheet 14: False_Positive_Rate → SIEM tuning data

**From Finance**:

- Invoice data → Sheet 5 (Cost_Analysis) validation
- Budget allocations → Cost_Analysis.Budget_Next_Year
- Vendor payment status → Contract renewal decisions

**To Procurement**:

- Sheet 7: Action_Items (contract-related) → Procurement queue
- Sheet 12: SLA breach data → Vendor performance reviews
- Sheet 5: ROI analysis → Budget justification

**To Legal/Compliance**:

- Sheet 6: Compliance_Check data → DPA renewal tracking
- Sheet 11: Vendor contacts (DPO) → GDPR/FADP inquiries
- Sheet 14: Validation evidence → ISO 27001 audit trail

---

# Evidence Requirements

## Required Documentation (All Sources)

**Vendor Contracts & Agreements**:

- Master Service Agreement (MSA)
- Statement of Work (SOW)
- Service Level Agreement (SLA)
- Data Processing Agreement (DPA)
- Standard Contractual Clauses (SCC) if EU/CH data transfer
- Pricing schedules

**Compliance Documentation**:

- Vendor ISO 27001 / SOC 2 certificates
- Privacy policies and security whitepapers
- Subprocessor lists
- Data location certifications
- GDPR/FADP compliance attestations

**Technical Documentation**:

- API documentation
- Integration guides
- Data format specifications (STIX, JSON schemas)
- Authentication procedures
- Rate limit specifications

## Evidence Storage

**Primary Location**: `\\fileserver\ISMS\Evidence\5.7.1-Sources\`  

**Folder Structure**:

5.7.1-Sources/
├── Contracts/
│   ├── SRC-2025-001_CrowdStrike_MSA_2024-01-15.pdf
│   ├── SRC-2025-001_CrowdStrike_DPA_2024-01-15.pdf
│   └── ...
├── Validation/
│   ├── VAL-2025Q1-001_CrowdStrike_Evidence.zip
│   ├── VAL-2025Q1-001_CrowdStrike_Report.pdf
│   └── ...
├── Continuity/
│   ├── 2024-12-15_Continuity_Test_Report.pdf
│   ├── 2024-12-15_Continuity_Test_Evidence.zip
│   └── ...
├── SLA_Reports/
│   ├── 2025-Q1_SLA_Compliance_Summary.xlsx
│   └── ...
└── Access_Documentation/
    ├── TI_Access_Matrix.xlsx (encrypted)
    ├── Critical_Sources_Credentials.keepass
    └── ...

**Naming Conventions**:

- Contracts: `[Source_ID]_[Vendor]_[Document_Type]_[Date].pdf`
- Validation: `[Validation_ID]_[Vendor]_[Type].[ext]`
- Tests: `[YYYY-MM-DD]_[Test_Type]_[Result].[ext]`

**Retention**:

- Contracts: Per organizational records management policy (default: 7 years post-termination)
- Validation evidence: 3 years minimum (ISO 27001 requirement)
- Continuity tests: 3 years minimum
- SLA reports: 3 years minimum

## Audit-Ready Evidence Checklist

For ISO 27001:2022 Control A.5.7 audits, prepare:

**Source Quality Evidence**:

- [ ] Last 4 quarters of Sheet 14 validation records
- [ ] Sample lists with cross-validation sources
- [ ] Admiralty Code justifications (Sheet 3)
- [ ] Action items created for failed validations

**Business Continuity Evidence**:

- [ ] Current Sheet 15 with all Critical roles documented
- [ ] Last annual continuity test report + evidence
- [ ] Training records for primary and backup personnel
- [ ] Access documentation location and verification

**Vendor Management Evidence**:

- [ ] SLA compliance reports (Sheet 12)
- [ ] API integration health dashboards (Sheet 13)
- [ ] Vendor contact list with verification dates (Sheet 11)
- [ ] Integration status for all active sources (Sheet 9)

**Compliance Evidence**:

- [ ] DPAs for all sources handling PII (Sheet 6)
- [ ] GDPR/FADP compliance attestations
- [ ] SCCs for EU/CH data transfers
- [ ] Privacy policy links and review dates

---

# Completion Instructions

## Initial Assessment (New Deployment)

**Estimated Time**: 3-5 days for organization with 15-20 sources

**Phase 1: Core Source Data** (Day 1-2)
1. Populate Sheet 2 (Source_Inventory) with all current sources

   - Include CVSS_Support for each source
   - Verify contract dates and ownership

2. Complete Sheet 3 (Source_Evaluation) for each active source

   - Assign Admiralty Codes
   - Note: Initial CVSS accuracy may be "N/A" until first validation

3. Fill Sheet 4 (Coverage_Matrix) to identify gaps
4. Document costs in Sheet 5 (Cost_Analysis)
5. Verify compliance in Sheet 6 (Compliance_Check)

**Phase 2: Vendor Management** (Day 3)
6. Complete Sheet 9 (Integration_Points) for all sources
7. Fill Sheet 10 (Update_Frequency) with SLA commitments
8. Populate Sheet 11 (Source_Contacts) with current vendor contacts
9. Document SLAs in Sheet 12 (Vendor_SLAs)
10. Configure Sheet 13 (API_Integration) for API-based sources

**Phase 3: Audit Evidence** (Day 4-5)
11. Perform initial validation in Sheet 14 (Source_Performance_Validation)

    - May use historical data if available
    - Otherwise, document as "Baseline - First Validation"

12. Document continuity in Sheet 15 (Business_Continuity_Plan)

    - Identify Critical roles
    - Assign backup personnel
    - Document access locations
    - Schedule first annual test

13. Generate initial action items in Sheet 7 for any issues identified

**Phase 4: Review & Approval**
14. Internal review by TI Team Lead
15. Review by CISO or Security Manager
16. Final approval and baseline establishment

## Quarterly Review

**Estimated Time**: 6-8 hours per quarter

**Week 1 of Quarter** (2 hours):
1. Update Sheet 2 (Source_Inventory):

   - Add new sources
   - Update status changes (Active → Inactive, etc.)
   - Update CVSS_Support if vendors upgrade
   - Verify contract renewal dates

2. Quick review of Sheets 9-13:

   - Verify integration status
   - Check for new API issues
   - Update vendor contacts if changed

**Week 2-3 of Quarter** (3-4 hours):
3. **CRITICAL**: Complete Sheet 14 quarterly validation:

   - Sample 10 IOCs + 10 CVEs per source
   - Cross-validate accuracy
   - Calculate accuracy rates (automated formulas)
   - Assign Admiralty Codes
   - Create action items if validation fails

4. Update Sheet 3 with validation results:

   - Update CVSS_Accuracy_Rate from Sheet 14
   - Update Admiralty Code if changed
   - Update Recommendation if needed

**Week 4 of Quarter** (1-2 hours):
5. Review Sheet 12 (Vendor_SLAs):

   - Update actual performance metrics
   - Document any SLA breaches
   - Escalate to vendors if needed

6. Review Sheet 15 (Business_Continuity_Plan):

   - Verify backup personnel still Active
   - Check training expiration dates
   - Update if personnel changes

7. Update/close action items in Sheet 7
8. Quarterly review meeting with stakeholders

## Annual Review (Additional Tasks)

**Estimated Time**: 2-3 days annually (in addition to quarterly review)

**Business Continuity Test** (8-16 hours):
1. Execute annual continuity test per Sheet 15 procedures
2. Document test results and evidence
3. Update Sheet 15 with test outcomes
4. Create action items for any gaps

**Strategic Review** (8-12 hours):
5. Comprehensive coverage gap analysis (Sheet 4)
6. Cost-benefit analysis for all commercial sources (Sheet 5)
7. Vendor performance review (Sheets 10, 12)
8. Integration optimization (Sheets 9, 13)
9. Compliance verification (Sheet 6)
10. Source portfolio optimization:

    - Consider new sources for gaps
    - Deprecate underperforming sources
    - Renegotiate contracts based on SLA data

**Documentation Update**:
11. Update ISMS-IMP-A.5.7.1 specification if needed
12. Update generator script if new requirements
13. Archive previous year's evidence
14. Management review and approval

---

# Validation Rules

## Automated Validation (Generator Script)

**Data Integrity**:

- Source_ID uniqueness across all sheets
- Date logic (Contract_End > Contract_Start, Next_Review > Last_Review)
- Email format validation
- URL format validation
- Required field completeness

**Cross-Sheet References**:

- Sheet 9-15 Source_ID dropdowns reference Sheet 2
- VLOOKUP formulas include IFERROR wrappers
- Named ranges properly defined
- No broken references

**Formula Validation**:

- Accuracy calculations in Sheet 14
- Compliance status in Sheet 15
- Cost calculations in Sheet 5
- ROI calculations in Sheet 5
- SLA variance in Sheet 12

**Conditional Formatting**:

- All color codes consistent (use standard palette)
- Formatting rules don't conflict
- Performance-friendly (avoid volatile functions)

## Business Logic Validation (Manual Review)

**Sheet 2 (Source_Inventory)**:

- All Active sources must have Last_Review_Date within 180 days
- Commercial sources must have Contract_End date
- Sources with Status = "Pending_Renewal" must have Contract_End within 90 days

**Sheet 3 (Source_Evaluation)**:

- All active sources must have evaluation within 90 days
- Sources with CVSS_Support ≠ "None" should have CVSS_Accuracy_Rate populated
- Recommendation "Discontinue" must have action item in Sheet 7

**Sheet 14 (Source_Performance_Validation)**:

- All Active sources must have validation within 90 days
- Sample sizes meet minimums (≥10 IOC, ≥10 CVE)
- Validation_Pass = "Fail" must have Action_Item_Created = "Yes"
- Evidence_Location must be documented for all validations

**Sheet 15 (Business_Continuity_Plan)**:

- All Critical roles must have Compliance_Status = "Compliant"
- Last_Continuity_Test_Date must be within 365 days for Critical roles
- Non-Compliant Critical roles must have Remediation_Action_ID

**Sheet 6 (Compliance_Check)**:

- Sources with PII must have FADP/GDPR compliance documented
- Commercial sources must have DPA if handling PII
- DPA_Expiry_Date must be > TODAY() or have renewal action item

## Validation Script

**Script**: `excel_sanity_check_a57_1.py`  
**Validation**: Now validates 15 sheets

**Runs**: 

- On-demand via CLI
- Automated monthly (scheduled task)
- Before management review
- Before audit

**Outputs**: 

- Validation report (JSON, HTML, or text)
- Pass/Fail/Warning status per check
- Detailed error messages with row references
- Suggested remediation actions

**Critical Checks**:

- Sheet 14: Quarterly validation completeness
- Sheet 14: Minimum sample sizes enforced
- Sheet 15: Critical role compliance verification
- Sheet 15: Annual test currency (<365 days)
- All sheets: VLOOKUP error checking
- All sheets: Orphaned Source_IDs (referenced but not in Sheet 2)

---

# Related Documents

**Policy Framework**:

- ISMS-POL-A.5.7 (Threat Intelligence Policy - Master Document)
- ISMS-POL-A.5.7, Section 1 (Purpose, Scope, Definitions)
- ISMS-POL-A.5.7, Section 2 (Threat Intelligence Requirements)
- ISMS-POL-A.5.7, Section 3 (Roles and Responsibilities)
- ISMS-POL-A.5.7, Section 3 (Policy Governance) - **Sections 4.4.3, 4.4.6 are audit critical**
- ISMS-POL-A.5.7, Annexes (Annexes)

**Implementation Specifications**:

- ISMS-IMP-A.5.7.2 (Collection & Analysis Assessment)
- ISMS-IMP-A.5.7.3 (Integration & Distribution Assessment)
- ISMS-IMP-A.5.7.4 (Effectiveness Dashboard)
- ISMS-IMP-A.5.7.5 (Standalone Dashboard)

**Cross-Control Integration**:

- ISMS-IMP-A.8.8 (Management of Technical Vulnerabilities) - CVSS integration
- ISMS-POL-A.8.8 (Vulnerability Management Policy) - VulnerabilityThreatLink schema

**External References**:

- ISO/IEC 27001:2022 Annex A Control A.5.7
- MITRE ATT&CK Framework v18.1
- NIST SP 800-150 (Guide to Cyber Threat Information Sharing)
- Admiralty Code for Intelligence Evaluation
- CVSS 4.0 Specification (FIRST.org)
- STIX 2.1 Specification

**Templates & Tools**:

- Data Protection Impact Assessment (DPIA) template
- Vendor DPA template
- Standard Contractual Clauses (SCC) template
- Business Continuity Test Report template

---

# Appendices

## Appendix A: Admiralty Code Quick Reference

Source Reliability + Information Credibility = Intelligence Grade

Reliability (Source):
A = Completely reliable (≥95% accuracy)
B = Usually reliable (90-95% accuracy)
C = Fairly reliable (85-90% accuracy)
D = Not usually reliable (80-85% accuracy)
E = Unreliable (<80% accuracy)
F = Reliability cannot be judged (insufficient data)

Credibility (Information):

1 = Confirmed by other sources
2 = Probably true
3 = Possibly true
4 = Doubtful
5 = Improbable
6 = Truth cannot be judged

Examples:
Best: A1, B1, A2 (high-confidence intelligence)
Good: B2, C1, C2 (actionable intelligence)
Use with caution: D3, D4, E5 (low-confidence intelligence)
Avoid: F6 (no basis for judgment)

Operational Guidance:

- A1/B1: Use immediately for decision-making
- C2/D3: Corroborate before acting
- E5/F6: Use only for awareness, not action

## Appendix B: CVSS 4.0 vs. 3.1 Comparison

| Aspect | CVSS 4.0 | CVSS 3.1 | Notes |
|--------|----------|----------|-------|
| **Release Date** | Nov 2023 | Jun 2019 | 4.0 is current standard |
| **Score Range** | 0.0-10.0 | 0.0-10.0 | Same range, different calculation |
| **Metrics** | Base, Threat, Environmental, Supplemental | Base, Temporal, Environmental | 4.0 adds Supplemental metrics |
| **OT/IoT Support** | Native support | Limited | 4.0 better for OT environments |
| **Granularity** | Improved (e.g., "Safety" metric) | Standard | 4.0 more nuanced |
| **Adoption** | Growing (2024-2025) | Widespread | 3.1 still dominant in 2025 |

**Recommendation for [Organization]**:

- Prefer sources with "4.0 Full" or "4.0 Basic" support
- Accept "3.1 Full" as current standard (transition period)
- Flag "2.0 Only" for deprecation planning (obsolete)
- Avoid "None" / "Proprietary" for vulnerability tracking

## Appendix C: Sample Cost-Benefit Analysis

**Example: Commercial TI Platform**

| Metric | Value | Calculation |
|--------|-------|-------------|
| Annual Cost | CHF 50,000 | Contract price |
| Alerts Per Month | 150 | From SIEM integration |
| Incidents Prevented | 2 per year | Conservative estimate |
| Avg Incident Cost | CHF 100,000 | Industry benchmark |
| Estimated Savings | CHF 200,000 | 2 × CHF 100,000 |
| ROI Ratio | 4.0 | 200,000 / 50,000 |
| ROI Category | Good | 3.0-5.0 range |

**Sensitivity Analysis**:

- If only 1 incident prevented: ROI = 2.0 (break-even+)
- If 3 incidents prevented: ROI = 6.0 (excellent)
- Cost threshold for "Good" ROI: CHF 66,666 (at 2 incidents)

## Appendix D: Coverage Gap Prioritization Matrix

**Prioritization Framework**: Risk-based approach

| Risk Level | Coverage | Geography | Sector | Threat Type | Action |
|------------|----------|-----------|--------|-------------|--------|
| **Critical** | 0 sources | Switzerland, DACH | Financial | Ransomware, APT | Immediate acquisition |
| **High** | 1 source | Core markets | Critical Infra | Data Breach | Acquire within Q |
| **Medium** | 1 source | Adjacent markets | Other sectors | Phishing, DDoS | Plan for next FY |
| **Low** | 2+ sources | Any | Any | Any | Monitor, no action |

**Decision Criteria**:
1. **Business Impact**: What's the financial/operational impact if we miss a threat?
2. **Threat Likelihood**: How often do threats target this geography/sector?
3. **Current Visibility**: Do we have ANY coverage, or complete blind spot?
4. **Alternative Controls**: Can we compensate with other controls (e.g., EDR, WAF)?

**Example**: 

- Gap: Only 1 source covering Swiss financial sector ransomware
- Risk Level: **High** (critical sector + high likelihood)
- Action: Acquire additional source within Q1 2025
- Budget: Up to CHF 25,000 (half of primary source cost)

## Appendix E: Business Continuity Test Scenarios

**Scenario 1: Primary Analyst Unexpected Leave**

- **Trigger**: Primary TI analyst on medical leave (unplanned)
- **Duration**: 1 week simulation
- **Test Objective**: Backup can perform all critical functions
- **Success Criteria**: All sources accessed, daily report generated, urgent threat escalated

**Scenario 2: Platform Administrator Departure**

- **Trigger**: TI platform admin departs (planned)
- **Duration**: 2 days simulation
- **Test Objective**: Backup can administer TIP, manage integrations
- **Success Criteria**: User accounts managed, feeds reconfigured, no service disruption

**Scenario 3: Team Lead on Vacation**

- **Trigger**: TI Team Lead on vacation (planned)
- **Duration**: 2 weeks actual (not simulation)
- **Test Objective**: Operations continue without escalation to Team Lead
- **Success Criteria**: Routine operations maintained, only critical issues escalated to CISO

**Scenario 4: Disaster Recovery**

- **Trigger**: TIP platform failure, credentials vault inaccessible
- **Duration**: 4 hours simulation
- **Test Objective**: Recover access to critical sources from backup documentation
- **Success Criteria**: Access restored within 4 hours using offline backup

---

**END OF SPECIFICATION**

---

*"An expert is a person who has made all the mistakes that can be made in a very narrow field."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-01-31 -->

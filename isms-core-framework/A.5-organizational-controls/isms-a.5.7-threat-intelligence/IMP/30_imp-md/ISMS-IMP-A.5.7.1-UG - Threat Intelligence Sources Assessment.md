**ISMS-IMP-A.5.7.1-UG - Threat Intelligence Sources Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.1-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.7.1-TG.

---

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->

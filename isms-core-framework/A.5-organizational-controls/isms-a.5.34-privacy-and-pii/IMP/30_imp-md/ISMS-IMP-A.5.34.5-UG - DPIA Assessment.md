**ISMS-IMP-A.5.34.5-UG - Data Protection Impact Assessment (DPIA)**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.5-UG |
| **Version** | 1.0 |
| **Assessment Area** | Data Protection Impact Assessment (DPIA) for High-Risk Processing Activities |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.5 (Data Protection Impact Assessment) |
| **Purpose** | Guide users through DPIA trigger assessment, systematic risk evaluation, and compliance with GDPR Article 35 requirements for high-risk processing activities |
| **Target Audience** | DPO/Privacy Officers, Legal Counsel, Business Owners, Product Managers, IT/Security Teams, Compliance Officers, Auditors |
| **Assessment Type** | Risk Assessment & Compliance |
| **Review Cycle** | Annual or upon introduction of new high-risk processing activities |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for DPIA assessment workbook | ISMS Implementation Team |

---

**Document Purpose**

This implementation guide specifies procedures for conducting Data Protection Impact Assessments (DPIAs) as required by GDPR Article 35. A DPIA is a systematic process to evaluate the necessity, proportionality, and risks of processing operations that are likely to result in high risk to individuals' rights and freedoms.

**Key Objectives:**
1. Identify processing activities requiring DPIA (trigger assessment)
2. Conduct systematic risk assessment for high-risk processing
3. Implement appropriate mitigation measures to reduce risks
4. Maintain comprehensive DPIA register for audit and compliance
5. Ensure stakeholder consultation (DPO, data subjects, supervisory authority)
6. Track DPIA lifecycle from initial assessment through annual reviews

**Regulatory Foundation:**

**GDPR Article 35(1):** "Where a type of processing in particular using new technologies, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data."

**GDPR Article 35(3) - Mandatory DPIA Triggers:**

- (a) Systematic and extensive evaluation of personal aspects including profiling with legal/similarly significant effects
- (b) Large-scale processing of special category data (Art. 9) or criminal convictions (Art. 10)
- (c) Systematic monitoring of publicly accessible areas on a large scale (e.g., CCTV)

**Additional WP248 Triggers:**

- Innovative technologies or novel applications of existing technology
- Processing that prevents data subjects from exercising rights or using services
- Processing on a large scale
- Matching/combining datasets from different sources
- Processing vulnerable data subjects (children, employees, mentally ill)
- Processing involving cross-border data transfers outside EEA
- Decisions with potential to cause significant harm (automated decision-making)

**ISO/IEC 27001:2022 Control A.5.34 Requirement:** Organizations must implement privacy impact assessments when required by applicable privacy regulations.

---

**Target Audience:** Data Protection Officers (DPOs), Privacy Teams, Legal Counsel, Product Managers, System Architects, CISO

**Prerequisites:**

- Completion of ISMS-IMP-A.5.34.1 (PII Identification) - must know what PII you process
- Completion of ISMS-IMP-A.5.34.2 (Legal Basis) - must know lawful basis for processing
- Access to system architecture documentation (data flow diagrams)
- Stakeholder availability (DPO, system owners, legal counsel)

**Time Required:**

- **Initial DPIA Trigger Assessment:** 30-45 minutes per processing activity
- **Full DPIA Execution:** 4-8 hours per high-risk processing activity
- **Annual DPIA Review:** 1-2 hours per existing DPIA

**Important Note on DPIA Timing:** GDPR Article 35(1) requires DPIAs to be conducted **"prior to the processing"**. This means:

- For new projects: DPIA must be completed BEFORE processing begins (during design/procurement phase)
- For existing processing: DPIA should be completed retroactively if not previously done
- For material changes: DPIA must be updated BEFORE changes are implemented

---

### Assessment Overview: 8-Sheet Workbook Structure

**Layer 1 - Local Dashboard (Excel Formulas):**
Each DPIA workbook contains an embedded compliance dashboard (Sheet 8) that auto-calculates DPIA completion scores and risk levels using Excel formulas. This provides real-time visibility into DPIA status without external scripts.

**Layer 2 - BIG DASHBOARD (Python openpyxl):**
The A.5.34.7 Privacy Compliance Dashboard reads completed DPIA workbooks using Python's `load_workbook()` function to aggregate metrics across all privacy assessments (A.5.34.1 through A.5.34.6). This consolidation happens AFTER individual workbooks are completed.

**Layer 3 - Optional Consolidation (Post-Processing):**
A separate consolidation script can extract DPIA risk registers for enterprise risk management integration or supervisory authority reporting.

---

### Sheet-by-Sheet Completion Guide

---

#### SHEET 1: Instructions & Legend

**Purpose:** Provide guidance on completing the DPIA workbook and define terminology

**Who Completes:** DPO or Privacy Team (pre-populated template)

**Completion Status:** Pre-populated, read-only for users

**Key Sections:**

1. **Workbook Overview**

   - Purpose of DPIA assessment
   - When DPIA is required (Article 35 triggers)
   - Roles and responsibilities (DPO, system owner, legal counsel)
   - Expected completion timeline

2. **Sheet Navigation Guide**

   - Sheet 2: DPIA Trigger Assessment (30-45 min)
   - Sheet 3: DPIA Register (ongoing maintenance)
   - Sheet 4: Risk Assessment Matrix (2-4 hours per DPIA)
   - Sheet 5: Mitigation Measures (1-2 hours per DPIA)
   - Sheet 6: Stakeholder Consultation (30-60 min per DPIA)
   - Sheet 7: Gap Analysis (30 min per DPIA)
   - Sheet 8: Compliance Dashboard (auto-calculated)

3. **Terminology Legend**

   - **Processing Activity:** Specific data processing operation (e.g., "Employee performance tracking system")
   - **High Risk:** Likely to result in significant impact to data subjects' rights and freedoms
   - **Residual Risk:** Risk remaining after mitigation measures are applied
   - **Supervisory Authority:** Data protection authority in your jurisdiction (e.g., EDPS, ICO, CNIL)

4. **Risk Assessment Methodology**

   - **Likelihood Scale:** Rare (1), Unlikely (2), Possible (3), Likely (4), Almost Certain (5)
   - **Impact Scale:** Negligible (1), Minor (2), Moderate (3), Major (4), Severe (5)
   - **Risk Score = Likelihood × Impact** (1-25 scale)
   - **Risk Levels:**
     - Low (1-6): Standard controls adequate
     - Medium (8-12): Enhanced controls required
     - High (15-16): Senior management approval + comprehensive mitigation
     - Critical (20-25): Supervisory authority consultation required + fundamental redesign

5. **Color Coding System**

   - **Green:** DPIA not required OR DPIA complete with low residual risk
   - **Yellow:** DPIA required, in progress OR medium residual risk
   - **Red:** DPIA overdue OR high/critical residual risk
   - **Gray:** Not applicable or exempt

6. **Evidence Requirements**

   - System architecture diagrams (data flow diagrams showing PII processing)
   - Data processing agreements (DPAs) with processors
   - Privacy notices provided to data subjects
   - Security control implementation documentation
   - DPO consultation records
   - Supervisory authority correspondence (if applicable)

7. **Common Pitfalls**

   - Starting DPIA too late (after processing already began)
   - Conducting DPIA in isolation without stakeholder input
   - Generic risk assessments without processing-specific details
   - Failing to update DPIA when processing changes materially
   - Not consulting DPO or supervisory authority when required

**Mandatory Fields:** None (sheet is pre-populated reference material)

**Validation:** Read-only sheet

**Formula Logic:** None (instructional content only)

---

#### SHEET 2: DPIA Trigger Assessment

**Purpose:** Determine which processing activities require a full DPIA based on GDPR Article 35 criteria

**Who Completes:** DPO, Privacy Team, Product Managers, System Architects

**Completion Frequency:** 

- For new processing activities: During design/planning phase (before processing begins)
- For existing processing: Quarterly review to identify any newly risky activities
- For changed processing: Immediately when material changes occur

**Importance:** This is the screening step. Not all processing requires a full DPIA - only those "likely to result in high risk." Incorrectly skipping a DPIA when required can result in regulatory fines (up to €10M or 2% of global turnover under Article 83(4)).

**Columns (15 total):**

| Column | Field Name | Type | Description | Validation |
|--------|-----------|------|-------------|------------|
| A | Processing Activity ID | Text | Unique identifier (e.g., "PROC-001") | Dropdown from A.5.34.1 Sheet 2 |
| B | Processing Activity Name | Text | Descriptive name (e.g., "AI-powered resume screening") | Text (100 char max) |
| C | System/Application | Text | Technical system performing processing | Text (100 char max) |
| D | Trigger 1: Systematic Profiling | Yes/No | Automated evaluation with legal/significant effects (Art. 35(3)(a)) | Dropdown: Yes, No |
| E | Trigger 2: Large-Scale Special Categories | Yes/No | Health, biometric, genetic, race, religion data (Art. 9) at scale | Dropdown: Yes, No |
| F | Trigger 3: Systematic Monitoring | Yes/No | Large-scale monitoring of public areas (CCTV, tracking) | Dropdown: Yes, No |
| G | Trigger 4: Innovative Technology | Yes/No | Novel tech or novel use (AI, blockchain, IoT) | Dropdown: Yes, No |
| H | Trigger 5: Denial of Service | Yes/No | Processing prevents data subjects from exercising rights | Dropdown: Yes, No |
| I | Trigger 6: Large Scale | Yes/No | Affects significant number of data subjects (WP248: >5,000 people) | Dropdown: Yes, No |
| J | Trigger 7: Matching Datasets | Yes/No | Combining data from different sources/controllers | Dropdown: Yes, No |
| K | Trigger 8: Vulnerable Subjects | Yes/No | Children, employees, asylum seekers, elderly, patients | Dropdown: Yes, No |
| L | Trigger 9: Cross-Border Transfer | Yes/No | Transfers outside EEA without adequacy decision | Dropdown: Yes, No |
| M | Total Triggers | Number | Auto-calculated count of "Yes" answers | Formula: COUNTIF(D:L,"Yes") |
| N | DPIA Required? | Yes/No/Uncertain | Auto-determined based on trigger count | Formula: IF(M>=2,"Yes",IF(M=1,"Uncertain","No")) |
| O | Notes | Text | Justification or additional context | Text (500 char max) |

**Step-by-Step Completion Instructions:**

**Step 1: Identify Processing Activities**

- Import processing activity list from ISMS-IMP-A.5.34.1 (Sheet 2: System Inventory)
- Each row = one distinct processing activity
- Use same Processing Activity IDs for consistency across assessments

**Step 2: Answer Trigger Questions (Columns D-L)**
For each processing activity, answer 9 trigger questions:

**Column D - Systematic Profiling:**

- **Yes if:** Automated decision-making with legal/significant effects (hiring decisions, creditworthiness, insurance pricing, automated suspensions)
- **No if:** Processing doesn't involve automated profiling OR profiling has no legal/significant effects
- **Example Yes:** AI resume screening that automatically rejects candidates without human review
- **Example No:** Basic analytics on website usage (no individual decisions)

**Column E - Large-Scale Special Categories:**

- **Yes if:** Processing health data, biometric data, genetic data, racial/ethnic origin, religious beliefs, sex life, trade union membership AND affects >5,000 data subjects OR entire populations (employees, citizens)
- **No if:** Small-scale processing (<1,000 subjects) OR not special category data
- **Example Yes:** National health insurance database, employee health screening program
- **Example No:** Small clinic with 500 patients

**Column F - Systematic Monitoring:**

- **Yes if:** Continuous/regular monitoring of public areas (CCTV in public spaces, location tracking via mobile apps, internet activity monitoring at scale)
- **No if:** One-time monitoring OR monitoring non-public areas with consent
- **Example Yes:** City-wide CCTV network with facial recognition
- **Example No:** Office building security cameras (not public area)

**Column G - Innovative Technology:**

- **Yes if:** Using emerging technology (AI/ML, blockchain, IoT sensors, biometrics) OR using existing technology in novel way
- **No if:** Mature, widely deployed technology with established best practices
- **Example Yes:** Emotion recognition AI for customer service, smart city IoT sensors
- **Example No:** Standard CRM system, email marketing platform

**Column H - Denial of Service:**

- **Yes if:** Processing could prevent data subjects from accessing services, exercising rights, or entering contracts
- **No if:** Processing doesn't restrict access to services
- **Example Yes:** Blacklist for fraud prevention that denies banking services
- **Example No:** Optional loyalty program (subjects can opt out without consequences)

**Column I - Large Scale:**

- **Yes if:** WP248 criteria met: (a) Number of data subjects (>5,000 as threshold OR substantial proportion of population), (b) Volume of data, (c) Duration of processing, (d) Geographic extent
- **No if:** Small, limited processing
- **Example Yes:** National tax system, social media platform, telecom provider
- **Example No:** Single retail store customer database (500 customers)

**Column J - Matching Datasets:**

- **Yes if:** Combining data from multiple sources/controllers OR merging datasets for new purposes beyond original collection
- **No if:** Processing stays within single source and original purpose
- **Example Yes:** Matching HR data with badge access logs and email metadata for insider threat detection
- **Example No:** Standard customer data stored in single CRM

**Column K - Vulnerable Subjects:**

- **Yes if:** Data subjects in vulnerable position (children <16, employees, asylum seekers/refugees, elderly, mentally ill, prisoners)
- **No if:** General adult population with full capacity to consent
- **Example Yes:** School student records, employee monitoring, asylum seeker processing
- **Example No:** B2B customer data for corporate clients

**Column L - Cross-Border Transfer:**

- **Yes if:** Transferring PII outside EEA to countries WITHOUT adequacy decision (e.g., USA, India, China) even with SCCs/BCRs
- **No if:** Processing stays within EEA OR transfers to adequate countries (UK, Switzerland, Japan, etc.)
- **Example Yes:** Using US-based cloud provider (AWS, Azure, GCP) without data residency
- **Example No:** EU-only cloud hosting with data residency guarantee

**Step 3: Review Auto-Calculated Fields**

**Column M - Total Triggers:**

- Auto-calculated: Counts number of "Yes" answers in columns D-L
- Review for accuracy (if count seems wrong, check for typos in trigger columns)

**Column N - DPIA Required?:**

- Auto-determined logic:
  - **Yes:** 2+ triggers → DPIA mandatory (WP248 guidance: multiple criteria = high risk)
  - **Uncertain:** 1 trigger → DPO consultation required to decide
  - **No:** 0 triggers → Standard privacy controls sufficient, DPIA not required
- **Important:** "Uncertain" requires DPO judgment call - some single triggers are sufficient (e.g., special category data at scale always needs DPIA)

**Step 4: Document Justification (Column O)**

- For "Yes" → Explain which specific triggers apply and why (e.g., "AI-based hiring tool with automated rejection = systematic profiling + innovative tech")
- For "Uncertain" → Document DPO consultation outcome (e.g., "DPO reviewed: not large scale (<2,000 subjects), DPIA not required")
- For "No" → Confirm assessment rationale (e.g., "Standard employee onboarding, no special categories, no automated decisions")

**Step 5: Escalation for "Yes" Results**
For any processing marked "DPIA Required = Yes":
1. Create formal DPIA project (assign owner, timeline)
2. Register in Sheet 3 (DPIA Register) with status "Planned" or "In Progress"
3. If processing already started without DPIA → IMMEDIATE STOP until DPIA complete (regulatory violation)
4. Proceed to Sheet 4 (Risk Assessment) to conduct full DPIA

**Common Mistakes:**

❌ **Mistake 1:** "We only have 1 trigger, so no DPIA needed"

- **Wrong:** Single triggers CAN require DPIA (e.g., large-scale health data processing)
- **Correct:** Consult DPO for "Uncertain" cases, err on side of caution

❌ **Mistake 2:** "We've been processing for years, DPIA doesn't apply retroactively"

- **Wrong:** GDPR requires DPIA for ALL high-risk processing, even if predates GDPR
- **Correct:** Conduct DPIA retroactively for existing processing, document as remediation

❌ **Mistake 3:** "Small company = not large scale"

- **Wrong:** "Large scale" depends on data subjects affected, not company size
- **Correct:** A 50-person startup processing 100,000 user accounts IS large scale

❌ **Mistake 4:** "We use standard technology (AWS), not innovative"

- **Wrong:** "Innovative use" includes novel applications of existing tech
- **Correct:** AI/ML use cases on AWS cloud = innovative technology trigger

**Evidence Collection:**

- Meeting notes from DPO consultations on "Uncertain" cases
- Email approvals for "No DPIA required" decisions
- Project charter for processing activities marked "DPIA Required = Yes"

**Audit Trail:**

- Version control: Track changes to trigger assessments over time
- Quarterly reviews: Re-assess existing processing for new triggers (e.g., feature expansion makes processing "large scale")
- Material changes: Re-trigger DPIA assessment when processing significantly changes

---

#### SHEET 3: DPIA Register

**Purpose:** Maintain comprehensive catalog of all DPIAs (mandatory record-keeping per Article 5(2) accountability principle)

**Who Completes:** DPO or Privacy Team (ongoing maintenance)

**Completion Frequency:** 

- Add new DPIA within 1 week of identifying "DPIA Required = Yes" in Sheet 2
- Update status monthly as DPIAs progress through lifecycle
- Archive completed DPIAs annually (retain records for 3+ years)

**Importance:** The DPIA register demonstrates accountability to supervisory authorities. During audits, regulators will ask: "Show me your DPIA register." Missing DPIAs for high-risk processing can result in significant fines.

**Columns (18 total):**

| Column | Field Name | Type | Description | Validation |
|--------|-----------|------|-------------|------------|
| A | DPIA ID | Text | Unique identifier (e.g., "DPIA-2024-001") | Text, sequential numbering |
| B | Processing Activity ID | Text | Link to Sheet 2 trigger assessment | Dropdown from Sheet 2 Column A |
| C | Processing Activity Name | Text | Descriptive name | Auto-populated from Sheet 2 Column B |
| D | System/Application | Text | Technical system | Auto-populated from Sheet 2 Column C |
| E | Business Owner | Text | Department/person responsible | Dropdown: HR, IT, Marketing, Sales, Finance, Legal, Operations, Other |
| F | DPO Assigned | Text | DPO conducting assessment | Text (name of DPO or privacy analyst) |
| G | DPIA Start Date | Date | When DPIA project began | Date format: YYYY-MM-DD |
| H | Target Completion Date | Date | Planned finish date | Date format: YYYY-MM-DD |
| I | Actual Completion Date | Date | When DPIA was finalized | Date format: YYYY-MM-DD (blank until complete) |
| J | DPIA Status | Dropdown | Current lifecycle stage | Dropdown: Planned, In Progress, Under Review, Complete, Overdue |
| K | Initial Risk Rating | Dropdown | Risk before mitigation (from Sheet 4) | Dropdown: Low, Medium, High, Critical |
| L | Residual Risk Rating | Dropdown | Risk after mitigation (from Sheet 7) | Dropdown: Low, Medium, High, Critical |
| M | Supervisory Authority Consulted? | Yes/No | Required if residual risk remains high (Art. 36) | Dropdown: Yes, No, N/A |
| N | Authority Consultation Date | Date | When authority was consulted | Date format: YYYY-MM-DD (blank if not consulted) |
| O | Authority Reference Number | Text | Case number from authority | Text (e.g., "ICO-DPIA-2024-12345") |
| P | Next Review Date | Date | Annual DPIA review scheduled | Auto-calculated: Completion Date + 365 days |
| Q | DPIA Document Location | Text | File path or URL to full DPIA report | Text (file path or SharePoint URL) |
| R | Notes | Text | Additional context | Text (500 char max) |

**Step-by-Step Completion Instructions:**

**Step 1: Create DPIA Entry**

- When Sheet 2 shows "DPIA Required = Yes" → create new row in Sheet 3
- Assign sequential DPIA ID (e.g., DPIA-2024-001, DPIA-2024-002)
- Link to Processing Activity ID from Sheet 2 for traceability

**Step 2: Assign Ownership (Columns E-F)**

**Column E - Business Owner:**

- The department or individual responsible for the processing activity
- This is NOT the DPO - it's the business function that owns the system
- **Examples:**
  - HR system → HR department
  - Marketing automation → Marketing department
  - Customer portal → IT department

**Column F - DPO Assigned:**

- Name of DPO or privacy analyst conducting the DPIA
- One DPO can handle multiple DPIAs (centralized expertise)
- If outsourced, note consultant name (e.g., "External DPO - Smith & Associates")

**Step 3: Set Timeline (Columns G-I)**

**Column G - DPIA Start Date:**

- Date when DPIA project formally begins (kickoff meeting date)
- For new processing: Should be early in design phase (before development starts)
- For existing processing: Date of retroactive DPIA initiation

**Column H - Target Completion Date:**

- Planned finish date for DPIA
- **Recommended timeline:** 4-8 weeks from start for complex processing, 2-3 weeks for simpler assessments
- Must be BEFORE processing begins (for new activities)

**Column I - Actual Completion Date:**

- Leave blank until DPIA is finalized and approved
- Completion = all mitigation measures documented, DPO sign-off, business owner approval
- If completion date exceeds target → mark Status as "Overdue" (red flag)

**Step 4: Track Status (Column J)**

**Column J - DPIA Status:**

- **Planned:** DPIA identified as needed, not yet started (awaiting resources/approval)
- **In Progress:** Active DPIA work (stakeholder interviews, risk assessment, mitigation planning)
- **Under Review:** DPIA draft complete, awaiting approvals (DPO review, legal review, business owner sign-off)
- **Complete:** DPIA finalized, mitigation measures implemented, documented in register
- **Overdue:** Actual date > Target Completion Date AND status not "Complete" (requires escalation)

**Status Progression:** Planned → In Progress → Under Review → Complete
**Escalation:** If stuck in "In Progress" for >8 weeks → escalate to Senior Management

**Step 5: Document Risk Levels (Columns K-L)**

**Column K - Initial Risk Rating:**

- Risk level BEFORE applying mitigation measures
- Populated from Sheet 4 (Risk Assessment Matrix) - highest individual risk score
- **Determines urgency:**
  - Critical (20-25) → Immediate mitigation required, consider stopping processing
  - High (15-16) → Comprehensive mitigation plan required, senior management approval
  - Medium (8-12) → Standard mitigation controls acceptable
  - Low (1-6) → Minimal mitigation needed

**Column L - Residual Risk Rating:**

- Risk level AFTER applying mitigation measures
- Populated from Sheet 7 (Gap Analysis) - post-mitigation risk calculation
- **Acceptable residual risk:**
  - Low → Proceed with processing
  - Medium → Acceptable with monitoring and annual review
  - High/Critical → Requires supervisory authority consultation (GDPR Art. 36)

**Step 6: Supervisory Authority Consultation (Columns M-O)**

**GDPR Article 36(1):** "The controller shall consult the supervisory authority prior to processing where a data protection impact assessment [...] indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk."

**Column M - Supervisory Authority Consulted?:**

- **Yes:** Required when residual risk remains High or Critical despite mitigation
- **No:** Not required when residual risk reduced to Low or Medium
- **N/A:** DPIA not yet complete, TBD

**When consultation is required:**
1. Residual risk = High/Critical (even after mitigation)
2. Novel processing with no regulatory guidance
3. Processing likely to cause significant public concern
4. Uncertainty about adequacy of mitigation measures

**Column N - Authority Consultation Date:**

- Date when formal consultation was submitted to supervisory authority
- **Processing must stop until authority responds** (Art. 36(2): authority has 8 weeks to respond, extendable to 14 weeks)

**Column O - Authority Reference Number:**

- Case tracking number provided by supervisory authority
- Used for follow-up correspondence
- Example: "ICO-DPIA-2024-12345" (UK), "CNIL-DPIA-2024-67890" (France)

**Step 7: Schedule Next Review (Column P)**

**Column P - Next Review Date:**

- Auto-calculated: Actual Completion Date + 365 days
- **GDPR requires ongoing review** - DPIAs are not "one and done"
- Review trigger events (earlier than annual):
  - Material changes to processing (new data types, new purposes, new systems)
  - Security incidents affecting the processing activity
  - New regulatory guidance (e.g., EDPB guidelines on specific tech)
  - Complaints from data subjects
  - Supervisory authority feedback

**Step 8: Document Evidence (Column Q)**

**Column Q - DPIA Document Location:**

- File path or URL to full DPIA report (detailed documentation beyond this workbook)
- **Recommended structure:** SharePoint folder with subfolders per DPIA ID
  - `/DPIAs/DPIA-2024-001/DPIA-Report-Final.pdf`
  - `/DPIAs/DPIA-2024-001/Risk-Assessment-Details.xlsx`
  - `/DPIAs/DPIA-2024-001/Stakeholder-Consultation-Minutes.docx`
  - `/DPIAs/DPIA-2024-001/Authority-Correspondence/`

**Step 9: Add Contextual Notes (Column R)**

- Document exceptions or special circumstances
- **Examples:**
  - "Retroactive DPIA for legacy system - processing stopped pending mitigation"
  - "Supervisory authority provided verbal approval pending formal response"
  - "DPIA delayed due to vendor data processing agreement negotiation"

**Common Pitfalls:**

❌ **Pitfall 1: Incomplete DPIA Register**

- **Mistake:** Only registering DPIAs that were actually completed, not those identified as required
- **Correct:** Register ALL processing activities where Sheet 2 shows "DPIA Required = Yes", even if DPIA hasn't started yet (mark as "Planned")

❌ **Pitfall 2: No Follow-Through on "Overdue" Status**

- **Mistake:** DPIAs stuck in "In Progress" for months with no escalation
- **Correct:** Monthly status review, escalate overdue DPIAs to CISO/CPO, reassign resources if needed

❌ **Pitfall 3: Missing Authority Consultation**

- **Mistake:** Proceeding with high residual risk without consulting supervisory authority
- **Correct:** GDPR Article 36 requires consultation for high residual risk - non-negotiable

❌ **Pitfall 4: Forgetting Annual Reviews**

- **Mistake:** Completing DPIA and never reviewing again (treating as checkbox exercise)
- **Correct:** Set calendar reminders for Next Review Date, update DPIA for any material changes

**Audit Questions to Prepare For:**
1. "How many DPIAs have you conducted in the past 12 months?" → Count rows with Actual Completion Date in last year
2. "Show me DPIAs for your highest-risk processing." → Sort by Initial Risk Rating (Critical/High)
3. "What DPIAs are currently overdue?" → Filter Status = "Overdue"
4. "Have you consulted us (supervisory authority) when required?" → Review Column M for "Yes" entries with supporting evidence

**Integration with Other Assessments:**

- **A.5.34.1 (PII Identification):** Processing activities flow from Sheet 2 System Inventory
- **A.5.34.2 (Legal Basis):** Legal basis documented in DPIA must match Legal Basis Assessment
- **A.5.34.4 (TOMs):** Technical/organizational measures from DPIA feed into TOMs assessment
- **A.5.34.7 (Dashboard):** DPIA completion rate tracked in master compliance dashboard

---

#### SHEET 4: Risk Assessment Matrix

**Purpose:** Systematically assess risks to data subjects' rights and freedoms for each processing activity requiring DPIA

**Who Completes:** DPO, Privacy Team, System Architects, Security Team, Legal Counsel

**Completion Frequency:** Once per DPIA (during "In Progress" phase), updated if processing changes materially

**Importance:** This is the core of the DPIA - identifying and evaluating risks. GDPR Article 35(7) requires DPIAs to contain:

- (a) Systematic description of processing operations and purposes
- (b) Assessment of necessity and proportionality
- (c) Assessment of risks to rights and freedoms
- (d) Measures to address risks

Sheet 4 covers items (a)-(c). Sheet 5 covers item (d).

**Columns (20 total):**

| Column | Field Name | Type | Description | Validation |
|--------|-----------|------|-------------|------------|
| A | DPIA ID | Text | Link to DPIA Register | Dropdown from Sheet 3 Column A |
| B | Risk ID | Text | Unique risk identifier (e.g., "DPIA-2024-001-R01") | Auto-generated: DPIA ID + "-R" + sequential number |
| C | Risk Category | Dropdown | Type of risk to data subjects | Dropdown: See risk categories below |
| D | Risk Description | Text | Detailed description of specific risk | Text (500 char max) |
| E | Data Subject Impact | Text | How data subjects are harmed | Text (300 char max) |
| F | Likelihood (Before Mitigation) | Dropdown | Probability risk will materialize | Dropdown: 1-Rare, 2-Unlikely, 3-Possible, 4-Likely, 5-Almost Certain |
| G | Impact (Before Mitigation) | Dropdown | Severity of harm to data subjects | Dropdown: 1-Negligible, 2-Minor, 3-Moderate, 4-Major, 5-Severe |
| H | Inherent Risk Score | Number | Likelihood × Impact (before mitigation) | Formula: =F*G |
| I | Inherent Risk Level | Text | Risk classification | Formula: =IF(H>=20,"Critical",IF(H>=15,"High",IF(H>=8,"Medium","Low"))) |
| J | Necessity Justified? | Yes/No | Is processing necessary for stated purpose? (Art. 35(7)(b)) | Dropdown: Yes, No, Uncertain |
| K | Necessity Justification | Text | Why processing is necessary | Text (300 char max) |
| L | Proportionality Justified? | Yes/No | Are data minimization principles followed? (Art. 35(7)(b)) | Dropdown: Yes, No, Uncertain |
| M | Proportionality Justification | Text | Evidence of data minimization | Text (300 char max) |
| N | Legal Basis | Dropdown | GDPR Article 6 lawful basis | Dropdown: Consent, Contract, Legal Obligation, Vital Interests, Public Task, Legitimate Interests |
| O | Special Category Legal Basis | Dropdown | GDPR Article 9 basis (if applicable) | Dropdown: N/A, Explicit Consent, Employment Law, Vital Interests, Medical Purposes, Public Health, Archiving/Research |
| P | Data Subject Rights Respected? | Yes/No | Can subjects exercise rights (access, erasure, etc.)? | Dropdown: Yes, No, Partial |
| Q | Rights Restrictions Documented | Text | Justification for any restrictions on rights | Text (300 char max) |
| R | Third-Party Recipients | Text | Who receives data (processors, joint controllers) | Text (200 char max) |
| S | Cross-Border Transfers | Yes/No | Data transferred outside EEA? | Dropdown: Yes, No |
| T | Transfer Safeguards | Text | SCCs, BCRs, adequacy decision, etc. | Text (200 char max) |

**Risk Categories (Column C):**

The following risk categories align with WP248 guidelines and ISO/IEC 29134:2017:

1. **Discrimination:** Processing could lead to unfair treatment (e.g., algorithmic bias in hiring, credit scoring discrimination against protected classes)

2. **Identity Theft/Fraud:** PII could be stolen/misused (e.g., SSN exposure, financial data breach, account takeover)

3. **Financial Loss:** Data subjects could suffer economic harm (e.g., unauthorized transactions, credit damage, employment termination)

4. **Reputational Damage:** Disclosure could harm reputation (e.g., health data leak, embarrassing personal info exposure, online shaming)

5. **Physical Harm:** Processing could endanger physical safety (e.g., location data revealing domestic abuse victim whereabouts, health data exposure leading to insurance denial for critical treatment)

6. **Loss of Confidentiality:** Unauthorized disclosure (e.g., medical records breach, whistleblower identity revealed, trade secrets exposed via employee monitoring)

7. **Loss of Control:** Data subjects cannot manage their data (e.g., inability to correct inaccurate data, no opt-out mechanism, data sold to third parties without knowledge)

8. **Surveillance:** Excessive monitoring creating chilling effects (e.g., continuous employee surveillance, behavioral tracking affecting free expression, public space monitoring deterring lawful activity)

9. **Profiling with Significant Effects:** Automated decisions affecting opportunities (e.g., loan denial, job application rejection, insurance rate increases, all without human review)

10. **Social Disadvantage:** Processing perpetuates inequality (e.g., algorithmic amplification of existing biases, digital exclusion of vulnerable groups, processing that disadvantages minorities)

11. **Psychological Harm:** Emotional distress (e.g., anxiety from data breach notification, stress from surveillance, manipulation via behavioral targeting)

12. **Loss of Rights/Freedoms:** Inability to exercise fundamental rights (e.g., freedom of expression chilled by monitoring, freedom of movement restricted by tracking, political participation deterred)

**Step-by-Step Completion Instructions:**

**Step 1: Link to DPIA (Column A)**

- Select DPIA ID from Sheet 3 register
- All risks for a single processing activity will share same DPIA ID
- Typical DPIA has 5-15 distinct risks identified

**Step 2: Identify Risks (Columns B-E)**

**Column B - Risk ID:**

- Auto-generated format: `[DPIA ID]-R[sequential number]`
- Example: DPIA-2024-001-R01, DPIA-2024-001-R02, etc.

**Column C - Risk Category:**

- Select from predefined list (see categories above)
- One risk can fit multiple categories - choose the PRIMARY category
- If uncertain, default to "Loss of Confidentiality" (most common)

**Column D - Risk Description:**

- Describe the specific risk scenario (not generic)
- **Bad example:** "Data breach could occur"
- **Good example:** "Customer PII stored in unencrypted S3 bucket accessible via misconfigured IAM policy could be exfiltrated by unauthorized attacker, exposing names, addresses, and payment card data of 50,000 customers"

**Column E - Data Subject Impact:**

- Explain concrete harm to individuals (not organization)
- **Bad example:** "Reputational damage to company"
- **Good example:** "Customers could suffer identity theft requiring credit monitoring, potential financial fraud, emotional distress from breach notification, and loss of trust in service"

**Step 3: Assess Likelihood and Impact (Columns F-I)**

**Column F - Likelihood (Before Mitigation):**

Assess probability the risk will materialize WITHOUT mitigation controls:

- **1 - Rare:** <5% chance, requires multiple unlikely failures, no precedent in industry
  - *Example:* Breach of air-gapped system with no network connectivity

- **2 - Unlikely:** 5-25% chance, requires specific vulnerabilities to be exploited
  - *Example:* SQL injection on well-maintained system with regular security patches

- **3 - Possible:** 25-50% chance, vulnerabilities known but not actively exploited
  - *Example:* Phishing attack against employees without security awareness training

- **4 - Likely:** 50-75% chance, common attack vector with known exploits
  - *Example:* Ransomware attack against unpatched Windows systems (WannaCry-style)

- **5 - Almost Certain:** >75% chance, inevitable without controls
  - *Example:* Public S3 bucket with PII (Shodan will find it within days)

**Column G - Impact (Before Mitigation):**

Assess severity of harm to data subjects if risk materializes:

- **1 - Negligible:** No material harm, minor inconvenience
  - *Example:* Exposure of publicly available information (company name)

- **2 - Minor:** Limited, reversible harm
  - *Example:* Temporary service disruption, need to reset password

- **3 - Moderate:** Significant but manageable harm
  - *Example:* Financial loss <€1,000, reputational damage requiring explanation

- **4 - Major:** Severe harm with lasting consequences
  - *Example:* Identity theft requiring years to resolve, job loss, significant financial damage

- **5 - Severe:** Catastrophic harm, potentially irreversible
  - *Example:* Physical harm (domestic abuse victim location revealed), life-altering discrimination, severe psychological trauma

**Column H - Inherent Risk Score:**

- Auto-calculated: Likelihood × Impact
- Range: 1 to 25

**Column I - Inherent Risk Level:**

- Auto-determined based on score:
  - **Low (1-6):** Acceptable risk, standard controls sufficient
  - **Medium (8-12):** Moderate risk, enhanced controls required
  - **High (15-16):** Significant risk, comprehensive mitigation + management approval
  - **Critical (20-25):** Unacceptable risk, fundamental redesign or supervisory authority consultation

**Step 4: Assess Necessity and Proportionality (Columns J-M)**

**GDPR Article 35(7)(b) Requirement:** DPIA must include "an assessment of the necessity and proportionality of the processing operations in relation to the purposes."

**Column J - Necessity Justified?**

- **Yes:** Processing is necessary to achieve stated purpose, no less intrusive alternative exists
- **No:** Processing is not strictly necessary, alternatives available
- **Uncertain:** Requires further analysis or legal review

**Column K - Necessity Justification:**

- Document why processing is necessary
- **Test:** Could the purpose be achieved without this processing? If yes → not necessary
- **Good example:** "Credit scoring requires financial history analysis - no alternative method to assess creditworthiness exists that doesn't involve processing financial PII"
- **Bad example:** "We've always done it this way"

**Column L - Proportionality Justified?**

- **Yes:** Data minimization principles followed (Art. 5(1)(c)), only collect/process minimum necessary data
- **No:** Processing excessive data beyond what's needed
- **Uncertain:** Requires data inventory review

**Column M - Proportionality Justification:**

- Document evidence of data minimization
- **Good example:** "Marketing campaign only requires email + first name for personalization. We do NOT collect full postal address, phone, or demographic data because unnecessary for email marketing purpose."
- **Bad example:** "We collect everything just in case we need it later"

**Step 5: Document Legal Basis (Columns N-O)**

**Column N - Legal Basis:**

- Select GDPR Article 6 lawful basis (must align with A.5.34.2 Legal Basis Assessment)
- **Consent:** Freely given, specific, informed, unambiguous (high bar)
- **Contract:** Processing necessary for contract performance (e.g., shipping address for order fulfillment)
- **Legal Obligation:** Required by law (e.g., tax reporting, employment law)
- **Vital Interests:** Life-or-death situations (rarely applicable)
- **Public Task:** Public authorities performing official functions
- **Legitimate Interests:** Balancing test - your interests vs. data subject rights (requires DPIA for high-risk cases)

**Column O - Special Category Legal Basis:**

- Required ONLY if processing special category data (Art. 9: health, biometric, genetic, race, religion, sex life, trade union)
- **N/A:** Not processing special categories
- **Explicit Consent:** Higher bar than Art. 6 consent (must be explicit, not implied)
- **Employment Law:** Necessary for employment/social security law compliance
- **Vital Interests:** Emergency medical treatment when subject cannot consent
- **Medical Purposes:** Healthcare provision, medical diagnosis (requires professional secrecy)
- **Public Health:** Public health emergencies (COVID-19 contact tracing)
- **Archiving/Research:** Scientific/historical research with safeguards

**Step 6: Assess Data Subject Rights (Columns P-Q)**

**Column P - Data Subject Rights Respected?**

- **Yes:** All GDPR Chapter III rights fully available (access, rectification, erasure, restriction, portability, objection, automated decision-making)
- **No:** One or more rights significantly restricted
- **Partial:** Some restrictions apply but with valid legal justification

**Column Q - Rights Restrictions Documented:**

- If "No" or "Partial" → document legal justification for restrictions
- **Valid restrictions:**
  - Art. 17(3): Erasure not possible due to legal obligation to retain (e.g., tax records)
  - Art. 21(1): Objection not possible due to legal basis override (e.g., contract necessity)
- **Invalid restrictions:**
  - "It's technically difficult to implement" → Not a valid restriction
  - "We don't want to" → Not acceptable

**Step 7: Document Third-Party Sharing (Columns R-T)**

**Column R - Third-Party Recipients:**

- List all recipients of PII (processors, joint controllers, third-party controllers)
- **Examples:**
  - "AWS (cloud infrastructure processor), Salesforce (CRM processor), Google Analytics (analytics processor)"
  - "Partner company XYZ Corp (joint controller for marketing campaign)"

**Column S - Cross-Border Transfers:**

- **Yes:** Data leaves EEA (even if to "adequate" country, document it)
- **No:** Data stays within EEA

**Column T - Transfer Safeguards:**

- Document legal mechanism for transfers
- **Examples:**
  - "SCCs (Standard Contractual Clauses) executed with AWS on 2024-01-15"
  - "Adequacy decision (UK under Art. 45)"
  - "BCRs (Binding Corporate Rules) for intra-group transfers"
  - "Consent (Art. 49(1)(a)) for non-repeated transfers"

**Common Pitfalls:**

❌ **Pitfall 1: Generic Risk Descriptions**

- **Mistake:** "Data breach risk" without specifics
- **Correct:** Describe the specific vulnerability, attack vector, and impact (see Column D guidance)

❌ **Pitfall 2: Underestimating Likelihood/Impact**

- **Mistake:** Marking everything "Low" to avoid mitigation work
- **Correct:** Be honest about risks - auditors/regulators will challenge unrealistic ratings

❌ **Pitfall 3: Confusing Necessity with Convenience**

- **Mistake:** "We need this data for business intelligence" (want ≠ need)
- **Correct:** Necessity means no alternative exists to achieve purpose

❌ **Pitfall 4: Missing Special Category Basis**

- **Mistake:** Processing health data with only Art. 6 basis (missing Art. 9 basis)
- **Correct:** Special category data requires BOTH Art. 6 AND Art. 9 legal basis

**Evidence Collection:**

- Data flow diagrams showing processing operations
- System architecture diagrams (where data is stored/processed)
- Data processing agreements (DPAs) with processors
- Standard Contractual Clauses (SCCs) for transfers
- Privacy notices provided to data subjects
- Consent records (if consent is legal basis)

**Output from Sheet 4:**

- Inherent risk scores feed into Sheet 5 (Mitigation Measures) → determine which controls to implement
- Highest inherent risk becomes "Initial Risk Rating" in Sheet 3 (DPIA Register)
- Risks with "Necessity = No" or "Proportionality = No" → require processing redesign (fundamental DPIA requirement)

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->

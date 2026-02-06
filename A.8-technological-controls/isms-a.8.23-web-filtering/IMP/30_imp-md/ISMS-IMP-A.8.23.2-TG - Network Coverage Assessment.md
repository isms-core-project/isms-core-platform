**ISMS-IMP-A.8.23.2-TG - Network Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.23: Web Filtering

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.23.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Web Filtering Network Coverage & Deployment Topology |
| **Related Policy** | ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements) |
| **Purpose** | Verify WHERE web filtering is applied across network topology, identify coverage gaps, and ensure comprehensive protection across all network segments where users/devices access the internet |
| **Target Audience** | Network Engineers, Security Engineers, Infrastructure Team, System Administrators, System Owners, Compliance Officers, Auditors, Workbook Developers (Python/Excel script maintainers) |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Web Filtering Network Coverage assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.23.2-UG.

---

# Technical Specification

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section

- **Title:** "ISMS-IMP-A.8.23.2 – Network Coverage Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.23: Web Filtering"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.23.2
Assessment Area:       Network Coverage & Deployment Topology
Related Policy:        ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

**Audience:** Workbook developers, Python script maintainers

**Note:** This section provides technical specifications for workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section

- **Title:** "ISMS-IMP-A.8.23.2 — Network Coverage Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.23: Web Filtering"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```plaintext
Document ID:           ISMS-IMP-A.8.23.2
Assessment Area:       Network Coverage & Deployment Topology
Related Policy:        ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Complete Network_Segment_Inventory for EVERY network segment in your environment
2. Document YOUR specific network architecture (office LANs, WLANs, VPN, cloud, etc.)
3. Map filtering solutions to network segments in Coverage_Matrix
4. Calculate coverage percentages and identify gaps
5. Document any devices/segments exempt from filtering in Exemption_Register
6. Track evidence in Evidence_Register
7. Review and approve via Approval_Sign_Off
8. Update quarterly or after network topology changes
9. Coordinate with ISMS-IMP-A.8.23.1 (Infrastructure Assessment)

#### Status Legend
 | Symbol | Status | Description | Color Code | 
 | -------- | -------- | ------------- | ------------ | 
 | ✅ | Protected | Web filtering active and operational | Green (C6EFCE) | 
 | ⚠️ | Partial | Partial coverage or limited protection | Yellow (FFEB9C) | 
 | ❌ | Unprotected | No web filtering deployed | Red (FFC7CE) | 
 | 🔄 | Planned | Protection planned with target date | Blue (B4C7E7) | 
 | 🚫 | Exempt | Approved exemption (documented) | Gray (D9D9D9) | 

#### Network Segment Types (Examples)
Organizations map THEIR environment to these generic types:

- **On-Premises LANs** (corporate office networks)
- **Wireless Networks (WLAN)** (corporate WiFi, guest WiFi)
- **Remote Access / VPN** (remote workers, site-to-site VPN)
- **Cloud-Based Endpoints** (VDI, DaaS, Windows 365, virtual desktops)
- **Guest/Partner Networks** (visitor access, vendor access)
- **DMZ / Extranet** (public-facing services, partner connections)
- **Branch Offices** (remote sites, field offices)
- **Mobile Devices** (smartphones, tablets, laptops outside VPN)
- **IoT/OT Networks** (building systems, manufacturing, special-purpose)
- **Development/Test Networks** (staging environments, labs)

#### Acceptable Evidence (Examples)

- ✓ Network topology diagrams
- ✓ VLAN configurations and documentation
- ✓ Firewall/routing policies showing filtering enforcement
- ✓ DHCP configurations (DNS redirection, proxy settings)
- ✓ VPN concentrator configurations
- ✓ Cloud service dashboards (showing endpoint protection)
- ✓ WiFi controller configurations
- ✓ Network access control (NAC) policies
- ✓ Exemption request approvals (email, tickets)
- ✓ Coverage verification tests/reports
- ✓ Network monitoring dashboards
- ✓ Change management records for network modifications

---

## Sheet 2: Network_Segment_Inventory

### Purpose
Document EVERY network segment where users/devices can access the internet. This is the foundation for coverage analysis.

### Header Section
**Row 1:** "NETWORK SEGMENT INVENTORY"  
**Row 2:** "Document all network segments requiring web filtering protection"

### Column Structure (Rows 4+)

 | Column | Header | Width | Type | Validation | 
 | -------- | -------- | ------- | ------ | ------------ | 
 | A | Segment ID | 15 | Text | Auto-generated (SEG-001) | 
 | B | Segment Name | 30 | Text | Customer fills in | 
 | C | Segment Type | 25 | Dropdown | On-Premises LAN, WLAN, VPN, Cloud Endpoints, Guest, DMZ, Branch, Mobile, IoT/OT, Dev/Test, Other | 
 | D | Location/Site | 25 | Text | Physical or logical location | 
 | E | Subnet/VLAN | 20 | Text | Network address (e.g., 192.168.10.0/24, VLAN 100) | 
 | F | User Count | 12 | Number | Approximate users on this segment | 
 | G | Device Count | 12 | Number | Approximate devices | 
 | H | Internet Access? | 15 | Dropdown | Yes, No, Restricted | 
 | I | Filtering Required? | 15 | Dropdown | Yes, No, N/A | 
 | J | Filtering Status | 18 | Dropdown | ✅ Protected, ⚠️ Partial, ❌ Unprotected, 🔄 Planned, 🚫 Exempt | 
 | K | Filtering Solution(s) | 30 | Text | Which solution(s) protect this segment? | 
 | L | Coverage % | 12 | Number | 0-100% | 
 | M | Bypass Methods | 25 | Text | Any known ways to bypass filtering? | 
 | N | Exemption ID | 15 | Text | If exempt, reference exemption | 
 | O | Evidence | 35 | Text | Evidence location | 

**Data Rows:** 50 rows for segment documentation

### Segment Details Template (Rows 60+)

For each critical segment, provide detailed analysis:

**Segment Detail Section (repeatable):**
```
SEGMENT: [Segment Name from inventory]
────────────────────────────────────────────────────────────

Traffic Flow:
  • Inbound:  [Describe]
  • Outbound: [Describe]
  • Lateral:  [Describe]

Filtering Implementation:
  • Enforcement Point:    [Where is filtering applied?]
  • Technology:           [Which solution?]
  • Policy Applied:       [Which filtering policy?]
  • HTTPS Inspection:     [Yes/No/Partial]

User Profile:
  • User Types:           [Employees/Guests/Contractors/etc.]
  • Risk Level:           [High/Medium/Low]
  • Acceptable Use:       [Compliance with AUP?]

Technical Details:
  • Default Gateway:      [IP address or N/A]
  • DNS Servers:          [IP addresses]
  • Proxy Settings:       [Automatic/Manual/None]
  • Authentication:       [Required/Optional/None]

Gaps/Issues:
  • Coverage Gaps:        [Describe any gaps]
  • Bypass Risks:         [Known bypass methods?]
  • Remediation Plan:     [If gaps exist]
```

---

## Sheet 3: Coverage_Matrix

### Purpose
Cross-reference network segments with filtering solutions to visualize coverage.

### Header
**Row 1:** "NETWORK COVERAGE MATRIX"  
**Row 2:** "Map filtering solutions to network segments"

### Matrix Structure (Rows 4+)

 | Network Segment | Solution 1 | Solution 2 | Solution 3 | Solution 4 | Total Coverage | Status | 
 | ----------------- | ----------- | ----------- | ----------- | ----------- | ---------------- | -------- | 
 | [SEG-001] Corp LAN | ✅ 100% | - | - | - | 100% | ✅ Protected | 
 | [SEG-002] Guest WiFi | - | ✅ 100% | - | - | 100% | ✅ Protected | 
 | [SEG-003] VPN | ⚠️ 60% | - | ⚠️ 40% | - | 100% | ⚠️ Multiple | 
 | ... |  |  |  |  |  |  | 

**Legend:**

- ✅ XX% = Protected by this solution (percentage coverage)
- ❌ = Not protected by this solution
- ⚠️ = Partial coverage
- 🚫 = Exempt from this solution

**Summary Row (auto-calculated):**

- Total segments assessed: [COUNT]
- Fully protected (100%): [COUNT]
- Partially protected (<100%): [COUNT]
- Unprotected (0%): [COUNT]
- Exempted: [COUNT]

### Coverage Heatmap Section

Visual representation of coverage quality:

 | Coverage Level | Segment Count | % of Total | Status | 
 | ---------------- | --------------- | ------------ | -------- | 
 | 100% Coverage | [Formula] | [Formula] | ✅ Good | 
 | 75-99% Coverage | [Formula] | [Formula] | ⚠️ Needs Attention | 
 | 50-74% Coverage | [Formula] | [Formula] | ⚠️ Risk | 
 | <50% Coverage | [Formula] | [Formula] | ❌ Critical | 
 | 0% Coverage | [Formula] | [Formula] | ❌ Urgent | 
 | Exempt | [Formula] | [Formula] | 🚫 Approved | 

**Overall Network Coverage Score:** [Formula calculating weighted average]

---

## Sheet 4: Gap_Identification

### Purpose
Document segments with insufficient filtering coverage and track remediation.

### Header
**Row 1:** "COVERAGE GAPS & REMEDIATION TRACKING"  
**Row 2:** "Identify unprotected/partially protected segments and plan remediation"

### Gap Register (Rows 4+)

 | Gap ID | Segment ID | Segment Name | Current Coverage | Gap Description | Risk Level | Impact | Remediation Plan | Owner | Target Date | Status | Budget | 
 | -------- | ----------- | -------------- | ------------------ | ----------------- | ------------ | -------- | ------------------ | ------- | ------------- | -------- | -------- | 
 | GAP-001 | [Auto-pull] | [Auto-pull] | XX% | [Describe gap] | Dropdown | Text | Text | Text | Date | Dropdown | Dropdown | 

**Columns:**

- **Gap ID:** Auto-generated (GAP-001, GAP-002, etc.)
- **Segment ID:** Reference to Network_Segment_Inventory
- **Current Coverage:** Percentage (0-100%)
- **Risk Level:** Critical / High / Medium / Low
- **Impact:** Business impact description
- **Remediation Plan:** How will gap be closed?
- **Status:** Open / In Progress / Resolved / Accepted Risk / Exempt

**Data Rows:** 30 rows for gap tracking

### Gap Summary Metrics

 | Risk Level | Gap Count | % of Total | Avg Time Open | 
 | ------------ | ----------- | ------------ | --------------- | 
 | Critical | [Formula] | [Formula] | [Formula] | 
 | High | [Formula] | [Formula] | [Formula] | 
 | Medium | [Formula] | [Formula] | [Formula] | 
 | Low | [Formula] | [Formula] | [Formula] | 

### Key Metrics

- Total gaps identified: [Formula]
- Gaps resolved: [Formula]
- Gaps remaining: [Formula]
- Average remediation time: [Formula] days
- Segments at risk: [Formula]

---

## Sheet 5: Device_Inventory

### Purpose
Track individual devices/endpoints and their filtering protection status (especially for BYOD, mobile, remote workers).

### Header
**Row 1:** "DEVICE-LEVEL FILTERING INVENTORY"  
**Row 2:** "Track endpoint protection for mobile/remote devices"

### Device Registry (Rows 4+)

 | Device ID | Device Type | OS | User/Owner | Primary Network | Filtering Solution | Agent-Based? | Status | Last Verified | Evidence | 
 | ----------- | ------------- | ---- | ----------- | ----------------- | -------------------- | -------------- | -------- | --------------- | ---------- | 
 | DEV-001 | Dropdown | Text | Text | Dropdown | Text | Dropdown | Dropdown | Date | Text | 

**Columns:**

- **Device ID:** Auto-generated
- **Device Type:** Laptop / Desktop / Smartphone / Tablet / Virtual Desktop / Other
- **OS:** Windows / macOS / Linux / iOS / Android / ChromeOS / Other
- **User/Owner:** Employee name or department
- **Primary Network:** Which segment is this device usually on?
- **Filtering Solution:** Which solution protects this device?
- **Agent-Based?:** Yes (endpoint agent) / No (network-based) / Hybrid
- **Status:** ✅ Protected / ⚠️ Partial / ❌ Unprotected / 🔄 Pending
- **Last Verified:** Date of last verification

**Data Rows:** 100 rows for device tracking

**Use Cases:**

- BYOD (Bring Your Own Device) programs
- Remote workers outside VPN
- Mobile devices (smartphones/tablets)
- Executive/VIP devices requiring special attention
- Contractor/temporary worker devices

### Device Summary

 | Device Type | Total | Protected | Unprotected | Coverage % | 
 | ------------- | ------- | ----------- | ------------- | ------------ | 
 | Laptops | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Desktops | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Smartphones | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Tablets | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Virtual Desktops | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Other | [Formula] | [Formula] | [Formula] | [Formula] | 

---

## Sheet 6: Exemption_Register

### Purpose
Document approved exemptions from web filtering requirements with business justification.

### Header
**Row 1:** "FILTERING EXEMPTION REGISTER"  
**Row 2:** "Document approved exceptions to web filtering requirements"

### Exemption Registry (Rows 4+)

 | Exemption ID | Segment/Device | Exemption Type | Business Justification | Risk Assessment | Compensating Controls | Approved By | Approval Date | Review Date | Status | Evidence | 
 | -------------- | --------------- | ---------------- | ------------------------ | ----------------- | ---------------------- | ------------- | --------------- | ------------- | -------- | ---------- | 
 | EXM-001 | Text | Dropdown | Text | Text | Text | Text | Date | Date | Dropdown | Text | 

**Columns:**

- **Exemption ID:** Auto-generated (EXM-001)
- **Segment/Device:** What is exempt?
- **Exemption Type:** Dropdown:
  - Full Exemption (no filtering)
  - Partial Exemption (reduced filtering)
  - Temporary Exemption (time-limited)
  - Category Exemption (specific categories allowed)
  - Technical Exemption (incompatibility)
- **Business Justification:** Why is exemption necessary?
- **Risk Assessment:** What risks does this create?
- **Compensating Controls:** How is risk mitigated?
  - Enhanced monitoring
  - Network segmentation
  - Restricted access
  - Alternative controls
- **Approved By:** Name and role (must be CISO or delegate)
- **Approval Date:** When was exemption granted?
- **Review Date:** When must exemption be reviewed? (max 12 months)
- **Status:** Active / Expired / Revoked / Under Review
- **Evidence:** Link to approval documentation

**Data Rows:** 20 rows for exemption tracking

### Exemption Summary

 | Exemption Type | Active Count | Expired/Overdue | Avg Duration | 
 | ---------------- | -------------- | ----------------- | -------------- | 
 | Full Exemption | [Formula] | [Formula] | [Formula] | 
 | Partial Exemption | [Formula] | [Formula] | [Formula] | 
 | Temporary Exemption | [Formula] | [Formula] | [Formula] | 
 | Category Exemption | [Formula] | [Formula] | [Formula] | 
 | Technical Exemption | [Formula] | [Formula] | [Formula] | 

**Alert Conditions:**

- ⚠️ Exemptions >12 months old require re-approval
- ⚠️ Exemptions without compensating controls = HIGH RISK
- ⚠️ >10% of segments exempt = escalate to CISO

---

## Sheet 7: Coverage_Verification

### Purpose
Document testing/verification that filtering is actually working on each segment.

### Header
**Row 1:** "COVERAGE VERIFICATION LOG"  
**Row 2:** "Test and verify filtering effectiveness per network segment"

### Verification Log (Rows 4+)

 | Verification ID | Segment ID | Segment Name | Test Date | Tester | Test Method | Test Results | Issues Found | Status | Next Test Date | 
 | ----------------- | ----------- | -------------- | ----------- | -------- | ------------- | -------------- | -------------- | -------- | ---------------- | 
 | VER-001 | [Pull] | [Pull] | Date | Text | Dropdown | Text | Text | Dropdown | [Formula] | 

**Columns:**

- **Verification ID:** Auto-generated
- **Segment ID:** Reference to Network_Segment_Inventory
- **Test Date:** When was verification performed?
- **Tester:** Who performed the test?
- **Test Method:** Dropdown:
  - Manual Browse Test (attempt to access blocked sites)
  - Automated Scan (security tool)
  - Curl/wget Test (command-line)
  - Browser Extension Test
  - Vendor Verification Tool
  - Penetration Test
  - Other
- **Test Results:** Pass / Fail / Partial / Inconclusive
- **Issues Found:** Description of any problems
- **Status:** ✅ Verified / ❌ Failed / ⚠️ Needs Retest
- **Next Test Date:** [Auto-calculate: Test Date + 90 days]

**Data Rows:** 50 rows for verification tracking

### Test Checklist Template

For each segment, verify:
```
☐ Malicious URL blocked (test with EICAR or known bad domains)
☐ Phishing site blocked (test with PhishTank samples)
☐ Known malware download blocked
☐ HTTPS sites properly filtered (if HTTPS inspection enabled)
☐ Logging working (blocked attempts logged)
☐ Bypass methods ineffective (proxy bypass, VPN bypass, etc.)
☐ User experience acceptable (latency, false positives)
☐ Exemptions working as intended
```

---

## Sheet 8: Evidence_Register

### Purpose
Centralized evidence repository linking to all supporting documentation.

### Header
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document all evidence supporting network coverage assessment"

### Evidence Inventory (Rows 4-103, 100 rows)

 | Evidence ID | Evidence Type | Description | Related Sheet/Row | Location/Path | Date Collected | Collected By | Verification Status | 
 | ------------- | --------------- | ------------- | ------------------- | --------------- | ---------------- | -------------- | ------------------- | 
 | EVD-001 | Dropdown | Text | Text | Text | Date | Text | Dropdown | 

**Evidence Types:**

- Network Diagram
- VLAN Configuration
- Firewall Policy
- VPN Configuration
- WiFi Controller Config
- Cloud Dashboard Screenshot
- NAC Policy
- Exemption Approval
- Test Results
- Monitoring Report
- Change Record
- Other

**Data Rows:** 100 rows

---

## Sheet 9: Approval_Sign_Off

### Purpose
Formal approval workflow for completed assessment.

### Assessment Summary (Rows 3-10)
```
Assessment Document:        ISMS-IMP-A.8.23.2 - Network Coverage
Assessment Period:          [USER INPUT]
Total Segments Assessed:    [Formula from Network_Segment_Inventory]
Fully Protected:            [Formula - 100% coverage segments]
Partially Protected:        [Formula - <100% coverage segments]
Unprotected:                [Formula - 0% coverage segments]
Exempted:                   [Formula from Exemption_Register]
Overall Coverage Score:     [Formula]%
Critical Gaps:              [Formula from Gap_Identification]
Assessment Status:          [Dropdown: Draft/Final/Requires Remediation/Re-assessment]
```

### Completed By (Rows 12-18)

- Name, Role, Department, Email, Date, Signature

### Reviewed By - Network Administrator (Rows 20-26)

- Name, Date, Review Notes, Recommendation

### Reviewed By - Information Security Officer (Rows 28-34)

- Name, Date, Review Notes, Recommendation

### Approved By - CISO (Rows 36-42)

- Name, Date, Approval Decision, Conditions/Notes

### Next Review Details (Rows 44-47)

- Next Review Date: [Auto-calculate +3 months]
- Review Responsible
- Special Considerations

---

## Cell Styling Reference

### Header Styles

- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue)
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (blue)
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (gray)

### Input Cell Styles

- **Fill:** FFFFCC (light yellow)
- **Alignment:** Left/center, wrapped
- **Border:** Thin black on all sides

### Status Fills

- **Protected (✅):** C6EFCE (green)
- **Partial (⚠️):** FFEB9C (yellow)
- **Unprotected (❌):** FFC7CE (red)
- **Planned (🔄):** B4C7E7 (blue)
- **Exempt (🚫):** D9D9D9 (gray)

---

## Freeze Panes

- **Network_Segment_Inventory:** Freeze at A5
- **Coverage_Matrix:** Freeze at A5
- **All other assessment sheets:** Freeze at A5
- **Evidence_Register:** Freeze at A5
- **Approval_Sign_Off:** Freeze at A3

---

## File Naming Convention

**Format:** `ISMS-IMP-A.8.23.2_Network_Coverage_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.8.23.2_Network_Coverage_20260101.xlsx`

---

## Quarterly Review Cycle

1. Review network segment inventory for changes (new VLANs, cloud services, etc.)
2. Re-verify filtering coverage on all segments
3. Update Coverage_Matrix with current status
4. Test filtering effectiveness (Coverage_Verification)
5. Review and renew exemptions (max 12 months)
6. Update gap remediation status
7. Re-calculate overall coverage score
8. Address any new critical gaps
9. Update approval sign-off
10. Coordinate with ISMS-IMP-A.8.23.1 (Infrastructure changes)

---

## Integration Points

### Related Documents

- ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements): Threat Protection Requirements
- ISMS-IMP-A.8.23.1: Filtering Infrastructure Assessment (which solutions are deployed)
- ISMS-IMP-A.8.23.3: Policy Configuration Assessment (which policies apply where)
- ISMS-IMP-A.8.23.5: Compliance Dashboard (pulls coverage data)
- Network Architecture Documentation
- Change Management: Link network changes to coverage updates
- Risk Register: Link coverage gaps to risk IDs

### Audit Trail

- All network segments documented
- Coverage percentages calculated and tracked
- Exemptions formally approved and reviewed
- Verification tests documented
- Evidence maintained for all claims
- Approval sign-off with quarterly reviews

---

**END OF SPECIFICATION**

---

*"Rational behavior is just a small part of game theory. The interesting part is when people deviate from rationality."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->

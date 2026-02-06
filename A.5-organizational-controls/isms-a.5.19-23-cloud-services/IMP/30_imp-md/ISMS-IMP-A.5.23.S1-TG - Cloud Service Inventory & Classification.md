**ISMS-IMP-A.5.23.S1-TG - Cloud Service Inventory & Classification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Cloud Service Inventory & Classification |
| **Related Policy** | ISMS-POL-A.5.19-23-S5 (Cloud Services Security), ISMS-POL-A.5.19-23-S1 (Supplier Relationships) |
| **Purpose** | Maintain authoritative inventory of all cloud services with data classification, criticality assessment, and exit feasibility analysis |
| **Target Audience** | IT Operations, Procurement, Finance, Security Teams, Compliance Officers, Auditors |
| **Assessment Type** | Inventory & Classification |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.23.S1-UG.

---

# Technical Specification

*(This section contains the detailed Excel workbook structure, column specifications, formulas, styling, and integration points - similar to the original ISMS-IMP-A.5.23.S1 technical spec, but updated to reflect the new exit strategy columns for Sheets 4-6)*

## Workbook Structure (10 Sheets)

1. **Instructions & Legend** - Assessment guidance and legend
2. **2. SaaS Services** - Software-as-a-Service inventory
3. **3. IaaS PaaS Services** - Infrastructure and Platform services
4. **4. Cloud Security Services** - Security services (also serves as Exit Feasibility sheet with extended columns R-AC)
5. **5. Cloud Storage Services** - Storage and backup services
6. **6. Data Classification** - What data is processed
7. **7. Service Criticality** - Business impact assessment
8. **8. Summary Dashboard** - Auto-calculated metrics
9. **9. Evidence Register** - Audit trail
10. **10. Approval Sign-Of** - Three-level approval

## Sheet 4: Exit Feasibility - Updated Column Structure

### Extended Columns (R-AC)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| R | Exit Strategy Type | 20 | Dropdown | Cloud-to-Cloud, Hybrid, On-Premises, Not Yet Determined |
| S | Alternative Identified | 22 | Dropdown | Cloud Provider (Name), Hybrid (Cloud+OnPrem), On-Prem Only, Multiple Options, Not Yet Assessed |
| T | Export Format Available | 20 | Dropdown | Standard (CSV/JSON), Proprietary, API Only, None |
| U | Export Tested | 16 | Dropdown | Yes, No, Partial |
| V | Data Volume (GB) | 16 | Number | - |
| W | Migration Complexity | 22 | Dropdown | Cloud-to-Cloud (Low), Cloud-to-Cloud (Medium), Cloud-to-Cloud (High), Hybrid (Medium), Hybrid (High), On-Prem (High), On-Prem (Very High) |
| X | Lock-In Risk | 16 | Dropdown | Low, Medium, High, Critical |
| Y | Hybrid: Workload Segmentation | 25 | Dropdown | Documented, In Progress, Not Applicable |
| Z | Hybrid: Data Sync Latency | 28 | Dropdown | Excellent (<100ms), Acceptable (100-500ms), Concern (>500ms), Not Tested, N/A |
| AA | OnPrem: TCO Analysis Complete | 25 | Dropdown | Yes (Favorable), Yes (Unfavorable), In Progress, Not Started, N/A |
| AB | OnPrem: Infrastructure Available | 25 | Dropdown | Yes (Sufficient), Partial (Upgrade Needed), No (Full Build), Not Assessed, N/A |
| AC | OnPrem: Staffing Plan Documented | 25 | Dropdown | Yes, In Progress, Not Started, N/A |

### Checklist Items (Sheet 4)

**Original 15 items (keep):**
```
☐ Exit strategy documented for Critical/High services
☐ Exit triggers defined
☐ Alternative providers/solutions identified
☐ Alternative provider assessment completed
☐ Migration effort estimated
☐ Data extraction requirements documented
☐ Application dependencies mapped
☐ Integration points documented
☐ Transition timeline template created
☐ Communication plan for exit scenarios
☐ Contract exit clauses reviewed
☐ Notice period requirements documented
☐ Exit plan reviewed annually
☐ Exit plan tested or tabletop exercised
☐ Lessons learned from exits incorporated
```

**NEW 10 items (add):**
```
☐ Exit strategy type selected per policy (Cloud-to-Cloud / Hybrid / On-Prem)
☐ [HYBRID] Workload segmentation documented (cloud vs. on-prem components)
☐ [HYBRID] Hybrid connectivity requirements assessed (VPN, Direct Connect, ExpressRoute)
☐ [HYBRID] Data synchronization requirements documented (latency, consistency)
☐ [HYBRID] Hybrid TCO calculated (3-5 year comparison)
☐ [ON-PREM] Comprehensive TCO analysis completed (CAPEX + 5-year OPEX)
☐ [ON-PREM] Infrastructure capacity planning documented
☐ [ON-PREM] Staffing requirements assessed (4-7 FTE estimate)
☐ [ON-PREM] Technology refresh budget allocated (3-5 year lifecycle)
☐ [ON-PREM] Regulatory justification or cost inversion documented
```

**Total: 25 checklist items**

---

**END OF SPECIFICATION**

---

*"What I cannot create, I do not understand."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->

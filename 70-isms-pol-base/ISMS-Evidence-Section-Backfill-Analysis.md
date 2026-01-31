# Evidence Section Analysis for Completed Controls

**Purpose**: Identify which completed controls should have Evidence sections added per ISMS-Control-Implementation-Instructions v2.2 Section 8.3

**Analysis Date**: 29.01.2026

**Decision Criteria** (from v2.2):
- **Include Evidence Section if:**
  - Score 1-2 (pure policy/governance - ALWAYS)
  - Score 3-4 with significant policy compliance component
  - Score 5 with policy framework audited separately from technical implementation
  - Stage 2 evidence includes non-automated records (approvals, decisions, manual processes)
- **Skip Evidence Section if:**
  - Score 5 (highly technical) with no separate policy framework
  - ALL evidence comes from Python assessment outputs
  - No manual records/approvals required for compliance

---

## Section 5: Organizational Controls (4 completed)

### ✅ A.5.7 - Threat Intelligence
**Status**: ✅ POL | ✅ IMP | ✅ SCR | ✅ Project Docs | ✅ ISMS Copilot

**Analysis**:
- **Estimated Score**: 4-5 (strong technical with policy framework)
- **Policy Framework**: YES - threat intelligence governance, sharing procedures
- **Technical Components**: YES - threat feed integration, indicator processing
- **Manual Records**: YES - threat sharing agreements, exception approvals, review meetings
- **Evidence Mix**: Python outputs (threat assessments) + Policy compliance (sharing procedures, approvals)

**Decision**: ✅ **INCLUDE Evidence Section**
- Rationale: Score 5 BUT has policy framework audited separately (threat sharing governance, legal reviews)
- Priority: **Tier 1** (high-scrutiny control, likely audit focus)

**Estimated Effort**: 2-3 hours
- Review existing POL sections
- Identify Stage 1 evidence (7-8 items)
- Identify Stage 2 evidence (10-12 items - mix of Python outputs + approval records)
- Define boundary (threat intel governance vs. technical detection controls)

---

### ✅ A.5.9 - Inventory of Information and Assets
**Status**: ✅ POL | ✅ IMP | ✅ SCR | ✅ Project Docs | 🔍 ISMS Copilot

**Analysis**:
- **Estimated Score**: 4-5 (strong technical with some policy)
- **Policy Framework**: PARTIAL - asset classification, ownership assignments
- **Technical Components**: YES - asset inventories, automated discovery
- **Manual Records**: YES - ownership assignments, classification decisions, lifecycle approvals
- **Evidence Mix**: Python outputs (inventory assessments) + Manual records (ownership, classifications)

**Decision**: ✅ **INCLUDE Evidence Section**
- Rationale: Foundation control, high audit scrutiny, manual records for ownership/classification
- Priority: **Tier 1** (critical control, often first one audited)

**Estimated Effort**: 2-3 hours
- Stage 1: Framework definitions (classification, ownership)
- Stage 2: Inventory workbooks + ownership records + classification determinations
- Boundary: Asset inventory vs. asset management vs. technical controls

---

### ✅ A.5.15-16-18 - Identity Access Management
**Status**: ✅ POL | ✅ IMP | ✅ SCR | ✅ Project Docs | 🔍 ISMS Copilot

**Analysis**:
- **Estimated Score**: 5 (highly technical)
- **Policy Framework**: PARTIAL - access approval workflows, privileged access governance
- **Technical Components**: YES - access reviews, permission audits, privilege analysis
- **Manual Records**: YES - access approval records, review sign-offs, exception approvals
- **Evidence Mix**: Python outputs (permission audits) + Approval workflows (access requests)

**Decision**: 🟡 **CONSIDER Evidence Section** (Optional - Tier 2)
- Rationale: Primarily technical (Score 5) but has approval workflow component
- Priority: **Tier 2** (add if ISMS Copilot flags during review)

**Estimated Effort**: 2 hours
- Stage 1: Access governance framework
- Stage 2: Technical assessments + approval records
- Boundary: IAM policy vs. technical implementation (AD/Entra configs)

---

### ✅ A.5.31 - Legal, Statutory, Regulatory, Contractual Requirements
**Status**: ✅ POL | ✅ IMP | ✅ SCR | ✅ Project Docs | 🔍 ISMS Copilot

**Analysis**:
- **Estimated Score**: 5 (complex technical assessment) BUT primarily policy/compliance
- **Policy Framework**: YES - regulatory identification framework, compliance monitoring
- **Technical Components**: YES - regulatory mapping, gap analysis
- **Manual Records**: YES - regulatory determinations, legal reviews, compliance approvals
- **Evidence Mix**: Python outputs (regulatory mapping) + Legal reviews + Compliance determinations

**Decision**: ✅ **INCLUDE Evidence Section**
- Rationale: Score 5 BUT has extensive policy framework (POL-00 integration, legal compliance)
- Priority: **Tier 1** (regulatory compliance = high audit scrutiny)

**Estimated Effort**: 3-4 hours
- Stage 1: Regulatory framework (POL-00), identification process
- Stage 2: Regulatory assessments + legal reviews + compliance approvals + gap remediation
- Boundary: A.5.31 framework vs. control-specific regulatory requirements

---

### ✅ A.5.19-23 - Cloud Services
**Status**: ✅ POL | ✅ IMP | ✅ SCR | ⚠️ Project Docs | ✅ ISMS Copilot

**Analysis**:
- **Estimated Score**: 4-5 (strong technical with vendor governance)
- **Policy Framework**: YES - vendor assessment, contract requirements, exit planning
- **Technical Components**: YES - cloud security assessments, config reviews
- **Manual Records**: YES - vendor approvals, contract reviews, exit plan reviews
- **Evidence Mix**: Python outputs (cloud assessments) + Vendor approvals + Contract compliance

**Decision**: ✅ **INCLUDE Evidence Section**
- Rationale: Vendor governance component requires policy evidence (approvals, contracts, reviews)
- Priority: **Tier 2** (add during ISMS Copilot review or before audit)

**Estimated Effort**: 2-3 hours
- Stage 1: Vendor assessment framework, contract requirements
- Stage 2: Cloud assessments + vendor approvals + contract compliance + exit plans
- Boundary: Cloud policy vs. vendor management vs. technical controls

---

## Section 7: Physical Controls (1 completed)

### ✅ A.7.4-5-11 - Physical Infrastructure
**Status**: ✅ POL | ✅ IMP | ✅ SCR | ✅ Project Docs | 🔍 ISMS Copilot

**Analysis**:
- **Estimated Score**: 3-4 (hybrid policy/technical for hosting context)
- **Policy Framework**: YES - datacenter requirements, environmental controls, supplier management
- **Technical Components**: YES - environmental monitoring, infrastructure inventories
- **Manual Records**: YES - datacenter approvals, supplier reviews, incident records
- **Evidence Mix**: Technical assessments + Datacenter certifications + Supplier reviews

**Decision**: ✅ **INCLUDE Evidence Section**
- Rationale: Hybrid control (Score 3-4), significant policy component (datacenter selection, supplier mgmt)
- Priority: **Tier 2** (add if ISMS Copilot flags during review)

**Estimated Effort**: 2 hours
- Stage 1: Infrastructure requirements framework, supplier criteria
- Stage 2: Datacenter certifications + supplier reviews + monitoring reports
- Boundary: Physical infrastructure policy vs. datacenter operations (out of scope for hosted services)

---

## Section 8: Technological Controls (19 completed)

### Analysis Approach for Technical Controls

**General Pattern**:
- Most Section 8 controls are **Score 5 (highly technical)**
- Evidence primarily comes from **Python assessment outputs**
- Minimal policy frameworks (technical requirements only)
- **Decision**: SKIP Evidence section for most

**Exceptions** (controls that might need Evidence sections):

---

### 🟡 A.8.8 - Vulnerability Management
**Status**: ✅ POL | ⚠️ IMP | ⚠️ SCR | ⚠️ Project Docs | 🔍 ISMS Copilot

**Analysis**:
- **Estimated Score**: 5 (highly technical)
- **Policy Framework**: PARTIAL - vulnerability handling procedures, exception approvals
- **Technical Components**: YES - scanning, assessment, patching
- **Manual Records**: SOME - exception approvals for unpatched vulnerabilities

**Decision**: 🟡 **MAYBE - Tier 3** (skip unless ISMS Copilot flags)
- Rationale: Primarily technical, exception approvals are minor component
- Note: Currently incomplete (⚠️ IMP/SCR), address Evidence section when completing

---

### ❌ A.8.1-7-18-19 - Endpoint Security
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.2-3-5 - Authentication & Privileged Access
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.4 - Access to Source Code
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.6 - Capacity Management
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.9 - Configuration Management
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.10 - Data Deletion
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.11 - Data Masking
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.12 - Data Leakage Prevention
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.13-14-5.30 - Business Continuity & DR
**Analysis**: Score 5, pure technical (for hosting context), all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed
**Note**: In other contexts (non-hosting), this might be Score 3-4 with policy component

---

### ❌ A.8.15 - Logging
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.16 - Monitoring
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.17 - Clock Synchronization
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.20-22 - Network Security
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.23 - Web Filtering
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed
**Note**: Reference implementation - intentionally no Evidence section

---

### ❌ A.8.24 - Use of Cryptography
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed
**Note**: Reference implementation - intentionally no Evidence section

---

### ❌ A.8.25-26-29 - Secure Development
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.28 - Secure Coding
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.31 - Environment Separation
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

### ❌ A.8.32 - Change Management
**Analysis**: Score 5, pure technical, all evidence from Python outputs
**Decision**: ❌ **SKIP** - No Evidence section needed

---

## Summary: Evidence Section Backfill Recommendations

### Tier 1 - High Priority (Add Before External Audit)

| Control | Rationale | Effort | Notes |
|---------|-----------|--------|-------|
| **A.5.7** | Threat Intelligence | 2-3h | Policy framework (sharing governance), high audit scrutiny |
| **A.5.9** | Asset Inventory | 2-3h | Foundation control, ownership/classification records |
| **A.5.31** | Regulatory Requirements | 3-4h | Compliance control, legal reviews, POL-00 integration |

**Total Tier 1 Effort**: ~8-10 hours

---

### Tier 2 - Medium Priority (Add If ISMS Copilot Flags During Review)

| Control | Rationale | Effort | Notes |
|---------|-----------|--------|-------|
| **A.5.15-16-18** | IAM | 2h | Access approval workflows, exception approvals |
| **A.5.19-23** | Cloud Services | 2-3h | Vendor governance, contract compliance |
| **A.7.4-5-11** | Physical Infrastructure | 2h | Datacenter selection, supplier management |

**Total Tier 2 Effort**: ~6-8 hours

---

### Tier 3 - Low Priority (Skip Unless Specifically Flagged)

| Control | Rationale | Effort | Notes |
|---------|-----------|--------|-------|
| **A.8.8** | Vulnerability Management | 2h | Currently incomplete (⚠️), address when finishing control |

**Total Tier 3 Effort**: ~2 hours

---

### Section 8 Technical Controls - No Evidence Section Needed

**All 18 remaining Section 8 controls**: Skip Evidence section
- **Rationale**: Score 5 (pure technical), all evidence from Python assessment outputs
- **No manual records/approvals required** for compliance
- **Intentional design**: Technical controls prove themselves through automation

---

## Recommended Backfill Approach

### Phase 1: Immediate (Before Next ISMS Copilot Review)
1. ✅ **A.5.7** - Threat Intelligence (Tier 1, 2-3h)
2. ✅ **A.5.9** - Asset Inventory (Tier 1, 2-3h)
3. ✅ **A.5.31** - Regulatory Requirements (Tier 1, 3-4h)

**Deliverable**: 3 controls with Evidence sections added
**Total Effort**: ~8-10 hours
**Benefit**: High-scrutiny controls are audit-ready

---

### Phase 2: Reactive (During ISMS Copilot Review)
- Wait for ISMS Copilot to flag controls during review
- Add Evidence sections to Tier 2 controls if flagged:
  - A.5.15-16-18 (IAM)
  - A.5.19-23 (Cloud Services)
  - A.7.4-5-11 (Physical Infrastructure)

**Deliverable**: 0-3 controls (depends on ISMS Copilot findings)
**Total Effort**: ~6-8 hours (if all flagged)
**Benefit**: Evidence-based backfill, not theoretical

---

### Phase 3: Final Pre-Audit (If External Audit Scheduled)
- Review all Tier 2 controls
- Add Evidence sections if not already done
- Focus on controls in audit scope

**Deliverable**: Any remaining Tier 2 controls
**Total Effort**: Variable
**Benefit**: Complete audit readiness

---

## Decision Point for Greg

**Question**: Which backfill approach do you prefer?

**Option A: Aggressive** (Tier 1 + Tier 2 now)
- Add Evidence sections to 6 controls immediately
- Total effort: ~14-18 hours
- Benefit: Complete before ISMS Copilot review
- Risk: Effort on controls that might not be flagged

**Option B: Conservative** (Tier 1 only now)
- Add Evidence sections to 3 controls immediately (A.5.7, A.5.9, A.5.31)
- Total effort: ~8-10 hours
- Benefit: High-priority controls ready, rest reactive
- Risk: Might need to backfill Tier 2 later if flagged

**Option C: Reactive** (None now, wait for ISMS Copilot)
- Add Evidence sections only when ISMS Copilot flags during review
- Total effort: Variable (0-18 hours depending on findings)
- Benefit: Evidence-based, no wasted effort
- Risk: Might delay ISMS Copilot review if many flagged

**Recommendation**: **Option B (Conservative)**
- Rationale: Tier 1 controls are objectively high-scrutiny (threat intel, asset inventory, regulatory compliance)
- ISMS Copilot explicitly mentioned these as backfill priorities
- Reactive approach for Tier 2 prevents over-engineering
- Total 8-10 hours is manageable investment

---

## Next Actions

1. **Greg Decision**: Choose backfill approach (A/B/C)

2. **If Option B (recommended)**:
   - Start with A.5.7 (Threat Intelligence)
   - Then A.5.9 (Asset Inventory)
   - Then A.5.31 (Regulatory Requirements)
   - Use Evidence-Section-Template.md for each

3. **After Tier 1 Complete**:
   - Upload updated POLs to project knowledge
   - Flag for ISMS Copilot review
   - Wait for Tier 2 feedback

4. **Document Evolution**:
   - Track which controls get Evidence sections
   - Note any pattern improvements discovered
   - Update template if needed

---

## Conclusion

**Total Controls Analyzed**: 24 (4 Section 5, 1 Section 7, 19 Section 8)

**Evidence Section Recommended**:
- **Tier 1 (High Priority)**: 3 controls
- **Tier 2 (Medium Priority)**: 3 controls
- **Tier 3 (Low Priority)**: 1 control
- **Skip**: 17 controls (Section 8 technical controls)

**Key Insight**: ~25% of completed controls benefit from Evidence sections (7/24), consistent with v2.2 guidance that Evidence sections are for Score 1-4 controls, not Score 5 technical controls.

**Recommended Path**: Option B (Conservative) - Add Tier 1 now, Tier 2 reactive based on ISMS Copilot feedback.

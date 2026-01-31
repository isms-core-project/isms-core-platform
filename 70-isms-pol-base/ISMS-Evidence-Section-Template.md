# Evidence Section Template for ISMS Policy Documents

**Purpose**: Use this template when adding Evidence sections to Score 1-4 controls per ISMS-Control-Implementation-Instructions v2.2 Section 8.3.

**When to Use**: See decision tree in v2.2 instructions (Score 1-2 ALWAYS, Score 3-4 often, Score 5 sometimes)

**Placement**: At end of POL document, before any Annexes

---

## Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:
- ✅ This policy document (ISMS-POL-A.X.XX v1.0)
- ✅ Approval signatures from [CISO / Executive Management / relevant stakeholders]
- ✅ [Key framework/process] defined (Section X.X)
- ✅ [Requirements/activities/controls] documented (Section X.X)
- ✅ [Specific requirement category] specified (Section X.X)
- ✅ Roles and responsibilities assigned (Section X)
- ✅ Governance and review procedures defined (Section X)
- ✅ Integration with related controls documented (Section X.X)

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:
- [Specific operational records - be concrete, not generic]
- [Assessment/review documentation with dates and approvers]
- [Registers/inventories relevant to this control]
- [Test results/validation evidence if applicable]
- [Approval records showing governance in action]
- [Metrics/dashboards showing compliance trends over time]
- [Exception/deviation tracking if applicable]
- [Training completion records if applicable]
- [Incident/audit findings and remediation if applicable]
- [Handover/transition documentation if applicable]
- [Sample outputs from assessment workbooks - if technical component exists]

**Clarification on Compliance Evidence:**

This policy establishes [what this policy does - concise statement]. It does NOT establish:
- **[Related concern 1]** (addressed in [related policy or organizational process])
- **[Related concern 2]** (addressed in [related policy or organizational process])
- **[Related concern 3]** (organizational decision, not ISMS policy requirement)

The boundary is: [one sentence explaining policy scope vs. what's excluded].

---

## Customization Guidance

### Stage 1 Evidence - Customization Points

**Always include:**
1. Policy document reference
2. Approval signatures
3. Framework/process definitions (reference actual POL sections)
4. Roles and responsibilities
5. Governance procedures
6. Integration with related controls

**Control-specific items to add:**
- Classification frameworks (if control involves classification)
- Requirement categories (if control has multiple requirement types)
- Decision matrices (if control has decision frameworks)
- Procedures (if control defines specific procedures)

**Example customizations:**

**For Project Management (A.5.8):**
- ✅ Project classification framework defined (Section 2.2)
- ✅ Security activities by phase documented (Section 2.3)
- ✅ Security requirements categories specified (Section 2.4)

**For Training (A.6.3):**
- ✅ Training curriculum framework defined (Section 2.1)
- ✅ Role-based training requirements documented (Section 2.2)
- ✅ Competency assessment criteria specified (Section 2.3)

**For Incident Management (A.5.24-28):**
- ✅ Incident classification framework defined (Section 2.1)
- ✅ Incident response procedures documented (Section 2.3)
- ✅ Escalation criteria specified (Section 2.4)

### Stage 2 Evidence - Customization Points

**Principles:**
- Be specific, not generic ("project classification approvals" not "compliance records")
- Include both ongoing evidence (metrics, dashboards) and point-in-time evidence (approvals)
- Reference actual artifacts (workbooks, registers, meeting minutes, reports)
- Cover full lifecycle of the control area

**Control-specific evidence types:**

**Policy/Governance Controls (Score 1-2):**
- Approval records
- Decision documentation
- Review meeting minutes
- Exception registers
- Audit findings

**Hybrid Controls (Score 3-4):**
- Assessment workbooks (from IMP procedures)
- Compliance registers
- Test results
- Metrics dashboards
- Training records
- Review documentation

**Technical Controls with Policy Framework (Score 5):**
- Technical assessment outputs (Python/Excel)
- Policy compliance records
- Exception approvals
- Review documentation

**Example customizations:**

**For Training (A.6.3):**
- Training completion records (by role, by individual)
- Training effectiveness assessments (test scores, feedback)
- Annual training refresh completion rates
- Security culture survey results
- Training exception register (deferrals, exemptions)

**For Incident Management (A.5.24-28):**
- Incident register (all incidents logged with classifications)
- Incident response timelines (detection → containment → resolution)
- Escalation records (who notified, when)
- Post-incident review reports (lessons learned)
- Incident trend analysis (monthly/quarterly)
- Security improvement actions from incidents
- Tabletop exercise results

**For Asset Inventory (A.5.9):**
- Asset inventory assessments (from ISMS-IMP-A.5.9 workbooks)
- Asset classification determinations
- Asset ownership assignments
- Asset lifecycle records (acquisition → disposal)
- Inventory reconciliation reports
- Exception register (unclassified/unowned assets)

### Boundary Clarification - Customization Points

**Structure:**
1. Positive statement: "This policy establishes [X]"
2. Negative statements: 2-4 things it does NOT establish
3. Where excluded concerns ARE addressed
4. One-sentence summary of boundary

**Common patterns:**

**For Governance/Process Controls:**
```
This policy establishes [governance process/framework].
Does NOT establish:
- Specific technical controls (addressed in A.8.XX technical policies)
- Organizational structure (organizational decision)
- General requirements (addressed in other Annex A controls)
```

**For Technical Controls with Policy Framework:**
```
This policy establishes [technical requirements + policy framework].
Does NOT establish:
- Implementation details (addressed in IMP specifications)
- Tool-specific configurations (organizational choice)
- Related control requirements (addressed in A.X.XX policies)
```

**Examples:**

**For Training (A.6.3):**
```
This policy establishes security awareness and training requirements.
Does NOT establish:
- Specific training content (developed by training team based on risk assessment)
- HR onboarding processes (organizational HR policy)
- General competency requirements (covered in job descriptions)
Boundary: Training policy defines WHO needs WHAT training WHEN → Training team develops content → HR manages delivery logistics
```

**For Incident Management (A.5.24-28):**
```
This policy establishes incident management process.
Does NOT establish:
- Technical detection controls (covered in A.8.16 Monitoring)
- Technical response controls (covered in A.8.X technical controls)
- Business continuity procedures (covered in A.5.29-30)
Boundary: Incident policy defines PROCESS for managing incidents → Technical controls provide DETECTION/RESPONSE capabilities → BC/DR handles RECOVERY
```

---

## Quality Checklist

Before finalizing Evidence section, verify:

**Stage 1 Evidence:**
- [ ] All 7-9 items present (policy, approvals, frameworks, roles, governance, integration)
- [ ] References specific POL sections (not "appropriate documentation")
- [ ] Control-specific items added (frameworks, requirements, procedures)

**Stage 2 Evidence:**
- [ ] 8-12 specific evidence items listed
- [ ] Mix of ongoing (metrics) and point-in-time (approvals) evidence
- [ ] Specific artifact names (not generic "compliance records")
- [ ] Covers full control lifecycle
- [ ] Includes assessment workbook outputs (if technical component)

**Boundary Clarification:**
- [ ] Positive statement of what policy establishes
- [ ] 2-4 negative statements of what it doesn't establish
- [ ] References where excluded concerns are addressed
- [ ] One-sentence summary of boundary

**Integration with IMP:**
- [ ] No duplication (POL = WHAT evidence, IMP = HOW to collect)
- [ ] Complementary abstraction levels
- [ ] Stage 2 evidence aligns with IMP assessment procedures

---

## Reference Implementation

See **ISMS-A.5.8-Information-Security-in-Project-Management** POL document for working example of this pattern.

---

## Version History

- **v1.0** (29.01.2026): Initial template based on A.5.8 Evidence section pattern

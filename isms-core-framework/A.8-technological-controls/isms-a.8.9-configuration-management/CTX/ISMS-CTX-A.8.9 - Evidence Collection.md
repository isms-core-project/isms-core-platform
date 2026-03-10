<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.9-evidence-collection:framework:CTX:a.8.9 -->
**ISMS-CTX-A.8.9 — Evidence Collection**

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-CTX-A.8.9-evidence-collection |
| **Version** | 1.0 |
| **Document Type** | Technical Reference (NOT ISMS) |
| **Related Policy** | ISMS-POL-A.8.9 (All Sections) |
| **Purpose** | Provide standardized evidence repository structure for ISO 27001:2022 Control A.8.9 compliance demonstration and audit preparation |
| **Target Audience** | Configuration Managers, System Administrators, Auditors, Compliance Officers, Evidence Custodians |
| **Review Cycle** | Annual (or upon audit requirements change) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial evidence collection guidance (NOT ISMS) | ISMS Implementation Team |

### Approvers

- Primary: Configuration Manager
- Technical Review: Security Architect
- NO Executive Approval Required (NOT ISMS)

### Distribution

Configuration management team, system administrators, IT operations, security engineers, compliance officers, internal auditors, external auditors

### Related Documents

- ISMS-POL-A.8.9: Configuration Management Policy (Consolidated)
- ISMS-CTX-A.8.9: Configuration Management Reference (NOT ISMS)
- ISMS-IMP-A.8.9-UG: Configuration Management Implementation Guide (User)
- ISMS-IMP-A.8.9-TG: Configuration Management Implementation Guide (Technical)

---

## ⚠️ CRITICAL: Document Status

**THIS DOCUMENT IS NOT PART OF THE ISMS.**

**THIS DOCUMENT DOES NOT DEFINE MANDATORY REQUIREMENTS.**

**THIS DOCUMENT DOES NOT ESTABLISH BINDING OBLIGATIONS.**

**ALL BINDING REQUIREMENTS ARE DEFINED IN ISMS-POL-A.8.9.**

**This is technical reference and operational guidance for evidence collection, organisation, and audit preparation only.**

**Purpose**: Provide practical guidance for organising evidence to demonstrate Control A.8.9 compliance during ISO 27001:2022 audits. This document supplements ISMS-POL-A.8.9 and ISMS-IMP-A.8.9 but does NOT replace policy requirements.

**Audience**: Evidence custodians, audit coordinators, configuration managers responsible for preparing audit evidence packages.

**Usage**: Reference for establishing evidence repository structure, naming conventions, retention policies, and audit preparation workflows. Organisations customize this content to their specific document management systems and audit requirements.

**Updates**: This document may be updated more frequently than ISMS policies to reflect evolving audit practices, document management tools, and compliance requirements. Updates do not require executive approval but must be communicated to affected personnel.

---

## Overview

This guide defines the standardized evidence repository structure for ISO 27001:2022 Control A.8.9 (Configuration Management). Proper evidence organisation enables efficient audits, demonstrates control effectiveness, and supports compliance verification.

**Repository Location**: [Organisation to define - e.g., SharePoint/Network Drive/Document Management System]

**Access Control**: Evidence repository SHALL be access-controlled with read access for auditors and compliance officers, write access restricted to Configuration Management team.

**Retention Period**: Minimum 3 years per ISO 27001:2022 requirements; longer if required by sector-specific regulations.

---

## Root Evidence Structure

```
Evidence/
  ISMS-A.8.9-Baseline-Configuration/
  ISMS-A.8.9-Change-Control/
  ISMS-A.8.9-Configuration-Monitoring/
  ISMS-A.8.9-Security-Hardening/
```

---

## Baseline Configuration Evidence

**Assessment File**: ISMS-IMP-A.8.9.xlsx (generated from Python script)

### Directory Structure

**Evidence/ISMS-A.8.9-Baseline-Configuration/**

#### 1. Asset-Inventory/
Contains complete asset inventory demonstrating scope of baseline coverage.

**Required Files**:

- `CMDB-Export-YYYYMMDD.xlsx` - Complete Configuration Management Database export
- `Network-Scan-Results-YYYYMMDD.pdf` - Network discovery scan results
- `Asset-Criticality-Classifications.pdf` - Asset tier classifications (Tier 1-4)
- `Cloud-Asset-Inventory-AWS-YYYYMMDD.csv` - AWS asset inventory
- `Cloud-Asset-Inventory-Azure-YYYYMMDD.csv` - Azure asset inventory
- `Asset-Inventory-Reconciliation-Report.xlsx` - Comparison of multiple sources

**Evidence Purpose**: Demonstrates complete asset inventory exists and baseline coverage targets are measurable.

#### 2. Baseline-Documentation/
Contains approved baseline configurations organised by asset type.

**Sub-directories**:

**Windows-Server/**

- `BL-WIN2022-DC-v2.1.docx` - Windows Server 2022 Domain Controller baseline
- `BL-WIN2022-FS-v1.5.docx` - Windows Server 2022 File Server baseline
- `BL-WIN2022-APP-v1.8.docx` - Windows Server 2022 Application Server baseline
- `CIS-Windows-Server-2022-Mapping.xlsx` - CIS Benchmark mapping

**Linux-Unix/**

- `BL-RHEL9-STD-v1.3.pdf` - Red Hat Enterprise Linux 9 baseline
- `BL-UBUNTU2204-WEB-v2.0.pdf` - Ubuntu 22.04 Web Server baseline
- `BL-SUSE15-DB-v1.2.pdf` - SUSE Linux 15 Database Server baseline
- `CIS-Linux-Benchmark-Mapping.xlsx` - CIS Benchmark mapping

**Network-Devices/**

- `BL-Cisco-ASA-FW-v3.1.pdf` - Cisco ASA Firewall baseline
- `BL-Palo-Alto-NGFW-v2.5.pdf` - Palo Alto Next-Gen Firewall baseline
- `BL-Cisco-Switch-IOS-v1.9.pdf` - Cisco Switch IOS baseline
- `BL-F5-LoadBalancer-v1.4.pdf` - F5 Load Balancer baseline

**Cloud-Platforms/**

- `BL-AWS-EC2-Linux-v2.2.pdf` - AWS EC2 Linux instance baseline
- `BL-AWS-RDS-MySQL-v1.6.pdf` - AWS RDS MySQL baseline
- `BL-Azure-VM-Windows-v1.8.pdf` - Azure Windows VM baseline
- `CIS-AWS-Foundations-Benchmark-Mapping.xlsx` - CIS AWS mapping

**Databases/**

- `BL-SQLServer2022-v1.7.pdf` - SQL Server 2022 baseline
- `BL-PostgreSQL15-v1.4.pdf` - PostgreSQL 15 baseline
- `BL-Oracle19c-v2.1.pdf` - Oracle 19c baseline
- `DISA-STIG-Database-Mapping.xlsx` - DISA STIG mapping

**Containers/**

- `BL-Docker-v1.5.pdf` - Docker baseline
- `BL-Kubernetes-v2.0.pdf` - Kubernetes baseline
- `CIS-Kubernetes-Benchmark-Mapping.xlsx` - CIS Kubernetes mapping

**Naming Convention**: `BL-[Technology]-[Role]-v[Version].pdf`

- BL = Baseline
- Technology = Product/Platform (WIN2022, RHEL9, etc.)
- Role = Purpose (DC, WEB, APP, DB, etc.)
- Version = Semantic versioning (major.minor)

**Evidence Purpose**: Demonstrates baselines exist, are documented, and reference recognized standards.

#### 3. Golden-Images/
Contains golden image inventory and approval records.

**Required Files**:

- `Image-Inventory-Register.xlsx` - Master list of all golden images
- `WIN2022-STD-v2.1-20240115-ApprovalRecord.pdf` - Image approval with signatures
- `RHEL9-SEC-v1.3-20240120-ApprovalRecord.pdf` - Image approval with signatures

**Image-Build-Manifests/** (IaC code for reproducible builds):

- `WIN2022-STD-v2.1-BuildManifest.yaml` - Automated build definition
- `RHEL9-SEC-v1.3-BuildManifest.yaml` - Automated build definition

**Vulnerability-Scans/** (pre-approval security validation):

- `WIN2022-STD-v2.1-VulnScan-YYYYMMDD.pdf` - Vulnerability scan report
- `RHEL9-SEC-v1.3-VulnScan-YYYYMMDD.pdf` - Vulnerability scan report

**Evidence Purpose**: Demonstrates golden images implement baselines and are security-validated before production use.

#### 4. Approval-Records/
Contains formal approvals for baselines.

**Required Files**:

- `Baseline-Approval-Matrix.xlsx` - Master tracking of all baseline approvals
- `CAB-Meeting-Minutes-YYYYMMDD.pdf` - CAB meetings where baselines approved
- `Email-Approval-BL-WIN2022-DC-v2.1.pdf` - Email approval chains
- `CISO-Approval-Baseline-Security-Standards.pdf` - Executive approval

**Evidence Purpose**: Demonstrates baselines have proper authorisation and governance oversight.

#### 5. Configuration-Snapshots/
Contains actual configuration exports demonstrating baseline compliance.

**Required Files**:

- `Server-Config-WebServer01-YYYYMMDD.txt` - Actual server configuration
- `Firewall-Rules-Export-YYYYMMDD.xml` - Firewall configuration export
- `Database-Config-DBSERVER01-YYYYMMDD.sql` - Database configuration
- `Kubernetes-Manifest-Export-YYYYMMDD.yaml` - K8s configuration

**Evidence Purpose**: Demonstrates deployed configurations match approved baselines.

#### 6. Deviation-Documentation/
Contains approved exceptions to baselines.

**Required Files**:

- `Deviation-Register.xlsx` - Master list of all approved deviations
- `Deviation-Request-DEV-2024-001.pdf` - Deviation request with business justification
- `Risk-Assessment-DEV-2024-001.pdf` - Risk analysis for deviation
- `Compensating-Controls-DEV-2024-001.pdf` - Mitigating controls documentation
- `CISO-Approval-DEV-2024-001.pdf` - Executive approval

**Naming Convention**: `DEV-YYYY-###` where ### is sequential number.

**Evidence Purpose**: Demonstrates deviations are formally managed with risk assessment and approval.

#### 7. Assessment-Reports/
Contains completed assessment workbooks and summary reports.

**Required Files**:

- `Baseline-Assessment-YYYYMMDD.xlsx` - Completed ISMS-IMP-A.8.9 workbook
- `Assessment-Summary-Presentation.pptx` - Executive summary
- `Evidence-Register-Index.pdf` - Index of all evidence collected
- `Gap-Remediation-Plan.xlsx` - Action plan for identified gaps

**Evidence Purpose**: Demonstrates regular assessment of baseline compliance and gap remediation.

---

## Change Control Evidence

**Assessment File**: ISMS-IMP-A.8.9.xlsx (generated from Python script)

### Directory Structure

**Evidence/ISMS-A.8.9-Change-Control/**

#### 1. Change-Requests/
Contains all change request documentation.

**Sub-directories by Year-Quarter**:

- `2024-Q1/` - All Q1 2024 changes
- `2024-Q2/` - All Q2 2024 changes
- etc.

**Per Change**:

- `CR-2024-001-Change-Request-Form.pdf` - Completed change request
- `CR-2024-001-Risk-Assessment.pdf` - Risk analysis
- `CR-2024-001-Testing-Results.pdf` - Test validation
- `CR-2024-001-Implementation-Log.pdf` - Actual implementation steps
- `CR-2024-001-Post-Implementation-Review.pdf` - PIR within 5 days

**Naming Convention**: `CR-YYYY-###` where ### is sequential number.

#### 2. CAB-Records/
Contains Change Advisory Board meeting documentation.

**Required Files**:

- `CAB-Meeting-Schedule-2024.pdf` - Published CAB schedule
- `CAB-Membership-Roster.pdf` - Current CAB members and roles
- `CAB-Charter.pdf` - CAB authority and responsibilities
- `CAB-Meeting-Minutes-20240115.pdf` - Meeting minutes with decisions
- `CAB-Meeting-Minutes-20240122.pdf` - Meeting minutes with decisions
- `CAB-Attendance-Log-2024.xlsx` - Attendance tracking for quorum verification

**Evidence Purpose**: Demonstrates CAB operates regularly with proper governance.

#### 3. Approval-Workflows/
Contains approval chains for different change types.

**Required Files**:

- `Approval-Workflow-Diagram.pdf` - Visual representation of approval tiers
- `Standard-Change-Catalog.xlsx` - Pre-approved standard changes
- `Emergency-Change-Log.xlsx` - All emergency changes with retrospective reviews
- `Approval-Authority-Matrix.pdf` - Who can approve what

#### 4. Testing-Validation/
Contains test plans and results.

**Per High-Risk Change**:

- `TEST-CR-2024-001-TestPlan.pdf` - Formal test plan
- `TEST-CR-2024-001-TestResults.xlsx` - Detailed test results
- `TEST-CR-2024-001-Screenshots.pdf` - Visual evidence
- `TEST-CR-2024-001-RollbackTest.pdf` - Rollback procedure validation

#### 5. Change-Success-Metrics/
Contains change management KPI reports.

**Required Files** (Monthly/Quarterly):

- `Change-Metrics-Dashboard-202401.pdf` - Monthly metrics report
- `Change-Success-Rate-Trend-Analysis.xlsx` - Historical tracking
- `Emergency-Change-Analysis-Q1-2024.pdf` - Emergency change justification review
- `Failed-Change-Root-Cause-Analysis.pdf` - Analysis of rollbacks

**Evidence Purpose**: Demonstrates change management effectiveness and continuous improvement.

#### 6. Assessment-Reports/

- `Change-Control-Assessment-YYYYMMDD.xlsx` - Completed ISMS-IMP-A.8.9 workbook
- `Assessment-Summary-Presentation.pptx` - Executive summary
- `Evidence-Register-Index.pdf` - Evidence collected

---

## Configuration Monitoring Evidence

**Assessment File**: ISMS-IMP-A.8.9.xlsx (generated from Python script)

### Directory Structure

**Evidence/ISMS-A.8.9-Configuration-Monitoring/**

#### 1. Monitoring-Infrastructure/
Contains monitoring tool deployment evidence.

**Required Files**:

- `Monitoring-Tool-Inventory.xlsx` - All deployed monitoring tools
- `Monitoring-Architecture-Diagram.pdf` - How monitoring is deployed
- `Monitoring-Coverage-Report.xlsx` - Asset coverage by tier
- `Monitoring-Agent-Deployment-Status.xlsx` - Agent installation tracking

#### 2. Drift-Alerts/
Contains drift detection alerts and remediation.

**Sub-directories by Severity**:

- `Critical-Drift/` - Critical security control changes
- `High-Drift/` - High severity changes
- `Medium-Drift/` - Medium severity changes
- `Low-Drift/` - Low severity informational changes

**Per Drift Incident**:

- `DRIFT-2024-001-Alert.pdf` - Original alert with details
- `DRIFT-2024-001-Investigation.pdf` - Root cause investigation
- `DRIFT-2024-001-Remediation.pdf` - Remediation actions taken
- `DRIFT-2024-001-Closure.pdf` - Incident closure with verification

**Naming Convention**: `DRIFT-YYYY-###`

#### 3. Baseline-Comparison-Reports/
Contains regular baseline compliance scans.

**Required Files** (Monthly minimum for Tier 1, Quarterly for Tier 2):

- `Baseline-Compliance-Scan-202401-Tier1.pdf` - Tier 1 assets compliance
- `Baseline-Compliance-Scan-202401-Tier2.pdf` - Tier 2 assets compliance
- `Drift-Trend-Analysis-Q1-2024.xlsx` - Trending analysis

#### 4. Remediation-Tracking/
Contains drift remediation action tracking.

**Required Files**:

- `Drift-Remediation-Register.xlsx` - All open/closed drift incidents
- `SLA-Compliance-Report.xlsx` - Remediation SLA adherence
- `Recurring-Drift-Analysis.pdf` - Root cause analysis for repeated drift

#### 5. Monitoring-Performance/
Contains monitoring tool health and reliability evidence.

**Required Files**:

- `Monitoring-Tool-Uptime-Report.xlsx` - Tool availability metrics
- `Alert-False-Positive-Rate.xlsx` - Alert tuning effectiveness
- `Monitoring-Incident-Log.xlsx` - Monitoring system failures

#### 6. Assessment-Reports/

- `Monitoring-Assessment-YYYYMMDD.xlsx` - Completed ISMS-IMP-A.8.9 workbook
- `Assessment-Summary-Presentation.pptx` - Executive summary
- `Evidence-Register-Index.pdf` - Evidence collected

---

## Security Hardening Evidence

**Assessment File**: ISMS-IMP-A.8.9.xlsx (generated from Python script)

### Directory Structure

**Evidence/ISMS-A.8.9-Security-Hardening/**

#### 1. Hardening-Standards/
Contains hardening standard documentation.

**Required Files**:

- `Hardening-Standards-Register.xlsx` - All applicable standards mapped to assets
- `CIS-Benchmarks-Library/` - Downloaded CIS Benchmark PDFs
- `DISA-STIG-Library/` - Downloaded STIG files
- `Vendor-Security-Guides/` - Vendor hardening documentation
- `Standard-Selection-Rationale.pdf` - Why each standard was chosen

#### 2. Compliance-Scans/
Contains automated hardening compliance scans.

**Sub-directories by Asset Type**:

- `Windows-Servers/`
- `Linux-Servers/`
- `Network-Devices/`
- `Databases/`
- `Cloud-Platforms/`

**Per Asset Type (Quarterly minimum)**:

- `CIS-Scan-WIN2022-202401.pdf` - Compliance scan results
- `CIS-Scan-RHEL9-202401.pdf` - Compliance scan results
- `Compliance-Trend-Analysis-Q1-2024.xlsx` - Historical tracking

#### 3. Gap-Analysis/
Contains identified hardening gaps and remediation plans.

**Required Files**:

- `Hardening-Gap-Register.xlsx` - All identified gaps
- `Critical-Gap-Remediation-Plan.xlsx` - Action plan for critical gaps
- `Gap-Risk-Assessment.pdf` - Risk analysis for gaps
- `Remediation-Status-Dashboard.xlsx` - Progress tracking

#### 4. Hardening-Exceptions/
Contains approved exceptions to hardening standards.

**Per Exception**:

- `HARD-EX-2024-001-Exception-Request.pdf` - Formal exception request
- `HARD-EX-2024-001-Risk-Assessment.pdf` - Risk analysis
- `HARD-EX-2024-001-Compensating-Controls.pdf` - Mitigation measures
- `HARD-EX-2024-001-Approval.pdf` - CISO/Security Architect approval

**Naming Convention**: `HARD-EX-YYYY-###`

#### 5. Hardening-Implementation/
Contains evidence of hardening implementation.

**Required Files**:

- `Pre-Hardening-Scans/` - Baseline before hardening
- `Post-Hardening-Scans/` - Validation after hardening
- `Hardening-Scripts/` - Automated hardening scripts
- `Implementation-Logs/` - Audit trail of hardening changes

#### 6. Compliance-Reports/
Contains regular compliance reporting.

**Required Files** (Quarterly):

- `Hardening-Compliance-Dashboard-Q1-2024.pdf` - Executive dashboard
- `Compliance-by-Asset-Tier-Q1-2024.xlsx` - Tier-based compliance
- `Critical-Controls-Compliance-Report.xlsx` - Focus on critical controls
- `Year-over-Year-Improvement-Analysis.pdf` - Maturity progression

#### 7. Assessment-Reports/

- `Hardening-Assessment-YYYYMMDD.xlsx` - Completed ISMS-IMP-A.8.9 workbook
- `Assessment-Summary-Presentation.pptx` - Executive summary
- `Evidence-Register-Index.pdf` - Evidence collected

---

## Evidence Collection Best Practices

### Naming Conventions Summary

**General Format**: `[Type]-[Date/ID]-[Description].[ext]`

**Examples**:

- Assessment workbooks: `Baseline-Assessment-20240315.xlsx`
- Change requests: `CR-2024-042-Firewall-Rule-Update.pdf`
- Drift incidents: `DRIFT-2024-018-Unauthorised-Service-Start.pdf`
- Exceptions: `HARD-EX-2024-005-Legacy-App-Exception.pdf`
- CAB minutes: `CAB-Meeting-Minutes-20240315.pdf`

### Date Format Standards

**All dates in filenames**: YYYYMMDD format (ISO 8601)

- Correct: `20240315`
- Incorrect: `03-15-2024`, `15.03.2024`

**Rationale**: Ensures alphabetical sorting = chronological sorting

### File Format Standards

**Preferred Formats**:

- **Formal documents**: PDF/A (archival format)
- **Spreadsheets**: XLSX (Excel) or CSV (for data interchange)
- **Configuration exports**: Native format (XML, JSON, YAML, TXT)
- **Diagrams**: PDF (from Visio/draw.io), PNG (if interactive not needed)

**Avoid**:

- Proprietary formats without free viewers
- Password-protected files (use repository access control instead)
- Compressed archives (store uncompressed for indexing)

### Evidence Retention Rules

| Evidence Type | Retention Period | Rationale |
|---------------|------------------|-----------|
| Assessment workbooks | 3 years minimum | ISO 27001 requirement |
| Change requests | 3 years minimum | Audit trail requirement |
| Drift incidents | 3 years minimum | Security incident tracking |
| Approval records | 7 years | Legal/compliance requirement |
| Configuration snapshots | 1 year rolling | Operational need only |
| CAB minutes | Permanent | Governance documentation |
| Hardening scans | 1 year rolling | Operational need only |

**Sector-Specific Extensions**:

- Financial services (FINMA): 10 years
- Healthcare (HIPAA): 6 years
- Government contracts: Per contract terms

### Evidence Quality Checklist

Before filing evidence, verify:

- [ ] Filename follows naming convention
- [ ] Date is accurate and in YYYYMMDD format
- [ ] File is in preferred format (PDF/XLSX)
- [ ] Document is complete (not draft/partial)
- [ ] Sensitive data is appropriately classified
- [ ] File is not corrupted (open to verify)
- [ ] Cross-references to other evidence are accurate
- [ ] Placed in correct directory per this guide

### Evidence Access Control

**Read Access**:

- Configuration Management team
- Internal audit team
- External auditors (during audit periods)
- Compliance officers
- CISO and direct reports

**Write Access**:

- Configuration Manager
- Designated evidence custodians
- Automated collection systems (service accounts)

**No Access**:

- General IT staff (request via Configuration Manager)
- External parties without NDA
- Terminated employees (revoke immediately)

### Evidence Collection Automation

**Recommended Automation**:

- **CMDB exports**: Weekly automated export
- **Compliance scans**: Automated quarterly scans
- **Configuration snapshots**: Nightly backup of critical configs
- **Drift alerts**: Real-time export to evidence repository
- **Change request archival**: Automatic when change closed

**Manual Collection**:

- Approval signatures (wet signatures required)
- Risk assessments (human judgment required)
- CAB meeting minutes (human-generated)
- Incident investigations (human analysis required)

---

## Appendix: Evidence Template Downloads

[Organisation should provide templates for]:

- Change Request Form (CR-Template.docx)
- Deviation Request Form (DEV-Template.docx)
- Exception Request Form (HARD-EX-Template.docx)
- Risk Assessment Template (Risk-Assessment-Template.xlsx)
- CAB Meeting Minutes Template (CAB-Minutes-Template.docx)

**Template Location**: [Organisation to define - e.g., SharePoint/Intranet]

---

## Evidence Repository Maintenance

**Quarterly Review** (Configuration Manager responsibilities):

- Verify evidence completeness for past quarter
- Archive evidence >1 year old per retention schedule
- Update Evidence-Register-Master-Index.pdf
- Review access control list (joiners/leavers)
- Verify backup/disaster recovery of evidence repository

**Annual Review** (CISO responsibilities):

- Audit evidence repository structure compliance with this guide
- Review retention policy compliance
- Assess evidence quality and completeness
- Update this guide if process improvements identified

---

**END OF TECHNICAL REFERENCE DOCUMENT**

*For binding policy requirements, refer to ISMS-POL-A.8.9 Configuration Management Policy.*

<!-- QA_VERIFIED: 2026-03-08 -->

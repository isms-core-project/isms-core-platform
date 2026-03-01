<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.10.2-TG:framework:TG:a.8.10.2 -->
**ISMS-IMP-A.8.10.2-TG - Deletion Methods Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Deletion Methods Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.10.2-TG |
| **Related Policy** | ISMS-POL-A.8.10 (Data Deletion) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.10 (Information Deletion) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.10 (Data Deletion)
- ISMS-IMP-A.8.10.1 (Retention Deletion Triggers)
- ISMS-IMP-A.8.10.3 (Third-Party & Cloud Deletion Assessment)
- ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a810_2_deletion_methods.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.10.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. Physical Storage Media |
| 3 | 3. Database Systems |
| 4 | 4. Cloud Storage |
| 5 | 5. File Systems & Backup Media |
| 6 | 6. Deletion Verification Test |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #006100 | Dark Green (Pass) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
| #9C5700 | Custom |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Media Type / System Name |
| 2 | Data Classification |
| 3 | Owner / Responsible Party |
| 4 | Deletion Method Used |
| 5 | Tool/Vendor Used |
| 6 | Status |
| 7 | Implementation Date |
| 8 | Last Effectiveness Test |
| 9 | Next Test Date |
| 10 | Gap Identified |
| 11 | Remediation Plan |
| 12 | Target Completion |
| 13 | Risk Level |
| 14 | Evidence Reference |
| 15 | Notes / Comments |
| 16 | Remediation Owner |
| 17 | Budget Required |
| 18 | NIST SP 800-88 Rev. 2 Method |
| 19 | Verification Method |
| 20 | Last Forensic Test Result |
| 21 | Media Disposal Method |
| 22 | Provider Tier |
| 23 | Deletion API Available |
| 24 | Snapshot/Backup Deletion |
| 25 | Multi-Region Deletion Verified |
| 26 | Deletion Type |
| 27 | Referential Integrity Handled |
| 28 | Backup Purging |
| 29 | Crypto-Erasure Key Management |
| 30 | Device Type |
| 31 | MDM Solution Used |
| 32 | Remote Wipe Capability |
| 33 | Full Disk Encryption |
| 34 | Test Frequency |
| 35 | Forensic Tool Used |
| 36 | Pass Rate (Last 12 Months) |
| 37 | Independent Testing |
| 38 | EXCEPTIONS / DEVIATIONS |
| 39 | EVIDENCE REGISTER |
| 40 | ASSESSMENT APPROVAL AND SIGN-OFF |
| 41 | ASSESSMENT SUMMARY |
| 42 | FINAL DECISION: |
| 43 | NEXT REVIEW DETAILS |
| 44 | Evidence ID |
| 45 | Category |
| 46 | Description |
| 47 | Source Document |
| 48 | Date Collected |
| 49 | Collected By |
| 50 | Notes |
| 51 | Assessment Area |
| 52 | Total Items |
| 53 | Compliant |
| 54 | Partial |
| 55 | Non-Compliant |
| 56 | N/A |
| 57 | Compliance % |
| 58 | Finding |
| 59 | Impact |
| 60 | Recommendation |
| 61 | Priority |

### Data Validation Values

All dropdown/list values used across sheets:

```
Public, Internal, Confidential, Restricted, Critical, High, Medium, Low, Yes
No, Unknown, Overwrite (1-pass), Overwrite (3-pass)
Overwrite (7-pass DoD 5220.22-M), Secure Erase (ATA/NVMe)
Cryptographic Erasure, Degaussing, Physical Destruction (Shred)
Physical Destruction (Incinerate), Physical Destruction (Crush/Pulverize)
Other (specify in notes), Clear, Purge, Destroy, N/A, Software Verification
Visual Inspection, Certificate of Destruction, Forensic Test, None
Pass (No Recovery), Fail (Partial Recovery), Fail (Full Recovery), Not Tested
Reuse, Recycle, Shred, Incinerate, Degauss, Other, Cloud Provider API Delete
Cloud Lifecycle Policy, Manual Console Delete, Crypto-Shred (Key Deletion)
Account Closure, Tier 1, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6, Tier 7
Tier 8, Tier 9, Tier 10, Yes - Automated, Yes - Manual, Automatic, Manual
Logical DELETE (soft delete), Hard DELETE (permanent), TRUNCATE TABLE
DROP TABLE/DATABASE, Purge/Vacuum, Crypto-Shred, Archive then Delete
Logical Delete, Hard Delete, Truncate, Yes - Cascading, Not Implemented
Factory Reset, MDM Remote Wipe, Full Disk Encryption + Format, Secure Erase
Physical Destruction, Corporate Laptop, Corporate Mobile, BYOD Laptop
BYOD Mobile, Tablet, Yes - Tested, Yes - Untested, Yes - BitLocker
Yes - FileVault, Yes - LUKS, Yes - Other, Forensic Recovery Test
Certificate Review, Monthly, Quarterly, Semi-Annual, Annual, Ad-hoc, Never
Yes - External, Yes - Internal, Planned, Configuration file, Screenshot
Deletion log, Documentation, Vendor spec, Audit log, Compliance report
Forensic test report, Verified, Pending verification, Not verified
Requires update, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 61 columns, 118 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"Secure deletion is not destruction — it is liberation from liability."*
— Data governance principle

<!-- QA_VERIFIED: 2026-03-01 -->

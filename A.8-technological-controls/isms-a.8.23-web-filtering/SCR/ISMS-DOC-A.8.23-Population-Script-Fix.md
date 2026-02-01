# ISMS-DOC-A.8.23 — Population Script Fix Documentation

**Date:** 2026-02-01
**Control:** A.8.23 Web Filtering
**Issue Type:** Data Validation Mismatch
**Status:** Resolved

---

## Issue Summary

The Excel workbook generators for A.8.23 define Status field dropdown validations with emoji-prefixed values, but the population scripts were inserting plain text values that did not match the validation lists.

## Root Cause

**Generator Validation (Correct):**
```python
formula1='"✅ Deployed,⚠️ Partial,❌ Not Deployed,🔄 Planned,N/A"'
formula1='"✅ Met,⚠️ Partial,❌ Not Met,N/A"'
formula1='"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"'
formula1='"✅ Integrated,⚠️ Partial,❌ Not Integrated,🔄 Planned"'
```

**Population Script Values (Incorrect):**
```python
["Squid Proxy", ..., "Non-Compliant", ...]  # Missing emoji prefix
["URL Filtering", ..., "Compliant", ...]  # Missing emoji prefix
```

## Affected Files

### Population Scripts Fixed

| Script | Status Fields Fixed |
|--------|---------------------|
| `populate_a823_1_filtering_infrastructure.py` | Deployed, Partial, Non-Compliant, Compliant, Integrated, Met |
| `populate_a823_2_network_coverage.py` | Non-Compliant, Partial |
| `populate_a823_3_policy_configuration.py` | Compliant, Partial |
| `populate_a823_4_monitoring_response.py` | No changes needed (uses different status values) |

### Values Changed

| Original Value | Corrected Value |
|----------------|-----------------|
| `"Deployed"` | `"✅ Deployed"` |
| `"Integrated"` | `"✅ Integrated"` |
| `"Met"` | `"✅ Met"` |
| `"Compliant"` | `"✅ Compliant"` |
| `"Partial"` | `"⚠️ Partial"` |
| `"Non-Compliant"` | `"❌ Non-Compliant"` |

## Related Fixes

This fix was identified alongside a similar issue in A.8.24 Use of Cryptography population scripts. See `ISMS-DOC-A.8.24-Population-Script-Fix.md` for that documentation.

## Prevention

For future population scripts, always verify Status field values match the generator's `DataValidation.formula1` setting before deployment.

---

**QA_VERIFIED:** 2026-02-01

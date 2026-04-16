# Third-Party Risk Management (TPRM)

<!-- ISMS-CORE:USER-MANUAL:13-tprm:v1.0:2026-04-16 -->

---

## Overview

The **TPRM** module manages third-party and supplier risk under ISO 27001:2022 controls A.5.19 (Information security in supplier relationships) through A.5.22 (Monitoring and review of supplier services). It includes dedicated DORA ICT third-party risk fields for financial sector organisations.

Navigate to **Risk & Operations → TPRM** in the sidebar.

---

## Vendor Register

The vendor register is a catalogue of all suppliers, third-party service providers, and business partners that have access to your information assets or provide ICT services.

### Adding a Vendor

1. Click **New Vendor**
2. Complete the vendor form:

| Field | Description |
|-------|-------------|
| **Vendor name** | Legal or trading name |
| **Category** | Software / Cloud / Outsourcing / Professional Services / Hardware / Other |
| **Criticality** | Critical / High / Medium / Low — your assessment of the vendor's importance |
| **Services provided** | What the vendor does for your organisation |
| **Data access** | Does the vendor have access to personal data? Classified data? |
| **Contract owner** | Internal owner of the vendor relationship |
| **Review date** | Next scheduled vendor review |

### DORA ICT Fields

For financial sector organisations subject to DORA, additional fields are available on each vendor record:

| Field | Description |
|-------|-------------|
| **ICT service type** | Software-as-a-Service / Infrastructure / Platform / Data analytics / Other ICT |
| **ICT provider entity type** | Provider type as defined in DORA Article 3 (credit institution, payment institution, etc.) |
| **Substitutability** | Easy / Medium / Difficult / Impossible — how replaceable is this provider? |
| **Systemic relevance** | Is this provider systemically relevant (potential market-wide impact)? |
| **Contract reference** | Reference to the ICT services contract |

The DORA Register view (see below) aggregates all vendors with DORA fields filled in and calculates your ICT concentration risk profile.

---

## Vendor Assessments

For each vendor, record periodic security assessments:

1. Open the vendor record and navigate to the **Assessments** tab
2. Click **New Assessment**
3. Record:
   - Assessment date
   - Assessment type (questionnaire / on-site / remote / certification review)
   - Assessor (internal or external)
   - Overall rating (Satisfactory / Needs Improvement / Unsatisfactory)
   - Key findings and required actions
   - Next review date

Assessment history is retained permanently — showing an auditor multiple assessment cycles over time demonstrates ongoing supplier monitoring under A.5.22.

---

## Contract Tracking

For each vendor, track the associated contracts:

1. Open the vendor record and navigate to the **Contracts** tab
2. Click **New Contract**
3. Record:
   - Contract reference number
   - Start and expiry date
   - Auto-renewal clause (yes/no)
   - Notice period (days)
   - Key obligations (data protection clauses, audit rights, SLAs)
   - Contract owner

Contracts approaching expiry are highlighted and can trigger the health notification banner if the expiry threshold is crossed.

---

## DORA ICT Register View

Navigate to **TPRM → DORA Register** for a dedicated view of all ICT third-party relationships required under DORA Article 28.

This view shows:

- All vendors with ICT service type populated
- Substitutability distribution (the DORA concentration risk indicator)
- Vendors flagged as systemically relevant
- Vendors with expiring contracts within 90 days

The DORA register can be exported as XLSX for submission to your competent authority if required.

---

## TPRM and Gap Management

If a vendor assessment identifies a security deficiency, create a gap directly from the vendor assessment view. The gap is linked to the vendor record and to the relevant ISO control group (A.5.19–A.5.22) for full traceability.

---

## TPRM Export

Export the vendor register and assessment history as:

- **CSV** — all vendor records with DORA fields
- **XLSX** — formatted vendor register with assessment status and contract expiry dates

<!-- QA_VERIFIED: 2026-04-16 -->

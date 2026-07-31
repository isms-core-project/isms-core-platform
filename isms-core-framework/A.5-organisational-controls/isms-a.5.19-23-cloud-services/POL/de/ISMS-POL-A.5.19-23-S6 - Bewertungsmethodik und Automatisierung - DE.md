<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S6-DE:framework:POL:a.5.19-23-s6 -->
**ISMS-POL-A.5.19-23-S6 — Bewertungsmethodik & Automatisierung**
**Cloud-Dienste-Sicherheit – Systems-Engineering-Ansatz**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Bewertungsmethodik & Automatisierung |
| **Dokumenttyp** | Richtlinienabschnitt |
| **Dokument-ID** | ISMS-POL-A.5.19-23-S6 |
| **Dokumentersteller** | Information Security Officer (ISO) |
| **Dokumenteigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISO | Erstfassung zum Python-basierten Bewertungsrahmenwerk |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Information Security Officer (ISO)
- Technik: Systems-Engineering-Teamleiter
- Qualität: Qualitätssicherungsmanager
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit)
- ISMS-POL-A.5.19-23 (Übergeordnete Richtlinie – Lieferanten- und Cloud-Dienste-Sicherheit)
- Alle ISMS-IMP-A.5.19-23-Implementierungsleitfäden
- ISMS-REF-A.5.23 (Cloud-Anbieter-Referenzregister)
- Python-Generatorskripte in 50_scripts-excel/
- ISO/IEC 27001:2022 Abschnitt 9.2 (Internes Audit)

---

# Zusammenfassung für das Management

## Zweck

Dieses Dokument definiert den **Systems-Engineering-(SE)-Ansatz** für die Bewertung der Cloud-Dienste-Sicherheits-Compliance. Anstelle traditioneller Checkbox-Audits werden **Python-generierte Excel-Arbeitsmappen** verwendet, die erzwingen:

- **Wiederholbare** Bewertungen (identische Struktur vierteljährlich)
- **Quantitative** Compliance-Metriken (87,3 % konform vs. „hauptsächlich konform")
- **Evidenzbasierte** Verifizierung (Screenshots, Konfigurationen, Verträge)
- **Transparente** Dashboards (automatisch aus Bewertungen berechnet)

## Kritischer Grundsatz

**„Wenn Sie es nicht generieren können, können Sie es nicht warten"**: Manuelle Tabellenkalkulationen degradieren mit der Zeit – Formeln brechen, Validierungen verschwinden und Inkonsistenzen entstehen über Bewertungszyklen hinweg. Kopierte Vorlagen weichen ab, wenn verschiedene Stakeholder lokale Versionen ohne Versionskontrolle ändern. Bewertungswerkzeuge müssen programmatisch generiert werden, um Konsistenz, Wiederholbarkeit und systematische Aktualisierungen bei Anforderungsänderungen sicherzustellen. Diese Richtlinie verwendet Python-Generatoren zur Erstellung von Excel-Bewertungsarbeitsmappen und ermöglicht schnelle Bereitstellung, kontrollierte Änderungen und evidenzbasierte Compliance-Messung mit vollständigen Audit-Trails.

**Systems-Engineering-Ansatz:**
```
1. Python-Generator ausführen → ISMS_REG_A523_1_Inventory.xlsx
2. Einkauf vervollständigt Dienstliste mit Nachweisen
3. Dashboard berechnet automatisch: „45/78 Dienste konform (57,7 %)"
4. Gap-Bericht identifiziert: „33 Dienste ohne MFA"
```

**Ergebnis:** Objektive, quantitative Bewertung des tatsächlichen Compliance-Status – keine subjektive Selbsteinschätzung.

---

# Framework-Architektur

## Fünf-Schichten-Design

```
┌─────────────────────────────────────────────────────────────┐
│ SCHICHT 1: RICHTLINIENEBENE                                 │
│ • ISMS-POL-A.5.19-23 (Master-Index)                         │
│ • ISMS-POL-A.5.19-23-S5 (Cloud-Dienste-Anforderungen)       │
│ • ISMS-POL-A.5.19-23-S6 (Dieses Dokument – Methodik)        │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ SCHICHT 2: BEWERTUNGSSPEZIFIKATIONEN (Markdown)             │
│ • ISMS-IMP-A.5.19-23.S1.md – Inventar & Klassifizierung     │
│ • ISMS-IMP-A.5.19-23.S2.md – Lieferanten-Due-Diligence      │
│ • ISMS-IMP-A.5.19-23.S3.md – Sichere Konfiguration          │
│ • ISMS-IMP-A.5.19-23.S4.md – Laufende Governance            │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ SCHICHT 3: IMPLEMENTIERUNG (Python-Skripte)                 │
│ • generate_reg_a523_1_inventory.py                          │
│ • generate_reg_a523_2_vendor_dd.py                          │
│ • generate_reg_a523_3_secure_config.py                      │
│ • generate_reg_a523_4_governance.py                         │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ SCHICHT 4: ÜBERPRÜFUNG (Integrierte Zusammenfassungs-       │
│ Dashboards)                                                 │
│ • Jede Arbeitsmappe enthält eigene Zusammenfassungs-        │
│   Dashboard-Tabelle                                         │
│ • Compliance-Metriken direkt in jeder Arbeitsmappe prüfen   │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ SCHICHT 5: ABZEICHNUNG (Genehmigung & Audit-Trail)          │
│ • Genehmigungsabzeichnungsblatt in jeder Arbeitsmappe       │
│ • Nachweisregister für Audit-Rückverfolgbarkeit             │
│ • Gap-Analyse und Abhilfeplanung pro Domäne                 │
└─────────────────────────────────────────────────────────────┘
```

## Bewertungsarbeitsmappen-Struktur

Jede Arbeitsmappe folgt diesem bewährten Muster:

| Tabellenblatt | Zweck | Ausgefüllt von | Überprüfungszyklus |
|---------------|-------|---------------|-------------------|
| **Anleitung & Legende** | Verwendungshinweise + Statuscodes | Automatisch generiert | N/A |
| **Bewertungsblätter (2–6)** | Domänenspezifische Checklisten | Stakeholder | Vierteljährlich |
| **Zusammenfassungs-Dashboard** | Compliance % pro Domäne | Formelgesteuert | Automatisch |
| **Nachweisregister** | Links zu Nachweisdokumenten | Stakeholder | Vierteljährlich |
| **Genehmigungsabzeichnung** | ISB-Genehmigung + Überprüfungsdaten | Management | Vierteljährlich |

---

# Spezifikation der Bewertungsarbeitsmappen

## Arbeitsmappe 1: Cloud-Dienste-Inventar & Klassifizierung

**Dokument-ID:** ISMS-IMP-A.5.19-23.S1
**Dateiname:** `ISMS_REG_A523_1_Inventory_JJJJMMTT.xlsx`
**Generiert von:** `generate_reg_a523_1_inventory.py`
**Stakeholder:** IT-Betrieb, Einkauf, Finanzen
**Tabellenanzahl:** 10 Tabellenblätter

**Zweck:** Verbindliches Inventar aller Cloud-Dienste mit Kritikalitätsklassifizierung führen.

**Tabellenstruktur:**
1. Anleitung & Legende
2. SaaS-Dienste (Office 365, Salesforce, Zoom usw.)
3. IaaS/PaaS-Dienste (AWS, Azure, GCP usw.)
4. Cloud-Sicherheitsdienste (CrowdStrike, Zscaler usw.)
5. Cloud-Speicherdienste (Dropbox, Box usw.)
6. Datenklassifizierungs-Mapping
7. Servicekritikalitätsbewertung
8. Zusammenfassungs-Dashboard
9. Nachweisregister
10. Genehmigungsabzeichnung

**Basisspalten (17 Standard A–Q):**

- A: Name des Cloud-Dienstes
- B: Diensttyp (SaaS/IaaS/PaaS/Security/Storage)
- C: Anbietername
- D: Servicekritikalität (Kritisch/Hoch/Mittel/Niedrig)
- E: Datenklassifizierung (Eingeschränkt/Vertraulich/Intern/Öffentlich)
- F: Datenresidenzregion (Schweiz/EU/USA/Global)
- G: Vertragsstatus (Aktiv/Verlängerung fällig/Abgelaufen)
- H: Status (✅ Konform / ⚠️ Teilweise / ❌ Nicht konform)
- I: Nachweisort
- J: Lückenbeschreibung
- K: Abhilfe erforderlich (Ja/Nein)
- L: Ausnahme-ID
- M: Risiko-ID
- N: Kompensierende Kontrollen
- O: Dienstverantwortlicher
- P: Ziel-Behebungsdatum
- Q: Budgetauswirkung (Hoch/Mittel/Niedrig/Keine)

**Erweiterte Spalten (R–X inventarspezifisch):**

- R: Monatliche Kosten (Formel: numerisch validiert)
- S: Jährlicher Vertragswert
- T: Anzahl lizenzierter Benutzer
- U: Integrationsanzahl (Anzahl verbundener Systeme)
- V: Backup-Dienst verfügbar (Ja/Nein)
- W: Exit-Machbarkeit (Einfach/Mittel/Schwer/Unbekannt)
- X: Letztes Inventarüberprüfungsdatum

## Arbeitsmappe 2: Lieferanten-Due-Diligence & Verträge

**Dokument-ID:** ISMS-IMP-A.5.19-23.S2
**Dateiname:** `ISMS_REG_A523_2_DueDiligence_JJJJMMTT.xlsx`
**Generiert von:** `generate_reg_a523_2_vendor_dd.py`
**Stakeholder:** Recht, Einkauf, Compliance, ISO
**Tabellenanzahl:** 10 Tabellenblätter

**Zweck:** Lieferantensicherheitszertifizierungen, Vertragsbedingungen, SLAs und Prüfungsrechte verfolgen.

**Tabellenblätter:**
1. Anleitung & Legende
2. Lieferantensicherheitszertifizierungen
3. Vertragsbedingungsanalyse
4. SLA-Anforderungen & Leistung
5. Datensouveränitäts-Compliance
6. Forensik & Störungsunterstützung
7. Prüfungsrecht & Penetrationstests
8. Zusammenfassungs-Dashboard
9. Nachweisregister
10. Genehmigungsabzeichnung

**Erweiterte Spalten (R–X):**

- R: ISO 27001 zertifiziert (Ja/Nein/Unbekannt + Zertifikat-Nr.)
- S: SOC 2 Type II-Bericht verfügbar (Ja/Nein/Unbekannt)
- T: Vertragsablaufdatum
- U: SLA-Verfügbarkeit % (99,9 %, 99,95 % usw.)
- V: Prüfungsrechtsklausel (Ja/Nein)
- W: Datenportabilitätsklausel (Ja/Nein)
- X: Forensik/IR-Unterstützung (Ja/Nein/Begrenzt)

## Arbeitsmappe 3: Sichere Konfiguration & Bereitstellung

**Dokument-ID:** ISMS-IMP-A.5.19-23.S3
**Dateiname:** `ISMS_REG_A523_3_Configuration_JJJJMMTT.xlsx`
**Generiert von:** `generate_reg_a523_3_secure_config.py`
**Stakeholder:** IT-Sicherheit, DevOps, Systemadministratoren
**Tabellenanzahl:** 11 Tabellenblätter

**Zweck:** Sicherheitskonfiguration-Baseline-Compliance für bereitgestellte Cloud-Dienste bewerten.

**Tabellenblätter:**
1. Anleitung & Legende
2. Identitäts- & Zugriffsmanagement
3. Datenverschlüsselung (Ruhezustand & Übertragung)
4. Netzwerksicherheit & Segmentierung
5. Protokollierungs- & Überwachungskonfiguration
6. Backup & Disaster Recovery
7. Datenklassifizierungs-Kennzeichnung
8. API-Sicherheit & Integration
9. Zusammenfassungs-Dashboard
10. Nachweisregister
11. Genehmigungsabzeichnung

**Erweiterte Spalten (R–X):**

- R: MFA aktiviert (Ja/Nein/Teilweise)
- S: Verschlüsselung im Ruhezustand (Ja/Nein/Unbekannt)
- T: Verschlüsselung bei Übertragung (TLS 1.3/TLS 1.2/Schwach)
- U: Zentralisierte Protokollierung (Ja/Nein/Teilweise)
- V: SSO-Integration (Ja/Nein/Geplant)
- W: Datenklassifizierungslabels angewendet (Ja/Nein/Teilweise)
- X: Konfigurationsbaseline dokumentiert (Ja/Nein)

## Arbeitsmappe 4: Laufende Governance & Risikomanagement

**Dokument-ID:** ISMS-IMP-A.5.19-23.S4
**Dateiname:** `ISMS_REG_A523_4_Governance_JJJJMMTT.xlsx`
**Generiert von:** `generate_reg_a523_4_governance.py`
**Stakeholder:** IT-Management, Risikomanagement, ISO
**Tabellenanzahl:** 11 Tabellenblätter

**Zweck:** Laufende Governance, Lieferantenrisiko, Betriebskontinuität und Änderungsmanagement überwachen.

**Tabellenblätter:**
1. Anleitung & Legende
2. Sicherheitsbewusstsein & Schulung
3. Incident-Response-Verfahren
4. Sicherheits-Update-Management
5. Vendor-Lock-in-Bewertung
6. Vendor-Lock-out-Bewertung
7. Betriebskontinuitätsplanung
8. Änderungsmanagement-Verfolgung
9. Zusammenfassungs-Dashboard
10. Nachweisregister
11. Genehmigungsabzeichnung

**Erweiterte Spalten (R–X):**

- R: Sicherheitsschulung abgeschlossen (Ja/Nein + Datum)
- S: Letztes Sicherheitsüberprüfungsdatum
- T: Incident-Response-Plan getestet (Ja/Nein/Geplant)
- U: Vendor-Lock-in-Risiko (Hoch/Mittel/Niedrig)
- V: BC/DR-Plan vorhanden (Ja/Nein)
- W: BC/DR letztes Testdatum
- X: Änderungsmanagementprozess (Ja/Nein)

---

# Python-Generator-Architektur

## Skriptstruktur (Standardmuster)

Alle Generatorskripte folgen dieser modularen Architektur:

```python
# ============================================================================
# ABSCHNITT 1: ARBEITSMAPPENERSTELLUNG & STILDEFINITIONEN
# ============================================================================
def create_workbook() -> Workbook:
    """Alle Tabellenblätter gemäss Spezifikation erstellen."""

def setup_styles() -> dict:
    """Farben, Schriften, Rahmen definieren (NEUE Objekte pro Zelle!)."""

# ============================================================================
# ABSCHNITT 2: SPALTENDEFINITIONEN (BASIS + ERWEITERT)
# ============================================================================
def get_base_cloud_columns() -> dict:
    """Gibt 17 Standardspalten (A–Q) für ALLE Cloud-Bewertungen zurück."""

def get_extended_columns_inventory() -> dict:
    """Gibt domänenspezifische Spalten R–X für Inventar zurück."""

# ============================================================================
# ABSCHNITT 3: VALIDIERUNGSDEFINITIONEN
# ============================================================================
def create_base_validations(ws) -> dict:
    """Dropdown-Validierungen für Standardfelder erstellen."""

def create_extended_validations(ws, sheet_type) -> dict:
    """Domänenspezifische Dropdowns erstellen."""

# ============================================================================
# ABSCHNITT 4: CHECKLISTEN-ELEMENTDEFINITIONEN
# ============================================================================
def get_checklist_items(sheet_type) -> list:
    """Domänenspezifische Compliance-Checkliste zurückgeben."""

# ============================================================================
# ABSCHNITT 5: REFERENZTABELLENDEFINITIONEN
# ============================================================================
def get_reference_tables(sheet_type) -> dict:
    """Nachschlagetabellen zurückgeben (Anbieter, Regionen, Standards)."""

# ============================================================================
# ABSCHNITT 6: GENERISCHER BEWERTUNGSBLATT-BUILDER
# ============================================================================
def create_assessment_sheet(ws, styles, section_title, policy_ref,
                           question, sheet_type):
    """Universeller Builder – EINE Funktion erstellt ALLE Bewertungsblätter."""

# ============================================================================
# ABSCHNITT 7: SPEZIALISIERTE TABELLENBLATT-ERSTELLER
# ============================================================================
def create_instructions_sheet(ws, styles):
def create_summary_dashboard(ws, styles):
def create_evidence_register(ws, styles):
def create_approval_signoff(ws, styles):

# ============================================================================
# ABSCHNITT 8: DOMÄNENSPEZIFISCHE BEWERTUNGSBLÄTTER
# ============================================================================
def create_1_saas_services(ws, styles):
def create_2_iaas_paas_services(ws, styles):
# usw.

# ============================================================================
# ABSCHNITT 9: HAUPTAUSFÜHRUNG
# ============================================================================
def main():
    """Arbeitsmappengenerierung orchestrieren."""
```

## Kritische Implementierungshinweise

**Best Practice für Stil-Objekte:**
```python
# ❌ VERMEIDEN – Gemeinsam genutzte Objekte können Excel-Kompatibilitätsprobleme verursachen
border = Border(left=Side(style="thin"), ...)
cell1.border = border  # Referenz 1
cell2.border = border  # Referenz 2

# ✅ EMPFOHLEN – Neues Objekt pro Zelle gewährleistet Kompatibilität
def apply_border(cell):
    cell.border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin")
    )
```

**Implementierungsbegründung:** Die Erstellung neuer Stil-Objekte für jede Zelle verhindert potenzielle Excel-Kompatibilitätswarnungen und gewährleistet saubere Arbeitsmappengenerierung.

---

# Validierung & Integration

## Verarbeitungsskripte

| Skript | Zweck | Zeitpunkt der Ausführung |
|--------|-------|--------------------------|
| **generate_a523_1_inventory.py** | Generiert Arbeitsmappe S1 Cloud-Dienste-Inventar | Vor Beginn des Bewertungszyklus |
| **generate_a523_2_vendor_dd.py** | Generiert Arbeitsmappe S2 Lieferanten-Due-Diligence | Vor Beginn des Bewertungszyklus |
| **generate_a523_3_secure_config.py** | Generiert Arbeitsmappe S3 Sichere Konfiguration | Vor Beginn des Bewertungszyklus |
| **generate_a523_4_governance.py** | Generiert Arbeitsmappe S4 Laufende Governance | Vor Beginn des Bewertungszyklus |

## Verarbeitungsworkflow

```
┌────────────────────────────────────────────────────────────┐
│ 1. Arbeitsmappe generieren                                 │
│    $ python3 generate_reg_a523_1_inventory.py              │
│    Ausgabe: ISMS_REG_A523_1_Inventory_20260115.xlsx        │
└────────────────────────────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────────────────┐
│ 2. An Stakeholder verteilen                                │
│    - E-Mail an IT-Betrieb, Einkauf, Recht                  │
│    - Frist: 2 Wochen zur Fertigstellung                    │
└────────────────────────────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────────────────┐
│ 3. Zusammenfassungs-Dashboards überprüfen                  │
│    Jede fertiggestellte Arbeitsmappe öffnen und das        │
│    eingebaute Zusammenfassungs-Dashboard-Tabellenblatt     │
│    auf Compliance-Metriken prüfen                          │
└────────────────────────────────────────────────────────────┘
```

---

# Dashboard-Integration

## Formelgesteuerte Aggregation

```excel
# Beispiel: Konforme Dienste aus Inventararbeitsmappe zählen
=COUNTIF('[ISMS_REG_A523_1_Inventory_20260115.xlsx]2. SaaS Services'!$H$8:$H$50,"✅*")

# Beispiel: Compliance-Prozentsatz berechnen
=IF((B4-F4)=0,"0%",ROUND(C4/(B4-F4)*100,1)&"%")
```

**Vorteile:**

- **Keine manuellen Updates** – Bewertung ändern → Dashboard aktualisiert sich
- **Echtzeit-Metriken** – Stakeholder sehen live Compliance %
- **Audit-Trail** – Formeln zeigen genau, woher Daten stammen

## Dashboard-Visualisierungen

**Compliance-Übersichtstabelle:**
| Bewertungsbereich | Gesamt | Konform | Teilweise | Nicht konform | N/A | Compliance % |
|------------------|--------|---------|----------|---------------|-----|-------------|
| Inventar         | 78     | 45      | 18       | 15            | 0   | 57,7 %       |
| Lieferanten-DD   | 78     | 62      | 10       | 6             | 0   | 79,5 %       |
| Konfiguration    | 156    | 98      | 35       | 23            | 0   | 63,2 %       |
| Governance       | 78     | 51      | 20       | 7             | 0   | 65,4 %       |
| **GESAMT**       | **390** | **256** | **83** | **51**       | **0** | **65,6 %** |

**Risiko-Heatmap:**

- Hohes Vendor-Lock-in + geringe Exit-Machbarkeit = 🔴 Kritisches Risiko
- Eingeschränkte Daten + Nicht-EU-Residenz = 🔴 Souveränitätsverstoss
- Kritischer Dienst + kein BC/DR-Test = 🟡 Hohes Risiko

---

# Bewertungszyklus & Workflow

## Vierteljährlicher Bewertungszyklus

```
Woche 1: GENERIERUNG
├─ Security Engineering führt Python-Generatoren aus
├─ Qualitätsprüfung der generierten Arbeitsmappen
└─ An Stakeholder mit Anweisungen verteilen

Wochen 2–3: BEWERTUNG
├─ IT-Betrieb vervollständigt Inventar & Konfiguration
├─ Einkauf aktualisiert Lieferanten- & Vertragsdaten
├─ Recht überprüft Compliance & Exit-Klauseln
└─ Nachweise gesammelt (Verträge, Zertifikate, Screenshots)

Woche 4: ÜBERPRÜFUNG
├─ ISO überprüft fertiggestellte Bewertungen
├─ Gap-Analyse durchgeführt
├─ Abhilfeprioritäten zugewiesen
└─ ISB-Genehmigung eingeholt

Woche 5: INTEGRATION
├─ Zusammenfassungs-Dashboards überprüfen
├─ Führungskräfte-Zusammenfassung erstellt
└─ Board-Berichtspaket vorbereitet
```

## Ad-hoc-Bewertungsauslöser

Bewertungen ausserhalb des Quartalszyklus durchführen, wenn:

- **Onboarding neuer Cloud-Dienste** (Arbeitsmappe 1 + 2 verwenden)
- **Wesentliche Konfigurationsänderungen** (Arbeitsmappe 3 verwenden)
- **Sicherheitsvorfälle** (Arbeitsmappe 4 + 5 verwenden)
- **Vertragsverlängerungen** (Arbeitsmappe 2 verwenden)
- **Audit-Vorbereitung** (alle 5 Arbeitsmappen verwenden)

---

# Stakeholder-Leitfaden

## Wer füllt was aus

| Arbeitsmappe | Primär | Sekundär | Tertiär |
|-------------|--------|---------|--------|
| 1. Inventar | IT-Betrieb | Einkauf | Finanzen |
| 2. Lieferanten-DD | Einkauf | Recht | Compliance |
| 3. Konfiguration | IT-Sicherheit | DevOps | Sys-Admins |
| 4. Governance | Risikomanagement | ISO | IT-Management |
| 5. Dashboard | ISO | (Automatisch generiert) | ISB |

## Ausfüllanweisungen

**Für jedes Bewertungsblatt:**
1. **Gelbe Zellen** mit Ihren Daten füllen
2. **Dropdown-Menüs** verwenden (nicht freihand eingeben)
3. **Nachweisort** angeben (Dateipfad, Link, Dok-ID)
4. Wenn Status = Teilweise/Nicht konform:

   - **Lückenbeschreibung** ausfüllen
   - **Abhilfe erforderlich** = Ja setzen
   - **Verantwortliche Person** zuweisen
   - **Zieldatum** festlegen

5. **Nachweisregister** mit unterstützenden Dokumenten aktualisieren

**Nachweisanforderungen:**

- ✅ Vertrags-PDFs (Lieferantenvereinbarungen, SLAs)
- ✅ Sicherheitszertifizierungen (ISO 27001, SOC 2-Berichte)
- ✅ Konfigurations-Screenshots (MFA-Einstellungen, Verschlüsselung)
- ✅ Auditberichte (Penetrationstests, Schwachstellen-Scans)
- ✅ Schulungsnachweise (Sicherheitsbewusstseins-Abschluss)
- ✅ BC/DR-Testergebnisse (letzter Wiederherstellungs-Drill-Bericht)
- ❌ „Wir haben einen Prozess" (ohne Beweis nicht akzeptabel!)

## Bewertungsabzeichnungskriterien

Eine Bewertung ist **bereit zur ISO/ISB-Abzeichnung** nur wenn alle folgenden Bedingungen erfüllt sind:

| Kriterium | Anforderung |
|-----------|------------|
| **Pflichtspalten vollständig** | 100 % der Spalten A–Q (Basisspalten) für jede Zeile ausgefüllt; N/A-Einträge erfordern einen dokumentierten Grund in der Lückenbeschreibung |
| **Nachweisort angegeben** | Jede Nicht-N/A-Zeile hat einen Nachweisort (Dateipfad, SharePoint-URL, Dokument-ID oder Vertragsreferenz) – „wird bereitgestellt" ist nicht akzeptabel |
| **Lückenbeschreibungen spezifisch** | Alle Teilweise- oder Nicht-konform-Zeilen haben eine Lückenbeschreibung, die die spezifisch fehlende Kontrolle benennt; generischer Text („TBD", „in Prüfung", „in Bearbeitung") wird nicht akzeptiert |
| **Behebungsdaten realistisch** | Zieldaten sind Kalenderdaten ≤12 Monate; „so bald wie möglich" oder leer werden nicht akzeptiert |
| **Verantwortliche Person zugewiesen** | Jede offene Lücke hat eine benannte Person (kein Team oder Rollentitel), die bestätigt, von ihrer Zuweisung zu wissen |
| **Regulatorische Felder vollständig** | Wenn der Dienst DORA- oder NIS2-anwendbar ist (gemäss ISMS-POL-A.5.19-23 Abschnitt 12), sind die entsprechenden regulatorischen Felder ausgefüllt |
| **Stichproben-Audit bestanden** | ISO führt Stichprobe von 10 % der Zeilen (mindestens 5 Zeilen) durch und bestätigt, dass Nachweise zugänglich sind und dem angegebenen Status entsprechen |

**Abzeichnungsprozess:**

1. Bewerter reicht fertiggestellte Arbeitsmappe über das Dokumentenmanagementsystem bei ISO ein
2. ISO führt Vollständigkeitsprüfung gegen alle obigen Kriterien durch
3. Kriterien erfüllt → ISO zeichnet Genehmigungsabzeichnungsblatt ab und erfasst Datum
4. Kriterien nicht erfüllt → ISO gibt Arbeitsmappe mit spezifischen Mängelhinweisen zurück; Bewerter hat 5 Werktage zur Behebung und Wiedereinreichung
5. ISB zeichnet alle Stufe-1-Lieferanten-Arbeitsmappen ab; ISO zeichnet Stufe 2–4 ab

**Mindestakzeptable Nachweisformate:**

| Nachweistyp | Akzeptabel | Nicht akzeptabel |
|-------------|-----------|----------------|
| Vertrag | Unterzeichnetes PDF, SharePoint-Link, Vertrags-ID im Managementsystem | E-Mail-Thread, mündliche Bestätigung |
| Zertifizierung | Aktuelles Zertifikat-PDF oder direkter öffentlicher Registry-Link | Abgelaufenes Zertifikat, Selbsterklärung des Anbieters |
| Konfiguration | Screenshot mit sichtbarem Datum und Systemname oder exportierte Konfigurationsdatei | Beschreibung ohne Beweis |
| Audit/Pen-Test | Unterzeichneter Bericht von akkreditierter/lizenzierter Stelle | Zusammenfassungsfolie, Executive Deck |
| Schulung | LMS-Abschlussnachweis mit Namen und Daten | „Schulung wurde durchgeführt" |

---

# Kontinuierliche Verbesserung

## Framework-Verbesserungsprozess

**Verbesserungsauslöser:**

- Auditbefunde
- Stakeholder-Feedback
- Neue Cloud-Diensttypen
- Regulatorische Änderungen
- Technologische Entwicklung

**Prozess:**
1. Problem in GitHub/Jira dokumentieren
2. Markdown-Spezifikation aktualisieren
3. Python-Skript regenerieren
4. Generierte Arbeitsmappen testen
5. Dieses S6-Dokument aktualisieren
6. Änderungen an Stakeholder kommunizieren

## Qualitätsmetriken

**Framework-Gesundheitsindikatoren:**

- ✅ <2 Stunden Generierungszeit (alle 5 Arbeitsmappen)
- ✅ >80 % Stakeholder-Fertigstellungsrate (innerhalb von 2 Wochen)
- ✅ <5 % Fehlerrate in fertiggestellten Bewertungen
- ✅ Keine kritischen Befunde in Auditüberprüfungen
- ✅ Vierteljährliche Framework-Updates planmässig abgeschlossen

---

# Referenzinformation

## Verwandte Dokumente

**Richtlinienebene:**

- ISMS-POL-A.5.19-23 (Master-Index)
- ISMS-POL-A.5.19-23-S5 (Cloud-Dienste-Sicherheitsanforderungen)

**Bewertungsspezifikationen:**

- ISMS-IMP-A.5.19-23.S1 – Inventar & Klassifizierungsspezifikation
- ISMS-IMP-A.5.19-23.S2 – Lieferanten-Due-Diligence-Spezifikation
- ISMS-IMP-A.5.19-23.S3 – Sichere Konfigurationsspezifikation
- ISMS-IMP-A.5.19-23.S4 – Laufende Governance-Spezifikation

**Generator-Skripte:**

- generate_reg_a523_1_inventory.py
- generate_reg_a523_2_vendor_dd.py
- generate_reg_a523_3_secure_config.py
- generate_reg_a523_4_governance.py

## Externe Standards

- ISO/IEC 27001:2022 – Massnahme A.5.23
- ISO/IEC 27002:2022 – Cloud-Sicherheitsleitlinien
- ISO/IEC 27017:2026 – Cloud-spezifische Kontrollen
- ISO/IEC 27018:2025 – Personenbezogene Informationen in öffentlichen Clouds
- NIST SP 800-144 – Leitlinien zu Sicherheit und Datenschutz in der öffentlichen Cloud
- CSA Cloud Controls Matrix (CCM) v4

---

# Anhang A: Kurzreferenz

## Skriptausführungs-Spickzettel

```bash
# Alle Bewertungsarbeitsmappen generieren
python3 generate_reg_a523_1_inventory.py
python3 generate_reg_a523_2_vendor_dd.py
python3 generate_reg_a523_3_secure_config.py
python3 generate_reg_a523_4_governance.py

# Zusammenfassungs-Dashboards überprüfen
```

---

**DOKUMENTENDE**

*„Das erste Prinzip ist, dass man sich selbst nicht täuschen darf – und man ist die Person, die am leichtesten zu täuschen ist."*
*— Richard Feynman*

**Übersetzung für das ISMS:** Evidenzbasierte Compliance verhindert Cloud-Washing! ☁️🔍
<!-- QA_VERIFIED: 2026-03-28 -->

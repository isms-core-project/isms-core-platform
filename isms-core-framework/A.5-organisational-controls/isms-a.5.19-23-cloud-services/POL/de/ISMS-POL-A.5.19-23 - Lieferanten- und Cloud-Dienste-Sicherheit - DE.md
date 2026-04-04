<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-DE:framework:POL:a.5.19-23 -->
**ISMS-POL-A.5.19-23 — Lieferanten- und Cloud-Dienste-Sicherheit**
**Umfassendes Richtlinien- und Umsetzungsrahmenwerk**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Lieferanten- und Cloud-Dienste-Sicherheit |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.19-23 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB/ISO | Erstrichtlinienrahmenwerk für ISO 27001:2022-Erstzertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Compliance: Rechts-/Compliance-Beauftragter
- Beschaffung: Beschaffungsleiter
- Letzte Autorität: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.5.19-23-S1 (Grundlagen der Lieferantenbeziehungen)
- ISMS-POL-A.5.19-23-S2 (Anforderungen an Lieferantenvereinbarungen)
- ISMS-POL-A.5.19-23-S3 (IKT-Lieferkettensicherheit)
- ISMS-POL-A.5.19-23-S4 (Lieferantenüberwachung & Änderungsmanagement)
- ISMS-POL-A.5.19-23-S5 (Cloud-Dienste-Sicherheit)
- ISMS-POL-A.5.19-23-S6 (Bewertungsmethodik & Automatisierung)
- ISMS-IMP-A.5.19-23.S1-UG/TG (Cloud-Dienst-Inventar & Klassifizierung)
- ISMS-IMP-A.5.19-23.S2-UG/TG (Anbieter-Due-Diligence & Verträge)
- ISMS-IMP-A.5.19-23.S3-UG/TG (Sichere Konfiguration & Bereitstellung)
- ISMS-IMP-A.5.19-23.S4-UG/TG (Laufende Governance & Risikomanagement)
- ISMS-REF-A.5.23 (Cloud-Anbieter-Referenzregister)
- ISO/IEC 27001:2022 Kontrollen A.5.19-23
- ISO/IEC 27036 (Lieferantenbeziehungen)
- ISO/IEC 27017 (Cloud-Sicherheit)
- ISO/IEC 27018 (Cloud-Datenschutz)

**Verteilung**: Alle Mitarbeitenden, Auftragnehmer, Beschaffungspersonal, Rechtsabteilung, IT-Betrieb, Cloud-Administratoren

---

## Zusammenfassung für die Geschäftsleitung

Dieses Dokument dient als **Masterindex** für das Lieferanten- und Cloud-Dienste-Sicherheitsrahmenwerk von [Organisation] und setzt ISO/IEC 27001:2022 Kontrollen A.5.19 bis A.5.23 um.

**Zweck**: Festlegung verbindlicher Anforderungen für das Management von Informationssicherheitsrisiken im Zusammenhang mit externen Lieferanten, Vertragsvereinbarungen, IKT-Lieferkettenabhängigkeiten, laufendem Lieferantenbeziehungsmanagement und dem Cloud-Dienste-Lebenszyklus.

**Anwendungsbereich**: Alle Lieferantenbeziehungen mit Zugang zu Organisationsinformationen oder -systemen, alle Cloud-Dienste (IaaS, PaaS, SaaS, Sicherheitsdienste), alle Vertragsvereinbarungen mit externen Dienstleistern sowie alle IKT-Produkte mit Lieferkettenabhängigkeiten.

**Kritischer Grundsatz – „Lieferantenvertrauen muss verifiziert, nicht angenommen werden"**: Dieses Rahmenwerk erfordert eine evidenzbasierte Validierung der Sicherheitslage von Lieferanten durch systematische Due-Diligence-Prüfung, vertragliche Verpflichtungen mit durchsetzbaren Bedingungen und kontinuierliche Überwachung während des gesamten Beziehungslebenszyklus. Lieferantenansprüche ohne Drittpartei-Bescheinigung (SOC 2, ISO 27001, Compliance-Zertifikate), Verträge ohne durchsetzbare Sicherheitsklauseln und Prüfrechte sowie Beziehungen ohne regelmässige Überprüfung sind inakzeptable Risiken. Vertrauen mit Überprüfung durch dokumentierte Nachweise ist nicht verhandelbar.

**Rahmenwerkskomponenten**:

- **Richtlinienebene:** Governance-Dokumente mit Anforderungen (7 Richtliniendokumente)
- **Bewertungsebene:** Technische Bewertungsspezifikationen (Markdown-Dokumentation)
- **Umsetzungsebene:** Python-generierte Excel-Arbeitsmappen (4 Bewertungsarbeitsmappen)
- **Validierungsebene:** Qualitätssicherungs- und Normalisierungsskripte
- **Integrationsebene:** Individuelle Arbeitsmappe-Übersichts-Dashboards

**Ansatz**: Dieses Rahmenwerk verwendet einen **dokumentierten, systematischen Prozess**, bei dem Bewertungstools programmgesteuert aus kontrollierten Spezifikationen generiert werden und nicht manuell erstellt werden. Dies gewährleistet Konsistenz, Wiederholbarkeit und Versionskontrolle.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00, einschliesslich Schweizer nDSG, EU DSGVO Art. 28, ISO/IEC 27001:2022 und bedingte Anforderungen für DORA, NIS2, EU KI-Act und US CLOUD Act.

---

## Kontrollausrichtung

**ISO/IEC 27001:2022 Anhang A.5.19-23 — Lieferanten- und Cloud-Dienste-Sicherheit**

Dieses Richtlinienrahmenwerk bietet organisatorische Governance für fünf verwandte Kontrollen, die den vollständigen Lieferanten- und Cloud-Dienste-Lebenszyklus abdecken:

### A.5.19 – Informationssicherheit in Lieferantenbeziehungen

> *Prozesse und Verfahren sollten mit Lieferanten definiert und vereinbart werden, um Informationssicherheitsrisiken im Zusammenhang mit der Nutzung von Produkten oder Dienstleistungen des Lieferanten zu managen.*

**Kontrollziel**: Sicherstellung, dass Informationssicherheitsrisiken im Zusammenhang mit Lieferantenbeziehungen über den gesamten Beziehungslebenszyklus identifiziert, bewertet und gemanagt werden.

**ISO/IEC 27002:2022 Leitlinien-Zusammenfassung**:

- Lieferantenbeziehungen müssen durch definierte Prozesse für den gesamten Lebenszyklus verwaltet werden (Auswahl, Onboarding, Betrieb, Beendigung)
- Lieferanten müssen basierend auf Zugriffstyp, Datensensibilität und Servicekritikalität identifiziert und klassifiziert werden
- Due Diligence muss vor der Gewährung von Lieferantenzugriff auf Organisationsinformationen oder -systeme durchgeführt werden
- Lieferantensicherheitsanforderungen müssen auf Basis der Risikoklassifizierung und Datenklassifizierung definiert werden
- Die Lieferantenleistung und -sicherheitslage muss während der gesamten Beziehungsdauer überwacht werden
- Lieferanten-Ausstiegsverfahren müssen zur sicheren Beendigung und Datenrückgabe eingerichtet werden
- Shadow-IT und nicht autorisierte Lieferantennutzung muss aktiv identifiziert und gemanagt werden
- Lieferantenabhängigkeiten und Konzentrationsrisiken müssen für kritische Dienste bewertet werden

**Richtlinienreferenz**: Siehe ISMS-POL-A.5.19-23-S1 (Grundlagen der Lieferantenbeziehungen) für detaillierte Anforderungen.

### A.5.20 – Berücksichtigung von Informationssicherheit in Lieferantenvereinbarungen

> *Relevante Informationssicherheitsanforderungen sollten mit jedem Lieferanten festgelegt und vereinbart werden, der auf Informationen der Organisation zugreifen, diese verarbeiten, speichern, kommunizieren oder IKT-Infrastrukturkomponenten bereitstellen kann.*

**Kontrollziel**: Sicherstellung, dass Informationssicherheitsanforderungen vertraglich bindend und durchsetzbar sind.

**ISO/IEC 27002:2022 Leitlinien-Zusammenfassung**:

- Informationssicherheitsanforderungen müssen in alle Lieferantenverträge aufgenommen werden
- Anforderungen müssen Vertraulichkeit, Integrität und Verfügbarkeit von Organisationsinformationen abdecken
- Verträge müssen Zugangskontrollen, Authentifizierungsanforderungen und Autorisierungsverfahren definieren
- Datenschutz- und Privatsphäreverpflichtungen müssen gemäss anwendbaren Vorschriften spezifiziert werden (DSGVO Art. 28, nDSG)
- Anforderungen an Vorfallsmeldungen müssen mit konkreten Zeitvorgaben dokumentiert werden
- Prüfrechte und Compliance-Verifizierungsmechanismen müssen eingerichtet werden
- SLAs müssen Sicherheitskennzahlen und Leistungsindikatoren umfassen
- Ausstiegsverfahren und Datenverpflichtungen zur Rückgabe/Vernichtung müssen vertraglich definiert sein

**Richtlinienreferenz**: Siehe ISMS-POL-A.5.19-23-S2 (Anforderungen an Lieferantenvereinbarungen) für detaillierte Vertragsanforderungen.

### A.5.21 – Management der Informationssicherheit in der IKT-Lieferkette

> *Prozesse und Verfahren sollten mit Lieferanten definiert und vereinbart werden, um Informationssicherheitsrisiken im Zusammenhang mit der IKT-Dienste- und Produkt-Lieferkette zu managen.*

**Kontrollziel**: Management von Informationssicherheitsrisiken innerhalb der IKT-Lieferkette einschliesslich Sub-Lieferanten, Komponenten und Software-Abhängigkeiten.

**ISO/IEC 27002:2022 Leitlinien-Zusammenfassung**:

- IKT-Lieferkettenrisiken müssen systematisch identifiziert und bewertet werden
- Sicherheitsanforderungen für IKT-Produkte und -Dienste müssen in der Beschaffung spezifiziert werden
- Sub-Lieferanten (Lieferkettentransparenz) müssen bewertet und offengelegt werden
- Software-Lieferkettensicherheit muss inklusive Abhängigkeiten, Bibliotheken und Open-Source-Komponenten behandelt werden
- Hardware-Lieferkettensicherheit muss einschliesslich Fälschungserkennung berücksichtigt werden
- Lieferkettenresilienz muss für kritische IKT-Dienste geplant werden
- Lieferantenänderungen müssen über Change-Control-Prozesse gemanagt werden

**Richtlinienreferenz**: Siehe ISMS-POL-A.5.19-23-S3 (IKT-Lieferkettensicherheit) für detaillierte Lieferkettenanforderungen.

### A.5.22 – Überwachung, Überprüfung und Änderungsmanagement von Lieferantendiensten

> *Die Organisation sollte die Informationssicherheitspraktiken und die Servicelieferung von Lieferanten regelmässig überwachen, überprüfen, bewerten und Änderungen daran verwalten.*

**Kontrollziel**: Sicherstellung der fortlaufenden Validierung der Lieferantensicherheitslage und kontrolliertes Management von Änderungen an Lieferantendiensten.

**Richtlinienreferenz**: Siehe ISMS-POL-A.5.19-23-S4 (Lieferantenüberwachung & Änderungsmanagement) für detaillierte Governance-Anforderungen.

### A.5.23 – Informationssicherheit bei der Nutzung von Cloud-Diensten

> *Prozesse für die Beschaffung, Nutzung, Verwaltung und den Ausstieg aus Cloud-Diensten sollten in Übereinstimmung mit den Informationssicherheitsanforderungen der Organisation festgelegt werden.*

**Kontrollziel**: Systematisches Management des Cloud-Dienste-Lebenszyklus von der Auswahl bis zum sicheren Ausstieg.

**Richtlinienreferenz**: Siehe ISMS-POL-A.5.19-23-S5 (Cloud-Dienste-Sicherheit) für detaillierte Cloud-spezifische Anforderungen.

---

# Rahmenwerksstruktur

## Zweck

Festlegung verbindlicher Anforderungen für das Management von Informationssicherheitsrisiken im Zusammenhang mit:

- Externen Lieferanten, die Produkte oder Dienste bereitstellen
- Vertragsvereinbarungen mit Lieferanten
- IKT-Lieferkettenabhängigkeiten
- Laufendem Lieferantenbeziehungsmanagement
- Cloud-Dienste-Beschaffung, -betrieb und -ausstieg

## Anwendungsbereich

Dieses Rahmenwerk gilt für:

- Alle Lieferantenbeziehungen mit Zugang zu Organisationsinformationen oder -systemen
- Alle Cloud-Dienste (IaaS, PaaS, SaaS, XaaS-Modelle einschliesslich Sicherheitsdienste, Kollaborationsplattformen, Speicher)
- Alle Vertragsvereinbarungen mit externen Dienstleistern
- Alle IKT-Produkte und -Dienste mit Lieferkettenabhängigkeiten
- Alle Mitarbeitenden, Auftragnehmer und Dritte, die Lieferantenbeziehungen managen

## Ausschlüsse

Dieses Rahmenwerk deckt nicht ab:

- Einmalige Käufe ohne laufende Dienstleistungsbeziehung oder Datenzugriff
- Lieferanten ohne Zugang zu organisatorischen Informationswerten
- Interne Dienstleister (abgedeckt durch separate HR/operative Richtlinien)

---

# Richtliniendokumente

## Richtlinienstruktur

Das Lieferanten- und Cloud-Dienste-Sicherheitsrahmenwerk besteht aus folgenden modularen Dokumenten:

| Dokument-ID | Titel | Primäre Kontrolle(n) | Zweck |
|-------------|-------|----------------------|-------|
| **ISMS-POL-A.5.19-23** | Masterindex | Alle (5.19-23) | Rahmenwerksübersicht und Navigation |
| **ISMS-POL-A.5.19-23-S1** | Grundlagen der Lieferantenbeziehungen | A.5.19 | Risikoklassifizierung und Due Diligence |
| **ISMS-POL-A.5.19-23-S2** | Anforderungen an Lieferantenvereinbarungen | A.5.20 | Vertragsklauseln und SLA-Anforderungen |
| **ISMS-POL-A.5.19-23-S3** | IKT-Lieferkettensicherheit | A.5.21 | Sub-Lieferanten- und Komponentensicherheit |
| **ISMS-POL-A.5.19-23-S4** | Lieferantenüberwachung & Änderungsmanagement | A.5.22 | Überprüfungszyklen und Änderungsverfahren |
| **ISMS-POL-A.5.19-23-S5** | Cloud-Dienste-Sicherheit | A.5.23 | Cloud-Lebenszyklusmanagement |
| **ISMS-POL-A.5.19-23-S6** | Bewertungsmethodik & Automatisierung | Alle (5.19-23) | Programmgesteuerte Dokumentengenerierung |

**Design-Philosophie**: Jedes Dokument ist unabhängig versionierbar, um granulares Änderungsmanagement, gezielte Stakeholder-Reviews und klare Prüfpfade zu ermöglichen.

## Dokumentenhierarchie

```
ISMS-POL-A.5.19-23 (Masterindex) ← Sie befinden sich hier
│
├── S1: Grundlagen der Lieferantenbeziehungen (A.5.19)
│   └── Definiert: Risikokategorien, Klassifizierung, Due Diligence
│
├── S2: Anforderungen an Lieferantenvereinbarungen (A.5.20)
│   └── Definiert: Vertragsklauseln, SLA-Anforderungen, Sicherheitsbedingungen
│
├── S3: IKT-Lieferkettensicherheit (A.5.21)
│   └── Definiert: Sub-Lieferanten-Anforderungen, Komponentensicherheit
│
├── S4: Lieferantenüberwachung & Änderungsmanagement (A.5.22)
│   └── Definiert: Überprüfungszyklen, Prüfrechte, Änderungsverfahren
│
├── S5: Cloud-Dienste-Sicherheit (A.5.23)
│   └── Definiert: Cloud-Lebenszyklus (Auswahl → Umsetzung → Ausstieg)
│
└── S6: Bewertungsmethodik & Automatisierung (Alle Kontrollen)
    └── Definiert: Excel-Arbeitsmappen, Python-Skripte, Validierung

Umsetzungsebene (Separate Dokumente):
├── ISMS-IMP-A.5.19-23.0 (Regulatorische Update-Spezifikation - DORA/NIS2/KI-Act/CLOUD Act)
├── ISMS-IMP-A.5.19-23.1 (Cloud-Dienst-Inventar & Klassifizierung)
├── ISMS-IMP-A.5.19-23.2 (Anbieter-Due-Diligence & Verträge)
├── ISMS-IMP-A.5.19-23.3 (Sichere Konfiguration & Bereitstellung)
└── ISMS-IMP-A.5.19-23.4 (Laufende Governance & Risikomanagement)

Referenzdaten:
└── ISMS-REF-A.5.23 (Cloud-Anbieter-Referenzregister)
```

---

# Bewertungs- & Umsetzungsdokumente

## Bewertungsspezifikationen (Markdown)

Das Rahmenwerk enthält umfassende Bewertungsspezifikationen, die Struktur und Anforderungen für die Excel-Arbeitsmappen-Generierung definieren:

| Dokument-ID | Titel | Zweck | Tabellenblätter |
|-------------|-------|-------|-----------------|
| **ISMS-IMP-A.5.19-23.0** | Regulatorische Update-Spezifikation | DORA, NIS2, KI-Act, CLOUD Act-Erweiterungen | N/A (Spezifikation) |
| **ISMS-IMP-A.5.19-23.1** | Cloud-Dienst-Inventar & Klassifizierung | Massgebliches Inventar mit Datenklassifizierung und Kritikalität | ~10 |
| **ISMS-IMP-A.5.19-23.2** | Anbieter-Due-Diligence & Verträge | Due-Diligence-Kriterien, Vertrags-Sicherheitsklauseln | ~8 |
| **ISMS-IMP-A.5.19-23.3** | Sichere Konfiguration & Bereitstellung | Cloud-Dienst-Konfigurationsbaselines und Bereitstellung | ~8 |
| **ISMS-IMP-A.5.19-23.4** | Laufende Governance & Risikomanagement | Überwachung, Überprüfungszyklen, Vorfallsmanagement | ~8 |

## Generierte Excel-Arbeitsmappen

Wenn Python-Generatoren ausgeführt werden, produzieren sie:

| Arbeitsmappe | Tabellenblätter | Hauptnutzer | Zweck |
|--------------|-----------------|-------------|-------|
| **ISMS_REG_A523_1_Inventory_JJJJMMTT.xlsx** | ~10 | Beschaffung, Sicherheit, IT-Betrieb | Dienst-Inventar, Datenklassifizierung, Ausstiegsmachbarkeit |
| **ISMS_REG_A523_2_DueDiligence_JJJJMMTT.xlsx** | ~8 | Beschaffung, Recht, Sicherheit | Anbieterbewertung, Vertragsprüfung, Sicherheitsklauseln |
| **ISMS_REG_A523_3_Configuration_JJJJMMTT.xlsx** | ~8 | Cloud-Architekten, Sicherheit | Sicherheitskonfigurationsbaselines, Bereitstellungs-Compliance |
| **ISMS_REG_A523_4_Governance_JJJJMMTT.xlsx** | ~8 | IT-Betrieb, Sicherheit | Laufende Überwachung, Änderungsmanagement, Vorfallsverfolgung |

**Gesamte Bewertungsausgabe:** ~34 Tabellenblätter in 4 Arbeitsmappen

## Bewertungsdomänen erklärt

**Domäne 0 – Regulatorische Updates (Spezifikation)**:
Welche regulatorischen Rahmenwerke gelten? (DORA, NIS2, KI-Act) | Welche Jurisdiktionsrisiken bestehen? (US CLOUD Act) | Welche zusätzlichen Felder sind erforderlich?

**Domäne 1 – Cloud-Dienst-Inventar & Klassifizierung**:
Welche Cloud-Dienste existieren? | Welche Daten werden verarbeitet? (Klassifizierung) | Was ist die Servicekritikalität? | Wo befinden sich die Daten? (Datenspeicherort) | Was ist die Ausstiegsmachbarkeit?

**Domäne 2 – Anbieter-Due-Diligence & Verträge**:
Welche Due-Diligence-Prüfung wurde durchgeführt? | Welche Sicherheitsklauseln bestehen in Verträgen? | Welche SLA-Verpflichtungen gibt es? | Was ist die Anbieterjurisdiktion? | Welcher CLOUD Act-Exposition besteht?

**Domäne 3 – Sichere Konfiguration & Bereitstellung**:
Welche Konfigurationsbaselines gelten? | Welche Sicherheitskontrollen sind aktiviert? | Wie wird der Zugriff verwaltet? | Was wird überwacht?

**Domäne 4 – Laufende Governance & Risikomanagement**:
Welcher Überprüfungsplan gilt? | Welche Leistungskennzahlen existieren? | Welche Vorfälle sind aufgetreten? | Welche Änderungen wurden genehmigt? | Welche Risiken werden verfolgt?

**Domäne 5 – Compliance-Überwachungs-Dashboard**:
Was ist der Gesamt-Compliance-Status? (Ampelindikation) | Was sind die wichtigsten KPIs? | Welche Lücken bestehen? | Welcher regulatorische Nachweis liegt vor?

## Bewertungsworkflow

```
┌──────────────────────────────────────────────────────────────┐
│ PHASE 1: GENERIERUNG (Tag 1)                               │
│ • 4 Python-Generatorskripte ausführen                      │
│ • Ergebnis: 4 Excel-Arbeitsmappen mit ~34 Tabellenblättern │
│ • Validierung: Automatisierte Struktur- und Formelprüfung  │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ PHASE 2: BEWERTUNG (Wochen 1-3)                            │
│ • Beschaffung/IT/Sicherheitsteams füllen Arbeitsmappen aus │
│ • Designierte Zellen ausfüllen, Dropdown-Validierungen     │
│ • Lücken dokumentieren, Nachweise bereitstellen            │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ PHASE 3: NORMALISIERUNG (Tag 15)                           │
│ • Normalisierungsskript ausführen                          │
│ • Dateinamen aus dem Überprüfungsprozess standardisieren   │
│ • Audit-Trail-Manifest erstellen                           │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ PHASE 4: EXECUTIVE-REVIEW (Woche 4)                        │
│ • ISB überprüft Dashboard und Risikoregister              │
│ • Behebungsroadmap und Budget genehmigen                   │
│ • Bewertungspaket abzeichnen                               │
│ • An Auditoren liefern (intern/extern/regulatorisch)       │
└──────────────────────────────────────────────────────────────┘
```

---

# Automatisierungsskripte

## Bewertungs-Generator-Skripte

| Skript | Ausgabe-Arbeitsmappe | Zweck |
|--------|---------------------|-------|
| `generate_reg_a523_1_inventory.py` | ISMS-IMP-A.5.19-23.1_Inventory_{JJJJMMTT}.xlsx | Cloud-Dienst-Inventar und Klassifizierung |
| `generate_reg_a523_2_vendor_dd.py` | ISMS-IMP-A.5.19-23.2_VendorDD_{JJJJMMTT}.xlsx | Anbieterbewertung und Vertragsprüfung |
| `generate_reg_a523_3_secure_config.py` | ISMS-IMP-A.5.19-23.3_SecureConfig_{JJJJMMTT}.xlsx | Sichere Konfiguration und Bereitstellung |
| `generate_reg_a523_4_governance.py` | ISMS-IMP-A.5.19-23.4_Governance_{JJJJMMTT}.xlsx | Laufende Überwachung und Risikomanagement |

**Regulatorische Erweiterung**: Alle Generatoren integrieren Felder aus der ISMS-IMP-A.5.19-23.0-Spezifikation für DORA-, NIS2-, KI-Act- und CLOUD-Act-Compliance-Anforderungen.

---

# Rollen & Verantwortlichkeiten

## Führungsrollen

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **ISB** | Gesamtverantwortung, Richtliniengenehmigung, Ausnahmen-Abzeichnung, Risikoakzeptanz, Budgetgenehmigung |
| **Geschäftsleitung** | Strategische Lieferantenentscheidungen, Budgetzuweisung, Risikogovernance |
| **Beschaffungsleiter** | Anbieterauswahl, Vertragsverhandlung, Kostenmanagement |
| **Rechtsabteilung** | Vertragsprüfung, regulatorische Compliance, Vertragsbedingungen, Streitbeilegung |

## Operative Rollen

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **Informationssicherheitsbeauftragter** | Richtlinieneigentümerschaft, Durchsetzung, Compliance-Überwachung, Lieferantenrisikobewertung |
| **Beschaffungsteam** | Anbieterauswahl, Ausschreibungsmanagement, Lieferantenbeziehungsmanagement, Vertragsverwaltung |
| **IT-Betrieb** | Technische Umsetzung, Konfiguration, Überwachung, Änderungsmanagement |
| **Cloud-Architekten** | Cloud-Dienst-Design, Sicherheitskonfiguration, Architekturüberprüfung |
| **Systemeigentümer** | Lieferantenbeziehungen in ihren Bereichen, Geschäftsbegründung, Budgetgenehmigung |

## Unterstützende Rollen

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **Compliance & Audit** | Regulatorische Auslegung (DORA, NIS2, KI-Act), Audit-Unterstützung, Nachweiserhebung |
| **Risikomanagement** | Lieferantenrisikobewertung, Konzentrationsrisikoanalyse, Risikoregisterpflege |
| **Datenschutzbeauftragter (DSB)** | DSGVO Art. 28-Compliance, Auftragsverarbeitungsverträge, Datenschutz-Folgenabschätzungen |
| **Informationssicherheit** | Entwicklung von Bewertungstools, Generatorskripte, Validierungsautomatisierung |
| **Finanzen** | Budgetverfolgung, Kostenanalyse, ROI-Bewertung |

## Benutzerverantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **Alle Mitarbeitenden** | Einhaltung der genehmigten Cloud-Dienstliste, Verbot von Shadow-IT, Vorfallsmeldung |
| **Vorgesetzte** | Budgetgenehmigung für Lieferantendienste, Geschäftsbegründung, Benutzerzugriffsmanagement |

## Kompetenzanforderungen

Personal, das Lieferanten- und Cloud-Sicherheitsbewertungsaktivitäten durchführt, muss folgende Kompetenzanforderungen erfüllen:

**Beschaffungspersonal:**
- Schulung zur Lieferantenrisikobewertung (intern oder gleichwertig)
- Verständnis der Sicherheitsanforderungen für Cloud-Dienste
- Jährliche Auffrischung zu Vertrags-Sicherheitsklauseln

**Cloud-Architekten / Technische Bewerter:**
- Cloud-Sicherheitszertifizierung (CCSP, CCSK oder anbieterspezifisch)
- Verständnis von Modellen der gemeinsamen Verantwortung
- Erfahrung mit Cloud-Sicherheitskonfigurationsüberprüfung

**Rechtsabteilung:**
- Schulung zu DSGVO und Datenschutzrecht
- Verständnis von Auftragsverarbeitungsverträgen (DSGVO Art. 28)
- Vertrautheit mit DORA/NIS2-Anforderungen (wo anwendbar)

**Informationssicherheitsbeauftragter:**
- ISO 27001 Lead Implementer oder gleichwertig
- Schulung zur Risikobewertungsmethodik
- Cloud-Sicherheitsrahmenwerke (CSA CCM, ISO 27017/27018)

---

# Bewertungsmethodik

## Programmgesteuerter Dokumentationsansatz

Dieses Rahmenwerk verwendet **quantitative, evidenzbasierte Bewertung** anstelle subjektiver Beurteilung:

**Kernprinzip**: Was systematisch erstellt werden kann, kann systematisch gepflegt und objektiv verifiziert werden.

**Nachweis-Anforderungen für jeden Lieferantendienst**:

| Nachweistyp | Erforderliche Dokumentation | Mindeststandard |
|-------------|---------------------------|-----------------|
| **Zertifizierung** | SOC 2 Type II, ISO 27001, ISO 27017, CSA STAR | Aktuell (siehe Gültigkeitsregeln) |
| **Vertrag** | Unterzeichnete Vereinbarung mit Sicherheitsklauseln | DSGVO Art. 28 konform mindestens |
| **Konfiguration** | Dokumentation der Sicherheits-Basiseinstellungen | CIS-Benchmark oder Anbieter-Hardening-Leitfaden |
| **Überwachung** | SLA-Leistungsdaten, Vorfallsprotokolle | Mindestens vierteljährlich |
| **Risikobewertung** | Dokumentierte Due Diligence und Risikobewertung | Vom ISB genehmigt |

**Zertifizierungsgültigkeitsregeln:**

| Zertifizierung | Gültigkeitsdauer | Aktualitätsprüfung |
|----------------|-----------------|---------------------|
| **ISO 27001** | 3 Jahre (Zertifikatszykus) | Jährliches Überwachungsaudit bestätigt innerhalb 12 Monate |
| **SOC 2 Type II** | 1 Jahr (Berichtszeitraum) | Berichtsdatum innerhalb 12 Monate |
| **CSA STAR** | 2 Jahre (Stufe 2) | Jährliche Rezertifizierung oder kontinuierliche Überwachung |
| **ISO 27017/27018** | 3 Jahre (ausgerichtet an ISO 27001) | Überwachungsaudit bestätigt innerhalb 12 Monate |

**Ablehnungskriterien**:

- Selbstbewertung des Lieferanten ohne Drittpartei-Validierung
- Abgelaufene Zertifizierungen (über obige Gültigkeitsdauer)
- Verträge ohne Sicherheitsklauseln oder Prüfrechte
- Fehlender Auftragsverarbeitungsvertrag (DSGVO-Verletzung)
- Keine Ausstiegsstrategie oder Daten-Portabilitätsmechanismus

## Lieferantenrisikoklassifizierung

Lieferanten werden mittels **quantitativer Bewertung** über sechs Dimensionen klassifiziert:

| Dimension | Gewichtung | Bewertungskriterien |
|-----------|-----------|---------------------|
| **Datenzugriff** | 25 % | Eingeschränkt=100, Vertraulich=75, Intern=50, Öffentlich=25, Keiner=0 |
| **Servicekritikalität** | 25 % | Kritisch (Stufe 1)=100, Hoch (Stufe 2)=75, Mittel (Stufe 3)=50, Niedrig (Stufe 4)=25 |
| **Ersetzbarkeit** | 15 % | Einzige Quelle=100, Begrenzte Alternativen=75, Mehrere Alternativen=50, Standardware=25 |
| **Integrationstiefe** | 15 % | Tiefe Integration=100, Moderat=75, Gering=50, Keine=25 |
| **Regulatorische Auswirkung** | 10 % | DORA/NIS2 kritisch=100, DSGVO-Verarbeiter=75, Compliance-relevant=50, Keine Auswirkung=25 |
| **Konzentrationsrisiko** | 10 % | >50 % Budget=100, 25-50 %=75, 10-25 %=50, <10 %=25 |

> **Hinweis:** Dimensionsgewichtungen können je nach organisatorischem Kontext angepasst werden. Finanzinstitute, die FINMA, DORA oder ähnlichen Aufsichtsrahmenwerken unterliegen, können das Gewicht **Regulatorische Auswirkung** auf 15-20 % erhöhen.

**Gesamtpunktzahl → Klassifizierung**:

- **Stufe 1 (Kritisch):** 75-100 Punkte → Vierteljährliche Überprüfung, obligatorischer SOC 2 Type II oder ISO 27001, Vor-Ort-Prüfrechte
- **Stufe 2 (Hoch):** 50-74 Punkte → Halbjährliche Überprüfung, Drittpartei-Bescheinigung erforderlich, Remote-Prüfrechte
- **Stufe 3 (Mittel):** 25-49 Punkte → Jährliche Überprüfung, Selbstbewertung mit Stichprobenvalidierung akzeptabel
- **Stufe 4 (Niedrig):** 0-24 Punkte → Zweijährliche Überprüfung, Selbstbewertung akzeptabel

## Compliance-Bewertung

**Gesamt-Compliance-Status** (Ampelmodell):

| Status | Kriterien | Erforderliche Massnahme |
|--------|-----------|-------------------------|
| **Grün (Konform)** | Alle Anforderungen erfüllt, Nachweise aktuell (<12 Monate), keine offenen Befunde | Routineüberwachung |
| **Gelb (Teilweise konform)** | Geringfügige Lücken oder veraltete Nachweise (12-18 Monate), unkritische Befunde | Behebungsplan innerhalb 90 Tage |
| **Rot (Nicht konform)** | Grosse Lücken, fehlende Nachweise, abgelaufene Zertifizierungen (>18 Monate), kritische Befunde | Sofortige Behebung oder Dienstaussetzung |

## Regulatorische Bedingungslogik

Bewertungsarbeitsmappen implementieren **bedingte Feldanzeige** basierend auf regulatorischer Anwendbarkeit:

**DORA-Felder** (angezeigt wenn: Finanzsektor-Unternehmen in der EU):
- IKT-Drittparteien-Risikoregister-Eintrag
- Konzentrationsrisikobewertung
- Ausstiegsstrategiedokumentation
- Genehmigungs-Status der Sub-Auslagerung
- Kooperationsklauseln mit zuständiger Behörde

**NIS2-Felder** (angezeigt wenn: Wesentliche/wichtige Einrichtung in der EU):
- Lieferkettensicherheitsmassnahmen
- 24-Stunden-Vorfallsmeldungsfähigkeit
- Dokumentation der Managementverantwortung
- Jährlicher Cybersicherheitsrisikobericht

**KI-Act-Felder** (angezeigt wenn: KI-System-Anbieter/Betreiber):
- Klassifizierung von Hochrisiko-KI-Systemen
- Status der Konformitätsbewertung
- Transparenzpflichten
- Mechanismen zur menschlichen Aufsicht

**CLOUD-Act-Felder** (angezeigt wenn: US-ansässiger Anbieter):
- Jurisdiktionsrisikobewertung
- Rechtliche Widerspruchsverpflichtungen
- Verschlüsselung und Schlüsselmanagement
- Ergänzende Massnahmen (SCCs, TIA)

---

# Kontrollintegrationsmatrix

## Zusammenspiel der Kontrollen

Dieses Rahmenwerk deckt fünf verwandte Kontrollen ab, die über den Lieferanten-/Cloud-Dienste-Lebenszyklus zusammenwirken:

| Lebenszyklusphase | Primäre Kontrolle | Unterstützende Kontrollen | Wesentliche Aktivitäten |
|-------------------|------------------|--------------------------|------------------------|
| **Identifikation** | A.5.19 | — | Lieferantenentdeckung, Shadow-IT-Identifikation, Inventarerstellung |
| **Risikobewertung** | A.5.19 | A.5.21 | Risikoklassifizierung, Kritikalitätsbewertung, Due-Diligence-Umfang |
| **Auswahl** | A.5.19 + A.5.23 | A.5.21 | Anbieterbewertung, Sicherheitsfragebögen, Proof of Concept |
| **Vertragsabschluss** | A.5.20 | A.5.19, A.5.23 | Vertragsverhandlung, Sicherheitsklauseln, SLA-Definition, Ausstiegsregelungen |
| **Umsetzung** | A.5.23 | A.5.20 | Dienstbereitstellung, Konfiguration, Zugriffsprovisionierung |
| **Betrieb** | A.5.22 | A.5.19, A.5.23 | Leistungsüberwachung, Vorfallsmanagement, Änderungssteuerung |
| **Überprüfung** | A.5.22 | A.5.19, A.5.20, A.5.21 | Periodische Bewertungen, Prüfrechtsausübung, Rezertifizierung |
| **Ausstieg** | A.5.23 | A.5.20 | Datenextraktion, Konfigurationssicherung, Dienstmigration |

## Modell der gemeinsamen Verantwortung

```
┌─────────────────────────────────────────────────────────────────┐
│                    GEMEINSAME VERANTWORTUNG                     │
├─────────────────────────────────────────────────────────────────┤
│  ORGANISATION                    │  LIEFERANT/CSP               │
│  ─────────────────────────────── │  ─────────────────────────── │
│  • Sicherheitsanforderungen def. │  • Vertragsbedingungen erf.  │
│  • Due Diligence durchführen     │  • Zertifizierungen vorlegen │
│  • Verträge prüfen               │  • Vereinbarte Kontrollen    │
│  • Compliance überwachen         │  • Vorfälle melden           │
│  • Zugangskontrollen verwalten   │  • Audits unterstützen       │
│  • Nachweise dokumentieren       │  • SLAs einhalten            │
│  • Ausstiegsstrategie planen     │  • Datenportabilität ermögl. │
│  • Ausstiegsverfahren testen     │  • Übergangssupport leisten  │
│  • Sub-Lieferanten bewerten      │  • Lieferkette offenlegen    │
│  • Regulatorische Compliance     │  • Zertifizierungen pflegen  │
└─────────────────────────────────────────────────────────────────┘
```

**Verantwortungsaufteilung nach Servicemodell:**

| Schicht | IaaS (AWS EC2) | PaaS (Azure App Service) | SaaS (Microsoft 365) |
|---------|----------------|--------------------------|----------------------|
| **Daten** | Organisation | Organisation | Organisation |
| **Anwendung** | Organisation | Organisation | Anbieter |
| **Laufzeitumgebung** | Organisation | Anbieter | Anbieter |
| **Betriebssystem** | Organisation | Anbieter | Anbieter |
| **Virtualisierung** | Anbieter | Anbieter | Anbieter |
| **Server** | Anbieter | Anbieter | Anbieter |
| **Speicher** | Anbieter | Anbieter | Anbieter |
| **Netzwerk** | Geteilt | Anbieter | Anbieter |

---

# Lebenszyklusmanagement

## Lieferanten-Lebenszyklusphasen

**Phase 1: Auswahl & Due Diligence (A.5.19, A.5.21)**
- Geschäftsbedarfsdefinition
- Anbieteridentifikation und Vorauswahl
- Sicherheitsfragebögen verteilen
- Risikobewertung und Klassifizierung
- Technische Evaluierung (POC/Pilot)
- Due-Diligence-Prüfung (Zertifizierungen, Referenzen, finanzielle Stabilität)

**Phase 2: Vertragsabschluss (A.5.20)**
- Vertragsverhandlung mit Sicherheitsklauseln
- Auftragsverarbeitungsvertrag (DSGVO Art. 28)
- SLA-Definition
- Prüfrechtseinrichtung
- Ausstiegsstrategiedokumentation
- Genehmigungg durch Recht und Beschaffung

**Phase 3: Onboarding & Konfiguration (A.5.23)**
- Sicherheits-Baseline-Konfiguration
- Zugriffsprovisionierung (geringstmögliche Berechtigung)
- Einrichtung von Überwachung und Protokollierung
- Integration in Organisationssysteme
- Benutzerschulung und Dokumentation
- Go-Live-Freigabe

**Phase 4: Betrieb & Überwachung (A.5.22)**
- Kontinuierliche Leistungsüberwachung
- SLA-Compliance-Verfolgung
- Periodische Sicherheitsüberprüfungen
- Änderungsmanagement
- Vorfallsreaktion und -lösung
- Beziehungsmanagement

**Phase 5: Überprüfung & Optimierung (A.5.22)**
- Jährliche Vertragsprüfung
- Kosten-Nutzen-Analyse
- Dienstoptimierung
- Neuverhandlung oder Verlängerung
- Alternativenbewertung

**Phase 6: Ausstieg & Übergang (A.5.23)**
- Identifikation von Ausstiegsauslösern
- Datenexport und -validierung
- Dienstmigration oder -ersatz
- Vertragsbeendigung
- Datenlöschungsverifizierung
- Lessons-Learned-Dokumentation

**Anforderungen an Ausstiegsplantests:**
- Ausstiegspläne für **Stufe 1 (Kritisch)** müssen jährlich getestet werden (DORA Art. 28.6 wo anwendbar)
- Ausstiegspläne für **Stufe 2 (Hoch)** müssen alle zwei Jahre oder bei grossen Serviceänderungen getestet werden
- Testergebnisse in ISMS-IMP-A.5.19-23.4 (Governance-Arbeitsmappe) dokumentiert und dem ISB berichtet

## Überprüfungszyklen

| Lieferantenstufe | Überprüfungshäufigkeit | Überprüfungsumfang |
|------------------|----------------------|--------------------|
| **Stufe 1 (Kritisch)** | Vierteljährlich | Vollständige Compliance-Überprüfung, SLA-Leistung, Risiko-Neubewertung, Zertifizierungsstatus |
| **Stufe 2 (Hoch)** | Halbjährlich | Compliance-Stichprobe, SLA-Leistung, Überprüfung grösser Änderungen |
| **Stufe 3 (Mittel)** | Jährlich | Compliance-Validierung, Vertragsverlängerungsbewertung |
| **Stufe 4 (Niedrig)** | Zweijährlich | Vertragsverlängerungsentscheidung, fortbestehender Geschäftsbedarf |

**Auslöserereignisse für Ad-hoc-Überprüfungen**:
- Sicherheitsvorfall beim Lieferanten
- Grosse Serviceänderung oder -migration
- Vertragsänderung oder -verlängerung
- Fusion/Übernahme des Lieferanten
- Regulatorische Änderung mit Auswirkung auf Lieferantenpflichten
- Audit-Befund oder Compliance-Lücke

## Ausnahmenmanagement

**Ausnahmeantragsprozess**:

1. **Antragseinreichung**: Antragsteller dokumentiert Ausnahme mit Geschäftsbegründung
2. **Risikobewertung**: Sicherheitsteam bewertet Risikostufe und mögliche Auswirkungen
3. **Kompensierende Kontrollen**: Mitigationsmassnahmen für genehmigte Ausnahmen identifizieren
4. **Genehmigungsentscheidung**:
   - Niedriges Risiko: Informationssicherheitsbeauftragter
   - Mittleres Risiko: ISB
   - Hohes Risiko: ISB + ITL
   - Kritisches Risiko: Geschäftsleitung
5. **Dokumentation**: Ausnahme mit Genehmigung, Dauer und Überprüfungsdatum erfasst
6. **Überwachung**: Periodische Überprüfung (vierteljährlich für temporäre, jährlich für dauerhafte)
7. **Behebung**: Aktionsplan zum Ausnahmenabschluss bei temporären Ausnahmen

## Shadow-IT-Erkennung

Shadow-IT (nicht autorisierte Cloud-Dienste oder Lieferanten ohne IT/Sicherheits-Genehmigung) muss aktiv erkannt werden:

**Erkennungsmethoden:**
- **Firewall-/Proxy-Protokollanalyse**: Verbindungen zu nicht registrierten SaaS/Cloud-Diensten identifizieren
- **DNS-Abfrageüberwachung**: Auflösung von Domänen nicht im genehmigten Lieferantenregister erkennen
- **Cloud Access Security Broker (CASB)**: Automatisierte Entdeckung von Cloud-Diensten (wo eingesetzt)
- **Spesenabrechnung**: Cloud-Dienst-Abonnements in Beschaffungs-/Finanzunterlagen identifizieren
- **Benutzerselbstmeldung**: Freiwillige Offenlegung durch Awareness-Kampagnen fördern (No-Blame-Richtlinie)

**Erkennungshäufigkeit:**
- Vierteljährliche Shadow-IT-Scans durch IT-Betrieb
- Ergebnisse mit Behebungsempfehlungen dem ISB gemeldet
- Entdeckte Dienste auf Risiko bewertet und entweder in das genehmigte Register aufgenommen oder stillgelegt

---

# Vorfallsmanagement

## Lieferantenvorfall-Kategorien

| Vorfallstyp | Definition | Reaktion |
|-------------|------------|----------|
| **Sicherheitsverletzung** | Unbefugter Zugriff, Datenpanne, Ransomware | Sofortige Eindämmung, forensische Untersuchung, Meldung (DSGVO 72h, NIS2 24h) |
| **Dienstausfall** | Ungeplante Ausfallzeit über SLA | Vorfallsmanagement, Business-Continuity-Aktivierung, Lieferantenkommunikation |
| **Vertragsverletzung** | Lieferant-Nichteinhaltung der Vereinbarung | Eskalation an Recht, Behebungsanforderung, mögliche Kündigung |
| **Leistungsabbau** | SLA-Kennzahl-Unterschreitungen | Leistungsverbesserungsplan, verstärkte Überwachung |
| **Änderungsfehler** | Nicht autorisierte oder fehlgeschlagene Änderung | Rollback-Verfahren, Änderungssteuerungsüberprüfung |

## Benachrichtigungsanforderungen

**Interne Benachrichtigung**:
- Sofort: ISB, Systemeigentümer, IT-Betrieb
- Innerhalb 4 Stunden: Geschäftsleitung (bei kritischen Vorfällen)
- Innerhalb 24 Stunden: DSB (wenn Personendaten betroffen)

**Externe Benachrichtigung**:
- **DSGVO**: Datenschutzbehörde innerhalb 72 Stunden (Art. 33)
- **NIS2**: Zuständige Behörde innerhalb 24 Stunden (Frühwarnung), 72 Stunden (Vorfallsmeldung), 1 Monat (Abschlussbericht)
- **DORA**: Zuständige Behörde gemäss regulatorischem Zeitplan
- **Vertraglich**: Kundenbenachrichtigung gemäss Vertragsbedingungen

**Lieferanten-Benachrichtigungsanforderungen**:

| Vorfallsschwere | Benachrichtigungsfrist des Lieferanten |
|----------------|---------------------------------------|
| **Kritisch** (Datenpanne, Ransomware) | Sofort (innerhalb 4 Stunden nach Bekanntwerden) |
| **Hoch** (Dienstausfall, Sicherheitsereignis) | Innerhalb 24 Stunden |
| **Mittel** (Leistungsabbau, Konfigurationsänderung) | Innerhalb 72 Stunden |
| **Niedrig** (Wartung, geplante Ausfallzeit) | 5 Werktage Vorabbenachrichtigung |

---

# Compliance & Audit

## Obligatorische Anforderungen

Dieses Richtlinienrahmenwerk belegt Compliance mit:

**Primäre Standards:**
- ISO/IEC 27001:2022 Anhang A Kontrollen 5.19-5.23
- ISO/IEC 27002:2022 Kontrollen 5.19-5.23
- ISO/IEC 27036 (Reihe) – Informationssicherheit für Lieferantenbeziehungen

**Cloud-spezifische Standards:**
- ISO/IEC 27017:2015 – Cloud-Sicherheitskontrollen
- ISO/IEC 27018:2019 – Cloud-Datenschutz (Schutz personenbezogener Informationen)
- CSA CCM – Cloud Controls Matrix-Rahmenwerk-Ausrichtung

**Regulatorische Ausrichtung:**
- **Schweizer nDSG**: Auftragsverarbeitungsverträge, Art. 9 Pflichten des Auftragsverarbeiters
- **EU DSGVO**: Art. 28 Auftragsverarbeitungsverträge, Offenlegung von Sub-Verarbeitern
- **DORA**: IKT-Drittparteien-Risikomanagement für EU-Finanzunternehmen
- **NIS2**: Lieferkettensicherheit für wesentliche/wichtige Einrichtungen in der EU
- **EU KI-Act**: Pflichten von KI-System-Anbietern/Betreibern wo anwendbar
- **US CLOUD Act**: Jurisdiktionsrisikobewertung und -minderung

## Audit-Nachweise

**Richtliniendokumentation:**
- Vollständiges Richtlinienrahmenwerk (ISMS-POL-A.5.19-23 und Unterabschnitte S1-S6)
- Genehmigungsprotokolle (ISB, Geschäftsleitung, Recht, Beschaffungsleiter)
- Verteilungsnachweise

**Umsetzungsnachweise:**
- Abgeschlossene Bewertungsarbeitsmappen (4 Excel-Dateien)
- Lieferanteninventar mit Risikobewertungen
- Lieferantenverträge mit markierten Sicherheitsklauseln
- Cloud-Dienste-Vereinbarungen mit SLA und Ausstiegsregelungen

**Operative Nachweise:**
- Protokolle der Lieferantenüberprüfungsbesprechungen
- Vorfallsmeldungen von Lieferanten gemäss Vertragspflichten
- Änderungsmanagementprotokoll
- Lieferantenauditberichte und Befunde
- SLA-Leistungsberichte

---

# Richtlinienpflege

## Überprüfungsplan

**Jährliche Überprüfung:** Umfassende Überprüfung aller Richtlinienabschnitte (empfohlen Q4)

**Ausgelöste Überprüfungen:** Grosse Ereignisse, die sofortige Richtlinienüberprüfung erfordern:
- Bedeutende regulatorische Änderungen
- Grosse Lieferantensicherheitsvorfälle
- Änderungen bei Cloud-Dienstanbietern
- M&A-Aktivitäten der Organisation

## Änderungsprozess

**Standardänderungen:**
1. Änderungsantrag beim Richtlinieneigentümer (ISB) einreichen
2. Folgenabschätzung (betroffene Stakeholder, Lieferanten, Verträge, regulatorische Pflichten)
3. Stakeholder-Konsultation (Beschaffung, Recht, IT-Betrieb, Sicherheit, Compliance, DSB)
4. Überarbeitungsentwurf mit nachverfolgten Änderungen erstellen
5. Überprüfung und Genehmigung
6. Kommunikationsplan ausführen

**Notfallsänderungen:**
- Kritische Lieferantenvorfälle oder regulatorische Fristen können beschleunigten Prozess erfordern
- Notfallgenehmigung durch ISB mit nachträglicher Stakeholder-Überprüfung

---

# Integration mit dem ISMS

## Verwandte Kontrollen

Lieferanten- und Cloud-Dienste-Sicherheit integriert sich mit mehreren ISO 27001-Kontrollen:

| Kontrolle | Integrationspunkt |
|-----------|-------------------|
| **A.5.1** | Richtlinien – Lieferanten-/Cloud-Richtlinie ist Teil der ISMS-Richtliniensammlung |
| **A.5.9** | Inventar – Lieferanten-/Cloud-Dienste im Asset-Inventar verfolgt |
| **A.5.12** | Klassifizierung – Datenklassifizierung bestimmt Lieferantensicherheitsanforderungen |
| **A.5.24-5.28** | Vorfallsmanagement – Lieferantenvorfall-Meldung und -reaktion |
| **A.5.30** | **Business Continuity – Lieferantenunterbrechungsszenarien, alternative Anbieter** ⭐ |
| **A.5.31** | Rechtlich & Regulatorisch – Vertragliche Sicherheitspflichten |
| **A.8.8** | Schwachstellenmanagement – Lieferanten-Patching-Verpflichtungen |
| **A.8.10** | Informationslöschung – Lieferantendatenlöschungsverifizierung bei Ausstieg |
| **A.8.13-14** | **Sicherung & Redundanz – Unabhängige Backups für Cloud-Ausstieg** ⭐ |
| **A.8.24** | Kryptographie – Verschlüsselungsanforderungen für Lieferanten |
| **Klausel 6.1** | Risikobewertung – Lieferantenrisiken im organisatorischen Risikoregister |

## BC/DR-Integration für Ausstiegsszenarien

**Kritisches Prinzip:** Ausstiegsszenarien erfordern **SOWOHL** A.5.19-23 (vertragliche Rechte) ALS AUCH BC/DR (technische Fähigkeit)

| Szenario | A.5.19-23 Anforderung | BC/DR-Fähigkeit | Integration erforderlich |
|----------|----------------------|-----------------|--------------------------|
| **Cloud-Anbieter-Insolvenz** | Kündigungsrechte (A.5.20) | Unabhängige Backups (A.8.13) | ✅ BEIDE |
| **Dienstverschlechterung** | SLA-Durchsetzung (A.5.20) | Failover-Fähigkeit (A.8.14) | ✅ BEIDE |
| **Regulatorische Datensouveränität** | Geografische Einschränkungen (A.5.23) | Alternativstandort (A.8.14) | ✅ BEIDE |
| **Strategischer Cloud-Ausstieg** | Ausstiegsverfahren (A.5.23) | Migrationsfähigkeit (A.5.30) | ✅ BEIDE |
| **Vendor-Lock-in-Bedenken** | Portabilitätsrechte (A.5.23) | Formatunabhängigkeit (A.8.13) | ✅ BEIDE |

---

# Regulatorische Anwendbarkeit

## Stufe 1: Obligatorische Compliance

| Regulierung | Anforderung | Anwendbarkeit |
|-------------|-------------|---------------|
| **Schweizer nDSG** | Sicherheitsmassnahmen des Auftragsverarbeiters (Art. 9), Offenlegung von Sub-Verarbeitern | Alle Personendatenverarbeitungen |
| **EU DSGVO** | Auftragsverarbeitungsverträge (Art. 28), Sicherheitsmassnahmen (Art. 32), Datenpannenmeldung (Art. 33) | Bei Verarbeitung europäischer Personendaten |
| **ISO/IEC 27001:2022** | Kontrollen A.5.19-23 | Zertifizierungsumfang |

## Stufe 2: Bedingte Anwendbarkeit

| Regulierung | Anforderung | Auslösebedingung |
|-------------|-------------|-----------------|
| **FINMA Rundschreiben 2023/1** | Operative Resilienz, Auslagerungsgovernance, Sub-Auslagerungsregister, Vorfallsmeldung | Schweizer FINMA-reguliertes Finanzinstitut |
| **DORA** | IKT-Drittparteien-Risikomanagement (Art. 28-31) | EU-Finanzdienstleistungsunternehmen |
| **NIS2** | Lieferkettensicherheitsmassnahmen (Art. 21), Vorfallsmeldung (Art. 23) | Wesentliche/wichtige Einrichtung |
| **EU KI-Act** | Hochrisiko-KI-System-Anforderungen (Art. 9-15) | Bereitstellung/Betrieb von KI-Systemen in der EU |
| **US CLOUD Act** | Jurisdiktionelle Datenzugriffserwägungen | Nutzung von US-ansässigen Cloud-Anbietern |

**Bestimmung der Anwendbarkeit (Bedingte Vorschriften):**

| Regulierung | Sie unterliegen dieser, wenn... | Bestätigen mit |
|------------|--------------------------------|----------------|
| **DORA** | Ihr Unternehmen ein Kreditinstitut, Zahlungsinstitut, E-Geld-Institut, Versicherungsunternehmen, Wertpapierfirma oder anderes Finanzunternehmen gemäss DORA Art. 2(2) ist | Recht/Compliance |
| **NIS2** | Ihr Unternehmen gemäss NIS2 Anhang I/II als wesentlich oder wichtig eingestuft ist | Recht/Compliance |
| **FINMA** | Ihr Unternehmen von der FINMA als Bank, Versicherungsunternehmen oder Wertpapierfirma lizenziert ist | Recht/Compliance |
| **EU KI-Act** | Ihr Unternehmen KI-Systeme bereitstellt, betreibt oder verwendet, die unter EU KI-Act Anhang III als Hochrisiko eingestuft sind | Recht/Compliance |

> **Mehrere bedingte Vorschriften:** Organisationen, die mehreren bedingten Vorschriften unterliegen, müssen die strengste Anforderung umsetzen, wo Überschneidungen bestehen.

## Stufe 3: Orientierende Hinweise

Best-Practice-Rahmenwerke – nicht obligatorische Compliance-Anforderungen:
- ISO/IEC 27036, ISO/IEC 27017, ISO/IEC 27018
- NIST SP 800-161 (Cybersecurity Supply Chain Risk Management)
- CSA Cloud Controls Matrix (CCM)

## DORA-Spezifische Anforderungen

Für EU-Finanzunternehmen, die DORA unterliegen:

**Art. 28 – IKT-Drittparteien-Risiko**: Umfassendes IKT-Drittparteien-Risikoregister pflegen | Risikobewertung für jeden IKT-Drittanbieter dokumentieren | Konzentrationsrisiken identifizieren

**Art. 29 – Wesentliche Vertragsklauseln**: Volle Kooperation mit zuständigen Behörden | Sub-Beauftragungsanforderungen | Ausstiegsstrategien | SLAs mit Sicherheitskennzahlen | Prüfrechte

**Art. 30 – Sub-Auslagerung**: Register der Sub-Auslagerungsvereinbarungen pflegen | Risiken aus Sub-Auslagerung bewerten

**Art. 31 – IKT-Konzentrationsrisiko**: Konzentrationsrisiko von einzelnen IKT-Drittanbietern bewerten | Abhängigkeiten von kritischen Anbietern dokumentieren

## NIS2-Spezifische Anforderungen

**Art. 21 – Cybersicherheitsrisikomanagement**: Lieferkettensicherheitsmassnahmen | Richtlinien zur IKT-Beschaffung und -Wartung

**Art. 23 – Vorfallsmeldung**: Frühwarnung an CSIRT/zuständige Behörde (24 Stunden) | Vorfallsmeldung (72 Stunden) | Abschlussbericht (1 Monat)

## Datensouveränität & Grenzüberschreitende Erwägungen

| Rahmenwerk | Auswirkung auf Cloud-Dienste |
|-----------|------------------------------|
| **US CLOUD Act** | US-ansässige Anbieter können zur Offenlegung von Daten verpflichtet werden, unabhängig vom Speicherort. Anbieterjurisdiktion bewerten, technische Schutzmassmnahmen implementieren. |
| **EU-Datenbegrenzungsinitiativen** | Einige Anbieter bieten EU-only-Datenverarbeitungsgarantien (AWS European Sovereign Cloud, Azure EU Data Boundary). Vertragliche Verpflichtungen verifizieren. |
| **Schweizer-US-Datenschutzrahmen** | Angemessenheitsmechanismus für US-Übermittlungen. Anbieter-Selbstzertifizierung verifizieren. |
| **Schrems-II-Implikationen** | Zusätzliche Garantien erforderlich für Drittlandübermittlungen: TIA, SCCs, ergänzende technische Massnahmen. |

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Lieferant** | Externe Organisation, die Produkte oder Dienste für [Organisation] bereitstellt und möglicherweise auf Organisationsinformationen zugreift, diese verarbeitet, speichert oder überträgt |
| **Cloud-Dienstanbieter (CSP)** | Lieferant, der Cloud-Computing-Dienste (IaaS, PaaS, SaaS) über ein Netzwerk bereitstellt |
| **IKT-Drittanbieter** | Lieferant kritischer IKT-Produkte oder -Dienste (DORA-Terminologie) |
| **Sub-Verarbeiter** | Eigene Lieferanten des Lieferanten (Sub-Lieferanten), die auf Organisationsdaten zugreifen können |
| **Modell der gemeinsamen Verantwortung** | Aufteilung der Sicherheitsverantwortlichkeiten zwischen Cloud-Dienstanbieter und Kunde |
| **Due Diligence** | Systematische Bewertung der Sicherheitslage des Lieferanten vor dem Engagement |
| **Konzentrationsrisiko** | Risiko durch Abhängigkeit von einem einzigen Lieferanten für kritische Dienste |
| **Vendor-Lock-in** | Abhängigkeit von proprietärer Technologie eines Lieferanten, die Migration kostspielig oder schwierig macht |
| **Ausstiegsstrategie** | Plan für die geordnete Beendigung der Lieferantenbeziehung einschliesslich Datenexport und Dienstmigration |
| **Datenspeicherort** | Geografischer Standort, an dem Daten physisch gespeichert und verarbeitet werden |
| **Datensouveränität** | Rechtliche Anforderung, dass Daten den Gesetzen des Landes unterliegen, in dem sie sich befinden |
| **Transfer Impact Assessment (TIA)** | Bewertung der Angemessenheit des Datenschutzes im Zielland |
| **Standarddatenschutzklauseln (SCCs)** | Von der EU-Kommission genehmigte Vertragsbedingungen für internationale Datenübermittlungen |
| **US CLOUD Act** | US-Gesetz, das US-Unternehmen verpflichtet, Daten an US-Strafverfolgungsbehörden herauszugeben, unabhängig vom Speicherort |
| **DORA** | Digital Operational Resilience Act – EU-Verordnung für IKT-Risikomanagement im Finanzsektor |
| **NIS2** | Netz- und Informationssicherheitsrichtlinie 2 – EU-Richtlinie für Cybersicherheit wesentlicher/wichtiger Einrichtungen |
| **Shadow-IT** | Nicht autorisierte Cloud-Dienste oder Lieferanten, die ohne IT/Sicherheits-Genehmigung genutzt werden |

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **IT-Leiter (ITL)** | [Name] | [Date] |
| **Beschaffungsleiter** | [Name] | [Date] |
| **Rechts-/Compliance-Beauftragter** | [Name] | [Date] |
| **Geschäftsleitung** | [Name] | [Date] |

---

# Nachweise für dieses Richtlinienrahmenwerk

## Stufe-1-Nachweise (Dokumentationsprüfung)

- ✅ Dieses Masterrichtliniendokument (ISMS-POL-A.5.19-23 v1.0)
- ✅ Genehmigungsunterschriften von ISB, ITL, Beschaffungsleiter, Rechts-/Compliance-Beauftragtem, Geschäftsleitung
- ✅ Vollständige Unterrichtliniendokumente (S1-S6)
- ✅ Kontrollausrichtung mit ISO/IEC 27001:2022 A.5.19-23 dokumentiert
- ✅ Lieferantenrisikoklassifizierungsmethodik definiert
- ✅ Compliance-Bewertungsschwellenwerte festgelegt
- ✅ Lebenszyklusmanagementphasen dokumentiert
- ✅ Vorfallsmanagement-Kategorien und Benachrichtigungsanforderungen definiert
- ✅ Rollen und Verantwortlichkeiten mit Kompetenzanforderungen zugewiesen
- ✅ Regulatorischer Anwendbarkeitsrahmen dokumentiert

## Stufe-2-Nachweise (Operative Wirksamkeit)

- **Cloud-Dienst-Inventar**: ISMS-IMP-A.5.19-23.1 Arbeitsmappe mit vollständigem Inventar
- **Anbieter-Due-Diligence-Protokoll**: ISMS-IMP-A.5.19-23.2 Arbeitsmappe
- **Unterzeichnete Verträge mit Sicherheitsklauseln**: Lieferantenvereinbarungen mit DSGVO Art. 28-Bestimmungen
- **Konfigurationsbaselines**: ISMS-IMP-A.5.19-23.3 Arbeitsmappe
- **Protokolle der Lieferantenüberprüfungsbesprechungen**: Dokumentation mit SLA-Leistung, Compliance-Status
- **Laufende Governance-Protokolle**: ISMS-IMP-A.5.19-23.4 Arbeitsmappe
- **Lieferantenzertifizierungsnachweise**: Aktuelle SOC 2 Type II, ISO 27001, CSA STAR-Zertifikate
- **Ausstiegsplantestergebnisse**: Jährliche Ausstiegsstrategievalidierung
- **Konzentrationsrisikobewertungen**: Dokumentierte Analyse kritischer Lieferantenabhängigkeiten
- **Ausnahmenregister**: Genehmigte Ausnahmen mit Geschäftsbegründung und ISB-Abzeichnung

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Dieser Masterindex bietet umfassende Governance für die Lieferanten- und Cloud-Dienste-Sicherheit. Detaillierte Anforderungen für jede Kontrolle sind in den Abschnitten S1-S6 dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-DE:framework:POL:a.5.19-23 -->

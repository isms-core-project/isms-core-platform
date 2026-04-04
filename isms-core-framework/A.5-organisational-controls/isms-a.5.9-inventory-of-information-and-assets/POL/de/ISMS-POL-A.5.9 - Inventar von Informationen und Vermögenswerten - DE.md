<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.9-DE:framework:POL:a.5.9 -->
**ISMS-POL-A.5.9 — Inventar von Informationen und Vermögenswerten**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Inventar von Informationen und Vermögenswerten |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.9 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstversion für ISO 27001:2022-Erstzertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Inkrafttreten + 12 Monate]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Compliance: Rechts-/Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.5.10 bis A.5.18 (Kontrollen zum Asset-Management)
- ISMS-POL-A.8.x (Technische Kontrollen)
- ISMS-IMP-A.5.9.1-UG/TG (Asset-Identifikation und -Entdeckung)
- ISMS-IMP-A.5.9.2-UG/TG (Inventarstruktur und -pflege)
- ISMS-IMP-A.5.9.3-UG/TG (Bewertungsspezifikationen)
- ISMS-IMP-A.5.9.4-UG/TG (Eigentümer-Rechenschaftspflicht-Bewertung)
- ISO/IEC 27001:2022 Kontrolle A.5.9

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an die Führung eines Inventars von Informationen und zugehörigen Vermögenswerten gemäss ISO/IEC 27001:2022 Kontrolle A.5.9 fest.

**Das Grundprinzip**: Man kann nicht schützen, was man nicht zu besitzen weiss. Das Asset-Inventar ist das Fundament, auf dem alle anderen Sicherheitskontrollen aufbauen — Risikobewertung, Zugriffskontrolle, Klassifizierung, Schwachstellenmanagement, Incident Response und Business-Continuity-Planung.

**Geltungsbereich**: Diese Richtlinie gilt für alle Informationsvermögenswerte (Daten, Inhalte, geistiges Eigentum) und zugehörigen Vermögenswerte (IT-Infrastruktur, Anwendungen, physische Einrichtungen, Personalkompetenzen) im Informationssicherheits-Management-Geltungsbereich von [Organisation]. Die Richtlinie legt fest, WAS inventarisiert werden muss, WER rechenschaftspflichtig ist und WIE die Compliance überprüft wird.

**Zweck**: Definition der organisatorischen Anforderungen an die Erstellung, Pflege und Governance des Asset-Inventars. Diese Richtlinie legt den Governance-Rahmen fest (WAS und WARUM). Implementierungsverfahren (WIE) sind gesondert im ISMS-IMP-A.5.9-Paket dokumentiert, und Bewertungswerkzeuge bieten objektive Überprüfungsmechanismen.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert obligatorische Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich Schweizerisches nDSG, EU GDPR und ISO/IEC 27001:2022. Bedingte sektorspezifische Anforderungen (PCI DSS v4.0.1, FINMA, DORA, NIS2, HIPAA) gelten, sofern die Geschäftstätigkeiten von [Organisation] die Anwendbarkeit auslösen.

---

# Kontrollausrichtung und Geltungsbereich

## ISO/IEC 27001:2022 Kontrolle A.5.9

**ISO/IEC 27001:2022 Anhang A.5.9 — Inventar von Informationen und anderen zugehörigen Vermögenswerten**

> *Ein Inventar von Informationen und anderen zugehörigen Vermögenswerten, einschliesslich der Eigentümer, sollte erstellt und gepflegt werden.*

**Kontrollziel (ISO/IEC 27002:2022)**: Identifizierung der Informationen und anderen zugehörigen Vermögenswerte der Organisation, um deren Informationssicherheit zu gewährleisten und angemessene Verantwortlichkeiten zuzuweisen.

**Kontrolltyp**: Organisatorisch
**Informationssicherheitseigenschaften**: Vertraulichkeit, Integrität, Verfügbarkeit
**Cybersicherheitskonzepte**: Identifizieren
**Operative Fähigkeiten**: Asset-Management
**Sicherheitsdomänen**: Governance und Ökosystem

**Diese Richtlinie regelt**:

- Anforderungen an die Identifikation und Klassifizierung von Informationsvermögenswerten
- Inventaranforderungen für zugehörige Vermögenswerte (IT, physisch, Personal)
- Zuweisung der Asset-Eigentümerschaft und Rechenschaftsrahmen
- Standards für Genauigkeit, Vollständigkeit und Aktualität des Inventars
- Organisatorische Rollen und Verantwortlichkeiten für das Asset-Management
- Integration mit anderen ISMS-Kontrollen und Organisationssystemen
- Bewertungsmethodik und Compliance-Überprüfung

## Was diese Richtlinie bewirkt

Diese Richtlinie:

- **Definiert** was einen Informationsvermögenswert und einen zugehörigen Vermögenswert darstellt, der inventarisiert werden muss
- **Legt fest** obligatorische Attribute für Inventareinträge (Eigentümer, Klassifizierung, Standort usw.)
- **Spezifiziert** Anforderungen an die Eigentümerschaftszuweisung und die Rechenschaftspflicht des Eigentümers
- **Setzt** Standards für Genauigkeit, Vollständigkeit und Aktualität der Inventarpflege
- **Identifiziert** organisatorische Rollen und Verantwortlichkeiten für das Asset-Inventar
- **Verweist** auf anwendbare regulatorische Anforderungen gemäss ISMS-POL-00

## Was diese Richtlinie NICHT regelt

Diese Richtlinie regelt NICHT:

- **Technische Implementierungsdetails** (siehe ISMS-IMP-A.5.9 Implementierungsleitfäden)
- **Auswahl von Inventarwerkzeugen** (Technologieentscheidungen basierend auf den Bedürfnissen von [Organisation])
- **Detaillierte Entdeckungsverfahren** (siehe ISMS-IMP-A.5.9-1 Asset-Identifikation)
- **Pflegeworkflows** (siehe ISMS-IMP-A.5.9-2 Inventarpflege)
- **Ersatz der Risikobewertung** (Inventar liefert Input für den Risikobewertungsprozess)

**Begründung**: Die Trennung von Richtlinienanforderungen und Implementierungsleitfaden ermöglicht:

- Richtlinienstabilität trotz organisatorischer Änderungen
- Technische Agilität für Werkzeug- und Prozessaktualisierungen ohne Richtlinienrevision
- Klare Unterscheidung zwischen Governance (Richtlinie) und Ausführung (Implementierung)
- Anpassungsfähigkeit an verschiedene organisatorische Kontexte und Risikoprofile

## Geltungsbereich

**Diese Richtlinie gilt für**:

- Alle Informationsvermögenswerte im ISMS-Geltungsbereich von [Organisation] (Datenbanken, Dokumente, Unterlagen, geistiges Eigentum, Konfigurationsdaten)
- Alle IT-Infrastruktur zur Informationsverarbeitung (Server, Speicher, Netzwerk, Endpunkte)
- Alle Anwendungen und Software (Geschäftsanwendungen, SaaS-Dienste, Entwicklungstools)
- Alle physischen Vermögenswerte zur Informationssicherheitsunterstützung (Einrichtungen, Medien, Geräte)
- Alle personalbezogenen Vermögenswerte, die für den Betrieb kritisch sind (Schlüsselrollen, Spezialkompetenzen)
- Alle Drittanbieterdienste, die Informationen von [Organisation] verarbeiten

**Kategorien im Geltungsbereich**:

1. **Informationsvermögenswerte**: Jegliche Daten, Inhalte oder Kenntnisse mit Wert für [Organisation]

   - Strukturierte Daten (Datenbanken, Data Warehouses)
   - Unstrukturierte Dokumente (Dateien, E-Mails, Berichte)
   - Unterlagen und Archive (regulatorische Aufbewahrung)
   - Geistiges Eigentum (Geschäftsgeheimnisse, Patente, Designs)
   - Konfigurationen und Parameter (Systemkonfigurationen)
   - Authentifizierungs- und kryptografisches Material (Schlüssel, Zertifikate, Anmeldedaten)

2. **Zugehörige Vermögenswerte — IT-Infrastruktur**: Systeme, die Informationen verarbeiten, speichern oder übertragen

   - Physische Server und virtuelle Maschinen
   - Speichersysteme und Backup-Infrastruktur
   - Netzwerkinfrastruktur (Router, Switches, Firewalls, Load Balancer)
   - Endpunkte (Workstations, Laptops, mobile Geräte)
   - Cloud-Infrastruktur und -Dienste

3. **Zugehörige Vermögenswerte — Anwendungen**: Software, die Informationen verarbeitet

   - Geschäftsanwendungen (ERP, CRM, Finanzsysteme)
   - SaaS- und Cloud-Dienste
   - Eigenentwickelte Anwendungen
   - Entwicklungstools und CI/CD-Pipelines
   - APIs und Integrationsplattformen

4. **Zugehörige Vermögenswerte — Physisch**: Materielle Ressourcen zur Betriebsunterstützung

   - Einrichtungen und Rechenzentren
   - Wechseldatenträger (USB-Sticks, Backup-Bänder, portable Laufwerke)
   - Physische Sicherheitsausstattung (Zugangskontrolle, Überwachung)
   - Papierdokumente und gedruckte Materialien

5. **Zugehörige Vermögenswerte — Personal**: Personalressourcen und -kompetenzen

   - Schlüsselrollen (kritisch für den Betrieb)
   - Spezialkompetenzen (einzigartige Fähigkeiten, Zertifizierungen)
   - NICHT individuelle Personendatensätze (Datenschutz-Compliance)

**Nicht im Geltungsbereich**:

- Vermögenswerte im Eigentum von Drittparteien (sofern sie keine Informationen von [Organisation] verarbeiten)
- Persönliche Geräte, die nicht für die Arbeit bei [Organisation] genutzt werden (sofern keine BYOD-Richtlinie gilt)
- Öffentliche Informationen ohne Anforderungen an Vertraulichkeit, Integrität oder Verfügbarkeit
- Büromaterial ohne Sicherheitsauswirkung

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** kategorisiert.

**Stufe 1: Obligatorische Compliance** (gilt für alle Tätigkeiten von [Organisation]):

- **Schweizerisches nDSG (Art. 8)**: Sicherheit personenbezogener Daten erfordert das Wissen, welche Daten vorhanden sind und wo
- **EU GDPR (Art. 5, 32)**: Datenschutz durch Technikgestaltung erfordert ein dokumentiertes Dateninventar
- **ISO/IEC 27001:2022 (Kontrolle A.5.9)**: Explizite Kontrollanforderung für die Zertifizierung

**Stufe 2: Bedingte Anwendbarkeit** (ausgelöst durch spezifische Geschäftstätigkeiten):

- **PCI DSS v4.0.1 (Anf. 2.4, 12.5)**: Inventar der Systemkomponenten in der Karteninhaberdaten-Umgebung
- **HIPAA (164.310(d)(1))**: Inventar und Asset-Kontrollen für Systeme mit Gesundheitsinformationen
- **FINMA**: Risikobasierte Asset-Inventar-Anforderungen für Schweizer Finanzinstitute
- **DORA/NIS2**: IKT-Asset-Inventar für kritische Infrastrukturen und Finanzunternehmen
- **SOX**: IT General Controls erfordern ein dokumentiertes Systeminventar für die Finanzberichterstattung
- **Branchenspezifische Vorschriften**: Können eine spezielle Asset-Kategorisierung erfordern

**Stufe 3: Informative Referenz** (Best Practices, rechtlich nicht bindend):

- **ISO/IEC 19770-1**: Anforderungen an IT-Asset-Management-Systeme
- **ISO 55001**: Asset Management — Anforderungen an Managementsysteme
- **NIST SP 800-53 (CM-8, PM-5)**: Kontrollen für Systemkomponenten und -inventare
- **CIS Controls (1, 2)**: Inventar und Kontrolle von Unternehmens-Assets und Software
- **COBIT 2019 (BAI09)**: Managed-Assets-Framework

Vollständige regulatorische Kategorisierung und Methodik zur Anwendbarkeitsbestimmung: ISMS-POL-00.

---

# Anforderungsrahmen

## Erstellung des Asset-Inventars

**Anforderung A.5.9-R1**: [Organisation] MUSS ein Inventar von Informationen und zugehörigen Vermögenswerten führen.

**Obligatorischer Abdeckungsbereich**:

- Alle Informationsvermögenswerte im ISMS-Geltungsbereich (Datenbanken, Dokumente, geistiges Eigentum, Konfigurationen)
- Alle IT-Infrastruktur zur Informationsverarbeitung (Server, Speicher, Netzwerk, Endpunkte)
- Alle Anwendungen und Dienste (Geschäftsanwendungen, SaaS, APIs, Entwicklungstools)
- Alle physischen Vermögenswerte zur Sicherheitsunterstützung (Einrichtungen, Medien, Geräte)
- Alle personalbezogenen Vermögenswerte, die für den Betrieb kritisch sind (Schlüsselrollen, Kompetenzen)

**Implementierungsansatz**: [Organisation] bestimmt die geeignete Inventarstruktur auf Basis der Risikobewertung. Das Inventar kann aus mehreren spezialisierten Inventaren bestehen (CMDB für IT, HRIS für Personal, Dokumenten-Repositories), sofern sie die Kontrollanforderungen kollektiv erfüllen.

**Überprüfungsmethode**: Vollständigkeitsbewertung gemäss ISMS-IMP-A.5.9-3 (Qualitäts- und Compliance-Bewertung).

## Asset-Kategorisierung

**Anforderung A.5.9-R2**: [Organisation] MUSS Vermögenswerte kategorisieren, um die Anwendung angemessener Sicherheitskontrollen zu ermöglichen.

**Kategorisierungsdimensionen**:

1. **Nach Asset-Typ** (primäre Kategorisierung):

   - Informationsvermögenswerte (was geschützt werden muss)
   - IT-Infrastruktur (Systeme, die Informationen verarbeiten)
   - Anwendungen (Software, die Informationen verarbeitet)
   - Physische Vermögenswerte (materielle Ressourcen)
   - Personalvermögenswerte (Kompetenzen und Rollen)

2. **Nach Kritikalität** (für risikobasierte Behandlung):

   - Kritisch: Verlust würde schwerwiegende Geschäftsauswirkungen verursachen (Betriebsunterbrechung, Regulierungsverstoss)
   - Hoch: Verlust würde erhebliche Geschäftsauswirkungen verursachen (finanzieller Verlust, Reputationsschäden)
   - Mittel: Verlust würde moderate Geschäftsauswirkungen verursachen (Effizienzminderung, Unannehmlichkeiten für Kunden)
   - Niedrig: Verlust würde minimale Geschäftsauswirkungen verursachen (geringfügige Unannehmlichkeiten, leicht ersetzbar)

3. **Nach Lebenszyklus-Status** (für Wartungsplanung):

   - Aktiv: Im Produktionseinsatz
   - Entwicklung: Wird entwickelt oder getestet
   - Wartung: Für Aktualisierungen oder Patches vorgesehen
   - Pensioniert: Für die Ausserbetriebnahme geplant
   - Archiviert: Für Compliance-Zwecke aufbewahrt, aber nicht aktiv genutzt

**Entscheidungshilfe**: Anhang A bietet einen Entscheidungsrahmen und Beispiele zur Kategorisierung.

**Überprüfungsmethode**: Kategorienzuweisungen werden im Rahmen des Asset-Eigentümer-Bestätigungsprozesses gemäss ISMS-IMP-A.5.9-4 überprüft.

## Obligatorische Inventarattribute

**Anforderung A.5.9-R3**: [Organisation] MUSS obligatorische Attribute für jeden inventarisierten Vermögenswert dokumentieren.

**Kernattribute** (für alle Vermögenswerte erforderlich):

| Attribut | Beschreibung | Zweck | Überprüfung |
|----------|-------------|-------|-------------|
| **Asset-ID** | Eindeutige Kennung | Nachverfolgbarkeit zwischen Systemen | Automatisch (systemgeneriert) |
| **Asset-Name** | Menschenlesbarer Name | Kommunikation und Berichterstattung | Eigentümer-Verifizierung |
| **Asset-Typ** | Kategorie gemäss Abschnitt 2.2 | Kontrollanwendbarkeit | Kategorievalidierung |
| **Eigentümer** | Rechenschaftspflichtige Person (bei Informationsvermögenswerten ist dies der „Dateneigentümer" in GDPR-Terminologie — die geschäftlich verantwortliche Partei) | Verantwortungszuweisung | Eigentümer-Bestätigung |
| **Verwalter** | Tagesverantwortlicher (kann vom Eigentümer abweichen) — technische Partei, die Infrastruktur/Systeme verwaltet | Operative Verantwortung | Verwalter-Bestätigung |
| **Beschreibung** | Zweck und Funktion | Verständnis und Kontext | Eigentümer-Verifizierung |
| **Standort** | Physischer oder logischer Standort | Asset-Tracking, Datenspeicherort | Physische Überprüfung |
| **Status** | Lebenszyklus-Status gemäss Abschnitt 2.2 | Wartungsplanung | Status-Workflow |
| **Kritikalität** | Geschäftsauswirkung gemäss Abschnitt 2.2 | Risikoprioritisierung | Risikobewertungs-Abgleich |
| **Erstellungsdatum** | Anschaffungs-/Erstellungsdatum | Asset-Alterserfassung | Dokumentationsverifizierung |
| **Zuletzt aktualisiert** | Letzte Änderung des Eintrags | Aktualitätsnachverfolgung | Automatischer Zeitstempel |
| **Zuletzt geprüft** | Letzte Überprüfung durch Eigentümer | Genauigkeitssicherung | Eigentümer-Bestätigung |
| **Nächstes Prüfdatum** | Geplante Überprüfung | Proaktive Wartung | Prüfungsplan |

**Spezifische Attribute für Informationsvermögenswerte**:

| Attribut | Beschreibung | Zweck |
|----------|-------------|-------|
| **Datenklassifizierung** | Vertraulichkeits-/Integritäts-/Verfügbarkeitsstufe gemäss A.5.12 | Auswahl von Sicherheitskontrollen |
| **Datenformat** | Dateiformat, Schema, Struktur | Technische Kompatibilität |
| **Speicherort(e)** | Physischer Speicherort der Daten | Compliance bzgl. Datenspeicherort |
| **Aufbewahrungsfrist** | Gesetzliche/geschäftliche Aufbewahrungsanforderung | Compliance, Speicherplanung |
| **Gesetzliche/Regulatorische Anforderungen** | Anwendbare Vorschriften | Compliance-Tracking |
| **Verwandte Systeme** | Systeme, die auf diese Informationen zugreifen | Abhängigkeitsanalyse |
| **Verschlüsselungsstatus** | Im Ruhezustand, bei der Übertragung oder beides | Überprüfung des kryptografischen Schutzes |

**Spezifische Attribute für IT-Infrastruktur**:

| Attribut | Beschreibung | Zweck |
|----------|-------------|-------|
| **Hersteller/Lieferant** | Hersteller des Vermögenswerts | Supportverträge, Kompatibilität |
| **Modell/Version** | Spezifische Produktversion | Patch-Management, EOL-Nachverfolgung |
| **Seriennummer/Asset-Tag** | Physische Kennung | Physische Asset-Verifizierung |
| **IP-Adresse/Hostname** | Netzwerkkennung | Netzwerkverwaltung |
| **Konfigurationsbasislinie** | Referenz für Standardkonfiguration | Konfigurationsmanagement (A.8.9) |
| **Abhängigkeiten** | Für den Betrieb erforderliche Vermögenswerte | Auswirkungsbeurteilung |
| **Unterstützte Informationen** | Verarbeitete Informationsvermögenswerte | Klassifizierungsvererbung |

**Optionale Attribute**: [Organisation] kann das Inventar um zusätzliche Attribute erweitern (Anschaffungskosten, Garantiedaten, Energieverbrauch, Compliance-Zertifizierungen), sofern dies keinen übermässigen Pflegeaufwand verursacht.

**Überprüfungsmethode**: Attributvollständigkeit geprüft gemäss ISMS-IMP-A.5.9-3.

## Asset-Eigentümerschaft

**Anforderung A.5.9-R4**: [Organisation] MUSS jedem inventarisierten Vermögenswert einen Eigentümer zuweisen.

**Eigentümerschaftsprinzipien**:

- **Universelle Zuweisung**: Jeder Vermögenswert MUSS einen zugewiesenen Eigentümer haben (keine Ausnahmen)
- **Rechenschaftspflicht**: Der Eigentümer ist während des gesamten Lebenszyklus für den Vermögenswert verantwortlich
- **Delegation zulässig**: Der Eigentümer darf Verwalterpflichten delegieren, bleibt aber rechenschaftspflichtig
- **Bestätigung erforderlich**: Eigentümer müssen die Eigentümerschaft und ihre Verantwortlichkeiten bestätigen
- **Änderungsmanagement**: Eigentümerwechsel lösen eine Inventaraktualisierung aus

**Verantwortlichkeiten des Eigentümers**:

- Vermögenswert gemäss Geschäftswert und Risiko klassifizieren
- Sicherstellen, dass angemessene Sicherheitskontrollen angewendet werden
- Inventareinträge mindestens jährlich auf Richtigkeit überprüfen
- Zugriffsanfragen auf eigene Vermögenswerte genehmigen
- Sicherheitsvorfälle, die eigene Vermögenswerte betreffen, melden
- An Asset-Lebenszyklusentscheidungen teilnehmen (Ausserbetriebnahme, Archivierung)
- Regulatorische Anforderungen, die eigene Vermögenswerte betreffen, kennen

**Bei unklarer Eigentümerschaft**:

1. Innerhalb von 5 Werktagen nach der Asset-Entdeckung an die zuständige Führungsebene eskalieren
2. Temporäre Verwalterzuweisung dokumentieren (operative Verantwortung während des Bestimmungszeitraums)
3. Frist für die dauerhafte Eigentümerbestimmung festlegen:
   - **Initialer Bestimmungszeitraum**: 30 Kalendertage
   - **Verlängerung möglich**: Bis zu 90 Kalendertage mit ISB-Genehmigung, wenn die Eigentümerschaft eine funktionsübergreifende Lösung erfordert (Begründung und kompensierende Kontrollen dokumentieren: zugewiesener Verwalter überwacht den Vermögenswert, Sicherheitsvorfälle werden sofort eskaliert)
4. Vermögenswerte ohne Eigentümer nach 90 Tagen erfordern die Genehmigung der Geschäftsleitung als formelle Ausnahme (Abschnitt 3.4)

Eskalationen wegen eigentümerlosen Vermögenswerten werden im Ausnahmenregister nachverfolgt. Ziel: ≥95 % der Vermögenswerte innerhalb von 30 Tagen einem dauerhaften Eigentümer zugewiesen, 100 % innerhalb von 90 Tagen.

**Überprüfungsmethode**: Vollständigkeit der Eigentümerzuweisung (Ziel: 100 %) gemäss ISMS-IMP-A.5.9-4 verifiziert.

## Qualitätsstandards des Inventars

**Anforderung A.5.9-R5**: [Organisation] MUSS die Inventarqualität durch Standards für Genauigkeit, Vollständigkeit und Aktualität aufrechterhalten.

### Vollständigkeit

**Standard**: Das Inventar muss alle Vermögenswerte im Geltungsbereich umfassen.

**Überprüfungsansatz**:

- Periodische Entdeckungsscans und Abgleich
- Kreuzvalidierung mit anderen Systemen (CMDB, Beschaffung, HR)
- Stichprobentests auf fehlende Vermögenswerte
- Management-Bestätigung

**Zulässige Granularität**: Wird durch Asset-Kritikalität und -Risiko bestimmt. Hochwertige/Hochrisiko-Vermögenswerte erfordern detaillierte Einzeleinträge. Niedrigrisiko-Standardvermögenswerte können gruppiert werden (z. B. „Standard-Mitarbeiterlaptops — Anzahl 50" vs. individuelle Seriennummern).

**Erstzertifizierungsziel**: 85 % Vollständigkeit für kritische Vermögenswerte, 80 % für Standardvermögenswerte, bewertet innerhalb von 90 Tagen nach Richtliniengenehmigung via Basisinventarbewertung (ISMS-IMP-A.5.9-1).

**Reifezustandsziel** (erreicht innerhalb von 12 Monaten nach Zertifizierung): 95 % Vollständigkeit für kritische, 90 % für Standardvermögenswerte. Fortschritt quartalsweise im Summary Dashboard nachverfolgt.

### Genauigkeit

**Standard**: Inventardaten müssen den tatsächlichen Zustand der Vermögenswerte korrekt widerspiegeln.

**Überprüfungsansatz**:

- Regelmässige Überprüfungen durch Asset-Eigentümer (mindestens jährlich)
- Statistische Stichproben zur Datengenauigkeitsvalidierung
- Automatisierte Validierung, sofern technisch machbar
- Vorfall-basierte Verifizierung (Inventar wird bei Vorfällen überprüft)

**Genauigkeitsziele bei Erstzertifizierung** (Basislinie + 90 Tage):

- Informationsvermögenswerte: 85 % Genauigkeit
- IT-Infrastruktur: 90 % Genauigkeit
- Physische Vermögenswerte: 80 % Genauigkeit
- Personalvermögenswerte: 95 % Genauigkeit

**Genauigkeitsziele im Reifezustand** (innerhalb von 12 Monaten nach Zertifizierung):

- Informationsvermögenswerte: 95 % Genauigkeit
- IT-Infrastruktur: 98 % Genauigkeit
- Physische Vermögenswerte: 90 % Genauigkeit
- Personalvermögenswerte: 100 % Genauigkeit

Genauigkeitsverbesserung quartalsweise nachverfolgt. Stichprobenmethodik in ISMS-IMP-A.5.9-3 definiert.

### Aktualität

**Standard**: Das Inventar muss den aktuellen Zustand widerspiegeln, nicht den historischen.

**Aktualisierungsauslöser**:

- Asset-Erstellung (Neubeschaffung, Entwicklung)
- Asset-Änderung (Konfigurationsänderung, Standortwechsel)
- Asset-Entsorgung (Ausserbetriebnahme, Löschung)
- Eigentümerwechsel
- Klassifizierungsänderung
- Geplante periodische Überprüfung

**Maximale Veraltung** (Aktualisierungsauslöser — wie schnell das Inventar nach einem Änderungsereignis aktualisiert wird):

- Kritische Vermögenswerte: Echtzeit- oder tägliche Aktualisierungen
- Hochrisiko-Vermögenswerte: Aktualisierungen innerhalb von 3 Werktagen
- Standardvermögenswerte: Aktualisierungen innerhalb von 1 Woche
- Niedrigrisiko-Vermögenswerte: Aktualisierungen innerhalb von 1 Monat
- Alle Vermögenswerte: Mindestens jährlich überprüft

**Klarstellung**: Maximale Veraltung bezieht sich auf **Aktualisierungsauslöser** (wie schnell das Inventar nach einem Änderungsereignis aktualisiert wird). Der nachstehende Überprüfungsplan bezieht sich auf **proaktive Eigentümerüberprüfung** (periodische Bestätigung). Kritische Vermögenswerte erfordern prompte Aktualisierungen bei Änderungen (täglich) UND geplante Eigentümerüberprüfungen, um unbemerkte Abweichungen zu erkennen.

**Integrationsanforderung**: Das Asset-Inventar MUSS in Change-Management-Prozesse integriert werden (Änderungen lösen automatische Inventaraktualisierungen aus, sofern technisch machbar).

### Überprüfungsplan

| Asset-Kategorie | Überprüfungshäufigkeit | Verantwortliche Rolle | Überprüfungsmethode |
|-----------------|----------------------|----------------------|---------------------|
| Kritische Informationen | Quartalsweise | Informationseigentümer | Eigentümer-Bestätigung + Stichproben |
| Hochrisiko-IT-Infrastruktur | Quartalsweise | Systemeigentümer | Automatisierter Scan + manuelle Verifizierung |
| Standardvermögenswerte | Halbjährlich | Asset-Eigentümer | Eigentümerüberprüfung + Stichproben |
| Niedrigrisiko-Vermögenswerte | Jährlich | Asset-Eigentümer | Eigentümer-Bestätigung |
| Alle Personalvermögenswerte | Quartalsweise | HR + Abteilungsleiter | HR-Systemabgleich |

**Überprüfungsmethode**: Aktualitäts- und Genauigkeitsmetriken gemäss ISMS-IMP-A.5.9-3 nachverfolgt.

## Integrationsanforderungen

**Anforderung A.5.9-R6**: [Organisation] MUSS das Asset-Inventar mit anderen ISMS-Prozessen und Organisationssystemen integrieren.

**Obligatorische Integrationspunkte**:

| ISMS-Kontrolle/Prozess | Integrationsanforderung | Zweck |
|------------------------|------------------------|-------|
| **A.5.12 (Informationsklassifizierung)** | Klassifizierung für Informationsvermögenswerte vergeben | Auswahl von Sicherheitskontrollen |
| **A.5.13 (Kennzeichnung)** | Kennzeichen verweisen auf Inventarklassifizierung | Sichtbare Sicherheitskennzeichnung |
| **A.5.15 (Zugriffskontrolle)** | Zugriffsregeln auf Basis von Asset-Eigentümerschaft und -klassifizierung | Autorisierungsentscheidungen |
| **A.5.18 (Zugriffsrechte)** | Zugriffsrechte durch Asset-Eigentümer genehmigt | Durchsetzung der Rechenschaftspflicht |
| **A.8.x (Technische Kontrollen)** | Technische Kontrollen schützen inventarisierte Vermögenswerte | Kontroll-Asset-Mapping |
| **Risikomanagement (Klausel 6)** | Inventar liefert Input für die Risikobewertung | Identifikation von Bedrohungs-Asset-Schwachstellen |
| **Änderungsmanagement** | Änderungen lösen Inventaraktualisierungen aus | Aktualitätspflege |
| **Incident-Management** | Vorfälle referenzieren betroffene Vermögenswerte | Auswirkungsbeurteilung |
| **Business Continuity** | Identifizierung kritischer Vermögenswerte für BCP/DRP | Priorisierung |

**Integration in Organisationssysteme**:

| System | Integrationszweck | Synchronisation |
|--------|------------------|----------------|
| **CMDB (Configuration Management Database)** | Quelle für IT-Asset-Inventar | Bidirektional (sofern technisch machbar) |
| **Beschaffung/Finanzen** | Nachverfolgung der Asset-Anschaffung | Eingehend (Beschaffung → Inventar) |
| **HR-System** | Validierung von Personalvermögenswerten | Eingehend (HR → Inventar für Rollen/Kompetenzen) |
| **Asset-Management-System** | Physisches Asset-Tracking | Bidirektional |
| **Dokumentenmanagement** | Informationsvermögenswert-Repository | Eingehend (DMS → Inventar-Metadaten) |

**Integrationsreife-Ansatz**: Integrationsanforderungen sind **phasenweise** auf Basis der Systemreife der Organisation:

**Phase 1 — Erstzertifizierung** (minimale Integrationsanforderung):

- CMDB: Falls CMDB vorhanden, quartalsweiser manueller Export/Abgleich. Falls keine CMDB vorhanden, IT-Infrastruktur in dedizierter Asset-Datenbank mit quartalsweiser Validierung gegen Beschaffungsunterlagen und Netzwerk-Entdeckungsscans nachverfolgt.
- HRIS: Quartalsweiser manueller Abgleich von Personalvermögenswerten (kritische Rollen/Kompetenzen) gegen HR-Unterlagen.
- Beschaffung: Jährliche Überprüfung der Beschaffungsunterlagen auf neue Asset-Zugänge; neue Vermögenswerte innerhalb von 30 Tagen nach Beschaffungsgenehmigung ins Inventar aufgenommen.
- Dokumentenmanagement: Informationsvermögenswerte via Metadaten-Exporte aus dem Dokumenten-Repository identifiziert (quartalsweise).

**Phase 2 — Reifezustand** (innerhalb von 18 Monaten nach Zertifizierung):

- Bidirektionale automatisierte Synchronisation, sofern technisch machbar (CMDB ↔ Inventar, HRIS → Inventar).
- Echtzeit-Beschaffungsintegration (neue Asset-Einträge automatisch aus genehmigten Bestellungen erstellt).
- Automatisierte Entdeckungsscans (wöchentlich) mit Abgleich-Alerts.

Fortschritt der Phasen in ISMS-IMP-A.5.9-2 dokumentiert. Aktuelle Phase quartalsweise im Summary Dashboard bewertet.

**Überprüfungsmethode**: Integrationswirksamkeit gemäss ISMS-IMP-A.5.9-2 und ISMS-IMP-A.5.9-3 bewertet.

---

# Governance und Compliance

## Rollen und Verantwortlichkeiten

**3.1.1 Geschäftsleitung**

**Strategische Rechenschaftspflicht**:

- Genehmigung der Asset-Inventar-Richtlinie und wesentlicher Änderungen
- Bereitstellung von Ressourcen für die Inventarimplementierung und -pflege
- Empfang jährlicher Inventar-Compliance-Berichte
- Sicherstellung einer Organisationskultur, die Asset-Rechenschaftspflicht unterstützt

**Spezifische Aufgaben**:

- Genehmigung der RACI-Matrix für die Asset-Inventar-Governance
- Lösung von auf Geschäftsbereichsebene eskalierter Eigentümerschaftsstreitigkeiten
- Genehmigung von Ausnahmen von Inventaranforderungen (selten, dokumentiert)

**3.1.2 Informationssicherheitsbeauftragter (ISB)**

**Operative Rechenschaftspflicht**:

- Eigentümerschaft der Asset-Inventar-Richtlinie und des Rahmens
- Definition von Inventaranforderungen und Qualitätsstandards
- Überwachung der Compliance mit Inventaranforderungen
- Berichterstattung über Inventar-Compliance-Status an die Geschäftsleitung
- Koordination mit anderen Kontrolleigentümern (Klassifizierung A.5.12, Zugriffskontrolle A.5.15)

**Spezifische Aufgaben**:

- Genehmigung des Inventar-Kategorisierungsrahmens
- Definition von Genauigkeits-, Vollständigkeits- und Aktualitätszielen
- Überprüfung und Genehmigung von Bewertungsergebnissen
- Eskalation wesentlicher Lücken an die Geschäftsleitung
- Bewusstsein für regulatorische Änderungen, die das Inventar betreffen

**3.1.3 Informationssicherheitsmanager**

**Taktische Implementierung**:

- Implementierung des Asset-Inventar-Rahmens
- Durchführung periodischer Inventarbewertungen
- Bereitstellung von Leitlinien für Asset-Eigentümer und -Verwalter
- Nachverfolgung und Berichterstattung über Metriken (Vollständigkeit, Genauigkeit, Eigentümerzuweisung)
- Koordination periodischer Überprüfungs- und Validierungsaktivitäten

**Spezifische Aufgaben**:

- Generierung von Bewertungsarbeitsbüchern
- Durchführung des Eigentümer-Bestätigungsprozesses
- Durchführung von Stichproben und Validierungsaktivitäten
- Pflege von Bewertungsnachweisen
- Vorbereitung von Compliance-Berichten für den ISB

**3.1.4 IT-Betrieb / Infrastrukturteams**

**IT-Asset-Management**:

- Pflege des IT-Infrastruktur-Inventars (Server, Speicher, Netzwerk, Endpunkte)
- Integration des Inventars mit der CMDB
- Durchführung automatisierter Entdeckungsscans
- Aktualisierung des Inventars bei IT-Asset-Lebenszyklusereignissen
- Unterstützung der Inventarvalidierung und des Abgleichs

**3.1.5 Anwendungseigentümer / Systemeigentümer**

**Anwendungs-Asset-Management**:

- Pflege des Anwendungs- und Systeminventars
- Dokumentation von Anwendungsabhängigkeiten und Informationsflüssen
- Klassifizierung von Anwendungen gemäss Kritikalitätsrahmen
- Aktualisierung des Inventars bei Anwendungsänderungen (Versionen, Konfigurationen, Ausserbetriebnahmen)
- Sicherstellen, dass Anwendungs-zu-Informationsvermögenswert-Beziehungen dokumentiert sind

**3.1.6 Informationseigentümer / Dateneigentümer**

**Eigentümerschaft von Informationsvermögenswerten**:

- Eigentümerschaft zugewiesener Informationsvermögenswerte über den gesamten Lebenszyklus
- Klassifizierung von Informationen gemäss A.5.12 (Informationsklassifizierung)
- Überprüfung der Inventareinträge für Informationsvermögenswerte mindestens jährlich
- Genehmigung des Zugangs zu eigenen Informationen
- Teilnahme an Informationsrisikobewertungen
- Entscheidungen über Aufbewahrung und Entsorgung gemäss A.8.10 (Informationslöschung)

**3.1.7 Asset-Verwalter**

**Tagesmanagement von Vermögenswerten**:

- Durchführung operativer Aufgaben, die vom Asset-Eigentümer delegiert wurden
- Aufrechterhaltung von Asset-Verfügbarkeit und -Integrität
- Aktualisierung von Inventareinträgen bei routinemässigen Änderungen
- Meldung von Problemen an den Asset-Eigentümer
- Implementierung von Sicherheitskontrollen gemäss Eigentümer-Anweisungen

**Unterschied**: Verwalter haben operative Verantwortung, aber die Rechenschaftspflicht verbleibt beim Eigentümer.

**3.1.8 Alle Mitarbeitenden**

**Nutzerverantwortlichkeiten**:

- Sofortige Meldung verloren gegangener, gestohlener oder beschädigter Vermögenswerte
- Einhaltung der Richtlinien zur akzeptablen Nutzung für zugewiesene Vermögenswerte
- IT-Betrieb bei Asset-Änderungen benachrichtigen (Hardware, Software)
- Rückgabe von Vermögenswerten beim Ausscheiden oder Rollenwechsel
- Teilnahme an periodischen Asset-Überprüfungen auf Anfrage

**3.1.9 Interne Revision / Compliance**

**Unabhängige Verifizierung**:

- Durchführung unabhängiger Inventaraudits
- Verifizierung der Compliance mit Richtlinienanforderungen
- Prüfung der Kontrollwirksamkeit (Genauigkeit, Vollständigkeit, Eigentümerzuweisung)
- Berichterstattung der Ergebnisse an Geschäftsleitung und ISB
- Empfehlung von Verbesserungen am Inventarrahmen

## RACI-Matrix

**Asset-Inventar-Governance**:

| Aktivität | Geschäftsltg. | ISB | InfoSec Mgr | IT-Betr. | App-Eigent. | Info-Eigent. | Verwalter | Nutzer | Revision |
|-----------|--------------|------|-------------|---------|------------|-------------|----------|--------|---------|
| **Richtliniengenehmigung** | A | V | B | I | I | I | I | I | B |
| **Rahmendesign** | I | A | V | B | B | B | I | I | B |
| **Asset-Identifikation** | I | I | B | V | V | V | B | I | I |
| **Eigentümerzuweisung** | I | A | B | B | B | V | I | I | I |
| **Eintrags-Erstellung** | I | I | B | V | V | B | B | I | I |
| **Eintrags-Pflege** | I | I | B | V | V | V | V | I | I |
| **Genauigkeitsprüfung** | I | I | B | B | V | V | B | I | I |
| **Compliance-Bewertung** | I | A | V | B | B | B | I | I | B |
| **Lückenbeseitigung** | B | A | V | V | V | V | B | I | I |
| **Berichterstattung** | I | A | V | B | B | I | I | I | B |
| **Unabhängige Prüfung** | I | I | B | I | I | I | I | I | A/V |
| **Ausnahmengenehmigung** | A | V | B | I | B | B | I | I | B |

**Legende**: V = Verantwortlich (führt die Arbeit durch), A = Accountable (Letztentscheid), B = Beratend (Input eingeholt), I = Informiert (auf dem Laufenden gehalten)

## Bewertung und Verifizierung

**Anforderung A.5.9-R7**: [Organisation] MUSS periodische Bewertungen zur Verifizierung der Inventar-Compliance durchführen.

**Bewertungsrahmen** (5 Domänen):

| Bewertungsdomäne | Dokument-ID | Bewertungsschwerpunkt | Häufigkeit |
|-----------------|-------------|----------------------|-----------|
| **Asset-Identifikation und -Entdeckung** | ISMS-IMP-A.5.9-1 | Entdeckungsverfahren, Vollständigkeit | Quartalsweise |
| **Inventarpflege** | ISMS-IMP-A.5.9-2 | Struktur, Aktualisierungsverfahren, Integration | Quartalsweise |
| **Qualität und Compliance** | ISMS-IMP-A.5.9-3 | Genauigkeits-, Vollständigkeits-, Aktualitätsverifizierung | Quartalsweise |
| **Eigentümer-Rechenschaftspflicht** | ISMS-IMP-A.5.9-4 | Eigentümerzuweisung, Bestätigung, Schulung | Quartalsweise |

**Bewertungswerkzeuge**: Excel-basierte Arbeitsbücher, die aus Python-Skripten generiert werden, bieten:

- Strukturierte Datenerfassung
- Automatisierte Compliance-Berechnungen
- Lückenidentifizierung
- Nachweisregister
- Trend-Tracking

**Implementierungshinweis**: Detaillierte Bewertungsspezifikationen, Nutzerhandbücher und Python-Skript-Generatoren sind in der ISMS-IMP-A.5.9-Serie dokumentiert.

**Compliance-Metriken**:

| Metrik | Ziel | Messmethode | Berichtshäufigkeit |
|--------|------|-------------|------------------|
| **Vollständigkeit** | ≥95 % für Kritisch, ≥90 % für Standard | Entdeckungsabgleich | Quartalsweise |
| **Genauigkeit** | ≥95 % Information, ≥98 % IT-Infrastruktur | Statistische Stichproben | Quartalsweise |
| **Aktualität** | ≥98 % innerhalb der Veraltungsschwellenwerte | Prüfdatumsanalyse | Monatlich |
| **Eigentümerzuweisung** | 100 % | Prüfung auf leere Eigentümerfelder | Monatlich |
| **Eigentümer-Bestätigung** | ≥95 % innerhalb von 30 Tagen | Bestätigungs-Tracking | Monatlich |
| **Einhaltung des Überprüfungsplans** | ≥90 % pünktliche Überprüfungen | Termintreue-Analyse | Quartalsweise |

## Ausnahmenmanagement

**Anforderung A.5.9-R8**: [Organisation] MUSS einen formellen Ausnahmeprozess für Abweichungen von Inventaranforderungen einrichten.

**Ausnahmekategorien**:

1. **Granularitätsausnahme**: Vermögenswert erfordert anderen Detailgrad als Standard
2. **Überprüfungsfrequenz-Ausnahme**: Vermögenswert erfordert anderen Überprüfungsplan
3. **Eigentümerschaftsausnahme**: Vermögenswert hat unklare Eigentümerschaft, die erweiterte Lösungszeit erfordert
4. **Technische Ausnahme**: Technische Einschränkungen verhindern Standardinventaransatz

**Ausnahme-Antragsverfahren**:
1. Antragsteller reicht Ausnahmeantrag mit geschäftlicher Begründung ein
2. Informationssicherheitsmanager führt Risikobewertung durch
3. ISB genehmigt/lehnt Ausnahme ab
4. Genehmigte Ausnahmen werden dokumentiert mit:

   - Begründung und Risikobewertung
   - Kompensierende Kontrollen (sofern zutreffend)
   - Ablaufdatum der Ausnahme (maximal 12 Monate)
   - Neubewertungskriterien

5. Ausnahmen werden während periodischer Bewertungen überprüft
6. Ausnahmenregister als Nachweis geführt

**Ausnahmegenehmigung**:

- **Informationssicherheitsmanager**: Temporäre Ausnahmen ≤30 Tage genehmigen (taktisch)
- **ISB**: Ausnahmen ≤12 Monate genehmigen (strategisch)
- **Geschäftsleitung**: Ausnahmen >12 Monate genehmigen (selten, auf Vorstandsebene dokumentiert)

**Maximale Ausnahmedauer**: 12 Monate (muss erneuert oder behoben werden)

**Überprüfungsmethode**: Ausnahmenregister gemäss Summary Dashboard überprüft.

## Incident Response

**Anforderung A.5.9-R9**: [Organisation] MUSS das Asset-Inventar zur Unterstützung von Incident-Response-Prozessen nutzen.

**Inventar in der Incident Response**:

- **Asset-Identifikation**: Schnelle Identifizierung betroffener Vermögenswerte und Abhängigkeiten
- **Eigentümer-Benachrichtigung**: Kontaktaufnahme mit Asset-Eigentümern zur Geschäftsauswirkungsbewertung
- **Auswirkungsbeurteilung**: Bestimmung von Kritikalität und Geschäftsauswirkung anhand von Inventar-Metadaten
- **Eindämmung**: Abhängigkeitsinformationen zur Isolierung betroffener Systeme nutzen
- **Wiederherstellung**: Wiederherstellung basierend auf Asset-Kritikalitätsklassifizierung priorisieren
- **Ursachenanalyse**: Asset-Konfigurationen und -Beziehungen gegenüberstellen

**Inventar-Aktionen bei Vorfällen**:

- Überprüfung, ob Inventareinträge betroffener Vermögenswerte aktuell sind
- Asset-Status aktualisieren, wenn Vermögenswert beschädigt oder kompromittiert
- Vorfall in der Asset-Geschichte dokumentieren
- Risikoklassifizierung überprüfen und ggf. aktualisieren
- Inventarvalidierung nach dem Vorfall durchführen

**Integration**: Das Incident-Management-System MUSS das Asset-Inventar für betroffene Vermögenswerte referenzieren.

## Richtlinien-Governance

**Überprüfungshäufigkeit**: Mindestens jährlich oder ausgelöst durch:

- Wesentliche organisatorische Änderungen (Fusionen, Akquisitionen, Umstrukturierungen)
- Wesentliche regulatorische Änderungen, die das Asset-Management betreffen
- Prüfungsergebnisse, die Richtlinienaktualisierungen erfordern
- Risikobewertung, die Richtlinienlücken identifiziert
- Technologieänderungen, die den Inventaransatz betreffen

---

# Implementierung und Referenzen

## Integration in das ISMS

Diese Richtlinie ist in das Informationssicherheits-Managementsystem von [Organisation] integriert:

**Risikobewertung** (ISO 27001 Klausel 6.1):

- Asset-Inventar bildet die Grundlage für die Risikoidentifizierung
- Asset-Kritikalität beeinflusst Risikoeinstufung und Behandlungspriorisierung
- Bedrohungs-Asset-Schwachstellenanalyse erfordert ein vollständiges Asset-Inventar
- Risikobehandlungspläne referenzieren inventarisierte Vermögenswerte

**Verwandte Kontrollen**:

| Kontrolle | Beziehung | Integrationspunkt |
|-----------|-----------|------------------|
| **A.5.10 (Akzeptable Nutzung)** | Definiert akzeptable Nutzung inventarisierter Vermögenswerte | Asset-Einträge referenzieren Richtlinie zur akzeptablen Nutzung |
| **A.5.11 (Rückgabe von Vermögenswerten)** | Rückgabe im Inventar nachverfolgt | Status bei Rückgabe/Entsorgung aktualisiert |
| **A.5.12 (Klassifizierung)** | Klassifizierung auf Informationsvermögenswerte angewendet | Klassifizierungsfeld im Inventar |
| **A.5.13 (Kennzeichnung)** | Kennzeichen gemäss Inventarklassifizierung angewendet | Kennzeichengenerierung nutzt Inventardaten |
| **A.5.14 (Informationsübertragung)** | Übertragungskontrollen basierend auf Asset-Klassifizierung | Übertragungsprotokolle referenzieren Asset-Inventar |
| **A.5.15 (Zugriffskontrolle)** | Zugriffsregeln schützen inventarisierte Vermögenswerte | Asset-basierte Zugriffskontrollrichtlinien |
| **A.5.16 (Identitätsmanagement)** | Identitäten verknüpft mit Personalvermögenswerten | Personalinventar validiert Identitäten |
| **A.5.18 (Zugriffsrechte)** | Asset-Eigentümer genehmigen Zugriffsrechte | Eigentümerschaft im Inventar ermöglicht Genehmigungs-Workflow |
| **A.8.9 (Konfigurationsmanagement)** | Konfigurationsbasislinie für IT-Infrastruktur | Basislinie im Inventar referenziert |
| **A.8.10 (Informationslöschung)** | Entsorgung aktualisiert Inventarstatus | Entsorgung löst Inventaraktualisierung aus |
| **A.8.19 (Software-Installation)** | Software-Installation erstellt Inventareintrag | Anwendungsinventar gepflegt |

## Implementierungsressourcen

**Implementierungsleitfaden-Paket** (ISMS-IMP-A.5.9):

| Dokument-ID | Titel | Zweck | Zielgruppe |
|-------------|-------|-------|------------|
| **ISMS-IMP-A.5.9-1-UG/TG** | Asset-Identifikation und -Entdeckung | Verfahren zur Asset-Identifikation, Entdeckungsmethoden, Vollständigkeitsverifizierung | Sicherheitsteam, IT-Betrieb |
| **ISMS-IMP-A.5.9-2-UG/TG** | Inventarpflege | Inventarstrukturdesign, Aktualisierungsverfahren, Integrationsmethoden | Sicherheitsteam, IT-Betrieb, Systemeigentümer |
| **ISMS-IMP-A.5.9-3-UG/TG** | Qualitäts- und Compliance-Bewertung | Genauigkeitsstichproben, Aktualitätsverifizierung, Lückenanalyse | Sicherheitsteam, Revision, Compliance |
| **ISMS-IMP-A.5.9-4-UG/TG** | Eigentümer-Rechenschaftspflicht-Bewertung | Eigentümerzuweisung, Bestätigungs-Tracking, Verantwortlichkeitsverifizierung | Sicherheitsteam, Management, Asset-Eigentümer |

---

# Begriffsbestimmungen

**Vermögenswert (Asset)**: Alles, was für [Organisation] Wert hat und Schutz erfordert. Dazu gehören Informationen, IT-Infrastruktur, Anwendungen, physische Ressourcen und Personalkompetenzen.

**Informationsvermögenswert (Information Asset)**: Daten, Inhalte oder Kenntnisse in beliebiger Form (strukturierte Datenbanken, unstrukturierte Dokumente, geistiges Eigentum, Konfigurationen, Anmeldedaten) mit Anforderungen an Vertraulichkeit, Integrität oder Verfügbarkeit.

**Zugehöriger Vermögenswert (Associated Asset)**: Infrastruktur, Anwendungen, Einrichtungen oder Personal, das Informationsvermögenswerte verarbeitet, speichert, überträgt oder schützt. Diese Vermögenswerte leiten ihre Sicherheitsanforderungen aus den von ihnen unterstützten Informationen ab.

**Asset-Eigentümer (Asset Owner)**: Person, die während des gesamten Lebenszyklus für einen Vermögenswert rechenschaftspflichtig ist. Der Eigentümer ist verantwortlich für Klassifizierung, Zugangsgenehmigung, Schutzentscheidungen und Einhaltung von Sicherheitsanforderungen. Eigentümerschaft wird auf Basis geschäftlicher Rechenschaftspflicht zugewiesen, nicht technischer Verwaltung.

**Asset-Verwalter (Asset Custodian)**: Einzelperson oder Team mit täglicher operativer Verantwortung für einen Vermögenswert. Der Verwalter implementiert Sicherheitskontrollen gemäss Eigentümer-Anweisungen, die Rechenschaftspflicht verbleibt jedoch beim Eigentümer.

**Asset-Inventar (Asset Inventory)**: Strukturiertes Register von Informationen und zugehörigen Vermögenswerten, das obligatorische Attribute einschliesslich Eigentümer, Klassifizierung, Standort und Lebenszyklus-Status dokumentiert.

**Inventarvollständigkeit (Inventory Completeness)**: Grad, in dem das Inventar alle Vermögenswerte im Geltungsbereich umfasst. Gemessen als Prozentsatz der entdeckbaren Vermögenswerte, die im Inventar vorhanden sind.

**Inventargenauigkeit (Inventory Accuracy)**: Grad, in dem die Inventardaten den tatsächlichen Zustand der Vermögenswerte korrekt widerspiegeln. Gemessen durch Stichproben und Validierung gegen autoritative Quellen.

**Inventaraktualität (Inventory Currency)**: Grad, in dem das Inventar den aktuellen Zustand widerspiegelt und nicht den historischen. Gemessen an Prüfdaten und Aktualität der Aktualisierungen.

**Kritikalität**: Bewertung der Geschäftsauswirkung, sollte ein Vermögenswert nicht verfügbar, kompromittiert oder zerstört sein. Wird zur Priorisierung der Risikobehandlung und Incident Response verwendet.

**Lebenszyklus-Status**: Aktuelle Phase im Asset-Lebenszyklus (aktiv, Entwicklung, Wartung, pensioniert, archiviert). Bestimmt anwendbare Kontrollen und Wartungsanforderungen.

**CMDB (Configuration Management Database)**: Organisationssystem zur Dokumentation von IT-Infrastrukturkonfigurationen. Primäre Quelle für IT-Asset-Inventar, sofern implementiert.

**Personalvermögenswert (Personnel Asset)**: Schlüsselrollen und Spezialkompetenzen der Organisation (nicht individuelle Personendatensätze). Generisch dokumentiert zum Schutz der Privatsphäre bei gleichzeitiger Ermöglichung der Business-Continuity-Planung.

**Granularität**: Detailstufe, auf der Vermögenswerte inventarisiert werden. Hochrisiko-Vermögenswerte erfordern Einzeleinträge; Niedrigrisiko-Vermögenswerte können gruppiert werden (z. B. „Standard-Laptops — Anzahl 50").

---

# Nachweise für diese Richtlinie

**Stage 1 (Dokumentationsprüfung) Nachweise:**

Erforderliche Nachweise, die belegen, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.5.9 v1.0)
- ✅ Genehmigungsunterschriften von ISB, Geschäftsleitung und Rechts-/Compliance-Beauftragtem
- ✅ Anforderungen an die Inventarerstellung definiert (Abschnitt 2.1)
- ✅ Asset-Kategorisierungsrahmen dokumentiert (Abschnitt 2.2, Anhang A)
- ✅ Obligatorische Inventarattribute spezifiziert (Abschnitt 2.3)
- ✅ Asset-Eigentümerschaftsanforderungen definiert (Abschnitt 2.4)
- ✅ Inventarqualitätsstandards festgelegt (Abschnitt 2.5 — Vollständigkeit, Genauigkeit, Aktualität)
- ✅ Integrationsanforderungen mit anderen ISMS-Kontrollen dokumentiert (Abschnitt 2.6)
- ✅ Rollen und Verantwortlichkeiten zugewiesen (Abschnitt 3)
- ✅ Governance und Überprüfungsverfahren definiert (Abschnitt 3.3)
- ✅ Integration mit verwandten Kontrollen dokumentiert (Abschnitt 4.1)

**Stage 2 (Operative Wirksamkeit) Nachweise:**

Erforderliche Nachweise, die belegen, dass diese Richtlinie operativ wirksam ist:

- Bewertungen der Asset-Identifikation und -Entdeckung gemäss ISMS-IMP-A.5.9-1 (Vollständigkeitsverifizierung, Entdeckungsmethoden)
- Inventarpflegebewertungen gemäss ISMS-IMP-A.5.9-2 (Aktualisierungsverfahren, Integrationsmethoden, Aktualitäts-Tracking)
- Qualitäts- und Compliance-Bewertungen gemäss ISMS-IMP-A.5.9-3 (Genauigkeitsstichproben, Lückenanalyse, Vollständigkeitsmetriken)
- Eigentümer-Rechenschaftspflicht-Bewertungen gemäss ISMS-IMP-A.5.9-4 (Eigentümerzuweisung, Bestätigungs-Tracking, Verantwortlichkeitsverifizierung)
- Asset-Inventareinträge (alle Asset-Typen: Informations-, IT-Infrastruktur-, Anwendungs-, physische und Personalvermögenswerte)
- Asset-Kategorisierungsentscheidungen (Typ, Kritikalität, Lebenszyklus-Status)
- Asset-Eigentümerzuweisungen mit Eigentümer-Bestätigungen (Ziel: 100 %)
- Inventarvollständigkeitsmetriken (Prozentsatz entdeckter vs. inventarisierter Vermögenswerte)
- Inventargenauigkeitsmetriken (Prozentsatz als korrekt verifizierter Einträge)
- Inventaraktualitätsmetriken (Prozentsatz der innerhalb der geforderten Fristen aktualisierten Einträge)
- Überprüfungsunterlagen der Asset-Eigentümer (jährliche Bestätigungen)
- Integrationsnachweise mit anderen Kontrollen (Zugriffskontrolle, Klassifizierung, Änderungsmanagement, Incident-Management)
- Synchronisationsnachweise der CMDB/HR/Beschaffungssysteme
- Asset-Lebenszyklusdokumentation (Anschaffungs-, Änderungs- und Ausserbetriebnahmeunterlagen)
- Eskalationsnachweise für eigentümerlosen Vermögenswerte (falls vorhanden — mit Lösung innerhalb <30 Tagen)
- Prüfungsergebnisse und Behebungsnachweise für Inventarlücken

---

# Anhang A: Asset-Kategorisierungs-Entscheidungsmatrix

## Zweck

Dieser Anhang bietet einen praktischen Entscheidungsrahmen für die Kategorisierung von Vermögenswerten im Inventar. Dies sind **generische Beispiele**, die [Organisation] im Rahmen ihrer Risikobewertung an ihren spezifischen Kontext anpasst.

## Primäre Kategorisierung: Information vs. Zugehöriger Vermögenswert

**Entscheidungsfrage**: Handelt es sich um INFORMATION oder um ETWAS, DAS INFORMATIONEN VERARBEITET/SPEICHERT?

```
┌─ INFORMATION (Daten, Inhalte, Wissen)
│  └─ Kategorien von Informationsvermögenswerten:
│     ├─ Strukturierte Daten (Datenbanken, Tabellen, Data Warehouses)
│     ├─ Unstrukturierte Dokumente (Dateien, E-Mails, Berichte)
│     ├─ Unterlagen und Archive (für Compliance aufbewahrt)
│     ├─ Geistiges Eigentum (Geschäftsgeheimnisse, Patente, Designs)
│     ├─ Konfigurationen und Parameter (Systemkonfigurationen, Einstellungen)
│     ├─ Authentifizierung und Kryptografie (Schlüssel, Zertifikate, Anmeldedaten)
│     ├─ Kommunikationsunterlagen (E-Mails, Chats, Anrufprotokolle)
│     └─ Business Intelligence (Berichte, Analysen, Dashboards)
│
└─ ETWAS ANDERES (System, Gerät, Einrichtung, Person)
   └─ Kategorien zugehöriger Vermögenswerte:
      ├─ IT-Infrastruktur (Server, Speicher, Netzwerk, Endpunkte)
      ├─ Anwendungen (Software, SaaS, Dienste, APIs)
      ├─ Physische Vermögenswerte (Einrichtungen, Medien, Geräte)
      └─ Personalvermögenswerte (Schlüsselrollen, Spezialkompetenzen)
```

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Datum festzulegen] |
| **IT-Leiter (ITL)** | [Name] | [Datum festzulegen] |
| **Rechts-/Compliance-Beauftragter** | [Name] | [Datum festzulegen] |
| **Geschäftsleitung** | [Name] | [Datum festzulegen] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen an das Inventar von Informationen und Vermögenswerten fest. Implementierungsverfahren, Bewertungswerkzeuge und detaillierte Leitlinien sind in ISMS-IMP-A.5.9 (UG/TG) dokumentiert.*

<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.9-DE:framework:POL:a.5.9 -->

<!-- QA_VERIFIED: 2026-03-28 -->

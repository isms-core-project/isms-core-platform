<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.25-26-29-DE:framework:POL:a.8.25-26-29 -->
**ISMS-POL-A.8.25-26-29 — Richtlinie zum sicheren Entwicklungsrahmenwerk**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Sicheres Entwicklungsrahmenwerk |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.25-26-29 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] | |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | ISB / Application Security Lead | Konsolidiertes sicheres Entwicklungsrahmenwerk – Erstversion |

**Überprüfungsturnus**: Jährlich (oder bei wesentlichen SDLC-Methodenänderungen, regulatorischen Aktualisierungen oder grossen Sicherheitsvorfällen)

---

# Zusammenfassung

Diese Richtlinie etabliert das sichere Entwicklungsrahmenwerk von [Organisation] und implementiert ISO/IEC 27001:2022 Controls A.8.26 (Anwendungssicherheitsanforderungen), A.8.25 (Sicherer Entwicklungslebenszyklus) und A.8.29 (Sicherheitstests in Entwicklung und Abnahme) als einheitliches Sicherheitsrahmenwerk.

**Zweck**: Definition der organisatorischen Anforderungen an sichere Softwareentwicklung über den gesamten Software-Entwicklungslebenszyklus (SDLC). Diese Richtlinie legt fest, WAS an Sicherheitspraktiken erforderlich ist, WANN sie angewandt werden müssen und WER verantwortlich ist. Implementierungsverfahren (WIE) sind separat in den ISMS-IMP-A.8.25-26-29-Implementierungsleitfäden (UG/TG-Varianten) dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich Swiss nDSG (Datenschutz durch Technikgestaltung), EU DSGVO Artikel 25 (Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen) sowie ISO/IEC 27001:2022.

---

# Anwendungsbereich

## Im Geltungsbereich

**Anwendungen**:

- Alle intern entwickelten Anwendungen (Web, Mobile, Desktop, Eingebettet, APIs)
- Erworbene Anwendungen, die Anpassung oder Integration erfordern
- Infrastructure-as-Code (IaC) und Konfigurationsmanagement-Code

**Entwicklungsaktivitäten**:

- Neuentwicklung von Anwendungen
- Anwendungsverbesserungen und Sicherheits-Patches
- Anwendungsmodernisierung und Cloud-Migration

**Entwicklungsmodelle**:

- Interne Entwicklungsteams
- Ausgelagerte Entwicklung (Auftragnehmer, Offshore-Teams)
- Hybride Entwicklungsmodelle

**SDLC-Methodologien**:

- Waterfall, Agile/Scrum, DevOps/DevSecOps
- Continuous Delivery und Continuous Deployment (CI/CD)

## Nicht im Geltungsbereich

- Commercial Off-The-Shelf (COTS)-Software ohne Anpassung (gedeckt durch Lieferanten-Sicherheitsbeurteilung)
- Schwachstellenmanagement in der Produktion nach Deployment (gedeckt durch ISMS-POL-A.8.8)
- Operationelle Sicherheitsüberwachung (gedeckt durch ISMS-POL-A.8.15-16)

---

# ISO/IEC 27001:2022 Kontrollanforderungen

**A.8.26 – Anwendungssicherheitsanforderungen**
> *Informationssicherheitsanforderungen sollten bei der Entwicklung oder dem Erwerb von Anwendungen identifiziert, spezifiziert und genehmigt werden.*

**A.8.25 – Sicherer Entwicklungslebenszyklus**
> *Regeln für die sichere Entwicklung von Software und Systemen sollten etabliert und angewendet werden.*

**A.8.29 – Sicherheitstests in Entwicklung und Abnahme**
> *Sicherheitstestprozesse sollten im Entwicklungslebenszyklus definiert und implementiert werden.*

---

# Richtlinienanforderungen

## Anwendungsrisikoklassifizierung (A.8.26)

[Organisation] MUSS alle Anwendungen nach Risikograd klassifizieren, um angemessene Sicherheitsanforderungen zu bestimmen.

**Hochrisiko-Anwendungen** erfüllen EINES dieser Kriterien:

- Verarbeitung vertraulicher oder eingeschränkt zugänglicher Daten
- Umgang mit personenbezogenen Daten (PII) gemäss DSGVO, DSG
- Internetzugang oder Zugang durch externe Parteien
- Kritische Geschäftsfunktion oder Finanztransaktionsverarbeitung
- Zahlungskarteninformationen (PCI DSS v4.0.1-Umfang)

**Mittelrisiko-Anwendungen** erfüllen EINES dieser Kriterien:

- Verarbeitung interner Daten
- Begrenzte PII-Exposition (nur Namen, E-Mail-Adressen)
- Ausschliesslich interner Zugang
- Wichtige, aber nicht kritische Geschäftsfunktion

**Niedrigrisiko-Anwendungen** erfüllen ALLE diese Kriterien:

- Verarbeitung ausschliesslich öffentlicher Daten
- Keine PII, keine sensiblen Geschäftsdaten
- Nicht kritische Geschäftsfunktion

## Sicherheitsanforderungsspezifikation (A.8.26)

[Organisation] MUSS Sicherheitsanforderungen für alle Anwendungen basierend auf der Risikoklassifizierung festlegen.

**Verbindliche Anforderungen nach Risikograd**:

| Anforderung | Hochrisiko | Mittelrisiko | Niedrigrisiko |
|-------------|-----------|-------------|--------------|
| Sicherheitsanforderungsspezifikation | Verbindlich | Verbindlich | Einfache Checkliste |
| Threat Modeling | Verbindlich | Empfohlen | Optional |
| Sicherheitsarchitektur-Review | Verbindlich | Empfohlen | Optional |
| Anforderungs-Traceability | Verbindlich | Empfohlen | Optional |

**Sicherheitsanforderungen MÜSSEN adressieren**:

- Authentifizierungs- und Autorisierungskontrollen
- Eingabevalidierung und Ausgabe-Encoding
- Kryptographie (Daten in Transit und im Ruhezustand)
- Session-Management
- Fehlerbehandlung und Protokollierung
- API-Sicherheit (wo zutreffend)
- Datenschutzanforderungen

**Threat-Modeling-Methodik**:
Hochrisiko-Anwendungen MÜSSEN eine strukturierte Threat-Modeling-Methodik verwenden (z.B. STRIDE, PASTA oder Attack Trees). Vorlagen und Leitfäden für Threat Modeling sind in **ISMS-IMP-A.8.25-26-29-S1 (Sicherheitsanforderungsprozess)** bereitgestellt.

## Integration des sicheren Entwicklungslebenszyklus (A.8.25)

[Organisation] MUSS Sicherheitsaktivitäten in alle SDLC-Phasen integrieren.

**Sicherheits-Gates nach Phase**:

| Phase | Sicherheits-Gate | Genehmigungsbehörde |
|-------|-----------------|---------------------|
| Anforderungen | Sicherheitsanforderungen genehmigt | Security Architect |
| Design | Architektur genehmigt, Threat Model vollständig | Security Architect (ISB für Hochrisiko) |
| Entwicklung | Sicherheitsfehler unterhalb Schwellenwert | Entwicklungsmanager |
| Test | Sicherheitstests bestanden | Security Architect |
| Deployment | Produktionssicherheit validiert | ISB (Hochrisiko), Security Architect (Mittel) |

**Verbindliche Sicherheitsaktivitäten**:

- Sichere Codierungsstandards anwenden (gemäss ISMS-POL-A.8.28)
- Code Review durchführen (Peer Review für allen Code, Sicherheits-Review für Hochrisiko-Code)
- Sicherheitstools einsetzen (SAST, SCA, Secret Scanning)
- Sicherheitsfehler verfolgen und beheben
- Entwickler-Sicherheitsschulung abschliessen

## Sicherheitstestanforderungen (A.8.29)

[Organisation] MUSS Sicherheitstests basierend auf der Anwendungsrisikoklassifizierung implementieren.

**Erforderliche Tests nach Risikograd**:

| Testtyp | Hochrisiko | Mittelrisiko | Niedrigrisiko |
|---------|-----------|-------------|--------------|
| SAST (Statische Analyse) | Pro Commit/täglich | Pro Commit/täglich | Wöchentlich |
| SCA (Abhängigkeits-Scan) | Täglich/kontinuierlich | Täglich/kontinuierlich | Wöchentlich |
| DAST (Dynamisches Testen) | Pro Deployment/wöchentlich | Monatlich | Optional |
| Penetrationstests | Jährlich + grössere Releases | Alle 2 Jahre | Optional |
| Sicherheits-Abnahmetests | Pro Deployment | Pro Deployment | Einfache Checkliste |

**Tool-Auswahl und -Wartung**:
Sicherheitstesttools MÜSSEN auf Basis der in **ISMS-REF-A.8.25-26-29 (Sicherheitstest-Tools-Referenz)** dokumentierten Kriterien ausgewählt werden, einschliesslich Abdeckung erforderlicher Schwachstellenklassen, Integration in CI/CD-Pipelines und Anbieter-Support. Das aktuelle Toolset wird im [Sicherheitstools-Register] gepflegt.

**Software Bill of Materials (SBOM)**:
- Hochrisiko-Anwendungen MÜSSEN eine SBOM im CycloneDX- oder SPDX-Format pflegen
- SBOMs MÜSSEN automatisch während des Build-Prozesses generiert und im [SBOM-Repository] gespeichert werden
- SBOMs MÜSSEN bei Abhängigkeitsänderungen aktualisiert und vierteljährlich auf bekannte Schwachstellen überprüft werden

## Schwachstellenbehebungsanforderungen (A.8.29)

[Organisation] MUSS Sicherheitsschwachstellen innerhalb definierter Fristen beheben.

**Service Level Agreements für Schwachstellenbehebung**:

| Schweregrad | CVSS-Score | Behebungs-SLA | Auswirkung auf Deployment |
|-------------|------------|---------------|--------------------------|
| Kritisch | 9,0–10,0 | 7 Tage | Deployment blockiert, wenn nicht behoben |
| Hoch | 7,0–8,9 | 30 Tage | Deployment blockiert, wenn überfällig |
| Mittel | 4,0–6,9 | 90 Tage | Als technische Schulden verfolgen |
| Niedrig | 0,1–3,9 | 180 Tage | Für nächstes grösseres Release planen |

## Fehlermodus-Management

[Organisation] MUSS Verfahren für den Umgang mit Sicherheitskontrollausfällen und Ausnahmen definieren.

**Sicherheits-Gate-Überbrückung**:
- Notfall-Deployments, die Sicherheits-Gates umgehen, erfordern ISB-Genehmigung + retrospektive Sicherheitsvalidierung innerhalb von 72 Stunden
- Überbrückte Gates MÜSSEN im [Release-Management-System] mit Begründung und Behebungszeitplan protokolliert werden

**SLA-Überschreitungs-Eskalation**:
- Schwachstellen, die das Behebungs-SLA überschreiten, MÜSSEN eskaliert werden:
  - **Kritisch (7 Tage)**: Automatische Eskalation an ISB + Anwendungseigentümer + Risikoausschuss
  - **Hoch (30 Tage)**: Eskalation an ISB + Anwendungseigentümer
  - **Mittel (90 Tage)**: Eskalation an Security Architect + Entwicklungsmanager
- Überfällige Schwachstellen MÜSSEN nachfolgende Deployments blockieren, bis sie behoben oder eine Ausnahme genehmigt wurde

**Ausnahmeablauf**:
- Abgelaufene Ausnahmen MÜSSEN die automatische Widerrufung der Deployment-Genehmigung auslösen
- Anwendungen mit abgelaufenen Ausnahmen MÜSSEN innerhalb von 14 Tagen aus der Produktion entfernt oder in die Behebungswarteschlange überführt werden

**Fehlerverfolgung**:
- Alle Ausfälle (überbrückte Gates, SLA-Überschreitungen, Ausnahmeabläufe) MÜSSEN im [Lückennregister / Risikoregister] mit Behebungsstatus protokolliert werden

## Anforderungen an ausgelagerte Entwicklung (A.8.25)

[Organisation] MUSS Anforderungen an sichere Entwicklung auf ausgelagerte und Drittanbieter-Entwicklung anwenden.

**Vertragliche Anforderungen**:

- Compliance mit Sicherheitsanforderungen und sicheren Codierungsstandards
- Sicherheitstestanforderungen (SAST, DAST, SCA)
- SLAs zur Schwachstellenbehebung
- Anforderungen zur Benachrichtigung bei Sicherheitsvorfällen
- Rechte auf Code-Review und Sicherheitsarchitektur-Review

**Verifizierung der Auftragnehmer-Compliance**:
[Organisation] MUSS die Einhaltung der Anforderungen an sichere Entwicklung durch Auftragnehmer verifizieren durch:
- **Vierteljährliche Berichte**: Auftragnehmer MÜSSEN Sicherheitstestberichte (SAST/DAST/SCA-Ergebnisse, Behebungsstatus) an den Application Security Lead einreichen
- **Zugang zu Auftragnehmer-Tools**: [Organisation] MUSS Lesezugriff auf SAST/DAST-Plattformen der Auftragnehmer erhalten oder exportierte Berichte bekommen
- **Periodische Prüfungen**: Hochrisiko-ausgelagerte Projekte MÜSSEN bei wichtigen Meilensteinen (Design-Genehmigung, Vorproduktion) einem Sicherheits-Review durch Security Architects von [Organisation] unterzogen werden
- **Vertragliche Prüfungsrechte**: Verträge MÜSSEN das Recht von [Organisation] enthalten, Sicherheitspraktiken der Auftragnehmer mit 30-Tage-Frist zu prüfen

## Entwickler-Sicherheitsschulung (A.8.25)

[Organisation] MUSS Sicherheitsschulung für alle Entwickler bereitstellen.

**Schulungsanforderungen**:

| Schulungstyp | Zielgruppe | Turnus | Dauer |
|--------------|------------|--------|-------|
| Initiale Sicherheitsschulung | Alle Entwickler | Vor Produktionscode | Mindestens 4 Stunden |
| Jährliche Auffrischung | Alle Entwickler | Jährlich | Mindestens 2 Stunden |
| Security-Champion-Schulung | Security Champions | Initial + Jährlich | 8 Stunden + 4 Stunden |

---

# Rollen und Verantwortlichkeiten

## Governance

| Rolle | Verantwortung |
|-------|---------------|
| **GF** | Letztverantwortung für das sichere Entwicklungsrahmenwerk; genehmigt Richtlinie; weist Ressourcen zu |
| **ISB** | Gesamtverantwortung für die Rahmenwerk-Implementierung; Richtlinien-Governance; Eskalationsbehörde |
| **Application Security Lead** | Verantwortung für Rahmenwerk-Implementierung; Sicherheitstools-Programm; Überwachung des Schulungsprogramms |

## Security Team

| Rolle | Verantwortung |
|-------|---------------|
| **Security Architects** | Sicherheitsanforderungs-Review; Architektur-Review; Threat Modeling; Sicherheitsdesign-Leitfaden |
| **Security Analysts** | Assessment-Durchführung; Schwachstellentriage; Sicherheitstests; Kennzahlen-Berichterstattung |
| **Penetration Tester** | Penetrationstest-Durchführung; Schwachstellenvalidierung; Sicherheitstest-Methodik |

## Entwicklungsorganisation

| Rolle | Verantwortung |
|-------|---------------|
| **Entwicklungsmanager** | SDLC-Sicherheitsintegration; Schulungsunterstützung; Code-Review-Durchsetzung; Aufsicht über Fehlerbeseitigung |
| **Security Champions** | Sicherheitsfürsprache in Teams; Sicherheits-Code-Review; Mentoring zu sicherer Codierung |
| **Entwickler** | Implementierung von Sicherheitsanforderungen; Einhaltung sicherer Codierung; Schwachstellenbehebung |
| **Solution Architects** | Sicherheitsarchitektur-Design; Teilnahme an Threat Modeling; technische Sicherheitsentscheide |

## Qualitätssicherung

| Rolle | Verantwortung |
|-------|---------------|
| **QA-Manager** | Sicherheitstest-Integration; Koordination der Sicherheits-Abnahmetests |
| **QA Engineers** | Ausführung von Sicherheitstestfällen; DAST-Betrieb; Sicherheitsfehler-Berichterstattung |

## DevOps

| Rolle | Verantwortung |
|-------|---------------|
| **DevOps Lead** | Sicherheitstools-Integration in CI/CD; Implementierung von Sicherheits-Gates |
| **DevOps Engineers** | CI/CD-Sicherheitsautomatisierung; Produktionssicherheitskonfiguration |

## Anwendungsmanagement

| Rolle | Verantwortung |
|-------|---------------|
| **Product Manager / Anwendungseigentümer** | Anwendungsrisikoklassifizierung; Einleitung von Sicherheitsanforderungen; Ausnahmeanträge |

---

# Governance und Compliance

## Assessment und Verifizierung

[Organisation] MUSS die Wirksamkeit der Kontrollen für sichere Entwicklung durch strukturierte Assessments verifizieren.

**Assessment-Turnus**:

| Umfang | Turnus |
|--------|--------|
| Umfassendes Rahmenwerk-Assessment | Jährlich |
| Verifizierung Hochrisiko-Anwendungen | Vierteljährlich |
| Verifizierung Mittelrisiko-Anwendungen | Halbjährlich |
| Verifizierung Niedrigrisiko-Anwendungen | Jährlich |
| Ausgelöstes Assessment (Vorfälle, Prüfungsbefunde) | Innerhalb von 30 Tagen |

**Assessment-Methodik**:
Bewertungsverfahren sind in den jeweiligen Assessment-Arbeitsmappen (S1–S4) dokumentiert, jede mit einem Summary Dashboard zur Verfolgung des Compliance-Status. Assessments MÜSSEN umfassen:
- Überprüfung der Aktualität der Anwendungsrisikoklassifizierung
- Beweisstichproben (SAST/DAST/SCA-Berichte, Penetrationstest-Berichte, Sicherheits-Gate-Genehmigungen)
- Verifizierung der Einhaltung von Schwachstellenbehebungs-SLAs
- Verifizierung des Abschlusses der Sicherheitsschulung
- Ausnahmen-Review

## Beweiserfassung und -aufbewahrung

[Organisation] MUSS verifizierbare Nachweise der Implementierung von Kontrollen für sichere Entwicklung aufbewahren.

**Nachweistypen und Speicherung**:

| Kontrollaktivität | Nachweistyp | Speicherort | Aufbewahrungsfrist |
|-------------------|-------------|-------------|-------------------|
| Anwendungsrisikoklassifizierung | Risikobeurteilungsaufzeichnungen | [GRC-Plattform / Risikoregister] | Lebensdauer der Anwendung + 3 Jahre |
| SAST-Ausführung | Tool-Ausführungsprotokolle, Befundberichte | [SAST-Plattform – z.B. GitHub Security/Snyk/SonarQube] | 2 Jahre |
| DAST-Ausführung | Scan-Berichte, validierte Befunde | [DAST-Plattform / Sicherheitstest-Repository] | 2 Jahre |
| SCA-Ausführung | Abhängigkeits-Scan-Berichte, SBOM-Updates | [SCA-Plattform / SBOM-Repository] | 2 Jahre |
| Penetrationstests | Testberichte, Behebungsverifikation | [Security-Team-Dokumentenrepository] | 5 Jahre |
| Sicherheits-Gate-Genehmigungen | Genehmigungsaufzeichnungen (Architektur-Review, Deployment-Freigabe) | [Release-Management-System / Jira] | 3 Jahre |
| Schwachstellenbehebung | Behebungstickets mit SLA-Verfolgung | [Issue-Tracking-System / Jira Security] | 3 Jahre |
| Sicherheitsschulungsabschluss | Schulungsaufzeichnungen | [HR-System / LMS] | Beschäftigungsdauer + 3 Jahre |
| Ausnahmegenehmigungen | Ausnahmeanträge, Genehmigungen, Überprüfungsaufzeichnungen | [GRC-Plattform / Ausnahmeregister] | Ausnahmedauer + 3 Jahre |

**Nachweisvalidierung**:
- Security Architects MÜSSEN SAST/DAST/SCA-Befunde monatlich überprüfen, um Behebungsfortschritte zu validieren und False Positives zu triagieren
- Application Security Lead MUSS vierteljährlich Beweisstichproben-Prüfungen durchführen

## Lückenbehebung und -verfolgung

[Organisation] MUSS ein zentralisiertes Lückenregister für Defizite bei Kontrollen für sichere Entwicklung führen.

**Quellen der Lückenidentifizierung**:
- Vierteljährliche/halbjährliche/jährliche Assessments
- Sicherheitstestbefunde (SAST/DAST/SCA/Penetrationstests)
- Sicherheits-Gate-Ausfälle oder SLA-Überschreitungen
- Prüfungsbefunde (intern/extern)
- Sicherheitsvorfälle im Zusammenhang mit Anwendungsschwachstellen

**Anforderungen ans Lückenregister**:

| Feld | Beschreibung |
|------|--------------|
| Lücken-ID | Eindeutige Kennung |
| Kontroll-ID | Betroffene ISO-27001-Kontrollen (A.8.25, A.8.26, A.8.29) |
| Anwendung | Betroffene Anwendung(en) |
| Beschreibung | Spezifisch identifiziertes Defizit |
| Risikobewertung | Hoch/Mittel/Niedrig (basierend auf Anwendungsrisikoklassifizierung) |
| Eigentümer | Zugewiesener Behebungseigentümer (Entwicklungsmanager / Security Architect) |
| Fälligkeitsdatum | Behebungsfrist (gemäss SLA oder Ausnahmezeitplan) |
| Status | Offen / In Bearbeitung / Geschlossen / Ausnahme genehmigt |
| Schliessungsnachweis | Verweis auf Verifikationsnachweis (Testbericht, Code-Review, Deployment-Bestätigung) |

**Lückenschliessungs-Verifizierung**:
- Security Architects MÜSSEN die Lückenschliessung verifizieren, bevor der Status auf „Geschlossen" gesetzt wird
- Application Security Lead MUSS das Lückenregister monatlich überprüfen, um überfällige Positionen zu verfolgen

**Lückenregister-Speicherort**: [GRC-Plattform / Jira Security / SharePoint Lückenregister]

## Ausnahmemanagement

**Ausnahmeantragsanforderungen**:

- Dokumentierte geschäftliche oder technische Begründung
- Risikobeurteilung und Bewertung des Restrisikos
- Vorgeschlagene kompensierende Kontrollen
- Zeitplan zur Erreichung vollständiger Compliance

**Genehmigungsbehörde**:

| Anwendungsrisiko | Genehmigungsbehörde |
|------------------|---------------------|
| Niedrigrisiko | Security Architect |
| Mittelrisiko | ISB |
| Hochrisiko | ISB + Risikoausschuss (bei hochwirkenden Risiken) |

## Richtlinienüberprüfung

**Überprüfungsauslöser**:

- Jährlich geplante Überprüfung
- Regulatorische Änderungen, die sichere Entwicklung betreffen
- Grosse Sicherheitsvorfälle
- Wesentliche SDLC-Methoden- oder Technologieänderungen
- Prüfungsbefunde, die Richtlinienaktualisierungen erfordern

**Aktualisierungsbehörde**:

- Geringfügige Aktualisierungen (Klarstellungen, Verweise): ISB-Genehmigung
- Wesentliche Aktualisierungen (Umfangs-, Anforderungsänderungen): Vollständige Genehmigungskette

---

# Regulatorischer Rahmen

## Verbindliche Compliance (Tier 1)

**ISO/IEC 27001:2022**

- Controls: A.8.25, A.8.26, A.8.29
- Anforderungen: Dokumentierte Richtlinien, Verfahren, Implementierungsnachweise

**Schweizerisches Bundesgesetz über den Datenschutz (DSG/nDSG)**

- Artikel 8: Technische und organisatorische Massnahmen zum Datenschutz
- Artikel 26: Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen

**EU-Datenschutz-Grundverordnung (DSGVO)**

- Artikel 25: Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen
- Artikel 32: Sicherheit der Verarbeitung

## Bedingte Compliance (Tier 2)

Sektorspezifische Anforderungen gelten, wenn die Geschäftsaktivitäten von [Organisation] deren Anwendbarkeit auslösen:

| Regulation | Auslösebedingung | Wesentliche Anforderungen |
|------------|-----------------|--------------------------|
| DORA | EU-Finanzunternehmen | IKT-Risikomanagement, Resilienztests |
| NIS2 | Wesentliche/wichtige Einrichtung | Cybersicherheits-Risikomanagement |
| FINMA Circular 2023/1 | Schweizer Finanzinstitut | Sicherheit für Finanzanwendungen |
| PCI DSS v4.0.1 | Zahlungskartenverarbeitung | Anforderung 6: Sichere Entwicklung |

**Vollständige regulatorische Kategorisierung in ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen).**

---

# Verwandte Dokumente

## Richtlinien

| Dokument-ID | Titel | Beziehung |
|-------------|-------|-----------|
| ISMS-POL-00 | Regulatorischer Anwendbarkeitsrahmen | Regulatorische Tier-Klassifizierung |
| ISMS-POL-A.8.28 | Sichere Codierung | Sichere Codierungsstandards |
| ISMS-POL-A.8.4 | Zugang zu Quellcode | Repository-Sicherheit |
| ISMS-POL-A.8.31 | Umgebungstrennung | Dev/Test/Prod-Isolation |
| ISMS-POL-A.8.32 | Änderungsmanagement | Sicherheitsfreigabe in Releases |
| ISMS-POL-A.8.8 | Schwachstellenmanagement | Produktionsschwachstellen |

## Implementierungsleitfäden

| Dokument-ID | Titel | Inhalt |
|-------------|-------|--------|
| ISMS-IMP-A.8.25-26-29-S1 | Sicherheitsanforderungsprozess | Anforderungserhebung, Threat Modeling |
| ISMS-IMP-A.8.25-26-29-S2 | SDLC-Sicherheitsintegration | Sicherheitsaktivitäten nach Phase |
| ISMS-IMP-A.8.25-26-29-S3 | Sichere Codierungspraktiken | Code-Review, Tool-Deployment |
| ISMS-IMP-A.8.25-26-29-S4 | Sicherheitstest-Implementierung | SAST/DAST/SCA-Konfiguration |

## Referenzmaterialien

| Dokument-ID | Titel | Inhalt |
|-------------|-------|--------|
| ISMS-REF-A.8.25-26-29 | Sicherheitstest-Tools-Referenz | Tool-Vergleich, Auswahlkriterien |
| ISMS-CTX-A.8.25-26-29 | SDLC-Sicherheitsentwicklung | Branchenkontext, Sensibilisierung |

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Anwendung** | Von [Organisation] entwickeltes, erworbenes oder integriertes Softwaresystem |
| **DAST** | Dynamic Application Security Testing – analysiert laufende Anwendungen |
| **Penetrationstest** | Manueller Sicherheitstest durch qualifizierte Fachkräfte |
| **SAST** | Static Application Security Testing – analysiert Quellcode |
| **SCA** | Software Composition Analysis – identifiziert Schwachstellen in Abhängigkeiten |
| **SDLC** | Software Development Lifecycle (Software-Entwicklungslebenszyklus) |
| **Security Champion** | Entwickler mit spezialisierter Sicherheitsschulung, der als Sicherheitskontaktperson des Teams fungiert |
| **Threat Modeling** | Strukturierter Ansatz zur Identifizierung von Sicherheitsbedrohungen im Anwendungsdesign |

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date to be set] |
| **Application Security Lead** | [Name] | [Date to be set] |
| **Entwicklungsmanager** | [Name] | [Date to be set] |
| **Legal/Compliance Officer** | [Name] | [Date to be set] |
| **Geschäftsführer (GF)** | [Name] | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen an sichere Softwareentwicklung fest. Implementierungsverfahren (WIE) sind in den ISMS-IMP-A.8.25-26-29-Implementierungsleitfäden (UG/TG) dokumentiert. Technischer Tool-Leitfaden ist in ISMS-REF-A.8.25-26-29 bereitgestellt.*

<!-- QA_VERIFIED: 2026-03-29 -->

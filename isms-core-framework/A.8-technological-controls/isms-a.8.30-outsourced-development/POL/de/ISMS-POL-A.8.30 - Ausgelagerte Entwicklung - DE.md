<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.30-DE:framework:POL:a.8.30 -->
**ISMS-POL-A.8.30 — Ausgelagerte Entwicklung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Richtlinie zur ausgelagerten Entwicklung |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.30 |
| **Ersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstrichtlinie für ISO-27001:2022-Erstzertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Technischer Leiter (TL)
- Einkauf: Beschaffung/Lieferantenmanagement
- Compliance: Rechts-/Compliance-Beauftragter
- Letztinstanzlich: Geschäftsleitung

**Zugehörige Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.8.28 (Sichere Codierung)
- ISMS-POL-A.5.19-23 (Lieferantenbeziehungen und Cloud-Dienste)
- ISMS-IMP-A.8.30.1-UG/TG (Lieferantenbewertung und -verzeichnis)
- ISMS-IMP-A.8.30.2-UG/TG (Vertragskonformität)
- ISMS-IMP-A.8.30.3-UG/TG (Sicherheitstests und Abnahme)
- ISO/IEC 27001:2022 Massnahme A.8.30
- ISO/IEC 27002:2022 Massnahme 8.30

---

## Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen von [Organisation] an das Sicherheitsmanagement bei der ausgelagerten System- und Softwareentwicklung gemäss ISO/IEC 27001:2022 Massnahme A.8.30 fest.

**Zweck**: Festlegung, WELCHE Sicherheitskontrollen für ausgelagerte Entwicklung erforderlich sind und WER die Verantwortung trägt. Technische Umsetzungsdetails (WIE) sind in den ISMS-IMP-A.8.30-Spezifikationen dokumentiert.

**Geltungsbereich**: Alle ausgelagerten Entwicklungsaktivitäten einschliesslich beauftragter Entwicklung, Offshore-Entwicklung, freiberuflicher Entwickler und Anpassung erworbener Software.

**Adressiertes Geschäftsrisiko**: Durch Drittentwicklung eingeführte Sicherheitsschwachstellen, die zu Datenschutzverletzungen, Diebstahl geistigen Eigentums, Lieferkettenkompromittierung und regulatorischer Nichtkonformität führen können.

**Regulatorische Ausrichtung**: Gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen):

- **Verbindlich**: Schweizer nDSG (Art. 8), EU DSGVO (Art. 32), ISO 27001:2022
- **Bedingt**: FINMA, DORA (Art. 28–30 IKT-Drittparteienrisiko), NIS2 (Art. 21 Lieferkette)
- **Informativ**: NIST SP 800-218 SSDF, ISO/IEC 27036 (Lieferantenbeziehungen)

---

# Kontrollanpassung und Geltungsbereich

## ISO/IEC 27001:2022 Massnahme A.8.30

**Kontrollaussage**:
> *Die Organisation soll die Aktivitäten im Zusammenhang mit der ausgelagerten Systementwicklung steuern, überwachen und überprüfen.*

**Kontrolltyp**: Präventiv und Detektiv

**Kontrollziel**: Sicherstellen, dass die von [Organisation] geforderten Informationssicherheitsmassnahmen auch dann wirksam umgesetzt werden, wenn die System- und Softwareentwicklung an Dritte ausgelagert wird.

**Diese Massnahme adressiert**:

- Steuerung der Sicherheitsanforderungen für ausgelagerte Entwicklung
- Überwachung der Entwicklungsaktivitäten von Drittparteien
- Überprüfung und Verifikation ausgelagerter Lieferobjekte
- Vertragliche Sicherheitsanforderungen
- Sicherheitstests von Drittanbietercode
- Management von Unterauftragnehmern und Lieferkette

## Geltungsbereichsdefinition

**Im Geltungsbereich**:

- Gesamte beauftragte Softwareentwicklung (vollständige Projekte, Module, Komponenten)
- Offshore- und Nearshore-Entwicklungsteams
- Freiberufliche/unabhängige Entwickler
- Personalaufstockung mit Entwicklungszugang
- Erworbene Software, die Anpassungen erfordert
- Entwicklungsplattformanbieter (wo Code von [Organisation] gehostet wird)
- Verwaltete Entwicklungsdienste

**Nicht im Geltungsbereich**:

- Kommerzielle Standardsoftware (COTS) ohne Anpassung (siehe A.8.31)
- Interne Entwicklung durch Mitarbeiter (siehe A.8.28)
- Cloud-Dienstanbieter nur für Infrastruktur (siehe A.5.23)
- Allgemeines Lieferantenmanagement (siehe A.5.19-22)

## Dokumentenhierarchie

| Dokumententyp | Inhalt | Aktualisierungshäufigkeit |
|---------------|--------|--------------------------|
| **Diese Richtlinie (POL)** | Anforderungen, Governance, Verantwortlichkeit | Jährlich |
| **Umsetzung (IMP)** | Bewertungsverfahren, Arbeitsmappenspezifikationen | Vierteljährlich |
| **Referenz (REF)** | Vertragsvorlagen, Checklisten | Bei Bedarf |

---

# Lieferantenauswahl und Due Diligence

## Anforderungen an Sicherheitsbewertungen

**Bewertung vor der Beauftragung**:

Vor der Beauftragung eines Lieferanten für ausgelagerte Entwicklung MUSS [Organisation] eine sicherheitsbezogene Due-Diligence-Prüfung durchführen, die folgende Bereiche umfasst:

| Bewertungsbereich | Anforderung | Erforderliche Nachweise |
|-------------------|-------------|-------------------------|
| **Sicherheitszertifizierung** | ISO 27001 oder SOC 2 Typ II bevorzugt | Aktuelles Zertifikat (innerhalb von 12 Monaten) |
| **Sichere Entwicklungspraktiken** | OWASP SAMM, Microsoft SDL oder gleichwertig | SDLC-Dokumentation oder Bestätigung |
| **Sicherheitsvorfallshistorie** | Keine grösseren Verstösse in den vergangenen 24 Monaten | Lieferantenoffenlegung + Referenzprüfungen |
| **Technische Fähigkeiten** | SAST/DAST/SCA-Tools im Einsatz | Tool-Inventar und Musterberichte |
| **Personalsicherheit** | Hintergrundprüfungen für Entwickler | Schriftliche Bestätigung der Screeningrichtlinie |

**Risikobasierte Bewertungstiefe**:

| Projektklassifizierung | Bewertungstiefe | Genehmiger |
|------------------------|-----------------|-----------|
| **Kritisch** (Produktionssysteme, sensible Daten) | Vollständiger Sicherheitsfragebogen + Vor-Ort-/Fernaudit + Referenzprüfungen | ISB |
| **Hoch** (interne Systeme, Geschäftsdaten) | Sicherheitsfragebogen + Referenzprüfungen | IT Security Manager |
| **Standard** (nicht sensibel, geringes Risiko) | Sicherheitsfragebogen + Zertifizierungsverifizierung | Beschaffung + Sicherheitsüberprüfung |

**Verifizierung**: Due-Diligence-Unterlagen werden im Lieferantenmanagementsystem aufbewahrt; Bewertungsergebnisse in Arbeitsmappe 1 dokumentiert.

## Genehmigtes Lieferantenverzeichnis

[Organisation] MUSS ein genehmigtes Lieferantenverzeichnis für die ausgelagerte Entwicklung pflegen:

- Lieferanten werden vor der Beauftragung bewertet und genehmigt
- Verzeichnis enthält: Lieferantenname, Bewertungsdatum, Risikoklasse, genehmigte Projekttypen, Verlängerungsdatum
- Jährliche Neubewertung für aktive Lieferanten erforderlich
- Entfernung aus dem Verzeichnis bei Vertragsbeendigung, Sicherheitsvorfall oder fehlgeschlagener Neubewertung

**Verifizierung**: Genehmigtes Lieferantenverzeichnis wird von der Beschaffung mit Sicherheitsbeteiligung gepflegt; vierteljährliche Überprüfung aktiver Lieferanten.

---

# Vertragliche Sicherheitsanforderungen

## Verbindliche Vertragsklauseln

Alle Verträge für ausgelagerte Entwicklung MÜSSEN folgende Sicherheitsanforderungen enthalten:

**Einhaltung von Sicherheitsstandards**:

- Einhaltung der Richtlinien zur sicheren Codierung von [Organisation] (ISMS-POL-A.8.28)
- Konformität mit den Sicherheitsrichtlinien und -verfahren von [Organisation]
- Verwendung genehmigter Entwicklungstools und -umgebungen
- Anforderungen zur Absolvierung von Sicherheitsschulungen

**Schutz geistigen Eigentums und Code**:

- Klare Eigentumsregelung für entwickelten Code und Dokumentation
- Source-Code-Escrow-Vereinbarungen für kritische Projekte
- Schutz der proprietären Informationen von [Organisation]
- Geheimhaltungs- und Vertraulichkeitsverpflichtungen

**Sicherheitsverifizierungsrechte**:

- Recht zur Prüfung von Entwicklungsprozessen und Sicherheitskontrollen
- Recht zur Durchführung von Sicherheitstests an Lieferobjekten
- Recht zur Anforderung von Sicherheitszertifizierungen und -bestätigungen
- Recht auf Zugang zu Informationen über Sicherheitsvorfälle

**Meldepflicht bei Vorfällen**:

- Meldung von Sicherheitsvorfällen innerhalb von 24 Stunden
- Sofortige Meldung bei Verdacht auf Datenschutzverletzungen
- Kooperation bei der Vorfallsuntersuchung
- Anforderungen zur Behebung nach einem Vorfall

**Management von Unterauftragnehmern**:

- Vorab schriftliche Genehmigung für Unterauftragnehmer erforderlich
- Weitergabe aller Sicherheitsanforderungen an Unterauftragnehmer
- Recht von [Organisation], Unterauftragnehmer abzulehnen
- Prüfungsrechte gegenüber Unterauftragnehmern

## SLAs für die Schwachstellenbehebung

Verträge MÜSSEN Fristen zur Schwachstellenbehebung festlegen, die mit ISMS-POL-A.8.28 übereinstimmen:

| Schweregrad | CVSS-Score | Behebungs-SLA |
|-------------|------------|---------------|
| **Kritisch** | 9,0–10,0 | 7 Tage |
| **Hoch** | 7,0–8,9 | 30 Tage |
| **Mittel** | 4,0–6,9 | 90 Tage |
| **Niedrig** | 0,1–3,9 | Nächste Version oder 180 Tage |

**SLA-Durchsetzung**:

- SLA-Konformität wird im Projektmanagementsystem verfolgt
- Wiederholte SLA-Verstösse werden an Lieferantenmanagement und ISB eskaliert
- Chronische Nichtkonformität kann zu Vertragsüberprüfung oder -kündigung führen
- SLA-Ausnahmen erfordern dokumentierte Risikoakzeptanz (ISB-Genehmigung bei Kritisch/Hoch)

**Verifizierung**: Vertragsvorlagen werden von der Rechtsabteilung mit Sicherheitsbeteiligung gepflegt; Konformität in Arbeitsmappe 2 verfolgt.

## Kündigung und Übergang

Verträge MÜSSEN Sicherheitsanforderungen für die Kündigung regeln:

- Rückgabe oder sichere Vernichtung der Daten von [Organisation]
- Widerruf aller Zugangsdaten innerhalb von 24 Stunden
- Übertragung von Dokumentation und Quellcode
- Wissenstransferphase für kritische Projekte
- Vertraulichkeitsverpflichtungen nach Vertragsende
- Zertifizierung der Datenvernichtung

---

# Anforderungen an die sichere Entwicklung

## Entwicklungsstandards

Ausgelagerte Entwickler MÜSSEN die Richtlinien zur sicheren Codierung von [Organisation] gemäss ISMS-POL-A.8.28 einhalten:

**Verbindliche Anforderungen**:

- Eingabevalidierung für alle Benutzer- und externen Eingaben
- Kontextbezogenes Ausgabe-Encoding
- Sichere Authentifizierung und Session-Management
- Serverseitige Autorisierungsdurchsetzung
- Verwendung genehmigter kryptographischer Methoden
- Sichere Fehlerbehandlung (keine sensiblen Daten in Logs)
- Keine hartcodierten Geheimnisse im Quellcode

**Verbotene Praktiken**:

- Hartcodierte Zugangsdaten, API-Schlüssel oder Geheimnisse
- Veraltete oder unsichere Funktionen
- Aufbau von SQL-Abfragen durch String-Verkettung
- Deaktivierte Sicherheitskontrollen
- Einchecken von Geheimnissen in die Versionsverwaltung
- Ignorieren von Sicherheitstoolfunden ohne dokumentierte Ausnahme

**Verifizierung**: Konformität mit sicherer Codierung wird durch Code-Review und Sicherheitstests verifiziert; Befunde in Arbeitsmappe 3 dokumentiert.

## Sicherheit der Entwicklungsumgebung

Ausgelagerte Entwicklungsumgebungen MÜSSEN Mindestsicherheitsanforderungen erfüllen:

| Anforderung | Beschreibung |
|-------------|--------------|
| **Zugriffskontrolle** | MFA für alle Entwicklungssysteme erforderlich; Prinzip der minimalen Rechte |
| **Netzwerksicherheit** | Entwicklungsumgebung isoliert oder abgesichert; kein direkter Produktionszugang |
| **Endpunktsicherheit** | Entwickler-Workstations mit aktueller Sicherheitssoftware |
| **Code-Repository** | Branch-Schutz, Code-Review-Durchsetzung, Secret-Scanning |
| **Datenverarbeitung** | Keine Produktionsdaten in der Entwicklung ohne Maskierung/Anonymisierung |

**Verifizierung**: Sicherheitsanforderungen an die Umgebung in Arbeitsmappe 1 dokumentiert; Lieferantenbestätigung erforderlich.

## Schulung für Drittentwickler

Vor dem Zugang zu Systemen oder Code von [Organisation] MÜSSEN ausgelagerte Entwickler:

- Die Schulung zur sicheren Codierung von [Organisation] absolvieren (oder eine gleichwertige Schulung)
- Die Sicherheitsrichtlinien und Anforderungen zur akzeptablen Nutzung von [Organisation] bestätigen
- Verständnis der projektspezifischen Sicherheitsanforderungen nachweisen

**Schulungsverifizierung**:

- Schulungsabschluss wird in der Lieferanten-Onboarding-Checkliste verfolgt **und in [HR-/Lieferantenmanagementsystem] erfasst**
- **Zugriffsanfragen werden vor der Genehmigung mit Schulungsunterlagen abgeglichen** (systemseitig durchgesetzt, wo realisierbar; verfahrensmässige Überprüfung bei manuellem Zugriffsmanagement)
- Jährliche Auffrischung für langfristige Beauftragungen erforderlich
- Schulungsunterlagen für Auditzwecke aufbewahrt

**Verifizierung**: Schulungsabschluss wird vor der Zugriffsgewährung bestätigt; Unterlagen in Arbeitsmappe 4.

---

# Sicherheitsverifizierung und -tests

## Anforderungen an Code-Reviews

Sämtlicher ausgelagerter Code MUSS vor der Abnahme einer Sicherheitsüberprüfung unterzogen werden:

| Überprüfungstyp | Anforderung | Prüfer |
|-----------------|-------------|--------|
| **Peer-Review** | Alle Codeänderungen vor dem Merge überprüft | Interner Entwickler (mindestens 1) |
| **Sicherheitsreview** | Sicherheitssensible Änderungen durch Sicherheitsteam überprüft | Application-Security-Team |
| **Architekturreview** | Neue Komponenten oder wesentliche Änderungen | Sicherheitsarchitekt |

**Überprüfungskriterien** (gemäss ISMS-REF-A.8.28):

- Eingabevalidierung und Ausgabe-Encoding
- Authentifizierungs- und Autorisierungslogik
- Kryptographische Implementierungen
- Fehlerbehandlung und Protokollierung
- Verwendung von Drittanbieterkomponenten

**Verifizierung**: Code-Review-Unterlagen im Versionsverwaltungssystem aufbewahrt; Review-Statistiken in Arbeitsmappe 3.

## Anforderungen an Sicherheitstests

Ausgelagerte Lieferobjekte MÜSSEN vor der Produktionsbereitstellung Sicherheitstests durchlaufen:

**Automatisierte Tests**:

- SAST (Static Application Security Testing): Bei allem Code vor der Abnahme ausführen
- SCA (Software Composition Analysis): Alle Drittanbieter-Abhängigkeiten scannen
- Secret-Scanning: Verifizieren, dass keine Geheimnisse in der Codebasis vorhanden sind

**Manuelle Tests**:

- DAST (Dynamic Application Security Testing): In Staging-Umgebung ausführen
- Penetrationstest: Für kritische Projekte vor dem Go-live erforderlich

**Testzuständigkeiten**:

| Testtyp | Primäre Zuständigkeit | Verifizierung |
|---------|----------------------|---------------|
| SAST | Lieferant (mit Tool-Zugang von [Organisation]) oder [Organisation] | Scan-Berichte überprüft |
| SCA | Lieferant oder [Organisation] | SBOM und Schwachstellenbericht |
| DAST | [Organisation] Application Security | Testbericht dokumentiert |
| Penetrationstest | [Organisation] oder genehmigter Drittanbieter | Befunde vor Go-live behoben |

**Abnahmekriterien**:

- Keine kritischen oder hohen Schwachstellen (oder dokumentierte Ausnahme mit ausgleichenden Massnahmen)
- Alle Sicherheitsanforderungen verifiziert
- Sicherheitstestberichte dokumentiert und aufbewahrt

**Verifizierung**: Testergebnisse in Arbeitsmappe 3 dokumentiert; Abnahmefreigabe erforderlich.

## Software Bill of Materials (SBOM)

Für alle ausgelagerten Entwicklungsprojekte MUSS [Organisation] erhalten:

- Vollständige SBOM mit allen Drittanbieterkomponenten
- Komponentenversionen und Lizenzen
- Status bekannter Schwachstellen zum Zeitpunkt der Lieferung
- Aktualisierungsplan für Komponenten mit bekannten Schwachstellen

**SBOM-Format**: CycloneDX oder SPDX bevorzugt; Tabellenkalkulation für einfache Projekte akzeptabel.

**Verifizierung**: SBOM wird überprüft und mit der Projektdokumentation aufbewahrt; in Arbeitsmappe 3 verfolgt.

---

# Überwachung und Kontrolle

## Anforderungen an aktive Überwachung

[Organisation] MUSS bei ausgelagerter Entwicklung aktiv eingebunden sein (keine passive Überwachung):

**Steuerung**:

- Klare Sicherheitsanforderungen bei Projektinitiierung kommuniziert
- Sicherheitskontrollpunkte in Projektmeilensteinen definiert
- Regelmässige Sicherheitsanleitungen und Klärungen

**Überwachung**:

- Regelmässige Statusaktualisierungen zu Sicherheitsaktivitäten
- Zugang zu Sicherheitstestergebnissen des Lieferanten
- Beteiligung an sicherheitsrelevanten Diskussionen
- Alarmüberwachung bei Sicherheitsvorfällen

**Überprüfung**:

- Sicherheitslieferobjekte bei jedem Meilenstein überprüft
- Abschliessende Sicherheitsüberprüfung vor der Abnahme
- Lessons-Learned für zukünftige Projekte erfasst

## Überwachungshäufigkeit

| Projektklassifizierung | Statusaktualisierungen | Sicherheitsreviews | Vollständiges Audit |
|------------------------|----------------------|---------------------|---------------------|
| **Kritisch** | Wöchentlich | Bei jedem Meilenstein + abschliessend | Jährlich (oder Projektende) |
| **Hoch** | Zweiwöchentlich | Bei Hauptmeilensteinen + abschliessend | Auf Anfrage |
| **Standard** | Monatlich | Abnahme abschliessend | Auf Anfrage |

**Verifizierung**: Überwachungsaktivitäten im Projektmanagementsystem protokolliert; Zusammenfassung in Arbeitsmappe 2.

## Eskalation bei Problemen

Bei der Überwachung identifizierte Sicherheitsprobleme MÜSSEN eskaliert werden:

| Problemschwere | Eskalationspfad | Zeitrahmen |
|----------------|-----------------|------------|
| **Kritisch** (aktive Schwachstelle, Verstoss) | Projektmanager → ISB → Executive | Sofort |
| **Hoch** (Sicherheitsanforderung nicht erfüllt) | Projektmanager → IT Security Manager | Innerhalb von 24 Stunden |
| **Mittel** (Abweichung von Standards) | Projektmanager → Security Lead | Innerhalb von 5 Werktagen |
| **Niedrig** (geringfügige Beobachtung) | Für Projektreview protokolliert | Nächstes Statusmeeting |

---

# Management von Unterauftragnehmern

## Anforderungen an Unterauftragnehmer

Lieferanten für ausgelagerte Entwicklung DÜRFEN Unterauftragnehmer NICHT beauftragen ohne:

- Vorherige schriftliche Genehmigung von [Organisation]
- Sicherheitsbewertung des Unterauftragnehmers (proportional zum Risiko)
- Weitergabe aller Sicherheitsanforderungen an den Unterauftragnehmer, einschliesslich:
  - Richtlinien zur sicheren Codierung (gemäss ISMS-POL-A.8.28)
  - Anforderungen an Sicherheitstests (gemäss ISMS-POL-A.8.29)
  - **SBOM-Lieferpflichten (auch für Komponenten von Unterauftragnehmern)**
  - SLAs für die Schwachstellenbehebung (gemäss Abschnitt 5.2)
- Direkte Prüfungsrechte gegenüber dem Unterauftragnehmer (oder durch den Lieferanten durchgeführtes Audit)
- Geheimhaltungs- und IP-Schutzverpflichtungen

## Genehmigungsprozess für Unterauftragnehmer

**Genehmigungsanforderungen**:

| Leistungsumfang des Unterauftragnehmers | Genehmigungsbefugnis | Erforderliche Bewertung |
|-----------------------------------------|---------------------|------------------------|
| Zugang zu Systemen/Daten von [Organisation] | ISB | Vollständiger Sicherheitsfragebogen |
| Entwicklung ohne direkten Zugang | IT Security Manager | Kurzfragebogen + Lieferantenbestätigung |
| Begrenzte/spezialisierte Aufgaben | Projektmanager + Sicherheit | Lieferantenbestätigung zur Weitergabe der Sicherheitsanforderungen |

**Verifizierung**: Genehmigungen für Unterauftragnehmer in Projektunterlagen dokumentiert; in Arbeitsmappe 4 verfolgt.

---

# Rollen und Verantwortlichkeiten

## Geschäftsleitung

- Genehmigung der Sicherheitsrichtlinie für ausgelagerte Entwicklung
- Budgetzuweisung für Sicherheitsbewertungen und -tests
- Überprüfung von Hochrisikolieferantenbeziehungen
- Eskalationsstelle bei kritischen Sicherheitsproblemen

## Informationssicherheitsbeauftragter (ISB)

- Gesamtverantwortung für die Sicherheit bei ausgelagerter Entwicklung
- Genehmigung von Hochrisikolieferantenbeziehungen
- Genehmigung von Sicherheitsausnahmen
- Überprüfung von Sicherheitsmetriken und Lieferantenperformance
- Eskalation bei lieferantenbezogenen Sicherheitsvorfällen

## IT Security Manager

- Tägliche Überwachung der Lieferantenkonformität mit Sicherheitsanforderungen
- Durchführung oder Koordination von Sicherheitsbewertungen
- Überprüfung von Sicherheitstestergebnissen
- Genehmigung standardrisikobehafteter Lieferantenbeziehungen
- Verwaltung der Sicherheitsvorfallsreaktion bei Lieferanten

## Application-Security-Team

- Definition der Anforderungen an sichere Entwicklung
- Durchführung von Sicherheitstests an Lieferobjekten
- Überprüfung sicherheitssensibler Codeänderungen
- Bereitstellung von Sicherheitsanleitungen für Projektteams
- Pflege von Sicherheitstesttools und -verfahren

## Beschaffung/Lieferantenmanagement

- Pflege des genehmigten Lieferantenverzeichnisses
- Sicherstellung, dass Verträge die erforderlichen Sicherheitsklauseln enthalten
- Koordination von Lieferantenbewertungen mit der Sicherheitsabteilung
- Verwaltung der Lieferantenperformance einschliesslich Sicherheitsmetriken
- Koordination des Lieferanten-Offboardings

## Projektmanager

- Sicherstellung, dass Sicherheitsanforderungen in den Projektumfang aufgenommen werden
- Überwachung der Lieferantenkonformität mit Sicherheitsanforderungen
- Angemessene Eskalation von Sicherheitsproblemen
- Sicherstellung, dass Sicherheitsmeilensteine eingehalten werden
- Koordination von Sicherheitsreviews und -tests

## Entwicklungsteamleiter

- Überprüfung von ausgelagertem Code vor der Abnahme
- Verifizierung der Vollständigkeit der Sicherheitstests
- Sicherstellung der Integration mit internen Sicherheitspraktiken
- Meldung von Sicherheitsbedenken an das Sicherheitsteam

---

# Governance und Compliance

## Überwachung der Richtlinienkonformität

**Kontinuierliche Überwachung**:

- Status der Lieferantensicherheitsbewertung verfolgt
- Konformität mit vertraglichen Sicherheitsklauseln verifiziert
- Sicherheitstestergebnisse überprüft

**Periodische Bewertung**:

- Vierteljährlich: Überprüfung des Sicherheitsstatus aktiver Lieferanten
- Jährlich: Vollständige Sicherheitsneubewertung der Lieferanten
- Jährlich: Überprüfung der Richtlinienwirksamkeit

## Umgang mit Nichtkonformität

**Lieferanten-Nichtkonformität**:

| Schweregrad | Reaktion | Eskalation |
|-------------|----------|------------|
| **Kritisch** (aktiver Sicherheitsverstoß, grobe Verletzung) | Sofortige Zugangssperrung; Vorfallsreaktion | ISB, Executive, Rechtsabteilung |
| **Hoch** (wesentliche Sicherheitslücke) | Behebungsplan innerhalb von 5 Tagen erforderlich; erhöhte Überwachung | IT Security Manager, Projektsponsor |
| **Mittel** (Abweichung von Anforderungen) | Dokumentierte Verwarnung; Behebung innerhalb von 30 Tagen | Projektmanager, Security Lead |
| **Niedrig** (geringfügige Beobachtung) | Für nächste Überprüfung vermerkt | Projektmanager |

**Wiederholte Nichtkonformität**: Lieferanten mit wiederholten Nichtkonformitätsproblemen können:

- Erhöhter Überwachung unterliegen
- Auf Niedrigrisikoprojekte beschränkt werden
- Aus dem genehmigten Lieferantenverzeichnis entfernt werden
- Der Vertragskündigung unterliegen

## Ausnahmenmanagement

- Alle Ausnahmen erfordern dokumentierte geschäftliche Begründung
- Risikobeurteilung und ausgleichende Massnahmen verbindlich
- Genehmigungsbefugnis basierend auf Risikoniveau (Security Lead für Mittel; ISB für Hoch/Kritisch)
- Ausnahmen im zentralen Register verfolgt (Arbeitsmappe 4)
- Maximale Laufzeit: 90 Tage (erneuerbar mit erneuter Genehmigung)

**Angemessenheitskriterien für ausgleichende Massnahmen**:

- **Wirksamkeit**: Massnahme mindert das spezifische Risiko (nicht generische Sicherheit)
- **Zuverlässigkeit**: Massnahme funktioniert kontinuierlich mit Alarmierung bei Ausfall
- **Überprüfbarkeit**: Massnahme kann getestet und überwacht werden
- **Umfang**: Massnahme deckt alle betroffenen Systeme/Datenflüsse ab

**Ausnahmen erfordern eine dokumentierte Risikobeurteilung**, die das Restrisiko mit und ohne die vorgeschlagenen ausgleichenden Massnahmen quantifiziert. Die Risikobeurteilung MUSS vom Projektteam erstellt und vom IT Security Manager validiert werden, bevor die zuständige Genehmigungsbehörde prüft.

---

# Nachweise für diese Richtlinie

**Stufe 1 (Dokumentationsüberprüfung) — Erforderliche Nachweise:**

Nachweise, die belegen, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.8.30 v1.0)
- ✅ Genehmigungsunterschriften von ISB, ITL, Geschäftsleitung
- ✅ Dokumentierte Sicherheitsanforderungen an Lieferanten
- ✅ Vertragliche Sicherheitsklauseln definiert
- ✅ Sicherheitstestanforderungen spezifiziert
- ✅ Rollen und Verantwortlichkeiten zugewiesen
- ✅ Referenzen auf Bewertungsarbeitsmappen dokumentiert (ISMS-IMP-A.8.30)

**Stufe 2 (Operative Wirksamkeit) — Erforderliche Nachweise:**

Nachweise, die belegen, dass diese Richtlinie operativ wirksam ist:

- Genehmigtes Lieferantenverzeichnis mit Bewertungsunterlagen
- Vertragsvorlagen mit Sicherheitsklauseln
- Sicherheitsbewertungsberichte für Lieferanten
- Sicherheitstestergebnisse für ausgelagerte Lieferobjekte
- Code-Review-Unterlagen
- Genehmigungsunterlagen für Unterauftragnehmer
- Ausnahmen- und Vorfallsunterlagen
- Schulungsabschlussnachweise

**Bewertungsarbeitsmappen** (ISMS-IMP-A.8.30-Suite):
- ISMS-IMP-A.8.30.1: Lieferantenbewertung und -verzeichnis
- ISMS-IMP-A.8.30.2: Vertragskonformität
- ISMS-IMP-A.8.30.3: Sicherheitstests und Abnahme

**Aufbewahrung von Nachweisen:**
- Lieferantenbewertungsunterlagen: Dauer der Geschäftsbeziehung + 3 Jahre
- Vertragsunterlagen: Vertragslaufzeit + 7 Jahre
- Sicherheitstestergebnisse: 5 Jahre (entsprechend DORA Art. 28(6), falls anwendbar) oder Projektlaufzeit + 3 Jahre
- Code-Review-Unterlagen: Projektlaufzeit + 2 Jahre
- Vorfallsunterlagen: 5 Jahre

---

# Integration mit verwandten Massnahmen

## Verwandte ISMS-Massnahmen

| Massnahme | Integration |
|-----------|-------------|
| **A.5.19** (Lieferantensicherheit) | Lieferantenrisikobewertungsrahmen fliesst in A.8.30 ein |
| **A.5.20** (Lieferantenvereinbarungen) | Vertragliche Sicherheitsklauseln aus A.8.30 |
| **A.5.21** (IKT-Lieferkette) | SBOM- und Unterauftraggeberanforderungen stimmen überein |
| **A.5.22** (Lieferantenüberwachung) | Kontinuierliche Lieferantenüberwachung gemäss A.8.30 |
| **A.8.25** (Sichere Architektur) | Architekturanforderungen gelten für ausgelagerte Systeme |
| **A.8.28** (Sichere Codierung) | Richtlinien zur sicheren Codierung gelten für Drittparteien |
| **A.8.29** (Sicherheitstests) | Testanforderungen für ausgelagerte Lieferobjekte |
| **A.8.31** (Entwicklungsumgebung) | Umgebungssicherheitsanforderungen für Lieferanten |

## Regulatorisches Mapping

| Anforderung | Schweizer nDSG | EU DSGVO | ISO 27001 | DORA* |
|-------------|---------------|----------|-----------|-------|
| Lieferantensicherheitsbewertung | Art. 8 | Art. 28, 32 | A.8.30 | Art. 28 |
| Vertragliche Sicherheitsanforderungen | Art. 8 | Art. 28 | A.5.20 | Art. 30 |
| Sicherheitstests | Art. 8 | Art. 32 | A.8.29 | Art. 24–25 |
| Management von Unterauftragnehmern | Art. 8 | Art. 28(4) | A.5.21 | Art. 29 |

*DORA anwendbar, sofern [Organisation] als Finanzunternehmen eingestuft ist.

---

# Genehmigungsprotokoll

| Funktion | Name | Datum |
|----------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **Technischer Leiter (TL)** | [Name] | [Date] |
| **Beschaffungsmanager** | [Name] | [Date] |
| **Rechts-/Compliance-Beauftragter** | [Name] | [Date] |
| **Geschäftsleitung** | [Name] | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen an die Sicherheit bei ausgelagerter Entwicklung fest. Umsetzungsverfahren, Bewertungsmethoden und Arbeitsmappenspezifikationen sind in ISMS-IMP-A.8.30.1–4 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-29 -->

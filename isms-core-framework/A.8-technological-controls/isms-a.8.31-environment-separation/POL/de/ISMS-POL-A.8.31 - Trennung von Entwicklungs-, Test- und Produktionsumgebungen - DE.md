<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.31-DE:framework:POL:a.8.31 -->
**ISMS-POL-A.8.31 — Trennung von Entwicklungs-, Test- und Produktionsumgebungen**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Trennung von Entwicklungs-, Test- und Produktionsumgebungen |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.31 |
| **Ersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] | |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | ISB / IT Operations | Erstrichtlinie für ISO-27001:2022-Zertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

---

# Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen von [Organisation] zur Trennung von Entwicklungs-, Test- und Produktionsumgebungen fest, um Risiken im Zusammenhang mit unbefugten Änderungen und Datenexposition gemäss ISO/IEC 27001:2022 Massnahme A.8.31 zu reduzieren.

**Zweck**: Festlegung der organisatorischen Anforderungen an die Umgebungstrennung — was getrennt werden MUSS und wer verantwortlich ist. Umsetzungsverfahren (WIE) sind separat in ISMS-IMP-A.8.31 (UG/TG-Varianten) dokumentiert.

**Grundprinzipien**:

- Produktionsumgebungen MÜSSEN vor Entwicklungs- und Testaktivitäten geschützt werden
- Produktionsdaten DÜRFEN NICHT in Entwicklungs- oder Testumgebungen verwendet werden
- Änderungen MÜSSEN über definierte Beförderungspfade laufen, bevor sie die Produktion erreichen
- Entwicklerzugang zur Produktion MUSS auf Notfallsituationen beschränkt werden

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich ISO/IEC 27001:2022, Schweizer nDSG, EU DSGVO sowie sektorspezifischer Anforderungen, soweit anwendbar.

---

# Geltungsbereich

## Im Geltungsbereich

Diese Richtlinie gilt für:

**Umgebungstypen**:

- Entwicklungsumgebungen (aktive Code-Entwicklung, Experimente)
- Test-/QA-Umgebungen (Qualitätssicherung, Integrationstests, UAT)
- Staging-/Pre-Production-Umgebungen (finale Validierung vor Produktion)
- Produktionsumgebungen (aktiver Geschäftsbetrieb)

**Technologischer Geltungsbereich**:

- Alle von [Organisation] betriebenen Informationssysteme und Anwendungen
- On-Premises-, Cloud-, Hybrid- und Container-basierte Infrastruktur
- Interne und kundenseitige Systeme
- Von Drittanbietern verwaltete Systeme, die organisatorische Daten verarbeiten

**Personal**:

- Alle Mitarbeiter, Auftragnehmer und Drittparteien mit Zugang zu Organisationssystemen

## Nicht im Geltungsbereich

Diese Richtlinie gilt NICHT für:

- Einzelbenutzer-isolierte Forschungsumgebungen, die nicht mit Organisationsnetzwerken verbunden sind
- Temporäre Proof-of-Concept-Systeme ohne Organisationsdaten
- Vom Anbieter vollständig verwaltete Vendor-Demonstrationssysteme

Sobald Forschungs- oder Proof-of-Concept-Systeme zur organisatorischen Nutzung übergehen, MÜSSEN sie dieser Richtlinie entsprechen.

---

# Richtlinienanweisungen

## Anforderungen an die Umgebungsarchitektur

[Organisation] MUSS getrennte Umgebungen mit folgenden Merkmalen unterhalten:

**3.1.1 Mindest-Umgebungsebenen**

- Organisationen MÜSSEN mindestens drei Umgebungsebenen unterhalten: Entwicklung, Testing/QA und Produktion
- Jede Umgebungsebene MUSS einen definierten Zweck, Infrastrukturressourcen, Datenverarbeitungsrestriktionen und Zugriffskontrollen haben
- Umgebungsbezeichnungen MÜSSEN den Umgebungstyp klar unterscheiden, um Verwechslungen zu vermeiden

**3.1.2 Netzwerktrennung**

- Umgebungen MÜSSEN durch Netzwerksegmentierung isoliert werden
- Interumgebungs-Datenverkehr MUSS standardmässig gesperrt sein (Deny-All)
- Kontrollierte Beförderungspfade MÜSSEN die einzig zulässige Cross-Umgebungs-Konnektivität sein
- Produktionsumgebungen DÜRFEN KEINE direkte Netzwerkverbindung zu Entwicklungsumgebungen haben

**3.1.3 Infrastrukturtrennung**

- Compute-, Speicher- und Datenbankressourcen MÜSSEN pro Umgebung getrennt werden
- Produktions- und Nicht-Produktions-Workloads DÜRFEN KEINE gemeinsame Infrastruktur nutzen
- Zugangsdaten und Geheimnisse MÜSSEN pro Umgebung eindeutig sein

**3.1.4 Konfigurationsmanagement**

- Umgebungskonfigurationen MÜSSEN als Code verwaltet und versionskontrolliert werden
- Staging-Umgebungen MÜSSEN die Produktionskonfiguration spiegeln
- Konfigurationsänderungen MÜSSEN denselben Beförderungspfad wie Anwendungscode durchlaufen

**3.1.4.1 Konfigurationsvalidierung**

- Umgebungskonfigurationen MÜSSEN in einem versionskontrollierten Repository mit Zugangskontrolle gespeichert werden
- Konfigurationsänderungen MÜSSEN denselben Beförderungsworkflow wie Anwendungscode befolgen (Abschnitt 3.4.1)
- Die Staging-Konfiguration MUSS vor jeder Produktionsbereitstellung gegen die Produktionskonfiguration validiert werden
- Die Erkennung von Konfigurationsdrift MUSS wöchentlich durchgeführt werden, wobei Verstösse dem IT Operations Manager gemeldet werden

## Anforderungen an die Umgebungszugriffskontrolle

**3.2.1 Rollenbasierter Zugriff**

- Zugriff auf jede Umgebung MUSS dem Prinzip der minimalen Rechte folgen
- Zugriffsrechte MÜSSEN pro Rolle und Umgebungsebene definiert werden
- Entwickler MÜSSEN vollen Zugang nur zu Entwicklungsumgebungen haben
- Das Operations-Team MUSS primären Zugang zu Produktionsumgebungen haben

**3.2.2 Produktionszugangsbeschränkungen**

- Entwickler DÜRFEN KEINEN dauerhaften Zugang zur Produktionsinfrastruktur haben
- Produktionszugang MUSS Privileged-Access-Management-Kontrollen erfordern
- Multi-Faktor-Authentifizierung MUSS für jeden Produktionszugang erforderlich sein
- Produktionszugangssitzungen MÜSSEN protokolliert und überwacht werden

**3.2.3 Notfallzugang (Break-Glass)**

- Entwickler-Notfallzugang zur Produktion DARF NUR während erklärter Vorfälle genehmigt werden
- Break-Glass-Zugang MUSS die Genehmigung des Incident Commander und des ISB erfordern
- Break-Glass-Zugang MUSS zeitlich begrenzt sein (maximal 8 Stunden, erneuerbar mit erneuter Genehmigung) und zweckgebunden sein
- Ein Post-Incident-Review MUSS für alle Break-Glass-Aktivierungen verpflichtend sein

**3.2.3.1 Dokumentationsanforderungen für Break-Glass**

Break-Glass-Aktivierungen MÜSSEN mit folgenden Angaben protokolliert werden:

- Vorfallskennung (aus dem Vorfallsmanagementsystem) und deklarierter Schweregradlevel
- Name, Funktion und Vorgesetzte(r) des anfragenden Entwicklers
- Namen des genehmigenden Incident Commander und des ISB mit Genehmigungszeitstempeln
- Zugangsdauer (gewährt, genutzt, abgelaufen) und zugegriffene Systeme/Anwendungen
- Während der Break-Glass-Sitzung durchgeführte Aktionen (aus Sitzungsaufzeichnung oder Aktivitätslog)
- Ergebnis des Post-Incident-Reviews (abgeschlossen innerhalb von 7 Tagen nach Vorfallsabschluss)
- Erkannte Lessons Learned und Prozessverbesserungen

Break-Glass-Protokolle MÜSSEN:

- Im Privileged-Access-Management (PAM)-System mit automatisierter Aufbewahrung gepflegt werden
- Monatlich vom Information Security Manager auf Muster und Richtlinienkonformität überprüft werden
- Im vierteljährlichen ISB-Dashboard mit Trendanalyse (Häufigkeit, Dauer, Begründungskategorien) enthalten sein

**3.2.4 Zugriffsüberprüfungen**

- Produktionsumgebungszugang MUSS vierteljährlich überprüft werden
- Staging-Umgebungszugang MUSS halbjährlich überprüft werden
- Entwicklungs-/Testumgebungszugang MUSS jährlich überprüft werden
- Zugang von ausgeschiedenen Mitarbeitern MUSS innerhalb von 24 Stunden widerrufen werden

## Anforderungen an die Datenverarbeitung

**3.3.1 Verbot von Produktionsdaten**

- Produktionsdaten DÜRFEN NICHT in Entwicklungs- oder Testumgebungen kopiert werden
- Produktionsdatenbank-Backups DÜRFEN NICHT in Nicht-Produktionsumgebungen wiederhergestellt werden
- Produktionszugangsdaten DÜRFEN NICHT in Nicht-Produktionsumgebungen verwendet werden

**3.3.2 Genehmigte Daten für Nicht-Produktionsumgebungen**

- Synthetische Daten (generiert, nicht aus der Produktion abgeleitet) SOLLEN bevorzugt werden
- Anonymisierte Daten DÜRFEN mit Genehmigung des Datenschutzbeauftragten verwendet werden
- Anonymisierung MUSS irreversibel sein (keine Pseudonymisierung oder Verschlüsselung)
- Anonymisierte Daten MÜSSEN innerhalb von 30 Tagen nach Projektabschluss gelöscht werden

**3.3.2.1 Validierungsprozess für die Anonymisierung**

Bevor der Datenschutzbeauftragte anonymisierte Daten für die Nicht-Produktionsnutzung genehmigt:

- Der Datenschutzbeauftragte MUSS die Wirksamkeit der Anonymisierung durch Re-Identifizierungsversuche testen
- Die Validierung MUSS das Risiko der Re-Identifizierung beurteilen durch:
  - Verifizierung der Entfernung direkter Identifikatoren
  - Analyse der Kombination von Quasi-Identifikatoren (k-Anonymity-Bewertung mit k ≥ 5)
  - Simulation von Verknüpfungsangriffen unter Verwendung öffentlich verfügbarer Datensätze
- Ergebnisse MÜSSEN im Datenverarbeitungsregister dokumentiert werden (ISMS-IMP-A.8.31-S2)
- Anonymisierungsverfahren MÜSSEN vor dem ersten Einsatz von ISB und Datenschutzbeauftragtem überprüft und genehmigt werden
- Fehlgeschlagene Validierung führt zur Ablehnung oder zu zusätzlichen Anonymisierungsmassnahmen

**3.3.3 Durchsetzung der Datenklassifizierung**

- Vertrauliche und eingestufte Datenklassifizierungen MÜSSEN in Entwicklungs- und Testumgebungen verboten sein
- Automatisiertes Scanning MUSS verbotene Daten in Nicht-Produktionsumgebungen erkennen
- Verstösse MÜSSEN innerhalb von 7 Tagen nach Erkennung behoben werden

**3.3.3.1 Automatisiertes Daten-Scanning**

- Nicht-Produktionsumgebungen MÜSSEN wöchentlich auf Produktionsdatenmuster gescannt werden
- Scanning MUSS Datenbanken, Dateisysteme, Log-Dateien und Container-Images abdecken
- Scanning-Tools und Erkennungsmuster MÜSSEN in ISMS-IMP-A.8.31-S2 definiert werden
- Verstösse MÜSSEN innerhalb von 24 Stunden Warnmeldungen an den Information Security Manager auslösen
- Scanning-Abdeckung und -Wirksamkeit MÜSSEN während der vierteljährlichen Eigenbewertungen verifiziert werden

## Anforderungen an die Umgebungsbeförderung

**3.4.1 Verbindlicher Beförderungspfad**

- Änderungen MÜSSEN dem Standard-Beförderungspfad folgen: Entwicklung → Testing → Staging → Produktion
- Direkte Bereitstellung in der Produktion MUSS verboten sein, ausser bei genehmigten Notfallkorrekturen
- Das Überspringen von Umgebungsebenen MUSS dokumentierte Ausnahme und ISB-Genehmigung erfordern

**3.4.2 Genehmigungsanforderungen**

- Produktionsbereitstellungen MÜSSEN eine Genehmigung des Change Advisory Board gemäss ISMS-POL-A.8.32 (Änderungsmanagement) erfordern
- Zusammensetzung des CAB und Genehmigungsbefugnis sind in ISMS-POL-A.8.32 definiert
- Produktionsbereitstellungen DÜRFEN NUR während genehmigter Änderungsfenster erfolgen
- Rollback-Pläne MÜSSEN vor der Produktionsbereitstellung dokumentiert und verfügbar sein
- Notfalländerungen DÜRFEN die CAB-Genehmigung umgehen, mit Post-Implementierungs-Review innerhalb von 48 Stunden

**3.4.3 Rollback-Fähigkeit**

- Frühere Versionen MÜSSEN für Rollback-Zwecke aufbewahrt werden
- Rollback-Verfahren MÜSSEN dokumentiert und regelmässig getestet werden
- Das Operations-Team MUSS befugt sein, Rollbacks während Vorfällen ohne zusätzliche Genehmigung durchzuführen

## Anforderungen an den Produktionssupport

**3.5.1 Überwachungszugang**

- Schreibgeschützter Überwachungszugang MUSS die Fehlerbehebung ohne Produktionszugang ermöglichen
- Sensible Daten MÜSSEN aus Logs geschwärzt werden, die für Nicht-Operations-Personal zugänglich sind
- Zugangsdaten DÜRFEN NICHT in Logs enthalten sein

**3.5.2 Remote-Fehlerbehebung**

- Fehlerbehebungsverfahren MÜSSEN die Problemlösung ohne Entwickler-Produktionszugang ermöglichen
- Runbooks MÜSSEN für gängige Betriebsszenarien gepflegt werden
- Screen-Sharing DARF mit dem Operations-Team, das Produktionssysteme steuert, verwendet werden

**3.5.3 Integration der Vorfallsreaktion**

- Anforderungen an die Umgebungstrennung MÜSSEN in Vorfallsreaktionsverfahren integriert werden
- Abgestufte Eskalation MUSS befolgt werden, bevor Notfall-Produktionszugang gewährt wird
- Break-Glass-Nutzung MUSS verfolgt und für kontinuierliche Verbesserung ausgewertet werden

---

# Rollen und Verantwortlichkeiten

## Governance-Rollen

| Funktion | Verantwortlichkeiten |
|----------|---------------------|
| **ISB** | Richtlinieneigentümer; genehmigt Ausnahmen; überprüft Konformität vierteljährlich |
| **IT Operations Manager** | Produktionsumgebungssicherheit; Produktionszugangsgenehmigung; PAM-Management |
| **Development Manager** | Management von Entwicklungs-/Testumgebungen; Umsetzung des Beförderungsworkflows |
| **Information Security Manager** | Compliance-Bewertungen; Untersuchungen von Richtlinienverstössen; Richtlinienpflege |
| **Datenschutzbeauftragter** | Anonymisierungsgenehmigung; Datenverarbeitungs-Compliance; Re-Identifizierungstests |

## Operative Rollen

| Funktion | Verantwortlichkeiten |
|----------|---------------------|
| **Systemeigentümer** | Definition der Umgebungsarchitektur; Compliance-Dokumentation; Ausnahmenmeldung |
| **Entwickler** | Ausschliessliche Nutzung zugewiesener Umgebungen; Einhaltung der Datenverarbeitungsanforderungen; Nutzung der Beförderungsworkflows |
| **QA-Team** | Tests in geeigneten Umgebungen; Testdatenmanagement; Meldung von Datenverstössen |
| **Operations-Team** | Produktionszugangsverwaltung; Produktionsbereitstellungen; Vorfallsreaktion |
| **Sicherheitsteam** | Überwachung von Zugriffsprotokollen; Vorfallsuntersuchung; Sicherheitsbewertungen |

---

# Compliance und Durchsetzung

## Bewertungsanforderungen

| Bewertungstyp | Häufigkeit | Verantwortliche Partei |
|---------------|-----------|------------------------|
| Eigenbewertung | Vierteljährlich | Systemeigentümer, IT Operations |
| Sicherheitsbewertung | Halbjährlich | Information-Security-Team |
| Interne Revision | Jährlich | Interne Revision |
| Externe Revision | Jährlich | Externer Revisor (ISO 27001) |
| Kontinuierliche Überwachung | Fortlaufend | Security Operations |

**4.1 Bewertungsmethodik**

Bewertungen MÜSSEN die Konformität der Umgebungstrennung durch folgende Massnahmen verifizieren:

**4.1.1 Validierung technischer Kontrollen**

- Netzwerksegmentierung: Testen, dass umgebungsübergreifender Datenverkehr gesperrt ist (vierteljährlich)
- Zugangserzwingung: Verifizieren, dass Entwickler-Produktionszugang verboten ist (vierteljährlich)
- Daten-Scanning: Überprüfung automatisierter Scan-Ergebnisse auf Produktionsdaten in Nicht-Produktion (vierteljährlich)
- Konfigurationskonsistenz: Validieren, dass Staging die Produktion spiegelt (vierteljährlich)

**4.1.2 Validierung von Prozesskontrollmassnahmen**

- Beförderungsworkflow: Prüfung der letzten 30 Tage der Produktionsbereitstellungen auf Genehmigungskonformität (vierteljährlich)
- Break-Glass-Nutzung: Überprüfung der Post-Incident-Dokumentation für alle Aktivierungen (vierteljährlich)
- Zugriffsüberprüfungen: Verifizierung der Abschluss- und Ergebnislösung (vierteljährlich für Produktion, halbjährlich für Staging)
- Ausnahmenmanagement: Verifizierung, dass aktive Ausnahmen noch gerechtfertigt sind und ausgleichende Massnahmen wirksam sind (vierteljährlich)

**4.1.3 Nachweis-Validierung**

- Aktualität der Dokumentation: Verifizieren, dass Architekturdokumente den aktuellen Stand widerspiegeln (halbjährlich)
- Log-Vollständigkeit: Validieren, dass erforderliche Protokolle generiert und aufbewahrt werden (vierteljährlich)
- Schulungsunterlagen: Verifizieren, dass relevantes Personal die Schulung zur Umgebungstrennung abgeschlossen hat (jährlich)

Bewertungsergebnisse MÜSSEN im Compliance-Bewertungsregister dokumentiert werden (ISMS-IMP-A.8.31-S3) mit:

- Bewertungsdatum und Bewerter
- Bewertete Massnahmen und identifizierte Befunde
- Risikobewertung für jeden Befund (Kritisch/Hoch/Mittel/Niedrig gemäss ISMS-POL-00)
- Behebungsmassnahmen mit Zielschluss-Datum
- Ergebnisse der Nachfolgevalidierung

## Nachweisanforderungen

[Organisation] MUSS Compliance-Nachweise pflegen, einschliesslich:

- Umgebungsarchitektur-Dokumentation
- Zugangskontrollmatrizen pro Umgebung
- Dokumentation des Beförderungsworkflows
- Unterlagen zu Zugriffsüberprüfungen
- Break-Glass-Aktivierungsprotokolle und Post-Incident-Reviews
- Dokumentation der Datenverarbeitungsverfahren
- Compliance-Bewertungsberichte

## Nichtkonformität

Verstösse gegen diese Richtlinie können zu Folgendem führen:

- Sofortiger Zugangsregelung
- Disziplinarischen Massnahmen gemäss HR-Richtlinien
- Vorfallsmeldung an Aufsichtsbehörden, wenn erforderlich
- Behebungsmassnahmen-Verfolgung im Risikoregister

---

# Ausnahmenmanagement

## Ausnahmenkriterien

Ausnahmen DÜRFEN NUR genehmigt werden für:

- Legacy-Systeme, die für die Stilllegung innerhalb von 12 Monaten geplant sind
- Technische Einschränkungen, bei denen eine Trennung nicht durchführbar ist (mit dokumentierter Begründung)
- Temporäre Ausnahmen während Migrations- oder Transformationsprojekten

## Ausnahmenprozess

1. **Antrag**: Systemeigentümer dokumentiert Begründung, Risikobeurteilung, ausgleichende Massnahmen und Behebungsplan
2. **Überprüfung**: Information Security Manager validiert Begründung und ausgleichende Massnahmen
3. **Genehmigung**: ISB genehmigt oder lehnt ab mit optionalen zusätzlichen Massnahmen
4. **Verfolgung**: Ausnahme im Risikoregister mit Ablaufdatum verfolgt
5. **Neugenehmigung**: Ausnahmen laufen ab und erfordern Neugenehmigung gemäss definierter Laufzeit

## Ausgleichende Massnahmen

Bei genehmigten Ausnahmen MÜSSEN ausgleichende Massnahmen eine oder mehrere der folgenden Massnahmen umfassen:

- Erweiterte Zugangsprotokollierung und -überwachung
- Verbindliches Code-Review für alle Änderungen
- Nur-Lese-Zugangsrestriktionen
- Datenmaskierungsanforderungen
- Erhöhte Änderungsmanagement-Stringenz
- Häufigere Sicherheitsbewertungen

---

# Zugehörige Dokumente

## ISMS-Framework-Dokumente

| Dokument-ID | Titel |
|-------------|-------|
| ISMS-POL-00 | Regulatorischer Anwendbarkeitsrahmen |
| ISMS-POL-A.8.25-26-29 | Sicheres Entwicklungsrahmenwerk |
| ISMS-POL-A.8.32 | Änderungsmanagement |
| ISMS-POL-A.5.15-16-18 | Identitäts- und Zugriffsmanagement |
| ISMS-POL-A.8.2-3-5 | Authentifizierung und Privileged-Access-Management |

## Umsetzungsdokumente

| Dokument-ID | Titel |
|-------------|-------|
| ISMS-IMP-A.8.31-S1 | Umsetzung der Umgebungsarchitektur |
| ISMS-IMP-A.8.31-S2 | Umsetzung der Umgebungszugriffskontrolle |
| ISMS-IMP-A.8.31-S3 | Bewertung und Dashboard zur Umgebungstrennung |

## Referenzdokumente

| Dokument-ID | Titel |
|-------------|-------|
| ISMS-REF-A.8.31-Environment-Architecture-Patterns | Umgebungsarchitektur-Muster |
| ISMS-REF-A.8.31-CICD-Pipeline-Integration | CI/CD-Pipeline-Integration |

## Externe Standards

- ISO/IEC 27001:2022 — Massnahme A.8.31
- ISO/IEC 27002:2022 — Umsetzungsleitlinien für A.8.31
- NIST SP 800-53 Rev. 5 — CM-7 (Least Functionality), SA-11 (Developer Testing)

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Anonymisierung** | Irreversibler Prozess zur Entfernung personenbezogener Daten, sodass Personen nicht re-identifiziert werden können |
| **Break-Glass-Zugang** | Notfallverfahren, das Entwicklern während erklärter Vorfälle vorübergehenden Produktionszugang ermöglicht |
| **Umgebung** | Eigenständiger Satz von Infrastrukturressourcen für einen bestimmten SDLC-Zweck |
| **Privileged Access Management (PAM)** | System zur Verwaltung und Sicherung privilegierter Zugangsdaten |
| **Produktionsumgebung** | Live-Betriebsumgebung für echte Benutzer mit echten Geschäftsdaten |
| **Beförderung** | Prozess der Überführung von Änderungen von einer Umgebung in eine andere durch einen definierten Workflow |
| **Pseudonymisierung** | Reversibler Prozess, der Identifikatoren durch Pseudonyme ersetzt (gilt weiterhin als personenbezogene Daten) |
| **Staging-Umgebung** | Pre-Production-Umgebung, die die Produktion für die finale Validierung spiegelt |
| **Synthetische Daten** | Künstlich generierte Daten, die keine echten personenbezogenen Informationen enthalten |

---

# Nachweise für diese Richtlinie

**Stufe 1 (Dokumentationsüberprüfung) — Erforderliche Nachweise:**

Nachweise, die belegen, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.8.31 v1.0)
- ✅ Genehmigungsunterschriften von ISB, ITL, Geschäftsleitung
- ✅ Anforderungen an die Umgebungstrennung definiert
- ✅ Produktionszugangsbeschränkungen dokumentiert
- ✅ Datenverarbeitungsanforderungen spezifiziert
- ✅ Rollen und Verantwortlichkeiten zugewiesen
- ✅ Bewertungsanforderungen dokumentiert

**Stufe 2 (Operative Wirksamkeit) — Erforderliche Nachweise:**

Nachweise, die belegen, dass diese Richtlinie operativ wirksam ist:

- Umgebungsarchitektur-Dokumentation
- Zugangskontrollmatrizen pro Umgebung
- Dokumentation des Beförderungsworkflows
- Unterlagen zu Zugriffsüberprüfungen
- Break-Glass-Aktivierungsprotokolle und Post-Incident-Reviews
- Dokumentation der Datenverarbeitungsverfahren
- Compliance-Bewertungsberichte

---

# Genehmigungsprotokoll

| Funktion | Name | Unterschrift | Datum |
|----------|------|-------------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | | [Date to be set] |
| **IT-Leiter (ITL)** | [Name] | | [Date to be set] |
| **IT Operations Manager** | [Name] | | [Date to be set] |
| **Development Manager** | [Name] | | [Date to be set] |
| **Datenschutzbeauftragter (DSB)** | [Name] | | [Date to be set] |
| **Rechts-/Compliance-Beauftragter** | [Name] | | [Date to be set] |
| **Geschäftsführer (GF)** | [Name] | | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen an die Trennung von Entwicklungs-, Test- und Produktionsumgebungen fest. Umsetzungsverfahren sind in ISMS-IMP-A.8.31-S1, S2 und S3 dokumentiert.*

<!-- QA_VERIFIED: 2026-03-29 -->

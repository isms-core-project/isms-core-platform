<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.33-34-DE:framework:POL:a.8.33-34 -->
**ISMS-POL-A.8.33-34 — Schutz von Testinformationen und Audit-Aktivitäten**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Schutz von Testinformationen und Audit-Aktivitäten |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.33-34 |
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
| 1.0 | [Date to be set] | ISB | Erste konsolidierte Richtlinie für ISO 27001:2022 Zertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL) / IT-Betriebsleiter
- Datenschutz: Datenschutzbeauftragter (DSB)
- Compliance: Rechts-/Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung (GF)

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.8.11 (Datenmaskierung)
- ISMS-POL-A.8.31 (Umgebungstrennung)
- ISMS-IMP-A.8.33-34.1-UG (Testdatenschutz – Benutzerhandbuch)
- ISMS-IMP-A.8.33-34.1-TG (Testdatenschutz – Technische Spezifikation)
- ISMS-IMP-A.8.33-34.2-UG (Verwaltung von Audit-Aktivitäten – Benutzerhandbuch)
- ISMS-IMP-A.8.33-34.2-TG (Verwaltung von Audit-Aktivitäten – Technische Spezifikation)
- ISO/IEC 27001:2022 Controls A.8.33 und A.8.34

---

# Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen von [Organisation] zum Schutz von Testinformationen und zur Absicherung von Informationssystemen während Audit-Tests gemäss ISO/IEC 27001:2022 Controls A.8.33 und A.8.34 fest.

**Geltungsbereich**: Diese Richtlinie gilt für alle Aktivitäten zur Auswahl und zum Schutz von Testdaten, alle Audit- und Sicherheitstestaktivitäten, alle Umgebungen, in denen Tests stattfinden, sowie alle am Test- und Audit-Betrieb beteiligten Personen.

**Zweck**: Organisatorische Anforderungen an den Testdatenschutz und Audit-Testkontrollen definieren und dabei festlegen, WAS für Schutzmaßnahmen erforderlich sind und WER verantwortlich ist. Umsetzungsverfahren (WIE) sind separat in ISMS-IMP-A.8.33-34 dokumentiert.

**Grundprinzipien**:

- Testdaten DÜRFEN KEINE ungeschützten Produktions-Personendaten oder sensiblen Daten enthalten
- In Tests verwendete Produktionsdaten MÜSSEN maskiert oder anonymisiert werden
- Testumgebungen MÜSSEN von Produktionssystemen isoliert sein
- Audit-Tests SOLLEN so geplant werden, dass der Betrieb minimal gestört wird
- Audit-Tools und -Protokolle MÜSSEN geschützt und kontrolliert werden

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich des Schweizer nDSG, der EU-DSGVO und ISO/IEC 27001:2022, sowie bedingte branchenspezifische Anforderungen (PCI DSS v4.0.1, HIPAA, FINMA), sofern zutreffend.

---

# Geltungsbereich

## Im Geltungsbereich

Diese Richtlinie gilt für:

**Control A.8.33 – Testinformationen**:

- Alle Testdaten in Entwicklungs-, QA-, Staging- und Schulungsumgebungen
- Kopien von Produktionsdaten für Testzwecke
- Synthetische und generierte Testdaten
- Testdatenbanken und Datenrepositories
- Daten für User Acceptance Testing (UAT)
- Datensätze für Performance- und Lasttests
- Daten für Sicherheitstests

**Control A.8.34 – Audit-Tests**:

- Interne Sicherheitsaudits und -bewertungen
- Externe Zertifizierungsaudits (ISO 27001)
- Penetrationstests und Schwachstellenbewertungen
- Technische Compliance-Scans
- Sicherheitsbewertungen durch Dritte
- Audits zur regulatorischen Compliance

**Umgebungen**:

- Entwicklungsumgebungen
- Test-/QA-Umgebungen
- Staging-/Vorproduktionsumgebungen
- Schulungs- und Demonstrationsumgebungen
- Sandbox- und Experimentierumgebungen

**Personal**:

- Alle an Testaktivitäten beteiligten Mitarbeitenden
- Entwicklungs- und QA-Teams
- Interne und externe Auditoren
- Penetrationstest-Teams
- Drittbewerter und Berater

## Nicht im Geltungsbereich

Diese Richtlinie gilt NICHT für:

- Betrieb der Produktionsumgebung (durch Betriebsrichtlinien abgedeckt)
- Routinemässige Überwachungsaktivitäten (durch A.8.16 abgedeckt)
- Spezifikationen von Datenmaskierungstechniken (durch A.8.11 abgedeckt)
- Anforderungen an die Umgebungsarchitektur (durch A.8.31 abgedeckt)

---

# Richtlinienanforderungen – Control A.8.33: Testinformationen

## Anforderungen an die Testdatenauswahl

**REQ-TEST-001: Kein Echtbetrieb als Standard**

[Organisation] DARF KEINE operativen (Live-)Produktionsdaten mit Personendaten oder sensiblen Informationen für Tests verwenden, es sei denn, dies ist ausdrücklich genehmigt und geschützt.

**Bevorzugte Datenquellen** (nach Präferenz geordnet):
1. Synthetische Daten – künstlich generiert, kein Bezug zu Echtdaten
2. Anonymisierte Daten – irreversibel de-identifizierte Produktionsdaten
3. Maskierte/pseudonymisierte Daten – geschützte Produktionsdaten (genehmigungspflichtig)

**Begründung**: Ungeschützte Produktionsdaten in Testumgebungen schaffen Datenschutzverletzungsrisiken, regulatorische Nichtkonformität und unautorisierte Zugriffsexposition.

---

**REQ-TEST-002: Klassifizierung von Testdaten**

Testdaten MÜSSEN gemäss dem Datenklassifizierungsschema von [Organisation] klassifiziert werden:

- **Synthetische Daten** (keine Produktionsdatenquelle): Als Öffentlich oder Intern klassifiziert, je nach Geschäftskontext
- **Produktionsabgeleitete Daten** (maskiert, anonymisiert oder pseudonymisiert): Erbt die Produktionsdatenklassifizierung, bis die Maskierungsvalidierung die Nicht-Umkehrbarkeit bestätigt, danach kann mit Genehmigung des Dateneigentümers eine Herabstufung erfolgen
- **Direkte Produktionskopien** (während des Aktualisierungsprozesses): Als Vertraulich klassifiziert, bis Maskierung angewendet wird
- Klassifizierung bestimmt Schutzanforderungen und Zugriffskontrollen
- Genehmigung des Dateneigentümers für vertrauliche oder eingeschränkte Testdaten erforderlich

---

## Anforderungen an den Datenschutz

**REQ-TEST-003: Maskierung von Produktionsdaten**

Wenn Produktionsdaten für Tests erforderlich sind, MUSS [Organisation] Datenmaskierung gemäss ISMS-POL-A.8.11 anwenden:

- Personendaten MÜSSEN maskiert, anonymisiert oder durch synthetische Werte ersetzt werden
- Finanzdaten (Kontonummern, Zahlungskarten) MÜSSEN maskiert werden
- Zugangsdaten und Geheimnisse MÜSSEN durch Testwerte ersetzt werden
- Gesundheitsdaten MÜSSEN gemäss den anwendbaren Vorschriften de-identifiziert werden

**Maskierungsvalidierung**: Maskierte Daten MÜSSEN validiert werden, um zu bestätigen:

- Ursprüngliche sensible Werte sind nicht durch Pattern-Matching, Wörterbuchangriffe oder Re-Identifikationstechniken wiederherstellbar
- Datenformat für Anwendungskompatibilität erhalten
- Referenzielle Integrität über Datensätze hinweg aufrechterhalten

**Anforderungen an Validierungstests**:

- Validierungstests MÜSSEN beinhalten: (1) Vergleich mit Produktionsdaten-Stichproben zur Erkennung von Ähnlichkeiten im Muster, (2) Statistische Analyse zur Bestätigung von Verteilungsunterschieden gegenüber der Produktion, (3) Überprüfung, dass keine Klartext-Personendaten in Testdatenbankexporten vorhanden sind
- Validierungsergebnisse MÜSSEN dokumentiert und vom Informationssicherheitsmanager genehmigt werden, bevor die Testumgebung genutzt wird
- Validierungsverfahren sind in ISMS-IMP-A.8.33-34.1 dokumentiert

---

**REQ-TEST-004: Testdatenisolierung**

Testdaten MÜSSEN von der Produktion isoliert werden:

- Testdatenbanken MÜSSEN logisch oder physisch von der Produktion getrennt sein
- Keine direkten Zugriffspfade zwischen Test- und Produktionsdatenspeichern
- Testdatenexporte MÜSSEN kontrolliert und protokolliert werden
- Datenerneuerungsverfahren MÜSSEN eine erneute Maskierung umfassen

---

## Anforderungen an die Testumgebung

**REQ-TEST-005: Umgebungstrennung**

[Organisation] MUSS gemäss ISMS-POL-A.8.31 getrennte Testumgebungen unterhalten:

- Entwicklungs-, Test- und Produktionsumgebungen MÜSSEN getrennt sein
- Netzwerksegmentierung MUSS unautorisierte umgebungsübergreifende Zugriffe verhindern
- Für jede Umgebung MÜSSEN separate Zugangsdaten erforderlich sein
- Klare Umgebungskennzeichnung MUSS Verwechslungen verhindern

---

**REQ-TEST-006: Zugriffskontrollen**

Der Zugriff auf Testumgebungen mit sensiblen Daten MUSS:

- Das Prinzip der minimalen Rechtevergabe (Least Privilege) befolgen
- Eine ausdrückliche Autorisierung basierend auf der beruflichen Funktion erfordern
- Mindestens jährlich überprüft werden
- Bei Rollenwechsel oder Beendigung des Arbeitsverhältnisses widerrufen werden

---

## Lebenszyklus der Testdaten

**REQ-TEST-007: Datenaufbewahrung**

Testdaten mit maskierten Produktionsdaten MÜSSEN:

- Nur für die Dauer der Testanforderungen aufbewahrt werden
- Innerhalb von 30 Tagen nach Projektabschluss gelöscht werden

Bei kontinuierlichen Testumgebungen, bei denen ein "Projektabschluss" nicht klar definiert ist:

- Die Aufbewahrung von Testdaten MUSS vierteljährlich überprüft werden
- Testdaten, die älter als 90 Tage sind und keine dokumentierte aktive Nutzung aufweisen, MÜSSEN gelöscht werden, es sei denn:
  - Der Dateneigentümer erteilt eine schriftliche Genehmigung mit geschäftlicher Begründung
  - Die Ausnahme ist im Ausnahmenregister mit Ablaufdatum dokumentiert (maximal 12 Monate)
- Automatisiertes Aufbewahrungsmonitoring MUSS Daten, die Schwellenwerte überschreiten, zur Überprüfung kennzeichnen

Testdaten MÜSSEN:

- Dokumentierten Aufbewahrungs- und Löschungsverfahren folgen
- In die Überprüfung der Datenlöschung einbezogen werden

---

**REQ-TEST-008: Aktualisierung von Testdaten**

Wenn Testdaten aus der Produktion aktualisiert werden:

- Maskierung MUSS angewendet werden, bevor Daten in der Testumgebung zugänglich sind
- Aktualisierungsverfahren MÜSSEN dokumentiert und genehmigt sein
- Aktualisierungsaktivitäten MÜSSEN für Auditpurposes protokolliert werden
- Genehmigung des Dateneigentümers für geplante Aktualisierungen erforderlich

---

# Richtlinienanforderungen – Control A.8.34: Audit-Tests

## Anforderungen an die Audit-Planung

**REQ-AUDIT-001: Vorab-Audit-Vereinbarung**

[Organisation] MUSS vor jedem Audit-Test eine formelle Vereinbarung treffen:

- Umfang der zu testenden Systeme und Informationen
- Verwendete Testmethoden und -tools
- Zeitpunkt und Dauer der Testaktivitäten
- Eskalationsverfahren für entdeckte Probleme
- Vertraulichkeitsanforderungen für Audit-Feststellungen

**Vertragsparteien**: Management und Auditor/Bewerter MÜSSEN gemeinsam den Testumfang und die Methoden genehmigen, bevor Tests beginnen.

---

**REQ-AUDIT-002: Zeitpunkt und Planung**

Audit-Testaktivitäten MÜSSEN so geplant werden, dass die betrieblichen Auswirkungen minimiert werden:

- Kritische Geschäftsperioden SOLLEN vermieden werden (es sei denn, es wird gezielt die Resilienz getestet)
- Testfenster MÜSSEN mit dem IT-Betrieb koordiniert werden
- Interessengruppen MÜSSEN über geplante Testaktivitäten informiert werden
- Notfalltests MÜSSEN dem beschleunigten Genehmigungsverfahren folgen

---

## Anforderungen an Zugriffskontrollen

**REQ-AUDIT-003: Auditorenzugang**

Auditoren und Bewertern gewährter Zugriff MUSS:

- Auf den in der Vorab-Audit-Vereinbarung vereinbarten Umfang beschränkt sein
- Standardmässig Lesezugriff auf Informationen und Software
- Multi-Faktor-Authentifizierung für den Zugriff auf sensible Systeme erfordern
- Auf die Audit-Dauer zeitlich begrenzt sein
- Während des gesamten Engagements protokolliert und überwacht werden

---

**REQ-AUDIT-004: Gerätesicherheit**

Von Auditoren verwendete Geräte für den Zugriff auf die Systeme von [Organisation] MÜSSEN:

- Die Mindestsicherheitsanforderungen von [Organisation] erfüllen
- Über aktuellen Endpunktschutz und aktuelle Patches verfügen
- Keine Schadsoftware oder nicht autorisierte Software einführen
- Vor der Zugriffsgewährung überprüft werden

---

## Testkontrollen

**REQ-AUDIT-005: Testgrenzen**

Audit-Testaktivitäten MÜSSEN:

- Innerhalb der vereinbarten Umfangsgrenzen bleiben
- Nicht auf Systeme oder Daten ausserhalb des definierten Umfangs zugreifen
- Sofort stoppen, wenn unbeabsichtigte Auswirkungen auftreten
- Ausgesetzt werden, wenn kritische Probleme entdeckt werden, die den Betrieb betreffen

---

**REQ-AUDIT-006: Penetrationstest-Kontrollen**

Penetrationstests und aktive Sicherheitstests MÜSSEN:

- Schriftlich von der zuständigen Führungsebene autorisiert werden
- Soweit möglich in isolierten oder Nicht-Produktionsumgebungen durchgeführt werden
- Rollback- und Wiederherstellungsverfahren umfassen
- Den IT-Betrieb während aktiver Tests in Bereitschaft haben
- Vereinbarten Einsatzregeln (Rules of Engagement) folgen

---

## Schutz von Daten und Protokollen

**REQ-AUDIT-007: Umgang mit Audit-Daten**

Während Audits aufgerufene oder gesammelte Daten MÜSSEN:

- Gemäss ihrer Klassifizierung geschützt werden
- Nicht länger als für Auditpurposes notwendig aufbewahrt werden
- Nach Abschluss des Audits sicher gelöscht werden
- Vertraulichkeitsvereinbarungen unterliegen

---

**REQ-AUDIT-008: Schutz von Audit-Protokollen**

Während Audit-Aktivitäten erzeugte Protokolle MÜSSEN:

- Vor nicht autorisierter Änderung oder Löschung geschützt werden
- Gemäss der Protokollaufbewahrungsrichtlinie von [Organisation] aufbewahrt werden
- Zur Überprüfung verfügbar sein, wenn Audit-Feststellungen angefochten werden
- Während des Testzeitraums in das Sicherheitsmonitoring einbezogen werden

---

## Incident-Response während Audits

**REQ-AUDIT-009: Vorfallsbehandlung**

Wenn Audit-Tests unbeabsichtigte Auswirkungen verursachen:

- Tests MÜSSEN sofort ausgesetzt werden
- Der IT-Betrieb MUSS zur Eindämmung benachrichtigt werden
- Die Ursache MUSS dokumentiert werden
- Die Wiederaufnahme erfordert eine ausdrückliche Genehmigung des IT-Betriebsleiters

---

**REQ-AUDIT-010: Entdeckung von Schwachstellen**

Während Audit-Tests entdeckte Schwachstellen MÜSSEN:

- Bei kritischen Befunden sofort dem Sicherheitsteam gemeldet werden
- In den Audit-Feststellungen dokumentiert werden
- Gemäss dem Schwachstellenmanagementprozess von [Organisation] behandelt werden
- Nicht über den für die Verifikation erforderlichen Umfang hinaus ausgenutzt werden

---

# Rollen und Verantwortlichkeiten

## Governance-Rollen

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümer; genehmigt Audit-Testumfang; überprüft Compliance; autorisiert Penetrationstests |
| **IT-Betriebsleiter** | Produktionsschutz; Audit-Planung; Incident-Response während Tests |
| **Datenschutzbeauftragter (DSB)** | Datenschutz-Compliance für Testdaten; Genehmigung der Anonymisierung; regulatorische Ausrichtung |
| **Informationssicherheitsmanager** | Audit-Koordination; Teststandards; Richtlinienpflege |
| **Interne Revision** | Audit-Planung; Engagement-Management; Berichterstattung von Feststellungen |

## Operative Rollen

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Dateneigentümer** | Autorisierung von Testdaten; Genehmigung der Maskierung; Datenklassifizierungsentscheidungen |
| **Entwicklungsleiter** | Testumgebungsmanagement; Testdatenverfahren; Entwickler-Compliance |
| **QA-Manager** | Qualität der Testdaten; Compliance mit dem Testprozess; UAT-Aufsicht |
| **Sicherheitsteam** | Verwaltung von Audit-Tools; Koordination von Penetrationstests; Schwachstellenbehandlung |
| **Externe Auditoren** | Einhaltung von Zugriffsbeschränkungen; Vertraulichkeit; Umfangseinhaltung |

---

# Compliance und Durchsetzung

## Bewertungsanforderungen

| Bewertungstyp | Häufigkeit | Verantwortliche Partei |
|---------------|-----------|----------------------|
| Testdateninventur | Vierteljährlich | Entwicklungs-/QA-Manager |
| Überprüfung der Testumgebung | Halbjährlich | IT-Betrieb, Sicherheitsteam |
| Überprüfung der Auditverfahren | Jährlich | Interne Revision, ISB |
| Compliance-Bewertung | Jährlich | Informationssicherheitsmanager |

## Überprüfungsmechanismen

[Organisation] überprüft die Compliance durch:

- Automatisiertes Scanning auf sensible Daten in Testumgebungen
- Überprüfungen von Zugriffsprotokollen für den Testumgebungszugriff
- Überprüfungen der Audit-Engagement-Dokumentation
- Validierung der Wirksamkeit der Testdatenmaskierung
- Überprüfung des Abschlusses von Vorab-Audit-Checklisten

## Anforderungen an Nachweise

[Organisation] MUSS Nachweise führen, einschliesslich:

- Verfahren und Genehmigungen zur Testdatenbehandlung
- Nachweise der Maskierungsvalidierung
- Audit-Engagement-Vereinbarungen und Umfangsdokumente
- Auditorenzugriffsprotokolle und Aktivitätsaufzeichnungen
- Autorisierung von Penetrationstests und Einsatzregeln
- Vorfallsberichte aus Testaktivitäten

## Nichtkonformität

Verstösse gegen diese Richtlinie können folgendes nach sich ziehen:

- Sofortige Aussetzung von Testaktivitäten
- Widerruf des Zugriffs für nichtkonformes Personal
- Disziplinarmassnahmen gemäss HR-Richtlinien
- Vertragsbeendigung für Drittanbieter-Verstösse
- Vorfallsmeldung bei regulatorischem Verstoss

---

# Ausnahmenmanagement

## Ausnahmekriterien

Ausnahmen DÜRFEN nur genehmigt werden für:

- Legacy-Systeme, die für spezifisches Debugging Produktionsdaten benötigen
- Regulatorische Anforderungen, die spezifische Testansätze vorschreiben
- Technische Einschränkungen, die Standard-Maskierungsansätze verhindern

## Ausnahmeprozess

1. **Antrag**: Antragsteller dokumentiert geschäftliche Begründung, Risikobewertung und kompensierende Kontrollen
2. **Überprüfung**: Sicherheitsteam validiert technische Notwendigkeit und bewertet kompensierende Kontrollen
3. **Genehmigung**: ISB (Testdaten) oder IT-Betriebsleiter (Audit-Zeitpunkt) genehmigt mit Bedingungen
4. **Verfolgung**: Ausnahme wird mit Ablaufdatum und Überprüfungsplan verfolgt
5. **Überwachung**: Kompensierende Kontrollen werden während des gesamten Ausnahmezeitraums verifiziert

## Kompensierende Kontrollen

Bei genehmigten Ausnahmen MÜSSEN kompensierende Kontrollen folgendes umfassen:

- Erweiterte Zugriffsprotokollierung und -überwachung
- Verkürzte Datenaufbewahrungsfristen
- Zusätzliche Zugangsbeschränkungen
- Erhöhte Aufsicht und Überprüfungsfrequenz

---

# Regulatorische Ausrichtung

## Verbindliche Compliance

| Vorschrift | Testinformationen (A.8.33) | Audit-Tests (A.8.34) |
|-----------|---------------------------|----------------------|
| **Schweizer nDSG** | Art. 8 – Datenschutz durch Design; Minimierung personenbezogener Daten bei Tests | Art. 8 – Angemessene technische Massnahmen bei der Verarbeitung |
| **EU-DSGVO** | Art. 5(1)(c) – Datensparsamkeit; Art. 25 – Privacy by Design; Art. 32 – Pseudonymisierung | Art. 32 – Sicherheit der Verarbeitung; Tests als Sicherheitsmassnahme |
| **ISO 27001:2022** | Control A.8.33 – Auswahl und Schutz von Testinformationen | Control A.8.34 – Planung von Audit-Tests und Systemschutz |

## Bedingte Anwendbarkeit

| Vorschrift | Auslöser | Schlüsselanforderungen |
|-----------|---------|----------------------|
| **PCI DSS v4.0.1** | Zahlungskartenverarbeitung | Anf. 3.4 – Testdatenmaskierung; Anf. 11 – Sicherheitstestanforderungen |
| **HIPAA** | US-Gesundheitsdaten | De-Identifikationsstandards für Testdaten |
| **FINMA** | Schweizer Finanzdienstleistungen | Risikobasierte Testkontrollen; Auslagerungssicherheit |

---

# Verwandte Dokumente

## ISMS-Framework-Dokumente

| Dokument-ID | Titel |
|-------------|-------|
| ISMS-POL-00 | Regulatorischer Anwendbarkeitsrahmen |
| ISMS-POL-A.8.11 | Datenmaskierung |
| ISMS-POL-A.8.31 | Umgebungstrennung |
| ISMS-POL-A.8.32 | Änderungsmanagement |
| ISMS-POL-A.5.15-16-18 | Identity and Access Management |

## Umsetzungsdokumente

| Dokument-ID | Titel |
|-------------|-------|
| ISMS-IMP-A.8.33-34.1-UG | Testdatenschutz – Benutzerhandbuch |
| ISMS-IMP-A.8.33-34.1-TG | Testdatenschutz – Technische Spezifikation |
| ISMS-IMP-A.8.33-34.2-UG | Verwaltung von Audit-Aktivitäten – Benutzerhandbuch |
| ISMS-IMP-A.8.33-34.2-TG | Verwaltung von Audit-Aktivitäten – Technische Spezifikation |

## Externe Standards

- ISO/IEC 27001:2022 – Controls A.8.33, A.8.34
- ISO/IEC 27002:2022 – Umsetzungsleitlinien für A.8.33, A.8.34
- NIST SP 800-53 Rev. 5 – SA-11 (Entwicklertests), AU-11 (Aufbewahrung von Audit-Aufzeichnungen)

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Anonymisierung** | Irreversibler Prozess, der alle identifizierenden Informationen entfernt, so dass eine Re-Identifikation nicht möglich ist |
| **Audit-Test** | Systematische Prüfung von Systemen, Kontrollen und Prozessen zur Verifikation von Compliance und Wirksamkeit |
| **Datenmaskierung** | Prozess der Verschleierung von Originaldaten mit modifiziertem Inhalt unter Beibehaltung von Format und Verwendbarkeit |
| **Penetrationstest** | Autorisierter simulierter Angriff auf Systeme zur Identifikation von Sicherheitsschwachstellen |
| **Produktionsdaten** | Live-Betriebsdaten aus Geschäftssystemen mit echten Informationen |
| **Pseudonymisierung** | Ersatz von Identifikatoren durch Pseudonyme; re-identifizierbar mit separatem Schlüssel |
| **Synthetische Daten** | Künstlich generierte Daten ohne reale Personen- oder Geschäftsinformationen |
| **Testumgebung** | Nicht-Produktionssystem für Entwicklungs-, Test- oder Schulungszwecke |

---

# Nachweise für diese Richtlinie

**Stufe 1 (Dokumentationsprüfung) – Nachweise:**

Nachweise zur Demonstration, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.8.33-34 v1.0)
- ✅ Genehmigungsunterschriften von ISB, ITL, Geschäftsleitung
- ✅ Anforderungen an die Testdatenbehandlung definiert
- ✅ Audit-Schutzanforderungen dokumentiert
- ✅ Penetrationstest-Anforderungen spezifiziert
- ✅ Rollen und Verantwortlichkeiten zugewiesen

**Stufe 2 (Operative Wirksamkeit) – Nachweise:**

Nachweise zur Demonstration, dass diese Richtlinie operativ wirksam ist:

- Verfahren und Genehmigungen zur Testdatenbehandlung
- Nachweise der Maskierungsvalidierung
- Audit-Engagement-Vereinbarungen und Umfangsdokumente
- Auditorenzugriffsprotokolle und Aktivitätsaufzeichnungen
- Autorisierung von Penetrationstests und Einsatzregeln
- Vorfallsberichte aus Testaktivitäten

---

# Genehmigungsnachweis

| Rolle | Name | Unterschrift | Datum |
|-------|------|-------------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | | [Date to be set] |
| **IT-Leiter (ITL)** | [Name] | | [Date to be set] |
| **IT-Betriebsleiter** | [Name] | | [Date to be set] |
| **Datenschutzbeauftragter (DSB)** | [Name] | | [Date to be set] |
| **Revisionsleiter (Interne Revision)** | [Name] | | [Date to be set] |
| **Rechts-/Compliance-Beauftragter** | [Name] | | [Date to be set] |
| **Geschäftsführer (GF)** | [Name] | | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen für den Schutz von Tests und Audits fest. Umsetzungsverfahren sind in ISMS-IMP-A.8.33-34.1-UG/TG, .2-UG/TG und .3-UG/TG dokumentiert.*

<!-- QA_VERIFIED: 2026-03-29 -->

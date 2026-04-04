<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.33-34-DE:operational:OP-POL:a.8.33-34 -->
**ISMS-OP-POL-A.8.33-34 — Testinformationen und Schutz von Informationssystemen bei Audit-Tests**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Testinformationen und Schutz von Informationssystemen bei Audit-Tests |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.33-34 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstfassung der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.8.33 — Test information
- ISO/IEC 27001:2022 Control A.8.34 — Protection of information systems during audit testing
- ISO/IEC 27002:2022 Sections 8.33 and 8.34 — Implementation guidance
- NIST SP 800-53 Rev 5 — SA-11 (Developer Testing and Evaluation), CA-8 (Penetration Testing), AU-11 (Audit Record Retention)
- CIS Controls v8 — Safeguard 3.1–3.14 (Data Protection), Safeguard 18.1–18.5 (Penetration Testing)

**Verwandte Annex-A-Controls**:

| Control | Bezug zu Testinformationen und Audit-Schutz |
|---------|----------------------------------------------|
| A.5.9 Inventar von Informationen und anderen verbundenen Assets | Testumgebungen und Audit-Tools im Asset-Inventar erfasst |
| A.5.15–16–18 Identitäts- und Zugriffsmanagement | Bereitstellung von Auditor- und Tester-Zugriffen; zeitlich begrenzte Zugriffskontrollen |
| A.5.24–28 Incident-Management-Lebenszyklus | Vorfallsbehandlung während Audit-Tests; Eskalation bei Schwachstellenentdeckung |
| A.5.34 Datenschutz und personenbezogene Daten | Schutz personenbezogener Daten in Testdaten; Anonymisierungs- und Pseudonymisierungsanforderungen |
| A.8.2–3–5 Authentifizierung und privilegierter Zugriff | MFA-Anforderungen für Testumgebungszugriff; Auditor-Authentifizierung |
| A.8.8 Schwachstellenmanagement | Schwachstellenbehandlung für Befunde aus Penetrationstests und Audits |
| A.8.11 Datenmaskierung | Datenmaskierungstechniken für Produktionsdaten in Testumgebungen |
| A.8.15 Protokollierung | Audit-Trail für Testdaten-Handling und Auditor-Zugriffsaktivitäten |
| A.8.16 Monitoring | Echtzeit-Monitoring während aktiver Audit- und Penetrationstests |
| A.8.31 Trennung von Entwicklungs-, Test- und Produktionsumgebungen | Umgebungsisolation zum Schutz von Testdaten |

**Verwandte interne Richtlinien**:

- Richtlinie für Identitäts- und Zugriffsmanagement
- Datenmaskierungsrichtlinie
- Protokollierungsrichtlinie
- Richtlinie für Monitoring-Aktivitäten (A.8.16)
- Schwachstellenmanagement-Richtlinie
- Incident-Management-Richtlinie
- Richtlinie zur Informationsklassifikation und -behandlung
- Umgebungstrennungsrichtlinie

---

# Richtlinie für Testinformationen und Schutz bei Audit-Tests

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass Testinformationen angemessen ausgewählt, geschützt und verwaltet werden und dass Audit-Tests und andere Sicherungsmassnahmen, die die Beurteilung operativer Systeme umfassen, geplant und vereinbart werden, um Störungen zu minimieren und gleichzeitig die Systemintegrität aufrechtzuerhalten.

Diese Richtlinie adressiert zwei komplementäre Anliegen: den Schutz sensibler Daten vor Exposition durch Testumgebungen (A.8.33) und den Schutz operativer Systeme vor unbeabsichtigten Auswirkungen während Audit- und Sicherheitstests (A.8.34).

Diese Richtlinie unterstützt den schweizerischen nDSG (revDSG) Art. 8, indem sie technische und organisatorische Massnahmen entsprechend dem Risiko zum Schutz personenbezogener Daten implementiert, die in Testumgebungen verwendet oder durch diese exponiert werden. Soweit die Organisation Daten von Personen in der EU/EWR verarbeitet, gelten ausserdem die Anforderungen der DSGVO Art. 25 (Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen) und Art. 32 (Sicherheit der Verarbeitung). Testdatenmanagement ist eine wesentliche technische Massnahme, um nachzuweisen, dass personenbezogene Daten nicht unnötig durch Nicht-Produktionsumgebungen exponiert werden.

## Geltungsbereich

Diese Richtlinie gilt für alle Aktivitäten zur Auswahl, Erstellung, zum Schutz und zur Entsorgung von Testdaten sowie für alle Audit-, Penetrationstest- und Sicherungsaktivitäten, die die Beurteilung operativer Systeme umfassen.

Dies umfasst:

- Alle Testdaten in Entwicklungs-, QA-, Staging-, UAT-, Schulungs-, Sandbox- und Demonstrationsumgebungen.
- Alle Produktionsdaten-Kopien, -Extrakte oder -Ableitungen, die für Testzwecke verwendet werden.
- Alle synthetischen, anonymisierten, pseudonymisierten und maskierten Testdatensätze.
- Alle internen Sicherheitsaudits und Bewertungen.
- Alle externen Zertifizierungsaudits (ISO 27001 und Äquivalente).
- Alle Penetrationstests, Schwachstellenbewertungen und aktiven Sicherheitstests.
- Alle Sicherheitsbewertungen durch Dritte und regulatorische Compliance-Audits.
- Alle am Testing, Audit oder Sicherungsmassnahmen beteiligten Personen, einschliesslich Mitarbeitende, Auftragnehmer, interne Auditoren, externe Auditoren und Penetrationstester.

**Nicht im Geltungsbereich**: Betrieb der Produktionsumgebung (abgedeckt durch operative Richtlinien); routinemässiges automatisiertes Monitoring (abgedeckt durch A.8.16); Spezifikationen für Datenmaskierungstechniken und Tool-Konfiguration (abgedeckt durch A.8.11); Umgebungsarchitektur und Trennungsanforderungen (abgedeckt durch A.8.31); sichere Programmierungs- und Entwicklungstestpraktiken (abgedeckt durch A.8.25–26–29).

## Grundsatz

Testdaten sind als potenzieller Vektor für Datenpannen zu behandeln. Die Standardposition ist, dass Produktionsdaten mit Personendaten, sensiblen Informationen oder vertraulichen Geschäftsdaten nicht in Testumgebungen verwendet werden dürfen. Wenn aus der Produktion abgeleitete Daten erforderlich sind, sind diese vor der Verwendung zu anonymisieren, pseudonymisieren oder zu maskieren.

Audit- und Sicherungsmassnahmen müssen mit dem für die Erreichung ihrer Ziele minimal erforderlichen Zugriff und Einfluss durchgeführt werden. Auditoren erhalten standardmässig Nur-Lese-Zugriff, Tests sind zeitlich begrenzt und umfangsbeschränkt, und operative Systeme sind vor unbeabsichtigten Störungen zu schützen.

---

## Testdatenauswahl

Die Organisation legt eine klare Präferenzhierarchie für Testdatenquellen fest.

**Testdatenquellen-Hierarchie** (in Präferenzreihenfolge):

| Priorität | Datenquelle | Beschreibung | Genehmigung erforderlich |
|-----------|-------------|-------------|--------------------------|
| 1 | **Synthetische Daten** | Künstlich generierte Daten ohne Bezug zu echten Personen oder Geschäftsdatensätzen | Development Manager |
| 2 | **Anonymisierte Daten** | Unwiderruflich de-identifizierte Produktionsdaten, bei denen eine Re-Identifikation nicht vernünftigerweise möglich ist | Information Security Manager |
| 3 | **Pseudonymisierte Daten** | Produktionsdaten mit durch Pseudonyme ersetzten Identifikatoren; mit separatem Schlüssel re-identifizierbar | Information Security Manager + Dateneigentümer |
| 4 | **Maskierte Produktionsdaten** | Produktionsdaten mit mithilfe genehmigter Maskierungstechniken verdeckten sensiblen Feldern | ISB + Dateneigentümer |
| 5 | **Direkte Produktionskopie** | Unmodifizierte Produktionsdaten (nur unter aussergewöhnlichen Umständen) | ISB + DSB + Dateneigentümer |

Direkte Produktionskopien sind nur zulässig, wenn alle anderen Optionen nachweislich unzureichend sind, mit dokumentierter Begründung, zeitlich begrenzter Genehmigung (maximal 30 Tage), erweiterten Zugriffskontrollen und obligatorischer Löschung nach Abschluss.

**Entscheidungsbaum für Testdatenquellen**:

Zur Bestimmung der geeigneten Testdatenquelle ist folgende Entscheidungslogik anzuwenden:

```
Erfordert der Test echte Dateneigenschaften (Verteilungen, Randfälle)?
+-- NEIN --> Synthetische Daten verwenden (Priorität 1)
+-- JA
    +-- Können synthetische Daten mit diesen Eigenschaften generiert werden?
        +-- JA --> Synthetische Daten verwenden (Priorität 1)
        +-- NEIN
            +-- Sind die Daten Personendaten gemäss nDSG/DSGVO?
                +-- NEIN --> Maskierte Produktionsdaten verwenden (Priorität 4)
                +-- JA
                    +-- Kann Re-Identifikation unmöglich gemacht werden?
                        +-- JA --> Anonymisierte Daten verwenden (Priorität 2)
                        +-- NEIN --> Pseudonymisierte Daten verwenden (Priorität 3)
                            (Erfordert Genehmigung von Information Security Manager + Dateneigentümer)
```

Bei einem Ergebnis von Priorität 3 oder höher sind der Dateneigentümer und der Information Security Manager vor dem Fortfahren zu konsultieren.

**Klassifikation von Testdaten**: Testdaten sind gemäss dem Informationsklassifikationsschema der Organisation einzustufen. Aus der Produktion abgeleitete Testdaten erben die Klassifikation der Quelldaten, bis Maskierung oder Anonymisierung validiert ist. Synthetische Daten werden basierend auf dem Geschäftskontext klassifiziert (typischerweise Intern). Die Klassifikation bestimmt die erforderlichen Schutzkontrollen.

---

## Testdatenschutz

### Anonymisierung und Pseudonymisierung

Wenn Produktionsdaten für Tests erforderlich sind, wendet die Organisation Datenschutztechniken an, bevor die Daten in einer Testumgebung zugänglich sind.

**Anonymisierungsanforderungen**:

- Anonymisierung muss eine Re-Identifikation unter Berücksichtigung verfügbarer Re-Identifikationsmittel, der Kosten der Re-Identifikation und des beabsichtigten Zwecks nicht vernünftigerweise ermöglichen.
- Anonymisierte Daten sind keine Personendaten mehr gemäss nDSG oder DSGVO und können mit Genehmigung des Dateneigentümers auf einer niedrigeren Stufe klassifiziert werden.
- Anonymisierungstechniken sind vor der Verwendung zu validieren und jährlich auf ihre fortbestehende Wirksamkeit zu überprüfen, unter Berücksichtigung von Fortschritten bei Re-Identifikationstechniken einschliesslich KI-gestützter Methoden.

**Pseudonymisierungsanforderungen**:

- Pseudonymisierte Daten bleiben Personendaten und sind entsprechend zu schützen.
- Der Zuordnungsschlüssel (Pseudonym-zu-Identität) ist getrennt vom pseudonymisierten Datensatz zu speichern, mit Zugriffsbeschränkung auf autorisiertes Personal.
- Pseudonymisierte Testdaten unterliegen denselben Zugriffskontrollen wie die ursprüngliche Datenklassifikation.

### Datenmaskierung

Datenmaskierung wird mit [Datenmaskierungs-Tool] durchgeführt (z.B. Informatica, Delphix, IBM InfoSphere Optim oder Äquivalent) oder mithilfe genehmigter skriptbasierter Methoden.

**Maskierungsanforderungen**:

| Datentyp | Maskierungstechnik | Validierung |
|----------|-------------------|-------------|
| Personennamen | Substitution durch synthetische Namen | Verifizieren, dass keine Originalnamen verbleiben |
| E-Mail-Adressen | Domain-Ersatz (z.B. @example.com) | Format beibehalten, keine echten Adressen vorhanden |
| Nationale Kennzeichen (AHV/SSN) | Format-erhaltende Randomisierung | Format gültig, aber nicht existent |
| Finanzdaten (IBAN, Kontonummern) | Format-erhaltende Verschlüsselung oder Randomisierung | Format beibehalten, referentielle Integrität gewahrt |
| Geburtsdaten | Datumsverschiebung (konsistenter Offset pro Datensatz) | Altersverteilungen für Tests beibehalten |
| Freitextfelder | Schwärzung oder synthetischer Ersatz | Kein personenbezogener Daten-Leck in unstrukturiertem Text |
| Adressen | Substitution durch synthetische Adressen | Geografische Verteilung bei Bedarf beibehalten |

**Kurzreferenz für Datenmaskierung**:

Die folgende Tabelle bietet eine Kurzreferenz für gängige Datentypen und empfohlene Maskierungsansätze:

| Datentyp | Empfohlene Technik | Tool/Methode (Beispiel) |
|----------|-------------------|-------------------------|
| Namen | Substitution | Faker-Bibliothek: `fake.name()` (Schweizer Locale) |
| E-Mails | Domain-Swap | `user123@testdomain.example` |
| Telefonnummern | Format-erhaltende Randomisierung | Faker-Bibliothek: `fake.phone_number()` |
| Datumsangaben | Konsistenter Offset | Alle Datumsangaben um zufälligen +/- 1-3 Jahre verschieben |
| Adressen | Substitution | Faker-Bibliothek: `fake.address()` (Schweizer Locale) |
| Freitext | Schwärzung oder NER + Ersatz | Cloud-NLP-Dienst + benutzerdefinierte Ersatzlogik |
| Finanzwerte | Format-erhaltende Verschlüsselung | FPE-Algorithmus mit genehmigtem Schlüsselmanagement |

**Maskierungsvalidierung**: Maskierte Daten sind vor der Freigabe in Testumgebungen zu validieren, um zu bestätigen, dass originale sensible Werte nicht wiederhergestellt werden können, das Datenformat für die Applikationskompatibilität erhalten bleibt, die referentielle Integrität über verwandte Datensätze hinweg aufrechterhalten wird und kein Klartext-Personendaten im maskierten Output vorhanden sind. Validierungsergebnisse sind zu dokumentieren und vom Information Security Manager zu genehmigen.

### Synthetische Datengenerierung

Wenn synthetische Daten verwendet werden, sind diese so zu generieren, dass die statistischen Eigenschaften, Datenverteilungen und die referentielle Integrität für effektives Testing erhalten bleiben, ohne echte persönliche oder Geschäftsdaten zu enthalten.

Synthetische Datengeneratoren sind zu dokumentieren, versionszukontrollieren und regelmässig zu überprüfen, um sicherzustellen, dass die generierten Daten dem Zweck entsprechen. Die Organisation führt Aufzeichnungen über Parameter der synthetischen Datengenerierung und Validierungsergebnisse.

---

## Testdaten-Lebenszyklus

### Erstellung und Bereitstellung

- Testdatenerstellung oder -aktualisierung ist über einen dokumentierten Prozess anzufordern.
- Genehmigung des Dateneigentümers ist erforderlich, bevor aus der Produktion abgeleitete Daten in eine Testumgebung gelangen.
- Maskierung oder Anonymisierung ist anzuwenden, bevor Daten in der Testumgebung zugänglich sind (nicht danach).
- Alle Datenbereitsstellungsaktivitäten sind für Auditzwecke zu protokollieren.

### Aufbewahrung und Entsorgung

Testdaten mit maskierten oder pseudonymisierten Produktionsdaten sind nur für die Dauer des Testbedarfs aufzubewahren. Nach Projektabschluss sind Testdaten innerhalb von 30 Tagen zu löschen.

Für kontinuierliche Testumgebungen:

- Testdaten sind vierteljährlich auf fortbestehenden Bedarf zu überprüfen.
- Daten, die älter als 90 Tage sind, ohne dokumentierte aktive Nutzung, sind für die Löschung zu kennzeichnen.
- Aufbewahrung über 90 Tage hinaus erfordert Genehmigung des Dateneigentümers mit dokumentierter geschäftlicher Begründung.
- Automatisiertes Aufbewahrungsmonitoring meldet Überschreitungen von Schwellenwerten.

**Entsorgung**: Testdaten-Entsorgung folgt denselben sicheren Löschverfahren wie Produktionsdaten gleicher Klassifikation. Entsorgung ist zu verifizieren und zu dokumentieren.

### Datenaktualisierung

Wenn Testdaten aus Produktionsquellen aktualisiert werden:

- Frische Maskierung ist auf jeden Aktualisierungszyklus anzuwenden (frühere Maskierung gilt nicht für aktualisierte Daten).
- Aktualisierungsverfahren sind zu dokumentieren und vom Dateneigentümer zu genehmigen.
- Aktualisierungsaktivitäten sind zu protokollieren, einschliesslich Quellsystem, Volumen, Maskierungsmethode und ausführende Person.
- Vorherige Testdaten sind vor oder unmittelbar nach Abschluss der Aktualisierung sicher zu löschen.

---

## Auditplanung und Governance

### Vorab-Vereinbarung für Audits

Vor dem Beginn von Audit-Tests richtet die Organisation eine formale Vereinbarung zwischen dem Tester und der zuständigen Führungskraft ein, die Folgendes abdeckt:

- **Umfang**: Zu testende Systeme, Netzwerke, Applikationen und Daten.
- **Methodik**: Einzusetzende Testmethoden, Tools und Techniken.
- **Zeitplanung**: Start- und Enddatum, Testfenster und etwaige Sperrzeiten.
- **Grenzen**: Systeme und Daten, die explizit vom Testing ausgeschlossen sind.
- **Eskalation**: Verfahren für Probleme, Vorfälle oder kritische Befunde während des Tests.
- **Vertraulichkeit**: Anforderungen an die Nichtoffenlegung von Auditbefunden und zugegriffenen Daten.
- **Berichterstattung**: Erwartete Liefergegenstände, Format und Zeitplan für Befunde.

Vorab-Vereinbarungen sind zu dokumentieren, von beiden Parteien zu unterzeichnen und als Nachweis aufzubewahren.

### Terminplanung und Koordination

Audit-Testaktivitäten sind so zu planen, dass die betrieblichen Auswirkungen minimiert werden:

- Kritische Geschäftsperioden (z.B. Monatsabschluss, Handelsspitzen, Systemwartungsfenster) sind zu vermeiden, ausser wenn speziell die Resilienz in diesen Perioden getestet wird.
- Testfenster sind mit IT Operations und den relevanten Systemeigentümern zu koordinieren.
- Betroffene Stakeholder sind über geplante Testaktivitäten, einschliesslich Zeitpunkt, Umfang und potenzielle Auswirkungen, zu informieren.
- Notfall- oder ungeplante Tests folgen einem beschleunigten Genehmigungsverfahren mit nachträglicher Überprüfung innerhalb von 48 Stunden.

---

## Zugriffssteuerung für Auditoren

Auditoren, Bewertern und Penetrationstestern gewährter Zugriff folgt dem Prinzip der minimalen Rechtevergabe.

**Zugriffsanforderungen**:

| Anforderung | Standard |
|-------------|----------|
| Standard-Zugriffsebene | Nur lesend auf Informationen und Software |
| Schreib- oder Admin-Zugriff | Nur wenn Nur-Lese-Zugriff unzureichend ist; Administrator führt Zugriff auf Anfrage des Auditors durch, wo machbar |
| Authentifizierung | MFA erforderlich für Zugriff auf jedes System mit sensiblen Daten |
| Dauer | Zeitlich begrenzt auf die vereinbarte Auditperiode; automatischer Ablauf |
| Umfang | Auf im Vorab-Vertrag definierte Systeme und Daten beschränkt |
| Protokollierung | Gesamter Auditorzugriff wird während des gesamten Auftrags protokolliert und überwacht |

Wo Nur-Lese-Zugriff nicht machbar ist, führt ein Administrator mit den erforderlichen Zugriffsrechten System- oder Datenzugriff im Auftrag des Auditors durch, während der Auditor beobachtet und Anweisungen gibt.

**Gerätesicherheit**: Vor der Zugriffserteilung verifiziert die Organisation, dass Auditor-Geräte Mindestsicherheitsanforderungen erfüllen, einschliesslich aktueller Betriebssystem-Patches, aktivem Endpunktschutz, vollständiger Festplattenverschlüsselung und keiner bekannten Malware. Auditoren mit nicht konformen Geräten erhalten organisationsverwaltete Geräte oder virtuellen Desktop-Zugriff.

**Zugangsentzug**: Der Auditor-Zugriff ist innerhalb von 24 Stunden nach Abschluss des Audits oder dem vereinbarten Zugriffsablaufdatum widerrufen, je nachdem, was früher eintritt. Deprovisioning ist zu verifizieren und zu dokumentieren.

---

## Penetrationstest-Kontrollen

### Autorisierung und Rules of Engagement

Penetrationstests und aktive Sicherheitstests sind schriftlich vom ISB (oder Stellvertreter) und den relevanten Systemeigentümern zu autorisieren, bevor das Testing beginnt.

**Rules of Engagement** dokumentieren:

- Autorisierten Testumfang (IP-Bereiche, Applikationen, Konten, physische Standorte).
- Verbotene Aktivitäten (Denial of Service, Social Engineering spezifischer Personen, Exfiltration echter Daten).
- Testmethodik und Rahmen (z.B. OWASP Testing Guide, PTES, NIST SP 800-115).
- Kommunikationsprotokolle (Hauptkontakt, Notfallkontakt, Häufigkeit der Statusberichterstattung).
- Datenverarbeitungsanforderungen für während des Tests zugegriffene Daten.
- Vorfallsverfahren, wenn das Testing unbeabsichtigte betriebliche Auswirkungen verursacht.
- Handhabung und sichere Vernichtung von Test-Artefakten.

### Betriebliche Sicherheitsvorkehrungen

Während Penetrationstests:

- IT Operations steht in Bereitschaft mit der Fähigkeit einzugreifen, wenn operative Systeme betroffen sind.
- Tests werden wo möglich in isolierten oder Nicht-Produktionsumgebungen durchgeführt.
- Wenn Produktionstests erforderlich sind, sind Rollback- und Wiederherstellungsverfahren im Voraus vorzubereiten.
- Tests sind sofort auszusetzen, wenn unbeabsichtigte betriebliche Auswirkungen auftreten, und ohne explizite Genehmigung des IT-Operations-Managers und ISB nicht wiederaufzunehmen.

### Befundsmanagement

- Kritische Schwachstellen, die während des Tests entdeckt werden, sind dem Security Team unverzüglich zu melden (nicht auf den Abschlussbericht zu verschieben).
- Schwachstellen werden gemäss dem Schwachstellenmanagementprozess der Organisation (A.8.8) behandelt.
- Tester dürfen Schwachstellen nicht über den für Verifizierung und Risikobewertung notwendigen Umfang hinaus ausnutzen.
- Penetrationstest-Berichte sind als Vertraulich einzustufen und nur an autorisierte Empfänger zu verteilen.

### Kommunikation des Teststatus

Während aktiver Penetrationstests oder erweiterter Audit-Aufträge stellt der Tester dem designierten Organisationskontakt tägliche Statusaktualisierungen bereit. Statusaktualisierungen umfassen:

- Zusammenfassung der im Berichtszeitraum abgeschlossenen Aktivitäten.
- Zusammenfassung der identifizierten Befunde (nach Schweregrad: Kritisch, Hoch, Mittel, Niedrig).
- Geplante Aktivitäten für den nächsten Berichtszeitraum.
- Aufgetretene Probleme, Bedenken oder beobachtete betriebliche Auswirkungen.

Kritische Befunde sind dem ISB zusätzlich zu jeder täglichen Statusaktualisierung unverzüglich telefonisch zu melden. Format und Häufigkeit der Statusberichterstattung werden in der Vorab-Vereinbarung festgelegt.

---

## Audit-Tool-Management

### Tool-Genehmigung und -Kontrolle

Für die Beurteilung der Organisationssysteme verwendete Audit- und Test-Tools:

- Sind vor der Verwendung auf Organisationssystemen vom Information Security Manager vorab zu genehmigen.
- Sind als frei von Malware oder unautorisierten Funktionen zu verifizieren.
- Sind in der Vorab-Vereinbarung zu dokumentieren (Tool-Name, Version, Zweck).
- Sind auf den vereinbarten Testumfang zu beschränken.

Audit-Tools dürfen ohne explizite ISB-Genehmigung nicht auf Produktionssystemen installiert werden. Wo möglich sind Audit-Tools von dedizierten Audit-Workstations oder isolierten virtuellen Umgebungen aus zu betreiben.

### Tool-Schutz

Audit-Tools, Skripte und Konfigurationsdateien sind sowohl während als auch nach dem Auftrag vor unberechtigtem Zugriff zu schützen. Tools, die zur Ausnutzung von Schwachstellen oder zur Umgehung von Sicherheitskontrollen in der Lage sind, sind nach Abschluss des Audits von Organisationssystemen zu entfernen.

---

## Audit-Log-Schutz

Während Audit- und Testaktivitäten generierte Protokolle sind vor unberechtigter Modifikation oder Löschung zu schützen, um die Integrität des Audit-Trails aufrechtzuerhalten.

**Log-Schutzanforderungen**:

- Audit-Protokolle sind in manipulationssicheren Speicher zu schreiben (z.B. Einmalbeschreibemedien, SIEM mit Integritätskontrollen oder Äquivalent).
- Protokolle erfassen: Zeitstempel (UTC), Benutzeridentität, Quell-IP, durchgeführte Aktion, betroffenes System und Ergebnis (Erfolg/Fehler).
- Während Audit-Tests generierte Protokolle werden gemäss der Log-Aufbewahrungsrichtlinie der Organisation aufbewahrt (mindestens 1 Jahr für Zugriffsereignisse, 3 Jahre für Sicherheitsereignisse).
- Protokolle sind für die Überprüfung verfügbar, wenn Auditbefunde angefochten werden oder eine Klärung erfordern.
- Während aktiver Penetrationstests ist erweitertes Monitoring zu aktivieren, um autorisierte Testaktivitäten von echten Sicherheitsereignissen zu unterscheiden.

---

## Vorfallsbehandlung während Audit-Tests

Wenn Audit- oder Penetrationstests unbeabsichtigte betriebliche Auswirkungen verursachen:

1. **Sofortige Aussetzung**: Tests werden sofort nach Erkennung unbeabsichtigter Auswirkungen eingestellt.
2. **Benachrichtigung**: IT Operations wird für Eindämmung und Wiederherstellung benachrichtigt.
3. **Ursachenanalyse**: Die Ursache der unbeabsichtigten Auswirkung wird dokumentiert.
4. **Behebung**: Betroffene Systeme werden in den normalen Betrieb zurückgesetzt.
5. **Genehmigung zur Wiederaufnahme**: Tests dürfen ohne explizite Genehmigung des IT-Operations-Managers nicht wiederaufgenommen werden.
6. **Erkenntnisse**: Vorfall ist zu dokumentieren und in die zukünftige Vorab-Auditplanung einzubeziehen.

Echte Sicherheitsvorfälle, die während Audit-Tests entdeckt werden (z.B. Hinweise auf frühere Kompromittierungen, aktive Bedrohungen), sind sofort gemäss dem Incident-Management-Prozess der Organisation zu eskalieren (A.5.24-28).

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Anonymisierung** | Unwiderruflicher Prozess der Entfernung aller identifizierenden Informationen, so dass Re-Identifikation nicht vernünftigerweise möglich ist |
| **Audit-Testing** | Systematische Untersuchung von Systemen, Kontrollen und Prozessen zur Verifizierung der Compliance und Wirksamkeit |
| **Datenmaskierung** | Prozess der Verdeckung originaler Daten durch modifizierte Inhalte unter Beibehaltung von Format und Verwendbarkeit für Tests |
| **Grey-Box-Testing** | Penetrationstest-Ansatz, bei dem der Tester partielles Wissen über die Zielumgebung hat |
| **Penetrationstest** | Autorisierter simulierter Angriff auf Systeme zur Identifikation ausnutzbarer Sicherheitsschwachstellen |
| **Produktionsdaten** | Live-operative Daten aus Geschäftssystemen mit echten persönlichen oder Geschäftsinformationen |
| **Pseudonymisierung** | Ersatz direkter Identifikatoren durch Pseudonyme; mit einem separat gespeicherten Zuordnungsschlüssel re-identifizierbar |
| **Rules of Engagement** | Dokumentierte Vereinbarung, die Umfang, Grenzen, Methoden und Einschränkungen für Penetrationstests definiert |
| **Synthetische Daten** | Künstlich generierte Daten ohne echte persönliche oder Geschäftsinformationen, die Produktionsdateneigenschaften nachahmen |
| **Testumgebung** | Nicht-produktive Systeme, die für Entwicklungs-, Test-, Schulungs- oder Demonstrationszwecke verwendet werden |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Autorisierung von Penetrationstests; Genehmigung von Ausnahmen für direkte Produktionsdatenverwendung; Aufsicht über Audit-Testing-Governance; jährliche Richtlinienüberprüfung; Berichterstattung an Geschäftsleitung |
| **Information Security Manager** | Richtlinienpflege; Audit-Koordination; Genehmigung der Maskierungsvalidierung; Ausnahmenüberprüfung; Compliance-Monitoring; vierteljährliche Berichterstattung an ISB |
| **Datenschutzbeauftragter** | Datenschutz-Compliance von Testdaten; Überprüfung der Anonymisierungsadäquanz; nDSG- und DSGVO-Alignment; Genehmigung für pseudonymisierte Datenverwendung |
| **IT-Operations-Manager** | Schutz von Produktionssystemen während Audit-Tests; Terminplanungskoordination; Incident Response während Tests; Verifizierung der Auditor-Geräte |
| **Dateneigentümer** | Testdatengenehmigung; Maskierungsgenehmigung; Datenklassifikationsentscheidungen; Aufbewahrungsüberprüfung für von ihren Systemen abgeleitete Testdaten |
| **Development Manager / QA Manager** | Testumgebungsmanagement; Testdaten-Bereitstellungsverfahren; Entwickler- und Tester-Compliance; Aufsicht über die Generierung synthetischer Daten |
| **Security Team** | Audit-Tool-Management; Penetrationstest-Koordination; Schwachstellenbefundsbehandlung; erweitertes Monitoring während Tests |
| **Interne Revision** | Auditplanung und Auftragsmanagement; Vorbereitung der Vorab-Vereinbarungen; Befundsberichterstattung und Follow-up |
| **Externe Auditoren und Penetrationstester** | Einhaltung von Zugangsbeschränkungen, Rules of Engagement und Vertraulichkeitsanforderungen; Umfangseinhaltung; sofortige Meldung kritischer Befunde |
| **Alle Testpersonen** | Einhaltung der Testdaten-Handhabungsanforderungen; keine Verwendung unmaskierter Produktionsdaten ohne Genehmigung; Vorfallsmeldung; sichere Entsorgung von Test-Artefakten |

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| # | Nachweis | Verantwortlich | Häufigkeit | Aufbewahrung |
|---|----------|----------------|-----------|--------------|
| 1 | **Testdateninventar** mit allen Testdatensätzen, Quellentyp (synthetisch/anonymisiert/maskiert), Klassifikation und verantwortlichem Team | Development Manager / QA Manager | Fortlaufend gepflegt; vierteljährlich überprüft | Lebensdauer des Datensatzes + 1 Jahr |
| 2 | **Testdatenanforderungs- und Genehmigungsaufzeichnungen** (Anfragen, Begründungen, Dateneigentümer-Genehmigungen, verwendete Maskierungsmethode) | Dateneigentümer / Information Security Manager | Pro Anfrage | 3 Jahre |
| 3 | **Datenmaskierungsvalidierungsaufzeichnungen** (Validierungstestergebnisse, Information-Security-Manager-Genehmigung, Datum) | Information Security Manager / Security Team | Pro Maskierungsoperation | 3 Jahre |
| 4 | **Synthetische Datengenerierungsaufzeichnungen** (Generatorparameter, Validierungsergebnisse, Version) | Development Manager | Pro Generierung | 2 Jahre |
| 5 | **Testdaten-Aufbewahrungen- und Entsorgungsaufzeichnungen** (vierteljährliche Überprüfungen, Löschungsbestätigungen, Entsorgungsmethode) | Development Manager / QA Manager | Vierteljährliche Überprüfung; pro Entsorgungsereignis | 3 Jahre |
| 6 | **Vorab-Vereinbarungen für Audits und Penetrationstests** (Umfang, Methodik, Zeitplanung, Rules of Engagement, Unterschriften) | ISB / Interne Revision | Pro Auftrag | 3 Jahre |
| 7 | **Auditor- und Tester-Zugangsaufzeichnungen** (Zugangsbereitstellung, Umfang, Dauer, Deprovisioning-Bestätigung) | IT Operations / Information Security Manager | Pro Auftrag | 3 Jahre |
| 8 | **Auditor-Gerätecompliance-Verifizierungsaufzeichnungen** (Sicherheitsprüfergebnisse, Genehmigung) | IT Operations | Pro Auftrag | 1 Jahr |
| 9 | **Penetrationstest-Berichte und Befunde** (vollständige Berichte, Behebungs-Tracking, Abschlussnachweis) | ISB / Security Team | Pro Auftrag | 3 Jahre |
| 10 | **Audit-Tool-Genehmigungsaufzeichnungen** (Tool-Name, Version, Zweck, Information-Security-Manager-Genehmigung) | Information Security Manager | Pro Auftrag | 2 Jahre |
| 11 | **Audit- und Testaktivitätsprotokolle** (Auditorzugriffsprotokolle, Testaktivitätsaufzeichnungen, Monitoring-Warnungen) | IT Operations / Security Team | Kontinuierlich | Gemäss Log-Aufbewahrungsrichtlinie (1-3 Jahre) |
| 12 | **Vorfallsberichte aus Testaktivitäten** (unbeabsichtigte Auswirkungen, Grundursache, Behebung, Erkenntnisse) | IT Operations / ISB | Pro Vorfall | 3 Jahre |
| 13 | **Ausnahmeregister** (Anträge auf direkte Produktionsdatenverwendung in Testumgebungen, Genehmigungen, kompensierende Kontrollen, Ablauf) | Information Security Manager | Fortlaufend gepflegt; vierteljährlich überprüft | Ausnahmedauer + 3 Jahre |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheitsmanagement-Team verifiziert die Einhaltung dieser Richtlinie durch verschiedene Methoden, darunter unter anderem Testdateninventare, Maskierungsvalidierungsaufzeichnungen, Audit-Auftragsdokumentation, Zugriffsprotokolle, Penetrationstest-Berichte, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

**Compliance-Kennzahlen**:

| Kennzahl | Ziel | Messhäufigkeit |
|----------|------|----------------|
| Testumgebungen mit synthetischen oder anonymisierten Daten (keine unmaskierten Produktionsdaten) | >= 95% | Vierteljährlich |
| Maskierungsvalidierung vor Testdatenfreigabe abgeschlossen und genehmigt | 100% | Pro Maskierungsoperation |
| Vorab-Vereinbarungen vor Testbeginn unterzeichnet | 100% | Pro Auftrag |
| Auditor-Zugriff innerhalb von 24 Stunden nach Auditabschluss widerrufen | 100% | Pro Auftrag |
| Penetrationstest-Befunde innerhalb der SLA behoben | >= 90% | Pro Auftrag |
| Testdaten innerhalb von 30 Tagen nach Projektabschluss entsorgt | >= 90% | Vierteljährlich |

**Compliance-Bewertung**:

| Komponente | Gewichtung | Berechnung |
|------------|------------|------------|
| Testdatenschutz-Compliance | 40% | (Testumgebungen mit genehmigten Datenquellen + abgeschlossene Maskierungsvalidierungen) / Gesamte Testumgebungen × 100 |
| Audit-Governance-Compliance | 30% | (Aufträge mit unterzeichneten Vorab-Vereinbarungen + ordnungsgemäss bereitgestelltem und entzogenem Zugriff) / Gesamtaufträge × 100 |
| Befundsmanagement-Compliance | 20% | (Penetrationstest- und Auditbefunde innerhalb der SLA behoben) / Gesamtbefunde × 100 |
| Datenlebenszyklus-Compliance | 10% | (Innerhalb der Richtlinienfristen entsorgte Testdatensätze) / Gesamte entsorgungspflichtige Datensätze × 100 |

**Umgang mit Nichteinhaltung**: Ein Wert unter 70% erfordert sofortige ISB-Eskalation und einen Massnahmenplan. Ein Wert zwischen 70-89% erfordert die Aufsicht durch den Information Security Manager mit monatlichen Überprüfungen. Ein Wert von 90% und mehr folgt dem standardmässigen vierteljährlichen Monitoring.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom ISB im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, kompensierenden Kontrollen (erweiterte Protokollierung, reduzierte Aufbewahrung, zusätzliche Zugriffsbeschränkungen) und einem definierten Überprüfungsdatum (maximal 12 Monate). Ausnahmen für die direkte Produktionsdatenverwendung in Testumgebungen erfordern zusätzlich die DSB-Genehmigung. Ausnahmen sind dem Management Review Team zu berichten.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarisch belangt werden, bis hin zur Kündigung des Arbeitsverhältnisses. Die Verwendung unmaskierter Produktionsdaten in Testumgebungen ohne Genehmigung wird als Datenverwaltungsvorfall behandelt und entsprechend untersucht. Richtlinienverstösse sind zu dokumentieren, durch den Information Security Manager zu untersuchen und dem ISB zu berichten.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Fortschritte bei Anonymisierungs- und synthetischen Datengenerierungstechniken, neue Re-Identifikationsrisiken (einschliesslich KI-gestützter De-Anonymisierung), Änderungen bei Penetrationstest-Methodologien und der Bedrohungslandschaft, regulatorische Änderungen (insbesondere nDSG-Leitlinien und DSGVO-Durchsetzungspräzedenzfälle), Auditbefunde und Erkenntnisse aus Testvorfällen sowie Rückmeldungen von Entwicklungs-, QA- und Audit-Teams.

---

# Adressierte Bereiche des ISO 27001-Standards

Richtlinie für Testinformationen und Schutz bei Audit-Tests — ISO 27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Verantwortlichkeiten des Managements |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | 6.3 Sensibilisierung, Schulung und Training zur Informationssicherheit |
| Klausel 9.2 Interne Revision | 8.11 Datenmaskierung |
| | **8.33 Testinformationen** |
| | **8.34 Schutz von Informationssystemen bei Audit-Tests** |
| | 8.31 Trennung von Entwicklungs-, Test- und Produktionsumgebungen |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|----------|
| Schweizerischer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen zum Datenschutz; Anonymisierung und Pseudonymisierung als Datenschutzmassnahmen; Testdaten mit Personendaten unterliegen nDSG-Anforderungen |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1-3 — Mindestanforderungen an die Datensicherheit, einschliesslich Testumgebungskontrollen |
| EU DSGVO (sofern anwendbar) | Art. 5(1)(c) — Datensparsamkeit (keine unnötigen Produktionsdaten in Testumgebungen); Art. 25 — Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen; Art. 32 — Sicherheit der Verarbeitung (Pseudonymisierung als Sicherheitsmassnahme) |
| ISO/IEC 27001:2022 | Annex-A-Massnahmen 8.33 und 8.34 |
| ISO/IEC 27002:2022 | Abschnitte 8.33 und 8.34 — Implementierungsleitfaden |
| NIST SP 800-53 Rev 5 | SA-11 (Developer Testing and Evaluation), CA-8 (Penetration Testing), AU-11 (Audit Record Retention), SI-12 (Information Management and Retention) |
| CIS Controls v8 | 3.1-3.14 (Datenschutz), 18.1-18.5 (Penetration Testing) |

---

<!-- QA_VERIFIED: 2026-03-29 -->

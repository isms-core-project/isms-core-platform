<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.24-28-DE:operational:OP-POL:a.5.24-28 -->
**ISMS-OP-POL-A.5.24-28 — Incident Management**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Incident Management |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.24-28 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Kontrollen A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 — Planung des Incident Managements, Bewertung, Reaktion, Lernen, Beweiserhebung

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zum Incident Management |
|-----------|-------------------------------|
| A.5.5–6 Kontakt mit Behörden und Interessengruppen | Externe Meldepflichten (EDÖB, Strafverfolgung, CERT) |
| A.5.7 Bedrohungsintelligenz | Bedrohungsintelligenz unterstützt Vorfallserkennung und -reaktion |
| A.5.29 Informationssicherheit bei Störungen | Aktivierung der Geschäftskontinuität bei schwerwiegenden Vorfällen |
| A.5.34 Datenschutz und Schutz von PII | Anforderungen an die Benachrichtigung bei Datenschutzverletzungen |
| A.6.8 Meldung von Informationssicherheitsereignissen | Meldungen von Benutzern über Sicherheitsereignisse fliessen in das Incident-Triage ein |
| A.8.15 Protokollierung | Protokolldaten unterstützen Vorfallserkennung und forensische Analyse |
| A.8.16 Überwachungsaktivitäten | Überwachung erkennt Sicherheitsereignisse für das Incident-Triage |

**Verwandte interne Richtlinien**:

- Zugangskontrollrichtlinie
- Protokollierungsrichtlinie
- Richtlinie zu Überwachungsaktivitäten (A.8.16)
- Richtlinie zur Geschäftskontinuität
- Richtlinie zum Datenschutz und Schutz von PII
- Richtlinie zur Informationsklassifizierung und -handhabung

---

# Richtlinie zum Incident Management

## Zweck

Diese Richtlinie bietet Leitlinien für die strukturierte Verwaltung von Informationssicherheitsvorfällen, einschliesslich der Identifizierung, Bewertung, Reaktion und Lösung von Sicherheitsereignissen und -vorfällen sowie der Identifizierung, Erhebung, Beschaffung und Aufbewahrung von Informationen, die als Beweise dienen können.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) und die Datenschutzverordnung (DSV), indem sie Verfahren zur Benachrichtigung bei Datenschutzverletzungen und technische und organisatorische Massnahmen entsprechend dem Risiko umsetzt. Soweit die Organisation Daten von Personen in der EU/EEA verarbeitet, gelten auch die DSGVO-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle Informationssysteme, Anwendungen und Dienste, die im ISO-27001-Anwendungsbereich enthalten sind.

## Grundsatz

Alle Informationssicherheitsereignisse sollten gemeldet und bewertet werden. Bestätigte Vorfälle sollten über einen strukturierten Reaktionsprozess mit definierten Rollen, Eskalationspfaden und Kommunikationsverfahren verwaltet werden. Die Organisation sollte aus Vorfällen lernen, um ihre Sicherheitslage zu verbessern. Wenn Vorfälle zu externen Untersuchungen oder rechtlichen Verfahren führen können, sollten spezialisierte externe Ressourcen eingebunden werden.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Sicherheitsereignis** | Ein identifiziertes Vorkommnis, das auf einen möglichen Verstoss gegen die Sicherheitsrichtlinie oder ein Versagen der Kontrollen hinweist. Nicht alle Ereignisse sind Vorfälle. |
| **Sicherheitsvorfall** | Ein Sicherheitsereignis, das bewertet und als tatsächliche oder mögliche nachteilige Auswirkung auf die Vertraulichkeit, Integrität oder Verfügbarkeit von Informationen bestätigt wurde. |
| **Datenschutzverletzung** | Ein Sicherheitsvorfall mit versehentlicher oder unrechtmässiger Vernichtung, Verlust, Änderung, unbefugter Offenlegung oder unbefugtem Zugriff auf personenbezogene Daten. |
| **Schwerwiegender Vorfall** | Ein Vorfall, der einen gesetzlichen oder regulatorischen Verstoss darstellt, zu einer externen Untersuchung oder rechtlichen Verfahren führen könnte oder ein hohes Risiko für betroffene Personen schafft. |

---

## Vorfallsmeldung

Alle Mitarbeitenden und Drittnutzer sollten Sicherheitsereignisse sofort nach der Entdeckung über die designierten Meldekanäle an das Informationssicherheits-Management-Team melden:

- **Primär**: IT-Service-Desk (E-Mail, Telefon oder Ticketsystem).
- **Alternativ**: Direkter Kontakt mit dem Informationssicherheits-Management-Team (E-Mail-Verteilerliste oder Telefon).
- **Ausserhalb der Geschäftszeiten**: Sicherheitsdienst auf Abruf (Telefon oder Nachrichtendienst).
- **Anonym**: Wenn Mitarbeitende Bedenken anonym melden möchten, können Meldungen über den Whistleblowing- oder Ethik-Meldungsmechanismus der Organisation eingereicht werden.

Meldekanäle sollten bei der Einarbeitung und in der jährlichen Sensibilisierungsschulung kommuniziert und im Organisationsintranet veröffentlicht werden.

Meldungen sollten, wenn bekannt, umfassen:

- Was beobachtet wurde (Beschreibung des Ereignisses).
- Wann es eingetreten oder entdeckt wurde.
- Welche Systeme, Daten oder Personen betroffen sind.
- Bereits ergriffene Massnahmen.

Sicherheitsereignisse können auch durch automatisierte Überwachung, Protokollanalyse oder Drittparteibenachrichtigungen erkannt werden.

Mitarbeitende sollten nicht versuchen, vermutete Vorfälle selbst zu untersuchen oder zu lösen. Die Beweiserhaltung hat Vorrang vor der Neugier.

---

## Ereignisbewertung und Triage

Das Informationssicherheits-Management-Team sollte alle gemeldeten Sicherheitsereignisse bewerten, um zu bestimmen, ob sie einen Sicherheitsvorfall darstellen.

Die Bewertung sollte berücksichtigen:

- Art und Umfang des Ereignisses.
- Klassifizierung der betroffenen Informationen.
- Anzahl der betroffenen Datenpersonen oder Systeme.
- Ob personenbezogene Daten betroffen sind (mögliche Datenschutzverletzung).
- Die möglichen geschäftlichen, rechtlichen oder regulatorischen Auswirkungen.

Ereignisse, die den Schwellenwert für einen Vorfall nicht erreichen, sollten protokolliert werden, und Trends sollten überwacht werden.

### Vorfallsregister

Alle gemeldeten Sicherheitsereignisse und bestätigten Vorfälle sollten im Vorfallsregister mit den folgenden Mindestfeldern aufgezeichnet werden:

| Feld | Beschreibung |
|------|--------------|
| Vorfall-ID | Eindeutige Kennung (z. B. INC-2026-001) |
| Datum/Uhrzeit der Meldung | Wann das Ereignis gemeldet wurde |
| Datum/Uhrzeit der Entdeckung | Wann das Ereignis eingetreten oder zuerst entdeckt wurde |
| Melder | Wer das Ereignis gemeldet hat |
| Beschreibung | Zusammenfassung des Vorgefallenen |
| Betroffene Systeme/Daten | Welche Systeme, Anwendungen oder Datentypen betroffen sind |
| Klassifizierungsstufe | Klassifizierung der betroffenen Informationen |
| Personenbezogene Daten betroffen | Ja/Nein; wenn ja, Kategorien und geschätzte Anzahl der betroffenen Personen |
| Schweregrad | Kritisch / Hoch / Mittel / Niedrig |
| Status | Offen / In Untersuchung / Eingedämmt / Gelöst / Geschlossen |
| Zugewiesen an | Incident-Handler oder -Team |
| Ursache | Nach der Untersuchung bestimmt |
| Ergriffene Massnahmen | Eingrenzungs-, Beseitigungs-, Wiederherstellungsmassnahmen mit Zeitstempeln |
| Erkenntnisse | Verweis auf Post-Incident-Überprüfung (falls durchgeführt) |
| Schlussdatum | Wenn der Vorfall formell geschlossen wurde |

---

## Vorfallsklassifizierung

Bestätigte Vorfälle sollten nach Schweregrad klassifiziert werden, um Reaktionspriorität, Eskalation und Kommunikationsanforderungen zu bestimmen:

| Schweregrad | Beschreibung | Beispiele | Erstreaktion |
|-------------|--------------|-----------|--------------|
| **Kritisch** | Bestätigte Datenschutzverletzung, vollständiger Dienstausfall, aktive Kompromittierung kritischer Systeme | Ransomware, Datenexfiltration, Kompromittierung von Authentifizierungssystemen | Sofort (innerhalb von 1 Stunde) |
| **Hoch** | Erhebliche Auswirkungen auf Hauptfunktionen, mögliche Datenexposition, gezielter Angriff | Malware auf mehreren Endpunkten, unbefugter Zugriff auf sensible Daten, Phishing-Kampagne gegen Führungskräfte | Innerhalb von 4 Stunden |
| **Mittel** | Begrenzte Auswirkungen, auf einzelnes System oder Benutzer beschränkt, kein bestätigter Datenverlust | Einzelne Malware-Erkennung, Richtlinienverstoss, fehlgeschlagener Eindringversuch | Innerhalb von 1 Werktag |
| **Niedrig** | Minimale Auswirkungen, keine Daten betroffen, informativ | Spamzunahme, geringfügige Richtlinienabweichung, einzelnes fehlgeschlagenes Anmeldemuster | Innerhalb von 3 Werktagen |

Der Schweregrad kann jederzeit während des Vorfallslebenszyklus eskaliert werden, wenn neue Informationen auftauchen.

---

## Vorfallsreaktion

### Reaktionslebenszyklus

Vorfälle sollten durch die folgenden Phasen verwaltet werden, ausgerichtet an NIST SP 800-61:

1. **Eindämmung** — Auswirkungen begrenzen und weitere Schäden verhindern. Kurzfristige Eindämmungsmassnahmen (z. B. betroffene Systeme isolieren, kompromittierte Konten deaktivieren) sollten sofort ergriffen werden. Langfristige Eindämmungsstrategien sollten geplant werden, wenn eine sofortige Beseitigung nicht möglich ist.

2. **Beseitigung** — Ursache des Vorfalls entfernen. Dies kann das Entfernen von Malware, das Schliessen von Schwachstellen, das Zurücksetzen kompromittierter Anmeldedaten oder den Wiederaufbau betroffener Systeme umfassen.

3. **Wiederherstellung** — Systeme und Dienste auf den Normalbetrieb zurückführen. Die Wiederherstellung sollte durch Tests vor der Rückgabe von Systemen in die Produktion verifiziert werden. Die Überwachung sollte während der Wiederherstellungsphase intensiviert werden, um ein Wiederauftreten zu erkennen.

4. **Post-Incident-Überprüfung** — Nach der Lösung eine strukturierte Überprüfung durchführen (siehe Abschnitt Erkenntnisse unten).

Alle Vorfallsreaktionsmassnahmen sollten mit Zeitstempeln, ergriffenen Massnahmen und beteiligtem Personal dokumentiert werden.

### Incident-Response-Team

Die folgenden Rollen sollten innerhalb der Incident-Response-Kapazität zugewiesen werden:

| Rolle | Verantwortung | Zugewiesen an |
|-------|---------------|---------------|
| **Incident-Response-Team-Leiter** | Gesamtkoordination der Vorfallsreaktion; Eskalationsentscheidungen; Kommunikation mit der Geschäftsleitung | ISB oder IT-Sicherheitsmanager |
| **Technischer Leiter** | Technische Untersuchung, Eindämmung und Beseitigung; Beweiserhaltung | Leitender IT-Sicherheitsanalyst oder IT-Betriebsleiter |
| **Kommunikationsleiter** | Interne und externe Kommunikation; Medienkontakt (falls erforderlich) | ISB oder designierter Sprecher |
| **Rechtsberater** | Rechtliche Beratung zu Meldepflichten, Beweishandhabung, regulatorischen Anforderungen | Rechtsbeistand (intern oder extern) |
| **Business-Verbindung** | Bewertung der Geschäftsauswirkungen; Koordination mit betroffenen Geschäftsbereichen | Abteilungsleiter oder Geschäftskontinuitätskoordinator |

Rollenzuweisungen sollten dokumentiert, allen Teammitgliedern mitgeteilt und jährlich überprüft werden. Für jede Rolle sollten Stellvertreter benannt werden, um die Verfügbarkeit sicherzustellen.

### Eskalation

Der Incident-Response-Team-Leiter sollte Vorfälle an die Geschäftsleitung eskalieren, wenn:

- Der Vorfall als kritisch oder hoch eingestuft wird.
- Der Vorfall personenbezogene Daten umfasst (mögliche Benachrichtigung bei Datenschutzverletzung).
- Der Vorfall eine externe Benachrichtigung erfordern könnte (regulatorisch, Strafverfolgung, Kunden).
- Der Vorfall die Fähigkeit oder Autorität des Reaktionsteams übersteigt.
- Der Vorfall nicht innerhalb des erwarteten Zeitrahmens eingedämmt wurde.

### Kommunikation

Vorfallsinformationen sollten strikt auf Need-to-know-Basis geteilt werden. Die Kommunikation während eines aktiven Vorfalls sollte durch den Incident-Response-Team-Leiter koordiniert werden.

Interne Statusaktualisierungen sollten in regelmässigen Abständen für kritische und hohe Vorfälle bereitgestellt werden.

Externe Kommunikation (Medien, Kunden, Partner) sollte vor der Veröffentlichung von der Geschäftsleitung genehmigt und vom Rechtsbeistand überprüft werden.

---

## Schwerwiegende Vorfälle

Schwerwiegende Vorfälle sind definiert als Vorfälle, die einen gesetzlichen oder regulatorischen Verstoss darstellen, zu einer externen Untersuchung führen könnten oder zu rechtlichen Verfahren führen könnten.

### Übergeordnete Leitlinien

In allen Fällen, in denen eine Situation zu einer externen Untersuchung oder rechtlichen Verfahren führen könnte, sollten spezialisierte externe Ressourcen eingebunden werden.

So früh wie möglich sollten alle Arbeiten an, Zugriffe auf, Änderungen an oder Manipulationen von betroffenen Systemen, Dokumenten, Standorten, Dateien, Datenbanken, Anwendungen oder anderen betroffenen Entitäten eingestellt werden. Die einzigen Ausnahmen sind die Erhaltung von Leben, Gesundheit und Sicherheit oder die absolut notwendigen Massnahmen für Triage und Sicherung.

### Prozess

1. Einen Significant-Incident-Team-Leiter aus dem Geschäftsleitungsteam als einzigen Ansprechpartner und Koordinator ernennen.
2. Den obigen Leitlinien folgen, um zu stoppen und zu sichern.
3. Sofort den Rechtsbeistand kontaktieren.
4. Sofort einen Computer-Forensik- und Ermittlungslieferanten von einem qualifizierten und autorisierten Unternehmen kontaktieren.
5. Nach Bedarf die Behörden kontaktieren, einschliesslich Strafverfolgung, den Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB) und alle anwendbaren Branchenregulatoren.
6. Falls eine Cyber-Versicherungsdeckung besteht, sofort die Versicherungsgesellschaft informieren.
7. Den Leitlinien des Rechtsbeistands, der Strafverfolgung, der forensischen Ermittler und der Versicherungsgesellschaften folgen, während dem Incident-Management-Prozess für die Aufzeichnung, Verfolgung und Verwaltung des Vorfalls gefolgt wird.

---

## Benachrichtigung bei Datenschutzverletzungen

Wenn ein Vorfall personenbezogene Daten betrifft (eine Datenschutzverletzung), gelten die folgenden Benachrichtigungsanforderungen:

### Benachrichtigung gemäss schweizerichem nDSG

| Benachrichtigung | Auslöser | Zeitrahmen |
|-----------------|---------|------------|
| **EDÖB** (Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter) | Datenschutzverletzung, die voraussichtlich ein **hohes Risiko** für die Persönlichkeit oder die Grundrechte der betroffenen Personen zur Folge hat | **So schnell wie möglich** nach Bekanntwerden der Verletzung |
| **Betroffene Personen** | Wenn eine Benachrichtigung zum Schutz der betroffenen Personen notwendig ist oder wenn der EDÖB sie verlangt | **So schnell wie möglich** (keine feste Frist) |
| **Auftragsverarbeiter → Verantwortlicher** | Auftragsverarbeiter entdeckt eine Verletzung mit den personenbezogenen Daten des Verantwortlichen | **So schnell wie möglich** nach Entdeckung |

### EU-DSGVO-Benachrichtigung (soweit anwendbar)

| Benachrichtigung | Auslöser | Zeitrahmen |
|-----------------|---------|------------|
| **Aufsichtsbehörde** | Jede Datenschutzverletzung, es sei denn, es ist unwahrscheinlich, dass ein Risiko für Rechte und Freiheiten entsteht | **Innerhalb von 72 Stunden** nach Bekanntwerden |
| **Betroffene Personen** | Verletzung, die voraussichtlich ein **hohes Risiko** für Rechte und Freiheiten zur Folge hat | **Unverzüglich** |

Wenn sowohl nDSG als auch DSGVO gelten, sollte die Organisation die strengere Frist einhalten (72 Stunden).

### Inhalt der Benachrichtigung

Benachrichtigungen bei Verletzungen an Aufsichtsbehörden sollten mindestens umfassen:

| Element | nDSG (Art. 24) | DSGVO (Art. 33) |
|---------|-----------------|-----------------|
| Art der Verletzung | Erforderlich | Erforderlich (einschliesslich Kategorien und ungefähre Anzahl der betroffenen Personen und Datensätze) |
| Folgen und Risiken | Erforderlich | Erforderlich (wahrscheinliche Folgen) |
| Ergriffene oder geplante Massnahmen | Erforderlich | Erforderlich (ergriffene oder vorgeschlagene Massnahmen zur Behebung und Minderung) |
| Kontaktstelle | Erforderlich (wo der EDÖB oder die betroffenen Personen weitere Informationen erhalten können) | Erforderlich (Name und Kontaktdaten des DSB oder einer anderen Kontaktstelle) |

Wenn vollständige Informationen zum Zeitpunkt der Benachrichtigung nicht verfügbar sind, sollten sie in Phasen ohne unnötige Verzögerung bereitgestellt werden.

### Verletzungsbewertung

Nicht alle Sicherheitsvorfälle mit personenbezogenen Daten erfordern eine Benachrichtigung. Das Incident-Response-Team sollte bewerten:

- Art und Sensitivität der betroffenen personenbezogenen Daten.
- Anzahl der betroffenen Datenpersonen.
- Schwere und Wahrscheinlichkeit der Folgen für die betroffenen Personen.
- Ob die Daten verschlüsselt oder anderweitig unlesbar gemacht wurden.
- Ob die Verletzung eingedämmt und das Risiko gemindert wurde.

Die Bewertung und Entscheidung (einschliesslich der Begründung für eine eventuelle Nichtbenachrichtigung) sollten dokumentiert werden.

---

## Erhebung und Aufbewahrung von Beweismitteln

Wenn ein Vorfall eine forensische Analyse, rechtliche Massnahmen oder eine behördliche Untersuchung erfordern könnte, sollten Beweismittel nach folgenden Grundsätzen erhoben und aufbewahrt werden:

### Beweishandhabung

- Beweismittel sollten so schnell wie möglich nach der Identifizierung des Vorfalls erhoben werden.
- Auf die Originalbeweise sollte nicht direkt zugegriffen, sie sollten nicht modifiziert oder analysiert werden. Forensische Kopien (Bit-für-Bit-Images) sollten mit Schreibschutz-Tools erstellt werden.
- Alle Beweismittel sollten mit kryptografischen Hash-Funktionen (mindestens SHA-256) verifiziert werden, um die Integrität zu bestätigen.

### Beweiskette

Eine Beweiskettenaufzeichnung sollte für alle Beweismittel geführt werden, mit Dokumentation von:

- Was erhoben wurde (Beschreibung, Seriennummern, Kennungen).
- Wann es erhoben wurde (Datum, Uhrzeit).
- Wer es erhoben hat.
- Wo es gespeichert ist.
- Wer darauf zugegriffen hat und wann.
- Alle Übertragungen zwischen Verwahrern.

### Beweisaufbewahrung

- Beweismittel sollten an einem sicheren Ort mit eingeschränktem Zugang aufbewahrt werden.
- Digitale Beweismittel sollten auf verschlüsselten Medien gespeichert werden.
- Physische Beweismittel sollten in einem verschlossenen, manipulationssicheren Behälter aufbewahrt werden.
- Beweismittel sollten für mindestens **12 Monate** nach Vorfallsschliessung aufbewahrt werden, oder länger wenn dies vom Rechtsbeistand, regulatorischen Anforderungen oder laufenden Verfahren verlangt wird.

### Externe forensische Unterstützung

Bei schwerwiegenden Vorfällen sollten qualifizierte externe forensische Ermittler hinzugezogen werden. Die Organisation sollte mindestens einen externen forensischen Anbieter identifizieren und vorab genehmigen sowie aktuelle Kontaktdaten und Beauftragungsbedingungen (Retainer oder vorab vereinbarte Aufgabenbeschreibung) pflegen. Internes Personal sollte keine forensische Analyse durchführen, es sei denn, es ist hierfür ausgebildet und qualifiziert.

---

## Erkenntnisse

Eine Post-Incident-Überprüfung sollte für alle kritischen und hohen Vorfälle durchgeführt werden, und optional für mittlere Vorfälle, wenn nützliche Erkenntnisse gewonnen werden können.

### Überprüfungsprozess

Die Überprüfung sollte innerhalb von 5 Werktagen nach der Vorfallslösung stattfinden, während die Details noch frisch sind. Die Überprüfung sollte alle an der Reaktion beteiligten Personen einbeziehen.

Die Überprüfung sollte dokumentieren:

- **Zeitachse**: Eine sachliche Chronologie des Vorfalls von der Erkennung bis zur Lösung.
- **Ursache**: Die zugrunde liegende Ursache des Vorfalls (nicht nur der Auslöser).
- **Was funktionierte**: Effektive Reaktionsmassnahmen, erfolgreiche Eindämmungsmassnahmen, gute Teamkoordination.
- **Was verbessert werden könnte**: Erkennungslücken, Reaktionsverzögerungen, Kommunikationsprobleme, fehlende Tools oder Verfahren.
- **Massnahmen**: Spezifische, messbare Verbesserungen mit zugewiesenem Eigentümer und Frist.

### Nachverfolgung

- Massnahmen sollten bis zum Abschluss verfolgt werden.
- Erkenntnisse sollten dem relevanten Personal mitgeteilt werden.
- Der Incident-Response-Plan sollte aktualisiert werden, wenn Erkenntnisse Lücken aufzeigen.
- Trends über Vorfälle sollten vierteljährlich überprüft werden, um systemische Probleme zu identifizieren.

Überprüfungen sollten schuldfreiheitlich durchgeführt werden und auf System- und Prozessverbesserung statt auf individuelle Schuld ausgerichtet sein.

---

## Testen der Vorfallsreaktion

Der Incident-Response-Plan sollte mindestens **jährlich** durch Tabletop-Übungen oder Simulationen getestet werden, um zu verifizieren, dass:

- Rollen und Verantwortlichkeiten verstanden werden.
- Kommunikationskanäle korrekt funktionieren.
- Eskalationspfade klar und effektiv sind.
- Beweiserhebungsverfahren praktikabel sind.
- Benachrichtigungsfristen bei Datenschutzverletzungen eingehalten werden können.

**Mindest-Testszenarien** (jährlich rotierend):

| Szenario | Testet | Häufigkeit |
|----------|--------|------------|
| Ransomware-Angriff mit Datenverschlüsselung | Eindämmung, Wiederherstellung aus Backup, Kommunikation, Entscheidung Zahlen/Nicht zahlen | Mindestens alle 2 Jahre |
| Datenschutzverletzung mit Meldepflicht | Verletzungsbewertung, EDÖB-Meldeprozess, Benachrichtigung betroffener Personen | Mindestens alle 2 Jahre |
| Insider-Bedrohung / kompromittiertes privilegiertes Konto | Erkennung, Zugriffswiderruf, Beweiserhaltung, HR-Koordination | Mindestens alle 2 Jahre |
| Business-Email-Kompromittierung / Social Engineering | Erkennung, Verifizierung finanzieller Kontrollen, Vorfallsmeldung | Mindestens alle 2 Jahre |

Testergebnisse und Verbesserungen sollten dokumentiert werden, einschliesslich Teilnehmer, Szenariodetails, beobachtete Lücken und Korrekturmassnahmen mit Eigentümern und Fristen.

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

- **Vorfallsregister** (alle gemeldeten Ereignisse und bestätigten Vorfälle mit Schweregrad, Status, Lösung) — *laufend gepflegt; vierteljährlich auf Trends überprüft*
- **Vorfallsreaktionsaufzeichnungen** (Eingrenzungs-, Beseitigungs-, Wiederherstellungsmassnahmen mit Zeitstempeln) — *mindestens 3 Jahre aufbewahrt*
- **Datenschutzverletzungsbewertungs- und -meldungsaufzeichnungen** (einschliesslich Entscheidungen gegen Benachrichtigung mit Begründung) — *5 Jahre aufbewahrt*
- **Beweiskettenaufzeichnungen** für forensische Beweise — *für die Dauer jeglicher Rechtsverfahren plus 2 Jahre aufbewahrt*
- **Post-Incident-Überprüfungsberichte** mit Massnahmen und Fertigstellungsverfolgung — *innerhalb von 5 Werktagen nach Lösung abgeschlossen; Massnahmen bis zum Abschluss verfolgt*
- **Vorfallsreaktions-Testaufzeichnungen** (Tabletop-Übungen, Simulationen) — *jährlich; 3 Jahre aufbewahrt*
- **Kontaktliste für Vorfallsreaktion** (internes Team, Rechtsbeistand, vorab genehmigter forensischer Anbieter, EDÖB, Cyber-Versicherungsanbieter) — *vierteljährlich überprüft; bei jeder Änderung aktualisiert*
- **Kommunikationsvorlagen** (interne Benachrichtigung, externe Benachrichtigung, Benachrichtigung betroffener Personen, Pressemitteilung) — *vom Rechtsbeistand vorab genehmigt; jährlich überprüft*

### Vorfallsmetriken

Die folgenden Metriken sollten dem ISB und dem Management-Review-Team vierteljährlich gemeldet werden:

| Metrik | Beschreibung |
|--------|--------------|
| Gemeldete Ereignisse gesamt | Volumen der eingegangenen Sicherheitsereignisse |
| Ereignisse, die zu Vorfällen wurden | Anzahl und Prozentsatz der als Vorfälle klassifizierten Ereignisse |
| Vorfälle nach Schweregrad | Aufschlüsselung nach Kritisch / Hoch / Mittel / Niedrig |
| Mittlere Erkennungszeit (MTTD) | Durchschnittliche Zeit vom Ereignisauftreten bis zur Erkennung |
| Mittlere Reaktionszeit (MTTR) | Durchschnittliche Zeit von der Erkennung bis zur Eindämmung |
| Mittlere Lösungszeit | Durchschnittliche Zeit von der Erkennung bis zum Abschluss |
| Überfällige Vorfälle | Vorfälle, die die Ziel-Reaktionszeiträume überschreiten |
| Gemeldete Datenschutzverletzungen | Anzahl, die eine Meldung beim EDÖB oder der Aufsichtsbehörde erfordern |
| Abgeschlossene Post-Incident-Überprüfungen | Prozentsatz der kritischen/hohen Vorfälle mit abgeschlossenen Überprüfungen |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team sollte die Einhaltung dieser Richtlinie durch verschiedene Methoden verifizieren, einschliesslich, aber nicht beschränkt auf, Vorfallsreaktionsmetriken, Abschluss von Post-Incident-Überprüfungen, Testaufzeichnungen, interne und externe Audits sowie Feedback an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie sollte vom ISB im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen sollten dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterworfen werden, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollten Änderungen an Incident-Management-Standards, regulatorischen Meldeanforderungen, neuen Bedrohungen sowie Erkenntnisse aus Vorfällen und Übungen berücksichtigen.

---

# Bereiche des ISO-27001-Standards, die abgedeckt werden

Richtlinie zum Incident Management — ISO-27001-Kontrollmapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortlichkeiten |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Konformität mit Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | **5.24 Planung und Vorbereitung des Informationssicherheits-Incident-Managements** |
| Klausel 8.1 Operationale Planung und Kontrolle | **5.25 Bewertung und Entscheidung über Informationssicherheitsereignisse** |
| | **5.26 Reaktion auf Informationssicherheitsvorfälle** |
| | **5.27 Lernen aus Informationssicherheitsvorfällen** |
| | **5.28 Erhebung von Beweismitteln** |
| | 6.3 Informationssicherheitsbewusstsein, Ausbildung und Schulung |
| | 6.4 Disziplinarischer Prozess |
| | 6.8 Meldung von Informationssicherheitsereignissen |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizer nDSG (revDSG) | Art. 24 — Benachrichtigung bei Datenschutzverletzungen beim EDÖB («so schnell wie möglich») |
| Schweizer DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 33–34 — Verletzungsbenachrichtigung (72 Stunden an Behörde, unverzüglich an betroffene Personen) |
| ISO/IEC 27001:2022 | Annex A Kontrollen 5.24, 5.25, 5.26, 5.27, 5.28 |
| ISO/IEC 27002:2022 | Abschnitte 5.24–5.28 — Implementierungsleitfaden |
| ISO/IEC 27037:2012 | Leitlinien für Identifizierung, Erhebung, Beschaffung und Aufbewahrung digitaler Beweismittel |
| NIST SP 800-61 Rev 2 | Leitfaden zur Handhabung von Computer-Sicherheitsvorfällen (Vier-Phasen-Lebenszyklus) |
| CIS Controls v8 | Kontrolle 17 (Incident Response Management) |

---

<!-- QA_VERIFIED: 2026-03-29 -->

<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.11-12-DE:privacy:POL:a.3.11-12 -->
**PRIV-POL-A.3.11-12 — Datenschutz-Vorfallmanagement**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Datenschutz-Vorfallmanagement |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | PRIV-POL-A.3.11-12 |
| **Dokumentersteller** | Datenschutzbeauftragter (DSB) |
| **Dokumentverantwortlicher** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |
| **Privacy-Produktversion** | 1.0 |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | DSB | Erstrichtlinie für ISO/IEC 27701:2025 Erstzertifizierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen regulatorischen oder organisatorischen Änderungen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Datenschutzbeauftragter (DSB)
- Sekundär: Informationssicherheitsbeauftragter (ISB)
- Legal: Legal/Compliance Officer
- Letztentscheidung: Geschäftsleitung

**Zugehörige Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- PRIV-POL-01 (Datenschutz-Governance und Entscheidungsrahmen)
- PRIV-IMP-A.3.11-12-UG (Datenschutz-Vorfallmanagement — Benutzerhandbuch)
- PRIV-IMP-A.3.11-12-TG (Datenschutz-Vorfallmanagement — Technisches Handbuch)
- ISMS-POL-A.5.24-28 (Vorfallmanagement-Lebenszyklus — ISMS-Pendant)
- ISMS-POL-A.6.8 (Meldung von Informationssicherheitsereignissen — ISMS-Pendant)
- ISO/IEC 27701:2025 Kontrollen A.3.11, A.3.12
- ISO/IEC 27701:2025 Anhang B (Implementierungsleitfaden B.3.11, B.3.12)
- GDPR Art. 33 (Meldung an die Aufsichtsbehörde); Art. 34 (Benachrichtigung der betroffenen Personen)
- CH FADP Art. 24 (Meldung von Datensicherheitsverletzungen)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für die Planung, Vorbereitung und Reaktion auf Informationssicherheitsvorfälle im Zusammenhang mit der PII-Verarbeitung fest — gemäss ISO/IEC 27701:2025 Kontrollen A.3.11 und A.3.12.

**Anwendungsbereich**: Alle Informationssicherheitsvorfälle, die die Vertraulichkeit, Integrität oder Verfügbarkeit der von [Organisation] verarbeiteten PII betreffen, berühren oder berühren könnten; alle Mitarbeitenden mit Rollen bei der Erkennung, Eskalation, dem Management oder der Meldung von Datenschutzvorfällen.

**Zweck**: Festlegung organisatorischer Anforderungen für:

- Planung und Vorbereitung auf PII-bezogene Informationssicherheitsvorfälle (A.3.11)
- Reaktion auf Informationssicherheitsvorfälle im Zusammenhang mit der PII-Verarbeitung (A.3.12)

Diese Richtlinie legt fest, **WAS** für Datenschutz-Vorfallmanagementstrukturen und Meldepflichten gelten, **WER** die Verantwortung für Datenschutzvorfälle trägt und **WANN** wichtige Massnahmen und Meldungen erfolgen müssen. Implementierungsverfahren (**WIE**) sind in PRIV-IMP-A.3.11-12-UG und PRIV-IMP-A.3.11-12-TG dokumentiert.

**Rollenanwendbarkeit**: Diese Richtlinie gilt für [Organisation] in der Rolle als **PII-Verantwortlicher und PII-Auftragsverarbeiter**. Die Kontrollen A.3.11 und A.3.12 sind gemeinsame Kontrollen (Tabelle A.3) und gelten unabhängig von der Verarbeitungsrolle. Die Meldepflichten unterscheiden sich jedoch wesentlich zwischen Verantwortlichen- und Auftragsverarbeiterrolle und werden in dieser Richtlinie gesondert behandelt.

**Begründung für die zusammengefassten Kontrollen**: A.3.11 (Planung und Vorbereitung) und A.3.12 (Reaktion) sind die zwei Phasen derselben Fähigkeit. Eine wirksame Reaktion ist ohne vorherige Planung unmöglich; Planung ohne erprobte Reaktionsverfahren bleibt theoretisch. Sie werden gemeinsam als integriertes Datenschutz-Vorfallmanagementprogramm implementiert, das das ISMS-Vorfallmanagementrahmenwerk (ISMS-POL-A.5.24-28) für PII-Verarbeitungskontexte erweitert und spezialisiert.

---

# Anwendungsbereich und Gültigkeit

## ISO/IEC 27701:2025 Kontrollanforderungen

**Kontrolle A.3.11 — Planung und Vorbereitung des Informationssicherheits-Vorfallmanagements**
Kontrolle A.3.11 verlangt von [Organisation], sich auf Informationssicherheitsvorfälle mit Bezug zur PII-Verarbeitung vorzubereiten, indem die Vorfallmanagementprozesse, Rollen und Verantwortlichkeiten definiert, etabliert und kommuniziert werden, die die datenschutzspezifische Reaktion regeln.

**Kontrolle A.3.12 — Reaktion auf Informationssicherheitsvorfälle**
Kontrolle A.3.12 verlangt von [Organisation], auf Informationssicherheitsvorfälle im Zusammenhang mit der PII-Verarbeitung gemäss seinen dokumentierten Reaktionsverfahren zu reagieren.

## Was diese Richtlinie abdeckt

**Vorfallplanung und -vorbereitung**:

- Datenschutz-Vorfallmanagementprozesse, Rollen und Verantwortlichkeiten
- Struktur und Governance des Datenschutz-Incident-Response-Plans (PIRP)
- Eskalations- und Kommunikationspfade spezifisch für PII-Vorfälle
- Vorbereitungsaktivitäten: Tischübungen, Sensibilisierung, Reaktionswerkzeuge

**Vorfallreaktion**:

- Beurteilung, ob ein Informationssicherheitsvorfall eine Datenpanne darstellt
- Reaktionsverfahren bei Datenpannen, einschliesslich Eindämmung und Wiederherstellung
- Interne Melde- und Eskalationsketten für PII-Vorfälle
- Regulatorische Meldepflichten (Aufsichtsbehörden)
- Benachrichtigungspflichten für betroffene Personen
- Auftragsverarbeiter-Meldepflichten (wenn als Auftragsverarbeiter tätig oder Auftragsverarbeiter eingesetzt)
- Nachsorge spezifisch für PII-Vorfälle

**Umfang der PII-Vorfälle**:

Alle folgenden Ereignisse stellen PII-bezogene Vorfälle dar, die unter dieser Richtlinie zu verwalten sind:

- Nicht autorisierter Zugriff auf PII (bestätigt oder vermutet)
- Versehentliche Offenlegung von PII gegenüber nicht autorisierten Empfängern
- Verlust oder Diebstahl eines Geräts, Datenträgers oder Dokuments mit PII
- Ransomware, Malware oder Systemkompromittierung mit Auswirkungen auf PII-Verarbeitungssysteme
- Versehentliche Löschung oder Beschädigung von PII
- Rechtswidrige Verarbeitung von PII (Verarbeitung ohne Rechtsgrundlage, Verstoss gegen Zweckbindung)
- Lieferanten-/Auftragsverarbeitermeldung eines Vorfalls mit Auswirkungen auf die PII von [Organisation]

## Was diese Richtlinie NICHT abdeckt

- Allgemeines Informationssicherheits-Vorfallmanagement (siehe ISMS-POL-A.5.24-28)
- Forensische Beweissicherungsverfahren (siehe ISMS-POL-A.5.24-28)
- Meldung von Informationssicherheitsereignissen durch Mitarbeitende (siehe ISMS-POL-A.6.8)
- Geschäftskontinuität und Notfallwiederherstellung (siehe ISMS-POL-A.5.29-30)
- Reaktionsverfahren auf Betroffenenrechte für Zugangs- und Löschanfragen (siehe PRIV-POL-A.1.3.5-10)

## Regulatorischer Rahmen

**Tier 1: Obligatorische Compliance** (gemäss PRIV-POL-00):

- **EU GDPR**: Art. 33 (Meldung an die Aufsichtsbehörde innerhalb von 72 Stunden nach Bekanntwerden einer Datenpanne); Art. 34 (Benachrichtigung der betroffenen Personen bei hohem Risiko); Art. 5(1)(f) (Grundsatz der Integrität und Vertraulichkeit)
- **CH FADP**: Art. 24 (Meldung an den EDÖB bei Datensicherheitsverletzungen mit wahrscheinlichem hohem Risiko für die betroffenen Personen, unverzüglich)
- **ISO/IEC 27701:2025**: Kontrollen A.3.11, A.3.12 (normativ)

**Tier 2: Bedingte Anwendbarkeit** (gemäss PRIV-POL-00):

- **ISO/IEC 27018:2025**: Anhang A — Auftragsverarbeiter-Meldepflichten gegenüber Kunden (A.2.5.5), sofern Cloud-PII-Verarbeitung im Anwendungsbereich

**Tier 3: Informative Referenz** (gemäss PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementierungsleitfaden für Vorfallmanagement (5.24–5.28)
- **ISO/IEC 27701:2025 Anhang B**: B.3.11 (Vorfallplanung), B.3.12 (Vorfallreaktion)

Für eine vollständige regulatorische Kategorisierung siehe PRIV-POL-00.

---

# Richtlinienanforderungen: Planung und Vorbereitung von Datenschutzvorfällen (A.3.11)

## Datenschutz-Vorfallmanagementprogramm

[Organisation] **muss** die Verwaltung von Informationssicherheitsvorfällen im Zusammenhang mit der PII-Verarbeitung als definiertes, etabliertes und kommuniziertes Programm planen und vorbereiten. Dieses Programm erweitert das ISMS-Vorfallmanagementrahmenwerk (ISMS-POL-A.5.24-28) um PII-spezifische Prozesse, Rollen und Pflichten.

### Datenschutz-Incident-Response-Plan

[Organisation] **muss** einen Datenschutz-Incident-Response-Plan (PIRP) aufrechterhalten, der Folgendes definiert:

- Klassifikationskriterien und Schweregrad-Stufen für PII-Vorfälle
- Rollen und Verantwortlichkeiten für das Datenschutz-Vorfallmanagement (siehe Abschnitt Rollen und Verantwortlichkeiten)
- Eskalations- und Kommunikationsketten für jede Schweregrad-Stufe
- Entscheidungslogik für regulatorische Meldungen (ob, wann und an wen Meldungen erforderlich sind)
- Entscheidungskriterien und Verfahren für die Benachrichtigung betroffener Personen
- Auftragsverarbeiter-Meldepflichten (wenn [Organisation] als Auftragsverarbeiter tätig ist)
- Anforderungen an die Beweissicherung bei PII-Vorfällen
- Prozess für die Nachsorge und Lessons-Learned-Auswertung

Der PIRP ist ein kontrolliertes Dokument, das vom DSB gepflegt wird. Struktur- und Inhaltsanforderungen sind in PRIV-IMP-A.3.11-12-UG definiert.

### Schweregradklassifikation von Datenschutzvorfällen

PII-Vorfälle **müssen** nach Schweregrad klassifiziert werden, um Eskalation und Reaktionsdringlichkeit zu bestimmen:

| Schweregrad | Kriterien | Reaktionsdringlichkeit |
|-------------|----------|----------------------|
| **Kritisch** | Grossmassstäbliche Datenpanne; besondere Kategorien von PII betroffen; hohe Wahrscheinlichkeit erheblicher Schäden für betroffene Personen; systemische Kompromittierung von PII-Verarbeitungssystemen | Sofortig — Incident-Response-Team innerhalb von 2 Stunden aktiviert |
| **Hoch** | Bestätigte Datenpanne; regulatorische Meldung wahrscheinlich; bedeutsames Schadensrisiko für betroffene Personen; erhebliches Volumen an betroffener PII | Gleichtag — DSB innerhalb von 4 Stunden einbezogen |
| **Mittel** | Vermutete Datenpanne unter Untersuchung; begrenzte PII betroffen; Schadensrisiko gering, aber nicht vernachlässigbar; Eindämmung erreicht | 24-Stunden-Reaktion — DSB innerhalb von 24 Stunden einbezogen |
| **Niedrig** | Beinahevorfall oder potenzielles Ereignis; kein bestätigter PII-Zugriff; Verfahrensverstoss ohne tatsächliche Datenpanne | Standard — innerhalb von 5 Werktagen bewertet |

Die Schweregradklassifikation erfolgt durch den Datenschutz-Vorfallverantwortlichen und kann bei Entdeckung zusätzlicher Informationen während der Untersuchung eskaliert werden.

### Bereitschaftsanforderungen

[Organisation] **muss** die Bereitschaft für Datenschutzvorfälle durch folgende Massnahmen aufrechterhalten:

- **Rollen zugewiesen und kommuniziert**: Alle Datenschutz-Vorfallrollen (Datenschutz-Vorfallverantwortlicher, DSB, Legal/Compliance, ISB, Kommunikation) müssen definiert, dokumentiert sein, und die Mitarbeitenden müssen sich ihrer Verantwortlichkeiten bewusst sein
- **Schulung**: Mitarbeitende mit Datenschutz-Vorfallrollen müssen rollenspezifische Schulungen erhalten; alle Mitarbeitenden müssen allgemeine Sensibilisierung darüber erhalten, wie potenzielle PII-Vorfälle erkannt und gemeldet werden
- **Tests**: Der PIRP muss mindestens jährlich durch Tischübungen getestet werden; Testaufzeichnungen müssen geführt werden
- **Kontaktpflege**: Regulatorische Kontaktinformationen (CNIL/AEPD/EDPB/ICO-Kontaktangaben für GDPR; EDÖB für CH FADP) und Zugang zu Benachrichtigungsportalen der Aufsichtsbehörden müssen aktuell gehalten werden
- **Benachrichtigungsvorlagen**: Entwürfe für Benachrichtigungsvorlagen für Aufsichtsbehörden und betroffene Personen müssen vorbereitet, von Legal/DSB überprüft und für den schnellen Einsatz bereitgehalten werden

---

# Richtlinienanforderungen: Reaktion auf Datenschutzvorfälle (A.3.12)

## Reaktionsanforderungen

Reaktionen auf Informationssicherheitsvorfälle im Zusammenhang mit der PII-Verarbeitung **müssen** gemäss den dokumentierten Verfahren im PIRP und PRIV-IMP-A.3.11-12-UG durchgeführt werden. Für die Reaktion gelten folgende Anforderungen:

### Beurteilung einer Datenpanne

Wenn ein PII-bezogener Vorfall erkannt wird, **muss** [Organisation] unverzüglich beurteilen, ob der Vorfall eine **Datenpanne** darstellt — definiert als eine Sicherheitsverletzung, die zur zufälligen oder rechtswidrigen Vernichtung, zum Verlust, zur Änderung, zur unbefugten Offenlegung von oder zum unbefugten Zugang zu personenbezogenen Daten führt.

Die Beurteilung der Datenpanne **muss** folgende Aspekte berücksichtigen:

- Ob auf PII zugegriffen, diese offengelegt, verloren oder ohne Genehmigung vernichtet wurde oder werden könnte
- Die Kategorien und die ungefähre Menge der betroffenen PII
- Die wahrscheinlichen Folgen für betroffene Personen (Risiko finanzieller Schäden, Diskriminierung, Identitätsdiebstahl, Belastung oder andere erhebliche negative Auswirkungen)
- Ob die Datenpanne wahrscheinlich zu einem Risiko (oder hohen Risiko) für die Rechte und Freiheiten natürlicher Personen führt

Die Beurteilung und ihr Ergebnis **müssen** unabhängig von der Schlussfolgerung dokumentiert werden.

### Regulatorische Meldung: Als PII-Verantwortlicher

Wenn [Organisation] als PII-Verantwortlicher tätig ist und eine Datenpanne bestätigt oder vernünftigerweise vermutet wird:

**GDPR — Meldung an die Aufsichtsbehörde (Art. 33)**:

Die 72-Stunden-Meldefrist beginnt, wenn [Organisation] hinreichende Gewissheit hat, dass eine Datenpanne eingetreten ist — nicht zum Zeitpunkt des ersten Verdachts. Wenn die erste Untersuchung nicht schlüssig ist, beginnt die Frist, wenn ausreichende Fakten festgestellt sind, um zu bestätigen, dass eine Datenpanne eingetreten ist. Eine langwierige Untersuchung ohne vorläufige Feststellung ist nicht akzeptabel; wenn eine Datenpanne innerhalb von 24 Stunden nicht ausgeschlossen werden kann, muss der DSB eine vorläufige Meldung an die Aufsichtsbehörde vornehmen und diese mit weiteren Informationen ergänzen, sobald diese vorliegen.

- WENN die Datenpanne wahrscheinlich zu einem Risiko für die Rechte und Freiheiten natürlicher Personen führt: die zuständige Aufsichtsbehörde **ohne unangemessene Verzögerung und, sofern möglich, spätestens 72 Stunden** nach Bekanntwerden der Datenpanne benachrichtigen
- WENN die Meldung nach 72 Stunden erfolgt: eine begründete Rechtfertigung für die Verzögerung beifügen
- WENN die Datenpanne wahrscheinlich kein Risiko darstellt: Meldung an die Aufsichtsbehörde ist nicht erforderlich, die Datenpanne **muss** jedoch intern dokumentiert werden (Datenpannen-Register)
- Meldeinhalt: Art der Datenpanne; Kategorien und ungefähre Anzahl der betroffenen Personen; Kategorien und ungefähre Anzahl der betroffenen Datensätze; Name/Kontakt des DSB; wahrscheinliche Folgen; ergriffene oder vorgeschlagene Massnahmen zur Behebung

**CH FADP — Meldung an den EDÖB (Art. 24)**:

- WENN die Datenpanne wahrscheinlich zu einem hohen Risiko für die Persönlichkeit oder die Grundrechte der betroffenen Personen führt: den EDÖB **so rasch wie möglich** benachrichtigen
- Die Meldung an den EDÖB muss dem vom EDÖB festgelegten Format folgen

**GDPR — Benachrichtigung der betroffenen Personen (Art. 34)**:

- WENN die Datenpanne wahrscheinlich zu einem **hohen Risiko** für die Rechte und Freiheiten der betroffenen Personen führt: die betroffenen Personen **ohne unangemessene Verzögerung** benachrichtigen
- Benachrichtigungsinhalt: Art der Datenpanne (in verständlicher Sprache); Name/Kontakt des DSB; wahrscheinliche Folgen; ergriffene oder vorgeschlagene Massnahmen
- Benachrichtigung kann verzögert werden, wenn Strafverfolgungsgesichtspunkte dies erfordern (Koordination mit Legal erforderlich)

### Regulatorische Meldung: Als PII-Auftragsverarbeiter

Wenn [Organisation] als PII-Auftragsverarbeiter tätig ist und eine Datenpanne (oder potenzielle Datenpanne) mit Auswirkungen auf die PII eines Kunden festgestellt wird:

- Den PII-Verantwortlichen (Kunden) **ohne unangemessene Verzögerung** nach Bekanntwerden einer bestätigten oder vermuteten Datenpanne benachrichtigen — die Benachrichtigung ist nicht abhängig vom Abschluss der internen Untersuchung. Die Auftragsverarbeiterbenachrichtigung ermöglicht dem Verantwortlichen, seine eigene 72-Stunden-Meldefrist zu starten; [Organisation] darf die Auftragsverarbeiterbenachrichtigung nicht bis zur vollständigen Bestätigung verzögern. Maximale Benachrichtigungsfrist: 24 Stunden ab dem Zeitpunkt, an dem [Organisation] erkennt, dass eine Datenpanne eingetreten ist oder vernünftigerweise vermutet wird
- Die Benachrichtigung muss alle zum Zeitpunkt verfügbaren Informationen enthalten, mit ergänzenden Aktualisierungen im Verlauf der Untersuchung; Meldungen sind an den im Auftragsverarbeitungsvertrag festgelegten Sicherheits- oder Datenschutzkontakt des Kunden zu richten
- Alle verfügbaren Informationen bereitstellen, um dem Verantwortlichen die Erfüllung seiner Art. 33-Meldepflichten zu ermöglichen
- Die Aufsichtsbehörde oder betroffene Personen NICHT direkt benachrichtigen, es sei denn, der Verantwortliche hat dies ausdrücklich genehmigt oder [Organisation] ist unabhängig davon durch geltendes Recht dazu verpflichtet
- Vollumfänglich mit der Untersuchung des Verantwortlichen kooperieren

### Massnahmen bei der Vorfallreaktion

Die Datenschutz-Vorfallreaktion **muss** in folgender Prioritätsreihenfolge umfassen:

1. **Eindämmen**: Die laufende Datenpanne stoppen oder weiteren PII-Verlust verhindern
2. **Beurteilen**: Umfang, betroffene PII-Kategorien, Volumen und betroffene Personen bestimmen
3. **Sichern**: Beweise sichern (Protokolle, Aufzeichnungen, betroffene Systeme) — mit ISB gemäss ISMS-POL-A.5.24-28 koordinieren
4. **Melden**: Regulatorische und Benachrichtigungen der betroffenen Personen gemäss den oben genannten Schwellenwerten durchführen
5. **Wiederherstellen**: PII-Verarbeitung mit geeigneten Sicherheitsmassnahmen in den Normalbetrieb zurückführen
6. **Überprüfen**: Nachsorge durchführen; PIRP und Kontrollen bei Bedarf aktualisieren

### Datenpannen-Register

[Organisation] **muss** ein Datenpannen-Register führen, das alle Datenpannen aufzeichnet, unabhängig davon, ob eine regulatorische Meldung erforderlich war. Das Register **muss** enthalten:

- Vorfallreferenz und Entdeckungsdatum
- Art der Datenpanne und betroffene PII-Kategorien
- Ungefähre Anzahl der betroffenen Personen und Datensätze
- Ergebnis der Risikobewertung (Risiko / hohes Risiko / kein Risiko für betroffene Personen)
- Meldeentscheidungen (Aufsichtsbehörde, betroffene Personen) und Zeitpunkte
- Ergriffene Abhilfemassnahmen
- Verweis auf die Nachsorgeüberprüfung

Der DSB führt das Datenpannen-Register. Es ist ein vertrauliches Dokument und Nachweis der regulatorischen Compliance. Aufbewahrung: mindestens 5 Jahre.

---

# Rollen und Verantwortlichkeiten

## Datenschutz-Vorfallmanagementrollen

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Datenschutzbeauftragter (DSB)** | Datenschutz-Vorfallverantwortlicher — aktiviert PIRP; trifft regulatorische Meldeentscheidungen; kommuniziert mit Aufsichtsbehörden; genehmigt Benachrichtigungen der betroffenen Personen; führt Datenpannen-Register; leitet Nachsorgeüberprüfung |
| **ISB** | Technischer Vorfallverantwortlicher — koordiniert Eindämmung und Wiederherstellung; sichert forensische Beweise; leitet technische Untersuchung; Schnittstelle mit IT-Sicherheitsteam und externen Reaktionsteams |
| **Legal/Compliance Officer** | Rechtsberatung zu Meldepflichten, Rechten der betroffenen Personen und strafverfolgungsrechtlichen Erwägungen; überprüft Meldungen an Aufsichtsbehörden vor Einreichung; berät zu Auftragsverarbeiterpflichten |
| **Privacy Champions** | Erste Eskalationsstelle für Mitarbeitende, die PII-Vorfälle in ihrer Geschäftseinheit melden; erstmalige Triage und Eskalation an DSB |
| **IT-Sicherheitsteam** | Technische Untersuchung und Eindämmung; Protokollanalyse; Systemisolierung und -wiederherstellung; Beweissicherung gemäss ISMS-POL-A.5.24-28 |
| **Geschäftsleitung** | Wird über alle Hoch- und Kritisch-Vorfälle informiert; genehmigt Krisenkommunikation; unterstützt regulatorisches Engagement auf Führungsebene, wenn erforderlich |
| **Kommunikation** | Entwurf von Benachrichtigungen der betroffenen Personen (mit DSB-Genehmigung); Medien-/PR-Management bei grossmassstäblichen Datenpannen |
| **Alle Mitarbeitenden** | Vermutete PII-Vorfälle sofort ihrem Privacy Champion oder direkt dem DSB melden; Beweise sichern; mit der Untersuchung kooperieren |

---

# Nachweisanforderungen

Folgende Nachweise belegen den Betrieb dieser Richtlinie:

| Nachweis | Beschreibung | Aufbewahrung |
|---------|-------------|--------------|
| Datenschutz-Incident-Response-Plan (PIRP) | Aktuelle genehmigte Version mit Rollen, Prozessen und Meldeentscheidungslogik | Aktuell + 3 Jahre |
| Datenpannen-Register | Aufzeichnung aller Datenpannen und Beinahevorfälle mit Risikobewertung und Meldeentscheidungen | 5 Jahre |
| Meldungen an Aufsichtsbehörden | Kopien aller eingereichten Art. 33 / FADP Art. 24-Meldungen | 5 Jahre |
| Benachrichtigungen der betroffenen Personen | Kopien der Art. 34-Benachrichtigungen an betroffene Personen | 5 Jahre |
| PIRP-Testaufzeichnungen | Nachweis jährlicher Tischübungen einschliesslich Erkenntnisse und Verbesserungen | 3 Jahre |
| Aufzeichnungen zur Vorfallreaktionszeitlinie | Nachweis der Einhaltung der 72-Stunden-Meldefrist (oder dokumentierte Begründung für Verzögerung) | 5 Jahre |
| Nachsorgeüberprüfungsberichte | Lessons-Learned-Erkenntnisse und Verbesserungsmassnahmen für PIRP/Kontrollen | 3 Jahre |

---

# Prüfungshinweise

Prüfer, die die Compliance mit A.3.11 und A.3.12 verifizieren, sollten Folgendes vorfinden:

**Für A.3.11 (Planung und Vorbereitung)**:
- Ein dokumentierter Datenschutz-Incident-Response-Plan mit PII-spezifischen Prozessen und Rollen
- Nachweis, dass Rollen zugewiesen und Mitarbeitende sich ihrer Verantwortlichkeiten bewusst sind
- Jährliche PIRP-Testaufzeichnungen (Tischübung oder äquivalent)
- Gepflegte Kontaktinformationen der Aufsichtsbehörden und Zugang zu Benachrichtigungsportalen
- Vorbereitete, von Legal/DSB überprüfte Benachrichtigungsvorlagen

**Für A.3.12 (Reaktion)**:
- Datenpannen-Register mit allen aufgezeichneten Vorfällen einschliesslich Nicht-Melde-Feststellungen
- Bei gemeldeten Datenpannen: Meldungen an Aufsichtsbehörden innerhalb der 72-Stunden-Frist (oder dokumentierte Begründung für Verzögerung)
- Dokumentation der Datenpannenbeurteilung für alle Hoch/Kritisch-Vorfälle
- Nachsorgeüberprüfungsberichte mit bis zum Abschluss verfolgten Verbesserungsmassnahmen
- Nachweis, dass Auftragsverarbeiter-Meldepflichten erfüllt wurden (rechtzeitige Kundenbenachrichtigung bei Tätigkeit als Auftragsverarbeiter)

---

<!-- QA_VERIFIED: 2026-03-29 -->

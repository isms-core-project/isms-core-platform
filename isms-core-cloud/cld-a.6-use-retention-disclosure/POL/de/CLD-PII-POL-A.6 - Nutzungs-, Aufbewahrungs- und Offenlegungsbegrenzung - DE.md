<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.6-DE:cloud:POL:a.6 -->
**CLD-PII-POL-A.6 — Nutzungs-, Aufbewahrungs- und Offenlegungsbegrenzung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Nutzungs-, Aufbewahrungs- und Offenlegungsbegrenzung |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-PII-POL-A.6 |
| **Dokumentersteller** | Datenschutzbeauftragter (DSB) / ISB |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |
| **Cloud-Produktversion** | 1.0 |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | DSB / ISB | Erstversion für ISO/IEC 27018:2025 Ausg. 3 Implementierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen regulatorischen oder Dienstmodell-Änderungen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Datenschutzbeauftragter (DSB)
- Sekundär: ISB / Cloud Security Manager
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII)
- ISMS-POL-A.5.33 (Schutz von Aufzeichnungen)
- CLD-PII-POL-A.3 (Zwecklegitimität und -spezifikation)
- CLD-PII-POL-A.5 (Datenminimerung)
- CLD-PII-POL-A.10 (Rechenschaftspflicht — Verletzungsmeldung, Rückgabe/Entsorgung)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.6 und Kontrollen A.6.1–A.6.2
- ISO/IEC 27701:2025 Kontrollen A.2.5.4 (Aufzeichnungen über PII-Offenlegungen gegenüber Dritten), A.2.5.5 (Benachrichtigung über PII-Offenlegungsanfragen) und A.2.5.6 (rechtlich bindende PII-Offenlegungen)
- DSGVO Artikel 5 Abs. 1 lit. b und e (Zweckbindung, Speicherbegrenzung); Artikel 28 Abs. 3 lit. a (weisungsgebundene Verarbeitung); Artikel 28 Abs. 3 lit. f (Unterstützung bei regulatorischen Pflichten)
- CH DSG Artikel 6 Abs. 3 (Zweckbindung); Artikel 9 Abs. 2 lit. d (Unterstützungspflicht des Auftragsverarbeiters)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] als Public-Cloud-PII-Auftragsverarbeiter in Bezug auf Nutzungs-, Aufbewahrungs- und Offenlegungsbegrenzung fest — insbesondere die Pflicht, PII-Verantwortliche über gesetzlich erzwungene PII-Offenlegungen gegenüber Dritten zu informieren und Aufzeichnungen über alle solchen Offenlegungen zu führen — gemäss ISO/IEC 27018:2025 Annex A, Abschnitt A.6 und Kontrollen A.6.1 und A.6.2.

**Geltungsbereich**: Alle von [Organisation] im Auftrag von PII-Verantwortlichen aufbewahrten PII und alle Offenlegungen solcher PII gegenüber Dritten, einschliesslich Strafverfolgungsbehörden, Regulierungsbehörden und anderen Einrichtungen.

**Begründung für die kombinierten Kontrollen**: A.6.1 und A.6.2 befassen sich mit dem kritischen Szenario in der Public Cloud, in dem staatliche oder regulatorische Stellen den Auftragsverarbeiter zur Offenlegung von PII ohne Wissen des Verantwortlichen zwingen. Gemeinsam fordern sie Transparenz (den Verantwortlichen informieren) und Rechenschaft (alle Offenlegungen aufzeichnen), damit der Verantwortliche seinen eigenen regulatorischen Meldepflichten nachkommen kann.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 Kontrollaussagen

**Abschnitt A.6 — Nutzungs-, Aufbewahrungs- und Offenlegungsbegrenzung (Grundsatz)**

Abschnitt A.6 legt den Grundsatz fest, dass PII nur so lange aufbewahrt werden sollte, wie es für den festgelegten Zweck erforderlich ist, mit dokumentierten und durchgesetzten Aufbewahrungsfristen, und dass Offenlegungen gegenüber Dritten auf autorisierte Empfänger beschränkt und auf das erforderliche Minimum begrenzt werden sollten.

**Kontrolle A.6.1 — Benachrichtigung bei PII-Offenlegung**

Kontrolle A.6.1 verpflichtet den Auftragsverarbeiter, den PII-Verantwortlichen zu benachrichtigen, wenn er gesetzlich zur Offenlegung von PII gegenüber einem Dritten gezwungen wird — möglichst vor der Offenlegung oder zum frühestmöglichen Zeitpunkt, nachdem ein etwaiges gesetzliches Mitteilungsverbot erlischt.

**Kontrolle A.6.2 — Aufzeichnung von PII-Offenlegungen**

Kontrolle A.6.2 verpflichtet den Auftragsverarbeiter, Aufzeichnungen über alle PII-Offenlegungen gegenüber Dritten zu führen, einschliesslich Empfänger, Datum, PII-Kategorien, Rechtsgrundlage und ob der Verantwortliche benachrichtigt wurde, und diese Aufzeichnungen dem Verantwortlichen auf Anfrage zur Verfügung zu stellen.

## Was diese Richtlinie NICHT regelt

- Primäre Datenaufbewahrungsfristen für ruhende PII — diese werden durch die Weisungen des PII-Verantwortlichen festgelegt und in Dienstleistungsverträgen aufgenommen. Steht eine Aufbewahrungsanweisung im Widerspruch zu einem Legal Hold oder einer zwingenden Aufbewahrungsanordnung, bewahrt [Organisation] PII für den gesetzlich vorgeschriebenen Zeitraum auf und benachrichtigt den Verantwortlichen. Siehe CLD-PII-POL-A.10.3 für Rückgabe und Entsorgung nach Vertragsende.
- Rückgabe oder Entsorgung von PII bei Vertragsbeendigung — behandelt in CLD-PII-POL-A.10.3

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 5 Abs. 1 lit. b (Zweckbindung); Artikel 5 Abs. 1 lit. e (Speicherbegrenzung); Artikel 28 Abs. 3 lit. a (weisungsgebundene Verarbeitung); Artikel 28 Abs. 3 lit. f (Auftragsverarbeiter unterstützt den Verantwortlichen bei der Erfüllung der Pflichten gemäss Artikel 32–36)
- **CH DSG**: Artikel 6 Abs. 3 (Zweckbindung); Artikel 9 Abs. 2 lit. d (Unterstützungspflicht des Auftragsverarbeiters)
- **ISO/IEC 27018:2025**: Kontrollen A.6.1 und A.6.2

---

# Richtlinienaussagen: Aufbewahrungsbegrenzung (Grundsatz A.6)

## Einhaltung des Aufbewahrungsplans

[Organisation] darf PII im Auftrag der Verantwortlichen nur für die im Dienstleistungsvertrag festgelegte Dauer aufbewahren. Sofern im Dienstleistungsvertrag kein Aufbewahrungszeitraum angegeben ist, muss [Organisation] vor der Implementierung einer Aufbewahrungskonfiguration ausdrückliche schriftliche Weisungen des PII-Verantwortlichen einholen.

[Organisation] muss, wo technisch durchführbar, automatisierte Aufbewahrungsdurchsetzung (automatisierte Löschung oder Archivierung) implementieren. Die Abhängigkeit von manueller Löschung ist nur akzeptabel, wo eine automatisierte Durchsetzung technisch nicht möglich ist; in diesem Fall muss die manuelle Löschung dokumentiert und vierteljährlich überprüft werden.

---

# Richtlinienaussagen: Benachrichtigung bei PII-Offenlegung (A.6.1)

## Anforderung der vorherigen Benachrichtigung

Sofern [Organisation] eine rechtlich bindende Anfrage einer Strafverfolgungsbehörde, Regulierungsbehörde, eines Gerichts oder einer anderen staatlichen Stelle erhält, die die Offenlegung von PII eines PII-Verantwortlichen verlangt, muss [Organisation]:

1. Den betreffenden PII-Verantwortlichen **vor der Offenlegung** über die Offenlegungsanfrage informieren, einschliesslich:
   - Der Identität der anfragenden Behörde (soweit rechtlich zulässig)
   - Der Kategorien und des Umfangs der angeforderten PII
   - Der für die Anfrage angeführten Rechtsgrundlage
   - Der angeforderten Offenlegungsfrist

2. Dem PII-Verantwortlichen mindestens 5 Werktage einräumen, um rechtliche Rechtsmittel oder einstweiligen Rechtsschutz zu suchen, bevor die Offenlegung erfolgt, sofern die Offenlegungsfrist dies erlaubt. Wo die Frist keine 5 Werktage erlaubt, gewährt [Organisation] die maximal verfügbare Zeit

3. Die Offenlegung erst verarbeiten, nachdem:
   - Die Verantwortlichen-Benachrichtigung erfolgt und die Antwortfrist abgelaufen ist, oder
   - Die Offenlegungsfrist sofortiges Handeln erfordert; in diesem Fall muss der Verantwortliche gleichzeitig mit der Offenlegung benachrichtigt werden

## Gesetzlich verbotene Benachrichtigung

Sofern anwendbares Recht [Organisation] verbietet, den PII-Verantwortlichen über eine Offenlegungsanfrage zu informieren (z. B. eine gesetzlich auferlegte Schweigeverfügung), muss [Organisation]:

- Das gesetzliche Verbot und das Datum, ab dem die Benachrichtigung eingeschränkt ist, dokumentieren
- Den PII-Verantwortlichen zum **frühestmöglichen Zeitpunkt** nach Erlöschen des gesetzlichen Verbots benachrichtigen
- Sofern [Organisation] dauerhaft daran gehindert ist, den Verantwortlichen zu benachrichtigen (z. B. laufende nationale Sicherheitsanordnung), einen Transparenzbericht oder Warrant Canary im gesetzlich maximal zulässigen Umfang veröffentlichen. Der Warrant Canary muss mindestens vierteljährlich überprüft und aktualisiert werden, wobei der Rechts-/Compliance-Beauftragte für die Pflege seiner Genauigkeit verantwortlich ist

## Minimierende Offenlegung

Alle gesetzlich erzwungenen Offenlegungen müssen auf die zur Erfüllung der gesetzlichen Pflicht erforderlichen Mindest-PII beschränkt sein. [Organisation] darf keinen umfassenderen Zugang oder umfangreichere Datensätze bereitstellen, als von der rechtlichen Anordnung spezifisch verlangt. Der ISB muss bestätigen, dass [Organisation] vor jeder Offenlegung über die technische Möglichkeit verfügt, begrenzte PII-Extrakte zu erstellen, und diese Möglichkeit nutzen, um den Umfang der bereitgestellten Daten einzuschränken.

---

# Richtlinienaussagen: Aufzeichnung von PII-Offenlegungen (A.6.2)

## Offenlegungsregister

[Organisation] muss ein **PII-Offenlegungsregister** führen, das jede Offenlegung von PII gegenüber Dritten aufzeichnet, einschliesslich gesetzlich erzwungener Offenlegungen. Jeder Eintrag muss erfassen:

| Feld | Beschreibung |
|------|-------------|
| **Datum der Offenlegung** | Datum, an dem PII offengelegt oder übertragen wurde |
| **Empfänger** | Identität der empfangenden Partei (Behörde, Einrichtung oder Einzelperson) |
| **Kategorien der offengelegten PII** | Arten der übertragenen PII (z. B. Identitätsdaten, Kontaktdaten, Verarbeitungsprotokolle) |
| **Umfang** | Ungefähre Anzahl der betroffenen Personen |
| **Rechtsgrundlage** | Rechtliche Befugnis oder Verantwortlichen-Weisung, die die Offenlegung genehmigt |
| **Verantwortlicher benachrichtigt** | Ja / Nein — und falls Nein: Begründung und Datum der nachträglichen Benachrichtigung |
| **Genehmigt von** | Leitungskraft von [Organisation], die die Offenlegung genehmigt hat. Sofern eine vorherige Genehmigung aufgrund von Dringlichkeit nicht möglich war, muss die genehmigende Leitungskraft innerhalb von 24 Stunden nach der Offenlegung dokumentiert werden |

## Zugang und Aufbewahrung

Das PII-Offenlegungsregister muss:

- Vom DSB gepflegt und gegen unbefugte Änderung geschützt werden
- Jedem PII-Verantwortlichen auf Anfrage zur Verfügung gestellt werden (für Aufzeichnungen, die seine PII betreffen)
- Mindestens **5 Jahre** ab dem Datum jeder aufgezeichneten Offenlegung aufbewahrt werden — die 5-jährige Aufbewahrung entspricht dem standardmässigen vertraglichen Verjährungszeitraum in EU- und Schweizer Rechtsordnungen für Streitigkeiten aus Auftragsverarbeiter-Vereinbarungen und unterstützt rückwirkende regulatorische Prüfanforderungen
- Einer vierteljährlichen Überprüfung durch den DSB unterzogen werden

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Datenschutzbeauftragter (DSB)** | Verantwortlich für das PII-Offenlegungsregister; überprüft und genehmigt alle PII-Offenlegungen gegenüber Dritten; verwaltet den Verantwortlichen-Benachrichtigungsprozess; überwacht den Ablauf von Mitteilungsverboten |
| **Rechts-/Compliance-Beauftragter** | Prüft die rechtliche Gültigkeit von Offenlegungsanfragen; berät zu rechtlichen Rechtsmitteln; interpretiert Mitteilungsverbote; verwaltet Warrant-Canary-Aktualisierungen |
| **ISB / Cloud Security Manager** | Implementiert technische Aufbewahrungsdurchsetzung; stellt sicher, dass Offenlegungen technisch auf den minimal erforderlichen Umfang beschränkt sind |
| **Geschäftsleitung** | Genehmigt Offenlegungen in ambivalenten oder risikoreichen Szenarien; genehmigt Transparenzberichte |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| PII-Offenlegungsregister | Vollständiges Protokoll aller PII-Offenlegungen gegenüber Dritten mit Pflichtfeldern | 5 Jahre ab jedem Offenlegungsdatum |
| Aufbewahrungskonfigurations-Aufzeichnungen | Technische Dokumentation der automatisierten Aufbewahrungsdurchsetzung pro Dienst | Aktuell + 3 Jahre |
| Verantwortlichen-Benachrichtigungsaufzeichnungen | Aufzeichnungen aller an Verantwortliche gesendeten Benachrichtigungen zu erzwungenen Offenlegungen | 5 Jahre |
| Dokumentation gesetzlicher Verbote | Aufzeichnungen von Mitteilungsverboten und Daten nachträglicher Benachrichtigung | 5 Jahre |
| Transparenzberichte / Warrant Canary | Veröffentlichte Aussagen zum Nichtvorliegen nicht offengelegter rechtlicher Anordnungen | 5 Jahre |

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-PII-POL-A.6 verifizieren, sollten Folgendes vorfinden:

- Ein gepflegtes PII-Offenlegungsregister, das alle Drittoffenlegungen mit vollständigen Pflichtfeldern abdeckt
- Belege, dass PII-Verantwortliche über alle gesetzlich erzwungenen Offenlegungen benachrichtigt wurden (oder Dokumentation, warum eine Benachrichtigung gesetzlich verboten war)
- Automatisierte Aufbewahrungsdurchsetzungskonfigurationen, die mit den vertraglich vereinbarten Aufbewahrungsfristen übereinstimmen
- Rechts-/Compliance-Aufzeichnungen, die dokumentieren, wie gesetzlich erzwungene Offenlegungsanfragen geprüft und behandelt wurden

---

<!-- QA_VERIFIED: 2026-03-29 -->

<!-- ISMS-CORE:POLICY:CLD-POL-A.10-DE:cloud:POL:a.10 -->
**CLD-POL-A.10 — Rechenschaftspflicht**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Rechenschaftspflicht |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-POL-A.10 |
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
- ISMS-POL-A.5.24-28 (Vorfallmanagement-Lebenszyklus — übergeordnete Vorfallrichtlinie)
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII)
- ISMS-POL-A.5.33 (Schutz von Aufzeichnungen)
- CLD-POL-A.1 (Allgemein)
- CLD-POL-A.6 (Nutzungs-, Aufbewahrungs- und Offenlegungsbegrenzung)
- CLD-POL-A.11 (Informationssicherheit)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.10 und Kontrollen A.10.1–A.10.3
- ISO/IEC 27701:2025 Kontrollen A.3.11–A.3.12 (Vorfallmanagementplanung und -reaktion — Verletzungsmeldung); Abschnitt 7.5 (dokumentierte Informationen — Dokumentenaufbewahrung); A.2.4.3 (Rückgabe, Übertragung oder Entsorgung von PII)
- DSGVO Artikel 33 (Meldung an die Aufsichtsbehörde — 72 Stunden); Artikel 34 (Benachrichtigung der betroffenen Personen); Artikel 28 Abs. 3 lit. f (Auftragsverarbeiter unterstützt bei Verletzungsmeldungen); Artikel 28 Abs. 3 lit. g (Auftragsverarbeiter stellt Compliance-Informationen bereit)
- CH DSG Artikel 24 (Meldung von Datenschutzverletzungen an den EDÖB)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] als Public-Cloud-PII-Auftragsverarbeiter in Bezug auf Rechenschaftspflicht fest — insbesondere Verletzungsmeldung an PII-Verantwortliche, Aufbewahrung von administrativer Sicherheitsdokumentation und Verfahren zur Rückgabe, Übertragung und Entsorgung von PII bei Vertragsbeendigung — gemäss ISO/IEC 27018:2025 Annex A, Abschnitt A.10 und Kontrollen A.10.1, A.10.2 und A.10.3.

**Geltungsbereich**: Alle von [Organisation] im Auftrag von PII-Verantwortlichen durchgeführten PII-Verarbeitungen, einschliesslich Pflichten bei Vertragsende.

**Begründung für die kombinierten Kontrollen**: A.10.1–A.10.3 etablieren die drei Säulen der Auftragsverarbeiter-Rechenschaft: (1) den Verantwortlichen unverzüglich zu informieren, wenn Dinge schiefgehen (A.10.1), (2) Belege für Sicherheitszusagen so lange aufzubewahren, wie erforderlich (A.10.2), und (3) sicherzustellen, dass PII nicht in den Systemen von [Organisation] verbleiben, nachdem sie nicht mehr benötigt werden (A.10.3).

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 Kontrollaussagen

**Abschnitt A.10 — Rechenschaftspflicht (Grundsatz)**

Abschnitt A.10 legt den Grundsatz fest, dass ein Public-Cloud-PII-Auftragsverarbeiter gegenüber PII-Verantwortlichen Rechenschaft durch zeitnahe Verletzungsmeldung, Aufbewahrung von Compliance-Dokumentation und sichere Rückgabe oder Entsorgung von PII am Ende eines Dienstleistungsengagements wahren muss.

**Kontrolle A.10.1 — Meldung einer Datenschutzverletzung mit PII-Bezug**

Kontrolle A.10.1 verpflichtet den Auftragsverarbeiter, den PII-Verantwortlichen über bestätigte oder vermutete PII-Sicherheitsvorfälle ohne unangemessene Verzögerung und innerhalb einer Frist zu benachrichtigen, die dem Verantwortlichen die Erfüllung seiner eigenen regulatorischen Meldepflichten ermöglicht.

**Kontrolle A.10.2 — Aufbewahrungsdauer für administrative Sicherheitsrichtlinien und -leitlinien**

Kontrolle A.10.2 verpflichtet den Auftragsverarbeiter, administrative Sicherheitsrichtlinien und damit verbundene Dokumentation für einen ausreichenden Zeitraum aufzubewahren, um Compliance nachzuweisen und rückwirkende Prüfungen und Untersuchungen zu unterstützen.

**Kontrolle A.10.3 — PII-Rückgabe, -Übertragung und -Entsorgung**

Kontrolle A.10.3 verpflichtet den Auftragsverarbeiter, bei Vertragsbeendigung alle PII gemäss den Weisungen des Verantwortlichen zurückzugeben oder sicher zu vernichten und die Vollständigkeit schriftlich zu bestätigen.

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 28 Abs. 3 lit. f (Auftragsverarbeiter unterstützt Verantwortlichen bei Verletzungsmeldungen und Sicherheitspflichten); Artikel 33 (Verantwortlicher muss Aufsichtsbehörde innerhalb von 72 Stunden melden — Auftragsverarbeiter muss Verantwortlichen rechtzeitig informieren); Artikel 34 (Verantwortlicher informiert betroffene Personen bei schwerwiegenden Verletzungen); Artikel 28 Abs. 3 lit. g (Auftragsverarbeiter stellt alle zum Compliance-Nachweis erforderlichen Informationen bereit)
- **CH DSG**: Artikel 24 (Verletzungsmeldung an EDÖB — so rasch wie möglich); Artikel 9 (Rechenschaftspflichten des Auftragsverarbeiters)
- **ISO/IEC 27018:2025**: Kontrollen A.10.1, A.10.2, A.10.3

---

# Richtlinienaussagen: Verletzungsmeldung (A.10.1)

## Meldepflicht

[Organisation] muss den betreffenden PII-Verantwortlichen über jeden bestätigten oder hinreichend vermuteten PII-Sicherheitsvorfall **ohne unangemessene Verzögerung**, in jedem Fall jedoch innerhalb von **24 Stunden** nach Erkennung benachrichtigen. Ein hinreichender Verdacht entsteht, wenn erste Belege auf unbefugten Zugang zu einem System mit PII hinweisen, auch wenn der vollständige Umfang der Auswirkungen noch nicht bestimmt wurde. Diese Frist stellt sicher, dass der Verantwortliche ausreichend Zeit zur Erfüllung seiner eigenen 72-Stunden-DSGVO-Meldepflicht gegenüber der Aufsichtsbehörde hat.

## Meldeinhalt

Verletzungsmeldungen an PII-Verantwortliche müssen folgende Informationen enthalten, soweit diese zum Zeitpunkt der Meldung verfügbar sind:

| Element | Beschreibung |
|---------|-------------|
| **Art der Verletzung** | Typ des Vorfalls (unbefugter Zugang, versehentliche Offenlegung, Ransomware, Datenverlust usw.) |
| **PII-Kategorien** | Arten der betroffenen personenbezogenen Daten (Identität, Kontakt, Finanzen, Gesundheit usw.) |
| **Ungefähre Anzahl betroffener Personen** | Geschätzte Anzahl von Personen, deren PII möglicherweise betroffen sind |
| **Wahrscheinliche Folgen** | Voraussichtliche Auswirkungen auf betroffene Personen |
| **Ergriffene Massnahmen** | Implementierte oder vorgeschlagene Eindämmungs- und Remediierungsschritte |
| **Vorfallreferenz** | Interne Vorfallreferenznummer von [Organisation] |
| **Ansprechpartner** | DSB oder Sicherheitskontakt für Folgeabfragen des Verantwortlichen |

Sofern zum Zeitpunkt der ersten Meldung nicht alle Informationen vollständig vorliegen, muss [Organisation] die Informationen in phasenweisen Updates ohne weitere unangemessene Verzögerung und in jedem Fall in Abständen von maximal 24 Stunden bereitstellen, bis der Vorfall vollständig charakterisiert ist.

## Eskalation und Koordination

Das Verletzungsreaktionsverfahren von [Organisation] für PII-Vorfälle:

1. **Erkennung** — Sicherheitsbetrieb oder Cloud Engineering erkennt potenziellen PII-Vorfall
2. **Triage** (innerhalb von 2 Stunden) — ISB bestimmt, ob PII betroffen ist; aktiviert PII-Verletzungsreaktion bei Bestätigung oder Verdacht
3. **Erstmeldung** (innerhalb von 24 Stunden nach Erkennung) — DSB benachrichtigt betroffene PII-Verantwortliche mit verfügbaren Informationen
4. **Untersuchung** — Parallele Eindämmung und forensische Untersuchung; phasenweise Verantwortlichen-Updates bei Bekanntwerden von Fakten
5. **Abschluss** — Ursachenanalyse und Remediierung bestätigt; abschliessender Vorfallbericht an Verantwortlichen übergeben

---

# Richtlinienaussagen: Dokumentenaufbewahrung (A.10.2)

## Aufbewahrungsplan

[Organisation] muss folgende administrative Dokumentation für die definierten Mindestfristen aufbewahren:

| Dokumententyp | Mindestaufbewahrung |
|---------------|---------------------|
| CLD-POL-A.X Cloud-Sicherheitsrichtlinien (alle Versionen) | 5 Jahre ab Versionssupersession |
| Unterauftragsverarbeiter-Vereinbarungen und -Register | Dauer der Beauftragung + 5 Jahre |
| PII-Verarbeitungsaufzeichnungen (Verzeichnis der Verarbeitungstätigkeiten) | Verarbeitungsdauer + 5 Jahre |
| Verletzungsmeldungsaufzeichnungen und Vorfallberichte | 5 Jahre ab Vorfallabschluss |
| PII-Offenlegungsaufzeichnungen (CLD-POL-A.6.2-Register) | 5 Jahre ab Offenlegung |
| Bestätigungen zur Datenrückgabe/-entsorgung (A.10.3) | 5 Jahre ab Abschluss |
| Sicherheitsbeurteilungs- und Prüfberichte | 5 Jahre |
| Verantwortlichen-Dienstleistungsverträge | Vertragsdauer + 5 Jahre |

## Versionshistorie

Alle CLD-POL-A.X-Richtliniendokumente müssen eine Versionshistorie führen, die Dokumentversion, Datum, Autor und Zusammenfassung der Änderungen erfasst. Vorgängerversionen müssen gemäss dem obigen Aufbewahrungsplan aufbewahrt werden.

---

# Richtlinienaussagen: PII-Rückgabe, -Übertragung und -Entsorgung (A.10.3)

## Pflicht bei Vertragsende

Bei Beendigung oder Ablauf eines Cloud-Dienstleistungsvertrags, unter dem [Organisation] PII verarbeitet, muss [Organisation] gemäss den Weisungen des PII-Verantwortlichen:

**Option A — Rückgabe**: Alle PII in strukturiertem, maschinenlesbarem Format (JSON, CSV oder standardmässiger Datenbankexport wie vereinbart) an den PII-Verantwortlichen zurückgeben, innerhalb der im Dienstleistungsvertrag festgelegten Frist oder, falls keine solche Festlegung besteht, innerhalb von **30 Kalendertagen** nach Beendigung.

**Option B — Entsorgung**: Alle PII (einschliesslich primärer Speicher, Backups, replizierter Kopien und etwaiger Unterauftragsverarbeiter-Kopien) mit Methoden, die eine Wiederherstellung verhindern, sicher vernichten, innerhalb von **30 Kalendertagen** nach Beendigung. [Organisation] muss dem PII-Verantwortlichen ein **schriftliches Vernichtungszertifikat** (siehe Abschnitt Vernichtungszertifikat unten) zur Bestätigung des Abschlusses ausstellen.

Sofern das Volumen oder die Komplexität der gehaltenen PII einen Abschluss innerhalb von 30 Kalendertagen undurchführbar macht, kann [Organisation] mit dem PII-Verantwortlichen eine verlängerte Frist **schriftlich vor Ablauf der 30-Tage-Frist** vereinbaren. Jede vereinbarte Verlängerung muss ein überarbeitetes Abschlussdatum und Zwischenmeilenstein-Bestätigungen spezifizieren.

## Backup- und Replizierte Kopien

Sofern zum Zeitpunkt der Vertragsbeendigung PII in Backup- oder replizierten Kopien vorhanden sind, muss [Organisation]:

- Backup-Kopien in den Rückgabe- oder Entsorgungsprozess innerhalb desselben 30-Tage-Fensters (oder vereinbarter verlängerter Frist) einbeziehen
- Im Dienstleistungsvertrag den maximalen Zeitrahmen für die Backup-Entsorgung definieren (unter Berücksichtigung von Backup-Rotationszyklen)
- Den Abschluss der Backup-Entsorgung schriftlich bestätigen

## Entsorgung durch Unterauftragsverarbeiter

Sofern [Organisation] Unterauftragsverarbeiter beauftragt, die PII halten, muss [Organisation]:

- Unterauftragsverarbeiter anweisen, PII innerhalb desselben 30-Tage-Fensters (oder vereinbarter verlängerter Frist) zurückzugeben oder zu vernichten
- Von jedem Unterauftragsverarbeiter ein schriftliches Vernichtungszertifikat einholen und es als Teil des eigenen Bestätigungsnachweises von [Organisation] an den PII-Verantwortlichen weiterleiten
- [Organisation] bleibt gegenüber dem PII-Verantwortlichen für die Entsorgung durch Unterauftragsverarbeiter verantwortlich — die Unterauftragsverarbeiter-Zertifikate sind unterstützende Belege, keine Entbindung von der Pflicht von [Organisation]

## Vernichtungszertifikat

Sofern PII-Entsorgung gewählt wird (Option B), muss das dem PII-Verantwortlichen ausgestellte schriftliche Vernichtungszertifikat mindestens enthalten:

| Feld | Beschreibung |
|------|-------------|
| **Abschlussdatum** | Datum, an dem die Entsorgung abgeschlossen wurde |
| **Umfang** | Kategorien der vernichteten PII und ungefähres Volumen (Anzahl der Datensätze oder betroffenen Personen) |
| **Abgedeckte Systeme** | Primärspeicher, Backup-Medien, replizierte Datenspeicher und alle anderen als bereinigt bestätigten Systeme |
| **Entsorgungsmethode** | Eingesetzte technische Methode (z. B. kryptografische Löschung, sichere Überschreibung gemäss NIST SP 800-88, physische Vernichtung) |
| **Unterauftragsverarbeiter-Bestätigung** | Bestätigung, dass Kopien bei Unterauftragsverarbeitern ebenfalls vernichtet wurden (mit Unterauftragsverarbeiter-Zertifikaten als Anlage oder Referenz) |
| **Zertifizierender Leitender** | Name und Funktion der zertifizierenden Leitungskraft von [Organisation] |

## Bestätigungsnachweis

[Organisation] muss dem PII-Verantwortlichen eine schriftliche Bestätigung der abgeschlossenen Rückgabe oder Entsorgung bereitstellen, einschliesslich:

- Datum der Rückgabelieferung oder des Entsorgungsabschlusses
- Umfang der zurückgegebenen oder entsorgten PII (Kategorien, ungefähres Volumen)
- Entsorgungsmethode (sofern Entsorgung gewählt wurde)
- Bestätigung, dass PII bei Unterauftragsverarbeitern ebenfalls zurückgegeben oder entsorgt wurden

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Datenschutzbeauftragter (DSB)** | Verantwortlich für den Verletzungsmeldungsprozess; stellt sicher, dass Verantwortlichen-Benachrichtigungen innerhalb von 24 Stunden erfolgen; verwaltet den Dokumentenaufbewahrungsplan; beaufsichtigt den PII-Rückgabe-/-entsorgungsprozess bei Vertragsende |
| **ISB / Cloud Security Manager** | Leitet die technische Verletzungsreaktion (Eindämmung, Untersuchung); bestätigt den PII-Umfang von Vorfällen; implementiert sichere Entsorgung für Pflichten bei Vertragsende |
| **Rechts-/Compliance-Beauftragter** | Berät zu Meldepflichten gemäss DSGVO und DSG; überprüft Vertragsklauseln zur Rückgabe/Entsorgung; pflegt die Einhaltung des Aufbewahrungsplans |
| **Cloud Engineering** | Implementiert sichere Entsorgungsmechanismen; erstellt Datenexporte für Rückgaben; bestätigt den Abschluss der Backup-Bereinigung |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| Verletzungsmeldungsaufzeichnungen | Alle an PII-Verantwortliche gesendeten Benachrichtigungen mit Zeitstempeln und Inhalt | 5 Jahre ab Vorfallabschluss |
| Vorfallberichte | Abschliessende Post-Incident-Berichte für alle PII-Sicherheitsereignisse | 5 Jahre ab Vorfallabschluss |
| Dokumentenversionsarchiv | Alle Vorgängerversionen der CLD-POL-A.X-Richtlinien | 5 Jahre ab Versionssupersession |
| Vertragsende-Bestätigungen | Schriftliche Bestätigungen der PII-Rückgabe oder -Entsorgung pro Vertrag | 5 Jahre ab Abschluss |
| Vernichtungszertifikate | Zertifikate, die sichere Entsorgung mit Methode und Umfang bestätigen | 5 Jahre ab Abschluss |
| Backup-Entsorgungsbestätigungen | Schriftliche Bestätigung, dass Backup-Kopien von PII bereinigt wurden | 5 Jahre ab Abschluss |

5-jährige Aufbewahrungsfristen entsprechen dem standardmässigen vertraglichen Verjährungszeitraum in EU- und Schweizer Rechtsordnungen für Streitigkeiten aus Auftragsverarbeiter-Vereinbarungen und unterstützen rückwirkende regulatorische Prüfanforderungen.

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-POL-A.10 verifizieren, sollten Folgendes vorfinden:

- Ein dokumentiertes Verletzungsmeldungsverfahren mit 24-Stunden-Verantwortlichen-Meldeanforderung
- Aufzeichnungen aller PII-Sicherheitsvorfälle einschliesslich Meldezeitstempeln — Meldungen sollten dem Ablauf der 72-Stunden-DSGVO-Frist jedes Verantwortlichen vorausgehen
- Versionshistorie für alle CLD-POL-A.X-Richtliniendokumente mit plankonformer Aufbewahrung
- Vertragsende-Rückgabe- oder -Entsorgungsbestätigungen und Vernichtungszertifikate für alle im Prüfungszeitraum beendeten Verträge

---

<!-- QA_VERIFIED: 2026-03-29 -->

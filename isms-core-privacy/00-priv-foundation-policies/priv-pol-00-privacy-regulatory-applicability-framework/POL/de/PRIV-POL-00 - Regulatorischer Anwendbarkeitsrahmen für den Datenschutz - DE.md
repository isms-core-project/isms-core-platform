<!-- ISMS-CORE:POLICY:PRIV-POL-00-DE:privacy:POL:00 -->
**PRIV-POL-00 — Regulatorischer Anwendbarkeitsrahmen für den Datenschutz**
**Massgebliche Referenz für PIMS-Compliance-Pflichten**

---

## Dokumentenkontrolle

| Feld | Wert |
|------|------|
| **Dokumententitel** | Regulatorischer Anwendbarkeitsrahmen für den Datenschutz |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | PRIV-POL-00 |
| **Dokumentenersteller** | Datenschutzbeauftragter (DSB) |
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
| 0.1 | [Date - 8 weeks] | DSB | Ersterstellung — Drei-Stufen-Rahmenstruktur, GDPR + FADP-Geltungsbereich |
| 0.2 | [Date - 6 weeks] | DSB + Legal | ISO 27701:2025 und ISO 27018:2025 Stufen hinzugefügt; internationale Geltungsbereichsbedingungen |
| 0.3 | [Date - 4 weeks] | ISB | Abstimmung mit ISMS-POL-00-Methodik; Cloud- und Cloud-Sicherheitsreferenzen ergänzt |
| 0.4 | [Date - 2 weeks] | DSB/Legal/ISB | Stakeholder-Feedback eingearbeitet; ISO 27017 Hinweis auf bevorstehende Ausgabe ergänzt |
| 1.0 | [Date] | DSB/Legal/ISB | Erstgenehmigung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen regulatorischen Änderungen, neuen Standardveröffentlichungen oder Änderungen des Zertifizierungsumfangs)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Datenschutzbeauftragter (DSB)
- Sekundär: Informationssicherheitsbeauftragter (ISB)
- Compliance: Legal/Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- PRIV-POL-01 — Datenschutz-Governance und Entscheidungsrahmen
- ISMS-POL-00 — Regulatorischer Anwendbarkeitsrahmen (ISMS-Basis — obligatorische Querverweisnahme)
- ISO/IEC 27701:2025 Klausel 5.2 (Verstehen der Bedürfnisse und Erwartungen interessierter Parteien)
- ISO/IEC 27701:2025 Klausel 5.3 (Bestimmung des Geltungsbereichs des PIMS)
- Alle PIMS-Richtliniendokumente (obligatorische Referenz)

**Verteilung**: Alle PIMS-Stakeholder, Datenschutzbeauftragte, Richtlinienautoren, Systemeigentümer, Auditoren, Auftragsverarbeiter
**Referenziert durch**: Alle PIMS-Richtliniendokumente (PRIV-POL-01, alle PRIV-POL-A.x.x-Kontrollgruppen-POLs)

**Sprachstrategie**: Technische oder regulatorische Begriffe, die international etabliert sind (z.B. GDPR, ISO/IEC, FADP, PII), werden in englischer Sprache beibehalten, um Präzision zu wahren und grenzüberschreitende regulatorische Referenzen zu erleichtern.

---

## Zusammenfassung für die Geschäftsleitung

Dieses Dokument stellt die **massgebliche Referenz** für die Interpretation der regulatorischen Anwendbarkeit von Datenschutzvorschriften und -rahmen für das gesamte Privacy Information Management System (PIMS) dar.

**Zweck**: Beseitigung von Unklarheiten und Inkonsistenzen bei der Referenzierung von Datenschutzgesetzen, -verordnungen und -standards in PIMS-Richtlinien, Verfahren und Kontrollen.

**Geltungsbereich**: Alle Verweise auf Datenschutzgesetze, Datenschutzverordnungen und Datenschutzrahmen in der PIMS-Dokumentation.

**Verhältnis zum ISMS**: Diese Richtlinie ist ein datenschutzspezifischer Begleiter zu **ISMS-POL-00** (Regulatorischer Anwendbarkeitsrahmen). ISMS-POL-00 regelt Informationssicherheitspflichten. PRIV-POL-00 regelt Datenschutzpflichten. Bei überlappenden Pflichten (z.B. GDPR Artikel 32 — Sicherheit der Verarbeitung) hat ISMS-POL-00 Vorrang für die Informationssicherheitsdimension; PRIV-POL-00 regelt die Datenschutzdimension.

**Grundprinzip**: **Regulatorische Datenschutzanwendbarkeit muss explizit festgestellt werden, nicht angenommen werden.** Verweise auf Datenschutzvorschriften und -rahmen fallen in drei Kategorien:

1. **Obligatorische Compliance** — Rechtspflichten, die für die Organisation gelten
2. **Bedingte Anwendbarkeit** — Anforderungen, die nur unter bestimmten Umständen gelten
3. **Informativer Verweis** — Bewährte Verfahren und technische Leitfäden

**Verwendung**: Alle PIMS-Kontrollgruppen-Richtlinien SOLLEN einen Abschnitt «Regulatorischer Rahmen» enthalten, der dieses Dokument referenziert und angibt, welcher Stufe jede zitierte Verordnung/jeder zitierte Standard angehört.

**Schlüsselbegriffe**: Definitionen für in dieser Richtlinie verwendete Begriffe (Obligatorisch, Bedingt, Stufe 1/2/3, Anwendbarkeitsauslöser, PII, PII Principal, Verantwortlicher, Auftragsverarbeiter) sind im **Glossar** am Ende dieses Dokuments aufgeführt.

---

## Richtlinienautorität und Grenzen

### Zweck und Geltungsbereich dieser Richtlinie

Diese Richtlinie definiert die **Identifikation und Anwendbarkeit** von gesetzlichen, behördlichen, regulatorischen und vertraglichen Anforderungen für das Privacy Information Management System der Organisation.

**Diese Richtlinie legt fest:**

- Welche Datenschutzgesetze und -standards für die Organisation gelten
- Kategorisierung von Datenschutzpflichten (Obligatorisch, Bedingt, Informativ)
- Bewertungsmethodik zur Bestimmung der Anwendbarkeit
- Überprüfungs- und Aktualisierungsprozesse bei Änderungen im regulatorischen Datenschutzumfeld

**Diese Richtlinie legt NICHT fest:**

- Datenschutz-Risikobehandlungsentscheidungen (behandelt im PIMS-Risikomanagement)
- Anforderungen an die Kontrollumsetzung (behandelt in Kontrollgruppen-POLs und IMPs)
- Compliance-Status oder -Verifizierung (behandelt in Compliance-Monitoring-Prozessen)
- Informationssicherheitspflichten (behandelt in ISMS-POL-00)

Das Ergebnis der Datenschutz-Regulatorischen-Anwendbarkeitsbewertung dient als **Eingabe** für:

- Umfangsentscheidungen für alle PIMS-Kontrollgruppen
- Datenschutzrisikobewertung und -behandlungspriorisierung
- Verhältnismässigkeitsentscheidungen für die Kontrollumsetzung (Verantwortlicher vs. Auftragsverarbeiter-Pflichten)
- Auditplanung und Compliance-Verifizierung

**Grenzprinzip**: Diese Richtlinie legt die regulatorische Datenschutzanwendbarkeit fest. Umsetzung, Durchsetzung und Verifizierung werden durch separate PIMS-Prozesse und Kontrollgruppen-Richtlinien gehandhabt.

**Integration mit ISO 27701:2025:**

- **Klausel 5.2 (Interessierte Parteien)**: Regulatorische Datenschutzanforderungen stellen die primären Pflichten der interessierten Parteien dar. Diese Richtlinie identifiziert sie explizit.
- **Klausel 5.3 (Geltungsbereich)**: Die Geltungsbereichsbestimmung wird davon beeinflusst, welche Stufe-1-Vorschriften gelten und ob die Organisation als Verantwortlicher, Auftragsverarbeiter oder beides handelt.
- **Klausel 6 (Risikobewertung)**: Regulatorische Pflichten fliessen in das PIMS-Risikoregister ein. Stufe 1 = Hohe Priorität, Bedingte Stufe 2 = Mittlere Priorität, Stufe 3 = Informativer Beitrag.

**Integration mit ISMS-POL-00:**

Diese Richtlinie operiert neben und unterhalb von ISMS-POL-00 in allen Informationssicherheitsangelegenheiten. Wo eine Verordnung sowohl Datenschutz- als auch Sicherheitsdimensionen hat (z.B. GDPR Artikel 32, CH-nDSG Artikel 7), werden die Pflichten gemeinsam behandelt. PRIV-POL-00 regelt die Datenschutzinterpretation; ISMS-POL-00 regelt die Sicherheitsinterpretation.

---

**Kategorien der regulatorischen Anwendbarkeit**

**Obligatorische Compliance**
Rechtliche oder vertragliche Datenschutzpflichten, die die Organisation EINHALTEN MUSS. Nichteinhaltung führt zu rechtlicher Haftung, behördlichen Bussen, Untersuchungen durch Aufsichtsbehörden oder Zertifizierungsverlust.

**Merkmale**:

- Durch Datenschutzbehörde (DPA) oder Gericht durchsetzbar
- Nichteinhaltung hat rechtliche/finanzielle Konsequenzen (Bussen, Durchsetzungsverfügungen)
- Erfordert dokumentierten Compliance-Nachweis (Verarbeitungsverzeichnisse, DPIAs, Einwilligungsnachweise)
- Unterliegt behördlichen Audits, Inspektionen und Aufsichtsbehördenbefugnissen

**Bedingte Anwendbarkeit**
Datenschutzanforderungen, die nur gelten, wenn bestimmte Bedingungen erfüllt sind (z.B. bestimmte verarbeitete Datenkategorien, geografischer Geltungsbereich, gesuchte Zertifizierung, Kundenverträge, Cloud-Servicemodell).

**Merkmale**:

- Anwendbarkeit hängt von Verarbeitungsaktivitäten, Datentypen oder geografischem Geltungsbereich ab
- Kann basierend auf Geschäftstätigkeiten oder vertraglichen Anforderungen obligatorisch werden
- Erfordert regelmässige Neubewertung bei Änderungen von Geschäfts- und Verarbeitungsaktivitäten

**Informativer Verweis / Ausrichtung an bewährten Verfahren**
Rahmen und Standards, die für technische und organisatorische Leitlinien, Benchmarking oder freiwillige Ausrichtung verwendet werden. Diese informieren Datenschutzpraktiken, stellen aber keine obligatorischen Compliance-Anforderungen dar.

**Merkmale**:

- Freiwillige Übernahme für bewährte Verfahren
- Kein direkter Rechtsdurchsetzungsmechanismus
- Wird für die Umsetzung technischer und organisatorischer Massnahmen (TOM) verwendet
- Kann obligatorisch werden, wenn in Verträgen oder Zertifizierungsanforderungen referenziert

---

## Compliance-Hierarchie

```
┌─────────────────────────────────────────────────────────────────┐
│              DATENSCHUTZ-COMPLIANCE-HIERARCHIE                  │
├─────────────────────────────────────────────────────────────────┤
│  STUFE 1: OBLIGATORISCH (Rechtlich/Vertraglich)                  │
│  • EU GDPR (bei Verarbeitung personenbezogener EU-Daten)        │
│  • Schweizerisches Datenschutzgesetz (FADP/nDSG)               │
│                                                                 │
│  STUFE 2: BEDINGT (Kontextabhängig)                             │
│  • ISO/IEC 27701:2025 (bei gesuchter oder vertraglich          │
│    geforderter Zertifizierung)                                  │
│  • ISO/IEC 27018:2025 (Cloud-PII-Auftragsverarbeiter)          │
│  • UK GDPR (bei Verarbeitung personenbezogener UK-Daten         │
│    nach Brexit)                                                 │
│  • LGPD (bei Verarbeitung personenbezogener                    │
│    Daten aus Brasilien)                                         │
│  • PIPL (bei Verarbeitung personenbezogener                    │
│    Daten aus China)                                             │
│  • Andere Ländergesetze (auslöserbasierte Bewertung)           │
│                                                                 │
│  STUFE 3: INFORMATIV (Bewährte Verfahren / Technische Leitlinien│
│  • ISO/IEC 27017:2019 (Cloud-Sicherheits-Basis für 27018)      │
│  • ISO/IEC 27002:2022 (Sicherheitskontroll-Umsetzung)         │
│  • NIST Privacy Framework 2.0 (Datenschutzrisikomanagement)   │
│                                                                 │
│  BEVORSTEHEND (Beobachten — Bei Veröffentlichung übernehmen)   │
│  • ISO/IEC 27017:2025 (Cloud-Sicherheit — noch nicht          │
│    veröffentlicht)                                              │
└─────────────────────────────────────────────────────────────────┘
```

> *Sollten die Rahmenzeichen nicht korrekt dargestellt werden, sind die Stufendefinitionen in den folgenden Abschnitten massgeblich.*

---

# Obligatorische Compliance (Stufe 1)

> **Hinweis zur ISO/IEC 27701:2025-Klassifikation**: ISO/IEC 27701:2025 ist in diesem Rahmen als **Stufe 2 (Bedingt)** klassifiziert. Es handelt sich nicht um eine rechtlich durchsetzbare Verordnung. Es wird für [Organisation] obligatorisch, wenn eine Zertifizierung aktiv angestrebt wird oder ein Kundenvertrag explizit PIMS-Compliance fordert. Wenn keine dieser Bedingungen zutrifft, fungiert es als freiwilliger Best-Practice-Rahmen. Siehe den Abschnitt ISO/IEC 27701:2025 unter Stufe 2 für vollständige Details.

## EU-Datenschutz-Grundverordnung (DSGVO / GDPR)

**Anwendbarkeit**: Bei der Verarbeitung personenbezogener Daten von Personen in der EU/EWR, unabhängig davon, wo die Organisation ansässig ist.

**Wesentliche Anforderungen**:

- Artikel 5: Grundsätze der Verarbeitung (Rechtmässigkeit, Treu und Glauben, Transparenz, Zweckbindung, Datensparsamkeit, Richtigkeit, Speicherbegrenzung, Integrität und Vertraulichkeit, Rechenschaftspflicht)
- Artikel 6: Rechtmässigkeit der Verarbeitung
- Artikel 7–9: Einwilligungsanforderungen und besondere Kategorien von Daten
- Artikel 13–14: Informationspflichten gegenüber PII Principals (Datenschutzhinweise)
- Artikel 15–22: Betroffenenrechte (Auskunft, Berichtigung, Löschung, Einschränkung, Übertragbarkeit, Widerspruch, automatisierte Entscheidungsfindung)
- Artikel 24: Verantwortlichkeit des Verantwortlichen (Rechenschaftspflicht, Richtlinien, Massnahmen)
- Artikel 25: Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen
- Artikel 28: Pflichten des Auftragsverarbeiters (schriftlicher Vertrag, Sicherheitsmassnahmen, Sub-Auftragsverarbeiter-Kontrollen)
- Artikel 30: Verzeichnis der Verarbeitungstätigkeiten (ROPA)
- Artikel 32: Sicherheit der Verarbeitung (Verschlüsselung, Pseudonymisierung, Belastbarkeit, Tests)
- Artikel 33–34: Meldung von Verletzungen (72 Stunden an DPA; unverzüglich an betroffene Personen bei hohem Risiko)
- Artikel 35–36: Datenschutz-Folgenabschätzung (DPIA) für Hochrisikoverarbeitungen; vorherige Konsultation der DPA bei verbleibendem hohem Risiko
- Artikel 37–39: Pflichten des Datenschutzbeauftragten, soweit anwendbar
- Artikel 44–49: Einschränkungen bei internationalen Datentransfers

**PIMS-Auswirkungen**:

- Privacy by Design und by Default in allen Verarbeitungsaktivitäten
- Verarbeitungsverzeichnisse (ROPA) durch Verantwortlichen und Auftragsverarbeiter geführt
- Rechtmässige Grundlage für jede Verarbeitungsaktivität dokumentiert
- Betroffenenrechte-Verfahren implementiert und getestet
- Auftragsverarbeitungsverträge gemäss Artikel 28 vorhanden
- DPIA-Prozess für Hochrisikoverarbeitungen
- Meldeverfahren bei Verletzungen mit 72-Stunden-Frist
- Sicherheitsmassnahmen für internationale Transfers (Angemessenheitsbeschlüsse, Standardvertragsklauseln, BCRs)

**Aufsichtsbehörde**: Zuständige EU/EWR-Datenschutzbehörde (DPA) der Hauptniederlassung oder des Landes der betroffenen Person.

**Referenz**: Verordnung (EU) 2016/679, in Kraft seit 25. Mai 2018

---

## Schweizerisches Datenschutzgesetz (DSG / nDSG / FADP)

**Anwendbarkeit**: Alle Verarbeitungen personenbezogener Daten durch die Organisation, die der schweizerischen Zuständigkeit unterliegen; sowie jede Verarbeitung personenbezogener Daten von in der Schweiz wohnhaften Personen aus dem Ausland, wenn die Auswirkungen in der Schweiz eintreten.

**Wesentliche Anforderungen**:

- Artikel 6: Grundsätze (Rechtmässigkeit, Treu und Glauben, Verhältnismässigkeit, Zweckbindung)
- Artikel 7: Datensicherheit (technische und organisatorische Massnahmen entsprechend dem Risiko)
- Artikel 8: Datenverarbeitung durch Auftragsverarbeiter (schriftliche Vereinbarung, Sicherheit, Sub-Auftragsverarbeiter)
- Artikel 9: Bekanntgabe ins Ausland (Angemessenheit oder geeignete Garantien)
- Artikel 10: Vertretung in der Schweiz (bei keiner Niederlassung)
- Artikel 12: Register der Verarbeitungstätigkeiten (für Verantwortliche mit >250 VZÄ oder Hochrisikoverarbeitung)
- Artikel 19–21: Informationspflicht (Datenschutzhinweise für betroffene Personen)
- Artikel 22: Datenschutz-Folgenabschätzung (DPIA) für Hochrisikoverarbeitungen
- Artikel 25: Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen
- Artikel 26: Rechte betroffener Personen (Auskunft, Berichtigung, Löschung, Einschränkung, Übertragbarkeit, Widerspruch)
- Artikel 24: Meldung von Verletzungen an EDÖB bei wahrscheinlich hohem Risiko
- Artikel 328b OR: Überwachung von Arbeitnehmenden und Persönlichkeitsschutz

**FADP / GDPR-Angleichung**: Das revidierte DSG (in Kraft seit 1. September 2023) ist strukturell und inhaltlich weitgehend an die DSGVO angeglichen. Für Organisationen, die beiden Regelwerken unterliegen, erfüllt ein DSGVO-konformes Programm in der Regel auch die DSG-Anforderungen. Wesentliche Unterschiede: Das DSG kennt keine obligatorische DSB-Pflicht; die schweizerische Angemessenheitsliste unterscheidet sich von der EU; kein Bussgeldsystem (stattdessen Strafrecht).

**PIMS-Auswirkungen**:

- Verarbeitungsregister geführt (Art. 12)
- Auftragsverarbeitungsverträge gemäss Art. 8 vorhanden
- Datenschutzhinweise an betroffene Personen erteilt (Art. 19–21)
- DPIA-Prozess für Hochrisikoverarbeitungen (Art. 22)
- Meldung von Verletzungen mit hohem Risiko an den EDÖB
- Sicherheitsmassnahmen für internationale Transfers bei Datenweitergabe aus der Schweiz

**Aufsichtsbehörde**: Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (EDÖB)

**Referenz**: Bundesgesetz über den Datenschutz (SR 235.1), in Kraft seit 1. September 2023

---

# Bedingte Anwendbarkeit (Stufe 2)

Diese Verordnungen und Standards gelten **nur wenn bestimmte Bedingungen erfüllt sind**.

## ISO/IEC 27701:2025 — Privacy Information Management System

**Standard**: ISO/IEC 27701:2025 (Zweite Ausgabe) — Privacy Information Management System

**Anwendbarkeitsauslöser**:

- Die Organisation **strebt eine ISO/IEC 27701:2025-Zertifizierung an** (entweder eigenständig oder kombiniert mit ISO 27001-Zertifizierung)
- Ein Kundenvertrag **fordert explizit** PIMS-Compliance mit diesem Standard

**Klassifikationshinweis**: ISO/IEC 27701:2025 ist in diesem Rahmen als Stufe 2 (Bedingt) klassifiziert. Es handelt sich nicht um eine rechtlich durchsetzbare Verordnung. Es wird nicht allein dadurch obligatorisch, dass die Organisation PII verarbeitet — GDPR und FADP erfüllen diese Rolle. Wenn eine Zertifizierung angestrebt oder vertraglich gefordert wird, wird es als bindende operative Verpflichtung behandelt, die für die Dauer der Zertifizierung Stufe 1 entspricht.

**Wesentliche Anforderungen**:

- Klausel 5: Kontext des PIMS (Verstehen der Organisation, interessierter Parteien, Geltungsbereich)
- Klausel 6: Führung (Engagement, Richtlinie, Rollen, Verantwortlichkeiten)
- Klausel 7: Planung (Risiken, Ziele, Privacy-by-Design-Auslöser)
- Klausel 8: Unterstützung (Ressourcen, Kompetenz, Bewusstsein, Kommunikation, dokumentierte Informationen)
- Klausel 9: Betrieb (betriebliche Planung, Risikobehandlung, DPIA-Prozess)
- Klausel 10: Leistungsbewertung (Monitoring, internes Audit, Management-Review)
- Klausel 11: Verbesserung (Nichtkonformität, Korrekturmassnahmen, kontinuierliche Verbesserung)
- Anhang A: Verantwortlichen-spezifische Kontrollen (A.1.x — 31 Kontrollen)
- Anhang A: Auftragsverarbeiter-spezifische Kontrollen (A.2.x — 18 Kontrollen)
- Anhang A: Gemeinsame Sicherheitskontrollen (A.3.x — 29 Kontrollen)
- Anhang B: Zuordnung von ISO/IEC 27001:2022-Kontrollen zu PIMS (normativ)

**PIMS-Auswirkungen**:

- Vollständige Umsetzung aller PRIV-POL-A.x.x-Kontrollgruppen-Richtlinien in 51-isms-core-privacy/
- Rollendetermination dokumentiert (Verantwortlicher, Auftragsverarbeiter oder beides pro Verarbeitungsaktivität)
- PIMS in ISO 27001 ISMS integriert oder darauf aufgebaut

**Hinweis zur Ausgabe**: ISO/IEC 27701:2025 (Zweite Ausgabe) ist ein eigenständiger PIMS-Standard, keine Erweiterungsklauseln für ISO 27001. Er kann unabhängig implementiert und zertifiziert werden. Wenn eine Organisation eine ISO 27001-Zertifizierung besitzt, bietet Anhang B die normative Zuordnung zwischen 27001-Kontrollen und 27701-Anforderungen.

**Referenz**: ISO/IEC 27701:2025, Information security, cybersecurity and privacy protection — Privacy information management system

---

## ISO/IEC 27018:2025 — Cloud-PII-Auftragsverarbeiter

**Standard**: ISO/IEC 27018:2025 (Dritte Ausgabe) — Information technology — Security techniques — Code of practice for protection of personally identifiable information (PII) in public clouds acting as PII processors

**Anwendbarkeitsauslöser**:

- Die Organisation handelt als **PII-Auftragsverarbeiter, der öffentliche Cloud-Dienste betreibt** (Cloud-Dienstanbieter, der Kunden-PII verarbeitet)
- Kundenverträge **fordern explizit** ISO/IEC 27018-Compliance oder -Zertifizierung
- Eine Zertifizierung gemäss ISO/IEC 27018:2025 wird angestrebt

**Inhalt von ISO 27018:2025**:

ISO 27018:2025 umfasst zwei unterschiedliche Teile:

- **Hauptteil (Klauseln 5–18)**: Umsetzungsleitlinien für ISO/IEC 27002:2022-Kontrollen in öffentlichen Cloud-Umgebungen. Diese Leitlinien sind informativ und begründen keine zusätzlichen obligatorischen Anforderungen über ISO 27002 hinaus.
- **Anhang A (normativ bei Zertifizierung)**: 25 PII-spezifische Kontrollen, die nicht in ISO 27002 enthalten sind. Dies sind die genuinen neuen Cloud-PII-Auftragsverarbeiter-Pflichten (Einwilligung, Transparenz, Zweckbindung, Rückgabe/Löschung, Sub-Auftragsverarbeiter-Offenlegung usw.).

**PIMS-Lieferung**: ISO 27018 Anhang A-Kontrollen (25 Kontrollen) werden als Crosswalk-Overlay auf `priv-a.2.5.7-9-sub-processor-management` und angrenzende Auftragsverarbeiter-Pakete geliefert. Sie sind KEINE eigenständigen Pakete.

**Bewertung**: Wenn die Organisation öffentliche Cloud-Dienste bereitstellt und Kunden-PII verarbeitet → ISO 27018:2025 Anhang A auf Anwendbarkeit prüfen.

**Referenz**: ISO/IEC 27018:2025, Dritte Ausgabe, 2025

---

## UK-Datenschutz-Grundverordnung (UK GDPR)

**Verordnung**: UK GDPR (beibehaltenes EU-Recht in der durch die Data Protection, Privacy and Electronic Communications (Amendments etc) (EU Exit) Regulations 2019 geänderten Fassung) + Data Protection Act 2018, weiter geändert durch den **Data (Use and Access) Act 2025**

**Anwendbarkeitsauslöser**:

- Die Organisation **verarbeitet personenbezogene Daten von Personen in Grossbritannien** nach dem Brexit (1. Januar 2021)
- Die Organisation hat eine **Niederlassung im Vereinigten Königreich**
- Die Organisation **richtet sich an Personen im Vereinigten Königreich oder überwacht sie**

**Wesentliche Unterschiede zur EU GDPR**:

- Aufsichtsbehörde: Information Commissioner's Office (ICO), nicht EU-Datenschutzbehörden
- Internationale Transfers: UK-Angemessenheitsverordnungen (nicht EU-Angemessenheitsbeschlüsse); EU→UK-Transfer durch EU-Angemessenheitsbeschluss für UK gedeckt (aktuell zum Zeitpunkt der Abfassung — auf Überprüfung achten)
- UK Standard Contractual Clauses (IDTA) oder UK Addendum zu EU SCCs für Transfers in Drittländer erforderlich
- **Data (Use and Access) Act 2025**: Führt gezielte UK-spezifische Änderungen der Datenschutzpflichten ein; DSB bewertet laufend die Auswirkungen auf Organisationen mit UK-Betrieb

**Bewertung**: Wenn die Organisation personenbezogene UK-Daten verarbeitet → UK GDPR-Compliance parallel zur EU GDPR erforderlich. Für die meisten CH/EU-Organisationen mit UK-Betrieb oder UK-Kunden wird dies obligatorisch sein. ICO-Leitlinien zur Umsetzung des Data (Use and Access) Act 2025 beobachten.

**Referenz**: UK GDPR; Data Protection Act 2018 (UK); Data (Use and Access) Act 2025

---

## Lei Geral de Proteção de Dados (LGPD) — Brasilien

**Verordnung**: Lei n° 13.709/2018 — Lei Geral de Proteção de Dados Pessoais

**Anwendbarkeitsauslöser**:

- Die Organisation **verarbeitet personenbezogene Daten von in Brasilien befindlichen Personen**
- Verarbeitung **findet in Brasilien statt** (unabhängig von der Niederlassung)
- Verarbeitung erfolgt **zum Zweck des Angebots von Waren oder Dienstleistungen** in Brasilien

**Wesentliche Anforderungen** (GDPR-ähnliche Struktur):

- Rechtmässige Grundlagen für die Verarbeitung (10 Rechtsgrundlagen, einschliesslich Einwilligung und berechtigtes Interesse)
- Rechte betroffener Personen (Auskunft, Berichtigung, Löschung, Übertragbarkeit, Widerspruch)
- Pflichten des Datenschutzbeauftragten (DSB/Encarregado)
- Meldung von Sicherheitsvorfällen an ANPD (brasilianische DPA) und betroffene Personen
- Internationale Transfers: Angemessenheitsbeschluss, Vertragsklauseln oder Einwilligung

**Bewertung**: Wenn die Organisation brasilianische Kunden bedient oder personenbezogene brasilianische Daten verarbeitet → LGPD-Anwendbarkeit prüfen. Strukturell ähnlich der GDPR; ein bestehendes GDPR-konformes Programm deckt die meisten Anforderungen ab.

**Aufsichtsbehörde**: Autoridade Nacional de Proteção de Dados (ANPD)

**Referenz**: Lei n° 13.709/2018, in Kraft seit September 2020 (Durchsetzung ab August 2021)

---

## Personal Information Protection Law (PIPL) — China

**Verordnung**: Personal Information Protection Law (个人信息保护法), in Kraft seit 1. November 2021

**Anwendbarkeitsauslöser**:

- Die Organisation **verarbeitet personenbezogene Daten von in China befindlichen Personen**
- Die Organisation bietet **Produkte oder Dienstleistungen** für Personen in China an
- Die Organisation **analysiert das Verhalten** von Personen in China

**Wesentliche Anforderungen**:

- Einwilligung als primäre Rechtsgrundlage (engerer Geltungsbereich für berechtigtes Interesse als GDPR)
- Datenlokalisierung: Personenbezogene Daten chinesischer Personen, die in China gesammelt werden, können eine lokale Speicherung erfordern
- Grenzüberschreitende Transfers: Drei Mechanismen verfügbar — (1) Sicherheitsbewertung durch CAC für Transfers über Volumenschwellen erforderlich; (2) Standardvertrag (SCC) für kleinere Volumina; (3) Personenbezogener Datenschutz-Zertifizierung durch anerkannte Stelle (für Transfers innerhalb multinationaler Gruppen — CAC-Durchführungsbestimmungen beachten)
- Datenschutzbeauftragter: Erforderlich, wenn Verarbeitung über Schwellenwerte hinausgeht
- Meldung von Verletzungen innerhalb von 24 Stunden an die Behörde

**Bewertung**: Wenn die Organisation Dienste für Personen in China anbietet oder personenbezogene Daten aus China sammelt → PIPL-Anwendbarkeitsbewertung erforderlich. Hinweis: PIPL ist in mehreren Aspekten strenger als GDPR (Einwilligungsstandard, Lokalisierung, grenzüberschreitende Transfer-Kontrollen).

**Aufsichtsbehörde**: Cyberspace Administration of China (CAC — 国家互联网信息办公室)

**Referenz**: PIPL 2021; CAC Provisions on Standard Contracts for Cross-border Transfer of Personal Information (2023)

---

## Weitere bedingt anwendbare Datenschutzbestimmungen

Organisationen sollten zusätzliche bedingt anwendbare Datenschutzvorschriften basierend auf ihren spezifischen Verarbeitungsaktivitäten und ihrem geografischen Geltungsbereich prüfen und dokumentieren:

| Vorschrift | Auslöser | Aufsichtsbehörde |
|------------|----------|------------------|
| **CCPA/CPRA** (Kalifornien) | Bedienung von Personen in Kalifornien; Umsatz-/Datenschwellen | California Privacy Protection Agency (CPPA) |
| **PIPEDA** (Kanada) | Kommerzielle Verarbeitung personenbezogener kanadischer Daten | Office of the Privacy Commissioner of Canada (OPC) |
| **PDPA** (Singapur) | Verarbeitung personenbezogener Daten von Personen in Singapur | Personal Data Protection Commission (PDPC) |
| **APPI** (Japan) | Verarbeitung personenbezogener Daten von Personen in Japan | Personal Information Protection Commission (PPC) |
| **POPIA** (Südafrika) | Verarbeitung personenbezogener Daten von Personen in Südafrika | Information Regulator |
| **Sektorvorschriften** | Gesundheitswesen (eHealth), Finanzdaten, Kinderdaten | Sektorzuständige Behörde |

**Bewertungsansatz**: Für jeden neuen geografischen Markt oder jede neue Verarbeitungsaktivität ist anhand der vorstehenden Auslöser zu prüfen, ob eine Datenschutzverordnung gilt. Die Feststellung ist im Regulatorischen Monitoring-Log zu dokumentieren (siehe Abschnitt Pflege).

---

# Informativer Verweis / Bewährte Verfahren (Stufe 3)

## ISO/IEC 27017:2019 — Cloud-Sicherheitskontrollen

**Standard**: ISO/IEC 27017:2019 — Information technology — Security techniques — Code of practice for information security controls based on ISO/IEC 27002 for cloud services

**Rolle in PRIV-POL-00**: ISO 27017 ist ein **Cloud-Sicherheits**-Standard (kein Datenschutzstandard). Er wird hier als unterstützende technische Basis referenziert, weil ISO 27018:2025 (Anhang A — Cloud-PII-Auftragsverarbeiter-Kontrollen) direkt auf dem durch ISO 27017 etablierten Sicherheitsfundament aufbaut. Organisationen, die ISO 27018 implementieren, sollten ISO 27017-Kontrollen als Sicherheitsbasis für Cloud-PII-Verarbeitungsumgebungen behandeln.

**Primäre Heimat**: ISO 27017 ist in **ISMS-POL-00** (Stufe 3) als Cloud-Sicherheits-Best-Practice referenziert. Seine Präsenz in PRIV-POL-00 ist nur als datenschutzunterstützende Referenz.

**Wesentliche Leitlinienbereiche** (relevant für Cloud-PII-Verarbeitung):

- Geteilte Verantwortung zwischen Cloud-Kunden und Cloud-Dienstanbietern
- Virtuelle Maschinenhärtung und Isolierung
- Administrative operative Sicherheit
- Monitoring von Cloud-Diensten
- Netzwerksicherheit in Cloud-Umgebungen

**Verwendung im PIMS**: Referenziert in `priv-a.2.4.2-4-processor-lifecycle-controls` und `priv-a.2.5.7-9-sub-processor-management` (ISO 27018 Overlay-Pakete).

**Referenz**: ISO/IEC 27017:2019, Information security controls for cloud services

---

## ISO/IEC 27017:2025 — Bevorstehend (Beobachten — Bei Veröffentlichung übernehmen)

**Status**: **Noch nicht veröffentlicht** zum Zeitpunkt dieser Richtlinie.

ISO/IEC 27017:2025 wird als zweite Ausgabe des Cloud-Sicherheitskontroll-Standards entwickelt. Wenn veröffentlicht, ist diese Richtlinie zu aktualisieren, um ISO/IEC 27017:2025 an Stelle von (oder neben) ISO/IEC 27017:2019 zu referenzieren.

**Massnahmen bei Veröffentlichung**:

1. ISO/IEC 27017:2025 auf strukturelle Änderungen gegenüber der Ausgabe 2019 überprüfen
2. Auswirkungen auf Kontrollpakete `priv-a.2.4.2-4` und `priv-a.2.5.7-9` bewerten
3. PRIV-POL-00 Stufe-3-Referenz von 2019 auf 2025 aktualisieren
4. Änderungen an relevante Kontrollgruppen-Eigentümer kommunizieren
5. Kontrollpaket-IMPs aktualisieren, wo 27017-Leitlinien referenziert werden

**Beobachten**: ISO.org Veröffentlichungen — SC 27 Arbeitsprogramm — WG 4 (Sicherheitskontrollen und -dienste)

---

## ISO/IEC 27002:2022 — Umsetzungsleitfaden für Sicherheitskontrollen

**Standard**: ISO/IEC 27002:2022 — Information security, cybersecurity and privacy protection — Information security controls

**Rolle in PRIV-POL-00**: ISO 27002 bietet Umsetzungsleitlinien für die A.3.x gemeinsamen Sicherheitskontrollen (ISO 27701:2025 Anhang A.3). Die 29 gemeinsamen A.3-Kontrollen sind datenschutzspezifische Overlays auf dem durch ISO 27002 etablierten Informationssicherheits-Kontrollrahmen.

**Referenz**: ISO/IEC 27002:2022

---

## NIST Privacy Framework 2.0

**Rahmen**: NIST Privacy Framework: A Tool for Improving Privacy Through Enterprise Risk Management, Version 2.0 (2024)

**Rolle in PRIV-POL-00**: Informativer Verweis für die Datenschutzrisikomanagement-Methodik. Bietet ein funktionsbasiertes (Identify-P, Govern-P, Control-P, Communicate-P, Protect-P) Vokabular für die Reifegradsbewertung von Datenschutzprogrammen. Version 2.0 ist enger am NIST Cybersecurity Framework 2.0 ausgerichtet, fügt die Govern-P-Funktion hinzu und stärkt die Leitlinien zu Supply-Chain-Datenschutzrisiken. Kann für Gap-Analysen und Datenschutzrisikobewertungs-Benchmarking verwendet werden.

**Referenz**: NIST Privacy Framework v2.0, NIST, 2024

---

# Bestimmung der regulatorischen Datenschutzanwendbarkeit

## Bewertungsprozess

Bei der Beurteilung, ob eine Datenschutzverordnung für die Organisation gilt, ist dieser Entscheidungsprozess anzuwenden:

**Schritt 1: Verarbeitungsaktivitäten identifizieren**

Jede Kategorie der PII-Verarbeitung dokumentieren: welche Daten, wessen Daten (betroffene Personen), in welchen Territorien, zu welchem Zweck, als Verantwortlicher oder Auftragsverarbeiter.

**Schritt 2: Geografische Auslöser anwenden**

Für jede Verordnung den Anwendbarkeitsauslöser gegen die Verarbeitungsübersicht prüfen:

| Auslösertyp | Fragen |
|-------------|--------|
| **Niederlassung** | Ist die Organisation in der Rechtsordnung niedergelassen? |
| **Standort der betroffenen Person** | Befinden sich Personen in der Rechtsordnung, deren Daten verarbeitet werden? |
| **Ausrichtung / Beobachtung** | Richtet sich die Organisation an Personen in der Rechtsordnung oder beobachtet sie? |
| **Dienstleistungserbringung** | Bietet die Organisation Waren/Dienstleistungen in der Rechtsordnung an? |

**Schritt 3: Verantwortlichen- vs. Auftragsverarbeiter-Rolle bestimmen**

Datenschutzpflichten unterscheiden sich erheblich je nach Rolle:

- **Verantwortlicher**: Bestimmt Zwecke und Mittel der Verarbeitung → Volle Stufe-1-Pflichten gelten (GDPR Artikel 5–39)
- **Auftragsverarbeiter**: Verarbeitet im Auftrag eines Verantwortlichen → Auftragsverarbeiter-spezifische Pflichten gelten (GDPR Artikel 28; ISO 27701 Anhang A.2)
- **Beides**: Wenn die Organisation für einige Verarbeitungen als Verantwortlicher und für andere als Auftragsverarbeiter handelt → Pflichten gelten pro Verarbeitungsaktivität

**Schritt 4: Klassifizieren und dokumentieren**

| Befund | Massnahme |
|--------|-----------|
| Verordnung gilt — keine Bedingungen | Als Stufe 1 (Obligatorisch) klassifizieren |
| Verordnung gilt nur wenn Bedingung erfüllt | Als Stufe 2 (Bedingt) klassifizieren — Auslöser dokumentieren |
| Standard bietet Leitlinien — nicht rechtlich durchsetzbar | Als Stufe 3 (Informativ) klassifizieren |
| Verordnung explizit nicht anwendbar | Als Nicht Anwendbar mit Begründung dokumentieren |

**Schritt 5: Aufzeichnungen aktualisieren**

Das Datenschutz-Regulatorische-Register (im PIMS-Dokumentations-Repository gepflegt) mit Feststellung, Begründung und Überprüfungsdatum aktualisieren.

---

## Vorlage für die Datenschutz-Regulatorische-Anwendbarkeitsmatrix

Diese Vorlage verwenden, um die Anwendbarkeit für jede Verordnung zu dokumentieren:

| Verordnung | Stufe | Gilt? | Auslöser | Bewertungsdatum | Prüfer | Nächste Überprüfung |
|-----------|-------|-------|----------|-----------------|--------|---------------------|
| EU GDPR | 1 | Ja/Nein | Verarbeitung EU-Personendaten | [Date] | DSB | Jährlich |
| CH FADP | 1 | Ja/Nein | Schweizer Betrieb | [Date] | DSB | Jährlich |
| ISO 27701:2025 | 1/2 | Ja/Nein | Zertifizierung angestrebt | [Date] | ISB | Jährlich |
| ISO 27018:2025 | 2 | Ja/Nein | Cloud-PII-Auftragsverarbeiter | [Date] | ISB | Jährlich |
| UK GDPR | 2 | Ja/Nein | UK-Personendaten | [Date] | DSB/Legal | Jährlich |
| LGPD | 2 | Ja/Nein | Brasilianische Personendaten | [Date] | Legal | Jährlich |
| PIPL | 2 | Ja/Nein | Chinesische Personendaten | [Date] | Legal | Jährlich |

---

## Wann neu zu bewerten ist

| Auslöserereignis | Erforderliche Massnahme |
|-----------------|-------------------------|
| Neuer geografischer Markt erschlossen | Vollständige Anwendbarkeitsbewertung für diese Rechtsordnung |
| Neue Verarbeitungsaktivität (neues Produkt, Dienst, Datentyp) | Verantwortlichen-/Auftragsverarbeiter-Rolle + anwendbare Verordnungen |
| Wechsel von On-Premises zu Cloud-Verarbeitung | ISO 27018:2025-Bewertung |
| Kundenvertrag mit expliziten Datenschutzanforderungen | Vertragsspezifische Stufen-Aktualisierung |
| Neue Verordnung veröffentlicht oder in Kraft getreten | Anwendbarkeit prüfen, Register aktualisieren |
| Bestehende Verordnung wesentlich geändert | Betroffene Stufen-Klassifikation neu bewerten |
| ISO 27017:2025 veröffentlicht | Stufe-3-Referenz aktualisieren; Kontrollpaket-Auswirkungen bewerten |
| Geschäftliche Veränderung (Akquisition, neue Einheit, Auslagerung) | Vollständige Anwendbarkeits-Neubewertung für betroffene Aktivitäten |

---

# Verwendung in PIMS-Richtlinien

## Standard-Referenzsprache

Alle PIMS-Kontrollgruppen-Richtlinien (PRIV-POL-01 und alle PRIV-POL-A.x.x-Kontrollgruppen-POLs) SOLLEN einen Abschnitt **Regulatorischer Rahmen** mit dieser Standard-Referenz enthalten:

```
## Regulatorischer Rahmen

Diese Richtlinie operiert innerhalb des in PRIV-POL-00 etablierten
datenschutz-regulatorischen Rahmens.
Folgende Pflichten sind für diese Kontrollgruppe relevant:

**Obligatorisch (Stufe 1):**
- EU GDPR: [spezifische Artikel relevant für diese Kontrollgruppe]
- CH FADP: [spezifische Artikel]
- ISO/IEC 27701:2025: [spezifische Klauseln/Kontrollen]

**Bedingt (Stufe 2):**
- ISO/IEC 27018:2025: [Anhang A-Kontrollen, wenn Auftragsverarbeiter-Pakete]

**Informativ (Stufe 3):**
- ISO/IEC 27017:2019: [wenn Cloud-bezogene Kontrollen]
```

## Rollenkennzeichnung in Kontrollpaketen

Kontrollgruppen-Richtlinien SOLLEN die angesprochene organisatorische Rolle klar angeben:

- `privacy-controller/`-Pakete → **«Diese Richtlinie gilt für die Organisation in ihrer Rolle als PII Verantwortlicher.»**
- `privacy-processor/`-Pakete → **«Diese Richtlinie gilt für die Organisation in ihrer Rolle als PII Auftragsverarbeiter.»**
- `privacy-shared/`-Pakete → **«Diese Richtlinie gilt für die Organisation sowohl als PII Verantwortlicher als auch als PII Auftragsverarbeiter.»**

---

# Regulatorischer Rahmen (Diese Richtlinie)

## Obligatorische Compliance

| Verordnung | Version | Status | PIMS-Kontrollrelevanz |
|-----------|---------|--------|----------------------|
| EU GDPR | 2016/679 | Aktiv — Obligatorisch | Alle PRIV-POL-A.x.x-Kontrollgruppen |
| CH FADP/nDSG | SR 235.1 (2023) | Aktiv — Obligatorisch | Alle PRIV-POL-A.x.x-Kontrollgruppen |

## Bedingte Anwendbarkeit

| Verordnung | Version | Status | Auslöser |
|-----------|---------|--------|----------|
| ISO/IEC 27701:2025 | Ausg. 2, 2025 | Bedingt | Zertifizierung angestrebt oder vertraglich gefordert |
| ISO/IEC 27018:2025 | Ausg. 3, 2025 | Bedingt | Cloud-PII-Auftragsverarbeiter-Dienste |
| UK GDPR + DUA Act 2025 | 2018/2021/2025 | Bedingt | UK-Personendaten |
| LGPD | 2018 | Bedingt | Brasilianische Personendaten |
| PIPL | 2021 | Bedingt | Chinesische Personendaten |

## Informativer Verweis

| Standard | Version | Status | Verwendung |
|---------|---------|--------|------------|
| ISO/IEC 27017:2019 | 2019 | Aktiv — Stufe 3 | Cloud-Sicherheits-Basis (unterstützt 27018-Umsetzung) |
| ISO/IEC 27017:2025 | Noch nicht veröffentlicht | Bevorstehend | Bei Veröffentlichung übernehmen |
| ISO/IEC 27002:2022 | 2022 | Aktiv — Stufe 3 | Sicherheitskontroll-Leitlinien für A.3 gemeinsame Kontrollen |
| NIST Privacy Framework | 2.0, 2024 | Aktiv — Stufe 3 | Datenschutzrisikomanagement-Methodik |

## Audit-Referenzen

| Anforderung | Nachweis | Ablageort |
|------------|---------|-----------|
| Regulatorische Anwendbarkeit dokumentiert | Diese Richtlinie + Datenschutz-Regulatorisches-Register | PIMS-Dokumentations-Repository |
| DPA-Registrierungen aktuell | Registrierungszertifikate | Legal/Compliance-Akte |
| ROPA geführt | Verzeichnis der Verarbeitungstätigkeiten | [GRC-Plattform / ISMS-System] |
| DPIA-Prozess dokumentiert | DPIA-Vorlage + abgeschlossene DPIAs | [GRC-Plattform] |
| Auftragsverarbeitungsverträge vorhanden | Unterzeichnete AVV gemäss GDPR Art. 28 | Vertragsablage |

---

# Aktueller Regulatorischer Status

## Stufe 1: Obligatorische Compliance (Aktiv)

| Verordnung | Anwendbarkeitsbasis | Bestätigt | Nächste Überprüfung |
|-----------|---------------------|-----------|---------------------|
| EU GDPR | Verarbeitung EU-Personendaten | [Date] | [Date + 12M] |
| CH FADP | Schweizer Betrieb | [Date] | [Date + 12M] |

## Stufe 2: Bedingte Anwendbarkeit

| Verordnung | Aktueller Status | Auslöser-Status | Massnahme |
|-----------|-----------------|----------------|-----------|
| ISO 27701:2025 | [Anwendbar / Nicht Anwendbar] | [Zertifizierung angestrebt oder vertraglich gefordert?] | [Als bindende Verpflichtung behandeln, wenn anwendbar] |
| ISO 27018:2025 | [Anwendbar / Nicht Anwendbar] | [Cloud-PII-Auftragsverarbeiter-Dienste im Geltungsbereich?] | [Anhang A-Overlay implementieren, wenn anwendbar] |
| UK GDPR + DUA Act 2025 | [Anwendbar / Nicht Anwendbar] | [UK-Personendaten im Geltungsbereich?] | [Dokumentieren, wenn anwendbar; ICO DUA-Leitlinien beobachten] |
| LGPD | [Anwendbar / Nicht Anwendbar] | [Brasilianische Personendaten im Geltungsbereich?] | [Bewerten, wenn anwendbar] |
| PIPL | [Anwendbar / Nicht Anwendbar] | [Chinesische Personendaten im Geltungsbereich?] | [Bewerten, wenn anwendbar] |

## Stufe 3: Informativer Verweis (Aktive Verwendung)

| Standard | Verwendung | Referenziert in |
|---------|-----------|----------------|
| ISO/IEC 27017:2019 | Cloud-Sicherheits-Basis | priv-a.2.4 und priv-a.2.5 Auftragsverarbeiter-Pakete |
| ISO/IEC 27002:2022 | Sicherheitskontroll-Leitlinien | Alle A.3 gemeinsamen Kontrollpakete |
| NIST Privacy Framework 2.0 | Risiko-Methodik-Referenz | PIMS-Risikobewertungsdokumentation |

---

# Pflege und Aktualisierungen

## Überprüfungsplan

| Überprüfungstyp | Häufigkeit | Leitung | Lieferobjekt |
|----------------|-----------|---------|-------------|
| Jährliche umfassende Überprüfung | Jährlich (Q4) | DSB + ISB + Legal | Aktualisierte Richtlinie + Managementbriefing |
| Vierteljährliches Monitoring | Vierteljährlich | DSB + Legal | Aktualisierung des Regulatorischen Monitoring-Logs |
| Ausgelöste Bewertung | Bei Auslöserereignis | DSB (Leitung) | Bericht zur ausgelösten Bewertung |
| ISO 27017:2025-Beobachtung | Bei Veröffentlichung | ISB | Kontrollpaket-Auswirkungsbewertung |

## Regulatorische Monitoring-Quellen

| Quelle | Monitoring-Häufigkeit | Verantwortlich |
|--------|---------------------|----------------|
| EU Amtsblatt (eur-lex.europa.eu) | Monatlich | Legal |
| EDPB-Leitlinien und Stellungnahmen (edpb.europa.eu) | Monatlich | DSB |
| EDÖB-Veröffentlichungen (edoeb.admin.ch) | Vierteljährlich | DSB |
| ISO.org — SC 27-Veröffentlichungen | Vierteljährlich | ISB |
| ICO (UK) Leitlinien | Vierteljährlich (wenn UK im Geltungsbereich) | Legal |
| Nationale DPA-Leitlinien (Mitgliedstaaten) | Vierteljährlich | DSB |

## Kommunikation

Änderungen an dieser Richtlinie SOLLEN kommuniziert werden an:

- Alle PIMS-Kontrollgruppen-Richtlinieneigentümer
- Datenschutzbeauftragte / Dateneigentümer
- Auftragsverarbeiter unter Vertrag mit der Organisation
- Interne Revision

---

# Verwandte Dokumente

| Dokument | Typ | Beziehung |
|---------|-----|-----------|
| ISMS-POL-00 | ISMS-Richtlinie | Übergeordnet — Informationssicherheits-Regulatorischer Rahmen |
| PRIV-POL-01 | PIMS-Richtlinie | Geschwisterdokument — Datenschutz-Governance und Entscheidungsfindung |
| priv-a.1.2.6-9 POL | Kontrollgruppen-Richtlinie | Datenschutz-Governance und Verzeichnisse (Verantwortlicher) |
| priv-a.3.13-16 POL | Kontrollgruppen-Richtlinie | Datenschutz-Compliance und Audit (gemeinsam) |
| ISO/IEC 27701:2025 | Standard | Primärer Governance-Standard |
| ISO/IEC 27018:2025 | Standard | Ergänzender Standard für Cloud-PII-Auftragsverarbeiter |

---

# Glossar

| Begriff | Definition |
|---------|------------|
| **PII** | Personally Identifiable Information — jede Information, die zur direkten oder indirekten Identifikation einer natürlichen Person verwendet werden kann (entspricht «personenbezogenen Daten» gemäss GDPR/FADP) |
| **PII Principal** | Die natürliche Person, auf die sich PII bezieht (entspricht «betroffener Person») |
| **Verantwortlicher** | Die Einheit, die Zwecke und Mittel der PII-Verarbeitung bestimmt (GDPR: «Verantwortlicher») |
| **Auftragsverarbeiter** | Die Einheit, die PII im Auftrag eines Verantwortlichen verarbeitet (GDPR: «Auftragsverarbeiter») |
| **Verarbeitung** | Jeder mit PII durchgeführte Vorgang: Erhebung, Aufzeichnung, Speicherung, Anpassung, Abruf, Verwendung, Weitergabe, Löschung |
| **PIMS** | Privacy Information Management System — das unter ISO/IEC 27701:2025 etablierte Management-System-Framework |
| **DPA** | Data Protection Authority — die Aufsichtsbehörde, die für die Durchsetzung des Datenschutzgesetzes in einer Rechtsordnung verantwortlich ist |
| **DPIA** | Data Protection Impact Assessment — strukturierte Bewertung von Hochrisiko-Verarbeitungsaktivitäten |
| **ROPA** | Records of Processing Activities — Dokumentation, die durch GDPR Artikel 30 und FADP Artikel 12 gefordert wird |
| **Obligatorisch** | Rechtspflicht, durch DPA oder Gericht durchsetzbar, Nichteinhaltung hat Konsequenzen |
| **Bedingt** | Gilt nur, wenn bestimmte Auslöser erfüllt sind (Rechtsordnung, Datentyp, Rolle, Zertifizierung) |
| **Informativ** | Referenz für bewährte Verfahren, nicht rechtlich durchsetzbar, freiwillige Übernahme |
| **Stufe 1** | Obligatorische Compliance (rechtlich, vertraglich) |
| **Stufe 2** | Bedingte Compliance (kontextabhängig) |
| **Stufe 3** | Informativer Verweis (bewährte Verfahren, freiwillig) |
| **Anwendbarkeitsauslöser** | Ereignis oder Bedingung, das/die dazu führt, dass eine Stufe-2-Verordnung anwendbar wird |
| **Regulatorisches Monitoring** | Systematische vierteljährliche Überprüfung regulatorischer Änderungen und organisatorischer Aktivitäten zur Erkennung von Anwendbarkeitsänderungen |
| **GL** | Geschäftsleitung — das deutschsprachige/schweizerische Äquivalent für Executive Management oder Geschäftsführendes Organ; wird in der PIMS-Dokumentation austauschbar mit «Executive Management» verwendet. Jeder Verweis auf «GL» in PIMS-Richtlinien bezeichnet das leitende Exekutivgremium, das für die Governance der Organisation verantwortlich ist |

---

# Abschlusserklärung

Diese Richtlinie legt die regulatorische Datenschutzanwendbarkeit für das Privacy Information Management System der Organisation fest.

**Was diese Richtlinie festlegt:**

- Identifikation der anwendbaren Datenschutzverordnungen (obligatorisch, bedingt, informativ)
- Bewertungsmethodik zur Bestimmung der regulatorischen Datenschutzanwendbarkeit
- Überprüfungs- und Aktualisierungsprozesse bei Änderungen im regulatorischen Datenschutzumfeld

**Was diese Richtlinie NICHT festlegt:**

- Datenschutz-Risikobehandlungsentscheidungen (behandelt im PIMS-Risikomanagement und Kontrollgruppen-IMPs)
- Anforderungen an die Kontrollumsetzung (behandelt in PRIV-POL-A.x.x-Kontrollgruppen-POLs und IMPs)
- Compliance-Status oder -Verifizierung (behandelt in Compliance-Monitoring-Prozessen)
- Informationssicherheitspflichten (behandelt in ISMS-POL-00)

**Trennung der Verantwortlichkeiten:**

- **Diese Richtlinie (PRIV-POL-00)**: Definiert WELCHE Datenschutzverordnungen gelten
- **PRIV-POL-01**: Definiert WIE das PIMS geführt und Entscheidungen getroffen werden
- **Kontrollgruppen-POLs (PRIV-POL-A.x.x)**: Definieren WAS die Organisation pro Kontrollbereich tun muss
- **Kontrollgruppen-IMPs**: Definieren WIE die Kontrollanforderungen umzusetzen sind
- **Compliance-Monitoring**: Verifiziert und verfolgt den COMPLIANCE-Status

---

**ENDE VON PRIV-POL-00**

*«Regulatorische Datenschutzanwendbarkeit ist das Fundament. Umsetzung und Compliance sind das darauf errichtete Gebäude.»*

<!-- QA_VERIFIED: 2026-03-29 -->

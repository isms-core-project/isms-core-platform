<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.14-DE:framework:POL:a.5.14 -->
**ISMS-POL-A.5.14 — Informationsübermittlung**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Informationsübermittlung |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.14 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] | |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | ISB | Erstrichtlinie für ISO 27001:2022-Zertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Letzte Autorität: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.5.12-13 (Informationsklassifizierung und -kennzeichnung)
- ISMS-POL-A.8.24 (Einsatz von Kryptographie)
- ISMS-POL-A.5.19-23 (Cloud-Dienste)
- ISMS-POL-A.6.6 (Vertraulichkeits- und Geheimhaltungsvereinbarungen)
- ISMS-IMP-A.5.14.1-UG/TG (Übermittlungsregeln und -verfahren)
- ISMS-IMP-A.5.14.2-UG/TG (Sicherheitsbewertung von Kanälen)
- ISMS-IMP-A.5.14.3-UG/TG (Register der Übermittlungsvereinbarungen)
- ISO/IEC 27001:2022 Kontrolle A.5.14

---

## Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen von [Organisation] für die sichere Übermittlung von Informationen fest, um Informationen bei der Übertragung über alle Arten von Kommunikationskanälen und -einrichtungen zu schützen.

**Anwendungsbereich**: Diese Richtlinie gilt für alle Informationsübermittlungen, ob elektronisch, physisch oder mündlich, einschliesslich Übermittlungen innerhalb von [Organisation] und mit externen Parteien.

**Zweck**: Definition der organisatorischen Anforderungen an die Sicherheit der Informationsübermittlung. Diese Richtlinie legt fest, WELCHE Übermittlungsmethoden genehmigt sind und WER berechtigt ist. Umsetzungsverfahren (WIE) sind separat in ISMS-IMP-A.5.14 (UG/TG-Varianten) dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich des Schweizer nDSG, der EU DSGVO und ISO/IEC 27001:2022. Bedingte branchenspezifische Anforderungen (FINMA, PCI DSS v4.0.1) gelten, sofern die Geschäftstätigkeit von [Organisation] deren Anwendbarkeit auslöst.

---

**Kontrollausrichtung & Anwendungsbereich**

**ISO/IEC 27001:2022 Kontrolle A.5.14**

**ISO/IEC 27001:2022 Anhang A.5.14 – Informationsübermittlung**

> *Für alle Arten von Übermittlungseinrichtungen innerhalb der Organisation und zwischen der Organisation und anderen Parteien sollten Regeln, Verfahren oder Vereinbarungen zur Informationsübermittlung vorhanden sein.*

**Kontrollziele**:

- Schutz von Vertraulichkeit, Integrität und Verfügbarkeit von Informationen während der Übermittlung
- Sicherstellung geeigneter Übermittlungsmethoden entsprechend der Informationssensibilität
- Abschluss von Übermittlungsvereinbarungen mit externen Parteien
- Aufrechterhaltung der Rechenschaftspflicht und Prüfpfade für Übermittlungen

**Kontrolltyp**: Präventiv
**Kontrollkategorie**: Organisatorisch

**Diese Richtlinie adressiert**:

- Genehmigte Übermittlungsmethoden und -kanäle
- Übermittlungsanforderungen je Informationsklassifizierung
- Externe Übermittlungsvereinbarungen und -anforderungen
- Übermittlungsautorisierung und Rechenschaftspflicht
- Behandlung von Vorfällen bei Übermittlungsfehlern

## Was diese Richtlinie regelt

Diese Richtlinie:

- **Definiert** genehmigte Übermittlungsmethoden für jede Klassifizierungsstufe
- **Legt fest** die Anforderungen für externe und grenzüberschreitende Übermittlungen
- **Spezifiziert** Autorisierungsanforderungen für verschiedene Übermittlungstypen
- **Referenziert** anwendbare regulatorische Anforderungen gemäss ISMS-POL-00

## Was diese Richtlinie NICHT regelt

Diese Richtlinie regelt NICHT:

- **Konfiguration von Verschlüsselungstools** (siehe ISMS-IMP-A.5.14 und ISMS-POL-A.8.24)
- **Verfahren für Dateiübertragungsplattformen** (siehe ISMS-IMP-A.5.14)
- **Administration von Secure-Email-Gateways** (operative Dokumentation)
- **Beauftragung physischer Kurierdienstleistungen** (siehe ISMS-IMP-A.5.14)

**Begründung**: Die Trennung von Richtlinienanforderungen und Umsetzungsanleitungen ermöglicht:

- Stabilität der Richtlinie trotz Technologie- oder Plattformwechseln
- Flexibilität für unterschiedliche Übermittlungslösungen
- Klare Unterscheidung zwischen Governance (Richtlinie) und Ausführung (Umsetzung)

## Anwendungsbereich

**Diese Richtlinie gilt für**:

- Alle Informationsübermittlungen (elektronisch, physisch, mündlich)
- Alle Übermittlungsmethoden (E-Mail, Dateifreigabe, Kurier, persönliche Übergabe)
- Alle Mitarbeitenden (Angestellte, Auftragnehmer, Dritte), die Organisationsinformationen übermitteln
- Alle externen Übermittlungen an Kunden, Partner, Anbieter und Aufsichtsbehörden

**Nicht im Anwendungsbereich**:

- Persönliche Kommunikation ohne Bezug zu Organisationsinformationen
- Öffentliche Informationen, die bereits frei verfügbar sind
- Echtzeit-Datenbankreplikation (durch Systemarchitektur abgedeckt)

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** kategorisiert.

**Stufe 1: Obligatorische Compliance**

| Regulierung | Anwendbarkeit | Wesentliche Anforderungen |
|-------------|---------------|--------------------------|
| **Schweizer nDSG Art. 16–17** | Alle Personendatenübermittlungen | Anforderungen an grenzüberschreitende Übermittlungen |
| **ISO/IEC 27001:2022** | Zertifizierungsumfang | Kontrolle A.5.14 – Informationsübermittlung |

**Stufe 2: Bedingte Anwendbarkeit**

Gilt nur, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Regulierung | Auslösebedingung | Übermittlungsanforderungen |
|-------------|-----------------|---------------------------|
| **EU DSGVO Art. 44–49** | Verarbeitung europäischer Personendaten | Schutzgarantien für internationale Datenübermittlungen, SCCs |
| **FINMA** | Reguliertes Schweizer Finanzinstitut | Erhöhte Sicherheit für Finanzdatenübermittlungen |
| **Schweizer Bankgeheimnis** | Bankkundendaten | Strenge Übermittlungskontrollen |
| **PCI DSS v4.0.1** | Zahlungskartendaten | Verschlüsselungsanforderungen für Karteninhaberdaten |
| **HIPAA** | US-amerikanische Gesundheitsdaten | Business Associate Agreements |

**Stufe 3: Orientierende Hinweise**

Diese Rahmenwerke informieren die Umsetzung, begründen aber keine obligatorische Compliance, sofern nicht vertraglich gefordert:

- ISO 27002:2022 Umsetzungsleitfaden für A.5.14
- NIST SP 800-53 (System- und Kommunikationsschutz)
- CIS Controls v8.1 (Datenschutz)
- ENISA-Leitlinien zur Sicherheit der Datenübermittlung

**Compliance-Feststellung**: [Organisation] bestimmt anwendbare Stufe-2-Vorschriften durch regelmässige Bewertung der Geschäftstätigkeit. Bei Überschneidung mehrerer Vorschriften gelten die strengsten Übermittlungsanforderungen.

---

# Richtlinienaussagen

## Anforderungen an Übermittlungsmethoden

### Elektronische Übermittlung

**E-Mail-Kommunikation**:

| Klassifizierung | Anforderung |
|-----------------|-------------|
| ÖFFENTLICH | Standard-Unternehmens-E-Mail zulässig |
| INTERN | Nur Unternehmens-E-Mail; externe Empfänger erfordern eine dokumentierte geschäftliche Begründung (Zweck, Empfänger, Klassifizierung, Ablauf der Zugriffsberechtigung) |
| VERTRAULICH | Verschlüsselte E-Mail (TLS erzwungen) oder sichere Dateifreigabeplattform |
| EINGESCHRÄNKT | Ende-zu-Ende-verschlüsselte Plattform, Empfängerverifizierung erforderlich |

**E-Mail-Sicherheitskontrollen**:

- Transport Layer Security (TLS) für alle ausgehenden E-Mails obligatorisch
- S/MIME oder Äquivalent für VERTRAULICHE/EINGESCHRÄNKTE Anhänge
- E-Mail-Grössenlimits erzwungen (Anhänge >25 MB über sichere Dateifreigabe)
- DLP-Richtlinien aktiv zur Erkennung sensibler Datenmuster
- Warnhinweise für externe Empfänger vor dem Versand angezeigt

**Dateiübertragung**:

| Methode | Erlaubte Nutzung | Klassifizierungsgrenze |
|---------|-----------------|------------------------|
| Unternehmensbasierte Dateifreigabe (SharePoint/OneDrive) | Interne Übermittlungen | Bis EINGESCHRÄNKT |
| Sichere Dateiübertragungsplattform | Externe Übermittlungen | Bis EINGESCHRÄNKT |
| SFTP/SCP | Systemintegrationen | Bis VERTRAULICH |
| USB-Sticks (verschlüsselt) | Nur ausnahmsweise | Bis VERTRAULICH |
| Öffentliche Dateifreigabe (Dropbox, Google Drive) | Nie für Unternehmensdaten | Nur ÖFFENTLICH (private Nutzung) |

**Webbasierte Übermittlung**:

- HTTPS für alle Webübermittlungen erforderlich
- Zertifikatsvalidierung obligatorisch
- VERTRAULICHE und EINGESCHRÄNKTE Informationen dürfen ausschliesslich über genehmigte, im Register der genehmigten Übermittlungstools (ISMS-REG-EXCEPTIONS) aufgeführte webbasierte Dienste übermittelt werden; andere Ziele erfordern eine genehmigte Ausnahme
- Sichere Upload-Portale für die Einreichung von Kundendaten

### Physische Übermittlung

**Dokumentenübermittlung**:

| Klassifizierung | Übermittlungsmethode |
|-----------------|---------------------|
| ÖFFENTLICH | Standardpost oder Kurier |
| INTERN | Interne Post oder Standardkurier |
| VERTRAULICH | Versiegelter Umschlag, verfolgbarer Kurier, Empfängerunterschrift |
| EINGESCHRÄNKT | Doppelt versiegeltes Paket, konzessionierter Kurier, Übergabeprotokoll |

**Medienübermittlung** (USB, Festplatten, Sicherungsbänder):

- Alle Wechselmedien vor der Übermittlung verschlüsseln
- Medieninventar mit Trackingnummer erfassen
- Sicherer Kurier mit Übergabeprotokoll für VERTRAULICH und höher
- EINGESCHRÄNKTE Medien: Dedizierter Sicherheitskurier, manipulationssichere Verpackung

**Persönliche Übergabe**:

- Identität des Empfängers vor der Übergabe verifizieren
- Übermittlung mit Empfangsbestätigung dokumentieren
- EINGESCHRÄNKTE Informationen: Anwesenheit eines Zeugen erforderlich

### Mündliche Übermittlung

**Telefon-/Videokommunikation**:

| Klassifizierung | Anforderung |
|-----------------|-------------|
| ÖFFENTLICH/INTERN | Standard-Unternehmenssysteme |
| VERTRAULICH | Verifizierte Teilnehmer, keine Aufzeichnung ohne Einwilligung |
| EINGESCHRÄNKT | Nur sichere/verschlüsselte Kanäle, Teilnehmerverifizierung |

**Persönliche Gespräche**:

- VERTRAULICH: Privater Ort, keine unbefugten Zuhörer
- EINGESCHRÄNKT: Sicherheitsraum, keine elektronischen Geräte, ausschliesslich berechtigte Teilnehmer

## Anforderungen an externe Übermittlungen

### Übermittlungsvereinbarungen

Externe Übermittlungen der Klassifizierungsstufe INTERN oder höher müssen folgende Mindestanforderungen erfüllen:

**Mindestinhalte einer Vereinbarung**:

- Verpflichtungen des Empfängers zur Informationsbehandlung
- Beschränkungen der zulässigen Nutzung und Weitergabe
- Anforderungen an Rückgabe oder Vernichtung
- Pflichten zur Benachrichtigung bei Verletzungen
- Prüfrechte, sofern angemessen

**Vereinbarungstypen**:

| Übermittlungstyp | Erforderliche Vereinbarung |
|-----------------|---------------------------|
| Einmalige Übermittlung | Vertraulichkeitsbestätigung |
| Laufende Beziehung | NDA (gemäss ISMS-POL-A.6.6) |
| Anbieter/Lieferant | Auftragsverarbeitungsvertrag (bei Personendaten) |
| Kundendaten | Dienstleistungsvertrag mit Sicherheitsbedingungen |

### Grenzüberschreitende Übermittlungen

Übermittlungen ausserhalb der Schweiz/des EWR müssen folgendes einhalten:

**Rechtliche Anforderungen**:

- Überprüfung von Angemessenheitsbeschlüssen (Länderbewertung)
- Standarddatenschutzklauseln (SCCs), wo erforderlich
- Ergänzende Massnahmen für Hochrisiko-Jurisdiktionen; für grenzüberschreitende Übermittlungen von Personendaten ist ein Datenschutz-Folgenabschätzungsprotokoll zu erstellen und im Nachweisregister zu hinterlegen (einschliesslich Angemessenheitsbasis/SCC-Grundlage, Entscheid über ergänzende Massnahmen und DSB-Genehmigungsverweis)
- DSB-Genehmigung für Personendatenübermittlungen

**Technische Anforderungen**:

- Verschlüsselung bei der Übertragung obligatorisch
- Überprüfung der Einhaltung von Datenspeicherungsanforderungen
- Protokollierung und Überwachung der Übermittlungen

**Verbotene Ziele**:

- Länder, die Sanktionen unterliegen
- Jurisdiktionen ohne angemessenen Rechtsschutz (ohne geeignete Garantien)

### Kunden- und Drittparteidaten

Besondere Behandlung von Daten externer Parteien:

- Klassifizierung: Mindestens VERTRAULICH für alle Kundendaten
- Übermittlung: Gemäss vertraglichen Anforderungen des Kunden
- Dokumentation: Übermittlungsprotokolle gemäss vertraglichen/regulatorischen Anforderungen aufbewahren
- Benachrichtigung: Dateneigentümer über Übermittlungen informieren, soweit vertraglich gefordert

## Übermittlungskontrollen

### Autorisierung

**Autorisierungsmatrix für Übermittlungen**:

| Klassifizierung | Interne Übermittlung | Externe Übermittlung |
|-----------------|---------------------|---------------------|
| ÖFFENTLICH | Selbstautorisiert | Selbstautorisiert |
| INTERN | Selbstautorisiert | Genehmigung Vorgesetzte/r |
| VERTRAULICH | Genehmigung Vorgesetzte/r | Informationseigentümer + Vorgesetzte/r |
| EINGESCHRÄNKT | Abteilungsleitung | Abteilungsleitung + ISB |

### Protokollierung und Rechenschaftspflicht

Alle VERTRAULICHEN und EINGESCHRÄNKTEN Übermittlungen müssen protokolliert werden:

**Protokollinhalte**:

- Datum/Uhrzeit der Übermittlung
- Identifikation von Sender und Empfänger
- Informationsbeschreibung (nicht der Inhalt)
- Verwendete Übermittlungsmethode
- Autorisierungsreferenz

**Aufbewahrung**: Übermittlungsprotokolle werden mindestens 2 Jahre aufbewahrt.

### Vorfallsreaktion

Bei Übermittlungsfehlern oder vermutetem Kompromittierungen:

- Sofortige Benachrichtigung des ISB für VERTRAULICH und höher
- Untersuchung gemäss ISMS-POL-A.5.24-28 (Vorfallsmanagement)
- Benachrichtigung des Daten-/Informationseigentümers
- Regulatorische und vertragliche Benachrichtigungen bei Personendatenverletzungen erfolgen über den Vorfallsmanagementprozess (ISMS-POL-A.5.24-28) und das Datenschutz-Verletzungsbenachrichtigungsverfahren der Organisation, basierend auf den Anwendbarkeitsentscheiden gemäss ISMS-POL-00

---

# Rollen und Verantwortlichkeiten

## Verantwortlichkeitsmatrix

| Rolle | Verantwortlichkeiten bei Übermittlungen |
|-------|----------------------------------------|
| **Geschäftsleitung** | Übermittlungsrichtlinie genehmigen, externe EINGESCHRÄNKTE Übermittlungen autorisieren |
| **ISB** | Übermittlungsanforderungen definieren, Plattformen genehmigen, Vorfallsaufsicht |
| **IT-Betrieb** | Sichere Übermittlungsinfrastruktur implementieren, Plattformen verwalten |
| **Informationseigentümer** | Übermittlungen eigener Informationen autorisieren, Empfängerangemessenheit prüfen |
| **Abteilungsleitungen** | Abteilungsübermittlungen genehmigen, Compliance sicherstellen |
| **Alle Mitarbeitenden** | Genehmigte Übermittlungsmethoden verwenden, Informationen während der Übermittlung schützen |

## Eskalationspfad

- Unsicherheit bei Übermittlungsmethoden: Mitarbeitende → Vorgesetzte/r → ISB
- Externe Übermittlungsgenehmigung: Informationseigentümer → Abteilungsleitung → ISB (EINGESCHRÄNKT)
- Übermittlungsvorfall: Mitarbeitende → ISB → Geschäftsleitung (bei bedeutenden Vorfällen)

---

# Governance & Compliance

## Bewertungsrahmen

| Bewertung | Häufigkeit | Eigentümer | Nachweis |
|-----------|------------|------------|----------|
| Sicherheitsüberprüfung der Übermittlungsplattform | Vierteljährlich | IT-Betrieb | Plattformberichte |
| Wirksamkeit der DLP-Richtlinien | Monatlich | ISB | DLP-Berichte |
| Compliance bei grenzüberschreitenden Übermittlungen | Vierteljährlich | DSB | Compliance-Unterlagen |
| Inventar der Übermittlungsvereinbarungen | Jährlich | Rechtsabteilung | Vereinbarungsregister |

**Governance-Kennzahlen**:

- Nutzung genehmigter Übermittlungsmethoden (Ziel: 100 %)
- Behebungszeit bei DLP-Vorfällen (Ziel: <24 Stunden)
- Compliance bei grenzüberschreitenden Übermittlungen (Ziel: 100 %)
- Abdeckung durch Übermittlungsvereinbarungen (Ziel: 100 % bei laufenden Beziehungen)

## Richtlinienüberprüfung

- **Häufigkeit**: Mindestens jährlich
- **Auslöser**: Neue Übermittlungstechnologien, regulatorische Änderungen, Sicherheitsvorfälle
- **Prüfer**: ISB, DSB, IT-Betrieb, Rechtsabteilung
- **Genehmigung**: Geschäftsleitung

## Ausnahmenmanagement

**Zulässige Ausnahmen**:

- Alternative Übermittlungsmethode bei Nichtverfügbarkeit der genehmigten Methode (mit kompensierenden Kontrollen)
- Notfallübermittlungen mit nachträglicher Dokumentation innerhalb von 24 Stunden
- Legacy-Systemübermittlungen mit dokumentiertem Mitigationsplan

**Ausnahmeprozess**:

1. Ausnahme mit geschäftlicher Begründung beantragen
2. Risikobewertung der alternativen Methode
3. Kompensierende Kontrollen dokumentieren
4. ISB-Genehmigung für VERTRAULICH und höher erforderlich
5. Zeitlich begrenzte Genehmigung (maximal 90 Tage)

**Nicht zulässig**:

- Übermittlung EINGESCHRÄNKTER Informationen über nicht genehmigte Kanäle
- Grenzüberschreitende Übermittlungen ohne Rechtsgrundlage
- Dauerhafter Einsatz unsicherer Übermittlungsmethoden

Alle Ausnahmen müssen im Ausnahmenregister (ISMS-REG-EXCEPTIONS) erfasst werden.

## Verknüpfung mit Korrekturmassnahmen

Nichtkonformitäten in Bezug auf diese Richtlinie (z. B. nicht genehmigte Übermittlungsmethoden, fehlende Vereinbarungen, Verstösse gegen grenzüberschreitende Übermittlungsregeln) müssen über den ISMS-Korrekturmassnahmenprozess (Klausel 10.2) mit Ursachenanalyse und nachverfolgter Behebung erfasst und verwaltet werden.

---

# Umsetzung & Referenzen

## Integration mit dem ISMS

Diese Richtlinie ist in das Informationssicherheits-Managementsystem von [Organisation] integriert:

**Risikobeurteilung** (ISO 27001 Klausel 6.1):

- Übermittlungskontrollen werden auf Basis der Risikobeurteilung von [Organisation] ausgewählt
- Die Informationsklassifizierung bestimmt die Mindestsicherheitsanforderungen für Übermittlungen
- Risikobehandlungspläne dokumentieren die Umsetzung der Übermittlungskontrollen

**Anwendbarkeitserklärung** (ISO 27001 Klausel 6.1.3):

- Anwendbarkeit der Kontrolle A.5.14 in der SoA von [Organisation] begründet
- Umsetzungsstatus verfolgt und berichtet

**Verwandte Kontrollen**:

- A.5.12-13 (Informationsklassifizierung und -kennzeichnung): Bestimmt Sicherheitsanforderungen für Übermittlungen
- A.5.19-23 (Cloud-Dienste): Anforderungen an cloudbasierte Übermittlungsplattformen
- A.6.6 (Vertraulichkeits- und Geheimhaltungsvereinbarungen): Vereinbarungen für externe Übermittlungen
- A.8.24 (Einsatz von Kryptographie): Verschlüsselungsstandards für Übermittlungen
- A.8.12 (Verhinderung von Datenlecks): DLP-Kontrollen zur Überwachung von Übermittlungen
- A.8.15 (Protokollierung): Anforderungen an die Protokollierung von Übermittlungsaktivitäten

**Gestapelte Kontrollintegration**:

A.5.14 (Informationsübermittlung) wirkt mit verwandten Kontrollen zusammen und bietet umfassenden Schutz:

| Gestapelte Kontrolle | Integrationspunkt | Beitrag von A.5.14 |
|---------------------|-------------------|-------------------|
| **A.5.12-13** (Klassifizierung) | Klassifizierungsbasierte Behandlung | A.5.14 spezifiziert Übermittlungsmethoden je Klassifizierungsstufe |
| **A.8.24** (Kryptographie) | Verschlüsselung bei der Übertragung | A.5.14 schreibt Verschlüsselung vor; A.8.24 spezifiziert Algorithmen |
| **A.8.12** (DLP) | Inhaltsinspektion | A.5.14 definiert Übermittlungskanäle; A.8.12 überwacht auf Richtlinienverstösse |

Die Bewertung von A.5.14 sollte gestapelte Kontrollbewertungen für eine vollständige Abdeckung berücksichtigen.

## Umsetzungsressourcen

**Struktur der Umsetzungsdokumente** (ISMS-IMP-A.5.14 Suite):

| Dokument-ID | Titel | Zweck |
|-------------|-------|-------|
| **ISMS-IMP-A.5.14-UG/TG** | Umsetzungsleitfaden Informationsübermittlung | Detaillierte Verfahren für die sichere Informationsübermittlung |

**Querverweise**:

- ISMS-POL-A.8.24 für kryptographische Anforderungen
- ISMS-POL-A.5.12-13 für Klassifizierungsanforderungen
- ISMS-IMP-A.5.14 für detaillierte Übermittlungsverfahren

---

# Nachweise für diese Richtlinie

**Stufe-1-Nachweise (Dokumentationsprüfung):**

Erforderliche Stufe-1-Nachweise umfassen:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.5.14 v1.0)
- ✅ Dokumentierte Genehmigung durch ISB, ITL, Geschäftsleitung
- ✅ Nachweis der Kommunikation an relevante Rollen
- ✅ Genehmigte Übermittlungsmethoden definiert (Anforderungen an Übermittlungsmethoden)
- ✅ Anforderungen für externe Übermittlungen dokumentiert (Anforderungen an externe Übermittlungen)
- ✅ Anforderungen für grenzüberschreitende Übermittlungen spezifiziert (Grenzüberschreitende Übermittlungen)
- ✅ Autorisierungsmatrix für Übermittlungen definiert (Übermittlungskontrollen)
- ✅ Rollen und Verantwortlichkeiten zugewiesen (Rollen und Verantwortlichkeiten)

Der Nachweisstatus wird im ISMS-Nachweisregister verfolgt.

**Stufe-2-Nachweise (Operative Wirksamkeit):**

Nachweise zum Beleg der operativen Wirksamkeit dieser Richtlinie:

- Übermittlungsprotokolle für VERTRAULICHE/EINGESCHRÄNKTE Übermittlungen
- Muster externer Übermittlungsvereinbarungen (geschwärzt)
- DLP-Vorfallsberichte und Behebungsmassnahmen
- Zugriffsprotokolle der sicheren Dateifreigabeplattform
- Berichte des E-Mail-Sicherheits-Gateways (TLS-Erzwingung)
- Unterlagen zu grenzüberschreitenden Übermittlungen (SCCs, Angemessenheitsbewertungen)
- Schulungsnachweise für Übermittlungsverfahren
- Ausnahmenregister mit Genehmigungen

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Informationsübermittlung** | Die Bewegung von Informationen von einem Ort, System oder einer Person zu einer anderen durch beliebige Mittel |
| **Übermittlungseinrichtung** | Jede Technologie, Ausrüstung oder Dienstleistung zur Übertragung von Informationen (E-Mail-Systeme, Dateifreigabe, Kurier usw.) |
| **Grenzüberschreitende Übermittlung** | Übermittlung von Informationen an einen Empfänger in einem anderen Land/einer anderen Jurisdiktion |
| **Standarddatenschutzklauseln (SCCs)** | Von der EU-Kommission genehmigte Vertragsbedingungen für internationale Datenübermittlungen |
| **Übergabeprotokoll** | Dokumentierter Nachweis aller Personen, die Informationen während der physischen Übermittlung gehandhabt haben |
| **Ende-zu-Ende-Verschlüsselung** | Verschlüsselung, bei der nur Sender und vorgesehener Empfänger die Informationen entschlüsseln können |

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date to be set] |
| **IT-Leiter (ITL)** | [Name] | [Date to be set] |
| **Geschäftsleitung** | [Name] | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen an die Informationsübermittlung fest. Umsetzungsverfahren sind in ISMS-IMP-A.5.14 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.14-DE:framework:POL:a.5.14 -->

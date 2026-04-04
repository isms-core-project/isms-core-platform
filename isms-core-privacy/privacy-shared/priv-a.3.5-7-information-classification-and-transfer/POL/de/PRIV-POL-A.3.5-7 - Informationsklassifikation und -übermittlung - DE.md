<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.5-7-DE:privacy:POL:a.3.5-7 -->
**PRIV-POL-A.3.5-7 — Informationsklassifikation und -übermittlung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Informationsklassifikation und -übermittlung |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | PRIV-POL-A.3.5-7 |
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
- PRIV-IMP-A.3.5-7-UG (Informationsklassifikation und -übermittlung — Benutzerhandbuch)
- PRIV-IMP-A.3.5-7-TG (Informationsklassifikation und -übermittlung — Technisches Handbuch)
- ISMS-POL-A.5.12-13 (Informationsklassifikation und -kennzeichnung — ISMS-Pendant)
- ISMS-POL-A.5.14 (Informationsübermittlung — ISMS-Pendant)
- ISO/IEC 27701:2025 Kontrollen A.3.5, A.3.6, A.3.7
- ISO/IEC 27701:2025 Anhang B (Implementierungsleitfaden B.3.5, B.3.6, B.3.7)
- GDPR Art. 32 (Sicherheit der Verarbeitung); Art. 44–49 (Internationale Übermittlungen)
- CH FADP Art. 7 (Datensicherheit); Art. 16–17 (Grenzüberschreitende Bekanntgabe)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für Informationsklassifikation, -kennzeichnung und -übermittlung im Zusammenhang mit der Verarbeitung personenbezogener Daten (PII) fest — gemäss ISO/IEC 27701:2025 Kontrollen A.3.5, A.3.6 und A.3.7.

**Anwendungsbereich**: Alle Informationen, die PII enthalten oder sich auf PII beziehen; alle auf PII angewandten Klassifikations- und Kennzeichnungsverfahren; alle Übermittlungen von PII innerhalb von [Organisation] und zwischen [Organisation] und anderen Parteien.

**Zweck**: Festlegung organisatorischer Anforderungen für:

- PII-informierte Klassifikation von Informationen (A.3.5)
- Kennzeichnungsverfahren, die den PII-Status erkennen (A.3.6)
- Übermittlungsregeln, -verfahren und -vereinbarungen für die PII-Verarbeitung (A.3.7)

Diese Richtlinie legt fest, **WAS** für Klassifikationskriterien und Übermittlungsregeln für PII gelten, **WER** die Verantwortung für PII-Klassifikations- und Übermittlungsentscheidungen trägt und **WANN** Überprüfungen und Aktualisierungen stattfinden. Implementierungsverfahren (**WIE**) sind in PRIV-IMP-A.3.5-7-UG und PRIV-IMP-A.3.5-7-TG dokumentiert.

**Rollenanwendbarkeit**: Diese Richtlinie gilt für [Organisation] in der Rolle als **PII-Verantwortlicher und PII-Auftragsverarbeiter**. Die Kontrollen A.3.5, A.3.6 und A.3.7 sind gemeinsame Kontrollen (Tabelle A.3) und gelten unabhängig von der Verarbeitungsrolle.

**Begründung für die zusammengefassten Kontrollen**: A.3.5 (Klassifikation), A.3.6 (Kennzeichnung) und A.3.7 (Übermittlung) bilden eine kohärente PII-Datenflusssicherheitstriade. Die Klassifikation informiert die angewandte Kennzeichnung; die Kennzeichnung bestimmt die erforderliche Übermittlungsmethode. Sie werden gemeinsam als integrierte PII-Schutzschicht implementiert, die das ISMS-Klassifikationsrahmenwerk überlagert und erweitert.

---

# Anwendungsbereich und Gültigkeit

## ISO/IEC 27701:2025 Kontrollanforderungen

**Kontrolle A.3.5 — Klassifikation von Informationen**
Kontrolle A.3.5 verlangt von [Organisation], Informationen entsprechend ihrem Informationssicherheitsbedarf zu klassifizieren, wobei PII-Inhalte neben Vertraulichkeit, Integrität, Verfügbarkeit und den Anforderungen relevanter interessierter Parteien zu berücksichtigen sind.

**Kontrolle A.3.6 — Kennzeichnung von Informationen**
Kontrolle A.3.6 verlangt von [Organisation], Informationskennzeichnungsverfahren zu entwickeln und zu implementieren, die PII erkennen und mit dem Klassifikationsschema der Organisation konsistent sind.

**Kontrolle A.3.7 — Informationsübermittlung**
Kontrolle A.3.7 verlangt von [Organisation], Regeln, Verfahren und Vereinbarungen für die Übermittlung von PII über alle Arten von Übermittlungskanälen vorzuhalten, sowohl innerhalb als auch ausserhalb der Organisation.

## Was diese Richtlinie abdeckt

**Informationen**:

- Alle Datensätze, Aufzeichnungen, Dateien, Datenbanken und Mitteilungen mit PII-Inhalt
- Aggregierte Datensätze, aus denen PII abgeleitet oder erschlossen werden kann, auch wenn kein einzelnes Feld direkt identifizierend ist
- Informationen mit besonderer Kategorie von PII (Gesundheit, Biometrie, ethnische Herkunft, religiöse Überzeugung usw.)
- Informationen über betroffene Personen in jeglichem Format (elektronisch, physisch, mündlich)

**Klassifikation**:

- Das auf PII-haltige Informationen angewandte Klassifikationsschema, einschliesslich PII-spezifischer Klassifikationskriterien, die das ISMS-Klassifikationsschema erweitern
- Mindestklassifikationsstufen für definierte PII-Kategorien
- Aggregationsregeln, bei denen kombinierte Daten die Klassifikation erhöhen

**Kennzeichnung**:

- Kennzeichnungsarten und -formate, die PII-haltige Informationen identifizieren
- Kennzeichnungsanforderungen spezifisch für PII-Sensibilität und -Kategorie
- Kennzeichnungspflichten für Systeme und Repositories, die PII verarbeiten

**Übermittlung**:

- Jede Bewegung von PII innerhalb von [Organisation] (System zu System, Team zu Team, Verarbeitungsumgebung zu Verarbeitungsumgebung)
- Jede Übermittlung von PII an externe Parteien (PII-Auftragsverarbeiter, gemeinsam Verantwortliche, Empfänger, Behörden)
- Grenzüberschreitende und internationale Übermittlung von PII, einschliesslich Cloud-Verarbeitung in anderen Jurisdiktionen

## Was diese Richtlinie NICHT abdeckt

- Klassifikationskennzeichnungsvorlagen, Tools und Konfigurationsverfahren (siehe PRIV-IMP-A.3.5-7-TG)
- Übermittlungsplattformkonfigurationen und Einrichtung sicherer Kanäle (siehe PRIV-IMP-A.3.5-7-TG)
- Verfahren zu Betroffenenrechten für PII-Zugang und Datenübertragbarkeit (siehe PRIV-POL-A.1.3.5-10 und PRIV-POL-A.1.4.6-10)
- Auftragsverarbeitungsvereinbarungen und Sorgfaltsprüfungsverfahren (siehe PRIV-POL-A.2.2.2-7)
- Incident Response bei PII-Übermittlungsverletzungen (siehe PRIV-POL-A.3.11-12)
- ISMS-weite Klassifikations- und Übermittlungsanforderungen (siehe ISMS-POL-A.5.12-13 und ISMS-POL-A.5.14)

## Regulatorischer Rahmen

**Tier 1: Obligatorische Compliance** (gemäss PRIV-POL-00):

- **EU GDPR**: Art. 32 (angemessene Sicherheit der Verarbeitung, einschliesslich Schutz bei der Übermittlung); Art. 44–49 (Garantien für internationale Übermittlungen — SCCs, Angemessenheitsbeschlüsse, BCRs); Art. 5(1)(f) (Grundsatz der Integrität und Vertraulichkeit)
- **CH FADP**: Art. 7 (technische und organisatorische Massnahmen proportional zur Sensibilität); Art. 16–17 (grenzüberschreitende Bekanntgabe — Äquivalenz, Standarddatenschutzklauseln)
- **ISO/IEC 27701:2025**: Kontrollen A.3.5, A.3.6, A.3.7 (normativ)

**Tier 2: Bedingte Anwendbarkeit** (gemäss PRIV-POL-00):

- **ISO/IEC 27018:2025**: Anhang A — Anforderungen an Cloud-PII-Übermittlungen, sofern öffentliche Cloud-Verarbeitung im Anwendungsbereich

**Tier 3: Informative Referenz** (gemäss PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementierungsleitfaden für Klassifikation (5.12–5.13) und Übermittlung (5.14)
- **ISO/IEC 27701:2025 Anhang B**: Implementierungsleitfaden B.3.5 (Klassifikation mit PII), B.3.6 (PII-bewusste Kennzeichnung), B.3.7 (PII-Übermittlungsregeln)

Für eine vollständige regulatorische Kategorisierung siehe PRIV-POL-00.

---

# Richtlinienanforderungen: PII-informierte Klassifikation von Informationen (A.3.5)

## Erweiterung des Klassifikationsschemas für PII

Das Informationsklassifikationsschema von [Organisation] (gemäss ISMS-POL-A.5.12-13) **muss** auf alle Informationen angewandt werden. Für Informationen, die PII enthalten oder sich auf PII beziehen, legt diese Richtlinie PII-spezifische Kriterien fest, die das ISMS-Klassifikationsschema erweitern und ergänzen.

### PII-Mindestklassifikationsstufen

Folgende Mindestklassifikationsstufen **müssen** für PII-haltige Informationen gelten, unabhängig von anderen Klassifikationskriterien:

| PII-Kategorie | Mindestklassifikation |
|--------------|----------------------|
| **Gewöhnliche Personendaten** (Name, Adresse, Kontaktangaben, Beschäftigungsakte) | VERTRAULICH |
| **Finanzielle Personendaten** (Bankkonten, Zahlungsaufzeichnungen, Gehalt, Kreditinformationen) | VERTRAULICH |
| **Besondere Kategorien von PII** (Gesundheit/Medizin, Biometrie, Genetik, ethnische Herkunft, religiöse Überzeugung, politische Meinung, Sexualleben/-orientierung, Gewerkschaftszugehörigkeit) | EINGESCHRÄNKT |
| **Sensible Personendaten** (Kinderdaten, Strafregisterauszüge, nationale Identifikationsnummern) | EINGESCHRÄNKT |
| **Authentifizierungsdaten** (Passwörter, Token, kryptografische Schlüssel mit Bezug zu individuellen Identitäten) | EINGESCHRÄNKT — aus Gründen der operativen Praktikabilität aufgeführt, da sie häufig gemeinsam mit PII in Identitätsdatensätzen vorkommen; auf Informationssicherheitsgrundlage gemäss ISMS-POL-A.5.12-13 als EINGESCHRÄNKT klassifiziert |
| **PII von Hochrisiko-Personen** (schutzbedürftige Personen, Hinweisgeber, betroffene Personen unter Schutzmassnahmen) | EINGESCHRÄNKT |

### PII-Aggregationsregel

Wenn Informationen, die einzeln unterhalb von VERTRAULICH klassifiziert sind, so kombiniert werden, dass PII abgeleitet, identifiziert oder erschlossen werden kann, **muss** der aggregierte Datensatz mindestens als VERTRAULICH klassifiziert werden. Wenn der aggregierte Datensatz besondere Kategorien von PII enthält oder deren Ableitung ermöglicht, **muss** er als EINGESCHRÄNKT klassifiziert werden.

Der Data Owner (oder DSB, wenn kein Data Owner zugewiesen ist) **muss** die Aggregationsklassifikationsentscheidung treffen und im Klassifikationsregister dokumentieren. Der DSB ist Eigentümer des Klassifikationsregisters.

### Klassifikationsbefugnis für PII

| Klassifikationsstufe | Befugnis zur Klassifikation | Befugnis zur Deklassifikation |
|---------------------|-----------------------------|------------------------------|
| VERTRAULICH (gewöhnliche PII) | Data Owner, DSB | Data Owner mit DSB-Benachrichtigung |
| EINGESCHRÄNKT (besondere Kategorien von PII) | Data Owner mit DSB-Genehmigung | Data Owner mit DSB- und Geschäftsleitungsgenehmigung |
| EINGESCHRÄNKT (Hochrisiko-PII) | DSB mit Geschäftsleitungsgenehmigung | DSB mit Geschäftsleitungsgenehmigung |

### Klassifikationsüberprüfung für PII

Zusätzlich zu den Überprüfungsauslösern in ISMS-POL-A.5.12-13 **muss** die PII-Klassifikation überprüft werden:

- Wenn sich der Verarbeitungszweck ändert, sodass andere PII-Kategorien betroffen sind
- Wenn sich die Rechtsgrundlage der Verarbeitung ändert und die Sensibilitätsstufe beeinflusst
- Nach einer DPIA, die eine Umklassifizierungsanforderung identifiziert
- Bei Benachrichtigung durch eine Datenschutzbehörde oder Aufsichtsbehörde
- Wenn neue Leitlinien oder Rechtsprechung die Auslegung einer PII-Kategorie wesentlich ändern

---

# Richtlinienanforderungen: PII-bewusste Kennzeichnung von Informationen (A.3.6)

## Kennzeichnungsanforderungen für PII

[Organisation] **muss** Kennzeichnungsverfahren entwickeln und implementieren, die PII-haltige Informationen als solche identifizieren. PII-Kennzeichnungsverfahren **müssen** mit dem ISMS-Kennzeichnungsschema (ISMS-POL-A.5.12-13) konsistent sein und dieses erweitern.

### Obligatorische PII-Kennzeichnung

Alle auf Basis von PII-Inhalt als VERTRAULICH oder EINGESCHRÄNKT klassifizierten Informationen **müssen** enthalten:

1. Die anwendbare Klassifikationskennzeichnung (VERTRAULICH oder EINGESCHRÄNKT) gemäss ISMS-Kennzeichnungsstandards
2. Einen PII-Indikator, der anzeigt, dass die Information personenbezogene Daten enthält

**PII-Indikatorformate** (detailliert definiert in PRIV-IMP-A.3.5-7-TG):

| Format | PII-Indikator |
|--------|--------------|
| Elektronische Dokumente | Vermerk "Enthält Personendaten" in Kopf-/Fusszeile oder Dokumenteigenschaften |
| Physische Dokumente | Stempel "PERSONENDATEN" oder gedruckter Indikator auf Deckblatt und erster Seite |
| Datenbanken und Datenspeicher | Klassifikations-Metadatenfeld: `pii_present = true`; PII-Kategoriefeld ausgefüllt |
| E-Mail | Präfix im Betreff, wo Inhalt PII enthält: `[PD]` oder `[SPD]` für besondere Kategorien |
| Datei-/Ordnerbenennung | Suffix `_PII` oder `_SPD` wo praktikabel und konsistent mit Systemfähigkeiten |

### Kennzeichnung besonderer Kategorien von PII

Informationen mit besonderen Kategorien von PII **müssen** zusätzlich einen Spezialkatgorieindikator tragen, um eine erhöhte Handhabung zu ermöglichen. Das spezifische Format dieses Indikators ist in PRIV-IMP-A.3.5-7-TG definiert.

### System- und Repository-Kennzeichnung

Repositories, Datenbanken, Systeme und Verarbeitungsumgebungen, die PII speichern oder verarbeiten, **müssen** auf Systemebene gekennzeichnet sein mit:

- Ob PII vorhanden ist (ja/nein)
- Verarbeitete PII-Kategorien (gewöhnlich, finanziell, besondere Kategorien oder Liste anwendbarer Kategorien)
- Anwendbarer jurisdiktionaler Umfang (z.B. Betroffene im EU/EWR, Betroffene in der CH)

Die Kennzeichnung auf Systemebene wird im Datenanlagenregister geführt (Registerstruktur siehe PRIV-IMP-A.3.5-7-TG).

### Pflicht zur Kennzeichnungskonsistenz

Wenn die ISMS-Klassifikationskennzeichnung und die PII-Kennzeichnungsanforderung in Konflikt stehen (z.B. ein Asset nach ISMS-Kriterien als INTERN klassifiziert ist, aber gewöhnliche PII enthält, die VERTRAULICH erfordert), **muss** die höhere Klassifikation gelten und der PII-Mindestboden **muss** angewandt werden.

---

# Richtlinienanforderungen: PII-Übermittlungsregeln und -vereinbarungen (A.3.7)

## Übermittlungsanforderungen für PII

[Organisation] **muss** Regeln, Verfahren und Vereinbarungen erstellen und aufrechterhalten, die alle Übermittlungen von PII über alle Arten von Übermittlungskanälen abdecken, ob intern oder extern, elektronisch oder physisch.

### Interne PII-Übermittlung

**Innerhalb von [Organisation]**:

- PII **darf** nur an organisatorische Rollen und Mitarbeitende mit einem legitimen Verarbeitungszweck und entsprechender Zugangsberechtigung übermittelt werden
- Interne Übermittlungen von EINGESCHRÄNKTER PII (besondere Kategorien) **müssen** protokolliert und nachverfolgbar sein
- System-zu-System-PII-Übermittlungen **müssen** verschlüsselte Kanäle verwenden; Übermittlungskonfigurationen sind in PRIV-IMP-A.3.5-7-TG dokumentiert
- Interne Übermittlungen von PII in Verarbeitungsumgebungen in anderen Jurisdiktionen **müssen** für regulatorische Compliance-Zwecke als grenzüberschreitende Übermittlungen behandelt werden

### Externe PII-Übermittlung

**An PII-Auftragsverarbeiter (Lieferanten und Dienstleister)**:

Externe Übermittlungen von PII an Auftragsverarbeiter erfordern eine aktuelle und gültige Auftragsverarbeitungsvereinbarung (GDPR Art. 28; CH FADP Art. 9), die vor Beginn der Übermittlung vorliegen muss. Keine PII-Übermittlung an einen externen Auftragsverarbeiter ohne unterzeichnete Auftragsverarbeitungsvereinbarung. Der DSB führt das Auftragsverarbeitungsvereinbarungsregister.

**An gemeinsam Verantwortliche**:

Externe Übermittlungen von PII an gemeinsam Verantwortliche erfordern eine Vereinbarung für gemeinsame Verantwortliche (GDPR Art. 26), die die jeweiligen Zuständigkeiten dokumentiert. Der DSB muss Vereinbarungen für gemeinsam Verantwortliche genehmigen, bevor PII übermittelt wird.

**An Empfänger und Dritte**:

Externe Übermittlungen von PII an Empfänger, die keine Auftragsverarbeiter oder gemeinsam Verantwortlichen sind (einschliesslich Behörden, Rechtsberater, Prüfer und andere), erfordern:

- Eine dokumentierte Rechtsgrundlage für die Offenlegung gemäss GDPR Art. 6 (und Art. 9 für besondere Kategorien)
- DSB-Prüfung, wenn die Offenlegung nicht routinemässig ist
- Eine Aufzeichnung der Übermittlung im Verzeichnis der Verarbeitungstätigkeiten (VVT)

### Grenzüberschreitende und internationale PII-Übermittlung

Übermittlungen von PII in Länder oder internationale Organisationen ausserhalb des EWR (für GDPR) oder ausserhalb der Schweiz (für CH FADP) unterliegen folgenden Anforderungen:

**Rechtsgrundlage für die Übermittlung**:

| Mechanismus | Anwendbarkeit |
|-------------|--------------|
| Angemessenheitsbeschluss (EU-Kommission / Schweizer EDÖB) | Übermittlungen in Länder mit anerkanntem angemessenem Schutz — keine zusätzlichen Massnahmen erforderlich |
| Standardvertragsklauseln (SCCs) | Übermittlungen in Länder ohne Angemessenheit — EU SCCs (2021) oder Schweizer SCCs entsprechend |
| Verbindliche interne Datenschutzvorschriften (BCRs) | Konzerninterne Übermittlungen, sofern BCRs von zuständiger Datenschutzbehörde genehmigt — erfordert Datenschutzbehördengenehmigung und gilt nur für Konzerngruppen, die den BCR-Genehmigungsprozess durchlaufen haben; dieser Mechanismus ist der Vollständigkeit halber aufgeführt; seine Verfügbarkeit für [Organisation] hängt von der Konzernstruktur ab |
| Art. 49-Ausnahmen | Nur ausnahmsweise (Einwilligung der betroffenen Person, lebenswichtige Interessen, wichtiges öffentliches Interesse, Rechtsansprüche) — nicht für systematische Übermittlungen |

**Transfer Impact Assessment (TIA)**:

Wenn SCCs oder andere vertragliche Mechanismen verwendet werden, **muss** [Organisation] ein TIA durchführen, um zu beurteilen, ob das Rechtssystem des Ziellandes einen im Wesentlichen gleichwertigen Schutz bietet. Das TIA, die Entscheidung über ergänzende Massnahmen und die DSB-Genehmigung **müssen** im internationalen Übermittlungsregister dokumentiert werden.

**Verbotene Zielländer**:

- Länder, die internationalen Sanktionen unterliegen, wenn die Übermittlung rechtswidrig wäre
- Jurisdiktionen, in denen kein angemessener Rechtsmechanismus verfügbar ist und keine Ausnahme gilt

### Übermittlungsmethoden für PII

Die Anforderungen an die PII-Übermittlungsmethode werden durch die Klassifikationsstufe bestimmt, konsistent mit ISMS-POL-A.5.14 und wie folgt erweitert:

| Übermittlungsart | VERTRAULICHE PII | EINGESCHRÄNKTE / Besondere Kategorien von PII |
|-----------------|------------------|--------------------------------------------|
| **Elektronisch — intern** | Verschlüsselter Kanal (TLS mindestens) | Verschlüsselter Kanal + Protokolleintrag |
| **Elektronisch — extern** | Verschlüsselte E-Mail oder sichere Dateiübertragungsplattform | Ende-zu-Ende-verschlüsselte Plattform; Empfängeridentitätsverifizierung erforderlich |
| **Physisch — Dokumente** | Versiegelter Umschlag, Sendungsverfolgung, Empfängerunterschrift | Doppelt versiegelt, Kurier mit Sicherheitsüberprüfung, Übergabedokumentation |
| **Physisch — Medien** | Verschlüsselte Medien, Sendungsverfolgung | Verschlüsselte Medien, Sicherheitskurier, Lieferbestätigung |
| **Cloud — Verarbeitung** | Verschlüsselt im Ruhezustand und im Transit; Datenspeicherort verifiziert | Verschlüsselt im Ruhezustand und im Transit; Datenspeicherort bestätigt; Auftragsverarbeiter mit Datenschutzbehördengenehmigung |

### Übermittlungsvereinbarungen

Alle externen Übermittlungen von PII im Rahmen laufender Beziehungen **müssen** durch eine schriftliche Vereinbarung geregelt sein, die mindestens Folgendes abdeckt:

- Zwecke, für die der Empfänger die PII verwenden darf
- Aufbewahrungsfristen und Löschungs-/Rückgabepflichten
- Sicherheitsmassnahmen, die der Empfänger aufrechterhalten muss
- Beschränkungen zur Beauftragung von Unterauftragsverarbeitern (für Auftragsverarbeitungsbeziehungen)
- Verletzungsmeldungspflichten und -fristen
- Prüfungsrechte (sofern anwendbar)
- Anwendbares Recht und Gerichtsstand

Der DSB führt das Übermittlungsvereinbarungsregister. Keine laufende externe PII-Übermittlung darf ohne eine aktuelle Vereinbarung im Register aufgenommen werden.

---

# Rollen und Verantwortlichkeiten

## Verantwortungsmatrix

| Rolle | Verantwortlichkeiten für A.3.5–A.3.7 |
|-------|--------------------------------------|
| **Datenschutzbeauftragter (DSB)** | Primäre Instanz für PII-Mindestklassifikationsstufen und Übermittlungsregeln; genehmigt grenzüberschreitende Übermittlungsmechanismen; führt internationales Übermittlungsregister und Übermittlungsvereinbarungsregister; überprüft Aggregationsklassifikationsentscheidungen |
| **Data Owner** | Klassifiziert PII-Datensätze in seinem Bereich; wendet PII-Kennzeichnungen an; genehmigt interne Übermittlungen; eskaliert grenzüberschreitende Übermittlungen an DSB |
| **ISB** | Stellt sicher, dass das ISMS-Klassifikationsschema konsistent auf PII gemäss dieser Richtlinie erweitert wird; stellt sicher, dass Übermittlungskontrollen (Verschlüsselung, Protokollierung) für PII implementiert sind; koordiniert mit DSB zu technischen Übermittlungskontrollen |
| **IT-Sicherheitsteam / System-Owner** | Implementiert PII-Kennzeichnung auf Systemebene; konfiguriert verschlüsselte Übermittlungskanäle; pflegt Systemklassifikations-Metadaten; stellt Prüfprotokolle für PII-Übermittlungen bereit |
| **Privacy Champions** | Erstlinie Unterstützung für PII-Klassifikationsfragen; eskaliert Umklassifizierungsauslöser an Data Owner und DSB |
| **Legal/Compliance** | Berät zu grenzüberschreitenden Übermittlungsmechanismen; überprüft SCCs und DPA-Angemessenheitsbeschlüsse; unterstützt TIA-Dokumentation |
| **Alle Mitarbeitenden** | Wenden Klassifikation und Kennzeichnung auf in ihrer Rolle bearbeitete PII an; verwenden nur genehmigte Übermittlungsmethoden für PII; melden vermutete Fehlklassifikationen oder unautorisierten Übermittlungen |

---

# Nachweisanforderungen

Folgende Nachweise belegen den Betrieb dieser Richtlinie:

| Nachweis | Beschreibung | Aufbewahrung |
|---------|-------------|--------------|
| Klassifikationsregister | Aufzeichnung der PII-Datensatzklassifikationen, einschliesslich Aggregationsentscheidungen und Klassifikationsbefugnis | 3 Jahre ab dem Datum, an dem die Klassifikation abgelöst oder der Datensatz entsorgt wurde |
| Datenanlagenregister | PII-Kennzeichnungsaufzeichnungen auf Systemebene (pii_present, pii_categories, jurisdiktionaler Umfang) | Aktuell + 3 Jahre |
| Internationales Übermittlungsregister | TIA-Aufzeichnungen, SCCs, Verweise auf Angemessenheitsbeschlüsse, DSB-Genehmigungen für grenzüberschreitende PII-Übermittlungen | Dauer der Übermittlungsaktivität + 3 Jahre |
| Übermittlungsvereinbarungsregister | Unterzeichnete Auftragsverarbeitungsvereinbarungen, Vereinbarungen für gemeinsam Verantwortliche, Empfängervereinbarungen | Vertragsdauer + 3 Jahre |
| Interne Übermittlungsprotokolle | Protokolle interner EINGESCHRÄNKTER PII-Übermittlungen, einschliesslich Zweck und Genehmigung | 3 Jahre ab Übermittlungsdatum |
| Klassifikationsüberprüfungsaufzeichnungen | Nachweis der periodischen Klassifikationsüberprüfung und anlassbezogener Überprüfungen | 3 Jahre ab Überprüfungsdatum |

---

# Prüfungshinweise

Prüfer, die die Compliance mit A.3.5, A.3.6 und A.3.7 verifizieren, sollten Folgendes vorfinden:

**Für A.3.5 (Klassifikation)**:
- Klassifikationsschema-Dokumentation mit PII-Mindestklassifikationsstufen
- Nachweis, dass PII-Datensätze auf oder über der geforderten Mindestklassifikation eingestuft sind
- Aggregationsklassifikationsentscheidungen für relevante kombinierte Datensätze
- Klassifikationsüberprüfungsaufzeichnungen in geplanten Abständen oder bei Auslöseereignissen

**Für A.3.6 (Kennzeichnung)**:
- Kennzeichnungsverfahren für PII-haltige Informationen in allen Formaten
- Exemplarisch gekennzeichnete Dokumente und Systemmetadaten mit PII-Indikatorfeldern
- Datenanlagenregister mit ausgefüllten PII-Feldern für Systeme im Anwendungsbereich
- Nachweis, dass VERTRAULICH/EINGESCHRÄNKT-Klassifikation und PII-Indikator konsistent zusammen angewandt werden

**Für A.3.7 (Übermittlung)**:
- Übermittlungsregeln und -verfahren für interne und externe PII-Übermittlungen
- Unterzeichnete Auftragsverarbeitungsvereinbarungen für alle aktiven Auftragsverarbeitungsbeziehungen
- Internationales Übermittlungsregister mit TIA-Dokumentation für grenzüberschreitende Übermittlungen
- Nachweis angemessener Übermittlungsmechanismen (SCCs, Angemessenheitsbeschlüsse) für internationale Übermittlungen
- Übermittlungsprotokolle für EINGESCHRÄNKTE PII-Übermittlungen

---

<!-- QA_VERIFIED: 2026-03-29 -->

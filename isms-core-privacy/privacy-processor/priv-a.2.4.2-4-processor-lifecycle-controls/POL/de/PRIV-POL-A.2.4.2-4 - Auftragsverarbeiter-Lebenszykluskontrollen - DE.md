<!-- ISMS-CORE:POLICY:PRIV-POL-A.2.4.2-4-DE:privacy:POL:a.2.4.2-4 -->
**PRIV-POL-A.2.4.2-4 — Auftragsverarbeiter-Lebenszykluskontrollen**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Auftragsverarbeiter-Lebenszykluskontrollen |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | PRIV-POL-A.2.4.2-4 |
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
- Letztentscheidung: Geschäftsleitung

**Zugehörige Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- PRIV-POL-01 (Datenschutz-Governance und Entscheidungsrahmen)
- PRIV-IMP-A.2.4.2-4-UG (Auftragsverarbeiter-Lebenszykluskontrollen — Benutzerhandbuch)
- PRIV-IMP-A.2.4.2-4-TG (Auftragsverarbeiter-Lebenszykluskontrollen — Technisches Handbuch)
- PRIV-POL-A.2.2.2-7 (Auftragsverarbeiter-Vereinbarungen — grundlegende Auftragsverarbeiter-Richtlinie)
- PRIV-POL-A.1.4.6-10 (PII-Lebenszyklus des Verantwortlichen — das verantwortlicherseitige Gegenstück für temporäre Dateien und Aufbewahrung)
- PRIV-POL-A.3.5-7 (Informationsklassifikation und -übermittlung — Übertragungsregeln)
- ISO/IEC 27701:2025 Kontrollen A.2.4.2, A.2.4.3, A.2.4.4
- ISO/IEC 27701:2025 Anhang B (Implementierungsleitfaden B.2.4.2 bis B.2.4.4)
- GDPR Art. 28(3)(g) (Rückgabe oder Löschung bei Vertragsende); Art. 32(1)(a) (Verschlüsselung und Übertragungssicherheit)
- CH FADP Art. 9 (Sicherheitsmassnahmen equivalent zu Verantwortlichen-Anforderungen)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] in der Rolle als PII-Auftragsverarbeiter für die Entsorgung temporärer Dateien, die sichere Rückgabe/Übertragung/Vernichtung von Kunden-PII bei Vertragsende und Übertragungskontrollen für PII fest — gemäss ISO/IEC 27701:2025 Kontrollen A.2.4.2, A.2.4.3 und A.2.4.4.

**Anwendungsbereich**: Alle bei der Verarbeitung von Kunden-PII erzeugten temporären Dateien; alle Behandlungen von Kunden-PII bei Vertragsende; alle Übertragungen von PII über Datennetzwerke im Kundenauftrag.

**Rollenanwendbarkeit**: Diese Richtlinie gilt für [Organisation] ausschliesslich in der Rolle als **PII-Auftragsverarbeiter**. Die Kontrollen A.2.4.2–A.2.4.4 sind auftragsverarbeiterspezifisch (Tabelle A.2).

---

# Anwendungsbereich und Gültigkeit

## ISO/IEC 27701:2025 Kontrollanforderungen

**Kontrolle A.2.4.2 — Temporäre Dateien**
Kontrolle A.2.4.2 verlangt von [Organisation] sicherzustellen, dass bei der PII-Verarbeitung erzeugte temporäre Dateien innerhalb eines definierten, dokumentierten Zeitraums nach dokumentierten Verfahren entsorgt werden.

**Kontrolle A.2.4.3 — Rückgabe, Übertragung oder Entsorgung von PII**
Kontrolle A.2.4.3 verlangt von [Organisation], in der Lage zu sein, Kunden-PII zurückzugeben, zu übertragen oder sicher zu entsorgen, und seine Rückgabe-/Entsorgungsrichtlinie Kunden zugänglich zu machen.

**Kontrolle A.2.4.4 — PII-Übertragungskontrollen**
Kontrolle A.2.4.4 verlangt von [Organisation], auf im Kundenauftrag über Datennetzwerke übertragene PII geeignete Kontrollen anzuwenden, um sicherzustellen, dass Daten ihren beabsichtigten Empfänger erreichen.

## Regulatorischer Rahmen

**Tier 1: Obligatorische Compliance** (gemäss PRIV-POL-00):

- **EU GDPR**: Art. 28(3)(g) (Auftragsverarbeiter löscht oder gibt PII bei Vertragsende zurück und löscht Kopien, sofern nicht rechtlich erforderlich); Art. 32(1)(a) (Pseudonymisierung, Verschlüsselung und Übertragungssicherheit)
- **CH FADP**: Art. 9 (Sicherheitsmassnahmen equivalent zu Verantwortlichen-Anforderungen)
- **ISO/IEC 27701:2025**: Kontrollen A.2.4.2–A.2.4.4 (normativ)

---

# Richtlinienanforderungen

## A.2.4.2 — Temporäre Dateien (Auftragsverarbeiter)

[Organisation] **muss** sicherstellen, dass infolge der PII-Verarbeitung im Kundenauftrag erzeugte temporäre Dateien innerhalb dokumentierter, festgelegter Zeiträume entsorgt werden.

Entsorgungsanforderungen für temporäre Dateien bei Auftragsverarbeitungsaktivitäten sind konsistent mit der allgemeinen Richtlinie für temporäre Dateien in PRIV-POL-A.1.4.6-10 (A.1.4.7), angewandt auf Kunden-PII-Kontexte:

- Verarbeitungs-Cache- und Staging-Dateien: innerhalb von 48 Stunden nach Verarbeitungsabschluss entsorgt
- Fehler-/Ausnahmeprotokolle mit Kunden-PII: innerhalb von 30 Tagen entsorgt (automatisierte Rotation)
- Für Kundenlieferung erzeugte Exportdateien: innerhalb von 72 Stunden nach bestätigter Lieferung an den Kunden entsorgt

Spezifische Zeiträume sind in PRIV-IMP-A.2.4.2-4-TG dokumentiert. Automatisierte Löschmechanismen werden bevorzugt.

---

## A.2.4.3 — Rückgabe, Übertragung oder Entsorgung von Kunden-PII

Wenn ein Kundenvertrag endet oder ein Kunde die Rückgabe oder Löschung seiner PII beantragt, **muss** [Organisation] in der Lage sein:

- Die PII in einem strukturierten, vereinbarten Format an den **Kunden zurückzugeben**
- Die PII an einen vom Kunden bezeichneten anderen Auftragsverarbeiter zu **übertragen**
- Die PII mithilfe genehmigter Löschverfahren sicher zu **entsorgen**

[Organisation] **muss** zwischen diesen Optionen gemäss der dokumentierten Kundenanweisung wählen. Fehlt bei Vertragsende eine spezifische Kundenanweisung, **muss** [Organisation] Weisungen anfordern und dem im Auftragsverarbeitungsvertrag festgelegten Standard folgen.

### Entsorgungsstandards

Die PII-Entsorgung bei Vertragsende folgt den in PRIV-POL-A.1.4.6-10 (A.1.4.9) definierten Methoden:

- Datenbankeinträge: SQL DELETE oder Äquivalent; oder kryptografische Löschung für verschlüsselte Speicher
- Dateisystem: kryptografische Löschung oder genehmigter Überschreibungsstandard
- Backup-Medien: abgestimmt auf den Backup-Aufbewahrungsplan; abgelaufene Backups werden planmässig gelöscht; oder ausserplanmässige Löschung auf Kundenanweisung mit Bestätigung. Wenn der nächste geplante Backup-Ablauf nicht innerhalb des vom Kunden geforderten Löschfensters eintritt, **muss** [Organisation] sofort den Zugriff auf die PII dieses Kunden enthaltende Backups als Zwischenmassnahme isolieren und einschränken, bis zur physischen Löschung beim nächsten Ablauf

Die Entsorgung **muss** dem Kunden schriftlich innerhalb der im Auftragsverarbeitungsvertrag festgelegten Frist bestätigt werden; der organisatorische Standard ist innerhalb von 30 Tagen nach Vertragsende, sofern die Vereinbarung nichts anderes vorsieht.

**Standard bei Vertragsende**: Wenn keine Kundenanweisung eingeht und der Auftragsverarbeitungsvertrag keinen Standard vorsieht, **muss** [Organisation] innerhalb von 5 Werktagen nach Vertragsende beim Kunden Weisungen anfordern. Wenn innerhalb von 30 Tagen nach dieser Benachrichtigung keine Antwort eingeht, wird [Organisation] alle Kunden-PII sicher löschen und die Löschung dem Kunden schriftlich bestätigen.

### Richtlinienverfügbarkeit

[Organisation] **muss** seine Rückgabe-, Übertragungs- und Entsorgungsrichtlinie Kunden auf Anfrage und, sofern vertraglich erforderlich, als Teil der Auftragsverarbeitungsvereinbarungs-Dokumentation zugänglich machen.

---

## A.2.4.4 — PII-Übertragungskontrollen (Auftragsverarbeiter)

[Organisation] **muss** im Kundenauftrag über Datennetzwerke übertragene PII geeigneten Kontrollen unterziehen, um sicherzustellen, dass sie ihren beabsichtigten Empfänger erreicht.

Übertragungskontrollen sind konsistent mit PRIV-POL-A.3.5-7 (Übertragungsregeln) und PRIV-POL-A.3.23-31 (kryptografische Kontrollen):

- Alle über Netzwerke übertragene PII **muss** im Transit verschlüsselt sein (mindestens TLS 1.2; TLS 1.3 bevorzugt)
- VERTRAULICHE und EINGESCHRÄNKTE PII-Übertragungen **müssen** genehmigte sichere Übertragungsmethoden verwenden
- Lieferbestätigungen oder Empfangsquittierungen **müssen** für EINGESCHRÄNKTE PII-Übertragungen an Dritte eingeholt werden
- Übertragungsprotokolle für über Netzwerke transportierte PII werden gemäss PRIV-POL-A.3.25 (Protokollierung) geführt

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Datenschutzbeauftragter (DSB)** | Verwaltet PII-Rückgabe-/Entsorgungsprozess bei Vertragsende; bestätigt Abschluss an Kunden; führt Entsorgungsaufzeichnungen |
| **ISB / IT-Sicherheitsteam** | Implementiert temporäre Dateilöschmechanismen; führt Entsorgungen durch; konfiguriert TLS-Durchsetzung; liefert Entsorgungsbestätigungen |
| **Customer Success** | Koordiniert mit Kunden bei der bevorzugten Rückgabe-/Entsorgungsoption bei Vertragsende; verfolgt Entsorgungsabschluss |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrung |
|---------|-------------|--------------|
| Temporäre Dateilöschaufzeichnungen | Automatisierte/manuelle Löschbestätigungen für temporäre Kunden-PII-Dateien | 3 Jahre ab Löschdatum |
| Vertragsende-Entsorgungsaufzeichnungen | Schriftliche Bestätigung der PII-Rückgabe/-Übertragung/-Entsorgung pro Kunde | 5 Jahre |
| Kunden-PII-Entsorgungsbestätigung | Schriftliche Bestätigung an Kunden bei Vertragsende | 5 Jahre |
| Übertragungsverschlüsselungskonfiguration | TLS-Konfigurationsaufzeichnungen für Kunden-PII-Übertragung | Aktuell + 3 Jahre |

---

# Prüfungshinweise

- Temporäre Dateientsorgungsfristen dokumentiert und automatisierte Mechanismen vorhanden
- Vertragsende-PII-Behandlung: Nachweis der Rückgabe, Übertragung oder Entsorgung gemäss Kundenanweisung
- Schriftliche Entsorgungsbestätigung innerhalb der vertraglichen Frist an Kunden bereitgestellt
- TLS-Durchsetzung für PII-Übertragung (Konfigurationsnachweis)
- Rückgabe-/Entsorgungsrichtlinie für Kunden verfügbar

---

<!-- QA_VERIFIED: 2026-03-29 -->

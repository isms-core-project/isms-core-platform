<!-- ISMS-CORE:POLICY:PRIV-POL-A.1.3.11-DE:privacy:POL:a.1.3.11 -->
**PRIV-POL-A.1.3.11 — Automatisierte Entscheidungsfindung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Automatisierte Entscheidungsfindung |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | PRIV-POL-A.1.3.11 |
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
- Sekundär: Legal/Compliance Officer
- Letztentscheidung: Geschäftsleitung

**Zugehörige Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- PRIV-POL-01 (Datenschutz-Governance und Entscheidungsrahmen)
- PRIV-IMP-A.1.3.11-UG (Automatisierte Entscheidungsfindung — Benutzerhandbuch)
- PRIV-IMP-A.1.3.11-TG (Automatisierte Entscheidungsfindung — Technisches Handbuch)
- PRIV-POL-A.1.3.5-10 (Betroffenenrechte — Schwesterrichtlinie: Recht auf menschliche Überprüfung)
- PRIV-POL-A.1.3.2-4 (Transparenz — Schwesterrichtlinie: Transparenzpflicht bei AEF)
- ISO/IEC 27701:2025 Kontrolle A.1.3.11
- ISO/IEC 27701:2025 Anhang B (Implementierungsleitfaden B.1.3.11)
- GDPR Art. 22 (Automatisierte Einzelentscheidungen einschliesslich Profilerstellung); Erwägungsgrund 71
- CH FADP Art. 21 (Automatisierte Einzelentscheide)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für die Identifizierung, Dokumentation und Adressierung von Pflichten gegenüber betroffenen Personen fest, die sich aus der ausschliesslich auf automatisierter Verarbeitung von PII basierenden Entscheidungsfindung ergeben — gemäss ISO/IEC 27701:2025 Kontrolle A.1.3.11.

**Anwendungsbereich**: Alle Verarbeitungstätigkeiten, bei denen [Organisation] als PII-Verantwortlicher Entscheidungen über Personen trifft, die ausschliesslich auf automatisierter Verarbeitung beruhen und rechtliche oder ähnlich erhebliche Auswirkungen auf diese Personen haben; alle Profilerstellungsaktivitäten, die solche Entscheidungen speisen.

**Rollenanwendbarkeit**: Diese Richtlinie gilt für [Organisation] ausschliesslich in der Rolle als **PII-Verantwortlicher**. Kontrolle A.1.3.11 ist verantwortlicherspezifisch (Tabelle A.1).

---

# Anwendungsbereich und Gültigkeit

## ISO/IEC 27701:2025 Kontrollanforderung

**Kontrolle A.1.3.11 — Automatisierte Entscheidungsfindung**
Kontrolle A.1.3.11 verlangt von [Organisation], die Pflichten — einschliesslich rechtlicher Pflichten — gegenüber betroffenen Personen im Zusammenhang mit ausschliesslich durch automatisierte Verarbeitung ihrer PII getroffenen Entscheidungen zu identifizieren und zu dokumentieren sowie nachzuweisen, wie diese Pflichten erfüllt werden.

## Was diese Richtlinie regelt

- Automatisierte Entscheidungsfindungsaktivitäten mit rechtlichen oder ähnlich erheblichen Auswirkungen auf betroffene Personen
- Profilerstellungsaktivitäten, die automatisierte Entscheidungen speisen
- Pflichten gegenüber betroffenen Personen aus solchen Verarbeitungen
- Nachweisbarkeit, wie [Organisation] diesen Pflichten nachkommt

## Was diese Richtlinie NICHT regelt

- Technische Implementierung von AEF-Systemen (siehe PRIV-IMP-A.1.3.11-TG)
- Allgemeine KI/ML-Governance über Datenschutzpflichten hinaus
- Entscheidungsunterstützungssysteme mit menschlicher Beteiligung, bei denen Menschen die endgültige Entscheidung treffen (diese unterliegen nicht den Art. 22-Einschränkungen, obwohl Transparenzpflichten weiterhin gelten)

## Regulatorischer Rahmen

**Tier 1: Obligatorische Compliance** (gemäss PRIV-POL-00):

- **EU GDPR**: Art. 22 (Recht, nicht ausschliesslich automatisierten Entscheidungen mit erheblichen Auswirkungen zu unterliegen; Ausnahmen: Vertrag, Gesetz, ausdrückliche Einwilligung — mit Garantien); Art. 13(2)(f) / 14(2)(g) (Transparenz über AEF-Existenz, Logik, Bedeutung, Konsequenzen); Erwägungsgrund 71 (Kontext der Profilerstellung und Garantien)
- **CH FADP**: Art. 21 (Recht auf Erläuterung automatisierter Entscheide; Recht auf Anforderung einer menschlichen Überprüfung)
- **ISO/IEC 27701:2025**: Kontrolle A.1.3.11 (normativ)

---

# Richtlinienanforderungen

## Identifizierung automatisierter Entscheidungsfindung

[Organisation] **muss** alle Verarbeitungstätigkeiten identifizieren und dokumentieren, bei denen:

- Entscheidungen ausschliesslich auf automatisierter Verarbeitung von PII (ohne bedeutungsvolle menschliche Beteiligung) basieren, UND
- Diese Entscheidungen rechtliche oder ähnlich erhebliche Auswirkungen auf betroffene Personen haben

Beispiele erheblicher Auswirkungen: Kreditablehnung, automatische Ablehnung von Bewerbungen, Versicherungspreisgestaltung, personalisierte Preisgestaltung mit wesentlichen finanziellen Auswirkungen, automatisierter Ausschluss von Diensten.

**Nicht im Anwendungsbereich** (obwohl Transparenzpflichten weiterhin gelten können):
- Entscheidungsunterstützungstools, bei denen ein Mensch die endgültige Entscheidung überprüft und trifft — sofern die Überprüfung bedeutungsvoll ist, d.h. der Prüfer die Informationen und die Fähigkeit hat, das automatisierte Ergebnis zu überschreiben
- Automatisierte Filterung, die Optionen liefert, aber keine endgültige Entscheidung trifft

Der DSB führt ein **AEF-Register** mit allen relevanten automatisierten Entscheidungsfindungsaktivitäten.

## Pflichtidentifizierung

Für jede AEF-Aktivität **muss** [Organisation] Pflichten gegenüber betroffenen Personen identifizieren und dokumentieren, einschliesslich:

- Das Recht, der Entscheidung nicht zu unterliegen (Art. 22(1)), sofern keine Ausnahme gilt
- Anwendbare Ausnahmen: erforderlich für Vertrag (Art. 22(2)(a)), durch Unions- oder Mitgliedstaatsrecht autorisiert (Art. 22(2)(b)) oder ausdrückliche Einwilligung (Art. 22(2)(c))
- Wo eine Ausnahme gilt: erforderliche Garantien (Recht auf menschliche Intervention, Recht auf Äusserung des eigenen Standpunkts, Recht auf Anfechtung der Entscheidung)
- Transparenzpflichten: Betroffene Personen müssen über das Vorhandensein der AEF, die beteiligte Logik sowie die Bedeutung und die vorgesehenen Konsequenzen informiert werden

## Garantien für relevante AEF

Wenn AEF erhebliche Auswirkungen hat und eine Ausnahme zu Art. 22 in Anspruch genommen wird, **muss** [Organisation] implementieren:

1. **Recht auf menschliche Überprüfung**: Ein Mechanismus für betroffene Personen, menschliche Intervention zu beantragen — entweder (a) bevor die Entscheidung umgesetzt wird, oder (b) im Rahmen der Anfechtung einer bereits mitgeteilten Entscheidung. Der Prüfer muss über die Informationen und die Autorität verfügen, das automatisierte Ergebnis zu überschreiben; eine oberflächliche Überprüfung erfüllt diese Garantie nicht
2. **Standpunktäusserung**: Ein Mechanismus für betroffene Personen, ihren Standpunkt zur automatisierten Entscheidung zu äussern
3. **Anfechtung**: Ein Mechanismus für betroffene Personen, die automatisierte Entscheidung anzufechten

Diese Garantien **müssen** den betroffenen Personen im Datenschutzhinweis und bei Mitteilung der automatisierten Entscheidung kommuniziert werden.

## Transparenz

Für jede relevante AEF-Aktivität **müssen** die betroffenen Personen bereitgestellten Transparenzinformationen (gemäss PRIV-POL-A.1.3.2-4) enthalten:

- Das Vorhandensein der automatisierten Entscheidungsfindung
- Aussagekräftige Informationen über die beteiligte Logik (auf einem für betroffene Personen verständlichen Niveau — keine Offenlegung proprietärer Algorithmen)
- Die Bedeutung und die vorgesehenen Konsequenzen dieser Verarbeitung für die betroffene Person

## Besondere Kategorien von PII bei AEF

AEF, die besondere Kategorien von PII verarbeitet, erfordert zusätzlich zu einer Art. 22-Ausnahme eine Art. 9(2)-Bedingung. Eine solche Verarbeitung erfordert die ausdrückliche DSB-Genehmigung und in den meisten Fällen eine DPIA (gemäss PRIV-POL-A.1.2.6-9).

## Nachweisbarkeit

[Organisation] **muss** jederzeit nachweisen können, wie es seinen Pflichten für jede AEF-Aktivität nachkommt — gegenüber Aufsichtsbehörden, betroffenen Personen und Zertifizierungsprüfern. Das AEF-Register und die zugehörige Dokumentation (einschliesslich DPIA, sofern durchgeführt) sind die primären Nachweise.

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Datenschutzbeauftragter (DSB)** | Pflegt AEF-Register; genehmigt neue AEF-Aktivitäten; überprüft Pflichtidentifizierung; genehmigt Garantiendesign; DPIAs für AEF-Verarbeitungen |
| **Legal/Compliance** | Berät zu anwendbaren Ausnahmen von Art. 22; überprüft Rechtsgrundlage für AEF; berät zur Angemessenheit der Art. 22-Garantien |
| **Entwicklungs-/Data-Science-Teams** | Identifizieren AEF-Aktivitäten in den von ihnen entwickelten Systemen; benachrichtigen DSB vor Einsatz von AEF; implementieren Mechanismen für menschliche Überprüfung und Anfechtung |
| **Produktmanagement** | Stellt sicher, dass AEF-Aktivitäten dem DSB während des Produktdesigns gemeldet werden; unterstützt die Implementierung von Garantien |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrung |
|---------|-------------|--------------|
| AEF-Register | Alle AEF-Aktivitäten mit Rechtsgrundlage, geltend gemachter Ausnahme, Garantien, Transparenz | Aktuell + 3 Jahre |
| DPIAs für AEF | Bei Hochrisiko-AEF-Verarbeitung | Dauer der AEF + 3 Jahre |
| Nachweis der Garantienimplementierung | Technische Aufzeichnungen des Mechanismus für menschliche Überprüfung, Anfechtungsprozess | Aktuell + 3 Jahre |
| Register der Betroffenenrechtsanfragen | Anfragen auf menschliche Überprüfung, Standpunktäusserung oder Anfechtung | 5 Jahre |

---

# Prüfungshinweise

Prüfer, die die Compliance mit A.1.3.11 verifizieren, sollten erwarten zu finden:

- AEF-Register mit Identifizierung aller relevanten automatisierten Entscheidungsfindungsaktivitäten
- Für jede Aktivität: dokumentierte geltend gemachte Ausnahme zu Art. 22(1) und vorhandene Garantien
- Transparenzinformationen im Datenschutzhinweis über AEF-Existenz, Logik und Konsequenzen
- Betriebsfähige und zugängliche Mechanismen für menschliche Überprüfung, Standpunktäusserung und Anfechtung
- DPIA für Hochrisiko-AEF-Aktivitäten durchgeführt

---

<!-- QA_VERIFIED: 2026-03-29 -->

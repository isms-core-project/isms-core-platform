<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.8-DE:cloud:POL:a.8 -->
**CLD-PII-POL-A.8 — Offenheit, Transparenz und Mitteilung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Offenheit, Transparenz und Mitteilung |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-PII-POL-A.8 |
| **Dokumentersteller** | Datenschutzbeauftragter (DSB) |
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
| 1.0 | [Date to be set] | DSB | Erstversion für ISO/IEC 27018:2025 Ausg. 3 Implementierung |

**Überprüfungszyklus**: Jährlich (oder bei Änderungen an Unterauftragsverarbeitern oder Dienstmodellen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Datenschutzbeauftragter (DSB)
- Sekundär: ISB / Cloud Security Manager
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII)
- CLD-PII-POL-A.1 (Allgemein)
- CLD-PII-POL-A.11 (Informationssicherheit — §11.12: Unterbeauftragte PII-Verarbeitung)
- CLD-PII-POL-A.12 (Datenschutz-Compliance — geografische Offenlegung)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.8 und Kontrolle A.8.1
- ISO/IEC 27701:2025 Kontrollen A.2.5.7 (Offenlegung der zur PII-Verarbeitung eingesetzten Unterauftragnehmer), A.2.5.8 (Beauftragung eines Unterauftragnehmers zur PII-Verarbeitung) und A.2.5.9 (Wechsel eines Unterauftragnehmers zur PII-Verarbeitung)
- DSGVO Artikel 28 Abs. 2 (Unterauftragsverarbeiter-Genehmigung und Weitergabe von Pflichten); Artikel 28 Abs. 3 lit. d (Auftragsverarbeiter informiert Verantwortlichen über Unterauftragsverarbeiter)
- CH DSG Artikel 9 Abs. 3 (Offenlegungspflichten für Unterauftragsverarbeiter)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] als Public-Cloud-PII-Auftragsverarbeiter in Bezug auf Offenheit, Transparenz und Mitteilung fest — insbesondere die Pflicht, Unterauftragsverarbeiter offenzulegen, die PII im Auftrag von [Organisation] verarbeiten, und eine Vorankündigung über Änderungen an Unterauftragsverarbeiter-Regelungen zu geben — gemäss ISO/IEC 27018:2025 Annex A, Abschnitt A.8 und Kontrolle A.8.1.

**Geltungsbereich**: Alle von [Organisation] beauftragten Unterauftragsverarbeiter, die PII-Verarbeitungsvorgänge als Teil der Cloud-Diensteerbringung durchführen.

**Begründung für die kombinierten Kontrollen**: Transparenz über Unterauftragsverarbeiter ist zentral für das Vertrauensverhältnis zwischen Cloud-Auftragsverarbeitern und ihren Kunden. PII-Verantwortliche müssen wissen, wer Zugang zu ihren PII hat, um ihren eigenen Rechenschaftspflichten nachzukommen, Due Diligence durchzuführen und vertragliche Rechte auszuüben (einschliesslich Widerspruch gegen Unterauftragsverarbeiter-Änderungen gemäss DSGVO Artikel 28 Abs. 2).

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 Kontrollaussagen

**Abschnitt A.8 — Offenheit, Transparenz und Mitteilung (Grundsatz)**

Abschnitt A.8 legt den Grundsatz fest, dass ein Public-Cloud-PII-Auftragsverarbeiter PII-Verantwortlichen Informationen darüber bereitstellen sollte, wo PII verarbeitet wird, welche Unterauftragsverarbeiter eingesetzt werden und etwaige Änderungen an Verarbeitungsregelungen, und seine Datenschutzhinweise aktuell halten sollte.

**Kontrolle A.8.1 — Offenlegung unterbeauftragter PII-Verarbeitung**

Kontrolle A.8.1 verpflichtet den Auftragsverarbeiter, PII-Verantwortlichen die Identität aller Unterauftragsverarbeiter offenzulegen, die PII in seinem Auftrag verarbeiten, und im Voraus über beabsichtigte Ergänzungen oder Ersetzungen zu informieren, damit der Verantwortliche Widerspruch einlegen kann.

## Was diese Richtlinie NICHT regelt

- Vertragsinhalt und Sicherheitsweiterleitung bei Unterauftragsverarbeitern — behandelt in CLD-PII-POL-A.11 (§11.12)
- Geografischer Standort der PII-Verarbeitung — behandelt in CLD-PII-POL-A.12.1
- Benachrichtigungen bei gesetzlich erzwungenen Offenlegungen — behandelt in CLD-PII-POL-A.6.1

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 28 Abs. 2 (Unterauftragsverarbeiter-Beauftragung erfordert vorherige schriftliche Genehmigung des Verantwortlichen — allgemein oder spezifisch); Artikel 28 Abs. 3 lit. d (Auftragsverarbeiter darf Unterauftragsverarbeiter nicht ohne vorherige schriftliche Genehmigung des Verantwortlichen beauftragen); Artikel 28 Abs. 4 (Unterauftragsverarbeiter-Pflichten müssen den Auftragsverarbeiter-Pflichten entsprechen)
- **CH DSG**: Artikel 9 Abs. 3 (Auftragsverarbeiter muss Verantwortlichen über Unterauftragsverarbeiter informieren und Einwilligung einholen; gleichwertige Sicherheit muss vertraglich vorgeschrieben sein)
- **ISO/IEC 27018:2025**: Kontrollen A.8 (Grundsatz) und A.8.1

---

# Richtlinienaussagen: Offenlegung von Unterauftragsverarbeitern (A.8.1)

## Unterauftragsverarbeiter-Register

[Organisation] muss ein **Unterauftragsverarbeiter-Register** führen, das alle Unterauftragsverarbeiter auflistet, die im Auftrag von [Organisation] PII verarbeiten. Das Register muss für jeden Unterauftragsverarbeiter folgende Felder enthalten:

| Feld | Beschreibung |
|------|-------------|
| **Name des Unterauftragsverarbeiters** | Name der juristischen Person |
| **Erbrachte Leistungen** | Spezifische durchgeführte Verarbeitungsvorgänge |
| **Zugängliche PII-Kategorien** | Kategorien von PII, auf die der Unterauftragsverarbeiter zugreifen kann |
| **Verarbeitungsstandort(e)** | Länder oder Regionen, in denen die Verarbeitung stattfindet |
| **Vertragsreferenz** | Verweis auf die bindende Unterauftragsverarbeiter-Vereinbarung |
| **Einwilligungsstatus des Verantwortlichen** | Datum, an dem die allgemeine/spezifische Einwilligung des Verantwortlichen eingeholt wurde |
| **Hinzufügungsdatum / zuletzt geprüft** | Einführungsdatum und jüngstes Überprüfungsdatum |

Das Unterauftragsverarbeiter-Register muss vom DSB gepflegt und allen PII-Verantwortlichen auf Anfrage zur Verfügung gestellt werden. [Organisation] muss ausserdem eine aktuelle Unterauftragsverarbeiter-Liste auf seiner Website oder seinem Trust-Portal für Verantwortliche veröffentlichen, die unter allgemeiner Genehmigung tätig sind. Verantwortliche, die unter spezifischer Unterauftragsverarbeiter-Genehmigung tätig sind, erhalten direkte Benachrichtigungen statt der öffentlichen Liste. Bestehende Einträge im Unterauftragsverarbeiter-Register müssen mindestens jährlich und bei wesentlichen Änderungen der Betriebsweise eines Unterauftragsverarbeiters überprüft werden, um die Aktualität des Registers sicherzustellen.

[Organisation] muss vor der Beauftragung jedes Unterauftragsverarbeiters eine dokumentierte Sicherheits- und Datenschutz-Due-Diligence-Beurteilung durchführen. Die Ergebnisse müssen im Unterauftragsverarbeiter-Register referenziert werden; die Beurteilungsmethodik wird in CLD-PII-POL-A.11 (§11.12) behandelt.

## Vorankündigung bei Änderungen

[Organisation] muss PII-Verantwortliche vor der Umsetzung beabsichtigter Änderungen an Unterauftragsverarbeiter-Regelungen im Voraus informieren, einschliesslich:

- Beauftragung eines neuen Unterauftragsverarbeiters
- Ersatz eines bestehenden Unterauftragsverarbeiters
- Wesentliche Änderung des Umfangs oder Standorts der Verarbeitung eines bestehenden Unterauftragsverarbeiters

**Ankündigungsfrist**: Sofern im Dienstleistungsvertrag keine längere Frist festgelegt ist, muss [Organisation] eine Mindestfrist von **30 Tagen** vor beabsichtigten Unterauftragsverarbeiter-Änderungen einhalten.

Ankündigungen müssen über den im Dienstleistungsvertrag festgelegten Benachrichtigungskanal zugestellt werden (z. B. E-Mail an den designierten Datenschutzkontakt des Verantwortlichen, Trust-Portal-Benachrichtigung oder veröffentlichtes Änderungsprotokoll mit Abonnenten-Benachrichtigungen).

## Widerspruchsrecht des Verantwortlichen

PII-Verantwortliche, die unter allgemeiner Unterauftragsverarbeiter-Genehmigung tätig sind (DSGVO Artikel 28 Abs. 2), haben das Recht, während der Vorankündigungsfrist Widerspruch gegen beabsichtigte Unterauftragsverarbeiter-Änderungen einzulegen. Das Verfahren von [Organisation] zur Behandlung von Widersprüchen lautet:

1. Den Widerspruch innerhalb von 3 Werktagen schriftlich bestätigen
2. Mit dem Verantwortlichen in Kontakt treten, um die Gründe für den Widerspruch zu verstehen
3. Wird dem Widerspruch stattgegeben: eine alternative Verarbeitungsregelung vor der Änderung identifizieren und umsetzen
4. Kann dem Widerspruch nicht entsprochen werden: den Verantwortlichen benachrichtigen und eine Vertragsbeendigung zu angemessenen Bedingungen ohne Vertragsstrafe ermöglichen

Verantwortliche, die innerhalb der Ankündigungsfrist keinen Widerspruch einlegen, gelten als mit der Änderung einverstanden, sofern die allgemeine Unterauftragsverarbeiter-Genehmigung gilt. Dieser Mechanismus der stillschweigenden Akzeptanz gilt nur im Rahmen des allgemeinen Genehmigungsmodells; Verantwortliche, die unter spezifischer Unterauftragsverarbeiter-Genehmigung tätig sind, können eine positive Bestätigung anstelle von Stillschweigen als Akzeptanz verlangen — der Rechts-/Compliance-Beauftragte muss bestätigen, welches Modell für jede Verantwortlichen-Beziehung gilt.

## Notfall-Unterauftragsverarbeiter-Wechsel

Sofern [Organisation] dringend einen Ersatz-Unterauftragsverarbeiter beauftragen muss (z. B. aufgrund von Insolvenz oder Sicherheitsvorfall eines Unterauftragsverarbeiters), muss [Organisation]:

- Betroffene PII-Verantwortliche innerhalb von 72 Stunden nach der Entscheidung zur Beauftragung des Ersatz-Unterauftragsverarbeiters benachrichtigen
- Dem Verantwortlichen eine schriftliche Begründung für die Notfalländerung geben
- Gleichwertige Sicherheits- und Datenschutzkontrollen beim Ersatz-Unterauftragsverarbeiter vor dem PII-Transfer implementieren. Sofern eine vollständige Sicherheitsüberprüfung vor einem Notfalltransfer nicht abgeschlossen werden kann, ist ein vom ISB und DSB unterzeichnetes Risikoakzeptanzdokument erforderlich, mit einem definierten Remediierungszeitraum für etwaige nach dem Transfer festgestellte Lücken
- Die Notfallbenachrichtigung formal abschliessen und das Unterauftragsverarbeiter-Register innerhalb von 5 Werktagen aktualisieren

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Datenschutzbeauftragter (DSB)** | Verantwortlich für das Unterauftragsverarbeiter-Register; verwaltet Verantwortlichen-Benachrichtigungs- und Widerspruchsprozess; genehmigt neue Unterauftragsverarbeiter-Beauftragungen |
| **Rechts-/Compliance-Beauftragter** | Überprüft Unterauftragsverarbeiter-Vereinbarungen auf DSGVO-Artikel-28-Abs.-4-Compliance; berät zur Behandlung von Verantwortlichen-Widersprüchen; pflegt Vertragsreferenzen im Unterauftragsverarbeiter-Register |
| **ISB / Cloud Security Manager** | Beurteilt die Sicherheitslage vorgeschlagener Unterauftragsverarbeiter; stellt sicher, dass Sicherheitskontrollen vertraglich weitergegeben werden; verwaltet Notfall-Unterauftragsverarbeiter-Wechsel |
| **Beschaffung** | Löst DSB- und Rechtsüberprüfung vor der Beauftragung eines neuen Unterauftragsverarbeiters mit PII-Zugang aus; stellt sicher, dass das Unterauftragsverarbeiter-Register bei neuen Beauftragungen aktualisiert wird |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| Unterauftragsverarbeiter-Register | Vollständiges und aktuelles Register mit Pflichtfeldern | Aktuell + Vorgängerversionen für 5 Jahre nach Beauftragungsende — 5-jährige Aufbewahrung entspricht der standardmässigen vertraglichen Verjährungsfrist in EU- und Schweizer Recht |
| Verantwortlichen-Vorankündigungen | Aufzeichnungen der an jeden Verantwortlichen gesendeten Unterauftragsverarbeiter-Änderungsbenachrichtigungen | 5 Jahre |
| Verantwortlichen-Widerspruchsaufzeichnungen | Etwaige eingegangene Verantwortlichen-Widersprüche, Reaktion von [Organisation] und Lösung | 5 Jahre |
| Veröffentlichte Unterauftragsverarbeiter-Liste | Zeitgestempelte Kopien der öffentlich verfügbaren Unterauftragsverarbeiter-Liste bei jeder Version | 5 Jahre |

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-PII-POL-A.8 verifizieren, sollten Folgendes vorfinden:

- Ein aktuelles, vollständiges Unterauftragsverarbeiter-Register mit Verantwortlichen-Einwilligungsstatus für jeden Unterauftragsverarbeiter
- Belege, dass PII-Verantwortliche über alle Unterauftragsverarbeiter-Änderungen im Prüfungszeitraum innerhalb der vorgeschriebenen Ankündigungsfrist vorab informiert wurden
- Aufzeichnungen über etwaige eingegangene Verantwortlichen-Widersprüche und deren Lösung
- Eine öffentlich zugängliche Unterauftragsverarbeiter-Liste, die mit dem internen Unterauftragsverarbeiter-Register übereinstimmt

---

<!-- QA_VERIFIED: 2026-03-29 -->

<!-- ISMS-CORE:POLICY:CLD-POL-A.1-DE:cloud:POL:a.1 -->
**CLD-POL-A.1 — Allgemein**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Allgemeine Anwendbarkeit und Pflichten |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-POL-A.1 |
| **Dokumentersteller** | ISB / Datenschutzbeauftragter (DSB) |
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
| 1.0 | [Date to be set] | ISB / DSB | Erstversion für ISO/IEC 27018:2025 Ausg. 3 Implementierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen regulatorischen oder Dienstmodell-Änderungen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: ISB / Cloud Security Manager
- Sekundär: Datenschutzbeauftragter (DSB)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII — übergeordnete ISMS-Richtlinie)
- CLD-POL-A.2 (Einwilligung und Wahlmöglichkeit)
- CLD-POL-A.3 (Zwecklegitimität und -spezifikation)
- CLD-POL-A.10 (Rechenschaftspflicht)
- CLD-POL-A.11 (Informationssicherheit)
- CLD-POL-A.12 (Datenschutz-Compliance)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.1 (Allgemein)
- ISO/IEC 27701:2025 (Datenschutz-Informationsmanagementsystem)
- ISO/IEC 27002:2022 (Informationssicherheitskontrollen)
- DSGVO Artikel 28 (Auftragsverarbeiter-Pflichten)
- CH DSG Artikel 9 (Bedingungen für die Auftragsverarbeitung)

---

## Zusammenfassung

Diese Richtlinie legt den Geltungsbereich, die Anwendbarkeit und die allgemeinen Pflichten von [Organisation] fest, die als **Public-Cloud-PII-Auftragsverarbeiter** gemäss ISO/IEC 27018:2025 Annex A, Abschnitt A.1 handelt.

**Geltungsbereich**: Alle Cloud-Dienste von [Organisation], bei denen [Organisation] personenbezogene Daten (PII) im Auftrag und auf Weisung eines PII-Verantwortlichen verarbeitet. Dies gilt unabhängig vom Cloud-Dienstmodell (IaaS, PaaS, SaaS) oder Bereitstellungsmodell (öffentlich, hybrid). Hybrid-Bereitstellungen fallen in den Geltungsbereich, soweit die öffentliche Cloud-Komponente die Verarbeitung von PII im Auftrag eines Verantwortlichen umfasst.

**Rollenklärung**: ISO/IEC 27018:2025 gilt für [Organisation] in seiner Eigenschaft als **PII-Auftragsverarbeiter** — eine Einheit, die PII im Auftrag und auf Weisung eines PII-Verantwortlichen verarbeitet. [Organisation] bestimmt nicht die Zwecke und Mittel einer solchen Verarbeitung; diese Verantwortung liegt beim PII-Verantwortlichen.

**Hinweis zu erweiterten Kontrollen**: Die Kontrollen in ISO/IEC 27018:2025 Annex A sind informativer Natur. [Organisation] implementiert sie als Teil seiner Cloud-Datenschutzpraxis, unabhängig von ihrem normativen Status innerhalb des Standards.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 — Abschnitt A.1

**Abschnitt A.1 — Allgemein**

Abschnitt A.1 von ISO/IEC 27018:2025 Annex A legt die allgemeine Anwendbarkeit des Kontrollsatzes fest und definiert die Rolle des Public-Cloud-PII-Auftragsverarbeiters sowie die grundlegenden Pflichten, auf denen alle nachfolgenden Kontrollen des erweiterten Annex-A-Kontrollsatzes aufbauen.

## Anwendbarkeit

Diese Richtlinie und die CLD-POL-A.X-Richtliniensuite gilt für:

- Alle Public-Cloud-Dienste von [Organisation], die PII im Auftrag von Kunden (PII-Verantwortliche) verarbeiten
- Alle Mitarbeitenden, Systeme, Prozesse und Unterauftragsverarbeiter, die an der PII-Verarbeitung beteiligt sind
- Alle Rechtsordnungen, in denen [Organisation] Cloud-Dienste erbringt, bei denen PII von betroffenen Personen verarbeitet wird

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 28 (Auftragsverarbeiter-Pflichten — schriftlicher Vertrag, weisungsgebundene Verarbeitung, Sicherheit, Unterauftragsverarbeiter, Unterstützung, Rückgabe/Löschung, Prüfrechte); Artikel 32 (Sicherheit der Verarbeitung)
- **CH DSG**: Artikel 9 (Bedingungen für die Auftragsverarbeitung und damit verbundene Datensicherheitspflichten)
- **ISO/IEC 27018:2025**: Erweiterter Annex-A-Kontrollsatz — als organisatorische Verpflichtung implementiert

---

# Richtlinienaussagen: Allgemeine Anwendbarkeit (A.1)

## Rolle als PII-Auftragsverarbeiter

[Organisation] muss ausschliesslich als PII-Auftragsverarbeiter handeln — PII nur gemäss den dokumentierten Weisungen der PII-Verantwortlichen verarbeiten. [Organisation] darf nicht:

- Die Zwecke oder Mittel der PII-Verarbeitung über die technische Dienstleistungserbringung hinaus bestimmen
- PII für eigene kommerzielle, analytische oder operative Zwecke ohne ausdrückliche Genehmigung des Verantwortlichen verarbeiten
- Im Auftrag eines Verantwortlichen verarbeitete PII übermitteln, verkaufen oder anderweitig verwerten

## Vertragsanforderung

[Organisation] darf PII nur verarbeiten, wenn ein schriftlicher Vertrag mit dem PII-Verantwortlichen besteht. Dieser Vertrag muss mindestens den Verarbeitungsumfang, Sicherheitspflichten, Benachrichtigung bei Datenschutzverletzungen, Unterauftragsverarbeiter-Regelungen, Datenrückgabe/-löschung und Prüfrechte regeln — gemäss CLD-POL-A.11 (§11.11 — Vertragsanforderungen).

## Dokumentation der Kontrollen

[Organisation] muss dokumentieren, wie jede anwendbare Kontrolle aus ISO/IEC 27018:2025 Annex A in seinen Diensten umgesetzt wird. Diese Dokumentation muss PII-Verantwortlichen auf Anfrage zur Verfügung gestellt und gegebenenfalls vertraglich in Dienstleistungsvereinbarungen aufgenommen werden.

## Weisungsgebundene Verarbeitung

[Organisation] muss PII ausschliesslich gemäss dokumentierten, aktuellen Weisungen des PII-Verantwortlichen verarbeiten. Sofern [Organisation] durch anwendbares Recht zur PII-Verarbeitung über die Weisungen des Verantwortlichen hinaus verpflichtet wird, muss [Organisation] den PII-Verantwortlichen vor der Verarbeitung darüber informieren — es sei denn, dies ist gesetzlich untersagt.

## Management von Unterauftragsverarbeitern

[Organisation] darf Unterauftragsverarbeiter nur mit vorheriger schriftlicher Zustimmung des PII-Verantwortlichen einsetzen. Alle Unterauftragsverarbeiter müssen durch gleichwertige Datenschutzpflichten gebunden sein. [Organisation] bleibt gegenüber dem Verantwortlichen für die Compliance der Unterauftragsverarbeiter verantwortlich. Unterauftragsverarbeiter-Regelungen werden im Detail durch CLD-POL-A.11 (§11.12 — Pflichten der Unterauftragsverarbeiter) geregelt.

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB / Cloud Security Manager** | Pflegt die CLD-POL-A.X-Richtliniensuite; stellt sicher, dass technische Kontrollen die Anforderungen von ISO 27018:2025 Annex A erfüllen; berichtet über die Compliance des Cloud-PII-Auftragsverarbeiters |
| **Datenschutzbeauftragter (DSB)** | Berät zur regulatorischen Compliance von Auftragsverarbeiter-Aktivitäten; prüft Auftragsverarbeiter-Vereinbarungen; koordiniert PII-Angelegenheiten mit Verantwortlichen |
| **Rechts-/Compliance-Beauftragter** | Prüft Vertragsbedingungen für Auftragsverarbeiter; berät zu anwendbaren gesetzlichen Pflichten; bewertet regulatorische Änderungen mit Auswirkungen auf Auftragsverarbeiter-Pflichten |
| **Cloud-Diensteerbringung** | Betreibt Dienste innerhalb dokumentierter Weisungen der Verantwortlichen; eskaliert Anfragen ausserhalb des Geltungsbereichs an ISB und DSB |
| **Alle Mitarbeitenden** | Verarbeiten PII nur wie autorisiert; melden mutmassliche Richtlinienverstösse unverzüglich an ISB und DSB |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| Auftragsverarbeiter-Vereinbarungsregister | Liste aller aktiven PII-Verantwortlichen-Vereinbarungen mit Umfang, Status und Überprüfungsdatum | Aktuell + 3 Jahre nach Vertragsende |
| Dokumentation der Kontrollumsetzung | Dokumentation der Umsetzung jeder CLD-POL-A.X-Kontrolle pro Dienst | Aktuelle Version + Vorgängerversionen für 3 Jahre nach Ablösung |
| Unterauftragsverarbeiter-Register | Liste genehmigter Unterauftragsverarbeiter mit Einwilligungsnachweisen der Verantwortlichen | Aktuell + 3 Jahre nach Ende der Beauftragung |
| Weisungsnachweise | Aufzeichnungen dokumentierter Verarbeitungsweisungen der Verantwortlichen und etwaiger Abweichungen | Vertragsdauer + 3 Jahre |

> **Aufbewahrungsgrundlage**: 3-Jahres-Zeiträume entsprechen den anwendbaren Verjährungsfristen gemäss EU- und Schweizer Recht für Streitigkeiten aus Auftragsverarbeiter-Vereinbarungen. Längere Zeiträume können gelten, sofern regulatorische Prüfanforderungen oder Vertragsbedingungen dies vorschreiben.

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-POL-A.1 verifizieren, sollten Folgendes vorfinden:

- Auftragsverarbeiter-Vereinbarungsregister, das schriftliche Verträge mit allen PII-Verantwortlichen belegt
- Dokumentation, die jede Kontrolle aus ISO/IEC 27018:2025 Annex A der Dienst-Implementierung zuordnet
- Unterauftragsverarbeiter-Register mit Einwilligungsnachweisen der Verantwortlichen für jeden Unterauftragsverarbeiter
- Belege, dass die Verarbeitung ausschliesslich gemäss dokumentierten Weisungen der Verantwortlichen erfolgt

---

<!-- QA_VERIFIED: 2026-03-29 -->

<!-- ISMS-CORE:POLICY:CLD-POL-A.3-DE:cloud:POL:a.3 -->
**CLD-POL-A.3 — Zwecklegitimität und -spezifikation**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Zwecklegitimität und -spezifikation |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-POL-A.3 |
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

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen regulatorischen oder Dienstmodell-Änderungen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Datenschutzbeauftragter (DSB)
- Sekundär: ISB / Cloud Security Manager
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII)
- CLD-POL-A.1 (Allgemein)
- CLD-POL-A.2 (Einwilligung und Wahlmöglichkeit)
- CLD-POL-A.4 (Datenerhebungsbegrenzung)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.3 und Kontrollen A.3.1–A.3.2
- ISO/IEC 27701:2025 Kontrollen A.2.2.3 (Auftragsverarbeiter — Zwecke der Organisation) und A.2.2.4 (Auftragsverarbeiter — Marketing- und Werbenutzung)
- DSGVO Artikel 28 Abs. 3 lit. a (weisungsgebundene Verarbeitung); Artikel 5 Abs. 1 lit. b (Zweckbindungsgrundsatz)
- CH DSG Artikel 6 Abs. 3 (Zweckbindung); Artikel 9 (Auftragsverarbeiter-Pflichten)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] als Public-Cloud-PII-Auftragsverarbeiter in Bezug auf Zwecklegitimität und -spezifikation fest — insbesondere die Beschränkung auf vom Verantwortlichen festgelegte Verarbeitungszwecke und das absolute Verbot der kommerziellen Nutzung von PII der Verantwortlichen ohne ausdrückliche Genehmigung — gemäss ISO/IEC 27018:2025 Annex A, Kontrollen A.3.1 und A.3.2.

**Geltungsbereich**: Alle PII-Verarbeitungsvorgänge, die [Organisation] im Auftrag von PII-Verantwortlichen auf der Grundlage von Cloud-Dienstleistungsverträgen durchführt.

**Begründung für die kombinierten Kontrollen**: A.3.1 und A.3.2 definieren gemeinsam die Zweckgrenze für [Organisation] als Auftragsverarbeiter. A.3.1 beschränkt die Verarbeitung auf vereinbarte Zwecke; A.3.2 verbietet ausdrücklich die Monetarisierung von PII zugunsten des Auftragsverarbeiters. Diese Kontrollen sind der operative Ausdruck des in CLD-POL-A.2 festgelegten Grundsatzes der weisungsgebundenen Verarbeitung.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 Kontrollaussagen

**Abschnitt A.3 — Zwecklegitimität und -spezifikation (Grundsatz)**

Abschnitt A.3 legt den Grundsatz fest, dass ein Public-Cloud-PII-Auftragsverarbeiter alle Verarbeitungsvorgänge auf die in seiner Vereinbarung mit dem PII-Verantwortlichen festgelegten Zwecke beschränken und vor der Einführung eines neuen Verarbeitungszwecks eine Genehmigung des Verantwortlichen einholen muss.

**Kontrolle A.3.1 — Verarbeitungszweck des Public-Cloud-PII-Auftragsverarbeiters**

Kontrolle A.3.1 verpflichtet den Auftragsverarbeiter, PII nur für die mit dem Verantwortlichen vereinbarten dokumentierten Zwecke zu verarbeiten, und untersagt die Verarbeitung für eigene Zwecke des Auftragsverarbeiters, es sei denn, der Verantwortliche hat dies schriftlich ausdrücklich genehmigt.

**Kontrolle A.3.2 — Kommerzielle Nutzung durch den Public-Cloud-PII-Auftragsverarbeiter**

Kontrolle A.3.2 untersagt dem Auftragsverarbeiter die Nutzung von PII der Verantwortlichen zu eigenen kommerziellen Zwecken — einschliesslich Werbung, Profiling, Datenverkauf oder Produktverbesserung — ohne dokumentierte schriftliche Genehmigung des Verantwortlichen, und verlangt die Offenlegung einer solchen Vereinbarung im Dienstleistungsvertrag.

## Was diese Richtlinie NICHT regelt

- Die Bestimmung oder Validierung der Legitimität des Verarbeitungszwecks des Verantwortlichen — das liegt in der Verantwortung des Verantwortlichen
- Die eigene Verarbeitung von Daten durch [Organisation], die es direkt erhebt (nicht im Auftrag eines Verantwortlichen) — geregelt durch ISMS-POL-A.5.34

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 5 Abs. 1 lit. b (Zweckbindungsgrundsatz — gilt für den Verantwortlichen; der Auftragsverarbeiter darf ihn nicht untergraben); Artikel 28 Abs. 3 lit. a (Auftragsverarbeiter verarbeitet nur auf Weisung des Verantwortlichen und für keinen anderen Zweck)
- **CH DSG**: Artikel 6 Abs. 3 (Zweckbindung); Artikel 9 Abs. 2 lit. b (Auftragsverarbeiter ist an die Zweckspezifikation des Verantwortlichen gebunden)
- **ISO/IEC 27018:2025**: Kontrollen A.3.1 und A.3.2

---

# Richtlinienaussagen: Verarbeitungszweck des Auftragsverarbeiters (A.3.1)

## Zweckbeschränkung

[Organisation] darf PII nur für die im Dienstleistungsvertrag oder in schriftlichen Verarbeitungsweisungen des PII-Verantwortlichen ausdrücklich dokumentierten Zwecke verarbeiten. Die Verarbeitung darf ohne vorherige schriftliche Genehmigung des Verantwortlichen nicht auf neue Zwecke ausgeweitet werden.

## Dokumentation von Verarbeitungszwecken

Alle Cloud-Dienstleistungsverträge mit PII-Verantwortlichen müssen eine Verarbeitungsbeschreibung enthalten, die Folgendes spezifiziert:

- Die zu verarbeitenden PII-Kategorien
- Die Verarbeitungszwecke
- Die durchzuführenden Verarbeitungsvorgänge
- Die Verarbeitungsdauer
- Etwaige genehmigte Unterauftragsverarbeiter-Regelungen

## Anfragen zu neuen Zwecken

Sofern [Organisation] einen betrieblichen Bedarf identifiziert, PII für einen nicht durch die aktuelle Vereinbarung abgedeckten Zweck zu verarbeiten (z. B. Vorfalluntersuchung, die Zugriff auf PII über die normale Diensteerbringung hinaus erfordert), muss [Organisation]:

1. Den vorgeschlagenen neuen Zweck schriftlich dokumentieren
2. Vor Beginn der Verarbeitung eine schriftliche Genehmigung des Verantwortlichen einholen
3. Die Genehmigung im Auftragsverarbeiter-Vereinbarungsregister erfassen
4. Die zusätzliche Verarbeitung einstellen, falls die Genehmigung verweigert oder widerrufen wird

Reagiert ein Verantwortlicher nicht innerhalb von 15 Werktagen auf eine schriftliche Anfrage für einen neuen Zweck, gilt die Anfrage als abgelehnt, und [Organisation] führt die zusätzliche Verarbeitung nicht durch.

## Betriebliche Telemetrie

[Organisation] darf Dienst-Telemetrie und betriebliche Metadaten (z. B. Performance-Metriken, Fehlerprotokolle) erheben, soweit dies für die Diensteerbringung erforderlich ist. Sofern solche Telemetrie zufällig PII enthält:

- Ist sie als PII zu behandeln, die dieser Richtlinie unterliegt
- Ist die Aufbewahrung auf den für betriebliche Zwecke erforderlichen Mindestzeitraum zu begrenzen, höchstens 90 Tage, es sei denn, dies ist betrieblich begründet und mit Genehmigung von ISB und DSB dokumentiert
- Darf sie nicht ohne Genehmigung des Verantwortlichen für Analyse-, Produktverbesserungs- oder kommerzielle Zwecke genutzt werden

---

# Richtlinienaussagen: Verbot der kommerziellen Nutzung (A.3.2)

## Absolutes Verbot

[Organisation] darf PII, die im Auftrag eines PII-Verantwortlichen verarbeitet wird, nicht für eigene kommerzielle Zwecke von [Organisation] nutzen, einschliesslich, aber nicht beschränkt auf:

- Zielgerichtete Werbung oder Werbe-Profiling
- Verkauf oder Lizenzierung von PII oder abgeleiteten Datensätzen an Dritte
- Training oder Verbesserung von Machine-Learning-Modellen unter Verwendung von PII
- Nutzung von PII der Verantwortlichen für Wettbewerbsanalyse oder Marktpositionierungszwecke
- Marktforschung oder Kundenanalysen, die nicht direkt den vertraglichen Dienst unterstützen

Dieses Verbot gilt unabhängig davon, ob die PII aggregiert, pseudonymisiert oder de-identifiziert wurde — es sei denn, der DSB von [Organisation] hat schriftlich bestätigt, dass die Daten echte und irreversible Anonymisierung darstellen.

## Vertragliche Verpflichtung

Die Dienstleistungsverträge von [Organisation] müssen eine ausdrückliche Klausel enthalten, die das Verbot der kommerziellen Nutzung bestätigt. Jede vorgeschlagene Vereinbarung zur kommerziellen Nutzung (einschliesslich solcher, die echte anonymisierte Daten betreffen) muss:

- Dem PII-Verantwortlichen vor der Implementierung vorgeschlagen und schriftlich vereinbart werden
- Im Dienstleistungsvertrag offengelegt werden
- Vor der Ausführung vom DSB und vom Rechts-/Compliance-Beauftragten überprüft werden

## Interne Sicherheitsmassnahmen

Zur Durchsetzung des Verbots der kommerziellen Nutzung muss [Organisation]:

- Technische Zugriffskontrollen implementieren, die PII der Verantwortlichen von den internen Produkt- und Analysesystemen von [Organisation] trennen
- Marketing- und Geschäftsteams von [Organisation] den Zugriff auf PII der Verantwortlichen ohne DSB-Genehmigung untersagen
- Das Verbot der kommerziellen Nutzung in das Mitarbeiterschulungsprogramm zur Sicherheitskompetenz (siehe ISMS-POL-A.6.3) und in standardmässige Vertraulichkeitsvereinbarungen in Arbeits- und Auftragnehmerverträgen aufnehmen

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Datenschutzbeauftragter (DSB)** | Prüft und genehmigt vorgeschlagene neue Verarbeitungszwecke oder Vereinbarungen zur kommerziellen Nutzung; pflegt Aufzeichnungen über Zweckgenehmigungen; überwacht die Einhaltung der Zweckbeschränkung |
| **Rechts-/Compliance-Beauftragter** | Prüft Verarbeitungsbeschreibungen in Dienstleistungsverträgen auf Vollständigkeit und Compliance; berät zu Zweckbindungspflichten gemäss DSGVO und DSG |
| **ISB / Cloud Security Manager** | Implementiert technische Kontrollen, die eine Querkontamination von PII der Verantwortlichen und internen Systemen von [Organisation] verhindern; integriert Zweckkontrollen in die Dienstarchitektur |
| **Produkt-/Geschäftsteams** | Dürfen ohne schriftliche DSB-Genehmigung nicht auf PII der Verantwortlichen für Produktentwicklung oder kommerzielle Zwecke zugreifen; müssen entsprechende Anfragen über den DSB weiterleiten |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| Verarbeitungsbeschreibungen in Dienstleistungsverträgen | Dokumentierter Verarbeitungszweck pro Dienst und pro Verantwortlichem | Vertragsdauer + 3 Jahre |
| Aufzeichnungen zu Genehmigungen neuer Zwecke | Schriftliche Verantwortlichen-Genehmigungen für Verarbeitungen über die ursprüngliche Vereinbarung hinaus | Verarbeitungsdauer + 3 Jahre |
| DSB-Anonymisierungsbestätigungen | Schriftliche DSB-Beurteilungen, die bestätigen, dass ein abgeleiteter Datensatz echte Anonymisierung darstellt | Nutzungsdauer + 3 Jahre |
| Zugriffscontroll-Dokumentation | Technische Dokumentation, die die Trennung von PII der Verantwortlichen von internen Systemen belegt | Aktuell + 3 Jahre |

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-POL-A.3 verifizieren, sollten Folgendes vorfinden:

- Dienstleistungsverträge mit ausdrücklichen Verarbeitungszweckbeschreibungen für alle aktiven Verantwortlichen-Beziehungen
- Keine Belege für den Zugriff von Marketing-, Analyse- oder Produktteams von [Organisation] auf PII der Verantwortlichen ohne dokumentierte Genehmigung
- Aufzeichnungen über etwaige von Verantwortlichen eingeholte Genehmigungen für neue Zwecke
- Technische Architekturdokumentation, die die systemseitige Trennung zwischen PII der Verantwortlichen und den internen Datensystemen von [Organisation] belegt

---

<!-- QA_VERIFIED: 2026-03-29 -->

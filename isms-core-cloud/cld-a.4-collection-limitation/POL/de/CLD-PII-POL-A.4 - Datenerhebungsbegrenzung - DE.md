<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.4-DE:cloud:POL:a.4 -->
**CLD-PII-POL-A.4 — Datenerhebungsbegrenzung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Datenerhebungsbegrenzung |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-PII-POL-A.4 |
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
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII)
- CLD-PII-POL-A.3 (Zwecklegitimität und -spezifikation)
- CLD-PII-POL-A.5 (Datenminimerung)
- CLD-PII-POL-A.6 (Nutzungs-, Aufbewahrungs- und Offenlegungsbegrenzung)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.4 (Datenerhebungsbegrenzung — Grundsatz)
- ISO/IEC 27701:2025 Kontrollen A.2.4.2 (Auftragsverarbeiter — temporäre Dateien) und A.2.4.3 (Auftragsverarbeiter — Rückgabe, Übertragung oder Entsorgung von PII)
- DSGVO Artikel 5 Abs. 1 lit. c (Datenminimerungsgrundsatz); Artikel 28 Abs. 3 lit. a (weisungsgebundene Verarbeitung)
- CH DSG Artikel 6 Abs. 2 (Verhältnismässigkeit); Artikel 9 (Auftragsverarbeiter-Pflichten)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] als Public-Cloud-PII-Auftragsverarbeiter in Bezug auf die Datenerhebungsbegrenzung fest — insbesondere die Pflicht, nur die zur Erbringung des vertraglichen Dienstes erforderlichen Mindest-PII zu verarbeiten, und den Umgang mit überschüssig erhobenen PII im Rahmen der Diensteerbringung — gemäss ISO/IEC 27018:2025 Annex A, Abschnitt A.4.

**Geltungsbereich**: Alle PII, die [Organisation] im Rahmen der Erbringung von Cloud-Diensten für PII-Verantwortliche erhebt, empfängt oder anderweitig erlangt.

**Hinweis zum Grundsatz**: Abschnitt A.4 gilt auf Grundsatzebene. Diese Richtlinie überträgt diesen Grundsatz in spezifische betriebliche Pflichten für die Cloud-Dienste von [Organisation]. Technische Datenminimerungsmethoden — einschliesslich Anonymisierung, Pseudonymisierung und Verwaltung temporärer Dateien — werden in CLD-PII-POL-A.5 behandelt.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 — Abschnitt A.4

**Abschnitt A.4 — Datenerhebungsbegrenzung (Grundsatz)**

Abschnitt A.4 legt den Grundsatz fest, dass ein Public-Cloud-PII-Auftragsverarbeiter nur die für den vertraglichen Dienst erforderlichen PII erheben, seine Erhebungspraktiken dokumentieren und etwaige im Rahmen der Diensteerbringung anfallende überschüssige PII unverzüglich bereinigen sollte.

## Was diese Richtlinie NICHT regelt

- Die Bestimmung, welche PII ein Verantwortlicher von betroffenen Personen rechtmässig erheben darf — das liegt in der Verantwortung des Verantwortlichen
- Technische Anonymisierungs- und Löschungsmethoden für temporäre Dateien — behandelt in CLD-PII-POL-A.5

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 5 Abs. 1 lit. c (Datenminimerung — angemessen, erheblich und auf das notwendige Mass beschränkt); Artikel 28 Abs. 3 lit. a (Auftragsverarbeiter verarbeitet nur weisungsgemäss — keine übermässige Erhebung)
- **CH DSG**: Artikel 6 Abs. 2 (Verhältnismässigkeit — die Verarbeitung personenbezogener Daten muss dem Zweck angemessen sein)
- **ISO/IEC 27018:2025**: Grundsatz Abschnitt A.4

---

# Richtlinienaussagen: Datenerhebungsbegrenzung (A.4)

## Erhebung des erforderlichen Minimums

[Organisation] darf ausschliesslich die zur Erbringung des vertraglichen Cloud-Dienstes erforderlichen Mindest-PII erheben, aufbewahren oder anderweitig verarbeiten. [Organisation] darf nicht:

- PII-Kategorien vom PII-Verantwortlichen anfordern oder entgegennehmen, die über das für die Diensteerbringung Erforderliche hinausgehen
- PII über die betriebliche Notwendigkeit der Verarbeitung hinaus in Systemkomponenten, Protokollen oder betrieblichen Datenbanken speichern
- PII ohne ausdrückliche Genehmigung des Verantwortlichen zu anderen Zwecken als Diensteerbringung und Ausfallsicherheit über Umgebungen hinweg replizieren (Entwicklung, Test, Staging, Produktion)

## Dokumentation der Erhebungspraktiken

[Organisation] muss die PII-Erhebungspraktiken für jeden Cloud-Dienst dokumentieren, einschliesslich:

- Kategorien von PII, die im Rahmen der Diensteerbringung erhoben oder empfangen werden
- Der betrieblichen Begründung für jede PII-Kategorie
- Der Systemkomponenten, Protokolle und Speicherorte, an denen PII vorhanden sein kann
- Der für jeden Erhebungstyp geltenden Aufbewahrungsfristen

Diese Dokumentation muss im ISMS-Dokumentenmanagementsystem (oder der designierten GRC-Plattform) gepflegt, jährlich überprüft und bei wesentlichen Änderungen der Dienstarchitektur aktualisiert werden. Der ISB ist der designierte Eigentümer der Dokumentation der Erhebungspraktiken.

## Überschüssige PII

Sofern [Organisation] feststellt, dass PII erhoben wurde, die den Umfang des vertraglichen Dienstes überschreitet (z. B. wenn ein Verantwortlicher einen Datensatz hochlädt, der PII-Kategorien ausserhalb des Dienstumfangs enthält), muss [Organisation]:

1. Den PII-Verantwortlichen innerhalb von 3 Werktagen nach der Feststellung über die überschüssigen PII informieren
2. Mit dem Verantwortlichen vereinbaren, ob die überschüssigen PII zurückgegeben oder sicher gelöscht werden sollen
3. Die vereinbarte Massnahme innerhalb der mit dem Verantwortlichen vereinbarten Frist abschliessen
4. Den Vorfall und das Ergebnis dokumentieren

## Entwicklungs- und Testumgebungen

[Organisation] sollte in Nicht-Produktionsumgebungen, wo technisch durchführbar, anonymisierte oder synthetische Daten verwenden und den Einsatz von Produktions-PII als letztes Mittel behandeln. PII aus Produktionsumgebungen darf ohne ausdrückliche schriftliche Genehmigung des PII-Verantwortlichen nicht in Entwicklungs-, Test- oder Staging-Umgebungen verwendet werden. Sofern eine Genehmigung des Verantwortlichen vorliegt, müssen die erforderlichen Mindest-PII verwendet werden, die in der Produktion geltenden Sicherheitskontrollen müssen angewendet werden (gemäss CLD-PII-POL-A.11), und der Zugang muss auf den für den spezifischen Zweck minimal erforderlichen Personenkreis beschränkt sein.

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB / Cloud Security Manager** | Stellt sicher, dass die Dienstarchitektur die erforderlichen Mindest-PII erhebt; pflegt Erhebungsdokumentation; überprüft den Erhebungsumfang bei Dienstentwicklung und -änderungen |
| **Datenschutzbeauftragter (DSB)** | Überprüft Erhebungsdokumentation jährlich; berät zu Verhältnismässigkeitsprüfungen; überwacht auf Ereignisse überschüssiger Erhebung |
| **Cloud-Diensteerbringung / Engineering** | Implementiert Architektur mit minimaler Erhebung; meldet Ereignisse überschüssiger Erhebung unverzüglich an ISB und DSB |
| **Rechts-/Compliance-Beauftragter** | Berät zu Verhältnismässigkeits- und Minimerungspflichten gemäss DSGVO und DSG |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| Dokumentation der Erhebungspraktiken | Dokumentierte PII-Kategorien, Begründungen und Speicherorte pro Dienst | Aktuell + Vorgängerversionen für 3 Jahre |
| Aufzeichnungen der jährlichen Überprüfung | Unterzeichnete Aufzeichnungen der jährlichen Überprüfungen der Erhebungspraktiken | 3 Jahre |
| Aufzeichnungen zu Ereignissen überschüssiger PII | Dokumentation etwaiger Ereignisse überschüssiger PII, Verantwortlichen-Benachrichtigungen und Lösungen | Vertragsdauer + 3 Jahre |
| Genehmigungsnachweise für Entwicklung/Test | Schriftliche Verantwortlichen-Genehmigungen für die Nutzung von Produktions-PII in Nicht-Produktionsumgebungen | Nutzungsdauer + 3 Jahre |

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-PII-POL-A.4 verifizieren, sollten Folgendes vorfinden:

- Dokumentierte Erhebungspraxisaufzeichnungen für jeden Cloud-Dienst mit PII-Kategorien und Begründungen
- Belege für jährliche Überprüfungen der Erhebungspraktiken
- Keine PII-Kategorien in Betriebssystemen, die den vertraglichen Dienstumfang überschreiten
- Etwaige Ereignisse überschüssiger PII dokumentiert mit Verantwortlichen-Benachrichtigung und Lösungsaufzeichnungen
- Keine Produktions-PII in Entwicklungs- oder Testumgebungen ohne dokumentierte Genehmigung des Verantwortlichen

---

<!-- QA_VERIFIED: 2026-03-29 -->

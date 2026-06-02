<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.5-DE:cloud:POL:a.5 -->
**CLD-PII-POL-A.5 — Datenminimerung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Datenminimerung |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-PII-POL-A.5 |
| **Dokumentersteller** | ISB / Cloud Security Manager |
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
| 1.0 | [Date to be set] | ISB / Cloud Security Manager | Erstversion für ISO/IEC 27018:2025 Ausg. 3 Implementierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Änderungen der Dienstarchitektur)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: ISB / Cloud Security Manager
- Sekundär: Datenschutzbeauftragter (DSB)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII)
- ISMS-POL-A.8.10 (Informationslöschung)
- CLD-PII-POL-A.4 (Datenerhebungsbegrenzung)
- CLD-PII-POL-A.6 (Nutzungs-, Aufbewahrungs- und Offenlegungsbegrenzung)
- CLD-PII-POL-A.11 (Informationssicherheit — umfasst portable Datenträger, Verschlüsselung, Entsorgung)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.5 und Kontrolle A.5.1
- ISO/IEC 27701:2025 Kontrollen A.2.4.2 (Auftragsverarbeiter — temporäre Dateien) und A.2.4.3 (Auftragsverarbeiter — Rückgabe, Übertragung oder Entsorgung von PII)
- DSGVO Artikel 5 Abs. 1 lit. c (Datenminimerung); Artikel 5 Abs. 1 lit. e (Speicherbegrenzung)
- CH DSG Artikel 6 Abs. 2 (Verhältnismässigkeit)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] als Public-Cloud-PII-Auftragsverarbeiter in Bezug auf Datenminimerung fest — insbesondere die sichere Löschung temporärer Dateien mit PII, die bei Cloud-Verarbeitungsvorgängen entstehen — gemäss ISO/IEC 27018:2025 Annex A, Abschnitt A.5 und Kontrolle A.5.1.

**Geltungsbereich**: Alle flüchtigen, temporären und Arbeitsspeicher, die von den Cloud-Diensten von [Organisation] während der PII-Verarbeitung erstellt werden, einschliesslich Cache, Swap, Arbeitsdateien und Protokolle.

**Begründung für die kombinierten Kontrollen**: Abschnitt A.5 legt den Grundsatz fest, dass eine vollständige Identifizierung vermieden werden sollte, wenn die Verarbeitung mit anonymisierten oder pseudonymisierten Daten durchgeführt werden kann. Kontrolle A.5.1 befasst sich mit dem spezifischen Cloud-Risiko, dass PII nach Abschluss der Verarbeitung in temporärem Speicher verbleiben — ein besonders erhebliches Risiko in mandantenfähigen Cloud-Umgebungen, in denen Speicher neu zugewiesen werden kann.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 Kontrollaussagen

**Abschnitt A.5 — Datenminimerung (Grundsatz)**

Abschnitt A.5 legt den Grundsatz fest, dass eine vollständige Identifizierung von betroffenen Personen vermieden werden sollte, wenn die Verarbeitung mit anonymisierten, pseudonymisierten oder aggregierten Daten durchgeführt werden kann, und dass die eingesetzten Techniken dokumentiert und überprüft werden sollten.

**Kontrolle A.5.1 — Sichere Löschung temporärer Dateien**

Kontrolle A.5.1 befasst sich mit dem spezifischen Risiko, dass PII nach Abschluss der Verarbeitung in temporärem Speicher verbleiben. Sie verpflichtet den Auftragsverarbeiter, sichere Löschung temporärer Dateien — einschliesslich Cache, Swap, Arbeitsdateien und Protokolle — mit Methoden zu implementieren, die eine Wiederherstellung verhindern, sowohl für persistenten als auch für flüchtigen Speicher.

## Was diese Richtlinie NICHT regelt

- Aufbewahrungsfristen für primäre PII-Datenspeicher — behandelt in CLD-PII-POL-A.6
- Sichere Entsorgung physischer Speichermedien — behandelt in CLD-PII-POL-A.11

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 5 Abs. 1 lit. c (Datenminimerung); Artikel 5 Abs. 1 lit. e (Speicherbegrenzung — nicht länger als erforderlich); Artikel 32 Abs. 1 lit. a (Pseudonymisierung und Verschlüsselung als angemessene Sicherheitsmassnahmen)
- **CH DSG**: Artikel 6 Abs. 2 (Verhältnismässigkeit); Artikel 9 (Auftragsverarbeiter-Pflichten — angemessene technische Massnahmen)
- **ISO/IEC 27018:2025**: Kontrollen A.5 (Grundsatz) und A.5.1

---

# Richtlinienaussagen: Datenminimerungsgrundsatz (A.5)

## Pseudonymisierung und Anonymisierung

Sofern der Verarbeitungszweck ohne direkte Identifizierung von betroffenen Personen erfüllt werden kann, muss [Organisation] Pseudonymisierung oder Anonymisierung als Teil des Dienstdesigns implementieren. Insbesondere:

- Analyse- und Berichtsfunktionen müssen, wo technisch durchführbar, pseudonymisierte oder aggregierte Daten verwenden
- Protokollierungs- und Telemetriesysteme müssen die PII-Erfassung auf das betrieblich notwendige Minimum beschränken
- Test- und Entwicklungsumgebungen müssen, wo immer möglich, synthetische oder anonymisierte Datensätze verwenden

Auf PII der Verantwortlichen angewendete Anonymisierungstechniken müssen dokumentiert und vor der Implementierung einer DSB-Überprüfung unterzogen werden, um zu bestätigen, dass das Ergebnis echte und irreversible Anonymisierung darstellt. Die DSB-Beurteilung muss gemäss den Leitlinien der zuständigen Aufsichtsbehörde durchgeführt werden (einschliesslich EDSA Opinion 05/2014 zu Anonymisierungstechniken oder ihrer Nachfolgeversion).

---

# Richtlinienaussagen: Sichere Löschung temporärer Dateien (A.5.1)

## Typen temporärer Dateien im Geltungsbereich

Die Cloud-Dienste von [Organisation] erzeugen folgende Kategorien temporären Speichers, der PII enthalten kann und dieser Richtlinie unterliegt:

- **Cache-Dateien**: Von Anwendungsschichten während der aktiven Verarbeitung temporär gespeicherte Daten
- **Swap-Dateien / Auslagerungsdateien**: Arbeitsspeicher-Überlauf des Betriebssystems, der auf Datenträger ausgelagert wird
- **Arbeitsdateien / Scratch Space**: Zwischen-Verarbeitungsdateien, die bei Stapel- oder Streamoperationen erstellt werden
- **Anwendungsprotokolldateien**: Dienst-Protokolle, die bei der Verarbeitung erstellt werden und PII in Nutzdaten, Fehler-Traces oder Debug-Ausgaben erfassen können
- **Flüchtiger Compute-Speicher**: An Compute-Instanzen während der Auftragsausführung angehängter Blockspeicher

## Löschungsanforderung

[Organisation] muss alle oben aufgeführten Kategorien temporären Speichers nach Abschluss des Verarbeitungsvorgangs, für den sie erstellt wurden, sicher löschen. Die Löschung muss mit Methoden durchgeführt werden, die eine Datenwiederherstellung verhindern, gemäss NIST SP 800-88 (Guidelines for Media Sanitization) oder gleichwertig, einschliesslich:

- Kryptografische Löschung (Verschlüsselungsschlüssel-Löschung für verschlüsselte Volumes) — nur wirksam, wenn die Daten mit einem dedizierten Schlüssel verschlüsselt wurden, der ausserhalb des Löschbereichs weder repliziert noch gesichert wurde
- Mehrfachüberschreibung für persistenten Speicher, wenn kryptografische Löschung nicht anwendbar ist
- Sicheres Speicher-Nullen für In-Memory-PII nach Verwendung

Der Löschungsmechanismus muss, wo technisch durchführbar, automatisiert in die Dienst-Pipeline integriert werden, um die Abhängigkeit von manuellen Verfahren zu vermeiden.

## Protokoll-Minimerung

Anwendungs- und Infrastrukturprotokolle, die PII erfassen, unterliegen:

- **Minimerter Erfassung**: Protokollkonfigurationen müssen überprüft werden, um sicherzustellen, dass PII in Nutzdaten, Headern oder Parametern maskiert oder ausgeschlossen wird, sofern dies betrieblich nicht unbedingt erforderlich ist
- **Aufbewahrungsbegrenzungen**: Protokolle mit PII dürfen nicht länger als für den betrieblichen Zeitraum erforderlich aufbewahrt werden, in jedem Fall nicht länger als 30 Tage, sofern dies nicht betrieblich begründet und dokumentiert ist — oder kürzer, falls im Dienstleistungsvertrag mit dem PII-Verantwortlichen eine kürzere Frist festgelegt ist
- **Automatisierter Löschung**: Protokoll-Aufbewahrungsrichtlinien müssen als automatisierte Löschungsregeln implementiert werden, nicht als manuelle Prozesse

## Mandantenisolierung im Mehrmandanten-Speicher

In Mehrmandanten-Umgebungen muss [Organisation] sicherstellen, dass temporärer Speicher, der der Verarbeitung eines PII-Verantwortlichen zugewiesen ist:

- Während der aktiven Verarbeitung von anderen Mandanten isoliert ist
- Vor der Neuzuweisung an einen anderen Mandanten oder eine andere Arbeitslast sicher gelöscht wird
- Prüfbar ist — Neuzuweisungsereignisse müssen protokolliert und zur Inspektion verfügbar sein

Dies wird im Detail in CLD-PII-POL-A.11 (§11.13 — Zugang zu Daten auf zuvor genutztem Datenspeicherplatz) behandelt. Mandantenisolierungstests müssen mindestens jährlich und nach wesentlichen Änderungen an der Speicherinfrastruktur durchgeführt werden.

## Verfahrensabdeckung

Verfahren zur Löschung temporärer Dateien müssen ausdrücklich abdecken:

- Sowohl persistenten Speicher (SSD, HDD, NVMe) als auch flüchtigen Speicher (Instance Store, Container-Ephemeral)
- Alle Compute-Schichten: Bare Metal, virtuelle Maschine, Container, Serverless-Funktion (Serverless-spezifische Löschungsüberlegungen, einschliesslich /tmp-Speicher und Layer-Caching, werden in den dienststufigen Löschungsverfahren behandelt)
- Alle geografischen Regionen, in denen [Organisation] Cloud-Infrastruktur betreibt

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB / Cloud Security Manager** | Verantwortlich für Standards zur Löschung temporärer Dateien; überprüft die Implementierung jährlich; eskaliert ungelöste Lücken an DSB und Geschäftsleitung |
| **Cloud Engineering** | Implementiert automatisierte Löschungsmechanismen in Dienst-Pipelines; stellt sicher, dass Protokoll-Minimerungskonfigurationen angewendet werden; testet die Löschungseffektivität |
| **Datenschutzbeauftragter (DSB)** | Überprüft Anonymisierungs-/Pseudonymisierungsbeurteilungen; bestätigt die Angemessenheit von Protokoll-Minimerungskonfigurationen; berät zu Speicherbegrenzungspflichten |
| **Sicherheitsbetrieb** | Überwacht auf anomale Datenremanenz-Ereignisse; reagiert auf Vorfälle, bei denen PII möglicherweise in temporärem Speicher verblieben sind |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| Verfahren zur Löschung temporärer Dateien | Dokumentierte Verfahren pro Dienst und Speichertyp mit angegebener Löschungsmethode | Aktuell + Vorgängerversionen für 3 Jahre |
| Aufzeichnungen zur automatisierten Löschungskonfiguration | Technische Konfigurationsaufzeichnungen, die die Implementierung der automatisierten Löschung belegen | Aktuell + 3 Jahre |
| Aufzeichnungen zur Protokoll-Minimerungskonfiguration | Dokumentierte Protokollkonfigurationen, die eine minimierende PII-Erfassung bestätigen | Aktuell + Vorgängerversionen für 3 Jahre |
| Aufzeichnungen zu Mandantenisolierungstests | Ergebnisse periodischer Tests, die keine mandantenübergreifende Datenremanenz bestätigen | 3 Jahre |
| DSB-Anonymisierungsüberprüfungen | Unterzeichnete DSB-Beurteilungen der auf PII der Verantwortlichen angewendeten Anonymisierungstechniken | Nutzungsdauer + 3 Jahre |

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-PII-POL-A.5 verifizieren, sollten Folgendes vorfinden:

- Dokumentierte Verfahren zur Löschung temporärer Dateien für alle relevanten Speichertypen und Compute-Schichten
- Technische Belege, dass die Löschung in Dienst-Pipelines automatisiert ist und nicht auf manuelle Schritte angewiesen ist
- Überprüfte und bestätigte Protokoll-Minimerungskonfigurationen, die unnötige PII ausschliessen
- Testergebnisse, die bestätigen, dass zwischen Mandanten neu zugewiesener Speicher keine verbleibenden PII aus vorheriger Mandantenverarbeitung enthält

---

<!-- QA_VERIFIED: 2026-03-29 -->

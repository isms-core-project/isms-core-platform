<!-- ISMS-CORE:POLICY:CLD-POL-A.7-DE:cloud:POL:a.7 -->
**CLD-POL-A.7 — Genauigkeit und Qualität**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Genauigkeit und Qualität |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-POL-A.7 |
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

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Änderungen der Dienstarchitektur)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: ISB / Cloud Security Manager
- Sekundär: Datenschutzbeauftragter (DSB)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII)
- CLD-POL-A.2 (Einwilligung und Wahlmöglichkeit — Kooperation bei Betroffenenrechten)
- CLD-POL-A.6 (Nutzungs-, Aufbewahrungs- und Offenlegungsbegrenzung)
- CLD-POL-A.9 (Individuelle Teilnahme und Zugang)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.7 (Genauigkeit und Qualität — Grundsatz)
- ISO/IEC 27701:2025 Kontrolle A.2.3.2 (Auftragsverarbeiter — Einhaltung von Pflichten gegenüber PII-Hauptbetroffenen, einschliesslich Berichtigungsunterstützung)
- DSGVO Artikel 5 Abs. 1 lit. d (Grundsatz der Richtigkeit); Artikel 16 (Recht auf Berichtigung); Artikel 28 Abs. 3 lit. e (Auftragsverarbeiter unterstützt bei Betroffenenrechten)
- CH DSG Artikel 6 Abs. 4 (Richtigkeit und Berichtigungspflichten); Artikel 9 Abs. 2 lit. c (Zusammenarbeit des Auftragsverarbeiters mit dem Verantwortlichen bei Betroffenenrechtsanfragen)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] als Public-Cloud-PII-Auftragsverarbeiter in Bezug auf Genauigkeit und Qualität fest — insbesondere die Pflicht, die Integrität der in Cloud-Systemen gespeicherten PII aufrechtzuerhalten, PII-Verantwortlichen Mechanismen zur Korrektur, Aktualisierung oder Löschung ungenauer PII bereitzustellen und eine Verschlechterung der Datenqualität durch Verarbeitungsvorgänge zu vermeiden — gemäss ISO/IEC 27018:2025 Annex A, Abschnitt A.7.

**Geltungsbereich**: Alle von [Organisation] im Auftrag von PII-Verantwortlichen gespeicherten oder verarbeiteten PII.

**Hinweis zum Grundsatz**: ISO/IEC 27018:2025 Annex A, Abschnitt A.7 ist ein Grundsatzabschnitt ohne zusätzliche Unterkontrollen über den Haupttext des Standards hinaus. Diese Richtlinie setzt den Grundsatz als operative Verpflichtung um. Die primäre Verantwortung für die PII-Genauigkeit liegt beim PII-Verantwortlichen; die Rolle von [Organisation] besteht darin, die Genauigkeit zu erhalten und nicht zu verschlechtern sowie dem Verantwortlichen Werkzeuge für deren Pflege bereitzustellen.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 — Abschnitt A.7

**Abschnitt A.7 — Genauigkeit und Qualität (Grundsatz)**

Abschnitt A.7 legt den Grundsatz fest, dass ein Public-Cloud-PII-Auftragsverarbeiter Kontrollen implementieren sollte, um die Genauigkeit und Vollständigkeit der im Auftrag von Verantwortlichen verarbeiteten PII zu erhalten, dem Verantwortlichen Mechanismen zur Korrektur oder Aktualisierung ungenauer PII bereitzustellen und eine Qualitätsverschlechterung durch Verarbeitungsvorgänge zu vermeiden.

## Was diese Richtlinie NICHT regelt

- Die Überprüfung der Genauigkeit von PII, die [Organisation] vom PII-Verantwortlichen bereitgestellt wird — die Genauigkeit der Quelldaten liegt in der Verantwortung des Verantwortlichen
- Datenqualitätsstandards für die eigene Verarbeitung des Verantwortlichen — das sind die Pflichten des Verantwortlichen gemäss DSGVO Artikel 5 Abs. 1 lit. d

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 5 Abs. 1 lit. d (Richtigkeit — PII müssen sachlich richtig und erforderlichenfalls auf dem neuesten Stand sein; unrichtige PII sind unverzüglich zu löschen oder zu berichtigen); Artikel 16 (Recht auf Berichtigung — der Verantwortliche muss dieses Recht ausüben können, was die Zusammenarbeit des Auftragsverarbeiters erfordert); Artikel 28 Abs. 3 lit. e (Auftragsverarbeiter unterstützt Verantwortlichen bei Betroffenenrechtspflichten)
- **CH DSG**: Artikel 6 Abs. 4 (Richtigkeit und Berichtigungspflichten); Artikel 9 Abs. 2 lit. c (Zusammenarbeit des Auftragsverarbeiters mit dem Verantwortlichen bei Betroffenenrechtsanfragen)
- **ISO/IEC 27018:2025**: Grundsatz Abschnitt A.7

---

# Richtlinienaussagen: Genauigkeit und Qualität (A.7)

## Wahrung der Datenintegrität

[Organisation] muss technische Kontrollen implementieren, die sicherstellen, dass in Cloud-Systemen gespeicherte PII durch Verarbeitungsvorgänge nicht verschlechtert, beschädigt oder verändert werden, es sei denn, dies ist vom PII-Verantwortlichen autorisiert. Insbesondere:

- Speichersysteme müssen Integritätsprüfungen (z. B. Prüfsummen, kryptografische Hashwerte) für PII-Datenspeicher implementieren, um unbefugte oder versehentliche Änderungen zu erkennen
- Transformationsvorgänge an PII während der Verarbeitung müssen, wo technisch durchführbar, reversibel sein; bei irreversiblen Transformationen muss der ursprüngliche PII-Zustand in einem separaten Datensatz oder Backup vor der Transformation bewahrt werden
- Backup- und Replikationsvorgänge müssen die Genauigkeit und Vollständigkeit der PII ohne Datenverlust erhalten

## Mechanismen zur Verantwortlichen-Korrektur

[Organisation] muss PII-Verantwortlichen technische Fähigkeiten zur Korrektur, Aktualisierung und Löschung von PII in Cloud-Speichern bereitstellen. Diese Mechanismen müssen:

- Feldebenen-Korrekturen oder vollständige Datensatzaktualisierungen für strukturierte PII-Datenspeicher ermöglichen
- Korrekturen innerhalb von 24 Stunden an aktive Replikate und Lesereplikate und innerhalb von 72 Stunden an Backup-Kopien propagieren, nach Anwendung der Korrektur — und in jedem Fall innerhalb der Frist, die der Verantwortliche zur Erfüllung seiner Betroffenenrechtspflichten benötigt
- Bei Abschluss von Korrekturen einen Bestätigungsdatensatz erstellen, der angibt, welche Datensätze geändert wurden und den Zeitstempel

## Qualitätsprüfungen

[Organisation] muss für PII-Datenspeicher folgende Qualitätskontrollen implementieren:

- **Datenvollständigkeitsprüfungen**: Datensätze mit fehlenden Pflichtfeldern identifizieren und kennzeichnen, die auf Datenbeschädigung oder unvollständige Übertragung hinweisen können
- **Datenkonsistenzprüfungen**: PII-Konsistenz über replizierte oder verteilte Datenspeicher hinweg verifizieren, um Replikationsfehler zu erkennen
- **Backup-Integritätsverifikation**: Backup-PII-Daten für kritische PII-Datenspeicher mindestens vierteljährlich wiederherstellen und verifizieren, um die Backup-Integrität zu bestätigen

Ergebnisse von Qualitätsprüfungen müssen protokolliert und vierteljährlich vom Cloud-Engineering-Team überprüft werden. Eine Zusammenfassung der vierteljährlichen Qualitätsprüfungsergebnisse muss auch dem DSB vorgelegt werden. Wesentliche Datenqualitätsprobleme — definiert als Probleme, die mehr als 1 % der Datensätze in einem Datenspeicher betreffen, oder jedes Problem, das möglicherweise eine Betroffenenrechtsentscheidung beeinflusst hat oder zur Offenlegung ungenauer PII gegenüber einem Dritten geführt hat — müssen dem PII-Verantwortlichen innerhalb von 3 Werktagen nach der Feststellung gemeldet werden. Wird ein Datenintegritätsfehler festgestellt, muss der Vorfall gemäss CLD-POL-A.11 (Informationssicherheit) eskaliert werden.

## Verarbeitungsbedingte Ungenauigkeit

Sofern [Organisation] im Auftrag eines Verantwortlichen Datentransformations-, Anreicherungs- oder Verarbeitungsvorgänge an PII durchführt, muss [Organisation]:

- Die Transformationslogik und ihre Auswirkungen auf die PII-Genauigkeit dokumentieren
- Eine Genehmigung des Verantwortlichen für jede Transformation einholen, die PII-Attribute modifiziert und nicht bereits durch den Dienstleistungsvertrag oder die dokumentierte Verarbeitungsbeschreibung abgedeckt ist
- Den Verantwortlichen benachrichtigen, wenn ein Verarbeitungsvorgang Ergebnisse liefert, die auf eine mögliche Ungenauigkeit in den Quelldaten hinweisen

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB / Cloud Security Manager** | Verantwortlich für Integritätskontrollen für PII-Datenspeicher; stellt sicher, dass Korrekturmechanismen funktionsfähig sind; beaufsichtigt das Qualitätsprüfprogramm |
| **Cloud Engineering** | Implementiert Integritätsprüfungen, Korrekturmechanismen und Qualitätsprüfprozesse; untersucht und löst Datenqualitätsprobleme |
| **Datenschutzbeauftragter (DSB)** | Berät zu Genauigkeitspflichten gemäss DSGVO und DSG; überprüft verantwortlichenseitige Fähigkeitsdokumentation; überwacht Datenqualitätsvorfallsmeldungen |
| **Cloud-Diensteerbringung** | Kommuniziert von Verantwortlichen gemeldete Genauigkeitsprobleme an Cloud Engineering; verfolgt die Lösung und bestätigt den Abschluss gegenüber dem Verantwortlichen |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| Integritätsprüfungs-Konfigurationsaufzeichnungen | Technische Dokumentation der Integritätsprüfmechanismen pro Datenspeicher | Aktuell + 3 Jahre |
| Dokumentation der Korrekturmechanismen | Beschreibung der PII-Korrektur-, Aktualisierungs- und Löschtools für Verantwortliche pro Dienst | Aktuell + Vorgängerversionen für 3 Jahre |
| Qualitätsprüfungsprotokolle | Vierteljährliche Qualitätsprüfungsergebnisse einschliesslich Vollständigkeit, Konsistenz und Backup-Verifikation | 3 Jahre |
| Aufzeichnungen zu Datenqualitätsvorfällen | Aufzeichnungen wesentlicher Datenqualitätsprobleme, Verantwortlichen-Benachrichtigungen und Lösungen | Vertragsdauer + 3 Jahre |

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-POL-A.7 verifizieren, sollten Folgendes vorfinden:

- Technische Dokumentation, die bestätigt, dass Integritätsprüfungen für PII-Datenspeicher implementiert sind
- Belege, dass PII-Verantwortliche innerhalb von Cloud-Diensten Zugang zu Korrektur-, Aktualisierungs- und Löschmechanismen haben
- Qualitätsprüfungsprotokolle für den Prüfungszeitraum mit dokumentierter Überprüfung
- Etwaige Datenqualitätsvorfälle, die den Verantwortlichen mit Lösungsbelegen gemeldet wurden

---

<!-- QA_VERIFIED: 2026-03-29 -->

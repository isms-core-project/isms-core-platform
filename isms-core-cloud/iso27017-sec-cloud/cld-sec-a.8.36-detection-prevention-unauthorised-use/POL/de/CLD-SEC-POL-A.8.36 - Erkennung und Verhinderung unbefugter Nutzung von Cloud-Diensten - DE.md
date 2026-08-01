<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.8.36-DE:sec:POL:a.8.36 -->
**CLD-SEC-POL-A.8.36 — Erkennung und Verhinderung unbefugter Nutzung von Cloud-Diensten**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Erkennung und Verhinderung unbefugter Nutzung von Cloud-Diensten |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-SEC-POL-A.8.36 |
| **Dokumentersteller** | ISB / Cloud Security Manager |
| **Dokumenteigentümer** | ISB |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Noch festzulegen] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |
| **Cloud-Produktversion** | 1.0 |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Noch festzulegen] | ISB | Erstversion für ISO/IEC 27017:2026 Ausg. 2 Implementierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Änderungen der Cloud-Nutzungsüberwachungsfähigkeit, oder nach einem bestätigten Vorfall unbefugter Nutzung)
**Nächstes Überprüfungsdatum**: [Datum des Inkrafttretens + 12 Monate]

**Genehmigungskette**:

- Primär: ISB
- Sekundär: Cloud Security Manager
- Technisch: Security Operations Lead
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-A.8.16 (Überwachungsaktivitäten — übergeordnete ISMS-Richtlinie)
- CLD-SEC-POL-A.5.38 (Gemeinsame Rollen und Verantwortlichkeiten in einer Cloud-Computing-Umgebung)
- CLD-SEC-POL-A.8.35 (Trennung in virtuellen Rechenumgebungen)
- CLD-SEC-IMP-A.8.36-TG (Erkennung und Verhinderung unbefugter Nutzung von Cloud-Diensten — Technischer Leitfaden, enthält die vollständigen Überwachungsschemata)
- CLD-SEC-REF-A.5-A.8 (Cloud-Sicherheits-Leitfadenanhang)
- ISO/IEC 27017:2026, Abschnitt 8.36 (CLD — Erkennung und Verhinderung unbefugter Nutzung von Cloud-Diensten)
- ISO/IEC 19086 (alle Teile) (Cloud Computing — Rahmenwerk für Service-Level-Agreements)

---

## Zusammenfassung

Diese Richtlinie legt fest, wie [Organisation] die Aktivitäten von Cloud-Service-Nutzenden (CSU) überwacht, um unbefugten Zugriff, unbeabsichtigte Datenübertragung und andere unbefugte Aktivitäten bei Cloud-Diensten zu erkennen und zu verhindern, gemäss ISO/IEC 27017:2026, Abschnitt 8.36.

**Geltungsbereich**: Alle Cloud-Dienste, die [Organisation] als Cloud-Service-Kunde (CSC) verwaltet, einschliesslich der Überwachung der eigenen Cloud-Service-Nutzenden von [Organisation]; sowie alle Cloud-Dienste, die [Organisation] als Cloud-Service-Anbieter (CSP) bereitstellt, einschliesslich der den CSC bereitgestellten Überwachungshinweise und -funktionen.

**Hinweis zu erweiterten Kontrollen**: ISO/IEC 27017:2026, Abschnitt 8.36 ist eine von vier cloudspezifischen erweiterten „CLD"-Kontrollen, die mit der zweiten Ausgabe des Standards eingeführt wurden (neben 5.38, 5.39 und 8.35). Sie ist vollständig neu — sie hat kein Äquivalent in der ersten Ausgabe 2015 von ISO/IEC 27017 und kein direktes Äquivalent in ISO/IEC 27002:2022. [Organisation] implementiert sie als informative Erweiterung ihres auf ISO/IEC 27001:2022 basierenden ISMS, neben der Kontrolle 8.16 im Annex A (Überwachungsaktivitäten).

**Kernrisiko**: Cloud-Dienste lassen sich leicht bereitstellen und ebenso leicht missbrauchen — ein einzelner CSU kann Schatteninfrastruktur schaffen, Daten über einen autorisierten Dienst auf unbefugte Weise exfiltrieren oder den vorgesehenen Zugriff überschreiten, ohne herkömmliche Netzwerk-Perimeterkontrollen auszulösen. Die Erkennung hängt von der Überwachung von Nutzungsmustern ab, nicht nur von der Überwachung externer Angriffe. Ein bestätigter Fall unbefugter Nutzung eines Cloud-Dienstes wird als Informationssicherheitsvorfall behandelt, eskaliert und gemäss dem Vorfallmanagementprozess von [Organisation] untersucht — nicht lediglich protokolliert und abgeschlossen.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27017:2026 — Abschnitt 8.36

**Kontrollaussage (ISO/IEC 27017:2026, 8.36):**
> „Die Nutzung von Cloud-Diensten durch die CSU sollte überwacht werden, um unbefugten Zugriff, Datenübertragung und andere Aktivitäten bei Cloud-Diensten zu verhindern."

**Zweck (ISO/IEC 27017:2026, 8.36):**
> „Ermöglichung der Überwachung und Verhinderung der unbeabsichtigten Nutzung von Cloud-Diensten sowie der unbeabsichtigten Datenübertragung zu und von Cloud-Diensten."

*(Arbeitsübersetzung des englischen Originaltextes der Norm zur besseren Lesbarkeit; bei Abweichungen ist der offizielle englische Text von ISO/IEC 27017:2026 massgebend.)*

## Anwendbarkeit

Diese Richtlinie gilt für:

- Alle Cloud-Service-Nutzenden (CSU) innerhalb von [Organisation], die im Auftrag von [Organisation] als CSC auf Cloud-Dienste zugreifen
- Alle Cloud-Dienste, die [Organisation] als CSP für ihre eigenen CSC bereitstellt, hinsichtlich der von [Organisation] bereitzustellenden Überwachungshinweise und -funktionen
- Alle Informationssicherheits-Ereignismanagementprozesse, die Cloud-Nutzungsdaten verarbeiten

## Regulatorischer und normativer Rahmen

ISO/IEC 27017:2026 ist eine informative Erweiterung von ISO/IEC 27002:2022. Abschnitt 8.36 entspricht keiner nummerierten Kontrolle von ISO/IEC 27002:2022; er ist neu in der zweiten Ausgabe 2026, ohne Äquivalent selbst in der ersten Ausgabe 2015 von ISO/IEC 27017. Er wird parallel zur Kontrolle 8.16 im Annex A von ISO/IEC 27001:2022 (Überwachungsaktivitäten) umgesetzt und stützt sich auf die SLA-Leitlinien der Reihe ISO/IEC 19086, sofern Cloud-SLA-Bedingungen die für [Organisation] verfügbaren Überwachungsdaten regeln.

---

# Richtlinienaussagen: Erkennung und Verhinderung unbefugter Cloud-Nutzung (8.36)

## Risikobasierte Geltungsbereichsfestlegung

Vor der Implementierung der Überwachung für einen bestimmten Cloud-Dienst muss [Organisation]:

- Die Datenklassifikation des Dienstes (Öffentlich / Intern / Vertraulich / Eingeschränkt) bestätigen, unter Verwendung der Erklärung der Trennungsanforderungen (CLD-SEC-IMP-A.8.35-TG, Abschnitt 1), sofern für den Dienst bereits eine solche existiert
- Die CSU-Aktivitätsüberwachung als verbindliche Mindestanforderung für als Vertraulich oder Eingeschränkt klassifizierte Cloud-Dienste anwenden
- Für als Öffentlich oder Intern klassifizierte Dienste eine risikobasierte Empfehlung (überwachen oder nicht, und weshalb) zur Genehmigung durch den ISB erstellen und die Entscheidung dokumentieren — Überwachung wird nicht standardmässig ausgelassen, sondern ist eine dokumentierte Entscheidung

## Pflichten als Cloud-Service-Kunde (CSC)

Wenn [Organisation] als Cloud-Service-Kunde handelt, muss [Organisation] für jeden im Geltungsbereich liegenden Cloud-Dienst:

- Die Überwachung der Aktivitäten der CSU implementieren, wobei mindestens Authentifizierungsereignisse, Ressourcenbereitstellung/-freigabe, Datenzugriff und Konfigurationsänderungen erfasst und – soweit möglich – an die zentrale Sicherheitsüberwachungsfunktion von [Organisation] gemäss ISMS-POL-A.8.16 weitergeleitet werden
- Eine periodische technische Compliance-Überprüfung gegenüber der Informationssicherheitsrichtlinie von [Organisation], ihrer themenspezifischen Richtlinie zur Nutzung von Cloud-Diensten sowie einschlägigen Regeln und Standards durchführen — mindestens jährlich für Vertrauliche oder Eingeschränkte Dienste — wobei nicht konforme Feststellungen zur Nachverfolgung der Behebung an den Cloud Security Manager eskaliert werden
- Unbeabsichtigte oder unbefugte Informationsübertragung zu und von der durch [Organisation] verwalteten Cloud-Dienstumgebung überwachen und verhindern, unter Einsatz verfügbarer technischer Kontrollen (z. B. Data-Loss-Prevention-Integration, eingeschränkte Freigabeeinstellungen, Egress-Überwachung)
- Für jeden überwachten Dienst eine Baseline der normalen Cloud-Dienstnutzung etablieren und Anomalien — wie zunehmende Ressourcennutzung oder unbekannte Dienstnutzung — durch Erkennung von Abweichungen von dieser Baseline feststellen
- Jede ausgelöste Anomalie-Warnung untersuchen und deren Einstufung dokumentieren (Fehlalarm, bestätigte unbefugte Nutzung, behoben, an die Vorfallreaktion eskaliert); eine bestätigte unbefugte Nutzung als Informationssicherheitsvorfall behandeln

## Pflichten als Cloud-Service-Anbieter (CSP)

Wenn [Organisation] als Cloud-Service-Anbieter handelt, muss [Organisation]:

- CSC Hinweise und Funktionen bereitstellen, die es ihnen ermöglichen, die Nutzung des von [Organisation] bereitgestellten Cloud-Dienstes durch ihre CSU zu überwachen und zu kontrollieren — mit Dokumentation, welche Aktivitätsdaten offengelegt werden, wie CSC darauf zugreifen können, und wie etwaige konfigurierbare Überwachungsfunktionen (z. B. benutzerdefinierte Warnschwellen) eingerichtet werden
- Diese CSC-gerichteten Überwachungshinweise mit der Weiterentwicklung des Dienstes aktuell halten und sie mindestens im Rahmen der jährlichen Richtlinienüberprüfung überprüfen

## Kommunikation und Sensibilisierung

[Organisation] muss den Überwachungsumfang, die Verantwortlichkeiten der CSU, die Regeln zur zulässigen Nutzung sowie die Meldeverfahren für vermutete unbefugte Nutzung den internen CSU und relevanten Teams kommunizieren, über das Informationssicherheits-Sensibilisierungsprogramm der Organisation (siehe ISMS-POL-A.6.3) und dienstspezifische Einführungsunterlagen. Wo [Organisation] als CSP handelt, müssen entsprechende Informationen den Kunden-CSU über die veröffentlichten CSC-gerichteten Überwachungshinweise kommuniziert werden.

## Protokoll der Überwachungsumfang-Entscheidungen — Mindestinhalt

Das Protokoll der Überwachungsumfang-Entscheidungen (vollständiges Schema in CLD-SEC-IMP-A.8.36-TG, Abschnitt 1) muss je Cloud-Dienst erfassen: die Dienstkennung; dessen Datenklassifikation; die Überwachungsentscheidung (verbindlich, risikobasiert umgesetzt, oder risikobasiert nicht umgesetzt); die Begründung und, sofern zutreffend, die Genehmigung des ISB; sowie das Datum der letzten Überprüfung.

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **ISB** | Ist Eigentümer von CLD-SEC-POL-A.8.36; genehmigt die risikobasierte Geltungsbereichsfestlegung der Überwachung für niedriger klassifizierte Cloud-Dienste; prüft Anomalie-Eskalationen mit organisationsweiter Auswirkung; verantwortet bestätigte Vorfälle unbefugter Nutzung über den Vorfallmanagementprozess von [Organisation] |
| **Security Operations Lead** | Implementiert und betreibt die CSU-Aktivitätsüberwachung, die technische Compliance-Überprüfung und die Anomalieerkennung (CSC-Rolle); berichtet dem ISB Kennzahlen zu Überwachungsabdeckung und Anomalien |
| **Cloud Security Manager** | Stellt sicher, dass die CSC-gerichteten Überwachungshinweise und -funktionen dokumentiert und verfügbar sind, wo [Organisation] als CSP auftritt; dokumentiert risikobasierte Geltungsbereichsentscheidungen |
| **Cloud-Diensteerbringung / Engineering** | Konfiguriert Cloud-Dienst-Überwachungsfähigkeiten; reagiert auf festgestellte unbeabsichtigte oder unbefugte Informationsübertragung |
| **Alle Mitarbeitenden (als CSU)** | Nutzen Cloud-Dienste nur innerhalb des autorisierten Umfangs; melden vermutete unbefugte Nutzung, die sie beobachten |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Verantwortlich | Aufbewahrungsdauer |
|----------|-------------|-----------------|---------------------|
| Protokoll der Überwachungsumfang-Entscheidungen | Vom ISB genehmigte risikobasierte Entscheidungen für Öffentliche/Interne Dienste, bei denen keine Überwachung implementiert ist | Cloud Security Manager | Aktuell + 3 Jahre |
| Konfiguration der CSU-Aktivitätsüberwachung | Dokumentation des Überwachungsumfangs und der Mechanismen je Cloud-Dienst (CSC-Rolle) | Security Operations Lead | Aktuelle Version + Vorgängerversionen für 3 Jahre |
| Nachweise der technischen Compliance-Überprüfung | Nachweise periodischer Überprüfungen gegenüber der Informationssicherheitsrichtlinie, der Cloud-Nutzungsrichtlinie und Standards | Security Operations Lead | Aktuell + 3 Jahre |
| Anomalie-Erkennungsprotokoll | Protokoll erkannter Anomalien (unerwartete Ressourcennutzung, unbekannte Dienstnutzung) und deren Einstufung | Security Operations Lead | Aktuell + 3 Jahre |
| Nachweise bestätigter unbefugter Nutzung / Vorfälle | Nachweise von als unbefugte Nutzung bestätigten Anomalien, verknüpft mit dem Vorfallmanagementprozess | ISB | Aktuell + 3 Jahre |
| CSC-gerichtete Überwachungshinweise (CSP-Rolle) | Den CSC bereitgestellte Dokumentation und Funktionen zur Überwachung und Kontrolle der Nutzung durch ihre eigenen CSU | Cloud Security Manager | Aktuelle Version + Vorgängerversionen für 3 Jahre |

---

# Überwachung und Kennzahlen

Der Security Operations Lead berichtet dem ISB mindestens vierteljährlich:

- Den Anteil der Vertraulichen/Eingeschränkten Cloud-Dienste mit aktiver CSU-Überwachung
- Die Anzahl der erkannten Anomalien und deren Einstufungsverteilung (Fehlalarm / bestätigte unbefugte Nutzung / behoben / eskaliert)
- Die Anzahl der Feststellungen aus der technischen Compliance-Überprüfung und deren Behebungsstatus
- Die Zeit von der Anomalieerkennung bis zur Einstufung, bei als unbefugte Nutzung bestätigten Anomalien

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-SEC-POL-A.8.36 verifizieren, sollten Folgendes vorfinden:

- Einen dokumentierten Umfang der CSU-Aktivitätsüberwachung für jeden als Vertraulich oder Eingeschränkt klassifizierten Cloud-Dienst
- Nachweise periodischer technischer Compliance-Überprüfung gegenüber der Informationssicherheitsrichtlinie und der Cloud-Nutzungsrichtlinie
- Ein Anomalie-Erkennungsprotokoll, das eine aktive Überprüfung und Nachverfolgung der Einstufung belegt, nicht nur passive Protokollsammlung
- Für Dienste, bei denen [Organisation] als CSP auftritt, veröffentlichte Überwachungshinweise und den CSC zur Verfügung gestellte Funktionen
- Eine dokumentierte Genehmigung des ISB, wo die Überwachung für niedriger klassifizierte Dienste risikobasiert reduziert wurde
- Belege, dass bestätigte Feststellungen unbefugter Nutzung über den Vorfallmanagementprozess von [Organisation] bearbeitet wurden, mit einer Aufzeichnung der Zeit bis zur Einstufung

---

<!-- QA_VERIFIED: 2026-08-01 -->

<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.5.38-DE:sec:POL:a.5.38 -->
**CLD-SEC-POL-A.5.38 — Gemeinsame Rollen und Verantwortlichkeiten in einer Cloud-Computing-Umgebung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Gemeinsame Rollen und Verantwortlichkeiten in einer Cloud-Computing-Umgebung |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-SEC-POL-A.5.38 |
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

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Änderungen des Cloud-Dienstmodells oder der Lieferantenbeziehungen, oder nach einem Vorfall oder einer Streitigkeit im Zusammenhang mit gemeinsamer Verantwortung)
**Nächstes Überprüfungsdatum**: [Datum des Inkrafttretens + 12 Monate]

**Genehmigungskette**:

- Primär: ISB
- Sekundär: Cloud Security Manager
- Compliance: Rechts-/Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-A.5.1-2-6.1-2 (Sicheres Beschäftigungsverhältnis und Rollen — übergeordnete ISMS-Richtlinie für Rollen und Verantwortlichkeiten gemäss A.5.2)
- ISMS-POL-A.5.19-23-S5 (Cloud-Dienste-Sicherheit — übergeordnete ISMS-Cloud-Richtlinie)
- CLD-SEC-POL-A.5.39 (Vereinbarung über Rollen und Verantwortlichkeiten des Cloud-Service-Partners — regelt die Weitergabe dieser Verantwortlichkeiten an Cloud-Service-Partner)
- CLD-SEC-POL-A.8.35 (Trennung in virtuellen Rechenumgebungen)
- CLD-SEC-POL-A.8.36 (Erkennung und Verhinderung unbefugter Nutzung von Cloud-Diensten)
- CLD-SEC-IMP-A.5.38-TG (Gemeinsame Rollen und Verantwortlichkeiten — Technischer Leitfaden, enthält das vollständige Schema der Matrix der gemeinsamen Verantwortung)
- CLD-SEC-REF-A.5-A.8 (Cloud-Sicherheits-Leitfadenanhang)
- ISO/IEC 27017:2026, Abschnitt 5.38 (CLD — Gemeinsame Rollen und Verantwortlichkeiten in einer Cloud-Computing-Umgebung)
- ISO/IEC 27002:2022 (Informationssicherheitsmassnahmen)
- ISO/IEC 22123-3 (Cloud Computing — Referenzarchitektur)

---

## Zusammenfassung

Diese Richtlinie legt fest, wie [Organisation] Rollen und Verantwortlichkeiten im Bereich der Informationssicherheit in jeder Cloud-Computing-Beziehung, an der sie beteiligt ist, zuweist, dokumentiert, kommuniziert und umsetzt, gemäss ISO/IEC 27017:2026, Abschnitt 5.38.

**Geltungsbereich**: Alle Cloud-Dienste, an denen [Organisation] beteiligt ist — sei es als Cloud-Service-Kunde (CSC), der einen Cloud-Dienst eines Drittanbieters nutzt, oder als Cloud-Service-Anbieter (CSP), der einen Cloud-Dienst für seine eigenen Kunden bereitstellt. Wenn [Organisation] beide Rollen gleichzeitig innehat (zum Beispiel, wenn sie auf der Infrastruktur eines CSP aufbaut, um ihren eigenen Cloud-Dienst bereitzustellen), gilt diese Richtlinie für jede Rolle unabhängig. Sie umfasst öffentliche, private, hybride und Multi-Cloud-Bereitstellungen über die Modelle IaaS, PaaS und SaaS, einschliesslich gestufter Beziehungen, bei denen sich Verantwortlichkeiten entlang einer Lieferkette fortsetzen.

**Hinweis zu erweiterten Kontrollen**: ISO/IEC 27017:2026, Abschnitt 5.38 ist eine von vier cloudspezifischen erweiterten „CLD"-Kontrollen, die mit der zweiten Ausgabe des Standards eingeführt wurden (neben 5.39, 8.35 und 8.36) und die kein direktes Äquivalent in ISO/IEC 27002:2022 oder im Annex A von ISO/IEC 27001:2022 haben. [Organisation] implementiert sie als informative Erweiterung ihres auf ISO/IEC 27001:2022 basierenden ISMS, im Einklang damit, wie ISO/IEC 27017:2026 diese Kontrollen selbst einordnet.

**Grundprinzip**: Informationssicherheit im Cloud Computing liegt nie ausschliesslich in der Verantwortung des CSP oder ausschliesslich in der des CSC — sie wird geteilt, und die geteilte Zuweisung muss von beiden Parteien identifiziert, dokumentiert, kommuniziert und umgesetzt werden, bevor sie als verlässlich gelten kann. Unklarheit in dieser Zuweisung wird als Informationssicherheitsrisiko behandelt, nicht als eine später zu klärende Formalität.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27017:2026 — Abschnitt 5.38

**Kontrollaussage (ISO/IEC 27017:2026, 5.38):**
> „Verantwortlichkeiten für gemeinsame Informationssicherheitsrollen bei der Nutzung des Cloud-Dienstes sollten identifizierten Parteien zugewiesen, dokumentiert, kommuniziert und sowohl vom CSC als auch vom CSP umgesetzt werden."

**Zweck (ISO/IEC 27017:2026, 5.38):**
> „Klärung der Beziehung hinsichtlich gemeinsamer Rollen und Verantwortlichkeiten zwischen dem CSC und dem CSP für das Informationssicherheitsmanagement."

*(Arbeitsübersetzung des englischen Originaltextes der Norm zur besseren Lesbarkeit; bei Abweichungen ist der offizielle englische Text von ISO/IEC 27017:2026 massgebend.)*

## Anwendbarkeit

Diese Richtlinie gilt für:

- Alle Cloud-Dienste, die [Organisation] als Cloud-Service-Kunde (CSC) nutzt, über alle Bereitstellungsmodelle (öffentlich, privat, hybrid, Multi-Cloud) und Dienstmodelle (IaaS, PaaS, SaaS) hinweg
- Alle Cloud-Dienste, die [Organisation] als Cloud-Service-Anbieter (CSP) für ihre eigenen Kunden bereitstellt
- Alle Mitarbeitenden, die an der Auswahl, Konfiguration, dem Betrieb oder der Bereitstellung von Cloud-Diensten im Auftrag von [Organisation] beteiligt sind

## Regulatorischer und normativer Rahmen

ISO/IEC 27017:2026 ist eine informative Erweiterung von ISO/IEC 27002:2022 und liefert cloudspezifische Hinweise für Kontrollen, die die Organisation bereits im Rahmen ihres auf ISO/IEC 27001:2022 basierenden ISMS umsetzt. Abschnitt 5.38 entspricht keiner nummerierten Kontrolle von ISO/IEC 27002:2022; es handelt sich um eine neue Kontrolle, die mit der zweiten Ausgabe 2026 eingeführt wurde und thematisch am ehesten den Pflichten zu Rollen und Verantwortlichkeiten der Kontrolle 5.2 im Annex A von ISO/IEC 27001:2022 entspricht — und parallel dazu umgesetzt wird.

---

# Richtlinienaussagen: Gemeinsame Rollen und Verantwortlichkeiten (5.38)

## Pflichten als Cloud-Service-Kunde (CSC)

Wenn [Organisation] als Cloud-Service-Kunde handelt, muss [Organisation]:

- Die vom CSP vorgeschlagene Zuweisung von Rollen und Verantwortlichkeiten im Bereich Informationssicherheit während der Dienstauswahl und -einführung einholen und diese vor der Produktivsetzung des Dienstes anhand der eigenen Fähigkeiten und Risikobereitschaft von [Organisation] prüfen
- Sicherstellen, dass die Informationssicherheitsrollen und -verantwortlichkeiten sowohl von [Organisation] als auch vom CSP in einer schriftlichen Vereinbarung festgehalten werden — nicht allein der öffentlichen Dokumentation des CSP überlassen, die sich ohne Vorankündigung ändern kann
- Eine benannte Kontaktperson innerhalb der Kundensupportfunktion des CSP für die Eskalation von Informationssicherheitsangelegenheiten identifizieren und pflegen
- Vom CSP Informationen zu dessen Informationssicherheitsfähigkeiten anfordern — einschliesslich Authentifizierung, Kryptografie, Backup und Protokollierung — und Rahmenwerke Dritter oder unabhängiger Stellen (z. B. Umfang der ISO/IEC 27001-Zertifizierung, SOC-2-Bericht, CSA-STAR-Eintrag) nutzen, um diese Informationen zu ergänzen, wenn die Angaben des CSP unzureichend sind
- Jede Lücke zwischen der vom CSP vorgeschlagenen Zuweisung und der Fähigkeit von [Organisation], ihre eigenen zugewiesenen Verantwortlichkeiten zu erfüllen, als Informationssicherheitsrisiko bewerten und in den dokumentierten Risikobeurteilungs- und Behandlungsprozess von [Organisation] einbringen, sofern sie vor der Inbetriebnahme nicht geschlossen werden kann
- Das Bewusstsein der Mitarbeitenden für die vereinbarte Zuweisung bei den von ihnen genutzten Cloud-Diensten durch das Informationssicherheits-Sensibilisierungsprogramm der Organisation (siehe ISMS-POL-A.6.3) und die Einbindung in die Überprüfung der Cloud-Architektur aufrechterhalten

## Pflichten als Cloud-Service-Anbieter (CSP)

Wenn [Organisation] als Cloud-Service-Anbieter handelt, muss [Organisation]:

- Die Zuweisung von Informationssicherheitsrollen und -verantwortlichkeiten definieren und dokumentieren, die ihre CSC, [Organisation] selbst und die eigenen Lieferanten oder Cloud-Service-Partner von [Organisation] jeweils umsetzen sollen
- Die Zuweisung gegenüber potenziellen und bestehenden CSC vor Vertragsabschluss und nach jeder wesentlichen Änderung kommunizieren — über die Dienstvereinbarung, kundengerichtete Sicherheitsdokumentation oder Einführungsunterlagen, je nach Angemessenheit für den Dienst
- Die Beziehung zu jedem CSC hinsichtlich Informationssicherheitsfragen aufbauen und pflegen, einschliesslich eines definierten, in der Vereinbarung dokumentierten Eskalationswegs
- CSC Informationen zu den Informationssicherheitsfähigkeiten des Cloud-Dienstes und den von [Organisation] getroffenen Informationssicherheitsmassnahmen bereitstellen, in einem Grad an Klarheit, der es dem CSC ermöglicht, diese angemessen zu verstehen — unter Nutzung anerkannter Rahmenwerke Dritter oder unabhängiger Stellen, sofern dies zur Vermittlung dieser Informationen hilfreich ist
- Wo der Dienst auf einem zugrundeliegenden CSP beruht (eine gestufte Beziehung oder Lieferkettenbeziehung), bewerten und dokumentieren, wie sich Verantwortlichkeiten fortsetzen, und die Konsistenz mit den Vereinbarungen sicherstellen, die [Organisation] mit ihren eigenen Cloud-Service-Partnern gemäss CLD-SEC-POL-A.5.39 hält
- Eine Streitigkeit oder anhaltende Unklarheit bezüglich der Verantwortungszuweisung, die von einem CSC vorgebracht oder intern festgestellt wird, als eskalationsbedürftiges Informationssicherheitsereignis behandeln, nicht als routinemässige Supportanfrage

## Grundsatz der gemeinsamen Zuweisung

Rollen und Verantwortlichkeiten im Cloud Computing werden typischerweise zwischen dem CSC und dem CSP aufgeteilt. [Organisation] muss bei der Zuweisung von Rollen und Verantwortlichkeiten in beiden Eigenschaften die Daten des CSC und die Anwendungen des CSC berücksichtigen, für die [Organisation] (als CSP) Verwahrer ist, oder für die [Organisation] (als CSC) trotz der technischen Verwahrung durch den CSP verantwortlich bleibt.

## Matrix der gemeinsamen Verantwortung — Mindestinhalt

Jede Cloud-Dienst-Beziehung im Geltungsbereich dieser Richtlinie muss durch eine aktuelle Matrix der gemeinsamen Verantwortung gestützt werden. Die Matrix erfasst mindestens, je Verantwortungsbereich (z. B. Authentifizierung, Kryptografie, Backup, Protokollierung, Patch-Management, Netzwerksegmentierung): welcher Partei er zugewiesen ist (CSC, CSP oder gemeinsam); welche Massnahme jede Partei zur Erfüllung ihres Anteils ergreifen muss; ob [Organisation] bestätigt hat, dass sie ihren eigenen zugewiesenen Anteil erfüllen kann; und das Datum der letzten Überprüfung. Das vollständige Schema wird in CLD-SEC-IMP-A.5.38-TG, Abschnitt 1, geführt. Die Matrix muss vom Cloud Security Manager vor der Produktivsetzung einer neuen Cloud-Dienst-Beziehung und danach mindestens jährlich überprüft werden.

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **ISB** | Ist Eigentümer von CLD-SEC-POL-A.5.38; genehmigt die Zuweisung gemeinsamer Verantwortung für strategische oder risikoreiche Cloud-Dienst-Beziehungen; eskaliert ungelöste Zuweisungslücken an die Geschäftsleitung; prüft die Wirksamkeit der Richtlinie bei der Managementbewertung |
| **Cloud Security Manager** | Prüft die vom CSP bereitgestellte Rollen-/Verantwortlichkeitsdokumentation für genutzte Dienste (CSC-Rolle); erstellt und pflegt die CSC gegenüber veröffentlichte Rollen-/Verantwortlichkeitsdokumentation für bereitgestellte Dienste (CSP-Rolle); pflegt die Matrix der gemeinsamen Verantwortung für jede aktive Beziehung; berichtet dem ISB Kennzahlen zu Zuweisungslücken und Matrixabdeckung |
| **Rechts-/Compliance-Beauftragter** | Stellt sicher, dass die vereinbarte Zuweisung von Rollen und Verantwortlichkeiten in der schriftlichen Vereinbarung mit jeder CSC- oder CSP-Gegenpartei abgebildet ist |
| **Cloud-Diensteerbringung / Engineering** | Setzt die technischen Kontrollen um, die den [Organisation] zugewiesenen Verantwortlichkeiten entsprechen; eskaliert jede Verantwortlichkeit, die [Organisation] nicht erfüllen kann |
| **Alle Mitarbeitenden** | Handeln nur innerhalb der ihrer Funktion zugewiesenen Rollen und Verantwortlichkeiten; melden jede Unklarheit bei der Zuweisung gemeinsamer Verantwortung an den Cloud Security Manager |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Verantwortlich | Aufbewahrungsdauer |
|----------|-------------|-----------------|---------------------|
| Matrix der gemeinsamen Verantwortung | Je Cloud-Dienst-Beziehung, dokumentiert, welche Sicherheitsverantwortlichkeiten bei [Organisation] und welche bei der Gegenpartei (CSC oder CSP) liegen, gemäss obigem Mindestinhalt | Cloud Security Manager | Aktuell + 3 Jahre nach Ende der Beziehung |
| Vereinbarungsklauseln | Auszug aus der schriftlichen Vereinbarung mit den vereinbarten Rollen und Verantwortlichkeiten | Rechts-/Compliance-Beauftragter | Dauer der Vereinbarung + 3 Jahre |
| Überprüfungs- und Freigabenachweise | Nachweise, dass die Matrix vor der Produktivsetzung aktiv überprüft und genehmigt wurde, nicht passiv akzeptiert | Cloud Security Manager | Aktuell + 3 Jahre |
| CSP-Fähigkeitsangaben (CSC-Rolle) | Nachweise der von CSP angeforderten und bereitgestellten Informationen zu deren Sicherheitsfähigkeiten | Cloud Security Manager | Aktuell + 3 Jahre |
| CSC-gerichtete Fähigkeitsdokumentation (CSP-Rolle) | CSC gegenüber veröffentlichte Dokumentation der Sicherheitsfähigkeiten und -massnahmen von [Organisation] | Cloud Security Manager | Aktuelle Version + Vorgängerversionen für 3 Jahre |
| Zuweisungslücken-/Risikonachweise | Nachweise jeder in den Risikobeurteilungs- und Behandlungsprozess eskalierten Zuweisungslücke, mit Lösung | ISB | Aktuell + 3 Jahre |

> **Aufbewahrungsgrundlage**: Die 3-Jahres-Zeiträume entsprechen dem in der gesamten ISMS-Core-Cloud-Produktreihe verwendeten Aufbewahrungsansatz für vertrags- und vereinbarungsbezogene Nachweise.

---

# Überwachung und Kennzahlen

Der Cloud Security Manager berichtet dem ISB mindestens vierteljährlich:

- Den Anteil aktiver Cloud-Dienst-Beziehungen (CSC- und CSP-Rollen) mit einer aktuellen, überprüften Matrix der gemeinsamen Verantwortung
- Die Anzahl der identifizierten und in den Risikobeurteilungs- und Behandlungsprozess eskalierten Zuweisungslücken sowie deren Lösungsstatus
- Die Anzahl der von CSC oder internen Teams vorgebrachten Streitigkeiten oder Unklarheiten bezüglich der Verantwortungszuweisung

Die Wirksamkeit dieser Richtlinie wird im Rahmen der Managementbewertung sowie nach jedem cloudbezogenen Sicherheitsvorfall bewertet, bei dem die Zuweisung gemeinsamer Verantwortung für die Ursachenanalyse relevant ist.

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-SEC-POL-A.5.38 verifizieren, sollten Folgendes vorfinden:

- Eine Matrix der gemeinsamen Verantwortung für jede aktive Cloud-Dienst-Beziehung, in der CSC- oder CSP-Rolle, die den obigen Mindestinhaltsanforderungen entspricht
- Schriftliche Vereinbarungen, welche die Zuweisung von Informationssicherheitsrollen und -verantwortlichkeiten festlegen, statt sie nur zu implizieren
- Belege, dass [Organisation] als CSC die von CSP vorgeschlagene Zuweisung aktiv geprüft und bestätigt hat, statt sie standardmässig zu akzeptieren
- Belege, dass [Organisation] als CSP ihre Zuweisung proaktiv dokumentiert und an CSC kommuniziert hat, statt abzuwarten, bis CSC danach fragen
- Belege, dass Zuweisungslücken in den Risikobeurteilungs- und Behandlungsprozess eingebracht wurden, nicht nur vermerkt und offengelassen
- Vierteljährliche Überwachungskennzahlen, die eine aktive Überwachung der Matrixabdeckung belegen, keine einmalige Übung

---

<!-- QA_VERIFIED: 2026-08-01 -->

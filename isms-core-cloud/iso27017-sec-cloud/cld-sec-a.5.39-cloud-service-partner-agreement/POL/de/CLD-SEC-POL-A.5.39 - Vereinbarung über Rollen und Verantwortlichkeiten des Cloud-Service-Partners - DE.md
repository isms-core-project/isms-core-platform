<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.5.39-DE:sec:POL:a.5.39 -->
**CLD-SEC-POL-A.5.39 — Vereinbarung über Rollen und Verantwortlichkeiten des Cloud-Service-Partners**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Vereinbarung über Rollen und Verantwortlichkeiten des Cloud-Service-Partners |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-SEC-POL-A.5.39 |
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

**Überprüfungszyklus**: Jährlich (oder bei Aufnahme/Wechsel eines Cloud-Service-Partners, oder nach einer Eskalation aufgrund eines Geltungsbereichskonflikts)
**Nächstes Überprüfungsdatum**: [Datum des Inkrafttretens + 12 Monate]

**Genehmigungskette**:

- Primär: ISB
- Sekundär: Cloud Security Manager
- Compliance: Rechts-/Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- CLD-SEC-POL-A.5.38 (Gemeinsame Rollen und Verantwortlichkeiten in einer Cloud-Computing-Umgebung — die CSC/CSP-Zuweisung, mit der diese Richtlinie konsistent bleiben muss)
- ISMS-POL-A.5.19-23-S1 (Grundlagen der Lieferantenbeziehung)
- ISMS-POL-A.5.19-23-S2 (Anforderungen an Lieferantenvereinbarungen)
- ISMS-POL-A.5.19-23-S5 (Cloud-Dienste-Sicherheit)
- CLD-SEC-IMP-A.5.39-TG (Vereinbarung über Rollen und Verantwortlichkeiten des Cloud-Service-Partners — Technischer Leitfaden, enthält das vollständige CSN-Rollenregister und die Konsistenzprüfungsschemata)
- CLD-SEC-REF-A.5-A.8 (Cloud-Sicherheits-Leitfadenanhang)
- ISO/IEC 27017:2026, Abschnitt 5.39 (CLD — Vereinbarung über Rollen und Verantwortlichkeiten des Cloud-Service-Partners)
- ISO/IEC 22123-3 (Cloud Computing — Referenzarchitektur)

---

## Zusammenfassung

Diese Richtlinie legt fest, wie [Organisation] die Informationssicherheitsrollen und -verantwortlichkeiten jedes **Cloud-Service-Partners (CSN)**, den sie beauftragt oder von dem sie beauftragt wird, klassifiziert, definiert und vereinbart, gemäss ISO/IEC 27017:2026, Abschnitt 5.39.

**Geltungsbereich**: Alle Cloud-Service-Partner — Dritte, deren Tätigkeiten die Rolle von [Organisation] als Cloud-Service-Kunde (CSC), die Rolle von [Organisation] als Cloud-Service-Anbieter (CSP) oder beide unterstützen oder ergänzen. Gemäss ISO/IEC 22123-3 fallen die Tätigkeiten eines CSN typischerweise in eine oder mehrere von drei Unterrollen: Cloud-Service-Entwickler, Cloud-Auditor und Cloud-Service-Broker.

**Hinweis zu erweiterten Kontrollen**: ISO/IEC 27017:2026, Abschnitt 5.39 ist eine von vier cloudspezifischen erweiterten „CLD"-Kontrollen, die mit der zweiten Ausgabe des Standards eingeführt wurden (neben 5.38, 8.35 und 8.36). Sie ist vollständig neu — sie hat kein Äquivalent in der ersten Ausgabe 2015 von ISO/IEC 27017 und kein direktes Äquivalent in ISO/IEC 27002:2022. [Organisation] implementiert sie als informative Erweiterung ihres auf ISO/IEC 27001:2022 basierenden ISMS.

**Bezug zu CLD-SEC-POL-A.5.38**: Der CSC und der CSP haben bereits gemäss CLD-SEC-POL-A.5.38 gemeinsame Rollen und Verantwortlichkeiten untereinander. Jede von [Organisation] mit einem Cloud-Service-Partner getroffene Vereinbarung muss mit dieser bereits bestehenden gemeinsamen Zuweisung konsistent sein — eine CSN-Vereinbarung kann keine Verantwortlichkeit vom CSC oder CSP wegverlagern, ohne die Zustimmung beider. Eine CSN-Beauftragung, die eine solche Neuzuweisung schaffen würde, wird als Informationssicherheitsrisiko behandelt, das vor Unterzeichnung eskaliert werden muss, nicht als eine nachträglich zu klärende Angelegenheit.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27017:2026 — Abschnitt 5.39

**Kontrollaussage (ISO/IEC 27017:2026, 5.39):**
> „Informationssicherheitsrollen und -verantwortlichkeiten des CSN sollten mit dem CSC oder CSP, der den Dienst des CSN nutzt, definiert und vereinbart werden."

**Zweck (ISO/IEC 27017:2026, 5.39):**
> „Abgrenzung der Rollen und Verantwortlichkeiten des CSC und des CSP bei Nutzung eines CSN."

*(Arbeitsübersetzung des englischen Originaltextes der Norm zur besseren Lesbarkeit; bei Abweichungen ist der offizielle englische Text von ISO/IEC 27017:2026 massgebend.)*

## Unterrollen des Cloud-Service-Partners (gemäss ISO/IEC 22123-3)

| Unterrolle | Beschreibung | Typische Beispiele für [Organisation] |
|------------|-------------|-------------------------------------------|
| **Cloud-Service-Entwickler** | Entwirft, entwickelt, testet oder wartet Komponenten, die zur Bereitstellung eines Cloud-Dienstes verwendet werden | Beauftragtes Engineering-Unternehmen, das ein in einem bereitgestellten Dienst verwendetes Modul erstellt; Anbieter einer verwalteten CI/CD-Pipeline |
| **Cloud-Auditor** | Führt eine unabhängige Bewertung des Betriebs, der Kontrollen oder der Compliance eines Cloud-Dienstes durch | Externer ISO/IEC-27001- oder SOC-2-Auditor; unabhängiges Unternehmen für Penetrationstests |
| **Cloud-Service-Broker** | Verwaltet die Nutzung, Leistung oder Bereitstellung von Cloud-Diensten und verhandelt Beziehungen zwischen CSC und CSP | Cloud-Reseller; Managed-Service-Anbieter, der mehrere CSP im Auftrag von [Organisation] bündelt |

Ein CSN kann eine einzelne Unterrolle, mehrere Unterrollen innehaben oder — in manchen Beauftragungen — in einer Beziehung als eigenständiger CSN und in einer anderen als CSP auftreten. [Organisation] muss anhand des in CLD-SEC-IMP-A.5.39-UG, Teil 1, beschriebenen Klassifizierungsverfahrens bestimmen und dokumentieren, welche Unterrolle(n) für jeden von ihr beauftragten Cloud-Service-Partner gelten.

## Anwendbarkeit

Diese Richtlinie gilt für:

- Alle Dritten, die [Organisation] entweder in ihrer CSC- oder CSP-Eigenschaft beauftragt, deren Tätigkeiten der ISO/IEC-22123-3-Definition eines Cloud-Service-Partners entsprechen (Unterrolle Entwickler, Auditor oder Broker)
- Alle internen Teams, die für die Auswahl, Beauftragung oder Überwachung solcher Partner zuständig sind

---

# Richtlinienaussagen: Vereinbarung über Rollen des Cloud-Service-Partners (5.39)

## Klassifizierung und Vereinbarung der Rollen des CSN

[Organisation] muss, bevor ein Cloud-Service-Partner eine Tätigkeit aufnimmt, die einen von [Organisation] genutzten (als CSC) oder bereitgestellten (als CSP) Cloud-Dienst betrifft:

- Den Dritten anhand der drei ISO/IEC-22123-3-Unterrollen klassifizieren und bestätigen, ob die Beauftragung den Dritten auch unabhängig zu einem eigenständigen CSP macht (in diesem Fall gilt CLD-SEC-POL-A.5.38 zusätzlich für diesen Teil der Beziehung)
- Die vom CSN zu übernehmenden Rollen und Verantwortlichkeiten, verknüpft mit seiner (seinen) klassifizierten Unterrolle(n), vor Abschluss der Vertragsverhandlung klar definieren
- Die vom CSN vorgeschlagenen Verantwortlichkeiten abrufen und gegen die Matrix der gemeinsamen Verantwortung (CLD-SEC-IMP-A.5.38-TG, Abschnitt 1) für die vom CSN unterstützte Cloud-Dienst-Beziehung prüfen
- Mit dem CSN vor Arbeitsbeginn eine schriftliche Vereinbarung über diese Rollen und Verantwortlichkeiten treffen — eine informelle oder mündliche Absprache erfüllt diese Anforderung nicht
- Wo die Konsistenzprüfung einen Konflikt mit der bestehenden CSC-/CSP-Zuweisung feststellt, vor der Fortsetzung die schriftliche Zustimmung der Gegenpartei (CSC oder CSP) einholen oder die Beauftragung ablehnen

## Vertragliche Anforderungen

Jede Cloud-Service-Partner-Beauftragung im Geltungsbereich dieser Richtlinie muss durch eine schriftliche Vereinbarung geregelt sein, verhandelt gemäss ISMS-POL-A.5.19-23-S2 (Anforderungen an Lieferantenvereinbarungen), die mindestens:

- Die Unterrolle(n) des CSN identifiziert (Entwickler, Auditor, Broker oder Kombination)
- Die dem CSN zugewiesenen spezifischen Informationssicherheitsverantwortlichkeiten als Vertragstext festhält — nicht als informelle Nebenabsprache
- Bestätigt, dass die Pflichten des CSN nicht im Widerspruch zu den bestehenden CSC-/CSP-Verpflichtungen zur gemeinsamen Verantwortung von [Organisation] stehen, unter Bezugnahme auf die durchgeführte Konsistenzprüfung

## Kommunikation der vereinbarten Rollen

[Organisation] muss die vereinbarten Rollen und Verantwortlichkeiten des CSN den internen Teams, die mit dem CSN zusammenarbeiten (Cloud-Diensteerbringung, Engineering, betroffenes Projektpersonal), über das CSN-Rollenregister und das Informationssicherheits-Sensibilisierungsprogramm der Organisation (siehe ISMS-POL-A.6.3) kommunizieren, sowie dem eigenen operativen Personal des CSN über die unterzeichnete Vereinbarung, ergänzt durch eine gemeinsame Verantwortlichkeitsbesprechung bei Beauftragungen mit informationssicherheitsrelevantem Geltungsbereich.

## CSN-Rollenregister — Mindestinhalt

Das CSN-Rollenregister (vollständiges Schema in CLD-SEC-IMP-A.5.39-TG, Abschnitt 1) muss je Cloud-Service-Partner mindestens erfassen: den Namen des CSN; seine klassifizierte(n) Unterrolle(n) und ob er zudem unabhängig als CSP auftritt; die ihm zugewiesenen Verantwortlichkeiten; die zugehörige Cloud-Dienst-Beziehung und den Verweis auf die Matrix der gemeinsamen Verantwortung; die Referenz und das Datum der Vereinbarung; das Ergebnis der Konsistenzprüfung; und das Datum der letzten Überprüfung. Das Register muss vom Cloud Security Manager geführt und mindestens jährlich überprüft werden.

## Laufende Überwachung und Änderungen des Geltungsbereichs

[Organisation] muss:

- Das CSN-Rollenregister mindestens jährlich überprüfen und bestätigen, dass die Klassifizierung, die vereinbarten Verantwortlichkeiten und die fortbestehende Konsistenz mit der jeweiligen Matrix der gemeinsamen Verantwortung jedes CSN weiterhin zutreffend sind
- Die Klassifizierung und Konsistenz neu bewerten und die Vereinbarung entsprechend anpassen, sobald sich die tatsächliche Tätigkeit eines CSN wesentlich von seinem ursprünglich vereinbarten Geltungsbereich unterscheidet
- Jeden Fall, in dem die Tätigkeit eines CSN seinen vereinbarten Geltungsbereich überschreitet, an den Cloud Security Manager und, falls ungelöst, an den ISB eskalieren und dies als Informationssicherheitsrisiko behandeln, das einer Bewertung bedarf, nicht lediglich als vertragliche Formalität

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **ISB** | Ist Eigentümer von CLD-SEC-POL-A.5.39; genehmigt CSN-Beauftragungen mit informationssicherheitsrelevantem Geltungsbereich; löst Konflikte zwischen CSN-Vereinbarungen und bestehenden CSC-/CSP-Zuweisungen; prüft CSN-bezogene Risikoeskalationen |
| **Cloud Security Manager** | Klassifiziert jeden potenziellen CSN nach Unterrolle; führt die Konsistenzprüfung gegen die anwendbare Matrix der gemeinsamen Verantwortung durch und dokumentiert sie vor Unterzeichnung der CSN-Vereinbarung; pflegt das CSN-Rollenregister; berichtet dem ISB Kennzahlen zur CSN-Abdeckung |
| **Rechts-/Compliance-Beauftragter** | Verhandelt und schliesst CSN-Vereinbarungen gemäss ISMS-POL-A.5.19-23-S2 ab; stellt sicher, dass vereinbarte Rollen und Verantwortlichkeiten im Vertragstext festgehalten sind |
| **Cloud-Diensteerbringung / Engineering** | Handelt innerhalb der Grenzen der vereinbarten Rollen des CSN; eskaliert jede Tätigkeit des CSN, die seinen vereinbarten Geltungsbereich überschreitet |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Verantwortlich | Aufbewahrungsdauer |
|----------|-------------|-----------------|---------------------|
| CSN-Rollenregister | Liste aller aktiven Cloud-Service-Partner mit zugewiesener(n) Unterrolle(n), Geltungsbereich und Vereinbarungsreferenz | Cloud Security Manager | Aktuell + 3 Jahre nach Ende der Beauftragung |
| CSN-Vereinbarungsauszüge | Auszug aus der schriftlichen Vereinbarung jedes CSN mit den vereinbarten Rollen und Verantwortlichkeiten | Rechts-/Compliance-Beauftragter | Dauer der Vereinbarung + 3 Jahre |
| Konsistenzprüfungsnachweise | Nachweise, dass jede CSN-Vereinbarung vor Unterzeichnung gegen die anwendbare Matrix der gemeinsamen Verantwortung geprüft wurde, einschliesslich Ergebnis und etwaiger eingeholter Zustimmung der Gegenpartei | Cloud Security Manager | Aktuell + 3 Jahre |
| Nachweise zu Geltungsbereichsänderungen | Nachweise der CSN-Geltungsbereichs-Neuklassifizierung und Vereinbarungsanpassung bei wesentlicher Änderung der Tätigkeit eines CSN | Cloud Security Manager | Aktuell + 3 Jahre |
| CSN-Risikoeskalationsnachweise | Nachweise jedes CSN-bezogenen Konflikts oder jeder Geltungsbereichsüberschreitung, die in den Risikobeurteilungs- und Behandlungsprozess eskaliert wurde, mit Lösung | ISB | Aktuell + 3 Jahre |

---

# Überwachung und Kennzahlen

Der Cloud Security Manager berichtet dem ISB mindestens vierteljährlich:

- Den Anteil aktiver Cloud-Service-Partner mit einem aktuellen, klassifizierten CSN-Rollenregistereintrag und abgeschlossener Konsistenzprüfung
- Die Anzahl der CSN-Beauftragungen, bei denen ein Konflikt mit der bestehenden CSC-/CSP-Zuweisung festgestellt wurde, und dessen Lösung
- Die Anzahl der Eskalationen wegen Geltungsbereichsüberschreitung und deren Lösungsstatus

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-SEC-POL-A.5.39 verifizieren, sollten Folgendes vorfinden:

- Ein CSN-Rollenregister, das jeden Dritten abdeckt, der der ISO/IEC-22123-3-Definition eines Cloud-Service-Partners entspricht
- Schriftliche Vereinbarungen, welche die zugewiesene(n) Unterrolle(n) und Informationssicherheitsverantwortlichkeiten des CSN ausdrücklich festlegen
- Dokumentierte Nachweise, dass jede CSN-Vereinbarung vor Abschluss gegen die massgebliche Matrix der gemeinsamen Verantwortung gemäss CLD-SEC-POL-A.5.38 geprüft wurde, einschliesslich der Lösung etwaiger Konflikte
- Belege, dass Geltungsbereichsänderungen eine Neuklassifizierung und Vereinbarungsanpassung ausgelöst haben, keine stille Abweichung
- Vierteljährliche Überwachungskennzahlen, die eine aktive Überwachung belegen, keine einmalige Übung bei der Aufnahme

---

<!-- QA_VERIFIED: 2026-08-01 -->

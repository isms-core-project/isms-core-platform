<!-- ISMS-CORE:POLICY:CLD-POL-A.12-DE:cloud:POL:a.12 -->
**CLD-POL-A.12 — Datenschutz-Compliance**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Datenschutz-Compliance |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-POL-A.12 |
| **Dokumentersteller** | Datenschutzbeauftragter (DSB) / ISB |
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
| 1.0 | [Date to be set] | DSB / ISB | Erstversion für ISO/IEC 27018:2025 Ausg. 3 Implementierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen regulatorischen, Dienst-Footprint- oder Datenresidenz-Änderungen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Datenschutzbeauftragter (DSB)
- Sekundär: ISB / Cloud Security Manager
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII)
- ISMS-POL-A.5.19-23 (Lieferanten- und Drittanbieterbeziehungen)
- CLD-POL-A.1 (Allgemein)
- CLD-POL-A.8 (Offenheit, Transparenz — Unterauftragsverarbeiter-Offenlegung)
- CLD-POL-A.11 (§11.12 — Unterbeauftragte PII-Verarbeitung)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.12 und Kontrollen A.12.1–A.12.2
- ISO/IEC 27701:2025 Kontrollen A.2.5.2 (Grundlage für PII-Übermittlung zwischen Rechtsordnungen) und A.2.5.3 (Länder und internationale Organisationen, an die PII übermittelt werden können)
- DSGVO Artikel 28 Abs. 3 lit. a (Auftragsverarbeiter verarbeitet nur gemäss dokumentierten Verantwortlichen-Weisungen, einschliesslich Standort); Artikel 44–49 (Übermittlung an Drittländer); Artikel 46 (geeignete Garantien für internationale Übermittlungen)
- CH DSG Artikel 16–17 (internationale Übermittlung personenbezogener Daten); Artikel 9 Abs. 3 (Pflichten des Auftragsverarbeiters bezüglich Unterauftragsverarbeitern und Standorten)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] als Public-Cloud-PII-Auftragsverarbeiter in Bezug auf Datenschutz-Compliance fest — insbesondere die Pflicht, die geografischen Standorte offenzulegen, an denen PII gespeichert, verarbeitet oder durchgeleitet werden, von PII-Verantwortlichen auferlegte Datenresidenzanforderungen zu respektieren und alle beabsichtigten PII-Zielorte einschliesslich internationaler Übermittlungen und ihrer Rechtsgrundlage zu dokumentieren und mitzuteilen — gemäss ISO/IEC 27018:2025 Annex A, Abschnitt A.12 und Kontrollen A.12.1 und A.12.2.

**Geltungsbereich**: Alle von [Organisation] im Auftrag von PII-Verantwortlichen verarbeiteten PII, über alle Infrastrukturregionen, Verfügbarkeitszonen und Unterauftragsverarbeiter-Standorte hinweg.

**Begründung für die kombinierten Kontrollen**: A.12.1 und A.12.2 befassen sich mit der geografischen Dimension der PII-Verarbeitungstransparenz. A.12.1 legt die Pflicht zur Offenlegung des PII-Aufenthaltsorts fest; A.12.2 legt die Pflicht fest, alle Zielorte, an die PII fliessen kann, zu identifizieren und die Rechtsgrundlage für jede Übermittlung ausserhalb der Rechtsordnung des Verantwortlichen zu dokumentieren. Gemeinsam ermöglichen diese Kontrollen PII-Verantwortlichen, ihren eigenen Übermittlungs-Rechenschaftspflichten gemäss DSGVO Artikel 44+ und gleichwertigem nationalem Recht nachzukommen.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 Kontrollaussagen

**Abschnitt A.12 — Datenschutz-Compliance (Grundsatz)**

Abschnitt A.12 legt den Grundsatz fest, dass ein Public-Cloud-PII-Auftragsverarbeiter die geografischen Standorte, an denen PII gespeichert, verarbeitet oder übertragen werden, gegenüber Verantwortlichen pflegen und offenlegen, Mechanismen zur Durchsetzung von Datenresidenzanforderungen implementieren und die Rechtsgrundlage für grenzüberschreitende Übermittlungen dokumentieren sollte.

**Kontrolle A.12.1 — Geografischer Standort von PII**

Kontrolle A.12.1 verpflichtet den Auftragsverarbeiter, alle an der PII-Verarbeitung beteiligten Länder und Regionen offenzulegen — einschliesslich Unterauftragsverarbeiter-Standorten — eine Vorankündigung vor Änderungen dieser Standorte zu geben und vereinbarte Residenzeinschränkungen technisch durchzusetzen.

**Kontrolle A.12.2 — Beabsichtigte Zielorte von PII**

Kontrolle A.12.2 verpflichtet den Auftragsverarbeiter, alle beabsichtigten Zielorte für PII-Übermittlungen einschliesslich des anwendbaren Übermittlungsmechanismus und der Garantien für jeden grenzüberschreitenden oder rechtsordnungsübergreifenden Datenfluss zu dokumentieren und mitzuteilen.

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 28 Abs. 3 lit. a (Auftragsverarbeiter verarbeitet nur gemäss Weisungen des Verantwortlichen, einschliesslich Standort); Artikel 44–49 (Verbot von Übermittlungen an Drittländer ohne angemessenes Schutzniveau, sofern keine geeigneten Garantien vorhanden sind); Artikel 46 (Standardvertragsklauseln, verbindliche interne Datenschutzvorschriften, Verhaltenskodizes als Übermittlungsmechanismen); Artikel 30 (Verzeichnis der Verarbeitungstätigkeiten einschliesslich Empfänger und Drittländer)
- **CH DSG**: Artikel 16–17 (Verbot der Übermittlung personenbezogener Daten in Länder ohne angemessenes Schutzniveau; anerkannte Garantien); Artikel 9 Abs. 3 (Unterbeauftragung und Standortpflichten des Auftragsverarbeiters)
- **ISO/IEC 27018:2025**: Kontrollen A.12.1, A.12.2

---

# Richtlinienaussagen: Geografischer Standort von PII (A.12.1)

## Standortoffenlegung

[Organisation] muss ein **PII-Verarbeitungsstandort-Register** führen, das alle Länder und Regionen dokumentiert, in denen PII als Teil der Cloud-Diensteerbringung gespeichert, verarbeitet oder durchgeleitet werden. Das Register muss abdecken:

- **Primäre Speicherstandorte**: Rechenzentren und Cloud-Regionen, in denen ruhende PII gespeichert sind
- **Verarbeitungsstandorte**: Compute-Regionen, in denen PII aktiv verarbeitet werden
- **Transitrouten**: Regionen, durch die PII bei Replizierungs-, Backup- oder Liefervorgängen durchgeleitet werden können
- **Unterauftragsverarbeiter-Standorte**: Alle geografischen Standorte der gemäss CLD-POL-A.11 (§11.12) beauftragten Unterauftragsverarbeiter

Das PII-Verarbeitungsstandort-Register muss PII-Verantwortlichen auf Anfrage zur Verfügung gestellt werden. Eine zusammengefasste Version — die primäre Speicher- und Verarbeitungsstandorte sowie Unterauftragsverarbeiter-Länder umfasst, jedoch detaillierte Transitrouteninformationen weglässt — muss im Trust-Portal von [Organisation] für Verantwortliche unter allgemeiner Genehmigung veröffentlicht werden. Authentifizierte Verantwortliche können das vollständige Register über das Trust-Portal oder direkt beim DSB anfordern. Transitroutendetails werden nur an authentifizierte Verantwortliche bereitgestellt, angesichts der Sicherheitsimplikationen einer vollständigen öffentlichen Offenlegung.

## Durchsetzung der Datenresidenz

Sofern ein PII-Verantwortlicher Datenresidenzanforderungen im Dienstleistungsvertrag spezifiziert (z. B. "Nur EU-Speicherung", "Nur Schweiz"), muss [Organisation]:

- Die Residenzeinschränkung durch Infrastrukturkonfiguration (Regionseinschränkungen, Geo-Fencing, Speicherrichtlinienregeln) **technisch durchsetzen**
- Den zur Durchsetzung der Einschränkung eingesetzten technischen Mechanismus **dokumentieren** und diese Dokumentation dem Verantwortlichen auf Anfrage zur Verfügung stellen
- Die Residenz-Compliance mindestens jährlich und bei wesentlichen Infrastrukturänderungen **prüfen** und bestätigen, dass keine PII ausserhalb der vereinbarten Regionen gespeichert oder verarbeitet wurden

## Änderungsbenachrichtigung

Vor der Änderung des geografischen Standorts der PII-Verarbeitung — einschliesslich der Öffnung einer neuen Dienstregion, Hinzufügung eines Unterauftragsverarbeiters in einer neuen Rechtsordnung oder Verlagerung von Backup-Speicherung — muss [Organisation]:

1. Den betreffenden PII-Verantwortlichen im Voraus mit einer Mindestfrist von **30 Tagen** informieren (sofern im Dienstleistungsvertrag keine längere Frist festgelegt ist)
2. Den neuen Standort identifizieren und die betriebliche Begründung für die Änderung erläutern
3. Vorherige Zustimmung von Verantwortlichen einholen, deren Dienstleistungsverträge spezifische Einwilligung (nicht nur allgemeine Genehmigung) für Standortänderungen verlangen
4. Das PII-Verarbeitungsstandort-Register innerhalb von 5 Werktagen nach Inkrafttreten der Änderung aktualisieren

Notfall-Standortänderungen (z. B. aufgrund von Rechenzentrumsausfällen oder höherer Gewalt) müssen betroffenen Verantwortlichen ohne unangemessene Verzögerung mitgeteilt werden. [Organisation] muss betroffenen Verantwortlichen zusätzlich eine vorläufige schriftliche Bestätigung der Abweichung zukommen lassen — einschliesslich des neuen temporären Standorts, der erwarteten Dauer der Abweichung und etwaiger temporärer Residenzlücken — damit Verantwortliche während der Lückenperiode informierte Entscheidungen über ihre eigenen Meldepflichten treffen können. Die rückwirkende formale Dokumentation der Änderung und ihrer Begründung muss innerhalb von 5 Werktagen abgeschlossen werden.

---

# Richtlinienaussagen: Beabsichtigte Zielorte von PII (A.12.2)

## Übermittlungsdokumentation

[Organisation] muss dokumentierte Aufzeichnungen aller **beabsichtigten Zielorte** führen, an die PII als Teil der Cloud-Diensteerbringung übermittelt werden können, einschliesslich grenzüberschreitender oder rechtsordnungsübergreifender Datenflüsse an:

- Unterauftragsverarbeiter (ob innerhalb oder ausserhalb des EWR)
- Backup- und Desaster-Recovery-Standorte in Drittländern
- Cloud-Anbieter-Infrastruktur in Rechtsordnungen ausserhalb des Heimatlandes des Verantwortlichen
- Support- oder Betriebspersonal, das remote von ausserhalb der Verarbeitungsregion auf PII zugreift (gehandhabt über Jump-Server-Architektur, die Daten in der Region hält, oder über in Arbeits- oder Auftragnehmerverträge einbezogene SCCs — der spezifische Mechanismus von [Organisation] muss in den Übermittlungsziel-Aufzeichnungen dokumentiert werden)

Für jeden identifizierten Zielort muss [Organisation] dokumentieren:

| Element | Beschreibung |
|---------|-------------|
| **Zielland/-region** | Rechtsordnung des beabsichtigten Empfängers oder Verarbeitungsstandorts |
| **Übermittlungszweck** | Betriebliche Begründung für die Übermittlung (Backup, Support-Zugang, Replizierung usw.) |
| **Übermittlungsmechanismus** | Rechtsgrundlage für die Übermittlung (Angemessenheitsbeschluss, SCCs, BCRs, Ausnahme — siehe unten) |
| **Bestehende Garantien** | Angewendete technische und vertragliche Schutzvorrichtungen (Verschlüsselung im Transit, DPA/Nachtrag, Unterauftragsverarbeiter-Vereinbarung) |
| **Verantwortlichen-Benachrichtigungsstatus** | Ob der Verantwortliche über diesen Zielort informiert wurde |

## Übermittlungsmechanismen

Für Übermittlungen von PII in Länder ausserhalb des EWR oder der Schweiz ohne Angemessenheitsbeschluss muss [Organisation] einen der folgenden genehmigten Übermittlungsmechanismen implementieren:

- **Standardvertragsklauseln (SCCs)**: Von der EU genehmigte SCCs (Set 2021) in Unterauftragsverarbeiter- und Datenverarbeitungsvereinbarungen einbezogen
- **UK International Data Transfer Agreement (IDTA)**: Für Übermittlungen in das/aus dem Vereinigten Königreich — der Rechts-/Compliance-Beauftragte muss aktuelle ICO-Leitlinien zu IDTA-Versionen vor der Ausführung prüfen
- **Schweizer EDÖB-Standarddatenschutzklauseln**: Für Übermittlungen gemäss CH DSG — der Rechts-/Compliance-Beauftragte muss den genauen Instrumententitel und das Veröffentlichungsdatum von der EDÖB-Website vor der Ausführung bestätigen
- **Angemessenheitsbeschluss**: Sofern für das Zielland zum Zeitpunkt der Übermittlung ein EU- oder Schweizer Angemessenheitsbeschluss besteht
- **Verbindliche interne Datenschutzvorschriften (BCRs)**: Sofern anwendbar für konzerninterne Übermittlungen

[Organisation] darf PII nicht in ein Drittland übermitteln, es sei denn, einer der oben genannten Mechanismen ist vorhanden und dokumentiert. Ändert sich der Angemessenheitsstatus eines Ziellandes, muss [Organisation]:

1. **Neue Übermittlungen** in das betroffene Land innerhalb von **5 Werktagen** nach Erlöschen oder Ungültigwerden des Angemessenheitsbeschlusses **einstellen**
2. **Alternative Übermittlungsmechanismen** (z. B. SCCs) innerhalb von **60 Tagen** implementieren, mit DSB-Aufsicht und Verantwortlichen-Benachrichtigung während des gesamten Zeitraums
3. **Betroffene PII-Verantwortliche informieren**, sobald [Organisation] von der Angemessenheitsänderung Kenntnis erlangt, und dabei das Einstellungsdatum und den beabsichtigten alternativen Mechanismus bestätigen

Die Trennung der Einstellungspflicht von der Implementierung des alternativen Mechanismus trägt der praktischen Realität der gleichzeitigen Neuverhandlung von Instrumenten mit mehreren Unterauftragsverarbeitern Rechnung und schützt betroffene Personen vor fortgesetzten ungesicherten Übermittlungen.

## Übermittlungs-Folgenabschätzungen

Eine Transfer Impact Assessment (TIA) ist erforderlich, bevor PII in ein Land übermittelt werden, für das Anlass zur Annahme besteht, dass der lokale Rechtsrahmen keinen im Wesentlichen gleichwertigen Schutz wie die DSGVO bietet. Indikatoren, die eine TIA auslösen, umfassen: Länder mit dokumentierten Massenüberwachungsprogrammen, ohne unabhängige Datenschutzbehörde oder ohne Rechtsstaatlichkeitsschutz für Daten ausländischer Staatsangehöriger. Der DSB muss eine Liste der derzeit als TIA-pflichtig bezeichneten Rechtsordnungen pflegen. Die TIA-Methodik folgt den EDSA Empfehlungen 01/2020 zu ergänzenden Massnahmen. Abgeschlossene TIAs werden gemäss dem Nachweisplan aufbewahrt und Verantwortlichen auf Anfrage zur Verfügung gestellt.

## Standortänderungen von Unterauftragsverarbeitern

Unterauftragsverarbeiter sind vertraglich verpflichtet, [Organisation] über Änderungen des geografischen Standorts ihrer PII-Verarbeitungsvorgänge innerhalb von 10 Werktagen nach der Änderung zu informieren (gemäss den Unterauftragsverarbeiter-Vereinbarungsanforderungen von CLD-POL-A.11 §11.12). [Organisation] muss Unterauftragsverarbeiter-Standortdaten mindestens jährlich im Rahmen der jährlichen Unterauftragsverarbeiter-Prüfung gemäss CLD-POL-A.11 §11.12 überprüfen und das PII-Verarbeitungsstandort-Register entsprechend aktualisieren.

## Verantwortlichen-Information

[Organisation] muss Verantwortlichen auf Anfrage Übermittlungsdokumentation zur Verfügung stellen. Sofern ein Verantwortlicher dies anfordert, um sein eigenes DSGVO-Artikel-30-Verzeichnis der Verarbeitungstätigkeiten oder TIAs zu unterstützen, muss [Organisation] bereitstellen:

- Die vollständige Liste der Übermittlungszielorte für die PII des Verantwortlichen
- Den Übermittlungsmechanismus und relevanten Rechtsinstrument-Verweis (z. B. SCCs-Klauselreferenz, Angemessenheitsbeschluss-Zitat) für jeden Zielort
- Eine Zusammenfassung der für Übermittlungen in Hochrisiko-Rechtsordnungen angewendeten ergänzenden technischen Garantien

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Datenschutzbeauftragter (DSB)** | Verantwortlich für das PII-Verarbeitungsstandort-Register und Übermittlungsdokumentation; berät zu Angemessenheitsbewertungen und Übermittlungsmechanismus-Auswahl; verwaltet Verantwortlichen-Benachrichtigung bei Standortänderungen; überprüft Übermittlungsmechanismen jährlich |
| **ISB / Cloud Security Manager** | Implementiert und prüft technische Datenresidenz-Durchsetzungskontrollen; beaufsichtigt Unterauftragsverarbeiter-Standortüberwachung; verwaltet Notfall-Standortänderungs-Benachrichtigungen |
| **Rechts-/Compliance-Beauftragter** | Pflegt SCCs-, IDTA- und Schweizer Standardklauseln-Vorlagen; berät zu Angemessenheitsstatus von Drittländern; überprüft Übermittlungsdokumentation auf regulatorische Compliance |
| **Cloud Engineering** | Implementiert geografische Dateneinschränkungen und Residenz-Durchsetzungsmechanismen; konfiguriert regionale Isolierung für Kunden-Workloads; prüft Residenz-Compliance |
| **Beschaffung** | Stellt sicher, dass Unterauftragsverarbeiter-Standorte vor Vertragsunterzeichnung erfasst werden; löst DSB-Überprüfung für neue oder geänderte Unterauftragsverarbeiter-Standorte aus |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| PII-Verarbeitungsstandort-Register | Vollständiges Register aller PII-Speicher-, Verarbeitungs- und Transitstandorte einschliesslich Unterauftragsverarbeiter | Aktuell + Vorgängerversionen für 5 Jahre |
| Datenresidenz-Konfigurationsaufzeichnungen | Technische Dokumentation der Residenz-Durchsetzungsmechanismen pro Verantwortlichem | Vereinbarungsdauer + 5 Jahre |
| Residenz-Prüfergebnisse | Jährliche Prüfergebnisse, die keine ausserplanmässige PII-Verarbeitung bestätigen | 5 Jahre |
| Standortänderungs-Benachrichtigungen | Aufzeichnungen der Vorankündigungen an Verantwortliche für Standortänderungen | 5 Jahre |
| Übermittlungsziel-Aufzeichnungen | Vollständige Übermittlungsziel-Dokumentation pro Verantwortlichem | Vereinbarungsdauer + 5 Jahre |
| Übermittlungsmechanismus-Instrumente | Kopien von SCCs, IDTAs, BCRs und Angemessenheitsbeschluss-Zitaten | Engagementdauer + 5 Jahre |
| TIA-Aufzeichnungen | Dokumentierte TIAs oder gleichwertige Beurteilungen für Übermittlungen in Hochrisiko-Rechtsordnungen | 5 Jahre |

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-POL-A.12 verifizieren, sollten Folgendes vorfinden:

- Ein aktuelles PII-Verarbeitungsstandort-Register, das alle Speicher-, Verarbeitungs- und Transitstandorte einschliesslich Unterauftragsverarbeiter abdeckt — konsistent mit der veröffentlichten Unterauftragsverarbeiter-Liste (CLD-POL-A.8.1)
- Technische Belege, dass Datenresidenzkontrollen für alle Verantwortlichen mit Residenzanforderungen implementiert und durchgesetzt sind
- Aufzeichnungen über Vorankündigungen an Verantwortliche für etwaige Standortänderungen im Prüfungszeitraum
- Übermittlungsziel-Aufzeichnungen mit dokumentierten Übermittlungsmechanismen für alle Nicht-EWR-/Nicht-Schweizer Verarbeitungsstandorte — einschliesslich SCCs oder gleichwertiger Instrumente für jeden Drittland-Zielort
- Keine undokumentierten PII-Übermittlungen in Drittländer ohne genehmigten Übermittlungsmechanismus

---

<!-- QA_VERIFIED: 2026-03-29 -->

<!-- ISMS-CORE:POLICY:CLD-POL-A.11-DE:cloud:POL:a.11 -->
**CLD-POL-A.11 — Informationssicherheit**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Public-Cloud-PII-Auftragsverarbeiter — Informationssicherheit |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | CLD-POL-A.11 |
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

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Infrastruktur-, Technologie- oder regulatorischen Änderungen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: ISB / Cloud Security Manager
- Sekundär: Datenschutzbeauftragter (DSB)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- ISMS-POL-A.5.34 (Datenschutz und Schutz von PII)
- ISMS-POL-A.5.15-16-18 (Identitäts- und Zugangsverwaltung)
- ISMS-POL-A.5.19-23 (Lieferanten- und Drittanbieterbeziehungen)
- ISMS-POL-A.8.10 (Informationslöschung)
- ISMS-POL-A.8.24 (Verwendung von Kryptografie)
- CLD-POL-A.1 (Allgemein)
- CLD-POL-A.5 (Datenminimerung — Löschung temporärer Dateien)
- CLD-POL-A.8 (Offenheit, Transparenz — Unterauftragsverarbeiter-Offenlegung)
- CLD-POL-A.10 (Rechenschaftspflicht — Verletzungsmeldung)
- ISO/IEC 27018:2025 Annex A, Abschnitt A.11 und Kontrollen A.11.1–A.11.13
- ISO/IEC 27701:2025 Annex A.3 (Informationssicherheitskontrollen — A.3.3 bis A.3.31, anwendbar auf Verantwortliche und Auftragsverarbeiter, durch diese Richtlinie implementiert)
- ISO/IEC 27002:2022 Kontrollen 6.2 (Bedingungen und Konditionen), 8.11 (Datenmaskierung), 8.12 (Datenverlustprävention), 8.24 (Kryptografie)
- DSGVO Artikel 28 Abs. 3 lit. c (Auftragsverarbeiter implementiert angemessene technische und organisatorische Massnahmen gemäss Artikel 32); Artikel 32 (Sicherheit der Verarbeitung)
- CH DSG Artikel 9 (Bedingungen für die Auftragsverarbeitung und damit verbundene Datensicherheitspflichten)

---

## Zusammenfassung

Diese Richtlinie legt die Informationssicherheitsanforderungen von [Organisation] für den Schutz von PII in Public-Cloud-Umgebungen fest — den umfangreichsten Abschnitt des ISO/IEC 27018:2025 Annex-A-Kontrollsatzes, der 13 Kontrollen in den Bereichen Vertraulichkeit, physische Mediensicherheit, Zugangsverwaltung, Verschlüsselung, Prüfprotokollierung, Unterauftragsverarbeiter-Management und Speicherremanenz abdeckt.

**Geltungsbereich**: Alle Systeme, Mitarbeitenden, Prozesse und Unterauftragsverarbeiter, die an der Verarbeitung von PII im Auftrag von PII-Verantwortlichen innerhalb der Public-Cloud-Dienste von [Organisation] beteiligt sind.

**Kontrollabdeckung**: Diese Richtlinie behandelt ISO/IEC 27018:2025 Kontrollen A.11.1 bis A.11.13.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27018:2025 Kontrollaussagen

**A.11.1 — Vertraulichkeits- oder Geheimhaltungsvereinbarungen**: Personal mit PII-Zugang ist durch dokumentierte NDA-Pflichten gebunden, die über die Beendigung hinaus gelten.

**A.11.2 — Einschränkung der Erstellung von Papierkopien**: Ausdrucken von PII auf dokumentierte legitime Zwecke beschränkt; ausgedruckte PII sicher behandelt.

**A.11.3 — Kontrolle und Protokollierung der Datenwiederherstellung**: Backup-Wiederherstellung von PII ist eine kontrollierte, protokollierte Operation; Protokolle geschützt und überprüft.

**A.11.4 — Schutz von Daten auf das Betriebsgelände verlassenden Speichermedien**: Physische Medien mit PII verschlüsselt oder vernichtet, bevor sie die kontrollierte Umgebung verlassen.

**A.11.5 — Verwendung unverschlüsselter portabler Speichermedien und -geräte**: Unverschlüsselte portable Geräte für PII verboten; Verlust/Diebstahl als PII-Vorfall behandelt.

**A.11.6 — Verschlüsselung von PII bei der Übertragung über öffentliche Datenübertragungsnetze**: PII im Transit mit TLS 1.2 Minimum, bevorzugt 1.3 verschlüsselt; HTTPS erzwungen.

**A.11.7 — Sichere Entsorgung von Papierkopien**: Papier-PII durch Kreuzschnitt-Schreddern oder gleichwertig entsorgt; Entsorgung dokumentiert.

**A.11.8 — Eindeutige Verwendung von Benutzer-IDs**: Jede Person mit PII-Zugang erhält eine eindeutige Kennung; keine gemeinsamen Konten.

**A.11.9 — Benutzer-ID-Verwaltung**: Benutzer-ID-Lebenszyklus verwaltet; bei Beendigung oder Rollenänderung unverzüglich deaktiviert; inaktive Konten überprüft.

**A.11.10 — Aufzeichnungen autorisierter Benutzer**: Aktuelle Aufzeichnungen aller autorisierten PII-Systemnutzer; mindestens vierteljährlich überprüft; dem Verantwortlichen verfügbar.

**A.11.11 — Vertragsmassnahmen**: Auftragsverarbeiter-Verantwortlichen-Vereinbarungen umfassen Umfang, Sicherheit, Verletzungsmeldung, Rechtshilfe, Prüfung, Unterauftragsverarbeiter-Genehmigung, Rückgabe/Löschung, Rechtsordnung.

**A.11.12 — Unterbeauftragte PII-Verarbeitung**: Unterauftragsverarbeiter durch bindende Verträge mit gleichwertigen Pflichten gebunden; periodisch geprüft; Auftragsverarbeiter bleibt verantwortlich.

**A.11.13 — Zugang zu Daten auf zuvor genutztem Datenspeicherplatz**: Einem neuen Kunden neu zugewiesener Speicher kryptografisch gelöscht; Ausser-Betrieb-Nahme-Verfahren dokumentiert und getestet.

## Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss PRIV-POL-00):

- **EU DSGVO**: Artikel 28 Abs. 3 lit. c (Auftragsverarbeiter implementiert angemessene technische und organisatorische Massnahmen gemäss Artikel 32); Artikel 32 (Sicherheit der Verarbeitung — Pseudonymisierung, Verschlüsselung, Belastbarkeit, Wiederherstellung, Tests)
- **CH DSG**: Artikel 9 (Bedingungen für die Auftragsverarbeitung und damit verbundene Datensicherheitspflichten)
- **ISO/IEC 27018:2025**: Kontrollen A.11.1–A.11.13

---

# Richtlinienaussagen: Vertraulichkeitspflichten (A.11.1)

Alle Mitarbeitenden und Auftragnehmer von [Organisation] mit Zugang zu PII-haltigen Systemen müssen durch schriftliche Vertraulichkeits- und Geheimhaltungspflichten gebunden sein. NDAs müssen ausdrücklich:

- Sekundärnutzung, persönliche Aufbewahrung oder unbefugte Offenlegung von PII untersagen
- Über die Beendigung des Arbeitsverhältnisses oder Engagements hinaus gelten
- Vor der Gewährung des Zugangs zu einem PII-System unterzeichnet werden

NDAs werden gemäss ISMS-POL-A.6.3 (Vertraulichkeitsvereinbarungen) verwaltet. Die NDA-Abdeckung muss während des Onboarding- und Abgangsprozesses verifiziert werden.

---

# Richtlinienaussagen: Einschränkung von Papierkopien (A.11.2)

Die Erstellung von Papierkopien (Ausdrucken) mit PII ist **eingeschränkt**. Das Ausdrucken von PII erfordert:

- Dokumentierte geschäftliche Begründung (z. B. regulatorische Anforderung, Prüfungsunterlagen)
- Genehmigung durch die zuständige Teamleitung und DSB-Vermerk bei Grossvolumen-Ausdrucken
- Sofortige Entnahme vom Drucker; PII-Material darf in gemeinsam genutzten Bereichen nicht unbeaufsichtigt gelassen werden

Ausgedruckte PII müssen unter Clean-Desk-Verfahren behandelt und gemäss §11.7 (sichere Papierkopien-Entsorgung) entsorgt werden. Wo technisch durchführbar, müssen Druckerverwaltungssoftware oder DLP-Kontrollen konfiguriert werden, um Druckaufträge mit PII zu kennzeichnen oder einzuschränken; wo technische Durchsetzung nicht implementiert ist, muss die Abhängigkeit von verfahrenstechnischen Kontrollen vom ISB mit identifizierten kompensierenden Überwachungsmassnahmen dokumentiert werden.

---

# Richtlinienaussagen: Kontrolle und Protokollierung der Datenwiederherstellung (A.11.3)

Die Wiederherstellung von PII aus Backup oder Archiv ist eine **kontrollierte Operation**, die erfordert:

- Dokumentierte Wiederherstellungsgenehmigung von Teamleitung oder Incident Commander
- Protokollierung von: Operatoren-Identität, Zeitstempel, Backup-Quelle, Umfang der wiederhergestellten Daten und Genehmigungsreferenz
- Wiederherstellungsprotokolle gegen Manipulationen geschützt (write-once oder kryptografisch signiert)
- Vierteljährliche Überprüfung der Wiederherstellungsprotokolle durch ISB

Automatisierte Benachrichtigungen müssen konfiguriert werden, um den ISB in Echtzeit über Wiederherstellungsereignisse zu informieren, was die Erkennung ausserplanmässiger Wiederherstellungen ohne Warten auf die vierteljährliche Protokollprüfung ermöglicht. Ungeplante oder nicht autorisierte Wiederherstellungsversuche müssen als Sicherheitsereignisse behandelt und gemäss ISMS-POL-A.5.24-28 untersucht werden.

---

# Richtlinienaussagen: Speichermedien, die das Betriebsgelände verlassen (A.11.4)

Physische Speichermedien (Laufwerke, Bänder, Wechselmedien) mit PII, die die Cloud-Einrichtungen von [Organisation] verlassen, müssen:

- **Verschlüsselt** sein unter Verwendung genehmigter Full-Disk- oder Volume-Verschlüsselung mit Schlüsselverwaltung gemäss ISMS-POL-A.8.24, oder
- **Physisch vernichtet** werden nach einem Standard, der Datenabruf verhindert (z. B. NIST-SP-800-88-konforme Vernichtung), bevor sie das Gelände verlassen

Medienbewegungen müssen:
- Vom ISB oder Cloud Security Manager genehmigt werden
- In einem Medienbewegungsregister mit Chain-of-Custody-Dokumentation protokolliert werden
- Bis zum Endziel (Rückgabe- oder Vernichtungsanlage) nachverfolgt werden

---

# Richtlinienaussagen: Unverschlüsselte portable Speichergeräte (A.11.5)

Die Verwendung unverschlüsselter portabler Speichermedien und -geräte zur Speicherung oder Übertragung von PII ist **verboten**. Dieses Verbot umfasst USB-Laufwerke, externe Festplatten, Laptops, Tablets und Mobiltelefone.

Sofern portable Geräte für PII autorisiert sind:
- Full-Disk-Verschlüsselung gemäss genehmigten Standards (mindestens AES-256) ist **verpflichtend**
- Der Verschlüsselungsstatus des Geräts muss vor der Gewährung des PII-Zugangs durch die IT verifiziert werden
- Die Fernlöschungsfähigkeit muss für mobile Geräte aktiviert sein

**Verlust oder Diebstahl** jedes portablen Geräts, das möglicherweise PII enthält, muss sofort dem ISB und DSB gemeldet und als PII-Sicherheitsvorfall gemäss CLD-POL-A.10.1 und ISMS-POL-A.5.24-28 behandelt werden.

---

# Richtlinienaussagen: Verschlüsselung von PII im Transit (A.11.6)

PII, die über öffentliche Netze übertragen werden, müssen verschlüsselt sein. Anforderungen:

- **TLS 1.3 erforderlich** für alle neuen Implementierungen; **TLS 1.2 nur für bestehende Integrationen zulässig**, wo TLS 1.3 noch nicht technisch durchführbar ist, vorbehaltlich eines dokumentierten Remediierungsplans und ISB-Genehmigung
- **HTTPS erzwungen** auf allen Web-Schnittstellen und API-Endpunkten, die PII verarbeiten; HTTP-Weiterleitung zu HTTPS verpflichtend
- TLS-Zertifikate müssen von vertrauenswürdigen Zertifizierungsstellen ausgestellt und vor dem Ablauf erneuert werden (automatische Erneuerung bevorzugt)
- **Unverschlüsselte Übertragung** (einfaches HTTP, FTP, SMTP ohne STARTTLS) von PII ist verboten

Cipher-Suite-Konfigurationen müssen jährlich gegen aktuelle Best Practices überprüft werden (z. B. BSI TR-02102, NIST SP 800-52). Schwache Chiffren (RC4, DES, 3DES, SSL 3.0, TLS 1.0, TLS 1.1) müssen deaktiviert werden.

---

# Richtlinienaussagen: Sichere Entsorgung von Papierkopien (A.11.7)

Papierkopien mit PII müssen sicher entsorgt werden:

- **Einzelentsorgung**: Kreuzschnitt-Schreddern nach DIN 66399 Stufe P-5 (max. 30 mm² Partikelgrösse) für PII oder besondere Kategorien enthaltende Dokumente; P-4 ist für allgemeine interne Dokumente ohne PII akzeptabel
- **Massenentsorgung**: Zertifizierte Vernichtungsdienstleistungen mit dem Anfragenden übergebener Vernichtungsurkunde
- **Entsorgungsbehälter**: Abgeschlossene, zugangskontrollierte Behälter für PII-Material in allen PII-haltigen Arbeitsbereichen

Die Entsorgung muss dokumentiert werden. Vernichtungsurkunden müssen 3 Jahre aufbewahrt werden.

---

# Richtlinienaussagen: Eindeutige Benutzer-IDs (A.11.8)

Jeder Person mit Zugang zu PII-Systemen muss eine **eindeutige Benutzerkennung** zugewiesen werden. Gemeinsame, generische oder rollenbasierte Konten dürfen NICHT für den Zugang zu Systemen verwendet werden, in denen PII verarbeitet oder gespeichert werden.

Eindeutige IDs stellen sicher, dass alle Aktionen an PII für Prüfungs- und Rechenschaftszwecke einer bestimmten Person zugeordnet werden können. Ausnahmen (z. B. Service-Accounts) erfordern ISB-Genehmigung und verstärkte kompensierende Kontrollen (Privileged Access Management, Sitzungsaufzeichnung).

---

# Richtlinienaussagen: Benutzer-ID-Verwaltung (A.11.9)

Benutzerkennungen für PII-Systeme müssen durch einen dokumentierten Lebenszyklus verwaltet werden:

| Lebenszyklusphase | Anforderung |
|-------------------|-------------|
| **Provisionierung** | Erfordert dokumentierte Genehmigung vom Vorgesetzten des Benutzers und Systemeigentümer |
| **Zugangsprüfung** | Alle PII-Systemkonten mindestens vierteljährlich überprüft |
| **Rollenänderung** | Zugang innerhalb von 1 Werktag nach bestätigter Rollenänderung aktualisiert |
| **Beendigung** | Konto innerhalb von 4 Stunden nach HR-bestätigtem Abgang deaktiviert |
| **Inaktive Konten** | Konten, die bei PII-kritischen Systemen 30 Tage inaktiv sind (bei PII-Systemen mit geringerer Sensitivität 45 Tage), überprüft; bis zur Überprüfung gesperrt; bei fehlender geschäftlicher Begründung gelöscht |

Die Benutzer-ID-Lebenszyklusverwaltung ist in ISMS-POL-A.5.15-16-18 (IAM) integriert.

---

# Richtlinienaussagen: Aufzeichnungen autorisierter Benutzer (A.11.10)

[Organisation] muss für jedes PII-System ein **Register autorisierter Benutzer** führen, das erfasst:

- Individuelle Identität und Rolle
- Umfang des gewährten Zugangs (Lesen, Schreiben, Admin)
- Genehmigungsdatum und genehmigender Vorgesetzter
- Letztes Überprüfungsdatum

Das Register autorisierter Benutzer muss:
- Mindestens **vierteljährlich** von Systemeigentümern überprüft und bestätigt werden
- Jedem PII-Verantwortlichen auf Anfrage zur Verfügung gestellt werden — [Organisation] stellt jedem Verantwortlichen einen **abgegrenzten Auszug** bereit, der nur Personal mit Zugang zu den PII-Daten dieses Verantwortlichen zeigt, nicht das vollständige Register über alle Kunden hinweg
- Innerhalb von 1 Werktag nach jeder Zugangssänderung aktualisiert werden

---

# Richtlinienaussagen: Vertragsmassnahmen (A.11.11)

Dienstleistungsverträge zwischen [Organisation] und PII-Verantwortlichen müssen Bestimmungen enthalten, die Folgendes regeln:

- Umfang und dokumentierter Zweck der PII-Verarbeitung
- Sicherheitspflichten gemäss DSGVO Artikel 32 und dieser Richtlinie
- Anforderungen zur Verletzungsmeldung (Verantwortlichen-Benachrichtigung innerhalb von 24 Stunden gemäss CLD-POL-A.10.1)
- Unterstützungspflichten bei Betroffenenrechten (gemäss CLD-POL-A.2.1 und CLD-POL-A.9)
- Prüfrechte: Verantwortlicher (oder beauftragter Prüfer) kann die Compliance von [Organisation] prüfen, ausübbar mit mindestens 30 Tagen Vorankündigung, höchstens einmal pro Kalenderjahr, es sei denn, ein bestätigter Sicherheitsvorfall rechtfertigt eine zusätzliche Prüfung, und auf Kosten des Verantwortlichen, sofern keine Non-Compliance nachgewiesen wird
- Anforderungen zur Unterauftragsverarbeiter-Genehmigung (gemäss CLD-POL-A.8.1)
- PII-Rückgabe oder -Löschung bei Beendigung (gemäss CLD-POL-A.10.3)
- Anwendbares Recht und Gerichtsstand

Vertragsbedingungen müssen bei wesentlichen Änderungen der regulatorischen Anforderungen überprüft werden. Der Rechts-/Compliance-Beauftragte pflegt die Standardvorlage für Auftragsverarbeiter-Vereinbarungen.

---

# Richtlinienaussagen: Unterbeauftragte PII-Verarbeitung (A.11.12)

[Organisation] muss allen Unterauftragsverarbeitern über bindende Verträge **gleichwertige Pflichten** wie in dieser Richtlinie und der vollständigen CLD-POL-A.X-Suite auferlegen. Unterauftragsverarbeiter-Verträge müssen:

- Die Datenschutzpflichten aus der Verantwortlichen-Auftragsverarbeiter-Vereinbarung widerspiegeln
- Vor jeder weiteren Unterverarbeitung eine vorherige schriftliche Genehmigung von [Organisation] (und mittelbar vom PII-Verantwortlichen) verlangen
- Prüfrechte für [Organisation] über die Compliance des Unterauftragsverarbeiters umfassen
- Verletzungsmeldung an [Organisation] innerhalb von 12 Stunden nach Erkennung verlangen (um die 24-Stunden-Verantwortlichen-Meldepflicht von [Organisation] gemäss CLD-POL-A.10.1 zu ermöglichen) — diese 12-Stunden-Anforderung ist eine **verpflichtende Klausel** in allen Unterauftragsverarbeiter-Vereinbarungen; der Rechts-/Compliance-Beauftragte pflegt die Standardvorlage für Unterauftragsverarbeiter-Vereinbarungen
- PII-Rückgabe oder -Entsorgung bei Beendigung der Unterauftragsverarbeiter-Beauftragung verlangen

[Organisation] muss Unterauftragsverarbeiter mindestens jährlich prüfen (per Fragebogen, Dokumentenprüfung oder Vor-Ort-Prüfung) und bleibt PII-Verantwortlichen gegenüber für Compliance-Verstösse von Unterauftragsverarbeitern **vollständig verantwortlich**. Unterauftragsverarbeiter-Prüfergebnisse müssen dokumentiert und Verantwortlichen auf Anfrage zur Verfügung gestellt werden.

---

# Richtlinienaussagen: Zuvor genutzter Datenspeicherplatz (A.11.13)

[Organisation] muss sicherstellen, dass auf PII nicht von einem Speicher zugegriffen werden kann, der zuvor einem anderen Kunden zugewiesen war (**Datenremanenz-Prävention**).

Bevor Speicher einem neuen Kunden-Workload neu zugewiesen wird:
- Müssen alle vorherigen Daten **kryptografisch gelöscht** werden (Verschlüsselungsschlüssel-Löschung für verschlüsselte Volumes — die primäre Methode für Cloud-Speicher) oder nach einem Wiederherstellungs-verhindernden Standard überschrieben werden
- Muss die Löschung dokumentiert und der Ausser-Betrieb-Nahme-Nachweis aufbewahrt werden

Ausser-Betrieb-Nahme-Verfahren müssen:
- Alle Speichertypen abdecken: Blockspeicher (EBS, Volumes), Objektspeicher (Bucket-Inhalte), flüchtiger Instanzspeicher und Datenbankspeicher
- Mindestens **jährlich** getestet werden, indem neu zugewiesener Speicher zufällig beprobt und auf fehlende Restdaten überprüft wird
- Gleichermassen für die physische Ausser-Betrieb-Nahme von Speichermedien gelten (siehe A.11.4)

Diese Kontrolle ist die Grundlage der Mandanten-PII-Isolation. Jeder Fehler muss als potenzieller PII-Sicherheitsvorfall behandelt werden.

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB / Cloud Security Manager** | Verantwortlich für diese Richtlinie; stellt sicher, dass alle 13 Kontrollen implementiert und gepflegt werden; führt jährliche Sicherheitsüberprüfung durch; verwaltet Medienbewegung und Unterauftragsverarbeiter-Prüfprogramm |
| **Datenschutzbeauftragter (DSB)** | Überprüft Richtlinie jährlich auf regulatorische Ausrichtung; berät zu Vertragsbedingungen (A.11.11); beaufsichtigt Angemessenheitsbewertungen von Unterauftragsverarbeitern |
| **Cloud Engineering** | Implementiert technische Kontrollen (Verschlüsselung, TLS-Konfiguration, Löschung, Protokollierung); testet Ausser-Betrieb-Nahme-Verfahren |
| **IT / Identitätsverwaltung** | Verwaltet Benutzer-ID-Lebenszyklus gemäss A.11.8–A.11.10; pflegt Register autorisierter Benutzer; setzt Zugriffsrichtlinien durch |
| **Rechts-/Compliance-Beauftragter** | Pflegt Standardvorlage für Auftragsverarbeiter-Vereinbarungen; überprüft Unterauftragsverarbeiter-Vereinbarungen; berät zu Rechtsordnung und Prüfrechts-Klauseln |
| **HR** | Löst Benutzerkonto-Deaktivierung bei Abgang aus; verwaltet NDA-Unterzeichnungsprozess beim Onboarding |

---

# Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrungsdauer |
|----------|-------------|-------------------|
| NDA-Aufzeichnungen | Unterzeichnete NDAs für alle Mitarbeitenden mit PII-Zugang | Engagementdauer + 5 Jahre |
| Druckgenehmigungsprotokolle | Aufzeichnungen autorisierter PII-Druckoperationen | 3 Jahre |
| Backup-Wiederherstellungsprotokolle | Protokollierte Wiederherstellungsereignisse mit Genehmigungsnachweisen | 3 Jahre |
| Medienbewegungsregister | Protokoll physischer Medienbewegungen mit Chain-of-Custody | 3 Jahre |
| TLS- / Verschlüsselungs-Konfigurationsaufzeichnungen | Aktuelle Cipher-Suite- und TLS-Konfigurationsdokumentation | Aktuell + Vorgängerversionen 5 Jahre |
| Vernichtungsurkunden | Papierkopien- und Medienentsorgungsurkunden | 3 Jahre |
| Register autorisierter Benutzer | Vierteljährlich bestätigte Zugangsnachweise pro PII-System | 5 Jahre |
| Unterauftragsverarbeiter-Prüfaufzeichnungen | Jährliche Prüfergebnisse für jeden Unterauftragsverarbeiter | 5 Jahre |
| Speicher-Ausser-Betrieb-Nahme-Aufzeichnungen | Aufzeichnungen der kryptografischen Löschung pro Speicher-Ausser-Betrieb-Nahme-Ereignis | 3 Jahre |
| Ausser-Betrieb-Nahme-Testergebnisse | Jährliche Testergebnisse, die keine Restdaten in neu zugewiesenem Speicher bestätigen | 3 Jahre |

---

# Prüfungshinweise

Prüfende, die die Compliance mit CLD-POL-A.11 verifizieren, sollten Folgendes vorfinden:

- NDA-Abdeckung für alle Mitarbeitenden mit PII-Zugang — keine Ausnahmen
- TLS 1.2+ auf allen PII-verarbeitenden Netzwerkschnittstellen erzwungen; TLS 1.0/1.1 deaktiviert
- Vierteljährliche Bestätigungen des Registers autorisierter Benutzer mit unverzüglicher Entfernung von Abgängern und Rollenwechslern
- Unterauftragsverarbeiter-Prüfberichte für den Prüfungszeitraum, die die Durchsetzung gleichwertiger Pflichten bestätigen
- Speicher-Ausser-Betrieb-Nahme-Testergebnisse, die keine mandantenübergreifende Datenremanenz bestätigen
- Backup-Wiederherstellungsprotokolle mit Genehmigungsnachweisen für alle Wiederherstellungsereignisse

---

<!-- QA_VERIFIED: 2026-03-29 -->

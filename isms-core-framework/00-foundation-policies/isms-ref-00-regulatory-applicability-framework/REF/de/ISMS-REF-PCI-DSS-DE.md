<!-- ISMS-CORE:REF:ISMS-REF-PCI-DSS-DE:framework:REF:pci-dss -->
**ISMS-REF-PCI-DSS — PCI DSS Anforderungsreferenz**
**Sicherheitsanforderungen für Zahlungskartendaten (Nicht-ISMS-Technische Referenz)**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | PCI DSS Anforderungsreferenz |
| **Dokumententyp** | Intern – Technische Referenz (Nicht ISMS) |
| **Dokument-ID** | ISMS-REF-PCI-DSS |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | ISB (Technische Referenz – Keine Genehmigung durch die Geschäftsleitung erforderlich) |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB / Zahlungssicherheitsteam | Erstversion der technischen Referenz für PCI DSS v4.0.1 |

**Überprüfungszyklus**: Jährlich (oder bei PCI-DSS-Versionsaktualisierungen)
**Nächstes Überprüfungsdatum**: [Datum + 12 Monate]
**Genehmiger**: ISB / Zahlungssicherheitsleiter (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verteiler**: Zahlungsabwicklungsteam, ISB, Compliance, IT-Betrieb (für Organisationen, die Zahlungskarten verarbeiten)

---

⚠️ **WICHTIG – NICHT-ISMS-TECHNISCHES UNTERSTÜTZUNGSDOKUMENT**

Dieses Dokument dient ausschließlich zu Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist NICHT Teil des Informationssicherheitsmanagementsystems (ISMS).
- Dieses Dokument definiert KEINE verbindlichen Anforderungen, es sei denn, [Organisation] verarbeitet Zahlungskarten.
- Dieses Dokument begründet KEINE verbindlichen Anforderungen, Fristen, KPIs oder SLAs für Nicht-Kartenverarbeitende.
- Dieses Dokument schreibt die Übernahme von PCI-DSS-Anforderungen für Organisationen, die keine Zahlungskarten verarbeiten, NICHT vor.
- Dieses Dokument setzt KEINE ISMS-Richtlinie ausser Kraft oder erweitert diese.

**Anwendbarkeitsbestimmung**:
PCI-DSS-Anforderungen gelten NUR, WENN [Organisation]:

- Karteninhaberdaten (CHD) speichert, verarbeitet oder überträgt
- Zugang zur Karteninhaberdaten-Umgebung (CDE) hat
- Als Händler Kredit-/Debitkartenzahlungen akzeptiert
- Zahlungsdienstleister oder -verarbeiter ist
- Von Zahlungsmarken (Visa, Mastercard usw.) als compliance-pflichtig eingestuft wurde

Für alle anderen Organisationen dient dieses Dokument ausschließlich als:

- Technische Referenz für potenzielle PCI-DSS-Anforderungen
- Kontext für die Erweiterung in die Zahlungsabwicklung
- Bewusstsein für Zahlungskartenstandards
- **Dieses Dokument darf nicht als Prüfnachweis verwendet werden, es sei denn, [Organisation] ist PCI-DSS-konform**

Die Verwendung dieses Dokuments impliziert keine PCI-DSS-Anwendbarkeit, keine Compliance-Verpflichtungen und keinen Zahlungskarten-Verarbeitungsstatus.

**Kritischer Positionierungshinweis**:
Dieses Dokument enthält absichtlich regulatorische Details, die über das hinausgehen, was für die meisten Organisationen gilt. Sein Zweck ist ausschließlich die Sensibilisierung für Organisationen, die möglicherweise dem PCI DSS unterliegen, oder die Dienstleistungen für Händler oder Zahlungsverarbeiter erbringen. Aus der Anwesenheit, Abwesenheit oder dem Umsetzungsstand einer im Folgenden aufgeführten PCI-DSS-Anforderung dürfen keine Prüfungsschlüsse gezogen werden, es sei denn, [Organisation] verarbeitet ausdrücklich Zahlungskarten.

---

# Dokumentenzweck und Geltungsbereich

## Zweck

Dieses Dokument bietet einen technischen Überblick über die Anforderungen des Payment Card Industry Data Security Standard (PCI DSS) v4.0.1. Es dient zur Unterstützung von:

- Bewusstsein für PCI-DSS-Anforderungen für Organisationen, die Zahlungskarten verarbeiten
- Verständnis der 12 PCI-DSS-Anforderungen über 6 Kontrollziele
- Kontext für Organisationen, die die Akzeptanz von Zahlungskarten in Betracht ziehen
- Potenzielle zukünftige Anwendbarkeitsbewertung
- Zuordnung von PCI-DSS-Anforderungen zu ISO-27001:2022-Kontrollen

## Was dieses Dokument NICHT ist

Dieses Dokument:

- Begründet KEINE verbindlichen Anforderungen für Organisationen, die keine Zahlungskarten verarbeiten
- Definiert KEINE Compliance-Verpflichtungen von [Organisation] (siehe POL-00 für regulatorische Anwendbarkeit)
- Schafft KEINE Prüfkriterien, es sei denn, [Organisation] verarbeitet Zahlungskarten
- Ersetzt NICHT den Leitfaden eines Qualified Security Assessor (QSA)
- Stellt KEINE Rechts- oder Compliance-Beratung zu PCI DSS dar
- Deckt NICHT alle Varianten des Self-Assessment Questionnaire (SAQ) ab
- Begründet KEINE Umsetzungsverfahren oder Validierungsprozesse

## Beziehung zum ISMS

Dieses Dokument ist eine **nicht bindende technische Referenz**, SOFERN [Organisation] keine Zahlungskarten verarbeitet (wie in ISMS-POL-00 Abschnitt 3.4 festgestellt).

**Wenn [Organisation] Zahlungskarten verarbeitet:**

- PCI-DSS-Anforderungen werden gemäß POL-00 zu Tier 1 (Pflichtige Compliance)
- Dieses Dokument bietet Implementierungsleitfaden
- ISMS-Kontrollen müssen PCI-DSS-Compliance belegen
- Jährliche Validierung erforderlich (Compliance-Bericht oder Self-Assessment Questionnaire)

**Wenn [Organisation] KEINE Zahlungskarten verarbeitet:**

- PCI DSS verbleibt gemäß POL-00 in Tier 3 (Informationsreferenz)
- Dieses Dokument dient nur zur Sensibilisierung
- Es bestehen keine PCI-DSS-Compliance-Verpflichtungen
- ISMS-Kontrollen folgen ausschließlich ISO 27001:2022

## Inhaltsorganisation

Diese Referenz organisiert PCI-DSS-Anforderungen nach:

- Anwendbarkeit und Händlerniveaus
- 12 Anforderungen über 6 Kontrollziele
- Definition des Geltungsbereichs der Karteninhaberdaten-Umgebung (CDE)
- Validierungsmethoden (ROC vs. SAQ)
- Zuordnung zu ISO-27001:2022-Annex-A-Kontrollen
- Neue Anforderungen und Zeitpläne von PCI DSS v4.0.1

---

# PCI DSS – Überblick und Anwendbarkeit

## Was ist PCI DSS?

**Payment Card Industry Data Security Standard (PCI DSS)** ist ein globaler Informationssicherheitsstandard zum Schutz von Zahlungskartendaten.

**Lenkungsgremium**: PCI Security Standards Council (PCI SSC)

- Gegründet von grossen Zahlungsmarken (Visa, Mastercard, American Express, Discover, JCB)
- Entwickelt und pflegt PCI DSS
- Zertifiziert Qualified Security Assessors (QSAs)

**Aktuelle Version**: **PCI DSS v4.0.1** (veröffentlicht März 2024)

- Wirksamkeit: 31. März 2024
- Übergangsfrist von v3.2.1 endete: 31. März 2024
- Neue Anforderungen bis 31. März 2025 eingeführt

**Zweck**:

- Karteninhaberdaten vor Diebstahl und Betrug schützen
- Mindestsicherheitsanforderungen festlegen
- Sicherheitskontrollen im gesamten Zahlungsökosystem standardisieren
- Risiko von Datenpannen reduzieren

## Wer muss PCI DSS einhalten?

**Jede Organisation, die Karteninhaberdaten speichert, verarbeitet oder überträgt**:

| Entitätstyp | Beschreibung | Beispiele |
|-------------|--------------|-----------|
| **Händler** | Akzeptieren Zahlungskarten als Zahlungsmittel | Einzelhändler, E-Commerce, Restaurants, Hotels |
| **Dienstleister** | Verarbeiten, speichern oder übertragen CHD im Auftrag von Händlern | Zahlungs-Gateways, Verarbeiter, Hosting-Anbieter, Managed Security Services |
| **Finanzinstitute** | Geben Zahlungskarten aus oder erwerben Transaktionen | Banken, Kreditgenossenschaften, Zahlungsnetzwerke |
| **POS-Anbieter** | Stellen POS-Systeme oder -Anwendungen bereit | POS-Software-Anbieter, Terminal-Hersteller |

**Kernprinzip**: Wer Karteninhaberdaten berührt, muss PCI DSS einhalten.

## Händlerniveaus

Zahlungsmarken (Visa, Mastercard usw.) klassifizieren Händler in Niveaus basierend auf dem Transaktionsvolumen:

**Visa-Händlerniveaus**:

| Niveau | Transaktionsvolumen (jährlich) | Validierungsanforderung |
|--------|-------------------------------|-------------------------|
| **Niveau 1** | > 6 Millionen Visa-Transaktionen | Jährlicher Compliance-Bericht (ROC) durch QSA + Quartalsweise Netzwerk-Scans |
| **Niveau 2** | 1–6 Millionen Visa-Transaktionen | Jährlicher Self-Assessment Questionnaire (SAQ) + Quartalsweise Netzwerk-Scans |
| **Niveau 3** | 20.000 – 1 Million Visa-E-Commerce-Transaktionen | Jährlicher SAQ + Quartalsweise Netzwerk-Scans |
| **Niveau 4** | < 20.000 Visa-E-Commerce ODER < 1 Million Visa-Transaktionen gesamt | Jährlicher SAQ + Quartalsweise Netzwerk-Scans (kann je nach Acquirer variieren) |

**Hinweis**: Andere Zahlungsmarken (Mastercard, Amex, Discover) haben ähnliche, aber leicht abweichende Niveaudefinitionen. Organisationen sollten die Anforderungen mit ihrer Akquisitionsbank prüfen.

## Karteninhaberdaten (CHD) und Sensible Authentifizierungsdaten (SAD)

**Karteninhaberdaten (CHD)**:

- **Primäre Kontonummer (PAN)**: Die 13–19-stellige Zahlungskartennummer
- **Karteninhabername**: Name auf der Karte
- **Ablaufdatum**: Kartenablaufdatum
- **Servicecode**: 3-stelliger Code auf dem Magnetstreifen

**Sensible Authentifizierungsdaten (SAD)** – DÜRFEN nach der Autorisierung NICHT gespeichert werden:

- **Vollständige Magnetstreifendaten** (Track 1, Track 2 oder äquivalente Chip-Daten)
- **Kartenprüfnummer/-wert** (CVV/CVC/CVV2/CID – 3- oder 4-stelliger Code)
- **PIN / PIN-Block**: Persönliche Identifikationsnummer

**Kritische Regel**: SAD darf NIEMALS nach Abschluss der Transaktionsautorisierung gespeichert werden, auch nicht verschlüsselt.

## Karteninhaberdaten-Umgebung (CDE)

**Definition**: Personen, Prozesse und Technologien, die Karteninhaberdaten oder SAD speichern, verarbeiten oder übertragen, einschließlich verbundener Systeme.

**CDE-Komponenten**:

- **Geltungsbereich-Systeme**: Systeme, die CHD speichern, verarbeiten oder übertragen
- **Verbundene Systeme**: Systeme, die Sicherheitsdienste für Geltungsbereich-Systeme bereitstellen oder die CDE-Sicherheit beeinflussen könnten
- **Systeme ausserhalb des Geltungsbereichs**: Ordnungsgemäß segmentierte Systeme ohne Auswirkung auf die CDE

**Strategien zur Geltungsbereichsreduzierung**:

- **Tokenisierung**: PAN durch ein nicht-sensibles Token ersetzen
- **Point-to-Point-Verschlüsselung (P2PE)**: Am Eingabepunkt verschlüsseln, ausserhalb der Händlerumgebung entschlüsseln
- **Netzwerksegmentierung**: CDE vom restlichen Netzwerk isolieren
- **Datenspeicherung reduzieren**: CHD nicht speichern, wenn nicht erforderlich
- **Outsourcing**: Validierte Zahlungsverarbeiter nutzen (reduziert Händler-Geltungsbereich)

## Anwendbarkeitsbestimmung

**PCI DSS gilt für [Organisation], WENN**:

| Kriterium | Status | Nachweis |
|-----------|--------|---------|
| Karteninhaberdaten (PAN) werden gespeichert | ⬜ Ja ⬜ Nein | [Beschreibung der Speicherung] |
| Karteninhaberdaten (PAN) werden verarbeitet | ⬜ Ja ⬜ Nein | [Beschreibung der Verarbeitung] |
| Karteninhaberdaten (PAN) werden übertragen | ⬜ Ja ⬜ Nein | [Beschreibung der Übertragung] |
| Systeme sind mit der CDE verbunden | ⬜ Ja ⬜ Nein | [Beschreibung der Verbindungen] |
| Dienstleistungen für Entitäten, die CHD verarbeiten, werden erbracht | ⬜ Ja ⬜ Nein | [Dienstleistertyp] |

**Bei EINEM „Ja"**: PCI-DSS-Anforderungen sind gemäß POL-00 Abschnitt 3.4 **Tier 1 (Pflichtige Compliance)**

**Bei ALLEN „Nein"**: PCI-DSS-Anforderungen verbleiben in **Tier 3 (Informationsreferenz)** gemäß POL-00

**Transaktionsvolumen** (falls zutreffend): [Jährliches Volumen] → Händlerniveau: [1/2/3/4]

---

# PCI-DSS-Struktur – 6 Kontrollziele und 12 Anforderungen

```
┌─────────────────────────────────────────────────────────────────┐
│              PCI DSS v4.0.1 STRUKTUR                            │
├─────────────────────────────────────────────────────────────────┤
│  SICHERES NETZWERK UND SYSTEME AUFBAUEN UND PFLEGEN             │
│    1. Netzwerksicherheitskontrollen installieren und pflegen     │
│    2. Sichere Konfigurationen für alle Systemkomponenten        │
│       anwenden                                                  │
├─────────────────────────────────────────────────────────────────┤
│  KARTENINHABERDATEN SCHÜTZEN                                     │
│    3. Gespeicherte Kontodaten schützen                          │
│    4. Karteninhaberdaten mit starker Kryptografie bei           │
│       Übertragung über offene, öffentliche Netzwerke schützen  │
├─────────────────────────────────────────────────────────────────┤
│  PROGRAMM ZUM SCHWACHSTELLENMANAGEMENT PFLEGEN                  │
│    5. Alle Systeme und Netzwerke vor Schadsoftware schützen     │
│    6. Sichere Systeme und Software entwickeln und pflegen       │
├─────────────────────────────────────────────────────────────────┤
│  STARKE ZUGANGSKONTROLLMASSNAHMEN IMPLEMENTIEREN                │
│    7. Zugang zu Karteninhaberdaten nach Geschäftsbedarf         │
│       einschränken                                              │
│    8. Nutzer identifizieren und Zugang zu Systemkomponenten     │
│       authentifizieren                                          │
│    9. Physischen Zugang zu Karteninhaberdaten einschränken      │
├─────────────────────────────────────────────────────────────────┤
│  NETZWERKE REGELMÄSSIG ÜBERWACHEN UND TESTEN                    │
│   10. Alle Zugriffe auf Systemkomponenten und Kartendaten       │
│       protokollieren und überwachen                             │
│   11. Sicherheit von Systemen und Netzwerken regelmässig testen │
├─────────────────────────────────────────────────────────────────┤
│  INFORMATIONSSICHERHEITSRICHTLINIE PFLEGEN                      │
│   12. Informationssicherheit durch organisatorische Richtlinien │
│       und Programme unterstützen                                │
└─────────────────────────────────────────────────────────────────┘
```

---

# Detaillierte Anforderungen

## Anforderung 1: Netzwerksicherheitskontrollen installieren und pflegen

**Ziel**: Firewalls und Router sind für die Netzwerksicherheit unerlässlich und kontrollieren den Datenverkehr zwischen nicht vertrauenswürdigen Netzwerken und der CDE.

**Wesentliche Unteranforderungen**:

**1.1 Prozesse und Mechanismen für die Installation und Pflege von Netzwerksicherheitskontrollen**

- Dokumentierte Prozesse für Netzwerksicherheitskontrollen
- Rollen und Verantwortlichkeiten zugewiesen
- Jährliche Überprüfung und Aktualisierung

**1.2 Netzwerksicherheitskontrollen (NSCs) konfiguriert und gepflegt**

- **1.2.1**: Konfigurationsstandards für NSCs definiert und umgesetzt
- **1.2.2**: Deny-All, Permit-by-Exception Firewall-Regelwerke
- **1.2.3**: Ein- und ausgehender Datenverkehr auf das Notwendige beschränkt
- **1.2.4**: Regeln dokumentiert und begründet (Geschäftsbedarf)
- **1.2.5**: Firewall-Regeln mindestens alle 6 Monate überprüft
- **1.2.6**: Änderungen an NSC-Regelwerken genehmigt
- **1.2.7**: Konfigurationen auf Sicherheitsparameter überprüft

**1.3 Netzwerkzugang zur und von der CDE eingeschränkt**

- **1.3.1**: Eingehender Datenverkehr zur CDE eingeschränkt
- **1.3.2**: Ausgehender Datenverkehr aus der CDE autorisiert
- **1.3.3**: NSCs zwischen Drahtlosnetzwerken und CDE installiert

**1.4 Netzwerkverbindungen zwischen vertrauenswürdigen und nicht vertrauenswürdigen Netzwerken kontrolliert**

- **1.4.1**: NSCs zur Datenverkehrskontrolle umgesetzt
- **1.4.2**: Konfigurationen entsprechen dem „Deny All"-Prinzip
- **1.4.3**: Anti-Spoofing-Massnahmen umgesetzt
- **1.4.4**: Systemkomponenten geben keine internen IP-Adressen preis
- **1.4.5**: Öffentlich zugängliche Webanwendungen geschützt (WAF oder gleichwertig) – **[Neu v4.0.1, Best Practice bis 31. März 2025]**

**1.5 Risiken für die CDE durch Rechengeräte, die mit nicht vertrauenswürdigen Netzwerken und der CDE verbunden werden können, werden verwaltet**

- **1.5.1**: Personal-Firewall-Software oder gleichwertige Kontrollen eingesetzt

**Zuordnung zu ISO 27001:2022**:

- A.8.20: Netzwerksicherheit
- A.8.21: Sicherheit von Netzwerkdiensten
- A.8.22: Netzwerksegmentierung
- A.8.23: Web-Filterung

---

## Anforderung 2: Sichere Konfigurationen für alle Systemkomponenten anwenden

**Ziel**: Böswillige Akteure zielen auf Standard-Konten und -Einstellungen ab. Sichere Konfigurationen müssen angewendet werden.

**Wesentliche Unteranforderungen**:

**2.1 Prozesse und Mechanismen für die Anwendung sicherer Konfigurationen**

- Konfigurationsstandards dokumentiert
- Regelmässige Konfigurationsüberprüfungen

**2.2 Systemkomponenten sicher konfiguriert und verwaltet**

- **2.2.1**: Herstellerstandard-Einstellungen vor der Produktion geändert
- **2.2.2**: Vom Hersteller bereitgestellte Standard-Passwörter geändert (oder deaktiviert)
- **2.2.3**: Primäre Funktionen, die unterschiedliche Sicherheitsniveaus erfordern, durch separate Komponenten verwaltet (z. B. Webserver, Datenbankserver getrennt)
- **2.2.4**: Unsichere Dienste, Protokolle, Daemons entfernt oder deaktiviert
- **2.2.5**: Sicherheitsdienste und -parameter konfiguriert
- **2.2.6**: Sicherheitsparameter konfiguriert, um Missbrauch zu verhindern
- **2.2.7**: Nicht-konsolenbasierter Verwaltungszugang mit starker Kryptografie verschlüsselt

**2.3 Drahtlose Umgebungen sicher konfiguriert und verwaltet**

- **2.3.1**: Drahtlose Herstellerstandards geändert
- **2.3.2**: Drahtlose Netzwerke mit starker Kryptografie gesichert (WPA2/WPA3)

**Zuordnung zu ISO 27001:2022**:

- A.8.9: Konfigurationsmanagement
- A.8.19: Installation von Software auf Betriebssystemen
- A.8.1: Benutzer-Endgeräte

---

## Anforderung 3: Gespeicherte Kontodaten schützen

**Ziel**: Gespeicherte Karteninhaberdaten sind ein Hauptangriffsziel. Schutzmassnahmen müssen vorhanden sein.

**Wesentliche Unteranforderungen**:

**3.1 Prozesse und Mechanismen zum Schutz gespeicherter Kontodaten**

- Richtlinien zur Datenspeicherung und -löschung
- Dokumentation der CHD-Speicherorte

**3.2 Speicherung von Kontodaten auf ein Minimum beschränkt**

- **3.2.1**: Kontodatenspeicherung minimiert
- Richtlinien zur Datenspeicherung begrenzen Speichermenge und -dauer

**3.3 Sensible Authentifizierungsdaten (SAD) werden nach der Autorisierung nicht gespeichert**

- **3.3.1**: SAD nach der Autorisierung nicht aufbewahrt – **KRITISCHE REGEL**
- **3.3.2**: SAD vor der Autorisierung gespeichert, nicht wiederherstellbar gemacht
- **3.3.3**: PANs nicht angezeigt, wenn nicht erforderlich (Maskierung)

**3.4 Zugang zu vollständigen PAN-Anzeigen eingeschränkt**

- **3.4.1**: PAN bei Anzeige maskiert (maximal erste 6 und letzte 4 Stellen)
- **3.4.2**: Technische Kontrollen erzwingen Maskierung – **[Neu v4.0.1, Best Practice bis 31. März 2025]**

**3.5 Primäre Kontonummer (PAN) überall gesichert, wo sie gespeichert wird**

- **3.5.1**: PAN unleserlich gemacht (Verschlüsselung, Trunkierung, Hashing, Tokenisierung)
- **3.5.1.1**: Hashes verwenden Keyed Hash (HMAC) und Schlüssel gesichert – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **3.5.1.2**: PANs mit Festplatten- oder Partitionsebenen-Verschlüsselung gesichert – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **3.5.1.3**: Kryptoperiodenzeiten definiert und umgesetzt

**3.6 Kryptografische Schlüssel zum Schutz gespeicherter Kontodaten sind gesichert**

- **3.6.1**: Verfahren für das Schlüsselmanagement definiert und umgesetzt
- **3.6.2**: Schlüssel sicher gespeichert (geringstmögliche Standorte, verschlüsselte Speicherung)
- **3.6.3**: Schlüsselmanagement auf wenige Verwalter beschränkt
- **3.6.4**: Schlüsselmanagement für kryptografische Schlüssel, die das Ende der Kryptoperiodenzeit erreicht haben
- **3.6.5**: Schlüsselverwalter-Bestätigung
- **3.6.6**: Sichere kryptografische Schlüsselverteilung
- **3.6.7**: Verhinderung unbefugter Schlüsselersetzung
- **3.6.8**: Anforderung, dass Schlüsselverwalter das Verständnis ihrer Verantwortlichkeiten formal bestätigen

**3.7 Schlüsselmanagementprozesse und -verfahren wo Kryptografie genutzt wird**

- **3.7.1**: Schlüsselmanagement-Richtlinien und -verfahren gepflegt
- **3.7.2**: Kryptografisches Schlüsselmanagement
- **3.7.3**: Schlüsselwiderrufsprozess
- **3.7.4**: Entfernung oder Vernichtung von Schlüsseln
- **3.7.5**: Schlüsselwechsel bei Integritätskompromittierung
- **3.7.6**: Schlüsselsplits sicher gespeichert (für manuelles Schlüsselmanagement)
- **3.7.7**: Verhinderung unbefugter Ersetzung
- **3.7.8**: Schlüsselverwalter bestätigen Verantwortlichkeiten formal
- **3.7.9**: Hardware- und Software-Inventar kryptografischer Geräte – **[Neu v4.0.1, Best Practice bis 31. März 2025]**

**Zuordnung zu ISO 27001:2022**:

- A.8.24: Verwendung von Kryptografie
- A.8.10: Datenlöschung
- A.8.11: Datenmaskierung

---

## Anforderung 4: Karteninhaberdaten mit starker Kryptografie bei der Übertragung schützen

**Ziel**: Über öffentliche Netzwerke übertragene Karteninhaberdaten müssen verschlüsselt werden.

**Wesentliche Unteranforderungen**:

**4.1 Prozesse und Mechanismen zum Schutz von Karteninhaberdaten mit starker Kryptografie bei der Übertragung**

- Inventar der CHD-Übertragungspunkte
- Kryptografie-Richtlinien und -verfahren

**4.2 PAN mit starker Kryptografie bei der Übertragung geschützt**

- **4.2.1**: Starke Kryptografie und Sicherheitsprotokolle schützen PAN bei Übertragung über offene, öffentliche Netzwerke
- **4.2.1.1**: Inventar vertrauenswürdiger Schlüssel und Zertifikate – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **4.2.2**: PAN nicht über Endnutzer-Messaging-Technologien gesendet

**Zuordnung zu ISO 27001:2022**:

- A.8.24: Verwendung von Kryptografie
- A.5.14: Informationsübertragung

**Verschlüsselungsstandards**:

- TLS 1.2 Minimum (TLS 1.3 bevorzugt)
- Starke Cipher-Suites (keine veralteten Algorithmen)
- Kein SSL, keine frühen TLS-Versionen

---

## Anforderung 5: Alle Systeme und Netzwerke vor Schadsoftware schützen

**Ziel**: Schadsoftware nutzt Schwachstellen aus. Anti-Malware-Schutz muss eingesetzt werden.

**Wesentliche Unteranforderungen**:

**5.1 Prozesse und Mechanismen zum Schutz aller Systeme und Netzwerke vor Schadsoftware**

- Deployment-Plan für Anti-Malware-Lösung
- Regelmässige Aktualisierungen und Überprüfungen

**5.2 Schadsoftware verhindert, erkannt und behandelt**

- **5.2.1**: Anti-Malware-Lösungen auf allen Systemen eingesetzt (häufig von Schadsoftware betroffen)
- **5.2.2**: Anti-Malware-Mechanismen gepflegt (aktuell, aktiv, protokolliert)
- **5.2.3**: Anti-Malware-Mechanismen können nicht deaktiviert oder verändert werden

**5.3 Anti-Phishing-Mechanismen schützen Nutzer vor Phishing-Angriffen**

- **5.3.1**: Prozesse zur Erkennung und zum Schutz des Personals vor Phishing-Angriffen umgesetzt
- **5.3.2**: Anti-Phishing-Mechanismen gepflegt und regelmässig bewertet – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **5.3.3**: Anti-Phishing-Mechanismen schützen vor Bedrohungen – **[Neu v4.0.1, Best Practice bis 31. März 2025]**

**5.4 Anti-Malware-Mechanismen und -Prozesse aktiv und gepflegt**

- **5.4.1**: Anti-Malware-Protokolle aufbewahrt und überprüft

**Zuordnung zu ISO 27001:2022**:

- A.8.7: Schutz vor Schadsoftware
- A.5.7: Bedrohungsintelligenz

---

## Anforderung 6: Sichere Systeme und Software entwickeln und pflegen

**Ziel**: Schwachstellen in Systemen und Software ermöglichen Angreifern die Kompromittierung von CHD.

**Wesentliche Unteranforderungen**:

**6.1 Prozesse und Mechanismen für die Entwicklung und Pflege sicherer Systeme und Software**

- Sicherer Entwicklungslebenszyklus
- Änderungskontrollverfahren

**6.2 Individuelle und massgeschneiderte Software sicher entwickelt**

- **6.2.1**: Individuelle und massgeschneiderte Software sicher entwickelt
- **6.2.2**: Softwareentwickler in sicherer Codierung geschult
- **6.2.3**: Code-Reviews für individuelle und massgeschneiderte Software vor der Produktion – **[Aktualisiert v4.0.1]**
- **6.2.4**: Software-Engineering-Techniken in der Entwicklung zur Vermeidung häufiger Schwachstellen

**6.3 Sicherheitsschwachstellen identifiziert und behandelt**

- **6.3.1**: Sicherheitsschwachstellen mit branchenakzeptierten Methoden identifiziert und bewertet
- **6.3.2**: Inventar von individueller und massgeschneiderter Software sowie Drittanbieterkomponenten
- **6.3.3**: Alle Systemkomponenten und Software vor bekannten Schwachstellen geschützt (Patches angewendet)
- **6.3.4**: Relevante Patches/Sicherheitsupdates überprüft und innerhalb definierter Zeiträume eingesetzt

**Patch-Zeitpläne** (6.3.4):

- **Kritische Schwachstellen**: Maximal 30 Tage
- **Hohe Schwachstellen**: Gemäss organisatorischer Risikoeinstufung (in der Regel 30–90 Tage)
- **Andere Schwachstellen**: Risikobasierter Ansatz

**6.4 Öffentlich zugängliche Webanwendungen vor Angriffen geschützt**

- **6.4.1**: Öffentlich zugängliche Webanwendungen geschützt (automatisierte technische Lösung, manuelle Überprüfung, WAF)
- **6.4.2**: Techniken zur Skript-Integrität der Zahlungsseite – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **6.4.3**: HTTP-Header zum Browser-Schutz vor Angriffen

**6.5 Änderungen an allen Systemkomponenten sicher verwaltet**

- **6.5.1**: Änderungen gemäss Änderungskontrollverfahren verwaltet
- **6.5.2**: Änderungen an Systemen auf Sicherheitsauswirkungen überprüft
- **6.5.3**: Individuelle und massgeschneiderte Software-Änderungen vor der Bereitstellung überprüft
- **6.5.4**: Testdaten und -konten vor der Produktion entfernt
- **6.5.5**: Änderungskontrollverfahren dokumentiert
- **6.5.6**: Produktionsdaten nicht für Tests/Entwicklung verwendet

**Zuordnung zu ISO 27001:2022**:

- A.8.8: Management technischer Schwachstellen
- A.8.25: Sicherer Entwicklungslebenszyklus
- A.8.26: Anwendungssicherheitsanforderungen
- A.8.27: Sichere Systemarchitektur und Engineering-Prinzipien
- A.8.28: Sicheres Coding
- A.8.29: Sicherheitstests in der Entwicklung und Abnahme
- A.8.30: Ausgelagerte Entwicklung
- A.8.31: Trennung von Entwicklungs-, Test- und Produktionsumgebungen
- A.8.32: Änderungsmanagement
- A.8.33: Testinformationen

---

## Anforderung 7: Zugang zu Karteninhaberdaten nach Geschäftsbedarf einschränken

**Ziel**: Zugang zu CHD muss auf diejenigen beschränkt werden, die ihn für ihre Arbeit benötigen.

**Wesentliche Unteranforderungen**:

**7.1 Prozesse und Mechanismen zur Einschränkung des Zugangs zu Systemkomponenten und Karteninhaberdaten**

- Zugriffskontrollrichtlinien definiert
- Rollen und Verantwortlichkeiten

**7.2 Zugang zu Systemkomponenten und Daten angemessen definiert und zugewiesen**

- **7.2.1**: Zugang basierend auf Stellenklassifizierung und -funktion gewährt (Need-to-know)
- **7.2.2**: Zugang basierend auf geringstem Privileg zugewiesen
- **7.2.3**: Erforderliche Rechte durch autorisiertes Personal genehmigt
- **7.2.4**: Zugriffsrechte mindestens einmal alle 6 Monate überprüft
- **7.2.5**: Privilegierte Konten bestimmten Nutzern zugewiesen – **[Aktualisiert v4.0.1]**
- **7.2.6**: Alle Benutzerzugriffe auf Repositories gespeicherter CHD eingeschränkt

**7.3 Zugang zu Systemkomponenten und Daten über Zugangskontrollsysteme verwaltet**

- **7.3.1**: Zugangskontrollsysteme für Systemkomponenten vorhanden
- **7.3.2**: Zugangskontrollsysteme konfiguriert, um Berechtigungen durchzusetzen (Deny-All-Prinzip)
- **7.3.3**: Zugangskontrollsysteme konfiguriert, um Rechteerweiterungen zu verhindern

**Zuordnung zu ISO 27001:2022**:

- A.5.15: Zugangskontrolle
- A.5.18: Zugriffsrechte
- A.8.2: Privilegierte Zugriffsrechte
- A.8.3: Informationszugangsbeschränkung

---

## Anforderung 8: Nutzer identifizieren und Zugang zu Systemkomponenten authentifizieren

**Ziel**: Authentifizierung stellt sicher, dass Nutzer tatsächlich diejenigen sind, die sie zu sein behaupten, bevor sie auf Systeme zugreifen.

**Wesentliche Unteranforderungen**:

**8.1 Prozesse und Mechanismen zur Identifizierung von Nutzern und Authentifizierung des Zugangs**

- Richtlinien zur Nutzeridentifizierung und -authentifizierung

**8.2 Nutzeridentifikation und zugehörige Konten streng verwaltet**

- **8.2.1**: Eindeutige ID vor Zugriffsgewährung zugewiesen
- **8.2.2**: Gemeinsame IDs verboten (außer ausdrücklich genehmigt)
- **8.2.3**: Generische Konten nur wenn notwendig verwendet (genehmigt, kontrolliert)
- **8.2.4**: Dienstanbieter-Personal mit Fernzugang hat individuelle Zugangsdaten
- **8.2.5**: Gemeinsame Dienstanbieter-Konten verwenden MFA – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **8.2.6**: Anwendungs- und Systemkonten verwaltet, um Missbrauch zu verhindern
- **8.2.7**: Benutzerkonten zeitnah hinzugefügt, gelöscht oder geändert
- **8.2.8**: Ungültige Authentifizierungsversuche führen zur Kontosperrung (nach maximal 10 Versuchen)

**8.3 Starke Authentifizierung für Nutzer und Administratoren eingerichtet und verwaltet**

- **8.3.1**: Multi-Faktor-Authentifizierung (MFA) für alle Zugänge zur CDE
- **8.3.2**: MFA für alle Netzwerkzugänge (Fern- und intern)
- **8.3.3**: MFA-Systeme konfiguriert, um Missbrauch zu verhindern
- **8.3.4**: MFA für alle Verwaltungszugänge erforderlich
- **8.3.5**: MFA für alle CDE-Zugänge verwendet Faktoren aus zwei verschiedenen Kategorien – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **8.3.6**: Phishing-resistente MFA für Personal mit Verwaltungszugang – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **8.3.7**: MFA für Anwendungs- und Systemkonten zur Ausführung privilegierter Befehle – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **8.3.8**: MFA für Dienstanbieter mit Fernzugang zu Systemen der Entität – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **8.3.9**: Starke kryptografische Authentifizierung für nicht-konsolenbasierten Verwaltungszugang
- **8.3.10**: Nutzerauthentifizierungsmethoden der Umgebung der Entität angemessen

**8.4 Multi-Faktor-Authentifizierung (MFA) für den Zugang zur CDE umgesetzt**

- **[Neu v4.0.1, konsolidiert aus verschiedenen 8.3-Anforderungen]**

**8.5 Passwörter und Passphrasen erfüllen Mindeststärke-Anforderungen**

- **8.5.1**: Passwörter/Passphrasen mindestens 12 Zeichen (oder 8, wenn System 12 nicht unterstützt) – **[Aktualisiert v4.0.1]**

**8.6 Verwendung von Anwendungs- und Systemkonten und zugehörigen Authentifizierungsfaktoren streng verwaltet**

- **8.6.1**: Anwendungs- und Systemkonten gesichert (kein interaktiver Login möglich)
- **8.6.2**: Passwörter/Passphrasen bei vermutetem oder bekanntem Kompromittierung geändert
- **8.6.3**: Passwörter/Passphrasen zur Missbrauchsverhinderung verwaltet

**Zuordnung zu ISO 27001:2022**:

- A.5.16: Identitätsmanagement
- A.5.17: Authentifizierungsinformationen
- A.8.5: Sichere Authentifizierung

---

## Anforderung 9: Physischen Zugang zu Karteninhaberdaten einschränken

**Ziel**: Physischer Zugang zu Systemen und Medien, die CHD enthalten, muss kontrolliert werden.

**Wesentliche Unteranforderungen**:

**9.1 Prozesse und Mechanismen zur Einschränkung des physischen Zugangs zu Karteninhaberdaten**

- Richtlinien und Verfahren zur physischen Sicherheit

**9.2 Physische Zugangskontrollen verwalten den Eintritt in Einrichtungen und Systeme mit Karteninhaberdaten**

- **9.2.1**: Physische Zugangskontrollen zur Beschränkung des Zugangs zu CDE-Systemen
- **9.2.2**: Logische und physische Zugangskontrolle sicherstellt, dass nur autorisiertes Personal Zugang hat
- **9.2.3**: Physischer Zugang für Personal sofort nach Kündigung entzogen
- **9.2.4**: Besucherzugangsverfahren und Besucherausweis-System
- **9.2.5**: Physische Zugangskontrollen für Drahtloszugriffspunkte
- **9.2.6**: Physische Zugriffsprotokolle mindestens einmal alle 3 Monate überprüft
- **9.2.7**: Videokameras oder Zugangskontrollmechanismen überwachen sensible Bereiche

**9.3 Physischer Zugang für Personal und Besucher autorisiert und verwaltet**

- **9.3.1**: Besucher autorisiert und in CHD-Bereichen begleitet
- **9.3.2**: Besucherausweis-System unterscheidet Besucher von Personal
- **9.3.3**: Besucherausweise vor dem Verlassen abgegeben oder deaktiviert

**9.4 Medien mit Karteninhaberdaten sicher gespeichert, aufgerufen, verteilt und vernichtet**

- **9.4.1**: Medien mit CHD an sicherem Ort gespeichert (Offsite-Backups gesichert)
- **9.4.2**: Medien nach Sensibilität klassifiziert
- **9.4.3**: Medien per Sicherheitskurier gesendet (Tracking verwendet)
- **9.4.4**: Managementgenehmigung für Medien, die gesicherte Bereiche verlassen
- **9.4.5**: Medien mindestens jährlich inventarisiert
- **9.4.6**: Medien bei Nichtmehrbedarf vernichtet (Kreuzschnitt-Schredder, Verbrennung, Entmagnetisierung)
- **9.4.7**: Medien mit CHD bei Nichtmehrbedarf aus geschäftlichen/rechtlichen Gründen vernichtet

**9.5 Point-of-Interaction (POI)-Geräte vor Manipulation und unbefugter Ersetzung geschützt**

- **9.5.1**: POI-Geräte vor Manipulation geschützt (manipulationsaufdeckende Siegel usw.)
- **9.5.2**: Verfahren zur Erkennung und Meldung von Manipulation/Ersetzung
- **9.5.3**: Schulung des Personals zur Erkennung von Manipulations-/Ersetzungsversuchen

**Zuordnung zu ISO 27001:2022**:

- A.7.1: Physische Sicherheitsbereiche
- A.7.2: Physischer Eintritt
- A.7.3: Sicherung von Büros, Räumen und Einrichtungen
- A.7.4: Physische Sicherheitsüberwachung
- A.7.7: Klarer Schreibtisch und klarer Bildschirm
- A.7.8: Standort und Schutz von Geräten
- A.7.10: Speichermedien
- A.7.14: Sichere Entsorgung oder Wiederverwendung von Geräten

---

## Anforderung 10: Alle Zugriffe auf Systemkomponenten und Karteninhaberdaten protokollieren und überwachen

**Ziel**: Protokollierungsmechanismen und die Möglichkeit, Benutzeraktivitäten zu verfolgen, sind kritisch für die Verhinderung, Erkennung oder Minimierung der Auswirkungen einer Datenkompromittierung.

**Wesentliche Unteranforderungen**:

**10.1 Prozesse und Mechanismen für die Protokollierung und Überwachung aller Zugriffe**

- Richtlinien zur Protokollierung und Überwachung definiert

**10.2 Audit-Protokolle umgesetzt zur Unterstützung der Anomalie- und Verdachtsaktivitätserkennung**

- **10.2.1**: Audit-Protokolle aktiviert und aktiv für Systemkomponenten
- **10.2.2**: Audit-Protokolle erfassen: Nutzer-ID, Ereignistyp, Datum/Uhrzeit, Erfolg/Misserfolg, Herkunft, Identität/Name betroffener Daten/Systemkomponente

**10.3 Audit-Protokolle vor Vernichtung und unbefugter Änderung geschützt**

- **10.3.1**: Lesezugang zu Audit-Protokolldateien auf Berechtigte beschränkt
- **10.3.2**: Audit-Protokolldateien vor unbefugter Änderung geschützt
- **10.3.3**: Audit-Protokolldateien umgehend auf sicheren zentralen Log-Server gesichert
- **10.3.4**: Dateiintegritäts-Überwachung oder Änderungserkennungssoftware für Audit-Protokolle verwendet

**10.4 Audit-Protokolle zur Identifizierung von Anomalien oder Verdachtsaktivitäten überprüft**

- **10.4.1**: Sicherheitsrichtlinien und -verfahren identifizieren Anomalien und Verdachtsaktivitäten
- **10.4.1.1**: Automatisierte Mechanismen alarmieren Personal bei Anomalien oder Verdachtsaktivitäten – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **10.4.2**: Audit-Protokolle mindestens täglich überprüft
- **10.4.3**: Bei der Überprüfung identifizierte Ausnahmen und Anomalien behandelt

**10.5 Audit-Protokoll-Verlauf aufbewahrt und für Analysen verfügbar**

- **10.5.1**: Audit-Protokoll-Verlauf mindestens 12 Monate aufbewahrt (mindestens 3 Monate sofort verfügbar)

**10.6 Zeitsynchronisierungsmechanismen unterstützen konsistente Zeiteinstellungen**

- **10.6.1**: Systemuhren mit Zeitsynchronisierungstechnologie synchronisiert
- **10.6.2**: Zeitsynchronisierungstechnologien konsistent konfiguriert
- **10.6.3**: Kritische Zeitserver akzeptieren Zeit von externen Quellen (Stratum 0 oder 1)

**10.7 Ausfälle kritischer Sicherheitskontrollsysteme erkannt, gemeldet und umgehend beantwortet**

- **10.7.1**: Zusätzliche Anforderung nur für Dienstleister – Ausfälle erkannt und gemeldet – **[Neu v4.0.1]**
- **10.7.2**: Zusätzliche Anforderung nur für Dienstleister – Ausfälle umgehend beantwortet – **[Neu v4.0.1]**
- **10.7.3**: Zusätzliche Anforderung nur für Dienstleister – Ausfälle umfassen Wiederherstellung der Sicherheitsfunktionen – **[Neu v4.0.1]**

**Zuordnung zu ISO 27001:2022**:

- A.8.15: Protokollierung
- A.8.16: Überwachungsaktivitäten

---

## Anforderung 11: Sicherheit von Systemen und Netzwerken regelmässig testen

**Ziel**: Schwachstellen werden kontinuierlich entdeckt. Regelmässige Tests identifizieren und bestätigen, dass Kontrollen vorhanden sind.

**Wesentliche Unteranforderungen**:

**11.1 Prozesse und Mechanismen für regelmässige Sicherheitstests**

- Testrichtlinien und -verfahren definiert

**11.2 Drahtlose Zugangspunkte identifiziert und überwacht**

- **11.2.1**: Autorisierte und nicht autorisierte drahtlose Zugangspunkte erkannt
- **11.2.2**: Drahtlose IDS/IPS oder gleichwertig eingesetzt

**11.3 Externe und interne Schwachstellen regelmässig identifiziert, priorisiert und behandelt**

- **11.3.1**: Interne Schwachstellen-Scans mindestens einmal alle 3 Monate
- **11.3.2**: Externe Schwachstellen-Scans mindestens einmal alle 3 Monate (durch Approved Scanning Vendor – ASV)
- **11.3.3**: Externe und interne Penetrationstests durchgeführt

**Penetrationstests (11.4)**:

- **11.4.1**: Penetrationstest-Methodik definiert und umgesetzt
- **11.4.2**: Interne Penetrationstests mindestens einmal alle 12 Monate
- **11.4.3**: Externe Penetrationstests mindestens einmal alle 12 Monate
- **11.4.4**: Ausnutzbare Schwachstellen aus Penetrationstests behoben
- **11.4.5**: Segmentierungskontrollen getestet (bei Netzwerksegmentierung zur Geltungsbereichs-einschränkung)
- **11.4.6**: Zusätzliche Anforderung für Dienstleister – Penetrationstests nach wesentlichen Infrastruktur-/Anwendungs-Upgrades
- **11.4.7**: Multi-Tenant-Dienstleister unterstützen Kunden-Penetrationstests oder stellen Testnachweise bereit – **[Neu v4.0.1, Best Practice bis 31. März 2025]**

**11.5 Netzwerksicherheitskontrollen vorhanden und wirksam**

- **11.5.1**: Änderungserkennungsmechanismen eingesetzt
- **11.5.2**: Änderungserkennungsmechanismen konfiguriert, Personal zu alarmieren

**11.6 Unbefugte Änderungen an Zahlungsseiten erkannt und beantwortet**

- **11.6.1**: Änderungs- und Manipulationserkennungsmechanismus auf Zahlungsseiten eingesetzt – **[Aktualisiert v4.0.1]**

**Zuordnung zu ISO 27001:2022**:

- A.8.8: Management technischer Schwachstellen
- A.5.7: Bedrohungsintelligenz
- A.8.34: Schutz von Informationssystemen bei Audit-Tests

---

## Anforderung 12: Informationssicherheit durch organisatorische Richtlinien und Programme unterstützen

**Ziel**: Sicherheitsrichtlinien und -verfahren setzen Erwartungen und leiten Personal in seinen täglichen Aufgaben.

**Wesentliche Unteranforderungen**:

**12.1 Eine übergeordnete Informationssicherheitsrichtlinie eingerichtet und veröffentlicht**

- **12.1.1**: Sicherheitsrichtlinie eingerichtet, dokumentiert, kommuniziert
- **12.1.2**: Sicherheitsrichtlinie mindestens jährlich überprüft und bei Bedarf aktualisiert
- **12.1.3**: Rollen und Verantwortlichkeiten für Sicherheit zugewiesen
- **12.1.4**: Oberste Unternehmensführung hat letztendliche Verantwortung für den Schutz von CHD

**12.2 Acceptable-Use-Richtlinien für Endnutzertechnologien definiert und umgesetzt**

- **12.2.1**: Acceptable-Use-Richtlinie für Endnutzertechnologien definiert

**12.3 Risiken für die Karteninhaberdaten-Umgebung formal identifiziert, bewertet und verwaltet**

- **12.3.1**: Zielgerichtete Risikoanalyse mindestens einmal alle 12 Monate
- **12.3.2**: Zielgerichtete Risikoanalyse bei wesentlichen Änderungen
- **12.3.3**: Risikoanalyseergebnisse überprüft und dokumentiert
- **12.3.4**: PCI-DSS-Compliance-Programm mindestens vierteljährlich auf Betrieb bestätigt

**12.4 PCI-DSS-Compliance verwaltet**

- **12.4.1**: Verantwortlichkeiten für das PCI-DSS-Management zugewiesen
- **12.4.2**: Oberste Unternehmensführung pflegt Bewusstsein und Aufsicht

**12.5 PCI-DSS-Geltungsbereich dokumentiert und validiert**

- **12.5.1**: Inventar aller Systemkomponenten im PCI-DSS-Geltungsbereich
- **12.5.2**: Geltungsbereichsbestimmung mindestens einmal alle 12 Monate
- **12.5.2.1**: Auswirkungen von Änderungen auf den PCI-DSS-Geltungsbereich bestimmt – **[Neu v4.0.1, Best Practice bis 31. März 2025]**
- **12.5.3**: Sicherheitsauswirkungen von Änderungen an Systemkomponenten bestimmt

**12.6 Sicherheitsbewusstsein als kontinuierliche Aktivität**

- **12.6.1**: Sicherheitsbewusstseinsprogramm umgesetzt
- **12.6.2**: Personal absolviert Sensibilisierungsschulung bei Einstellung und mindestens einmal alle 12 Monate
- **12.6.3**: Schulungsmaterialien verweisen auf korrekte Sicherheitsrichtlinien und -verfahren
- **12.6.3.1**: Personal erhält Schulung zu Phishing und Social Engineering – **[Neu v4.0.1, Best Practice bis 31. März 2025]**

**12.7 Personal wird geprüft, um Insider-Risiken zu reduzieren**

- **12.7.1**: Potenzielles Personal vor der Einstellung geprüft (Hintergrundprüfungen gemäss lokalem Recht)

**12.8 Risiken durch Drittanbieter-Dienstleister (TPSP) verwaltet**

- **12.8.1**: Liste der TPSPs gepflegt (einschließlich erbrachter Dienstleistungen)
- **12.8.2**: Schriftliche Vereinbarungen mit TPSPs beinhalten Anerkennung der Verantwortung
- **12.8.3**: Prozesse zur Einbindung von TPSPs (Due Diligence vor Beauftragung)
- **12.8.4**: Programm zur Überwachung des PCI-DSS-Compliance-Status von TPSPs
- **12.8.5**: Informationen zu PCI-DSS-Anforderungen gepflegt, die von jedem TPSP verwaltet werden

**12.9 Drittanbieter-Dienstleister (TPSPs) unterstützen PCI-DSS-Compliance ihrer Kunden**

- **12.9.1**: TPSPs bestätigen Verantwortung für CHD-Sicherheit
- **12.9.2**: TPSPs stellen auf Anfrage Informationen für Kunden bereit

**12.10 Mutmassliche und bestätigte Sicherheitsvorfälle werden sofort beantwortet**

- **12.10.1**: Incident-Response-Plan erstellt und gepflegt
- **12.10.2**: Incident-Response-Plan mindestens jährlich getestet
- **12.10.3**: Personal für Incident Response benannt und geschult
- **12.10.4**: Alarmierungs- und Überwachungssysteme vorhanden
- **12.10.5**: Intrusion-Detection/-Prevention-Systeme überwachen gesamten CDE-Datenverkehr
- **12.10.6**: Änderungserkennungsmechanismen überwachen Audit-Protokolle
- **12.10.7**: Incident-Response-Verfahren beinhalten: (i) Rollen/Verantwortlichkeiten, (ii) Kommunikationsstrategie, (iii) spezifische Verfahren, (iv) Geschäftswiederherstellungsverfahren, (v) Datensicherungsprozesse, (vi) gesetzliche Anforderungen, (vii) Forensik

**Zuordnung zu ISO 27001:2022**:

- A.5.1: Richtlinien für Informationssicherheit
- A.5.36: Einhaltung von Richtlinien, Regeln und Standards für Informationssicherheit
- A.6.3: Bewusstsein, Schulung und Ausbildung zur Informationssicherheit
- A.5.24–5.28: Vorfallmanagement
- A.5.19–5.23: Lieferantenbeziehungen
- Klausel 6.1.2–6.1.3: Risikobewertung und -behandlung

---

# PCI DSS v4.0.1 – Neue und aktualisierte Anforderungen

## Stufenweiser Umsetzungszeitplan

**PCI DSS v4.0** führte neue Anforderungen schrittweise ein:

| Anforderungskategorie | Wirksamkeitsdatum | Status |
|-----------------------|-------------------|--------|
| **Alle bestehenden v3.2.1-Anforderungen** | 31. März 2024 | Pflicht |
| **Neue Anforderungen – Zukünftig datiert** | 31. März 2024 – 31. März 2025 | Best Practice |
| **Alle v4.0.1-Anforderungen** | 31. März 2025 | Pflicht |

## Wesentliche neue Anforderungen (ab 31. März 2025 wirksam)

**Erweiterung der Multi-Faktor-Authentifizierung**:

- 8.3.5: MFA muss Faktoren aus zwei verschiedenen Kategorien verwenden (etwas, das man weiß, hat, ist)
- 8.3.6: Phishing-resistente MFA für Verwaltungszugang
- 8.3.7: MFA für privilegierte Anwendungs-/Systemkonten
- 8.3.8: MFA für Dienstanbieter-Fernzugang

**Erweiterte Authentifizierung**:

- 8.5.1: Mindestens 12 Zeichen (vorher 7)

**Kryptografische Verbesserungen**:

- 3.5.1.1: Keyed Hashes (HMAC) für PAN-Hashing erforderlich
- 3.5.1.2: Festplatten-/Partitionsebenen-Verschlüsselung mit Schlüsselmanagement-Trennung
- 3.7.9: Hardware-/Software-Inventar kryptografischer Geräte
- 4.2.1.1: Inventar vertrauenswürdiger Schlüssel und Zertifikate

**Webanwendungssicherheit**:

- 1.4.5: NSCs zwischen Internet und Webanwendungen (WAF oder gleichwertig)
- 6.4.2: Skript-Integritätstechniken für Zahlungsseiten (CSP, SRI usw.)
- 11.6.1: Verbesserte Manipulationserkennung für Zahlungsseiten

**Anti-Phishing**:

- 5.3.2: Anti-Phishing-Mechanismen gepflegt und bewertet
- 5.3.3: Technische Anti-Phishing-Kontrollen umgesetzt
- 12.6.3.1: Schulung des Personals zu Phishing und Social Engineering

**Protokollierung und Überwachung**:

- 10.4.1.1: Automatisierte Alarmierung bei Anomalien/Verdachtsaktivitäten
- 10.7.1–10.7.3: Erkennung und Reaktion auf Ausfälle kritischer Sicherheitskontrollen (Dienstleister)

**Geltungsbereich und Risikomanagement**:

- 12.3.4: Bestätigung des PCI-DSS-Compliance-Programmbetriebs (vierteljährlich)
- 12.5.2.1: Auswirkungen von Änderungen auf PCI-DSS-Geltungsbereich

**Dienstleister-Anforderungen**:

- 11.4.7: Multi-Tenant-Dienstleister unterstützen Kunden-Penetrationstests

---

# Validierung und Compliance

## Validierungsmethoden

**Compliance-Bericht (Report on Compliance – ROC)**:

- Erforderlich für: Händler Niveau 1, Dienstleister
- Durchgeführt von: Qualified Security Assessor (QSA)
- Häufigkeit: Jährlich
- Ergebnis: Detaillierter Compliance-Bericht (300+ Seiten)

**Self-Assessment Questionnaire (SAQ)**:

- Erforderlich für: Händler Niveau 2–4 (je nach Zahlungskanal)
- Durchgeführt von: Interne Bewertung (oder optionaler QSA)
- Häufigkeit: Jährlich
- Ergebnis: Ausgefüllter SAQ + Konformitätserklärung (AOC)

**SAQ-Typen**:

| SAQ-Typ | Anwendbarkeit | Anforderungen |
|---------|---------------|---------------|
| **SAQ A** | Kartenabwesenheit, vollständig ausgelagert (keine elektronische Speicherung, Verarbeitung, Übertragung) | 22 Anforderungen |
| **SAQ A-EP** | E-Commerce, teilweise ausgelagert | 169 Anforderungen |
| **SAQ B** | Nur Prägemaschinen ODER eigenständige Wählterminals | 41 Anforderungen |
| **SAQ B-IP** | Eigenständige IP-verbundene Terminals, keine elektronische Speicherung | 79 Anforderungen |
| **SAQ C** | Zahlungsanwendungssysteme mit Internetverbindung, keine elektronische Speicherung | 158 Anforderungen |
| **SAQ C-VT** | Web-basiertes virtuelles Terminal, keine elektronische Speicherung | 80 Anforderungen |
| **SAQ P2PE** | Hardware-Zahlungsterminals mit validierter P2PE-Lösung | 32 Anforderungen |
| **SAQ D – Händler** | Alle anderen Händler, die nicht in die obigen Kategorien passen | 337 Anforderungen |
| **SAQ D – Dienstleister** | SAQ-berechtigte Dienstleister | 337 Anforderungen |

**Quartalsweise Netzwerk-Scans**:

- Erforderlich für: Alle Entitäten mit öffentlich zugänglichen CDE-Systemen
- Durchgeführt von: Approved Scanning Vendor (ASV)
- Häufigkeit: Mindestens vierteljährlich (auch nach wesentlichen Netzwerkänderungen)
- Bestehensvoraussetzungen: Keine Schwachstellen mit CVSS-Score 4.0 oder höher

## Konformitätserklärung (Attestation of Compliance – AOC)

Erforderliche Dokumentation, die dem Acquirer/der Zahlungsmarke übermittelt wird:

- Ausgefüllter ROC oder SAQ
- Konformitätserklärung (AOC) – unterzeichnetes Dokument
- ASV-Scan-Ergebnisse (4 bestandene Quartals-Scans)
- Segmentierungstests (bei Netzwerksegmentierung zur Geltungsbereichseinschränkung)

---

# Zuordnung ISO 27001:2022 → PCI DSS

## Kontrollzuordnungsmatrix

| PCI-DSS-Anforderung | ISO 27001:2022-Kontrolle | Lückenanalyse |
|---------------------|--------------------------|---------------|
| 1. Netzwerksicherheitskontrollen | A.8.20–8.23 | PCI DSS: Präskriptivere Firewall-Regeln |
| 2. Sichere Konfigurationen | A.8.9, A.8.19, A.8.1 | Ausgerichtet |
| 3. Gespeicherte CHD schützen | A.8.24, A.8.10, A.8.11 | **PCI-DSS-spezifisch**: SAD-Speicherverbot, strenge Verschlüsselungsanforderungen |
| 4. CHD bei Übertragung schützen | A.8.24, A.5.14 | PCI DSS: Schreibt TLS 1.2+ vor, verbietet Endnutzer-Messaging |
| 5. Vor Schadsoftware schützen | A.8.7, A.5.7 | PCI DSS: Fügt Anti-Phishing-Anforderungen hinzu (v4.0) |
| 6. Sichere Entwicklung | A.8.8, A.8.25–8.33 | PCI DSS: Präskriptive Patch-Zeitpläne (30 Tage kritisch) |
| 7. Zugang nach Need-to-Know einschränken | A.5.15, A.5.18, A.8.2–8.3 | Ausgerichtet |
| 8. Identifizieren und Authentifizieren | A.5.16–5.17, A.8.5 | **PCI-DSS-spezifisch**: Pflicht-MFA, 12-Zeichen-Passwörter |
| 9. Physischen Zugang einschränken | A.7.1–7.4, A.7.7–7.8, A.7.10, A.7.14 | PCI DSS: Fügt POI-Geräteschutz hinzu |
| 10. Protokollieren und Überwachen | A.8.15–8.16 | PCI DSS: Präskriptive 12-Monate-Aufbewahrung, tägliche Überprüfung |
| 11. Sicherheit testen | A.8.8, A.5.7, A.8.34 | **PCI-DSS-spezifisch**: Quartalsweise ASV-Scans, jährliche Pentests |
| 12. Sicherheitsrichtlinie und -programm | A.5.1, A.5.36, A.6.3, A.5.24–5.28, A.5.19–5.23 | PCI DSS: Fügt zielgerichtete Risikoanalyse, Rechenschaftspflicht der Führung hinzu |

## Wesentliche Lücken zwischen ISO 27001:2022 und PCI DSS

**Lücke 1: Karteninhaberdaten-spezifische Anforderungen**

- ISO 27001: Allgemeiner Datenschutz
- PCI DSS: Explizite CHD-Verarbeitung, SAD-Speicherverbot, PAN-Maskierung

**Lücke 2: Präskriptive technische Kontrollen**

- ISO 27001: Risikobasierte Kontrollauswahl
- PCI DSS: Obligatorische Kontrollen (Firewalls, Verschlüsselung, MFA, Anti-Malware)

**Lücke 3: Test- und Validierungshäufigkeit**

- ISO 27001: Keine vorgeschriebene Testhäufigkeit
- PCI DSS: Quartalsweise ASV-Scans, jährliche Pentests, jährliche Compliance-Validierung

**Lücke 4: Händler-/Dienstleister-spezifische Anforderungen**

- ISO 27001: Keine händlerspezifischen Leitlinien
- PCI DSS: Explizite Händlerniveaus, SAQ-Typen, Dienstleisterpflichten

**Lücke 5: Rechenschaftspflicht der Führung**

- ISO 27001: Managementverpflichtung
- PCI DSS: Letztendliche Verantwortung der obersten Unternehmensführung (12.1.4)

## PCI-DSS-Compliance mit ISO-27001-Fundament

**Kernaussage**:
ISO-27001:2022-Zertifizierung bietet grundlegende Sicherheitskontrollen. Allerdings erfordert PCI DSS:
1. **CDE-Geltungsbereichsbestimmung** und Dokumentation der Karteninhaberdatenflüsse
2. **Präskriptive technische Kontrollen** (MFA, Verschlüsselungsstandards, Patch-Zeitpläne)
3. **Regelmässige Validierung** (ASV-Scans, Pentests, jährliche Compliance-Bestätigung)
4. **Spezifische Protokollierungs-/Überwachungsanforderungen** (12 Monate Aufbewahrung, tägliche Überprüfung)
5. **Händlerspezifische Anforderungen** basierend auf Transaktionsvolumen

Organisationen mit ISO 27001 benötigen in der Regel **30–50 % zusätzlichen Aufwand** zur Erreichung der PCI-DSS-Compliance, hauptsächlich in CDE-Geltungsbereichsbestimmung, präskriptiven Kontrollen und Validierungsprozessen.

---

# Implementierungserwägungen

## PCI-DSS-Compliance-Fahrplan

**Wenn [Organisation] Zahlungskarten verarbeitet**:

**Phase 1: Geltungsbereich (Monate 1–2)**

- Karteninhaberdatenflüsse dokumentieren
- Karteninhaberdaten-Umgebung (CDE) definieren
- Geltungsbereich-Systeme und verbundene Systeme identifizieren
- Netzwerksegmentierung falls zutreffend
- Händlerniveau und Validierungsanforderungen bestimmen

**Phase 2: Lückenbewertung (Monate 2–3)**

- Aktuelle Kontrollen gegen PCI-DSS-Anforderungen bewerten
- Lücken und Behebungsprioritäten identifizieren
- Ausgleichskontrollen dokumentieren, falls erforderlich
- Behebungszeitplan und Budget schätzen

**Phase 3: Behebung (Monate 3–9)**

- **Kritische Lücken zuerst**: Anf. 3 (gespeicherte CHD schützen), Anf. 4 (CHD-Übertragung schützen), Anf. 8 (MFA)
- **Hohe Priorität**: Anf. 1–2 (Netzwerksicherheit, Konfigurationen), Anf. 6 (Patching), Anf. 10 (Protokollierung)
- **Mittlere Priorität**: Anf. 5 (Anti-Malware), Anf. 7 (Zugangskontrolle), Anf. 9 (physische Sicherheit)
- **Administrativ**: Anf. 11 (Tests), Anf. 12 (Richtlinien und Verfahren)

**Phase 4: Validierungsvorbereitung (Monate 9–11)**

- Interne Bereitschaftsbewertung
- ASV-Quartals-Scans (4 bestandene Scans erforderlich)
- Interne Penetrationstests
- Dokumentationszusammenstellung
- QSA-Beauftragung (falls ROC erforderlich)

**Phase 5: Compliance-Validierung (Monat 12)**

- QSA-Audit (Niveau 1) oder SAQ-Ausfüllung
- Abschliessender ASV-Scan
- Konformitätserklärung (AOC) abschliessen
- Einreichung bei Acquirer/Zahlungsmarken

**Laufend (nach Compliance)**:

- Quartalsweise ASV-Scans
- Jährliche Compliance-Revalidierung
- Kontinuierliche Überwachung und Protokollüberprüfung
- Änderungsmanagement mit PCI-Auswirkungsbewertung
- Jährliche Penetrationstests und Schwachstellenmanagement

## Ressourcenanforderungen

**Personal**:

- PCI-Compliance-Manager/-Koordinator
- QSA (extern, für Händler Niveau 1)
- ASV (extern, für Quartals-Scans)
- Internes Sicherheitsteam (Firewall, Verschlüsselung, Protokollierung, Patching)
- Anwendungsentwicklungsteam (sicheres Coding, Zahlungsseiten-Schutz)
- Physisches Sicherheitsteam (falls zutreffend)

**Technologie**:

- Netzwerksicherheitskontrollen (Firewalls, IDS/IPS)
- Verschlüsselungslösungen (TLS für Übertragung, Festplatten-/Datenbankver-schlüsselung)
- Multi-Faktor-Authentifizierungsplattform
- SIEM oder zentralisierte Protokollierung
- Werkzeuge zur Schwachstellenprüfung
- Anti-Malware-Lösungen
- Dateiintegritäts-Überwachung (FIM)
- Zeitsynchronisierung (NTP)
- Zahlungs-Tokenisierung oder P2PE (optional, zur Geltungsbereichsreduzierung)

**Externe Dienstleistungen**:

- QSA für Jahresaudit (Niveau 1)
- ASV für Quartals-Schwachstellenscans
- Penetrationstest-Dienstleistungen (jährlich)
- Sicherer Entsorgungs-/Vernichtungsanbieter (Medien)
- Forensische Untersuchungs-Rückstellungen (Incident Response)

## Kostenimplikationen

PCI-DSS-Compliance-Kosten variieren erheblich je nach Händlerniveau und Umgebungskomplexität:

**Händler Niveau 1 (> 6 Mio. Transaktionen/Jahr)**:

- QSA-Audit: 30.000–100.000 $ (jährlich)
- ASV-Scans: 3.000–10.000 $ (jährlich)
- Penetrationstests: 15.000–50.000 $ (jährlich)
- Technologieinvestitionen: 100.000–500.000 $ (initial)
- Personal: 1–3 Vollzeitstellen für PCI-Compliance
- **Jährliche Gesamtkosten**: 200.000–1.000.000+ $

**Händler Niveau 2–4 (< 6 Mio. Transaktionen/Jahr)**:

- SAQ + AOC: 0–20.000 $ (bei QSA-Unterstützung)
- ASV-Scans: 2.000–5.000 $ (jährlich)
- Penetrationstests: 10.000–30.000 $ (jährlich)
- Technologieinvestitionen: 50.000–200.000 $ (initial)
- Personal: 0,5–1 Vollzeitstelle für PCI-Compliance
- **Jährliche Gesamtkosten**: 50.000–250.000 $

**Bußgelder bei Nichtkonformität**:

- Zahlungsmarken-Bußgelder: 5.000–100.000 $ pro Monat (eskalierend)
- Acquirer-Bußgelder und -Gebühren
- Möglicher Verlust der Kartenakzeptanz
- Pannenkosten: 200+ $ pro kompromittiertem Datensatz
- Reputationsschaden

---

# Häufige Fallstricke und gewonnene Erkenntnisse

## Häufige PCI-DSS-Compliance-Herausforderungen

**Herausforderung 1: Geltungsbereichs-Creep**

- CDE nicht ordnungsgemäss vom restlichen Netzwerk segmentiert
- „Flache" Netzwerke führen zur gesamten Umgebung im Geltungsbereich
- Fehlende Netzwerkdiagramme und Datenfluss-Dokumentation

**Herausforderung 2: Speicherung sensibler Authentifizierungsdaten (SAD)**

- Versehentliche Speicherung von CVV/CVV2, vollständigen Track-Daten, PIN
- Auch verschlüsselte SAD-Speicherung ist nach der Autorisierung verboten
- Legacy-Anwendungen können versteckte SAD-Speicherung aufweisen

**Herausforderung 3: Multi-Faktor-Authentifizierungs-Implementierung**

- Unterschätzung der MFA-Deployment-Komplexität (v4.0-Erweiterung)
- Legacy-Systeme unterstützen MFA nicht
- Ausnahmen für „Dienstkonten" nicht ordnungsgemäss verwaltet

**Herausforderung 4: Protokollierungs- und Überwachungslücken**

- Protokolle nicht 12 Monate aufbewahrt
- Tägliche Protokollüberprüfung nicht konsequent durchgeführt
- SIEM nicht ordnungsgemäss für CDE konfiguriert
- Zeitsynchronisierungsprobleme (Uhren nicht synchron)

**Herausforderung 5: Quartalsweise ASV-Scan-Fehler**

- Ungepatchte Schwachstellen bei Scans entdeckt
- Verwaltung von False-Positives
- Scan-Zeitfenster nicht mit Compliance-Einreichungsfristen abgestimmt

**Herausforderung 6: Änderungsmanagement**

- CDE-Änderungen nicht auf PCI-Auswirkungen geprüft
- Netzwerksegmentierung durch Änderungen unterbrochen
- Firewall-Regeln ohne Dokumentation/Begründung hinzugefügt

**Herausforderung 7: Lieferantenmanagement**

- Drittanbieter-Dienstleister nicht auf PCI-Compliance validiert
- Zahlungsanwendungen nicht durch PA-DSS oder PCI SSC validiert
- Hosting-Anbieter nicht PCI-DSS-konform

## Best Practices

**Praxis 1**: Geltungsbereich durch Tokenisierung, P2PE oder Outsourcing reduzieren
**Praxis 2**: Starke Netzwerksegmentierung einsetzen (CDE-Geltungsbereich reduzieren)
**Praxis 3**: QSA für Vorab-Lückenbewertung nutzen (vor formalem Audit)
**Praxis 4**: Compliance-Überwachung automatisieren (kontinuierliche Compliance)
**Praxis 5**: PCI DSS in SDLC für Zahlungsanwendungen integrieren
**Praxis 6**: Vierteljährliche interne PCI-Bereitschaftsüberprüfungen durchführen
**Praxis 7**: Gesamtes Personal zu PCI-DSS-Grundlagen schulen (nicht nur IT)
**Praxis 8**: Dokumentation von Ausgleichskontrollen verwenden, wenn technische Kontrollen nicht realisierbar
**Praxis 9**: Umfassende Dokumentation pflegen (Diagramme, Richtlinien, Nachweise)
**Praxis 10**: ASV-Scans frühzeitig planen (Zeit für Behebung vor Fristen einplanen)

---

# Referenzen und Ressourcen

## Offizielle PCI-DSS-Ressourcen

**PCI Security Standards Council (PCI SSC)**:

- Website: https://www.pcisecuritystandards.org/
- PCI DSS v4.0.1: https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf
- PCI DSS Quick Reference Guide
- Self-Assessment Questionnaires (SAQs)
- Priorisierter Ansatz für PCI DSS v4.0

**Zahlungsmarken-Ressourcen**:

- **Visa**: https://usa.visa.com/support/small-business/security-compliance.html
- **Mastercard**: https://www.mastercard.us/en-us/business/overview/safety-and-security/security-recommendations.html
- **American Express**: https://www.americanexpress.com/us/merchant/data-security-operating-policy.html
- **Discover**: https://www.discoverglobalnetwork.com/en-us/resources/compliance

## Qualifizierte Dienstleister

**QSA finden (Qualified Security Assessor)**:

- PCI SSC QSA-Verzeichnis: https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors

**ASV finden (Approved Scanning Vendor)**:

- PCI SSC ASV-Verzeichnis: https://www.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors

**Validierte Zahlungsanwendungen**:

- PCI SSC Validierte Anwendungen: https://www.pcisecuritystandards.org/assessors_and_solutions/payment_applications

## Verwandte Standards und Rahmenwerke

**ISO-Standards**:

- ISO/IEC 27001:2022: Informationssicherheitsmanagement
- ISO/IEC 27002:2022: Informationssicherheitskontrollen

**NIST-Publikationen** (informationsreferenz):

- NIST SP 800-53: Sicherheits- und Datenschutzkontrollen
- NIST Cybersecurity Framework

**Branchenleitfäden**:

- OWASP Application Security: https://owasp.org/
- CIS Controls: https://www.cisecurity.org/controls

## Schulung und Zertifizierung

**PCI SSC Schulungen**:

- PCI Professional (PCIP): Einstiegszertifizierung
- Internal Security Assessor (ISA): Interne Audit-Zertifizierung
- Qualified Security Assessor (QSA): Externe Auditoren-Zertifizierung

**Online-Ressourcen**:

- PCI Guru: https://pciguru.wordpress.com/ (inoffizieller Blog)
- PCI Compliance Guide: https://www.pcicomplianceguide.org/

---

# Anhang A: PCI-DSS-Compliance-Selbstbewertungscheckliste

Diese Checkliste bietet High-Level-Abdeckung. Organisationen sollten offizielle SAQs für eine vollständige Bewertung verwenden.

## Sicheres Netzwerk aufbauen und pflegen (Anf. 1–2)

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Firewall-Regeln dokumentiert und begründet | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Firewall-Regeln alle 6 Monate überprüft | ⬜ Ja ⬜ Nein | | |
| Netzwerksegmentierung zwischen CDE und anderen Netzwerken | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Herstellerstandard-Passwörter geändert | ⬜ Ja ⬜ Nein | | |
| Unnötige Dienste deaktiviert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Drahtlose Netzwerke gesichert (WPA2/WPA3) | ⬜ Ja ⬜ Nein ⬜ N/A | | |

## Karteninhaberdaten schützen (Anf. 3–4)

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| CHD-Speicherung minimiert (nur wenn erforderlich) | ⬜ Ja ⬜ Nein | | |
| Sensible Authentifizierungsdaten (SAD) NICHT nach Autorisierung gespeichert | ⬜ Ja ⬜ Nein | | |
| PAN bei Anzeige maskiert (maximal erste 6, letzte 4) | ⬜ Ja ⬜ Nein | | |
| PAN bei Speicherung verschlüsselt oder tokenisiert | ⬜ Ja ⬜ Nein | | |
| Verschlüsselungsschlüssel gesichert und verwaltet | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| TLS 1.2+ für CHD-Übertragung über offene Netzwerke | ⬜ Ja ⬜ Nein | | |
| PAN nicht per Endnutzer-Messaging (E-Mail, Chat, SMS) gesendet | ⬜ Ja ⬜ Nein | | |

## Schwachstellenmanagement pflegen (Anf. 5–6)

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Anti-Malware auf allen Systemen eingesetzt (häufig betroffen) | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Anti-Malware aktuell, aktiv und protokolliert | ⬜ Ja ⬜ Nein | | |
| Anti-Phishing-Mechanismen eingesetzt | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Sicherheits-Patches innerhalb von 30 Tagen angewendet (kritische Schwachstellen) | ⬜ Ja ⬜ Nein | | |
| Schwachstellenmanagementprozess vorhanden | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Sichere Codierungspraktiken für massgeschneiderte Software | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Öffentlich zugängliche Webanwendungen geschützt (WAF oder gleichwertig) | ⬜ Ja ⬜ Nein ⬜ N/A | | |

## Starke Zugangskontrollmassnahmen umsetzen (Anf. 7–9)

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Zugang basierend auf Need-to-know gewährt | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Zugriffsrechte mindestens alle 6 Monate überprüft | ⬜ Ja ⬜ Nein | | |
| Eindeutige Benutzer-IDs jeder Person zugewiesen | ⬜ Ja ⬜ Nein | | |
| Gemeinsame Konten verboten (ausser genehmigt) | ⬜ Ja ⬜ Nein | | |
| Multi-Faktor-Authentifizierung (MFA) für alle CDE-Zugänge | ⬜ Ja ⬜ Nein | | |
| MFA für Fernzugang zum Netzwerk der Entität | ⬜ Ja ⬜ Nein | | |
| Passwörter mindestens 12 Zeichen | ⬜ Ja ⬜ Nein | | |
| Kontosperrung nach 10 fehlgeschlagenen Anmeldeversuchen | ⬜ Ja ⬜ Nein | | |
| Physische Zugangskontrollen für CDE-Systeme | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Besucherzugang kontrolliert und protokolliert | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Medien mit CHD bei Nichtmehrbedarf sicher vernichtet | ⬜ Ja ⬜ Nein | | |

## Netzwerke überwachen und testen (Anf. 10–11)

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Audit-Protokolle für alle Systemkomponenten aktiviert | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Audit-Protokolle mindestens täglich überprüft | ⬜ Ja ⬜ Nein | | |
| Audit-Protokolle mindestens 12 Monate aufbewahrt | ⬜ Ja ⬜ Nein | | |
| Zeitsynchronisierung umgesetzt (NTP) | ⬜ Ja ⬜ Nein | | |
| Drahtlose Zugangspunkte erkannt (autorisiert/nicht autorisiert) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Interne Schwachstellenscans alle 3 Monate | ⬜ Ja ⬜ Nein | | |
| Externe Schwachstellenscans (ASV) alle 3 Monate – 4 bestandene Scans | ⬜ Ja ⬜ Nein | | |
| Interne Penetrationstests mindestens jährlich | ⬜ Ja ⬜ Nein | | |
| Externe Penetrationstests mindestens jährlich | ⬜ Ja ⬜ Nein | | |
| Änderungserkennungsmechanismen eingesetzt (FIM) | ⬜ Ja ⬜ Nein | | |

## Informationssicherheitsrichtlinie (Anf. 12)

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Informationssicherheitsrichtlinie eingerichtet und veröffentlicht | ⬜ Ja ⬜ Nein | | |
| Sicherheitsrichtlinie mindestens jährlich überprüft | ⬜ Ja ⬜ Nein | | |
| Acceptable-Use-Richtlinie für Endnutzertechnologien | ⬜ Ja ⬜ Nein | | |
| Zielgerichtete Risikoanalyse mindestens jährlich | ⬜ Ja ⬜ Nein | | |
| PCI-DSS-Geltungsbereich dokumentiert und jährlich validiert | ⬜ Ja ⬜ Nein | | |
| Sicherheitsbewusstseinschulung von gesamtem Personal absolviert (jährlich) | ⬜ Ja ⬜ Nein | | |
| Phishing- und Social-Engineering-Schulung bereitgestellt | ⬜ Ja ⬜ Nein | | |
| Hintergrundprüfungen für Personal vor der Einstellung | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |
| Drittanbieter-Dienstleister auf PCI-Compliance validiert | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Incident-Response-Plan erstellt und jährlich getestet | ⬜ Ja ⬜ Nein | | |

---

# Anhang B: Vorlage für Karteninhaberdatenfluss-Diagramm

Organisationen sollten ein detailliertes Datenfluss-Diagramm erstellen, das zeigt, wie CHD in die Umgebung eintritt, durch sie fliesst und sie verlässt.

**Vorlagenelemente**:

```
[Kunde]
    ↓
[Zahlungskanal: POS / Web / Mobil / Telefon]
    ↓
[Eingangspunkt: Zahlungsterminal / Webformular / Zahlungs-Gateway]
    ↓
[Verarbeitung: Zahlungsanwendung / Server]
    ↓
[Speicherung: Datenbank / Dateisystem] ← (falls gespeichert)
    ↓
[Übertragung: Verarbeiter / Acquirer / Zahlungsmarke]
    ↓
[Ausgang: Autorisierungsantwort / Abrechnung]
```

**Erforderliche Dokumentation**:

- Alle Systeme, die CHD speichern, verarbeiten oder übertragen
- Netzwerkzonen und Segmentierung
- Datenverschlüsselungspunkte (bei Übertragung und im Ruhezustand)
- Datenspeicherungsrichtlinien und Löschverfahren
- Drittanbieter-Verbindungen zur CDE

---

**ENDE DER TECHNISCHEN REFERENZ**

---

*Diese technische Referenz unterstützt potenzielle PCI-DSS-Compliance-Anforderungen, wie in ISMS-POL-00 festgestellt. Alle regulatorischen Anwendbarkeitsbestimmungen und verbindlichen Anforderungen sind in ISMS-POL-00 und genehmigten ISMS-Richtliniendokumenten definiert.*

*Für Organisationen, die KEINE Zahlungskarten verarbeiten, dient dieses Dokument ausschließlich zur informativen Sensibilisierung und begründet KEINE Compliance-Verpflichtungen.*

<!-- ISMS-CORE:REF:ISMS-REF-PCI-DSS-DE:framework:REF:pci-dss -->

<!-- QA_VERIFIED: 2026-03-28 -->

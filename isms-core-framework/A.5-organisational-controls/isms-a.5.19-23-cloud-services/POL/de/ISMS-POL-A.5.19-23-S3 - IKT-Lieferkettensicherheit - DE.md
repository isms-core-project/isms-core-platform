<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S3-DE:framework:POL:a.5.19-23-s3 -->
**ISMS-POL-A.5.19-23-S3 — IKT-Lieferkettensicherheit**
**Massnahme A.5.21: Management der Informationssicherheit in der IKT-Lieferkette**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | IKT-Lieferkettensicherheit |
| **Dokumenttyp** | Richtlinienabschnitt |
| **Dokument-ID** | ISMS-POL-A.5.19-23-S3 |
| **Dokumentersteller** | Information Security Officer (ISO) |
| **Dokumenteigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISO | Erstfassung für ISO 27001:2022 Massnahme A.5.21 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Information Security Officer (ISO)
- Compliance: Legal/Compliance Officer
- Technik: IT-Leiter (ITL)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit)
- ISMS-POL-A.5.19-23 (Übergeordnete Richtlinie – Lieferanten- und Cloud-Dienste-Sicherheit)
- ISMS-POL-A.5.19-23-S1 (Grundlagen der Lieferantenbeziehungen)
- ISMS-POL-A.5.19-23-S2 (Anforderungen an Lieferantenvereinbarungen)
- ISO/IEC 27001:2022 Massnahme A.5.21
- ISO/IEC 27036-3 (IKT-Lieferkettensicherheit)
- NIST SP 800-161 (Cybersecurity Supply Chain Risk Management)

---

# Zweck

Dieser Abschnitt definiert Anforderungen für das Management von Informationssicherheitsrisiken innerhalb der IKT-Lieferkette, einschliesslich Sub-Lieferanten, Komponentenanbietern und Software-Abhängigkeiten. Er adressiert das „Lieferant-des-Lieferanten"-Problem und Angriffsvektoren in der Lieferkette.

**Kritischer Grundsatz – „Vertrauen kaskadiert durch die Kette"**: Die Sicherheitslage Ihrer Lieferanten hängt von deren Lieferanten ab, die wiederum von deren Lieferanten abhängen. Die SolarWinds-, Log4Shell- und MOVEit-Vorfälle zeigen, dass Lieferkettenkompromittierungen als Kraftmultiplikator wirken – eine Backdoor in einer weit verbreiteten Komponente gewährt Angreifern Zugang zu Tausenden von nachgelagerten Organisationen. Diese Richtlinie erfordert systematische Transparenz, Weitergabe von Sicherheitsanforderungen und kontinuierliche Überwachung in mehrstufigen IKT-Lieferketten.

**ISO/IEC 27001:2022 Massnahme A.5.21 – Management der Informationssicherheit in der IKT-Lieferkette**

> *Prozesse und Verfahren sollten definiert und mit Lieferanten vereinbart werden, um Informationssicherheitsrisiken im Zusammenhang mit der Lieferkette von IKT-Diensten und -Produkten zu managen.*

**Massnahmenziel**: Informationssicherheitsrisiken innerhalb der IKT-Lieferkette einschliesslich Sub-Lieferanten, Komponenten und Software-Abhängigkeiten managen.

**Zusammenfassung der ISO/IEC 27002:2022-Leitlinien**:

- IKT-Lieferkettenrisiken sollen systematisch identifiziert und bewertet werden
- Sicherheitsanforderungen für IKT-Produkte und -Dienste sollen in Beschaffungsprozessen festgelegt werden
- Sub-Lieferanten (Lieferkettentransparenz) sollen bewertet und offengelegt werden
- Software-Lieferkettensicherheit soll adressiert werden, einschliesslich Abhängigkeiten, Bibliotheken und Open-Source-Komponenten
- Hardware-Lieferkettensicherheit soll berücksichtigt werden, einschliesslich Fälschungserkennung und Manipulationsschutz
- Lieferkettenkontinuität und -resilienz sollen für kritische IKT-Dienste geplant werden
- Lieferantenänderungen und -updates sollen durch formale Änderungskontrollprozesse gemanagt werden
- Lieferkettenrisikobewertung soll geopolitische, Konzentrations- und Einzelquellen-Abhängigkeiten umfassen

---

# Geltungsbereich

## Elemente der Lieferkette

| Element | Beschreibung | Beispiele |
|---------|-------------|----------|
| **Sub-Lieferanten** | Von Primärlieferanten beauftragte Lieferanten | Subunternehmer, Sub-Auftragsverarbeiter, Dienstleister für Lieferanten |
| **Fourth Parties** | Lieferanten von Sub-Lieferanten | Infrastrukturanbieter für SaaS-Anbieter, Rechenzentren für Cloud-Anbieter |
| **Software-Komponenten** | Code-Abhängigkeiten und Bibliotheken | Open-Source-Pakete, SDKs, APIs, Frameworks |
| **Hardware-Komponenten** | Physische Komponenten in IKT-Produkten | Prozessoren, Speichermodule, Netzwerk-Chips, Firmware |
| **Dienstabhängigkeiten** | Von Primärdiensten benötigte Dienste | DNS-Anbieter, CDN-Netzwerke, Zahlungs-Gateways, Identity-Provider |
| **Entwicklungswerkzeuge** | Zur Erstellung/Bereitstellung von Produkten verwendete Tools | CI/CD-Plattformen, Code-Repositories, Build-Systeme |

## Lieferkettenrisikokategorien

| Risikokategorie | Beschreibung | Auswirkung |
|-----------------|-------------|-----------|
| **Kompromittierungsrisiko** | In die Lieferkette eingebrachter Schadcode oder Backdoors | Datenpanne, Systemkompromittierung, Spionage |
| **Verfügbarkeitsrisiko** | Lieferkettenunterbrechung oder Single Point of Failure | Dienstausfall, Geschäftsunterbrechung, Lieferverzögerungen |
| **Integritätsrisiko** | Unbefugte Änderungen an Komponenten oder Diensten | Datenverfälschung, Systeminstabilität, Compliance-Verstösse |
| **Compliance-Risiko** | Regulatorische Verstösse via Lieferkette (DSGVO, DORA, NIS2) | Bussen, Sanktionen, Rechtshaftung, Reputationsschaden |
| **Konzentrationsrisiko** | Überabhängigkeit von einzelnem Lieferanten/Komponente/Jurisdiktion | Weitreichende Auswirkung bei Einzelausfall, Vendor Lock-in |
| **Geopolitisches Risiko** | Lieferkette exponiert gegenüber feindlichen Jurisdiktionen oder Sanktionen | Datenzugang durch ausländische Regierungen, Dienstunterbrechung |

---

# Sub-Lieferantenmanagement

## Anforderungen an die Sub-Lieferantentransparenz

| Lieferantenstufe | Transparenzanforderung |
|-----------------|------------------------|
| Stufe 1 (Kritisch) | Vollständiges Sub-Lieferantenregister für alle datenverarbeitenden und kritischen Serviceaktivitäten |
| Stufe 2 (Hoch) | Sub-Lieferantenregister für wesentliche Dienste oder Datenzugang |
| Stufe 3 (Mittel) | Kenntnis wichtiger Sub-Lieferanten auf Anfrage |
| Stufe 4 (Niedrig) | Nicht erforderlich |

**Regulatorische Erweiterung**:

- **DORA-Einheiten**: Vollständiges Sub-Auslagerungs-Register gemäss Artikel 30 erforderlich, einschliesslich Fourth-Party-Transparenz
- **NIS2-Einheiten**: Sub-Lieferantenoffenlegung für kritische Dienste gemäss Artikel 21 Lieferkettensicherheitsanforderungen

## Sub-Lieferantenregister

Für Lieferanten der Stufe 1 und 2 soll umfassende Transparenz sichergestellt werden, einschliesslich:

| Feld | Beschreibung | Aktualisierungsauslöser |
|------|-------------|------------------------|
| Sub-Lieferantenname | Juristischer Unternehmensname und Kennung | Neue Beauftragung |
| Sub-Lieferantentyp | Kategorie (Infrastruktur, Entwicklung, Support, Verarbeitung) | Dienstleistungsänderung |
| Erbrachte Dienste | Spezifische Dienste des Sub-Lieferanten an den Primärlieferanten | Umfangsänderung |
| Datenzugang | Ob Sub-Lieferant auf Daten der [Organisation] zugreift, Klassifizierungsstufe | Zugriffsänderung |
| Verarbeitungsort | Geografische Standorte der Datenverarbeitung oder Diensterbringung | Standortänderung |
| Zertifizierungsstatus | Gehaltene Sicherheitszertifizierungen (ISO 27001, SOC 2) | Zertifikat-Ablauf/-Erneuerung |
| Kritikalität | Auswirkung bei Ausfall des Sub-Lieferanten (Kritisch/Hoch/Mittel/Niedrig) | Jährliche Überprüfung |
| Genehmigungsstatus | Genehmigung der [Organisation] (Genehmigt/Ausstehend/Abgelehnt) | Prüfungsentscheidung |
| Vertragsbedingungen | Wesentliche Sicherheitsverpflichtungen des Sub-Lieferanten | Vertragsänderung |

**Registerpflege**:

- Aktualisierung innerhalb von 10 Werktagen nach Sub-Lieferantenänderungen
- Vierteljährliche Prüfung auf Genauigkeit und Vollständigkeit
- Jährliche Abstimmung mit vom Lieferanten bereitgestellter Dokumentation

## Kontrollpflichten gegenüber Sub-Lieferanten

**Primärlieferanten sollen:**

| Anforderung | Stufe 1 | Stufe 2 | Stufe 3–4 |
|-------------|---------|---------|----------|
| [Organisation] über Sub-Lieferantenänderungen informieren | ✓ 30 Tage vorab | ✓ Vor Beauftragung | — |
| Schriftliche Genehmigung für neue Sub-Lieferanten einholen | ✓ Erforderlich | ✓ Benachrichtigung ausreichend | — |
| Sicherheitsanforderungen an Sub-Lieferanten weitergeben | ✓ Wortgetreu | ✓ Gleichwertig | — |
| Vollständig für Handlungen von Sub-Lieferanten haften | ✓ Erforderlich | ✓ Erforderlich | ✓ Erforderlich |
| Auf Anfrage Sub-Lieferanten-Auditberichte bereitstellen | ✓ Innerhalb von 30 Tagen | ✓ Nach bestem Bemühen | — |
| Einspruch der [Organisation] gegen bestimmte Sub-Lieferanten ermöglichen | ✓ 14 Tage Einspruchsfrist | ✓ Angemessener Einspruch | — |
| Sub-Lieferantenregister führen | ✓ Aktuell, umfassend | ✓ Wichtige Sub-Lieferanten | — |
| Due Diligence bei Sub-Lieferanten durchführen | ✓ Gleichwertig wie [Organisation] | ✓ Risikobasiert | — |

## Sub-Lieferanten-Änderungsprozess

```
┌─────────────────────────────────────────────────────────────┐
│ BENACHRICHTIGUNGSPROZESS BEI SUB-LIEFERANTENÄNDERUNGEN      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Lieferant informiert [Organisation] über geplante       │
│     Änderung                                                │
│     • Name und Details des Sub-Lieferanten                  │
│     • Zu erbringende Dienste                                │
│     • Datenzugangsanforderungen                             │
│     • Geografische Standorte                                │
│     • Sicherheitszertifizierungen                           │
│                         ↓                                   │
│  2. Sicherheitsabteilung der [Organisation] prüft           │
│     Sub-Lieferanten                                         │
│     • Zertifizierungen (ISO 27001, SOC 2)                   │
│     • Datenzugangsumfang und Klassifizierung                │
│     • Geografischer Standort und Jurisdiktion               │
│     • Auswirkung auf Konzentrationsrisiko                   │
│     • Regulatorische Implikationen (DORA, NIS2, DSGVO)     │
│                         ↓                                   │
│  3. [Organisation] antwortet (innerhalb von 14 Tagen)       │
│     • GENEHMIGT: Beauftragung fortführen                    │
│     • WEITERE INFORMATIONEN ANFORDERN                       │
│     • EINSPRUCH: Begründeter Sicherheits-/Compliance-Grund  │
│                         ↓                                   │
│  4. Bei Einspruch: Lieferant schlägt Alternative oder       │
│     Mitigierungskontrollen vor                              │
│                         ↓                                   │
│  5. Sub-Lieferantenregister und Vertragsänderungen          │
│     aktualisieren                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Einspruchsgründe**:

- Sub-Lieferant in Hochrisikoland ansässig
- Sub-Lieferant besitzt nicht die erforderlichen Zertifizierungen
- Sub-Lieferant hat eine Geschichte von Sicherheitsvorfällen
- Konzentrationsrisiko (gleicher Sub-Lieferant bei mehreren Primärlieferanten)
- Regulatorische Inkompatibilität (DORA, NIS2, DSGVO)

---

# Fourth-Party-Risikomanagement

## Fourth-Party-Transparenz

Fourth Parties sind Lieferanten der Lieferanten Ihrer Lieferanten (z.B. der Infrastrukturanbieter, der die Cloud-Plattform Ihres SaaS-Anbieters betreibt).

| Ansatz | Beschreibung | Anwendbarkeit |
|--------|-------------|--------------|
| **Direkte Transparenz** | Fourth-Party-Informationen mit Dokumentation vom Lieferanten anfordern | Stufe-1-Lieferanten für kritische Dienste |
| **Zertifizierungsverlass** | ISO 27001/SOC 2-Zertifizierung des Lieferanten deckt Fourth-Party-Management ab | Stufe-2-Lieferanten, ergänzt direkte Transparenz für Stufe 1 |
| **Vertragliche Weitergabe** | Lieferanten verpflichten, Sicherheitsanforderungen an alle Fourth Parties weiterzugeben | Alle Lieferanten mit Datenzugang |

## Kritische Fourth-Party-Abhängigkeiten

Identifizierung und Dokumentierung von Fourth-Party-Abhängigkeiten für:

**Infrastrukturdienste**:

- Rechenplattformen (AWS, Azure, GCP als Grundlage für SaaS-Anbieter)
- Speicheranbieter (Objektspeicher, Blockspeicher, Backup)
- Netzwerkanbieter (Internetkonnektivität, Private Links, CDN)

**Sicherheitsdienste**:

- Identity-Provider (SSO, MFA, Verzeichnisdienste)
- Verschlüsselungsdienste (Schlüsselmanagement, HSM, Zertifizierungsstellen)
- Überwachungsdienste (SIEM, Log-Aggregation, Bedrohungsinformationen)

**Betriebsdienste**:

- DNS-Anbieter (kritisch für Verfügbarkeit)
- CDN-Netzwerke (Content Delivery, DDoS-Schutz)
- Zahlungsabwickler (Finanztransaktionsabwicklung)

## Fourth-Party-Risikoindikatoren

| Indikator | Risikosignal | Mitigierung |
|-----------|-------------|------------|
| Lieferant nutzt einzelnen Fourth Party für kritische Funktion | Konzentrationsrisiko | Redundanz oder Notfallplan vom Lieferanten fordern |
| Fourth Party in Hochrisikoland (US CLOUD Act, Sanktionen) | Geopolitisches Risiko | Datenresidenz, Verschlüsselung, vertraglichen Schutz bewerten |
| Fourth Party hat Geschichte von Vorfällen oder Ausfällen | Zuverlässigkeitsrisiko | Vorfallshistorie anfordern, BC/DR-Nachweise |
| Keine vertraglichen Kontrollen gegenüber Fourth Party | Compliance-Risiko | Weitergabe-Anforderungen im Lieferantenvertrag sicherstellen |
| Fourth Party ohne Sicherheitszertifizierungen | Sicherheitsrisiko | Due-Diligence-Dokumentation vom Lieferanten fordern |

**Konzentrationsrisikobewertung**: Wenn mehrere Stufe-1-Lieferanten vom gleichen Fourth Party abhängen (z.B. alle SaaS-Anbieter nutzen AWS), soll bewertet werden:

- Auswirkung bei Ausfall des Fourth Party
- Verfügbare Alternativlieferanten
- Business-Continuity-Implikationen
- Mitigierungsstrategien (Multi-Cloud, Hybrid-Architektur)

## Fourth-Party-Risikoakzeptanzkriterien

Wenn Fourth-Party-Risikoindikatoren identifiziert werden, wendet die Sicherheitsabteilung der [Organisation] den folgenden strukturierten Entscheidungsprozess an:

**Schwellenwerte für Vorfallshistorie:**

| Fourth-Party-Vorfallshistorie | Entscheidung |
|-------------------------------|-------------|
| 0–1 grössere Vorfälle in den letzten 3 Jahren | Akzeptieren, wenn Zertifizierungen aktuell und BC/DR-Nachweise vorhanden |
| 2 grössere Vorfälle in den letzten 3 Jahren | Bedingte Akzeptanz — Lieferant muss geografische Redundanz oder alternativen Fourth Party innerhalb von 90 Tagen implementieren |
| 3+ grössere Vorfälle in den letzten 3 Jahren | Ablehnen, es sei denn ISB genehmigt mit dokumentierten kompensierenden Kontrollen und zeitlich begrenztem Dispens |
| Aktiver, ungelöster kritischer Vorfall zum Zeitpunkt der Prüfung | Ablehnen bis Vorfall gelöst und Ursachenanalyse akzeptiert |

> „Grösserer Vorfall" = Ausfall oder Sicherheitsereignis mit >4h Dienstauswirkung auf kritische Dienste, bestätigte Verletzung von Kundendaten oder regulatorische Sanktion gegen den Fourth Party.

**Entscheidungsfluss Akzeptanz/Ablehnung:**

```
Fourth Party in Lieferkette des Lieferanten identifiziert
              ↓
Ist Fourth Party in Hochrisikojurisdiktion?
  JA  → Datenresidenz, Verschlüsselung, vertraglichen Schutz bewerten
        → Bei unzureichendem Schutz → ABLEHNEN / Fourth-Party-Wechsel fordern
  NEIN → Weiter
              ↓
Besitzt Fourth Party erforderliche Zertifizierungen (ISO 27001, SOC 2)?
  NEIN → Lieferant muss kompensierende Nachweise bereitstellen (Drittprüfung, ISB-Bewertung)
         → Keine Nachweise → ABLEHNEN
  JA   → Weiter
              ↓
Vorfallshistorie prüfen (3-Jahres-Rückblick)
  3+ grössere Vorfälle → ISB für Dispens-Entscheidung einschalten
  2 Vorfälle → Bedingte Akzeptanz mit zeitgebundenem Mitigierungsplan
  0–1 Vorfälle → AKZEPTIEREN
              ↓
Konzentrationsrisiko prüfen
  >50 % der Stufe-1-Lieferanten hängen von gleichem Fourth Party ab?
  JA  → Konzentrationsrisiko im Risikoregister dokumentieren; Multi-Cloud-/Redundanz-Roadmap fordern
  NEIN → AKZEPTIEREN
```

**Eskalation**: Alle Fourth-Party-ABLEHNEN-Entscheidungen und ISB-Dispense sollen im Lieferantenrisikoregister mit Begründung, Risikoverantwortlichem und Dispens-Ablaufdatum (max. 12-monatige Dispensdauer) dokumentiert werden.

---

# Software-Lieferkettensicherheit

## Risiken bei Software-Komponenten

| Risiko | Beschreibung | Mitigierung |
|--------|-------------|------------|
| Anfällige Abhängigkeiten | Bekannte CVEs in Bibliotheken, Frameworks oder Open-Source-Komponenten | Kontinuierliches Schwachstellen-Scanning, Software Composition Analysis (SCA), zeitnahe Patches |
| Schadhafte Pakete | Typosquatting-Angriffe, kompromittierte legitime Pakete, Backdoors | Paketverifizierung, Prüfsummenvalidierung, nur vertrauenswürdige Repository-Quellen |
| Aufgegebene Software | Nicht gewartete Komponenten ohne Sicherheitsupdates | Lebenszyklusüberwachung, Migration zu gewarteten Alternativen, Lieferantenbenachrichtigung |
| Lizenz-Compliance | Inkompatible Lizenzen (GPL, AGPL) oder unklare Lizenzierung | Lizenz-Scanning, rechtliche Prüfung, Open-Source-Richtliniendurchsetzung |
| Build-Kompromittierung | Manipulierte Build-Pipelines, kompromittiertes CI/CD, Lieferketteninjektion | Sichere CI/CD-Härtung, Code-Signierung, reproduzierbare Builds, Artefaktverifizierung |

## Anforderungen an Software-Lieferanten

**Lieferanten der Stufe 1 und 2, die Software oder Software-as-a-Service bereitstellen, sollen:**

| Anforderung | Beschreibung |
|-------------|-------------|
| Software Bill of Materials (SBOM) | Umfassende SBOM für gesamte eingesetzte Software einschliesslich Abhängigkeiten führen |
| Schwachstellenmanagement | Regelmässiges automatisiertes Scanning und zeitnahe Patches (kritisch: 14 Tage, hoch: 30 Tage) |
| Sicherer Entwicklungslebenszyklus | Sicherem SDLC folgen (OWASP SAMM, Microsoft SDL oder gleichwertig) |
| Code-Signierung | Alle Versionen und Updates digital signieren zur Integritäts- und Authentizitätsverifizierung |
| Source-Code-Repository-Sicherheit | MFA, Branch-Schutz, Audit-Protokollierung, Secrets-Scanning in Repositories |
| Genehmigung von Drittanbieter-Bibliotheken | Formaler Prozess für die Genehmigung von Open-Source- und Drittanbieter-Komponenten |
| Update-Benachrichtigung | [Organisation] innerhalb von 24 Stunden über sicherheitsrelevante Updates informieren |
| Abhängigkeits-Update-Rhythmus | Regelmässige Aktualisierung der Abhängigkeiten (mindestens vierteljährlich für nicht-sicherheitsrelevante) |

## Software Bill of Materials (SBOM)

Für Stufe-1-Software-Lieferanten soll die SBOM enthalten:

| Feld | Beschreibung |
|------|-------------|
| Komponentenname | Paket-/Bibliothekskennung (z.B. org.apache.logging.log4j:log4j-core) |
| Version | Spezifische verwendete Version (semantische Versionierung) |
| Quelle | Repository oder Anbieter, von dem die Komponente bezogen wurde |
| Lizenz | SPDX-Lizenzkennung (MIT, Apache-2.0, GPL-3.0) |
| Direkt vs. transitiv | Ob [Organisation] die Komponente direkt nutzt oder es eine Abhängigkeit ist |
| Bekannte Schwachstellen | Aktueller CVE-Status mit CVSS-Bewertungen |
| Kritikalität | Auswirkung bei Kompromittierung der Komponente (basierend auf Berechtigungen, Datenzugang) |

**SBOM-Standards**: SBOM in Standardformat bevorzugen:

- **CycloneDX**: OWASP-Standard für Software Bill of Materials
- **SPDX**: Linux-Foundation-Standard
- Beide unterstützen JSON- und XML-Formate für automatisierte Verarbeitung

**SBOM-Aktualisierungshäufigkeit**:

- Vierteljährlich für Routineaktualisierungen
- Innerhalb von 48 Stunden nach Entdeckung einer neuen kritischen Schwachstelle in einer Komponente

**CVE-Entdeckungsverantwortung**: Lieferanten sollen autoritative Schwachstellen-Feeds abonnieren – einschliesslich NVD (nvd.nist.gov), GitHub Dependabot-Alarme, Snyk oder branchenspezifische CERT/ISAC-Feeds – um CVEs zu überwachen, die Komponenten in ihrer SBOM betreffen. Die 48-Stunden-Frist beginnt ab dem Zeitpunkt, zu dem der Lieferant durch einen Feed benachrichtigt wird, nicht ab dem Zeitpunkt, zu dem die [Organisation] das Problem anspricht. Die [Organisation] überwacht Bedrohungsinformationen auch unabhängig; wenn die [Organisation] ein kritisches CVE in der SBOM eines Lieferanten identifiziert, bevor der Lieferant es meldet, kann die [Organisation] eine beschleunigte SBOM-Aktualisierung und Patch-Zeitplan ausserhalb des geplanten Zyklus anfordern. Lieferanten, die keine aktive CVE-Überwachung aufrechterhalten, verstossen gegen diese Anforderung.

## Open-Source-Sicherheit

| Überlegung | Leitlinie |
|------------|----------|
| Quellenverifizierung | Pakete nur von offiziellen Repositories herunterladen (npmjs.org, pypi.org, Maven Central) |
| Paketintegrität | Prüfsummen/Signaturen vor Verwendung verifizieren, Lock-Files verwenden (package-lock.json, Pipfile.lock) |
| Wartungsstatus | Aufgegebene Projekte (keine Commits >12 Monate) für kritische Funktionen vermeiden |
| Community-Gesundheit | Aktive Betreuer, schnelle Reaktion auf Sicherheitsprobleme, etablierte Governance |
| Sicherheits-Track-Record | Geschichte der Schwachstellen-Offenlegung und Behebungsgeschwindigkeit |
| Lizenzkompatibilität | Lizenz erlaubt kommerzielle Nutzung und abgeleitete Werke (AGPL in Diensten vermeiden) |
| Sicherheits-Tools | Dependabot, Snyk oder gleichwertig für automatisierte Schwachstellenerkennung verwenden |

**Verbotene Praktiken**:

- Installation von Paketen von inoffiziellen Mirrors oder modifizierten Repositories
- Verwendung nicht gewarteter Pakete für Kryptographie, Authentifizierung oder Autorisierung
- Einbeziehung von Paketen mit bekannten kritischen Schwachstellen ohne Behebungsplan
- Code-Übernahme von Stack Overflow oder GitHub ohne Sicherheitsprüfung

---

# Hardware-Lieferkettensicherheit

## Hardware-Lieferkettenrisiken

| Risiko | Beschreibung | Beispiele |
|--------|-------------|---------|
| Gefälschte Komponenten | Nicht echte Teile als Ersatz für authentische Komponenten | Gefälschte Cisco-Switches, gefälschte Speicherchips, geklonte Batterien |
| Manipulierte Hardware | Böswillige Änderungen bei der Herstellung oder im Transit | Eingepflanzte Backdoors in Servern, kompromittierte Netzwerkgeräte |
| Kompromittierte Firmware | Vorinstallierte Schad-Firmware oder BIOS-Änderungen | Firmware-Rootkits, UEFI-Malware, BMC-Backdoors |
| Komponentenausfall | Minderwertige oder aufbereitete Komponenten, die zu Frühausfällen führen | Ausgefallene Festplatten, unzuverlässige Netzteile |
| End-of-Life-Hardware | Nicht mehr unterstützte Hardware ohne Sicherheits-Patches | Legacy-Server, EOL-Netzwerkgeräte mit bekannten Schwachstellen |

## Hardware-Beschaffungsanforderungen

**Für Hardware-Lieferanten der Stufe 1 und 2:**

| Anforderung | Beschreibung |
|-------------|-------------|
| Autorisierte Kanäle | Ausschliesslich über vom Hersteller autorisierte Distributoren kaufen |
| Lieferkette | Vollständige Dokumentation der Handhabung und des Transports ab Werk |
| Integritätsverifizierung | Manipulationsgeschützte Versiegelungen, Verpackungsintegrität, Seriennummer-Authentifizierung verifizieren |
| Firmware-Verifizierung | Firmware-Versionen gegen Herstellerdatenbank validieren, digitale Signaturen verifizieren |
| Komponentenauthentizität | Anti-Fälschungsmassnahmen für kritische Komponenten (Prozessoren, Speicher, Speichergeräte) |
| Werksstandards | Hardware in Werksstandard-Zustand geliefert, nicht vorkonfiguriert |
| Dokumentation | Vollständige Herstellerdokumentation, Echtheitszertifikate |

**Verifizierungsmethoden**:

- Seriennummernvalidierung beim Hersteller
- Verpackungs- und Hologramm-Inspektion
- Gewichtsvergleich (Fälschungen oft unterschiedliches Gewicht)
- Sichtprüfung auf Manipulationsnachweise
- Firmware-Hash-Verifizierung gegen bekannte gute Werte

## Hardware-Lebenszyklusbetrachtungen

| Phase | Sicherheitsbetrachtung |
|-------|------------------------|
| Beschaffung | Autorisierte Quelle, Integritätsverifizierung, Authentizitätsprüfungen |
| Empfang | Manipulationsprüfung, Dokumentationsverifizierung, Quarantänezeitraum |
| Bereitstellung | Sichere Konfiguration, Firmware-Updates auf aktuelle Versionen, Asset-Registrierung |
| Betrieb | Patch-Management, Firmware-Updates, Umgebungsüberwachung, physische Sicherheit |
| Wartung | Ausschliesslich autorisierte Serviceanbieter, Hardware-Service begleiten, Integrität nach Service verifizieren |
| End-of-Life | Sichere Ausserdienststellung, Datenvernichtung (NIST SP 800-88 Rev. 2), Vernichtungszertifikat |

---

# Serviceabhängigkeitsmanagement

## Kritische Serviceabhängigkeiten

Dienste identifizieren, von denen Lieferanten abhängen, und Auswirkungen bewerten:

| Abhängigkeitstyp | Beispiele | Risiko bei Nichtverfügbarkeit |
|-----------------|---------|-------------------------------|
| Infrastruktur | Cloud-Plattformen (AWS, Azure, GCP), Rechenzentren, Colocation-Einrichtungen | Vollständiger Dienstausfall, Datenzugang nicht möglich |
| Identität & Zugang | Authentifizierungsanbieter (Auth0, Okta), SSO, MFA-Dienste | Zugangsstörungen, Authentifizierungsfehler |
| Sicherheitsdienste | Zertifizierungsstellen, Verschlüsselungsschlüsselmanagement (KMS), Sicherheitsüberwachung | Sicherheitsdegradation, Zertifikatablauf, Compliance-Lücken |
| Kommunikation | E-Mail-Gateways, Messaging-Plattformen, Benachrichtigungsdienste | Kommunikationsausfall, Verzögerung bei Störungsmeldungen |
| Betriebsdienste | DNS-Anbieter, CDN-Netzwerke, Load Balancer, DDoS-Schutz | Leistungsdegradation, Verfügbarkeitsauswirkung, Angriffsexposition |
| Zahlungsabwicklung | Zahlungs-Gateways, Betrugserkennung, Währungskonvertierung | Transaktionsfehler, Umsatzauswirkung |

## Abhängigkeitsdokumentation

Für Stufe-1-Lieferanten sollen alle kritischen Serviceabhängigkeiten dokumentiert werden:

| Feld | Beschreibung |
|------|-------------|
| Serviceabhängigkeit | Spezifischer Dienst, von dem der Lieferant abhängt (z.B. AWS RDS, Cloudflare CDN) |
| Anbieter | Name des Fourth-Party-Dienstleisters |
| Kritikalität | Auswirkung bei Ausfall der Abhängigkeit (Kritisch/Hoch/Mittel/Niedrig) |
| Alternativen | Backup- oder Failover-Optionen (Multi-Cloud, redundante Anbieter) |
| SLA | Service Level Commitment des Abhängigkeitsanbieters |
| Geografischer Umfang | Von Abhängigkeitsausfall betroffene Regionen |
| Datenresidenz | Wo Abhängigkeit Daten verarbeitet oder speichert |
| Konzentrationsrisiko | Ob mehrere Lieferanten dieselbe Abhängigkeit teilen |

**Konzentrationsrisikobeispiel**:
Wenn alle Ihre SaaS-Anbieter AWS us-east-1 verwenden, betrifft ein regionaler AWS-Ausfall alle Dienste gleichzeitig. Mitigierung: Multi-Region oder Multi-Cloud für Stufe-1-Lieferanten fordern.

---

# Mitigierung von Lieferkettenangriffen

## Gängige Angriffsvektoren

| Vektor | Beschreibung | Reales Beispiel | Mitigierung |
|--------|-------------|----------------|------------|
| Kompromittierte Updates | Schadhafte Software-Updates über legitime Kanäle verbreitet | SolarWinds Orion, ASUS Live Update | Code-Signierungsverifizierung, gestaffelte Rollouts, Update-Tests |
| Abhängigkeitsverwechslung | Schadhafte Pakete mit gleichem Namen in öffentlichen vs. privaten Repositories | npm Dependency Confusion-Angriffe | Private Registry-Konfiguration, Namespace-Reservierung |
| Anmeldediebstahl | Gestohlene Lieferantenanmeldedaten für Zugang genutzt | Okta/LastPass-Vorfälle | MFA-Durchsetzung, Anmeldedatenüberwachung, geringstmögliche Berechtigung |
| Watering-Hole | Entwicklungstools oder Websites des Lieferanten kompromittiert, um Nachgelagerte zu infizieren | CCleaner, NotPetya via MeDoc | Netzwerksegmentierung, Endpoint-Erkennung, Lieferkettenüberwachung |
| Social Engineering | Angriffe auf Lieferantenpersonal durch Phishing oder Pretexting | LAPSUS$-Angriffe auf Lieferanten | Sicherheitsbewusstseinsanforderungen für Lieferanten, Authentifizierungshärtung |
| Insider-Bedrohung | Böswilliger Lieferantenmitarbeiter oder Auftragnehmer | Snowden-ähnliche Exfiltration | Hintergrundüberprüfungen, Zugriffskontrollen, Aktivitätsüberwachung, Aufgabentrennung |

## Lieferkettensicherheitskontrollen

| Kontrolle | Beschreibung |
|----------|-------------|
| Lieferantennetzwerksegmentierung | Lieferantenzugang auf dedizierte Segmente isolieren, keine laterale Bewegung zur Produktion |
| Privilegiertes Zugriffsmanagement | PAM für alle privilegierten Lieferantenzugänge fordern, Sitzungsaufzeichnung |
| Kontinuierliche Überwachung | Lieferantenaktivitäten protokollieren und Alarme setzen, Verhaltensanalyse, Anomalieerkennung |
| Integritätsverifizierung | Prüfsummen/Signaturen für Updates, Downloads und Kommunikation von Lieferanten verifizieren |
| Incident-Response-Planung | Lieferkettenkompromittierungsszenarien in Incident-Response-Pläne und Tabletop-Übungen einbeziehen |
| Ersatzlieferanten | Alternativen für kritische Lieferanten identifizieren und vorqualifizieren (Multi-Vendor-Strategie) |
| Lieferketten-Bedrohungsinformationen | Bedrohungsinformationen zu lieferantenbezogenen Schwachstellen und Kompromittierungen überwachen |
| Software-Attestierung | Lieferanten zur Attestierung der Build-Integrität und Sicherheitspraktiken verpflichten |

## Indikatoren für Kompromittierungserkennung

Überwachung auf Anzeichen einer Lieferkettenkompromittierung:

- Unerwartete Lieferantenanmeldedatennutzung (Zeit, Ort, Volumen)
- Ungewöhnliche Datenzugriffsmuster durch Lieferantenkonten
- Software-Updates mit unerwarteten Code-Änderungen oder fehlenden Signaturen
- Neue Sub-Lieferanten oder Serviceabhängigkeiten, die nicht vorher offengelegt wurden
- Lieferantenkommunikation über ungewöhnliche Kanäle oder Domains
- Abnormaler Netzwerkverkehr zu/von lieferantenkontrollierten Systemen

---

# Weitergabe von Sicherheitsanforderungen

## Weitergabe durch die Lieferkette

Primärlieferanten sollen Sicherheitsanforderungen durch die gesamte Lieferkette weitergeben:

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Organisation │ ───► │   Lieferant  │ ───► │ Sub-Lieferant│ ───► │ Fourth Party │
│              │      │  (Stufe 1)   │      │              │      │              │
│ Anforderungen│      │ MUSS Anforde-│      │ MUSS Anforde-│      │ MUSS Anforde-│
│ definiert in │      │ rungen wort- │      │ rungen gleich│      │ rungen gleich│
│ dieser Pol.  │      │ getreu weiter│      │ wertig weiter│      │ wertig weiter│
└──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘
```

## Mindestanforderungen für die Weitergabe

| Anforderung | Weitergabe an Sub-Lieferanten | Verifizierungsmethode |
|-------------|------------------------------|----------------------|
| Vertraulichkeitsverpflichtungen | ✓ Immer, wortgetreu | Sub-Lieferantenverträge prüfen |
| Datenschutz (DSGVO Art. 28) | ✓ Bei Verarbeitung personenbezogener Daten | DVVs mit Sub-Auftragsverarbeitern prüfen |
| Sicherheitskontroll-Baseline | ✓ Bei Zugang zu Daten oder Systemen der [Organisation] | Sub-Lieferanten-Zertifizierungen prüfen |
| Störungsmeldung (24 Stunden) | ✓ Immer | Vorfalls-Eskalationsverfahren verifizieren |
| Prüfungskooperation | ✓ Für kritische Sub-Lieferanten | Prüfungsrechtsklausel im Vertrag verifizieren |
| Unterlieferantengenehmigung | ✓ Wenn Sub-Lieferant Fourth Parties nutzt | Beschaffungsprozess des Sub-Lieferanten prüfen |
| Datenresidenz | ✓ Bei geografischen Einschränkungen | Datenverarbeitungsstandorte verifizieren |
| Sichere Entwicklungspraktiken | ✓ Bei involvierter Software-Entwicklung | SDLC-Dokumentation prüfen |

**Verifizierung**: Die [Organisation] kann Nachweise der Weitergabe anfordern, einschliesslich:

- Auszüge aus Sub-Lieferantenverträgen (geschwärzt für nicht-sicherheitsrelevante Bedingungen)
- Sicherheitsfragebögen und Zertifizierungen von Sub-Lieferanten
- Lieferantenmanagementverfahren des Lieferanten
- Auditberichte zum Sub-Lieferantenmanagement

---

# Überwachung & Überprüfung

## Lieferkettenüberwachungsaktivitäten

| Aktivität | Häufigkeit | Verantwortlich | Dokumentation |
|-----------|-----------|---------------|--------------|
| Sub-Lieferantenregister-Überprüfung | Vierteljährlich | Einkauf + Sicherheit | Aktualisiertes Register, Prüfungsnotizen |
| Fourth-Party-Risikobewertung | Jährlich | Sicherheitsrisikomanagement | Risikobewertungsbericht |
| Software-Abhängigkeits-Scan | Kontinuierlich (automatisiert) | IT-Betrieb + Entwicklung | Scan-Ergebnisse, Behebungstickets |
| Lieferkettenvorfalls-Überprüfung | Bei Eintreten | Sicherheits-Incident-Response | Vorfallsbericht, Lessons Learned |
| Validierung kritischer Abhängigkeiten | Halbjährlich | IT-Betrieb | Abhängigkeitsabbildung, SLA-Verifizierung |
| Konzentrationsrisikobewertung | Jährlich | ISB + Risikomanagement | Konzentrationsanalyse, Mitigierungsplan |
| SBOM-Überprüfung (kritische Software) | Vierteljährlich | Sicherheit + IT | SBOM-Validierung, Schwachstellenbewertung |

## Lieferketten-Kennzahlen und KPIs

| Kennzahl | Ziel | Messmethode |
|----------|------|------------|
| Sub-Lieferantentransparenz (Stufe 1) | 100 % dokumentiert | Registervollständigkeits-Audit |
| Kritische Abhängigkeiten identifiziert | 100 % dokumentiert | Abhängigkeitsinventar-Vollständigkeit |
| SBOM-Abdeckung (kritische Software) | 100 % verfügbar, <90 Tage alt | SBOM-Sammlung und -Validierung |
| Anfällige Abhängigkeiten | 0 kritische, <5 hohe | SCA-Tool-Befunde |
| Lieferkettenvorfälle | Erfassen und Trend verfolgen, Ursachenanalyse für alle | Incident-Management-System |
| Sub-Lieferanten-Zertifizierungsrate (S1) | >90 % ISO 27001 oder SOC 2 | Zertifizierungsverfolgung |
| Konzentrationsrisikopunktzahl | Unter Schwellenwert halten | Konzentrationsrisikobewertung |

## Lieferketten-Berichterstattung

**Vierteljährlicher Lieferkettenbericht** soll enthalten:

- Sub-Lieferantenänderungen (Ergänzungen, Entfernungen, Modifikationen)
- Fourth-Party-Risikoübersicht (kritische Abhängigkeiten, identifizierte Risiken)
- Software-Schwachstellentrends (neue CVEs, Behebungsstatus)
- Lieferkettenvorfälle (Zusammenfassung, Auswirkung, Behebung)
- Aktualisierungen der Konzentrationsrisikobewertung
- Non-Compliance-Probleme und Abhilfepläne

**Zielgruppe**: ISB, ITL, Risikomanagement, Geschäftsleitung (Jahresübersicht)

---

# Regulatorische Anforderungen

## DORA Sub-Auslagerung (Artikel 30)

Für von DORA erfasste IKT-Dienste soll ein umfassendes Sub-Auslagerungs-Register geführt werden, einschliesslich:

- Alle Sub-Auslagerungs-Vereinbarungen von IKT-Drittanbieter-Dienstleistern
- Art der ausgelagerten Funktionen
- Jurisdiktionen, in denen Sub-Auslagerung stattfindet
- Datum der Sub-Auslagerungs-Verträge
- Benachrichtigung der [Organisation] vor der Sub-Auslagerung

**Konzentrationsrisiko**: Konzentrationsrisiko aus Sub-Auslagerungs-Vereinbarungen gemäss DORA Artikel 28 bewerten und dokumentieren.

## FINMA Sub-Auslagerung (Rundschreiben 2023/1)

Für schweizerische Banken, die dem FINMA-Rundschreiben 2023/1 unterliegen, umfassen Sub-Auslagerungs-Anforderungen:

- Umfassendes Register aller Sub-Auslagerungs-Vereinbarungen
- Vorherige Genehmigung der Bank vor wesentlicher Sub-Auslagerung
- Risikobewertung operationeller, Konzentrations-, Datenschutz- und Jurisdiktionsrisiken
- Vertragliche Weitergabe von Bankanforderungen an Sub-Auslagerer
- Prüfungsrechte erstrecken sich auf Sub-Auslagerer (direkt oder über Dienstleister)
- FINMA-Genehmigungsstatus wo erforderlich nachverfolgt

**Konzentrationsrisiko**: Konzentrationsrisiko bei Sub-Auslagerung bewerten, insbesondere wo mehrere Lieferanten von gemeinsamen Sub-Auslagerers abhängen oder wo Sub-Auslagerer in Jurisdiktionen mit begrenzter Durchsetzbarkeit ansässig sind.

## NIS2-Lieferkettensicherheit (Artikel 21)

Für von NIS2 erfasste Einheiten sollen Lieferkettensicherheitsmassnahmen umfassen:

- Richtlinien zur Beschaffung, Entwicklung und Wartung von IKT-Systemen
- Sicherheitsanforderungen für Lieferanten- und Sub-Lieferantenbeziehungen
- Störungsmeldung von Lieferanten, die 24-Stunden-Behördenmeldung ermöglicht
- Lieferkettenrisikobewertung und Mitigierungsstrategien

---

# Referenzen

| Dokument | Beziehung |
|----------|----------|
| **ISMS-POL-A.5.19-23** | Übergeordnetes Richtlinienrahmenwerk |
| **ISMS-POL-A.5.19-23-S1** | Lieferantenklassifizierung und Due Diligence |
| **ISMS-POL-A.5.19-23-S2** | Unterlieferanten-Vertragsanforderungen und Weitergabeklauseln |
| **ISMS-IMP-A.5.19-23.S1-UG/TG** | Lieferanteninventar (einschliesslich Sub-Lieferanten und Abhängigkeiten) |
| **ISO/IEC 27036-3:2023** | Leitlinien für IKT-Lieferkettensicherheit |
| **NIST SP 800-161r1** | Cybersecurity Supply Chain Risk Management-Praktiken |

---

**Nächstes Dokument:** ISMS-POL-A.5.19-23-S4 — Lieferantenüberwachung & Änderungsmanagement (Massnahme A.5.22)

---

*„Ihre Sicherheit ist nur so stark wie der schwächste Lieferant Ihres schwächsten Lieferanten."*
<!-- QA_VERIFIED: 2026-03-28 -->

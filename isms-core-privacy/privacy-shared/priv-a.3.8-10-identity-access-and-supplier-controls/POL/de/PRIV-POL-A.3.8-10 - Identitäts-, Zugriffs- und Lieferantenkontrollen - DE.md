<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.8-10-DE:privacy:POL:a.3.8-10 -->
**PRIV-POL-A.3.8-10 — Identitäts-, Zugriffs- und Lieferantenkontrollen**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Identitäts-, Zugriffs- und Lieferantenkontrollen |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | PRIV-POL-A.3.8-10 |
| **Dokumentersteller** | Datenschutzbeauftragter (DSB) |
| **Dokumentverantwortlicher** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |
| **Privacy-Produktversion** | 1.0 |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | DSB | Erstrichtlinie für ISO/IEC 27701:2025 Erstzertifizierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen regulatorischen oder organisatorischen Änderungen)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Datenschutzbeauftragter (DSB)
- Sekundär: Informationssicherheitsbeauftragter (ISB)
- Legal: Legal/Compliance Officer
- Letztentscheidung: Geschäftsleitung

**Zugehörige Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- PRIV-POL-01 (Datenschutz-Governance und Entscheidungsrahmen)
- PRIV-IMP-A.3.8-10-UG (Identitäts-, Zugriffs- und Lieferantenkontrollen — Benutzerhandbuch)
- PRIV-IMP-A.3.8-10-TG (Identitäts-, Zugriffs- und Lieferantenkontrollen — Technisches Handbuch)
- ISMS-POL-A.5.15-16-18 (Identitäts- und Zugriffsmanagement — ISMS-Pendant)
- ISMS-POL-A.5.19-23 (Cloud-Services und Lieferantenbeziehungen — ISMS-Pendant)
- ISO/IEC 27701:2025 Kontrollen A.3.8, A.3.9, A.3.10
- ISO/IEC 27701:2025 Anhang B (Implementierungsleitfaden B.3.8, B.3.9, B.3.10)
- GDPR Art. 25 (Datenschutz durch Technikgestaltung und durch datenschutzfreundliche Voreinstellungen); Art. 28 (Auftragsverarbeiterpflichten); Art. 32 (Sicherheit der Verarbeitung)
- CH FADP Art. 7 (Datensicherheit); Art. 9 (Auftragsverarbeitungsvereinbarungen)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für Identitätslebenszyklusmanagement, Zugriffsrechte-Governance und Informationssicherheitspflichten in Lieferantenvereinbarungen im Zusammenhang mit der Verarbeitung personenbezogener Daten (PII) fest — gemäss ISO/IEC 27701:2025 Kontrollen A.3.8, A.3.9 und A.3.10.

**Anwendungsbereich**: Alle Identitäten, die für den Zugriff auf PII oder PII-Verarbeitungssysteme verwendet werden; alle Zugriffsrechte auf PII und zugehörige Assets; alle Lieferantenbeziehungen, bei denen Informationssicherheitsanforderungen für die PII-Verarbeitung gelten.

**Zweck**: Festlegung organisatorischer Anforderungen für:

- Vollständiges Lebenszyklusmanagement der mit der PII-Verarbeitung verbundenen Identitäten (A.3.8)
- Bereitstellung, Überprüfung, Änderung und Entfernung von Zugriffsrechten auf PII und zugehörige Assets (A.3.9)
- Festlegung und Vereinbarung von Informationssicherheitsanforderungen für die PII-Verarbeitung mit jedem Lieferanten (A.3.10)

Diese Richtlinie legt fest, **WAS** für Identitätslebenszyklus-, Zugriffsrechte- und Lieferantensicherheitsanforderungen für PII gelten, **WER** die Verantwortung für diese Kontrollen trägt und **WANN** Überprüfungen und Aktualisierungen stattfinden. Implementierungsverfahren (**WIE**) sind in PRIV-IMP-A.3.8-10-UG und PRIV-IMP-A.3.8-10-TG dokumentiert.

**Rollenanwendbarkeit**: Diese Richtlinie gilt für [Organisation] in der Rolle als **PII-Verantwortlicher und PII-Auftragsverarbeiter**. Die Kontrollen A.3.8, A.3.9 und A.3.10 sind gemeinsame Kontrollen (Tabelle A.3) und gelten unabhängig von der Verarbeitungsrolle.

**Begründung für die zusammengefassten Kontrollen**: A.3.8 (Identitätslebenszyklus), A.3.9 (Zugriffsrechte) und A.3.10 (Lieferantensicherheit) bilden die Zugriffs-Governance-Triade für den PII-Schutz. Identitäten schaffen die Akteure; Zugriffsrechte bestimmen, was sie erreichen können; Lieferantenvereinbarungen erstrecken diese Kontrollen auf die Lieferkette. Sie werden gemeinsam als integrierte Zugriffs- und Lieferketten-Governance-Schicht über die PII-Verarbeitung implementiert.

---

# Anwendungsbereich und Gültigkeit

## ISO/IEC 27701:2025 Kontrollanforderungen

**Kontrolle A.3.8 — Identitätsmanagement**
Kontrolle A.3.8 verlangt von [Organisation], den vollständigen Lebenszyklus aller Identitäten mit Bezug zur PII-Verarbeitung zu verwalten — umfassend die Bereitstellung, Änderung, Sperrung und Ausserbetriebnahme sowohl menschlicher als auch nicht-menschlicher Identitäten.

**Kontrolle A.3.9 — Zugriffsrechte**
Kontrolle A.3.9 verlangt von [Organisation], Zugriffsrechte auf PII und andere zugehörige Assets gemäss seiner themenspezifischen Zugriffskontrollrichtlinie und -regeln bereitzustellen, zu überprüfen, zu ändern und zu entfernen.

**Kontrolle A.3.10 — Informationssicherheit in Lieferantenvereinbarungen**
Kontrolle A.3.10 verlangt von [Organisation], relevante Informationssicherheitsanforderungen für die PII-Verarbeitung mit jedem Lieferanten entsprechend der Art der Lieferantenbeziehung festzulegen und zu vereinbaren.

## Was diese Richtlinie abdeckt

**Identitäten (A.3.8)**:

- Alle menschlichen Identitäten (Mitarbeitendenkonten, Auftragnehmerkonten, Zeitarbeiterkonten), die für den Zugriff auf PII oder PII verarbeitende Systeme verwendet werden
- Nicht-menschliche Identitäten (Dienstkonten, Anwendungskonten, automatisierte Verarbeitungskonten), die in PII-Verarbeitungs-Pipelines verwendet werden
- Privilegierte Identitäten mit erweitertem Zugriff auf PII-Verarbeitungsumgebungen oder PII-Datenspeicher
- Identitätslebenszyklusphasen: Bereitstellung, Änderung, Sperrung, Reaktivierung und Ausserbetriebnahme

**Zugriffsrechte (A.3.9)**:

- Zugriffsrechte auf PII-Datenspeicher, Datenbanken und Repositories
- Zugriffsrechte auf Anwendungen und Systeme, die PII verarbeiten
- Zugriffsrechte auf PII-Verarbeitungsinfrastruktur (Server, Cloud-Umgebungen, Verarbeitungsplattformen)
- Zugriffsrechte auf zugehörige Assets, soweit diese die PII-Verarbeitung unterstützen (z.B. Backup-Systeme, Protokollierungsplattformen, Schlüsselmanagementsysteme)

**Lieferantensicherheit (A.3.10)**:

- Alle Lieferanten, die PII im Auftrag von [Organisation] verarbeiten (PII-Auftragsverarbeiter)
- Alle Lieferanten, die im Rahmen ihrer Leistungserbringung Zugang zu PII oder PII-Verarbeitungssystemen haben (z.B. IT-Support, verwaltete Dienste, SaaS-Anbieter)
- Informationssicherheitsanforderungen für die PII-Verarbeitung, die in Lieferantenvereinbarungen festgelegt und vereinbart werden müssen
- Differenzierung der Lieferantentypen für die Verhältnismässigkeit der Anforderungen

## Was diese Richtlinie NICHT abdeckt

- Identitätsbereitstellungs-Workflows und -Werkzeuge (siehe PRIV-IMP-A.3.8-10-TG)
- Technische Konfiguration der Zugriffskontrolle (siehe PRIV-IMP-A.3.8-10-TG)
- Sorgfaltsprüfungs- und Auswahlverfahren für Lieferanten (siehe PRIV-POL-A.2.2.2-7 für auftragsverarbeiterspezifische Kontrollen)
- Lieferantenüberwachung und Performance-Management (siehe ISMS-POL-A.5.19-23)
- Anforderungen an Vertraulichkeits- und Geheimhaltungsvereinbarungen (siehe PRIV-POL-A.3.17-19)
- Anforderungen an Authentifizierungstechnologien (siehe PRIV-POL-A.3.23-31)

## Regulatorischer Rahmen

**Tier 1: Obligatorische Compliance** (gemäss PRIV-POL-00):

- **EU GDPR**: Art. 25 (Zugriffskontrolle als Massnahme des Datenschutzes durch Technikgestaltung); Art. 28 (Auftragsverarbeitungsvereinbarungen müssen angemessene Sicherheitspflichten enthalten); Art. 32 (angemessene technische Massnahmen einschliesslich Zugriffskontrollen); Art. 5(1)(f) (Grundsatz der Integrität und Vertraulichkeit)
- **CH FADP**: Art. 7 (technische und organisatorische Sicherheitsmassnahmen); Art. 9 (Auftragsverarbeitungsvereinbarungen müssen gleichwertigen Datenschutz gewährleisten)
- **ISO/IEC 27701:2025**: Kontrollen A.3.8, A.3.9, A.3.10 (normativ)

**Tier 2: Bedingte Anwendbarkeit** (gemäss PRIV-POL-00):

- **ISO/IEC 27018:2025**: Anhang A — Offenlegungsanforderungen für Lieferanten und Unterauftragsverarbeiter (A.2.5.7–A.2.5.9), sofern Cloud-PII-Verarbeitung im Anwendungsbereich

**Tier 3: Informative Referenz** (gemäss PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementierungsleitfaden für Identitätsmanagement (5.15–5.18), Zugriffskontrolle (5.15) und Lieferantenbeziehungen (5.19–5.21)
- **ISO/IEC 27701:2025 Anhang B**: Implementierungsleitfaden B.3.8, B.3.9, B.3.10

Für eine vollständige regulatorische Kategorisierung siehe PRIV-POL-00.

---

# Richtlinienanforderungen: Identitätslebenszyklusmanagement für die PII-Verarbeitung (A.3.8)

## Anforderungen an den Identitätslebenszyklus

[Organisation] **muss** den vollständigen Lebenszyklus aller Identitäten mit Zugang zu PII oder PII-Verarbeitungssystemen verwalten. Das Identitätslebenszyklusmanagement für PII **muss** mit den ISMS-Identitätsmanaementanforderungen (ISMS-POL-A.5.15-16-18) konsistent sein und diese mit den in dieser Richtlinie definierten PII-spezifischen Anforderungen erweitern.

### Identitätsbereitstellung für PII-Zugang

Identitäten, denen Zugang zu PII oder PII-Verarbeitungssystemen gewährt wird, **müssen** auf folgender Grundlage bereitgestellt werden:

- **Dokumentierter Geschäftszweck**: Eine dokumentierte und genehmigte Geschäftsbegründung für den PII-Zugang muss vor der Bereitstellung vorliegen
- **Rollenausrichtung**: Der Zugang **muss** auf die dokumentierten PII-Verarbeitungsverantwortlichkeiten der Rolle abgestimmt sein; Zugang zu PII, der für die Rolle nicht erforderlich ist, **darf nicht** bereitgestellt werden
- **Minimalrecht**: Identitäten **müssen** mit dem für den dokumentierten Zweck minimal notwendigen Zugangsumfang bereitgestellt werden (Grundsatz der minimal notwendigen Verarbeitung, konsistent mit GDPR Art. 5(1)(c) Datenminimerung)
- **Genehmigungsinstanz**: Die PII-Zugriffsbereitstellung erfordert die Genehmigung des Data Owner für den relevanten PII-Datensatz oder des DSB, wenn kein Data Owner zugewiesen ist

### Identitätsänderung und -sperrung

Wenn sich eine Rolle ändert, eine Person in eine andere Funktion wechselt oder sich die Umstände so ändern, dass ein zuvor begründeter PII-Zugangszweck nicht mehr zutrifft:

- PII-Zugriffsrechte **müssen** innerhalb der in PRIV-IMP-A.3.8-10-TG festgelegten Frist geändert oder gesperrt werden
- Die Benachrichtigung über Rollenänderungen **muss** durch die Linienführung an das IT-Sicherheitsteam weitergegeben und dokumentiert werden
- Sperrung (keine sofortige Löschung) **muss** angewandt werden, wenn ein Legal Hold oder eine Untersuchung die Aufbewahrung von Identitätsaufzeichnungen erfordert

### Identitätsausserbetriebnahme

Wenn das Arbeitsverhältnis oder die Beauftragung einer Person endet oder der Zweck eines Dienstkontos beendet wird:

- PII-Zugriffsrechte **müssen** am oder vor dem letzten Zugangtag entfernt werden (Mitarbeitendenaustritt, Vertragsende)
- Aufzeichnungen über die Identitätsausserbetriebnahme **müssen** 3 Jahre ab dem Ausserbetriebnahmedatum aufbewahrt werden, um Prüfung und Untersuchung zu unterstützen
- Wenn die Ausserbetriebnahme aus technischen Gründen verzögert ist, **muss** der Zugang sofort gesperrt und die Ausserbetriebnahme innerhalb von 5 Werktagen abgeschlossen werden
- Um eine rechtzeitige Ausserbetriebnahme sicherzustellen, wenn keine HR-Benachrichtigung eingeht, **muss** IT-Sicherheit monatlich aktive Identitäten mit PII-Zugang mit aktuellen HR-Aufzeichnungen abgleichen; jede Identität ohne aktuellen aktiven Beschäftigungs- oder Beauftragungsstatus **muss** bis zur DSB-Bestätigung gesperrt werden

### Verwaltung nicht-menschlicher Identitäten

Dienstkonten, Anwendungskonten und automatisierte Verarbeitungskonten, die in PII-Verarbeitungs-Pipelines verwendet werden, **müssen**:

- Individuell identifiziert und im Identitätsregister registriert sein
- Einem verantwortlichen menschlichen Eigentümer zugewiesen sein (verantwortlich für den Lebenszyklus des Dienstkontos)
- Einer periodischen Überprüfung unterliegen (mindestens jährlich), um die fortgesetzte Notwendigkeit zu bestätigen
- Ausser Betrieb genommen werden, wenn der von ihnen unterstützte Verarbeitungszweck eingestellt wird

---

# Richtlinienanforderungen: Zugriffsrechte auf PII und zugehörige Assets (A.3.9)

## Anforderungen an Zugriffsrechte

[Organisation] **muss** sicherstellen, dass Zugriffsrechte auf PII und zugehörige Assets gemäss der ISMS-Zugriffskontrollrichtlinie (ISMS-POL-A.5.15-16-18) und den in dieser Richtlinie definierten PII-spezifischen Erweiterungen bereitgestellt, überprüft, geändert und entfernt werden.

### Grundsätze für PII-Zugriffsrechte

Zugriffsrechte auf PII **müssen** nach folgenden Grundsätzen geregelt werden:

1. **Minimal notwendiger Zugang**: Der gewährte Zugang ist auf das minimale PII und die minimalen zugehörigen Assets zu beschränken, die zur Erfüllung des dokumentierten Verarbeitungszwecks erforderlich sind
2. **Verarbeitungsnotwendigkeit**: Zugang wird nur gewährt, wenn ein dokumentierter und aktueller Bedarf zur Verarbeitung der spezifischen PII besteht
3. **Funktionstrennung**: Wenn die PII-Verarbeitung Hochrisikooperationen umfasst (Löschung, Export, Massenzugriff), **müssen** Funktionstrennnungskontrollen implementiert werden, um Missbrauch durch einzelne Akteure zu verhindern. Der Mindeststandard ist, dass keine einzelne Identität eine Hochrisiko-PII-Operation sowohl initiieren als auch genehmigen kann
4. **Zeitlich begrenzter Zugang**: Wenn Zugang für ein bestimmtes Projekt, eine Aufgabe oder einen vorübergehenden Zweck gewährt wird, **müssen** Zugriffsrechte zeitlich begrenzt und bei Ablauf automatisch überprüft werden

### Überprüfung von Zugriffsrechten auf PII

Zugriffsrechte auf PII und PII-Verarbeitungssysteme **müssen** überprüft werden:

- **Mindestens jährlich** für alle Zugriffsrechte (formale Zertifizierung)
- **Bei Rollenänderung** für die betroffene Person
- **Bei organisatorischer Änderung** (Umstrukturierung, Geschäftseinheitsänderungen), die Verarbeitungszwecke berührt
- **Nach einem Datenschutzvorfall**, der nicht autorisierten oder unangemessenen Zugriff auf PII beinhaltete
- **Auf Anfrage des Data Owner** für den relevanten PII-Datensatz

Überprüfungen von Zugriffsrechten **müssen** dokumentiert werden. Als nicht mehr notwendig bestätigte Rechte **müssen** innerhalb von 5 Werktagen bei Standardzugang und sofort bei privilegiertem Zugang entfernt werden. Überprüfungsaufzeichnungen **müssen** als Nachweis aufbewahrt werden.

### Privilegierter Zugang zu PII

Privilegierter Zugang zu PII-Verarbeitungssystemen (Administratorzugang, Massendatenzugang, Datenbankadministratorrechte, Backup- und Wiederherstellungszugang) erfordert:

- Ausdrückliche DSB-Benachrichtigung und Data Owner-Genehmigung vor der Gewährung
- Separate privilegierte Identität (nicht mit der Standard-Benutzeridentität kombiniert)
- Verbesserte Prüfprotokollierung privilegierter Sitzungsaktivitäten mit PII-Bezug
- Häufigere periodische Überprüfung (mindestens alle 6 Monate)
- Sofortiger Widerruf bei jedem Hinweis auf Missbrauch

### Zugriffsrechteregister

[Organisation] **muss** ein Zugriffsrechteregister für PII führen, das dokumentiert:

- Identitäten mit Zugang zu PII, nach Datensatz und System
- Gewährte Zugangsebene und -umfang
- Genehmigungsgrundlage und Genehmiger-Identität
- Datum der Gewährung und Datum der letzten Überprüfung
- Ablaufdatum (bei zeitlich begrenztem Zugang)

Das Zugriffsrechteregister wird vom IT-Sicherheitsteam unter DSB-Aufsicht geführt. Struktur und Pflegeverfahren sind in PRIV-IMP-A.3.8-10-TG definiert.

---

# Richtlinienanforderungen: Informationssicherheit in Lieferantenvereinbarungen (A.3.10)

## Lieferantensicherheitsanforderungen für PII

[Organisation] **muss** relevante Informationssicherheitsanforderungen für die PII-Verarbeitung mit jedem Lieferanten proportional zur Art der Lieferantenbeziehung festlegen und vereinbaren.

### Lieferantenkategorisierung für PII-Anforderungen

Lieferanten werden nach ihrer Beziehung zur PII-Verarbeitung kategorisiert, um anwendbare Anforderungen zu bestimmen:

| Lieferantenkategorie | Beschreibung | Mindestanforderungen |
|---------------------|-------------|---------------------|
| **PII-Auftragsverarbeiter** | Verarbeitet PII direkt im Auftrag von [Organisation] auf Weisung | Vollständige Auftragsverarbeitungsvereinbarung gemäss GDPR Art. 28 / CH FADP Art. 9 + PII-Sicherheitsanhang |
| **PII-benachbarter Lieferant** | Hat im Rahmen der Leistungserbringung Zugang zu Systemen oder Umgebungen mit PII (z.B. IT Managed Services, Cloud-Infrastruktur, Wartung) | Vertraulichkeitspflicht + Einschränkungen für den Umgang mit Daten + Verletzungsmeldungspflicht |
| **Kein PII-Zugang** | Erbringt Dienste ohne Zugang zu PII oder PII-Verarbeitungssystemen | Standard-Lieferantensicherheitsbedingungen (ISMS-POL-A.5.19-23) — kein PII-spezifischer Nachtrag erforderlich |

### Obligatorische PII-Sicherheitsanforderungen in Lieferantenvereinbarungen

Für die Kategorien PII-Auftragsverarbeiter und PII-benachbarter Lieferant **müssen** folgende Informationssicherheitsanforderungen für die PII-Verarbeitung in der Lieferantenvereinbarung festgelegt und vereinbart werden:

**Sicherheitspflichten**:

- Verpflichtung zur Implementierung und Aufrechterhaltung geeigneter technischer und organisatorischer Sicherheitsmassnahmen für PII, die nicht weniger schützend sind als die eigenen Anforderungen von [Organisation]
- Pflicht, PII ausschliesslich auf Weisung von [Organisation] zu verarbeiten (für Auftragsverarbeiter)
- Verbot der Nutzung von PII für eigene Zwecke des Lieferanten

**Vertraulichkeit**:

- Mitarbeitende des Lieferanten mit Zugang zu PII sind durch Vertraulichkeitspflichten gebunden
- Vertraulichkeitspflichten überdauern die Beendigung der Vereinbarung

**Verletzungsmeldung**:

- Pflicht zur Benachrichtigung von [Organisation] über jeden tatsächlichen oder vermuteten PII-Sicherheitsvorfall innerhalb der in der Vereinbarung festgelegten Frist (abgestimmt auf regulatorische Benachrichtigungsfristen — maximal 24 Stunden bei Risiko einer Datenpanne)
- Kooperation bei Untersuchung und Behebung

**Kontrolle von Unterauftragsverarbeitern/Unterauftragnehmern**:

- Vorherige schriftliche Zustimmung erforderlich, bevor Unterauftragsverarbeiter mit Zugang zur PII von [Organisation] beauftragt werden
- Weitergabe gleichwertiger Sicherheitspflichten an jeden Unterauftragsverarbeiter

**Prüfungsrechte**:

- Recht von [Organisation], die PII-Sicherheitsmassnahmen des Lieferanten zu prüfen oder zu beurteilen, oder Drittanbieter-Prüfberichte zu erhalten (z.B. ISO 27001-Zertifizierung, SOC 2 Typ II)

**Rückgabe und Löschung**:

- Bei Beendigung oder auf Anfrage muss der Lieferant alle PII zurückgeben oder sicher löschen und die Löschung schriftlich bestätigen

**Regulatorische Compliance**:

- Der Lieferant erkennt den anwendbaren regulatorischen Rahmen (GDPR, CH FADP) an und verpflichtet sich zur Compliance bei seinen Verarbeitungsaktivitäten

### Überprüfung von Lieferantenvereinbarungen

PII-bezogene Lieferantenvereinbarungen **müssen** überprüft werden:

- Mindestens jährlich oder bei Vertragsverlängerung
- Bei wesentlicher Änderung der Art der vom Lieferanten verarbeiteten PII
- Nach einem Sicherheitsvorfall mit Beteiligung des Lieferanten
- Bei wesentlichen Änderungen der anwendbaren regulatorischen Anforderungen
- Bei Benachrichtigung über eine Änderung der Unterauftragsverarbeiter-Vereinbarungen des Lieferanten

---

# Rollen und Verantwortlichkeiten

## Verantwortungsmatrix

| Rolle | Verantwortlichkeiten für A.3.8–A.3.10 |
|-------|---------------------------------------|
| **Datenschutzbeauftragter (DSB)** | Genehmigt privilegierten PII-Zugang; überwacht Zugriffsrechteregister; genehmigt PII-relevante Lieferantenvereinbarungen; überprüft Lieferantenkategorisierungsentscheidungen; führt Auftragsverarbeitungsvereinbarungsregister |
| **Data Owner** | Genehmigt PII-Zugriffsbereitstellung für seinen Datensatz; führt oder überwacht periodische Zugriffsrechteüberprüfungen; eskaliert unautorisierten Zugriff an DSB und ISB |
| **ISB** | Definiert technische Anforderungen für Identitätslebenszyklus und Zugriffskontrolle; stellt sicher, dass ISMS-Identitätsmanagement auf PII gemäss dieser Richtlinie ausgedehnt wird; überprüft Lieferantensicherheitsanhänge auf technische Angemessenheit |
| **IT-Sicherheitsteam** | Führt Identitätsregister und Zugriffsrechteregister; führt Zugriffsbereitstellung und -ausserbetriebnahme durch; führt Zugriffsrechteüberprüfungen durch; implementiert privilegierte Zugriffskontrollen |
| **Legal/Compliance** | Überprüft PII-Sicherheitsklauseln in Lieferantenvereinbarungen; berät zu Art. 28-Auftragsverarbeitungsvertragsanforderungen; hält sich über regulatorische Änderungen auf dem Laufenden |
| **Beschaffung / Lieferantenmanagement** | Stellt sicher, dass die PII-Lieferantenkategorisierung vor der Vertragsunterzeichnung durchgeführt wird; bezieht Legal/DSB für PII-relevante Vereinbarungen ein; führt Lieferantenvereinbarungsinventar |
| **Linienführung** | Benachrichtigt IT-Sicherheitsteam über Rollenänderungen und Abgänge; genehmigt PII-Zugriffsanfragen für Teammitglieder |

---

# Nachweisanforderungen

Folgende Nachweise belegen den Betrieb dieser Richtlinie:

| Nachweis | Beschreibung | Aufbewahrung |
|---------|-------------|--------------|
| Identitätsregister | Alle Identitäten (menschlich und nicht-menschlich) mit PII-Zugang, einschliesslich Lebenszyklusstatus | Aktuell + 3 Jahre |
| Zugriffsrechteregister | PII-Zugriffsrechte nach Identität, Datensatz und System; Genehmigungs- und Überprüfungsaufzeichnungen | Aktuell + 3 Jahre |
| Zugriffsrechteüberprüfungsaufzeichnungen | Dokumentierter Nachweis der periodischen Zugriffsrechtezertifizierung, einschliesslich entfernter Rechte | 3 Jahre ab Überprüfungsdatum |
| Lieferantenvereinbarungsinventar | Liste aller Lieferantenvereinbarungen mit PII-Kategorisierung und Verweis auf PII-Sicherheitsklausel | Aktuell + 3 Jahre |
| Lieferantenvereinbarungskopien | Unterzeichnete Vereinbarungen (oder Vertragsanhänge) mit PII-Sicherheitspflichten | Vertragsdauer + 3 Jahre |
| Genehmigungsaufzeichnungen für privilegierten Zugang | DSB-Benachrichtigungen und Data Owner-Genehmigungen für privilegierten PII-Zugang | 3 Jahre ab dem Datum des Zugangswiderrufs |
| Identitätsausserbetriebnahmeaufzeichnungen | Nachweis der rechtzeitigen Zugangsentfernung bei Abgang oder Rollenänderung | 3 Jahre ab Ausserbetriebnahmedatum |

---

# Prüfungshinweise

Prüfer, die die Compliance mit A.3.8, A.3.9 und A.3.10 verifizieren, sollten Folgendes vorfinden:

**Für A.3.8 (Identitätsmanagement)**:
- Identitätsregister mit allen menschlichen und nicht-menschlichen Identitäten mit PII-Zugang
- Nachweis dokumentierter Genehmigung für die PII-Zugriffsbereitstellung
- Aufzeichnungen über Identitätsausserbetriebnahme bei Abgang oder Rollenänderung
- Periodische Überprüfungsaufzeichnungen für nicht-menschliche Identitäten

**Für A.3.9 (Zugriffsrechte)**:
- Zugriffsrechteregister für PII mit aktuellen dokumentierten Zugriffsrechten
- Nachweis periodischer Zugriffsrechteüberprüfungen (mindestens jährlich)
- Aufzeichnungen über Zugriffsänderung oder -entfernung nach Rollenänderungen
- Genehmigungsaufzeichnungen und Überprüfungsaufzeichnungen für privilegierten Zugang
- Nachweis der Funktionstrennung bei Hochrisiko-PII-Operationen

**Für A.3.10 (Lieferantenvereinbarungen)**:
- Lieferantenkategorisierungsaufzeichnungen (PII-Auftragsverarbeiter / PII-benachbart / kein PII-Zugang)
- Unterzeichnete Lieferantenvereinbarungen mit PII-Informationssicherheitsanforderungen
- Nachweis jährlicher Überprüfung oder anlassbezogener Überprüfung von PII-Lieferantenvereinbarungen
- Unterauftragsverarbeiter-Genehmigungsaufzeichnungen und Bestätigung der Weitergabepflichten

---

<!-- QA_VERIFIED: 2026-03-29 -->

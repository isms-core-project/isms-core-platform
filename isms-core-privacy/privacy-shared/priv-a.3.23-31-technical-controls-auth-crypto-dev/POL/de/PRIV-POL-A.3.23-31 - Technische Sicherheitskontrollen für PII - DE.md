<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.23-31-DE:privacy:POL:a.3.23-31 -->
**PRIV-POL-A.3.23-31 — Technische Sicherheitskontrollen für PII**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Technische Sicherheitskontrollen für PII |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | PRIV-POL-A.3.23-31 |
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
- Technisch: Entwicklungsleiter / IT-Architektur
- Letztentscheidung: Geschäftsleitung

**Zugehörige Dokumente**:

- PRIV-POL-00 (Regulatorischer Anwendbarkeitsrahmen für den Datenschutz)
- PRIV-POL-01 (Datenschutz-Governance und Entscheidungsrahmen)
- PRIV-IMP-A.3.23-31-UG (Technische Sicherheitskontrollen für PII — Benutzerhandbuch)
- PRIV-IMP-A.3.23-31-TG (Technische Sicherheitskontrollen für PII — Technisches Handbuch)
- ISMS-POL-A.8.2 (Privilegierte Zugriffsrechte — ISMS-Pendant)
- ISMS-POL-A.8.5 (Sichere Authentifizierung — ISMS-Pendant)
- ISMS-POL-A.8.13 (Informationssicherung — ISMS-Pendant)
- ISMS-POL-A.8.15-16 (Protokollierung und Überwachung — ISMS-Pendant)
- ISMS-POL-A.8.24 (Verwendung von Kryptografie — ISMS-Pendant)
- ISMS-POL-A.8.25-31 (Sichere Entwicklung — ISMS-Pendant)
- ISO/IEC 27701:2025 Kontrollen A.3.23 bis A.3.31
- ISO/IEC 27701:2025 Anhang B (Implementierungsleitfaden B.3.23 bis B.3.31)
- GDPR Art. 25 (Datenschutz durch Technikgestaltung und durch datenschutzfreundliche Voreinstellungen); Art. 32 (Sicherheit der Verarbeitung)
- CH FADP Art. 7 (Technische und organisatorische Massnahmen)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für technische Sicherheitskontrollen im Zusammenhang mit der Verarbeitung personenbezogener Daten (PII) fest, umfassend Authentifizierung, Datensicherung, Protokollierung, Kryptografie, sichere Entwicklung, Anwendungssicherheit, Systemarchitektur, ausgelagerte Entwicklung und Testinformationen — gemäss ISO/IEC 27701:2025 Kontrollen A.3.23 bis A.3.31.

**Anwendungsbereich**: Alle technischen Kontrollen, die für Systeme, Anwendungen und Infrastruktur implementiert sind, die PII verarbeiten; alle Software- und Systementwicklungsaktivitäten mit PII-Verarbeitung; alle Testumgebungen, die PII verwenden oder simulieren.

**Zweck**: Festlegung organisatorischer Anforderungen für neun technische Kontrollbereiche, die PII auf System- und Entwicklungsebene schützen. Diese Richtlinie legt fest, **WAS** für technische Anforderungen für PII-verarbeitende Systeme gelten, **WER** die Verantwortung trägt und **WANN** Überprüfungen und Verifizierungen stattfinden. Implementierungsverfahren (**WIE**) sind in PRIV-IMP-A.3.23-31-UG und PRIV-IMP-A.3.23-31-TG dokumentiert.

**Rollenanwendbarkeit**: Diese Richtlinie gilt für [Organisation] in der Rolle als **PII-Verantwortlicher und PII-Auftragsverarbeiter**. Die Kontrollen A.3.23–A.3.31 sind gemeinsame Kontrollen (Tabelle A.3) und gelten unabhängig von der Verarbeitungsrolle.

**Begründung für die zusammengefassten Kontrollen**: A.3.23–A.3.31 bilden die technische Assurance-Schicht für die PII-Verarbeitung. Sie erweitern und spezialisieren das ISMS-technische Kontrollrahmenwerk für PII-Kontexte — und stellen sicher, dass jeder bedeutsame technische Kontrollbereich (Authentifizierung, Datensicherung, Protokollierung, Kryptografie, Entwicklung, Architektur, Auslagerung, Testing) PII ausdrücklich berücksichtigt. GDPR Art. 25 (Privacy by Design und by Default) und Art. 32 (angemessene technische Massnahmen) bilden die regulatorische Grundlage für diese Gruppe als Ganzes.

---

# Anwendungsbereich und Gültigkeit

## ISO/IEC 27701:2025 Kontrollanforderungen

**Kontrolle A.3.23 — Sichere Authentifizierung**
Kontrolle A.3.23 verlangt von [Organisation], sichere Authentifizierungstechnologien und -verfahren für PII-Verarbeitungssysteme zu implementieren, abgestimmt auf die für jedes System oder jeden Datensatz geltenden Zugriffseinschränkungen.

**Kontrolle A.3.24 — Informationssicherung**
Kontrolle A.3.24 verlangt von [Organisation], Sicherungskopien von PII sowie der Software und Systeme der PII-Verarbeitung aufzubewahren und diese Sicherungen regelmässig zu testen.

**Kontrolle A.3.25 — Protokollierung**
Kontrolle A.3.25 verlangt von [Organisation], Protokolle zu erzeugen, zu speichern, zu schützen und zu analysieren, die Aktivitäten, Ausnahmen, Fehler und andere relevante Ereignisse im Zusammenhang mit der PII-Verarbeitung aufzeichnen.

**Kontrolle A.3.26 — Verwendung von Kryptografie**
Kontrolle A.3.26 verlangt von [Organisation], Regeln für den effektiven Einsatz von Kryptografie im PII-Verarbeitungskontext — einschliesslich kryptografischem Schlüsselmanagement — zu definieren und umzusetzen.

**Kontrolle A.3.27 — Sicherer Entwicklungslebenszyklus**
Kontrolle A.3.27 verlangt von [Organisation], Regeln für die sichere Entwicklung von Software und Systemen, die an der PII-Verarbeitung beteiligt sind, festzulegen und anzuwenden.

**Kontrolle A.3.28 — Anwendungssicherheitsanforderungen**
Kontrolle A.3.28 verlangt von [Organisation], Informationssicherheitsanforderungen im Zusammenhang mit der PII-Verarbeitung bei der Entwicklung oder Beschaffung von Anwendungen zu identifizieren, zu spezifizieren und zu genehmigen.

**Kontrolle A.3.29 — Sichere Systemarchitektur und Engineeringprinzipien**
Kontrolle A.3.29 verlangt von [Organisation], Prinzipien für die Entwicklung sicherer Systeme im Kontext der PII-Verarbeitung über alle Informationssystementwicklungsaktivitäten hinweg festzulegen, zu dokumentieren, aufrechtzuerhalten und anzuwenden.

**Kontrolle A.3.30 — Ausgelagerte Entwicklung**
Kontrolle A.3.30 verlangt von [Organisation], Aktivitäten im Zusammenhang mit der ausgelagerten Entwicklung von Systemen für die PII-Verarbeitung zu leiten, zu überwachen und zu überprüfen.

**Kontrolle A.3.31 — Testinformationen**
Kontrolle A.3.31 verlangt von [Organisation], im Kontext von PII-Verarbeitungssystemen verwendete Testinformationen angemessen auszuwählen, zu schützen und zu verwalten.

## Was diese Richtlinie abdeckt

Alle neun oben aufgeführten Kontrollen, angewandt auf:

- Systeme und Anwendungen, die PII als Teil ihrer Hauptfunktion verarbeiten
- Infrastruktur und Plattformen, die PII-Verarbeitungssysteme hosten oder mit diesen verbunden sind
- Software und Systeme, die für PII-Verarbeitungszwecke entwickelt oder beschafft werden
- Testumgebungen, die während der Entwicklung, Qualitätssicherung oder Integration von PII-verarbeitenden Systemen verwendet werden

## Was diese Richtlinie NICHT abdeckt

- ISMS-weite technische Kontrollen (vollständiges technisches Kontrollrahmenwerk siehe ISMS-POL-A.8.x)
- Zugriffsrechte-Governance (siehe PRIV-POL-A.3.8-10)
- Endgeräteverwaltung (siehe PRIV-POL-A.3.20-22)
- Auftragsverarbeitungsvereinbarungsanforderungen (siehe PRIV-POL-A.2.2.2-7)

## Regulatorischer Rahmen

**Tier 1: Obligatorische Compliance** (gemäss PRIV-POL-00):

- **EU GDPR**: Art. 25 (Privacy by Design und by Default — technische Kontrollen als Gestaltungsanforderung); Art. 32 (Pseudonymisierung, Verschlüsselung, Verfügbarkeitswiederherstellung, regelmässige Tests der TOMs)
- **CH FADP**: Art. 7 (technische Massnahmen proportional zum Risiko)
- **ISO/IEC 27701:2025**: Kontrollen A.3.23–A.3.31 (normativ)

**Tier 2: Bedingte Anwendbarkeit** (gemäss PRIV-POL-00):

- **ISO/IEC 27018:2025**: Anhang A — technische Kontrollen für Cloud-PII-Verarbeitung wo anwendbar

**Tier 3: Informative Referenz** (gemäss PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementierungsleitfaden für Kontrollen 8.5 (Authentifizierung), 8.13 (Datensicherung), 8.15–16 (Protokollierung), 8.24 (Kryptografie), 8.25–8.31 (sichere Entwicklung)
- **ISO/IEC 27701:2025 Anhang B**: B.3.23 bis B.3.31

Für eine vollständige regulatorische Kategorisierung siehe PRIV-POL-00.

---

# Richtlinienanforderungen

## A.3.23 — Sichere Authentifizierung für PII-Verarbeitung

[Organisation] **muss** sichere Authentifizierungstechnologien und -verfahren für den Zugang zu PII-Verarbeitungssystemen implementieren, basierend auf den für jeden PII-Datensatz und jedes System definierten Zugriffseinschränkungen.

### Authentifizierungsanforderungen für PII-Systeme

| PII-Sensibilität | Mindest-Authentifizierungsanforderung |
|-----------------|--------------------------------------|
| VERTRAULICHE PII | Multi-Faktor-Authentifizierung (MFA) für Fernzugang; starke Passwortrichtlinie für internen Zugang |
| EINGESCHRÄNKTE PII (besondere Kategorien) | MFA für ALLE Zugriffe erforderlich (intern und extern) |
| Administrativer / privilegierter Zugang zu PII | MFA erforderlich; separate privilegierte Zugangsdaten von Standard-Identität |

Authentifizierungsstandards und genehmigte MFA-Technologien sind in PRIV-IMP-A.3.23-31-TG definiert, konsistent mit ISMS-POL-A.8.5.

### Anforderungen an Authentifizierungsverfahren

- Authentifizierungsverfahren **müssen** Zugriffseinschränkungen durchsetzen, die mit den in PRIV-POL-A.3.8-10 definierten Zugriffsrechten übereinstimmen
- Fehlgeschlagene Authentifizierungsversuche bei PII-Systemen **müssen** protokolliert werden und eine Kontosperrung gemäss den in PRIV-IMP-A.3.23-31-TG definierten Schwellenwerten auslösen
- Authentifizierungsdaten für PII-Systeme **müssen** individuell pro Person sein; gemeinsame Zugangsdaten sind für den PII-Systemzugang verboten

---

## A.3.24 — Sicherung von PII und zugehörigen Systemen

[Organisation] **muss** Sicherungskopien von PII sowie der Software und Systeme der PII-Verarbeitung aufbewahren und die Integrität und Wiederherstellbarkeit dieser Sicherungen regelmässig testen.

### PII-Sicherungsanforderungen

- Alle von [Organisation] verarbeiteten PII **müssen** durch ein Sicherungsregime mit dokumentierten Recovery-Point-Zielen (RPO) abgedeckt sein, die auf die PII-Verarbeitungskritikalität und regulatorischen Anforderungen abgestimmt sind
- Sicherungen mit PII **müssen** denselben Klassifikations- und Zugriffskontrollen wie die primären PII unterliegen (VERTRAULICH oder EINGESCHRÄNKT entsprechend)
- Sicherungskopien mit PII **müssen** mit demselben Standard wie die Primärdaten verschlüsselt sein
- Externe oder Cloud-Sicherungskopien mit PII **müssen** gleichwertigen Sicherheitskontrollen wie der primäre Speicher unterliegen, einschliesslich Zugriffseinschränkungen und Verschlüsselung im Transit und im Ruhezustand

### Sicherungstests

- Sicherungswiederherstellung **muss** mindestens jährlich getestet werden, um zu bestätigen, dass PII wiederherstellbar und vollständig ist
- Ergebnisse von Wiederherstellungstests **müssen** dokumentiert werden, einschliesslich Datenintegritätsverifizierung
- Wiederherstellungstestfehler bei PII **müssen** als Risikoereignis behandelt und dem ISB und DSB eskaliert werden

---

## A.3.25 — Protokollierung für die PII-Verarbeitung

[Organisation] **muss** Protokolle erzeugen, speichern, schützen und analysieren, die Aktivitäten, Ausnahmen, Fehler und andere relevante Ereignisse im Zusammenhang mit der PII-Verarbeitung aufzeichnen.

### PII-Protokollierungsanforderungen

Folgende Ereignisse im Zusammenhang mit der PII-Verarbeitung **müssen** protokolliert werden:

- Zugang zu PII-Datenspeichern (Lesen, Schreiben, Export) durch authentifizierte Benutzer
- Fehlgeschlagene Zugriffsversuche bei PII-Systemen
- Massenoperationen mit PII (Export, Löschung, Pseudonymisierung, Anonymisierung)
- Änderungen der Zugriffsrechte für PII-Systeme (Gewähren, Widerrufen, Ändern)
- Privilegierte Operationen auf PII-Verarbeitungssystemen
- Betroffenenrechtserfüllungsoperationen (Zugang, Löschung, Einschränkung, Übertragbarkeit)
- System- und Anwendungsfehler oder -ausnahmen in PII-Verarbeitungskomponenten

### Protokollschutz

Protokolle mit PII-Verarbeitungsaktivitäten **müssen**:

- Gegen Modifikation und Löschung geschützt sein (manipulationssicherer Speicher)
- Als mindestens VERTRAULICH klassifiziert sein
- Nur für autorisiertes Personal zugänglich sein (IT-Sicherheitsteam, ISB, DSB für Datenschutzuntersuchungszwecke)
- Mindestens 12 Monate als operativer Boden aufbewahrt werden, mit mindestens 3 Jahren für Protokolle, die als Nachweis der GDPR-Rechenschaftspflicht-Compliance benötigt werden könnten (z.B. Zugriffsprotokolle für Betroffenenrechtserfüllung, Massenlöschungs- und Anonymisierungsoperationen und privilegierter Zugang zu PII-Systemen). ISB und DSB vereinbaren spezifische Aufbewahrungsfristen pro Protokollkategorie in PRIV-IMP-A.3.23-31-TG unter Berücksichtigung anwendbarer regulatorischer Anforderungen und vertraglicher Pflichten

### Protokollanalyse

Protokolle **müssen** überprüft werden:

- Ausnahmebasiert (Benachrichtigungen bei anomalen PII-Zugriffsmustern)
- Im Rahmen der periodischen Compliance-Überprüfung (PRIV-POL-A.3.13-16)
- In Reaktion auf einen Datenschutzvorfall (PRIV-POL-A.3.11-12)
- Im Rahmen der Zugriffsrechteüberprüfung (PRIV-POL-A.3.8-10)

Protokollanalysestandards und -werkzeuge sind in PRIV-IMP-A.3.23-31-TG definiert, konsistent mit ISMS-POL-A.8.15-16.

---

## A.3.26 — Kryptografie für die PII-Verarbeitung

[Organisation] **muss** Regeln für den effektiven Einsatz von Kryptografie im Zusammenhang mit der PII-Verarbeitung — einschliesslich kryptografischem Schlüsselmanagement — definieren und umsetzen.

### Kryptografische Anforderungen für PII

- **Verschlüsselung im Ruhezustand**: Alle in Datenbanken, Dateien oder auf Medien gespeicherten VERTRAULICHEN und EINGESCHRÄNKTEN PII **müssen** im Ruhezustand mit einem genehmigten Algorithmus verschlüsselt sein (mindestens AES-256 oder äquivalent gemäss ISMS-POL-A.8.24)
- **Verschlüsselung im Transit**: Alle über Netzwerke übertragenen PII **müssen** im Transit mit aktuellen TLS-Standards verschlüsselt sein (mindestens TLS 1.2; TLS 1.3 bevorzugt)
- **Pseudonymisierung**: Wenn PII für Analysen, Testing, Forschung oder sekundäre Zwecke verwendet wird, **muss** Pseudonymisierung angewandt werden, um das Re-Identifizierungsrisiko zu reduzieren, sofern technisch durchführbar
- **Anonymisierung**: Wenn irreversible Anonymisierung angewandt wird, ist das Ergebnis keine dem GDPR unterliegende PII mehr — aber die Anonymisierung muss robust sein: Der DSB muss mittels einer dokumentierten Methodik bestätigen, dass eine Re-Identifizierung durch keine vernünftigerweise wahrscheinlichen Mittel möglich ist, unter Berücksichtigung der Risiken der Herausstellung (Isolierung einer Person in einem Datensatz), Verknüpfbarkeit (Verknüpfung von Datensätzen über Datasets hinweg zur Personenidentifizierung) und Inferenz (Ableitung von Attributen über eine Person aus verbleibenden Daten). Eine Anonymisierung, die diese Beurteilung nicht besteht, ist als Pseudonymisierung zu behandeln, und die zugrundeliegenden Daten bleiben weiterhin PII

### Schlüsselmanagement für PII-Verschlüsselung

- Kryptografische Schlüssel zum Schutz von PII **müssen** getrennt von der PII, die sie schützen, verwaltet werden
- Schlüsselzugang **muss** auf autorisiertes Personal mit dokumentiertem operativen Bedarf beschränkt sein
- Schlüsselrotation **muss** in den in PRIV-IMP-A.3.23-31-TG definierten Intervallen erfolgen
- Schlüsselkompromittierung oder -verlust bei PII-schützenden Schlüsseln **muss** als PII-Sicherheitsvorfall gemäss PRIV-POL-A.3.11-12 behandelt werden

Vollständige kryptografische Standards sind in ISMS-POL-A.8.24 definiert; dieser Abschnitt legt die PII-spezifischen Anforderungen fest, die innerhalb dieses Rahmenwerks gelten.

---

## A.3.27 — Sicherer Entwicklungslebenszyklus für PII-Systeme

[Organisation] **muss** Regeln für die sichere Entwicklung von Software und Systemen im Zusammenhang mit der PII-Verarbeitung festlegen und anwenden.

### PII in der sicheren Entwicklung

Die Regeln für die sichere Entwicklung von Systemen mit PII-Verarbeitung **müssen** folgende Aspekte umfassen:

- **Privacy by Design**: Datenschutz- und PII-Schutzanforderungen **müssen** von der frühesten Gestaltungsphase jedes Systems für die PII-Verarbeitung berücksichtigt werden; nachträgliches Einbauen von Datenschutzkontrollen ist kein akzeptabler Ansatz
- **Privacy by Default**: Systemstandards **müssen** PII-Sammlung und -verarbeitung minimieren; die datenschutzfreundlichsten Einstellungen **müssen** der Standard sein und keine individuelle Konfiguration durch Endbenutzer erfordern
- **PII-Datenminimerung im Design**: Systeme **müssen** so gestaltet sein, dass nur die für den angegebenen Zweck minimal notwendige PII gesammelt und verarbeitet wird; überschüssige Felderfassung **muss** während der Designüberprüfung identifiziert und entfernt werden
- **Trennung von PII-Anliegen**: Wo technisch machbar, **muss** PII in der Systemgestaltung von Nicht-PII-Daten isoliert sein (separate Datenbanken, separate Verarbeitungspfade)

### GDPR Art. 25-Compliance

Systeme mit PII-Verarbeitung **müssen** vor der Produktionsbereitstellung als Privacy-by-Design-konform dokumentiert sein. Der DPIA-Prozess (PRIV-POL-A.1.2.6-9) **muss** für Hochrisiko-Verarbeitungssysteme während der Entwurfsphase ausgelöst werden, nicht nach der Bereitstellung.

---

## A.3.28 — Anwendungssicherheitsanforderungen für PII

[Organisation] **muss** Informationssicherheitsanforderungen im Zusammenhang mit der PII-Verarbeitung bei der Entwicklung oder Beschaffung von Anwendungen identifizieren, spezifizieren und genehmigen.

### PII-Sicherheitsanforderungen in Entwicklung und Beschaffung

Für jede Anwendung, die PII verarbeitet (ob intern entwickelt oder beschafft):

- PII-Sicherheitsanforderungen **müssen** vor Entwicklungsbeginn oder vor der Beschaffungsentscheidung dokumentiert sein
- Anforderungen **müssen** mindestens folgende Aspekte abdecken: Authentifizierung, Zugriffskontrolle, Verschlüsselung im Ruhezustand und im Transit, Protokollierung und Datenspeicherung/-löschung
- Anforderungen **müssen** vom DSB (für Datenschutzanforderungen) und ISB (für Sicherheitsanforderungen) vor Beginn genehmigt werden
- Bei beschafften Anwendungen: Sicherheitsanforderungen **müssen** in Beschaffungsspezifikationen aufgenommen werden; die Sicherheitsbewertung des Anbieters **muss** PII-Verarbeitungskontrollen abdecken

### Überprüfung der Sicherheitsanforderungen

PII-Anwendungssicherheitsanforderungen **müssen** überprüft werden:

- Bei jedem grösseren Versions-Release oder wesentlicher Änderung
- Bei Änderungen der anwendbaren regulatorischen Anforderungen
- Nach einem Sicherheitsvorfall mit der Anwendung

---

## A.3.29 — Sichere Architektur und Engineeringprinzipien für PII

[Organisation] **muss** Prinzipien für die Entwicklung sicherer Systeme im Zusammenhang mit der PII-Verarbeitung festlegen, dokumentieren, aufrechterhalten und anwenden.

### PII-Architekturprinzipien

Folgende Prinzipien **müssen** auf Systemarchitektur mit PII-Bezug angewandt werden:

1. **Minimale Exposition**: PII soll durch die minimal notwendige Anzahl von Systemkomponenten fliessen; unnötige Exposition von PII gegenüber Zwischensystemen oder Protokollen soll vermieden werden
2. **Minimalrecht in der Architektur**: Systemkomponenten sollen nur auf die PII zugreifen, die sie benötigen; Service-zu-Service-Zugriff auf PII soll eingegrenzt und authentifiziert sein
3. **Datentrennung**: Wo machbar, soll PII aus verschiedenen Verarbeitungszwecken oder verschiedener betroffener Personen logisch getrennt sein
4. **Prüfbarkeit**: PII-verarbeitende Systeme sollen so gestaltet sein, dass sie die von A.3.25 geforderten Protokolle ohne zusätzliche Instrumentierung erzeugen
5. **Wiederherstellbarkeit**: Die Architektur soll die Sicherungs- und Wiederherstellungsanforderungen von A.3.24 für PII unterstützen
6. **Anonymisierungs- und Pseudonymisierungspfade**: Die Architektur soll technische Mechanismen umfassen, um PII für sekundäre Verwendungszwecke zu pseudonymisieren oder zu anonymisieren, ohne Zugang zu primären PII-Speichern zu benötigen

Diese Prinzipien erweitern und spezialisieren die ISMS-Secure-Engineering-Prinzipien in ISMS-POL-A.8.27.

---

## A.3.30 — Ausgelagerte Entwicklung von PII-Verarbeitungssystemen

[Organisation] **muss** Aktivitäten im Zusammenhang mit der ausgelagerten Entwicklung von PII-Verarbeitungssystemen leiten, überwachen und überprüfen.

### Anforderungen für ausgelagerte Entwicklung

Wenn die Entwicklung von Systemen für die PII-Verarbeitung an Dritte ausgelagert wird:

- Der Entwicklungspartner **muss** gemäss PRIV-POL-A.3.8-10 als PII-Auftragsverarbeiter oder PII-benachbarter Lieferant behandelt werden (Lieferantenkategorisierung)
- Eine Vereinbarung über PII-Sicherheitspflichten **muss** vorliegen, bevor Entwicklungszugang zu PII (oder PII-fähigen Systemen) gewährt wird
- PII-Sicherheitsanforderungen (A.3.28) **müssen** vor Entwicklungsbeginn kommuniziert und vereinbart werden
- Sicherheits- und Datenschutzanforderungen **müssen** in Abnahmetests vor der Bereitstellung einbezogen werden
- [Organisation] **muss** das Recht behalten, Entwicklungsartefakte (Code, Designdokumente) auf PII-Compliance zu überprüfen
- Der Entwicklungspartner **muss** einen während der Entwicklung entdeckten PII-Vorfall sofort melden

### PII in ausgelagerten Entwicklungsumgebungen

- Entwicklungspartner **dürfen** keine echte PII in Entwicklungs- oder Testumgebungen ohne ausdrückliche DSB-Genehmigung verwenden
- Wenn echte PII verwendet werden muss (z.B. für reproduzierbare Fehleruntersuchungen), **muss** die Genehmigung zeitlich begrenzt und dokumentiert sein; die PII **muss** nach Abschluss der spezifischen Untersuchung gelöscht werden

---

## A.3.31 — Testinformationen im Zusammenhang mit PII

[Organisation] **muss** im Zusammenhang mit der PII-Verarbeitung verwendete Testinformationen angemessen auswählen, schützen und verwalten.

### Verbot echter PII in Testumgebungen

Echte PII **darf** in Testumgebungen standardmässig nicht verwendet werden. Testumgebungen **müssen** verwenden:

- Synthetisch erzeugte Daten, die PII in ihrer Struktur ähneln, aber keine echten Personendaten enthalten, ODER
- Irreversibel anonymisierte Daten aus echten PII-Datensätzen (DSB-Bestätigung der Anonymisierung erforderlich)

### Ausnahme: Verwendung echter PII in Tests

Wenn die Verwendung echter PII in Tests operativ notwendig ist (z.B. zur Reproduktion eines spezifischen Datenfehlers), **müssen** folgende Bedingungen gelten:

- Schriftliche Genehmigung des DSB vor dem Kopieren echter PII in die Testumgebung
- Umfang auf die minimal notwendige PII für die minimal erforderliche Dauer begrenzt
- Testumgebung **muss** dieselben Zugriffskontrollen und Verschlüsselung wie die Produktionsumgebung anwenden
- Echte PII **muss** unmittelbar nach Abschluss des spezifischen Tests aus der Testumgebung gelöscht werden; Löschung muss bestätigt und dokumentiert werden
- Alle Zugriffe auf echte PII in der Testumgebung **müssen** protokolliert werden

### Testdatenmanagement

Synthetische und anonymisierte Testdatensätze, die für Tests von PII-Verarbeitungssystemen verwendet werden, **müssen**:

- Im Testdateninventar dokumentiert sein (Eigentümer, Format, Aktualität, Zweck)
- Gegen versehentlichen Ersatz durch echte PII geschützt sein
- Periodisch überprüft werden, um sicherzustellen, dass sie für Testzwecke repräsentativ bleiben

---

# Rollen und Verantwortlichkeiten

## Verantwortungsmatrix

| Rolle | Verantwortlichkeiten für A.3.23–A.3.31 |
|-------|----------------------------------------|
| **Datenschutzbeauftragter (DSB)** | Genehmigt PII-Sicherheitsanforderungen für neue Systeme (A.3.28); bestätigt Anonymisierungsentscheidungen (A.3.26); genehmigt DPIA für neue PII-Verarbeitungssysteme (A.3.27); genehmigt Verwendung echter PII in Tests (A.3.31); überprüft PII-Compliance ausgelagerter Entwicklung (A.3.30) |
| **ISB** | Definiert Authentifizierungsstandards (A.3.23); setzt Sicherungsstandards (A.3.24); verwaltet Protokollierungsinfrastruktur (A.3.25); pflegt kryptografische Standards (A.3.26); ist Eigentümer des Secure-Development-Rahmenwerks (A.3.27–A.3.30) |
| **IT-Sicherheitsteam** | Implementiert Authentifizierungs-, Sicherungs-, Protokollierungs- und Verschlüsselungskontrollen; überwacht Protokolle auf PII-Zugriffsanomalien; verwaltet Schlüsselmanagementinfrastruktur |
| **Entwicklungs-/DevOps-Teams** | Wendet Privacy-by-Design- und Secure-Development-Regeln an; implementiert PII-Sicherheitsanforderungen im Code; verwendet nur genehmigte Testdaten (keine echte PII ohne DSB-Genehmigung) |
| **IT-Architektur** | Pflegt Secure-Architecture-Prinzipien für PII; überprüft neue Systemdesigns auf PII-Architektur-Compliance |
| **Beschaffung / Legal** | Stellt sicher, dass Verträge für ausgelagerte Entwicklung PII-Sicherheitspflichten enthalten |

---

# Nachweisanforderungen

Folgende Nachweise belegen den Betrieb dieser Richtlinie:

| Nachweis | Beschreibung | Aufbewahrung |
|---------|-------------|--------------|
| PII-System-Authentifizierungskonfiguration | MFA-Durchsetzungsaufzeichnungen und Zugriffseinschränkungskonfigurationen für PII-Systeme | Aktuell + 3 Jahre |
| Sicherungstestaufzeichnungen | Jährliche Wiederherstellungstestergebnisse für PII-Sicherungen | 3 Jahre |
| PII-Zugriffsprotokolle | Aktivitätsprotokolle für PII-Datenspeicher- und Systemzugriff | Mindestens 12 Monate; länger gemäss regulatorischen oder vertraglichen Anforderungen |
| Kryptografiestandards-Dokumentation | Genehmigte Algorithmen, Schlüsselverwaltungsverfahren, Schlüsselrotationsaufzeichnungen | Aktuell + 3 Jahre |
| Privacy-by-Design-Bewertungen | Designüberprüfungsaufzeichnungen, die PbD-Compliance für PII-Verarbeitungssysteme bestätigen | Betriebsdauer des Systems + 3 Jahre |
| PII-Sicherheitsanforderungsdokumente | Genehmigte Sicherheitsanforderungen für entwickelte oder beschaffte PII-Anwendungen | Betriebsdauer der Anwendung + 3 Jahre |
| Genehmigungsaufzeichnungen für echte PII-Tests | DSB-Genehmigungen für Verwendung echter PII in Testumgebungen mit Löschbestätigungen | 3 Jahre |
| Vereinbarungen über ausgelagerte Entwicklung mit PII | Vereinbarungen mit Entwicklungspartnern über PII-Sicherheitspflichten | Vereinbarungsdauer + 3 Jahre |

---

# Prüfungshinweise

Prüfer, die die Compliance mit A.3.23–A.3.31 verifizieren, sollten Folgendes vorfinden:

**Für A.3.23 (Authentifizierung)**: MFA-Konfigurationsnachweis für VERTRAULICHE/EINGESCHRÄNKTE PII-Systeme; Zugriffseinschränkungsausrichtung mit definierten Zugriffsrechten; Protokollierung von Fehlversuchen.

**Für A.3.24 (Datensicherung)**: Sicherungsrichtlinie für PII; Verschlüsselung von Sicherungen; jährliche Wiederherstellungstestaufzeichnungen mit PII-Integritätsverifizierung.

**Für A.3.25 (Protokollierung)**: Definierte PII-Ereignisse werden protokolliert; manipulationssicherer Protokollspeicher; Zugriffskontrollen auf Protokolle; Nachweis der Protokollanalyse für Anomalieerkennung.

**Für A.3.26 (Kryptografie)**: Verschlüsselung im Ruhezustand für VERTRAULICHE/EINGESCHRÄNKTE PII; TLS-Durchsetzung für PII im Transit; Schlüsselverwaltungsdokumentation; Nachweis der Pseudonymisierungsverwendung.

**Für A.3.27 (Sichere Entwicklung)**: Privacy-by-Design-Nachweis in Systemdesignaufzeichnungen; DPIA-Auslösung für Hochrisikosysteme; Datenminimerungsüberprüfung im Design.

**Für A.3.28 (Anwendungssicherheitsanforderungen)**: Dokumentierte und von DSB/ISB genehmigte PII-Sicherheitsanforderungen für Anwendungen im Anwendungsbereich; Sicherheitsanforderungen in Beschaffungsspezifikationen.

**Für A.3.29 (Architekturprinzipien)**: Dokumentierte PII-Architekturprinzipien; Designüberprüfungsnachweis für die Anwendung der Prinzipien auf neue Systeme.

**Für A.3.30 (Ausgelagerte Entwicklung)**: Vereinbarungen für ausgelagerte Entwicklung mit PII-Sicherheitsklauseln; keine echte PII in ausgelagerten Entwicklungsumgebungen ohne DSB-Genehmigung.

**Für A.3.31 (Testinformationen)**: Standardmässige Verwendung synthetischer oder anonymisierter Testdaten; DSB-Genehmigungsaufzeichnungen für Verwendung echter PII in Tests; Löschbestätigungen für echte PII nach Tests.

---

<!-- QA_VERIFIED: 2026-03-29 -->

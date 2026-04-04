<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.31-DE:operational:OP-POL:a.8.31 -->
**ISMS-OP-POL-A.8.31 — Trennung von Entwicklungs-, Test- und Produktionsumgebungen**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Trennung von Entwicklungs-, Test- und Produktionsumgebungen |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.31 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstfassung der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.8.31 — Separation of development, test and production environments
- ISO/IEC 27002:2022 Section 8.31 — Implementation guidance for environment separation
- NIST SP 800-53 Rev 5 — CM-4 (Impact Analyses), CM-7 (Least Functionality), SA-11 (Developer Testing), SC-32 (System Partitioning)
- CIS Controls v8 — Safeguard 16.1–16.14 (Application Software Security)

**Verwandte Annex-A-Controls**:

| Control | Bezug zur Umgebungstrennung |
|---------|-----------------------------|
| A.5.15–16–18 Identitäts- und Zugriffsmanagement | Grundlegender IAM-Rahmen; rollenbasierter Zugriff je Umgebungsstufe |
| A.5.34 Datenschutz und personenbezogene Daten | Testdaten mit Personendaten erfordern Anonymisierung oder Ersatz durch synthetische Daten |
| A.8.2–3–5 Authentifizierung und privilegierter Zugriff | MFA für Produktionszugriff; Privileged-Access-Management für Break-Glass |
| A.8.4 Zugriff auf Quellcode | Repository-Zugriffskontrollen und Branch-Schutz fliessen in Promotion-Workflows ein |
| A.8.9 Konfigurationsmanagement | Umgebungsspezifische Konfigurations-Baselines und Drift-Erkennung |
| A.8.11 Datenmaskierung | Techniken zum Schutz von Daten in Nicht-Produktionsumgebungen |
| A.8.15 Protokollierung | Audit-Protokollierung für Umgebungszugriffe, Promotionen und Break-Glass-Ereignisse |
| A.8.25–26–29 Sicherer Entwicklungslebenszyklus | SDLC-Integration; Sicherheitsprüfungs-Gates zwischen Umgebungen |
| A.8.32 Change Management | CAB-Genehmigung für Produktionsdeployments |
| A.8.33 Testinformationen | Schutz und Verwaltung von Testdaten in allen Umgebungen |

**Verwandte interne Richtlinien**:

- Richtlinie für Identitäts- und Zugriffsmanagement
- Richtlinie für den sicheren Entwicklungslebenszyklus
- Change-Management-Richtlinie
- Protokollierungsrichtlinie
- Richtlinie zur Datenklassifikation und -behandlung
- Datenschutz- und Personendaten-Richtlinie
- Incident-Response-Richtlinie

---

# Richtlinie zur Trennung von Entwicklungs-, Test- und Produktionsumgebungen

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass Entwicklungs-, Test- und Produktionsumgebungen getrennt und gesichert werden, um das Risiko unberechtigter Zugriffe auf oder Änderungen in der Produktionsumgebung zu reduzieren. Die Umgebungstrennung schützt den Geschäftsbetrieb vor Entwicklungs- und Testaktivitäten, die Fehler, Schwachstellen oder unberechtigte Änderungen an Live-Systemen und -Daten einbringen könnten.

Diese Richtlinie unterstützt den schweizerischen nDSG (revDSG) Art. 8, indem sie technische und organisatorische Massnahmen entsprechend dem Risiko zum Schutz personenbezogener Daten in Produktionsumgebungen implementiert und die Verwendung produktiver Personendaten in Entwicklungs- und Testumgebungen ohne gleichwertige Schutzmassnahmen untersagt. Soweit die Organisation Daten von Personen in der EU/EWR verarbeitet, gelten ausserdem die Anforderungen der DSGVO Art. 32. Die Umgebungstrennung ist eine wesentliche technische Massnahme, um nachzuweisen, dass Systeme, die Personendaten verarbeiten, angemessenen Zugriffsbeschränkungen und Datenverarbeitungskontrollen unterliegen.

## Geltungsbereich

Alle Informationssysteme, Applikationen und Infrastrukturen, die von der Organisation betrieben, verwaltet oder kontrolliert werden und als im Geltungsbereich der ISO 27001-Scope-Erklärung befindlich eingestuft sind. Dies umfasst:

- Alle Umgebungsstufen: Entwicklung, Test/QA, Staging/Vorproduktion und Produktion.
- Alle Hosting-Modelle: On-Premises, Cloud ([Cloud Provider] — z.B. AWS, Azure, GCP oder Äquivalent), Hybrid und containerbasierte Infrastruktur ([Container-Plattform] — z.B. Kubernetes, Docker Swarm oder Äquivalent).
- Alle CI/CD-Pipelines ([CI/CD-Plattform] — z.B. GitHub Actions, GitLab CI, Jenkins, Azure DevOps oder Äquivalent), die Änderungen zwischen Umgebungen befördern.
- Durch Dritte verwaltete Systeme, die Organisationsdaten verarbeiten, bei denen die Organisation die Verantwortung für das Umgebungsmanagement behält.

Alle Mitarbeitenden, Auftragnehmer und Drittbenutzer mit Zugriff auf eine beliebige Umgebung.

**Nicht im Geltungsbereich**: Isolierte Einzelnutzer-Forschungsumgebungen, die nicht mit dem Organisationsnetzwerk verbunden sind; temporäre Proof-of-Concept-Systeme ohne Organisations- oder Personendaten; Anbieter-Demonstrationssysteme, die vollständig durch Anbieter verwaltet werden. Sobald Forschungs- oder Proof-of-Concept-Systeme in den Organisationsbetrieb übergehen, müssen sie diese Richtlinie einhalten.

## Grundsatz

Entwicklungs-, Test- und Produktionsumgebungen sind zu trennen, um die Integrität, Verfügbarkeit und Vertraulichkeit von Produktionssystemen und -daten zu schützen. Änderungen müssen über definierte Promotion-Pfade mit angemessener Überprüfung und Genehmigung auf jeder Stufe laufen. Keine einzelne Person darf in der Lage sein, Änderungen sowohl an der Entwicklung als auch an der Produktion ohne vorherige Überprüfung und Genehmigung vorzunehmen. Der Grad der Trennung muss dem Risiko für den Geschäftsbetrieb und der Sensitivität der verarbeiteten Daten entsprechen.

Die Organisation administriert den Umgebungszugriff zentral über rollenbasierte Zugriffskontrollen. Der standardmässige Zugriff auf Produktionsumgebungen ist «kein Zugriff» — für jede Zugriffsstufe ist eine explizite Erteilung erforderlich. Entwickler dürfen keinen dauerhaften Zugriff auf Produktionsinfrastruktur haben.

---

## Umgebungsdefinitionen

Die Organisation pflegt mindestens die folgenden Umgebungsstufen. Jede Stufe muss einen definierten Zweck, dedizierte Infrastrukturressourcen, dokumentierte Datenverarbeitungseinschränkungen und durchgesetzte Zugriffskontrollen haben.

**Umgebungsstufen**:

| Umgebung | Zweck | Erlaubte Daten | Zugriff |
|----------|-------|----------------|---------|
| **Entwicklung** | Aktive Code-Entwicklung, Experimente, Integration | Ausschliesslich synthetische Daten; keine Produktionsdaten | Entwickler (vollständig); QA (lesend); Operations (nach Bedarf) |
| **Test / QA** | Qualitätssicherung, Integrationstests, User-Acceptance-Testing | Synthetische oder anonymisierte Daten (DSB-genehmigt) | QA-Team (vollständig); Entwickler (eingeschränkt); Operations (nach Bedarf) |
| **Staging / Vorproduktion** | Abschlussvalidierung vor Produktionsrelease; spiegelt Produktionskonfiguration | Synthetische oder anonymisierte Daten; Produktionskonfiguration (keine Daten) | Operations (vollständig); QA (lesend); Entwickler (nur lesend/Monitoring) |
| **Produktion** | Live-Geschäftsbetrieb für echte Benutzer mit echten Geschäftsdaten | Produktionsdaten (echte Geschäfts- und Personendaten) | Operations (vollständig); Entwickler (kein dauerhafter Zugriff; nur Break-Glass) |
| **Sandbox** (optional) | Isolierte Experimente, Technologiebewertung, Proof-of-Concept | Ausschliesslich synthetische Daten; keine Netzwerkverbindung zu anderen Umgebungen | Entwickler (vollständig); keine Verbindung zu Produktionsnetzwerken |

Umgebungsnamen und visuelle Labels müssen den Umgebungstyp klar erkennbar machen (z.B. farbcodierte Banner, Hostname-Präfixe, Console-Labels), um versehentliche Operationen in der falschen Umgebung zu verhindern.

---

## Netzwerktrennung

Umgebungen sind durch Netzwerksegmentierung zu isolieren, um unbeabsichtigte umgebungsübergreifende Datenflüsse und Zugriffe zu verhindern.

**Anforderungen an die Netzwerktrennung**:

| Anforderung | Standard |
|-------------|----------|
| Netzwerkisolation | Jede Umgebung in einem eigenen Netzwerksegment, VLAN, VPC oder Äquivalent |
| Standard-Traffic-Regel | Deny-all zwischen Umgebungen; nur kontrollierte Promotion-Pfade erlaubt |
| Produktions-zu-Entwicklungs-Konnektivität | Verboten — kein direkter Netzwerkpfad zwischen Produktion und Entwicklung |
| Firewall-Regeln | Dokumentiert, vierteljährlich überprüft, auf minimal erforderliche Datenflüsse beschränkt |
| DNS-Trennung | Separate DNS-Zonen oder Namespaces pro Umgebung, um umgebungsübergreifende Auflösung zu verhindern |

**Cloud-Umgebungstrennung**:

Wo die Organisation Cloud-Infrastruktur nutzt, wird die Umgebungstrennung über das Konto- oder Abonnementgrenzenmodell des Cloud-Anbieters implementiert:

| Cloud-Anbieter | Trennungsmechanismus |
|----------------|---------------------|
| AWS | Separate AWS-Konten pro Umgebung innerhalb einer AWS-Organisation |
| Azure | Separate Abonnements pro Umgebung innerhalb einer Management Group |
| GCP | Separate Projekte pro Umgebung innerhalb einer Organisation |
| Multi-Cloud | Konsistentes Trennungsmodell pro Anbieter dokumentiert |

**Container- und Kubernetes-Trennung**:

Wo die Organisation Container-Orchestrierungsplattformen nutzt, werden Umgebungen getrennt durch:

- Separate Cluster pro Umgebung (bevorzugt für Produktionsisolation).
- Namespace-Trennung mit durchgesetzten Netzwerkrichtlinien für Nicht-Produktionsumgebungen.
- Produktions-Workloads dürfen keinen Cluster mit Entwicklungs- oder Test-Workloads teilen.
- Container-Image-Registries sind pro Umgebung zu trennen oder mit Zugriffskontrolle zu versehen.

**Sicherheit für Produktions-Container**:

- Produktions-Container dürfen keine Host-Dateisysteme einbinden, ausser für explizit genehmigte Anwendungsfälle.
- Produktions-Container laufen als Nicht-Root-Benutzer.
- Produktions-Container-Images sind vor dem Deployment zu signieren und zu verifizieren.
- Container-Registries sind pro Umgebung zu trennen (z.B. `prod.registry.example.com` vs. `dev.registry.example.com`).

**Kubernetes-Produktions-Hardening**:

- Produktionscluster nutzen separate Control Planes und Node Pools.
- Pod Security Standards (PSS) werden auf Stufe «Restricted» für Produktion durchgesetzt.
- Netzwerkrichtlinien verweigern standardmässig allen Verkehr mit expliziten Allow-Regeln.
- Service-Accounts sind auf minimal erforderliche Berechtigungen beschränkt.

---

## Zugangskontrolle pro Umgebung

Der Zugriff auf jede Umgebung folgt dem Prinzip der minimalen Rechtevergabe. Zugriffsrechte werden pro Rolle und Umgebungsstufe definiert.

**Zugangsmatrix**:

| Rolle | Entwicklung | Test / QA | Staging | Produktion |
|-------|-------------|-----------|---------|------------|
| **Entwickler** | Vollständig | Lesen + Deploy zu Test | Nur lesend | Kein dauerhafter Zugriff |
| **QA Engineer** | Lesen | Vollständig | Lesen + Tests ausführen | Kein Zugriff |
| **Operations / SRE** | Nach Bedarf | Nach Bedarf | Vollständig | Vollständig |
| **Datenbankadministrator** | Nach Bedarf | Nach Bedarf | Nach Bedarf | Vollständig (mit PAM) |
| **Security Team** | Lesen (Audit) | Lesen (Audit) | Lesen (Audit) | Lesen (Audit + Monitoring) |
| **Externer Auftragnehmer** | Auf Projekt beschränkt | Auf Projekt beschränkt | Kein Zugriff | Kein Zugriff |

**Produktionszugriffsbeschränkungen**:

- Entwickler dürfen keinen dauerhaften Zugriff auf Produktionsinfrastruktur, Datenbanken oder Applikationskonsolen haben.
- Jeder Produktionszugriff erfordert Multi-Faktor-Authentifizierung.
- Produktionszugriffssitzungen sind zu protokollieren, aufzuzeichnen und zu überwachen.
- Privilegierter Produktionszugriff muss über ein Privileged-Access-Management(PAM)-System verwaltet werden ([PAM-Tool] — z.B. CyberArk, HashiCorp Boundary, AWS SSM Session Manager oder Äquivalent).

**Notfallzugriff (Break-Glass)**:

Notfallzugriff für Entwickler auf die Produktion ist nur während erklärter Vorfälle zulässig, bei denen das Fachwissen von Entwicklern zur Lösung erforderlich ist. Break-Glass-Zugriff erfordert:

- Genehmigung durch den Incident Commander und ISB (oder Stellvertreter).
- Zeitlich begrenzt auf maximal 8 Stunden, verlängerbar mit erneuter Genehmigung.
- Auf den Umfang des erklärten Vorfalls beschränkt.
- Protokollierung mit: Vorfallskennung, anfragender Entwickler, genehmigende Instanz, Zugangsdauer, zugegriffene Systeme und durchgeführte Massnahmen.
- Auslösung einer obligatorischen Post-Incident-Review innerhalb von 7 Tagen nach Vorfallsabschluss.

Break-Glass-Aktivierungen werden monatlich durch den Information Security Manager überprüft und im vierteljährlichen ISB-Dashboard mit Trendanalyse berichtet.

**Zugriffsüberprüfungen**:

| Umgebung | Überprüfungshäufigkeit |
|----------|----------------------|
| Produktion | Vierteljährlich |
| Staging | Halbjährlich |
| Entwicklung / Test | Jährlich |

Der Zugriff ausgeschiedener Mitarbeitender ist noch am selben Geschäftstag in allen Umgebungen zu entziehen. Automatisches Deprovisioning über das Identitätsmanagementsystem wird bevorzugt.

---

## Datenverarbeitungsregeln

Produktionsdaten dürfen nicht in Entwicklungs- oder Testumgebungen verwendet werden. Diese Anforderung schützt geschäftskritische Daten vor Exposition in weniger kontrollierten Umgebungen und unterstützt die nDSG-Compliance für Personendaten.

**Verbot von Produktionsdaten**:

- Produktionsdaten dürfen nicht kopiert, exportiert, wiederhergestellt oder in Entwicklungs-, Test- oder Staging-Umgebungen repliziert werden.
- Produktions-Datenbank-Backups dürfen nicht in Nicht-Produktionsumgebungen wiederhergestellt werden.
- Produktions-Zugangsdaten, API-Keys, Verbindungszeichenfolgen und Secrets dürfen nicht in Nicht-Produktionsumgebungen verwendet werden.
- Log-Dateien mit produktiven Personendaten dürfen ohne Anonymisierung nicht in Nicht-Produktionsumgebungen übertragen werden.

**Genehmigte Datenquellen für Nicht-Produktionsumgebungen**:

| Datenquelle | Genehmigung erforderlich | Einschränkungen |
|-------------|--------------------------|-----------------|
| **Synthetische Daten** (generiert, nicht aus Produktion abgeleitet) | Keine zusätzliche Genehmigung | Bevorzugte Methode; strukturell repräsentativ, aber vollständig künstlich |
| **Anonymisierte Daten** (unwiderruflich de-identifiziert aus Produktion) | Genehmigung des Datenschutzbeauftragten | Anonymisierung muss unwiderruflich sein; auf Re-Identifikationsrisiko validiert; innerhalb von 30 Tagen nach Projektabschluss gelöscht |
| **Pseudonymisierte Daten** (widerruflich de-identifiziert) | ISB- und DSB-Genehmigung; nach nDSG als Personendaten zu behandeln | Nur akzeptabel, wenn Anonymisierung oder synthetische Daten technisch nicht machbar sind; gleichwertige Sicherheitskontrollen erforderlich |
| **Teilmenge der Produktionsstruktur** (nur Schema, keine Daten) | Genehmigung des Development Managers | Datenbankschemas, API-Verträge, Konfigurationsvorlagen ohne Datenwerte |

Nach dem schweizerischen nDSG (revDSG) bleiben pseudonymisierte Daten für jede Partei, die den Pseudonymisierungsschlüssel besitzt oder darauf zugreifen kann, Personendaten. Vollständig anonymisierte Daten — bei denen eine Re-Identifikation mit vertretbaren Mitteln nicht möglich ist — fallen nicht unter das nDSG.

**Durchsetzung der Datenklassifikation**:

- Die Klassifikationen «Vertraulich» und «Eingeschränkt» sind in Entwicklungs- und Testumgebungen verboten.
- Automatisiertes Scanning ist zu implementieren, um verbotene Produktionsdatenmuster (z.B. echte Namen, nationale Kennzeichen, Finanzkontennummern) in Nicht-Produktionsumgebungen zu erkennen. Das Scanning umfasst Datenbanken, Dateisysteme, Log-Dateien und Container-Images.
- Verstösse sind innerhalb von 7 Tagen nach Erkennung zu beheben und dem Information Security Manager zu melden.

---

## Testdatenmanagement

Testdaten sind als kontrolliertes Asset während des gesamten Software-Entwicklungslebenszyklus zu verwalten.

**Testdatenprinzipien**:

- Synthetische Daten sind der Standard- und bevorzugte Ansatz für alle Testaktivitäten.
- Testdaten müssen strukturell repräsentativ für Produktionsdaten sein (gleiches Schema, Datentypen, Beziehungen und Volumencharakteristiken) ohne echte persönliche oder Geschäftsdaten zu enthalten.
- Die Testdatengenerierung ist wo praktikabel zu automatisieren mit [Testdaten-Tool] (z.B. Faker, Mockaroo, Tonic.ai, Delphix oder Äquivalent).
- Testdaten sind zu versionieren und reproduzierbar zu halten, um Regressionstests zu unterstützen.
- Testdaten sind innerhalb von 30 Tagen nach Projektabschluss oder Testzyklusende aus Nicht-Produktionsumgebungen zu löschen.

**Anonymisierungsvalidierung**:

Wenn anonymisierte Produktionsdaten für die Verwendung in Nicht-Produktionsumgebungen genehmigt sind, ist der Anonymisierungsprozess vor jeder Verwendung zu validieren:

1. Der Datenschutzbeauftragte verifiziert, dass direkte Identifikatoren entfernt oder ersetzt wurden.
2. Quasi-Identifikator-Kombinationen werden auf Re-Identifikationsrisiko geprüft.
3. Validierungsergebnisse sind zu dokumentieren und für Auditzwecke aufzubewahren.
4. Fehlgeschlagene Validierung führt zur Ablehnung und Korrektur, bevor die Daten verwendet werden können.

**Karteninhaberdaten**: Karteninhaberdaten (PAN, CVV, Track-Daten) dürfen unabhängig vom Anonymisierungsstatus niemals in Entwicklungs- oder Testumgebungen verwendet werden. Stattdessen sind synthetische Kartennummern aus Testbereichen zu verwenden.

---

## Code-Promotion-Prozess

Änderungen müssen einem definierten Promotion-Pfad von der Entwicklung zur Produktion folgen. Direkte Deployments in die Produktion sind ausser bei genehmigten Notfallkorrekturen verboten.

**Standard-Promotion-Pfad**:

```
Entwicklung → Test / QA → Staging → Produktion
```

Jeder Promotion-Schritt umfasst definierte Qualitäts- und Sicherheitsgates.

**Anforderungen an Promotion-Gates**:

| Gate | Von → Nach | Anforderungen |
|------|------------|---------------|
| **Gate 1** | Entwicklung → Test | Code-Review abgeschlossen (mindestens 1 Reviewer, nicht der Autor); automatisierte Unit-Tests bestanden; Static-Analysis-Scan bestanden; keine kritischen oder hohen Schwachstellen |
| **Gate 2** | Test → Staging | Integrationstests bestanden; QA-Freigabe; Sicherheitstests abgeschlossen (SAST, DAST wo anwendbar); Performance-Tests für kritische Systeme bestanden |
| **Gate 3** | Staging → Produktion | Change-Advisory-Board-Genehmigung (gemäss A.8.32); Rollback-Plan dokumentiert und getestet; Produktions-Backup verifiziert; Deployment-Runbook überprüft; Genehmigung des Systemeigentümers |

**Funktionstrennung bei der Promotion**:

- Der Entwickler, der den Code schreibt, darf nicht dieselbe Person sein, die dessen Promotion in die Produktion genehmigt.
- Die Person, die Code zu Staging befördert, darf — soweit die Teamgrösse es erlaubt — nicht dieselbe Person sein, die ihn zur Produktion befördert.
- CI/CD-Pipeline-Zugangsdaten für Produktions-Deployments sind auf das Operations-Team beschränkt.

**CI/CD-Pipeline-Sicherheit**:

- Pipeline-Definitionen sind versionskontrolliert und unterliegen dem Code-Review.
- Pipeline-Zugangsdaten und Secrets sind im Secret-Store der Pipeline-Plattform zu speichern — nicht fest kodiert in Pipeline-Definitionen.
- Jede Umgebung hat dedizierte Pipeline-Zugangsdaten mit minimal erforderlichen Berechtigungen.
- Pipeline-Ausführungsprotokolle sind für Auditzwecke aufzubewahren (mindestens 1 Jahr).
- Artefakte werden einmal erstellt und unveränderlich durch Umgebungen befördert — nicht pro Umgebung neu erstellt.

**Notfall-Deployments**:

Notfallkorrekturen dürfen unter folgenden Bedingungen den Standard-Promotion-Pfad umgehen:

- Ein erklärter Vorfall oder eine kritische Sicherheitsschwachstelle, die eine sofortige Behebung erfordert.
- Genehmigung durch den Incident Commander (oder On-Call-Manager) und ISB (oder Stellvertreter).
- Post-Implementation-Review innerhalb von 48 Stunden, einschliesslich retrospektiver Tests in allen übersprungenen Umgebungen.
- Dokumentation des Notfalls im Change-Management-System mit Begründung für das Umgehen der Gates.

**Rollback-Fähigkeit**:

- Frühere Versionen sind für Rollbacks aufzubewahren.
- Rollback-Verfahren sind zu dokumentieren und mindestens vierteljährlich zu testen.
- Das Operations-Team ist berechtigt, Rollbacks während Vorfällen ohne zusätzliche Genehmigung durchzuführen.
- Produktionsumgebungen sind vor jedem Deployment zu sichern, um Rollbacks zu ermöglichen.
- Testdaten und Entwicklungsartefakte sind vor der Promotion in die Produktion zu entfernen.

---

## Konfigurationstrennung

Umgebungskonfigurationen sind zu verwalten, um Zugangsdatenlecks, umgebungsübergreifende Kontamination und Konfigurationsdrift zu verhindern.

**Anforderungen an die Konfigurationstrennung**:

| Anforderung | Standard |
|-------------|----------|
| Zugangsdaten und Secrets | Einzigartig pro Umgebung; in einem Secrets-Manager gespeichert ([Secrets Manager] — z.B. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault oder Äquivalent) |
| Datenbankverbindungszeichenfolgen | Umgebungsspezifisch; niemals umgebungsübergreifend geteilt |
| API-Endpoints | Umgebungsspezifische URLs; keine fest kodierten Produktions-Endpoints in Nicht-Produktionscode |
| Feature-Flags | Umgebungsspezifische Konfiguration; Produktions-Flags separat von Entwicklung verwaltet |
| Infrastructure as Code | Umgebungskonfigurationen in Versionskontrolle; Änderungen folgen demselben Promotion-Pfad wie Applikationscode |

**Konfigurationsparität**:

- Staging-Umgebungen sollen die Produktionskonfiguration so genau wie möglich spiegeln (gleiche Softwareversionen, gleiche Infrastrukturgrösse im Rahmen von Budgetbeschränkungen, gleiche Sicherheitskontrollen).
- Konfigurationsdrift zwischen Staging und Produktion ist zu erkennen und zu melden. Drift-Erkennung ist mindestens wöchentlich durchzuführen.
- Unterschiede zwischen Staging und Produktion sind zu dokumentieren, zu begründen und vom IT-Operations-Manager zu genehmigen.

**Dokumentierte Staging-Produktions-Unterschiede**:

Die folgende Tabelle ist vom IT-Operations-Manager zu pflegen und vierteljährlich zu überprüfen. Nicht genehmigte Unterschiede, die durch Drift-Erkennung festgestellt werden, sind zu untersuchen und zu beheben.

| Konfigurationselement | Staging | Produktion | Begründung |
|-----------------------|---------|------------|------------|
| Instanzgrösse | Reduziert (Kostenoptimierung) | Vollständige Produktionsspezifikation | Kostenoptimierung; Staging validiert Funktionalität, nicht Last |
| Replikat-Anzahl | Minimal (1-2) | Gemäss Verfügbarkeitsanforderungen (3+) | Kostenoptimierung; Staging erfordert keine Hochverfügbarkeit |
| Backup-Aufbewahrung | 7 Tage | Gemäss Datenaufbewahrungsrichtlinie (90+ Tage) | Compliance-Anforderung nur für Produktionsdaten |
| Monitoring-Granularität | 5-Minuten-Intervalle | 1-Minuten-Intervalle | Produktion erfordert feingranularere Alarmierung |

**Umgebungsidentifikation**:

- Jede Umgebung zeigt eine klare visuelle Identifikation, um versehentliche Operationen in der falschen Umgebung zu verhindern.
- Hostname-Präfixe, Console-Banner, Browser-Tab-Labels und farbcodierte UI-Elemente unterscheiden Umgebungsstufen.
- Produktionsumgebungen zeigen prominente Identifikation (z.B. rote Banner, «[PRODUKTION]»-Labels).

---

## Cloud-Umgebungstrennung

Wo die Organisation in einer Cloud- oder Multi-Cloud-Umgebung tätig ist, gelten folgende zusätzliche Kontrollen.

**Konto- und Abonnementtrennung**:

- Produktions-Workloads müssen in dedizierten Cloud-Konten, Abonnements oder Projekten liegen — getrennt von allen Nicht-Produktions-Workloads.
- IAM-Richtlinien müssen kontoübergreifende Zugriffe verhindern, ausser durch explizit definierte, geprüfte Rollen.
- Service Control Policies (SCPs), Azure Policies oder Organisationsrichtlinien setzen Umgebungsgrenzen auf Organisationsebene durch.
- Die Abrechnung ist pro Umgebung zu trennen, um Kostenzuordnung und Anomalieerkennung zu ermöglichen.

**Cloud-Ressourcen-Tagging**:

Alle Cloud-Ressourcen sind mit Umgebungsidentifikation zu versehen (z.B. `env:production`, `env:staging`, `env:development`), um Folgendes zu unterstützen:

- Automatisierte Richtliniendurchsetzung (z.B. verhindern, dass Produktionsdatendienste durch Entwicklungsrollen zugänglich sind).
- Kostenzuordnung und -berichterstattung pro Umgebung.
- Compliance-Scanning und Audit-Berichterstattung.

**Infrastructure-as-Code-Governance**:

- Infrastrukturdefinitionen werden in versionskontrollierten Repositories gespeichert.
- Infrastrukturänderungen folgen demselben Promotion-Workflow wie Applikationscode (entwickeln, überprüfen, testen, deployment).
- Manuelle Änderungen an Produktionsinfrastruktur («ClickOps») sind verboten; alle Änderungen werden über die CI/CD-Pipeline angewendet.

---

## Umgebungstrennung und Incident Response

Die Umgebungstrennung unterstützt die Incident-Response-Ziele:

| Vorfallstyp | Vorteil der Umgebungstrennung | Reaktionsverfahren |
|-------------|-------------------------------|-------------------|
| **Produktionskompromittierung** | Angreifer kann nicht zu Entwicklungs-/Staging-Code pivotieren | Betroffene Produktionsumgebung isolieren; Entwicklung läuft ungestört weiter |
| **Entwicklungskompromittierung** | Angreifer kann nicht auf Produktionsdaten oder -systeme zugreifen | Entwicklungsumgebung neu aufbauen; kein Produktionseinfluss |
| **Supply-Chain-Angriff** | Schädlicher Code in Tests erkannt, bevor er die Produktion erreicht | Promotion blockieren; Umfang untersuchen; in Entwicklung beheben |
| **CI/CD-Pipeline-Kompromittierung** | Pro Umgebung beschränkte Pipeline-Zugangsdaten begrenzen den Schadenradius | Betroffene Zugangsdaten rotieren; Pipeline-Konfiguration prüfen; betroffene Artefakte neu erstellen |

Bei Vorfällen mit Umgebungsgrenzenverletzungen (unberechtigter Zugriff über Umgebungen hinweg, Produktionsdaten in Nicht-Produktionsumgebungen entdeckt) muss der Information Security Manager:

- Sofort ISB und DSB benachrichtigen.
- Datenexposition und regulatorische Meldepflichten nach nDSG beurteilen.
- Eindämmungsmassnahmen implementieren, um weiteren umgebungsübergreifenden Zugriff zu verhindern.
- Post-Incident-Review zur Identifikation der Grundursache und Vermeidung von Wiederholungen durchführen.
- Verletzung im Ausnahmeregister mit Korrekturmassnahmen dokumentieren.

---

## Entwicklererfahrung und Produktivität

Diese Richtlinie ist darauf ausgelegt, Produktionssysteme zu schützen und gleichzeitig eine effiziente Software-Auslieferung zu ermöglichen. Zur Unterstützung der Entwicklerproduktivität:

- **Lokale Entwicklungsumgebungen** sind uneingeschränkt (auf Entwickler-Workstations).
- **Nur-lese-Produktionszugriff** ist für Monitoring, Logs und Metriken verfügbar.
- **Staging-Umgebung** spiegelt Produktion eng für realistische Tests.
- **Break-Glass-Zugriff** ist bei Vorfällen (mit Genehmigung) verfügbar.
- **Synthetische Testdaten** sind leicht verfügbar und repräsentativ für Produktionsmuster.

Entwickler werden ermutigt, Verbesserungen für Entwicklungs- und Testumgebungen vorzuschlagen, die die Sicherheit wahren und gleichzeitig die Produktivität verbessern.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Anonymisierung** | Unwiderruflicher Prozess der Entfernung von Personendaten, so dass Personen auf keine vertretbare Weise re-identifiziert werden können; anonymisierte Daten sind keine Personendaten gemäss nDSG |
| **Break-Glass-Zugriff** | Notfallverfahren, das Personal ohne dauerhaften Produktionszugriff einen zeitlich begrenzten, genehmigten Produktionszugriff ermöglicht |
| **Change Advisory Board (CAB)** | Funktionsübergreifende Gruppe, die Änderungen an Produktionsumgebungen überprüft und genehmigt |
| **CI/CD-Pipeline** | Automatisierter Workflow, der Software-Änderungen durch Umgebungsstufen erstellt, testet und deployed |
| **Konfigurationsdrift** | Unbeabsichtigte Abweichung zwischen der beabsichtigten Konfiguration (wie in Code oder Dokumentation definiert) und der tatsächlichen Laufzeitkonfiguration einer Umgebung |
| **Unveränderliches Artefakt** | Ein Software-Build-Artefakt, das einmal erstellt und unverändert durch alle Umgebungen befördert wird, um Konsistenz zu gewährleisten |
| **MFA** | Multi-Faktor-Authentifizierung — erfordert zwei oder mehr Verifikationsfaktoren für den Zugriff |
| **PAM** | Privileged Access Management — System zur Verwaltung, Überwachung und Sicherung des Zugriffs auf privilegierte Konten und Zugangsdaten |
| **Pod Security Standards (PSS)** | Kubernetes-nativer Rahmen zur Definition von Sicherheitsrichtlinien auf Pod-Ebene; definiert drei Stufen (Privileged, Baseline, Restricted) |
| **Produktionsumgebung** | Live-Betriebsumgebung, die echte Benutzer mit echten Geschäftsdaten bedient |
| **Promotion** | Prozess der Beförderung von Änderungen von einer Umgebungsstufe zu einer anderen durch einen definierten, kontrollierten Workflow |
| **Pseudonymisierung** | Reversibler Prozess der Ersetzung identifizierender Daten durch Pseudonyme; pseudonymisierte Daten bleiben für jede Partei, die auf den Re-Identifikationsschlüssel zugreifen kann, Personendaten gemäss nDSG |
| **Staging-Umgebung** | Vorproduktionsumgebung, die die Produktionskonfiguration für die Abschlussvalidierung vor dem Release spiegelt |
| **Synthetische Daten** | Künstlich generierte Daten, die die statistischen und strukturellen Eigenschaften von Produktionsdaten beibehalten, ohne echte persönliche oder Geschäftsinformationen zu enthalten |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Genehmigung von Umgebungstrennungsausnahmen; Break-Glass-Genehmigungsinstanz; vierteljährliche Compliance-Überprüfung; jährliche Richtlinienüberprüfung; Berichterstattung an Geschäftsleitung |
| **TL / Development Manager** | Verwaltung von Entwicklungs- und Testumgebungen; CI/CD-Pipeline-Implementierung; Durchsetzung des Promotion-Workflows; Entwicklerschulung zur Umgebungstrennung; Ressourcenzuweisung für Umgebungsinfrastruktur |
| **IT-Operations-Manager** | Sicherheit der Produktionsumgebung; Genehmigung des Produktionszugriffs; PAM-Management; Deployment-Durchführung; Rollback-Verfahren; Infrastruktur-Monitoring; Konfigurationsdrift-Erkennung; Dokumentation der Staging-Produktions-Parität |
| **Information Security Manager** | Richtlinienpflege; Compliance-Bewertungen; Break-Glass-Überprüfung; Ausnahmenüberprüfung; Sicherheits-Monitoring; Vorfallsuntersuchung; vierteljährliche Compliance-Berichterstattung an ISB; Reaktion auf Umgebungsgrenzenverletzungen |
| **Datenschutzbeauftragter (DSB)** | Anonymisierungsgenehmigung für Nicht-Produktionsdatenverwendung; Re-Identifikationsrisikobewertung; Testdaten-Compliance mit nDSG; Datenverwaltungs-Audit |
| **QA-Teamleiter** | Verwaltung der Testumgebung; Testdaten-Lebenszyklus-Management; Integrität der Testumgebung; QA-Freigabe für Promotion-Gates |
| **Systemeigentümer** | Dokumentation der Umgebungsarchitektur; Compliance-Nachweise für eigene Systeme; Ausnahmemeldungen; Promotionsgenehmigung für ihre Systeme |
| **Entwickler** | Nur zugewiesene Umgebungen nutzen; Datenverarbeitungsanforderungen einhalten; definierte Promotion-Workflows verwenden; Umgebungsverletzungen melden; Umgebungstrennungsschulung absolvieren; Produktivitätsverbesserungen innerhalb der Richtliniengrenzen vorschlagen |
| **Security Team** | Monitoring der Umgebungszugriffsprotokolle; Scanning auf Produktionsdaten in Nicht-Produktionsumgebungen; Verletzungsuntersuchungen; Sicherheitsbewertung der Umgebungstrennungskontrollen; Incident Response bei Umgebungsgrenzenverletzungen |

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| # | Nachweis | Verantwortlich | Häufigkeit | Aufbewahrung |
|---|----------|----------------|-----------|--------------|
| 1 | **Umgebungsinventar** mit Stufenklassifikation, Hosting-Modell, Netzwerksegmentierungsdetails und verantwortlichem Eigentümer | IT-Operations-Manager | Fortlaufend gepflegt; jährlich überprüft | Lebensdauer der Umgebung + 3 Jahre |
| 2 | **Netzwerksegmentierungsdokumentation** (Firewall-Regeln, VPC-Konfigurationen, VLAN-Zuweisungen) mit vierteljährlichen Überprüfungsaufzeichnungen | IT-Operations-Manager / Network Team | Vierteljährlich | 3 Jahre |
| 3 | **Zugriffssteuerungsmatrizen** pro Umgebungsstufe mit Rollen-zu-Berechtigungs-Zuordnungen | IT-Operations-Manager / Development Manager | Fortlaufend gepflegt; gemäss Zugriffsüberprüfungsplan überprüft | 3 Jahre |
| 4 | **Zugriffsüberprüfungsaufzeichnungen** (Produktion vierteljährlich, Staging halbjährlich, Dev/Test jährlich) | Systemeigentümer / IT-Operations-Manager | Gemäss Plan | 3 Jahre |
| 5 | **Break-Glass-Aktivierungsprotokolle** mit Vorfallskennung, Genehmiger, Dauer, Massnahmen und Post-Incident-Review | Information Security Manager | Pro Ereignis; monatliche Überprüfung | 3 Jahre |
| 6 | **CI/CD-Pipeline-Konfiguration** mit Promotion-Gates, Genehmigungsanforderungen und Funktionstrennung | Development Manager / DevOps | Fortlaufend gepflegt; vierteljährlich überprüft | 2 Jahre |
| 7 | **Produktions-Deployment-Aufzeichnungen** mit CAB-Genehmigung, Rollback-Plan und Deployment-Ergebnis | IT-Operations-Manager | Pro Deployment | 3 Jahre |
| 8 | **Testdaten-Management-Aufzeichnungen** (Synthetische-Daten-Generierungsprotokolle, Anonymisierungsgenehmigungen, Datenlöschungsbestätigungen) | QA-Teamleiter / DSB | Pro Testzyklus | 3 Jahre |
| 9 | **Scan-Ergebnisse für Nicht-Produktionsumgebungen** ohne erkannte Produktionsdaten (oder Behebungsaufzeichnungen für Verstösse) | Security Team | Wöchentlicher Scan; monatliche Berichterstattung | 2 Jahre |
| 10 | **Konfigurationsdrift-Berichte** zwischen Staging und Produktion mit Lösungsaufzeichnungen | IT-Operations-Manager | Wöchentliche Erkennung; vierteljährliche Überprüfung | 2 Jahre |
| 11 | **Cloud-Konto/Abonnements-Trennungsdokumentation** mit IAM-Richtlinienexporten und Service Control Policies | IT-Operations-Manager / Cloud Team | Vierteljährlich | 3 Jahre |
| 12 | **Ausnahmeregister** (Anträge, Genehmigungen, kompensierende Kontrollen, Ablaufdaten, vierteljährliche Überprüfungen) | Information Security Manager | Fortlaufend gepflegt; vierteljährlich überprüft | Ausnahmedauer + 3 Jahre |
| 13 | **Schulungsnachweise zur Umgebungstrennung** für Entwickler, QA- und Operations-Personal | ISB / HR | Jährlich | Beschäftigungsdauer + 3 Jahre |
| 14 | **Notfall-Deployment-Aufzeichnungen** mit Begründung für das Umgehen des Standard-Promotion-Pfads und Post-Implementation-Review | IT-Operations-Manager / Development Manager | Pro Ereignis | 3 Jahre |
| 15 | **Staging-Produktions-Konfigurationsparitätsdokumentation** mit genehmigten Unterschieden und vierteljährlichen Überprüfungsaufzeichnungen | IT-Operations-Manager | Vierteljährlich | 2 Jahre |
| 16 | **Umgebungsgrenzenvorfallsaufzeichnungen** mit Eindämmungsmassnahmen, Ursachenanalyse und Korrekturmassnahmen | Information Security Manager | Pro Ereignis | 3 Jahre |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheitsmanagement-Team verifiziert die Einhaltung dieser Richtlinie durch verschiedene Methoden, darunter unter anderem Umgebungszugriffsberichte, Netzwerksegmentierungsaudits, CI/CD-Pipeline-Konfigurationsüberprüfungen, Daten-Scan-Berichte, Deployment-Genehmigungsaufzeichnungen, Zugriffsüberprüfungsabschlussaufzeichnungen, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

**Compliance-Kennzahlen**:

| Kennzahl | Ziel | Messhäufigkeit |
|----------|------|----------------|
| Umgebungen mit konformer Netzwerktrennung (Deny-all Standard, kein Entwicklungs-zu-Produktions-Pfad) | 100% | Vierteljährlich |
| Produktionszugriff auf autorisiertes Operations-Personal beschränkt (kein dauerhafter Entwicklerzugriff) | 100% | Vierteljährlich |
| Produktions-Deployments mit CAB-Genehmigung und dokumentiertem Rollback-Plan | >= 95% | Monatlich |
| Nicht-Produktionsumgebungen ohne erkannte Produktionsdaten (Scan sauber) | >= 95% | Monatlich |
| Break-Glass-Aktivierungen mit vollständiger Dokumentation und Post-Incident-Review | 100% | Pro Ereignis |
| Zugriffsüberprüfungen termingerecht gemäss Umgebungsstufe abgeschlossen | >= 90% | Vierteljährlich |
| CI/CD-Pipelines mit Durchsetzung von Promotion-Gates und Funktionstrennung | >= 95% | Vierteljährlich |
| Testdaten innerhalb von 30 Tagen nach Projektabschluss gelöscht | >= 90% | Vierteljährlich |
| Container-Images in Produktion signiert und verifiziert | 100% | Monatlich |

**Compliance-Bewertung**:

| Komponente | Gewichtung | Berechnung |
|------------|------------|------------|
| Netzwerktrennungs-Compliance | 25% | (Umgebungen mit konformer Netzwerktrennung) / Gesamtumgebungen × 100 |
| Zugriffssteuerungs-Compliance | 25% | (Umgebungen mit korrektem rollenbasiertem Zugriff + abgeschlossene Reviews) / Gesamt × 100 |
| Promotion-Prozess-Compliance | 25% | (Konforme Produktions-Deployments mit Genehmigung + Rollback-Plan) / Gesamtdeployments × 100 |
| Datenverarbeitungs-Compliance | 25% | (Nicht-Produktionsumgebungen ohne Produktionsdaten + termingerecht gelöschte Testdaten) / Gesamt × 100 |

**Compliance-Dashboard (Ziel)**:

Der Information Security Manager erstellt dieses Dashboard vierteljährlich und präsentiert es beim Management Review:

| Bereich | Wert | Status |
|---------|------|--------|
| **Gesamt-Compliance** | [berechnet] | GRÜN (>=90%) / GELB (>=70%) / ROT (<70%) |
| Netzwerktrennung | [berechnet] | |
| Zugriffssteuerung | [berechnet] | |
| Promotion-Prozess | [berechnet] | |
| Datenverarbeitung | [berechnet] | |

Im Dashboard-Bericht sind Punkte, die Aufmerksamkeit erfordern, sowie jüngste Verbesserungen hervorzuheben.

**Umgang mit Nichteinhaltung**: Ein Wert unter 70% erfordert sofortige ISB-Eskalation und einen Massnahmenplan. Ein Wert zwischen 70-89% erfordert die Aufsicht durch den Information Security Manager mit monatlichen Überprüfungen. Ein Wert von 90% und mehr folgt dem standardmässigen vierteljährlichen Monitoring.

**Behebungsverantwortung nach Bewertungskomponente**:

| Komponente | Unter Ziel | Behebungsverantwortlicher | Eskalation |
|------------|------------|---------------------------|------------|
| Netzwerktrennungs-Compliance | <100% | IT-Operations-Manager | ISB nach 15 Tagen Überschreitung |
| Zugriffssteuerungs-Compliance | <100% (Produktion) | IT-Operations-Manager / Development Manager | ISB nach 15 Tagen Überschreitung |
| Promotion-Prozess-Compliance | <95% | Development Manager / DevOps | ISB nach 30 Tagen Überschreitung |
| Datenverarbeitungs-Compliance | <95% | QA-Teamleiter / DSB | ISB sofort, wenn produktive Personendaten in Nicht-Produktionsumgebung gefunden |

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom Information Security Manager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, kompensierenden Kontrollen und einem definierten Überprüfungsdatum (maximal 12 Monate). Ausnahmen sind dem Management Review Team zu berichten.

Ausnahmen dürfen nur für folgende Fälle genehmigt werden: Legacy-Systeme, die innerhalb von 12 Monaten ausser Betrieb genommen werden sollen; technische Einschränkungen, bei denen eine vollständige Trennung nicht machbar ist (mit dokumentierter Begründung und kompensierenden Kontrollen); und temporäre Ausnahmen während Migrations- oder Transformationsprojekten (mit definiertem Enddatum).

Wenn Ausnahmen genehmigt werden, müssen kompensierende Kontrollen eine oder mehrere der folgenden umfassen: erweiterte Zugriffsprotokollierung und -überwachung, obligatorischer Code-Review für alle Änderungen, Nur-Lese-Zugriffsbeschränkungen, Datenmaskierungsanforderungen, erhöhter Change-Management-Rigor und häufigere Sicherheitsbewertungen.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarisch belangt werden, bis hin zur Kündigung des Arbeitsverhältnisses. Richtlinienverstösse sind zu dokumentieren, durch den Information Security Manager zu untersuchen und dem ISB zu berichten.

Verstösse, die eine Exposition von Produktionsdaten in Nicht-Produktionsumgebungen beinhalten, werden als Datenvorfälle behandelt und dem Datenschutzbeauftragten zur Beurteilung der Meldepflichten nach nDSG gemeldet.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen an Cloud- und Container-Plattformfähigkeiten, neue Bedrohungen für die Umgebungstrennung (Supply-Chain-Angriffe, CI/CD-Pipeline-Kompromittierungen, Container-Escape-Schwachstellen), regulatorische Änderungen (nDSG, DSGVO), Auditbefunde sowie Erkenntnisse aus Break-Glass-Aktivierungen und Umgebungsvorfällen.

---

# Adressierte Bereiche des ISO 27001-Standards

Richtlinie zur Trennung von Entwicklungs-, Test- und Produktionsumgebungen — ISO 27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Verantwortlichkeiten des Managements |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | 6.3 Sensibilisierung, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | 8.9 Konfigurationsmanagement |
| | 8.11 Datenmaskierung |
| | 8.25 Sicherer Entwicklungslebenszyklus |
| | **8.31 Trennung von Entwicklungs-, Test- und Produktionsumgebungen** |
| | 8.32 Change Management |
| | 8.33 Testinformationen |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|----------|
| Schweizerischer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen zum Datenschutz; Umgebungstrennung als technische Massnahme; Verbot produktiver Personendaten in Nicht-Produktionsumgebungen ohne gleichwertige Kontrollen |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit; Umgebungszugriffskontrollen als Sicherheitsmassnahme |
| EU DSGVO (sofern anwendbar) | Art. 25 — Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen (Umgebungstrennung); Art. 32 — Sicherheit der Verarbeitung (Zugangskontrolle pro Umgebung) |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.31 — Trennung von Entwicklungs-, Test- und Produktionsumgebungen |
| ISO/IEC 27002:2022 | Abschnitt 8.31 — Implementierungsleitfaden für Umgebungstrennung |
| NIST SP 800-53 Rev 5 | CM-4 (Impact Analyses), CM-7 (Least Functionality), SA-11 (Developer Testing and Evaluation), SC-32 (System Partitioning) |
| CIS Controls v8 | 4.1 (Secure Configuration of Enterprise Assets), 16.1–16.4 (Application Software Security) |

---

<!-- QA_VERIFIED: 2026-03-29 -->

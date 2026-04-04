<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.9-DE:operational:OP-POL:a.8.9 -->
**ISMS-OP-POL-A.8.9 — Konfigurationsmanagement**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Konfigurationsmanagement |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.9 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.8.9 — Configuration management
- ISO/IEC 27002:2022 Section 8.9 — Implementation guidance for configuration management
- NIST SP 800-128 — Guide for Security-Focused Configuration Management of Information Systems
- NIST SP 800-53 Rev 5 — CM-2 (Baseline Configuration), CM-3 (Configuration Change Control), CM-6 (Configuration Settings), CM-7 (Least Functionality)
- CIS Controls v8 — Control 4 (Secure Configuration of Enterprise Assets and Software)
- CIS Benchmarks — Plattformspezifische Härtungsleitfäden

**Verwandte Annex-A-Controls**:

| Control | Bezug zum Konfigurationsmanagement |
|---------|-----------------------------------|
| A.5.9 Inventar von Informationen und anderen zugehörigen Assets | Asset-Inventar definiert den Umfang des Konfigurationsmanagements; jedes Konfigurationselement ist einem inventarisierten Asset zugeordnet |
| A.5.23 Informationssicherheit für Cloud-Dienste | Cloud-Dienstkonfigurationen werden unter dieser Richtlinie verwaltet; das Modell der geteilten Verantwortung definiert Konfigurationsgrenzen |
| A.5.24–28 Incident-Management | Konfigurationsdrift oder nicht autorisierte Änderungen können Incident-Response auslösen; fehlgeschlagene Änderungen werden als Vorfälle eskaliert |
| A.8.1–7–18–19 Endpunktsicherheit | Endpunkt-Konfigurationsbaselines und Härtungsstandards werden unter dieser Richtlinie definiert und durchgesetzt |
| A.8.8 Management technischer Schwachstellen | Schwachstellenbehebung kann Konfigurationsänderungen erfordern; Härtung reduziert die Schwachstellenoberfläche |
| A.8.15 Protokollierung | Konfigurationsänderungsereignisse werden für Audit-Trail und Drift-Erkennung protokolliert |
| A.8.16 Überwachungsaktivitäten | Monitoring-Tools erkennen Konfigurationsdrift und nicht autorisierte Änderungen |
| A.8.20–22 Netzwerksicherheit | Netzwerkgerätekonfigurationen (Firewalls, Switches, Router) werden als Konfigurationselemente verwaltet |
| A.8.32 Änderungsmanagement | Konfigurationsänderungen folgen dem Änderungsmanagement-Genehmigungsprozess; komplementäre Disziplinen |

**Verwandte interne Richtlinien**:

- Asset-Management-Richtlinie
- Änderungsmanagementrichtlinie
- Endpunktsicherheitsrichtlinie
- Netzwerksicherheitsrichtlinie
- Protokollierungsrichtlinie
- Richtlinie für Überwachungsaktivitäten (A.8.16)
- Schwachstellenmanagementrichtlinie
- Incident-Management-Richtlinie

---

# Konfigurationsmanagement-Richtlinie

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass Konfigurationen, einschliesslich Sicherheitskonfigurationen, von Hardware, Software, Diensten und Netzwerken auf eine Weise eingerichtet, dokumentiert, implementiert, überwacht und überprüft werden, die das Risiko von Sicherheitsvorfällen durch Fehlkonfiguration, nicht autorisierte Änderungen oder Konfigurationsdrift reduziert.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem technische und organisatorische Massnahmen dem Risiko entsprechend implementiert werden, um personenbezogene Daten zu schützen, die von Systemen unter Konfigurationsmanagement verarbeitet werden. Die sichere Konfiguration von Systemen, die personenbezogene Daten verarbeiten, ist eine grundlegende technische Massnahme, die die Einhaltung von Datenschutzpflichten demonstriert. Soweit die Organisation Daten von Personen in der EU/im EWR verarbeitet, gelten auch die DSGVO-Art.-32-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden, Auftragnehmer und Drittnutzer mit Verantwortung für die Konfiguration, Wartung oder Verwaltung von Informationssystemen.

Alle Informationssysteme, Infrastruktur und Dienste, die Konfigurationsmanagement erfordern, einschliesslich:

- **Compute und Infrastruktur**: Server (physisch und virtuell), Container, Workstations, mobile Geräte.
- **Netzwerkgeräte**: Firewalls, Router, Switches, Load Balancer, WLAN-Access-Points, VPN-Gateways.
- **Cloud-Dienste**: IaaS-, PaaS- und SaaS-Konfigurationen im Einflussbereich der Organisation.
- **Betriebssysteme**: Server- und Endpunkt-Betriebssystemkonfigurationen.
- **Anwendungen und Middleware**: Anwendungsserver, Datenbanken, Webserver, Nachrichtenwarteschlangen.
- **Sicherheitssysteme**: SIEM, Endpunktschutz, Einbruchserkennung/-prävention, Identity Provider.
- **IoT- und OT-Systeme**: Vernetzte Geräte und Betriebstechnologie unter der Verwaltung der Organisation.

In allen Umgebungen: Produktion, Nicht-Produktion (Entwicklung, Test, QA, Staging), Disaster Recovery und Sandbox.

**Nicht im Geltungsbereich**: BYOD-Geräte, die nicht von der Organisation verwaltet werden; SaaS-Plattformen, bei denen die Organisation keine Konfigurationskontrolle hat (nur anbieterseitig verwaltet); temporäre Systeme mit einem Lebenszyklus von weniger als 24 Stunden (sofern keine personenbezogenen oder sensiblen Daten verarbeitet werden); Systeme, die über dokumentierte Risikobewertung mit ISB-Genehmigung explizit ausgeschlossen wurden.

## Grundsatz

Alle Informationssysteme sollen gemäss dokumentierten, genehmigten Sicherheitsbaselines konfiguriert werden, bevor sie in der Produktion bereitgestellt werden. Standard-Herstellerkonfigurationen ("out of the box") sind für den Produktionsbetrieb nicht akzeptabel.

Konfigurationen sollen:

- **Eingerichtet**: Sichere Baselines für jeden Asset-Typ unter Verwendung anerkannter Härtungsstandards definiert.
- **Dokumentiert**: Baseline-Parameter aufgezeichnet, versionskontrolliert und für autorisiertes Personal zugänglich.
- **Implementiert**: Systeme aus genehmigten Baselines oder Golden Images bereitgestellt.
- **Überwacht**: Tatsächliche Konfigurationen mit genehmigten Baselines verglichen, um Drift zu erkennen.
- **Überprüft**: Baselines in definierten Intervallen und nach wesentlichen Änderungen überprüft und aktualisiert.

Die Organisation soll das Prinzip der minimalen Funktionalität anwenden: Systeme sollen so konfiguriert werden, dass sie nur die Fähigkeiten bereitstellen, die für ihren beabsichtigten Zweck erforderlich sind, mit deaktivierten oder entfernten unnötigen Diensten, Ports, Protokollen und Konten.

**Implementierung minimaler Funktionalität** (spezifische Anforderungen):

**Dienste (Prozesse/Daemons)**:
- Ansatz: Nur erforderliche Dienste für die Systemrolle auf Whitelist setzen.
- Beispiel — Ubuntu-Anwendungsserver-Baseline: Erforderliche Dienste: sshd (Remote-Management), systemd-resolved (DNS), chrony (Zeitsync), Anwendungsdienst (z. B. nginx, App-Prozess). Deaktiviert/entfernt: cups (Drucken), avahi-daemon (mDNS), Bluetooth, X11 (grafische Dienste).
- Validierung: `systemctl list-units --state=running` mit Baseline-Whitelist verglichen; nicht autorisierte Dienste markiert.

**Netzwerkports**:
- Ansatz: Nur erforderliche abhörende Ports auf Whitelist setzen.
- Beispiel — Windows Server 2022 Domain Controller: Erforderliche Ports: 53 (DNS), 88 (Kerberos), 135 (RPC), 389/636 (LDAP/LDAPS), 445 (SMB), 3389 (RDP — auf Admin-Subnet beschränkt). Blockiert: Alle anderen Ports via Host-Firewall.
- Validierung: `netstat -an` oder `ss -tuln` mit Baseline verglichen; unerwartete Listener markiert.

**Protokolle**:
- Legacy-/unsichere Protokolle deaktivieren: SMBv1 (deaktiviert), TLS unter 1.2 (deaktiviert), SSHv1 (deaktiviert), Telnet (entfernt), FTP (durch SFTP/FTPS ersetzt).
- Nur sichere Alternativen aktivieren: SSH (mindestens v2), nur TLS 1.2/1.3, HTTPS obligatorisch.

**Standard-Konten**:
- Entfernen oder deaktivieren: Gastkonten, Hersteller-Standardkonten (Administrator umbenannt, Standardpasswörter geändert), nicht verwendete Dienstkonten.
- Baseline-Anforderung: Alle Konten in der Baseline mit Begründung dokumentieren (warum das Konto existiert, wofür es verwendet wird).

**Unnötige Funktionen/Rollen**:
- Windows: Nicht verwendete Serverrollen entfernen (z. B. Druckdienste entfernen, wenn kein Druckserver, IIS entfernen, wenn kein Webserver).
- Linux: Nicht verwendete Pakete entfernen (`apt autoremove`, `yum remove`).
- Cloud: Nicht verwendete Cloud-Dienste deaktivieren (z. B. AWS-EC2-Serielle Konsole deaktivieren wenn nicht benötigt, Azure Bastion deaktivieren wenn nicht verwendet).

Dokumentation: Jede Baseline soll eine Tabelle "Erforderliche Dienste und Ports" enthalten, die Whitelist-Elemente mit Begründung auflistet.

---

## Konfigurationsbaselines

### Baseline-Definition

Die Organisation soll sichere Konfigurationsbaselines auf **Asset-Typ-Ebene** definieren und pflegen (z. B. "Windows Server 2022 — Domain Controller", "Ubuntu 24.04 — Application Server", "Cisco IOS-XE — Core Switch"), nicht auf Einzelasset-Ebene.

Baselines sollen für alle Asset-Typen im aktiven Produktionsbetrieb definiert werden.

**Baseline-Abdeckungsanforderungen**:

Die Abdeckung soll gemessen werden nach:

- **Asset-Typ-Abdeckung**: Prozentsatz der unterschiedlichen Asset-Typen (OS + Rollen-Kombinationen) mit dokumentierten Baselines.
- **Instanz-Abdeckung**: Prozentsatz der gesamten Produktions-Asset-Instanzen, die von Baselines abgedeckt werden.

**Abdeckungsziele**:

| Asset-Tier | Asset-Typ-Abdeckung | Instanz-Abdeckung | Zeitrahmen |
|------------|--------------------|--------------------|------------|
| **Tier 1 (Kritisch)** | 100% | 100% | Sofort (keine Ausnahmen) |
| **Tier 2 (Hoch)** | 100% | 95% | Innerhalb von 6 Monaten nach Produktions-Deployment |
| **Tier 3 (Mittel)** | 90% | 90% | Innerhalb von 12 Monaten nach Produktions-Deployment |
| **Tier 4 (Niedrig)** | 80% | 80% | Best Effort |

**Lückenbehandlung**:

- **Tier-1/2-Assets ohne Baselines**: Deployment in Produktion soll blockiert werden, bis eine Baseline erstellt ist (durch Änderungsgenehmigung durchgesetzt).
- **Tier-3/4-Lücken**: Im Baseline-Lückenregister mit Sanierungsplan dokumentieren (Ziel: Baseline innerhalb von 90 Tagen nach Produktions-Deployment erstellt).
- **Ausnahme**: Legacy-Systeme kurz vor der Ausserdienststellung (weniger als 12 Monate verbleibende Lebensdauer) können auf die Baseline-Anforderung verzichten, mit ISB-Risikoakzeptanz und verbessertem Monitoring.

Jede Baseline soll dokumentieren:

- **Baseline-Kennung** (z. B. BASE-WIN2022-DC-v1.2) und Version.
- **Asset-Typ** und anwendbare Umgebungen.
- **Betriebssystemeinstellungen**: Sicherheitseinstellungen, aktivierte/deaktivierte Dienste, Kernel-Parameter, Registry-Einstellungen.
- **Anwendungskonfigurationen**: Standardeinstellungen, Sicherheitsparameter, Integrationspunkte.
- **Netzwerkeinstellungen**: IP-Konfiguration, Firewall-Regeln, Access-Control-Lists, Routing.
- **Sicherheitskonfigurationen**: Authentifizierungseinstellungen, Verschlüsselungsparameter, Protokollierungs- und Audit-Einstellungen, Passwortrichtlinien.
- **Angewendeter Härtungsstandard**: CIS-Benchmark-Niveau, Herstellerleitfaden oder benutzerdefinierter Standard mit Begründung.
- **Ausnahmen und Abweichungen**: Jede Abweichung vom Härtungsstandard mit dokumentierter Begründung und Risikoakzeptanz.
- **Validierungskriterien**: Wie überprüft wird, ob ein System der Baseline entspricht.

### Baseline-Genehmigung

Neue Baselines und Baseline-Updates sollen einem definierten Genehmigungsworkflow folgen:

| Aktion | Genehmigungsbefugnis | Zeitrahmen |
|--------|---------------------|------------|
| **Neue Baseline** | Technischer Lead (validiert Richtigkeit) + ISB oder Stellvertreter (validiert Sicherheit) | 14 Arbeitstage |
| **Baseline-Update** | Technischer Lead + ISB oder Stellvertreter | 7 Arbeitstage |
| **Notfall-Baseline-Änderung** | ISB (beschleunigt) | 24 Stunden; retrospektive Überprüfung innerhalb von 5 Arbeitstagen |

### Baseline-Überprüfung

Baselines sollen überprüft und aktualisiert werden:

- **Jährlich** (mindestens) für alle Baselines.
- **Vierteljährlich** für Tier-1-Systembaselines (kritisch).
- **Ad hoc** wenn ausgelöst durch: neue Schwachstellenoffenbarungen, die Baseline-Einstellungen betreffen, Technologie-Upgrades oder Versionsänderungen, Änderungen regulatorischer oder Compliance-Anforderungen, Erkenntnisse aus Sicherheitsvorfällen.

### Baseline-Ausserbetriebnahme

Wenn ein Asset-Typ ausser Betrieb genommen oder ersetzt wird:

- Die Baseline soll mit einem effektiven Datum als "DEPRECATED" markiert werden.
- Die Baseline soll 3 Jahre im Repository für historische Referenz aufbewahrt werden.
- Die Baseline soll aus dem aktiven Compliance-Monitoring entfernt werden.
- Eine Ersatz-Baseline (falls zutreffend) soll im Repository verknüpft werden.

---

## Standard-Builds und Golden Images

Die Organisation sollte Standard-Builds und Golden Images einführen, um eine konsistente, reproduzierbare Bereitstellung sicher konfigurierter Systeme sicherzustellen.

### Golden-Image-Anforderungen

Golden Images sollen:

- Die genehmigte Baseline für den betreffenden Asset-Typ implementieren.
- Nur genehmigte und lizenzierte Software enthalten.
- Aktuelle Sicherheits-Patches zum Zeitpunkt der Image-Erstellung enthalten.
- In einer Nicht-Produktionsumgebung getestet werden, bevor sie für den Produktionseinsatz genehmigt werden.
- Versioniert und in einem Konfigurations-Repository verfolgt werden.

**Golden-Image-Aktualisierungsrichtlinie** (risikobasiert):

**Geplante Aktualisierung** (Baseline):
- **Tier-1/2-Images**: Monatliche Aktualisierung.
- **Tier-3/4-Images**: Vierteljährliche Aktualisierung.

**Ausgelöste Aktualisierung** (sofort, überschreibt Zeitplan):
- **Kritischer Schwachstellen-Patch**: Innerhalb von 7 Tagen nach Patch-Veröffentlichung (für Schwachstellen in Baseline-Software mit CVSS >= 9,0 oder aktiver Ausnutzung).
- **Baseline-Update**: Innerhalb von 14 Tagen nach genehmigter Baseline-Änderung.
- **Sicherheitsvorfall**: Sofort, wenn das Golden Image kompromittiert sein könnte oder eine anfällige Konfiguration enthält.

**Aktualisierungsverfahren**:
1. Basis-Image mit neuesten Patches aktualisieren.
2. Aktuelle Baseline-Konfiguration anwenden.
3. In Nicht-Produktion testen: Testinstanz bereitstellen, Validierungs-Suite ausführen (Funktionstests, Sicherheits-Scan).
4. Sicherheitsteam-Validierung: Auf Fehlkonfigurationen scannen, Härtungskonformität verifizieren.
5. Genehmigung: IT-Operations-Manager + Sicherheitsteam-Abzeichnung.
6. Veröffentlichen: Altes Image im Repository ersetzen, altes Image als "DEPRECATED" markieren.
7. Benachrichtigen: Systemadministratoren über neue Image-Version informieren.

**Aufbewahrung alter Images**:
- Vorherige Version: 90 Tage aufbewahrt (Rollback-Möglichkeit wenn neues Image Probleme hat).
- Ältere Versionen: 1 Jahr archiviert (historische Referenz).

**Deployment-Durchsetzung**:
- Deployments mit Images älter als 60 Tage: Zur Überprüfung markiert (warum kein aktuelles Image?).
- Deployments mit Images älter als 90 Tage: Abgelehnt (muss aktuelles Image verwenden oder Ausnahme dokumentieren).

**Image-Alters-Tracking**: [Asset-Management-System] soll das Image-Erstellungsdatum pro bereitgestellter Instanz aufzeichnen; monatlichen Bericht über "veraltete Deployments" (Instanzen von Images älter als 30 Tage) erstellen.

Die Erstellung von Golden Images soll auf autorisiertes Personal (Systemadministratoren oder DevOps-Engineers) beschränkt werden. Neue oder aktualisierte Golden Images sollen vor der Genehmigung vom Sicherheitsteam validiert werden.

### Infrastructure as Code

Soweit machbar, sollte die Organisation Konfigurationsbaselines als Code definieren (z. B. Terraform, Ansible, CloudFormation, Kubernetes-Manifeste, Puppet, Chef) und sie durch Versionskontrolle verwalten:

- **Versionskontrolle**: IaC-Definitionen in Git oder gleichwertigem System mit vollständiger Änderungshistorie gespeichert.
- **Code-Review**: Konfigurationsänderungen über Pull-Request eingereicht und vor dem Merge überprüft.
- **Automatisierte Tests**: IaC durch automatisierte Tests validiert (Linting, Policy-as-Code-Scanning, Dry-Run) vor dem Deployment.
- **Änderungskontroll-Integration**: IaC-Deployments dem Änderungsmanagementprozess der Organisation unterworfen.
- **Fehlkonfigurations-Scanning**: IaC-Templates vor dem Deployment auf Sicherheitsfehlkonfigurationen gescannt (z. B. Checkov, tfsec oder gleichwertig).

**IaC-Sicherheits-Scanning-Anforderungen**:

**Scanning-Tools**: [Checkov / tfsec / Terraform Sentinel / Open Policy Agent] gemäss Organisationsstandards konfiguriert.

**Obligatorische Scan-Regeln** (alle IaC-Templates):

| Kategorie | Regelbeispiele | Durchsetzungsstufe |
|-----------|----------------|-------------------|
| **Verschlüsselung** | S3-Buckets im Ruhezustand verschlüsselt, RDS-Verschlüsselung aktiviert, EBS-Volumes verschlüsselt, TLS im Transit | Blockierend (Deployment schlägt bei Verletzung fehl) |
| **Zugangskontrolle** | Keine öffentlichen S3-Buckets (sofern nicht explizit genehmigt), Security Groups kein 0.0.0.0/0-Ingress auf sensiblen Ports (22, 3389), IAM-Richtlinien folgen minimaler Rechtevergabe | Blockierend |
| **Protokollierung** | CloudTrail aktiviert, VPC-Flow-Logs aktiviert, RDS/Datenbank-Protokollierung aktiviert | Blockierend |
| **Secrets-Management** | Keine hartcodierten Anmeldedaten in IaC (muss Secret-Manager-Referenzen verwenden), keine API-Keys im Klartext | Blockierend |
| **Netzwerksicherheit** | Standard-VPC nicht verwendet, Subnetze korrekt segmentiert (öffentlich/privat), NACLs konfiguriert | Warnung (Überprüfung erforderlich, kann mit Begründung überschrieben werden) |
| **Minimale Funktionalität** | Standard-Security-Group-Regeln entfernt, unnötige Dienste in Launch-Configs deaktiviert | Warnung |

**Benutzerdefinierte Regeln** (organisationsspezifisch):
- Obligatorische Tags: Alle Ressourcen mit Owner, Environment, CostCenter, DataClassification getaggt.
- Genehmigte Instanztypen: Nur von der Organisation genehmigte Instanzfamilien (keine exotischen Typen ohne Genehmigung).
- Genehmigte Regionen: Deployments nur in genehmigte Cloud-Regionen (z. B. eu-central-1, westeurope).

**Scan-Ausführung**:
- **Pre-Commit**: Entwickler führen Scans lokal vor dem Committen von IaC-Änderungen durch (empfohlen, nicht erzwungen).
- **CI/CD-Pipeline**: Automatisierter Scan bei Pull-Request (erforderlich); blockierende Verletzungen verhindern Merge.
- **Ausnahmeprozess**: Wenn blockierende Verletzung nicht behoben werden kann (legitimer Geschäftsbedarf), dokumentiert Entwickler Ausnahme in [Exception Tracker], ISB genehmigt, Ausnahme als Kommentar + Unterdrückungsregel in IaC aufgenommen.

**Scan-Ergebnisbehandlung**:
- Blockierende Verletzungen: Deployment gestoppt, beheben vor erneutem Versuch.
- Warnungseverletzungen: Protokolliert, wöchentlich vom Sicherheitsteam überprüft, eskaliert wenn Muster erkennbar.
- Ausnahmen: Vierteljährlich überprüft, widerrufen wenn nicht mehr gerechtfertigt.

**Regelset-Pflege**:
- Sicherheitsteam pflegt IaC-Scan-Regelset in [Git Repository].
- Regelset vierteljährlich überprüft, für neue Bedrohungen und Best Practices aktualisiert.
- Versionskontrolliert mit Änderungsprotokoll.

IaC ersetzt nicht den Bedarf an dokumentierten Baselines; es ist die bevorzugte Methode zur Implementierung und Durchsetzung.

---

## Konfigurationsänderungskontrolle

Alle Änderungen an Systemkonfigurationen sollen dem Änderungsmanagementprozess der Organisation folgen (siehe **Änderungsmanagementrichtlinie — A.8.32**). Dieser Abschnitt behandelt konfigurationsspezifische Anforderungen, die das Änderungsmanagement ergänzen.

### Änderungsklassifizierung

Konfigurationsänderungen sollen nach Risiko und Auswirkung klassifiziert werden:

| Typ | Definition | Genehmigung | Beispiele |
|-----|------------|-------------|-----------|
| **Standard** | Vorgenehmigte, risikoarme, wiederholbare Konfigurationsänderung gemäss dokumentiertem Verfahren | Vorgenehmigt (Katalog) | Zertifikatserneuerung, DNS-Datensatzzusatz, Standard-Firewall-Regel |
| **Normal** | Erfordert Bewertung, Tests und formale Genehmigung | Service-Owner / CAB | Baseline-Update, neuer Härtungsstandard, Netzwerktopologieänderung |
| **Notfall** | Dringende Änderung zur Lösung eines kritischen Vorfalls oder einer Schwachstelle | ISB oder IT-Operations-Manager (beschleunigt) | Deaktivierung eines kompromittierten Dienstes, Notfall-Firewall-Regel, kritischer Patch |

### Kategorisierung von Konfigurationsänderungen

**Erfordert formale Änderungsgenehmigung** (Änderungsmanagementrichtlinie A.8.32):
- Sicherheitsrelevante Konfigurationsänderungen: Authentifizierungseinstellungen, Verschlüsselungsparameter, Firewall-Regeln, Zugangskontrolle, Protokollierungsniveaus (Sicherheitsereignisse), Nutzer-/Gruppenberechtigungen.
- Baseline-Änderungen: Jede Änderung an einer genehmigten Baseline-Definition.
- Produktionssystemänderungen: Jede Konfigurationsänderung an Tier-1/2-Produktionssystemen (unabhängig von Sicherheitsrelevanz).
- Netzwerktopologieänderungen: Routing, VLANs, Subnetting, Firewall-Richtlinien.
- Mehrfachsystemänderungen: Konfigurationsänderungen, die mehr als 5 Systeme gleichzeitig betreffen.

**Vorgenehmigt** (Standard-Änderungskatalog, kein CAB):
- Parameter-Anpassung innerhalb dokumentierter Bereiche: Log-Rotationstage (7–30 Tage), Cache-Grössen (innerhalb definierter Grenzen), Timeout-Werte (innerhalb sicherer Bereiche).
- Zertifikatserneuerungen: TLS/SSL-Zertifikatsersatz mit gleichen Parametern.
- DNS-Datensatzzusätze: Hinzufügen von A/AAAA/CNAME-Datensätzen (keine Änderung autoritativer Server).
- Nutzer-Bereitstellung/Entzug: Gemäss dokumentierten Joiner/Mover/Leaver-Verfahren.

**Erfordert keine Änderungsgenehmigung** (betriebliche Anpassung):
- Kosmetische Änderungen: UI-Labels, nicht funktionale Beschreibungen, Kommentarfelder.
- Monitoring-Schwellenwert-Anpassung: Alarm-Schwellenwerte basierend auf beobachteten Baselines anpassen (in Monitoring-Tool dokumentiert).
- Nicht-Produktionssysteme: Konfigurationsänderungen an Tier-3/4-Entwicklungs-/Testsystemen (protokolliert, aber nicht formal genehmigt, sofern nicht sicherheitsrelevant).

Leitlinie: Bei Unsicherheit, ob eine Änderung eine Genehmigung erfordert, standardmässig **ja** (Änderungsantrag einreichen).

Dokumentation: Standard-Änderungskatalog soll in [Change-Management-System] mit vorab genehmigten Verfahren und Risikobewertungen gepflegt werden.

### Konfigurationsdokumentation-Update

Nach jeder genehmigten Konfigurationsänderung sollen folgende Dokumente innerhalb von **5 Arbeitstagen** aktualisiert werden:

- Konfigurationsbaseline-Dokumentation (wenn sich die Baseline selbst geändert hat).
- Konfigurationsmanagement-Datenbank (CMDB) oder gleichwertige Asset-Datensätze.
- Netzwerkdiagramme und Topologiedokumentation (bei Netzwerkkonfigurationsänderung).
- Betriebsverfahren und Runbooks (bei Änderung betrieblicher Schritte).
- Disaster-Recovery-Verfahren (wenn die Änderung kritische Systeme oder RTO/RPO betrifft).

### Nicht autorisierte Konfigurationsänderungen

Konfigurationsänderungen, die ausserhalb des genehmigten Änderungsmanagementprozesses vorgenommen wurden, sollen als Sicherheitsereignisse behandelt werden:

- Erkennung durch Konfigurationsmonitoring und Drift-Erkennung.
- Untersuchung zur Bestimmung der Ursache (böswillig, versehentlich oder Prozesslücke).
- Meldung an den ISB.
- Gegebenenfalls Korrektivmassnahmen, die disziplinarische Massnahmen einschliessen können.
- Das betroffene System soll auf die genehmigte Baseline saniert oder eine neue Baseline formal durch den Standardprozess genehmigt werden.

---

## Konfigurationsdrift-Erkennung und Monitoring

### Monitoring-Anforderungen

Die Organisation soll Konfigurationsmonitoring implementieren, um Abweichungen von genehmigten Baselines zu erkennen.

**Abdeckungsziele nach Asset-Kritikalität**:

| Asset-Tier | Abdeckungsziel | Monitoring-Häufigkeit | Akzeptable Abdeckungslücke |
|------------|---------------|-----------------------|---------------------------|
| **Tier 1 (Kritisch)** | 100% | Echtzeit oder stündlich | 0% |
| **Tier 2 (Hoch)** | 95% oder mehr | Täglich | Weniger als 5% |
| **Tier 3 (Mittel)** | 85% oder mehr | Wöchentlich | Weniger als 15% |
| **Tier 4 (Niedrig)** | 70% oder mehr | Monatlich | Weniger als 30% |

Monitoring-Tools sollen:

- Tatsächliche Systemkonfiguration mit der genehmigten Baseline vergleichen.
- Alarme generieren, wenn Konfigurationsabweichungen erkannt werden.
- Monitoring-Ergebnisse mindestens 90 Tage aufbewahren.
- Wenn praktikabel, mit [SIEM] für zentralisierte Alarmierung und Korrelation integrieren.

**Tool-Auswahl**: Die Organisation soll für ihre technische Umgebung geeignete Konfigurationsmonitoring-Tools auswählen. Tools sollen Baseline-Vergleich und Drift-Erkennung unterstützen. Beispiele: File-Integrity-Monitoring (FIM)-Tools, Cloud-Konfigurationsbewertungs-Tools (z. B. AWS Config, Azure Policy, GCP Security Command Center), Endpoint-Management-Plattformen und Konfigurationskonformitäts-Scanner.

Asset-Typen, die noch nicht unter automatisiertem Monitoring stehen, sollen mit einem geplanten Deployment-Datum und Zwischen-Kontrollen dokumentiert werden (z. B. vierteljährliche manuelle Audits). Abdeckungslücken sollen vom ISB risikoakzeptiert und im Risikoregister erfasst werden.

### Verwaltung von Monitoring-Abdeckungslücken

**Lückendokumentationsanforderungen**:
- Asset-Typ/-Instanz, der noch nicht überwacht wird: Im Monitoring-Lückenregister protokolliert.
- Registerfelder: Asset-ID, Tier, Lückengrund (Tool-Einschränkung, ausstehender Budget, technische Beschränkung), Zwischen-Kontrolle (manuelle Prüfung, verbesserte Protokollierung, eingeschränkter Zugang), Verantwortlicher (wer behebt), Geplantes Deployment-Datum, Tatsächliches Deployment-Datum, Status (Offen/In Bearbeitung/Geschlossen).

**Lückenschliessungs-SLAs** (von Identifikation bis Monitoring-Deployment):

| Asset-Tier | Maximale Lückendauer | Zwischen-Kontroll-Anforderung | Eskalation bei SLA-Verfehlung |
|------------|---------------------|------------------------------|-------------------------------|
| **Tier 1** | 30 Tage | Erweitertes manuelles Audit (wöchentliche Konfigurationsüberprüfung + monatliches Vollaudit) | ISB (sofort); kann Produktionsstopp bis Monitoring bereitgestellt erfordern |
| **Tier 2** | 90 Tage | Manuelles Audit (monatliche Konfigurationsüberprüfung) | IT-Operations-Manager, dann ISB nach 60 Tagen |
| **Tier 3** | 180 Tage | Manuelles Audit (vierteljährlich) | IT-Operations-Manager nach 120 Tagen |
| **Tier 4** | 365 Tage | Jährliches manuelles Audit akzeptabel | IT-Operations-Manager nach 270 Tagen |

**Lückenschliessungs-Verantwortlichkeit**:
- Lücken-Verantwortlicher: Zuständig für Implementierung der Monitoring-Lösung bis zum geplanten Deployment-Datum.
- Monatliche Überprüfung: IT-Operations-Manager überprüft Monitoring-Lückenregister, verfolgt Fortschritt, eskaliert überfällige Lücken.
- Vierteljährliche Berichterstattung: Zusammenfassung des Lückenregisters an ISB gemeldet (Anzahl offener Lücken nach Tier, durchschnittliche Schliessungszeit, überfällige Lücken).

**Zwischen-Kontrollen** (während Lücke besteht):
- Manuelle Konfigurationsüberprüfung: Systemadministrator exportiert Konfiguration, vergleicht manuell mit Baseline, dokumentiert Befunde.
- Verbesserte Zugangsprotokollierung: Privilegierter Kontozugang zu nicht überwachten Systemen wöchentlich protokolliert und überprüft.
- Änderungsstopp (nur Tier 1): Wenn Monitoring nicht innerhalb der SLA bereitgestellt werden kann, Einfrieren von Nicht-Notfalländerungen in Betracht ziehen bis Monitoring verfügbar ist.

**Lücken-Risikoakzeptanz**:
- Wenn Lücke nicht geschlossen werden kann (z. B. Legacy-System inkompatibel mit Monitoring-Tools, Budgetbeschränkungen): ISB genehmigt Risikoakzeptanz mit dokumentierter Begründung, kompensierenden Kontrollen und jährlicher Überprüfung.
- Risikoakzeptanz entbindet nicht von Zwischen-Kontrollen — manuelle Audits sollen fortgesetzt werden.

**Erfolgskriterium**: Ziel: Weniger als 5% der Tier-1/2-Assets im Monitoring-Lückenregister zu jeder Zeit.

### Drift-Klassifizierung und Reaktion

Wenn Konfigurationsdrift erkannt wird, soll dieser nach Schweregrad klassifiziert und innerhalb definierter Fristen beantwortet werden:

| Schweregrad | Definition | Reaktions-SLA | Beispiele |
|-------------|------------|---------------|-----------|
| **Kritisch** | Sicherheitskontrolle deaktiviert oder kompromittiert | Weniger als 1 Stunde | Firewall deaktiviert, nicht autorisiertes Admin-Konto erstellt, Verschlüsselung ausgeschaltet, Protokollierung auf kritischem System deaktiviert |
| **Hoch** | Sicherheitsrelevante Konfiguration geändert | Weniger als 4 Stunden | Passwortrichtlinie geschwächt, unnötiger Dienst aktiviert, Access-Control-List ohne Genehmigung geändert |
| **Mittel** | Nicht sicherheitsrelevanter Konfigurationsdrift | Weniger als 24 Stunden | Dienst-Port geändert, nicht kritische Anwendungseinstellung geändert, Dokumentationsabweichung |
| **Niedrig** | Informationelle Abweichung | Weniger als 5 Arbeitstage | Kosmetische Änderungen, nicht funktionale Einstellungen, geringfügige Parameterunterschiede |

**Alarm-Routing**:

- **Kritisch und Hoch**: Security-Operations-Team + ISB + Systemverantwortlicher.
- **Mittel**: IT-Operations-Manager + Systemverantwortlicher.
- **Niedrig**: IT-Betrieb (konsolidierter Tagesbericht).

### Drift-Behebung

Die Drift-Behebung soll einem strukturierten Workflow folgen:

1. **Erkennung**: Automatisches Monitoring identifiziert Konfigurationsabweichung.
2. **Triage**: IT-Betrieb untersucht die Ursache und bestimmt, ob die Änderung autorisiert, nicht autorisiert oder ein False Positive war.
3. **Massnahme**:
   - **Autorisierte Änderung** (genehmigt, aber Baseline noch nicht aktualisiert): Baseline-Dokumentation aktualisieren; Alarm schliessen.
   - **Nicht autorisierte Änderung**: System auf genehmigte Baseline sanieren; Ursache untersuchen; an ISB melden; nach Lösung schliessen.
   - **False Positive**: Monitoring-Regeln anpassen; Alarm schliessen.
4. **Dokumentation**: Alle Drift-Vorfälle protokolliert, bis zum Abschluss verfolgt und für Audit aufbewahrt.

**Drift-Behebungs-Verifizierung** (obligatorisch):

Behebungsverfahren:
1. **Drift identifizieren**: Monitoring-Tool erkennt Abweichung (z. B. Firewall-Regel hinzugefügt, Dienst aktiviert, Parameter geändert).
2. **Untersuchen**: Feststellen, ob autorisiert (genehmigte Änderung noch nicht dokumentiert) oder nicht autorisiert.
3. **Sanieren**: Wenn nicht autorisiert, auf Baseline zurücksetzen:
   - Manuell: Systemadministrator setzt Konfigurationsparameter auf Baseline-Wert zurück.
   - Automatisch: Konfigurationsmanagement-Tool (Ansible, Puppet, Chef) wendet Baseline erneut an.
   - Re-Image: Bei schwerwiegendem Drift oder Kompromittierung aus Golden Image neu aufbauen.
4. **Behebung verifizieren** (innerhalb von 24 Stunden nach Behebung):
   - System mit demselben Monitoring-Tool erneut scannen, das den Drift erkannt hat.
   - Bestätigen, dass Drift-Alarm gelöscht ist.
   - Dokumentieren: Behebungs-Ticket mit Verifizierungs-Zeitstempel, Scan-Ergebnissen und Abzeichnung aktualisiert.
5. **Ursachenanalyse** (für kritischen/hohen Drift):
   - Warum ist Drift aufgetreten? (Prozesslücke, nicht autorisierter Zugang, Automatisierungsfehler, Baseline-Fehler.)
   - Präventive Massnahme: Baseline aktualisieren, Automatisierung verbessern, Zugangskontrolle stärken, Personal schulen.
6. **Ticket schliessen**: Erst nach Verifizierung, die Baseline-Konformität bestätigt.

**Fehlgeschlagene Verifizierung**:
- Wenn erneuter Scan zeigt, dass Drift anhält: IT-Operations-Manager eskalieren, Behebung wiederholen, Systemisolation bei Sicherheitskontroll-Drift erwägen.
- Wenn Drift innerhalb von 30 Tagen erneut auftritt: Ursachenanalyse obligatorisch, ISB benachrichtigt.

**Verfolgte Drift-Behebungs-Kennzahlen**:
- Prozentsatz der Drift-Behebungen mit abgeschlossener Verifizierung: Ziel 100%.
- Zeit von Behebung bis Verifizierung: Ziel weniger als 24 Stunden.
- Wiederkehrender Drift (gleiches System, gleicher Parameter, mehr als 2 Vorkommen): Ziel 0.

Monatlich an ISB gemeldet.

**Behebungs-SLAs**:

| Schweregrad | Behebungs-SLA | Eskalation bei SLA-Verfehlung |
|-------------|--------------|-------------------------------|
| **Kritisch** | Weniger als 4 Stunden | ISB — kann System aus Produktion isolieren |
| **Hoch** | Weniger als 24 Stunden | ISB |
| **Mittel** | Weniger als 5 Arbeitstage | IT-Operations-Manager |
| **Niedrig** | Weniger als 30 Tage | Best Effort |

Wiederkehrender Drift am selben System oder Asset-Typ soll eine Ursachenanalyse auslösen. Wenn die Ursache eine Baseline ist, die in der Praxis nicht aufrechterhalten werden kann, soll die Baseline durch den standardmässigen Genehmigungsprozess überprüft und aktualisiert werden, anstatt wiederholt Ausnahmen zu akzeptieren.

---

## Sicherheitshärtungsstandards

### Auswahl des Härtungsstandards

Die Organisation soll für alle Asset-Typen in der Produktion anerkannte Sicherheitshärtungsstandards auswählen und anwenden.

**Anerkannte Standards** (in bevorzugter Reihenfolge):

| Standard | Anbieter | Typische Verwendung |
|----------|----------|---------------------|
| **CIS Benchmarks** | Center for Internet Security | Primäre Referenz für gängige Plattformen (Windows, Linux, Cloud, Netzwerkgeräte, Datenbanken) |
| **Herstellersicherheitsleitfäden** | Microsoft, AWS, Azure, GCP, Cisco usw. | Cloud-Plattformen, herstellerspezifische Produkte |
| **DISA STIGs** | Defense Information Systems Agency | Hochsicherheitsumgebungen, regierungsausgerichtete Umgebungen |
| **NIST-Baselines** | NIST SP 800-53, SP 800-128 | Framework-Ausrichtung, ergänzende Leitlinien |

Wenn mehrere Standards für einen Asset-Typ existieren, soll die Organisation den Standard auswählen, der am besten zu ihrem Risikoprofil passt, und die Auswahlbegründung dokumentieren.

### Härtungs-Implementierung

Alle Produktionssysteme sollen vor dem Deployment gehärtet werden. Die Härtung soll mindestens umfassen:

- **Nicht erforderliche Dienste, Ports und Protokolle entfernen oder deaktivieren** (Prinzip der minimalen Funktionalität — NIST CM-7).
- **Standard-Konten entfernen oder deaktivieren** oder alle Standard-Passwörter ändern.
- **Nicht erforderliche Funktionen** und Softwarekomponenten deaktivieren.
- **Authentifizierung konfigurieren** in Übereinstimmung mit der Authentifizierungsrichtlinie der Organisation.
- **Protokollierung und Audit-Trails aktivieren** für sicherheitsrelevante Ereignisse.
- **Aktuelle Sicherheits-Patches anwenden** vor der Produktionsplatzierung.
- **Verschlüsselung konfigurieren** für ruhende und übertragene Daten soweit anwendbar.
- **Administrativen Zugang einschränken** auf autorisiertes Personal mit MFA.

### Härtungs-Compliance-Ziele

| Asset-Tier | Kritische Sicherheitskontrollen | Gesamte Härtungs-Compliance | Akzeptable Lücken |
|------------|--------------------------------|-----------------------------|-------------------|
| **Tier 1 (Kritisch)** | 100% | 95% oder mehr | 0 kritische Lücken |
| **Tier 2 (Hoch)** | 95% oder mehr | 90% oder mehr | Weniger als 5 kritische Lücken |
| **Tier 3 (Mittel)** | 90% oder mehr | 80% oder mehr | Weniger als 10 kritische Lücken |
| **Tier 4 (Niedrig)** | 80% oder mehr | 70% oder mehr | Best Effort |

**Kritische Sicherheitskontrollen**: Authentifizierungsdurchsetzung, Verschlüsselungseinstellungen, Protokollierungskonfiguration, Zugangskontrolldurchsetzung und Patch-Aktualität.

### Härtungs-Verifizierung

Die Härtungskonformität soll durch periodisches Scanning verifiziert werden:

| Asset-Tier | Automatisierte Scan-Häufigkeit | Manuelle Verifizierung (wenn Automatisierung nicht verfügbar) |
|------------|-------------------------------|--------------------------------------------------------------|
| **Tier 1 (Kritisch)** | Vierteljährlich | Halbjährlich |
| **Tier 2 (Hoch)** | Halbjährlich | Jährlich |
| **Tier 3/4 (Mittel/Niedrig)** | Jährlich | Jährlich |

Verifizierungs-Tools können umfassen: OpenSCAP, Nessus, Qualys, Tenable, Cloud-native Compliance-Tools (z. B. AWS Security Hub, Azure Defender for Cloud) oder gleichwertige Plattformen.

Scan-Ergebnisse und Compliance-Berichte sollen mindestens **3 Jahre** für Auditzwecke aufbewahrt werden.

### Lücken-Behebung

Durch Verifizierung identifizierte Härtungslücken sollen risikoorientiert behoben werden:

| Lückenrisiko | Behebungszeitrahmen | Ausnahmegenehmigung |
|--------------|---------------------|---------------------|
| **Kritisch** | Weniger als 30 Tage | Nur ISB |
| **Hoch** | Weniger als 90 Tage | ISB oder IT-Operations-Manager |
| **Mittel** | Weniger als 180 Tage | IT-Operations-Manager |
| **Niedrig** | Best Effort | IT-Operations-Manager |

Lücken, die aufgrund technischer Einschränkungen oder Geschäftsanforderungen nicht behoben werden können, sollen als Ausnahmen mit kompensierenden Kontrollen dokumentiert werden (siehe Ausnahmeverwaltung unten).

**Kompensierende Kontrollen für Härtungsausnahmen** (spezifische Anforderungen):

Ausnahmeszenario: Eine Härtungsempfehlung kann nicht implementiert werden (z. B. Legacy-Protokoll kann nicht deaktiviert, Standard-Konto kann nicht entfernt, anfällige Komponente kann nicht gepatcht werden).

**Framework für kompensierende Kontrollen** (mehrschichtige Verteidigung):

Beispiel 1 — Kann SMBv1 nicht deaktivieren (Legacy-Anwendungsabhängigkeit):
- Kompensierende Kontrollen:
  1. Netzwerkisolation: System in isoliertem VLAN, Firewall-Regeln blockieren SMB von nicht vertrauenswürdigen Netzwerken.
  2. Zugangsbeschränkung: Nur spezifische Legacy-Client-IPs für SMB-Zugang auf Whitelist (ACL).
  3. Verbessertes Monitoring: IDS/IPS-Signaturen für SMBv1-Exploit-Versuche, Alarme bei ungewöhnlichem SMB-Datenverkehr.
  4. Patch-Aktualität: Sicherstellen, dass alle anderen verfügbaren Patches angewendet werden (auch wenn SMBv1 nicht deaktiviert werden kann, MS17-010 und ähnliche patchen).
  5. Ausserdienststellungsplan: Plan zur Migration von Legacy-Anwendung innerhalb von 12 Monaten dokumentieren (Ausnahme nicht unbefristet).

Beispiel 2 — Kann Standard-Administratorkonto nicht entfernen (Anwendung hartcodierte Abhängigkeit):
- Kompensierende Kontrollen:
  1. Konto umbenennen: Kontoname von "Administrator" in nicht offensichtlichen Namen ändern.
  2. Starkes Passwort: 20+ Zeichen zufälliges Passwort in [Password Vault] gespeichert.
  3. MFA-Durchsetzung: MFA für Kontoanmeldung erfordern.
  4. Monitoring: Alarm bei jeder Kontonutzung, alle Aktionen protokollieren.
  5. Regelmässige Passwortrotation: Alle 90 Tage.

Beispiel 3 — Kann anfällige Komponente nicht patchen (Hersteller stellt keine Patches mehr bereit, Ausserdienststellung geplant):
- Kompensierende Kontrollen:
  1. Netzwerkisolation: Air-gapped oder dediziertes Netzwerksegment.
  2. Remote-Zugang deaktivieren: Kein RDP/SSH von ausserhalb des isolierten Netzwerks.
  3. Virtuelles Patching: IPS-Regel einsetzen, um bekannte Exploit-Versuche zu blockieren.
  4. Daten minimieren: Wenn möglich, keine VERTRAULICHEN Daten auf dem System speichern.
  5. Ausserdienststellungs-Zeitplan: Dokumentierter Plan zur Systemreplatzierung innerhalb von 6 Monaten.

**Angemessenheitsbewertung kompensierender Kontrollen**:
- Kontrollen sollen das Risiko auf ein akzeptables Niveau reduzieren (ISB-Entscheidung).
- Mehrschichtige Verteidigung: Mindestens 3 kompensierende Kontrollen für kritische/hohe Lücken erforderlich.
- Kontrollen sollen verifizierbar und prüfbar sein (nicht nur "wir werden vorsichtig sein").

**Ausnahmedokumentation** (im Ausnahmeregister):
- Härtungsempfehlung, die nicht erfüllt werden kann.
- Geschäftlicher/technischer Grund (warum Behebung nicht möglich ist).
- Risikobewertung (welches Risiko durch Nichtbehebung entsteht).
- Kompensierende Kontrollen (spezifisch, messbar).
- Genehmigung: ISB-Unterschrift.
- Überprüfungsfrequenz: Vierteljährlich für kritische Lücken, halbjährlich für hohe/mittlere Lücken.
- Ablauf: Maximum 12 Monate; muss neu begründet werden wenn noch nötig.

**Ausnahmekennzahlen**:
- Gesamte aktive Ausnahmen: Trend im Laufe der Zeit sinkend.
- Ausnahmen älter als 12 Monate: Ziel 0 (erfordert erneute Genehmigung oder Behebung).
- Ausnahmen ohne angemessene kompensierende Kontrollen: 0 (beheben oder Kontrollen stärken).

---

## Konfigurationsaudit

### Interne Konfigurationsaudits

Die Organisation soll periodische Konfigurationsaudits durchführen, um zu verifizieren, dass:

- Systeme den genehmigten Baselines entsprechen.
- Konfigurationsdokumentation korrekt und aktuell ist.
- Änderungskontrollprozesse bei Konfigurationsänderungen befolgt wurden.
- Monitoring-Abdeckung definierte Ziele erfüllt.
- Härtungskonformität definierte Schwellenwerte erfüllt.

**Audit-Häufigkeit**:

- **Jährlich**: Vollständiger Konfigurationsaudit über alle Asset-Tiers.
- **Vierteljährlich**: Gezielter Audit von Tier-1- und Tier-2-Assets.
- **Ad hoc**: Nach wesentlichen Vorfällen, grossen Technologieänderungen oder regulatorischen Befunden.

### Audit-Nachweise

Konfigurationsaudits sollen dokumentierte Nachweise produzieren, einschliesslich:

- Baseline-Konformitäts-Scan-Ergebnisse.
- Konfigurationsänderungsaufzeichnungen für den Auditiertszeitraum.
- Drift-Erkennungsberichte und Behebungsaufzeichnungen.
- Härtungskonformitätswerte pro Asset-Typ.
- Ausnahmeregister-Überprüfung.
- Monitoring-Abdeckungsbewertung.

Audit-Ergebnisse sollen dem ISB gemeldet und in den Managementüberprüfungsprozess aufgenommen werden.

---

## Notfall-Konfigurationsänderungen

Notfall-Konfigurationsänderungen werden primär unter der **Änderungsmanagementrichtlinie (A.8.32)** behandelt. Konfigurationsspezifische Anforderungen für Notfalländerungen umfassen:

- Das System soll so schnell wie möglich in einen dokumentierten, bekannt-guten Konfigurationszustand zurückversetzt werden.
- Wenn die Notfalländerung zu einem neuen Konfigurationszustand führt (kein Zurückkehren zur Baseline), soll die Baseline innerhalb von **5 Arbeitstagen** durch den standardmässigen Genehmigungsprozess aktualisiert werden.
- Alle Notfall-Konfigurationsänderungen sollen protokolliert werden mit: den spezifisch geänderten Konfigurationsparametern, den vorherigen Werten, den neuen Werten, der Person, die die Änderung vorgenommen hat, und der geschäftlichen Begründung.
- Eine retrospektive Überprüfung durch den ISB oder Stellvertreter soll innerhalb von **48 Stunden** erfolgen.

Notfall-Konfigurationsänderungen sollen in keinem Kalendermonat **10%** aller Konfigurationsänderungen überschreiten. Das Überschreiten dieses Schwellenwerts löst eine Prozessüberprüfung aus.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Baseline-Konfiguration** | Dokumentierter Satz von Sicherheits- und Betriebskonfigurationsparametern für einen Asset-Typ, der als Referenz für Deployment, Compliance-Verifizierung und Drift-Erkennung dient |
| **Konfigurationsdrift** | Abweichung der tatsächlichen Systemkonfiguration von der genehmigten Baseline, möglicherweise auf nicht autorisierte Änderungen, Prozesslücken oder Dokumentationsfehler hinweisend |
| **Konfigurationselement (CI)** | Jedes Asset, jeder Dienst oder jede Komponente, die durch Konfigurationsmanagement verwaltet wird, mit definierten Attributen und Beziehungen verfolgt |
| **CMDB** | Konfigurationsmanagement-Datenbank — Repository, das Konfigurationsbaselines, Asset-Konfigurationen, Änderungshistorie und Beziehungen zwischen Konfigurationselementen speichert |
| **CIS Benchmark** | Konsensbasierter Sicherheitskonfigurationsleitfaden für bewährte Praktiken, veröffentlicht vom Center for Internet Security für spezifische Plattformen und Technologien |
| **Golden Image** | Vorkonfiguriertes System-Image, das die genehmigte Baseline implementiert und für die schnelle, konsistente Bereitstellung neuer Systeme verwendet wird |
| **Härtung** | Prozess der Sicherung von Systemkonfigurationen durch Implementierung anerkannter Sicherheitsstandards und Entfernung unnötiger Dienste, Konten, Ports und Funktionen |
| **Infrastructure as Code (IaC)** | Praxis der Verwaltung von Konfigurationsbaselines und Infrastrukturbereitstellung durch maschinenlesbaren Code, der in Versionskontrolle gespeichert ist |
| **Minimale Funktionalität** | Prinzip der Konfiguration von Systemen, um nur die für ihren beabsichtigten Zweck erforderlichen Fähigkeiten bereitzustellen |
| **Standard-Build** | Genehmigte, getestete und dokumentierte Systemkonfiguration, die als Basis für die Bereitstellung neuer Instanzen eines bestimmten Asset-Typs verwendet wird |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Baseline- und Ausnahme-Genehmigungsbefugnis; Drift-Eskalationspunkt; Härtungskonformitäts-Aufsicht; Berichterstattung an die Geschäftsleitung |
| **IT-Operations-Manager** | Tägliche Konfigurationsmanagement-Operationen; Baseline-Repository-Pflege; Monitoring-Koordination; Kennzahlenberichterstattung an ISB |
| **Sicherheitsteam** | Auswahl und Überprüfung von Härtungsstandards; Sicherheitsvalidierung von Baselines; Untersuchung von Drift-Alarmen; Compliance-Scanning; Audit-Unterstützung |
| **Systemverantwortliche** | Verantwortlichkeit für Konfigurationskonformität der eigenen Systeme; Änderungsgenehmigung für eigene Systeme; zeitnahe Drift-Behebung; Ressourcenzuweisung für Härtung |
| **Systemadministratoren / DevOps-Engineers** | Baseline-Implementierung; Erstellung und Pflege von Golden Images; Setup von Konfigurationsmonitoring; Ausführung genehmigter Änderungen; Drift-Triage und -Behebung |
| **Change Manager / CAB** | Genehmigung von Konfigurationsänderungen (normal und Notfall); Post-Implementierungs-Review; Erfolgs-Tracking von Änderungen |
| **Interne / externe Auditoren** | Unabhängige Verifizierung der Konfigurationskonformität; Nachweisüberprüfung; Befundberichterstattung |

---

## Nachweise

Die folgenden Nachweise belegen die Konformität mit dieser Richtlinie:

| # | Nachweis | Eigentümer | Häufigkeit | Aufbewahrung |
|---|---------|-----------|------------|--------------|
| 1 | **Konfigurationsbaseline-Repository** mit Versionshistorie, Genehmigungsaufzeichnungen und Überprüfungsdaten pro Asset-Typ | IT-Operations-Manager | Kontinuierlich gepflegt; jährlich überprüft (vierteljährlich für Tier 1) | Lebensdauer des Asset-Typs + 3 Jahre |
| 2 | **Golden-Image-Inventar** mit Version, Erstellungsdatum, Patch-Niveau und Validierungsaufzeichnungen | Systemadministratoren / DevOps | Kontinuierlich gepflegt; monatlich aktualisiert (Tier 1/2) oder vierteljährlich (Tier 3/4) | Lebensdauer des Images + 1 Jahr |
| 3 | **CMDB oder Konfigurationsinventar** mit Konfigurationselementen, angewendeten Baselines und aktuellem Compliance-Status | IT-Operations-Manager | Kontinuierlich gepflegt; vierteljährlich auditiert | Aktiv + 3 Jahre |
| 4 | **Konfigurationsänderungsaufzeichnungen** (Änderungsanträge, Genehmigungen, Implementierungsprotokolle, Post-Änderungs-Verifizierung) | Change Manager | Pro Änderung; vierteljährlich auditiert | 3 Jahre (7 Jahre für Auditnachweis) |
| 5 | **Drift-Erkennungsberichte** und Alarmprotokolle mit Triage-Ergebnissen, Behebungsaufzeichnungen und Post-Behebungs-Verifizierungsergebnissen | Sicherheitsteam / IT-Betrieb | Kontinuierlich; monatlich überprüft | 3 Jahre |
| 6 | **Härtungs-Compliance-Scan-Ergebnisse** pro Asset-Typ mit Compliance-Prozentsatz und identifizierten Lücken | Sicherheitsteam | Gemäss Scan-Zeitplan (vierteljährlich bis jährlich nach Tier) | 3 Jahre |
| 7 | **Lückenbehebungsregister** mit Lückenbeschreibung, Risikobewertung, Verantwortlichem, Fälligkeitsdatum, Status und Abschlussnachweis | IT-Operations-Manager | Kontinuierlich gepflegt; monatlich überprüft | Lückendauer + 3 Jahre |
| 8 | **Ausnahmeregister** für Konfigurationsabweichungen (Antrag, Begründung, kompensierende Kontrollen, Genehmigung, Ablaufdatum) | ISB | Kontinuierlich gepflegt; vierteljährlich überprüft | Ausnahmedauer + 3 Jahre |
| 9 | **Konfigurationsauditberichte** (intern und extern) mit Befunden und Korrekturmassnahmen | ISB / Auditoren | Jährlich (vollständig) + vierteljährlich (gezielt) | 3 Jahre |
| 10 | **Notfall-Konfigurationsänderungsaufzeichnungen** mit Begründung, Genehmigung, retrospektiver Überprüfung und Baseline-Update-Bestätigung | ISB | Pro Ereignis; retrospektiv innerhalb von 48 Stunden | 3 Jahre |
| 11 | **IaC-Repository-Zugangs- und Änderungsprotokolle** (Commit-Historie, Pull-Request-Reviews, Deployment-Aufzeichnungen) | DevOps / IT-Betrieb | Kontinuierlich | 3 Jahre |
| 12 | **Monitoring-Abdeckungsbericht** mit Prozentsatz der Assets unter automatisiertem Konfigurationsmonitoring nach Tier, einschliesslich Monitoring-Lückenregister-Status | IT-Operations-Manager | Monatlich | 1 Jahr |
| 13 | **SOC-2-Konfigurationskonformitätsnachweise** — Vierteljährliche Berichte, die zeigen, dass Tier-1/2-Systeme Härtungsbaselines erfüllen, mit Konfigurationsexporten als Stichprobe und Scan-Ergebnissen | Sicherheitsteam | Vierteljährlich vor SOC-2-Audit | 3 Jahre |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Managementteam verifiziert die Einhaltung dieser Richtlinie durch verschiedene Methoden, einschliesslich unter anderem Baseline-Abdeckungsbewertungen, Konfigurationsmonitoring-Berichte, Härtungskonformitäts-Scans, Drift-Erkennungs- und Behebungsaufzeichnungen, Änderungsdokumentation-Audits, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

**Konformitätskennzahlen**:

| Kennzahl | Ziel | Messhäufigkeit |
|----------|------|----------------|
| Tier-1-Asset-Typen mit dokumentierten, genehmigten Baselines | 100% | Vierteljährlich |
| Tier-2-Asset-Typen mit dokumentierten, genehmigten Baselines | 100% | Vierteljährlich |
| Tier-3/4-Asset-Typen mit dokumentierten, genehmigten Baselines | >= 80% | Vierteljährlich |
| Tier-1- und Tier-2-Assets unter automatisiertem Konfigurationsmonitoring | >= 95% | Monatlich |
| Drift-Alarme innerhalb SLA behoben | >= 90% | Monatlich |
| Drift-Behebungen mit abgeschlossener Post-Behebungs-Verifizierung | 100% | Monatlich |
| Härtungskonformität für kritische Sicherheitskontrollen (Tier 1) | >= 95% | Vierteljährlich |
| Notfall-Konfigurationsänderungen als Prozentsatz aller Änderungen | < 10% | Monatlich |
| Konfigurationsauditbefunde innerhalb vereinbarter Fristen geschlossen | >= 90% | Vierteljährlich |
| Golden Images planmässig aktualisiert (monatlich für Tier 1/2, vierteljährlich für Tier 3/4) | 100% | Monatlich |
| Monitoring-Lückenschliessung innerhalb SLA nach Tier | >= 90% | Vierteljährlich |
| Härtungsausnahmen älter als 12 Monate | 0 | Vierteljährlich |

**Handhabung von Nichtkonformität**: Kennzahlen unter 70% erfordern sofortige ISB-Eskalation und einen Sanierungsplan mit definierten Fristen. Kennzahlen zwischen 70% und 89% erfordern IT-Operations-Manager-Aufsicht mit monatlichen Fortschrittsüberprüfungen. Kennzahlen bei 90% und darüber folgen dem standardmässigen vierteljährlichen Monitoring.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom ISB genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, kompensierenden Kontrollen und einem definierten Ablaufdatum (Maximum 12 Monate). Ausnahmen sollen vierteljährlich überprüft und dem Management-Review-Team gemeldet werden. Abgelaufene Ausnahmen sollen Behebung oder formale Erneuerung durch den standardmässigen Genehmigungsprozess auslösen.

## Nichtkonformität

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterzogen werden, bis hin zur Beendigung des Arbeitsverhältnisses. Nicht autorisierte Konfigurationsänderungen an Produktionssystemen vorzunehmen, Sicherheitskontrollen zu deaktivieren, das Änderungsmanagement zu umgehen oder Konfigurationsdrift zu verschleiern, werden als schwerwiegende Verstösse betrachtet.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen an Branchen-Härtungsstandards (neue CIS-Benchmark-Versionen, Herstellersicherheitsleitfaden-Updates), neue Bedrohungen und Angriffstechniken, die auf Fehlkonfigurationen abzielen, Technologieänderungen (neue Plattformen, Cloud-Service-Einführung, Containerisierung), regulatorische Änderungen, Audit-Befunde sowie Erkenntnisse aus konfigurationsbezogenen Vorfällen berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Konfigurationsmanagement-Richtlinie — ISO-27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Verantwortlichkeiten des Managements |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | 5.37 Dokumentierte Betriebsverfahren |
| Klausel 8.1 Betriebliche Planung und Kontrolle | 6.3 Bewusstsein, Schulung und Training zur Informationssicherheit |
| | **8.9 Konfigurationsmanagement** |
| | 8.8 Management technischer Schwachstellen |
| | 8.32 Change Management |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen für die Datensicherheit; sichere Konfiguration als grundlegende technische Massnahme zum Schutz von Systemen, die personenbezogene Daten verarbeiten |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit; Konfigurationsmanagement unterstützt Zugangskontroll-, Protokollierungs- und Systemintegritätsanforderungen |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung; sicheres Konfigurationsmanagement als angemessene technische und organisatorische Massnahme |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.9 — Konfigurationsmanagement |
| ISO/IEC 27002:2022 | Abschnitt 8.9 — Implementierungsleitfaden für das Konfigurationsmanagement (neue Massnahme in der Ausgabe 2022) |
| NIST SP 800-128 | Guide for Security-Focused Configuration Management of Information Systems |
| NIST SP 800-53 Rev 5 | CM-2 (Baseline Configuration), CM-3 (Configuration Change Control), CM-6 (Configuration Settings), CM-7 (Least Functionality), CM-8 (System Component Inventory) |
| CIS Controls v8 | Control 4: Secure Configuration of Enterprise Assets and Software (Safeguards 4.1–4.12) |
| CIS Benchmarks | Plattformspezifische Härtungsleitfäden (Windows, Linux, macOS, Cloud-Plattformen, Netzwerkgeräte, Datenbanken) |

---

<!-- QA_VERIFIED: 2026-03-29 -->

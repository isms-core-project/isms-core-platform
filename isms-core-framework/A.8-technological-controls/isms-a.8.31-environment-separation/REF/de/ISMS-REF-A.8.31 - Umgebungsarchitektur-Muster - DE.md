<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-umgebungsarchitektur-muster-DE:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 — Umgebungsarchitektur-Muster**
**Technische Referenz für die Infrastrukturimplementierung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Umgebungsarchitektur-Muster |
| **Dokumententyp** | Referenzdokument (Nicht-ISMS-Technische Referenz) |
| **Dokument-ID** | ISMS-REF-A.8.31 |
| **Ersteller** | IT Operations Manager / Cloud-Architektur |
| **Dokumenteneigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | IT Operations Manager (Technische Referenz — keine Geschäftsleitungsgenehmigung erforderlich) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | IT Operations / Cloud-Architektur | Erstveröffentlichung technische Referenz für Umgebungstrennungsmuster |

**Überprüfungszyklus**: Bei Bedarf (Technologie- und Plattformentwicklung)
**Nächstes Überprüfungsdatum**: [Date + 12 months]
**Genehmiger**: IT Operations Manager / Cloud-Architekt (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verteiler**: IT Operations, Cloud-Architektur, DevOps, Systemeigentümer (zur technischen Implementierungssensibilisierung)

---

⚠️ **WICHTIG — NICHT-ISMS-TECHNISCHES SUPPORTDOKUMENT**

Dieses Dokument dient ausschliesslich zu Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist NICHT Bestandteil des Informationssicherheits-Managementsystems (ISMS).
- Dieses Dokument definiert KEINE verbindlichen Umgebungstrennungskontrollen oder -anforderungen.
- Dieses Dokument begründet KEINE verbindlichen Anforderungen, Fristen, KPIs oder SLAs.
- Dieses Dokument schreibt die Verwendung, das Verbot oder die Konfiguration spezifischer Cloud-Plattformen, Architekturen oder Tools weder vor noch untersagt es diese.
- Dieses Dokument überschreibt oder erweitert KEINE ISMS-Richtlinie.

Alle verbindlichen Anforderungen an die Umgebungstrennung, Verpflichtungen und Governance-Entscheidungen sind ausschliesslich in **ISMS-POL-A.8.31 (Umgebungstrennungsrichtlinie)** und anderen genehmigten ISMS-Dokumenten festgelegt.

Dieses Dokument dient ausschliesslich als technische Referenz für:

- Beschreibung häufig anzutreffender Umgebungsarchitektur-Muster
- Bereitstellung plattformspezifischer Implementierungsbeispiele
- Unterstützung bei Architekturentscheidungen während der Implementierung
- Information über technische Diskussionen und zukünftige Implementierungsplanung
- **Dieses Dokument darf NICHT als Revisions-Nachweis der Implementierung verwendet werden**

Die Verwendung dieses Dokuments impliziert keine Implementierung, Konformität oder operative Reife.

**Kritische Positionierungsaussage**:
Dieses Dokument enthält absichtlich technische Details, die über den Umfang der ISO/IEC-27001-Richtliniendokumentation hinausgehen. Sein Zweck ist ausschliesslich die technische Sensibilisierung. Aus dem Vorhandensein, Fehlen oder der Klassifizierung von Architekturmustern, Plattformen oder Konfigurationen in diesem Dokument dürfen keine Revisisonschlüsse gezogen werden.

---

# Dokumentzweck und Geltungsbereich

## Zweck

Dieses Dokument stellt technische Referenzmuster für die Implementierung der Umgebungstrennung auf gängigen Infrastrukturplattformen bereit. Es dient zur Unterstützung von:

- Technischer Sensibilisierung für plattformspezifische Trennungsansätze
- Verständnis von Cloud-Anbieter-Konto-/Abonnementmodellen
- Kontext für Infrastrukturarchitekturentscheidungen
- Diskussionen zur künftigen Implementierungsplanung
- Evaluierungskriterien für Tools und Plattformen

## Was dieses Dokument NICHT ist

Dieses Dokument:

- Definiert NICHT die erforderlichen oder verbotenen Architekturen von [Organisation]
- Begründet KEINE verbindlichen Implementierungsanforderungen
- Schafft KEINE Compliance-Verpflichtungen oder Revisionskriterien
- Ersetzt NICHT die Richtlinienanforderungen von ISMS-POL-A.8.31
- Schreibt KEINE spezifischen Cloud-Anbieter oder -Plattformen vor
- Ersetzt NICHT Anbieterdokumentation oder Best Practices

## Beziehung zur ISMS-Richtlinie

**Verbindliche Anforderungen**: ISMS-POL-A.8.31 legt fest, **WAS** an Umgebungstrennung erforderlich ist (Netzwerkisolierung, Infrastrukturtrennung, Credential-Trennung usw.)

**Dieses Dokument**: Erklärt **WIE** diese Anforderungen auf spezifischen Plattformen implementiert werden können (AWS-Multi-Account, Azure-Abonnements, Kubernetes-Namespaces usw.)

Organisationen wählen Plattformen und Architekturen entsprechend ihren Anforderungen. Die Anforderung ist Trennung; die Implementierung variiert.

---

# AWS (Amazon Web Services) — Multi-Account-Muster

## Architekturübersicht

**AWS-Organisationsstruktur**:

Empfohlene Struktur mit Organizational Units (OUs) zur Gruppierung von Konten nach Umgebung:

```
Root-Organisation
├── Security-OU (Organisational Unit)
│   ├── Audit-Konto (CloudTrail-Logs, Compliance-Reporting)
│   └── Security-Tooling-Konto (GuardDuty, SecurityHub, Inspector)
├── Development-OU
│   ├── Dev-Konto 1 (Anwendungsteam A — Entwicklung)
│   ├── Dev-Konto 2 (Anwendungsteam B — Entwicklung)
│   └── Geteiltes Dev-Services-Konto (DevOps-Tools, Artefakt-Repositories)
├── Testing-OU
│   ├── Test-Konto 1 (Anwendungsteam A — Testing)
│   ├── Test-Konto 2 (Anwendungsteam B — Testing)
│   └── Geteiltes Test-Services-Konto (QA-Automatisierungstools)
├── Staging-OU
│   ├── Staging-Konto 1 (Anwendungsteam A — Pre-Production)
│   └── Staging-Konto 2 (Anwendungsteam B — Pre-Production)
└── Production-OU
    ├── Production-Konto 1 (Anwendungsteam A — Produktion)
    ├── Production-Konto 2 (Anwendungsteam B — Produktion)
    └── Production Shared Services (Überwachung, Backup, Disaster Recovery)
```

**Gründe für Multi-Account**:

- **IAM-Grenze**: IAM-Richtlinien können keine Kontogrenzen überschreiten (verhindert Dev-→-Prod-Zugang)
- **Schadensbegrenzung**: Kompromittierung des Dev-Kontos beeinträchtigt die Produktion nicht
- **Kostenzuordnung**: Separate Abrechnung pro Umgebung
- **Service-Limits**: Separate Service-Kontingente pro Konto
- **Audit-Trail**: CloudTrail-Logs separat pro Konto

## Netzwerktrennung

**VPC (Virtual Private Cloud) pro Umgebung**:

Empfohlene CIDR-Blöcke (privater RFC-1918-Adressraum):

- Development-VPC: 10.1.0.0/16 (65.536 IPs)
- Testing-VPC: 10.2.0.0/16 (65.536 IPs)
- Staging-VPC: 10.3.0.0/16 (65.536 IPs)
- Production-VPC: 10.4.0.0/16 (65.536 IPs)

**VPC-Peering-Konfiguration**:

Kontrolliertes Peering nur zwischen benachbarten Umgebungen:

- ✅ Dev ↔ Test-Peering: Erlaubt (Deployment-Pipelines)
- ✅ Test ↔ Staging-Peering: Erlaubt (Beförderungsworkflows)
- ✅ Staging ↔ Production-Peering: Erlaubt (Deployment-Automatisierung)
- ❌ Dev ↔ Production-Peering: **VERBOTEN** (direkte Verbindung verstösst gegen Trennung)

**Security Groups**:

- Standard-Deny (kein eingehender Datenverkehr, wenn nicht explizit erlaubt)
- Separate Security Groups pro Umgebung
- Produktions-Security-Groups: nur über Terraform/CloudFormation verwaltet (manuelle Drift verhindern)
- Security-Group-Naming: `{umgebung}-{dienst}-{richtung}` (z.B. `prod-web-inbound`)

**Routing-Tabellen**:

- Standardroute zu Internet Gateway für öffentliche Subnetze
- NAT-Gateway für ausgehenden Datenverkehr privater Subnetze
- Keine Routen zwischen nicht benachbarten VPCs

## Zugangskontrolle (IAM)

**Rollenbasiertes Zugriffsmodell**:

**Entwickler-IAM-Rollen** (nur im Dev-Konto):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["ec2:*", "s3:*", "rds:*"],
    "Resource": "*",
    "Condition": {
      "StringEquals": {"aws:RequestedRegion": "eu-central-1"}
    }
  }]
}
```

**Operations-IAM-Rollen** (im Production-Konto):

- MFA für Console-Zugang erforderlich
- Sitzungsdauer: maximal 4 Stunden
- Genehmigungsworkflow (ServiceNow, Jira) vor AssumeRole erforderlich

**Cross-Account-AssumeRole** (Deployment-Pipeline):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::DEV-ACCOUNT-ID:root"},
    "Action": "sts:AssumeRole",
    "Resource": "arn:aws:iam::TEST-ACCOUNT-ID:role/DeploymentRole",
    "Condition": {
      "StringEquals": {"sts:ExternalId": "unique-deployment-external-id"}
    }
  }]
}
```

**Break-Glass-Notfallrolle** (Produktion):
```json
{
  "RoleName": "EmergencyBreakGlassRole",
  "MFARequired": true,
  "ApprovalRequired": true,
  "SessionDuration": 14400,
  "Logging": "Alle Aktionen in CloudTrail + SNS-Alarm protokolliert"
}
```

## Datentrennung

**S3-Buckets** (pro Umgebung):

- Naming: `{umgebung}-{app}-{zweck}-{konto-id}`
- Beispiele:
  - `dev-webapp-data-123456789012`
  - `test-webapp-data-234567890123`
  - `prod-webapp-data-345678901234`

**S3-Bucket-Richtlinien** (Produktion — Cross-Account-Zugang verhindern):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": "arn:aws:s3:::prod-webapp-data-*/*",
    "Condition": {
      "StringNotEquals": {"aws:PrincipalAccount": "PROD-ACCOUNT-ID"}
    }
  }]
}
```

**RDS-Datenbanken**:

- Separate RDS-Instanzen pro Umgebung
- Produktions-RDS:
  - Verschlüsselung im Ruhezustand (AWS KMS kundenverwalteter Schlüssel)
  - Automatisierte Backups (7–35 Tage Aufbewahrung)
  - Multi-AZ-Deployment (Hochverfügbarkeit)
  - Erweiterte Überwachung aktiviert
- Dev-/Test-RDS:
  - Kleinere Instanztypen zulässig
  - Einzelne AZ akzeptabel
  - Kürzere Backup-Aufbewahrung (7 Tage)

**AWS Secrets Manager**:

- Separate Geheimnisse pro Umgebung
- Namenskonvention: `{umgebung}/{dienst}/{geheimnis}` (z.B. `prod/webapp/db-passwort`)
- Produktionsgeheimnisse: automatische Rotation aktiviert (30–90 Tage)
- Cross-Account-Geheimniszugang: **VERBOTEN** über Ressourcenrichtlinien

## Deployment-Pipeline-Integration

**CodePipeline-Struktur**:

```
Quelle (CodeCommit/GitHub)
  ↓
Build (CodeBuild im Dev-Konto)
  ↓
Deploy ins Dev-Konto (automatisch)
  ↓
Test im Test-Konto (automatisch nach erfolgreichem Build)
  ↓
Deploy ins Staging-Konto (manuelle Genehmigung)
  ↓
Deploy ins Production-Konto (manuelle Genehmigung + CAB)
```

**Cross-Account-Deployment-Rolle**:

- Pipeline im Dev-Konto übernimmt Rolle in Zielkonten
- Zeitbegrenzte Credentials (1-Stunden-Sitzung)
- Audit-Trail in CloudTrail für alle Deployments

---

# Azure — Multi-Abonnement-Muster

## Architekturübersicht

**Azure-Verwaltungsgruppen-Hierarchie**:

```
Mandanten-Stammgruppe
├── Security-Verwaltungsgruppe
│   ├── Audit-Abonnement (Azure Monitor Logs, Log Analytics)
│   └── Security-Tools-Abonnement (Microsoft Defender, Sentinel)
├── Development-Verwaltungsgruppe
│   ├── Dev-Abonnement — Team A
│   └── Dev-Abonnement — Team B
├── Testing-Verwaltungsgruppe
│   ├── Test-Abonnement — Team A
│   └── Test-Abonnement — Team B
├── Staging-Verwaltungsgruppe
│   ├── Staging-Abonnement — Team A
│   └── Staging-Abonnement — Team B
└── Production-Verwaltungsgruppe
    ├── Production-Abonnement — Team A
    └── Production-Abonnement — Team B
```

**Gründe für Multi-Abonnement**:

- **Azure-Policy-Durchsetzung**: Auf Verwaltungsgruppenebene angewendete Richtlinien kaskadieren zu Abonnements
- **RBAC-Grenze**: Azure RBAC überschreitet keine Abonnementgrenzen
- **Kostenverwaltung**: Separate Abrechnung und Budgets pro Abonnement
- **Service-Limits**: Separate Kontingentgrenzen pro Abonnement
- **Schadensbegrenzung**: Kompromittierung eines Dev-Abonnements ist von der Produktion isoliert

## Netzwerktrennung

**Virtual Networks (VNets)** pro Abonnement:

- Development-VNet: 10.10.0.0/16
- Testing-VNet: 10.20.0.0/16
- Staging-VNet: 10.30.0.0/16
- Production-VNet: 10.40.0.0/16

**Network Security Groups (NSGs)**:

- Standard-Deny aller eingehenden Verbindungen
- Explizite Erlaubnisregeln für erforderlichen Datenverkehr
- Produktions-NSG: über Azure Policy verwaltet (manuelle Überschreibung verhindern)

**VNet-Peering**:

- Hub-and-Spoke-Topologie (zentrales Hub-VNet für gemeinsame Dienste)
- Spoke-VNets (Dev, Test, Staging, Prod) peeren nur zum Hub
- Transitives Routing deaktiviert (Dev kann Prod nicht über Hub erreichen)
- User-Defined Routes (UDRs) steuern den Datenverkehrsfluss

## Zugangskontrolle (Azure RBAC)

**Rollenzuweisungen nach Umgebung**:

**Entwickler** (Dev-Abonnement):

- Rolle: Mitwirkender (kann Ressourcen erstellen/ändern)
- Geltungsbereich: Ressourcengruppen im Dev-Abonnement
- Kein Zugang zu Test-/Staging-/Prod-Abonnements

**QA-Team** (Test-Abonnement):

- Rolle: Leser (Ressourcen anzeigen) + spezifischer App-Zugang
- Geltungsbereich: Ressourcengruppen des Test-Abonnements

**Operations** (Production-Abonnement):

- Rolle: Mitwirkender (über Privileged Identity Management — PIM)
- Erfordert: JIT-Aktivierung (Just-in-Time) + MFA + Genehmigung
- Sitzung: maximal 4 Stunden
- Audit: Alle Aktionen in Log Analytics protokolliert

**Azure AD Conditional Access**:

- Produktionszugang erfordert:
  - Verwaltetes Gerät (Intune-Compliance)
  - Multi-Faktor-Authentifizierung (MFA)
  - Vertrauenswürdiger Netzwerkstandort
  - Risikobasierte Richtlinien (Azure AD Identity Protection)

## Datentrennung

**Azure Storage Accounts**:

- Naming: `{env}{app}{zweck}{eindeutig-id}` (max. 24 Zeichen)
- Beispiele:
  - `devwebappdata001abc`
  - `testwebappdata002xyz`
  - `prodwebappdata003pqr`

**Azure SQL Database**:

- Separate Azure SQL Server pro Umgebung
- Produktions-SQL:
  - Transparent Data Encryption (TDE) aktiviert
  - Automatisierte Backups (7–35 Tage)
  - Georeplikation für DR
  - Advanced Threat Protection aktiviert
- Dev-/Test-SQL:
  - Niedrigere Performance-Tiers zulässig
  - Keine Georeplikation erforderlich

**Azure Key Vault**:

- Separate Key Vaults pro Umgebung
- Naming: `{umgebung}-{app}-kv` (z.B. `prod-webapp-kv`)
- Produktions-Key-Vault:
  - Soft-Delete aktiviert (90 Tage Aufbewahrung)
  - Schutz vor endgültigem Löschen aktiviert
  - Private Endpoint (kein öffentlicher Zugang)
  - Firewall-Regeln (nur bestimmte VNets erlauben)

## Azure-Policy-Durchsetzung

**Verwaltungsgruppen-Richtlinien**:

**Produktions-Verwaltungsgruppe** (auf allen Produktionsabonnements durchgesetzt):
```json
{
  "policyRule": {
    "if": {
      "allOf": [
        {"field": "type", "equals": "Microsoft.Storage/storageAccounts"},
        {"field": "Microsoft.Storage/storageAccounts/encryption.keySource",
         "notEquals": "Microsoft.KeyVault"}
      ]
    },
    "then": {"effect": "deny"}
  }
}
```
Bedeutung: Produktions-Storage-Accounts MÜSSEN kundenverwaltete Verschlüsselungsschlüssel verwenden.

**Deployment-Pipeline**:

- Azure DevOps Pipelines oder GitHub Actions
- Service-Principal pro Umgebung (auf Abonnement beschränkt)
- Pipeline: Dev → Test → Staging → Prod (manuelle Gates zwischen Phasen)

---

# GCP (Google Cloud Platform) — Projekt-Muster

## Architekturübersicht

**GCP-Organisations-Hierarchie**:

```
Organisation (beispiel.com)
├── Security-Ordner
│   ├── Audit-Projekt (Cloud-Logging-Aggregation)
│   └── Security-Tools-Projekt (Security Command Center)
├── Development-Ordner
│   ├── Dev-Projekt — Team A
│   └── Dev-Projekt — Team B
├── Testing-Ordner
│   ├── Test-Projekt — Team A
│   └── Test-Projekt — Team B
├── Staging-Ordner
│   ├── Staging-Projekt — Team A
│   └── Staging-Projekt — Team B
└── Production-Ordner
    ├── Production-Projekt — Team A
    └── Production-Projekt — Team B
```

**Gründe für Multi-Projekt**:

- **IAM-Grenze**: IAM-Richtlinien auf Projekte beschränkt
- **Abrechnung**: Separate Abrechnungskonten pro Projekt
- **Kontingente**: Separate Ressourcenkontingente pro Projekt
- **Audit**: Separate Cloud Audit Logs pro Projekt

## Netzwerktrennung

**VPC-Netzwerke** (pro Projekt):

- Shared-VPC-Architektur (Host-Projekt teilt VPC mit Dienstprojekten)
- Development-VPC: 10.100.0.0/16
- Testing-VPC: 10.110.0.0/16
- Staging-VPC: 10.120.0.0/16
- Production-VPC: 10.130.0.0/16

**VPC-Peering**:

- Kontrolliertes Peering zwischen benachbarten Umgebungen
- Private Google Access aktiviert (Zugang zu GCP-Diensten ohne öffentliche IPs)
- Kein transitives Peering (Dev kann Prod nicht erreichen)

**Firewall-Regeln**:

- Standard-Deny aller eingehenden Verbindungen
- Explizite Erlaubnisregeln erforderlich
- Produktions-Firewall-Regeln: über Terraform verwaltet (manuelle Änderungen verhindern)
- Priorität: 1000 (Deny All) → 100–500 (explizite Erlaubnisse)

## Zugangskontrolle (Cloud IAM)

**IAM-Rollen nach Umgebung**:

**Entwickler** (Dev-Projekt):

- Rolle: `roles/editor` (kann Ressourcen erstellen/ändern)
- Geltungsbereich: Nur Dev-Projekt
- Kein Zugang zu anderen Projekten

**Operations** (Production-Projekt):

- Rolle: `roles/compute.admin` + `roles/storage.admin` (eingeschränkter Geltungsbereich)
- Erfordert: Context-Aware Access + MFA
- Sitzung: zeitgebunden (4 Stunden über temporäre Credentials)

**Service Accounts** (für Anwendungen):

- Separate Service Accounts pro Umgebung
- Naming: `{env}-{app}-sa@{projekt-id}.iam.gserviceaccount.com`
- Produktions-Service-Accounts: Schlüsselrotation erzwungen (90 Tage)

**Deployment-Service-Account** (CI/CD):

- Service Account im Dev-Projekt
- Kann Service Accounts in Test-/Staging-/Prod-Projekten imitieren (Cross-Projekt-Deployment)
- Workload Identity Federation (keine JSON-Schlüssel in der Pipeline gespeichert)

## Datentrennung

**Cloud Storage Buckets**:

- Naming: `{projekt-id}-{app}-{zweck}` (z.B. `prod-team-a-webapp-data`)
- Produktions-Buckets:
  - Versionierung aktiviert
  - Aufbewahrungsrichtlinie (mindestens 30 Tage)
  - Kundenverwaltete Verschlüsselungsschlüssel (Cloud KMS)

**Cloud SQL**:

- Separate Cloud-SQL-Instanzen pro Projekt
- Produktions-SQL:
  - Automatisierte Backups (7–365 Tage)
  - Hochverfügbarkeit (regional)
  - Nur Private IP (keine öffentliche IP)
  - Datenbankverschlüsselung mit Cloud KMS

**Secret Manager**:

- Separate Geheimnisse pro Projekt
- Naming: `{umgebung}_{dienst}_{geheimnis}` (z.B. `prod_webapp_db_passwort`)
- Produktionsgeheimnisse: automatische Rotation (Secret Manager Rotation)

---

# Kubernetes-Umgebungstrennung

## Architekturoptionen

**Option 1: Namespace-basierte Trennung** (Einzelner Cluster):
```
Kubernetes-Cluster (geteilt)
├── dev-Namespace
├── test-Namespace
├── staging-Namespace
└── production-Namespace
```

**Vorteile**: Ressourceneffizienz, einfachere Verwaltung
**Nachteile**: Schwächere Isolation (Produktion teilt Control Plane mit Dev)
**Anwendungsfall**: Kleine Organisationen, risikoarme Anwendungen

**Option 2: Cluster-basierte Trennung** (Separate Cluster):
```
Development-Cluster
Test-Cluster
Staging-Cluster
Production-Cluster (separat)
```

**Vorteile**: Starke Isolation (Produktions-Control-Plane separat)
**Nachteile**: Höherer operativer Aufwand, höhere Kosten
**Anwendungsfall**: Grosse Organisationen, Hochrisikoanwendungen, regulatorische Anforderungen

**Empfehlung**: Cluster-basierte Trennung für Produktion, Namespace-basierte Trennung für Dev/Test/Staging.

## Namespace-basierte Trennung

**Namespace-Konfiguration**:

```yaml
# Produktions-Namespace mit Ressourcenkontingenten
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    environment: production
---
apiVersion: v1
kind: ResourceQuota
metadata:
  name: prod-quota
  namespace: production
spec:
  hard:
    requests.cpu: "100"
    requests.memory: 200Gi
    persistentvolumeclaims: "10"
```

**Netzwerkrichtlinien** (Namespaces isolieren):

```yaml
# Gesamten Datenverkehr zum Produktions-Namespace ausser von Ingress verweigern
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-from-other-namespaces
  namespace: production
spec:
  podSelector: {}
  policyTypes:

  - Ingress

  ingress:

  - from:
    - namespaceSelector:

        matchLabels:
          environment: production
```

**RBAC** (Rollenbasierte Zugriffskontrolle):

```yaml
# Entwickler dürfen nur auf den Dev-Namespace zugreifen
apiVersion: rbac.authorisation.k8s.io/v1
kind: RoleBinding
metadata:
  name: developers
  namespace: dev
subjects:

- kind: Group

  name: developers
  apiGroup: rbac.authorisation.k8s.io
roleRef:
  kind: ClusterRole
  name: edit
  apiGroup: rbac.authorisation.k8s.io
```

## Cluster-basierte Trennung

**Separate EKS-/AKS-/GKE-Cluster**:

**Development-Cluster**:

- Knotenanzahl: Auto-Scaling 2–10 Knoten
- Knotengrösse: Kleinere Instanztypen (Kostenoptimierung)
- Überwachung: Grundlegend (Prometheus)

**Production-Cluster**:

- Knotenanzahl: Auto-Scaling 5–50 Knoten
- Knotengrösse: Performance-optimierte Instanzen
- Überwachung: Vollständige Beobachtbarkeit (Prometheus, Grafana, Jaeger Tracing)
- Hochverfügbarkeit: Multi-AZ-Knotenpools

**Pod-Sicherheitsstandards**:

- Produktion: `restricted` (höchste Sicherheit)
- Staging: `restricted`
- Test: `baseline`
- Dev: `privileged` (Entwickler benötigen Flexibilität)

**Service Mesh** (Istio/Linkerd):

- mTLS zwischen Diensten (automatische Verschlüsselung)
- Datenverkehrsrichtlinien (Rate Limiting, Circuit Breakers)
- Beobachtbarkeit (Distributed Tracing)

---

# On-Premises / Traditionelle Infrastruktur

## VLAN-basierte Trennung

**Netzwerksegmentierung**:

```
Core-Netzwerk (192.168.0.0/16)
├── VLAN 10: Development (192.168.10.0/24)
├── VLAN 20: Testing (192.168.20.0/24)
├── VLAN 30: Staging (192.168.30.0/24)
└── VLAN 40: Production (192.168.40.0/24)
```

**Firewall-Regeln zwischen VLANs**:

- Standard-Deny aller Datenverkehr
- ACLs (Access Control Lists) erlauben Deployment-Datenverkehr (Dev → Test → Staging → Prod)
- Produktions-VLAN: kein eingehender Datenverkehr von Dev-/Test-VLANs

**Physische Switches**:

- VLAN-Tagging (IEEE 802.1Q)
- Private VLANs (PVLAN) für zusätzliche Isolation
- Spanning Tree Protocol (STP) zur Schleifenverhinderung

## Physische Trennung (Hohe Sicherheit)

**Separate Infrastruktur pro Umgebung**:

**Development-Rechenzentrum / Serverraum**:

- Dedizierte Server für Entwicklungs-Workloads
- Separater Netzwerk-Switch
- Separater Internetanschluss (optional)

**Production-Rechenzentrum** (separater physischer Standort):

- Dedizierte Produktionsserver
- Separate Netzwerkinfrastruktur
- Physische Zugangskontrollen (Kartenleser, Biometrie)
- 24/7-Überwachung

**Anwendungsfall**: Finanzinstitute, Behörden, Gesundheitswesen (hohe Compliance-Anforderungen)

## DMZ und Staging-Zonen

**Mehrstufige Netzwerkarchitektur**:

```
Internet
  ↓
Firewall (DMZ)
  ↓
Web-Tier-VLAN (öffentlich zugänglich)
  ↓
Firewall
  ↓
Applikations-Tier-VLAN
  ↓
Firewall
  ↓
Datenbank-Tier-VLAN (am stärksten eingeschränkt)
```

**Staging-Zone** (spiegelt Produktion):

- Separates Staging-VLAN
- Spiegelt die Produktionsarchitektur (gleiche Tiers, gleiche Firewall-Regeln)
- Validiert Produktionsbereitstellung vor der eigentlichen Produktion

---

# Hybrid-Cloud-Muster

## Cloud + On-Premises Hybrid

**Architektur**:

- Entwicklung/Test: Cloud-basiert (AWS/Azure/GCP)
- Produktion: On-Premises-Rechenzentrum (regulatorische Anforderung)

**Konnektivität**:

- VPN oder Direct Connect / ExpressRoute / Cloud Interconnect
- Deployment-Pipeline deployt in Cloud Dev/Test, dann in On-Premises Prod

**Anwendungsfall**: Organisationen in der Cloud-Migration (Produktion während des Übergangs On-Premises behalten)

## Multi-Cloud Hybrid

**Architektur**:

- Entwicklung: AWS (kostengünstig)
- Testing: Azure (PaaS-Dienste)
- Produktion: GCP (Hochleistungs-Compute)

**Herausforderungen**:

- Komplexes IAM (separate Identitätssysteme)
- Netzwerkkonnektivität (VPN zwischen Clouds)
- Kostenverwaltung (Multi-Cloud-Abrechnung)

**Anwendungsfall**: Anbieter-Diversifizierung, Best-of-Breed-Dienste

---

# Referenz-Architekturdiagramme

## AWS Multi-Account-Trennung

```
┌─────────────────────────────────────────────────────────────┐
│ AWS-Organisations-Root                                       │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Dev-Konto    │  │ Test-Konto   │  │ Prod-Konto   │      │
│  │              │  │              │  │              │      │
│  │ VPC 10.1.0.0 │  │ VPC 10.2.0.0 │  │ VPC 10.4.0.0 │      │
│  │              │  │              │  │              │      │
│  │ IAM: Dev-    │  │ IAM: QA-     │  │ IAM: Ops-    │      │
│  │ Rollen       │  │ Rollen       │  │ Rollen (PAM) │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│         │                  │                  │              │
│         └──────────────────┴──────────────────┘              │
│          Deployment-Pipeline (CodePipeline)                  │
└─────────────────────────────────────────────────────────────┘
```

## Kubernetes-Namespace-Trennung

```
┌──────────────────────────────────────────────────┐
│ Kubernetes-Cluster                                │
│                                                   │
│ ┌────────────┐ ┌────────────┐ ┌────────────┐    │
│ │ dev        │ │ test       │ │ production │    │
│ │ namespace  │ │ namespace  │ │ namespace  │    │
│ │            │ │            │ │            │    │
│ │ Pods       │ │ Pods       │ │ Pods       │    │
│ │ Services   │ │ Services   │ │ Services   │    │
│ │            │ │            │ │            │    │
│ │ Netzwerk-  │ │ Netzwerk-  │ │ Netzwerk-  │    │
│ │ Richtlinie:│ │ Richtlinie:│ │ Richtlinie:│    │
│ │ Erlaubt    │ │ Eingeschr. │ │ Isoliert   │    │
│ └────────────┘ └────────────┘ └────────────┘    │
└──────────────────────────────────────────────────┘
```

---

# Entscheidungsrahmen

## Wahl des Trennungsansatzes

| Faktor | Namespace-basiert | Konto-/Abonnement-basiert | Physische Trennung |
|--------|------------------|--------------------------|-------------------|
| **Kosten** | Niedrig (gemeinsame Ressourcen) | Mittel (separate Konten) | Hoch (duplizierte Infrastruktur) |
| **Isolation** | Mittel (nur logisch) | Hoch (Kontogrenzen) | Maximum (physisch) |
| **Compliance** | Niedriges bis mittleres Risiko | Hohes Risiko akzeptabel | Maximum (Finanzwesen, Gesundheitswesen) |
| **Komplexität** | Niedrig (Einzelcluster/-konto) | Mittel (Multi-Account-Management) | Hoch (separate Rechenzentren) |
| **Empfohlen für** | Kleine Organisationen, geringes Risiko | Die meisten Organisationen | Regulierte Branchen |

## Migrationspfad

**Phase 1**: Mit Namespace-basierter Trennung beginnen (schnell zu implementieren)
**Phase 2**: Zu Konto-/Abonnement-basierter Trennung migrieren (stärkere Isolation)
**Phase 3**: Physische Trennung nur für Produktion in Betracht ziehen (bei regulatorischer Anforderung)

---

**ENDE DES REFERENZDOKUMENTS**

---

*Dieses technische Referenzdokument unterstützt ISMS-POL-A.8.31. Implementierungsentscheidungen sollten auf der Risikobeurteilung der Organisation basieren und vom ISB genehmigt werden.*

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

<!-- QA_VERIFIED: 2026-03-29 -->

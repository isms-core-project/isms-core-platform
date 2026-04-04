<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-IT-environment-architecture-patterns:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 — Modelli di architettura degli ambienti**
**Riferimento tecnico per l'implementazione dell'infrastruttura**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Modelli di architettura degli ambienti |
| **Tipo di documento** | Documento di riferimento (Riferimento tecnico non-SGSI) |
| **Identificativo del documento** | ISMS-REF-A.8.31 |
| **Autore del documento** | Responsabile delle operazioni IT / Architettura cloud |
| **Proprietario del documento** | RSSI |
| **Approvato da** | Responsabile delle operazioni IT (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Distribuzione**: Operazioni IT, Architettura cloud, DevOps, Proprietari dei sistemi

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione. NON fa parte del SGSI, NON stabilisce requisiti vincolanti e NON sostituisce ISMS-POL-A.8.31.

---

# Scopo e ambito del documento

## Scopo

Questo documento fornisce modelli di riferimento tecnico per l'implementazione della separazione degli ambienti sulle piattaforme di infrastruttura più comuni. È inteso a supportare:

- La consapevolezza tecnica degli approcci di separazione specifici per piattaforma
- La comprensione dei modelli di account/abbonamento dei provider cloud
- Le decisioni di architettura dell'infrastruttura
- La pianificazione dell'implementazione

## Relazione con la politica SGSI

**Requisiti vincolanti**: ISMS-POL-A.8.31 definisce COSA è richiesto (isolamento di rete, separazione dell'infrastruttura, separazione delle credenziali, ecc.)

**Questo documento**: Fornisce COME tali requisiti possono essere implementati su piattaforme specifiche (multi-account AWS, abbonamenti Azure, namespace Kubernetes, ecc.)

---

# Modello multi-account AWS

## Panoramica dell'architettura

**Struttura delle AWS Organizations**:

Struttura raccomandata che utilizza Unità Organizzative (OU) per raggruppare gli account per ambiente:

```
Organizzazione radice
├── OU Sicurezza
│   ├── Account Audit (log CloudTrail, report di conformità)
│   └── Account Strumenti di sicurezza (GuardDuty, SecurityHub, Inspector)
├── OU Sviluppo
│   ├── Account Dev 1 (Team A — Sviluppo)
│   ├── Account Dev 2 (Team B — Sviluppo)
│   └── Account Servizi Dev Condivisi (strumenti DevOps, repository di artefatti)
├── OU Test
│   ├── Account Test 1 (Team A — Test)
│   └── Account Servizi Test Condivisi (strumenti di automazione QA)
├── OU Staging
│   ├── Account Staging 1 (Team A — Pre-produzione)
│   └── Account Staging 2 (Team B — Pre-produzione)
└── OU Produzione
    ├── Account Produzione 1 (Team A — Produzione)
    ├── Account Produzione 2 (Team B — Produzione)
    └── Servizi Condivisi Produzione (monitoraggio, backup, disaster recovery)
```

**Perché il multi-account**:

- **Confine IAM**: Le politiche IAM non possono attraversare i confini degli account (impedisce l'accesso dev → prod)
- **Raggio di impatto**: La compromissione dell'account dev non influisce sulla produzione
- **Attribuzione dei costi**: Fatturazione separata per ambiente
- **Limiti di servizio**: Quote di servizio separate per account
- **Traccia di audit**: Log CloudTrail separati per account

## Separazione di rete

**VPC (Virtual Private Cloud) per ambiente**:

Blocchi CIDR consigliati (spazio di indirizzamento privato RFC 1918):

- VPC Sviluppo: 10.1.0.0/16 (65.536 IP)
- VPC Test: 10.2.0.0/16 (65.536 IP)
- VPC Staging: 10.3.0.0/16 (65.536 IP)
- VPC Produzione: 10.4.0.0/16 (65.536 IP)

**Configurazione del peering VPC**:

Peering controllato solo tra ambienti adiacenti:

- ✅ Peering Dev ↔ Test: Consentito (pipeline di distribuzione)
- ✅ Peering Test ↔ Staging: Consentito (flussi di promozione)
- ✅ Peering Staging ↔ Produzione: Consentito (automazione della distribuzione)
- ❌ Peering Dev ↔ Produzione: **VIETATO** (la connessione diretta viola la separazione)

**Security Group**:

- Rifiuto predefinito (nessun traffico in ingresso a meno che non sia esplicitamente consentito)
- Security group separati per ambiente
- Security group di produzione: gestiti solo tramite Terraform/CloudFormation
- Denominazione: `{ambiente}-{servizio}-{direzione}` (es. `prod-web-ingresso`)

## Controllo degli accessi (IAM)

**Modello di accesso basato sui ruoli**:

**Ruoli IAM Sviluppatori** (solo nell'account Dev):
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

**Ruoli IAM Operazioni** (nell'account Produzione):

- Richiedere MFA per l'accesso alla console
- Durata della sessione: massimo 4 ore
- Flusso di approvazione richiesto prima di AssumeRole

**AssumeRole cross-account** (pipeline di distribuzione):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::ID-ACCOUNT-DEV:root"},
    "Action": "sts:AssumeRole",
    "Resource": "arn:aws:iam::ID-ACCOUNT-TEST:role/DeploymentRole",
    "Condition": {
      "StringEquals": {"sts:ExternalId": "id-esterno-distribuzione-unico"}
    }
  }]
}
```

**Ruolo di emergenza (Break-Glass)** (Produzione):

- MFA obbligatoria
- Approvazione richiesta
- Durata della sessione: 4 ore
- Registrazione: tutte le azioni registrate in CloudTrail + avviso SNS

## Separazione dei dati

**Bucket S3** (per ambiente):

- Denominazione: `{ambiente}-{app}-{scopo}-{id-account}`
- Esempi: `dev-webapp-data-123456789012`, `prod-webapp-data-345678901234`

**Politiche dei bucket S3** (produzione — impedire l'accesso cross-account):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": "arn:aws:s3:::prod-webapp-data-*/*",
    "Condition": {
      "StringNotEquals": {"aws:PrincipalAccount": "ID-ACCOUNT-PROD"}
    }
  }]
}
```

**Database RDS**:

- Istanze RDS separate per ambiente
- RDS Produzione: crittografia a riposo (chiave gestita dal cliente AWS KMS), backup automatici (7-35 giorni), distribuzione Multi-AZ, monitoraggio avanzato
- Dev/Test RDS: tipi di istanza più piccoli accettabili, Single-AZ accettabile

**AWS Secrets Manager**:

- Segreti separati per ambiente
- Convenzione di denominazione: `{ambiente}/{servizio}/{segreto}` (es. `prod/webapp/db-password`)
- Segreti di produzione: rotazione automatica abilitata (30-90 giorni)

---

# Modello multi-abbonamento Azure

## Panoramica dell'architettura

**Gerarchia dei gruppi di gestione Azure**:

```
Gruppo radice del tenant
├── Gruppo di gestione Sicurezza
│   ├── Abbonamento Audit (log Azure Monitor, Log Analytics)
│   └── Abbonamento Strumenti di sicurezza (Microsoft Defender, Sentinel)
├── Gruppo di gestione Sviluppo
│   ├── Abbonamento Dev — Team A
│   └── Abbonamento Dev — Team B
├── Gruppo di gestione Test
├── Gruppo di gestione Staging
└── Gruppo di gestione Produzione
    ├── Abbonamento Produzione — Team A
    └── Abbonamento Produzione — Team B
```

**Perché il multi-abbonamento**:

- **Applicazione delle politiche Azure**: Le politiche al livello del gruppo di gestione si propagano agli abbonamenti
- **Confine RBAC**: Azure RBAC non attraversa i confini degli abbonamenti
- **Gestione dei costi**: Fatturazione e budget separati per abbonamento
- **Contenimento del raggio di impatto**: La compromissione dell'abbonamento dev è isolata dalla produzione

## Separazione di rete

**Reti virtuali (VNet)** per abbonamento:

- VNet Sviluppo: 10.10.0.0/16
- VNet Test: 10.20.0.0/16
- VNet Staging: 10.30.0.0/16
- VNet Produzione: 10.40.0.0/16

**Gruppi di sicurezza di rete (NSG)**:

- Rifiuto predefinito di tutto il traffico in ingresso
- Regole di autorizzazione esplicite per il traffico richiesto
- NSG Produzione: gestito tramite Azure Policy (impedire la sostituzione manuale)

**Peering VNet**:

- Topologia hub-and-spoke (VNet hub centrale per i servizi condivisi)
- VNet spoke (Dev, Test, Staging, Prod) si connettono solo all'Hub
- Routing transitivo disabilitato (Dev non può raggiungere Prod tramite Hub)

## Controllo degli accessi (Azure RBAC)

**Assegnazioni di ruolo per ambiente**:

**Sviluppatori** (Abbonamento Dev):

- Ruolo: Collaboratore (può creare/modificare risorse)
- Ambito: Gruppi di risorse nell'abbonamento Dev
- Non può accedere agli abbonamenti Test/Staging/Prod

**Team QA** (Abbonamento Test):

- Ruolo: Lettore + accesso specifico all'applicazione
- Ambito: Gruppi di risorse dell'abbonamento Test

**Operazioni** (Abbonamento Produzione):

- Ruolo: Collaboratore (tramite Privileged Identity Management — PIM)
- Requisiti: Attivazione JIT (Just-in-Time) + MFA + approvazione
- Sessione: massimo 4 ore
- Audit: tutte le azioni registrate in Log Analytics

**Accesso condizionale Azure AD**:

L'accesso alla produzione richiede:

- Dispositivo gestito (conformità Intune)
- Autenticazione a più fattori (AMF)
- Posizione di rete attendibile
- Politiche basate sul rischio (Azure AD Identity Protection)

## Separazione dei dati

**Account di archiviazione Azure**:

- Denominazione: `{amb}{app}{scopo}{idunivoco}` (max 24 caratteri)
- Esempi: `devwebappdata001abc`, `prodwebappdata003pqr`

**Azure SQL Database**:

- Server Azure SQL separati per ambiente
- SQL Produzione: TDE abilitato, backup automatici (7-35 giorni), geo-replica per DR, Advanced Threat Protection
- Dev/Test SQL: livelli di prestazioni inferiori accettabili

**Azure Key Vault**:

- Vault separati per ambiente
- Denominazione: `{ambiente}-{app}-kv` (es. `prod-webapp-kv`)
- Key Vault Produzione: eliminazione reversibile abilitata (90 giorni), protezione dalla purga abilitata, endpoint privato, regole del firewall

## Applicazione delle politiche Azure

**Politiche del gruppo di gestione**:

**Gruppo di gestione Produzione** (applicato a tutti gli abbonamenti di produzione):
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
Traduzione: Gli account di archiviazione di produzione DEVONO utilizzare chiavi di crittografia gestite dal cliente.

---

# Modello multi-progetto GCP

## Panoramica dell'architettura

**Gerarchia dell'organizzazione GCP**:

```
Organizzazione (example.com)
├── Cartella Sicurezza
│   └── Progetto Strumenti di sicurezza (Security Command Center)
├── Cartella Sviluppo
│   ├── Progetto Dev — Team A
│   └── Progetto Dev — Team B
├── Cartella Test
├── Cartella Staging
└── Cartella Produzione
    ├── Progetto Produzione — Team A
    └── Progetto Produzione — Team B
```

**Perché il multi-progetto**:

- **Confine IAM**: Politiche IAM con ambito limitato ai progetti
- **Fatturazione**: Account di fatturazione separati per progetto
- **Quote**: Quote di risorse separate per progetto
- **Audit**: Cloud Audit Log separati per progetto

## Separazione di rete

**Reti VPC** (per progetto):

- Sviluppo VPC: 10.100.0.0/16
- Test VPC: 10.110.0.0/16
- Staging VPC: 10.120.0.0/16
- Produzione VPC: 10.130.0.0/16

**Regole del firewall**:

- Rifiuto predefinito di tutto il traffico in ingresso
- Regole di autorizzazione esplicite richieste
- Regole del firewall di produzione: gestite tramite Terraform

## Controllo degli accessi (Cloud IAM)

**Ruoli IAM per ambiente**:

**Sviluppatori** (Progetto Dev):

- Ruolo: `roles/editor` (può creare/modificare risorse)
- Ambito: Solo progetto dev

**Operazioni** (Progetto Produzione):

- Ruoli con ambito limitato (compute.admin, storage.admin)
- Accesso contestuale + MFA richiesti
- Con limite di tempo (4 ore tramite credenziali temporanee)

**Account di servizio applicativi**:

- Account di servizio separati per ambiente
- Denominazione: `{amb}-{app}-sa@{id-progetto}.iam.gserviceaccount.com`
- Account di servizio di produzione: rotazione delle chiavi applicata (90 giorni)

## Separazione dei dati

**Bucket Cloud Storage**:

- Produzione: versioning abilitato, politica di conservazione (minimo 30 giorni), chiavi di crittografia gestite dal cliente (Cloud KMS)

**Cloud SQL**:

- Istanze Cloud SQL separate per progetto
- Produzione: backup automatici, alta disponibilità (regionale), solo IP privato, crittografia Cloud KMS

**Secret Manager**:

- Segreti separati per progetto
- Denominazione: `{ambiente}_{servizio}_{segreto}` (es. `prod_webapp_db_password`)
- Produzione: rotazione automatica

---

# Separazione degli ambienti Kubernetes

## Opzioni di architettura

**Opzione 1: Separazione per namespace** (cluster singolo):
```
Cluster Kubernetes (condiviso)
├── namespace dev
├── namespace test
├── namespace staging
└── namespace production
```

**Vantaggi**: Efficienza delle risorse, gestione più semplice  
**Svantaggi**: Isolamento più debole (la produzione condivide il piano di controllo con dev)  
**Caso d'uso**: Piccole organizzazioni, applicazioni a basso rischio

**Opzione 2: Separazione per cluster** (cluster distinti):
```
Cluster Sviluppo
Cluster Test
Cluster Staging
Cluster Produzione (separato)
```

**Vantaggi**: Isolamento forte (piano di controllo della produzione separato)  
**Svantaggi**: Maggiore overhead operativo, costo più elevato  
**Caso d'uso**: Grandi organizzazioni, applicazioni ad alto rischio

**Raccomandato**: Separazione per cluster per la produzione, per namespace per dev/test/staging.

## Separazione per namespace

**Configurazione del namespace**:

```yaml
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

**Politiche di rete** (isolare i namespace):

```yaml
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

**RBAC**:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developers
  namespace: dev
subjects:
- kind: Group
  name: developers
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: edit
  apiGroup: rbac.authorization.k8s.io
```

## Separazione per cluster

**Cluster EKS/AKS/GKE distinti**:

**Cluster Sviluppo**:

- Numero di nodi: Auto-scaling 2-10
- Dimensione dei nodi: Tipi di istanza più piccoli (ottimizzazione dei costi)
- Monitoraggio: Base (Prometheus)

**Cluster Produzione**:

- Numero di nodi: Auto-scaling 5-50
- Dimensione dei nodi: Istanze ad alte prestazioni
- Monitoraggio: Osservabilità completa (Prometheus, Grafana, tracciamento Jaeger)
- Alta disponibilità: Pool di nodi Multi-AZ

**Standard di sicurezza dei pod**:

- Produzione: `restricted` (sicurezza massima)
- Staging: `restricted`
- Test: `baseline`
- Dev: `privileged` (gli sviluppatori hanno bisogno di flessibilità)

---

# Infrastruttura on-premises / Tradizionale

## Separazione basata su VLAN

**Segmentazione di rete**:

```
Rete principale (192.168.0.0/16)
├── VLAN 10: Sviluppo (192.168.10.0/24)
├── VLAN 20: Test (192.168.20.0/24)
├── VLAN 30: Staging (192.168.30.0/24)
└── VLAN 40: Produzione (192.168.40.0/24)
```

**Regole del firewall tra VLAN**:

- Rifiuto predefinito di tutto il traffico
- ACL che consentono il traffico di distribuzione (dev → test → staging → prod)
- VLAN Produzione: nessun traffico in ingresso dalle VLAN dev/test

---

# Infrastruttura ibrida

## Cloud + On-premises

**Architettura**:

- Sviluppo/Test: basato su cloud (AWS/Azure/GCP)
- Produzione: data center on-premises (requisito normativo)

**Connettività**:

- VPN o Direct Connect / ExpressRoute / Cloud Interconnect

**Caso d'uso**: Organizzazioni in migrazione al cloud (mantenimento della produzione on-premises durante la transizione)

---

# Quadro decisionale

## Scelta dell'approccio di separazione

| Fattore | Per namespace | Per account/abbonamento | Separazione fisica |
|---------|--------------|------------------------|--------------------|
| **Costo** | Basso (risorse condivise) | Medio (account separati) | Alto (infrastruttura duplicata) |
| **Isolamento** | Medio (solo logico) | Alto (confini dell'account) | Massimo (fisico) |
| **Conformità** | Rischio basso-medio | Rischio alto accettabile | Massimo (finance, sanità) |
| **Complessità** | Bassa | Media | Alta |
| **Consigliato per** | Piccole org., basso rischio | La maggior parte delle organizzazioni | Settori regolamentati |

## Percorso di migrazione

**Fase 1**: Iniziare con la separazione per namespace (rapida da implementare)  
**Fase 2**: Migrare alla separazione per account/abbonamento (isolamento più forte)  
**Fase 3**: Considerare la separazione fisica solo per la produzione (se requisito normativo)

---

**FINE DEL DOCUMENTO DI RIFERIMENTO**

---

*Questo riferimento tecnico supporta ISMS-POL-A.8.31. Le decisioni di implementazione devono essere basate sulla valutazione del rischio organizzativo e approvate dal RSSI.*

<!-- QA_VERIFIED: 2026-04-04 -->

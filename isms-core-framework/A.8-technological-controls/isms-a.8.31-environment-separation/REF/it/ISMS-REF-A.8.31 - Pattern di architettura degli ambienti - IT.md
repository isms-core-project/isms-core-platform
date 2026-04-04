<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-IT-environment-architecture-patterns:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 — Pattern di architettura degli ambienti**
**Riferimento tecnico per l'implementazione dell'infrastruttura**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Pattern di architettura degli ambienti |
| **Tipo di documento** | Documento di riferimento (Riferimento tecnico non-SGSI) |
| **Identificativo del documento** | ISMS-REF-A.8.31 |
| **Autore del documento** | Responsabile delle operazioni IT / Architettura cloud |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Responsabile delle operazioni IT (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | Operazioni IT / Architettura cloud | Riferimento tecnico iniziale per i pattern di separazione degli ambienti |

**Ciclo di revisione**: In base alle esigenze (evoluzione della tecnologia e delle piattaforme)  
**Prossima data di revisione**: [Data + 12 mesi]

**Distribuzione**: Operazioni IT, Architettura cloud, DevOps, Proprietari dei sistemi (per la consapevolezza tecnica)

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione. Non fa parte del SGSI, non stabilisce requisiti obbligatori e non deve essere utilizzato come prova di audit dell'implementazione. Tutti i requisiti vincolanti sono definiti in **ISMS-POL-A.8.31 (Politica di separazione degli ambienti)**.

---

# Scopo e ambito del documento

## Scopo

Questo documento fornisce pattern di riferimento tecnici per implementare la separazione degli ambienti su piattaforme di infrastruttura comuni. È inteso a supportare:

- La consapevolezza tecnica degli approcci di separazione specifici per piattaforma
- La comprensione dei modelli di account/abbonamento dei provider cloud
- Il contesto per le decisioni di architettura dell'infrastruttura

## Relazione con la politica SGSI

**Requisiti vincolanti**: ISMS-POL-A.8.31 definisce **COSA** è richiesto come separazione degli ambienti (isolamento di rete, separazione dell'infrastruttura, separazione delle credenziali, ecc.)

**Questo documento**: Fornisce **COME** questi requisiti possono essere implementati su piattaforme specifiche (multi-account AWS, abbonamenti Azure, namespace Kubernetes, ecc.)

---

# Pattern multi-account AWS (Amazon Web Services)

## Panoramica dell'architettura

**Struttura di AWS Organizations**:

Struttura consigliata utilizzando Unità Organizzative (OU) per raggruppare gli account per ambiente:

```
Organizzazione radice
├── OU Sicurezza
│   ├── Account Audit (log CloudTrail, reporting sulla conformità)
│   └── Account Strumenti di sicurezza (GuardDuty, SecurityHub)
├── OU Sviluppo
│   ├── Account Dev 1 (Team A - Sviluppo)
│   └── Account Servizi Dev condivisi
├── OU Test
│   ├── Account Test 1 (Team A - Test)
│   └── Account Servizi Test condivisi
├── OU Staging
│   └── Account Staging (Pre-produzione)
└── OU Produzione
    ├── Account Produzione 1 (Team A - Produzione)
    └── Servizi di produzione condivisi (Monitoraggio, backup)
```

**Perché multi-account**:

- **Confine IAM**: Le politiche IAM non possono attraversare i confini degli account (impedisce dev → prod)
- **Raggio di esplosione**: La compromissione dell'account dev non influisce sulla produzione
- **Attribuzione dei costi**: Fatturazione separata per ambiente
- **Limiti di servizio**: Quote di servizio separate per account
- **Pista di audit**: Log CloudTrail separati per account

## Separazione di rete

**VPC (Virtual Private Cloud) per ambiente**:

Blocchi CIDR consigliati:

- VPC Sviluppo: 10.1.0.0/16
- VPC Test: 10.2.0.0/16
- VPC Staging: 10.3.0.0/16
- VPC Produzione: 10.4.0.0/16

**Configurazione del peering VPC**:

Peering controllato solo tra ambienti adiacenti:

- ✅ Dev ↔ Test: Consentito (pipeline di distribuzione)
- ✅ Test ↔ Staging: Consentito (flussi di promozione)
- ✅ Staging ↔ Produzione: Consentito (automazione della distribuzione)
- ❌ Dev ↔ Produzione: **VIETATO** (la connessione diretta viola la separazione)

**Gruppi di sicurezza**:

- Rifiuto predefinito (nessun traffico in entrata a meno che non sia esplicitamente consentito)
- Gruppi di sicurezza separati per ambiente
- Gruppi di sicurezza di produzione: gestiti solo tramite Terraform/CloudFormation
- Denominazione: `{ambiente}-{servizio}-{direzione}` (es. `prod-web-entrata`)

## Controllo degli accessi (IAM)

**Modello di accesso basato sui ruoli**:

**Ruoli IAM sviluppatori** (solo nell'account Dev):
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

- MFA richiesta per l'accesso alla console
- Durata della sessione: massimo 4 ore
- Flusso di approvazione richiesto prima di AssumeRole

**AssumeRole tra account** (Pipeline di distribuzione):
```json
{
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::DEV-ACCOUNT-ID:root"},
  "Action": "sts:AssumeRole",
  "Condition": {
    "StringEquals": {"sts:ExternalId": "unique-deployment-external-id"}
  }
}
```

## Separazione dei dati

**Bucket S3** (per ambiente):

- Denominazione: `{ambiente}-{app}-{scopo}-{account-id}`
- Esempi:
  - `dev-webapp-data-123456789012`
  - `prod-webapp-data-345678901234`

**Politica del bucket S3** (produzione — impedire l'accesso tra account):
```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": "arn:aws:s3:::prod-webapp-data-*/*",
  "Condition": {
    "StringNotEquals": {"aws:PrincipalAccount": "PROD-ACCOUNT-ID"}
  }
}
```

**Database RDS**:

- Istanze RDS separate per ambiente
- RDS di produzione:
  - Crittografia a riposo (chiave AWS KMS gestita dal cliente)
  - Backup automatici (conservazione 7-35 giorni)
  - Distribuzione Multi-AZ (alta disponibilità)
  - Monitoraggio avanzato abilitato
- RDS Dev/Test:
  - Tipi di istanza più piccoli accettabili
  - Single-AZ accettabile
  - Conservazione dei backup più breve (7 giorni)

**AWS Secrets Manager**:

- Segreti separati per ambiente
- Convenzione di denominazione: `{ambiente}/{servizio}/{segreto}`
- Segreti di produzione: rotazione automatica abilitata (30-90 giorni)
- Accesso ai segreti tra account: **VIETATO**

---

# Pattern multi-abbonamento Azure

## Panoramica dell'architettura

**Gerarchia dei gruppi di gestione Azure**:

```
Gruppo radice del tenant
├── Gruppo di gestione Sicurezza
│   ├── Abbonamento Audit
│   └── Abbonamento Strumenti di sicurezza
├── Gruppo di gestione Sviluppo
│   └── Abbonamento Dev - Team A
├── Gruppo di gestione Test
│   └── Abbonamento Test - Team A
├── Gruppo di gestione Staging
│   └── Abbonamento Staging - Team A
└── Gruppo di gestione Produzione
    └── Abbonamento Produzione - Team A
```

**Perché multi-abbonamento**:

- **Applicazione dei criteri Azure**: I criteri applicati a livello di gruppo di gestione si propagano agli abbonamenti
- **Confine RBAC**: Azure RBAC non attraversa i confini degli abbonamenti
- **Gestione dei costi**: Fatturazione e budget separati per abbonamento
- **Limiti di servizio**: Limiti di quota separati per abbonamento

## Separazione di rete

**Reti virtuali (VNet)** per abbonamento:

- VNet Sviluppo: 10.10.0.0/16
- VNet Test: 10.20.0.0/16
- VNet Staging: 10.30.0.0/16
- VNet Produzione: 10.40.0.0/16

**Gruppi di sicurezza di rete (NSG)**:

- Rifiutare tutto il traffico in entrata per impostazione predefinita
- Regole di autorizzazione esplicite per il traffico richiesto
- NSG di produzione: gestiti tramite Criteri di Azure

**Peering VNet**:

- Topologia hub-and-spoke (VNet hub centrale per i servizi condivisi)
- VNet spoke (Dev, Test, Staging, Prod) si collegano solo all'hub
- Routing transitivo disabilitato (Dev non può raggiungere Prod tramite l'hub)

## Controllo degli accessi (Azure RBAC)

**Assegnazioni di ruoli per ambiente**:

**Sviluppatori** (Abbonamento Dev):

- Ruolo: Contributor (può creare/modificare risorse)
- Ambito: Gruppi di risorse nell'abbonamento Dev
- Non può accedere agli abbonamenti Test/Staging/Prod

**Team QA** (Abbonamento Test):

- Ruolo: Reader + accesso specifico all'applicazione

**Operazioni** (Abbonamento Produzione):

- Ruolo: Contributor (tramite Privileged Identity Management — PIM)
- Richiede: Attivazione JIT (Just-in-Time) + MFA + approvazione
- Sessione: massimo 4 ore
- Audit: Tutte le azioni registrate

**Accesso condizionale Azure AD**:

L'accesso alla produzione richiede:

- Dispositivo gestito (conformità Intune)
- Autenticazione multi-fattore (MFA)
- Posizione di rete attendibile
- Criteri basati sul rischio (Azure AD Identity Protection)

## Separazione dei dati

**Account di archiviazione Azure**:

- Denominazione: `{env}{app}{scopo}{id_univoco}` (max 24 caratteri)
- Esempi:
  - `devwebappdata001abc`
  - `prodwebappdata003pqr`

**Azure SQL Database**:

- Server Azure SQL separati per ambiente
- SQL di produzione:
  - Transparent Data Encryption (TDE) abilitata
  - Backup automatici
  - Geo-replica per il ripristino di emergenza
  - Advanced Threat Protection abilitata

**Azure Key Vault**:

- Key Vault separati per ambiente
- Denominazione: `{ambiente}-{app}-kv` (es. `prod-webapp-kv`)
- Key Vault di produzione:
  - Eliminazione reversibile abilitata (conservazione 90 giorni)
  - Protezione dall'eliminazione abilitata
  - Endpoint privato (nessun accesso pubblico)
  - Regole del firewall (consentire solo VNet specifiche)

## Applicazione dei criteri Azure

**Criteri del gruppo di gestione Produzione**:
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

# Pattern multi-progetto GCP (Google Cloud Platform)

## Panoramica dell'architettura

**Gerarchia dell'organizzazione GCP**:

```
Organizzazione (example.com)
├── Cartella Sicurezza
│   ├── Progetto Audit (aggregazione Cloud Logging)
│   └── Progetto Strumenti di sicurezza
├── Cartella Sviluppo
│   └── Progetto Dev - Team A
├── Cartella Test
│   └── Progetto Test - Team A
├── Cartella Staging
│   └── Progetto Staging - Team A
└── Cartella Produzione
    └── Progetto Produzione - Team A
```

## Separazione di rete

**Reti VPC** (per progetto):

- VPC Sviluppo: 10.100.0.0/16
- VPC Test: 10.110.0.0/16
- VPC Staging: 10.120.0.0/16
- VPC Produzione: 10.130.0.0/16

**Regole firewall**:

- Rifiuto predefinito di tutto il traffico in entrata
- Regole di autorizzazione esplicite richieste
- Regole firewall di produzione: gestite tramite Terraform

## Controllo degli accessi (Cloud IAM)

**Ruoli IAM per ambiente**:

**Sviluppatori** (Progetto Dev): `roles/editor` — solo ambito progetto dev

**Operazioni** (Progetto Produzione): `roles/compute.admin` + `roles/storage.admin` — accesso limitato, basato su tempo (4 ore)

**Account di servizio** (per le applicazioni):

- Account di servizio separati per ambiente
- Denominazione: `{env}-{app}-sa@{project-id}.iam.gserviceaccount.com`
- Account di servizio di produzione: rotazione delle chiavi obbligatoria (90 giorni)

## Separazione dei dati

**Bucket Cloud Storage**:

- Produzione:
  - Versioning abilitato
  - Criteri di conservazione (minimo 30 giorni)
  - Chiavi di crittografia gestite dal cliente (Cloud KMS)

**Cloud SQL**:

- Produzione:
  - Backup automatici
  - Alta disponibilità (regionale)
  - Solo IP privato (nessun IP pubblico)

**Secret Manager**:

- Segreti separati per progetto
- Denominazione: `{ambiente}_{servizio}_{segreto}`
- Segreti di produzione: rotazione automatica

---

# Separazione degli ambienti Kubernetes

## Opzioni di architettura

**Opzione 1: Separazione basata su namespace** (cluster singolo):
```
Cluster Kubernetes (condiviso)
├── namespace dev
├── namespace test
├── namespace staging
└── namespace production
```

**Pro**: Efficienza delle risorse, gestione semplificata  
**Contro**: Isolamento più debole (la produzione condivide il piano di controllo con dev)  
**Caso d'uso**: Organizzazioni piccole, applicazioni a basso rischio

**Opzione 2: Separazione basata su cluster** (cluster separati):
```
Cluster Sviluppo
Cluster Test
Cluster Staging
Cluster Produzione (separato)
```

**Pro**: Isolamento forte (piano di controllo della produzione separato)  
**Contro**: Maggiore carico operativo, costo più elevato  
**Caso d'uso**: Grandi organizzazioni, applicazioni ad alto rischio, requisiti normativi

**Raccomandato**: Separazione basata su cluster per la produzione, basata su namespace per dev/test/staging.

## Separazione basata su namespace

**Configurazione dei namespace**:

```yaml
# Namespace di produzione con quote di risorse
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
```

**Criteri di rete** (isolare i namespace):

```yaml
# Rifiutare tutto il traffico verso il namespace di produzione tranne dall'ingress
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
# Gli sviluppatori possono accedere solo al namespace dev
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

## Separazione basata su cluster

**Cluster EKS/AKS/GKE separati**:

**Cluster di sviluppo**:

- Auto-scaling: 2-10 nodi
- Tipi di istanza più piccoli (ottimizzazione dei costi)

**Cluster di produzione**:

- Auto-scaling: 5-50 nodi
- Istanze ottimizzate per le prestazioni
- Alta disponibilità: pool di nodi multi-AZ
- Osservabilità completa (Prometheus, Grafana, tracciamento Jaeger)

**Standard di sicurezza dei pod**:

- Produzione: `restricted` (sicurezza massima)
- Staging: `restricted`
- Test: `baseline`
- Dev: `privileged` (gli sviluppatori hanno bisogno di flessibilità)

---

# Infrastruttura on-premise / Tradizionale

## Separazione basata su VLAN

**Segmentazione di rete**:

```
Rete principale (192.168.0.0/16)
├── VLAN 10: Sviluppo (192.168.10.0/24)
├── VLAN 20: Test (192.168.20.0/24)
├── VLAN 30: Staging (192.168.30.0/24)
└── VLAN 40: Produzione (192.168.40.0/24)
```

**Regole firewall tra VLAN**:

- Rifiuto predefinito di tutto il traffico
- ACL (Liste di controllo degli accessi) per il traffico di distribuzione controllato
- VLAN Produzione: nessun traffico in entrata dalle VLAN dev/test

## Architettura di rete multi-livello

```
Internet
  ↓
Firewall (DMZ)
  ↓
VLAN Livello Web (esposta al pubblico)
  ↓
Firewall
  ↓
VLAN Livello Applicazione
  ↓
Firewall
  ↓
VLAN Livello Database (più restrittiva)
```

---

# Framework di riferimento

## Framework decisionale — Scegliere l'approccio di separazione

| Fattore | Per namespace | Per account/abbonamento | Separazione fisica |
|---------|---------------|------------------------|--------------------|
| **Costo** | Basso (risorse condivise) | Medio (account separati) | Alto (infrastruttura duplicata) |
| **Isolamento** | Medio (solo logico) | Alto (confini dell'account) | Massimo (fisico) |
| **Conformità** | Rischio basso-medio | Rischio alto accettabile | Massimo (finanza, sanità) |
| **Complessità** | Bassa (cluster/account singolo) | Media (gestione multi-account) | Alta (data center separati) |
| **Consigliato per** | Org. piccole, basso rischio | La maggior parte delle organizzazioni | Settori regolamentati |

## Percorso di migrazione

**Fase 1**: Iniziare con la separazione basata su namespace (rapida da implementare)  
**Fase 2**: Migrare alla separazione per account/abbonamento (isolamento più forte)  
**Fase 3**: Considerare la separazione fisica solo per la produzione (se requisito normativo)

---

**FINE DEL DOCUMENTO DI RIFERIMENTO**

---

*Questo riferimento tecnico supporta ISMS-POL-A.8.31. Le decisioni di implementazione devono essere basate sulla valutazione del rischio organizzativo e approvate dal RSSI.*
<!-- QA_VERIFIED: 2026-04-04 -->

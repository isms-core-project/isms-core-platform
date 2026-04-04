<!-- ISMS-CORE:REF:ISMS-REF-A.5.19-23-IT-registro-fornitori-cloud:framework:REF:a.5.19-23 -->
**ISMS-REF-A.5.19-23 — Registro di riferimento dei fornitori di servizi cloud**
**Riferimento autorevole per la valutazione dei fornitori cloud e SaaS di terze parti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Registro dei fornitori di servizi cloud |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-A.5.19-23 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | RSSI (Riferimento tecnico — Nessuna approvazione esecutiva richiesta) |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Semestrale (o in caso di cambiamenti significativi nel panorama dei fornitori)
**Approvatori**: RSSI; Responsabile Operazioni IT; Acquisti/Gestione fornitori
**Distribuito a**: Parti interessate SGSI, proprietari di sistemi, acquisti, gestione fornitori
**Referenziato da**: ISMS-POL-A.5.19-23, ISMS-POL-A.8.10

---

# Scopo

Il presente documento fornisce il **registro di riferimento autorevole** dei fornitori di servizi cloud e delle piattaforme SaaS comunemente presenti negli ambienti IT organizzativi.

**Utilizzo**: Pre-compilare i classeur di valutazione (A.5.23, A.8.10, ecc.); standardizzare la categorizzazione dei fornitori nel SGSI; abilitare la valutazione coerente del rischio dei fornitori; supportare la conformità alla cancellazione e conservazione dei dati (A.8.10).

**Principio chiave**: Questo registro è **neutro nei confronti dei fornitori** ai fini della politica — cataloga i fornitori per la valutazione, non per l'approvazione. Le organizzazioni documentano il PROPRIO utilizzo e le PROPRIE configurazioni specifiche.

---

# Quadro di classificazione dei fornitori

## Modelli di servizio

| Codice | Modello | Descrizione |
|--------|---------|-------------|
| **IaaS** | Infrastruttura come servizio | Macchine virtuali, storage, rete |
| **PaaS** | Piattaforma come servizio | Piattaforme di sviluppo, runtime gestiti |
| **SaaS** | Software come servizio | Applicazioni per l'utente finale |
| **DBaaS** | Database come servizio | Servizi di database gestiti |
| **BaaS** | Backup come servizio | Backup e ripristino gestiti |
| **SECaaS** | Sicurezza come servizio | Servizi di sicurezza gestiti |
| **IDaaS** | Identità come servizio | Gestione delle identità e degli accessi |
| **CDN** | Rete di distribuzione dei contenuti | Caching e distribuzione edge |

## Livelli di priorità di valutazione

| Livello | Priorità | Criteri | Frequenza di valutazione |
|---------|----------|---------|--------------------------|
| **Livello 1** | Critico | Hyperscaler, infrastruttura core | Trimestrale |
| **Livello 2** | Critico | Principali piattaforme enterprise | Trimestrale |
| **Livello 3** | Alto | Fornitori infrastruttura e sicurezza | Semestrale |
| **Livello 4** | Alto | Specialisti backup e storage | Semestrale |
| **Livello 5** | Alto | Comunicazione e collaborazione | Semestrale |
| **Livello 6** | Medio | Piattaforme DevOps e sviluppo | Annuale |
| **Livello 7** | Medio | Database e analisi gestiti | Annuale |
| **Livello 8** | Alto | Sicurezza e identità (sensibili) | Semestrale |
| **Livello 9** | Alto | HR e Finanza (ricchi di DCP) | Semestrale |
| **Livello 10** | Regionale | Fornitori regionali Svizzera/UE | Semestrale |

## Indicatori di sensibilità dei dati

| Indicatore | Descrizione | Priorità di cancellazione |
|------------|-------------|--------------------------|
| 🔴 **DCP** | Dati personali | Critica (RGPD Art. 17 / nLPD) |
| 🟠 **PCI** | Dati di carte di pagamento | Critica (PCI DSS) |
| 🟡 **RIS** | Dati aziendali riservati | Alta |
| 🟢 **INT** | Dati interni | Media |
| ⚪ **PUB** | Dati pubblici | Bassa |

---

# Registro dei fornitori

## Livello 1: Hyperscaler (Critico)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **Microsoft Azure** | IaaS, PaaS | USA (regioni UE) | Calcolo, Storage, Database, IA | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Microsoft 365** | SaaS | USA (regioni UE) | Exchange, SharePoint, OneDrive, Teams | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Amazon Web Services (AWS)** | IaaS, PaaS | USA (regioni UE) | EC2, S3, RDS, Glacier | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Google Cloud Platform (GCP)** | IaaS, PaaS | USA (regioni UE) | Calcolo, Storage, BigQuery | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Google Workspace** | SaaS | USA (regioni UE) | Gmail, Drive, Documenti, Meet | 🔴🟡 | A.5.23, A.8.10 |

**Note di valutazione**: Tutti i fornitori di Livello 1 offrono opzioni di residenza dei dati nell'UE; richiedono Accordi di trattamento dei dati (DPA) con SCC; le capacità di cancellazione sono ben documentate ma verificare la conservazione nei backup; la cancellazione crittografica è generalmente disponibile.

---

## Livello 2: Principali fornitori enterprise (Critico)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **Oracle Cloud (OCI)** | IaaS, PaaS, SaaS | USA (regioni UE) | Database, Calcolo, ERP, HCM | 🔴🟡 | A.5.23, A.8.10 |
| **IBM Cloud** | IaaS, PaaS | USA (regioni UE) | Storage, IA, Database | 🟡 | A.5.23, A.8.10 |
| **SAP** | SaaS, PaaS | Germania | S/4HANA, SuccessFactors, BTP | 🔴🟡 | A.5.23, A.8.10 |
| **Salesforce** | SaaS | USA (regioni UE) | CRM, Marketing, Service Cloud | 🔴🟡 | A.5.23, A.8.10 |
| **ServiceNow** | SaaS | USA (regioni UE) | ITSM, Flussi di lavoro, CMDB | 🟡 | A.5.23, A.8.10 |

---

## Livello 3: Infrastruttura e sicurezza (Alto)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **Cloudflare** | CDN, Sicurezza, IaaS | USA | CDN, WAF, R2 Storage, Workers | 🟡 | A.5.23, A.8.10, A.8.23 |
| **Akamai** | CDN, Sicurezza | USA | CDN, WAF, Edge Security | 🟡 | A.5.23, A.8.23 |
| **OVHcloud** | IaaS | Francia | Hosting, Storage, Cloud | 🟡 | A.5.23, A.8.10 |
| **Hetzner** | IaaS | Germania | Hosting, Storage, Cloud | 🟡 | A.5.23, A.8.10 |
| **DigitalOcean** | IaaS | USA | Droplets, Spaces, Database | 🟡 | A.5.23, A.8.10 |
| **Fastly** | CDN | USA | Edge Compute, CDN | 🟡 | A.5.23 |
| **Linode (Akamai)** | IaaS | USA | VM, Storage, Kubernetes | 🟡 | A.5.23, A.8.10 |
| **Vultr** | IaaS | USA | VM, Storage, Kubernetes | 🟡 | A.5.23, A.8.10 |

**Note di valutazione**: OVHcloud e Hetzner hanno sede nell'UE (favorevoli per il RGPD); i fornitori CDN mettono in cache i dati sull'edge — importante la propagazione della cancellazione.

---

## Livello 4: Specialisti backup e storage (Alto)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **Veeam Cloud Connect** | BaaS | USA/Svizzera | Repository di backup | 🔴🟡 | A.5.23, A.8.10 |
| **Commvault** | BaaS | USA | Backup, Archiviazione, Ripristino | 🔴🟡 | A.5.23, A.8.10 |
| **Rubrik** | BaaS | USA | Backup, Ripristino ransomware | 🔴🟡 | A.5.23, A.8.10 |
| **Cohesity** | BaaS | USA | Backup, Gestione dati | 🔴🟡 | A.5.23, A.8.10 |
| **Wasabi** | Storage | USA | Storage compatibile S3 | 🟡 | A.5.23, A.8.10 |
| **Backblaze B2** | Storage | USA | Storage compatibile S3 | 🟡 | A.5.23, A.8.10 |
| **Dropbox Business** | SaaS | USA | Sincronizzazione file, Collaborazione | 🔴🟡 | A.5.23, A.8.10 |
| **Box** | SaaS | USA | Gestione dei contenuti | 🔴🟡 | A.5.23, A.8.10 |

**Note di valutazione**: I fornitori di backup sono CRITICI per A.8.10 — i dati persistono nei backup dopo la cancellazione primaria; verificare che i periodi di conservazione dei backup siano allineati con i requisiti di cancellazione; Veeam ha una presenza svizzera (favorevole per le organizzazioni svizzere).

---

## Livello 5: Comunicazione e collaborazione (Alto)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **Slack** | SaaS | USA | Messaggistica, File, Integrazioni | 🔴🟡 | A.5.23, A.8.10 |
| **Zoom** | SaaS | USA | Video, Registrazioni, Chat | 🔴🟡 | A.5.23, A.8.10 |
| **Cisco Webex** | SaaS | USA | Video, Messaggistica, Riunioni | 🔴🟡 | A.5.23, A.8.10 |
| **Atlassian Cloud** | SaaS | Australia | Jira, Confluence, Bitbucket | 🟡 | A.5.23, A.8.10 |
| **Notion** | SaaS | USA | Spazi di lavoro, Documentazione | 🟡 | A.5.23, A.8.10 |
| **Asana** | SaaS | USA | Progetti, Attività | 🟡 | A.5.23, A.8.10 |
| **Monday.com** | SaaS | Israele | Progetti, Flussi di lavoro | 🟡 | A.5.23, A.8.10 |

---

## Livello 6: Piattaforme DevOps e sviluppo (Medio)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **GitHub** | SaaS | USA (Microsoft) | Repository, Actions, Pacchetti | 🟡 | A.5.23, A.8.10 |
| **GitLab** | SaaS/Self-hosted | USA/Paesi Bassi | Repository, CI/CD, Registry | 🟡 | A.5.23, A.8.10 |
| **Bitbucket** | SaaS | Australia (Atlassian) | Repository, Pipeline | 🟡 | A.5.23, A.8.10 |
| **Docker Hub** | SaaS | USA | Immagini container | 🟡 | A.5.23, A.8.10 |
| **JFrog** | SaaS | USA/Israele | Artifact, Container Registry | 🟡 | A.5.23, A.8.10 |
| **Terraform Cloud** | SaaS | USA (HashiCorp) | File di stato, Spazi di lavoro | 🟡🔴 | A.5.23, A.8.10 |

**Note di valutazione**: I repository di codice sorgente possono contenere segreti; i file di stato Terraform contengono spesso dettagli sensibili dell'infrastruttura; GitLab ha un'entità UE (Paesi Bassi).

---

## Livello 7: Database e analisi (Medio)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **MongoDB Atlas** | DBaaS | USA | Database documentali | 🔴🟡 | A.5.23, A.8.10 |
| **Snowflake** | SaaS | USA | Data Warehouse | 🔴🟡 | A.5.23, A.8.10 |
| **Databricks** | SaaS | USA | Analisi, Lakehouse | 🔴🟡 | A.5.23, A.8.10 |
| **Elastic Cloud** | SaaS | USA/Paesi Bassi | Elasticsearch, Log | 🔴🟡 | A.5.23, A.8.10, A.8.16 |
| **Redis Cloud** | DBaaS | USA | Cache, Database | 🟡 | A.5.23, A.8.10 |
| **PlanetScale** | DBaaS | USA | Compatibile MySQL | 🔴🟡 | A.5.23, A.8.10 |
| **Supabase** | DBaaS | USA | PostgreSQL, Storage | 🔴🟡 | A.5.23, A.8.10 |

---

## Livello 8: Sicurezza e identità (Alto — Sensibili)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **Okta** | IDaaS | USA | Identità, SSO, AMF | 🔴 | A.5.23, A.8.10, A.5.15 |
| **Auth0** | IDaaS | USA (Okta) | Identità, Gestione utenti | 🔴 | A.5.23, A.8.10, A.5.15 |
| **CrowdStrike** | SECaaS | USA | EDR, Threat Intelligence | 🟡 | A.5.23, A.8.10 |
| **SentinelOne** | SECaaS | USA/Israele | EDR, XDR | 🟡 | A.5.23, A.8.10 |
| **Splunk Cloud** | SaaS | USA (Cisco) | Aggregazione log, SIEM | 🔴🟡 | A.5.23, A.8.10, A.8.16 |
| **Datadog** | SaaS | USA | Monitoraggio, Log, APM | 🟡 | A.5.23, A.8.10, A.8.16 |
| **New Relic** | SaaS | USA | APM, Log, Monitoraggio | 🟡 | A.5.23, A.8.10 |

---

## Livello 9: HR e Finanza (Alto — Ricchi di DCP)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **Workday** | SaaS | USA | HR, Finanza, Pianificazione | 🔴 | A.5.23, A.8.10 |
| **ADP** | SaaS | USA | Paghe, HR | 🔴 | A.5.23, A.8.10 |
| **BambooHR** | SaaS | USA | Gestione HR | 🔴 | A.5.23, A.8.10 |
| **Personio** | SaaS | Germania | HR (focus UE) | 🔴 | A.5.23, A.8.10 |
| **Xero** | SaaS | Nuova Zelanda | Contabilità | 🔴🟠 | A.5.23, A.8.10 |
| **QuickBooks Online** | SaaS | USA (Intuit) | Contabilità | 🔴🟠 | A.5.23, A.8.10 |
| **Stripe** | SaaS | USA/Irlanda | Pagamenti | 🔴🟠 | A.5.23, A.8.10 |
| **PayPal** | SaaS | USA | Pagamenti | 🔴🟠 | A.5.23, A.8.10 |

**Note di valutazione**: I sistemi HR contengono DCP estesi dei dipendenti — si applicano i diritti di cancellazione RGPD; Personio ha sede nell'UE (Germania); i processori di pagamento (Stripe, PayPal) hanno requisiti di conservazione PCI DSS.

---

## Livello 10: Fornitori regionali Svizzera/UE (Regionale)

| Fornitore | Modello | Sede | Servizi chiave | Sensibilità | Rilevanza SGSI |
|-----------|---------|------|----------------|------------|----------------|
| **Exoscale** | IaaS | Svizzera | Calcolo, Storage, Kubernetes | 🟡 | A.5.23, A.8.10 |
| **Infomaniak** | IaaS, SaaS | Svizzera | Hosting, kDrive, Mail | 🔴🟡 | A.5.23, A.8.10 |
| **Proton (ProtonMail/Drive)** | SaaS | Svizzera | Email cifrata, Storage | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Tresorit** | SaaS | Svizzera | Storage cifrato | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **STACKIT** | IaaS | Germania | Cloud (Gruppo Schwarz) | 🟡 | A.5.23, A.8.10 |
| **IONOS** | IaaS | Germania | Hosting, Cloud | 🟡 | A.5.23, A.8.10 |
| **Scaleway** | IaaS | Francia | Cloud, Storage | 🟡 | A.5.23, A.8.10 |

**Note di valutazione**: I fornitori svizzeri (Exoscale, Infomaniak, Proton, Tresorit) sono soggetti alla nLPD svizzera; nessuna esposizione al CLOUD Act statunitense per i fornitori solo svizzeri; Proton e Tresorit usano la cifratura end-to-end.

---

# Riepilogo del registro

## Conteggio fornitori per livello

| Livello | Categoria | Conteggio | Priorità |
|---------|-----------|-----------|----------|
| 1 | Hyperscaler | 5 | Critico |
| 2 | Fornitori enterprise | 5 | Critico |
| 3 | Infrastruttura e sicurezza | 8 | Alto |
| 4 | Backup e storage | 8 | Alto |
| 5 | Collaborazione | 7 | Alto |
| 6 | DevOps | 6 | Medio |
| 7 | Database e analisi | 7 | Medio |
| 8 | Sicurezza e identità | 7 | Alto |
| 9 | HR e Finanza | 8 | Alto |
| 10 | Regionali Svizzera/UE | 7 | Regionale |
| **TOTALE** | | **68** | |

## Conteggio per regione della sede

| Regione | Conteggio | Note |
|---------|-----------|------|
| USA | 48 | La maggior parte richiede DPA con SCC per dati UE/CH |
| UE (Germania, Francia, Paesi Bassi, Irlanda) | 10 | Nativi RGPD |
| Svizzera | 4 | Nativi nLPD, nessun CLOUD Act |
| Altro (Israele, Australia, Nuova Zelanda) | 6 | Verificare le decisioni di adeguatezza |

---

# Integrazione nella valutazione

## Controlli SGSI correlati

| Controllo | Punto di integrazione |
|-----------|----------------------|
| **A.5.19** | Sicurezza delle informazioni nelle relazioni con i fornitori |
| **A.5.20** | Considerazione della sicurezza negli accordi con i fornitori |
| **A.5.21** | Gestione della sicurezza nella catena di approvvigionamento TIC |
| **A.5.22** | Monitoraggio e gestione dei cambiamenti dei servizi |
| **A.5.23** | Sicurezza delle informazioni per i servizi cloud |
| **A.8.10** | Cancellazione delle informazioni |
| **A.8.24** | Utilizzo della crittografia |

## Pre-compilazione dei classeur Excel

Questo registro DEVE essere usato per pre-compilare: ISMS-IMP-A.5.19-23.x (classeur di valutazione); ISMS-IMP-A.8.10.3 (valutazione della cancellazione da terzi e cloud); Registro dei rischi dei fornitori; Registro dei trattamenti (RGPD art. 30).

---

# Appendice A: Scheda di riferimento rapido

```
┌────────────────────────────────────────────────────────────────────┐
│         RIFERIMENTO RAPIDO VALUTAZIONE FORNITORI CLOUD             │
├────────────────────────────────────────────────────────────────────┤
│  CRITICO (Valutazione trimestrale)                                 │
│  • Livello 1: Azure, M365, AWS, GCP, Google Workspace              │
│  • Livello 2: Oracle, IBM, SAP, Salesforce, ServiceNow             │
│                                                                    │
│  ALTA PRIORITÀ (Valutazione semestrale)                            │
│  • Livello 3: Cloudflare, Akamai, OVH, Hetzner                    │
│  • Livello 4: Veeam, Rubrik, Wasabi, Dropbox, Box                 │
│  • Livello 5: Slack, Zoom, Atlassian, Teams                       │
│  • Livello 8: Okta, CrowdStrike, Splunk, Datadog                  │
│  • Livello 9: Workday, Personio, Stripe                           │
│                                                                    │
│  PRIORITÀ MEDIA (Valutazione annuale)                              │
│  • Livello 6: GitHub, GitLab, Docker Hub                          │
│  • Livello 7: MongoDB, Snowflake, Elastic                         │
│                                                                    │
│  FORNITORI SVIZZERA/UE PREFERITI                                   │
│  • CH: Exoscale, Infomaniak, Proton, Tresorit                     │
│  • DE: SAP, Hetzner, STACKIT, IONOS                               │
│  • FR: OVHcloud, Scaleway                                         │
│  • NL: GitLab, Elastic                                            │
│  • IE: Stripe                                                      │
├────────────────────────────────────────────────────────────────────┤
│  🔴 DCP = Diritti di cancellazione RGPD Art. 17 / nLPD applicabili│
│  🟠 PCI = Requisiti di conservazione carte di pagamento            │
│  🟡 RIS = Cancellazione standard secondo la politica di conservaz. │
└────────────────────────────────────────────────────────────────────┘
```

---

**FINE DEL DOCUMENTO**

*«Il vostro fornitore cloud dice "prendiamo la sicurezza sul serio". Questo registro aiuta a verificare cosa significa concretamente per I VOSTRI dati.»*

<!-- QA_VERIFIED: 2026-04-03 -->

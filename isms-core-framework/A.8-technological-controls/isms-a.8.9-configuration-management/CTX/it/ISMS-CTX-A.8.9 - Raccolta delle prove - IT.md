<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.9-IT-evidence-collection:framework:CTX:a.8.9 -->
**ISMS-CTX-A.8.9 — Raccolta delle prove**

**Controllo del documento**

| Attributo | Valore |
|-----------|--------|
| **Identificativo del documento** | ISMS-CTX-A.8.9-raccolta-prove |
| **Versione** | 1.0 |
| **Tipo di documento** | Riferimento tecnico (NON SGSI) |
| **Politica correlata** | ISMS-POL-A.8.9 (Tutte le sezioni) |
| **Scopo** | Fornire una struttura standardizzata del repository delle prove per la dimostrazione della conformità e la preparazione agli audit del Controllo A.8.9 della ISO 27001:2022 |
| **Destinatari** | Responsabili della configurazione, Amministratori di sistema, Revisori, Responsabili della conformità, Custodi delle prove |
| **Ciclo di revisione** | Annuale (o in caso di modifica dei requisiti di audit) |
| **Data** | [Data] |

**Approvatori**: Responsabile della configurazione (primario), Architetto della sicurezza (revisione tecnica). NESSUNA approvazione esecutiva richiesta (NON SGSI).

**Documenti correlati**: ISMS-POL-A.8.9, ISMS-CTX-A.8.9, ISMS-IMP-A.8.9-UG, ISMS-IMP-A.8.9-TG

---

## ⚠️ CRITICO: Stato del documento

**QUESTO DOCUMENTO NON FA PARTE DEL SGSI.**

**QUESTO DOCUMENTO NON DEFINISCE REQUISITI OBBLIGATORI.**

**QUESTO DOCUMENTO NON STABILISCE OBBLIGHI VINCOLANTI.**

**TUTTI I REQUISITI VINCOLANTI SONO DEFINITI IN ISMS-POL-A.8.9.**

**Si tratta di riferimento tecnico e guida operativa esclusivamente per la raccolta delle prove, l'organizzazione e la preparazione agli audit.**

---

## Panoramica

Questa guida definisce la struttura standardizzata del repository delle prove per il Controllo A.8.9 della ISO 27001:2022 (Gestione della configurazione). Una corretta organizzazione delle prove consente audit efficienti, dimostra l'efficacia dei controlli e supporta la verifica della conformità.

**Ubicazione del repository**: [L'organizzazione deve definire — es. SharePoint/Unità di rete/Sistema di gestione documentale]

**Controllo degli accessi**: Il repository delle prove DEVE essere controllato nell'accesso: accesso in lettura per revisori e responsabili della conformità, accesso in scrittura limitato al team di Gestione della configurazione.

**Periodo di conservazione**: Minimo 3 anni per i requisiti della ISO 27001:2022; più lungo se richiesto da normative specifiche del settore.

---

## Struttura del repository delle prove

```
Prove/
  ISMS-A.8.9-Configurazione-Baseline/
  ISMS-A.8.9-Controllo-Modifiche/
  ISMS-A.8.9-Monitoraggio-Configurazione/
  ISMS-A.8.9-Hardening-Sicurezza/
```

---

## Prove sulla configurazione baseline

### Struttura della directory

**Prove/ISMS-A.8.9-Configurazione-Baseline/**

#### 1. Inventario-Asset/
Contiene l'inventario completo degli asset che dimostra l'ambito della copertura della baseline.

**File richiesti**:

- `Export-CMDB-AAAAMMGG.xlsx` — Export completo del Configuration Management Database
- `Risultati-Scansione-Rete-AAAAMMGG.pdf` — Risultati della scansione di scoperta della rete
- `Classificazioni-Criticità-Asset.pdf` — Classificazioni dei livelli degli asset (Livello 1-4)
- `Inventario-Asset-Cloud-AWS-AAAAMMGG.csv` — Inventario asset AWS
- `Inventario-Asset-Cloud-Azure-AAAAMMGG.csv` — Inventario asset Azure
- `Report-Riconciliazione-Inventario-Asset.xlsx` — Confronto tra più fonti

**Scopo delle prove**: Dimostra che esiste un inventario completo degli asset e che gli obiettivi di copertura della baseline sono misurabili.

#### 2. Documentazione-Baseline/
Contiene le configurazioni baseline approvate organizzate per tipo di asset.

**Sottodirectory**:

**Windows-Server/**

- `BL-WIN2022-DC-v2.1.docx` — Baseline Windows Server 2022 Domain Controller
- `BL-WIN2022-FS-v1.5.docx` — Baseline Windows Server 2022 File Server
- `BL-WIN2022-APP-v1.8.docx` — Baseline Windows Server 2022 Application Server
- `Mappatura-CIS-Windows-Server-2022.xlsx` — Mappatura CIS Benchmark

**Linux-Unix/**

- `BL-RHEL9-STD-v1.3.pdf` — Baseline Red Hat Enterprise Linux 9
- `BL-UBUNTU2204-WEB-v2.0.pdf` — Baseline Ubuntu 22.04 Web Server
- `BL-SUSE15-DB-v1.2.pdf` — Baseline SUSE Linux 15 Database Server
- `Mappatura-CIS-Linux-Benchmark.xlsx` — Mappatura CIS Benchmark

**Dispositivi-Rete/**

- `BL-Cisco-ASA-FW-v3.1.pdf` — Baseline Firewall Cisco ASA
- `BL-Palo-Alto-NGFW-v2.5.pdf` — Baseline Firewall Next-Gen Palo Alto
- `BL-Cisco-Switch-IOS-v1.9.pdf` — Baseline Cisco Switch IOS
- `BL-F5-LoadBalancer-v1.4.pdf` — Baseline F5 Load Balancer

**Piattaforme-Cloud/**

- `BL-AWS-EC2-Linux-v2.2.pdf` — Baseline istanza AWS EC2 Linux
- `BL-AWS-RDS-MySQL-v1.6.pdf` — Baseline AWS RDS MySQL
- `BL-Azure-VM-Windows-v1.8.pdf` — Baseline Azure Windows VM
- `Mappatura-CIS-AWS-Foundations-Benchmark.xlsx` — Mappatura CIS AWS

**Database/**

- `BL-SQLServer2022-v1.7.pdf` — Baseline SQL Server 2022
- `BL-PostgreSQL15-v1.4.pdf` — Baseline PostgreSQL 15
- `BL-Oracle19c-v2.1.pdf` — Baseline Oracle 19c
- `Mappatura-DISA-STIG-Database.xlsx` — Mappatura DISA STIG

**Container/**

- `BL-Docker-v1.5.pdf` — Baseline Docker
- `BL-Kubernetes-v2.0.pdf` — Baseline Kubernetes
- `Mappatura-CIS-Kubernetes-Benchmark.xlsx` — Mappatura CIS Kubernetes

**Convenzione di denominazione**: `BL-[Tecnologia]-[Ruolo]-v[Versione].pdf`

- BL = Baseline
- Tecnologia = Prodotto/Piattaforma (WIN2022, RHEL9, ecc.)
- Ruolo = Scopo (DC, WEB, APP, DB, ecc.)
- Versione = Versionamento semantico (major.minor)

**Scopo delle prove**: Dimostra che le baseline esistono, sono documentate e fanno riferimento a standard riconosciuti.

#### 3. Immagini-Golden/
Contiene l'inventario delle immagini golden e i relativi documenti di approvazione.

**File richiesti**:

- `Registro-Inventario-Immagini.xlsx` — Elenco principale di tutte le immagini golden
- `WIN2022-STD-v2.1-20240115-RecordApprovazione.pdf` — Approvazione dell'immagine con firme
- `RHEL9-SEC-v1.3-20240120-RecordApprovazione.pdf` — Approvazione dell'immagine con firme

**Manifesti-Build-Immagini/** (codice IaC per build riproducibili):

- `WIN2022-STD-v2.1-BuildManifest.yaml` — Definizione di build automatizzata
- `RHEL9-SEC-v1.3-BuildManifest.yaml` — Definizione di build automatizzata

**Scansioni-Vulnerabilità/** (validazione della sicurezza pre-approvazione):

- `WIN2022-STD-v2.1-ScansVuln-AAAAMMGG.pdf` — Report di scansione delle vulnerabilità
- `RHEL9-SEC-v1.3-ScansVuln-AAAAMMGG.pdf` — Report di scansione delle vulnerabilità

**Scopo delle prove**: Dimostra che le immagini golden implementano le baseline e sono validate per la sicurezza prima dell'uso in produzione.

#### 4. Record-Approvazione/
Contiene le approvazioni formali per le baseline.

**File richiesti**:

- `Matrice-Approvazione-Baseline.xlsx` — Tracciamento principale di tutte le approvazioni delle baseline
- `Verbali-Riunione-CAB-AAAAMMGG.pdf` — Riunioni CAB in cui le baseline sono state approvate
- `Email-Approvazione-BL-WIN2022-DC-v2.1.pdf` — Catene di approvazione email
- `Approvazione-RSSI-Standard-Sicurezza-Baseline.pdf` — Approvazione esecutiva

**Scopo delle prove**: Dimostra che le baseline hanno la corretta autorizzazione e la supervisione della governance.

#### 5. Snapshot-Configurazione/
Contiene gli export di configurazione effettivi che dimostrano la conformità alla baseline.

**File richiesti**:

- `Config-Server-WebServer01-AAAAMMGG.txt` — Configurazione effettiva del server
- `Export-Regole-Firewall-AAAAMMGG.xml` — Export della configurazione del firewall
- `Config-Database-DBSERVER01-AAAAMMGG.sql` — Configurazione del database
- `Export-Manifest-Kubernetes-AAAAMMGG.yaml` — Configurazione K8s

**Scopo delle prove**: Dimostra che le configurazioni distribuite corrispondono alle baseline approvate.

#### 6. Documentazione-Deviazioni/
Contiene le eccezioni alle baseline approvate.

**File richiesti**:

- `Registro-Deviazioni.xlsx` — Elenco principale di tutte le deviazioni approvate
- `Richiesta-Deviazione-DEV-2024-001.pdf` — Richiesta di deviazione con giustificazione aziendale
- `Valutazione-Rischio-DEV-2024-001.pdf` — Analisi del rischio per la deviazione
- `Controlli-Compensativi-DEV-2024-001.pdf` — Documentazione dei controlli attenuanti
- `Approvazione-RSSI-DEV-2024-001.pdf` — Approvazione esecutiva

**Convenzione di denominazione**: `DEV-AAAA-###` dove ### è un numero sequenziale.

**Scopo delle prove**: Dimostra che le deviazioni sono formalmente gestite con valutazione del rischio e approvazione.

#### 7. Report-Valutazione/
Contiene i libri di lavoro di valutazione completati e i report di riepilogo.

**File richiesti**:

- `Valutazione-Baseline-AAAAMMGG.xlsx` — Libro di lavoro ISMS-IMP-A.8.9 completato
- `Presentazione-Riepilogo-Valutazione.pptx` — Riepilogo esecutivo
- `Indice-Registro-Prove.pdf` — Indice di tutte le prove raccolte
- `Piano-Rimedio-Lacune.xlsx` — Piano d'azione per le lacune identificate

---

## Prove sul controllo delle modifiche

### Struttura della directory

**Prove/ISMS-A.8.9-Controllo-Modifiche/**

#### 1. Richieste-Modifica/
Contiene tutta la documentazione delle richieste di modifica.

**Sottodirectory per Anno-Trimestre**:

- `2024-T1/` — Tutte le modifiche del T1 2024
- `2024-T2/` — Tutte le modifiche del T2 2024

**Per ogni modifica**:

- `CR-2024-001-Modulo-Richiesta-Modifica.pdf` — Richiesta di modifica completata
- `CR-2024-001-Valutazione-Rischio.pdf` — Analisi del rischio
- `CR-2024-001-Risultati-Test.pdf` — Validazione dei test
- `CR-2024-001-Log-Implementazione.pdf` — Passaggi effettivi di implementazione
- `CR-2024-001-Revisione-Post-Implementazione.pdf` — PIR entro 5 giorni

**Convenzione di denominazione**: `CR-AAAA-###` dove ### è un numero sequenziale.

#### 2. Record-CAB/
Contiene la documentazione delle riunioni del Change Advisory Board.

**File richiesti**:

- `Calendario-Riunioni-CAB-2024.pdf` — Calendario CAB pubblicato
- `Elenco-Membri-CAB.pdf` — Attuali membri CAB e ruoli
- `Statuto-CAB.pdf` — Autorità e responsabilità del CAB
- `Verbali-Riunione-CAB-20240115.pdf` — Verbali della riunione con decisioni
- `Log-Presenze-CAB-2024.xlsx` — Tracciamento delle presenze per la verifica del quorum

**Scopo delle prove**: Dimostra che il CAB opera regolarmente con la dovuta governance.

#### 3. Flussi-Approvazione/
Contiene le catene di approvazione per i diversi tipi di modifica.

**File richiesti**:

- `Diagramma-Flusso-Approvazione.pdf` — Rappresentazione visiva dei livelli di approvazione
- `Catalogo-Modifiche-Standard.xlsx` — Modifiche standard pre-approvate
- `Log-Modifiche-Emergenza.xlsx` — Tutte le modifiche di emergenza con revisioni retrospettive
- `Matrice-Autorità-Approvazione.pdf` — Chi può approvare cosa

#### 4. Test-Validazione/
Contiene piani e risultati dei test.

**Per ogni modifica ad alto rischio**:

- `TEST-CR-2024-001-PianoTest.pdf` — Piano di test formale
- `TEST-CR-2024-001-RisultatiTest.xlsx` — Risultati dettagliati dei test
- `TEST-CR-2024-001-Screenshot.pdf` — Prove visive
- `TEST-CR-2024-001-TestRollback.pdf` — Validazione della procedura di rollback

#### 5. Metriche-Successo-Modifiche/
Contiene report KPI della gestione delle modifiche.

**File richiesti** (mensili/trimestrali):

- `Dashboard-Metriche-Modifiche-202401.pdf` — Report mensile delle metriche
- `Analisi-Tendenza-Tasso-Successo-Modifiche.xlsx` — Tracciamento storico
- `Analisi-Modifiche-Emergenza-T1-2024.pdf` — Revisione della giustificazione delle modifiche di emergenza
- `Analisi-Cause-Profonde-Modifiche-Fallite.pdf` — Analisi dei rollback

---

## Prove sul monitoraggio della configurazione

### Struttura della directory

**Prove/ISMS-A.8.9-Monitoraggio-Configurazione/**

#### 1. Infrastruttura-Monitoraggio/
Contiene le prove della distribuzione degli strumenti di monitoraggio.

**File richiesti**:

- `Inventario-Strumenti-Monitoraggio.xlsx` — Tutti gli strumenti di monitoraggio distribuiti
- `Diagramma-Architettura-Monitoraggio.pdf` — Come è distribuito il monitoraggio
- `Report-Copertura-Monitoraggio.xlsx` — Copertura degli asset per livello
- `Stato-Distribuzione-Agent-Monitoraggio.xlsx` — Tracciamento dell'installazione degli agent

#### 2. Avvisi-Scostamento/
Contiene gli avvisi di rilevamento degli scostamenti e i rimedi.

**Sottodirectory per gravità**:

- `Scostamento-Critico/` — Modifiche critiche dei controlli di sicurezza
- `Scostamento-Alto/` — Modifiche di alta gravità
- `Scostamento-Medio/` — Modifiche di media gravità
- `Scostamento-Basso/` — Modifiche informative di bassa gravità

**Per ogni incidente di scostamento**:

- `DRIFT-2024-001-Avviso.pdf` — Avviso originale con dettagli
- `DRIFT-2024-001-Indagine.pdf` — Indagine sulle cause profonde
- `DRIFT-2024-001-Rimedio.pdf` — Azioni di rimedio intraprese
- `DRIFT-2024-001-Chiusura.pdf` — Chiusura dell'incidente con verifica

**Convenzione di denominazione**: `DRIFT-AAAA-###`

#### 3. Report-Confronto-Baseline/
Contiene le scansioni periodiche di conformità alla baseline.

**File richiesti** (mensili minimo per Livello 1, trimestrali per Livello 2):

- `Scansione-Conformità-Baseline-202401-Livello1.pdf` — Conformità asset Livello 1
- `Scansione-Conformità-Baseline-202401-Livello2.pdf` — Conformità asset Livello 2
- `Analisi-Tendenza-Scostamento-T1-2024.xlsx` — Analisi delle tendenze

#### 4. Tracciamento-Rimedio/
Contiene il tracciamento delle azioni di rimedio degli scostamenti.

**File richiesti**:

- `Registro-Rimedio-Scostamento.xlsx` — Tutti gli incidenti di scostamento aperti/chiusi
- `Report-Conformità-SLA.xlsx` — Rispetto degli SLA di rimedio
- `Analisi-Scostamento-Ricorrente.pdf` — Analisi delle cause profonde per gli scostamenti ripetuti

#### 5. Prestazioni-Monitoraggio/
Contiene le prove di salute e affidabilità degli strumenti di monitoraggio.

**File richiesti**:

- `Report-Uptime-Strumento-Monitoraggio.xlsx` — Metriche di disponibilità degli strumenti
- `Tasso-Falsi-Positivi-Avvisi.xlsx` — Efficacia dell'ottimizzazione degli avvisi
- `Log-Incidenti-Monitoraggio.xlsx` — Guasti del sistema di monitoraggio

---

## Prove sull'hardening della sicurezza

### Struttura della directory

**Prove/ISMS-A.8.9-Hardening-Sicurezza/**

#### 1. Standard-Hardening/
Contiene la documentazione degli standard di hardening.

**File richiesti**:

- `Registro-Standard-Hardening.xlsx` — Tutti gli standard applicabili mappati agli asset
- `Libreria-CIS-Benchmark/` — PDF CIS Benchmark scaricati
- `Libreria-DISA-STIG/` — File STIG scaricati
- `Guide-Sicurezza-Fornitore/` — Documentazione di hardening del fornitore
- `Motivazione-Selezione-Standard.pdf` — Perché è stato scelto ogni standard

#### 2. Scansioni-Conformità/
Contiene le scansioni automatizzate di conformità all'hardening.

**Sottodirectory per tipo di asset**:

- `Windows-Server/`
- `Linux-Server/`
- `Dispositivi-Rete/`
- `Database/`
- `Piattaforme-Cloud/`

**Per tipo di asset (minimo trimestrale)**:

- `Scansione-CIS-WIN2022-202401.pdf` — Risultati della scansione di conformità
- `Scansione-CIS-RHEL9-202401.pdf` — Risultati della scansione di conformità
- `Analisi-Tendenza-Conformità-T1-2024.xlsx` — Tracciamento storico

#### 3. Analisi-Lacune/
Contiene le lacune di hardening identificate e i piani di rimedio.

**File richiesti**:

- `Registro-Lacune-Hardening.xlsx` — Tutte le lacune identificate
- `Piano-Rimedio-Lacune-Critiche.xlsx` — Piano d'azione per le lacune critiche
- `Valutazione-Rischio-Lacune.pdf` — Analisi del rischio per le lacune
- `Dashboard-Stato-Rimedio.xlsx` — Tracciamento dei progressi

#### 4. Eccezioni-Hardening/
Contiene le eccezioni approvate agli standard di hardening.

**Per ogni eccezione**:

- `HARD-EX-2024-001-Richiesta-Eccezione.pdf` — Richiesta formale di eccezione
- `HARD-EX-2024-001-Valutazione-Rischio.pdf` — Analisi del rischio
- `HARD-EX-2024-001-Controlli-Compensativi.pdf` — Misure di mitigazione
- `HARD-EX-2024-001-Approvazione.pdf` — Approvazione RSSI/Architetto della sicurezza

**Convenzione di denominazione**: `HARD-EX-AAAA-###`

#### 5. Implementazione-Hardening/
Contiene le prove dell'implementazione dell'hardening.

**File richiesti**:

- `Scansioni-Pre-Hardening/` — Baseline prima dell'hardening
- `Scansioni-Post-Hardening/` — Validazione dopo l'hardening
- `Script-Hardening/` — Script di hardening automatizzati
- `Log-Implementazione/` — Traccia di audit delle modifiche di hardening

#### 6. Report-Conformità/
Contiene la reportistica periodica sulla conformità.

**File richiesti** (trimestrali):

- `Dashboard-Conformità-Hardening-T1-2024.pdf` — Dashboard esecutivo
- `Conformità-per-Livello-Asset-T1-2024.xlsx` — Conformità basata sul livello
- `Report-Conformità-Controlli-Critici.xlsx` — Focus sui controlli critici
- `Analisi-Miglioramento-Anno-su-Anno.pdf` — Progressione della maturità

---

## Migliori pratiche per la raccolta delle prove

### Riepilogo delle convenzioni di denominazione

**Formato generale**: `[Tipo]-[Data/ID]-[Descrizione].[ext]`

**Esempi**:

- Libri di lavoro di valutazione: `Valutazione-Baseline-20240315.xlsx`
- Richieste di modifica: `CR-2024-042-Aggiornamento-Regola-Firewall.pdf`
- Incidenti di scostamento: `DRIFT-2024-018-Avvio-Servizio-Non-Autorizzato.pdf`
- Eccezioni: `HARD-EX-2024-005-Eccezione-App-Legacy.pdf`
- Verbali CAB: `Verbali-Riunione-CAB-20240315.pdf`

### Standard del formato data

**Tutte le date nei nomi di file**: Formato AAAAMMGG (ISO 8601)

- Corretto: `20240315`
- Errato: `03-15-2024`, `15.03.2024`

**Motivazione**: Garantisce che l'ordinamento alfabetico = ordinamento cronologico

### Standard del formato file

**Formati preferiti**:

- **Documenti formali**: PDF/A (formato archivio)
- **Fogli di calcolo**: XLSX (Excel) o CSV (per lo scambio di dati)
- **Export di configurazione**: Formato nativo (XML, JSON, YAML, TXT)
- **Diagrammi**: PDF (da Visio/draw.io), PNG (se l'interattività non è necessaria)

**Evitare**:

- Formati proprietari senza visualizzatori gratuiti
- File protetti da password (usare il controllo degli accessi del repository)
- Archivi compressi (archiviare non compressi per l'indicizzazione)

### Regole di conservazione delle prove

| Tipo di prova | Periodo di conservazione | Motivazione |
|---------------|--------------------------|-------------|
| Libri di lavoro di valutazione | Minimo 3 anni | Requisito ISO 27001 |
| Richieste di modifica | Minimo 3 anni | Requisito della traccia di audit |
| Incidenti di scostamento | Minimo 3 anni | Tracciamento degli incidenti di sicurezza |
| Record di approvazione | 7 anni | Requisito legale/di conformità |
| Snapshot di configurazione | 1 anno (rotante) | Solo esigenza operativa |
| Verbali CAB | Permanente | Documentazione della governance |
| Scansioni di hardening | 1 anno (rotante) | Solo esigenza operativa |

**Estensioni specifiche del settore**:

- Servizi finanziari (FINMA): 10 anni
- Assistenza sanitaria (HIPAA): 6 anni
- Contratti governativi: Secondo i termini del contratto

### Lista di controllo per la qualità delle prove

Prima di archiviare le prove, verificare:

- [ ] Il nome del file segue la convenzione di denominazione
- [ ] La data è accurata e nel formato AAAAMMGG
- [ ] Il file è nel formato preferito (PDF/XLSX)
- [ ] Il documento è completo (non bozza/parziale)
- [ ] I dati sensibili sono classificati in modo appropriato
- [ ] Il file non è danneggiato (aprire per verificare)
- [ ] I riferimenti incrociati ad altre prove sono accurati
- [ ] Collocato nella directory corretta secondo questa guida

### Controllo degli accessi alle prove

**Accesso in lettura**:

- Team di Gestione della configurazione
- Team di audit interno
- Revisori esterni (durante i periodi di audit)
- Responsabili della conformità
- RSSI e riporti diretti

**Accesso in scrittura**:

- Responsabile della configurazione
- Custodi delle prove designati
- Sistemi di raccolta automatizzata (account di servizio)

**Nessun accesso**:

- Personale IT generale (richiedere tramite Responsabile della configurazione)
- Parti esterne senza NDA
- Dipendenti cessati (revocare immediatamente)

### Automazione della raccolta delle prove

**Automazione raccomandata**:

- **Export CMDB**: Export automatizzato settimanale
- **Scansioni di conformità**: Scansioni trimestrali automatizzate
- **Snapshot di configurazione**: Backup notturno delle configurazioni critiche
- **Avvisi di scostamento**: Export in tempo reale al repository delle prove
- **Archiviazione richieste di modifica**: Automatica alla chiusura della modifica

**Raccolta manuale**:

- Firme di approvazione (firme autografe richieste)
- Valutazioni del rischio (giudizio umano richiesto)
- Verbali delle riunioni CAB (generati da esseri umani)
- Indagini sugli incidenti (analisi umana richiesta)

---

## Appendice: Download dei modelli per le prove

[L'organizzazione deve fornire modelli per]:

- Modulo di richiesta di modifica (CR-Modello.docx)
- Modulo di richiesta di deviazione (DEV-Modello.docx)
- Modulo di richiesta di eccezione (HARD-EX-Modello.docx)
- Modello di valutazione del rischio (Modello-Valutazione-Rischio.xlsx)
- Modello di verbale riunione CAB (Modello-Verbali-CAB.docx)

**Ubicazione dei modelli**: [L'organizzazione deve definire — es. SharePoint/Intranet]

---

## Manutenzione del repository delle prove

**Revisione trimestrale** (Responsabilità del Responsabile della configurazione):

- Verificare la completezza delle prove per il trimestre passato
- Archiviare le prove con più di 1 anno secondo il calendario di conservazione
- Aggiornare il PDF dell'Indice-Registro-Prove-Principale
- Rivedere l'elenco di controllo degli accessi (entrate/uscite)
- Verificare il backup/ripristino di emergenza del repository delle prove

**Revisione annuale** (Responsabilità del RSSI):

- Audit della conformità della struttura del repository delle prove con questa guida
- Revisione della conformità della politica di conservazione
- Valutare la qualità e la completezza delle prove
- Aggiornare questa guida se vengono identificati miglioramenti al processo

---

**FINE DEL DOCUMENTO DI RIFERIMENTO TECNICO**

*Per i requisiti di politica vincolanti, fare riferimento a ISMS-POL-A.8.9 Politica di gestione della configurazione.*

<!-- QA_VERIFIED: 2026-04-04 -->

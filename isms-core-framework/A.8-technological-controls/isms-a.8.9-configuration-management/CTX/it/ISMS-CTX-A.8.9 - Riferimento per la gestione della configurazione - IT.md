<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.9-IT-configuration-management-reference:framework:CTX:a.8.9 -->
**ISMS-CTX-A.8.9 — Riferimento per la gestione della configurazione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento per la gestione della configurazione |
| **Tipo di documento** | Riferimento tecnico (NON SGSI) |
| **Identificativo del documento** | ISMS-CTX-A.8.9 |
| **Autore del documento** | Responsabile della configurazione |
| **Proprietario del documento** | Architetto della sicurezza |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Data] |
| **Classificazione** | Interno |
| **Stato** | Riferimento |

**Ciclo di revisione**: Semestrale o quando cambiano standard/tecnologie  
**Autorità di revisione**: Revisione tecnica (Responsabile configurazione), Revisione sicurezza (Architetto sicurezza). NESSUNA approvazione esecutiva richiesta (NON SGSI).

---

## ⚠️ CRITICO: Stato del documento

**QUESTO DOCUMENTO NON FA PARTE DEL SGSI.**

**QUESTO DOCUMENTO NON DEFINISCE REQUISITI OBBLIGATORI.**

**QUESTO DOCUMENTO NON STABILISCE OBBLIGHI VINCOLANTI.**

**TUTTI I REQUISITI VINCOLANTI SONO DEFINITI IN ISMS-POL-A.8.9.**

**Si tratta di riferimento tecnico e guida operativa esclusivamente per la sensibilizzazione e il supporto all'implementazione.**

**Scopo**: Fornire riferimento agli standard tecnici, procedure di implementazione e guida operativa per supportare l'implementazione della politica di gestione della configurazione.

**Destinatari**: Responsabili della configurazione, amministratori di sistema, ingegneri DevOps, ingegneri della sicurezza, personale operativo.

---

## Parte 1: Riferimento agli standard di configurazione

### Panorama degli standard di hardening

**1.1.1 CIS Benchmark** (Center for Internet Security)

**Copertura**: Oltre 100 benchmark su 25+ famiglie tecnologiche

- Sistemi operativi: Windows, Linux (RHEL, Ubuntu, SUSE), macOS, varianti Unix
- Piattaforme cloud: AWS, Azure, GCP, Oracle Cloud
- Dispositivi di rete: Cisco, Palo Alto, Fortinet
- Database: Oracle, SQL Server, PostgreSQL, MongoDB, MySQL
- Applicazioni: Web server, piattaforme container, Kubernetes

**Livelli**:

- **Livello 1**: Hardening baseline pratico (impatto operativo minimo)
- **Livello 2**: Difesa in profondità (può influire sulla funzionalità)

**Come ottenere**: Download gratuito da cisecurity.org (registrazione richiesta)

**1.1.2 DISA STIG** (Defense Information Systems Agency)

**Copertura**: Requisiti di sicurezza del Dipartimento della Difesa USA

- Sistemi operativi: Windows, Linux, Unix
- Applicazioni: Database, web server, application server
- Dispositivi di rete: Router, switch, firewall

**Classificazione**: CAT I (Critico), CAT II (Alto), CAT III (Medio)

**Come ottenere**: Download gratuito da public.cyber.mil/stigs

**1.1.3 Guide di sicurezza dei fornitori**

**Microsoft**: Windows Server Security Baseline, Microsoft 365 Security Baseline, Azure Security Baseline, Security Compliance Toolkit

**Provider cloud**: AWS Security Best Practices, Azure Security Benchmarks, Google Cloud Security Foundations

**Fornitori di rete**: Guide di sicurezza Cisco, Palo Alto, Fortinet, Check Point

**1.1.4 Pubblicazioni NIST**

- **NIST SP 800-53 Rev. 5**: Controlli di sicurezza e privacy (famiglia CM)
- **NIST SP 800-128**: Gestione della configurazione incentrata sulla sicurezza
- **NIST SP 800-70**: Programma nazionale delle checklist
- **NIST Cybersecurity Framework**: Gestione della configurazione nella funzione PROTECT

**1.1.5 Standard aggiuntivi**

- **BSI Grundschutz**: Ufficio federale tedesco per la sicurezza informatica
- **Essential Eight**: Centro australiano per la sicurezza informatica
- **CMMC**: Cybersecurity Maturity Model Certification (appaltatori della difesa)
- **SWIFT CSC**: Controlli di sicurezza per i messaggi finanziari

### Standard di configurazione per tipo di asset

**1.2.1 Sistemi operativi**

**Windows Server**:

- **Standard primario**: CIS Windows Server Benchmark (specifico per versione)
- **Supplementare**: Microsoft Security Baselines, DISA STIG (alta sicurezza)
- **Controlli chiave**:
  - User Account Control (UAC) abilitato
  - Windows Firewall abilitato con regole restrittive
  - Registrazione degli audit per autenticazione, uso dei privilegi, accesso agli oggetti
  - Politica password: minimo 14 caratteri, complessità, blocco dopo 5 tentativi
  - Servizi disabilitati: Print Spooler (se non necessario), Desktop remoto (se non necessario)
  - Patch di sicurezza: installazione mensile entro 30 giorni

**Linux/Unix**:

- **Standard primario**: CIS Benchmark specifico per distribuzione (RHEL, Ubuntu, SUSE, ecc.)
- **Supplementare**: DISA STIG (alta sicurezza)
- **Controlli chiave**:
  - Login root disabilitato (usare sudo)
  - Hardening SSH (autenticazione con chiave, disabilita login root, disabilita protocollo 1)
  - iptables/firewalld configurati con default-deny
  - SELinux/AppArmor abilitato (modalità enforcing)
  - Daemon di audit (auditd) abilitato e configurato
  - Permessi file: /etc/passwd 644, /etc/shadow 000, /boot 700

**1.2.2 Dispositivi di rete**

**Firewall** (Palo Alto, Fortinet, Cisco ASA):

- **Standard primario**: Guida di sicurezza specifica del fornitore + CIS Benchmark
- **Controlli chiave**:
  - Policy default-deny
  - Set di regole con minimo privilegio
  - Registrazione abilitata per tutte le decisioni allow/deny
  - Accesso admin limitato alla VLAN di gestione
  - Autenticazione a più fattori per l'accesso admin
  - Revisione e pulizia regolare delle policy

**Router/Switch** (Cisco, Juniper, Arista):

- **Standard primario**: CIS Network Device Benchmark
- **Controlli chiave**:
  - Controllo accesso console e VTY (solo SSH, no Telnet)
  - SNMP v3 o disabilitato
  - Autenticazione AAA
  - Registrazione su syslog centralizzato
  - Sincronizzazione NTP
  - Porte inutilizzate disabilitate

**Load Balancer**:

- **Controlli chiave**: Solo TLS 1.2+, suite di cifratura robuste, validazione del certificato, configurazione del timeout di sessione, interfaccia admin sulla rete di gestione

**1.2.3 Piattaforme cloud**

**AWS**:

- **Standard primario**: CIS AWS Foundations Benchmark
- **Controlli chiave**:
  - IAM: MFA per tutti gli utenti, principio del minimo privilegio, rotazione regolare delle chiavi di accesso
  - Registrazione: CloudTrail abilitato in tutte le regioni, registrazione bucket S3, VPC Flow Logs
  - Monitoraggio: allarmi CloudWatch per chiamate API non autorizzate
  - Rete: gruppi di sicurezza VPC default-deny, nessun bucket S3 pubblico (se non esplicitamente richiesto)
  - Crittografia: crittografia EBS, crittografia S3 a riposo

**Azure**:

- **Standard primario**: CIS Microsoft Azure Foundations Benchmark
- **Controlli chiave**:
  - Identità: MFA abilitata, policy di accesso condizionale, PIM per ruoli privilegiati
  - Registrazione: conservazione Activity Log ≥365 giorni, Impostazioni diagnostiche abilitate
  - Rete: NSG default-deny, no RDP/SSH da internet
  - Crittografia: Azure Disk Encryption, Storage Service Encryption

**Google Cloud Platform (GCP)**:

- **Standard primario**: CIS Google Cloud Platform Foundation Benchmark
- **Controlli chiave**:
  - IAM: rotazione chiavi account servizio, principio del minimo privilegio
  - Registrazione: Cloud Audit Logs abilitati, sink di log configurati
  - Rete: regole firewall VPC restrittive, accesso privato Google
  - Crittografia: CMEK dove richiesto, dischi persistenti crittografati

**1.2.4 Database**

**SQL Server**: Standard primario CIS + DISA STIG. Controlli chiave: modalità autenticazione Windows, account sa disabilitato/rinominato, funzionalità non necessarie disabilitate (xp_cmdshell, OLE Automation, ecc.), SQL Server Audit abilitato, crittografia TDE e Always Encrypted per colonne sensibili.

**Oracle Database**: Standard primario CIS + DISA STIG. Controlli chiave: policy password robusta, account predefiniti bloccati, auditing abilitato, crittografia TDE e Network Encryption.

**PostgreSQL/MySQL/MongoDB**: Standard primario CIS Benchmark per ciascuno. Controlli chiave: autenticazione richiesta, connessioni SSL/TLS obbligatorie, permessi utente con minimo privilegio, registrazione audit abilitata.

**1.2.5 Container e orchestrazione**

**Docker**:

- **Standard primario**: CIS Docker Benchmark
- **Controlli chiave**: Eseguire container come utente non root, filesystem root in sola lettura dove possibile, limiti di risorse (CPU, memoria), profili AppArmor/SELinux, scansione regolare delle immagini per vulnerabilità

**Kubernetes**:

- **Standard primario**: CIS Kubernetes Benchmark
- **Controlli chiave**: RBAC abilitato e configurato, Pod Security Standards applicati, policy di rete definite, gestione dei segreti (store di segreti esterno), autenticazione e autorizzazione del server API, crittografia etcd a riposo

**1.2.6 Applicazioni**

**Web Server** (Apache, Nginx, IIS): Eseguire come utente non privilegiato, moduli non necessari disabilitati, registrazione accessi abilitata, solo TLS 1.2+, intestazioni di sicurezza (HSTS, X-Frame-Options, CSP).

**Application Server** (JBoss, WebLogic, Tomcat): Account predefiniti rimossi, interfaccia di gestione su rete separata, registrazione audit abilitata, servizi non necessari disabilitati.

### Albero decisionale per la selezione degli standard

```
INIZIO: Quale standard di hardening devo usare?

├─ L'asset elabora dati regolamentati (PCI, HIPAA, ecc.)?
│  ├─ SÌ → Usare prima lo standard richiesto dalla normativa
│  └─ NO → Continuare

├─ Esiste un CIS Benchmark per questo tipo di asset?
│  ├─ SÌ → Usare CIS Benchmark (Livello 1 baseline, Livello 2 alta sicurezza)
│  └─ NO → Continuare

├─ Esiste una guida di sicurezza specifica del fornitore?
│  ├─ SÌ → Usare la guida del fornitore
│  └─ NO → Continuare

├─ Il tipo di asset è coperto dalle linee guida NIST?
│  ├─ SÌ → Usare i controlli NIST come riferimento
│  └─ NO → Sviluppare baseline personalizzata con approvazione dell'Architetto della sicurezza

SEMPRE: Documentare la selezione dello standard nella documentazione della baseline
```

### Metodi di verifica

**Scansione automatizzata**:

- **OpenSCAP**: Scansione di conformità CIS e STIG (Linux/Windows)
- **Nessus/Tenable**: Scansione di vulnerabilità e conformità
- **Qualys**: Scansione di conformità basata su cloud
- **AWS Security Hub**: Conformità specifica AWS (CIS AWS Benchmark)
- **Azure Security Center**: Conformità specifica Azure
- **GCP Security Command Center**: Conformità specifica GCP

**Verifica manuale**:

- Revisione dei file di configurazione rispetto alla baseline
- Esecuzione di script di verifica della conformità
- Validazione dei controlli di sicurezza tramite test
- Documentazione dei risultati e delle eccezioni

**Conformità continua**:

- Integrazione della scansione nei pipeline CI/CD
- Reportistica automatica del dashboard di riepilogo
- Avviso sullo scostamento dalla conformità
- Rivalutazione regolare (minimo trimestrale)

---

## Parte 2: Guida all'implementazione della gestione delle modifiche

### Modello di modulo di richiesta di modifica

**Sezione 1: Identificazione della modifica**

- ID richiesta di modifica: [Auto-generato o CR-AAAA-####]
- Data di invio: [GG.MM.AAAA]
- Inviato da: [Nome, Dipartimento, Contatto]
- Titolo della modifica: [Titolo descrittivo breve, max 100 caratteri]
- Classificazione della modifica: [Standard / Normale / Emergenza]
- Se emergenza, giustificazione: [Perché non può attendere il processo normale]

**Sezione 2: Descrizione della modifica**

- Giustificazione aziendale: [Perché è necessaria? Quale problema risolve?]
- Descrizione tecnica: [Cosa verrà modificato specificamente?]
- Sistemi/Servizi interessati: [Elencare tutti gli asset impattati]
- Elementi di configurazione (CI): [Numeri CI CMDB se applicabile]

**Sezione 3: Valutazione dell'impatto**

- Impatto sugli utenti: [Nessuno / Minimo / Moderato / Significativo / Grave]
- Downtime del servizio richiesto: [Nessuno / <1ora / 1-4ore / 4-8ore / >8ore]
- Livello di rischio: [Basso / Medio / Alto / Critico]
- Dipendenze: [Altri sistemi, servizi, team interessati]

**Sezione 4: Piano di implementazione**

- Passaggi di implementazione: [Procedura dettagliata passo-passo]
- Data/Ora di implementazione: [GG.MM.AAAA HH:MM]
- Durata dell'implementazione: [Tempo stimato]
- Team di implementazione: [Nomi e ruoli]
- Risorse necessarie: [Strumenti, accesso, supporto del fornitore necessari]

**Sezione 5: Test e validazione**

- Ambiente di test: [Dev / Test / Staging / UAT]
- Data del test: [GG.MM.AAAA]
- Risultati del test: [Superato / Non superato / Parziale]
- Prove del test: [Link alla documentazione dei test]
- Criteri di successo: [Come determinare se la modifica ha avuto successo]

**Sezione 6: Piano di rollback**

- Criteri di attivazione del rollback: [Quando eseguire il rollback]
- Procedura di rollback: [Istruzioni passo-passo]
- Durata del rollback: [Tempo stimato]
- Backup dei dati verificato: [Sì / No / N/D]
- Rollback testato: [Sì / No / N/D - data se testato]

**Sezione 7: Comunicazione**

- Utenti da notificare: [Lista di distribuzione]
- Metodo di comunicazione: [Email / Portale / Annuncio]
- Tempi di notifica: [Prima / Durante / Dopo la modifica]

**Sezione 8: Approvazioni**

- Revisione tecnica: [Nome, Ruolo, Decisione, Data, Commenti]
- Revisione della sicurezza: [Nome, Ruolo, Decisione, Data, Commenti]
- Decisione CAB: [Approvato / Approvato con condizioni / Rifiutato / Rinviato]
- Data CAB: [GG.MM.AAAA]
- Condizioni: [Eventuali condizioni di approvazione]

**Sezione 9: Revisione post-implementazione**

- Data/Ora effettiva di implementazione: [GG.MM.AAAA HH:MM]
- Stato dell'implementazione: [Riuscita / Riuscita con problemi / Fallita / Rollback]
- Problemi riscontrati: [Descrizione]
- Risoluzione: [Come i problemi sono stati risolti]
- Lezioni apprese: [Cosa si potrebbe migliorare]

### Procedure per le riunioni CAB

**Pre-riunione (Responsabilità del Presidente CAB)**:

- Distribuire le richieste di modifica 48 ore prima della riunione
- Assicurarsi che tutte le approvazioni necessarie siano state ottenute
- Pre-filtrare per completezza (rifiutare le richieste incomplete)
- Pubblicare l'agenda della riunione

**Durante la riunione**:

- Esaminare ogni richiesta di modifica normale
- Valutare rischio e impatto
- Verificare piani di test e rollback
- Dare priorità in caso di conflitti di risorse
- Prendere la decisione di approvazione (Approvato / Approvato con condizioni / Rifiutato / Rinviato)
- Documentare la decisione e la motivazione

**Post-riunione**:

- Pubblicare i verbali della riunione entro 24 ore
- Notificare ai richiedenti di modifica le decisioni
- Aggiornare il sistema di gestione delle modifiche
- Pianificare la prossima riunione

### Catalogo delle modifiche standard

Le modifiche standard sono pre-approvate dal CAB ed eseguibili senza revisione individuale. Esempi:

**Reset della password**: Basso rischio. Procedura: Seguire la procedura di verifica dell'identità, reset in AD/IAM.

**Rinnovo dei certificati**: Basso rischio. Procedura: Generare CSR, inviare alla CA, installare nuovo certificato. Test: Verificare la catena di certificati e la scadenza.

**Patch software standard**: Basso rischio. Procedura: Installare dall'elenco di patch approvate in test, poi in produzione. Test richiesti nell'ambiente di test.

**Creazione/eliminazione di account utente**: Basso rischio. Procedura: Seguire il processo joiner/leaver.

Le organizzazioni mantengono il proprio Catalogo delle modifiche standard in base alle esigenze operative e alla propensione al rischio.

### Procedure per le modifiche di emergenza

**Quando utilizzare il processo di modifica di emergenza**:

- Exploit di sicurezza attivo (vulnerabilità attivamente sfruttata)
- Interruzione critica del servizio che colpisce le operazioni aziendali
- Contenimento di una violazione dei dati
- Violazione critica della conformità che richiede rimedio immediato

**Quando NON utilizzare**:

- Pianificazione inadeguata («dimenticato di inviare la richiesta di modifica»)
- Convenienza («non voglio aspettare il CAB»)
- Pressione del fornitore («il fornitore dice che deve essere fatto ora»)

**Flusso di lavoro per le modifiche di emergenza**:
1. **Approvazione verbale immediata**: Contattare CIO, RSSI o Presidente CAB per telefono
2. **Documentare la giustificazione**: Entro 1 ora, inviare email documentando la giustificazione dell'emergenza
3. **Implementare la modifica**: Eseguire la modifica sotto supervisione (regola del due persone se possibile)
4. **Documentare l'implementazione**: Entro 24 ore, completare il modulo di richiesta di modifica con i passaggi effettivi eseguiti
5. **Revisione retrospettiva CAB**: Entro 5 giorni lavorativi, presentare al CAB per la revisione

---

## Parte 3: Procedure di risposta alle deviazioni della configurazione

### Rilevamento e triage degli scostamenti

**Passaggio 1: Ricezione dell'avviso**

- Lo strumento di monitoraggio della configurazione genera un avviso di scostamento
- Avviso instradato al Responsabile della configurazione e al Proprietario del sistema
- L'avviso contiene: ID asset, modifica rilevata, valore atteso dalla baseline, valore effettivo, timestamp di rilevamento

**Passaggio 2: Triage iniziale** (Entro 1-4 ore in base alla gravità)

- Il Responsabile della configurazione esamina i dettagli dell'avviso
- Verifica nel sistema di gestione delle modifiche le modifiche autorizzate
- Classifica lo scostamento: Autorizzato, Non autorizzato, o Falso positivo

**Passaggio 3: Decisione di classificazione**

**Scostamento autorizzato**: La modifica era approvata ma la baseline non è ancora stata aggiornata

- Azione: Aggiornare la documentazione della baseline, aggiornare il CMDB, chiudere il ticket dell'incidente

**Scostamento non autorizzato**: Modifica non approvata o sconosciuta

- Azione: Procedere all'indagine (Passaggio 4)

**Falso positivo**: Errata configurazione dello strumento di monitoraggio o errore della baseline

- Azione: Ottimizzare la regola di monitoraggio, aggiornare la baseline se errata, chiudere il ticket

**Passaggio 4: Indagine sullo scostamento non autorizzato**

- Esaminare i log di sistema per determinare chi/cosa ha effettuato la modifica
- Determinare il timestamp della modifica
- Valutare se la modifica è malevola o un errore operativo
- Classificare la gravità (Critico / Alto / Medio / Basso)

**Passaggio 5: Risposta agli incidenti** (se malevola)

- Escalation al Centro operativo per la sicurezza (SOC)
- Seguire le procedure di risposta agli incidenti (ISMS-POL-A.5.24)
- Preservare le prove
- Contenere la minaccia

**Passaggio 6: Rimedio** (se errore operativo)

- Ripristinare la configurazione alla baseline
- Documentare le azioni di rimedio
- Condurre l'analisi delle cause profonde
- Implementare misure preventive
- Chiudere il ticket dell'incidente

### Processo di richiesta di eccezione

**Procedura di richiesta di eccezione**:

**Passaggio 1: Compilare il modulo di richiesta di eccezione**

- Sistema/Asset che richiede l'eccezione
- Controllo/i della baseline che richiedono l'eccezione
- Giustificazione aziendale (perché è necessaria l'eccezione)
- Valutazione del rischio (quale rischio introduce l'eccezione)
- Controlli compensativi (come viene mitigato il rischio)
- Durata richiesta (massimo 12 mesi)
- Piano per raggiungere la piena conformità (se temporanea)

**Passaggio 2: Revisione della sicurezza**

- L'Architetto della sicurezza esamina la richiesta
- Convalida la valutazione del rischio
- Verifica l'adeguatezza dei controlli compensativi
- Raccomanda approvazione/rifiuto

**Passaggio 3: Decisione di approvazione**

- Autorità di eccezione in base al livello di rischio (per ISMS-POL-A.8.9 Sezione 2.5.4)
- Critico: Solo RSSI
- Alto: Responsabile configurazione + Architetto della sicurezza
- Medio/Basso: Responsabile della configurazione

### Flussi di lavoro di rimedio

**Rimedio scostamento critico** (<4 ore): Il SOC e il Responsabile della configurazione vengono avvisati immediatamente. Il Proprietario del sistema indaga entro 1 ora. Se non autorizzato, ripristinare immediatamente alla baseline. Revisione post-incidente entro 48 ore.

**Rimedio scostamento alto** (<24 ore): Il Responsabile della configurazione e il Proprietario del sistema vengono notificati. Indagare entro 4 ore. Sviluppare il piano di rimedio ed eseguire entro 24 ore.

**Rimedio scostamento medio** (<5 giorni lavorativi): Il Responsabile della configurazione assegna al Proprietario del sistema. Pianificare il rimedio nella finestra di manutenzione. Eseguire e verificare.

**Rimedio scostamento basso** (<30 giorni): Aggiungere al backlog di rimedio. Dare priorità con altro lavoro.

---

## Parte 4: Riferimento rapido

### Quando devo inviare una richiesta di modifica?

**SÌ — Richiesta di modifica richiesta**:

- Modifica delle regole del firewall
- Modifica delle configurazioni di sistema (OS, applicazione, rete)
- Installazione di nuovo software
- Aggiornamento delle versioni del software
- Modifica delle impostazioni di sicurezza
- Aggiunta/rimozione di servizi
- Modifiche di rete (routing, VLAN, ACL)
- Aggiornamenti della baseline

**NO — Richiesta di modifica NON richiesta**:

- Reset della password (Modifica standard)
- Rinnovo dei certificati (Modifica standard — se stessi parametri)
- Patch di routine dall'elenco approvato (Modifica standard)
- Avvisi/notifiche di monitoraggio
- Lettura dei file di configurazione

**In caso di dubbio**: Contattare il Responsabile della configurazione

### Albero decisionale per la classificazione delle modifiche

```
INIZIO: Che tipo di modifica è questa?

├─ È una procedura ripetibile, pre-approvata, a basso rischio?
│  └─ SÌ → MODIFICA STANDARD (pre-approvata, seguire le POS)

├─ È un incidente di sicurezza urgente o un'interruzione critica?
│  └─ SÌ → MODIFICA DI EMERGENZA (approvazione accelerata)

├─ Tutto il resto
   └─ MODIFICA NORMALE (approvazione CAB richiesta)

Se MODIFICA NORMALE, qual è il livello di rischio?

├─ Ambito limitato, sistema singolo, facile rollback
│  └─ RISCHIO BASSO → Approvazione a un livello

├─ Più sistemi, impatto moderato, procedura standard
│  └─ RISCHIO MEDIO → Approvazione a due livelli

├─ A livello organizzativo, sistemi critici, complesso/non testato
   └─ RISCHIO ALTO → Approvazione a tre livelli (CAB)
```

### Chi approva cosa?

| Rischio modifica | Approvatori | Tempistica |
|-----------------|-------------|------------|
| **Standard** | Pre-approvato (seguire le POS) | Immediato |
| **Normale — Basso** | Responsabile tecnico / Proprietario sistema | 1-2 giorni |
| **Normale — Medio** | Responsabile tecnico + Proprietario servizio | 3-5 giorni |
| **Normale — Alto** | CAB (3 livelli) | 5-10 giorni |
| **Emergenza** | CIO o RSSI (verbale) | <4 ore |

### Attività comuni di configurazione

**Visualizzare la baseline per tipo di asset**: Accedere al Repository di configurazione (SharePoint/CMDB). Navigare a: Baseline → [Tipo di asset]. Esempio: Baseline → Windows Server 2022 → Domain Controller.

**Richiedere un'eccezione alla baseline**: Scaricare il modulo di richiesta di eccezione. Compilare tutti i campi (giustificazione aziendale, valutazione del rischio, controlli compensativi). Inviare all'Architetto della sicurezza per la revisione. Tempistica di approvazione: 5-10 giorni lavorativi.

**Segnalare uno scostamento dalla configurazione**: Se non rilevato automaticamente, creare un ticket di incidente. Fornire: ID asset, parametro di configurazione modificato, valore atteso, valore effettivo. Instradare al Responsabile della configurazione.

### FAQ

**D: La mia richiesta di modifica è stata rifiutata. Cosa faccio ora?**
R: Esaminare il motivo del rifiuto, affrontare le preoccupazioni del CAB, reinviare con aggiornamenti.

**D: Posso aggirare il controllo delle modifiche per esigenze aziendali urgenti?**
R: No. Usare il processo di modifica di emergenza con la dovuta giustificazione e revisione retrospettiva.

**D: Come trovo la baseline giusta per il mio sistema?**
R: Cercare nel Repository di configurazione per sistema operativo e ruolo. Se non trovata, contattare il Responsabile della configurazione.

**D: Ho ricevuto un avviso di scostamento per una modifica autorizzata. Cosa faccio?**
R: Verificare che la modifica fosse autorizzata, aggiornare la documentazione della baseline, chiudere l'incidente.

**D: Il mio sistema non può soddisfare la baseline a causa dei limiti del fornitore. Quali sono le mie opzioni?**
R: Richiedere un'eccezione formale con controlli compensativi, o contattare il fornitore per una soluzione alternativa/aggiornamento.

**D: Con quale frequenza devo verificare i miei sistemi rispetto alle baseline?**
R: Il monitoraggio automatizzato verifica continuamente. Revisioni manuali: Livello 1 (mensile), Livello 2 (trimestrale), Livello 3 (semestrale), Livello 4 (annuale).

---

## Appendice: Aggiornamenti del documento

Questo riferimento tecnico può essere aggiornato più frequentemente rispetto alle politiche SGSI per riflettere nuovi standard di hardening, cambiamenti tecnologici, evoluzione degli strumenti e miglioramenti procedurali.

---

**FINE DEL DOCUMENTO DI RIFERIMENTO TECNICO**

*Per i requisiti di politica vincolanti, fare riferimento a ISMS-POL-A.8.9 Politica di gestione della configurazione.*

<!-- QA_VERIFIED: 2026-04-04 -->

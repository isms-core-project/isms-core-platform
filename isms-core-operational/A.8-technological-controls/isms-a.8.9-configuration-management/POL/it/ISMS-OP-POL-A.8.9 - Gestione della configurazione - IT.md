<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.9-IT:operational:OP-POL:a.8.9 -->
**ISMS-OP-POL-A.8.9 — Gestione della configurazione**

---

**Controllo del documento**

| Campo | Valore |
|-------|-------|
| **Titolo del documento** | Gestione della configurazione |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.9 |
| **Creatore del documento** | Responsabile della Sicurezza delle Informazioni (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|---------|------|--------|---------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.9 — Gestione della configurazione
- ISO/IEC 27002:2022 Sezione 8.9 — Linee guida di implementazione per la gestione della configurazione
- NIST SP 800-128 — Guida per la gestione della configurazione orientata alla sicurezza dei sistemi informativi
- NIST SP 800-53 Rev 5 — CM-2 (Configurazione di base), CM-3 (Controllo delle modifiche alla configurazione), CM-6 (Impostazioni di configurazione), CM-7 (Funzionalità minima)
- CIS Controls v8 — Controllo 4 (Configurazione sicura degli asset e del software aziendali)
- CIS Benchmarks — Guide di hardening specifiche per piattaforma

**Controlli Annex A correlati**:

| Controllo | Relazione con la gestione della configurazione |
|---------|------------------------------------------|
| A.5.9 Inventario delle informazioni e degli altri asset associati | L'inventario degli asset fornisce l'ambito per la gestione della configurazione; ogni elemento di configurazione si ricollega a un asset inventariato |
| A.5.23 Sicurezza delle informazioni per l'uso dei servizi cloud | Le configurazioni dei servizi cloud gestite sotto questa politica; il modello di responsabilità condivisa definisce i confini della configurazione |
| A.5.24–28 Gestione degli incidenti | La deriva della configurazione o le modifiche non autorizzate possono attivare la risposta agli incidenti; le modifiche fallite escalate come incidenti |
| A.8.1–7–18–19 Sicurezza degli endpoint | Le configurazioni di base degli endpoint e gli standard di hardening definiti e applicati sotto questa politica |
| A.8.8 Gestione delle vulnerabilità tecniche | La remediation delle vulnerabilità può richiedere modifiche alla configurazione; l'hardening riduce la superficie delle vulnerabilità |
| A.8.15 Registrazione | Gli eventi di modifica della configurazione registrati per l'audit trail e il rilevamento delle derive |
| A.8.16 Attività di monitoraggio | Gli strumenti di monitoraggio rilevano la deriva della configurazione e le modifiche non autorizzate |
| A.8.20–22 Sicurezza di rete | Le configurazioni dei dispositivi di rete (firewall, switch, router) gestite come elementi di configurazione |
| A.8.32 Gestione delle modifiche | Le modifiche alla configurazione seguono il processo di approvazione della gestione delle modifiche; discipline complementari |

**Politiche interne correlate**:

- Politica di gestione degli asset
- Politica di gestione delle modifiche
- Politica di sicurezza degli endpoint
- Politica di sicurezza di rete
- Politica di registrazione
- Politica delle attività di monitoraggio (A.8.16)
- Politica di gestione delle vulnerabilità
- Politica di gestione degli incidenti

---

# Politica di gestione della configurazione

## Scopo

Lo scopo di questa politica è garantire che le configurazioni, incluse le configurazioni di sicurezza, di hardware, software, servizi e reti siano stabilite, documentate, implementate, monitorate e revisionate in modo da ridurre il rischio di incidenti di sicurezza causati da configurazioni errate, modifiche non autorizzate o deriva della configurazione.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative appropriate al rischio per proteggere i dati personali trattati dai sistemi sotto gestione della configurazione. La configurazione sicura dei sistemi che trattano dati personali è una misura tecnica fondamentale che dimostra la conformità agli obblighi di protezione dei dati. Dove l'organizzazione tratta dati di individui nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 32.

## Ambito

Tutti i dipendenti, i collaboratori esterni e gli utenti terzi con responsabilità di configurazione, manutenzione o amministrazione dei sistemi informativi.

Tutti i sistemi informativi, l'infrastruttura e i servizi che richiedono la gestione della configurazione, inclusi:

- **Elaborazione e infrastruttura**: Server (fisici e virtuali), container, workstation, dispositivi mobili.
- **Dispositivi di rete**: Firewall, router, switch, load balancer, access point wireless, gateway VPN.
- **Servizi cloud**: Configurazioni IaaS, PaaS e SaaS nell'ambito del controllo dell'organizzazione.
- **Sistemi operativi**: Configurazioni del sistema operativo dei server e degli endpoint.
- **Applicazioni e middleware**: Server applicativi, database, server web, code di messaggi.
- **Sistemi di sicurezza**: SIEM, protezione endpoint, rilevamento/prevenzione delle intrusioni, provider di identità.
- **Sistemi IoT e OT**: Dispositivi connessi e tecnologia operativa sotto la gestione dell'organizzazione.

In tutti gli ambienti: produzione, non di produzione (sviluppo, test, QA, staging), ripristino di emergenza e sandbox.

**Fuori ambito**: Dispositivi BYOD non gestiti dall'organizzazione; piattaforme SaaS dove l'organizzazione non ha controllo sulla configurazione (solo gestione del provider); sistemi temporanei con un ciclo di vita inferiore a 24 ore (a meno che non trattino dati personali o sensibili); sistemi esplicitamente esclusi tramite valutazione del rischio documentata con approvazione del RSSI.

## Principio

Tutti i sistemi informativi devono essere configurati secondo configurazioni di sicurezza di base documentate e approvate prima del rilascio in produzione. Le configurazioni predefinite del produttore ("out of the box") non sono accettabili per l'uso in produzione.

Le configurazioni devono essere:

- **Stabilite**: Configurazioni di sicurezza di base definite per ogni tipo di asset utilizzando standard di hardening riconosciuti.
- **Documentate**: I parametri di base registrati, sotto controllo versione e accessibili al personale autorizzato.
- **Implementate**: Sistemi rilasciati da configurazioni di base o golden image approvate.
- **Monitorate**: Configurazioni effettive confrontate con le configurazioni di base approvate per rilevare le derive.
- **Revisionate**: Le configurazioni di base revisionate e aggiornate a intervalli definiti e a seguito di modifiche significative.

L'organizzazione deve applicare il principio di funzionalità minima: i sistemi devono essere configurati per fornire solo le capacità richieste per il loro scopo previsto, con servizi, porte, protocolli e account non necessari disabilitati o rimossi.

**Implementazione della funzionalità minima** (requisiti specifici):

**Servizi (processi/demoni)**:
- Approccio: Whitelist solo dei servizi richiesti per il ruolo del sistema.
- Esempio — Configurazione di base del server applicativo Ubuntu: Servizi richiesti: sshd (gestione remota), systemd-resolved (DNS), chrony (sincronizzazione dell'ora), servizio applicativo (ad es. nginx, processo dell'app). Disabilitati/rimossi: cups (stampa), avahi-daemon (mDNS), bluetooth, X11 (servizi grafici).
- Validazione: `systemctl list-units --state=running` confrontato con la whitelist di base; servizi non autorizzati segnalati.

**Porte di rete**:
- Approccio: Whitelist solo delle porte in ascolto richieste.
- Esempio — Windows Server 2022 Domain Controller: Porte richieste: 53 (DNS), 88 (Kerberos), 135 (RPC), 389/636 (LDAP/LDAPS), 445 (SMB), 3389 (RDP — limitato alla subnet di amministrazione). Bloccate: Tutte le altre porte tramite firewall host.
- Validazione: `netstat -an` o `ss -tuln` confrontato con la baseline; listener imprevisti segnalati.

**Protocolli**:
- Disabilitare i protocolli legacy/non sicuri: SMBv1 (disabilitato), TLS sotto 1.2 (disabilitato), SSHv1 (disabilitato), Telnet (rimosso), FTP (sostituito con SFTP/FTPS).
- Abilitare solo alternative sicure: SSH (v2 minimo), solo TLS 1.2/1.3, HTTPS obbligatorio.

**Account predefiniti**:
- Rimuovere o disabilitare: Account guest, account predefiniti del fornitore (Administrator rinominato, password predefinite cambiate), account di servizio non utilizzati.
- Requisito di base: Documentare tutti gli account nella baseline con giustificazione (perché l'account esiste, come viene utilizzato).

**Funzionalità/ruoli non necessari**:
- Windows: Rimuovere i ruoli server non utilizzati (ad es. rimuovere i Servizi di stampa se non è un server di stampa, rimuovere IIS se non è un server web).
- Linux: Rimuovere i pacchetti non utilizzati (`apt autoremove`, `yum remove`).
- Cloud: Disabilitare i servizi cloud non utilizzati (ad es. disabilitare la console seriale AWS EC2 se non necessaria, disabilitare Azure Bastion se non utilizzato).

Documentazione: Ogni baseline deve includere una tabella "Servizi e porte richiesti" che elenca gli elementi nella whitelist con giustificazione.

---

## Configurazioni di base

### Definizione delle configurazioni di base

L'organizzazione deve definire e mantenere configurazioni di sicurezza di base al livello del **tipo di asset** (ad es. "Windows Server 2022 — Domain Controller", "Ubuntu 24.04 — Server applicativo", "Cisco IOS-XE — Core Switch"), non al livello del singolo asset.

Le configurazioni di base devono essere definite per tutti i tipi di asset in uso attivo in produzione.

**Requisiti di copertura delle configurazioni di base**:

La copertura deve essere misurata da:

- **Copertura del tipo di asset**: Percentuale di tipi di asset distinti (combinazioni OS + ruolo) con configurazioni di base documentate.
- **Copertura delle istanze**: Percentuale delle istanze totali degli asset di produzione coperte dalle configurazioni di base.

**Obiettivi di copertura**:

| Livello di asset | Copertura tipo di asset | Copertura istanze | Tempistica |
|------------|-------------------|------------------|----------|
| **Livello 1 (Critico)** | 100% | 100% | Immediata (nessuna eccezione) |
| **Livello 2 (Alto)** | 100% | 95% | Entro 6 mesi dal rilascio in produzione |
| **Livello 3 (Medio)** | 90% | 90% | Entro 12 mesi dal rilascio in produzione |
| **Livello 4 (Basso)** | 80% | 80% | Best effort |

**Gestione delle lacune**:

- **Asset di livello 1/2 senza configurazioni di base**: Il rilascio in produzione deve essere bloccato fino alla creazione di una configurazione di base (applicato tramite l'approvazione delle modifiche).
- **Lacune di livello 3/4**: Documentare nel registro delle lacune delle configurazioni di base con piano di remediation (obiettivo: configurazione di base creata entro 90 giorni dal rilascio in produzione).
- **Eccezione**: I sistemi legacy prossimi alla dismissione (meno di 12 mesi di vita residua) possono rinunciare al requisito della configurazione di base con accettazione del rischio del RSSI e monitoraggio avanzato.

Ogni configurazione di base deve documentare:

- **Identificatore della baseline** (ad es. BASE-WIN2022-DC-v1.2) e versione.
- **Tipo di asset** e ambienti applicabili.
- **Impostazioni del sistema operativo**: Impostazioni di sicurezza, servizi abilitati/disabilitati, parametri del kernel, impostazioni del registro.
- **Configurazioni delle applicazioni**: Impostazioni predefinite, parametri di sicurezza, punti di integrazione.
- **Impostazioni di rete**: Configurazione IP, regole del firewall, access control list, routing.
- **Configurazioni di sicurezza**: Impostazioni di autenticazione, parametri di cifratura, impostazioni di registrazione e audit, policy sulle password.
- **Standard di hardening applicato**: Livello del CIS Benchmark, guida del fornitore o standard personalizzato con motivazione.
- **Eccezioni e deviazioni**: Qualsiasi scostamento dallo standard di hardening, con giustificazione documentata e accettazione del rischio.
- **Criteri di validazione**: Come verificare che un sistema sia conforme alla configurazione di base.

### Approvazione delle configurazioni di base

Le nuove configurazioni di base e gli aggiornamenti devono seguire un flusso di approvazione definito:

| Azione | Autorità di approvazione | Tempistica |
|--------|--------------------|----------|
| **Nuova configurazione di base** | Technical Lead (valida l'accuratezza) + RSSI o delegato (valida la sicurezza) | 14 giorni lavorativi |
| **Aggiornamento della configurazione di base** | Technical Lead + RSSI o delegato | 7 giorni lavorativi |
| **Modifica d'emergenza della configurazione di base** | RSSI (accelerata) | 24 ore; revisione retrospettiva entro 5 giorni lavorativi |

### Revisione delle configurazioni di base

Le configurazioni di base devono essere revisionate e aggiornate:

- **Annualmente** (minimo) per tutte le configurazioni di base.
- **Trimestralmente** per le configurazioni di base dei sistemi di livello 1 (critico).
- **Ad hoc** quando attivate da: nuove divulgazioni di vulnerabilità che influenzano le impostazioni di base, aggiornamenti tecnologici o cambiamenti di versione, modifiche ai requisiti normativi o di conformità, lezioni apprese dagli incidenti di sicurezza.

### Deprecazione delle configurazioni di base

Quando un tipo di asset viene dismesso o sostituito:

- La configurazione di base deve essere contrassegnata come "DEPRECATA" con una data di entrata in vigore.
- La configurazione di base deve essere conservata nel repository per 3 anni come riferimento storico.
- La configurazione di base deve essere rimossa dal monitoraggio della conformità attivo.
- Una configurazione di base sostitutiva (se applicabile) deve essere collegata nel repository.

---

## Build standard e golden image

L'organizzazione dovrebbe adottare build standard e golden image per garantire un rilascio coerente e ripetibile di sistemi configurati in modo sicuro.

### Requisiti delle golden image

Le golden image devono:

- Implementare la configurazione di base approvata per il tipo di asset pertinente.
- Contenere solo software approvato e con licenza.
- Includere le patch di sicurezza correnti al momento della creazione dell'immagine.
- Essere testate in un ambiente non di produzione prima dell'approvazione per l'uso in produzione.
- Essere versionizzate e tracciate in un repository di configurazione.

**Policy di aggiornamento delle golden image** (basata sul rischio):

**Aggiornamento pianificato** (baseline):
- **Immagini di livello 1/2**: Aggiornamento mensile.
- **Immagini di livello 3/4**: Aggiornamento trimestrale.

**Aggiornamento attivato** (immediato, sovrascrive il piano):
- **Patch per vulnerabilità critica**: Entro 7 giorni dal rilascio della patch (per vulnerabilità che interessano il software di base con CVSS >= 9.0 o sfruttamento attivo).
- **Aggiornamento della configurazione di base**: Entro 14 giorni dalla modifica approvata della configurazione di base.
- **Incidente di sicurezza**: Immediatamente se la golden image potrebbe essere compromessa o contenere configurazioni vulnerabili.

**Procedura di aggiornamento**:
1. Aggiornare l'immagine base con le ultime patch.
2. Applicare la configurazione di sicurezza di base corrente.
3. Testare in ambienti non di produzione: Rilasciare un'istanza di test, eseguire la suite di validazione (test funzionali, scansione di sicurezza).
4. Validazione del team di sicurezza: Scansionare per configurazioni errate, verificare la conformità all'hardening.
5. Approvazione: Firma del Responsabile delle operazioni IT + Team di sicurezza.
6. Pubblicare: Sostituire la vecchia immagine nel repository, contrassegnare la vecchia immagine come "DEPRECATA".
7. Notificare: Informare gli amministratori di sistema della nuova versione dell'immagine.

**Conservazione delle vecchie immagini**:
- Versione precedente: Conservata 90 giorni (capacità di rollback se la nuova immagine ha problemi).
- Versioni precedenti: Archiviate per 1 anno (riferimento storico).

**Applicazione del rilascio**:
- Rilasci che utilizzano immagini più vecchie di 60 giorni: Segnalati per revisione (perché non si utilizza l'immagine corrente?).
- Rilasci che utilizzano immagini più vecchie di 90 giorni: Rifiutati (è necessario utilizzare l'immagine corrente o documentare l'eccezione).

**Monitoraggio dell'età delle immagini**: [Sistema di gestione degli asset] deve registrare la data di creazione dell'immagine per istanza rilasciata; report mensile sui "rilasci obsoleti" (istanze da immagini più vecchie di 30 giorni).

La creazione delle golden image deve essere limitata al personale autorizzato (amministratori di sistema o ingegneri DevOps). Le golden image nuove o aggiornate devono essere validate dal team di sicurezza prima dell'approvazione.

### Infrastructure as Code

Dove fattibile, l'organizzazione dovrebbe definire le configurazioni di base come codice (ad es. Terraform, Ansible, CloudFormation, manifest Kubernetes, Puppet, Chef) e gestirle tramite controllo versione:

- **Controllo versione**: Le definizioni IaC archiviate in Git o equivalente con cronologia completa delle modifiche.
- **Revisione del codice**: Le modifiche alla configurazione inviate tramite pull request e revisionate prima del merge.
- **Test automatizzati**: IaC validata tramite test automatizzati (linting, scansione policy-as-code, dry-run) prima del rilascio.
- **Integrazione del controllo delle modifiche**: I rilasci IaC soggetti al processo di gestione delle modifiche dell'organizzazione.
- **Scansione delle configurazioni errate**: I template IaC scansionati per configurazioni di sicurezza errate prima del rilascio (ad es. Checkov, tfsec o equivalente).

**Requisiti di scansione della sicurezza IaC**:

**Strumenti di scansione**: [Checkov / tfsec / Terraform Sentinel / Open Policy Agent] configurati secondo gli standard organizzativi.

**Regole di scansione obbligatorie** (tutti i template IaC):

| Categoria | Esempi di regole | Livello di applicazione |
|----------|---------------|------------------|
| **Cifratura** | Bucket S3 cifrati a riposo, cifratura RDS abilitata, volumi EBS cifrati, TLS in transito | Bloccante (il rilascio fallisce se violato) |
| **Controllo degli accessi** | Nessun bucket S3 pubblico (salvo esplicita approvazione), security group senza ingress 0.0.0.0/0 su porte sensibili (22, 3389), le policy IAM seguono il privilegio minimo | Bloccante |
| **Registrazione** | CloudTrail abilitato, log di flusso VPC abilitati, registrazione RDS/database abilitata | Bloccante |
| **Gestione dei segreti** | Nessuna credenziale hardcoded nell'IaC (devono utilizzare riferimenti al secret manager), nessuna chiave API in testo in chiaro | Bloccante |
| **Sicurezza di rete** | VPC predefinito non utilizzato, subnet correttamente segmentate (pubblica/privata), NACL configurate | Avviso (revisione richiesta, può essere ignorato con giustificazione) |
| **Funzionalità minima** | Regole del security group predefinite rimosse, servizi non necessari disabilitati nelle configurazioni di lancio | Avviso |

**Regole personalizzate** (specifiche dell'organizzazione):
- Tag obbligatori: Tutte le risorse etichettate con Owner, Environment, CostCenter, DataClassification.
- Tipi di istanza approvati: Solo famiglie di istanze approvate dall'organizzazione (nessun tipo insolito senza approvazione).
- Regioni approvate: Rilasci solo nelle regioni cloud approvate (ad es. eu-central-1, westeurope).

**Esecuzione della scansione**:
- **Pre-commit**: Gli sviluppatori eseguono scansioni localmente prima di committare le modifiche IaC (consigliato, non obbligatorio).
- **Pipeline CI/CD**: Scansione automatizzata sulla pull request (obbligatoria); le violazioni bloccanti impediscono il merge.
- **Processo di eccezione**: Se una violazione bloccante non può essere remediated (legittima necessità aziendale), lo sviluppatore documenta l'eccezione in [Tracker eccezioni], il RSSI approva, l'eccezione viene aggiunta all'IaC come commento + regola di soppressione.

**Gestione dei risultati della scansione**:
- Violazioni bloccanti: Rilascio interrotto, remediation prima di riprovare.
- Violazioni di avviso: Registrate, revisionate dal team di sicurezza settimanalmente, escalate se emerge un pattern.
- Eccezioni: Revisionate trimestralmente, revocate se non più giustificate.

**Manutenzione del ruleset**:
- Il team di sicurezza mantiene il ruleset di scansione IaC in [Repository Git].
- Ruleset revisionato trimestralmente, aggiornato per nuove minacce e best practice.
- Sotto controllo versione con changelog.

L'IaC non sostituisce la necessità di configurazioni di base documentate; è il metodo preferito per implementarle e applicarle.

---

## Controllo delle modifiche alla configurazione

Tutte le modifiche alle configurazioni di sistema devono seguire il processo di gestione delle modifiche dell'organizzazione (vedere **Politica di gestione delle modifiche — A.8.32**). Questa sezione affronta i requisiti specifici della configurazione che integrano la gestione delle modifiche.

### Classificazione delle modifiche

Le modifiche alla configurazione devono essere classificate in base al rischio e all'impatto:

| Tipo | Definizione | Approvazione | Esempi |
|------|------------|----------|----------|
| **Standard** | Modifica alla configurazione pre-approvata, a basso rischio e ripetibile per procedura documentata | Pre-approvata (catalogo) | Rinnovo del certificato, aggiunta di record DNS, regola del firewall standard |
| **Normale** | Richiede valutazione, testing e approvazione formale | Proprietario del servizio / CAB | Aggiornamento della configurazione di base, nuovo standard di hardening, modifica della topologia di rete |
| **Emergenza** | Modifica urgente per risolvere un incidente critico o una vulnerabilità | RSSI o Responsabile delle operazioni IT (accelerata) | Disabilitazione di un servizio compromesso, regola del firewall d'emergenza, patch critica |

### Categorizzazione delle modifiche alla configurazione

**Richiede approvazione formale delle modifiche** (Politica di gestione delle modifiche A.8.32):
- Modifiche alla configurazione rilevanti per la sicurezza: Impostazioni di autenticazione, parametri di cifratura, regole del firewall, controlli degli accessi, livelli di registrazione (eventi di sicurezza), autorizzazioni utente/gruppo.
- Modifiche alla configurazione di base: Qualsiasi modifica alla definizione della configurazione di base approvata.
- Modifiche ai sistemi di produzione: Qualsiasi modifica alla configurazione dei sistemi di produzione di livello 1/2 (indipendentemente dalla rilevanza per la sicurezza).
- Modifiche alla topologia di rete: Routing, VLAN, subnetting, policy del firewall.
- Modifiche a più sistemi: Modifiche alla configurazione che interessano più di 5 sistemi contemporaneamente.

**Pre-approvate** (catalogo delle modifiche standard, nessun CAB):
- Ottimizzazione dei parametri entro intervalli documentati: Giorni di rotazione dei log (7–30 giorni), dimensioni della cache (entro limiti definiti), valori di timeout (entro intervalli sicuri).
- Rinnovi dei certificati: Sostituzione del certificato TLS/SSL con gli stessi parametri.
- Aggiunte di record DNS: Aggiunta di record A/AAAA/CNAME (non modifica dei server autorevoli).
- Provisioning/deprovisioning degli utenti: Seguendo le procedure joiner/mover/leaver documentate.

**Non richiede l'approvazione delle modifiche** (aggiustamento operativo):
- Modifiche cosmetiche: Etichette UI, descrizioni non funzionali, campi di commento.
- Ottimizzazione delle soglie di monitoraggio: Aggiustamento delle soglie degli alert in base alle baseline osservate (documentato nello strumento di monitoraggio).
- Sistemi non di produzione: Modifiche alla configurazione dei sistemi di sviluppo/test di livello 3/4 (registrate ma non formalmente approvate, a meno che non siano rilevanti per la sicurezza).

Linea guida: In caso di incertezza se una modifica richiede l'approvazione, l'impostazione predefinita è **sì** (inviare la richiesta di modifica).

Documentazione: Il catalogo delle modifiche standard deve essere mantenuto in [Sistema di gestione delle modifiche] con procedure pre-approvate e valutazioni del rischio.

### Aggiornamento della documentazione della configurazione

A seguito di qualsiasi modifica approvata alla configurazione, i seguenti elementi devono essere aggiornati entro **5 giorni lavorativi**:

- Documentazione della configurazione di base (se la configurazione di base stessa è cambiata).
- Database di gestione della configurazione (CMDB) o registrazioni equivalenti degli asset.
- Diagrammi di rete e documentazione della topologia (se la configurazione di rete è cambiata).
- Procedure operative e runbook (se i passaggi operativi sono cambiati).
- Procedure di ripristino di emergenza (se la modifica riguarda sistemi critici o RTO/RPO).

### Modifiche alla configurazione non autorizzate

Le modifiche alla configurazione apportate al di fuori del processo approvato di gestione delle modifiche devono essere trattate come eventi di sicurezza:

- Rilevate tramite monitoraggio della configurazione e rilevamento delle derive.
- Investigate per determinare la causa principale (malevola, accidentale o lacuna del processo).
- Segnalate al RSSI.
- Soggette ad azioni correttive, che possono includere azioni disciplinari.
- Il sistema interessato deve essere rimediato alla configurazione di base approvata o deve essere formalmente approvata una nuova configurazione di base attraverso il processo standard.

---

## Rilevamento e monitoraggio della deriva della configurazione

### Requisiti di monitoraggio

L'organizzazione deve implementare il monitoraggio della configurazione per rilevare le deviazioni dalle configurazioni di base approvate.

**Obiettivi di copertura per criticità degli asset**:

| Livello di asset | Obiettivo di copertura | Frequenza di monitoraggio | Lacuna di copertura accettabile |
|------------|----------------|----------------------|-------------------------|
| **Livello 1 (Critico)** | 100% | In tempo reale o ogni ora | 0% |
| **Livello 2 (Alto)** | 95% o superiore | Giornaliero | Meno del 5% |
| **Livello 3 (Medio)** | 85% o superiore | Settimanale | Meno del 15% |
| **Livello 4 (Basso)** | 70% o superiore | Mensile | Meno del 30% |

Gli strumenti di monitoraggio devono:

- Confrontare la configurazione effettiva del sistema con la configurazione di base approvata.
- Generare alert quando vengono rilevate deviazioni dalla configurazione.
- Conservare i risultati del monitoraggio per un minimo di 90 giorni.
- Integrarsi con [SIEM] per alerting centralizzato e correlazione dove praticabile.

**Selezione degli strumenti**: L'organizzazione deve selezionare strumenti di monitoraggio della configurazione appropriati al suo ambiente tecnico. Gli strumenti devono supportare il confronto con la configurazione di base e il rilevamento delle derive. Esempi includono: strumenti di monitoraggio dell'integrità dei file (FIM), strumenti di valutazione della configurazione cloud (ad es. AWS Config, Azure Policy, GCP Security Command Center), piattaforme di gestione degli endpoint e scanner di conformità della configurazione.

I tipi di asset non ancora sotto monitoraggio automatizzato devono essere documentati con una data di rilascio pianificata e controlli manuali provvisori (ad es. audit manuali trimestrali). Le lacune di copertura devono essere accettate dal RSSI come rischio e registrate nel registro dei rischi.

### Gestione delle lacune di copertura del monitoraggio

**Requisiti di documentazione delle lacune**:
- Tipo/istanza di asset non ancora monitorato: Registrato nel Registro delle lacune di monitoraggio.
- Campi del registro: ID asset, Livello, Motivo della lacuna (limitazione dello strumento, budget in attesa, vincolo tecnico), Controllo provvisorio (audit manuale, registrazione avanzata, accesso limitato), Proprietario (chi effettuerà la remediation), Data di rilascio pianificata, Data di rilascio effettiva, Stato (Aperto/In corso/Chiuso).

**SLA di chiusura delle lacune** (dall'identificazione al rilascio del monitoraggio):

| Livello di asset | Durata massima della lacuna | Requisito del controllo provvisorio | Escalation se SLA mancato |
|------------|---------------------|----------------------------|--------------------------|
| **Livello 1** | 30 giorni | Audit manuale avanzato (revisione settimanale della configurazione + audit mensile completo) | RSSI (immediato); può richiedere il blocco della produzione fino al rilascio del monitoraggio |
| **Livello 2** | 90 giorni | Audit manuale (revisione mensile della configurazione) | Responsabile delle operazioni IT poi RSSI a 60 giorni |
| **Livello 3** | 180 giorni | Audit manuale (trimestrale) | Responsabile delle operazioni IT a 120 giorni |
| **Livello 4** | 365 giorni | Audit manuale annuale accettabile | Responsabile delle operazioni IT a 270 giorni |

**Responsabilità per la chiusura delle lacune**:
- Proprietario della lacuna: Responsabile dell'implementazione della soluzione di monitoraggio entro la data di rilascio pianificata.
- Revisione mensile: Il Responsabile delle operazioni IT revisionare il Registro delle lacune di monitoraggio, monitora i progressi, escalate le lacune in ritardo.
- Reportistica trimestrale: Sintesi del registro delle lacune segnalata al RSSI (numero di lacune aperte per livello, tempo medio di chiusura, lacune in ritardo).

**Controlli provvisori** (mentre la lacuna persiste):
- Revisione manuale della configurazione: L'amministratore di sistema esporta la configurazione, la confronta manualmente con la configurazione di base, documenta i risultati.
- Registrazione degli accessi avanzata: L'accesso con account privilegiati ai sistemi non monitorati registrato e revisionato settimanalmente.
- Blocco delle modifiche (solo livello 1): Se il monitoraggio non può essere rilasciato entro lo SLA, considerare il blocco delle modifiche non d'emergenza fino a quando il monitoraggio è disponibile.

**Accettazione del rischio delle lacune**:
- Se la lacuna non può essere chiusa (ad es. sistema legacy incompatibile con gli strumenti di monitoraggio, vincoli di budget): Il RSSI approva l'accettazione del rischio con giustificazione documentata, controlli compensativi e revisione annuale.
- L'accettazione del rischio non esonera dai controlli provvisori — gli audit manuali devono continuare.

**Criteri di successo**: Obiettivo meno del 5% degli asset di livello 1/2 nel Registro delle lacune di monitoraggio in qualsiasi momento.

### Classificazione della deriva e risposta

Quando viene rilevata una deriva della configurazione, deve essere classificata per gravità e gestita entro le tempistiche definite:

| Gravità | Definizione | SLA di risposta | Esempi |
|----------|------------|--------------|---------|
| **Critica** | Controllo di sicurezza disabilitato o compromesso | Meno di 1 ora | Firewall disabilitato, account admin non autorizzato creato, cifratura disattivata, registrazione disabilitata su sistema critico |
| **Alta** | Configurazione rilevante per la sicurezza cambiata | Meno di 4 ore | Policy sulle password indebolita, servizio non necessario abilitato, access control list modificata senza approvazione |
| **Media** | Deriva della configurazione non di sicurezza | Meno di 24 ore | Porta del servizio cambiata, impostazione dell'applicazione non critica modificata, mancata corrispondenza della documentazione |
| **Bassa** | Deviazione informativa | Meno di 5 giorni lavorativi | Modifiche cosmetiche, impostazioni non funzionali, differenze minori nei parametri |

**Routing degli alert**:

- **Critica e Alta**: Team delle operazioni di sicurezza + RSSI + Proprietario del sistema.
- **Media**: Responsabile delle operazioni IT + Proprietario del sistema.
- **Bassa**: Operazioni IT (report consolidato giornaliero).

### Remediation della deriva

La remediation della deriva deve seguire un flusso di lavoro strutturato:

1. **Rilevamento**: Il monitoraggio automatizzato identifica la deviazione della configurazione.
2. **Triage**: Le operazioni IT investigano la causa e determinano se la modifica era autorizzata, non autorizzata o un falso positivo.
3. **Azione**:
   - **Modifica autorizzata** (approvata ma configurazione di base non ancora aggiornata): Aggiornare la documentazione della configurazione di base; chiudere l'alert.
   - **Modifica non autorizzata**: Rimediare il sistema alla configurazione di base approvata; investigare la causa principale; segnalare al RSSI; chiudere dopo la risoluzione.
   - **Falso positivo**: Ottimizzare le regole di monitoraggio; chiudere l'alert.
4. **Documentazione**: Tutti gli incidenti di deriva registrati, monitorati fino alla chiusura e conservati per l'audit.

**Verifica della remediation della deriva** (obbligatoria):

Procedura di remediation:
1. **Identificare la deriva**: Lo strumento di monitoraggio rileva la deviazione (ad es. regola del firewall aggiunta, servizio abilitato, parametro modificato).
2. **Investigare**: Determinare se autorizzata (modifica approvata non ancora documentata) o non autorizzata.
3. **Remediation**: Se non autorizzata, ripristinare alla configurazione di base:
   - Manuale: L'amministratore di sistema ripristina il parametro di configurazione al valore di base.
   - Automatizzato: Lo strumento di gestione della configurazione (Ansible, Puppet, Chef) riapplica la configurazione di base.
   - Re-imaging: Per derive gravi o compromissioni, ricostruire dalla golden image.
4. **Verificare la remediation** (entro 24 ore dalla remediation):
   - Ri-scansionare il sistema con lo stesso strumento di monitoraggio che ha rilevato la deriva.
   - Confermare che l'alert di deriva sia stato eliminato.
   - Documentare: Il ticket di remediation aggiornato con timestamp della verifica, risultati della scansione e firma.
5. **Analisi della causa principale** (per derive Critiche/Alte):
   - Perché si è verificata la deriva? (Lacuna del processo, accesso non autorizzato, errore di automazione, errore della configurazione di base.)
   - Azione preventiva: Aggiornare la configurazione di base, migliorare l'automazione, potenziare i controlli degli accessi, formare il personale.
6. **Chiudere il ticket**: Solo dopo che la verifica conferma la conformità alla configurazione di base.

**Verifica fallita**:
- Se la nuova scansione mostra che la deriva persiste: Escalare al Responsabile delle operazioni IT, ripetere la remediation, considerare l'isolamento del sistema se è una deriva del controllo di sicurezza.
- Se la deriva ricorre entro 30 giorni: Indagine obbligatoria sulla causa principale, RSSI notificato.

**Metriche di remediation della deriva** tracciate:
- Percentuale di remediation della deriva con verifica completata: Obiettivo 100%.
- Tempo dalla remediation alla verifica: Obiettivo meno di 24 ore.
- Deriva ricorrente (stesso sistema, stesso parametro, più di 2 occorrenze): Obiettivo 0.

Segnalato mensilmente al RSSI.

**SLA di remediation**:

| Gravità | SLA di remediation | Escalation se SLA non rispettato |
|----------|----------------|---------------------------|
| **Critica** | Meno di 4 ore | RSSI — può isolare il sistema dalla produzione |
| **Alta** | Meno di 24 ore | RSSI |
| **Media** | Meno di 5 giorni lavorativi | Responsabile delle operazioni IT |
| **Bassa** | Meno di 30 giorni | Best effort |

La deriva ricorrente sullo stesso sistema o tipo di asset deve attivare un'analisi della causa principale. Se la causa principale è una configurazione di base che non è pratica da mantenere, la configurazione di base deve essere revisionata e aggiornata attraverso il processo standard di approvazione piuttosto che accettare ripetutamente eccezioni.

---

## Standard di hardening della sicurezza

### Selezione degli standard di hardening

L'organizzazione deve selezionare e applicare standard di hardening della sicurezza riconosciuti per tutti i tipi di asset di produzione.

**Standard riconosciuti** (in ordine di preferenza):

| Standard | Provider | Utilizzo tipico |
|----------|----------|---------------|
| **CIS Benchmarks** | Center for Internet Security | Riferimento primario per le piattaforme comuni (Windows, Linux, cloud, dispositivi di rete, database) |
| **Guide di sicurezza dei fornitori** | Microsoft, AWS, Azure, GCP, Cisco, ecc. | Piattaforme cloud, prodotti specifici del fornitore |
| **DISA STIGs** | Defense Information Systems Agency | Ambienti ad alta sicurezza, allineamento governativo |
| **Baseline NIST** | NIST SP 800-53, SP 800-128 | Allineamento del framework, linee guida supplementari |

Dove esistono più standard per un tipo di asset, l'organizzazione deve selezionare lo standard più appropriato al suo profilo di rischio e documentare la motivazione della selezione.

### Implementazione dell'hardening

Tutti i sistemi di produzione devono essere sottoposti a hardening prima del rilascio. L'hardening deve includere, come minimo:

- **Rimuovere o disabilitare servizi, porte e protocolli non necessari** (principio di funzionalità minima — NIST CM-7).
- **Rimuovere o disabilitare gli account predefiniti** o cambiare tutte le password predefinite.
- **Disabilitare funzionalità** e componenti software non necessari.
- **Configurare l'autenticazione** in conformità con la politica di autenticazione dell'organizzazione.
- **Abilitare la registrazione e gli audit trail** per gli eventi rilevanti per la sicurezza.
- **Applicare le patch di sicurezza correnti** prima del posizionamento in produzione.
- **Configurare la cifratura** per i dati a riposo e in transito dove applicabile.
- **Limitare l'accesso amministrativo** al personale autorizzato con AMF.

### Obiettivi di conformità all'hardening

| Livello di asset | Controlli di sicurezza critici | Conformità complessiva all'hardening | Lacune accettabili |
|------------|---------------------------|------------------------------|-----------------|
| **Livello 1 (Critico)** | 100% | 95% o superiore | 0 lacune critiche |
| **Livello 2 (Alto)** | 95% o superiore | 90% o superiore | Meno di 5 lacune critiche |
| **Livello 3 (Medio)** | 90% o superiore | 80% o superiore | Meno di 10 lacune critiche |
| **Livello 4 (Basso)** | 80% o superiore | 70% o superiore | Best effort |

**Controlli di sicurezza critici**: Applicazione dell'autenticazione, impostazioni di cifratura, configurazione della registrazione, applicazione del controllo degli accessi e aggiornamento delle patch.

### Verifica dell'hardening

La conformità all'hardening deve essere verificata attraverso scansioni periodiche:

| Livello di asset | Frequenza della scansione automatizzata | Verifica manuale (se automazione non disponibile) |
|------------|--------------------------|------------------------------------------------|
| **Livello 1 (Critico)** | Trimestrale | Semestrale |
| **Livello 2 (Alto)** | Semestrale | Annuale |
| **Livello 3/4 (Medio/Basso)** | Annuale | Annuale |

Gli strumenti di verifica possono includere: OpenSCAP, Nessus, Qualys, Tenable, strumenti di conformità cloud-native (ad es. AWS Security Hub, Azure Defender for Cloud) o piattaforme equivalenti.

I risultati della scansione e i rapporti di conformità devono essere conservati per un minimo di **3 anni** a fini di audit.

### Remediation delle lacune

Le lacune di hardening identificate attraverso la verifica devono essere remediated in base al rischio:

| Rischio della lacuna | Tempistica di remediation | Approvazione dell'eccezione |
|----------|----------------------|--------------------|
| **Critico** | Meno di 30 giorni | Solo RSSI |
| **Alto** | Meno di 90 giorni | RSSI o Responsabile delle operazioni IT |
| **Medio** | Meno di 180 giorni | Responsabile delle operazioni IT |
| **Basso** | Best effort | Responsabile delle operazioni IT |

Le lacune che non possono essere remediated a causa di vincoli tecnici o requisiti aziendali devono essere documentate come eccezioni con controlli compensativi (vedere Gestione delle eccezioni di seguito).

**Framework dei controlli compensativi per le eccezioni di hardening** (requisiti specifici):

Scenario di eccezione: Una raccomandazione di hardening non può essere implementata (ad es. impossibile disabilitare un protocollo legacy, impossibile rimuovere un account predefinito, impossibile patchare un componente vulnerabile).

**Framework dei controlli compensativi** (difesa in profondità):

Esempio 1 — Impossibile disabilitare SMBv1 (dipendenza da applicazione legacy):
- Controlli compensativi:
  1. Isolamento di rete: Sistema in VLAN isolata, regole del firewall bloccano SMB dalle reti non affidabili.
  2. Restrizione degli accessi: Solo IP specifici del client legacy nella whitelist per l'accesso SMB (ACL).
  3. Monitoraggio avanzato: Firme IDS/IPS per tentativi di exploit SMBv1, alert sul traffico SMB insolito.
  4. Aggiornamento delle patch: Garantire che tutte le altre patch disponibili siano applicate (anche se SMBv1 non può essere disabilitato, patchare MS17-010 e simili).
  5. Piano di dismissione: Documentare il piano per la migrazione dall'applicazione legacy entro 12 mesi (l'eccezione non è indefinita).

Esempio 2 — Impossibile rimuovere l'account amministratore predefinito (dipendenza hardcoded dell'applicazione):
- Controlli compensativi:
  1. Rinominare l'account: Cambiare il nome dell'account da "Administrator" a un nome non ovvio.
  2. Password forte: Password casuale di 20+ caratteri archiviata in [Vault delle password].
  3. Applicazione AMF: Richiedere AMF per l'accesso all'account.
  4. Monitoraggio: Alert su qualsiasi uso dell'account, registrare tutte le azioni.
  5. Rotazione regolare della password: Ogni 90 giorni.

Esempio 3 — Impossibile patchare un componente vulnerabile (il fornitore non fornisce più patch, dismissione pianificata):
- Controlli compensativi:
  1. Isolamento di rete: Air-gapped o segmento di rete dedicato.
  2. Disabilitare l'accesso remoto: Nessun RDP/SSH dall'esterno della rete isolata.
  3. Virtual patching: Rilasciare regola IPS per bloccare i tentativi di exploit noti.
  4. Minimizzare i dati: Non archiviare dati RISERVATI sul sistema se possibile.
  5. Tempistica di dismissione: Piano documentato per la sostituzione del sistema entro 6 mesi.

**Valutazione dell'adeguatezza dei controlli compensativi**:
- I controlli devono ridurre il rischio a un livello accettabile (determinazione del RSSI).
- Difesa in profondità: Minimo 3 controlli compensativi richiesti per lacune Critiche/Alte.
- I controlli devono essere verificabili e auditabili (non solo "staremo attenti").

**Documentazione dell'eccezione** (nel Registro delle eccezioni):
- Raccomandazione di hardening che non può essere rispettata.
- Motivo aziendale/tecnico (perché la remediation non è possibile).
- Valutazione del rischio (qual è il rischio di non effettuare la remediation).
- Controlli compensativi (specifici, misurabili).
- Approvazione: Firma del RSSI.
- Frequenza di revisione: Trimestrale per lacune Critiche, semestrale per Alte/Medie.
- Scadenza: Massimo 12 mesi; deve essere nuovamente giustificata se ancora necessaria.

**Metriche delle eccezioni**:
- Totale eccezioni attive: Tendenza al ribasso nel tempo.
- Eccezioni più vecchie di 12 mesi: Obiettivo 0 (richiede nuova approvazione o remediation).
- Eccezioni senza controlli compensativi adeguati: 0 (remediation o potenziamento dei controlli).

---

## Audit della configurazione

### Audit interni della configurazione

L'organizzazione deve condurre audit periodici della configurazione per verificare che:

- I sistemi siano conformi alle configurazioni di base approvate.
- La documentazione della configurazione sia accurata e aggiornata.
- I processi di controllo delle modifiche siano stati seguiti per le modifiche alla configurazione.
- La copertura del monitoraggio soddisfi gli obiettivi definiti.
- La conformità all'hardening soddisfi le soglie definite.

**Frequenza degli audit**:

- **Annuale**: Audit completo della configurazione su tutti i livelli di asset.
- **Trimestrale**: Audit mirato degli asset di livello 1 e livello 2.
- **Ad hoc**: A seguito di incidenti significativi, importanti cambiamenti tecnologici o risultati normativi.

### Evidenze dell'audit

Gli audit della configurazione devono produrre evidenze documentate incluse:

- Risultati della scansione di conformità della configurazione di base.
- Record delle modifiche alla configurazione per il periodo di audit.
- Rapporti di rilevamento delle derive e registri di remediation.
- Punteggi di conformità all'hardening per tipo di asset.
- Revisione del registro delle eccezioni.
- Valutazione della copertura del monitoraggio.

I risultati dell'audit devono essere segnalati al RSSI e inclusi nel processo di revisione della direzione.

---

## Modifiche alla configurazione d'emergenza

Le modifiche alla configurazione d'emergenza sono affrontate principalmente dalla **Politica di gestione delle modifiche (A.8.32)**. I requisiti specifici della configurazione per le modifiche d'emergenza includono:

- Il sistema deve essere ripristinato a uno stato di configurazione documentato e noto come corretto il più rapidamente possibile.
- Se la modifica d'emergenza risulta in un nuovo stato di configurazione (non un ritorno alla configurazione di base), la configurazione di base deve essere aggiornata attraverso il processo standard di approvazione entro **5 giorni lavorativi**.
- Tutte le modifiche alla configurazione d'emergenza devono essere registrate con: i parametri di configurazione specifici modificati, i valori precedenti, i nuovi valori, la persona che ha apportato la modifica e la giustificazione aziendale.
- La revisione retrospettiva del RSSI o del delegato deve avvenire entro **48 ore**.

Le modifiche alla configurazione d'emergenza non devono superare il **10%** di tutte le modifiche alla configurazione in qualsiasi mese di calendario. Il superamento di questa soglia attiva una revisione del processo.

---

## Definizioni

| Termine | Definizione |
|------|------------|
| **Configurazione di base** | Insieme documentato di parametri di configurazione della sicurezza e operativi per un tipo di asset, che serve come riferimento per il rilascio, la verifica della conformità e il rilevamento delle derive |
| **Deriva della configurazione** | Deviazione della configurazione effettiva del sistema dalla configurazione di base approvata, che potrebbe indicare modifiche non autorizzate, lacune del processo o errori di documentazione |
| **Elemento di configurazione (CI)** | Qualsiasi asset, servizio o componente gestito attraverso la gestione della configurazione, monitorato con attributi e relazioni definiti |
| **CMDB** | Database di gestione della configurazione — repository che archivia le configurazioni di base, le configurazioni degli asset, la cronologia delle modifiche e le relazioni tra gli elementi di configurazione |
| **CIS Benchmark** | Guida alla configurazione di sicurezza basata sul consenso pubblicata dal Center for Internet Security per piattaforme e tecnologie specifiche |
| **Golden image** | Immagine di sistema pre-configurata che implementa la configurazione di base approvata, utilizzata per il rilascio rapido e coerente di nuovi sistemi |
| **Hardening** | Processo di messa in sicurezza delle configurazioni di sistema implementando standard di sicurezza riconosciuti e rimuovendo servizi, account, porte e funzionalità non necessari |
| **Infrastructure as Code (IaC)** | Pratica di gestione delle configurazioni di base e del provisioning dell'infrastruttura attraverso codice leggibile da macchina archiviato nel controllo versione |
| **Funzionalità minima** | Principio di configurazione dei sistemi per fornire solo le capacità richieste per il loro scopo previsto |
| **Build standard** | Configurazione di sistema approvata, testata e documentata utilizzata come base per il rilascio di nuove istanze di un tipo di asset specifico |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|------|-----------------|
| **RSSI** | Proprietà della politica; autorità di approvazione della configurazione di base e delle eccezioni; punto di escalation per le derive; supervisione della conformità all'hardening; reportistica alla Direzione generale |
| **Responsabile delle operazioni IT** | Operazioni di gestione della configurazione quotidiane; manutenzione del repository delle configurazioni di base; coordinamento del monitoraggio; reportistica delle metriche al RSSI |
| **Team di sicurezza** | Selezione e revisione degli standard di hardening; validazione della sicurezza delle configurazioni di base; indagine sugli alert di deriva; scansione della conformità; supporto all'audit |
| **Proprietari dei sistemi** | Responsabilità per la conformità alla configurazione dei sistemi di proprietà; approvazione delle modifiche per i sistemi di proprietà; remediation tempestiva delle derive; allocazione delle risorse per l'hardening |
| **Amministratori di sistema / Ingegneri DevOps** | Implementazione della configurazione di base; creazione e manutenzione delle golden image; configurazione del monitoraggio della configurazione; esecuzione delle modifiche approvate; triage e remediation delle derive |
| **Change Manager / CAB** | Approvazione delle modifiche alla configurazione (normali e d'emergenza); revisione post-implementazione; monitoraggio del successo delle modifiche |
| **Auditor interni / esterni** | Verifica indipendente della conformità alla configurazione; revisione delle evidenze; reportistica dei risultati |

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa politica:

| # | Evidenza | Proprietario | Frequenza | Conservazione |
|---|----------|-------|-----------|-----------|
| 1 | **Repository delle configurazioni di base** con cronologia delle versioni, record di approvazione e date di revisione per tipo di asset | Responsabile delle operazioni IT | Mantenuto continuamente; revisionato annualmente (trimestralmente per il livello 1) | Vita del tipo di asset + 3 anni |
| 2 | **Inventario delle golden image** con versione, data di creazione, livello delle patch e record di validazione | Amministratori di sistema / DevOps | Mantenuto continuamente; aggiornato mensilmente (livello 1/2) o trimestralmente (livello 3/4) | Vita dell'immagine + 1 anno |
| 3 | **CMDB o inventario della configurazione** che mostra gli elementi di configurazione, le configurazioni di base applicate e lo stato di conformità corrente | Responsabile delle operazioni IT | Mantenuto continuamente; auditato trimestralmente | Attivo + 3 anni |
| 4 | **Record delle modifiche alla configurazione** (richieste di modifica, approvazioni, log di implementazione, verifica post-modifica) | Change Manager | Per modifica; auditato trimestralmente | 3 anni (7 anni per evidenze di audit) |
| 5 | **Rapporti di rilevamento delle derive** e log degli alert con esiti del triage, registri di remediation e risultati della verifica post-remediation | Team di sicurezza / Operazioni IT | Continuamente; revisionato mensilmente | 3 anni |
| 6 | **Risultati della scansione di conformità all'hardening** per tipo di asset che mostrano la percentuale di conformità e le lacune identificate | Team di sicurezza | Per calendario di scansione (trimestrale o annuale per livello) | 3 anni |
| 7 | **Registro delle remediation delle lacune** con descrizione della lacuna, valutazione del rischio, proprietario, data di scadenza, stato ed evidenza di chiusura | Responsabile delle operazioni IT | Mantenuto continuamente; revisionato mensilmente | Durata della lacuna + 3 anni |
| 8 | **Registro delle eccezioni** per le deviazioni dalla configurazione (richiesta, giustificazione, controlli compensativi, approvazione, data di scadenza) | RSSI | Mantenuto continuamente; revisionato trimestralmente | Durata dell'eccezione + 3 anni |
| 9 | **Rapporti degli audit della configurazione** (interni ed esterni) con risultati e azioni correttive | RSSI / Auditor | Annuale (completo) + trimestrale (mirato) | 3 anni |
| 10 | **Record delle modifiche alla configurazione d'emergenza** con giustificazione, approvazione, revisione retrospettiva e conferma dell'aggiornamento della configurazione di base | RSSI | Per evento; revisione retrospettiva entro 48 ore | 3 anni |
| 11 | **Log di accesso e modifica del repository IaC** (cronologia dei commit, revisioni delle pull request, record di rilascio) | DevOps / Operazioni IT | Continuamente | 3 anni |
| 12 | **Rapporto sulla copertura del monitoraggio** che mostra la percentuale di asset sotto monitoraggio automatizzato della configurazione per livello, incluso lo stato del Registro delle lacune di monitoraggio | Responsabile delle operazioni IT | Mensile | 1 anno |
| 13 | **Evidenze di conformità alla configurazione SOC 2** — Rapporti trimestrali che mostrano che i sistemi di livello 1/2 soddisfano le configurazioni di base di hardening, con esportazioni di configurazione campione e risultati delle scansioni | Team di sicurezza | Trimestrale prima dell'audit SOC 2 | 3 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui valutazioni della copertura delle configurazioni di base, rapporti di monitoraggio della configurazione, scansioni di conformità all'hardening, record di rilevamento e remediation delle derive, audit della documentazione delle modifiche, audit interni ed esterni, e feedback al proprietario della politica.

**Metriche di conformità**:

| Metrica | Obiettivo | Frequenza di misurazione |
|--------|--------|-----------------------|
| Tipi di asset di livello 1 con configurazioni di base documentate e approvate | 100% | Trimestrale |
| Tipi di asset di livello 2 con configurazioni di base documentate e approvate | 100% | Trimestrale |
| Tipi di asset di livello 3/4 con configurazioni di base documentate e approvate | >= 80% | Trimestrale |
| Asset di livello 1 e livello 2 sotto monitoraggio automatizzato della configurazione | >= 95% | Mensile |
| Alert di deriva remediati entro SLA | >= 90% | Mensile |
| Remediation delle derive con verifica post-remediation completata | 100% | Mensile |
| Conformità all'hardening per i controlli di sicurezza critici (livello 1) | >= 95% | Trimestrale |
| Modifiche alla configurazione d'emergenza come percentuale di tutte le modifiche | < 10% | Mensile |
| Risultati degli audit della configurazione chiusi entro le tempistiche concordate | >= 90% | Trimestrale |
| Golden image aggiornate secondo il piano (mensile per livello 1/2, trimestrale per livello 3/4) | 100% | Mensile |
| Chiusura delle lacune di monitoraggio entro SLA per livello | >= 90% | Trimestrale |
| Eccezioni di hardening più vecchie di 12 mesi | 0 | Trimestrale |

**Gestione della non conformità**: Le metriche al di sotto del 70% richiedono un'escalation immediata al RSSI e un piano di remediation con tempistiche definite. Le metriche tra il 70% e l'89% richiedono la supervisione del Responsabile delle operazioni IT con revisioni mensili dei progressi. Le metriche al 90% e oltre seguono il monitoraggio trimestrale standard.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata dal RSSI preventivamente, con accettazione del rischio documentata, controlli compensativi e una data di scadenza definita (massimo 12 mesi). Le eccezioni devono essere revisionate trimestralmente e segnalate al Team di revisione della direzione. Le eccezioni scadute devono attivare la remediation o il rinnovo formale attraverso il processo standard di approvazione.

## Non conformità

Un dipendente che viola questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. L'apportare modifiche alla configurazione non autorizzate ai sistemi di produzione, la disabilitazione dei controlli di sicurezza, il bypass della gestione delle modifiche o la dissimulazione della deriva della configurazione sono considerati violazioni gravi.

## Miglioramento continuo

Questa politica viene revisionata e aggiornata come parte del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti agli standard di hardening del settore (nuove versioni dei CIS Benchmark, aggiornamenti delle guide di sicurezza dei fornitori), le minacce emergenti e le tecniche di attacco che prendono di mira le configurazioni errate, i cambiamenti tecnologici (nuove piattaforme, adozione di servizi cloud, containerizzazione), le modifiche normative, i risultati degli audit e le lezioni apprese dagli incidenti legati alla configurazione.

---

# Aree della norma ISO 27001 affrontate

Politica di gestione della configurazione — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 5.37 Procedure operative documentate |
| Clausola 8.1 Pianificazione e controllo operativi | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | **8.9 Gestione della configurazione** |
| | 8.8 Gestione delle vulnerabilità tecniche |
| | 8.32 Gestione delle modifiche |

**Quadro normativo e legale**:

| Quadro | Pertinenza |
|-----------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la sicurezza dei dati; la gestione sicura della configurazione come misura tecnica fondamentale a protezione dei sistemi che trattano dati personali |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati; la gestione della configurazione supporta i requisiti di controllo degli accessi, registrazione e integrità del sistema |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento; la gestione sicura della configurazione come misura tecnica e organizzativa appropriata |
| ISO/IEC 27001:2022 | Controllo Annex A 8.9 — Gestione della configurazione |
| ISO/IEC 27002:2022 | Sezione 8.9 — Linee guida di implementazione per la gestione della configurazione (nuovo controllo nell'edizione 2022) |
| NIST SP 800-128 | Guida per la gestione della configurazione orientata alla sicurezza dei sistemi informativi |
| NIST SP 800-53 Rev 5 | CM-2 (Configurazione di base), CM-3 (Controllo delle modifiche alla configurazione), CM-6 (Impostazioni di configurazione), CM-7 (Funzionalità minima), CM-8 (Inventario dei componenti del sistema) |
| CIS Controls v8 | Controllo 4: Configurazione sicura degli asset e del software aziendali (Salvaguardie 4.1–4.12) |
| CIS Benchmarks | Guide di hardening specifiche per piattaforma (Windows, Linux, macOS, piattaforme cloud, dispositivi di rete, database) |

---

<!-- QA_VERIFIED: 2026-04-03 -->

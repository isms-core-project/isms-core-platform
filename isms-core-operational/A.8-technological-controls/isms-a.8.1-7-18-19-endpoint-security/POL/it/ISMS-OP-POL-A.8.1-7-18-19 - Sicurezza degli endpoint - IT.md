<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.1-7-18-19-IT:operational:OP-POL:a.8.1-7-18-19 -->
**ISMS-OP-POL-A.8.1-7-18-19 — Sicurezza degli endpoint**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza degli endpoint |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.1-7-18-19 |
| **Creatore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione esecutiva |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controlli A.8.1, A.8.7, A.8.18, A.8.19 — Dispositivi endpoint degli utenti, protezione contro i malware, uso di programmi di utilità con privilegi, installazione di software sui sistemi operativi

**Controlli Allegato A correlati**:

| Controllo | Relazione con la sicurezza degli endpoint |
|-----------|-------------------------------------------|
| A.5.9 Inventario delle informazioni e delle altre risorse associate | Inventario dei dispositivi endpoint e registro delle risorse |
| A.5.15–18 Controllo degli accessi e gestione delle identità | Autenticazione degli utenti e diritti di accesso sugli endpoint |
| A.8.2 Diritti di accesso privilegiato | Gestione degli accessi privilegiati sui dispositivi endpoint |
| A.8.5 Autenticazione sicura | Meccanismi di autenticazione per l'accesso agli endpoint |
| A.8.8 Gestione delle vulnerabilità tecniche | Patch management per sistemi operativi e applicazioni degli endpoint |
| A.8.9 Gestione della configurazione | Baseline di configurazione degli endpoint e hardening |
| A.8.20 Sicurezza di rete | Requisiti di ammissione alla rete per i dispositivi endpoint |
| A.8.24 Uso della crittografia | Crittografia completa del disco (FDE) per i dispositivi endpoint |

**Politiche interne correlate**:

- Politica di controllo degli accessi
- Politica sull'uso della crittografia
- Politica di sicurezza di rete
- Politica di gestione delle risorse
- Politica di classificazione e gestione delle informazioni
- Politica di gestione degli incidenti

---

# Politica di sicurezza degli endpoint

## Scopo

La presente politica ha lo scopo di gestire e proteggere i dispositivi endpoint dell'organizzazione e di mitigare il rischio di malware, software non autorizzato e uso improprio dei programmi di utilità con privilegi.

La presente politica supporta la nLPD svizzera (revDSG) e l'Ordinanza sulla protezione dei dati (OPDo) implementando misure tecniche e organizzative proporzionate al rischio per proteggere i dati personali (compresi i dati personali degni di particolare protezione) sui dispositivi endpoint. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR.

## Ambito di applicazione

Tutti i dipendenti e gli utenti di terze parti.

Tutti i dispositivi di proprietà dell'organizzazione (laptop, desktop, telefoni cellulari, tablet).

Tutti i dispositivi utilizzati per accedere, trattare, trasmettere o memorizzare informazioni dell'organizzazione, inclusi i dispositivi di proprietà personale ove sia consentito il BYOD.

Dispositivi virtuali ed endpoint cloud-hosted ove applicabile e fattibile.

## Principio

I dispositivi dell'organizzazione devono avere un'adeguata protezione delle informazioni dal rischio di malware, software non autorizzato e perdita o furto. Gli endpoint sono gestiti secondo il principio del privilegio minimo con sicurezza by design e by default.

---

## Dispositivi endpoint degli utenti

### Registrazione e inventario dei dispositivi

Tutti i dispositivi endpoint devono essere registrati nel registro delle risorse prima di essere assegnati agli utenti. Il registro deve registrare il tipo di dispositivo, il numero seriale, l'utente assegnato, il sistema operativo, lo stato di crittografia e la data di assegnazione.

I dispositivi persi, rubati, dismessi o riassegnati devono essere aggiornati tempestivamente nel registro delle risorse.

### Baseline di configurazione degli endpoint

Tutti i dispositivi endpoint devono essere configurati secondo una baseline di sicurezza documentata prima della distribuzione. La baseline deve includere:

- Sistema operativo rafforzato (hardening) secondo le linee guida del fornitore e CIS Benchmark (Livello 1 minimo; Livello 2 per i sistemi che trattano dati riservati o dati personali sensibili).
- Servizi, porte e account predefiniti non necessari disabilitati o rimossi.
- Crittografia completa del disco (FDE) abilitata (vedere la sezione Crittografia di seguito).
- Protezione antimalware installata e attiva (vedere la sezione Protezione antimalware di seguito).
- Blocco schermo e timeout di sessione configurati.
- Firewall locale abilitato.
- Aggiornamenti automatici del sistema operativo e delle applicazioni abilitati.

La baseline di configurazione deve essere documentata e sotto controllo delle versioni. Gli standard della baseline devono fare riferimento alle guide di hardening del fornitore e ai CIS Benchmark. La baseline deve essere rivista almeno annualmente o quando si verificano modifiche significative al sistema operativo o al panorama delle minacce.

### Strumenti di gestione degli endpoint

Le seguenti categorie di strumenti di gestione devono essere distribuite a supporto della sicurezza degli endpoint:

| Categoria | Scopo | Esempi |
|-----------|-------|--------|
| **Endpoint Detection and Response (EDR)** | Rilevamento delle minacce, indagine e risposta sugli endpoint | CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne o equivalente |
| **Mobile Device Management (MDM)** | Registrazione del dispositivo, configurazione, conformità, cancellazione remota | Jamf Pro, Microsoft Intune, VMware Workspace ONE o equivalente |
| **Patch Management** | Distribuzione automatizzata e reportistica di conformità per le patch di SO e applicazioni | WSUS, Jamf Pro, ManageEngine o equivalente |
| **Escrow delle chiavi di crittografia** | Conservazione centralizzata delle chiavi di ripristino per la crittografia completa del disco | Integrato MDM o gestione dedicata delle chiavi |
| **Approvazione software** | Allow-listing delle applicazioni e controllo delle installazioni | AppLocker, Santa, catalogo applicazioni MDM o equivalente |

### Crittografia

Tutti i dispositivi endpoint (laptop, desktop, dispositivi mobili) devono avere la crittografia completa del disco (FDE) abilitata:

| Piattaforma | Tecnologia di crittografia | Standard minimo |
|-------------|---------------------------|-----------------|
| Windows | BitLocker | AES-XTS 256 bit |
| macOS | FileVault | XTS-AES 128 bit |
| Mobile (iOS/Android) | Crittografia nativa del dispositivo | Abilitata per impostazione predefinita; verifica attivazione |
| Linux | LUKS / dm-crypt | AES-XTS 256 bit |

- La crittografia del dispositivo non deve essere disabilitata dall'utente finale.
- Le chiavi di ripristino devono essere archiviate in modo centralizzato tramite MDM (es. Jamf Pro, Intune o equivalente) o soluzione equivalente di escrow delle chiavi gestita dall'IT. L'accesso alle chiavi di ripristino deve essere registrato e limitato al personale IT autorizzato.
- Lo stato di crittografia deve essere verificato prima che il dispositivo sia approvato per l'uso con dati riservati.

### Blocco schermo e timeout di sessione

- I dispositivi devono bloccarsi automaticamente dopo **15 minuti** di inattività. I dispositivi con accesso a dati riservati o dati personali sensibili devono bloccarsi dopo **5 minuti** di inattività.
- Gli utenti devono bloccare manualmente i propri dispositivi quando si allontanano (Windows+L, Ctrl+Command+Q o equivalente).
- Per sbloccare è richiesta l'autenticazione (password, PIN o biometria).
- Il blocco alla sospensione e alla chiusura del coperchio deve essere abilitato su tutti i laptop.

### Sicurezza fisica

- I dispositivi non devono essere lasciati incustoditi in luoghi pubblici o visibili in veicoli incustoditi.
- I lucchetti a cavo dovrebbero essere utilizzati per i dispositivi desktop in aree condivise o pubbliche.
- I dispositivi portatili devono essere conservati in modo sicuro quando non sono in uso (cassetto o armadietto chiuso a chiave).
- La perdita o il furto di qualsiasi dispositivo devono essere segnalati immediatamente al team di gestione della sicurezza delle informazioni.

### Cancellazione remota

L'organizzazione deve mantenere la capacità di cancellare o bloccare da remoto i dispositivi persi o rubati tramite la piattaforma MDM o strumento di gestione equivalente.

Procedura di cancellazione remota:

1. Dispositivo segnalato come perso o rubato — il dipendente notifica immediatamente l'IT e il responsabile diretto.
2. L'IT avvia il **blocco remoto** entro **1 ora** dalla notifica durante l'orario lavorativo (all'inizio del successivo giorno lavorativo per le segnalazioni fuori orario).
3. Se il dispositivo non viene recuperato entro **24 ore**, l'IT avvia la **cancellazione remota**.
4. La conferma della cancellazione remota deve essere documentata, inclusi data, ID dispositivo, stato della cancellazione (confermata/in attesa) e persona che ha autorizzato.
5. Laddove venga cancellato un dispositivo BYOD, devono essere cancellati solo il contenitore dell'organizzazione o il profilo di lavoro (non i dati personali), salvo che il dipendente abbia acconsentito alla cancellazione completa nell'accordo BYOD.

### BYOD (Bring Your Own Device)

Se l'organizzazione consente ai dispositivi di proprietà personale di accedere alle informazioni dell'organizzazione, si applicano i seguenti requisiti:

- Il dispositivo deve essere registrato nella soluzione MDM dell'organizzazione.
- I dati aziendali devono essere separati dai dati personali utilizzando la containerizzazione o un profilo di lavoro gestito.
- Il dispositivo deve soddisfare la stessa baseline di sicurezza dei dispositivi di proprietà dell'organizzazione (crittografia, blocco schermo, SO aggiornato, protezione antimalware).
- L'organizzazione si riserva il diritto di cancellare da remoto i dati dell'organizzazione (non i dati personali) dal dispositivo.
- Gli utenti devono riconoscere le proprie responsabilità, incluse la protezione fisica, gli aggiornamenti software e la cooperazione con i requisiti di sicurezza.
- L'accesso BYOD deve essere revocato alla cessazione del rapporto di lavoro o alla fine del contratto per la Politica di controllo degli accessi.

### Procedura di registrazione BYOD

1. Il dipendente invia la richiesta di accesso BYOD all'IT, specificando il tipo di dispositivo, il sistema operativo e l'ambito di utilizzo aziendale previsto.
2. L'IT verifica che il dispositivo soddisfi i requisiti minimi (versione SO supportata, capacità di crittografia, assenza di jailbreak/root).
3. Il dipendente firma l'accordo BYOD riconoscendo i requisiti di sicurezza, il consenso alla cancellazione remota per i dati dell'organizzazione e gli obblighi di cooperazione.
4. L'IT registra il dispositivo nell'MDM e configura il profilo di lavoro gestito o il contenitore.
5. L'IT verifica la conformità alla baseline di sicurezza (crittografia attiva, blocco schermo configurato, SO aggiornato) prima di concedere l'accesso.

Se il BYOD non è consentito, ciò deve essere dichiarato e applicato tramite controlli tecnici.

---

## Protezione antimalware e antivirus

### Software approvato

Solo software approvato e concesso in licenza dall'organizzazione deve essere installato sulle attrezzature dell'organizzazione.

Software non autorizzato, software scaricato, freeware o utilità non approvate non devono essere installati.

### Requisiti di protezione antimalware

Il software di protezione antimalware (endpoint detection and response — EDR, o antivirus di nuova generazione — NGAV, appropriato al profilo di rischio dell'organizzazione) deve essere installato su ogni dispositivo in grado di eseguirlo.

Il software di protezione antimalware deve:

- Aggiornare automaticamente le definizioni di rilevamento e i motori non appena rilasciati dal fornitore.
- Non essere modificato, disabilitato o disinstallato dall'utente finale.
- Produrre un avviso quando si verifica un'infezione o un'infezione sospetta.
- Essere impostato per riparare automaticamente o mettere in quarantena i file sospetti.
- Eseguire automaticamente la scansione dello storage locale e dei dispositivi di storage collegati.
- Eseguire automaticamente la scansione di qualsiasi file a cui si accede, che viene modificato o eseguito.
- Conservare i log di audit inoltrati al sistema di registrazione centralizzato.

Le infezioni sospette devono essere gestite tramite il processo di gestione degli incidenti. I seguenti eventi devono attivare un rapporto di incidente:

- Avviso EDR/antivirus che indica il rilevamento confermato di malware (non falso positivo).
- Indicatori di ransomware (attività di crittografia dei file, file di richiesta di riscatto).
- Connessioni in uscita non autorizzate verso infrastrutture command-and-control note.
- Comportamenti sospetti segnalati dagli utenti (pop-up inaspettati, degrado delle prestazioni, processi sconosciuti).
- Rilevamento di software o strumenti non autorizzati sul dispositivo.

### Protezione e-mail

I server e i gateway e-mail devono disporre di scansione antimalware che ispeziona tutte le e-mail in entrata e in uscita, inclusi gli allegati.

### Protezione web gateway

I proxy Internet o i secure web gateway devono essere configurati per:

- Bloccare i siti con reputazioni malevole note.
- Eseguire la scansione dei contenuti per le minacce sui siti con reputazioni intermedie.
- Registrare tutti i rilevamenti.
- Controllare automaticamente la disponibilità di aggiornamenti delle definizioni.

L'allow-listing e il deny-listing devono essere distribuiti per controllare l'accesso alle risorse web approvate e vietate.

### Monitoraggio dell'integrità dei file

Il monitoraggio dell'integrità dei file deve essere implementato per i file critici del sistema e i file che contengono o forniscono accesso a dati personali o riservati, in base al rischio e alle esigenze aziendali.

### Controlli sui supporti rimovibili

- L'avvio automatico (autorun e autoplay) deve essere disabilitato per tutti i supporti rimovibili.
- I supporti rimovibili devono essere automaticamente sottoposti a scansione antimalware quando vengono collegati.
- Solo i supporti rimovibili di proprietà dell'organizzazione e crittografati devono essere approvati per l'uso con dati riservati, in linea con la Politica di trasferimento delle informazioni.

---

## Formazione

Gli utenti devono essere periodicamente formati nell'ambito del programma di sensibilizzazione alla sicurezza su:

- Riconoscimento delle e-mail di phishing e degli attacchi di ingegneria sociale.
- Uso sicuro di Internet e della posta elettronica.
- Utilizzo del software approvato e divieto di software non approvato.
- Come comportarsi in caso di sospetta infezione da malware.
- Sicurezza fisica dei dispositivi (blocco, conservazione, segnalazione di perdita/furto).

---

## Programmi di utilità con privilegi

### Ambito

I programmi di utilità con privilegi sono strumenti che possono superare i controlli di sistema o applicazione. Questi includono, a titolo esemplificativo e non esaustivo:

- Strumenti di amministrazione del sistema (gestione di utenti/gruppi, gestione dei servizi).
- Editor del registro di sistema, PowerShell (policy di esecuzione senza restrizioni) e strumenti a riga di comando con privilegi elevati.
- Diagnostica, debugger e utilità disco.
- Utilità di backup e ripristino con accesso ai dati grezzi.
- Strumenti di gestione e scansione di rete.

### Controlli

- L'accesso ai programmi di utilità con privilegi deve essere limitato al solo personale autorizzato, in base al principio del privilegio minimo.
- L'autenticazione a più fattori (AMF) deve essere richiesta per l'accesso ai programmi di utilità con privilegi sui sistemi critici.
- Tutta l'esecuzione dei programmi di utilità con privilegi deve essere registrata, inclusi utente, timestamp, nome dell'utilità e sistema di destinazione.
- I programmi di utilità con privilegi non necessari per scopi operativi devono essere rimossi o disabilitati.
- L'uso dei programmi di utilità con privilegi deve essere soggetto a revisione periodica (almeno trimestrale) per verificare la continuità della giustificazione aziendale.
- L'organizzazione deve mantenere un elenco documentato dei programmi di utilità con privilegi approvati per ruolo.

---

## Installazione di software sui sistemi operativi

### Controlli sull'installazione del software

- L'installazione di software sui sistemi operativi deve essere eseguita solo da personale autorizzato (amministratori IT o personale di supporto designato).
- Gli utenti standard non devono avere diritti di amministratore locale. Laddove sia necessaria l'elevazione, deve essere utilizzato un meccanismo gestito di escalation dei privilegi:
  - **Accesso just-in-time (JIT)**: Elevazione temporanea concessa per un periodo definito (massimo 4 ore), revocata automaticamente alla scadenza.
  - **Flusso di approvazione**: L'utente invia la richiesta con giustificazione aziendale; l'IT o il responsabile diretto approva; l'elevazione viene concessa e registrata.
  - Tutte le escalation dei privilegi devono essere registrate (utente, timestamp, giustificazione, durata, approvatore).
- Tutte le installazioni di software devono seguire il processo di gestione delle modifiche dell'organizzazione, inclusi test, approvazione e documentazione.
- Solo il software approvato dal catalogo software dell'organizzazione deve essere installato. Le richieste di nuovo software devono essere sottoposte attraverso un processo formale di approvazione.

### Patch management

I sistemi operativi, le applicazioni e il software del browser sui dispositivi endpoint devono essere mantenuti aggiornati. Le patch di sicurezza devono essere applicate secondo i seguenti tempi:

| Gravità | Tempistica |
|---------|-----------|
| Vulnerabilità critiche (CVSS 9,0+, sfruttamento attivo) | Entro 14 giorni |
| Vulnerabilità alte (CVSS 7,0–8,9) | Entro 30 giorni |
| Vulnerabilità medie (CVSS 4,0–6,9) | Entro 90 giorni |
| Vulnerabilità basse (CVSS 0,1–3,9) | Prossima finestra di manutenzione programmata |

Le patch devono essere testate prima della distribuzione con il seguente approccio:

| Tipo di sistema | Requisito di test |
|----------------|------------------|
| Endpoint standard (laptop, desktop) | Distribuire a un **gruppo pilota** (5–10% dei dispositivi) per **48 ore** prima del rollout completo |
| Dispositivi mobili | Distribuire a un gruppo pilota tramite MDM per 48 ore prima del rollout completo |
| Endpoint specializzati (kiosk, sistemi da laboratorio) | Testare in ambiente non di produzione prima della distribuzione |

- **Patch d'emergenza P0** (sfruttamento attivo confermato) possono bypassare il test pilota con approvazione del RSSI. Sono richiesti il monitoraggio potenziato per 48 ore post-distribuzione e un piano di rollback documentato.
- **Gestione dei guasti delle patch**: Se una patch causa problemi operativi nel gruppo pilota, la distribuzione deve essere interrotta, il problema documentato e il fornitore contattato. Deve essere applicata una soluzione alternativa o un controllo compensativo fino a quando non sia disponibile una patch stabile.

Gli aggiornamenti automatici devono essere abilitati per i sistemi operativi e le applicazioni supportate. I dispositivi che non hanno applicato le patch critiche entro il termine definito devono essere contrassegnati per il rimedio o limitati nell'accesso alla rete.

### Rollback

Prima di applicare aggiornamenti o installazioni ai sistemi operativi deve essere concordata una strategia di rollback per garantire la continuità operativa nel caso in cui una patch causi problemi.

### Pista di audit

Deve essere mantenuto un registro di tutte le modifiche al software sui sistemi operativi, inclusi nome del software, versione, data di installazione e individuo che ha eseguito la modifica.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **RSSI** | Titolarità della politica; approvazione delle eccezioni e dei bypass delle patch d'emergenza; punto di escalation per la non conformità |
| **IT Operations / Team endpoint** | Provisioning dei dispositivi, configurazione baseline, gestione MDM, distribuzione delle patch, esecuzione della cancellazione remota |
| **Team di gestione della sicurezza delle informazioni** | Monitoraggio EDR, triage degli incidenti malware, revisioni dei programmi di utilità con privilegi, reportistica di conformità |
| **Proprietario delle risorse / Responsabile diretto** | Approvazione dell'assegnazione dei dispositivi, delle richieste BYOD e delle richieste software per il proprio team |
| **Tutti gli utenti** | Sicurezza fisica dei dispositivi, segnalazione immediata di perdita/furto, cooperazione con i requisiti di sicurezza, divieto di disabilitare i controlli di sicurezza |

---

## Prove

Le seguenti prove dimostrano la conformità alla presente politica:

| # | Prova | Responsabile | Frequenza |
|---|-------|-------------|-----------|
| 1 | **Inventario dei dispositivi endpoint** (registro delle risorse con stato di crittografia, versione SO, utente assegnato) | IT Operations | *Aggiornato per evento; audit completo annuale* |
| 2 | Documentazione della **baseline di configurazione degli endpoint** e report delle scansioni di conformità | IT Operations | *Baseline rivista annualmente; scansioni di conformità mensili* |
| 3 | Report di distribuzione e stato degli aggiornamenti della **protezione antimalware** (percentuale di copertura, aggiornamento delle definizioni) | Sicurezza delle informazioni | *Report mensili; obiettivo: copertura 100%* |
| 4 | **Log di rilevamento malware e degli incidenti** (rilevamenti, azioni di quarantena, escalation degli incidenti) | Sicurezza delle informazioni | *Rivisti mensilmente; conservati 12 mesi* |
| 5 | **Registrazioni delle installazioni software** e approvazioni della gestione delle modifiche | IT Operations | *Per evento; audit trimestrale* |
| 6 | Elenco approvato e log di utilizzo dei **programmi di utilità con privilegi** | Sicurezza delle informazioni | *Elenco rivisto trimestralmente; log conservati 12 mesi* |
| 7 | **Report di conformità delle patch** (percentuale di dispositivi aggiornati, patch in scaduto per gravità) | IT Operations | *Mensile; obiettivo: ≥95% aggiornati entro i tempi SLA* |
| 8 | **Registrazioni di registrazione BYOD** e stato di conformità MDM (se applicabile) | IT Operations | *Aggiornato per evento; rivisto semestralmente* |
| 9 | **Registrazioni di esecuzione della cancellazione remota** (ID dispositivo, data, stato della cancellazione, persona autorizzante) | IT Operations | *Per evento; conservato 3 anni* |
| 10 | **Registrazioni dei test delle patch nel gruppo pilota** (risultati dei test, problemi identificati, decisioni di rollout) | IT Operations | *Per ciclo di patch* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica tramite vari metodi, inclusi tra gli altri: scansioni di conformità degli endpoint, report di rilevamento malware, report sullo stato delle patch, audit dell'inventario software, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione alla presente politica deve essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni devono essere segnalate al Team di revisione della direzione.

## Non conformità

Un dipendente che risulti aver violato la presente politica può essere soggetto a provvedimenti disciplinari, fino al licenziamento.

## Miglioramento continuo

La presente politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono tener conto di modifiche agli standard di sicurezza degli endpoint, minacce emergenti (incluse nuove tecniche malware e vettori di attacco), modifiche normative e lezioni apprese dagli incidenti.

---

# Aree della norma ISO 27001 trattate

Politica di sicurezza degli endpoint — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **8.1 Dispositivi endpoint degli utenti** |
| | **8.7 Protezione contro i malware** |
| | **8.18 Uso di programmi di utilità con privilegi** |
| | **8.19 Installazione di software sui sistemi operativi** |
| | 8.23 Filtraggio web |

**Quadro normativo e legale**:

| Quadro | Rilevanza |
|--------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la protezione dei dati |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento (controlli degli endpoint come misura appropriata) |
| ISO/IEC 27001:2022 | Allegato A Controlli 8.1, 8.7, 8.18, 8.19 |
| ISO/IEC 27002:2022 | Sezioni 8.1, 8.7, 8.18, 8.19 — Guida all'implementazione |
| NIST SP 800-53 Rev 5 | SC-28 (Protezione delle informazioni a riposo), SI-3 (Protezione dal codice malevolo), CM-11 (Software installato dagli utenti) |
| CIS Controls v8 | Controllo 2 (Inventario e controllo delle risorse software), Controllo 4 (Configurazione sicura), Controllo 10 (Difese antimalware) |

---

<!-- QA_VERIFIED: 2026-04-03 -->

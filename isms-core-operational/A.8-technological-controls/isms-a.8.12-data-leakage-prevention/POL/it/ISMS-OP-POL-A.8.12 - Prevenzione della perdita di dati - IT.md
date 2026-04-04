<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.12-IT:operational:OP-POL:a.8.12 -->
**ISMS-OP-POL-A.8.12 — Prevenzione della perdita di dati**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Prevenzione della perdita di dati |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.12 |
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
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.12 — Prevenzione della perdita di dati
- ISO/IEC 27002:2022 Sezione 8.12 — Indicazioni di implementazione per la prevenzione della perdita di dati
- NIST SP 800-53 Rev 5 — AC-4 (Information Flow Enforcement), SC-7 (Boundary Protection), SI-4 (System Monitoring)
- CIS Controls v8 — Misura 3.13 (Deploy a Data Loss Prevention Solution), 3.1–3.14 (Data Protection)

**Controlli correlati dell'Annex A**:

| Controllo | Relazione con la prevenzione della perdita di dati |
|-----------|---------------------------------------------------|
| A.5.10 Uso accettabile delle informazioni e di altri asset correlati | Definisce le pratiche di gestione e trasferimento dei dati applicate dal DLP |
| A.5.12 Classificazione delle informazioni | La classificazione dei dati determina la gravità delle regole DLP e la modalità di applicazione |
| A.5.13 Etichettatura delle informazioni | Le etichette dei documenti abilitano il rilevamento del contenuto e la corrispondenza con le policy DLP |
| A.5.14 Trasferimento di informazioni | Le policy di trasferimento applicate tramite monitoraggio dei canali DLP |
| A.5.15–16–18 Gestione delle identità e degli accessi | Il contesto dell'identità utente viene utilizzato nella valutazione delle regole DLP e nella gestione delle eccezioni |
| A.5.24–28 Ciclo di vita della gestione degli incidenti | Gli avvisi DLP alimentano il flusso di lavoro della gestione degli incidenti e la notifica delle violazioni |
| A.5.34 Privacy e protezione dei dati personali | Il DLP impedisce la divulgazione non autorizzata dei dati personali; il diritto alla privacy limita l'ambito del monitoraggio |
| A.8.10 Cancellazione delle informazioni | Il DLP integra i controlli di cancellazione impedendo la conservazione su supporti rimovibili |
| A.8.11 Mascheratura dei dati | La mascheratura applicata prima della condivisione riduce il volume degli avvisi DLP e il rischio residuo |
| A.8.15 Registrazione degli eventi | Gli eventi DLP vengono registrati ai fini delle indagini, della correlazione e delle prove di conformità |
| A.8.16 Attività di monitoraggio | Il DLP genera eventi di sicurezza per l'integrazione SIEM e l'analisi comportamentale |
| A.8.20–22 Sicurezza della rete | La segmentazione della rete definisce il posizionamento dei sensori DLP e i punti di ispezione |
| A.8.23 Filtro web | Il filtro web e il DLP controllano congiuntamente i canali di esfiltrazione dei dati via web |
| A.8.24 Uso della crittografia | I canali crittografati possono richiedere l'ispezione TLS per l'analisi del contenuto DLP |

**Politiche interne correlate**:

- Politica di classificazione e gestione delle informazioni
- Politica di uso accettabile
- Politica di gestione degli incidenti
- Politica di registrazione degli eventi
- Politica delle attività di monitoraggio (A.8.16)
- Politica di sicurezza della rete
- Politica sulla privacy e la protezione dei dati personali
- Politica di filtro web

---

# Politica di prevenzione della perdita di dati

## Scopo

Lo scopo di questa politica è stabilire i requisiti per i controlli di prevenzione della perdita di dati (DLP) che rilevano, impediscono e gestiscono la divulgazione, il trasferimento o l'esfiltrazione non autorizzati di informazioni sensibili dai sistemi, dalle reti e dagli endpoint dell'organizzazione. I controlli DLP affrontano sia l'esfiltrazione dolosa (minacce interne, account compromessi, minacce persistenti avanzate) sia la divulgazione accidentale (errore dell'utente, configurazione errata, comunicazioni misdirette).

Questa politica supporta la nLPD (revDSG) svizzera all'Art. 8 implementando misure tecniche e organizzative adeguate al rischio per proteggere i dati personali trattati dall'organizzazione. Il monitoraggio DLP è implementato in conformità con il diritto del lavoro svizzero, in particolare l'Art. 26 OLL3 (divieto dei sistemi di sorveglianza comportamentale) e l'Art. 328b CO svizzero (trattamento proporzionato dei dati del dipendente). Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR all'Art. 32 (sicurezza del trattamento) e all'Art. 88 (trattamento nel contesto lavorativo).

## Impegni nei confronti dei clienti e protezione dei loro dati

I controlli DLP supportano gli impegni dell'organizzazione nei confronti dei clienti in merito alla protezione dei dati dei clienti da divulgazioni non autorizzate. I contratti con i clienti includono tipicamente impegni quali:

- "Il Fornitore di servizi implementerà misure tecniche e organizzative per impedire la divulgazione non autorizzata dei Dati del cliente."
- "Il Fornitore di servizi notificherà al Cliente entro [X ore] qualsiasi accesso non autorizzato o divulgazione dei Dati del cliente."
- "Il Fornitore di servizi manterrà sistemi di monitoraggio per rilevare e prevenire l'esfiltrazione dei dati."

### Requisiti di protezione dei dati dei clienti

I dati dei clienti trattati dall'organizzazione devono ricevere una protezione DLP proporzionale agli impegni contrattuali:

| Tipo di dati del cliente | Classificazione DLP | Livello di protezione | Requisito di notifica (in caso di fuga) |
|--------------------------|--------------------|-----------------------|----------------------------------------|
| **Dati personali del cliente** | Minimo Riservato | Monitoraggio e-mail + Web + Endpoint + Cloud; blocco verso destinatari esterni | Notifica al cliente entro [X ore] contrattualmente; notifica normativa ai sensi della nLPD Art. 24 |
| **Dati aziendali del cliente** (non dati personali) | Riservato o Interno | Monitoraggio e-mail + Web minimo; blocco o avviso in base ai termini contrattuali | Notifica al cliente entro [X ore] contrattualmente |
| **Credenziali/chiavi API del cliente** | Ristretto | Tutti i canali; blocco immediato + risposta agli incidenti | Notifica immediata al cliente (entro 1 ora) |
| **Dati aggregati/anonimizzati del cliente** | Interno | Solo monitoraggio; rilevamento focalizzato sul rischio di re-identificazione | Notifica al cliente in caso di sospetta de-anonimizzazione |

### Procedure di notifica al cliente

Quando gli incidenti DLP riguardano i dati dei clienti:

1. **Valutazione iniziale** (entro 1 ora): Determinare l'ambito, i clienti interessati, i tipi di dati e la durata dell'esposizione.
2. **Contenimento** (immediato): Bloccare il trasferimento, isolare i sistemi, revocare le credenziali se appropriato.
3. **Notifica al cliente** (in base ai termini contrattuali, tipicamente 4-24 ore):
   - Riepilogo dell'incidente (cosa è successo, quando è stato rilevato)
   - Tipi e volume di dati interessati
   - Clienti interessati (in caso di multi-tenant)
   - Azioni intraprese dall'organizzazione
   - Azioni raccomandate al cliente
   - Contatto per domande
4. **Notifica normativa** (se applicabile): nLPD Art. 24 (senza ritardo ingiustificato), GDPR Art. 33 (72 ore).
5. **Follow-up**: Rapporto di analisi delle cause profonde fornito ai clienti interessati entro [X giorni lavorativi].

**Requisiti specifici del cliente**: Laddove i clienti abbiano negoziato tempistiche di notifica personalizzate, soglie di gravità degli incidenti o requisiti di reporting, questi dovranno essere documentati nel registro dei contratti con i clienti e integrati nei flussi di lavoro di instradamento degli avvisi DLP e di risposta agli incidenti.

## Ambito di applicazione

Questa politica si applica a tutti gli asset informativi classificati come Interno, Riservato o Ristretto secondo lo schema di classificazione dei dati dell'organizzazione. Ciò include:

- Tutti i sistemi, le applicazioni, le reti, gli endpoint e i servizi che trattano, memorizzano o trasmettono informazioni organizzative.
- Tutti i canali di uscita dei dati: e-mail (SMTP, webmail), web (caricamenti HTTP/HTTPS), endpoint (USB, archiviazione locale, stampa), rete (protocolli di trasferimento file), servizi cloud (SaaS, archiviazione cloud), dispositivi mobili (aziendali e BYOD), e API applicative.
- Tutto il personale dell'organizzazione (dipendenti, collaboratori, personale temporaneo) con accesso alle informazioni organizzative.
- Tutti i fornitori terzi di servizi e servizi cloud che gestiscono dati organizzativi.
- Tutti i modelli di distribuzione (on-premises, ibrido, cloud-native).

**Fuori ambito**: Informazioni pubbliche che non richiedono protezione DLP. Sicurezza fisica dei documenti cartacei (disciplinata da A.7.x Controlli fisici). Processi di backup e archiviazione (disciplinati da A.8.13 Backup delle informazioni). Conservazione ed eliminazione dei dati (disciplinati da A.8.10 Cancellazione delle informazioni). Mascheratura e anonimizzazione dei dati (disciplinati da A.8.11 Mascheratura dei dati). Controlli di sicurezza delle informazioni non correlati all'esfiltrazione dei dati (il controllo degli accessi, l'autenticazione e la gestione delle patch sono trattati nei rispettivi controlli).

## Principio

Le misure di prevenzione della perdita di dati dovrebbero essere applicate ai sistemi, alle reti e a qualsiasi altro dispositivo che tratta, memorizza o trasmette informazioni sensibili (ISO 27001:2022 Controllo A.8.12).

L'organizzazione DEVE implementare controlli DLP proporzionati alla sensibilità delle informazioni protette e al rischio di divulgazione non autorizzata. I controlli DLP devono essere basati sulla classificazione: i requisiti di protezione aumentano con la sensibilità dei dati. L'organizzazione deve bilanciare il monitoraggio della sicurezza con i diritti alla privacy dei dipendenti, garantendo che il monitoraggio DLP sia trasparente, proporzionato e focalizzato sulla protezione dei dati piuttosto che sulla sorveglianza del comportamento dei dipendenti.

I controlli DLP non devono essere utilizzati per la valutazione delle prestazioni dei dipendenti, il monitoraggio dei tempi di lavoro o qualsiasi scopo diverso dalla sicurezza delle informazioni e dalla protezione dei dati.

---

## Integrazione con la classificazione dei dati

I controlli DLP devono essere applicati in base allo schema di classificazione dei dati dell'organizzazione. La classificazione determina la modalità di applicazione, la copertura dei canali e la priorità di risposta per ciascuna categoria di dati.

**Protezione DLP basata sulla classificazione**:

| Livello di classificazione | Requisito DLP | Modalità di applicazione |
|---------------------------|---------------|--------------------------|
| **Ristretto** | Monitoraggio e blocco DLP completi su tutti i canali di uscita | Blocco e avviso |
| **Riservato** | Monitoraggio e blocco DLP sui canali ad alto rischio (e-mail, web, endpoint, cloud) | Blocco o richiesta di giustificazione all'utente |
| **Interno** | Monitoraggio DLP sui canali di uscita principali (e-mail, web) | Monitoraggio e avviso (rilevamento senza blocco automatico) |
| **Pubblico** | Nessun controllo DLP richiesto | Non applicabile |

**Categorie di dati sensibili che richiedono protezione DLP**:

| Categoria di dati | Esempi | Normativa di riferimento |
|-------------------|--------|--------------------------|
| **Dati personali** | Nomi, indirizzi, numeri di identità nazionali, numeri AVS, numeri di telefono | nLPD svizzera, GDPR (se applicabile) |
| **Dati dei dipendenti** | Registri HR, buste paga, valutazioni delle prestazioni, informazioni sanitarie | nLPD svizzera, CO svizzero Art. 328b |
| **Credenziali di autenticazione** | Password, chiavi API, token, certificati, chiavi SSH | ISO 27001 A.5.17 |
| **Proprietà intellettuale** | Codice sorgente, progetti, brevetti, segreti commerciali, piani strategici | Rischio aziendale |
| **Dati dei clienti** | Elenchi clienti, contratti, prezzi, comunicazioni | Obblighi contrattuali |
| **Dati finanziari** | Numeri di conto bancario, dati di pagamento, bilanci finanziari | Rischio aziendale, contrattuale |

**Metodi di identificazione dei dati**:

L'organizzazione DEVE implementare più metodi di identificazione per rilevare le informazioni sensibili in transito:

- **Ispezione del contenuto**: Corrispondenza di pattern, espressioni regolari e rilevamento di parole chiave per dati strutturati (ad es. numeri di carta di credito, numeri di identità nazionali, numeri AVS).
- **Etichettatura dei documenti**: Metadati di classificazione incorporati nei file (intestazioni, piè di pagina, proprietà) che consentono al DLP di identificare i documenti sensibili indipendentemente dal contenuto.
- **Analisi contestuale**: Valutazione del sistema di origine, del ruolo dell'utente, della destinazione, del volume di trasferimento e dell'orario per valutare il livello di rischio.
- **Fingerprinting** (raccomandato): Tracciamento basato su hash per documenti di alto valore come codice sorgente, specifiche di progettazione e piani strategici.

L'organizzazione DEVE mantenere un inventario dei dati sensibili che richiedono protezione DLP, riconciliato trimestralmente con l'inventario degli asset (A.5.9). I pattern di rilevamento specifici, le regole regex e le etichette di classificazione devono essere documentati e mantenuti dal Team di sicurezza.

---

## Protezione dei canali

L'organizzazione DEVE implementare controlli DLP su tutti i canali di uscita dei dati per prevenire la divulgazione non autorizzata di informazioni. La copertura dei canali deve essere verificata tramite test tecnici almeno trimestralmente.

### Protezione della posta elettronica

Tutte le e-mail in uscita (SMTP e webmail) DEVONO essere soggette a ispezione del contenuto DLP:

- Scansione del corpo dei messaggi e degli allegati per individuare contenuti sensibili corrispondenti alle regole di rilevamento DLP.
- Convalida dei domini dei destinatari: distinguere destinatari interni, esterni attendibili ed esterni non attendibili.
- Blocco o quarantena dei messaggi contenenti dati Ristretti verso destinatari esterni.
- Avviso sui dati Riservati verso destinatari esterni (blocco o richiesta all'utente a seconda della classificazione e della destinazione).
- Supporto alla crittografia (S/MIME, TLS) per le e-mail sensibili approvate laddove esiste un'esigenza aziendale.
- Monitoraggio dei servizi webmail basati su browser (ad es. Gmail, Outlook.com, Yahoo Mail) per prevenire l'elusione dei controlli DLP basati su SMTP.

### Protezione dei canali web e cloud

I canali di uscita dei dati basati sul web DEVONO essere monitorati e controllati:

- **Caricamenti web**: Monitorare e controllare i caricamenti di file su servizi di archiviazione cloud (ad es. Dropbox, Google Drive, account OneDrive personali). L'archiviazione cloud aziendale approvata [Piattaforma di archiviazione cloud] deve essere distinta dai servizi personali o non approvati.
- **Applicazioni cloud**: Integrare [CASB] (Cloud Access Security Broker) o equivalente per il monitoraggio delle applicazioni SaaS (ad es. Microsoft 365, Google Workspace). Monitorare la condivisione dei dati, la collaborazione esterna e i trasferimenti cloud-to-cloud.
- **Moduli web**: Monitorare l'attività di incolla e compilazione di moduli su moduli web esterni laddove il rischio lo giustifichi.
- **Ispezione TLS**: Ove legalmente consentito e tecnicamente fattibile, ispezionare il traffico web crittografato al gateway internet per rilevare contenuti sensibili nei caricamenti HTTPS. L'ispezione TLS deve essere conforme ai requisiti sulla privacy e documentata nell'informativa sulla privacy dell'organizzazione.

### Protezione degli endpoint

I controlli DLP per gli endpoint DEVONO essere distribuiti su tutti i dispositivi gestiti:

- **Supporti rimovibili**: Monitorare e controllare i trasferimenti di file su unità USB, dischi rigidi esterni, schede SD e altri supporti rimovibili. Bloccare l'utilizzo non autorizzato di supporti rimovibili per dati Ristretti e Riservati. I supporti rimovibili approvati (ad es. dispositivi USB aziendali crittografati) devono essere documentati.
- **Archiviazione locale**: Monitorare le operazioni di scrittura su disco locale, condivisioni di rete e archiviazione offline per i dati sensibili.
- **Stampa**: Monitorare i lavori di stampa per i dati Ristretti. L'attività di stampa su PDF e di stampante virtuale deve essere inclusa nell'ambito del monitoraggio.
- **Screenshot e appunti** (basato sul rischio): Laddove la valutazione del rischio lo giustifichi, monitorare gli strumenti di acquisizione dello schermo e le operazioni degli appunti per i dati Ristretti. Questo controllo deve essere applicato solo a ruoli o set di dati specifici ad alto rischio, non all'intera organizzazione.
- **Applicazione offline**: Gli agenti DLP degli endpoint devono applicare le policy quando il dispositivo è disconnesso dalla rete aziendale.
- **Rilevamento Shadow IT**: Rilevare applicazioni di archiviazione cloud, messaggistica e condivisione di file non approvate installate sugli endpoint gestiti.

### Protezione della rete

I controlli DLP a livello di rete DEVONO monitorare i flussi di dati nei punti di uscita:

- Monitorare il traffico di rete ai gateway internet e ai punti di connessione cloud.
- Monitorare i protocolli di trasferimento file (FTP, SFTP, SCP, rsync) per i trasferimenti di dati sensibili.
- Rilevare l'esfiltrazione di dati tramite canali nascosti (DNS tunneling, esfiltrazione ICMP, steganografia) laddove la valutazione delle minacce identifichi questo rischio.
- Integrare gli avvisi DLP con firewall, proxy e [SIEM] per la correlazione e le indagini.

### Protezione dei dispositivi mobili

I dati aziendali sui dispositivi mobili DEVONO essere protetti:

- Integrare il DLP con [MDM] (Mobile Device Management) per applicare le policy di protezione dei dati sui dispositivi mobili aziendali.
- Separare le applicazioni e i dati aziendali sui dispositivi BYOD per prevenire la perdita di dati verso le applicazioni personali.
- Monitorare la condivisione di e-mail e documenti dai dispositivi mobili.
- Applicare policy di accesso condizionale che limitino l'accesso ai dati sensibili ai dispositivi conformi.

### Verifica della copertura

L'organizzazione DEVE verificare la copertura dei canali DLP tramite test tecnici almeno trimestralmente. Le lacune nella copertura devono essere documentate con:

- Descrizione della lacuna e sistemi o utenti interessati.
- Valutazione del rischio della lacuna.
- Approvazione del RSSI per l'accettazione del rischio (se applicabile).
- Piano di rimedio con tempistiche (se non accettato).

Eccezioni di copertura accettabili (documentate e approvate dal RSSI): reti ospiti senza accesso ai dati sensibili; connessioni B2B dedicate con controlli alternativi; reti air-gapped senza connettività internet; gruppi di utenti specifici con eccezioni documentate e approvate (ad es. consulenti legali che gestiscono comunicazioni privilegiate).

---

## Gestione dei fornitori terzi di servizi DLP

Laddove l'organizzazione utilizzi soluzioni DLP basate su cloud (CASB, gateway di sicurezza e-mail as-a-service, piattaforme DLP cloud):

### Criteri di selezione dei fornitori

I fornitori di servizi DLP DEVONO essere valutati rispetto a:

| Criterio | Requisito | Metodo di convalida |
|----------|-----------|---------------------|
| **Certificazioni di sicurezza** | SOC 2 Tipo II (corrente, entro 12 mesi); ISO 27001 | Richiedere e rivedere i rapporti annualmente |
| **Residenza dei dati** | Dati trattati e memorizzati in Svizzera o nell'UE/SEE (o giurisdizione adeguata per nLPD) | Confermare nel contratto; verificare nel rapporto SOC 2 |
| **Conformità alla protezione dei dati** | Accordo sul trattamento dei dati conforme al GDPR; impegno di conformità alla nLPD | Revisione legale del DPA |
| **Precisione di rilevamento** | <10% di falsi positivi durante il periodo di prova; >95% di tasso di rilevamento per set di dati di test noti | Proof-of-concept di 30 giorni con campione di traffico di produzione |
| **Prestazioni** | <500ms di latenza e-mail; <100ms di latenza proxy web (modalità inline) | Test di carico durante il periodo di prova |
| **Capacità di integrazione** | Integrazione API con [SIEM], [ITSM], provider di identità | Convalida tecnica durante il POC |
| **Risposta agli incidenti** | Il fornitore fornisce supporto 24x7; risposta <1 ora per avvisi critici | Termini SLA; referenze |

### Requisiti dell'accordo sul trattamento dei dati

I contratti con i fornitori DLP cloud DEVONO includere:

- **Obblighi del responsabile del trattamento** (nLPD Art. 9; GDPR Art. 28 ove applicabile)
- **Divulgazione e approvazione dei sub-responsabili** (elenco dei sub-responsabili; notifica delle modifiche)
- **Conservazione ed eliminazione dei dati** (eliminazione automatica dopo il periodo di conservazione; conferma dell'eliminazione su richiesta)
- **Notifica degli incidenti di sicurezza** (il fornitore notifica all'organizzazione entro 24 ore da qualsiasi violazione che interessi i dati del cliente)
- **Diritti di audit** (l'organizzazione o l'auditor può verificare i controlli del fornitore; il rapporto SOC 2 è accettabile se corrente)
- **Portabilità dei dati** (esportazione di log DLP e policy in formato standard alla cessazione)
- **Giurisdizione e legge applicabile** (preferibilmente legge svizzera; legge UE accettabile; controversie in Svizzera)

### Monitoraggio continuo delle prestazioni del fornitore

| Metrica | Obiettivo | Frequenza di revisione | Responsabile |
|---------|-----------|------------------------|--------------|
| **Disponibilità del servizio** | Per SLA del fornitore (tipicamente 99,5-99,9%) | Mensile | IT Operations |
| **Tasso di falsi positivi** | <10% | Mensile | Team di sicurezza |
| **Precisione di rilevamento** | >95% per scenari di test | Trimestrale | Team di sicurezza |
| **Prestazioni (latenza)** | Per gli obiettivi sopra indicati | Settimanale | IT Operations |
| **Reattività del supporto** | Per SLA (critico: <1h; alto: <4h; medio: <24h) | Per ticket | Responsabile del Team di sicurezza |
| **Incidenti di sicurezza del fornitore** | 0 che interessano i dati dei clienti | Per occorrenza | RSSI |

### Revisione annuale del fornitore

I fornitori DLP cloud DEVONO ricevere una revisione annuale che comprende:

- **Revisione del rapporto SOC 2 Tipo II**: Confronto del rapporto corrente con il precedente; identificazione di eventuali nuove eccezioni o qualifiche; verifica che l'ambiente di controllo rimanga accettabile.
- **Prestazioni rispetto agli SLA**: Disponibilità, latenza, tempi di risposta del supporto.
- **Tendenze dei falsi positivi**: In miglioramento, stabili o in peggioramento?
- **Incidenti di sicurezza**: Violazioni o quasi-incidenti lato fornitore negli ultimi 12 mesi?
- **Allineamento alla roadmap**: La direzione tecnologica del fornitore è allineata alle esigenze dell'organizzazione?
- **Costi-benefici**: Valore fornito rispetto al costo dell'abbonamento; confronto con alternative.
- **Raccomandazione**: Rinnovo, rinegoziazione o sostituzione.

**Documentazione della revisione**: Conservata 3 anni; decisioni di rinnovo documentate con motivazione.

### Escalation degli incidenti del fornitore

Se un fornitore DLP cloud subisce un incidente di sicurezza che interessa l'organizzazione:

1. **Notifica immediata**: Il fornitore DEVE notificare all'organizzazione entro 24 ore (come da contratto).
2. **Valutazione dell'impatto**: Il Team di sicurezza valuta l'impatto sull'organizzazione e sui clienti.
3. **Notifica al cliente**: Se i dati dei clienti sono interessati, notificare i clienti secondo gli impegni di servizio.
4. **Notifica normativa**: Se i dati personali sono interessati e soddisfano i criteri di violazione (nLPD Art. 24), notificare l'IFPDT.
5. **Revisione delle azioni correttive del fornitore**: Il fornitore fornisce un'analisi delle cause profonde e un piano di rimedio entro 10 giorni lavorativi.
6. **Revisione del contratto**: Valutare se l'incidente costituisce una violazione materiale; considerare la sostituzione del fornitore.

**Documentazione degli incidenti del fornitore**: Conservata almeno 5 anni; inclusa nella revisione annuale del fornitore.

---

## Monitoraggio e rilevamento

L'organizzazione DEVE implementare un monitoraggio continuo per rilevare i tentativi di perdita di dati e le violazioni delle policy.

**Modalità di rilevamento**:

| Modalità | Descrizione | Caso d'uso |
|----------|-------------|------------|
| **Solo monitoraggio** | Registrazione e avviso senza blocco | Fase di distribuzione iniziale, canali a basso rischio, periodo di ottimizzazione |
| **Richiesta all'utente** | Richiesta di giustificazione all'utente prima di consentire il trasferimento | Trasferimenti di dati Riservati verso destinatari esterni |
| **Blocco** | Impedire il trasferimento dei dati e avvisare il Team di sicurezza | Dati Ristretti verso destinazioni non attendibili, fuga di credenziali |
| **Quarantena** | Sospendere il trasferimento per la revisione del Team di sicurezza | Esfiltrazione sospetta dolosa, casi ambigui |

**Priorità degli avvisi e tempi di risposta**:

| Priorità | Esempi di attivazione | Tempo di risposta |
|----------|-----------------------|-------------------|
| **Critica** | Dati Ristretti esfiltrati esternamente; fuga di credenziali; trasferimento in blocco di grande volume | Immediata (< 15 minuti) |
| **Alta** | Dati Riservati verso un dominio non attendibile; violazione della policy da parte di un utente privilegiato; violazioni ripetute | < 1 ora |
| **Media** | Dati Riservati verso una parte esterna approvata; trasferimento di file in blocco nel normale contesto aziendale | < 4 ore |
| **Bassa** | Dati Interni verso l'esterno; avvisi informativi; candidati a falso positivo | < 24 ore |

**Registrazione degli eventi DLP**:

Tutti gli eventi DLP DEVONO essere registrati con le seguenti informazioni:

- Timestamp (UTC, formato ISO 8601).
- Identità dell'utente (nome utente, ID dipendente).
- Sistema di origine (nome host, indirizzo IP, identificatore del dispositivo).
- Destinazione (e-mail del destinatario, URL, servizio esterno, identificatore del supporto rimovibile).
- Classificazione dei dati attivata (Ristretto, Riservato, Interno).
- Metodo di rilevamento (ispezione del contenuto, etichettatura, analisi contestuale).
- Azione intrapresa (bloccato, consentito, messo in quarantena, giustificato dall'utente).
- Campione di dati (primi 100 caratteri o estratto anonimizzato — limitato al minimo necessario per le indagini, in conformità con i requisiti sulla privacy).

**Conservazione dei log**:

- Eventi di sicurezza DLP (trasferimenti bloccati, violazioni delle policy, avvisi critici): minimo 12 mesi.
- Log operativi DLP (trasferimenti consentiti, eventi informativi): minimo 90 giorni.
- Conservazione estesa laddove i requisiti normativi impongano periodi più lunghi.
- Log protetti con controlli di integrità e riservatezza conformemente ad A.8.15.

**Analisi comportamentale** (raccomandato): Laddove l'organizzazione disponga di sistemi UEBA (User and Entity Behaviour Analytics), i dati DLP devono essere correlati con l'attività baseline degli utenti per rilevare pattern di trasferimento anomali (ad es. volume insolito, destinazione insolita, orario insolito). L'analisi comportamentale DEVE essere conforme ai requisiti legali di monitoraggio dei dipendenti definiti in questa politica.

**Integrazione dell'intelligence sulle minacce** (raccomandato): I sistemi DLP dovrebbero integrarsi con i feed di intelligence sulle minacce per identificare indicatori di esfiltrazione noti (domini di command-and-control, firme malware, tecniche APT documentate in MITRE ATT&CK).

---

## Risposta agli incidenti DLP

Gli incidenti di sicurezza DLP DEVONO seguire il processo di gestione degli incidenti dell'organizzazione (A.5.24-28) con i seguenti requisiti specifici DLP.

**Classificazione degli incidenti DLP**:

| Gravità | Indicatori | Azioni iniziali |
|---------|-----------|-----------------|
| **Critica** | Dati Ristretti confermati come esfiltrati; credenziali fugate esternamente; indicatori di minaccia interna; pattern di esfiltrazione APT | Bloccare l'utente; isolare l'endpoint; notificare RSSI e DPD; avviare la risposta all'incidente |
| **Alta** | Dati Riservati verso un destinatario non attendibile; trasferimento in blocco di dati sensibili; violazioni ripetute delle policy da parte dello stesso utente | Bloccare il trasferimento; esaminare l'attività dell'utente; escalare al responsabile del Team di sicurezza |
| **Media** | Dati Riservati verso una parte esterna approvata tramite un canale non approvato; errore dell'utente con esposizione limitata | Contenere il trasferimento; intervistare l'utente; valutare l'ambito; rimediare |
| **Bassa** | Falso positivo; ottimizzazione delle regole DLP necessaria; chiarimento richiesto all'utente | Registrare; ottimizzare la regola DLP; comunicare con l'utente se necessario |

**Flusso di lavoro di risposta**:

1. **Rilevamento**: Il sistema DLP genera un avviso in base alla violazione della policy.
2. **Triage**: Il Team di sicurezza classifica la gravità dell'incidente, determina l'ambito e avvia il contenimento.
3. **Contenimento**: Bloccare l'account utente, isolare l'endpoint, revocare le credenziali o mettere in quarantena il trasferimento come appropriato.
4. **Indagine**: Analisi delle cause profonde (dolosa vs. accidentale), determinazione dell'ambito (volume dei dati, sensibilità, destinatari, durata dell'esposizione), raccolta di prove forensi.
5. **Eradicazione**: Rotazione delle credenziali (in caso di fuga di credenziali), bonifica dal malware (in caso di esfiltrazione tramite malware), revoca degli accessi.
6. **Ripristino**: Ripristino delle normali operazioni, adeguamento della policy DLP, riabilitazione dell'utente con i controlli appropriati.
7. **Revisione post-incidente**: Lessons learned (entro 30 giorni), ottimizzazione della policy DLP, raccomandazioni per il miglioramento dei controlli.

**Notifica normativa delle violazioni dei dati**:

Laddove gli incidenti DLP costituiscano violazioni di dati personali, l'organizzazione DEVE seguire i requisiti di notifica:

| Normativa | Requisito | Tempistica |
|-----------|-----------|------------|
| **nLPD svizzera** | Art. 24 — Notificare all'IFPDT se la violazione comporta un rischio elevato per le persone interessate | Senza ritardo ingiustificato |
| **GDPR UE** (se applicabile) | Art. 33 — Notificare all'autorità di controllo | 72 ore |
| **Interessati GDPR** | Art. 34 — Notificare alle persone fisiche se ad alto rischio | Senza ritardo ingiustificato |

Il Responsabile della protezione dei dati (DPD) o il referente per la privacy designato DEVE essere consultato per tutti gli incidenti DLP che coinvolgono dati personali per determinare gli obblighi di notifica delle violazioni.

**Integrazione DLP-gestione degli incidenti**: Gli eventi DLP di gravità Critica e Alta DEVONO creare automaticamente ticket di incidente in [Piattaforma ITSM] (ad es. ServiceNow, Jira Service Management o equivalente). I ticket non riconosciuti entro l'SLA di risposta devono essere sottoposti ad escalation automatica secondo le procedure di gestione degli incidenti.

---

## Requisiti legali per il monitoraggio dei dipendenti

Il monitoraggio DLP costituisce una forma di monitoraggio dei dipendenti ai sensi del diritto svizzero. L'organizzazione DEVE conformarsi ai seguenti requisiti legali prima di distribuire e operare i controlli DLP.

### Quadro giuridico svizzero

**Art. 26 OLL3 (Ordinanza 3 alla Legge sul Lavoro)**: I sistemi di monitoraggio e sorveglianza non devono essere utilizzati se il loro unico scopo o scopo principale è monitorare il comportamento dei dipendenti. I sistemi DLP sono ammissibili perché il loro scopo principale è proteggere i dati organizzativi dalla divulgazione non autorizzata, non monitorare la condotta individuale dei dipendenti. Tuttavia, l'implementazione del DLP deve dimostrabilmente servire un obiettivo di protezione dei dati, e qualsiasi monitoraggio incidentale del comportamento dei dipendenti deve essere proporzionato.

**Art. 328b CO svizzero (Codice delle obbligazioni svizzero)**: Il datore di lavoro può trattare dati relativi ai dipendenti solo nella misura in cui riguardino l'idoneità del dipendente al rapporto di lavoro o siano necessari per l'esecuzione del contratto di lavoro. I dati di monitoraggio DLP devono essere trattati esclusivamente per scopi di sicurezza delle informazioni. I dati DLP non devono essere utilizzati per:

- Valutazione o classificazione delle prestazioni dei dipendenti.
- Monitoraggio dei tempi e delle presenze.
- Sorveglianza della navigazione o delle comunicazioni personali.
- Qualsiasi scopo non correlato alla sicurezza dei dati e alla prevenzione della perdita di dati.

**Principi della nLPD svizzera**:

- **Liceità**: Il monitoraggio DLP deve avere una base legittima (la protezione dei dati organizzativi è un interesse legittimo).
- **Proporzionalità**: L'ambito del monitoraggio deve essere limitato a quanto necessario per la protezione dei dati. L'organizzazione non deve monitorare più ampiamente del necessario.
- **Limitazione delle finalità**: I dati raccolti tramite DLP devono essere utilizzati solo per scopi di sicurezza, non riutilizzati per altri obiettivi.
- **Trasparenza**: I dipendenti DEVONO essere informati del monitoraggio DLP prima della sua attivazione.

### Requisiti del GDPR UE (se applicabile)

Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE:

- **Art. 6(1)(f) Interesse legittimo**: Il monitoraggio DLP si basa sull'interesse legittimo di proteggere i dati organizzativi, bilanciato con i diritti alla privacy dei dipendenti.
- **Art. 32 Sicurezza del trattamento**: Il DLP è una misura tecnica appropriata per la protezione dei dati personali.
- **Art. 88 Trattamento nel contesto lavorativo**: Il monitoraggio DLP deve essere conforme al diritto del lavoro nazionale in ciascuna giurisdizione UE in cui opera l'organizzazione.

### Valutazione della proporzionalità

L'organizzazione DEVE condurre una valutazione della proporzionalità prima di distribuire i controlli DLP. La valutazione DEVE verificare che:

**Proporzionato (ammissibile)**:
- Monitoraggio dei canali di uscita per pattern di dati sensibili (allegati e-mail, caricamenti web, trasferimenti USB).
- Registrazione degli avvisi DLP con conservazione limitata (90 giorni routine, 12 mesi eventi di sicurezza).
- Limitazione dell'accesso ai log DLP al Team di sicurezza, RSSI e DPD secondo il principio del need-to-know.
- Distribuzione iniziale in modalità solo monitoraggio prima di abilitare il blocco.
- Limitazione dei campioni di dati nei log al minimo necessario per le indagini.

**Sproporzionato (non ammissibile)**:
- Registrazione di tutti i contenuti e-mail a tempo indeterminato indipendentemente dalla sensibilità.
- Monitoraggio di tutta l'attività di navigazione web senza limitazione dell'ambito basata sul rischio.
- Keylogging o registrazione continua dello schermo senza specifica giustificazione documentata.
- Consentire a HR o ai responsabili diretti di consultare gli avvisi DLP per la gestione delle prestazioni.
- Monitoraggio dei dispositivi personali per attività non lavorative.
- Utilizzo dei dati DLP per valutazioni dei dipendenti o azioni disciplinari non correlate alla sicurezza dei dati.

### Requisiti di trasparenza

L'organizzazione DEVE informare tutti i dipendenti del monitoraggio DLP attraverso:

1. **Contratti di lavoro o addendum**: Dichiarazione chiara che il monitoraggio DLP è in atto, il suo ambito, scopo e periodi di conservazione dei dati.
2. **Informativa sulla privacy / manuale del dipendente**: Spiegazione dettagliata di ciò che viene monitorato, di ciò che non viene monitorato, di come vengono utilizzati i dati e di chi vi ha accesso.
3. **Politica di uso accettabile**: Esplicito divieto di esfiltrazione dei dati, esempi di attività vietate, conseguenze delle violazioni e processo di eccezione.
4. **Formazione sulla consapevolezza della sicurezza**: Modulo di formazione annuale che copre lo scopo del DLP, le responsabilità degli utenti, le richieste di eccezione e le segnalazioni.
5. **Consultazione della commissione del personale** (ove applicabile): Nelle giurisdizioni che richiedono la co-determinazione, la commissione del personale DEVE essere consultata prima di distribuire il monitoraggio DLP.

**Critico**: La mancata trasparenza può rendere illecito il monitoraggio DLP. Il monitoraggio DLP NON DEVE essere attivato fino al completamento e alla documentazione della notifica ai dipendenti. L'organizzazione DEVE conservare le prove della notifica ai dipendenti (riconoscimenti firmati, registrazioni del completamento della formazione, registrazioni della distribuzione dell'informativa sulla privacy).

### Rischio di non conformità

La non conformità ai requisiti di monitoraggio dei dipendenti espone l'organizzazione a:

- **nLPD svizzera**: Sanzioni fino a CHF 250.000 per violazioni individuali; azioni esecutive dell'IFPDT.
- **GDPR UE**: Sanzioni fino a EUR 20.000.000 o al 4% del fatturato globale annuo.
- **Diritto del lavoro**: Il monitoraggio illecito può essere motivo di rivendicazioni dei dipendenti ai sensi dei diritti della personalità (CC svizzero Art. 28); le prove DLP ottenute illecitamente possono essere inammissibili nei procedimenti disciplinari.

---

## Consapevolezza degli utenti e uso accettabile

Tutto il personale DEVE essere informato dei controlli DLP e delle proprie responsabilità.

**Responsabilità degli utenti**:

- Gestire i dati sensibili secondo la loro classificazione e la politica di uso accettabile.
- Utilizzare canali approvati per i trasferimenti di dati (e-mail aziendale, archiviazione cloud approvata, strumenti di trasferimento crittografati).
- Richiedere eccezioni tramite il processo formale di eccezione per esigenze aziendali legittime che richiedono la deviazione dalla policy DLP.
- Segnalare falsi positivi e problemi di usabilità al Team di sicurezza o all'Help Desk.
- Completare la formazione annuale sulla consapevolezza DLP.

**Attività vietate**:

- Tentare di eludere i controlli DLP tramite proxy, crittografia dei dati per evitare l'ispezione, utilizzo di servizi cloud non approvati o qualsiasi altro metodo di aggiramento.
- Trasferire dati Ristretti o Riservati ad account e-mail personali, archiviazione cloud personale o servizi esterni non approvati.
- Disabilitare o manomettere gli agenti DLP degli endpoint.
- Condividere credenziali di eccezione DLP o metodi di trasferimento approvati con persone non autorizzate.

Le violazioni della policy DLP sono soggette ad azioni disciplinari conformemente alla politica HR. I tentativi deliberati o ripetuti di aggirare i controlli DLP possono comportare il licenziamento.

**Se il DLP blocca un trasferimento**:

1. Verificare la classificazione dei dati: si tratta effettivamente di dati sensibili?
2. Utilizzare un metodo di trasferimento approvato (e-mail aziendale con crittografia, condivisione cloud approvata, trasferimento file sicuro).
3. Se il trasferimento è un'esigenza aziendale legittima, inviare una richiesta di eccezione al Team di sicurezza.
4. Contattare l'Help Desk per assistenza urgente o per segnalare un falso positivo.

---

## Prestazioni e ottimizzazione DLP

L'organizzazione DEVE monitorare l'efficacia DLP attraverso indicatori chiave di prestazione e ottimizzare continuamente le regole DLP per ridurre i falsi positivi mantenendo la copertura del rilevamento.

**Metriche di prestazione**:

| Metrica | Obiettivo | Intervallo accettabile | Frequenza di revisione |
|---------|-----------|------------------------|------------------------|
| Tasso di falsi positivi | < 5% del totale degli avvisi | < 10% massimo | Mensile |
| Conformità agli SLA di risposta agli avvisi | > 95% nei tempi previsti | > 90% minimo | Settimanale |
| Copertura dei canali (percorsi di uscita critici) | 100% | > 95% minimo | Trimestrale |
| Tasso di rilevamento degli incidenti (dati Ristretti) | 100% dei tentativi di esfiltrazione | > 98% minimo | Per revisione degli incidenti |
| Efficacia dell'ottimizzazione delle policy | > 20% di riduzione dei FP per ciclo di ottimizzazione | Tendenza positiva richiesta | Trimestrale |
| Problemi segnalati dagli utenti | < 10 al mese | < 20 massimo | Mensile |

**Processo di ottimizzazione**:

- **Mensile**: Il Team di sicurezza esamina le tendenze dei falsi positivi e adegua le regole di rilevamento.
- **Trimestrale**: Revisione completa dell'efficacia delle regole DLP, delle lacune nella copertura e dei tipi di dati emergenti.
- **Per incidente**: La revisione post-incidente identifica miglioramenti alle regole di rilevamento e miglioramenti della copertura.
- **Annuale**: Revisione completa del programma DLP nell'ambito della revisione della direzione (ISO 27001 Clausola 9.3), inclusa la valutazione della tecnologia e la valutazione del fornitore.

**Risposta ai valori sotto gli obiettivi**: Se le metriche scendono al di sotto dell'intervallo accettabile per due periodi di misurazione consecutivi, il RSSI DEVE condurre un'analisi delle cause profonde entro 30 giorni, implementare un piano di azione correttiva e riportare lo stato del rimedio alla Direzione generale.

---

## Disponibilità del sistema DLP e impatto sulle prestazioni

I sistemi DLP che introducono latenza, bloccano le normali operazioni aziendali o si guastano in modo da interrompere i servizi possono influire negativamente sugli impegni di disponibilità dell'organizzazione.

### Requisiti di disponibilità del sistema DLP

| Componente | Obiettivo di disponibilità | Impatto del guasto | Failover/Ridondanza |
|------------|---------------------------|-------------------|---------------------|
| **Gateway DLP per e-mail** | 99,5% | Ritardi o errori nella consegna delle e-mail | Coppia ad alta disponibilità; opzione fail-open per classificazioni non critiche |
| **Proxy DLP web** | 99,5% | Degrado o blocco dell'accesso web | Proxy ridondanti; fail-open con registrazione per dati non Ristretti |
| **Agenti DLP endpoint** | 99% (per endpoint) | Solo applicazione offline; nessuna sincronizzazione di rete | Gli agenti continuano l'applicazione offline; avviso in caso di disconnessione prolungata (>72h) |
| **Sensori DLP di rete** | 99% | Perdita di visibilità; nessuna capacità di blocco a livello di rete | Monitoraggio passivo; non interrompe la connettività |
| **DLP cloud (CASB)** | 99,5% (SLA del fornitore) | L'accesso ai servizi cloud potrebbe degradarsi se inline; la modalità API continua | Ridondanza fornita dal fornitore; configurazione modalità inline vs. API |

### Modalità fail-safe

I sistemi DLP DEVONO essere configurati con un comportamento fail-safe esplicito per prevenire interruzioni del servizio:

| Scenario | Comportamento fail-safe | Razionale |
|----------|------------------------|-----------|
| **Guasto del gateway DLP per e-mail** | Fail-open per dati Interni e Riservati (consegna continua con registrazione); fail-closed per dati Ristretti (e-mail in coda fino al ripristino del sistema) | Bilanciamento disponibilità vs. sicurezza in base alla sensibilità dei dati |
| **Guasto del proxy DLP web** | Fail-open con registrazione completa; avvisi generati per tutto il traffico durante il periodo fail-open | Mantenere la continuità aziendale; esaminare l'attività durante il periodo di guasto |
| **Crash dell'agente DLP endpoint** | Continuare l'applicazione offline della policy; avvisare IT Operations per il rimedio | Mantenere la protezione di base; ripristinare il monitoraggio completo il prima possibile |
| **Guasto del database/console di gestione DLP** | Gli agenti continuano con l'ultima policy nota; nessuna nuova regola distribuita fino al ripristino | Prevenire la perdita dell'applicazione delle policy |

### Monitoraggio delle prestazioni

Le prestazioni del sistema DLP DEVONO essere monitorate per prevenire il degrado del servizio:

| Metrica | Obiettivo | Soglia di avviso | Frequenza di revisione |
|---------|-----------|------------------|------------------------|
| **Latenza di elaborazione e-mail** | <500ms per messaggio | >2 secondi sostenuti per 5 minuti | Monitoraggio in tempo reale |
| **Latenza proxy web** | <100ms di latenza aggiunta | >300ms sostenuti per 5 minuti | Monitoraggio in tempo reale |
| **Utilizzo CPU agente endpoint** | <5% medio | >15% sostenuti per 10 minuti | Monitoraggio orario |
| **Utilizzo memoria agente endpoint** | <200MB | >500MB | Monitoraggio orario |
| **Tasso di falsi positivi che impattano la produttività** | <5% degli utenti che segnalano blocchi su attività legittime | >10% di reclami utenti al mese | Analisi mensile del feedback degli utenti |
| **Uptime del sistema DLP** | Per gli obiettivi di disponibilità sopra indicati | <99% in qualsiasi mese solare | Revisione mensile degli SLA |

### Pianificazione della capacità

- I sistemi DLP DEVONO essere dimensionati per gestire il traffico di picco con un margine del 30%.
- La revisione annuale della capacità DEVE proiettare la crescita e identificare le esigenze di scalabilità.
- Volume e-mail, traffico web, numero di endpoint e volumi di trasferimento dati monitorati trimestralmente.
- Avvisi di capacità attivati al 70% di utilizzo; aggiornamento pianificato prima dell'85% di utilizzo.

### Impatto degli incidenti sui servizi

Gli incidenti DLP possono influire sulla disponibilità del servizio attraverso azioni di contenimento:

| Azione di contenimento | Impatto sul servizio | Mitigazione |
|-----------------------|---------------------|-------------|
| **Account utente disabilitato** (minaccia interna) | L'utente non può lavorare; i servizi possono continuare per altri utenti | Indagine rapida (<1 ora) per determinare se il blocco totale è giustificato o se è sufficiente una restrizione parziale |
| **Endpoint isolato** (esfiltrazione dati in corso) | L'utente non può accedere alla rete; i servizi cloud possono essere accessibili | Fornire un dispositivo sostitutivo pulito se l'indagine si estende oltre le 4 ore |
| **Credenziali dell'account di servizio revocate** (chiave API fugate) | L'applicazione o l'integrazione potrebbe non funzionare | Coordinarsi con il proprietario dell'applicazione; generare nuove credenziali; testare prima della revoca laddove fattibile |
| **Segmento di rete messo in quarantena** (esfiltrazione in blocco) | Più utenti interessati | Raro; richiede l'approvazione del RSSI; notifica ai clienti se i servizi rivolti all'esterno sono interessati |

**Notifica al cliente**: Se le azioni di contenimento DLP impattano sui servizi rivolti ai clienti, i clienti DEVONO essere notificati secondo le procedure di comunicazione degli incidenti (tipicamente entro 1 ora per gli incidenti che impattano i clienti).

### Continuità aziendale e disaster recovery

I controlli DLP DEVONO supportare gli obiettivi di continuità aziendale e disaster recovery dell'organizzazione:

#### DLP negli scenari di disaster recovery

Quando l'organizzazione attiva le procedure di disaster recovery:

| Scenario DR | Applicazione DLP | Razionale |
|-------------|-----------------|-----------|
| **Guasto del datacenter primario; failover al sito DR** | Piena applicazione DLP mantenuta (DLP del sito DR configurato identicamente al primario) | I requisiti di protezione dei dati rimangono invariati |
| **Guasto del sistema e-mail; uso di emergenza di un'e-mail alternativa** | Il DLP e-mail si applica al sistema alternativo; se non tecnicamente fattibile, monitoraggio potenziato e revisione manuale | Prevenire la perdita di dati durante le interruzioni |
| **Guasto dell'infrastruttura di rete; connettività alternativa temporanea** | Il DLP di rete può essere ridotto; il DLP endpoint diventa il controllo principale | Gli agenti endpoint continuano l'applicazione durante le interruzioni di rete |
| **Incidente ransomware; segmenti di rete isolati** | Il DLP può essere temporaneamente aggirato per isolamento/rimedio; supervisione manuale potenziata e revisione post-incidente | La risposta alla sicurezza ha la precedenza; i controlli manuali si sostituiscono temporaneamente |

#### Priorità di recovery del sistema DLP

I sistemi DLP DEVONO essere inclusi nella pianificazione del disaster recovery con priorità di recovery definite:

| Componente DLP | Recovery Time Objective (RTO) | Recovery Point Objective (RPO) | Livello di priorità |
|----------------|------------------------------|-------------------------------|---------------------|
| **DLP e-mail** | 4 ore (critico per le operazioni aziendali) | 1 ora (modifiche di policy/regole) | Livello 1 |
| **Agenti DLP endpoint** | N/A (operano in modo indipendente) | 24 ore (sincronizzazione policy) | Livello 2 (push policy) |
| **DLP di rete** | 8 ore (monitoraggio; non blocco) | 24 ore (log) | Livello 2 |
| **Console di gestione DLP** | 24 ore (per le modifiche alle policy) | 4 ore (configurazione) | Livello 2 |
| **CASB / DLP cloud** | Gestito dal fornitore (per SLA del fornitore) | Gestito dal fornitore | Livello 1 (responsabilità del fornitore) |

#### Rilassamento temporaneo della policy DLP

In circostanze eccezionali (incidente grave, disaster recovery, operazioni di emergenza), il rilassamento temporaneo delle policy DLP può essere autorizzato:

- **Approvazione richiesta**: RSSI + CIO (o AD se entrambi non disponibili).
- **Documentazione**: Eccezione documentata con giustificazione, controlli compensativi, durata.
- **Controlli compensativi**: Revisione manuale potenziata, limitata a utenti/tipi di dati specifici, a tempo determinato.
- **Durata massima**: 72 ore; richiede ri-approvazione per l'estensione.
- **Audit trail**: Tutta l'attività durante il periodo di rilassamento registrata e revisionata post-incidente.

**Scenario di esempio**: Durante il recovery da ransomware, il team IT deve trasferire grandi volumi di dati verso un servizio di backup cloud normalmente non approvato. Il DLP consente temporaneamente questo specifico trasferimento con registrazione potenziata e supervisione del Team di sicurezza.

#### Test DR annuale

I sistemi DLP DEVONO essere inclusi nei test annuali di disaster recovery:
- Verificare che l'applicazione DLP continui durante il failover al sito DR.
- Testare il recovery del sistema DLP entro l'RTO.
- Convalidare la sincronizzazione delle policy dopo il recovery.
- Documentare i risultati dei test e le lacune per il rimedio.

---

## Test dell'efficacia DLP

L'organizzazione DEVE condurre test strutturati per convalidare che i controlli DLP rilevino e prevengano la divulgazione non autorizzata dei dati come progettato.

### Programma di test

| Tipo di test | Frequenza | Metodo | Criteri di successo | Responsabile |
|--------------|-----------|--------|---------------------|--------------|
| **Test di rilevamento positivo** (il DLP dovrebbe bloccare) | Trimestrale | Inviare e-mail/file di test contenenti dati sensibili simulati (numeri di carta di credito di test, dati personali di test, credenziali di test) a indirizzi esterni; tentare caricamenti web; trasferimenti USB | 100% di rilevamento e blocco per i dati Ristretti; >95% per i dati Riservati | Team di sicurezza |
| **Test negativo** (il DLP dovrebbe consentire) | Trimestrale | Inviare comunicazioni aziendali legittime che storicamente hanno generato falsi positivi; verificare l'efficacia dell'ottimizzazione | <5% di tasso di falsi positivi | Team di sicurezza |
| **Verifica della copertura dei canali** | Trimestrale | Testare ogni canale monitorato (e-mail, webmail, caricamento cloud, USB, stampa, mobile) con dati di test | Tutti i canali nell'ambito rilevano i dati di test | Team di sicurezza |
| **Test di tentativo di aggiramento** | Semestrale | Tentare di aggirare il DLP utilizzando tecniche comuni (crittografia, offuscamento, canali alternativi, protocol tunneling) | Tentativi di aggiramento rilevati o prevenuti | Team di sicurezza + Red Team (se disponibile) |
| **Test dell'impatto sulle prestazioni** | Annuale | Misurare la latenza e-mail, la latenza proxy web, l'utilizzo di CPU/memoria degli endpoint durante il carico di picco | Prestazioni entro gli obiettivi (vedere la sezione disponibilità) | IT Operations + Team di sicurezza |
| **Instradamento degli avvisi ed escalation** | Trimestrale | Generare un avviso critico di test; verificare la creazione del ticket di incidente, l'avvenuta escalation, il tempo di risposta entro gli SLA | Il 100% degli avvisi di test elaborati correttamente | Team di sicurezza |

### Gestione dei dati di test

- **Set di dati di test**: Mantenere una libreria di file di test contenenti dati sensibili simulati:
  - Numeri di carta di credito di test (con risultati dell'algoritmo di Luhn non validi)
  - Numeri di previdenza sociale svizzeri di test (AVS) con cifre di controllo non valide note
  - Dati personali di test (nomi, indirizzi, e-mail di persone fittizie)
  - Credenziali di test (password false, chiavi API, certificati)
- **Account e-mail di test**: Mantenere indirizzi e-mail esterni di test per l'invio/ricezione di messaggi di test.
- **Documentazione dei test**: Ogni test documentato con data, scenario di test, risultato atteso, risultato effettivo, esito (passato/non passato), azioni di follow-up.

### Test Red Team / Purple Team

Ove le risorse lo consentano, includere il DLP negli esercizi annuali di test della sicurezza:

- **Red Team**: Tenta l'esfiltrazione dei dati utilizzando tecniche avversariali realistiche (simulazione di minaccia interna, simulazione di account compromesso, pattern di esfiltrazione APT).
- **Blue Team** (SOC/Team di sicurezza): Rileva e risponde utilizzando gli avvisi DLP e altri strumenti di monitoraggio.
- **Debriefing**: Identifica le lacune nel rilevamento DLP, i miglioramenti alle regole, i miglioramenti della copertura.
- **Monitoraggio dei miglioramenti**: Le azioni degli esercizi tracciate nel registro delle azioni correttive.

**Per le organizzazioni senza capacità di red team**: Gli esercizi tabletop che simulano scenari di esfiltrazione dei dati costituiscono un'alternativa accettabile. Gli scenari dovrebbero coprire:
- Minaccia interna (dipendente scontento che esfiltran i dati dei clienti)
- Account compromesso (attaccante che utilizza credenziali rubate per esfiltrare dati)
- Divulgazione accidentale (utente che invia dati sensibili al destinatario sbagliato)
- Attacco alla supply chain (sistema di terze parti utilizzato per esfiltrare dati)

### Documentazione dei test

Tutte le attività di test documentate con:
- Data del test, tester, ambito del test.
- Scenari di test e risultati attesi.
- Risultati effettivi (passato/non passato, tassi di rilevamento, falsi positivi).
- Lacune identificate e valutazione della gravità.
- Azioni correttive assegnate con scadenze e responsabili.
- Convalida di follow-up delle azioni correttive.

**I registri dei test vengono conservati 3 anni; i fallimenti dei test vengono escalati al RSSI; le lacune critiche vengono remediate entro 30 giorni.**

---

## Reporting alla direzione e supervisione

L'efficacia e la conformità del programma DLP DEVONO essere riportate alla direzione generale per dimostrare governance e supervisione.

### Dashboard esecutivo trimestrale

Il RSSI DEVE fornire un riepilogo trimestrale del programma DLP alla direzione generale che comprende:

| Sezione | Metriche incluse | Scopo |
|---------|------------------|-------|
| **Stato del programma** | Percentuale di copertura dei canali; eccezioni attive; tendenza del tasso di falsi positivi | Salute complessiva del programma |
| **Rilevamento delle minacce** | Incidenti Critici/Alti rilevati; tentativi di esfiltrazione bloccati; indicatori di minaccia interna | Dimostrare il valore fornito |
| **Stato di conformità** | Completamento della notifica ai dipendenti; valutazione della proporzionalità corrente; requisiti normativi soddisfatti | Garanzia legale/normativa |
| **Prestazioni** | Percentuale di disponibilità; tendenza dei falsi positivi; reclami degli utenti | Efficacia operativa |
| **Miglioramento continuo** | Azioni di ottimizzazione delle policy intraprese; lacune nella copertura remediate; risultati dei test | Maturità del programma |

### Revisione annuale della direzione

Nell'ambito della revisione della direzione ISO 27001 (Clausola 9.3), il RSSI DEVE presentare una revisione annuale del programma DLP che comprende:

- **Efficacia del programma**: Il DLP ha prevenuto le violazioni dei dati? Incidenti rilevati vs. mancati.
- **Conformità**: Conformità al diritto del lavoro svizzero; conformità alla legge sulla protezione dei dati; risultati degli audit.
- **Valutazione della tecnologia**: La tecnologia DLP attuale è adeguata? Prestazioni del fornitore? Lacune che richiedono investimenti?
- **Cambiamenti nel panorama dei rischi**: Nuove minacce di esfiltrazione; nuovi tipi di dati che richiedono protezione; nuovi canali di uscita.
- **Budget e risorse**: Il personale attuale è adeguato? Esigenze di aggiornamento tecnologico? Requisiti di formazione?
- **Raccomandazioni strategiche**: Miglioramenti del programma; modifiche alle policy; priorità di investimento.

**Documentazione della revisione**: Conservata 3 anni; decisioni della direzione e azioni tracciate.

### Reporting al Consiglio di amministrazione (se applicabile)

Per le organizzazioni con comitati di audit o supervisione del rischio a livello di Consiglio, viene fornito un riepilogo annuale del DLP che comprende:

- Efficacia del programma di alto livello (incidenti critici, stato di conformità normativa).
- Incidenti DLP significativi e lessons learned.
- Rischi normativi e postura di conformità (diritto del lavoro, legge sulla protezione dei dati).
- Investimenti strategici e progressione della maturità del programma.
- Benchmarking rispetto ai peer di settore (se disponibile).

**Il reporting al Consiglio viene conservato almeno 7 anni (documentazione di governance aziendale).**

---

## Gestione delle eccezioni

Le eccezioni ai requisiti della policy DLP DEVONO essere richieste per iscritto e DEVONO includere:

- Requisito/i specifico/i che richiedono l'eccezione.
- Giustificazione aziendale e descrizione del caso d'uso.
- Valutazione del rischio (probabilità di perdita di dati, impatto in caso di fuga).
- Controlli compensativi (crittografia, monitoraggio potenziato, ambito limitato, accesso a tempo determinato).
- Durata richiesta dell'eccezione (massimo 12 mesi; i trasferimenti una-tantum possono essere approvati senza un'eccezione continuativa).

**Autorità di approvazione**:

| Tipo di eccezione | Approvazione richiesta |
|-------------------|------------------------|
| Singolo trasferimento una-tantum | Responsabile del Team di sicurezza |
| Eccezione per singolo utente | Responsabile del Team di sicurezza + Responsabile diretto |
| Eccezione per reparto o gruppo | RSSI + Responsabile del reparto |
| Eccezione per canale (disabilitare il monitoraggio per un canale) | RSSI + CIO |
| Eccezione per classificazione dei dati (ridurre la protezione per una categoria di dati) | RSSI + Direzione generale |

**Restrizioni**: Le seguenti eccezioni non sono consentite in nessuna circostanza:

- Disabilitare la protezione DLP per i dati Ristretti senza controlli compensativi.
- Aggirare il DLP per i trasferimenti di credenziali (password, chiavi API, certificati).
- Eccezioni permanenti senza controlli compensativi documentati e revisione trimestrale.

Tutte le eccezioni attive DEVONO essere registrate nel Registro delle eccezioni DLP (formato: DLP-EC-AAAA-NNN), revisionate almeno trimestralmente e revocate quando la giustificazione aziendale non si applica più o il profilo di rischio cambia.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **CASB** | Cloud Access Security Broker — un punto di applicazione della policy di sicurezza tra i consumatori di servizi cloud e i fornitori di servizi cloud |
| **Ispezione del contenuto** | Analisi del contenuto dei dati per rilevare informazioni sensibili mediante corrispondenza di pattern, rilevamento di parole chiave ed espressioni regolari |
| **Analisi contestuale** | Valutazione del contesto di trasferimento dei dati (origine, destinazione, ruolo dell'utente, volume, tempistica) per valutare il rischio |
| **Perdita di dati** | Divulgazione involontaria o non autorizzata di informazioni sensibili a parti esterne o interne non autorizzate |
| **Prevenzione della perdita di dati (DLP)** | Tecnologie, processi e policy progettati per rilevare, prevenire e rispondere alla divulgazione non autorizzata dei dati |
| **Modalità di rilevamento** | Modalità operativa che determina la risposta DLP: solo monitoraggio, richiesta all'utente, blocco o quarantena |
| **Canale di uscita** | Qualsiasi percorso di comunicazione attraverso il quale i dati possono uscire dal controllo dell'organizzazione (e-mail, web, endpoint, rete, cloud, mobile, API) |
| **Esfiltrazione** | Trasferimento non autorizzato di dati dai sistemi organizzativi verso posizioni o attori esterni |
| **Falso negativo** | Perdita di dati che si verifica nonostante i controlli DLP (aggirata o non rilevata) |
| **Falso positivo** | Attività aziendale legittima erroneamente identificata come violazione della policy DLP |
| **Fingerprinting** | Tracciamento di documenti basato su hash che consente al DLP di identificare documenti specifici indipendentemente dal nome del file o dalle modifiche del formato |
| **Minaccia interna** | Rischio di sicurezza posto da individui con accesso autorizzato che causano intenzionalmente o non intenzionalmente la divulgazione dei dati |
| **MDM** | Mobile Device Management — tecnologia per la gestione e la protezione dei dispositivi mobili che accedono ai dati aziendali |
| **Proporzionalità** | Requisito legale che il monitoraggio della sicurezza deve essere proporzionato all'obiettivo legittimo di sicurezza e non invadere eccessivamente la privacy dei dipendenti |
| **Quarantena** | Sospensione temporanea dei trasferimenti di dati in attesa di revisione del Team di sicurezza prima del rilascio o del blocco definitivo |
| **SIEM** | Security Information and Event Management — piattaforma per la raccolta centralizzata dei log, la correlazione e gli avvisi di sicurezza |
| **Ispezione TLS** | Decrittografia e ri-crittografia del traffico crittografato TLS a un gateway di rete per l'analisi del contenuto DLP |
| **Trasparenza** | Obbligo legale di informare i dipendenti sulle attività di monitoraggio prima dell'attivazione |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della policy; supervisione del programma DLP; approvazione delle eccezioni ad alto rischio e delle eccezioni per canale; escalation degli incidenti DLP critici alla Direzione generale; revisione annuale della policy; proprietà del budget per la tecnologia DLP |
| **Responsabile della sicurezza delle informazioni** | Manutenzione quotidiana della policy; revisione delle eccezioni; monitoraggio della sicurezza e indagine sugli incidenti; coordinamento degli audit; reporting trimestrale della conformità al RSSI |
| **Responsabile della protezione dei dati (DPD)** | Revisione del monitoraggio DLP per la conformità alla proporzionalità e alla trasparenza; consulenza sugli obblighi di notifica delle violazioni (nLPD Art. 24, GDPR Art. 33/34); approvazione della distribuzione DLP dalla prospettiva della privacy; conduzione o revisione delle valutazioni degli interessi legittimi |
| **Team di sicurezza** | Distribuire e mantenere le soluzioni DLP su tutti i canali; configurare le regole e le policy di rilevamento; monitorare gli avvisi e rispondere agli incidenti; elaborare le richieste di eccezione; ottimizzare le policy per ridurre i falsi positivi; condurre le valutazioni della copertura |
| **IT Operations / Team di rete** | Distribuire e mantenere l'infrastruttura DLP; garantire che la topologia di rete supporti la copertura DLP (instradamento del traffico, punti di ispezione TLS); mantenere la disponibilità e le prestazioni del sistema DLP; coordinarsi con il Team di sicurezza per le modifiche alla rete |
| **Proprietari dei dati / Proprietari dei sistemi** | Classificare i dati nel proprio dominio; definire i requisiti di protezione; esaminare gli incidenti DLP che coinvolgono i propri dati; approvare le eccezioni per trasferimenti giustificati aziendalmente |
| **HR** | Garantire che i contratti di lavoro includano la presa di conoscenza del monitoraggio DLP; coordinarsi sulle azioni disciplinari per le violazioni delle policy; supportare i requisiti di trasparenza (aggiornamenti delle informative sulla privacy, aggiornamenti del manuale del dipendente) |
| **Legale / Conformità** | Esaminare le policy DLP per la conformità legale (diritto del lavoro, legge sulla protezione dei dati); fornire consulenza sull'interpretazione normativa; supportare le indagini sugli incidenti che richiedono competenze legali |
| **Tutto il personale** | Conformarsi alle policy DLP e ai requisiti di uso accettabile; segnalare falsi positivi e problemi di usabilità; utilizzare il processo di eccezione per esigenze aziendali legittime; completare la formazione annuale sulla consapevolezza DLP; non tentare di aggirare i controlli DLP |

---

## Prove

Le seguenti prove dimostrano la conformità a questa policy. **Per gli audit SOC 2 Tipo II**, gli auditor testeranno l'efficacia operativa nel corso del periodo di audit (tipicamente 12 mesi).

| N. | Prova | Responsabile | Frequenza | Conservazione |
|----|-------|--------------|-----------|---------------|
| 1 | **Inventario delle soluzioni DLP** con ambito di distribuzione, copertura dei canali e informazioni sulla versione | Team di sicurezza | Mantenuto continuamente; revisionato trimestralmente | Durata della distribuzione + 3 anni |
| 2 | **Inventario della classificazione dei dati** con categorie di dati sensibili, regole di rilevamento e mapping delle regole DLP | Team di sicurezza / Proprietari dei dati | Mantenuto continuamente; riconciliato trimestralmente con l'inventario degli asset | 3 anni |
| 3 | **Valutazione della copertura dei canali** con risultati dei test per canale (e-mail, web, endpoint, rete, cloud, mobile) | Team di sicurezza | Trimestrale | 3 anni |
| 4 | **Log degli avvisi e degli incidenti DLP** (trasferimenti bloccati, violazioni delle policy, avvisi critici, rapporti di incidente) | Team di sicurezza | Continuo | Eventi di sicurezza: 12 mesi; log operativi: 90 giorni |
| 5 | **Metriche di prestazione DLP** (tasso di falsi positivi, conformità agli SLA, copertura, tasso di rilevamento, efficacia dell'ottimizzazione) | Team di sicurezza / RSSI | Metriche mensili; revisione trimestrale | 3 anni |
| 6 | **Registro delle eccezioni DLP** (richieste, approvazioni, controlli compensativi, date di scadenza, registrazioni delle revisioni) | Responsabile del Team di sicurezza | Mantenuto continuamente; revisionato trimestralmente | Durata dell'eccezione + 3 anni |
| 7 | **Valutazione della proporzionalità** che documenta che il monitoraggio DLP è proporzionato all'obiettivo di sicurezza | DPD / RSSI | Prima della distribuzione; revisionata annualmente | Durata della distribuzione + 3 anni |
| 8 | **Registrazioni della notifica ai dipendenti** (contratti/addendum firmati, distribuzione dell'informativa sulla privacy, prese di conoscenza dell'uso accettabile) | HR / Legale | Per onboarding; annualmente per la formazione sulla consapevolezza | Durata dell'impiego + 3 anni |
| 9 | **Registrazioni del completamento della formazione sulla consapevolezza DLP** | RSSI / HR | Annualmente | Durata dell'impiego + 3 anni |
| 10 | **Registrazioni della risposta agli incidenti DLP** (timeline, contenimento, indagine, rimedio, lessons learned) | Team di sicurezza | Per incidente | 3 anni |
| 11 | **Registrazioni della notifica delle violazioni** (notifiche normative presentate, notifiche agli interessati inviate) | DPD / Legale | Per incidente | 7 anni |
| 12 | **Log di ottimizzazione delle regole DLP** (regole modificate, riduzione dei falsi positivi, giustificazione, approvazione) | Team di sicurezza | Per modifica | 3 anni |
| 13 | **Registrazioni della consultazione della commissione del personale** (ove applicabile) | HR | Prima della distribuzione; per ogni modifica dell'ambito | Durata della distribuzione + 3 anni |
| 14 | **Registrazioni del controllo degli accessi ai log DLP** (chi ha accesso, giustificazione, registrazioni delle revisioni) | IT Operations / Team di sicurezza | Mantenuto continuamente; revisionato trimestralmente | 3 anni |
| 15 | **Mapping della protezione dei dati dei clienti** (contratti con i clienti con classificazione dei dati e regole DLP) | Team di sicurezza + Legale | Per cliente; revisionato trimestralmente | 3 anni |
| 16 | **Registrazioni della notifica ai clienti** (incidenti DLP che coinvolgono dati dei clienti) | Team di sicurezza + Customer Success | Per incidente | 7 anni |
| 17 | **Rapporti sulla disponibilità del sistema DLP** (metriche di uptime, prestazioni e capacità) | IT Operations | Mensile | 3 anni |
| 18 | **Risultati dei test dell'efficacia DLP** (test trimestrali positivi/negativi/di aggiramento) | Team di sicurezza | Trimestrale | 3 anni |
| 19 | **Rapporti SOC 2 del fornitore** (per fornitori DLP cloud, CASB) | IT Operations / Team di sicurezza | Annuale (ricezione del rapporto del fornitore) | 3 anni |
| 20 | **Revisioni delle prestazioni del fornitore** (per fornitori DLP cloud) | Responsabile del Team di sicurezza | Annualmente per fornitore | 3 anni |
| 21 | **Risultati dei test di disaster recovery** (test di recovery DLP) | Responsabile IT Operations | Annuale (per test DR) | 3 anni |
| 22 | **Dashboard esecutivi trimestrali** (stato del programma DLP) | RSSI | Trimestrale | 3 anni |
| 23 | **Presentazione della revisione annuale della direzione** (revisione del programma DLP) | RSSI | Annuale | 3 anni |

### Aspettative di campionamento degli audit SOC 2 Tipo II

Gli auditor campionano tipicamente:
- **25 avvisi DLP** tra i livelli di gravità (verificare la risposta entro gli SLA, documentazione completa).
- **Tutti gli incidenti Critici/Alti** (verificare contenimento, indagine, notifica al cliente se applicabile).
- **Tutte le eccezioni attive** (verificare l'approvazione, il rispetto del calendario di revisione, i controlli compensativi documentati).
- **Tutti i cicli di test trimestrali** (verificare l'esecuzione dei test, la documentazione dei risultati, la remediation delle lacune).
- **Tutte le revisioni dei fornitori** (verificare il completamento, l'ottenimento dei rapporti SOC 2 correnti).
- **Prove di notifica ai dipendenti** per **25 dipendenti** (verificare il completamento della formazione, la presa di conoscenza documentata).
- **Valutazione della proporzionalità** (verificare la corrente, approvata da DPD/RSSI).

**La completezza è fondamentale**: Le prove mancanti per qualsiasi elemento campionato costituiscono un rilievo di audit. Garantire la documentazione continua per tutto il periodo di audit.

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, rapporti del sistema DLP, valutazioni della copertura dei canali, registrazioni della risposta agli incidenti, revisioni del registro delle eccezioni, audit della notifica ai dipendenti, audit interni ed esterni e feedback al proprietario della politica.

**Metriche di conformità**:

| Metrica | Obiettivo | Frequenza di misurazione |
|---------|-----------|--------------------------|
| Copertura dei canali DLP (percorsi di uscita critici) | >= 95% | Trimestrale |
| Risposta agli avvisi DLP entro gli SLA | >= 95% | Settimanale |
| Tasso di falsi positivi | < 10% | Mensile |
| Eccezioni attive revisionate nei tempi previsti | 100% | Trimestrale |
| Completamento della formazione sulla consapevolezza DLP | >= 95% | Annualmente |
| Documentazione sulla trasparenza del monitoraggio dei dipendenti completa | 100% | Annualmente |
| Valutazione della proporzionalità corrente e approvata | 100% | Annualmente |

**Punteggio di conformità**:

| Componente | Peso | Calcolo |
|------------|------|---------|
| Copertura dei canali | 30% | (Canali con copertura DLP verificata) / (Totale canali di uscita critici) x 100 |
| Efficacia della risposta agli incidenti | 25% | (Incidenti con risposta entro gli SLA) / (Totale incidenti) x 100 |
| Ottimizzazione delle policy e gestione dei falsi positivi | 20% | Inverso del tasso di falsi positivi + tendenza di miglioramento dell'ottimizzazione |
| Conformità legale (trasparenza, proporzionalità) | 15% | (Requisiti legali completati) / (Totale requisiti legali) x 100 |
| Gestione delle eccezioni | 10% | (Eccezioni revisionate nei tempi previsti) / (Totale eccezioni attive) x 100 |

**Gestione della non conformità**: Al di sotto del 70% è richiesta l'escalation immediata al RSSI e un piano di rimedio entro 30 giorni. Tra il 70-89% è richiesta la supervisione del Responsabile della sicurezza delle informazioni con revisioni mensili. Il 90% e oltre segue il monitoraggio trimestrale standard.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita (massimo 12 mesi). Le eccezioni devono essere riportate al team di revisione della direzione. Le eccezioni permanenti non sono consentite senza controlli compensativi documentati e revisione trimestrale.

## Non conformità

Un dipendente che risulti aver violato questa politica può essere soggetto ad azioni disciplinari, fino al licenziamento. I tentativi deliberati di aggirare i controlli DLP devono essere trattati come grave inadempimento. Le violazioni della politica devono essere documentate, investigate dal Responsabile della sicurezza delle informazioni e segnalate al RSSI. Laddove le violazioni comportino violazioni di dati personali, il DPD deve essere consultato.

## Miglioramento continuo

Questa politica viene rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti nelle capacità tecnologiche DLP, le tecniche di esfiltrazione dei dati in evoluzione (minacce interne, minacce persistenti avanzate, attacchi alla supply chain), i cambiamenti normativi che interessano il monitoraggio dei dipendenti o i requisiti di protezione dei dati, i risultati degli audit, le metriche e le tendenze delle prestazioni DLP, il feedback degli utenti sui falsi positivi e le lessons learned dagli incidenti DLP.

---

# Aree dello standard ISO 27001 trattate

Politica di prevenzione della perdita di dati — Mapping dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.10 Uso accettabile delle informazioni e di altri asset correlati |
| Clausola 6.1 Azioni per affrontare rischi e opportunità | 5.12 Classificazione delle informazioni |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.13 Etichettatura delle informazioni |
| Clausola 7.3 Consapevolezza | 5.14 Trasferimento di informazioni |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | **8.12 Prevenzione della perdita di dati** |
| Clausola 9.3 Revisione della direzione | 8.15 Registrazione degli eventi |
| Clausola 10.1 Miglioramento continuo | 8.16 Attività di monitoraggio |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|-----------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la protezione dei dati; DLP come misura tecnica. Art. 6 — Principi di proporzionalità, limitazione delle finalità e trasparenza |
| CO svizzero Art. 328b | Il trattamento dei dati dei dipendenti è limitato all'idoneità al lavoro e all'esecuzione del contratto; il monitoraggio DLP deve essere conforme |
| OLL3 Art. 26 | Divieto dei sistemi di sorveglianza comportamentale; il DLP è ammissibile laddove lo scopo principale sia la protezione dei dati |
| OPDo svizzero | Art. 1-3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (se applicabile) | Art. 5 (Principi di trattamento), Art. 6 (Base giuridica), Art. 32 (Misure di sicurezza), Art. 33/34 (Notifica delle violazioni), Art. 88 (Trattamento nel contesto lavorativo) |
| ISO/IEC 27001:2022 | Annex A Controllo 8.12 — Prevenzione della perdita di dati |
| ISO/IEC 27002:2022 | Sezione 8.12 — Indicazioni di implementazione per le misure di prevenzione della perdita di dati |
| NIST SP 800-53 Rev 5 | AC-4 (Information Flow Enforcement), SC-7 (Boundary Protection), SI-4 (System Monitoring) |
| CIS Controls v8 | 3.1-3.14 (Data Protection), 3.13 (Deploy a Data Loss Prevention Solution) |

---

<!-- QA_VERIFIED: 2026-04-03 -->

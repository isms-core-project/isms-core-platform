<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.10-IT:operational:OP-POL:a.7.10 -->
**ISMS-OP-POL-A.7.10 — Supporti di memorizzazione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Supporti di memorizzazione |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.7.10 |
| **Creatore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione esecutiva |
| **Data di creazione** | [Data] |
| **Versione** | 0.1 |
| **Data di versione** | [Data] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 0.1 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.7.10 — Supporti di memorizzazione
- ISO/IEC 27002:2022 Sezione 7.10 — Guida all'implementazione
- NIST SP 800-88 Rev. 2 — Linee guida per la sanificazione dei supporti (settembre 2025)
- IEEE 2883:2022 — Standard per la sanificazione dello storage
- DIN 66399 — Distruzione dei supporti di dati (livelli di sicurezza e categorie di supporti)
- nLPD svizzera (revDSG) — Legge federale sulla protezione dei dati
- OPDo svizzera (Ordinanza sulla protezione dei dati) — Art. 1–3 (requisiti minimi di sicurezza dei dati)

**Controlli Allegato A correlati**:

| Controllo | Relazione con i supporti di memorizzazione |
|-----------|---------------------------------------------|
| A.5.9 Inventario delle informazioni e delle altre risorse associate | Registro delle risorse che include l'inventario dei supporti di memorizzazione |
| A.5.10–11 Uso accettabile e restituzione delle risorse | Regole d'uso accettabile e restituzione dei supporti all'uscita dal rapporto di lavoro |
| A.5.12–13 Classificazione e etichettatura delle informazioni | Il livello di classificazione determina i requisiti di gestione, conservazione e smaltimento dei supporti |
| A.7.6–7–14 Aree sicure, scrivania libera, smaltimento sicuro | Sicurezza fisica delle aree di conservazione; metodi di smaltimento delle attrezzature contenenti supporti |
| A.8.10 Cancellazione delle informazioni | Requisiti di cancellazione logica che integrano la sanificazione fisica dei supporti |
| A.8.24 Uso della crittografia | Standard di crittografia per la protezione dei supporti a riposo e in transito |

**Politiche interne correlate**:

- Politica di classificazione e gestione delle informazioni
- Politica di aree sicure e gestione dei supporti
- Politica di gestione delle risorse
- Politica di sicurezza degli endpoint
- Politica sull'uso della crittografia

---

# Politica sui supporti di memorizzazione

## Scopo

Lo scopo della presente politica è garantire che tutti i supporti di memorizzazione siano gestiti in modo sicuro lungo l'intero ciclo di vita — dall'acquisizione e registrazione, attraverso l'uso e il trasporto, fino allo smaltimento o al riutilizzo — in conformità con lo schema di classificazione delle informazioni dell'organizzazione e con i requisiti normativi applicabili.

La presente politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative proporzionate al rischio per proteggere i dati personali (compresi i dati personali degni di particolare protezione) memorizzati su supporti fisici e digitali. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR. Entrambi i quadri normativi richiedono che i dati personali sui supporti di memorizzazione vengano resi irrecuperabili prima dello smaltimento o del riutilizzo.

Il Controllo A.7.10 riguarda un singolo controllo dell'Allegato A, ma il suo ambito si estende all'intero ciclo di vita dei supporti: acquisizione, registrazione, uso, trasferimento dati, trasporto, conservazione sicura, riutilizzo e smaltimento. La presente politica combina i requisiti normativi con una guida operativa sufficiente a consentire a una PMI di implementare e dimostrare la conformità.

## Ambito di applicazione

Tutti i dipendenti, i collaboratori e gli utenti di terze parti che gestiscono, accedono o sono responsabili di supporti di memorizzazione contenenti informazioni dell'organizzazione.

**Tipi di supporti in ambito**:

- Supporti rimovibili digitali: chiavette USB, dischi rigidi esterni, schede SD/microSD, supporti ottici (CD, DVD, Blu-ray)
- Storage fisso: dischi rigidi interni (HDD), unità a stato solido (SSD), unità NVMe
- Supporti di backup e archiviazione: nastri LTO, cartucce DAT/DLT, cartucce RDX
- Storage di dispositivi mobili: smartphone, tablet e dispositivi con storage integrato
- Storage cloud e virtuale: backup cloud, file storage cloud, immagini disco di macchine virtuali
- Supporti cartacei e analogici: documenti stampati, microfilm, microschede, supporti fotografici

**Fasi del ciclo di vita coperte**: Acquisizione, registrazione, uso, trasferimento dati, trasporto, conservazione, riutilizzo e smaltimento.

**Fuori ambito**:

- Definizioni dello schema di classificazione delle informazioni (vedi Politica di classificazione e gestione delle informazioni, A.5.12–13)
- Contratti con fornitori di servizi cloud e gestione dei fornitori terzi (vedi Politica servizi cloud, A.5.19–23)
- Selezione degli algoritmi crittografici e dettagli sulla gestione delle chiavi (vedi Politica sull'uso della crittografia, A.8.24)

## Principio

ISO/IEC 27001:2022 Allegato A.7.10 stabilisce:

> *I supporti di memorizzazione dovrebbero essere gestiti lungo il loro ciclo di vita di acquisizione, uso, trasporto e smaltimento in conformità con lo schema di classificazione e i requisiti di gestione dell'organizzazione.*

I supporti di memorizzazione devono essere gestiti in modo proporzionato alla sensibilità delle informazioni che contengono o hanno mai contenuto. Il livello di classificazione più elevato dei dati mai memorizzati su un supporto determina i requisiti di gestione e smaltimento, indipendentemente dal fatto che tali dati siano stati successivamente cancellati.

Tutti i supporti di memorizzazione contenenti informazioni dell'organizzazione devono essere registrati, tracciati e protetti. Lo smaltimento deve rendere i dati irrecuperabili utilizzando metodi conformi agli standard NIST SP 800-88 Rev. 2 e DIN 66399, appropriati al tipo di supporto e alla classificazione delle informazioni.

I supporti rimovibili personali non devono essere utilizzati per i dati dell'organizzazione. Sono consentiti solo supporti crittografati approvati dall'organizzazione.

---

## Gestione dei supporti rimovibili

### Autorizzazione e registrazione

L'uso dei supporti di memorizzazione rimovibili deve essere autorizzato prima dell'impiego:

- I dipendenti devono ottenere l'autorizzazione dal proprio responsabile diretto prima di utilizzare qualsiasi supporto di memorizzazione rimovibile per i dati dell'organizzazione. L'autorizzazione deve specificare il caso d'uso consentito, la classificazione dei dati e la durata (predefinita 12 mesi, massimo 24 mesi).
- Tutti i supporti rimovibili devono essere registrati nel [Sistema di gestione delle risorse] con i seguenti dettagli: tipo di supporto, capacità, numero seriale o etichetta di inventario, utente assegnato, scopo, livello massimo di classificazione dei dati da memorizzare e data di scadenza dell'autorizzazione.
- Per i dati dell'organizzazione devono essere utilizzati solo supporti rimovibili emessi o approvati dall'organizzazione. Le chiavette USB personali, i dischi rigidi esterni o altri dispositivi di storage personali non devono essere utilizzati per dati RISERVATI o INTERNI in nessuna circostanza.
- I supporti rimovibili emessi dall'organizzazione devono essere acquistati tramite fornitori approvati attraverso il processo di approvvigionamento dell'organizzazione. I supporti non approvati o di origine sconosciuta non devono essere collegati ai sistemi dell'organizzazione.

**Ciclo di vita dell'autorizzazione**:
- 30 giorni prima della scadenza: Promemoria automatico via e-mail al dipendente e al responsabile diretto dal [Sistema di gestione delle risorse]
- Alla scadenza: Stato del supporto modificato in "Scaduto" nel sistema
- Se il supporto non viene rinnovato o restituito entro 15 giorni dalla scadenza: IT Operations contatta il dipendente per la restituzione o il rinnovo
- Rinnovo: Il dipendente invia una richiesta di rinnovo con giustificazione aziendale continuata; il responsabile diretto approva (massimo 24 mesi per autorizzazione; dopo 24 mesi, rivalutare la necessità da capo)
- Restituzione: Il dipendente restituisce il supporto a IT Operations; il supporto viene cancellato in modo sicuro secondo le procedure di smaltimento (anche se il supporto verrà riemesso — cancellazione tra un utente e l'altro); [Sistema di gestione delle risorse] aggiornato
- Escalation per supporti non restituiti: 15 giorni di ritardo → escalation al responsabile diretto; 30 giorni di ritardo → escalation al RSSI, supporto contrassegnato come "Mancante", avvio delle indagini sulla perdita; 60 giorni di ritardo → presumere perso/rubato, avviare la risposta agli incidenti per la procedura di supporto smarrito
- Metriche: Tasso di conformità dell'autorizzazione dei supporti (% restituiti o rinnovati nei tempi) — obiettivo >95%; supporti in ritardo (>15 giorni dalla scadenza) — obiettivo <3 elementi; riportato nella Revisione della direzione trimestrale

### Tipi di supporti approvati

L'organizzazione deve mantenere un elenco dei tipi di supporti rimovibili approvati. Come minimo:

- **Chiavette USB**: Crittografate hardware, emesse solo dall'organizzazione (es. [Modello USB crittografato]). La crittografia solo software è accettabile per i dati INTERNI laddove i dispositivi con crittografia hardware non siano disponibili, soggetta all'approvazione del RSSI e ai seguenti controlli compensativi:
  - I dati RISERVATI richiedono crittografia hardware — nessuna eccezione solo software
  - Durata massima dell'eccezione: 6 mesi (rinnovabile con approvazione del RSSI)
  - Strumenti software approvati: BitLocker To Go (Windows, AES-256), FileVault (macOS, AES-256), VeraCrypt (multipiattaforma, AES-256)
  - Passphrase forte obbligatoria: Minimo 16 caratteri, conservata nel [Gestore delle password]
  - Il supporto deve essere crittografato prima del primo uso (non crittografato dopo che i dati sono già stati scritti — rischio di dati non crittografati residui)
  - Monitoraggio potenziato: Utilizzo dei supporti con crittografia software registrato, revisione mensile dei modelli di accesso
  - Riautorizzazione trimestrale: L'utente riconferma la necessità aziendale ogni 3 mesi; se la necessità cessa, il supporto viene restituito per lo smaltimento sicuro
  - Migrazione alla crittografia hardware: Le eccezioni con crittografia software devono essere gradualmente eliminate man mano che i supporti con crittografia hardware diventano disponibili (obiettivo: tutti i dati INTERNI su crittografia hardware entro 12 mesi)
- **Dischi rigidi esterni**: Modelli con crittografia hardware AES-256 di fornitori approvati.
- **Supporti ottici (CD/DVD/Blu-ray)**: Emessi dall'organizzazione, etichettati con classificazione, riferimento di inventario, data di scrittura, descrizione del contenuto e data di scadenza della conservazione. Supporti a scrittura singola (CD-R, DVD-R, BD-R) obbligatori per: archiviazione RISERVATA (documenti legali, registrazioni di audit, documenti finanziari), conservazione delle prove (immagini forensi, prove di incidenti, blocchi legali) e conservazione a lungo termine (>5 anni). I supporti riscrivibili (CD-RW, DVD-RW, BD-RE) sono consentiti solo per il trasferimento temporaneo di dati INTERNI e dati di test/sviluppo (massimo 12 mesi, poi distrutti in modo sicuro). Conservazione: custodie jewel o slim (non buste di carta — rischio di graffi), orientamento verticale (non impilati piatti — rischio di deformazione), ambiente fresco e asciutto lontano dalla luce solare. Pianificare la migrazione a nuovi supporti a 5 anni per i dati di conservazione a lungo termine.
- **Schede SD/microSD**: Consentite solo per scopi specifici approvati (es. fotocamere, sistemi embedded). Devono essere crittografate ove il dispositivo lo supporti.

I supporti rimovibili non crittografati non devono essere utilizzati per i dati RISERVATI. Le eccezioni richiedono l'approvazione documentata del RSSI con controlli compensativi e un limite di tempo non superiore a 6 mesi.

### Manutenzione dell'elenco dei supporti approvati

L'elenco dei supporti approvati deve essere rivisto e aggiornato su base regolare:

- **Revisione annuale**: IT Operations e RSSI esaminano l'elenco dei supporti approvati nel quarto trimestre
- **Revisione attivata**: Quando è disponibile una nuova tecnologia di supporto, viene scoperta una vulnerabilità di sicurezza in un modello attualmente approvato, o l'approvvigionamento identifica un modello discontinuato

Criteri di revisione:
- Standard di crittografia aggiornato (AES-256 minimo per RISERVATI, AES-128 minimo per INTERNI)
- Crittografia hardware preferita (FIPS 140-2 Livello 2 o superiore per i supporti RISERVATI)
- Stato del supporto da parte del fornitore (supporto attivo, aggiornamenti di sicurezza disponibili)
- Rapporto costo-efficacia (prezzo per GB, disponibilità di approvvigionamento in blocco)
- Compatibilità con gli endpoint dell'organizzazione (Windows, macOS, Linux)

Processo di approvazione: IT Operations propone aggiunte o rimozioni con valutazione tecnica; il RSSI approva le modifiche; l'Approvvigionamento aggiorna l'elenco dei fornitori preferiti; l'elenco dei supporti approvati viene pubblicato sull'intranet e comunicato a tutto il personale. L'elenco deve includere la data di versione e la prossima data di revisione.

### Audit trimestrale dei supporti

Un audit basato sul rischio dei supporti rimovibili registrati deve essere condotto trimestralmente:

**Ambito dell'audit per livello di rischio**:

| Livello di rischio | Criteri | Campione trimestrale | Copertura annuale |
|--------------------|---------|---------------------|-------------------|
| **Alto rischio** | Supporti che hanno memorizzato dati RISERVATI (attuali o storici); supporti trasportati regolarmente fuori sede; supporti assegnati a dirigenti o utenti privilegiati | Verifica al 100% | 100% per trimestre |
| **Rischio medio** | Supporti con soli dati INTERNI; utilizzo solo in ufficio | Campione rotante al 50% | 100% in 2 trimestri |
| **Basso rischio** | Supporti con soli dati PUBBLICI; supporti in archiviazione sicura a lungo termine | Campione rotante al 25% | 100% annualmente |

**Procedura di audit**:
1. Generare l'elenco del campione dal [Sistema di gestione delle risorse] in base al livello di rischio
2. Verifica fisica: Confermare ubicazione, detentore, stato di crittografia, corrispondenza del numero seriale con il registro
3. Verifica a campione della crittografia: Test casuale al 10% dei supporti campionati (tentativo di accesso senza password/chiave di crittografia)
4. Documentare i risultati: Rapporto di riconciliazione con risultati, discrepanze e azioni di follow-up

**Escalation dei rilievi**:
- Supporti ad alto rischio mancanti: Escalation immediata al RSSI (in giornata); presumere perso/rubato; avviare la valutazione della violazione per la procedura di risposta agli incidenti dei supporti smarriti
- Supporti a rischio medio mancanti: Escalation entro 2 giorni lavorativi; indagine da parte di IT Operations
- Supporti a basso rischio mancanti: Documentare e seguire entro 5 giorni lavorativi

**Audit annuale completo**: Verifica al 100% di TUTTI i supporti (tutti i livelli di rischio) condotta una volta all'anno (quarto trimestre o come programmato dal RSSI).

I risultati degli audit devono essere documentati e conservati per 12 mesi.

---

## Requisiti di utilizzo dei supporti

### Trasferimento di dati su supporti rimovibili

- Il trasferimento di dati RISERVATI su supporti rimovibili richiede l'approvazione documentata della direzione prima del trasferimento. Il registro di approvazione deve indicare la giustificazione aziendale, il destinatario e la data di rientro prevista.
- Tutti i dati trasferiti su supporti rimovibili devono essere crittografati. Per i dati RISERVATI, la crittografia AES-256 (hardware o software) è obbligatoria. Per i dati INTERNI è richiesto AES-128 o superiore.
- Per i dati RISERVATI devono essere tenuti registri dei trasferimenti, con indicazione di: data, utente, identificatore del supporto, descrizione dei dati e destinatario.
- I dati devono essere rimossi dai supporti rimovibili non appena non siano più necessari per lo scopo approvato.

### Controllo degli accessi e protezione

- I supporti contenenti dati RISERVATI devono essere protetti da password o crittografati con autenticazione forte (PIN, passphrase o sblocco biometrico sul dispositivo).
- I supporti non devono essere lasciati incustoditi in nessun momento. Quando non sono in uso attivo, i supporti devono essere conservati in modo sicuro in contenitori chiusi a chiave appropriati al livello di classificazione.
- I supporti rimovibili non devono essere collegati a sistemi non attendibili o pubblici.
- Il contenuto dei supporti deve essere sottoposto a scansione antimalware da [Strumento di protezione endpoint] prima che i dati vengano aperti o trasferiti ai sistemi dell'organizzazione. La funzione di avvio automatico (auto-run e auto-play) deve essere disabilitata su tutti gli endpoint tramite il criterio di [Strumento di gestione endpoint].

### Controlli sulle porte USB e sui supporti rimovibili

- Le porte USB e l'accesso ai supporti rimovibili devono essere gestiti centralmente tramite [Strumento di gestione endpoint] (es. Criteri di gruppo, MDM o piattaforma di protezione endpoint).
- Criterio predefinito: I dispositivi di massa USB sono bloccati su tutti gli endpoint. Le eccezioni vengono concesse per numero seriale del dispositivo, solo per supporti registrati e crittografati.
- Tutti gli eventi di connessione USB devono essere registrati dalla piattaforma di protezione endpoint. I registri devono essere conservati per un minimo di 12 mesi.

**Controllo delle porte USB per tipo di workstation** — I diversi tipi di workstation hanno requisiti diversi per l'accesso USB:

| Tipo di workstation | USB di massa | Supporti approvati | Registrazione |
|---------------------|-------------|---------------------|---------------|
| **Desktop/laptop da ufficio standard** | Bloccato per impostazione predefinita | Eccezione per numero seriale (solo supporti crittografati registrati) | Tutti i tentativi di connessione registrati |
| **Workstation sviluppatore** | Consentito solo per supporti crittografati registrati | USB crittografato emesso dall'organizzazione + strumenti di sviluppo approvati (Yubikey, chiavi di sicurezza hardware) | Tutte le connessioni registrate |
| **Laptop dirigente/lavoratore mobile** | Consentito solo per supporti crittografati registrati | USB crittografato emesso dall'organizzazione | Tutte le connessioni registrate; revisione trimestrale degli accessi |
| **Sistema kiosk/pubblico** | Bloccato (nessuna eccezione) | Nessuno | Tutti i tentativi di connessione registrati e in allerta |
| **Server/infrastruttura** | Bloccato (nessuna eccezione tranne IT Operations autorizzato durante la manutenzione) | Solo supporti di salvataggio/diagnostica approvati (crittografati, di sola lettura ove possibile) | Tutte le connessioni registrate e in allerta |

Implementazione tramite [Strumento di gestione endpoint]: Criterio di controllo dispositivo con whitelist per numero seriale del dispositivo (non per tipo di dispositivo); diversi gruppi di criteri per tipo di workstation (basati su gruppo AD o tag dispositivo). Allerta in caso di: tentativi di connessione USB non autorizzati, connessioni USB fuori dall'orario lavorativo, trasferimenti di dati in blocco (>1 GB), tentativi di autenticazione multipli falliti su supporti crittografati.

**Eccezione temporanea** (visitatore/collaboratore, necessità breve <7 giorni): Approvazione di IT Operations + responsabile diretto; massimo 7 giorni; registrazione potenziata + revisione giornaliera; eccezione rimossa automaticamente dalla whitelist alla scadenza.

---

## Trasporto dei supporti di memorizzazione

### Requisiti di trasporto sicuro

Quando i supporti di memorizzazione devono essere trasportati, si applicano i seguenti requisiti:

**Spedizione tramite corriere e posta**:

- I supporti RISERVATI devono essere trasportati solo tramite servizi di corriere sicuro approvati, con tracciabilità e firma alla consegna. I servizi postali standard non devono essere utilizzati per i dati RISERVATI.
- I supporti INTERNI dovrebbero utilizzare servizi di corriere tracciati. I servizi postali standard possono essere utilizzati con consegna raccomandata/tracciata.
- Per tutti i supporti contenenti dati RISERVATI devono essere utilizzati imballaggi antimanomissione. Il destinatario deve ispezionare l'imballaggio per rilevare eventuali segni di manomissione e segnalare immediatamente qualsiasi anomalia.
- La documentazione della catena di custodia deve accompagnare tutte le spedizioni di supporti RISERVATI (vedere la sezione Catena di custodia di seguito).

**Trasporto personale (a mano)**:

- I supporti devono essere trasportati nel bagaglio a mano durante i viaggi (mai nel bagaglio da stiva).
- I supporti devono essere crittografati e non devono essere lasciati incustoditi in nessun momento durante il trasporto.
- Il trasporto attraverso aree ad alto rischio (hub di trasporto pubblico, conferenze, giurisdizioni estere senza adeguata protezione dei dati) dovrebbe essere evitato dove esistano alternative. Ove inevitabile, devono essere applicate misure di crittografia e controllo degli accessi aggiuntive.

**Alternativa al trasferimento elettronico**:

Ove fattibile, il trasferimento elettronico crittografato (es. condivisione sicura di file, SFTP, e-mail crittografata) dovrebbe essere preferito al trasporto fisico dei supporti. Il trasporto fisico dovrebbe essere utilizzato solo quando il trasferimento elettronico non è praticabile o è vietato.

**Protezione ambientale durante il trasporto**:

I supporti di memorizzazione (in particolare i nastri magnetici e gli HDD) sono sensibili a temperatura, umidità e urti fisici durante il trasporto:

- **Trasporto estivo (temperatura ambiente >30 °C)**: Utilizzare contenitori di spedizione isolati; evitare di lasciare i supporti nei veicoli; preferire la consegna in giornata o nella notte successiva per ridurre al minimo il tempo di transito
- **Trasporto invernale (temperatura ambiente <5 °C)**: Utilizzare contenitori di spedizione isolati; consentire ai supporti di acclimatarsi alla temperatura ambiente (minimo 2 ore) prima dell'uso se esposti al gelo
- **Protezione dagli urti**: Utilizzare pluriball antistatico + contenitore rigido esterno (non busta imbottita); etichettare "Fragile — Supporto elettronico" su tutti i lati; contrassegnare "Questo lato su" per le cartucce a nastro
- **Protezione dall'umidità**: Utilizzare bustine di essiccante (gel di silice) nei contenitori di spedizione per climi umidi o rapide variazioni di umidità

| Tipo di supporto | Tolleranza di temperatura (non operativo) | Sensibilità agli urti | Imballaggio raccomandato |
|------------------|-------------------------------------------|-----------------------|--------------------------|
| Nastro magnetico (LTO, DAT) | –40 a 65 °C | Alta (componenti meccanici interni) | Antistatico + custodia rigida + etichetta "Fragile" |
| HDD | –40 a 70 °C | Alta (parti mobili) | Antistatico + imbottitura in schiuma + custodia rigida |
| SSD / Flash | –40 a 85 °C | Bassa (nessuna parte mobile) | Antistatico + imballaggio standard |
| Ottico (CD/DVD) | 5 a 50 °C | Bassa | Custodia jewel + busta imbottita |

Istruzioni per il corriere per i supporti RISERVATI: Fornire istruzioni di gestione al corriere; richiedere firma alla consegna (no "lasciare alla porta"); tracciare la spedizione in tempo reale; investigare se la consegna è in ritardo di oltre 24 ore. Il destinatario deve ispezionare l'imballaggio per rilevare danni al ricevimento e segnalare immediatamente qualsiasi danno fisico.

### Catena di custodia

Tutti i trasferimenti di supporti contenenti dati RISERVATI tra individui, ubicazioni o organizzazioni devono essere documentati con:

- Data e ora della consegna
- Identità della parte cedente (nome, ruolo)
- Identità della parte ricevente (nome, ruolo, organizzazione se esterna)
- Identificatore del supporto (etichetta di inventario, numero seriale)
- Descrizione del contenuto (livello di classificazione, categoria generale dei dati — non i dati stessi)
- Conferma della ricezione (firma o conferma elettronica)
- Data di rientro prevista (ove applicabile)

I registri della catena di custodia devono essere conservati per 7 anni.

**Catena di custodia per il trasferimento logico dei dati**: Laddove i dati vengano trasferiti elettronicamente anziché tramite supporto fisico, la catena di custodia deve essere documentata anche in questo caso:
- Documentazione richiesta: Data/ora, mittente, destinatario, nomi/dimensioni dei file, classificazione, metodo di trasferimento (e-mail/SFTP/condivisione sicura di file), metodo di crittografia (es. "AES-256 tramite [Strumento]"), scadenza del link (se basato su link)
- Registrazione: Acquisizione automatica tramite log di audit di [Strumento di condivisione sicura di file] / [Gateway e-mail] ove disponibile
- Conservazione: 12 mesi (log); 7 anni (registrazioni di trasferimento RISERVATO)

*Metodo di trasferimento preferito per scenario*:

| Scenario | Metodo preferito | Motivazione |
|----------|-----------------|-------------|
| File <100 MB | E-mail crittografata o condivisione sicura di file (es. [Strumento]) | Più rapido; nessun rischio legato al supporto fisico |
| File 100 MB–10 GB | Condivisione sicura di file con link a scadenza | Evita i limiti di dimensione delle e-mail; tracciabile |
| File >10 GB | USB crittografato tramite corriere, o SFTP/sincronizzazione cloud | Il supporto fisico è pratico per i trasferimenti di grandi dimensioni |
| Archivio/backup (scala TB) | Nastro crittografato tramite corriere | Più conveniente per l'archiviazione di grandi volumi |

Per i trasferimenti logici RISERVATI: crittografia end-to-end obbligatoria (crittografato prima del caricamento/invio, il destinatario decrittografa). Condivisione tramite link: link a scadenza (massimo 7 giorni), protetti da password, notifica di download al mittente. E-mail: allegato crittografato (GPG/PGP o [Strumento di e-mail sicura]), identità del destinatario verificata prima dell'invio.

---

## Requisiti di conservazione

### Conservazione fisica per classificazione

I supporti di memorizzazione devono essere conservati in condizioni appropriate sia alla sensibilità delle informazioni che all'integrità fisica del supporto:

| Classificazione | Conservazione fisica | Crittografia | Controllo degli accessi | Requisiti ambientali |
|-----------------|---------------------|--------------|-------------------------|----------------------|
| **RISERVATO** | Cassaforte o armadio sicuro chiuso a chiave in un'area riservata | Obbligatoria — AES-256 (per la Politica sulla crittografia) | Solo individui nominati; accesso registrato | Temperatura 15–25 °C; umidità relativa 30–60%; lontano da campi magnetici e luce solare diretta |
| **INTERNO** | Armadio o cassetto chiuso a chiave | Raccomandata — AES-128 o superiore | Personale autorizzato con legittima necessità aziendale | Condizioni standard d'ufficio; lontano da rischi ambientali |
| **PUBBLICO** | Storage standard da ufficio | Opzionale | Accesso generale; sicurezza fisica mantenuta | Condizioni standard d'ufficio |

### Conservazione dei supporti di backup

- I nastri e le cartucce di backup devono essere conservati in un'ubicazione fisica separata dai sistemi di cui sono il backup (fuori sede o in una zona antincendio separata).
- I supporti di backup devono essere crittografati utilizzando la crittografia avanzata del fornitore o uno strumento di crittografia approvato dall'organizzazione.
- I supporti di backup devono essere inclusi nell'inventario dei supporti e soggetti allo stesso audit trimestrale dei supporti rimovibili.

### Conservazione e scadenza

- I supporti devono essere conservati in conformità con il calendario di conservazione dei dati dell'organizzazione. I periodi di conservazione sono definiti dal tipo di dato, dai requisiti normativi e dalle esigenze aziendali.
- Quando il periodo di conservazione dei dati su un supporto scade, il supporto deve essere sanificato o distrutto secondo la sezione Smaltimento della presente politica.
- I nastri di backup e gli snapshot cloud devono avere trigger documentati di smaltimento o cancellazione allineati al calendario di conservazione. La conservazione "a tempo indeterminato" non è consentita senza approvazione documentata del RSSI e revisione annuale.

**Quadro di conservazione dei supporti di backup** — Approccio a due livelli che separa il ripristino operativo dalla conservazione legale/di conformità:

*Conservazione operativa dei backup* (per disaster recovery e ripristino operativo):
- Backup giornalieri: 30 giorni
- Backup settimanali: 90 giorni (3 mesi)
- Backup mensili: 12 mesi
- Backup annuali: 3 anni (rete di sicurezza per il ripristino a lungo termine)

*Conservazione dei dati legali/di conformità* (per normative, blocchi legali, audit):
- Separata dai backup operativi — utilizzare storage di archiviazione strutturata, non backup completi del sistema su nastro
- Registri finanziari: 10 anni (CO svizzero Art. 958f)
- Registri HR: 10 anni
- Dati dei clienti: per contratto o normativa applicabile

*Trigger di cancellazione dei backup*:

| Tipo di backup | Trigger di cancellazione | Metodo |
|----------------|--------------------------|--------|
| Backup giornalieri >30 giorni | Cancellazione automatica da parte dello strumento di backup | Criterio di conservazione in [Strumento di backup], registrato |
| Backup settimanali >90 giorni | Cancellazione automatica da parte dello strumento di backup | Criterio di conservazione in [Strumento di backup] |
| Backup mensili >12 mesi | Revisione manuale + approvazione del responsabile IT Operations | Revisione trimestrale; cancellazione con approvazione firmata |
| Backup annuali >3 anni | Revisione manuale + approvazione del RSSI | Revisione annuale; cancellazione con approvazione firmata |
| Snapshot cloud (orfani) | Identificazione trimestrale + periodo di grazia di 90 giorni | Criterio del ciclo di vita; revisione degli snapshot orfani trimestralmente |

*Eccezione per blocco legale*: Se i dati sono soggetti a blocco legale (contenzioso, indagine, audit), la cancellazione dei backup deve essere sospesa per i dati interessati. Il blocco legale è documentato nel [Sistema di gestione delle risorse] con motivo del blocco, data di inizio e data di revisione. La ripresa della cancellazione richiede l'approvazione del Legale/Compliance.

---

## Smaltimento dei supporti di memorizzazione

### Principi di smaltimento

Lo smaltimento e la sanificazione devono garantire che le informazioni non possano essere recuperate, utilizzando metodi approvati dall'organizzazione appropriati al tipo di supporto e al livello di classificazione più elevato dei dati mai memorizzati sul supporto.

L'organizzazione adotta il quadro NIST SP 800-88 Rev. 2 per la sanificazione dei supporti, allineato con le raccomandazioni tecniche IEEE 2883:2022 per la sanificazione dei dispositivi di storage:

| Livello di sanificazione | Metodo | Descrizione | Caso d'uso |
|--------------------------|--------|-------------|------------|
| **Cancellazione (Clear)** | Sovrascrittura logica | Sovrascrive le aree di storage accessibili all'utente con dati non sensibili utilizzando comandi standard di lettura/scrittura. Protegge dalle tecniche di recupero dati semplici e non invasive. | Dati PUBBLICI; riutilizzo interno di apparecchiature a bassa sensibilità |
| **Eliminazione (Purge)** | Cancellazione crittografica, cancellazione a blocchi o comandi a livello firmware | Rende il recupero dei dati non praticabile con tecniche di laboratorio all'avanguardia. Include la cancellazione crittografica (distruzione delle chiavi di crittografia su unità auto-crittografanti) e i comandi di cancellazione sicura del produttore secondo IEEE 2883. | Dati INTERNI; riutilizzo interno; trasferimento esterno di apparecchiature precedentemente INTERNE |
| **Distruzione (Destroy)** | Distruzione fisica | Rende i supporti fisicamente inutilizzabili tramite triturazione, disintegrazione, polverizzazione o incenerimento. Il recupero dei dati è non praticabile indipendentemente dallo sforzo applicato. | Dati RISERVATI; qualsiasi smaltimento esterno di supporti che hanno memorizzato dati sensibili; fine vita per qualsiasi supporto per cui la sanificazione non può essere verificata |

### Requisiti di smaltimento per classificazione

| Classificazione | Risultato richiesto | Livello NIST minimo | Verifica |
|-----------------|--------------------|--------------------|---------|
| **RISERVATO** | Irrecuperabile con qualsiasi mezzo, incluse tecniche di laboratorio all'avanguardia | Distruzione (o solo Eliminazione per riutilizzo interno con cancellazione crittografica verificata) | Certificato di distruzione dal fornitore approvato; distruzione testimoniata per dati altamente sensibili |
| **INTERNO** | Irrecuperabile senza attrezzature o tecniche specializzate | Eliminazione | Verifica della cancellazione avvenuta con successo documentata con output del tool |
| **PUBBLICO** | Cancellazione standard con smaltimento documentato | Cancellazione | Documentazione dello smaltimento nel registro delle risorse |

### Metodi di smaltimento per tipo di supporto

| Tipo di supporto | RISERVATO | INTERNO | PUBBLICO |
|------------------|-----------|---------|---------|
| **Dischi rigidi (HDD)** | Distruzione fisica: triturazione o degaussing + triturazione | Eliminazione: cancellazione sicura del produttore (ATA Secure Erase, NVMe Sanitize) o sovrascrittura a passaggio singolo con verifica, oppure distruzione fisica | Formattazione e reinstallazione |
| **Unità a stato solido (SSD/NVMe)** | Distruzione fisica: triturazione o disintegrazione | Cancellazione crittografica o cancellazione sicura del produttore per IEEE 2883; distruzione fisica se la cancellazione crittografica non è disponibile | Comando di cancellazione sicura |
| **Chiavette USB / Schede SD** | Distruzione fisica: triturazione | Sovrascrittura sicura o distruzione fisica | Formattazione |
| **Nastri LTO / di backup** | Distruzione fisica: triturazione o incenerimento | Degaussing + sovrascrittura o distruzione fisica | Degaussing o sovrascrittura |
| **Supporti ottici (CD/DVD/Blu-ray)** | Distruzione fisica: triturazione o incenerimento | Distruzione fisica: triturazione | Distruzione fisica o deturpazione |
| **Dispositivi mobili** | Distruzione fisica dei componenti di storage | Ripristino delle impostazioni di fabbrica + verifica della cancellazione crittografica | Ripristino delle impostazioni di fabbrica |
| **Stampanti / Fotocopiatrici (HDD/SSD interno)** | Rimozione dello storage interno + distruzione | Rimozione dello storage interno + cancellazione sicura | Cancellazione della memoria / ripristino delle impostazioni di fabbrica |
| **Storage cloud / virtuale** | Cancellazione crittografica + conferma della cancellazione + affidamento alla certificazione SOC 2/ISO 27001 del fornitore | Cancellazione crittografica + conferma della cancellazione dal fornitore | Cancellazione standard tramite API/console del fornitore |

**Nota importante su SSD e supporti flash**: I tradizionali metodi di sovrascrittura non sono affidabili per SSD e storage flash a causa del livellamento dell'usura, dell'over-provisioning e dell'amplificazione della scrittura. Per i supporti SSD e flash, la cancellazione crittografica (ove supportata da unità auto-crittografanti — SED) o i comandi di cancellazione sicura del produttore per IEEE 2883:2022 sono i metodi di Eliminazione approvati. Ove nessuno dei due sia disponibile o non possa essere verificato, è richiesta la distruzione fisica.

**Sovrascrittura HDD — Guida NIST SP 800-88 Rev. 2**: NIST SP 800-88 Rev. 2 (settembre 2025) conferma che una sovrascrittura a passaggio singolo è sufficiente per gli HDD moderni (produzione post-2001). La sovrascrittura a passaggi multipli (es. i metodi legacy DoD 5220.22-M a 3 o 7 passaggi) non è più richiesta e non fornisce alcun beneficio di sicurezza aggiuntivo su unità moderne. Metodi di Eliminazione approvati per HDD: comando di cancellazione sicura del produttore (ATA Secure Erase, NVMe Sanitize), o sovrascrittura a passaggio singolo con verifica tramite tool approvato (es. DBAN, nwipe, shred o dd). La verifica deve includere il report di completamento del tool con numero seriale, timestamp e stato di superamento/fallimento.

**Requisiti di degaussing per i supporti magnetici**: L'efficacia del degaussing dipende dall'intensità del campo magnetico del degausser rispetto alla coercitività del supporto. Il degausser deve essere classificato per il tipo di supporto da sanificare:

| Tipo di supporto | Range di coercitività | Classificazione minima del degausser |
|------------------|-----------------------|--------------------------------------|
| Nastri LTO-7/8/9 | ~2.800–3.200 Oe | ≥7.000 Gauss (raccomandato NSA/CSS EPL) |
| Nastri LTO-5/6 | ~2.500–2.800 Oe | ≥5.000 Gauss |
| Cartucce DAT/DLT | ~1.500–2.000 Oe | ≥5.000 Gauss |
| HDD (legacy, pre-SSD) | ~2.000–5.000 Oe | ≥9.000 Gauss per una cancellazione affidabile |

Convalida del degausser: Le apparecchiature di degaussing devono essere testate annualmente (o secondo le raccomandazioni del produttore) per verificare che l'intensità del campo rimanga nelle specifiche. I registrazioni dei test devono essere conservati. Gli SSD e i supporti flash non possono essere sottoposti a degaussing — il degaussing non ha effetto sullo storage a stato solido.

**Smaltimento dello storage cloud e virtuale**: I principali fornitori cloud (AWS, Azure, GCP) non forniscono certificati di distruzione individuali per lo storage virtuale. Per lo smaltimento cloud, l'organizzazione deve:
- Eliminare volumi/oggetti tramite console o API cloud e cancellare le chiavi di crittografia dal KMS (cancellazione crittografica)
- Conservare le prove di conferma dell'eliminazione (screenshot o log di audit API con ID volume e timestamp di eliminazione)
- Fare affidamento sulla certificazione SOC 2 Tipo II / ISO 27001 del fornitore che attesta che lo storage eliminato viene sanificato per IEEE 2883 / NIST SP 800-88 prima del riutilizzo o dello smaltimento dell'hardware
- Documentare il ricorso alla certificazione del fornitore nel registro di smaltimento (es. "AWS SOC 2 Tipo II datato [Data]")
- Per i dati RISERVATI di massima sensibilità: Utilizzare la crittografia lato client (l'organizzazione controlla le chiavi, non il fornitore) come misura di mitigazione — anche se il fornitore non cancella, i dati rimangono crittografati
- La Direzione esecutiva deve riconoscere annualmente il ricorso ai processi di cancellazione certificati dal fornitore nella Revisione della direzione

### Riutilizzo interno

Prima che i supporti vengano riutilizzati all'interno dell'organizzazione:

- Tutti i dati devono essere cancellati in modo sicuro utilizzando un metodo appropriato alla classificazione dei dati precedenti.
- La cancellazione deve essere verificata utilizzando [Strumento di cancellazione sicura] e il log di verifica conservato.
- I supporti devono essere ispezionati per verificarne l'integrità fisica. I supporti danneggiati non devono essere riutilizzati ma distrutti.
- I registri del [Sistema di gestione delle risorse] devono essere aggiornati con la nuova assegnazione, la data e le prove di sanificazione.
- Il software concesso in licenza deve essere trasferito o rimosso conformemente ai termini di licenza.

### Smaltimento esterno

I supporti destinati allo smaltimento esterno devono:

- Avere tutti i dati cancellati in modo sicuro al livello richiesto, o essere fisicamente distrutti.
- Essere smaltiti solo tramite fornitori di distruzione approvati.
- Avere lo smaltimento documentato con certificati di distruzione conservati per 7 anni.
- Non essere mai venduti, donati o scartati con dati recuperabili.

Le apparecchiature che hanno memorizzato dati RISERVATI non devono essere riutilizzate esternamente. I supporti di memorizzazione devono essere fisicamente distrutti prima di qualsiasi trasferimento esterno.

### Certificati di distruzione

Per tutti i supporti distrutti da [Fornitore di distruzione] o fornitori specializzati:

- Deve essere ottenuto un certificato di distruzione per ogni lotto o singolo elemento distrutto.
- I certificati devono fare riferimento ai singoli numeri seriali o etichette di inventario, non solo agli identificatori di lotto.
- Il metodo di distruzione e lo standard di conformità (es. NIST SP 800-88 Distruzione, livello DIN 66399) devono essere indicati.
- I certificati devono essere confrontati con il registro di consegna per garantire che tutti gli elementi siano contabilizzati. Le discrepanze devono essere segnalate immediatamente e registrate come evento di sicurezza.
- I certificati devono essere archiviati con il registro di smaltimento e conservati per 7 anni.

---

## Documenti cartacei e supporti fisici

### Gestione dei documenti cartacei

- I documenti cartacei devono essere classificati e gestiti in conformità con la Politica di classificazione e gestione delle informazioni.
- I documenti RISERVATI devono essere conservati in armadi o casseforti chiusi a chiave quando non sono in uso attivo immediato:
  - **Archivio a cassetti chiuso a chiave**: Adatto per documenti aziendali RISERVATI standard (contratti, documenti finanziari, elenchi di clienti) fino a circa 1 cassetto (~1.000 fogli). Armadio metallico con serratura a chiave o combinazione, fissato al pavimento/muro ove fattibile.
  - **Cassaforte chiusa a chiave**: Richiesta per segreti commerciali, documenti M&A, materiali soggetti a privilegio legale e dati personali altamente sensibili (referti medici di dirigenti, risultati di verifiche dei precedenti). Cassaforte con resistenza al fuoco (minimo 1 ora), serratura a combinazione o elettronica, accesso limitato a 2–3 individui nominati.
  - **Archivio/sala sicura per documenti**: Richiesta per l'archiviazione RISERVATA di grandi volumi (>10 scatole di fascicoli). Sala dedicata chiusa a chiave con controllo degli accessi tramite card, CCTV e controlli ambientali (soppressione antincendio, umidità).
- I documenti devono essere raccolti immediatamente dalle stampanti, dalle fotocopiatrici e dai fax. Ove disponibile, dovrebbe essere implementata la stampa sicura con rilascio pull (pull printing).
- La politica della scrivania libera deve essere rispettata in ogni momento (vedi Politica di aree sicure e gestione dei supporti, A.7.6–7–14).

### Distruzione dei documenti cartacei

La distruzione della carta deve essere conforme agli standard DIN 66399. DIN 66399 definisce i livelli di sicurezza utilizzando un prefisso letterale per la categoria del supporto (P = carta) e un numero per il livello di sicurezza (1–7, più alto = particelle più piccole):

| Classificazione | Livello DIN 66399 | Dimensione particelle | Metodo |
|-----------------|-------------------|-----------------------|--------|
| **RISERVATO** | P-4 minimo (P-5 raccomandato per i dati personali sensibili) | P-4: max 160 mm², larghezza max 6 mm | Distruzione a taglio incrociato |
| **INTERNO** | P-3 minimo | P-3: max 320 mm², larghezza max 2 mm | Distruzione a taglio incrociato o a striscia |
| **PUBBLICO** | Nessun requisito minimo | N/D | Rifiuti generali / riciclaggio |

- La triturazione deve essere eseguita in loco con trituratori di proprietà dell'organizzazione ove possibile. Per la distruzione in blocco, possono essere utilizzati fornitori esterni approvati con raccolta in contenitori per rifiuti riservati chiusi a chiave e certificati di distruzione.
- I contenitori per rifiuti riservati devono essere forniti in ubicazioni accessibili in tutto l'ufficio. I contenitori devono essere chiusi a chiave e svuotati secondo un calendario programmato da personale autorizzato o dal [Fornitore di distruzione].
- Gli eventi di distruzione di massa (traslochi di ufficio, purga di archivi) devono essere testimoniati o certificati.

### Microfilm, microschede e supporti fotografici

- La distruzione deve seguire la categoria DIN 66399 F (film) ai livelli di sicurezza corrispondenti alla classificazione delle informazioni.
- RISERVATO: F-4 minimo (dimensione massima delle particelle 160 mm²). INTERNO: F-3 minimo.
- Ove la triturazione in loco dei supporti in pellicola non sia possibile, deve essere utilizzato un fornitore esterno approvato.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità per i supporti di memorizzazione |
|-------|--------------------------------------------------|
| **Direzione esecutiva** | Approvare la politica; allocare le risorse per l'infrastruttura di sicurezza dei supporti e i contratti con i fornitori |
| **RSSI** | Titolarità della politica; definire gli standard di sanificazione; supervisionare la conformità; approvare le eccezioni; esaminare i risultati degli audit trimestrali |
| **IT Operations** | Approvvigionamento e fornitura dei supporti; implementazione della crittografia; eseguire sanificazione e distruzione; mantenere i registri di smaltimento; gestire [Strumento di cancellazione sicura] e [Strumento di gestione endpoint] |
| **Responsabile della struttura** | Gestire l'infrastruttura di conservazione fisica (casseforti, armadi chiusi a chiave); coordinare la fornitura e la raccolta dei contenitori per rifiuti riservati; gestire le apparecchiature di triturazione in loco |
| **Responsabili diretti** | Autorizzare l'uso dei supporti rimovibili per i propri team; garantire la conformità del team ai requisiti di gestione e conservazione; affrontare i rilievi degli audit |
| **Approvvigionamento / Gestione fornitori** | Gestire i contratti con [Fornitore di distruzione]; verificare le certificazioni del fornitore; raccogliere e verificare i certificati di distruzione |
| **Gestione delle risorse** | Mantenere l'inventario dei supporti nel [Sistema di gestione delle risorse]; condurre audit trimestrali dei supporti; riconciliare i registri; aggiornare lo stato delle risorse al momento dello smaltimento |
| **Tutto il personale** | Gestire i supporti secondo i requisiti di classificazione; restituire i supporti all'uscita dal rapporto di lavoro; segnalare immediatamente supporti persi, rubati o danneggiati; non utilizzare supporti personali per i dati dell'organizzazione |

**Percorso di escalation**:

- Supporti persi o rubati: Dipendente → Responsabile diretto + IT Operations (immediato) → RSSI
- Domande sulla politica dei supporti: Dipendente → IT Operations → RSSI
- Certificati di distruzione mancanti: IT Operations → Approvvigionamento → RSSI
- Discrepanze nell'audit trimestrale: Gestione delle risorse → RSSI → Direzione esecutiva (se non risolto entro 5 giorni lavorativi)

### Risposta agli incidenti per supporti persi o rubati

Quando viene segnalata la perdita o il furto di un supporto, devono essere intraprese le seguenti azioni immediate:

**Entro 15 minuti dalla segnalazione:**

1. **Valutare la gravità**:
   - Classificazione dei dati sul supporto (RISERVATO = Critica, INTERNO = Alta, PUBBLICO = Bassa)
   - Stato di crittografia (crittografato = rischio inferiore, non crittografato = rischio superiore)
   - Numero di registrazioni di dati personali (>100 persone = rischio più elevato di notifica della violazione)

2. **Contenimento immediato** (se il supporto non è crittografato o contiene dati RISERVATI):
   - IT Operations: Cancellare da remoto il supporto se esiste la capacità di cancellazione remota (es. dispositivo mobile, supporto sincronizzato con il cloud)
   - IT Operations: Disabilitare le credenziali di accesso associate se il supporto conteneva credenziali (chiavi API, password)
   - IT Operations: Disattivare il numero seriale del supporto dall'elenco dei supporti approvati (prevenire la riconnessione se trovato)

**Entro 1 ora:**

3. **Classificazione dell'incidente**:
   - RISERVATO + non crittografato = Gravità critica (presumere violazione dei dati, avviare la risposta alla violazione per A.5.24–28)
   - RISERVATO + crittografato = Gravità alta (valutare la sicurezza delle chiavi, potenziale per la decrittografia)
   - INTERNO + non crittografato = Gravità alta
   - INTERNO + crittografato O PUBBLICO = Gravità media/bassa

4. **Escalation e indagine**:
   - RSSI notificato (gravità Critica/Alta)
   - DPD notificato (se sono coinvolti dati personali — valutare la notifica della violazione ai sensi della nLPD Art. 24 / GDPR Art. 33)
   - Indagine: Come è stato perso il supporto? Circostanze, cronologia, ultima ubicazione nota

**Entro 24 ore:**

5. **Valutazione della notifica della violazione**:
   - Se i criteri di violazione nLPD/GDPR sono soddisfatti: Notificare l'IFPDT/autorità di vigilanza secondo i tempi applicabili (nLPD: il prima possibile; GDPR: 72 ore)
   - Se è richiesta la notifica contrattuale (DPA del cliente): Notificare i clienti secondo i termini contrattuali
   - Documentare la decisione sulla violazione nel Log degli incidenti

6. **Rimedio**:
   - Sostituire il supporto se l'utente necessita ancora di supporti rimovibili per le attività aziendali
   - Riemettere supporti crittografati se il supporto perso non era crittografato
   - Aggiornare il [Sistema di gestione delle risorse]: Contrassegnare il supporto come "Perso" con riferimento all'incidente
   - Coaching/formazione dell'utente in caso di perdita dovuta a negligenza

**Post-incidente:**
- Analisi della causa principale: Perché è stato perso il supporto? Gap di processo? Violazione della politica?
- Azioni preventive: Se si verificano perdite ripetute (es. legate ai viaggi), implementare controlli aggiuntivi
- Riportato nella Revisione della direzione trimestrale: Statistiche sui supporti persi/rubati, trend, azioni correttive

---

## Prove a supporto della presente politica

| # | Prova | Responsabile | Frequenza | Conservazione |
|---|-------|-------------|-----------|---------------|
| 1 | Inventario dei supporti rimovibili (registro completo con stato di crittografia) | Gestione delle risorse | Continuo; audit trimestrale | Vita del registro della risorsa |
| 2 | Registrazioni di autorizzazione dei supporti (approvazioni del responsabile per l'uso dei supporti rimovibili) | Responsabili diretti | Per evento di autorizzazione | 3 anni |
| 3 | Registri di trasferimento dati RISERVATI (data, utente, ID supporto, descrizione dati, destinatario) | IT Operations | Per evento di trasferimento | 7 anni |
| 4 | Rapporti di audit trimestrale dei supporti (risultati di riconciliazione, discrepanze, risoluzioni) | Gestione delle risorse | Trimestrale | 3 anni |
| 5 | Registri di smaltimento delle apparecchiature (etichetta di inventario, classificazione, metodo, data, operatore) | IT Operations | Per evento di smaltimento | 7 anni |
| 6 | Certificati di distruzione dal [Fornitore di distruzione] | Approvvigionamento | Per evento di distruzione | 7 anni |
| 7 | Log di verifica della cancellazione sicura (output del tool per risorsa) | IT Operations | Per evento di cancellazione | 7 anni |
| 8 | Registrazioni della catena di custodia per il trasporto dei supporti | IT Operations | Per evento di trasporto | 7 anni |
| 9 | Log di connessione porte USB e supporti rimovibili (telemetria endpoint) | IT Operations | Continuo | 12 mesi |
| 10 | Registrazioni di raccolta contenitori rifiuti riservati e triturazione | Responsabile della struttura | Per evento di raccolta | 3 anni |
| 11 | Registrazioni di due diligence del fornitore per i servizi di distruzione | Approvvigionamento | Revisione annuale | Durata del contratto + 2 anni |
| 12 | Registrazioni di presa visione della politica (formazione sulla gestione dei supporti) | HR / RSSI | Annuale | Durata del rapporto di lavoro + 1 anno |
| 13 | Rapporti di incidente per supporti persi/rubati (gravità, contenimento, valutazione della violazione) | RSSI | Per incidente | 7 anni |
| 14 | Registrazioni di scadenza e rinnovo dell'autorizzazione dei supporti | IT Operations | Per evento | Durata dell'assegnazione + 1 anno |
| 15 | Cronologia delle versioni e registrazioni delle revisioni dell'elenco dei supporti approvati | IT Operations / RSSI | Annuale + attivato | 3 anni |

---

## Opzionale: Controlli sui dati delle carte di pagamento (PCI DSS)

*Applicabile solo se vengono trattati dati delle carte di pagamento e sussiste l'ambito PCI.*

Se si applica l'ambito PCI DSS, devono essere soddisfatti i seguenti requisiti aggiuntivi:

- I supporti contenenti dati dei titolari di carta devono essere fisicamente distrutti quando non sono più necessari per ragioni aziendali o legali (PCI DSS Requisito 9.4).
- Deve essere mantenuto un inventario dei supporti contenenti dati dei titolari di carta, riconciliato almeno annualmente (PCI DSS Requisito 9.4.1).
- Lo smaltimento sicuro dei supporti con dati dei titolari di carta deve essere documentato con certificati di distruzione (PCI DSS Requisito 9.4.7).
- Il trasporto interno ed esterno di supporti contenenti dati dei titolari di carta deve utilizzare corrieri sicuri ed essere registrato (PCI DSS Requisiti 9.4.3–9.4.4).

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica tramite vari metodi, inclusi tra gli altri:

- Audit trimestrali dei supporti rimovibili per metodologia di campionamento basata sul rischio (copertura annuale al 100%).
- Revisione mensile dei log di connessione USB e degli avvisi di protezione endpoint per i supporti non autorizzati.
- Revisione semestrale dei registri di smaltimento rispetto al registro delle risorse per identificare smaltimenti non contabilizzati.
- Revisione annuale dei contratti, delle certificazioni e della completezza dei certificati di distruzione del [Fornitore di distruzione].
- Verifica annuale che l'elenco dei supporti approvati, gli strumenti di sanificazione e le procedure rimangano aggiornati.
- Audit interni ed esterni e feedback al proprietario della politica.

**Metriche di governance**:

| Metrica | Obiettivo |
|---------|-----------|
| Supporti registrati con conformità crittografica | 100% |
| Perdite o furti di supporti (per trimestre) | 0 |
| Smaltimenti con certificato (RISERVATI) | 100% |
| Verifica cancellazione sicura completata (per smaltimento) | 100% |
| Tasso di completamento dell'audit trimestrale | 100% |
| Rientri di supporti in ritardo | < 3 |
| Tasso di corrispondenza del numero seriale sui certificati di distruzione | 100% |

## Eccezioni

Qualsiasi eccezione alla presente politica deve essere approvata e registrata preventivamente dal RSSI, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita non superiore a 6 mesi. Le eccezioni devono essere segnalate al Team di revisione della direzione.

Le eccezioni consentite includono:

- Supporti rimovibili non crittografati per specifici requisiti operativi in cui la crittografia è tecnicamente incompatibile, con controlli fisici potenziati e approvazione a tempo limitato.
- Conservazione oltre i periodi standard con giustificazione aziendale o legale documentata e revisione annuale.
- Metodi di trasporto alternativi con accettazione del rischio firmata dal RSSI.

Le eccezioni non devono essere concesse per:

- Dati RISERVATI su supporti rimovibili non crittografati senza controlli compensativi.
- Supporti personali per dati RISERVATI o INTERNI dell'organizzazione.
- Smaltimento di supporti RISERVATI senza verifica o certificato.
- Elusione dei requisiti di audit trimestrale dei supporti.

## Non conformità

Un dipendente che risulti aver violato la presente politica può essere soggetto a provvedimenti disciplinari, fino al licenziamento.

La gestione o lo smaltimento improprio di supporti contenenti dati personali può costituire inoltre una violazione della nLPD svizzera, con possibile avvio di un'indagine da parte dell'Incaricato federale della protezione dei dati e della trasparenza (IFPDT) e, ove applicabile, delle autorità di protezione dei dati dell'UE ai sensi del GDPR.

La perdita di supporti non crittografati contenenti dati personali deve essere segnalata come violazione dei dati e valutata nell'ambito delle procedure di gestione degli incidenti dell'organizzazione e dei requisiti applicabili di notifica delle violazioni.

## Miglioramento continuo

La presente politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono tener conto di:

- Modifiche agli standard di sanificazione (inclusi aggiornamenti NIST SP 800-88, revisioni IEEE 2883, emendamenti DIN 66399)
- Nuove tecnologie di storage (es. NVMe, memoria persistente, architetture flash emergenti)
- Modifiche alla nLPD svizzera, al GDPR o ad altre normative applicabili
- Rilievi di audit e incidenti di smaltimento
- Feedback dagli audit trimestrali dei supporti e dalle revisioni dei fornitori
- Modifiche allo schema di classificazione delle informazioni dell'organizzazione

---

# Aree della norma ISO 27001 trattate

Politica sui supporti di memorizzazione — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.1 Azioni per affrontare i rischi | 5.9 Inventario delle informazioni e delle altre risorse associate |
| Clausola 7.3 Consapevolezza | 5.10 Uso accettabile delle informazioni e delle altre risorse associate |
| Clausola 7.5 Informazioni documentate | 5.12 Classificazione delle informazioni |
| Clausola 8.1 Pianificazione e controllo operativo | 5.13 Etichettatura delle informazioni |
| Clausola 10.2 Non conformità e azioni correttive | **7.10 Supporti di memorizzazione** |
| | 7.14 Smaltimento sicuro o riutilizzo delle attrezzature |
| | 8.10 Cancellazione delle informazioni |
| | 8.24 Uso della crittografia |

# Quadro normativo

| Quadro | Rilevanza |
|--------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative; rendere i dati personali irrecuperabili prima dello smaltimento |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati, inclusa la protezione fisica dei supporti |
| GDPR UE (ove applicabile) | Art. 5(1)(f) — Integrità e riservatezza; Art. 17 — Diritto alla cancellazione; Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Allegato A Controllo 7.10 — Gestione del ciclo di vita dei supporti di memorizzazione |
| ISO/IEC 27002:2022 | Sezione 7.10 — Guida all'implementazione per i supporti di memorizzazione |
| NIST SP 800-88 Rev. 2 | Linee guida per la sanificazione dei supporti — Cancellazione, Eliminazione, Distruzione (settembre 2025; sostituisce Rev. 1) |
| IEEE 2883:2022 | Standard per la sanificazione dello storage — metodi tecnici per unità e supporti |
| DIN 66399 | Distruzione dei supporti di dati — livelli di sicurezza (categorie P/F/O/T/H/E, livelli 1–7) e classi di protezione |

---

<!-- QA_VERIFIED: 2026-04-03 -->

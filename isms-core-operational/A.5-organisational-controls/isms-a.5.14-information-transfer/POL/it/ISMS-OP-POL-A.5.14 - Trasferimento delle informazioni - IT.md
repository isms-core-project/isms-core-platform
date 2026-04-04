<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.14-IT:operational:OP-POL:a.5.14 -->
**ISMS-OP-POL-A.5.14 — Trasferimento delle informazioni**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Trasferimento delle informazioni |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.14 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Policy operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Data prossima revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- Controllo ISO/IEC 27001:2022 A.5.14 — Trasferimento delle informazioni

**Controlli Annex A correlati**:

| Controllo | Relazione con il trasferimento delle informazioni |
|-----------|---------------------------------------------------|
| A.5.10 Uso accettabile delle informazioni | Le regole di uso accettabile si applicano a tutti i trasferimenti di informazioni |
| A.5.12–13 Classificazione ed etichettatura delle informazioni | La classificazione determina il metodo di trasferimento e i requisiti di cifratura |
| A.5.19–23 Relazioni con i fornitori | Accordi di trasferimento con terzi e trasferimenti tramite servizi cloud |
| A.5.31 Requisiti legali, normativi e contrattuali | Requisiti legali per i trasferimenti transfrontalieri (nLPD Art. 16–17) |
| A.5.34 Privacy e protezione dei dati personali | Requisiti per il trasferimento dei dati personali e trigger per la DPIA |
| A.7.10 Supporti di archiviazione | Gestione dei supporti rimovibili e smaltimento sicuro |
| A.8.10 Cancellazione delle informazioni | Cancellazione sicura dei dati trasferiti dai supporti e dall'archiviazione temporanea |
| A.8.13 Backup delle informazioni | Sicurezza del trasporto dei supporti di backup e del trasferimento fuori sede |
| A.8.24 Uso della crittografia | Standard di cifratura per i dati in transito |

**Policy interne correlate**:

- Policy di classificazione e gestione delle informazioni
- Policy sull'uso della crittografia
- Policy di controllo degli accessi
- Policy sulla privacy e protezione dei dati personali
- Policy di gestione degli asset
- Policy di gestione degli incidenti

---

# Policy sul trasferimento delle informazioni

## Scopo

Lo scopo di questa policy è garantire il corretto trattamento nel trasferimento delle informazioni sia internamente che esternamente, e proteggere il trasferimento delle informazioni attraverso tutti i tipi di strumenti di comunicazione.

Questa policy supporta la nLPD svizzera (revDSG) e l'Ordinanza sulla protezione dei dati (OPDo) implementando misure tecniche e organizzative proporzionate al rischio per proteggere i dati personali (inclusi i dati personali degni di particolare protezione) durante il trasferimento. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Le informazioni che fanno parte dei sistemi e delle applicazioni inclusi nell'ambito della dichiarazione di scopo ISO 27001.

## Principi

Il trasferimento dei dati DEVE essere conforme a tutti i requisiti legali e normativi applicabili, inclusa la nLPD svizzera (revDSG) e, ove applicabile, il GDPR UE.

DEVONO essere in vigore accordi formali che includono clausole di non divulgazione e riservatezza per la condivisione dei dati con terzi, prima del trasferimento dei dati.

I dati personali NON devono essere trasferiti al di fuori della Svizzera senza una valida base giuridica ai sensi della nLPD Art. 16–17 (decisione di adeguatezza, Clausole Contrattuali Standard o eccezione applicabile). Si veda la sezione Trasferimenti transfrontalieri di seguito.

Nessuna informazione personale o riservata DEVE essere trasferita senza cifratura.

Tutti i trasferimenti DEVONO essere conformi alla Policy di classificazione e gestione delle informazioni.

---

## Controllo antivirus delle informazioni

Le informazioni oggetto di trasferimento DEVONO essere verificate per la presenza di malware prima dell'invio o prima dell'apertura alla ricezione. Ciò si applica a tutti i trasferimenti elettronici inclusi allegati email, trasferimenti di file e supporti rimovibili.

## Cifratura delle informazioni

Le informazioni personali e riservate DEVONO essere sempre cifrate prima del trasferimento, in conformità con la Policy sull'uso della crittografia.

Le credenziali di cifratura per nome utente e password, ove utilizzate, DEVONO essere condivise tramite due metodi di comunicazione separati e distinti. Il metodo preferito consiste nel condividere il link di accesso o il nome utente via email e la password o passphrase tramite una telefonata o un canale di messaggistica sicura.

## Accordi di trasferimento

DEVONO essere stipulati accordi formali di trasferimento con tutti i destinatari terzi di dati personali o riservati. Gli accordi di trasferimento DEVONO includere:

- Le parti coinvolte e i loro ruoli in materia di protezione dei dati (titolare, responsabile del trattamento).
- Categorie di interessati e dati personali da trasferire.
- Finalità e base giuridica del trasferimento.
- Misure tecniche e organizzative di sicurezza (cifratura, controlli degli accessi, logging).
- Obblighi di conservazione e cancellazione dei dati.
- Tempistiche di notifica delle violazioni.
- Diritti di audit.
- Controlli sui sub-responsabili del trattamento (ove applicabile).

Gli accordi di trasferimento DEVONO essere rivisti annualmente o in caso di modifiche sostanziali all'accordo di trasferimento.

---

## Metodi di trasferimento dei dati

### Metodo di trasferimento preferito

Il metodo di trasferimento preferito per i dati riservati e personali è una piattaforma sicura di condivisione file approvata dall'organizzazione (ad es. [servizio cloud cifrato], portale sicuro o soluzione di managed file transfer).

Tutti i metodi di trasferimento approvati dall'organizzazione DEVONO supportare:

- Cifratura in transito (TLS 1.2 minimo, TLS 1.3 preferito).
- Controlli degli accessi e autenticazione.
- Log di audit dei trasferimenti.

### Trasferimento elettronico di file

Per i trasferimenti automatizzati o in blocco di file, DEVONO essere utilizzati i seguenti protocolli:

| Protocollo | Stato |
|-----------|-------|
| SFTP (SSH File Transfer Protocol) | Approvato — preferito per i trasferimenti automatizzati |
| HTTPS | Approvato — per upload di file via web e trasferimenti API |
| FTPS (FTP su TLS) | Approvato — dove SFTP non è disponibile |
| FTP (non cifrato) | Vietato |
| SCP | Accettabile — ma SFTP è preferito |

### Trasferimento dati tramite email

L'email non è il metodo preferito per il trasferimento di informazioni personali o riservate, in quanto non è intrinsecamente sicura e non garantisce la consegna.

Laddove possibile e praticabile, DEVE essere preso in considerazione un metodo sicuro alternativo per il trasferimento di dati sensibili.

I sistemi email NON devono essere utilizzati per trasferire informazioni personali o riservate non cifrate.

Laddove i dati riservati debbano essere inviati via email:

- DEVE essere utilizzato un allegato cifrato con una lunghezza di chiave conforme ai requisiti della Policy sull'uso della crittografia (AES-256 minimo).
- La password o la chiave di decifratura DEVE essere condivisa tramite un canale di comunicazione separato (telefonata, messaggistica sicura).
- Il nome del file o l'oggetto NON devono rivelare il contenuto completo degli allegati o divulgare dati personali sensibili.

I messaggi email contenenti trasferimenti sensibili DEVONO includere istruzioni chiare sulle responsabilità del destinatario e sulle azioni da intraprendere se non si è il destinatario corretto.

L'utilizzo di account email personali per il trasferimento di dati dell'organizzazione è vietato. Ove tecnicamente fattibile, l'organizzazione DEVE implementare controlli per impedire l'inoltro di email aziendali verso account personali esterni (ad es. regole di flusso della posta, policy DLP, accesso condizionale).

L'organizzazione DEVE implementare l'autenticazione del dominio email (SPF, DKIM, DMARC) per proteggersi dallo spoofing e dall'intercettazione delle email. La policy DMARC DEVE essere impostata su **quarantine** o **reject** (non **none**) per i domini di produzione.

### Trasferimento dati tramite posta o corriere

I trasferimenti di dati che avvengono tramite supporti fisici quali documenti cartacei, schede di memoria o hard disk esterni DEVONO essere inviati esclusivamente tramite un corriere sicuro approvato dall'organizzazione (un servizio di corriere che fornisce consegna tracciata con firma, imballaggio antimanomissione e documentazione della catena di custodia, ad es. Posta Svizzera raccomandata, DHL Express con firma o equivalente). I servizi postali standard NON devono essere utilizzati per dati riservati o personali.

Il destinatario DEVE essere chiaramente indicato sul pacco e il supporto fisico DEVE essere imballato in modo sicuro per evitare danni o manomissioni. Per il materiale riservato DEVE essere utilizzato un imballaggio antimanomissione.

Il destinatario DEVE essere informato in anticipo che le informazioni sono in arrivo, in modo che sia consapevole di quando aspettarsi il materiale. Il destinatario DEVE confermare la ricezione sicura non appena le informazioni arrivano. Il mittente è responsabile della conferma che i dati siano arrivati in modo sicuro.

### Trasferimento dati su supporti rimovibili

Per il trasferimento di informazioni DEVONO essere utilizzati esclusivamente supporti rimovibili di proprietà dell'organizzazione, in conformità con la Policy di gestione degli asset. Il dispositivo DEVE essere approvato, registrato nell'inventario degli asset, assegnato a un utente e cifrato (cifratura completa del disco o a livello di file AES-256). La cifratura DEVE essere verificata dall'IT prima che il dispositivo sia approvato per i trasferimenti di dati riservati.

Le chiavette USB non cifrate, i dispositivi di archiviazione personali e i servizi cloud non approvati NON devono essere utilizzati per i trasferimenti di dati dell'organizzazione.

Il supporto rimovibile DEVE essere restituito al proprietario al completamento del trasferimento e i dati trasferiti DEVONO essere cancellati in modo sicuro dal dispositivo di archiviazione dopo l'uso. L'inventario degli asset DEVE essere aggiornato.

DEVONO essere fornite istruzioni chiare sulle responsabilità del destinatario e sulle azioni da intraprendere se non si è il destinatario previsto.

Eventuali messaggi di accompagnamento o nomi di file NON devono rivelare il contenuto del supporto.

Per la spedizione fisica dei supporti rimovibili DEVE essere seguita la procedura descritta per i trasferimenti di dati tramite posta o corriere.

### Telefoni, cellulari e conversazioni generali

Poiché le telefonate possono essere monitorate, intercettate o origliute (deliberatamente o accidentalmente), si DEVE prestare attenzione come segue:

- Essere consapevoli del proprio ambiente, specialmente sui mezzi di trasporto pubblici e in luoghi pubblici, quando si discutono informazioni personali, riservate o altrimenti sensibili.
- I dati personali NON devono essere trasferiti o discussi telefonicamente senza aver prima confermato l'identità e l'autorizzazione del destinatario.
- Quando si utilizza la segreteria telefonica, non lasciare messaggi sensibili o riservati né includere dati personali. Fornire solo un recapito e attendere di parlare personalmente con il destinatario.
- Quando si ascoltano messaggi in segreteria, assicurarsi di non riprodurli in aree open space dove altri potrebbero sentirli. Cancellarli immediatamente dopo l'ascolto.

### Trasferimento dati tramite Bluetooth

Il Bluetooth NON deve essere approvato come metodo di comunicazione per dati riservati, personali o altrimenti sensibili non cifrati.

Laddove il Bluetooth venga utilizzato per scopi approvati (ad es. periferiche come tastiere, auricolari):

- L'autenticazione reciproca del dispositivo DEVE essere eseguita per tutte le connessioni.
- La cifratura DEVE essere abilitata per tutte le trasmissioni.
- DEVE essere utilizzato il Bluetooth Security Mode 4, Level 3 (cifratura autenticata) o superiore. I Security Mode 1 e 2 sono vietati.
- I dispositivi DEVONO essere impostati in modalità non rilevabile quando non è in corso l'associazione.
- L'associazione DEVE essere eseguita in un'area sicura e non pubblica.
- Gli utenti NON devono accettare trasmissioni di alcun tipo da dispositivi sconosciuti o sospetti.
- Il trasferimento file Bluetooth (OBEX) DEVE essere disabilitato salvo approvazione specifica.
- I profili Bluetooth DEVONO essere limitati a quelli necessari per la funzione approvata.

---

## Trasferimenti transfrontalieri di dati

I dati personali NON devono essere trasferiti in un paese al di fuori della Svizzera, a meno che non sia soddisfatta una delle seguenti condizioni:

| Salvaguardia | Descrizione |
|-------------|-------------|
| Decisione di adeguatezza | Il Consiglio federale svizzero ha stabilito che il paese di destinazione garantisce un livello adeguato di protezione dei dati (Allegato 1, OPDo). Ciò include tutti gli stati UE/SEE, il Regno Unito e altri paesi elencati. |
| Swiss-US Data Privacy Framework | Per i destinatari statunitensi certificati nell'ambito del DPF (in vigore da settembre 2024). Lo stato della certificazione DEVE essere verificato prima di ogni trasferimento. |
| Clausole Contrattuali Standard | SCC UE adattate per la nLPD svizzera, con l'IFPDT svizzero come autorità di controllo. DEVE essere completata una Valutazione dell'impatto del trasferimento (TIA). |
| Norme vincolanti d'impresa | Approvate dall'IFPDT svizzero per i trasferimenti intra-gruppo. |
| Consenso esplicito | L'interessato ha fornito il consenso esplicito e informato al trasferimento specifico dopo essere stato informato dei rischi. |
| Necessità contrattuale | Il trasferimento è necessario per l'esecuzione di un contratto con l'interessato. |

DEVE essere mantenuto un registro di tutti i trasferimenti transfrontalieri di dati nella piattaforma GRC dell'organizzazione, nel sistema di gestione documentale o in una posizione centrale equivalente. Il registro DEVE documentare il destinatario, il paese di destinazione, la base giuridica, le salvaguardie e la data di revisione. Il registro DEVE essere rivisto annualmente dal RSSI o dal Consulente per la protezione dei dati.

### Valutazione dell'impatto del trasferimento (TIA)

Per i trasferimenti verso paesi privi di una decisione di adeguatezza (che fanno affidamento sulle SCC o altre salvaguardie), DEVE essere condotta una Valutazione dell'impatto del trasferimento prima dell'avvio del trasferimento. La TIA DEVE valutare:

- **Contesto legale**: Leggi nel paese di destinazione che possono influire sulla protezione dei dati (accesso governativo, leggi sulla sorveglianza).
- **Circostanze pratiche**: Se il destinatario è soggetto a obblighi legali confliggenti o a richieste di accesso governativo ai dati.
- **Misure tecniche**: Cifratura, pseudonimizzazione o altre salvaguardie che rendono i dati incomprensibili a soggetti non autorizzati.
- **Misure contrattuali**: SCC, clausole contrattuali aggiuntive, diritti di audit, rimedi per gli interessati.
- **Rischio residuo**: Se le misure supplementari riducono il rischio a livelli accettabili.

I risultati della TIA DEVONO essere documentati e approvati dal RSSI o dal Consulente per la protezione dei dati prima dell'autorizzazione del trasferimento. Le TIA DEVONO essere riviste annualmente o al variare delle circostanze (cambiamenti legali nel paese di destinazione, incidente di sicurezza).

---

## Informazioni perse o mancanti

Qualora si scopra o si sospetti che informazioni siano andate perse, manchino, non siano arrivate o siano giunte alla persona sbagliata, il dipendente o l'utente terzo DEVE informare immediatamente il proprio responsabile di linea e il team di gestione della sicurezza delle informazioni. DEVE essere seguito il processo di gestione degli incidenti.

Le informazioni perse o indirizzate erroneamente DEVONO essere classificate come:

- **Critico**: Riguarda dati personali degni di particolare protezione, dati commerciali riservati o genera un rischio elevato per gli interessati (possibile obbligo di notifica della violazione ai sensi della nLPD).
- **Alto**: Riguarda dati personali o informazioni riservate ma con un numero limitato di interessati o volume limitato.
- **Medio**: Riguarda dati interni o non riservati senza dati personali.

L'individuo che ha inviato i dati è responsabile dell'avvio del rapporto di incidente e della cooperazione nell'indagine.

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa policy:

- **Registro degli accordi di trasferimento** (accordi con terzi con date di revisione) — *revisione annuale; aggiornamento al momento di nuovi accordi*
- **Registro dei trasferimenti transfrontalieri** (destinazioni, basi giuridiche, salvaguardie) — *revisione annuale da parte del RSSI/DPD; aggiornamento al momento di nuovi trasferimenti*
- **Log dei trasferimenti sicuri di file** (SFTP, HTTPS, piattaforma di condivisione cloud) — *conservati per 12 mesi; revisione trimestrale per anomalie*
- **Documenti di autenticazione del dominio email** (configurazione SPF, DKIM, DMARC e rapporti di conformità) — *rapporti DMARC rivisti mensilmente*
- **Inventario e registri di assegnazione dei supporti rimovibili** — *aggiornati per evento; riconciliati semestralmente con l'inventario degli asset*
- **Log di spedizione e conferme di ricezione da corriere** — *conservati per 12 mesi*
- **Rapporti di incidente** relativi a informazioni perse o indirizzate erroneamente — *conservati ai sensi della policy di gestione degli incidenti*
- **Valutazioni dell'impatto del trasferimento** (per trasferimenti verso paesi non adeguati) — *revisione annuale o al variare del contesto legale nel paese di destinazione*
- **Log dei trasferimenti di dati** (trasferimenti elettronici di dati riservati o personali) — *conservati per 12 mesi; accessibili per l'audit*

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, inclusi a titolo non esaustivo: audit dei log di trasferimento, revisioni degli accordi, rapporti di incidente, audit interni ed esterni, e feedback al proprietario della policy.

## Deroghe

Qualsiasi deroga a questa policy DEVE essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con documentazione dell'accettazione del rischio, dei controlli compensativi e di una data di revisione definita. Le deroghe DEVONO essere segnalate al Team di revisione del management.

## Non conformità

Un dipendente ritenuto responsabile di aver violato questa policy potrà essere soggetto a misure disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa policy è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO tener conto delle variazioni agli standard di trasferimento dei dati, delle minacce emergenti, dei cambiamenti normativi (inclusi gli aggiornamenti dell'elenco di adeguatezza svizzero) e delle lezioni apprese dagli incidenti.

---

# Sezioni della norma ISO 27001 trattate

Policy sul trasferimento delle informazioni — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità del management |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | 5.36 Conformità a policy, regole e standard |
| Clausola 7.3 Consapevolezza | **5.14 Trasferimento delle informazioni** |
| Clausola 7.5.3 Controllo delle informazioni documentate | 6.3 Sensibilizzazione, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 7.10 Supporti di archiviazione |

**Quadro normativo e legale**:

| Quadro di riferimento | Rilevanza |
|-----------------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative; Art. 16–17 — Trasferimenti transfrontalieri |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi di sicurezza dei dati; Allegato 1 — Elenco di adeguatezza |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento; Art. 44–49 — Trasferimenti internazionali |
| ISO/IEC 27001:2022 | Controllo Annex A 5.14 — Trasferimento delle informazioni |
| ISO/IEC 27002:2022 | Sezione 5.14 — Linee guida per l'implementazione del trasferimento delle informazioni |
| NIST SP 800-53 Rev 5 | SC-8 (Riservatezza e integrità delle trasmissioni), MP-5 (Trasporto dei supporti) |
| CIS Controls v8 | Controllo 3 (Protezione dei dati — Salvaguardia 3.10: Cifratura dei dati sensibili in transito) |

---

<!-- QA_VERIFIED: 2026-04-03 -->

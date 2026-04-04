<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.9-IT:operational:OP-POL:a.5.9 -->
**ISMS-OP-POL-A.5.9 — Gestione degli asset**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Gestione degli asset |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.5.9 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
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
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Data prossima revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.5.9 — Inventario delle informazioni e degli altri asset associati

**Controlli Annex A correlati**:

| Controllo | Relazione con la gestione degli asset |
|-----------|---------------------------------------|
| A.5.10 Uso accettabile delle informazioni e degli altri asset associati | Le regole di uso accettabile fanno riferimento agli asset inventariati |
| A.5.11 Restituzione degli asset | La restituzione degli asset viene tracciata nell'inventario; il registro viene aggiornato in caso di restituzione/smaltimento |
| A.5.12–13 Classificazione ed etichettatura delle informazioni | La classificazione viene assegnata agli asset informativi nel registro |
| A.5.14 Trasferimento delle informazioni | I controlli sul trasferimento si basano sulla classificazione degli asset |
| A.5.15–18 Controllo degli accessi e gestione delle identità | I diritti di accesso vengono approvati dai proprietari degli asset |
| A.7.10 Supporti di memorizzazione | I supporti rimovibili vengono registrati come asset |
| A.7.14 Smaltimento sicuro o riutilizzo delle apparecchiature | Lo smaltimento aggiorna lo stato nell'inventario |
| A.8.1 Dispositivi endpoint degli utenti | I dispositivi endpoint vengono registrati nell'inventario degli asset |
| A.8.8 Gestione delle vulnerabilità tecniche | La gestione delle patch richiede un inventario completo degli asset |
| A.8.9 Gestione della configurazione | Le baseline di configurazione sono collegate agli asset IT inventariati |

**Politiche interne correlate**:

- Politica di classificazione e gestione delle informazioni
- Politica di controllo degli accessi
- Politica di sicurezza degli endpoint
- Politica di uso accettabile
- Politica sulla privacy e protezione dei dati personali

---

# Politica di gestione degli asset

## Scopo

Lo scopo della presente politica è l'identificazione, la registrazione e la gestione degli asset dell'organizzazione per garantire un'adeguata protezione e responsabilità durante tutto il loro ciclo di vita.

La presente politica supporta la nLPD svizzera e l'OPDo (Ordinanza sulla protezione dei dati) attuando misure tecniche e organizzative appropriate al rischio per proteggere i dati personali, inclusa la conoscenza di quali dati esistono, dove sono archiviati e chi ne è responsabile. Laddove l'organizzazione tratti dati di soggetti nell'UE/SEE, si applicano altresì i requisiti del GDPR.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutte le informazioni, l'infrastruttura IT, le applicazioni, gli asset fisici e i servizi cloud dell'organizzazione ritenuti nell'ambito dalla dichiarazione di ambito di ISO 27001.

## Principio

Gli asset dell'organizzazione sono conosciuti, identificati, classificati e gestiti con un'adeguata protezione. Non è possibile proteggere ciò che non si sa di avere. L'inventario degli asset è il fondamento su cui dipendono tutti gli altri controlli di sicurezza — valutazione del rischio, controllo degli accessi, classificazione, gestione delle vulnerabilità, risposta agli incidenti e pianificazione della continuità operativa.

### Registro degli asset

L'organizzazione DEVE mantenere il registro degli asset in uno strumento o piattaforma centralizzata (es. sistema di gestione degli asset IT, CMDB o foglio di calcolo strutturato con controlli di accesso). Il registro DEVE essere accessibile ai proprietari degli asset, all'IT e ai membri del team di gestione della sicurezza delle informazioni, e protetto da modifiche non autorizzate.

---

## Categorie di asset

Le seguenti categorie di asset DEVONO essere inventariate:

| Categoria | Descrizione | Esempi |
|-----------|-------------|--------|
| **Hardware** | Dispositivi fisici che elaborano, archiviano o trasmettono informazioni | Server, workstation, laptop, dispositivi mobili, apparecchiature di rete (router, switch, firewall), stampanti |
| **Software e licenze** | Software installato e servizi in abbonamento | Sistemi operativi, applicazioni aziendali, strumenti di sviluppo, software di sicurezza, abbonamenti SaaS |
| **Dati e informazioni** | Informazioni digitali e fisiche con valore per l'organizzazione | Database, file share, backup, archivi, contratti, proprietà intellettuale, dati di configurazione |
| **Servizi cloud** | Servizi ospitati esternamente che elaborano dati dell'organizzazione | IaaS (macchine virtuali, storage), PaaS (database, piattaforme), SaaS (e-mail, CRM, collaborazione) |
| **Asset fisici** | Risorse tangibili a supporto della sicurezza delle informazioni | Uffici, sale server, casseforti, supporti rimovibili (chiavette USB, nastri di backup) |
| **Competenze del personale** | Ruoli chiave e competenze specialistiche critiche per le operazioni | Ruoli critici (punti di singolo guasto), certificazioni specialistiche, conoscenze istituzionali |

**Competenze del personale**: Il registro documenta **ruoli e competenze**, non verbali personali dei singoli. Esempio: "Competenza di Amministratore del database (2 dipendenti qualificati)" — non i nomi individuali. Laddove una funzione critica dipenda da un singolo individuo (punto di singolo guasto), ciò DEVE essere segnalato e DEVE essere documentato un piano di successione o di trasferimento delle conoscenze per mitigare il rischio.

---

## Inventario dell'hardware e dell'infrastruttura IT

Tutti gli asset hardware e dell'infrastruttura IT DEVONO essere registrati nell'inventario degli asset. Per ogni asset DEVONO essere registrati i seguenti attributi:

**Attributi obbligatori**:

| Attributo | Descrizione |
|-----------|-------------|
| **ID asset** | Identificatore univoco (es. HW-0042) |
| **Nome asset** | Nome leggibile dall'utente |
| **Tipo di asset** | Categoria (server, laptop, dispositivo di rete, dispositivo mobile, ecc.) |
| **Descrizione** | Scopo e funzione |
| **Proprietario** | Persona responsabile dell'asset (nome e ruolo) |
| **Dipartimento** | Unità organizzativa |
| **Numero di serie / Tag asset** | Identificatore fisico |
| **Ubicazione** | Ubicazione fisica (ufficio, rack, sede) |
| **Classificazione** | Ai sensi della Politica di classificazione e gestione delle informazioni |
| **Stato** | Attivo / In magazzino / Dismesso / Smaltito |
| **Ultima revisione** | Data dell'ultima verifica del record |

**Attributi aggiuntivi raccomandati**:

- Criticità (Alta / Media / Bassa) — basata su: **Alta** = la perdita causerebbe una significativa interruzione dell'attività, violazione normativa o perdita di dati; **Media** = la perdita causerebbe un impatto moderato, è disponibile una soluzione alternativa; **Bassa** = la perdita causa un impatto minimo, facilmente sostituibile
- Indirizzo IP o hostname (per gli asset connessi alla rete)
- Produttore, modello e versione firmware/OS
- Data di acquisizione e scadenza della garanzia
- Stato della cifratura

---

## Inventario del software e delle licenze

Il software e le licenze software DEVONO essere registrati nell'inventario degli asset. Per ogni asset software DEVONO essere registrati i seguenti attributi:

| Attributo | Descrizione |
|-----------|-------------|
| **Nome del software** | Nome del prodotto e editore |
| **Versione** | Versione corrente distribuita |
| **Proprietario** | Persona responsabile |
| **Tipo di licenza** | Perpetua, in abbonamento, open-source, freeware |
| **Numero di licenze** | Numero di licenze acquistate vs. distribuite |
| **Data di rinnovo** | Scadenza dell'abbonamento o prossimo rinnovo |
| **Ubicazione di distribuzione** | Dove il software è installato o ospitato |
| **Scopo aziendale** | Perché il software viene utilizzato |
| **Stato del supporto** | Supportato dal fornitore / End of Life (EOL) / End of Support (EOS) |

DEVE essere distribuito solo software approvato dall'organizzazione e con licenza. Il software non autorizzato scoperto durante le revisioni dell'inventario DEVE essere segnalato al team di gestione della sicurezza delle informazioni per la valutazione e la rimozione.

Il software che ha raggiunto la fine del ciclo di vita o la fine del supporto DEVE essere segnalato e prioritizzato per l'aggiornamento o la sostituzione. Laddove il software non supportato non possa essere immediatamente sostituito, il rischio DEVE essere documentato nel registro dei rischi con controlli compensativi.

---

## Inventario dei servizi cloud e SaaS

I servizi cloud (IaaS, PaaS, SaaS) DEVONO essere registrati nell'inventario degli asset insieme al software tradizionale. Per ogni servizio cloud DEVONO essere registrati i seguenti attributi aggiuntivi:

| Attributo | Descrizione |
|-----------|-------------|
| **Fornitore del servizio** | Nome del fornitore |
| **Tipo di servizio** | IaaS / PaaS / SaaS |
| **Residenza dei dati** | Paese o regione in cui i dati sono archiviati |
| **Classificazione dei dati** | Classificazione dei dati trattati dal servizio |
| **Integrazione SSO** | Se il servizio è integrato con l'identity provider dell'organizzazione |
| **Responsabile del contratto** | Persona responsabile della relazione con il fornitore |
| **Data di rinnovo** | Scadenza del contratto o dell'abbonamento |

I servizi cloud DEVONO essere classificati come:

- **Autorizzato**: Approvato dall'IT e dalla sicurezza per l'uso dell'organizzazione.
- **Tollerato**: Noto ma non formalmente approvato; in revisione (massimo 90 giorni prima di essere autorizzato o vietato).
- **Vietato**: Non autorizzato; DEVE essere rimosso.

I nuovi servizi cloud DEVONO essere registrati nell'inventario degli asset **prima** che i dati dell'organizzazione vengano trattati nel servizio (o entro 5 giorni lavorativi per i deployment di emergenza con approvazione del RSSI).

I servizi cloud non autorizzati (shadow IT) DEVONO essere identificati attraverso revisioni periodiche dei report di spesa, dei log SSO e del traffico di rete. I servizi di nuova scoperta DEVONO essere valutati per la conformità alla sicurezza e alla protezione dei dati prima di essere autorizzati.

---

## Inventario dei dati e degli asset informativi

I dati e gli asset informativi DEVONO essere identificati e ne DEVE essere redatto e mantenuto un inventario. Per ogni asset di dati DEVONO essere registrati i seguenti attributi:

| Attributo | Descrizione |
|-----------|-------------|
| **Nome asset** | Nome del dataset, del database o del deposito di informazioni |
| **Proprietario** | Persona responsabile (la parte aziendale, non il custode tecnico) |
| **Classificazione** | Ai sensi della Politica di classificazione e gestione delle informazioni |
| **Ubicazione di archiviazione** | Sistema o servizio in cui risiedono i dati |
| **Residenza dei dati** | Paese in cui i dati sono fisicamente archiviati |
| **Periodo di conservazione** | Per quanto tempo i dati vengono conservati, ai sensi dei requisiti di conservazione |
| **Dati personali** | Se il dataset contiene dati personali (Sì / No) |

Laddove gli asset di dati contengano dati personali, il registro dovrebbe acquisire campi aggiuntivi per supportare la conformità alla nLPD svizzera:

- Categorie di interessati
- Finalità del trattamento
- Categorie di destinatari
- Se si verificano trasferimenti transfrontalieri (e relative misure di protezione applicabili)

Queste informazioni possono essere registrate nell'inventario degli asset di dati o in un apposito **Registro delle attività di trattamento (RoPA)** ai sensi della nLPD Art. 12, con un riferimento incrociato tra i due registri.

---

## Titolarità degli asset

A ogni asset inventariato DEVE essere assegnato un proprietario. La titolarità non DEVE essere lasciata vuota.

**Proprietario** indica la persona responsabile della sicurezza dell'asset durante tutto il suo ciclo di vita. Non indica i diritti di proprietà legale. Il proprietario può delegare la gestione quotidiana a un custode (es. l'IT gestisce il server, ma il responsabile dell'unità aziendale è il proprietario dei dati su di esso), ma la responsabilità rimane in capo al proprietario.

### Responsabilità del proprietario

I proprietari degli asset DEVONO:

- Garantire che i propri asset siano inventariati e che i record siano accurati.
- Classificare gli asset in base al valore aziendale e al rischio.
- Revisionare i record dell'inventario degli asset di propria proprietà almeno annualmente.
- Approvare le richieste di accesso agli asset di propria proprietà.
- Segnalare gli incidenti di sicurezza che interessano gli asset di propria proprietà.
- Partecipare alle decisioni sul ciclo di vita degli asset (dismissione, archiviazione, smaltimento).

### Assegnazione della titolarità

- I nuovi asset DEVONO avere un proprietario assegnato al momento della registrazione.
- Laddove la titolarità non sia chiara, il team di gestione della sicurezza delle informazioni DEVE effettuare l'escalation al manager appropriato per la determinazione entro **30 giorni di calendario**.
- Gli asset senza un proprietario assegnato oltre i 30 giorni DEVONO essere escalati al RSSI con giustificazione documentata.
- I cambiamenti di titolarità (es. partenza di un dipendente, cambio di ruolo) DEVONO essere aggiornati nel registro entro **5 giorni lavorativi**.

### Asset orfani

**Asset non registrati scoperti**: Gli asset trovati in uso ma non nell'inventario DEVONO essere immediatamente registrati con un proprietario temporaneo (il manager del rilevatore o l'IT), investigati entro **14 giorni lavorativi** per determinare il proprietario aziendale e lo scopo, e formalmente assegnati a un proprietario permanente oppure dismessi.

**Partenza del proprietario**: Quando un proprietario di asset lascia l'organizzazione, la titolarità DEVE essere riassegnata al manager del dipendente uscente o al successore designato entro **10 giorni lavorativi** dalla partenza. Gli asset senza titolarità riassegnata dopo 30 giorni DEVONO essere escalati al RSSI.

---

## Ciclo di vita degli asset

### Registrazione

Tutti gli asset DEVONO essere registrati nell'inventario degli asset entro **5 giorni lavorativi** dall'acquisizione o dal deployment. Gli asset NON DEVONO essere connessi alla rete o utilizzati per trattare dati dell'organizzazione fino alla registrazione.

### Manutenzione e modifica

Qualsiasi modifica al proprietario, all'ubicazione, alla classificazione o allo stato di un asset DEVE essere riflessa nel registro entro **5 giorni lavorativi** dalla modifica.

### Dismissione e smaltimento

Quando un asset viene dismesso o smaltito:

- I dati DEVONO essere cancellati o distrutti in modo sicuro in linea con la Politica di classificazione e gestione delle informazioni, utilizzando metodi conformi al **NIST SP 800-88** (Linee guida per la sanificazione dei supporti): Clear (sovrascrittura logica) per dati INTERNI, Purge (cancellazione crittografica o smagnetizzazione) per dati RISERVATI, o Destroy (distruzione fisica) ove richiesto.
- Le licenze software DEVONO essere recuperate o disattivate.
- Il registro degli asset DEVE essere aggiornato per riflettere lo smaltimento, inclusa la data e il metodo di smaltimento.
- Per gli asset che hanno archiviato dati riservati o personali, DEVE essere conservata l'evidenza della sanificazione dei dati (es. certificato di distruzione, log di conferma della cancellazione).

### BYOD (Bring Your Own Device)

Laddove il BYOD sia consentito, i dispositivi di proprietà personale utilizzati per accedere ai dati dell'organizzazione DEVONO essere registrati nell'inventario degli asset con un flag che indica la proprietà personale. Attributi minimi di registrazione BYOD:

- Tipo di dispositivo e sistema operativo
- Nome del dipendente
- Ambito di utilizzo aziendale (solo e-mail, accesso completo, ecc.)
- Stato di iscrizione MDM
- Accordo BYOD firmato (data)

Alla risoluzione del contratto o alla fine del rapporto di lavoro, i dati dell'organizzazione DEVONO essere cancellati dal dispositivo personale e il record BYOD DEVE essere aggiornato.

---

## Uso accettabile degli asset

L'uso accettabile degli asset DEVE essere in linea con la Politica di uso accettabile.

Gli utenti NON DEVONO installare software non autorizzato, connettere dispositivi non approvati alla rete o utilizzare gli asset dell'organizzazione per scopi al di fuori del proprio ruolo.

---

## Restituzione degli asset

Tutti i dipendenti e gli utenti terzi DEVONO restituire tutti gli asset dell'organizzazione in loro possesso alla cessazione del loro rapporto di lavoro, contratto o accordo.

Laddove un dipendente o un utente terzo abbia utilizzato la propria attrezzatura personale (BYOD), le procedure DEVONO garantire che tutte le informazioni dell'organizzazione vengano trasferite all'organizzazione e cancellate in modo sicuro dal dispositivo personale.

Durante i periodi di preavviso, l'organizzazione DEVE adottare misure ragionevoli per prevenire la copia non autorizzata di informazioni dell'organizzazione da parte di dipendenti o utenti terzi in partenza.

Il registro degli asset DEVE essere aggiornato per riflettere tutti gli asset restituiti, riassegnati o smaltiti.

---

## Revisione degli asset

L'inventario degli asset DEVE essere revisionato ai seguenti intervalli:

| Tipo di revisione | Frequenza | Responsabile |
|------------------|-----------|--------------|
| **Aggiornamenti basati su eventi** | Continuativamente (entro 5 giorni lavorativi dalla modifica) | Proprietari degli asset e IT |
| **Attestazione del proprietario** | Annualmente | Ogni proprietario di asset conferma l'accuratezza dei propri asset assegnati |
| **Audit completo dell'inventario** | Annualmente (allineato al riesame della direzione) | Team di gestione della sicurezza delle informazioni |
| **Revisione di scoperta cloud/SaaS** | Trimestralmente | IT e team di gestione della sicurezza delle informazioni |
| **Conformità delle licenze software** | Semestralmente | IT |

I responsabili di dipartimento DEVONO confermare che i loro elenchi di asset siano aggiornati durante la revisione annuale. Le discrepanze DEVONO essere investigate e risolte entro 30 giorni.

---

## Evidenze

Le seguenti evidenze dimostrano la conformità alla presente politica:

- **Registro dell'inventario degli asset** (hardware, software, dati, servizi cloud — con attributi obbligatori popolati) — *mantenuto nello strumento centralizzato; esportato come evidenza di audit*
- **Verbali di assegnazione del proprietario dell'asset** — *obiettivo: 100% degli asset con proprietari assegnati; misurato trimestralmente*
- **Verbali di attestazione del proprietario** (conferme della revisione annuale) — *firmati da ogni proprietario di asset; conservati per 3 anni*
- **Registro dei servizi cloud/SaaS** con residenza dei dati e classificazione — *aggiornato per evento; revisionato trimestralmente*
- **Verbali di conformità delle licenze software** (licenze acquistate vs. distribuite) — *verificati semestralmente*
- **Verbali di smaltimento degli asset** (data, metodo, evidenza di sanificazione NIST SP 800-88, certificati di distruzione) — *conservati per 5 anni*
- **Verbali di registrazione BYOD e firme degli accordi** (se applicabile) — *aggiornati per evento; revisionati annualmente*
- **Report annuale di audit dell'inventario** con risultati e azioni di remediation — *presentato al riesame della direzione*
- **Metrica di completezza dell'inventario** — *obiettivo: ≥95% degli asset noti registrati con attributi obbligatori completi; misurato annualmente*
- **Report di scoperta dello shadow IT** — *revisioni trimestrali documentate con esiti della valutazione*

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica attraverso vari metodi, inclusi ma non limitati a: audit del registro degli asset, revisioni dell'attestazione del proprietario, verifiche della conformità delle licenze, audit interni ed esterni, e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione alla presente politica DEVE essere approvata e registrata dal Responsabile della sicurezza delle informazioni in anticipo, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni DEVONO essere riferite al team di Riesame della direzione.

## Non conformità

Un dipendente che abbia violato la presente politica può essere soggetto a provvedimenti disciplinari, fino e inclusa la risoluzione del rapporto di lavoro.

## Miglioramento continuo

La presente politica è revisionata e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO considerare i cambiamenti agli standard di gestione degli asset, i cambiamenti organizzativi (acquisizioni, ristrutturazioni), l'adozione di servizi cloud, i cambiamenti normativi e le lezioni apprese dagli incidenti e dagli audit.

---

# Aree dello standard ISO 27001 trattate

Politica di gestione degli asset — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità del management |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | **5.9 Inventario delle informazioni e degli altri asset associati** |
| | 5.10 Uso accettabile delle informazioni e degli altri asset associati |
| | 5.11 Restituzione degli asset |
| | 6.3 Sensibilizzazione, formazione e istruzione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|------------------|-----------|
| nLPD svizzera | Art. 8 — Misure tecniche e organizzative (richiede la conoscenza di quali dati esistono e dove); Art. 12 — Registro delle attività di trattamento |
| OPDo svizzera | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR dell'UE (ove applicabile) | Art. 5 — Principio di responsabilità; Art. 30 — Registro delle attività di trattamento; Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Controllo Annex A 5.9 — Inventario delle informazioni e degli altri asset associati |
| ISO/IEC 27002:2022 | Sezione 5.9 — Guida all'implementazione |
| NIST SP 800-53 Rev 5 | CM-8 (Inventario delle componenti del sistema), PM-5 (Inventario dei sistemi) |
| CIS Controls v8 | Controllo 1 (Inventario e controllo degli asset aziendali), Controllo 2 (Inventario e controllo degli asset software) |

---

<!-- QA_VERIFIED: 2026-04-03 -->

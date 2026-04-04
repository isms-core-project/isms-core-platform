<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.6.4-5-IT:operational:OP-POL:a.6.4-5 -->
**ISMS-OP-POL-A.6.4-5 — Processo disciplinare e fine del rapporto di lavoro**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Processo disciplinare e fine del rapporto di lavoro |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.6.4-5 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Responsabile HR (DRH) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI / DRH | Policy operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.6.4 — Processo disciplinare
- ISO/IEC 27001:2022 Controllo A.6.5 — Responsabilità dopo la fine o il cambio del rapporto di lavoro
- ISO/IEC 27002:2022 Sezioni 6.4, 6.5 — Guida all'implementazione
- CO svizzero Art. 328 (Obbligo di protezione), Art. 337 (Licenziamento per giusta causa), Art. 337d (Abbandono del posto di lavoro)
- nLPD svizzera (revLPD) — Diritti degli interessati e revoca degli accessi

**Controlli Allegato A correlati**:

| Controllo | Relazione con il processo disciplinare e la fine del rapporto di lavoro |
|-----------|-------------------------------------------------------------------------|
| A.5.1 Policy per la sicurezza delle informazioni | Policy che il processo disciplinare fa rispettare |
| A.5.10 Uso accettabile delle informazioni e degli altri asset | Le violazioni dell'uso accettabile attivano azioni disciplinari |
| A.5.11 Restituzione degli asset | Requisiti di restituzione degli asset alla fine del rapporto di lavoro |
| A.5.15-16-18 Gestione delle identità e degli accessi | Esecuzione della revoca degli accessi per coloro che lasciano o cambiano ruolo |
| A.5.24-28 Ciclo di vita della gestione degli incidenti | Le violazioni di sicurezza possono costituire incidenti che richiedono indagini parallele |
| A.6.3 Consapevolezza e formazione sulla sicurezza delle informazioni | L'adeguatezza della formazione considerata come fattore attenuante nelle decisioni disciplinari |
| A.6.6 Accordi di riservatezza e di non divulgazione | Gli obblighi NDA continuano dopo il rapporto di lavoro |
| A.6.7-8 Lavoro a distanza e segnalazione degli eventi | Revoca dell'accesso remoto alla fine del rapporto; la segnalazione degli eventi può attivare provvedimenti disciplinari |
| A.8.2-3-5 Autenticazione e accesso privilegiato | Priorità nella revoca dell'accesso privilegiato alla cessazione |

**Policy interne correlate**:

- Policy sul controllo degli accessi
- Policy sull'uso accettabile e restituzione degli asset
- Policy sulla gestione degli incidenti
- Policy sulla classificazione e gestione delle informazioni
- Policy sugli accordi di riservatezza e di non divulgazione
- Policy sulla privacy e protezione dei dati personali
- Policy di screening pre-assunzione (i risultati delle verifiche dei precedenti personali sono indicati per i recidivi o i ruoli sensibili alla fiducia)

---

# Policy sul processo disciplinare e la fine del rapporto di lavoro

## Scopo

Lo scopo di questa policy è stabilire il processo disciplinare formale dell'organizzazione per le violazioni delle policy di sicurezza delle informazioni e definire i requisiti per la cessazione sicura o il cambio del rapporto di lavoro, inclusa la revoca degli accessi, il recupero degli asset e gli obblighi post-impiego.

Questa policy supporta la nLPD svizzera (revLPD) implementando misure tecniche e organizzative per garantire che l'accesso ai dati personali venga revocato tempestivamente alla cessazione o al cambio del rapporto di lavoro, e che gli obblighi di protezione dei dati vengano comunicati e applicati durante e oltre il ciclo di vita del rapporto di lavoro. Laddove l'organizzazione tratti dati di persone nell'UE/SEE, si applicano anche i requisiti del GDPR.

**Approccio combinato ai controlli**: I Controlli A.6.4 (Processo disciplinare) e A.6.5 (Responsabilità dopo la fine o il cambio del rapporto di lavoro) vengono implementati congiuntamente perché le azioni disciplinari relative alla sicurezza spesso precedono la cessazione del rapporto, e entrambi richiedono processi coordinati HR-Sicurezza con requisiti condivisi di revoca degli accessi, restituzione degli asset e documentazione.

## Ambito

Questa policy si applica a:

- Tutti i dipendenti, collaboratori, lavoratori temporanei e stagisti.
- Tutti i tipi di cessazione: dimissioni volontarie, licenziamento per giusta causa, licenziamento immediato, pensionamento, fine contratto, cambio di ruolo (trasferimento) e abbandono del posto di lavoro.
- Tutti i tipi di violazioni di sicurezza: violazioni delle policy, infrazioni dell'uso accettabile, mancanze nella gestione dei dati e comportamenti illeciti deliberati.
- Tutti i tipi di asset: fisici, logici, informativi e di proprietà intellettuale.

**Fuori ambito**:

- Screening pre-assunzione (vedere A.5.1-2-6.1-2 — Governance SGSI e impiego sicuro).
- Requisiti di formazione sulla sicurezza in corso (vedere A.6.3 — Consapevolezza e formazione sulla sicurezza delle informazioni).
- Procedure di cessazione con terze parti o fornitori (vedere A.5.19-23 — Sicurezza dei servizi cloud e dei fornitori).

## Principio

L'organizzazione DEVE mantenere un processo disciplinare formale e documentato che sia equo, proporzionato e allineato con il diritto del lavoro svizzero. Il processo DEVE scoraggiare le violazioni delle policy di sicurezza delle informazioni, proteggere i diritti degli individui e garantire conseguenze appropriate per le violazioni delle policy. Alla cessazione o al cambio del rapporto di lavoro, l'organizzazione DEVE revocare tempestivamente gli accessi, recuperare gli asset e comunicare gli obblighi continuativi al personale in uscita.

---

## Framework disciplinare (A.6.4)

### Riferimento al controllo ISO

> *Un processo disciplinare dovrebbe essere formalizzato e comunicato per adottare misure nei confronti del personale e di altre parti interessate pertinenti che abbiano commesso una violazione della policy di sicurezza delle informazioni.*
> — ISO/IEC 27001:2022, Controllo A.6.4 dell'Allegato A

### Principi

Il processo disciplinare DEVE essere:

- **Equo e coerente** — applicato allo stesso modo a tutto il personale indipendentemente dall'anzianità o dal ruolo.
- **Proporzionato** — la risposta DEVE corrispondere alla gravità della violazione e alle sue conseguenze.
- **Allineato con il diritto del lavoro** — conforme al CO svizzero Art. 328 (obbligo di protezione del datore di lavoro) e alle normative cantonali applicabili in materia di lavoro.
- **Documentato** — tutti i procedimenti registrati con prove appropriate e mantenuti in modo riservato.
- **Progressivo** — risposta graduata ove le circostanze lo consentano, dall'avvertimento verbale fino al licenziamento.
- **Tempestivo** — le violazioni vengono investigate e affrontate senza indebito ritardo.

Il processo disciplinare è allo stesso tempo **preventivo** (scoraggiare la negligenza comunicando le conseguenze) e **correttivo** (affrontare le violazioni per prevenire il ripetersi).

### Categorie di violazione

| Categoria | Esempi | Risposta tipica |
|-----------|--------|----------------|
| **Minore / Involontaria** | Violazione accidentale della policy (es. invio di dati interni al destinatario errato), prima violazione minore, mancato blocco dello schermo | Avvertimento verbale, formazione aggiuntiva, coaching documentato |
| **Moderata** | Violazioni minori ripetute dopo avvertimento, gestione negligente dei dati, condivisione delle credenziali con un collega, installazione di software non approvato | Avvertimento scritto, formazione di recupero obbligatoria, monitoraggio intensificato |
| **Grave** | Violazione deliberata della policy, significativa esposizione dei dati, aggiramento dei controlli di sicurezza, accesso ai dati senza autorizzazione | Avvertimento scritto finale, sospensione in attesa di indagini, licenziamento |
| **Comportamento illecito grave** | Furto o esfiltrazione dolosa di dati, sabotaggio dei sistemi, vendita di informazioni riservate, attività criminale | Licenziamento immediato (Art. 337 CO), azione legale, notifica normativa |

**Fattori aggravanti**: Intento deliberato, occultamento della violazione, abuso dell'accesso privilegiato, avvertimenti precedenti in archivio, danno agli interessati.

**Fattori attenuanti**: Auto-segnalazione, errore involontario, formazione insufficiente fornita, guida poco chiara sulla policy, azione correttiva immediata da parte dell'individuo.

**Adeguamento della gravità in base al ruolo**:

Per le violazioni che riguardano abuso degli accessi, gestione dei dati o condivisione delle credenziali, applicare il moltiplicatore di rischio del ruolo:
- **Utente standard**: Gravità base.
- **Utente con accesso privilegiato** (amministratore, sviluppatore, amministratore DB): +1 livello di gravità (moderata diventa grave).
- **Dirigente/alta dirigenza**: +1 livello di gravità (rischio reputazionale).
- **Membro del team di sicurezza**: +2 livelli di gravità (viola il fondamento di fiducia).

*Esempio*: Condivisione delle credenziali da parte di un utente standard = Moderata (avvertimento scritto). Stessa azione da parte di un amministratore DB = Grave (avvertimento finale o licenziamento).

**Auto-segnalazione delle violazioni**:

I dipendenti che auto-segnalano le violazioni delle policy prima della scoperta da parte della Direzione/team di sicurezza ricevono:
- Riduzione della classificazione della gravità (riduzione di un livello: grave diventa moderata) ove appropriato.
- Considerazione per il rimedio non disciplinare (formazione, miglioramento dei processi) per le prime violazioni involontarie.
- Documentazione della cooperazione in buona fede.

**Procedura di auto-segnalazione**: Segnalare al responsabile, alle HR o all'RSSI (canale anonimo disponibile tramite [Hotline etica]). L'auto-segnalazione DEVE avvenire entro 24 ore dalla scoperta della violazione da parte del dipendente.

**Esclusioni**: Il comportamento illecito grave (furto di dati, sabotaggio) non è idoneo alla riduzione della gravità attraverso l'auto-segnalazione.

### Procedura di indagine

La seguente procedura in cinque fasi DEVE essere seguita per tutte le violazioni delle policy di sicurezza delle informazioni:

**Fase 1 — Segnalazione**: La violazione viene segnalata alle HR e al team di sicurezza delle informazioni. Le segnalazioni possono provenire dal monitoraggio automatizzato, dall'osservazione della Direzione, dalla segnalazione di colleghi, dai risultati degli audit o dall'auto-segnalazione.

**Fase 2 — Valutazione preliminare**: Le HR e il team di sicurezza delle informazioni valutano congiuntamente la gravità della violazione segnalata. La valutazione determina se è giustificata un'indagine formale e se sono necessarie misure provvisorie (es. sospensione degli accessi).

**Tempistiche della valutazione preliminare per gravità**:
- **Sospetto comportamento illecito grave** (furto di dati, sabotaggio, attività criminale): Valutazione immediata (entro 2 ore), accesso sospeso in attesa di indagini.
- **Violazioni gravi**: Valutazione entro 4 ore lavorative.
- **Violazioni moderate**: Valutazione entro 1 giorno lavorativo.
- **Violazioni minori**: Valutazione entro 2 giorni lavorativi.

La gravità viene inizialmente determinata dal segnalante (responsabile, team di sicurezza, HR). La sovra-classificazione è accettabile; la sotto-classificazione crea rischi.

**Fase 3 — Raccolta delle prove**: Le prove pertinenti vengono raccolte e conservate, inclusi:
- Registri di sistema, tracce di audit e registrazioni degli accessi (da [SIEM] o [Fornitore di identità]).
- Registrazioni e-mail e registri di accesso ai file.
- Dichiarazioni testimoniali.
- Prove fisiche (documenti, dispositivi).
- Avvertimenti precedenti o registrazioni disciplinari.

Le prove DEVONO essere raccolte in modo che rispetti i diritti dell'individuo ai sensi del CO svizzero Art. 328 e della nLPD. La catena di custodia DEVE essere documentata.

**Fase 4 — Indagine**: Viene condotta un'indagine formale, inclusi colloqui con la persona interessata, i testimoni e i responsabili pertinenti. L'individuo DEVE essere informato della natura delle accuse e avere l'opportunità di rispondere. Per i casi di violazioni gravi o comportamenti illeciti gravi, DEVE essere consultato il Consulente legale.

**Fase 5 — Documentazione dei risultati**: I risultati dell'indagine vengono documentati, incluse le prove esaminate, la risposta dell'individuo, la conclusione raggiunta e il provvedimento disciplinare raccomandato. Il rapporto d'indagine è conservato nel fascicolo HR riservato con accesso limitato al personale autorizzato.

### Decisione e azione

A seguito dell'indagine:

1. **Determinazione della gravità** — La violazione viene categorizzata per la tabella delle categorie di violazione sopra.
2. **Fattori attenuanti e aggravanti** — Vengono considerate tutte le circostanze pertinenti, incluso se l'individuo ha ricevuto una formazione adeguata (per A.6.3), se si tratta di una prima o di un'infrazione ripetuta, e il registro complessivo della condotta dell'individuo.
3. **Selezione dell'azione** — Il provvedimento disciplinare appropriato viene selezionato dall'intervallo definito per la categoria di violazione.
4. **Comunicazione** — La decisione viene comunicata all'individuo per iscritto, con una spiegazione chiara delle motivazioni e il diritto di ricorso.
5. **Implementazione** — L'azione viene implementata, incluse eventuali restrizioni di accesso, formazione aggiuntiva o modifiche al rapporto di lavoro.
6. **Seguito** — Laddove l'individuo rimanga in servizio, viene applicato un monitoraggio di follow-up per un periodo definito per verificare la conformità.

### Garanzie procedurali

I seguenti requisiti di garanzia procedurale DEVONO essere osservati in tutti i procedimenti disciplinari, in conformità con il CO svizzero Art. 328 (obbligo di protezione del datore di lavoro):

- L'individuo DEVE essere **informato delle accuse specifiche** per iscritto prima di qualsiasi udienza disciplinare.
- All'individuo DEVE essere concessa una **ragionevole opportunità di rispondere** alle accuse, incluso il tempo per prepararsi.
- L'individuo DEVE avere il **diritto di essere rappresentato** alle riunioni disciplinari (es. un collega, un rappresentante sindacale o un consulente legale, come consentito dalla normativa sul lavoro applicabile).
- DEVE essere disponibile un **processo di ricorso**:
  - **Idoneità**: Decisioni per violazioni Moderate, Gravi o Comportamenti illeciti gravi (le violazioni minori non sono appellabili).
  - **Scadenza di presentazione**: 10 giorni lavorativi dal ricevimento della decisione disciplinare scritta.
  - **Modulo di ricorso**: Ricorso scritto con motivazioni presentato al DRH.
  - **Organo di revisione**: Commissione di 2-3 persone non coinvolte nell'indagine originale (es. DRH + consulente HR esterno, o Responsabile senior + DPD).
  - **Tempistiche**: Ricorso esaminato entro 15 giorni lavorativi dalla presentazione; decisione entro 5 giorni lavorativi dall'udienza.
  - **Ambito**: Revisione dell'equità del processo, della proporzionalità dell'azione, considerazione di nuove prove.
  - **Esito**: Conferma, riduzione della sanzione o annullamento. La decisione è definitiva (nessun ulteriore ricorso interno).
  - **Documentazione**: Decisione sul ricorso documentata e inserita nel fascicolo HR.
- Tutta la documentazione DEVE essere mantenuta in modo **riservato**, con accesso limitato a coloro che hanno una legittima necessità di sapere.
- I **dati personali** dell'individuo trattati durante l'indagine DEVONO essere gestiti in conformità alla nLPD e alla Policy sulla privacy e protezione dei dati personali dell'organizzazione.

### Coinvolgimento del team di sicurezza

Il team di sicurezza delle informazioni DEVE essere coinvolto nelle questioni disciplinari quando:

- La violazione riguarda una violazione della policy di sicurezza delle informazioni o una sospetta violazione dei dati.
- È richiesta un'indagine tecnica (analisi dei log, esame forense, revisione degli accessi).
- La revoca degli accessi, la sospensione dell'account o il monitoraggio intensificato è raccomandato come misura provvisoria o definitiva.
- Esiste il rischio per la sicurezza in corso (es. indicatori di minaccia interna).
- Potrebbe essere richiesta una notifica legale o normativa (es. notifica della violazione dei dati personali ai sensi dell'Art. 24 nLPD).

### Escalation e notifica

| Gravità della violazione | Notifica interna | Notifica esterna |
|--------------------------|-----------------|-----------------|
| **Minore** | Responsabile di linea, HR | Nessuna |
| **Moderata** | HR, RSSI | In genere nessuna |
| **Grave** | HR, RSSI, Consulente legale | Autorità di regolamentazione in caso di violazione dei dati personali (nLPD Art. 24) |
| **Comportamento illecito grave** | HR, RSSI, Consulente legale, Direzione generale | Polizia (se penale), autorità di regolamentazione (nLPD Art. 24, GDPR Art. 33 ove applicabile) |

**Notifica normativa**: Laddove una questione disciplinare riguardi una violazione dei dati personali confermata o sospetta, l'organizzazione DEVE valutare gli obblighi di notifica:

- **Fattori di valutazione del rischio**: Volume dei record interessati, sensibilità dei dati (i dati personali degni di particolare protezione ai sensi dell'Art. 5(c) nLPD attivano una maggiore urgenza), se i dati erano cifrati, probabilità di danno agli interessati, se la violazione è stata contenuta.
- **nLPD Art. 24**: Notifica all'IFPDT il prima possibile laddove la violazione possa comportare un rischio elevato per la personalità o i diritti fondamentali degli interessati. Nessuna scadenza fissa, ma "il prima possibile" interpretato come entro 72 ore dagli orientamenti dell'IFPDT.
- **GDPR Art. 33** (ove applicabile): Notifica all'autorità di vigilanza entro 72 ore dalla presa di conoscenza. Documentare i motivi del ritardo se superato.
- **Notifica agli interessati**: Richiesta ai sensi dell'Art. 24(4) nLPD ove necessario per la protezione dell'interessato o su richiesta dell'IFPDT. Ai sensi dell'Art. 34 GDPR, richiesta laddove vi sia un rischio elevato per i diritti e le libertà.
- **Soglie di notifica**: Qualsiasi violazione che coinvolga 1+ record di dati personali degni di particolare protezione (sanitari, biometrici, origine razziale/etnica) o 100+ record di dati personali standard attiva la valutazione obbligatoria dell'IFPDT. RSSI + DPD effettuano la determinazione entro 24 ore dalla conferma della violazione.

---

## Fine del rapporto di lavoro (A.6.5)

### Riferimento al controllo ISO

> *Le responsabilità e i compiti in materia di sicurezza delle informazioni che rimangono validi dopo la cessazione o il cambio del rapporto di lavoro dovrebbero essere definiti, applicati e comunicati al personale pertinente e alle altre parti interessate.*
> — ISO/IEC 27001:2022, Controllo A.6.5 dell'Allegato A

### Tempistiche di revoca degli accessi

Gli accessi DEVONO essere revocati secondo le seguenti tempistiche in base al tipo di cessazione:

| Tipo di cessazione | Tempistica di revoca degli accessi | Trigger |
|--------------------|------------------------------------|---------|
| **Licenziamento immediato** (comportamento illecito grave, Art. 337 CO) | Entro **1 ora** dalla decisione di licenziamento | Le HR registrano la cessazione in [Sistema HR]; ticket di offboarding IT sollevato immediatamente |
| **Licenziamento per giusta causa** | **Stesso giorno lavorativo**, prima della notifica ove possibile | Le HR registrano la cessazione; ticket di offboarding IT sollevato |
| **Dimissioni volontarie** | **Ultimo giorno lavorativo**, fine turno | Le HR registrano la data di uscita; offboarding IT programmato |
| **Pensionamento** | **Ultimo giorno lavorativo** | Le HR registrano la data di pensionamento; offboarding IT programmato |
| **Fine contratto** | **Data di fine contratto** | Le HR registrano la fine del contratto; offboarding IT programmato |
| **Cambio di ruolo — escalation dei privilegi** (standard a amministratore) | Nuovo accesso concesso entro **2 giorni lavorativi** dall'approvazione | Il responsabile notifica HR e IT del cambio di ruolo |
| **Cambio di ruolo — riduzione dei privilegi** (amministratore a standard) | Accesso elevato revocato **stesso giorno lavorativo** (entro 4 ore) | Il responsabile notifica HR e IT del cambio di ruolo |
| **Cambio di ruolo — spostamento laterale** (stesso livello di privilegio) | Accesso adeguato entro **2 giorni lavorativi** | Il responsabile notifica HR e IT del cambio di ruolo |
| **Cambio di ruolo — impatto sulla fiducia** (disciplinare, PIP, preoccupazione di sicurezza) | Revoca immediata per tempistiche "Licenziamento immediato" | Notifica HR e RSSI |
| **Abbandono del posto di lavoro** (Art. 337d CO) | Entro **1 ora** dalla determinazione dell'abbandono | Le HR determinano l'abbandono; ticket di offboarding IT sollevato |

### Autorizzazione al licenziamento immediato (Art. 337 CO)

Prima di eseguire il licenziamento immediato, DEVONO essere osservate le seguenti garanzie procedurali:

- **Autorizzazione richiesta**: DRH + Consulente legale (conferma la giusta causa ai sensi del CO Art. 337).
- **Tempistiche**: Decisione e revoca degli accessi nello stesso giorno lavorativo (il ritardo mina il requisito di "immediatezza" ai sensi della legge svizzera).
- **Documentazione**: Lettera di licenziamento scritta preparata prima o immediatamente dopo la notifica, indicante "licenziamento immediato per giusta causa" (motivazioni specifiche fornite su richiesta del dipendente ai sensi del CO Art. 337 cpv. 2).
- **Revoca degli accessi**: Eseguita entro 1 ora dall'autorizzazione, idealmente prima della notifica al dipendente ove operativamente fattibile (riduce il rischio di sabotaggio).
- **Post-revoca**: Le HR verificano la completezza della documentazione scritta entro 2 ore.

**Esempi di giusta causa** (CO Art. 337): furto, frode, grave violazione dei doveri, violenza, rifiuto di lavorare, negligenza grave che causa danni significativi. Le violazioni minori non sono sufficienti anche se ripetute.

**Trigger SLA**: Il timer di revoca degli accessi inizia quando la decisione di cessazione viene registrata in [Sistema HR] e la richiesta di offboarding IT viene inviata tramite [Strumento ITSM].

**Protocollo di notifica della cessazione**:
- **Sistema HR**: La cessazione registrata in [Sistema HR] attiva la notifica automatica all'IT Service Desk e al team IAM.
- **Notifica e-mail**: E-mail automatizzata inviata a [ITServiceDesk@], [IAM@], [RSSI@] entro 5 minuti dall'inserimento nel Sistema HR.
- **Notifica di backup**: Per i licenziamenti immediati, le HR telefonano all'IT Service Desk (hotline di emergenza: [numero]) per avviare la notifica verbale prima dell'inserimento nel sistema.
- **Conferma**: L'IT Service Desk conferma la ricezione e crea il ticket di offboarding entro 15 minuti.

**Controlli compensativi quando l'SLA non può essere rispettato**: Se la revoca completa su tutti i sistemi non può essere completata entro l'SLA, i seguenti controlli compensativi DEVONO essere applicati **immediatamente** mentre la revoca completa viene completata:

| Controllo compensativo | Azione | Tempistiche |
|-----------------------|--------|-------------|
| **Disabilitazione IdP** | Account utente disabilitato nel [Fornitore di identità] (blocca SSO a tutte le applicazioni integrate) | Entro 15 minuti |
| **Disabilitazione VPN** | Credenziali VPN revocate | Entro 15 minuti |
| **Disabilitazione badge** | Badge di accesso fisico disattivato | Entro 30 minuti |
| **Disabilitazione e-mail** | Account e-mail sospeso (posta in arrivo reindirizzata al responsabile o alla casella di posta condivisa) | Entro 30 minuti |

DEVE essere creato un record di non conformità o eccezione per qualsiasi violazione dell'SLA, con analisi della causa radice e rimedio monitorati fino alla chiusura per il processo delle azioni correttive.

### Determinazione dell'abbandono del posto di lavoro (Art. 337d CO)

**Criteri di abbandono** (per il CO svizzero Art. 337d):
- Dipendente assente senza autorizzazione per 3+ giorni lavorativi consecutivi.
- Nessuna risposta ai tentativi di contatto del responsabile (telefono, e-mail, contatto d'emergenza).
- Nessuna spiegazione accettabile (emergenza medica, forza maggiore escluse).

**Procedura di abbandono**:
1. **Giorno 1-2 di assenza**: Il responsabile tenta il contatto (3 tentativi nell'arco di 2 giorni, documentati).
2. **Giorno 3**: Le HR vengono notificate; tentativo di contatto d'emergenza.
3. **Pomeriggio del Giorno 3**: Se non c'è risposta, le HR escalano al DRH + Consulente legale.
4. **Determinazione dell'abbandono**: Il DRH effettua la determinazione finale con revisione legale.
5. **Revoca degli accessi**: Immediata (per SLA di 1 ora) alla determinazione.
6. **Notifica scritta**: Lettera raccomandata inviata all'ultimo indirizzo noto confermando la cessazione e il requisito di restituzione degli asset.
7. **Richiesta di risarcimento**: Le Finanze avviano la richiesta di 1/4 del salario mensile (scadenza 30 giorni per il CO Art. 337d).

**Prevenzione dei falsi positivi**: Le emergenze mediche, gli incidenti e la forza maggiore vengono verificati prima della finalizzazione della determinazione dell'abbandono.

### Ambito della revoca degli accessi

Tutti i tipi di accesso DEVONO essere affrontati durante il processo di offboarding:

| Tipo di accesso | Requisito di revoca |
|-----------------|---------------------|
| **Accesso fisico** | Badge disabilitato, chiavi restituite, registrazione biometrica rimossa. **Coordinamento fisico-logico**: La revoca dell'accesso fisico DEVE essere coordinata con la revoca dell'accesso logico per prevenire scenari in cui una persona mantiene l'accesso con badge dopo la disabilitazione degli account logici (o viceversa). Entrambi i tipi di revoca DEVONO essere avviati dallo stesso ticket di offboarding e confermati completi prima dell'approvazione finale. |
| **Accesso logico** | Tutti gli account disabilitati: servizi di directory, e-mail, applicazioni aziendali, VPN, piattaforme cloud |
| **Accesso remoto** | Credenziali VPN revocate, sessioni di desktop remoto terminate, profilo MDM rimosso |
| **Accesso di terze parti** | Account portale fornitori disabilitati, credenziali di sistema partner revocate |
| **Accesso delegato** | Accesso alla casella di posta condivisa rimosso, password degli account condivisi ruotate, chiavi API revocate |
| **Accesso ai dati** | Autorizzazioni di condivisione file rimosse, accesso al database revocato, autorizzazioni di archiviazione cloud rimosse |

**Sequenza di priorità per la revoca dell'accesso privilegiato**:

Laddove la persona in partenza detenga accesso privilegiato, la revoca DEVE seguire questo ordine di priorità:

| Priorità | Tipo di accesso | Tempistiche obiettivo | Motivazione |
|----------|-----------------|-----------------------|-------------|
| **P1 — Immediato** | Amministratore di dominio, root/sudo, amministratore cloud (AWS root, Azure Global Admin), amministratore database, amministratore strumenti di sicurezza | Entro 15 minuti dalla decisione di cessazione | Massimo raggio d'azione; può compromettere l'intera infrastruttura |
| **P2 — Urgente** | Amministratore applicazioni, accesso alla pipeline CI/CD, accesso in scrittura al codice sorgente, accesso al sistema di backup | Entro 1 ora | Può modificare i sistemi di produzione o esfiltrare PI |
| **P3 — Standard** | Account utente standard, e-mail, VPN, badge, condivisioni file | Per SLA del tipo di cessazione (vedere Tempistiche di revoca degli accessi) | Accesso standard con raggio d'azione limitato |

Per i licenziamenti immediati e i licenziamenti per giusta causa: P1 e P2 revocati prima o contemporaneamente alla notifica al dipendente ove operativamente fattibile.

**Processo automatizzato della lista di controllo di offboarding**:

1. **Generazione della lista di controllo**: Alla registrazione della cessazione in [Sistema HR], la lista di controllo di offboarding viene auto-generata dall'inventario autorevole di applicazioni e servizi, elencando ogni sistema in cui la persona in partenza detiene un account.
2. **Assegnazione**: Lista di controllo assegnata a IT Operations tramite [Strumento ITSM] con SLA basato sul tipo di cessazione.
3. **Verifica per sistema**: Ogni revoca di sistema viene singolarmente confermata dall'operatore (casella di controllo + timestamp). La verifica automatizzata è preferibile ove il [Fornitore di identità] fornisce la verifica dello stato dell'account tramite API.
4. **Escalation della lista di controllo incompleta**: Se un sistema rimane non revocato alla scadenza dell'SLA, lo [Strumento ITSM] esegue l'escalation automatica al Team Lead IAM e all'RSSI.
5. **Approvazione del completamento**: L'IT Operations Manager approva la lista di controllo completata. La lista di controllo viene conservata come prova (vedere tabella Prove).
6. **Traccia di audit**: Il timestamp di completamento della lista di controllo, il nome dell'operatore e i timestamp di revoca per sistema vengono registrati nello [Strumento ITSM] per il campionamento dell'audit SOC 2.

### Restituzione degli asset

L'organizzazione DEVE recuperare tutti gli asset organizzativi alla cessazione o al cambio del rapporto di lavoro.

**Asset fisici da restituire**:

- Laptop, computer desktop, monitor e periferiche.
- Dispositivi mobili (telefoni, tablet).
- Supporti di archiviazione (chiavette USB, dischi rigidi esterni).
- Badge di accesso, chiavi dell'ufficio, token di sicurezza e smart card.
- Documenti stampati, fascicoli e qualsiasi documento fisico.
- Carte di credito aziendali.

**Asset logici da affrontare**:

- Software concesso in licenza rimosso dai dispositivi personali (dove era autorizzato BYOD).
- Dati organizzativi sui dispositivi personali verificati come eliminati.
- Password degli account condivisi ruotate per le seguenti tempistiche a livelli:
  - **Licenziamento immediato / licenziamento per giusta causa**: Tutti gli account condivisi di cui l'individuo era a conoscenza ruotati entro 1 ora (contemporaneamente alla revoca dell'account individuale).
  - **Dimissioni volontarie / pensionamento / fine contratto**: Password degli account condivisi ruotate nell'ultimo giorno lavorativo, dopo il colloquio di uscita.
  - **Account di servizio con credenziali condivise**: Ruotati entro 4 ore dalla decisione di cessazione per gli account di servizio privilegiati; entro 24 ore per gli account di servizio standard.
  - **Credenziali dell'ambiente condiviso** (PSK Wi-Fi, codici porta, codici allarme): Ruotati entro 24 ore per i licenziamenti immediati; entro 5 giorni lavorativi per le partenze pianificate.
  - Tutte le rotazioni documentate nel record di offboarding con nome account, timestamp della rotazione e operatore.
- Token di autenticazione e certificati software revocati.

**Processo di restituzione degli asset** (6 fasi):

1. **Inventario**: IT genera un elenco di tutti gli asset assegnati alla persona in partenza dal registro degli asset.
2. **Notifica**: La persona in partenza riceve l'elenco degli asset e una data per l'appuntamento di restituzione.
3. **Raccolta**: Gli asset vengono restituiti all'IT all'appuntamento programmato (o spediti con consegna tracciata per i lavoratori a distanza).
4. **Verifica**: IT verifica tutti gli asset restituiti rispetto all'inventario. Le condizioni vengono documentate.
5. **Risoluzione delle lacune**: Gli asset mancanti o danneggiati vengono registrati. Gli asset mancanti vengono escalati al responsabile di linea e alle HR. Laddove gli asset non possano essere recuperati, viene elaborata una cancellazione per il processo di eccezione.
6. **Approvazione**: IT e HR approvano il modulo di restituzione degli asset. L'approvazione viene registrata in [Sistema HR] e [Strumento ITSM].

**Obiettivo**: Asset recuperati entro **5 giorni lavorativi** dall'ultimo giorno lavorativo (tasso di recupero >95%).

**Applicazione degli asset non restituiti** (per CO svizzero Art. 339a):

Laddove gli asset non vengano restituiti entro il target di 5 giorni lavorativi:

1. **Giorno 6**: IT Operations invia un promemoria scritto formale all'individuo (e-mail + lettera raccomandata) specificando gli elementi in sospeso e la scadenza di 5 giorni lavorativi.
2. **Giorno 11**: Le HR escalano al responsabile di linea. Secondo promemoria scritto inviato con riferimento all'obbligo contrattuale e alla potenziale detrazione salariale.
3. **Giorno 16**: HR + Consulente legale emettono una lettera di richiesta formale con riferimento al CO Art. 339a (restituzione reciproca dei beni) con scadenza finale di 10 giorni.
4. **Giorno 26**: Se ancora in sospeso, il Consulente legale valuta le opzioni di recupero: compensazione salariale rispetto al pagamento finale (consentita ai sensi del CO Art. 323b per le deduzioni concordate), azione civile o cancellazione con accettazione documentata del rischio.
5. **Cancellazione**: L'RSSI approva la cancellazione solo dopo aver confermato: esecuzione della cancellazione remota (se applicabile), cifratura del dispositivo confermata (se applicabile) e rischio residuo documentato nel registro delle eccezioni.

**Restituzione degli asset dei lavoratori a distanza**: Spedita tramite corriere tracciato a spese dell'organizzazione. Il corriere viene organizzato da IT Operations con un'etichetta di spedizione prepagata inviata all'individuo. Se non viene spedita entro 5 giorni lavorativi dal ricevimento dell'etichetta di spedizione, l'escalation segue i passaggi 1-5 sopra.

### Obblighi post-impiego

Gli obblighi continuativi DEVONO essere comunicati per iscritto alla persona in partenza prima o nell'ultimo giorno lavorativo:

**Riservatezza**:

- Gli obblighi NDA continuano per i termini dell'accordo firmato (vedere A.6.6 — Accordi di riservatezza e di non divulgazione). La durata dell'NDA è basata sul rischio in base alla classificazione delle informazioni:
  - **Segreti commerciali e algoritmi proprietari**: Indefinita (per CO svizzero Art. 321a).
  - **Informazioni riservate** (dati dei clienti, dati finanziari, architettura di sicurezza): 24 mesi dopo la partenza.
  - **Informazioni interne** (processi interni, dati organizzativi): 12 mesi dopo la partenza.
  - **Informazioni specifiche per cliente/contratto**: Per i termini del contratto del cliente (possono superare i periodi standard).
- I segreti commerciali e le informazioni proprietarie rimangono protetti **indefinitamente** ai sensi del CO svizzero Art. 321a (dovere di fedeltà) e della legge sui segreti commerciali applicabile.
- Le informazioni sui clienti rimangono riservate.
- Le informazioni classificate come Riservate o con Accesso limitato al momento della partenza rimangono soggette alle restrizioni di gestione.

**Restituzione e distruzione delle informazioni**:

- Tutte le informazioni organizzative in possesso dell'individuo DEVONO essere restituite o certificate come distrutte.
- Le copie personali dei dati organizzativi sono vietate.
- L'individuo DEVE confermare per iscritto che nessun dato organizzativo è stato conservato su dispositivi personali, archiviazione cloud personale o account e-mail personali.
- La verifica della restituzione o cancellazione dei dati DEVE utilizzare i seguenti metodi leciti e proporzionati al rischio:
  - **Auto-certificazione**: L'individuo completa una dichiarazione confermando la cancellazione di tutti i dati organizzativi dai dispositivi personali, dagli account e dall'archiviazione. Questo è il livello base per tutte le partenze.
  - **Verifica tecnica (dispositivi aziendali)**: IT esegue una scansione automatizzata dei dispositivi aziendali restituiti per verificare che non rimangano dati organizzativi. I risultati vengono documentati nel record di offboarding.
  - **Verifica tecnica (BYOD con MDM)**: Laddove l'individuo abbia utilizzato dispositivi personali iscritti a [MDM], l'organizzazione verifica il completamento della cancellazione selettiva avviata da MDM prima del disenrolment MDM.
  - **Verifica forense**: Solo laddove vi sia evidenza documentata di rischio di esfiltrazione dei dati (es. avvisi DLP, risultati delle indagini). Richiede l'approvazione del Consulente legale prima dell'avvio. Limitata ai dispositivi di proprietà aziendale e ai dispositivi iscritti a MDM. I dispositivi personali non sono soggetti a ispezione forense senza il consenso scritto dell'individuo e la guida del Consulente legale.
  - **Nessuna ispezione forzata dei dispositivi personali**: L'organizzazione NON DEVE imporre l'ispezione dei dispositivi personali senza il consenso dell'individuo. Laddove il consenso venga rifiutato e il rischio sia valutato come elevato, il Consulente legale DEVE fornire consulenza sulle misure disponibili ai sensi della legge svizzera.
- Tutto il lavoro creato durante il rapporto di lavoro appartiene all'organizzazione.

**Non concorrenza e non sollecitazione**: Ove applicabile, le clausole di non concorrenza o di non sollecitazione nel contratto di lavoro continuano per i loro termini, soggetti ai requisiti del CO svizzero Art. 340-340c (forma scritta, ambito ragionevole, compensazione ove richiesto).

### Colloquio di uscita

Un colloquio di uscita incentrato sulla sicurezza DEVE essere condotto per tutto il personale in partenza. Il colloquio DEVE coprire:

1. **Promemoria degli obblighi di riservatezza continuativi** — L'individuo viene ricordato del proprio NDA e di qualsiasi altro obbligo post-impiego.
2. **Riconoscimento dei termini NDA** — L'individuo conferma la comprensione e l'accettazione dei requisiti di riservatezza continuativi. Il riconoscimento viene documentato e firmato.
3. **Conferma della restituzione o cancellazione dei dati** — L'individuo conferma che tutti i dati organizzativi sono stati restituiti o eliminati dai dispositivi personali e dagli account.
4. **Identificazione delle questioni in sospeso** — Eventuali preoccupazioni di sicurezza irrisolte, problemi di accesso o elementi di passaggio di consegne vengono identificati e assegnati al responsabile appropriato.
5. **Documentazione finale** — Il modulo del colloquio di uscita viene completato e firmato da entrambe le parti. Una copia viene conservata nel fascicolo HR.

I colloqui di uscita DEVONO essere condotti dalle HR con il contributo del team di sicurezza delle informazioni laddove la persona in partenza abbia avuto accesso a dati Riservati o con Accesso limitato, abbia avuto accesso privilegiato ai sistemi, o stia partendo in circostanze disciplinari.

**Requisiti di tempistica del colloquio di uscita**:

| Tipo di cessazione | Tempistiche del colloquio | Note |
|--------------------|-----------------------------|------|
| **Dimissioni volontarie** | Durante il periodo di preavviso, minimo 3 giorni lavorativi prima dell'ultimo giorno | Consente tempo per affrontare le questioni in sospeso |
| **Licenziamento per giusta causa** | Nell'ultimo giorno lavorativo, prima della partenza | Combinato con l'appuntamento di restituzione degli asset |
| **Licenziamento immediato** | Entro 2 giorni lavorativi dal licenziamento, tramite telefono/video se di persona non è fattibile | L'individuo può rifiutare; il rifiuto viene documentato |
| **Pensionamento** | Durante l'ultimo mese di impiego | Può includere una discussione estesa sul passaggio di consegne |
| **Fine contratto** | Entro 5 giorni lavorativi prima della data di fine contratto | Programmato al punto di decisione del rinnovo del contratto |
| **Abbandono del posto di lavoro** | Questionario di uscita scritto inviato tramite posta raccomandata | L'individuo probabilmente non parteciperà; documentato come "non completato — abbandono" |

**Obiettivo**: Colloqui di uscita completati per il **100%** del personale in partenza (escluso l'abbandono del posto di lavoro dove l'individuo non è raggiungibile).

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **DRH / HR** | Proprietà del processo disciplinare; coordinamento del processo di uscita; conformità al diritto del lavoro; conduzione del colloquio di uscita; conservazione della documentazione |
| **RSSI** | Valutazione delle violazioni di sicurezza; verifica della revoca degli accessi; supporto forense; valutazione della notifica normativa; proprietà della policy |
| **Consulente legale** | Consulenza sulla conformità al diritto del lavoro; supporto al ricorso disciplinare; applicazione NDA; guida alla notifica normativa |
| **Responsabili di linea** | Avviare i rinvii disciplinari; coordinare il passaggio di consegne; verificare la restituzione degli asset; confermare la rimozione degli accessi per i cambi di ruolo |
| **IT Operations** | Esecuzione della revoca degli accessi; recupero e verifica degli asset; completamento della lista di controllo tecnica di offboarding |
| **Team IAM** | Disabilitazione degli account su tutti i sistemi; audit dell'accesso per completezza; monitoraggio degli account orfani |
| **Tutto il personale** | Segnalare le violazioni; rispettare le procedure di uscita; restituire gli asset; rispettare gli obblighi post-impiego |

**Percorso di escalation**:

- Questioni disciplinari: Responsabile di linea → HR → RSSI (se correlate alla sicurezza) → Consulente legale → Direzione generale.
- Problemi del processo di uscita: HR → IT Operations → RSSI.
- Restituzione degli asset in ritardo (>10 giorni lavorativi): IT Operations → HR → Consulente legale.

---

## Prove

Le seguenti prove dimostrano la conformità a questa policy:

| # | Prova | Responsabile | Frequenza |
|---|-------|--------------|-----------|
| 1 | **Registrazioni dei casi disciplinari** (anonimizzate) che mostrano il processo di indagine, la conformità alle garanzie procedurali e gli esiti. **Prontezza all'audit**: Ogni fascicolo del caso DEVE contenere un riepilogo strutturato (ID del caso, categoria di violazione, date dell'indagine, fasi delle garanzie procedurali completate, esito, stato del ricorso) adatto al campionamento dell'audit SOC 2 / ISO 27001 senza richiedere l'accesso al fascicolo HR riservato completo. | HR | *Per caso; conservati per i requisiti legali; verificati annualmente* |
| 2 | **Registri di revoca degli accessi** con timestamp che mostrano la data di cessazione rispetto alla data di revoca per sistema | Team IAM / IT Operations | *Per cessazione; rivisti mensilmente; obiettivo: 100% entro SLA* |
| 3 | **Registrazioni di restituzione degli asset** con documentazione di approvazione e riconciliazione dell'inventario | IT Operations | *Per cessazione; rivisto trimestralmente; obiettivo: >95% entro 5 giorni* |
| 4 | **Registrazioni del colloquio di uscita** che mostrano completamento, riconoscimento NDA e conferma della restituzione dei dati | HR | *Per cessazione; tasso di completamento monitorato mensilmente; obiettivo: 100%* |
| 5 | **Report degli account orfani** dalla riconciliazione periodica degli accessi | Team IAM | *Riconciliazione mensile; obiettivo: 0 account orfani dai dipendenti cessati* |

**Riconciliazione mensile degli account orfani**:

Il team IAM DEVE eseguire una riconciliazione mensile per rilevare e rimediare agli account orfani:

1. **Confronto delle fonti**: Confrontare gli account attivi nel [Fornitore di identità] e in tutte le applicazioni integrate con il registro HR del personale attivo.
2. **Rilevamento**: Qualsiasi account appartenente a una persona non nel registro attivo (cessata, contratto terminato, abbandonato) viene contrassegnato come potenzialmente orfano.
3. **Verifica**: Il team IAM verifica gli account contrassegnati rispetto ai record di offboarding. Account con offboarding completato ma ancora attivi = orfano confermato (rimediare immediatamente). Account senza record di offboarding = guasto del processo (escalare alle HR).
4. **Rimedio**: Account orfani confermati disabilitati entro 24 ore dal rilevamento. Causa radice documentata (es. sistema non incluso nella lista di controllo di offboarding, guasto del processo manuale, nuova applicazione non integrata con IdP).
5. **Reporting**: Conteggio mensile degli orfani segnalato all'RSSI. Tendenza monitorata trimestre per trimestre. Obiettivo: 0 account orfani. Qualsiasi orfano rilevato = non conformità registrata.
6. **Rimedio sistemico**: Laddove la stessa causa radice produca orfani in mesi consecutivi, è richiesta un'azione correttiva (es. aggiungere il sistema all'offboarding automatizzato, integrare l'applicazione con IdP).

| 6 | **Riconoscimenti degli obblighi post-impiego** (promemoria NDA firmati, conferme di restituzione dei dati) | HR | *Per cessazione; conservati per la durata NDA + 2 anni* |
| 7 | **Registrazioni di completamento della lista di controllo di offboarding** (verifica per sistema della revoca degli accessi) | IT Operations | *Per cessazione; conservati 3 anni* |
| 8 | **Voci del registro delle eccezioni** per violazioni degli SLA, cancellazioni degli asset e deviazioni del processo | RSSI / HR | *Per eccezione; rivisto trimestralmente* |
| 9 | **Registrazioni di formazione** per i responsabili sulle procedure disciplinari e sui processi di uscita | HR | *Annuale; obiettivo: 100% dei responsabili del personale formati* |
| 10 | **Risultati dell'audit trimestrale di conformità all'uscita** (revisione basata su campioni delle uscite completate) | Revisione interna / HR | *Trimestrale; presentato alla revisione della Direzione* |

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, tra cui: metriche di tempestività della revoca degli accessi, tassi di recupero degli asset, tassi di completamento del colloquio di uscita, monitoraggio degli account orfani, revisione dei casi disciplinari, audit interni ed esterni e feedback al proprietario della policy.

**Metriche di governance**:

| Metrica | Obiettivo | Frequenza di revisione |
|---------|-----------|------------------------|
| **Accesso revocato entro SLA** (per tipo di cessazione) | 100% | Mensile |
| **Asset recuperati entro 5 giorni lavorativi** | >95% | Trimestrale |
| **Colloqui di uscita completati** | 100% | Mensile |
| **Account orfani dai dipendenti cessati** | 0 | Mensile |
| **Restituzione degli asset in sospeso >30 giorni** | 0 | Mensile |
| **Casi disciplinari con garanzie procedurali documentate** | 100% | Annuale |
| **Riconoscimenti NDA post-impiego ottenuti** | 100% | Per cessazione |

Le metriche DEVONO essere riportate all'RSSI mensilmente e al team di revisione della Direzione trimestralmente.

## Eccezioni

Qualsiasi eccezione a questa policy DEVE essere approvata e registrata congiuntamente dall'RSSI e dal DRH, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni DEVONO essere riportate al team di revisione della Direzione.

**Eccezioni consentite**:

- Uscita accelerata con periodo di non operatività (garden leave) e revoca immediata degli accessi.
- Accesso esteso per un'esigenza aziendale documentata (a tempo limitato, massimo 10 giorni lavorativi, con controlli compensativi).
- Cancellazione degli asset per elementi persi o danneggiati dopo tentativi documentati di recupero.

**Non consentite**:

- Eccezioni permanenti alle tempistiche di revoca degli accessi.
- Eccezioni senza controlli compensativi.
- Rinuncia agli obblighi di riservatezza post-impiego.

## Non conformità

Un dipendente che violi questa policy può essere soggetto a provvedimenti disciplinari, fino al licenziamento. Anche i responsabili che non seguono le procedure di uscita richieste (es. notifica di offboarding ritardata, recupero degli asset incompleto) possono essere soggetti a provvedimenti disciplinari.

Ai sensi del CO svizzero Art. 337, il comportamento illecito grave che riguarda violazioni della sicurezza delle informazioni (es. furto di dati, sabotaggio, violazione deliberata della riservatezza) può costituire giusta causa per il licenziamento immediato senza preavviso. Le violazioni meno gravi ma ripetute possono giustificare il licenziamento per giusta causa a seguito di avvertimenti documentati per i requisiti dell'Art. 337.

## Miglioramento continuo

Questa policy viene rivista e aggiornata come parte del processo di miglioramento continuo. Le revisioni DEVONO tenere conto dei cambiamenti al diritto del lavoro svizzero, degli sviluppi normativi (nLPD, GDPR), delle lezioni apprese dai casi disciplinari e dai fallimenti del processo di uscita, dei risultati degli audit, dei cambiamenti al panorama tecnologico dell'organizzazione che influiscono sulle procedure di offboarding e delle best practice del settore per la gestione sicura del personale.

Le non conformità relative a questa policy (es. revoca degli accessi ritardata, asset non restituiti, processi di uscita incompleti, account orfani) DEVONO essere registrate e gestite attraverso il processo delle azioni correttive (ISO 27001 Clausola 10.2) con analisi della causa radice e rimedio monitorato.

---

# Aree dello standard ISO 27001 trattate

Policy sul processo disciplinare e la fine del rapporto di lavoro — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità della direzione |
| Clausola 5.3 Ruoli, responsabilità e autorità organizzative | 5.10 Uso accettabile delle informazioni e degli altri asset associati |
| Clausola 7.3 Consapevolezza | 5.11 Restituzione degli asset |
| Clausola 8.1 Pianificazione e controllo operativi | 6.2 Termini e condizioni del rapporto di lavoro |
| Clausola 10.2 Non conformità e azione correttiva | **6.4 Processo disciplinare** |
| | **6.5 Responsabilità dopo la fine o il cambio del rapporto di lavoro** |
| | 6.6 Accordi di riservatezza o di non divulgazione |

**Framework normativo e legale**:

| Framework | Rilevanza |
|-----------|-----------|
| CO svizzero Art. 328 | Obbligo di protezione del datore di lavoro — trattamento equo nei procedimenti disciplinari, protezione dei diritti della personalità del dipendente |
| CO svizzero Art. 337 | Licenziamento per giusta causa (fristlose Kündigung) — requisito di giusta causa per il licenziamento immediato, motivazione scritta su richiesta |
| CO svizzero Art. 337d | Abbandono del posto di lavoro — diritto del datore di lavoro a un risarcimento (1/4 del salario mensile), periodo di richiesta di 30 giorni |
| CO svizzero Art. 321a | Dovere di diligenza e fedeltà del dipendente — obbligo di proteggere i segreti commerciali, continua dopo il rapporto di lavoro |
| CO svizzero Art. 340-340c | Clausole di non concorrenza — requisiti di validità, limitazioni di ambito, compensazione ove richiesta |
| nLPD svizzera (revLPD) | Art. 8 — Misure tecniche e organizzative (revoca degli accessi come misura di sicurezza); Art. 24 — Notifica della violazione dei dati all'IFPDT |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento (misure di controllo degli accessi alla cessazione); Art. 33 — Notifica della violazione entro 72 ore |
| ISO/IEC 27001:2022 | Controlli A.6.4, A.6.5 dell'Allegato A |
| ISO/IEC 27002:2022 | Sezioni 6.4, 6.5 — Guida all'implementazione |
| NIST SP 800-53 Rev 5 | PS-4 (Cessazione del personale), PS-5 (Trasferimento del personale), PS-8 (Sanzioni al personale) |
| CIS Controls v8 | Controllo 6 (Gestione del controllo degli accessi — Salvaguardia 6.2: Stabilire un processo di revoca degli accessi) |

---

<!-- QA_VERIFIED: 2026-04-03 -->

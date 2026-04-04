<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.32-IT:operational:OP-POL:a.8.32 -->
**ISMS-OP-POL-A.8.32 — Gestione delle modifiche**

---

**Controllo del documento**

| Campo | Valore |
|-------|-------|
| **Titolo del documento** | Gestione delle modifiche |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.32 |
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

- ISO/IEC 27001:2022 Controllo A.8.32 — Gestione delle modifiche

**Controlli Annex A correlati**:

| Controllo | Relazione con la gestione delle modifiche |
|---------|-----------------------------------|
| A.5.9 Inventario delle informazioni e degli altri asset associati | L'inventario degli asset definisce l'ambito e la valutazione dell'impatto delle modifiche |
| A.5.24–28 Gestione degli incidenti | Le modifiche fallite possono attivare la risposta agli incidenti |
| A.5.37 Procedure operative documentate | Le procedure vengono aggiornate dopo le modifiche ai sistemi |
| A.8.8 Gestione delle vulnerabilità tecniche | Il rilascio delle patch segue il processo di gestione delle modifiche |
| A.8.9 Gestione della configurazione | Le configurazioni di base vengono aggiornate dopo le modifiche |
| A.8.19 Installazione di software sui sistemi operativi | Le installazioni di software seguono la gestione delle modifiche |
| A.8.25–29 Ciclo di vita dello sviluppo sicuro | Le modifiche di sviluppo seguono la gestione delle modifiche |
| A.8.31 Separazione degli ambienti | La promozione degli ambienti è controllata tramite il processo di modifica |
| A.8.33 Informazioni di test | I dati di test sono protetti durante il testing delle modifiche |

**Politiche interne correlate**:

- Politica di gestione degli asset
- Politica di gestione degli incidenti
- Politica delle procedure operative documentate
- Politica di sicurezza degli endpoint (gestione delle patch)
- Politica di sicurezza di rete

---

# Politica di gestione delle modifiche

## Scopo

Lo scopo di questa politica è gestire il rischio posto dalle modifiche ai sistemi di elaborazione delle informazioni, alle applicazioni, all'infrastruttura e alla tecnologia di supporto, garantendo che le modifiche siano pianificate, valutate, approvate, testate, implementate e documentate in modo controllato.

Questa politica supporta la nLPD svizzera (revDSG) e l'Ordinanza sulla protezione dei dati (OPDo) implementando misure tecniche e organizzative appropriate al rischio, garantendo che le modifiche ai sistemi che trattano dati personali non compromettano le garanzie di protezione dei dati. Dove l'organizzazione tratta dati di individui nell'UE/SEE, si applicano anche i requisiti del GDPR.

## Ambito

Tutti i dipendenti e gli utenti terzi.

Tutte le modifiche ai sistemi di elaborazione delle informazioni, alle applicazioni, all'infrastruttura, alle apparecchiature di rete, ai servizi cloud e ai sistemi di supporto indipendentemente dal modello di distribuzione (on-premises, cloud, ibrido).

Ciò include modifiche hardware, modifiche software, modifiche di configurazione, modifiche infrastrutturali, modifiche agli schemi dei dati e modifiche ai sistemi di sicurezza.

**Fuori ambito**: Aggiornamenti dei contenuti del sito web (testi, immagini), azioni self-service degli utenti (reimpostazione della password tramite portale approvato), operazioni automatizzate di routine (backup pianificati, rotazione dei log) e modifiche gestite interamente dai fornitori SaaS al di fuori del controllo del cliente.

## Principio

Tutte le modifiche ai sistemi di elaborazione delle informazioni devono essere soggette a procedure formali di gestione delle modifiche. Le modifiche devono essere pianificate, valutate per impatto e rischio, autorizzate, testate, comunicate, implementate in modo controllato e documentate. Le modifiche d'emergenza devono seguire procedure accelerate mantenendo al contempo il controllo e la supervisione.

---

## Definizioni

| Termine | Definizione |
|------|------------|
| **Modifica** | Qualsiasi aggiunta, modifica o rimozione di componenti del sistema informativo (hardware, software, configurazione, dati) che potrebbe influenzare la sicurezza delle informazioni o la disponibilità del sistema |
| **Modifica standard** | Modifica a basso rischio, pre-approvata e di routine che segue una procedura documentata del Catalogo delle modifiche standard |
| **Modifica normale** | Modifica che richiede una valutazione completa, revisione del CAB e flusso di approvazione standard |
| **Modifica d'emergenza** | Modifica che richiede un'implementazione accelerata per risolvere un incidente critico, una vulnerabilità attiva o prevenire un impatto aziendale significativo |
| **Comitato consultivo per le modifiche (CAB)** | Gruppo multidisciplinare che fornisce revisione specialistica, valutazione dell'impatto e raccomandazioni per le modifiche |
| **Revisione post-implementazione (PIR)** | Revisione strutturata dopo l'implementazione della modifica che verifica il raggiungimento degli obiettivi e acquisisce le lezioni apprese |
| **Modifica fallita** | Modifica che viene annullata a causa del mancato raggiungimento degli obiettivi, di un degrado delle prestazioni inaccettabile, dell'introduzione di una vulnerabilità della sicurezza o del deterioramento di funzioni aziendali critiche. Una modifica che richiede correzioni post-implementazione non è necessariamente "fallita" se la modifica originale non è stata annullata |

---

## Classificazione delle modifiche

Tutte le modifiche devono essere classificate in una delle tre categorie:

| Tipo | Livello di rischio | Approvazione | Revisione CAB | Testing |
|------|-----------|----------|------------|---------|
| **Standard** | Basso | Pre-approvata (catalogo) | Non richiesta | Per procedura del catalogo |
| **Normale** | Medio–Alto | Proprietario del servizio / CAB / RSSI (basato sul rischio) | Richiesta per alto rischio | Testing in ambiente non di produzione richiesto |
| **Emergenza** | Critico | RSSI o Responsabile delle operazioni IT | Retrospettiva (entro 48 ore) | Appropriato al rischio (può essere abbreviato) |

Le modifiche che rientrano in aree grigie devono essere escalate al Change Manager per la classificazione.

---

## Processo di richiesta di modifica

### Invio della richiesta di modifica

Tutte le modifiche nell'ambito devono essere inviate come richieste di modifica formali nel sistema di gestione delle modifiche: **[Specificare: ServiceNow, Jira Service Management, Azure DevOps, o "In selezione; interim: sistema di ticketing/foglio di calcolo"]**.

**Accesso al sistema**: L'invio delle modifiche è disponibile per tutto il personale IT; l'approvazione delle modifiche e il coordinamento del CAB sono limitati al personale autorizzato.

**Formato ID modifica**: [Specificare: MOD-AAAAMMGG-### o generato automaticamente dal sistema].

Ogni richiesta di modifica deve includere, come minimo:

| Campo | Descrizione |
|-------|-------------|
| ID modifica | Identificatore univoco assegnato dal sistema |
| Descrizione | Cosa viene modificato e perché |
| Giustificazione aziendale | Motivo della modifica |
| Sistemi interessati | Asset, servizi e dipendenze impattate |
| Classificazione del rischio | Basso / Medio / Alto / Critico |
| Piano di implementazione | Procedura passo-passo |
| Finestra di implementazione | Data, ora e durata proposta |
| Piano di rollback | Come annullare la modifica in caso di fallimento |
| Approccio al testing | Quali test verranno eseguiti |
| Richiedente e responsabile dell'implementazione | Chi ha richiesto e chi eseguirà |
| Piano di comunicazione | Chi deve essere informato |

### Valutazione dell'impatto e del rischio

Tutte le modifiche devono essere valutate per l'impatto prima dell'implementazione:

- **Impatto tecnico**: Sistemi interessati, dipendenze, punti di integrazione.
- **Impatto aziendale**: Servizi interessati, impatto sugli utenti, interruzione delle operazioni aziendali.
- **Impatto sulla sicurezza**: Rischi per la riservatezza, l'integrità, la disponibilità. Le modifiche che interessano sistemi che trattano dati personali devono includere una valutazione dell'impatto sulla protezione dei dati.
- **Impatto sulla conformità**: Obblighi normativi, controlli di audit.
- **Livello di rischio**: Combinazione della probabilità di fallimento e dell'entità dell'impatto.

### Flusso di approvazione

L'autorità di approvazione deve basarsi sul livello di rischio della modifica:

| Livello di rischio | Autorità di approvazione |
|------------|-------------------|
| **Basso** (Modifica standard) | Pre-approvata tramite il Catalogo delle modifiche standard |
| **Medio** | Proprietario del servizio o Team Lead |
| **Alto** | Responsabile delle operazioni IT e RSSI |
| **Critico** | Direzione generale |

---

## Comitato consultivo per le modifiche (CAB)

L'organizzazione deve istituire un Comitato consultivo per le modifiche per la revisione delle modifiche normali e d'emergenza.

### Composizione del CAB

| Ruolo | Responsabilità |
|------|---------------|
| **Change Manager** (Presidente) | Proprietà del processo, pianificazione, metriche, miglioramento continuo |
| **Rappresentante delle operazioni IT** | Fattibilità tecnica, impatto sull'infrastruttura |
| **Rappresentante della sicurezza** | Valutazione del rischio per la sicurezza, impatto sulla conformità |
| **Proprietari delle applicazioni aziendali** | Valutazione dell'impatto aziendale (per le modifiche rilevanti) |
| **Esperti in materia** | Competenze tecniche secondo necessità |

### Operazioni del CAB

- **Riunioni regolari**: **[Specificare: Settimanalmente il [giorno] alle [ora] CET]** (o appropriato al volume delle modifiche).
- **Formato delle riunioni**: [In persona / virtuale / ibrido].
- **Agenda pubblicata**: 24 ore prima della riunione (le richieste di modifica devono essere inviate entro il [giorno prima] alle 17:00 per il CAB del [giorno della riunione]).
- **CAB d'emergenza**: Convocato secondo necessità per le modifiche urgenti tramite [email/Teams/Slack]; può procedere con quorum ridotto (Change Manager + un membro aggiuntivo) con revisione retrospettiva completa del CAB entro **48 ore**.
- **Quorum**: Change Manager, Rappresentante delle operazioni IT, Rappresentante della sicurezza e almeno un membro aggiuntivo.
- **Verbali**: I verbali delle riunioni devono essere mantenuti per tutte le riunioni del CAB, documentando data, partecipanti, modifiche revisionate, decisioni, motivazioni e punti d'azione. I verbali vengono conservati per **3 anni**.

---

## Catalogo delle modifiche standard

L'organizzazione deve mantenere un Catalogo delle modifiche standard contenente modifiche pre-approvate, a basso rischio e di routine.

### Requisiti del catalogo

Ogni voce del catalogo deve includere:

- Descrizione e ambito della modifica.
- Condizioni preliminari e prerequisiti.
- Procedura passo-passo.
- Durata stimata.
- Procedura di rollback (se applicabile).
- Valutazione del rischio (completata una volta durante l'approvazione del catalogo).

### Governance del catalogo

- Il catalogo viene revisionato **trimestralmente** dal Change Manager con il contributo del CAB.
- Nuove voci vengono aggiunte da modifiche normali riuscite che sono ripetibili e a basso rischio.
- Le voci vengono rimosse o riclassificate dopo qualsiasi fallimento di una modifica standard.
- Obiettivo di tasso di successo: **>95%** per le modifiche standard.

Le modifiche standard devono comunque essere registrate nel sistema di gestione delle modifiche a fini di audit trail e correlazione con gli incidenti, anche se la revisione del CAB non è richiesta.

### Esempi di Catalogo delle modifiche standard

Le modifiche standard pre-approvate tipiche includono:

| Modifica | Riferimento procedura | Durata stimata | Prerequisiti |
|--------|--------------------|--------------------|---------------|
| Aggiunta utente al gruppo Active Directory | IT-SOP-001 | 5 minuti | Ticket di richiesta di accesso approvato |
| Riavvio del server applicativo (non di produzione) | IT-SOP-015 | 10 minuti | Notifica al proprietario del servizio |
| Rinnovo del certificato SSL | IT-SOP-023 | 30 minuti | Nuovo certificato ottenuto, backup del certificato precedente |
| Aggiunta di record DNS (dominio interno) | IT-SOP-031 | 10 minuti | Modulo di richiesta di modifica DNS compilato |
| Regola del firewall per applicazione approvata | IT-SOP-045 | 15 minuti | Pre-approvazione del team di sicurezza, regola documentata |

**Non sono modifiche standard**: Modifiche agli schemi del database, aggiornamenti del sistema operativo, modifiche alla topologia di rete, nuove installazioni di software, modifiche alla configurazione della sicurezza che interessano la produzione.

---

## Testing e validazione

### Requisiti di testing

Le modifiche devono essere testate prima del rilascio in produzione:

| Rischio della modifica | Testing richiesto |
|-------------|-----------------|
| **Basso** (Standard) | Per procedura del catalogo; verifica da parte del responsabile dell'implementazione |
| **Medio** | Test funzionali e test di integrazione in ambiente non di produzione |
| **Alto** | Test funzionali, di integrazione, delle prestazioni e di accettazione utente |
| **Critico** | Suite di test completa inclusi test di sicurezza e validazione del ripristino di emergenza |

### Separazione degli ambienti

- Le modifiche devono essere testate in ambienti non di produzione (sviluppo, test/QA, staging) prima del rilascio in produzione.
- Gli ambienti non di produzione devono essere logicamente o fisicamente separati dalla produzione con credenziali e controlli di accesso separati.
- I dati di produzione non devono essere utilizzati negli ambienti di test senza mascheratura o anonimizzazione ai sensi della Politica di classificazione e gestione delle informazioni.
- La promozione dal test alla produzione richiede un'approvazione formale e risultati di test verificati.

### Protezione dell'ambiente di produzione

Le modifiche alla produzione devono essere eseguite solo da personale autorizzato con i seguenti controlli:

- **Separazione dei compiti**: Gli sviluppatori non devono rilasciare le proprie modifiche in produzione senza revisione indipendente e approvazione da parte di un release manager designato, di un membro del team delle operazioni o del CAB.
- **Revisione tra pari**: Le modifiche al codice richiedono la revisione e l'approvazione tra pari prima del rilascio in produzione (tramite pull request o meccanismo equivalente).
- **L'autenticazione a più fattori (AMF)** deve essere richiesta per l'accesso alla produzione.
- **Gestione degli accessi privilegiati**: Gli account di rilascio in produzione devono essere separati dagli account di sviluppo.
- **Tutte le modifiche alla produzione devono essere registrate nel log di audit** con identità dell'utente, timestamp e contenuto della modifica.

**Eccezione**: Nelle organizzazioni con meno di 5 dipendenti IT dove la separazione completa non è fattibile, i controlli compensativi devono includere registrazione avanzata, revisione del RSSI di tutte le modifiche alla produzione mensilmente e revisione tra pari post-implementazione.

---

## Implementazione e rollback

### Implementazione controllata

Le modifiche devono essere implementate seguendo il piano di implementazione approvato con:

- Verifica dei prerequisiti e delle dipendenze prima di iniziare.
- Esecuzione dei passaggi documentati.
- Monitoraggio in tempo reale durante l'implementazione.
- Test di verifica post-implementazione.
- Documentazione dei passaggi effettivamente eseguiti e di eventuali deviazioni.

### Finestre di manutenzione

L'organizzazione deve stabilire finestre di modifica preferite per minimizzare le interruzioni aziendali:

**Finestre di modifica preferite**:
- **Finestra standard**: [Specificare: ad es. Martedì e giovedì 20:00–23:00 CET]
- **Finestra estesa**: [Specificare: ad es. Sabato 08:00–16:00 CET]
- **Emergenza**: In qualsiasi momento con approvazione del RSSI

**Periodi di blocco delle modifiche** (nessuna modifica non d'emergenza):
- [Specifici per l'azienda: ad es. "Prima settimana di ogni mese (chiusura finanziaria)", "15 dicembre–5 gennaio (blocco di fine anno)"]
- Giorni festivi: festività federali svizzere
- Principali eventi aziendali: documentati nel calendario delle modifiche con 90 giorni di anticipo

Le modifiche al di fuori delle finestre preferite richiedono l'**autorità di approvazione per Alto rischio** (Responsabile delle operazioni IT + RSSI) indipendentemente dal livello di rischio tecnico.

### Rollback

Una procedura di rollback deve essere concordata prima di implementare modifiche ai sistemi di produzione. Il rollback deve essere eseguito quando:

- La modifica non raggiunge i propri obiettivi.
- Si verifica un degrado delle prestazioni inaccettabile.
- Viene introdotta una vulnerabilità della sicurezza.
- Le funzioni aziendali critiche sono compromesse.

Autorità di decisione per il rollback: stessa autorità di approvazione della modifica originale (o superiore per il rollback d'emergenza).

### Testing del rollback

Per le modifiche ad **Alto** e **Critico** rischio, le procedure di rollback devono essere:

- Documentate e approvate come parte della richiesta di modifica.
- **Testate in ambienti non di produzione** prima dell'implementazione in produzione (dove fattibile).
- Verificate come eseguibili entro la finestra di rollback definita.

Il testing del rollback deve verificare:

- I passaggi della procedura di rollback sono accurati e completi.
- Il rollback può essere completato entro la finestra di modifica.
- L'integrità dei dati viene mantenuta durante il rollback.
- Il ripristino del servizio è confermato.

Dove il testing del rollback non è fattibile (migrazioni unidirezionali, modifiche distruttive), un piano di **forward-fix** deve essere documentato come alternativa al rollback.

---

## Comunicazione

### Notifica agli stakeholder

Gli stakeholder interessati devono essere notificati delle modifiche, inclusi:

- Programma e tempistiche della modifica.
- Impatto previsto sul servizio (durata, ambito).
- Azioni richieste agli utenti (se necessarie).
- Informazioni di contatto per il supporto durante la modifica.

**Modifiche pianificate**: Notifica minima anticipata per i requisiti organizzativi (raccomandato: 5 giorni lavorativi per alto impatto, 2 giorni lavorativi per impatto medio).

**Modifiche d'emergenza**: Comunicazione non appena possibile in modo sicuro.

**Completamento della modifica**: Conferma inviata agli stakeholder quando la modifica è completata.

---

## Modifiche d'emergenza

### Criteri di classificazione d'emergenza

Le modifiche devono essere classificate come d'emergenza solo quando:

- Si risolve un incidente di sicurezza attivo o una vulnerabilità attivamente sfruttata.
- Si ripristina un'interruzione di un servizio critico.
- Si previene un imminente guasto del sistema.
- Si risponde a un requisito normativo urgente.
- Si mitiga una violazione dei dati attiva.

La classificazione d'emergenza **non** deve essere utilizzata per comodità, scarsa pianificazione, lavoro di routine o funzionalità desiderate.

### Processo di modifica d'emergenza

1. Giustificazione dell'emergenza documentata (anche se breve).
2. Approvazione del RSSI o del Responsabile delle operazioni IT (minimo).
3. Testing appropriato al rischio (casi di test abbreviati, o accettazione documentata del rischio se il testing non è fattibile).
4. Implementazione con monitoraggio avanzato.
5. Piano di rollback in atto prima dell'esecuzione.
6. Revisione retrospettiva del CAB entro **48 ore**.
7. Revisione post-implementazione (PIR) obbligatoria entro **5 giorni lavorativi**.

### Monitoraggio delle modifiche d'emergenza

La percentuale di modifiche d'emergenza deve essere monitorata mensilmente. Obiettivo: **<5%** di tutte le modifiche.

Quando le modifiche d'emergenza superano il 5% per due mesi consecutivi:

1. Analisi della causa principale condotta dal Change Manager entro **14 giorni**.
2. Risultati presentati al CAB e al RSSI.
3. Azioni di remediation implementate entro **30 giorni**, che possono includere: formazione aggiuntiva sulla classificazione delle modifiche, miglioramenti del processo (ad es. flussi di approvazione più rapidi per le modifiche urgenti ma non d'emergenza), aggiustamenti delle risorse o azioni disciplinari per l'abuso della classificazione d'emergenza.
4. Revisione di follow-up dopo **60 giorni** per verificare l'efficacia.

**Abuso della classificazione d'emergenza**: L'utilizzo inappropriato della classificazione d'emergenza (comodità, scarsa pianificazione) costituisce non conformità alla politica e deve essere escalato al RSSI.

---

## Revisione post-implementazione (PIR)

Le revisioni post-implementazione devono essere condotte per:

- **Tutte le modifiche d'emergenza** (obbligatorie).
- **Tutte le modifiche fallite** (obbligatorie).
- **Modifiche normali classificate ad alto rischio o critiche**.

### Contenuto della PIR

- Obiettivi raggiunti rispetto ai risultati pianificati.
- Problemi riscontrati durante l'implementazione.
- Efficacia della pianificazione e del testing.
- Feedback degli utenti e impatto sul servizio.
- Lezioni apprese e opportunità di miglioramento.
- Se la modifica debba essere aggiunta al Catalogo delle modifiche standard.

### Tempistica della PIR

- Modifiche d'emergenza: entro **5 giorni lavorativi**.
- Modifiche fallite: entro **5 giorni lavorativi**.
- Modifiche normali ad alto rischio: entro **14 giorni lavorativi**.

---

## Periodi di blocco delle modifiche

In momenti critici dell'anno, l'organizzazione può imporre un periodo di blocco delle modifiche durante il quale sono consentite solo le modifiche d'emergenza.

I periodi di blocco delle modifiche devono essere:

- Approvati dalla direzione generale o dal RSSI.
- Comunicati a tutti gli stakeholder in anticipo (minimo 2 settimane).
- Documentati nel calendario delle modifiche.
- Esempi: chiusura finanziaria di fine anno, principali lanci di prodotti, stagioni di picco aziendale, periodi di invio normativo.

---

## Tenuta dei registri e documentazione

### Registri delle modifiche

I registri completi delle modifiche devono essere mantenuti includendo:

- Tutte le informazioni sulla richiesta di modifica.
- Registri delle approvazioni con timestamp e approvatori.
- Note e raccomandazioni della revisione del CAB.
- Log di implementazione e risultati di verifica.
- Registri delle comunicazioni.
- Problemi o incidenti durante l'implementazione.
- Decisioni di rollback ed esecuzione (se applicabile).
- Risultati della revisione post-implementazione.

I registri delle modifiche devono essere conservati per un minimo di **3 anni** per riferimento operativo e **7 anni** per prove di audit.

### Aggiornamenti della documentazione

Dopo le modifiche ai sistemi, la seguente documentazione deve essere aggiornata entro **5 giorni lavorativi**:

- Documentazione della configurazione del sistema.
- Diagrammi di rete e topologia.
- Procedure operative e runbook.
- Procedure di ripristino di emergenza (dove la modifica riguarda sistemi critici o RTO/RPO).

---

## Integrazione con la gestione della configurazione

La gestione delle modifiche e la gestione della configurazione sono discipline complementari:

- La **gestione delle modifiche** controlla *come* vengono apportate le modifiche (approvazione, testing, implementazione).
- La **gestione della configurazione** controlla *quale* è lo stato attuale (configurazioni di base, versioni, elementi di configurazione).

**Punti di integrazione**:

- Le configurazioni di base devono essere aggiornate dopo le modifiche approvate.
- Il rilevamento della deriva della configurazione (effettiva rispetto alla baseline) deve attivare un'indagine e una richiesta di modifica correttiva.
- Il database di gestione della configurazione (CMDB) o l'inventario equivalente deve essere la fonte autorevole per la valutazione dell'impatto (quali sistemi sono interessati).

Vedere la **Politica di gestione della configurazione (A.8.9)** per i requisiti dettagliati sulla baseline e il controllo versione.

---

## Modifiche non autorizzate

Le modifiche non autorizzate — modifiche apportate senza seguire il processo di gestione delle modifiche — devono essere:

- Rilevate tramite monitoraggio, registrazione degli audit e strumenti di gestione della configurazione.
- Investigate per determinare la causa principale e l'impatto.
- Segnalate al RSSI e escalate al Team di revisione della direzione.
- Soggette ad azioni correttive, che possono includere azioni disciplinari ai sensi del processo disciplinare dell'organizzazione.

---

## Correlazione modifiche-incidenti

Quando si verifica un incidente di sicurezza o un'interruzione del servizio, il Change Manager deve:

1. **Rivedere le modifiche recenti** nelle 48 ore precedenti all'inizio dell'incidente.
2. **Correlare la cronologia dell'incidente** con i timestamp di implementazione delle modifiche.
3. **Identificare le modifiche potenzialmente correlate** (stessi sistemi, dipendenze, periodo di tempo).
4. **Escalare al CAB e al RSSI** se si sospetta una modifica come causa principale.

Dove una modifica è confermata come causa principale di un incidente:

- **Revisione post-implementazione obbligatoria** entro **3 giorni lavorativi**.
- **Analisi della causa principale** per identificare le lacune del processo (testing inadeguato, valutazione dell'impatto mancata, approvazione insufficiente).
- **Azioni correttive** per prevenire il ripetersi.
- Se la modifica era nel Catalogo delle modifiche standard, la voce del catalogo deve essere revisionata e potenzialmente riclassificata o rimossa.

Il tasso di incidenti correlati alle modifiche viene monitorato come metrica chiave (obiettivo: 0 per trimestre).

---

## Metriche di gestione delle modifiche

Il team di gestione della sicurezza delle informazioni deve segnalare le metriche di gestione delle modifiche al RSSI almeno trimestralmente:

| Metrica | Obiettivo | Soglia critica |
|--------|--------|---------------|
| Tasso di successo delle modifiche (modifiche completate senza rollback o incidente) | ≥95% | <85% |
| Percentuale di modifiche d'emergenza | <5% | >10% |
| Tasso di completamento della PIR (per le PIR obbligatorie) | 100% | <80% |
| Utilizzo del Catalogo delle modifiche standard | ≥30% di tutte le modifiche | <15% |
| Incidenti correlati alle modifiche | 0 | >2 per trimestre |
| Modifiche in ritardo (oltre la data di implementazione pianificata) | 0 | >5 |
| Conformità all'aggiornamento della documentazione (entro 5 giorni lavorativi) | ≥95% | <80% |

Le metriche che superano le soglie critiche devono essere escalate al RSSI per attenzione immediata e segnalate nella successiva revisione della direzione.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|------|-----------------|
| **RSSI** | Proprietà della politica; approvazione delle modifiche ad alto rischio e d'emergenza; autorizzazione delle eccezioni; revisione delle metriche |
| **Change Manager** | Proprietà del processo; presidenza del CAB; manutenzione del Catalogo delle modifiche standard; monitoraggio delle metriche; miglioramento continuo |
| **Responsabile delle operazioni IT** | Approvazione delle modifiche a medio/alto rischio; presidenza del CAB d'emergenza; coordinamento della finestra di modifica |
| **Membri del CAB** | Revisione delle modifiche, valutazione dell'impatto, identificazione dei rischi, raccomandazioni di approvazione |
| **Richiedenti delle modifiche** | Invio di richieste di modifica complete con giustificazione aziendale e valutazione dell'impatto |
| **Responsabili dell'implementazione delle modifiche** | Esecuzione delle modifiche approvate seguendo le procedure documentate; esecuzione dei test di verifica |
| **Proprietari dei sistemi** | Approvazione delle modifiche ai sistemi di proprietà; fornitura della valutazione dell'impatto; responsabilità della disponibilità del sistema |

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa politica:

| # | Evidenza | Proprietario | Frequenza |
|---|----------|-------|-----------|
| 1 | **Registri del sistema di gestione delle modifiche** (tutte le richieste di modifica con i campi richiesti) | Change Manager | *Per evento; auditato trimestralmente* |
| 2 | **Verbali delle riunioni del CAB** (partecipanti, decisioni, motivazioni, punti d'azione) | Change Manager | *Per riunione; conservati 3 anni* |
| 3 | **Catalogo delle modifiche standard** con cronologia delle versioni e registri di revisione trimestrale | Change Manager | *Revisionato trimestralmente; sotto controllo versione* |
| 4 | **Calendario delle modifiche** con periodi di blocco e modifiche pianificate | Change Manager | *Mantenuto continuamente; revisionato mensilmente* |
| 5 | **Registri della revisione post-implementazione** per le modifiche d'emergenza, fallite e ad alto rischio | Change Manager | *Per modifica qualificante; obiettivo: 100% di completamento* |
| 6 | **Registri delle approvazioni** con timestamp che mostrano l'autorità appropriata per livello di rischio | Change Manager | *Per modifica; conservati 7 anni* |
| 7 | **Registri del testing** (piani di test, risultati, approvazioni) per le modifiche normali e ad alto rischio | Operazioni IT | *Per modifica; conservati 3 anni* |
| 8 | **Giustificazione della modifica d'emergenza** e registri di revisione retrospettiva del CAB | RSSI | *Per modifica d'emergenza; revisionato mensilmente* |
| 9 | **Rapporti delle metriche di gestione delle modifiche** | Change Manager | *Trimestrale; presentato alla revisione della direzione* |
| 10 | **Indagini sulle modifiche non autorizzate** e registri delle azioni correttive | RSSI | *Per evento; conservati 3 anni* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui audit dei registri delle modifiche, revisioni delle riunioni del CAB, monitoraggio del completamento delle PIR, analisi delle modifiche d'emergenza, audit interni ed esterni, e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita. Le eccezioni devono essere segnalate al Team di revisione della direzione.

## Non conformità

Un dipendente che viola questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa politica viene revisionata e aggiornata come parte del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti agli standard di gestione delle modifiche, le modifiche tecnologiche, i rischi emergenti, le modifiche normative, i risultati delle PIR e le lezioni apprese dagli incidenti correlati alle modifiche.

---

# Aree della norma ISO 27001 affrontate

Politica di gestione delle modifiche — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 6.3 Pianificazione delle modifiche | 5.37 Procedure operative documentate |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| Clausola 8.1 Pianificazione e controllo operativi | 6.4 Processo disciplinare |
| | **8.32 Gestione delle modifiche** |
| | 8.9 Gestione della configurazione |
| | 8.19 Installazione di software sui sistemi operativi |

**Quadro normativo e legale**:

| Quadro | Pertinenza |
|-----------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative (la gestione delle modifiche come misura organizzativa a protezione dei sistemi di elaborazione dei dati) |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento (la gestione delle modifiche come misura appropriata) |
| ISO/IEC 27001:2022 | Controllo Annex A 8.32 — Gestione delle modifiche |
| ISO/IEC 27002:2022 | Sezione 8.32 — Linee guida di implementazione (9 elementi obbligatori) |
| NIST SP 800-53 Rev 5 | CM-3 (Controllo delle modifiche alla configurazione), CM-4 (Analisi dell'impatto), CM-5 (Restrizioni di accesso per le modifiche) |
| CIS Controls v8 | Controllo 2 (Inventario e controllo degli asset software — Salvaguardia 2.5: Allowlist del software autorizzato) |

---

<!-- QA_VERIFIED: 2026-04-03 -->

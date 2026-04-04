<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.24-28-IT:operational:OP-POL:a.5.24-28 -->
**ISMS-OP-POL-A.5.24-28 — Gestione degli incidenti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Gestione degli incidenti |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.24-28 |
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

- Controlli ISO/IEC 27001:2022 A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 — Pianificazione, valutazione, risposta, apprendimento e raccolta delle prove nella gestione degli incidenti di sicurezza delle informazioni

**Controlli Annex A correlati**:

| Controllo | Relazione con la gestione degli incidenti |
|-----------|------------------------------------------|
| A.5.5–6 Contatti con autorità e gruppi di interesse | Obblighi di segnalazione esterna (IFPDT, forze dell'ordine, CERT) |
| A.5.7 Intelligence sulle minacce | L'intelligence sulle minacce informa il rilevamento e la risposta agli incidenti |
| A.5.29 Sicurezza delle informazioni durante le interruzioni | Attivazione della continuità operativa durante gli incidenti gravi |
| A.5.34 Privacy e protezione dei dati personali | Requisiti di notifica delle violazioni di dati personali |
| A.6.8 Segnalazione degli eventi di sicurezza delle informazioni | La segnalazione da parte degli utenti alimenta il triage degli incidenti |
| A.8.15 Logging | I dati di log supportano il rilevamento degli incidenti e l'analisi forense |
| A.8.16 Attività di monitoraggio | Il monitoraggio rileva gli eventi di sicurezza per il triage degli incidenti |

**Policy interne correlate**:

- Policy di controllo degli accessi
- Policy di logging
- Policy sulle attività di monitoraggio (A.8.16)
- Policy di continuità operativa
- Policy sulla privacy e protezione dei dati personali
- Policy di classificazione e gestione delle informazioni

---

# Policy di gestione degli incidenti

## Scopo

Questa policy fornisce indicazioni sulla gestione degli incidenti di sicurezza delle informazioni in modo strutturato, inclusa l'identificazione, la valutazione, la risposta e la risoluzione degli eventi e degli incidenti di sicurezza, nonché l'identificazione, la raccolta, l'acquisizione e la conservazione delle informazioni che possono fungere da prove.

Questa policy supporta la nLPD svizzera (revDSG) e l'Ordinanza sulla protezione dei dati (OPDo) implementando procedure di notifica delle violazioni e misure tecniche e organizzative proporzionate al rischio. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutti i sistemi informativi, le applicazioni e i servizi inclusi nell'ambito della dichiarazione di scopo ISO 27001.

## Principio

Tutti gli eventi di sicurezza delle informazioni DEVONO essere segnalati e valutati. Gli incidenti confermati DEVONO essere gestiti attraverso un processo di risposta strutturato con ruoli definiti, percorsi di escalation e procedure di comunicazione. L'organizzazione DEVE imparare dagli incidenti per migliorare la propria postura di sicurezza. Laddove gli incidenti possano portare a indagini esterne o procedimenti legali, DEVONO essere coinvolte risorse esterne specializzate.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Evento di sicurezza** | Un'occorrenza identificata che indica una possibile violazione della policy di sicurezza o un guasto dei controlli. Non tutti gli eventi sono incidenti. |
| **Incidente di sicurezza** | Un evento di sicurezza che è stato valutato e confermato come avente un effetto negativo reale o potenziale sulla riservatezza, integrità o disponibilità delle informazioni. |
| **Violazione di dati personali** | Un incidente di sicurezza che comporta la distruzione accidentale o illegittima, la perdita, la modifica, la divulgazione non autorizzata o l'accesso non autorizzato a dati personali. |
| **Incidente significativo** | Un incidente che costituisce una violazione legale o normativa, potrebbe portare a un'indagine esterna o a procedimenti legali, oppure crea un rischio elevato per gli interessati. |

---

## Segnalazione degli incidenti

Tutti i dipendenti e gli utenti terzi DEVONO segnalare immediatamente gli eventi di sicurezza al momento della scoperta al team di gestione della sicurezza delle informazioni attraverso i canali di segnalazione designati:

- **Principale**: Service desk IT (email, telefono o sistema di ticketing).
- **Alternativo**: Contatto diretto con il team di gestione della sicurezza delle informazioni (lista di distribuzione email o telefono).
- **Fuori orario**: Contatto di sicurezza di turno (telefono o messaggistica).
- **Anonimo**: Laddove i dipendenti desiderino segnalare preoccupazioni in modo anonimo, le segnalazioni possono essere inviate tramite il meccanismo di whistleblowing o di segnalazione etica dell'organizzazione.

I canali di segnalazione DEVONO essere comunicati durante l'onboarding e la formazione annuale di sensibilizzazione, e pubblicati sull'intranet dell'organizzazione.

Le segnalazioni DEVONO includere, ove noto:

- Cosa è stato osservato (descrizione dell'evento).
- Quando si è verificato o è stato scoperto.
- Quali sistemi, dati o persone sono coinvolti.
- Eventuali azioni già intraprese.

Gli eventi di sicurezza possono essere rilevati anche tramite monitoraggio automatizzato, analisi dei log o notifica di terzi.

I dipendenti NON devono tentare di investigare o risolvere autonomamente gli incidenti sospetti. La conservazione delle prove ha la priorità sulla curiosità.

---

## Valutazione e triage degli eventi

Il team di gestione della sicurezza delle informazioni DEVE valutare tutti gli eventi di sicurezza segnalati per determinare se costituiscono un incidente di sicurezza.

La valutazione DEVE considerare:

- La natura e l'ambito dell'evento.
- La classificazione delle informazioni coinvolte.
- Il numero di interessati o sistemi coinvolti.
- Se sono coinvolti dati personali (potenziale violazione di dati).
- Il potenziale impatto aziendale, legale o normativo.

Gli eventi che non raggiungono la soglia per un incidente DEVONO essere registrati, e le tendenze DEVONO essere monitorate.

### Registro degli incidenti

Tutti gli eventi di sicurezza segnalati e gli incidenti confermati DEVONO essere registrati nel registro degli incidenti con i seguenti campi minimi:

| Campo | Descrizione |
|-------|-------------|
| ID incidente | Identificatore univoco (es. INC-2026-001) |
| Data/ora segnalazione | Quando l'evento è stato segnalato |
| Data/ora rilevamento | Quando l'evento si è verificato o è stato rilevato per la prima volta |
| Segnalante | Chi ha segnalato l'evento |
| Descrizione | Riepilogo di quanto accaduto |
| Sistemi/dati coinvolti | Quali sistemi, applicazioni o tipi di dati sono coinvolti |
| Livello di classificazione | Classificazione delle informazioni coinvolte |
| Dati personali coinvolti | Sì/No; se sì, categorie e numero stimato di interessati |
| Gravità | Critico / Alto / Medio / Basso |
| Stato | Aperto / In indagine / Contenuto / Risolto / Chiuso |
| Assegnato a | Gestore dell'incidente o team |
| Causa profonda | Determinata dopo l'indagine |
| Azioni intraprese | Azioni di contenimento, eradicazione, ripristino con timestamp |
| Lezioni apprese | Riferimento alla revisione post-incidente (se condotta) |
| Data di chiusura | Quando l'incidente è stato formalmente chiuso |

---

## Classificazione degli incidenti

Gli incidenti confermati DEVONO essere classificati per gravità per determinare la priorità di risposta, l'escalation e i requisiti di comunicazione:

| Gravità | Descrizione | Esempi | Risposta iniziale |
|---------|-------------|--------|-------------------|
| **Critico** | Violazione di dati confermata, interruzione totale del servizio, compromissione attiva di sistemi critici | Ransomware, esfiltrazione di dati, compromissione dei sistemi di autenticazione | Immediata (entro 1 ora) |
| **Alto** | Impatto significativo sulle funzioni principali, possibile esposizione di dati, attacco mirato | Malware su più endpoint, accesso non autorizzato a dati sensibili, campagna di phishing diretta ai dirigenti | Entro 4 ore |
| **Medio** | Impatto limitato, circoscritto a un singolo sistema o utente, nessuna perdita confermata di dati | Rilevamento singolo di malware, violazione della policy, tentativo di intrusione fallito | Entro 1 giorno lavorativo |
| **Basso** | Impatto minimo, nessun dato coinvolto, informativo | Aumento dello spam, lieve deviazione dalla policy, singolo schema di login fallito | Entro 3 giorni lavorativi |

La gravità può essere escalata in qualsiasi momento durante il ciclo di vita dell'incidente man mano che emergono nuove informazioni.

---

## Risposta agli incidenti

### Ciclo di vita della risposta

Gli incidenti DEVONO essere gestiti attraverso le seguenti fasi, allineate con NIST SP 800-61:

1. **Contenimento** — Limitare l'impatto e prevenire ulteriori danni. Le azioni di contenimento a breve termine (ad es. isolamento dei sistemi coinvolti, disabilitazione degli account compromessi) DEVONO essere adottate immediatamente. Laddove l'eradicazione non possa essere immediata, DEVONO essere pianificate strategie di contenimento a lungo termine.

2. **Eradicazione** — Rimuovere la causa profonda dell'incidente. Ciò può includere la rimozione del malware, la chiusura delle vulnerabilità, il reset delle credenziali compromesse o la ricostruzione dei sistemi coinvolti.

3. **Ripristino** — Riportare i sistemi e i servizi alle normali operazioni. Il ripristino DEVE essere verificato attraverso test prima di riconsegnare i sistemi alla produzione. Il monitoraggio DEVE essere potenziato durante il periodo di ripristino per rilevare eventuali ricorrenze.

4. **Revisione post-incidente** — Condurre una revisione strutturata dopo la risoluzione (si veda la sezione Lezioni apprese di seguito).

Tutte le azioni di risposta agli incidenti DEVONO essere documentate con timestamp, azioni intraprese e personale coinvolto.

### Team di risposta agli incidenti

I seguenti ruoli DEVONO essere assegnati nell'ambito della capacità di risposta agli incidenti:

| Ruolo | Responsabilità | Assegnato a |
|-------|----------------|------------|
| **Responsabile del team di risposta agli incidenti** | Coordinamento complessivo della risposta agli incidenti; decisioni di escalation; comunicazione con il senior management | RSSI o IT Security Manager |
| **Responsabile tecnico** | Indagine tecnica, contenimento ed eradicazione; conservazione delle prove | Senior IT Security Analyst o IT Operations Lead |
| **Responsabile delle comunicazioni** | Comunicazioni interne ed esterne; portavoce con i media (se necessario) | RSSI o portavoce designato |
| **Consulente legale** | Consulenza legale sugli obblighi di notifica, gestione delle prove, requisiti normativi | Consulente legale (interno o esterno) |
| **Referente aziendale** | Valutazione dell'impatto aziendale; coordinamento con le unità aziendali coinvolte | Responsabile di dipartimento o coordinatore della continuità operativa |

Le assegnazioni dei ruoli DEVONO essere documentate, comunicate a tutti i membri del team e riviste annualmente. DEVONO essere assegnati sostituti per ogni ruolo per garantire la disponibilità.

### Escalation

Il responsabile del team di risposta agli incidenti DEVE escalare gli incidenti al senior management quando:

- L'incidente è classificato come Critico o Alto.
- L'incidente coinvolge dati personali (potenziale notifica di violazione di dati).
- L'incidente potrebbe richiedere una notifica esterna (normativa, forze dell'ordine, clienti).
- L'incidente supera la capacità o l'autorità del team di risposta.
- L'incidente non è stato contenuto entro il termine previsto.

### Comunicazione

Le informazioni sull'incidente DEVONO essere condivise su base strettamente necessaria. La comunicazione durante un incidente attivo DEVE essere coordinata tramite il responsabile del team di risposta agli incidenti.

Per gli incidenti Critici e Alti DEVONO essere forniti aggiornamenti interni sullo stato a intervalli regolari.

La comunicazione esterna (media, clienti, partner) DEVE essere approvata dal senior management e revisionata dal consulente legale prima della diffusione.

---

## Incidenti significativi

Gli incidenti significativi sono definiti come incidenti che costituiscono una violazione legale o normativa, potrebbero portare a un'indagine esterna o a procedimenti legali.

### Indicazioni generali

In tutti i casi in cui una situazione possa portare a un'indagine esterna o a procedimenti legali, DEVONO essere coinvolte risorse esterne specializzate.

Non appena possibile, DEVONO cessare tutte le attività sui, gli accessi ai, le modifiche ai o le manomissioni dei sistemi, documenti, luoghi, file, database, applicazioni o altre entità nell'ambito coinvolte. Le uniche eccezioni sono la tutela della vita, della salute e della sicurezza, o le azioni minime necessarie per il triage e la messa in sicurezza.

### Procedura

1. Nominare un Responsabile del team dell'incidente significativo dal senior management come unico punto di contatto e coordinamento.
2. Seguire le indicazioni sopra per fermare e mettere in sicurezza.
3. Contattare immediatamente il consulente legale.
4. Contattare immediatamente un fornitore di informatica forense e investigativa qualificato e autorizzato.
5. Se necessario, contattare le autorità competenti incluse le forze dell'ordine, l'Incaricato federale della protezione dei dati e della trasparenza (IFPDT) e gli eventuali regolatori di settore applicabili.
6. Se si dispone di una copertura assicurativa cyber, informare immediatamente la compagnia assicuratrice.
7. Seguire le indicazioni del consulente legale, delle forze dell'ordine, degli investigatori forensi e delle compagnie assicurative, rispettando nel contempo il processo di gestione degli incidenti per la registrazione, il monitoraggio e la gestione dell'incidente.

---

## Notifica delle violazioni di dati

Laddove un incidente coinvolga dati personali (una violazione di dati personali), si applicano i seguenti requisiti di notifica:

### Notifica ai sensi della nLPD svizzera

| Notifica | Trigger | Termine |
|----------|---------|---------|
| **IFPDT** (Incaricato federale della protezione dei dati e della trasparenza) | Violazione di dati che probabilmente risulterà in un **rischio elevato** per la personalità o i diritti fondamentali degli interessati | **Il prima possibile** dopo essere venuti a conoscenza della violazione |
| **Interessati** | Laddove la notifica sia necessaria per la protezione degli interessati, o laddove l'IFPDT lo richieda | **Il prima possibile** (nessun termine fisso) |
| **Responsabile del trattamento → Titolare** | Il responsabile del trattamento scopre una violazione che coinvolge i dati personali del titolare | **Il prima possibile** dopo la scoperta |

### Notifica ai sensi del GDPR UE (ove applicabile)

| Notifica | Trigger | Termine |
|----------|---------|---------|
| **Autorità di controllo** | Qualsiasi violazione di dati personali, salvo che sia improbabile che comporti un rischio per i diritti e le libertà delle persone | **Entro 72 ore** dall'acquisizione della consapevolezza |
| **Interessati** | Violazione che probabilmente comporterà un **rischio elevato** per i diritti e le libertà | **Senza indebito ritardo** |

Laddove si applichino sia la nLPD che il GDPR, l'organizzazione DEVE rispettare il termine più stringente (72 ore).

### Contenuto della notifica

Le notifiche di violazione alle autorità di controllo DEVONO includere, come minimo:

| Elemento | nLPD (Art. 24) | GDPR (Art. 33) |
|---------|-----------------|-----------------|
| Natura della violazione | Richiesto | Richiesto (incluse categorie e numero approssimativo di interessati e dati) |
| Conseguenze e rischi | Richiesto | Richiesto (conseguenze probabili) |
| Misure adottate o pianificate | Richiesto | Richiesto (misure adottate o proposte per affrontare e mitigare) |
| Punto di contatto | Richiesto (dove IFPDT o interessati possono ottenere ulteriori informazioni) | Richiesto (nome e dati di contatto del DPD o altro punto di contatto) |

Laddove al momento della notifica non siano disponibili informazioni complete, queste DEVONO essere fornite per fasi senza indebito ritardo.

### Valutazione della violazione

Non tutti gli incidenti di sicurezza che coinvolgono dati personali richiedono la notifica. Il team di risposta agli incidenti DEVE valutare:

- La natura e la sensibilità dei dati personali coinvolti.
- Il numero di interessati coinvolti.
- La gravità e la probabilità delle conseguenze per gli interessati.
- Se i dati erano cifrati o altrimenti resi incomprensibili.
- Se la violazione è stata contenuta e il rischio mitigato.

La valutazione e la decisione (inclusa la motivazione per non notificare, se applicabile) DEVONO essere documentate.

---

## Raccolta e conservazione delle prove

Laddove un incidente possa richiedere analisi forense, azioni legali o indagini normative, le prove DEVONO essere raccolte e conservate seguendo questi principi:

### Gestione delle prove

- Le prove DEVONO essere raccolte il prima possibile dopo l'identificazione dell'incidente.
- Le prove originali NON devono essere accedute, modificate o analizzate direttamente. DEVONO essere create copie forensi (immagini bit per bit) utilizzando strumenti di write-blocking.
- Tutte le prove DEVONO essere verificate utilizzando funzioni hash crittografiche (SHA-256 come minimo) per confermarne l'integrità.

### Catena di custodia

DEVE essere mantenuto un registro della catena di custodia per tutte le prove, documentando:

- Cosa è stato raccolto (descrizione, numeri di serie, identificatori).
- Quando è stato raccolto (data, ora).
- Chi lo ha raccolto.
- Dove è archiviato.
- Chi vi ha avuto accesso e quando.
- Eventuali trasferimenti tra custodi.

### Archiviazione delle prove

- Le prove DEVONO essere archiviate in un luogo sicuro con accesso limitato.
- Le prove digitali DEVONO essere archiviate su supporti cifrati.
- Le prove fisiche DEVONO essere archiviate in un contenitore antimanomissione e con serratura.
- Le prove DEVONO essere conservate per un minimo di **12 mesi** dalla chiusura dell'incidente, o più a lungo se richiesto dal consulente legale, da requisiti normativi o da procedimenti in corso.

### Supporto forense esterno

Per gli incidenti significativi, DEVONO essere coinvolti investigatori forensi esterni qualificati. L'organizzazione DEVE identificare e pre-approvare almeno un fornitore esterno di informatica forense e mantenere i dati di contatto aggiornati e le condizioni di ingaggio (retainer o termini di riferimento pre-concordati). Il personale interno NON deve condurre analisi forensi a meno che non sia adeguatamente formato e qualificato.

---

## Lezioni apprese

Una revisione post-incidente DEVE essere condotta per tutti gli incidenti di gravità Critica e Alta, e opzionalmente per quelli Medi laddove possano essere ricavate lezioni utili.

### Processo di revisione

La revisione DEVE essere tenuta entro 5 giorni lavorativi dalla risoluzione dell'incidente, mentre i dettagli sono ancora freschi. La revisione DEVE includere tutto il personale che ha contribuito alla risposta.

La revisione DEVE documentare:

- **Cronologia**: Una cronologia fattuale dell'incidente dal rilevamento alla risoluzione.
- **Causa profonda**: La causa sottostante dell'incidente (non solo il fattore scatenante).
- **Cosa ha funzionato**: Azioni di risposta efficaci, misure di contenimento riuscite, buon coordinamento del team.
- **Cosa potrebbe essere migliorato**: Lacune nel rilevamento, ritardi nella risposta, problemi di comunicazione, strumenti o procedure mancanti.
- **Azioni correttive**: Miglioramenti specifici e misurabili con proprietario assegnato e scadenza.

### Seguito

- Le azioni correttive DEVONO essere monitorate fino al completamento.
- Le lezioni apprese DEVONO essere comunicate al personale interessato.
- Il piano di risposta agli incidenti DEVE essere aggiornato laddove i risultati indichino lacune.
- Le tendenze tra gli incidenti DEVONO essere riviste trimestralmente per identificare problemi sistemici.

Le revisioni DEVONO essere condotte in modo non colpevolizzante, concentrandosi sul miglioramento dei sistemi e dei processi piuttosto che sulle colpe individuali.

---

## Test della risposta agli incidenti

Il piano di risposta agli incidenti DEVE essere testato almeno **annualmente** attraverso esercitazioni tabletop o simulazioni per verificare che:

- Ruoli e responsabilità siano compresi.
- I canali di comunicazione funzionino correttamente.
- I percorsi di escalation siano chiari ed efficaci.
- Le procedure di raccolta delle prove siano pratiche.
- I termini di notifica delle violazioni di dati possano essere rispettati.

**Scenari minimi di test** (da ruotare annualmente):

| Scenario | Test | Frequenza |
|----------|------|-----------|
| Attacco ransomware con cifratura dei dati | Contenimento, ripristino da backup, comunicazione, decisione se pagare/non pagare | Almeno ogni 2 anni |
| Violazione di dati personali con obbligo di notifica | Valutazione della violazione, processo di notifica all'IFPDT, notifica agli interessati | Almeno ogni 2 anni |
| Minaccia interna / account privilegiato compromesso | Rilevamento, revoca dell'accesso, conservazione delle prove, coordinamento HR | Almeno ogni 2 anni |
| Compromissione email aziendale / social engineering | Rilevamento, verifica dei controlli finanziari, segnalazione dell'incidente | Almeno ogni 2 anni |

I risultati dei test e i miglioramenti DEVONO essere documentati, inclusi i partecipanti, i dettagli dello scenario, le lacune osservate e le azioni correttive con proprietari e scadenze.

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa policy:

- **Registro degli incidenti** (tutti gli eventi segnalati e gli incidenti confermati con gravità, stato, risoluzione) — *mantenuto in modo continuativo; revisione trimestrale per le tendenze*
- **Registri di risposta agli incidenti** (azioni di contenimento, eradicazione, ripristino con timestamp) — *conservati per un minimo di 3 anni*
- **Registri di valutazione e notifica delle violazioni di dati** (incluse le decisioni di non notificare, con motivazione) — *conservati per 5 anni*
- **Registri della catena di custodia** per le prove forensi — *conservati per la durata di eventuali procedimenti legali più 2 anni*
- **Rapporti di revisione post-incidente** con azioni correttive e tracciamento del completamento — *completati entro 5 giorni lavorativi dalla risoluzione; azioni monitorate fino alla chiusura*
- **Registri dei test di risposta agli incidenti** (esercitazioni tabletop, simulazioni) — *annuali; conservati per 3 anni*
- **Elenco dei contatti per la risposta agli incidenti** (team interno, consulente legale, fornitore forense pre-approvato, IFPDT, fornitore di assicurazione cyber) — *revisione trimestrale; aggiornamento ad ogni modifica*
- **Template di comunicazione** (notifica interna, notifica esterna, notifica agli interessati, comunicato stampa) — *pre-approvati dal consulente legale; revisione annuale*

### Metriche degli incidenti

Le seguenti metriche DEVONO essere segnalate trimestralmente al RSSI e al Team di revisione del management:

| Metrica | Descrizione |
|---------|-------------|
| Totale eventi segnalati | Volume di eventi di sicurezza ricevuti |
| Eventi convertiti in incidenti | Numero e percentuale di eventi classificati come incidenti |
| Incidenti per gravità | Ripartizione di Critico / Alto / Medio / Basso |
| Tempo medio di rilevamento (MTTD) | Tempo medio dall'occorrenza dell'evento al rilevamento |
| Tempo medio di risposta (MTTR) | Tempo medio dal rilevamento al contenimento |
| Tempo medio di risoluzione | Tempo medio dal rilevamento alla chiusura |
| Incidenti scaduti | Incidenti che superano i termini di risposta target |
| Violazioni di dati segnalate | Numero che richiede notifica all'IFPDT o all'autorità di controllo |
| Revisioni post-incidente completate | Percentuale di incidenti Critici/Alti con revisioni completate |

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, inclusi a titolo non esaustivo: metriche di risposta agli incidenti, completamento delle revisioni post-incidente, registri dei test, audit interni ed esterni, e feedback al proprietario della policy.

## Deroghe

Qualsiasi deroga a questa policy DEVE essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con documentazione dell'accettazione del rischio, dei controlli compensativi e di una data di revisione definita. Le deroghe DEVONO essere segnalate al Team di revisione del management.

## Non conformità

Un dipendente ritenuto responsabile di aver violato questa policy potrà essere soggetto a misure disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa policy è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO tener conto delle variazioni agli standard di gestione degli incidenti, ai requisiti normativi di notifica, alle minacce emergenti e alle lezioni apprese dagli incidenti ed esercitazioni.

---

# Sezioni della norma ISO 27001 trattate

Policy di gestione degli incidenti — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità del management |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | 5.36 Conformità a policy, regole e standard |
| Clausola 7.3 Consapevolezza | **5.24 Pianificazione e preparazione della gestione degli incidenti di sicurezza delle informazioni** |
| Clausola 8.1 Pianificazione e controllo operativi | **5.25 Valutazione e decisione sugli eventi di sicurezza delle informazioni** |
| | **5.26 Risposta agli incidenti di sicurezza delle informazioni** |
| | **5.27 Apprendimento dagli incidenti di sicurezza delle informazioni** |
| | **5.28 Raccolta delle prove** |
| | 6.3 Sensibilizzazione, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 6.8 Segnalazione degli eventi di sicurezza delle informazioni |

**Quadro normativo e legale**:

| Quadro di riferimento | Rilevanza |
|-----------------------|-----------|
| nLPD svizzera (revDSG) | Art. 24 — Notifica della violazione di dati all'IFPDT ("il prima possibile") |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 33–34 — Notifica della violazione (72 ore all'autorità, senza indebito ritardo agli interessati) |
| ISO/IEC 27001:2022 | Controlli Annex A 5.24, 5.25, 5.26, 5.27, 5.28 |
| ISO/IEC 27002:2022 | Sezioni 5.24–5.28 — Linee guida per l'implementazione |
| ISO/IEC 27037:2012 | Linee guida per l'identificazione, la raccolta, l'acquisizione e la conservazione delle prove digitali |
| NIST SP 800-61 Rev 2 | Guida alla gestione degli incidenti di sicurezza informatica (ciclo di vita a quattro fasi) |
| CIS Controls v8 | Controllo 17 (Gestione della risposta agli incidenti) |

---

<!-- QA_VERIFIED: 2026-04-03 -->

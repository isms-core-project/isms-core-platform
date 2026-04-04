<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.8-IT:framework:POL:a.5.8 -->
**ISMS-POL-A.5.8 — Sicurezza delle informazioni nella gestione dei progetti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza delle informazioni nella gestione dei progetti |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.8 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI | Quadro di politica iniziale |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data da definire]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Direttore dei Sistemi Informativi (DSI)
- Operativo: Direttore Operativo (DCO)
- Conformità: Responsabile Legale/Conformità
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-IMP-A.5.8-UG/TG (Guida all'implementazione della sicurezza nella gestione dei progetti)
- ISMS-POL-A.5.15-18 (Gestione delle identità e degli accessi)
- ISMS-POL-A.5.19-22 (Sicurezza delle relazioni con i fornitori)
- ISMS-POL-A.8.24 (Utilizzo della crittografia)
- ISMS-POL-A.8.25-28 (Ciclo di sviluppo sicuro)
- ISMS-POL-A.8.32 (Gestione dei cambiamenti)
- ISO/IEC 27001:2022 Controllo A.5.8

---

# Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per l'integrazione della sicurezza delle informazioni nella gestione dei progetti, al fine di garantire che i rischi di sicurezza siano sistematicamente affrontati durante tutto il ciclo di vita del progetto, conformemente al Controllo A.5.8 della norma ISO/IEC 27001:2022.

**Scopo**: Definire i requisiti organizzativi per l'integrazione della sicurezza delle informazioni nei processi di gestione dei progetti. Questa politica stabilisce QUALI attività di sicurezza sono richieste in ciascuna fase del progetto e CHI è responsabile dei risultati di sicurezza.

**Perimetro**: Questa politica si applica a tutti i progetti intrapresi da [Organizzazione], indipendentemente dal tipo di progetto, dalla metodologia, dalla complessità, dalle dimensioni, dalla durata o dall'ambito organizzativo, inclusi i progetti gestiti da team interni, fornitori esterni o strutture ibride.

**Allineamento normativo**: nLPD svizzera (Art. 8); RGPD dell'UE (Art. 25 — Protezione dei dati fin dalla progettazione e per impostazione predefinita); ISO/IEC 27001:2022. I requisiti settoriali condizionali (NIS2, DORA, FINMA) si applicano dove le attività aziendali di [Organizzazione] ne determinano l'applicabilità.

---

# Perimetro e applicabilità

## Controllo ISO/IEC 27001:2022 A.5.8

> *La sicurezza delle informazioni deve essere integrata nella gestione dei progetti.*

**Obiettivo del controllo**: Garantire che i rischi di sicurezza delle informazioni associati ai progetti e ai prodotti dei progetti siano sistematicamente identificati, valutati e trattati durante tutto il ciclo di vita del progetto.

## Nel perimetro

Questa politica si applica a:

- **Progetti IT**: Sviluppo software, implementazione di sistemi, dispiegamento di infrastrutture
- **Progetti aziendali**: Ridisegno dei processi, cambiamento organizzativo, attività di fusione/acquisizione
- **Progetti infrastrutturali**: Costruzione di data center, modifiche alle strutture, installazione di apparecchiature
- **Progetti di conformità**: Implementazione normativa, rimedio di audit, programmi di certificazione
- Progetti di tutte le dimensioni e durate
- Progetti indipendentemente dalla metodologia di gestione (Agile, Waterfall, ibrida)
- Progetti gestiti da team interni, fornitori esterni o team ibridi
- Tutte le fasi del progetto: Avvio, pianificazione, esecuzione, monitoraggio/controllo, chiusura

## Fuori dal perimetro

- Attività operative di routine che non costituiscono un progetto (manutenzione business-as-usual)
- Attività di risposta agli incidenti di emergenza (trattate in A.5.24-27)
- Modifiche minori gestite tramite il processo di controllo dei cambiamenti (trattate in A.8.32)

## Requisiti normativi

**Livello 1 — Conformità obbligatoria**:

- nLPD svizzera (Art. 8): Misure tecniche e organizzative appropriate
- RGPD dell'UE (Artt. 25, 32): Protezione dei dati fin dalla progettazione e per impostazione predefinita
- ISO/IEC 27001:2022: Controllo A.5.8 sicurezza delle informazioni nella gestione dei progetti

**Livello 2 — Applicabilità condizionale** (per ISMS-POL-00):

- NIS2, DORA, Circolare FINMA 2008/21, PCI DSS v4.0.1 — si applicano quando le condizioni aziendali ne determinano l'applicabilità

---

# Enunciati di politica

## Principi di integrazione della sicurezza del progetto

[Organizzazione] DEVE integrare la sicurezza delle informazioni in tutti i progetti sulla base dei seguenti principi:

| Principio | Requisito | Esempio di applicazione |
|-----------|-----------|-------------------------|
| **Integrazione precoce** | La sicurezza DEVE essere considerata fin dall'avvio del progetto, non aggiunta in seguito | Il mandato del progetto include la classificazione della sicurezza; le risorse di sicurezza sono allocate nel budget del progetto prima della fase di pianificazione |
| **Proporzionalità** | Lo sforzo di sicurezza DEVE essere proporzionale alla classificazione del rischio del progetto | Un tool interno a basso rischio riceve la validazione della lista di controllo (2 ore); un portale clienti ad alto rischio riceve test di penetrazione (40 ore) |
| **Copertura del ciclo di vita** | Le attività di sicurezza DEVONO avvenire in tutte le fasi del progetto | Revisione della sicurezza a ogni gate di fase; requisiti di sicurezza nella pianificazione, test nell'esecuzione, handover alla chiusura |
| **Basato sul rischio** | Le decisioni di sicurezza DEVONO essere basate sulla valutazione del rischio | I controlli di sicurezza selezionati in base alla modellazione delle minacce e alla classificazione dei dati, non su liste di controllo generiche |
| **Requisiti tracciabili** | I requisiti di sicurezza DEVONO essere documentati e monitorati fino all'implementazione | Il Registro dei requisiti di sicurezza collega ciascun requisito all'elemento di progettazione, al caso di test e alla prova di dispiegamento |
| **Insegnamenti tratti** | Le esperienze di sicurezza del progetto DEVONO alimentare il miglioramento continuo | La revisione post-progetto della sicurezza identifica le lacune nei controlli; i risultati aggiornano i modelli dei requisiti di sicurezza |

## Requisito di classificazione del progetto

Tutti i progetti DEVONO essere classificati in base all'impatto sulla sicurezza delle informazioni per determinare i requisiti di sicurezza proporzionali.

**Fattori di classificazione e matrice di decisione**:

I progetti DEVONO essere classificati in base al fattore più applicabile:

| Fattore | Alto rischio | Rischio medio | Basso rischio |
|---------|-------------|---------------|---------------|
| **Sensibilità dei dati** | Dati Critici/Riservati (DCP, dati di pagamento, proprietà intellettuale, informazioni aziendali riservate per A.5.12) | Dati interni (dati aziendali non pubblici, registri dei dipendenti) | Dati pubblici (contenuti di marketing, documentazione pubblicata) |
| **Criticità del sistema** | RTO < 4 ore, sistema generatore di ricavi, servizio rivolto ai clienti | RTO 4-24 ore, importante per il business ma non critico per i ricavi | RTO > 24 ore, sistema di supporto operativo |
| **Ambito normativo** | RGPD/PCI DSS v4.0.1/FINMA direttamente applicabili | nLPD svizzera applicabile | Nessun trattamento di dati regolamentato |
| **Esposizione esterna** | Rivolto a Internet o accessibile a parti esterne (clienti, partner, pubblico) | Accesso esterno controllato (VPN, connessione dedicata) | Accesso solo interno |
| **Complessità tecnica** | Nuovo schema architetturale, integrazioni nuove, controlli di sicurezza personalizzati | Architettura standard con personalizzazione moderata | Dispiegamento standard, architettura collaudata |
| **Coinvolgimento di terze parti** | Funzione critica esternalizzata (hosting, autenticazione, elaborazione dei pagamenti) | Componenti gestiti da fornitori (integrazione SaaS, servizi gestiti) | Sviluppo e hosting completamente interni |

**Logica di classificazione**: Se **qualsiasi fattore** soddisfa i criteri di Alto rischio → classificare come **Alto rischio**. Se **qualsiasi fattore** soddisfa i criteri di Rischio medio (e nessun fattore di Alto rischio) → classificare come **Rischio medio**. Se **tutti i fattori** soddisfano i criteri di Basso rischio → classificare come **Basso rischio**.

**Documentazione della classificazione**: La determinazione della classificazione e la motivazione DEVONO essere documentate nel mandato del progetto e approvate per autorità di approvazione come di seguito.

**Livelli di classificazione**:

| Classificazione | Descrizione | Autorità di approvazione |
|----------------|-------------|--------------------------|
| **Alto rischio** | Impatto critico sulla sicurezza delle informazioni | Approvazione RSSI richiesta |
| **Rischio medio** | Impatto moderato sulla sicurezza delle informazioni | Approvazione del Responsabile della Sicurezza delle Informazioni |
| **Basso rischio** | Impatto minimo sulla sicurezza delle informazioni | Il Project Manager si auto-classifica con la revisione InfoSec |

La classificazione DEVE essere rivista a ogni gate di fase e aggiornata se l'ambito, la sensibilità dei dati o l'esposizione esterna cambiano in modo significativo.

## Requisiti di gate di fase della sicurezza

[Organizzazione] DEVE integrare le revisioni della sicurezza nella governance del progetto ai seguenti gate di fase:

| Gate di fase | Criteri di sicurezza richiesti |
|-------------|-------------------------------|
| **Approvazione del progetto** | Classificazione della sicurezza determinata; rischi di sicurezza iniziali identificati; budget di sicurezza allocato |
| **Approvazione della pianificazione** | Requisiti di sicurezza documentati e approvati; risorse di sicurezza impegnate |
| **Checkpoint di esecuzione** | Test di sicurezza condotti; risultati critici rimediati |
| **Approvazione del dispiegamento** | Tutti i risultati Critici/Alti rimediati o accettati; documentazione di handover della sicurezza completa |
| **Chiusura del progetto** | Rischi residui formalmente accettati; insegnamenti tratti documentati; asset registrati |

I progetti NON DEVONO procedere alla fase successiva fino a quando i criteri di sicurezza per la fase corrente non sono soddisfatti o formalmente accettati dall'autorità appropriata.

## Identificazione dei requisiti di sicurezza

I requisiti di sicurezza per i prodotti del progetto DEVONO essere identificati sistematicamente utilizzando il seguente processo:

**Processo di identificazione dei requisiti**:

1. **Valutazione dell'applicabilità**: Il Project Manager, con il supporto del Responsabile InfoSec, esamina ciascuna categoria di requisiti di sicurezza rispetto all'ambito del progetto:
   - Sicurezza delle applicazioni (A.8.25-28): Applicabile se il progetto include sviluppo software o codice personalizzato
   - Protezione dei dati (A.8.24, RGPD/nLPD): Applicabile in base alla classificazione dei dati per A.5.12
   - Controllo degli accessi (A.5.15-18): Applicabile per tutti i progetti (minimo: conformità alla politica di controllo degli accessi)
   - Sicurezza dell'infrastruttura (A.8.20-22): Applicabile se il progetto incide sull'architettura di rete o dispiegamento dell'infrastruttura
   - Sicurezza delle terze parti (A.5.19-22): Applicabile se il progetto coinvolge fornitori esterni o servizi cloud
   - Requisiti normativi (ISMS-POL-00): Applicabile in base all'analisi del Livello 1/2

2. **Scoping dei requisiti**: Per le categorie applicabili, i requisiti specifici vengono selezionati in base a: classificazione dei dati; requisiti di criticità del sistema (RTO/RPO per A.5.29-30); profilo delle minacce (per A.5.7 e modellazione delle minacce specifiche del progetto); obblighi normativi (per requisiti obbligatori Livello 1/2 ISMS-POL-00).

3. **Documentazione**: I requisiti applicabili DEVONO essere documentati in:
   - **Progetti a Rischio medio/Alto**: Registro dei requisiti di sicurezza (strumento di tracciamento formale)
   - **Progetti a Basso rischio**: Registro dei rischi del progetto (requisiti di sicurezza come voci di mitigazione del rischio)

4. **Approvazione**: I requisiti DEVONO essere rivisti e approvati da:
   - **Progetti ad Alto rischio**: Approvazione RSSI prima della fase di esecuzione
   - **Progetti a Rischio medio**: Approvazione del Responsabile InfoSec prima della fase di esecuzione
   - **Progetti a Basso rischio**: Conferma del Responsabile InfoSec della completezza dei requisiti

Le procedure dettagliate di identificazione dei requisiti, le liste di controllo specifiche per categoria e il modello del Registro dei requisiti di sicurezza sono forniti in ISMS-IMP-A.5.8.

## Requisito di test di sicurezza

Tutti i progetti DEVONO includere test di sicurezza proporzionali alla classificazione del progetto, con l'ambito dei test determinato come segue:

**Requisiti di test di sicurezza per classificazione**:

- **Progetti ad Alto rischio**:
  - **Obbligatorio**: Test di penetrazione esterni (metodologia OWASP o equivalente), scansione automatizzata delle vulnerabilità (settimanalmente durante lo sviluppo + scansione finale pre-dispiegamento), revisione del codice di sicurezza per il codice personalizzato (copertura minima del 20% delle funzioni di autenticazione, autorizzazione, protezione dei dati e crittografiche)
  - **Criteri di test**: I test di penetrazione DEVONO essere eseguiti da terze parti indipendenti. Tutti i risultati Critici e ≥80% dei risultati Alti DEVONO essere rimediati prima del dispiegamento.

- **Progetti a Rischio medio**:
  - **Obbligatorio**: Scansione automatizzata delle vulnerabilità (scansione finale pre-dispiegamento), test di sicurezza funzionali di autenticazione, autorizzazione, validazione dei dati e gestione degli errori
  - **Condizionale**: Test di penetrazione richiesti se il progetto è rivolto a Internet O elabora dati regolamentati (RGPD/PCI DSS v4.0.1)
  - **Criteri di test**: Tutti i risultati Critici e ≥70% dei risultati Alti DEVONO essere rimediati prima del dispiegamento.

- **Progetti a Basso rischio**:
  - **Obbligatorio**: Validazione della sicurezza rispetto alla lista di controllo dei requisiti di sicurezza (minimo: verifica del controllo degli accessi A.5.15-18, verifica della cifratura A.8.24 se applicabile)
  - **Opzionale**: Scansione automatizzata delle vulnerabilità (raccomandata ma non obbligatoria)
  - **Criteri di test**: I risultati Critici DEVONO essere rimediati prima del dispiegamento.

**Documentazione della sufficienza dei test**: Per i progetti a Rischio medio/Alto, l'adeguatezza dei test DEVE essere documentata nel report di valutazione della sicurezza e approvata dal Responsabile InfoSec (Medio) o dal RSSI (Alto) prima dell'autorizzazione al dispiegamento. Se l'obiettivo di rimedio non viene raggiunto, il rischio residuo DEVE essere formalmente accettato per la sezione Gestione delle eccezioni.

Le prove dei test (report di scansione, report di test di penetrazione, risultati della revisione del codice) DEVONO essere archiviate per A.5.33 e fornite nella documentazione di handover della sicurezza.

## Requisito di handover della sicurezza

Alla chiusura del progetto, la documentazione di handover della sicurezza DEVE essere fornita alle operazioni e convalidata come completa prima dell'autorizzazione alla chiusura del progetto.

**Criteri di completezza dell'handover della sicurezza**:

L'handover della sicurezza DEVE includere la seguente documentazione, consegnata al proprietario operativo e confermata completa tramite lista di controllo dell'handover:

1. **Documentazione dell'architettura della sicurezza**:
   - Progettazione della sicurezza del sistema (confini di fiducia, modello di autenticazione/autorizzazione, implementazione della cifratura)
   - Diagrammi del flusso dei dati che mostrano la classificazione dei dati e i controlli di protezione
   - Architettura di rete (regole del firewall, segmentazione della rete, punti di accesso esterni)
   - Sicurezza dell'integrazione (autenticazione API, dipendenze da servizi di terze parti)

2. **Procedure operative di sicurezza**:
   - Requisiti di monitoraggio (fonti di log di sicurezza, soglie di avviso, integrazione SIEM)
   - Requisiti di conservazione dei log (per A.8.15, periodi di conservazione normativi)
   - Procedure di backup e ripristino (per A.8.13, inclusi test di ripristino specifici per la sicurezza)
   - Escalation della risposta agli incidenti (tipi di incidenti di sicurezza, percorsi di escalation, informazioni di contatto)
   - Gestione delle patch di sicurezza (frequenza di aggiornamento, requisiti di test, procedure di rollback)

3. **Rischi residui accettati**:
   - Documenti di accettazione del rischio formali con firme di approvazione (per autorità di classificazione del rischio)
   - Controlli compensativi (se applicabili)
   - Cronologia di rivalutazione del rischio (per accettazioni a tempo limitato)

4. **Prove dei test di sicurezza**:
   - Report finale della scansione delle vulnerabilità (datato entro 7 giorni dal dispiegamento)
   - Report di test di penetrazione (se applicabile per il Requisito di test di sicurezza)
   - Documenti di rimedio per i risultati Critici/Alti (o accettazione del rischio per i risultati non risolti)

**Processo di validazione dell'handover**: Le Operazioni DEVONO confermare la completezza dell'handover tramite la Lista di controllo dell'handover della sicurezza firmata (modello in ISMS-IMP-A.5.8) prima che il Project Manager richieda l'autorizzazione alla chiusura del progetto. La documentazione di handover incompleta blocca la chiusura del progetto fino a quando le lacune non vengono risolte o esplicitamente accettate dal proprietario operativo e dal RSSI (per i progetti ad Alto rischio).

La documentazione di handover è archiviata per i requisiti di gestione dei documenti A.5.33 e mantenuta come documentazione di riferimento operativa per il ciclo di vita del sistema.

---

# Ruoli e responsabilità

## Direzione generale

**Responsabilità**: Sicurezza organizzativa complessiva, inclusa l'integrazione della sicurezza dei progetti.

**Compiti**: Approvare questa politica e garantire le risorse organizzative per l'implementazione; rivedere lo stato della sicurezza dei progetti ad alto rischio nelle revisioni della direzione; accettare i rischi residui per i progetti critici.

## Responsabile della Sicurezza dei Sistemi Informativi (RSSI)

**Responsabilità**: Implementazione del programma di sicurezza delle informazioni, inclusa la supervisione della sicurezza dei progetti.

**Compiti**: Approvare e mantenere questa politica; approvare le classificazioni dei progetti ad Alto rischio; accettare i rischi di sicurezza residui per i progetti ad Alto rischio; fornire risorse di sicurezza per il supporto ai progetti; monitorare le metriche di sicurezza dei progetti e riferire alla Direzione generale; approvare le eccezioni ai requisiti di sicurezza.

**Autorità**: Bloccare o ritardare i progetti con rischi di sicurezza inaccettabili; imporre controlli di sicurezza aggiuntivi.

## Responsabile della Sicurezza delle Informazioni / Team di sicurezza

**Responsabilità**: Guida operativa sulla sicurezza e supporto alla valutazione del rischio.

**Compiti**: Supportare i team di progetto nell'identificazione dei requisiti di sicurezza e nella valutazione del rischio; rivedere e approvare le classificazioni dei progetti a Rischio medio; rivedere i requisiti di sicurezza e fornire guida tecnica; condurre o commissionare test di sicurezza; mantenere modelli e liste di controllo dei requisiti di sicurezza.

**Autorità**: Escalation delle preoccupazioni di sicurezza al RSSI; raccomandare ritardi del progetto per i rischi non mitigati.

## Project Manager

**Responsabilità**: Successo complessivo del progetto, inclusa l'implementazione dei requisiti di sicurezza.

**Compiti**: Classificare il livello di rischio di sicurezza del progetto (con il supporto del Responsabile InfoSec); garantire che le attività di sicurezza siano pianificate e finanziate; eseguire le attività di sicurezza in ciascuna fase del progetto; mantenere il registro dei rischi di sicurezza del progetto; escalation dei rischi e dei problemi di sicurezza; documentare gli aspetti di sicurezza nella chiusura e nell'handover del progetto.

## Proprietario aziendale / Proprietario del prodotto

**Responsabilità**: Requisiti aziendali, incluse le esigenze di sicurezza dei prodotti del progetto.

**Compiti**: Definire i requisiti aziendali di sicurezza; partecipare alla valutazione del rischio di sicurezza; approvare i requisiti di sicurezza come parte dell'ambito del progetto; accettare i rischi di sicurezza residui per i sistemi/servizi di proprietà.

## Responsabile tecnico / Architetto della soluzione

**Responsabilità**: Progettazione e implementazione tecnica, inclusa l'architettura della sicurezza.

**Compiti**: Progettare i controlli di sicurezza nell'architettura della soluzione; implementare i requisiti di sicurezza secondo le specifiche; supportare la modellazione delle minacce e le revisioni dell'architettura della sicurezza; affrontare i risultati dei test o delle revisioni della sicurezza.

## Matrice RACI per le attività di sicurezza del progetto

| Attività | PM | InfoSec | RSSI | Prop. Aziendale | Resp. Tecnico |
|----------|----|---------| -----|-----------------|---------------|
| Classificazione del progetto | R | A | I | C | C |
| Identificazione dei requisiti di sicurezza | R | A | I | C | C |
| Progettazione dell'architettura della sicurezza | C | C | I | I | R/A |
| Esecuzione dei test di sicurezza | R | C | I | I | R |
| Accettazione del rischio residuo | I | C | A (Alto) | A (Medio/Basso) | I |
| Revisione dell'handover della sicurezza | R | A | I | C | C |

R = Responsabile (svolge il lavoro), A = Accountable (decisione finale), C = Consultato (fornisce input), I = Informato (tenuto aggiornato)

---

# Governance e gestione delle eccezioni

## Autorità di revisione della sicurezza

| Classificazione del progetto | Autorità di revisione |
|------------------------------|----------------------|
| Basso rischio | Auto-valutazione del Project Manager |
| Rischio medio | Revisione del Responsabile della Sicurezza delle Informazioni richiesta |
| Alto rischio | Approvazione del RSSI richiesta |

## Escalation

Le preoccupazioni di sicurezza DEVONO essere escalate entro: 2 giorni lavorativi per i progetti ad Alto rischio; 5 giorni lavorativi per i progetti a Rischio medio.

**Percorso di escalation**: Project Manager → Responsabile della Sicurezza delle Informazioni → RSSI → Direzione generale

**Trigger di escalation**:

- Risultati di sicurezza critici che non possono essere rimediati prima della scadenza del dispiegamento
- Requisiti di sicurezza in conflitto con gli obiettivi aziendali (che richiedono l'accettazione del rischio)
- Fornitore terzo incapace di soddisfare i requisiti di sicurezza
- Violazione dei dati o incidente di sicurezza che incide sui prodotti del progetto
- Preoccupazioni di conformità normativa identificate durante l'esecuzione del progetto

## Gestione delle eccezioni

Le eccezioni ai requisiti di sicurezza DEVONO essere: documentate con giustificazione aziendale e controlli compensativi; approvate dall'autorità appropriata in base alla classificazione del progetto; a tempo limitato e monitorate nel Registro delle eccezioni di sicurezza; riviste trimestralmente dal RSSI.

---

# Conformità e monitoraggio

## Requisiti di conformità

| Requisito | Misura di conformità |
|-----------|---------------------|
| Classificazione del progetto | Tutti i progetti classificati entro 5 giorni lavorativi dall'avvio |
| Requisiti di sicurezza | Documentati per tutti i progetti a Rischio medio/Alto prima dell'esecuzione |
| Test di sicurezza | Completati prima del dispiegamento per tutti i progetti |
| Accettazione del rischio residuo | Formalmente documentata prima della chiusura del progetto |
| Insegnamenti tratti | Acquisiti per tutti i progetti a Rischio medio/Alto |

## Monitoraggio e metriche

[Organizzazione] DEVE monitorare le metriche di sicurezza dei progetti incluse: progetti per classificazione della sicurezza; progetti con valutazioni della sicurezza completate; risultati della sicurezza per gravità e stato del rimedio; eccezioni di sicurezza concesse.

**Requisiti di reportistica delle metriche**:

- **Report mensile al RSSI**: Cruscotto dettagliato delle metriche: progetti per classificazione e stato della sicurezza (nei tempi / a rischio / in ritardo); risultati di sicurezza aperti per gravità e anzianità; eccezioni di sicurezza concesse rispetto a quelle rimediate; tassi di completamento dei test di sicurezza.

- **Report trimestrale alla Direzione**: Sintesi esecutiva: totale dei progetti e numero di progetti ad alto rischio; risultati di sicurezza critici e stato del rimedio; eccezioni di sicurezza che richiedono consapevolezza esecutiva; incidenti di sicurezza significativi che incidono sui progetti.

## Non conformità

La non conformità a questa politica può comportare: ritardi del progetto fino al soddisfacimento dei requisiti di sicurezza; escalation alla Direzione generale; azioni disciplinari per le politiche HR di [Organizzazione].

---

# Documenti correlati

| ID documento | Titolo del documento |
|-------------|---------------------|
| ISMS-POL-00 | Quadro di applicabilità normativa |
| ISMS-IMP-A.5.8-UG/TG | Guida all'implementazione della sicurezza nella gestione dei progetti |
| ISMS-POL-A.5.15-18 | Gestione delle identità e degli accessi |
| ISMS-POL-A.5.19-22 | Sicurezza delle relazioni con i fornitori |
| ISMS-POL-A.8.24 | Utilizzo della crittografia |
| ISMS-POL-A.8.25-28 | Ciclo di sviluppo sicuro |
| ISMS-POL-A.8.32 | Gestione dei cambiamenti |
| ISO/IEC 27001:2022 | Requisiti dei sistemi di gestione della sicurezza delle informazioni |
| ISO/IEC 27002:2022 | Controlli di sicurezza delle informazioni — Guida |
| ISO 21500:2021 | Gestione di progetti, programmi e portafogli |
| NIST SP 800-64 | Considerazioni sulla sicurezza nel ciclo di vita dello sviluppo dei sistemi |

---

# Prove per questa politica

**Prove per la Fase 1** (Revisione della documentazione): Documento di politica con firme di approvazione; quadro di classificazione del progetto definito; requisiti di gate di fase della sicurezza documentati; categorie di requisiti di sicurezza specificate; requisiti di test di sicurezza per classificazione; requisiti di handover della sicurezza documentati; ruoli e responsabilità assegnati; governance e procedure di eccezione definiti.

**Prove per la Fase 2** (Efficacia operativa): Approvazioni di classificazione del progetto che mostrano le determinazioni di classificazione del rischio di sicurezza (Alto/Medio/Basso); registri dei requisiti di sicurezza per i progetti a Rischio medio/Alto; documenti di approvazione del gate di fase con verifica dei criteri di sicurezza; report di test di sicurezza (test di penetrazione, scansioni delle vulnerabilità, revisioni del codice) per classificazione del progetto; monitoraggio dei risultati di sicurezza e del rimedio fino alla chiusura; pacchetti di documentazione di handover della sicurezza; documenti di accettazione del rischio residuo con approvazioni appropriate; documentazione degli insegnamenti tratti per i progetti a Rischio medio/Alto; registro delle eccezioni di sicurezza con approvazioni e limiti di tempo; cruscotti delle metriche di sicurezza dei progetti che mostrano le tendenze; documenti di formazione per i project manager sui requisiti di sicurezza.

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data da definire] |
| **Direttore Operativo (DCO)** | [Nome] | [Data da definire] |
| **Responsabile Legale/Conformità** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per l'integrazione della sicurezza delle informazioni nella gestione dei progetti. Le procedure di attuazione, i modelli di valutazione e le linee guida dettagliate sono documentate in ISMS-IMP-A.5.8 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->

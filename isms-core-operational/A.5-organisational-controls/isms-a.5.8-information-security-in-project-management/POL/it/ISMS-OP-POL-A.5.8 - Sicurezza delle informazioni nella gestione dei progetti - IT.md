<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.8-IT:operational:OP-POL:a.5.8 -->
**ISMS-OP-POL-A.5.8 — Sicurezza delle informazioni nella gestione dei progetti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza delle informazioni nella gestione dei progetti |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.5.8 |
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

- ISO/IEC 27001:2022 Controllo A.5.8 — Sicurezza delle informazioni nella gestione dei progetti
- ISO/IEC 27002:2022 Sezione 5.8 — Guida all'implementazione
- ISO 21500:2021 — Gestione di progetti, programmi e portfolio
- nLPD svizzera Art. 22 — Valutazione d'impatto sulla protezione dei dati
- NIST SP 800-53 Rev 5 SA-3 — Ciclo di vita dello sviluppo dei sistemi
- NIST SP 800-53 Rev 5 PL-2 — Piani di sicurezza e privacy dei sistemi

**Controlli Annex A correlati**:

| Controllo | Relazione con la sicurezza delle informazioni nella gestione dei progetti |
|-----------|--------------------------------------------------------------------------|
| A.5.1 Politiche per la sicurezza delle informazioni | Quadro normativo generale che fornisce la baseline dei requisiti di sicurezza per i progetti |
| A.5.7 Intelligence sulle minacce | L'intelligence sulle minacce informa la valutazione del rischio specifica del progetto e il threat modelling |
| A.5.9 Inventario delle informazioni e degli altri asset associati | I progetti creano nuovi asset che DEVONO essere registrati al momento del passaggio di consegne |
| A.5.12 Classificazione delle informazioni | La classificazione dei dati guida la classificazione di sicurezza del progetto e la selezione dei controlli |
| A.5.19 Sicurezza delle informazioni nelle relazioni con i fornitori | I requisiti di sicurezza dei fornitori si applicano ai progetti che coinvolgono fornitori esterni |
| A.5.34 Privacy e protezione dei dati personali | Requisiti DPIA per i progetti che trattano dati personali |
| A.8.25 Ciclo di vita dello sviluppo sicuro | Requisiti di sviluppo sicuro per i progetti software |
| A.8.26 Requisiti di sicurezza delle applicazioni | Identificazione dei requisiti di sicurezza per i progetti applicativi |
| A.8.27 Architettura di sistema sicura e principi di ingegneria | Sicurezza dell'architettura per i progetti infrastrutturali e di sistema |
| A.8.29 Test di sicurezza nello sviluppo e nell'accettazione | Requisiti di test di sicurezza integrati nei gate di fase del progetto |
| A.8.32 Gestione delle modifiche | Processo di controllo delle modifiche per le modifiche avviate dal progetto alla produzione |

**Politiche interne correlate**:

- Politica di classificazione e gestione delle informazioni
- Politica di sicurezza nelle relazioni con i fornitori
- Politica del ciclo di vita dello sviluppo sicuro
- Politica di gestione delle modifiche
- Politica sulla privacy e protezione dei dati personali
- Politica di gestione del rischio

---

# Politica sulla sicurezza delle informazioni nella gestione dei progetti

## Scopo

Lo scopo della presente politica è garantire che i rischi per la sicurezza delle informazioni correlati ai progetti e ai deliverable dei progetti siano sistematicamente identificati, valutati e trattati durante tutto il ciclo di vita del progetto. La sicurezza delle informazioni DEVE essere integrata nella gestione dei progetti in modo da essere parte di ogni progetto — non un elemento aggiunto alla fine.

I progetti introducono cambiamenti. I cambiamenti introducono rischi. Che il progetto riguardi una nuova applicazione software, un aggiornamento dell'infrastruttura, un approvvigionamento da fornitori o una riprogettazione dei processi aziendali, ogni progetto crea opportunità per l'indebolimento, l'aggiramento o l'omissione dei controlli di sicurezza, a meno che la sicurezza non sia esplicitamente affrontata in ogni fase.

La presente politica supporta la nLPD svizzera attuando misure organizzative appropriate al rischio per proteggere i dati personali durante le attività di progetto, incluso il requisito di valutazioni d'impatto sulla protezione dei dati (DPIA) ai sensi dell'Art. 22 laddove il trattamento sia suscettibile di comportare un elevato rischio per i diritti della personalità o i diritti fondamentali degli individui. Laddove l'organizzazione tratti dati di soggetti nell'UE/SEE, si applicano altresì i requisiti del GDPR Art. 25 (protezione dei dati fin dalla progettazione e per impostazione predefinita) e Art. 35 (DPIA).

## Ambito di applicazione

Tutti i progetti intrapresi dall'organizzazione, indipendentemente dal tipo, dalla metodologia, dalle dimensioni o dalla durata. Ciò include:

- Progetti di sviluppo software (interno e in outsourcing).
- Progetti di implementazione e integrazione di sistemi.
- Progetti di deployment e migrazione dell'infrastruttura (on-premises e cloud).
- Progetti di approvvigionamento IT (hardware, software, servizi SaaS).
- Progetti di riprogettazione dei processi aziendali con implicazioni per la sicurezza delle informazioni.
- Progetti di implementazione della conformità e della regolamentazione.
- Progetti di fusione, acquisizione o cessione che coinvolgono asset IT o dati.

**Escluso dall'ambito**: Attività operative di routine che non costituiscono un progetto (manutenzione e supporto ordinari); attività di risposta agli incidenti di emergenza (disciplinate dalla Politica di gestione degli incidenti); modifiche minori gestite attraverso il processo standard di controllo delle modifiche (disciplinate dalla Politica di gestione delle modifiche). Laddove vi sia incertezza sul fatto che un'attività costituisca un progetto, il RSSI o il Responsabile della sicurezza delle informazioni forniranno indicazioni.

## Principio

La sicurezza delle informazioni dovrebbe essere integrata nella gestione dei progetti. I requisiti di sicurezza DEVONO essere identificati tempestivamente — all'avvio del progetto — e affrontati proporzionalmente durante tutto il ciclo di vita del progetto in base alla classificazione del rischio di sicurezza del progetto. Nessun progetto DEVE procedere al deployment in produzione senza un'adeguata validazione della sicurezza per il proprio livello di classificazione.

Tutte le decisioni di sicurezza del progetto DEVONO essere basate sul rischio, considerando la sensibilità e la classificazione dei dati coinvolti, la criticità dei sistemi interessati, l'ambiente normativo e il potenziale impatto sul business in caso di sicurezza inadeguata.

---

## Classificazione dei progetti

Tutti i progetti DEVONO essere classificati in base al rischio per la sicurezza delle informazioni per determinare i requisiti di sicurezza proporzionali. La classificazione DEVE avvenire all'avvio del progetto ed essere documentata nel project charter o nel documento di avvio equivalente.

### Fattori di classificazione

I progetti DEVONO essere classificati in base al **fattore applicabile più elevato** nelle seguenti dimensioni:

| Fattore | Alto rischio | Rischio medio | Basso rischio |
|---------|-------------|---------------|---------------|
| **Sensibilità dei dati** | Dati riservati o con restrizioni (dati personali, verbali finanziari, proprietà intellettuale, segreti commerciali) | Dati interni (informazioni aziendali non pubbliche, verbali dei dipendenti) | Dati pubblici (contenuti di marketing, documentazione pubblicata) |
| **Criticità del sistema** | Sistema critico per il business (RTO < 4 ore); generatore di ricavi o rivolto ai clienti | Sistema importante per il business (RTO 4-24 ore); operativo interno | Sistema di supporto (RTO > 24 ore); strumentazione non critica |
| **Ambito normativo** | Trattamento ad alto rischio nLPD, DPIA GDPR Art. 35 richiesta, PCI DSS applicabile | Trattamento standard nLPD applicabile | Nessun trattamento di dati regolamentati |
| **Esposizione esterna** | Rivolto a Internet o accessibile a parti esterne (clienti, partner, pubblico) | Accesso esterno controllato (VPN, connessione dedicata) | Accesso solo interno |
| **Coinvolgimento di terze parti** | Funzione critica in outsourcing (hosting, autenticazione, elaborazione dei pagamenti) | Componenti gestiti da fornitori (integrazione SaaS, servizi gestiti) | Delivery completamente interna |

**Regola di classificazione**: Se **un singolo fattore** soddisfa i criteri di Alto rischio, il progetto DEVE essere classificato come **Alto rischio**. Se un fattore soddisfa il Rischio medio (e nessun fattore è Alto rischio), classificare come **Rischio medio**. Solo se **tutti i fattori** sono a Basso rischio il progetto DEVE essere classificato come **Basso rischio**.

### Esempi di classificazione

A supporto di decisioni di classificazione coerenti, i seguenti esempi illustrano scenari di progetto tipici per livello di classificazione:

| Fattore | Esempio Alto rischio | Esempio Rischio medio | Esempio Basso rischio |
|---------|---------------------|-----------------------|-----------------------|
| **Sensibilità dei dati** | Dati delle carte di credito dei clienti, cartelle sanitarie dei dipendenti | Indirizzi e-mail dei dipendenti, rapporti finanziari interni | Brochure di marketing, documentazione pubblica |
| **Criticità del sistema** | Sistema di elaborazione dei pagamenti (RTO < 1 ora) | CRM interno (RTO 8 ore) | Ambiente di test, sistema proof-of-concept |
| **Ambito normativo** | DPIA GDPR Art. 35 richiesta (profilazione), merchant PCI DSS Level 1 | nLPD svizzera applicabile (dati personali standard) | Nessun dato regolamentato |
| **Esposizione esterna** | Sito web pubblico, API rivolta ai clienti | Extranet dei partner, accesso solo VPN | Solo LAN interna |
| **Coinvolgimento di terze parti** | Processore di pagamenti ospitato su cloud, SaaS di autenticazione | Ospitato su AWS con gestione dell'organizzazione, Office 365 | Completamente interno, on-premises |

### Approvazione della classificazione

| Classificazione | Autorità di approvazione |
|-----------------|--------------------------|
| **Alto rischio** | Approvazione del RSSI obbligatoria |
| **Rischio medio** | Approvazione del Responsabile della sicurezza delle informazioni |
| **Basso rischio** | Il Project manager si auto-classifica; il Responsabile della sicurezza delle informazioni conferma |

La classificazione DEVE essere rivista a ogni gate di fase. Se l'ambito del progetto, la sensibilità dei dati o l'esposizione esterna cambiano in modo significativo, la classificazione DEVE essere aggiornata e nuovamente approvata.

### Guida al budget per la sicurezza

I project manager DEVONO stimare i costi di sicurezza in base alla classificazione del progetto durante la preparazione dei budget di progetto:

| Classificazione | Costo tipico della sicurezza | Attività incluse |
|-----------------|------------------------------|------------------|
| **Alto rischio** | 8–12% del costo totale del progetto | Threat modelling, revisione dell'architettura di sicurezza, penetration testing, revisione del codice di sicurezza, tempo del Responsabile della sicurezza delle informazioni |
| **Rischio medio** | 4–6% del costo totale del progetto | Analisi dei requisiti di sicurezza, scansione delle vulnerabilità, test funzionali di sicurezza, tempo del Responsabile della sicurezza delle informazioni |
| **Basso rischio** | 1–2% del costo totale del progetto | Revisione della checklist di sicurezza, scansione di base delle vulnerabilità |

Le stime del budget di sicurezza DEVONO essere incluse nella documentazione di avvio del progetto e approvate come parte del budget di progetto. Laddove si preveda che i costi di sicurezza effettivi superino l'intervallo stimato, il Project manager DEVE notificare il Responsabile della sicurezza delle informazioni e adeguare il budget di progetto di conseguenza.

---

## Identificazione dei requisiti di sicurezza

I requisiti di sicurezza per i deliverable del progetto DEVONO essere identificati sistematicamente durante la fase di pianificazione in base alla classificazione del progetto e alle categorie di asset e dati coinvolti.

### Categorie di requisiti

Il Project manager, con il supporto del Responsabile della sicurezza delle informazioni, DEVE valutare ciascuna delle seguenti categorie di requisiti rispetto all'ambito del progetto:

| Categoria di requisito | Applicabile quando | Fonte |
|------------------------|-------------------|-------|
| **Controllo degli accessi** | Tutti i progetti (baseline minima) | Politica di gestione delle identità e degli accessi |
| **Protezione dei dati e cifratura** | Il progetto coinvolge dati riservati o con restrizioni | Politica sull'uso della crittografia, nLPD Art. 8 |
| **Sicurezza delle applicazioni** | Il progetto include sviluppo software o codice personalizzato | Politica del ciclo di vita dello sviluppo sicuro |
| **Sicurezza dell'infrastruttura** | Il progetto distribuisce o modifica l'infrastruttura di rete | Politica di sicurezza della rete |
| **Sicurezza dei fornitori** | Il progetto coinvolge fornitori esterni o servizi cloud | Politica di sicurezza nelle relazioni con i fornitori |
| **Privacy e dati personali** | Il progetto tratta dati personali | Politica sulla privacy e protezione dei dati personali, nLPD Art. 22 |
| **Continuità operativa** | Il progetto riguarda sistemi critici per il business | Politica di continuità operativa e DR |
| **Registrazione e monitoraggio** | Il progetto distribuisce sistemi che richiedono monitoraggio della sicurezza | Politica di registrazione |

### Mappatura delle fonti dei requisiti

La seguente tabella di riferimento indica le aree di politica tipicamente applicabili ai tipi di progetto comuni, per assistere i project manager nell'identificazione dei requisiti applicabili:

| Tipo di progetto | Sempre applicabile | Spesso applicabile | Condizionatamente applicabile |
|-----------------|-------------------|-------------------|-------------------------------|
| **Sviluppo software** | Ciclo di vita dello sviluppo sicuro, Controllo degli accessi, Registrazione | Sicurezza delle applicazioni, Protezione dei dati, Gestione delle modifiche | Privacy e dati personali (se dati personali), Sicurezza dei fornitori (se esternalizzato) |
| **Deployment dell'infrastruttura** | Controllo degli accessi, Sicurezza della rete, Registrazione | Gestione della configurazione, Continuità operativa | Sicurezza dei fornitori (se gestito dal fornitore) |
| **Approvvigionamento SaaS** | Sicurezza dei fornitori, Controllo degli accessi | Protezione dei dati, Privacy e dati personali | Sicurezza delle applicazioni (se integrazione personalizzata) |

### Documentazione

- **Progetti ad Alto rischio e a Rischio medio**: I requisiti di sicurezza DEVONO essere documentati in un Registro dei requisiti di sicurezza (o nella sezione equivalente dello [Strumento di gestione dei progetti]) e tracciati fino all'implementazione e al testing.
- **Progetti a Basso rischio**: I requisiti di sicurezza DEVONO essere documentati come elementi di mitigazione del rischio nel registro dei rischi del progetto con conferma della conformità alla politica applicabile.

### Approvazione

- **Alto rischio**: Il RSSI approva i requisiti di sicurezza prima della fase di esecuzione.
- **Rischio medio**: Il Responsabile della sicurezza delle informazioni approva prima della fase di esecuzione.
- **Basso rischio**: Il Responsabile della sicurezza delle informazioni conferma la completezza dei requisiti.

---

## Gate di fase per le revisioni della sicurezza

Le revisioni della sicurezza DEVONO essere integrate nella governance del progetto ai seguenti gate di fase. I progetti NON DEVONO procedere alla fase successiva finché i criteri di sicurezza per il gate di fase corrente non siano soddisfatti o formalmente accettati dall'autorità appropriata.

### Requisiti dei gate di fase

| Gate di fase | Attività di sicurezza richieste |
|-------------|----------------------------------|
| **Avvio / Approvazione del progetto** | Classificazione del rischio di sicurezza determinata e approvata; rischi di sicurezza iniziali identificati nel registro dei rischi del progetto; stima del budget e dei requisiti di risorse per la sicurezza; screening DPIA completato (v. sezione Integrazione DPIA) |
| **Pianificazione / Approvazione del design** | Requisiti di sicurezza documentati, rivisti e approvati; threat model completato per i progetti ad Alto rischio (raccomandato per il Rischio medio); architettura di sicurezza revisionata per i progetti ad Alto rischio; DPIA completata dove lo screening ha indicato un alto rischio |
| **Esecuzione / Checkpoint di build** | Test di sicurezza condotti per classificazione; risultati di sicurezza tracciati e rimediati secondo gli obiettivi di gravità; requisiti di sicurezza tracciati fino all'evidenza di implementazione |
| **Deployment / Approvazione go-live** | Tutti i risultati Critici rimediati; risultati Elevati rimediati secondo gli obiettivi per classificazione (v. sezione Test di sicurezza); documentazione di passaggio di consegne di sicurezza completa e accettata dalle operazioni; rischi residui formalmente documentati e accettati dall'autorità appropriata |
| **Chiusura** | Lezioni apprese acquisite (obbligatorie per i progetti ad Alto rischio e Rischio medio); nuovi asset registrati nell'inventario degli asset; rischi residui trasferiti al registro dei rischi operativi; documentazione di sicurezza del progetto archiviata secondo i requisiti di gestione dei verbali |

### Tempistiche di escalation

Le preoccupazioni di sicurezza ai gate di fase DEVONO essere escalate entro:

- **2 giorni lavorativi** per i progetti ad Alto rischio.
- **5 giorni lavorativi** per i progetti a Rischio medio.

**Percorso di escalation**: Project manager → Responsabile della sicurezza delle informazioni → RSSI → Direzione generale.

I progetti NON DEVONO procedere alla fase successiva senza risolvere le preoccupazioni di sicurezza Critiche. Le preoccupazioni di sicurezza Elevate possono procedere con l'accettazione formale del rischio da parte dell'autorità appropriata. Le preoccupazioni Medie e Basse possono procedere con un piano di mitigazione documentato.

---

## Test di sicurezza per classificazione

Tutti i progetti DEVONO includere test di sicurezza proporzionali al loro livello di classificazione. I test DEVONO essere completati prima del deployment e i risultati documentati.

### Requisiti di testing

| Requisito | Alto rischio | Rischio medio | Basso rischio |
|-----------|-------------|---------------|---------------|
| **Penetration test esterno** | Obbligatorio (terza parte indipendente, metodologia OWASP o equivalente) | Obbligatorio se rivolto a Internet o che tratta dati regolamentati; altrimenti raccomandato | Non richiesto |
| **Scansione automatizzata delle vulnerabilità** | Obbligatoria (settimanale durante lo sviluppo + finale pre-deployment) | Obbligatoria (scansione finale pre-deployment) | Raccomandata |
| **Revisione del codice di sicurezza** | Obbligatoria per il codice personalizzato (minimo: autenticazione, autorizzazione, protezione dei dati, funzioni crittografiche) | Raccomandata per il codice personalizzato | Non richiesta |
| **Test funzionali di sicurezza** | Obbligatori (autenticazione, autorizzazione, validazione degli input, gestione degli errori, gestione delle sessioni) | Obbligatori (autenticazione, autorizzazione, validazione dei dati, gestione degli errori) | Validazione della sicurezza rispetto alla checklist dei requisiti |

### Obiettivi di remediation prima del deployment

| Gravità del risultato | Progetti ad Alto rischio | Progetti a Rischio medio | Progetti a Basso rischio |
|-----------------------|--------------------------|--------------------------|--------------------------|
| **Critico** | 100% rimediato | 100% rimediato | 100% rimediato |
| **Elevato** | >=80% rimediato | >=70% rimediato | Miglior sforzo; risk-accepted |
| **Medio** | Tracciato; piano di remediation | Tracciato; piano di remediation | Tracciato |
| **Basso** | Documentato | Documentato | Documentato |

Se gli obiettivi di remediation non possono essere raggiunti entro la scadenza del deployment, il rischio residuo DEVE essere formalmente accettato ai sensi della sezione Gestione delle eccezioni della presente politica.

Le evidenze dei test (report di scansione, report di penetration testing, risultati della revisione del codice) DEVONO essere archiviate ai sensi dei requisiti di gestione dei verbali.

---

## Passaggio di consegne e accettazione della sicurezza

Alla chiusura del progetto, la documentazione di passaggio di consegne della sicurezza DEVE essere fornita al team operativo e validata come completa prima che il progetto venga formalmente chiuso. Un passaggio di consegne di sicurezza incompleto blocca la chiusura del progetto.

### Documentazione del passaggio di consegne

Il pacchetto di passaggio di consegne della sicurezza DEVE includere:

1. **Documentazione dell'architettura di sicurezza** — progetto della sicurezza del sistema, confini di fiducia, modello di autenticazione e autorizzazione, implementazione della cifratura, diagrammi del flusso dei dati con classificazione, architettura di rete e segmentazione.

2. **Procedure operative di sicurezza** — requisiti di monitoraggio (fonti di log, soglie di alert, integrazione [SIEM]), procedure di backup e ripristino, approccio alla gestione delle patch di sicurezza, percorsi di escalation della risposta agli incidenti.

3. **Rischi residui accettati** — verbali di accettazione formale del rischio con firme di approvazione, controlli compensativi ove applicabili, calendario di rivalutazione del rischio per le accettazioni a tempo limitato.

4. **Evidenze dei test di sicurezza** — report finale di scansione delle vulnerabilità (datato entro 7 giorni dal deployment), report di penetration test (se applicabile), verbali di remediation per i risultati Critici ed Elevati.

### Accettazione del passaggio di consegne

Il proprietario operativo DEVE confermare la completezza del passaggio di consegne tramite una Checklist di passaggio di consegne della sicurezza firmata prima che il Project manager richieda l'autorizzazione alla chiusura del progetto. Per i progetti ad Alto rischio, il RSSI DEVE approvare anche il passaggio di consegne.

Dopo l'accettazione del passaggio di consegne, il Project manager DEVE garantire che:
- I nuovi asset siano registrati nell'inventario degli asset.
- I rischi residui siano trasferiti al registro dei rischi operativi.
- La documentazione di sicurezza sia archiviata ai sensi dei requisiti di gestione dei verbali.

---

## Ruoli di sicurezza del progetto

### Matrice RACI

| Attività | Project manager | Responsabile InfoSec | RSSI | Business owner | Lead tecnico |
|----------|:-:|:-:|:-:|:-:|:-:|
| Classificazione della sicurezza del progetto | R | A | I | C | C |
| Identificazione dei requisiti di sicurezza | R | A | I | C | C |
| Progettazione dell'architettura di sicurezza | C | C | I | I | R/A |
| Esecuzione dei test di sicurezza | R | C | I | I | R |
| Accettazione del rischio residuo | I | C | A (Alto) | A (Med/Basso) | I |
| Passaggio di consegne della sicurezza alle operazioni | R | A | I | C | C |
| Lezioni apprese | R | C | I | C | C |

R = Responsabile (esegue il lavoro), A = Accountable (decisione finale), C = Consultato (input richiesto), I = Informato (tenuto aggiornato).

### Descrizioni dei ruoli

| Ruolo | Responsabilità chiave |
|-------|----------------------|
| **Direzione generale** | Approvare la presente politica; accettare i rischi residui per i progetti critici; garantire le risorse per la sicurezza dei progetti |
| **RSSI** | Approvare le classificazioni ad Alto rischio; accettare i rischi residui per i progetti ad Alto rischio; bloccare i progetti con rischio di sicurezza inaccettabile; monitorare le metriche di sicurezza dei progetti |
| **Responsabile della sicurezza delle informazioni** | Supportare i team di progetto nella valutazione del rischio e nei requisiti; approvare le classificazioni a Rischio medio; revisionare l'adeguatezza dei test di sicurezza; mantenere i modelli e le checklist di sicurezza |
| **Project manager** | Classificare il rischio di sicurezza del progetto; pianificare e preventivare le attività di sicurezza; eseguire le attività di sicurezza a ogni gate di fase; mantenere il registro dei rischi di sicurezza del progetto; escalare le preoccupazioni di sicurezza |
| **Business owner / Product owner** | Definire i requisiti di sicurezza del business; partecipare alla valutazione del rischio; accettare i rischi residui per i sistemi di proprietà (Rischio medio/Basso) |
| **Lead tecnico / Soluzione Architect** | Progettare i controlli di sicurezza nell'architettura della soluzione; implementare i requisiti di sicurezza; supportare il threat modelling; affrontare i risultati dei test di sicurezza |
| **Fornitori terzi** | Conformarsi ai requisiti di sicurezza contrattuali; partecipare alle valutazioni della sicurezza; segnalare incidenti di sicurezza o vulnerabilità |

### Security Champion (opzionale)

Le organizzazioni con 50 o più dipendenti dovrebbero prendere in considerazione la nomina di Security Champion all'interno dei team di progetto per migliorare l'integrazione della sicurezza e ridurre i colli di bottiglia sul Responsabile della sicurezza delle informazioni:

| Aspetto | Descrizione |
|---------|-------------|
| **Selezione** | Membro del team formato (sviluppatore, business analyst o project manager) che funge da collegamento per la sicurezza all'interno del team di progetto |
| **Formazione** | I Security Champion DEVONO partecipare alla formazione sulla sicurezza (minimo 8 ore all'anno) che copre le pratiche di sviluppo sicuro, l'identificazione delle minacce e le politiche di sicurezza dell'organizzazione |
| **Responsabilità** | Aiutare a identificare i requisiti di sicurezza durante la pianificazione; sostenere la sicurezza all'interno del team di progetto; escalare le preoccupazioni di sicurezza al Responsabile della sicurezza delle informazioni; supportare il coordinamento dei test di sicurezza |
| **Vantaggi** | Riduce i colli di bottiglia sul Responsabile della sicurezza delle informazioni; costruisce la consapevolezza della sicurezza in tutta l'organizzazione; crea sostenitori della sicurezza integrati nei team di progetto |

Il Responsabile della sicurezza delle informazioni DEVE coordinare il programma Security Champion, inclusi i criteri di selezione, il contenuto della formazione e il supporto continuativo.

---

## Integrazione DPIA

Laddove un progetto comporti il trattamento di dati personali, DEVE essere eseguito uno screening della Valutazione d'impatto sulla protezione dei dati (DPIA) all'avvio del progetto per determinare se sia richiesta una DPIA completa.

### Screening DPIA

Uno screening DPIA DEVE essere completato per ogni progetto che tratta dati personali. Lo screening DEVE valutare se il trattamento pianificato sia suscettibile di comportare un elevato rischio per i diritti della personalità o i diritti fondamentali degli individui, come richiesto dalla nLPD svizzera Art. 22.

**Una DPIA è obbligatoria quando il progetto comporta uno dei seguenti elementi:**

- Trattamento esteso di dati personali sensibili (dati sanitari, dati biometrici, opinioni politiche, credenze religiose, precedenti penali o misure di assistenza sociale ai sensi della nLPD Art. 5).
- Monitoraggio sistematico ed esteso degli individui (inclusa la profilazione ai sensi della nLPD Art. 5 lett. f).
- Deployment di nuove tecnologie in cui l'impatto sulla privacy è incerto.
- Processo decisionale automatizzato su larga scala con effetti significativi sugli individui.
- Combinazione o abbinamento di set di dati da fonti diverse in modi che gli individui non si aspetterebbero ragionevolmente.

### Tempistiche della DPIA

- **Screening**: Completato all'avvio del progetto (prima del gate di fase di Pianificazione).
- **DPIA completa** (ove richiesta): Completata durante la fase di pianificazione, prima del gate di fase di esecuzione.
- **Aggiornamento della DPIA**: Richiesto quando l'ambito del progetto, il trattamento dei dati o la tecnologia cambia in modo significativo durante l'esecuzione.

### Approvazione della DPIA

La DPIA completata DEVE essere revisionata dal Delegato alla protezione dei dati (DPD) (o dal RSSI in assenza di un DPD nominato) e approvata prima che il progetto proceda all'esecuzione. Laddove la DPIA identifichi rischi elevati residui che non possono essere mitigati, l'organizzazione DEVE consultare l'Incaricato federale della protezione dei dati e della trasparenza (IFPDT) prima di procedere, come richiesto dalla nLPD Art. 23.

---

## Integrazione con i progetti agili e iterativi

Per i progetti che utilizzano metodologie Agile, Scrum o altre metodologie iterative, la sicurezza DEVE essere integrata nel processo iterativo anziché essere rinviata alla fine.

### Sicurezza nello sviluppo iterativo

| Attività Agile | Integrazione della sicurezza |
|---------------|------------------------------|
| **Refinement del backlog** | User story e criteri di accettazione della sicurezza aggiunti alle user story che coinvolgono dati sensibili, autenticazione, autorizzazione o interfacce esterne |
| **Sprint planning** | Task di sicurezza stimati e inclusi nella capacità dello sprint; user story di sicurezza prioritizzate insieme alle funzionalità di business |
| **Esecuzione dello sprint** | Test di sicurezza automatizzati (SAST, scansione delle dipendenze) integrati nella pipeline CI/CD; risultati di sicurezza trattati come difetti e tracciati nel backlog dello sprint |
| **Sprint review** | Stato della sicurezza riferito insieme ai progressi delle funzionalità; debito tecnico di sicurezza tracciato e prioritizzato |
| **Pianificazione del rilascio** | Requisiti di test di sicurezza (penetration testing, scansione delle vulnerabilità) pianificati prima del rilascio in produzione per classificazione |

### Checkpoint di sicurezza per i progetti iterativi

Anziché singoli gate di fase, i progetti iterativi DEVONO implementare checkpoint di sicurezza nei seguenti punti:

- **Avvio del progetto**: Classificazione della sicurezza, screening DPIA e threat model iniziale (come per i progetti tradizionali).
- **Architecture sprint / Sprint 0**: Revisione dell'architettura di sicurezza; baseline dei requisiti di sicurezza stabilita.
- **Ogni release candidate**: Risultati della scansione di sicurezza automatizzata revisionati; test di sicurezza manuali per i rilasci in produzione.
- **Rilascio in produzione**: Test di sicurezza completi per classificazione; documentazione del passaggio di consegne di sicurezza aggiornata.
- **Chiusura del progetto**: Lezioni apprese finali; rischi residui trasferiti alle operazioni.

---

## Sicurezza nei progetti di approvvigionamento

I progetti che comportano l'approvvigionamento di sistemi IT, software o servizi DEVONO includere i requisiti di sicurezza delle informazioni nel processo di approvvigionamento.

### Requisiti di sicurezza per l'approvvigionamento

- **Valutazione della sicurezza del fornitore**: I fornitori DEVONO essere valutati rispetto ai requisiti di sicurezza dei fornitori dell'organizzazione (ai sensi della Politica di sicurezza nelle relazioni con i fornitori) prima dell'aggiudicazione del contratto.
- **Requisiti di sicurezza nei contratti**: I contratti DEVONO includere requisiti di sicurezza delle informazioni, inclusi obblighi di protezione dei dati, requisiti di notifica degli incidenti, diritti di audit e controlli sui subappaltatori.
- **Criteri di accettazione della sicurezza**: I criteri di accettazione dell'approvvigionamento DEVONO includere la validazione della sicurezza (es. scansione delle vulnerabilità del sistema consegnato, revisione della configurazione di sicurezza, verifica del controllo degli accessi).
- **Accordi di trattamento dei dati**: Laddove il fornitore tratti dati personali per conto dell'organizzazione, DEVE essere eseguito un accordo di trattamento dei dati conforme alla nLPD Art. 9 (e al GDPR Art. 28 ove applicabile) prima dell'inizio del trattamento dei dati.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Progetto** | Un'impresa temporanea con date di inizio e fine definite, intrapresa per creare un prodotto, servizio o risultato unico che coinvolge asset informativi o sistemi informativi |
| **Gate di fase** | Un punto di revisione formale tra le fasi del progetto in cui i criteri di sicurezza devono essere soddisfatti prima che il progetto proceda |
| **Classificazione della sicurezza** | La categorizzazione di un progetto come Alto rischio, Rischio medio o Basso rischio in base ai fattori di impatto sulla sicurezza delle informazioni |
| **Registro dei requisiti di sicurezza** | Un elenco documentato di requisiti di sicurezza per un progetto, tracciato fino all'implementazione e al testing |
| **DPIA (Valutazione d'impatto sulla protezione dei dati)** | Una valutazione strutturata dell'impatto del trattamento pianificato dei dati sulla protezione dei dati personali, richiesta dalla nLPD Art. 22 laddove il trattamento sia suscettibile di comportare un elevato rischio |
| **Threat model** | Un'analisi strutturata delle potenziali minacce a un sistema o a un'applicazione, che identifica i vettori di attacco, gli attori delle minacce e le contromisure necessarie |
| **Rischio residuo** | Il rischio rimanente dopo l'implementazione dei controlli di sicurezza, che deve essere formalmente accettato dall'autorità appropriata |
| **Passaggio di consegne della sicurezza** | Il trasferimento formale della documentazione di sicurezza, delle responsabilità e delle procedure operative dal team di progetto al team operativo alla chiusura del progetto |
| **Security Champion** | Un membro del team formato integrato in un team di progetto che funge da collegamento per la sicurezza, aiutando a identificare i requisiti di sicurezza e a sostenere le best practice di sicurezza |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità relative alla sicurezza delle informazioni nella gestione dei progetti |
|-------|--------------------------------------------------------------------------------------|
| **Direzione generale** | Approvare la presente politica; garantire le risorse organizzative per la sicurezza dei progetti; accettare i rischi residui per i progetti critici; revisionare lo stato della sicurezza dei progetti ad Alto rischio nei riesami della direzione |
| **RSSI** | Approvare le classificazioni ad Alto rischio e l'accettazione dei rischi residui; bloccare o ritardare i progetti con rischio di sicurezza inaccettabile; monitorare le metriche di sicurezza dei progetti; approvare le eccezioni ai requisiti di sicurezza |
| **Responsabile della sicurezza delle informazioni** | Supportare i team di progetto nella valutazione del rischio di sicurezza e nell'identificazione dei requisiti; approvare le classificazioni a Rischio medio; revisionare l'adeguatezza dei test di sicurezza; mantenere modelli e checklist di sicurezza |
| **Project manager** | Classificare il rischio di sicurezza del progetto (con supporto InfoSec); pianificare e preventivare le attività di sicurezza; eseguire le attività di sicurezza a ogni gate di fase; mantenere il registro dei rischi di sicurezza del progetto; preparare la documentazione del passaggio di consegne di sicurezza |
| **Business owner** | Definire i requisiti di sicurezza del business; partecipare alla valutazione del rischio di sicurezza; accettare i rischi residui per i progetti a Rischio medio/Basso; approvare i requisiti di sicurezza come parte dell'ambito del progetto |
| **Lead tecnico** | Progettare i controlli di sicurezza nelle soluzioni; implementare i requisiti di sicurezza; supportare il threat modelling; affrontare i risultati dei test di sicurezza |
| **Delegato alla protezione dei dati (DPD)** | Revisionare e approvare le DPIA; fornire consulenza sui requisiti di protezione dei dati per i progetti; interfacciarsi con l'IFPDT ove richiesto dalla nLPD Art. 23 |

---

## Evidenze

Le seguenti evidenze dimostrano la conformità alla presente politica:

| # | Evidenza | Proprietario | Frequenza |
|---|----------|--------------|-----------|
| 1 | **Verbali di classificazione del progetto** che mostrano la determinazione e l'approvazione della classificazione del rischio di sicurezza per ogni progetto | Project manager | *Per avvio del progetto; archiviati alla chiusura del progetto* |
| 2 | **Registri dei requisiti di sicurezza** (o voci del registro dei rischi per il Basso rischio) che documentano i requisiti di sicurezza identificati e lo stato di implementazione | Project manager | *Per progetto; aggiornati durante il ciclo di vita* |
| 3 | **Verbali di approvazione dei gate di fase** con verifica dei criteri di sicurezza e approvazione | Project manager | *Per gate di fase; archiviati alla chiusura del progetto* |
| 4 | **Report dei test di sicurezza** (penetration test, scansioni delle vulnerabilità, revisioni del codice) per classificazione | Responsabile InfoSec | *Per progetto; report finale entro 7 giorni dal deployment* |
| 5 | **Verbali di remediation dei risultati di sicurezza** che tracciano i risultati fino alla chiusura o all'accettazione del rischio | Project manager | *Per progetto; aggiornati fino alla chiusura* |
| 6 | **Pacchetti di documentazione del passaggio di consegne di sicurezza** accettati dai team operativi | Project manager | *Per chiusura del progetto* |
| 7 | **Verbali di accettazione del rischio residuo** con le appropriate approvazioni per classificazione | RSSI / Business owner | *Per progetto in cui esistono rischi residui* |
| 8 | **Verbali di screening DPIA** (e DPIA completa ove applicabile) per i progetti che trattano dati personali | DPD / RSSI | *Per progetto che coinvolge dati personali* |
| 9 | **Documentazione delle lezioni apprese** per i progetti a Rischio medio e Alto rischio | Project manager | *Per chiusura del progetto* |
| 10 | **Registro delle eccezioni di sicurezza** con approvazioni, controlli compensativi e limiti di tempo | RSSI | *Per eccezione; rivisto trimestralmente* |
| 11 | **Dashboard delle metriche di sicurezza dei progetti** che mostra la distribuzione delle classificazioni, il completamento dei test e le tendenze dei risultati | RSSI | *Mensile; riferito trimestralmente alla Direzione generale* |
| 12 | **Verbali di formazione** per i project manager sull'integrazione dei requisiti di sicurezza | Risorse umane / Responsabile InfoSec | *Annuale; completamento tracciato* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica attraverso vari metodi, inclusi ma non limitati a: audit della classificazione dei progetti, revisioni della conformità ai gate di fase, verifica del completamento dei test di sicurezza, revisioni della documentazione del passaggio di consegne, audit interni ed esterni, e feedback al proprietario della politica.

Le seguenti metriche DEVONO essere tracciate e riferite al RSSI trimestralmente:

| Metrica | Obiettivo | Soglia critica |
|---------|-----------|----------------|
| Progetti classificati entro 5 giorni lavorativi dall'avvio | 100% | <80% |
| Progetti ad Alto/Medio rischio con registro dei requisiti di sicurezza completato | 100% | <90% |
| Test di sicurezza completati prima del deployment | 100% | <90% |
| Risultati di sicurezza Critici rimediati prima del deployment | 100% | <100% (qualsiasi risultato Critico distribuito = critico) |
| Documentazione del passaggio di consegne di sicurezza accettata prima della chiusura del progetto | 100% | <80% |
| Screening DPIA completato per i progetti che trattano dati personali | 100% | <90% |
| Lezioni apprese acquisite per i progetti ad Alto rischio e Rischio medio | 100% | <80% |

### Dashboard delle metriche

Il RSSI DEVE mantenere un dashboard delle metriche di sicurezza dei progetti che fornisca visibilità immediata sulla salute del programma. Il dashboard DEVE includere:

- **Punteggio di conformità complessivo del programma** — aggregato delle sette metriche sopra indicate, calcolato come media ponderata del raggiungimento degli obiettivi.
- **Barre di conformità per metrica** — ogni metrica visualizzata con la percentuale attuale e l'indicatore di stato (verde >= obiettivo, ambra >= soglia critica, rosso < soglia critica).
- **Progetti attivi per classificazione** — conteggio dei progetti attivi ad Alto rischio, Rischio medio e Basso rischio.
- **Elementi di attenzione** — progetti con attività di sicurezza in ritardo o metriche che superano le soglie ambra/rosso.

Il dashboard DEVE essere revisionato al riesame mensile del RSSI e incluso nel report trimestrale della Direzione generale per fornire una visibilità chiara dell'efficacia del programma di sicurezza dei progetti.

**Requisiti di reportistica**:
- **Dashboard mensile RSSI**: Progetti per classificazione e stato della sicurezza (in linea / a rischio / in ritardo); risultati di sicurezza aperti per gravità e anzianità; eccezioni di sicurezza concesse.
- **Report trimestrale alla Direzione generale**: Totale progetti e conteggio dei progetti ad Alto rischio; risultati di sicurezza critici e stato della remediation; tassi di completamento DPIA; incidenti di sicurezza significativi che interessano i progetti.
- **Riesame annuale della direzione**: Efficacia completa del programma di sicurezza dei progetti; tendenze delle metriche; risultati significativi; raccomandazioni di miglioramento.

Le metriche che superano le soglie critiche DEVONO essere segnalate al RSSI per attenzione immediata e riferite al successivo Riesame della direzione.

## Eccezioni

Qualsiasi eccezione alla presente politica DEVE essere approvata e registrata dal RSSI in anticipo, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni ai requisiti di test di sicurezza o ai gate di fase per i progetti ad Alto rischio richiedono l'approvazione congiunta del RSSI e della Direzione generale. Le eccezioni NON DEVONO superare i 90 giorni di calendario senza una nuova valutazione e una nuova approvazione.

## Non conformità

Un dipendente che abbia violato la presente politica può essere soggetto a provvedimenti disciplinari, fino e inclusa la risoluzione del rapporto di lavoro. I progetti distribuiti senza i test di sicurezza o la classificazione richiesti possono essere soggetti a sospensione immediata fino al soddisfacimento dei requisiti di sicurezza. La non conformità DEVE essere segnalata al RSSI e registrata nel registro delle non conformità del SGSI.

## Miglioramento continuo

La presente politica è revisionata e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO considerare i cambiamenti alla metodologia di gestione dei progetti, i risultati degli audit, i cambiamenti normativi (incluse le modifiche alla nLPD), gli incidenti di sicurezza correlati ai progetti, le tendenze delle eccezioni, le lezioni apprese dalle revisioni della sicurezza dei progetti e l'evoluzione del panorama delle minacce. Le non conformità relative alla presente politica DEVONO essere registrate e gestite attraverso il processo di azione correttiva del SGSI (Clausola 10.2) con analisi della causa principale e remediation tracciata.

---

# Aree dello standard ISO 27001 trattate

Politica sulla sicurezza delle informazioni nella gestione dei progetti — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.3 Ruoli, responsabilità e autorità organizzative | **5.8 Sicurezza delle informazioni nella gestione dei progetti** |
| Clausola 6.1 Azioni per affrontare rischi e opportunità | 5.7 Intelligence sulle minacce |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni e pianificazione | 5.9 Inventario delle informazioni e degli altri asset associati |
| Clausola 7.4 Comunicazione | 5.12 Classificazione delle informazioni |
| Clausola 8.1 Pianificazione e controllo operativi | 5.19 Sicurezza delle informazioni nelle relazioni con i fornitori |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | 5.34 Privacy e protezione dei dati personali |
| Clausola 10.2 Non conformità e azioni correttive | 8.25 Ciclo di vita dello sviluppo sicuro |
| | 8.26 Requisiti di sicurezza delle applicazioni |
| | 8.29 Test di sicurezza nello sviluppo e nell'accettazione |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|------------------|-----------|
| nLPD svizzera | Art. 7 — Protezione dei dati fin dalla progettazione e per impostazione predefinita; Art. 8 — Misure tecniche e organizzative; Art. 22 — DPIA per il trattamento ad alto rischio; Art. 23 — Consultazione dell'IFPDT |
| OPDo svizzera | Art. 1-3 — Requisiti minimi per la sicurezza dei dati |
| GDPR dell'UE (ove applicabile) | Art. 25 — Protezione dei dati fin dalla progettazione e per impostazione predefinita; Art. 32 — Sicurezza del trattamento; Art. 35 — Valutazione d'impatto sulla protezione dei dati |
| ISO/IEC 27001:2022 | Controllo Annex A 5.8 — Sicurezza delle informazioni nella gestione dei progetti |
| ISO/IEC 27002:2022 | Sezione 5.8 — Guida all'implementazione per la sicurezza delle informazioni nella gestione dei progetti |
| ISO 21500:2021 | Gestione di progetti, programmi e portfolio — Contesto e concetti |
| NIST SP 800-53 Rev 5 | SA-3 (Ciclo di vita dello sviluppo dei sistemi) — Integrazione della sicurezza durante il ciclo di vita del sistema; PL-2 (Piani di sicurezza e privacy dei sistemi) — Pianificazione della sicurezza per i sistemi |
| NIST CSF 2.0 | GV.RR — Ruoli, responsabilità e autorità; ID.RA — Valutazione del rischio; PR.IP — Processi e procedure di protezione delle informazioni |
| CIS Controls v8 | Controllo 16 (Sicurezza del software applicativo) — Misure di protezione del ciclo di vita dello sviluppo sicuro; Funzione di governance — Politiche e procedure per la protezione degli asset |

---

<!-- QA_VERIFIED: 2026-04-03 -->

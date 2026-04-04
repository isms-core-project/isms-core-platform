<!-- ISMS-CORE:POLICY:ISMS-POL-01-IT:framework:POL:01 -->
**ISMS-POL-01 — Quadro di governance e processo decisionale del SGSI**

---

## Controllo del documento

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Quadro di governance e processo decisionale del SGSI |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-01 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da determinare] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Storico delle versioni**:

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data - 4 settimane] | RSSI | Bozza iniziale — framework dei confini di governance |

**Ciclo di revisione**: Annuale (o in caso di modifiche significative al SGSI)
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondaria: Responsabile legale/conformità
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.1 (Politiche per la sicurezza delle informazioni)
- Dichiarazione di Applicabilità (DdA)
- Piano di trattamento dei rischi (ISO 27001 Clausola 6.1.3)
- Registro di accettazione dei rischi (Clausola 6.1.3d)
- ISO 27001:2022 Clausola 4.1 (Comprensione dell'organizzazione e del suo contesto)
- ISO 27001:2022 Clausola 5.3 (Ruoli, responsabilità e autorità)
- ISO 27001:2022 Clausola 6.1.3 (Trattamento dei rischi per la sicurezza delle informazioni)
- ISO 27001:2022 Clausola 7.5.3 (Controllo delle informazioni documentate)
- ISO 27001:2022 Clausola 9.2 (Audit interno)
- ISO 27001:2022 Clausola 9.3 (Riesame della direzione)
- ISO 27001:2022 Clausola 10.2 (Non conformità e azioni correttive)

**Distribuzione**: Tutte le parti interessate del SGSI, autori di politiche, proprietari di sistemi, revisori interni/esterni
**Referenziato da**: Tutti i documenti di politica del SGSI, Dichiarazione di Applicabilità, Piano di trattamento dei rischi

## Sintesi esecutiva

La presente politica stabilisce **dove viene esercitato il giudizio professionale** nel Sistema di Gestione della Sicurezza delle Informazioni (SGSI) dell'organizzazione, garantendo che:

- **Le decisioni di progettazione del modello siano documentate e autorizzate** (interpretazione dei controlli, applicabilità normativa, accettazione dei rischi)
- **L'autorità decisionale sia chiaramente assegnata** (competenza e ambito del RSSI, dell'ufficio legale/conformità e della Direzione generale)
- **I criteri di conformità evolvano attraverso processi controllati** (modifiche normative, evoluzione delle minacce, feedback degli audit)
- **La verifica dell'audit sia obiettiva e basata su prove** (i revisori verificano il modello documentato, non reinterpretano i requisiti)

**Scopo**: Consentire la **verifica obiettiva dell'audit** spostando il giudizio professionale alla **fase di progettazione del modello** (politiche documentate, valutazioni dei rischi, decisioni di applicabilità) piuttosto che alla **fase di discussione dell'audit** (interpretazione soggettiva durante la certificazione).

**Ambito**: Tutta l'autorità decisionale del SGSI, le determinazioni di applicabilità normativa, la gestione delle eccezioni ai controlli, l'evoluzione dei criteri di conformità e i processi di revisione della governance.

**Principio chiave**: **La certificazione ISO 27001 richiede giudizio professionale in due fasi:**

1. **Progettazione del modello** (responsabilità dell'organizzazione): Interpretare ISO 27001 per il contesto organizzativo, selezionare controlli basati sul rischio, definire la sufficienza delle prove
2. **Verifica del modello** (responsabilità del revisore): Valutare se l'interpretazione organizzativa soddisfa ISO 27001, verificare che l'implementazione corrisponda alla documentazione

La presente politica documenta il giudizio professionale organizzativo (Fase 1) per consentire la verifica obiettiva dell'audit (Fase 2).

---

### Guida rapida

| Ho bisogno di... | Vedi |
|---|---|
| Capire chi decide cosa | Sezione 2.1 (Confini di autorità) |
| Verificare i requisiti di competenza per un ruolo | Sezione 2.3 (Requisiti di competenza) |
| Determinare l'applicabilità normativa | Sezione 3.1 (Applicabilità normativa) → POL-00 |
| Determinare l'applicabilità dei controlli | Sezione 3.2 (Applicabilità dei controlli) → DdA |
| Gestire un disaccordo con un revisore | Sezione 3.3 (Protocollo di contestazione dell'applicabilità) |
| Elaborare un'eccezione a un controllo | Sezione 4.2 (Processo di eccezione — 5 fasi) |
| Monitorare il volume e la salute delle eccezioni | Sezione 4.4 (Monitoraggio del volume delle eccezioni) |
| Gestire una modifica ai criteri di conformità | Sezione 5.2 (Processo di modifica — 6 fasi) |
| Monitorare la rivalutazione dopo una modifica | Sezione 5.4 (Monitoraggio della rivalutazione) |
| Prepararsi per la revisione annuale della governance | Sezione 6.1 (Revisione annuale della governance) |
| Registrare una lezione appresa | Sezione 6.2 (Registro delle lezioni apprese) |
| Preparare la documentazione per un audit | Sezione 9.1 (Documenti forniti ai revisori) |

---

## Autorità di politica e confini di governance

### Scopo e ambito

La presente politica definisce l'**autorità decisionale** per la governance del SGSI, garantendo:

- Chiara assegnazione della responsabilità per l'interpretazione della conformità
- Processi documentati per applicabilità, eccezioni ed evoluzione
- Requisiti di competenza per i decisori
- Criteri oggettivi per la verifica dell'audit

**La presente politica stabilisce:**

- Confini di autorità per le decisioni del SGSI (Sezione 2: chi decide cosa, con quale competenza)
- Autorità di applicabilità normativa e dei controlli (Sezione 3: chi determina cosa si applica)
- Processi di eccezione e accettazione dei rischi (Sezione 4: come vengono gestiti i controlli non implementabili)
- Controllo delle modifiche ai criteri di conformità (Sezione 5: come evolve il modello nel tempo)
- Monitoraggio dell'efficacia della governance (Sezione 6: come viene valutata la qualità della governance)

**La presente politica NON stabilisce:**

- Requisiti specifici di implementazione dei controlli (trattati nelle politiche di controllo dell'Allegato A: serie ISMS-POL-A.X.XX)
- Metodologie di valutazione del rischio (trattate nella Procedura di valutazione del rischio: Clausola 6.1.2)
- Procedure di controllo dei documenti (trattate nella Procedura di controllo dei documenti: Clausola 7.5.3)
- Programma di audit interno (trattato nella Procedura di audit interno: Clausola 9.2)

**Integrazione con ISO 27001**:

- **Clausola 4.1 (Contesto)**: Questa politica supporta la comprensione del contesto esterno (come normative e standard vengono interpretati per il contesto organizzativo)
- **Clausola 5.3 (Ruoli e responsabilità)**: Formalizza la struttura di autorità per il processo decisionale del SGSI
- **Clausola 6.1.3 (Trattamento del rischio)**: Supporta la selezione di controlli basata sul rischio, controlli alternativi e autorità di accettazione del rischio
- **Clausola 7.5.3 (Controllo dei documenti)**: Stabilisce la governance per le modifiche ai criteri di conformità
- **Clausola 9.3 (Riesame della direzione)**: Fornisce il framework per rivedere l'efficacia della governance
- **Clausola 10.1 (Miglioramento continuo)**: Consente il miglioramento del processo di governance tramite le lezioni apprese

## Autorità e competenza

### Autorità decisionale

**Assegnazione dell'autorità**:

I seguenti ruoli esercitano l'autorità decisionale per la governance del SGSI. Ogni ruolo opera all'interno di un **dominio di autorità** definito:

| Dominio di autorità | Ruolo | Ambito decisionale | Requisito di competenza |
|---------------------|-------|-------------------|------------------------|
| **Sicurezza tecnica** | RSSI | Progettazione dei controlli tecnici, fattibilità operativa, sufficienza delle prove, decisioni di implementazione quotidiane | Competenza in sicurezza delle informazioni (CISSP/CISM o equivalente, 5+ anni di esperienza), background tecnico, conoscenza ISO 27001 |
| **Normativo e legale** | Responsabile legale/conformità | Interpretazione dei requisiti normativi, obblighi contrattuali, valutazione del rischio legale, determinazioni di Livello POL-00 | Formazione legale o certificazione di conformità, capacità di monitoraggio normativo, accesso a consulenza legale esterna ove necessario |
| **Protezione dei dati** | Responsabile della Protezione dei Dati (RPD) | Controlli specifici per la privacy (A.5.34, conformità RGPD/LPD svizzera), diritti degli interessati, valutazioni d'impatto sulla privacy. Il RPD esercita autorità indipendente in questo dominio ai sensi dell'Articolo 38.3 del RGPD. | Competenza RGPD/LPD svizzera, certificazione in protezione dei dati (CIPP/E o equivalente), indipendenza ai sensi dell'Articolo 38 RGPD |
| **Strategico e di rischio** | Direzione generale (AD/Consiglio) | Decisioni di rischio strategico, allocazione delle risorse, accettazione del rischio (Clausola 6.1.3d), modifiche all'ambito del SGSI, decisioni architetturali rilevanti | Responsabilità fiduciaria per il rischio organizzativo, responsabilità ultima per la certificazione ISO 27001, autorità di budget |

**Percorso di escalation delle decisioni**:

1. **Decisioni ordinarie** (implementazione tecnica, formato delle prove, progettazione dei controlli):
   - **Autorità**: RSSI
   - **Documentazione**: Documenti POL/IMP, decisioni di progettazione dei controlli

2. **Interpretazione normativa** (applicabilità Livello 1/2 di POL-00, requisiti di conformità contrattuale):
   - **Autorità**: Responsabile legale/conformità (determina l'applicabilità) + RSSI (implementa i controlli)
   - **Documentazione**: Sezione 8 di POL-00 (Matrice di applicabilità normativa)

3. **Accettazione del rischio** (esclusione del controllo senza alternativa, accettazione del rischio residuo ai sensi della Clausola 6.1.3d):
   - **Autorità**: RSSI propone (con valutazione del rischio), Direzione generale approva
   - **Documentazione**: Registro di accettazione dei rischi (requisito di documentazione Clausola 6.1.3d)

4. **Modifiche strategiche** (espansione dell'ambito del SGSI, cambiamento rilevante dell'architettura dei controlli, cambio dell'ente di certificazione):
   - **Autorità**: Approvazione della Direzione generale obbligatoria (il RSSI raccomanda, l'AD/Consiglio decide)
   - **Documentazione**: Verbali del riesame della direzione (Clausola 9.3.3), verbali del Consiglio ove applicabili

**Requisiti obbligatori**:

1. Il RSSI **deve** approvare tutte le implementazioni di controlli tecnici prima del deployment.
2. Il Responsabile legale/conformità **deve** approvare tutte le determinazioni di applicabilità normativa (assegnazioni di Livello POL-00) prima della pubblicazione o dell'aggiornamento di POL-00.
3. La Direzione generale **deve** approvare tutte le decisioni di accettazione del rischio (esclusioni di controlli, accettazione del rischio residuo) ai sensi della Clausola 6.1.3d di ISO 27001.
4. L'escalation delle decisioni **deve** seguire il percorso definito sopra. Le decisioni prese al di fuori dell'autorità designata richiedono approvazione retroattiva o azioni correttive ai sensi della Clausola 10.2.

**Prove dell'esercizio dell'autorità**:

- **Controlli tecnici**: Firme di approvazione sui documenti POL/IMP
- **Applicabilità normativa**: Firme di approvazione sulla Sezione 8 di POL-00
- **Accettazione del rischio**: Firma della Direzione generale nelle voci del Registro di accettazione dei rischi
- **Decisioni strategiche**: Verbali del riesame della direzione (Clausola 9.3) o delibere del Consiglio

### Giudizio professionale nella certificazione ISO 27001

**La certificazione ISO 27001 richiede giudizio professionale in due fasi distinte:**

**Fase 1: Progettazione del modello (Responsabilità dell'organizzazione)**

Il giudizio professionale esercitato dall'organizzazione include:

1. **Interpretazione del contesto** (Clausola 4.1): Determinare quali fattori esterni sono rilevanti per l'ambito del SGSI; documentato in: Documento di contesto organizzativo, POL-00

2. **Selezione dei controlli** (Clausola 6.1.3): Selezionare controlli basati sulla valutazione del rischio; documentato in: Dichiarazione di Applicabilità (DdA), Piano di trattamento dei rischi, documenti POL/IMP dei controlli

3. **Sufficienza delle prove**: Definire cosa dimostra l'efficacia del controllo; documentato in: Documenti IMP dei controlli (sezione prove)

4. **Applicabilità normativa** (POL-00): Determinare quali normative si applicano all'organizzazione; documentato in: Sezione 8 di POL-00 (Matrice di applicabilità normativa)

**Fase 2: Verifica del modello (Responsabilità del revisore)**

Il giudizio professionale esercitato dal revisore include:

1. **Valutazione della qualità del processo**: La metodologia di valutazione del rischio è solida? Le decisioni di selezione dei controlli sono ragionevoli?

2. **Allineamento con ISO 27001**: L'interpretazione organizzativa dei controlli dell'Allegato A soddisfa gli obiettivi di controllo di ISO 27001?

3. **Efficacia dell'implementazione** (Fase 2): L'implementazione effettiva corrisponde al modello documentato?

4. **Miglioramento continuo**: Il SGSI sta evolvendo? I risultati dell'audit interno vengono affrontati?

**Principio di collaborazione**:

Dove il revisore identifica potenziali lacune nel giudizio organizzativo, la risoluzione segue il **Protocollo di contestazione dell'applicabilità della Sezione 3.3**: la discussione si concentra sull'allineamento della clausola ISO 27001 e sul ragionamento documentato, non sull'autorità o il rango.

### Requisiti di competenza per i decisori

| **Ruolo** | **Competenza minima** | **Verifica** |
| --- | --- | --- |
| **RSSI** | - Certificazione in sicurezza delle informazioni (CISSP, CISM o equivalente) - 5+ anni di esperienza - Background tecnico - Conoscenza ISO 27001 | - CV che documenta l'esperienza - Certificazioni professionali (attuali) - Documentazione di formazione ISO 27001 |
| **Responsabile legale/conformità** | - Formazione legale o certificazione di conformità (CCEP, CRCM) - Capacità di monitoraggio normativo - Esperienza di revisione contrattuale | - Credenziali legali o certificazioni di conformità - Registri di coinvolgimento di consulenza legale esterna |
| **RPD** | - Competenza RGPD/LPD svizzera (CIPP/E, CIPM o equivalente) - Indipendenza dalla direzione operativa (ai sensi dell'Art. 38.3 RGPD) | - Certificazioni in protezione dei dati - Organigramma che mostra la linea di riporto (verifica dell'indipendenza) |
| **Direzione generale** | - Responsabilità fiduciaria per il rischio organizzativo (AD, DF, Consiglio) - Comprensione delle implicazioni della certificazione ISO 27001 - Autorità per l'allocazione del budget | - Verifica del ruolo (contratto di lavoro, nomina del consiglio) - Briefing esecutivo ISO 27001 (registrato nel riesame della direzione) |

---

## Autorità di applicabilità della conformità

### Applicabilità normativa

**Framework**: L'applicabilità normativa è determinata ai sensi di **ISMS-POL-00 (Quadro di applicabilità normativa)**, che stabilisce:

- **Livello 1 (Obbligatorio)**: Obblighi legali o contrattuali (LPD svizzera, RGPD ove applicabile, ISO 27001:2022 per la certificazione)
- **Livello 2 (Condizionale)**: Requisiti che si applicano solo quando si verificano trigger specifici (DORA, NIS2, PCI DSS, FINMA, AI Act UE)
- **Livello 3 (Informativo)**: Buone pratiche volontarie e orientamenti tecnici (serie NIST SP 800, CIS Controls, OWASP)

**Autorità decisionale**:

1. **Determinazione del Livello**: Il Responsabile legale/conformità determina l'applicabilità normativa ai sensi della Sezione 5 di POL-00
2. **Implementazione dei controlli**: Il RSSI implementa i controlli per soddisfare le normative applicabili
3. **Approvazione**: La Direzione generale approva annualmente la Matrice di applicabilità normativa di POL-00

**Ciclo di revisione**:

- **Monitoraggio trimestrale** (Sezione 4.3 di POL-00): Responsabile legale/conformità + RSSI esaminano le modifiche normative
- **Revisione annuale completa** (Sezione 7 di POL-00): Approvazione della Direzione generale
- **Rivalutazione avviata** (Sezione 5 di POL-00): Espansione aziendale, modifiche normative, requisiti dei contratti con i clienti

### Applicabilità dei controlli (Allegato A di ISO 27001)

**Framework**: L'applicabilità dei controlli è determinata ai sensi della **Clausola 6.1.3 di ISO 27001 (Trattamento del rischio)**, che richiede:

- Selezione dei controlli basata sul rischio
- Documentazione della Dichiarazione di Applicabilità (DdA) (tutti i 93 controlli dell'Allegato A documentati con stato di implementazione e giustificazione)
- Decisioni di trattamento del rischio (implementare il controllo, controllo alternativo, accettare il rischio ai sensi della Clausola 6.1.3d)

**Criteri per le decisioni di applicabilità dei controlli**:

| Stato | Criteri | Esempio | Documentazione richiesta |
|-------|---------|---------|--------------------------|
| **Applicabile** | Il rischio esiste, il controllo mitiga il rischio, l'implementazione è fattibile | A.8.15 (Registrazione): L'organizzazione gestisce server, la registrazione è necessaria per il rilevamento degli incidenti | POL-A.8.15 + IMP-A.8.15 + cartella di lavoro |
| **Non applicabile** | Il rischio non esiste per il contesto organizzativo | A.8.23 (Filtraggio web): L'infrastruttura è solo server, nessuna navigazione web degli utenti | Giustificazione DdA: «Nessun servizio di navigazione web fornito agli utenti; obiettivo del controllo non applicabile.» + valutazione del rischio |
| **Controllo alternativo** | Il controllo standard non è fattibile, un'alternativa raggiunge lo stesso obiettivo | A.7.4 (Sorveglianza fisica): Infrastruttura in colocation, CCTV gestito dal fornitore per contratto | Giustificazione DdA: «Sorveglianza fisica implementata tramite contratto con il provider colocation. Raggiunge lo stesso obiettivo.» + riferimento alla clausola contrattuale |
| **Rischio accettato** | Il rischio esiste, il controllo non è implementato, il rischio residuo è accettato dalla Direzione generale | A.8.11 (Mascheramento dei dati): Dati di produzione utilizzati nello sviluppo (limitazione tecnica), rischio residuo accettato con controlli compensativi | Giustificazione DdA + voce del Registro di accettazione dei rischi con firma della Direzione generale |

### Protocollo di contestazione dell'applicabilità

**Scopo**: Processo strutturato per risolvere i disaccordi sulle determinazioni di applicabilità tra l'organizzazione e il revisore.

**Quando si applica questo protocollo**:

- Il revisore mette in discussione la determinazione di applicabilità normativa
- Il revisore contesta l'esclusione di un controllo
- Il revisore ritiene che un controllo alternativo non raggiunga l'obiettivo ISO 27001

**Fasi del protocollo**:

**Fase 1: Il revisore solleva la preoccupazione** — Documenta la preoccupazione specifica, quale determinazione è messa in discussione, quale prova suggerisce che la determinazione potrebbe essere errata.

**Fase 2: L'organizzazione fornisce la documentazione** — Fornisce la motivazione documentata: per l'applicabilità normativa (valutazione ai sensi della Sezione 5 di POL-00, documentazione dei trigger, documentazione di approvazione); per l'esclusione del controllo (valutazione del rischio, giustificazione DdA, documentazione del contesto organizzativo).

**Fase 3: Valutazione collaborativa** — Organizzazione e revisore valutano: La motivazione documentata è ragionevole dato il contesto organizzativo? Esistono prove contraddittorie? L'interpretazione soddisfa i requisiti ISO 27001?

**Fase 4: Risoluzione**:

- **Esito A**: Il revisore accetta la motivazione → La determinazione rimane invariata, nessun risultato emesso
- **Esito B**: L'organizzazione riconosce la lacuna → L'organizzazione avvia azioni correttive ai sensi della Clausola 10.2
- **Esito C**: Il disaccordo persiste → Escalation alla revisione tecnica dell'ente di certificazione

**Principi**:

- **Basato sulle prove**: I disaccordi vengono risolti attraverso il ragionamento documentato e i riferimenti ISO 27001, non attraverso l'autorità o il rango
- **Collaborativo**: L'obiettivo è la comprensione condivisa dei requisiti ISO 27001, non un dibattito conflittuale
- **Orientato al miglioramento**: Se una determinazione di applicabilità era genuinamente errata, l'organizzazione apprende e migliora (miglioramento continuo Clausola 10.1)

---

## Gestione delle eccezioni e accettazione dei rischi

### Scenari di eccezione

**Definizione**: Un'eccezione si verifica quando un controllo dell'Allegato A di ISO 27001 non può essere implementato come documentato nella politica di controllo (POL-A.X.XX), richiedendo un approccio alternativo o l'accettazione del rischio.

**Scenari di eccezione comuni**:

| Scenario | Descrizione | Esempio | Percorso di risoluzione |
|----------|-------------|---------|------------------------|
| **Infeasibilità tecnica** | Il controllo presuppone una tecnologia/architettura non presente | A.8.22 (Segregazione di rete): Infrastruttura con rete piatta per scelta progettuale | Controllo alternativo: Implementare isolamento basato su host, controlli di accesso a livello applicativo |
| **Costo sproporzionato** | Il costo del controllo supera il beneficio della riduzione del rischio | A.8.16 (Deployment SIEM): Infrastruttura con 3 server, la revisione manuale dei log raggiunge lo stesso obiettivo a costo inferiore | Controllo alternativo: Processo documentato di revisione manuale dei log con frequenza definita |
| **Rischio già mitigato** | Un'implementazione alternativa raggiunge lo stesso obiettivo | A.8.5 (AMF per tutti gli account): Gli account di servizio usano autenticazione basata su certificato (funzionalmente equivalente all'AMF) | Controllo alternativo: Autenticazione con certificato documentata come equivalente all'AMF |
| **Vincolo normativo** | L'implementazione del controllo violerebbe un requisito legale di priorità superiore | A.8.10 (Cancellazione dei dati): Il RGPD richiede la cancellazione, ma la legge svizzera richiede 10 anni di conservazione per i documenti finanziari | Accettazione del rischio: Documentare l'obbligo legale che prevale sul controllo, implementare la segregazione dei dati per minimizzare l'ambito |
| **Vincolo di risorse** | L'organizzazione non ha la capacità di implementare il controllo completamente (stato temporaneo) | A.6.3 (Formazione annuale sulla sicurezza): Programma di formazione progettato ma non ancora erogato a tutto il personale | Implementazione differita: Controllo pianificato per il completamento entro [scadenza], misure provvisorie documentate |

### Processo di eccezione

**Processo obbligatorio in 5 fasi** (ai sensi della Clausola 6.1.3 di ISO 27001):

**Fase 1: Documentare il motivo**

- **Spiegazione tecnica**: Perché il controllo non può essere implementato come scritto
- **Valutazione dell'impatto**: Quale obiettivo di sicurezza non è pienamente raggiunto
- **Giustificazione del contesto**: Perché esiste questa limitazione

**Fase 2: Valutare il rischio residuo** (Clausola 6.1.2 di ISO 27001)

- **Probabilità**: Probabilità che la minaccia sfrutti la vulnerabilità
- **Impatto**: Conseguenza se la minaccia si materializza (impatto su Riservatezza/Integrità/Disponibilità)
- **Livello di rischio residuo**: Valutazione del rischio combinata
- **Confronto con la propensione al rischio**: Il rischio residuo è nell'ambito della propensione accettabile?

**Fase 3: Proporre una soluzione**

Selezionare uno dei tre percorsi:

- **Opzione A: Controllo alternativo** — Implementare un controllo diverso che raggiunga lo stesso obiettivo ISO 27001; documentare la mappatura degli obiettivi e le prove di efficacia
- **Opzione B: Accettazione del rischio** (Clausola 6.1.3d) — Accettare il rischio residuo senza ulteriori misure; richiede approvazione della Direzione generale
- **Opzione C: Implementazione differita** — Controllo pianificato per implementazione futura (eccezione temporanea); richiede scadenza documentata e misure provvisorie

**Fase 4: Ottenere l'approvazione** (ai sensi della Sezione 2.1)

| Soluzione | Autorità di approvazione |
|-----------|-------------------------|
| **Controllo alternativo** | RSSI |
| **Accettazione del rischio** | Direzione generale (AD/DF) |
| **Implementazione differita** | RSSI (scadenza) + Direzione generale (rischio residuo durante il periodo di differimento) |

**Fase 5: Documentare nella Dichiarazione di Applicabilità**

Aggiornare la DdA con: Stato del controllo, Giustificazione (sintesi delle fasi 1-3), Approvazione (riferimento all'autorità e alla data), Data della prossima revisione.

### Registro delle eccezioni

**Scopo**: Monitoraggio centralizzato di tutte le eccezioni all'implementazione dei controlli.

**Mantenuto da**: RSSI (proprietario), aggiornato man mano che le eccezioni vengono elaborate.

**Contenuti**:

| Campo | Descrizione |
|-------|-------------|
| ID eccezione | Identificativo univoco (ECC-AAAA-NNN) |
| Controllo | Riferimento al controllo dell'Allegato A |
| Motivo | Perché è richiesta l'eccezione (Fase 1) |
| Rischio residuo | Livello di rischio senza il controllo (Fase 2) |
| Soluzione | Controllo alternativo / Accettazione del rischio / Differimento (Fase 3) |
| Approvato da | Autorità ai sensi della Sezione 2.1 (Fase 4) |
| Data di approvazione | Data dell'approvazione |
| Data di revisione | Prossima data di revisione dell'eccezione |
| Stato | Aperto / Risolto / Chiuso |

### Monitoraggio del volume delle eccezioni

**Obiettivi**:

| Metrica | Obiettivo | Soglia di escalation | Azione se supera la soglia |
|---------|----------|---------------------|---------------------------|
| **Eccezioni totali** | < 5% dei controlli totali (4-5 eccezioni su 93 controlli) | > 10% (10+ eccezioni) | Revisione della Direzione generale: l'ambito del SGSI è realistico? Le risorse sono sufficienti? |
| **Accettazioni del rischio** (senza controllo alternativo) | < 3% dei controlli totali | > 5% (5+ accettazioni del rischio) | Rivalutazione della propensione al rischio |
| **Implementazioni differite** | < 2% dei controlli totali | > 5% o qualsiasi differimento > 180 giorni scaduto | Revisione dell'allocazione delle risorse |
| **Eccezioni in attesa > 90 giorni** | 0 | Qualsiasi eccezione non risolta > 90 giorni | Escalation alla Direzione generale |

---

## Controllo delle modifiche ai criteri di conformità

### Trigger di modifica

**Trigger di modifica esterni**:

| Categoria di trigger | Descrizione | Metodo di rilevamento |
|---------------------|-------------|----------------------|
| **Modifiche normative** | Nuove leggi, normative o orientamenti ufficiali | Monitoraggio trimestrale POL-00 (Sezione 4.3), allerte del consulente legale |
| **Revisioni degli standard** | ISO 27001 o standard correlati aggiornati | Monitoraggio delle pubblicazioni ISO, notifiche dell'ente di certificazione |
| **Modifiche contrattuali** | I contratti con i clienti aggiungono nuovi requisiti | Processo di revisione contrattuale (legale + RSSI prima della firma) |
| **Evoluzione del panorama delle minacce** | Nuove classi di attacchi richiedono aggiornamenti dei controlli | Monitoraggio dell'intelligence sulle minacce (A.5.7), analisi delle tendenze degli incidenti |
| **Modifiche tecnologiche** | Cambiamenti nell'infrastruttura o nell'architettura che influenzano l'implementazione dei controlli | Processo di gestione dei cambiamenti IT, decisioni del comitato di revisione architetturale |

**Trigger di modifica interni**:

| Categoria di trigger | Descrizione | Metodo di rilevamento |
|---------------------|-------------|----------------------|
| **Risultati dell'audit** | Il revisore esterno identifica una lacuna nel controllo o un problema di interpretazione | Registro dei risultati dell'audit (Clausola 10.2), revisione del rapporto di audit |
| **Scoperte dell'audit interno** | L'audit interno (Clausola 9.2) identifica una non conformità | Rapporti di audit interno, registro delle non conformità |
| **Incidenti di sicurezza** | La risposta agli incidenti rivela una debolezza del controllo | Processo di risposta agli incidenti (A.5.24-28), lezioni apprese (Sezione 6.2) |
| **Riesame della direzione** | Il riesame della direzione (Clausola 9.3) identifica un miglioramento strategico | Verbali del riesame della direzione, azioni di miglioramento continuo |
| **Miglioramento continuo** | Identificazione proattiva di opportunità di efficienza | Riunioni di revisione del SGSI, valutazione tecnologica |

### Processo di valutazione e implementazione delle modifiche

**Processo obbligatorio in 6 fasi**:

**Fase 1: Modifica identificata** — Evento trigger rilevato ai sensi delle fonti della Sezione 5.1.
**Output**: Voce nel Registro dei trigger di modifica che documenta l'evento trigger.

**Fase 2: Impatto valutato** — Valutare l'ambito e le implicazioni della modifica:
- Quali politiche/controlli sono interessati?
- Quale lacuna di conformità esiste?
- Quale rimedio è necessario?
- Qual è il rischio durante la transizione?

**Fase 3: Proposta di modifica documentata** — Formalizzare la raccomandazione di modifica con: motivazione, controlli interessati, piano di implementazione, rischio durante la transizione, piano di verifica.

**Fase 4: Approvazione ottenuta** (ai sensi della Sezione 2.1):

| Tipo di modifica | Autorità di approvazione |
|-----------------|--------------------------|
| **Modifiche tecniche** | RSSI |
| **Modifiche normative** (spostamento dell'applicabilità Livello 1/2) | RSSI + Responsabile legale/conformità (congiunto) |
| **Modifiche strategiche** | Approvazione della Direzione generale |
| **Modifiche di emergenza** | RSSI (implementazione immediata) + Direzione generale (approvazione retroattiva entro 7 giorni) |

**Fase 5: Implementazione eseguita** — Eseguire la modifica per: aggiornamenti delle politiche, rivalutazione dei controlli, rigenerazione delle prove, aggiornamento del registro delle modifiche.

**Fase 6: Verifica completata** — Confermare che la modifica sia stata implementata correttamente tramite audit interno, chiusura delle lacune, riesame della direzione.

### Controllo delle versioni e monitoraggio delle modifiche

**Standard di versioning dei documenti**:

Tutte le politiche del SGSI **devono** seguire il versioning standardizzato: formato `v[Maggiore].[Minore]`

| Tipo di modifica | Incremento versione | Trigger |
|-----------------|--------------------|---------| 
| **Versione maggiore** | Incrementa il numero maggiore, azzera il minore (es. v1.3 → v2.0) | Modifica sostanziale al requisito che influenza la valutazione della conformità |
| **Versione minore** | Incrementa il numero minore (es. v1.3 → v1.4) | Chiarimento, formattazione, o modifica non sostanziale |

**Registro centrale delle modifiche del SGSI**: Unica fonte di verità per tutte le modifiche ai criteri di conformità dell'intero SGSI.

### Monitoraggio della rivalutazione

Quando i criteri di conformità cambiano, i controlli interessati devono essere rivalutati per confermare che soddisfino i nuovi requisiti.

**Obiettivi di completamento della rivalutazione**:

| Metrica | Obiettivo | Soglia di escalation |
|---------|----------|---------------------|
| **Tasso di completamento della rivalutazione** | > 95% entro 90 giorni | < 80% → Revisione della Direzione generale |
| **Rivalutazioni scadute** | 0 elementi > 90 giorni scaduti | Qualsiasi elemento > 90 giorni → Escalation alla Direzione generale |
| **Verifiche fallite** | < 5% | > 10% verifiche fallite → Revisione del processo |

---

## Monitoraggio dell'efficacia della governance

### Revisione annuale della governance

**Frequenza**: Annuale (allineata con il Riesame della direzione di ISO 27001 Clausola 9.3)

**Partecipanti**: Direzione generale (AD/DF), RSSI, Responsabile legale/conformità, Audit interno, Rappresentanti dei proprietari dei controlli

**Argomenti della revisione**:

1. **Confini di autorità** (Sezione 2.1): I ruoli e le responsabilità sono chiaramente compresi? I processi di escalation funzionano?

2. **Framework di applicabilità** (Sezione 3): Il framework Livello 1/2/3 di POL-00 è efficace? I trigger delle normative condizionali sono monitorati adeguatamente?

3. **Gestione delle eccezioni** (Sezione 4): Quante eccezioni sono state elaborate nel corso dell'anno? Il volume è nella norma o indica un problema sistematico?

4. **Gestione delle modifiche** (Sezione 5): Quante modifiche ai criteri di conformità ci sono state? Il tasso di completamento della rivalutazione è > 95%?

5. **Feedback dei revisori** (Sezione 6.1): Cosa hanno commentato i revisori esterni sulla governance? Sono state contestate delle interpretazioni?

6. **Efficienza della governance** (Sezione 6.1): I processi di governance sono efficienti? Ci sono colli di bottiglia burocratici?

### Registro delle lezioni apprese

**Scopo**: Catturare i miglioramenti dall'esecuzione del processo di governance, consentendo il miglioramento continuo (Clausola 10.1 di ISO 27001).

**Trigger di aggiornamento**: Processo di governance eseguito con esito imprevisto, contestazione del revisore che rivela una lacuna nella documentazione, feedback interno dei proprietari dei controlli, buona pratica identificata da fonti esterne.

---

## Integrazione con i processi del SGSI

### Valutazione e trattamento del rischio (Clausola 6)

- La metodologia di valutazione del rischio informa le decisioni di selezione dei controlli (documentate nella DdA ai sensi della Sezione 3.2)
- Il piano di trattamento del rischio documenta l'approccio all'implementazione dei controlli, i controlli alternativi (Sezione 4.2) e le accettazioni del rischio (Sezione 4.2 Fase 3 Opzione B)
- Il RSSI propone il trattamento del rischio, la Direzione generale approva l'accettazione del rischio ai sensi della Clausola 6.1.3d

### Audit interno (Clausola 9.2)

- Il programma di audit interno include la verifica della conformità al processo di governance
- Gli audit pre-certificazione verificano che la documentazione di governance sia aggiornata
- Quando i criteri di conformità cambiano (Sezione 5.2), i controlli modificati vengono aggiunti al successivo ambito di audit interno

### Riesame della direzione (Clausola 9.3)

**Input del riesame della direzione** (Clausola 9.3.2) — Contributi della governance:
- Riepilogo del registro delle modifiche (Sezione 5.3)
- Risultati dell'audit relativi alla governance (Sezione 6.1 argomento 5)
- Lezioni apprese (Sezione 6.2), miglioramenti dei processi di governance
- Efficacia della governance: risultati della revisione annuale, metriche del volume delle eccezioni

**Output del riesame della direzione** (Clausola 9.3.3) — Decisioni di governance:
- Approvazione delle accettazioni del rischio ai sensi della Sezione 4.2 Fase 4
- Approvazione delle modifiche strategiche ai sensi del percorso di escalation della Sezione 2.1
- Allocazione delle risorse per la chiusura delle lacune, azioni di miglioramento della governance

### Non conformità e azioni correttive (Clausola 10.2)

**Trigger di non conformità relativi alla governance**:
- Processo di governance non seguito
- Il risultato dell'audit rivela una lacuna di interpretazione
- L'incidente rivela una debolezza del controllo che richiede un aggiornamento della politica

---

## Prove per questa politica

### Fase 1 (Revisione documentale)

- Questo documento di politica (ISMS-POL-01)
- Firme di approvazione dal RSSI, dal responsabile legale/conformità e dalla Direzione generale
- Struttura di governance documentata (Sezione 2.1 — tabella dei confini di autorità)
- Requisiti di competenza definiti (Sezione 2.3)
- Processo di gestione delle eccezioni documentato (Sezione 4.2 — processo in 5 fasi)
- Processo di gestione delle modifiche documentato (Sezione 5.2 — processo in 6 fasi)
- Processo di revisione annuale definito (Sezione 6.1)

### Fase 2 (Efficacia operativa)

- Prove di competenza per i decisori (certificazioni, documentazione della formazione)
- Registri di monitoraggio trimestrale di POL-00 (4 trimestri)
- DdA con giustificazioni per tutti i 93 controlli
- Registro delle eccezioni con documentazione del processo in 5 fasi
- Registro centrale delle modifiche del SGSI
- Verbali del riesame della direzione
- Rapporto della revisione annuale della governance

### Cartella di lavoro di valutazione della conformità

**Cartella di lavoro di valutazione della conformità della governance**: ISMS-CHK-POL-01

**Domini di valutazione**:

- **Dominio 1**: Confini di autorità (Sezione 2)
- **Dominio 2**: Decisioni di applicabilità (Sezione 3)
- **Dominio 3**: Gestione delle eccezioni (Sezione 4)
- **Dominio 4**: Gestione delle modifiche (Sezione 5)
- **Dominio 5**: Revisione della governance (Sezione 6)

---

## Preparazione all'audit e pacchetto di documentazione

### Documenti forniti ai revisori

**Audit Fase 1** (Revisione documentale):

- ISMS-POL-01 (questa politica)
- ISMS-POL-00 (Quadro di applicabilità normativa)
- Dichiarazione di Applicabilità (DdA)
- Piano di trattamento dei rischi (Clausola 6.1.3)
- Registro di accettazione dei rischi (Clausola 6.1.3d)
- Documento di contesto organizzativo (Clausole 4.1/4.2)
- Registro centrale delle modifiche del SGSI (Sezione 5.3)

**Audit Fase 2** (Verifica dell'implementazione):

- Cartella di lavoro di valutazione della conformità della governance (ISMS-CHK-POL-01)
- Registro delle eccezioni (Sezione 4.3)
- Registri di monitoraggio trimestrale di POL-00 (4 trimestri)
- Rapporti di audit interno (Clausola 9.2)
- Verbali del riesame della direzione (Clausola 9.3)
- Rapporto della revisione annuale della governance (Sezione 6.1)
- Registro delle lezioni apprese (Sezione 6.2)
- Documentazione di verifica della competenza (Sezione 2.3)

---

## Dichiarazione conclusiva

La presente politica stabilisce **dove viene esercitato il giudizio professionale** nel SGSI dell'organizzazione, consentendo:

**Verifica obiettiva dell'audit**: La conformità viene valutata rispetto alle decisioni organizzative documentate, non alla discrezione del revisore.

**Chiara autorità decisionale**: I ruoli (RSSI, Responsabile legale/conformità, Direzione generale) hanno confini di autorità espliciti con requisiti di competenza.

**Evoluzione controllata**: I criteri di conformità cambiano attraverso un processo documentato in 6 fasi con monitoraggio della rivalutazione, verifica e approvazione.

**Relazione di audit collaborativa**: Il giudizio del revisore si concentra sulla verifica della qualità del giudizio organizzativo, non sulla sostituzione delle decisioni organizzative.

---

**Il cambiamento di paradigma:**

**SGSI tradizionale**: Giudizio professionale esercitato durante l'audit (il revisore interpreta i requisiti, l'organizzazione si difende a posteriori)

**Questo SGSI**: Giudizio professionale esercitato durante la progettazione del modello (l'organizzazione documenta l'interpretazione, il revisore verifica la qualità e l'allineamento ISO 27001)

**Risultato**: L'audit diventa una verifica oggettiva del modello documentato, non una contestazione di interpretazione soggettiva.

---

**FINE DI ISMS-POL-01-IT**

<!-- QA_VERIFIED: 2026-04-03 -->

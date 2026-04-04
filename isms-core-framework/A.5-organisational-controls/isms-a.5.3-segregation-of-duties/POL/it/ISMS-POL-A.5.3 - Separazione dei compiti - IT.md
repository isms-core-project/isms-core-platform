<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.3-IT:framework:POL:a.5.3 -->
**ISMS-POL-A.5.3 — Separazione dei compiti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Separazione dei compiti |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.3 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI | Politica iniziale per la certificazione ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Direttore Finanziario (DF)
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.15-16-18 (Gestione delle identità e degli accessi)
- ISMS-POL-A.8.2-3-5 (Autenticazione e accesso privilegiato)
- ISMS-IMP-A.5.3.1-UG/TG (Valutazione della matrice SdC)
- ISMS-IMP-A.5.3.2-UG/TG (Analisi dei conflitti)
- ISMS-IMP-A.5.3.3-UG/TG (Mappatura ruoli-funzioni)
- ISO/IEC 27001:2022 Controllo A.5.3

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la separazione dei compiti al fine di ridurre il rischio di frodi, errori e attività non autorizzate, garantendo che le responsabilità in conflitto siano separate tra individui o sistemi diversi.

**Perimetro**: Questa politica si applica a tutti i processi aziendali, i sistemi informativi e le attività in cui i compiti in conflitto potrebbero portare a frodi, errori o violazioni della sicurezza se eseguiti da un singolo individuo.

**Scopo**: Definire i requisiti organizzativi per la separazione dei compiti. Questa politica stabilisce COSA è richiesto in termini di separazione e CHI è responsabile. Le procedure di attuazione (COME) sono documentate separatamente in ISMS-IMP-A.5.3 (varianti UG/TG).

**Allineamento normativo**: Questa politica affronta i requisiti di conformità obbligatori per ISMS-POL-00, inclusi CO svizzero, ISO/IEC 27001:2022 e RGPD dell'UE. I requisiti settoriali condizionali (FINMA, SOX, PCI DSS v4.0.1) si applicano dove le attività aziendali di [Organizzazione] ne determinano l'applicabilità.

---

## Allineamento sul controllo

**ISO/IEC 27001:2022 Allegato A.5.3 — Separazione dei compiti**

> *I compiti in conflitto e le aree di responsabilità in conflitto devono essere separati.*

**Obiettivo del controllo**: Ridurre il rischio di frodi, errori e aggiramento dei controlli di sicurezza delle informazioni separando i compiti in conflitto.

**Tipo di controllo**: Preventivo
**Categoria del controllo**: Organizzativo

**Questa politica affronta**: Identificazione dei compiti in conflitto che richiedono separazione; principi e requisiti di separazione per tipo di processo; controlli compensativi per i team ridotti; gestione delle eccezioni e processi di approvazione; requisiti di monitoraggio e verifica.

---

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Applicabilità | Requisiti chiave |
|-----------|---------------|-----------------|
| **CO svizzero Art. 728** | Tutte le entità svizzere | Sistema di controllo interno inclusa la separazione dei compiti |
| **ISO/IEC 27001:2022** | Ambito di certificazione | Controllo A.5.3 — Separazione dei compiti |

**Livello 2 — Applicabilità condizionale** (dove le attività aziendali di [Organizzazione] ne determinano l'applicabilità):

| Normativa | Condizione scatenante | Requisiti di separazione |
|-----------|----------------------|--------------------------|
| **RGPD dell'UE Art. 32** | Elaborazione di dati personali UE | Misure tecniche e organizzative appropriate |
| **FINMA** | Istituto finanziario svizzero regolamentato | Separazione rigorosa nel trading, liquidazione, gestione del rischio |
| **SOX Sezione 404** | Società quotata negli USA | Separazione dei controlli finanziari, attestazione del controllo interno |
| **PCI DSS v4.0.1** | Elaborazione di carte di pagamento | Requisito 6.4.2 — Separazione sviluppo/test/produzione |

**Livello 3 — Riferimento informativo**: Quadro di controllo interno COSO; ISACA COBIT; NIST SP 800-53 (AC-5); Standard internazionali IIA.

---

# Enunciati di politica

## Principi di separazione

Tutti i processi aziendali e i sistemi informativi DEVONO implementare la separazione dei compiti dove:

**Requisito basato sul rischio**:

- Le attività comportano transazioni finanziarie **superiori a CHF 10.000**, a meno che una soglia inferiore non sia definita in una procedura specifica del dipartimento approvata dal DF e dal RSSI sulla base del rischio
- È richiesto l'accesso a informazioni sensibili o classificate
- Vengono esercitati privilegi di amministrazione di sistema
- I controlli di sicurezza possono essere aggirati o disabilitati
- I log di audit o le prove possono essere modificati o eliminati

**Standard minimi di separazione**:

| Tipo di processo | Separazione minima |
|----------------|-------------------|
| Transazioni finanziarie >CHF 10.000 | Iniziatore ≠ Approvatore |
| Richieste di accesso al sistema | Richiedente ≠ Approvatore ≠ Provisioner |
| Gestione dei cambiamenti | Sviluppatore ≠ Tester ≠ Deployer |
| Monitoraggio della sicurezza | Amministratore ≠ Revisore dei log |
| Backup/Ripristino | Operatore ≠ Verificatore |

## Identificazione dei compiti in conflitto

Le seguenti combinazioni di compiti DEVONO essere separate:

**Processi finanziari**:

- Avvio dei pagamenti E approvazione dei pagamenti
- Creazione di record dei fornitori E elaborazione dei pagamenti ai fornitori
- Registrazione delle transazioni E riconciliazione dei conti
- Gestione delle buste paga E approvazione dei pagamenti delle buste paga

**Operazioni IT**:

- Sviluppo del codice E dispiegamento in produzione
- Amministrazione dei sistemi E revisione dei log di sistema
- Creazione di account utente E approvazione delle richieste di accesso
- Gestione dei backup E autorizzazione del ripristino dei dati
- Configurazione dei controlli di sicurezza E audit dell'efficacia della sicurezza

**Appalti e contratti**:

- Selezione dei fornitori E negoziazione dei contratti
- Approvazione degli acquisti E ricezione di beni/servizi
- Gestione dei contratti E verifica della conformità contrattuale

**Risorse umane**:

- Decisioni di assunzione E verifica del casellario giudiziale
- Definizione della retribuzione E approvazione delle buste paga
- Cessazione dell'accesso E conferma della revoca dell'accesso

## Considerazioni per i team ridotti

Dove la separazione non può essere ottenuta a causa di personale limitato:

**Controlli compensativi richiesti**:

1. Monitoraggio e registrazione avanzati di tutte le attività
2. Revisione da parte della direzione di tutte le transazioni (minimo settimanale)
3. Revisione periodica indipendente (minimo trimestrale)
4. Avvisi automatici per schemi insoliti
5. Piste di audit post-transazione con protezione dalla manomissione

**Requisito di documentazione**: Accettazione formale del rischio da parte della Direzione generale con controlli compensativi documentati e calendario di revisione.

**Trigger di rivalutazione**: Le disposizioni di controllo compensativo DEVONO essere rivalutate quando: vengono assunte ulteriori persone; cambia la struttura organizzativa; la valutazione del rischio identifica una maggiore esposizione; i risultati dell'audit indicano debolezze del controllo.

## Controlli tecnici di separazione

I sistemi informativi che supportano i processi separati DEVONO implementare:

**Requisiti di controllo degli accessi**:

- Controllo degli accessi basato sui ruoli (RBAC) che applica la separazione dei compiti
- Vincoli di esclusione reciproca che impediscono l'assegnazione di ruoli in conflitto
- Controlli del flusso di lavoro che richiedono approvatori diversi in ciascuna fase
- Gestione degli accessi privilegiati che impedisce l'auto-approvazione

**Requisiti della pista di audit**:

- Registrazione immutabile di tutte le attività separate
- Identificazione chiara degli attori in ciascuna fase del processo
- Registrazione di timestamp e azione per tutte le approvazioni
- Protezione contro la modifica o l'eliminazione dei log

**Definizione di registrazione immutabile**: La registrazione immutabile DEVE essere ottenuta utilizzando piattaforme e configurazioni di registrazione approvate come definite in ISMS-IMP-A.5.3 e nel controllo di registrazione (ISMS-POL-A.8.15). Le implementazioni accettabili includono: storage WORM, accesso amministratore limitato con revisore dei log separato, blocchi di conservazione e aggregazione centralizzata dei log con verifica dell'integrità.

## Gestione delle eccezioni

Le eccezioni ai requisiti di separazione richiedono:

**Eccezioni di emergenza** (≤24 ore):

- Autorizzazione verbale del Responsabile di dipartimento + RSSI
- Documentata entro 4 ore dall'utilizzo dell'eccezione
- Revisione completa entro 24 ore dalla fine dell'eccezione
- Controlli compensativi attivi durante il periodo di eccezione

**Eccezioni pianificate** (>24 ore):

- Richiesta di eccezione formale con giustificazione aziendale
- Valutazione del rischio dell'impatto dell'eccezione
- Controlli compensativi documentati e approvati
- Approvazione di RSSI e Direzione generale
- Durata massima: 90 giorni (rinnovabile con nuova valutazione)

**Non ammissibile**:

- Eccezioni permanenti ai requisiti di separazione finanziaria
- Eccezioni che eliminano le capacità di pista di audit
- Auto-approvazione delle eccezioni di separazione

Tutte le eccezioni DEVONO essere registrate nel Registro delle eccezioni (ISMS-REG-EXCEPTIONS).

**Contenuto minimo del registro delle eccezioni**: Ciascun record di eccezione DEVE includere: sistema/i interessato/i, identità/ruoli a cui è stata concessa l'eccezione, finestra temporale (inizio/fine), autorità di approvazione con prove, controlli compensativi attivi durante l'eccezione, esito della revisione post-eccezione e data di chiusura.

---

# Ruoli e responsabilità

## Matrice delle responsabilità

| Ruolo | Responsabilità per la separazione |
|-------|----------------------------------|
| **Direzione generale** | Approvare la politica di separazione, accettare i rischi residui, approvare i controlli compensativi |
| **RSSI** | Definire i requisiti di separazione, monitorare la conformità, approvare le eccezioni |
| **DF** | Supervisione della separazione dei processi finanziari, approvazione delle eccezioni ai controlli finanziari |
| **Responsabili di dipartimento** | Implementare la separazione nei dipartimenti, identificare i conflitti, richiedere eccezioni |
| **HR** | Mantenere la struttura organizzativa a supporto della separazione, assegnazioni dei ruoli |
| **Operazioni IT** | Implementare i controlli tecnici, configurazione RBAC, monitoraggio degli accessi |
| **Audit interno** | Verificare l'efficacia della separazione, segnalare le violazioni, valutare i controlli compensativi |

## Percorso di escalation

- Conflitti di separazione identificati: Responsabile di dipartimento → RSSI → Direzione generale
- Richieste di eccezione: Richiedente → Responsabile di dipartimento → RSSI → Direzione generale
- Violazione rilevata: Notifica immediata al RSSI e all'Audit interno

---

# Governance e conformità

## Quadro di valutazione

| Valutazione | Frequenza | Responsabile | Prove |
|------------|-----------|-------------|-------|
| Revisione della matrice di separazione | Annuale | RSSI | Matrice dei compiti aggiornata |
| Analisi dei diritti di accesso | Trimestrale | Operazioni IT | Report sugli accessi |
| Revisione dei controlli compensativi | Trimestrale | Audit interno | Valutazione dell'efficacia |
| Revisione del registro delle eccezioni | Mensile | RSSI | Log delle eccezioni |

**Monitoraggio della conformità**:

- Revisione dei diritti di accesso rispetto alla matrice di separazione dei compiti
- Analisi degli schemi di transazione per violazioni della separazione
- Verifica della catena di approvazione del flusso di lavoro
- Revisione dell'efficacia dei controlli compensativi

**Metriche di governance**:

- Numero di conflitti di separazione identificati
- Tempo per rimediare i conflitti
- Richieste e approvazioni di eccezioni
- Punteggi di efficacia dei controlli compensativi

## Revisione della politica

- **Frequenza**: Annuale come minimo
- **Trigger**: Ristrutturazione organizzativa, risultati di audit, aggiornamenti normativi, incidenti di sicurezza
- **Revisori**: RSSI, DF, Audit interno, Direttore HR
- **Approvazione**: Direzione generale

## Collegamento all'azione correttiva

Le non conformità relative a questa politica (es. violazioni della separazione, eccezioni non revisionate, fallimenti dei controlli compensativi) DEVONO essere registrate e gestite attraverso il processo di azione correttiva SGSI (Clausola 10.2) con analisi delle cause profonde e rimedio monitorato.

---

# Implementazione e riferimenti

## Integrazione con il SGSI

**Valutazione del rischio** (Clausola 6.1 ISO 27001): I requisiti di separazione sono informati dalla valutazione del rischio di frodi ed errori; i controlli compensativi sono documentati nei piani di trattamento del rischio; i rischi residui derivanti da separazione limitata sono formalmente accettati.

**Dichiarazione di Applicabilità** (Clausola 6.1.3 ISO 27001): L'applicabilità del Controllo A.5.3 è giustificata nella DdA di [Organizzazione].

**Controlli correlati**:

| Controllo | Relazione |
|-----------|----------|
| **A.5.15-16-18** | Gestione delle identità e degli accessi — Il RBAC applica la separazione dei compiti |
| **A.8.2-3-5** | Autenticazione e accesso privilegiato — Separazione degli accessi privilegiati |
| **A.8.15** | Registrazione — Piste di audit per le attività separate |

## Risorse di implementazione

| ID documento | Titolo | Scopo |
|-------------|--------|-------|
| **ISMS-IMP-A.5.3-UG/TG** | Guida all'implementazione della separazione dei compiti | Matrici dei compiti, controlli tecnici, procedure di monitoraggio |

---

# Prove per questa politica

**Prove per la Fase 1**: Documento di politica; firme di approvazione; comunicazione ai ruoli rilevanti; compiti in conflitto identificati; principi e standard minimi di separazione definiti; requisiti dei controlli compensativi specificati; processo di gestione delle eccezioni documentato; ruoli e responsabilità assegnati.

**Prove per la Fase 2**: Matrice di separazione dei compiti che mostra le combinazioni di ruoli in conflitto; report sui diritti di accesso che dimostrano l'applicazione della separazione; approvazioni del flusso di lavoro campione che mostrano il controllo multi-parte; registro delle eccezioni con approvazioni e controlli compensativi; report trimestrali di analisi della separazione; report di audit interno sulla conformità alla separazione; prove del monitoraggio dei controlli compensativi (dove la separazione non è ottenibile); documenti di formazione del personale sui requisiti di separazione.

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Separazione dei compiti (SdC)** | La pratica di dividere compiti e privilegi tra più individui per impedire a qualsiasi singola persona di avere il controllo completo su un processo critico |
| **Compiti in conflitto** | Responsabilità che, se combinate, consentirebbero a un individuo di commettere e nascondere errori o frodi |
| **Controllo compensativo** | Una misura di controllo alternativa implementata quando la separazione primaria non può essere ottenuta |
| **Esclusione reciproca** | Un controllo tecnico che impedisce a un utente di essere assegnato contemporaneamente a ruoli in conflitto |
| **Principio dei quattro occhi** | Un requisito secondo cui le azioni critiche richiedono l'approvazione o la verifica di almeno due individui autorizzati |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Direttore Finanziario (DF)** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la separazione dei compiti. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.3 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->

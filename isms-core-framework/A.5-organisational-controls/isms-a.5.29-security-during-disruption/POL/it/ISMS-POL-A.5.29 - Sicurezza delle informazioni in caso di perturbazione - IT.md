<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.29-IT:framework:POL:a.5.29 -->
**ISMS-POL-A.5.29 — Sicurezza delle informazioni in caso di perturbazione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza delle informazioni in caso di perturbazione |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.29 |
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
- Secondario: Responsabile della Continuità Operativa
- Integrazione: Direttore dei Sistemi Informativi (DSI)
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.30-8.13-14 (Quadro di continuità operativa e ripristino di emergenza)
- ISMS-POL-A.5.24-28 (Ciclo di vita della gestione degli incidenti)
- ISMS-POL-A.8.14 (Ridondanza delle strutture di elaborazione delle informazioni)
- ISMS-IMP-A.5.29.1-UG/TG (Valutazione dei controlli di sicurezza durante la perturbazione)
- ISMS-IMP-A.5.29.2-UG/TG (Requisiti di sicurezza in modalità degradata)
- ISMS-IMP-A.5.29.3-UG/TG (Lista di controllo per la validazione della sicurezza post-perturbazione)
- ISO/IEC 27001:2022 Controllo A.5.29

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per il mantenimento dei controlli di sicurezza delle informazioni durante gli eventi perturbativi, garantendo che la sicurezza non venga compromessa quando le operazioni normali sono interrotte.

**Perimetro**: Questa politica si applica a tutti gli eventi perturbativi che incidono sulla capacità di [Organizzazione] di operare normalmente, inclusi i disastri naturali, i guasti all'infrastruttura, gli incidenti informatici, le pandemie, le interruzioni della catena di approvvigionamento e le perturbazioni civili.

**Scopo**: Definire i requisiti organizzativi per la sicurezza durante la perturbazione. Questa politica stabilisce QUALI controlli di sicurezza devono essere mantenuti e CHI è responsabile della sicurezza durante le condizioni avverse. Le procedure di attuazione (COME) sono documentate separatamente in ISMS-IMP-A.5.29 (varianti UG/TG).

**Principio critico — «La sicurezza non può andare in vacanza»**: Le perturbazioni creano opportunità per gli attori delle minacce. Quando le organizzazioni si concentrano sul ripristino, gli avversari sfruttano la vigilanza ridotta. Questa politica garantisce che i controlli di sicurezza rimangano efficaci durante tutte le fasi della perturbazione e del ripristino.

---

# Allineamento sul controllo e perimetro

**ISO/IEC 27001:2022 Allegato A.5.29 — Sicurezza delle informazioni in caso di perturbazione**

[Organizzazione] mantiene controlli di sicurezza definiti durante le perturbazioni attraverso riferimenti stabiliti, livelli di postura a livelli e procedure di ripristino pre-pianificate che prevengono la compromissione della sicurezza durante condizioni avverse.

**Obiettivi del controllo**: Garantire che i controlli di sicurezza delle informazioni rimangano efficaci durante gli eventi perturbativi; integrare i requisiti di sicurezza nella pianificazione della continuità operativa e del ripristino di emergenza; prevenire la compromissione della sicurezza nell'interesse della rapidità durante le operazioni di ripristino; mantenere la conformità con gli obblighi normativi durante la perturbazione.

**Tipo di controllo**: Preventivo, Investigativo, Correttivo
**Categoria del controllo**: Organizzativo

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Applicabilità | Requisiti chiave |
|-----------|---------------|-----------------|
| **nLPD svizzera Art. 8** | Tutto il trattamento dei dati personali | Mantenere misure di sicurezza appropriate |
| **RGPD dell'UE Art. 32** | Elaborazione di dati personali UE | Sicurezza del trattamento inclusa la disponibilità |
| **ISO/IEC 27001:2022** | Ambito di certificazione | Controllo A.5.29 — Sicurezza durante la perturbazione |

**Livello 2 — Applicabilità condizionale**:

| Normativa | Condizione scatenante | Requisiti di sicurezza |
|-----------|----------------------|----------------------|
| **DORA** | Entità dei servizi finanziari UE | Resilienza operativa digitale inclusi gli incidenti TIC |
| **NIS2** | Entità essenziale/importante (UE) | Continuità operativa inclusa la gestione delle crisi |
| **FINMA** | Istituto finanziario svizzero regolamentato | Requisiti di resilienza operativa (Circolare 2023/1) |
| **Normative sanitarie** | Operazioni sanitarie | Continuità della protezione dei dati dei pazienti |

**Livello 3 — Riferimento informativo**: ISO 22301; NIST SP 800-34; Linee guida BCI di buone pratiche; Linee guida ENISA sulla continuità dei servizi TIC.

**Determinazione della conformità**: [Organizzazione] determina le normative applicabili del Livello 2 attraverso una valutazione periodica delle attività aziendali. I requisiti di sicurezza più stringenti si applicano dove più normative si sovrappongono.

---

# Enunciati di politica

## Requisiti del livello di sicurezza durante la perturbazione

### Livello minimo di sicurezza

[Organizzazione] DEVE mantenere i seguenti controlli minimi di sicurezza indipendentemente dallo stato operativo:

**Parametri di controllo / Fonti di verità**: Ai fini di questa politica:
- **Sistemi critici**: Sistemi classificati come Tier-1 o Tier-2 nel Registro di criticità dei sistemi derivato dalla BIA
- **Riservato+**: Informazioni classificate come RISERVATO o LIMITATO per ISMS-POL-A.5.12-13
- **Registrazione critica**: Il set minimo di log definito nello Standard di registrazione (ISMS-IMP-A.8.15), applicato a tutti i sistemi Tier-1/Tier-2
- **Confini critici**: Zone di segmentazione di rete che proteggono i sistemi Tier-1/Tier-2 come definito nella documentazione dell'Architettura di rete

**Controlli non negoziabili** (devono essere mantenuti in qualsiasi momento):

| Categoria di controllo | Requisito minimo | Motivazione |
|------------------------|-----------------|-------------|
| **Controllo degli accessi** | Autenticazione richiesta per tutti gli accessi al sistema | Previene l'accesso non autorizzato durante il caos |
| **Cifratura dei dati** | Cifratura a riposo per i dati Riservati+ | I dati rimangono protetti in caso di perdita del supporto |
| **Registrazione** | La registrazione dei sistemi critici continua | Pista di audit per l'indagine post-incidente |
| **Segmentazione di rete** | I confini di rete critici vengono mantenuti | Previene il movimento laterale durante il ripristino |
| **Protezione dei backup** | I backup rimangono cifrati e controllati nell'accesso | Previene la compromissione dei backup per il furto di dati |

**Modalità degradata accettabile** (con approvazione documentata e controlli compensativi):

| Categoria di controllo | Degrado accettabile | Controllo compensativo richiesto |
|------------------------|---------------------|----------------------------------|
| **AMF** | Fattore singolo se infrastruttura AMF non disponibile | Registrazione avanzata, limiti di sessione, restrizioni IP |
| **Scansione delle vulnerabilità** | Scansione ritardata accettabile | Revisione manuale delle sole patch critiche |
| **Monitoraggio della sicurezza** | Ambito ridotto accettabile | Focus sui sistemi critici, revisione manuale avanzata |
| **Revisioni degli accessi** | Revisioni rinviate accettabili (max 30 giorni) | Approvazione più rigorosa per le nuove richieste di accesso |
| **Gestione delle patch** | Patch ritardate accettabili (max 30 giorni per quelle non critiche) | Le vulnerabilità critiche/alte rimangono entro 72h/7g |

**Monitoraggio obbligatorio**: Qualsiasi degrado dei controlli approvato DEVE creare immediatamente una voce a tempo limitato nel Registro del debito di sicurezza o nel Registro delle eccezioni (ISMS-REG-EXCEPTIONS), includendo: titolare, controlli compensativi, data di inizio, data di chiusura dovuta allineata a questa politica e prove di chiusura.

**Mai accettabile** (anche durante la perturbazione):

- Registrazione disabilitata sui sistemi critici
- Rimozione dei requisiti di autenticazione
- Decifratura dei dati a riposo senza ri-cifratura
- Disabilitazione dei controlli di sicurezza di rete (firewall, IDS/IPS)
- Condivisione di credenziali privilegiate senza responsabilità individuale
- Aggiramento della gestione dei cambiamenti per i sistemi in produzione (salvo modifica di emergenza dichiarata per ISMS-IMP-A.8.32, con revisione post-implementazione entro 5 giorni lavorativi)

### Postura di sicurezza a livelli

[Organizzazione] DEVE definire livelli di postura di sicurezza allineati alla gravità della perturbazione:

| Livello | Stato di perturbazione | Postura di sicurezza | Esempio |
|---------|----------------------|---------------------|---------|
| **Normale** | Nessuna perturbazione | Controlli completi operativi | Operazioni quotidiane |
| **Elevato** | Perturbazione minore | Monitoraggio avanzato, patch accelerate | Guasto di un singolo sistema, incidente minore |
| **Degradato** | Perturbazione moderata | Controlli fondamentali mantenuti, non critici rinviati | Failover del data center, interruzione regionale |
| **Emergenza** | Perturbazione grave | Solo livello minimo, modalità sopravvivenza | Disastro multi-sito, grande attacco informatico |
| **Ripristino** | Ritorno alla normalità | Ripristino graduale con validazione della sicurezza | Fase di ripristino post-disastro |

**Autorità di transizione**:

| Transizione | Autorità richiesta | Documentazione |
|-------------|------------------|----------------|
| Normale → Elevato | RSSI o Responsabile del team di sicurezza | Ticket di incidente |
| Elevato → Degradato | RSSI + DSI | Notifica formale alla Direzione generale |
| Degradato → Emergenza | Direzione generale (AD o delegato) | Documento di dichiarazione di emergenza |
| Transizioni di ripristino | Approvazione RSSI per ogni fase | Lista di controllo del completamento della fase |

## Pianificazione della sicurezza per BCP/DRP

### Requisiti di sicurezza dei piani BCP/DRP

Tutti i piani di Continuità operativa e Ripristino di emergenza DEVONO includere:

**Considerazioni di sicurezza nei piani BCP/DRP**:

1. **Controllo degli accessi durante il ripristino**:
   - Chi ha accesso ai sistemi e ai dati di ripristino
   - Come viene autenticato l'accesso quando i sistemi normali non sono disponibili
   - Come viene revocato l'accesso quando il ripristino è completato
   - Account di accesso di emergenza e relativi controlli

2. **Protezione dei dati durante il ripristino**:
   - Come i dati sono protetti durante il trasferimento al sito di ripristino
   - Requisiti di cifratura per i supporti di ripristino
   - Catena di custodia per lo spostamento fisico dei dati
   - Applicazione della classificazione dei dati nell'ambiente di ripristino

3. **Sicurezza delle comunicazioni**:
   - Canali di comunicazione sicuri per il team di crisi
   - Comunicazione alternativa se i canali primari sono compromessi
   - Autenticazione delle comunicazioni di crisi (prevenire l'ingegneria sociale)
   - Confini di condivisione delle informazioni (cosa può essere condiviso esternamente)

4. **Sicurezza di terze parti**:
   - Controlli di accesso dei fornitori durante il ripristino
   - Requisiti di sicurezza per appaltatori durante le operazioni di emergenza
   - Sicurezza dei servizi cloud durante il failover
   - Sicurezza della catena di approvvigionamento per gli acquisti di emergenza

**Revisione della sicurezza BCP/DRP**:

- Il RSSI o delegato DEVE rivedere e approvare le sezioni di sicurezza di tutti i piani BCP/DRP
- La revisione della sicurezza DEVE avvenire prima dell'approvazione del piano BCP/DRP e dopo ogni aggiornamento
- Gli scenari di test BCP/DRP specifici per la sicurezza DEVONO essere inclusi nei test annuali
- Le deviazioni di sicurezza durante i test DEVONO essere documentate e affrontate

### Sicurezza del sito di ripristino

I siti di ripristino (siti caldi, tiepidi, freddi, DR cloud) DEVONO mantenere:

| Controllo | Requisito |
|-----------|-----------|
| **Sicurezza fisica** | Equivalente al sito primario per la criticità dei dati |
| **Sicurezza di rete** | Stessa segmentazione, regole firewall, monitoraggio |
| **Controllo degli accessi** | Stesso modello di autenticazione e autorizzazione |
| **Protezione dei dati** | Stessa cifratura, controlli di classificazione |
| **Registrazione** | Capacità di registrazione equivalente |
| **Rafforzamento** | Stesse linee di base di configurazione |

## Procedure di accesso di emergenza

### Account di emergenza (Break-glass)

[Organizzazione] DEVE mantenere meccanismi di accesso di emergenza per gli scenari di perturbazione:

**Requisiti dell'account di emergenza**:

| Requisito | Specifica |
|-----------|-----------|
| **Stato dell'account** | Dormiente (disabilitato) fino alla dichiarazione di emergenza |
| **Autorità di attivazione** | RSSI, DSI o AD (catena di autorità documentata) |
| **Autenticazione** | Autenticazione forte (archiviata in modo sicuro, fattori multipli) |
| **Ambito** | Pre-definito, limitato ai sistemi essenziali per il ripristino |
| **Registrazione** | Tutte le azioni registrate con protezione dalla manomissione |
| **Durata** | A tempo limitato (disabilitazione automatica al termine dell'emergenza dichiarata) |
| **Disattivazione** | Disattivazione formale con cambio/rotazione della password |

**Log di accesso di emergenza**: Ogni attivazione dell'account di emergenza DEVE essere registrata nel Log di accesso di emergenza con: approvatore, attivatore, sistemi a cui si è avuto accesso, ora di inizio/fine, azioni eseguite, conferma della cattura del log e verifica della disattivazione.

**Processo di attivazione dell'account di emergenza**:

1. Emergenza dichiarata dall'autorità autorizzata
2. Richiesta di attivazione dell'account di emergenza documentata (anche verbalmente, con follow-up scritto entro 4 ore)
3. Attivazione da parte del personale designato (regola del minimo due persone per i sistemi critici)
4. Notifica al RSSI e al Team di sicurezza
5. Monitoraggio avanzato abilitato
6. Accesso a tempo limitato (predefinito: 24 ore, rinnovabile con re-approvazione)
7. Disattivazione post-emergenza e revisione completa

### Disponibilità del personale

[Organizzazione] DEVE garantire la disponibilità del personale di sicurezza durante la perturbazione:

**Continuità del team di sicurezza**:

- I ruoli di sicurezza chiave hanno backup designati (piano di successione documentato)
- Le informazioni di contatto per il personale di sicurezza sono mantenute offline (stampate, USB cifrata)
- Distribuzione geografica del team di sicurezza dove possibile
- Formazione incrociata per garantire la copertura delle funzioni di sicurezza critiche
- Reperibilità per copertura 24/7 durante gli stati di elevazione/degrado/emergenza

## Validazione della sicurezza post-perturbazione

### Recupero della postura di sicurezza

Prima di tornare alle operazioni normali, [Organizzazione] DEVE validare la postura di sicurezza:

**Lista di controllo per il recupero della sicurezza**:

| Fase | Attività di validazione |
|------|------------------------|
| **Immediata (0-24h post-perturbazione)** | Verificare i controlli critici di sicurezza operativi, disabilitare l'accesso di emergenza, rivedere i log per anomalie |
| **Breve termine (1-7 giorni)** | Validazione completa dei controlli di sicurezza, scansione delle vulnerabilità, revisione degli accessi, analisi degli incidenti |
| **Medio termine (1-4 settimane)** | Rimedio del debito di sicurezza, patch rinviate applicate, ricertificazione completa degli accessi, test dei controlli |
| **Lungo termine (1-3 mesi)** | Implementazione degli insegnamenti tratti, aggiornamenti BCP/DRP, aggiornamenti delle politiche, aggiornamenti della formazione |

**Monitoraggio del debito di sicurezza**:

- Tutti i rilassamenti dei controlli di sicurezza durante la perturbazione DEVONO essere registrati nel registro del debito di sicurezza
- Ogni voce del debito DEVE avere un titolare, un piano di rimedio e una data obiettivo
- Il debito di sicurezza più vecchio di 30 giorni DEVE essere escalato al RSSI
- Il debito di sicurezza più vecchio di 90 giorni DEVE essere escalato alla Direzione generale o accettato come rischio permanente

---

# Ruoli e responsabilità

## Matrice delle responsabilità

| Ruolo | Responsabilità per la sicurezza durante la perturbazione |
|-------|----------------------------------------------------------|
| **Direzione generale** | Approvare i livelli di postura di sicurezza; autorizzare la modalità di emergenza; allocazione delle risorse |
| **RSSI** | Requisiti di sicurezza per BCP/DRP; approvare le transizioni di postura di sicurezza; validazione post-perturbazione |
| **Responsabile della Continuità Operativa** | Integrare i requisiti di sicurezza nei piani BCP/DRP; coordinarsi con il RSSI |
| **DSI** | Ripristino IT allineato ai requisiti di sicurezza; autorizzazione dell'accesso di emergenza |
| **Team di sicurezza** | Monitorare la sicurezza durante la perturbazione; attivare le procedure di emergenza; validare il ripristino |
| **Team di gestione delle crisi** | Includere le considerazioni di sicurezza nelle decisioni di crisi; comunicare con il RSSI |
| **Operazioni IT** | Implementare i controlli di sicurezza negli ambienti di ripristino; segnalare i problemi di sicurezza |
| **Tutto il personale** | Seguire le procedure di sicurezza durante la perturbazione; segnalare le preoccupazioni di sicurezza |

## Percorso di escalation

- Preoccupazioni di sicurezza durante la perturbazione attiva: Team di sicurezza → RSSI → Team di gestione delle crisi
- Incidenti di sicurezza durante la perturbazione: Per ISMS-POL-A.5.24-28 con priorità elevata
- Richieste di transizione della postura di sicurezza: Richiedente → RSSI → Direzione generale (se necessario)

---

# Governance e conformità

## Quadro di valutazione

| Valutazione | Frequenza | Responsabile | Prove |
|------------|-----------|-------------|-------|
| Revisione della sicurezza del piano BCP/DRP | Annuale + dopo gli aggiornamenti | RSSI | Report di revisione, firma di approvazione |
| Test delle procedure di accesso di emergenza | Annuale | Team di sicurezza | Risultati dei test, validazione delle procedure |
| Componente di sicurezza dei test BCP/DRP | Con i test BCP/DRP (annuale come minimo) | Team di sicurezza + Responsabile BCP | Scenari di test, risultati, rimedio |
| Valutazione della sicurezza del sito di ripristino | Annuale | Team di sicurezza | Revisione della configurazione, analisi delle lacune |
| Esercitazione sulla disponibilità del personale di sicurezza | Semestrale | RSSI | Risultati del test dei contatti, validazione della successione |

**Metriche di governance**:

- Piani BCP/DRP con approvazione della sicurezza del RSSI (obiettivo: 100%)
- Test delle procedure di accesso di emergenza completati (obiettivo: 100% annualmente)
- Incidenti di sicurezza durante gli eventi di perturbazione (monitoraggio delle tendenze)
- Voci del debito di sicurezza post-perturbazione (obiettivo: 0 voci >90 giorni)
- Risultati della valutazione della sicurezza del sito di ripristino (obiettivo: 0 risultati critici/alti)

## Revisione della politica

- **Frequenza**: Annuale come minimo
- **Trigger**: Evento di perturbazione grave, cambiamenti BCP/DRP, aggiornamenti normativi, risultati di audit
- **Revisori**: RSSI, Responsabile della Continuità Operativa, DSI, Team di gestione delle crisi
- **Approvazione**: Direzione generale

## Gestione delle eccezioni

**Eccezioni consentite**:

- Degrado del controllo di sicurezza durante la perturbazione attiva (con controlli compensativi documentati)
- Rilassamenti pre-approvati permanenti per scenari specifici (valutati per rischio e a tempo limitato)
- Debito di sicurezza post-perturbazione per piani di rimedio documentati

**Processo di eccezione**:

1. Documentare la giustificazione aziendale e il contesto della perturbazione
2. Valutazione del rischio per la sicurezza
3. Approvazione del RSSI (o backup designato se il RSSI non è disponibile)
4. Controlli compensativi documentati
5. Approvazione a tempo limitato (durata della perturbazione + 7 giorni per il ripristino)

**Non ammissibile**:

- Eccezioni permanenti al livello minimo di sicurezza
- Eccezioni che eliminano la capacità di pista di audit
- Eccezioni senza controlli compensativi

Tutte le eccezioni DEVONO essere registrate nel Registro delle eccezioni (ISMS-REG-EXCEPTIONS).

## Collegamento all'azione correttiva

Le non conformità relative a questa politica (es. revisione della sicurezza BCP/DRP inadeguata, accesso di emergenza non testato, accumulo del debito di sicurezza, lacune nel sito di ripristino) DEVONO essere registrate e gestite attraverso il processo di azione correttiva SGSI (Clausola 10.2) con analisi delle cause profonde e rimedio monitorato.

---

# Implementazione e riferimenti

## Integrazione con il SGSI

**Valutazione del rischio** (Clausola 6.1 ISO 27001): Gli scenari di perturbazione sono inclusi nella valutazione del rischio; i requisiti di sicurezza durante la perturbazione sono informati dall'analisi dell'impatto; i piani di trattamento del rischio documentano i controlli di sicurezza per BCP/DRP.

**Dichiarazione di Applicabilità** (Clausola 6.1.3): L'applicabilità del Controllo A.5.29 è giustificata nella DdA di [Organizzazione].

**Controlli correlati**:

| Controllo | Relazione |
|-----------|----------|
| **A.5.30** | Continuità operativa — La pianificazione BCP/DRP; A.5.29 fornisce i requisiti di sicurezza |
| **A.8.13** | Backup — Protezione dei dati durante la perturbazione |
| **A.8.14** | Ridondanza — Requisiti di sicurezza del sito di ripristino |
| **A.5.24-28** | Gestione degli incidenti — Incidenti di sicurezza durante la perturbazione |
| **A.8.15** | Registrazione — Requisiti di registrazione durante la perturbazione |
| **A.5.15-16-18** | Controllo degli accessi — Accesso di emergenza, accesso durante la perturbazione |

**Integrazione dei controlli sovrapposti**:

| Controllo sovrapposto | Punto di integrazione | Contributo di A.5.29 |
|-----------------------|----------------------|---------------------|
| **A.5.30** (Continuità operativa) | Pianificazione BCP/DRP | A.5.29 definisce i requisiti di sicurezza; A.5.30 definisce le procedure di continuità |
| **A.5.24-28** (Gestione degli incidenti) | Risposta agli incidenti | A.5.29 affronta la sicurezza durante qualsiasi perturbazione; A.5.24-28 per gli incidenti di sicurezza |
| **A.8.14** (Ridondanza) | Siti di ripristino | A.5.29 specifica i requisiti di sicurezza per gli ambienti di ripristino |

## Risorse di implementazione

| ID documento | Titolo | Scopo |
|-------------|--------|-------|
| **ISMS-IMP-A.5.29.1-UG/TG** | Requisiti di sicurezza per i piani BCP/DRP | Procedure di integrazione della sicurezza BCP/DRP |
| **ISMS-IMP-A.5.29.2-UG/TG** | Procedure di accesso di emergenza | Attivazione e disattivazione dell'account di emergenza |
| **ISMS-IMP-A.5.29.3-UG/TG** | Lista di controllo per la validazione post-perturbazione | Procedure di validazione del ripristino |

---

# Prove per questa politica

**Prove per la Fase 1** (Revisione della documentazione):

- ✅ Documento di politica (ISMS-POL-A.5.29 v1.0)
- ✅ Approvazione registrata da RSSI, Responsabile della Continuità Operativa, DSI, Direzione generale
- ✅ Prove della comunicazione ai ruoli rilevanti
- ✅ Livello minimo di sicurezza definito (Requisiti del livello di sicurezza durante la perturbazione)
- ✅ Livelli di postura di sicurezza a livelli definiti con autorità di transizione (Postura di sicurezza a livelli)
- ✅ Requisiti di sicurezza del piano BCP/DRP specificati (Pianificazione della sicurezza per BCP/DRP)
- ✅ Procedure di accesso di emergenza definite (Procedure di accesso di emergenza)
- ✅ Requisiti di validazione post-perturbazione definiti (Validazione della sicurezza post-perturbazione)
- ✅ Ruoli e responsabilità assegnati (Ruoli e responsabilità)

Lo stato delle prove è monitorato nel Registro delle prove SGSI.

**Prove per la Fase 2** (Efficacia operativa):

- Piani BCP/DRP con firme di approvazione della sicurezza del RSSI
- Risultati dei test dell'accesso di emergenza (account di emergenza) e validazione delle procedure
- Risultati dei test BCP/DRP che mostrano scenari specifici per la sicurezza
- Report di valutazione della sicurezza del sito di ripristino
- Risultati dell'esercitazione sulla disponibilità del personale di sicurezza
- Documenti di transizione della postura di sicurezza (se si sono verificate perturbazioni)
- Registro del debito di sicurezza con monitoraggio del rimedio
- Report di revisione della sicurezza post-perturbazione (se si sono verificate perturbazioni)
- Documenti di formazione per le procedure di sicurezza del team di gestione delle crisi

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Perturbazione** | Qualsiasi evento che interrompe o minaccia di interrompere le normali operazioni aziendali |
| **Livello di postura di sicurezza** | Stato definito dell'implementazione del controllo di sicurezza (Normale, Elevato, Degradato, Emergenza, Ripristino) |
| **Account di emergenza (Break-glass)** | Meccanismo di accesso privilegiato di emergenza attivato quando l'accesso normale non è disponibile |
| **Debito di sicurezza** | Controlli o attività di sicurezza differiti durante la perturbazione che richiedono un rimedio successivo |
| **Sito di ripristino** | Ubicazione alternativa (fisica o cloud) per la ripresa delle operazioni durante la perturbazione |
| **Team di gestione delle crisi** | Team interfunzionale attivato per gestire la risposta organizzativa alle perturbazioni gravi |
| **Controllo compensativo** | Misura di sicurezza alternativa implementata quando il controllo primario non è disponibile |
| **Livello minimo di sicurezza** | Controlli di sicurezza non negoziabili che devono essere mantenuti indipendentemente dallo stato operativo |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Responsabile della Continuità Operativa** | [Nome] | [Data da definire] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per il mantenimento della sicurezza delle informazioni durante la perturbazione. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.29 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->

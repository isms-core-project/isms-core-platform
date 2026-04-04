<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.24-28-IT:framework:POL:a.5.24-28 -->
**ISMS-POL-A.5.24-28 — Ciclo di vita della gestione degli incidenti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Ciclo di vita della gestione degli incidenti |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.24-28 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Catena di approvazione**: RSSI → DSI → Responsabile Risposta agli Incidenti / CSIRT → Responsabile Legale → Direzione generale

**Documenti correlati**: ISMS-POL-00; ISMS-REF-A.5.24-28; ISMS-IMP-A.5.24-28.-UG/TGS1-S5; ISO/IEC 27001:2022 Controlli A.5.24-28; ISMS-POL-A.8.15; ISMS-POL-A.8.16; ISMS-POL-A.6.8; ISMS-POL-A.5.29-30; ISMS-POL-A.5.31

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la gestione degli incidenti di sicurezza delle informazioni durante il loro ciclo di vita completo, conformemente ai Controlli A.5.24–A.5.28 della norma ISO/IEC 27001:2022.

**Approccio combinato ai controlli**: Questi cinque controlli sono implementati come quadro unificato del ciclo di vita:
1. **Pianificazione e preparazione (A.5.24)** — Stabilire le capacità prima che si verifichino gli incidenti
2. **Valutazione e decisione (A.5.25)** — Determinare se un evento è un incidente
3. **Operazioni di risposta (A.5.26)** — Contenere, eradicare, ripristinare
4. **Raccolta delle prove (A.5.28)** — Preservare le prove forensi (in parallelo alla risposta)
5. **Apprendimento e miglioramento (A.5.27)** — Estrarre insegnamenti, migliorare i controlli

**Allineamento normativo**: nLPD svizzera (Art. 24 — notifica al PFPDT «quanto prima possibile» in caso di alto rischio); RGPD dell'UE (Art. 33-34 — notifica all'autorità di supervisione entro 72 ore); ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Enunciati di politica

## Pianificazione e preparazione (A.5.24)

**PS-3.1.1 Capacità organizzativa**: [Organizzazione] DEVE stabilire una capacità di risposta agli incidenti tramite un CSIRT (Computer Security Incident Response Team) e/o un SOC (Security Operations Center) designati con autorità e risorse definite.

**PS-3.1.2 Procedure documentate**: [Organizzazione] DEVE documentare e mantenere procedure di risposta agli incidenti che coprono l'intero ciclo di vita, con controllo delle versioni e revisione annuale.

**PS-3.1.3 Quadro di classificazione**: [Organizzazione] DEVE stabilire un quadro di classificazione degli incidenti che definisce livelli di gravità e categorie per consentire una prioritizzazione e un'escalation coerenti.

**PS-3.1.4 Requisiti di formazione**: Il personale addetto alla risposta agli incidenti DEVE essere formato e dimostrare competenza prima di assumere mansioni di risposta. La competenza viene valutata tramite esercitazioni tabletop pratiche; la formazione viene rinnovata annualmente.

**PS-3.1.5 Requisiti di esercitazione**: [Organizzazione] DEVE condurre esercitazioni tabletop di risposta agli incidenti almeno due volte l'anno. I risultati DEVONO essere documentati e monitorati come azioni di miglioramento.

**PS-3.1.6 Strumenti e tecnologie**: [Organizzazione] DEVE fornire ai team di risposta strumenti appropriati: (1) sistema di gestione degli incidenti con tracciamento del flusso di lavoro; (2) capacità di acquisizione forense; (3) canale di comunicazione sicuro (cifrato); (4) accesso ai sistemi di monitoraggio/registrazione.

## Valutazione e decisione (A.5.25)

**PS-3.2.1 Requisito di valutazione**: Tutti gli eventi di sicurezza DEVONO essere valutati per determinare se costituiscono incidenti che richiedono risposta.

**PS-3.2.2 Classificazione della gravità**: Tutti gli incidenti confermati DEVONO ricevere un livello di gravità basato sull'impatto sulla riservatezza, integrità e disponibilità (matrice CIA).

**PS-3.2.3 Classificazione per categoria**: Tutti gli incidenti DEVONO essere categorizzati per tipo utilizzando la tassonomia organizzativa.

**PS-3.2.4 Requisiti di escalation**: Gli incidenti DEVONO essere escalati ai livelli di gestione appropriati in base alla gravità. Gli incidenti Critici richiedono una notifica immediata alla Direzione generale.

**PS-3.2.5 Documentazione**: Tutte le valutazioni DEVONO essere documentate nel sistema di gestione degli incidenti con i campi obbligatori: fonte dell'evento e timestamp di rilevamento; analisi dell'impatto CIA; livello di gravità; categoria; azioni di escalation; nome e timestamp dell'approvatore.

## Operazioni di risposta agli incidenti (A.5.26)

**PS-3.3.1 Esecuzione della risposta**: Tutti gli incidenti confermati DEVONO essere gestiti seguendo le procedure documentate appropriate alla gravità e alla categoria.

**Playbook di risposta per categoria** (in ISMS-REF-A.5.24-28 Sezione 3):
- **Software malevolo/Ransomware**: Isolamento, acquisizione forense, analisi, verifica dell'eradicazione
- **Accesso non autorizzato**: Revoca delle credenziali, terminazione delle sessioni, revisione dei log
- **Violazione dei dati**: Valutazione dell'ambito, analisi delle notifiche normative (RGPD/nLPD)
- **Denial of Service**: Analisi del traffico, attivazione della mitigazione, priorità di ripristino
- **Ingegneria sociale**: Notifica agli utenti, reset delle credenziali, prevenzione
- **Minaccia interna**: Conservazione delle prove, coordinamento HR, sospensione degli accessi
- **Sicurezza fisica**: Recupero degli asset, revisione dei controlli di accesso
- **Catena di approvvigionamento**: Notifica al fornitore, valutazione delle dipendenze, attivazione dei controlli compensativi

**PS-3.3.2 Contenimento**: La risposta agli incidenti DEVE prioritizzare il contenimento. L'efficacia del contenimento DEVE essere verificata prima di procedere all'eradicazione.

**PS-3.3.3 Eradicazione**: La causa radice degli incidenti DEVE essere eliminata prima che i sistemi vengano restituiti alla produzione.

**PS-3.3.4 Ripristino**: I sistemi e i servizi interessati DEVONO essere ripristinati alle operazioni normali seguendo le priorità di criticità aziendale. Priorità: (1) Sistemi critici (RTO < 4 ore) — ripristino immediato; (2) Alta priorità (RTO 4-24 ore) — stesso giorno lavorativo; (3) Priorità media (RTO 1-3 giorni) — giorno lavorativo successivo; (4) Bassa priorità (RTO > 3 giorni) — ripristino pianificato.

**PS-3.3.5 Comunicazioni**: Le comunicazioni sugli incidenti DEVONO seguire protocolli documentati per parti interessate interne, gestione, utenti e parti esterne (autorità di regolamentazione, clienti, forze dell'ordine).

**PS-3.3.6 Standard di tempo di risposta (SLA)**: [Organizzazione] DEVE definire e mantenere standard dei tempi di risposta per livello di gravità.

## Raccolta e conservazione delle prove forensi (A.5.28)

**PS-3.4.1 Raccolta delle prove**: Le prove forensi DEVONO essere raccolte per tutti gli incidenti di gravità Critica e gli incidenti di gravità Alta con potenziali implicazioni legali o normative.

**PS-3.4.2 Tempistica**: La raccolta delle prove inizia immediatamente al rilevamento dell'incidente e procede in parallelo alle operazioni di risposta.

**PS-3.4.3 Metodi forensicamente corretti**: Le prove DEVONO essere raccolte usando metodi forensicamente corretti che mantengano l'integrità e supportino la potenziale ammissibilità legale.

**PS-3.4.4 Catena di custodia**: Tutte le prove DEVONO avere una catena di custodia documentata dal momento della raccolta fino allo smaltimento.

**PS-3.4.5 Conservazione delle prove**: Le prove DEVONO essere conservate in modo sicuro con controlli degli accessi, cifratura e verifica dell'integrità.

**PS-3.4.6 Blocco legale**: [Organizzazione] DEVE implementare procedure di blocco legale quando è avviato un contenzioso o è ragionevolmente anticipato.

## Apprendimento post-incidente e miglioramento (A.5.27)

**PS-3.5.1 Revisione post-incidente (RPI)**: Le RPI DEVONO essere condotte per tutti gli incidenti Critici e di Alta gravità entro i tempi definiti. Gli incidenti di media gravità richiedono la RPI quando rivelano tecniche di attacco nuove o significativi fallimenti dei controlli.

**PS-3.5.2 Analisi delle cause profonde**: L'analisi delle cause profonde DEVE identificare i problemi sistemici sottostanti, non solo le cause prossimali.

**PS-3.5.3 Implementazione dei miglioramenti**: Gli insegnamenti tratti DEVONO essere tradotti in miglioramenti attuabili con titolari assegnati e date di completamento obiettivo.

**PS-3.5.4 Gestione delle conoscenze**: [Organizzazione] DEVE mantenere un repository degli insegnamenti tratti accessibile al personale di risposta agli incidenti. I playbook DEVONO essere aggiornati.

**PS-3.5.5 Metriche e analisi delle tendenze**: [Organizzazione] DEVE monitorare le metriche degli incidenti (volume, gravità, tempi di risposta, conformità agli SLA) e condurre analisi trimestrali delle tendenze.

**PS-3.5.6 Revisione annuale del programma**: Il programma di gestione degli incidenti DEVE essere rivisto annualmente per valutare l'efficacia e aggiornare procedure, formazione e strumenti.

---

# Quadro di governance

## Quadro di gravità degli incidenti

| Gravità | Definizione | Requisito di risposta |
|---------|-------------|----------------------|
| **Critica** | Impatto aziendale significativo; violazione su larga scala, ransomware in produzione | Risposta immediata, contenimento aggressivo, notifica Direzione generale, RPI obbligatoria |
| **Alta** | Impatto aziendale moderato; attacco mirato, accesso ai dati confermato | Risposta urgente, notifica RSSI, RPI obbligatoria |
| **Media** | Impatto aziendale limitato; infezione isolata, attacco non riuscito | Risposta standard, supervisione del team leader, RPI condizionale |
| **Bassa** | Impatto aziendale minimo; attacco bloccato, evento informativo | Gestione standard, elaborazione batch accettabile, nessuna RPI richiesta |

## Standard dei tempi di risposta (SLA)

| Gravità | Risposta iniziale | Obiettivo di contenimento | Obiettivo di risoluzione | Aggiornamenti gestione |
|---------|------------------|--------------------------|--------------------------|------------------------|
| **Critica** | 15 minuti | 1 ora | 24 ore | Tempo reale (orario) |
| **Alta** | 1 ora | 4 ore | 72 ore | Giornaliero |
| **Media** | 4 ore | 24 ore | 5 giorni lavorativi | Settimanale (se in corso) |
| **Bassa** | 8 ore | 48 ore | 10 giorni lavorativi | Report raggruppati |

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Direzione generale** | Responsabilità ultima; decide sulle azioni critiche per il business |
| **RSSI** | Responsabilità della conformità della politica; approva le procedure; accetta il rischio residuo |
| **Responsabile Risposta Incidenti / CSIRT** | Operazioni di risposta quotidiane; conformità agli SLA; coordinamento |
| **Analisti SOC / Gestori incidenti** | Triage, indagine, contenimento, eradicazione, ripristino, documentazione |
| **Specialisti forensi** | Integrità della raccolta delle prove; catena di custodia; analisi forense |
| **Operazioni IT** | Esecuzione delle azioni tecniche; ripristino dei servizi |
| **Consulente legale** | Mitigazione del rischio legale; conformità normativa; blocco legale |
| **RPD (RPD)** | Conformità alla privacy; valutazione dei requisiti di notifica delle violazioni |
| **Team di comunicazione** | Comunicazioni esterne; gestione della reputazione |
| **Tutto il personale** | Segnalazione degli incidenti ai sensi di ISMS-POL-A.6.8 |

---

# Conformità ed eccezioni

Le eccezioni richiedono: richiesta scritta con giustificazione; valutazione del rischio; approvazione RSSI (minimo); durata a tempo limitato (massimo 12 mesi); documentazione nel registro delle eccezioni SGSI.

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data] |
| **Responsabile Risposta agli Incidenti** | [Nome] | [Data] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data] |
| **Responsabile Legale** | [Nome] | [Data] |
| **Responsabile della Protezione dei Dati (RPD)** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la gestione degli incidenti di sicurezza delle informazioni (A.5.24-28). Le procedure di attuazione sono documentate in ISMS-IMP-A.5.24-28 (UG/TG).S1-S5.*

<!-- QA_VERIFIED: 2026-04-03 -->

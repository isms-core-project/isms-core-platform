<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.4-5-11-IT:framework:POL:a.7.4-5-11 -->
**ISMS-POL-A.7.4-5-11 — Sicurezza dell'infrastruttura fisica**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Politica di sicurezza dell'infrastruttura fisica |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.7.4-5-11 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale (o in caso di cambiamenti significativi alle strutture, incidenti di sicurezza o aggiornamenti normativi)

**Catena di approvazione**: Principale: RSSI; Secondario: Responsabile delle strutture; Autorità finale: Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.7.1-3; ISMS-POL-A.5.19-23; ISMS-POL-A.5.24-28; ISMS-POL-A.5.30-8.13-14; ISMS-IMP-A.7.4-5-11-S1–S4-UG/TG; ISO/IEC 27001:2022 Controlli A.7.4, A.7.5, A.7.11.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di sicurezza dell'infrastruttura fisica per proteggere gli asset informativi attraverso monitoraggio completo, protezione ambientale e resilienza delle utenze, conformemente ai Controlli A.7.4, A.7.5 e A.7.11 della norma ISO/IEC 27001:2022.

**Approccio a controlli combinati**: Questi tre controlli sono implementati come un Quadro unificato di sicurezza dell'infrastruttura fisica perché operano sulla stessa infrastruttura fisica, creano interdipendenze e condividono processi di valutazione comuni. Ciascun controllo mantiene requisiti distinti ai fini della DdA.

**Allineamento normativo**: nLPD svizzera (Art. 8); RGPD dell'UE (Art. 32); ISO/IEC 27001:2022; FINMA, DORA, NIS2 (applicabilità condizionale).

---

# Perimetro

## Strutture nel perimetro

**Strutture**: Data center on-premise e siti di ripristino di emergenza; sale server e armadi per le telecomunicazioni; uffici aziendali; strutture di colocation (con modello di responsabilità condivisa); strutture remote e temporanee.

## Organizzazioni solo cloud

Le organizzazioni che operano al 100% in ambienti cloud senza strutture di elaborazione delle informazioni on-premise possono indicare i Controlli A.7.4, A.7.5 e A.7.11 come «Non Applicabili» nella DdA. La determinazione «Non Applicabile» DEVE essere documentata con riferimento all'inventario degli asset, alla verifica della sicurezza fisica del provider cloud e alla conferma annuale.

---

# Enunciati di politica

## Monitoraggio della sicurezza fisica (A.7.4)

> *I locali devono essere continuamente monitorati per l'accesso fisico non autorizzato.*

[Organizzazione] DEVE: implementare il controllo degli accessi elettronico a tutti i punti di ingresso/uscita con autenticazione, registrazione e integrazione con la gestione delle identità; dispiegare sistemi di rilevamento delle intrusioni appropriati alla criticità della struttura; fornire copertura CCTV per gli ingressi, le aree riservate e l'infrastruttura critica; richiedere a tutti i visitatori di registrarsi e di essere accompagnati nelle aree riservate; condurre revisioni periodiche degli accessi; integrare gli eventi di sicurezza fisica con il SIEM (ISMS-POL-A.8.16).

**Prove di conformità**: Attraverso ISMS-IMP-A.7.4-5-11-S1 (Valutazione del monitoraggio fisico), che genera classeur mensili contenenti: log del sistema di controllo degli accessi; verifica della disponibilità e copertura del sistema CCTV; avvisi del sistema di rilevamento delle intrusioni e tempi di risposta; registri di gestione dei visitatori; risultati della revisione degli accessi.

## Protezione ambientale (A.7.5)

> *La protezione contro le minacce fisiche e ambientali deve essere progettata e implementata.*

[Organizzazione] DEVE: condurre una valutazione del rischio ambientale; implementare sistemi di rilevamento e soppressione degli incendi appropriati al tipo di struttura e ai requisiti normativi; installare sistemi di rilevamento dell'acqua e implementare misure di mitigazione delle inondazioni; mantenere temperatura e umidità entro intervalli accettabili; garantire l'integrità strutturale dell'edificio; documentare e testare le procedure di risposta alle emergenze.

**Prove di conformità**: Attraverso ISMS-IMP-A.7.4-5-11-S2 (Valutazione della protezione ambientale), con classeur trimestrali contenenti: risultati dei test del sistema antincendio e certificati di ispezione; log del sistema di rilevamento dell'acqua; dati di monitoraggio della temperatura/umidità con conformità alle soglie; verbali delle prove di evacuazione di emergenza.

## Resilienza delle utenze (A.7.11)

> *Le strutture di elaborazione delle informazioni devono essere protette da guasti di alimentazione e altre interruzioni causate da guasti nelle utenze di supporto.*

[Organizzazione] DEVE: implementare sistemi di alimentazione ininterrotta (UPS) con capacità appropriata alla criticità della struttura; fornire capacità di alimentazione di backup per le strutture critiche; implementare sistemi di raffreddamento con ridondanza appropriata; garantire la connettività delle telecomunicazioni con ridondanza appropriata; monitorare i sistemi di utenza in tempo reale; condurre test regolari dei sistemi di resilienza delle utenze.

**Calendario dei test**:

- Test di failover UPS: Trimestrale
- Test di carico del generatore di backup: Semestrale
- Verifica della ridondanza del raffreddamento: Trimestrale
- Failover delle telecomunicazioni: Annuale

**Prove di conformità**: Attraverso ISMS-IMP-A.7.4-5-11-S3 (Valutazione della resilienza delle utenze), con classeur trimestrali contenenti: log dei test UPS; report dei test di carico del generatore; documenti di verifica della ridondanza del raffreddamento; risultati dei test di failover delle telecomunicazioni.

## Livelli di criticità delle strutture

Le strutture DEVONO essere classificate in livelli di criticità in base alla BIA:

| Livello | Definizione | Monitoraggio | Ambientale | Utenze | Frequenza di revisione |
|---------|-------------|-------------|-----------|--------|----------------------|
| **Livello 1 — Critico** | Data center, sale server principali, siti DR | Monitoraggio SOC 24/7, SLA di risposta <15 min, rilevamento intrusioni obbligatorio | Soppressione + rilevamento incendi, rilevamento acqua in tutte le zone, temperatura 18-27°C ±2°C | UPS N+1 (30 min autonomia ciascuno), generatore di backup (48h carburante), doppio percorso di raffreddamento | Verifica mensile manuale |
| **Livello 2 — Standard** | Uffici aziendali, filiali, sale server non critiche | Monitoraggio 8/5, risposta il giorno lavorativo successivo, rilevamento intrusioni opzionale | Rilevamento incendi (soppressione se valore apparecchiature >CHF 500k), rilevamento acqua solo nelle aree ad alto rischio, temperatura 18-27°C ±5°C | UPS singolo (min. 15 min autonomia), nessun generatore richiesto, raffreddamento singolo | Verifica trimestrale manuale |

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Responsabilità complessiva del quadro; approvazione della politica; allocazione del budget; reporting esecutivo |
| **Responsabile delle strutture** | Operazioni quotidiane dell'infrastruttura fisica; manutenzione dei sistemi ambientali e di utenza; gestione dei fornitori |
| **Responsabile delle Operazioni di Sicurezza** | Implementazione del monitoraggio della sicurezza fisica; gestione del controllo degli accessi; operazioni CCTV; coordinamento della risposta agli incidenti |
| **Proprietari dei sistemi** | Requisiti di sicurezza fisica per i sistemi di proprietà; coordinamento del posizionamento delle apparecchiature |
| **Operazioni IT** | Integrazione fisico-logica della sicurezza (SIEM); infrastruttura di rete per i sistemi di sicurezza |
| **Audit interno** | Audit annuale di conformità alla sicurezza fisica; test dei controlli; revisione delle prove |

---

# Governance e conformità

## Punteggio di conformità

| Intervallo di punteggio | Valutazione | Azione richiesta |
|------------------------|-------------|------------------|
| >90% | Eccellente | Mantenere i controlli attuali |
| 75-89% | Buono | Affrontare le lacune nel prossimo ciclo di revisione |
| 60-74% | Accettabile | Sviluppare un piano di rimedio entro 30 giorni |
| <60% | Non conforme | Rimedio immediato richiesto, escalation al RSSI |

**Metodologia di punteggio** (metriche ponderate):

| Metrica | Peso | Fonte di misurazione |
|---------|------|---------------------|
| Disponibilità del sistema di controllo degli accessi | 20% | Log del sistema di controllo degli accessi |
| Conformità dei parametri ambientali (temp/umidità entro le soglie) | 20% | Sistema di monitoraggio ambientale |
| Tasso di successo dei test di resilienza delle utenze | 15% | Documenti dei test (classeur S3) |
| Stato operativo dei sistemi di rilevamento incendi/acqua | 15% | Documenti di ispezione |
| Conformità ai tempi di risposta agli incidenti di sicurezza | 15% | Sistema di gestione degli incidenti |
| Conformità alla gestione dei visitatori | 10% | Log dei visitatori |
| Completamento della formazione sulla sicurezza fisica | 5% | Documenti LMS |

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Monitoraggio della sicurezza fisica** | Sorveglianza continua e rilevamento dei tentativi di accesso fisico e delle condizioni ambientali |
| **Minaccia ambientale** | Pericoli naturali o artificiali che possono danneggiare le strutture (incendio, alluvione, temperature estreme) |
| **Utenze di supporto** | Servizi di infrastruttura necessari per il funzionamento della struttura (alimentazione, raffreddamento, telecomunicazioni) |
| **Livello di criticità della struttura** | Classificazione delle strutture in base all'impatto aziendale e al livello di protezione richiesto |
| **Ridondanza N+1** | Configurazione in cui un'unità aggiuntiva è disponibile oltre al requisito minimo |
| **Registro delle lacune** | Elenco documentato delle carenze dei controlli con monitoraggio del rimedio |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data da definire] |
| **Responsabile delle strutture** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti di [Organizzazione] per la sicurezza dell'infrastruttura fisica. Le procedure di attuazione sono documentate in ISMS-IMP-A.7.4-5-11 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->

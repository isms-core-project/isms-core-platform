<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S5-IT:framework:POL:a.5.19-23-s5 -->
**ISMS-POL-A.5.19-23-S5 — Sicurezza dei servizi cloud**
**Controllo A.5.23: Sicurezza delle informazioni per l'utilizzo dei servizi cloud**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza dei servizi cloud |
| **Tipo di documento** | Sezione di politica |
| **Identificativo del documento** | ISMS-POL-A.5.19-23-S5 |
| **Autore del documento** | Responsabile della Sicurezza delle Informazioni (RSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Catena di approvazione**: RSSI → RSI → Responsabile team architettura cloud → Responsabile Legale/Conformità → Direzione generale

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.5.19-23; ISMS-IMP-A.5.19-23.S1-S5-UG/TG; ISMS-REF-A.5.23; ISO/IEC 27001:2022 Controllo A.5.23; ISO/IEC 27017:2026; ISO/IEC 27018:2025

---

# Scopo

La presente sezione definisce i requisiti per l'acquisizione sicura, l'utilizzo, la gestione e l'uscita dai servizi cloud. Stabilisce il quadro del ciclo di vita dei servizi cloud e i controlli di sicurezza specifici del cloud.

**Principio fondamentale — «Il cloud è il computer di qualcun altro»**: I servizi cloud operano su un'infrastruttura che non si controlla, in giurisdizioni che non si governano, con accesso da parte di personale che non si è verificato. Il modello di responsabilità condivisa significa che i fallimenti della sicurezza possono verificarsi nel dominio di entrambe le parti — ma le conseguenze in termini di conformità e reputazione ricadono su [Organizzazione]. Questa politica richiede una gestione sistematica del ciclo di vita del cloud, dalla selezione all'uscita, con verifica continua che le dichiarazioni dei fornitori in materia di sicurezza corrispondano alla realtà operativa.

**ISO/IEC 27001:2022 Allegato A.5.23**

> *Devono essere stabiliti processi di acquisizione, utilizzo, gestione e uscita dai servizi cloud conformemente ai requisiti di sicurezza delle informazioni dell'organizzazione.*

---

# Perimetro

## Modelli di servizi cloud

| Modello | Descrizione | Responsabilità di [Organizzazione] |
|---------|-------------|----------------------------------|
| **IaaS** | Infrastruttura come servizio | SO, middleware, applicazioni, dati |
| **PaaS** | Piattaforma come servizio | Applicazioni, dati |
| **SaaS** | Software come servizio | Dati, configurazione utente |
| **XDR/SECaaS** | Sicurezza come servizio | Configurazione, politica, risposta |
| **FaaS** | Funzione come servizio | Codice, dati |
| **DaaS** | Desktop come servizio | Dati utente, politica endpoint |

## Modelli di dispiegamento cloud

| Modello | Descrizione | Considerazione |
|---------|-------------|---------------|
| **Pubblico** | Infrastruttura condivisa, multi-tenant | Isolamento dei dati, conformità |
| **Privato** | Infrastruttura dedicata | Costo, onere gestionale |
| **Ibrido** | Combinazione di pubblico e privato | Complessità di integrazione |
| **Multi-cloud** | Più fornitori cloud | Portabilità, coerenza |
| **Comunitario** | Condiviso da una comunità specifica | Governance, rischio condiviso |

---

# Ciclo di vita dei servizi cloud

## Panoramica del ciclo di vita

```
┌─────────────────────────────────────────────────────────┐
│           CICLO DI VITA DEI SERVIZI CLOUD               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  SELEZIONE → IMPLEMENTAZIONE → ESERCIZIO → USCITA       │
│      │             │              │           │         │
│  Requisiti    Config.         Monitoraggio  Piano       │
│  Valutazione  Integrazione    Revisione     Esportaz.   │
│  Rischi       Migrazione      Patch         Transiz.    │
│  Contratto    Test            Incidenti     Cancellaz.  │
│  Approvazione Messa in prod.  Modifiche     Verifica    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# Selezione e valutazione

## Requisiti preliminari alla selezione

| Requisito | Descrizione |
|-----------|-------------|
| Necessità aziendale | Giustificazione aziendale documentata |
| Classificazione dei dati | Classificazione dei dati da trattare |
| Requisiti di conformità | Obblighi normativi e contrattuali |
| Requisiti di integrazione | Sistemi e flussi di dati interessati |
| Requisiti di sicurezza | Controlli minimi di sicurezza richiesti |

## Lista di controllo per la valutazione della sicurezza

| Requisito | Metodo di verifica |
|-----------|-------------------|
| Certificazione ISO 27001 o SOC 2 | Revisione del certificato/report |
| Cifratura a riposo e in transito | Documentazione tecnica |
| Autenticazione multi-fattore | Capacità di configurazione |
| Registrazione e monitoraggio degli accessi | Verifica delle funzionalità |
| Opzioni di residenza dei dati | Revisione contrattuale e tecnica |
| Processo di notifica degli incidenti | Contratto e documentazione |
| Capacità di backup e ripristino | Documentazione tecnica |
| Programma di test di penetrazione | Disponibilità dei report |
| Gestione delle vulnerabilità | Documentazione dei processi |
| Trasparenza sui sub-responsabili | Revisione dell'elenco |

## Requisiti di approvazione

| Classificazione dei dati | Approvazione richiesta |
|--------------------------|----------------------|
| Limitato | RSSI + Proprietario aziendale + Legale |
| Riservato | RSI + Proprietario aziendale |
| Interno | Proprietario aziendale + revisione sicurezza |
| Pubblico | Proprietario aziendale |

---

# Implementazione e configurazione

## Principi di configurazione sicura

| Principio | Implementazione |
|-----------|----------------|
| **Minimo privilegio** | Permessi minimi per utenti e servizi |
| **Difesa in profondità** | Livelli multipli di controlli |
| **Sicurezza per impostazione predefinita** | Partire in modalità sicura |
| **Separazione** | Isolare ambienti, dati, accessi |
| **Cifratura** | Proteggere i dati a riposo e in transito |
| **Registrazione** | Piste di audit complete |

## Requisiti di configurazione

| Dominio di controllo | Requisiti |
|---------------------|----------|
| **Identità e accessi** | Integrazione SSO, AMF applicata, RBAC implementato |
| **Protezione dei dati** | Cifratura abilitata, classificazione applicata, DLP configurato |
| **Sicurezza di rete** | Restrizioni di accesso, connettività sicura, segmentazione |
| **Registrazione e monitoraggio** | Log di audit attivi, integrazione SIEM, avvisi configurati |
| **Backup e ripristino** | Backup automatizzati, ripristino testato |

---

# Gestione operativa

## Attività di sicurezza continue

| Attività | Frequenza | Responsabilità |
|----------|-----------|----------------|
| Revisione degli accessi | Trimestrale | Proprietario aziendale + IT |
| Revisione della configurazione | Semestrale | Sicurezza + IT |
| Valutazione della sicurezza | Annuale | Sicurezza |
| Verifica della conformità | Annuale | Conformità |
| Test dei backup | Semestrale | Operazioni IT |
| Esercitazione risposta agli incidenti | Annuale | Sicurezza |

---

# Modello di responsabilità condivisa

## Matrice delle responsabilità

```
┌──────────────────────────────────────────────────────────────┐
│      RESPONSABILITÀ CONDIVISA PER MODELLO DI SERVIZIO        │
├─────────────────────┬──────────┬──────────┬──────────────────┤
│ Responsabilità      │  IaaS    │  PaaS    │  SaaS            │
├─────────────────────┼──────────┼──────────┼──────────────────┤
│ Dati                │   VOI    │   VOI    │   VOI            │
│ Applicazioni        │   VOI    │   VOI    │  FORNITORE        │
│ Esecuzione          │   VOI    │ FORNITORE│  FORNITORE        │
│ Middleware          │   VOI    │ FORNITORE│  FORNITORE        │
│ Sistema operativo   │   VOI    │ FORNITORE│  FORNITORE        │
│ Virtualizzazione    │ FORNITORE│ FORNITORE│  FORNITORE        │
│ Infrastruttura      │ FORNITORE│ FORNITORE│  FORNITORE        │
│ Fisico              │ FORNITORE│ FORNITORE│  FORNITORE        │
└─────────────────────┴──────────┴──────────┴──────────────────┘
VOI = Responsabilità di [Organizzazione]
FORNITORE = Responsabilità del fornitore di servizi cloud
```

Per ogni servizio cloud, documentare: responsabilità del fornitore; responsabilità dell'organizzazione; responsabilità condivise; lacune; misure compensative per le lacune.

---

# Strategia di uscita

## Pianificazione dell'uscita

Tutti i servizi cloud devono avere una strategia di uscita documentata includente: eventi scatenanti; modalità di esportazione dei dati; servizi alternativi; approccio di migrazione; stima della tempistica; risorse necessarie; stima dei costi.

## Opzioni della strategia di uscita

**Principio di selezione (Regola 90-5-5):**

| Strategia | Utilizzo previsto | Fattori principali |
|-----------|------------------|-------------------|
| **Migrazione cloud-verso-cloud** | 90%+ dei servizi | Costo, rapidità, elasticità, innovazione |
| **Transizione ibrida** | 5-10% dei servizi | Conformità normativa, latenza, ottimizzazione costi |
| **Rimpatrio on-premises** | < 5% dei servizi | Mandato normativo, estrema inversione dei costi |

---

### Migrazione cloud-verso-cloud (Strategia di uscita principale)

La migrazione verso un fornitore cloud alternativo è la **strategia di uscita predefinita** per la maggior parte dei servizi grazie alle minori spese in conto capitale, ai tempi più brevi, al mantenimento dell'elasticità e al ridotto onere operativo.

**Vantaggi strategici**:

| Vantaggio | Beneficio |
|-----------|-----------|
| Nessun acquisto di infrastruttura | Zero CAPEX, modello di spesa operativa preservato |
| Transizione più rapida | 1-6 mesi tipici vs. 6-18 mesi per soluzioni on-premises |
| Elasticità mantenuta | Capacità di picco, scalabilità automatica, pay-per-use |
| Capacità moderne | Accesso ai servizi nativi cloud (container, serverless, IA/ML) |

**Fasi di migrazione (cloud-verso-cloud)**:

| Fase | Durata | Attività |
|------|--------|---------|
| Valutazione | 2-4 settimane | Valutazione del fornitore alternativo, analisi costi, valutazione rischi |
| Preparazione | 4-8 settimane | Creazione account, connettività, configurazione IAM |
| Migrazione | 4-12 settimane | Migrazione dati, dispiegamento applicativo, test di integrazione |
| Validazione | 2-4 settimane | Test delle performance, validazione della sicurezza |
| Pulizia | 1-2 settimane | Dismissione ambiente sorgente, verifica cancellazione dati |

**Durata totale tipica: 3-6 mesi**

**Quando è ottimale**: servizio nativo del cloud; domanda variabile; assenza di obbligo normativo di hosting fisico on-premises; TCO cloud favorevole; distribuzione geografica richiesta.

---

### Transizione ibrida (Rimpatrio parziale)

L'approccio ibrido mantiene alcuni carichi di lavoro nel cloud rimpatriando al contempo componenti selezionati verso un'infrastruttura on-premises.

**Scenari ibridi tipici**:

| Scenario | Componente cloud | Componente on-premises | Giustificazione |
|----------|-----------------|----------------------|----------------|
| **Sovranità dei dati** | Livello applicativo, calcolo | Database con dati sensibili | Requisiti normativi di residenza |
| **Ottimizzazione dei costi** | Capacità di picco, fuori-produzione | Baseline di produzione prevedibile | Baseline on-premises, picchi cloud |
| **Sensibile alla latenza** | Backup/DRP, analisi | Elaborazione transazionale in tempo reale | Ridurre la latenza per carichi critici |
| **Migrazione progressiva** | Nuovi servizi nativi cloud | Sistemi legacy in refactoring | Transizione graduale 12-24 mesi |

**Durata tipica: 6-12 mesi**

**Quando è ottimale**: requisiti normativi che impongono storage on-premises; carichi di lavoro con estrema sensibilità alla latenza; capacità on-premises esistente disponibile; profilo di costo misto.

---

### Rimpatrio on-premises (Ricostruzione completa)

**⚠️ CRITICO: Il rimpatrio on-premises è economicamente giustificato in meno del 5% degli scenari di uscita dal cloud.**

**Scenari realistici**:

| Scenario | Giustificazione | Probabilità |
|----------|-----------------|-------------|
| **Mandato normativo** | Obbligo legale di infrastruttura isolata (air gap) | Bassa-Media |
| **Inversione dei costi** | Costi cloud > TCO on-premises su 3-5 anni per carichi stabili ad alto volume | Bassa |
| **Indipendenza strategica** | Eliminare tutte le dipendenze esterne per infrastrutture critiche | Molto bassa |
| **Fallimento del fornitore** | Insolvenza, violazione irreparabile, perdita di accesso geopolitico | Molto bassa |
| **Rischio di concentrazione** | Diversificazione DORA art. 28.9 | Bassa |

**Stima dei costi (Organizzazione di medie dimensioni ~300 collaboratori)**:

| Componente | CAPEX (Anno 0) | OPEX (Annuale) |
|-----------|----------------|----------------|
| Calcolo | CHF 150K-300K | — |
| Storage | CHF 50K-150K | — |
| Rete | CHF 40K-80K | — |
| Licenze software | CHF 20K-50K | CHF 30K-100K |
| Personale (3-5 ETP) | — | CHF 300K-600K |
| Manutenzione | — | CHF 30K-80K |
| **TOTALE** | **CHF 390K-990K** | **CHF 470K-1,11M** |

**TCO totale su 5 anni: CHF 2,94M–7,04M**

**Quando NON è giustificato**: i costi cloud sono elevati ma il carico è elastico (ottimizzare il cloud); percezione manageriale «vogliamo il controllo» (un ibrido raggiunge il controllo); aumento a breve termine delle tariffe cloud (negoziare un accordo Enterprise).

**Durata tipica: 9-18 mesi**

---

### Matrice di decisione

```
INIZIO: Uscita dal servizio cloud richiesta
                │
                ▼
Esiste un MANDATO NORMATIVO per l'on-premises?
(sovranità dei dati, air gap)
    │ SÌ                          │ NO
    ▼                             ▼
On-premises o Ibrido    Costo cloud > CHF 500K/anno
                        E carico stabile (senza picchi)?
                            │ SÌ          │ NO
                            ▼             ▼
                    Effettuare analisi  Cloud-verso-cloud
                    TCO                 (Predefinito)
                            │
                    TCO on-premises < 70%
                    del cloud su 5 anni?
                        │ SÌ    │ NO
                        ▼       ▼
                   On-premises  Cloud-verso-
                   o Ibrido     cloud
```

**Confronto tra strategie**:

| Fattore | Cloud-verso-cloud | Ibrido | On-premises |
|---------|-----------------|--------|-------------|
| **CAPEX** | ✅ Nessuno | 🟡 CHF 95K-700K | ❌ CHF 390K-990K |
| **OPEX (Annuale)** | 🟡 CHF 50K-500K+ | 🟡 CHF 80K-300K | ❌ CHF 470K-1,11M |
| **TCO 5 anni** | 🟡 CHF 250K-2,5M+ | 🟡 CHF 335K-1,6M | ❌ CHF 2,94M-7,04M |
| **Durata** | ✅ 3-6 mesi | 🟡 6-12 mesi | ❌ 9-18 mesi |
| **Elasticità** | ✅ Mantenuta | 🟡 Parziale | ❌ Persa |
| **Complessità operativa** | ✅ Bassa | 🟡 Media | ❌ Alta |
| **Flessibilità normativa** | 🟡 Dipende dal fornitore | ✅ Alta | ✅ Controllo totale |

---

### Revisione e test annuali

La fattibilità della strategia di uscita DEVE essere rivista e testata annualmente.

**Requisiti di test (conformi DORA art. 28.6)**:

| Strategia | Requisito di test | Prove | Frequenza |
|-----------|-----------------|-------|-----------|
| Cloud-verso-cloud | Esportare un sottoinsieme di dati (10-20%), dispiegare presso il fornitore alternativo | Screenshot PoC, report di validazione delle esportazioni | Annuale |
| Ibrido | Testare la connettività ibrida, la latenza di sincronizzazione dei dati, le procedure di failover | Metriche di performance, risultati dei test | Annuale |
| On-premises | Aggiornare il calcolo TCO, verificare disponibilità/capacità dell'infrastruttura | Foglio di calcolo TCO, report di pianificazione capacità | Annuale |

**Profondità dei test per criticità**:

| Criticità del servizio | Profondità dei test | Dimensione del campione |
|----------------------|---------------------|------------------------|
| Critico | Simulazione completa di uscita | 100% dei dati |
| Alto | Test su campione significativo | 50% dei dati |
| Medio | Campione rappresentativo | 10-20% dei dati |
| Basso | Solo verifica documentale | Revisione documentale |

---

# Requisiti di sicurezza specifici del cloud

## Gestione delle identità e degli accessi

| Requisito | Implementazione |
|-----------|----------------|
| Identità federata | SSO tramite il fornitore d'identità organizzativo |
| Applicazione dell'AMF | Obbligatoria per tutti gli utenti, imperativa per gli amministratori |
| Accesso privilegiato | Just-in-time, a tempo limitato, supervisionato |
| Account di servizio | Inventario, rotazione delle credenziali, minimo privilegio |
| Revisioni degli accessi | Certificazione periodica dei diritti di accesso |

## Protezione dei dati

| Requisito | Implementazione |
|-----------|----------------|
| Cifratura in transito | TLS 1.2+ per tutte le comunicazioni |
| Cifratura a riposo | Chiavi gestite dal fornitore o dal cliente |
| Gestione delle chiavi | Storage sicuro delle chiavi, politica di rotazione |
| Classificazione dei dati | Etichette applicate, controlli applicati |
| Residenza dei dati | Localizzazione del trattamento documentata e verificata |
| Segregazione dei dati | Isolamento logico o fisico secondo i requisiti |

## Monitoraggio della sicurezza

| Requisito | Implementazione |
|-----------|----------------|
| Registrazione degli audit | Tutti gli eventi rilevanti per la sicurezza sono registrati |
| Centralizzazione dei log | Log esportati verso il SIEM organizzativo |
| Avvisi | Gli eventi di sicurezza attivano gli avvisi appropriati |
| Conservazione | Log conservati per almeno 12 mesi |

---

# Riferimento incrociato: Continuità operativa e DRP

Le strategie di uscita riguardano le **transizioni pianificate e volontarie** dai servizi cloud. Per gli **scenari di emergenza** che coinvolgono il fallimento del fornitore cloud, fare riferimento alla pianificazione della Continuità operativa e del Ripristino di emergenza (ISMS-POL-A.5.30-8.13-14).

| Tipo di scenario | Quadro di pianificazione | Tempistica | Esempio |
|-----------------|-------------------------|-----------|---------|
| **Uscita pianificata** | Questa politica (A.5.23) | 3-18 mesi | Mancato accordo contrattuale, ottimizzazione costi |
| **Failover di emergenza** | BCP/DRP (A.5.30-8.13-14) | Ore-Giorni | Interruzione del fornitore, violazione della sicurezza |

**Requisito DORA art. 28.6**: Gli accordi contrattuali sull'utilizzo di servizi TIC a supporto di funzioni critiche devono includere strategie di uscita, nonché l'obbligo per il fornitore terzo di cooperare durante i processi di uscita.

---

# Riferimenti

| Documento | Relazione |
|-----------|----------|
| ISMS-POL-A.5.19-23 | Quadro di politica genitore |
| ISMS-POL-A.5.19-23-S1 | I fornitori cloud sono fornitori |
| ISMS-POL-A.5.19-23-S2 | Requisiti contrattuali cloud |
| ISMS-POL-A.5.19-23-S3 | Gestione dei sub-responsabili cloud |
| ISMS-POL-A.5.19-23-S4 | Monitoraggio dei servizi cloud |
| ISMS-POL-A.5.30-8.13-14 | BCP/DRP per failover di emergenza |
| ISO/IEC 27017:2026 | Controlli di sicurezza per i servizi cloud |
| ISO/IEC 27018:2025 | Protezione della privacy nel cloud |

---

**Documento successivo**: ISMS-POL-A.5.19-23-S6 — Metodologia di valutazione e automazione

<!-- QA_VERIFIED: 2026-04-03 -->

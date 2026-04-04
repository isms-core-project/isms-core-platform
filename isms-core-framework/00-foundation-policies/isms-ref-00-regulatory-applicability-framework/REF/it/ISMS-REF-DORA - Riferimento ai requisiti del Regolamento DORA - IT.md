<!-- ISMS-CORE:REF:ISMS-REF-DORA-IT-digital-operational-resilience-act:framework:REF:dora -->
**ISMS-REF-DORA — Riferimento ai requisiti del Regolamento DORA**
**Requisiti di resilienza operativa digitale per il settore finanziario UE (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento ai requisiti DORA |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-DORA |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | RSSI (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale (o in caso di aggiornamenti degli standard tecnici normativi DORA)

**Distribuzione**: Team di conformità, RSSI, Consulenza legale (per le organizzazioni soggette a DORA)

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione. Non fa parte del SGSI e non stabilisce requisiti vincolanti a meno che [Organizzazione] non sia un'entità regolamentata da DORA.

**Determinazione dell'applicabilità**: I requisiti DORA si applicano SOLO SE [Organizzazione] è un'entità finanziaria operante nell'UE, è designata fornitore critico o importante di servizi TIC a entità finanziarie UE, o ha obblighi contrattuali di soddisfare i requisiti DORA.

---

# Scopo e ambito del documento

## Scopo

Questo documento fornisce una panoramica tecnica dei requisiti del Regolamento (UE) 2022/2554 sulla resilienza operativa digitale (DORA) per le entità del settore finanziario UE. È inteso a supportare: la sensibilizzazione ai requisiti DORA, la comprensione dei cinque pilastri DORA, il contesto per i fornitori di servizi TIC a entità finanziarie UE e la mappatura dei requisiti DORA ai controlli ISO 27001:2022.

## Relazione con il SGSI

Questo documento è un **riferimento tecnico non vincolante** a meno che [Organizzazione] non sia soggetta a DORA (come determinato in ISMS-POL-00 Sezione 3.2).

**Se [Organizzazione] È regolamentata da DORA**: I requisiti DORA diventano Livello 1 (Conformità obbligatoria). I controlli SGSI devono dimostrare la conformità DORA.

**Se [Organizzazione] NON È regolamentata da DORA**: DORA rimane Livello 3 (Riferimento informativo). Il SGSI segue solo la ISO 27001:2022.

**Se [Organizzazione] fornisce servizi TIC a entità finanziarie DORA**: Potrebbe essere designata fornitore di servizi TIC critico o importante. I requisiti contrattuali probabilmente faranno riferimento agli standard DORA.

---

# Panoramica e applicabilità DORA

## Cos'è DORA?

Il **Regolamento (UE) 2022/2554** sulla resilienza operativa digitale per il settore finanziario è entrato in vigore il 16 gennaio 2023 con applicazione dal **17 gennaio 2025**.

**Scopo**: Stabilire requisiti uniformi per la resilienza operativa digitale nel settore finanziario UE, affrontando l'approccio frammentato al rischio TIC, le crescenti minacce informatiche, il rischio di concentrazione nei fornitori di servizi TIC di terze parti, la necessità di segnalazione armonizzata degli incidenti e l'importanza della condivisione dell'intelligence sulle minacce.

**Base giuridica**: Regolamento UE (direttamente applicabile in tutti gli Stati membri, non richiede recepimento nazionale)

**Autorità di vigilanza**: Autorità europee di vigilanza (AEV):

- Autorità Bancaria Europea (ABE/EBA)
- Autorità Europea degli Strumenti Finanziari e dei Mercati (ESMA)
- Autorità Europea delle Assicurazioni e delle Pensioni Aziendali e Professionali (EIOPA)
- Più autorità competenti nazionali

## Chi deve conformarsi a DORA?

**Entità finanziarie** (Articolo 2):

| Categoria | Esempi | Autorità di vigilanza |
|-----------|--------|----------------------|
| **Enti creditizi** | Banche | ABE + CA nazionale |
| **Istituti di pagamento** | Fornitori di servizi di pagamento | ABE + CA nazionale |
| **Istituti di moneta elettronica** | Emittenti di e-money | ABE + CA nazionale |
| **Imprese di investimento** | Mediatori, gestori di portafogli | ESMA + CA nazionale |
| **Fornitori di servizi per le cripto-attività** | Borse crypto, depositari | ESMA + CA nazionale |
| **Depositari centrali di titoli** | CSD | ESMA + CA nazionale |
| **Sedi di negoziazione** | Borse, MTF | ESMA + CA nazionale |
| **Gestori di fondi di investimento alternativi** | Hedge fund, PE fund | ESMA + CA nazionale |
| **Imprese di assicurazione e riassicurazione** | Assicuratori, riassicuratori | EIOPA + CA nazionale |
| **Intermediari assicurativi** | Broker assicurativi | EIOPA + CA nazionale |
| **Agenzie di rating del credito** | Agenzie di rating | ESMA |
| **Fornitori di servizi di crowdfunding** | Piattaforme di crowdfunding | ESMA + CA nazionale |

**Fornitori di servizi TIC di terze parti** (Capitolo V, Sezione II): Fornitori di servizi cloud, fornitori di software, fornitori di analisi dei dati, fornitori di data center. Se designati "critici": soggetti al quadro di vigilanza DORA.

## Determinazione dell'applicabilità

**DORA si applica a [Organizzazione] SE**:

| Criterio | Stato | Evidenza |
|----------|-------|----------|
| Entità finanziaria operante nell'UE | ⬜ Sì ⬜ No | [Tipo di licenza / Paese] |
| Banca o ente creditizio UE | ⬜ Sì ⬜ No | [Licenza bancaria] |
| Istituto di pagamento o moneta elettronica UE | ⬜ Sì ⬜ No | [Licenza di pagamento] |
| Impresa di investimento UE | ⬜ Sì ⬜ No | [Licenza di investimento] |
| Fornitore di servizi per cripto-attività UE | ⬜ Sì ⬜ No | [Licenza MiCAR] |
| Impresa di assicurazione o riassicurazione UE | ⬜ Sì ⬜ No | [Licenza assicurativa] |
| Fornitore critico di servizi TIC di terze parti | ⬜ Sì ⬜ No ⬜ In attesa | [Lettera di designazione] |

---

# Panoramica dei cinque pilastri DORA

DORA organizza i requisiti in cinque pilastri:

```
┌─────────────────────────────────────────────────────────────────┐
│                    CINQUE PILASTRI DORA                         │
├─────────────────────────────────────────────────────────────────┤
│  CAPITOLO II:  Quadro di gestione del rischio TIC               │
│               Articoli 5-16                                      │
│               - Governance e strategia                           │
│               - Identificazione, protezione, rilevamento         │
│               - Risposta e recupero                              │
│               - Apprendimento ed evoluzione                      │
├─────────────────────────────────────────────────────────────────┤
│  CAPITOLO III: Gestione e segnalazione incidenti TIC            │
│               Articoli 17-23                                     │
│               - Rilevamento e classificazione degli incidenti    │
│               - Procedure di risposta agli incidenti             │
│               - Segnalazione alle autorità competenti            │
├─────────────────────────────────────────────────────────────────┤
│  CAPITOLO IV:  Test di resilienza operativa digitale            │
│               Articoli 24-27                                     │
│               - Programmi di test                                │
│               - Test avanzati (TLPT)                             │
│               - Principio di proporzionalità                     │
├─────────────────────────────────────────────────────────────────┤
│  CAPITOLO V:   Gestione del rischio TIC di terze parti          │
│               Articoli 28-44                                     │
│               - Quadro del rischio di terze parti                │
│               - Requisiti contrattuali                           │
│               - Vigilanza sui fornitori critici                  │
├─────────────────────────────────────────────────────────────────┤
│  CAPITOLO VI:  Accordi di condivisione delle informazioni       │
│               Articolo 45                                        │
│               - Condivisione dell'intelligence sulle minacce     │
└─────────────────────────────────────────────────────────────────┘
```

## Principio di proporzionalità

DORA applica la proporzionalità (Articolo 4): i requisiti sono graduati in base alle dimensioni, alla natura, alla portata e alla complessità delle attività e al profilo di rischio complessivo. Le piccole imprese di investimento non interconnesse beneficiano di un regime semplificato.

---

# Capitolo II — Quadro di gestione del rischio TIC

## Panoramica (Articoli 5-16)

Le entità finanziarie devono stabilire, mantenere e rivedere un quadro di gestione del rischio TIC che garantisca resilienza, continuità e sicurezza dei sistemi TIC.

**Articolo 5: Governance e organizzazione**

- L'organo di gestione è in ultima istanza responsabile del rischio TIC
- Approvazione del quadro di gestione del rischio TIC
- Allocazione di ruoli e responsabilità chiari
- Risorse sufficienti per la gestione del rischio TIC
- Linee di segnalazione interna all'organo di gestione

**Mappatura ISO 27001:2022**: Clausola 5.1, 5.3, A.5.1, A.5.2

---

**Articolo 6: Quadro di gestione del rischio TIC**

Il quadro completo comprende: strategie, politiche, procedure; sistemi e strumenti TIC; politiche di sicurezza TIC; politiche di continuità TIC; piani di risposta e recupero; test TIC; audit TIC; rischio TIC di terze parti.

**Mappatura ISO 27001:2022**: Clausole 4-10 (intero SGSI), A.5.1, A.5.9, A.8.13, A.5.29-5.30

---

**Articolo 8: Identificazione**

- Inventario completo degli asset TIC e informativi
- Identificazione di tutte le fonti di rischio TIC
- Metodologia di valutazione del rischio allineata alla criticità aziendale
- Documentazione delle sedi di elaborazione e flussi di dati
- Identificazione dei sistemi TIC legacy e valutazione del rischio

**Mappatura ISO 27001:2022**: A.5.9, A.5.12, Clausola 6.1.2

**Requisiti specifici DORA**: Identificazione esplicita dei sistemi legacy, mappatura delle interdipendenze, mappatura dei dati con sedi di elaborazione, classificazione dell'impatto aziendale.

---

**Articolo 9: Protezione e prevenzione**

Protezione dei sistemi TIC tramite: politiche, procedure, protocolli; strumenti di sicurezza TIC; crittografia; segmentazione della rete; controllo degli accessi; sicurezza fisica; gestione delle modifiche.

**Mappatura ISO 27001:2022**: A.8.1, A.8.2-8.5, A.8.7, A.8.9, A.8.20-8.24, A.7.4

**Enfasi DORA**: La segmentazione della rete è esplicitamente richiesta (non opzionale); la crittografia è obbligatoria per i dati sensibili; l'autenticazione a più fattori è attesa per l'accesso privilegiato.

---

**Articolo 10: Rilevamento**

- Meccanismi di monitoraggio continuo
- Rilevamento di attività anomale
- Capacità di allerta in tempo reale
- Correlazione degli eventi di sicurezza
- Integrazione dell'intelligence sulle minacce

**Mappatura ISO 27001:2022**: A.8.15, A.8.16, A.5.24-5.25, A.5.7

**Esempi tecnologici**: SIEM, EDR, analisi del traffico di rete, UEBA, piattaforme di intelligence sulle minacce.

---

**Articolo 11: Risposta e recupero**

- Piani di risposta agli incidenti TIC
- Procedure di gestione delle crisi
- Piani di comunicazione (interno ed esterno)
- Piani di continuità operativa (BCP)
- Piani di disaster recovery (DRP)
- Obiettivi di tempo di ripristino (RTO)
- Obiettivi di punto di ripristino (RPO)

**Mappatura ISO 27001:2022**: A.5.24-5.28, A.5.29-5.30, A.8.13-8.14

**Aspettative DORA**: RTO per funzioni critiche tipicamente 2-4 ore; RPO per dati critici quasi zero; revisione post-incidente obbligatoria.

---

**Articolo 12: Apprendimento ed evoluzione**

- Revisioni post-incidente
- Analisi delle cause profonde
- Implementazione di azioni correttive
- Integrazione delle lezioni apprese
- Miglioramento continuo del quadro del rischio TIC

**Mappatura ISO 27001:2022**: A.5.27, Clausola 10.1-10.2

---

**Articolo 15: Sensibilizzazione e formazione in materia di sicurezza TIC**

- Programmi regolari di sensibilizzazione alla sicurezza TIC
- Formazione basata sul ruolo per il personale TIC
- Simulazioni di phishing e test
- Misurazione dell'efficacia della formazione

**Mappatura ISO 27001:2022**: A.6.3

**Enfasi DORA**: I programmi di formazione devono essere documentati e misurabili; formazione annuale obbligatoria minima; test di phishing atteso come pratica standard.

---

**Articolo 16: Politiche relative alle TIC**

Le entità finanziarie devono stabilire politiche TIC che coprono: sicurezza TIC, continuità TIC, gestione delle modifiche TIC, operazioni TIC, gestione dei progetti TIC, sicurezza della rete, crittografia e gestione delle chiavi.

**Revisione delle politiche**: Minimo annuale, o in caso di modifiche significative.

---

# Capitolo III — Gestione e segnalazione degli incidenti TIC

## Panoramica (Articoli 17-23)

Le entità finanziarie devono avere processi per rilevare, gestire, notificare e segnalare gli incidenti relativi alle TIC.

**Articolo 17: Processo di gestione degli incidenti TIC**

- Indicatori di allerta precoce
- Procedure di rilevamento degli incidenti
- Criteri di classificazione (maggiore vs. non maggiore)
- Procedure di risposta e recupero
- Analisi delle cause profonde
- Procedure di escalation
- Piani di comunicazione

**Classificazione degli incidenti** (Articolo 18): Le entità finanziarie classificano gli incidenti in base a criticità, durata, perdita di dati, diffusione geografica e impatto reputazionale.

**Indicatori di incidenti principali**: Interruzione significativa delle funzioni critiche; indisponibilità del servizio superiore a una soglia; violazione dei dati che colpisce un gran numero di clienti; perdita finanziaria significativa; rischio sistemico potenziale.

---

**Articolo 19: Notifica iniziale e rapporti intermedi**

**Requisito**: Le entità finanziarie devono notificare alle autorità competenti gli **incidenti principali relativi alle TIC** secondo le tempistiche definite.

**Tempistica di notifica**:

| Fase | Tempistica | Contenuto |
|------|-----------|-----------|
| **Notifica iniziale** | Al più presto, entro le ore specificate (tipicamente 4 ore dal rilevamento) | Descrizione dell'incidente, ora di rilevamento, stato, impatto preliminare |
| **Rapporto intermedio** | Su richiesta o in caso di cambiamento significativo dello stato | Valutazione aggiornata, azioni intraprese, risposta in corso |
| **Rapporto finale** | Dopo la risoluzione dell'incidente (es. entro 1 mese) | Causa principale, valutazione dell'impatto, rimedio, lezioni apprese |

**Canali di segnalazione**: Portale dell'autorità competente nazionale; modelli di segnalazione standardizzati (per gli standard tecnici normativi); canali di comunicazione sicuri.

**Mappatura ISO 27001:2022**: A.5.5, A.5.26

**Segnalazione incrociata**: I requisiti di segnalazione DORA possono sovrapporsi con: notifiche di violazione dei dati personali RGPD (Articoli 33-34); segnalazione degli incidenti NIS2; requisiti di segnalazione nazionali degli incidenti.

---

**Articolo 23: Notifica volontaria di significative minacce informatiche**

Le entità finanziarie possono notificare volontariamente alle autorità competenti significative minacce informatiche anche senza un incidente effettivo, per supportare la consapevolezza e la prevenzione a livello di settore.

**Esempi**: Rilevamento di minacce persistenti avanzate (APT), scoperta di vulnerabilità zero-day, campagna ransomware che prende di mira il settore finanziario.

---

# Capitolo IV — Test di resilienza operativa digitale

## Panoramica (Articoli 24-27)

Le entità finanziarie devono stabilire, mantenere e rivedere un solido programma di test di resilienza operativa digitale.

**Articolo 24: Requisiti generali sui test**

**Componenti del programma di test**: valutazioni della vulnerabilità e scansioni; analisi open source; valutazioni della sicurezza della rete; analisi dei gap; revisioni della sicurezza fisica; test basati su scenari; test di compatibilità; test delle prestazioni; test end-to-end.

**Frequenza dei test**: Test di base almeno annualmente; sistemi critici con maggiore frequenza; test innescati dopo modifiche significative.

---

**Articolo 25: Test di strumenti, sistemi e processi TIC**

Le entità finanziarie implementano metodologie di test tra cui:

**1. Valutazioni della vulnerabilità**: Identificazione dei punti deboli, strumenti di scansione automatizzati, revisione manuale ove appropriata, scoring del rischio basato sulla gravità.

**2. Test basati su scenari**: Test di continuità operativa e disaster recovery, esercitazioni di gestione delle crisi, validazione del failover e ridondanza.

**3. Test di compatibilità e prestazioni**: Integrazione di nuovi sistemi, test di capacità e carico, test di stress in condizioni avverse.

---

**Articolo 26: Test avanzati (TLPT)**

**Test di penetrazione guidati dalla minaccia (TLPT)**: Le entità finanziarie designate devono condurre test avanzati almeno ogni **3 anni**.

**Applicabilità TLPT**: Designate dalle autorità competenti; tipicamente grandi entità finanziarie interconnesse; criteri: dimensioni, importanza sistemica, interconnessione.

**Requisiti TLPT**:

**Intelligence sulle minacce**: Scenari di minacce reali; simulazione di minacce persistenti avanzate (APT); basata su TIBER-EU o framework equivalenti.

**Test del red team**: Attacchi simulati su funzioni critiche; vettori di attacco fisici e digitali; elementi di ingegneria sociale; test delle capacità di rilevamento e risposta.

**Test dei controlli**: Esercitazioni purple team (red team + blue team); test del monitoraggio, rilevamento e risposta; validazione delle procedure di risposta agli incidenti.

**Chiusura e rimedio**: Report dettagliato dei risultati; piano di rimedio con scadenze; segnalazione alla direzione e al consiglio; notifica all'autorità di vigilanza.

**Framework di riferimento TLPT**: TIBER-EU (ECB), CBEST (UK), TIBER-NL (Paesi Bassi), iCAST (Irlanda).

---

# Capitolo V — Gestione del rischio TIC di terze parti

## Panoramica (Articoli 28-44)

Le entità finanziarie devono gestire il rischio TIC di terze parti attraverso un quadro completo e una vigilanza.

**Articolo 28: Principi generali**

**Quadro di gestione del rischio di terze parti**: strategia, politiche e procedure; registro dei fornitori di servizi TIC di terze parti; due diligence pre-contrattuale; accordi contrattuali; monitoraggio e vigilanza continui; strategie di uscita.

**Mappatura ISO 27001:2022**: A.5.19, A.5.20, A.5.21, A.5.22, A.5.23

---

**Articolo 29: Valutazione preliminare del rischio di concentrazione TIC**

Le entità finanziarie devono: identificare il rischio di concentrazione nei fornitori di servizi TIC di terze parti; valutare i potenziali single point of failure; considerare fornitori alternativi o strategie di mitigazione; segnalare rischi di concentrazione significativi all'autorità competente.

**Fattori di rischio di concentrazione**: Utilizzo dello stesso fornitore per più funzioni critiche; fornitori alternativi limitati disponibili; concentrazione geografica; catene di dipendenza.

---

**Articolo 30: Disposizioni contrattuali chiave**

**Elementi obbligatori del contratto** per i servizi TIC che supportano funzioni critiche o importanti:

**1. Descrizioni dei servizi**: Definizione chiara dei servizi forniti; SLA; sedi di elaborazione dei dati; supporto agli obblighi di conformità dell'entità finanziaria.

**2. Requisiti di sicurezza**: Misure di protezione dei dati e riservatezza; tempistiche di notifica degli incidenti di sicurezza; restrizioni e approvazioni del sub-appalto; procedure di restituzione e cancellazione dei dati.

**3. Diritti di accesso e audit**: Diritto dell'entità finanziaria di effettuare audit; diritto dell'autorità competente di accesso e audit; diritti di ispezione in loco; accesso alle informazioni per scopi di vigilanza.

**4. Risoluzione e uscita**: Strategie di uscita con periodo di transizione sufficiente; supporto alla portabilità e migrazione dei dati; continuità del servizio durante la transizione; restituzione o cancellazione dei dati.

**5. Giurisdizione e risoluzione delle controversie**: Legge applicabile (legge di uno Stato membro UE); meccanismi di risoluzione delle controversie; obblighi di cooperazione con le autorità di vigilanza.

**Mappatura ISO 27001:2022**: A.5.20, A.5.23

---

**Articolo 31: Registro dei fornitori di servizi TIC di terze parti**

Le entità finanziarie devono mantenere e aggiornare il registro di tutti i fornitori di servizi TIC di terze parti, inclusi: identificazione del fornitore, servizi forniti, classificazione della criticità, date del contratto e rinnovo, paese di stabilimento e sedi di elaborazione dei dati, sub-appaltatori utilizzati.

**Segnalazione**: Presentazione annuale all'autorità competente.

---

**Articoli 32-44: Quadro di vigilanza per i fornitori critici**

**Designazione di fornitore critico**: Le AEV possono designare i fornitori di servizi TIC di terze parti come "critici" in base a: impatto sistemico sulla stabilità finanziaria; numero e natura delle entità finanziarie servite; complessità e criticità dei servizi; sostituibilità e rischio di concentrazione.

**Attività di vigilanza**: Indagini generali e ispezioni in loco; richieste di informazioni e documentazione; raccomandazioni per il rimedio; sanzioni per la non conformità.

---

# Capitolo VI — Accordi di condivisione delle informazioni

## Articolo 45: Condivisione delle informazioni

Le entità finanziarie possono partecipare ad accordi di condivisione delle informazioni per migliorare l'intelligence sulle minacce informatiche e le capacità difensive.

**Informazioni condivisibili permesse**: Informazioni e intelligence sulle minacce informatiche; indicatori di compromissione (IOC); tattiche, tecniche e procedure (TTP); vulnerabilità e avvisi di sicurezza; pratiche di sicurezza efficaci.

**Piattaforme di condivisione**: FS-ISAC (Financial Services ISAC); European Financial ISAC (EU FS-ISAC); CERT e CSIRT nazionali; gruppi di condivisione specifici del settore.

**Mappatura ISO 27001:2022**: A.5.7

---

# Mappatura ISO 27001:2022 a DORA

## Matrice di mappatura dei controlli

| Requisito DORA | Articolo DORA | Controllo ISO 27001:2022 | Analisi delle lacune |
|----------------|---------------|--------------------------|----------------------|
| Governance del rischio TIC | Art. 5 | Clausola 5.1, 5.3, A.5.1, A.5.2 | DORA: responsabilità dell'organo di gestione esplicita |
| Quadro del rischio TIC | Art. 6 | Clausole 4-10 (intero SGSI) | DORA: elementi del quadro più prescrittivi |
| Identificazione degli asset | Art. 8 | A.5.9, A.5.12 | DORA: sistemi legacy espliciti, mappatura dei dati richiesta |
| Protezione e prevenzione | Art. 9 | A.8.1-8.24, A.7.4 | DORA: segmentazione della rete obbligatoria |
| Rilevamento | Art. 10 | A.8.15, A.8.16, A.5.7 | DORA: monitoraggio in tempo reale atteso |
| Risposta e recupero | Art. 11 | A.5.24-5.30, A.8.13-8.14 | DORA: RTO/RPO per funzioni critiche |
| Sensibilizzazione e formazione | Art. 15 | A.6.3 | DORA: programmi di formazione misurabili |
| Segnalazione degli incidenti | Art. 19-20 | A.5.5, A.5.26 | **Specifico DORA**: tempistiche di segnalazione normativa |
| Programma di test | Art. 24-25 | A.5.30, A.8.8 | DORA: requisiti di test più completi |
| TLPT | Art. 26-27 | Nessun equivalente | **Unico DORA**: test di penetrazione guidati dalla minaccia |
| Registro di terze parti | Art. 31 | A.5.19 | DORA: registro prescrittivo e segnalazione |
| Contratti di terze parti | Art. 30 | A.5.20, A.5.23 | **Specifico DORA**: clausole contrattuali obbligatorie |
| Rischio di concentrazione | Art. 29 | Nessuna mappatura diretta | **Unico DORA**: valutazione esplicita del rischio di concentrazione |
| Vigilanza fornitore critico | Art. 32-44 | Nessun equivalente | **Unico DORA**: quadro di vigilanza normativa |
| Condivisione delle informazioni | Art. 45 | A.5.7 | Allineato |

## Lacune principali tra ISO 27001:2022 e DORA

**Lacuna 1: Segnalazione normativa degli incidenti** — DORA richiede la segnalazione obbligatoria alle autorità competenti con tempistiche.

**Lacuna 2: Test di penetrazione guidati dalla minaccia (TLPT)** — DORA richiede TLPT per le entità finanziarie designate ogni 3 anni; nessun equivalente in ISO 27001.

**Lacuna 3: Disposizioni contrattuali di terze parti** — DORA prevede clausole contrattuali obbligatorie specifiche.

**Lacuna 4: Vigilanza del fornitore critico** — Il quadro di vigilanza ESA è unico per DORA.

**Lacuna 5: Rischio di concentrazione** — DORA richiede valutazione e segnalazione esplicite.

---

# Considerazioni sull'implementazione

## Cronologia di conformità DORA

**Se [Organizzazione] è un'entità finanziaria regolamentata da DORA**:

**Gennaio 2025 (Data di applicazione)**: DORA diventa applicabile.

**Linea temporale di preparazione raccomandata**:

**6-12 mesi prima**: Valutazione delle lacune rispetto ai requisiti DORA; miglioramenti del quadro di gestione del rischio TIC; istituzione del processo di segnalazione degli incidenti; revisione della gestione del rischio di terze parti; rinegoziazione dei contratti con i fornitori TIC critici.

**0-6 mesi dopo**: Test della capacità di segnalazione degli incidenti; lancio del programma di test di resilienza operativa digitale; istituzione del registro di terze parti; partecipazione alla condivisione delle informazioni.

**In corso**: Test annuali e miglioramento continuo; segnalazione trimestrale degli incidenti; presentazione annuale del registro di terze parti; ciclo TLPT triennale (se designato).

## Sfide comuni di conformità DORA

**Sfida 1: Sottostima della complessità della segnalazione normativa** — Le tempistiche di segnalazione degli incidenti sono stringenti (notifica iniziale entro ore); l'infrastruttura di segnalazione deve essere testata prima degli incidenti.

**Sfida 2: Rinegoziazione dei contratti di terze parti** — I principali provider cloud potrebbero resistere a termini contrattuali specifici DORA; le tempistiche di negoziazione possono estendersi 6-12 mesi.

**Sfida 3: Preparazione al TLPT** — Le organizzazioni non abituate agli esercizi red team potrebbero incontrare difficoltà; richiede capacità mature di rilevamento e risposta.

**Sfida 4: Valutazione del rischio di concentrazione** — Difficile quantificare il rischio di concentrazione; fornitori alternativi limitati in alcune categorie di servizi.

**Sfida 5: Sfide dei sistemi legacy** — I sistemi più vecchi potrebbero mancare di registrazione e monitoraggio; patch e aggiornamenti potrebbero essere impraticabili.

## Migliori pratiche

- Coinvolgere presto l'autorità competente per ricevere orientamenti
- Utilizzare la ISO 27001 come base, integrando con requisiti specifici DORA
- Stabilire il processo di segnalazione degli incidenti e testarlo trimestralmente
- Dare priorità alle relazioni con i fornitori critici di servizi TIC
- Condurre preparazione TLPT interna anche se non ancora designati
- Partecipare agli accordi di condivisione delle informazioni del settore

---

# Riferimenti e risorse

## Testi giuridici DORA

**Regolamento primario**: Regolamento (UE) 2022/2554 (DORA) — Gazzetta ufficiale dell'UE

**Standard tecnici normativi (RTS)**: Regolamenti delegati della Commissione sulla gestione del rischio TIC, sulla segnalazione degli incidenti, sui test di resilienza operativa digitale e sulla vigilanza delle terze parti.

**Siti web AEV**: EBA: https://www.eba.europa.eu/ | ESMA: https://www.esma.europa.eu/ | EIOPA: https://www.eiopa.europa.eu/

## Standard e framework correlati

**Standard ISO**: ISO/IEC 27001:2022, ISO/IEC 27002:2022, ISO/IEC 27005:2022, ISO 22301:2019.

**Framework TLPT**: TIBER-EU (ECB), CBEST (UK), TIBER-NL (Paesi Bassi), iCAST (Irlanda).

---

# Appendice A: Lista di controllo di autovalutazione della conformità DORA

## Quadro di gestione del rischio TIC (Capitolo II)

| Requisito | Stato | Ubicazione evidence | Note |
|-----------|-------|---------------------|------|
| Approvazione del quadro del rischio TIC da parte dell'organo di gestione | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Funzione di gestione del rischio TIC istituita | ⬜ Sì ⬜ No | | |
| Inventario completo degli asset TIC | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Sistemi legacy identificati e valutati | ⬜ Sì ⬜ No | | |
| Segmentazione della rete implementata | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Crittografia per dati sensibili (riposo e transito) | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Monitoraggio e rilevamento continui | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Piani di continuità operativa e disaster recovery | ⬜ Sì ⬜ No ⬜ Parziale | | |
| RTO/RPO definiti per le funzioni critiche | ⬜ Sì ⬜ No | | |
| Revisioni post-incidente e lezioni apprese | ⬜ Sì ⬜ No | | |
| Formazione annuale sulla sicurezza TIC | ⬜ Sì ⬜ No | | |

## Gestione e segnalazione degli incidenti (Capitolo III)

| Requisito | Stato | Ubicazione evidence | Note |
|-----------|-------|---------------------|------|
| Criteri di classificazione degli incidenti stabiliti | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Definizione degli incidenti principali documentata | ⬜ Sì ⬜ No | | |
| Processo di segnalazione all'autorità competente | ⬜ Sì ⬜ No ⬜ N/A | | |
| Capacità di notifica iniziale (entro ore) | ⬜ Sì ⬜ No | | |
| Test del processo di segnalazione degli incidenti | ⬜ Sì ⬜ No | | |

## Test di resilienza operativa digitale (Capitolo IV)

| Requisito | Stato | Ubicazione evidence | Note |
|-----------|-------|---------------------|------|
| Programma di test annuale stabilito | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Valutazioni della vulnerabilità condotte regolarmente | ⬜ Sì ⬜ No | | |
| Test BCP/DR basati su scenari | ⬜ Sì ⬜ No | | |
| TLPT condotto (se designato) | ⬜ Sì ⬜ No ⬜ N/A ⬜ In attesa | | |
| Risultati dei test documentati e rimediati | ⬜ Sì ⬜ No ⬜ Parziale | | |

## Gestione del rischio TIC di terze parti (Capitolo V)

| Requisito | Stato | Ubicazione evidence | Note |
|-----------|-------|---------------------|------|
| Quadro di gestione del rischio di terze parti | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Registro dei fornitori di servizi TIC | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Processo di due diligence pre-contrattuale | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Contratti conformi a DORA per fornitori critici | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Strategie di uscita per servizi TIC critici | ⬜ Sì ⬜ No ⬜ Parziale | | |
| Valutazione del rischio di concentrazione condotta | ⬜ Sì ⬜ No | | |
| Presentazione annuale del registro all'autorità | ⬜ Sì ⬜ No ⬜ N/A | | |

---

# Appendice B: Modello di notifica degli incidenti principali

**Incidente principale relativo alle TIC DORA — Notifica iniziale**

**A**: [Autorità competente nazionale — Punto di contatto unico]
**Da**: [Nome dell'entità finanziaria]
**Contatto**: [Nome del responsabile della risposta agli incidenti, Telefono, Email]
**Data/Ora**: [Formato ISO 8601]
**LEI (Legal Entity Identifier)**: [LEI]
**Tipo di notifica**: ⬜ Iniziale ⬜ Intermedia ⬜ Finale

---

**SEZIONE 1: RIEPILOGO DELL'INCIDENTE**

**ID Incidente**: [Numero di riferimento interno]
**Data/Ora di rilevamento**: [ISO 8601]
**Data/Ora di inizio dell'incidente** (stimata): [ISO 8601]
**Stato attuale**: ⬜ In corso ⬜ Contenuto ⬜ Risolto

**Tipo di incidente**:
⬜ Attacco informatico (specificare: ransomware, DDoS, malware, phishing, ecc.)
⬜ Guasto di sistema (specificare: hardware, software, rete)
⬜ Violazione dei dati / Perdita di dati
⬜ Interruzione del fornitore di servizi di terze parti
⬜ Impatto di catastrofe naturale
⬜ Altro (specificare): _____________

---

**SEZIONE 2: VALUTAZIONE DELL'IMPATTO**

**Funzioni critiche o importanti interessate**: [Funzione 1]: [Descrizione dell'impatto] / [Funzione 2]: [Descrizione dell'impatto]

**Interruzione del servizio**: Durata: [Ore/minuti di interruzione] / Clienti interessati: [Numero e tipo] / Portata geografica: [Paesi interessati]

**Impatto sui dati**: ⬜ Nessun dato interessato / ⬜ Dati potenzialmente compromessi: [Tipo, volume, sensibilità] / ⬜ Dati confermati compromessi: [Dettagli]

**Impatto finanziario** (preliminare): ⬜ Non ancora determinato / ⬜ Stimato: [Importo e base]

---

**SEZIONE 3: CAUSA PRINCIPALE** (preliminare)

[Breve descrizione della causa principale sospettata o confermata]

---

**SEZIONE 4: AZIONI DI RISPOSTA**

**Azioni intraprese**: 1. [Azione 1 - timestamp] / 2. [Azione 2 - timestamp] / 3. [Azione 3 - timestamp]

**Azioni in corso**: [Azione con completamento previsto]

---

**SEZIONE 5: DICHIARAZIONE**

Confermo che le informazioni fornite in questa notifica sono accurate al meglio delle mie conoscenze alla data/ora [Data/Ora].

**Nome**: [Rappresentante della direzione senior] / **Titolo**: [Titolo]

---

**FINE DEL RIFERIMENTO TECNICO**

*Questo riferimento tecnico supporta i potenziali requisiti di conformità DORA come determinato in ISMS-POL-00. Per le organizzazioni NON soggette a DORA, questo documento è esclusivamente a scopo informativo e NON crea obblighi di conformità.*

<!-- QA_VERIFIED: 2026-04-04 -->

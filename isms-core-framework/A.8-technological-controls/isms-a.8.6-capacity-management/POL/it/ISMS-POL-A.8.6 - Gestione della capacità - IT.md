<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.6-IT:framework:POL:a.8.6 -->
**ISMS-POL-A.8.6 — Gestione della capacità**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Politica di gestione della capacità |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.6 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale (allineato con il ciclo di pianificazione della capacità).

**Catena di approvazione**: RSSI → Responsabile Operazioni IT/Infrastrutture → Direttore Finanziario (DF) → DSI.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.6.1–3-UG/TG; ISMS-POL-A.8.16; ISMS-POL-A.8.14; ISMS-POL-A.8.13; ISMS-POL-A.7.11; ISMS-POL-A.5.30; ISO/IEC 27001:2022 Controllo A.8.6.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la gestione della capacità al fine di garantire un'infrastruttura e una capacità applicativa sufficienti, conformemente al Controllo A.8.6 della norma ISO/IEC 27001:2022.

**Allineamento normativo** (per ISMS-POL-00): Livello 1 — ISO/IEC 27001:2022 (Controllo A.8.6). Livello 2 — FINMA Circolare 2023/1, DORA Art. 11, NIS2 Art. 21(2) (dove applicabile).

---

# Perimetro

## Applicabilità

**Risorse infrastrutturali nel perimetro**: Capacità di elaborazione (server, VM, container, istanze cloud); capacità di archiviazione (spazio su disco, archiviazione database, archiviazione di backup); capacità di rete (larghezza di banda, throughput, connessioni); capacità applicativa (utenti concorrenti, tassi di transazione, limiti delle API); capacità cloud (quote dei servizi cloud, limiti); infrastruttura fisica (capacità di alimentazione, raffreddamento, spazio rack per A.7.11). **Copertura**: Sistemi che supportano le operazioni aziendali di produzione (obbligatorio); ambienti di sviluppo, test e QA (raccomandato); siti BC/DR (per A.5.30).

## Allineamento sul controllo ISO/IEC 27001:2022 A.8.6

> *L'utilizzo delle risorse deve essere monitorato e ottimizzato, e le proiezioni dei requisiti futuri di capacità devono essere effettuate per garantire le prestazioni di sistema richieste e per informare le decisioni di investimento.*

---

# Enunciati di politica

## Requisiti di monitoraggio della capacità

[Organizzazione] DEVE implementare il monitoraggio della capacità per tutte le risorse infrastrutturali e applicative con le seguenti caratteristiche:

- **Frequenza di raccolta delle metriche**: Minimo ogni 5 minuti per i sistemi di produzione, ogni 15 minuti per i sistemi non di produzione
- **Completezza dei dati**: ≥99,5% disponibilità delle metriche (escluse le finestre di manutenzione pianificata)
- **Recapito degli avvisi**: Avvisi per superamento delle soglie recapitati entro 5 minuti dalla rilevazione

**Requisiti di conservazione dei dati**: Metriche grezze: minimo 30 giorni per le indagini sugli incidenti; metriche aggregate: minimo 12 mesi per l'analisi delle tendenze; dati storici: minimo 36 mesi per la pianificazione strategica.

## Requisiti di previsione della capacità

[Organizzazione] DEVE sviluppare previsioni della capacità per tutte le risorse infrastrutturali e applicative critiche.

**Orizzonti di previsione**: Breve termine (3-6 mesi — pianificazione tattica); medio termine (6-12 mesi — pianificazione del budget); lungo termine (12-24 mesi — pianificazione strategica).

**Frequenza di aggiornamento**: Mensile (aggiornamenti delle previsioni a breve termine); trimestrale (revisione completa delle previsioni); annuale (previsione strategica allineata al ciclo di budget).

**Obiettivo di accuratezza**: Le previsioni entro ±15% dell'utilizzo effettivo (misurate trimestralmente).

**Eccezioni all'obiettivo di accuratezza**: Nuovi sistemi (primi 6 mesi): ±30% accettabile; carichi di lavoro ad alta variabilità (varianza >50%): ±25% con approvazione del DSI; maturità del programma (primi 12 mesi): ±20% obiettivo, che si abbassa a ±15% in seguito.

**Misurazione dell'accuratezza**: Calcolo trimestrale: (Utilizzo effettivo - Utilizzo previsto) / Utilizzo previsto; analisi delle cause radice obbligatoria per deviazioni >15% (completata entro 10 giorni lavorativi).

## Requisiti di pianificazione della capacità

[Organizzazione] DEVE implementare un processo strutturato di pianificazione della capacità.

**Ciclo di pianificazione**: Revisione mensile (avvisi di capacità, eventi near-miss, previsioni a breve termine); pianificazione trimestrale (pianificazione completa con orizzonte di 12 mesi); budget annuale (pianificazione a lungo termine allineata al ciclo di budget).

**Requisiti di approvazione**: Capacità di routine: Direttore IT/DSI nel budget approvato; capacità principale: approvazione del DF per l'impatto sul budget; capacità di emergenza: approvazione rapida del DSI con notifica esecutiva.

**Obiettivi di headroom della capacità**: Sistemi di produzione: minimo 20% di headroom al picco di utilizzo; sistemi di archiviazione: minimo 3 mesi di headroom al tasso di crescita attuale; larghezza di banda di rete: minimo 30% di headroom durante le ore lavorative.

## Requisiti di reporting della capacità

[Organizzazione] DEVE produrre report regolari sulla capacità:

- **Mensile**: Riepilogo dell'utilizzo, incidenti, punti salienti delle previsioni, azioni
- **Trimestrale**: Previsioni complete, piani di espansione, scorecard della salute
- **Annuale**: Piano strategico della capacità con proiezioni pluriennali

**Requisiti delle prove per i report**: Mensili: Consegnati al Team di Leadership IT, archiviati nella Piattaforma GRC/SharePoint; trimestrali: Presentati al Comitato di Pianificazione della Capacità con verbali della riunione; annuali: Approvati dal DSI, inclusi nella revisione della direzione (ISO 27001 Clausola 9.3).

## Modalità di guasto e risposta

**Guasti all'accuratezza delle previsioni**: Se la deviazione >15%: Il Responsabile Infrastrutture DEVE condurre un'analisi delle cause radice entro 10 giorni lavorativi; se la deviazione >30%: Notifica al DSI obbligatoria con piano di miglioramento del processo.

**Eventi di esaurimento della capacità**: Se la soglia critica della capacità viene superata: Le Operazioni IT DEVONO immediatamente implementare misure di mitigazione; se si verifica l'esaurimento della capacità (impatto sul servizio): Classificare come incidente Priority 1 per ISMS-POL-A.5.24-28.

**Lacune nella copertura del monitoraggio**: Se la copertura di produzione scende sotto il 100%: Il Responsabile Infrastrutture DEVE creare un piano di rimedio entro 5 giorni lavorativi; se il monitoraggio di un sistema critico fallisce: Escalation immediata al DSI + RSSI entro 4 ore.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Direzione generale (AD, Consiglio)** | Responsabilità ultima per una capacità adeguata; approvare i principali investimenti in capacità |
| **DSI** | Responsabilità complessiva per l'efficacia del programma di gestione della capacità; garantire headroom adeguato; bilanciare i requisiti di capacità con i vincoli di budget |
| **RSSI** | Garantire la capacità per i sistemi di sicurezza (SIEM, logging, monitoraggio, EDR); verifica della conformità per i controlli di gestione della capacità |
| **Team di pianificazione della capacità / Responsabile Infrastrutture** | Esecuzione quotidiana del programma; monitoraggio, previsione e analisi delle tendenze; pianificazione e coordinamento dell'espansione della capacità; reporting |
| **Team Operazioni IT** | Monitoraggio quotidiano e risposta agli avvisi; risposta immediata agli incidenti di capacità; dispiegamento delle espansioni approvate |
| **Proprietari delle applicazioni / dei sistemi** | Fornire proiezioni di crescita aziendale; partecipare alla pianificazione della capacità |
| **DF** | Approvare i budget di gestione della capacità (CapEx e OpEx) |

---

# Governance e conformità

**Organi di governance**:

**Comitato di Pianificazione della Capacità** (Operativo): Presidente: Responsabile Infrastrutture; frequenza: Mensile; scopo: Rivedere lo stato della capacità, le previsioni, pianificare le espansioni.

**Team di Leadership IT** (Strategico): Membri: DSI, RSSI, DF, Direttore IT; frequenza: Trimestrale; scopo: Rivedere i report sulla capacità, approvare i budget, decisioni strategiche.

**Verifica della conformità**:

- **Auto-valutazione mensile** (per ISMS-IMP-A.8.6.3): Eseguita dal Responsabile Infrastrutture; presentata al Responsabile Operazioni IT entro 10 giorni lavorativi dalla fine del mese
- **Audit interno trimestrale**: Eseguito dalla funzione di audit interno (indipendente dal team di pianificazione della capacità); campione di 3 sistemi critici
- **Audit esterno annuale**: Eseguito dall'auditor di certificazione ISO 27001

**KPI del programma di gestione della capacità** (riportati trimestralmente):

| Categoria KPI | Metrica | Obiettivo |
|--------------|---------|-----------|
| **Disponibilità** | Incidenti relativi alla capacità per trimestre | <2 |
| **Disponibilità** | Tempo medio di espansione della capacità | <30 giorni dall'approvazione |
| **Accuratezza** | Accuratezza delle previsioni | ±15% |
| **Accuratezza** | Tasso di falsi positivi degli avvisi | <10% |
| **Accuratezza** | Completezza dei dati di monitoraggio | >99% |
| **Efficienza** | Headroom medio tra i sistemi | 15-30% |
| **Efficienza** | Utilizzo medio al picco | 70-85% |
| **Efficienza** | Variazione del budget (effettivo vs. pianificato) | ±10% |

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Gestione della capacità** | Processo per garantire risorse adeguate per soddisfare i requisiti attuali e futuri di prestazioni e disponibilità |
| **Monitoraggio della capacità** | Misurazione continua dell'utilizzo delle risorse per comprenderne il consumo e monitorarne le tendenze |
| **Pianificazione della capacità** | Processo proattivo per determinare i requisiti futuri di capacità e sviluppare piani di espansione |
| **Soglia della capacità** | Livello di utilizzo definito che attiva avvisi o azioni quando viene superato |
| **Previsione della capacità** | Proiezione dei requisiti futuri di capacità basata sulle tendenze e sui piani aziendali |
| **Headroom** | Capacità inutilizzata rimanente disponibile per la crescita o la domanda imprevista |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data da definire] |
| **DSI** | [Nome] | [Data da definire] |
| **DF** | [Nome] | [Data da definire] |
| **Responsabile Operazioni IT** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti di gestione della capacità. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.6.1 (Implementazione del monitoraggio della capacità), ISMS-IMP-A.8.6.2 (Previsione e pianificazione della capacità) e ISMS-IMP-A.8.6.3 (Valutazione della gestione della capacità).*

<!-- QA_VERIFIED: 2026-04-03 -->

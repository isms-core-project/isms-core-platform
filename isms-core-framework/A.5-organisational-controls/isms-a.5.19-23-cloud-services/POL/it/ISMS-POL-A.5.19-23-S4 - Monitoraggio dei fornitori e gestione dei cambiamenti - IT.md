<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S4-IT:framework:POL:a.5.19-23-s4 -->
**ISMS-POL-A.5.19-23-S4 — Monitoraggio dei fornitori e gestione dei cambiamenti**
**Controllo A.5.22: Monitoraggio, revisione e gestione dei cambiamenti dei servizi dei fornitori**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Monitoraggio dei fornitori e gestione dei cambiamenti |
| **Tipo di documento** | Sezione di politica |
| **Identificativo del documento** | ISMS-POL-A.5.19-23-S4 |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.5.19-23; ISMS-POL-A.5.19-23-S1; ISMS-IMP-A.5.19-23.S4-UG/TG; ISMS-REF-A.5.23; ISO/IEC 27001:2022 Controllo A.5.22; ISO/IEC 27036-4

---

# Scopo

La presente sezione definisce i requisiti per il monitoraggio continuo, le revisioni periodiche e la gestione dei cambiamenti dei servizi dei fornitori. Garantisce che la postura di sicurezza dei fornitori sia continuamente validata e che i cambiamenti non introducano rischi inaccettabili.

**Principio fondamentale**: Un fornitore che ha soddisfatto la due diligence iniziale non è garantito che rimanga sicuro nel tempo. Le certificazioni scadono, le pratiche di sicurezza si deteriorano, le strutture di proprietà cambiano e si verificano incidenti. Il monitoraggio continuo e la rivalutazione periodica non sono controlli opzionali — sono controlli essenziali che rilevano il deterioramento prima che diventi una violazione.

**ISO/IEC 27001:2022 Allegato A.5.22**

> *L'organizzazione dovrebbe monitorare, rivedere, valutare e gestire regolarmente i cambiamenti nelle pratiche di sicurezza delle informazioni dei fornitori e nella consegna dei servizi.*

---

# Perimetro

## Applicabilità per livello di fornitore

| Attività | Livello 1 (Critico) | Livello 2 (Alto) | Livello 3 (Medio) | Livello 4 (Basso) |
|----------|---------------------|------------------|------------------|-------------------|
| Monitoraggio delle performance | Continuo (automatizzato) | Report mensili | Trimestrale | Annuale |
| Valutazione della sicurezza | Annuale completa | Annuale standard | Biennale | Solo iniziale |
| Verifica della conformità | Controllo trimestrale certificazioni | Semestrale | Annuale | Al rinnovo |
| Revisione della relazione | Governance trimestrale | Semestrale | Annuale | Secondo le esigenze |
| Revisione dei cambiamenti | Tutti i cambiamenti pre-approvati | Cambiamenti significativi esaminati | Solo cambiamenti importanti | Condizioni standard |

---

# Cicli di revisione

## Calendario di revisione per livello di fornitore

| Livello fornitore | Revisione della sicurezza | Revisione delle performance | Revisione della relazione |
|------------------|--------------------------|----------------------------|--------------------------|
| **Livello 1 (Critico)** | Annuale completa + monitoraggio continuo | Report SLA mensili | Riunioni di governance trimestrali |
| **Livello 2 (Alto)** | Valutazione annuale standard | Revisione trimestrale delle performance | Bilancio semestrale della relazione |
| **Livello 3 (Medio)** | Questionario di sicurezza biennale | Semestrale | Revisione annuale |
| **Livello 4 (Basso)** | Solo al rinnovo | Sintesi annuale | Solo al rinnovo |

## Trigger di revisione non pianificata

| Trigger | Perimetro della revisione | Tempistica |
|---------|--------------------------|-----------|
| Incidente di sicurezza che coinvolge il fornitore (confermato) | Revisione completa della sicurezza, conformità contrattuale | Entro 48 ore |
| Cambiamento significativo del servizio (architettura, piattaforma, localizzazione) | Valutazione dell'impatto, rivalutazione del rischio | Prima dell'implementazione |
| Cambiamento della proprietà del fornitore (M&A, acquisizione) | Rinnovo della due diligence, revisione contrattuale | Entro 30 giorni |
| Scadenza o perdita della certificazione | Revisione della conformità, valutazione del rischio | Immediatamente |
| Emendamento o addendum contrattuale significativo | Verifica delle clausole di sicurezza, analisi dell'impatto | Prima della firma |
| Cambiamento normativo che incide sugli obblighi del fornitore | Valutazione della conformità, analisi delle lacune | Entro 60 giorni |
| Evento negativo o danno alla reputazione (incidente pubblico) | Rivalutazione del rischio, comunicazione con il fornitore | Entro 7 giorni |
| Ripetute violazioni degli SLA (3 consecutive o 6 in 12 mesi) | Revisione delle performance, piano di correzione | Immediatamente |

---

# Monitoraggio delle performance

## Categorie di metriche

| Categoria di metrica | Esempi | Frequenza di monitoraggio | Soglia di allerta |
|---------------------|--------|--------------------------|------------------|
| Disponibilità | Tasso di disponibilità, interruzioni non pianificate | Continuo/Tempo reale | Sotto l'obiettivo SLA |
| Performance | Tempo di risposta, throughput, latenza | Continuo/Tempo reale | Degradazione > 10% |
| Supporto | Tempo di risposta ai ticket, tempo di risoluzione, escalation | Aggregazione settimanale | Violazione degli SLA |
| Capacità | Utilizzo delle risorse, margine di scalabilità | Analisi delle tendenze mensile | Utilizzo > 80% |
| Qualità | Tasso di errore, tasso di successo delle transazioni | Revisione mensile | Sopra la soglia di riferimento |

---

# Valutazione della sicurezza

## Metodi di valutazione

| Metodo | Descrizione | Applicabilità |
|--------|-------------|---------------|
| **Questionario di sicurezza** | Valutazione standardizzata (200-300 domande per N1) | Tutti i fornitori con accesso a dati o sistemi |
| **Revisione delle prove** | Esame di politiche, procedure, configurazioni, registri | Livelli 1 e 2 |
| **Revisione delle certificazioni** | Verifica della validità ISO 27001, SOC 2, ecc. | Livelli 1, 2, 3 (ove applicabile) |
| **Revisione dei report di audit** | Esame dettagliato dei risultati SOC 2 Tipo II | Livelli 1 e 2 (obbligatorio) |
| **Revisione dei test di penetrazione** | Esame dei risultati dei test di penetrazione esterni del fornitore | Livello 1 (obbligatorio annualmente) |
| **Valutazione in loco** | Visita fisica e ispezione delle strutture/controlli | Livello 1 (basata sul rischio, ogni 2-3 anni) |

## Gestione dei risultati della valutazione

| Gravità del risultato | Descrizione | Tempistica di correzione | Percorso di escalation |
|---------------------|-------------|--------------------------|----------------------|
| **Critica** | Rischio di violazione dei dati, controlli critici mancanti | Piano di correzione immediato, correzione entro 7 giorni | RSSI + Proprietario aziendale + Direzione generale |
| **Alta** | Lacune significative nei controlli, violazioni SLA | Correzione entro 30 giorni con aggiornamenti settimanali | RSI + Proprietario aziendale + notifica RSSI |
| **Media** | Miglioramenti dei controlli necessari, lacune documentali | Correzione entro 90 giorni con aggiornamenti mensili | RSI + Proprietario aziendale |
| **Bassa** | Raccomandazioni di best practice | Prossimo ciclo di revisione o 6 mesi | Monitoraggio nel dossier di valutazione |

---

# Monitoraggio della conformità

## Monitoraggio delle certificazioni

| Attività | Frequenza | Azione in caso di scadenza o fallimento |
|----------|-----------|----------------------------------------|
| Verifica validità ISO 27001 | Trimestrale | Richiedere prove di rinnovo entro 30 giorni, escalation al RSSI se scaduta > 60 giorni |
| Attualità SOC 2 Tipo II | Richiesta annuale (30 giorni prima dell'anniversario) | Richiedere un nuovo report, effettuare una valutazione del rischio in caso di ritardo |
| Certifications cloud (ISO 27017/27018, CSA STAR) | Annuale | Verificare il rinnovo, valutare l'impatto in caso di abbandono |

## Risposta alle carenze di conformità

| Scenario | Azione immediata | Tempistica | Escalation |
|----------|-----------------|-----------|-----------|
| Certificazione recentemente scaduta | Periodo di regolarizzazione di 30 giorni, valutazione del rischio, misure compensative | Il fornitore deve rinnovare entro 30 giorni | Proprietario aziendale + RSI |
| Certificazione ritirata o revocata | Valutazione immediata del rischio, possibile sospensione del servizio in attesa del rinnovo | 14 giorni per risolvere o avviare la sostituzione | RSSI + Proprietario aziendale |
| Audit fallito (risultati significativi non risolti) | Esaminare i risultati, richiedere un piano di correzione | Piano entro 30 giorni, esecuzione entro 90 giorni | RSI + Proprietario aziendale |
| Non conformità ripetuta (3 o più incidenti) | Piano formale di miglioramento delle performance o avvio della procedura di risoluzione | 60 giorni di miglioramento o pianificazione della transizione | RSSI + Direzione generale |

---

# Gestione dei cambiamenti

## Categorie di cambiamenti

| Tipo di cambiamento | Descrizione | Notifica richiesta | Approvazione richiesta |
|--------------------|-------------|-------------------|----------------------|
| **Cambiamenti del servizio** | Funzionalità, API, interfacce | Preavviso (30 giorni N1, 14 giorni N2) | Cambiamenti significativi (N1) |
| **Cambiamenti dell'infrastruttura** | Migrazione di piattaforma, trasferimento data center | Approvazione previa (N1), preavviso (N2) | N1: Sì, N2: se cambia la localizzazione dei dati |
| **Cambiamenti della sicurezza** | Controlli di sicurezza, metodi di cifratura, meccanismi di accesso | Preavviso (N1-N2) | Cambiamenti significativi (N1) |
| **Cambiamenti del personale** | Contatti chiave, responsabili dell'account, personale di sicurezza | Notifica rapida (entro 14 giorni) | No |
| **Cambiamenti della proprietà** | Acquisizione, fusione, cessione, cambio di controllo | Notifica immediata (entro 48 ore) | N1: Sì, N2: Notifica + revisione del rischio |
| **Cambiamenti dei sub-responsabili** | Nuovi sub-responsabili o modifiche con accesso ai dati | Approvazione previa (N1), preavviso (N2) | N1: Sì, N2: se accesso ai dati |
| **Cambiamenti contrattuali** | Condizioni, tariffe, SLA, condizioni di trattamento dei dati | Secondo il processo di addendum contrattuale | Secondo il contratto (generalmente sì) |
| **Cambiamenti normativi/conformità** | Perdita di certificazione, sanzioni normative | Notifica immediata | Valutazione del rischio richiesta |

## Definizione di cambiamento significativo

Un cambiamento è considerato **significativo** se soddisfa uno dei seguenti criteri:

**Relativo alla sicurezza**: Incide sui controlli di sicurezza che proteggono i dati di [Organizzazione]; modifica i metodi di cifratura, la gestione delle chiavi o i meccanismi di autenticazione; introduce nuove superfici di attacco.

**Relativo ai dati**: Modifica la localizzazione o la giurisdizione del trattamento dei dati (in particolare dall'UE/CH verso paesi senza garanzie adeguate); modifica i processi di trattamento dei dati; incide sull'esercizio dei diritti degli interessati.

**Relativo alla conformità**: Incide sulla conformità ai requisiti normativi (DORA, NIS2, RGPD); introduce nuovi sub-responsabili con accesso ai dati di [Organizzazione]; modifica l'ambito di certificazione.

**Relativo al business**: Modifica la proprietà o il controllo dell'entità fornitore; incide sulla capacità del fornitore di adempiere agli obblighi contrattuali.

---

# Governance delle relazioni

## Struttura di governance per livello di fornitore

| Livello fornitore | Modello di governance | Frequenza delle riunioni |
|------------------|----------------------|--------------------------|
| **Livello 1 (Critico)** | Comitato di governance formale con statuto documentato | Trimestrale |
| **Livello 2 (Alto)** | Bilanci aziendali regolari con volet sicurezza | Semestrale |
| **Livello 3 (Medio)** | Punti regolari secondo le esigenze | Annuale |
| **Livello 4 (Basso)** | Relazione transazionale | Secondo le esigenze |

**Ordine del giorno tipo — Riunione di governance trimestrale (Livello 1)**: Bilancio delle performance; conformità SLA e qualità del servizio; aggiornamento della postura di sicurezza; revisione degli incidenti; richieste di cambiamento e roadmap; stato della conformità (certificazioni, audit); problemi, rischi ed escalation; revisione delle azioni.

---

# Revisione degli incidenti

## Processo di revisione degli incidenti

| Fase | Attività | Tempistica | Responsabile |
|------|----------|-----------|-------------|
| **1. Notifica** | Ricevere la notifica dell'incidente dal fornitore | Secondo lo SLA (4-48 ore) | Fornitore → RSI |
| **2. Registrazione** | Registrare l'incidente nel registro degli incidenti dei fornitori | Entro 4 ore | RSI |
| **3. Valutazione dell'impatto** | Valutare l'impatto su [Organizzazione] (dati, sistemi, conformità, attività) | Entro 24 ore | RSI + Proprietario aziendale |
| **4. Verifica del contenimento** | Verificare che il fornitore abbia contenuto l'incidente | Entro 48 ore | RSI |
| **5. Analisi delle cause profonde** | Richiedere e rivedere l'ACR del fornitore | Entro 30 giorni | Fornitore fornisce, RSI esamina |
| **6. Revisione della correzione** | Esaminare le misure correttive e preventive | Entro 60 giorni | RSI |
| **7. Rivalutazione del rischio** | Aggiornare la valutazione del rischio se l'incidente rivela debolezze nei controlli | Entro 30 giorni dalla chiusura | RSI |

---

# Documentazione e reporting

## Reporting alla direzione

| Report | Frequenza | Destinatari | Contenuto |
|--------|-----------|-------------|-----------|
| **Sintesi dei rischi dei fornitori** | Trimestrale | RSSI, DSI, Direzione | Panoramica dei rischi, fornitori ad alto rischio, tendenze |
| **Stato dei fornitori critici** | Mensile | RSI, Proprietari aziendali | Performance N1, problemi, cambiamenti |
| **Sintesi degli incidenti** | Trimestrale | RSSI, Conformità | Incidenti di sicurezza, impatto, stato delle correzioni |
| **Stato della conformità** | Trimestrale | RSI, Conformità | Validità delle certificazioni, risultati di conformità |
| **Revisione annuale dei fornitori** | Annuale | Direzione generale | Revisione completa del portafoglio fornitori |

---

*«Monitorare senza agire è osservazione costosa. Agire senza monitorare è fiducia cieca.»*

<!-- QA_VERIFIED: 2026-04-03 -->

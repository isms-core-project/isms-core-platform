<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.31-IT:framework:POL:a.8.31 -->
**ISMS-POL-A.8.31 — Separazione degli ambienti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Separazione degli ambienti di sviluppo, test e produzione |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.31 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → Operazioni IT → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.31-UG/TG; ISMS-REF-A.8.31 (Pattern di architettura degli ambienti); ISMS-REF-A.8.31 (Integrazione pipeline CI/CD); ISO/IEC 27001:2022 Controllo A.8.31.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la separazione degli ambienti di sviluppo, test e produzione per ridurre i rischi associati a modifiche non autorizzate ed esposizione dei dati, conformemente al Controllo A.8.31 della norma ISO/IEC 27001:2022.

**Principi fondamentali**: Gli ambienti di produzione DEVONO essere protetti dalle attività di sviluppo e test; i dati di produzione NON DEVONO essere utilizzati negli ambienti di sviluppo o test; le modifiche DEVONO seguire percorsi di promozione definiti prima di raggiungere la produzione; l'accesso degli sviluppatori alla produzione DEVE essere limitato alle sole situazioni di emergenza.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.31

> *Gli ambienti di sviluppo, test e produzione devono essere separati e protetti.*

**Obiettivo del controllo**: Garantire che gli ambienti di sviluppo, test e produzione siano separati in modo sicuro per prevenire modifiche non autorizzate, esposizione dei dati e interruzioni del servizio.

---

# Definizioni degli ambienti

| Ambiente | Descrizione | Uso previsto |
|---------|-------------|--------------|
| **Sviluppo** | Sviluppo attivo del codice e sperimentazione | Sviluppatori — libero accesso |
| **Test/QA** | Garanzia della qualità, test di integrazione, UAT | Sviluppatori e tester con accesso controllato |
| **Staging/Pre-produzione** | Validazione finale prima della produzione | Team IT/Operazioni — accesso limitato agli sviluppatori |
| **Produzione** | Sistemi operativi in tempo reale che servono gli utenti finali | Solo IT/Operazioni — accesso degli sviluppatori solo in emergenza |
| **Disaster Recovery** | Sistemi di backup della produzione | Solo IT/Operazioni |

---

# Enunciati di politica

## Separazione tecnica degli ambienti

[Organizzazione] DEVE implementare la separazione tecnica tra tutti gli ambienti.

**Metodi di separazione richiesti** (in ordine di preferenza): Ambienti cloud separati (account/tenant distinti); reti separate con segmentazione di rete (VLAN, VPC distinti); separazione logica con controlli di accesso rigorosi (solo se i metodi fisici/cloud non sono fattibili, con approvazione del RSSI).

**Separazione minima obbligatoria**: La produzione DEVE essere sempre separata dai sistemi non di produzione; la staging/pre-produzione DEVE essere separata dallo sviluppo/test; i database di produzione NON DEVONO essere condivisi con ambienti non di produzione.

## Controllo degli accessi per ambiente

**Accesso alla produzione**: L'accesso regolare alla produzione DEVE essere limitato al personale IT/Operativo autorizzato; l'accesso degli sviluppatori alla produzione DEVE essere: solo in emergenza, soggetto ad AMF, registrato e monitorato, con approvazione da parte del lead delle operazioni, e revisionato entro 24 ore dall'utilizzo. **I developer NON DEVONO avere accesso admin alla produzione come corso ordinario delle operazioni.**

**Accesso alla staging**: Limitato al personale IT/Operativo e ai tester approvati; accesso degli sviluppatori consentito per la risoluzione dei problemi, non per lo sviluppo attivo.

**Accesso allo sviluppo/test**: I team di sviluppo hanno accesso completo; l'accesso di terze parti (appaltatori, fornitori) limitato per perimetro e durata.

## Promozione del codice tra gli ambienti

[Organizzazione] DEVE implementare un percorso di promozione del codice controllato.

**Flusso obbligatorio di promozione**: Sviluppo → Test/QA → Staging → Produzione (sequenziale; il salto di ambienti richiede la giustificazione documentata e l'approvazione del RSSI).

**Requisiti di promozione**: Ogni promozione a un ambiente superiore DEVE richiedere: completamento dei test nell'ambiente corrente; approvazione del responsabile tecnico (staging → produzione richiede l'approvazione dell'IT Manager); modifica registrata nel sistema di gestione dei cambiamenti (ISMS-POL-A.8.32); piano di rollback documentato per la promozione in produzione.

**Dispiegamenti in produzione**: DEVONO seguire il processo di gestione dei cambiamenti (ISMS-POL-A.8.32); i cambiamenti di produzione non pianificati richiedono l'approvazione di emergenza; tutti i dispiegamenti in produzione DEVONO essere registrati.

## Protezione dei dati tra gli ambienti

**Regola fondamentale**: I dati di produzione NON DEVONO essere utilizzati negli ambienti di sviluppo o test senza mascheramento. (per ISMS-POL-A.8.11)

**Dati di test**: Gli ambienti non di produzione DEVONO usare: dati sintetici generati artificialmente; dati di produzione mascherati/anonimizzati (approvazione del RSSI e RPD richiesta); subset di dati di produzione mascherati se i dati sintetici non sono fattibili.

**Dati di configurazione**: I file di configurazione con credenziali di produzione NON DEVONO essere condivisi con gli ambienti non di produzione; ogni ambiente DEVE avere credenziali distinte per tutti i servizi.

## Integrazione CI/CD

Le pipeline CI/CD DEVONO rispettare i confini di separazione degli ambienti.

**Requisiti**: Pipeline separate per ogni ambiente (sviluppo, test, staging, produzione); le pipeline di produzione DEVONO richiedere approvazione manuale prima del dispiegamento; i segreti specifici dell'ambiente DEVONO essere gestiti separatamente (secrets manager per ambiente); le pipeline NON DEVONO avere accesso diretto ai sistemi di produzione senza attraversare la gestione dei cambiamenti.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approva le eccezioni alla separazione |
| **DSI** | Supervisione della strategia di separazione degli ambienti |
| **Operazioni IT** | Implementazione e manutenzione della separazione degli ambienti |
| **Team di sviluppo** | Conformità ai requisiti di separazione; non accedere alla produzione al di fuori delle procedure di emergenza |
| **Proprietari dei sistemi** | Approvazione dei dispiegamenti in produzione per i sistemi di proprietà |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per la separazione degli ambienti. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.31 (UG/TG). I riferimenti tecnici sono in ISMS-REF-A.8.31.*

<!-- QA_VERIFIED: 2026-04-03 -->

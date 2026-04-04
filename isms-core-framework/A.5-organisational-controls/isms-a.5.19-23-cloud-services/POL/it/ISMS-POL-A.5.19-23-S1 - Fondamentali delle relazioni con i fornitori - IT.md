<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S1-IT:framework:POL:a.5.19-23-s1 -->
**ISMS-POL-A.5.19-23-S1 — Fondamentali delle relazioni con i fornitori**
**Controllo A.5.19: Sicurezza delle informazioni nelle relazioni con i fornitori**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Fondamentali delle relazioni con i fornitori |
| **Tipo di documento** | Sezione di politica |
| **Identificativo del documento** | ISMS-POL-A.5.19-23-S1 |
| **Autore del documento** | Responsabile della Sicurezza delle Informazioni (RSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Catena di approvazione**: RSSI → RSI → Responsabile Legale/Conformità → Direttore Acquisti → Direzione generale

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.5.19-23; ISMS-POL-A.5.19-23-S2; ISMS-IMP-A.5.19-23.S1-UG/TG; ISMS-REF-A.5.23; ISO/IEC 27001:2022 Controllo A.5.19; ISO/IEC 27036-1

---

# Scopo

La presente sezione definisce i requisiti fondamentali per la gestione dei rischi di sicurezza delle informazioni nelle relazioni con i fornitori. Stabilisce il quadro di classificazione, la metodologia di valutazione del rischio e i requisiti di due diligence applicabili a tutti i fornitori esterni.

**Principio critico — "Conoscete i vostri fornitori prima che conoscano i vostri dati"**: Le relazioni con i fornitori devono iniziare con una valutazione sistematica del rischio e una due diligence basata su prove, non con la scoperta post-contrattuale. Concedere l'accesso a un fornitore senza classificazione, consentire l'accesso ai dati senza due diligence, o firmare contratti senza valutazione della sicurezza crea rischi inaccettabili e potenzialmente irrecuperabili. La selezione dei fornitori è una decisione di sicurezza, non solo una decisione di approvvigionamento.

**ISO/IEC 27001:2022 Allegato A.5.19 — Sicurezza delle informazioni nelle relazioni con i fornitori**

> *Devono essere definiti e concordati con i fornitori processi e procedure per gestire i rischi di sicurezza delle informazioni associati all'uso dei prodotti o servizi del fornitore.*

---

# Perimetro

## Tipi di fornitori applicabili

| Tipo di fornitore | Descrizione | Esempi |
|------------------|-------------|--------|
| **Fornitori di servizi cloud** | Fornitori di IaaS, PaaS, SaaS, servizi XDR | Calcolo, storage, email, piattaforme di sicurezza |
| **Fornitori di servizi gestiti** | Operazioni e supporto IT esternalizzati | Helpdesk, gestione della rete, servizi SOC |
| **Fornitori di software** | Fornitori di software in licenza o su abbonamento | ERP, CRM, strumenti di sviluppo |
| **Fornitori di hardware** | Fornitori di apparecchiature IT fisiche | Server, apparecchiature di rete, postazioni di lavoro |
| **Servizi professionali** | Consulenti con accesso ai sistemi/dati | Revisori, integratori, sviluppatori |
| **Fornitori di strutture** | Servizi di data center e hosting | Colocation, sicurezza fisica |
| **Telecomunicazioni** | Fornitori di reti e connettività | Internet, WAN, servizi voce |

## Esclusioni

Questa politica non si applica a: fornitori di beni/servizi senza accesso alle informazioni organizzative; acquisti una tantum senza relazione continuativa; clienti individuali dei servizi di [Organizzazione].

---

# Classificazione dei fornitori

## Criteri di classificazione

I fornitori DEVONO essere classificati in base ai seguenti fattori:

| Fattore | Ponderazione | Domande di valutazione |
|---------|------------|------------------------|
| **Accesso ai dati** | Alta | A quali livelli di classificazione dei dati può accedere il fornitore? |
| **Accesso ai sistemi** | Alta | Il fornitore ha accesso ai sistemi di produzione? |
| **Criticità del servizio** | Alta | Un guasto del fornitore avrebbe un impatto sulle operazioni aziendali? |
| **Sostituibilità** | Media | Con quale facilità può essere sostituito il fornitore? |
| **Profondità di integrazione** | Media | Quanto sono integrati i servizi del fornitore? |
| **Impatto normativo** | Alta | Il fornitore influisce sulla conformità normativa? |

## Livelli di classificazione

### Livello 1: Fornitori critici

**Criteri (uno qualsiasi attiva il Livello 1)**: Accesso a dati Limitati o Riservati; accesso diretto ai sistemi o alle infrastrutture di produzione; punto singolo di guasto per i processi aziendali critici; dipendenza dalla conformità normativa (fornitore critico DORA, servizio essenziale NIS2, responsabile del trattamento RGPD per il trattamento ad alto rischio).

**Requisiti**: Valutazione annuale dettagliata in loco o da remoto; revisioni trimestrali di performance e sicurezza; piano di continuità operativa documentato; clausola di diritto di audit obbligatoria; sponsor esecutivo designato; certificazione SOC 2 Tipo II o ISO/IEC 27001 richiesta; notifica degli incidenti entro 4 ore; divulgazione e approvazione dei sub-responsabili del trattamento.

### Livello 2: Fornitori ad alto rischio

**Criteri**: Accesso a dati classificati come Interni; accesso a sistemi non di produzione (sviluppo, test); funzione aziendale importante ma non critica; più opzioni di fornitura disponibili; responsabile del trattamento RGPD per il trattamento a rischio standard.

**Requisiti**: Valutazione della sicurezza annuale (questionario + prove); revisioni semestrali delle performance; considerazioni sulla continuità operativa documentate; clausola di diritto di audit raccomandata; certificazione SOC 2 o ISO/IEC 27001 richiesta; notifica degli incidenti entro 24 ore; divulgazione dei sub-responsabili.

### Livello 3: Fornitori a rischio medio

**Criteri**: Accesso limitato ai dati (Pubblici o Interni minimi); nessun accesso diretto ai sistemi; funzione aziendale di supporto; facilmente sostituibile; nessun impatto sulla conformità normativa.

**Requisiti**: Valutazione della sicurezza biennale; revisione annuale delle performance; clausole di sicurezza contrattuali standard; certificazione preferibile se si gestiscono dati organizzativi; notifica degli incidenti entro 72 ore.

### Livello 4: Fornitori a basso rischio

**Criteri**: Nessun accesso ai dati organizzativi; nessun accesso ai sistemi; servizi generici; più alternative disponibili; nessun impatto normativo.

**Requisiti**: Solo due diligence iniziale; condizioni generali standard; revisione al rinnovo contrattuale.

## Matrice di classificazione

```
                      │ Nessun    │ Accesso non│ Accesso    │
                      │ accesso   │ produzione │ produzione │
──────────────────────┼───────────┼────────────┼────────────┤
Dati Limitati         │ Livello 2 │ Livello 1  │ Livello 1  │
Dati Riservati        │ Livello 2 │ Livello 1  │ Livello 1  │
Dati Interni          │ Livello 3 │ Livello 2  │ Livello 2  │
Solo dati Pubblici    │ Livello 4 │ Livello 3  │ Livello 3  │
Nessun accesso ai dati│ Livello 4 │ Livello 4  │ Livello 3  │
```

**Rivalutazione della classificazione**: La classificazione dei fornitori DEVE essere rivalutata annualmente; in caso di cambiamento significativo dell'ambito del servizio; in caso di fusione/acquisizione del fornitore; dopo un incidente di sicurezza significativo; in caso di cambiamenti dell'ambito normativo.

---

# Valutazione del rischio dei fornitori

## Categorie di rischio

| Categoria | Descrizione | Assi di valutazione |
|-----------|-------------|---------------------|
| **Rischio di riservatezza** | Divulgazione non autorizzata di informazioni | Gestione dei dati, controlli degli accessi, cifratura |
| **Rischio di integrità** | Modifica non autorizzata di dati/sistemi | Gestione dei cambiamenti, validazione degli input, controlli di qualità |
| **Rischio di disponibilità** | Interruzione del servizio o perdita di dati | Ridondanza, backup, ripristino di emergenza, impegni SLA |
| **Rischio di conformità** | Violazioni normative o contrattuali | Certificazioni, report di audit, attestazioni |
| **Rischio di concentrazione** | Eccessiva dipendenza da un unico fornitore | Alternative di mercato, fattibilità dell'uscita, vendor lock-in |
| **Rischio geopolitico** | Fattori giurisdizionali o politici | Residenza dei dati, quadri giuridici, esposizione al CLOUD Act statunitense |

## Matrice di punteggio del rischio

| Probabilità | Impatto: Basso | Impatto: Medio | Impatto: Alto | Impatto: Critico |
|-------------|----------------|----------------|---------------|------------------|
| **Raro** | 1 | 2 | 3 | 4 |
| **Improbabile** | 2 | 4 | 6 | 8 |
| **Possibile** | 3 | 6 | 9 | 12 |
| **Probabile** | 4 | 8 | 12 | 16 |
| **Quasi certo** | 5 | 10 | 15 | 20 |

**Soglie di valutazione del rischio**: 1-4: Basso → controlli standard, revisione annuale; 5-9: Medio → controlli rafforzati, revisione semestrale; 10-15: Alto → controlli significativi + approvazione RSSI + revisione trimestrale; 16-20: Critico → approvazione Direzione generale + monitoraggio continuo + piano di mitigazione obbligatorio.

**Rischio inaccettabile**: Punteggi di rischio 16-20 senza mitigazione fattibile devono comportare il rifiuto del fornitore o la risoluzione della relazione.

---

# Requisiti di due diligence

## Due diligence per livello di classificazione

| Requisito | Livello 1 | Livello 2 | Livello 3 | Livello 4 |
|-----------|-----------|-----------|-----------|-----------|
| Questionario sulla sicurezza | ✓ Dettagliato | ✓ Standard | ✓ Base | — |
| Verifica delle certificazioni | ✓ Richiesta | ✓ Richiesta | ✓ Se dichiarate | — |
| Revisione dei documenti di politica | ✓ Richiesta | ✓ Richiesta | — | — |
| Valutazione tecnica | ✓ Richiesta | ✓ Basata sul rischio | — | — |
| Verifica della stabilità finanziaria | ✓ Richiesta | ✓ Raccomandata | — | — |
| Verifica delle referenze | ✓ Richiesta | ✓ Raccomandata | — | — |
| Valutazione in loco | ✓ Basata sul rischio | — | — | — |
| Revisione del test di penetrazione | ✓ Richiesta | ✓ Se disponibile | — | — |
| Valutazione dei sub-responsabili | ✓ Richiesta | ✓ Se applicabile | — | — |
| Accordo di trattamento dei dati | ✓ Richiesto | ✓ Richiesto | ✓ Se accesso ai dati | — |
| Revisione della continuità operativa | ✓ Richiesta | ✓ Richiesta | ✓ Se critico | — |

## Certificazioni di sicurezza

**Certificazioni preferite** (in ordine di preferenza): ISO/IEC 27001 (3 anni, con sorveglianza annuale); SOC 2 Tipo II (12 mesi); SOC 2 Tipo I (istantanea); ISO/IEC 27017 (sicurezza cloud); ISO/IEC 27018 (privacy cloud); CSA STAR.

**Requisiti di certificazione per livello**: Livello 1: ISO/IEC 27001 o SOC 2 Tipo II richiesti (validi entro 12 mesi); Livello 2: ISO/IEC 27001 o SOC 2 (Tipo I accettabile) richiesti; Livello 3: certificazione preferibile ma non obbligatoria; Livello 4: nessun requisito.

**Attestazioni alternative**: In assenza di certificazioni ISO/SOC, [Organizzazione] può accettare: certificazioni governative (FedRAMP, C5 in Germania); certificazioni settoriali (PCI DSS v4.0.1, HITRUST); report di audit di sicurezza dettagliati di terzi (richiede approvazione RSSI).

---

# Requisiti di sicurezza delle informazioni

## Requisiti di base (Tutti i fornitori con accesso ai dati)

| Requisito | Descrizione |
|-----------|-------------|
| **Controllo degli accessi** | Principio del minimo privilegio, account individuali, accesso basato sui ruoli, registrazione degli accessi |
| **Autenticazione** | Autenticazione forte (password complesse o certificati), AMF per gli accessi privilegiati |
| **Cifratura in transito** | Dati cifrati durante la trasmissione con TLS 1.2+ o equivalente |
| **Segnalazione degli incidenti** | Incidenti di sicurezza segnalati a [Organizzazione] entro 24 ore dalla presa di conoscenza |
| **Sicurezza del personale** | Verifiche dei precedenti appropriate al livello di accesso per il personale con accesso ai dati di [Organizzazione] |
| **Riservatezza** | NDA o impegno contrattuale di riservatezza equivalente |
| **Minimizzazione dei dati** | Accesso solo ai dati necessari per la fornitura del servizio |
| **Residenza dei dati** | Trattamento dei dati nelle giurisdizioni approvate ai sensi del contratto |

## Requisiti rafforzati (Fornitori di Livelli 1 e 2)

| Requisito | Descrizione |
|-----------|-------------|
| **Cifratura a riposo** | Dati cifrati a riposo con algoritmi robusti (AES-256 o equivalente) |
| **Gestione delle vulnerabilità** | Scansioni regolari delle vulnerabilità, applicazione di patch nei tempi previsti (critiche entro 30 giorni, alte entro 60 giorni) |
| **Monitoraggio della sicurezza** | Registrazione, avvisi, integrazione SIEM ove applicabile |
| **Continuità operativa** | Piani BCP/DRP documentati e test annuali con prove fornite |
| **Diritti di audit** | [Organizzazione] può effettuare audit o esaminare i report di audit di terzi |
| **Controlli sui sub-responsabili** | I requisiti di sicurezza si estendono ai sub-responsabili; divulgazione richiesta |
| **Gestione dei cambiamenti** | Controllo formale dei cambiamenti con notifica a [Organizzazione] per i cambiamenti significativi |
| **Segregazione dei dati** | Segregazione logica o fisica dagli altri clienti (controlli multi-tenant) |

---

# Registro dei fornitori

## Requisiti del registro

[Organizzazione] DEVE mantenere un registro completo dei fornitori contenente: nome del fornitore; tipo di fornitore; livello di classificazione; servizi forniti; accesso ai dati; accesso ai sistemi; riferimento contrattuale; responsabile aziendale; contatto per la sicurezza; data dell'ultima valutazione; data della prossima revisione; valutazione del rischio; certificazioni; perimetro normativo; complessità dell'uscita.

**Manutenzione del registro**: Aggiornato all'integrazione di un nuovo fornitore (entro 5 giorni lavorativi); aggiornato in caso di cambiamenti contrattuali (entro 10 giorni lavorativi); revisione trimestrale dell'accuratezza da parte del RSI; audit annuale della completezza.

---

# Prevenzione dell'IT ombra

**IT ombra (Shadow IT)**: Utilizzo di fornitori, servizi cloud o software non autorizzati senza approvazione IT e Sicurezza. L'IT ombra aggira i controlli di sicurezza, la due diligence e le protezioni contrattuali, creando rischi non gestiti e spesso non rilevabili.

**Misure di prevenzione**: Catalogo dei servizi approvati; integrazione con gli acquisti (approvazione IT/Sicurezza nel flusso di lavoro); monitoraggio del traffico di rete per i servizi cloud non approvati; controlli degli endpoint; sensibilizzazione degli utenti; canale di segnalazione per i nuovi servizi.

**Risposta alla scoperta di IT ombra**: (1) Identificare il servizio e gli utenti; (2) Valutare il rischio; (3) Decisione: approvare retroattivamente, migrare ad alternativa approvata, o risolvere; (4) Se approvato: eseguire l'integrazione accelerata; (5) Se risolto: comunicare agli utenti, bloccare l'accesso, migrare i dati se necessario; (6) Analisi delle cause profonde.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Responsabile aziendale** | Identificare il bisogno del fornitore; mantenere la relazione; approvazione del budget |
| **Acquisti** | Coordinamento del processo di selezione; negoziazione e gestione del contratto |
| **Responsabile della Sicurezza delle Informazioni** | Valutazione del rischio; definizione dei requisiti di sicurezza; manutenzione del registro |
| **Legale/Conformità** | Revisione dei contratti; verifica della conformità normativa; revisione degli accordi di trattamento dei dati |
| **Operazioni IT** | Attuazione tecnica; provisioning degli accessi; supporto all'integrazione |
| **RSSI** | Approvazione della politica; approvazione dei fornitori ad alto rischio; approvazione delle eccezioni |
| **RPD** | Verifica della conformità RGPD; approvazione degli accordi di trattamento dei dati |

---

*«La solidità della vostra sicurezza è forte quanto il vostro anello più debole nella catena dei fornitori.»*

<!-- QA_VERIFIED: 2026-04-03 -->

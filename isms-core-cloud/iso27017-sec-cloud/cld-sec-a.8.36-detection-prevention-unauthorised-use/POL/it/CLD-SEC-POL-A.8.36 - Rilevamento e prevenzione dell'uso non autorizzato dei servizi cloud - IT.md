<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.8.36-IT:sec:POL:a.8.36 -->
**CLD-SEC-POL-A.8.36 — Rilevamento e prevenzione dell'uso non autorizzato dei servizi cloud**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Rilevamento e prevenzione dell'uso non autorizzato dei servizi cloud |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-SEC-POL-A.8.36 |
| **Autore del documento** | RSSI / Responsabile Sicurezza Cloud |
| **Proprietario del documento** | RSSI |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Data da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Cloud** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI | Politica iniziale per l'implementazione di ISO/IEC 27017:2026 Ed. 2 |

**Ciclo di revisione** : Annuale (o in caso di cambiamenti significativi alla capacità di monitoraggio dell'uso del cloud, o a seguito di un incidente confermato di uso non autorizzato)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :

- Principale: RSSI
- Secondaria: Responsabile Sicurezza Cloud
- Tecnica: Responsabile delle Operazioni di Sicurezza
- Autorità finale: Direzione generale

**Documenti correlati** :

- ISMS-POL-A.8.16 (Attività di monitoraggio — politica SGSI principale)
- CLD-SEC-POL-A.5.38 (Ruoli e responsabilità condivisi in un ambiente di cloud computing)
- CLD-SEC-POL-A.8.35 (Separazione negli ambienti di elaborazione virtuale)
- CLD-SEC-IMP-A.8.36-TG (Rilevamento e prevenzione dell'uso non autorizzato dei servizi cloud — Guida tecnica, contiene gli schemi completi di monitoraggio)
- CLD-SEC-REF-A.5-A.8 (Addendum di guidance sulla sicurezza cloud)
- ISO/IEC 27017:2026, Clausola 8.36 (CLD — Rilevamento e prevenzione dell'uso non autorizzato dei servizi cloud)
- ISO/IEC 19086 (tutte le parti) (Cloud computing — Quadro degli accordi sul livello di servizio)

---

## Riepilogo esecutivo

Questa politica stabilisce come [Organizzazione] monitora l'attività degli utenti di servizi cloud (CSU) per rilevare e prevenire accessi non autorizzati, trasferimenti di dati non voluti e altre attività non autorizzate sui servizi cloud, in conformità con ISO/IEC 27017:2026, Clausola 8.36.

**Perimetro** : Tutti i servizi cloud che [Organizzazione] gestisce in qualità di cliente di servizio cloud (CSC), incluso il monitoraggio dei propri utenti di servizi cloud; e tutti i servizi cloud che [Organizzazione] eroga in qualità di fornitore di servizio cloud (CSP), inclusi gli orientamenti e le funzioni di monitoraggio forniti ai CSC.

**Nota sui controlli estesi** : ISO/IEC 27017:2026, Clausola 8.36 è uno dei quattro controlli estesi specifici per il cloud «CLD» introdotti dalla seconda edizione dello standard (insieme a 5.38, 5.39 e 8.35). È interamente nuovo — non ha equivalenti nella prima edizione del 2015 di ISO/IEC 27017 né un equivalente diretto in ISO/IEC 27002:2022. [Organizzazione] lo implementa come estensione informativa del proprio SGSI basato su ISO/IEC 27001:2022, insieme al controllo 8.16 dell'Annex A (Attività di monitoraggio).

**Rischio fondamentale** : I servizi cloud sono facili da attivare e altrettanto facili da utilizzare in modo improprio — un singolo CSU può creare infrastrutture ombra, esfiltrare dati tramite un servizio autorizzato in modo non autorizzato, o eccedere l'accesso previsto senza attivare i controlli perimetrali di rete convenzionali. Il rilevamento dipende dal monitoraggio dei modelli di utilizzo, non solo dal monitoraggio per attacchi esterni. Un'istanza confermata di uso non autorizzato di un servizio cloud è trattata come un incidente di sicurezza delle informazioni, sottoposta a escalation e indagata secondo il processo di gestione degli incidenti di [Organizzazione] — non semplicemente registrata e chiusa.

---

# Perimetro e applicabilità

## ISO/IEC 27017:2026 — Clausola 8.36

**Dichiarazione del controllo (ISO/IEC 27017:2026, 8.36):**
> «L'uso dei servizi cloud da parte dei CSU dovrebbe essere monitorato per prevenire accessi non autorizzati, trasferimenti di dati e altre attività non autorizzate sui servizi cloud.»

**Finalità (ISO/IEC 27017:2026, 8.36):**
> «Consentire il monitoraggio e la prevenzione dell'uso non voluto dei servizi cloud e del trasferimento non voluto di dati da e verso i servizi cloud.»

*(Traduzione di lavoro predisposta a partire dal testo originale inglese della norma, a fini di leggibilità; in caso di discrepanza, fa fede il testo inglese ufficiale di ISO/IEC 27017:2026.)*

## Applicabilità

Questa politica si applica a:

- Tutti gli utenti di servizi cloud (CSU) all'interno di [Organizzazione] che accedono a servizi cloud per conto di [Organizzazione], in qualità di CSC
- Tutti i servizi cloud che [Organizzazione] eroga ai propri CSC, in qualità di CSP, per quanto riguarda gli orientamenti e le funzioni di monitoraggio che [Organizzazione] deve fornire
- Tutti i processi di gestione degli eventi di sicurezza delle informazioni che acquisiscono dati sull'utilizzo dei servizi cloud

## Quadro normativo e degli standard

ISO/IEC 27017:2026 è un'estensione informativa di ISO/IEC 27002:2022. La clausola 8.36 non corrisponde ad alcun controllo numerato di ISO/IEC 27002:2022; è nuova nella seconda edizione 2026, senza equivalenti nemmeno nella prima edizione del 2015 di ISO/IEC 27017. È implementata in parallelo al controllo 8.16 dell'Annex A di ISO/IEC 27001:2022 (Attività di monitoraggio), e si basa sulle indicazioni SLA della serie ISO/IEC 19086 laddove i termini dello SLA cloud disciplinano i dati di monitoraggio disponibili per [Organizzazione].

---

# Disposizioni della politica: Rilevamento e prevenzione dell'uso non autorizzato del cloud (8.36)

## Definizione del perimetro basata sul rischio

Prima di implementare il monitoraggio per un dato servizio cloud, [Organizzazione] DEVE:

- Confermare la classificazione dei dati del servizio (Pubblico / Interno / Confidenziale / Riservato), utilizzando la dichiarazione dei requisiti di separazione (CLD-SEC-IMP-A.8.35-TG, Sezione 1) laddove ne esista già una per il servizio
- Applicare il monitoraggio dell'attività dei CSU come base obbligatoria per i servizi cloud classificati come Confidenziali o Riservati
- Per i servizi classificati come Pubblici o Interni, preparare una raccomandazione basata sul rischio (monitorare o meno, e perché) per l'approvazione del RSSI, e registrare la decisione — il monitoraggio non è omesso per impostazione predefinita, bensì costituisce una decisione documentata

## Obblighi in qualità di cliente di servizio cloud (CSC)

Quando [Organizzazione] agisce in qualità di cliente di servizio cloud, [Organizzazione] DEVE, per ogni servizio cloud rientrante nel perimetro:

- Implementare il monitoraggio delle attività dei CSU, acquisendo come minimo gli eventi di autenticazione, il provisioning/deprovisioning delle risorse, l'accesso ai dati e le modifiche di configurazione, instradati verso la capacità centrale di monitoraggio della sicurezza di [Organizzazione] ai sensi di ISMS-POL-A.8.16 ove possibile
- Eseguire una revisione tecnica periodica di conformità rispetto alla politica di sicurezza delle informazioni di [Organizzazione], alla propria politica specifica sull'uso dei servizi cloud, e alle regole e agli standard pertinenti — come minimo annualmente per i servizi Confidenziali o Riservati — con i riscontri di non conformità sottoposti a escalation al Responsabile Sicurezza Cloud per il monitoraggio della remediation
- Monitorare e prevenire il trasferimento di informazioni non voluto o non autorizzato da e verso l'ambiente di servizio cloud gestito da [Organizzazione], utilizzando i controlli tecnici disponibili (ad es. integrazione di data loss prevention, impostazioni di condivisione limitate, monitoraggio del traffico in uscita)
- Stabilire una base di riferimento dell'utilizzo normale del servizio cloud per ciascun servizio monitorato, e rilevare le anomalie — come un aumento dell'utilizzo delle risorse o un utilizzo di servizio sconosciuto — individuando le deviazioni da tale base di riferimento
- Indagare ogni allarme di anomalia attivato e registrarne la classificazione (falso positivo, uso non autorizzato confermato, risolto, sottoposto a escalation alla risposta agli incidenti); trattare ogni riscontro di uso non autorizzato confermato come un incidente di sicurezza delle informazioni

## Obblighi in qualità di fornitore di servizio cloud (CSP)

Quando [Organizzazione] agisce in qualità di fornitore di servizio cloud, [Organizzazione] DEVE:

- Fornire ai CSC orientamenti e funzioni che consentano loro di monitorare e controllare l'uso da parte dei propri CSU del servizio cloud erogato da [Organizzazione] — documentando quali dati di attività sono esposti, come i CSC possono accedervi, e come vengono configurate eventuali funzioni di monitoraggio configurabili (ad es. soglie di allarme personalizzate)
- Mantenere aggiornati tali orientamenti di monitoraggio rivolti ai CSC man mano che il servizio evolve, rivedendoli almeno in occasione della revisione annuale della politica

## Comunicazione e sensibilizzazione

[Organizzazione] DEVE comunicare il perimetro di monitoraggio, le responsabilità dei CSU, le regole di uso accettabile e le modalità di segnalazione di sospetti usi non autorizzati ai CSU interni e ai team pertinenti, tramite il programma di sensibilizzazione alla sicurezza delle informazioni dell'organizzazione (vedere ISMS-POL-A.6.3) e i materiali di onboarding specifici del servizio. Laddove [Organizzazione] agisca in qualità di CSP, le informazioni equivalenti DEVONO essere comunicate ai CSU dei clienti tramite gli orientamenti di monitoraggio pubblicati rivolti ai CSC.

## Registro delle decisioni sul perimetro di monitoraggio — Contenuto minimo

Il registro delle decisioni sul perimetro di monitoraggio (schema completo in CLD-SEC-IMP-A.8.36-TG, Sezione 1) DEVE registrare, per ciascun servizio cloud: l'identificativo del servizio; la sua classificazione dei dati; la decisione di monitoraggio (obbligatorio, basato sul rischio e implementato, o basato sul rischio e non implementato); la motivazione e, ove applicabile, l'approvazione del RSSI; e la data dell'ultima revisione.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|-----------------|
| **RSSI** | È proprietario di CLD-SEC-POL-A.8.36; approva la definizione del perimetro di monitoraggio basata sul rischio per i servizi cloud di classificazione inferiore; esamina le escalation di anomalie con impatto a livello di organizzazione; è responsabile degli incidenti confermati di uso non autorizzato tramite il processo di gestione degli incidenti di [Organizzazione] |
| **Responsabile delle Operazioni di Sicurezza** | Implementa e gestisce il monitoraggio dell'attività dei CSU, la revisione tecnica di conformità e il rilevamento delle anomalie (ruolo CSC); riferisce al RSSI gli indicatori di copertura del monitoraggio e delle anomalie |
| **Responsabile Sicurezza Cloud** | Garantisce che gli orientamenti e le funzioni di monitoraggio rivolti ai CSC siano documentati e resi disponibili laddove [Organizzazione] sia un CSP; registra le decisioni sulla definizione del perimetro basata sul rischio |
| **Erogazione del servizio cloud / Ingegneria** | Configura le capacità di monitoraggio del servizio cloud; risponde ai trasferimenti di informazioni non voluti o non autorizzati rilevati |
| **Tutto il personale (in qualità di CSU)** | Utilizza i servizi cloud esclusivamente nell'ambito del perimetro autorizzato; segnala eventuali sospetti di uso non autorizzato osservati |

---

# Requisiti in materia di prove

| Prova | Descrizione | Responsabile | Conservazione |
|-------|-------------|--------------|---------------|
| Registro delle decisioni sul perimetro di monitoraggio | Decisioni basate sul rischio approvate dal RSSI per i servizi Pubblici/Interni in cui il monitoraggio non è implementato | Responsabile Sicurezza Cloud | In corso + 3 anni |
| Configurazione del monitoraggio dell'attività dei CSU | Documentazione del perimetro e dei meccanismi di monitoraggio per ciascun servizio cloud (ruolo CSC) | Responsabile delle Operazioni di Sicurezza | Versione attuale + versioni precedenti per 3 anni |
| Registrazioni della revisione tecnica di conformità | Registrazioni delle revisioni periodiche rispetto alla politica di sicurezza delle informazioni, alla politica di utilizzo del cloud e agli standard | Responsabile delle Operazioni di Sicurezza | In corso + 3 anni |
| Registro di rilevamento delle anomalie | Registro delle anomalie rilevate (utilizzo inatteso delle risorse, utilizzo di servizio sconosciuto) e della relativa classificazione | Responsabile delle Operazioni di Sicurezza | In corso + 3 anni |
| Registrazioni di uso non autorizzato confermato / incidenti | Registrazioni delle anomalie confermate come uso non autorizzato, correlate al processo di gestione degli incidenti | RSSI | In corso + 3 anni |
| Orientamenti di monitoraggio rivolti ai CSC (ruolo CSP) | Documentazione e funzioni fornite ai CSC per monitorare e controllare l'uso da parte dei propri CSU | Responsabile Sicurezza Cloud | Versione attuale + versioni precedenti per 3 anni |

---

# Monitoraggio e indicatori

Il Responsabile delle Operazioni di Sicurezza riferisce al RSSI, con cadenza almeno trimestrale:

- La proporzione dei servizi cloud Confidenziali/Riservati con monitoraggio attivo dei CSU
- Il numero di anomalie rilevate, con la ripartizione della relativa classificazione (falso positivo / uso non autorizzato confermato / risolto / sottoposto a escalation)
- Il numero di riscontri della revisione tecnica di conformità e il relativo stato di remediation
- Il tempo intercorso tra il rilevamento di un'anomalia e la sua classificazione, per le anomalie confermate come uso non autorizzato

---

# Considerazioni di audit

Gli auditor che verificano la conformità a CLD-SEC-POL-A.8.36 devono aspettarsi di trovare:

- Un perimetro di monitoraggio dell'attività dei CSU documentato per ogni servizio cloud classificato come Confidenziale o Riservato
- Prove della revisione tecnica periodica di conformità rispetto alla politica di sicurezza delle informazioni e alla politica di utilizzo del cloud
- Un registro di rilevamento delle anomalie che dimostri una revisione attiva e il monitoraggio della classificazione, non una mera raccolta passiva di log
- Per i servizi in cui [Organizzazione] è un CSP, orientamenti e funzioni di monitoraggio pubblicati e messi a disposizione dei CSC
- Un'approvazione documentata del RSSI laddove il monitoraggio sia stato ridotto in base al rischio per servizi di classificazione inferiore
- Prove che i riscontri di uso non autorizzato confermato siano stati gestiti tramite il processo di gestione degli incidenti di [Organizzazione], con una registrazione del tempo di classificazione

---

<!-- QA_VERIFIED: 2026-08-01 -->

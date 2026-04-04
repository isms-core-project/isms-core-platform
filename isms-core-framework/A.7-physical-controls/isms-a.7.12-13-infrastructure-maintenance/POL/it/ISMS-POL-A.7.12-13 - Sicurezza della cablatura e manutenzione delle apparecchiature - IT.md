<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.12-13-IT:framework:POL:a.7.12-13 -->
**ISMS-POL-A.7.12-13 — Sicurezza della cablatura e manutenzione delle apparecchiature**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza della cablatura e manutenzione delle apparecchiature |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.7.12-13 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale

**Catena di approvazione**: Principale: RSSI; Secondario: Responsabile Operazioni IT / Responsabile delle strutture; Autorità finale: Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.7.4-5-11; ISMS-POL-A.7.8-9; ISMS-POL-A.8.6; ISMS-IMP-A.7.12-13.S1–S3-UG/TG; ISO/IEC 27001:2022 Controlli A.7.12, A.7.13.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti per la sicurezza della cablatura e la manutenzione delle apparecchiature, garantendo l'integrità dell'infrastruttura e la continuità operativa.

**Approccio a controlli combinati**: I Controlli A.7.12 (Sicurezza della cablatura) e A.7.13 (Manutenzione delle apparecchiature) sono implementati insieme perché affrontano aspetti complementari della protezione dell'infrastruttura, con la cablatura che forma la base per la connettività delle apparecchiature e la manutenzione che garantisce l'affidabilità continua.

---

# Sicurezza della cablatura (A.7.12)

**Controllo ISO/IEC 27001:2022 A.7.12**: I cavi che trasportano alimentazione, dati o che supportano i servizi di informazione devono essere protetti da intercettazione, interferenza o danneggiamento.

## Protezione dei cavi

I cavi che trasportano alimentazione, dati o che supportano i servizi di informazione DEVONO essere protetti:

**Protezione fisica**: I cavi DEVONO essere instradati attraverso percorsi protetti (condotti, canaline, pavimenti sopraelevati); la cablatura sotterranea DEVE essere protetta da danni accidentali (condotti blindati); i cavi DEVONO essere protetti dalle interferenze elettromagnetiche; i percorsi dei cavi DEVONO evitare aree con alto rischio di danneggiamento.

**Controllo degli accessi**: L'infrastruttura di cablatura (pannelli di patch, distribuzioni) DEVE trovarsi in aree sicure; gli armadi di cablatura DEVONO avere controlli di accesso ed essere chiusi a chiave quando non occupati.

## Requisiti di separazione

**Separazione alimentazione e dati**: I cavi di alimentazione DEVONO essere separati dai cavi di comunicazione per prevenire interferenze; la separazione minima e i requisiti di schermatura DEVONO seguire la Base di sicurezza della cablatura di [Organizzazione] definita in ISMS-IMP-A.7.12-13.1.

**Separazione di rete**: I cavi che trasportano diverse classificazioni di sicurezza DEVONO essere fisicamente separati dove fattibile; i cavi di rete ad alta sicurezza DEVONO essere chiaramente identificati (codifica cromatica o etichettatura); i cavi in fibra ottica DEVONO essere utilizzati per trasmissioni ad alta sicurezza dove esiste un rischio di intercettazione.

## Documentazione e gestione della cablatura

**Documentazione**: L'infrastruttura di cablatura DEVE essere documentata (calendari dei cavi, diagrammi) e mantenuta aggiornata. I cavi DEVONO essere etichettati ad entrambe le estremità.

**Controllo dei cambiamenti**: Le modifiche alla cablatura DEVONO seguire il processo di gestione dei cambiamenti (ISMS-POL-A.8.32); i cavi non utilizzati DEVONO essere disconnessi e documentati.

**Sopralluoghi fisici trimestrali**: DEVONO essere condotti per identificare aggiunte o modifiche non autorizzate; i risultati DEVONO essere riconciliati rispetto ai diagrammi as-built e ai ticket di cambio, con risultati documentati e approvati nel classeur di ispezione della cablatura.

---

# Manutenzione delle apparecchiature (A.7.13)

**Controllo ISO/IEC 27001:2022 A.7.13**: Le apparecchiature devono essere mantenute correttamente per garantire la disponibilità, l'integrità e la riservatezza delle informazioni.

## Programma di manutenzione

[Organizzazione] DEVE stabilire e implementare un programma di manutenzione per tutte le apparecchiature:

**Requisiti del programma**: Tutte le apparecchiature nel perimetro registrate nell'inventario degli asset (ISMS-POL-A.5.9) DEVONO essere incluse nel programma di manutenzione; la riconciliazione trimestrale DEVE verificare che tutte le apparecchiature inventariate abbiano copertura della manutenzione; i calendari di manutenzione DEVONO seguire le raccomandazioni del produttore come minimo.

**Calendario di manutenzione preventiva**:

| Tipo di apparecchiatura | Frequenza di manutenzione preventiva |
|------------------------|--------------------------------------|
| Server | Annuale (firmware, pulizia, ispezione) |
| Apparecchiature di rete | Semestrale |
| Sistemi UPS | Controllo trimestrale della batteria, test annuale completo |
| HVAC/Raffreddamento | Trimestrale |
| Soppressione incendi | Per requisiti normativi |
| Sistemi di sicurezza | Semestrale |

## Personale di manutenzione

**Autorizzazione**: Solo il personale autorizzato DEVE eseguire la manutenzione; il personale di manutenzione DEVE essere identificato e verificato; la manutenzione di terze parti DEVE essere contrattata con fornitori approvati.

**Supervisione**: Il personale di manutenzione DEVE essere supervisionato quando accede ad apparecchiature sensibili; l'accesso alla manutenzione non supervisionato DEVE essere registrato e monitorato; la manutenzione remota DEVE essere soggetta a controlli di accesso.

## Sicurezza durante la manutenzione

**Protezione dei dati**: I dati sensibili DEVONO essere protetti durante le attività di manutenzione; le apparecchiature contenenti dati NON DEVONO lasciare i locali per la manutenzione dove evitabile; se è richiesta la manutenzione fuori sede, i dati DEVONO essere cancellati in modo sicuro prima; il personale di manutenzione NON DEVE avere accesso ai dati se non specificamente richiesto.

**Controlli di accesso**: L'accesso alla manutenzione DEVE essere limitato nel tempo; l'accesso DEVE essere registrato (chi, cosa, quando, perché); tutti gli strumenti e le apparecchiature DEVONO essere contabilizzati dopo la manutenzione; l'ispezione fisica DEVE verificare che non ci siano modifiche non autorizzate.

## Manutenzione remota

L'accesso remoto DEVE essere autorizzato e documentato; le sessioni remote DEVONO essere registrate e monitorate; l'accesso remoto DEVE essere disabilitato quando non attivamente richiesto.

## Registrazione della manutenzione

Tutta la manutenzione DEVE essere documentata. I registri DEVONO includere: data, apparecchiatura, lavoro eseguito, personale, risultati. I registri DEVONO essere conservati per il calendario di conservazione (minimo 3 anni) e disponibili per l'audit.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per la cablatura e la manutenzione |
|-------|--------------------------------------------------|
| **Direzione generale** | Approvare la politica, allocare risorse per la manutenzione dell'infrastruttura |
| **RSSI** | Proprietà della politica, standard di sicurezza per la manutenzione |
| **Responsabile Operazioni IT** | Programma di manutenzione delle apparecchiature, gestione dei fornitori |
| **Responsabile delle strutture** | Infrastruttura di cablatura, manutenzione dell'edificio |
| **Proprietari dei sistemi** | Garantire che le apparecchiature di proprietà siano mantenute |
| **Operazioni IT** | Esecuzione quotidiana della manutenzione, documentazione |

---

# Metriche di governance

- Completamento della manutenzione preventiva (obiettivo: 100% nei tempi previsti)
- Guasti delle apparecchiature dovuti a lacune nella manutenzione (obiettivo: 0)
- Accuratezza della documentazione della cablatura (obiettivo: >95%)
- Modifiche non autorizzate della cablatura rilevate (obiettivo: 0)
- Incidenti di sicurezza correlati alla manutenzione (obiettivo: 0)

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Infrastruttura di cablatura** | Tutti i cavi di alimentazione e comunicazione, condotti, percorsi e punti di terminazione |
| **Manutenzione preventiva** | Manutenzione programmata per prevenire guasti alle apparecchiature |
| **Manutenzione correttiva** | Manutenzione eseguita per riparare un guasto |
| **Manutenzione remota** | Manutenzione eseguita tramite accesso remoto senza presenza fisica |
| **Catena di custodia** | Trasferimento documentato della responsabilità delle apparecchiature |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data da definire] |
| **Responsabile Operazioni IT** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la sicurezza della cablatura e la manutenzione delle apparecchiature. Le procedure di attuazione sono documentate in ISMS-IMP-A.7.12-13 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->

<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.30-IT:operational:OP-POL:a.8.30 -->
**ISMS-OP-POL-A.8.30 — Sviluppo in outsourcing**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sviluppo in outsourcing |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.30 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.30 — Sviluppo in outsourcing
- ISO/IEC 27002:2022 Sezione 8.30 — Guida all'implementazione dello sviluppo in outsourcing
- NIST SP 800-53 Rev 5 — SA-4 (Acquisition Process), SA-9 (External System Services)
- OWASP Secure Software Contract Annex
- OWASP Top 10:2025 — A03 Software Supply Chain Failures
- CIS Controls v8 — Salvaguardia 16.4 (Third-Party Software Component Inventory)

**Controlli Allegato A correlati**:

| Controllo | Relazione con lo sviluppo in outsourcing |
|-----------|------------------------------------------|
| A.5.19–23 Sicurezza dei fornitori e dei servizi cloud | Framework di valutazione dei fornitori; piattaforme di sviluppo ospitate nel cloud |
| A.5.31 Requisiti legali, normativi e contrattuali | Obblighi normativi nei contratti di outsourcing |
| A.5.34 Privacy e protezione dei dati personali | Requisiti di protezione dei dati per l'accesso dei fornitori ai dati personali |
| A.8.4 Accesso al codice sorgente | Accesso dei fornitori ai repository dell'organizzazione |
| A.8.25–26–29 Ciclo di vita dello sviluppo sicuro | Requisiti di codifica sicura, testing e SDLC applicati al lavoro in outsourcing |
| A.8.28 Codifica sicura | Standard di codifica estesi agli sviluppatori terzi |
| A.8.31 Separazione degli ambienti | Segregazione degli ambienti per lo sviluppo in outsourcing |
| A.8.32 Gestione delle modifiche | Controllo delle modifiche per la promozione del codice in outsourcing |

**Politiche interne correlate**:

- Politica sul ciclo di vita dello sviluppo sicuro
- Politica di sicurezza dei fornitori e dei servizi cloud
- Politica di accesso al codice sorgente
- Politica di gestione delle modifiche
- Politica di classificazione e gestione delle informazioni
- Politica sulla privacy e protezione dei dati personali

---

# Politica sullo sviluppo in outsourcing

## Scopo

Lo scopo di questa politica è garantire che l'organizzazione indirizzi, monitori e riveda tutte le attività relative allo sviluppo di sistemi e software in outsourcing, in modo che il codice sviluppato esternamente soddisfi i requisiti di sicurezza delle informazioni dell'organizzazione prima dell'accettazione e della distribuzione.

Questa politica supporta la nLPD svizzera (revDSG) Art. 9 stabilendo requisiti contrattuali per i responsabili del trattamento dei dati coinvolti nello sviluppo del software, garantendo che le attività di sviluppo in outsourcing gestiscano i dati personali solo nel modo in cui l'organizzazione stessa è autorizzata a trattarli. I requisiti dell'Art. 8 per le misure tecniche e organizzative si applicano ugualmente ai componenti in outsourcing. Laddove l'organizzazione tratta dati di persone nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 28 (obblighi del responsabile del trattamento) e Art. 32 (sicurezza del trattamento).

## Ambito

Tutte le attività di sviluppo di sistemi e software svolte da parti esterne per conto dell'organizzazione, incluse:

- Sviluppo di software su misura da parte di aziende di sviluppo sotto contratto.
- Team di sviluppo offshore e nearshore.
- Sviluppatori freelance e collaboratori individuali.
- Partnership di sviluppo e accordi di co-sviluppo.
- Personalizzazione ed estensione di software acquisito da terze parti.
- Manutenzione e miglioramento da parte di terze parti di sistemi organizzativi esistenti.

Tutti i dipendenti responsabili dell'approvvigionamento, della gestione o dell'accettazione del lavoro di sviluppo in outsourcing.

**Fuori ambito**: Software commerciale off-the-shelf (COTS) acquistato senza personalizzazione (coperto dalla A.5.19–23); attività di sviluppo interno (coperto dalla A.8.25-26-29); servizi di piattaforma cloud dove non viene sviluppato codice personalizzato; software open source utilizzato come dipendenze (coperto dai requisiti SCA nella Politica sul ciclo di vita dello sviluppo sicuro).

## Principio

L'organizzazione mantiene la responsabilità per la sicurezza del codice in outsourcing indipendentemente da dove o da chi viene sviluppato. Lo sviluppo in outsourcing deve essere soggetto a requisiti di sicurezza, controlli contrattuali e attività di verifica equivalenti — o più rigorosi — di quelli applicati allo sviluppo interno.

Nessun codice in outsourcing deve essere distribuito in produzione senza la validazione indipendente della sicurezza dell'organizzazione e l'accettazione formale.

---

## Valutazione della sicurezza dei fornitori

Prima di coinvolgere un partner di sviluppo esterno, l'organizzazione deve condurre una valutazione della sicurezza per confermare la capacità del fornitore di soddisfare i requisiti di sicurezza delle informazioni.

**Criteri di valutazione pre-coinvolgimento**:

| Area di valutazione | Requisiti minimi |
|---------------------|-----------------|
| **Certificazioni di sicurezza** | Prove di certificazione ISO 27001, report SOC 2 Tipo II o equivalente; o completamento del questionario di sicurezza dei fornitori dell'organizzazione |
| **Pratiche di sviluppo sicuro** | SDLC documentato con attività di sicurezza; utilizzo di SAST, SCA e processi di code review |
| **Sicurezza del personale** | Verifiche dei precedenti per gli sviluppatori che accedono ai dati organizzativi; NDA firmato da tutte le persone con accesso |
| **Protezione dei dati** | Accordo sul trattamento dei dati (DPA) conforme alla nLPD svizzera Art. 9; valutazione della residenza e del trasferimento dei dati completata |
| **Risposta agli incidenti** | Capacità documentata di risposta agli incidenti di sicurezza; capacità di notificare l'organizzazione entro 24 ore da un evento di sicurezza |
| **Continuità aziendale** | Prove di pianificazione della continuità aziendale; deposito del codice sorgente in garanzia o accordo di continuità equivalente ove appropriato |
| **Riferimenti** | Riferimenti verificabili da contratti comparabili |

**Livelli di valutazione**:

| Livello fornitore | Criteri | Profondità della valutazione |
|-------------------|---------|------------------------------|
| **Livello 1 — Alto rischio** | Il fornitore sviluppa applicazioni ad alto rischio; accede ai dati di produzione o ai dati personali; sviluppa sistemi accessibili da Internet | Valutazione completa della sicurezza + audit in loco o da remoto + rivalutazione annuale |
| **Livello 2 — Rischio medio** | Il fornitore sviluppa strumenti interni; accesso limitato ai dati; nessun accesso diretto alla produzione | Questionario di sicurezza + revisione delle prove + rivalutazione biennale |
| **Livello 3 — Basso rischio** | Il fornitore sviluppa utilità non critiche; nessun accesso a dati sensibili | Questionario di sicurezza + autocertificazione + rivalutazione al rinnovo del contratto |

**Determinazione del livello del fornitore**:

I fornitori devono essere classificati in base al fattore di rischio più elevato presente:

**Elementi scatenanti per il Livello 1** (uno solo qualifica):
- Sviluppa applicazioni che trattano dati Riservato o Ristretto
- Accesso diretto agli ambienti di produzione o ai database
- Sviluppa sistemi accessibili da Internet con autenticazione degli utenti
- Tratta dati personali di >1.000 persone
- Personalizza sistemi di elaborazione dei pagamenti o finanziari
- Accesso ai repository del codice sorgente contenenti algoritmi proprietari

**Elementi scatenanti per il Livello 2** (nessuno del Livello 1, uno qualsiasi di questi):
- Sviluppa applicazioni solo per uso interno
- Accesso in sola lettura a dati non di produzione
- Tratta dati personali di <1.000 persone
- Lavoro di integrazione con API di terze parti
- Sviluppo di strumenti di reportistica e analisi

**Livello 3** (predefinito):
- Sviluppo di utilità (script, strumenti CLI, automazione non critica)
- Sviluppo di siti web statici senza raccolta di dati degli utenti
- Documentazione e design UI/UX (nessun accesso al codice)
- Lavoro di prototipazione/proof-of-concept solo con dati sintetici

La determinazione del livello deve essere documentata nel registro della valutazione della sicurezza del fornitore e revisionata in caso di modifiche all'ambito.

I risultati della valutazione devono essere documentati e conservati per la durata della relazione con il fornitore più 3 anni.

I fornitori che non superano la valutazione della sicurezza non devono essere coinvolti fino a quando le carenze identificate non vengono remediate e verificate.

### Segnali d'allarme nella valutazione dei fornitori

Durante la valutazione del fornitore, i seguenti sono rilievi preclusivi a meno che non vengano rimediati:

| Segnale d'allarme | Rischio | Remediation richiesta |
|-------------------|---------|----------------------|
| **Nessun SDLC formale** | Sviluppo non strutturato; pratiche di sicurezza inconsistenti | Documentare l'SDLC con gate di sicurezza; dimostrare ≥3 mesi di applicazione coerente |
| **Nessun strumento SAST/SCA** | Vulnerabilità non rilevate prima della consegna | Implementare la scansione automatica della sicurezza; dimostrare ≥3 scansioni con remediation |
| **Il fornitore rifiuta la clausola sui diritti di audit** | Impossibilità di verificare le dichiarazioni sulla sicurezza | Accettare i diritti di audit o fornire certificazione SOC 2 Tipo II / ISO 27001 |
| **Esternalizza a subcontraenti non dichiarati** | Security posture sconosciuta nella catena di approvvigionamento | Trasparenza totale sui subcontraenti; requisiti di sicurezza a cascata; valutazione di ciascuno |
| **Nessuna capacità di risposta agli incidenti** | Impossibilità di rilevare o rispondere a una compromissione | Documentare il piano IR; fornire impegno di notifica entro 24 ore; dimostrare test IR |
| **Precedente violazione significativa (non risolta)** | Schema di scarsa sicurezza | Dimostrare miglioramenti post-incidente; validazione di terze parti della remediation |
| **Mancanza di verifiche dei precedenti** | Rischio di minaccia interna | Implementare le verifiche dei precedenti per il personale con accesso ai dati |
| **Usa e-mail personale per il lavoro** | Nessuna separazione dei dati aziendali/personali | Fornire e-mail aziendale; documentare la politica di utilizzo accettabile |

**Durante il coinvolgimento, questi sono elementi scatenanti per l'escalation**:
- Il fornitore fornisce informazioni false nella valutazione della sicurezza
- Rilevata esfiltrazione non autorizzata di dati
- Il fornitore rifiuta la remediation delle vulnerabilità
- I risultati dei test di sicurezza vengono trattenuti o falsificati

---

## Requisiti di sicurezza contrattuali

Tutti gli accordi di sviluppo in outsourcing devono includere i requisiti di sicurezza come obblighi contrattuali.

**Clausole contrattuali obbligatorie**:

| Clausola | Requisito |
|----------|-----------|
| **Standard di sviluppo sicuro** | Il fornitore deve conformarsi agli standard di codifica sicura dell'organizzazione e alla Politica sul ciclo di vita dello sviluppo sicuro, o dimostrare standard equivalenti approvati dal RSSI |
| **Test di sicurezza** | Il fornitore deve eseguire SAST e SCA su tutti i deliverable; DAST per le applicazioni web e le API; i risultati devono essere condivisi con l'organizzazione prima dell'accettazione |
| **Remediation delle vulnerabilità** | Vulnerabilità critiche: 7 giorni; Alte: 30 giorni; Medie: 90 giorni; Basse: 180 giorni — allineati agli SLA di remediation dell'organizzazione |
| **Notifica degli incidenti di sicurezza** | Il fornitore deve notificare l'organizzazione entro 24 ore dalla scoperta di un incidente di sicurezza che riguarda il contratto, incluse violazioni dei dati sospette, compromissione del codice o accesso non autorizzato |
| **Diritti di audit** | L'organizzazione si riserva il diritto di verificare le pratiche di sicurezza del fornitore, gli ambienti di sviluppo e i processi con un preavviso scritto di 30 giorni di calendario |
| **Diritti di code review** | L'organizzazione deve avere il diritto di rivedere, testare e ispezionare tutto il codice sorgente, gli script di build e i file di configurazione consegnati ai sensi dell'accordo |
| **Subappalto** | Il fornitore non deve subappaltare il lavoro di sviluppo senza la preventiva approvazione scritta dell'organizzazione; i subappaltatori devono soddisfare requisiti di sicurezza equivalenti |
| **Protezione dei dati** | Accordo sul trattamento dei dati (DPA) secondo la nLPD svizzera Art. 9; i dati personali vengono trattati solo come indicato dall'organizzazione; i trasferimenti transfrontalieri soggetti a valutazione del trasferimento |
| **Riservatezza** | NDA che copre tutte le informazioni proprietarie, il codice sorgente, l'architettura del sistema e i dati accessibili durante il contratto |
| **Disposizioni di risoluzione** | Restituzione o distruzione sicura di tutti i dati organizzativi, codice sorgente, credenziali e accesso alla risoluzione del contratto; verifica entro 30 giorni |

**Clausole contrattuali raccomandate** (in base al rischio del contratto):

| Clausola | Applicabilità |
|----------|---------------|
| **Test di penetrazione** | Richiesto per i fornitori di Livello 1; l'organizzazione o una terza parte qualificata deve condurre test di penetrazione prima dell'accettazione in produzione |
| **Verifiche dei precedenti** | Richiesto per il personale dei fornitori di Livello 1 che accede a dati personali, dati finanziari o ambienti di produzione |
| **Formazione sulla sicurezza** | Il personale del fornitore deve completare il briefing sulla consapevolezza della sicurezza dell'organizzazione o dimostrare una formazione equivalente |
| **Responsabilità e indennizzo** | Responsabilità del fornitore per le violazioni della sicurezza causate dal mancato rispetto dei requisiti di sicurezza contrattuali |
| **Assicurazione** | Assicurazione per responsabilità professionale e cyber liability adeguata al valore e al rischio del contratto |

**Processo di approvazione del subappalto**:

Quando un fornitore richiede l'approvazione del subappalto:
1. **Notifica**: Il fornitore invia una richiesta scritta ≥30 giorni prima del coinvolgimento del subappaltatore, inclusi:
   - Nome e sede del subappaltatore
   - Ambito del lavoro da subappaltare
   - Accesso ai dati richiesto dal subappaltatore
   - Risultati della valutazione della sicurezza del subappaltatore
   - Conferma del flusso dei requisiti di sicurezza contrattuali

2. **Valutazione**: L'organizzazione rivede il subappaltatore in base agli stessi criteri di sicurezza del fornitore principale (valutazione appropriata al livello)

3. **Approvazione**:
   - Fornitori di Livello 1: Richiesta l'approvazione del RSSI
   - Fornitori di Livello 2/3: Approvazione del Responsabile sviluppo con notifica al RSSI

4. **Documentazione**: I subappaltatori approvati vengono aggiunti al registro della valutazione della sicurezza del fornitore; si applicano gli stessi requisiti di monitoraggio e gestione degli accessi

Il subappalto non approvato è una violazione materiale e motivo di risoluzione del contratto.

---

## Requisiti di sviluppo sicuro per i fornitori

Gli standard di sviluppo sicuro dell'organizzazione devono essere comunicati ai fornitori all'inizio di ogni contratto.

**Pacchetto di standard di sviluppo per i fornitori**:

L'organizzazione deve fornire a ciascun fornitore:

- Standard di codifica sicura applicabili allo stack tecnologico in uso.
- Specifica dei requisiti di sicurezza per il progetto.
- Modello delle minacce (dove ne esiste uno per l'applicazione).
- Standard crittografici e librerie approvate.
- Requisiti di registrazione e gestione degli errori.
- Standard di sicurezza delle API (ove applicabile).
- Requisiti di validazione degli input e codifica degli output.

**Requisiti dell'ambiente di sviluppo dei fornitori**:

| Requisito | Dettaglio |
|-----------|-----------|
| **Segregazione degli ambienti** | Gli ambienti di sviluppo, test e produzione devono essere separati; gli ambienti di sviluppo dei fornitori non devono avere accesso diretto ai sistemi di produzione dell'organizzazione |
| **Controllo degli accessi** | L'accesso dei fornitori ai repository e ai sistemi dell'organizzazione deve seguire il principio del privilegio minimo; l'accesso deve essere limitato nel tempo e legato alla durata del contratto |
| **Gestione delle credenziali** | Nessuna credenziale hardcoded nel codice sorgente; segreti gestiti tramite strumenti approvati di gestione dei segreti |
| **Controllo di versione** | Tutto il codice deve essere mantenuto in un sistema di controllo di versione approvato con cronologia completa dei commit e attribuzione |
| **Gestione delle dipendenze** | I fornitori devono mantenere una Software Bill of Materials (SBOM) per tutti i deliverable; le dipendenze di terze parti devono essere ottenute da registri approvati e scansionate per vulnerabilità note |

**Sicurezza della catena di approvvigionamento del software**:

I fornitori devono implementare controlli per mitigare i rischi della catena di approvvigionamento del software in conformità con OWASP Top 10:2025 A03 (Software Supply Chain Failures):

- Tutte le dipendenze di terze parti devono essere inventariate e tracciate in uno SBOM (formato CycloneDX o SPDX).
- Le dipendenze devono essere bloccate a versioni specifiche e ottenute da registri affidabili.
- Le dipendenze transitive devono essere incluse nella scansione delle vulnerabilità.
- I fornitori devono monitorare le dipendenze rispetto ai database delle vulnerabilità (NVD, OSV, GitHub Advisory Database) e rimediare alle vulnerabilità identificate entro gli SLA concordati.
- L'uso di componenti non mantenuti o a fine vita richiede l'accettazione del rischio documentata da parte dell'organizzazione.

**Dettaglio dei requisiti SBOM**:
- **Formato**: CycloneDX 1.4+ (preferito) o SPDX 2.3+
- **Profondità**: Includere le dipendenze transitive (non solo le dipendenze dirette)
- **Contenuto**: Nome del componente, versione, licenza, fornitore, hash crittografico
- **Consegna**: SBOM fornito con ogni rilascio e aggiornato per qualsiasi modifica alle dipendenze
- **Strumento**: Generato tramite strumento SBOM automatizzato (CycloneDX CLI, Syft, strumenti SPDX o equivalente) — non fogli di calcolo creati manualmente
- **Validazione**: L'organizzazione verifica la completezza dello SBOM utilizzando lo strumento SCA prima dell'accettazione

## Flusso di lavoro tipico dello sviluppo con fornitori

```
┌─────────────────────────────────────────────────────────────────┐
│ FASE DI COINVOLGIMENTO                                          │
├─────────────────────────────────────────────────────────────────┤
│ 1. Valutazione della sicurezza del fornitore (RSSI) ───────────┐│
│ 2. Contratto con clausole di sicurezza (Legale + RSSI) ────────┐││
│ 3. Esecuzione del DPA (DPD) ────────────────────────────────────┘││
│ 4. Consegna del pacchetto di sviluppo sicuro (Resp. sviluppo) ──┘│
│ 5. Provisioning degli accessi del fornitore (IT Operations) ────│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE DI SVILUPPO (iterativa)                                    │
├─────────────────────────────────────────────────────────────────┤
│ 6. Sviluppo + test di sicurezza del fornitore (Fornitore) ──────│
│    - SAST/SCA per build                                         │
│    - Risultati dei test condivisi con l'org.                    │
│ 7. Consegna per milestone (Fornitore → Resp. sviluppo) ─────────│
│ 8. Code review dell'organizzazione (Team sicurezza) ────────────│
│ 9. Remediation delle vulnerabilità (Fornitore) ─────────────────│
│    ↺ Ripetere fino al soddisfacimento dei criteri di accettaz. │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE DI ACCETTAZIONE                                            │
├─────────────────────────────────────────────────────────────────┤
│ 10. Test di sicurezza indipendente (Org. / Terza parte) ────────│
│     - SAST/SCA/DAST                                             │
│     - Test di penetrazione (Livello 1)                          │
│ 11. Consegna e revisione dello SBOM (Resp. sviluppo) ───────────│
│ 12. Completamento della checklist di accettazione ──────────────│
│ 13. Approvazione finale (basata sul rischio: RSSI/Resp. svilup.)│
│ 14. Deposito del codice in garanzia (se applicabile) ───────────│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ FASE POST-DISTRIBUZIONE                                         │
├─────────────────────────────────────────────────────────────────┤
│ 15. Deprovisioning degli accessi del fornitore (IT Operations) ─│
│ 16. Verifica della restituzione/distruzione dei dati (DPD) ─────│
│ 17. Contratto di supporto continuativo (se applicabile) ────────│
│ 18. Rivalutazione annuale della sicurezza (Livello 1) ──────────│
└─────────────────────────────────────────────────────────────────┘
```

---

## Code review e test di sicurezza

Tutto il codice in outsourcing deve essere sottoposto a validazione indipendente della sicurezza da parte dell'organizzazione prima dell'accettazione.

**Test del fornitore** (eseguiti dal fornitore, risultati forniti all'organizzazione):

| Tipo di test | Requisito | Tempistica |
|--------------|-----------|------------|
| **SAST** | Scansione di tutto il codice sorgente per vulnerabilità di sicurezza utilizzando [Strumento SAST] (esempi: SonarQube, Semgrep, Checkmarx, Veracode o equivalente approvato dal RSSI) | Per build o almeno settimanalmente durante lo sviluppo attivo |
| **SCA** | Scansione di tutte le dipendenze per vulnerabilità note e conformità delle licenze | Per build o almeno settimanalmente durante lo sviluppo attivo |
| **Test unitari/di integrazione** | Dimostrare l'efficacia dei controlli di sicurezza (autenticazione, autorizzazione, validazione degli input) | Continuo |
| **Scansione dei segreti** | Verificare che non ci siano credenziali, chiavi API o token nel codice sorgente o nella configurazione | Pre-commit e per build |

I risultati dei test del fornitore devono essere condivisi con l'organizzazione agli intervalli concordati (minimo: per milestone o consegna dello sprint).

**Test dell'organizzazione** (eseguiti dall'organizzazione o da una terza parte nominata):

| Tipo di test | Requisito | Tempistica |
|--------------|-----------|------------|
| **Code review indipendente** | Sviluppatore interno o Security Champion revisiona il codice del fornitore rispetto alla checklist di codifica sicura | Prima dell'accettazione di ogni deliverable |
| **SAST/SCA indipendente** | L'organizzazione esegue le proprie scansioni SAST e SCA sul codice consegnato | Prima dell'accettazione |
| **DAST** | Test dinamico dell'applicazione in esecuzione (ad esempio, OWASP ZAP, Burp Suite o equivalente) | Prima della distribuzione in produzione |
| **Test di penetrazione** | Test di penetrazione da parte di uno specialista esterno per le applicazioni ad alto rischio | Prima della distribuzione iniziale in produzione; annualmente in seguito |

**Base minima per i test**: Tutti i test di sicurezza devono, come minimo, coprire le categorie OWASP Top 10:2025.

Tutti i test di penetrazione devono essere condotti da una società specializzata indipendente esterna che soddisfi almeno uno dei seguenti requisiti:
- Certificazione CREST (CREST Registered Penetration Tester o superiore)
- Membri del team con certificazioni OSCP, GPEN o CEH
- Esperienza dimostrata con ≥5 test di penetrazione comparabili negli ultimi 2 anni con riferimenti verificabili
- Azienda di pentesting certificata ISO 27001 con portfolio di clienti pubblico

Il fornitore dei test di penetrazione non deve essere la stessa entità del fornitore di sviluppo per garantire l'indipendenza.

Le vulnerabilità identificate durante i test devono essere remediate dal fornitore a spese del fornitore prima che l'organizzazione accetti il deliverable. Le vulnerabilità critiche e alte bloccano l'accettazione.

### Gestione della remediation delle vulnerabilità

Tutte le vulnerabilità identificate nei deliverable dei fornitori devono essere tracciate fino alla risoluzione:

**Processo di tracciamento**:
1. **Scoperta**: Vulnerabilità identificata tramite SAST/SCA/DAST/pentest
2. **Assegnazione**: Vulnerabilità assegnata al fornitore con SLA di remediation
3. **Verifica**: Il fornitore fornisce la correzione + i risultati del re-test
4. **Validazione**: L'organizzazione valida l'efficacia della correzione
5. **Chiusura**: Chiusura documentata con prove dei test

**Tracciamento degli SLA di remediation**:

| Gravità | SLA | Risposta alla violazione dello SLA |
|---------|-----|-------------------------------------|
| **Critica** | 7 giorni | Escalation immediata al RSSI; bloccare l'accettazione; revisione delle prestazioni del fornitore |
| **Alta** | 30 giorni | Escalation al Responsabile sviluppo; accettazione condizionata al piano di remediation |
| **Media** | 90 giorni | Monitoraggio nelle riunioni di stato settimanali; può essere accettata con accettazione del rischio documentata e impegno di remediation |
| **Bassa** | 180 giorni | Monitoraggio nel backlog del progetto; può essere accettata con uno sprint futuro pianificato per la remediation |

**Decorrenza dello SLA**:
- Inizia dalla divulgazione della vulnerabilità al fornitore
- Si interrompe per richieste di chiarimento ragionevoli del fornitore (<5 giorni lavorativi)
- Si azzera su richiesta del fornitore di estensione dello SLA con giustificazione (approvazione del RSSI)

**Reportistica sulla conformità agli SLA**:
Tracciata per fornitore, per contratto. Una conformità <70% attiva la revisione delle prestazioni del fornitore.

---

## Criteri di accettazione

I deliverable in outsourcing non devono essere accettati o distribuiti in produzione fino a quando tutti i criteri di accettazione non sono soddisfatti.

**Checklist di accettazione della sicurezza**:

| # | Criterio | Verificato da |
|---|----------|---------------|
| 1 | Tutti i test di sicurezza contrattualmente richiesti completati e risultati forniti | Responsabile sviluppo |
| 2 | Nessuna vulnerabilità critica o alta non risolta nei risultati SAST, SCA, DAST o dei test di penetrazione | RSSI / Team sicurezza |
| 3 | Code review indipendente dell'organizzazione completata senza rilievi bloccanti | Responsabile sviluppo |
| 4 | SBOM fornito in formato CycloneDX o SPDX; nessun componente con vulnerabilità critiche o alte non risolte dove esistono patch disponibili; le vulnerabilità senza patch richiedono accettazione del rischio documentata e controlli compensativi | Responsabile sviluppo |
| 5 | Nessun segreto hardcoded, credenziali o dati di test presenti nel codice consegnato | Team sicurezza |
| 6 | Il codice soddisfa gli standard di codifica sicura dell'organizzazione | Security Champion / Sviluppatore senior |
| 7 | Tutta la documentazione consegnata (architettura, specifiche API, guide alla distribuzione, configurazione) | Responsabile sviluppo |
| 8 | Codice sorgente e tutti gli artefatti consegnati al repository dell'organizzazione o all'agente di deposito | Responsabile sviluppo |
| 9 | Requisiti di protezione dei dati soddisfatti; nessun dato personale non autorizzato conservato dal fornitore | Responsabile della protezione dei dati / RSSI |
| 10 | Licenze e proprietà intellettuale confermate secondo il contratto | Legale / Acquisti |

*I rilievi bloccanti includono:*
- Credenziali hardcoded, chiavi API o segreti
- Vulnerabilità di SQL injection (qualsiasi gravità)
- Vulnerabilità di bypass dell'autenticazione
- Difetti di autorizzazione che consentono l'escalation dei privilegi
- Uso di algoritmi crittograficamente compromessi (MD5, SHA-1 per la sicurezza, DES, RC4)
- Esposizione di dati sensibili in log o messaggi di errore
- Validazione degli input mancante per i dati forniti dagli utenti
- Rilievi critici o alti da SAST/DAST non affrontati

**Approvazione dell'accettazione**:

| Rischio dell'applicazione | Approvazione richiesta |
|---------------------------|------------------------|
| Alto rischio | RSSI + Responsabile sviluppo + Proprietario dell'applicazione |
| Rischio medio | Responsabile sviluppo + Proprietario dell'applicazione |
| Basso rischio | Responsabile sviluppo |

I registri di accettazione devono essere conservati per la durata del ciclo di vita dell'applicazione più 3 anni.

---

## Proprietà intellettuale e deposito del codice in garanzia

**Proprietà del codice**:

L'accordo di sviluppo deve definire chiaramente la proprietà di tutti i prodotti del lavoro, inclusi codice sorgente, documentazione, design e proprietà intellettuale correlata.

Laddove l'organizzazione commissiona lo sviluppo su misura, la posizione predefinita è che l'organizzazione possiede tutti i diritti di proprietà intellettuale sui deliverable al pagamento finale o alla consegna se il pagamento è alla consegna, a seconda di quale si verifica prima. Qualsiasi deroga alla proprietà totale deve essere documentata, approvata dal Legale e dal RSSI, e giustificata da esigenze aziendali.

**Licenze**:

Laddove il trasferimento completo della proprietà non è possibile (ad esempio, il fornitore mantiene i diritti sui componenti o sui framework preesistenti), l'accordo deve specificare:

- Una licenza perpetua e irrevocabile per l'organizzazione di utilizzare, modificare e mantenere il software consegnato.
- Identificazione chiara dei componenti di proprietà del fornitore rispetto a quelli di proprietà dell'organizzazione.
- Termini di licenza per tutti i componenti di terze parti e open source inclusi nel deliverable.

**Deposito del codice in garanzia**:

Per i contratti con fornitori di Livello 1 dove l'organizzazione non detiene direttamente il codice sorgente, l'organizzazione deve stabilire un accordo di deposito del codice in garanzia con un agente indipendente (ad esempio, Escode, Codekeeper o equivalente).

**Requisiti dell'accordo di deposito**:

| Requisito | Dettaglio |
|-----------|-----------|
| **Frequenza del deposito** | Codice sorgente depositato ad ogni rilascio principale, o almeno trimestralmente |
| **Contenuto del deposito** | Codice sorgente completo, script di build, specifiche dell'ambiente di build, documentazione, dipendenze e istruzioni di distribuzione sufficienti per costruire e distribuire il software in modo indipendente |
| **Condizioni di rilascio** | Insolvenza del fornitore, cessazione dell'attività, violazione materiale degli obblighi di manutenzione o mancata fornitura dei servizi contrattati |
| **Verifica** | I depositi in garanzia vengono verificati annualmente dall'agente di deposito (verifica della build — confermando che il codice depositato si compila e produce una build funzionante) |

**Criteri di verifica del deposito in garanzia**:
- Il codice sorgente si compila senza errori utilizzando le istruzioni di build documentate
- Tutte le dipendenze risolvibili dai repository pubblici o privati documentati
- Le specifiche dell'ambiente di build includono tutti gli strumenti, gli SDK e le versioni richiesti
- L'artefatto di build risultante (eseguibile, immagine container, pacchetto distribuibile) può essere distribuito in un ambiente di test
- Il test di base funzionale supera (l'applicazione si avvia, l'endpoint di health check risponde)
- Nessuno strumento proprietario esclusivo del fornitore richiesto per il processo di build

Verifica eseguita dall'agente di deposito annualmente. La verifica non riuscita richiede che il fornitore corregga il deposito entro 30 giorni.

Laddove l'organizzazione detiene direttamente il codice sorgente nei propri repository, il deposito in garanzia non è richiesto, ma l'organizzazione deve mantenere i propri backup verificati.

---

## Monitoraggio continuativo

L'organizzazione deve monitorare continuamente le attività di sviluppo in outsourcing durante tutto il ciclo di vita del contratto.

**Attività di monitoraggio**:

| Attività | Frequenza | Responsabile |
|----------|-----------|--------------|
| **Revisione dei report dei test di sicurezza** | Per milestone o consegna dello sprint | Responsabile sviluppo |
| **Revisione dei progressi e della qualità** | Ogni 2 settimane o per sprint (per i contratti agili) | Responsabile sviluppo / Project Manager |
| **Revisione della security posture del fornitore** | Annualmente (Livello 1); biennalmente (Livello 2); al rinnovo (Livello 3) | RSSI / Responsabile della sicurezza delle informazioni |
| **Revisione degli accessi** | Trimestrale — verificare che il personale del fornitore con accesso attivo ne abbia ancora bisogno | IT Operations / Responsabile sviluppo |
| **Verifica a campione della conformità** | Semestralmente — verificare l'aderenza del fornitore agli standard di codifica sicura | Team sicurezza |
| **Revisione degli incidenti e dei quasi-incidenti** | Per occorrenza | RSSI |

La scorecard delle prestazioni del fornitore deve essere mantenuta trimestralmente, tracciando: conformità ai test di sicurezza, rispetto degli SLA, conteggio degli incidenti e rilievi degli audit. I risultati devono essere comunicati alla direzione annualmente.

**Elementi scatenanti per l'escalation**:

| Elemento scatenante | Azione |
|--------------------|--------|
| Il fornitore non fornisce i risultati dei test di sicurezza entro i tempi concordati | Escalare al Responsabile sviluppo; bloccare l'accettazione |
| Vulnerabilità critica identificata nel codice consegnato dal fornitore | Escalare al RSSI; remediation del fornitore entro 7 giorni |
| Incidente di sicurezza del fornitore che riguarda i dati o i sistemi dell'organizzazione | Attivare il processo di gestione degli incidenti (A.5.24-28); notificare il RSSI entro 1 ora |
| Il fornitore non supera la rivalutazione annuale della sicurezza | Sospendere le nuove assegnazioni di lavoro; piano di remediation entro 30 giorni; revisione del contratto |
| Prove di subappalto non autorizzato | Escalare al RSSI e al Legale; revisione del contratto |

---

## Risposta agli incidenti di sicurezza del fornitore

Quando un fornitore subisce un incidente di sicurezza che riguarda il contratto dell'organizzazione:

**Obbligo di notifica del fornitore**:
- **Entro 24 ore**: Notifica iniziale dell'occorrenza dell'incidente, della natura e dell'impatto potenziale
- **Entro 72 ore**: Report dettagliato sull'incidente incluso l'ambito, l'analisi della causa principale (preliminare), i sistemi/dati interessati e le azioni di remediation

**Risposta dell'organizzazione**:

| Tipo di incidente | Azione di risposta |
|-------------------|-------------------|
| **Compromissione del repository del codice del fornitore** | 1. Sospendere l'accesso del fornitore ai sistemi dell'org. 2. Revisione forense di tutto il codice consegnato dal fornitore 3. Completo re-testing della sicurezza prima di qualsiasi ulteriore accettazione 4. Considerare la riscrittura del codice se si sospetta codice malevolo |
| **Furto delle credenziali del personale del fornitore** | 1. Revocare immediatamente tutte le credenziali di accesso del fornitore 2. Rivedere i log di accesso per attività non autorizzate 3. Riemettere le credenziali dopo che il fornitore conferma la remediation della compromissione 4. AMF obbligatoria per il nuovo accesso |
| **Violazione dei dati del fornitore (dati dell'org. esposti)** | 1. Attivare il processo di risposta agli incidenti dell'org. 2. Valutare i requisiti di notifica all'autorità di protezione dei dati 3. Indagine sull'incidente congiunta 4. Revisione del contratto per responsabilità e costi di remediation |
| **Compromissione della catena di approvvigionamento del fornitore** | 1. Sospendere l'accettazione di qualsiasi deliverable che utilizza il componente interessato 2. Revisionare lo SBOM per la dipendenza interessata in tutto il lavoro del fornitore 3. Richiedere al fornitore di rimuovere/sostituire il componente compromesso 4. Re-testing indipendente della sicurezza |

Il RSSI deve notificare la Direzione generale entro 24 ore da qualsiasi incidente del fornitore che riguardi i dati o i sistemi organizzativi.

**Azioni post-incidente**:
- Il fornitore deve fornire un report post-incidente entro 30 giorni
- L'organizzazione conduce una rivalutazione della sicurezza del fornitore
- La continuazione del contratto è subordinata a una remediation soddisfacente
- Gli incidenti significativi possono attivare la clausola di risoluzione del contratto

---

## Requisiti di protezione dei dati

Laddove lo sviluppo in outsourcing comporta l'accesso a dati personali o a sistemi che trattano dati personali, si applicano ulteriori requisiti di protezione dei dati.

**Accordo sul trattamento dei dati (DPA)**:

In conformità con la nLPD svizzera Art. 9, l'organizzazione deve eseguire un DPA con il fornitore di sviluppo che tratti:

- Categorie e tipi di dati personali accessibili.
- Scopo e durata del trattamento.
- Obbligo di trattare i dati solo come indicato dall'organizzazione.
- Obblighi di riservatezza per il personale del fornitore.
- Misure tecniche e organizzative di sicurezza implementate dal fornitore.
- Requisiti di notifica e approvazione dei sub-responsabili del trattamento.
- Obblighi di assistenza per i diritti degli interessati.
- Restituzione e cancellazione dei dati alla risoluzione del contratto.
- Diritti di audit e ispezione.

**Trasferimenti transfrontalieri**:

Laddove lo sviluppo del fornitore avviene al di fuori della Svizzera:

- Deve essere completata una valutazione dell'impatto del trasferimento secondo i requisiti della nLPD svizzera.
- Devono essere in atto salvaguardie appropriate (ad esempio, Clausole contrattuali standard, decisioni di adeguatezza del Consiglio federale o norme vincolanti d'impresa).
- Laddove il fornitore tratta dati di persone nell'UE/SEE, devono essere soddisfatti anche i requisiti di trasferimento del Capitolo V del GDPR.

**Minimizzazione dei dati per lo sviluppo**:

- I fornitori non devono ricevere dati personali di produzione per scopi di sviluppo o test.
- Laddove sono richiesti dati realistici, devono essere utilizzati dati sanificati, anonimizzati o pseudonimizzati.
- I dati sintetici (generati artificialmente) sono l'approccio preferito.
- Qualsiasi uso di dati personali trasformati deve essere documentato e approvato dal Responsabile della protezione dei dati o dal RSSI.

**Approcci di generazione di dati sintetici**:
- **Librerie Faker**: Dati realistici ma falsi (nomi, indirizzi, e-mail) — adatti per test UI, sviluppo di reportistica
- **Strumenti di mascheratura dei dati**: Mantenere la struttura dei dati e l'integrità referenziale oscurando i valori — adatti per test di schemi complessi
- **Generazione basata su regole**: Generare dati corrispondenti ai pattern e alle distribuzioni di produzione — adatti per i test delle prestazioni
- **Dati generati dall'AI**: Modelli ML addestrati su dati di produzione per generare dataset sintetici statisticamente simili — adatti per lo sviluppo di analisi

Esempi di strumenti: Faker (Python/JavaScript), Mockaroo (web-based), Tonic.ai, Gretel.ai (enterprise)

Laddove è assolutamente necessario utilizzare dati di produzione (relazioni di dati complesse, casi limite rari), i dati devono essere:
1. Limitati al numero minimo di record richiesti (non dump completo della produzione)
2. Anonimizzati o pseudonimizzati secondo nLPD Art. 5
3. Approvati dal Responsabile della protezione dei dati con giustificazione documentata
4. Cifrati a riposo e in transito verso l'ambiente del fornitore
5. Eliminati dai sistemi del fornitore entro 30 giorni dal completamento dello sviluppo

**Notifica all'Incaricato federale della protezione dei dati e della trasparenza (IFPDT)**:

Laddove un incidente di sicurezza del fornitore comporta un rischio elevato per gli interessati (nLPD Art. 24), l'organizzazione deve notificare l'IFPDT senza indebito ritardo. Gli indicatori di rischio elevato includono:
- Accesso non autorizzato a categorie particolari di dati personali (Art. 5 cpv. 2)
- Violazione dei dati che riguarda >500 residenti svizzeri
- Compromissione di dati personali sensibili (salute, finanziario, biometrico)
- Incidente che coinvolge dati di profilazione sistematica o di processo decisionale automatizzato

Il DPA del fornitore deve richiedere che il fornitore fornisca tutte le informazioni necessarie per la notifica all'IFPDT entro 48 ore dalla scoperta dell'incidente.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Test di accettazione** | Verifica formale che un deliverable soddisfi i requisiti specificati prima della distribuzione |
| **Deposito del codice in garanzia** | Accordo in cui il codice sorgente viene depositato presso una terza parte indipendente per il rilascio all'organizzazione in condizioni specificate |
| **DAST** | Dynamic Application Security Testing — analizza le applicazioni in esecuzione per vulnerabilità di sicurezza |
| **DPA** | Accordo sul trattamento dei dati — contratto che regola la gestione dei dati personali da parte di un responsabile del trattamento per conto del titolare del trattamento |
| **SAST** | Static Application Security Testing — analizza il codice sorgente per vulnerabilità di sicurezza senza eseguire il codice |
| **SBOM** | Software Bill of Materials — inventario di tutti i componenti software, le dipendenze e le loro versioni |
| **SCA** | Software Composition Analysis — identifica vulnerabilità e problemi di licenza nelle dipendenze di terze parti e open source |
| **Sub-responsabile del trattamento** | Terza parte coinvolta dal responsabile del trattamento dei dati (fornitore) per trattare i dati personali per conto del titolare del trattamento (organizzazione) |
| **Attacco alla catena di approvvigionamento** | Compromissione di un componente software, di una dipendenza o di uno strumento di sviluppo per iniettare codice malevolo o vulnerabilità nei sistemi a valle |
| **Fornitore di Livello 1/2/3** | Classificazione del rischio del fornitore basata sulla sensibilità dei sistemi sviluppati e dei dati accessibili |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **RSSI** | Titolarità della politica; approvazione della valutazione della sicurezza dei fornitori di Livello 1; approvazione finale per le applicazioni ad alto rischio; approvazione delle eccezioni; autorità di escalation; revisione annuale della politica |
| **Responsabile sviluppo** | Coordinamento del coinvolgimento dei fornitori; comunicazione dei requisiti di sicurezza; gestione della code review e dell'accettazione; monitoraggio dei deliverable dei fornitori; reportistica sulla conformità |
| **Responsabile della sicurezza delle informazioni** | Gestione dei questionari di sicurezza dei fornitori; verifiche a campione della conformità; monitoraggio della security posture dei fornitori; coordinamento delle indagini sugli incidenti |
| **Project Manager** | Gestione quotidiana della relazione con il fornitore; tracciamento delle milestone di consegna; escalation delle preoccupazioni di sicurezza al Responsabile sviluppo |
| **Responsabile della protezione dei dati / RSSI** | Revisione e approvazione dei DPA; valutazioni dell'impatto del trasferimento transfrontaliero; verifica della minimizzazione dei dati; coordinamento dei diritti degli interessati |
| **Legale / Acquisti** | Redazione e revisione dei contratti; termini IP e licenze; gestione degli NDA; verifica delle assicurazioni; coordinamento degli accordi di deposito in garanzia |
| **Team sicurezza** | Test di sicurezza indipendente dei deliverable dei fornitori; coordinamento dei test di penetrazione; esecuzione SAST/DAST/SCA; triage delle vulnerabilità |
| **IT Operations** | Provisioning e deprovisioning degli accessi dei fornitori; supporto alla revisione degli accessi; segregazione degli ambienti per l'accesso dei fornitori |
| **Proprietario dell'applicazione** | Avvio dei requisiti di sicurezza; approvazione finale; richieste di eccezione; budget per i test di sicurezza |

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| # | Prova | Responsabile | Frequenza | Conservazione |
|---|-------|--------------|-----------|---------------|
| 1 | **Registri della valutazione della sicurezza dei fornitori** (questionari, report di audit, prove di certificazione, decisioni di valutazione) | RSSI / Responsabile sicurezza informazioni | Per contratto + rivalutazione annuale (Livello 1) | Durata della relazione con il fornitore + 3 anni |
| 2 | **Contratti di sviluppo con clausole di sicurezza** (accordi firmati, DPA, NDA, accordi di deposito in garanzia) | Legale / Acquisti | Per contratto | Durata del contratto + 7 anni |
| 3 | **Report dei test di sicurezza del fornitore** (risultati SAST, SCA, DAST forniti dal fornitore per milestone) | Responsabile sviluppo | Per milestone o consegna dello sprint | Ciclo di vita dell'applicazione + 3 anni |
| 4 | **Risultati dei test indipendenti dell'organizzazione** (code review interna, SAST/SCA/DAST indipendente, report dei test di penetrazione) | Team sicurezza / RSSI | Per accettazione | Ciclo di vita dell'applicazione + 3 anni |
| 5 | **Registri di approvazione dell'accettazione** (checklist di accettazione della sicurezza, approvazione con data, approvatore, condizioni) | Responsabile sviluppo | Per deliverable | Ciclo di vita dell'applicazione + 3 anni |
| 6 | **Registri degli accessi dei fornitori** (concessioni di accesso, revisioni trimestrali, conferme di deprovisioning) | IT Operations / Responsabile sviluppo | Per evento di accesso; revisioni trimestrali | Durata della relazione con il fornitore + 3 anni |
| 7 | **Registri SBOM** (Software Bill of Materials per ogni deliverable accettato) | Responsabile sviluppo | Per deliverable | Ciclo di vita dell'applicazione + 3 anni |
| 8 | **Registri del deposito in garanzia e di verifica** (conferme del deposito, risultati annuali della verifica della build) | Legale / Responsabile sviluppo | Per deposito + verifica annuale | Durata del contratto + 3 anni |
| 9 | **Tracciamento della remediation delle vulnerabilità** (registri di remediation del fornitore, conformità agli SLA, prove di chiusura) | Responsabile sviluppo / Team sicurezza | Per vulnerabilità | 3 anni |
| 10 | **Registri di monitoraggio del fornitore** (revisioni dei progressi, verifiche a campione della conformità, registri di escalation) | Responsabile sviluppo / RSSI | Per ciclo di revisione | Durata della relazione con il fornitore + 3 anni |
| 11 | **Registri della protezione dei dati** (DPA, valutazioni dell'impatto del trasferimento, approvazioni della minimizzazione dei dati) | Responsabile protezione dati / RSSI | Per contratto | Durata del contratto + 10 anni (nLPD) |
| 12 | **Registro delle eccezioni** (richieste di eccezione, approvazioni, controlli compensativi, revisioni trimestrali) | Responsabile sicurezza informazioni | Per eccezione; rivisto trimestralmente | Durata dell'eccezione + 3 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, registri della valutazione della sicurezza dei fornitori, audit delle clausole contrattuali, report dei test di sicurezza, registri di accettazione, revisioni degli accessi, audit interni ed esterni e feedback al proprietario della politica.

**Metriche di conformità**:

| Metrica | Obiettivo | Frequenza di misurazione |
|---------|-----------|--------------------------|
| Contratti con fornitori con valutazione della sicurezza completata prima della firma | 100% | Per contratto |
| Contratti di sviluppo contenenti tutte le clausole di sicurezza obbligatorie | 100% | Per contratto |
| Deliverable in outsourcing con test di sicurezza indipendente dell'organizzazione prima dell'accettazione | 100% | Per deliverable |
| Vulnerabilità segnalate dal fornitore remediate entro lo SLA | >= 90% | Trimestrale |
| Revisioni degli accessi del fornitore completate secondo il calendario | 100% | Trimestrale |
| Fornitori di Livello 1 con rivalutazione della sicurezza corrente (entro 12 mesi) | 100% | Annualmente |
| Depositi in garanzia correnti (entro la frequenza concordata) | 100% | Per calendario dei depositi |

**Gestione della non conformità**: Al di sotto del 70% su qualsiasi metrica richiede un'escalation immediata al RSSI e un piano di remediation. 70-89% richiede la supervisione del Responsabile della sicurezza delle informazioni con revisione mensile fino al ripristino. Il 90% e oltre segue il monitoraggio trimestrale standard.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata dal Responsabile della sicurezza delle informazioni in anticipo, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita (massimo 12 mesi). Le eccezioni devono essere comunicate al Team di revisione della direzione.

## Non conformità

Un dipendente che si constata abbia violato questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. La non conformità del fornitore deve essere affrontata attraverso rimedi contrattuali, inclusa la sospensione o la risoluzione del contratto per violazioni materiali della sicurezza.

## Miglioramento continuo

Questa politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare le modifiche alle pratiche del settore dell'outsourcing e al panorama delle minacce della catena di approvvigionamento, le tecniche emergenti di attacco alla catena di approvvigionamento del software (dependency confusion, typosquatting, compromissione della pipeline CI/CD), le modifiche normative che riguardano gli accordi sul trattamento dei dati e i trasferimenti transfrontalieri, gli aggiornamenti del framework di gestione dei fornitori, i risultati degli audit e le lezioni apprese dagli incidenti di sicurezza che coinvolgono lo sviluppo in outsourcing.

---

## Checklist di implementazione (per le organizzazioni che si avvicinano all'outsourcing)

**Prima di coinvolgere il primo fornitore**:
- [ ] Modello del questionario di valutazione della sicurezza dei fornitori creato
- [ ] Modello di contratto standard per lo sviluppo in outsourcing con clausole di sicurezza redatto (revisione Legale)
- [ ] Modello DPA conforme alla nLPD svizzera Art. 9 preparato (revisione DPD)
- [ ] Standard di codifica sicura documentati e pubblicati
- [ ] Strumenti SAST/SCA/DAST selezionati e operativi
- [ ] Modello della checklist di accettazione della sicurezza creato
- [ ] Processo di provisioning degli accessi dei fornitori documentato
- [ ] Agente di deposito in garanzia selezionato (se applicabile per il Livello 1)

**Per ogni contratto**:
- [ ] Livello del fornitore determinato e documentato
- [ ] Valutazione della sicurezza completata e approvata
- [ ] Contratto con clausole di sicurezza firmato
- [ ] DPA eseguito (se il fornitore accede a dati personali)
- [ ] Pacchetto di sviluppo sicuro consegnato al fornitore
- [ ] Verifiche dei precedenti del personale del fornitore verificate (Livello 1)
- [ ] Accesso del fornitore provisioning con privilegio minimo
- [ ] Cadenza dei test di sicurezza programmata (revisioni per milestone/sprint)
- [ ] Criteri di accettazione comunicati al fornitore
- [ ] Repository del codice o accordo di deposito in garanzia stabilito

---

# Aree della norma ISO 27001 trattate

Politica sullo sviluppo in outsourcing — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.19 Sicurezza delle informazioni nelle relazioni con i fornitori |
| Clausola 7.3 Consapevolezza | 5.20 Gestione della sicurezza delle informazioni negli accordi con i fornitori |
| | 5.21 Gestione della sicurezza delle informazioni nella catena di approvvigionamento ICT |
| | 5.22 Monitoraggio, revisione e gestione delle modifiche dei servizi dei fornitori |
| | 5.36 Conformità a politiche, regole e standard |
| | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 8.4 Accesso al codice sorgente |
| | 8.25 Ciclo di vita dello sviluppo sicuro |
| | 8.26 Requisiti di sicurezza delle applicazioni |
| | 8.28 Codifica sicura |
| | 8.29 Test di sicurezza nello sviluppo e nell'accettazione |
| | **8.30 Sviluppo in outsourcing** |
| | 8.31 Separazione degli ambienti di sviluppo, test e produzione |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|------------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la protezione dei dati; Art. 9 — Trattamento dei dati da parte di terzi (accordi con i responsabili del trattamento) |
| OPDo svizzera | Art. 1-3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 28 — Obblighi del responsabile del trattamento; Art. 32 — Sicurezza del trattamento; Capitolo V — Trasferimenti transfrontalieri di dati |
| ISO/IEC 27001:2022 | Controllo Allegato A 8.30 — Sviluppo in outsourcing |
| ISO/IEC 27002:2022 | Sezione 8.30 — Guida all'implementazione dello sviluppo in outsourcing |
| NIST SP 800-53 Rev 5 | SA-4 (Acquisition Process), SA-9 (External System Services) |
| OWASP Top 10:2025 | A03 — Software Supply Chain Failures |
| CIS Controls v8 | 16.4 (Third-Party Software Component Inventory), 16.6 (Severity Rating for Application Vulnerabilities) |

---

<!-- QA_VERIFIED: 2026-04-03 -->

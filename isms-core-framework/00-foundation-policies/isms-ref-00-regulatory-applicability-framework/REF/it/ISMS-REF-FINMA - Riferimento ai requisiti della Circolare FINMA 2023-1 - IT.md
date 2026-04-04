<!-- ISMS-CORE:REF:ISMS-REF-FINMA-IT-finma-circular-2023-1-requirements:framework:REF:finma -->
**ISMS-REF-FINMA — Riferimento ai requisiti della Circolare FINMA 2023/1**
**Requisiti di sicurezza delle informazioni per gli istituti finanziari svizzeri (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento ai requisiti della Circolare FINMA 2023/1 |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-FINMA |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | RSSI (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale (o in seguito ad aggiornamenti delle circolari FINMA)
**Prossima data di revisione**: [Data + 12 mesi]

**Distribuzione**: Team di conformità, RSSI, consulente legale (per le organizzazioni soggette alla vigilanza FINMA)

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione.

- Questo documento NON fa parte del Sistema di Gestione della Sicurezza delle Informazioni (SGSI).
- Questo documento NON definisce requisiti obbligatori a meno che [Organizzazione] non sia un'entità regolata da FINMA.
- Questo documento NON stabilisce requisiti vincolanti, scadenze, ICP o SLA per le entità non regolate.
- Questo documento NON sostituisce né estende alcuna politica SGSI.

**Determinazione dell'applicabilità**:
I requisiti FINMA si applicano SOLO SE [Organizzazione]:

- È titolare di una licenza FINMA (banca, commerciante di valori mobiliari, assicurazione, gestione di fondi, servizi di pagamento)
- È soggetta alla vigilanza FINMA
- Opera come istituto finanziario svizzero

---

# Panoramica e applicabilità FINMA

## Cos'è la FINMA?

L'**Autorità federale di vigilanza sui mercati finanziari (FINMA)** è l'autorità di vigilanza svizzera responsabile della supervisione di banche, compagnie assicurative, borse, commercianti di valori mobiliari e altri intermediari finanziari in Svizzera.

**Base giuridica principale**:
- Legge federale sulla vigilanza dei mercati finanziari (LFINMA)
- Legge federale sulle banche (LBCR)
- Legge federale sulla sorveglianza delle imprese di assicurazione (LSA)
- Legge federale sugli istituti finanziari (LIsFi)

## Circolari FINMA

**Circolare FINMA 2023/1** — Rischi operativi e resilienza (banche):

- In vigore dal: 1° giugno 2024
- Si applica a: Banche e commercianti di valori mobiliari
- Ambito: Gestione del rischio operativo, continuità operativa, sicurezza delle informazioni, esternalizzazione
- **Margini 50-62**: Requisiti di sicurezza delle informazioni
- **Margini 63-72**: Requisiti di registrazione e monitoraggio
- **Margini 73-87**: Requisiti di continuità operativa e resilienza

**Circolare FINMA 2008/7** — Esternalizzazione (banche): gestione del rischio nelle relazioni di esternalizzazione.

## Determinazione dell'applicabilità

| Criterio | Stato | Prova |
|----------|-------|-------|
| È titolare di licenza bancaria FINMA | ⬜ Sì ⬜ No | [N. licenza / N/A] |
| È titolare di licenza di commerciante di valori mobiliari FINMA | ⬜ Sì ⬜ No | |
| È titolare di licenza assicurativa FINMA | ⬜ Sì ⬜ No | |
| È titolare di licenza di gestione di fondi FINMA | ⬜ Sì ⬜ No | |
| È soggetta alla vigilanza FINMA | ⬜ Sì ⬜ No | |

**Se QUALSIASI "Sì"**: i requisiti FINMA sono di **Livello 1 (Conformità obbligatoria)** ai sensi di POL-00.

---

# Circolare FINMA 2023/1 — Requisiti di sicurezza delle informazioni

## Panoramica (Margini 50-62)

**Principio fondamentale**: Le organizzazioni devono implementare misure di sicurezza delle informazioni **basate sul rischio** appropriate a natura e portata delle attività, complessità dei sistemi IT, sensibilità dei dati trattati e panorama delle minacce.

FINMA NON prescrive controlli tecnici specifici ma richiede "misure organizzative e tecniche appropriate."

## Margine 50: Strategia di sicurezza delle informazioni

**Requisito**: Definire e implementare una strategia di sicurezza delle informazioni allineata alla strategia aziendale, alla strategia IT, ai requisiti normativi e alle migliori pratiche del settore.

**Mappatura ISO 27001:2022**: Clausola 5.2; Clausola 6.2; A.5.1

**Considerazioni chiave**: Approvazione a livello di organo di gestione; revisione annuale; integrazione con la gestione del rischio aziendale; ruoli e responsabilità chiari (RSSI, gestione IT, unità aziendali).

## Margine 51: Organizzazione della sicurezza delle informazioni

**Requisito**: Struttura organizzativa chiara con ruoli e responsabilità definiti; separazione dei compiti (sviluppo, operazioni, sicurezza); funzione di sicurezza indipendente con autorità sufficiente; percorsi di escalation.

**Ruoli chiave attesi da FINMA**: RSSI o equivalente; Comitato per la sicurezza delle informazioni; Proprietari dei sistemi; Architetti della sicurezza; Team delle operazioni di sicurezza.

**Mappatura ISO 27001:2022**: Clausola 5.3; A.5.2

## Margine 52: Valutazione del rischio

**Requisito**: Valutazioni regolari del rischio di sicurezza delle informazioni che coprono identificazione delle risorse, valutazione delle minacce e delle vulnerabilità, valutazione e prioritizzazione del rischio, decisioni di trattamento del rischio, accettazione del rischio residuo.

**Aspettative FINMA**: Valutazione del rischio minimo annuale; valutazioni attivate da cambiamenti importanti; segnalazione dei rischi chiave al consiglio di amministrazione.

**Mappatura ISO 27001:2022**: Clausole 6.1.2, 6.1.3, 8.2, 8.3

## Margine 53: Politiche e standard di sicurezza

**Requisito**: Politiche e standard di sicurezza delle informazioni completi che coprono classificazione delle informazioni, controllo degli accessi, crittografia, sicurezza fisica, gestione degli incidenti, continuità operativa.

**Requisiti di documentazione**: Gerarchia di politiche (strategia → politica → standard → procedure); revisione e aggiornamento regolari; approvazione della direzione.

**Mappatura ISO 27001:2022**: A.5.1; A.5.10; A.5.12

## Margine 54: Sensibilizzazione e formazione sulla sicurezza

**Requisito**: Programma di sensibilizzazione e formazione che garantisca che tutto il personale comprenda gli obblighi di sicurezza; formazione specifica per ruolo; campagne di sensibilizzazione regolari; test di phishing.

**Aspettative FINMA**: Formazione annuale obbligatoria per tutto il personale; formazione specializzata per gli utenti privilegiati; tracciamento e metriche del completamento della formazione.

**Mappatura ISO 27001:2022**: A.6.3

## Margine 55: Gestione del rischio di terzi

**Requisito**: Approccio basato sul rischio alla sicurezza dei terzi, con valutazioni dei fornitori, requisiti contrattuali di sicurezza, monitoraggio continuo, diritto di audit.

**Specifico FINMA**: La Circolare FINMA 2008/7 si applica alle relazioni di esternalizzazione; l'esternalizzazione materiale richiede la notifica alla FINMA; strategie di uscita e pianificazione della transizione obbligatorie.

**Mappatura ISO 27001:2022**: A.5.19; A.5.20; A.5.21

## Margine 56: Autenticazione e controllo degli accessi

**Requisito**: Meccanismi forti di autenticazione e controllo degli accessi:

**Autenticazione**:
- Autenticazione forte per tutti gli utenti
- AMF (Autenticazione Multi-Fattore) per: accesso remoto, account privilegiati, accesso a dati sensibili
- Politiche di complessità e rotazione delle password; blocco dell'account dopo tentativi falliti

**Controllo degli accessi**:
- Controllo degli accessi basato sui ruoli (RBAC)
- Principio del minimo privilegio
- Certificazione regolare degli accessi (almeno annuale)
- Provisioning e deprovisioning automatizzati
- Gestione degli accessi privilegiati (PAM) per gli amministratori

**Mappatura ISO 27001:2022**: A.5.15; A.5.16; A.5.17; A.5.18; A.8.2; A.8.3; A.8.5

## Margine 58: Separazione dei compiti

**Requisito**: Definire e implementare la separazione dei compiti per prevenire conflitti di interesse e ridurre il rischio di frode.

**Esempi di separazione critica**:
- Sviluppo vs. accesso alla produzione
- Iniziatore del cambiamento vs. approvatore del cambiamento
- Iniziatore del pagamento vs. approvatore del pagamento
- Amministratore della sicurezza vs. amministratore del sistema

**Aspettative FINMA**: Matrice dei compiti incompatibili documentata; monitoraggio automatizzato della separazione dei compiti ove possibile; segnalazione trimestrale delle violazioni alla direzione.

**Mappatura ISO 27001:2022**: A.5.15; A.5.18; A.8.2

## Margine 62: Crittografia

**Requisito**: Implementare la crittografia per proteggere i dati sensibili.

**Dati in transito**: TLS 1.2 minimo (TLS 1.3 preferito); suite di cifratura forti; gestione e rotazione dei certificati.

**Dati a riposo**: Crittografia completa del disco per gli endpoint; crittografia del database per i dati sensibili; crittografia dei backup.

**Gestione delle chiavi**: Sistema centralizzato di gestione delle chiavi; separazione della gestione delle chiavi dall'accesso ai dati; rotazione e ciclo di vita delle chiavi; archiviazione sicura delle chiavi (Hardware Security Module preferito).

**Standard di crittografia**: AES-256 per la crittografia simmetrica; RSA 2048 bit minimo o ECC 256 bit per la crittografia asimmetrica; SHA-256 minimo per l'hashing; nessun algoritmo obsoleto (DES, 3DES, MD5, SHA-1).

**Mappatura ISO 27001:2022**: A.8.24

---

# Margini 63-72 — Registrazione e monitoraggio

## Margini 63-65: Registrazione degli eventi di sicurezza

**Requisito**: Registrazione completa degli eventi rilevanti per la sicurezza: autenticazione e autorizzazione degli utenti, operazioni privilegiate, modifiche ai sistemi, incidenti e allarmi di sicurezza, accesso ai dati (in particolare ai dati sensibili).

**Contenuto dei registri**: Chi (identificazione utente), Cosa (azione eseguita), Quando (timestamp sincronizzato), Dove (sistema/applicazione/indirizzo IP), Risultato (successo o fallimento).

**Conservazione dei registri**: Registri di sicurezza: minimo 12 mesi (aspettativa FINMA); registri di audit: 10 anni (in base al tipo di dati).

**Mappatura ISO 27001:2022**: A.8.15; A.8.16

## Margini 66-68: Gestione centralizzata dei registri

**Requisito**: Raccolta, archiviazione e analisi centralizzate dei registri di sicurezza tramite SIEM o equivalente; raccolta in tempo reale da tutti i sistemi critici; protezione dell'integrità dei registri (registri immutabili).

**Capacità SIEM**: Aggregazione dei registri; correlazione e analisi; avvisi e notifiche; reporting e cruscotti; integrazione con la risposta agli incidenti.

**Esempi di implementazione**: Splunk Enterprise Security; Microsoft Sentinel; Elastic Security; IBM QRadar; LogRhythm.

## Margini 69-72: Monitoraggio in tempo reale e avvisi

**Requisito**: Monitoraggio continuo e avvisi in tempo reale; monitoraggio di sicurezza 24/7 (SOC o equivalente); avvisi automatizzati per eventi critici; procedure di escalation definite.

**Categorie di avvisi**:
- Critico: Risposta immediata richiesta (entro 15 minuti)
- Elevato: Risposta entro 1 ora
- Medio: Risposta entro 4 ore
- Basso: Risposta entro 24 ore

**Approcci di implementazione**: SOC interno (Centro delle Operazioni di Sicurezza); Managed Security Service Provider (MSSP); SOC co-gestito (modello ibrido).

**Mappatura ISO 27001:2022**: A.8.16; A.5.24; A.5.25

---

# Margini 73-87 — Continuità operativa e resilienza

## Margini 73-75: Analisi dell'impatto sull'attività (BIA)

**Requisito**: Condurre regolari analisi dell'impatto sull'attività per identificare i processi aziendali critici, definire gli obiettivi di tempo di ripristino (RTO) e di punto di ripristino (RPO), valutare l'impatto finanziario e operativo.

**Aspettative FINMA**: RTO per i processi critici: tipicamente 2-4 ore; RPO per i dati critici: tipicamente 15 minuti - 1 ora; revisione e aggiornamento annuali della BIA; approvazione degli obiettivi RTO/RPO da parte del consiglio di amministrazione.

**Mappatura ISO 27001:2022**: A.5.29; A.5.30

## Margini 76-80: Piani di continuità operativa (BCP)

**Requisito**: Piani di continuità operativa documentati e testati, inclusi procedure di risposta agli incidenti, struttura di gestione delle crisi, piani di comunicazione (interna ed esterna), siti di elaborazione alternativi, procedure di backup e ripristino dei dati.

**Mappatura ISO 27001:2022**: A.5.29; A.5.30; A.8.13; A.8.14

## Margini 81-84: Test e validazione

**Requisito**: Test regolari delle capacità di continuità operativa e ripristino di emergenza.

**Tipi di test**:
- **Esercitazione di discussione (tabletop)**: Basata su discussione, nessuna attivazione di sistemi
- **Test parziale**: Test di componenti specifici (es. failover del database)
- **Test DR completo**: Failover completo al sito alternativo
- **Test a sorpresa**: Attivazione non annunciata per testare la prontezza

**Aspettative FINMA**: Test DR completo annuale documentato e segnalato; risultati dei test esaminati dal consiglio; lacune identificate remediate entro un periodo definito.

## Margini 85-87: Gestione degli incidenti e segnalazione

**Requisito**: Processo formale di gestione degli incidenti con classificazione, livelli di gravità, procedure di escalation, requisiti di notifica alla FINMA, analisi delle cause profonde, insegnamenti appresi.

**Segnalazione degli incidenti alla FINMA**:
- **Immediatamente**: Incidenti maggiori che colpiscono i processi aziendali critici
- **Entro 24 ore**: Violazioni della sicurezza, fughe di dati, interruzioni significative
- **Post-incidente**: Rapporto dettagliato entro un periodo definito

**Mappatura ISO 27001:2022**: A.5.24; A.5.25; A.5.26; A.5.27; A.5.28

---

# Circolare FINMA 2008/7 — Esternalizzazione (banche)

## Requisiti chiave

**Valutazione del rischio**: Valutazione completa del rischio prima dell'esternalizzazione; valutazione delle capacità del fornitore di servizi; valutazione del rischio di concentrazione; considerazioni sulla residenza e sovranità dei dati.

**Requisiti contrattuali**: Definizione chiara dei servizi e SLA; obblighi di sicurezza e riservatezza; diritto di audit e accesso alle informazioni; restrizioni e approvazioni per i subappalti; clausole di protezione dei dati; requisiti di continuità operativa; disposizioni di uscita e transizione.

**Monitoraggio continuo**: Revisioni periodiche delle performance del fornitore; valutazioni e audit periodici della sicurezza; requisiti di segnalazione degli incidenti; attestazione annuale di conformità (es. SOC 2 Tipo II).

**Mappatura ISO 27001:2022**: A.5.19; A.5.20; A.5.21; A.5.22; A.5.23

---

# Mappatura ISO 27001:2022 — FINMA

## Matrice di mappatura dei controlli

| Requisito FINMA | Margine FINMA | Controllo ISO 27001:2022 | Priorità |
|-----------------|---------------|--------------------------|----------|
| Strategia di sicurezza | 50 | Clausola 5.2; A.5.1 | Critica |
| Organizzazione della sicurezza | 51 | Clausola 5.3; A.5.2 | Critica |
| Valutazione del rischio | 52 | Clausole 6.1.2, 6.1.3, 8.2, 8.3 | Critica |
| Politiche di sicurezza | 53 | A.5.1; A.5.10; A.5.12 | Critica |
| Sensibilizzazione e formazione | 54 | A.6.3 | Elevata |
| Rischio di terzi | 55 | A.5.19; A.5.20; A.5.21 | Critica |
| Autenticazione e controllo accessi | 56 | A.5.15; A.5.16; A.5.17; A.5.18; A.8.2; A.8.3; A.8.5 | Critica |
| Separazione dei compiti | 58 | A.5.15; A.5.18; A.8.2 | Critica |
| Crittografia | 62 | A.8.24 | Critica |
| Registrazione degli eventi | 63-65 | A.8.15 | Critica |
| Gestione centralizzata dei registri | 66-68 | A.8.15; A.8.16 | Critica |
| Monitoraggio e avvisi | 69-72 | A.8.16; A.5.24; A.5.25 | Critica |
| Analisi impatto sull'attività | 73-75 | A.5.29; A.5.30 | Critica |
| Piani di continuità | 76-80 | A.5.29; A.5.30; A.8.13; A.8.14 | Critica |
| Test BCP/DR | 81-84 | A.5.30 | Critica |
| Gestione degli incidenti | 85-87 | A.5.24-A.5.28 | Critica |
| Esternalizzazione (Circ. 2008/7) | N/A | A.5.19-A.5.23 | Critica |

---

# Lista di controllo per l'auto-valutazione della conformità FINMA

## Quadro di sicurezza delle informazioni (Margini 50-55)

| Requisito | Stato | Note |
|-----------|-------|------|
| Strategia di sicurezza documentata e approvata dal consiglio | ⬜ Sì ⬜ No ⬜ Parziale | |
| RSSI o ruolo equivalente istituito | ⬜ Sì ⬜ No | |
| Valutazione annuale del rischio di sicurezza condotta | ⬜ Sì ⬜ No | |
| Politiche di sicurezza complete documentate | ⬜ Sì ⬜ No ⬜ Parziale | |
| Formazione annuale di sensibilizzazione per tutto il personale | ⬜ Sì ⬜ No | |
| Processo di valutazione del rischio di terzi istituito | ⬜ Sì ⬜ No ⬜ Parziale | |

## Autenticazione e controllo degli accessi (Margine 56)

| Requisito | Stato | Note |
|-----------|-------|------|
| AMF implementata per l'accesso remoto | ⬜ Sì ⬜ No ⬜ Parziale | |
| AMF implementata per gli account privilegiati | ⬜ Sì ⬜ No ⬜ Parziale | |
| RBAC implementato | ⬜ Sì ⬜ No ⬜ Parziale | |
| Ricertificazione annuale degli accessi condotta | ⬜ Sì ⬜ No | |
| PAM implementato | ⬜ Sì ⬜ No ⬜ Parziale | |

## Separazione dei compiti (Margine 58)

| Requisito | Stato | Note |
|-----------|-------|------|
| Matrice SoD documentata | ⬜ Sì ⬜ No ⬜ Parziale | |
| Monitoraggio automatizzato SoD implementato | ⬜ Sì ⬜ No | |
| Violazioni SoD segnalate trimestralmente | ⬜ Sì ⬜ No | |
| Controlli compensativi documentati per conflitti SoD inevitabili | ⬜ Sì ⬜ No ⬜ Parziale | |

## Crittografia (Margine 62)

| Requisito | Stato | Note |
|-----------|-------|------|
| TLS 1.2+ per tutti i dati in transito | ⬜ Sì ⬜ No ⬜ Parziale | |
| Crittografia completa del disco per gli endpoint | ⬜ Sì ⬜ No ⬜ Parziale | |
| Crittografia del database per i dati sensibili | ⬜ Sì ⬜ No ⬜ Parziale | |
| Sistema centralizzato di gestione delle chiavi | ⬜ Sì ⬜ No | |
| Nessun algoritmo di crittografia obsoleto in uso | ⬜ Sì ⬜ No | |

## Registrazione e monitoraggio (Margini 63-72)

| Requisito | Stato | Note |
|-----------|-------|------|
| Registrazione completa degli eventi di sicurezza | ⬜ Sì ⬜ No ⬜ Parziale | |
| Conservazione dei registri ≥ 12 mesi | ⬜ Sì ⬜ No | |
| Gestione centralizzata dei registri (SIEM) | ⬜ Sì ⬜ No | |
| Monitoraggio di sicurezza 24/7 (SOC) | ⬜ Sì ⬜ No | |
| Avvisi in tempo reale per eventi critici | ⬜ Sì ⬜ No ⬜ Parziale | |

## Continuità operativa (Margini 73-87)

| Requisito | Stato | Note |
|-----------|-------|------|
| BIA condotta | ⬜ Sì ⬜ No | |
| RTO/RPO definiti e approvati dal consiglio | ⬜ Sì ⬜ No | |
| Piani di continuità documentati | ⬜ Sì ⬜ No ⬜ Parziale | |
| Test DR completo annuale condotto | ⬜ Sì ⬜ No | |
| Processo di segnalazione degli incidenti alla FINMA istituito | ⬜ Sì ⬜ No | |

## Esternalizzazione (Circolare FINMA 2008/7)

| Requisito | Stato | Note |
|-----------|-------|------|
| Accordi di esternalizzazione materiale notificati alla FINMA | ⬜ Sì ⬜ No ⬜ N/A | |
| Valutazioni del rischio dei fornitori condotte | ⬜ Sì ⬜ No ⬜ Parziale | |
| I contratti includono clausole di diritto di audit | ⬜ Sì ⬜ No ⬜ Parziale | |
| Rapporti SOC 2 Tipo II annuali ottenuti dai fornitori | ⬜ Sì ⬜ No ⬜ Parziale | |
| Strategie di uscita documentate per i fornitori critici | ⬜ Sì ⬜ No ⬜ Parziale | |

---

**FINE DEL DOCUMENTO DI RIFERIMENTO TECNICO**

*Questo riferimento tecnico supporta i potenziali requisiti di conformità FINMA come determinato in ISMS-POL-00.*

*Per le organizzazioni NON soggette alla vigilanza FINMA, questo documento è solo a scopo informativo e NON crea obblighi di conformità.*

<!-- QA_VERIFIED: 2026-04-03 -->

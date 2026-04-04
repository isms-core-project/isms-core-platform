<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.25-26-29-IT:framework:POL:a.8.25-26-29 -->
**ISMS-POL-A.8.25-26-29 — Quadro di sviluppo sicuro**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Quadro di sviluppo sicuro |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.25-26-29 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale (o in caso di significativi cambiamenti metodologici, aggiornamenti normativi, o incidenti di sicurezza gravi).

**Catena di approvazione**: RSSI → DT/VP Engineering → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.25-26-29-UG/TG; ISMS-POL-A.8.28 (Codifica sicura); ISMS-POL-A.8.30 (Sviluppo esternalizzato); ISMS-POL-A.8.31 (Separazione degli ambienti); ISMS-POL-A.8.32 (Gestione dei cambiamenti); ISO/IEC 27001:2022 Controlli A.8.25, A.8.26, A.8.29.

---

## Riepilogo esecutivo

Questa politica stabilisce il Quadro di sviluppo sicuro di [Organizzazione], implementando i Controlli A.8.26 (Requisiti di sicurezza delle applicazioni), A.8.25 (Ciclo di vita dello sviluppo sicuro) e A.8.29 (Test di sicurezza nello sviluppo e nell'accettazione) come quadro di sicurezza unificato.

**Perimetro**: Si applica a tutte le applicazioni sviluppate internamente; alle applicazioni acquisite che richiedono personalizzazione o integrazione; al codice di Infrastruttura-come-Codice (IaC) e alla gestione della configurazione; a tutti i modelli di sviluppo (sviluppo interno, esternalizzato, ibrido) e alle metodologie SDLC (Waterfall, Agile/Scrum, DevOps/DevSecOps, CI/CD).

**Allineamento normativo**: nLPD svizzera (protezione dei dati fin dalla progettazione); RGPD dell'UE Art. 25 (protezione dei dati fin dalla progettazione e per impostazione predefinita); ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sul controllo

**A.8.26 — Requisiti di sicurezza delle applicazioni**: I requisiti di sicurezza delle informazioni devono essere identificati, specificati e approvati durante lo sviluppo o l'acquisizione di applicazioni.

**A.8.25 — Ciclo di vita dello sviluppo sicuro**: Devono essere stabilite e applicate regole per lo sviluppo sicuro di software e sistemi.

**A.8.29 — Test di sicurezza nello sviluppo e nell'accettazione**: I processi di test della sicurezza devono essere definiti e implementati nel ciclo di vita dello sviluppo.

---

# Requisiti di sicurezza delle applicazioni (A.8.26)

## Identificazione dei requisiti di sicurezza

[Organizzazione] DEVE identificare e documentare i requisiti di sicurezza prima dello sviluppo.

**Valutazione della classificazione dei dati**: Le applicazioni DEVONO essere classificate in base alla sensibilità dei dati che gestiscono; la classificazione determina il livello di protezione richiesto; la re-classificazione DEVE avvenire quando il perimetro dell'applicazione cambia.

**Requisiti minimi obbligatori**: Per ogni applicazione, i requisiti DEVONO includere: autenticazione e autorizzazione; protezione dei dati (cifratura in transito e a riposo); registrazione e monitoraggio degli audit; gestione delle sessioni; gestione degli errori e delle eccezioni; input validation e output encoding; rilevamento e risposta agli incidenti.

**Requisiti aggiuntivi per applicazioni critiche**: Architettura Zero Trust; difesa in profondità; tolleranza ai guasti e alta disponibilità; autenticazione multi-fattore.

**Requisiti specifici per la protezione dei dati**: Per le applicazioni che gestiscono DCP: Privacy by Design (RGPD Art. 25); inventario della raccolta dati; meccanismi per i diritti degli interessati (accesso, rettifica, cancellazione); conservazione limitata dei dati.

---

# Ciclo di vita dello sviluppo sicuro (A.8.25)

## Security by Design

[Organizzazione] DEVE integrare la sicurezza nell'intero ciclo di vita dello sviluppo.

**Fase di pianificazione/requisiti**: Valutazione della classificazione dei dati; identificazione dei requisiti di sicurezza; valutazione del rischio dell'applicazione; pianificazione dei test di sicurezza.

**Fase di progettazione**: Threat modeling (STRIDE, OWASP Threat Dragon o equivalente) per applicazioni che gestiscono dati Riservati o superiori; revisione dell'architettura di sicurezza; progettazione della protezione dei dati; pianificazione della separazione degli ambienti (per ISMS-POL-A.8.31).

**Fase di sviluppo**: Linee guida di codifica sicura (per ISMS-POL-A.8.28); revisione del codice con focalizzazione sulla sicurezza; pipeline di sicurezza CI/CD (SAST, SCA automatizzati); nessun segreto hard-coded nel codice sorgente.

**Fase di test**: Test di sicurezza integrati per ogni iterazione/sprint; SAST, DAST, SCA come requisiti minimi; penetration testing per applicazioni ad alta criticità.

**Fase di dispiegamento**: Processi di dispiegamento sicuri (per ISMS-POL-A.8.32); verifica della configurazione sicura; documentazione della sicurezza completa.

**Fase di manutenzione**: Gestione delle vulnerabilità post-dispiegamento (per ISMS-POL-A.8.8); patch tempestive; revisioni periodiche della sicurezza.

## Strumenti e pratiche CI/CD

Le pipeline CI/CD DEVONO integrare controlli di sicurezza automatizzati:

| Controllo | Tipo | Frequenza minima |
|---------|------|-----------------|
| SAST (Static Application Security Testing) | Obbligatorio | Ogni commit/PR |
| SCA (Software Composition Analysis) — dipendenze | Obbligatorio | Ogni build |
| Scansione dei segreti | Obbligatorio | Ogni commit |
| DAST (Dynamic Application Security Testing) | Obbligatorio | Ogni release |
| SBOM (Software Bill of Materials) | Raccomandato | Ogni release |

---

# Test di sicurezza (A.8.29)

## Requisiti minimi di test

[Organizzazione] DEVE implementare test di sicurezza appropriati al rischio dell'applicazione.

**Classificazione del rischio dell'applicazione e requisiti di test**:

| Livello di rischio | Criteri | Requisiti di test |
|-----------------|---------|-----------------|
| **Critico** | Dati Riservati/Limitati; funzioni finanziarie critiche; infrastruttura IT critica | SAST + DAST + Penetration test annuale + revisione del codice di sicurezza |
| **Alto** | Dati Interni sensibili; accesso con privilegi; integrazioni di sistema | SAST + DAST + revisione del codice di sicurezza |
| **Medio** | Dati Interni standard; accesso utente standard | SAST + SCA + test di sicurezza di base |
| **Basso** | Solo dati pubblici; sistemi interni non critici | SCA + revisione della configurazione di sicurezza |

**Penetration testing**: Annuale per applicazioni Critiche; ogni 2 anni per applicazioni ad Alto rischio; da eseguirsi da team di sicurezza interni qualificati o da fornitori di test di penetrazione terzi accreditati; i risultati DEVONO essere rimediati per ISMS-POL-A.8.8 (Gestione delle vulnerabilità).

**Test di accettazione della sicurezza**: Criteri di accettazione della sicurezza DEVONO essere definiti prima del dispiegamento in produzione; nessun dispiegamento con vulnerabilità Critiche o Alte irrisolte; le eccezioni richiedono l'approvazione del RSSI con controlli compensativi documentati.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approvazione dei test di sicurezza; supervisione degli incidenti di sicurezza delle applicazioni |
| **DT/VP Engineering** | Responsabilità per lo standard SDLC sicuro; disponibilità delle risorse per le attività di sicurezza |
| **Application Security Lead** | Definizione degli standard di sicurezza; revisione del design e del codice; supervisione dei test |
| **Team di sviluppo** | Implementazione dei requisiti di sicurezza; partecipazione alle revisioni; rimedio delle vulnerabilità |
| **Team di test** | Esecuzione dei test di sicurezza; documentazione dei risultati |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DT** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce il quadro di sviluppo sicuro. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.25-26-29 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->

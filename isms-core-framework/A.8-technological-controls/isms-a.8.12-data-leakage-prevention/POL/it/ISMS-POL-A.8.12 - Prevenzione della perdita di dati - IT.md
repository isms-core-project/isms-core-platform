<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.12-IT:framework:POL:a.8.12 -->
**ISMS-POL-A.8.12 — Prevenzione della perdita di dati (DLP)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Prevenzione della perdita di dati |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.12 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → RPD/Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.12.1–4-UG/TG; ISO/IEC 27001:2022 Controllo A.8.12; nLPD svizzera; RGPD dell'UE.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di Prevenzione della perdita di dati (DLP) per proteggere le informazioni sensibili dalla divulgazione non autorizzata, conformemente al Controllo A.8.12 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutti i dati sensibili (DCP, dati finanziari, proprietà intellettuale, segreti commerciali) su tutti i canali di egresso (email, web, endpoint, stampa, archiviazione cloud, dispositivi rimovibili) e a tutto il personale e le terze parti che gestiscono informazioni organizzative.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale).

---

# Controllo ISO/IEC 27001:2022 A.8.12

> *Misure devono essere applicate per rilevare e prevenire la divulgazione non autorizzata di informazioni da parte di sistemi e dispositivi.*

**Obiettivo del controllo**: Prevenire la perdita di dati non autorizzata attraverso il rilevamento tecnico, il blocco e i controlli di risposta su tutti i canali di egresso.

---

# Enunciati di politica

## Ambito della protezione DLP

[Organizzazione] DEVE implementare controlli DLP per proteggere le informazioni sensibili dalla divulgazione non autorizzata.

**Categorie di dati protetti**: DCP (tutte le categorie, comprese le categorie speciali); dati finanziari (dati delle carte di pagamento, informazioni bancarie); proprietà intellettuale e segreti commerciali; credenziali e materiale crittografico; informazioni aziendali riservate.

**Canali di egresso monitorati**:

| Canale | Requisito di copertura |
|--------|----------------------|
| Email (in uscita) | Ispezione obbligatoria del contenuto |
| Web/HTTP/HTTPS | Ispezione SSL obbligatoria |
| Endpoint (copia file, stampa, USB) | Monitoraggio obbligatorio degli endpoint |
| Servizi cloud/SaaS | Integrazione CASB raccomandata |
| Trasferimento di file (SFTP, SCP, FTP) | Monitoraggio obbligatorio |

## Modalità di applicazione DLP

**Modalità monitor** (rilevamento senza blocco): Registra i potenziali eventi di perdita di dati; avvisa il personale di sicurezza e l'utente; utilizzata per l'onboarding iniziale e i dati a basso rischio.

**Modalità blocca** (prevenzione attiva): Blocca il trasferimento non autorizzato dei dati; notifica l'utente con il motivo del blocco; richiede l'approvazione o la giustificazione per procedere; obbligatoria per i dati RISERVATI e le categorie speciali di DCP.

**Selezione della modalità**: La modalità blocca DEVE essere attivata entro 90 giorni dall'implementazione DLP per i canali che gestiscono dati RISERVATI; il RSSI può approvare la modalità monitor estesa con documentazione giustificativa.

## Copertura e configurazione

**Obiettivi di copertura**: ≥90% dei canali di egresso identificati monitorati attivamente; 100% di copertura per i canali che gestiscono dati RISERVATI.

**Gestione dei falsi positivi**: Revisione mensile dei tassi di falsi positivi; il tasso obiettivo di falsi positivi è <5%; la messa a punto delle regole deve essere approvata dal RSSI.

## Risposta agli incidenti DLP

**Classificazione della gravità**:

| Gravità | Descrizione | Tempo di risposta |
|---------|-------------|------------------|
| **Critico** | DCP di massa, dati finanziari, proprietà intellettuale critica | Immediato (entro 1 ora) |
| **Alto** | DCP individuali, dati aziendali riservati | Entro 4 ore |
| **Medio** | Dati interni, violazioni minori della policy | Entro 24 ore |
| **Basso** | Avvisi di conformità, tendenze | Revisione settimanale |

**Escalation**: Gli incidenti DLP Critici DEVONO essere segnalati al RSSI e al RPD entro 1 ora; le violazioni dei dati che coinvolgono DCP DEVONO seguire le procedure di notifica delle violazioni per ISMS-POL-A.5.34.

## Trasparenza e privacy degli utenti

[Organizzazione] DEVE comunicare le capacità DLP ai dipendenti: informativa sulla privacy che descrive il monitoraggio DLP; inclusione nella policy di utilizzo accettabile; esclusione dal monitoraggio delle comunicazioni personali dove tecnicamente fattibile.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approva le configurazioni DLP; supervisione degli incidenti |
| **RPD** | Supervisione DLP relativa ai DCP; revisione della privacy delle configurazioni |
| **Operazioni di Sicurezza** | Monitoring degli avvisi DLP; risposta agli incidenti; messa a punto delle regole |
| **IT** | Implementazione e manutenzione dell'infrastruttura DLP |
| **Tutti gli utenti** | Rispettare le politiche sulla gestione dei dati; non tentare di aggirare i controlli DLP |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **RPD** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti DLP. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.12 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->

<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S6-IT:framework:POL:a.5.19-23-s6 -->
**ISMS-POL-A.5.19-23-S6 — Metodologia di valutazione e automazione**
**Sicurezza dei servizi cloud — Approccio di ingegneria di sistema**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Metodologia di valutazione e automazione |
| **Tipo di documento** | Sezione di politica |
| **Identificativo del documento** | ISMS-POL-A.5.19-23-S6 |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.5.19-23; ISMS-IMP-A.5.19-23.S1-S4; Script Python in 50_scripts-excel/; ISO/IEC 27001:2022 Clausola 9.2

---

# Riepilogo esecutivo

## Scopo

Il presente documento definisce l'**approccio di ingegneria di sistema (IS)** per la valutazione della conformità alla sicurezza dei servizi cloud. Utilizziamo **classeur Excel generati da Python** che garantiscono: valutazioni riproducibili (struttura identica ogni trimestre); metriche di conformità quantitative (87,3% conforme vs. «generalmente conforme»); verifica basata su prove; cruscotti trasparenti calcolati automaticamente.

**Principio fondamentale**: «Se non si può generare, non si potrà mantenere». I fogli di calcolo manuali si deteriorano — le formule si rompono, le convalide scompaiono e si creano incoerenze tra cicli di valutazione. Gli strumenti di valutazione devono essere generati in modo programmatico.

**Approccio di ingegneria di sistema:**
```
1. Eseguire il generatore Python → ISMS_REG_A523_1_Inventory.xlsx
2. Gli acquisti completano l'elenco dei servizi con prove
3. Il cruscotto calcola automaticamente: «45/78 servizi conformi (57,7%)»
4. Il report delle lacune identifica: «33 servizi senza AMF»
```

---

# Architettura del quadro a cinque livelli

```
Livello 1: POLITICA       → ISMS-POL-A.5.19-23 + S5 + S6
Livello 2: SPECIFICHE     → ISMS-IMP-A.5.19-23.S1-S4 (Markdown)
Livello 3: IMPLEMENTAZIONE → Script Python di generazione
Livello 4: REVISIONE      → Cruscotti integrati nei classeur
Livello 5: VALIDAZIONE    → Approvazione RSSI e pista di audit
```

## Struttura dei classeur

| Scheda | Scopo | Compilato da | Frequenza |
|--------|-------|-------------|-----------|
| Istruzioni e legenda | Manuale d'uso + codici di stato | Generato automaticamente | N/A |
| Schede di valutazione (2-6) | Liste di controllo per dominio | Parti interessate | Trimestrale |
| Cruscotto | % conformità per dominio | Pilotato da formule | Automatico |
| Registro delle prove | Link ai documenti | Parti interessate | Trimestrale |
| Validazione | Approvazione RSSI + date | Direzione | Trimestrale |

---

# Specifiche dei classeur

## Classeur 1: Inventario e classificazione dei servizi cloud

**Nome file**: `ISMS_REG_A523_1_Inventory_AAAAMMGG.xlsx`
**Script**: `generate_reg_a523_1_inventory.py`
**Parti interessate**: Operazioni IT, Acquisti, Finanza

**Schede**: Istruzioni; Servizi SaaS; Servizi IaaS/PaaS; Servizi di sicurezza cloud; Servizi di storage cloud; Mappatura classificazione dati; Valutazione criticità; Cruscotto; Prove; Validazione.

**Colonne di base (A–Q — standard per tutte le valutazioni cloud)**:

| Col | Campo | Note |
|-----|-------|------|
| A | Nome del servizio cloud | |
| B | Tipo (SaaS/IaaS/PaaS/Sicurezza/Storage) | Lista a discesa |
| C | Nome del fornitore | |
| D | Criticità (Critico/Alto/Medio/Basso) | Lista a discesa |
| E | Classificazione dati (Limitato/Riservato/Interno/Pubblico) | Lista a discesa |
| F | Residenza dei dati (Svizzera/UE/USA/Globale) | Lista a discesa |
| G | Stato contratto (Attivo/Rinnovo/Scaduto) | Lista a discesa |
| H | Stato (✅ Conforme / ⚠️ Parziale / ❌ Non conforme) | Lista a discesa |
| I | Posizione delle prove | |
| J | Descrizione della lacuna | |
| K | Correzione necessaria (Sì/No) | Lista a discesa |
| L | ID eccezione | |
| M | ID rischio | |
| N | Misure compensative | |
| O | Proprietario del servizio | |
| P | Data obiettivo di correzione | Data |
| Q | Impatto budget (Alto/Medio/Basso/Nessuno) | Lista a discesa |

**Colonne estese inventario (R–X)**: Costo mensile; Valore contratto annuale; Numero utenti con licenza; Numero integrazioni; Servizio di backup disponibile (Sì/No); Facilità di uscita (Facile/Medio/Difficile/Sconosciuto); Data ultima revisione inventario.

## Classeur 2: Due diligence e contratti con i fornitori

**Nome file**: `ISMS_REG_A523_2_DueDiligence_AAAAMMGG.xlsx`
**Script**: `generate_reg_a523_2_vendor_dd.py`

**Scopo**: Monitorare le certificazioni di sicurezza dei fornitori, le condizioni contrattuali, gli SLA e i diritti di audit.

**Colonne estese (R–X)**: Certificazione ISO 27001 (Sì/No + N. cert.); Report SOC 2 Tipo II (Sì/No); Data rinnovo contratto; SLA disponibilità %; Clausola diritto di audit (Sì/No); Clausola portabilità dati (Sì/No); Supporto forense/risposta agli incidenti (Sì/No/Limitato).

## Classeur 3: Configurazione e dispiegamento sicuri

**Nome file**: `ISMS_REG_A523_3_Configuration_AAAAMMGG.xlsx`
**Script**: `generate_reg_a523_3_secure_config.py`

**Scopo**: Valutare la conformità al riferimento di configurazione di sicurezza per i servizi cloud dispiegati.

**Colonne estese (R–X)**: AMF abilitata (Sì/No/Parziale); Cifratura a riposo (Sì/No); Cifratura in transito (TLS 1.3/TLS 1.2/Debole); Registrazione centralizzata (Sì/No/Parziale); Integrazione SSO (Sì/No/Pianificata); Etichette classificazione applicate (Sì/No/Parziale); Riferimento configurazione documentato (Sì/No).

## Classeur 4: Governance continua e gestione del rischio

**Nome file**: `ISMS_REG_A523_4_Governance_AAAAMMGG.xlsx`
**Script**: `generate_reg_a523_4_governance.py`

**Scopo**: Monitorare la governance continua, i rischi dei fornitori, la continuità operativa e la gestione dei cambiamenti.

**Colonne estese (R–X)**: Formazione sicurezza completata (Sì/No + Data); Data ultima revisione sicurezza; Piano di risposta agli incidenti testato (Sì/No/Pianificato); Rischio di vendor lock-in (Alto/Medio/Basso); Piano BCP/DRP esistente (Sì/No); Data ultimo test BCP/DRP; Processo di gestione dei cambiamenti (Sì/No).

---

# Architettura degli script Python

## Struttura standard degli script

```python
# Sezione 1: Creazione del classeur e stili
def create_workbook() -> Workbook:
    """Crea tutte le schede secondo la specifica."""
def setup_styles() -> dict:
    """Definisce colori, caratteri, bordi (NUOVI oggetti per cella!)."""

# Sezione 2: Definizioni delle colonne
def get_base_cloud_columns() -> dict:
    """Restituisce le 17 colonne standard (A–Q)."""
def get_extended_columns_inventory() -> dict:
    """Restituisce le colonne R–X specifiche del dominio."""

# Sezione 3: Convalide
def create_base_validations(ws) -> dict:
    """Crea le convalide a lista a discesa per i campi standard."""

# Sezione 4: Costruttore generico di schede
def create_assessment_sheet(ws, styles, section_title, policy_ref,
                           question, sheet_type):
    """Costruttore universale — UNA sola funzione crea TUTTE le schede."""

# Sezione 5: Esecuzione principale
def main():
    """Orchestra la generazione del classeur."""
```

## Nota di implementazione critica — Oggetti di stile

```python
# ❌ DA EVITARE — oggetti condivisi possono causare problemi
border = Border(left=Side(style="thin"), ...)
cell1.border = border  # Riferimento 1
cell2.border = border  # Riferimento 2

# ✅ RACCOMANDATO — un nuovo oggetto per cella
def apply_border(cell):
    cell.border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin")
    )
```

---

# Ciclo di valutazione trimestrale

```
Settimana 1: GENERAZIONE
├─ Ingegneria della sicurezza esegue i generatori Python
├─ Revisione qualità dei classeur generati
└─ Distribuzione alle parti interessate con istruzioni

Settimane 2-3: VALUTAZIONE
├─ Operazioni IT completa inventario e configurazione
├─ Acquisti aggiorna i dati dei fornitori e contrattuali
├─ Legale rivede le clausole di conformità e di uscita
└─ Prove raccolte (contratti, certificazioni, screenshot)

Settimana 4: REVISIONE
├─ RSI rivede le valutazioni completate
├─ Analisi delle lacune effettuata
├─ Priorità di correzione assegnate
└─ Approvazione del RSSI ottenuta

Settimana 5: INTEGRAZIONE
└─ Revisione cruscotti e sintesi esecutiva
```

## Trigger di valutazione ad hoc

Effettuare valutazioni al di fuori del ciclo trimestrale in caso di: integrazione di un nuovo servizio cloud (Classeur 1 + 2); modifiche significative della configurazione (Classeur 3); incidenti di sicurezza (Classeur 4); rinnovi di contratti (Classeur 2); preparazione di audit (tutti i classeur).

---

# Guida alle parti interessate

## Chi compila cosa

| Classeur | Principale | Secondario | Terziario |
|---------|-----------|-----------|---------|
| 1. Inventario | Operazioni IT | Acquisti | Finanza |
| 2. Due diligence | Acquisti | Legale | Conformità |
| 3. Configurazione | Sicurezza IT | DevOps | Amministratori di sistema |
| 4. Governance | Gestione del rischio | RSI | Direzione IT |

## Istruzioni di compilazione

Per ogni scheda di valutazione: compilare le **celle gialle** con i propri dati; usare i **menu a discesa** (non inserire testo libero); fornire la **posizione delle prove** (percorso file, link, ID documento); se Stato = Parziale/Non conforme: compilare la Descrizione della lacuna, indicare Correzione necessaria = Sì, assegnare un Responsabile, definire una Data obiettivo; aggiornare il **Registro delle prove** con i documenti giustificativi.

**Esempi di prove accettabili**: PDF di contratti; certificazioni di sicurezza (ISO 27001, report SOC 2); screenshot delle configurazioni (impostazioni AMF, cifratura); report di audit (test di penetrazione, analisi delle vulnerabilità).

## Criteri di validazione della valutazione

Una valutazione è pronta per la validazione RSI/RSSI solo quando:

| Criterio | Requisito |
|----------|-----------|
| Colonne obbligatorie complete | 100% delle colonne A–Q compilate; le voci N/A richiedono giustificazione |
| Posizione delle prove specificata | Ogni riga non-N/A ha prove specifiche — «da fornire» non è accettabile |
| Descrizioni delle lacune accurate | Tutte le righe Parziali/Non conformi hanno descrizione specifica; testi generici non accettati |
| Date di correzione realistiche | Date di calendario ≤ 12 mesi nel futuro; non «APPENA POSSIBILE» o vuoto |
| Responsabile assegnato | Persona nominata specifica (non un team o una qualifica) |
| Verifica a campione superata | RSI effettua controllo su 10% casuale delle righe (min. 5 righe) |

**Formati minimi accettabili delle prove**:

| Tipo di prova | Accettabile | Non accettabile |
|--------------|-----------|----------------|
| Contratto | PDF firmato, link SharePoint, ID contratto | Thread email, conferma verbale |
| Certificazione | PDF del certificato corrente o link al registro pubblico | Certificato scaduto, auto-dichiarazione |
| Configurazione | Screenshot con data e nome del sistema visibili | Descrizione senza prova |
| Audit/test di penetrazione | Report firmato da organismo accreditato | Solo diapositiva di sintesi |
| Formazione | Report LMS con nomi e date | «La formazione è stata erogata» |

---

# Integrazione dei cruscotti

## Aggregazione basata su formule

```excel
# Contare i servizi conformi dal classeur Inventario
=COUNTIF('[ISMS_REG_A523_1_Inventory_20260115.xlsx]2. Servizi SaaS'!$H$8:$H$50,"✅*")

# Calcolare la percentuale di conformità
=IF((B4-F4)=0,"0%",ROUND(C4/(B4-F4)*100,1)&"%")
```

**Tabella di sintesi della conformità (esempio)**:

| Dominio di valutazione | Totale | Conforme | Parziale | Non conforme | % Conformità |
|------------------------|--------|----------|----------|-------------|-------------|
| Inventario | 78 | 45 | 18 | 15 | 57,7% |
| Due diligence | 78 | 62 | 10 | 6 | 79,5% |
| Configurazione | 156 | 98 | 35 | 23 | 63,2% |
| Governance | 78 | 51 | 20 | 7 | 65,4% |
| **TOTALE** | **390** | **256** | **83** | **51** | **65,6%** |

---

# Riferimenti

**Livello politica**: ISMS-POL-A.5.19-23; ISMS-POL-A.5.19-23-S5.

**Specifiche di valutazione**: ISMS-IMP-A.5.19-23.S1–S4.

**Norme esterne**: ISO/IEC 27001:2022 Controllo A.5.23; ISO/IEC 27017:2026; ISO/IEC 27018:2025; NIST SP 800-144; CSA Cloud Controls Matrix (CCM) v4.

---

*«Il primo principio è non ingannare se stessi — e voi siete la persona più facile da ingannare.» — Richard Feynman*

*Traduzione SGSI: La conformità basata su prove previene il cloud washing!*

<!-- QA_VERIFIED: 2026-04-03 -->
